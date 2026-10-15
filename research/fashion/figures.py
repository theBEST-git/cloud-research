"""Paper figures (static PDF + PNG) for RQ1-RQ3. Colours follow the validated reference palette (light mode):
categorical slots in fixed order, one-hue sequential ramp, blue <-> red diverging with a grey midpoint.

F1  forest plots: main estimate, 95% CI and every counted variant, with the SESOI band (needs output/frozen_run)
F2  trends: contribution-class shares; foundation-model vs new-architecture share; incumbency rate (ID switch marked)
F3  hot topics: prior growth by topic and year for topics hot in >= 3 years, hot cells marked
F4  dose-response after removing fixed effects (E6; needs output/frozen_run)
F5  H2d validation: peripheral share, flagged vs non-flagged, majority and per judge, with the gate thresholds
F6  dry-run power: full-rule detection rate by planted effect, with 80% line
F7  acceptance rate by contribution class and year (E10; needs output/frozen_run)

    python research/fashion/figures.py
Writes output/figures/F*.pdf and .png. Figures whose inputs are missing are skipped and listed.
"""
from __future__ import annotations

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm  # noqa: E402

from common import OUTPUT, TOPICS, class_of  # noqa: E402

FIG = OUTPUT / "figures"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
INK, INK2, MUTED, GRID, SURFACE, NEUTRAL = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb", "#f0efec"
BLUE_RAMP = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
DIVERGING = LinearSegmentedColormap.from_list("bluered", ["#1c5cab", "#86b6ef", NEUTRAL, "#f2a3a2", "#c23b3b"])

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.6, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.5, "axes.axisbelow": True,
    "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "legend.frameon": False, "legend.fontsize": 7.5, "lines.linewidth": 1.6,
})


def save(fig, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(FIG / f"{name}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def end_label(ax, x, y, text: str, dy: float = 0.0) -> None:
    ax.annotate(text, (x, y), xytext=(4, dy), textcoords="offset points", va="center", fontsize=7, color=INK2)


def end_labels(ax, x, ys: dict[str, float], gap: float) -> None:
    """Direct labels at the line ends, pushed apart to at least `gap` data units, with a thin leader."""
    items = sorted(ys.items(), key=lambda kv: kv[1])
    placed = []
    for name, y in items:
        yy = max(y, placed[-1][1] + gap) if placed else y
        placed.append((name, yy, y))
    for name, yy, y in placed:
        ax.annotate(name, (x, y), xytext=(x + 0.35, yy), textcoords="data", va="center", fontsize=7, color=INK2,
                    arrowprops={"arrowstyle": "-", "color": MUTED, "lw": 0.5, "shrinkA": 0, "shrinkB": 1})


def f2_trends() -> None:
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz")
    lab["cls"] = lab.primary_type.map(class_of).replace({"dataset_benchmark": "measurement", "evaluation": "measurement"})
    shares = pd.crosstab(lab.year, lab.cls, normalize="index")
    var = pd.read_csv(OUTPUT / "paper_variables.csv.gz")
    k = var[(var["map"] == "k100") & var.has_author_key]
    inc = k.groupby("year").incumbent.mean()
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.4), constrained_layout=True)
    ax = axes[0]
    order = ["method", "empirical", "measurement", "theory", "other"]
    for i, c in enumerate(order):
        ax.plot(shares.index, shares[c] * 100, color=SERIES[i], label=c)
    end_labels(ax, shares.index[-1], {c: shares[c].iloc[-1] * 100 for c in order}, gap=5.5)
    ax.set_title("Contribution class (% of papers)", loc="left")
    ax.set_ylim(0, 85)
    ax.set_xlim(2017, 2029.6)
    ax.legend(loc="center left", bbox_to_anchor=(0.0, 0.6), ncol=1, handlelength=1.2)
    ax = axes[1]
    fm = (lab.foundation_model == "yes").groupby(lab.year).mean() * 100
    arch = (lab.primary_type == "model").groupby(lab.year).mean() * 100
    ax.plot(fm.index, fm, color=SERIES[0], label="builds on a foundation model")
    ax.plot(arch.index, arch, color=SERIES[1], label="proposes a new architecture")
    end_labels(ax, fm.index[-1], {"FM": fm.iloc[-1], "new arch.": arch.iloc[-1]}, gap=5)
    ax.set_title("FM use vs new architectures (%)", loc="left")
    ax.set_xlim(2017, 2028.9)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.93), handlelength=1.2, fontsize=6.5)
    ax = axes[2]
    ax.axvspan(2020.5, 2022.5, color=NEUTRAL, lw=0)
    ax.text(2021.5, 33.5, "author-ID\nswitch", ha="center", va="top", fontsize=6.5, color=INK2)
    ax.plot(inc.index, inc * 100, color=SERIES[0], marker="o", markersize=3.5, markeredgecolor=SURFACE, markeredgewidth=0.8)
    ax.set_title("Incumbent papers, k100 (%)", loc="left")
    ax.set_ylim(0, 36)
    for ax in axes:
        ax.set_xticks([2017, 2020, 2023, 2026])
    save(fig, "F2_trends")


