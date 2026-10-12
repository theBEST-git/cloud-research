"""WP6 / D2: collect all D2 outputs into outputs/d2_carriers/results.json with verdicts against the
pre-registered predictions and falsification criteria (PLAN D2), Holm-adjusted one-sided p-values over the
confirmatory family H2a-H2e, and the summary table of RESULTS.md (written between the AUTO markers, so the
table can never go stale against the outputs; audit D2-C1).

One-sided p-values (null = the falsification side of each hypothesis; audit D2-C3 made H2c consistent):
  H2a  P(rho_last <= 0.5)                                key-cluster bootstrap
  H2b  P(rho_first - rho_last >= 0)                      joint key-cluster bootstrap
  H2c  P(change at share_new = 0 <= 0.3 x population)    t-test, two-way (key, paper) CGM-clustered SE
  H2d  P(G_style - G_topic <= 0)                         key-cluster bootstrap over markers
  H2e  max over NAME and compound of P(rho_any <= 0.3)   key-cluster bootstrap (email keys; intersection-union)
Bootstrap p-values are (#{draws on the null side} + 1) / (B + 1).

Verdicts (after the D2 audit, outputs/audit/d2/fix_log.md) also record whether the prediction is diagnostic: a
title is shared by all co-authors, so each rho is compared with the rho that a purely generational world would
produce with the observed co-authorship structure (shared-outcome null, d2_shiftshare.null_outcomes).

Run (after d2_panel, d2_shiftshare, d2_markers, d2_ident, d2_support):
    cd research/titles/src && /home/user/venv/bin/python -m analyses.d2_collect
"""
from __future__ import annotations

import json
import re

import numpy as np
import pandas as pd

from analyses import d2_panel as P

OUTDIR = P.OUTDIR


def bp(draws: np.ndarray, null_side) -> float:
    d = np.asarray(draws, float)
    d = d[np.isfinite(d)]
    return float((null_side(d).sum() + 1) / (len(d) + 1))


def holm(p: dict) -> dict:
    items = sorted(p.items(), key=lambda kv: kv[1])
    m = len(items)
    out, running = {}, 0.0
    for i, (k, v) in enumerate(items):
        running = max(running, min(1.0, (m - i) * v))
        out[k] = running
    return out


def r3(x):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), 4)


def ci(d, k=3, pct=False):
    """'est [lo, hi]' from a dict with est/lo/hi."""
    f = 100 if pct else 1
    return f"{d['est'] * f:.{k}f} [{d['lo'] * f:.{k}f}, {d['hi'] * f:.{k}f}]"


def fmt_p(p):
    return f"{p:.3f}" if p >= 0.00095 else f"{p:.1e}"


def um(s: str) -> str:
    """Typographic minus for negative numbers in the markdown table."""
    return re.sub(r"(?<![\w.])-(?=\d)", "\u2212", s)


