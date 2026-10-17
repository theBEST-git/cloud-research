"""Pre-specified joint analyses (prereg section 6, 'applying to all questions') and the integration table behind the
title-writing guide (outputs/cites/GUIDE.md, outputs/cites/fig_title_guide.png).

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here). The primary estimates and Holm
p-values are read from outputs/cites/primary.json and never recomputed for reporting.

What this module does
  1. Joint model (pre-specified secondary, no multiplicity claim): ONE model with all 8 primary features,
       y ~ G1 + G2 + G3 + G4 + G5a + G5b + G6a + G6b + log team size + log abstract words + 20 abstract PCs | year^topic50,
     SEs clustered by topic50 (core._fit; the base controls of core.controls, the 8 features in place of the
     feature-specific extra controls, which are all among the 8).
  2. LLM-topic heterogeneity (pre-specified secondary, no multiplicity claim), one model per feature:
       y ~ F x llm_topic + F + llm_topic + core.controls(F) | year^topic50 (interaction = ratio of multipliers),
     and the same model re-parametrised as F_in_llm + F_in_nonllm + llm_topic (group-specific slopes).
  3. Diagnostic (not pre-registered; integration): placebo calibration of the R1 matched-pairs procedure for G1 and
     G2, the two questions whose analyses did not run it. Same procedure as the G3/G4 audits
     (cites.audit_g3g4: random pseudo-treated papers without the feature, same per-year counts, R1 pairing; 200 draws).
     The pre-registered R1 and the verdicts are unchanged by this; it only says how to read raw R1.
  4. Guide table: per feature, frozen primary + Holm p, pre-registered R1 / R2, the verdict (read from each G's
     results.json and re-derived with core.verdict as a check), the placebo-calibrated R1 (diagnostic; read from the
     G3-G6 results.json, computed here for G1/G2), joint-model and LLM-heterogeneity estimates.
  5. Figure outputs/cites/fig_title_guide.{png,pdf,csv}.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.joint
Writes outputs/cites/joint_results.json and outputs/cites/fig_title_guide.{png,pdf,csv}.
"""
from __future__ import annotations

import json
import warnings

import numpy as np
import pandas as pd

from analyses import _core as C
from cites import audit_g3g4, core

warnings.filterwarnings("ignore")

PRESPEC = "pre-specified secondary (prereg section 6; no multiplicity claim)"
DIAG = "diagnostic (not pre-registered; added at integration)"
FEATS = list(core.FEATURES)
BASE = [c for c in core.controls(FEATS[0]) if c not in core.FEATURES]   # log team, log abstract words, 20 PCs
GROUP = {"G1_name": "G1", "G2_assertive": "G2", "G3_question": "G3", "G4_llm_words": "G4",
         "G5a_length5": "G5", "G5b_informative": "G5", "G6a_meme": "G6", "G6b_tentative": "G6"}
PLAIN = {  # plain-language labels for the guide figure
    "G1_name": "Leads with a method name (NAME: ...)",
    "G2_assertive": "States the finding (assertive verb)",
    "G3_question": "Is a question",
    "G4_llm_words": "Uses LLM-favoured words (enhancing, ...)",
    "G5a_length5": "Longer title (per +5 words)",
    "G5b_informative": "Closer in meaning to the abstract (per SD)",
    "G6a_meme": "Meme template (All You Need, ...)",
    "G6b_tentative": "Tentative framing (Towards, Rethinking, ...)",
}
# Confidence statements from the adversarial audits (outputs/cites/G*/RESULTS.md, 'Confidence in the advice').
AUDIT_CONFIDENCE = {
    "G1_name": "sign high; size medium",
    "G2_assertive": "verdict high; advice medium",
    "G3_question": "'no advice either way' high; direction low-medium",
    "G4_llm_words": "'neither establish nor rule out' high; direction medium-low",
    "G5a_length5": "high that no reliable association is shown",
    "G5b_informative": "sign high; size medium",
    "G6a_meme": "low-medium",
    "G6b_tentative": "medium that any association is small",
}


def _j(g: str) -> dict:
    return json.load(open(core.OUT / g / "results.json"))


def _pct(r: dict) -> dict:
    return {k: r.get(k) for k in ("pct", "lo", "hi", "p", "n", "n_pairs") if r.get(k) is not None}


