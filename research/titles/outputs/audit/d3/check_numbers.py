"""D3 fixer pass: targeted checks that numbers quoted in outputs/d3_register/RESULTS.md match the output files.
Each check formats a value from a results file and asserts the exact string occurs in RESULTS.md.
Run: cd research/titles/src && /home/user/venv/bin/python ../outputs/audit/d3/check_numbers.py"""
import json
from pathlib import Path

import pandas as pd

D = Path(__file__).resolve().parents[2] / "d3_register"
T = (D / "RESULTS.md").read_text()
R = json.loads((D / "results.json").read_text())
H = {h["id"]: h for h in R["hypotheses"]}
checks = []


def ci(a, b, c, k=2):
    return f"{a:.{k}f} [{b:.{k}f}, {c:.{k}f}]"


def add(desc, s):
    checks.append((desc, s, s in T))


# ---------------- H3a
sl = json.loads((D / "slots_results.json").read_text())
p = sl["primary"]
add("H3a pooled", ci(p["slots_post"]["OR"], p["slots_post"]["OR_lo"], p["slots_post"]["OR_hi"]))
add("H3a controls", ci(p["controls_post"]["OR"], p["controls_post"]["OR_lo"], p["controls_post"]["OR_hi"]))
add("H3a stacked", ci(p["stacked_interaction"]["OR"], p["stacked_interaction"]["OR_lo"], p["stacked_interaction"]["OR_hi"]))
rob = pd.read_csv(D / "slot_robustness.csv")


def rr(label, model):
    x = rob[(rob.label == label) & (rob.model == model)].iloc[0]
    return ci(x.OR, x.OR_lo, x.OR_hi)


for lab in ["NA pool (camera-ready-free)", "non-LLM subset", "topic100 FE", "bge topic100 FE",
            "exclude titles whose abstract has the slot word", "opener at title start only",
            "opener after NAME lead only", "excluding 2026", "2024-only post (2018-2024)", "with 2017", "without 2019",
            "unweighted V2 drop rule (also drops unleashing)", "any-compound-lead opener rule (V2 drops kept)",
            "full lexicon (no V2 drops)", "pilot-like: any-lead rule + full lexicon", "+ log authors",
            "no slot trends (level contrast)", "accepted only"]:
    add(f"H3a rob slots {lab}", rr(lab, "slots_post"))
    if lab != "accepted only":
        add(f"H3a rob stacked {lab}", rr(lab, "stacked_interaction"))
add("H3a level-contrast controls", rr("no slot trends (level contrast)", "controls_post"))
add("H3a controls without via", rr("controls without via/using (towards, novel only)", "controls_post"))
add("H3a stacked without via", rr("controls without via/using (towards, novel only)", "stacked_interaction"))
add("H3a stacked year FE", rr("stacked with year FE", "stacked_interaction"))
n_pl = int(rob[(rob.label == "pilot-like: any-lead rule + full lexicon") & (rob.model == "slots_post")].nobs.iloc[0])
add("pilot-like n", f"n = {n_pl:,}")
ps = pd.read_csv(D / "slot_per_slot.csv").set_index("label")
for lab in ["S-improve", "S-reveal", "S-exploit", "towards/toward", "novel/new", "via/using"]:
    x = ps.loc[lab]
    add(f"per-slot {lab}", f"| {lab}{' (control)' if '/' in lab else ''} | {ci(x.OR, x.OR_lo, x.OR_hi)}")
pb = pd.read_csv(D / "slot_placebo_breaks.csv")
cb = pb[(pb.scope == "full_2018_26") & (pb.model == "controls_post")].set_index("break_year")
for y in (2020, 2021, 2022, 2025):
    add(f"control break {y}", ci(cb.loc[y, "OR"], cb.loc[y, "OR_lo"], cb.loc[y, "OR_hi"]))
es = pd.read_csv(D / "slot_event_study.csv")
f = es[es.trends.str.startswith("frozen")].set_index(["model", "year"])
for y in (2023, 2024, 2025):
    x = f.loc[("slots", y)]
    add(f"frozen slots {y}", ci(x.OR, x.OR_lo, x.OR_hi) if y == 2023 else f"{x.OR:.2f} [{x.OR_lo:.2f}, {x.OR_hi:.1f}]")
