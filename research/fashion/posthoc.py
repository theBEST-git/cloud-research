"""Post hoc exploratory analysis PH1 (PREREGISTRATION.md post-run record, 2026-10-16): among newcomer papers, what goes
with a higher acceptance rate? NOT pre-registered. Every estimate is an exploratory association within the stated
fixed effects; Holm adjustment within each block ranks the evidence, it does not make anything confirmatory.

Population: the RQ3 filter (decided ordinary submissions) with at least one author ID, 2019-2026 (E2's population).
Newcomer: no author ID with an earlier discovery submission in the same k100 topic (D1/D2).
  A1  newcomer papers only: acceptance ~ contribution class (ref. method) + FM + team-size band (ref. 3-4) + hot topic
      + topic maturity | topic FE + year dummies (one model)
  A2  newcomer papers only: acceptance ~ contribution class + FM | topic x year
  B   newcomer gap (newcomer minus incumbent) | topic x year, separately within each class, FM yes/no, team-size band,
      hot / not hot topic and topic-maturity tercile
  C   by coarse area (20): the newcomer gap | topic x year; and newcomer acceptance minus the same year's overall
      acceptance, per area (all years) and per area x year (cells with >= 50 newcomer papers; grey otherwise)

PH2 (2026-10-16): which contribution types and areas favour small or large teams?
Population: the RQ3 filter (decided ordinary submissions), 2018-2026, at least one author. Team size capped at 16.
  A  all papers: acceptance ~ team-size band (ref. 3-4) + class + FM | topic x year; and the slope per doubling of
     team size (log2), also with a newcomer control on papers with an author ID (2019-2026)
  B  slope per doubling and band effects (ref. 3-4), separately within each contribution class and each coarse area,
     controls class (areas only) + FM | topic x year; Holm across the slopes of each set
  H  heterogeneity: one pooled model per set with log2(team) x group interactions | topic x year; joint Wald F
     statistic that the slope is the same in every group. Its F(q, G - 1) p-value is NOT valid: in 40 simulated nulls
     it rejected 10% (classes) and 90% (areas) at 0.05, because each area's interaction rests on about 5 topic
     clusters. The p-value used is calibrated on the real design instead: the same F computed on 200 simulated null
     outcomes (dgp.simulate, alternating the dry-run's RQ3 lo/hi settings, real papers, topics, years and team sizes),
     p = (1 + #F_null >= F) / 201. The slope and band tests themselves were sized 5.1% and 4.8% in those nulls.

PH3 (2026-10-16): is the newcomer acceptance gap about who the authors are? Author fixed effects.
Population: PH1's (decided papers with an author ID, 2019-2026). Author rows: one per (paper, author ID); each paper
weighs 1 in total (weights 1 / its number of author IDs). Fixed effects absorbed jointly by alternating projections:
topic x year and author. Controls: class, FM, log2(team size), log(1 + the author's earlier ICLR submissions in any
topic). Singleton authors and cells are dropped iteratively. CR1 SE by k100 topic (a paper sits in one topic), and,
as a check, two-way by topic and author (Cameron-Gelbach-Miller; larger one-way variance if not positive).
  M0  newcomer paper | topic x year, same stacked sample, no author FE (the baseline the others are compared with)
  M1  newcomer paper | topic x year + author                      (the same people, newcomer vs incumbent papers)
  M2  the author is new to the topic | topic x year + author      (the same person, topics new to them vs not)
  M3  newcomer paper | topic x year + first author                (one row per paper)
  M4  newcomer paper | topic x year + last author                 (one row per paper)

PH4 (2026-10-17): which research areas are accepted more or less often, and how does that change over time?
Population: the RQ3 filter (decided ordinary submissions), 2018-2026. Two sets of units: K, author keywords typed
research_area / specific_topic / property / application_domain used by >= 200 discovery submissions (68; a paper is
in a keyword if it lists it); T, the 100 k100 topics. Per unit u and year t, the cell gap g = acceptance of u's papers
minus acceptance of all other papers of year t, with binomial variance (rates shrunk to (k + 0.5) / (n + 1)).
  level   paper-weighted mean of g over 2018-2026; SE from the cell variances x max(1, sqrt(phi)), phi = dispersion of g
          around the level over the m years with >= 10 papers in u; p from t(m - 1)
  recent  the same over 2024-2026 (the unit's phi and m)
  trend   WLS of g on year (weights 1 / variance) over the m years with >= 10 papers, pp per year; SE x max(1,
          sqrt(weighted RSS / (m - 2))); p from t(m - 2); only if m >= 4
  adjusted level (check): LPM accepted ~ member + class + FM + log2 team | year FE, HC1 SE
Benjamini-Hochberg q within each set and estimand ("flagged": q < 0.05), Holm alongside, and a calibration on 200
within-year permutations of acceptance (per-test rejection at 0.05; share of permutations with any BH flag).

    python research/fashion/posthoc.py ph1|ph2|ph3|ph4   (only after the frozen run; code committed: outcomes.py)
    python research/fashion/posthoc.py plot2|plot3|plot4 (redraw from the saved estimates; reads no outcome)
Writes output/posthoc/ph{1,2,3,4}_*.csv and *.json and output/figures/PH{1,2,3,4}_*.png/pdf.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

import figures
import outcomes
import panel
from analysis import estimate
from common import OUTPUT, TOPICS, topic_layer
from dgp import simulate
from ols import demean, fe_ols
from panel import CLASS_CONTROLS
from variants import holm

OUT = OUTPUT / "posthoc"
YEARS = (2019, 2026)
CLASSES = ["method", "theory", "empirical", "dataset_benchmark", "evaluation", "other"]
BANDS = ["1-2", "3-4", "5-6", "7+"]
MIN_CELL = 50
TEAM_CAP = 16


def with_outcomes(load=None) -> pd.DataFrame:
    """The k100 frame with the post hoc outcome columns (the only place post hoc code reads outcomes)."""
    k = panel.frame("k100")
    out = (load or outcomes.load)("posthoc", k.submission_id)
    assert (out.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    return k.assign(rq3=out.rq3.to_numpy(), accepted=out.accepted.to_numpy())


def population(k: pd.DataFrame | None = None) -> pd.DataFrame:
    """PH1 population (E2's): decided papers with an author ID, 2019-2026."""
    k = with_outcomes() if k is None else k
    d = k[k.rq3 & k.has_author_key & k.year.between(*YEARS)].copy()
    return add_columns(d)


def add_columns(d: pd.DataFrame) -> pd.DataFrame:
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    d["area"] = d.topic.map(cat[cat.level == "mid"].set_index("topic").parent_coarse)
    d["area_name"] = d.area.map(cat[cat.level == "coarse"].set_index("topic").name)
    d["band"] = pd.cut(d.team_size, [0, 2, 4, 6, np.inf], labels=BANDS).astype(str)
    d["maturity_tercile"] = pd.qcut(d.maturity, 3, labels=["young", "middle", "mature"]).astype(str)
    for b in BANDS:
        d[f"band_{b}"] = (d.band == b).astype(float)
    d["incumbent"] = 1 - d.newcomer
    d["log2_team"] = np.log2(d.team_size.clip(lower=1, upper=TEAM_CAP))
    return d


def mean_diff(e: pd.Series, clusters: pd.Series) -> tuple[float, float, float, int]:
    """Mean of e with a CR1 cluster-robust SE (t with G - 1 df): (mean, se, p, G)."""
    n, m = len(e), float(e.mean())
    sums = (e - m).groupby(clusters.to_numpy()).sum()
    G = len(sums)
    if G < 2:
        return m, np.nan, np.nan, G
    se = float(np.sqrt(G / (G - 1) * (sums ** 2).sum()) / n)
    return m, se, float(2 * stats.t.sf(abs(m / se), G - 1)) if se > 0 else np.nan, G


def row(block: str, label: str, coef: float, se: float, p: float, n: int, dof: float, **extra) -> dict:
    q = stats.t.ppf(0.975, dof) if np.isfinite(dof) and dof > 0 else np.nan
    return {"block": block, "label": label, "coef": coef, "se": se, "p": p, "ci95_lo": coef - q * se,
            "ci95_hi": coef + q * se, "n": n, **extra}


def block_a(d: pd.DataFrame) -> list[dict]:
    nc = d[d.newcomer == 1].reset_index(drop=True)
    years = pd.get_dummies(nc.year, prefix="y", drop_first=True).astype(float)
    bands = [f"band_{b}" for b in BANDS if b != "3-4"]
    X = pd.concat([nc[CLASS_CONTROLS + ["fm"] + bands + ["hot", "maturity"]].astype(float), years], axis=1)
    r = fe_ols(nc.accepted.astype(float), X, nc.topic, nc.topic)
    rows = [row("A1", c, r.loc[c, "coef"], r.loc[c, "se"], r.loc[c, "p"], int(r.loc[c, "n"]), r.loc[c, "clusters"] - 1)
            for c in CLASS_CONTROLS + ["fm"] + bands + ["hot", "maturity"]]
    r2 = fe_ols(nc.accepted.astype(float), nc[CLASS_CONTROLS + ["fm"]].astype(float), nc.cell, nc.topic)
    rows += [row("A2", c, r2.loc[c, "coef"], r2.loc[c, "se"], r2.loc[c, "p"], int(r2.loc[c, "n"]), r2.loc[c, "clusters"] - 1)
             for c in CLASS_CONTROLS + ["fm"]]
    return rows


def gap(df: pd.DataFrame, block: str, label: str, controls) -> dict:
    e = estimate(df, "accepted", "newcomer", tuple(controls), "cell", YEARS)
    g = df.groupby("newcomer").accepted
    return row(block, label, e["coef"], e["se"], e["p"], e["n"], e["dof"],
               newcomer_papers=int((df.newcomer == 1).sum()), incumbent_papers=int((df.newcomer == 0).sum()),
               newcomer_rate=float(g.mean().get(1.0, np.nan)), incumbent_rate=float(g.mean().get(0.0, np.nan)))


def block_b(d: pd.DataFrame) -> list[dict]:
    base = CLASS_CONTROLS + ["fm"]
    rows = [gap(d, "B", "all papers", base)]
    for c in CLASSES:
        rows.append(gap(d[d.primary_class == c], "B", f"class: {c}", ["fm"]))
    for v, name in [(1.0, "FM paper"), (0.0, "not FM paper")]:
        rows.append(gap(d[d.fm == v], "B", name, CLASS_CONTROLS))
    for b in BANDS:
        rows.append(gap(d[d.band == b], "B", f"team size {b}", base))
    for v, name in [(1.0, "hot topic"), (0.0, "not hot topic")]:
        rows.append(gap(d[d.hot == v], "B", name, base))
    for t in ["young", "middle", "mature"]:
        rows.append(gap(d[d.maturity_tercile == t], "B", f"{t} topic (maturity tercile)", base))
    return rows


def block_c(d: pd.DataFrame) -> tuple[list[dict], pd.DataFrame]:
    rows = []
    year_rate = d.groupby("year").accepted.mean()
    d = d.assign(excess=d.accepted - d.year.map(year_rate))
    nc = d[d.newcomer == 1]
    names = d.drop_duplicates("area").set_index("area").area_name
    for a in sorted(d.area.dropna().unique()):
        r = gap(d[d.area == a], "C-gap", f"{a} {names[a]}", CLASS_CONTROLS + ["fm"])
        rows.append(r)
        m, se, p, G = mean_diff(nc.excess[nc.area == a], nc.topic[nc.area == a])
        rows.append(row("C-level", f"{a} {names[a]}", m, se, p, int((nc.area == a).sum()), G - 1))
    cells = []
    for (a, y), g in nc.groupby(["area", "year"]):
        if len(g) < MIN_CELL:
            cells.append({"area": a, "area_name": names[a], "year": y, "n": len(g), "diff": np.nan, "p": np.nan})
            continue
        m, se, p, G = mean_diff(g.excess, g.topic)
        cells.append({"area": a, "area_name": names[a], "year": y, "n": len(g), "diff": m, "se": se, "p": p, "topics": G})
    grid = pd.DataFrame(cells)
    tested = grid.p.notna()
    grid.loc[tested, "p_holm"] = holm(grid.loc[tested, "p"]).to_numpy()
    return rows, grid


def plot(res: pd.DataFrame, grid: pd.DataFrame) -> None:
    plt = figures.plt
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3), constrained_layout=True)
    a2 = res[res.block == "A2"].assign(label=lambda x: x.label.str.replace("cls_", "").str.replace("fm", "FM paper"))
    b = res[(res.block == "B") & (res.label != "all papers")]
    for ax, g, title in [(axes[0], a2, "Among newcomer papers: acceptance vs\nnewcomer method papers (same topic-year)"),
                         (axes[1], b, "Newcomer minus incumbent acceptance\nwithin topic-year, by subgroup")]:
        y = np.arange(len(g))[::-1]
        ax.axvline(0, color=figures.INK2, lw=0.7)
        ax.hlines(y, g.ci95_lo * 100, g.ci95_hi * 100, color=figures.SERIES[0], lw=1.6)
        ax.scatter(g.coef * 100, y, s=22, color=figures.SERIES[0], edgecolor=figures.SURFACE, linewidth=1, zorder=3)
        ax.set_yticks(y, g.label)
        ax.set_title(title, loc="left")
        ax.set_xlabel("percentage points (95% CI)")
    axes[1].axvline(res[(res.block == "B") & (res.label == "all papers")].coef.iloc[0] * 100, color=figures.MUTED,
                    lw=0.8, ls=(0, (3, 2)))
    figures.save(fig, "PH1_newcomer_what")

    piv = grid.pivot(index="area_name", columns="year", values="diff") * 100
    star = grid.pivot(index="area_name", columns="year", values="p_holm")
    order = grid.groupby("area_name").n.sum().sort_values(ascending=False).index
    piv, star = piv.loc[order], star.loc[order]
    fig, ax = plt.subplots(figsize=(7.4, 6.2), constrained_layout=True)
    lim = np.nanmax(np.abs(piv.to_numpy()))
    im = ax.imshow(np.ma.masked_invalid(piv.to_numpy()), cmap=figures.DIVERGING, vmin=-lim, vmax=lim, aspect="auto")
    ax.set_facecolor(figures.GRID)
    ax.grid(False)
    fig.colorbar(im, ax=ax, shrink=0.5, label="pp vs the year's overall acceptance")
    for i in range(piv.shape[0]):
        for j in range(piv.shape[1]):
            v = piv.iat[i, j]
            ax.text(j, i, "–" if np.isnan(v) else f"{v:+.1f}{'*' if star.iat[i, j] < 0.05 else ''}", ha="center",
                    va="center", fontsize=6.5, color=figures.INK2 if np.isnan(v) else figures.INK)
    ax.set_xticks(range(piv.shape[1]), piv.columns)
    ax.set_yticks(range(piv.shape[0]), piv.index, fontsize=7)
    ax.set_title("Newcomer papers' acceptance minus the year's overall acceptance (pp), by area and year\n"
                 f"post hoc, exploratory; grey: fewer than {MIN_CELL} newcomer papers; * Holm p < 0.05 across tested cells",
                 loc="left")
    for s in ax.spines.values():
        s.set_visible(False)
    figures.save(fig, "PH1_newcomer_areas")


