"""D3 identification audit B (H3b): (1) word-churn placebo: for every title word with >= 80 titles in 2025+2026,
within-area 2025->2026 sign counts over the 16 large areas and the area-FE rate ratio; how unusual are R24 and R26,
and how often do words with a given aggregate change pass the H3b sign thresholds? (2) random 4-word / 8-word families
matched on 2025 rate. (3) R26/R24 RR within topic100 (Poisson, topic100 FE) and the concentration of the R26 rise."""
import json, re
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3

OUT = C.OUT / "audit" / "d3_ident"
df = D3.load_frame()
d = df[df.year.isin([2025, 2026])].copy()
big = d.groupby("area_h").size()
big = big[big >= 500].index.tolist()
print("n large areas", len(big))
d = d[d.area_h.isin(big)].reset_index(drop=True)
tok = d.title_nfkc.fillna("").str.lower().map(lambda t: set(re.findall(r"[a-z][a-z\-]{2,}", t)))
from collections import Counter
cnt = Counter(w for s in tok for w in s)
vocab = [w for w, c in cnt.items() if c >= 80]
print("vocab", len(vocab))
widx = {w: i for i, w in enumerate(vocab)}
import scipy.sparse as sp
rows, cols = [], []
for i, s in enumerate(tok):
    for w in s:
        j = widx.get(w)
        if j is not None:
            rows.append(i); cols.append(j)
X = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(d), len(vocab)))
# add the families
fam = {"R24": d.r24_any.to_numpy(float), "R26": d.r26_any.to_numpy(float)}
cells = d.groupby(["area_h", "year"]).indices
areas = big
def area_counts(col):  # col: dense vector
    k = np.zeros((len(areas), 2)); n = np.zeros((len(areas), 2))
    for a_i, a in enumerate(areas):
        for y_i, y in enumerate((2025, 2026)):
            ix = cells[(a, y)]
            k[a_i, y_i] = col[ix].sum(); n[a_i, y_i] = len(ix)
    return k, n
# vectorised for vocab
Kw = np.zeros((len(vocab), len(areas), 2)); Nn = np.zeros((len(areas), 2))
for a_i, a in enumerate(areas):
    for y_i, y in enumerate((2025, 2026)):
        ix = cells[(a, y)]
        Kw[:, a_i, y_i] = np.asarray(X[ix].sum(axis=0)).ravel(); Nn[a_i, y_i] = len(ix)
def summarise(K, N):
    r25, r26 = K[..., 0] / N[:, 0], K[..., 1] / N[:, 1]
    up = (r26 > r25).sum(-1); down = (r26 < r25).sum(-1)
    # Mantel-Haenszel rate ratio (area-stratified)
    num = (K[..., 1] * N[:, 0] / N.sum(1)).sum(-1); den = (K[..., 0] * N[:, 1] / N.sum(1)).sum(-1)
    rr = num / np.maximum(den, 1e-9)
    rate25 = K[..., 0].sum(-1) / N[:, 0].sum()
    return up, down, rr, rate25
up, down, rr, rate25 = summarise(Kw, Nn)
W = pd.DataFrame(dict(word=vocab, n=[cnt[w] for w in vocab], up=up, down=down, RR=rr, rate25_per1k=1000 * rate25))
fr = {}
for f, v in fam.items():
    k, n = area_counts(v)
    u, dn, r, r25 = summarise(k[None], n)
    fr[f] = dict(up=int(u[0]), down=int(dn[0]), RR=float(r[0]), rate25_per1k=float(1000 * r25[0]))
print("families", fr)
W["logRR"] = np.log(W.RR)
# (1) How common are passes?
pass_up = (W.up >= 12).mean(); pass_down = (W.down >= 10).mean()
strong_up = W[W.RR >= 1.5]; strong_down = W[W.RR <= 0.80]
res = dict(n_words=len(W), share_words_up_ge12=float(pass_up), share_words_down_ge10=float(pass_down),
           share_words_up_ge12_or_down_ge12=float(((W.up >= 12) | (W.down >= 12)).mean()),
           n_words_RR_ge_1p5=len(strong_up), share_of_those_up_ge12=float((strong_up.up >= 12).mean()),
           share_of_those_up_16=float((strong_up.up == 16).mean()),
           n_words_RR_le_0p8=len(strong_down), share_of_those_down_ge10=float((strong_down.down >= 10).mean()),
           share_words_RR_ge_R26=float((W.RR >= fr["R26"]["RR"]).mean()),
           share_words_RR_le_R24=float((W.RR <= fr["R24"]["RR"]).mean()),
           share_words_abslogRR_ge_R24=float((W.logRR.abs() >= abs(np.log(fr["R24"]["RR"]))).mean()),
           families=fr)
