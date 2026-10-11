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

Outputs (outputs/d3_register/): register_rates.csv (area x year x family/word), register_area_tests.csv,
register_poisson.csv, register_results.json, area_imputation.json, fig_F3_2_register_heatmap.{pdf,png,csv}

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


def fig_f32(R: pd.DataFrame, big: list[str], order_n: pd.Series):
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    years = [2023, 2024, 2025, 2026]
    rows = ["All areas"] + sorted(big, key=lambda a: -order_n[a])
    fig, axes = C.new_fig("double", height=4.0, ncols=2, gridspec_kw={"wspace": 0.04})
    data = []
    for ax, fam, col, title in [(axes[0], "r24_any", C.COLORS[0], "R24 titles per 1,000"),
                                (axes[1], "r26_any", C.COLORS[1], "R26 titles per 1,000")]:
        M = np.full((len(rows), len(years)), np.nan)
        for j, y in enumerate(years):
            sub = R[R.year == y]
            for i, a in enumerate(rows):
                if a == "All areas":
                    k, n = sub[f"k_{fam}"].sum(), sub.n.sum()
                else:
                    s = sub[sub.area == a]
                    k, n = (s[f"k_{fam}"].sum(), s.n.sum()) if len(s) else (0, 0)
                if n >= 30:
                    M[i, j] = 1000 * k / n
                data.append(dict(family=fam, area=a, year=y, n=int(n), k=int(k),
                                 rate_per_1k=1000 * k / n if n else np.nan, shown=bool(n >= 30),
                                 area_imputed=bool(y == 2023)))
        cmap = LinearSegmentedColormap.from_list(f"seq_{fam}", ["#f7f6f3", col])
        vmax = np.nanpercentile(M, 98)
        ax.imshow(np.ma.masked_invalid(M), cmap=cmap, vmin=0, vmax=vmax, aspect="auto")
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if np.isfinite(M[i, j]):
                    ax.text(j, i, f"{M[i, j]:.0f}", ha="center", va="center", fontsize=6.5,
                            color="#ffffff" if M[i, j] > 0.62 * vmax else C.TEXT)
                else:
                    ax.text(j, i, "n/a", ha="center", va="center", fontsize=6, color=C.TEXT2)
        ax.set_xticks(range(len(years)), ["2023*", "2024", "2025", "2026"])
        labs = [C.AREA_SHORT.get(a, a) for a in rows]
        ax.set_yticks(range(len(rows)), labs if ax is axes[0] else [""] * len(rows))
        ax.tick_params(length=0)
        ax.grid(False)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.axhline(0.5, color="#ffffff", lw=2)
        ax.set_title(title, loc="left", fontsize=8.5, pad=16)
        ax.xaxis.tick_top()
    fig.text(0.01, 0.005, "R24 = enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*; "
                          "R26 = unified, unifying, beyond, bridging (title words).\n"
                          "* 2023 areas imputed from abstract embeddings (classifier trained on 2025 labels). "
                          "Rows: areas with >= 500 titles in 2025-26. n/a: area not in that year's taxonomy.",
             fontsize=6.5, color=C.TEXT2)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
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
        ctx[fam] = dict(n_areas=len(rows), n_up_2024_to_2025=int(sum(rows)))

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
               per_area_primary=tests[(tests.variant == "all") & tests.family.isin(["r24_any", "r26_any"])]
               .to_dict(orient="records"),
               verdict_inputs=verdict, runtime_s=round(time.time() - t0, 1))
    D3.write_json(res, OUTDIR / "register_results.json")
    print("verdict", verdict, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
