"""WP5 / D1 summary: merges its_results.json, content_cf.json, decompose.json, refit_boot_R1.{json,csv} and
refit_boot_fixed.json into results.json with verdicts against the pre-registered falsification criteria and Holm
over H1a-H1e; draws F1.1, F1.2, F1.3 (PDF + PNG + CSV).

Audit revision (see outputs/audit/d1/fix_log.md):
  * H1a confirmatory p = year-level random-effects meta-regression (t, 6 df); paper-level Wald and the
    randomization p are reported beside it (D1-C4, ID-1, REP-2).
  * H1c confirmatory CI/p = two-stage: refit paper bootstrap + year shocks. In the rolling design
    u_y = obs_y - obs_{y-1} - cs_y, so the pre/post contrast telescopes to an endpoint contrast of obs_2018,
    obs_2023 and obs_2026; year shocks e_y ~ N(0, (tau p_y (1 - p_y))^2) with tau the REML year-shock SD on the
    logit scale (d1_its) enter through those years (D1-C3, ID-3, REP-1).
  * H1d evaluated for each of 2024, 2025, 2026 with a fixed 2-year new-key lookback (D1-C6).
  * H1e tool share corrected for fingerprint misclassification and year-matched (D1-C5, ID-4, REP-5).
  * Labels: 'composition (declared keys)' instead of 'people'; 'unexplained residual' instead of 'fashion'.

Run after d1_its, d1_content_cf (fit + summarise + refit_boot), d1_decompose (fit + all + refit_boot):
    cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.d1_summary
"""
from __future__ import annotations

import json
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d1_content_cf as CF

OUTDIR = C.OUT / "d1_break"
B_BOOT = 2000
# one colour per quantity across F1.1-F1.3 (REP-15)
COL_OBS, COL_CONTENT, COL_UNEXPL, COL_COMP, COL_TOOL = C.TEXT, C.color(1), C.color(0), C.GREY, C.color(3)


def _j(p):
    p = OUTDIR / p
    return json.loads(p.read_text()) if p.exists() else None


def pboot(p, B=B_BOOT):
    """Bootstrap p with the (k+1)/(B+1) floor."""
    return (p * B + 1) / (B + 1)


def clean(o):
    """Recursively convert NaN/inf to None and numpy scalars to Python types (strict JSON)."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def positive_control_d3() -> dict:
    """PLAN D1 'positive control link' (integration pass): D3's H3a slot break and H3d slot uplift, read from
    outputs/d3_register/. The H3d rows are fitted with two fingerprints: F_any = F24 (>= 1 RARE21 word) | F26 |
    title typography (D3's primary) and F_d1 = F24 (>= 2 RARE21 words) | F26 | title typography (D1's tool-bound
    fingerprint). They differ only in the F24 threshold, which is what the contrast isolates. Only the F_d1 row
    speaks to the sensitivity of D1's bound. The reading is generated from the significance flags (integration
    pass 2), so a re-run of D3 cannot leave a stale 'not significant' in results.json, the Fig. 2 caption or the
    ledger."""
    d3 = C.OUT / "d3_register"
    sig_p, res_p = d3 / "signature_models.csv", d3 / "results.json"
    if not (sig_p.exists() and res_p.exists()):
        return {"status": "PENDING: outputs/d3_register/ does not exist (D3 not yet run)"}
    S = pd.read_csv(sig_p)
    r3 = json.loads(res_p.read_text())
    h3a = next(h for h in r3["hypotheses"] if h["id"] == "H3a")["estimates"]["pooled_slots_post"]

    def row(x):
        s = S[(S["x"] == x) & (S["controls"] == "none") & S["label"].str.contains(
            "primary" if x == "F_any" else "F_d1", regex=False)].iloc[0]
        return {"OR_slot": round(float(s.OR_slot), 4), "OR_slot_ci": [round(float(s.OR_slot_lo), 4),
                                                                    round(float(s.OR_slot_hi), 4)],
                "p_one_OR_slot_le1": float(s.p_one_OR_slot_le1),
                "OR_name_population": round(float(s.OR_name_pop), 4),
                "OR_name_population_ci": [round(float(s.OR_name_pop_lo), 4), round(float(s.OR_name_pop_hi), 4)],
                "ratio_population": round(float(s.ratio_pop), 4),
                "ratio_population_ci": [round(float(s.ratio_pop_lo), 4), round(float(s.ratio_pop_hi), 4)],
                "n_slot_rows": int(s.n_slot_rows), "n_F1_slot_rows": int(s.n_F1)}
    fd1, fany = row("F_d1"), row("F_any")
    validated = fd1["OR_slot_ci"][0] > 1
    any_sig = fany["OR_slot_ci"][0] > 1

    def sig(flag):
        return "CI excludes 1" if flag else "not significant"
    conclusion = ("The positive control therefore supports the sensitivity of F_d1 for lexical LLM traces in titles "
                  "(it does not test the delta*A model or the misclassification assumptions)." if validated else
                  "The positive control therefore does not validate the sensitivity of F_d1, and the D1 tool "
                  "estimate is not validated by a positive control on its own fingerprint.")
    return {"status": "reported (D3 audited outputs)",
            "H3a_slot_break_post_OR": [h3a["OR"], h3a["lo"], h3a["hi"]],
            "H3d_slot_uplift_F_d1": fd1, "H3d_slot_uplift_F_any": fany,
            "validates_F_d1_bound": bool(validated), "F_any_slot_uplift_significant": bool(any_sig),
            "fingerprints": "F_any = F24 (>= 1 RARE21 word) | F26 | title typography; F_d1 differs only in "
                            "requiring >= 2 RARE21 words",
            "reading": ("LLM-favoured slot openers rose from 2024 (H3a, pooled post OR "
                        f"{h3a['OR']:.2f} [{h3a['lo']:.2f}, {h3a['hi']:.2f}]), so the title-level design detects an "
                        "LLM-era lexical shift. With D1's own fingerprint F_d1 the slot uplift is "
                        f"OR {fd1['OR_slot']:.2f} [{fd1['OR_slot_ci'][0]:.2f}, {fd1['OR_slot_ci'][1]:.2f}] "
                        f"({sig(validated)}); with F_any (the same fingerprint with a 1-word F24 threshold) it is "
                        f"{fany['OR_slot']:.2f} [{fany['OR_slot_ci'][0]:.2f}, {fany['OR_slot_ci'][1]:.2f}] "
                        f"({sig(any_sig)}). " + conclusion)}


def holm(pvals: dict) -> dict:
    keys = sorted(pvals, key=lambda k: pvals[k])
    m = len(keys)
    out, running = {}, 0.0
    for i, k in enumerate(keys):
        adj = min(1.0, (m - i) * pvals[k])
        running = max(running, adj)
        out[k] = running
    return out


def telescoping_weights(pre, post) -> dict:
    """diff = mean_post u - mean_pre u = (obs_{post[-1]} - obs_{post[0]-1}) / |post| - (obs_{pre[-1]} -
    obs_{pre[0]-1}) / |pre| - (content-step means); returns the weight of each year's observed share."""
    w = defaultdict(float)
    w[post[-1]] += 1 / len(post); w[post[0] - 1] -= 1 / len(post)
    w[pre[-1]] -= 1 / len(pre); w[pre[0] - 1] += 1 / len(pre)
    return {k: v for k, v in w.items() if abs(v) > 1e-12}


