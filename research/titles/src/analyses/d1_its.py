"""WP5 / D1-H1a: dated 2024 break in NAME titles (segmented logit, placebo breaks, sup-LR scan, randomization p).

Model (PLAN D1):
    logit P(NAME_i) = a + b*(t - (B-1)) + g*post_B + d*post_B*(t - (B-1)) + l*log_authors + k*llm_topic + topic100 FE
with B = 2024 by default (so t - (B-1) = year - 2023 as in the plan), SEs clustered by topic100.
d (the slope change, reported as OR per year) does not depend on how the level shift is parameterised.

Outputs (outputs/d1_break/):
    T1_1_its.csv              ITS coefficients across pools, subsets, topic encoders and NAME definitions
    its_year_deviation.csv    year-dummy variant: deviations of 2024/25/26 from the extrapolated 2017-23 logit trend
    its_break_scan.csv        break at every candidate year (full data) and placebo breaks (pre-2024 data only)
    its_results.json          machine-readable H1a estimates and verdict inputs
    fig_its_scan.{pdf,png,csv} supplementary: slope-change OR by candidate break year

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d1_its
"""
from __future__ import annotations

import json
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C

OUTDIR = C.OUT / "d1_break"
OUTCOMES = {"primary": "name_primary", "strict": "name_strict", "loose": "name_loose", "compound": "name_compound"}


def load() -> pd.DataFrame:
    df = C.load_analysis_frame(
        feature_cols=list(OUTCOMES.values()),
        universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "non_llm", "NA", "ACC",
                       "REJ", "WD", "DR"],
        with_bge_topics=True)
    for c in list(OUTCOMES.values()) + ["llm_topic", "non_llm", "llm_topic_bge", "NA", "ACC", "REJ", "WD", "DR"]:
        df[c] = df[c].astype(int)
    return df


def _design(d: pd.DataFrame, B: int) -> pd.DataFrame:
    d = d.copy()
    d["tc"] = d.year - (B - 1)
    d["post"] = (d.year >= B).astype(int)
    d["post_t"] = d.post * d.tc
    return d


def its_fit(d: pd.DataFrame, outcome: str, B: int = 2024, fe: str | None = "topic100",
            controls=("log_authors", "llm_topic"), cluster: str | None = "topic100", slope_change: bool = True,
            level: bool = True):
    """Segmented logit (level shift and/or slope change at B); returns the statsmodels result."""
    d = _design(d, B)
    ctr = [c for c in controls if d[c].nunique() > 1]
    rhs = ["tc"] + (["post"] if level else []) + (["post_t"] if slope_change else []) + ctr + \
        ([f"C({fe})"] if fe else [])
    f = f"{outcome} ~ " + " + ".join(rhs)
    res = C.logit(f, d, cluster=cluster)
    return res


def tidy_its(res, label: dict) -> dict:
    t = C.or_table(res, [x for x in ["tc", "post", "post_t"] if x in res.params.index])
    out = dict(label)
    out["nobs"] = int(res.nobs)
    out["llf"] = float(res.llf)
    for term, nm in [("tc", "pre_slope"), ("post", "level"), ("post_t", "slope_change")]:
        if term in t.index:
            r = t.loc[term]
            out[f"{nm}_OR"] = float(r.OR)
            out[f"{nm}_OR_lo"] = float(r.OR_lo)
            out[f"{nm}_OR_hi"] = float(r.OR_hi)
            out[f"{nm}_z"] = float(r.z)
            out[f"{nm}_p"] = float(r.p)
    if "post_t" in t.index:
        out["slope_change_p_one_sided"] = float(stats.norm.sf(t.loc["post_t", "z"]))
    return out


