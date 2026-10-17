"""Figures for the research-fashion guide (discovery dry-run frame; held-out frame if present).

fig_fashion_map.png  (a) P(accept) and (b) P(top-10% cited | accepted) by local size x momentum tercile,
                     (c) P(hit) by team entry status x momentum tercile.
fig_fashion_quadrant.png  reviewers vs readers: relative effect of each lever on P(accept) (x) and on
                     P(top-10% | accepted) (y), joint LPM with year FE, 2022-25, SEs clustered by topic100.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C

OUT = C.OUT / "fashion"
LEVELS = ["lo", "mid", "hi"]
LEVERS = {"size_p": "established area", "mom_p": "rising area", "nnr_p": "close to a predecessor",
          "ins": "insider team", "ent": "entrant team", "G1_name": "NAME: subtitle",
          "G2_assertive": "title states finding", "G6b_tentative": "Towards / Rethinking",
          "G4_llm_words": "LLM-favoured words"}
OFFSET = {"size_p": (5, -9), "mom_p": (5, 3), "nnr_p": (5, 3), "ins": (-8, 6), "ent": (-30, -11), "G1_name": (-62, 4),
          "G2_assertive": (5, 4), "G6b_tentative": (5, 3), "G4_llm_words": (5, -9)}


def heat(ax, d, outcome, title, fmt="{:.0%}"):
    t = d[d[outcome].notna()].groupby(["size3", "mom3"], observed=True)[outcome].mean().unstack().reindex(index=LEVELS[::-1], columns=LEVELS)
    im = ax.imshow(t.to_numpy(), cmap="Blues", vmin=0, vmax=t.to_numpy().max() * 1.15)
    for i in range(3):
        for j in range(3):
            v = t.iloc[i, j]
            ax.text(j, i, fmt.format(v), ha="center", va="center", fontsize=8, color="white" if v > t.to_numpy().max() * 0.7 else C.TEXT)
    ax.set_xticks(range(3), ["falling", "flat", "rising"])
    ax.set_yticks(range(3), ["large", "medium", "small"])
    ax.set_xlabel("momentum (t−2 → t−1)")
    ax.set_ylabel("size (t−1)")
    ax.set_title(title, loc="left")
    ax.grid(False)


def fig_map(d, tag):
    fig, axs = C.new_fig("double", 2.5, ncols=3)
    heat(axs[0], d, "acc_rev", "a  Reviewers: P(accept)")
    heat(axs[1], d, "top10", "b  Readers: P(top-10% | accepted)")
    ax = axs[2]
    e = d[d.year.between(2022, 2025) & d.hit.notna() & d.entry.notna() & d.mom3.notna()]
    g = e.groupby(["entry", "mom3"], observed=True).hit.agg(["mean", "size"]).reset_index()
    for k, ent in enumerate(["newcomer", "entrant", "insider"]):
        gg = g[g.entry == ent].set_index("mom3").reindex(LEVELS)
        se = np.sqrt(gg["mean"] * (1 - gg["mean"]) / gg["size"])
        x = np.arange(3) + (k - 1) * 0.26
        ax.bar(x, gg["mean"], 0.25, yerr=1.96 * se, color=C.color(k), label=ent, error_kw=dict(lw=0.6, ecolor=C.TEXT2))
    ax.set_xticks(range(3), ["falling", "flat", "rising"])
    ax.set_xlabel("momentum (t−2 → t−1)")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_title("c  P(accepted & top-10%), 2022–25", loc="left")
    ax.legend(title="team", loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT / f"fig_fashion_map{tag}.png")
    fig.savefig(OUT / f"fig_fashion_map{tag}.pdf")


def fig_quadrant(d, tag):
    g = d[d.year.between(2022, 2025)].copy()
    for c in ["G2_assertive", "G6b_tentative", "G4_llm_words"]:
        if c not in g:
            return
    rhs = " + ".join(LEVERS) + " + log_authors + lprior_acc"
    est = {}
    for o in ["acc_rev", "top10"]:
        dd = g[g[o].notna() & g.mom_p.notna() & g.nnr_p.notna() & g.entry.notna()]
        t = pf.feols(f"{o} ~ {rhs} | year", data=dd, vcov={"CRV1": "topic100"}).tidy()
        base = dd[o].mean()
        est[o] = (t.loc[list(LEVERS), "Estimate"] / base, t.loc[list(LEVERS), "Std. Error"] / base)
    fig, ax = C.new_fig(4.2, 3.4)
    x, xs = est["acc_rev"]
    y, ys = est["top10"]
    ax.axhline(0, color=C.GREY, lw=0.6)
    ax.axvline(0, color=C.GREY, lw=0.6)
    for k in LEVERS:
        ax.errorbar(x[k], y[k], xerr=1.96 * xs[k], yerr=1.96 * ys[k], fmt="o", color=C.color(0), ms=3.5, lw=0.6)
        ax.annotate(LEVERS[k], (x[k], y[k]), fontsize=6.5, xytext=OFFSET[k], textcoords="offset points", color=C.TEXT)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:+.0%}")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:+.0%}")
    ax.set_xlabel("reviewers: relative change in P(accept)")
    ax.set_ylabel("readers: relative change in P(top-10% | accepted)")
    ax.set_title("Each lever's effect, joint model, 2022–25 (95% CI)", loc="left")
    fig.savefig(OUT / f"fig_fashion_quadrant{tag}.png")
    fig.savefig(OUT / f"fig_fashion_quadrant{tag}.pdf")
    return {k: {"acc_rel": float(x[k]), "acc_rel_se": float(xs[k]), "top10_rel": float(y[k]), "top10_rel_se": float(ys[k])} for k in LEVERS}


def main(argv):
    tag = argv[0] if argv else ""
    d = pd.read_parquet(OUT / ("heldout_frame.parquet" if tag == "_heldout" else "dryrun_frame.parquet"))
    if "G2_assertive" not in d:
        fr = pd.read_parquet(OUT / "frame.parquet")[["submission_id", "G2_assertive", "G6b_tentative", "G4_llm_words"]]
        d = d.merge(fr, on="submission_id", how="left")
    fig_map(d, tag)
    q = fig_quadrant(d, tag)
    if q:
        import json
        (OUT / f"quadrant{tag}.json").write_text(json.dumps(q, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