# frequency-matched: words with 2025 rate >= 10 per 1k (R26 2025 rate ~23, R24 ~63 per 1k)
for lo in (10, 20):
    Wm = W[W.rate25_per1k >= lo]
    res[f"freq_ge{lo}_n"] = len(Wm)
    res[f"freq_ge{lo}_share_RR_ge_R26"] = float((Wm.RR >= fr["R26"]["RR"]).mean())
    res[f"freq_ge{lo}_share_RR_le_R24"] = float((Wm.RR <= fr["R24"]["RR"]).mean())
    res[f"freq_ge{lo}_share_up_ge12"] = float((Wm.up >= 12).mean())
    res[f"freq_ge{lo}_share_down_ge10"] = float((Wm.down >= 10).mean())
    res[f"freq_ge{lo}_share_pass_either_H3b_threshold"] = float(((Wm.up >= 12) | (Wm.down >= 10)).mean())
# (2) random families of 4 words with 2025 rate in [2, 12] per 1k (R26 words: 'unified' 9, beyond 9, bridging 4)
rng = np.random.default_rng(1)
pool = np.flatnonzero((W.rate25_per1k.values >= 2) & (W.rate25_per1k.values <= 15))
fam_rr, fam_up = [], []
for _ in range(2000):
    j = rng.choice(pool, 4, replace=False)
    # any-of family indicator per title
    v = (X[:, j].sum(axis=1).A.ravel() > 0).astype(float)
    k, n = area_counts(v)
    u, dn, r, _ = summarise(k[None], n)
    fam_rr.append(r[0]); fam_up.append(u[0])
fam_rr = np.array(fam_rr); fam_up = np.array(fam_up)
res["random4_n_pool_words"] = int(len(pool))
res["random4_share_RR_ge_R26"] = float((fam_rr >= fr["R26"]["RR"]).mean())
res["random4_share_RR_le_R24"] = float((fam_rr <= fr["R24"]["RR"]).mean())
res["random4_share_up_ge12"] = float((fam_up >= 12).mean())
res["random4_share_down_ge10"] = float(((16 - fam_up) >= 10).mean())
res["random4_RR_quantiles"] = np.quantile(fam_rr, [0.01, 0.05, 0.5, 0.95, 0.99]).round(3).tolist()
print(json.dumps({k: v for k, v in res.items() if k != "families"}, indent=1))
W.sort_values("logRR").to_csv(OUT / "ident_B_word_churn.csv", index=False)
print("top risers\n", W.sort_values("RR", ascending=False).head(25)[["word", "n", "rate25_per1k", "RR", "up"]].to_string())
print("top fallers\n", W.sort_values("RR").head(15)[["word", "n", "rate25_per1k", "RR", "down"]].to_string())
# (3) within topic100 Poisson (topic FE + year), 2025-26 all papers
import statsmodels.formula.api as smf, statsmodels.api as sm
a = df[df.year.isin([2025, 2026])].copy()
for fam_c in ("r24_any", "r26_any"):
    g = a.groupby(["topic100", "year"]).agg(k=(fam_c, "sum"), n=(fam_c, "size")).reset_index()
    g = g[g.groupby("topic100").k.transform("sum") > 0]
    g["y26"] = (g.year == 2026).astype(int)
    g["tc"] = g.topic100.astype(str)
    m = smf.glm("k ~ tc + y26", g, offset=np.log(g.n), family=sm.families.Poisson()).fit(scale="X2")
    ci = m.conf_int().loc["y26"]
    res[f"topic100FE_RR_{fam_c}"] = [float(np.exp(m.params["y26"])), float(np.exp(ci[0])), float(np.exp(ci[1]))]
    # area FE for comparison
    g2 = a.groupby(["area_h", "year"]).agg(k=(fam_c, "sum"), n=(fam_c, "size")).reset_index()
    g2["y26"] = (g2.year == 2026).astype(int)
    g2["ac"] = g2.area_h.astype(str)
    m2 = smf.glm("k ~ ac + y26", g2, offset=np.log(g2.n), family=sm.families.Poisson()).fit(scale="X2")
    res[f"areaFE_RR_{fam_c}"] = float(np.exp(m2.params["y26"]))
    # crude
    res[f"crude_RR_{fam_c}"] = float(a[a.year == 2026][fam_c].mean() / a[a.year == 2025][fam_c].mean())
# concentration of R26 excess by topic100: excess = k26 - n26 * rate25(topic)
g = a.groupby(["topic100", "year"]).agg(k=("r26_any", "sum"), n=("r26_any", "size")).unstack("year").fillna(0)
exc = g[("k", 2026)] - g[("n", 2026)] * (g[("k", 2025)] / g[("n", 2025)].clip(lower=1))
exc = exc.sort_values(ascending=False)
res["R26_excess_total"] = float(exc.sum())
res["R26_excess_share_top5_topics"] = float(exc.head(5).sum() / exc.sum())
res["R26_excess_share_top10_topics"] = float(exc.head(10).sum() / exc.sum())
res["R26_excess_share_llm_cluster_topics"] = None
lab = df.groupby("topic100").llm_topic.mean()
res["R26_top5_topics"] = [(int(t), float(e), float(lab[t])) for t, e in exc.head(5).items()]
# R26 per word in llm_topic vs non-llm 2025->26
for w in ("r26_unified", "r26_beyond", "r26_bridging", "r26_unifying"):
    res[f"{w}_per1k_25_26_llm"] = [float(1000 * a[(a.year == y) & (a.llm_topic == 1)][w].astype(int).mean()) for y in (2025, 2026)]
    res[f"{w}_per1k_25_26_nonllm"] = [float(1000 * a[(a.year == y) & (a.llm_topic == 0)][w].astype(int).mean()) for y in (2025, 2026)]
