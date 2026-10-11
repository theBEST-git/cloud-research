"""I7 check: pooled 2024-26 NAME G_total (year-standardised) in LLM vs non-LLM topics and by harmonised area,
paper bootstrap (500, stratified by year) for the topic split; area cells with >= 300 s0 papers."""
import numpy as np
import pandas as pd
from analyses import d4_stage_gains as S
df = S.load_frame(density=False)
df = df[df.year.isin(S.POST)].reset_index(drop=True)
out = {}
for lab, m in [("non-LLM topics", df.llm_topic == 0), ("LLM topics", df.llm_topic == 1)]:
    d = df[m].reset_index(drop=True)
    g, _, _ = S.gain_table(d, ["NAME"], lab, n_boot=500, crf=False, periods={"2024-26": S.POST})
    r = g[(g.gain == "total") & (g.pooling == "std")].iloc[0]
    print(f"{lab:16s} n={len(d):6d} G_total {r.est:.3f} [{r.lo95:.3f}, {r.hi95:.3f}]")
rows = []
for a, d in df.groupby("area_h"):
    if len(d) < 300:
        continue
    d = d.reset_index(drop=True)
    g, _, _ = S.gain_table(d, ["NAME"], a, n_boot=0, crf=False, periods={"2024-26": S.POST})
    rows.append(dict(area=a, n=len(d), G_total=g[(g.gain == "total") & (g.pooling == "std")].est.iloc[0]))
t = pd.DataFrame(rows).sort_values("G_total")
print(t.round(3).to_string(index=False))
print("areas:", len(t), "range", t.G_total.min().round(3), t.G_total.max().round(3),
      "IQR", t.G_total.quantile([.25, .75]).round(3).tolist())
