"""Reported (non-criterion) diagnostics of dry-run v3, computed from its replication files after it finished and before
the freeze (pre-run log, dry-run v3 results). Outcome-blind: reads only output/dryrun/.

  - null scenarios: rate of each verdict, incl. 'significant in the opposite direction'; joint rejection by the
    bootstrap (or CR1) p and the S11 two-way p;
  - full-rule scenarios at 1 x SESOI: rate of 'equivalent to null' (an equivalence label for an effect of SESOI size).

    python research/fashion/dryrun_diagnostics.py      -> output/checks/dryrun_v3_diagnostics.json
"""
from __future__ import annotations

import json

import pandas as pd

from common import OUTPUT

DRY = OUTPUT / "dryrun"
NULLS = ["rq2_null_k100", "rq2_null_early", "rq3_permuted", "rq3_null_k100_lo", "rq3_null_k100_hi", "rq3_null_early_hi"]
FULL = ["rq2_fullrule_H2a_m1.0", "rq2_fullrule_H2b_m1.0", "rq2_fullrule_H2c_m1.0", "rq3_fullrule_H3a_m1.0_hi",
        "rq3_fullrule_H3b_m1.0_hi"]


def main() -> None:
    out = {"null": {}, "fullrule_1x_sesoi": {}}
    for sc in NULLS:
        d = pd.read_csv(DRY / f"{sc}.csv")
        d = d[~d.hypothesis.str.contains(":")]
        res = {}
        for h, g in d.groupby("hypothesis"):
            res[h] = {"reps": int(len(g)),
                      "verdicts": {k: round(float(v), 4) for k, v in g.verdict.value_counts(normalize=True).items()},
                      "p_and_twoway_both_below_05": round(float(((g.p < 0.05) & (g.p_twoway < 0.05)).mean()), 4),
                      "p_or_twoway_below_05": round(float(((g.p < 0.05) | (g.p_twoway < 0.05)).mean()), 4)}
        out["null"][sc] = res
    for sc in FULL:
        d = pd.read_csv(DRY / f"{sc}.csv")
        g = d[d.planted == True]                                            # noqa: E712  (the planted hypothesis)
        out["fullrule_1x_sesoi"][sc] = {"reps": int(len(g)),
                                        "verdicts": {k: round(float(v), 4) for k, v in g.verdict.value_counts(normalize=True).items()}}
    (OUTPUT / "checks" / "dryrun_v3_diagnostics.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
