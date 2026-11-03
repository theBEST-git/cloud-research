"""Paper figures. None reads an outcome or decision column: Figure 1 uses outcome-free keywords; Figures 2-4 read
outcome-free labels and committed result files only (hindsight check, registered and post hoc estimates, the held-out
run's estimates).

  fig1_waves   share of discovery submissions listing each author keyword, 2018-2026 (peak marked)
  fig2_field   (a) emerging / declining topics on k = 100 maps fitted on different years; (b) FM vs new-architecture share
  fig3_entry   (a) newcomer minus incumbent papers (contribution type, twins) and first-time teams' Emerging keywords;
               (b) first-time teams' FM-paper gap by the topic's prior FM adoption
  fig4_gate    (a) adjusted acceptance by fifth of closeness to the team's own record; (b) the gate tests by reference point

    python research/fashion/paper/make_figures.py      -> research/fashion/paper/figs/fig{1,2,3,4}_*.{pdf,png}
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import json  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from common import CORPUS, OUTPUT, POOLED_OUTPUT, TOPICS, topic_layer  # noqa: E402

assert CORPUS == "discovery", "run with ICLR_CORPUS unset: the figures show the discovery split"
FIGS = HERE / "figs"
BLUE, ORANGE, INK, INK2, MUTED, GRID, SHADE = "#2a78d6", "#eb6834", "#0b0b0b", "#3a3a38", "#7a7974", "#e4e3df", "#efefed"
CONF = POOLED_OUTPUT / "confirmation_run"                        # the single held-out run (committed estimates)
YEARS = np.arange(2018, 2027)
WAVES = [("generative adversarial networks", "GANs"), ("adversarial attack", "Adversarial attacks"),
         ("meta-learning", "Meta-learning"), ("graph neural networks", "Graph neural nets"),
         ("federated learning", "Federated learning"), ("self-supervised learning", "Self-supervised"),
         ("diffusion models", "Diffusion models"), ("large language models", "Large language models")]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2, "axes.linewidth": 0.8,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True,
                     "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "axes.spines.top": False,
                     "axes.spines.right": False})


def shares() -> dict[str, np.ndarray]:
    c = topic_layer().embedded_corpus()
    c = c[c.year.between(YEARS[0], YEARS[-1])]
    total = c.groupby("year").size().reindex(YEARS).to_numpy(float)
    return {kw: 100 * c[c.keywords.apply(lambda s, kw=kw: kw in s)].groupby("year").size()
            .reindex(YEARS, fill_value=0).to_numpy(float) / total for kw, _ in WAVES}


def waves() -> None:
    sh = shares()
    fig, axes = plt.subplots(2, 4, figsize=(7.0, 3.0), sharex=True)
    for ax, (kw, label) in zip(axes.ravel(), WAVES):
        y = sh[kw]
        i = int(np.argmax(y))
        ax.fill_between(YEARS, y, color=BLUE, alpha=0.15, lw=0)
        ax.plot(YEARS, y, color=BLUE, lw=1.8)
        ax.plot(YEARS[i], y[i], "o", color=BLUE, ms=4)
        ha = "left" if i <= 1 else "right" if i == len(YEARS) - 1 else "center"
        ax.annotate(f"{y[i]:.1f}% ({YEARS[i]})", (YEARS[i], y[i]), xytext=(0, 4), textcoords="offset points", ha=ha,
                    va="bottom", fontsize=7, color=INK)
        ax.set_ylim(0, y.max() * 1.35)
        ax.set_title(label, fontsize=8.5, color=INK, loc="left")
        ax.set_xticks([2018, 2022, 2026], ["'18", "'22", "'26"])
        ax.tick_params(labelsize=7.5, length=2)
        ax.yaxis.set_major_locator(plt.MaxNLocator(3))
    for ax in axes[:, 0]:
        ax.set_ylabel("% of subm.", fontsize=8)
    fig.tight_layout(w_pad=0.6, h_pad=0.8)
    FIGS.mkdir(exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"fig1_waves.{ext}", dpi=220, bbox_inches="tight")
    plt.close(fig)
    for kw, label in WAVES:
        y = sh[kw]
        print(f"{label}: peak {y.max():.1f}% ({YEARS[np.argmax(y)]}), 2026 {y[-1]:.1f}%")


def save(fig, name: str) -> None:
    FIGS.mkdir(exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"{name}.{ext}", dpi=220, bbox_inches="tight")
    plt.close(fig)


def row(df: pd.DataFrame, **match) -> pd.Series:
    m = np.ones(len(df), bool)
    for k, v in match.items():
        m &= (df[k] == v).to_numpy()
    assert m.sum() == 1, (match, m.sum())
    return df[m].iloc[0]


def field() -> None:
    """Figure 2: (a) emerging and declining topics by map; (b) FM and new-architecture shares with the H1d estimates."""
    maps = json.loads((TOPICS / "hindsight_check.json").read_text())["maps"]
    order = [("pooled", "all years"), ("seed_refit", "all years (refit)"), ("late", "2024\u201326"),
             ("balanced", "year-balanced"), ("middle", "2021\u201323"), ("early", "2017\u201320")]
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz", usecols=["year", "primary_type", "foundation_model"])
    by = lab.groupby("year").agg(fm=("foundation_model", lambda x: (x == "yes").mean()),
                                 arch=("primary_type", lambda x: (x == "model").mean())) * 100
    rq1 = row(pd.read_csv(OUTPUT / "rq1_results.csv"), hypothesis="H1d", variant="main")
    held = row(pd.read_csv(CONF / "h1d.csv"), hypothesis="H1d", variant="main")
    fig, (a, b) = plt.subplots(2, 1, figsize=(3.3, 4.3), gridspec_kw={"height_ratios": [1.05, 1]})
    y = np.arange(len(order))[::-1]
    em = [maps[k]["emerging_topics"] for k, _ in order]
    de = [maps[k]["declining_topics"] for k, _ in order]
    sh = [maps[k]["late_paper_share_in_emerging"] for k, _ in order]
    a.barh(y, em, color=BLUE, height=0.62, label="emerging")
    a.plot(de, y, "D", color=MUTED, ms=4, label="declining")
    for yi, e, dv, v in zip(y, em, de, sh):
        a.text(max(e, dv) + 1.2, yi, f"{e}  ({100 * v:.0f}%)", va="center", fontsize=7, color=INK)
    a.set_yticks(y, [lbl for _, lbl in order], fontsize=7.5)
    a.set_xlim(0, 40)
    a.set_xlabel("Topics (of 100)", fontsize=8)
    a.set_title("(a) Map fitted on \u2026", fontsize=8.5, loc="left", color=INK)
    a.grid(axis="y", visible=False)
    a.legend(fontsize=6.5, frameon=False, loc="lower right", handletextpad=0.3, borderaxespad=0.2)
    yrs = by.index.to_numpy()
    b.plot(yrs, by.fm, color=BLUE, lw=1.8, marker="o", ms=3)
    b.plot(yrs, by.arch, color=ORANGE, lw=1.8, marker="s", ms=3)
    b.text(2023.6, 30, "builds on a\nfoundation model", color=BLUE, fontsize=7, ha="right")
    b.text(2018.6, 19.5, "proposes a new architecture", color=ORANGE, fontsize=7)
    b.text(2026.2, by.fm.iloc[-1], f"{by.fm.iloc[-1]:.0f}%", fontsize=7, va="center", color=INK)
    b.text(2026.2, by.arch.iloc[-1], f"{by.arch.iloc[-1]:.0f}%", fontsize=7, va="center", color=INK)
    ci = (100 * (rq1.coef - 1.96 * rq1.se), 100 * (rq1.coef + 1.96 * rq1.se))
    b.text(2017.0, 58, "H1d, 0\u2192100% prior FM adoption:\n"
           f"discovery {100 * rq1.coef:.1f} [{ci[0]:.1f}, {ci[1]:.1f}]\n"
           f"held-out {100 * held.coef:.1f} [{100 * held.ci95_lo:.1f}, {100 * held.ci95_hi:.1f}] (A)",
           fontsize=6.5, color=INK2, va="top", ha="left",
           bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GRID, lw=0.6))
    b.set_xlim(2016.6, 2027.3)
    b.set_ylim(0, 60)
    b.set_xticks(range(2017, 2027, 3))
    b.set_ylabel("% of submissions", fontsize=8)
    b.set_title("(b) The package shift", fontsize=8.5, loc="left", color=INK)
    fig.tight_layout(h_pad=1.0)
    save(fig, "fig2_field")


def shaded_rows(ax, ys, predicted, lim) -> None:
    """Grey band on the side of zero that the herding prediction expected, one per row."""
    for yi, sgn in zip(ys, predicted):
        lo, hi = (0, lim[1]) if sgn > 0 else (lim[0], 0)
        ax.fill_between([lo, hi], yi - 0.42, yi + 0.42, color=SHADE, lw=0, zorder=0)


def dot(ax, y, est, lo, hi, colour, marker, filled=True) -> None:
    ax.plot([lo, hi], [y, y], color=colour, lw=1.4, zorder=2)
    ax.plot(est, y, marker, color=colour, ms=4.5, mfc=colour if filled else "white", mew=1.2, zorder=3)


def entry() -> None:
    """Figure 3: (a) entry contrasts with the herding-predicted side shaded; (b) first-time teams' FM-paper gap."""
    rq2 = pd.read_csv(OUTPUT / "frozen_run" / "rq2_results.csv")
    held = pd.read_csv(CONF / "rq2_rows.csv")
    herd = pd.read_csv(OUTPUT / "posthoc" / "ph5_position" / "free_herding.csv")
    prof = pd.read_csv(OUTPUT / "posthoc" / "ph5_kwtiming" / "free_profile_states.csv")
    fe = pd.read_csv(OUTPUT / "posthoc" / "ph5_fmwave" / "free_entry.csv")
    rows = [("Method paper", row(rq2, hypothesis="H2b", variant="main"), row(held, hypothesis="H2b", variant="main"), -1, "A"),
            ("Benchmark, dataset or\nevaluation paper", row(rq2, hypothesis="H2c", variant="main"),
             row(held, hypothesis="H2c", variant="main"), +1, "A"),
            ("Has a same-year twin", row(herd, term="newcomer"), None, +1, "E"),
            ("First-time vs returning team:\nEmerging keyword", row(prof, state="young_rising"), None, +1, "E")]
    fig, (a, b) = plt.subplots(2, 1, figsize=(3.3, 4.2), gridspec_kw={"height_ratios": [1.1, 1]})
    ys = [3.2, 2.2, 1.2, 0.0]
    lim = (-6.5, 6.5)
    shaded_rows(a, ys, [r[3] for r in rows], lim)
    for yi, (label, d, h, _, tier) in zip(ys, rows):
        dot(a, yi + (0.12 if h is not None else 0), 100 * d.coef, 100 * d.ci95_lo, 100 * d.ci95_hi, BLUE, "o")
        if h is not None:
            dot(a, yi - 0.12, 100 * h.coef, 100 * h.ci95_lo, 100 * h.ci95_hi, ORANGE, "s")
        a.text(lim[1] + 0.3, yi, tier, va="center", fontsize=7.5, color=INK)
    a.axhline(0.6, color=GRID, lw=0.8)
    a.axvline(0, color=INK2, lw=0.9)
    a.set_yticks(ys, [r[0] for r in rows], fontsize=7)
    a.set_xlim(*lim)
    a.set_ylim(-0.6, 3.75)
    a.set_xlabel("Newcomer minus incumbent paper (pp)", fontsize=7.5)
    a.grid(axis="y", visible=False)
    a.plot([], [], "o", color=BLUE, ms=4.5, label="discovery")
    a.plot([], [], "s", color=ORANGE, ms=4.5, label="held-out")
    a.fill_between([], [], color=SHADE, label="herding predicted")
    a.legend(fontsize=6.5, frameon=False, loc="lower left", ncol=3, bbox_to_anchor=(-0.02, 1.0), handletextpad=0.3,
             columnspacing=0.8)
    a.set_title("(a)", fontsize=8.5, loc="left", color=INK, pad=14)
    bins = ["0-5%", "5-15%", "15-30%", "30-50%", ">=50%"]
    x = np.arange(len(bins))
    for off, (term, label, colour, marker) in zip((-0.12, 0.12), [
            ("first_time (vs returning topic newcomer)", "first-time team vs returning newcomer", BLUE, "o"),
            ("topic newcomer (vs incumbent)", "returning newcomer vs incumbent", MUTED, "^")]):
        part = fe[fe.term == term].set_index("bin").reindex(bins)
        b.errorbar(x + off, 100 * part.coef, yerr=[100 * (part.coef - part.ci95_lo), 100 * (part.ci95_hi - part.coef)],
                   fmt=marker, color=colour, ms=4, lw=1.2, capsize=0, label=label)
    b.axhline(0, color=INK2, lw=0.9)
    b.set_xticks(x, ["0\u20135", "5\u201315", "15\u201330", "30\u201350", "\u226550"], fontsize=6.5, rotation=25)
    b.set_xlabel("Topic's prior-year FM adoption (%)", fontsize=7.5)
    b.set_ylabel("Gap in FM-paper share (pp)", fontsize=7.5)
    b.legend(fontsize=6.5, frameon=False, loc="lower left", bbox_to_anchor=(0.06, 1.0), ncol=1, handletextpad=0.3)
    b.set_title("(b)", fontsize=8.5, loc="left", color=INK, pad=22)
    b.set_xlim(-0.5, len(bins) - 0.5)
    b.grid(axis="x", visible=False)
    fig.tight_layout(h_pad=1.2)
    save(fig, "fig3_entry")


