"""WP8 / D4: collect the three D4 result files into outputs/d4_filter/results.json (machine-readable estimates and
verdicts for H4a-H4e, the decision-stage bound, robustness checks and exploratory analyses), write the T4.1 / T4.2
markdown tables and the auto-generated summary table (summary_table.md, spliced into RESULTS.md between the
AUTO:SUMMARY markers).

Verdicts are COMPUTED from the stored estimates (audit fix D4-7 / R25), with these rules:
  * Holm (PLAN section 0) over the D4 confirmatory family {H4a, H4b, H4c, H4d}; H4e is descriptive. Each hypothesis
    enters with one p-value: H4a = TOST bootstrap p of the pooled NAME G_total at [0.90, 1.11]; H4b = intersection-
    union p over its three pre-registered sub-tests (L-union total < 1, L-union desk x exit < 1, O-union total < 1);
    H4c = intersection-union p of 'ratio <= 0.85 in each of 2024-26'; H4d = intersection-union p of 'cross > 0' and
    'cross - within > 0'. Bootstrap p-values of 0 are floored at 1/2000.
  * falsified  -> the PLAN falsification condition holds (point estimates);
    supported  -> not falsified and the Holm-adjusted p < 0.05 (and the per-hypothesis extra conditions below);
    partially_supported -> not falsified, the full claim fails Holm or an extra condition, but a pre-registered
                           sub-claim passes at the hypothesis' Holm step;
    not_supported -> otherwise.
    Extra conditions: H4d additionally requires the cross-sectional excess to survive topic100 FE (co-primary after
    the identification audit); H4e (descriptive) is 'supported' only if every counted M statistic is within +/-10%.
  * Qualifiers (identification flags) are attached to each verdict and drive the wording in RESULTS.md.

Run (after d4_stage_gains, d4_bias_atlas, d4_exit_composition):
    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d4_collect
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import d4_stage_gains as S

OUTDIR = S.OUTDIR
SRC = Path(__file__).resolve().parent
SNAP = C.OUT / "snapshot"
P_FLOOR = 1.0 / S.N_BOOT
AUTO_START, AUTO_END = "<!-- AUTO:SUMMARY START -->", "<!-- AUTO:SUMMARY END -->"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def r3(x, k=3):
    if x is None:
        return None
    try:
        xf = float(x)
    except (TypeError, ValueError):
        return x
    return None if not np.isfinite(xf) else round(xf, k)


def f(x, k=3):
    """Format a number for notes."""
    return "n/a" if x is None or not np.isfinite(float(x)) else f"{float(x):.{k}f}"


def ci(d, k=3, lo="lo95", hi="hi95"):
    return f"{f(d['est'], k)} [{f(d[lo], k)}, {f(d[hi], k)}]"


def pfmt(p):
    return f"< {P_FLOOR:.4f}" if p <= P_FLOOR + 1e-12 else f"{p:.3f}" if p >= 0.001 else f"{p:.1e}"


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
    kb = pd.read_csv(OUTDIR / "kobak_bounds.csv")
    atlas = pd.read_csv(OUTDIR / "atlas.csv")
    cr = pd.read_csv(OUTDIR / "T4_1_continuation_ratio.csv")
    adj = pd.read_csv(OUTDIR / "T4_1_adjusted_total.csv")
    its_yl = pd.read_csv(OUTDIR / "its_pools_yearlevel.csv")
    exitc = pd.read_csv(OUTDIR / "exit_composition.csv")
    bound = pd.read_csv(OUTDIR / "T4_2_decision_bound.csv")
    flips = pd.read_csv(OUTDIR / "T4_2_audit_flips.csv")

    def G(feature, gain, period="2024-26", variant="primary", pooling="std"):
        r = gains[(gains.variant == variant) & (gains.feature == feature) & (gains.gain == gain)
                  & (gains.period == period) & (gains.pooling == pooling)]
        if not len(r):
            return None
        r = r.iloc[0]
        return {k: r3(r[k], 6) for k in ["est", "lo95", "hi95", "lo90", "hi90", "p_ge1", "p_le1"]}

    def pge1(feature, gain, **kw):
        return max(float(G(feature, gain, **kw)["p_ge1"]), P_FLOOR)

    # ---------------- WP4 canonical audit interface (outputs/snapshot), side by side with D4's own copy
    wp4 = None
    tp_path = SNAP / "T4_2_tipping_points.csv"
    if tp_path.exists():
        tp = pd.read_csv(tp_path)
        tp = tp[tp.period.eq("2024-26")].set_index("feature")
        gate = pd.read_csv(SNAP / "gate.csv") if (SNAP / "gate.csv").exists() else None
        absa = pd.read_csv(SNAP / "abstract_audit.csv") if (SNAP / "abstract_audit.csv").exists() else None
        wp4 = dict(
            source="outputs/snapshot/T4_2_tipping_points.csv, gate.csv, abstract_audit.csv (WP4 snapshot_bounds.py)",
            mtime=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(tp_path))),
            features={k: {c: r3(tp.loc[k, c], 4) for c in ["did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp",
                                                             "tip_total_pp", "G_dec_audit_lo", "G_dec_audit_hi",
                                                             "G_total_audit_lo", "G_total_audit_hi",
                                                             "G_total_corr_lo90", "G_total_corr_hi90",
                                                             "G_dec_identified", "G_total_identified"]}
                      for k in tp.index},
            gate=None if gate is None else gate.head(2).to_dict(orient="records"),
            abstract_audit=None if absa is None else absa[
                ["feature", "label", "n_acc", "v1_present_acc", "adds_acc", "drops_acc", "prev_v1_acc", "prev_or_acc",
                 "n_rej", "v1_present_rej", "adds_rej", "drops_rej", "prev_v1_rej", "prev_or_rej", "did", "did_lo",
                 "did_hi", "auditable", "tp_tip_dec_pp", "tp_tip_total_pp", "tp_G_total_audit_lo",
                 "tp_G_total_audit_hi", "tp_G_dec_identified", "tp_G_total_identified"]].to_dict(orient="records"),
        )

    # ---------------- Holm family
    a = sg["H4a"]
    tost = a["tost_0p90_1p11"]
    b = sg["H4b"]
    c = ba["H4c"]
    d = ex["H4d"]
    p_sub_h4b = {"L_union_total_lt1": pge1("L_union", "total"), "L_union_predec_lt1": pge1("L_union", "predec"),
                 "O_union_total_lt1": pge1("O_union", "total")}
    prim, topic = d["primary"], d["topic100_FE"]
    fam = {"H4a": max(float(tost["p_tost"]), P_FLOOR), "H4b": max(p_sub_h4b.values()),
           "H4c": max(float(c["p_iut_ratio_le_0p85"]), P_FLOOR),
           "H4d": max(float(prim["cross_p_one_sided_gt0"]), float(prim["diff_p_one_sided"]), 1e-12)}
    holm = S.holm_adjust(fam)
    order = sorted(fam, key=lambda k: fam[k])
    step = {k: len(fam) - i for i, k in enumerate(order)}  # Holm multiplier at the hypothesis' step
    holm_tab = [dict(hypothesis=k, p_raw=fam[k], holm_rank=i + 1, holm_threshold=0.05 / (len(fam) - i),
                     p_holm=holm[k], reject_0p05=bool(holm[k] < 0.05)) for i, k in enumerate(order)]

    # ---------------- H4a
    its = a["its_equality"]
    yl = its_yl.set_index("contrast")
    wpN = wp4["features"].get("NAME") if wp4 else None
    bN = bound.set_index("feature").loc["NAME"]
    h4a_fals = bool(a["falsified"])
    h4a_ci_band = a["name_by_year_ci_inside_band"]
    h4a_flags = dict(
        decision_stage_identified=bool(bN.G_total_identified),
        selection_only_G_total_interval_d4=[r3(bN.G_total_interval_lo), r3(bN.G_total_interval_hi)],
        selection_only_G_total_interval_wp4=None if wpN is None else [wpN["G_total_audit_lo"], wpN["G_total_audit_hi"]],
        selection_only_interval_crosses_0p90=bool(bN.G_total_interval_lo < 0.90 or
                                                  (wpN is not None and wpN["G_total_audit_lo"] < 0.90)),
        yearly_cis_inside_band=[y for y, v in h4a_ci_band.items() if v],
        its_pair_equivalence_paper_level=bool(its["all_pairs_equivalent_0p1"]),
        its_pair_equivalence_year_level={k: bool(yl.loc[k, "equivalent_0p1_90ci"]) for k in ["ACC-REJ", "ACC-WD",
                                                                                              "REJ-WD"]},
    )
    if h4a_fals:
        v4a = "falsified"
    elif holm["H4a"] < 0.05 and a["all_years_in_band"]:
        v4a = "supported"
    elif holm["H4a"] < 0.05:
        v4a = "partially_supported"
    else:
        v4a = "not_supported"
    pairs = {f"{p['a']}-{p['b']}": p for p in its["pairs"]}
    h4a = dict(
        statement="Neutral filter for the mainstream fashion: NAME G_total in [0.95, 1.10] every year 2018-26; pooled "
                  "2024-26 TOST within [0.90, 1.11]; 2024 slope-change OR equal across ACC, REJ, WD.",
        estimates=dict(
            name_total_by_year={y: {k: r3(v[k], 4) for k in ["est", "lo95", "hi95"]}
                                for y, v in a["name_total_by_year"].items()},
            all_years_in_band_point=a["all_years_in_band"], yearly_ci_inside_band=h4a_ci_band,
            pooled_2024_26_std=G("NAME", "total"), pooled_2024_26_raw=G("NAME", "total", pooling="raw"),
            pooled_2024_25_std=G("NAME", "total", "2024-25"), pooled_2018_23_std=G("NAME", "total", "2018-23"),
            pooled_2018_23_excl_2019=G("NAME", "total", "2018-23 excl. 2019"),
            pooled_2018_22_std=G("NAME", "total", "2018-22"),
            stage_gains_2024_26={g: G("NAME", g) for g in ["desk", "exit", "dec", "predec", "desk_crf", "exit_crf",
                                                           "predec_crf"]},
            tost=tost,
            its_pools={r["pool"]: dict(OR=r3(r["slope_change_OR"]), lo=r3(r["slope_change_OR_lo"]),
                                       hi=r3(r["slope_change_OR_hi"]), p=r3(r["slope_change_p"], 4), nobs=r["nobs"])
                       for r in a["its_pools"]},
            its_wald=dict(chi2=r3(its["wald_chi2"]), df=its["df"], p=r3(its["p"]), max_abs_dlogOR=r3(its["max_abs_dlogOR"]),
                          pairs=[{k: (r3(v, 4) if isinstance(v, float) else v) for k, v in p.items()}
                                 for p in its["pairs"]]),
            its_yearlevel=its_yl.round(4).to_dict(orient="records"),
            adjusted_stage_gains={st: cr[(cr.era == "2024-26") & (cr.stage == st) & (cr.feature == "NAME")][
                ["OR", "OR_lo", "OR_hi", "p", "q_bh", "G_raw", "G_adj", "G_adj_lo", "G_adj_hi"]].round(4).iloc[0].to_dict()
                for st in ["desk", "exit", "decision"]},
        ),
        falsification="pooled NAME G_total 90% CI outside [0.90, 1.11], or pool-specific break ORs differ at p < .05",
        falsified=h4a_fals, p_family=fam["H4a"], p_holm=holm["H4a"], verdict=v4a,
        verdict_label=("supported for the observed (published vs submitted) NAME share; review-stage neutrality not "
                       "identified" if v4a == "supported" else v4a),
        qualifiers=h4a_flags,
        notes=(f"Pooled 2024-26 NAME G_total {ci(G('NAME', 'total'))}; 90% CI [{f(tost['lo90'])}, {f(tost['hi90'])}] "
               f"inside [0.90, 1.11] (TOST p {pfmt(fam['H4a'])}, Holm {pfmt(holm['H4a'])}). All nine yearly point "
               f"estimates lie in [0.95, 1.10]; the 95% CIs lie inside the band only for "
               f"{', '.join(h4a_flags['yearly_cis_inside_band']) or 'no year'}. Pool breaks: Wald p = "
               f"{f(its['p'], 2)} (paper-level); year-level slope-change differences ACC-REJ "
               f"{f(yl.loc['ACC-REJ', 'est'])} [{f(yl.loc['ACC-REJ', 'lo95'])}, {f(yl.loc['ACC-REJ', 'hi95'])}], "
               f"ACC-WD [{f(yl.loc['ACC-WD', 'lo95'])}, {f(yl.loc['ACC-WD', 'hi95'])}]: no evidence of a difference, "
               f"equivalence at +/-0.1 not established (WD comparison uninformative). The decision stage is not "
               f"identified: the audit-implied selection-only G_total is [{f(bN.G_total_interval_lo)}, "
               f"{f(bN.G_total_interval_hi)}] (D4) / "
               + (f"[{f(wpN['G_total_audit_lo'])}, {f(wpN['G_total_audit_hi'])}] (WP4 canonical)" if wpN else "n/a")
               + ", which crosses the 0.90 margin."),
    )

    # ---------------- H4b
    sub_pass = {k: bool(p * step["H4b"] < 0.05) for k, p in p_sub_h4b.items()}
    h4b_fals = bool(b["falsified"])
    if h4b_fals:
        v4b = "falsified"
    elif holm["H4b"] < 0.05:
        v4b = "supported"
    elif any(sub_pass.values()):
        v4b = "partially_supported"
    else:
        v4b = "not_supported"
    LnoR = G("L_noR24", "total")
    R24pp = G("R24", "total", "2024-26 / 2018-23", "post_vs_pre")
    Ocrf = G("O_union", "predec_crf")
    h4b_flags = dict(
        L_total_survives_holm=sub_pass["L_union_total_lt1"],
        L_depletion_llm_specific=bool(LnoR["hi95"] < 1 and R24pp["hi95"] < 1),
        L_noR24_total=LnoR, R24_post_vs_pre_total=R24pp,
        O_depletion_identified_as_selection=bool(Ocrf["hi95"] < 1),
        O_union_predec_crf=Ocrf,
        identified_O_depletion=dict(all_caps_title_predec_crf=G("all_caps_title", "predec_crf"),
                                    all_caps_title_exit_crf=G("all_caps_title", "exit_crf")),
        ct6_identifies_llm_specific_selection=False,
    )
    comp_keys = ["title_typo", "R24", "R26", "F24", "F26", "emdash", "style_density", "all_caps_title",
                 "sentence_case", "question_opener", "L_noR24", "F26_incl_title", "allcaps_name", "F24_2", "L_title",
                 "L_abstract"]
    h4b = dict(
        statement="Depletion of LLM and outsider markers: pooled 2024-26 G_total < 1 for the L-union and O-union; "
                  "G_desk x G_exit < 1 for the L-union.",
        estimates=dict(
            L_union_total=G("L_union", "total"), O_union_total=G("O_union", "total"),
            L_union_predec=G("L_union", "predec"), L_union_predec_camera_ready_free=G("L_union", "predec_crf"),
            L_union_total_raw_pooling=G("L_union", "total", pooling="raw"),
            L_union_by_year_total={y: G("L_union", "total", y) for y in ["2024", "2025", "2026"]},
            L_union_by_year_predec={y: G("L_union", "predec", y) for y in ["2024", "2025", "2026"]},
            L_union_pre_2018_23={g: G("L_union", g, "2018-23") for g in ["total", "predec", "dec", "predec_crf"]},
            L_union_pre_2018_22={g: G("L_union", g, "2018-22") for g in ["total", "predec", "dec", "predec_crf"]},
            L_union_post_vs_pre={g: G("L_union", g, "2024-26 / 2018-23", "post_vs_pre")
                                 for g in ["total", "predec", "dec", "predec_crf"]},
            L_union_post_vs_pre_1822={g: G("L_union", g, "2024-26 / 2018-22", "post_vs_pre_1822")
                                      for g in ["total", "predec", "dec", "predec_crf"]},
            L_noR24={g: G("L_noR24", g) for g in ["total", "predec", "predec_crf", "dec"]},
            O_union_stage={g: G("O_union", g) for g in ["desk", "exit", "dec", "predec", "predec_crf", "exit_crf"]},
            components={k: {g: G(k, g) for g in ["total", "predec", "predec_crf", "exit", "exit_crf", "dec"]}
                        for k in comp_keys},
            components_post_vs_pre={k: {g: G(k, g, "2024-26 / 2018-23", "post_vs_pre") for g in
                                        ["total", "predec_crf"]} for k in comp_keys},
            components_post_vs_pre_1822={k: {g: G(k, g, "2024-26 / 2018-22", "post_vs_pre_1822") for g in
                                             ["total", "predec_crf"]} for k in comp_keys},
            components_pre_2018_23={k: {g: G(k, g, "2018-23") for g in ["total", "predec_crf"]} for k in comp_keys},
            style_density_reselect={g: G("style_density", g, variant="density_reselect")
                                    for g in ["total", "exit", "predec", "predec_crf"]},
            style_density_reselect_info=b.get("style_density_reselect", {}).get("info"),
            sub_tests_p=p_sub_h4b, sub_tests_pass_at_holm_step=sub_pass,
        ),
        falsification="L-union G_total >= 1",
        falsified=h4b_fals, p_family=fam["H4b"], p_holm=holm["H4b"], verdict=v4b,
        verdict_label=("partially supported: L-union total depletion not significant after Holm; the significant "
                       "pre-decision L depletion is carried by R24 title words, whose depletion pre-dates 2024; the O "
                       "depletion lies at the unidentified decision stage" if v4b == "partially_supported" else v4b),
        qualifiers=h4b_flags,
        notes=(f"L-union total {ci(G('L_union', 'total'))} (one-sided p {f(p_sub_h4b['L_union_total_lt1'], 4)}; Holm "
               f"step x{step['H4b']} -> {f(p_sub_h4b['L_union_total_lt1'] * step['H4b'], 3)}, not significant); "
               f"desk x exit {ci(G('L_union', 'predec'))} (camera-ready-free {ci(G('L_union', 'predec_crf'))}). "
               f"Without R24 the L-union is neutral: total {ci(LnoR)}, camera-ready-free pre-decision "
               f"{ci(G('L_noR24', 'predec_crf'))}. R24 total {ci(G('R24', 'total'))} vs 2018-23 "
               f"{ci(G('R24', 'total', '2018-23'))} (post/pre {ci(R24pp)}). O-union total {ci(G('O_union', 'total'))} "
               f"sits at the decision stage ({ci(G('O_union', 'dec'))}); its camera-ready-free pre-decision gain is "
               f"{ci(Ocrf)}; the identified O depletion is ALL-CAPS at exit (camera-ready-free pre-decision "
               f"{ci(G('all_caps_title', 'predec_crf'))})."),
    )

    # ---------------- H4c
    rat = c["ratio_acc_all"]
    h4c_fals = bool(c["falsified"])
    dir_p = max(float(c["p_iut_ratio_lt_1"]), P_FLOOR)
    if h4c_fals:
        v4c = "falsified"
    elif holm["H4c"] < 0.05:
        v4c = "supported"
    elif dir_p * step["H4c"] < 0.05:
        v4c = "partially_supported"
    else:
        v4c = "not_supported"
    ph = c["posthoc_max2122"]
    sens = kb[(kb.set == "ratio_acc_all") & kb.marker.isin(["F24", "F24_2", "L_abstract", "F26"])]
    h4c = dict(
        statement="Accepted-only Kobak-style lower bound on LLM-styled abstracts understates the all-submission bound "
                  "by >= 15% relative in each of 2024-26.",
        estimates=dict(
            bounds_pp={k: {kk: r3(100 * vv, 2) for kk, vv in v.items()} for k, v in c["bounds"].items()},
            ratio_acc_all={y: {k: r3(v, 4) for k, v in dd.items()} for y, dd in rat.items()},
            ratio_p_ge1=c["ratio_p_ge1"], p_iut_ratio_le_0p85=c["p_iut_ratio_le_0p85"], p_iut_ratio_lt_1=dir_p,
            posthoc_max2122={y: {k: r3(v, 4) for k, v in dd.items()} for y, dd in ph.items()},
            basic_bootstrap_ratio={str(x.year): [r3(x.basic_lo95), r3(x.basic_hi95)] for x in
                                   kb[(kb.marker == "F24") & (kb.baseline == "cons") & (kb.set == "ratio_acc_all")
                                      & kb.year.isin(["2024", "2025", "2026"])].itertuples()},
            sensitivity_ratios=[dict(marker=r.marker, baseline=r.baseline, year=r.year, ratio=r3(r.bound),
                                     lo95=r3(r.lo95), hi95=r3(r.hi95)) for r in sens.itertuples()],
            abstract_audit_F24=None if not wp4 or not wp4["abstract_audit"] else
            next((x for x in wp4["abstract_audit"] if x["feature"] == "F24"), None),
        ),
        falsification="accepted-only bound >= 0.9 x all-submission bound in 2024 and 2025",
        falsified=h4c_fals, falsified_under_posthoc_baseline=bool(c["falsified_under_posthoc_max2122"]),
        p_family=fam["H4c"], p_holm=holm["H4c"], verdict=v4c,
        verdict_label=("partially supported: direction (ratio < 1) supported; the >= 15% magnitude is met in point "
                       "estimates only, and the falsification condition is met under the post hoc pre-ChatGPT "
                       "baseline" if v4c == "partially_supported" else v4c),
        notes=(f"Ratios accepted/all {f(rat['2024']['ratio'])} / {f(rat['2025']['ratio'])} / {f(rat['2026']['ratio'])}"
               f" (2024/25/26); P(ratio >= 0.85) = {f(rat['2024']['p_ge_0p85'])} / {f(rat['2025']['p_ge_0p85'])} / "
               f"{f(rat['2026']['p_ge_0p85'])} (IUT p {f(c['p_iut_ratio_le_0p85'])}, Holm {f(holm['H4c'])}); "
               f"P(ratio >= 1) max {pfmt(dir_p)}. Post hoc baseline max(p2021, p2022): {f(ph['2024']['ratio'], 4)} / "
               f"{f(ph['2025']['ratio'], 4)} / {f(ph['2026']['ratio'], 4)}, which meets the falsification condition "
               f"(>= 0.9 in 2024 and 2025)."),
    )

    # ---------------- H4d
    h4d_fals = bool(d["falsified"])
    cond_cross = bool(prim["cross_lo95_pp"] > 0)
    cond_topic = bool(topic["cross_lo95_pp"] > 0)
    if h4d_fals:
        v4d = "falsified"
    elif holm["H4d"] < 0.05 and cond_topic:
        v4d = "supported"
    elif holm["H4d"] < 0.05:
        v4d = "partially_supported"
    else:
        v4d = "not_supported"
    rob = {r["spec"]: r for r in d["robustness"]}
    kxy = exitc[(exitc.key == "NAME") & exitc.spec.eq("key_x_year_topic100_FE")].iloc[0]

    def spec_row(r):
        return dict(cross=r3(r["cross_pp"], 2), cross_se=r3(r["cross_se_pp"], 2), cross_lo95=r3(r["cross_lo95_pp"], 2),
                    cross_hi95=r3(r["cross_hi95_pp"], 2), within=r3(r["within_pp"], 2),
                    within_se=r3(r["within_se_pp"], 2), within_lo95=r3(r["within_lo95_pp"], 2),
                    within_hi95=r3(r["within_hi95_pp"], 2), diff=r3(r["diff_pp"], 2), diff_se=r3(r["diff_se_pp"], 2),
                    full_cross=r3(r["full_cross_pp"], 2), full_cross_se=r3(r["full_cross_se_pp"], 2),
                    single_cross=r3(r.get("single_cross_pp"), 2), single_cross_se=r3(r.get("single_cross_se_pp"), 2),
                    single_nobs=r.get("single_nobs"), nobs=r["nobs"], n_keys=r["n_keys"])
    h4d = dict(
        statement="Within NA (withdrawn vs rejected), NAME coefficient > 0 in the cross-section, <= 0 within "
                  "last-position key, and the two differ (pre-registered reading: the excess is between keys).",
        estimates=dict(
            primary=spec_row(prim), topic100_FE=spec_row(topic),
            diff_key_bootstrap=dict(lo95=r3(d["key_bootstrap"]["diff_pp_lo95"], 2),
                                    hi95=r3(d["key_bootstrap"]["diff_pp_hi95"], 2)),
            diff_p_one_sided=prim["diff_p_one_sided"], cross_p_one_sided=prim["cross_p_one_sided_gt0"],
            nobs=prim["nobs"], n_keys=prim["n_keys"], n_keys_with_variation=prim["n_keys_with_variation"],
            robustness={k: spec_row(v) for k, v in rob.items()},
            other_features={r["key"]: spec_row(r) for r in d["other_features"]},
        ),
        falsification="within-author coefficient >= cross-sectional coefficient",
        falsified=h4d_fals, p_family=fam["H4d"], p_holm=holm["H4d"], verdict=v4d,
        verdict_label=("partially supported: the pre-registered contrast holds, but with topic100 FE the "
                       "cross-sectional excess is not significant; most of it is topic composition, and the residual "
                       "excess sits with single-paper keys that the within design cannot test"
                       if v4d == "partially_supported" else v4d),
        qualifiers=dict(cross_gt0_primary=cond_cross, cross_gt0_topic100=cond_topic,
                        within_le0_point=bool(prim["within_pp"] <= 0),
                        within_ci_upper_pp=r3(prim["within_hi95_pp"], 2)),
        notes=(f"Cross {f(prim['cross_pp'], 2)} pp (se {f(prim['cross_se_pp'], 2)}) vs within {f(prim['within_pp'], 2)} "
               f"(se {f(prim['within_se_pp'], 2)}); difference {f(prim['diff_pp'], 2)} (se {f(prim['diff_se_pp'], 2)}). "
               f"With topic100 FE: cross {f(topic['cross_pp'], 2)} [{f(topic['cross_lo95_pp'], 2)}, "
               f"{f(topic['cross_hi95_pp'], 2)}], within {f(topic['within_pp'], 2)}, difference {f(topic['diff_pp'], 2)} "
               f"(se {f(topic['diff_se_pp'], 2)}). Single-paper keys: {f(prim['single_cross_pp'], 2)} "
               f"(se {f(prim['single_cross_se_pp'], 2)}), with topic FE {f(topic['single_cross_pp'], 2)} "
               f"(se {f(topic['single_cross_se_pp'], 2)}). Key x year + topic FE within "
               f"{f(kxy.within_pp, 2)} [{f(kxy.within_lo95_pp, 2)}, {f(kxy.within_hi95_pp, 2)}]."),
    )

    # ---------------- H4e
    e = ba["H4e"]
    v4e = "supported" if e["M_all_within_10pct"] and e["deviations_concentrate_in_O_L"] else \
        "partially_supported" if e["deviations_concentrate_in_O_L"] else "not_supported"
    cols_e = ["label", "cls", "scale", "published_set", "interval_type", "in_count", "T_s0", "T_s3", "T_s2", "ratio",
              "ratio_lo95", "ratio_hi95", "within_10pct", "p_two_sided", "q_bh", "log_desk", "log_exit",
              "log_desk_crf", "log_exit_crf", "log_dec", "log_edit_lo", "log_edit_hi"]
    h4e = dict(
        statement="Accepted-only estimates fall within +/-10% of all-submission estimates for M metrics; deviations "
                  "concentrate in O and L; each gap split into selection and editing (audit).",
        estimates=dict(
            M_within_10pct=f"{e['M_within']}/{e['M_n']}",
            M_accepted_only_within_10pct=f"{e['M_accepted_only_within']}/{e['M_accepted_only_n']}",
            M_outside=e["M_outside"], M_ci90_within_10pct=f"{e['M_ci90_within']}/{e['M_ci90_n']}",
            n_statistics=e["n_statistics"], n_ratio_statistics=e["n_ratio_statistics"],
            n_counted_ratio_statistics=e["n_counted_ratio_statistics"],
            by_class=e["by_class"], knife_edge_0p90=e["knife_edge_0p90"], peaks=e["peaks"],
            M_yearly_total_gain_within_10pct={k: {y: bool(0.9 <= G(k, "total", y)["est"] <= 1.1)
                                                   for y in [str(x) for x in S.YEARS]}
                                              for k in ["NAME", "compound", "phrase_colon", "mixed_case_name",
                                                        "title_case"]},
            atlas=[{k: (r3(v, 4) if isinstance(v, (float, np.floating)) else (None if pd.isna(v) else v))
                    for k, v in r.items()} for r in atlas[cols_e].to_dict(orient="records")],
        ),
        falsification="none pre-registered (descriptive)", falsified=None, verdict=v4e,
        verdict_label=("partially supported (descriptive): prevalence-type M statistics within +/-10%; the ITS break "
                       "(effect scale) and the colon-premium trend are not" if v4e == "partially_supported" else v4e),
        notes=(f"M {e['M_within']}/{e['M_n']} within +/-10% on the effect scale (accepted-only "
               f"{e['M_accepted_only_within']}/{e['M_accepted_only_n']}); outside: {'; '.join(e['M_outside'])}. "
               + "; ".join(f"{r['cls']} {int(r['within'])}/{int(r['n'])} (median |log ratio| "
                           f"{f(r['median_abs_log'])})" for r in e["by_class"]) + "."),
    )

    # ---------------- decision-stage bound
    dec_bound = dict(
        source_d4="computed by d4_bias_atlas from cache/arxiv_audit.jsonl (D4's own copy)",
        wp4_canonical=wp4,
        n_pairs=ba["meta"]["n_pairs"], pairs_by_decision=ba["meta"]["pairs_by_decision"],
        NAME=dict(bound[bound.feature == "NAME"].iloc[0].to_dict()),
        identified_G_dec=bound[bound.G_dec_identified].feature.tolist(),
        identified_G_total=bound[bound.G_total_identified].feature.tolist(),
        unauditable=bound[~bound.auditable].feature.tolist(),
        gate="No title-feature acceptance gain is identified: every tipping point lies inside the audit DiD 95% CI.",
    )

    # ---------------- robustness
    pdv = sg["H4b"]["postdec_withdrawal_variants"]
    rob_out = dict(
        H4a_pooling_raw=G("NAME", "total", pooling="raw"),
        H4a_drop_wd_post=G("NAME", "total", variant="drop_wd_post"),
        H4a_excl_2026=G("NAME", "total", "2024-25"),
        H4a_2018_23_excl_2019=G("NAME", "total", "2018-23 excl. 2019"),
        H4a_its_no_controls=sg["H4a"]["its_robustness"]["no_controls"]["test"],
        H4a_its_acc_rej_2017_26=sg["H4a"]["its_robustness"]["acc_rej_2017_2026"]["test"],
        H4a_its_compound=sg["H4a"]["its_robustness"]["compound_outcome"]["test"],
        H4b_L_union_drop_wd_post=G("L_union", "total", variant="drop_wd_post"),
        H4b_L_union_raw_pooling=G("L_union", "total", pooling="raw"),
        H4b_L_union_excl_2026=G("L_union", "total", "2024-25"),
        H4b_L_union_2018_23_excl_2019=G("L_union", "total", "2018-23 excl. 2019"),
        H4b_O_union_drop_wd_post=G("O_union", "total", variant="drop_wd_post"),
        postdec_withdrawals_consistent=dict(
            note="exit/dec/predec only: G_total = P(s3)/P(s0) does not involve s2 and is identical by construction",
            counts=sg["H4b"]["postdec_withdrawal_counts"], estimates=pdv),
        secondary_markers={k: G(k, "total") for k in ["F24_2", "allcaps_name", "title_emdash", "NAME_strict",
                                                      "NAME_loose", "F26_incl_title"]},
        T4_1_adjusted_total=adj.round(4).to_dict(orient="records"),
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
        "reported as robustness. PLAN does not specify the pooling. The choice was made when d4_stage_gains was "
        "written; it is not separately timestamped before the first estimates.",
        "OTHER rows (71 in 2018 with unknown decision) are dropped from the D4 stage frame.",
        "ALL-CAPS title = casing class all_caps (whole title in capitals), matching the scout record (LITERATURE_BRIEF "
        "s3.5: 'ALL-CAPS titles ... accepted at 16.5% vs 40.5%'). The earlier statement that the pilot used the "
        "NAME-lead orthography is not supported by the scout record and is withdrawn; the NAME-lead variant is "
        "reported as allcaps_name (secondary). The pilot's exact period for 0.37 is not documented.",
        "L-union = any binary L marker (title typography, R24, R26, F24, F26, abstract em dash); the continuous "
        "style density is reported separately and is not in the union. Em dash = abstract em dash.",
        "F26 in the L set is abstract-only (F26 words, U+2011 or en-dash compounds in the abstract); the features_v2 "
        "f26 also fires on title typography (104 of 3,253 2024-26 F26 papers via the title only). Its title part is "
        "a subset of title typography, so the L-union is unchanged; L_abstract and the F26 rows changed slightly.",
        "Year-specific style density re-implements the scout rule on the frozen scout style pool "
        "(analyses/d4_lexicon.json); selected words 123/150/223 for 2024/25/26. Bootstrap CIs re-select the words "
        "in every replicate (variant density_reselect). T4.1 density ORs still condition on the full-sample list.",
        "Decision-stage tipping point accounts for accepted papers inside s2: D* = (P3 - P2)/(1 - a2). The plan's "
        "1.8 pp pilot ignored the (1 - a2) factor; with it NAME's tipping point is 2.9 pp (total-gain tipping point "
        "1.0 pp).",
        "Snapshot module computed inside d4_bias_atlas from cache/arxiv_audit.jsonl because outputs/snapshot/ did not "
        "exist at run time. WP4's canonical outputs (T4_2_tipping_points.csv) agree on point estimates; WP4's primary "
        "DiD interval is wider (pseudo-flip), so both are reported and gate statements use WP4's. WP4's abstract "
        "audit (330 v1 abstracts) makes F24 auditable; D4's own copy audits titles only.",
        "Colon premium: no accepted-only version exists; the published-only analogue is decided-only (ACC vs REJ). "
        "The pre-registered trend enters the M count; the level is supplementary.",
        "OR-type atlas statistics (ITS slope change, colon premium) are compared as ratios of log-ORs (effect scale) "
        "with delta-method CIs; the original OR-ratio comparison is kept in or_ratio columns.",
        "Opener-entropy and JSD intervals are random-selection null bands (pivot), not CIs; they are excluded from the "
        "90%-CI count. The paper bootstrap produced intervals excluding the point estimate.",
        "H4c: post hoc baseline sensitivity max(2021, 2022) added because ICLR 2023 camera-ready abstracts post-date "
        "ChatGPT; under it the falsification condition is met.",
        "Post-decision withdrawals: the primary stage frame follows _core.pool_flags (only the 2026 wd_post rows stay "
        "in s2, as in PLAN section 0 and the frozen CT6). A consistent definition (any withdrawn row with an "
        "accept/reject decision, plus 2025-26 withdrawals timestamped on/after the decision date) is reported for the "
        "exit, decision and pre-decision gains and in H4d.",
        "H4d: primary population REJ u WD (2024-26), outcome = withdrawn incl. 2026 post-decision withdrawals; last "
        "position = max list position (D2 convention); controls year FE, log authors, llm_topic. The topic100-FE "
        "contrast is co-primary after the audit.",
        "Holm over {H4a, H4b, H4c, H4d} with intersection-union p-values; BH over T4.1 and the atlas.",
        "Early vs late 2026 desk rejections not testable: all 737 desk-rejection timestamps fall on/after the "
        "decision date (bulk update).",
        "Desk-stage continuation-ratio logits fitted for 2024-26 only (2018-23 has 0-19 desk rejections a year).",
    ]
    files = sorted(str(p.name) for p in OUTDIR.iterdir() if p.is_file())
    results = dict(
        work_package="WP8 / D4 The gatekeeper", plan="research/titles/docs/PLAN.md D4",
        code={fn: sha(SRC / fn) for fn in ["d4_stage_gains.py", "d4_bias_atlas.py", "d4_exit_composition.py",
                                           "d4_collect.py", "d4_lexicon.json"]},
        lexicon_v2_sha256=sha(SRC / "lexicons.json"),
        meta=dict(stage_gains=sg["meta"], bias_atlas=ba["meta"], audit_fix="see outputs/audit/d4/fix_log.md"),
        multiplicity=dict(family="D4 confirmatory {H4a, H4b, H4c, H4d}; H4e descriptive", method="Holm",
                          table=holm_tab, bh="BH q-values in T4_1_continuation_ratio.csv (q_bh) and atlas.csv (q_bh)"),
        hypotheses=dict(H4a=h4a, H4b=h4b, H4c=h4c, H4d=h4d, H4e=h4e),
        decision_stage_bound=dec_bound, robustness=rob_out, exploratory=expl, deviations=deviations, files=files,
        language="Associational; declared profile keys are not persons; list positions are partition labels.",
    )
    S.write_json(results, OUTDIR / "results.json")

    # ---------------- markdown tables
    t1 = cr[["era", "stage", "feature", "nobs", "OR", "OR_lo", "OR_hi", "p", "q_bh", "G_raw", "G_adj", "G_adj_lo",
             "G_adj_hi"]].copy()
    (OUTDIR / "T4_1_continuation_ratio.md").write_text(
        "# T4.1 Continuation-ratio logits for passing each stage\n\n"
        "Logit of passing the stage on the feature, with year x area FE (2024-26) or year FE (2018-23), log authors, "
        "llm_topic and topic100 FE; SEs clustered by topic100; FE cells without outcome variation dropped. "
        "style_density OR is per SD (the word list is selected on the full sample; selection uncertainty is not in "
        "these CIs). G_adj = RR_att / (s RR_att + 1 - s). q_bh = Benjamini-Hochberg q over all "
        f"{int(cr.p.notna().sum())} tests in this table (PLAN section 0); only q < 0.05 effects are called notable. "
        "F26 is abstract-only.\n\n"
        + md_table(t1, {"p": ".4f", "q_bh": ".4f"}) +
        "\n\n## Adjusted total gain (2024-26): product of stage G_adj\n\n"
        "Approximate 95% CI treats stage estimates as independent (the continuation-ratio likelihood factorises over "
        "stages). G_raw_total is the product of raw-pooled stage gains.\n\n"
        + md_table(adj) + "\n")
    t2 = bound[["feature", "auditable", "P_s2", "P_s3", "G_dec_obs", "did_pp", "did_lo95_pp", "did_hi95_pp",
                "tip_dec_pp", "G_dec_interval_lo", "G_dec_interval_hi", "G_dec_identified", "G_total_obs",
                "tip_total_pp", "G_total_interval_lo", "G_total_interval_hi", "G_total_identified"]].copy()
    if wp4:
        t2["wp4_did_lo_pp"] = t2.feature.map(lambda k: wp4["features"].get(k, {}).get("did_lo_pp", np.nan))
        t2["wp4_did_hi_pp"] = t2.feature.map(lambda k: wp4["features"].get(k, {}).get("did_hi_pp", np.nan))
        t2["wp4_G_total_lo"] = t2.feature.map(lambda k: wp4["features"].get(k, {}).get("G_total_audit_lo", np.nan))
        t2["wp4_G_total_hi"] = t2.feature.map(lambda k: wp4["features"].get(k, {}).get("G_total_audit_hi", np.nan))
    t2 = t2.astype({c_: float for c_ in t2.columns if c_.startswith("wp4_")})
    f1 = flips[flips.spec == "primary"][["feature", "n_acc", "v1_present_acc", "adds_acc", "drops_acc", "n_rej",
                                         "v1_present_rej", "adds_rej", "drops_rej", "net_acc", "net_rej", "did",
                                         "did_se", "auditable"]]
    (OUTDIR / "T4_2_audit.md").write_text(
        "# T4.2 Camera-ready audit: flip matrices and decision-stage tipping points\n\n"
        f"{ba['meta']['n_pairs']} arXiv pairs with a pre-decision v1 ({ba['meta']['pairs_by_decision']}). "
        "adds = absent in v1, present in the stored title; drops = the reverse; net = (adds - drops)/n. "
        "D4's own copy (normal-theory DiD CI); WP4's canonical pseudo-flip interval (outputs/snapshot/"
        "T4_2_tipping_points.csv"
        + (f", {wp4['mtime']} UTC" if wp4 else "") + ") is shown in the wp4_ columns and is wider.\n\n"
        "## Flip matrices (primary, all audit years)\n\n" + md_table(f1, {"net_acc": ".4f", "net_rej": ".4f",
                                                                          "did": ".4f", "did_se": ".4f"}) +
        "\n\n## Decision-stage bound (2024-26, year-standardised prevalences; DiD in pp)\n\n" + md_table(t2) + "\n")

    # ---------------- auto-generated summary table
    Lt, Lp, Ot = G("L_union", "total"), G("L_union", "predec"), G("O_union", "total")
    rows = [
        ("H4a: neutral filter for NAME",
         "Yearly NAME G_total in [0.95, 1.10]; pooled TOST in [0.90, 1.11]; equal 2024 break across ACC/REJ/WD",
         f"Pooled G_total {ci(G('NAME', 'total'))}, 90% CI [{f(tost['lo90'])}, {f(tost['hi90'])}] (TOST p "
         f"{pfmt(fam['H4a'])}). All 9 yearly point estimates in band; 95% CIs inside it only for "
         f"{', '.join(h4a_flags['yearly_cis_inside_band'])}. Break ORs "
         f"{' / '.join(f(r['slope_change_OR']) for r in a['its_pools'])}, Wald p = {f(its['p'], 2)}; year-level "
         f"ACC-REJ difference [{f(yl.loc['ACC-REJ', 'lo95'])}, {f(yl.loc['ACC-REJ', 'hi95'])}], ACC-WD "
         f"[{f(yl.loc['ACC-WD', 'lo95'])}, {f(yl.loc['ACC-WD', 'hi95'])}]. Audit-implied selection-only G_total "
         + (f"[{f(wpN['G_total_audit_lo'])}, {f(wpN['G_total_audit_hi'])}] (WP4)" if wpN else "n/a"),
         f"**{v4a.replace('_', ' ').capitalize()}** for the observed published-vs-submitted NAME share (Holm p "
         f"{pfmt(holm['H4a'])}). Review-stage neutrality is not identified (the selection-only interval crosses "
         f"0.90). Pool equality is not rejected, but equivalence is not shown."),
        ("H4b: depletion of L and O markers",
         "G_total < 1 for the L-union and O-union; G_desk·G_exit < 1 for the L-union",
         f"L-union total {ci(Lt)}, one-sided p {f(p_sub_h4b['L_union_total_lt1'], 4)}. L-union desk·exit {ci(Lp)} "
         f"(camera-ready-free {ci(G('L_union', 'predec_crf'))}). L-union without R24: total {ci(LnoR)}. R24 post/pre "
         f"total {ci(R24pp)}. O-union total {ci(Ot)}; decision stage {f(G('O_union', 'dec')['est'])}; "
         f"camera-ready-free pre-decision {ci(Ocrf)}",
         f"**{v4b.replace('_', ' ').capitalize()}** (Holm p {f(holm['H4b'])}). The L-union total is not significant "
         f"after Holm. The identified pre-decision L depletion is R24 title words, which were depleted before 2024; "
         f"the other L markers are neutral. O: the published record under-represents O titles, but selection is "
         f"not identified (decision stage). The identified O depletion is ALL-CAPS at exit."),
        ("H4c: published-only Kobak bound understates",
         "Accepted/all bound ratio ≤ 0.85 in each of 2024–26; falsified if ≥ 0.9 in both 2024 and 2025",
         f"{f(rat['2024']['ratio'])} [{f(rat['2024']['lo95'])}, {f(rat['2024']['hi95'])}] / "
         f"{f(rat['2025']['ratio'])} [{f(rat['2025']['lo95'])}, {f(rat['2025']['hi95'])}] / "
         f"{f(rat['2026']['ratio'])} [{f(rat['2026']['lo95'])}, {f(rat['2026']['hi95'])}]. "
         f"P(ratio ≥ 0.85) {f(rat['2024']['p_ge_0p85'])} / {f(rat['2025']['p_ge_0p85'])} / "
         f"{f(rat['2026']['p_ge_0p85'])}. Post hoc pre-ChatGPT baseline: {f(ph['2024']['ratio'], 4)} / "
         f"{f(ph['2025']['ratio'], 4)} / {f(ph['2026']['ratio'], 3)}",
         f"**{v4c.replace('_', ' ').capitalize()}** (Holm p {f(holm['H4c'])}). Direction (ratio < 1) is supported. "
         f"The ≥ 15% size holds for point estimates only. The falsification condition is met under the post hoc "
         f"baseline."),
        ("H4d: withdrawal excess of NAME papers",
         "Cross-section > 0, within last-position key ≤ 0, and the two differ",
         f"{f(prim['cross_pp'], 2)} pp (se {f(prim['cross_se_pp'], 2)}) vs {f(prim['within_pp'], 2)} pp (se "
         f"{f(prim['within_se_pp'], 2)}); difference {f(prim['diff_pp'], 2)} (se {f(prim['diff_se_pp'], 2)}). With "
         f"topic100 FE: cross {f(topic['cross_pp'], 2)} [{f(topic['cross_lo95_pp'], 2)}, "
         f"{f(topic['cross_hi95_pp'], 2)}], within {f(topic['within_pp'], 2)}. Single-paper keys "
         f"{f(prim['single_cross_pp'], 2)} (topic FE {f(topic['single_cross_pp'], 2)})",
         f"**{v4d.replace('_', ' ').capitalize()}** (Holm p {pfmt(holm['H4d'])}). The pre-registered contrast holds. "
         f"Most of the excess is topic composition, and 'between keys' is not established as the mechanism."),
        ("H4e: published-only atlas",
         "M statistics within ±10%; deviations concentrate in O and L",
         f"M {e['M_within']}/{e['M_n']} within ±10% on the effect scale (accepted-only "
         f"{e['M_accepted_only_within']}/{e['M_accepted_only_n']}); outside: ITS slope change "
         f"{f(atlas.set_index('label').loc['ITS slope change (NAME), effect scale', 'ratio'], 2)}, colon-premium "
         f"trend {f(atlas.set_index('label').loc['Colon-premium trend, 2018-26 (decided-only)', 'ratio'], 2)}. "
         + "; ".join(f"{r['cls']} {int(r['within'])}/{int(r['n'])}" for r in e["by_class"] if r["cls"] != "M"),
         f"**{v4e.replace('_', ' ').capitalize()}** (descriptive). Prevalence levels are reproduced; the 2024 "
         f"break is halved."),
        ("Decision-stage gate", "A gain enters the headline only if its tipping point exceeds the audit CI",
         f"NAME G_dec tipping point {f(bN.tip_dec_pp, 2)} pp; audit DiD {f(bN.did_pp, 2)} pp [D4 "
         f"{f(bN.did_lo95_pp, 2)}, {f(bN.did_hi95_pp, 2)}; WP4 "
         + (f"{f(wpN['did_lo_pp'], 2)}, {f(wpN['did_hi_pp'], 2)}]" if wpN else "n/a]"),
         "**No title-feature decision gain is identified**"),
    ]
    tab = ["| Hypothesis | Pre-registered test | Result (2024–26 pooled unless stated) | Verdict |",
           "|---|---|---|---|"] + [f"| {a_} | {b_} | {c_} | {d_} |" for a_, b_, c_, d_ in rows]
    summary = "\n".join(tab)
    (OUTDIR / "summary_table.md").write_text(summary + "\n")
    rp = OUTDIR / "RESULTS.md"
    if rp.exists():
        txt = rp.read_text()
        if AUTO_START in txt and AUTO_END in txt:
            pre, rest = txt.split(AUTO_START, 1)
            _, post = rest.split(AUTO_END, 1)
            rp.write_text(pre + AUTO_START + "\n" + summary + "\n" + AUTO_END + post)
    print(json.dumps({k: v["verdict"] for k, v in results["hypotheses"].items()}))
    print(json.dumps({r["hypothesis"]: [round(r["p_raw"], 5), round(r["p_holm"], 5)] for r in holm_tab}))


if __name__ == "__main__":
    main()
