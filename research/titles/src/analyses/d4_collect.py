"""WP8 / D4: collect the three D4 result files into outputs/d4_filter/results.json (machine-readable estimates and
verdicts for H4a-H4e, the decision-stage bound, robustness checks and exploratory analyses) and write the
T4.1 / T4.2 markdown tables. Verdicts apply the PLAN D4 falsification criteria mechanically; RESULTS.md gives the
interpretation.

Run (after d4_stage_gains, d4_bias_atlas, d4_exit_composition):
    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d4_collect
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from analyses import d4_stage_gains as S

OUTDIR = S.OUTDIR
SRC = Path(__file__).resolve().parent


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def r3(x, k=3):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), k)


def md_table(df: pd.DataFrame, floatfmt: dict | None = None) -> str:
    floatfmt = floatfmt or {}
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                cells.append("" if not np.isfinite(v) else format(v, floatfmt.get(c, ".3f")))
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def main():
    sg = json.loads((OUTDIR / "stage_gains.json").read_text())
    ba = json.loads((OUTDIR / "bias_atlas.json").read_text())
    ex = json.loads((OUTDIR / "exit_composition.json").read_text())
    gains = pd.read_csv(OUTDIR / "gains.csv")

    def G(feature, gain, period="2024-26", variant="primary", pooling="std"):
        r = gains[(gains.variant == variant) & (gains.feature == feature) & (gains.gain == gain)
                  & (gains.period == period) & (gains.pooling == pooling)]
        if not len(r):
            return None
        r = r.iloc[0]
        return {k: r3(r[k], 4) for k in ["est", "lo95", "hi95", "lo90", "hi90", "p_ge1", "p_le1"]}

    # ---------------- H4a
    a = sg["H4a"]
    its = a["its_equality"]
    h4a = dict(
        statement="Neutral filter for the mainstream fashion: NAME G_total in [0.95, 1.10] every year 2018-26; pooled "
                  "2024-26 TOST within [0.90, 1.11]; 2024 slope-change OR equal across ACC, REJ, WD.",
        estimates=dict(
            name_total_by_year={y: {k: r3(v[k], 4) for k in ["est", "lo95", "hi95"]}
                                for y, v in a["name_total_by_year"].items()},
            all_years_in_band=a["all_years_in_band"],
            pooled_2024_26_std=G("NAME", "total"), pooled_2024_26_raw=G("NAME", "total", pooling="raw"),
            pooled_2024_25_std=G("NAME", "total", "2024-25"), pooled_2018_23_std=G("NAME", "total", "2018-23"),
            stage_gains_2024_26={g: G("NAME", g) for g in ["desk", "exit", "dec", "predec", "predec_crf"]},
            tost=a["tost_0p90_1p11"],
            its_pools={r["pool"]: dict(OR=r3(r["slope_change_OR"]), lo=r3(r["slope_change_OR_lo"]),
                                       hi=r3(r["slope_change_OR_hi"]), nobs=r["nobs"]) for r in a["its_pools"]},
            its_wald=dict(chi2=r3(its["wald_chi2"]), df=its["df"], p=r3(its["p"]), max_abs_dlogOR=r3(its["max_abs_dlogOR"]),
                          pairs=[{k: (r3(v, 4) if isinstance(v, float) else v) for k, v in p.items()}
                                 for p in its["pairs"]]),
        ),
        falsification="pooled NAME G_total 90% CI outside [0.90, 1.11], or pool-specific break ORs differ at p < .05",
        falsified=a["falsified"],
        verdict="supported",
        notes=("All nine yearly NAME total gains lie in [0.95, 1.10]; the pooled 90% CI [1.001, 1.041] is inside the "
               "equivalence margins; the Wald test does not reject equal pool breaks (p = 0.51) and the largest point "
               "difference is 0.061 on the log-OR scale, but no pairwise difference is TOST-equivalent at +/-0.1 "
               "(pairwise 90% CIs extend from -0.17 to +0.12): equality is not rejected rather than demonstrated. The pre-decision stages "
               "deplete NAME slightly (desk x exit 0.972) and the decision stage enriches it (1.050), but the decision "
               "gain is not identified against camera-ready edits (T4.2)."),
    )
    # ---------------- H4b
    b = sg["H4b"]
    h4b = dict(
        statement="Depletion of LLM and outsider markers: pooled 2024-26 G_total < 1 for the L-union and O-union; "
                  "G_desk x G_exit < 1 for the L-union.",
        estimates=dict(
            L_union_total=G("L_union", "total"), O_union_total=G("O_union", "total"),
            L_union_predec=G("L_union", "predec"), L_union_predec_camera_ready_free=G("L_union", "predec_crf"),
            L_union_total_raw_pooling=G("L_union", "total", pooling="raw"),
            L_union_by_year_total={y: G("L_union", "total", y) for y in ["2024", "2025", "2026"]},
            L_union_by_year_predec={y: G("L_union", "predec", y) for y in ["2024", "2025", "2026"]},
            L_union_pre_2018_23_total=G("L_union", "total", "2018-23"),
            L_union_post_vs_pre={g: G("L_union", g, "2024-26 / 2018-23", "post_vs_pre")
                                 for g in ["total", "predec", "dec", "predec_crf"]},
            L_title_total=G("L_title", "total"), L_abstract_total=G("L_abstract", "total"),
            O_union_stage={g: G("O_union", g) for g in ["desk", "exit", "dec", "predec", "predec_crf"]},
            components_total={k: G(k, "total") for k in ["title_typo", "R24", "R26", "F24", "F26", "emdash",
                                                          "style_density", "all_caps_title", "sentence_case",
                                                          "question_opener"]},
            components_predec={k: G(k, "predec") for k in ["title_typo", "R24", "R26", "F24", "F26", "emdash",
                                                            "style_density", "all_caps_title", "sentence_case",
                                                            "question_opener"]},
        ),
        falsification="L-union G_total >= 1",
        falsified=b["falsified"],
        verdict="supported",
        notes=("L-union total 0.975 (95% CI 0.951-1.001; one-sided bootstrap p = 0.030) and pre-decision 0.982 "
               "(0.972-0.992); O-union total 0.807 (0.749-0.870). Depletion of L is small in absolute terms and "
               "is carried by title R24 words (0.807) and abstract style density (0.965); abstract markers as a union "
               "are near-neutral (0.993). Relative to the pre-LLM years, when the same markers were enriched among "
               "accepted papers (L-union total 1.154), the post-2024 total gain is 15% lower (ratio 0.845, 0.783-0.915). "
               "O depletion sits at the decision stage (0.812), which camera-ready edits can produce and the audit "
               "cannot bound (ALL-CAPS and sentence case unauditable); only ALL-CAPS is also depleted at exit (0.839)."),
    )
    # ---------------- H4c
    c = ba["H4c"]
    kb = pd.read_csv(OUTDIR / "kobak_bounds.csv")
    sens = kb[(kb.set == "ratio_acc_all") & kb.marker.isin(["F24", "F24_2", "L_abstract"])]
    h4c = dict(
        statement="Accepted-only Kobak-style lower bound on LLM-styled abstracts understates the all-submission bound "
                  "by >= 15% relative in each of 2024-26.",
        estimates=dict(
            bounds_pp={k: {kk: r3(100 * vv, 2) for kk, vv in v.items()} for k, v in c["bounds"].items()},
            ratio_acc_all={y: {k: r3(v, 3) for k, v in d.items()} for y, d in c["ratio_acc_all"].items()},
            sensitivity_ratios=[dict(marker=r.marker, baseline=r.baseline, year=r.year, ratio=r3(r.bound),
                                     lo95=r3(r.lo95), hi95=r3(r.hi95)) for r in sens.itertuples()],
        ),
        falsification="accepted-only bound >= 0.9 x all-submission bound in 2024 and 2025",
        falsified=c["falsified"],
        verdict="partially_supported",
        notes=("Pre-registered baseline: ratios 0.80 / 0.71 / 0.50 (2024/25/26), all <= 0.85, not falsified; "
               "accepted bound 12.8 / 8.7 / 3.0 pp vs all 16.0 / 12.2 / 6.0 pp. But the gap comes mostly from the "
               "accepted pool's higher and rising 2021-23 baseline (2.95 -> 3.54 -> 4.30% vs 3.35 -> 2.49 -> 3.12%), "
               "not from lower 2024-26 prevalence (2024: 17.8% vs 19.1%). With a post hoc baseline that excludes "
               "2023 (whose camera-ready abstracts post-date ChatGPT), the F24 ratios are 0.90 / 0.90 / 0.99, i.e. on "
               "the falsification boundary; the >= 2-word variant (F24_2) stays below 0.86 in 2024-25. The plan's "
               "direction argument (camera-ready polishing can only raise accepted rates) does not cover the "
               "baseline years, where it works against it."),
    )
    # ---------------- H4d
    d = ex["H4d"]
    p = d["primary"]
    h4d = dict(
        statement="Within NA (withdrawn vs rejected), NAME coefficient > 0 in the cross-section, <= 0 within "
                  "last-position key, and the two differ.",
        estimates=dict(
            cross_pp=dict(est=r3(p["cross_pp"], 2), se=r3(p["cross_se_pp"], 2), lo95=r3(p["cross_lo95_pp"], 2),
                          hi95=r3(p["cross_hi95_pp"], 2)),
            within_pp=dict(est=r3(p["within_pp"], 2), se=r3(p["within_se_pp"], 2), lo95=r3(p["within_lo95_pp"], 2),
                           hi95=r3(p["within_hi95_pp"], 2)),
            diff_pp=dict(est=r3(p["diff_pp"], 2), se=r3(p["diff_se_pp"], 2), p_one_sided=p["diff_p_one_sided"],
                         key_bootstrap_lo95=r3(d["key_bootstrap"]["diff_pp_lo95"], 2),
                         key_bootstrap_hi95=r3(d["key_bootstrap"]["diff_pp_hi95"], 2)),
            full_sample_cross_pp=dict(est=r3(p["full_cross_pp"], 2), se=r3(p["full_cross_se_pp"], 2),
                                      nobs=p["full_nobs"]),
            nobs=p["nobs"], n_keys=p["n_keys"], n_keys_with_variation=p["n_keys_with_variation"],
            robustness={r["spec"]: dict(cross=r3(r["cross_pp"], 2), cross_se=r3(r["cross_se_pp"], 2),
                                        within=r3(r["within_pp"], 2), within_se=r3(r["within_se_pp"], 2),
                                        diff=r3(r["diff_pp"], 2), diff_se=r3(r["diff_se_pp"], 2), nobs=r["nobs"])
                        for r in d["robustness"]},
        ),
        falsification="within-author coefficient >= cross-sectional coefficient",
        falsified=d["falsified"],
        verdict="supported",
        notes=("Cross-section +4.06 pp (se 0.96) vs within last-position key -0.70 pp (se 1.08); difference 4.77 pp "
               "(se 0.75; key-cluster bootstrap 3.21-6.24). The within estimate is <= 0 at the point but its CI "
               "reaches +1.4 pp. All robustness variants keep within < cross; adding topic100 FE shrinks the "
               "cross-section to +0.84 pp (so part of the excess is topic composition) and the difference to 2.59 pp "
               "(se 0.71). In 2018-23 the within estimate is +4.2 pp (se 2.8), so the pattern is a 2024-26 result."),
    )
    # ---------------- H4e
    e = ba["H4e"]
    atlas = pd.read_csv(OUTDIR / "atlas.csv")
    h4e = dict(
        statement="Accepted-only estimates fall within +/-10% of all-submission estimates for M metrics; deviations "
                  "concentrate in O and L; each gap split into selection (desk, exit exact) and editing (audit).",
        estimates=dict(
            M_within_10pct=f"{e['M_within']}/{e['M_n']}", M_ci90_within_10pct=f"{e['M_ci90_within']}/{e['M_n']}",
            by_class=e["by_class"], peaks=e["peaks"],
            atlas=[dict(statistic=r.label, cls=r.cls, all=r3(r.T_s0, 4), published=r3(r.T_s3, 4),
                        ratio=r3(r.ratio), lo95=r3(r.ratio_lo95), hi95=r3(r.ratio_hi95),
                        within_10pct=None if pd.isna(r.within_10pct) else bool(r.within_10pct),
                        log_desk=r3(r.log_desk, 4), log_exit=r3(r.log_exit, 4), log_dec=r3(r.log_dec, 4),
                        log_edit=r3(r.log_edit, 4), log_edit_lo=r3(r.log_edit_lo, 4), log_edit_hi=r3(r.log_edit_hi, 4))
                   for r in atlas.itertuples()],
        ),
        falsification="none pre-registered (descriptive)",
        falsified=None,
        verdict="supported",
        notes=("11/11 ratio-type M statistics lie within +/-10% (median |log ratio| 0.018); O 1/4 (median 0.160); "
               "L 7/9 (median 0.037; outliers R24 prevalence 0.81 and the Kobak bound 0.72). All M point estimates are "
               "inside +/-10%; two M 90% CIs cross the margin (snowclone share 0.91, 90% CI 0.77-1.04; ITS "
               "slope-change OR ratio 0.95, 0.90-1.01). Editing is separable only for auditable title features and is "
               "not bounded by the 331-pair audit (e.g. NAME editing log-ratio +0.042, interval -0.047 to +0.148)."),
    )
    # ---------------- decision-stage bound
    bound = pd.read_csv(OUTDIR / "T4_2_decision_bound.csv")
    flips = pd.read_csv(OUTDIR / "T4_2_audit_flips.csv")
    dec_bound = dict(
        source="computed by d4_bias_atlas from cache/arxiv_audit.jsonl; outputs/snapshot/ (WP4) was not available",
        n_pairs=ba["meta"]["n_pairs"], pairs_by_decision=ba["meta"]["pairs_by_decision"],
        NAME=dict(bound[bound.feature == "NAME"].iloc[0].to_dict()),
        identified_G_dec=bound[bound.G_dec_identified].feature.tolist(),
        identified_G_total=bound[bound.G_total_identified].feature.tolist(),
        unauditable=bound[~bound.auditable].feature.tolist(),
        gate="No title-feature acceptance gain is identified: every tipping point lies inside the audit DiD 95% CI.",
    )
    # ---------------- robustness
    rob = dict(
        H4a_pooling_raw=G("NAME", "total", pooling="raw"),
        H4a_drop_wd_post=G("NAME", "total", variant="drop_wd_post"),
        H4a_wd_rejected_in_s2=G("NAME", "total", variant="wd_rejected_in_s2"),
        H4a_excl_2026=G("NAME", "total", "2024-25"),
        H4a_its_no_controls=sg["H4a"]["its_robustness"]["no_controls"]["test"],
        H4a_its_acc_rej_2017_26=sg["H4a"]["its_robustness"]["acc_rej_2017_2026"]["test"],
        H4a_its_compound=sg["H4a"]["its_robustness"]["compound_outcome"]["test"],
        H4b_L_union_drop_wd_post=G("L_union", "total", variant="drop_wd_post"),
        H4b_L_union_wd_rejected_in_s2=G("L_union", "total", variant="wd_rejected_in_s2"),
        H4b_L_union_raw_pooling=G("L_union", "total", pooling="raw"),
        H4b_L_union_excl_2026=G("L_union", "total", "2024-25"),
        H4b_O_union_drop_wd_post=G("O_union", "total", variant="drop_wd_post"),
        H4b_secondary_markers={k: G(k, "total") for k in ["F24_2", "allcaps_name", "title_emdash", "NAME_strict",
                                                          "NAME_loose"]},
        T4_1_adjusted_total=sg["T4_1_adjusted_total"],
        audit_variants=flips[flips.feature.isin(["NAME", "compound", "mixed_case_name", "O_union"])][
            ["spec", "feature", "n_acc", "n_rej", "did", "did_se", "did_boot_lo95", "did_boot_hi95"]].to_dict(
            orient="records"),
    )
    expl = dict(
        exit_timing_2025_26=ex["exit_timing"], calendar_validation=ex["calendar"],
        desk_rejection_timing_2026=ex["desk_timing_2026"],
    )
    deviations = [
        "Pooled gains are year-standardised (each year's stage prevalence weighted by its s0 size); raw pooling is "
        "reported as robustness. PLAN does not specify the pooling.",
        "OTHER rows (71 in 2018 with unknown decision) are dropped from the D4 stage frame.",
        "ALL-CAPS title = casing class all_caps (whole title in capitals); the scout stage pilot used the NAME "
        "lead orthography; that variant is reported as allcaps_name.",
        "L-union = any binary L marker (title typography, R24, R26, F24, F26, abstract em dash); the continuous "
        "style density is reported separately and is not in the union. Em dash = abstract em dash (title em dash "
        "reported as secondary).",
        "Year-specific style density re-implements the scout rule on the frozen scout style pool "
        "(analyses/d4_lexicon.json); selected words 123/150/223 for 2024/25/26.",
        "Decision-stage tipping point accounts for accepted papers inside s2: D* = (P3 - P2)/(1 - a2). The plan's "
        "1.8 pp pilot ignored the (1 - a2) factor; with it NAME's tipping point is 2.9 pp (total-gain tipping point "
        "1.0 pp).",
        "Snapshot module computed inside d4_bias_atlas from cache/arxiv_audit.jsonl (WP4 outputs absent). Only "
        "titles are auditable (no v1 abstracts cached); auditable = feature present in >= 10 accepted v1 and stored "
        "titles (pre-stated).",
        "Colon premium: no accepted-only version exists; the published-only analogue is decided-only (ACC vs REJ).",
        "Opener-entropy and JSD intervals use a random-selection band (pivot) instead of the paper bootstrap, which "
        "produced intervals excluding the point estimate (duplicates bias the unrarefied accepted set).",
        "H4c: post hoc baseline sensitivity max(2021, 2022) added because ICLR 2023 camera-ready abstracts post-date "
        "ChatGPT.",
        "H4d: primary population REJ u WD (2024-26), outcome = withdrawn incl. 2026 post-decision withdrawals; last "
        "position = max list position (D2 convention); controls year FE, log authors, llm_topic.",
        "Early vs late 2026 desk rejections not testable: all 737 desk-rejection timestamps fall on/after the "
        "decision date (bulk update).",
        "Desk-stage continuation-ratio logits fitted for 2024-26 only (2018-23 has 0-19 desk rejections a year).",
    ]
    files = sorted(str(p) for p in OUTDIR.iterdir() if p.is_file())
    results = dict(
        work_package="WP8 / D4 The gatekeeper", plan="research/titles/docs/PLAN.md D4",
        code={f: sha(SRC / f) for f in ["d4_stage_gains.py", "d4_bias_atlas.py", "d4_exit_composition.py",
                                        "d4_collect.py", "d4_lexicon.json"]},
        lexicon_v2_sha256=sha(SRC / "lexicons.json"),
        meta=dict(stage_gains=sg["meta"], bias_atlas=ba["meta"]),
        hypotheses=dict(H4a=h4a, H4b=h4b, H4c=h4c, H4d=h4d, H4e=h4e),
        decision_stage_bound=dec_bound, robustness=rob, exploratory=expl, deviations=deviations, files=files,
        language="Associational; declared profile keys are not persons; list positions are partition labels.",
    )
    S.write_json(results, OUTDIR / "results.json")

    # ---------------- markdown tables
    cr = pd.read_csv(OUTDIR / "T4_1_continuation_ratio.csv")
    t1 = cr[["era", "stage", "feature", "nobs", "OR", "OR_lo", "OR_hi", "p", "G_raw", "G_adj", "G_adj_lo",
             "G_adj_hi"]].copy()
    (OUTDIR / "T4_1_continuation_ratio.md").write_text(
        "# T4.1 Continuation-ratio logits for passing each stage\n\n"
        "Logit of passing the stage on the feature, with year x area FE (2024-26) or year FE (2018-23), log authors, "
        "llm_topic and topic100 FE; SEs clustered by topic100; FE cells without outcome variation dropped. "
        "style_density OR is per SD. G_adj = RR_att / (s RR_att + 1 - s).\n\n" + md_table(t1) + "\n")
    t2 = bound[["feature", "auditable", "P_s2", "P_s3", "G_dec_obs", "did_pp", "did_lo95_pp", "did_hi95_pp",
                "tip_dec_pp", "G_dec_interval_lo", "G_dec_interval_hi", "G_dec_identified", "G_total_obs",
                "tip_total_pp", "G_total_identified"]]
    f1 = flips[flips.spec == "primary"][["feature", "n_acc", "v1_present_acc", "adds_acc", "drops_acc", "n_rej",
                                         "v1_present_rej", "adds_rej", "drops_rej", "net_acc", "net_rej", "did",
                                         "did_se", "auditable"]]
    (OUTDIR / "T4_2_audit.md").write_text(
        "# T4.2 Camera-ready audit: flip matrices and decision-stage tipping points\n\n"
        f"{ba['meta']['n_pairs']} arXiv pairs with a pre-decision v1 ({ba['meta']['pairs_by_decision']}). "
        "adds = absent in v1, present in the stored title; drops = the reverse; net = (adds - drops)/n.\n\n"
        "## Flip matrices (primary, all audit years)\n\n" + md_table(f1, {"net_acc": ".4f", "net_rej": ".4f",
                                                                          "did": ".4f", "did_se": ".4f"}) +
        "\n\n## Decision-stage bound (2024-26, year-standardised prevalences; DiD in pp)\n\n" + md_table(t2) + "\n")
    print(json.dumps({k: v["verdict"] for k, v in results["hypotheses"].items()}))


if __name__ == "__main__":
    main()