def main():
    ss = json.loads((OUTDIR / "shiftshare_results.json").read_text())
    mk = json.loads((OUTDIR / "markers_results.json").read_text())
    sp = json.loads((OUTDIR / "support_results.json").read_text())
    idr = json.loads((OUTDIR / "ident_results.json").read_text())
    info = json.loads((OUTDIR / "panel_info.json").read_text())
    D = np.load(OUTDIR / "shiftshare_boot_draws.npz")
    M = np.load(OUTDIR / "markers_boot_draws.npz")
    fe = pd.read_csv(OUTDIR / "T2_2_author_fe.csv")
    ap = pd.read_csv(OUTDIR / "T2_2b_allprior.csv", keep_default_na=False)
    team = pd.read_csv(OUTDIR / "team_type_shiftshare.csv")
    rem = pd.read_csv(OUTDIR / "removal_extrapolation.csv")
    t21 = pd.read_csv(OUTDIR / "T2_1_decomposition.csv")
    tw = pd.read_csv(OUTDIR / "T2_1b_twoway_se.csv").set_index("stat")
    nf = pd.read_csv(OUTDIR / "T2_4_newcomer_free.csv", keep_default_na=False)
    gap1 = pd.read_csv(OUTDIR / "h2b_first_position.csv")
    s21 = pd.DataFrame(sp["s2_1"]["table"])
    s22 = pd.DataFrame(sp["s2_2"]["table"])

    main_ = ss["main"]
    rho = lambda part, wt="paper": main_[part][wt]["rho"]
    g = lambda spec, st="rho", o="name_primary": D[f"{spec}::{o}::{st}"]
    nul = ss["null_rho"]
    omn = ss["obs_minus_null"]
    twd = lambda st: dict(est=float(tw.loc[st, "est"]), se=float(tw.loc[st, "se_cgm"]), lo=float(tw.loc[st, "cgm_lo"]),
                          hi=float(tw.loc[st, "cgm_hi"]), se_key=float(tw.loc[st, "se_key"]),
                          pigeonhole_lo=float(tw.loc[st, "pig_lo"]), pigeonhole_hi=float(tw.loc[st, "pig_hi"]))
    nfa = nf[nf["sample"].eq("all")].set_index("contrast")

    def nfd(label, sample="all"):
        r = nf[(nf["sample"] == sample) & (nf.contrast == label)].iloc[0]
        return dict(est=float(r.ratio), lo=float(r.ratio_lo), hi=float(r.ratio_hi), n_E=int(r.n_E), n_L=int(r.n_L),
                    change=float(r.change), P_E=float(r.P_E), P_L=float(r.P_L))

    # ---------------- H2a ----------------
    rl, ra = rho("last"), rho("any")
    kl, ka = main_["last"]["paper"]["kit_within_share"], main_["any"]["paper"]["kit_within_share"]
    p_h2a = bp(g("main|last|paper"), lambda d: d <= 0.5)
    h2a_pred_rho = rl["est"] >= 0.70 and ra["est"] >= 0.60
    h2a_pred_lit = kl["est"] >= 0.70 and ka["est"] >= 0.60
    n_last, n_any = nul["main"]["last"]["null_NRfirst"]["est"], nul["main"]["any"]["null_NRfirst"]["est"]
    n1_last, n1_any = nul["main"]["last"]["null_Nfirst"]["est"], nul["main"]["any"]["null_Nfirst"]["est"]
    h2a_null_meets = min(n_last, n1_last) >= 0.70 and min(n_any, n1_any) >= 0.60
    h2a_fals = rl["hi"] < 0.5
    sbar_last = (main_["last"]["paper"]["s_E"]["est"] + main_["last"]["paper"]["s_L"]["est"]) / 2
    sbar_any = (main_["any"]["paper"]["s_E"]["est"] + main_["any"]["paper"]["s_L"]["est"]) / 2
    if h2a_fals:
        v_h2a = "falsified"
    elif h2a_pred_rho and h2a_null_meets:
        v_h2a = "not identified"
    elif h2a_pred_rho and rl["lo"] > 0.5:
        v_h2a = "supported"
    else:
        v_h2a = "partially supported"
    h2a = dict(
        id="H2a", statement="Communal dominance: within-stayer share >= 0.70 (last list position) and >= 0.60 "
                            "(any role), E = 2022-23 -> L = 2025-26, profile keys.",
        estimate=dict(rho_last=rl, rho_any=ra, rho_last_twoway=twd("rho_last"), rho_any_twoway=twd("rho_any"),
                      rho_last_author_wt=rho("last", "author"), rho_any_author_wt=rho("any", "author"),
                      kitagawa_within_share_last=kl, kitagawa_within_share_any=ka,
                      stayer_weight_sbar_last=sbar_last, stayer_weight_sbar_any=sbar_any,
                      ipw_last=main_["last"]["paper"]["rho_ipw"], ipw_any=main_["any"]["paper"]["rho_ipw"],
                      scenario_a_last=main_["last"]["paper"]["bound_a"], scenario_b_last=main_["last"]["paper"]["bound_b"],
                      scenario_a_any=main_["any"]["paper"]["bound_a"], scenario_b_any=main_["any"]["paper"]["bound_b"],
                      exiter_minus_stayer_E_last=main_["last"]["paper"]["gap_XS_E"],
                      shared_outcome_null={part: nul["main"][part] for part in ("last", "any", "first")},
                      obs_minus_null={k: v for k, v in omn.items() if k.startswith("main|")},
                      obs_minus_null_twoway={"last_vs_Nfirst": twd("rho_minus_null_last"),
                                             "any_vs_Nfirst": twd("rho_minus_null_any")},
                      newcomer_free={k: nfd(k) for k in [
                          "all-stayer teams (every declared position a stayer key)",
                          "last=S; L papers with no entrant key", "last=S; L papers with an entrant first author",
                          "first=S and last=S (distinct keys)",
                          "papers with a repeated stayer dyad; L without entrant key",
                          "last=S; lag-1 all-prior team in both windows (symmetric)",
                          "fixed 2021-22-base all-prior teams, E = 2023", "lag-1 all-prior teams",
                          "2-year-lookback all-prior teams, E = 2023"]}),
        p_one_sided=p_h2a, null="rho_last <= 0.5",
        p_vs_shared_outcome_null=omn["main|last|null_NRfirst"]["p_le0"],
        prediction_met=dict(on_rho=bool(h2a_pred_rho), on_literal_kitagawa_share=bool(h2a_pred_lit),
                            under_shared_outcome_null=bool(h2a_null_meets)),
        diagnostic=bool(not h2a_null_meets), falsified=bool(h2a_fals), verdict=v_h2a,
        verdict_note="Prediction met on rho (the pilot-calibrated statistic, deviation D2-1) but not on the literal "
                     "Kitagawa within share; a purely generational world with the observed co-authorship would also "
                     "meet it, so communal dominance is not identified by H2a.")

    # ---------------- H2b ----------------
    dfl = ss["joint_differences"]["rho_first_minus_last"]
    rf = rho("first")
    gap_first = main_["first"]["paper"]["gap_NS_L"]
    p_h2b = bp(g("main|first|paper") - g("main|last|paper"), lambda d: d >= 0)
    h2b_pred = (dfl["est"] <= -0.2) and gap_first["lo"] > 0
    h2b_fals = (dfl["lo"] <= 0 <= dfl["hi"]) and rf["est"] >= 0.8

    def jd(a, b, o="name_primary"):
        x = D[f"{a}::{o}::rho"] - D[f"{b}::{o}::rho"]
        x = x[np.isfinite(x)]
        est = float(t21[(t21.spec == a) & (t21.outcome == o)].rho.iat[0] - t21[(t21.spec == b) & (t21.outcome == o)].rho.iat[0])
        return dict(est=est, se=float(x.std(ddof=1)), lo=float(np.quantile(x, .025)), hi=float(np.quantile(x, .975)))
    extra_diffs = {"alias_restricted": jd("alias_restricted|first|paper", "alias_restricted|last|paper"),
                   "alias_collapse_extreme_bound": jd("alias_collapse|first|paper", "alias_collapse|last|paper"),
                   "topic100_adjusted": jd("adj_topic100|first|paper", "adj_topic100|last|paper", "name_adj_topic"),
                   "trim_top1pct": jd("trim_top1pct|first|paper", "trim_top1pct|last|paper"),
                   "partition_specific_stayers": jd("partition_specific_stayers|first|paper",
                                                    "partition_specific_stayers|last|paper"),
                   "L2026_only": jd("L2026_only|first|paper", "L2026_only|last|paper"),
                   "no_email_papers": jd("no_email_papers|first|paper", "no_email_papers|last|paper")}
    sym = idr["h2b_first_position"]["symmetric_prior_first"]
    gl = gap1.set_index("spec")
    gap_lk = gap1[(gap1.analysis.str.startswith("L entrant-first")) & (gap1.spec == "last-key + size-bin + topic100 FE")].iloc[0]
    prem_chg = gap1[gap1.analysis.str.contains("change 2025-26 vs 2023")].iloc[0]
    h2b_mag_robust = (1 - sym["ratio_prior"]) >= 0.2
    v_h2b = ("falsified" if h2b_fals else
             ("supported" if (h2b_pred and h2b_mag_robust) else
              ("supported on the pre-registered groups; magnitude not robust" if h2b_pred else "partially supported")))
    h2b = dict(
        id="H2b", statement="Generational increment at first list position: rho_first lower than rho_last by >= 0.2; "
                            "entrant first-position keys' L NAME share exceeds stayers'.",
        estimate=dict(rho_first=rf, rho_last=rl, first_minus_last=dfl, first_minus_last_twoway=twd("first_minus_last"),
                      first_minus_last_author_wt=ss["joint_differences"]["rho_first_minus_last_author_wt"],
                      first_minus_last_NA_pool=ss["joint_differences"]["rho_first_minus_last_NA"],
                      first_minus_last_excl2026=ss["joint_differences"]["rho_first_minus_last_excl2026"],
                      first_minus_last_other_variants=extra_diffs,
                      entrant_minus_stayer_L_first=gap_first,
                      entrant_minus_stayer_L_first_within_lastkey_size_topic=dict(
                          est=float(gap_lk.est), se=float(gap_lk.se), lo=float(gap_lk.lo), hi=float(gap_lk.hi)),
                      newcomer_premium_change_2025_26_vs_2023=dict(est=float(prem_chg.est), se=float(prem_chg.se),
                                                                   lo=float(prem_chg.lo), hi=float(prem_chg.hi)),
                      symmetric_lookback_prior_first_ratio=sym,
                      P_NL_first=main_["first"]["paper"]["P_NL"], P_SL_first=main_["first"]["paper"]["P_SL"]),
        p_one_sided=p_h2b, null="rho_first - rho_last >= 0", prediction_met=bool(h2b_pred),
        magnitude_robust_to_symmetric_lookback=bool(h2b_mag_robust), falsified=bool(h2b_fals), verdict=v_h2b,
        verdict_note="The pre-registered contrast holds on the D2 groups, also with two-way SEs; D2 stayers have >= 3 "
                     "years of presence, so the contrast mixes cohort with tenure: within the same last-position key the "
                     "entrant-first premium is about half the raw gap, and with a symmetric 2-year lookback prior first "
                     "keys changed nearly as much as the first-position population.")

    # ---------------- H2c ----------------
    f0 = fe.iloc[0]
    fl = fe[fe.model.eq("lag-1 new-coauthor definition")].iloc[0]
    pop = float(f0.pop_change)

    def apd(dfn, win, smp="all"):
        r = ap[(ap.definition == dfn) & (ap.window == win) & (ap["sample"] == smp)].iloc[0]
        return dict(est=float(r.ratio), lo=float(r.ratio_lo), hi=float(r.ratio_hi), change=float(r.allprior_change),
                    change_lo=float(r.allprior_lo), change_hi=float(r.allprior_hi), P_E=float(r.allprior_P_E),
                    P_L=float(r.allprior_P_L), n_E=int(r.n_allprior_E), n_L=int(r.n_allprior_L),
                    share_L=float(r.share_allprior_L), E=str(r.E), L=str(r.L), pop_change=float(r.pop_change))
    ii = {"rolling": apd("roll", "main"), "lag1": apd("lag1", "main"), "symmetric_2yr_E2023": apd("sym2", "E2023"),
          "fixed_2021_22_base_E2023": apd("fixed", "E2023"), "rolling_E2023": apd("roll", "E2023"),
          "rolling_2023to2026": apd("roll", "2023to2026"), "rolling_NA_pool": apd("roll", "main", "NA_pool")}
    adj_topic_delta = None
    ta = t21[(t21.spec == "adj_topic100|any|paper")]
    if not ta.empty:
        adj_topic_delta = float(ta.delta.iat[0])
    c_i = f0.change_EtoL_at_share_new0 >= 0.5 * pop
    contradicted_i = f0.ratio_hi < 0.5
    c_ii = {k: v["est"] >= 0.5 for k, v in ii.items()}
    h2c_fals = (f0.lo_change <= 0 <= f0.hi_change) and f0.change_EtoL_at_share_new0 < 0.3 * pop
    if h2c_fals:
        v_h2c = "falsified"
    elif c_i and all(c_ii[k] for k in ("rolling", "lag1", "fixed_2021_22_base_E2023")):
        v_h2c = "supported"
    elif contradicted_i:
        v_h2c = "not supported"
    else:
        v_h2c = "partially supported"
    h2c = dict(
        id="H2c", statement="Not driven by entrant co-author keys: (i) on stayers' author-paper rows with key FE, the "
                            "implied E->L change at share_new_coauthors = 0 is >= 0.5 x the population change; (ii) "
                            "teams whose keys all appeared earlier (rolling) rise by >= 0.5 x the population rise.",
        estimate=dict(change_at_share_new0=dict(est=float(f0.change_EtoL_at_share_new0), se=float(f0.se_change),
                                                lo=float(f0.lo_change), hi=float(f0.hi_change),
                                                se_keyonly=float(f0.se_change_keyonly)),
                      population_change=pop, ratio_i=dict(est=float(f0.ratio_to_pop), lo=float(f0.ratio_lo),
                                                          hi=float(f0.ratio_hi), lo_popunc=float(f0.ratio_lo_popunc),
                                                          hi_popunc=float(f0.ratio_hi_popunc),
                                                          lo_keyonly=float(f0.ratio_lo_keyonly),
                                                          hi_keyonly=float(f0.ratio_hi_keyonly)),
                      ratio_i_lag1=dict(est=float(fl.ratio_to_pop), lo=float(fl.ratio_lo), hi=float(fl.ratio_hi)),
                      p_ratio_i_ge_0_5=float(f0.p_ratio_ge_0_5), p_ratio_i_le_0_3=float(f0.p_ratio_le_0_3),
                      ratio_i_vs_topic_adjusted_population_change=(float(f0.change_EtoL_at_share_new0) / adj_topic_delta
                                                                   if adj_topic_delta else None),
                      topic_adjusted_population_change=adj_topic_delta,
                      b_post_x_share_new=dict(est=float(f0.b_post_x_share_new), se=float(f0.se_post_x_share_new)),
                      b_post_x_share_new_lag1=dict(est=float(fl.b_post_x_share_new), se=float(fl.se_post_x_share_new)),
                      variants=fe.to_dict(orient="records"), allprior_ii=ii,
                      rolling_allprior_L_composition={k: nfd(k) for k in [
                          "rolling all-prior; L teams containing an entrant key",
                          "rolling all-prior; L teams with a returner, no entrant",
                          "rolling all-prior; L teams of stayer keys only"]}),
        p_one_sided=float(f0.p_ratio_le_0_3), null="change at share_new = 0 <= 0.3 x population change",
        prediction_met=dict(part_i=bool(c_i), part_i_contradicted=bool(contradicted_i),
                            part_ii={k: bool(v) for k, v in c_ii.items()}),
        falsified=bool(h2c_fals), verdict=v_h2c,
        verdict_note="(i) is contradicted (two-way CI of the ratio excludes 0.5 from below); (ii) is met on the point "
                     "estimate under the rolling and lag-1 definitions only (CIs reach below 0.5) and fails under the "
                     "fixed 2021-22 base; not falsified because the CI of (i) excludes 0, although its margin above "
                     "0.3x is not significant.")

    # ---------------- H2d ----------------
    sa = mk["stats"]["any"]
    hb = idr["h2d_benchmark"]
    p_h2d = bp(M["any::G_style_minus_topic"], lambda d: d <= 0)
    h2d_pred = 0.7 <= sa["slope_all"]["est"] and sa["G_style_minus_topic"]["est"] > 0
    h2d_fals = sa["slope_all"]["est"] < 0.7 or sa["G_style_minus_topic"]["hi"] < 0
    null_slope = hb["null_rho_any"]["null_Nfirst"]["est"]
    slope_diag = null_slope < 0.7
    contrast_robust = (sa["G_style_minus_topic"]["lo"] > 0 and sa["nollm_nonamefam__G_style_minus_topic"]["lo"] > 0
                       and sa["median_rho_style_minus_topic"]["hi"] < 0)
    v_h2d = ("falsified" if h2d_fals else
             ("supported" if h2d_pred and slope_diag and contrast_robust else
              ("supported (channel contrast); slope criterion not diagnostic" if h2d_pred and contrast_robust
               else "partially supported")))
    h2d = dict(
        id="H2d", statement="Style vs topic channel: across markers, within-stayer change regressed on population change "
                            "has slope ~1 (falsified if < 0.7); the generational increment share 1 - within/pop is "
                            "larger for style than for topic markers.",
        estimate=dict(n_style=mk["n_style"], n_topic=mk["n_topic"],
                      **{k: sa[k] for k in ["slope_all", "r_all", "slope0_style", "slope0_topic", "G_style", "G_topic",
                                            "G_style_minus_topic", "Gratio_style", "Gratio_topic",
                                            "Gratio_style_minus_topic", "nollm__slope_all", "nollm__G_style_minus_topic",
                                            "nonamefam__slope_all", "nonamefam__G_style", "nonamefam__G_style_minus_topic",
                                            "nollm_nonamefam__G_style", "nollm_nonamefam__G_topic",
                                            "nollm_nonamefam__G_style_minus_topic", "median_rho_style",
                                            "median_rho_topic", "median_rho_style_minus_topic",
                                            "median_rho_big_style", "median_rho_big_topic"]},
                      weight_shares_any=mk["weight_shares_any"], n_generational_side=mk["n_generational_side"],
                      random_subset_benchmark=hb,
                      last_partition={k: mk["stats"]["last"][k] for k in ["slope_all", "G_style", "G_topic",
                                                                          "G_style_minus_topic", "median_rho_style",
                                                                          "median_rho_topic"]},
                      first_partition={k: mk["stats"]["first"][k] for k in ["slope_all", "G_style", "G_topic",
                                                                            "G_style_minus_topic", "median_rho_style",
                                                                            "median_rho_topic"]}),
        p_one_sided=p_h2d, null="G_style - G_topic <= 0", prediction_met=bool(h2d_pred),
        slope_criterion_diagnostic=bool(slope_diag), channel_contrast_robust=bool(contrast_robust),
        falsified=bool(h2d_fals), verdict=v_h2d,
        verdict_note="A random paper subset gives slope ~1.00 and the shared-outcome generational null gives slope = "
                     "the null rho (~0.78), both above 0.7, so the slope criterion cannot discriminate. The style-topic "
                     "contrast is informative (the null predicts the same ratio for every marker) and survives "
                     "equal weighting and dropping both llm_topic and the NAME family.")

    # ---------------- H2e ----------------
    he = ss["h2e"]["email_2018to2020"]
    ra_e, rc_e = he["name_primary"]["any"]["rho"], he["name_compound"]["any"]["rho"]
    ke, kc_e = he["name_primary"]["any"]["kit_within_share"], he["name_compound"]["any"]["kit_within_share"]
    t_e = t21[(t21.spec == "email_2018to2020|any|paper") & (t21.outcome == "name_primary")].iloc[0]
    sbar_e = (t_e.s_E + t_e.s_L) / 2
    p_name = bp(g("email_2018to2020|any|paper"), lambda d: d <= 0.3)
    p_comp = bp(g("email_2018to2020|any|paper", o="name_compound"), lambda d: d <= 0.3)
    p_h2e = max(p_name, p_comp)
    h2e_pred_rho = ra_e["est"] >= 0.5 and rc_e["est"] >= 0.5
    h2e_fals_rho = ra_e["est"] < 0.3 or rc_e["est"] < 0.3
    h2e_fals_lit = ke["est"] < 0.3 or kc_e["est"] < 0.3
    en = nul["email_2018to2020"]["any"]
    omn_e = omn["email_2018to2020|any|null_Nfirst|name_primary"]
    if h2e_fals_rho:
        v_h2e = "falsified"
    elif h2e_pred_rho and ra_e["lo"] > 0.3 and rc_e["lo"] > 0.3 and not h2e_fals_lit:
        v_h2e = "supported"
    else:
        v_h2e = "inconclusive"
    h2e = dict(
        id="H2e", statement="Pre-LLM replication: with email keys, 2018 -> 2020, the NAME and colon (compound) rise is "
                            ">= 50% within stayers (any role primary).",
        estimate=dict(name_any=ra_e, compound_any=rc_e, name_any_kitagawa_share=ke, compound_any_kitagawa_share=kc_e,
                      stayer_weight_sbar_any=float(sbar_e),
                      name_any_author_wt=ss["h2e_author"]["email_2018to2020"]["name_primary"]["any"]["rho"],
                      compound_any_author_wt=ss["h2e_author"]["email_2018to2020"]["name_compound"]["any"]["rho"],
                      name_last=he["name_primary"]["last"]["rho"], name_first=he["name_primary"]["first"]["rho"],
                      compound_last=he["name_compound"]["last"]["rho"], compound_first=he["name_compound"]["first"]["rho"],
                      delta_name_any=he["name_primary"]["any"]["delta"],
                      delta_compound_any=he["name_compound"]["any"]["delta"],
                      shared_outcome_null_any=en, name_any_minus_null_Nfirst=omn_e,
                      two_year_windows_1718_to_1920=ss["h2e"]["email_1718to1920"],
                      counts=ss["h2e_counts"].get("email_2018to2020|any|paper")),
        p_one_sided=p_h2e, p_name=p_name, p_compound=p_comp,
        null="rho_any <= 0.3 for NAME or for compound (intersection-union)",
        prediction_met=dict(on_rho=bool(h2e_pred_rho), name_lo_above_0_3=bool(ra_e["lo"] > 0.3),
                            compound_lo_above_0_3=bool(rc_e["lo"] > 0.3)),
        falsified=dict(on_rho=bool(h2e_fals_rho), on_literal_kitagawa_share=bool(h2e_fals_lit)), verdict=v_h2e,
        verdict_note="On the literal pre-registered Kitagawa within share both outcomes fall below 0.3, but that "
                     "statistic cannot exceed the stayer weight s_bar = %.2f even under purely communal change. On rho "
                     "(post hoc for H2e, deviation D2-1) NAME is 1.20 and exceeds the shared-outcome null by a margin "
                     "whose CI nearly reaches 0; compound is imprecise and the author-weighted compound rho is below "
                     "0.5." % sbar_e)

    hyps = [h2a, h2b, h2c, h2d, h2e]
    adj = holm({h["id"]: h["p_one_sided"] for h in hyps})
    for h in hyps:
        h["p_holm"] = adj[h["id"]]

    # ---------------- robustness ----------------
    rob = []
    for _, r in t21[t21.outcome.isin(["name_primary", "name_adj_topic", "name_adj_size"])].iterrows():
        rob.append(dict(spec=r.spec, outcome=r.outcome, rho=r3(r.rho), lo=r3(r.rho_lo), hi=r3(r.rho_hi),
                        delta=r3(r.delta), P_SE=r3(r.P_SE), P_SL=r3(r.P_SL), gap_NS_L=r3(r.gap_NS_L),
                        rho_noR=r3(r.rho_noR), rho_noR_lo=r3(r.get("rho_noR_lo")), rho_noR_hi=r3(r.get("rho_noR_hi"))))
    removal = rem[rem.frac.eq(0.2)].to_dict(orient="records")
    team_main = team[(team.window == "main") & (team.stat == "within_share")].to_dict(orient="records")

    # ---------------- supporting ----------------
    s1 = s21[(s21["rule"] == "union") & (s21["sample"] == "dest>=2024")].iloc[0]
    s1s = s21[(s21["rule"] == "strict") & (s21["sample"] == "dest>=2024")].iloc[0]
    s1pre = s21[(s21["rule"] == "union") & (s21["sample"] == "dest<=2023")].iloc[0]
    prim = s22[s22.model.str.startswith("placebo: clean, T 2023-25")].set_index("outcome")
    pil = s22[s22.model.str.startswith("placebo: clean, no topic FE")].set_index("outcome")
    ctrl_prim = prim.loc["llm_topic", "b_expo_past"] - 1.96 * prim.loc["llm_topic", "se_expo_past"] > 0
    ctrl_pil = pil.loc["llm_topic", "b_expo_past"] - 1.96 * pil.loc["llm_topic", "se_expo_past"] > 0
    ctrl_same_order = prim.loc["llm_topic", "past_minus_future"] <= 0 and pil.loc["llm_topic", "past_minus_future"] <= 0
    if ctrl_prim and not ctrl_same_order and prim.loc["name_primary", "past_minus_future"] <= 0:
        v_s22 = "supported"
    else:
        v_s22 = "inconclusive"
    s1_content_fixed_sig = s1.name_primary_p_change_minus_drift_topicadj < 0.05
    support = dict(
        S2_1=dict(statement="Even among retitled resubmissions (destination >= 2024), NAME is not added on net.",
                  n_pairs=int(s1.n_pairs), mean_dNAME=float(s1.name_primary_mean_change),
                  se=float(s1.name_primary_se), adds=int(s1.name_primary_adds), drops=int(s1.name_primary_drops),
                  implied_drift=float(s1.name_primary_implied_drift),
                  change_minus_drift=float(s1.name_primary_change_minus_drift),
                  change_minus_drift_se=float(s1.name_primary_change_minus_drift_se),
                  p_change_minus_drift=float(s1.name_primary_p_change_minus_drift),
                  implied_drift_topicadj=float(s1.name_primary_implied_drift_topicadj),
                  change_minus_drift_topicadj=float(s1.name_primary_change_minus_drift_topicadj),
                  change_minus_drift_topicadj_se=float(s1.name_primary_change_minus_drift_topicadj_se),
                  p_change_minus_drift_topicadj=float(s1.name_primary_p_change_minus_drift_topicadj),
                  implied_drift_intopic=float(s1.name_primary_implied_drift_intopic),
                  change_minus_drift_intopic=float(s1.name_primary_change_minus_drift_intopic),
                  change_minus_drift_intopic_se=float(s1.name_primary_change_minus_drift_intopic_se),
                  p_change_minus_drift_intopic=float(s1.name_primary_p_change_minus_drift_intopic),
                  mde=float(s1.name_primary_mde),
                  samekey_other_papers_change=float(s1.samekey_other_papers_name_change),
                  samekey_other_papers_se=float(s1.samekey_other_papers_se),
                  samekey_pairs=int(s1.samekey_other_papers_pairs),
                  within_pair_minus_samekey=float(s1.within_pair_minus_samekey),
                  within_pair_minus_samekey_se=float(s1.within_pair_minus_samekey_se),
                  p_within_pair_minus_samekey=float(s1.p_within_pair_minus_samekey),
                  strict_rule=dict(n_pairs=int(s1s.n_pairs), mean_dNAME=float(s1s.name_primary_mean_change),
                                   se=float(s1s.name_primary_se), implied_drift=float(s1s.name_primary_implied_drift),
                                   change_minus_drift=float(s1s.name_primary_change_minus_drift),
                                   change_minus_drift_se=float(s1s.name_primary_change_minus_drift_se),
                                   p_change_minus_drift=float(s1s.name_primary_p_change_minus_drift)),
                  pre2024_destinations=dict(n_pairs=int(s1pre.n_pairs), mean_dNAME=float(s1pre.name_primary_mean_change),
                                            se=float(s1pre.name_primary_se),
                                            implied_drift=float(s1pre.name_primary_implied_drift)),
                  compound=dict(mean=float(s1.name_compound_mean_change), se=float(s1.name_compound_se),
                                implied_drift=float(s1.name_compound_implied_drift)),
                  purity=sp["s2_1"]["info"]["purity"],
                  caveat="Pairs are selected on retitling (the export keeps one submission per family); transition "
                         "rates are not behaviour.",
                  verdict=("NAME not added on net; lag behind content-fixed drift established" if s1_content_fixed_sig
                           else "NAME not added on net; lag behind content-fixed drift not established")),
        S2_2=dict(statement="Future-tie placebo: past-collaborator exposure is no larger than future-collaborator "
                            "exposure in the clean sample.",
                  primary={o: {k: float(prim.loc[o, k]) for k in ["b_expo_past", "se_expo_past", "b_expo_future",
                                                                   "se_expo_future", "past_minus_future", "se_diff",
                                                                   "mde_expo_past", "mde_diff", "nobs", "n_keys"]}
                           for o in prim.index},
                  pilot_spec_no_topic_fe={o: {k: float(pil.loc[o, k]) for k in ["b_expo_past", "se_expo_past",
                                                                                 "b_expo_future", "se_expo_future",
                                                                                 "past_minus_future", "se_diff",
                                                                                 "mde_diff"]}
                                          for o in pil.index},
                  positive_control_detected=dict(primary=bool(ctrl_prim), pilot_spec=bool(ctrl_pil)),
                  positive_control_shows_same_ordering=bool(ctrl_same_order),
                  equivalence_upper_bound_past_minus_future_NAME_primary=float(
                      prim.loc["name_primary", "past_minus_future"] + 1.96 * prim.loc["name_primary", "se_diff"]),
                  verdict=v_s22,
                  verdict_note="The ordering past <= future holds for NAME, but the llm_topic positive control is not "
                               "detected in the primary specification and shows the same ordering where it is "
                               "detected, so the design cannot separate tie contagion from homophily."))

    # ---------------- summary table (markdown, auto-generated) ----------------
    tw_l, tw_a, tw_d = twd("rho_last"), twd("rho_any"), twd("first_minus_last")
    i2 = h2c["estimate"]
    rows = [
        ("H2a communal dominance", "within-stayer share: last ≥ 0.70, any role ≥ 0.60",
         f"ρ_last {ci(rl)} (two-way [{tw_l['lo']:.3f}, {tw_l['hi']:.3f}]); ρ_any {ci(ra)} (two-way [{tw_a['lo']:.3f}, "
         f"{tw_a['hi']:.3f}]). Literal Kitagawa share {ci(kl, 2)} / {ci(ka, 2)}. Shared-outcome null: ρ_last "
         f"{n1_last:.2f}–{n_last:.2f}, ρ_any {n1_any:.2f}–{n_any:.2f}",
         "no (upper CI ≫ 0.5)",
         f"**{v_h2a}**: met on ρ (D2-1) but not on the literal share; a purely generational world also meets it"),
        ("H2b first-position increment", "ρ_first ≤ ρ_last − 0.2; entrants > stayers at first position in L",
         f"ρ_first − ρ_last = {ci(dfl)} (two-way [{tw_d['lo']:.3f}, {tw_d['hi']:.3f}]); entrant − stayer "
         f"{ci(gap_first, 1, True)} pp, within the same last key {gap_lk.est * 100:.1f} [{gap_lk.lo * 100:.1f}, "
         f"{gap_lk.hi * 100:.1f}] pp; symmetric-lookback prior-first ratio {sym['ratio_prior']:.2f} "
         f"[{sym['ratio_prior_lo']:.2f}, {sym['ratio_prior_hi']:.2f}]",
         "no", f"**{v_h2b}**"),
        ("H2c not driven by entrant co-author keys", "(i) change at share_new = 0 ≥ 0.5 × population; (ii) all-prior teams ≥ 0.5 × population",
         f"(i) {i2['change_at_share_new0']['est'] * 100:+.2f} pp [{i2['change_at_share_new0']['lo'] * 100:.2f}, "
         f"{i2['change_at_share_new0']['hi'] * 100:.2f}] = {i2['ratio_i']['est']:.2f} [{i2['ratio_i']['lo']:.2f}, "
         f"{i2['ratio_i']['hi']:.2f}] × {pop * 100:.1f} pp (two-way SE; lag-1 {i2['ratio_i_lag1']['est']:.2f}); "
         f"(ii) rolling {ii['rolling']['est']:.2f} [{ii['rolling']['lo']:.2f}, {ii['rolling']['hi']:.2f}], lag-1 "
         f"{ii['lag1']['est']:.2f} [{ii['lag1']['lo']:.2f}, {ii['lag1']['hi']:.2f}], fixed 2021–22 base "
         f"{ii['fixed_2021_22_base_E2023']['est']:.2f} [{ii['fixed_2021_22_base_E2023']['lo']:.2f}, "
         f"{ii['fixed_2021_22_base_E2023']['hi']:.2f}] (n_L = {ii['fixed_2021_22_base_E2023']['n_L']})",
         "no (CI of (i) excludes 0; margin above 0.3× not significant)",
         f"**{v_h2c}**: (i) contradicted (p = {fmt_p(f0.p_ratio_ge_0_5)} against ≥ 0.5); (ii) met on the point "
         f"estimate under rolling and lag-1 only"),
        ("H2d style vs topic", "slope ≈ 1 (≥ 0.7); G_style > G_topic",
         f"slope {ci(sa['slope_all'])} (random-subset benchmark {hb['random_subset_slope_mean']:.2f}, null "
         f"{null_slope:.2f}); G_style {ci(sa['G_style'])} vs G_topic {ci(sa['G_topic'])}; difference "
         f"{ci(sa['G_style_minus_topic'])}; without llm_topic and NAME family "
         f"{ci(sa['nollm_nonamefam__G_style_minus_topic'], 2)}; equal-weight median ρ style − topic "
         f"{ci(sa['median_rho_style_minus_topic'], 2)}",
         "no", f"**{v_h2d}**"),
        ("H2e pre-LLM (email keys, 2018→2020)", "NAME and colon within share ≥ 0.5",
         f"ρ_any NAME {ci(ra_e, 2)}, compound {ci(rc_e, 2)}; author-weighted "
         f"{h2e['estimate']['name_any_author_wt']['est']:.2f} / {h2e['estimate']['compound_any_author_wt']['est']:.2f}; "
         f"literal Kitagawa share {ci(ke, 2)} / {ci(kc_e, 2)} (s̄ = {sbar_e:.2f}); ρ_any − null {ci(omn_e, 2)}",
         "yes on the literal share (< 0.3), which cannot exceed s̄ even under purely communal change; no on ρ",
         f"**{v_h2e}**"),
    ]
    tbl = ["| Hypothesis | Pre-registered prediction | Estimate (95% CI) | Falsified? | Verdict | one-sided p (Holm) |",
           "|---|---|---|---|---|---|"]
    for (lab, pred, est, fals, verd), h in zip(rows, hyps):
        tbl.append(f"| {lab} | {pred} | {um(est)} | {fals} | {verd} | {fmt_p(h['p_one_sided'])} ({fmt_p(h['p_holm'])}) |")
    table_md = "\n".join(tbl)
    (OUTDIR / "T2_0_summary_table.md").write_text(table_md + "\n")
    res_md = OUTDIR / "RESULTS.md"
    if res_md.exists():
        txt = res_md.read_text()
        pat = re.compile(r"(<!-- BEGIN AUTO: summary_table[^>]*-->\n).*?(<!-- END AUTO: summary_table -->)", re.S)
        if pat.search(txt):
            res_md.write_text(pat.sub(lambda m_: m_.group(1) + table_md + "\n" + m_.group(2), txt))
        else:
            print("WARNING: summary-table markers not found in RESULTS.md")

    out = dict(
        direction="D2 Who carries the fashion: communal vs generational change (WP6)",
        plan="research/titles/docs/PLAN.md D2", windows=dict(E=list(P.E_WIN), L=list(P.L_WIN)),
        panel=info, n_boot=ss["n_boot"], hypotheses=hyps, holm_family=list(adj.keys()),
        main_decomposition_T2_1={part: main_[part] for part in ("last", "first", "any")},
        twoway_se=tw.reset_index().to_dict(orient="records"),
        shared_outcome_null=nul, obs_minus_null=omn,
        newcomer_free=nf.to_dict(orient="records"),
        name_definitions=ss["name_defs"], compound=ss["compound_main"], variants=ss["variants"],
        team_types=team_main, allprior=ap.to_dict(orient="records"), removal_simulation=removal,
        family_removal_simulation=idr["family_removal"], ipw=ss["ipw"], alias=ss["alias"],
        alias_restricted=ss["alias_restricted"], email_position_papers=ss["email_position_papers"],
        trim=ss["trim_top1pct"], robustness_rho=rob, h2b_first_position=idr["h2b_first_position"],
        supporting=support, summary_table_md=table_md,
        files=sorted(p.name for p in OUTDIR.iterdir() if p.is_file()))
    (OUTDIR / "results.json").write_text(json.dumps(out, indent=1, default=float))
    for h in hyps:
        print(h["id"], h["verdict"], "p=%.4g holm=%.4g" % (h["p_one_sided"], h["p_holm"]), h["prediction_met"],
              "falsified" if h["falsified"] is True else "")
    print("S2.1", support["S2_1"]["verdict"], "| S2.2", support["S2_2"]["verdict"])
    print(table_md)


if __name__ == "__main__":
    main()
