"""Slide figures for the talk. Reads only committed outputs (hindsight check, RQ1 results, frozen-run and post hoc
estimates, including PH4 and PH5), the outcome-free contribution labels, the estimates of the single held-out
(confirmation) run in output_pooled/confirmation_run, and the estimates of the exploratory pooled re-run in
output_pooled/ (pooled_table, appendix A18); it never reads acceptance or review columns.

Figures are drawn at about 1.55x their size on the slide, so 15 pt text lands near 10 pt. Academic style: white
background, plain panel labels (a), (b), formal axis titles; captions are set in LaTeX. replication_table() writes a
booktabs table (figs/replication_table.tex) that slides.tex includes with \\input.

    python research/fashion/presentation/make_figures.py      -> research/fashion/presentation/figs/*.pdf

From a copy outside the repository, point PYTHONPATH at research/fashion (for common.py) and leave ICLR_CORPUS unset,
so that every read resolves to the committed discovery outputs:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<repo>/research/fashion python make_figures.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import transforms  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from common import CORPUS, OUTPUT, POOLED_OUTPUT, TOPICS  # noqa: E402

assert CORPUS == "discovery", "run with ICLR_CORPUS unset: the slides quote the discovery record"
CONFIRM = POOLED_OUTPUT / "confirmation_run"                                    # the single held-out run (read-only)
FIGS = HERE / "figs"
BLUE, ORANGE, GREEN = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, MUTED, GRID, BG, SHADE = "#0b0b0b", "#3a3a38", "#7a7974", "#e4e3df", "#ffffff", "#efefed"
FS = 15                                                                          # base font size

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": FS, "axes.titlesize": FS + 1, "axes.labelsize": FS,
    "axes.edgecolor": INK2, "axes.linewidth": 0.9, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "axes.titleweight": "normal", "axes.titlelocation": "left",
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
                    color=colour, fontsize=FS)
    ax.set_xticks(range(2017, 2027, 3))
    ax.set_xlim(2016.6, 2026.4)
    ax.set_ylim(38, 100)
    ax.set_xlabel("Submission year")
    ax.set_ylabel("Effective topics (of 100)")
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
        ax.text(c + 0.6, yi, str(c), va="center", fontsize=FS + 1, color=INK)
    ax.set_yticks(y, [r for _, r, _ in rows])
    ax.set_xlim(0, 34)
    ax.set_xlabel("Number of emerging topics (≥3× growth)")
    ax.grid(axis="y", visible=False)
    ax.set_title("Map fitted on", fontsize=FS)
    save(fig, "hindsight_emerging")


def lifecycle() -> None:
    """H1a / H1b under the standard map and the early map: same model, same papers (and the prospective version)."""
    r = pd.read_csv(OUTPUT / "rq1_results.csv")
    rows = [("main", "standard map", BLUE), ("early", "early map", GREEN),
            ("early_prospective", "early map,\n2021–26 papers", GREEN)]
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2), sharey=True)
    for ax, (h, title, pred) in zip(axes, [("H1a", "(a) New-method papers", "predicted: −"),
                                             ("H1b", "(b) Benchmark & evaluation papers", "predicted: +")]):
        for i, (variant, _, colour) in enumerate(rows):
            g = r[(r.hypothesis == h) & (r.variant == variant)].iloc[0]
            c, se = 100 * g.coef, 100 * g.se
            yi = len(rows) - 1 - i
            ax.plot([c - T99 * se, c + T99 * se], [yi, yi], color=colour, lw=3.5, solid_capstyle="round")
            ax.plot(c, yi, "o", color=colour, ms=11, mec=BG, mew=1.5)
            ax.annotate(minus(f"{c:+.1f}"), (c, yi), xytext=(0, 10), textcoords="offset points", ha="center",
                        fontsize=FS, color=INK)
        ax.axvline(0, color=INK2, lw=1.2)
        ax.set_title(title)
        ax.set_xlim(-7.5, 7.5)
        ax.set_ylim(-0.6, 2.75)
        ax.text(0.98 if h == "H1b" else 0.02, 0.03, pred, transform=ax.transAxes, fontsize=FS - 2, color=MUTED,
                ha="right" if h == "H1b" else "left")
        ax.set_xlabel("Estimate (pp)", fontsize=FS - 1)
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
                        color=INK)
    ax.text(2017.3, 49, "builds on a\nfoundation model", color=BLUE, fontsize=FS)
    ax.text(2017.6, 29, "proposes a new\narchitecture", color=ORANGE, fontsize=FS)
    ax.set_xticks(range(2017, 2027, 3))
    ax.set_xlim(2014.9, 2027.6)
    ax.set_ylim(-2, 60)
    ax.set_xlabel("Submission year")
    ax.set_ylabel("Share of submissions (%)")
    save(fig, "fm_trend")


def newcomers() -> None:
    """H2b / H2c: main estimate with 95% CI, the ten counted variants, and the predicted side shaded."""
    r = pd.read_csv(OUTPUT / "frozen_run" / "rq2_results.csv")
    fig, axes = plt.subplots(2, 1, figsize=(5.4, 3.9), sharex=True)
    for ax, h, title, sign in [(axes[0], "H2b", "(a) New-method papers (H2b)", -1),
                               (axes[1], "H2c", "(b) Benchmark & evaluation papers (H2c)", 1)]:
        g = r[r.hypothesis == h]
        m = g[g.kind == "main"].iloc[0]
        v = g[g.kind == "counted"]
        lo, hi = (-5, 0) if sign < 0 else (0, 5)
        ax.axvspan(lo, hi, color=SHADE, zorder=0)
        ax.text(lo + 0.15 if sign < 0 else hi - 0.15, 0.72, "registered\nprediction", fontsize=FS - 2,
                color=MUTED, ha="left" if sign < 0 else "right", va="center")
        ax.scatter(100 * v.coef, [0.45] * len(v), s=70, marker="|", color=INK2, lw=2.2, zorder=2)
        ax.plot([100 * m.ci95_lo, 100 * m.ci95_hi], [0, 0], color=INK, lw=3.5, zorder=3, solid_capstyle="round")
        ax.plot(100 * m.coef, 0, "o", color=BLUE if sign < 0 else ORANGE, ms=14, mec=BG, mew=1.5, zorder=4)
        ax.annotate(minus(f"{100 * m.coef:+.1f} pp"), (100 * m.coef, 0), xytext=(0, -26),
                    textcoords="offset points", ha="center", fontsize=FS + 1, color=INK)
        ax.axvline(0, color=INK2, lw=1.2)
        ax.set_yticks([])
        ax.set_ylim(-1, 1)
        ax.set_title(title, fontsize=FS)
        ax.grid(axis="y", visible=False)
        ax.spines["left"].set_visible(False)
    axes[1].annotate("10 alternative specs.", (100 * r[(r.hypothesis == "H2c") & (r.kind == "counted")].coef.min(),
                                                  0.45), xytext=(-10, 0), textcoords="offset points", ha="right",
                     va="center", fontsize=FS - 2, color=INK2)
    axes[1].set_xlim(-5, 5)
    axes[1].set_xlabel("Coefficient on newcomer paper (pp, 95% CI)")
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
        ax.text(100 * lo - 0.3, yi, minus(f"{100 * c:.1f}"), ha="right", va="center", fontsize=FS)
    ax.set_yticks(range(len(rows))[::-1], [r[0] for r in rows])
    ax.yaxis.tick_right()
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(True)
    ax.set_xlim(-14.5, 0)
    ax.set_xticks([-12, -8, -4, 0], ["−12", "−8", "−4", "0"])
    ax.set_xlabel("Newcomer coefficient (pp, 95% CI)")                  # short enough not to run off the left edge
    ax.grid(axis="y", visible=False)
    save(fig, "newcomer_gap")


def area_ranking() -> None:
    """PH4: among keywords with >= 5 years of >= 10 papers, the six highest and six lowest acceptance levels."""
    r = pd.read_csv(OUTPUT / "posthoc" / "ph4_keywords.csv")
    r = r[r.years_with_min_cell >= 5].sort_values("level")
    pick = pd.concat([r.head(6), r.tail(6)])
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    y = np.arange(len(pick))
    for yi, (_, x) in zip(y, pick.iterrows()):
        colour = ORANGE if x.level < 0 else BLUE
        ax.plot([100 * x.level_ci_lo, 100 * x.level_ci_hi], [yi, yi], color=colour, lw=2.4, solid_capstyle="round")
        ax.plot(100 * x.level, yi, "o", color=colour, ms=8, mec=BG, mew=1.2)
    labels = [u + ("  ◀" if u == "federated learning" else "") for u in pick.unit]
    ax.set_yticks(y, labels, fontsize=FS - 2)
    ax.axvline(0, color=INK2, lw=1)
    ax.axhline(5.5, color=GRID, lw=1.2, ls="--")
    ax.set_xlabel("Gap vs. same-year papers (pp, 95% CI)")
    ax.grid(axis="y", visible=False)
    save(fig, "area_ranking")


def fl_story() -> None:
    """PH4/PH4b for federated learning: share of all submissions (outcome-free) and the acceptance gap by year."""
    comp = pd.read_csv(OUTPUT / "posthoc" / "ph4_mechanism_composition.csv")
    comp = comp[comp.unit == "federated learning"]
    cells = pd.read_csv(OUTPUT / "posthoc" / "ph4_keywords_cells.csv")
    c = cells[(cells.unit == "federated learning") & (cells.papers >= 10)]
    lvl = pd.read_csv(OUTPUT / "posthoc" / "ph4_keywords.csv").set_index("unit").loc["federated learning", "level"]
    # drawn at about 1.9x its size on the slide (shown at 0.56\textwidth), so FS text lands near 8 pt
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.35))
    ax = axes[0]
    ax.plot(comp.year, 100 * comp.share_of_all_submissions, color=BLUE, lw=3, marker="o", ms=6, mec=BG, mew=1.5)
    peak = comp.loc[comp.share_of_all_submissions.idxmax()]
    ax.annotate(f"peak {100 * peak.share_of_all_submissions:.1f}%", (peak.year, 100 * peak.share_of_all_submissions),
                xytext=(-6, 8), textcoords="offset points", ha="right", fontsize=FS)
    ax.set_title("(a) Share of submissions (%)", fontsize=FS)
    ax.set_ylim(0, 4.2)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax = axes[1]
    ax.axhline(0, color=INK2, lw=1)
    ax.axhline(100 * lvl, color=ORANGE, lw=1.2, ls="--")
    ax.errorbar(c.year, 100 * c.gap, yerr=196 * c.gap_se, fmt="o", color=ORANGE, ms=7, lw=2, capsize=0, mec=BG)
    # the average's label sits in the right margin, clear of the error bars
    ax.text(1.02, 100 * lvl, f"avg.\n{100 * lvl:+.0f}".replace("-", "−"), color=ORANGE, fontsize=FS, va="center",
            ha="left", transform=transforms.blended_transform_factory(ax.transAxes, ax.transData))
    ax.set_title("(b) Acceptance gap (pp)", fontsize=FS)
    ax.set_yticks([-40, -20, 0, 20, 40])
    for a_ in axes:
        a_.set_xticks([2018, 2022, 2026])
        a_.set_xlim(2017.5, 2026.5)
        a_.grid(axis="x", visible=False)
        a_.tick_params(labelsize=FS)
    fig.tight_layout(w_pad=1.6)
    save(fig, "fl_story")


def team_size() -> None:
    """Backup: acceptance by team-size band (post hoc PH2, committed summary)."""
    s = json.loads((OUTPUT / "posthoc" / "ph2_summary.json").read_text())["acceptance_by_band"]
    bands = ["1-2", "3-4", "5-6", "7+"]
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    vals = [100 * s[b] for b in bands]
    ax.bar(bands, vals, color=BLUE, width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v + 1, f"{v:.0f}%", ha="center", fontsize=FS, color=INK)
    ax.set_ylim(0, 58)
    ax.set_xlabel("Number of authors")
    ax.set_ylabel("Acceptance rate (%)")
    ax.grid(axis="x", visible=False)
    save(fig, "team_size")


def far_jump() -> None:
    """PH5 pivot (post hoc in discovery; held-out test registered): (a) discovery adjusted acceptance by quintile of
    closeness to the experienced co-authors' earlier ICLR work; (b) the declared far-jump contrast E1 (closeness at
    p10 minus the median), discovery vs held-out papers, each with its 95% CI. Sample sizes go in the LaTeX caption."""
    q = pd.read_csv(OUTPUT / "posthoc" / "ph5_pivot" / "quintiles.csv")
    q = q[q.model.str.startswith("P1 F_max")].sort_values("quintile")
    disc = pd.read_csv(OUTPUT / "posthoc" / "ph5_pivot" / "tests.csv").set_index("test").loc["E1"]
    held = pd.read_csv(CONFIRM / "ph5" / "tests.csv").set_index("test").loc["E1"]
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 4.1), gridspec_kw={"width_ratios": [1.3, 1]})
    ax = axes[0]
    x = np.arange(1, 6)
    c, lo, hi = 100 * q.coef.to_numpy(), 100 * q.ci95_lo.to_numpy(), 100 * q.ci95_hi.to_numpy()
    ax.vlines(x, lo, hi, color=BLUE, lw=3, zorder=2)
    ax.plot(x, c, "o", color=BLUE, ms=10, mec=BG, mew=1.5, zorder=3)
    for xi, v, h in zip(x, c, hi):
        ax.annotate(f"{v:.1f}", (xi, h), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                    fontsize=FS - 2, color=INK)
    ax.set_xticks(x, ["1\nfar", "2", "3", "4", "5\nclose"])
    ax.set_xlim(0.4, 5.6)
    ax.set_ylim(36, 51)
    ax.set_yticks([38, 42, 46, 50])
    ax.set_xlabel("Closeness quintile")
    ax.set_ylabel("Adjusted acceptance (%)")
    ax.set_title("(a) Discovery", fontsize=FS)
    ax.grid(axis="x", visible=False)
    ax = axes[1]
    for i, (r, colour) in zip([0, 1.25], [(disc, BLUE), (held, ORANGE)]):
        ax.plot([i, i], [100 * r.ci95_lo, 100 * r.ci95_hi], color=colour, lw=3.5, solid_capstyle="round")
        ax.plot(i, 100 * r.coef, "o", color=colour, ms=11, mec=BG, mew=1.5)
        ax.annotate(minus(f"{100 * r.coef:.1f}"), (i, 100 * r.ci95_lo), xytext=(0, -6), textcoords="offset points",
                    ha="center", va="top", fontsize=FS - 2, color=INK)
    ax.axhline(0, color=INK2, lw=1.2)
    ax.set_xticks([0, 1.25], ["Discovery", "Held-out"], fontsize=FS - 2)
    ax.set_xlim(-0.65, 1.9)
    ax.set_ylim(-12.5, 1)
    ax.set_yticks([-12, -8, -4, 0])
    ax.set_ylabel("Far minus median (pp)")
    ax.set_title("(b) Far jump", fontsize=FS)
    ax.grid(axis="x", visible=False)
    fig.tight_layout(w_pad=1.2)
    save(fig, "far_jump")


def premia_scatter() -> None:
    """Backup: early-map topic premia out of sample. x = committed discovery 2018-22 raw premium, y = held-out 2024-26
    premium (75 units with >= 15 decided held-out papers), the registered WLS slope b and the line y = x."""
    u = pd.read_csv(CONFIRM / "ph5" / "premia_units.csv")
    u = u[(u.unit_type == "early") & u.used]
    p = pd.read_csv(CONFIRM / "ph5" / "premia.csv").set_index("unit_type").loc["early"]
    w = 1 / (u.v2 + (p.tau_w2_pp / 100) ** 2)                               # the registered weights
    xm, ym = (w * u.w1).sum() / w.sum(), (w * u.w2).sum() / w.sum()
    b = (w * (u.w1 - xm) * (u.w2 - ym)).sum() / (w * (u.w1 - xm) ** 2).sum()
    assert abs(b - p.b) < 1e-9, "slope does not reproduce premia.csv"
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    ax.axhline(0, color=GRID, lw=1.2, zorder=0)
    ax.axvline(0, color=GRID, lw=1.2, zorder=0)
    ax.scatter(100 * u.w1, 100 * u.w2, s=12 + 0.45 * u.papers_w2, color=BLUE, alpha=0.55, edgecolor=BG, lw=0.6,
               zorder=2)
    xs = np.array([-17, 22])
    ax.plot(xs, xs, color=MUTED, lw=1.5, ls="--", zorder=1)
    ax.plot(xs, 100 * (ym + b * (xs / 100 - xm)), color=ORANGE, lw=3, zorder=3)
    ax.text(21.5, 21.5, "y = x", color=MUTED, fontsize=FS - 2, ha="right", va="bottom")
    ax.text(-16, 18, f"slope b = {p.b:.2f}\n(95% CI {p.b_ci95_lo:.2f} to {p.b_ci95_hi:.2f})", color=ORANGE,
            fontsize=FS - 1, va="top")
    ax.set_xlim(-17, 22)
    ax.set_ylim(-25, 24)
    ax.set_xlabel("Discovery premium, 2018–22 (pp)")
    ax.set_ylabel("Held-out premium, 2024–26 (pp)")
    save(fig, "premia_scatter")


def _tex(text: str) -> str:
    return text.replace("-", "$-$").replace("+", "$+$")


def _pp(x: float, d: int = 1) -> str:
    """A proportion as signed percentage points, LaTeX minus and plus."""
    return _tex(f"{100 * x:+.{d}f}")


def _ci(lo: float, hi: float, d: int = 1, scale: float = 100, sign: bool = True) -> str:
    f = (lambda v: f"{scale * v:+.{d}f}") if sign else (lambda v: f"{scale * v:.{d}f}")
    return _tex(f"[{f(lo)}, {f(hi)}]")


def _p(p: float) -> str:
    return f"{p:.3f}" if p < 0.1 else f"{p:.2f}"


def replication_table() -> None:
    """figs/replication_table.tex: registered tests on the held-out papers next to the discovery estimates.

    Discovery numbers come from the committed discovery outputs (rq1_results, frozen_run, posthoc PH4/PH5); held-out
    numbers from output_pooled/confirmation_run (summary.json, ph5/tests.csv). Estimates in pp unless noted; p is
    one-sided, Holm-adjusted within the registered families (RQ2; PH5 primary), unadjusted for the secondary tests; the
    group headings say which. The discovery premia b (double dagger) is the within-discovery 2024-26 on 2018-22 slope,
    a different comparison from the held-out b."""
    s = json.loads((CONFIRM / "summary.json").read_text())
    ph5 = pd.read_csv(CONFIRM / "ph5" / "tests.csv").set_index("test")
    rq1 = pd.read_csv(OUTPUT / "rq1_results.csv")
    rq1 = rq1[(rq1.hypothesis == "H1d") & (rq1.variant == "main")].iloc[0]
    rq2 = pd.read_csv(OUTPUT / "frozen_run" / "rq2_results.csv")
    rq2 = rq2[rq2.kind == "main"].set_index("hypothesis")
    disc = json.loads((OUTPUT / "frozen_run" / "summary.json").read_text())
    fl = pd.read_csv(OUTPUT / "posthoc" / "ph4_keywords.csv").set_index("unit").loc["federated learning"]
    piv = pd.read_csv(OUTPUT / "posthoc" / "ph5_pivot" / "tests.csv").set_index("test")
    pos = pd.read_csv(OUTPUT / "posthoc" / "ph5_position" / "tests.csv").set_index("test")
    teams = pd.read_csv(OUTPUT / "posthoc" / "ph5_teams" / "family.csv").set_index("test")
    kw = pd.read_csv(OUTPUT / "posthoc" / "ph5_kwtiming" / "tests.csv").set_index("test")
    prem = pd.read_csv(OUTPUT / "posthoc" / "ph5_premia" / "tests.csv")
    prem_b = prem[(prem.unit_type == "early") & (prem.test == "b")].iloc[0]

    v = {"H1d": s["rq1"]["verdicts"]["H1d"], "H2b'": s["rq2"]["verdicts"]["H2b'"],
         "H2c'": s["rq2"]["verdicts"]["H2c'"], "H3a": s["rq3"]["verdicts"]["H3a"]}
    fl_h = s["h4fl"]["primary"]
    sign = {-1: "$-$", 1: "$+$"}
    dagger = r"\textsuperscript{\dag}"

    def verdict(text: str, est: float, mde: float | None) -> str:
        """The registered reading rule: a non-supported test whose |estimate| is below its MDE80 is uninformative."""
        if text != "supported" and mde is not None and abs(est) < mde:
            return text + dagger
        return text

    def bold(test_id: str) -> str:
        return r"\textbf{" + test_id + "}"

    def group(title: str, first: bool = False) -> str:
        return ("" if first else "\\addlinespace[2pt]\n") + rf"\multicolumn{{6}}{{@{{}}l}}{{\emph{{{title}}}}} \\"

    rows: list[tuple[str, ...] | str] = [group("Registered hypotheses (one-sided $p$, Holm-adjusted within family)",
                                                first=True)]
    for h, label in [("H1d", "FM adoption (0 $\\to$ 1) $\\to$ new arch."),
                     ("H2b'", "newcomer $\\to$ method paper"),
                     ("H2c'", "newcomer $\\to$ benchmark paper"),
                     ("H3a", "maturity (log) $\\to$ acceptance")]:
        r = v[h]
        if h == "H1d":
            d = _pp(rq1.coef)
        elif h == "H3a":
            d = _pp(disc["rq3"]["verdicts"]["H3a"]["coef"])
        else:
            d = _pp(rq2.loc[h.rstrip("'")].coef)
        rows.append((bold(h.replace("'", "$'$")) + " " + label, sign[r["predicted_sign"]], d,
                     f"{_pp(r['coef'])} {_ci(*r['ci95'])}", _p(r["p_holm"]),
                     verdict(r["verdict"], r["coef"], r.get("mde80"))))
    rows.append((bold("H4-FL") + " FL keyword $\\to$ acceptance", sign[fl_h["predicted_sign"]],
                 _pp(fl.level), f"{_pp(fl_h['coef'])} {_ci(*fl_h['ci95'])}", _p(fl_h["p_holm"]),
                 verdict(fl_h["verdict"], fl_h["coef"], fl_h["mde80"])))
    rows.append(group("PH5 primary (post hoc in discovery; one-sided $p$, Holm-adjusted over the pair)"))
    for t, label, d in [("E1", "far jump (p10 $-$ median)", piv.loc["E1"].coef),
                        ("P1b", "least-novel $-$ middle fifth", pos.loc["P1b"].coef)]:
        r = ph5.loc[t]
        rows.append((f"{bold(t)} {label}", sign[int(r.predicted_sign)], _pp(d),
                     f"{_pp(r.coef)} {_ci(r.ci95_lo, r.ci95_hi)}", _p(r.p_holm),
                     verdict(r.verdict, r.coef, r.mde80_calibrated)))
    rows.append(group("PH5 secondary (one-sided $p$, unadjusted)"))
    for t, label, d, digits in [("E4", "within author, per $+$0.1 cos", piv.loc["E4"].coef, 2),
                                ("H1", "teams: one insider vs none", teams.loc["H1"].estimate, 1),
                                ("A1", "Emerging $-$ Mainstream keyword", kw.loc["A1"].coef, 1)]:
        r = ph5.loc[t]
        name = "Teams H1" if t == "H1" else t
        rows.append((f"{bold(name)} {label.replace('teams: ', '')}", sign[int(r.predicted_sign)], _pp(d, digits),
                     f"{_pp(r.coef, digits)} {_ci(r.ci95_lo, r.ci95_hi, digits)}", _p(r.p), r.verdict))
    r = ph5.loc["premia_b"]
    rows.append((bold("Premia $b$") + " topic edges (early map)", "$0<b<1$",
                 f"{prem_b.estimate:.2f}" + r"\textsuperscript{\ddag}",
                 f"{r.coef:.2f} {_ci(r.ci95_lo, r.ci95_hi, 2, 1, False)}", _p(r.p), r.verdict))

    lines = [r"% generated by make_figures.replication_table(); do not edit by hand",
             r"\begin{tabular}{@{}l c r l r l@{}}", r"\toprule",
             r"Test & Pred. & Discovery & Held-out [95\% CI] & One-sided $p$ & Verdict \\", r"\midrule"]
    for row in rows:
        lines.append(row if isinstance(row, str) else " & ".join(row) + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    (FIGS / "replication_table.tex").write_text("\n".join(lines) + "\n")


def pooled_table() -> None:
    """figs/pooled_table.tex (appendix A18): headline estimates of the exploratory pooled re-run (all 54,579 papers,
    output_pooled/) next to the discovery record (output/). Estimates only; about 80% of each pooled sample is
    discovery papers, so the pooled column confirms nothing."""
    def est(base: Path) -> dict[str, float]:
        rq1 = pd.read_csv(base / "rq1_results.csv")
        rq2 = pd.read_csv(base / "frozen_run" / "rq2_results.csv")
        rq2 = rq2[rq2.kind == "main"].set_index("hypothesis")
        h3a = json.loads((base / "frozen_run" / "summary.json").read_text())["rq3"]["verdicts"]["H3a"]
        ex = pd.read_csv(base / "frozen_run" / "exploratory_estimates.csv")
        ph = base / "posthoc"
        kw = pd.read_csv(ph / "ph4_keywords.csv").set_index("unit")
        tp = pd.read_csv(ph / "ph4_topics.csv").set_index("unit")
        prem = pd.read_csv(ph / "ph5_premia" / "tests.csv")
        return {
            "H1d": rq1[(rq1.hypothesis == "H1d") & (rq1.variant == "main")].iloc[0].coef,
            "H2b": rq2.loc["H2b"].coef, "H2c": rq2.loc["H2c"].coef, "H3a": h3a["coef"],
            "H3a_p": h3a["p"], "H3a_holm": h3a["p_holm"],
            "E8": ex[ex.analysis == "E8"].iloc[0].coef,
            "FLk": kw.loc["federated learning"].level, "FLt": tp.loc["m029 Federated learning"].level,
            "FLt_q": tp.loc["m029 Federated learning"].level_q,
            "E1": pd.read_csv(ph / "ph5_pivot" / "tests.csv").set_index("test").loc["E1"].coef,
            "P1b": pd.read_csv(ph / "ph5_position" / "tests.csv").set_index("test").loc["P1b"].coef,
            "H1": pd.read_csv(ph / "ph5_teams" / "family.csv").set_index("test").loc["H1"].estimate,
            "A1": pd.read_csv(ph / "ph5_kwtiming" / "tests.csv").set_index("test").loc["A1"].coef,
            "b": prem[(prem.unit_type == "early") & (prem.test == "b")].iloc[0].estimate,
        }

    d, q = est(OUTPUT), est(POOLED_OUTPUT)
    rows = [("H1d", "H1d: new architectures $\\sim$ prior FM adoption", "pp, 0 $\\to$ 100\\% FM"),
            ("H2b", "H2b: method papers $\\sim$ newcomer paper", "pp"),
            ("H2c", "H2c: benchmark/eval.\\ papers $\\sim$ newcomer paper", "pp"),
            ("H3a", "H3a: acceptance $\\sim$ topic maturity", "pp per log unit"),
            ("E8", "E8: acceptance, new arch.\\ $\\times$ prior FM adoption", "pp, 0 $\\to$ 100\\% FM"),
            ("FL", "PH4 federated-learning gap: keyword / topic", "pp"),
            ("E1", "PH5 E1 far jump from own record (p10 vs.\\ median)", "pp"),
            ("P1b", "PH5 P1b least-novel fifth vs.\\ middle fifth", "pp"),
            ("H1", "PH5 teams H1 one topic insider vs.\\ none", "pp"),
            ("A1", "PH5 A1 Emerging vs.\\ Mainstream keyword", "pp"),
            ("b", "PH5 premia $b$, topic edges 2024--26 on 2018--22 (early map)", "slope $b$")]
    lines = [r"% generated by make_figures.pooled_table(); do not edit by hand",
             r"\begin{tabular}{@{}llrr@{}}", r"\toprule",
             r"Association & Unit & Discovery & Pooled \\", r"\midrule"]
    for key, label, unit in rows:
        if key == "FL":
            dv, qv = f"{_pp(d['FLk'])} / {_pp(d['FLt'])}", f"{_pp(q['FLk'])} / {_pp(q['FLt'])}"
        elif key == "b":
            dv, qv = f"{d['b']:.2f}", f"{q['b']:.2f}"
        else:
            dv, qv = _pp(d[key]), _pp(q[key])
        lines.append(f"{label} & {unit} & {dv} & {qv} \\\\")
        if key == "H2c":
            lines.append(r"\addlinespace")
    lines += [r"\bottomrule", r"\end{tabular}"]
    (FIGS / "pooled_table.tex").write_text("\n".join(lines) + "\n")
    print(f"pooled H3a p {q['H3a_p']:.3f} Holm {q['H3a_holm']:.3f}; pooled FL topic q {q['FLt_q']:.3f}")


if __name__ == "__main__":
    FIGS.mkdir(exist_ok=True)
    for make in (hindsight, emerging, lifecycle, fm_trend, newcomers, newcomer_gap, area_ranking, fl_story, team_size,
                 far_jump, premia_scatter, replication_table, pooled_table):
        make()
    print("figures written to", FIGS)