def fe_vcov(y: pd.Series, X: pd.DataFrame, absorb: pd.Series, cluster: pd.Series):
    """fe_ols with the full CR1 covariance (same estimator as ols.fe_ols): (beta, vcov, G)."""
    keep = (y.notna() & X.notna().all(axis=1)).to_numpy()
    yd = demean(y.to_numpy(float)[keep], absorb.to_numpy()[keep])
    Xd = demean(X.to_numpy(float)[keep], absorb.to_numpy()[keep])
    xtx_inv = np.linalg.pinv(Xd.T @ Xd)
    beta = xtx_inv @ Xd.T @ yd
    resid = yd - Xd @ beta
    _, cinv = np.unique(cluster.to_numpy()[keep], return_inverse=True)
    G, n, k = cinv.max() + 1, len(yd), Xd.shape[1]
    scores = np.zeros((G, k))
    np.add.at(scores, cinv, Xd * resid[:, None])
    vcov = (G / (G - 1)) * ((n - 1) / (n - k)) * xtx_inv @ (scores.T @ scores) @ xtx_inv
    return pd.Series(beta, X.columns), pd.DataFrame(vcov, X.columns, X.columns), int(G)


def wald(beta: pd.Series, vcov: pd.DataFrame, cols: list[str], G: int) -> tuple[float, float, int]:
    """Joint test that the coefficients in cols are all zero: (F, p, q), F(q, G - 1)."""
    b, V = beta[cols].to_numpy(), vcov.loc[cols, cols].to_numpy()
    q = len(cols)
    F = float(b @ np.linalg.pinv(V) @ b / q)
    return F, float(stats.f.sf(F, q, G - 1)), q


