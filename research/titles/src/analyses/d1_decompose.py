"""WP5 / D1-H1d, H1e: composition (DFL reweighting, Shapley content x composition) and the tool bound.

H1d  DFL: reweight year-y papers (y = 2024, 2025, 2026) to the 2023 joint distribution of team-size bins
     (1-2, 3, 4, 5, 6-7, 8+) x new-key-share bins (0, (0,.5], (.5,1]) x llm_topic; composition share of the
     2023->y rise = (obs_y - cf_y) / (obs_y - obs_2023), cf_y = sum_c P_2023(c) P_y(NAME|c). Evaluated for each of
     2024, 2025 and 2026 (audit fix D1-C6).
     New-key share (audit fix D1-C6): share of the paper's declared profile keys NOT seen on any submission in the
     two preceding years (fixed 2-year lookback). The first pipeline version used "no prior submission since the
     export began", whose lookback grows from 2 years (2023) to 5 years (2026) because profile keys only start in
     2021. 2021 has no profile-key lookback, so its new-key share is missing (its own 'NA' cell in the Shapley
     composition model); 2022's lookback effectively covers 2021 only. The growing-lookback version is kept as a
     DFL sensitivity. Keys are declared profile keys, not persons.
     Shapley over (content -> composition) and (composition -> content): fixed-window logit models (train
     2021-23, intercept recalibrated on cross-fitted 2023 scores, fold-ensemble prediction) with content = R1,
     composition = cell one-hot (size x new keys x llm_topic), both = R1 + cells.
H1e  Tool: F = F24(>=2 RARE21 words, the D1 variant) | F26 | title typography.
     (i) NAME rise among F = 0 papers vs all (+ the minimum F=1 NAME gap that criterion (i) can detect);
     (ii) delta = LPM NAME ~ F + log_authors | topic100 x year, 2024-26, SE clustered by topic100 (+ per-year,
     DiD against 2021-23, components, title-typography sensitivities);
     (iii) tool share = delta x A_max / dNAME(2023->2026) as pre-registered ('naive'), and corrected for
     fingerprint misclassification (audit fix D1-C5): delta = tau (P(L|F=1) - P(L|F=0)), with recall implied by A,
     the 2026 F share and the 2023 (pre-ChatGPT) F share as false-positive rate; tau = delta / k; tool share =
     tau x A / dNAME. Year-matched version uses the 2026-only delta with the 2026 A. Not identified at A = 1.

Outputs (outputs/d1_break/): decompose.json, dfl_table.csv, shapley_table.csv, T1_3_tool_bound.csv,
tool_delta_models.csv, refit_boot_fixed.{csv,json} (stage refit_boot); fig_F1_3 is drawn by d1_summary.

Run:  cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.d1_decompose [fit|all|refit_boot B]
"""
from __future__ import annotations

import json
import sys
import time
import warnings

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.special import expit

from analyses import _core as C
from analyses import d1_content_cf as CF

OUTDIR = C.OUT / "d1_break"
SIZE_BINS = [(0, 2, "1-2"), (3, 3, "3"), (4, 4, "4"), (5, 5, "5"), (6, 7, "6-7"), (8, 10**6, "8+")]
A_MAX = (0.24, 0.39, 0.5, 0.75, 1.0)
A_POINT = 0.39
LOOKBACK = 2
FIRST_KEY_YEAR = 2021  # declared profile keys start here (2017-20 rows carry e-mail keys)


def size_bin(n: pd.Series) -> pd.Series:
    out = pd.Series(index=n.index, dtype=object)
    for lo, hi, lab in SIZE_BINS:
        out[(n >= lo) & (n <= hi)] = lab
    return out


def new_bin(s: pd.Series) -> pd.Series:
    # PLAN bins 0, (0, .5], (.5, 1) -- the last bin is read as (.5, 1] so all-new teams are kept (logged deviation)
    return pd.Series(np.select([s.eq(0), s.gt(0) & s.le(0.5), s.gt(0.5)], ["0", "(0,.5]", "(.5,1]"], "NA"),
                     index=s.index)


def exp_bin(s: pd.Series) -> pd.Series:
    return pd.cut(s.fillna(0), [-1, 0, 2, 9, 10**6], labels=["0", "1-2", "3-9", "10+"]).astype(str)


