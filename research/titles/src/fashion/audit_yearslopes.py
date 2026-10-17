"""Audit: the pooled interaction specs (H4, H6) are confounded by year-varying momentum slopes x year-varying moderator
shares (within-year permutation of G1_name gives a null t centred at +0.74, not 0; centred at 0 once mom_p x year is
added). Re-estimate H4 and H6 with year-specific momentum slopes (mom_p:C(year)). Discovery data only.
Writes outputs/fashion/explore/audit/results_yearslopes.csv.
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.audit_common import AUD, est
from fashion.audit_tests import lincomb
from fashion.audit_vars import with_variants

warnings.filterwarnings("ignore")
ROWS = []
YS = " + mom_p:C(year)"


def run(h, test, d, y, rhs, terms, fe="year"):
    r = est(d, y, rhs, fe=fe, terms=terms)
    for k, (b, se, p, n) in r.items():
        ROWS.append(dict(h=h, test=test, term=k, b=b, se=se, p=p, n=n))
    print(f"{h:4s} {test:55s} " + "  ".join(f"{k}={b:+.3f}({se:.3f})" for k, (b, se, p, n) in r.items()) + f"  n={n}")


def diff(h, test, d, y, rhs, w, fe="year"):
    b, se, n = lincomb(d, y, rhs, fe, w)
    ROWS.append(dict(h=h, test=test, term="contrast", b=b, se=se, p=np.nan, n=n))
    print(f"{h:4s} {test:55s} contrast = {b:+.3f} ({se:.3f}) t={b / se:.2f}  n={n}")


def main():
    f = with_variants()
    f["l_team_prev"] = np.log1p(f.team_prev_n)
    u = C.load_universe(["submission_id", "lsum_prior_accs"])
    f = f.merge(u, on="submission_id", how="left")
    acc = f[(f.ACC == 1) & (f.year <= 2025) & f.top10.notna()].copy()
    h4 = f[(f.year.between(2022, 2025)) & f.hit.notna()].copy()
    H4R = "ins*mom_p + ent*mom_p + size_p + nnr_p + log_authors + lprior_acc"
    w = {"ins:mom_p": 1, "ent:mom_p": -1}
    # ---- H4 ----
    run("H4", "baseline", h4, "hit", H4R, ["ins:mom_p", "ent:mom_p"])
    run("H4", "+ mom_p x year", h4, "hit", H4R + YS, ["ins:mom_p", "ent:mom_p"])
    diff("H4", "+ mom_p x year: ins-ent slope", h4, "hit", H4R + YS, w)
    diff("H4", "+ mom_p x year, same-team-free mom", h4, "hit",
         H4R.replace("mom_p", "mom_p_nt").replace("size_p", "size_p_nt").replace("nnr_p", "nnr_p_nt") + " + mom_p_nt:C(year)",
         {"ins:mom_p_nt": 1, "ent:mom_p_nt": -1})
    diff("H4", "+ mom_p x year + l_team_prev*mom_p", h4, "hit", H4R + YS + " + l_team_prev*mom_p", w)
    diff("H4", "+ mom_p x year + team_area_acc*mom_p", h4, "hit", H4R + YS + " + team_area_acc*mom_p", w)
    diff("H4", "+ mom_p x year + l_team_prev*mom_p + team_area_acc*mom_p", h4, "hit",
         H4R + YS + " + l_team_prev*mom_p + team_area_acc*mom_p", w)
    diff("H4", "+ mom_p x year + topic100 FE", h4, "hit", H4R + YS, w, fe="year + topic100")
    diff("H4", "+ mom_p x year, non-LLM", h4[h4.llm_topic == 0], "hit", H4R + YS, w)
    diff("H4", "+ mom_p x year, 2023-25", h4[h4.year >= 2023], "hit", H4R + YS, w)
    a22 = acc[acc.year >= 2022]
    diff("H4", "[top10|acc] + mom_p x year", a22, "top10", H4R + YS, w)
    diff("H4", "[acc_rev] + mom_p x year", h4, "acc_rev", H4R + YS, w)
    # ---- H6 ----
    G = "G1_name*mom_p + size_p + nnr_p + log_authors"
    run("H6", "baseline", acc, "top10", G, ["G1_name:mom_p"])
    run("H6", "+ mom_p x year", acc, "top10", G + YS, ["G1_name:mom_p"])
    run("H6", "+ mom_p x year + G5a, G2, llm_topic", acc, "top10", G + YS + " + G5a_length5 + G2_assertive + llm_topic",
        ["G1_name:mom_p"])
    run("H6", "+ mom_p x year + G5a, G2, llm_topic + topic50 FE", acc, "top10",
        G + YS + " + G5a_length5 + G2_assertive + llm_topic", ["G1_name:mom_p"], fe="year + topic50")
    ctl_x = " + (G5a_length5 + G2_assertive + llm_topic + log_authors + G3_question + G4_llm_words)*mom_p"
    run("H6", "+ mom_p x year + controls x mom_p + topic50 FE", acc, "top10", G + YS + ctl_x, ["G1_name:mom_p"],
        fe="year + topic50")
    run("H6", "+ mom_p x year + G1 x year", acc, "top10", G + YS + " + G1_name:C(year)", ["G1_name:mom_p"])
    run("H6", "+ mom_p x year, outcome cite_pct", acc, "cite_pct", G + YS, ["G1_name:mom_p"])
    run("H6", "+ mom_p x year, outcome log1p cites", acc, "y", G + YS, ["G1_name:mom_p"])
    run("H6", "+ mom_p x year, non-LLM", acc[acc.llm_topic == 0], "top10", G + YS, ["G1_name:mom_p"])
    run("H6", "+ mom_p x year, same-team-free heat", acc, "top10",
        "G1_name*mom_p_nt + size_p_nt + nnr_p_nt + log_authors + mom_p_nt:C(year)", ["G1_name:mom_p_nt"])
    for tau in (78, 82, 85):
        run("H6", f"+ mom_p x year, tau 0.{tau}", acc, "top10",
            f"G1_name*mom_p_{tau} + size_p_{tau} + nnr_p_{tau} + log_authors + mom_p_{tau}:C(year)", [f"G1_name:mom_p_{tau}"])
    # placebo family with year slopes
    for g in ["ortho_mixed_case", "G5b_informative", "G4_llm_words"]:
        d = acc.copy()
        d[g] = d[g].astype(float)
        run("H6", f"family + mom_p x year: {g}", d, "top10", f"{g}*mom_p + size_p + nnr_p + log_authors" + YS, [f"{g}:mom_p"])
    # nnr x mom exploratory with year slopes
    R = "size_p + mom_p*nnr_p + log_authors"
    run("NNR", "acc mom x nnr + mom_p x year", f[f.acc_rev.notna()], "acc_rev", R + YS, ["nnr_p", "mom_p:nnr_p"])
    run("NNR", "top10 mom x nnr + mom_p x year", acc, "top10", R + YS, ["nnr_p", "mom_p:nnr_p"])
    pd.DataFrame(ROWS).to_csv(AUD / "results_yearslopes.csv", index=False)


if __name__ == "__main__":
    main()