# --------------------------------------------------------------------------------------------
# 1-2. pre-specified joint analyses
# --------------------------------------------------------------------------------------------
def joint_model(df: pd.DataFrame) -> dict:
    out = {"label": PRESPEC,
           "model": "y ~ all 8 primary features + log_authors + log_abs_words + 20 abstract PCs | year^topic50, CRV1 topic50",
           "features": {}}
    ns = set()
    for f in FEATS:
        r = core._fit(df, "y", f, BASE + [g for g in FEATS if g != f])
        if f in core.BINARY:
            r["n_with"] = int(df[f].sum())
        out["features"][f] = r
        ns.add(r["n"])
    assert len(ns) == 1, "the 8 coefficients must come from the same estimation sample"
    out["note"] = ("Each coefficient compares papers with the feature with papers that share all other 7 title features; "
                   "for G2/G3 this means 'plain' titles (G2 excludes questions by construction, and named titles go "
                   "with more citations), so the reference group differs from the primary's.")
    out["feature_correlations"] = df[FEATS].corr().round(3).to_dict()
    return out


def llm_heterogeneity(df: pd.DataFrame) -> dict:
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(int)
    out = {"label": PRESPEC, "n_llm_topic_papers": int(d.llm.sum()), "features": {},
           "model": "per feature: y ~ F x llm_topic + F + llm_topic + core.controls(F) | year^topic50, CRV1 topic50; "
                    "group slopes from the same model re-parametrised as F_in_llm + F_in_nonllm + llm_topic"}
    for f in FEATS:
        d["F_in_llm"], d["F_in_nonllm"] = d[f] * d.llm, d[f] * (1 - d.llm)
        llm = core._fit(d, "y", "F_in_llm", core.controls(f, ["F_in_nonllm", "llm"]))
        non = core._fit(d, "y", "F_in_nonllm", core.controls(f, ["F_in_llm", "llm"]))
        inter = core._fit(d, "y", "F_in_llm", core.controls(f, [f, "llm"]))
        if f in core.BINARY:
            llm["n_with"], non["n_with"] = int(d.F_in_llm.sum()), int(d.F_in_nonllm.sum())
        out["features"][f] = {
            "llm_topic_papers": llm, "non_llm_topic_papers": non,
            "interaction": {"b": inter["b"], "se": inter["se"], "p": inter["p"], "ratio": float(np.exp(inter["b"])),
                            "ratio_lo": float(np.exp(inter["b"] - 1.96 * inter["se"])),
                            "ratio_hi": float(np.exp(inter["b"] + 1.96 * inter["se"]))}}
    ps = {f: v["interaction"]["p"] for f, v in out["features"].items()}
    out["descriptive_holm_over_8_interactions"] = {
        "label": DIAG, "p_holm": core.holm(ps),
        "note": "descriptive only: the prereg makes no multiplicity claim for secondary analyses"}
    return out


# --------------------------------------------------------------------------------------------
# 3. diagnostic: R1 placebo calibration for G1 and G2
# --------------------------------------------------------------------------------------------
def r1_placebo(df: pd.DataFrame, feats=("G1_name", "G2_assertive"), n_rep: int = 200, seed: int = 0) -> dict:
    d = df.reset_index(drop=True)
    E = audit_g3g4._embedding(d)
    years, yv = d.year.to_numpy(), d.y.to_numpy()
    out = {"label": DIAG,
           "method": "cites.audit_g3g4 placebo (as in the G3/G4 audits): pseudo-treated = random papers without the "
                     "feature, same per-year counts, matched with the R1 rule to the remaining papers without it; "
                     "adjusted = exp(observed mean log diff - placebo mean) - 1, CI from the placebo SD"}
    for f in feats:
        tr = (d[f] == 1).to_numpy()
        t, c = audit_g3g4._pairs(E, years, tr, ~tr)
        obs = float((yv[t] - yv[c]).mean())
        st = audit_g3g4._placebo(E, years, yv, tr, ~tr, n_rep, seed)
        core_r1 = _j(GROUP[f])["robustness"]["R1_matched_pairs"]
        out[f] = {**audit_g3g4._calibrate(obs, st), "n_pairs": int(len(t)), "seed": seed,
                  "reproduces_core_R1": bool(len(t) == core_r1["n_pairs"] and abs(np.exp(obs) - 1 - core_r1["pct"]) < 1e-9)}
        # sensitivity: within-year permutation of the feature over ALL papers, so the pseudo-treated and control pools
        # have exactly the real sizes (matters for G1, where 24.5% of papers are treated and the default placebo
        # matches against a control pool reduced by the pseudo-treated draw)
        counts = pd.Series(years[tr]).value_counts()
        rng = np.random.default_rng(seed + 7)
        sp = []
        for _ in range(n_rep):
            ptr = np.zeros(len(years), bool)
            for y, k in counts.items():
                ptr[rng.choice(np.where(years == y)[0], int(k), replace=False)] = True
            a, b = audit_g3g4._pairs(E, years, ptr, ~ptr)
            sp.append(float((yv[a] - yv[b]).mean()))
        out[f]["sensitivity_within_year_permutation"] = {
            **audit_g3g4._calibrate(obs, np.array(sp)), "seed": seed + 7,
            "note": "pseudo-treated = random papers (any status), same per-year counts; controls = all other papers"}
    return out


