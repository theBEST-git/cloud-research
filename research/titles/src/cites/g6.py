"""G6: catchy title templates and citations among accepted ICLR papers 2017-2025.

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here).
Features (core.load):
  G6a_meme      = any of core.MEME (All You Need, Is Secretly, Free Lunch, Less Is More, Lost In, Devil In, A Tale Of,
                  To Rule Them All, Worth A Thousand / N Words, Matters, Do X Really, When X Meets Y); n = 83.
  G6b_tentative = any of core.TENTATIVE (Towards, Rethinking, Revisiting, Understanding, On the, Demystifying); n = 500.
Template regexes: src/features.py TEMPLATES (run on the lowercased title).

What this module does
  1. Primary (pre-registered): reads the frozen estimates and Holm p for G6a and G6b from outputs/cites/primary.json and
     re-computes them with core.primary as a reproduction check (the frozen numbers are the ones reported).
  2. Robustness R1-R7 (pre-registered): core.robustness for each feature.
  3. Verdict (pre-registered rule): core.verdict(frozen primary, robustness, frozen Holm p).
  4. Secondary (pre-registered, prereg section 6; no multiplicity claim):
       - G6: each template with n >= 20 separately (tpl_* columns), (i) template dummy in the primary spec, reference =
         all other titles; (ii) plus a dummy for 'another template of the same family', reference = titles with no
         template of that family. Templates with n < 20 get descriptive counts only;
       - (all questions) joint model with all 8 primary features;
       - (all questions) heterogeneity by LLM-topic papers.
  5. Diagnostics (NOT pre-registered; every block is labelled so in results.json):
       (a) superstar papers: every meme-template paper with its citations, within-year percentile and leave-one-out
           estimate; G6a re-run dropping the 3 (and 1/5/10) most-cited meme papers, by raw count and by within-year
           percentile; symmetric trims; a placebo for the mechanical downward shift of 'drop the top 3'; a within-year
           citation-percentile outcome; the same drop-top-k checks for G6b;
       (b) S2 split-record artefact: arXiv-id share by G6a / G6b status (raw, by era, adjusted), zero-citation share,
           primary spec within records with / without an arXiv id and with an arXiv-id indicator, QC sample counts;
       (c) overlap with other title features: crosstabs; G6a with a G2 (assertive) control and within assertive /
           non-assertive titles (the ASSERT regex matches 'is', 'matters', 'need' in many meme titles); G6b with a G1
           (named) control and within non-named titles; paper type (method-paper regex from g1.py);
       (d) power: minimum detectable effects and whether the +/-10% 'no meaningful difference' band was attainable;
       (e) measure spot-check: most / least cited tentative titles and a seeded random sample; counts by template;
       (f) R1 calibration: placebo null of the R1 matched-pairs procedure (random papers without the feature, same
           per-year counts, matched with the R1 rule), as in g4.py, which found R1 shifted down under the null; the
           placebo-adjusted R1 and where treated papers and their matched controls sit relative to their own
           year x topic50 cell.
       (g) adversarial audit (cites/audit_g5g6.py, added 2026-10-17): alternative explanations (preprint timing, code
           links, paper type, tail, camera-ready retitling via WP4 v1 titles, combined) and richer / non-bge content
           controls.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g6
Writes outputs/cites/G6/{results.json, fig.png, fig.csv}.
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

FA, FB = "G6a_meme", "G6b_tentative"
FAMILY = {FA: list(core.MEME), FB: list(core.TENTATIVE)}
OUT = core.OUT / "G6"
DIAG = "diagnostic (not pre-registered)"
SEC = "pre-specified secondary (prereg section 6; no multiplicity claim)"
MIN_N = 20  # prereg section 6: each template with n >= 20
METHOD_RX = re.compile(r"\b(?:we propose|we introduce|we present|this paper proposes)\b", re.I)  # same regex as g1.py
TPL_LABEL = {
    "tpl_all_you_need": "X Is All You Need", "tpl_is_secretly": "X Is Secretly Y", "tpl_free_lunch": "Free Lunch",
    "tpl_less_is_more": "Less Is More", "tpl_lost_in": "Lost In", "tpl_devil_in": "The Devil Is In",
    "tpl_tale_of": "A Tale Of", "tpl_rule_them_all": "To Rule Them All", "tpl_worth_a_thousand": "Worth A Thousand / N Words",
    "tpl_matters": "X Matters", "tpl_do_really": "Do X Really ...?", "tpl_when_meets": "When X Meets Y / X Meets Y",
    "tpl_towards": "Towards", "tpl_rethinking": "Rethinking", "tpl_revisiting": "Revisiting",
    "tpl_understanding": "Understanding", "tpl_on_the": "On the", "tpl_demystifying": "Demystifying",
}
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


def fit_n(d: pd.DataFrame, F: str, extra=(), y="y") -> dict:
    r = core._fit(d, y, F, core.controls(F, list(extra)))
    r["n_with"] = int(d[F].sum())
    return r


def ratio(r: dict) -> dict:
    return {"b": r["b"], "se": r["se"], "p": r["p"], "ratio": float(np.exp(r["b"])),
            "ratio_lo": float(np.exp(r["b"] - 1.96 * r["se"])), "ratio_hi": float(np.exp(r["b"] + 1.96 * r["se"]))}


def era(y):
    return "2017-21" if y <= 2021 else "2022-25"


def with_pctile(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(pctile=df.groupby("year").cites.rank(pct=True), has_arxiv=df.arxiv.notna().astype(int))


def template_of(row, fam) -> str:
    return ", ".join(TPL_LABEL[t] for t in fam if bool(row[t]))


# --------------------------------------------------------------------------------------------
# pre-registered parts
# --------------------------------------------------------------------------------------------
def primary_block(df: pd.DataFrame, F: str) -> dict:
    frozen = json.load(open(core.OUT / "primary.json"))
    prim = frozen["primary"][F]
    rep = core.primary(df, F)
    diff = {k: abs(prim[k] - rep[k]) for k in ["b", "se", "p", "pct", "lo", "hi"]}
    ok = diff["b"] < 1e-8 and diff["se"] < 1e-8 and prim["n"] == rep["n"] and prim["n_with"] == rep["n_with"]
    pv = {k: v["p"] for k, v in frozen["primary"].items()}
    rank = sorted(pv, key=pv.get).index(F)  # 0-based position in the Holm step-down
    return {"frozen": {**prim, "source": "outputs/cites/primary.json (Holm across the 8 primary tests)"}, "reproduced": rep,
            "max_abs_diff": max(diff.values()), "reproduction_ok": bool(ok),
            "holm_rank_1_based": rank + 1, "holm_step_alpha": 0.05 / (len(pv) - rank),
            "n_papers_frame": int(len(df)), "n_papers_frozen": int(frozen["n_papers"])}


def secondary_templates(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, G6): each template with n >= 20 separately."""
    d = with_pctile(df)
    out = {"label": SEC, "min_n": MIN_N,
           "note": "(i) 'vs_all_other_titles': y ~ template + primary controls | year^topic50 (the template dummy replaces "
                   "the family feature in the primary spec). (ii) 'vs_titles_without_family_template': adds a dummy for "
                   "'another template of the same family', so the reference group is titles with no template of that "
                   "family. SE clustered by topic50. Templates with n < 20 get descriptive counts only (not estimated)."}
    for F, fam in FAMILY.items():
        X = d[fam].fillna(False).astype(bool)
        res = {}
        for t in fam:
            n = int(X[t].sum())
            r = {"label": TPL_LABEL[t], "n_with": n, "estimated": n >= MIN_N,
                 "n_with_2022_25": int(X.loc[d.year >= 2022, t].sum()),
                 "raw_median_within_year_pctile": float(d.loc[X[t], "pctile"].median()) if n else None,
                 "raw_mean_log1p_cites": float(d.loc[X[t], "y"].mean()) if n else None}
            if n >= MIN_N:
                dd = d.assign(**{t: X[t].astype(int), "other_same_family": X.drop(columns=t).any(axis=1).astype(int)})
                r["vs_all_other_titles"] = core._fit(dd, "y", t, core.controls(F))
                r["vs_titles_without_family_template"] = core._fit(dd, "y", t, core.controls(F, ["other_same_family"]))
                r["n_other_same_family"] = int(dd.other_same_family.sum())
            res[t] = r
        res["n_titles_two_templates_in_family"] = int((X.sum(axis=1) >= 2).sum())
        res["reference_raw_median_within_year_pctile_no_family_template"] = float(d.loc[~X.any(axis=1), "pctile"].median())
        out[F] = res
    return out


