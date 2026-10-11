"""WP7 / D3-H3b: register turnover within primary areas (PLAN.md D3).

R24 = {enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*} and R26 = {unified, unifying,
beyond, bridging} in the title (features_v2 r24_any / r26_any). Rates are titles containing any family word per 1,000
titles.

H3b test. Large areas = harmonised primary areas (area_h, the 2025/26 taxonomy) with >= 500 titles in 2025+2026
(the pilot rule; 16 areas). Prediction: from 2025 to 2026 the R24 rate falls in >= 10 of 16 areas and the R26 rate rises
in >= 12 of 16; falsified if fewer than 9 of 16 move in the predicted direction. One-sided sign tests (binomial, p=0.5)
and per-area exact conditional (binomial) rate ratios are reported.

Poisson model (PLAN): area x year cell counts with a log(#titles) offset, area FE + year FE, 2023-26. primary_area does
not exist before 2024, so 2023 areas are IMPUTED (deviation): a multinomial logistic regression on bge-small abstract
embeddings trained on 2025 papers (5-fold CV accuracy and the out-of-year 2024 accuracy are reported). The 2023 column
is used only for the heat map and the 2023-26 Poisson model, never for the H3b test (2025 vs 2026, real labels).

Fixer pass (audit/d3; added, not in the PLAN):
- Neutral-synonym benchmark (D3-ID-1): N24 = improv*|utili[sz]*|exploit* in the title; within-area quasi-Poisson RR
  2026/2025 for N24 next to R24, and the stacked ratio of RRs (R24 vs N24, area x family FE). A register turnover would
  need R24 to fall relative to N24; also the meaning-fixed check: LLM-variant share of slot-filled titles 2026 vs 2025
  (logit, slot FE + area FE, topic100 clusters) and the number of large areas where it rose. All papers and NA pool.
- Word-churn benchmark (D3-ID-2): every title word with >= 80 titles in 2025+2026 (large areas) gets the same 16-area
  sign count and an area-stratified (Mantel-Haenszel) RR; reports how often words with a large aggregate move pass the
  H3b thresholds, where R24/R26 fall in that distribution, and random 4-word families matched on the 2025 rate. R26 was
  chosen after the scout/pilot saw it rise in this same discovery data, so its sign test is descriptive.
- 2024 -> 2025 context (D3-C8) crosses the 2025 taxonomy change; a sensitivity reassigns 2025 papers in the two new
  areas to a 2024-taxonomy area with a classifier trained on 2024 labels (bge abstract embeddings).
- F3.2: common colour scale for both panels with a colourbar each; cells with n < 100 greyed with n printed.

Outputs (outputs/d3_register/): register_rates.csv (area x year x family/word), register_area_tests.csv,
register_poisson.csv, register_results.json, area_imputation.json, register_neutral_benchmark.csv,
register_word_churn.csv, fig_F3_2_register_heatmap.{pdf,png,csv}

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d3_register
"""
from __future__ import annotations

import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d3_slots as D3

warnings.filterwarnings("ignore")
OUTDIR = D3.OUTDIR
R24_WORDS = ["enhanc", "leverag", "unveil", "unleash", "harness", "empower", "elevat", "boost"]
R26_WORDS = ["unified", "unifying", "beyond", "bridging"]
MIN_AREA_N = 500
NEW_2025 = ["foundation or frontier models, including LLMs", "learning on time series and dynamical systems"]
N24_RX = r"\b(improv\w*|utili[sz]\w*|exploit\w*)"
SEED = D3.SEED


def _pois_y26(g: pd.DataFrame, fe: str = "ac") -> tuple[float, float, float]:
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    m = smf.glm(f"k ~ {fe} + y26", g, offset=np.log(g.n), family=sm.families.Poisson()).fit(scale="X2")
    b, se = float(m.params["y26"]), float(m.bse["y26"])
    return float(np.exp(b)), float(np.exp(b - 1.96 * se)), float(np.exp(b + 1.96 * se))


