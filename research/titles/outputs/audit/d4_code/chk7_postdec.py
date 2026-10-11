"""Re-define post-decision withdrawals by the withdrawal timestamp (modification_ms >= decision date, 2025-26)
and recompute exit / decision gains; compare with primary (wd_post = 2026 decision=='rejected' only)."""
import numpy as np, pandas as pd
from common import read_table
from analyses import d4_stage_gains as S
df = S.load_frame()
m = read_table("metadata_provenance")[["submission_id", "modification_ms"]]
df = df.merge(m, on="submission_id", how="left", validate="1:1")
df["mod"] = pd.to_datetime(df.modification_ms, unit="ms")
dec = {2025: "2025-01-22", 2026: "2026-01-26"}
df["wd_post_ts"] = 0
for y, d in dec.items():
    df.loc[(df.year == y) & (df.WD == 1) & (df["mod"] >= pd.Timestamp(d)), "wd_post_ts"] = 1
print("timestamp-based post-decision WD:", df[df.wd_post_ts == 1].groupby(["year", "decision"]).size().to_dict())
print("primary wd_post:", int(df.wd_post.sum()))
alt = df.copy()
alt["s2"] = ((alt.s1 == 1) & ((alt.WD == 0) | (alt.wd_post == 1) | (alt.wd_post_ts == 1))).astype(int)
alt["s2n"] = alt.s2 * (1 - alt.ACC)
keys = ["NAME", "L_union", "R24", "F24", "O_union", "style_density"]
per = {"2025": (2025,), "2026": (2026,), "2024-26": S.POST}
g0, _, _ = S.gain_table(df, keys, "primary", n_boot=200, periods=per)
g1, _, _ = S.gain_table(alt, keys, "wd_post_by_timestamp", n_boot=200, periods=per)
g = pd.concat([g0, g1])
g = g[(g.pooling == "std") & g.gain.isin(["exit", "dec", "predec", "total"])]
print(g.pivot_table(index=["feature", "period", "gain"], columns="variant", values="est").round(4).to_string())