def f3_hot_topics() -> None:
    var = pd.read_csv(OUTPUT / "paper_variables.csv.gz")
    k = var[(var["map"] == "k100") & (var.year >= 2019)].drop_duplicates(["topic", "year"])
    hot = k.pivot(index="topic", columns="year", values="hot")
    growth = np.log2(k.pivot(index="topic", columns="year", values="prior_growth"))
    keep = hot.index[hot.sum(axis=1) >= 3]
    first = hot.loc[keep].apply(lambda r: r[r == 1].index.min(), axis=1)
    keep = first.sort_values().index
    names = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False).set_index("topic").name
    g = growth.loc[keep]
    fig, ax = plt.subplots(figsize=(5.2, 0.17 * len(keep) + 0.9), constrained_layout=True)
    lim = np.nanmax(np.abs(g.values))
    cmap = DIVERGING.copy()
    cmap.set_bad(SURFACE)
    im = ax.imshow(np.ma.masked_invalid(g.values), aspect="auto", cmap=cmap, norm=TwoSlopeNorm(0, -lim, lim))
    yy, xx = np.where(hot.loc[keep].values == 1)
    ax.scatter(xx, yy, s=7, color=INK, linewidths=0, label="hot (top 20% prior growth)")
    ax.set_xticks(range(g.shape[1]), [f"'{y % 100:02d}" for y in g.columns], fontsize=6.5)
    labels = [f"{t} {names.get(t, '')}" for t in keep]
    ax.set_yticks(range(len(keep)), [s if len(s) < 52 else s[:50] + "…" for s in labels], fontsize=6.5)
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    cb = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.02)
    cb.set_label("log2 prior growth (share t-1 / t-2)", color=INK2)
    cb.outline.set_visible(False)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), fontsize=7)
    ax.set_title("Topics hot in >= 3 of 8 years (k100), by first hot year; blank = no papers", loc="left", pad=16)
    save(fig, "F3_hot_topics")


