"""Alternative-explanation and R1-calibration diagnostics for G5 and G6, added by the adversarial audit (2026-10-17).

Everything here is DIAGNOSTIC (NOT PRE-REGISTERED). Nothing changes the pre-registered primary estimate, sample,
outcome, controls, fixed effects or verdict. Unless stated otherwise each re-fit uses core._fit with the primary
controls (core.controls), year^topic50 FE and SEs clustered by topic50.

Parts
  r1_null_continuous  R1 calibration for a continuous feature (G5a, G5b and g5's MiniLM variant). g4/g6 showed that the
                      R1 matched-pairs procedure is shifted downward when there is no association (nearest-neighbour
                      controls are 'hub' papers that sit above their cell mean). g5 used R1 and two pair-difference
                      regressions without checking this. Here the feature is permuted within year (200 times), the
                      within-year terciles and the core R1 pairing are rebuilt, and the R1 statistic and both
                      pair-difference slopes of g5 diagnostic (d) are recomputed under that null. Placebo-adjusted
                      R1 = exp(observed mean log diff - null mean) - 1 (approximate CI from the null SD, as in g4/g6).
  alt_explanations    Alternative explanations, as audit_g1g2.py:
    timing     Preprint exposure time. arXiv-id records only; months from first arXiv posting (from the id) to May of
               the ICLR year, entered as FE bins.
    code       Promotion / reuse: the abstract announces code or a URL.
    paper_type Method vs findings paper (abstract regexes, crude and unvalidated).
    tail       Superstars and zero-citation records: within-year citation percentile outcome; drop the top 5% per
               year; drop zero-citation records.
    retitling  Reverse causation through camera-ready retitling. The WP4 camera-ready audit (audit_pairs.csv, read
               only) gives the arXiv v1 title posted before the decision for 568 accepted 2023-25 papers in this
               sample. The feature is rebuilt on the v1 title (word count; bge v1-title-abstract cosine, z-scored with
               the camera-ready year mean and SD; template regexes from features.py) and used as the exposure on the
               same papers. Title-derived primary controls (G1, G5a) are rebuilt on the v1 title as well.
    combined   arXiv-id records; lead-month FE bins added to year^topic50; code + method + findings indicators.
"""
from __future__ import annotations

import os

import numpy as np
import pandas as pd
import statsmodels.api as sm

from analyses import _core as C
from cites import core
from cites.audit_g1g2 import AUDIT_PAIRS, CODE_RX, FINDING_RX, LEAD_BINS, METHOD_RX, add_columns

LABEL = "diagnostic (not pre-registered; added by the adversarial audit)"
BGE = "BAAI/bge-small-en-v1.5"


# --------------------------------------------------------------------------------------------
# R1 calibration for continuous features
# --------------------------------------------------------------------------------------------
def _masked_E(d: pd.DataFrame) -> np.ndarray:
    """Same embedding as core.matched_pairs: name-masked abstract (unmasked where none, e.g. 2017)."""
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    return E / np.linalg.norm(E, axis=1, keepdims=True)