def new_key_share_lookback(df: pd.DataFrame, lookback: int = LOOKBACK) -> pd.Series:
    """Share of the paper's declared keys not seen on any submission in years y-lookback..y-1 (any submission in
    the discovery export). NaN for years without a profile-key lookback (<= FIRST_KEY_YEAR) and for keyless rows."""
    from common import read_table
    a = read_table("submission_authors")[["submission_id", "year", "declared_id_key"]]
    a = a[a.declared_id_key.notna() & a.declared_id_key.astype(str).ne("")]
    a = a.drop_duplicates(["submission_id", "declared_id_key"]).reset_index(drop=True)
    seen = a[["declared_id_key", "year"]].drop_duplicates()
    hit = np.zeros(len(a), dtype=bool)
    for L in range(1, lookback + 1):
        s = seen.assign(year=seen.year + L, _hit=True)
        m = a[["declared_id_key", "year"]].merge(s, on=["declared_id_key", "year"], how="left")
        hit |= m["_hit"].fillna(False).to_numpy(dtype=bool)
    a["new"] = ~hit
    sh = a.groupby("submission_id").new.mean()
    out = df.submission_id.map(sh).astype(float)
    out[df.year.to_numpy() <= FIRST_KEY_YEAR] = np.nan
    return out


def load() -> pd.DataFrame:
    df = CF.load_frame()
    extra = C.load_analysis_frame(
        feature_cols=["f24_2", "f24", "f26", "title_typo", "F_any"],
        universe_cols=["submission_id", "area_h", "max_prior_subs", "llast_prior_accs", "title"])
    df = df.merge(extra, on="submission_id", how="left", validate="1:1")
    for c in ["f24_2", "f24", "f26", "title_typo", "F_any"]:
        df[c] = df[c].astype(int)
    df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
    df["title_intraword_dash"] = C.rx_contains(df.title.fillna(""), r"[A-Za-z][\-‐‑–][A-Za-z]").astype(int)
    df["sizeb"] = size_bin(df.declared_name_count)
    df["share_new_l2"] = new_key_share_lookback(df)
    df["newb"] = new_bin(df.share_new_l2)                 # primary: fixed 2-year lookback (NA in 2017-21)
    df["newb_grow"] = new_bin(df.share_new_authors)       # first pipeline version (growing lookback)
    df["expb"] = exp_bin(df.max_prior_subs)
    df["cell"] = df.sizeb + "|" + df.newb + "|" + df.llm_topic.astype(str)
    return df


# ------------------------------------------------------------------------------------------------
# H1d: DFL reweighting with a stratified paper bootstrap
# ------------------------------------------------------------------------------------------------
def dfl(df: pd.DataFrame, cellcols, y="name_primary", ref=2023, targets=(2024, 2025, 2026), n_boot=2000, seed=0):
    d = df[df.year.isin((ref,) + tuple(targets))].copy()
    d = d[~d[cellcols].astype(str).isin(["NA", "nan"]).any(axis=1)]
    key = d[cellcols].astype(str).agg("|".join, axis=1)
    codes, uniq = pd.factorize(key)
    K = len(uniq)
    yrs = d.year.to_numpy()
    Y = d[y].to_numpy().astype(float)
    out = {}
    rng = np.random.default_rng(seed)
    idx = {yy: np.where(yrs == yy)[0] for yy in (ref,) + tuple(targets)}

    def stats_from(wref, wt, ir, it):
        Oref = np.zeros((wref.shape[0], K)); np.add.at(Oref.T, codes[ir], wref.T)
        Ot = np.zeros((wt.shape[0], K)); np.add.at(Ot.T, codes[it], wt.T)
        Nt = np.zeros((wt.shape[0], K)); np.add.at(Nt.T, codes[it], (wt * Y[it]).T)
        Nref = np.zeros((wref.shape[0], K)); np.add.at(Nref.T, codes[ir], (wref * Y[ir]).T)
        pref = Oref / Oref.sum(1, keepdims=True)
        pt = Ot / Ot.sum(1, keepdims=True)
        overall_t = Nt.sum(1) / Ot.sum(1)
        rate_t = np.where(Ot > 0, Nt / np.maximum(Ot, 1e-12), overall_t[:, None])  # empty cell -> year mean
        rate_ref = np.where(Oref > 0, Nref / np.maximum(Oref, 1e-12), (Nref.sum(1) / Oref.sum(1))[:, None])
        obs_t, obs_ref = overall_t, Nref.sum(1) / Oref.sum(1)
        cf = (pref * rate_t).sum(1)                       # DFL: y rates at 2023 composition
        expl_ref_rates = ((pt - pref) * rate_ref).sum(1)  # Oaxaca explained part with 2023 rates
        dlt = obs_t - obs_ref
        return obs_ref, obs_t, cf, (obs_t - cf) / dlt, expl_ref_rates / dlt, (Ot[:, :] == 0).sum(1)

    for t in targets:
        ir, it = idx[ref], idx[t]
        o_r, o_t, cf, sh, sh2, nempty = stats_from(np.ones((1, len(ir))), np.ones((1, len(it))), ir, it)
        bs, bs2 = [], []
        for start in range(0, n_boot, 500):
            b = min(500, n_boot - start)
            wr = rng.multinomial(len(ir), np.full(len(ir), 1 / len(ir)), size=b).astype(float)
            wt = rng.multinomial(len(it), np.full(len(it), 1 / len(it)), size=b).astype(float)
            r = stats_from(wr, wt, ir, it)
            bs.append(r[3]); bs2.append(r[4])
        bs, bs2 = np.concatenate(bs), np.concatenate(bs2)
        out[t] = {"obs_ref": float(o_r[0]), "obs": float(o_t[0]), "cf": float(cf[0]), "share": float(sh[0]),
                  "share_ci": CF.ci(bs), "p_share_ge_0_5": float(np.mean(bs >= 0.5)),
                  "p_share_ge_0_3": float(np.mean(bs >= 0.3)),
                  "share_oaxaca_ref_rates": float(sh2[0]), "share_oaxaca_ref_rates_ci": CF.ci(bs2),
                  "n_cells": int(K), "n_empty_target_cells": int(nempty[0]), "n_ref": int(len(ir)), "n_t": int(len(it))}
    return out