def f5_validation() -> None:
    v = json.loads((OUTPUT / "h2d_validation.json").read_text())
    fig, ax = plt.subplots(figsize=(3.6, 2.2), constrained_layout=True)
    rows = [("flagged uses", "p_flag", 0), ("non-flagged uses", "p_nonflag", 1)]
    for label, key, y in rows:
        lo, hi = v[f"{key}_ci95"]
        ax.plot([lo * 100, hi * 100], [y, y], color=SERIES[0], lw=1.6, solid_capstyle="round")
        ax.scatter([v[key] * 100], [y], s=36, color=SERIES[0], edgecolor=SURFACE, linewidth=1.2, zorder=3,
                   label="majority of 3 judges (95% CI)" if y == 0 else None)
        for j, (judge, r) in enumerate(v["per_judge"].items()):
            ax.scatter([r[key] * 100], [y + 0.18], s=12, marker="v", color=MUTED, zorder=3,
                       label="single judge" if (y == 0 and j == 0) else None)
    ax.axvline(50, color=INK2, lw=0.8, ls=(0, (3, 2)))
    ax.text(50.8, -0.5, "gate:\n>= 50%", fontsize=6.5, color=INK2, va="top")
    ax.axvline(2 * v["p_nonflag"] * 100, color=MUTED, lw=0.8, ls=(0, (1, 2)))
    ax.text(2 * v["p_nonflag"] * 100 + 0.8, -0.5, "gate: 2x\nnon-flagged", fontsize=6.5, color=INK2, va="top")
    ax.set_yticks([0, 1], [r[0] for r in rows])
    ax.set_ylim(1.45, -0.6)
    ax.set_xlim(0, 75)
    ax.set_xlabel("judged peripheral to the contribution (%)")
    ax.set_title(f"Buzzword measure, blind validation (gate: {v['gate']})", loc="left")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=2, fontsize=6.5)
    save(fig, "F5_h2d_validation")


def f6_power() -> None:
    s = json.loads((OUTPUT / "dryrun" / "summary.json").read_text())
    sesoi = {"H2a": 2, "H2b": 2, "H2c": 1, "H3a": 1, "H3b": 1}
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.3), sharey=True, constrained_layout=True)
    for ax, hs, title in [(axes[0], ["H2a", "H2b", "H2c"], "RQ2 (following)"), (axes[1], ["H3a", "H3b"], "RQ3 (reward)")]:
        for i, h in enumerate(hs):
            c = s["power"].get(h)
            if not c:
                continue
            x = [float(m) * sesoi[h] for m in c]
            y = [c[m]["full_rule"] * 100 for m in c]
            ax.plot(x, y, color=SERIES[i], marker="o", markersize=3.5, markeredgecolor=SURFACE, markeredgewidth=0.8, label=h)
            end_label(ax, x[-1], y[-1], h)
        ax.axhline(80, color=INK2, lw=0.8, ls=(0, (3, 2)))
        ax.set_title(title, loc="left")
        ax.set_xlabel("planted effect (percentage points)")
        ax.set_ylim(-3, 103)
        ax.legend(loc="lower right")
    axes[0].set_ylabel("supported under the full rule (%)")
    save(fig, "F6_power")