def _nn_pairs(E, years, tr, co, caliper=0.80):
    T, Cc = [], []
    for y in sorted(np.unique(years)):
        ti = np.where(tr & (years == y))[0]
        ci = np.where(co & (years == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        ok = S[np.arange(len(ti)), j] >= caliper
        T.append(ti[ok])
        Cc.append(ci[j[ok]])
    return np.concatenate(T), np.concatenate(Cc)


def _terciles(x: np.ndarray, years: np.ndarray):
    q = pd.Series(x).groupby(years).rank(pct=True).to_numpy()
    return q >= 2 / 3, q <= 1 / 3


def _slopes(dy, dx, Z):
    """(no-intercept slope on dx, intercept, with-intercept slope on dx), covariate differences Z included."""
    b0 = np.linalg.lstsq(np.column_stack([dx, Z]), dy, rcond=None)[0][0]
    c = np.linalg.lstsq(np.column_stack([np.ones_like(dx), dx, Z]), dy, rcond=None)[0]
    return float(b0), float(c[0]), float(c[1])


def r1_null_continuous(df: pd.DataFrame, F: str, covs: list[str], core_r1: dict | None = None, n_rep: int = 200,
                       seed: int = 0, unit: str = "") -> dict:
    d = df.reset_index(drop=True)
    E = _masked_E(d)
    years, y, x = d.year.to_numpy(), d.y.to_numpy(), d[F].to_numpy(dtype=float)
    Zall = d[covs].to_numpy(dtype=float)

    def run(xv):
        tr, co = _terciles(xv, years)
        T, Cc = _nn_pairs(E, years, tr, co)
        return T, Cc, y[T] - y[Cc], xv[T] - xv[Cc], Zall[T] - Zall[Cc]

    T, Cc, dy, dx, Z = run(x)
    obs = float(dy.mean())
    cm = d.groupby("yt").y.transform("mean").to_numpy()
    out = {"label": LABEL, "feature": F, "unit": unit, "n_pairs": int(len(T)), "observed_pct": float(np.exp(obs) - 1),
           "mean_feature_contrast_in_pairs": float(dx.mean()), "covariates_differenced": covs,
           "treated_y_minus_own_cell_mean": float((y[T] - cm[T]).mean()),
           "controls_y_minus_own_cell_mean": float((y[Cc] - cm[Cc]).mean()),
           "n_unique_controls": int(len(np.unique(Cc))),
           "mechanism_note": "cell = year x topic50 over all papers; controls chosen as nearest neighbours are re-used "
                             "(with replacement) and sit above their cell mean"}
    if core_r1 is not None:
        out["reproduces_core_R1"] = bool(len(T) == core_r1["n_pairs"] and abs(np.exp(obs) - 1 - core_r1["pct"]) < 1e-9)
    # observed pair-difference regressions (SE clustered by control paper, as in g5 pair_scale)
    Zd = pd.DataFrame(Z, columns=[f"d_{c}" for c in covs])
    X0 = Zd.copy()
    X0.insert(0, "d_feature", dx)
    m0 = sm.OLS(dy, X0).fit(cov_type="cluster", cov_kwds={"groups": Cc})
    m1 = sm.OLS(dy, sm.add_constant(X0)).fit(cov_type="cluster", cov_kwds={"groups": Cc})
    pc = lambda b, se: {"pct": float(np.exp(b) - 1), "lo": float(np.exp(b - 1.96 * se) - 1), "hi": float(np.exp(b + 1.96 * se) - 1)}
    out["observed_slope_no_intercept"] = {**pc(m0.params["d_feature"], m0.bse["d_feature"]), "p": float(m0.pvalues["d_feature"]),
                                          "note": "g5 diagnostic (d) 'pair_difference_slope_per_unit'"}
    out["observed_slope_with_intercept"] = {**pc(m1.params["d_feature"], m1.bse["d_feature"]), "p": float(m1.pvalues["d_feature"]),
                                            "intercept_pct": float(np.exp(m1.params["const"]) - 1),
                                            "note": "intercept absorbs any constant shift of the pairing procedure; slope "
                                                    "identified from variation in the feature contrast across pairs"}
    # null: permute the feature within year
    rng = np.random.default_rng(seed)
    idx_by_year = {yy: np.where(years == yy)[0] for yy in np.unique(years)}
    stats, b0s, b1s, a1s = [], [], [], []
    for _ in range(n_rep):
        xp = x.copy()
        for yy, ii in idx_by_year.items():
            xp[ii] = x[rng.permutation(ii)]
        _, _, dyp, dxp, Zp = run(xp)
        stats.append(float(dyp.mean()))
        b0, a1, b1 = _slopes(dyp, dxp, Zp)
        b0s.append(b0)
        b1s.append(b1)
        a1s.append(a1)
    stats, b0s, b1s = np.array(stats), np.array(b0s), np.array(b1s)
    adj = obs - stats.mean()
    se = float(stats.std(ddof=1) * np.sqrt(1 + 1 / n_rep))
    p_lo = (1 + (stats <= obs).sum()) / (n_rep + 1)
    p_hi = (1 + (stats >= obs).sum()) / (n_rep + 1)
    out["null"] = {"n_rep": n_rep, "method": "feature permuted within year; terciles and core R1 pairing rebuilt",
                   "mean_log_diff": float(stats.mean()), "sd_log_diff": float(stats.std(ddof=1)),
                   "pct_at_mean": float(np.exp(stats.mean()) - 1),
                   "q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(stats, [2.5, 97.5])],
                   "slope_no_intercept_null_mean_pct": float(np.exp(b0s.mean()) - 1),
                   "slope_no_intercept_null_q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(b0s, [2.5, 97.5])],
                   "slope_with_intercept_null_mean_pct": float(np.exp(b1s.mean()) - 1),
                   "slope_with_intercept_null_q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(b1s, [2.5, 97.5])],
                   "intercept_null_mean_pct": float(np.exp(np.mean(a1s)) - 1)}
    out["placebo_p_two_sided"] = float(min(1.0, 2 * min(p_lo, p_hi)))
    out["placebo_adjusted"] = {"pct": float(np.exp(adj) - 1), "lo": float(np.exp(adj - 1.96 * se) - 1),
                               "hi": float(np.exp(adj + 1.96 * se) - 1),
                               "note": "exp(observed mean log diff - null mean) - 1; approximate CI from the null SD"}
    sh = float(b0s.mean())
    out["slope_no_intercept_null_corrected"] = {"pct": float(np.exp(m0.params["d_feature"] - sh) - 1),
                                                "lo": float(np.exp(m0.params["d_feature"] - sh - 1.96 * m0.bse["d_feature"]) - 1),
                                                "hi": float(np.exp(m0.params["d_feature"] - sh + 1.96 * m0.bse["d_feature"]) - 1),
                                                "note": "observed no-intercept slope minus its null mean (approximate CI)"}
    return out


# --------------------------------------------------------------------------------------------
# alternative explanations
# --------------------------------------------------------------------------------------------
def _nw(r: dict, d: pd.DataFrame, F: str, binary: bool) -> dict:
    r = dict(r)
    if binary:
        r["n_with"] = int(d[F].sum())
    return r


def _lpm(r: dict) -> dict:
    return {"b_pp": 100 * r["b"], "lo_pp": 100 * (r["b"] - 1.96 * r["se"]), "hi_pp": 100 * (r["b"] + 1.96 * r["se"]),
            "p": r["p"], "n": r["n"]}


def _by(d: pd.DataFrame, F: str, col: str) -> dict:
    return {"with_feature": float(d.loc[d[F] == 1, col].mean()), "without_feature": float(d.loc[d[F] == 0, col].mean())}


def _encode_bge(texts: list[str]) -> np.ndarray:
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(2)
    m = SentenceTransformer(BGE, device="cpu")  # local cache only (offline)
    return m.encode(texts, batch_size=64, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)


def v1_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Accepted audit-pair papers in the analysis frame with v1-title versions of G1, G5a, G5b, G6a, G6b."""
    from features import title_features
    A = pd.read_csv(AUDIT_PAIRS)
    A = A[A.decision == "accepted"][["submission_id", "v1_title", "or_title", "NAME_v1", "NAME_or", "n_words_v1",
                                     "n_words_or", "v1_lag_days", "v1_in_review"]]
    m = df.merge(A, on="submission_id", how="inner").reset_index(drop=True)
    tf = pd.DataFrame([title_features(t) for t in m.v1_title.fillna("")])
    tfo = pd.DataFrame([title_features(t) for t in m.or_title.fillna("")])
    m["G1_name_v1"] = m.NAME_v1.astype(int)
    m["G5a_length5_v1"] = tf.n_words.to_numpy() / 5.0
    m["G6a_meme_v1"] = tf[core.MEME].any(axis=1).astype(int).to_numpy()
    m["G6b_tentative_v1"] = tf[core.TENTATIVE].any(axis=1).astype(int).to_numpy()
    rep = {"G1_name": float((m.NAME_or.astype(int) == m.G1_name).mean()),
           "G5a_length5": float((tfo.n_words.to_numpy() / 5.0 == m.G5a_length5.to_numpy()).mean()),
           "G6a_meme": float((tfo[core.MEME].any(axis=1).astype(int).to_numpy() == m.G6a_meme.to_numpy()).mean()),
           "G6b_tentative": float((tfo[core.TENTATIVE].any(axis=1).astype(int).to_numpy() == m.G6b_tentative.to_numpy()).mean())}
    # G5b on the v1 title: bge cosine to the (final) abstract embedding, z-scored with the camera-ready year mean / SD
    Ea = C.load_embedding(m, "abstract", "bge-small-en-v1.5")
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    Ev = _encode_bge(m.v1_title.fillna("").tolist())
    Eo = _encode_bge(m.or_title.fillna("").tolist())
    cos_v1, cos_or = (Ev * Ea).sum(1), (Eo * Ea).sum(1)
    mu = df.groupby("year").title_abs_cos.mean()
    sd = df.groupby("year").title_abs_cos.std()
    m["G5b_informative_v1"] = (cos_v1 - m.year.map(mu).to_numpy()) / m.year.map(sd).to_numpy()
    g5b_or = (cos_or - m.year.map(mu).to_numpy()) / m.year.map(sd).to_numpy()
    rep["G5b_informative_max_abs_diff_reencoded_vs_frozen"] = float(np.abs(g5b_or - m.G5b_informative.to_numpy()).max())
    m.attrs["reproduction"] = rep
    m["title_changed"] = (m.v1_title.fillna("").str.strip().str.lower() != m.or_title.fillna("").str.strip().str.lower()).astype(int)
    return m


V1_SWAP = {"G1_name": "G1_name_v1", "G5a_length5": "G5a_length5_v1"}


def _retitling(d: pd.DataFrame, m: pd.DataFrame, F: str, binary: bool) -> dict:
    Cc = core.controls(F)
    Fv = f"{F}_v1"
    Cv = [V1_SWAP.get(c, c) for c in Cc]
    out = {"label": LABEL, "source": "outputs/snapshot/audit_pairs.csv (accepted, arXiv v1 posted before the decision)",
           "n_papers": int(len(m)), "years": sorted(int(y) for y in m.year.unique()),
           "n_title_changed": int(m.title_changed.sum()),
           "reproduction_of_camera_ready_feature_from_or_title": m.attrs["reproduction"],
           "v1_controls": Cv,
           "camera_ready_exposure_same_papers": _nw(core._fit(m, "y", F, Cc), m, F, binary),
           "v1_exposure_same_papers": core._fit(m, "y", Fv, Cv),
           "note": "small, selected subsample (accepted 2023-25 papers with a pre-decision arXiv v1); SEs are wide"}
    if binary:
        out["n_with_camera_ready"] = int(m[F].sum())
        out["n_with_v1"] = int(m[Fv].sum())
        out["added_at_camera_ready"] = int(((m[F] == 1) & (m[Fv] == 0)).sum())
        out["removed_at_camera_ready"] = int(((m[F] == 0) & (m[Fv] == 1)).sum())
        st = m[m[F] == m[Fv]]
    else:
        ch = m[F] - m[Fv]
        out["corr_camera_ready_v1"] = float(np.corrcoef(m[F], m[Fv])[0, 1])
        out["mean_change_cr_minus_v1"] = float(ch.mean())
        out["mean_abs_change_among_changed_titles"] = float(ch[m.title_changed == 1].abs().mean())
        st = m[m.title_changed == 0]
    out["stable_status_papers_only"] = _nw(core._fit(st, "y", F, Cc), st, F, binary)
    s = d[d.year.isin(m.year.unique())]
    out["full_sample_same_years_primary_spec"] = _nw(core._fit(s, "y", F, Cc), s, F, binary)
    return out


def alt_explanations(df: pd.DataFrame, F: str, binary: bool, v1: pd.DataFrame | None = None) -> dict:
    d = add_columns(df)
    Cc = core.controls(F)
    out = {"label": LABEL, "feature": F, "doc": __doc__.split("alt_explanations")[1].strip()}
    a = d[d.arxiv_month_idx.notna()]
    tim = {"label": LABEL,
           "lead_months_on_feature_primary_controls": core._fit(a, "lead_months", F, Cc),
           "arxiv_only_primary_spec": _nw(core._fit(a, "y", F, Cc), a, F, binary),
           "arxiv_only_plus_lead_bin_fe": _nw(core._fit(a, "y", F, Cc, fe="year^topic50 + lead_bin"), a, F, binary),
           "lead_bins_months": LEAD_BINS}
    if binary:
        tim["mean_lead_months"] = _by(a, F, "lead_months")
    out["timing"] = tim
    code = {"label": LABEL, "regex": CODE_RX.pattern,
            "code_on_feature_lpm_pp": _lpm(core._fit(d, "code_link", F, Cc)),
            "plus_code_control": core._fit(d, "y", F, Cc + ["code_link"]),
            "code_indicator_coef": core._fit(d, "y", "code_link", Cc + [F])}
    if binary:
        code["share"] = _by(d, F, "code_link")
    out["code"] = code
    pt = {"label": LABEL, "method_regex": METHOD_RX.pattern, "finding_regex": FINDING_RX.pattern,
          "method_on_feature_lpm_pp": _lpm(core._fit(d, "method_abs", F, Cc)),
          "finding_on_feature_lpm_pp": _lpm(core._fit(d, "finding_abs", F, Cc)),
          "plus_method_and_finding_controls": core._fit(d, "y", F, Cc + ["method_abs", "finding_abs"]),
          "within_method_abstracts": _nw(core._fit(d[d.method_abs == 1], "y", F, Cc), d[d.method_abs == 1], F, binary),
          "within_non_method_abstracts": _nw(core._fit(d[d.method_abs == 0], "y", F, Cc), d[d.method_abs == 0], F, binary),
          "within_finding_abstracts": _nw(core._fit(d[d.finding_abs == 1], "y", F, Cc), d[d.finding_abs == 1], F, binary)}
    if binary:
        pt["share_method"] = _by(d, F, "method_abs")
        pt["share_finding"] = _by(d, F, "finding_abs")
    out["paper_type"] = pt
    tail = {"label": LABEL}
    r = core._fit(d, "cite_pctile", F, Cc)
    tail["cite_percentile_outcome_pp"] = {"b_pp": r["b"], "lo_pp": r["b"] - 1.96 * r["se"], "hi_pp": r["b"] + 1.96 * r["se"],
                                          "p": r["p"], "n": r["n"]}
    cap5 = d.groupby("year").cites.transform(lambda s: s.quantile(0.95))
    tail["drop_top5pct_per_year"] = _nw(core._fit(d[d.cites <= cap5], "y", F, Cc), d[d.cites <= cap5], F, binary)
    tail["drop_zero_citation_records"] = _nw(core._fit(d[d.cites > 0], "y", F, Cc), d[d.cites > 0], F, binary)
    out["tail"] = tail
    if v1 is not None:
        out["retitling"] = _retitling(d, v1, F, binary)
    comb = core._fit(a, "y", F, Cc + ["code_link", "method_abs", "finding_abs"], fe="year^topic50 + lead_bin")
    out["combined_arxiv_only_lead_fe_code_method_finding"] = {**_nw(comb, a, F, binary), "label": LABEL}
    return out


def fmt(r: dict) -> str:
    return f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"


def summary_lines(res: dict) -> list[str]:
    f = lambda r: f"{fmt(r)} n={r.get('n')}" + (f" n_with={r['n_with']}" if "n_with" in r else "")
    t, c, p, ta = res["timing"], res["code"], res["paper_type"], res["tail"]
    L = [f"timing: lead on F {t['lead_months_on_feature_primary_controls']['b']:+.2f} mo (p {t['lead_months_on_feature_primary_controls']['p']:.2g}); "
         f"arXiv-only {f(t['arxiv_only_primary_spec'])}; + lead FE {f(t['arxiv_only_plus_lead_bin_fe'])}",
         f"code: lpm {c['code_on_feature_lpm_pp']['b_pp']:+.2f} pp; + code {f(c['plus_code_control'])}; code coef {fmt(c['code_indicator_coef'])}",
         f"paper type: method lpm {p['method_on_feature_lpm_pp']['b_pp']:+.2f} pp, finding lpm {p['finding_on_feature_lpm_pp']['b_pp']:+.2f} pp; "
         f"+ both {f(p['plus_method_and_finding_controls'])}; within method {f(p['within_method_abstracts'])}; "
         f"within non-method {f(p['within_non_method_abstracts'])}",
         f"tail: pctile {ta['cite_percentile_outcome_pp']['b_pp']:+.2f} [{ta['cite_percentile_outcome_pp']['lo_pp']:+.2f}, "
         f"{ta['cite_percentile_outcome_pp']['hi_pp']:+.2f}]; drop top5 {f(ta['drop_top5pct_per_year'])}; drop zero {f(ta['drop_zero_citation_records'])}"]
    if "retitling" in res:
        rt = res["retitling"]
        L.append(f"retitling: n {rt['n_papers']} changed {rt['n_title_changed']}; CR {f(rt['camera_ready_exposure_same_papers'])}; "
                 f"v1 {f(rt['v1_exposure_same_papers'])}; stable {f(rt['stable_status_papers_only'])}; "
                 f"full same years {f(rt['full_sample_same_years_primary_spec'])}; repro {rt['reproduction_of_camera_ready_feature_from_or_title']}"
                 + (f"; added {rt['added_at_camera_ready']} removed {rt['removed_at_camera_ready']}" if "added_at_camera_ready" in rt
                    else f"; corr {rt['corr_camera_ready_v1']:.3f}"))
    L.append(f"combined: {f(res['combined_arxiv_only_lead_fe_code_method_finding'])}")
    return L


def r1_lines(r: dict) -> str:
    n = r["null"]
    return (f"R1 null {r['feature']}: pairs {r['n_pairs']} obs {100 * r['observed_pct']:+.1f}% null mean {100 * n['pct_at_mean']:+.1f}% "
            f"(95% {[round(100 * v, 1) for v in n['q2.5_q97.5_pct']]}) placebo p {r['placebo_p_two_sided']:.3f} adj {fmt(r['placebo_adjusted'])} | "
            f"slope no-int obs {fmt(r['observed_slope_no_intercept'])} null mean {100 * n['slope_no_intercept_null_mean_pct']:+.1f}% "
            f"corrected {fmt(r['slope_no_intercept_null_corrected'])} | slope with-int obs {fmt(r['observed_slope_with_intercept'])} "
            f"null mean {100 * n['slope_with_intercept_null_mean_pct']:+.1f}% | repro {r.get('reproduces_core_R1')}")


# --------------------------------------------------------------------------------------------
# content controls, split-record mechanism, MiniLM measure
# --------------------------------------------------------------------------------------------
def content_controls(df: pd.DataFrame, features: list[str]) -> dict:
    """Is the association content leakage beyond the 20 bge PCs? Re-fit with 50 / 100 bge abstract PCs, with 20 MiniLM
    abstract PCs added, and with 20 MiniLM PCs replacing the bge PCs (the G5b measure is itself bge-based)."""
    from sklearn.decomposition import PCA
    Ea = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    Em = C.load_embedding(df, "abstract", "all-MiniLM-L6-v2")
    Em /= np.linalg.norm(Em, axis=1, keepdims=True)
    P = PCA(n_components=100, random_state=0).fit_transform(Ea)
    Q = PCA(n_components=20, random_state=0).fit_transform(Em)
    d = df.copy()
    for k in range(100):
        d[f"bpc{k}"] = P[:, k]
    for k in range(20):
        d[f"mpc{k}"] = Q[:, k]
    out = {"label": LABEL, "first_20_bge_pcs_equal_core_pcs": bool(np.allclose(P[:, :20], df[[f"pc{k}" for k in range(20)]].to_numpy(), atol=1e-4))}
    for F in features:
        base = [c for c in core.controls(F) if not c.startswith("pc")]
        out[F] = {"primary": core.primary(d, F),
                  "bge_50_pcs": core._fit(d, "y", F, base + [f"bpc{k}" for k in range(50)]),
                  "bge_100_pcs": core._fit(d, "y", F, base + [f"bpc{k}" for k in range(100)]),
                  "bge_20_plus_minilm_20_pcs": core._fit(d, "y", F, core.controls(F) + [f"mpc{k}" for k in range(20)]),
                  "minilm_20_pcs_instead_of_bge": core._fit(d, "y", F, base + [f"mpc{k}" for k in range(20)])}
    return out


def split_record_mechanism(df: pd.DataFrame) -> dict:
    """Is a venue record without an arXiv id a split S2 record (artefact) or a paper that is not on arXiv (exposure)?
    Among accepted audit-pair papers every paper has a pre-decision arXiv v1, so a missing arXiv id on the S2 venue
    record cannot mean 'not on arXiv'. Compare citations by venue-record arXiv status, and test whether camera-ready
    retitling (which can stop S2 merging the two records) and title length predict a missing id."""
    A = pd.read_csv(AUDIT_PAIRS)
    A = A[A.decision == "accepted"][["submission_id", "v1_title", "or_title"]]
    m = df.merge(A, on="submission_id", how="inner").reset_index(drop=True)
    m["has_arxiv"] = m.arxiv.notna().astype(int)
    m["title_changed"] = (m.v1_title.fillna("").str.strip().str.lower() != m.or_title.fillna("").str.strip().str.lower()).astype(int)
    m["len_tercile"] = pd.qcut(m.n_words.rank(method="first"), 3, labels=["short", "middle", "long"])
    yd = pd.get_dummies(m.year, prefix="yr", drop_first=True, dtype=float)
    ols = lambda yv, xs: sm.OLS(m[yv].astype(float), sm.add_constant(pd.concat([m[xs].astype(float), yd], axis=1))).fit(cov_type="HC1")
    r = ols("has_arxiv", ["title_changed", "G5a_length5"])
    r2 = ols("title_changed", ["G5a_length5"])
    r3 = ols("y", ["has_arxiv"])
    ci = lambda res, k: [float(res.params[k] - 1.96 * res.bse[k]), float(res.params[k] + 1.96 * res.bse[k])]
    return {"label": LABEL, "n_papers": int(len(m)), "years": sorted(int(y) for y in m.year.unique()),
            "share_venue_record_with_arxiv_id": float(m.has_arxiv.mean()),
            "mean_y_by_venue_arxiv_status": {int(k): float(v) for k, v in m.groupby("has_arxiv").y.mean().items()},
            "median_cites_by_venue_arxiv_status": {int(k): float(v) for k, v in m.groupby("has_arxiv").cites.median().items()},
            "y_gap_has_minus_no_arxiv_year_fe": {"b": float(r3.params["has_arxiv"]), "ci95": ci(r3, "has_arxiv")},
            "share_with_arxiv_id_by_title_changed": {int(k): float(v) for k, v in m.groupby("title_changed").has_arxiv.mean().items()},
            "n_by_title_changed": {int(k): int(v) for k, v in m.groupby("title_changed").size().items()},
            "by_length_tercile": m.groupby("len_tercile", observed=True).agg(
                mean_words=("n_words", "mean"), share_with_arxiv_id=("has_arxiv", "mean"),
                share_title_changed=("title_changed", "mean"), n=("y", "size")).reset_index().to_dict(orient="records"),
            "lpm_has_arxiv_on_title_changed_and_length": {
                "title_changed_pp": 100 * float(r.params["title_changed"]), "title_changed_ci_pp": [100 * v for v in ci(r, "title_changed")],
                "per_5_words_pp": 100 * float(r.params["G5a_length5"]), "per_5_words_ci_pp": [100 * v for v in ci(r, "G5a_length5")],
                "model": "OLS, year FE, HC1"},
            "lpm_title_changed_on_length_per_5_words_pp": {"b_pp": 100 * float(r2.params["G5a_length5"]),
                                                           "ci_pp": [100 * v for v in ci(r2, "G5a_length5")]}}


def minilm_informativeness(df: pd.DataFrame) -> pd.Series:
    """g5 diagnostic (b) measure: all-MiniLM-L6-v2 title-abstract cosine, z within year."""
    Et = C.load_embedding(df, "title", "all-MiniLM-L6-v2")
    Ea = C.load_embedding(df, "abstract", "all-MiniLM-L6-v2")
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    s = pd.Series((Et * Ea).sum(1), index=df.index)
    return s.groupby(df.year).transform(lambda v: (v - v.mean()) / v.std())