# --------------------------------------------------------------------------------------------
# 4. guide table (reads each G's audited results.json)
# --------------------------------------------------------------------------------------------
def _stored(f: str) -> dict:
    """Pre-registered R1/R2 and verdict, and the placebo-calibrated R1 (diagnostic), from the G results files."""
    g = GROUP[f]
    r = _j(g)
    if g == "G5":
        x = r["features"][f]
        rob, verdict = x["robustness"], x["verdict"]
        n0 = r["diagnostics_not_preregistered"]["g_audit"]["r1_null"][f]
        cal = {**n0["placebo_adjusted"], "null_mean_pct": n0["null"]["pct_at_mean"],
               "contrast_units": n0["mean_feature_contrast_in_pairs"],
               "source": f"G5/results.json diagnostics_not_preregistered.g_audit.r1_null.{f}"}
    elif g == "G6":
        rob, verdict = r["robustness"][f], r["verdict"][f]
        x = r["diagnostics_not_preregistered"]["f_r1_calibration"][f]
        cal = {**x["placebo_adjusted"], "null_mean_pct": x["placebo"]["pct_at_mean"],
               "source": f"G6/results.json diagnostics_not_preregistered.f_r1_calibration.{f}"}
    else:
        rob, verdict = r["robustness"], r["verdict"]
        cal = None
        if g == "G3":
            x = r["diagnostics"]["f_audit_r1_calibration"]["placebo"]
            cal = {"pct": x["adjusted_pct"], "lo": x["adjusted_lo"], "hi": x["adjusted_hi"], "null_mean_pct": x["null_mean_pct"],
                   "source": "G3/results.json diagnostics.f_audit_r1_calibration.placebo"}
        elif g == "G4":
            x = r["diagnostics_not_preregistered"]["d_r1_calibration_and_family_pairs"]["G4_llm_words"]
            cal = {"pct": x["placebo_adjusted_pct"], "lo": x["placebo_adjusted_lo"], "hi": x["placebo_adjusted_hi"],
                   "null_mean_pct": x["placebo"]["pct_at_mean"],
                   "source": "G4/results.json diagnostics_not_preregistered.d_r1_calibration_and_family_pairs.G4_llm_words"}
    return {"R1": rob["R1_matched_pairs"], "R2": rob["R2_ppml_counts"], "verdict": verdict, "R1_calibrated": cal}


