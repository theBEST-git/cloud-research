"""Fixer check: every key number printed in outputs/d1_break/RESULTS.md is re-derived from the machine-readable
outputs and formatted; the script asserts that the formatted string occurs in RESULTS.md. Prints FAIL lines."""
import json
from pathlib import Path

import pandas as pd

D1 = Path("/home/user/cloud-research/research/titles/outputs/d1_break")
md = (D1 / "RESULTS.md").read_text().replace("\u2212", "-")
R = json.loads((D1 / "results.json").read_text())
CFJ = json.loads((D1 / "content_cf.json").read_text())
DC = json.loads((D1 / "decompose.json").read_text())
T13 = pd.read_csv(D1 / "T1_3_tool_bound.csv")
DM = pd.read_csv(D1 / "tool_delta_models.csv").set_index("spec")
DFL = pd.read_csv(D1 / "dfl_table.csv", keep_default_na=False)


def f3(x):
    return f"{x:.3f}"


def ci3(c):
    return f"[{c[0]:.3f}, {c[1]:.3f}]"


def pp(x, k=2):
    return f"{100 * x:.{k}f}"


def cipp(c, k=2):
    return f"[{100 * c[0]:.{k}f}, {100 * c[1]:.{k}f}]"


checks = []
a = R["H1a"]
checks += [f"OR 1.098 [{a['slope_change_OR_U'][1]:.3f}, {a['slope_change_OR_U'][2]:.3f}]",
           f"OR {a['year_level_U']['OR'][0]:.3f} [{a['year_level_U']['OR'][1]:.3f}, {a['year_level_U']['OR'][2]:.3f}]",
           f"{a['year_level_NA']['OR'][0]:.3f} [{a['year_level_NA']['OR'][1]:.3f}, {a['year_level_NA']['OR'][2]:.3f}]",
           f"p = {a['p_one_sided_year_level']:.3f}"]
yl = a["year_level_all"]
for pop in ["U", "NA pool", "non-LLM subset", "U excluding 2026"]:
    r = yl[pop]["re_logit"]
    checks.append(f"{r['OR']:.3f} [{r['OR_lo']:.3f}, {r['OR_hi']:.3f}]")
    l = yl[pop]["re_lpm"]
    checks.append(f"{l['pp']:+.2f} [{l['pp_lo']:.2f}, {l['pp_hi']:.2f}]")
checks.append(f"[{yl['U']['quasi_binomial']['OR_lo']:.3f}, {yl['U']['quasi_binomial']['OR_hi']:.3f}]")
adj = R["holm"]["adjusted_p"]
checks += [f"{adj['H1a']:.3f}", f"{adj['H1c']:.3f}", f"{adj['H1d']:.3f}", f"{adj['H1e']:.3f}", f"{adj['H1b']:.2f}"]
sh = R["H1b"]["shares"]
for k in ["R1|fixed", "R3|fixed", "R5|fixed", "R1|rolling", "R3|rolling", "R5|rolling", "R1yfe|fixed", "R1yfe|rolling",
          "R3yfe|fixed", "R3yfe|rolling", "R5yfe|fixed", "R5yfe|rolling", "R2|fixed", "R2|rolling", "R6|fixed",
          "R6|rolling", "R6b|fixed", "R6b|rolling", "R4|fixed", "R4|rolling", "R1u|fixed", "R1u|rolling",
          "R1n|fixed", "R1n|rolling", "R1@0.5|fixed", "R1@0.5|rolling"]:
    checks.append(f"{sh[k]['share']:.3f} {ci3(sh[k]['ci'])}")
    checks.append(f"{sh[k]['auc']:.3f} | {sh[k]['cal_slope']:.2f}")
checks += [f"refit {ci3(sh['R1|rolling']['ci_refit'])}", f"refit {ci3(sh['R1|fixed']['ci_refit'])}",
           f"R1 fixed {sh['R1|fixed']['share_slope_recal']:.3f}, rolling **{sh['R1|rolling']['share_slope_recal']:.3f}**",
           f"R5 fixed {sh['R5|fixed']['share_slope_recal']:.3f}, rolling **{sh['R5|rolling']['share_slope_recal']:.3f}**",
           f"R3 fixed {sh['R3|fixed']['share_slope_recal']:.3f}, rolling {sh['R3|rolling']['share_slope_recal']:.3f}"]
