"""G3: question titles and citations among accepted ICLR papers 2017-2025.

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here).

What this module does
  1. Primary (pre-registered): reads the frozen estimate and Holm p for G3_question from outputs/cites/primary.json
     and re-computes it with core.primary as a reproduction check (the frozen numbers are the ones reported).
  2. Robustness R1-R7 (pre-registered): core.robustness.
  3. Verdict (pre-registered rule): core.verdict(frozen primary, robustness, frozen Holm p).
  4. Secondary (pre-registered, prereg section 6, common to all questions; no multiplicity claim):
       - joint model with all 8 primary features;
       - heterogeneity by LLM-topic papers.
  5. Diagnostics (NOT pre-registered; every block is labelled so in results.json):
       (a) S2 split-record artefact: arXiv-id share by G3 status (raw, by era, adjusted); primary spec within
           records with / without an arXiv id and with an arXiv-id indicator; QC split-record sample;
       (b) measure validity: the most- and least-cited question titles (within-year percentile), the V1
           detector validation (outputs/validation/v1_detector_metrics.csv, read only), '?' encoding-artefact
           scan, question forms (descriptive counts only);
       (c) power and fragility: minimum detectable effects for n = 223, whether the pre-registered
           'no meaningful difference' band is attainable, and the influence of the most-cited question titles;
       (d) overlap with other title features and paper type: crosstabs, + G6a / G1 controls, meme ('Do X
           really ...?') and named titles excluded, + method-paper indicator;
       (e) why R1 (matched pairs) differs from the primary: pair composition and balance, pair-level regression
           adjustment, caliper / era / arXiv-only variants, and matching against plain (non-named, non-assertive) titles.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g3
Writes outputs/cites/G3/{results.json, fig.png}.
"""
from __future__ import annotations

import json
import re
import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy.stats import norm  # noqa: E402

from cites import core  # noqa: E402

warnings.filterwarnings("ignore")

F = "G3_question"
OUT = core.OUT / "G3"
VALID = core.OUT.parent / "validation"
DIAG = "diagnostic (not pre-registered)"
SEC = "pre-specified secondary (prereg section 6; no multiplicity claim)"
METHOD_RX = re.compile(r"\b(?:we propose|we introduce|we present|this paper proposes)\b", re.I)  # same regex as g1.py
YESNO = {"can", "could", "do", "does", "did", "is", "are", "was", "were", "should", "will", "would", "has", "have", "must", "shall"}
WH = {"how", "what", "what's", "why", "when", "where", "which", "who", "whose", "whom"}
ROB_LABEL = {
    "R1_matched_pairs": "R1 content-matched pairs",
    "R2_ppml_counts": "R2 PPML on counts (sign check)",
    "R3_influential": "R3 influential citations",
    "R4_drop_top1pct": "R4 drop top 1% per year",
    "R5_era_2017_21": "R5 2017-21 only",
    "R5_era_2022_25": "R5 2022-25 only",
    "R6_team_prior_2022_25": "R6 2022-25 + team prior",
    "R7_year_plus_topic100_fe": "R7 year + topic100 FE",
}


# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def fmt(r: dict) -> str:
    if r.get("pct") is None:
        return "n/a"
    return f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [float(c - h), float(c + h)]


def share(x: pd.Series) -> dict:
    x = x.astype(int)
    k, n = int(x.sum()), int(len(x))
    return {"share": k / n if n else None, "ci95_wilson": wilson(k, n), "k": k, "n": n}


def lpm_pp(r: dict) -> dict:
    """core._fit result for a 0/1 outcome as a linear-probability difference in percentage points."""
    return {"b_pp": 100 * r["b"], "lo_pp": 100 * (r["b"] - 1.96 * r["se"]), "hi_pp": 100 * (r["b"] + 1.96 * r["se"]),
            "p": r["p"], "n": r["n"], "model": "linear probability, primary controls and year^topic50 FE, SE clustered by topic50"}


def fit_n(d: pd.DataFrame, extra=(), y="y") -> dict:
    r = core._fit(d, y, F, core.controls(F, list(extra)))
    r["n_with"] = int(d[F].sum())
    return r


def ratio(r: dict) -> dict:
    return {"b": r["b"], "se": r["se"], "p": r["p"], "ratio": float(np.exp(r["b"])),
            "ratio_lo": float(np.exp(r["b"] - 1.96 * r["se"])), "ratio_hi": float(np.exp(r["b"] + 1.96 * r["se"]))}


