"""D4 identification audit, check 6: the atlas judges OR-type M statistics (ITS slope change, colon premium) by a
+/-10% band on the OR ratio. For ORs near 1 this compresses large relative differences in the effect itself.
Recompute the published-only / all-submission ratio on the log-OR (effect) scale, from atlas.csv and from a raw
year-level ITS on logit NAME prevalence (s0 vs s3)."""
import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d4_stage_gains as S  # noqa: E402

a = pd.read_csv(S.OUTDIR / "atlas.csv")
for lab in ["ITS slope-change OR (NAME)", "Colon premium OR, 2024-26 (decided-only)"]:
    r = a[a.label == lab].iloc[0]
    pub = r.T_s3 if np.isfinite(r.T_s3) else r.T_s2
    lo, hi = np.log(r.ratio_lo95), np.log(r.ratio_hi95)
    eff_all = np.log(r.T_s0)
    print(f"{lab}: all OR {r.T_s0:.3f}, published-only OR {pub:.3f}; OR ratio {r.ratio:.3f} (within10={r.within_10pct});"
          f" effect (log-OR) ratio {np.log(pub) / eff_all:.2f}; 95% CI of effect ratio "
          f"[{(eff_all + lo) / eff_all:.2f}, {(eff_all + hi) / eff_all:.2f}]")
df = S.load_frame(min_year=2018, density=False)
def its(y):
    t = np.array(y.index, float) - 2023
    post = (t >= 1).astype(float)
    m = sm.OLS(y.values, sm.add_constant(np.column_stack([t, post, post * t]))).fit()
    return m.params[3], m.bse[3]
for st in ["s0", "s3"]:
    p = df[df[st] == 1].groupby("year").name_primary.mean()
    b, se = its(np.log(p / (1 - p)))
    print(f"raw year-level ITS slope change, {st}: logOR {b:+.3f} (se {se:.3f})")