def neutral_benchmark(df: pd.DataFrame, big: list[str]) -> tuple[pd.DataFrame, dict]:
    """D3-ID-1: does R24 fall relative to its neutral synonyms, and does the within-slot LLM share fall?"""
    import json
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    a = df[df.year.isin([2025, 2026]) & df.area_h.isin(big)].copy()
    tl = a.title_nfkc.fillna("").str.lower()
    a["n24"] = C.rx_contains(tl, N24_RX).astype(int)
    a["n24_improv"] = C.rx_contains(tl, r"\bimprov\w*").astype(int)
    a["r24_enh"] = a.r24_enhanc.astype(int)
    rows, out = [], {}
    for samp, d in [("all", a), ("NA pool", a[a.NA == 1])]:
        for c, lab in [("r24_any", "R24 (LLM-favoured family)"), ("n24", "N24 = improv*|utili[sz]*|exploit* (neutral)"),
                       ("r24_enh", "enhanc*"), ("n24_improv", "improv*")]:
            g = d.groupby(["area_h", "year"]).agg(k=(c, "sum"), n=(c, "size")).reset_index()
            g["y26"], g["ac"] = (g.year == 2026).astype(int), g.area_h.astype(str)
            rr, lo, hi = _pois_y26(g)
            w = g.pivot(index="area_h", columns="year", values=["k", "n"])
            down = int(((w["k"][2026] / w["n"][2026]) < (w["k"][2025] / w["n"][2025])).sum())
            rows.append(dict(sample=samp, outcome=c, label=lab, RR_2026_vs_2025=rr, lo=lo, hi=hi, down_of_16=down,
                             per1k_2025=1000 * d[d.year == 2025][c].mean(), per1k_2026=1000 * d[d.year == 2026][c].mean()))
        st = []
        for c in ("r24_any", "n24"):
            g = d.groupby(["area_h", "year"]).agg(k=(c, "sum"), n=(c, "size")).reset_index()
            g["fam"] = c
            st.append(g)
        st = pd.concat(st)
        st["y26"], st["r24"] = (st.year == 2026).astype(int), (st.fam == "r24_any").astype(int)
        st["af"] = st.area_h.astype(str) + "_" + st.fam
        m = smf.glm("k ~ af + y26 + y26:r24", st, offset=np.log(st.n), family=sm.families.Poisson()).fit(scale="X2")
        b, se = float(m.params["y26:r24"]), float(m.bse["y26:r24"])
        out[f"{samp}|R24_vs_N24_ratio_of_RR"] = dict(ratio=float(np.exp(b)), lo=float(np.exp(b - 1.96 * se)),
                                                     hi=float(np.exp(b + 1.96 * se)),
                                                     p_one_R24_falls_more=float(stats.norm.cdf(b / se)))
        # meaning-fixed: LLM-variant share of slot-filled titles, 2026 vs 2025, within slot and area
        inv = json.loads((OUTDIR / "slot_inventory.json").read_text())["inventory"]
        P = D3.slot_panel(d, inv, controls=False, years_from=2025)
        P = P.merge(d[["submission_id", "area_h"]], on="submission_id", how="left")
        P["y26"], P["ac"] = (P.year == 2026).astype(int), P.area_h.astype(str)
        r = C.logit("y ~ C(slot) + ac + y26", P, cluster="topic100")
        t = C.or_table(r, ["y26"]).iloc[0]
        sh = P.groupby(["area_h", "year"]).y.mean().unstack()
        out[f"{samp}|slot_llm_share"] = dict(share_2025=float(P[P.year == 2025].y.mean()),
                                             share_2026=float(P[P.year == 2026].y.mean()),
                                             n_2025=int((P.year == 2025).sum()), n_2026=int((P.year == 2026).sum()),
                                             OR_2026_vs_2025=float(t.OR), lo=float(t.OR_lo), hi=float(t.OR_hi),
                                             n_areas_share_up=int((sh[2026] > sh[2025]).sum()),
                                             n_areas_share_down=int((sh[2026] < sh[2025]).sum()))
    return pd.DataFrame(rows), out


