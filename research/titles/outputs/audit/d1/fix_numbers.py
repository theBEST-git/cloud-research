"""Fixer helper: print every number RESULTS.md quotes, straight from the regenerated D1 outputs (no estimation)."""
import json
from pathlib import Path

import pandas as pd

D1 = Path("/home/user/cloud-research/research/titles/outputs/d1_break")
R = json.loads((D1 / "results.json").read_text())
CFJ = json.loads((D1 / "content_cf.json").read_text())
DC = json.loads((D1 / "decompose.json").read_text())
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)


def f(x, k=3):
    return None if x is None else round(x, k)


print("== verdicts", {k: R[k]["verdict"] for k in ["H1a", "H1b", "H1c", "H1d", "H1e"]})
print("== holm", json.dumps(R["holm"]["raw_p"]), json.dumps(R["holm"]["adjusted_p"]))
print("   paper", json.dumps(R["holm"]["alternative_paper_level"]["adjusted_p"]))
print("   rand ", json.dumps(R["holm"]["alternative_H1a_randomization"]["adjusted_p"]))
a = R["H1a"]
print("== H1a", a["slope_change_OR_U"], a["lpm_slope_change_pp_U"], a["lpm_pre_slope_pp_U"], a["pre_slope_OR_U"])
print("   year-level U", a["year_level_U"], "NA", a["year_level_NA"])
for p, v in a["year_level_all"].items():
    print("  ", p, {k: f(vv, 4) for k, vv in v["re_logit"].items() if isinstance(vv, float)})
    print("   lpm", {k: f(vv, 3) for k, vv in v["re_lpm"].items() if k in ("pp", "pp_lo", "pp_hi", "p_one_sided_t", "tau_year_shock")})
    print("   quasi", {k: f(vv, 4) for k, vv in v["quasi_binomial"].items()})
print("   p paper", a["p_one_sided_paper_level"], "p year", a["p_one_sided_year_level"], "rand", a["randomization_p"])
b = R["H1b"]
for k, v in b["shares"].items():
    if v.get("status") == "pending":
        continue
    print("   ", k, f(v["share"]), [f(x) for x in v["ci"]], "auc", f(v["auc"]), "cs", f(v["cal_slope"], 2),
          "sr", f(v.get("share_slope_recal")), "b", f(v.get("slope_recal_mean_b"), 2), "refit", v.get("ci_refit"),
          "p>=.6", f(v["p_ge_0_6"]), v.get("p_ge_0_6_refit"))
print("== H1b", {k: b[k] for k in ["masked_range_preregistered", "masked_range_year_fe", "masked_range_slope_recal",
                                    "honest_range_all_specs", "rolling_ci_contains_0.60", "p_IUT_share_ge_0.60"]})
c = R["H1c"]
print("== H1c", {k: c[k] for k in ["u_pre", "u_post", "diff", "diff_ci_conditional", "ratio", "ratio_ci_conditional",
                                    "p_ratio_lt_1_5_conditional", "p_conditional", "p_paper_level", "p_used"]})
print("   refit", {k: c["refit_bootstrap"][k] for k in ["diff_ci", "diff_se", "ratio_ci", "content_share_post_steps_ci",
                                                         "p_share_ge_0_6", "p_diff_le0"]})
print("   two-stage", {k: v for k, v in c["year_level_two_stage"].items()})
print("   two-stage lpm", c["year_level_two_stage_lpm_tau"])
print("   excl26", {k: c["year_level_two_stage_excluding_2026"][k] for k in ["diff_ci", "p_diff_le0", "ratio_ci"]})
print("   w/o19", {k: c["year_level_two_stage_without_2019"][k] for k in ["diff_ci", "p_diff_le0", "ratio_ci"]})
print("   perm", c["year_permutation"])
print("   acc", c["acceleration_decomposition"])
print("   by_year")
print(pd.DataFrame(c["by_year"])[["year", "obs", "step", "content_step", "unexplained", "auc", "cal_slope"]].round(4).to_string())
print("   excl26", c["excluding_2026"], "w/o19", c["without_2019"])
print("   established", {k: v for k, v in c.get("established_topics_only", {}).items() if k != "by_year"})
for k, v in c["replications"].items():
    print("   repl", k, f(100 * v["diff"], 2), [f(100 * x, 2) for x in v["diff_ci"]], f(v["ratio"], 2),
          [f(x, 2) for x in v["ratio_ci"]], "yr", [f(100 * x, 2) for x in v["diff_ci_year_robust"]],
          f(v["p_year_robust"], 3), "perm", f(v["p_perm"], 3), "share", f(v["content_share_post_steps"], 3))