def lpm_its(d: pd.DataFrame, outcome: str, B: int = 2024, fe: str | None = "topic100",
            controls=("log_authors", "llm_topic"), cluster: str = "topic100") -> dict:
    """Same segmentation as an LPM (pp per year), for interpretation only."""
    d = _design(d, B)
    ctr = [c for c in controls if d[c].nunique() > 1]
    r = C.feols(d, outcome, ["tc", "post", "post_t"] + ctr, fe=[fe] if fe else None, cluster=cluster)
    ci = r.conf_int()
    return {"lpm_pre_slope_pp": 100 * float(r.params["tc"]), "lpm_slope_change_pp": 100 * float(r.params["post_t"]),
            "lpm_slope_change_pp_lo": 100 * float(ci.loc["post_t", "lo"]),
            "lpm_slope_change_pp_hi": 100 * float(ci.loc["post_t", "hi"]),
            "lpm_level_pp": 100 * float(r.params["post"])}


def year_deviation(d: pd.DataFrame, outcome: str, fe: str | None = "topic100",
                   controls=("log_authors", "llm_topic"), cluster: str = "topic100",
                   post_years=(2024, 2025, 2026)) -> pd.DataFrame:
    """Logit with a linear 2017-23 trend plus one dummy per post year: each dummy is the deviation from the
    extrapolated pre-trend (logit scale). Also returns the implied pp deviation (average over that year's rows
    of p(with dummy) - p(without)), with a CI from the coefficient bounds (monotone map)."""
    d = d.copy()
    d["tc"] = d.year - 2023
    ctr = [c for c in controls if d[c].nunique() > 1]
    dums = []
    for y in post_years:
        d[f"D{y}"] = (d.year == y).astype(int)
        dums.append(f"D{y}")
    f = f"{outcome} ~ tc + " + " + ".join(dums + ctr + ([f"C({fe})"] if fe else []))
    res = C.logit(f, d, cluster=cluster)
    t = C.or_table(res, dums)
    rows = []
    # design matrix actually used by the fit (avoids re-evaluating the formula: `C` is the core module here)
    X = pd.DataFrame(res.model.exog, columns=res.model.exog_names)
    beta = res.params[X.columns].to_numpy()
    for y, dn in zip(post_years, dums):
        m = (d.loc[res.model_rows, "year"] == y).to_numpy()
        Xy = X[m].to_numpy()
        j = list(X.columns).index(dn)
        eta = Xy @ beta
        base = eta - beta[j]
        def pp(b):
            return 100 * float(np.mean(1 / (1 + np.exp(-(base + b))) - 1 / (1 + np.exp(-base))))
        r = t.loc[dn]
        rows.append(dict(year=y, dev_OR=float(r.OR), dev_OR_lo=float(r.OR_lo), dev_OR_hi=float(r.OR_hi),
                         dev_p=float(r.p), dev_pp=pp(r.coef), dev_pp_lo=pp(r.lo), dev_pp_hi=pp(r.hi),
                         obs_share=float(d.loc[res.model_rows][m][outcome].mean()),
                         trend_pred_share=float(np.mean(1 / (1 + np.exp(-base)))),
                         pre_slope_OR=float(np.exp(res.params["tc"]))))
    return pd.DataFrame(rows)


