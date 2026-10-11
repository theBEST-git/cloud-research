"""D3 audit A2: (a) LLM vs neutral slot-variant rates per 1k in the non-LLM subset and NA pool, 2022-2024;
(b) which gerund openers drove the 2023->2024 rise of the gerund-opener construction (non-slot gerunds included);
(c) H3a share model vs a count model: post level shift in neutral-variant per-1k rate with year-level Poisson + slot FE."""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
OUT = C.OUT / "audit" / "d3_ident"
df = D3.load_frame()
g = C.load_features(["opener_gerund"])
df = df.merge(g, on="submission_id")
inv = json.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
llm, neu = set(), set()
for s in ("improve", "reveal", "exploit"):
    llm |= set(inv[s]["llm"]); neu |= set(inv[s]["neutral"])
df["ow"] = df.opener_word.fillna("").astype(str)
df["is_llm"] = df.ow.isin(llm).astype(int); df["is_neu"] = df.ow.isin(neu).astype(int)
df["ger_other"] = ((df.opener_gerund == 1) & ~df.ow.isin(llm | neu)).astype(int)
res = {}
for nm, m in [("all", df.year > 0), ("non_llm", df.non_llm == 1), ("NA", df.NA == 1), ("non_llm_NA", (df.non_llm == 1) & (df.NA == 1))]:
    t = df[m & df.year.between(2020, 2026)].groupby("year")[["is_llm", "is_neu", "ger_other"]].mean() * 1000
    res[nm] = t.round(2).to_dict(orient="index")
    print(nm); print(t.round(2).to_string())
# top gerund openers change 2022-23 -> 2024 (per 1k), non-slot only
a = df[df.year.isin([2022, 2023, 2024])].copy()
a["per"] = np.where(a.year == 2024, "y24", "y2223")
gg = a[a.opener_gerund == 1].groupby(["ow", "per"]).size().unstack(fill_value=0)
n = a.groupby("per").size()
gg = gg.div(n, axis=1) * 1000
gg["diff"] = gg.y24 - gg.y2223
gg = gg.sort_values("diff", ascending=False)
print("top risers among gerund openers 2022-23 -> 2024 (per 1k)\n", gg.head(15).round(2).to_string())
print("top fallers\n", gg.tail(8).round(2).to_string())
res["gerund_top_risers"] = gg.head(15).round(3).reset_index().to_dict(orient="records")
res["gerund_diff_total_per1k"] = float(gg["diff"].sum())
res["gerund_diff_from_llm_slot_words"] = float(gg.loc[gg.index.isin(llm), "diff"].sum())
res["gerund_diff_from_neutral_slot_words"] = float(gg.loc[gg.index.isin(neu), "diff"].sum())
print({k: res[k] for k in ("gerund_diff_total_per1k", "gerund_diff_from_llm_slot_words", "gerund_diff_from_neutral_slot_words")})
json.dump(res, open(OUT / "ident_A2_gerund.json", "w"), indent=1, default=float)
