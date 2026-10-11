import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d4_stage_gains as S
df = S.load_frame()
g = pd.read_csv(S.OUTDIR / "gains.csv")
def P(d, col, st): return d.loc[d[st] == 1, col].mean()
out = []
for k in ["NAME", "L_union", "O_union", "R24", "style_density", "all_caps_title"]:
    col = S.FEAT_COL[k]
    w = {y: (df.year == y).sum() for y in S.POST}
    W = sum(w.values())
    Pst = {st: sum(w[y] / W * P(df[df.year == y], col, st) for y in S.POST) for st in ["s0", "s1", "s2", "s3"]}
    for gn, (a, b) in S.GAIN_DEFS.items():
        mine = Pst[a] / Pst[b]
        theirs = g[(g.variant == "primary") & (g.feature == k) & (g.gain == gn) & (g.period == "2024-26") & (g.pooling == "std")].est.iloc[0]
        out.append((k, gn, round(mine, 5), round(theirs, 5)))
print(pd.DataFrame(out, columns=["feat", "gain", "indep", "file"]).to_string())
# check: stratified-by-year bootstrap SE vs analytic delta-method for NAME total 2024-26