def gate() -> None:
    """Figure 4: (a) adjusted acceptance by fifth of F_max; (b) gate tests grouped by reference point."""
    q = pd.read_csv(OUTPUT / "posthoc" / "ph5_pivot" / "quintiles.csv")
    q = q[q.model == "P1 F_max quintiles (adjusted P(accept))"]
    held = pd.read_csv(CONF / "ph5" / "tests.csv")
    piv = pd.read_csv(OUTPUT / "posthoc" / "ph5_pivot" / "tests.csv")
    teams = pd.read_csv(OUTPUT / "posthoc" / "ph5_teams" / "family.csv")
    pos = pd.read_csv(OUTPUT / "posthoc" / "ph5_position" / "tests.csv")
    rq3 = row(pd.read_csv(OUTPUT / "frozen_run" / "rq3_results.csv"), hypothesis="H3a", variant="main")
    rq3h = row(pd.read_csv(CONF / "rq3_rows.csv"), hypothesis="H3a", variant="main")
    e1h = row(held, test="E1")
    tests = [  # label, unit note, discovery (coef, lo, hi), held-out, verdict
        ("Far jump (p10 \u2212 median)", row(piv, test="E1"), e1h, "supported"),
        ("Same author, +0.1 cosine", row(piv, test="E4"), row(held, test="E4"), "supported"),
        ("One topic insider vs none", row(teams, test="H1").rename({"estimate": "coef"}), row(held, test="H1"), "supported"),
        ("Crowding, per log unit", rq3, rq3h, "uninformative"),
        ("Least-distant fifth vs middle", row(pos, test="P1b"), row(held, test="P1b"), "uninformative"),
        ("Same author, +10 pct of distance", row(pos, test="P7"), row(held, test="P7"), "not supported")]
    fig = plt.figure(figsize=(3.3, 5.2))
    top = fig.add_gridspec(1, 1, left=0.15, right=0.97, top=0.95, bottom=0.62)
    a = fig.add_subplot(top[0])
    x = np.arange(1, 6)
    a.errorbar(x, 100 * q.coef, yerr=[100 * (q.coef - q.ci95_lo), 100 * (q.ci95_hi - q.coef)], fmt="o-", color=BLUE,
               ms=4, lw=1.4, capsize=0)
    for xi, v in zip(x, 100 * q.coef):
        a.text(xi + 0.12, v + 1.0, f"{v:.1f}", ha="left", fontsize=6.5, color=INK)
    a.set_xticks(x, ["1\nfar", "2", "3", "4", "5\nnear"], fontsize=7)
    a.set_xlim(0.6, 5.6)
    a.set_ylabel("Adjusted acceptance (%)", fontsize=7.5)
    a.set_ylim(36, 52)
    a.text(0.97, 0.05, f"held-out far jump: {100 * e1h.coef:.1f} [{100 * e1h.ci95_lo:.1f}, {100 * e1h.ci95_hi:.1f}] (B)",
           transform=a.transAxes, ha="right", fontsize=6.5, color=ORANGE)
    a.set_title("(a) Closeness to the team's own earlier work, by fifth", fontsize=8, loc="left", color=INK)
    rows = fig.add_gridspec(8, 1, left=0.43, right=0.76, top=0.50, bottom=0.03,
                            height_ratios=[0.55, 1, 1, 1, 0.55, 1, 1, 1], hspace=0.55)
    for i, txt in [(0, "(b) Referenced to a record"), (4, "Referenced to others or the field")]:
        ax = fig.add_subplot(rows[i])
        ax.axis("off")
        ax.text(-1.25, 0.0, txt, fontsize=7.5, color=INK, transform=ax.transAxes, va="bottom")
    for slot, (label, d, h, verdict) in zip([1, 2, 3, 5, 6, 7], tests):
        ax = fig.add_subplot(rows[slot])
        vals = [100 * d.coef, 100 * d.ci95_lo, 100 * d.ci95_hi, 100 * h.coef, 100 * h.ci95_lo, 100 * h.ci95_hi]
        m = max(abs(v) for v in vals) * 1.15
        dot(ax, 0.3, vals[0], vals[1], vals[2], BLUE, "o")
        dot(ax, -0.3, vals[3], vals[4], vals[5], ORANGE, "s")
        ax.axvline(0, color=INK2, lw=0.8)
        ax.set_xlim(-m, m)
        ax.set_ylim(-0.8, 0.8)
        ax.set_yticks([])
        ax.tick_params(axis="x", labelsize=5.5, length=2, pad=1)
        ax.grid(False)
        ax.spines["left"].set_visible(False)
        ax.text(-0.04, 0.5, label, transform=ax.transAxes, ha="right", va="center", fontsize=6.5, color=INK)
        ax.text(1.04, 0.5, verdict, transform=ax.transAxes, ha="left", va="center", fontsize=6.5,
                color=INK if verdict == "supported" else MUTED)
    save(fig, "fig4_gate")


if __name__ == "__main__":
    waves()
    field()
    entry()
    gate()
