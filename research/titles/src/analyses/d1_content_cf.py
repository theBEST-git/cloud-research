"""WP5 / D1-H1b, H1c: content counterfactuals for the NAME rise (R1-R6), fixed and rolling designs, placebo window,
new-topic placebo, V4 leakage diagnostics.

Representations (PLAN D1; L2 logit, C chosen by 5-fold CV (log loss) inside each training window):
    R1  name-masked abstract TF-IDF, 1-2-grams (features_v2.mask_abstract_lower: lead removed, lowercase tokens only;
        min_df 5, max_df 0.5, 50k features, sublinear tf)                                  [primary, name-masked]
    R2  keyword TF-IDF on normalized_keywords_json (each keyword phrase is one token)       [lower]
    R3  bge-small embeddings of R3-masked abstracts (outputs/topics/emb_masked_bge.npy)     [name-masked]
    R4  bge-small embeddings of unmasked abstracts (cache)                                  [upper, leaky]
    R5  R1 vocabulary minus the frozen rhetorical-move n-grams (lexicons.json)              [name-masked, genre-stripped]
    R6  topic100 one-hot (MiniLM) + llm_topic                                               [coarse]
    R6b topic100 one-hot (bge) + llm_topic_bge                                              [coarse, replication]
    R1u unmasked abstract TF-IDF (all tokens, lead kept): V4 masked-vs-unmasked diagnostic only

Designs:
    rolling  train y-3..y-1, test y (2019..2026); intercept recalibrated so cross-fitted (OOF) predictions of
             year y-1 match obs_{y-1}; u_y = obs_y - p_hat_y                                [primary for H1c]
    fixed    train 2021-23, recalibrate to 2023 (OOF), predict 2024-26
    placebo  train 2018-20, recalibrate to 2020 (OOF), predict 2021-23

Stages (each well under 20 min with 2 threads):
    python -m analyses.d1_content_cf fit reps=R1,R5,R6,R6b   U pool, NAME primary, listed reps, all designs
    python -m analyses.d1_content_cf fit reps=R4,R2,R1u      (split in two processes to stay under ~15 min each)
    python -m analyses.d1_content_cf fit variants    R1 on NA / non-LLM pools and strict/loose/compound outcomes
    python -m analyses.d1_content_cf fit r3          R3 (needs outputs/topics/emb_masked_bge.npy)
    python -m analyses.d1_content_cf summarise       bootstraps, tables, content_cf.json
    python -m analyses.d1_content_cf refit_boot [B]  refit bootstrap of R1 rolling (model uncertainty for H1c)
"""
from __future__ import annotations

import json
import sys
import zlib
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.special import expit, logit as _logit

from analyses import _core as C
from analyses.features_v2 import lead_survives, lexicon, mask_abstract_lower

OUTDIR = C.OUT / "d1_break"
SCORES = OUTDIR / "scores"
CACHE_DIR = OUTDIR / "cache"
OUTCOMES = {"primary": "name_primary", "strict": "name_strict", "loose": "name_loose", "compound": "name_compound"}
GRID_SPARSE = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
GRID_DENSE = (0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0)
GRID_ONEHOT = (0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0)
GRID_KW = (0.03, 0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0)  # keywords: optimum sits below the text grid
REP_INFO = {
    "R1": ("name-masked abstract TF-IDF", "masked"),
    "R2": ("keyword TF-IDF", "lower"),
    "R3": ("bge, name-masked abstract", "masked"),
    "R4": ("bge, unmasked abstract", "upper (leaky)"),
    "R5": ("R1 minus rhetorical moves", "masked"),
    "R6": ("topic100 (MiniLM) + llm_topic", "coarse"),
    "R6b": ("topic100 (bge) + llm_topic_bge", "coarse"),
    "R1u": ("unmasked abstract TF-IDF (V4 diagnostic)", "diagnostic"),
    "R1@0.5": ("R1 at the pilot's fixed C = 0.5 (sensitivity, not CV-chosen)", "sensitivity"),
    "R1n": ("R1 minus naming-announcement/LaTeX-format tokens (exploratory V4 diagnostic)", "diagnostic"),
}
# Exploratory (not pre-registered) V4 follow-up: abstract tokens that announce a coined name or typeset it.
NAMING_TOKENS = ["named", "called", "dubbed", "termed", "coined", "textbf", "textsc", "textit", "texttt", "emph",
                 "mathtt", "mathsf"]
MASKED_REPS = ("R1", "R3", "R5")
PRE_Y, POST_Y = (2019, 2020, 2021, 2022, 2023), (2024, 2025, 2026)


# ------------------------------------------------------------------------------------------------
# data
# ------------------------------------------------------------------------------------------------
def load_frame() -> pd.DataFrame:
    df = C.load_analysis_frame(
        feature_cols=list(OUTCOMES.values()) + ["lead_segment", "lead_raw"],
        universe_cols=["submission_id", "year", "abstract", "normalized_keywords_json", "topic100", "llm_topic",
                       "non_llm", "NA", "emb_row", "log_authors", "declared_name_count", "share_new_authors"],
        with_bge_topics=True)
    for c in list(OUTCOMES.values()) + ["llm_topic", "non_llm", "NA", "llm_topic_bge"]:
        df[c] = df[c].astype(int)
    return df.reset_index(drop=True)


def r1_texts(df: pd.DataFrame) -> np.ndarray:
    p = CACHE_DIR / "r1_text.parquet"
    if p.exists():
        t = pd.read_parquet(p)
        if len(t) == len(df) and (t.submission_id.to_numpy() == df.submission_id.to_numpy()).all():
            return t.text.to_numpy(dtype=object)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    txt = [mask_abstract_lower(a, l) for a, l in zip(df.abstract, df.lead_segment.fillna(""))]
    pd.DataFrame({"submission_id": df.submission_id, "text": txt}).to_parquet(p, index=False)
    return np.array(txt, dtype=object)


