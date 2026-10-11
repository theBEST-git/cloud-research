"""D4 identification audit, check 4 (H4a pool-specific 2024 break): small-T inference.
The D4 Wald test treats papers as independent given topic clusters; the slope change is identified from 9 annual
cohorts, so pool-specific year shocks are ignored. Here:
  (1) year-level series of logit NAME prevalence by pool (raw) and the ACC-REJ, ACC-WD difference series;
  (2) ITS on the 9-point difference series (t, post, post*t), OLS with t(5) SEs: slope-change difference;
  (3) placebo break scan on the difference series (break years 2020..2025) for the slope-change difference;
  (4) the same on the paper-level D4 spec: ACC-REJ log-OR difference at placebo breaks 2020-2023 (does a gap of the
      observed size arise at null break years?).
"""
import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d4_stage_gains as S  # noqa: E402

df = S.load_frame(min_year=2018, density=False)
yrs = list(range(2018, 2027))
tab = df[df.pool.isin(["ACC", "REJ", "WD"])].groupby(["year", "pool"]).name_primary.agg(["mean", "size"]).unstack()
p = tab["mean"]
n = tab["size"]
print("NAME prevalence by pool:")
print(p.round(4).to_string())
lg = np.log(p / (1 - p))


def its_series(y, brk=2024):
    t = np.array(y.index, float) - (brk - 1)
    post = (t >= 1).astype(float)
    X = sm.add_constant(np.column_stack([t, post, post * t]))
    m = sm.OLS(y.values, X, missing="drop").fit()
    return m.params[3], m.bse[3], m.df_resid


for a, b in [("ACC", "REJ"), ("ACC", "WD"), ("REJ", "WD")]:
    d = (lg[a] - lg[b]).loc[[y for y in yrs if not (b == "WD" and y < 2018)]]
    est, se, dfr = its_series(d)
    print(f"\n{a}-{b}: logit gap by year: " + ", ".join(f"{y}:{v:+.3f}" for y, v in d.items()))
    print(f"  year-level ITS slope-change difference = {est:+.3f} (se {se:.3f}, df {dfr:.0f}); "
          f"95% CI [{est - 2.571 * se:+.3f}, {est + 2.571 * se:+.3f}]")
    scan = {}
    for brk in range(2020, 2026):
        e, s_, _ = its_series(d, brk)
        scan[brk] = round(e, 3)
    print(f"  placebo-break scan of slope-change difference: {scan}")

# per-pool year-level ITS slope change (for reference)
for pool in ["ACC", "REJ", "WD"]:
    est, se, dfr = its_series(lg[pool])
    print(f"{pool}: year-level slope change logOR {est:+.3f} (se {se:.3f}, df {dfr:.0f}) -> OR {np.exp(est):.3f} "
          f"[{np.exp(est - 2.571 * se):.3f}, {np.exp(est + 2.571 * se):.3f}]")

# paper-level D4 spec at placebo breaks
print("\npaper-level D4 ITS (topic FE, controls), ACC vs REJ slope-change at different break years:")
for brk in [2021, 2022, 2023, 2024, 2025]:
    out = {}
    for pool in ["ACC", "REJ"]:
        d = df[df.pool.eq(pool)].copy()
        d["tc"] = d.year - (brk - 1)
        d["post"] = (d.year >= brk).astype(int)
        d["post_t"] = d.post * d.tc
        from analyses import _core as C
        r = C.logit("name_primary ~ tc + post + post_t + log_authors + llm_topic + C(topic100)", d, cluster="topic100")
        out[pool] = (r.params["post_t"], r.bse["post_t"])
    dlt = out["ACC"][0] - out["REJ"][0]
    se = np.sqrt(out["ACC"][1] ** 2 + out["REJ"][1] ** 2)
    print(f"  break {brk}: ACC {out['ACC'][0]:+.3f} ({out['ACC'][1]:.3f})  REJ {out['REJ'][0]:+.3f} ({out['REJ'][1]:.3f})"
          f"  diff {dlt:+.3f} (indep se {se:.3f})")