def word_churn(df: pd.DataFrame, big: list[str], n_rand: int = 1000) -> tuple[pd.DataFrame, dict]:
    """D3-ID-2: how informative is the 16-area sign test? Same statistics for every title word with >= 80 titles
    in 2025+2026 (large areas): area sign counts and the area-stratified Mantel-Haenszel RR 2026/2025."""
    import re
    from collections import Counter
    import scipy.sparse as sp
    d = df[df.year.isin([2025, 2026]) & df.area_h.isin(big)].reset_index(drop=True)
    tok = d.title_nfkc.fillna("").str.lower().map(lambda t: set(re.findall(r"[a-z][a-z\-]{2,}", t)))
    cnt = Counter(w for s_ in tok for w in s_)
    vocab = sorted(w for w, c in cnt.items() if c >= 80)
    widx = {w: i for i, w in enumerate(vocab)}
    ri, ci = [], []
    for i, s_ in enumerate(tok):
        for w in s_:
            j = widx.get(w)
            if j is not None:
                ri.append(i)
                ci.append(j)
    X = sp.csr_matrix((np.ones(len(ri)), (ri, ci)), shape=(len(d), len(vocab)))
    cells = d.groupby(["area_h", "year"]).indices
    N = np.array([[len(cells[(a, y)]) for y in (2025, 2026)] for a in big], float)
    sel = [[cells[(a, y)] for y in (2025, 2026)] for a in big]

    def counts(M):  # M: n x k (sparse or dense 2-d)
        K = np.zeros((M.shape[1], len(big), 2))
        for ai in range(len(big)):
            for yi in range(2):
                K[:, ai, yi] = np.asarray(M[sel[ai][yi]].sum(axis=0)).ravel()
        return K

    def summ(K):
        r25, r26 = K[..., 0] / N[:, 0], K[..., 1] / N[:, 1]
        up, down = (r26 > r25).sum(-1), (r26 < r25).sum(-1)
        num = (K[..., 1] * N[:, 0] / N.sum(1)).sum(-1)
        den = (K[..., 0] * N[:, 1] / N.sum(1)).sum(-1)
        return up, down, num / np.maximum(den, 1e-9), K[..., 0].sum(-1) / N[:, 0].sum()
    up, down, rr, r25 = summ(counts(X))
    W = pd.DataFrame(dict(word=vocab, n_titles=[cnt[w] for w in vocab], up_of_16=up, down_of_16=down, RR_MH=rr,
                          rate2025_per1k=1000 * r25))
    fam = {}
    for f, c in [("R24", "r24_any"), ("R26", "r26_any")]:
        u, dn, r_, q = summ(counts(d[[c]].to_numpy(float)))
        fam[f] = dict(up_of_16=int(u[0]), down_of_16=int(dn[0]), RR_MH=float(r_[0]), rate2025_per1k=float(1000 * q[0]))
    big_up, big_dn = W[W.RR_MH >= 1.5], W[W.RR_MH <= 0.8]
    freq = W[W.rate2025_per1k >= 20]
    res = dict(n_words=len(W), families=fam,
               share_words_RR_ge_R26=float((W.RR_MH >= fam["R26"]["RR_MH"]).mean()),
               share_words_RR_le_R24=float((W.RR_MH <= fam["R24"]["RR_MH"]).mean()),
               n_words_RR_ge_1p5=len(big_up), share_of_those_up_ge12=float((big_up.up_of_16 >= 12).mean()),
               n_words_RR_le_0p8=len(big_dn), share_of_those_down_ge10=float((big_dn.down_of_16 >= 10).mean()),
               n_words_rate_ge20=len(freq),
               share_freq_words_pass_either_threshold=float(((freq.up_of_16 >= 12) | (freq.down_of_16 >= 10)).mean()),
               words_up_16_of_16=W[W.up_of_16 == 16].sort_values("RR_MH", ascending=False).word.tolist(),
               words_up_15_of_16=W[W.up_of_16 == 15].sort_values("RR_MH", ascending=False).word.tolist())
    rng = np.random.default_rng(SEED)
    pool = np.flatnonzero((W.rate2025_per1k.values >= 2) & (W.rate2025_per1k.values <= 15))
    fr, fu = [], []
    for _ in range(n_rand):
        j = rng.choice(pool, 4, replace=False)
        v = (np.asarray(X[:, j].sum(axis=1)).ravel() > 0).astype(float)[:, None]
        u, _, r_, _ = summ(counts(v))
        fr.append(r_[0])
        fu.append(u[0])
    fr, fu = np.array(fr), np.array(fu)
    res.update(random4_n_draws=n_rand, random4_pool_words=int(len(pool)),
               random4_share_RR_ge_R26=float((fr >= fam["R26"]["RR_MH"]).mean()),
               random4_share_up_ge12=float((fu >= 12).mean()),
               random4_RR_q01_q50_q99=np.quantile(fr, [0.01, 0.5, 0.99]).round(3).tolist())
    return W.sort_values("RR_MH"), res