def kw_lists(df: pd.DataFrame) -> np.ndarray:
    out = []
    for x in df.normalized_keywords_json.fillna("[]"):
        try:
            v = json.loads(x)
        except Exception:
            v = []
        out.append([str(k).strip().lower() for k in v if str(k).strip()] if isinstance(v, list) else [])
    return np.array(out, dtype=object)


def r5_excluded(feature: str, moves: list[list[str]]) -> bool:
    toks = feature.split()
    for m in moves:
        k = len(m)
        for i in range(len(toks) - k + 1):
            if toks[i:i + k] == m:
                return True
    return False


class Reps:
    """Feature builders per representation. Text vectorisers are fitted on the training rows only."""

    def __init__(self, df: pd.DataFrame, need=("R1", "R1u", "R2", "R4", "R5", "R6", "R6b")):
        self.df = df
        self.texts = {}
        need = {n.split("@")[0] for n in need}
        if {"R1", "R5", "R1n"} & set(need):
            self.texts["R1"] = r1_texts(df)
        if "R1u" in need:
            self.texts["R1u"] = df.abstract.fillna("").to_numpy(dtype=object)
        if "R2" in need:
            self.kw = kw_lists(df)
        if "R4" in need:
            self.E4 = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
        if "R3" in need:
            E3, found = C.load_masked_embedding(df)
            self.E3, self.found3 = E3, found
        self.moves = [m.split() for m in lexicon()["rhetorical_moves_R5"]["core"]]

    def available(self, rep: str) -> np.ndarray:
        if rep.split("@")[0] == "R3":
            return self.found3
        return np.ones(len(self.df), dtype=bool)

    def grid(self, rep):
        if "@" in rep:  # fixed-C sensitivity, e.g. 'R1@0.5'
            return (float(rep.split("@")[1]),)
        return {"R3": GRID_DENSE, "R4": GRID_DENSE, "R6": GRID_ONEHOT, "R6b": GRID_ONEHOT, "R2": GRID_KW}.get(rep, GRID_SPARSE)

    def build(self, rep: str, tr: np.ndarray, te: np.ndarray):
        """Return X_train, X_test, info. tr/te are integer row indices."""
        from scipy import sparse
        from sklearn.feature_extraction.text import TfidfVectorizer
        info = {}
        rep = rep.split("@")[0]
        if rep in ("R1", "R5", "R1u", "R1n"):
            docs = self.texts["R1" if rep in ("R5", "R1n") else rep]
            vec = TfidfVectorizer(min_df=5, max_df=0.5, ngram_range=(1, 2), sublinear_tf=True, max_features=50000,
                                  dtype=np.float32)
            Xtr = vec.fit_transform(docs[tr])
            if rep in ("R5", "R1n"):
                feats = vec.get_feature_names_out()
                excl = self.moves if rep == "R5" else [[t] for t in NAMING_TOKENS]
                kept = [f for f in feats if not r5_excluded(f, excl)]
                info["r5_removed"] = int(len(feats) - len(kept))
                vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, vocabulary=kept, dtype=np.float32)
                Xtr = vec.fit_transform(docs[tr])
            Xte = vec.transform(docs[te])
            info["n_features"] = int(Xtr.shape[1])
            info["vectorizer"] = vec
        elif rep == "R2":
            vec = TfidfVectorizer(analyzer=lambda x: x, min_df=5, max_df=0.5, sublinear_tf=True, max_features=50000,
                                  dtype=np.float32)
            Xtr = vec.fit_transform(self.kw[tr])
            Xte = vec.transform(self.kw[te])
            info["n_features"] = int(Xtr.shape[1])
        elif rep in ("R3", "R4"):
            E = self.E3 if rep == "R3" else self.E4
            Xtr, Xte = E[tr], E[te]
            info["n_features"] = int(E.shape[1])
        elif rep in ("R6", "R6b"):
            tcol, lcol = ("topic100", "llm_topic") if rep == "R6" else ("topic100_bge", "llm_topic_bge")
            k = self.df[tcol].to_numpy().astype(int)
            K = int(k.max()) + 1
            def oh(idx):
                M = sparse.csr_matrix((np.ones(len(idx)), (np.arange(len(idx)), k[idx])), shape=(len(idx), K))
                return sparse.hstack([M, sparse.csr_matrix(self.df[lcol].to_numpy()[idx][:, None].astype(float))]).tocsr()
            Xtr, Xte = oh(tr), oh(te)
            info["n_features"] = K + 1
        else:
            raise KeyError(rep)
        return Xtr, Xte, info


# ------------------------------------------------------------------------------------------------
# model fitting
# ------------------------------------------------------------------------------------------------
def _lr(Cv, rep):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression(C=Cv, max_iter=5000, tol=1e-5)


def cv_select(X, y, grid, rep, seed=0, sample_weight=None, folds=None):
    """5-fold CV over the C grid (log loss); returns best C, OOF decision scores at best C, log-loss table."""
    from sklearn.model_selection import StratifiedKFold
    n = len(y)
    if folds is None:
        folds = list(StratifiedKFold(5, shuffle=True, random_state=seed).split(np.zeros(n), y))
    oof = {Cv: np.zeros(n) for Cv in grid}
    for trf, vaf in folds:
        for Cv in grid:
            sw = None if sample_weight is None else sample_weight[trf]
            m = _lr(Cv, rep).fit(X[trf], y[trf], sample_weight=sw)
            oof[Cv][vaf] = m.decision_function(X[vaf])
    ll = {}
    for Cv in grid:
        p = np.clip(expit(oof[Cv]), 1e-9, 1 - 1e-9)
        w = np.ones(n) if sample_weight is None else sample_weight
        ll[Cv] = float(-(w * (y * np.log(p) + (1 - y) * np.log(1 - p))).sum() / w.sum())
    best = min(ll, key=ll.get)
    return best, oof[best], ll