def era(y):
    return "2017-21" if y <= 2021 else "2022-25"


# --------------------------------------------------------------------------------------------
# pre-registered parts
# --------------------------------------------------------------------------------------------
def primary_block(df: pd.DataFrame) -> dict:
    frozen = json.load(open(core.OUT / "primary.json"))
    prim = frozen["primary"][F]
    rep = core.primary(df, F)
    diff = {k: abs(prim[k] - rep[k]) for k in ["b", "se", "p", "pct", "lo", "hi"]}
    ok = diff["b"] < 1e-8 and diff["se"] < 1e-8 and prim["n"] == rep["n"] and prim["n_with"] == rep["n_with"]
    return {"frozen": {**prim, "source": "outputs/cites/primary.json (Holm across the 8 primary tests)"}, "reproduced": rep,
            "max_abs_diff": max(diff.values()), "reproduction_ok": bool(ok),
            "n_papers_frame": int(len(df)), "n_papers_frozen": int(frozen["n_papers"])}


def secondary_joint(df: pd.DataFrame) -> dict:
    others = [f for f in core.FEATURES if f != F]
    r = core._fit(df, "y", F, core.controls(F, others))
    r["model"] = "y ~ all 8 primary features + primary controls | year^topic50"
    r["note"] = ("G2_assertive is defined as 'assertive verb AND not a question', so G2 and G3 never co-occur; in the joint "
                 "model G3 is compared with titles that are neither questions nor assertive (nor carry the other features).")
    r["label"] = SEC
    return r


def secondary_llm(df: pd.DataFrame) -> dict:
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(bool).astype(int)
    d["G3_in_llm"] = d[F] * d.llm
    d["G3_in_nonllm"] = d[F] * (1 - d.llm)
    d["G3_x_llm"] = d[F] * d.llm
    llm = core._fit(d, "y", "G3_in_llm", core.controls(F, ["G3_in_nonllm", "llm"]))
    non = core._fit(d, "y", "G3_in_nonllm", core.controls(F, ["G3_in_llm", "llm"]))
    inter = core._fit(d, "y", "G3_x_llm", core.controls(F, [F, "llm"]))
    llm["n_with"] = int(d.G3_in_llm.sum())
    non["n_with"] = int(d.G3_in_nonllm.sum())
    return {"label": SEC, "llm_topic_papers": llm, "non_llm_topic_papers": non,
            "difference_llm_minus_non": ratio(inter), "n_llm_topic_papers": int(d.llm.sum()),
            "share_llm_topic": {"question": float(d.loc[d[F] == 1, "llm"].mean()), "other": float(d.loc[d[F] == 0, "llm"].mean())},
            "note": "One model with G3 split by llm_topic plus an llm_topic main effect; 'difference' is the G3 x llm_topic "
                    "interaction (ratio of the two citation multipliers)."}


