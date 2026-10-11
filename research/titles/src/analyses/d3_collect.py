"""WP7 / D3: collect the four D3 result files into outputs/d3_register/results.json (machine-readable estimates,
verdicts against the PLAN falsification criteria, Holm over the confirmatory family H3a-H3d, robustness checks,
deviations). Verdicts are mechanical; RESULTS.md gives the interpretation.

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
            event_study_vs_2018_22_trend=sl["event_study"],
            placebo_pre_only=sl["placebo_pre_only"]),
        per_slot=[{k: (r(x[k], 4) if isinstance(x[k], float) else x[k]) for k in
                   ("slot", "label", "estimator", "n", "n_pre", "n_post", "share_pre", "share_post", "OR", "OR_lo",
                    "OR_hi", "pp", "pp_lo", "pp_hi", "p_one", "q_BH_one_sided") if k in x} for x in sl["per_slot"]],
        robustness=h3a_rob, leave_one_variant_out=sl["loo_summary"],
        camera_ready_audit=sl["audit"],
        p_one_sided=v["p_H3a_intersection_union"],
        p_note="intersection-union: max of the one-sided p for pooled post > 0 and stacked interaction > 0",
        verdict=h3a_verdict, verdict_inputs=v)

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
            all_21_areas=rg["all21_areas"], context_2024_to_2025=rg["context_2024_to_2025"],
            large_areas=rg["large_areas"], area_imputation_2023=rg["area_imputation"]),
        p_one_sided=rv["p_H3b_intersection_union"], p_note="intersection-union: max of the two one-sided sign tests",
        verdict="falsified" if rv["falsified"] else (
            "supported" if (rv["r24_meets_prediction_ge10"] and rv["r26_meets_prediction_ge12"]) else
            "partially_supported"),
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
                       lpm_topic_x_year=vt["lpm"]),
        robustness={f"{x['outcome_family']}|{x['label']}": vrow(x["label"], x["outcome_family"]) for x in M},
        p_one_sided=vv["p_one"],
        verdict="falsified" if vv["falsified"] else ("supported" if vv["ratio_CI_excludes_1"] else
                                                     "partially_supported"),
        verdict_inputs=vv)

    # ---------------- H3d
    dv = sg["verdict_inputs_H3d"]
    S = sg["signature"]

    def srow(x):
        return {k: (r(x[k], 4) if isinstance(x[k], float) else x[k]) for k in
                ("label", "x", "n_papers", "n_slot_rows", "n_F1", "p0_slot", "p0_name", "delta_slot_pp",
                 "delta_name_pp", "OR_slot", "OR_slot_lo", "OR_slot_hi", "OR_name", "OR_name_lo", "OR_name_hi",
                 "ratio", "ratio_lo", "ratio_hi", "p_one_ratio_le1", "n_boot", "estimable") if k in x}
    H3d = dict(
        id="H3d", statement="2024-26 within topic100 x year: OR(F -> LLM slot variant | slot filled) >= 1.5 x OR(F -> "
                            "NAME) (same papers; two LPMs, seemingly-unrelated cluster bootstrap). Falsified if "
                            "OR_slot <= OR_NAME.",
        estimates=dict(primary=srow(S[0]), name_all_2024_26_population=sg["name_all_2024_26"],
                       logit_and_conditional_logit=sg["logit_signature"]),
        robustness=[srow(x) for x in S[1:]],
        p_one_sided=dv["p_one_ratio_le1"], p_note="bootstrap share of draws with OR_slot / OR_NAME <= 1 (1,000 draws)",
        verdict="falsified" if dv["falsified"] else ("supported" if dv["prediction_ratio_ge_1p5"] and
                                                     dv["ratio_lo"] > 1 else "partially_supported"),
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
    code = {p.name: D3.sha(p) for p in sorted(SRC.glob("d3_*.py"))}
    res = dict(
        work_package="WP7 / D3 The machine register", plan="research/titles/docs/PLAN.md D3",
        code_sha256=code, lexicons_sha256=inv["lexicons_json_sha256"],
        slot_inventory=inv["inventory"], slot_variants_dropped=inv["dropped"],
        holm=dict(family="H3a-H3d (confirmatory); H3e exploratory", raw_p=pv, adjusted_p=adj),
        hypotheses=[H3a, H3b, H3c, H3d, H3e],
        figures=["fig_F3_1_slot_shares", "fig_F3_2_register_heatmap", "fig_F3_3_vintage_forest", "fig_F3_4_signature",
                 "fig_S3_1_secondhand"],
        tables=["T3_1_slot_models.csv", "T3_1_slot_models.md"],
        deviations=[
            "Slot inventory frozen after V2: exploit/unlocking, exploit/enabling and reveal/decoding dropped (V2 sense "
            "precision < 0.85); a dropped word makes the slot 'not filled'. Borderline words (unleashing, harnessing, "
            "boosting) kept and tested by leave-one-variant-out and the unweighted-rule inventory.",
            "Primary opener rule = PLAN text (opener after an optional NAME lead), not the pilot's any-colon-lead rule; "
            "the pilot-like rule is a robustness row. Hence n = 1,922 slot titles (2018+) vs the pilot's 2,362.",
            "H3a randomization inference over break years and a year-level REML meta-regression (group-year shocks) "
            "were added (study convention, PLAN section 0); an event study of year deviations from 2018-22 slot "
            "trends was added after the break scan showed a comparable stacked OR at 2023.",
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
            "event study with 2018-22 trends.",
            "Camera-ready audit: pairs from cache/arxiv_audit.jsonl plus the enlargement file as present at run "
            "time (the enlargement job is still running; the line count is frozen in slots_results.json)."],
    )
    D3.write_json(res, OUTDIR / "results.json")
    print(json.dumps({h["id"]: (h["verdict"], h.get("p_holm")) for h in res["hypotheses"]}, indent=1))
    print("holm", adj)


if __name__ == "__main__":
    main()
