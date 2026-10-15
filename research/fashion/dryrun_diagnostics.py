"""Reported (non-criterion) diagnostics of dry-run v3, computed from its replication files after it finished and before
the freeze (pre-run log: dry-run v3 results, review round B7). Outcome-blind: reads only output/dryrun*/.

Null scenarios, per hypothesis:
  - the share of each verdict (incl. 'significant in the opposite direction');
  - main_directional_holm: Holm-adjusted p < 0.05 with the predicted sign, and the share of those that also pass the
    75% and hindsight requirements (robust_and_hindsight_given_main);
  - joint and either rejection by p and the S11 two-way p; supported_and_s11_agrees: supported and the S11 p,
    Holm-adjusted within the family (missing as 1), below 0.05 (the S11 coefficient is the main one, so its sign is);
  - t_sd: standard deviation of the CR1 t-statistic (1 under a correctly sized test).
Null scenarios, per family: any hypothesis supported (family-wise false support), the same without the S11 qualifier,
any directional claim (supported or opposite), and for RQ2 'H2b or H2c supported'.
Stress sensitivity (review round B7/B8): for H2b and H2c in the RQ2 nulls, the rejection rate of the stress p (CR1 t
divided by its standard deviation under rq2_null_early, t with 99 df), i.e. how the frozen sensitivity behaves.
Full-rule scenarios at 1 x SESOI: share of each verdict of the planted hypothesis.
v2_v3_identical: the CR1 columns and verdicts of every null scenario are the same in dry-run v2 and v3.

    python research/fashion/dryrun_diagnostics.py      -> output/checks/dryrun_v3_diagnostics.json
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from scipy import stats

from common import OUTPUT
from variants import ROBUST_SHARE, holm

DRY, V2 = OUTPUT / "dryrun", OUTPUT / "dryrun_v2"
NULLS = ["rq2_null_k100", "rq2_null_early", "rq3_permuted", "rq3_null_k100_lo", "rq3_null_k100_hi", "rq3_null_early_hi"]
FULL = ["rq2_fullrule_H2a_m1.0", "rq2_fullrule_H2b_m1.0", "rq2_fullrule_H2c_m1.0", "rq3_fullrule_H3a_m1.0_hi",
        "rq3_fullrule_H3b_m1.0_hi"]


def rate(x) -> float:
    return round(float(np.mean(x)), 4)


def null_scenario(d: pd.DataFrame) -> dict:
    d = d[~d.hypothesis.str.contains(":")].copy()
    d["s11_holm"] = d.groupby("rep").p_twoway.transform(lambda p: holm(p.fillna(1.0)))
    right = np.sign(d.coef) == d.predicted_sign
    d["main"] = right & (d.p_holm < 0.05)
    d["passes"] = (d.robust >= ROBUST_SHARE) & d.hindsight.astype(bool)
    d["supported"] = d.verdict == "supported"
    d["agrees"] = d.supported & (d.s11_holm < 0.05)
    d["claim"] = d.supported | (d.verdict == "significant in the opposite direction")
    res = {}
    for h, g in d.groupby("hypothesis"):
        t = g.coef / g.se
        res[h] = {"reps": int(len(g)),
                  "verdicts": {k: round(float(v), 4) for k, v in g.verdict.value_counts(normalize=True).items()},
                  "main_directional_holm": rate(g.main),
                  "robust_and_hindsight_given_main": rate(g.passes[g.main]) if g.main.any() else None,
                  "p_and_twoway_both_below_05": rate((g.p < 0.05) & (g.p_twoway < 0.05)),
                  "p_or_twoway_below_05": rate((g.p < 0.05) | (g.p_twoway < 0.05)),
                  "supported_and_s11_agrees": rate(g.agrees),
                  "t_sd": round(float(t.std(ddof=1)), 4)}
    reps = d.groupby("rep")
    fam = {"any_supported": rate(reps.supported.any()), "any_supported_and_s11_agrees": rate(reps.agrees.any()),
           "any_directional_claim": rate(reps.claim.any())}
    if {"H2b", "H2c"} <= set(d.hypothesis):
        fam["H2b_or_H2c_supported"] = rate(d[d.hypothesis.isin(["H2b", "H2c"])].groupby("rep").supported.any())
    return {"hypotheses": res, "family": fam}


def v2_v3_identical() -> dict:
    out = {}
    for sc in NULLS:
        a, b = pd.read_csv(V2 / f"{sc}.csv"), pd.read_csv(DRY / f"{sc}.csv")
        b = b.assign(p=b.p_cr1.where(b.p_cr1.notna(), b.p))              # logit rows carry only p
        cols = ["scenario", "rep", "hypothesis", "coef", "se", "p", "n", "verdict"]
        out[sc] = bool(len(a) == len(b) and all(((a[c] == b[c]) | (a[c].isna() & b[c].isna())).all() for c in cols))
    return out


def stress_size() -> dict:
    t = lambda d: d.coef / d.se
    early = pd.read_csv(DRY / "rq2_null_early.csv")
    r = {h: float(t(g).std(ddof=1)) for h, g in early.groupby("hypothesis") if h in ("H2b", "H2c")}
    out = {}
    for sc in ["rq2_null_k100", "rq2_null_early"]:
        d = pd.read_csv(DRY / f"{sc}.csv")
        out[sc] = {h: rate(2 * stats.t.sf(np.abs(t(g)) / r[h], 99) < 0.05) for h, g in d.groupby("hypothesis") if h in r}
    return out


def main() -> None:
    out = {"null": {sc: null_scenario(pd.read_csv(DRY / f"{sc}.csv")) for sc in NULLS}, "fullrule_1x_sesoi": {},
           "v2_v3_identical": v2_v3_identical(), "stress_p_size": stress_size()}
    for sc in FULL:
        d = pd.read_csv(DRY / f"{sc}.csv")
        g = d[d.planted == True]                                            # noqa: E712  (the planted hypothesis)
        out["fullrule_1x_sesoi"][sc] = {"reps": int(len(g)),
                                        "verdicts": {k: round(float(v), 4) for k, v in g.verdict.value_counts(normalize=True).items()}}
    (OUTPUT / "checks" / "dryrun_v3_diagnostics.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