# --------------------------------------------------------------------------------------------
# diagnostics (not pre-registered)
# --------------------------------------------------------------------------------------------
def diag_arxiv(df: pd.DataFrame) -> dict:
    """(a) A venue record without an arXiv id may miss citations credited to a separate arXiv record
    (qc_split_records.jsonl). If that is more common in one G3 group, the primary estimate is biased."""
    d = df.assign(has_arxiv=df.arxiv.notna().astype(int), multi_s2=(df.n_s2.fillna(1) > 1).astype(int), era=df.year.map(era))
    out = {"label": DIAG}
    out["arxiv_share"] = {"question": share(d.loc[d[F] == 1, "has_arxiv"]), "other": share(d.loc[d[F] == 0, "has_arxiv"])}
    out["arxiv_share_by_era"] = {e: {"question": share(g.loc[g[F] == 1, "has_arxiv"]), "other": share(g.loc[g[F] == 0, "has_arxiv"])}
                                 for e, g in d.groupby("era")}
    out["arxiv_share_diff_adjusted_pp"] = lpm_pp(core._fit(d, "has_arxiv", F, core.controls(F)))
    out["multi_record_share"] = {"question": share(d.loc[d[F] == 1, "multi_s2"]), "other": share(d.loc[d[F] == 0, "multi_s2"])}
    out["zero_citation_share"] = {"question": share(d.loc[d[F] == 1, "cites"] == 0), "other": share(d.loc[d[F] == 0, "cites"] == 0)}
    out["primary_spec_arxiv_only"] = fit_n(d[d.has_arxiv == 1])
    out["primary_spec_no_arxiv_only"] = fit_n(d[d.has_arxiv == 0])
    out["primary_spec_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, ["has_arxiv"]))
    # difference between the two subsets in one model; controls and FE interacted with has_arxiv (as in g1.py)
    dd = d.copy()
    dd["G3_x_noarxiv"] = dd[F] * (1 - dd.has_arxiv)
    ctrl = core.controls(F)
    for c in ctrl:
        dd[f"{c}_na"] = dd[c] * (1 - dd.has_arxiv)
    inter = core._fit(dd, "y", "G3_x_noarxiv", ctrl + [F] + [f"{c}_na" for c in ctrl], fe="year^topic50^has_arxiv")
    out["difference_no_arxiv_minus_arxiv"] = {**ratio(inter), "model": "G3 x no-arXiv interaction; controls and year^topic50 FE "
                                                                        "interacted with has_arxiv"}
    q = pd.read_json(core.OUT / "qc_split_records.jsonl", lines=True)
    q = q.merge(d[["submission_id", F]], left_on="sid", right_on="submission_id", how="left")
    q["split"] = q.match_pid.notna() & (q.match_pid != q.venue_pid)
    out["qc_split_sample"] = {
        "n_checked": int(len(q)), "n_split": int(q.split.sum()),
        "n_checked_question": int((q[F] == 1).sum()), "n_split_question": int((q.split & (q[F] == 1)).sum()),
        "note": "Random sample of matched records without an arXiv id (qc_split.py; file may still be growing). Sizes the "
                "artefact only; far too few question titles for a comparison."}
    return out


def v1_validation() -> dict:
    """V1 measurement validation of the 'question' detector ('?' in title) against the adjudicated consensus of two
    blind LLM annotation passes (outputs/validation; read only). Sample = all ICLR submissions 2017-2026."""
    out = {"label": DIAG, "source": "outputs/validation/v1_detector_metrics.csv and v1_consensus.csv (read only)"}
    m = pd.read_csv(VALID / "v1_detector_metrics.csv")
    m = m[(m.detector == "question") & (m.block == "all")]
    cols = ["n_items", "n_det_pos", "n_truth_pos", "n_fp", "n_fn", "precision", "precision_lo", "precision_hi",
            "recall", "recall_lo", "recall_hi", "specificity", "specificity_lo", "specificity_hi"]
    out["metrics_all_years"] = {r.estimator: {c: getattr(r, c) for c in cols} for r in m.itertuples()}
    c = pd.read_csv(VALID / "v1_consensus.csv")
    out["consensus_crosstab_detector_vs_truth"] = {"det1_true1": int(((c.question == True) & (c.t_question == 1)).sum()),  # noqa: E712
                                                   "det1_true0": int(((c.question == True) & (c.t_question == 0)).sum()),  # noqa: E712
                                                   "det0_true1": int(((c.question == False) & (c.t_question == 1)).sum()),  # noqa: E712
                                                   "det0_true0": int(((c.question == False) & (c.t_question == 0)).sum())}  # noqa: E712
    k = out["consensus_crosstab_detector_vs_truth"]
    out["plain_wilson_on_consensus_items"] = {
        "precision": wilson(k["det1_true1"], k["det1_true1"] + k["det1_true0"]),
        "recall": wilson(k["det1_true1"], k["det1_true1"] + k["det0_true1"]),
        "point_precision": k["det1_true1"] / (k["det1_true1"] + k["det1_true0"]),
        "point_recall": k["det1_true1"] / (k["det1_true1"] + k["det0_true1"]),
        "note": "unweighted Wilson 95% CI over all 1,400 consensus items (main + hard); the stratified estimator's "
                "100-100% precision CI understates uncertainty with so few positive items"}
    fn = c[(c.question == False) & (c.t_question == 1)]  # noqa: E712
    out["false_negatives"] = [{"year": int(r.year), "title": r.title} for r in fn.itertuples()]
    out["note"] = ("Codebook: 'y' if the title or any part of it is a direct question; indirect question phrases without '?' "
                   "('How Transformers Learn Syntax') are 'n'. Annotator pass A vs B kappa = 1.000 for question.")
    return out


def qform(t: str) -> str:
    """Descriptive question form: where the question sits and how it opens."""
    if ":" in t and "?" in t.split(":", 1)[1] and "?" not in t.split(":", 1)[0]:
        seg = t.split(":", 1)[1].strip()
        pos = "subtitle"
    else:
        seg = t.split("?", 1)[0]
        seg = re.split(r"[:.!]\s+", seg)[-1].strip() if re.search(r"[:.!]\s+", seg) else seg.strip()
        pos = "main"
    w = seg.split()[0].lower().strip("\"'“”‘’(") if seg.split() else ""
    kind = "yes/no" if w in YESNO else ("wh-" if w in WH else "other opener")
    return f"{pos} | {kind}"


def diag_titles(df: pd.DataFrame) -> dict:
    """(b) measure validity: who are the most- and least-cited question titles?"""
    d = df.assign(pctile=df.groupby("year").cites.rank(pct=True), has_arxiv=df.arxiv.notna().astype(int))
    Q = d[d[F] == 1].copy()
    Q["form"] = Q.title.map(qform)
    row = lambda r: {"title": r.title, "year": int(r.year), "cites": int(r.cites), "pctile_in_year": round(float(r.pctile), 3),
                     "named": int(r.G1_name), "meme": int(r.G6a_meme), "llm_topic": int(bool(r.llm_topic) if pd.notna(r.llm_topic) else 0),
                     "venue_record_has_arxiv_id": int(r.has_arxiv), "form": r.form}
    top = Q.sort_values(["pctile", "cites"], ascending=[False, False]).head(15)
    bot = Q.sort_values(["pctile", "cites", "year"], ascending=[True, True, True]).head(15)
    # '?' that sits between two word characters looks like an encoding artefact (e.g. 'Schr?dinger'), not a question
    mid = Q[Q.title.str.contains(r"\w\?\w", regex=True)]
    forms = Q.groupby("form").agg(n=("title", "size"), median_pctile=("pctile", "median")).sort_values("n", ascending=False)
    return {"label": DIAG,
            "ranking": "within-year citation percentile among all 8,602 papers (age-adjusted); raw S2 count shown",
            "top15": [row(r) for r in top.itertuples()], "bottom15": [row(r) for r in bot.itertuples()],
            "pctile_distribution_question": {k: float(v) for k, v in Q.pctile.quantile([0.1, 0.25, 0.5, 0.75, 0.9]).items()},
            "median_pctile_other": float(d.loc[d[F] == 0, "pctile"].median()),
            "question_by_year": Q.year.value_counts().sort_index().to_dict(),
            "share_by_year": {int(k): float(v) for k, v in d.groupby("year")[F].mean().items()},
            "share_of_question_titles_from_2025": float((Q.year == 2025).mean()),
            "question_mark_between_letters": {"n": int(len(mid)), "titles": mid.title.tolist(),
                                              "note": "possible encoding artefacts; each listed title was read by eye"},
            "multiple_question_marks": int((Q.title.str.count(r"\?") > 1).sum()),
            "question_forms_descriptive": {k: {"n": int(r.n), "median_pctile_in_year": float(r.median_pctile)} for k, r in forms.iterrows()},
            "question_forms_note": "Descriptive only (counts and raw within-year percentiles, no controls, no tests); "
                                   "cells are too small for inference.",
            "v1_validation": v1_validation()}


def diag_power(df: pd.DataFrame, pj: dict, rob: dict) -> dict:
    """(c) power and fragility for a rare binary exposure (n = 223)."""
    se = pj["se"]
    zb = norm.ppf(0.80)
    mde = {}
    for nm, a in [("alpha_0.05_unadjusted", 0.05), ("alpha_0.0167_holm_step_of_G3", 0.05 / 3), ("alpha_0.00625_bonferroni_8", 0.05 / 8)]:
        z = norm.ppf(1 - a / 2)
        b = (z + zb) * se
        mde[nm] = {"alpha": a, "mde_b": float(b), "mde_pct_up": float(np.exp(b) - 1), "mde_pct_down": float(np.exp(-b) - 1)}
    pw = {}
    for eff in [0.10, 0.20, 0.30]:
        b = np.log1p(eff)
        pw[f"+{int(eff * 100)}%"] = {nm: float(norm.cdf(b / se - norm.ppf(1 - m["alpha"] / 2)) + norm.cdf(-b / se - norm.ppf(1 - m["alpha"] / 2)))
                                     for nm, m in mde.items()}
    # pre-registered 'no meaningful difference' band: 95% CI of exp(b)-1 inside (-10%, +10%)
    lo_b, hi_b = np.log(0.9), np.log(1.1)
    width_needed = hi_b - lo_b
    se_max_any = width_needed / (2 * 1.96)          # CI fits only if 2*1.96*se < band width (point estimate at band centre)
    centre = (lo_b + hi_b) / 2
    # SE at which a true effect of 0 gives an 80% chance that the 95% CI lies inside the band
    from scipy.optimize import brentq
    p_in = lambda s: norm.cdf((hi_b - 1.96 * s) / s) - norm.cdf((lo_b + 1.96 * s) / s)
    se_80 = brentq(lambda s: p_in(s) - 0.80, 1e-4, se_max_any - 1e-6)
    n = pj["n_with"]
    # empirical SE scaling across the 6 binary primary features (log se on log n_with)
    P = json.load(open(core.OUT / "primary.json"))["primary"]
    xs = np.log([P[f]["n_with"] for f in core.BINARY])
    ys = np.log([P[f]["se"] for f in core.BINARY])
    slope = float(np.polyfit(xs, ys, 1)[0])
    n_needed = lambda s_target, k: float(n * (se / s_target) ** (1 / k))
    equiv = {"band_pct": [-10, 10], "ci_width_log_now": float(2 * 1.96 * se), "band_width_log": float(width_needed),
             "attainable_at_current_se": bool(2 * 1.96 * se < width_needed),
             "prob_ci_inside_band_if_true_effect_0": float(max(0.0, p_in(se))) if 2 * 1.96 * se < width_needed else 0.0,
             "se_needed_for_ci_to_fit_at_all": float(se_max_any), "se_needed_for_80pct_equivalence_power_if_true_0": float(se_80),
             "band_centre_log": float(centre),
             "n_question_titles_needed_80pct": {"se_prop_1_over_sqrt_n": n_needed(se_80, 0.5),
                                                 f"empirical_slope_{slope:.2f}": n_needed(se_80, -slope)},
             "empirical_se_slope_across_binary_features": slope,
             "note": "Rough: assumes the SE scales with the number of question titles only (1/sqrt(n), or the empirical "
                     "slope of log SE on log n_with across the six binary primary features)."}
    # fragility: drop the k most-cited question titles (biased downward by construction) and a symmetric trim
    d = df.assign(pctile=df.groupby("year").cites.rank(pct=True))
    Q = d[d[F] == 1].sort_values(["pctile", "cites"], ascending=[False, False])
    drop_top, trim_sym = {}, {}
    for k in [1, 3, 5, 10, 20]:
        drop_top[str(k)] = fit_n(d.drop(index=Q.index[:k]))
        trim_sym[str(k)] = fit_n(d.drop(index=list(Q.index[:k]) + list(Q.index[-k:])))
    return {"label": DIAG, "n_question": n, "primary_se_b": se, "ci95_halfwidth_log": float(1.96 * se),
            "mde_80pct_power": mde, "power_for_true_effects": pw, "equivalence_band": equiv,
            "R1_n_pairs": rob["R1_matched_pairs"].get("n_pairs"),
            "R5_n_question_by_era": {"2017-21": int(df.loc[df.year <= 2021, F].sum()), "2022-25": int(df.loc[df.year >= 2022, F].sum())},
            "drop_k_most_cited_question_titles": drop_top,
            "trim_k_most_and_k_least_cited_question_titles": trim_sym,
            "fragility_note": "Most-cited = highest within-year citation percentile. Dropping only the top k is biased "
                              "downward by construction (a fragility check, not an estimate); the symmetric trim drops the "
                              "k highest and k lowest."}


def diag_overlap(df: pd.DataFrame) -> dict:
    """(d) overlap with other title features and with paper type (method vs analysis)."""
    d = df.assign(method=df.abstract.fillna("").map(lambda a: int(bool(METHOD_RX.search(a)))))
    d["do_really"] = d.tpl_do_really.fillna(False).astype(bool).astype(int)
    out = {"label": DIAG}
    out["crosstabs_question_rows_feature_cols"] = {g: {"question": [int(((d[F] == 1) & (d[g] == v)).sum()) for v in (0, 1)],
                                                       "other": [int(((d[F] == 0) & (d[g] == v)).sum()) for v in (0, 1)]}
                                                   for g in ["G1_name", "G2_assertive", "G4_llm_words", "G6a_meme", "G6b_tentative",
                                                             "do_really"]}
    out["plus_G6a_meme_control"] = core._fit(d, "y", F, core.controls(F, ["G6a_meme"]))
    out["plus_G1_name_control"] = core._fit(d, "y", F, core.controls(F, ["G1_name"]))
    out["meme_titles_excluded"] = fit_n(d[d.G6a_meme == 0])
    out["named_titles_excluded"] = fit_n(d[d.G1_name == 0])
    out["assertive_titles_excluded"] = {**fit_n(d[d.G2_assertive == 0]),
                                        "note": "reference group = titles that are neither questions nor assertive (G2)"}
    out["method_abstract_share"] = {"question": share(d.loc[d[F] == 1, "method"]), "other": share(d.loc[d[F] == 0, "method"]),
                                    "diff_adjusted_pp": lpm_pp(core._fit(d, "method", F, core.controls(F)))}
    out["plus_method_indicator"] = core._fit(d, "y", F, core.controls(F, ["method"]))
    out["method_indicator_coef"] = core._fit(d, "y", "method", core.controls(F, [F]))
    out["method_regex"] = METHOD_RX.pattern
    return out


def _pairs(d: pd.DataFrame, caliper=0.80):
    """Re-implementation of core.matched_pairs' pairing (same embedding, same-year nearest control, cosine >= caliper,
    with replacement) that also returns the pair indices. Validated against core.matched_pairs in diag_r1."""
    d = d.reset_index(drop=True)
    tr, co = d[F] == 1, d[F] == 0
    Em, found = core.C.load_masked_embedding(d)
    Ea = core.C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    T, K, S_ = [], [], []
    for y in sorted(d.year.unique()):
        ti = np.where(tr & (d.year == y))[0]
        ci = np.where(co & (d.year == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        s = S[np.arange(len(ti)), j]
        ok = s >= caliper
        T += list(ti[ok]); K += list(ci[j[ok]]); S_ += list(s[ok])
    return d, np.array(T, int), np.array(K, int), np.array(S_)


def diag_r1(df: pd.DataFrame, rob: dict) -> dict:
    """(e) R1 (content-matched pairs) has the opposite sign to the primary. What are the matched controls?"""
    out = {"label": DIAG}
    d, T, K, S = _pairs(df)
    dy = d.y.to_numpy()[T] - d.y.to_numpy()[K]
    out["reimplementation_check"] = {"n_pairs": int(len(T)), "pct": float(np.exp(dy.mean()) - 1),
                                     "matches_core": bool(len(T) == rob["R1_matched_pairs"]["n_pairs"]
                                                          and abs(np.exp(dy.mean()) - 1 - rob["R1_matched_pairs"]["pct"]) < 1e-9)}
    col = lambda c: d[c].to_numpy()
    out["pair_balance"] = {
        "mean_cosine": float(S.mean()), "n_distinct_controls": int(len(set(K))),
        "share_same_topic50": float((col("topic50")[T] == col("topic50")[K]).mean()),
        "mean_diff_log_authors": float((col("log_authors")[T] - col("log_authors")[K]).mean()),
        "mean_diff_log_abs_words": float((col("log_abs_words")[T] - col("log_abs_words")[K]).mean()),
        "controls_named_share": float(col("G1_name")[K].mean()), "controls_assertive_share": float(col("G2_assertive")[K].mean()),
        "treated_named_share": float(col("G1_name")[T].mean()),
        "base_rate_named_nonquestion": float(df.loc[df[F] == 0, "G1_name"].mean()),
        "base_rate_assertive_nonquestion": float(df.loc[df[F] == 0, "G2_assertive"].mean()),
        "controls_llm_topic_share": float(d.llm_topic.fillna(False).astype(bool).to_numpy()[K].mean()),
        "treated_llm_topic_share": float(d.llm_topic.fillna(False).astype(bool).to_numpy()[T].mean())}
    # pair-level regression adjustment for the non-embedding primary controls (+ the other two big title features)
    rng = np.random.default_rng(0)
    for nm, cols in [("adj_team_abstract", ["log_authors", "log_abs_words"]),
                     ("adj_team_abstract_named_assertive", ["log_authors", "log_abs_words", "G1_name", "G2_assertive"])]:
        X = np.column_stack([np.ones(len(T))] + [col(c)[T].astype(float) - col(c)[K].astype(float) for c in cols])
        beta = np.linalg.lstsq(X, dy, rcond=None)[0]
        bs = []
        for _ in range(2000):
            i = rng.integers(0, len(dy), len(dy))
            bs.append(np.linalg.lstsq(X[i], dy[i], rcond=None)[0][0])
        lo, hi = np.percentile(bs, [2.5, 97.5])
        out[f"R1_regression_{nm}"] = {"pct": float(np.exp(beta[0]) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1),
                                      "n_pairs": int(len(T)), "adjusted_for_pair_differences_in": cols}
    out["R1_caliper_0.85"] = core.matched_pairs(df, F, caliper=0.85)
    out["R1_era_2017_21"] = core.matched_pairs(df[df.year <= 2021], F)
    out["R1_era_2022_25"] = core.matched_pairs(df[df.year >= 2022], F)
    out["R1_arxiv_id_only"] = core.matched_pairs(df[df.arxiv.notna()], F)
    plain = df[(df[F] == 1) | ((df.G1_name == 0) & (df.G2_assertive == 0))]
    out["R1_controls_plain_titles_only"] = {**core.matched_pairs(plain, F),
                                            "note": "control pool restricted to non-question titles that are neither named (G1) "
                                                    "nor assertive (G2); matched-pairs counterpart of the joint model"}
    return out


# --------------------------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------------------------
def figure(res: dict, path):
    prim, rob = res["primary"]["frozen"], res["robustness"]
    rows = [("Primary", prim, True)] + [(ROB_LABEL[k], rob[k], False) for k in ROB_LABEL]
    BLUE, INK, INK2, MUTED, GRID, BAND = "#2a78d6", "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1", "#f1f0ec"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, ax = plt.subplots(figsize=(8.6, 4.6), facecolor="white")
    ax.set_facecolor("white")
    lo_all = min(r[1]["lo"] for r in rows) * 100
    hi_all = max(r[1]["hi"] for r in rows) * 100
    ax.axvspan(-10, 10, color=BAND, zorder=0, lw=0)
    for i, (name, e, is_p) in enumerate(rows):
        col = BLUE if is_p else INK2
        ax.plot([e["lo"] * 100, e["hi"] * 100], [i, i], color=col, lw=2.4 if is_p else 2, solid_capstyle="round", zorder=2)
        ax.scatter([e["pct"] * 100], [i], s=60 if is_p else 34, color=col, edgecolor="white", linewidth=1.2, zorder=3)
        lab = f"{e['pct'] * 100:+.0f}%  [{e['lo'] * 100:+.0f}, {e['hi'] * 100:+.0f}]".replace("-", "\u2212")
        if "n_pairs" in e:
            lab += f"   {e['n_pairs']} pairs"
        ax.text(1.01, i, lab, transform=ax.get_yaxis_transform(), va="center", ha="left", fontsize=9,
                color=INK if is_p else INK2, fontweight="bold" if is_p else "normal")
    ax.axvline(0, color=INK2, lw=0.9, zorder=1)
    ax.text(-10, -0.75, "±10%: pre-registered 'no meaningful difference' band", ha="left", va="bottom", fontsize=8, color=MUTED,
            transform=ax.transData)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows])
    for t, r in zip(ax.get_yticklabels(), rows):
        t.set_color(INK if r[2] else INK2)
        if r[2]:
            t.set_fontweight("bold")
    ax.set_ylim(len(rows) - 0.4, -1.0)
    step = 20 if (hi_all - min(lo_all, -10)) <= 100 else 40
    xmin = np.floor(min(lo_all, -10) / 20) * 20
    xmax = np.ceil(hi_all / 20) * 20
    ax.set_xlim(xmin - 2, xmax + 2)
    ticks = np.arange(np.ceil(xmin / step) * step, xmax + 1, step)
    ax.set_xticks(ticks)
    ax.set_xticklabels([("0" if v == 0 else f"{v:+.0f}%".replace("-", "\u2212")) for v in ticks])
    ax.set_xlabel("Difference in citations, question vs other titles (95% CI)", color=INK2)
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
    for s_ in ["top", "right", "left"]:
        ax.spines[s_].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors=INK2)
    ax.set_title(f"Question titles ({res['n_with']} of {res['n_papers']:,}), accepted ICLR papers 2017-25", color=INK,
                 fontsize=11, pad=12)
    fig.tight_layout()
    fig.savefig(path, dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


# --------------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = core.load()

    pb = primary_block(df)
    pj = pb["frozen"]
    print("primary (json):", fmt(pj), "p", f"{pj['p']:.4f}", "Holm", f"{pj['p_holm']:.4f}", "| reproduced:", pb["reproduction_ok"],
          "max diff", pb["max_abs_diff"])

    rob = core.robustness(df, F)
    ver = core.verdict(pj, rob, pj["p_holm"])
    for k, r in rob.items():
        extra = f"pairs={r['n_pairs']}" if "n_pairs" in r else f"p={r['p']:.4f} n={r['n']}"
        print(f"  {k:28s} {fmt(r)}  {extra}")
    print("verdict:", ver)

    sec = {"joint_model_all8": secondary_joint(df), "heterogeneity_llm_topic": secondary_llm(df)}
    print("joint:", fmt(sec["joint_model_all8"]))
    h = sec["heterogeneity_llm_topic"]
    print("llm:", fmt(h["llm_topic_papers"]), h["llm_topic_papers"]["n_with"], "| non:", fmt(h["non_llm_topic_papers"]),
          h["non_llm_topic_papers"]["n_with"], "| ratio", h["difference_llm_minus_non"])

    diag = {"label": DIAG,
            "a_artefact_arxiv": diag_arxiv(df),
            "b_titles_validity": diag_titles(df),
            "c_power_fragility": diag_power(df, pj, rob),
            "d_overlap_paper_type": diag_overlap(df),
            "e_r1_vs_primary": diag_r1(df, rob)}
    e = diag["e_r1_vs_primary"]
    assert e["reimplementation_check"]["matches_core"], e["reimplementation_check"]
    print("R1 diag:", e["pair_balance"])
    for k in ["R1_regression_adj_team_abstract", "R1_regression_adj_team_abstract_named_assertive", "R1_caliper_0.85",
              "R1_era_2017_21", "R1_era_2022_25", "R1_arxiv_id_only", "R1_controls_plain_titles_only"]:
        print(f"  {k}: {fmt(e[k])} pairs={e[k].get('n_pairs')}")
    a = diag["a_artefact_arxiv"]
    print("arxiv share q/o:", a["arxiv_share"]["question"]["share"], a["arxiv_share"]["other"]["share"],
          "adj pp", a["arxiv_share_diff_adjusted_pp"])
    print("  arxiv only:", fmt(a["primary_spec_arxiv_only"]), a["primary_spec_arxiv_only"]["n_with"],
          "| no arxiv:", fmt(a["primary_spec_no_arxiv_only"]), a["primary_spec_no_arxiv_only"]["n_with"],
          "| +ctrl:", fmt(a["primary_spec_plus_arxiv_control"]), "| diff", a["difference_no_arxiv_minus_arxiv"])
    c = diag["c_power_fragility"]
    print("MDE:", {k: round(v["mde_pct_up"], 3) for k, v in c["mde_80pct_power"].items()}, "power:", c["power_for_true_effects"])
    print("equiv:", c["equivalence_band"])
    print("drop top:", {k: fmt(v) for k, v in c["drop_k_most_cited_question_titles"].items()})
    print("trim sym:", {k: fmt(v) for k, v in c["trim_k_most_and_k_least_cited_question_titles"].items()})
    o = diag["d_overlap_paper_type"]
    for k in ["plus_G6a_meme_control", "plus_G1_name_control", "meme_titles_excluded", "named_titles_excluded",
              "assertive_titles_excluded", "plus_method_indicator", "method_indicator_coef"]:
        print(f"  {k}: {fmt(o[k])}")

    res = {"feature": F, "label": core.FEATURES[F],
           "question": "G3: among accepted ICLR papers 2017-2025, do papers whose title is (or contains) a direct question "
                       "receive more or fewer Semantic Scholar citations than accepted papers with similar content?",
           "n_papers": int(len(df)), "n_with": int(df[F].sum()),
           "primary": pb, "robustness": rob, "verdict": ver,
           "verdict_rule": "more/fewer citations: Holm p < 0.05 and same sign in R1 and R2; no meaningful difference: 95% CI "
                           "within +/-10%; else inconclusive",
           "secondary": sec, "diagnostics": diag}
    json.dump(_clean(res), open(OUT / "results.json", "w"), indent=1, ensure_ascii=False)
    figure(res, OUT / "fig.png")
    print("wrote", OUT / "results.json", OUT / "fig.png")


if __name__ == "__main__":
    main()