def f1_forest() -> None:
    fr = OUTPUT / "frozen_run"
    rq1 = pd.read_csv(OUTPUT / "rq1_results.csv").rename(columns={"hypothesis": "hypothesis"})
    rq1["kind"] = np.where(rq1.variant == "main", "main", "counted")
    rq1 = rq1.assign(sesoi=np.nan)
    rows = [rq1[["hypothesis", "variant", "kind", "coef", "se"]]]
    for f in ["rq2_results.csv", "rq3_results.csv"]:
        d = pd.read_csv(fr / f)
        rows.append(d[d.kind.isin(["main", "counted"])][["hypothesis", "variant", "kind", "coef", "se"]])
    d = pd.concat(rows, ignore_index=True)
    summ = json.loads((fr / "summary.json").read_text())
    verdict = {h: v["verdict"] for part in ("rq2", "rq3") for h, v in summ[part]["verdicts"].items()}
    sesoi = {h: v["sesoi"] for part in ("rq2", "rq3") for h, v in summ[part]["verdicts"].items()}
    rq1s = json.loads((OUTPUT / "rq1_summary.json").read_text())["hypotheses"]
    verdict.update({h: v["verdict"] for h, v in rq1s.items()})
    hyps = list(dict.fromkeys(d.hypothesis))
    fig, axes = plt.subplots(2, int(np.ceil(len(hyps) / 2)), figsize=(7.4, 3.6), constrained_layout=True)
    for ax, h in zip(axes.flat, hyps):
        g = d[d.hypothesis == h]
        m = g[g.kind == "main"].iloc[0]
        if h in sesoi:
            ax.axvspan(-sesoi[h] * 100, sesoi[h] * 100, color=NEUTRAL, lw=0)
        ax.axvline(0, color=INK2, lw=0.7)
        var = g[g.kind == "counted"]
        ax.scatter(var.coef * 100, np.linspace(0.35, 0.65, len(var)), s=10, color=MUTED, linewidths=0, label="variants")
        ax.plot([(m.coef - 1.96 * m.se) * 100, (m.coef + 1.96 * m.se) * 100], [0, 0], color=SERIES[0], lw=1.8,
                solid_capstyle="round")
        ax.scatter([m.coef * 100], [0], s=30, color=SERIES[0], edgecolor=SURFACE, linewidth=1.2, zorder=3, label="main (95% CI)")
        ax.set_ylim(1, -0.4)
        ax.set_yticks([])
        ax.set_title(f"{h}: {verdict.get(h, '')}", loc="left", fontsize=7.5)
        ax.tick_params(axis="x", labelsize=7)
    for ax in list(axes.flat)[len(hyps):]:
        ax.set_visible(False)
    axes.flat[0].legend(loc="lower left", fontsize=6.5)
    fig.supxlabel("estimate (percentage points; grey band = smallest effect of interest)", fontsize=7.5, color=INK2)
    save(fig, "F1_forest")


def f4_dose() -> None:
    d = pd.read_csv(OUTPUT / "frozen_run" / "dose_response.csv")
    labels = list(dict.fromkeys(d.label))
    fig, axes = plt.subplots(1, len(labels), figsize=(7.2, 2.2), constrained_layout=True)
    for ax, lab in zip(np.atleast_1d(axes), labels):
        g = d[d.label == lab]
        ax.plot(g.x, g.y * 100, color=SERIES[0], marker="o", markersize=3.5, markeredgecolor=SURFACE, markeredgewidth=0.8)
        ax.set_title(lab, loc="left", fontsize=7.5)
        ax.set_ylabel("% (FE removed, mean added back)")
    save(fig, "F4_dose_response")


def f7_acceptance() -> None:
    d = pd.read_csv(OUTPUT / "frozen_run" / "acceptance_by_class_year.csv")
    piv = d.pivot(index="year", columns="primary_class", values="acceptance_rate") * 100
    n = d.pivot(index="year", columns="primary_class", values="papers")
    order = [c for c in ["method", "empirical", "theory", "dataset_benchmark", "evaluation", "other"] if c in piv]
    fig, ax = plt.subplots(figsize=(4.2, 2.6), constrained_layout=True)
    for i, c in enumerate(order):
        s = piv[c].where(n[c] >= 30)
        ax.plot(s.index, s, color=SERIES[i], label=c, marker="o", markersize=3, markeredgecolor=SURFACE, markeredgewidth=0.6)
        end_label(ax, s.dropna().index[-1], s.dropna().iloc[-1], c)
    ax.set_xlim(2017.7, 2028.2)
    ax.set_ylabel("accepted (%)")
    ax.set_title("Acceptance rate by primary contribution class (cells with >= 30 papers)", loc="left")
    ax.legend(loc="lower left", ncol=2, fontsize=6.5)
    save(fig, "F7_acceptance_by_class")


def main() -> None:
    done, skipped = [], []
    for name, fn in [("F1", f1_forest), ("F2", f2_trends), ("F3", f3_hot_topics), ("F4", f4_dose), ("F5", f5_validation),
                     ("F6", f6_power), ("F7", f7_acceptance)]:
        try:
            fn()
            done.append(name)
        except FileNotFoundError as e:
            skipped.append(f"{name} ({e.filename})")
    print("written:", done, "| skipped (inputs missing):", skipped)


if __name__ == "__main__":
    main()