# ------------------------------------------------------------------------------------------------
# Shapley content x composition (fixed window, recalibrated, fold-ensemble prediction)
# ------------------------------------------------------------------------------------------------
class RepsP(CF.Reps):
    def __init__(self, df):
        super().__init__(df, need=("R1",))
        self.cellcode = pd.factorize(df.cell)[0]

    def grid(self, rep):
        return CF.GRID_ONEHOT if rep == "P" else CF.GRID_SPARSE

    def _oh(self, idx):
        K = int(self.cellcode.max()) + 1
        return sparse.csr_matrix((np.ones(len(idx), dtype=np.float32), (np.arange(len(idx)), self.cellcode[idx])),
                                 shape=(len(idx), K))

    def build(self, rep, tr, te):
        if rep == "P":
            return self._oh(tr), self._oh(te), {"n_features": int(self.cellcode.max()) + 1}
        if rep == "R1P":
            Xtr, Xte, info = super().build("R1", tr, te)
            return (sparse.hstack([Xtr, self._oh(tr)]).tocsr(), sparse.hstack([Xte, self._oh(te)]).tocsr(),
                    {"n_features": info["n_features"] + int(self.cellcode.max()) + 1})
        return super().build(rep, tr, te)


def stage_fit():
    t0 = time.time()
    df = load()
    R = RepsP(df)
    CF.REP_INFO.setdefault("P", ("composition cells (size x new keys x llm_topic)", "composition"))
    CF.REP_INFO.setdefault("R1P", ("R1 + composition cells", "content+composition"))
    for rep in ["P", "R1P"]:
        CF.run_fit(R, rep, "fixed")
        print(f"{rep} fixed done {time.time() - t0:.0f}s", flush=True)


def _shapley_from(v: dict, dlt):
    """v: {'R1','P','R1P'} -> value (p_hat - obs_2023), arrays allowed."""
    phiC = 0.5 * (v["R1"] + v["R1P"] - v["P"])
    phiP = 0.5 * (v["P"] + v["R1P"] - v["R1"])
    return phiC / dlt, phiP / dlt, v["R1P"] / dlt


def shapley(n_boot=2000, seed=11) -> dict:
    sets = {}
    for rep in ["R1", "P", "R1P"]:
        S, _ = CF.load_scores(rep, "U", "primary", "fixed")
        if S is None:
            return {"status": "pending"}
        P = CF.point_summary(S).set_index("year")
        Bt, _ = CF.boot_runs(S, n_boot=n_boot, seed=seed)
        sets[rep] = (P, Bt["fixed"])
    for yv in CF.POST_Y:  # same seed and row sets -> identical weights; verify via obs
        assert np.allclose(sets["R1"][1][yv]["obs"], sets["P"][1][yv]["obs"])
        assert np.allclose(sets["R1"][1][yv]["obs"], sets["R1P"][1][yv]["obs"])
    out = {}
    for yv in CF.POST_Y:
        P0 = sets["R1"][0]
        o0 = float(P0.loc[yv, "obs_calib"])
        dlt = float(P0.loc[yv, "obs"]) - o0
        v = {k: float(sets[k][0].loc[yv, "p_hat"]) - o0 for k in sets}
        vb = {k: sets[k][1][yv]["phat"] - sets[k][1][yv]["obs_calib"] for k in sets}
        db = sets["R1"][1][yv]["obs"] - sets["R1"][1][yv]["obs_calib"]
        sc, sp, sj = _shapley_from(v, dlt)
        scb, spb, sjb = _shapley_from(vb, db)
        out[yv] = {
            "delta": dlt, "v_content": v["R1"], "v_composition": v["P"], "v_both": v["R1P"],
            "content_first": {"content": v["R1"] / dlt, "composition": (v["R1P"] - v["R1"]) / dlt},
            "composition_first": {"composition": v["P"] / dlt, "content": (v["R1P"] - v["P"]) / dlt},
            "shapley_content_share": sc, "shapley_content_share_ci": CF.ci(scb),
            "shapley_composition_share": sp, "shapley_composition_share_ci": CF.ci(spb),
            "joint_share": sj, "joint_share_ci": CF.ci(sjb),
            "residual_share": 1 - sj, "residual_share_ci": CF.ci(1 - sjb),
            "ci_type": "conditional paper bootstrap (fitted models held fixed; recalibration recomputed)",
            "auc_composition": float(sets["P"][0].loc[yv, "auc"]), "auc_both": float(sets["R1P"][0].loc[yv, "auc"]),
        }
    return out