def windows(design: str):
    if design == "rolling":
        return [dict(name=f"roll{y}", train=tuple(range(y - 3, y)), calib=y - 1, test=(y,)) for y in range(2019, 2027)]
    if design == "fixed":
        return [dict(name="fixed", train=(2021, 2022, 2023), calib=2023, test=POST_Y)]
    if design == "placebo":
        return [dict(name="placebo", train=(2018, 2019, 2020), calib=2020, test=(2021, 2022, 2023))]
    raise KeyError(design)


def run_fit(R: Reps, rep: str, design: str, pop: str = "U", outcomes=("primary",), keep_model=False):
    """Fit one representation x design x population for one or more outcomes (features shared).
    Writes scores/<rep>__<pop>__<outcome>__<design>.parquet and a meta json; returns meta."""
    df = R.df
    yrs = df.year.to_numpy()
    popm = np.ones(len(df), bool) if pop == "U" else (df[pop].to_numpy() == 1)
    popm &= R.available(rep)
    metas = {o: {"rep": rep, "design": design, "pop": pop, "outcome": o, "windows": {}} for o in outcomes}
    parts = {o: [] for o in outcomes}
    models = {}
    for w in windows(design):
        tr = np.where(popm & np.isin(yrs, w["train"]))[0]
        te = np.where(popm & np.isin(yrs, w["test"]))[0]
        if len(tr) == 0 or len(te) == 0:
            continue
        t0 = time.time()
        Xtr, Xte, info = R.build(rep, tr, te)
        for o in outcomes:
            y = df[OUTCOMES[o]].to_numpy()
            ytr = y[tr]
            best, oof, ll = cv_select(Xtr, ytr, R.grid(rep), rep)
            m = _lr(best, rep).fit(Xtr, ytr)
            s_te = m.decision_function(Xte)
            calib_rows = yrs[tr] == w["calib"]
            parts[o].append(pd.DataFrame({"window": w["name"], "role": "calib", "row": tr[calib_rows],
                                          "year": yrs[tr][calib_rows], "y": ytr[calib_rows],
                                          "score": oof[calib_rows]}))
            parts[o].append(pd.DataFrame({"window": w["name"], "role": "test", "row": te, "year": yrs[te],
                                          "y": y[te], "score": s_te}))
            # also keep OOF scores for all training rows (for training-window diagnostics)
            parts[o].append(pd.DataFrame({"window": w["name"], "role": "train_oof", "row": tr, "year": yrs[tr],
                                          "y": ytr, "score": oof}))
            grid = R.grid(rep)
            metas[o]["windows"][w["name"]] = {
                "train_years": list(w["train"]), "calib_year": w["calib"], "test_years": list(w["test"]),
                "n_train": int(len(tr)), "n_test": int(len(te)), "C": best,
                "C_at_grid_edge": bool(best in (grid[0], grid[-1])),
                "cv_logloss": {str(k): v for k, v in ll.items()},
                "n_features": info.get("n_features"), "r5_removed": info.get("r5_removed"),
                "seconds": round(time.time() - t0, 1)}
            if keep_model:
                models[(w["name"], o)] = (m, info)
        print(f"  {rep} {design} {pop} {w['name']}: n_tr={len(tr)} n_te={len(te)} "
              f"C={[metas[o]['windows'][w['name']]['C'] for o in outcomes]} {time.time() - t0:.1f}s", flush=True)
    SCORES.mkdir(parents=True, exist_ok=True)
    for o in outcomes:
        S = pd.concat(parts[o], ignore_index=True)
        S["submission_id"] = df.submission_id.to_numpy()[S.row.to_numpy()]
        stem = f"{rep}__{pop}__{o}__{design}"
        S.to_parquet(SCORES / f"{stem}.parquet", index=False)
        (SCORES / f"{stem}.json").write_text(json.dumps(metas[o], indent=1))
    return metas, models


# ------------------------------------------------------------------------------------------------
# recalibration and summaries
# ------------------------------------------------------------------------------------------------
def shift_for(scores: np.ndarray, target: float, w: np.ndarray | None = None) -> float:
    from scipy.optimize import brentq
    w = np.ones(len(scores)) if w is None else w
    f = lambda c: float((w * expit(scores + c)).sum() / w.sum() - target)
    return brentq(f, -20, 20)


def shift_batch(scores: np.ndarray, W: np.ndarray, targets: np.ndarray, c0: float, iters: int = 30) -> np.ndarray:
    """Vectorised Newton: for each replicate b find c_b with sum_i W_bi expit(s_i + c_b) / sum_i W_bi = target_b."""
    c = np.full(W.shape[0], c0, dtype=float)
    ws = W.sum(1)
    for _ in range(iters):
        P = expit(scores[None, :] + c[:, None])
        f = (W * P).sum(1) / ws - targets
        fp = (W * P * (1 - P)).sum(1) / ws
        step = f / np.maximum(fp, 1e-12)
        c -= step
        if np.max(np.abs(step)) < 1e-10:
            break
    return c


def load_scores(rep, pop, outcome, design):
    p = SCORES / f"{rep}__{pop}__{outcome}__{design}.parquet"
    if not p.exists():
        return None, None
    return pd.read_parquet(p), json.loads((SCORES / f"{rep}__{pop}__{outcome}__{design}.json").read_text())


def point_summary(S: pd.DataFrame) -> pd.DataFrame:
    """Per window x test year: obs, calibrated p_hat, obs of the calibration year, AUC, calibration slope."""
    from sklearn.metrics import roc_auc_score
    import statsmodels.api as sm
    rows = []
    for wname, g in S.groupby("window", sort=False):
        cal = g[g.role == "calib"]
        c = shift_for(cal.score.to_numpy(), cal.y.mean())
        for yv, t in g[g.role == "test"].groupby("year"):
            s = t.score.to_numpy() + c
            ph = expit(s)
            try:
                auc = roc_auc_score(t.y, t.score)
            except ValueError:
                auc = np.nan
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    cs = sm.Logit(t.y.to_numpy(), sm.add_constant(s)).fit(disp=0).params[1]
            except Exception:
                cs = np.nan
            rows.append(dict(window=wname, year=int(yv), calib_year=int(cal.year.iloc[0]), n=len(t),
                             obs=float(t.y.mean()), p_hat=float(ph.mean()), p_hat_uncal=float(expit(t.score).mean()),
                             obs_calib=float(cal.y.mean()), shift=c, auc=auc, cal_slope=float(cs)))
    P = pd.DataFrame(rows)
    P["step"] = P.obs - P.obs_calib
    P["content_step"] = P.p_hat - P.obs_calib
    P["unexplained"] = P.obs - P.p_hat
    return P