def context_reassigned(df: pd.DataFrame, big: list[str]) -> dict:
    """D3-C8: 2024 -> 2025 R24/R26 direction across the 14 large areas present in both taxonomies, raw and with 2025
    papers of the two new areas reassigned to a 2024-taxonomy area (classifier on 2024 labels, bge embeddings)."""
    from sklearn.linear_model import LogisticRegression
    d = df[df.year.isin([2024, 2025])].copy()
    E = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    tr = (d.year == 2024).to_numpy()
    clf = LogisticRegression(max_iter=2000, C=1.0).fit(E[tr], d.loc[tr, "area_h"].astype(str).to_numpy())
    mv = ((d.year == 2025) & d.area_h.isin(NEW_2025)).to_numpy()
    d["area_ctx"] = d.area_h.astype(object)
    d.loc[mv, "area_ctx"] = clf.predict(E[mv])
    areas14 = [a for a in big if a not in NEW_2025]
    out = dict(n_reassigned_2025=int(mv.sum()),
               reassigned_to=pd.Series(d.loc[mv, "area_ctx"]).value_counts().head(6).to_dict())
    for lab, col in [("raw (2025 native labels)", "area_h"), ("new 2025 areas reassigned", "area_ctx")]:
        R = rates(d, col, ["r24_any", "r26_any"])
        for fam in ("r24_any", "r26_any"):
            up = 0
            for a in areas14:
                r4 = R[(R.area == a) & (R.year == 2024)].iloc[0]
                r5 = R[(R.area == a) & (R.year == 2025)].iloc[0]
                up += int(r5[f"k_{fam}"] / r5.n > r4[f"k_{fam}"] / r4.n)
            g = R[R.area.isin(areas14)].rename(columns={f"k_{fam}": "k"}).copy()
            g["y26"], g["ac"] = (g.year == 2024).astype(int), g.area.astype(str)  # y26 = indicator for 2024 here
            rr, lo, hi = _pois_y26(g)
            out[f"{lab}|{fam}"] = dict(n_areas=len(areas14), n_up_2024_to_2025=up, RR_2024_vs_2025=rr, lo=lo, hi=hi)
    out["note"] = ("2024 -> 2025 crosses the 2025 taxonomy change (two new areas absorb papers that 2024 filed "
                   "elsewhere); read as taxonomy-confounded context, not as a within-area comparison")
    return out


def impute_2023_area(df: pd.DataFrame) -> tuple[pd.Series, dict]:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score, StratifiedKFold
    E = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    tr = (df.year == 2025).to_numpy()
    clf = LogisticRegression(max_iter=2000, C=1.0)
    ytr = df.loc[tr, "area_h"].astype(str).to_numpy()
    cv = cross_val_score(clf, E[tr], ytr, cv=StratifiedKFold(5, shuffle=True, random_state=0), n_jobs=1)
    clf.fit(E[tr], ytr)
    m24 = (df.year == 2024).to_numpy()
    acc24 = float((clf.predict(E[m24]) == df.loc[m24, "area_h"].astype(str).to_numpy()).mean())
    m23 = (df.year == 2023).to_numpy()
    pred = pd.Series(np.nan, index=df.index, dtype=object)
    pred[m23] = clf.predict(E[m23])
    # predicted 2024 distribution vs true (taxonomy-transfer check)
    p24 = pd.Series(clf.predict(E[m24])).value_counts(normalize=True)
    t24 = df.loc[m24, "area_h"].value_counts(normalize=True)
    tv24 = 0.5 * float((p24.reindex(t24.index.union(p24.index)).fillna(0) -
                        t24.reindex(t24.index.union(p24.index)).fillna(0)).abs().sum())
    meta = dict(method="multinomial logistic regression (C=1) on bge-small-en-v1.5 abstract embeddings, trained on 2025 "
                       "papers (area_h, 21 areas)", n_train=int(tr.sum()), cv5_accuracy_2025=float(cv.mean()),
                cv5_accuracy_sd=float(cv.std()), accuracy_on_2024_true_labels=acc24,
                total_variation_pred_vs_true_2024_mix=tv24, n_imputed_2023=int(m23.sum()),
                note="2024 true labels lack 'foundation or frontier models' and 'time series' (2025+ only), so the "
                     "2024 accuracy is a pessimistic transfer check")
    return pred, meta


