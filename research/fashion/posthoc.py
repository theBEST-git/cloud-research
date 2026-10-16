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

    python research/fashion/posthoc.py     (only after the frozen run; the code must be committed: outcomes.py)
Writes output/posthoc/ph1_*.csv, ph1_summary.json and output/figures/PH1_*.png/pdf.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from scipy import stats

import figures
import outcomes
import panel
from analysis import estimate
from common import OUTPUT, TOPICS
from ols import fe_ols
from panel import CLASS_CONTROLS
from variants import holm

OUT = OUTPUT / "posthoc"
YEARS = (2019, 2026)
CLASSES = ["method", "theory", "empirical", "dataset_benchmark", "evaluation", "other"]
BANDS = ["1-2", "3-4", "5-6", "7+"]
MIN_CELL = 50


def population() -> pd.DataFrame:
    k = panel.frame("k100")
    out = outcomes.load("posthoc", k.submission_id)
    assert (out.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    d = k.assign(rq3=out.rq3.to_numpy(), accepted=out.accepted.to_numpy())
    d = d[d.rq3 & d.has_author_key & d.year.between(*YEARS)].copy()
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    d["area"] = d.topic.map(cat[cat.level == "mid"].set_index("topic").parent_coarse)
    d["area_name"] = d.area.map(cat[cat.level == "coarse"].set_index("topic").name)
    d["band"] = pd.cut(d.team_size, [0, 2, 4, 6, np.inf], labels=BANDS).astype(str)
    d["maturity_tercile"] = pd.qcut(d.maturity, 3, labels=["young", "middle", "mature"]).astype(str)
    for b in BANDS:
        d[f"band_{b}"] = (d.band == b).astype(float)
    d["incumbent"] = 1 - d.newcomer
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


def main() -> None:
    d = population()
    OUT.mkdir(parents=True, exist_ok=True)
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