def rolling_stats(P: pd.DataFrame, pre=PRE_Y, post=POST_Y) -> dict:
    P = P.set_index("year")
    pre = [y for y in pre if y in P.index]
    post = [y for y in post if y in P.index]
    up, uq = P.loc[pre, "unexplained"].mean(), P.loc[post, "unexplained"].mean()
    return {"u_pre": float(up), "u_post": float(uq), "diff": float(uq - up),
            "ratio": float(uq / up) if up != 0 else np.nan,
            "content_share_post_steps": float(P.loc[post, "content_step"].sum() / P.loc[post, "step"].sum()),
            "content_step_pre_mean": float(P.loc[pre, "content_step"].mean()),
            "content_step_post_mean": float(P.loc[post, "content_step"].mean()),
            "step_pre_mean": float(P.loc[pre, "step"].mean()), "step_post_mean": float(P.loc[post, "step"].mean()),
            "pre_years": pre, "post_years": post}


def fixed_stats(P: pd.DataFrame) -> dict:
    P = P.set_index("year")
    o0 = float(P.obs_calib.iloc[0])
    out = {"obs_anchor": o0}
    for y in P.index:
        d = P.loc[y, "obs"] - o0
        out[f"share_{y}"] = float((P.loc[y, "p_hat"] - o0) / d) if d != 0 else np.nan
        out[f"obs_{y}"] = float(P.loc[y, "obs"])
        out[f"p_hat_{y}"] = float(P.loc[y, "p_hat"])
        out[f"unexplained_{y}"] = float(P.loc[y, "obs"] - P.loc[y, "p_hat"])
    return out


def boot_runs(S: pd.DataFrame, n_boot: int = 2000, seed: int = 0, chunk: int = 250, extra=None):
    """Conditional (fixed-model) paper bootstrap, stratified by year: resample papers within each year (one weight
    vector per year, shared by its test and calibration roles), recompute the recalibration shift and all
    per-year obs / p_hat. Returns dict window -> {year: (obs_b, phat_b, obs_calib_b)} arrays of length n_boot.
    `extra(window, year, W, P)` may compute further per-replicate statistics on test rows (P = calibrated probs)."""
    rng = np.random.default_rng(seed)
    rows_by_year = {int(y): np.sort(S.loc[S.year == y, "row"].unique()) for y in S.year.unique()}
    out = {}
    extras = {}
    # draw per-year weights in chunks
    for start in range(0, n_boot, chunk):
        b = min(chunk, n_boot - start)
        Wy = {y: rng.multinomial(len(r), np.full(len(r), 1 / len(r)), size=b).astype(np.float32)
              for y, r in rows_by_year.items()}
        pos = {y: pd.Series(np.arange(len(r)), index=r) for y, r in rows_by_year.items()}
        for wname, g in S.groupby("window", sort=False):
            cal = g[g.role == "calib"]
            cy = int(cal.year.iloc[0])
            Wc = Wy[cy][:, pos[cy].loc[cal.row.to_numpy()].to_numpy()]
            yc = cal.y.to_numpy().astype(float)
            tgt = (Wc @ yc) / Wc.sum(1)
            c0 = shift_for(cal.score.to_numpy(), yc.mean())
            cb = shift_batch(cal.score.to_numpy(), Wc, tgt, c0)
            for yv, t in g[g.role == "test"].groupby("year"):
                yv = int(yv)
                Wt = Wy[yv][:, pos[yv].loc[t.row.to_numpy()].to_numpy()]
                Pt = expit(t.score.to_numpy()[None, :] + cb[:, None])
                ws = Wt.sum(1)
                ob = (Wt @ t.y.to_numpy().astype(float)) / ws
                ph = (Wt * Pt).sum(1) / ws
                d = out.setdefault(wname, {}).setdefault(yv, {"obs": [], "phat": [], "obs_calib": []})
                d["obs"].append(ob); d["phat"].append(ph); d["obs_calib"].append(tgt)
                if extra is not None:
                    e = extra(wname, yv, t, Wt, Pt)
                    if e is not None:
                        extras.setdefault((wname, yv), []).append(e)
    for wname in out:
        for yv in out[wname]:
            out[wname][yv] = {k: np.concatenate(v) for k, v in out[wname][yv].items()}
    extras = {k: np.concatenate(v, axis=0) for k, v in extras.items()}
    return out, extras


def ci(a, level=0.95):
    a = np.asarray(a, float)
    a = a[np.isfinite(a)]
    if len(a) == 0:
        return [np.nan, np.nan]
    return [float(np.quantile(a, (1 - level) / 2)), float(np.quantile(a, 1 - (1 - level) / 2))]


