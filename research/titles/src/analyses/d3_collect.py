"""WP7 / D3: collect the four D3 result files into outputs/d3_register/results.json (machine-readable estimates,
verdicts against the PLAN falsification criteria, Holm over the pre-specified family H3a-H3d, robustness checks,
deviations). Verdicts are mechanical; RESULTS.md gives the interpretation.

All D3 estimates use the DISCOVERY split, on which the PLAN pilots were also computed; the verdicts are discovery-sample
replications of pre-specified rules, not confirmations (confirmation: held-out CT4 = H3a, CT7 = H3c, CT8 = H3b).
Fixer pass (audit/d3): H3d verdict uses the population NAME comparator as co-primary (the same-paper comparator is
collider-conditioned); H3b is labelled descriptive (R26 selected in-sample; neutral synonyms fell alike); H3c's vintage
reading is reported as not established; a sensitivity Holm family (H3d with the population comparator, H3b excluded)
is added next to the pre-specified one.

Run (after d3_slots, d3_register, d3_vintage, d3_signature_bound):
    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d3_collect
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from analyses import d3_slots as D3

OUTDIR = D3.OUTDIR
SRC = Path(__file__).resolve().parent


def holm(p: dict) -> dict:
    keys = sorted(p, key=lambda k: p[k])
    m = len(keys)
    out, run = {}, 0.0
    for i, k in enumerate(keys):
        run = max(run, min(1.0, (m - i) * p[k]))
        out[k] = run
    return out


def r(x, k=4):
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        return x
    return None if not np.isfinite(x) else round(x, k)


def pick(rows, **kw):
    for row in rows:
        if all(row.get(k) == v for k, v in kw.items()):
            return row
    return None


def main():
    sl = json.loads((OUTDIR / "slots_results.json").read_text())
    rg = json.loads((OUTDIR / "register_results.json").read_text())
    vt = json.loads((OUTDIR / "vintage_results.json").read_text())
    sg = json.loads((OUTDIR / "signature_results.json").read_text())
    inv = json.loads((OUTDIR / "slot_inventory.json").read_text())
    pb = pd.read_csv(OUTDIR / "slot_placebo_breaks.csv")
    loo = pd.read_csv(OUTDIR / "slot_loo.csv")
    dry = json.loads((OUTDIR.parent / "prereg" / "dryrun.json").read_text())["results"]
    power = {ct: dry[ct]["projected_heldout_power"] for ct in ("CT4", "CT7", "CT8")}

    # ---------------- H3a
    P = sl["primary"]
    sp, cp, si = P["slots_post"], P["controls_post"], P["stacked_interaction"]
    v = sl["verdict_inputs"]
    yl = {x["model"]: x for x in sl["year_level"]}
    rob = sl["robustness"]

    def rob_row(label, model):
        x = pick(rob, label=label, model=model)
        if x is None:
            return None
        if x.get("OR") is not None:
            return dict(OR=r(x["OR"], 3), lo=r(x["OR_lo"], 3), hi=r(x["OR_hi"], 3), p_one=r(x["p_one"], 5),
                        n=x.get("nobs"))
        return dict(pp=r(x.get("pp"), 2), lo=r(x.get("pp_lo"), 2), hi=r(x.get("pp_hi"), 2), p_one=r(x["p_one"], 5),
                    n=x.get("nobs"))
    labels = sorted({x["label"] for x in rob})
    h3a_rob = {lab: {m: rob_row(lab, m) for m in ("slots_post", "controls_post", "stacked_interaction")
                     if rob_row(lab, m) is not None} for lab in labels}
    vrs = {(x["sample"], x["slot"], x["side"]): x for x in sl["variant_rate_shift"]}
    rr_llm = vrs[("all", "pooled", "llm")]["RR_post"]
    rr_neu = vrs[("all", "pooled", "neutral")]["RR_post"]
    loo_enh = loo[(loo.word == "enhancing") & (loo.model == "slots_post")].iloc[0]
    lvl = pick(rob, label="no slot trends (level contrast)", model="controls_post")
    h3a_verdict = "falsified" if v["falsified"] else (
        "supported" if (v["pooled_OR_ge_2"] and v["control_OR_in_067_15"] and v["stacked_CI_excludes_0"])
        else "partially_supported")
    H3a = dict(
        id="H3a", statement="Meaning-fixed LLM title slots break at 2024: pooled post OR >= 2; control pairs post OR in "
                            "[0.67, 1.5]; slot-minus-control log OR > 0 (stacked post x LLM-slot, CT4 parameter).",
        model="logit y ~ slot FE + slot x (t-2023) + post + llm_topic, 2018-26, CRV by topic100; frozen V2 inventory; "
              "primary opener rule (after an optional NAME lead)",
        estimates=dict(
            pooled_slots_post=dict(OR=r(sp["OR"], 3), lo=r(sp["OR_lo"], 3), hi=r(sp["OR_hi"], 3), p_one=r(sp["p_one"], 6),
                                   n=sp["nobs"], n_post=sp["n_post"], share_pre=r(sp["share_pre"], 3),
                                   share_post=r(sp["share_post"], 3)),
            controls_post=dict(OR=r(cp["OR"], 3), lo=r(cp["OR_lo"], 3), hi=r(cp["OR_hi"], 3), p_one=r(cp["p_one"], 4),
                               n=cp["nobs"]),
            stacked_interaction=dict(OR=r(si["OR"], 3), lo=r(si["OR_lo"], 3), hi=r(si["OR_hi"], 3),
                                     log_or=r(si["coef"], 4), se=r(si["se"], 4), p_one=r(si["p_one"], 6), n=si["nobs"]),
            lpm=sl["primary_lpm"],
            year_level_REML=yl, randomization_over_break_years=sl["randomization"],
            event_study_trends_estimated_jointly=sl["event_study"],
            event_study_trends_frozen_2018_22=sl["event_study_frozen_trends"],
            placebo_pre_only=sl["placebo_pre_only"],
            control_break_scan=[{k: r(x[k], 4) for k in ("break_year", "OR", "OR_lo", "OR_hi", "p_two")}
                                for x in pb[(pb.scope == "full_2018_26") & (pb.model == "controls_post")]
                                .to_dict(orient="records")],
            level_contrast_no_slot_trends={m: rob_row("no slot trends (level contrast)", m) for m in
                                           ("slots_post", "controls_post", "stacked_interaction")},
            addition_vs_substitution_rates=dict(
                level_shift_vs_2018_23_trend=[{k: (r(v_, 4) if isinstance(v_, float) else v_) for k, v_ in x.items()}
                                              for x in sl["variant_rate_shift"]],
                note="per-1,000-title rates of LLM-favoured vs neutral variants (slot_variant_rates.csv): the 2024 "
                     "share break is an addition of LLM-variant openers; neutral variants fall only in 2025-26"),
            leave_out_enhancing={m: {k: r(x[k], 3) for k in ("OR", "OR_lo", "OR_hi", "p_one")} for m, x in
                                 loo[(loo.word == "enhancing")].set_index("model").to_dict(orient="index").items()}),
        per_slot=[{k: (r(x[k], 4) if isinstance(x[k], float) else x[k]) for k in
                   ("slot", "label", "estimator", "n", "n_pre", "n_post", "share_pre", "share_post", "OR", "OR_lo",
                    "OR_hi", "pp", "pp_lo", "pp_hi", "p_one", "q_BH_one_sided") if k in x} for x in sl["per_slot"]],
        robustness=h3a_rob, leave_one_variant_out=sl["loo_summary"],
        camera_ready_audit=sl["audit"],
        p_one_sided=v["p_H3a_intersection_union"],
        p_note="intersection-union: max of the one-sided p for pooled post > 0 and stacked interaction > 0",
        verdict=h3a_verdict,
        verdict_detail=("pre-specified rule met in the discovery split. Caveats: the share rise is an addition of "
                        f"LLM-variant openers (per-1k rate level shift x{rr_llm:.1f}; neutral x{rr_neu:.2f}) without "
                        "displacement of neutral synonyms until 2025-26; the OR >= 2 margin depends on 'enhancing', a "
                        f"word the scout selected in this data (without it OR {loo_enh.OR:.2f} [{loo_enh.OR_lo:.2f}, "
                        f"{loo_enh.OR_hi:.2f}]); the pooled control null holds at the pre-registered 2024 break only "
                        "(controls shift significantly at every other candidate year 2020-23 and 2025, and under a "
                        f"level contrast, OR {lvl['OR']:.2f}); not sharply dated against 2023"),
        verdict_inputs=v)

    # ---------------- H3b
    rv = rg["verdict_inputs"]
    summ = rg["summary"]
    pois = rg["poisson"]

    def pois_row(fam, spec):
        x = pick(pois, family=fam, spec=spec)
        return dict(RR_2026_vs_2025=r(x["RR_2026_vs_2025"], 3), lo=r(x["RR_2026_vs_2025_lo"], 3),
                    hi=r(x["RR_2026_vs_2025_hi"], 3), RR_2024_vs_2025=r(x.get("RR_2024_vs_2025"), 3),
                    RR_2023_vs_2025=r(x.get("RR_2023_vs_2025"), 3), dispersion=r(x["dispersion"], 3))
    H3b = dict(
        id="H3b", statement="From 2025 to 2026 the R24 title rate falls within area in >= 10 of 16 large areas and R26 "
                            "rises in >= 12 of 16; falsified if fewer than 9 of 16 move as predicted.",
        estimates=dict(
            r24_down=f"{rv['r24_down_areas']}/{rv['n_areas']}", r26_up=f"{rv['r26_up_areas']}/{rv['n_areas']}",
            sign_test_p_r24=r(rv["p_sign_r24"], 6), sign_test_p_r26=r(rv["p_sign_r26"], 7),
            rates_per_1k={k: dict(r2025=r(x["rate_2025_all"], 1), r2026=r(x["rate_2026_all"], 1),
                                  r2026_std_to_2025_mix=r(x["rate_2026_std_to_2025_mix"], 1),
                                  n_predicted_direction=x["n_predicted_direction"],
                                  sign_p=r(x["sign_test_p_one"], 5)) for k, x in summ.items()},
            poisson_area_FE={f"{fam}|{spec}": pois_row(fam, spec) for fam in ("r24_any", "r26_any", "r24_n", "r26_n")
                             for spec in ("2023-26 (2023 imputed), large areas", "2024-26, large areas",
                                          "2025-26, large areas", "2023-26, all areas")},
            all_21_areas=rg["all21_areas"], context_2024_to_2025_taxonomy_confounded=rg["context_2024_to_2025"],
            large_areas=rg["large_areas"], area_imputation_2023=rg["area_imputation"],
            neutral_synonym_benchmark=rg["neutral_benchmark"], word_churn_benchmark=rg["word_churn"]),
        p_one_sided=rv["p_H3b_intersection_union"],
        p_note=("intersection-union: max of the two one-sided sign tests. NOT a valid test of R26: the R26 words were "
                "chosen after the scout/pilot saw them rise in this discovery data; the 16 areas share one 2025->2026 "
                "transition (common shock), so the sign test measures how pervasive the move is, not independent "
                "replication. Descriptive; inference deferred to held-out CT8."),
        verdict="falsified" if rv["falsified"] else (
            "thresholds met (descriptive); register turnover not identified"
            if (rv["r24_meets_prediction_ge10"] and rv["r26_meets_prediction_ge12"]) else "partially_supported"),
        verdict_detail=("the sign thresholds are met, but R24 fell no more than its neutral synonyms (ratio of RRs "
                        f"{rg['neutral_benchmark']['all|R24_vs_N24_ratio_of_RR']['ratio']:.2f}) and the LLM-variant "
                        "share within meaning-fixed slots did not fall (OR 2026/2025 "
                        f"{rg['neutral_benchmark']['all|slot_llm_share']['OR_2026_vs_2025']:.2f}); what fell is how "
                        "often titles are framed as improving/exploiting; R26 is not an LLM register (vintage mirror "
                        "null) and was selected in-sample"),
        verdict_inputs=rv)

    # ---------------- H3c
    vv = vt["verdict_inputs"]
    M = vt["models"]

    def vrow(label, fam):
        x = pick(M, label=label, outcome_family=fam)
        if x is None:
            return None
        return dict(outcome=x["outcome"], x_a=x["x_a"], x_b=x["x_b"], OR_a=r(x["OR_a"], 3),
                    OR_a_ci=[r(x["OR_a_lo"], 3), r(x["OR_a_hi"], 3)], OR_b=r(x["OR_b"], 3),
                    OR_b_ci=[r(x["OR_b_lo"], 3), r(x["OR_b_hi"], 3)], ratio=r(x["ratio"], 3),
                    ratio_ci=[r(x["ratio_lo"], 3), r(x["ratio_hi"], 3)], p_one=r(x["p_one"], 5), n=x["nobs"])
    H3c = dict(
        id="H3c", statement="2025-26, logit with year FE, topic100 FE, log authors, llm_topic, log title length: "
                            "OR(F24 -> R24 in title) > OR(F26 -> R24 in title). Falsified if the ratio is <= 1.",
        estimates=dict(primary=vrow("primary 2025-26", "R24"), mirror_R26_exploratory=vrow("primary 2025-26", "R26"),
                       co_primary_shared_lemma_free=vrow("both without harness/unveil", "R24"),
                       F26_arm_2026_only=vrow("F26 arm = F26 x 2026 (F26 x 2025 as covariate)", "R24"),
                       pre_LLM_placebo_2018_23=vrow("pre-LLM placebo 2018-23", "R24"),
                       genre_benchmark_N24=vrow("genre benchmark: neutral N24 outcome (improv*|utili[sz]*|exploit*)",
                                                "N24"),
                       meaning_fixed_shared_lemma_free=vrow(
                           "meaning-fixed, both without harness/unveil: R24 among titles with R24 or N24", "R24"),
                       meaning_fixed_slot_shared_lemma_free=vrow(
                           "meaning-fixed, without harness/unveil: LLM slot variant | slot filled (slot FE)", "R24"),
                       lpm_topic_x_year=vt["lpm"], fingerprint_prevalence=vt["fingerprint_prevalence"]),
        robustness={f"{x['outcome_family']}|{x['label']}": vrow(x["label"], x["outcome_family"]) for x in M},
        p_one_sided=vv["p_one"],
        verdict="falsified" if vv["falsified"] else (
            "prediction met; vintage reading not established" if vv["ratio_CI_excludes_1"] else "partially_supported"),
        verdict_detail=("pre-registered ratio > 1 with CI excluding 1. The contrast is carried by F26 papers avoiding "
                        "R24 (F26 does not mark the 2026 vintage in 2025, where its prevalence equals the pre-LLM base "
                        "rate); no positive F24 -> R24 association beyond the shared lemmas harness/unveil (OR "
                        f"{vv['co_primary_shared_lemma_free']['OR_F24']:.2f}); weaker in the NA pool and in 2026 alone "
                        "(CIs include 1); the R26 mirror is null; the pre-LLM placebo is uninformative, so a writer-type "
                        "confound is not excluded. Conditional on meaning (LLM-favoured vs neutral word) the contrast is "
                        "larger and F24 is positive"),
        verdict_inputs=vv)

    # ---------------- H3d
    dv = sg["verdict_inputs_H3d"]
    S = sg["signature"]

    def srow(x):
        return {k: (r(x[k], 4) if isinstance(x[k], float) else x[k]) for k in
                ("label", "x", "n_papers", "n_slot_rows", "n_F1", "p0_slot", "p0_name", "delta_slot_pp",
                 "delta_name_pp", "OR_slot", "OR_slot_lo", "OR_slot_hi", "OR_name", "OR_name_lo", "OR_name_hi",
                 "ratio", "ratio_lo", "ratio_hi", "p_one_ratio_le1", "p_ratio_lt_1p5", "n_boot", "estimable",
                 "n_pop", "OR_name_pop", "OR_name_pop_lo", "OR_name_pop_hi", "ratio_pop", "ratio_pop_lo",
                 "ratio_pop_hi", "p_one_ratio_pop_le1", "p_ratio_pop_ge_1p5", "p_one_OR_slot_le1") if k in x}
    H3d = dict(
        id="H3d", statement="2024-26 within topic100 x year: OR(F -> LLM slot variant | slot filled) >= 1.5 x OR(F -> "
                            "NAME) (same papers; two LPMs, seemingly-unrelated cluster bootstrap). Falsified if "
                            "OR_slot <= OR_NAME.",
        estimates=dict(primary=srow(S[0]), name_all_2024_26_population=sg["name_all_2024_26"],
                       population_comparator=dict(OR_slot=r(dv["OR_slot"], 3), OR_name_pop=r(dv["OR_name_pop"], 3),
                                                  OR_name_pop_ci=[r(dv["OR_name_pop_lo"], 3),
                                                                  r(dv["OR_name_pop_hi"], 3)],
                                                  ratio=r(dv["ratio_pop"], 3),
                                                  ratio_ci=[r(dv["ratio_pop_lo"], 3), r(dv["ratio_pop_hi"], 3)],
                                                  p_one_ratio_le1=r(dv["p_one_ratio_pop_le1"], 4),
                                                  p_ratio_ge_1p5=r(dv["p_ratio_pop_ge_1p5"], 4)),
                       collider_diagnostic=sg["collider_diagnostic"],
                       logit_and_conditional_logit=sg["logit_signature"]),
        robustness=[srow(x) for x in S[1:]],
        p_one_sided=dv["p_one_ratio_le1"],
        p_note="bootstrap share of draws with OR_slot / OR_NAME <= 1 (1,000 draws), same-paper comparator (PLAN)",
        p_one_sided_population_comparator=dv["p_one_ratio_pop_le1"],
        verdict="falsified" if (dv["falsified"] and dv["falsified_pop"]) else (
            "supported" if (dv["prediction_ratio_ge_1p5"] and dv["ratio_lo"] > 1 and dv["prediction_ratio_pop_ge_1p5"]
                            and dv["ratio_pop_lo"] > 1) else "partially supported"),
        verdict_detail=("same-paper comparator (PLAN): ratio >= 1.5 by the point estimate and CI excluding 1, but that "
                        "comparator is collider-conditioned (selection factor "
                        f"{dv['collider_selection_factor']:.2f} on the OR) and on the same papers NAME is just the slot "
                        "word's position; population comparator (same FE and controls, joint bootstrap): ratio "
                        f"{dv['ratio_pop']:.2f} [{dv['ratio_pop_lo']:.2f}, {dv['ratio_pop_hi']:.2f}], "
                        f"P(ratio <= 1) = {dv['p_one_ratio_pop_le1']:.3f}: ratio > 1 marginal, 1.5x not met; F is "
                        "associated with NAME in the population (OR "
                        f"{dv['OR_name_pop']:.2f} [{dv['OR_name_pop_lo']:.2f}, {dv['OR_name_pop_hi']:.2f}])"),
        verdict_inputs=dv)

    # ---------------- H3e
    ev = sg["verdict_inputs_H3e"]
    H3e = dict(
        id="H3e", statement="Exploratory, bounded: U* = (p_F0,post - p_pre) / (p_F1,post - p_pre) in a pooled-slot "
                            "analysis; 'second-hand diffusion' is claimed only if U* > 0.8, otherwise unresolved.",
        estimates=dict(primary=pick(sg["ustar"], post="2024-25", baseline="2022-23"),
                       table=[{k: r(v_, 4) if isinstance(v_, float) else v_ for k, v_ in x.items()}
                              for x in sg["ustar"]]),
        verdict="not_supported", verdict_detail=("second-hand diffusion claimed" if ev["claim_secondhand_diffusion"]
                                                 else "unresolved (U* <= 0.8): no second-hand-diffusion claim"),
        verdict_inputs=ev)

    # ---------------- Holm over the confirmatory family
    pv = {"H3a": H3a["p_one_sided"], "H3b": H3b["p_one_sided"], "H3c": H3c["p_one_sided"],
          "H3d": max(H3d["p_one_sided"], 1 / (S[0].get("n_boot", 1000) + 1))}
    adj = holm(pv)
    for h in (H3a, H3b, H3c, H3d):
        h["p_holm"] = r(adj[h["id"]], 6)
    # sensitivity family: H3d with the population comparator; H3b excluded (descriptive, R26 selected in-sample)
    pv_s = {"H3a": pv["H3a"], "H3c": pv["H3c"],
            "H3d": max(H3d["p_one_sided_population_comparator"], 1 / (S[0].get("n_boot", 1000) + 1))}
    adj_s = holm(pv_s)
    for h in (H3a, H3c, H3d):
        h["p_holm_sensitivity"] = r(adj_s[h["id"]], 6)
    H3b["p_holm_sensitivity"] = None
    code = {p.name: D3.sha(p) for p in sorted(SRC.glob("d3_*.py"))}
    res = dict(
        work_package="WP7 / D3 The machine register", plan="research/titles/docs/PLAN.md D3",
        code_sha256=code, lexicons_sha256=inv["lexicons_json_sha256"],
        slot_inventory=inv["inventory"], slot_variants_dropped=inv["dropped"],
        sample_note=("All estimates use the discovery split, on which the PLAN pilots were computed. The verdicts are "
                     "discovery-sample replications of pre-specified rules, not confirmations; confirmation rests on "
                     "held-out CT4 (H3a), CT7 (H3c) and CT8 (H3b)."),
        heldout_projected_power=power,
        holm=dict(family="H3a-H3d (pre-specified discovery family); H3e exploratory", raw_p=pv, adjusted_p=adj,
                  sensitivity=dict(family="H3a, H3c, H3d (population NAME comparator); H3b excluded as descriptive",
                                   raw_p=pv_s, adjusted_p=adj_s)),
        thesis_line_D3=("In meaning-fixed title slots, LLM-favoured verb openers rose from 2024 (pooled OR "
                        f"{sp['OR']:.1f} [{sp['OR_lo']:.1f}, {sp['OR_hi']:.1f}]; accelerating from 2024, not sharply "
                        "dated against 2023; carried mainly by the improve slot; an addition of new openers rather than "
                        "a swap of synonyms) while control pairs stayed flat at the 2024 break. Fingerprinted "
                        "abstracts go with the LLM-favoured slot variant somewhat more than with NAME titles ("
                        f"{dv['ratio_pop']:.2f}x [{dv['ratio_pop_lo']:.2f}, {dv['ratio_pop_hi']:.2f}] against the "
                        "population NAME comparator), so the lexical-over-structural margin is small. The 2026 fall "
                        "of R24 is shared by its neutral synonyms, so no register turnover is identified. (Replaces the "
                        "PLAN section 1 bullet 'LLM-favoured verbs jump at 2024 (pooled OR ~ 2.7) ... Their register "
                        "turns over in step with the model generation'; PLAN.md is locked and was not edited.)"),
        hypotheses=[H3a, H3b, H3c, H3d, H3e],
        figures=["fig_F3_1_slot_shares", "fig_F3_2_register_heatmap", "fig_F3_3_vintage_forest", "fig_F3_4_signature",
                 "fig_S3_1_secondhand"],
        tables=["T3_1_slot_models.csv", "T3_1_slot_models.md"],
        deviations=[
            "Slot inventory frozen after V2: exploit/unlocking, exploit/enabling and reveal/decoding dropped (V2 sense "
            "precision < 0.85); a dropped word makes the slot 'not filled'. Borderline words (unleashing, harnessing, "
            "boosting) kept and tested by leave-one-variant-out and the unweighted-rule inventory.",
            "Primary opener rule = PLAN text (opener after an optional NAME lead), not the pilot's any-colon-lead rule; "
            "the any-lead rule is a robustness row (n = 2,163, OR 2.49), and the truly pilot-like row (any-lead rule + "
            "full lexicon, n = 2,321, OR 2.80) shows that the two analyst choices together lower the OR to 2.18 "
            "(n = 1,922) from the pilot-like 2.80.",
            "H3a randomization inference over break years and a year-level REML meta-regression (group-year shocks) "
            "were added (study convention, PLAN section 0); an event study of year deviations from slot trends "
            "(estimated jointly with the 2023-26 dummies; and, in the fixer pass, frozen on 2018-22 with a bootstrap) "
            "was added after the break scan showed a comparable stacked OR at 2023.",
            "H3b: primary_area does not exist before 2024, so 2023 areas were imputed with a classifier on bge "
            "abstract embeddings trained on 2025 labels; 2023 enters only the heat map and the 2023-26 Poisson "
            "model, never the 2025-vs-2026 test. Large areas follow the pilot rule (>= 500 titles in 2025+2026).",
            "H3b is tested on the R24/R26 family rates (titles with any family word); the pilot numbers in the PLAN "
            "were for single words (enhanc*, unified). Single-word results are reported as robustness.",
            "H3c uses the frozen v2 lexicons (RARE21 scout list; R24 stems), which differ from the vintage pilot's "
            "19-term regex and -ing forms; the pilot lexicons are rerun as a reconciliation row.",
            "H3d: LPM coefficients are converted to implied ORs at the F = 0 mean of each outcome; logit and "
            "conditional-logit ORs are reported as robustness. The NAME OR is estimated on the same slot-filled "
            "papers (PLAN: 'two LPMs on the same papers'); the population NAME OR is also reported.",
            "H3e: post = 2024-25 and p_pre = 2022-23 fixed before estimation (pilot baseline); pooled over slots with "
            "common post weights. F1 contamination correction U*(1 - c) added as a sensitivity.",
            "Adversarial-pass additions (not in the PLAN): control-pair leave-one-out rows (controls without via/using, "
            "novel/new, towards/toward) and event-study rows for controls without via; the stacked contrast without "
            "via/using is 1.41 [0.74, 2.68] under the PLAN level-shift model but 6.39 [1.68, 24.3] in 2024 under the "
            "event study with jointly estimated slot trends (the frozen-trend version is unstable for towards/novel).",
            "Camera-ready audit: pairs from cache/arxiv_audit.jsonl plus the first ENLARGE_N = 1,620 lines of the "
            "append-only enlargement file (pinned at the fixer pass for reproducibility); reported as counts with "
            "exact Clopper-Pearson intervals, no bootstrap CI.",
            "Fixer pass (audit/d3): H3d adds the population NAME comparator (all papers of the same years/subset, "
            "same topic100 x year FE, same controls, joint topic100-cluster bootstrap) as co-primary, a collider "
            "diagnostic, D1's fingerprint F_d1, a pre-LLM 2018-23 row and a + log authors row; H3e skips empty "
            "bootstrap cells and adds no-study_adj and topic100-cluster-bootstrap sensitivities; H3c adds the "
            "shared-lemma-free co-primary, an F26 x 2026 arm, pre-LLM placebos, genre (N24) and meaning-fixed "
            "benchmarks and F26 components; H3b adds the neutral-synonym benchmark, within-slot shares, a word-churn "
            "benchmark and a taxonomy-reassigned 2024->2025 context; H3a adds a frozen-trend event study (bootstrap "
            "CIs), per-1k variant rates and a truly pilot-like row (any-lead + full lexicon)."],
    )
    D3.write_json(res, OUTDIR / "results.json")
    print(json.dumps({h["id"]: (h["verdict"], h.get("p_holm")) for h in res["hypotheses"]}, indent=1))
    print("holm", adj)


if __name__ == "__main__":
    main()