def ph2_group(d: pd.DataFrame, block: str, label: str, controls) -> list[dict]:
    e = estimate(d, "accepted", "log2_team", tuple(controls), "cell", (2018, 2026))
    out = [row(block, label, e["coef"], e["se"], e["p"], e["n"], e["dof"], term="slope per doubling",
               rate_1_2=float(d[d.band == "1-2"].accepted.mean()), rate_7plus=float(d[d.band == "7+"].accepted.mean()),
               papers_1_2=int((d.band == "1-2").sum()), papers_7plus=int((d.band == "7+").sum()))]
    bands = [f"band_{b}" for b in BANDS if b != "3-4"]
    X = d[bands + list(controls)].astype(float)
    X = X.loc[:, X.groupby(d.cell.to_numpy()).transform(lambda c: c - c.mean()).std() > 1e-12]
    r = fe_ols(d.accepted.astype(float), X, d.cell, d.topic)
    for b in bands:
        if b in r.index:
            out.append(row(block, label, r.loc[b, "coef"], r.loc[b, "se"], r.loc[b, "p"], int(r.loc[b, "n"]),
                           r.loc[b, "clusters"] - 1, term=f"{b[5:]} vs 3-4"))
    return out


def ph2_heterogeneity(d: pd.DataFrame, group: str, levels: list[str], controls) -> dict:
    X = d[["log2_team"] + list(controls)].astype(float)
    inter = []
    for g in levels[1:]:
        c = f"log2_team_x_{g}"
        X[c] = d.log2_team * (d[group] == g)
        inter.append(c)
    beta, vcov, G = fe_vcov(d.accepted.astype(float), X, d.cell, d.topic)
    F, p, q = wald(beta, vcov, inter, G)
    return {"set": group, "groups": len(levels), "F": F, "df1": q, "df2": G - 1, "p": p}


HET_DRAWS, HET_SEED = 200, 20261016


def het_null_p(d: pd.DataFrame, sets: list[tuple], observed: list[dict]) -> None:
    """Calibrated p for each heterogeneity F (see the module docstring); adds 'p_calibrated' to observed in place."""
    import dryrun
    rng = np.random.default_rng(HET_SEED)
    null = {name: [] for name, *_ in sets}
    for i in range(HET_DRAWS):
        dd = d.assign(accepted=simulate(d, dryrun.RQ3_DGP["lo" if i % 2 == 0 else "hi"], rng))
        for name, group, levels, ctr in sets:
            null[name].append(ph2_heterogeneity(dd, group, levels, ctr)["F"])
    for (name, *_), obs in zip(sets, observed):
        f = np.array(null[name])
        obs["p_naive_invalid"] = obs.pop("p")
        obs["p_calibrated"] = float((1 + (f >= obs["F"]).sum()) / (1 + len(f)))
        obs["null_F_median"], obs["null_F_95pct"] = float(np.median(f)), float(np.quantile(f, 0.95))


def ph2(k: pd.DataFrame) -> None:
    d = add_columns(k[k.rq3 & k.year.between(2018, 2026) & (k.team_size >= 1)].copy())
    base = CLASS_CONTROLS + ["fm"]
    rows = ph2_group(d, "A", "all papers", base)
    keyed = d[d.has_author_key & d.year.between(*YEARS)]
    e = estimate(keyed, "accepted", "log2_team", tuple(base) + ("newcomer",), "cell", YEARS)
    rows.append(row("A", "papers with an author ID, newcomer control", e["coef"], e["se"], e["p"], e["n"], e["dof"],
                    term="slope per doubling"))
    for c in CLASSES:
        rows += ph2_group(d[d.primary_class == c], "B-class", c, ["fm"])
    names = d.drop_duplicates("area").set_index("area").area_name
    areas = sorted(d.area.dropna().unique())
    for a in areas:
        rows += ph2_group(d[d.area == a], "B-area", f"{a} {names[a]}", base)
    res = pd.DataFrame(rows)
    for blk in ["B-class", "B-area"]:
        m = (res.block == blk) & (res.term == "slope per doubling")
        res.loc[m, "p_holm_slopes"] = holm(res.loc[m, "p"].fillna(1.0)).to_numpy()
    d["cls"] = d.primary_class
    sets = [("classes", "cls", CLASSES, base), ("areas", "area", areas, base)]
    het = [ph2_heterogeneity(d, g, lv, c) for _, g, lv, c in sets]
    het_null_p(d, sets, het)
    res.to_csv(OUT / "ph2_estimates.csv", index=False)
    rates = (d.groupby(["primary_class", "band"]).accepted.agg(["mean", "size"]).rename(
        columns={"mean": "acceptance_rate", "size": "papers"}).reset_index())
    rates.to_csv(OUT / "ph2_rates_by_class_and_band.csv", index=False)
    summary = {"population_papers": int(len(d)), "team_size_median": float(d.team_size.median()),
               "papers_by_band": d.band.value_counts().to_dict(),
               "acceptance_by_band": d.groupby("band").accepted.mean().round(4).to_dict(), "heterogeneity": het,
               "note": "post hoc exploratory (PREREGISTRATION.md, 2026-10-16); associations, not causal effects"}
    (OUT / "ph2_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    plot_ph2(res)
    print(json.dumps(summary, indent=1))
    show = res.assign(**{c: (res[c] * 100).round(2) for c in ["coef", "ci95_lo", "ci95_hi"]})
    cols = ["block", "label", "term", "coef", "ci95_lo", "ci95_hi", "p", "p_holm_slopes", "n"]
    print(show[cols].to_string(index=False))


def plot_ph2(res: pd.DataFrame) -> None:
    plt = figures.plt
    slopes = res[res.term == "slope per doubling"]
    overall = slopes[(slopes.block == "A") & (slopes.label == "all papers")].coef.iloc[0] * 100
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.6), constrained_layout=True,
                             gridspec_kw={"width_ratios": [1, 1.5]})
    for ax, blk, title in [(axes[0], "B-class", "By contribution class"), (axes[1], "B-area", "By area")]:
        g = slopes[slopes.block == blk].sort_values("coef")
        y = np.arange(len(g))
        ax.axvline(0, color=figures.INK2, lw=0.7)
        ax.axvline(overall, color=figures.MUTED, lw=0.8, ls=(0, (3, 2)))
        ax.hlines(y, g.ci95_lo * 100, g.ci95_hi * 100, color=figures.SERIES[0], lw=1.6)
        ax.scatter(g.coef * 100, y, s=22, color=figures.SERIES[0], edgecolor=figures.SURFACE, linewidth=1, zorder=3)
        ax.set_yticks(y, [lab.split(" ", 1)[1] if blk == "B-area" else lab for lab in g.label], fontsize=6.8)
        ax.set_title(title, loc="left")
        ax.set_xlabel("pp per doubling of team size (95% CI)")
    fig.suptitle("Acceptance and team size within topic-year (post hoc, exploratory); dashed: all papers",
                 x=0.01, ha="left", fontsize=8.5)
    figures.save(fig, "PH2_team_size")