# ------------------------------------------------------------------------------------------------
# D1-C9: refit bootstrap for the fixed window (R1, P, R1P with shared replicate weights)
# ------------------------------------------------------------------------------------------------
def stage_refit_boot(B: int = 200, seed: int = 13):
    from sklearn.model_selection import StratifiedKFold
    t0 = time.time()
    df = load()
    R = RepsP(df)
    yrs = df.year.to_numpy()
    y = df.name_primary.to_numpy()
    w = CF.windows("fixed")[0]
    tr = np.where(np.isin(yrs, w["train"]))[0]
    te = np.where(np.isin(yrs, w["test"]))[0]
    folds = list(StratifiedKFold(CF.N_FOLDS, shuffle=True, random_state=0).split(np.zeros(len(tr)), y[tr]))
    feats = {}
    for rep in ["R1", "P", "R1P"]:
        meta = json.loads((CF.SCORES / f"{rep}__U__primary__fixed.json").read_text())
        assert "fold ensemble" in str(meta["windows"]["fixed"].get("prediction", "")), "refit fixed scores first"
        Xtr, Xte, _ = R.build(rep, tr, te)
        feats[rep] = (Xtr, Xte, meta["windows"]["fixed"]["C"])
    ck = OUTDIR / "refit_boot_fixed.csv"
    done = pd.read_csv(ck) if ck.exists() else pd.DataFrame()
    start = int(done.b.max()) + 1 if len(done) else 0
    rows_by_year = {yy: np.where(yrs == yy)[0] for yy in range(2021, 2027)}
    cal = yrs[tr] == w["calib"]
    print(f"features built {time.time() - t0:.0f}s", flush=True)
    for b in range(start, B):
        rng = np.random.default_rng(seed * 100003 + b)
        wgt = np.zeros(len(df))
        for yy, r in rows_by_year.items():
            wgt[r] = rng.multinomial(len(r), np.full(len(r), 1 / len(r)))
        sw = wgt[tr]
        keep = sw > 0
        calk = cal & keep
        wt = wgt[te]
        rec = {"b": b, "obscal": float(np.average(y[tr][calk], weights=sw[calk]))}
        for yy in w["test"]:
            m_ = yrs[te] == yy
            rec[f"obs_{yy}"] = float(np.average(y[te][m_], weights=wt[m_]))
        for rep, (Xtr, Xte, Cv) in feats.items():
            oof = np.zeros(len(tr))
            st = []
            for trf, vaf in folds:
                trf = trf[keep[trf]]
                m = CF._lr(Cv, rep).fit(Xtr[trf], y[tr][trf], sample_weight=sw[trf])
                oof[vaf] = m.decision_function(Xtr[vaf])
                st.append(m.decision_function(Xte))
            c = CF.shift_for(oof[calk], rec["obscal"], w=sw[calk])
            ph = CF.ens_prob(np.array(st), c)
            for yy in w["test"]:
                m_ = yrs[te] == yy
                rec[f"{rep}_phat_{yy}"] = float(np.average(ph[m_], weights=wt[m_]))
        pd.DataFrame([rec]).to_csv(ck, mode="a", header=not ck.exists(), index=False)
        if b % 5 == 0:
            print(f"refit boot fixed {b + 1}/{B} {time.time() - t0:.0f}s", flush=True)
    D = pd.read_csv(ck)
    out = {"B": int(len(D)), "reps": ["R1", "P", "R1P"], "prediction": "fold ensemble", "by_year": {}}
    for yy in w["test"]:
        dlt = D[f"obs_{yy}"] - D.obscal
        v = {rep: D[f"{rep}_phat_{yy}"] - D.obscal for rep in ["R1", "P", "R1P"]}
        sc, sp, sj = _shapley_from(v, dlt)
        out["by_year"][int(yy)] = {"R1_share_ci": CF.ci(v["R1"] / dlt), "P_share_ci": CF.ci(v["P"] / dlt),
                                   "R1P_share_ci": CF.ci(v["R1P"] / dlt),
                                   "p_R1_share_ge_0_6": float(np.mean(v["R1"] / dlt >= 0.6)),
                                   "shapley_content_ci": CF.ci(sc), "shapley_composition_ci": CF.ci(sp),
                                   "residual_ci": CF.ci(1 - sj)}
    (OUTDIR / "refit_boot_fixed.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


# ------------------------------------------------------------------------------------------------
# H1e: tool bound
# ------------------------------------------------------------------------------------------------
def f0_rise(df, F="F_d1", y="name_primary", ref=2023, targets=(2024, 2025, 2026), n_boot=2000, seed=3):
    d = df[df.year.isin((ref,) + tuple(targets))]
    out = {}
    rng = np.random.default_rng(seed)
    for t in targets:
        a, b = d[d.year == ref], d[d.year == t]
        def stat(wa, wb):
            ya, yb = a[y].to_numpy(float), b[y].to_numpy(float)
            fa, fb = (a[F].to_numpy() == 0), (b[F].to_numpy() == 0)
            all_ = (wb @ yb) / wb.sum(-1) - (wa @ ya) / wa.sum(-1)
            f0 = (wb[..., fb] @ yb[fb]) / wb[..., fb].sum(-1) - (wa[..., fa] @ ya[fa]) / wa[..., fa].sum(-1)
            f1 = (wb[..., ~fb] @ yb[~fb]) / wb[..., ~fb].sum(-1) - (wa[..., ~fa] @ ya[~fa]) / wa[..., ~fa].sum(-1)
            return all_, f0, f1
        all_, f0, f1 = stat(np.ones(len(a)), np.ones(len(b)))
        bs = []
        for start in range(0, n_boot, 500):
            k = min(500, n_boot - start)
            wa = rng.multinomial(len(a), np.full(len(a), 1 / len(a)), size=k).astype(float)
            wb = rng.multinomial(len(b), np.full(len(b), 1 / len(b)), size=k).astype(float)
            r = stat(wa, wb)
            bs.append(r[1] / r[0])
        bs = np.concatenate(bs)
        sF = float(b[F].mean())
        # power of criterion (i): F=1 NAME gap (pp) in year t that would push the ratio below 0.85 / 0.70
        need = {thr: float((f0 / thr - f0) / sF) for thr in (0.85, 0.70)}
        out[t] = {"rise_all": float(all_), "rise_F0": float(f0), "rise_F1": float(f1), "ratio_F0_all": float(f0 / all_),
                  "ratio_ci": CF.ci(bs), "p_ratio_le_0_70": float(np.mean(bs <= 0.70)),
                  "p_ratio_lt_0_85": float(np.mean(bs < 0.85)),
                  "share_F_ref": float(a[F].mean()), "share_F_t": sF,
                  "name_F0_ref": float(a.loc[a[F] == 0, y].mean()), "name_F0_t": float(b.loc[b[F] == 0, y].mean()),
                  "name_F1_ref": float(a.loc[a[F] == 1, y].mean()), "name_F1_t": float(b.loc[b[F] == 1, y].mean()),
                  "min_F1_gap_for_ratio_below_0.85": need[0.85], "min_F1_gap_for_ratio_below_0.70": need[0.70],
                  "max_possible_F1_gap": float(1 - b.loc[b[F] == 0, y].mean())}
    return out


def delta_models(df) -> pd.DataFrame:
    post = df[df.year.isin(CF.POST_Y)].copy()
    post["ty"] = C.fe_interact(post.topic100, post.year)
    post["ay"] = C.fe_interact(post.area_h.fillna("none"), post.year)
    post["ty_bge"] = C.fe_interact(post.topic100_bge, post.year)
    rows = []
    specs = [
        ("primary: F_d1, topic100 x year FE", "F_d1", post, ["ty"], ["log_authors"]),
        ("F_d1 + llm_topic control", "F_d1", post, ["ty"], ["log_authors", "llm_topic"]),
        ("F_d1, topic100 x year + area x year FE", "F_d1", post, ["ty", "ay"], ["log_authors"]),
        ("F_d1, bge topic100 x year FE", "F_d1", post, ["ty_bge"], ["log_authors"]),
        ("F_any (F24 >= 1 word), topic100 x year FE", "F_any", post, ["ty"], ["log_authors"]),
        ("F24 (>=2) only", "f24_2", post, ["ty"], ["log_authors"]),
        ("F26 only", "f26", post, ["ty"], ["log_authors"]),
        ("title typography only", "title_typo", post, ["ty"], ["log_authors"]),
        ("title typography only | title has an intra-word dash", "title_typo", post[post.title_intraword_dash == 1],
         ["ty"], ["log_authors"]),
        ("title typography only, 2026 only", "title_typo", post[post.year == 2026], ["ty"], ["log_authors"]),
        ("F_d1, NA pool", "F_d1", post[post.NA == 1], ["ty"], ["log_authors"]),
        ("F_d1, non-LLM subset", "F_d1", post[post.non_llm == 1], ["ty"], ["log_authors"]),
        ("F_d1, excluding 2026 (2024-25)", "F_d1", post[post.year <= 2025], ["ty"], ["log_authors"]),
    ]
    for yv in CF.POST_Y:
        specs.append((f"F_d1, {yv} only", "F_d1", post[post.year == yv], ["ty"], ["log_authors"]))
    for yv in CF.POST_Y:
        specs.append((f"F_any, {yv} only", "F_any", post[post.year == yv], ["ty"], ["log_authors"]))
    # pre-period (pre-ChatGPT) association: selection of 'LLM-like' human writers (ID-4c)
    pre = df[df.year.isin((2021, 2022, 2023))].copy()
    pre["ty"] = C.fe_interact(pre.topic100, pre.year)
    for F in ["F_d1", "F_any"]:
        specs.append((f"{F}, pre-period 2021-23 (selection placebo)", F, pre, ["ty"], ["log_authors"]))
    for lab, F, d, fe, ctr in specs:
        clv = "topic100_bge" if "bge" in lab else "topic100"
        r = C.feols(d, "name_primary", [F] + ctr, fe=fe, cluster=clv)
        ci = r.conf_int()
        rows.append(dict(spec=lab, F=F, nobs=r.nobs, n_clusters=r.n_clusters, share_F=float(d[F].mean()),
                         delta=float(r.params[F]), se=float(r.se[F]), lo=float(ci.loc[F, "lo"]),
                         hi=float(ci.loc[F, "hi"]), p=float(r.pvalue[F])))
    # DiD: F x post on 2021-26 (selection-corrected delta, ID-4c)
    dd = df[df.year >= 2021].copy()
    dd["post"] = (dd.year >= 2024).astype(int)
    dd["ty"] = C.fe_interact(dd.topic100, dd.year)
    for F in ["F_d1", "F_any"]:
        dd[f"{F}_x_post"] = dd[F] * dd.post
        r = C.feols(dd, "name_primary", [F, f"{F}_x_post", "log_authors"], fe=["ty"], cluster="topic100")
        ci = r.conf_int()
        k = f"{F}_x_post"
        rows.append(dict(spec=f"{F} x post DiD, 2021-26 (selection-corrected)", F=F, nobs=r.nobs,
                         n_clusters=r.n_clusters, share_F=float(dd.loc[dd.post == 1, F].mean()),
                         delta=float(r.params[k]), se=float(r.se[k]), lo=float(ci.loc[k, "lo"]),
                         hi=float(ci.loc[k, "hi"]), p=float(r.pvalue[k])))
    # logit adjOR comparable with the pilot (topic100 FE + year FE)
    for F in ["F_d1", "F_any"]:
        res = C.logit(f"name_primary ~ {F} + log_authors + C(year) + C(topic100)", post, cluster="topic100")
        t = C.or_table(res, [F]).iloc[0]
        rows.append(dict(spec=f"logit adjOR {F}, topic100 FE + year FE", F=F, nobs=int(res.nobs), n_clusters=100,
                         share_F=float(post[F].mean()), delta=np.nan, se=np.nan, lo=np.nan, hi=np.nan, p=float(t.p),
                         OR=float(t.OR), OR_lo=float(t.OR_lo), OR_hi=float(t.OR_hi)))
    return pd.DataFrame(rows)


def misclass_factor(A: float, share_F: float, fpr: float) -> dict:
    """Nondifferential misclassification of LLM drafting L by the fingerprint F in the target year: prevalence A,
    observed F share s, false-positive rate fpr (pre-ChatGPT F share). recall = (s - (1-A) fpr) / A;
    k = P(L|F=1) - P(L|F=0); delta = tau * k. Not identified when A >= 1 or recall outside (0, 1]."""
    if A >= 1:
        return {"recall": np.nan, "P_L_F1": np.nan, "P_L_F0": np.nan, "k": np.nan, "identified": False}
    rec = (share_F - (1 - A) * fpr) / A
    if not (0 < rec <= 1):
        return {"recall": rec, "P_L_F1": np.nan, "P_L_F0": np.nan, "k": np.nan, "identified": False}
    p1 = A * rec / share_F
    p0 = A * (1 - rec) / (1 - share_F)
    return {"recall": rec, "P_L_F1": p1, "P_L_F0": p0, "k": p1 - p0, "identified": True}


def tool_table(D: pd.DataFrame, df: pd.DataFrame, dname: float) -> pd.DataFrame:
    """Tool share at each A: 'naive' = delta * A / dNAME (pre-registered formula); 'corrected' = (delta / k) * A /
    dNAME with k from misclass_factor using the 2026 F share and the 2023 F share as false-positive rate."""
    sh = {F: (float(df.loc[df.year == 2023, F].mean()), float(df.loc[df.year == 2026, F].mean()))
          for F in ["F_d1", "F_any", "title_typo"]}
    use = ["primary: F_d1, topic100 x year FE", "F_d1, 2026 only", "F_d1 x post DiD, 2021-26 (selection-corrected)",
           "F_d1, topic100 x year + area x year FE", "F_d1 + llm_topic control",
           "F_any (F24 >= 1 word), topic100 x year FE", "F_any, 2026 only",
           "F_any x post DiD, 2021-26 (selection-corrected)", "title typography only",
           "title typography only | title has an intra-word dash", "title typography only, 2026 only"]
    rows = []
    for _, r in D[D.spec.isin(use)].iterrows():
        fpr, s26 = sh[r.F]
        for A in A_MAX:
            mc = misclass_factor(A, s26, fpr)
            k = mc["k"]
            rows.append(dict(spec=r.spec, F=r.F, A_max=A, delta=r.delta, delta_lo=r.lo, delta_hi=r.hi, dNAME=dname,
                             tool_share_naive=r.delta * A / dname, tool_share_naive_lo=r.lo * A / dname,
                             tool_share_naive_hi=r.hi * A / dname, share_F_2026=s26, fpr_2023=fpr,
                             recall=mc["recall"], P_L_F1=mc["P_L_F1"], P_L_F0=mc["P_L_F0"], k=k,
                             identified=mc["identified"],
                             tool_share=(r.delta / k * A / dname) if mc["identified"] else np.nan,
                             tool_share_lo=(r.lo / k * A / dname) if mc["identified"] else np.nan,
                             tool_share_hi=(r.hi / k * A / dname) if mc["identified"] else np.nan))
    return pd.DataFrame(rows)


def stage_all(n_boot=2000):
    t0 = time.time()
    df = load()
    res = {}
    # ---------------- H1d DFL ----------------
    variants = {
        "size": ["sizeb"],
        "size_x_llm": ["sizeb", "llm_topic"],
        "size_x_new": ["sizeb", "newb"],
        "full (size x new x llm_topic)": ["sizeb", "newb", "llm_topic"],
        "full + experience bins": ["sizeb", "newb", "llm_topic", "expb"],
        "full, growing-lookback new keys (first version)": ["sizeb", "newb_grow", "llm_topic"],
        "size_x_new, growing-lookback new keys (first version)": ["sizeb", "newb_grow"],
    }
    dfl_rows = []
    res["dfl"] = {}
    for pop, d in [("U", df), ("NA", df[df.NA == 1]), ("non_llm", df[df.non_llm == 1])]:
        for name, cols in variants.items():
            if pop == "non_llm" and "llm_topic" in cols:
                cols = [c for c in cols if c != "llm_topic"]
            r = dfl(d, cols, n_boot=n_boot)
            res["dfl"][f"{pop}|{name}"] = r
            for t, v in r.items():
                dfl_rows.append(dict(pop=pop, variant=name, target_year=t, **{k: v[k] for k in
                                ["obs_ref", "obs", "cf", "share", "share_oaxaca_ref_rates", "n_cells",
                                 "n_empty_target_cells", "p_share_ge_0_5", "p_share_ge_0_3", "n_ref", "n_t"]},
                                share_lo=v["share_ci"][0], share_hi=v["share_ci"][1],
                                oaxaca_lo=v["share_oaxaca_ref_rates_ci"][0], oaxaca_hi=v["share_oaxaca_ref_rates_ci"][1]))
        print(f"DFL {pop} {time.time() - t0:.0f}s", flush=True)
    DFL = pd.DataFrame(dfl_rows)
    DFL.assign(pop=DFL["pop"].replace({"NA": "NApool"})).to_csv(OUTDIR / "dfl_table.csv", index=False)
    print(DFL[DFL.target_year == 2026].round(3).to_string(), flush=True)

    # composition descriptives
    comp = df[df.year.isin([2023, 2024, 2025, 2026])].groupby("year").agg(
        mean_authors=("declared_name_count", "mean"), share_new_l2=("share_new_l2", "mean"),
        share_new_growing=("share_new_authors", "mean"),
        llm_topic=("llm_topic", "mean"), name=("name_primary", "mean"))
    res["composition_descriptives"] = comp.round(4).reset_index().to_dict(orient="records")
    res["new_key_share_by_year"] = df.groupby("year")[["share_new_l2", "share_new_authors"]].mean().round(4).reset_index().to_dict(orient="records")

    # ---------------- Shapley ----------------
    res["shapley"] = shapley(n_boot=n_boot)
    if res["shapley"].get("status") != "pending":
        sh = []
        for yv, v in res["shapley"].items():
            sh.append(dict(target_year=yv, delta=v["delta"], content_first_content=v["content_first"]["content"],
                           content_first_composition=v["content_first"]["composition"],
                           composition_first_composition=v["composition_first"]["composition"],
                           composition_first_content=v["composition_first"]["content"],
                           shapley_content=v["shapley_content_share"], shapley_content_lo=v["shapley_content_share_ci"][0],
                           shapley_content_hi=v["shapley_content_share_ci"][1],
                           shapley_composition=v["shapley_composition_share"],
                           shapley_composition_lo=v["shapley_composition_share_ci"][0],
                           shapley_composition_hi=v["shapley_composition_share_ci"][1],
                           residual_unexplained=v["residual_share"], residual_lo=v["residual_share_ci"][0],
                           residual_hi=v["residual_share_ci"][1], ci_type="conditional (models fixed)"))
        pd.DataFrame(sh).to_csv(OUTDIR / "shapley_table.csv", index=False)
        print(pd.DataFrame(sh).round(3).to_string(), flush=True)

    # ---------------- H1e tool ----------------
    res["f0_rise"] = {"F_d1": f0_rise(df, "F_d1", n_boot=n_boot), "F_any": f0_rise(df, "F_any", n_boot=n_boot),
                      "F_d1|NA": f0_rise(df[df.NA == 1], "F_d1", n_boot=n_boot)}
    D = delta_models(df)
    D.to_csv(OUTDIR / "tool_delta_models.csv", index=False)
    print(D.round(4).to_string(), flush=True)
    dname = float(df.loc[df.year == 2026, "name_primary"].mean() - df.loc[df.year == 2023, "name_primary"].mean())
    T13 = tool_table(D, df, dname)
    T13.to_csv(OUTDIR / "T1_3_tool_bound.csv", index=False)
    prim = D[D.spec.str.startswith("primary")].iloc[0]
    d26 = D[D.spec == "F_d1, 2026 only"].iloc[0]
    fpr, s26 = float(df.loc[df.year == 2023, "F_d1"].mean()), float(df.loc[df.year == 2026, "F_d1"].mean())

    def corr(r, A):
        mc = misclass_factor(A, s26, fpr)
        if not mc["identified"]:
            return {"share": None, "lo": None, "hi": None, "k": None, "note": "not identified"}
        k = mc["k"]
        return {"share": r.delta / k * A / dname, "lo": r.lo / k * A / dname, "hi": r.hi / k * A / dname, "k": k,
                "recall": mc["recall"], "P_L_F1": mc["P_L_F1"], "P_L_F0": mc["P_L_F0"]}
    res["tool"] = {
        "F_definition": "F_d1 = f24_2 (>= 2 distinct RARE21 words in abstract) | f26 | title_typo",
        "delta_primary": {"delta": prim.delta, "se": prim.se, "lo": prim.lo, "hi": prim.hi, "p": prim.p,
                          "nobs": int(prim.nobs), "share_F_2024_26": prim.share_F},
        "delta_2026": {"delta": d26.delta, "se": d26.se, "lo": d26.lo, "hi": d26.hi, "p": d26.p, "nobs": int(d26.nobs)},
        "dNAME_2023_2026": dname,
        "fpr_2023": fpr, "share_F_2026": s26,
        "tool_share_at_A_naive": {str(A): {"share": prim.delta * A / dname, "lo": prim.lo * A / dname,
                                           "hi": prim.hi * A / dname} for A in A_MAX},
        "tool_share_at_A_corrected_pooled_delta": {str(A): corr(prim, A) for A in A_MAX},
        "tool_share_at_A_corrected_2026_delta": {str(A): corr(d26, A) for A in A_MAX},
        "primary_bound": "misclassification-corrected, year-matched (2026-only delta, A for 2026)",
        "detectable_only_contribution": {
            "share_F_2023": fpr, "share_F_2026": s26,
            "delta_x_dshareF_over_dNAME": float(prim.delta * (s26 - fpr) / dname)},
        "A_point": A_POINT,
        "A_note": "A_max = 0.39 is the PLAN's held-out greedy abstract bound for 2026 (taken as given; not "
                  "re-estimated in D1); sensitivity range 0.24-1.0; at A = 1 every paper is drafted and the F "
                  "contrast cannot identify tau",
        "assumptions": "linear delta*A model; nondifferential misclassification (F depends on NAME only through L); "
                       "homogeneous NAME uplift tau in detected and undetected drafted papers; no spillover to "
                       "undrafted papers; 2023 F share = pure false positives",
    }
    print(json.dumps(res["f0_rise"]["F_d1"], indent=1), flush=True)
    print(json.dumps(res["tool"], indent=1, default=float), flush=True)
    (OUTDIR / "decompose.json").write_text(json.dumps(res, indent=1, default=lambda x: float(x) if np.isscalar(x) else str(x)))
    print(f"done {time.time() - t0:.0f}s")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage == "fit":
        stage_fit()
    elif stage == "all":
        stage_all(int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
    elif stage == "refit_boot":
        stage_refit_boot(int(sys.argv[2]) if len(sys.argv) > 2 else 200)
    else:
        raise SystemExit(stage)