print(json.dumps({k: v for k, v in res.items() if k.startswith(("topic", "area", "crude", "R26", "r26"))}, indent=1))
json.dump(res, open(OUT / "ident_B_churn.json", "w"), indent=1, default=float)

# (4) neutral counterparts: does R24 fall more than its meaning-matched neutral words (within area)?
tl = a.title_nfkc.fillna("").str.lower()
a["n24"] = C.rx_contains(tl, r"\b(improv\w*|utili[sz]\w*|exploit\w*)").astype(int)
a["imp"] = C.rx_contains(tl, r"\bimprov\w*").astype(int)
a["enh"] = a.r24_enhanc.astype(int)
out4 = {}
for c in ("r24_any", "n24", "enh", "imp"):
    g2 = a[a.area_h.isin(big)].groupby(["area_h", "year"]).agg(k=(c, "sum"), n=(c, "size")).reset_index()
    g2["y26"] = (g2.year == 2026).astype(int); g2["ac"] = g2.area_h.astype(str)
    m2 = smf.glm("k ~ ac + y26", g2, offset=np.log(g2.n), family=sm.families.Poisson()).fit(scale="X2")
    ci = m2.conf_int().loc["y26"]
    w = g2.pivot(index="area_h", columns="year", values=["k", "n"])
    down = int(((w["k"][2026] / w["n"][2026]) < (w["k"][2025] / w["n"][2025])).sum())
    out4[c] = dict(RR=float(np.exp(m2.params["y26"])), lo=float(np.exp(ci[0])), hi=float(np.exp(ci[1])), down_of_16=down,
                   per1k_25=float(1000 * a[a.year == 2025][c].mean()), per1k_26=float(1000 * a[a.year == 2026][c].mean()))
# relative: R24 vs N24 stacked Poisson with family x year interaction
st = []
for c in ("r24_any", "n24"):
    g2 = a[a.area_h.isin(big)].groupby(["area_h", "year"]).agg(k=(c, "sum"), n=(c, "size")).reset_index()
    g2["fam"] = c; st.append(g2)
st = pd.concat(st); st["y26"] = (st.year == 2026).astype(int); st["r24"] = (st.fam == "r24_any").astype(int)
st["af"] = st.area_h.astype(str) + "_" + st.fam
m3 = smf.glm("k ~ af + y26 + y26:r24", st, offset=np.log(st.n), family=sm.families.Poisson()).fit(scale="X2")
ci = m3.conf_int().loc["y26:r24"]
out4["R24_vs_N24_ratio_of_RR"] = [float(np.exp(m3.params["y26:r24"])), float(np.exp(ci[0])), float(np.exp(ci[1]))]
# meaning-fixed: improve-slot LLM share within area 2025 vs 2026
import json as _j
inv = _j.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
pooled = []
for s_ in D3.SLOTS:
    y_, _ = D3.slot_y(a, s_, inv)
    pooled.append(pd.DataFrame({"area_h": a.area_h, "year": a.year, "y": y_, "slot": s_}).dropna())
pooled = pd.concat(pooled)
pb = pooled[pooled.area_h.isin(big)]
sh = pb.groupby(["area_h", "year"]).y.mean().unstack()
out4["slot_llm_share_within_area_up_2025_26_of_16"] = int((sh[2026] > sh[2025]).sum())
out4["slot_llm_share_pooled_2025_2026"] = [float(pb[pb.year == 2025].y.mean()), float(pb[pb.year == 2026].y.mean())]
import statsmodels.formula.api as smf2
pb = pb.assign(y26=(pb.year == 2026).astype(int), ac=pb.area_h.astype(str), sl=pb.slot.astype(str))
mm = smf2.logit("y ~ sl + ac + y26", pb).fit(disp=0, cov_type="cluster", cov_kwds={"groups": pd.factorize(pb.ac)[0]})
ci = mm.conf_int().loc["y26"]
out4["slot_llm_share_OR_2026_vs_2025_slotFE_areaFE"] = [float(np.exp(mm.params["y26"])), float(np.exp(ci[0])), float(np.exp(ci[1]))]
print(json.dumps(out4, indent=1))
res["neutral_counterparts"] = out4
json.dump(res, open(OUT / "ident_B_churn.json", "w"), indent=1, default=float)