def rolling_boot_stats(Bt: dict, pre=PRE_Y, post=POST_Y) -> dict:
    u = {}
    cs, st = {}, {}
    for wname, d in Bt.items():
        for yv, r in d.items():
            u[yv] = r["obs"] - r["phat"]
            cs[yv] = r["phat"] - r["obs_calib"]
            st[yv] = r["obs"] - r["obs_calib"]
    pre = [y for y in pre if y in u]
    post = [y for y in post if y in u]
    up = np.mean([u[y] for y in pre], axis=0)
    uq = np.mean([u[y] for y in post], axis=0)
    diff = uq - up
    ratio = uq / up
    share = np.sum([cs[y] for y in post], axis=0) / np.sum([st[y] for y in post], axis=0)
    return {"diff_ci": ci(diff), "diff_se": float(np.std(diff, ddof=1)), "p_diff_le0": float(np.mean(diff <= 0)),
            "ratio_ci": ci(ratio), "p_ratio_lt_1_5": float(np.mean(ratio < 1.5)), "p_ratio_lt_1_2": float(np.mean(ratio < 1.2)),
            "u_pre_ci": ci(up), "u_post_ci": ci(uq), "content_share_post_steps_ci": ci(share),
            "p_share_ge_0_6": float(np.mean(share >= 0.6)),
            "u_year_ci": {int(y): ci(u[y]) for y in sorted(u)},
            "content_step_year_ci": {int(y): ci(cs[y]) for y in sorted(cs)}}


def year_permutation(P: pd.DataFrame, pre=PRE_Y, post=POST_Y) -> dict:
    """Year-level exact permutation test of mean(u_post) - mean(u_pre): treats each year's u_y as one draw and
    permutes the pre/post labels over the 8 years (C(8,3) = 56 arrangements); also a Welch t-test across years.
    This adds year-to-year (shock) variability that the within-year paper bootstrap holds fixed."""
    from itertools import combinations
    from scipy import stats as st_
    u = P.set_index("year").unexplained
    yrs = [y for y in list(pre) + list(post) if y in u.index]
    vals = u.loc[yrs].to_numpy()
    k = len([y for y in post if y in u.index])
    obs = vals[-k:].mean() - vals[:-k].mean()
    diffs = []
    for comb in combinations(range(len(vals)), k):
        m = np.zeros(len(vals), bool); m[list(comb)] = True
        diffs.append(vals[m].mean() - vals[~m].mean())
    diffs = np.array(diffs)
    w = st_.ttest_ind(vals[-k:], vals[:-k], equal_var=False, alternative="greater")
    return {"diff": float(obs), "p_perm_one_sided": float(np.mean(diffs >= obs - 1e-12)), "n_arrangements": int(len(diffs)),
            "welch_t": float(w.statistic), "welch_p_one_sided": float(w.pvalue),
            "sd_u_pre_years": float(vals[:-k].std(ddof=1)), "sd_u_post_years": float(vals[-k:].std(ddof=1))}


def fixed_boot_stats(Bt: dict) -> dict:
    out = {}
    for wname, d in Bt.items():
        for yv, r in d.items():
            share = (r["phat"] - r["obs_calib"]) / (r["obs"] - r["obs_calib"])
            out[f"share_{yv}_ci"] = ci(share)
            out[f"p_share_{yv}_ge_0_6"] = float(np.mean(share >= 0.6))
            out[f"unexplained_{yv}_ci"] = ci(r["obs"] - r["phat"])
            out[f"p_hat_{yv}_ci"] = ci(r["phat"])
    return out


# ------------------------------------------------------------------------------------------------
# new-topic placebo (calibration-in-the-large in fast-growing topic clusters)
# ------------------------------------------------------------------------------------------------
def fast_clusters(df: pd.DataFrame, train_years, test_year, tcol="topic100", ratio=3.0) -> set:
    yrs = df.year
    s_tr = df.loc[yrs.isin(train_years), tcol].value_counts(normalize=True)
    s_te = df.loc[yrs.eq(test_year), tcol].value_counts(normalize=True)
    r = (s_te / s_tr.reindex(s_te.index)).fillna(np.inf)
    return set(r.index[r >= ratio])


def new_topic_placebo(df: pd.DataFrame, S: pd.DataFrame, P: pd.DataFrame, years, n_boot=2000, tcol="topic100",
                      seed=1) -> dict:
    """Pooled over test `years`: |obs - p_hat| among papers in fast-growing clusters vs elsewhere."""
    rows = []
    shifts = P.set_index(["window", "year"])["shift"]
    flags = {}
    for (wname, yv), t in S[S.role == "test"].groupby(["window", "year"]):
        if yv not in years:
            continue
        wins = windows("rolling") if wname.startswith("roll") else windows(wname)
        w = [x for x in wins if x["name"] == wname][0]
        fc = fast_clusters(df, w["train"], yv, tcol)
        f = df[tcol].to_numpy()[t.row.to_numpy()]
        fast = np.isin(f, list(fc))
        ph = expit(t.score.to_numpy() + shifts.loc[(wname, yv)])
        res = t.y.to_numpy() - ph
        rows.append(pd.DataFrame({"window": wname, "year": yv, "fast": fast, "res": res, "row": t.row.to_numpy()}))
        flags[(wname, yv)] = (fast, len(fc))
    D = pd.concat(rows, ignore_index=True)
    by_year = {int(yv): {"res_fast": float(g.loc[g.fast, "res"].mean()) if g.fast.any() else None,
                         "res_else": float(g.loc[~g.fast, "res"].mean()), "n_fast": int(g.fast.sum()),
                         "n_else": int((~g.fast).sum())} for yv, g in D.groupby("year")}
    gf = abs(D.loc[D.fast, "res"].mean()) if D.fast.any() else np.nan
    ge = abs(D.loc[~D.fast, "res"].mean())
    # bootstrap (stratified by year x fast; residuals held at the point calibration)
    strata = (D.year.astype(str) + D.fast.astype(str)).to_numpy()
    fm = D.fast.to_numpy()
    r = D.res.to_numpy()
    bf_, be_ = [], []
    for W in C.boot_weights(len(D), n_boot, strata=strata, seed=seed, chunk=200):
        bf_.append(np.abs((W[:, fm] @ r[fm]) / W[:, fm].sum(1)) if fm.any() else np.full(len(W), np.nan))
        be_.append(np.abs((W[:, ~fm] @ r[~fm]) / W[:, ~fm].sum(1)))
    gap = np.concatenate(bf_) - np.concatenate(be_)
    return {"years": [int(y) for y in years], "n_fast": int(D.fast.sum()), "n_else": int((~D.fast).sum()),
            "n_fast_clusters_by_year": {f"{k[0]}:{k[1]}": int(v[1]) for k, v in flags.items()},
            "signed_res_fast": float(D.loc[D.fast, "res"].mean()) if D.fast.any() else np.nan,
            "signed_res_else": float(D.loc[~D.fast, "res"].mean()),
            "abs_gap_fast": float(gf), "abs_gap_else": float(ge), "gap_diff": float(gf - ge),
            "gap_diff_ci": ci(gap), "pass": bool(gf <= ge + 0.02), "topics": tcol, "by_year": by_year}