def secondary_joint(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, all questions): G6a and G6b coefficients in one model with all 8 primary features."""
    out = {"label": SEC, "model": "y ~ all 8 primary features + primary controls | year^topic50, SE clustered by topic50"}
    for F in FAMILY:
        others = [f for f in core.FEATURES if f != F]
        out[F] = core._fit(df, "y", F, core.controls(F, others))
    return out


def secondary_llm(df: pd.DataFrame, F: str) -> dict:
    """Pre-specified (prereg s6, all questions): heterogeneity by LLM-topic papers."""
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(bool).astype(int)
    d["f_in_llm"] = d[F] * d.llm
    d["f_in_nonllm"] = d[F] * (1 - d.llm)
    llm = core._fit(d, "y", "f_in_llm", core.controls(F, ["f_in_nonllm", "llm"]))
    non = core._fit(d, "y", "f_in_nonllm", core.controls(F, ["f_in_llm", "llm"]))
    inter = core._fit(d, "y", "f_in_llm", core.controls(F, [F, "llm"]))  # interaction given the main effect
    llm["n_with"] = int(d.f_in_llm.sum())
    non["n_with"] = int(d.f_in_nonllm.sum())
    return {"label": SEC, "llm_topic_papers": llm, "non_llm_topic_papers": non,
            "difference_llm_minus_non": ratio(inter), "n_llm_topic_papers": int(d.llm.sum()),
            "share_llm_topic": {"with": float(d.loc[d[F] == 1, "llm"].mean()), "without": float(d.loc[d[F] == 0, "llm"].mean())},
            "note": "One model with the feature split by llm_topic plus an llm_topic main effect; 'difference' is the "
                    "feature x llm_topic interaction (ratio of the two citation multipliers)."}


# --------------------------------------------------------------------------------------------
# diagnostics (not pre-registered)
# --------------------------------------------------------------------------------------------
def _order_most_cited(G: pd.DataFrame, by: str) -> pd.Index:
    if by == "raw_count":
        return G.sort_values(["cites", "pctile"], ascending=[False, False]).index
    return G.sort_values(["pctile", "cites"], ascending=[False, False]).index


def _drop_checks(d: pd.DataFrame, F: str, ks=(1, 3, 5, 10)) -> dict:
    G = d[d[F] == 1]
    out = {}
    for by in ["raw_count", "within_year_pctile"]:
        idx = _order_most_cited(G, by)
        out[f"drop_k_most_cited_by_{by}"] = {str(k): {**fit_n(d.drop(index=idx[:k]), F),
                                                      "dropped": d.loc[idx[:k], "title"].tolist()} for k in ks}
        out[f"trim_k_most_and_k_least_cited_by_{by}"] = {str(k): fit_n(d.drop(index=list(idx[:k]) + list(idx[-k:])), F)
                                                         for k in ks}
    return out


def _placebo_drop_top(d: pd.DataFrame, F: str, k: int = 3, n_rep: int = 200, seed: int = 0) -> dict:
    """Mechanical effect of 'drop the k most-cited treated papers'. Among papers without the feature, draw pseudo-treated
    groups with the same per-year counts as the real group, estimate the primary spec, drop the pseudo group's k most-cited
    papers (raw count) and re-estimate. The mean change is the downward shift that dropping the top k produces with no
    association at all."""
    pool = d[d[F] == 0].copy()
    counts = d.loc[d[F] == 1, "year"].value_counts()
    rng = np.random.default_rng(seed)
    full, drop = [], []
    for _ in range(n_rep):
        pseudo = np.zeros(len(pool), int)
        for y, c in counts.items():
            idx = np.where(pool.year.to_numpy() == y)[0]
            pseudo[rng.choice(idx, int(c), replace=False)] = 1
        p = pool.assign(pseudo=pseudo)
        r_full = core._fit(p, "y", "pseudo", core.controls(F))
        top = p[p.pseudo == 1].sort_values(["cites", "pctile"], ascending=[False, False]).index[:k]
        r_drop = core._fit(p.drop(index=top), "y", "pseudo", core.controls(F))
        full.append(r_full["b"])
        drop.append(r_drop["b"])
    full, drop = np.array(full), np.array(drop)
    return {"n_rep": n_rep, "k": k, "mean_b_full": float(full.mean()), "sd_b_full": float(full.std(ddof=1)),
            "mean_shift_b": float((drop - full).mean()), "sd_shift_b": float((drop - full).std(ddof=1)),
            "q2.5_q97.5_shift_b": [float(q) for q in np.percentile(drop - full, [2.5, 97.5])],
            "_shift": (drop - full).tolist()}


def diag_superstars(df: pd.DataFrame, prim: dict) -> dict:
    """(a) Do 1-3 superstar papers drive G6a? (and the same drop-top-k checks for G6b)."""
    d = with_pctile(df)
    out = {"label": DIAG}
    # every meme-template paper, with its leave-one-out estimate
    G = d[d[FA] == 1].copy()
    G["template"] = G.apply(lambda r: template_of(r, FAMILY[FA]), axis=1)
    loo = {}
    for i in G.index:
        r = core._fit(d.drop(index=i), "y", FA, core.controls(FA))
        loo[i] = r
    G["loo_pct"] = [loo[i]["pct"] for i in G.index]
    G["loo_p"] = [loo[i]["p"] for i in G.index]
    G["loo_delta_pp"] = 100 * (G.loo_pct - prim[FA]["pct"])
    G = G.sort_values(["cites", "pctile"], ascending=[False, False])
    cols = ["year", "cites", "pctile", "has_arxiv", "template", "G1_name", "G2_assertive", "G3_question", "llm_topic",
            "loo_pct", "loo_p", "loo_delta_pp", "title"]
    rec = G[cols].copy()
    rec["llm_topic"] = rec.llm_topic.fillna(False).astype(bool)
    out["meme_papers_by_citations"] = rec.reset_index(drop=True).to_dict(orient="records")
    out["meme_citation_summary"] = {
        "n": int(len(G)), "total_cites": float(G.cites.sum()), "median_cites": float(G.cites.median()),
        "top1_share_of_total_cites": float(G.cites.iloc[0] / G.cites.sum()),
        "top3_share_of_total_cites": float(G.cites.iloc[:3].sum() / G.cites.sum()),
        "median_within_year_pctile": float(G.pctile.median()),
        "share_above_year_median": float((G.pctile > 0.5).mean()),
        "share_in_top_decile_of_year": float((G.pctile > 0.9).mean()),
        "non_meme_share_above_year_median": float((d.loc[d[FA] == 0, "pctile"] > 0.5).mean()),
        "non_meme_share_in_top_decile_of_year": float((d.loc[d[FA] == 0, "pctile"] > 0.9).mean()),
    }
    out["leave_one_out"] = {"min_pct": float(G.loo_pct.min()), "max_pct": float(G.loo_pct.max()),
                            "max_p": float(G.loo_p.max()),
                            "most_influential_title": G.loc[G.loo_pct.idxmin(), "title"],
                            "most_influential_loo_pct": float(G.loo_pct.min()),
                            "n_loo_with_p_below_0.05": int((G.loo_p < 0.05).sum())}
    out[FA] = _drop_checks(d, FA)
    out[FA]["requested_drop_top3_by_raw_count"] = out[FA]["drop_k_most_cited_by_raw_count"]["3"]
    pl = _placebo_drop_top(d, FA, k=3)
    shift = np.array(pl.pop("_shift"))
    real = out[FA]["requested_drop_top3_by_raw_count"]["b"] - prim[FA]["b"]
    adj_b = out[FA]["requested_drop_top3_by_raw_count"]["b"] - pl["mean_shift_b"]
    se3 = out[FA]["requested_drop_top3_by_raw_count"]["se"]
    pl.update({"real_shift_b": float(real), "real_shift_pctile_in_placebo": float((shift <= real).mean()),
               "drop_top3_placebo_centred": {"b": float(adj_b), "pct": float(np.exp(adj_b) - 1),
                                             "lo": float(np.exp(adj_b - 1.96 * se3) - 1),
                                             "hi": float(np.exp(adj_b + 1.96 * se3) - 1)},
               "note": "real_shift_pctile_in_placebo near 0 means the meme group's top 3 are unusually influential "
                       "relative to the top 3 of a random same-size, same-year-mix group. The placebo-centred estimate "
                       "adds back the mean mechanical shift; its CI reuses the drop-top-3 SE (approximate)."})
    out[FA]["placebo_drop_top3"] = pl
    out[FB] = _drop_checks(d, FB)
    # within-year citation percentile as outcome: each paper's influence is bounded
    d["y_rank"] = 100 * d.pctile
    for F in FAMILY:
        r = core._fit(d, "y_rank", F, core.controls(F))
        out[f"{F}_within_year_pctile_outcome"] = {"b_pctile_points": r["b"], "lo": r["b"] - 1.96 * r["se"],
                                                  "hi": r["b"] + 1.96 * r["se"], "p": r["p"], "n": r["n"],
                                                  "model": "100 x within-year citation percentile ~ feature + primary "
                                                           "controls | year^topic50"}
    T = d[d[FB] == 1].sort_values(["cites", "pctile"], ascending=[False, False])
    out["tentative_top10_by_citations"] = T[["year", "cites", "pctile", "title"]].head(10).to_dict(orient="records")
    out["tentative_citation_summary"] = {"n": int(len(T)), "top3_share_of_total_cites": float(T.cites.iloc[:3].sum() / T.cites.sum()),
                                         "median_within_year_pctile": float(T.pctile.median())}
    return out


def diag_arxiv(df: pd.DataFrame, F: str) -> dict:
    """(b) A venue record without an arXiv id may miss citations credited to a separate arXiv record
    (qc_split_records.jsonl). If that is more common in one group, the primary estimate is biased."""
    d = df.assign(has_arxiv=df.arxiv.notna().astype(int), multi_s2=(df.n_s2.fillna(1) > 1).astype(int), era=df.year.map(era))
    out = {"label": DIAG}
    out["arxiv_share"] = {"with": share(d.loc[d[F] == 1, "has_arxiv"]), "without": share(d.loc[d[F] == 0, "has_arxiv"])}
    out["arxiv_share_by_era"] = {e: {"with": share(g.loc[g[F] == 1, "has_arxiv"]), "without": share(g.loc[g[F] == 0, "has_arxiv"])}
                                 for e, g in d.groupby("era")}
    out["arxiv_share_diff_adjusted_pp"] = lpm_pp(core._fit(d, "has_arxiv", F, core.controls(F)))
    out["multi_record_share"] = {"with": share(d.loc[d[F] == 1, "multi_s2"]), "without": share(d.loc[d[F] == 0, "multi_s2"])}
    out["zero_citation_share"] = {"with": share(d.loc[d[F] == 1, "cites"] == 0), "without": share(d.loc[d[F] == 0, "cites"] == 0)}
    out["primary_spec_arxiv_only"] = fit_n(d[d.has_arxiv == 1], F)
    out["primary_spec_no_arxiv_only"] = fit_n(d[d.has_arxiv == 0], F)
    out["primary_spec_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, ["has_arxiv"]))
    dd = d.copy()
    dd["f_x_noarxiv"] = dd[F] * (1 - dd.has_arxiv)
    ctrl = core.controls(F)
    for c in ctrl:
        dd[f"{c}_na"] = dd[c] * (1 - dd.has_arxiv)
    inter = core._fit(dd, "y", "f_x_noarxiv", ctrl + [F] + [f"{c}_na" for c in ctrl], fe="year^topic50^has_arxiv")
    out["difference_no_arxiv_minus_arxiv"] = {**ratio(inter), "model": "feature x no-arXiv interaction; controls and "
                                                                        "year^topic50 FE interacted with has_arxiv (as in g1/g3)"}
    q = pd.read_json(core.OUT / "qc_split_records.jsonl", lines=True)
    q = q.merge(d[["submission_id", F]], left_on="sid", right_on="submission_id", how="left")
    q["split"] = q.match_pid.notna() & (q.match_pid != q.venue_pid)
    out["qc_split_sample"] = {"n_checked": int(len(q)), "n_split": int(q.split.sum()),
                              "n_checked_with": int((q[F] == 1).sum()), "n_split_with": int((q.split & (q[F] == 1)).sum()),
                              "note": "Random sample of matched records without an arXiv id (qc_split.py); sizes the "
                                      "artefact only, far too few template titles for a comparison."}
    return out


def diag_overlap(df: pd.DataFrame) -> dict:
    """(c) Overlap with other title features and paper type."""
    d = df.assign(method=df.abstract.fillna("").map(lambda a: int(bool(METHOD_RX.search(a)))))
    out = {"label": DIAG, "method_regex": METHOD_RX.pattern}
    feats = ["G1_name", "G2_assertive", "G3_question", "G4_llm_words", "G6a_meme", "G6b_tentative"]
    for F in FAMILY:
        o = {"overlap_counts_with": {g: int(((d[F] == 1) & (d[g] == 1)).sum()) for g in feats if g != F},
             "share_with": {g: float(d.loc[d[F] == 1, g].mean()) for g in feats if g != F},
             "share_without": {g: float(d.loc[d[F] == 0, g].mean()) for g in feats if g != F}}
        o["method_abstract_share"] = {"with": share(d.loc[d[F] == 1, "method"]), "without": share(d.loc[d[F] == 0, "method"]),
                                      "diff_adjusted_pp": lpm_pp(core._fit(d, "method", F, core.controls(F)))}
        o["plus_method_indicator"] = core._fit(d, "y", F, core.controls(F, ["method"]))
        out[F] = o
    a = out[FA]
    a["plus_G2_control"] = core._fit(d, "y", FA, core.controls(FA, ["G2_assertive"]))
    a["plus_G1_G2_G3_controls"] = core._fit(d, "y", FA, core.controls(FA, ["G1_name", "G2_assertive", "G3_question"]))
    a["within_non_assertive_titles"] = fit_n(d[d.G2_assertive == 0], FA)
    a["within_assertive_titles"] = fit_n(d[d.G2_assertive == 1], FA)
    a["G2_coef_with_G6a_control"] = core._fit(d, "y", "G2_assertive", core.controls("G2_assertive", [FA]))
    a["G2_within_non_meme_titles"] = fit_n(d[d[FA] == 0], "G2_assertive")
    a["note"] = ("The G2 ASSERT regex matches 'is', 'are', 'matters', 'need(s)' etc., so 'X Is All You Need', "
                 "'X Matters' and 'X Is Secretly Y' titles are mostly also G2.")
    b = out[FB]
    b["plus_G1_control"] = core._fit(d, "y", FB, core.controls(FB, ["G1_name"]))
    b["within_non_named_titles"] = fit_n(d[d.G1_name == 0], FB)
    b["within_named_titles"] = fit_n(d[d.G1_name == 1], FB)
    return out


def diag_power(pj: dict, holm_alpha: float) -> dict:
    """(d) Power for the observed SE and attainability of the pre-registered +/-10% band."""
    se = pj["se"]
    zb = norm.ppf(0.80)
    mde = {}
    for nm, a in [("alpha_0.05", 0.05), ("alpha_holm_step", holm_alpha), ("alpha_0.00625_bonferroni_8", 0.05 / 8)]:
        b = (norm.ppf(1 - a / 2) + zb) * se
        mde[nm] = {"alpha": a, "mde_b": float(b), "mde_pct_up": float(np.exp(b) - 1), "mde_pct_down": float(np.exp(-b) - 1)}
    pw = {}
    for eff in [0.10, 0.20, 0.38]:
        b = np.log1p(eff)
        pw[f"+{int(round(eff * 100))}%"] = {nm: float(norm.cdf(b / se - norm.ppf(1 - m["alpha"] / 2))
                                                      + norm.cdf(-b / se - norm.ppf(1 - m["alpha"] / 2)))
                                            for nm, m in mde.items()}
    lo_b, hi_b = np.log(0.9), np.log(1.1)
    return {"label": DIAG, "se_b": se, "n_with": pj["n_with"], "ci95_width_log": float(2 * 1.96 * se),
            "band_width_log": float(hi_b - lo_b), "band_attainable_at_current_se": bool(2 * 1.96 * se < hi_b - lo_b),
            "se_needed_for_ci_to_fit_band": float((hi_b - lo_b) / (2 * 1.96)),
            "mde_80pct_power": mde, "power_for_true_effects": pw}


def diag_measure(df: pd.DataFrame) -> dict:
    """(e) Measure spot-check for G6b (G6a titles are all listed in (a))."""
    d = with_pctile(df)
    T = d[d[FB] == 1].copy()
    T["template"] = T.apply(lambda r: template_of(r, FAMILY[FB]), axis=1)
    cols = ["year", "cites", "pctile", "template", "title"]
    lead = T.title.str.lower().str.match(r"^[^:]*:\s*(?:towards?|rethinking|revisiting|understanding|demystifying)\b")
    return {"label": DIAG,
            "tentative_after_name_prefix": int(lead.sum()),
            "tentative_by_year": {int(k): int(v) for k, v in T.groupby("year").size().items()},
            "meme_by_year": {int(k): int(v) for k, v in d[d[FA] == 1].groupby("year").size().items()},
            "tentative_top10_by_pctile": T.sort_values("pctile", ascending=False)[cols].head(10).to_dict(orient="records"),
            "tentative_bottom10_by_pctile": T.sort_values("pctile")[cols].head(10).to_dict(orient="records"),
            "tentative_random20_seed0": T.sample(20, random_state=0)[cols].to_dict(orient="records"),
            "regexes": "src/features.py TEMPLATES; tentative openers match at title start or right after a 'NAME:' "
                       "prefix, except 'On the' (title start only)."}


def diag_audit(df: pd.DataFrame) -> dict:
    """(g) Adversarial-audit diagnostics (cites/audit_g5g6.py)."""
    from cites import audit_g5g6 as AU
    v1 = AU.v1_frame(df)
    return {"label": AU.LABEL, "alt_explanations": {F: AU.alt_explanations(df, F, True, v1) for F in FAMILY},
            "content_controls": AU.content_controls(df, list(FAMILY))}


def _emb(d: pd.DataFrame) -> np.ndarray:
    """Same embedding as core.matched_pairs: name-masked abstract (unmasked where no masked text, e.g. 2017)."""
    from analyses import _core as C
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    return E / np.linalg.norm(E, axis=1, keepdims=True)


def _nn_pairs(E: np.ndarray, years: np.ndarray, tr: np.ndarray, co: np.ndarray, caliper: float = 0.80):
    """Nearest same-year control for each treated row, as in core.matched_pairs (with replacement, cosine >= caliper)."""
    T, Cc = [], []
    for y in np.unique(years):
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


def diag_r1_calibration(df: pd.DataFrame, rob: dict, n_rep: int = 200, seed: int = 0) -> dict:
    """(f) Placebo null of the R1 statistic (method of g4.py diagnostic (d)): draw pseudo-treated papers at random from
    papers without the feature with the same per-year counts, match them to the remaining papers without the feature with
    the R1 rule, record the mean within-pair log difference. Under no association this should centre on 0."""
    d = df.reset_index(drop=True)
    E = _emb(d)
    years, yv, yt = d.year.to_numpy(), d.y.to_numpy(), d.yt.to_numpy()
    out = {"label": DIAG}
    for F in FAMILY:
        tr, pool0 = (d[F] == 1).to_numpy(), (d[F] == 0).to_numpy()
        t, c = _nn_pairs(E, years, tr, pool0)
        obs = float((yv[t] - yv[c]).mean())
        counts = pd.Series(years[tr]).value_counts()
        rng = np.random.default_rng(seed)
        stats = []
        for _ in range(n_rep):
            ptr = np.zeros(len(d), bool)
            for y, k in counts.items():
                ptr[rng.choice(np.where(pool0 & (years == y))[0], int(k), replace=False)] = True
            tt, cc = _nn_pairs(E, years, ptr, pool0 & ~ptr)
            stats.append(float((yv[tt] - yv[cc]).mean()))
        stats = np.array(stats)
        adj = obs - stats.mean()
        se = float(stats.std(ddof=1) * np.sqrt(1 + 1 / n_rep))
        p_lo = (1 + (stats <= obs).sum()) / (n_rep + 1)
        p_hi = (1 + (stats >= obs).sum()) / (n_rep + 1)
        cm = d[d[F] == 0].groupby("yt").y.mean()
        out[F] = {"n_pairs": int(len(t)), "observed_pct": float(np.exp(obs) - 1),
                  "reimplementation_matches_core_R1": bool(len(t) == rob[F]["R1_matched_pairs"]["n_pairs"]
                                                           and abs(np.exp(obs) - 1 - rob[F]["R1_matched_pairs"]["pct"]) < 1e-9),
                  "placebo": {"n_rep": n_rep, "mean_log_diff": float(stats.mean()), "sd_log_diff": float(stats.std(ddof=1)),
                              "pct_at_mean": float(np.exp(stats.mean()) - 1),
                              "q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(stats, [2.5, 97.5])]},
                  "placebo_p_two_sided": float(min(1.0, 2 * min(p_lo, p_hi))),
                  "placebo_adjusted": {"pct": float(np.exp(adj) - 1), "lo": float(np.exp(adj - 1.96 * se) - 1),
                                       "hi": float(np.exp(adj + 1.96 * se) - 1)},
                  "treated_y_minus_own_cell_mean_without": float(np.nanmean(yv[t] - cm.reindex(yt[t]).to_numpy())),
                  "controls_y_minus_own_cell_mean_without": float(np.nanmean(yv[c] - cm.reindex(yt[c]).to_numpy())),
                  "share_pairs_same_topic50": float((d.topic50.to_numpy()[t] == d.topic50.to_numpy()[c]).mean()),
                  "n_unique_controls": int(len(np.unique(c))),
                  "note": "adjusted = exp(observed mean log diff - placebo mean) - 1; approximate CI uses the placebo SD "
                          "of the R1 statistic as the SE"}
    return out


# --------------------------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------------------------
def figure(res: dict, path_png, path_csv):
    BLUE, INK, INK2, MUTED, GRID, BAND = "#2a78d6", "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1", "#f1f0ec"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9.5})
    R1ADJ, DROP3 = "R1 placebo-adjusted (diagnostic)", "Drop 3 most-cited (diagnostic)"
    panels = []
    for F, title in [(FA, "Meme templates"), (FB, "Tentative framings")]:
        prim = res["primary"][F]["frozen"]
        rob = res["robustness"][F]
        D = res["diagnostics_not_preregistered"]
        drop3 = D["a_superstars"][F]["drop_k_most_cited_by_raw_count"]["3"]
        r1adj = D["f_r1_calibration"][F]["placebo_adjusted"]
        rows = [("Primary", prim, "main")]
        for k in ROB_LABEL:
            rows.append((ROB_LABEL[k], rob[k], "rob"))
            if k == "R1_matched_pairs":
                rows.append((R1ADJ, r1adj, "diag"))
        rows.append((DROP3, drop3, "diag"))
        panels.append((F, f"{title}  (n = {prim['n_with']})", rows))
    labels = [r[0] for r in panels[0][2]]
    allv = [v for _, _, rows in panels for _, e, _ in rows for v in (e["lo"], e["hi"])]
    xlo, xhi = np.log1p(min(allv + [-0.1])), np.log1p(max(allv + [0.1]))
    ticks_pct = [t for t in [-75, -50, -25, 0, 50, 100, 200, 400, 800] if np.log1p(t / 100) >= xlo - 0.05 and np.log1p(t / 100) <= xhi + 0.05]
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.6), facecolor="white", sharey=True)
    csv = []
    for ax, (F, title, rows) in zip(axes, panels):
        ax.set_facecolor("white")
        ax.axvspan(np.log1p(-0.10), np.log1p(0.10), color=BAND, zorder=0, lw=0)
        ax.axvline(0, color=INK2, lw=0.9, zorder=1)
        for i, (name, e, kind) in enumerate(rows):
            col = BLUE if kind == "main" else (MUTED if kind == "diag" else INK2)
            x, lo, hi = np.log1p(e["pct"]), np.log1p(e["lo"]), np.log1p(e["hi"])
            ax.plot([lo, hi], [i, i], color=col, lw=2.4 if kind == "main" else 1.8, solid_capstyle="round", zorder=2)
            if kind == "diag":
                ax.scatter([x], [i], s=34, facecolor="white", edgecolor=col, linewidth=1.4, zorder=3)
            else:
                ax.scatter([x], [i], s=60 if kind == "main" else 34, color=col, edgecolor="white", linewidth=1.2, zorder=3)
            pc = lambda v: "0" if int(round(100 * v)) == 0 else f"{int(round(100 * v)):+d}"
            lab = f"{pc(e['pct'])}%  [{pc(e['lo'])}, {pc(e['hi'])}]".replace("-", "−")
            ax.text(xhi + 0.12, i, lab, va="center", ha="left", fontsize=8.5, color=INK if kind == "main" else INK2,
                    fontweight="bold" if kind == "main" else "normal", clip_on=False)
            csv.append({"feature": F, "row": name, "pct": e["pct"], "lo": e["lo"], "hi": e["hi"],
                        "n_pairs": e.get("n_pairs"), "kind": kind})
        ax.set_xlim(xlo - 0.08, xhi + 0.08)
        ax.set_xticks([np.log1p(t / 100) for t in ticks_pct])
        ax.set_xticklabels([("0" if t == 0 else f"{t:+d}%".replace("-", "−")) for t in ticks_pct])
        ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
        for s_ in ["top", "right", "left"]:
            ax.spines[s_].set_visible(False)
        ax.spines["bottom"].set_color(MUTED)
        ax.tick_params(axis="y", length=0)
        ax.tick_params(axis="x", colors=INK2, labelsize=8.5)
        ax.set_title(title, loc="left", color=INK, fontsize=10.5, pad=8)
    axes[0].set_yticks(range(len(labels)))
    axes[0].set_yticklabels(labels)
    for t in axes[0].get_yticklabels():
        if t.get_text() == "Primary":
            t.set_fontweight("bold")
            t.set_color(INK)
        elif "diagnostic" in t.get_text():
            t.set_color(MUTED)
            t.set_fontstyle("italic")
        else:
            t.set_color(INK2)
    axes[0].set_ylim(len(labels) - 0.4, -0.8)
    fig.supxlabel("% difference in citations vs other accepted papers (95% CI, log scale; shaded band ±10%)",
                  color=INK2, fontsize=9, y=0.02)
    fig.tight_layout(w_pad=9.5)
    fig.savefig(path_png, dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    pd.DataFrame(csv).to_csv(path_csv, index=False)


# --------------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = core.load()
    res = {
        "question": "G6: among accepted ICLR papers 2017-2025, do papers whose titles use catchy templates - meme templates "
                    "(G6a: All You Need, Is Secretly, Matters, When X Meets Y, ...) or tentative framings (G6b: Towards, "
                    "Rethinking, Revisiting, Understanding, On the, Demystifying) - receive more or fewer Semantic Scholar "
                    "citations than accepted papers with similar content?",
        "features": {F: core.FEATURES[F] for F in FAMILY},
        "templates": {F: {t: TPL_LABEL[t] for t in fam} for F, fam in FAMILY.items()},
        "outcome": "y = log(1 + Semantic Scholar citationCount, retrieved 2026-10-17); % difference = exp(b) - 1",
        "n_papers": int(len(df)),
        "primary": {}, "robustness": {}, "verdict": {}, "verdict_inputs": {},
    }
    for F in FAMILY:
        P = primary_block(df, F)
        prim, p_holm = P["frozen"], P["frozen"]["p_holm"]
        rob = core.robustness(df, F)
        res["primary"][F], res["robustness"][F] = P, rob
        res["verdict"][F] = core.verdict(prim, rob, p_holm)
        res["verdict_inputs"][F] = {"p_holm": p_holm, "holm_below_0.05": bool(p_holm < 0.05),
                                    "R1_sign_same": bool((rob["R1_matched_pairs"]["pct"] > 0) == (prim["pct"] > 0)),
                                    "R2_sign_same": bool((rob["R2_ppml_counts"]["pct"] > 0) == (prim["pct"] > 0)),
                                    "ci_within_10pct": bool(prim["lo"] > -0.10 and prim["hi"] < 0.10)}
    prim_frozen = {F: res["primary"][F]["frozen"] for F in FAMILY}
    res["secondary_prespecified"] = {
        "label": SEC,
        "each_template_n_ge_20": secondary_templates(df),
        "joint_model_8_features": secondary_joint(df),
        "llm_topic_heterogeneity": {F: secondary_llm(df, F) for F in FAMILY},
    }
    res["diagnostics_not_preregistered"] = {
        "label": DIAG,
        "a_superstars": diag_superstars(df, prim_frozen),
        "b_arxiv_share_split_records": {F: diag_arxiv(df, F) for F in FAMILY},
        "c_overlap_and_paper_type": diag_overlap(df),
        "d_power": {F: diag_power(prim_frozen[F], res["primary"][F]["holm_step_alpha"]) for F in FAMILY},
        "e_measure_spot_check": diag_measure(df),
        "f_r1_calibration": diag_r1_calibration(df, res["robustness"]),
        "g_audit": diag_audit(df),
    }
    figure(res, OUT / "fig.png", OUT / "fig.csv")
    res["figure"] = {"png": str(OUT / "fig.png"), "csv": str(OUT / "fig.csv")}
    json.dump(_clean(res), open(OUT / "results.json", "w"), indent=1)

    # console summary
    for F in FAMILY:
        P = res["primary"][F]
        prim = P["frozen"]
        print(f"== {F}: reproduction ok {P['reproduction_ok']} (max|diff| {P['max_abs_diff']:.1e}); holm rank "
              f"{P['holm_rank_1_based']} step alpha {P['holm_step_alpha']:.4f}")
        print(f"primary {fmt(prim)}  p {prim['p']:.3g}  holm p {prim['p_holm']:.3g}  n {prim['n']}  n_with {prim['n_with']}")
        for k in ROB_LABEL:
            r = res["robustness"][F][k]
            extra = f"n_pairs {r['n_pairs']}" if "n_pairs" in r else f"p {r['p']:.3g} n {r['n']}"
            print(f"  {k:26s} {fmt(r)}  {extra}")
        print("verdict:", res["verdict"][F], res["verdict_inputs"][F])
    S = res["secondary_prespecified"]
    for F in FAMILY:
        for t in FAMILY[F]:
            r = S["each_template_n_ge_20"][F][t]
            line = f"  {t:22s} n {r['n_with']:4d} med pct {r['raw_median_within_year_pctile']}"
            if r["estimated"]:
                line += (f"  vs all {fmt(r['vs_all_other_titles'])} p {r['vs_all_other_titles']['p']:.3g}"
                         f"  vs none {fmt(r['vs_titles_without_family_template'])} p {r['vs_titles_without_family_template']['p']:.3g}")
            print(line)
        J = S["joint_model_8_features"][F]
        L = S["llm_topic_heterogeneity"][F]
        print(f"  joint {fmt(J)} p {J['p']:.3g} | llm {fmt(L['llm_topic_papers'])} n {L['llm_topic_papers']['n_with']} | non "
              f"{fmt(L['non_llm_topic_papers'])} n {L['non_llm_topic_papers']['n_with']} | ratio "
              f"{L['difference_llm_minus_non']['ratio']:.2f} [{L['difference_llm_minus_non']['ratio_lo']:.2f}, "
              f"{L['difference_llm_minus_non']['ratio_hi']:.2f}] p {L['difference_llm_minus_non']['p']:.3g}")
    D = res["diagnostics_not_preregistered"]
    A = D["a_superstars"]
    print("meme summary", A["meme_citation_summary"])
    print("loo", A["leave_one_out"])
    for F in FAMILY:
        for key in ["drop_k_most_cited_by_raw_count", "drop_k_most_cited_by_within_year_pctile",
                    "trim_k_most_and_k_least_cited_by_raw_count"]:
            print(" ", F, key, {k: f"{fmt(v)} p {v['p']:.3g}" for k, v in A[F][key].items()})
        r = A[f"{F}_within_year_pctile_outcome"]
        print(f"  {F} pctile outcome {r['b_pctile_points']:+.2f} [{r['lo']:+.2f}, {r['hi']:+.2f}] p {r['p']:.3g}")
    pl = A[FA]["placebo_drop_top3"]
    print("placebo drop3", {k: v for k, v in pl.items() if k != "note"})
    for F in FAMILY:
        B = D["b_arxiv_share_split_records"][F]
        print(F, "arxiv", round(B["arxiv_share"]["with"]["share"], 4), B["arxiv_share"]["with"]["ci95_wilson"],
              round(B["arxiv_share"]["without"]["share"], 4), "adj pp", {k: round(v, 3) for k, v in B["arxiv_share_diff_adjusted_pp"].items() if isinstance(v, float)})
        print("   by era", {e: (round(v["with"]["share"], 3), v["with"]["k"], v["with"]["n"], round(v["without"]["share"], 3))
                            for e, v in B["arxiv_share_by_era"].items()})
        print("   zero", B["zero_citation_share"]["with"]["share"], B["zero_citation_share"]["without"]["share"],
              "multi", B["multi_record_share"]["with"]["share"], B["multi_record_share"]["without"]["share"])
        print("   arxiv only", fmt(B["primary_spec_arxiv_only"]), B["primary_spec_arxiv_only"]["n_with"],
              "| no arxiv", fmt(B["primary_spec_no_arxiv_only"]), B["primary_spec_no_arxiv_only"]["n_with"],
              "| +ctrl", fmt(B["primary_spec_plus_arxiv_control"]),
              "| ratio", round(B["difference_no_arxiv_minus_arxiv"]["ratio"], 3), round(B["difference_no_arxiv_minus_arxiv"]["ratio_lo"], 3),
              round(B["difference_no_arxiv_minus_arxiv"]["ratio_hi"], 3), "p", round(B["difference_no_arxiv_minus_arxiv"]["p"], 3),
              "| qc", B["qc_split_sample"])
    O = D["c_overlap_and_paper_type"]
    for F in FAMILY:
        o = O[F]
        print(F, "overlap", o["overlap_counts_with"], "method share", round(o["method_abstract_share"]["with"]["share"], 3),
              round(o["method_abstract_share"]["without"]["share"], 3), "adj", {k: round(v, 2) for k, v in o["method_abstract_share"]["diff_adjusted_pp"].items() if isinstance(v, float)},
              "+method", fmt(o["plus_method_indicator"]))
    a = O[FA]
    for k in ["plus_G2_control", "plus_G1_G2_G3_controls", "within_non_assertive_titles", "within_assertive_titles",
              "G2_coef_with_G6a_control", "G2_within_non_meme_titles"]:
        print(f"  {k}: {fmt(a[k])} p {a[k]['p']:.3g} n {a[k]['n']} n_with {a[k].get('n_with')}")
    b = O[FB]
    for k in ["plus_G1_control", "within_non_named_titles", "within_named_titles"]:
        print(f"  {k}: {fmt(b[k])} p {b[k]['p']:.3g} n {b[k]['n']} n_with {b[k].get('n_with')}")
    for F in FAMILY:
        Pw = D["d_power"][F]
        print(F, "power", {k: round(v, 4) if isinstance(v, float) else v for k, v in Pw.items() if k not in ("mde_80pct_power", "power_for_true_effects")},
              {k: (round(v["mde_pct_up"], 3), round(v["mde_pct_down"], 3)) for k, v in Pw["mde_80pct_power"].items()},
              Pw["power_for_true_effects"])
    E = D["e_measure_spot_check"]
    print("after name prefix", E["tentative_after_name_prefix"])
    for F in FAMILY:
        R = D["f_r1_calibration"][F]
        print(F, "R1 calib", {k: v for k, v in R.items() if k != "note"})
    from cites import audit_g5g6 as AU
    G = D["g_audit"]
    for F in FAMILY:
        print("(g)", F)
        for line in AU.summary_lines(G["alt_explanations"][F]):
            print("     ", line)
        print("      content:", {k: fmt(v) for k, v in G["content_controls"][F].items()})


if __name__ == "__main__":
    main()
