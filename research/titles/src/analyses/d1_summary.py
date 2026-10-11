"""WP5 / D1 summary: merges its_results.json, content_cf.json, decompose.json (and refit_boot_R1.json if present)
into results.json with verdicts against the pre-registered falsification criteria and Holm over H1a-H1e;
draws F1.1, F1.2, F1.3 (PDF + PNG + CSV).

Run after d1_its, d1_content_cf (fit + summarise), d1_decompose:
    cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.d1_summary
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d1_content_cf as CF

OUTDIR = C.OUT / "d1_break"
B_BOOT = 2000


def _j(p):
    p = OUTDIR / p
    return json.loads(p.read_text()) if p.exists() else None


def pboot(p, B=B_BOOT):
    """Bootstrap p with the (k+1)/(B+1) floor."""
    return (p * B + 1) / (B + 1)


def holm(pvals: dict) -> dict:
    keys = sorted(pvals, key=lambda k: pvals[k])
    m = len(keys)
    out, running = {}, 0.0
    for i, k in enumerate(keys):
        adj = min(1.0, (m - i) * pvals[k])
        running = max(running, adj)
        out[k] = running
    return out


def main():
    its = _j("its_results.json")["H1a"]
    cf = _j("content_cf.json")
    dc = _j("decompose.json")
    rb = _j("refit_boot_R1.json")
    reps = cf["representations"]
    res = {"direction": "D1 The 2024 naming break: content, people, or tool?",
           "universe_n": 43482, "outcome_primary": "name_primary (NAME: coined lead before colon/spaced dash)"}

    # ---------------- H1a ----------------
    T11 = pd.read_csv(OUTDIR / "T1_1_its.csv")
    crit = its["criteria"]
    h1a_supported = all(crit.values())
    h1a = {"statement": "Dated 2024 slope break in a segmented logit on U; holds in NA pool and non-LLM subset; "
                        "sup-LR selects 2024/2025; placebo breaks 2020-22 null",
           "slope_change_OR_U": [its["primary"]["slope_change_OR"], its["primary"]["slope_change_OR_lo"],
                                 its["primary"]["slope_change_OR_hi"]],
           "slope_change_OR_NA": [its["NA_pool"]["slope_change_OR"], its["NA_pool"]["slope_change_OR_lo"],
                                  its["NA_pool"]["slope_change_OR_hi"]],
           "slope_change_OR_non_llm": [its["non_llm"]["slope_change_OR"], its["non_llm"]["slope_change_OR_lo"],
                                       its["non_llm"]["slope_change_OR_hi"]],
           "lpm_slope_change_pp_U": [its["primary"]["lpm_slope_change_pp"], its["primary"]["lpm_slope_change_pp_lo"],
                                     its["primary"]["lpm_slope_change_pp_hi"]],
           "pre_slope_OR_U": its["primary"]["pre_slope_OR"],
           "supLR_selected": its["supLR_selected_break"], "supLR_by_year": its["supLR_by_year"],
           "supLR_kink_only_selected": its.get("supLR_kink_only_selected_break"),
           "randomization_p": its["randomization_p_z"], "placebos": its["placebo_pre_data"],
           "year_deviation_U": its["year_deviation_U"], "criteria": crit,
           "p_one_sided": its["p_one_sided_primary"],
           "falsified": its["falsified"]}
    h1a["verdict"] = ("falsified" if its["falsified"] else ("supported" if h1a_supported else "partially_supported"))
    res["H1a"] = h1a

    # ---------------- H1b ----------------
    shares = {}
    for rep in CF.REP_INFO:
        for design in ["fixed", "rolling"]:
            e = reps.get(f"{rep}|U|primary|{design}", {})
            if e.get("status") != "done":
                shares[f"{rep}|{design}"] = {"status": "pending"}
                continue
            if design == "fixed":
                shares[f"{rep}|{design}"] = {"share": e["share_2026"], "ci": e["share_2026_ci"],
                                             "p_ge_0_6": e["p_share_2026_ge_0_6"], "auc": e["auc_mean"],
                                             "cal_slope": e["cal_slope_mean"]}
            else:
                shares[f"{rep}|{design}"] = {"share": e["content_share_post_steps"],
                                             "ci": e["content_share_post_steps_ci"], "p_ge_0_6": e["p_share_ge_0_6"],
                                             "auc": e["auc_mean"], "cal_slope": e["cal_slope_mean"]}
    masked = {k: v for k, v in shares.items() if k.split("|")[0] in CF.MASKED_REPS and v.get("status") != "pending"}
    pending = [k for k, v in shares.items() if k.split("|")[0] in CF.MASKED_REPS and v.get("status") == "pending"]
    in_band = all(0.20 <= v["share"] <= 0.50 for v in masked.values())
    none_gt60 = all(v["share"] < 0.60 for v in masked.values())
    p_h1b = pboot(max(v["p_ge_0_6"] for v in masked.values()))
    res["H1b"] = {"statement": "Content's share of the 2023->2026 rise in [0.20, 0.50] for every name-masked "
                               "representation; none >= 0.60",
                  "shares": shares, "masked_reps_evaluated": sorted(masked), "masked_reps_pending": pending,
                  "all_masked_in_0.20_0.50": in_band, "none_masked_ge_0.60": none_gt60,
                  "masked_range": [min(v["share"] for v in masked.values()), max(v["share"] for v in masked.values())],
                  "p_IUT_share_ge_0.60": p_h1b,
                  "verdict": ("falsified" if not none_gt60 else ("supported" if in_band else "partially_supported"))}

    # ---------------- H1c ----------------
    r1 = reps["R1|U|primary|rolling"]
    h1c = {"statement": "Acceleration of content-unexplained drift: mean(u_2024-26) - mean(u_2019-23) > 0, ratio >= 1.5",
           "u_pre": r1["u_pre"], "u_post": r1["u_post"], "diff": r1["diff"], "diff_ci_conditional": r1["diff_ci"],
           "ratio": r1["ratio"], "ratio_ci_conditional": r1["ratio_ci"],
           "content_share_post_steps": r1["content_share_post_steps"],
           "content_share_post_steps_ci": r1["content_share_post_steps_ci"],
           "by_year": r1["by_year"], "without_2019": r1["without_2019"], "excluding_2026": r1["excluding_2026"],
           "p_conditional": pboot(r1["p_diff_le0"])}
    if rb:
        h1c["refit_bootstrap"] = rb
        h1c["p_refit"] = (rb["p_diff_le0"] * rb["B"] + 1) / (rb["B"] + 1)
    p_h1c = max(h1c["p_conditional"], h1c.get("p_refit", 0))
    ci_lo = min(r1["diff_ci"][0], rb["diff_ci"][0]) if rb else r1["diff_ci"][0]
    h1c["p_used"] = p_h1c
    # replications across reps / pools / outcomes
    repl = {}
    for k, e in list(reps.items()) + list(cf["variants"].items()):
        if k.endswith("|rolling") and e.get("status") == "done":
            repl[k] = {"diff": e["diff"], "diff_ci": e["diff_ci"], "ratio": e["ratio"], "ratio_ci": e["ratio_ci"],
                       "u_pre": e["u_pre"], "u_post": e["u_post"], "content_share_post_steps": e["content_share_post_steps"]}
    h1c["replications"] = repl
    # exploratory: acceleration of unexplained drift outside fast-growing topic clusters (new-topic placebo split)
    ntp = cf["new_topic_placebo"]
    if "R1|rolling_pre_2019_23" in ntp and "by_year" in ntp["R1|rolling_pre_2019_23"]:
        by = {**ntp["R1|rolling_pre_2019_23"]["by_year"], **ntp["R1|rolling_post_2024_26"]["by_year"]}
        pre_e = [by[str(y)]["res_else"] for y in (2019, 2020, 2021, 2022, 2023)]
        post_e = [by[str(y)]["res_else"] for y in (2024, 2025, 2026)]
        pre_f = [by[str(y)]["res_fast"] for y in (2019, 2020, 2021, 2022, 2023) if by[str(y)]["res_fast"] is not None]
        post_f = [by[str(y)]["res_fast"] for y in (2024, 2025, 2026) if by[str(y)]["res_fast"] is not None]
        h1c["established_topics_only"] = {
            "u_pre": float(np.mean(pre_e)), "u_post": float(np.mean(post_e)),
            "diff": float(np.mean(post_e) - np.mean(pre_e)), "ratio": float(np.mean(post_e) / np.mean(pre_e)),
            "fast_growing_u_pre": float(np.mean(pre_f)), "fast_growing_u_post": float(np.mean(post_f)),
            "by_year": by,
            "note": "u_y averaged over papers outside topic100 clusters whose share grew >= 3x vs the training "
                    "window (exploratory split of the pre-registered new-topic placebo)"}
    fals = (r1["ratio"] < 1.2) or (ci_lo <= 0)
    h1c["verdict"] = "falsified" if fals else ("supported" if r1["ratio"] >= 1.5 else "partially_supported")
    res["H1c"] = h1c

    # ---------------- H1d ----------------
    dfl = dc["dfl"]["U|full (size x new x llm_topic)"]["2026"]
    sh = dc.get("shapley", {})
    h1d = {"statement": "DFL reweighting of 2024-26 to 2023 composition (size x newcomer x llm_topic) explains <= 30%",
           "dfl_full_2026": dfl, "dfl_all": dc["dfl"], "shapley": sh,
           "p_share_ge_0.5": pboot(dfl["p_share_ge_0_5"])}
    h1d["verdict"] = ("falsified" if dfl["share"] >= 0.5 else
                      ("supported" if dfl["share"] <= 0.30 else "partially_supported"))
    res["H1d"] = h1d

    # ---------------- H1e ----------------
    f0 = dc["f0_rise"]["F_d1"]["2026"]
    tool = dc["tool"]
    d = tool["delta_primary"]
    dname = tool["dNAME_2023_2026"]
    # one-sided p for tool share at A=0.39 >= 0.5  <=> delta >= 0.5*dname/0.39
    thr = 0.5 * dname / 0.39
    p_tool = float(stats.norm.sf((thr - d["delta"]) / d["se"]))
    p_f0 = pboot(f0["p_ratio_le_0_70"])
    ts39 = tool["tool_share_at_A"]["0.39"]
    crit_e = {"F0_rise_ge_0.85": f0["ratio_F0_all"] >= 0.85, "delta_le_5pp": d["delta"] <= 0.05,
              "tool_share_at_0.39_lt_0.25": ts39["share"] < 0.25}
    fals_e = (f0["ratio_F0_all"] < 0.70) or (ts39["share"] >= 0.5)
    res["H1e"] = {"statement": "Tool bounded: F=0 rise >= 85% of total; delta <= +5pp; max tool share at A_max "
                               "< 0.25", "f0_rise": dc["f0_rise"], "tool": tool, "criteria": crit_e,
                  "p_IUT": max(p_f0, p_tool), "p_F0_ratio_le_0.70": p_f0, "p_tool_share_ge_0.5": p_tool,
                  "verdict": "falsified" if fals_e else ("supported" if all(crit_e.values()) else "partially_supported")}
    d3 = None
    for cand in [C.OUT / "d3_register" / "results.json"]:
        if cand.exists():
            try:
                d3 = json.loads(cand.read_text())
            except Exception:
                d3 = None
    res["H1e"]["positive_control_D3"] = ("see outputs/d3_register/results.json (H3a)" if d3 else
                                         "D3 slot result not available at time of writing (computed by WP7)")

    # ---------------- Holm ----------------
    pv = {"H1a": h1a["p_one_sided"], "H1b": p_h1b, "H1c": p_h1c, "H1d": h1d["p_share_ge_0.5"], "H1e": res["H1e"]["p_IUT"]}
    adj = holm(pv)
    res["holm"] = {"family": "H1a-H1e", "raw_p": pv, "adjusted_p": adj,
                   "tests": {"H1a": "one-sided Wald, slope-change log OR <= 0 (U, primary spec)",
                             "H1b": "intersection-union: max over masked reps x designs of bootstrap P(share >= 0.60)",
                             "H1c": "bootstrap P(diff <= 0), max of conditional and refit bootstraps",
                             "H1d": "bootstrap P(DFL share 2026 >= 0.50)",
                             "H1e": "intersection-union of bootstrap P(F0 ratio <= 0.70) and one-sided Wald "
                                    "P(tool share at A=0.39 >= 0.50)"}}
    res["new_topic_placebo"] = cf["new_topic_placebo"]
    res["v4_leakage"] = cf["v4"]
    res["placebo_window"] = {k: {kk: v.get(kk) for kk in ["share_2021", "share_2022", "share_2023", "unexplained_2021",
                                                         "unexplained_2022", "unexplained_2023", "share_2023_ci",
                                                         "unexplained_2023_ci", "obs_anchor", "auc_mean"]}
                             for k, v in reps.items() if k.endswith("|placebo") and v.get("status") == "done"}
    res["its_table"] = T11.to_dict(orient="records")
    (OUTDIR / "results.json").write_text(json.dumps(res, indent=1, default=lambda x: float(x) if np.isscalar(x) else str(x)))
    print(json.dumps({k: res[k].get("verdict") for k in ["H1a", "H1b", "H1c", "H1d", "H1e"]}, indent=1))
    print(json.dumps(res["holm"], indent=1))
    figures(res, cf, dc)


# ------------------------------------------------------------------------------------------------
def figures(res, cf, dc):
    import matplotlib.pyplot as plt
    reps = cf["representations"]
    U = C.load_analysis_frame(feature_cols=["name_primary"], universe_cols=["submission_id", "year", "NA"])
    obs = U.groupby("year").name_primary.mean()
    obs_na = U[U.NA].groupby("year").name_primary.mean()

    # ---------- F1.1 ----------
    rows = []
    for k, e in reps.items():
        rep, pop, o, design = k.split("|")
        if e.get("status") != "done" or design == "rolling" or rep == "R1u":
            continue
        anchor = e["obs_anchor"]
        anchor_year = 2023 if design == "fixed" else 2020
        rows.append(dict(rep=rep, design=design, year=anchor_year, p_hat=anchor))
        for r in e["by_year"]:
            rows.append(dict(rep=rep, design=design, year=r["year"], p_hat=r["p_hat"]))
    CFp = pd.DataFrame(rows)
    fig, ax = C.new_fig("single", 3.0)
    ax.plot(obs.index, 100 * obs.values, "-o", color=C.color(0), ms=4.5, zorder=5)
    env_rows = []
    for design in ["placebo", "fixed"]:
        g = CFp[CFp.design == design]
        allv = g[g.rep.isin(["R1", "R2", "R3", "R4", "R5", "R6", "R6b"])].groupby("year").p_hat.agg(["min", "max"])
        msk = g[g.rep.isin(list(CF.MASKED_REPS))].groupby("year").p_hat.agg(["min", "max"])
        r1 = g[g.rep == "R1"].set_index("year").p_hat
        ax.fill_between(allv.index, 100 * allv["min"], 100 * allv["max"], color=C.color(1), alpha=0.18, lw=0)
        ax.fill_between(msk.index, 100 * msk["min"], 100 * msk["max"], color=C.color(1), alpha=0.45, lw=0)
        ax.plot(r1.index, 100 * r1.values, "--", color=C.color(1), lw=1.4)
        for yv in allv.index:
            env_rows.append(dict(design=design, year=yv, all_min=allv.loc[yv, "min"], all_max=allv.loc[yv, "max"],
                                 masked_min=msk.loc[yv, "min"] if yv in msk.index else np.nan,
                                 masked_max=msk.loc[yv, "max"] if yv in msk.index else np.nan,
                                 R1=r1.get(yv, np.nan), observed=obs.get(yv)))
    ax.set_xlim(2016.6, 2028.2)
    ax.set_ylim(0, 45)
    ax.set_ylabel("NAME titles (% of submissions)")
    ax.set_xticks(range(2017, 2027, 1), [f"'{y % 100:02d}" for y in range(2017, 2027)])
    C.label_end(ax, 2026, 100 * obs[2026], "observed", C.color(0), dx=0.3)
    fx = CFp[(CFp.design == "fixed") & (CFp.rep == "R1")].set_index("year").p_hat
    C.label_end(ax, 2026, 100 * fx[2026], "content\ncounterfactual\n(R1)", C.color(1), dx=0.3)
    ax.annotate("placebo window\n(train 2018-20)", (2021.5, 12.6), fontsize=6.5, color=C.TEXT2,
                ha="center", va="top")
    ax.annotate("fixed window\n(train 2021-23)", (2025.0, 16.0), fontsize=6.5, color=C.TEXT2, ha="center", va="top")
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    ax.legend(handles=[Patch(color=C.color(1), alpha=0.18, label="envelope R1-R6"),
                       Patch(color=C.color(1), alpha=0.45, label="name-masked (R1, R3, R5)"),
                       Line2D([], [], color=C.color(1), ls="--", lw=1.4, label="R1 (primary)")],
              loc="upper center", fontsize=6.5, handlelength=1.6, bbox_to_anchor=(0.5, -0.12), ncol=3,
              columnspacing=0.8)
    # inset: NA pool
    na_r1 = reps.get("R1|U|primary|fixed")
    va = cf["variants"].get("R1|NA|primary|fixed")
    vp = cf["variants"].get("R1|NA|primary|placebo")
    axin = ax.inset_axes([0.07, 0.56, 0.36, 0.38])
    axin.plot(obs_na.index, 100 * obs_na.values, "-", color=C.color(0), lw=1.4)
    inset_rows = []
    for v, anc in [(vp, 2020), (va, 2023)]:
        if v and v.get("status") == "done":
            xs = [anc] + [r["year"] for r in v["by_year"]]
            ys = [v["obs_anchor"]] + [r["p_hat"] for r in v["by_year"]]
            axin.plot(xs, 100 * np.array(ys), "--", color=C.color(1), lw=1.2)
            inset_rows += [dict(year=x, R1_NA_cf=y_) for x, y_ in zip(xs, ys)]
    axin.set_title("NA pool", fontsize=7, pad=2)
    axin.tick_params(labelsize=6, length=2)
    axin.set_xticks([2018, 2022, 2026], ["'18", "'22", "'26"])
    axin.set_ylim(0, 45)
    axin.grid(True, lw=0.4)
    data = pd.DataFrame(env_rows)
    obs_df = pd.DataFrame({"year": obs.index, "observed_U": obs.values, "observed_NA": obs_na.reindex(obs.index).values})
    C.save_fig(fig, "fig_F1_1_counterfactual", OUTDIR,
               data={"envelope": data, "observed": obs_df, "all_reps": CFp, "inset_NA_R1": pd.DataFrame(inset_rows)})

    # ---------- F1.2 ----------
    e = reps["R1|U|primary|rolling"]
    by = pd.DataFrame(e["by_year"]).set_index("year")
    uci = pd.DataFrame(e["u_year_ci"], index=["lo", "hi"]).T
    uci.index = uci.index.astype(int)
    cci = pd.DataFrame(e["content_step_year_ci"], index=["lo", "hi"]).T
    cci.index = cci.index.astype(int)
    fig, ax = C.new_fig("single", 2.8)
    x = by.index.to_numpy()
    w = 0.38
    ax.bar(x - w / 2, 100 * by.content_step, w, color=C.color(1), label="content step")
    ax.bar(x + w / 2, 100 * by.unexplained, w, color=C.color(0), label="unexplained (u)")
    ax.errorbar(x + w / 2, 100 * by.unexplained, yerr=[100 * (by.unexplained - uci.loc[x, "lo"]),
                                                       100 * (uci.loc[x, "hi"] - by.unexplained)],
                fmt="none", ecolor=C.TEXT2, lw=0.8)
    ax.errorbar(x - w / 2, 100 * by.content_step, yerr=[100 * (by.content_step - cci.loc[x, "lo"]),
                                                        100 * (cci.loc[x, "hi"] - by.content_step)],
                fmt="none", ecolor=C.TEXT2, lw=0.8)
    ax.plot(x, 100 * by.step, "o", color=C.TEXT, ms=4, label="observed step", zorder=5)
    ax.hlines(100 * e["u_pre"], 2018.6, 2023.4, color=C.color(0), lw=1.2, ls="--",
              label=f"mean u: {100 * e['u_pre']:.1f} pp (2019-23), {100 * e['u_post']:.1f} pp (2024-26)")
    ax.hlines(100 * e["u_post"], 2023.6, 2026.4, color=C.color(0), lw=1.2, ls="--")
    ax.axhline(0, color=C.TEXT2, lw=0.6)
    ax.axvline(2023.5, color=C.GREY, lw=0.8, ls=":")
    ax.set_xticks(x, [f"'{v % 100:02d}" for v in x])
    ax.set_ylabel("annual change in NAME share (pp)")
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.0), fontsize=6.8, ncol=2, handlelength=1.5,
              columnspacing=1.0)
    d12 = by[["obs", "obs_calib", "p_hat", "step", "content_step", "unexplained"]].copy()
    d12["u_lo"], d12["u_hi"] = uci.loc[x, "lo"].values, uci.loc[x, "hi"].values
    d12["content_lo"], d12["content_hi"] = cci.loc[x, "lo"].values, cci.loc[x, "hi"].values
    d12["u_pre_mean"], d12["u_post_mean"] = e["u_pre"], e["u_post"]
    C.save_fig(fig, "fig_F1_2_steps", OUTDIR, data=d12.reset_index())

    # ---------- F1.3 ----------
    sh = dc.get("shapley", {}).get("2026")
    dfl = dc["dfl"]["U|full (size x new x llm_topic)"]["2026"]
    tool = dc["tool"]
    rows = []
    if sh:
        rows.append(dict(component="content (masked abstract, R1)", share=sh["shapley_content_share"],
                         lo=sh["shapley_content_share_ci"][0], hi=sh["shapley_content_share_ci"][1],
                         alt=reps["R1|U|primary|fixed"]["share_2026"], alt_label="R1 alone (fixed window)"))
        rows.append(dict(component="team/newcomer composition", share=sh["shapley_people_share"],
                         lo=sh["shapley_people_share_ci"][0], hi=sh["shapley_people_share_ci"][1],
                         alt=dfl["share"], alt_label="DFL reweighting"))
        rows.append(dict(component="residual fashion", share=sh["residual_share"], lo=sh["residual_share_ci"][0],
                         hi=sh["residual_share_ci"][1], alt=np.nan, alt_label=""))
    t39 = tool["tool_share_at_A"]["0.39"]
    rows.append(dict(component="max. tool share (A=0.39)", share=t39["share"], lo=t39["lo"], hi=t39["hi"],
                     alt=tool["detectable_only_contribution"]["delta_x_dshareF_over_dNAME"],
                     alt_label="detectable fingerprints only"))
    D = pd.DataFrame(rows)
    fig, ax = C.new_fig("single", 2.3)
    yy = np.arange(len(D))[::-1]
    for i, (_, r) in enumerate(D.iterrows()):
        ax.barh(yy[i], 100 * r.share, color=C.color(i), height=0.6)
        ax.plot([100 * r.lo, 100 * r.hi], [yy[i], yy[i]], color=C.TEXT, lw=1.0)
        if np.isfinite(r.alt):
            ax.plot(100 * r.alt, yy[i], "D", color=C.TEXT, ms=4, mfc="white", zorder=5)
            ax.annotate(r.alt_label, (100 * r.alt, yy[i]), xytext=(-2, 6), textcoords="offset points", fontsize=6,
                        color=C.TEXT2, ha="left", va="bottom")
    ax.set_yticks(yy, D.component)
    ax.axvline(0, color=C.TEXT2, lw=0.6)
    ax.set_xlabel("share of the 2023-2026 NAME rise (%)")
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.annotate("bars: Shapley split (content, composition, residual) and tool bound; whiskers 95% CI;\n"
                "open diamonds: alternative estimates", (1.0, -0.36), xycoords="axes fraction", ha="right",
                fontsize=6, color=C.TEXT2)
    C.save_fig(fig, "fig_F1_3_decomposition", OUTDIR, data=D)
    plt.close("all")


if __name__ == "__main__":
    main()