def main():
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    warnings.filterwarnings("ignore")
    df = load()
    print("loaded", df.shape, f"{time.time() - t0:.0f}s", flush=True)
    rows = []
    res_json = {}

    # ---------------- primary + T1.1 variants ----------------
    specs = []  # (label dict, data, outcome, fe, controls, cluster)
    base_ctr = ("log_authors", "llm_topic")
    for oname, ocol in OUTCOMES.items():
        specs.append((dict(spec="U, topic100 FE (primary)" if oname == "primary" else "U, topic100 FE",
                           pool="U", subset="all", years="2017-2026", outcome=oname, topics="MiniLM topic100"),
                      df, ocol, "topic100", base_ctr, "topic100"))
    o = "name_primary"
    specs += [
        (dict(spec="U, no controls", pool="U", subset="all", years="2017-2026", outcome="primary", topics="none"),
         df, o, None, (), "topic100"),
        (dict(spec="U, controls, no topic FE", pool="U", subset="all", years="2017-2026", outcome="primary",
              topics="none"), df, o, None, base_ctr, "topic100"),
        (dict(spec="U, bge topic100 FE", pool="U", subset="all", years="2017-2026", outcome="primary",
              topics="bge topic100"), df, o, "topic100_bge", ("log_authors", "llm_topic_bge"), "topic100_bge"),
        (dict(spec="NA pool", pool="NA", subset="all", years="2017-2026", outcome="primary",
              topics="MiniLM topic100"), df[df.NA == 1], o, "topic100", base_ctr, "topic100"),
        (dict(spec="non-LLM subset", pool="U", subset="non_llm", years="2017-2026", outcome="primary",
              topics="MiniLM topic100"), df[df.non_llm == 1], o, "topic100", base_ctr, "topic100"),
        (dict(spec="NA pool x non-LLM", pool="NA", subset="non_llm", years="2017-2026", outcome="primary",
              topics="MiniLM topic100"), df[(df.NA == 1) & (df.non_llm == 1)], o, "topic100", base_ctr, "topic100"),
        (dict(spec="2018+", pool="U", subset="all", years="2018-2026", outcome="primary", topics="MiniLM topic100"),
         df[df.year >= 2018], o, "topic100", base_ctr, "topic100"),
        (dict(spec="without 2019", pool="U", subset="all", years="2017-2026 excl. 2019", outcome="primary",
              topics="MiniLM topic100"), df[df.year != 2019], o, "topic100", base_ctr, "topic100"),
        (dict(spec="excluding 2026", pool="U", subset="all", years="2017-2025", outcome="primary",
              topics="MiniLM topic100"), df[df.year <= 2025], o, "topic100", base_ctr, "topic100"),
        (dict(spec="ACC pool", pool="ACC", subset="all", years="2017-2026", outcome="primary",
              topics="MiniLM topic100"), df[df.ACC == 1], o, "topic100", base_ctr, "topic100"),
        (dict(spec="REJ pool", pool="REJ", subset="all", years="2017-2026", outcome="primary",
              topics="MiniLM topic100"), df[df.REJ == 1], o, "topic100", base_ctr, "topic100"),
        (dict(spec="WD pool", pool="WD", subset="all", years="2018-2026", outcome="primary",
              topics="MiniLM topic100"), df[df.WD == 1], o, "topic100", base_ctr, "topic100"),
    ]
    # NA pool for each alternative definition
    for oname, ocol in OUTCOMES.items():
        if oname == "primary":
            continue
        specs.append((dict(spec="NA pool", pool="NA", subset="all", years="2017-2026", outcome=oname,
                           topics="MiniLM topic100"), df[df.NA == 1], ocol, "topic100", base_ctr, "topic100"))
        specs.append((dict(spec="non-LLM subset", pool="U", subset="non_llm", years="2017-2026", outcome=oname,
                           topics="MiniLM topic100"), df[df.non_llm == 1], ocol, "topic100", base_ctr, "topic100"))

    for lab, d, oc, fe, ctr, cl in specs:
        res = its_fit(d, oc, 2024, fe, ctr, cl)
        r = tidy_its(res, lab)
        r.update(lpm_its(d, oc, 2024, fe, ctr, cl))
        r["share_2023"] = float(d.loc[d.year == 2023, oc].mean())
        r["share_2026"] = float(d.loc[d.year == 2026, oc].mean()) if (d.year == 2026).any() else np.nan
        rows.append(r)
        print(f"{lab['spec']:<28s} {lab['outcome']:<9s} n={r['nobs']:>6d} slopeOR={r['slope_change_OR']:.3f} "
              f"[{r['slope_change_OR_lo']:.3f},{r['slope_change_OR_hi']:.3f}] lpm={r['lpm_slope_change_pp']:.2f}pp "
              f"{time.time() - t0:.0f}s", flush=True)
    T = pd.DataFrame(rows)
    T.to_csv(OUTDIR / "T1_1_its.csv", index=False)

    # ---------------- year-dummy variant ----------------
    devs = []
    for lab, d in [("U", df), ("NA", df[df.NA == 1]), ("non_llm", df[df.non_llm == 1])]:
        dv = year_deviation(d, "name_primary")
        dv.insert(0, "population", lab)
        devs.append(dv)
    DV = pd.concat(devs)
    DV.to_csv(OUTDIR / "its_year_deviation.csv", index=False)
    print(DV.round(3).to_string(), flush=True)

    # ---------------- break scan (full data), randomization p, placebo breaks (pre data) ----------------
    scan = []
    # linear-only model: drop post too (pure trend)
    d0 = _design(df, 2024)
    lin_res = C.logit("name_primary ~ tc + log_authors + llm_topic + C(topic100)", d0, cluster="topic100")
    ll0 = float(lin_res.llf)
    for B in range(2019, 2026):
        res = its_fit(df, "name_primary", B)
        r = tidy_its(res, dict(sample="full 2017-2026", break_year=B))
        r["LR_vs_linear"] = 2 * (r["llf"] - ll0)
        scan.append(r)
    for pop, dd in [("NA", df[df.NA == 1]), ("non_llm", df[df.non_llm == 1])]:
        d0p = _design(dd, 2024)
        ll0p = float(C.logit("name_primary ~ tc + log_authors + llm_topic + C(topic100)"
                             if pop == "NA" else "name_primary ~ tc + log_authors + C(topic100)",
                             d0p, cluster="topic100").llf)
        for B in range(2020, 2026):
            res = its_fit(dd, "name_primary", B)
            r = tidy_its(res, dict(sample=f"full 2017-2026, {pop}", break_year=B))
            r["LR_vs_linear"] = 2 * (r["llf"] - ll0p)
            scan.append(r)
    # robustness: kink-only (continuous) segmented model, no level shift
    for B in range(2020, 2026):
        res = its_fit(df, "name_primary", B, level=False)
        r = tidy_its(res, dict(sample="full 2017-2026, kink only (no level shift)", break_year=B))
        r["LR_vs_linear"] = 2 * (r["llf"] - ll0)
        scan.append(r)
    pre = df[df.year <= 2023]
    for B in (2020, 2021, 2022):
        res = its_fit(pre, "name_primary", B)
        scan.append(tidy_its(res, dict(sample="placebo, pre-2024 data 2017-2023", break_year=B)))
    for pop, dd in [("NA", pre[pre.NA == 1]), ("non_llm", pre[pre.non_llm == 1])]:
        for B in (2020, 2021, 2022):
            res = its_fit(dd, "name_primary", B)
            scan.append(tidy_its(res, dict(sample=f"placebo, pre-2024 data 2017-2023, {pop}", break_year=B)))
    S = pd.DataFrame(scan)
    S.to_csv(OUTDIR / "its_break_scan.csv", index=False)
    print(S[["sample", "break_year", "slope_change_OR", "slope_change_OR_lo", "slope_change_OR_hi",
             "slope_change_p", "LR_vs_linear"]].round(4).to_string(), flush=True)

    full = S[S["sample"] == "full 2017-2026"].set_index("break_year")
    z24 = full.loc[2024, "slope_change_z"]
    rand_p = float((full.slope_change_z >= z24).mean())
    rand_p_or = float((full.slope_change_OR >= full.loc[2024, "slope_change_OR"]).mean())
    sup = full.loc[2020:2025, "LR_vs_linear"]
    sel = int(sup.idxmax())
    kink = S[S["sample"] == "full 2017-2026, kink only (no level shift)"].set_index("break_year")
    sel_kink = int(kink.LR_vs_linear.idxmax())
    placebo = S[S["sample"] == "placebo, pre-2024 data 2017-2023"].set_index("break_year")

    prim = T[(T.spec == "U, topic100 FE (primary)") & (T.outcome == "primary")].iloc[0]
    na = T[(T.spec == "NA pool") & (T.outcome == "primary")].iloc[0]
    nl = T[(T.spec == "non-LLM subset") & (T.outcome == "primary")].iloc[0]
    max_placebo_or = float(placebo.slope_change_OR.max())
    crit = {
        "primary_OR_gt_1": bool(prim.slope_change_OR_lo > 1),
        "NA_pool_CI_excludes_1": bool(na.slope_change_OR_lo > 1),
        "non_llm_CI_excludes_1": bool(nl.slope_change_OR_lo > 1),
        "supLR_selects_2024_or_2025": sel in (2024, 2025),
        "placebos_null": bool(((placebo.slope_change_OR_lo <= 1) & (placebo.slope_change_OR_hi >= 1)).all()),
        "no_placebo_as_large": bool(max_placebo_or < prim.slope_change_OR),
    }
    falsified = (not crit["NA_pool_CI_excludes_1"]) or (not crit["no_placebo_as_large"])
    res_json = {
        "H1a": {
            "primary": {k: (float(v) if isinstance(v, (int, float, np.floating, np.integer)) else v)
                        for k, v in prim.items()},
            "NA_pool": {k: (float(v) if isinstance(v, (int, float, np.floating, np.integer)) else v)
                        for k, v in na.items()},
            "non_llm": {k: (float(v) if isinstance(v, (int, float, np.floating, np.integer)) else v)
                        for k, v in nl.items()},
            "randomization_p_z": rand_p, "randomization_p_OR": rand_p_or,
            "randomization_candidates": list(range(2019, 2026)),
            "randomization_note": "p = share of candidate break years 2019-2025 (full data) with slope-change z "
                                  ">= the 2024 z; the minimum attainable p with 7 candidates is 1/7 = 0.143",
            "supLR_selected_break": sel,
            "supLR_by_year": {int(k): float(v) for k, v in sup.items()},
            "supLR_kink_only_selected_break": sel_kink,
            "supLR_kink_only_by_year": {int(k): float(v) for k, v in kink.LR_vs_linear.items()},
            "supLR_note": "LR of the segmented logit (level + slope change at B) against the pure linear-trend "
                          "logit with the same controls and topic100 FE; argmax over B = 2020-2025",
            "placebo_pre_data": {int(B): {"OR": float(r.slope_change_OR), "lo": float(r.slope_change_OR_lo),
                                          "hi": float(r.slope_change_OR_hi), "p": float(r.slope_change_p)}
                                 for B, r in placebo.iterrows()},
            "year_deviation_U": DV[DV.population == "U"].drop(columns="population").to_dict(orient="records"),
            "criteria": crit,
            "falsified": falsified,
            "p_one_sided_primary": float(prim.slope_change_p_one_sided),
        }
    }
    (OUTDIR / "its_results.json").write_text(json.dumps(res_json, indent=1, default=float))

    # ---------------- supplementary figure: slope-change OR by candidate break ----------------
    fig, ax = C.new_fig("single", 2.4)
    fs = S[S["sample"].isin(["full 2017-2026", "placebo, pre-2024 data 2017-2023"])].copy()
    for i, (samp, lab) in enumerate([("full 2017-2026", "full data 2017-26"),
                                     ("placebo, pre-2024 data 2017-2023", "pre-2024 data only (placebo)")]):
        g = fs[fs["sample"] == samp].sort_values("break_year")
        off = -0.08 if i == 0 else 0.08
        col = C.color(0) if i == 0 else C.GREY
        ax.errorbar(g.break_year + off, g.slope_change_OR,
                    yerr=[g.slope_change_OR - g.slope_change_OR_lo, g.slope_change_OR_hi - g.slope_change_OR],
                    fmt="o", color=col, ms=5, lw=1.4, capsize=0, label=lab)
    ax.axhline(1, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_xlabel("candidate break year")
    ax.set_ylabel("slope-change OR per year")
    ax.set_xticks(range(2019, 2026))
    ax.legend(loc="upper left")
    C.save_fig(fig, "fig_its_scan", OUTDIR, data=fs[["sample", "break_year", "slope_change_OR", "slope_change_OR_lo",
                                                      "slope_change_OR_hi", "slope_change_p", "LR_vs_linear"]])
    print(json.dumps(res_json["H1a"]["criteria"], indent=1), "falsified:", falsified)
    print(f"done {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
