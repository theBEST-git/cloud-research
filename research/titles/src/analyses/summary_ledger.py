"""Integration pass: one consolidated ledger of every pre-registered hypothesis -> outputs/SUMMARY.{json,md}.

Reads only finished outputs (run after every direction, WP4, the prereg dry run and figures.py):
    outputs/d1_break/results.json, outputs/d2_carriers/results.json, outputs/d3_register/results.json,
    outputs/d4_filter/results.json, outputs/snapshot/results.json (+ interim_254/results.json),
    outputs/prereg/{dryrun.json, bundle.sha256, frozen/params.json}, outputs/validation/validation.json,
    outputs/tables/table1_hypotheses.csv (estimate strings and final verdict wording, so the ledger and Table 1
    cannot drift apart).
The pre-audit verdicts and the 'what changed' notes are transcribed from each direction's fix log
(outputs/audit/<dir>/fix_log.md) and RESULTS.md 'Audit response'; every number is read from the outputs.
Integration pass 2: verdict_code is normalised to a fixed vocabulary (VERDICT_VOCAB; the direction's own code is kept
in verdict_code_upstream and the reviewed wording in verdict), CT readings cover every audit-qualified test, and the
'Consistency fixes' section records the second integration pass.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.summary_ledger
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT


def rj(rel: str) -> dict:
    return json.loads((OUT / rel).read_text())


def hyp(d: dict, hid: str) -> dict:
    H = d["hypotheses"]
    return H[hid] if isinstance(H, dict) else next(h for h in H if h.get("id") == hid)


def r(x, k=3):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), k)


def ci3(d) -> str:
    return f"{d['est']:.3f} [{d['lo95']:.3f}, {d['hi95']:.3f}]"


def est(e, lo=None, hi=None, scale="", k=3):
    return dict(est=r(e, k), lo=r(lo, k), hi=r(hi, k), scale=scale)


# ------------------------------------------------------------------------------------------------
# Pre-audit verdicts and audit changes (transcribed from the fix logs; see module docstring)
# ------------------------------------------------------------------------------------------------
AUDIT = {
    "H1a": ("partially supported", "Year-level random-effects inference made primary (Holm p 0.0006 -> 0.071); "
            "smooth-vs-break comparison added. 'Dated 2024 break' replaced by 'convex acceleration from about "
            "2022-24, most visible in 2026'. Verdict label unchanged."),
    "H1b": ("falsified", "Calibration bug fixed (test rows now scored by the fold models that set the intercept): R1 "
            "rolling share 0.620 -> 0.574. Verdict moved from 'falsified' to 'not falsified, prediction fails'; "
            "year-FE and slope-recalibration sensitivities give a range of 0.37-0.65."),
    "H1c": ("supported", "Paper bootstrap held year shocks fixed; two-stage year-level inference made primary "
            "(diff CI [0.03, 2.71] pp, Holm 0.067). Verdict moved to 'not established at the year level'."),
    "H1d": ("supported", "Fixed 2-year new-key lookback; evaluated per year: 2025 share 0.316 > 0.30. Verdict "
            "moved to 'partially supported'."),
    "H1e": ("supported", "Tool share corrected for fingerprint misclassification and year-matched (3.1% -> 7.1%); "
            "'bounded from above' withdrawn. Integration pass: the D3 positive control with D1's fingerprint is not "
            "significant (slot OR 1.29 [0.92, 1.81]), so the tool estimate is not validated by a positive control "
            "on its own fingerprint."),
    "H2a": ("supported", "Shared-outcome generational null added (rho_last 0.88-0.93 under a purely generational "
            "world). Verdict moved to 'not identified'; 'same keys / same people' wording withdrawn."),
    "H2b": ("supported", "Newcomer-premium and within-key contrasts added; symmetric-lookback ratio 0.86 [0.72, "
            "1.01]. Verdict qualified: 'magnitude not robust'."),
    "H2c": ("partially supported", "Two-way (key, paper) SEs; fixed-base all-prior definition gives -0.07 "
            "[-0.42, 0.24]; 41% of rolling all-prior teams contain an entrant key. Verdict moved to 'not supported "
            "(not falsified)'."),
    "H2d": ("supported", "Random-subset slope ~1.00 and null slope ~0.78 show the slope criterion cannot "
            "discriminate; the style-vs-topic contrast survives (drop-both variant, equal-weight medians)."),
    "H2e": ("supported", "Both outcomes required (IUT p 0.061, Holm 0.122); email-era null 0.69-0.76. Verdict "
            "moved to 'inconclusive'; 'general mode' withdrawn."),
    "S2.1": ("supported", "Content-fixed drift benchmarks added (topic-adjusted -4.8 pp, p 0.057; same-key -3.4 pp, "
             "p 0.33). The lag behind drift is not established; NAME is still not added on net."),
    "S2.2": ("supported", "Verdict requires the positive control (llm_topic) to be detected in the same "
             "specification; it is not. Verdict moved to 'inconclusive'; 'fits homophily' removed."),
    "H3a": ("supported", "Pilot-like row (2.80) and frozen-trend event study added; OR >= 2 shown to depend on "
            "'enhancing' (1.72 without it); addition-not-substitution rates added; camera-ready audit pinned "
            "(rejected arm unauditable). Label unchanged, qualified. Integration pass 2: the slot audit was a "
            "pre-freeze pin (1,620 enlargement lines); it now reads WP4's final freeze (2,004 lines; 1,317 pairs, "
            "LLM-slot v1 titles 23 accepted / 5 rejected, still unauditable)."),
    "H3b": ("supported", "Neutral-synonym benchmark (R24 vs N24 1.08 [0.86, 1.36]) and word-churn benchmark (R26 in "
            "the top 3.6% of words, selected in-sample). Verdict moved to 'thresholds met (descriptive); register "
            "turnover not identified'."),
    "H3c": ("supported", "Shared-lemma-free co-primary (1.32 [1.04, 1.66], OR_F24 1.00); pre-LLM placebo and genre "
            "benchmarks. Verdict moved to 'prediction met; vintage reading not established'."),
    "H3d": ("supported", "Same-paper comparator shown to be collider-conditioned (selection factor 0.79); population "
            "NAME comparator co-primary: ratio 1.24 [0.99, 1.57]. Verdict moved to 'partially supported'. "
            "Integration pass: Figure 4c now shows only the population comparator."),
    "H3e": ("unresolved", "Empty bootstrap cells skipped (CI unchanged); no-study-adj 0.61 [0.47, 0.76]. Unchanged."),
    "H4a": ("supported", "D4 fixer: qualified ('review-stage neutrality not identified', selection-only interval "
            "crossed 0.90 on the 331-pair audit). Integration pass: on WP4's complete audit the selection-only "
            "interval is 0.948-1.033 and the editing-corrected 90% CI 0.949-1.031, so the equivalence is robust to "
            "camera-ready editing; a small decision-stage premium remains unidentified."),
    "H4b": ("supported", "Holm over H4a-H4d (H4b 0.059); L depletion shown to be R24-driven and pre-2024; O "
            "depletion sits at the unidentified decision stage. Verdict moved to 'partially supported'. Integration "
            "pass 2: the new 3-4% pre-decision depletion of F24 and the abstract style density is stated beside the "
            "R24 genre penalty."),
    "H4c": ("partially supported", "IUT p 0.209 for the >= 15% magnitude; post hoc pre-ChatGPT baseline meets the "
            "falsification condition. Integration pass: abstract-editing DiD on the complete audit +0.71 pp "
            "(was +3.55 on 330 pairs)."),
    "H4d": ("supported", "Topic100-FE contrast co-primary (cross +0.84 [-1.05, 2.74]); 'between authors' removed. "
            "Verdict moved to 'partially supported'."),
    "H4e": ("supported", "OR statistics compared on the effect scale: ITS break ratio 0.50, colon trend 0.89; M "
            "11/11 -> 9/11. Verdict moved to 'partially supported (descriptive)'."),
}

VERDICT_VOCAB = {
    "supported": "the pre-registered rule is met (the reviewed wording may add qualifiers)",
    "partially_supported": "some pre-registered criteria are met, or the rule is met only with a material qualification",
    "not_identified": "the pre-registered statistic is met, but an alternative explanation meets it too, so the "
                      "substantive reading is not identified",
    "not_established": "positive point estimate, but the inference required for the claim fails",
    "not_supported": "the rule is not met and the falsification condition is not met either",
    "inconclusive": "the design cannot discriminate (e.g. the required positive control is not detected)",
    "unresolved": "exploratory; the pre-set claim threshold is not reached, which is not a rejection",
    "falsified": "the pre-registered falsification condition is met",
}
# direction codes (snake_case or free text, as stored upstream) -> VERDICT_VOCAB; a code not listed fails loudly
NORMALISE = {
    "supported": "supported", "partially_supported": "partially_supported", "partially supported": "partially_supported",
    "not_supported": "not_supported", "not supported": "not_supported", "falsified": "falsified",
    "not_established_year_level": "not_established", "not identified": "not_identified",
    "inconclusive": "inconclusive", "unresolved": "unresolved",
    "supported on the pre-registered groups; magnitude not robust": "supported",
    "supported (channel contrast); slope criterion not diagnostic": "supported",
    "NAME not added on net; lag behind content-fixed drift not established": "supported",
    "thresholds met (descriptive); register turnover not identified": "not_identified",
    "prediction met; vintage reading not established": "not_identified",
}


def norm_code(hid: str, code) -> str:
    c = str(code).strip()
    if c not in NORMALISE:
        raise KeyError(f"summary_ledger: upstream verdict code {c!r} for {hid} has no entry in NORMALISE")
    return NORMALISE[c]


WP4_CHANGE = {
    "SB1": "Complete audit (803/508 pairs): DiD +1.48 [-0.63, 3.59] vs D* 2.92; still not identified.",
    "SB2": "Multiplicity-controlled gate adopted: 0 of 18 auditable features pass (uncorrected rule would pass "
           "compound and O-union w/o ALL-CAPS). Interim '0 of 24' held only by accident of the 254-record freeze.",
    "SB3": "'using' and R24 became auditable as the audit grew; R26, LLM slot words and typography remain "
           "unauditable. Interim 'supported' -> 'partially supported'.",
    "SB4": "Pooled sample bounds the NAME effect on findability near 1 (OR 1.00 [0.81, 1.22]).",
    "SB5": "Camera-ready retitling excess (+6/+10 pp) withdrawn: +1.5 [-3.2, 6.1]; -2.7 pp where v1 was posted "
           "during review.",
    "V7a": "Both routes share an abstract-similarity rule; near-miss bound 0.33 -> 0.25 added.",
    "V7b": "Unchanged label; route-B-only pairs move the NAME DiD by 0.20 pp.",
    "G1": "Upgraded from 'partially supported' to 'supported' on the complete audit (corrected 90% CI "
          "[0.949, 1.031]).",
    "G2": "L-title audited as R24 or R26 (channel rule); not identified (Holm 0.33).",
    "G2b": "New: O-union audited without ALL-CAPS; not identified (Holm 0.12).",
    "G3": "Abstract audit pooled with the enlargement's v1 abstracts; not identified.",
    "G4": "Magnitude fell from +3.55 to +0.71 pp; 'LLM-assisted polishing' sentence withdrawn.",
    "G4_sens": "2023-26 pairs: +0.73 pp.",
}


def main():
    t1 = pd.read_csv(OUT / "tables" / "table1_hypotheses.csv")
    t1 = t1.set_index("ID")
    r1, r2, r3, r4 = (rj("d1_break/results.json"), rj("d2_carriers/results.json"), rj("d3_register/results.json"),
                      rj("d4_filter/results.json"))
    rs, rsi = rj("snapshot/results.json"), rj("snapshot/interim_254/results.json")
    dry = rj("prereg/dryrun.json")
    params = rj("prereg/frozen/params.json")
    bundle_text = (OUT / "prereg" / "bundle.sha256").read_text()
    bundle_hash = hashlib.sha256(bundle_text.encode()).hexdigest()
    val = rj("validation/validation.json")

    am = hyp(r3, "H3a")["camera_ready_audit"]
    fl = {(x["period"], x["decision"]): x for x in am["flips"]}
    assert (am["meta"]["n_enlarge_lines_used"], am["meta"]["n_usable_pairs"], fl[("all", "accepted")]["n_llm_v1"],
            fl[("all", "rejected")]["n_llm_v1"]) == (2004, 1317, 23, 5), "H3a audit note is stale (AUDIT['H3a'])"

    # ---------------- numeric primary estimates (one per hypothesis)
    a, c, dd, e = r1["H1a"], r1["H1c"], r1["H1d"], r1["H1e"]
    h2 = {k: hyp(r2, k)["estimate"] for k in ("H2a", "H2b", "H2c", "H2d", "H2e")}
    H3 = {k: hyp(r3, k) for k in ("H3a", "H3b", "H3c", "H3d", "H3e")}
    H4 = r4["hypotheses"]
    tc = e["tool_share_0.39_corrected_2026"]
    pc = H3["H3d"]["estimates"]["population_comparator"]
    s1, s2 = r2["supporting"]["S2_1"], r2["supporting"]["S2_2"]["primary"]["name_primary"]
    num = {
        "H1a": est(*a["year_level_U"]["OR"], scale="slope-change OR/yr, year level (U)"),
        "H1b": est(r1["H1b"]["shares"]["R1|rolling"]["share"], *r1["H1b"]["shares"]["R1|rolling"]["ci"],
                   scale="R1 rolling content share of 2024-26 steps"),
        "H1c": est(100 * c["diff"], *(100 * np.array(c["year_level_two_stage"]["diff_ci"])),
                   scale="pp/yr, mean u 2024-26 minus 2019-23 (two-stage year-level CI)"),
        "H1d": est(dd["dfl_full_by_year"]["2025"]["share"], *dd["dfl_full_by_year"]["2025"]["ci"],
                   scale="DFL composition share, 2025 (the year that fails; 2024 0.287, 2026 0.261)"),
        "H1e": est(tc["share"], tc["lo"], tc["hi"], scale="corrected tool share at A = 0.39 (2026 delta)"),
        "H2a": est(h2["H2a"]["rho_last"]["est"], h2["H2a"]["rho_last"]["lo"], h2["H2a"]["rho_last"]["hi"],
                   scale="rho_last (generational null 0.88-0.93)"),
        "H2b": est(h2["H2b"]["first_minus_last"]["est"], h2["H2b"]["first_minus_last"]["lo"],
                   h2["H2b"]["first_minus_last"]["hi"], scale="rho_first - rho_last"),
        "H2c": est(h2["H2c"]["ratio_i"]["est"], h2["H2c"]["ratio_i"]["lo"], h2["H2c"]["ratio_i"]["hi"],
                   scale="change at share_new = 0 / population change"),
        "H2d": est(h2["H2d"]["G_style"]["est"] - h2["H2d"]["G_topic"]["est"], None, None,
                   scale=f"G_style - G_topic (G_style {h2['H2d']['G_style']['est']:.3f}, G_topic "
                         f"{h2['H2d']['G_topic']['est']:.3f})"),
        "H2e": est(h2["H2e"]["name_any"]["est"], h2["H2e"]["name_any"]["lo"], h2["H2e"]["name_any"]["hi"],
                   scale="rho_NAME, email-key era 2018->20"),
        "S2.1": est(s1["mean_dNAME"], s1["mean_dNAME"] - 1.96 * s1["se"], s1["mean_dNAME"] + 1.96 * s1["se"],
                    scale="mean within-pair change in NAME (n = 297 retitled resubmissions)"),
        "S2.2": est(s2["past_minus_future"], s2["past_minus_future"] - 1.96 * s2["se_diff"],
                    s2["past_minus_future"] + 1.96 * s2["se_diff"], scale="past - future exposure coefficient"),
        "H3a": est(H3["H3a"]["estimates"]["pooled_slots_post"]["OR"], H3["H3a"]["estimates"]["pooled_slots_post"]["lo"],
                   H3["H3a"]["estimates"]["pooled_slots_post"]["hi"], scale="pooled slot post OR"),
        "H3b": est(H3["H3b"]["estimates"]["neutral_synonym_benchmark"]["all|R24_vs_N24_ratio_of_RR"]["ratio"],
                   H3["H3b"]["estimates"]["neutral_synonym_benchmark"]["all|R24_vs_N24_ratio_of_RR"]["lo"],
                   H3["H3b"]["estimates"]["neutral_synonym_benchmark"]["all|R24_vs_N24_ratio_of_RR"]["hi"],
                   scale="R24 vs neutral synonyms, ratio of within-area RRs 2026/2025 (signs: R24 down 14/16, "
                         "R26 up 16/16)"),
        "H3c": est(H3["H3c"]["estimates"]["primary"]["ratio"], *H3["H3c"]["estimates"]["primary"]["ratio_ci"],
                   scale="OR(F24->R24)/OR(F26->R24)"),
        "H3d": est(pc["ratio"], *pc["ratio_ci"], scale="OR_slot / OR_NAME, population comparator"),
        "H3e": est(H3["H3e"]["estimates"]["primary"]["U_star"], H3["H3e"]["estimates"]["primary"]["U_lo"],
                   H3["H3e"]["estimates"]["primary"]["U_hi"], scale="U*"),
        "H4a": est(H4["H4a"]["estimates"]["tost"]["est"], H4["H4a"]["estimates"]["tost"]["lo90"],
                   H4["H4a"]["estimates"]["tost"]["hi90"], scale="pooled 2024-26 NAME G_total (90% CI)"),
        "H4b": est(H4["H4b"]["estimates"]["L_union_total"]["est"], H4["H4b"]["estimates"]["L_union_total"]["lo95"],
                   H4["H4b"]["estimates"]["L_union_total"]["hi95"], scale="L-union G_total"),
        "H4c": est(H4["H4c"]["estimates"]["ratio_acc_all"]["2024"]["ratio"],
                   H4["H4c"]["estimates"]["ratio_acc_all"]["2024"]["lo95"],
                   H4["H4c"]["estimates"]["ratio_acc_all"]["2024"]["hi95"],
                   scale="accepted/all Kobak bound ratio, 2024 (2025 0.714, 2026 0.502)"),
        "H4d": est(H4["H4d"]["estimates"]["topic100_FE"]["cross"], H4["H4d"]["estimates"]["topic100_FE"]["cross_lo95"],
                   H4["H4d"]["estimates"]["topic100_FE"]["cross_hi95"],
                   scale="pp, withdrawal excess of NAME papers with topic100 FE (pre-registered spec +4.06)"),
        "H4e": est(None, scale=f"M {H4['H4e']['estimates']['M_within_10pct']} within +/-10%"),
    }
    holm_src = {"H1a": a["holm_adjusted_p"], "H1b": r1["H1b"]["holm_adjusted_p"], "H1c": c["holm_adjusted_p"],
                "H1d": dd["holm_adjusted_p"], "H1e": e["holm_adjusted_p"],
                **{k: hyp(r2, k)["p_holm"] for k in ("H2a", "H2b", "H2c", "H2d", "H2e")},
                **{k: H3[k].get("p_holm") for k in ("H3a", "H3b", "H3c")},
                "H3d": H3["H3d"]["p_holm_sensitivity"],
                **{k: H4[k].get("p_holm") for k in ("H4a", "H4b", "H4c", "H4d")}}
    codes = {"H1a": a["verdict"], "H1b": r1["H1b"]["verdict"], "H1c": c["verdict"], "H1d": dd["verdict"],
             "H1e": e["verdict"], **{k: hyp(r2, k)["verdict"] for k in ("H2a", "H2b", "H2c", "H2d", "H2e")},
             "S2.1": r2["supporting"]["S2_1"]["verdict"], "S2.2": r2["supporting"]["S2_2"]["verdict"],
             **{k: H3[k]["verdict"] for k in ("H3a", "H3b", "H3c", "H3d", "H3e")},
             **{k: H4[k]["verdict"] for k in ("H4a", "H4b", "H4c", "H4d", "H4e")}}
    dirn = {"1": "D1 naming acceleration", "2": "D2 carriers (declared profile keys)", "3": "D3 machine register",
            "4": "D4 gatekeeper"}
    ledger = []
    for hid in ["H1a", "H1b", "H1c", "H1d", "H1e", "H2a", "H2b", "H2c", "H2d", "H2e", "S2.1", "S2.2",
                "H3a", "H3b", "H3c", "H3d", "H3e", "H4a", "H4b", "H4c", "H4d", "H4e"]:
        row = t1.loc[hid]
        fam = ("supporting test (exploratory)" if hid.startswith("S") else "exploratory" if hid == "H3e" else
               "descriptive" if hid == "H4e" else "discovery confirmatory family (Holm within direction)")
        ledger.append(dict(
            id=hid, direction=dirn[hid[1]], family=fam, prediction=row["Prediction"],
            primary_estimate=num[hid], estimate=row["Estimate (95% CI)"],
            holm_p=r(holm_src.get(hid), 6), holm_p_note=("sensitivity family, population comparator" if hid == "H3d"
                                                         else None),
            verdict=row["Final verdict (post-audit)"], verdict_code=norm_code(hid, codes[hid]),
            verdict_code_upstream=str(codes[hid]),
            verdict_before_audit=AUDIT[hid][0], what_changed_in_audit=AUDIT[hid][1]))

    # ---------------- WP4 gates
    interim = {h["id"]: h["verdict"] for h in rsi["hypotheses"]}
    gates = [dict(id=h["id"], claim=h["statement"], estimate=h["estimate"], verdict=h["verdict"],
                  verdict_interim_254=interim.get(h["id"]), what_changed=WP4_CHANGE.get(h["id"], ""))
             for h in rs["hypotheses"]]

    # ---------------- prereg dry run
    H4b_e = H4["H4b"]["estimates"]
    H4b_c, H4b_pre = H4b_e["components"], H4b_e["components_pre_2018_23"]
    rob3 = pd.read_csv(OUT / "d3_register" / "slot_robustness.csv")
    nv_ = rob3[rob3["label"].str.startswith("controls without via/using")
               & (rob3["model"] == "stacked_interaction")].iloc[0]
    le_ = H3["H3a"]["estimates"]["leave_out_enhancing"]["slots_post"]
    h2b_w = hyp(r2, "H2b")["estimate"]["entrant_minus_stayer_L_first_within_lastkey_size_topic"]
    h2b_s = hyp(r2, "H2b")["estimate"]["symmetric_lookback_prior_first_ratio"]
    old = {"CT1": "not confirmed", "CT2": "not confirmed", "CT3": "confirmed", "CT4": "confirmed",
           "CT5": "confirmed", "CT6": "not confirmed", "CT7": "confirmed", "CT8": "confirmed", "CT9": "confirmed",
           "CT10": "confirmed", "CT11": "not confirmed", "CT12": "confirmed"}   # revision-1 dryrun.json
    reading = {
        "CT3": "A confirmed CT3 would confirm the statistic, not communal change: the generational null gives "
               "rho_last 0.88-0.93 > 0.5 (H2a not identified).",
        "CT7": "Carried by F26 papers avoiding R24; without shared lemmas OR(F24) = 1.00. Not a vintage-alignment test "
               "on its own.",
        "CT8": "Neutral synonyms fell alike (R24 vs N24 1.08 [0.86, 1.36]); R26 selected in-sample. A shift in word "
               "families, not register turnover.",
        "CT9": "Little power by construction; positive control fails on this fingerprint.",
        "CT10": "Gate now fails: identification p 0.041 (Holm family {CT10}) > 0.025 and the editing-corrected upper "
                "bound 0.918 > 0.90. Passed under the revision-1 uncorrected rule.",
        "CT6": (f"L-union unauditable through arXiv (typography, em dash); can never be 'confirmed'. A G < 1, including "
                f"the audit-free G_desk x G_exit, would mainly re-detect the pre-2024 R24 depletion (R24 total "
                f"{H4b_c['R24']['total']['est']:.3f} vs {H4b_pre['R24']['total']['est']:.3f} in 2018-23); LLM-specific "
                f"selection needs the L-union without R24 ({H4b_e['L_noR24']['total']['est']:.3f}) or the post/pre "
                f"ratio."),
        "CT1": (f"Discovery OR 1.098 is below the pre-registered minimal effect 1.10. The p-value uses paper-level SEs; "
                f"D1's year-level REML p is {a['p_one_sided_year_level']:.3f} (Holm {a['holm_adjusted_p']:.3f}), so a "
                f"confirmed CT1 should be reported with the year-level test."),
        "CT2": (f"Content-share upper bound 0.66 > 0.60 already in discovery; underpowered (projected z ~ 1). "
                f"Within-year resampling holds year shocks fixed, so a confirmed CT2 would not establish year-level "
                f"acceleration (D1 two-stage: [{100 * c['year_level_two_stage']['diff_ci'][0]:.2f}, "
                f"{100 * c['year_level_two_stage']['diff_ci'][1]:.2f}] pp, Holm {c['holm_adjusted_p']:.3f})."),
        "CT4": (f"Confirms the stacked statistic on the pre-registered 2024 spec; the control contrast leans on "
                f"via/using ({nv_.OR:.2f} [{nv_.OR_lo:.2f}, {nv_.OR_hi:.2f}] without it) and OR >= 2 on 'enhancing' "
                f"(slots {le_['OR']:.2f} [{le_['OR_lo']:.2f}, {le_['OR_hi']:.2f}] without it); controls shift at the "
                f"other candidate break years; not sharply dated against 2023."),
        "CT11": "No pair equivalent within +/-0.1 in discovery; ACC-pair gate fails (b_max 0.092).",
        "CT12": (f"Confirms the D2-group contrast, which mixes cohort and tenure (within-last-key entrant-first gap "
                 f"{100 * h2b_w['est']:.1f} pp [{100 * h2b_w['lo']:.1f}, {100 * h2b_w['hi']:.1f}]; symmetric-lookback ratio "
                 f"{h2b_s['ratio_prior']:.2f} [{h2b_s['ratio_prior_lo']:.2f}, {h2b_s['ratio_prior_hi']:.2f}]); not a role "
                 f"effect."),
    }
    ct = []
    for s_ in dry["summary"]:
        g = dry["results"][s_["id"]]["gate"]
        ct.append(dict(id=s_["id"], title=s_["title"], family=s_["family"], estimate=s_["estimate"], ci=s_["ci"],
                       ci_level=s_["ci_level"], p_one_sided=s_["p_one_sided"], p_adjusted=s_["p_adjusted"],
                       gate_applies=s_["gate_applies"], gate_passes=s_["gate_passes"],
                       gate_kind=g.get("kind"), gate_p_ident_holm=g.get("p_ident_holm"),
                       verdict_as_if=s_["verdict_as_if"], reasons=s_["reasons"],
                       verdict_as_if_revision_1=old[s_["id"]], reading=reading.get(s_["id"], "")))
    rv = params.get("revision", {})
    hist = {h["revision"]: h for h in rv.get("history", [])}
    prereg = dict(revision=rv.get("revision"), bundle_hash=bundle_hash,
                  previous_bundle_hash=rv.get("previous_bundle_hash"),
                  previous_revision=rv.get("previous_revision", (rv.get("revision") or 2) - 1), reason=rv.get("reason"),
                  revision_history=[dict(revision=h["revision"], bundle_hash=h["bundle_hash"],
                                         why=h.get("reason") or h.get("gate_audit")) for h in rv.get("history", [])],
                  gate_rule=params["audit"].get("gate_rule"),
                  audit_freeze=dict(enlargement_lines=params["audit"]["state"]["enlargement"]["n_lines_used"],
                                    sha256=params["audit"]["state"]["enlargement"]["sha256_of_lines_used"],
                                    title_pairs=params["audit"]["state"]["pooled"]["n_pairs"],
                                    abstract_pairs=params["audit"]["state"]["v1_abstracts"]["n_pairs"]),
                  dry_run=ct,
                  note="Dry-run verdicts are 'as if' discovery were the held-out split; they are not confirmations. "
                       "The held-out split has not been requested or seen.")

    # ---------------- validation (PLAN section 3)
    v1 = val["V1"]
    validation = [
        dict(id="V1", check="NAME / compound / orthography / casing detectors (two blind LLM passes + adjudication)",
             result="kappa 0.948-1.000 on all labels (target 0.80); NAME precision 97.8%, recall 97.3%; precision drift "
                    "1.2 pp across eras (< 5 pp); misclassification-corrected ITS OR 1.090 vs 1.098 (within 10%)",
             verdict="pass"),
        dict(id="V2", check="Slot sense and swap preservation", result="3 variants dropped (precision < 0.85): "
             "exploit/unlocking, exploit/enabling, reveal/decoding; swap preservation 0.75-0.99", verdict="pass "
             "(inventory frozen after drops)"),
        dict(id="V3", check="Fingerprint specificity and convergent validity", result="FPR 2021-22: F24 2.9%, "
             "F26 3.2%, F_any 5.9%, typography 0.04%; LLM-polish rating Spearman 0.25 (F_any); recall unknown",
             verdict="weak convergent validity; all tool estimates are bounds or model-conditional"),
        dict(id="V4", check="Name-masking leakage", result="whole-word lead survives R3 masking in 0 of 12,928 NAME "
             "abstracts, R1 in 22 (0.17%, URL suffixes); variant spellings 0.36-0.81%", verdict="pass (R3); R1 "
             "near-pass"),
        dict(id="V5", check="Topic labels and stability", result="LLM-cluster flag vs regex kappa 0.86; MiniLM vs "
             "bge topic100 ARI 0.42", verdict="pass for the LLM flag; topic partitions only moderately stable"),
        dict(id="V6", check="Author keys", result="0 key-years > 40 papers; trailing-digit aliasing changes 24.2% of "
             "2022+ papers' new-key share (0.552 -> 0.495)", verdict="aliasing material for D2; restricted-alias "
             "sensitivity reported"),
        dict(id="V7", check="Camera-ready audit validity (WP4)", result="see gates V7a (supported) and V7b "
             "(partially supported)", verdict="see gates"),
    ]
    assert v1["kappa"] is not None

    # ---------------- robust findings and withdrawn claims
    nm = H4["H4a"]["estimates"]
    R24c = H4b_c["R24"]
    t41_ = pd.read_csv(OUT / "d4_filter" / "T4_1_continuation_ratio.csv")
    t41 = t41_[(t41_["stage"] == "exit") & (t41_["feature"] == "R24")].set_index("era")["OR"]
    tpw = pd.read_csv(OUT / "snapshot" / "T4_2_tipping_points.csv")
    tpw = tpw[tpw["period"] == "2024-26"].set_index("feature")
    sb2_unc = [k for k in tpw.index if bool(tpw.loc[k, "passes_uncorrected_dec"])]
    assert set(sb2_unc) == {"compound", "O_union_arxiv"}, f"X8 wording stale: uncorrected passes {sb2_unc}"
    assert not bool(tpw.loc["sentence_case", "passes_uncorrected_dec"])
    min_holm = float(tpw.loc[tpw["auditable"].astype(bool), "p_holm_dec"].min())
    fpath = pd.read_csv(OUT / "snapshot" / "T4_2_freeze_path.csv").set_index("enlarge_lines")
    assert all("sentence_case" in str(fpath.loc[n_, "passes_uncorrected"]) for n_ in (600, 1000, 1261)) and \
        "sentence_case" not in str(fpath.loc[2004, "passes_uncorrected"]), "X8 freeze-path wording stale"
    g1 = hyp(rs, "G1")["estimate"]
    robust = [
        dict(claim="ICLR submissions titled 'NAME: subtitle' doubled from 2023 to 2026 (20.3% -> 40.5% of 43,482 "
                   "submissions), on a trend that became convex (accelerated) from about 2022-24, most visibly in "
                   "2026.",
             evidence=f"LPM slope change +2.8 pp/yr [1.3, 4.4] (year level); camera-ready-free pool year-level OR "
                      f"{a['year_level_NA']['OR'][0]:.3f} [{a['year_level_NA']['OR'][1]:.3f}, "
                      f"{a['year_level_NA']['OR'][2]:.3f}]; misclassification-corrected ITS within 10% (V1).",
             caveat="Not a dated 2024 break; not tied to ChatGPT."),
        dict(claim="A published-only study reproduces the all-submission NAME share, and this survives correction "
                   "for camera-ready editing.",
             evidence=f"G_total {nm['tost']['est']:.3f} (90% CI {nm['tost']['lo90']:.3f}-{nm['tost']['hi90']:.3f}); "
                      f"editing-corrected {g1.split('corrected 90% CI ')[1].split(';')[0]} (complete arXiv audit).",
             caveat="A small decision-stage NAME premium (G_dec 1.05) is not identified against editing."),
        dict(claim="In meaning-fixed title-opener slots, LLM-favoured verbs ('Enhancing' over 'Improving', etc.) rose "
                   "from 2024 while control pairs did not shift at 2024, including in the camera-ready-free pool; the "
                   "new openers were added rather than swapped for neutral synonyms.",
             evidence="Pooled post OR 2.18 [1.41, 3.38]; stacked slot-vs-control 2.55 [1.53, 4.25]; NA pool 2.18 "
                      "[1.28, 3.70]; LLM-variant rate RR 3.91 [1.84, 8.29] vs neutral 1.17 [0.70, 1.94].",
             caveat="Associational; OR >= 2 depends on 'enhancing'; not sharply dated against 2023; the control "
                    "null holds at the 2024 specification only."),
        dict(claim="Title-style markers move more slowly among stayer keys than abstract-topic markers do "
                   "(style-vs-topic channel contrast).",
             evidence=f"G_style {h2['H2d']['G_style']['est']:.2f} [{h2['H2d']['G_style']['lo']:.2f}, "
                      f"{h2['H2d']['G_style']['hi']:.2f}] vs G_topic {h2['H2d']['G_topic']['est']:.2f} "
                      f"[{h2['H2d']['G_topic']['lo']:.2f}, {h2['H2d']['G_topic']['hi']:.2f}] (any position).",
             caveat="Declared profile keys, not persons; the slope criterion itself is not diagnostic."),
        dict(claim="Measured team composition (size x new keys x LLM topic) does not account for most of the "
                   "2023-26 NAME rise.",
             evidence="DFL share 0.29 / 0.32 / 0.26 (2024/25/26), far below the 0.50 falsification line; Shapley "
                      "share net of content 0.09.",
             caveat="The <= 0.30 prediction fails in 2025."),
        dict(claim="Retitled resubmissions do not add NAME on net.",
             evidence="Mean change 0.000 (se 0.025; 28 adds, 28 drops; n = 297).",
             caveat="Pairs are selected on retitling; a lag behind the population drift is not established."),
        dict(claim="No title feature's acceptance association survives the camera-ready audit under multiplicity "
                   "control.",
             evidence="0 of 18 auditable features pass the Holm gate on 1,311 pre-decision arXiv pairs; NAME DiD "
                      "+1.48 pp [-0.63, 3.59] vs tipping point 2.92 pp.",
             caveat="'Not identified' is a statement about the audit, not evidence that editing explains the "
                    "associations; ALL-CAPS, typography and the em dash cannot be audited through arXiv."),
        dict(claim="A published-only study recovers mainstream title prevalences within 10% but halves the 2024 NAME "
                   "slope change and under-represents outsider casing.",
             evidence="M 9/11 within +/-10% (effect scale); ITS break ratio 0.50 [-0.15, 1.16]; ALL-CAPS titles "
                      "0.36 [0.26, 0.47] of their all-submission share.",
             caveat="Outsider under-representation is not identified as selection (camera-ready recasing)."),
        dict(claim="Desk rejection and withdrawal deplete 'Enhancing X via Y'-type R24 title words, as they did "
                   "before 2024. The LLM-style union without R24 is neutral in total, but F24 and the abstract style "
                   "density show a new 3-4% pre-decision depletion.",
             evidence=(f"R24 pre-decision {ci3(R24c['predec'])}; camera-ready-free {ci3(R24c['predec_crf'])}; T4.1 exit "
                       f"OR {t41['2018-23']:.3f} in 2018-23 vs {t41['2024-26']:.3f} in 2024-26. L-union without R24, "
                       f"total {ci3(H4b_e['L_noR24']['total'])}. Camera-ready-free pre-decision: F24 "
                       f"{ci3(H4b_c['F24']['predec_crf'])}, style density {ci3(H4b_c['style_density']['predec_crf'])}; "
                       f"F24 post/pre {ci3(H4b_e['components_post_vs_pre']['F24']['predec_crf'])} against 2018-23 but "
                       f"{ci3(H4b_e['components_post_vs_pre_1822']['F24']['predec_crf'])} against 2018-22."),
             caveat="The F24 part is new only against a baseline that includes 2023. No decision-stage association is "
                    "identified against camera-ready editing (R24's total gain includes an unidentified decision part). "
                    "Not evidence that review detects LLM use."),
        dict(claim="The raw withdrawal excess of NAME papers is mostly topic composition.",
             evidence="+4.06 pp cross-section without topic FE; +0.84 [-1.05, 2.74] with topic100 FE.",
             caveat="Within-key, not within-person."),
        dict(claim="The camera-ready NAME audit, the findability gap and the absence of a camera-ready retitling "
                   "excess are robust measurement facts about the arXiv audit itself.",
             evidence="Found 86.5% vs 53.1% (accepted vs rejected; OR 5.68); retitling +1.5 pp [-3.2, 6.1]; NAME "
                      "does not predict findability (OR 1.00 [0.81, 1.22]).",
             caveat="Both retrieval routes share an abstract-similarity rule."),
    ]
    withdrawn = [
        dict(claim="'Dated slope break at 2024 (pilot OR 1.28/yr)'", status="not identified",
             why="Year-level CI on U includes 1 (1.096 [0.990, 1.214]); sup-LR picks 2023; null without 2026; 1.28 was "
                 "for compound titles."),
        dict(claim="'Content explains only a minority (30-45%)'", status="not established",
             why="Name-masked content explains 0.37-0.65 depending on design and calibration."),
        dict(claim="'Unexplained drift accelerated from 1.7 to 3.9 pp/yr'", status="not established",
             why="Point estimate 1.5 -> 2.9 pp/yr; two-stage year-level CI [0.03, 2.71] pp fails Holm; absent in the "
                 "NA pool and the non-LLM subset."),
        dict(claim="'Detectable LLM drafting adds little and is bounded from above'", status="not established as a bound",
             why="7% [1, 13] for the pre-registered fingerprint; 16-33% for other markers; the fingerprint fails D3's "
                 "positive control (slot OR 1.29 [0.92, 1.81])."),
        dict(claim="'The same people changed: communal change within incumbent authors'", status="not identified",
             why="A purely generational world with the observed co-authorship gives rho_last 0.88-0.93."),
        dict(claim="Newcomer-free teams rose >= 0.5x the population (H2c)", status="not supported",
             why="0.34 [0.19, 0.48] x population at zero new co-author keys."),
        dict(claim="Communal change as the general (pre-LLM) mode (H2e)", status="inconclusive",
             why="IUT p 0.061 (Holm 0.122); email-era null 0.69-0.76."),
        dict(claim="Retitled papers lag the content-fixed drift (S2.1)", status="not established",
             why="Topic-adjusted -4.8 pp (p 0.057); same-key -3.4 pp (p 0.33)."),
        dict(claim="Tie contagion falsified by the future-tie placebo (S2.2)", status="inconclusive",
             why="The positive control is not detected in the primary specification."),
        dict(claim="'LLM register turns over in step with the model generation'", status="withdrawn",
             why="R24's 2026 fall is shared by neutral synonyms (1.08 [0.86, 1.36]); R26 selected in-sample."),
        dict(claim="Title register aligns with the abstract's LLM vintage (H3c)", status="not established",
             why="Without shared lemmas OR(F24 -> R24) = 1.00; the contrast is F26 papers avoiding R24."),
        dict(claim="'Lexical, not structural' LLM signature (H3d, ratio >= 1.5)", status="weakened to marginal",
             why="Against the population NAME comparator 1.24 [0.99, 1.57]; F is associated with NAME (OR 1.14)."),
        dict(claim="Second-hand diffusion of LLM wording to non-users (H3e)", status="unresolved",
             why="U* 0.65 [0.50, 0.81] < 0.8."),
        dict(claim="'Peer review neither creates nor amplifies the naming fashion'", status="partly retained",
             why="Amplification is not supported (editing-corrected centre 0.991; equivalence holds); whether the "
                 "decision stage carries a small NAME premium is not identified."),
        dict(claim="'Review depletes LLM and outsider markers'", status="not supported as written",
             why=(f"L-union total fails Holm ({ci3(H4b_e['L_union_total'])}); its identified depletion is R24 and "
                  f"pre-dates 2024; F24 and the abstract style density show a new 3-4% pre-decision (desk and "
                  f"withdrawal) depletion (camera-ready-free {H4b_c['F24']['predec_crf']['est']:.3f} and "
                  f"{H4b_c['style_density']['predec_crf']['est']:.3f}), not an identified decision-stage effect; O "
                  f"depletion is not identified as selection except ALL-CAPS at exit.")),
        dict(claim="Published-only studies understate LLM use by >= 15%", status="not established",
             why="IUT p 0.209; the falsification condition is met under a post hoc pre-ChatGPT baseline; the prereg "
                 "CT10 gate now fails in the dry run."),
        dict(claim="The withdrawal excess of named papers is between authors (H4d)", status="withdrawn",
             why="With topic100 FE the cross-sectional excess is +0.84 [-1.05, 2.74]."),
        dict(claim="Camera-ready retitling excess among accepted papers (+6 to +10 pp)", status="withdrawn",
             why="Complete audit: +1.5 [-3.2, 6.1]; -2.7 pp where v1 was posted during review."),
        dict(claim="'Consistent with LLM-assisted camera-ready polishing' of abstracts", status="withdrawn",
             why="Abstract-editing DiD fell from +3.55 to +0.71 pp [-1.95, 3.36]."),
        dict(claim="Acceptance associations of compound titles, sentence case or outsider casing", status="not identified",
             why=(f"Compound and outsider casing without ALL-CAPS pass only the uncorrected rule; sentence case "
                  f"passed it only at interim freezes (600-1,261 enlargement lines), not on the complete audit; all "
                  f"have Holm p >= {min_holm:.2f}.")),
    ]
    integration = [
        "figures.py: Figure 4c shows the population NAME comparator (ratio 1.24 [0.99, 1.57]) and D1's fingerprint; "
        "the collider-conditioned same-paper comparator is dropped. Figure 4b adds the neutral synonyms of R24. "
        "Figures 5-6 and Tables 1 and 4 updated to the final D4/WP4 outputs (complete audit, Holm gate, effect-scale "
        "atlas); Table 1 shows final post-audit verdicts and fails loudly if an upstream verdict changes.",
        "D1: positive control from D3 wired into d1_summary (results.json -> H1e.positive_control_D3) and RESULTS.md "
        "§5; H1e wording adjusted.",
        "D4: d4_bias_atlas builds its flip tables on WP4's complete frozen audit (1,311 pairs) with WP4's rule and "
        "CI (asserted equal to WP4); d4_collect reads WP4's Holm gate; RESULTS.md audit-dependent numbers updated; "
        "H4a strengthened (robust to camera-ready editing).",
        "WP4: the RESULTS.md section on audit consumers now records that D4 and the prereg are aligned.",
        f"prereg: revision 2 re-froze the gate audit on WP4's complete audit (2,004 lines) and adopted the Holm "
        f"gate; dry run re-run (every test statistic unchanged; CT10 now 'not confirmed (gate)'); bundle hash "
        f"{hist.get(2, {}).get('bundle_hash', '?')} (revision 1: {hist.get(1, {}).get('bundle_hash', '?')}); "
        f"superseded by revision 3 in the second integration pass (section 9).",
    ]
    consistency = [
        "Robust finding 9 and the withdrawn row 'Review depletes LLM and outsider markers' now agree with D4: desk "
        "rejection and withdrawal deplete R24 title words as before 2024 (stated on pre-decision gains, not the total, "
        "whose decision part is not identified), the L-union without R24 is neutral in total, and F24 and the abstract "
        "style density show a new 3-4% pre-decision depletion (X1).",
        "D4's suggested thesis line no longer calls the decision stage 'neutral for LLM markers' and gives the Kobak "
        "understatement as point estimates (>= 15% not established in any year); D4's summary bullets and auto-generated "
        "H4b verdict state the F24 / style-density depletion (X2).",
        "D3's camera-ready slot audit read a 1,620-line pre-freeze pin; it now reads WP4's final 2,004-line freeze "
        "(SHA-256 checked): 1,317 pairs, LLM-slot v1 titles 23 accepted / 5 rejected, still unauditable. WP4 §8 lists D3 "
        "as a consumer; H3a 'what changed' updated (X3).",
        "F_any is defined in full (F24 with >= 1 RARE21 word ∪ F26 ∪ title typography; F_d1 differs only in the >= 2-word "
        "threshold) in D1, D3, d1_summary and the Fig. 4 caption (X4).",
        "Reading notes added for CT1 and CT2 (paper-level inference that D1's audit demoted; year-level p 0.035 / Holm "
        "0.071 and two-stage CI [0.03, 2.71]) and for CT4, CT6 and CT12, in prereg.md and in section 3 here; decision "
        "rules unchanged (X5, X6).",
        "README: d1_summary must run after D3 (it reads D3 for the positive control); D3's camera-ready slot audit "
        "and D4's d4_bias_atlas need step 4 and the archived arXiv caches; d3_slots now fails with a clear message "
        "when the caches are missing (X7).",
        "The compound / sentence-case / outsider-casing row uses the complete audit: only compound and the O-union "
        "without ALL-CAPS pass the uncorrected rule; sentence case passed it only at interim freezes (X8).",
        "D3 results.json stores H3e's verdict code as 'unresolved'; SUMMARY.json verdict_code uses a fixed vocabulary "
        "(verdict_vocabulary), with the direction's code in verdict_code_upstream (X9).",
        "Table 4 shows '— (channel)' instead of net-flip DiDs for channel-unauditable features, labels D* as the G_dec "
        "tipping point and notes F24's G_total tipping point (-0.67 pp, as in Fig. 6b and WP4) (X10).",
        "Atlas prevalence ratios reuse the stage-gain bootstrap, so their CIs equal D4's G_total CIs (e.g. L-union "
        "[0.951, 1.001], O-union [0.749, 0.870], R24 [0.740, 0.874]); D4 H4e and Fig. 6a updated (X11).",
        "Table 2 labels the accepted and rejected pool rows 2017-26; Table 1 (H4a) and Fig. 5 label D4's pool breaks "
        "'ITS 2018-26' (X12).",
        "D1 §5 (iii) adds the false-positive-baseline sensitivity: the 2021-22 rate (3.2%) gives a corrected tool share "
        "of 7.4% [1.4, 13.4] (7.1% with the 2023 rate; 7.0% with non-accepted 2023 papers) (X13).",
        "Fig. 3a's reference row is relabelled: it is the ratio to the paper-level change (1.00), not rho_last (0.995) "
        "(X14).",
        "V4 uses one denominator, 22 of 12,928 NAME abstracts of 2018-26; D1's 12,962 includes the 34 NAME papers of "
        "2017, not placeholder rows (X15).",
        "The D3 positive-control wording is generated from the computed significance flag in d1_summary, the Fig. 2 and "
        "Fig. 4 captions and the prereg CT9 note (X16).",
        "Person-language for declared keys removed from D2 RESULTS and VALIDATION V6 (X17).",
        "'Discovery split'; D4's R1 and I9 audit rows marked as original-audit values; D4's T4.2 bullet points to WP4's "
        "sub-union gates G2 and G2b; the Fig. 6 caption counts the beyond-PLAN atlas rows and states the full gate "
        "rule (X18).",
        "Audit trail: the first integration pass's pre-change copies are in "
        "outputs/audit/integration/pre_fix_backup/pass1/, this pass's in pass2/; README §9 lists the required-code "
        "rule (X19).",
        f"Pre-registration revision 3 (required code changed: prereg_confirm.py, d3_slots.py, d4_bias_atlas.py; no "
        f"held-out data requested): bundle hash {bundle_hash}, superseding {rv.get('previous_bundle_hash')}; frozen "
        f"parameters byte-identical except params.json and rules.json; dry run re-run with every statistic unchanged; "
        f"verify ok.",
    ]
    out = dict(
        study="Research fashion in ICLR titles (with abstracts), 2017-2026",
        generated=_dt.datetime.now().isoformat(timespec="seconds"), script="src/analyses/summary_ledger.py",
        data=dict(n_universe=43482, years="2017-2026", split="discovery split (~80%); the held-out confirmation split "
                  "has not been requested", pools="all submissions incl. rejected, withdrawn and desk-rejected"),
        language=("Associational throughout; declared profile keys are not persons; list position is a partition "
                  "label, not seniority; acceptance associations are subject to the camera-ready caveat; nothing is "
                  "attributed causally to ChatGPT or any tool."),
        ledger=ledger, wp4_gates=gates, prereg=prereg, validation=validation, robust_findings=robust,
        withdrawn_or_not_identified=withdrawn, integration_changes=integration,
        consistency_fixes_integration_pass_2=consistency, verdict_vocabulary=VERDICT_VOCAB)
    (OUT / "SUMMARY.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    write_md(out)
    print(f"wrote {OUT / 'SUMMARY.json'} and SUMMARY.md: {len(ledger)} hypotheses, {len(gates)} gates, "
          f"{len(ct)} CTs; bundle {bundle_hash[:16]}")


def _ci(d):
    if d.get("est") is None:
        return d.get("scale", "")
    if d.get("lo") is None:
        return f"{d['est']:.3f} ({d['scale']})"
    return f"{d['est']:.3f} [{d['lo']:.3f}, {d['hi']:.3f}] ({d['scale']})"


def _p(x):
    return "—" if x is None else ("<0.001" if x < 0.001 else f"{x:.3f}")


def _fmt(x):
    if isinstance(x, dict):
        return "; ".join(f"{k} {_fmt(v)}" for k, v in x.items())
    if isinstance(x, (list, tuple)):
        return "[" + ", ".join(_fmt(v) for v in x) + "]"
    if isinstance(x, float):
        return f"{x:.3f}"
    return str(x)


def write_md(o: dict):
    L = []
    A = L.append
    p = o["prereg"]
    A("# Consolidated results ledger: research fashion in ICLR titles, 2017–2026")
    A("")
    A(f"Generated by `{o['script']}` on {o['generated'][:10]} from the final, audited outputs of D1–D4, the camera-"
      "ready audit (WP4), the measurement validation and the pre-registration dry run. Machine-readable version: "
      "`outputs/SUMMARY.json`.")
    A("")
    A(f"- **Data.** {o['data']['n_universe']:,} ICLR submissions, {o['data']['years']}, {o['data']['pools']}. "
      f"All estimates use the {o['data']['split']}.")
    A(f"- **Language.** {o['language']}")
    A(f"- **Pre-registration.** Revision {p['revision']}, bundle hash `{p['bundle_hash']}` (supersedes "
      f"`{p['previous_bundle_hash']}`; see the prereg section below). No held-out data have been requested or seen.")
    A("- **Verdicts on the discovery split are replications of pre-specified rules, not confirmations.**")
    A("")
    A("## 1. Hypothesis ledger")
    A("")
    A("Final estimate (primary statistic, 95% CI unless stated), Holm-adjusted one-sided p within the direction's "
      "family, final verdict after the three audits, the verdict before the audits, and what the audits changed.")
    A("")
    A("| ID | Prediction | Final estimate | Holm p | Final verdict | Before audit | What changed |")
    A("|---|---|---|---|---|---|---|")
    for h in o["ledger"]:
        A(f"| {h['id']} | {h['prediction']} | {h['estimate']} | {_p(h['holm_p'])}"
          f"{' (pop.)' if h['holm_p_note'] else ''} | **{h['verdict']}** | {h['verdict_before_audit']} | "
          f"{h['what_changed_in_audit']} |")
    A("")
    A("## 2. Camera-ready audit claims and gates (WP4)")
    A("")
    A("Complete frozen audit: original 616-paper audit + all 2,000 enlargement records (2,004 lines), 1,311 "
      "pre-decision arXiv pairs (803 accepted / 508 rejected), 2023–26. Gate: auditable (count and arXiv channel), "
      "editing-corrected 95% CI excludes 1, Holm-adjusted identification p < 0.025.")
    A("")
    A("| ID | Claim | Estimate | Verdict | Interim (254 records) | What changed |")
    A("|---|---|---|---|---|---|")
    for g in o["wp4_gates"]:
        claim = g["claim"] if len(g["claim"]) < 220 else g["claim"][:217] + "…"
        estt = g["estimate"] if len(g["estimate"]) < 260 else g["estimate"][:257] + "…"
        A(f"| {g['id']} | {claim} | {estt} | **{g['verdict'].replace('_', ' ')}** | "
          f"{(g['verdict_interim_254'] or 'n/a').replace('_', ' ')} | {g['what_changed']} |")
    A("")
    A(f"## 3. Pre-registered held-out tests: discovery dry run (revision {p['revision']})")
    A("")
    A(f"- Bundle hash (SHA-256 of `outputs/prereg/bundle.sha256`): `{p['bundle_hash']}`.")
    earlier = [h for h in p.get("revision_history", []) if h["bundle_hash"] != p["previous_bundle_hash"]]
    A(f"- Previous (revision {p['previous_revision']}) hash: `{p['previous_bundle_hash']}`"
      + "".join(f"; revision {h['revision']}: `{h['bundle_hash']}`" for h in earlier) + ".")
    A(f"- Why it changed: {p['reason']}")
    A(f"- Gate audit: {p['audit_freeze']['enlargement_lines']:,} enlargement lines (SHA-256 "
      f"`{p['audit_freeze']['sha256'][:16]}…`), {p['audit_freeze']['title_pairs']:,} title pairs, "
      f"{p['audit_freeze']['abstract_pairs']:,} abstract pairs (2024–26).")
    A(f"- {p['note']}")
    A("")
    A(f"| Test | Estimate | CI | p (one-sided) | p adjusted | Gate | Verdict as if (rev. {p['revision']}) | Rev. 1 | "
      "Reading |")
    A("|---|---|---|---|---|---|---|---|---|")
    for c in p["dry_run"]:
        gate = "n/a" if not c["gate_applies"] else ("pass" if c["gate_passes"] else "fail")
        A(f"| {c['id']} {c['title']} | {_fmt(c['estimate'])} | {_fmt(c['ci'])} ({int(100 * c['ci_level'])}%) | "
          f"{_p(c['p_one_sided'])} | {_p(c['p_adjusted'])} | {gate} | **{c['verdict_as_if']}**"
          f"{' (' + '; '.join(c['reasons']) + ')' if c['reasons'] else ''} | {c['verdict_as_if_revision_1']} | "
          f"{c['reading']} |")
    A("")
    A("## 4. Measurement validation (PLAN §3)")
    A("")
    A("| ID | Check | Result | Verdict |")
    A("|---|---|---|---|")
    for v in o["validation"]:
        A(f"| {v['id']} | {v['check']} | {v['result']} | {v['verdict']} |")
    A("")
    A("## 5. Robust findings (survived every audit)")
    A("")
    for i, f in enumerate(o["robust_findings"], 1):
        A(f"{i}. **{f['claim']}** {f['evidence']} *Caveat:* {f['caveat']}")
    A("")
    A("## 6. Claims withdrawn or not identified")
    A("")
    A("| Claim | Status | Why |")
    A("|---|---|---|")
    for w in o["withdrawn_or_not_identified"]:
        A(f"| {w['claim']} | **{w['status']}** | {w['why']} |")
    A("")
    A("## 7. What the first integration pass changed")
    A("")
    for x in o["integration_changes"]:
        A(f"- {x}")
    A("")
    A("## 8. Where to look")
    A("")
    A("- Direction reports: `outputs/d1_break/RESULTS.md`, `outputs/d2_carriers/RESULTS.md`, "
      "`outputs/d3_register/RESULTS.md`, `outputs/d4_filter/RESULTS.md`, `outputs/snapshot/RESULTS.md`, "
      "`outputs/validation/VALIDATION.md`; each ends with an 'Audit response' section.")
    A("- Fix logs: `outputs/audit/<direction>/fix_log.md`; integration log: `outputs/audit/integration/fix_log.md`.")
    A("- Pre-registration: `outputs/prereg/prereg.md`, `dryrun.json`, `bundle.sha256`.")
    A("- Paper figures and tables: `outputs/figures/` (captions in `manifest.json`), `outputs/tables/`.")
    A("")
    A("## 9. Consistency fixes (second integration pass)")
    A("")
    A("A cross-direction check found 19 issues (X1-X19); each was re-checked and fixed. Details, commands and checks: "
      "`outputs/audit/integration/fix_log.md`. No verdict changed; H3e's stored code now matches its 'unresolved' wording.")
    A("")
    for x in o["consistency_fixes_integration_pass_2"]:
        A(f"- {x}")
    (OUT / "SUMMARY.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