# ------------------------------------------------------------------------------------------------
# stages
# ------------------------------------------------------------------------------------------------
def stage_fit(which: str):
    t0 = time.time()
    df = load_frame()
    if which.startswith("reps="):
        reps = which.split("=", 1)[1].split(",")
        R = Reps(df, need=tuple(reps))
        for rep in reps:
            for design in ["rolling", "fixed", "placebo"]:
                metas, models = run_fit(R, rep, design, keep_model=(rep == "R1" and design == "fixed"))
                if rep == "R1" and design == "fixed":
                    m, info = models[("fixed", "primary")]
                    top_features(m, info["vectorizer"])
            print(f"{rep} done {time.time() - t0:.0f}s", flush=True)
    elif which == "variants":
        R = Reps(df, need=("R1",))
        for design in ["rolling", "fixed", "placebo"]:
            run_fit(R, "R1", design, pop="U", outcomes=("strict", "loose", "compound"))
            print(f"outcome variants {design} {time.time() - t0:.0f}s", flush=True)
        for pop in ["NA", "non_llm"]:
            for design in ["rolling", "fixed", "placebo"]:
                run_fit(R, "R1", design, pop=pop)
            print(f"pop {pop} {time.time() - t0:.0f}s", flush=True)
    elif which == "r3":
        if not C.MASKED_EMB_PATH.exists():
            print("R3 pending: emb_masked_bge.npy not found", flush=True)
            return
        R = Reps(df, need=("R3",))
        print("R3 rows with masked embedding:", int(R.found3.sum()), flush=True)
        for design in ["rolling", "fixed", "placebo"]:
            run_fit(R, "R3", design)
        print(f"R3 done {time.time() - t0:.0f}s", flush=True)
    else:
        raise KeyError(which)


def top_features(model, vec, k=200):
    """V4: top-k R1 features (fixed-window model) by positive coefficient, with word-frequency flags."""
    from wordfreq import zipf_frequency
    names = vec.get_feature_names_out()
    co = model.coef_.ravel()
    idx = np.argsort(-co)[:k]
    rows = []
    for r, i in enumerate(idx):
        toks = names[i].split()
        z = min(zipf_frequency(t, "en") for t in toks)
        rows.append(dict(rank=r + 1, feature=names[i], coef=float(co[i]), min_token_zipf=z,
                         rare_token=bool(z < 2.0)))
    T = pd.DataFrame(rows)
    T.to_csv(OUTDIR / "v4_top200_R1_features.csv", index=False)
    neg = np.argsort(co)[:k]
    pd.DataFrame({"rank": np.arange(1, k + 1), "feature": names[neg], "coef": co[neg]}).to_csv(
        OUTDIR / "v4_bottom200_R1_features.csv", index=False)
    return T