d = R["H1d"]
print("== H1d", d["dfl_full_by_year"], d["p_share_ge_0.5"])
for yv, v in d["shapley"].items():
    print("   shapley", yv, {k: (f(vv) if isinstance(vv, float) else vv) for k, vv in v.items() if not isinstance(vv, str)})
print("   shapley refit", d["shapley_refit_ci"])
print(pd.read_csv(D1 / "dfl_table.csv", keep_default_na=False).round(3).to_string())
print("   comp", DC["composition_descriptives"])
print("   newkey", DC["new_key_share_by_year"])
e = R["H1e"]
print("== H1e crit", e["criteria"], "p", e["p_IUT"], e["p_F0_ratio_le_0.70"], e["p_tool_share_ge_0.5"])
for F, v in e["f0_rise"].items():
    for yv, vv in v.items():
        print("   f0", F, yv, {k: f(x, 4) if isinstance(x, float) else x for k, x in vv.items()})
print("   corrected 2026", e["tool_share_0.39_corrected_2026"], "naive", e["tool_share_0.39_naive_preregistered"])
t = e["tool"]
print("   delta prim", t["delta_primary"], "d26", t["delta_2026"], "dname", t["dNAME_2023_2026"], t["fpr_2023"], t["share_F_2026"])
for A in ["0.24", "0.39", "0.5", "0.75", "1.0"]:
    print("   A", A, "naive", {k: f(v) for k, v in t["tool_share_at_A_naive"][A].items()},
          "corr pooled", {k: (f(v) if isinstance(v, float) else v) for k, v in t["tool_share_at_A_corrected_pooled_delta"][A].items()},
          "corr 26", {k: (f(v) if isinstance(v, float) else v) for k, v in t["tool_share_at_A_corrected_2026_delta"][A].items()})
print("   detectable", t["detectable_only_contribution"])
print(pd.read_csv(D1 / "tool_delta_models.csv").round(4).to_string())
T13 = pd.read_csv(D1 / "T1_3_tool_bound.csv")
print(T13[T13.A_max.isin([0.39, 1.0])][["spec", "A_max", "delta", "tool_share_naive", "tool_share_naive_hi", "k",
                                         "tool_share", "tool_share_lo", "tool_share_hi"]].round(3).to_string())
print("== new-topic placebo")
for k, v in R["new_topic_placebo"].items():
    print("  ", k, "fast", f(100 * v["signed_res_fast"], 2), "else", f(100 * v["signed_res_else"], 2), "n_fast", v["n_fast"],
          "absF", f(100 * v["abs_gap_fast"], 2), "absE", f(100 * v["abs_gap_else"], 2), "gap", f(100 * v["gap_diff"], 2),
          [f(100 * x, 2) for x in v["gap_diff_ci"]], "signed", f(100 * v["signed_gap_diff"], 2), "pass", v["pass"])
print("== placebo window", json.dumps(R["placebo_window"], indent=None)[:3000])
print("== v4", {k: v for k, v in R["v4_leakage"].items() if k != "auc"})
print("== variants", json.dumps({k: {kk: (f(vv) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in R["content_variants"].items()}, indent=None)[:4000])
T12 = pd.read_csv(D1 / "T1_2_representations.csv")
print(T12.round(3).to_string())
T11 = pd.read_csv(D1 / "T1_1_its.csv", keep_default_na=False)
print(T11[["spec", "pool", "outcome", "nobs", "slope_change_OR", "slope_change_OR_lo", "slope_change_OR_hi", "lpm_slope_change_pp",
           "lpm_slope_change_pp_lo", "lpm_slope_change_pp_hi"]].round(3).to_string())
print(pd.read_csv(D1 / "its_year_deviation.csv", keep_default_na=False).round(3).to_string())
