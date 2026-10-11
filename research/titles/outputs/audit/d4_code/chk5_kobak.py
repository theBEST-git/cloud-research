import numpy as np, pandas as pd
from analyses import d4_stage_gains as S
df = S.load_frame(density=False)
kb = pd.read_csv(S.OUTDIR / "kobak_bounds.csv")
for st in ["s0", "s3"]:
    p = {y: df.loc[(df.year == y) & (df[st] == 1), "f24"].mean() for y in range(2021, 2027)}
    x = np.array([2021, 2022, 2023.]); sl, ic = np.polyfit(x, [p[2021], p[2022], p[2023]], 1)
    for Y in (2024, 2025, 2026):
        q = max(max(ic + sl * Y, 0), max(p[2022], p[2023]))
        f = kb[(kb.marker == "F24") & (kb.baseline == "cons") & (kb.year.astype(str) == str(Y)) & (kb.set == st)].bound.iloc[0]
        print(st, Y, round(100 * p[Y], 2), "q", round(100 * q, 2), "bound", round(100 * (p[Y] - q), 2), "file", round(100 * f, 2))
    print(st, {y: round(100 * v, 2) for y, v in p.items()})