def stage_summarise(n_boot: int = 2000):
    t0 = time.time()
    df = load_frame()
    res = {"representations": {}, "variants": {}, "new_topic_placebo": {}, "v4": {}}
    steps_rows, fixed_rows, t12 = [], [], []
    runs = []
    for rep in REP_INFO:
        if rep in ("P", "R1P"):
            continue
        for design in ["rolling", "fixed", "placebo"]:
            runs.append((rep, "U", "primary", design))
    for o in ["strict", "loose", "compound"]:
        for design in ["rolling", "fixed", "placebo"]:
            runs.append(("R1", "U", o, design))
    for pop in ["NA", "non_llm"]:
        for design in ["rolling", "fixed", "placebo"]:
            runs.append(("R1", pop, "primary", design))
    for rep, pop, o, design in runs:
        S, meta = load_scores(rep, pop, o, design)
        key = f"{rep}|{pop}|{o}|{design}"
        if S is None:
            res["representations" if (pop == "U" and o == "primary") else "variants"][key] = {"status": "pending"}
            continue
        P = point_summary(S)
        P.insert(0, "design", design); P.insert(0, "outcome", o); P.insert(0, "pop", pop); P.insert(0, "rep", rep)
        Bt, _ = boot_runs(S, n_boot=n_boot, seed=zlib.crc32(key.encode()))
        entry = {"status": "done", "label": REP_INFO[rep][0], "role": REP_INFO[rep][1],
                 "C_by_window": {k: v["C"] for k, v in meta["windows"].items()},
                 "C_at_grid_edge": [k for k, v in meta["windows"].items() if v["C_at_grid_edge"]],
                 "auc_mean": float(P.auc.mean()), "cal_slope_mean": float(P.cal_slope.mean())}
        if design == "rolling":
            st = rolling_stats(P)
            st.update(rolling_boot_stats(Bt))
            # variants: without 2019, excluding 2026
            v1 = rolling_stats(P, pre=(2020, 2021, 2022, 2023)); v1b = rolling_boot_stats(Bt, pre=(2020, 2021, 2022, 2023))
            v2 = rolling_stats(P, post=(2024, 2025)); v2b = rolling_boot_stats(Bt, post=(2024, 2025))
            st["year_permutation"] = year_permutation(P)
            st["without_2019"] = {"diff": v1["diff"], "ratio": v1["ratio"], "diff_ci": v1b["diff_ci"],
                                  "ratio_ci": v1b["ratio_ci"], "u_pre": v1["u_pre"]}
            st["excluding_2026"] = {"diff": v2["diff"], "ratio": v2["ratio"], "diff_ci": v2b["diff_ci"],
                                    "ratio_ci": v2b["ratio_ci"], "u_post": v2["u_post"],
                                    "content_share_post_steps": v2["content_share_post_steps"],
                                    "content_share_post_steps_ci": v2b["content_share_post_steps_ci"]}
            entry.update(st)
            entry["by_year"] = P[["year", "n", "obs", "obs_calib", "p_hat", "step", "content_step", "unexplained",
                                  "auc", "cal_slope"]].to_dict(orient="records")
            steps_rows.append(P)
        else:
            st = fixed_stats(P)
            st.update(fixed_boot_stats(Bt))
            entry.update(st)
            entry["by_year"] = P[["year", "n", "obs", "obs_calib", "p_hat", "p_hat_uncal", "unexplained", "auc",
                                  "cal_slope"]].to_dict(orient="records")
            fixed_rows.append(P)
        res["representations" if (pop == "U" and o == "primary") else "variants"][key] = entry
        print(f"{key}: auc={entry['auc_mean']:.3f} " + (
            f"diff={entry['diff']:.4f} {entry['diff_ci']} ratio={entry['ratio']:.2f} share={entry['content_share_post_steps']:.2f}"
            if design == "rolling" else
            " ".join(f"share{y}={entry.get(f'share_{y}', np.nan):.2f}" for y in (2021, 2022, 2023, 2024, 2025, 2026)
                     if f"share_{y}" in entry)) + f" {time.time() - t0:.0f}s", flush=True)

        # new-topic placebo for R1 primary runs (and R3 when present)
        if rep in ("R1", "R3") and pop == "U" and o == "primary":
            if design == "placebo":
                res["new_topic_placebo"][f"{rep}|placebo_2021_23"] = new_topic_placebo(df, S, P, (2021, 2022, 2023))
                res["new_topic_placebo"][f"{rep}|placebo_2021_23|bge"] = new_topic_placebo(
                    df, S, P, (2021, 2022, 2023), tcol="topic100_bge")
            elif design == "fixed":
                res["new_topic_placebo"][f"{rep}|fixed_2024_26"] = new_topic_placebo(df, S, P, POST_Y)
            elif design == "rolling":
                res["new_topic_placebo"][f"{rep}|rolling_pre_2019_23"] = new_topic_placebo(df, S, P, PRE_Y)
                res["new_topic_placebo"][f"{rep}|rolling_post_2024_26"] = new_topic_placebo(df, S, P, POST_Y)
                res["new_topic_placebo"][f"{rep}|rolling_pre_2019_23|bge"] = new_topic_placebo(
                    df, S, P, PRE_Y, tcol="topic100_bge")

    # ---- tables ----
    if steps_rows:
        pd.concat(steps_rows).to_csv(OUTDIR / "cf_rolling_steps.csv", index=False)
    if fixed_rows:
        pd.concat(fixed_rows).to_csv(OUTDIR / "cf_fixed_paths.csv", index=False)
    for key, e in res["representations"].items():
        rep, pop, o, design = key.split("|")
        if e.get("status") != "done":
            t12.append(dict(rep=rep, label=REP_INFO[rep][0], role=REP_INFO[rep][1], design=design, status="pending"))
            continue
        row = dict(rep=rep, label=e["label"], role=e["role"], design=design, status="done",
                   auc_mean=e["auc_mean"], cal_slope_mean=e["cal_slope_mean"])
        if design == "rolling":
            row.update(content_share=e["content_share_post_steps"],
                       content_share_lo=e["content_share_post_steps_ci"][0],
                       content_share_hi=e["content_share_post_steps_ci"][1],
                       u_pre=e["u_pre"], u_post=e["u_post"], diff=e["diff"], diff_lo=e["diff_ci"][0],
                       diff_hi=e["diff_ci"][1], ratio=e["ratio"], ratio_lo=e["ratio_ci"][0], ratio_hi=e["ratio_ci"][1])
        elif design == "fixed":
            row.update(content_share=e.get("share_2026"), content_share_lo=e.get("share_2026_ci", [np.nan])[0],
                       content_share_hi=e.get("share_2026_ci", [np.nan, np.nan])[1],
                       share_2024=e.get("share_2024"), share_2025=e.get("share_2025"))
        else:
            row.update(content_share=e.get("share_2023"), content_share_lo=e.get("share_2023_ci", [np.nan])[0],
                       content_share_hi=e.get("share_2023_ci", [np.nan, np.nan])[1],
                       unexplained_2023=e.get("unexplained_2023"))
        t12.append(row)
    T12 = pd.DataFrame(t12)
    T12.to_csv(OUTDIR / "T1_2_representations.csv", index=False)

    # ---- V4 leakage diagnostics ----
    r1 = r1_texts(df)
    nm = df.name_primary.to_numpy() == 1
    surv = [lead_survives(t, l) for t, l in zip(r1[nm], df.lead_raw.to_numpy()[nm])]
    rep_auc = {k.split("|")[0] + "|" + k.split("|")[3]: v.get("auc_mean") for k, v in res["representations"].items()
               if v.get("status") == "done"}
    v4 = {"lead_survives_R1_mask_n": int(np.sum(surv)), "name_papers": int(nm.sum()),
          "auc": rep_auc}
    for design in ["rolling", "fixed", "placebo"]:
        a1, a1u = rep_auc.get(f"R1|{design}"), rep_auc.get(f"R1u|{design}")
        a3, a4 = rep_auc.get(f"R3|{design}"), rep_auc.get(f"R4|{design}")
        v4[f"auc_gap_R1u_minus_R1|{design}"] = (a1u - a1) if (a1 and a1u) else None
        v4[f"auc_gap_R4_minus_R3|{design}"] = (a4 - a3) if (a3 and a4) else None
    tf = OUTDIR / "v4_top200_R1_features.csv"
    if tf.exists():
        T = pd.read_csv(tf)
        v4["top200_rare_token_share"] = float(T.rare_token.mean())
        v4["top200_rare_tokens"] = T.loc[T.rare_token, "feature"].tolist()[:40]
    res["v4"] = v4
    (OUTDIR / "content_cf.json").write_text(json.dumps(res, indent=1, default=lambda x: float(x) if np.isscalar(x) else str(x)))
    print(T12.round(3).to_string())
    print(json.dumps(res["new_topic_placebo"], indent=1, default=str)[:3000])
    print(json.dumps(v4, indent=1, default=str)[:1500])
    print(f"summarise done {time.time() - t0:.0f}s")


