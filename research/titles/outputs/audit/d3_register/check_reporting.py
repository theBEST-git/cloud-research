"""Reporting audit for D3: recompute a sample of RESULTS.md numbers from the analysis frame.
Read-only on the direction's files. Run from research/titles/src:
  OMP_NUM_THREADS=1 python ../outputs/audit/d3_register/check_reporting.py
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path.cwd()))
from analyses import _core as C
from analyses import d3_slots as S

OUT = Path(__file__).resolve().parent
inv = json.load(open(C.OUT / "d3_register" / "slot_inventory.json"))
inv = inv.get("inventory", inv)
df = S.load_frame()
P = S.slot_panel(df, inv)
res = {}
sl = P[P.llm_slot == 1]
ct = P[P.llm_slot == 0]
res["n_slot_rows_2018plus"] = int(len(sl)); res["n_slot_papers"] = int(sl.submission_id.nunique())
res["n_ctrl_rows"] = int(len(ct)); res["ctrl_by_pair"] = ct.slot.value_counts().to_dict()
res["via_share_of_controls"] = float((ct.slot == "via").mean())
res["pooled_slot_share_by_year"] = sl.groupby("year").y.mean().round(3).to_dict()
res["pooled_ctrl_share_by_year"] = ct.groupby("year").y.mean().round(3).to_dict()
# 2023 deviation by pool: is it carried by accepted (camera-ready, finalised after ChatGPT) titles?
for pool in ["ACC", "NA"]:
    m = sl[pool].astype(bool) if pool in sl.columns else None
    if m is None:
        m = sl.submission_id.isin(df.loc[df[pool].astype(bool), "submission_id"])
    g = sl[m].groupby("year").y.agg(["mean", "size"])
    res[f"slot_share_{pool}"] = {int(k): [round(v["mean"], 3), int(v["size"])] for k, v in g.iterrows()}
# register rates 2025/2026 all titles and fingerprint prevalence
for y in (2021, 2022, 2023, 2024, 2025, 2026):
    d = df[df.year == y]
    res[f"rates_{y}"] = dict(r24_per1k=round(1000 * d.r24_any.mean(), 1), r26_per1k=round(1000 * d.r26_any.mean(), 1),
                             F=round(d.F_any.mean(), 4), f24=round(d.f24.mean(), 4), f26=round(d.f26.mean(), 4), n=len(d))
pre = df[df.year.isin([2021, 2022])]
res["F_rate_2021_22"] = round(pre.F_any.mean(), 4)
# H3e raw shares
s2 = sl.merge(df[["submission_id", "F_any"]], on="submission_id", how="left", suffixes=("", "_f"))
fcol = "F_any_f" if "F_any_f" in s2.columns else "F_any"
res["pre_2022_23_share"] = round(s2[s2.year.isin([2022, 2023])].y.mean(), 3)
for y in (2024, 2025, 2026):
    g = s2[s2.year == y].groupby(fcol).y.agg(["mean", "size"])
    res[f"share_by_F_{y}"] = {str(k): [round(v["mean"], 3), int(v["size"])] for k, v in g.iterrows()}
json.dump(res, open(OUT / "check_reporting.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
