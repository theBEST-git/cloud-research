"""WP8 / D4: stage-wise filter gains (H4a, H4b), continuation-ratio logits (T4.1) and the pool-specific 2024 break.

Stages (PLAN D4, built in _core.pool_flags; years 2018-2026; the 112 OTHER rows with unknown decision, all in
2017-18, are dropped because they can be neither accepted nor removed at a stage):
    s0 = U;  s1 = not desk-rejected;  s2 = s1 and not withdrawn before decision (2026 wd_post rows stay, as
    rejected);  s3 = accepted (ACC).
Gains (ratio of feature prevalence after vs before a stage; for the continuous style density, ratio of means):
    G_desk = P(f|s1)/P(f|s0), G_exit = P(f|s2)/P(f|s1), G_dec = P(f|s3)/P(f|s2), G_total = P(f|s3)/P(f|s0),
    G_predec = G_desk * G_exit = P(f|s2)/P(f|s0).
Pooling over years: PRIMARY = year-standardised (each year's stage prevalence weighted by that year's share of
s0 papers in the pooled years, so the pooled accepted set is not tilted toward low-acceptance years); the raw
pooled ratio (papers pooled across years) is reported as a robustness check.
CIs: paper bootstrap stratified by year, 2,000 replicates (percentile; 90% CIs for TOST). One-sided bootstrap
p-values: p_ge1 = share of replicates with G >= 1 (test of G < 1).

Feature sets (PLAN D4):
    M  NAME (name_primary), compound, phrase colon, mixed-case name, Title Case
    O  ALL-CAPS title (casing == all_caps), sentence case, question opener; O-union = any of the three
    L  title typography (raw title), R24 (title), R26 (title), F24 (abstract RARE21 >= 1), F26, em dash in the
       abstract, year-specific LLM-style density (continuous, per 100 abstract words);
       L-union = any binary L marker (the continuous density is not part of the union).
Adjusted gains: continuation-ratio logits for passing each stage (desk: s0->s1, exit: s1->s2, decision: s2->s3)
with year x area FE (2024-26) or year FE (2018-23), log authors, llm_topic and topic100 FE; SEs clustered by
topic100. FE cells without outcome variation are dropped (as fixest does). The adjusted gain converts the
adjusted risk ratio on the feature holders (RR_att) into the gain that the feature alone would produce:
G_adj = RR / (s*RR + 1 - s), s = feature share among papers entering the stage (exact identity for raw gains).

H4a pool test: the D1 ITS logit (tc, post, post*tc, log_authors, llm_topic, topic100 FE; cluster topic100) is
fitted separately in the ACC, REJ and WD pools (2018-2026); the joint cluster-robust covariance of the three
slope-change coefficients is built from per-observation influence functions summed by topic100 cluster (this
equals the fully interacted stacked model). Wald equality test (2 df) and pairwise TOST at +/-0.1 on log OR.

Audit revisions (outputs/audit/d4/fix_log.md):
  * F26 in the L set is abstract-only (f26_words | abs_nbhyphen | abs_endash_compound); the features_v2 f26, which also
    fires on title typography, is the secondary 'F26_incl_title'. The L-union is unchanged (its title part is a subset
    of title_typo) and still uses BINARY_L, which prereg_confirm imports.
  * L_noR24 = L-union without the R24 title words (the L depletion is R24-driven; R24 was depleted before 2024).
  * 2018-22 baseline (pre-ChatGPT for accepted camera-ready text) and post/pre contrasts against it.
  * Post-decision withdrawals defined consistently across years (variants wd_decided_in_s2 and wd_postdec_ts); only
    exit/dec/predec gains are informative there (G_total does not involve s2).
  * TOST bootstrap p for H4a; BH q-values over all T4.1 tests; approximate CIs for the adjusted total gains.
  * Style density: the excess-word list is re-selected inside every bootstrap replicate (variant density_reselect).
  * Year-level (small-T) inference for the pool-specific 2024 break (its_pools_yearlevel.csv).
  The functions prereg_confirm imports (BINARY_L, stage_sums, pooled_prev, its_pools, _clean, SEED) are unchanged.

Outputs (outputs/d4_filter/): style_density.parquet, style_density_words.json, gains.csv, prevalence_by_stage.csv,
T4_1_continuation_ratio.csv, its_pools.csv, its_pools_yearlevel.csv, stage_gains.json,
fig_F4_1_stage_ladder.{pdf,png,csv}, fig_S4_1_total_gain_by_year.{pdf,png,csv}, d4_stage_gains.log

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d4_stage_gains
"""
from __future__ import annotations

import json
import re
import time
import unicodedata
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C

OUTDIR = C.OUT / "d4_filter"
LEX_PATH = Path(__file__).resolve().parent / "d4_lexicon.json"
YEARS = tuple(range(2018, 2027))
POST = (2024, 2025, 2026)
PRE = tuple(range(2018, 2024))
N_BOOT = 2000
SEED = 20261011

# (key, column, set, label)
FEATURES = [
    ("NAME", "name_primary", "M", "NAME (coined lead)"),
    ("compound", "name_compound", "M", "Compound (any colon/dash)"),
    ("phrase_colon", "phrase_colon", "M", "Phrase colon"),
    ("mixed_case_name", "ortho_mixed_case", "M", "Mixed-case name"),
    ("title_case", "case_title_case", "M", "Title Case"),
    ("all_caps_title", "case_all_caps", "O", "ALL-CAPS title"),
    ("sentence_case", "case_sentence_case", "O", "Sentence case"),
    ("question_opener", "question_opener", "O", "Question opener"),
    ("O_union", "O_union", "O", "O-union"),
    ("title_typo", "title_typo", "L", "Title typography"),
    ("R24", "r24_any", "L", "R24 register (title)"),
    ("R26", "r26_any", "L", "R26 register (title)"),
    ("F24", "f24", "L", "F24 RARE21 (abstract)"),
    ("F26", "f26_abs", "L", "F26 (abstract)"),
    ("emdash", "abs_emdash", "L", "Em dash (abstract)"),
    ("style_density", "xs_per100", "L", "Style density (abstract)"),
    ("L_union", "L_union", "L", "L-union"),
]
# secondary features (robustness / atlas only)
SECONDARY = [
    ("NAME_strict", "name_strict", "M2", "NAME strict"),
    ("NAME_loose", "name_loose", "M2", "NAME loose"),
    ("allcaps_name", "ortho_all_caps", "O2", "ALL-CAPS name lead"),
    ("F24_2", "f24_2", "L2", "F24 >= 2 words"),
    ("title_emdash", "title_emdash", "L2", "Em dash (title)"),
    ("L_title", "L_title", "L2", "L-union, title markers"),
    ("L_abstract", "L_abstract", "L2", "L-union, abstract markers"),
    ("L_noR24", "L_noR24", "L2", "L-union without R24"),
    ("F26_incl_title", "f26", "L2", "F26 incl. title typography"),
]
COMPUTED_COLS = ("O_union", "L_union", "L_title", "L_abstract", "L_noR24", "xs_per100", "f26_abs")
ALL_FEATURES = FEATURES + SECONDARY
FEAT_COL = {k: c for k, c, _, _ in ALL_FEATURES}
FEAT_SET = {k: s for k, _, s, _ in ALL_FEATURES}
FEAT_LABEL = {k: l for k, _, _, l in ALL_FEATURES}
BINARY_L = ["title_typo", "r24_any", "r26_any", "f24", "f26", "abs_emdash"]
STAGES = ["s0", "s1", "s2", "s3"]
GAIN_DEFS = {"desk": ("s1", "s0"), "exit": ("s2", "s1"), "dec": ("s3", "s2"), "total": ("s3", "s0"),
             "predec": ("s2", "s0")}
