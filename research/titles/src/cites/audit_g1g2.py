"""Alternative-explanation diagnostics for G1 and G2, added by the adversarial audit (2026-10-17).

Everything here is DIAGNOSTIC (NOT PRE-REGISTERED). Nothing changes the pre-registered primary estimate, sample,
outcome, controls, fixed effects or verdict. Unless stated otherwise each re-fit uses core._fit with the primary
controls (core.controls), year^topic50 FE and SEs clustered by topic50.

Alternative explanations tested:
  timing     Preprint exposure time. The arXiv id gives the month of first arXiv posting. lead_months = months between
             that month and May of the ICLR year. Earlier preprints have had longer to collect citations. Records with
             an arXiv id only; lead_months enters as FE bins.
  code       Promotion / reuse. The abstract announces code or a URL (github, http(s)://, 'code ... available /
             released / public', open-source).
  paper_type Method vs findings paper. The abstract announces a method ('we propose / introduce / present', 'this paper
             proposes') or a finding ('we show / find / demonstrate / study / investigate / analyse / observe / reveal /
             identify / prove / argue', 'empirical study / analysis / investigation'). Both regexes are crude and
             unvalidated.
  tail       Superstar outliers and zero-citation records. Outcome = within-year citation percentile (0-100, effect in
             percentile points); drop the top 5% most-cited per year (R4 drops the top 1%); drop zero-citation records
             (mostly split S2 records); share of the feature among the top 5% / 1% per year.
  retitling  Reverse causation through retitling (early attention -> authors add a name / a claim at camera-ready).
             The WP4 camera-ready audit (outputs/snapshot/audit_pairs.csv, read only) gives the arXiv v1 title, posted
             before the decision, for accepted 2023-25 papers. Compare feature status on the v1 and camera-ready titles
             and re-estimate with the v1 status as the exposure on the same papers.
  combined   Records with an arXiv id; lead-month FE bins added to year^topic50; code + method + findings indicators.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

from cites import core

LABEL = "diagnostic (not pre-registered; added by the adversarial audit)"
LEAD_BINS = [-1000, -1, 3, 6, 9, 12, 18, 1000]  # months before May of the conference year
CODE_RX = re.compile(r"github\.com|https?://|\bcode\b[^.]{0,40}\b(?:available|released|public)|open[- ]source", re.I)
METHOD_RX = re.compile(r"\b(?:we propose|we introduce|we present|this paper proposes)\b", re.I)
FINDING_RX = re.compile(r"\bwe (?:show|find|demonstrate|study|investigate|analy[sz]e|observe|reveal|identify|prove|argue)\b"
                        r"|\bempirical (?:study|analysis|investigation)\b", re.I)
AUDIT_PAIRS = core.OUT.parent / "snapshot" / "audit_pairs.csv"


def add_columns(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    m = d.arxiv.astype("string").str.extract(r"^(\d{2})(\d{2})\.")
    yy, mm = pd.to_numeric(m[0], errors="coerce"), pd.to_numeric(m[1], errors="coerce")
    d["arxiv_month_idx"] = (2000 + yy) * 12 + mm - 1
    d["lead_months"] = d.year * 12 + 4 - d.arxiv_month_idx
    d["lead_bin"] = pd.cut(d.lead_months, LEAD_BINS, labels=False)
    ab = d.abstract.fillna("")
    d["code_link"] = [int(CODE_RX.search(a) is not None) for a in ab]
    d["method_abs"] = [int(METHOD_RX.search(a) is not None) for a in ab]
    d["finding_abs"] = [int(FINDING_RX.search(a) is not None) for a in ab]
    d["cite_pctile"] = 100 * d.groupby("year").cites.rank(pct=True)
    return d


def _nw(r: dict, d: pd.DataFrame, F: str) -> dict:
    r = dict(r)
    r["n_with"] = int(d[F].sum())
    return r


def _by(d: pd.DataFrame, F: str, col: str) -> dict:
    return {"with_feature": float(d.loc[d[F] == 1, col].mean()), "without_feature": float(d.loc[d[F] == 0, col].mean())}


def _v1_status(F: str, A: pd.DataFrame) -> pd.Series:
    if F == "G1_name":
        return A.NAME_v1.astype(int)
    if F == "G2_assertive":
        t = A.v1_title.fillna("")
        return (t.map(lambda s: core.ASSERT.search(s) is not None) & ~t.str.contains("?", regex=False)).astype(int)
    raise ValueError(F)


def _cr_status_check(F: str, a: pd.DataFrame) -> float:
    """Share of audited papers where re-applying the v1 rule to the camera-ready title reproduces the frozen feature."""
    if F == "G1_name":
        return float((a.NAME_or.astype(int) == a[F]).mean())
    t = a.or_title.fillna("")
    re_cr = (t.map(lambda s: core.ASSERT.search(s) is not None) & ~t.str.contains("?", regex=False)).astype(int)
    return float((re_cr == a[F]).mean())


def alt_explanations(df: pd.DataFrame, F: str) -> dict:
    d = add_columns(df)
    C = core.controls(F)
    out = {"label": LABEL, "feature": F, "doc": __doc__.split("Alternative explanations tested:")[1].strip()}

    # timing
    a = d[d.arxiv_month_idx.notna()]
    out["timing"] = {
        "label": LABEL,
        "mean_lead_months": _by(a, F, "lead_months"),
        "share_posted_7plus_months_before_conference": {k: float(v) for k, v in
                                                       a.assign(e=(a.lead_months >= 7).astype(int)).pipe(lambda x: _by(x, F, "e")).items()},
        "lead_months_diff_primary_controls": core._fit(a, "lead_months", F, C),
        "arxiv_only_primary_spec": _nw(core._fit(a, "y", F, C), a, F),
        "arxiv_only_plus_lead_bin_fe": _nw(core._fit(a, "y", F, C, fe="year^topic50 + lead_bin"), a, F),
        "lead_bins_months": LEAD_BINS,
    }
    # code / URL in abstract
    out["code"] = {
        "label": LABEL, "regex": CODE_RX.pattern, "share": _by(d, F, "code_link"),
        "plus_code_control": core._fit(d, "y", F, C + ["code_link"]),
        "code_indicator_coef": core._fit(d, "y", "code_link", C + [F]),
        "within_code_abstracts": _nw(core._fit(d[d.code_link == 1], "y", F, C), d[d.code_link == 1], F),
        "within_other_abstracts": _nw(core._fit(d[d.code_link == 0], "y", F, C), d[d.code_link == 0], F),
    }
    # paper type
    out["paper_type"] = {
        "label": LABEL, "method_regex": METHOD_RX.pattern, "finding_regex": FINDING_RX.pattern,
        "share_method": _by(d, F, "method_abs"), "share_finding": _by(d, F, "finding_abs"),
        "plus_method_and_finding_controls": core._fit(d, "y", F, C + ["method_abs", "finding_abs"]),
        "within_method_abstracts": _nw(core._fit(d[d.method_abs == 1], "y", F, C), d[d.method_abs == 1], F),
        "within_non_method_abstracts": _nw(core._fit(d[d.method_abs == 0], "y", F, C), d[d.method_abs == 0], F),
        "within_finding_abstracts": _nw(core._fit(d[d.finding_abs == 1], "y", F, C), d[d.finding_abs == 1], F),
        "within_non_finding_abstracts": _nw(core._fit(d[d.finding_abs == 0], "y", F, C), d[d.finding_abs == 0], F),
    }
    # heavy tail
    tail = {"label": LABEL}
    r = core._fit(d, "cite_pctile", F, C)
    tail["cite_percentile_outcome_pp"] = {"b_pp": r["b"], "lo_pp": r["b"] - 1.96 * r["se"], "hi_pp": r["b"] + 1.96 * r["se"],
                                          "p": r["p"], "n": r["n"]}
    cap5 = d.groupby("year").cites.transform(lambda s: s.quantile(0.95))
    tail["drop_top5pct_per_year"] = _nw(core._fit(d[d.cites <= cap5], "y", F, C), d[d.cites <= cap5], F)
    tail["drop_zero_citation_records"] = _nw(core._fit(d[d.cites > 0], "y", F, C), d[d.cites > 0], F)
    for q in (0.95, 0.99):
        cap = d.groupby("year").cites.transform(lambda s, q=q: s.quantile(q))
        top = d.cites > cap
        tail[f"share_feature_in_top{round(100 * (1 - q))}pct_per_year"] = {
            "share": float(d.loc[top, F].mean()), "n_feature_in_top": int(d.loc[top, F].sum()), "n_top": int(top.sum()),
            "share_overall": float(d[F].mean())}
    out["tail"] = tail
    # retitling (WP4 audit pairs)
    A = pd.read_csv(AUDIT_PAIRS)
    A = A[A.decision == "accepted"]
    m = d.merge(A[["submission_id", "v1_title", "or_title", "NAME_or", "NAME_v1", "v1_in_review", "v1_lag_days"]],
                on="submission_id", how="inner")
    m["F_v1"] = _v1_status(F, m).to_numpy()
    ct = pd.crosstab(m.F_v1, m[F])
    ret = {"label": LABEL, "source": "outputs/snapshot/audit_pairs.csv (accepted, arXiv v1 posted before the decision)",
           "n_papers": int(len(m)), "years": sorted(int(y) for y in m.year.unique()),
           "max_v1_lag_days_after_deadline": float(m.v1_lag_days.max()),
           "camera_ready_rule_reproduces_feature": _cr_status_check(F, m),
           "n_with_camera_ready": int(m[F].sum()), "n_with_v1": int(m.F_v1.sum()),
           "added_at_camera_ready": int(((m[F] == 1) & (m.F_v1 == 0)).sum()),
           "removed_at_camera_ready": int(((m[F] == 0) & (m.F_v1 == 1)).sum()),
           "crosstab_v1_rows_camera_ready_cols": {int(i): {int(j): int(ct.loc[i, j]) for j in ct.columns} for i in ct.index},
           "camera_ready_exposure_same_papers": core._fit(m, "y", F, C),
           "v1_exposure_same_papers": core._fit(m, "y", "F_v1", C),
           "stable_status_papers_only": _nw(core._fit(m[m[F] == m.F_v1], "y", F, C), m[m[F] == m.F_v1], F),
           "full_sample_same_years_primary_spec": _nw(core._fit(d[d.year.isin(m.year.unique())], "y", F, C),
                                                      d[d.year.isin(m.year.unique())], F),
           "note": "small, selected subsample (accepted papers with an arXiv v1 found by the WP4 audit); SEs are wide"}
    # is the audited subsample different from the rest of the same years? (G x audited interaction; pre-decision preprints)
    s = d[d.year.isin(m.year.unique())].copy()
    s["audited"] = s.submission_id.isin(set(m.submission_id)).astype(int)
    s["F_x_audited"] = s[F] * s.audited
    ia = core._fit(s, "y", "F_x_audited", C + [F, "audited"])
    ret["audited_minus_rest_same_years"] = {"ratio": float(np.exp(ia["b"])), "ratio_lo": float(np.exp(ia["b"] - 1.96 * ia["se"])),
                                            "ratio_hi": float(np.exp(ia["b"] + 1.96 * ia["se"])), "p": ia["p"], "n": ia["n"]}
    pre = s[s.lead_months >= 4]
    ret["full_sample_same_years_arxiv_posted_before_decision"] = _nw(core._fit(pre, "y", F, C), pre, F)
    out["retitling"] = ret
    # combined
    out["combined_arxiv_only_lead_fe_code_method_finding"] = _nw(
        core._fit(a, "y", F, C + ["code_link", "method_abs", "finding_abs"], fe="year^topic50 + lead_bin"), a, F)
    out["combined_arxiv_only_lead_fe_code_method_finding"]["label"] = LABEL
    return out


def summary_lines(res: dict) -> list[str]:
    f = lambda r: f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}] n={r['n']}"
    t, c, p, ta, rt = res["timing"], res["code"], res["paper_type"], res["tail"], res["retitling"]
    return [
        f"timing: lead months {t['mean_lead_months']}; arXiv-only {f(t['arxiv_only_primary_spec'])}; + lead FE {f(t['arxiv_only_plus_lead_bin_fe'])}",
        f"code: share {c['share']}; + code {f(c['plus_code_control'])}; within code {f(c['within_code_abstracts'])}; within other {f(c['within_other_abstracts'])}",
        f"paper type: method {p['share_method']} finding {p['share_finding']}; + both {f(p['plus_method_and_finding_controls'])}",
        f"tail: pctile pp {ta['cite_percentile_outcome_pp']}; drop top5 {f(ta['drop_top5pct_per_year'])}; drop zero {f(ta['drop_zero_citation_records'])}",
        f"retitling: n {rt['n_papers']} added {rt['added_at_camera_ready']} removed {rt['removed_at_camera_ready']}; CR {f(rt['camera_ready_exposure_same_papers'])}; v1 {f(rt['v1_exposure_same_papers'])}; full same years {f(rt['full_sample_same_years_primary_spec'])}; audited-vs-rest p {rt['audited_minus_rest_same_years']['p']:.3f}; pre-decision preprints {f(rt['full_sample_same_years_arxiv_posted_before_decision'])}",
        f"combined: {f(res['combined_arxiv_only_lead_fe_code_method_finding'])}",
    ]