c = R["H1c"]
checks += [f"{100 * c['u_pre']:.2f} → {100 * c['u_post']:.2f}".replace(".51 →", ".51 →"),
           cipp(c["diff_ci_conditional"]), cipp(c["refit_bootstrap"]["diff_ci"]),
           cipp(c["year_level_two_stage"]["diff_ci"]), cipp(c["year_level_two_stage_lpm_tau"]["ci_normal"]),
           cipp(c["year_level_two_stage_excluding_2026"]["diff_ci"]), cipp(c["year_level_two_stage_without_2019"]["diff_ci"]),
           f"[{c['year_level_two_stage']['ratio_ci'][0]:.2f}, {c['year_level_two_stage']['ratio_ci'][1]:.2f}]",
           f"[{c['ratio_ci_conditional'][0]:.2f}, {c['ratio_ci_conditional'][1]:.2f}]",
           f"[{c['refit_bootstrap']['ratio_ci'][0]:.2f}, {c['refit_bootstrap']['ratio_ci'][1]:.2f}]"]
for k, v in c["replications"].items():
    if k in ("R1|U|primary|rolling", "R3|U|primary|rolling", "R5|U|primary|rolling", "R1|NA|primary|rolling",
             "R1|non_llm|primary|rolling", "R1|U|strict|rolling", "R1|U|loose|rolling", "R1|U|compound|rolling",
             "R6|U|primary|rolling", "R4|U|primary|rolling"):
        checks.append(f"{cipp(v['diff_ci'])} | {cipp(v['diff_ci_year_robust'])} | {v['ratio']:.2f}")
acc = c["acceleration_decomposition"]
checks += [f"{100 * acc['step_pre_mean']:.2f} to {100 * acc['step_post_mean']:.2f} pp/yr",
           f"{100 * acc['content_step_pre_mean']:.2f} to {100 * acc['content_step_post_mean']:.2f} pp/yr",
           f"{100 * acc['content_fraction_of_acceleration']:.0f}%"]
by = pd.DataFrame(c["by_year"]).set_index("year")
checks.append(" | ".join(f"{100 * v:+.1f}" for v in by.unexplained))
checks.append(" | ".join(f"{100 * v:+.1f}" for v in by.content_step))
d = R["H1d"]["dfl_full_by_year"]
checks += [f"{d['2024']['share']:.3f} {ci3(d['2024']['ci'])}", f"{d['2025']['share']:.3f} {ci3(d['2025']['ci'])}",
           f"{d['2026']['share']:.3f} {ci3(d['2026']['ci'])}"]
s26 = R["H1d"]["shapley"]["2026"]
checks += [f"{s26['shapley_content_share']:.3f}** (conditional {ci3(s26['shapley_content_share_ci'])}",
           f"{s26['shapley_composition_share']:.3f}** (conditional {ci3(s26['shapley_composition_share_ci'])}",
           f"{s26['residual_share']:.3f} (conditional {ci3(s26['residual_share_ci'])}"]
rf = R["H1d"]["shapley_refit_ci"]["2026"]
checks += [f"refit {ci3(rf['shapley_content_ci'])}", f"refit {ci3(rf['shapley_composition_ci'])}", f"refit {ci3(rf['residual_ci'])}"]
for _, r in DFL[(DFL["pop"] == "U") & (DFL.target_year == 2026)].iterrows():
    checks.append(f"{r.share:.3f} [{r.share_lo:.3f}, {r.share_hi:.3f}]")
e = R["H1e"]
cc = e["tool_share_0.39_corrected_2026"]
checks += [f"{100 * cc['share']:.1f}% [{100 * cc['lo']:.1f}, {100 * cc['hi']:.1f}]"]
for spec in ["F_d1, 2026 only", "primary: F_d1, topic100 x year FE"]:
    for _, r in T13[(T13.spec == spec) & (T13.A_max < 1)].iterrows():
        checks.append(f"{100 * r.tool_share:.1f}% [{100 * r.tool_share_lo:.1f}, {100 * r.tool_share_hi:.1f}]")
for spec in ["primary: F_d1, topic100 x year FE", "F_d1, NA pool", "F_d1, non-LLM subset", "F_d1, excluding 2026 (2024-25)",
             "F_d1, 2024 only", "F_d1, 2025 only", "F_d1, 2026 only", "title typography only",
             "title typography only | title has an intra-word dash", "F_d1 x post DiD, 2021-26 (selection-corrected)",
             "F_any x post DiD, 2021-26 (selection-corrected)"]:
    r = DM.loc[spec]
    checks.append(f"{100 * r.delta:+.2f}")
    checks.append(f"[{100 * r.lo:+.2f}, {100 * r.hi:+.2f}]")
for k, v in R["new_topic_placebo"].items():
    if k.startswith("R1|"):
        checks.append(f"{100 * v['gap_diff']:.1f} pp [{100 * v['gap_diff_ci'][0]:.1f}, {100 * v['gap_diff_ci'][1]:.1f}]")
fails = [x for x in checks if x not in md]
print(f"{len(checks)} checks, {len(fails)} not found")
for x in fails:
    print("FAIL:", x)
