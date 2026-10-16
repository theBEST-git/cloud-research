"""Slide figures for the talk. Reads only committed outputs (hindsight check, RQ1 results, frozen-run and post hoc
estimates) and the outcome-free contribution labels; it never reads acceptance or review columns.

Figures are drawn at about 1.55x their size on the slide, so 15 pt text lands near 10 pt.

    python research/fashion/presentation/make_figures.py      -> research/fashion/presentation/figs/*.pdf
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from common import OUTPUT, TOPICS  # noqa: E402

FIGS = HERE / "figs"
BLUE, ORANGE, GREEN = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, MUTED, GRID, BG, SHADE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fafafa", "#eeeeec"
FS = 15                                                                          # base font size

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": FS, "axes.titlesize": FS + 1, "axes.labelsize": FS,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.9, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "axes.titleweight": "bold", "axes.titlelocation": "left",
    "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG, "legend.frameon": False,
})
T99 = stats.t.ppf(0.975, 99)                                                    # 100 topic clusters


def minus(x: str) -> str:
    return x.replace("-", "−")


def save(fig, name: str) -> None:
    fig.savefig(FIGS / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(FIGS / f"{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def hindsight() -> None:
    """Effective number of topics (of 100) per year under maps fitted on different years."""
    maps = json.loads((TOPICS / "hindsight_check.json").read_text())["maps"]
    fig, ax = plt.subplots(figsize=(5.6, 3.7))
    for key, label, colour in [("early", "2017–20 map", GREEN), ("pooled", "standard map", BLUE),
                               ("late", "2024–26 map", ORANGE)]:
        eff = maps[key]["effective_topics_over_k_by_year"]
        years, vals = [int(y) for y in eff], [100 * v for v in eff.values()]
        ax.plot(years, vals, color=colour, lw=3, marker="o", ms=6, mec=BG, mew=1.5)
        ax.annotate(label, (years[-1], vals[-1]), xytext=(8, 0), textcoords="offset points", va="center",
                    color=colour, fontsize=FS, fontweight="bold")
    ax.set_xticks(range(2017, 2027, 3))
    ax.set_xlim(2016.6, 2026.4)
    ax.set_ylim(38, 100)
    ax.set_ylabel("topics in real use (of 100)")
    save(fig, "hindsight_diversity")


def emerging() -> None:
    """Backup: number of topics that look 'emerging' under each map."""
    maps = json.loads((TOPICS / "hindsight_check.json").read_text())["maps"]
    rows = [("early", "2017–20 papers", GREEN), ("balanced", "all years, equal weight", MUTED),
            ("pooled", "all years (standard)", BLUE), ("late", "2024–26 papers", ORANGE)]
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    y = list(range(len(rows)))[::-1]
    counts = [maps[k]["emerging_topics"] for k, _, _ in rows]
    ax.barh(y, counts, color=[c for _, _, c in rows], height=0.6)
    for yi, c in zip(y, counts):
        ax.text(c + 0.6, yi, str(c), va="center", fontsize=FS + 1, color=INK, fontweight="bold")
    ax.set_yticks(y, [r for _, r, _ in rows])
    ax.set_xlim(0, 34)
    ax.set_xlabel("topics that look 'emerging' (≥3× growth)")
    ax.grid(axis="y", visible=False)
    ax.set_title("Map built from …", fontsize=FS)
    save(fig, "hindsight_emerging")


def lifecycle() -> None:
    """H1a / H1b under the standard map and the early map: same model, same papers (and the prospective version)."""
    r = pd.read_csv(OUTPUT / "rq1_results.csv")
    rows = [("main", "standard map", BLUE), ("early", "early map", GREEN),
            ("early_prospective", "early map,\n2021–26 papers", GREEN)]
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2), sharey=True)
    for ax, (h, title, pred) in zip(axes, [("H1a", "New-method papers", "predicted: fewer"),
                                             ("H1b", "Benchmark & evaluation papers", "predicted: more")]):
        for i, (variant, _, colour) in enumerate(rows):
            g = r[(r.hypothesis == h) & (r.variant == variant)].iloc[0]
            c, se = 100 * g.coef, 100 * g.se
            yi = len(rows) - 1 - i
            ax.plot([c - T99 * se, c + T99 * se], [yi, yi], color=colour, lw=3.5, solid_capstyle="round")
            ax.plot(c, yi, "o", color=colour, ms=11, mec=BG, mew=1.5)
            ax.annotate(minus(f"{c:+.1f}"), (c, yi), xytext=(0, 10), textcoords="offset points", ha="center",
                        fontsize=FS, color=INK, fontweight="bold")
        ax.axvline(0, color=INK2, lw=1.2)
        ax.set_title(title)
        ax.set_xlim(-7.5, 7.5)
        ax.set_ylim(-0.6, 2.75)
        ax.text(0.98 if h == "H1b" else 0.02, 0.03, pred, transform=ax.transAxes, fontsize=FS - 2, color=MUTED,
                ha="right" if h == "H1b" else "left")
        ax.set_xlabel("pp per 2.7× more papers", fontsize=FS - 1)
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(len(rows))[::-1], [lab for _, lab, _ in rows])
    fig.tight_layout(w_pad=1.5)
    save(fig, "lifecycle_flip")


def fm_trend() -> None:
    """Share of papers building on a foundation model vs proposing a new architecture, by year (outcome-free)."""
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz", usecols=["year", "primary_type", "foundation_model"])
    by = lab.groupby("year").agg(fm=("foundation_model", lambda s: (s == "yes").mean()),
                                 arch=("primary_type", lambda s: (s == "model").mean())) * 100
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    for col, colour in [("fm", BLUE), ("arch", ORANGE)]:
        ax.plot(by.index, by[col], color=colour, lw=3.2, marker="o", ms=6, mec=BG, mew=1.5)
        for x, v, dx, ha in [(by.index[0], by[col].iloc[0], -8, "right"), (by.index[-1], by[col].iloc[-1], 8, "left")]:
            low = v < 1                                                          # 0.3%: label above the point
            ax.annotate(f"{v:.1f}%" if low else f"{v:.0f}%", (x, v), xytext=(0, 12) if low else (dx, 0),
                        textcoords="offset points", va="center", ha="center" if low else ha, fontsize=FS,
                        color=INK, fontweight="bold")
    ax.text(2017.3, 49, "builds on a\nfoundation model", color=BLUE, fontsize=FS, fontweight="bold")
    ax.text(2017.6, 29, "proposes a new\narchitecture", color=ORANGE, fontsize=FS, fontweight="bold")
    ax.set_xticks(range(2017, 2027, 3))
    ax.set_xlim(2014.9, 2027.6)
    ax.set_ylim(-2, 60)
    ax.set_ylabel("% of submissions")
    save(fig, "fm_trend")


def newcomers() -> None:
    """H2b / H2c: main estimate with 95% CI, the ten counted variants, and the predicted side shaded."""
    r = pd.read_csv(OUTPUT / "frozen_run" / "rq2_results.csv")
    fig, axes = plt.subplots(2, 1, figsize=(5.4, 3.9), sharex=True)
    for ax, h, title, sign in [(axes[0], "H2b", "New-method papers", -1),
                               (axes[1], "H2c", "Benchmark & evaluation papers", 1)]:
        g = r[r.hypothesis == h]
        m = g[g.kind == "main"].iloc[0]
        v = g[g.kind == "counted"]
        lo, hi = (-5, 0) if sign < 0 else (0, 5)
        ax.axvspan(lo, hi, color=SHADE, zorder=0)
        ax.text(lo + 0.15 if sign < 0 else hi - 0.15, 0.72, "we predicted\nthis side", fontsize=FS - 2,
                color=MUTED, ha="left" if sign < 0 else "right", va="center")
        ax.scatter(100 * v.coef, [0.45] * len(v), s=70, marker="|", color=INK2, lw=2.2, zorder=2)
        ax.plot([100 * m.ci95_lo, 100 * m.ci95_hi], [0, 0], color=INK, lw=3.5, zorder=3, solid_capstyle="round")
        ax.plot(100 * m.coef, 0, "o", color=BLUE if sign < 0 else ORANGE, ms=14, mec=BG, mew=1.5, zorder=4)
        ax.annotate(minus(f"{100 * m.coef:+.1f} pp"), (100 * m.coef, 0), xytext=(0, -26),
                    textcoords="offset points", ha="center", fontsize=FS + 1, fontweight="bold", color=INK)
        ax.axvline(0, color=INK2, lw=1.2)
        ax.set_yticks([])
        ax.set_ylim(-1, 1)
        ax.set_title(title, fontsize=FS)
        ax.grid(axis="y", visible=False)
        ax.spines["left"].set_visible(False)
    axes[1].annotate("10 alternative analyses", (100 * r[(r.hypothesis == "H2c") & (r.kind == "counted")].coef.min(),
                                                  0.45), xytext=(-10, 0), textcoords="offset points", ha="right",
                     va="center", fontsize=FS - 2, color=INK2)
    axes[1].set_xlim(-5, 5)
    axes[1].set_xlabel("newcomer minus incumbent paper (pp)")
    fig.tight_layout(h_pad=0.4)
    save(fig, "newcomers")


def newcomer_gap() -> None:
    """Backup: the newcomer acceptance gap as controls are added (E2, then post hoc PH3; committed estimates)."""
    e = pd.read_csv(OUTPUT / "frozen_run" / "exploratory_estimates.csv")
    e2 = e[(e.analysis == "E2") & e.label.str.contains("classes")].iloc[0]
    ph3 = pd.read_csv(OUTPUT / "posthoc" / "ph3_estimates.csv").set_index("model")
    rows = [("same topic and year", e2.coef, e2.ci95_lo, e2.ci95_hi),
            ("+ team size and\nICLR experience", *ph3.loc["M0", ["coef", "ci95_lo", "ci95_hi"]]),
            ("+ same authors\n(author fixed effects)", *ph3.loc["M1", ["coef", "ci95_lo", "ci95_hi"]])]
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    for i, (label, c, lo, hi) in enumerate(rows):
        yi = len(rows) - 1 - i
        ax.barh(yi, 100 * c, color=[MUTED, MUTED, BLUE][i], height=0.55)
        ax.plot([100 * lo, 100 * hi], [yi, yi], color=INK, lw=1.6)
        ax.text(100 * lo - 0.3, yi, minus(f"{100 * c:.1f}"), ha="right", va="center", fontsize=FS, fontweight="bold")
    ax.set_yticks(range(len(rows))[::-1], [r[0] for r in rows])
    ax.yaxis.tick_right()
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(True)
    ax.set_xlim(-14.5, 0)
    ax.set_xticks([-12, -8, -4, 0], ["−12", "−8", "−4", "0"])
    ax.set_xlabel("newcomer acceptance gap (pp, 95% CI)")
    ax.grid(axis="y", visible=False)
    save(fig, "newcomer_gap")


def team_size() -> None:
    """Backup: acceptance by team-size band (post hoc PH2, committed summary)."""
    s = json.loads((OUTPUT / "posthoc" / "ph2_summary.json").read_text())["acceptance_by_band"]
    bands = ["1-2", "3-4", "5-6", "7+"]
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    vals = [100 * s[b] for b in bands]
    ax.bar(bands, vals, color=BLUE, width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v + 1, f"{v:.0f}%", ha="center", fontsize=FS, color=INK, fontweight="bold")
    ax.set_ylim(0, 58)
    ax.set_xlabel("authors on the paper")
    ax.set_ylabel("accepted (%)")
    ax.grid(axis="x", visible=False)
    save(fig, "team_size")


if __name__ == "__main__":
    FIGS.mkdir(exist_ok=True)
    for make in (hindsight, emerging, lifecycle, fm_trend, newcomers, newcomer_gap, team_size):
        make()
    print("figures written to", FIGS)
