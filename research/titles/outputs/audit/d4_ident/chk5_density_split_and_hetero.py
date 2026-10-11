"""D4 identification audit, check 5.
(a) Style-density marker selection: the year-specific excess words are selected on all of U (s0), which is ~70%
    non-accepted. Honest split: select the words on a random half of papers, measure stage gains on the other half
    (2 folds, swapped, 5 random splits). If the depletion survives, it is not a selection-on-the-sample artefact.
(b) R24 by stem, pre (2018-23) vs post (2024-26) identified-stage (camera-ready-free) and total gains.
(c) NAME G_total heterogeneity: LLM topic vs not; by harmonised area (2024-26). Does 'neutral' average over
    offsetting subgroups?
"""
import sys
import unicodedata
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d4_stage_gains as S  # noqa: E402

pd.set_option("display.width", 200)
df = S.load_frame(min_year=2018, density=True)
u = S.C.load_analysis_frame(feature_cols=["f24"], universe_cols=["submission_id", "year", "abstract"])
pool = S.lexicon()["style_pool"]
ab = u.abstract.fillna("").map(lambda x: unicodedata.normalize("NFKC", x).lower())
cv = CountVectorizer(lowercase=False, token_pattern=r"(?u)\b[a-z][a-z]+\b", binary=True, vocabulary=pool)
X = cv.fit_transform(ab.values).tocsr()
vocab = np.array(cv.get_feature_names_out())
nw = u.abstract.fillna("").str.split().str.len().clip(lower=1).to_numpy()
years = u.year.to_numpy()
pos = pd.Series(np.arange(len(u)), index=u.submission_id)


def select_words(mask):
    n_by = {y: int((years[mask] == y).sum()) for y in range(2017, 2027)}
    P = {y: np.asarray(X[mask & (years == y)].sum(axis=0)).ravel() / n_by[y] for y in range(2017, 2027)}
    bx = np.array([2021, 2022, 2023], float)
    B = np.column_stack([P[2021], P[2022], P[2023]])
    xm = bx.mean()
    slope = ((bx - xm) * (B - B.mean(1, keepdims=True))).sum(1) / ((bx - xm) ** 2).sum()
    icpt = B.mean(1) - slope * xm
    words = {}
    for Y in S.POST:
        lin = np.clip(icpt + slope * Y, 0, None)
        cons = np.maximum(lin, np.maximum(P[2022], P[2023]))
        qf = np.maximum(cons, 0.5 / n_by[2023])
        ratio = P[Y] / qf
        se = np.sqrt(qf * (1 - qf) / n_by[Y] + qf * (1 - qf) / n_by[2023])
        z = (P[Y] - cons) / se
        words[Y] = np.where((ratio >= 2) & (z > 4))[0]
    return words


def density_with(words):
    xs = np.zeros(len(u))
    for Y in range(2017, 2027):
        cols = words[Y] if Y in words else words[2024]
        m = years == Y
        xs[m] = np.asarray(X[np.where(m)[0]][:, cols].sum(axis=1)).ravel()
    return 100 * xs / nw


def gains(d, col):
    out = {}
    w = d[d.year.isin(S.POST)].groupby("year").size()
    w = w / w.sum()
    def P(st):
        return sum(w[y] * d.loc[(d.year == y) & (d[st] == 1), col].mean() for y in w.index)
    p = {st: P(st) for st in ["s0", "s2", "s3", "s0n", "s2n"]}
    return dict(total=p["s3"] / p["s0"], predec=p["s2"] / p["s0"], predec_crf=p["s2n"] / p["s0n"])


rng = np.random.default_rng(11)
rows = []
idx = pos.reindex(df.submission_id).to_numpy()
print("full-sample (original) density gains:", {k: round(v, 4) for k, v in gains(df, "xs_per100").items()})
for rep in range(5):
    half = rng.random(len(u)) < 0.5
    for fold, (sel, ev) in enumerate([(half, ~half), (~half, half)]):
        wds = select_words(sel)
        dens = density_with(wds)
        d = df.copy()
        d["dens_h"] = dens[idx]
        d = d[ev[idx]]
        g = gains(d, "dens_h")
        g.update(rep=rep, fold=fold, n_words_2026=len(wds[2026]))
        rows.append(g)
r = pd.DataFrame(rows)
print("(a) honest split-sample density gains (select on one half, evaluate on the other):")
print(r.round(4).to_string())
print("mean:", r[["total", "predec", "predec_crf"]].mean().round(4).to_dict())

# (b) R24 stems pre vs post
stems = ["r24_enhanc", "r24_leverag", "r24_unveil", "r24_unleash", "r24_harness", "r24_empower", "r24_elevat",
         "r24_boost"]
f = S.C.load_features(["submission_id"] + stems)
d = df.merge(f, on="submission_id", how="left")
print("\n(b) R24 stems: n (pre/post) and gains (year-standardised) pre 2018-23 vs post 2024-26")
for s in stems + ["r24_any"]:
    d[s] = d[s].astype(float)
    out = []
    for per, yrs in [("pre", S.PRE), ("post", S.POST)]:
        dd = d[d.year.isin(yrs)]
        w = dd.groupby("year").size()
        w = w / w.sum()
        def P(st):
            return sum(w[y] * dd.loc[(dd.year == y) & (dd[st] == 1), s].mean() for y in yrs)
        p = {st: P(st) for st in ["s0", "s2", "s3", "s0n", "s2n"]}
        out.append(f"{per}: n={int(dd[s].sum()):4d} total {p['s3'] / p['s0']:.3f} predec_crf {p['s2n'] / p['s0n']:.3f}")
    print(f"  {s:12s} " + " | ".join(out))

# (c) NAME heterogeneity, 2024-26
print("\n(c) NAME gains by subgroup, 2024-26 (year-standardised)")
post = df[df.year.isin(S.POST)].copy()
for name, grp in [("llm_topic", "llm_topic"), ("area", "area_h")]:
    res = []
    for g_, dd in post.groupby(grp):
        if len(dd) < 600:
            continue
        gg = gains(dd, "name_primary")
        w = dd.groupby("year").size()
        dec = sum((w[y] / w.sum()) * dd.loc[(dd.year == y) & (dd.s3 == 1), "name_primary"].mean() for y in w.index) / \
            sum((w[y] / w.sum()) * dd.loc[(dd.year == y) & (dd.s2 == 1), "name_primary"].mean() for y in w.index)
        res.append(dict(group=str(g_)[:40], n=len(dd), name_share=dd.name_primary.mean(), total=gg["total"],
                        predec=gg["predec"], dec=dec))
    print(pd.DataFrame(res).sort_values("total").round(3).to_string())