def stage_refit_boot(B: int = 100, rep: str = "R1", seed: int = 7):
    """Refit bootstrap for the rolling design: resample papers within year (stratified), refit the L2 logit at the
    window's chosen C on the window's original vocabulary (sample weights = bootstrap counts), recompute
    5-fold OOF scores with paper-level folds, recalibrate on the resampled y-1 rows and predict the resampled
    test rows. Captures model-estimation uncertainty that the conditional bootstrap ignores. Checkpointed."""
    from sklearn.model_selection import StratifiedKFold
    t0 = time.time()
    df = load_frame()
    R = Reps(df, need=(rep,))
    meta = json.loads((SCORES / f"{rep}__U__primary__rolling.json").read_text())
    yrs = df.year.to_numpy()
    y = df.name_primary.to_numpy()
    ck = OUTDIR / f"refit_boot_{rep}.csv"
    done = pd.read_csv(ck) if ck.exists() else pd.DataFrame()
    start = int(done.b.max()) + 1 if len(done) else 0
    # Pre-build features per window once
    feats = {}
    for w in windows("rolling"):
        tr = np.where(np.isin(yrs, w["train"]))[0]
        te = np.where(np.isin(yrs, w["test"]))[0]
        Xtr, Xte, _ = R.build(rep, tr, te)
        folds = list(StratifiedKFold(5, shuffle=True, random_state=0).split(np.zeros(len(tr)), y[tr]))
        feats[w["name"]] = (tr, te, Xtr, Xte, folds, meta["windows"][w["name"]]["C"], w)
    print(f"features built {time.time() - t0:.0f}s", flush=True)
    rows_by_year = {yy: np.where(yrs == yy)[0] for yy in range(2017, 2027)}
    for b in range(start, B):
        rng = np.random.default_rng(seed * 100003 + b)
        wgt = np.zeros(len(df))
        for yy, r in rows_by_year.items():
            wgt[r] = rng.multinomial(len(r), np.full(len(r), 1 / len(r)))
        rec = {"b": b}
        for wname, (tr, te, Xtr, Xte, folds, Cv, w) in feats.items():
            sw = wgt[tr]
            keep = sw > 0
            oof = np.zeros(len(tr))
            for trf, vaf in folds:
                trf = trf[keep[trf]]
                m = _lr(Cv, rep).fit(Xtr[trf], y[tr][trf], sample_weight=sw[trf])
                oof[vaf] = m.decision_function(Xtr[vaf])
            kk = np.where(keep)[0]
            m = _lr(Cv, rep).fit(Xtr[kk], y[tr][kk], sample_weight=sw[kk])
            cal = (yrs[tr] == w["calib"]) & keep
            c = shift_for(oof[cal], np.average(y[tr][cal], weights=sw[cal]), w=sw[cal])
            st = m.decision_function(Xte)
            wt = wgt[te]
            yy = w["test"][0]
            rec[f"obs_{yy}"] = float(np.average(y[te], weights=wt))
            rec[f"phat_{yy}"] = float(np.average(expit(st + c), weights=wt))
            rec[f"obscal_{yy}"] = float(np.average(y[tr][cal], weights=sw[cal]))
        pd.DataFrame([rec]).to_csv(ck, mode="a", header=not ck.exists(), index=False)
        if b % 5 == 0:
            print(f"refit boot {b + 1}/{B} {time.time() - t0:.0f}s", flush=True)
    D = pd.read_csv(ck)
    u = {yy: D[f"obs_{yy}"] - D[f"phat_{yy}"] for yy in range(2019, 2027)}
    cs = {yy: D[f"phat_{yy}"] - D[f"obscal_{yy}"] for yy in range(2019, 2027)}
    st_ = {yy: D[f"obs_{yy}"] - D[f"obscal_{yy}"] for yy in range(2019, 2027)}
    up = np.mean([u[yy] for yy in PRE_Y], axis=0)
    uq = np.mean([u[yy] for yy in POST_Y], axis=0)
    share = np.sum([cs[yy] for yy in POST_Y], axis=0) / np.sum([st_[yy] for yy in POST_Y], axis=0)
    out = {"rep": rep, "B": int(len(D)), "diff_ci": ci(uq - up), "diff_se": float(np.std(uq - up, ddof=1)),
           "p_diff_le0": float(np.mean(uq - up <= 0)), "ratio_ci": ci(uq / up),
           "u_pre_ci": ci(up), "u_post_ci": ci(uq), "content_share_post_steps_ci": ci(share),
           "p_share_ge_0_6": float(np.mean(share >= 0.6)),
           "u_year_mean": {yy: float(u[yy].mean()) for yy in u}, "u_year_ci": {yy: ci(u[yy]) for yy in u}}
    (OUTDIR / f"refit_boot_{rep}.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=UserWarning)
    stage = sys.argv[1] if len(sys.argv) > 1 else "fit"
    if stage == "fit":
        stage_fit(sys.argv[2] if len(sys.argv) > 2 else "main")
    elif stage == "summarise":
        stage_summarise(int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
    elif stage == "refit_boot":
        stage_refit_boot(int(sys.argv[2]) if len(sys.argv) > 2 else 100, sys.argv[3] if len(sys.argv) > 3 else "R1")
    else:
        raise SystemExit(f"unknown stage {stage}")
