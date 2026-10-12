"""Paper-side figure revisions for the Naming Turn module (review round 1).

Run from research/titles/src:  OMP_NUM_THREADS=2 python ../paper/figures/make_paper_figures.py

This script does NOT modify src/analyses/figures.py (which is hashed in the pre-registration bundle)
and writes nothing under outputs/. It imports the analysis figure module, redirects its output folder to
paper/figures/, and applies the label/colour/annotation changes requested in review (R3, R4, R6, R16):
  fig1  dashed line relabelled "Logit-linear 2017-23 trend"                       (R3, R16)
  fig2  rebuilt: additive fixed-window Shapley bar on top; DFL for 2024/25/26     (R6, R16)
  fig3  panel a uses a hue distinct from panel b's "title style" blue             (R16)
  fig4  panel a shows each control pair separately, via/using dashed              (R4, R16)
  fig5  "Compound (any colon)" relabelled "Compound (colon or dash)"              (R16)
  fig6  truncated CI of the ITS slope-change row printed in panel a               (R16)
Every plotted number is read from the same output files the analysis figures read.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / "src"
sys.path.insert(0, str(SRC))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.colors as mcolors  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from analyses import figures as F  # noqa: E402
from analyses import _core as C  # noqa: E402

F.FIG_DIR = HERE            # redirect every save() to paper/figures/
_orig_save = F.save
HOOKS = {}


def hooked_save(fig, name, data):
    if name in HOOKS:
        HOOKS[name](fig)
    return _orig_save(fig, name, data)


F.save = hooked_save


def replace_text(fig, mapping):
    for t in fig.findobj(matplotlib.text.Text):
        s = t.get_text()
        for a, b in mapping.items():
            if a in s:
                t.set_text(s.replace(a, b))
                s = t.get_text()


# ---------------------------------------------------------------- fig1
def _fig1_hook(fig):
    replace_text(fig, {"2017–23 trend, extrapolated": "Logit-linear 2017–23 trend"})


HOOKS["fig1_naming_turn"] = _fig1_hook


# ---------------------------------------------------------------- fig2 (rebuilt)
def fig2():
    r1 = F.rj(F.D1 / "results.json")
    sh = r1["H1b"]["shares"]
    shap = F.rc(F.D1 / "shapley_table.csv").set_index("target_year").loc[2026]
    dfl = r1["H1d"]["dfl_full_by_year"]
    tb = F.rc(F.D1 / "T1_3_tool_bound.csv")
    tb = tb[np.isclose(tb["A_max"], 0.39)].set_index("spec")
    tool_c = r1["H1e"]["tool_share_0.39_corrected_2026"]
    tool_n = r1["H1e"]["tool_share_0.39_naive_preregistered"]
    dN = r1["H1e"]["tool"]["dNAME_2023_2026"]

    def row(lbl, est, lo, hi, grp):
        return {"group": grp, "label": lbl, "share": est, "lo95": lo, "hi95": hi}

    G1, G2, G3, G4, G5 = ("Content, fixed window", "Content, rolling", "Composition",
                          "LLM drafting (A = 0.39)", "Unexplained")
    rows = [row("R1 masked TF-IDF", sh["R1|fixed"]["share"], *sh["R1|fixed"]["ci"], G1),
            row("R3 masked bge", sh["R3|fixed"]["share"], *sh["R3|fixed"]["ci"], G1),
            row("R5 R1 minus moves", sh["R5|fixed"]["share"], *sh["R5|fixed"]["ci"], G1),
            row("Shapley (additive)", shap["shapley_content"], shap["shapley_content_lo"],
                shap["shapley_content_hi"], G1),
            row("R1 masked TF-IDF", sh["R1|rolling"]["share"], *sh["R1|rolling"]["ci"], G2),
            row("R3 masked bge", sh["R3|rolling"]["share"], *sh["R3|rolling"]["ci"], G2),
            row("R5 R1 minus moves", sh["R5|rolling"]["share"], *sh["R5|rolling"]["ci"], G2)]
    for y in ("2024", "2025", "2026"):
        rows.append(row(f"DFL reweighting ({y})", dfl[y]["share"], *dfl[y]["ci"], G3))
    rows += [row("Shapley (additive)", shap["shapley_composition"], shap["shapley_composition_lo"],
                 shap["shapley_composition_hi"], G3),
             row("Pre-registered formula", tool_n["share"], tool_n["lo"], tool_n["hi"], G4),
             row("Misclassif.-corrected", tool_c["share"], tool_c["lo"], tool_c["hi"], G4)]
    for spec, lbl in (("F_any x post DiD, 2021-26 (selection-corrected)", "Any fingerprint, DiD"),
                      ("title typography only", "Title typography only")):
        t = tb.loc[spec]
        rows.append(row(lbl, t["tool_share"], t["tool_share_lo"], t["tool_share_hi"], G4))
    rows.append(row("Shapley residual (additive)", shap["residual_unexplained"], shap["residual_lo"],
                    shap["residual_hi"], G5))
    df = pd.DataFrame(rows)
    pred = {G1: (0.20, 0.50), G2: (0.20, 0.50), G3: (0.0, 0.30), G4: (0.0, 0.25)}

    F.style()
    fig = plt.figure(figsize=(3.35, 5.7))
    # ---- top: the one additive split
    tx = fig.add_axes([0.06, 0.885, 0.90, 0.045])
    parts = [("Content", shap["shapley_content"], F.AQUA), ("Comp.", shap["shapley_composition"], F.ORANGE),
             ("Unexplained", shap["residual_unexplained"], F.YELLOW)]
    left = 0.0
    for lbl, v, col in parts:
        tx.barh(0, v, left=left, color=col, edgecolor="white", height=0.9)
        tx.text(left + v / 2, 0, f"{lbl} {v:.2f}" if v > 0.15 else f"{v:.2f}", ha="center", va="center",
                fontsize=F.FS, color=F.TEXT)
        left += v
    tx.set_xlim(0, 1.0)
    tx.set_ylim(-0.5, 0.5)
    tx.axis("off")
    fig.text(0.06, 0.945, "a  Additive split, fixed window (Shapley, sums to 1)", fontsize=9, color=F.TEXT,
             fontweight="bold")
    fig.text(0.42, 0.862, "composition", fontsize=F.FS, color=F.TEXT2, ha="center")
    # ---- bottom: every estimator (not additive)
    ax = fig.add_axes([0.40, 0.155, 0.575, 0.655])
    fig.text(0.06, 0.835, "b  Estimates by design (not additive)", fontsize=9, color=F.TEXT, fontweight="bold")
    ypos, labels, y, heads = [], [], 0.0, []
    for g, sub in df.groupby("group", sort=False):
        heads.append((y, g))
        y -= 1.0
        g_top = y + 0.45
        for _, r in sub.iterrows():
            ypos.append(y)
            labels.append(r["label"])
            y -= 1.0
        g_bot = y + 0.55
        if g in pred:
            lo_, hi_ = pred[g]
            ax.fill_betweenx([g_bot, g_top], lo_, hi_, color=F.BAND_GREY, alpha=0.55, lw=0, zorder=0)
        y -= 0.35
    for yy, (_, r) in zip(ypos, df.iterrows()):
        F.dot_ci(ax, yy, r["share"], r["lo95"], r["hi95"], F.BLUE)
    for yy, g in heads:
        ax.text(-0.02, yy, g, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8.5,
                color=F.TEXT, fontweight="bold")
    ax.set_yticks(ypos, labels)
    F.hide_y_grid(ax)
    ax.set_ylim(y + 0.6, 0.6)
    ax.set_xlim(-0.02, 0.72)
    ax.set_xticks([0, 0.2, 0.4, 0.6], ["0", "20", "40", "60"])
    ax.axvline(0, color=F.TEXT2, lw=0.6, zorder=1)
    ax.set_xlabel(f"Share of the 2023→26 NAME rise\n(%; Δ = {dN * 100:.1f} pp)")
    ax.spines["left"].set_visible(False)
    ax.legend([Line2D([], [], color=F.BLUE, lw=1.6, marker="o", ms=5.5, mec="white"),
               Patch(color=F.BAND_GREY, alpha=0.55, lw=0)],
              ["Estimate (95% CI)", "Pre-specified range"], loc="upper center", frameon=False,
              bbox_to_anchor=(0.36, -0.145), ncol=2, columnspacing=0.8, handlelength=1.4, handletextpad=0.4)
    _orig_save(fig, "fig2_decomposition", df)


# ---------------------------------------------------------------- fig3
NEW_A = C.COLORS[6]   # violet for panel a; panel b keeps blue = title style


def _fig3_hook(fig):
    replace_text(fig, {"No newcomer keys": "Grouped by key newness"})
    ax = fig.axes[0]
    for ln in ax.lines:
        if mcolors.same_color(ln.get_color(), F.BLUE):
            ln.set_color(NEW_A)
            if ln.get_marker() not in (None, "None", ""):
                ln.set_markerfacecolor(NEW_A)
    leg = ax.get_legend()
    if leg is not None:
        for h in getattr(leg, "legend_handles", getattr(leg, "legendHandles", [])):
            if isinstance(h, Line2D) and mcolors.same_color(h.get_color(), F.BLUE):
                h.set_color(NEW_A)
                h.set_markerfacecolor(NEW_A)


HOOKS["fig3_carriers"] = _fig3_hook


# ---------------------------------------------------------------- fig4 (panel a rebuilt)
def fig4():
    ss = F.rc(F.D3 / "fig_F3_1_slot_shares.csv")
    sy = F.rc(F.D3 / "slot_shares_by_year.csv")
    fpv = F.rc(F.D3 / "fingerprint_prevalence_by_year.csv").set_index("year")
    sig = F.rc(F.D3 / "fig_F3_4_signature.csv")
    sm = F.rc(F.D3 / "signature_models.csv")

    F.style()
    fig = plt.figure(figsize=(7.0, 3.55))
    ax = fig.add_axes([0.075, 0.40, 0.215, 0.51])
    bx = fig.add_axes([0.375, 0.40, 0.175, 0.51])
    cx = fig.add_axes([0.655, 0.40, 0.155, 0.51])
    yrs = list(range(2018, 2027))
    sl = ss[ss["slot"] == "pooled_slots"].sort_values("year")
    ax.fill_between(sl["year"], sl["lo"] * 100, sl["hi"] * 100, color=F.BLUE, alpha=0.18, lw=0, zorder=1)
    ax.plot(sl["year"], sl["share"] * 100, color=F.BLUE, lw=2, marker="o", ms=5, mec="white", mew=0.8, zorder=4)
    ctrl = [("towards", "towards (vs toward)", C.COLORS[6], "-", "s"),
            ("novel", "novel (vs new)", C.COLORS[4], "-", "^"),
            ("via", "via (vs using)", F.GREY, (0, (3, 1.5)), "s")]
    rowsA = [sl.assign(series="pooled LLM slots")]
    for k, lbl, col, ls, mk in ctrl:
        d = sy[(sy["slot"] == k) & (sy["year"] >= 2018)].sort_values("year")
        ax.plot(d["year"], d["share"] * 100, color=col, lw=1.6, ls=ls, marker=mk, ms=4, mec="white", mew=0.6,
                zorder=3)
        rowsA.append(d.assign(series=lbl))
    ax.axvline(2023.5, color=F.GREY, lw=0.8, ls=":", zorder=1)
    ax.set_ylim(0, 100)
    ax.set_xlim(2017.6, 2026.4)
    ax.set_xticks(yrs, [f"’{y % 100:02d}" if y % 2 == 0 else "" for y in yrs])
    ax.set_ylabel("Share of slot-filled titles (%)")
    ax.set_xlabel("ICLR year")
    F.panel_title(ax, "a", "Meaning-fixed slots")

    yb = [y for y in fpv.index if y >= 2021]
    n24 = F._n24_rates(yb)
    fam = (("r24_any", F.ORANGE, "-", "o", "R24 (enhanc*, leverag*, …)"),
           ("n24", F.GREY, (0, (3, 1.5)), "s", "Neutral (improv*, utili[sz]*, …)"),
           ("r26_any", F.AQUA, "-", "o", "R26 (unified, beyond, …)"))
    rates = {"r24_any": fpv.loc[yb, "r24_any"] * 1000, "r26_any": fpv.loc[yb, "r26_any"] * 1000,
             "n24": n24.loc[yb] * 1000}
    for k, col, ls, mk_, lbl in fam:
        bx.plot(yb, rates[k].to_numpy(), color=col, lw=2, ls=ls, marker=mk_, ms=4.6, mec="white", mew=0.8)
    bx.axvline(2023.5, color=F.GREY, lw=0.8, ls=":", zorder=1)
    bx.set_xticks(yb, [f"’{y % 100:02d}" for y in yb])
    bx.set_xlim(2020.6, 2026.4)
    bx.set_ylim(0, 75)
    bx.set_ylabel("Titles per 1,000")
    bx.set_xlabel("ICLR year")
    F.panel_title(bx, "b", "Title word families")

    rows = ["2024-26 pooled", "2024", "2025", "2026", "NA pool", "F_d1"]
    disp = {"2024-26 pooled": "2024–26", "NA pool": "NA pool", "F_d1": "D1 fingerprint"}
    fd1 = sm[(sm["x"] == "F_d1") & (sm["controls"] == "none")].iloc[0]
    recs = []
    for rw in rows[:-1]:
        for outc, key in (("LLM slot variant | slot filled", "slot"), ("NAME title (all papers)", "name_pop")):
            r = sig[(sig["row"] == rw) & (sig["outcome"] == outc)].iloc[0]
            recs.append(dict(row=rw, outcome=key, OR=r["OR"], lo=r["lo"], hi=r["hi"], ratio_pop=r["ratio_pop"],
                             ratio_pop_lo=r["ratio_pop_lo"], ratio_pop_hi=r["ratio_pop_hi"]))
    for key, a_, l_, h_ in (("slot", "OR_slot", "OR_slot_lo", "OR_slot_hi"),
                            ("name_pop", "OR_name_pop", "OR_name_pop_lo", "OR_name_pop_hi")):
        recs.append(dict(row="F_d1", outcome=key, OR=fd1[a_], lo=fd1[l_], hi=fd1[h_], ratio_pop=fd1["ratio_pop"],
                         ratio_pop_lo=fd1["ratio_pop_lo"], ratio_pop_hi=fd1["ratio_pop_hi"]))
    sigc = pd.DataFrame(recs)
    for i, rw in enumerate(rows):
        yy = len(rows) - 1 - i
        for dy, key, col in ((0.16, "slot", F.BLUE), (-0.16, "name_pop", F.GREY)):
            r = sigc[(sigc["row"] == rw) & (sigc["outcome"] == key)].iloc[0]
            F.dot_ci(cx, yy + dy, r["OR"], r["lo"], r["hi"], col, ms=5, lw=1.4)
        r = sigc[sigc["row"] == rw].iloc[0]
        cx.text(1.06, yy, f"{r['ratio_pop']:.2f} [{r['ratio_pop_lo']:.2f}, {r['ratio_pop_hi']:.2f}]",
                transform=cx.get_yaxis_transform(), fontsize=F.FS, color=F.TEXT, va="center", ha="left")
    cx.text(1.06, len(rows) - 0.25, "ratio slot/NAME", transform=cx.get_yaxis_transform(), fontsize=F.FS,
            color=F.TEXT2, va="center", ha="left")
    cx.axhline(0.5, color=F.GRID, lw=0.8, zorder=0)
    cx.axvline(1, color=F.GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    cx.set_xscale("log")
    cx.set_xlim(0.6, 3.2)
    cx.set_xticks([0.7, 1, 1.5, 2, 3], ["0.7", "1", "1.5", "2", "3"])
    cx.minorticks_off()
    cx.set_yticks(range(len(rows) - 1, -1, -1), [disp.get(r, r) for r in rows])
    F.hide_y_grid(cx)
    cx.set_ylim(-0.6, len(rows) + 0.1)
    cx.set_xlabel("OR of fingerprinted abstract (log)")
    F.panel_title(cx, "c", "Lexical vs structural")

    hs = [Line2D([], [], color=F.BLUE, lw=2, marker="o", ms=5, mec="white")]
    ls_ = ["a: LLM-favoured verb (slots)"]
    for k, lbl, col, ls, mk in ctrl:
        hs.append(Line2D([], [], color=col, lw=1.6, ls=ls, marker=mk, ms=4, mec="white"))
        ls_.append("a: control " + lbl)
    for k, col, ls, mk_, lbl in fam:
        hs.append(Line2D([], [], color=col, lw=2, ls=ls, marker=mk_, ms=4.6, mec="white"))
        ls_.append("b: " + lbl)
    blank = Line2D([], [], lw=0)
    hs += [blank, Line2D([], [], color=F.BLUE, lw=1.4, marker="o", ms=5, mec="white"),
           Line2D([], [], color=F.GREY, lw=1.4, marker="o", ms=5, mec="white"), blank]
    ls_ += ["", "c: LLM slot variant | slot filled", "c: NAME title, all papers", ""]
    fig.legend(hs, ls_, loc="lower center", bbox_to_anchor=(0.5, -0.01), ncol=3, frameon=False,
               handlelength=1.8, columnspacing=1.4)
    _orig_save(fig, "fig4_register", {"a_slot_and_control_shares": pd.concat(rowsA),
                                      "b_word_family_rates": pd.DataFrame({"year": yb, **{k: v.to_numpy() for k, v
                                                                                           in rates.items()}}),
                                      "c_signature_population": sigc})


# ---------------------------------------------------------------- fig5
F.FEAT_LABEL["compound"] = "Compound (colon or dash)"


# ---------------------------------------------------------------- fig6
def _fig6_hook(fig):
    ax = fig.axes[0]
    labs = [t.get_text() for t in ax.get_yticklabels()]
    ys = ax.get_yticks()
    for lab, y in zip(labs, ys):
        if lab.startswith("2024 slope change"):
            ax.text(0.54, y + 0.40, "95% CI [−0.15, 1.16]", fontsize=F.FS - 1, color=F.TEXT2, ha="left",
                    va="center")


HOOKS["fig6_published_bias"] = _fig6_hook


def main():
    caps = {"fig1": F.fig1(), "fig3": F.fig3(), "fig5": F.fig5(), "fig6": F.fig6()}
    fig2()
    fig4()
    print("written:", sorted(p.name for p in HERE.glob("fig*.pdf")))
    # check the hard-coded CI text against the source
    at = F.rc(F.D4 / "atlas.csv")
    its = at[at["label"].astype(str).str.startswith("ITS slope change")].iloc[0]
    print("ITS row CI in atlas.csv:", round(its["ratio_lo95"], 2), round(its["ratio_hi95"], 2))
    return caps


if __name__ == "__main__":
    main()