def shock_sd(weights: dict, shares: dict, tau_logit: float) -> float:
    return float(np.sqrt(sum((w * tau_logit * shares[y] * (1 - shares[y])) ** 2 for y, w in weights.items())))


def obs_by_year(entry) -> dict:
    by = pd.DataFrame(entry["by_year"]).set_index("year")
    o = by.obs.to_dict()
    o[int(by.index.min()) - 1] = float(by.obs_calib.iloc[0])
    return {int(k): float(v) for k, v in o.items()}


def two_stage_refit(csv_path, tau_logit, pre=CF.PRE_Y, post=CF.POST_Y, M=200, seed=5) -> dict:
    """Refit bootstrap draws (papers within year, models refitted) + independent year shocks on the telescoped
    endpoint years. Percentile CI; p = (#{diff* <= 0} + 1) / (N + 1)."""
    D = pd.read_csv(csv_path)
    u = {y: (D[f"obs_{y}"] - D[f"phat_{y}"]).to_numpy() for y in range(2019, 2027)}
    up = np.mean([u[y] for y in pre], axis=0)
    uq = np.mean([u[y] for y in post], axis=0)
    shares = {y: float(D[f"obs_{y}"].mean()) for y in range(2019, 2027)}
    shares[2018] = float(D["obscal_2019"].mean())
    rng = np.random.default_rng(seed)
    yrs_needed = sorted({post[-1], post[0] - 1, pre[-1], pre[0] - 1})
    E = {y: rng.normal(0, tau_logit * shares[y] * (1 - shares[y]), size=(len(D), M)) for y in yrs_needed}
    up_s = up[:, None] + (E[pre[-1]] - E[pre[0] - 1]) / len(pre)
    uq_s = uq[:, None] + (E[post[-1]] - E[post[0] - 1]) / len(post)
    diff = (uq_s - up_s).ravel()
    ratio = (uq_s / up_s).ravel()
    w = telescoping_weights(pre, post)
    return {"B_refit": int(len(D)), "M_shocks_per_draw": M, "tau_logit": tau_logit,
            "sd_diff_year_shocks": shock_sd(w, shares, tau_logit), "sd_diff_refit": float(np.std(uq - up, ddof=1)),
            "sd_diff_total": float(np.std(diff, ddof=1)), "diff_ci": CF.ci(diff), "ratio_ci": CF.ci(ratio),
            "p_diff_le0": float((np.sum(diff <= 0) + 1) / (len(diff) + 1)),
            "p_ratio_lt_1_5": float(np.mean(ratio < 1.5)), "p_ratio_lt_1_2": float(np.mean(ratio < 1.2)),
            "telescoping_weights": {int(k): v for k, v in w.items()}}


def year_robust_normal(entry, tau_logit, pre=CF.PRE_Y, post=CF.POST_Y) -> dict:
    """Normal approximation for replications that only have the conditional bootstrap SE."""
    shares = obs_by_year(entry)
    w = telescoping_weights(pre, post)
    sdy = shock_sd(w, shares, tau_logit)
    se = float(np.sqrt(entry["diff_se"] ** 2 + sdy ** 2)) if entry.get("diff_se") is not None else np.nan
    d = entry["diff"]
    return {"sd_year_shocks": sdy, "se_total": se, "ci": [d - 1.96 * se, d + 1.96 * se],
            "p_one_sided": float(stats.norm.sf(d / se))}