def rates(d: pd.DataFrame, area_col: str, cols: list[str]) -> pd.DataFrame:
    g = d.groupby([area_col, "year"])
    out = g.size().rename("n").to_frame()
    for c in cols:
        out[f"k_{c}"] = g[c].sum()
    out = out.reset_index().rename(columns={area_col: "area"})
    return out


def exact_rr(x25, n25, x26, n26, alpha=0.05):
    """Conditional binomial exact CI for the rate ratio (2026 / 2025)."""
    m = x25 + x26
    rr = (x26 / n26) / (x25 / n25) if x25 > 0 else np.inf
    if m == 0:
        return rr, np.nan, np.nan, np.nan, np.nan
    lo = stats.beta.ppf(alpha / 2, x26, m - x26 + 1) if x26 > 0 else 0.0
    hi = stats.beta.ppf(1 - alpha / 2, x26 + 1, m - x26) if x26 < m else 1.0
    f = lambda p: p * n25 / ((1 - p) * n26) if p < 1 else np.inf  # noqa: E731
    p0 = n26 / (n25 + n26)
    p_down = stats.binom.cdf(x26, m, p0)  # one-sided: rate fell
    p_up = stats.binom.sf(x26 - 1, m, p0)  # one-sided: rate rose
    return rr, f(lo), f(hi), p_down, p_up


def area_tests(R: pd.DataFrame, big: list[str], fam: str) -> pd.DataFrame:
    rows = []
    for a in big:
        r25 = R[(R.area == a) & (R.year == 2025)].iloc[0]
        r26 = R[(R.area == a) & (R.year == 2026)].iloc[0]
        x25, n25, x26, n26 = r25[f"k_{fam}"], r25.n, r26[f"k_{fam}"], r26.n
        rr, lo, hi, pd_, pu = exact_rr(x25, n25, x26, n26)
        rows.append(dict(family=fam, area=a, n_2025=int(n25), n_2026=int(n26), k_2025=int(x25), k_2026=int(x26),
                         rate_2025=1000 * x25 / n25, rate_2026=1000 * x26 / n26, RR=rr, RR_lo=lo, RR_hi=hi,
                         p_down=pd_, p_up=pu, down=bool(x26 / n26 < x25 / n25), up=bool(x26 / n26 > x25 / n25)))
    return pd.DataFrame(rows)


def sign_test(k: int, n: int) -> float:
    return float(stats.binom.sf(k - 1, n, 0.5))


def poisson_cells(R: pd.DataFrame, fam: str, years=(2023, 2024, 2025, 2026), areas=None) -> dict:
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    d = R[R.year.isin(years)].copy()
    if areas is not None:
        d = d[d.area.isin(areas)]
    d = d[d.n > 0]
    d["k"] = d[f"k_{fam}"]
    d["year_c"] = pd.Categorical(d.year.astype(str), categories=["2025"] + [str(y) for y in years if y != 2025])
    d["area_c"] = pd.Categorical(d.area.astype(str))  # (patsy's C() is shadowed by the _core alias)
    m = smf.glm("k ~ area_c + year_c", data=d, offset=np.log(d.n), family=sm.families.Poisson()).fit(scale="X2")
    out = dict(family=fam, years=list(years), n_cells=len(d), dispersion=float(m.scale))
    for y in years:
        if y == 2025:
            continue
        nm = f"year_c[T.{y}]"
        b, se = float(m.params[nm]), float(m.bse[nm])
        out[f"RR_{y}_vs_2025"] = np.exp(b)
        out[f"RR_{y}_vs_2025_lo"] = np.exp(b - 1.96 * se)
        out[f"RR_{y}_vs_2025_hi"] = np.exp(b + 1.96 * se)
        out[f"p_{y}_vs_2025_two"] = float(2 * stats.norm.sf(abs(b / se)))
    return out