x = f.loc[("slot_minus_control", 2024)]
add("frozen contrast 2024", f"{x.OR:.2f} [{x.OR_lo:.2f}, {x.OR_hi:.1f}]")
j = es[es.trends.str.startswith("estimated")].set_index(["model", "year"])
x = j.loc[("slots", 2023)]
add("joint slots 2023", ci(x.OR, x.OR_lo, x.OR_hi))
vs = pd.read_csv(D / "slot_variant_rate_shift.csv").set_index(["sample", "slot", "side"])
x = vs.loc[("all", "pooled", "llm")]
add("rate shift llm", ci(x.RR_post, x.lo, x.hi))
x = vs.loc[("all", "pooled", "neutral")]
add("rate shift neutral", ci(x.RR_post, x.lo, x.hi))
vr = pd.read_csv(D / "slot_variant_rates.csv")
v = vr[(vr["sample"] == "all") & (vr.slot == "pooled")].set_index(["side", "year"]).per1k
add("rate llm 2024", f"**{v[('llm', 2024)]:.1f} (2024)**")
add("rate neutral 2024", f"**{v[('neutral', 2024)]:.1f}**")
loo = pd.read_csv(D / "slot_loo.csv")
x = loo[(loo.word == "enhancing") & (loo.model == "slots_post")].iloc[0]
add("loo enhancing", ci(x.OR, x.OR_lo, x.OR_hi))
fl = pd.read_csv(D / "slot_audit_flips.csv").set_index(["period", "decision"])
add("audit pairs", f"**{sl['audit']['meta']['n_usable_pairs']:,}**")
add("audit acc pairs", f"{int(fl.loc[('all', 'accepted'), 'n_pairs'])} accepted")
add("audit rej pairs", f"{int(fl.loc[('all', 'rejected'), 'n_pairs'])} rejected")
add("audit acc llm v1", f"Accepted: {int(fl.loc[('all', 'accepted'), 'n_llm_v1'])} v1 titles")
add("audit acc drops", f"{int(fl.loc[('all', 'accepted'), 'drops_llm'])} drops")
add("audit rej llm v1", f"Rejected: {int(fl.loc[('all', 'rejected'), 'n_llm_v1'])} v1 titles")
add("audit add CP", f"{100 * fl.loc[('all', 'accepted'), 'add_hi']:.2f}%")
add("audit did", f"{sl['audit']['meta']['did_net_llm_adds']['all']['did_pp']:.2f} pp".replace("-", "\u2212"))
add("enlarge n", f"{sl['audit']['meta']['n_enlarge_lines_used']:,} lines")

# ---------------- H3b
rg = json.loads((D / "register_results.json").read_text())
nb = rg["neutral_benchmark"]
x = nb["all|R24_vs_N24_ratio_of_RR"]
add("R24/N24", ci(x["ratio"], x["lo"], x["hi"]))
x = nb["NA pool|R24_vs_N24_ratio_of_RR"]
add("R24/N24 NA", ci(x["ratio"], x["lo"], x["hi"]))
x = nb["all|slot_llm_share"]
add("slot share OR", ci(x["OR_2026_vs_2025"], x["lo"], x["hi"]))
add("slot share 25", f"{x['share_2025']:.3f} (2025)")
add("slot share up", f"up in {x['n_areas_share_up']} and down in {x['n_areas_share_down']} of 16")
x = nb["NA pool|slot_llm_share"]
add("slot share OR NA", ci(x["OR_2026_vs_2025"], x["lo"], x["hi"]))
nbr = pd.DataFrame(nb["rates"]).set_index(["sample", "outcome"])
for o in ("r24_any", "n24", "n24_improv", "r24_enh"):
    x = nbr.loc[("all", o)]
    add(f"nb {o}", ci(x.RR_2026_vs_2025, x.lo, x.hi, 3))
wc = rg["word_churn"]
add("wc RR>=1.5 n", f"{wc['n_words_RR_ge_1p5']} words with an area-stratified RR")
add("wc share up", f"{100 * wc['share_of_those_up_ge12']:.0f}%")
add("wc share down", f"{100 * wc['share_of_those_down_ge10']:.0f}%")
add("wc freq pass", f"{100 * wc['share_freq_words_pass_either_threshold']:.0f}%")
add("wc top", f"top {100 * wc['share_words_RR_ge_R26']:.1f}%")
ctx = rg["context_2024_to_2025"]["reassigned_sensitivity"]
add("ctx n reassigned", f"{ctx['n_reassigned_2025']:,} papers")
x = ctx["new 2025 areas reassigned|r24_any"]
add("ctx reassigned r24", f"R24 up in {x['n_up_2024_to_2025']} of 14")
add("ctx reassigned RR", ci(x["RR_2024_vs_2025"], x["lo"], x["hi"]))
po = pd.read_csv(D / "register_poisson.csv")
x = po[(po.family == "r24_any") & (po.spec == "2023-26 (2023 imputed), large areas")].iloc[0]
add("pois r24", ci(x.RR_2026_vs_2025, x.RR_2026_vs_2025_lo, x.RR_2026_vs_2025_hi, 3))
add("pois r24 2024", ci(x.RR_2024_vs_2025, x.RR_2024_vs_2025_lo, x.RR_2024_vs_2025_hi))
add("pois r24 2023", ci(x.RR_2023_vs_2025, x.RR_2023_vs_2025_lo, x.RR_2023_vs_2025_hi))
x = po[(po.family == "r26_any") & (po.spec == "2023-26 (2023 imputed), large areas")].iloc[0]
add("pois r26", ci(x.RR_2026_vs_2025, x.RR_2026_vs_2025_lo, x.RR_2026_vs_2025_hi, 3))
rng24 = po[po.family == "r24_any"].RR_2026_vs_2025
add("pois r24 range", f"{rng24.min():.3f}–{rng24.max():.3f}")
rng26 = po[po.family == "r26_any"].RR_2026_vs_2025
add("pois r26 range", f"{rng26.min():.3f}–{rng26.max():.3f}")
su = pd.read_csv(D / "register_summary.csv").set_index(["variant", "family"])
x = su.loc[("all", "r24_any")]
add("r24 large 2025", f"{x.rate_2025_large_areas:.1f} in 2025 and {x.rate_2026_std_to_2025_mix:.1f} in 2026")
add("r24 all", f"{x.rate_2025_all:.1f} (2025) to {x.rate_2026_all:.1f} (2026)")