def guide_table(joint: dict, het: dict, plac: dict) -> dict:
    frozen = json.load(open(core.OUT / "primary.json"))["primary"]
    rows = {}
    for f in FEATS:
        p = frozen[f]
        s = _stored(f)
        v_check = core.verdict(p, {"R1_matched_pairs": s["R1"], "R2_ppml_counts": s["R2"]}, p["p_holm"])
        assert v_check == s["verdict"], (f, v_check, s["verdict"])
        cal = s["R1_calibrated"]
        if cal is None:   # G1, G2: computed here
            x = plac[f]
            cal = {"pct": x["adjusted_pct"], "lo": x["adjusted_lo"], "hi": x["adjusted_hi"], "null_mean_pct": x["null_mean_pct"],
                   "source": "joint_results.json r1_placebo_G1_G2"}
        cal["label"] = DIAG if f in ("G1_name", "G2_assertive") else "diagnostic (not pre-registered; from the G audit)"
        row = {"question": GROUP[f], "label": core.FEATURES[f], "plain_label": PLAIN[f],
               "unit": {"G5a_length5": "per +5 words", "G5b_informative": "per +1 SD within year"}.get(f, "with vs without"),
               "primary": {k: p[k] for k in ("pct", "lo", "hi", "p", "n")} | ({"n_with": p["n_with"]} if "n_with" in p else {}),
               "p_holm": p["p_holm"], "R1_matched_pairs_prereg": _pct(s["R1"]), "R2_ppml_prereg": _pct(s["R2"]),
               "verdict": s["verdict"], "verdict_recomputed_with_core_verdict": v_check,
               "R1_placebo_calibrated": cal,
               "joint_model": _pct(joint["features"][f]),
               "llm_topic_interaction_ratio": {k: het["features"][f]["interaction"][k] for k in ("ratio", "ratio_lo", "ratio_hi", "p")},
               "audit_confidence": AUDIT_CONFIDENCE[f]}
        if f in ("G5a_length5", "G5b_informative"):
            k = cal["contrast_units"]
            row["R1_per_unit_rescaled"] = {
                "label": "diagnostic (not pre-registered): R1 compares top with bottom within-year tercile; rescaled to the "
                         f"primary's unit by exp(log(1 + R1) / {k:.3f}) - 1, {k:.3f} = mean feature contrast in the pairs",
                "contrast_units": k,
                "raw": {q: float(np.exp(np.log1p(s["R1"][q]) / k) - 1) for q in ("pct", "lo", "hi")},
                "calibrated": {q: float(np.exp(np.log1p(cal[q]) / k) - 1) for q in ("pct", "lo", "hi")}}
        rows[f] = row
    return rows


# --------------------------------------------------------------------------------------------
# 5. figure
# --------------------------------------------------------------------------------------------
def figure(rows: dict) -> dict:
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.ticker import FixedLocator, NullLocator

    order = sorted(FEATS, key=lambda f: rows[f]["primary"]["pct"], reverse=True)
    recs = []
    for f in order:
        r = rows[f]
        resc = r.get("R1_per_unit_rescaled")
        r1 = resc["raw"]["pct"] if resc else r["R1_matched_pairs_prereg"]["pct"]
        r1c = resc["calibrated"]["pct"] if resc else r["R1_placebo_calibrated"]["pct"]
        recs.append({"feature": f, "label": r["plain_label"], "unit": r["unit"], "primary_pct": r["primary"]["pct"],
                     "primary_lo": r["primary"]["lo"], "primary_hi": r["primary"]["hi"], "p_holm": r["p_holm"],
                     "matched_pairs_prereg_pct": r1, "matched_pairs_calibrated_pct": r1c,
                     "matched_pairs_rescaled_per_unit": bool(resc), "verdict": r["verdict"]})
    D = pd.DataFrame(recs)

    fig, ax = C.new_fig("double", height=3.5)
    BLUE, GREY, ORANGE = C.COLORS[0], C.GREY, C.COLORS[1]
    ypos = np.arange(len(D))[::-1]
    for yv, (_, r) in zip(ypos, D.iterrows()):
        sig = r.verdict in ("more citations", "fewer citations")
        col = BLUE if sig else GREY
        ax.plot([1 + r.primary_lo, 1 + r.primary_hi], [yv, yv], color=col, lw=2.0, solid_capstyle="round", zorder=3)
        ax.plot([1 + r.primary_pct], [yv], "o", color=col, ms=7, mec="white", mew=1.2, zorder=4)
        ax.plot([1 + r.matched_pairs_prereg_pct], [yv], "D", mfc="white", mec=C.TEXT2, mew=1.2, ms=5.5, zorder=5)
        ax.plot([1 + r.matched_pairs_calibrated_pct], [yv], "^", mfc="white", mec=ORANGE, mew=1.2, ms=6, zorder=5)
        hp = "<0.001" if r.p_holm < 0.001 else f"{r.p_holm:.2f}"
        ax.annotate(f"{r.verdict}  (Holm p {hp})", xy=(1.0, yv), xycoords=("axes fraction", "data"), xytext=(8, 0),
                    textcoords="offset points", va="center", ha="left", fontsize=8,
                    color=C.TEXT if sig else C.TEXT2, fontweight="bold" if sig else "normal", annotation_clip=False)
    ax.axvline(1.0, color=C.TEXT2, lw=0.8, zorder=1)
    ax.set_xscale("log")
    ticks = [-0.3, -0.2, -0.1, 0, 0.1, 0.25, 0.5, 1.0]
    ax.set_xlim(0.62, 2.05)
    ax.xaxis.set_major_locator(FixedLocator([1 + t for t in ticks]))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_xticklabels(["0" if t == 0 else f"{100 * t:+.0f}%" for t in ticks])
    ax.set_yticks(ypos, D.label)
    ax.set_ylim(-0.7, len(D) - 0.3)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Difference in citations among accepted ICLR papers with similar content (log scale)")
    handles = [Line2D([], [], color=BLUE, marker="o", lw=2, ms=6, mec="white", label="Primary, 95% CI: verdict 'more citations'"),
               Line2D([], [], color=GREY, marker="o", lw=2, ms=6, mec="white", label="Primary, 95% CI: verdict 'inconclusive'"),
               Line2D([], [], color=C.TEXT2, marker="D", lw=0, mfc="white", ms=5, label="Matched pairs (pre-registered R1)"),
               Line2D([], [], color=ORANGE, marker="^", lw=0, mfc="white", ms=6, label="Matched pairs, placebo-calibrated (diagnostic)")]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=7.5, handlelength=1.8,
              columnspacing=1.5)
    fig.text(0.0, -0.035, "Length and similarity: per unit; their matched pairs (top vs bottom tercile) rescaled to the same unit. "
             "Raw matched pairs sit ~17-22% low under the null (placebo).", fontsize=6.8, color=C.TEXT2, ha="left")
    paths = C.save_fig(fig, "fig_title_guide", core.OUT, data=D)
    return {"paths": {k: str(v) for k, v in paths.items()}, "rows_top_to_bottom": D.feature.tolist()}