def main():
    its_all = _j("its_results.json")["H1a"]
    its = its_all
    cf = _j("content_cf.json")
    dc = _j("decompose.json")
    rb = _j("refit_boot_R1.json")
    rbf = _j("refit_boot_fixed.json")
    reps = cf["representations"]
    yl = its["year_level"]
    res = {"direction": "D1 The naming acceleration (pre-registered as 'the 2024 naming break'): content, "
                        "composition, or tool?",
           "universe_n": 43482, "dropped_rows_by_year": {2017: 1, 2018: 5, 2019: 7, 2020: 1, 2021: 4, 2022: 0,
                                                         2023: 0, 2024: 1, 2025: 7, 2026: 8},
           "outcome_primary": "name_primary (NAME: coined lead before colon/spaced dash)"}

    # ---------------- H1a ----------------
    T11 = pd.read_csv(OUTDIR / "T1_1_its.csv", keep_default_na=False, na_values=[""])
    crit = its["criteria"]
    yU, yNA = yl["U"]["re_logit"], yl["NA pool"]["re_logit"]
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
           "lpm_pre_slope_pp_U": its["primary"]["lpm_pre_slope_pp"],
           "pre_slope_OR_U": its["primary"]["pre_slope_OR"],
           "year_level_U": {"OR": [yU["OR"], yU["OR_lo"], yU["OR_hi"]], "p_one_sided_t6": yU["p_one_sided_t"],
                            "tau_logit": yU["tau_year_shock"]},
           "year_level_NA": {"OR": [yNA["OR"], yNA["OR_lo"], yNA["OR_hi"]], "p_one_sided_t6": yNA["p_one_sided_t"],
                             "tau_logit": yNA["tau_year_shock"]},
           "year_level_all": yl,
           "supLR_selected": its["supLR_selected_break"], "supLR_by_year": its["supLR_by_year"],
           "supLR_kink_only_selected": its.get("supLR_kink_only_selected_break"),
           "supLR_kink_only_note": "post hoc robustness scan (deviation 2)",
           "randomization_p": its["randomization_p_z"], "placebos": its["placebo_pre_data"],
           "year_deviation_U": its["year_deviation_U"], "criteria": crit,
           "p_one_sided_paper_level": its["p_one_sided_paper_level_wald"],
           "p_one_sided_year_level": its["p_one_sided_year_level"],
           "p_used": its["p_one_sided_year_level"],
           "falsified": its["falsified"]}
    h1a["verdict"] = "falsified" if its["falsified"] else (
        "supported" if all(crit.values()) else "partially_supported")
    h1a["verdict_note"] = ("not falsified (NA pool CI excludes 1 at paper and year level; no placebo as large); "
                           "sup-LR selects 2023; on U the year-level CI includes 1; excluding 2026 the slope change "
                           "is null; a dated 2024 break is not distinguishable from a convex trend or a 2023 break")
    res["H1a"] = h1a

    # ---------------- H1b ----------------
    shares = {}
    for rep in CF.REP_INFO:
        for design in ["fixed", "rolling", "placebo"]:
            e = reps.get(f"{rep}|U|primary|{design}", {})
            if e.get("status") != "done":
                shares[f"{rep}|{design}"] = {"status": "pending"}
                continue
            if design == "fixed":
                v = {"share": e["share_2026"], "ci": e["share_2026_ci"], "p_ge_0_6": e["p_share_2026_ge_0_6"]}
            elif design == "rolling":
                v = {"share": e["content_share_post_steps"], "ci": e["content_share_post_steps_ci"],
                     "p_ge_0_6": e["p_share_ge_0_6"]}
            else:
                v = {"share": e["share_2023"], "ci": e["share_2023_ci"], "p_ge_0_6": e["p_share_2023_ge_0_6"]}
            v.update(auc=e["auc_mean"], cal_slope=e["cal_slope_mean"], ci_type="conditional bootstrap (models fixed)")
            if "slope_recal" in e:
                sr = e["slope_recal"]
                v["share_slope_recal"] = (sr.get("share_2026") if design == "fixed" else
                                          sr.get("content_share_post_steps") if design == "rolling" else sr.get("share_2023"))
                v["slope_recal_mean_b"] = e.get("slope_recal_mean_b")
            shares[f"{rep}|{design}"] = v
    if rb:
        shares["R1|rolling"]["ci_refit"] = rb["content_share_post_steps_ci"]
        shares["R1|rolling"]["p_ge_0_6_refit"] = rb["p_share_ge_0_6"]
    if rbf:
        shares["R1|fixed"]["ci_refit"] = rbf["by_year"]["2026"]["R1_share_ci"]
        shares["R1|fixed"]["p_ge_0_6_refit"] = rbf["by_year"]["2026"]["p_R1_share_ge_0_6"]
    pre_reg = {k: v for k, v in shares.items() if k.split("|")[0] in CF.MASKED_REPS and k.split("|")[1] in
               ("fixed", "rolling") and v.get("status") != "pending"}
    yfe = {k: v for k, v in shares.items() if k.split("|")[0] in CF.YFE_REPS and k.split("|")[1] in
           ("fixed", "rolling") and v.get("status") != "pending"}
    pending = [k for k, v in shares.items() if k.split("|")[0] in CF.MASKED_REPS and v.get("status") == "pending"]
    in_band = all(0.20 <= v["share"] <= 0.50 for v in pre_reg.values())
    none_gt60 = all(v["share"] < 0.60 for v in pre_reg.values())
    p_list = [v["p_ge_0_6"] for v in pre_reg.values()]
    p_h1b = pboot(max(p_list))
    if rb:
        p_h1b = max(p_h1b, (rb["p_share_ge_0_6"] * rb["B"] + 1) / (rb["B"] + 1))
    sr_vals = [v.get("share_slope_recal") for k, v in pre_reg.items() if v.get("share_slope_recal") is not None]
    all_vals = [v["share"] for v in list(pre_reg.values()) + list(yfe.values())] + sr_vals
    res["H1b"] = {"statement": "Content's share of the 2023->2026 rise in [0.20, 0.50] for every name-masked "
                               "representation; none >= 0.60",
                  "shares": shares, "masked_reps_evaluated": sorted(pre_reg), "masked_reps_pending": pending,
                  "all_masked_in_0.20_0.50": in_band, "none_masked_ge_0.60": none_gt60,
                  "masked_range_preregistered": [min(v["share"] for v in pre_reg.values()),
                                                 max(v["share"] for v in pre_reg.values())],
                  "masked_range_year_fe": [min(v["share"] for v in yfe.values()), max(v["share"] for v in yfe.values())]
                  if yfe else None,
                  "masked_range_slope_recal": [min(sr_vals), max(sr_vals)] if sr_vals else None,
                  "honest_range_all_specs": [min(all_vals), max(all_vals)],
                  "rolling_ci_contains_0.60": {k: bool(v["ci"][0] <= 0.60 <= v["ci"][1]) for k, v in pre_reg.items()
                                               if k.endswith("rolling")},
                  "p_IUT_share_ge_0.60": p_h1b,
                  "p_note": "p tests the falsification boundary (share >= 0.60), not the prediction (share <= 0.50)",
                  "verdict": ("falsified" if not none_gt60 else ("supported" if in_band else "partially_supported"))}
    res["H1b"]["verdict_note"] = (
        "pre-registered spec with consistent (fold-ensemble) calibration: no masked share reaches 0.60 (not "
        "falsified), but the rolling shares exceed the predicted [0.20, 0.50] band, 0.60 lies inside every rolling "
        "CI, and intercept+slope recalibration puts R1/R5 rolling above 0.60; 'content is a minority' is not "
        "established")

    # ---------------- H1c ----------------
    r1 = reps["R1|U|primary|rolling"]
    tauU = yU["tau_year_shock"]
    taus = {"U": tauU, "NA": yNA["tau_year_shock"], "non_llm": yl["non-LLM subset"]["re_logit"]["tau_year_shock"]}
    tau_pp = yl["U"]["re_lpm"]["tau_year_shock"]
    h1c = {"statement": "Acceleration of content-unexplained drift: mean(u_2024-26) - mean(u_2019-23) > 0, ratio >= 1.5",
           "u_pre": r1["u_pre"], "u_post": r1["u_post"], "diff": r1["diff"], "diff_ci_conditional": r1["diff_ci"],
           "ratio": r1["ratio"], "ratio_ci_conditional": r1["ratio_ci"],
           "p_ratio_lt_1_5_conditional": r1["p_ratio_lt_1_5"],
           "content_share_post_steps": r1["content_share_post_steps"],
           "content_share_post_steps_ci": r1["content_share_post_steps_ci"],
           "by_year": r1["by_year"], "without_2019": r1["without_2019"], "excluding_2026": r1["excluding_2026"],
           "p_conditional": pboot(r1["p_diff_le0"]), "year_permutation": r1.get("year_permutation"),
           "telescoping_identity": "diff = (obs_2026 - obs_2023 - sum cs_2024-26)/3 - (obs_2023 - obs_2018 - sum "
                                   "cs_2019-23)/5: an endpoint contrast; obs_2023 enters with weight -8/15"}
    acc = {"step_pre_mean": r1["step_pre_mean"], "step_post_mean": r1["step_post_mean"],
           "content_step_pre_mean": r1["content_step_pre_mean"], "content_step_post_mean": r1["content_step_post_mean"]}
    acc["step_acceleration"] = acc["step_post_mean"] - acc["step_pre_mean"]
    acc["content_acceleration"] = acc["content_step_post_mean"] - acc["content_step_pre_mean"]
    acc["unexplained_acceleration"] = r1["diff"]
    acc["content_fraction_of_acceleration"] = acc["content_acceleration"] / acc["step_acceleration"]
    h1c["acceleration_decomposition"] = acc
    if rb:
        h1c["refit_bootstrap"] = rb
        h1c["p_refit"] = (rb["p_diff_le0"] * rb["B"] + 1) / (rb["B"] + 1)
        ts = two_stage_refit(OUTDIR / "refit_boot_R1.csv", tauU)
        w = telescoping_weights(CF.PRE_Y, CF.POST_Y)
        sd_lpm = tau_pp * float(np.sqrt(sum(v ** 2 for v in w.values())))
        se_lpm = float(np.sqrt(rb["diff_se"] ** 2 + sd_lpm ** 2))
        h1c["year_level_two_stage"] = ts
        h1c["year_level_two_stage_lpm_tau"] = {"tau_pp": 100 * tau_pp, "sd_diff_year_shocks": sd_lpm,
                                               "se_total": se_lpm,
                                               "ci_normal": [r1["diff"] - 1.96 * se_lpm, r1["diff"] + 1.96 * se_lpm],
                                               "p_one_sided": float(stats.norm.sf(r1["diff"] / se_lpm))}
        # two-stage for the 'excluding 2026' and 'without 2019' contrasts
        h1c["year_level_two_stage_excluding_2026"] = two_stage_refit(OUTDIR / "refit_boot_R1.csv", tauU,
                                                                     post=(2024, 2025))
        h1c["year_level_two_stage_without_2019"] = two_stage_refit(OUTDIR / "refit_boot_R1.csv", tauU,
                                                                   pre=(2020, 2021, 2022, 2023))
    p_paper = max(h1c["p_conditional"], h1c.get("p_refit", 0))
    ci_lo_paper = min(r1["diff_ci"][0], rb["diff_ci"][0]) if rb else r1["diff_ci"][0]
    h1c["p_paper_level"] = p_paper
    p_year = h1c["year_level_two_stage"]["p_diff_le0"] if rb else np.nan
    ci_year = h1c["year_level_two_stage"]["diff_ci"] if rb else [np.nan, np.nan]
    h1c["p_used"] = p_year
    # replications across reps / pools / outcomes, with year-shock-inflated normal CIs
    repl = {}
    for k, e in list(reps.items()) + list(cf["variants"].items()):
        if k.endswith("|rolling") and e.get("status") == "done":
            pop = k.split("|")[1]
            yr = year_robust_normal(e, taus.get(pop, tauU))
            repl[k] = {"diff": e["diff"], "diff_ci": e["diff_ci"], "ratio": e["ratio"], "ratio_ci": e["ratio_ci"],
                       "u_pre": e["u_pre"], "u_post": e["u_post"], "content_share_post_steps": e["content_share_post_steps"],
                       "diff_ci_year_robust": yr["ci"], "p_year_robust": yr["p_one_sided"],
                       "p_perm": (e.get("year_permutation") or {}).get("p_perm_one_sided")}
    h1c["replications"] = repl
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
    fals_paper = (r1["ratio"] < 1.2) or (ci_lo_paper <= 0)
    fals_year = (r1["ratio"] < 1.2) or (ci_year[0] <= 0)
    h1c["falsification_rule_met_paper_level"] = bool(fals_paper)
    h1c["falsification_rule_met_year_level"] = bool(fals_year)
    if fals_paper:
        h1c["verdict"] = "falsified"
    elif fals_year:
        h1c["verdict"] = "not_established_year_level"
    else:
        h1c["verdict"] = "supported" if r1["ratio"] >= 1.5 else "partially_supported"
    res["H1c"] = h1c

    # ---------------- H1d ----------------
    dflU = dc["dfl"]["U|full (size x new x llm_topic)"]
    sh = dc.get("shapley", {})
    per_year = {y: {"share": dflU[str(y)]["share"], "ci": dflU[str(y)]["share_ci"],
                    "p_ge_0_3": dflU[str(y)]["p_share_ge_0_3"], "p_ge_0_5": dflU[str(y)]["p_share_ge_0_5"]}
                for y in (2024, 2025, 2026)}
    h1d = {"statement": "DFL reweighting of 2024-26 to 2023 composition (size x new keys x llm_topic) explains <= 30%",
           "new_key_definition": "share of declared keys not seen in y-2..y-1 (fixed lookback)",
           "dfl_full_by_year": per_year, "dfl_full_2026": dflU["2026"], "dfl_all": dc["dfl"], "shapley": sh,
           "shapley_refit_ci": (rbf or {}).get("by_year"),
           "p_share_ge_0.5": pboot(max(v["p_ge_0_5"] for v in per_year.values()))}
    all_le_30 = all(v["share"] <= 0.30 for v in per_year.values())
    any_ge_50 = any(v["share"] >= 0.50 for v in per_year.values())
    h1d["verdict"] = "falsified" if any_ge_50 else ("supported" if all_le_30 else "partially_supported")
    h1d["p_used"] = h1d["p_share_ge_0.5"]
    res["H1d"] = h1d

    # ---------------- H1e ----------------
    f0 = dc["f0_rise"]["F_d1"]["2026"]
    tool = dc["tool"]
    d = tool["delta_primary"]
    d26 = tool["delta_2026"]
    dname = tool["dNAME_2023_2026"]
    c39 = tool["tool_share_at_A_corrected_2026_delta"]["0.39"]
    k39 = c39["k"]
    thr = 0.5 * dname * k39 / 0.39          # delta_2026 needed for a corrected tool share of 0.5 at A = 0.39
    p_tool = float(stats.norm.sf((thr - d26["delta"]) / d26["se"]))
    p_f0 = pboot(f0["p_ratio_le_0_70"])
    naive39 = tool["tool_share_at_A_naive"]["0.39"]
    crit_e = {"F0_rise_ge_0.85": f0["ratio_F0_all"] >= 0.85, "delta_le_5pp": d["delta"] <= 0.05,
              "tool_share_at_0.39_lt_0.25": c39["share"] < 0.25}
    fals_e = (f0["ratio_F0_all"] < 0.70) or (c39["share"] >= 0.5)
    D = pd.read_csv(OUTDIR / "tool_delta_models.csv")
    T13 = pd.read_csv(OUTDIR / "T1_3_tool_bound.csv")
    res["H1e"] = {"statement": "Tool bounded: F=0 rise >= 85% of total; delta <= +5pp; max tool share at A_max "
                               "< 0.25", "f0_rise": dc["f0_rise"], "tool": tool, "criteria": crit_e,
                  "tool_share_0.39_corrected_2026": c39, "tool_share_0.39_naive_preregistered": naive39,
                  "criterion_i_power": {"min_F1_gap_for_ratio_below_0.85": f0["min_F1_gap_for_ratio_below_0.85"],
                                        "min_F1_gap_for_ratio_below_0.70": f0["min_F1_gap_for_ratio_below_0.70"],
                                        "max_possible_F1_gap": f0["max_possible_F1_gap"]},
                  "p_IUT": max(p_f0, p_tool), "p_F0_ratio_le_0.70": p_f0, "p_tool_share_ge_0.5": p_tool,
                  "verdict": "falsified" if fals_e else ("supported" if all(crit_e.values()) else "partially_supported"),
                  "verdict_note": "criteria met for the pre-registered fingerprint after the misclassification "
                                  "correction; the bound is assumption-dependent (linear delta*A, nondifferential "
                                  "misclassification, homogeneous uplift, no spillover) and title-level markers "
                                  "give larger associations"}
    res["H1e"]["positive_control_D3"] = pc_d3 = positive_control_d3()
    if "validates_F_d1_bound" in pc_d3:   # wording follows the computed flag (integration pass 2)
        res["H1e"]["verdict_note"] += ("; the D3 positive control supports the sensitivity of D1's own fingerprint "
                                       "F_d1 (slot uplift OR CI excludes 1)" if pc_d3["validates_F_d1_bound"] else
                                       "; the D3 positive control does not validate the bound on D1's own "
                                       "fingerprint F_d1 (slot uplift OR CI includes 1)")
    else:
        res["H1e"]["verdict_note"] += "; the D3 positive control is PENDING (run D3, then d1_summary again)"
    res["H1e"]["p_used"] = res["H1e"]["p_IUT"]

    # ---------------- Holm ----------------
    pv = {"H1a": h1a["p_used"], "H1b": p_h1b, "H1c": h1c["p_used"], "H1d": h1d["p_used"], "H1e": res["H1e"]["p_IUT"]}
    pv_paper = dict(pv, H1a=h1a["p_one_sided_paper_level"], H1c=h1c["p_paper_level"])
    pv_rand = dict(pv, H1a=h1a["randomization_p"])
    res["holm"] = {"family": "H1a-H1e", "raw_p": pv, "adjusted_p": holm(pv),
                   "alternative_paper_level": {"raw_p": pv_paper, "adjusted_p": holm(pv_paper),
                                               "note": "H1a cluster-Wald and H1c paper bootstrap (first version)"},
                   "alternative_H1a_randomization": {"raw_p": pv_rand, "adjusted_p": holm(pv_rand),
                                                     "note": "H1a randomization p over break years 2019-25 (min 1/7)"},
                   "tests": {"H1a": "one-sided t(6), slope change in the REML random-effects meta-regression on "
                                    "adjusted logit year effects (U)",
                             "H1b": "intersection-union: max over masked reps x designs of bootstrap P(share >= 0.60) "
                                    "(tests the falsification boundary, not the <= 0.50 prediction)",
                             "H1c": "two-stage P(diff <= 0): refit paper bootstrap + year shocks (tau from H1a)",
                             "H1d": "intersection-union over 2024-26 of bootstrap P(DFL share >= 0.50) (tests the "
                                    "falsification boundary; prediction is <= 0.30)",
                             "H1e": "intersection-union of bootstrap P(F0 ratio <= 0.70) and one-sided Wald "
                                    "P(corrected tool share at A=0.39 >= 0.50)"}}
    adj = res["holm"]["adjusted_p"]
    for hk in ["H1a", "H1b", "H1c", "H1d", "H1e"]:
        res[hk]["holm_adjusted_p"] = adj[hk]
    # H1c: 'supported' requires the year-level falsification rule not to be met AND the Holm-adjusted year-level p
    # below 0.05 (audit D1-C3 / ID-3 / REP-1)
    if res["H1c"]["verdict"] == "supported" and adj["H1c"] >= 0.05:
        res["H1c"]["verdict"] = "not_established_year_level"
    res["H1c"]["verdict_note"] = (
        "point estimate positive under every content specification; R1 two-stage year-level CI "
        f"[{100 * ci_year[0]:.2f}, {100 * ci_year[1]:.2f}] pp, raw p {p_year:.3f}, Holm-adjusted p {adj['H1c']:.3f}; "
        "year-label permutation p and the year-robust CIs of R3, the NA pool, the non-LLM subset, strict NAME and "
        "the excluding-2026 contrast do not exclude 0")
    res["H1a"]["verdict_note"] += f"; Holm-adjusted year-level p {adj['H1a']:.3f}"
    res["new_topic_placebo"] = cf["new_topic_placebo"]
    res["v4_leakage"] = cf["v4"]
    res["placebo_window"] = {k: {kk: v.get(kk) for kk in ["share_2021", "share_2022", "share_2023", "unexplained_2021",
                                                         "unexplained_2022", "unexplained_2023", "share_2023_ci",
                                                         "unexplained_2023_ci", "obs_anchor", "auc_mean"]}
                             for k, v in reps.items() if k.endswith("|placebo") and v.get("status") == "done"}
    res["its_table"] = T11.to_dict(orient="records")
    res["H1a"]["break_scan"] = pd.read_csv(OUTDIR / "its_break_scan.csv").to_dict(orient="records")
    res["H1a"]["year_deviation_all"] = pd.read_csv(OUTDIR / "its_year_deviation.csv", keep_default_na=False,
                                                   na_values=[""]).to_dict(orient="records")
    res["H1e"]["delta_models"] = D.to_dict(orient="records")
    res["H1e"]["tool_bound_table_T1_3"] = T13.to_dict(orient="records")
    res["T1_2_representations"] = pd.read_csv(OUTDIR / "T1_2_representations.csv").to_dict(orient="records")
    res["content_variants"] = {k: {kk: v.get(kk) for kk in ["share_2024", "share_2025", "share_2026", "share_2026_ci",
                                                           "content_share_post_steps", "content_share_post_steps_ci",
                                                           "diff", "diff_ci", "ratio", "ratio_ci", "auc_mean",
                                                           "share_2023", "share_2023_ci"]}
                               for k, v in cf["variants"].items() if v.get("status") == "done"}
    res["deviations_from_plan"] = [
        "Pilot ITS 1.28/yr was for colon (compound) titles; NAME estimated as pre-registered (all 4 definitions reported)",
        "Added kink-only sup-LR scan as robustness next to the pre-specified level+slope scan (post hoc)",
        "H1c paper bootstrap implemented as conditional (B=2000) and refit (B=300) versions; added year-label "
        "permutation and Welch tests",
        "C grids for R2 (keywords) and R6/R6b (one-hot) widened after the first fit hit the lower grid edge",
        "Cross-fitted intercept recalibration also applied in fixed (to 2023) and placebo (to 2020) windows",
        "R2 treats each normalised keyword phrase as one token",
        "R5 removes the 6 frozen move n-grams by token-subsequence match",
        "DFL newcomer bin (.5,1) read as (.5,1]; keyless rows dropped",
        "F for D1 = f24_2 | f26 | title_typo (the >=2 RARE21 variant per D3 note); A_max=0.39 taken from PLAN",
        "R3 covers 2018-26 only (2019 rolling window trains on 2018)",
        "Exploratory diagnostics added: R1u, R1n, R1@0.5, established-topics split of u, 3-year cumulative comparison",
        "Extra script d1_summary.py for merging, Holm and figures",
        "AUDIT: test rows predicted with the CV fold models that calibrate the intercept (fold ensemble) [D1-C1]",
        "AUDIT: year-FE content models (R1yfe/R3yfe/R5yfe) and intercept+slope recalibration added as "
        "sensitivities [D1-C2, ID-5, REP-9]",
        "AUDIT: H1a and H1c confirmatory inference moved to year level (random-effects meta-regression; two-stage "
        "refit bootstrap + year shocks) [D1-C3, D1-C4, ID-1, ID-3]",
        "AUDIT: new-key share with a fixed 2-year lookback; H1d evaluated for 2024, 2025 and 2026 [D1-C6]",
        "AUDIT: tool share corrected for fingerprint misclassification and year-matched; A = 1 not identified "
        "[D1-C5, ID-4]",
        "AUDIT: new-topic placebo uses per-year absolute residuals and recalibrates inside the bootstrap [D1-C7]",
        "AUDIT: R2 restricted to papers with keywords [D1-C8]",
        "AUDIT: refit bootstrap added for the fixed-window R1, P and R1P fits (Shapley) [D1-C9]"]
    (OUTDIR / "results.json").write_text(json.dumps(clean(res), indent=1, allow_nan=False,
                                                    default=lambda x: float(x) if np.isscalar(x) else str(x)))
    print(json.dumps({k: res[k].get("verdict") for k in ["H1a", "H1b", "H1c", "H1d", "H1e"]}, indent=1))
    print(json.dumps(clean(res["holm"]["adjusted_p"]), indent=1))
    figures(res, cf, dc)


