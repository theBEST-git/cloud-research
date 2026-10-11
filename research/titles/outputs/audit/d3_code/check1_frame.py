"""Audit D3: frame sanity (NaN drops, area coverage, slot panel composition)."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3

df = D3.load_frame()
print("rows", len(df), "dup ids", df.submission_id.duplicated().sum())
for c in ["topic100", "topic100_bge", "llm_topic", "log_authors", "n_words", "F_any"]:
    print(c, "NaN:", int(df[c].isna().sum()))
# area coverage 2024-26
for y in (2024, 2025, 2026):
    d = df[df.year == y]
    print(y, "area_h NaN", int(d.area_h.isna().sum()), "of", len(d), "| by pool NaN:",
          d[d.area_h.isna()].pool.value_counts().to_dict())
inv = D3.frozen_inventory()
P = D3.slot_panel(df, inv)
print(P.groupby(["slot", "post"]).size().unstack())
print("opener_pos x post among LLM slots (opener slots only):")
S = P[(P.llm_slot == 1) & (P.slot != "study_adj")]
print(pd.crosstab(S.year, S.opener_pos))
print("LLM share by opener_pos x post:")
print(S.groupby(["post", "opener_pos"]).y.agg(["mean", "size"]))
# in_abs by variant
S2 = P[P.llm_slot == 1]
print("in_abs by slot x y (share with same lemma in abstract):")
print(S2.groupby(["slot", "y"]).in_abs.agg(["mean", "size"]))
print("post x y x in_abs among exclusion sample")
print(S2.groupby(["post", "y"]).in_abs.mean().unstack())
