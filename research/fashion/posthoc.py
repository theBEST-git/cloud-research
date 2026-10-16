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

    python research/fashion/posthoc.py ph1|ph2   (only after the frozen run; the code must be committed: outcomes.py)
Writes output/posthoc/ph{1,2}_*.csv and *.json and output/figures/PH{1,2}_*.png/pdf.
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
from common import OUTPUT, TOPICS
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
        ax.set_xlabel("pp acceptance per doubling of team size (95% CI)")
    fig.suptitle("Acceptance and team size within topic-year (post hoc, exploratory); dashed: all papers",
                 x=0.01, ha="left", fontsize=8.5)
    figures.save(fig, "PH2_team_size")


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which not in ("ph1", "ph2"):
        raise SystemExit("usage: posthoc.py ph1|ph2")
    OUT.mkdir(parents=True, exist_ok=True)
    if which == "ph2":
        ph2(with_outcomes())
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