# ------------------------------------------------------------------------------------------------
def figures(res, cf, dc):
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    reps = cf["representations"]
    U = C.load_analysis_frame(feature_cols=["name_primary"], universe_cols=["submission_id", "year", "NA"])
    obs = U.groupby("year").name_primary.mean()
    obs_na = U[U.NA].groupby("year").name_primary.mean()

    # ---------- F1.1 ----------
    rows = []
    for k, e in reps.items():
        rep, pop, o, design = k.split("|")
        if e.get("status") != "done" or design == "rolling" or rep in ("R1u", "R1n", "R1@0.5"):
            continue
        anchor = e["obs_anchor"]
        anchor_year = 2023 if design == "fixed" else 2020
        rows.append(dict(rep=rep, design=design, year=anchor_year, p_hat=anchor))
        for r in e["by_year"]:
            rows.append(dict(rep=rep, design=design, year=r["year"], p_hat=r["p_hat"]))
    CFp = pd.DataFrame(rows)
    roll = pd.DataFrame(reps["R1|U|primary|rolling"]["by_year"]).set_index("year")
    o23 = float(roll.loc[2024, "obs_calib"])
    roll_cum = pd.Series([o23] + list(o23 + roll.loc[[2024, 2025, 2026], "content_step"].cumsum()),
                         index=[2023, 2024, 2025, 2026])
    fig, ax = C.new_fig("single", 3.1)
    ax.plot(obs.index, 100 * obs.values, "-o", color=COL_OBS, ms=4.0, lw=1.4, zorder=5)
    env_rows = []
    masked_set = list(CF.MASKED_REPS) + list(CF.YFE_REPS)
    for design in ["placebo", "fixed"]:
        g = CFp[CFp.design == design]
        allv = g[g.rep.isin(["R1", "R2", "R3", "R4", "R5", "R6", "R6b"] + list(CF.YFE_REPS))].groupby("year").p_hat.agg(["min", "max"])
        msk = g[g.rep.isin(masked_set)].groupby("year").p_hat.agg(["min", "max"])
        r1 = g[g.rep == "R1"].set_index("year").p_hat
        ax.fill_between(allv.index, 100 * allv["min"], 100 * allv["max"], color=COL_CONTENT, alpha=0.15, lw=0)
        ax.fill_between(msk.index, 100 * msk["min"], 100 * msk["max"], color=COL_CONTENT, alpha=0.40, lw=0)
        ax.plot(r1.index, 100 * r1.values, "--", color=COL_CONTENT, lw=1.4)
        for yv in allv.index:
            env_rows.append(dict(design=design, year=yv, all_min=allv.loc[yv, "min"], all_max=allv.loc[yv, "max"],
                                 masked_min=msk.loc[yv, "min"] if yv in msk.index else np.nan,
                                 masked_max=msk.loc[yv, "max"] if yv in msk.index else np.nan,
                                 R1=r1.get(yv, np.nan), observed=obs.get(yv)))
    ax.plot(roll_cum.index, 100 * roll_cum.values, ":", marker="s", ms=3.2, color=COL_CONTENT, lw=1.4)
    for yv in roll_cum.index:
        env_rows.append(dict(design="rolling (cumulative one-step R1)", year=yv, R1=roll_cum[yv], observed=obs.get(yv)))
    ax.set_xlim(2016.6, 2028.4)
    ax.set_ylim(0, 45)
    ax.set_ylabel("NAME titles (% of submissions)")
    ax.set_xticks(range(2017, 2027, 1), [f"'{y % 100:02d}" for y in range(2017, 2027)])
    C.label_end(ax, 2026, 100 * obs[2026], "observed", COL_OBS, dx=0.3)
    fx = CFp[(CFp.design == "fixed") & (CFp.rep == "R1")].set_index("year").p_hat
    C.label_end(ax, 2026, 100 * roll_cum[2026], "rolling", COL_CONTENT, dx=0.3)
    C.label_end(ax, 2026, 100 * fx[2026], "fixed", COL_CONTENT, dx=0.3)
    ax.annotate("placebo window\n(train 2018-20)", (2021.5, 12.6), fontsize=6.5, color=C.TEXT2, ha="center", va="top")
    ax.annotate("fixed window\n(train 2021-23)", (2025.0, 16.0), fontsize=6.5, color=C.TEXT2, ha="center", va="top")
    ax.legend(handles=[Line2D([], [], color=COL_OBS, marker="o", ms=3.5, lw=1.4, label="observed"),
                       Line2D([], [], color=COL_CONTENT, ls="--", lw=1.4, label="R1 content cf., fixed window"),
                       Line2D([], [], color=COL_CONTENT, ls=":", marker="s", ms=3, lw=1.4,
                              label="R1, rolling: 2023 + cumulative content steps"),
                       Patch(color=COL_CONTENT, alpha=0.15, label="range R1-R6 (not a CI)"),
                       Patch(color=COL_CONTENT, alpha=0.40, label="range, name-masked reps (not a CI)")],
              loc="upper center", fontsize=6.0, handlelength=1.8, bbox_to_anchor=(0.5, -0.12), ncol=2,
              columnspacing=0.8)
    va = cf["variants"].get("R1|NA|primary|fixed")
    vp = cf["variants"].get("R1|NA|primary|placebo")
    axin = ax.inset_axes([0.07, 0.56, 0.36, 0.38])
    axin.plot(obs_na.index, 100 * obs_na.values, "-", color=COL_OBS, lw=1.4)
    inset_rows = []
    for v, anc in [(vp, 2020), (va, 2023)]:
        if v and v.get("status") == "done":
            xs = [anc] + [r["year"] for r in v["by_year"]]
            ys = [v["obs_anchor"]] + [r["p_hat"] for r in v["by_year"]]
            axin.plot(xs, 100 * np.array(ys), "--", color=COL_CONTENT, lw=1.2)
            inset_rows += [dict(year=x, R1_NA_cf=y_) for x, y_ in zip(xs, ys)]
    axin.set_title("NA pool", fontsize=7, pad=2)
    axin.tick_params(labelsize=6, length=2)
    axin.set_xticks([2018, 2022, 2026], ["'18", "'22", "'26"])
    axin.set_ylim(0, 45)
    axin.grid(True, lw=0.4)
    data = pd.DataFrame(env_rows)
    obs_df = pd.DataFrame({"year": obs.index, "observed_U": obs.values, "observed_NApool": obs_na.reindex(obs.index).values})
    C.save_fig(fig, "fig_F1_1_counterfactual", OUTDIR,
               data={"envelope": data, "observed": obs_df, "all_reps": CFp, "inset_NA_R1": pd.DataFrame(inset_rows)})

    # ---------- F1.2 ----------
    e = reps["R1|U|primary|rolling"]
    by = pd.DataFrame(e["by_year"]).set_index("year")
    uci = pd.DataFrame(e["u_year_ci"], index=["lo", "hi"]).T
    uci.index = uci.index.astype(int)
    cci = pd.DataFrame(e["content_step_year_ci"], index=["lo", "hi"]).T
    cci.index = cci.index.astype(int)
    fig, ax = C.new_fig("single", 3.0)
    x = by.index.to_numpy()
    w = 0.38
    ax.bar(x - w / 2, 100 * by.content_step, w, color=COL_CONTENT, label="content step")
    ax.bar(x + w / 2, 100 * by.unexplained, w, color=COL_UNEXPL, label="unexplained (u)")
    ax.errorbar(x + w / 2, 100 * by.unexplained, yerr=[100 * (by.unexplained - uci.loc[x, "lo"]),
                                                       100 * (uci.loc[x, "hi"] - by.unexplained)],
                fmt="none", ecolor=C.TEXT2, lw=0.8)
    ax.errorbar(x - w / 2, 100 * by.content_step, yerr=[100 * (by.content_step - cci.loc[x, "lo"]),
                                                        100 * (cci.loc[x, "hi"] - by.content_step)],
                fmt="none", ecolor=C.TEXT2, lw=0.8)
    ax.plot(x, 100 * by.step, "o", color=COL_OBS, ms=4, label="observed step", zorder=5)
    cpre, cpost = e["content_step_pre_mean"], e["content_step_post_mean"]
    ax.hlines(100 * e["u_pre"], 2018.6, 2023.4, color=COL_UNEXPL, lw=1.2, ls="--",
              label=f"mean u {100 * e['u_pre']:.1f} -> {100 * e['u_post']:.1f} pp")
    ax.hlines(100 * e["u_post"], 2023.6, 2026.4, color=COL_UNEXPL, lw=1.2, ls="--")
    ax.hlines(100 * cpre, 2018.6, 2023.4, color=COL_CONTENT, lw=1.2, ls=":",
              label=f"mean content step {100 * cpre:.1f} -> {100 * cpost:.1f} pp")
    ax.hlines(100 * cpost, 2023.6, 2026.4, color=COL_CONTENT, lw=1.2, ls=":")
    ax.axhline(0, color=C.TEXT2, lw=0.6)
    ax.axvline(2023.5, color=C.GREY, lw=0.8, ls=":")
    ax.set_xticks(x, [f"'{v % 100:02d}" for v in x])
    ax.set_ylabel("annual change in NAME share (pp)")
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.0), fontsize=6.3, ncol=2, handlelength=1.5, columnspacing=1.0)
    ax.annotate("whiskers: 95% conditional paper-bootstrap CI (models fixed; year shocks not included)",
                (0.0, -0.17), xycoords="axes fraction", fontsize=5.8, color=C.TEXT2, ha="left", va="top")
    d12 = by[["obs", "obs_calib", "p_hat", "step", "content_step", "unexplained"]].copy()
    d12["u_lo"], d12["u_hi"] = uci.loc[x, "lo"].values, uci.loc[x, "hi"].values
    d12["content_lo"], d12["content_hi"] = cci.loc[x, "lo"].values, cci.loc[x, "hi"].values
    d12["u_pre_mean"], d12["u_post_mean"] = e["u_pre"], e["u_post"]
    d12["content_pre_mean"], d12["content_post_mean"] = cpre, cpost
    d12["ci_type"] = "conditional paper bootstrap (models fixed)"
    C.save_fig(fig, "fig_F1_2_steps", OUTDIR, data=d12.reset_index())

    # ---------- F1.3 ----------
    sh = dc.get("shapley", {}).get("2026")
    dfl = dc["dfl"]["U|full (size x new x llm_topic)"]["2026"]
    tool = dc["tool"]
    rows = []
    if sh:
        rows.append(dict(component="content (masked abstract, R1)", share=sh["shapley_content_share"],
                         lo=sh["shapley_content_share_ci"][0], hi=sh["shapley_content_share_ci"][1],
                         alt=reps["R1|U|primary|fixed"]["share_2026"], alt_label="R1 alone, fixed",
                         alt2=reps["R1|U|primary|rolling"]["content_share_post_steps"], alt2_label="R1, rolling",
                         color=COL_CONTENT))
        rows.append(dict(component="composition: size x new keys x llm_topic", share=sh["shapley_composition_share"],
                         lo=sh["shapley_composition_share_ci"][0], hi=sh["shapley_composition_share_ci"][1],
                         alt=dfl["share"], alt_label="DFL", alt2=np.nan, alt2_label="", color=COL_COMP))
        rows.append(dict(component="residual (unexplained; incl. new-topic naming)", share=sh["residual_share"],
                         lo=sh["residual_share_ci"][0], hi=sh["residual_share_ci"][1], alt=np.nan, alt_label="",
                         alt2=np.nan, alt2_label="", color=COL_UNEXPL))
    t39 = tool["tool_share_at_A_corrected_2026_delta"]["0.39"]
    rows.append(dict(component="tool, corrected (A=0.39; in residual)", share=t39["share"], lo=t39["lo"], hi=t39["hi"],
                     alt=tool["tool_share_at_A_naive"]["0.39"]["share"], alt_label="uncorrected", alt2=np.nan,
                     alt2_label="", color=COL_TOOL))
    D = pd.DataFrame(rows)
    fig, ax = C.new_fig("single", 2.5)
    yy = np.array([3.6, 2.6, 1.6, 0.0])[:len(D)] if len(D) == 4 else np.arange(len(D))[::-1].astype(float)
    for i, (_, r) in enumerate(D.iterrows()):
        ax.barh(yy[i], 100 * r.share, color=r.color, height=0.5)
        ax.plot([100 * r.lo, 100 * r.hi], [yy[i], yy[i]], color=C.TEXT, lw=1.0)
        if np.isfinite(r.alt):
            ax.plot(100 * r.alt, yy[i], "D", color=C.TEXT, ms=4, mfc="white", zorder=5)
            ax.annotate(r.alt_label, (100 * r.alt, yy[i] + 0.27), fontsize=5.8, color=C.TEXT2, ha="center", va="bottom")
        if np.isfinite(r.alt2):
            ax.plot(100 * r.alt2, yy[i], "^", color=C.TEXT, ms=4.5, zorder=5)
            ax.annotate(r.alt2_label, (100 * r.alt2, yy[i] + 0.27), fontsize=5.8, color=C.TEXT2, ha="center",
                        va="bottom")
    if len(D) == 4:
        ax.axhline(0.8, color=C.GREY, lw=0.8, ls="--")
        ax.annotate("not additive: the tool share is part of the residual", (1.0, 0.86), xycoords=("axes fraction", "data"),
                    ha="right", va="bottom", fontsize=5.8, color=C.TEXT2)
    ax.set_yticks(yy, D.component)
    ax.axvline(0, color=C.TEXT2, lw=0.6)
    ax.set_xlabel("share of the 2023-2026 NAME rise (%)")
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0, labelsize=6.5)
    ax.set_ylim(-0.6, 4.2)
    ax.annotate("bars: fixed-window Shapley split (lower end of the content bracket) and the misclassification-\n"
                "corrected tool share; whiskers: 95% conditional bootstrap CI; markers: alternative estimators",
                (1.0, -0.33), xycoords="axes fraction", ha="right", fontsize=5.6, color=C.TEXT2)
    C.save_fig(fig, "fig_F1_3_decomposition", OUTDIR, data=D.drop(columns=["color"]))
    plt.close("all")


if __name__ == "__main__":
    main()