def fig_f32(R: pd.DataFrame, big: list[str], order_n: pd.Series, min_n: int = 100):
    """Area x year heat map of R24 and R26 rates per 1,000 titles, 2023-26. One colour scale shared by both panels
    (0 to the 98th percentile of all shown cells), a colourbar per panel; cells with n < min_n are greyed, with n."""
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    years = [2023, 2024, 2025, 2026]
    rows = ["All areas"] + sorted(big, key=lambda a: -order_n[a])
    fig, axes = C.new_fig("double", height=4.4, ncols=2, gridspec_kw={"wspace": 0.04})
    data, Ms, Ns = [], {}, {}
    for fam in ("r24_any", "r26_any"):
        M = np.full((len(rows), len(years)), np.nan)
        Nn = np.zeros((len(rows), len(years)))
        for j, y in enumerate(years):
            sub = R[R.year == y]
            for i, a in enumerate(rows):
                if a == "All areas":
                    k, n = sub[f"k_{fam}"].sum(), sub.n.sum()
                else:
                    s_ = sub[sub.area == a]
                    k, n = (s_[f"k_{fam}"].sum(), s_.n.sum()) if len(s_) else (0, 0)
                Nn[i, j] = n
                if n > 0:
                    M[i, j] = 1000 * k / n
                data.append(dict(family=fam, area=a, year=y, n=int(n), k=int(k),
                                 rate_per_1k=1000 * k / n if n else np.nan, shown_coloured=bool(n >= min_n),
                                 area_imputed=bool(y == 2023 and a != "All areas")))
        Ms[fam], Ns[fam] = M, Nn
    shown = np.concatenate([Ms[f][Ns[f] >= min_n] for f in Ms])
    vmax = float(np.nanpercentile(shown, 98))
    for ax, fam, col, title in [(axes[0], "r24_any", C.COLORS[0], "R24 titles per 1,000"),
                                (axes[1], "r26_any", C.COLORS[1], "R26 titles per 1,000")]:
        M, Nn = Ms[fam], Ns[fam]
        cmap = LinearSegmentedColormap.from_list(f"seq_{fam}", ["#f7f6f3", col])
        cmap.set_bad("#ffffff")
        im = ax.imshow(np.ma.masked_where(~(Nn >= min_n), M), cmap=cmap, vmin=0, vmax=vmax, aspect="auto")
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if Nn[i, j] >= min_n:
                    ax.text(j, i, f"{M[i, j]:.0f}", ha="center", va="center", fontsize=6.5,
                            color="#ffffff" if M[i, j] > 0.62 * vmax else C.TEXT)
                elif Nn[i, j] > 0:
                    ax.text(j, i, f"{M[i, j]:.0f} (n={int(Nn[i, j])})", ha="center", va="center", fontsize=5.5,
                            color=C.TEXT2)
                else:
                    ax.text(j, i, "n/a", ha="center", va="center", fontsize=6, color=C.TEXT2)
        ax.set_xticks(range(len(years)), ["2023*", "2024", "2025", "2026"])
        labs = [C.AREA_SHORT.get(a, a) for a in rows]
        ax.set_yticks(range(len(rows)), labs if ax is axes[0] else [""] * len(rows))
        ax.tick_params(length=0)
        ax.grid(False)
        for s_ in ax.spines.values():
            s_.set_visible(False)
        ax.axhline(0.5, color="#ffffff", lw=2)
        ax.set_title(title, loc="left", fontsize=8.5, pad=16)
        ax.xaxis.tick_top()
        cb = fig.colorbar(im, ax=ax, orientation="horizontal", fraction=0.035, pad=0.02, aspect=30)
        cb.ax.tick_params(labelsize=6.5, length=2)
        cb.outline.set_visible(False)
        cb.set_label("titles per 1,000 (one scale for both panels)", fontsize=6.5, labelpad=1)
    fig.text(0.01, 0.005, "R24 = enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*; "
                          "R26 = unified, unifying, beyond, bridging (title words).\nRows: areas with >= 500 titles "
                          "in 2025-26. * 2023 area rows use areas imputed from abstract embeddings (classifier trained "
                          "on 2025 labels);\nthe 2023 All-areas value is observed. Grey text: cells with fewer than "
                          f"{min_n} titles (rate and n shown, not coloured). n/a: area not in that year's taxonomy.",
             fontsize=6.3, color=C.TEXT2)
    fig.subplots_adjust(left=0.2, right=0.99, top=0.9, bottom=0.15)
    return C.save_fig(fig, "fig_F3_2_register_heatmap", OUTDIR, data=pd.DataFrame(data))


