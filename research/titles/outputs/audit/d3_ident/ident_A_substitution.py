"""D3 identification audit A: is the H3a slot 'break' a substitution (meaning-fixed swap) or an addition of new
slot-filled titles? Per-1k-titles rates of LLM-variant and neutral-variant openers by year, plus gerund-opener rate.
Also: share model restricted to 2020+ (drop the sparse 2018-19 trend anchors) and with slot-specific quadratic trend."""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3

OUT = C.OUT / "audit" / "d3_ident"
df = D3.load_frame()
inv = json.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
g = C.load_features(["opener_gerund", "opener_word"])
df = df.merge(g[["submission_id", "opener_gerund"]], on="submission_id")
N = df.groupby("year").size()
rows = []
for s in D3.SLOTS:
    y, w = D3.slot_y(df, s, inv)
    t = pd.DataFrame({"year": df.year, "y": y})
    for side, val in (("llm", 1), ("neutral", 0)):
        k = t[t.y == val].groupby("year").size().reindex(N.index, fill_value=0)
        for yr in N.index:
            rows.append(dict(slot=s, side=side, year=yr, k=int(k[yr]), per1k=1000 * k[yr] / N[yr]))
R = pd.DataFrame(rows)
piv = R.pivot_table(index="year", columns=["slot", "side"], values="per1k").round(2)
# pooled (opener slots only)
po = R[R.slot != "study_adj"].groupby(["year", "side"]).k.sum().unstack()
po = po.div(N, axis=0) * 1000
ger = df.groupby("year").opener_gerund.mean() * 1000
# neutral-variant per 1k in NA pool
rowsna = []
for s in ["improve", "reveal", "exploit"]:
    y, _ = D3.slot_y(df, s, inv)
    for val, side in ((1, "llm"), (0, "neutral")):
        k = df[(y == val) & (df.NA == 1)].groupby("year").size()
        rowsna.append((k / df[df.NA == 1].groupby("year").size() * 1000).rename(f"{s}_{side}"))
na = pd.concat(rowsna, axis=1).round(2)
pd.set_option("display.width", 250)
print("per-1k titles by slot x side\n", piv)
print("pooled opener slots per 1k\n", po.round(2))
print("gerund-opener rate per 1k\n", ger.round(1))
print("NA pool per 1k\n", na)
# Poisson for neutral and llm counts, pooled opener slots, pre linear trend 2018-23 + post
from statsmodels.api import GLM, families
import statsmodels.formula.api as smf
cnt = po.mul(N, axis=0).round().astype(int).reset_index()
cnt["n"] = N.values
cnt = cnt[cnt.year >= 2018]
cnt["t"], cnt["post"] = cnt.year - 2023, (cnt.year >= 2024).astype(int)
res = {}
for side in ("llm", "neutral"):
    m = smf.glm(f"{side} ~ t + post", cnt, family=families.Poisson(), offset=np.log(cnt.n)).fit(scale="X2")
    res[side] = dict(RR_post=float(np.exp(m.params["post"])), lo=float(np.exp(m.conf_int().loc["post", 0])),
                     hi=float(np.exp(m.conf_int().loc["post", 1])), RR_trend=float(np.exp(m.params["t"])))
print("Poisson per-1k rate, post level shift vs linear pre trend (quasi):", res)
# simple pre/post means
pre = cnt[cnt.year.between(2021, 2023)]; post = cnt[cnt.year >= 2024]
simple = {side: dict(pre_2021_23=float(pre[side].sum() / pre.n.sum()),
                     post_2024_26=float(post[side].sum() / post.n.sum())) for side in ("llm", "neutral")}
print("pooled per1k pre(2021-23) vs post(2024-26):", simple)
json.dump(dict(per1k=piv.reset_index().to_dict(orient="records") if False else None, pooled_per1k=po.round(3).reset_index().to_dict(orient="records"),
               gerund_per1k=ger.round(2).to_dict(), poisson=res, simple=simple), open(OUT / "ident_A_substitution.json", "w"), indent=1, default=str)
R.to_csv(OUT / "ident_A_substitution_rates.csv", index=False)