# camera-ready-free variant: accepted papers removed from every stage set (exiting papers vs non-accepted survivors)
GAIN_DEFS_CRF = {"desk_crf": ("s1n", "s0n"), "exit_crf": ("s2n", "s1n"), "predec_crf": ("s2n", "s0n")}


def log(msg: str, fh=None):
    print(msg, flush=True)
    if fh is not None:
        fh.write(msg + "\n")
        fh.flush()


def lexicon() -> dict:
    return json.loads(LEX_PATH.read_text())


def _clean(o):
    """Recursively convert numpy scalars to Python types and NaN/inf to None (strict JSON)."""
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.bool_, bool)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return float(o) if np.isfinite(o) else None
    if isinstance(o, np.ndarray):
        return _clean(o.tolist())
    if o is pd.NA or o is pd.NaT:
        return None
    return o


def write_json(obj, path: Path):
    path.write_text(json.dumps(_clean(obj), indent=1))


# --------------------------------------------------------------------------------------------
# Year-specific LLM-style density (Kobak-style excess words from the frozen scout style pool)
# --------------------------------------------------------------------------------------------
def style_density(u: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """u: universe rows (all years) with submission_id, year, abstract. Returns per-paper density and word lists."""
    from sklearn.feature_extraction.text import CountVectorizer
    lx = lexicon()
    pool = lx["style_pool"]
    ab = u.abstract.fillna("").map(lambda x: unicodedata.normalize("NFKC", x).lower())
    cv = CountVectorizer(lowercase=False, token_pattern=r"(?u)\b[a-z][a-z]+\b", binary=True, vocabulary=pool)
    X = cv.fit_transform(ab.values).tocsc()
    vocab = np.array(cv.get_feature_names_out())
    years = u.year.to_numpy()
    n_by = {y: int((years == y).sum()) for y in range(2017, 2027)}
    P = {y: np.asarray(X[years == y].sum(axis=0)).ravel() / n_by[y] for y in range(2017, 2027)}
    bx = np.array([2021, 2022, 2023], float)
    B = np.column_stack([P[2021], P[2022], P[2023]])
    xm = bx.mean()
    slope = ((bx - xm) * (B - B.mean(1, keepdims=True))).sum(1) / ((bx - xm) ** 2).sum()
    icpt = B.mean(1) - slope * xm
    words = {}
    for Y in POST:
        lin = np.clip(icpt + slope * Y, 0, None)
        cons = np.maximum(lin, np.maximum(P[2022], P[2023]))
        qf = np.maximum(cons, 0.5 / n_by[2023])
        ratio = P[Y] / qf
        se = np.sqrt(qf * (1 - qf) / n_by[Y] + qf * (1 - qf) / n_by[2023])
        z = (P[Y] - cons) / se
        words[Y] = sorted(vocab[(ratio >= 2) & (z > 4)].tolist())
    idx = {w: i for i, w in enumerate(vocab)}
    xs = np.zeros(len(u))
    for Y in range(2017, 2027):
        lst = words[Y] if Y in words else words[2024]
        m = years == Y
        cols = [idx[w] for w in lst]
        if cols and m.any():
            xs[m] = np.asarray(X[np.where(m)[0]][:, cols].sum(axis=1)).ravel()
    nw = u.abstract.fillna("").str.split().str.len().clip(lower=1).to_numpy()
    out = pd.DataFrame({"submission_id": u.submission_id.values, "xs_n": xs, "xs_per100": 100 * xs / nw})
    return out, {str(k): v for k, v in words.items()}


# --------------------------------------------------------------------------------------------
# Frame
# --------------------------------------------------------------------------------------------
UNIVERSE_COLS = ["submission_id", "year", "pool", "decision", "ACC", "REJ", "WD", "DR", "NA", "wd_post",
                 "wd_decided", "stage_s1", "stage_s2", "stage_s3", "topic100", "log_authors", "llm_topic",
                 "area_h", "abstract", "title"]


def load_frame(min_year: int = 2018, density: bool = True) -> pd.DataFrame:
    fcols = sorted({c for _, c, _, _ in ALL_FEATURES if c not in COMPUTED_COLS})
    fcols += ["casing", "name_orthography", "first_word", "lead_segment", "title_case_share", "llm_t_abbrev",
              "llm_t_spelled", "llm_t_abbrev_only", "llm_t_named", "f24_n", "f26_words", "abs_nbhyphen",
              "abs_endash_compound", "f26"]
    df = C.load_analysis_frame(feature_cols=list(dict.fromkeys(fcols)), universe_cols=UNIVERSE_COLS)
    if density:
        p = OUTDIR / "style_density.parquet"
        if p.exists():
            sd = pd.read_parquet(p)
        else:
            sd, words = style_density(df)
            OUTDIR.mkdir(parents=True, exist_ok=True)
            sd.to_parquet(p, index=False)
            (OUTDIR / "style_density_words.json").write_text(json.dumps(words, indent=1))
        df = df.merge(sd, on="submission_id", how="left", validate="1:1")
    bool_cols = [c for c in df.columns if df[c].dtype == bool]
    for c in bool_cols:
        df[c] = df[c].astype(int)
    df["O_union"] = df[["case_all_caps", "case_sentence_case", "question_opener"]].max(axis=1)
    # F26 restricted to the abstract (features_v2 f26 also fires on U+2011 / en-dash compounds in the title)
    df["f26_abs"] = df[["f26_words", "abs_nbhyphen", "abs_endash_compound"]].max(axis=1)
    df["L_union"] = df[BINARY_L].max(axis=1)  # identical with f26_abs: f26's title part is a subset of title_typo
    df["L_noR24"] = df[[c for c in BINARY_L if c != "r24_any"]].max(axis=1)
    df["L_title"] = df[["title_typo", "r24_any", "r26_any"]].max(axis=1)
    df["L_abstract"] = df[["f24", "f26_abs", "abs_emdash"]].max(axis=1)
    df = df[df.year >= min_year]
    df = df[df.pool.ne("OTHER")].copy()
    df["s0"] = 1
    df["s1"] = df.stage_s1
    df["s2"] = df.stage_s2
    df["s3"] = df.stage_s3
    nacc = 1 - df.ACC
    df["s0n"], df["s1n"], df["s2n"] = df.s0 * nacc, df.s1 * nacc, df.s2 * nacc
    return df.reset_index(drop=True)


# --------------------------------------------------------------------------------------------
# Bootstrap of stage prevalences
# --------------------------------------------------------------------------------------------
def stage_sums(df: pd.DataFrame, cols: list[str], stage_cols: list[str], n_boot: int = N_BOOT,
               seed: int = SEED) -> dict:
    """Per year: S (B+1, F, K) weighted feature sums within stage sets and N (B+1, K) stage sizes.
    Row 0 is the point estimate; rows 1.. are paper-bootstrap replicates (stratified by year by construction)."""
    X = df[cols].to_numpy(float)
    Sg = df[stage_cols].to_numpy(float)
    F, K = X.shape[1], Sg.shape[1]
    out = {}
    for y in sorted(df.year.unique()):
        m = (df.year == y).to_numpy()
        Xy, Sy = X[m], Sg[m]
        V = np.concatenate([Sy, (Xy[:, :, None] * Sy[:, None, :]).reshape(len(Xy), -1)], axis=1)
        parts = [V.sum(0)[None]]
        if n_boot:
            parts += [W.astype(np.float64) @ V for W in C.boot_weights(int(m.sum()), n_boot, seed=seed + int(y))]
        A = np.vstack(parts)
        out[int(y)] = (A[:, K:].reshape(-1, F, K), A[:, :K])
    return out


def pooled_prev(sums: dict, years, how: str = "std") -> np.ndarray:
    """(B+1, F, K) prevalence pooled over `years`: 'std' = year-standardised to s0 sizes (stage col 0),
    'raw' = papers pooled."""
    years = [y for y in years if y in sums]
    if how == "raw":
        S = sum(sums[y][0] for y in years)
        N = sum(sums[y][1] for y in years)
        return S / N[:, None, :]
    w = np.array([sums[y][1][0, 0] for y in years], float)
    w = w / w.sum()
    return sum(wi * sums[y][0] / sums[y][1][:, None, :] for wi, y in zip(w, years))


def summarise(samples: np.ndarray) -> dict:
    est = float(samples[0])
    b = samples[1:]
    b = b[np.isfinite(b)]
    if len(b) == 0:
        return dict(est=est, se=np.nan, lo95=np.nan, hi95=np.nan, lo90=np.nan, hi90=np.nan, p_ge1=np.nan,
                    p_le1=np.nan)
    return dict(est=est, se=float(np.std(b, ddof=1)), lo95=float(np.quantile(b, .025)),
                hi95=float(np.quantile(b, .975)), lo90=float(np.quantile(b, .05)), hi90=float(np.quantile(b, .95)),
                p_ge1=float(np.mean(b >= 1)), p_le1=float(np.mean(b <= 1)))


PRE22 = tuple(range(2018, 2023))  # pre-ChatGPT for accepted camera-ready text (ICLR 2023 finals post-date 30 Nov 2022)
PERIODS = {**{str(y): (y,) for y in YEARS}, "2024-26": POST, "2024-25": (2024, 2025), "2018-23": PRE,
           "2018-23 excl. 2019": tuple(y for y in PRE if y != 2019), "2018-22": PRE22}


def gain_table(df: pd.DataFrame, keys: list[str], variant: str, n_boot: int = N_BOOT, crf: bool = True,
               periods: dict | None = None) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    stage_cols = STAGES + (["s0n", "s1n", "s2n"] if crf else [])
    cols = [FEAT_COL[k] for k in keys]
    sums = stage_sums(df, cols, stage_cols, n_boot=n_boot)
    defs = dict(GAIN_DEFS, **(GAIN_DEFS_CRF if crf else {}))
    rows, prev_rows = [], []
    periods = periods or PERIODS
    store = {}
    for plabel, yrs in periods.items():
        for how in (["std", "raw"] if len(yrs) > 1 else ["std"]):
            P = pooled_prev(sums, yrs, how)
            store[(plabel, how)] = P
            for j, k in enumerate(keys):
                for si, s in enumerate(stage_cols):
                    n_stage = sum(sums[y][1][0, si] for y in yrs if y in sums)
                    prev_rows.append(dict(variant=variant, feature=k, period=plabel, pooling=how, stage=s,
                                          prev=float(P[0, j, si]), n_stage=float(n_stage)))
                for g, (a, b) in defs.items():
                    ia, ib = stage_cols.index(a), stage_cols.index(b)
                    with np.errstate(divide="ignore", invalid="ignore"):
                        G = P[:, j, ia] / P[:, j, ib]
                    r = dict(variant=variant, feature=k, set=FEAT_SET[k], period=plabel, pooling=how, gain=g)
                    r.update(summarise(G))
                    rows.append(r)
    return pd.DataFrame(rows), pd.DataFrame(prev_rows), store


# --------------------------------------------------------------------------------------------
# Logit influence functions (joint cluster-robust covariance across separately fitted models)
# --------------------------------------------------------------------------------------------
def logit_if(res, term: str) -> np.ndarray:
    X = np.asarray(res.model.exog, float)
    y = np.asarray(res.model.endog, float)
    p = 1 / (1 + np.exp(-(X @ res.params.to_numpy())))
    XtWX = X.T @ (X * (p * (1 - p))[:, None])
    j = list(res.model.exog_names).index(term)
    e = np.zeros(X.shape[1])
    e[j] = 1.0
    v = np.linalg.lstsq(XtWX, e, rcond=None)[0]
    return (X @ v) * (y - p)


def joint_cov(ifs: list[np.ndarray], clusters: list[np.ndarray]) -> tuple[np.ndarray, int]:
    labs = pd.Index(pd.unique(np.concatenate([np.asarray(c) for c in clusters])))
    G = len(labs)
    U = np.zeros((G, len(ifs)))
    for k, (f, c) in enumerate(zip(ifs, clusters)):
        U[:, k] = np.bincount(labs.get_indexer(np.asarray(c)), weights=f, minlength=G)
    return U.T @ U * G / (G - 1), G


def its_design(d: pd.DataFrame) -> pd.DataFrame:
    d = d.copy()
    d["tc"] = d.year - 2023
    d["post"] = (d.year >= 2024).astype(int)
    d["post_t"] = d.post * d.tc
    return d


ITS_FORMULA = "{y} ~ tc + post + post_t + log_authors + llm_topic + C(topic100)"


def its_pools(df: pd.DataFrame, outcome: str = "name_primary", pools=("ACC", "REJ", "WD"),
              formula: str = ITS_FORMULA, years=YEARS, label: str = "primary") -> tuple[list[dict], dict]:
    fits, ifs, cls = {}, [], []
    rows = []
    for pool in pools:
        d = its_design(df[df.pool.eq(pool) & df.year.isin(years)])
        res = C.logit(formula.format(y=outcome), d, cluster="topic100")
        fits[pool] = res
        ifs.append(logit_if(res, "post_t"))
        cls.append(d.loc[res.model_rows, "topic100"].to_numpy())
        t = C.or_table(res, ["post_t", "tc", "post"])
        rows.append(dict(spec=label, outcome=outcome, pool=pool, years=f"{min(years)}-{max(years)}",
                         nobs=int(res.nobs), slope_change_logOR=float(t.loc["post_t", "coef"]),
                         slope_change_se=float(t.loc["post_t", "se"]), slope_change_OR=float(t.loc["post_t", "OR"]),
                         slope_change_OR_lo=float(t.loc["post_t", "OR_lo"]),
                         slope_change_OR_hi=float(t.loc["post_t", "OR_hi"]), slope_change_p=float(t.loc["post_t", "p"]),
                         pre_slope_OR=float(t.loc["tc", "OR"]), level_OR=float(t.loc["post", "OR"])))
    V, G = joint_cov(ifs, cls)
    b = np.array([r["slope_change_logOR"] for r in rows])
    for r, v in zip(rows, np.diag(V)):
        r["slope_change_se_if"] = float(np.sqrt(v))
    R = np.array([[1, -1, 0], [0, 1, -1]], float) if len(pools) == 3 else np.array([[1, -1]], float)
    Rb = R @ b
    chi2 = float(Rb @ np.linalg.solve(R @ V @ R.T, Rb))
    dfree = R.shape[0]
    test = dict(spec=label, outcome=outcome, wald_chi2=chi2, df=dfree, p=float(stats.chi2.sf(chi2, dfree)),
                n_clusters=G, pairs=[])
    z90, z95 = stats.norm.ppf(0.95), stats.norm.ppf(0.975)
    for i in range(len(pools)):
        for j in range(i + 1, len(pools)):
            dlt = b[i] - b[j]
            se = float(np.sqrt(V[i, i] + V[j, j] - 2 * V[i, j]))
            p_tost = max(stats.norm.sf((dlt + 0.1) / se), stats.norm.cdf((dlt - 0.1) / se))
            test["pairs"].append(dict(a=pools[i], b=pools[j], dlogOR=float(dlt), se=se,
                                      lo95=float(dlt - z95 * se), hi95=float(dlt + z95 * se),
                                      lo90=float(dlt - z90 * se), hi90=float(dlt + z90 * se),
                                      p_diff=float(2 * stats.norm.sf(abs(dlt) / se)),
                                      tost_p=float(p_tost), equivalent_0p1=bool((dlt - z90 * se > -0.1)
                                                                                  and (dlt + z90 * se < 0.1))))
    test["max_abs_dlogOR"] = float(max(abs(p["dlogOR"]) for p in test["pairs"]))
    test["all_pairs_equivalent_0p1"] = bool(all(p["equivalent_0p1"] for p in test["pairs"]))
    return rows, test


def bh_q(p) -> np.ndarray:
    """Benjamini-Hochberg q-values (NaN p-values stay NaN)."""
    p = np.asarray(p, float)
    q = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    pv = p[ok]
    m = len(pv)
    if m == 0:
        return q
    o = np.argsort(pv)
    qq = np.empty(m)
    qq[o] = np.minimum.accumulate((pv[o] * m / np.arange(1, m + 1))[::-1])[::-1]
    q[ok] = np.minimum(qq, 1.0)
    return q


def holm_adjust(p: dict) -> dict:
    """Holm step-down adjusted p-values for a dict name -> p."""
    names = sorted(p, key=lambda k: p[k])
    m = len(names)
    out, run = {}, 0.0
    for i, k in enumerate(names):
        run = max(run, min(1.0, (m - i) * p[k]))
        out[k] = run
    return out


def its_pools_yearlevel(df: pd.DataFrame, outcome: str = "name_primary", years=YEARS, brk: int = 2024) -> pd.DataFrame:
    """Small-T inference for the pool-specific break: ITS (t, post, post*t) by OLS on the 9 annual logit prevalences of
    each pool and on the pairwise logit-gap series; t(df_resid) CIs. Year shocks common to a pool are not averaged
    away by paper-level SEs, so these intervals are the honest ones for 'equal breaks'."""
    import statsmodels.api as sm
    d = df[df.pool.isin(["ACC", "REJ", "WD"]) & df.year.isin(years)]
    p = d.groupby(["year", "pool"])[outcome].mean().unstack()
    lg = np.log(p / (1 - p))

    def fit(y):
        t = np.array(y.index, float) - (brk - 1)
        post = (t >= 1).astype(float)
        X = sm.add_constant(np.column_stack([t, post, post * t]))
        m = sm.OLS(y.to_numpy(float), X).fit()
        tq = stats.t.ppf(0.975, m.df_resid)
        tq90 = stats.t.ppf(0.95, m.df_resid)
        return dict(est=float(m.params[3]), se=float(m.bse[3]), df=float(m.df_resid),
                    lo95=float(m.params[3] - tq * m.bse[3]), hi95=float(m.params[3] + tq * m.bse[3]),
                    lo90=float(m.params[3] - tq90 * m.bse[3]), hi90=float(m.params[3] + tq90 * m.bse[3]),
                    p=float(m.pvalues[3]))
    rows = []
    for pool in ["ACC", "REJ", "WD"]:
        r = fit(lg[pool])
        rows.append(dict(kind="pool", contrast=pool, **r, OR=np.exp(r["est"]), OR_lo95=np.exp(r["lo95"]),
                         OR_hi95=np.exp(r["hi95"])))
    for a, b in [("ACC", "REJ"), ("ACC", "WD"), ("REJ", "WD")]:
        r = fit(lg[a] - lg[b])
        r["equivalent_0p1_90ci"] = bool(r["lo90"] > -0.1 and r["hi90"] < 0.1)
        rows.append(dict(kind="difference", contrast=f"{a}-{b}", **r))
    return pd.DataFrame(rows)


def density_reselect(df: pd.DataFrame, n_boot: int = N_BOOT, seed: int = SEED) -> tuple[pd.DataFrame, dict]:
    """Style-density stage gains with the year-specific excess-word list re-selected inside every bootstrap replicate
    (D4-11). Replicate weights use the stage_sums seeds (seed + year), so replicate b is the same paper resample as
    in gain_table. Row 0 reproduces the cached density (selection on the full sample)."""
    from sklearn.feature_extraction.text import CountVectorizer
    pool = lexicon()["style_pool"]
    sel_years = (2021, 2022, 2023) + POST
    sets = STAGES + ["s0n", "s1n", "s2n"]
    data = {}
    for y in sel_years:
        d = df[df.year == y]
        ab = d.abstract.fillna("").map(lambda x: unicodedata.normalize("NFKC", x).lower())
        cv = CountVectorizer(lowercase=False, token_pattern=r"(?u)\b[a-z][a-z]+\b", binary=True, vocabulary=pool)
        X = cv.fit_transform(ab.values).tocsr().astype(np.float64)
        nw = d.abstract.fillna("").str.split().str.len().clip(lower=1).to_numpy().astype(float)
        data[y] = dict(X=X, nw=nw, St=d[sets].to_numpy(float), n=len(d),
                       gen=C.boot_weights(len(d), n_boot, seed=seed + int(y)))

    def select(Pm: dict, nby: dict) -> dict:
        """Pm: year -> (b, V) prevalences. Returns Y -> (b, V) boolean selection (the style_density rule)."""
        bx = np.array([2021, 2022, 2023], float)
        B = np.stack([Pm[2021], Pm[2022], Pm[2023]], axis=-1)
        xm = bx.mean()
        slope = ((bx - xm) * (B - B.mean(-1, keepdims=True))).sum(-1) / ((bx - xm) ** 2).sum()
        icpt = B.mean(-1) - slope * xm
        out = {}
        for Y in POST:
            lin = np.clip(icpt + slope * Y, 0, None)
            cons = np.maximum(lin, np.maximum(Pm[2022], Pm[2023]))
            qf = np.maximum(cons, 0.5 / nby[2023])
            ratio = Pm[Y] / qf
            se = np.sqrt(qf * (1 - qf) / nby[Y] + qf * (1 - qf) / nby[2023])
            z = (Pm[Y] - cons) / se
            out[Y] = (ratio >= 2) & (z > 4)
        return out

    nby = {y: data[y]["n"] for y in sel_years}

    def stage_means(Wd: dict) -> np.ndarray:
        """Wd: year -> (b, n_y) weights. Returns (b, K) year-standardised pooled mean density per stage set."""
        Pm = {y: np.asarray(data[y]["X"].T @ Wd[y].T).T / nby[y] for y in sel_years}  # (b, V)
        sel = select(Pm, nby)
        w = np.array([data[Y]["St"][:, 0].sum() for Y in POST], float)
        w = w / w.sum()
        out = 0
        for wi, Y in zip(w, POST):
            dens = 100 * np.asarray(data[Y]["X"] @ sel[Y].T.astype(np.float64)) / data[Y]["nw"][:, None]  # (n, b)
            S_ = (Wd[Y] * dens.T) @ data[Y]["St"]
            N_ = Wd[Y] @ data[Y]["St"]
            out = out + wi * S_ / N_
        nsel = {Y: sel[Y].sum(1) for Y in POST}
        return out, sel, nsel
    point_W = {y: np.ones((1, nby[y])) for y in sel_years}
    M0, sel0, n0 = stage_means(point_W)
    parts, nsel_all, jac = [M0], {Y: [] for Y in POST}, {Y: [] for Y in POST}
    gens = {y: data[y]["gen"] for y in sel_years}
    done = 0
    while done < n_boot:
        Wd = {y: next(gens[y]).astype(np.float64) for y in sel_years}
        M, sel, ns = stage_means(Wd)
        parts.append(M)
        for Y in POST:
            nsel_all[Y].append(ns[Y])
            inter = (sel[Y] & sel0[Y][0]).sum(1)
            union = (sel[Y] | sel0[Y][0]).sum(1)
            jac[Y].append(inter / np.maximum(union, 1))
        done += len(M)
    A = np.vstack(parts)  # (B+1, K)
    rows = []
    for g, (a, b) in dict(GAIN_DEFS, **GAIN_DEFS_CRF).items():
        G = A[:, sets.index(a)] / A[:, sets.index(b)]
        r = dict(variant="density_reselect", feature="style_density", set="L", period="2024-26", pooling="std", gain=g)
        r.update(summarise(G))
        rows.append(r)
    info = {str(Y): dict(n_words_point=int(n0[Y][0]), n_words_median=float(np.median(np.concatenate(nsel_all[Y]))),
                         n_words_p05=float(np.quantile(np.concatenate(nsel_all[Y]), .05)),
                         n_words_p95=float(np.quantile(np.concatenate(nsel_all[Y]), .95)),
                         jaccard_median=float(np.median(np.concatenate(jac[Y])))) for Y in POST}
    return pd.DataFrame(rows), info


# --------------------------------------------------------------------------------------------
# Continuation-ratio logits
# --------------------------------------------------------------------------------------------
STAGE_PASS = {"desk": ("s0", "s1"), "exit": ("s1", "s2"), "decision": ("s2", "s3")}


def drop_novar(d: pd.DataFrame, y: str, fes: list[str]) -> pd.DataFrame:
    while True:
        n0 = len(d)
        for f in fes:
            v = d.groupby(f)[y].transform("std").fillna(0)
            d = d[v > 0]
        if len(d) == n0:
            return d


def cr_fit(df: pd.DataFrame, key: str, stage: str, era: str) -> dict | None:
    col = FEAT_COL[key]
    ent, pas = STAGE_PASS[stage]
    yrs = POST if era == "2024-26" else PRE
    d = df[(df[ent] == 1) & df.year.isin(yrs)].copy()
    d["pass_"] = d[pas].astype(int)
    d["fe_cell"] = (d.year.astype(str) + "|" + d.area_h.fillna("none").astype(str)) if era == "2024-26" \
        else d.year.astype(str)
    if key == "style_density":
        sd = d[col].std()
        d["f_"] = (d[col] - d[col].mean()) / sd
    else:
        d["f_"] = d[col].astype(int)
    n_f = int((d.f_ > 0).sum()) if key != "style_density" else len(d)
    if key != "style_density" and (n_f < 30 or d.loc[d.f_ == 1, "pass_"].nunique() < 2):
        return None
    d = drop_novar(d, "pass_", ["fe_cell", "topic100"])
    if len(d) < 200:
        return None
    try:
        res = C.logit("pass_ ~ f_ + log_authors + llm_topic + C(fe_cell) + C(topic100)", d, cluster="topic100")
    except Exception as e:  # noqa: BLE001
        warnings.warn(f"cr_fit {key} {stage} {era}: {e}")
        return None
    t = C.or_table(res, ["f_"])
    out = dict(era=era, stage=stage, feature=key, set=FEAT_SET[key], nobs=int(res.nobs),
               pass_rate=float(d.pass_.mean()), coef=float(t.coef.iloc[0]), se=float(t.se.iloc[0]),
               p=float(t.p.iloc[0]), OR=float(t.OR.iloc[0]), OR_lo=float(t.OR_lo.iloc[0]),
               OR_hi=float(t.OR_hi.iloc[0]),
               converged=bool(res.mle_retvals.get("converged", True)) if hasattr(res, "mle_retvals") else True)
    if key != "style_density":
        X = np.asarray(res.model.exog, float)
        beta = res.params.to_numpy()
        j = list(res.model.exog_names).index("f_")
        fm = X[:, j] == 1
        eta = X[fm] @ beta
        s = float(fm.mean())
        p_pass_f = float(d.loc[res.model_rows][fm].pass_.mean())
        p_pass = float(d.loc[res.model_rows].pass_.mean())

        def rr(bf):
            e1 = eta - beta[j] + bf
            e0 = eta - beta[j]
            return float(np.mean(1 / (1 + np.exp(-e1))) / np.mean(1 / (1 + np.exp(-e0))))

        def gadj(r):
            return r / (s * r + 1 - s)
        R, Rlo, Rhi = rr(beta[j]), rr(t.lo.iloc[0]), rr(t.hi.iloc[0])
        out.update(n_f=int(fm.sum()), share_f=s, RR_adj=R, RR_adj_lo=Rlo, RR_adj_hi=Rhi,
                   G_raw=p_pass_f / p_pass, G_adj=gadj(R), G_adj_lo=gadj(Rlo), G_adj_hi=gadj(Rhi))
    else:
        out.update(n_f=len(d), share_f=np.nan, note="OR per SD of density")
    return out


# --------------------------------------------------------------------------------------------
# Figures
# --------------------------------------------------------------------------------------------
def fig_ladder(gains: pd.DataFrame, period: str = "2024-26"):
    import matplotlib.pyplot as plt
    keys = [k for k, _, _, _ in FEATURES]
    g = gains[(gains.variant == "primary") & (gains.period == period) & (gains.pooling == "std")
              & gains.feature.isin(keys) & gains.gain.isin(["desk", "exit", "dec", "total"])]
    series = [("desk", "Desk screen", C.COLORS[0], "o"), ("exit", "Author exit", C.COLORS[1], "o"),
              ("dec", "Decision (hollow: not identified vs camera-ready edits, T4.2)", C.COLORS[2], "o"),
              ("total", "Total (accepted/all; includes the decision stage)", C.COLORS[3], "D")]
    fig, ax = C.new_fig("double", height=5.6)
    n = len(keys)
    base = np.arange(n)[::-1].astype(float)
    offs = {"desk": 0.27, "exit": 0.09, "dec": -0.09, "total": -0.27}
    plot_rows = []
    XMIN, XMAX = 0.70, 1.30
    offscale = {}
    for gname, lab, col, mk in series:
        sub = g[g.gain == gname].set_index("feature").reindex(keys)
        yy = base + offs[gname]
        for yv, (k, r) in zip(yy, sub.iterrows()):
            if not np.isfinite(r.est):
                continue
            plot_rows.append(dict(feature=k, label=FEAT_LABEL[k], set=FEAT_SET[k], gain=gname, est=r.est,
                                  lo95=r.lo95, hi95=r.hi95, y=yv))
            lo_, hi_ = max(r.lo95, XMIN), min(r.hi95, XMAX)
            if hi_ > XMIN:
                ax.plot([lo_, hi_], [yv, yv], color=col, lw=1.4, solid_capstyle="butt")
            hollow = gname == "dec"
            if r.est < XMIN:
                ax.plot([XMIN], [yv], marker="<", color=col, ms=5, lw=0, clip_on=False,
                        markerfacecolor="white" if hollow else col)
                offscale.setdefault(k, []).append(f"{lab.split(' (')[0].lower()} {r.est:.2f} "
                                                  f"[{r.lo95:.2f}, {r.hi95:.2f}]")
            else:
                ax.plot([r.est], [yv], marker=mk, color=col, ms=5 if mk == "o" else 5.5, lw=0,
                        markerfacecolor="white" if hollow else col,
                        markeredgecolor="white" if mk == "D" else col, markeredgewidth=1.0 if hollow else 0.4)
        ax.plot([], [], marker=mk, color=col, lw=1.4, ms=5, label=lab,
                markerfacecolor="white" if gname == "dec" else col)
    for k, txt in offscale.items():
        yv = base[keys.index(k)]
        ax.text(1.29, yv - 0.02, "off scale (left): " + "\n".join(txt), fontsize=6.8, color=C.TEXT2,
                va="center", ha="right")
    ax.axvline(1.0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_xscale("log")
    ticks = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    ax.set_xticks(ticks, [f"{t:g}" for t in ticks])
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlim(XMIN, XMAX)
    ax.set_yticks(base, [FEAT_LABEL[k] for k in keys])
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    # set separators and labels
    sets = [FEAT_SET[k] for k in keys]
    for i in range(1, n):
        if sets[i] != sets[i - 1]:
            ax.axhline(base[i] + 0.5, color=C.GRID, lw=0.8)
    set_names = {"M": "Mainstream (M)", "O": "Outsider (O)", "L": "LLM-style (L)"}
    for s in ["M", "O", "L"]:
        idx = [i for i, x in enumerate(sets) if x == s]
        ax.text(1.005, base[idx[0]] + 0.35, set_names[s], transform=ax.get_yaxis_transform(), ha="left",
                va="center", fontsize=8, color=C.TEXT2)
    ax.set_xlabel("Stage gain = P(feature | passed stage) / P(feature | entered stage) (ratio of means for "
                  "style density), log scale")
    ax.set_ylim(-0.7, n - 0.3)
    ax.legend(ncol=2, loc="lower center", bbox_to_anchor=(0.45, 1.0), handlelength=1.6, columnspacing=1.2,
              fontsize=7.5)
    ax.set_title("Stage gains, ICLR 2024-26 pooled (year-standardised), 95% paper-bootstrap CIs; values below 0.7 "
                 "marked off scale", loc="left", fontsize=8.5, pad=34)
    ax.text(0.0, -0.13, "Desk and exit compare exiting papers with survivor sets that include accepted (camera-ready) "
            "text; camera-ready-free variants are in gains.csv.", transform=ax.transAxes, fontsize=6.8,
            color=C.TEXT2, ha="left", va="top")
    return fig, pd.DataFrame(plot_rows)


def fig_total_by_year(gains: pd.DataFrame):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    fig, ax = C.new_fig("single", height=2.9)
    feats = [("NAME", "NAME", C.COLORS[0]), ("O_union", "O-union", C.COLORS[1]), ("L_union", "L-union", C.COLORS[2])]
    rows = []
    ax.axhspan(0.95, 1.10, color=C.GRID, alpha=0.8, lw=0, zorder=0)
    ax.axhline(1.0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    off = {"NAME": -0.14, "O_union": 0.0, "L_union": 0.14}
    label_y = {"NAME": 1.10, "O_union": 0.76, "L_union": 0.93}
    for k, lab, col in feats:
        sub = gains[(gains.variant == "primary") & (gains.feature == k) & (gains.gain == "total")
                    & gains.period.isin([str(y) for y in YEARS])].copy()
        sub["year"] = sub.period.astype(int)
        sub = sub.sort_values("year")
        x = sub.year + off[k]
        ax.errorbar(x, sub.est, yerr=[sub.est - sub.lo95, sub.hi95 - sub.est], color=col, lw=0, elinewidth=1.1,
                    marker="o", ms=4.5, capsize=0, label=lab)
        ax.plot(x, sub.est, color=col, lw=1.2, alpha=0.8)
        ax.text(2026.45, label_y[k], lab, color=col, fontsize=7.5, va="center", ha="left")
        for _, r in sub.iterrows():
            rows.append(dict(feature=k, year=r.year, est=r.est, lo95=r.lo95, hi95=r.hi95))
    ax.set_yscale("log")
    yt = [0.4, 0.5, 0.7, 1.0, 1.4]
    ax.set_yticks(yt, [f"{t:g}" for t in yt])
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_ylim(0.38, 1.7)
    ax.set_xticks(list(YEARS), [f"'{str(y)[2:]}" for y in YEARS])
    ax.set_xlim(2017.6, 2027.4)
    ax.set_ylabel("Total gain (accepted / all), 95% CI, log scale")
    h, l_ = ax.get_legend_handles_labels()
    h.append(Patch(color=C.GRID, label="H4a band [0.95, 1.10] (NAME only)"))
    ax.legend(handles=h, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=4, fontsize=6.8, handlelength=1.0,
              columnspacing=0.8)
    return fig, pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fh = open(OUTDIR / "d4_stage_gains.log", "w")
    df = load_frame()
    log(f"frame: {len(df)} rows, years {df.year.min()}-{df.year.max()} (OTHER rows dropped)", fh)
    log(df.groupby("year")[["s0", "s1", "s2", "s3"]].sum().to_string(), fh)
    words = json.loads((OUTDIR / "style_density_words.json").read_text())
    log("style-density words: " + "; ".join(f"{y}: {len(w)}" for y, w in words.items()), fh)

    keys_primary = [k for k, _, _, _ in FEATURES]
    keys_all = [k for k, _, _, _ in ALL_FEATURES]

    # ---------------- gains: primary + variants
    gains, prev, store = gain_table(df, keys_all, "primary")
    log(f"primary gains done ({time.time() - t0:.0f}s)", fh)
    # wd_post dropped (PLAN sensitivity)
    g2, p2, _ = gain_table(df[df.wd_post == 0].reset_index(drop=True), keys_primary, "drop_wd_post",
                           periods={"2026": (2026,), "2024-26": POST})
    # Post-decision withdrawals defined consistently across years (D4-5). _core.pool_flags keeps only the 2026
    # wd_post rows in s2; 2024-25 withdrawals that carry an accept/reject decision, and 2025-26 withdrawals timestamped
    # on/after the decision date (modification_ms; 2024 timestamps are a bulk post-decision update and unusable), are
    # also post-decision exits. G_total = P(s3)/P(s0) does not involve s2, so only desk/exit/dec/predec can move.
    from common import read_table
    from arxiv_audit import DECISION_DATE
    mod = read_table("metadata_provenance")[["submission_id", "modification_ms"]]
    dts = df[["submission_id", "year", "WD"]].merge(mod, on="submission_id", how="left", validate="1:1")
    ts = pd.to_datetime(dts.modification_ms, unit="ms", errors="coerce")
    dd = pd.to_datetime(dts.year.map({y: DECISION_DATE.get(y) for y in (2025, 2026)}))
    df["wd_post_ts"] = ((dts.WD == 1) & dts.year.isin([2025, 2026]) & (ts >= dd)).astype(int).to_numpy()
    wd_dec = df.wd_decided.astype(bool)
    pd_variants = {"wd_decided_in_s2": wd_dec, "wd_postdec_ts": wd_dec | df.wd_post_ts.astype(bool)}
    var_tabs, var_prev = [], []
    postdec_counts = {}
    for vname, keep in pd_variants.items():
        dv = df.copy()
        dv["s2"] = (dv.s1.astype(bool) & (~dv.WD.astype(bool) | keep)).astype(int)
        dv["s2n"] = dv.s2 * (1 - dv.ACC)
        postdec_counts[vname] = {str(y): int(n) for y, n in dv[dv.WD.astype(bool) & keep].groupby("year").size().items()}
        gv, pv, _ = gain_table(dv, keys_primary + ["L_noR24"], vname,
                               periods={"2024-26": POST, "2024": (2024,), "2025": (2025,), "2026": (2026,)})
        var_tabs.append(gv)
        var_prev.append(pv)
    log(f"post-decision withdrawals kept in s2: {postdec_counts}", fh)
    # style density with the excess-word list re-selected in every bootstrap replicate (D4-11)
    g_dens, dens_info = density_reselect(df)
    log(f"density re-selection bootstrap: {dens_info} ({time.time() - t0:.0f}s)", fh)
    # post (2024-26) vs pre contrasts of log gains (same replicate index; years are disjoint strata). Two baselines:
    # 2018-23 (pre-registered 'pre') and 2018-22 (accepted 2023 camera-ready text post-dates ChatGPT).
    pp_rows = []
    stage_cols = STAGES + ["s0n", "s1n", "s2n"]
    for vlabel, pre_lab in [("post_vs_pre", "2018-23"), ("post_vs_pre_1822", "2018-22")]:
        Ppost, Ppre = store[("2024-26", "std")], store[(pre_lab, "std")]
        for j, k in enumerate(keys_all):
            for gname, (a, b) in dict(GAIN_DEFS, **GAIN_DEFS_CRF).items():
                ia, ib = stage_cols.index(a), stage_cols.index(b)
                with np.errstate(divide="ignore", invalid="ignore"):
                    r_ = (Ppost[:, j, ia] / Ppost[:, j, ib]) / (Ppre[:, j, ia] / Ppre[:, j, ib])
                row = dict(variant=vlabel, feature=k, set=FEAT_SET[k], period=f"2024-26 / {pre_lab}", pooling="std",
                           gain=gname)
                row.update(summarise(r_))
                pp_rows.append(row)
    gains = pd.concat([gains, g2] + var_tabs + [g_dens, pd.DataFrame(pp_rows)], ignore_index=True)
    prev = pd.concat([prev, p2] + var_prev, ignore_index=True)
    gains.to_csv(OUTDIR / "gains.csv", index=False)
    prev.to_csv(OUTDIR / "prevalence_by_stage.csv", index=False)
    log(f"variants done ({time.time() - t0:.0f}s)", fh)

    def G(feature, gain, period="2024-26", variant="primary", pooling="std"):
        r = gains[(gains.variant == variant) & (gains.feature == feature) & (gains.gain == gain)
                  & (gains.period == period) & (gains.pooling == pooling)]
        return r.iloc[0].to_dict() if len(r) else None

    show = gains[(gains.variant == "primary") & (gains.period == "2024-26") & (gains.pooling == "std")
                 & gains.gain.isin(["desk", "exit", "dec", "total", "predec"])]
    piv = show.pivot(index="feature", columns="gain", values="est").reindex(keys_all)
    log("\n2024-26 pooled (std) gains:\n" + piv.round(3).to_string(), fh)
    for k in ["NAME", "O_union", "L_union", "all_caps_title", "title_typo"]:
        sub = gains[(gains.variant == "primary") & (gains.feature == k) & (gains.gain == "total")
                    & gains.period.isin([str(y) for y in YEARS])]
        log(f"{k} G_total by year: " + ", ".join(f"{r.period} {r.est:.3f} [{r.lo95:.3f},{r.hi95:.3f}]"
                                                 for r in sub.itertuples()), fh)

    # ---------------- H4a
    name_years = {str(y): G("NAME", "total", str(y)) for y in YEARS}
    in_band = {y: bool(0.95 <= r["est"] <= 1.10) for y, r in name_years.items()}
    pooled = G("NAME", "total")
    jN = keys_all.index("NAME")
    Gn = store[("2024-26", "std")][:, jN, STAGES.index("s3")] / store[("2024-26", "std")][:, jN, STAGES.index("s0")]
    tost = dict(est=pooled["est"], lo90=pooled["lo90"], hi90=pooled["hi90"],
                within=bool(pooled["lo90"] > 0.90 and pooled["hi90"] < 1.11),
                p_lower=float(np.mean(Gn[1:] <= 0.90)), p_upper=float(np.mean(Gn[1:] >= 1.11)))
    # TOST p = larger of the two one-sided bootstrap p-values; 0 replicates beyond a margin is floored at 1/N_BOOT
    tost["p_tost"] = max(tost["p_lower"], tost["p_upper"], 1.0 / N_BOOT)
    its_rows, its_test = its_pools(df)
    its_rows_b, its_test_b = its_pools(df, formula="{y} ~ tc + post + post_t", label="no controls, no topic FE")
    d17 = load_frame(min_year=2017, density=False)
    its_rows_c, its_test_c = its_pools(d17, pools=("ACC", "REJ"), years=tuple(range(2017, 2027)),
                                       label="ACC vs REJ, 2017-2026")
    its_rows_d, its_test_d = its_pools(df, outcome="name_compound", label="compound outcome")
    pd.DataFrame(its_rows + its_rows_b + its_rows_c + its_rows_d).to_csv(OUTDIR / "its_pools.csv", index=False)
    its_yl = its_pools_yearlevel(df)
    its_yl.to_csv(OUTDIR / "its_pools_yearlevel.csv", index=False)
    log("ITS year-level (9 annual points, t(5)):\n" + its_yl.round(3).to_string(), fh)
    for r in its_rows:
        log(f"ITS {r['pool']}: slope-change OR {r['slope_change_OR']:.3f} [{r['slope_change_OR_lo']:.3f}, "
            f"{r['slope_change_OR_hi']:.3f}] se {r['slope_change_se']:.4f} (IF se {r['slope_change_se_if']:.4f})", fh)
    log(f"ITS equality Wald chi2({its_test['df']}) = {its_test['wald_chi2']:.2f}, p = {its_test['p']:.3f}; "
        f"max |dlogOR| {its_test['max_abs_dlogOR']:.3f}", fh)
    h4a = dict(
        name_total_by_year=name_years, in_band_0p95_1p10=in_band, all_years_in_band=bool(all(in_band.values())),
        pooled_2024_26=pooled, pooled_2024_26_raw=G("NAME", "total", pooling="raw"), tost_0p90_1p11=tost,
        its_pools=its_rows, its_equality=its_test, its_yearlevel=its_yl.to_dict(orient="records"),
        name_by_year_ci_inside_band={y: bool(r["lo95"] >= 0.95 and r["hi95"] <= 1.10) for y, r in name_years.items()},
        its_robustness={"no_controls": dict(rows=its_rows_b, test=its_test_b),
                        "acc_rej_2017_2026": dict(rows=its_rows_c, test=its_test_c),
                        "compound_outcome": dict(rows=its_rows_d, test=its_test_d)},
    )
    h4a["falsified"] = bool((not tost["within"]) or its_test["p"] < 0.05)
    h4a["verdict_parts"] = dict(
        per_year_band=h4a["all_years_in_band"], tost=tost["within"], its_equal_p_ge_0p05=its_test["p"] >= 0.05,
        its_all_pairs_within_0p1=its_test["all_pairs_equivalent_0p1"],
        its_point_max_dlogOR_lt_0p1=its_test["max_abs_dlogOR"] < 0.1)

    # ---------------- H4b
    h4b = {}
    for k in ["L_union", "O_union"] + [k for k in keys_all if FEAT_SET[k] in ("L", "O", "L2", "O2")
                                       and k not in ("L_union", "O_union")]:
        h4b[k] = {g: G(k, g) for g in ["total", "predec", "desk", "exit", "dec", "predec_crf", "desk_crf",
                                       "exit_crf"]}
        h4b[k]["by_year_total"] = {str(y): G(k, "total", str(y)) for y in POST}
        h4b[k]["by_year_predec"] = {str(y): G(k, "predec", str(y)) for y in POST}
        h4b[k]["pre_2018_23_total"] = G(k, "total", "2018-23")
    L = h4b["L_union"]
    h4b["tests"] = dict(
        L_union_total_lt1=dict(est=L["total"]["est"], hi95=L["total"]["hi95"], p_one_sided=L["total"]["p_ge1"]),
        O_union_total_lt1=dict(est=h4b["O_union"]["total"]["est"], hi95=h4b["O_union"]["total"]["hi95"],
                               p_one_sided=h4b["O_union"]["total"]["p_ge1"]),
        L_union_predec_lt1=dict(est=L["predec"]["est"], hi95=L["predec"]["hi95"], p_one_sided=L["predec"]["p_ge1"]),
        L_union_predec_crf_lt1=dict(est=L["predec_crf"]["est"], hi95=L["predec_crf"]["hi95"],
                                    p_one_sided=L["predec_crf"]["p_ge1"]),
    )
    h4b["tests"]["L_noR24_total_lt1"] = dict(est=h4b["L_noR24"]["total"]["est"], hi95=h4b["L_noR24"]["total"]["hi95"],
                                             p_one_sided=h4b["L_noR24"]["total"]["p_ge1"])
    h4b["tests"]["L_noR24_predec_crf_lt1"] = dict(est=h4b["L_noR24"]["predec_crf"]["est"],
                                                  hi95=h4b["L_noR24"]["predec_crf"]["hi95"],
                                                  p_one_sided=h4b["L_noR24"]["predec_crf"]["p_ge1"])
    # LLM-specific estimand (I1): post/pre ratio of gains per marker, against 2018-23 and 2018-22
    for k in ["NAME"] + [k for k in keys_all if FEAT_SET[k] in ("L", "O", "L2", "O2")]:
        h4b.setdefault(k, {})["post_vs_pre_ratio_of_gains"] = {
            g: G(k, g, "2024-26 / 2018-23", variant="post_vs_pre")
            for g in ["total", "predec", "dec", "predec_crf", "exit_crf", "desk_crf"]}
        h4b[k]["post_vs_pre_1822_ratio_of_gains"] = {
            g: G(k, g, "2024-26 / 2018-22", variant="post_vs_pre_1822")
            for g in ["total", "predec", "dec", "predec_crf", "exit_crf", "desk_crf"]}
        h4b[k]["pre_2018_22"] = {g: G(k, g, "2018-22") for g in ["total", "predec", "dec", "predec_crf"]}
        h4b[k]["pre_2018_23"] = {g: G(k, g, "2018-23") for g in ["total", "predec", "dec", "predec_crf"]}
    h4b["postdec_withdrawal_variants"] = {
        v: {k: {g: G(k, g, variant=v) for g in ["exit", "dec", "predec", "predec_crf"]}
            for k in ["NAME", "L_union", "L_noR24", "O_union", "R24", "F24", "style_density"]}
        for v in pd_variants}
    h4b["postdec_withdrawal_counts"] = postdec_counts
    h4b["style_density_reselect"] = dict(info=dens_info, **{
        g: G("style_density", g, variant="density_reselect") for g in ["total", "exit", "predec", "predec_crf",
                                                                        "desk", "dec"]})
    h4b["falsified"] = bool(L["total"]["est"] >= 1)
    for k, v in h4b["tests"].items():
        log(f"H4b {k}: {v}", fh)

    # ---------------- T4.1 continuation-ratio logits
    rows = []
    for era, stages_ in [("2024-26", ["desk", "exit", "decision"]), ("2018-23", ["exit", "decision"])]:
        for stage in stages_:
            for k in keys_primary:
                r = cr_fit(df, k, stage, era)
                if r is not None:
                    rows.append(r)
            log(f"CR logits {era} {stage} done ({time.time() - t0:.0f}s)", fh)
    cr = pd.DataFrame(rows)
    # BH q-values over every T4.1 feature test (PLAN section 0: BH across exploratory marker lists)
    cr["q_bh"] = bh_q(cr.p.to_numpy())
    cr["notable_q05"] = cr.q_bh < 0.05
    # adjusted total gain = product of stage adjusted gains (2024-26). Approximate 95% CI: the continuation-ratio
    # likelihood factorises over stages, so stage estimates are treated as independent; log-scale SEs are taken
    # from each stage's G_adj interval.
    post_cr = cr[(cr.era == "2024-26") & cr.G_adj.notna()] if "G_adj" in cr else cr.iloc[:0]

    def _chain(x):
        lg = np.log(x.G_adj.to_numpy())
        se = (np.log(x.G_adj_hi.to_numpy()) - np.log(x.G_adj_lo.to_numpy())) / (2 * 1.959964)
        tot, set_ = float(lg.sum()), float(np.sqrt((se ** 2).sum()))
        return pd.Series({"G_adj_total": float(np.exp(tot)), "G_adj_total_lo95_approx": float(np.exp(tot - 1.959964 * set_)),
                          "G_adj_total_hi95_approx": float(np.exp(tot + 1.959964 * set_)),
                          "G_raw_total": float(np.prod(x.G_raw)), "n_stages": len(x)})
    chain = post_cr.groupby("feature").apply(_chain, include_groups=False)
    cr.to_csv(OUTDIR / "T4_1_continuation_ratio.csv", index=False)
    chain.to_csv(OUTDIR / "T4_1_adjusted_total.csv")
    log("\nT4.1 (2024-26):\n" + cr[cr.era == "2024-26"][["stage", "feature", "nobs", "OR", "OR_lo", "OR_hi", "p",
                                                         "G_raw", "G_adj"]].round(3).to_string(), fh)
    log("adjusted total gain chain:\n" + chain.round(3).to_string(), fh)

    # ---------------- figures
    fig, data = fig_ladder(gains)
    C.save_fig(fig, "fig_F4_1_stage_ladder", OUTDIR, data=data)
    fig, data = fig_total_by_year(gains)
    C.save_fig(fig, "fig_S4_1_total_gain_by_year", OUTDIR, data=data)

    res = dict(
        meta=dict(n_rows=int(len(df)), years="2018-2026", n_boot=N_BOOT, seed=SEED, pooling_primary="year-standardised",
                  dropped_other_rows_2018=71, style_density_words={k: len(v) for k, v in words.items()},
                  runtime_s=round(time.time() - t0, 1)),
        H4a=h4a, H4b=h4b,
        T4_1=cr.to_dict(orient="records"), T4_1_adjusted_total=chain.reset_index().to_dict(orient="records"),
        gains_2024_26_std=show.to_dict(orient="records"),
    )
    write_json(res, OUTDIR / "stage_gains.json")
    log(f"done in {time.time() - t0:.0f}s", fh)
    fh.close()


if __name__ == "__main__":
    main()