def main():
    t0 = time.time()
    df = D3.load_frame()
    df = df[df.year >= 2023].copy()
    imp, imeta = impute_2023_area(df)
    df["area_all"] = df.area_h.astype(object).where(df.year >= 2024, imp)
    D3.write_json(imeta, OUTDIR / "area_imputation.json")
    print("imputation", imeta)
    df["r24_noamb"] = df[[f"r24_{w}" for w in R24_WORDS if w not in ("boost", "elevat")]].any(axis=1).astype(int)
    df["r24_noshared"] = df[[f"r24_{w}" for w in R24_WORDS if w not in ("harness", "unveil")]].any(axis=1).astype(int)
    word_cols = [f"r24_{w}" for w in R24_WORDS] + [f"r26_{w}" for w in R26_WORDS]
    for c in word_cols:
        df[c] = df[c].astype(int)
    fams = ["r24_any", "r26_any", "r24_n", "r26_n", "r24_noamb", "r24_noshared"] + word_cols

    n2526 = df[df.year.isin([2025, 2026])].groupby("area_h").size()
    big = sorted(n2526[n2526 >= MIN_AREA_N].index.tolist())
    print("large areas", len(big))
    R = rates(df, "area_all", fams)
    R["area_short"] = R.area.map(C.AREA_SHORT).fillna(R.area)
    R.to_csv(OUTDIR / "register_rates.csv", index=False)

    # ---- H3b tests (2025 vs 2026, real area labels)
    tests, summ = [], {}
    variants = [("all", df), ("NA pool", df[df.NA == 1]), ("non-LLM subset", df[df.non_llm == 1])]
    for vname, d in variants:
        Rv = rates(d, "area_all", fams)
        for fam, direction in [("r24_any", "down"), ("r26_any", "up"), ("r24_n", "down"), ("r26_n", "up"),
                               ("r24_noamb", "down"), ("r24_noshared", "down")] + \
                              [(f"r24_{w}", "down") for w in R24_WORDS] + [(f"r26_{w}", "up") for w in R26_WORDS]:
            at = area_tests(Rv, big, fam)
            at["variant"] = vname
            tests.append(at)
            k = int(at[direction].sum())
            tot = Rv[Rv.year.isin([2025, 2026])].groupby("year")[[f"k_{fam}", "n"]].sum()
            r25 = 1000 * tot.loc[2025, f"k_{fam}"] / tot.loc[2025, "n"]
            r26 = 1000 * tot.loc[2026, f"k_{fam}"] / tot.loc[2026, "n"]
            # 2026 standardised to the 2025 area mix (large areas)
            w25 = at.set_index("area").n_2025 / at.n_2025.sum()
            r26_std = float((at.set_index("area").rate_2026 * w25).sum())
            r25_big = float((at.set_index("area").rate_2025 * w25).sum())
            summ[f"{vname}|{fam}"] = dict(variant=vname, family=fam, direction=direction, n_areas=len(at),
                                         n_predicted_direction=k, sign_test_p_one=sign_test(k, len(at)),
                                         n_sig_area_p05=int((at[f"p_{direction}"] < 0.05).sum()),
                                         rate_2025_all=r25, rate_2026_all=r26, rate_2025_large_areas=r25_big,
                                         rate_2026_std_to_2025_mix=r26_std)
    tests = pd.concat(tests, ignore_index=True)
    tests["area_short"] = tests.area.map(C.AREA_SHORT).fillna(tests.area)
    tests.to_csv(OUTDIR / "register_area_tests.csv", index=False)
    summ_df = pd.DataFrame(summ.values())
    summ_df.to_csv(OUTDIR / "register_summary.csv", index=False)
    print(summ_df.to_string())

    # all 21 areas (small ones included; areas present in both years)
    at21 = {fam: area_tests(R, sorted(df.loc[df.year == 2025, "area_h"].dropna().unique()), fam)
            for fam in ("r24_any", "r26_any")}
    # 2024 -> 2025 (context: the R24 rise), 16 large areas minus the two 2025-only areas
    ctx = {}
    for fam, direction in [("r24_any", "up"), ("r26_any", "up")]:
        rows = []
        for a in [a for a in big if ((R.area == a) & (R.year == 2024)).any()]:
            r24_ = R[(R.area == a) & (R.year == 2024)].iloc[0]
            r25_ = R[(R.area == a) & (R.year == 2025)].iloc[0]
            rows.append((r25_[f"k_{fam}"] / r25_.n) > (r24_[f"k_{fam}"] / r24_.n))
        ctx[fam] = dict(n_areas=len(rows), n_up_2024_to_2025=int(sum(rows)), taxonomy_confounded=True)
    ctx["reassigned_sensitivity"] = context_reassigned(df, big)
    print("context 2024->2025", ctx)

    # ---- neutral-synonym benchmark and within-slot share (D3-ID-1); word churn (D3-ID-2)
    nb, nb_out = neutral_benchmark(df, big)
    nb.to_csv(OUTDIR / "register_neutral_benchmark.csv", index=False)
    print(nb.to_string())
    print(nb_out)
    wc, wc_out = word_churn(df, big)
    wc.to_csv(OUTDIR / "register_word_churn.csv", index=False)
    print({k: v for k, v in wc_out.items() if not k.startswith("words_")})

    # ---- Poisson (area FE + year FE, offset)
    pois = []
    for fam in ("r24_any", "r26_any", "r24_n", "r26_n"):
        for lab, yrs, areas in [("2023-26 (2023 imputed), large areas", (2023, 2024, 2025, 2026), big),
                                ("2024-26, large areas", (2024, 2025, 2026), big),
                                ("2025-26, large areas", (2025, 2026), big),
                                ("2023-26, all areas", (2023, 2024, 2025, 2026), None)]:
            r = poisson_cells(R, fam, yrs, areas)
            r["spec"] = lab
            pois.append(r)
    pois = pd.DataFrame(pois)
    pois.to_csv(OUTDIR / "register_poisson.csv", index=False)
    print(pois[["family", "spec", "dispersion", "RR_2026_vs_2025", "RR_2026_vs_2025_lo", "RR_2026_vs_2025_hi",
                "RR_2024_vs_2025"]].to_string())

    # ---- figure
    order_n = n2526
    fig_f32(R, big, order_n)

    # ---- verdict
    s24, s26 = summ["all|r24_any"], summ["all|r26_any"]
    verdict = dict(
        r24_down_areas=s24["n_predicted_direction"], r26_up_areas=s26["n_predicted_direction"], n_areas=len(big),
        r24_meets_prediction_ge10=bool(s24["n_predicted_direction"] >= 10),
        r26_meets_prediction_ge12=bool(s26["n_predicted_direction"] >= 12),
        falsified=bool(s24["n_predicted_direction"] < 9 or s26["n_predicted_direction"] < 9),
        p_sign_r24=s24["sign_test_p_one"], p_sign_r26=s26["sign_test_p_one"],
        p_H3b_intersection_union=float(max(s24["sign_test_p_one"], s26["sign_test_p_one"])))
    res = dict(hypothesis="H3b", large_areas=big, large_area_rule=f"area_h with >= {MIN_AREA_N} titles in 2025+2026",
               area_imputation=imeta, summary=summ, context_2024_to_2025=ctx,
               all21_areas={fam: dict(n_areas=len(a), n_down=int(a.down.sum()), n_up=int(a.up.sum()))
                            for fam, a in at21.items()},
               poisson=pois.to_dict(orient="records"),
               neutral_benchmark=dict(rates=nb.to_dict(orient="records"), **nb_out), word_churn=wc_out,
               per_area_primary=tests[(tests.variant == "all") & tests.family.isin(["r24_any", "r26_any"])]
               .to_dict(orient="records"),
               verdict_inputs=verdict, runtime_s=round(time.time() - t0, 1))
    D3.write_json(res, OUTDIR / "register_results.json")
    print("verdict", verdict, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