# ---------------- H3c
vt = json.loads((D / "vintage_results.json").read_text())
vv = vt["verdict_inputs"]
add("H3c primary", ci(vv["ratio"], vv["ratio_lo"], vv["ratio_hi"]))
add("H3c n", f"{vv['nobs_logit']:,}")
add("H3c dropped", f"{vv['n_dropped_no_variation']} papers")
for k in ("co_primary_shared_lemma_free", "F26_arm_2026_only", "by_year_2025", "by_year_2026", "NA_pool",
          "pre_LLM_placebo_2018_23", "meaning_fixed_R24_given_R24_or_N24", "meaning_fixed_slot",
          "meaning_fixed_R24_given_R24_or_N24_shared_lemma_free", "meaning_fixed_slot_shared_lemma_free"):
    x = vv[k]
    add(f"H3c {k}", ci(x["ratio"], x["ratio_lo"], x["ratio_hi"]))
x = vv["co_primary_shared_lemma_free"]
add("H3c co-primary F24", ci(x["OR_F24"], x["OR_F24_lo"], x["OR_F24_hi"]))
x = vv["genre_benchmark_N24"]
add("H3c F26->N24", ci(x["OR_F26"], x["OR_F26_lo"], x["OR_F26_hi"]))
add("H3c F24->N24", ci(x["OR_F24"], x["OR_F24_lo"], x["OR_F24_hi"]))
x = vv["pre_LLM_placebo_2018_23"]
add("H3c placebo F24", ci(x["OR_F24"], x["OR_F24_lo"], x["OR_F24_hi"]))
add("H3c placebo F26", ci(x["OR_F26"], x["OR_F26_lo"], x["OR_F26_hi"]))
vm = pd.read_csv(D / "vintage_models.csv")
x = vm[vm.label == "F26 component: principled (typography as covariate)"].iloc[0]
add("H3c principled", ci(x.OR_b, x.OR_b_lo, x.OR_b_hi))
add("H3c principled n", f"n = {int(x.n_xb):,}")
add("H3c mirror", ci(vv["mirror_R26_ratio_F26_over_F24"], vv["mirror_R26_ratio_lo"], vv["mirror_R26_ratio_hi"]))
fp = pd.read_csv(D / "fingerprint_prevalence_by_year.csv").set_index("year")
add("F26 2025 prev", f"{100 * fp.loc[2025, 'f26']:.1f}%")

# ---------------- H3d
sg = pd.read_csv(D / "signature_models.csv").set_index("label")
for lab, nm in [("2024-26 pooled (primary)", "2024–26 pooled (primary)"), ("2024", "2024"), ("2025", "2025"),
                ("2026", "2026"), ("2024-25 (excluding 2026)", "2024–25 (excluding 2026)"), ("NA pool", "NA pool"),
                ("non-LLM subset", "Non-LLM subset"), ("F without harness/unveil (shared lemmas)",
                                                         "F without harness/unveil"),
                ("abstract lacks the slot word", "Abstract lacks the slot word"),
                ("word fingerprints only (no typography)", "Word fingerprints only"),
                ("opener slots only (no study_adj)", "Opener slots only"), ("improve slot only", "Improve slot only"),
                ("F24 only as F", "F24 as F"), ("F26 only as F", "F26 as F"),
                ("F_d1 = F24>=2 | F26 | typography (D1 fingerprint)", "**F_d1 (D1's fingerprint)**")]:
    x = sg.loc[lab]
    row = (f"| {nm} | {ci(x.OR_slot, x.OR_slot_lo, x.OR_slot_hi)} | {ci(x.OR_name, x.OR_name_lo, x.OR_name_hi)} | "
           f"{ci(x.OR_name_pop, x.OR_name_pop_lo, x.OR_name_pop_hi)} | {ci(x.ratio, x.ratio_lo, x.ratio_hi)} | "
           f"{ci(x.ratio_pop, x.ratio_pop_lo, x.ratio_pop_hi)} |")
    add(f"H3d row {lab}", row)
