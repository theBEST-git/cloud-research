"""Minimal-text figures for the Notion findings page (findings 1-4).

Reads final outputs only (universe/features parquet, acceptance table, D2/D3 figure data) and writes
PNGs to outputs/notion/. Style follows the study's figure rules: white background, one y-axis,
fixed categorical colours, recessive grid, direct labels.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from . import _core as core

OUT = core.OUT / "notion"
PAPER_FIG = core.STUDY / "paper" / "figures"
BLUE, ORANGE, AQUA, GREY, INK, INK2, GRID = "#2a78d6", "#eb6834", "#1baf7a", "#8a8984", "#0b0b0b", "#52514e", "#e6e5e1"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": INK2, "axes.labelcolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
})


def load() -> pd.DataFrame:
    u = pd.read_parquet(core.OUT / "core" / "universe.parquet")
    f = pd.read_parquet(core.OUT / "features" / "features_v2.parquet")
    return u.merge(f[["submission_id", "name_primary", "F_any"]], on="submission_id")


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig1_no_payoff(d: pd.DataFrame):
    years = sorted(d.year.unique())
    allp = d.groupby("year").name_primary.mean() * 100
    acc = d[d.ACC].groupby("year").name_primary.mean() * 100
    rng = np.random.default_rng(0)
    ratio, lo, hi = [], [], []
    ryears = [y for y in years if y >= 2018]
    for y in ryears:
        g = d[d.year == y]
        a = g.name_primary.to_numpy(float); m = g.ACC.to_numpy(bool)
        r = a[m].mean() / a.mean()
        boots = []
        for _ in range(500):
            i = rng.integers(0, len(g), len(g))
            aa, mm = a[i], m[i]
            boots.append(aa[mm].mean() / aa.mean())
        ratio.append(r); lo.append(np.percentile(boots, 2.5)); hi.append(np.percentile(boots, 97.5))
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw={"width_ratios": [1.25, 1]})
    ax[0].plot(years, allp.values, color=BLUE, lw=2, marker="o", ms=5, label="All submissions")
    ax[0].plot(years, acc.reindex(years).values, color=ORANGE, lw=2, marker="s", ms=5, ls="--", label="Accepted papers")
    ax[0].set_title("Branded titles quadrupled")
    ax[0].set_ylabel("NAME: subtitle titles (%)"); ax[0].set_ylim(0, 45)
    ax[0].annotate(f"{allp.iloc[0]:.0f}%", (years[0], allp.iloc[0]), xytext=(0, -16), textcoords="offset points", ha="center", color=INK2)
    ax[0].annotate(f"{allp.iloc[-1]:.0f}%", (years[-1], allp.iloc[-1]), xytext=(-4, 8), textcoords="offset points", ha="right", color=INK2)
    ax[0].legend(frameon=False, loc="upper left")
    ax[1].axhline(1, color=GREY, lw=1, ls="--")
    ax[1].errorbar(ryears, ratio, yerr=[np.array(ratio) - lo, np.array(hi) - ratio], fmt="o", color=BLUE, ms=6, capsize=0, lw=1.5)
    ax[1].set_title("…but accepted papers carry them at the same rate")
    ax[1].set_ylabel("NAME share: accepted ÷ all"); ax[1].set_ylim(0.7, 1.3)
    ax[1].text(2017.8, 0.73, "1.0 = same rate as all submissions", color=INK2, fontsize=9)
    for a, ys in [(ax[0], years), (ax[1], ryears)]:
        a.set_xticks(ys); a.set_xticklabels([f"'{str(y)[2:]}" for y in ys])
    save(fig, "finding1_no_payoff")


def fig2_style_vs_topic():
    g = pd.read_csv(PAPER_FIG / "fig3_carriers__b_style_topic_G.csv")
    parts = [("first", "First author"), ("any", "All positions"), ("last", "Last author")]
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    x = np.arange(len(parts)); w = 0.36
    for k, (ch, col, lab) in enumerate([("topic", AQUA, "Research topic"), ("style", ORANGE, "Title style")]):
        sub = g[g.channel == ch].set_index("partition").loc[[p for p, _ in parts]]
        ax.bar(x + (k - 0.5) * w, sub.G * 100, w * 0.92, color=col, label=lab)
        ax.errorbar(x + (k - 0.5) * w, sub.G * 100, yerr=[(sub.G - sub.lo95) * 100, (sub.hi95 - sub.G) * 100], fmt="none", ecolor=INK2, lw=1.2)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels([l for _, l in parts])
    ax.set_ylabel("Returning authors lag the field (%)")
    ax.set_title("Returning authors keep up with topics, lag on title style")
    ax.text(0.62, 44, "0 = keeps pace with the field", color=INK2, fontsize=9)
    ax.legend(frameon=False, loc="upper right")
    save(fig, "finding2_style_vs_topic")


def fig3_words_not_structure(d: pd.DataFrame):
    s = pd.read_csv(PAPER_FIG / "fig4_register__a_slot_and_control_shares.csv")
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
    llm = s[s.series == "pooled LLM slots"]
    ax[0].plot(llm.year, llm.share * 100, color=BLUE, lw=2.2, marker="o", ms=5)
    ax[0].fill_between(llm.year, llm.lo * 100, llm.hi * 100, color=BLUE, alpha=0.12, lw=0)
    ax[0].text(2026.15, llm.share.iloc[-1] * 100, "LLM-favoured verb\n(Enhancing, Unveiling…)", color=BLUE, va="center", fontsize=9)
    for ser, lab in [("towards (vs toward)", "Towards vs Toward"), ("novel (vs new)", "novel vs new"), ("via (vs using)", "via vs using")]:
        c = s[s.series == ser]
        ax[0].plot(c.year, c.share * 100, color=GREY, lw=1.4, ls="--")
        ax[0].text(2026.15, c.share.iloc[-1] * 100, lab, color=GREY, va="center", fontsize=8.5)
    ax[0].axvline(2023.5, color=GREY, lw=0.8, ls=":")
    ax[0].set_title("Same meaning, new word: LLM verbs jump after 2023")
    ax[0].set_ylabel("Share choosing the first word (%)"); ax[0].set_ylim(0, 100); ax[0].set_xlim(2017.7, 2026.3)
    years = sorted(y for y in d.year.unique() if y >= 2023)
    for flag, col, lab, ls, mk in [(1, ORANGE, "Abstract has LLM-style fingerprint", "--", "s"), (0, BLUE, "No fingerprint", "-", "o")]:
        v = d[(d.F_any == flag) & d.year.isin(years)].groupby("year").name_primary.mean() * 100
        ax[1].plot(v.index, v.values, color=col, lw=2, ls=ls, marker=mk, ms=5, label=lab)
    ax[1].set_title("Branding rises with or without LLM fingerprints")
    ax[1].set_ylabel("NAME: subtitle titles (%)"); ax[1].set_ylim(0, 45)
    ax[1].legend(frameon=False, loc="upper left")
    for a, ys in [(ax[0], range(2018, 2027)), (ax[1], years)]:
        a.set_xticks(list(ys)); a.set_xticklabels([f"'{str(y)[2:]}" for y in ys])
    fig.tight_layout()
    save(fig, "finding3_words_not_structure")


def fig4_published_only(d: pd.DataFrame):
    years = sorted(y for y in d.year.unique() if y >= 2018)
    wd = d[d.year >= 2018].groupby("year").WD.mean() * 100
    a = pd.read_csv(core.OUT / "acceptance" / "feature_associations.csv").set_index("feature").loc["name_primary"]
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw={"width_ratios": [1.1, 1]})
    ax[0].bar(years, wd.values, color=BLUE, width=0.7)
    for y, v in zip(years, wd.values):
        if y in (2018, 2026):
            ax[0].text(y, v + 0.8, f"{v:.0f}%", ha="center", color=INK2, fontsize=9)
    ax[0].set_title("A quarter of submissions now withdraw")
    ax[0].set_ylabel("Withdrawn (% of submissions)"); ax[0].set_ylim(0, 32)
    ax[0].set_xticks(years); ax[0].set_xticklabels([f"'{str(y)[2:]}" for y in years])
    rows = [("Acceptance, decided papers only", "OR_adj", ORANGE), ("Acceptance, all submissions", "OR_all_adj", BLUE), ("Withdrawal", "OR_withdraw_adj", GREY)]
    for i, (lab, k, col) in enumerate(rows):
        ax[1].errorbar(a[k], i, xerr=[[a[k] - a[k + "_lo"]], [a[k + "_hi"] - a[k]]], fmt="o", color=col, ms=8, lw=2)
        ax[1].text(a[k + "_hi"] + 0.01, i, f"{a[k]:.2f}", va="center", color=INK2, fontsize=9)
    ax[1].axvline(1, color=GREY, lw=1, ls="--")
    ax[1].set_yticks(range(3)); ax[1].set_yticklabels([r[0] for r in rows]); ax[1].invert_yaxis()
    ax[1].set_xlim(0.9, 1.2); ax[1].set_xlabel("Odds ratio, NAME vs not (adjusted)")
    ax[1].set_title("Decided-only view inflates branding's payoff")
    ax[1].grid(axis="y", visible=False)
    fig.tight_layout()
    save(fig, "finding4_published_only")


def main():
    d = load()
    fig1_no_payoff(d)
    fig2_style_vs_topic()
    fig3_words_not_structure(d)
    fig4_published_only(d)


if __name__ == "__main__":
    main()