def main():
    df = core.load()
    joint = joint_model(df)
    het = llm_heterogeneity(df)
    plac = r1_placebo(df)
    rows = guide_table(joint, het, plac)
    res = {"study": "title -> citations, accepted ICLR 2017-2025 (docs/CITES_PREREG.md)",
           "n_papers": int(len(df)),
           "joint_model_8_features": joint,
           "llm_topic_heterogeneity": het,
           "r1_placebo_G1_G2": plac,
           "guide_table": rows,
           "notes": ["primary estimates and Holm p are read from primary.json (frozen); verdicts are read from each G's "
                     "results.json and re-derived with core.verdict on the frozen primary and stored R1/R2",
                     "all *_pct / lo / hi values are proportions: 0.2246 = +22.46%"]}
    res["figure"] = figure(rows)
    core.save(res, "joint_results.json")

    J = joint["features"]
    print("joint model (one fit, n %d):" % J[FEATS[0]]["n"])
    for f in FEATS:
        h = het["features"][f]
        print(f"  {f:16s} joint {100 * J[f]['pct']:+6.1f}% [{100 * J[f]['lo']:+6.1f}, {100 * J[f]['hi']:+6.1f}] p {J[f]['p']:.4f} | "
              f"LLM {100 * h['llm_topic_papers']['pct']:+6.1f}% non {100 * h['non_llm_topic_papers']['pct']:+6.1f}% "
              f"ratio {h['interaction']['ratio']:.2f} [{h['interaction']['ratio_lo']:.2f}, {h['interaction']['ratio_hi']:.2f}] "
              f"p {h['interaction']['p']:.3f}")
    for f in ("G1_name", "G2_assertive"):
        x = plac[f]
        print(f"  R1 placebo {f}: obs {100 * x['observed_pct']:+.1f}% null {100 * x['null_mean_pct']:+.1f}% "
              f"adj {100 * x['adjusted_pct']:+.1f}% [{100 * x['adjusted_lo']:+.1f}, {100 * x['adjusted_hi']:+.1f}] "
              f"p {x['placebo_p_two_sided']:.3f} reproduces core R1: {x['reproduces_core_R1']}")
        s = x["sensitivity_within_year_permutation"]
        print(f"     permutation null {100 * s['null_mean_pct']:+.1f}% adj {100 * s['adjusted_pct']:+.1f}% "
              f"[{100 * s['adjusted_lo']:+.1f}, {100 * s['adjusted_hi']:+.1f}] p {s['placebo_p_two_sided']:.3f}")
    for f, r in rows.items():
        c = r["R1_placebo_calibrated"]
        print(f"  {f:16s} primary {100 * r['primary']['pct']:+6.1f}% Holm {r['p_holm']:.4f} R1 {100 * r['R1_matched_pairs_prereg']['pct']:+6.1f}% "
              f"R1cal {100 * c['pct']:+6.1f}% [{100 * c['lo']:+.1f}, {100 * c['hi']:+.1f}] verdict {r['verdict']}")


if __name__ == "__main__":
    main()