def twfe(y: np.ndarray, X: np.ndarray, fes: list[np.ndarray], w: np.ndarray, tol: float = 1e-10,
         max_iter: int = 10_000) -> tuple[np.ndarray, np.ndarray]:
    """Weighted demeaning of y and X by several fixed effects at once (alternating projections)."""
    Z = np.column_stack([y, X]).astype(float)
    codes = [pd.factorize(f)[0] for f in fes]
    wsum = [np.bincount(c, weights=w) for c in codes]
    for _ in range(max_iter):
        delta = 0.0
        for c, ws in zip(codes, wsum):
            means = np.vstack([np.bincount(c, weights=w * Z[:, j]) for j in range(Z.shape[1])]).T / ws[:, None]
            Z -= means[c]
            delta = max(delta, float(np.abs(means).max()))
        if delta < tol:
            break
    else:
        raise RuntimeError("alternating projections did not converge")
    return Z[:, 0], Z[:, 1:]


def drop_singletons(d: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    while True:
        keep = np.ones(len(d), bool)
        for c in cols:
            keep &= d.groupby(c)[c].transform("size").to_numpy() > 1
        if keep.all():
            return d
        d = d[keep]


def wls_fe(d: pd.DataFrame, y: str, xs: list[str], fes: list[str], w: str, cluster: str,
           cluster2: str | None = None) -> pd.DataFrame:
    """Weighted least squares with several absorbed fixed effects; CR1 SE by `cluster` (t with G - 1 df) and, if
    given, a two-way (cluster, cluster2) SE for the first regressor."""
    d = drop_singletons(d.dropna(subset=[y, *xs]), fes).reset_index(drop=True)
    wv = d[w].to_numpy(float)
    yd, Xd = twfe(d[y].to_numpy(float), d[xs].to_numpy(float), [d[f].to_numpy() for f in fes], wv)
    keep = Xd.std(axis=0) > 1e-12
    xs = [x for x, k in zip(xs, keep) if k]
    Xd = Xd[:, keep]
    XtWX_inv = np.linalg.pinv(Xd.T @ (Xd * wv[:, None]))
    beta = XtWX_inv @ (Xd * wv[:, None]).T @ yd
    e = yd - Xd @ beta
    n, k = Xd.shape

    def var(groups):
        cg = pd.factorize(groups)[0]
        G = cg.max() + 1
        S = np.zeros((G, k))
        np.add.at(S, cg, Xd * (wv * e)[:, None])
        return (G / (G - 1)) * ((n - 1) / (n - k)) * XtWX_inv @ (S.T @ S) @ XtWX_inv, G

    V, G = var(d[cluster].to_numpy())
    se = np.sqrt(np.diag(V))
    out = pd.DataFrame({"coef": beta, "se": se, "p": 2 * stats.t.sf(np.abs(beta / se), G - 1), "dof": G - 1,
                        "rows": n, "papers": d.submission_id.nunique(), "clusters": G}, index=xs)
    if cluster2:
        V2, G2 = var(d[cluster2].to_numpy())
        V12, _ = var(d[cluster].astype(str).to_numpy() + "|" + d[cluster2].astype(str).to_numpy())
        v = V[0, 0] + V2[0, 0] - V12[0, 0]
        out.loc[xs[0], "se_twoway"] = float(np.sqrt(v if v > 0 else max(V[0, 0], V2[0, 0])))
    return out


def author_rows(k: pd.DataFrame) -> pd.DataFrame:
    """One row per (paper, author ID) for PH1's population, with the author's novelty in the topic and experience.
    History counts every discovery submission with a topic (any outcome, D1), as for incumbency."""
    from variables import load_authors
    from common import DATA
    a = load_authors(k.submission_id)[["submission_id", "key"]]
    pos = pd.read_csv(DATA / "submission_authors.csv.gz", keep_default_na=False, na_values=[r"\N"],
                      usecols=["submission_id", "declared_id_key", "source_list_position"]).rename(
        columns={"declared_id_key": "key"}).dropna(subset=["key"])
    pos = pos.groupby(["submission_id", "key"]).source_list_position.min().reset_index()
    a = a.merge(pos, on=["submission_id", "key"], how="left")
    papers = k[["submission_id", "topic", "year"]]
    at = a.merge(papers, on="submission_id")
    by_topic = at.groupby(["key", "topic", "year"]).size().rename("n").reset_index().sort_values(["key", "topic", "year"])
    by_topic["prior_in_topic"] = by_topic.groupby(["key", "topic"]).n.cumsum() - by_topic.n
    by_all = at.groupby(["key", "year"]).size().rename("n").reset_index().sort_values(["key", "year"])
    by_all["prior_any"] = by_all.groupby("key").n.cumsum() - by_all.n
    at = at.merge(by_topic[["key", "topic", "year", "prior_in_topic"]], on=["key", "topic", "year"])
    at = at.merge(by_all[["key", "year", "prior_any"]], on=["key", "year"])
    at["author_new"] = (at.prior_in_topic == 0).astype(float)
    at["log_exp"] = np.log1p(at.prior_any)
    last = at.groupby("submission_id").source_list_position.transform("max")
    at["first"] = at.source_list_position == at.groupby("submission_id").source_list_position.transform("min")
    at["last"] = at.source_list_position == last
    return at[["submission_id", "key", "author_new", "log_exp", "first", "last"]]


def ph3(k: pd.DataFrame) -> None:
    d = population(k)
    rows_a = author_rows(k)
    at = rows_a.merge(d, on="submission_id")
    at["w"] = 1.0 / at.groupby("submission_id").key.transform("size")
    ctr = CLASS_CONTROLS + ["fm", "log2_team", "log_exp"]
    res = []

    def add(model, label, r, x):
        res.append({"model": model, "label": label, "term": x, **r.loc[x].to_dict()})

    def pair(model, sample, x, who):
        """The author-FE model and, on exactly its sample, the same model without author FE."""
        same = drop_singletons(sample.dropna(subset=["accepted", x, *ctr]), ["cell", "key"])
        add(model, f"{x} | topic x year + {who}", wls_fe(same, "accepted", [x] + ctr, ["cell", "key"], "w", "topic", "key"), x)
        add(model + "-base", f"{x} | topic x year, same sample, no {who} FE", wls_fe(same, "accepted", [x] + ctr, ["cell"], "w", "topic", "key"), x)

    add("M0", "newcomer | topic x year, all author rows (no author FE)", wls_fe(at, "accepted", ["newcomer"] + ctr, ["cell"], "w", "topic", "key"), "newcomer")
    pair("M1", at, "newcomer", "author")
    pair("M2", at, "author_new", "author")
    for m, pos in [("M3", "first"), ("M4", "last")]:
        pair(m, at[at[pos]].drop_duplicates("submission_id").assign(w=1.0), "newcomer", f"{pos} author")
    res = pd.DataFrame(res)
    q = stats.t.ppf(0.975, res.dof)
    res["ci95_lo"], res["ci95_hi"] = res.coef - q * res.se, res.coef + q * res.se
    ident = at.groupby("key").newcomer.agg(["min", "max"])
    summary = {"papers": int(d.submission_id.nunique()), "author_rows": int(len(at)), "authors": int(at.key.nunique()),
               "authors_with_both_newcomer_and_incumbent_papers": int(((ident["min"] == 0) & (ident["max"] == 1)).sum()),
               "note": "post hoc exploratory (PREREGISTRATION.md, 2026-10-16); associations, not causal effects"}
    res.to_csv(OUT / "ph3_estimates.csv", index=False)
    (OUT / "ph3_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    plot_ph3(res)
    print(json.dumps(summary, indent=1))
    show = res.assign(**{c: (res[c] * 100).round(2) for c in ["coef", "ci95_lo", "ci95_hi", "se", "se_twoway"]})
    print(show[["model", "label", "coef", "ci95_lo", "ci95_hi", "se", "se_twoway", "p", "rows", "papers"]].to_string(index=False))


def plot_ph3(res: pd.DataFrame) -> None:
    plt = figures.plt
    names = {"M1": "newcomer paper, all authors", "M2": "author new to the topic", "M3": "newcomer paper, first author",
             "M4": "newcomer paper, last author"}
    fig, ax = plt.subplots(figsize=(6.6, 2.6), constrained_layout=True)
    ax.axvline(0, color=figures.INK2, lw=0.7)
    for i, (m, name) in enumerate(names.items()):
        y = len(names) - 1 - i
        for suffix, dy, colour, lab in [("-base", 0.15, figures.MUTED, "same sample, no author FE"),
                                        ("", -0.15, figures.SERIES[0], "with author FE")]:
            r = res[res.model == m + suffix].iloc[0]
            ax.hlines(y + dy, r.ci95_lo * 100, r.ci95_hi * 100, color=colour, lw=1.6)
            ax.scatter(r.coef * 100, y + dy, s=22, color=colour, edgecolor=figures.SURFACE, linewidth=1, zorder=3,
                       label=lab if i == 0 else None)
    ax.set_yticks(range(len(names))[::-1], list(names.values()), fontsize=7)
    ax.set_xlabel("acceptance difference within topic-year, pp (95% CI)")
    ax.set_title("Within the same authors the newcomer gap shrinks by a third to a half (post hoc, exploratory)",
                 loc="left")
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=6.5)
    figures.save(fig, "PH3_author_fe")


PH4_YEARS, PH4_RECENT, PH4_CENTRE = (2018, 2026), (2024, 2026), 2022
PH4_TYPES = ("research_area", "specific_topic", "property", "application_domain")
PH4_MIN_PAPERS, PH4_MIN_CELL, PH4_MIN_YEARS, PH4_PERMS, PH4_SEED = 200, 10, 4, 200, 20261017
FL_KEYWORD, FL_TOPIC = "federated learning", "m029"


def bh(p: pd.Series) -> pd.Series:
    """Benjamini-Hochberg adjusted p-values (q); NaN stays NaN."""
    ok = p.dropna()
    out = pd.Series(np.nan, index=p.index, dtype=float)
    if ok.empty:
        return out
    order = np.argsort(ok.to_numpy(), kind="stable")
    ps = ok.to_numpy()[order]
    m = len(ps)
    q = np.minimum.accumulate((ps * m / np.arange(1, m + 1))[::-1])[::-1].clip(max=1.0)
    adj = np.empty(m)
    adj[order] = q
    out.loc[ok.index] = adj
    return out


def cell_counts(member: np.ndarray, year_idx: np.ndarray, acc: np.ndarray, n_years: int):
    """Papers and acceptances per unit and year (units x years), and per year over all papers."""
    Y = np.zeros((len(year_idx), n_years))
    Y[np.arange(len(year_idx)), year_idx] = 1.0
    M = member.astype(float)
    Ya = Y * acc[:, None]
    return M.T @ Y, M.T @ Ya, Y.sum(axis=0), Ya.sum(axis=0)


def gap_summary(n1: np.ndarray, k1: np.ndarray, n0: np.ndarray, k0: np.ndarray, years: np.ndarray) -> dict:
    """Level, recent level and trend of the gap (unit minus all other papers of the same year) for one unit."""
    ok = (n1 > 0) & (n0 > 0)
    s1, s0 = (k1 + 0.5) / (n1 + 1), (k0 + 0.5) / (n0 + 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(ok, k1 / n1 - k0 / n0, np.nan)
        var = np.where(ok, s1 * (1 - s1) / n1 + s0 * (1 - s0) / n0, np.nan)
    return summarise_gaps(g, var, np.where(ok, n1, 0), years)


def summarise_gaps(g: np.ndarray, var: np.ndarray, n1: np.ndarray, years: np.ndarray) -> dict:
    """Level, recent level and trend from per-year gaps g with variances var; n1 = the unit's papers per year
    (0 where the year has no gap)."""
    ok = np.isfinite(g) & (n1 > 0)
    big = ok & (n1 >= PH4_MIN_CELL)
    m = int(big.sum())
    res = {"papers": int(n1.sum()), "years_with_min_cell": m}

    def level(mask):
        w = np.where(mask, n1, 0.0)
        if w.sum() == 0:
            return np.nan, np.nan
        w = w / w.sum()
        return float(np.nansum(w * np.where(mask, g, 0))), float(np.nansum(w ** 2 * np.where(mask, var, 0)))

    lev, v = level(ok)
    phi = float(np.sum((g[big] - lev) ** 2 / var[big]) / (m - 1)) if m >= 2 else np.nan
    infl = max(1.0, phi) if np.isfinite(phi) else 1.0
    dof = max(m - 1, 1)
    q = stats.t.ppf(0.975, dof)
    res["phi"] = phi
    for name, mask in [("level", ok), ("recent", ok & (years >= PH4_RECENT[0]) & (years <= PH4_RECENT[1]))]:
        est, vv = level(mask)
        se = float(np.sqrt(vv * infl)) if np.isfinite(vv) else np.nan
        res.update({name: est, f"{name}_se": se, f"{name}_p": float(2 * stats.t.sf(abs(est / se), dof)) if se > 0 else np.nan,
                    f"{name}_ci_lo": est - q * se, f"{name}_ci_hi": est + q * se, f"{name}_papers": int(n1[mask].sum())})
    res.update({"trend": np.nan, "trend_se": np.nan, "trend_p": np.nan, "trend_ci_lo": np.nan, "trend_ci_hi": np.nan})
    if m >= PH4_MIN_YEARS:
        x = years[big] - PH4_CENTRE
        X = np.column_stack([np.ones(m), x])
        W = 1.0 / var[big]
        xtwx = X.T @ (X * W[:, None])
        beta = np.linalg.solve(xtwx, X.T @ (W * g[big]))
        rss = float(np.sum(W * (g[big] - X @ beta) ** 2))
        cov = np.linalg.inv(xtwx) * max(1.0, rss / (m - 2))
        se = float(np.sqrt(cov[1, 1]))
        qt = stats.t.ppf(0.975, m - 2)
        res.update({"trend": float(beta[1]), "trend_se": se, "trend_p": float(2 * stats.t.sf(abs(beta[1] / se), m - 2)),
                    "trend_ci_lo": float(beta[1] - qt * se), "trend_ci_hi": float(beta[1] + qt * se)})
    return res


def ph4_members(d: pd.DataFrame) -> dict[str, tuple[list[str], np.ndarray]]:
    """Membership (papers x units) for K (author keywords) and T (k100 topics), aligned with d. Reads no outcome."""
    kt = pd.read_csv(TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = kt[kt.type.isin(PH4_TYPES) & (kt.papers >= PH4_MIN_PAPERS)].sort_values("papers", ascending=False).keyword
    corpus = topic_layer().embedded_corpus().set_index("submission_id")
    lists = [set(x) for x in corpus.keywords.reindex(d.submission_id.to_numpy())]
    K = np.array([[kw in s for kw in vocab] for s in lists], dtype=bool)
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    names = cat[cat.level == "mid"].set_index("topic").name
    topics = sorted(d.topic.unique())
    T = d.topic.to_numpy()[:, None] == np.array(topics)[None, :]
    return {"K": (list(vocab), K), "T": ([f"{t} {names.get(t, '')}" for t in topics], T)}


def ph4_set(d: pd.DataFrame, names: list[str], member: np.ndarray, rng: np.random.Generator):
    years = np.arange(PH4_YEARS[0], PH4_YEARS[1] + 1)
    yi = d.year.to_numpy() - PH4_YEARS[0]
    acc = d.accepted.to_numpy(float)
    n_in, k_in, n_all, k_all = cell_counts(member, yi, acc, len(years))
    res = pd.DataFrame([gap_summary(n_in[u], k_in[u], n_all - n_in[u], k_all - k_in[u], years) for u in range(len(names))])
    res.insert(0, "unit", names)
    for est in ("level", "recent", "trend"):
        res[f"{est}_q"] = bh(res[f"{est}_p"])
        ok = res[f"{est}_p"].notna()
        res.loc[ok, f"{est}_p_holm"] = holm(res.loc[ok, f"{est}_p"]).to_numpy()
    X0 = d[CLASS_CONTROLS + ["fm", "log2_team"]].astype(float).reset_index(drop=True)
    for u in range(len(names)):
        X = pd.concat([pd.Series(member[:, u].astype(float), name="member"), X0], axis=1)
        r = fe_ols(d.accepted.astype(float).reset_index(drop=True), X, d.year.reset_index(drop=True),
                   d.submission_id.reset_index(drop=True))
        res.loc[u, ["adjusted_level", "adjusted_level_se", "adjusted_level_p"]] = r.loc["member", ["coef", "se", "p"]].to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        rate_in = np.where(n_in > 0, k_in / n_in, np.nan)
        rate_out = (k_all - k_in) / (n_all - n_in)
    cells = pd.DataFrame({"unit": np.repeat(names, len(years)), "year": np.tile(years, len(names)),
                          "papers": n_in.ravel().astype(int), "rate": rate_in.ravel(), "rate_others": rate_out.ravel()})
    cells["gap"] = cells.rate - cells.rate_others
    s1 = (k_in + 0.5) / (n_in + 1)
    s0 = (k_all - k_in + 0.5) / (n_all - n_in + 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        cells["gap_se"] = np.sqrt(np.where(n_in > 0, s1 * (1 - s1) / n_in, np.nan) + s0 * (1 - s0) / (n_all - n_in)).ravel()
    # calibration: within-year permutations of acceptance on the same units
    groups = [np.flatnonzero(yi == j) for j in range(len(years))]
    rej = {e: [] for e in ("level", "recent", "trend")}
    anyflag = {e: [] for e in ("level", "recent", "trend")}
    for _ in range(PH4_PERMS):
        a = acc.copy()
        for idx in groups:
            a[idx] = acc[rng.permutation(idx)]
        _, kp, _, ka = cell_counts(member, yi, a, len(years))
        sim = pd.DataFrame([gap_summary(n_in[u], kp[u], n_all - n_in[u], ka - kp[u], years) for u in range(len(names))])
        for e in rej:
            ps = sim[f"{e}_p"].dropna()
            rej[e].append(float((ps < 0.05).mean()) if len(ps) else np.nan)
            anyflag[e].append(bool((bh(sim[f"{e}_p"]) < 0.05).any()))
    calib = {e: {"per_test_rejection_at_05": round(float(np.nanmean(rej[e])), 4),
                 "share_of_permutations_with_any_bh_flag": round(float(np.mean(anyflag[e])), 4)} for e in rej}
    return res, cells, calib


def ph4_compute(k: pd.DataFrame) -> dict:
    k = k.reset_index(drop=True)
    d = add_columns(k[k.rq3 & k.year.between(*PH4_YEARS)].copy())
    d = d.assign(orig_index=d.index).reset_index(drop=True)
    rng = np.random.default_rng(PH4_SEED)
    out = {"papers": int(len(d))}
    members = ph4_members(d)
    for set_name, (names, member) in members.items():
        out[set_name] = ph4_set(d, names, member, rng)
    names, member = members["K"]
    out["mechanisms"] = ph4_mechanisms(k, d, member, names, out["K"][0])
    return out


def ph4(k: pd.DataFrame) -> None:
    out = ph4_compute(k)
    summary = {"population_papers": out["papers"], "years": list(PH4_YEARS), "recent": list(PH4_RECENT),
               "note": "post hoc exploratory (PREREGISTRATION.md, 2026-10-17); associations, not causal effects"}
    for set_name, label in [("K", "keywords"), ("T", "topics")]:
        res, cells, calib = out[set_name]
        res.to_csv(OUT / f"ph4_{label}.csv", index=False)
        cells.to_csv(OUT / f"ph4_{label}_cells.csv", index=False)
        flagged = {e: res[res[f"{e}_q"] < 0.05].sort_values(e)[["unit", e, f"{e}_q"]].round(4).to_dict("records")
                   for e in ("level", "recent", "trend")}
        summary[label] = {"units": int(len(res)), "units_with_trend": int(res.trend.notna().sum()),
                          "flagged_counts": {e: len(v) for e, v in flagged.items()}, "flagged": flagged,
                          "calibration_within_year_permutations": calib}
    kw, tp = out["K"][0], out["T"][0]
    cols = ["unit", "papers", "level", "level_q", "recent", "recent_q", "trend", "trend_q", "adjusted_level"]
    summary["federated_learning"] = {"keyword": kw[kw.unit == FL_KEYWORD][cols].round(4).to_dict("records"),
                                     "topic": tp[tp.unit.str.startswith(FL_TOPIC + " ")][cols].round(4).to_dict("records")}
    mech, comp = out["mechanisms"]
    mech.to_csv(OUT / "ph4_mechanisms.csv", index=False)
    comp.to_csv(OUT / "ph4_mechanism_composition.csv", index=False)
    summary["mechanisms"] = mech[["unit", "trend", "adjusted_trend", "share_of_trend_kept_after_adjustment",
                                  "established_trend", "not_established_trend", "keyword_incumbent_trend",
                                  "keyword_newcomer_trend", "peak_share_year", "reading"]].round(4).to_dict("records")
    (OUT / "ph4_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    plot_ph4()
    plot_ph4_mechanisms()
    pd.set_option("display.width", 220)
    print(json.dumps({k_: v for k_, v in summary.items() if k_ != "keywords" and k_ != "topics"}, indent=1))
    for label in ("keywords", "topics"):
        print(label, json.dumps({k_: summary[label][k_] for k_ in ("units", "units_with_trend", "flagged_counts",
                                                                     "calibration_within_year_permutations")}))
    show = kw.assign(**{c: (kw[c] * 100).round(1) for c in ["level", "recent", "trend", "adjusted_level"]})
    print(show[cols].sort_values("trend").to_string(index=False))


def ph4_selected(res: pd.DataFrame) -> list[str]:
    """Trend panels: up to four flagged most negative and four most positive trends, plus federated learning."""
    f = res[res.trend_q < 0.05].sort_values("trend")
    picks = list(f[f.trend < 0].unit.head(4)) + list(f[f.trend > 0].unit.tail(4)[::-1])
    return picks + ([FL_KEYWORD] if FL_KEYWORD not in picks and FL_KEYWORD in set(res.unit) else [])


def plot_ph4() -> None:
    """Keyword map (level vs trend), trend panels and topic map, from the saved estimates (reads no outcome)."""
    plt = figures.plt
    red, blue = "#c23b3b", "#1c5cab"
    for label, title in [("keywords", "author keywords"), ("topics", "k100 topics")]:
        res = pd.read_csv(OUT / f"ph4_{label}.csv")
        r = res[res.trend.notna()]
        fig, ax = plt.subplots(figsize=(7.0, 4.6), constrained_layout=True)
        ax.axhline(0, color=figures.INK2, lw=0.7)
        ax.axvline(0, color=figures.INK2, lw=0.7)
        col = np.where(r.trend_q < 0.05, np.where(r.trend < 0, red, blue), figures.MUTED)
        ax.scatter(r.level * 100, r.trend * 100, s=12 + 60 * np.sqrt(r.papers / r.papers.max()), c=col, alpha=0.85,
                   edgecolor=figures.SURFACE, linewidth=0.6, zorder=3)
        lab = r[(r.trend_q < 0.05) | (r.level_q < 0.05) | (r.unit == FL_KEYWORD) | r.unit.str.startswith(FL_TOPIC + " ")]
        for _, x in lab.iterrows():
            name = x.unit if label == "keywords" else x.unit.split(" ", 1)[1][:28]
            ax.annotate(name, (x.level * 100, x.trend * 100), xytext=(3, 3), textcoords="offset points", fontsize=6,
                        color=figures.INK)
        ax.set_xlabel("level: acceptance gap vs other papers of the same year, 2018-2026 (pp)")
        ax.set_ylabel("trend of the gap (pp per year)")
        ax.set_title(f"PH4 ({title}): level and trend of the acceptance gap; red/blue: trend BH q < 0.05 "
                     "(post hoc, exploratory)", loc="left")
        figures.save(fig, f"PH4_{label}_map")

    res = pd.read_csv(OUT / "ph4_keywords.csv")
    cells = pd.read_csv(OUT / "ph4_keywords_cells.csv")
    picks = ph4_selected(res)
    n = len(picks)
    cols = min(4, n)
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(1.9 * cols, 1.7 * rows), sharex=True, sharey=True,
                             constrained_layout=True, squeeze=False)
    for ax, kw in zip(axes.flat, picks):
        c = cells[(cells.unit == kw) & (cells.papers >= PH4_MIN_CELL)]
        x = res[res.unit == kw].iloc[0]
        colour = red if x.trend < 0 else blue
        ax.axhline(0, color=figures.INK2, lw=0.6)
        ax.errorbar(c.year, c.gap * 100, yerr=1.96 * c.gap_se * 100, fmt="o", ms=3, color=colour, lw=0.9)
        yrs = np.array([c.year.min(), c.year.max()])
        # fitted trend line through the weighted mean of the gaps
        w = 1 / c.gap_se ** 2
        xm, gm = np.average(c.year, weights=w), np.average(c.gap, weights=w)
        ax.plot(yrs, (gm + x.trend * (yrs - xm)) * 100, color=colour, lw=1.2)
        ax.set_title(f"{kw}\n{x.trend * 100:+.1f} pp/yr, q={x.trend_q:.3f}", fontsize=6.5, loc="left")
    for ax in axes.flat[n:]:
        ax.set_visible(False)
    fig.suptitle("PH4: acceptance gap by year (95% CI), selected keywords (post hoc, exploratory)", fontsize=7.5)
    figures.save(fig, "PH4_keyword_trends")


def established_authors(k: pd.DataFrame) -> np.ndarray:
    """Per paper of k: some author ID had an accepted ICLR paper in an earlier year (any topic). Uses earlier outcomes."""
    from variables import load_authors
    a = load_authors(k.submission_id)[["submission_id", "key"]].merge(k[["submission_id", "year", "accepted"]],
                                                                      on="submission_id")
    first = a[a.accepted == 1].groupby("key").year.min()
    a["est"] = a.key.map(first) < a.year
    return a.groupby("submission_id").est.any().reindex(k.submission_id).fillna(False).to_numpy(bool)


def keyword_incumbent(kw: str, d: pd.DataFrame, corpus: pd.DataFrame, authors: pd.DataFrame) -> np.ndarray:
    """Per paper of d: 1 if some author ID has an earlier discovery submission (any outcome) listing kw, 0 if not,
    NaN without an author ID. Outcome-free."""
    users = corpus[[kw in set(x) for x in corpus.keywords]][["submission_id", "year"]]
    first = authors.merge(users, on="submission_id").groupby("key").year.min()
    a = authors[authors.submission_id.isin(set(d.submission_id))].merge(d[["submission_id", "year"]], on="submission_id")
    a["inc"] = a.key.map(first) < a.year
    inc = a.groupby("submission_id").inc.any().astype(float)
    return inc.reindex(d.submission_id).to_numpy()


def residual_gaps(r: np.ndarray, member: np.ndarray, year_idx: np.ndarray, years: np.ndarray) -> dict:
    """summarise_gaps on a continuous outcome r (adjusted acceptance): mean in the unit minus mean outside, per year."""
    g, var, n1 = np.full(len(years), np.nan), np.full(len(years), np.nan), np.zeros(len(years))
    for j in range(len(years)):
        a, b = r[(year_idx == j) & member], r[(year_idx == j) & ~member]
        if len(a) == 0 or len(b) < 2:
            continue
        va = a.var(ddof=1) if len(a) > 1 else 0.25
        g[j], var[j], n1[j] = a.mean() - b.mean(), va / len(a) + b.var(ddof=1) / len(b), len(a)
    return summarise_gaps(g, var, n1, years)


def ph4_mechanisms(k: pd.DataFrame, d: pd.DataFrame, member: np.ndarray, names: list[str], res: pd.DataFrame):
    """PH4b: adjusted trend, subgroup trends and composition for the selected keywords."""
    from variables import load_authors
    years = np.arange(PH4_YEARS[0], PH4_YEARS[1] + 1)
    yi = d.year.to_numpy() - PH4_YEARS[0]
    acc = d.accepted.to_numpy(float)
    d = d.assign(established=established_authors(k)[d.orig_index.to_numpy()].astype(float))
    ctr = CLASS_CONTROLS + ["fm", "log2_team", "established", "has_key"]
    d["has_key"] = d.has_author_key.astype(float)
    ctr = [c for c in ctr if d[c].nunique() > 1]                 # all decided papers have an author ID: drop has_key
    X = d[ctr].astype(float)
    fit = fe_ols(d.accepted.astype(float), X, d.year, d.submission_id)
    resid = acc - X.to_numpy() @ fit.loc[ctr, "coef"].to_numpy()
    corpus = topic_layer().embedded_corpus()[["submission_id", "year", "keywords"]]
    authors = load_authors(corpus.submission_id)[["submission_id", "key"]]
    share = {}
    totals = corpus.groupby("year").size()
    rows, comp = [], []
    for kw in ph4_selected(res):
        u = names.index(kw)
        m = member[:, u]
        raw = res.iloc[u]
        adj = residual_gaps(resid, m, yi, years)
        inc = keyword_incumbent(kw, d, corpus, authors)
        users = corpus[[kw in set(x) for x in corpus.keywords]].groupby("year").size()
        share = (users / totals).reindex(years).fillna(0)
        out = {"unit": kw, "papers": int(m.sum()), "trend": raw.trend, "trend_se": raw.trend_se, "trend_q": raw.trend_q,
               "adjusted_trend": adj["trend"], "adjusted_trend_se": adj["trend_se"], "adjusted_trend_p": adj["trend_p"],
               "peak_share_year": int(share.idxmax()), "peak_share": float(share.max())}
        out["share_of_trend_kept_after_adjustment"] = adj["trend"] / raw.trend if raw.trend else np.nan
        for gname, sub in [("established", d.established.to_numpy() == 1), ("not_established", d.established.to_numpy() == 0),
                           ("keyword_incumbent", inc == 1), ("keyword_newcomer", inc == 0)]:
            n_in, k_in, n_all, k_all = cell_counts((m & sub)[:, None], yi, acc, len(years))
            n_out, k_out, _, _ = cell_counts((~m)[:, None], yi, acc, len(years))
            st = gap_summary(n_in[0], k_in[0], n_out[0], k_out[0], years)
            out.update({f"{gname}_trend": st["trend"], f"{gname}_trend_se": st["trend_se"],
                        f"{gname}_trend_p": st["trend_p"], f"{gname}_papers": st["papers"]})
        sign = np.sign(raw.trend)
        kept = out["share_of_trend_kept_after_adjustment"] >= 0.5
        exp_sig = any(np.sign(out[f"{g_}_trend"]) == sign and out[f"{g_}_trend_p"] < 0.05
                      for g_ in ("established", "keyword_incumbent") if np.isfinite(out[f"{g_}_trend"]))
        new_sig = any(np.sign(out[f"{g_}_trend"]) == sign and out[f"{g_}_trend_p"] < 0.05
                      for g_ in ("not_established", "keyword_newcomer") if np.isfinite(out[f"{g_}_trend"]))
        out["reading"] = ("judged differently" if kept and exp_sig else
                          "composition" if (not kept) and (not exp_sig) and new_sig else "mixed")
        rows.append(out)
        for j, y in enumerate(years):
            sel = m & (yi == j)
            if not sel.any():
                continue
            ds = d[sel]
            comp.append({"unit": kw, "year": int(y), "papers": int(sel.sum()), "share_of_all_submissions": float(share[y]),
                         "established_share": float(ds.established.mean()),
                         "keyword_newcomer_share": float(np.nanmean(1 - inc[sel])) if np.isfinite(inc[sel]).any() else np.nan,
                         "mean_team_size": float(ds.team_size.mean()), "method_share": float(ds.method.mean()),
                         "fm_share": float(ds.fm.mean()), "rate": float(acc[sel].mean())})
    return pd.DataFrame(rows), pd.DataFrame(comp)


def plot_ph4_mechanisms() -> None:
    plt = figures.plt
    mech = pd.read_csv(OUT / "ph4_mechanisms.csv")
    parts = [("trend", "raw"), ("adjusted_trend", "adjusted for composition"), ("established_trend", "established authors"),
             ("not_established_trend", "no established author"), ("keyword_incumbent_trend", "keyword incumbents"),
             ("keyword_newcomer_trend", "keyword newcomers")]
    n = len(mech)
    fig, axes = plt.subplots(1, n, figsize=(1.9 * n, 2.6), sharey=True, constrained_layout=True, squeeze=False)
    for ax, (_, r) in zip(axes[0], mech.iterrows()):
        y = np.arange(len(parts))[::-1]
        for yy, (c, _) in zip(y, parts):
            est, se = r[c], r[c + "_se"]
            ax.errorbar(est * 100, yy, xerr=1.96 * se * 100, fmt="o", ms=3, color=figures.SERIES[0], lw=1)
        ax.axvline(0, color=figures.INK2, lw=0.6)
        ax.set_title(f"{r.unit}\n({r.reading})", fontsize=6.5, loc="left")
        ax.set_xlabel("pp per year", fontsize=6.5)
    axes[0, 0].set_yticks(np.arange(len(parts))[::-1], [lab for _, lab in parts], fontsize=6.5)
    fig.suptitle("PH4b: trend of the acceptance gap, raw, adjusted and by author group (95% CI; post hoc)", fontsize=7.5)
    figures.save(fig, "PH4_mechanisms")


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which in ("plot2", "plot3", "plot4"):               # redraw from the saved estimates; reads no outcome
        if which == "plot4":
            plot_ph4()
            plot_ph4_mechanisms()
        else:
            plot_ph2(pd.read_csv(OUT / "ph2_estimates.csv")) if which == "plot2" else plot_ph3(pd.read_csv(OUT / "ph3_estimates.csv"))
        return
    if which not in ("ph1", "ph2", "ph3", "ph4"):
        raise SystemExit("usage: posthoc.py ph1|ph2|ph3|ph4|plot2|plot3|plot4")
    OUT.mkdir(parents=True, exist_ok=True)
    if which == "ph2":
        ph2(with_outcomes())
        return
    if which == "ph3":
        ph3(with_outcomes())
        return
    if which == "ph4":
        ph4(with_outcomes())
        return
    d = population()
    rows_c, grid = block_c(d)
    res = pd.DataFrame(block_a(d) + block_b(d) + rows_c)
    for blk, g in res.groupby("block"):
        res.loc[g.index, "p_holm_within_block"] = holm(g.p.fillna(1.0)).to_numpy()
    res.to_csv(OUT / "ph1_estimates.csv", index=False)
    grid.to_csv(OUT / "ph1_area_year.csv", index=False)
    raw = (d.groupby(["newcomer", "primary_class"]).accepted.agg(["mean", "size"])
           .rename(columns={"mean": "acceptance_rate", "size": "papers"}).reset_index())
    raw.to_csv(OUT / "ph1_raw_rates_by_class.csv", index=False)
    summary = {"population_papers": int(len(d)), "newcomer_papers": int(d.newcomer.sum()),
               "acceptance_newcomer": float(d[d.newcomer == 1].accepted.mean()),
               "acceptance_incumbent": float(d[d.newcomer == 0].accepted.mean()),
               "note": "post hoc exploratory (PREREGISTRATION.md post-run record); associations, not causal effects"}
    (OUT / "ph1_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    plot(res, grid)
    pd.set_option("display.width", 200)
    print(json.dumps(summary, indent=1))
    show = res.assign(**{c: (res[c] * 100).round(2) for c in ["coef", "ci95_lo", "ci95_hi"]})
    print(show[["block", "label", "coef", "ci95_lo", "ci95_hi", "p", "p_holm_within_block", "n"]].to_string(index=False))


if __name__ == "__main__":
    main()