x = sg.loc["pre-LLM 2018-23 (fingerprints are false positives)"]
add("H3d pre slot", ci(x.OR_slot, x.OR_slot_lo, x.OR_slot_hi))
add("H3d pre name pop", ci(x.OR_name_pop, x.OR_name_pop_lo, x.OR_name_pop_hi))
add("H3d pre ratio pop", ci(x.ratio_pop, x.ratio_pop_lo, x.ratio_pop_hi))
x = sg.loc["2024-26 pooled, + log authors on every side"]
add("H3d log authors ratio", ci(x.ratio_pop, x.ratio_pop_lo, x.ratio_pop_hi))
add("H3d log authors name", ci(x.OR_name_pop, x.OR_name_pop_lo, x.OR_name_pop_hi))
x = sg.loc["2024-26 pooled (primary)"]
add("H3d p pop", f"P(ratio ≤ 1) = {x.p_one_ratio_pop_le1:.3f}")
add("H3d p>=1.5", f"P(ratio ≥ 1.5) = {x.p_ratio_pop_ge_1p5:.3f}")
add("H3d p<1.5", f"P(ratio < 1.5) = {x.p_ratio_lt_1p5:.2f}")
add("H3d n pop", f"{int(x.n_pop):,} papers")
sr = json.loads((D / "signature_results.json").read_text())
col = sr["collider_diagnostic"]
add("collider factor", f"**{col['selection_factor_on_OR']:.2f}**")
for k, s in [("NAME0_F0", "4.33%"), ("NAME0_F1", "5.47%"), ("NAME1_F0", "5.78%"), ("NAME1_F1", "5.74%")]:
    add(f"collider {k}", f"{100 * col['p_filled_by_NAME_F'][k]:.2f}%")
lg = sr["logit_signature"]
add("H3d logit ratio", ci(lg["ratio_logit"], lg["ratio_logit_lo"], lg["ratio_logit_hi"]))

# ---------------- H3e
U = pd.read_csv(D / "secondhand_ustar.csv")
pr = U[(U.post == "2024-25") & (U.baseline == "2022-23") & U.slot.isna() & U.variant.isna()].iloc[0]
add("U*", ci(pr.U_star, pr.U_lo, pr.U_hi))
add("U* p", f"P(U* > 0.8) = {pr.p_U_gt_08:.3f}")
add("U* gap F1", f"{pr.gap_F1_pp:.1f} pp [{pr.gap_F1_lo:.1f}, {pr.gap_F1_hi:.1f}]")
add("U* gap F0", f"{pr.gap_F0_pp:.1f} pp [{pr.gap_F0_lo:.1f}, {pr.gap_F0_hi:.1f}]")
x = U[U.variant == "opener slots only (no study_adj)"].iloc[0]
add("U* no study", ci(x.U_star, x.U_lo, x.U_hi))
x = U[U.variant == "topic100-cluster bootstrap"].iloc[0]
add("U* cluster", ci(x.U_star, x.U_lo, x.U_hi))
x = U[(U.post == "2024-26") & (U.baseline == "2022-23") & U.slot.isna() & U.variant.isna()].iloc[0]
add("U* 2024-26", ci(x.U_star, x.U_lo, x.U_hi))
x = U[(U.post == "2024") & (U.baseline == "2022-23") & U.slot.isna() & U.variant.isna()].iloc[0]
add("U* 2024", ci(x.U_star, x.U_lo, x.U_hi))
for s in ("improve", "reveal", "exploit"):
    x = U[U.slot == s].iloc[0]
    add(f"U* slot {s}", f"{s} {x.U_star:.2f}" if s != "exploit" else f"exploit **{x.U_star:.2f}**")

# ---------------- Holm and power
hl = R["holm"]
for k, v in hl["adjusted_p"].items():
    add(f"holm {k}", f"{v:.4f}".rstrip("0") if v < 0.001 else f"{v:.4f}"[:6].rstrip("0"))
add("holm sens H3d", f"{hl['sensitivity']['adjusted_p']['H3d']:.3f}")
pw = R["heldout_projected_power"]
add("power", f"{pw['CT4']['P(confirm) at alpha 0.0083']:.2f} / {pw['CT7']['alpha_0.0083']:.2f} / "
             f"{pw['CT8']['alpha_0.0083']:.2f}")

bad = [c for c in checks if not c[2]]
print(f"{len(checks)} checks, {len(bad)} not found")
for d_, s, _ in bad:
    print("  MISSING:", d_, "->", repr(s))
