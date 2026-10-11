"""WP6 / D2: collect all D2 outputs into outputs/d2_carriers/results.json with verdicts against the
pre-registered predictions and falsification criteria (PLAN D2), and Holm-adjusted one-sided p-values over the
confirmatory family H2a-H2e.

One-sided p-values (null = the falsification side of each hypothesis):
  H2a  P(rho_last <= 0.5)                       key-cluster bootstrap
  H2b  P(rho_first - rho_last >= 0)             joint key-cluster bootstrap
  H2c  P(change at share_new = 0 <= 0)          t-test, key-clustered CRV1 (T2.2 primary model)
  H2d  P(G_style - G_topic <= 0)                key-cluster bootstrap over markers
  H2e  P(rho_any(2018 -> 2020, NAME) <= 0.3)    key-cluster bootstrap (email keys)
Bootstrap p-values are (#{draws on the null side} + 1) / (B + 1).

Run (after d2_panel, d2_shiftshare, d2_markers, d2_support):
    cd research/titles/src && /home/user/venv/bin/python -m analyses.d2_collect
"""
from __future__ import annotations

import json

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


def main():
    ss = json.loads((OUTDIR / "shiftshare_results.json").read_text())
    mk = json.loads((OUTDIR / "markers_results.json").read_text())
    sp = json.loads((OUTDIR / "support_results.json").read_text())
    info = json.loads((OUTDIR / "panel_info.json").read_text())
    D = np.load(OUTDIR / "shiftshare_boot_draws.npz")
    M = np.load(OUTDIR / "markers_boot_draws.npz")
    fe = pd.read_csv(OUTDIR / "T2_2_author_fe.csv")
    team = pd.read_csv(OUTDIR / "team_type_shiftshare.csv")
    rem = pd.read_csv(OUTDIR / "removal_extrapolation.csv")
    t21 = pd.read_csv(OUTDIR / "T2_1_decomposition.csv")
    s21 = pd.DataFrame(sp["s2_1"]["table"])
    s22 = pd.DataFrame(sp["s2_2"]["table"])

    main_ = ss["main"]
    rho = lambda part, wt="paper": main_[part][wt]["rho"]
    g = lambda spec, st="rho", o="name_primary": D[f"{spec}::{o}::{st}"]

    # ---------------- H2a ----------------
    rl, ra = rho("last"), rho("any")
    p_h2a = bp(g("main|last|paper"), lambda d: d <= 0.5)
    h2a_pred = rl["est"] >= 0.70 and ra["est"] >= 0.60
    h2a_fals = rl["hi"] < 0.5
    h2a = dict(
        id="H2a", statement="Communal dominance: within-stayer share rho >= 0.70 (last list position) and >= 0.60 "
                            "(any role), E = 2022-23 -> L = 2025-26, profile keys.",
        estimate=dict(rho_last=rl, rho_any=ra, rho_last_author_wt=rho("last", "author"),
                      rho_any_author_wt=rho("any", "author"),
                      kitagawa_within_share_last=main_["last"]["paper"]["kit_within_share"],
                      kitagawa_within_share_any=main_["any"]["paper"]["kit_within_share"],
                      ipw_last=main_["last"]["paper"]["rho_ipw"], ipw_any=main_["any"]["paper"]["rho_ipw"],
                      bound_a_last=main_["last"]["paper"]["bound_a"], bound_b_last=main_["last"]["paper"]["bound_b"],
                      bound_a_any=main_["any"]["paper"]["bound_a"], bound_b_any=main_["any"]["paper"]["bound_b"],
                      exiter_minus_stayer_E_last=main_["last"]["paper"]["gap_XS_E"]),
        p_one_sided=p_h2a, null="rho_last <= 0.5",
        prediction_met=bool(h2a_pred), falsified=bool(h2a_fals),
        verdict="falsified" if h2a_fals else ("supported" if h2a_pred and rl["lo"] > 0.5 else "partially_supported"))

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
    extra_diffs = {"alias_collapse": jd("alias_collapse|first|paper", "alias_collapse|last|paper"),
                   "topic100_adjusted": jd("adj_topic100|first|paper", "adj_topic100|last|paper", "name_adj_topic"),
                   "trim_top1pct": jd("trim_top1pct|first|paper", "trim_top1pct|last|paper"),
                   "partition_specific_stayers": jd("partition_specific_stayers|first|paper",
                                                    "partition_specific_stayers|last|paper"),
                   "L2026_only": jd("L2026_only|first|paper", "L2026_only|last|paper")}
    h2b = dict(
        id="H2b", statement="Generational increment at first list position: rho_first lower than rho_last by >= 0.2; "
                            "entrant first-position keys' L NAME share exceeds stayers'.",
        estimate=dict(rho_first=rf, rho_last=rl, first_minus_last=dfl,
                      first_minus_last_author_wt=ss["joint_differences"]["rho_first_minus_last_author_wt"],
                      first_minus_last_NA_pool=ss["joint_differences"]["rho_first_minus_last_NA"],
                      first_minus_last_excl2026=ss["joint_differences"]["rho_first_minus_last_excl2026"],
                      first_minus_last_other_variants=extra_diffs,
                      entrant_minus_stayer_L_first=gap_first,
                      P_NL_first=main_["first"]["paper"]["P_NL"], P_SL_first=main_["first"]["paper"]["P_SL"]),
        p_one_sided=p_h2b, null="rho_first - rho_last >= 0", prediction_met=bool(h2b_pred), falsified=bool(h2b_fals),
        verdict="falsified" if h2b_fals else ("supported" if h2b_pred else "partially_supported"))

    # ---------------- H2c ----------------
    f0 = fe.iloc[0]
    ap = [a for a in ss["allprior"] if a["window"] == "main"][0]
    ap2326 = [a for a in ss["allprior"] if a["window"] == "2023to2026"][0]
    pop = float(f0.pop_change)
    adj_topic_delta = main_any_adj = None
    ta = t21[(t21.spec == "adj_topic100|any|paper")]
    if not ta.empty:
        adj_topic_delta = float(ta.delta.iat[0])
    c_i = f0.change_EtoL_at_share_new0 >= 0.5 * pop
    c_ii = ap["ratio"] >= 0.5
    h2c_fals = (f0.lo_change <= 0 <= f0.hi_change) and f0.change_EtoL_at_share_new0 < 0.3 * pop
    h2c = dict(
        id="H2c", statement="Not driven by entrant co-authors: (i) on stayers' author-paper rows with key FE, the "
                            "implied E->L change at share_new_coauthors = 0 is >= 0.5 x the population change; (ii) "
                            "teams whose keys all appeared earlier (rolling) rise by >= 0.5 x the population rise.",
        estimate=dict(change_at_share_new0=dict(est=float(f0.change_EtoL_at_share_new0), se=float(f0.se_change),
                                                lo=float(f0.lo_change), hi=float(f0.hi_change)),
                      population_change=pop, ratio_i=float(f0.ratio_to_pop), ratio_i_lo=float(f0.ratio_lo),
                      ratio_i_hi=float(f0.ratio_hi),
                      ratio_i_vs_topic_adjusted_population_change=(float(f0.change_EtoL_at_share_new0) / adj_topic_delta
                                                                   if adj_topic_delta else None),
                      topic_adjusted_population_change=adj_topic_delta,
                      b_post_x_share_new=dict(est=float(f0.b_post_x_share_new), se=float(f0.se_post_x_share_new)),
                      variants=fe[["model", "change_EtoL_at_share_new0", "lo_change", "hi_change", "ratio_to_pop",
                                   "b_post_x_share_new", "se_post_x_share_new", "nobs"]].to_dict(orient="records"),
                      allprior_ratio_ii=ap, allprior_ratio_2023to2026=ap2326),
        p_one_sided=float(f0.p_change_le0), null="change at share_new = 0 <= 0",
        prediction_met=dict(part_i=bool(c_i), part_ii=bool(c_ii)), falsified=bool(h2c_fals),
        verdict="falsified" if h2c_fals else ("supported" if (c_i and c_ii) else
                                              ("partially_supported" if (c_i or c_ii) else "not_supported")))

    # ---------------- H2d ----------------
    sa = mk["stats"]["any"]
    p_h2d = bp(M["any::G_style_minus_topic"], lambda d: d <= 0)
    h2d_pred = 0.7 <= sa["slope_all"]["est"] and sa["G_style_minus_topic"]["est"] > 0
    h2d_fals = sa["slope_all"]["est"] < 0.7 or sa["G_style_minus_topic"]["hi"] < 0
    h2d = dict(
        id="H2d", statement="Style vs topic channel: across markers, within-stayer change regressed on population change "
                            "has slope ~1 (falsified if < 0.7); the generational increment share 1 - within/pop is "
                            "larger for style than for topic markers.",
        estimate=dict(n_style=mk["n_style"], n_topic=mk["n_topic"],
                      **{k: sa[k] for k in ["slope_all", "r_all", "slope0_style", "slope0_topic", "G_style", "G_topic",
                                            "G_style_minus_topic", "Gratio_style", "Gratio_topic",
                                            "Gratio_style_minus_topic", "nollm__slope_all", "nollm__G_style_minus_topic",
                                            "nonamefam__slope_all", "nonamefam__G_style", "nonamefam__G_style_minus_topic"]},
                      last_partition={k: mk["stats"]["last"][k] for k in ["slope_all", "G_style", "G_topic",
                                                                          "G_style_minus_topic"]},
                      first_partition={k: mk["stats"]["first"][k] for k in ["slope_all", "G_style", "G_topic",
                                                                            "G_style_minus_topic"]}),
        p_one_sided=p_h2d, null="G_style - G_topic <= 0", prediction_met=bool(h2d_pred), falsified=bool(h2d_fals),
        verdict="falsified" if h2d_fals else ("supported" if h2d_pred and sa["G_style_minus_topic"]["lo"] > 0
                                              else "partially_supported"))

    # ---------------- H2e ----------------
    he = ss["h2e"]["email_2018to2020"]
    ra_e, rc_e = he["name_primary"]["any"]["rho"], he["name_compound"]["any"]["rho"]
    p_h2e = bp(g("email_2018to2020|any|paper"), lambda d: d <= 0.3)
    h2e_pred = ra_e["est"] >= 0.5 and rc_e["est"] >= 0.5
    h2e_fals = ra_e["est"] < 0.3 or rc_e["est"] < 0.3
    h2e = dict(
        id="H2e", statement="Pre-LLM replication: with email keys, 2018 -> 2020, the NAME and colon (compound) rise is "
                            ">= 50% within stayers (any role primary).",
        estimate=dict(name_any=ra_e, compound_any=rc_e, name_last=he["name_primary"]["last"]["rho"],
                      name_first=he["name_primary"]["first"]["rho"], compound_last=he["name_compound"]["last"]["rho"],
                      compound_first=he["name_compound"]["first"]["rho"],
                      delta_name_any=he["name_primary"]["any"]["delta"],
                      delta_compound_any=he["name_compound"]["any"]["delta"],
                      two_year_windows_1718_to_1920=ss["h2e"]["email_1718to1920"],
                      counts=ss["h2e_counts"].get("email_2018to2020|any|paper")),
        p_one_sided=p_h2e, null="rho_any(NAME) <= 0.3", prediction_met=bool(h2e_pred), falsified=bool(h2e_fals),
        verdict="falsified" if h2e_fals else ("supported" if h2e_pred and ra_e["lo"] > 0.3 else "partially_supported"))

    hyps = [h2a, h2b, h2c, h2d, h2e]
    adj = holm({h["id"]: h["p_one_sided"] for h in hyps})
    for h in hyps:
        h["p_holm"] = adj[h["id"]]

    # ---------------- robustness ----------------
    rob = []
    for _, r in t21[t21.outcome.isin(["name_primary", "name_adj_topic", "name_adj_size"])].iterrows():
        rob.append(dict(spec=r.spec, outcome=r.outcome, rho=r3(r.rho), lo=r3(r.rho_lo), hi=r3(r.rho_hi),
                        delta=r3(r.delta), P_SE=r3(r.P_SE), P_SL=r3(r.P_SL), gap_NS_L=r3(r.gap_NS_L)))
    removal = rem[rem.frac.eq(0.2)].to_dict(orient="records")
    team_main = team[(team.window == "main") & (team.stat == "within_share")].to_dict(orient="records")

    # ---------------- supporting ----------------
    s1 = s21[(s21["rule"] == "union") & (s21["sample"] == "dest>=2024")].iloc[0]
    s1s = s21[(s21["rule"] == "strict") & (s21["sample"] == "dest>=2024")].iloc[0]
    s1pre = s21[(s21["rule"] == "union") & (s21["sample"] == "dest<=2023")].iloc[0]
    prim = s22[s22.model.str.startswith("placebo: clean, T 2023-25")].set_index("outcome")
    pil = s22[s22.model.str.startswith("placebo: clean, no topic FE")].set_index("outcome")
    support = dict(
        S2_1=dict(statement="Even among retitled resubmissions (destination >= 2024), NAME is not added on net, "
                            "against the population drift implied by the pairs' years.",
                  n_pairs=int(s1.n_pairs), mean_dNAME=float(s1.name_primary_mean_change),
                  se=float(s1.name_primary_se), adds=int(s1.name_primary_adds), drops=int(s1.name_primary_drops),
                  implied_drift=float(s1.name_primary_implied_drift),
                  change_minus_drift=float(s1.name_primary_change_minus_drift),
                  change_minus_drift_se=float(s1.name_primary_change_minus_drift_se),
                  p_change_minus_drift=float(s1.name_primary_p_change_minus_drift),
                  mde=float(s1.name_primary_mde),
                  samekey_other_papers_change=float(s1.samekey_other_papers_name_change),
                  samekey_other_papers_se=float(s1.samekey_other_papers_se),
                  samekey_pairs=int(s1.samekey_other_papers_pairs),
                  strict_rule=dict(n_pairs=int(s1s.n_pairs), mean_dNAME=float(s1s.name_primary_mean_change),
                                   se=float(s1s.name_primary_se), implied_drift=float(s1s.name_primary_implied_drift)),
                  pre2024_destinations=dict(n_pairs=int(s1pre.n_pairs), mean_dNAME=float(s1pre.name_primary_mean_change),
                                            se=float(s1pre.name_primary_se),
                                            implied_drift=float(s1pre.name_primary_implied_drift)),
                  compound=dict(mean=float(s1.name_compound_mean_change), se=float(s1.name_compound_se),
                                implied_drift=float(s1.name_compound_implied_drift)),
                  purity=sp["s2_1"]["info"]["purity"],
                  caveat="Pairs are selected on retitling (the export keeps one submission per family); transition "
                         "rates are not behaviour.",
                  verdict="supported" if (s1.name_primary_change_minus_drift + 1.96 * s1.name_primary_change_minus_drift_se < 0)
                  else "partially_supported"),
        S2_2=dict(statement="Future-tie placebo: past-collaborator exposure is no larger than future-collaborator "
                            "exposure in the clean sample (homophily, not tie contagion).",
                  primary={o: {k: float(prim.loc[o, k]) for k in ["b_expo_past", "se_expo_past", "b_expo_future",
                                                                   "se_expo_future", "past_minus_future", "se_diff",
                                                                   "mde_expo_past", "mde_diff", "nobs", "n_keys"]}
                           for o in prim.index},
                  pilot_spec_no_topic_fe={o: {k: float(pil.loc[o, k]) for k in ["b_expo_past", "se_expo_past",
                                                                                 "b_expo_future", "se_expo_future",
                                                                                 "past_minus_future", "se_diff"]}
                                          for o in pil.index},
                  verdict="supported" if prim.loc["name_primary", "past_minus_future"] + 1.96 * prim.loc["name_primary", "se_diff"] < 0
                  or prim.loc["name_primary", "past_minus_future"] <= 0 else "not_supported"))

    out = dict(
        direction="D2 Who carries the fashion: communal vs generational change (WP6)",
        plan="research/titles/docs/PLAN.md D2", windows=dict(E=list(P.E_WIN), L=list(P.L_WIN)),
        panel=info, n_boot=ss["n_boot"], hypotheses=hyps, holm_family=list(adj.keys()),
        main_decomposition_T2_1={part: main_[part] for part in ("last", "first", "any")},
        name_definitions=ss["name_defs"], compound=ss["compound_main"], variants=ss["variants"],
        team_types=team_main, removal_simulation=removal, ipw=ss["ipw"], alias=ss["alias"],
        trim=ss["trim_top1pct"], robustness_rho=rob, supporting=support,
        files=sorted(p.name for p in OUTDIR.iterdir() if p.is_file()))
    (OUTDIR / "results.json").write_text(json.dumps(out, indent=1, default=float))
    for h in hyps:
        print(h["id"], h["verdict"], "p=%.4f holm=%.4f" % (h["p_one_sided"], h["p_holm"]), h["prediction_met"],
              "falsified" if h["falsified"] else "")
    print("S2.1", support["S2_1"]["verdict"], "S2.2", support["S2_2"]["verdict"])


if __name__ == "__main__":
    main()
