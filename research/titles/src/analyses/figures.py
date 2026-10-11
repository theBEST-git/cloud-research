"""WP10: main-paper figures (6) and tables (4), regenerated from the D1-D4 and snapshot outputs.

Run from research/titles/src:
    OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.figures

Reads only finished outputs (never refits a model):
    outputs/d1_break/   (WP5)   outputs/d2_carriers/ (WP6)   outputs/d3_register/ (WP7)
    outputs/d4_filter/  (WP8)   outputs/snapshot/    (WP4)
Writes
    outputs/figures/fig{1..6}_*.{pdf,png,csv}   (paper style via analyses._core.save_fig)
    outputs/tables/table{1..4}_*.{csv,tex}       (booktabs; needs \\usepackage{booktabs})
    outputs/figures/manifest.json                captions, source files and their mtimes

Every number in a caption is read from the source files at run time, so captions stay in sync
when an upstream work package is re-run. Language follows the README boundaries: declared profile
keys are not persons, list position is only a partition label, acceptance associations are
associational and subject to the camera-ready caveat.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from analyses import _core as C  # noqa: E402

OUT = C.OUT
D1, D2, D3, D4, SNAP = (OUT / "d1_break", OUT / "d2_carriers", OUT / "d3_register",
                        OUT / "d4_filter", OUT / "snapshot")
FIG_DIR, TAB_DIR = OUT / "figures", OUT / "tables"

BLUE, ORANGE, AQUA, YELLOW = C.COLORS[0], C.COLORS[1], C.COLORS[2], C.COLORS[3]
GREY, TEXT, TEXT2, GRID = C.GREY, C.TEXT, C.TEXT2, C.GRID
BAND_GREY = "#d9d8d4"   # light fill for reference bands (a tint of the control grey)
FS = 8                  # smallest font size used anywhere (style: 8-9 pt)

_INPUTS: dict[str, str] = {}


# ----------------------------------------------------------------------------------------------
# I/O helpers
# ----------------------------------------------------------------------------------------------
def _track(p: Path) -> Path:
    p = Path(p)
    if not p.exists():
        raise FileNotFoundError(f"missing upstream output: {p}")
    _INPUTS[str(p.relative_to(OUT))] = _dt.datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds")
    return p


def rj(p: Path) -> dict:
    return json.loads(_track(p).read_text())


def rc(p: Path, **kw) -> pd.DataFrame:
    return pd.read_csv(_track(p), **kw)


def hyp(d: dict, hid: str) -> dict:
    """Hypothesis entry from a results.json whose 'hypotheses' is a list or a dict."""
    H = d["hypotheses"]
    if isinstance(H, dict):
        return H[hid]
    return next(h for h in H if h.get("id") == hid)


# ----------------------------------------------------------------------------------------------
# Number formatting
# ----------------------------------------------------------------------------------------------
def fnum(x, d: int = 2, signed: bool = False) -> str:
    if x is None:
        return "n/a"
    try:
        x = float(x)
    except (TypeError, ValueError):
        return str(x)
    if not np.isfinite(x):
        return "n/a"
    s = f"{x:+.{d}f}" if signed else f"{x:.{d}f}"
    return s.replace("-0." + "0" * d, "0." + "0" * d) if not signed else s


def fci(est, lo, hi, d: int = 2, signed: bool = False, pct: bool = False) -> str:
    k = 100.0 if pct else 1.0
    f = (lambda v: fnum(None if v is None else float(v) * k, d, signed))
    return f"{f(est)} [{f(lo)}, {f(hi)}]"


def fp(p) -> str:
    if p is None or (isinstance(p, float) and not np.isfinite(p)):
        return "n/a"
    p = float(p)
    if p < 0.001:
        return "<0.001"
    return f"{p:.3f}" if p < 0.1 else f"{p:.2f}"


# ----------------------------------------------------------------------------------------------
# Plot helpers
# ----------------------------------------------------------------------------------------------
def style():
    C.set_style()
    plt.rcParams.update({"font.size": 8.5, "axes.labelsize": 8.5, "axes.titlesize": 9,
                         "xtick.labelsize": FS, "ytick.labelsize": FS, "legend.fontsize": FS,
                         "legend.handlelength": 1.8, "legend.borderaxespad": 0.3,
                         "axes.titlelocation": "left", "axes.titlepad": 6})


def panel_title(ax, letter: str, title: str):
    ax.set_title(f"$\\bf{{{letter}}}$  {title}", fontsize=9, loc="left", color=TEXT)


def dot_ci(ax, y, est, lo, hi, color, marker="o", ms=5.5, lw=1.6, mfc=None, zorder=3, label=None):
    ax.plot([lo, hi], [y, y], color=color, lw=lw, solid_capstyle="butt", zorder=zorder)
    ax.plot([est], [y], marker=marker, ms=ms, color=color, mfc=mfc or color, mec="white" if mfc is None else color,
            mew=0.8 if mfc is None else 1.3, lw=0, zorder=zorder + 1, label=label)


def hide_y_grid(ax):
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)


WIDTHS: dict[str, float] = {}


def save(fig, name: str, data) -> dict:
    """Save via the shared helper; record the tight-bbox size so column widths can be checked."""
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    WIDTHS[name] = (round(bb.width, 2), round(bb.height, 2), round(bb.x0, 2), round(bb.x1, 2))
    nominal = C.SINGLE_W if fig.get_figwidth() <= C.SINGLE_W + 1e-6 else C.DOUBLE_W
    if bb.width > nominal + 0.02:
        print(f"[warn] {name}: rendered width {bb.width:.2f} in exceeds the {nominal} in column width")
    return C.save_fig(fig, name, FIG_DIR, data=data)


# ----------------------------------------------------------------------------------------------
# LaTeX booktabs writer
# ----------------------------------------------------------------------------------------------
_TEX_SPECIAL = [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\^{}")]
_TEX_UNICODE = {"×": r"$\times$", "→": r"$\rightarrow$", "≥": r"$\geq$", "≤": r"$\leq$", "ρ": r"$\rho$",
                "δ": r"$\delta$", "Δ": r"$\Delta$", "±": r"$\pm$", "−": "-", "–": "--", "—": "---",
                "≈": r"$\approx$", "*": r"$^{*}$", "Ĝ": "G", "≠": r"$\neq$", "·": r"$\cdot$",
                ">": r"$>$", "<": r"$<$", "|": r"$|$"}


def tex_escape(s) -> str:
    s = "" if s is None else str(s)
    for a, b in _TEX_SPECIAL:
        if a == "\\":
            s = s.replace(a, "\x00")
        else:
            s = s.replace(a, b)
    s = s.replace("\x00", r"\textbackslash{}")
    s = re.sub(r"(?<![\w.])-(?=\d)", r"$-$", s)   # numeric minus signs
    for a, b in _TEX_UNICODE.items():
        s = s.replace(a, b)
    return s


def write_table(df: pd.DataFrame, name: str, caption: str, label: str, colspec: str,
                group_col: str | None = None, notes: str | None = None, star: bool = True,
                size: str = r"\footnotesize") -> dict:
    """Write <name>.csv (all columns) and <name>.tex (booktabs; group_col rows become italic headers)."""
    TAB_DIR.mkdir(parents=True, exist_ok=True)
    csv_p = TAB_DIR / f"{name}.csv"
    df.to_csv(csv_p, index=False)
    cols = [c for c in df.columns if c != group_col]
    env = "table*" if star else "table"
    lines = [f"% generated by analyses/figures.py on {_dt.date.today().isoformat()}; requires \\usepackage{{booktabs}}",
             f"\\begin{{{env}}}[t]", "\\centering", size, f"\\caption{{{tex_escape(caption)}}}",
             f"\\label{{{label}}}", f"\\begin{{tabular}}{{{colspec}}}", "\\toprule",
             " & ".join(tex_escape(c) for c in cols) + r" \\", "\\midrule"]
    prev = None
    for i, row in df.iterrows():
        if group_col is not None and row[group_col] != prev:
            if prev is not None:
                lines.append("\\addlinespace")
            lines.append(f"\\multicolumn{{{len(cols)}}}{{l}}{{\\textit{{{tex_escape(row[group_col])}}}}} \\\\")
            prev = row[group_col]
        lines.append(" & ".join(tex_escape(row[c]) for c in cols) + r" \\")
    lines += ["\\bottomrule", "\\end{tabular}"]
    if notes:
        lines += ["\\par\\smallskip", f"\\parbox{{\\linewidth}}{{\\scriptsize {tex_escape(notes)}}}"]
    lines.append(f"\\end{{{env}}}")
    tex_p = TAB_DIR / f"{name}.tex"
    tex_p.write_text("\n".join(lines) + "\n")
    return {"csv": csv_p, "tex": tex_p}


# ==============================================================================================
# Figure 1: the naming turn (D1 H1a-H1c)
# ==============================================================================================
def fig1() -> str:
    obs = rc(D1 / "fig_F1_1_counterfactual__observed.csv").set_index("year")
    fx = rc(D1 / "cf_fixed_paths.csv")
    rl = rc(D1 / "cf_rolling_steps.csv")
    dev = rc(D1 / "its_year_deviation.csv")
    steps = rc(D1 / "fig_F1_2_steps.csv").set_index("year")
    r1 = rj(D1 / "results.json")
    masked = ["R1", "R3", "R5"]

    fxu = fx[(fx["pop"] == "U") & (fx["outcome"] == "primary") & fx["rep"].isin(masked)]
    # sanity: the observed series used here equals the one the content models were evaluated on
    chk = fxu[(fxu["design"] == "fixed") & (fxu["rep"] == "R1")].set_index("year")["obs"]
    assert np.allclose(chk.values, obs.loc[chk.index, "observed_U"].values), "observed series mismatch"

    yrs = list(range(2017, 2027))
    oU = obs.loc[yrs, "observed_U"] * 100
    oN = obs.loc[yrs, "observed_NApool"] * 100

    # content counterfactual paths: fixed window (train 2021-23) and rolling one-step (cumulative content steps)
    o23 = obs.loc[2023, "observed_U"]
    paths = {}
    for rep in masked:
        f = fxu[(fxu["design"] == "fixed") & (fxu["rep"] == rep)].set_index("year")["p_hat"]
        paths[f"{rep}|fixed"] = pd.Series({2023: o23, **f.to_dict()})
        s = rl[(rl["pop"] == "U") & (rl["outcome"] == "primary") & (rl["rep"] == rep)].set_index("year")["content_step"]
        cum = o23 + s.loc[[2024, 2025, 2026]].cumsum()
        paths[f"{rep}|rolling"] = pd.Series({2023: o23, **cum.to_dict()})
    post = pd.DataFrame(paths).loc[[2023, 2024, 2025, 2026]] * 100
    # placebo window (train 2018-20, predict 2021-23), anchored at observed 2020
    o20 = obs.loc[2020, "observed_U"]
    plac = {}
    for rep in masked:
        f = fxu[(fxu["design"] == "placebo") & (fxu["rep"] == rep)].set_index("year")["p_hat"]
        plac[rep] = pd.Series({2020: o20, **f.to_dict()})
    plac = pd.DataFrame(plac).loc[[2020, 2021, 2022, 2023]] * 100

    # 2017-23 trend extrapolated (covariate-adjusted ITS pre-trend), CI from the year-deviation CI
    dU = dev[dev["population"] == "U"].set_index("year")
    tr_years = [2023, 2024, 2025, 2026]
    tr = [o23 * 100] + list(dU.loc[[2024, 2025, 2026], "trend_pred_share"] * 100)
    tr_lo = [o23 * 100] + list(dU.loc[[2024, 2025, 2026], "obs_share"] * 100 - dU.loc[[2024, 2025, 2026], "dev_pp_hi"])
    tr_hi = [o23 * 100] + list(dU.loc[[2024, 2025, 2026], "obs_share"] * 100 - dU.loc[[2024, 2025, 2026], "dev_pp_lo"])

    style()
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 3.2), gridspec_kw={"width_ratios": [1.5, 1.0], "wspace": 0.28})

    # ---- panel a
    ax.axvline(2023.5, color=GREY, lw=0.8, ls=":", zorder=1)
    ax.text(2023.62, 1.0, "2024 cohort onward", ha="left", va="bottom", fontsize=FS, color=TEXT2)
    ax.fill_between(tr_years, tr_lo, tr_hi, color=BAND_GREY, alpha=0.55, lw=0, zorder=1)
    ax.plot(tr_years, tr, color=GREY, lw=2, ls=(0, (4, 2)), zorder=2)
    ax.fill_between(post.index, post.min(axis=1), post.max(axis=1), color=AQUA, alpha=0.28, lw=0, zorder=2)
    ax.fill_between(plac.index, plac.min(axis=1), plac.max(axis=1), color=AQUA, alpha=0.28, lw=0, zorder=2)
    ax.plot(post.index, post["R1|fixed"], color=AQUA, lw=2, ls=(0, (1.5, 1.2)), zorder=3)
    ax.plot(plac.index, plac["R1"], color=AQUA, lw=2, ls=(0, (1.5, 1.2)), zorder=3)
    ax.plot(yrs, oU, color=BLUE, lw=2, marker="o", ms=5, mec="white", mew=0.8, zorder=5)
    ax.plot(yrs, oN, color=ORANGE, lw=2, ls=(0, (2.2, 1.6)), marker="s", ms=5, mfc="white", mec=ORANGE, mew=1.2,
            zorder=6)
    ax.text(2021.6, 11.2, "placebo window\n(trained 2018–20)", ha="center", va="top", fontsize=FS, color=TEXT2)
    ax.text(2023.7, 17.6, "fixed window\n(trained 2021–23)", ha="left", va="top", fontsize=FS, color=TEXT2)
    # direct labels at the right end (values only; identity is in the legend)
    ax.text(2026.25, oU.loc[2026], f"{oU.loc[2026]:.1f}%", va="center", ha="left", fontsize=FS, color=TEXT)
    ax.text(2026.25, tr[-1] - 0.3, f"{tr[-1]:.1f}%", va="center", ha="left", fontsize=FS, color=TEXT2)
    ax.text(2026.25, post.loc[2026].mean(), f"{post.loc[2026].min():.0f}–{post.loc[2026].max():.0f}%",
            va="center", ha="left", fontsize=FS, color=TEXT2)
    ax.set_xlim(2016.6, 2027.3)
    ax.set_ylim(0, 45)
    ax.set_xticks(yrs, [f"’{y % 100:02d}" for y in yrs])
    ax.set_ylabel("NAME titles (% of submissions)")
    ax.spines["bottom"].set_bounds(2016.6, 2026.4)
    handles = [Line2D([], [], color=BLUE, lw=2, marker="o", ms=5, mec="white"),
               Line2D([], [], color=ORANGE, lw=2, ls=(0, (2.2, 1.6)), marker="s", ms=5, mfc="white", mec=ORANGE),
               (Patch(color=AQUA, alpha=0.28, lw=0), Line2D([], [], color=AQUA, lw=2, ls=(0, (1.5, 1.2)))),
               (Patch(color=BAND_GREY, alpha=0.55, lw=0), Line2D([], [], color=GREY, lw=2, ls=(0, (4, 2))))]
    labels = ["All submissions", "Camera-ready-free pool", "Content counterfactual", "2017–23 trend, extrapolated"]
    ax.legend(handles, labels, loc="upper left", frameon=False, handlelength=2.4, borderaxespad=0.1)
    panel_title(ax, "a", "NAME share of ICLR submissions")

    # ---- panel b: annual steps = content-predicted + unexplained
    sy = list(range(2019, 2027))
    cs = steps.loc[sy, "content_step"].values * 100
    us = steps.loc[sy, "unexplained"].values * 100
    tot = steps.loc[sy, "step"].values * 100
    w = 0.66
    for x, c, u in zip(sy, cs, us):
        pos, neg = 0.0, 0.0
        for v, col in ((c, AQUA), (u, YELLOW)):
            base = pos if v >= 0 else neg
            bx.bar(x, v, w, bottom=base, color=col, edgecolor="white", linewidth=0.8, zorder=2)
            if v >= 0:
                pos += v
            else:
                neg += v
    bx.plot(sy, tot, lw=0, marker="o", ms=5, color=BLUE, mec="white", mew=0.8, zorder=4)
    bx.axhline(0, color=TEXT2, lw=0.6, zorder=3)
    bx.axvline(2023.5, ymax=0.56, color=GREY, lw=0.8, ls=":", zorder=1)
    h1 = r1["H1c"]
    ad = h1["acceleration_decomposition"]
    txt = (f"Mean per year (pp),\n2019–23 → 2024–26\n"
           f"content  {ad['content_step_pre_mean'] * 100:.1f} → {ad['content_step_post_mean'] * 100:.1f}\n"
           f"unexplained  {h1['u_pre'] * 100:.1f} → {h1['u_post'] * 100:.1f}")
    bx.text(2018.55, 10.0, txt, ha="left", va="top", fontsize=FS, color=TEXT2, linespacing=1.35)
    bx.set_xlim(2018.4, 2026.6)
    bx.set_ylim(-1.6, 10.2)
    bx.set_xticks(sy, [f"’{y % 100:02d}" for y in sy])
    bx.set_ylabel("Change from previous year (pp)")
    bx.grid(axis="x", visible=False)
    hb = [Line2D([], [], lw=0, marker="o", ms=5, color=BLUE, mec="white"), Patch(color=AQUA), Patch(color=YELLOW)]
    bx.legend(hb, ["Observed", "Content", "Unexplained"], loc="upper center",
              bbox_to_anchor=(0.5, -0.13), ncol=3, frameon=False, handlelength=1.0, columnspacing=0.8,
              handletextpad=0.4)
    panel_title(bx, "b", "Annual change, split by a content model")

    data = {
        "a_observed": pd.DataFrame({"year": yrs, "NAME_pct_all": oU.values, "NAME_pct_NApool": oN.values}),
        "a_content_cf_post": post.reset_index(names="year"),
        "a_content_cf_placebo": plac.reset_index(names="year"),
        "a_trend_extrapolated": pd.DataFrame({"year": tr_years, "trend_pct": tr, "lo95": tr_lo, "hi95": tr_hi}),
        "b_steps": pd.DataFrame({"year": sy, "observed_step_pp": tot, "content_step_pp": cs, "unexplained_pp": us}),
    }
    save(fig, "fig1_naming_turn", data)

    # caption numbers
    a = r1["H1a"]
    ylU = a["year_level_U"]["OR"]
    ylNA = a["year_level_NA"]["OR"]
    yl2 = h1["year_level_two_stage"]
    b = r1["H1b"]["shares"]
    d26 = dU.loc[2026]
    return (f"NAME titles (coined name before a colon or spaced dash) rose from {oU.loc[2023]:.1f}% of ICLR submissions "
            f"in 2023 to {oU.loc[2026]:.1f}% in 2026 on a trend already running since 2017 (pre-trend OR "
            f"{a['pre_slope_OR_U']:.3f}/yr), and the camera-ready-free pool (rejected, withdrawn, desk-rejected; "
            f"{oN.loc[2026]:.1f}% in 2026) tracks all submissions. "
            f"(a) The 2024 slope change is OR {fci(*a['slope_change_OR_U'], d=3)}/yr at paper level but "
            f"{fci(*ylU, d=3)} with year-level inference (NA pool {fci(*ylNA, d=3)}); only 2026 departs from the "
            f"extrapolated 2017-23 trend (+{d26['dev_pp']:.1f} pp [{d26['dev_pp_lo']:.1f}, {d26['dev_pp_hi']:.1f}]). "
            f"Aqua: name-masked abstract content counterfactuals (dotted line R1 fixed window; ribbon = range over R1/R3/R5 "
            f"in the fixed and rolling designs), which explain "
            f"{min(b[f'{r}|{d}']['share'] for r in masked for d in ('fixed', 'rolling')):.2f}-"
            f"{max(b[f'{r}|{d}']['share'] for r in masked for d in ('fixed', 'rolling')):.2f} of the 2023-26 rise; "
            f"the placebo window "
            f"(trained 2018-20) already under-predicts 2021-23. "
            f"(b) Annual change split into the part predicted by a rolling R1 content model and the unexplained part u; "
            f"mean u rose by {h1['diff'] * 100:+.2f} pp (two-stage year-level 95% CI "
            f"[{yl2['diff_ci'][0] * 100:.2f}, {yl2['diff_ci'][1] * 100:.2f}]; year-label permutation p = "
            f"{h1['year_permutation']['p_perm_one_sided']:.2f}).")


# ==============================================================================================
# Figure 2: what accounts for the 2023->2026 rise (D1 H1b, H1d, H1e)
# ==============================================================================================
def fig2() -> str:
    r1 = rj(D1 / "results.json")
    sh = r1["H1b"]["shares"]
    shap = rc(D1 / "shapley_table.csv").set_index("target_year").loc[2026]
    dfl = r1["H1d"]["dfl_full_by_year"]["2026"]
    tb = rc(D1 / "T1_3_tool_bound.csv")
    tb = tb[np.isclose(tb["A_max"], 0.39)].set_index("spec")
    tool_c = r1["H1e"]["tool_share_0.39_corrected_2026"]
    tool_n = r1["H1e"]["tool_share_0.39_naive_preregistered"]
    dN = r1["H1e"]["tool"]["dNAME_2023_2026"]

    def row(lbl, est, lo, hi, grp):
        return {"group": grp, "label": lbl, "share": est, "lo95": lo, "hi95": hi}

    G1, G2, G3, G4, G5 = ("Content, fixed window", "Content, rolling", "Composition", "LLM drafting (A = 0.39)",
                          "Unexplained")
    rows = [row("R1 masked TF-IDF", sh["R1|fixed"]["share"], *sh["R1|fixed"]["ci"], G1),
            row("R3 masked bge", sh["R3|fixed"]["share"], *sh["R3|fixed"]["ci"], G1),
            row("R5 R1 minus moves", sh["R5|fixed"]["share"], *sh["R5|fixed"]["ci"], G1),
            row("R1 masked TF-IDF", sh["R1|rolling"]["share"], *sh["R1|rolling"]["ci"], G2),
            row("R3 masked bge", sh["R3|rolling"]["share"], *sh["R3|rolling"]["ci"], G2),
            row("R5 R1 minus moves", sh["R5|rolling"]["share"], *sh["R5|rolling"]["ci"], G2),
            row("DFL reweighting", dfl["share"], *dfl["ci"], G3),
            row("Shapley, net of content", shap["shapley_composition"], shap["shapley_composition_lo"],
                shap["shapley_composition_hi"], G3),
            row("Pre-registered formula", tool_n["share"], tool_n["lo"], tool_n["hi"], G4),
            row("Misclassif.-corrected", tool_c["share"], tool_c["lo"], tool_c["hi"], G4)]
    for spec, lbl in (("F_any x post DiD, 2021-26 (selection-corrected)", "Any fingerprint, DiD"),
                      ("title typography only", "Title typography only")):
        if spec in tb.index:
            t = tb.loc[spec]
            rows.append(row(lbl, t["tool_share"], t["tool_share_lo"], t["tool_share_hi"], G4))
    rows.append(row("Shapley residual", shap["residual_unexplained"], shap["residual_lo"], shap["residual_hi"], G5))
    df = pd.DataFrame(rows)
    pred = {G1: (0.20, 0.50), G2: (0.20, 0.50), G3: (0.0, 0.30), G4: (0.0, 0.25)}

    style()
    fig = plt.figure(figsize=(3.4, 4.45))
    ax = fig.add_axes([0.39, 0.17, 0.585, 0.80])
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
            ax.fill_betweenx([g_bot, g_top], lo_, hi_, color=BAND_GREY, alpha=0.55, lw=0, zorder=0)
        y -= 0.35
    for yy, (_, r) in zip(ypos, df.iterrows()):
        dot_ci(ax, yy, r["share"], r["lo95"], r["hi95"], BLUE)
    for yy, g in heads:
        ax.text(-0.02, yy, g, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8.5,
                color=TEXT, fontweight="bold")
    ax.set_yticks(ypos, labels)
    hide_y_grid(ax)
    ax.set_ylim(y + 0.6, 0.6)
    ax.set_xlim(-0.02, 0.72)
    ax.set_xticks([0, 0.2, 0.4, 0.6], ["0", "20", "40", "60"])
    ax.axvline(0, color=TEXT2, lw=0.6, zorder=1)
    ax.set_xlabel(f"Share of the 2023→26 NAME rise\n(%; Δ = {dN * 100:.1f} pp)")
    ax.spines["left"].set_visible(False)
    ax.legend([Line2D([], [], color=BLUE, lw=1.6, marker="o", ms=5.5, mec="white"),
               Patch(color=BAND_GREY, alpha=0.55, lw=0)],
              ["Estimate (95% CI)", "Pre-registered range"], loc="upper center", frameon=False,
              bbox_to_anchor=(0.36, -0.15), ncol=2, columnspacing=0.8, handlelength=1.4, handletextpad=0.4)
    save(fig, "fig2_decomposition", df)

    return (f"Shares of the 2023-26 rise in NAME titles (Δ = {dN * 100:.1f} pp) attributed to abstract content, "
            f"team composition and detectable LLM drafting; grey bands are the pre-registered predictions "
            f"(content 0.20-0.50, composition ≤ 0.30, tool < 0.25). Name-masked content explains "
            f"{min(sh[k]['share'] for k in ('R1|fixed', 'R3|fixed', 'R5|fixed')):.2f}-"
            f"{max(sh[k]['share'] for k in ('R1|fixed', 'R3|fixed', 'R5|fixed')):.2f} in the fixed window and "
            f"{min(sh[k]['share'] for k in ('R1|rolling', 'R3|rolling', 'R5|rolling')):.2f}-"
            f"{max(sh[k]['share'] for k in ('R1|rolling', 'R3|rolling', 'R5|rolling')):.2f} in the rolling design, so "
            f"'content is a minority' is not established. Team size x new keys x LLM topic explains "
            f"{dfl['share']:.2f} by DFL reweighting but {shap['shapley_composition']:.2f} net of content (Shapley). "
            f"Detectable LLM drafting at A_max = 0.39 accounts for {tool_c['share'] * 100:.1f}% "
            f"[{tool_c['lo'] * 100:.1f}, {tool_c['hi'] * 100:.1f}] after misclassification correction "
            f"({tool_n['share'] * 100:.1f}% by the pre-registered formula), but alternative fingerprints give up to "
            f"{df[df.group == G4]['share'].max() * 100:.0f}%, so the tool share is small for the abstract fingerprint, "
            f"not bounded in general. The Shapley residual (unexplained by content or composition) is "
            f"{fci(shap['residual_unexplained'], shap['residual_lo'], shap['residual_hi'])}. "
            f"Content and composition CIs: conditional paper bootstrap (models fixed), B = 2000; tool-share CIs "
            f"propagate the 95% CI of the fingerprint uplift δ.")


# ==============================================================================================
# Figure 3: who carries the change (D2)
# ==============================================================================================
def fig3() -> str:
    f22 = rc(D2 / "fig_F2_2_decomposition.csv")
    mkr = rj(D2 / "markers_results.json")
    mk = mkr["stats"]
    r2 = rj(D2 / "results.json")
    c = f22[f22["panel"] == "c_newcomer_free"].set_index("label")
    order = [  # (source label, display label, is_reference)
        ("All keys seen 2021-22 (E = 2023)", "All keys present in 2021–22", False),
        ("All-stayer teams", "All keys are stayer keys", False),
        ("Repeated stayer dyad, no entrant", "Repeated stayer pair, no entrant", False),
        ("Last=S, L without entrant key", "Last stayer, no entrant co-author", False),
        ("All keys seen in prior 2 years (E = 2023)", "All keys seen in prior 2 years", False),
        ("First and last both stayers", "First and last keys both stayers", False),
        ("Rolling all-prior teams (H2c(ii))", "All keys seen in any earlier year", False),
        ("All keys seen the year before", "All keys seen the year before", False),
        ("Last=S, all papers (ρ_last)", "Last stayer, all papers (ρ_last)", True),
        ("Last=S, L with entrant first author", "Last stayer, entrant first key", True),
    ]
    order = [o for o in order if o[0] in c.index]
    style()
    fig = plt.figure(figsize=(7.0, 3.3))
    ax = fig.add_axes([0.262, 0.27, 0.34, 0.62])
    bx = fig.add_axes([0.765, 0.27, 0.21, 0.62])
    n = len(order)
    rowsA = []
    for i, (src, lbl, ref) in enumerate(order):
        r = c.loc[src]
        yy = n - 1 - i
        dot_ci(ax, yy, r["est"], r["lo"], r["hi"], GREY if ref else BLUE)
        ax.text(1.66, yy, f"{int(r['n_L']):,}", ha="right", va="center", fontsize=FS, color=TEXT2)
        rowsA.append({"row": lbl, "reference": ref, "ratio": r["est"], "lo95": r["lo"], "hi95": r["hi"],
                      "n_E": r["n_E"], "n_L": r["n_L"]})
    ax.text(1.66, n - 0.45, "n (L)", ha="right", va="bottom", fontsize=FS, color=TEXT2)
    ax.axvline(0, color=TEXT2, lw=0.6, zorder=1)
    ax.axvline(1, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.set_yticks(range(n - 1, -1, -1), [o[1] for o in order])
    hide_y_grid(ax)
    ax.set_xlim(-0.5, 1.68)
    ax.set_ylim(-0.6, n + 0.15)
    ax.set_xticks([-0.5, 0, 0.5, 1.0, 1.5])
    ax.spines["bottom"].set_bounds(-0.5, 1.5)
    ax.set_xlabel("NAME change E→L relative to the population")
    ax.legend([Line2D([], [], color=BLUE, lw=1.6, marker="o", ms=5.5, mec="white"),
               Line2D([], [], color=GREY, lw=1.6, marker="o", ms=5.5, mec="white")],
              ["No newcomer keys", "Reference: stayer keys"], loc="upper center",
              bbox_to_anchor=(0.42, -0.25), ncol=2, frameon=False, columnspacing=1.0, handlelength=1.4)
    panel_title(ax, "a", "Change by how new the team's keys are")

    # ---- panel b: generational increment G by list position, style vs topic markers
    parts = [("last", "Last position"), ("any", "Any position"), ("first", "First position")]
    rowsB = []
    for i, (p, lbl) in enumerate(parts):
        yy = len(parts) - 1 - i
        for dy, ch, col in ((0.14, "style", BLUE), (-0.14, "topic", ORANGE)):
            s = mk[p][f"G_{ch}"]
            dot_ci(bx, yy + dy, s["est"], s["lo"], s["hi"], col)
            rowsB.append({"partition": p, "channel": ch, "G": s["est"], "lo95": s["lo"], "hi95": s["hi"]})
    bx.axvline(0, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    bx.set_yticks(range(len(parts) - 1, -1, -1), [p[1] for p in parts])
    hide_y_grid(bx)
    bx.set_ylim(-0.6, len(parts) - 0.4)
    bx.set_xlim(-0.2, 0.55)
    bx.set_xticks([-0.2, 0, 0.2, 0.4])
    bx.set_xlabel("Generational increment G")
    bx.legend([Line2D([], [], color=BLUE, lw=1.6, marker="o", ms=5.5, mec="white"),
               Line2D([], [], color=ORANGE, lw=1.6, marker="o", ms=5.5, mec="white")],
              [f"Title style ({mkr['n_style']})", f"Abstract topic ({mkr['n_topic']})"], loc="upper center",
              bbox_to_anchor=(0.2, -0.25), ncol=2, frameon=False, columnspacing=0.8, handlelength=1.4)
    panel_title(bx, "b", "Style vs topic markers")

    save(fig, "fig3_carriers", {"a_newcomer_free": pd.DataFrame(rowsA), "b_style_topic_G": pd.DataFrame(rowsB)})

    h2a, h2b, h2d = hyp(r2, "H2a"), hyp(r2, "H2b"), hyp(r2, "H2d")
    ra = h2a["estimate"]
    ga = mk["any"]
    allstay = c.loc["All-stayer teams"]
    roll = c.loc["Rolling all-prior teams (H2c(ii))"]
    ent = c.loc["Last=S, L with entrant first author"]
    son = r2["shared_outcome_null"]["main"]
    nulls = [son[p_][k_]["est"] for p_ in ("last", "any") for k_ in ("null_Nfirst", "null_NRfirst")]
    return (f"Who carries the NAME rise between E = 2022-23 and L = 2025-26 (declared profile keys; list position is a "
            f"partition label only). (a) NAME change on papers grouped by how new their keys are, as a ratio of the "
            f"population change (key-cluster bootstrap 95% CIs; right column: L-period papers). Papers whose keys are "
            f"all stayer keys changed {fnum(allstay['est'])} [{fnum(allstay['lo'])}, {fnum(allstay['hi'])}] times the "
            f"population change, papers whose keys all appeared in an earlier year {fnum(roll['est'])} "
            f"[{fnum(roll['lo'])}, {fnum(roll['hi'])}], and last-position stayer keys on papers with an entrant first "
            f"key {fnum(ent['est'])} [{fnum(ent['lo'])}, {fnum(ent['hi'])}]: the rise is graded by team newness. "
            f"The pooled stayer-to-population ratios (ρ_last {fnum(ra['rho_last']['est'], 3)}, ρ_any "
            f"{fnum(ra['rho_any']['est'], 3)}) are not identified as communal change, because a purely generational "
            f"world with the observed co-authorship would give {min(nulls):.2f}-{max(nulls):.2f}. (b) Generational increment G = 1 - slope of "
            f"within-stayer on population change across {mkr['n_style']} title style and "
            f"{mkr['n_topic']} abstract topic markers: style markers move more slowly among stayer keys than "
            f"topic markers (any position: G_style {fci(ga['G_style']['est'], ga['G_style']['lo'], ga['G_style']['hi'])}"
            f" vs G_topic {fci(ga['G_topic']['est'], ga['G_topic']['lo'], ga['G_topic']['hi'])}), and the gap sits at the "
            f"first list position (G_style {fnum(mk['first']['G_style']['est'])}). Holm p: H2a "
            f"{fp(h2a['p_holm'])}, H2b {fp(h2b['p_holm'])}, H2d {fp(h2d['p_holm'])}.")


# ==============================================================================================
# Figure 4: the machine register (D3)
# ==============================================================================================
def fig4() -> str:
    ss = rc(D3 / "fig_F3_1_slot_shares.csv")
    fpv = rc(D3 / "fingerprint_prevalence_by_year.csv").set_index("year")
    sig = rc(D3 / "fig_F3_4_signature.csv")
    r3 = rj(D3 / "results.json")

    style()
    fig = plt.figure(figsize=(7.0, 3.2))
    ax = fig.add_axes([0.085, 0.36, 0.235, 0.55])
    bx = fig.add_axes([0.415, 0.36, 0.19, 0.55])
    cx = fig.add_axes([0.735, 0.36, 0.25, 0.55])
    leg_kw = dict(loc="upper center", bbox_to_anchor=(0.5, -0.27), ncol=1, frameon=False, handlelength=1.8)
    # ---- a: slot shares
    sl = ss[ss["slot"] == "pooled_slots"].sort_values("year")
    ct = ss[ss["slot"] == "pooled_controls"].sort_values("year")
    for d_, col, mk_ in ((ct, GREY, "s"), (sl, BLUE, "o")):
        ax.fill_between(d_["year"], d_["lo"] * 100, d_["hi"] * 100, color=col, alpha=0.18, lw=0, zorder=1)
        ax.plot(d_["year"], d_["share"] * 100, color=col, lw=2, marker=mk_, ms=5, mec="white", mew=0.8, zorder=3)
    ax.axvline(2023.5, color=GREY, lw=0.8, ls=":", zorder=1)
    ax.set_ylim(0, 100)
    ax.set_xlim(2017.6, 2026.4)
    yrs = list(range(2018, 2027))
    ax.set_xticks(yrs, [f"’{y % 100:02d}" if y % 2 == 0 else "" for y in yrs])
    ax.set_ylabel("Share of slot-filled titles (%)")
    ax.set_xlabel("ICLR year")
    ax.legend([Line2D([], [], color=BLUE, lw=2, marker="o", ms=5, mec="white"),
               Line2D([], [], color=GREY, lw=2, marker="s", ms=5, mec="white")],
              ["LLM-favoured verb (pooled slots)", "Control pairs (pooled)"], **leg_kw)
    panel_title(ax, "a", "Meaning-fixed slots")

    # ---- b: title register rates
    yb = [y for y in fpv.index if y >= 2021]
    for colname, col, lbl in (("r24_any", ORANGE, "R24 (2024-generation) words"),
                              ("r26_any", AQUA, "R26 (2026-generation) words")):
        bx.plot(yb, fpv.loc[yb, colname] * 1000, color=col, lw=2, marker="o", ms=5, mec="white", mew=0.8, label=lbl)
    bx.axvline(2023.5, color=GREY, lw=0.8, ls=":", zorder=1)
    bx.set_xticks(yb, [f"’{y % 100:02d}" for y in yb])
    bx.set_xlim(2020.6, 2026.4)
    bx.set_ylim(0, 75)
    bx.set_ylabel("Titles per 1,000")
    bx.set_xlabel("ICLR year")
    bx.legend(**leg_kw)
    panel_title(bx, "b", "Title register")

    # ---- c: signature forest
    rows = ["2024-26 pooled", "2024", "2025", "2026", "NA pool"]
    disp = {"2024-26 pooled": "2024–26", "NA pool": "NA pool"}
    sig = sig[sig["row"].isin(rows)]
    for i, rw in enumerate(rows):
        yy = len(rows) - 1 - i
        for dy, outc, col in ((0.15, "LLM slot variant | slot filled", BLUE), (-0.15, "NAME title", GREY)):
            r = sig[(sig["row"] == rw) & (sig["outcome"] == outc)]
            if len(r):
                r = r.iloc[0]
                dot_ci(cx, yy + dy, r["OR"], r["lo"], r["hi"], col)
    cx.axvline(1, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    cx.set_xscale("log")
    cx.set_xlim(0.2, 4.0)
    cx.set_xticks([0.25, 0.5, 1, 2, 4], ["0.25", "0.5", "1", "2", "4"])
    cx.minorticks_off()
    cx.set_yticks(range(len(rows) - 1, -1, -1), [disp.get(r, r) for r in rows])
    hide_y_grid(cx)
    cx.set_ylim(-0.6, len(rows) - 0.4)
    cx.set_xlabel("OR of fingerprinted abstract (log)")
    cx.legend([Line2D([], [], color=BLUE, lw=1.6, marker="o", ms=5.5, mec="white"),
               Line2D([], [], color=GREY, lw=1.6, marker="o", ms=5.5, mec="white")],
              ["LLM slot variant | slot filled", "NAME title (same papers)"], **leg_kw)
    panel_title(cx, "c", "Lexical vs structural")

    save(fig, "fig4_register", {"a_slot_shares": pd.concat([sl, ct]),
                                "b_register_rates": fpv.loc[yb, ["r24_any", "r26_any", "f24", "f26"]].reset_index(),
                                "c_signature": sig})

    h3a, h3b, h3c, h3d = (hyp(r3, k) for k in ("H3a", "H3b", "H3c", "H3d"))
    ea, eb, ed = h3a["estimates"], h3b["estimates"], h3d["estimates"]["primary"]
    ps = ea["pooled_slots_post"]
    cp = ea["controls_post"]
    st = ea["stacked_interaction"]
    r24 = eb["rates_per_1k"]["all|r24_any"]
    r26 = eb["rates_per_1k"]["all|r26_any"]
    s23 = sl.set_index("year")["share"]
    return (f"LLM-favoured wording in titles. (a) Share of titles that fill a meaning-fixed opener slot with the "
            f"LLM-favoured verb (Enhancing/Boosting vs Improving; Unveiling vs Understanding; Leveraging vs Exploiting; "
            f"comprehensive vs systematic), pooled over slots, against control pairs (towards/toward, novel/new, "
            f"via/using) in grey; bands are 95% Wilson intervals. The slot share moved from {s23.get(2023, np.nan):.2f} in "
            f"2023 to {s23.get(2024, np.nan):.2f} in 2024 (post OR {fci(ps['OR'], ps['lo'], ps['hi'])} with slot-specific "
            f"trends; controls {fci(cp['OR'], cp['lo'], cp['hi'])}; slot-minus-control OR "
            f"{fci(st['OR'], st['lo'], st['hi'])}); the 2023 cohort already deviates, so the break is better read as "
            f"an acceleration from 2024. (b) Title rates of the 2024-generation register R24 (enhanc*, leverag*, "
            f"unveil*, ...) and the 2026-generation register R26 (unified, unifying, beyond, bridging): from 2025 to "
            f"2026 R24 fell from {r24['r2025']:.1f} to {r24['r2026']:.1f} per 1,000 (down in {eb['r24_down']} large "
            f"areas) while R26 rose from {r26['r2025']:.1f} to {r26['r2026']:.1f} (up in {eb['r26_up']}). "
            f"(c) Association of an abstract LLM fingerprint (F24 ∪ F26 ∪ title typography) with the LLM slot variant "
            f"and with a NAME title on the same slot-filled papers, within topic100 x year (implied ORs from LPMs, "
            f"95% CIs): OR_slot {fci(ed['OR_slot'], ed['OR_slot_lo'], ed['OR_slot_hi'])} vs OR_NAME "
            f"{fci(ed['OR_name'], ed['OR_name_lo'], ed['OR_name_hi'])}, ratio {fci(ed['ratio'], ed['ratio_lo'], ed['ratio_hi'])}"
            f" (n = {ed['n_papers']:,} papers, 2024-26). Holm p: H3a {fp(h3a['p_holm'])}, H3b {fp(h3b['p_holm'])}, "
            f"H3d {fp(h3d['p_holm'])}.")


# ==============================================================================================
# Figure 5: stage-wise filter gains (D4 H4a, H4b)
# ==============================================================================================
FEAT_LABEL = {"NAME": "NAME", "compound": "Compound (any colon)", "mixed_case_name": "Mixed-case name",
              "title_case": "Title Case", "phrase_colon": "Phrase colon", "all_caps_title": "ALL-CAPS title",
              "sentence_case": "Sentence case", "question_opener": "Question opener", "O_union": "Outsider union",
              "R24": "R24 words (title)", "R26": "R26 words (title)", "title_typo": "LLM typography (title)",
              "F24": "F24 words (abstract)", "F26": "F26 (abstract)", "emdash": "Em dash (abstract)",
              "style_density": "Style density (abstract)", "L_union": "LLM-style union"}
SET_OF = {"NAME": "M", "compound": "M", "mixed_case_name": "M", "title_case": "M", "phrase_colon": "M",
          "all_caps_title": "O", "sentence_case": "O", "question_opener": "O", "O_union": "O",
          "R24": "L", "R26": "L", "title_typo": "L", "F24": "L", "F26": "L", "emdash": "L", "style_density": "L",
          "L_union": "L"}


def fig5() -> str:
    g = rc(D4 / "gains.csv")
    g = g[(g["variant"] == "primary") & (g["pooling"] == "std")]
    r4 = rj(D4 / "results.json")
    feats = ["NAME", "compound", "mixed_case_name", "all_caps_title", "O_union", "R24", "F24", "style_density",
             "L_union"]
    stages = [("desk", "Desk screen", BLUE), ("exit", "Author exit", ORANGE), ("dec", "Decision", AQUA),
              ("total", "Total (accepted/all)", YELLOW)]
    pooled = g[g["period"] == "2024-26"].set_index(["feature", "gain"])

    style()
    fig = plt.figure(figsize=(7.0, 3.55))
    gs = fig.add_gridspec(3, 2, width_ratios=[1.6, 1.0], wspace=0.42, hspace=0.32)
    ax = fig.add_subplot(gs[:, 0])
    XMIN, XMAX = 0.70, 1.25
    nF = len(feats)
    off = {"desk": 0.27, "exit": 0.09, "dec": -0.09, "total": -0.27}
    rowsA = []
    for i, f in enumerate(feats):
        yy = nF - 1 - i
        for st, _, col in stages:
            if (f, st) not in pooled.index:
                continue
            r = pooled.loc[(f, st)]
            e, lo, hi = r["est"], r["lo95"], r["hi95"]
            rowsA.append({"feature": f, "set": SET_OF.get(f), "stage": st, "gain": e, "lo95": lo, "hi95": hi})
            y_ = yy + off[st]
            if e < XMIN:   # off scale: arrow marker at the left edge, value printed
                ax.plot([XMIN * 1.004], [y_], marker="<", ms=5.5, color=col, mec="white", mew=0.6, lw=0,
                        zorder=4, clip_on=False)
                continue
            dot_ci(ax, y_, e, max(lo, XMIN), min(hi, XMAX), col, ms=5, lw=1.4)
        if (f, "dec") in pooled.index and pooled.loc[(f, "dec"), "est"] < XMIN:
            ax.text(XMIN * 1.02, yy - 0.18, f"off scale: decision {pooled.loc[(f, 'dec'), 'est']:.2f}, "
                    f"total {pooled.loc[(f, 'total'), 'est']:.2f}", fontsize=FS, color=TEXT2, va="center")
    for yb in (nF - 3.5, nF - 5.5):  # separators between M / O / L blocks
        ax.axhline(yb, color=GRID, lw=0.8, zorder=0)
    ax.axvline(1, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.set_xscale("log")
    ax.set_xlim(XMIN, XMAX)
    ax.set_xticks([0.7, 0.8, 0.9, 1.0, 1.1, 1.2], ["0.7", "0.8", "0.9", "1", "1.1", "1.2"])
    ax.minorticks_off()
    ax.set_yticks(range(nF - 1, -1, -1), [FEAT_LABEL[f] for f in feats])
    hide_y_grid(ax)
    ax.set_ylim(-0.6, nF - 0.4)
    ax.set_xlabel("Stage gain, 2024–26 (log scale)")
    ax.legend([Line2D([], [], color=c_, lw=1.4, marker="o", ms=5, mec="white") for _, _, c_ in stages],
              [s[1] for s in stages], loc="lower left", bbox_to_anchor=(-0.02, -0.3), ncol=4, frameon=False,
              columnspacing=1.0, handlelength=1.4)
    panel_title(ax, "a", "What each stage does to a feature")

    # ---- b: total gain by year, small multiples (yellow = total gain, as in a)
    series = [("NAME", "NAME"), ("O_union", "Outsider union"), ("L_union", "LLM-style union")]
    rowsB = []
    yrs = list(range(2018, 2027))
    for k, (f, lbl) in enumerate(series):
        bx = fig.add_subplot(gs[k, 1])
        d_ = g[(g["feature"] == f) & (g["gain"] == "total") & g["period"].isin([str(y) for y in yrs])].copy()
        d_["year"] = d_["period"].astype(int)
        d_ = d_.sort_values("year")
        if f == "NAME":
            bx.fill_between([2017.5, 2026.5], 0.95, 1.10, color=BAND_GREY, alpha=0.55, lw=0, zorder=0)
        bx.axhline(1, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
        bx.fill_between(d_["year"], d_["lo95"], d_["hi95"], color=YELLOW, alpha=0.22, lw=0, zorder=1)
        bx.plot(d_["year"], d_["est"], color=YELLOW, lw=2, marker="o", ms=4.8, mec="white", mew=0.7, zorder=3)
        bx.axvline(2023.5, color=GREY, lw=0.8, ls=":", zorder=1)
        bx.set_xlim(2017.5, 2026.5)
        bx.set_ylim(0.4, 1.6)
        bx.set_yticks([0.5, 1.0, 1.5])
        bx.text(2026.4, 1.58, lbl, fontsize=FS, color=TEXT, va="top", ha="right")
        bx.set_xticks(yrs, [f"’{y % 100:02d}" if y % 2 == 0 else "" for y in yrs] if k == 2 else [""] * len(yrs))
        if k == 1:
            bx.set_ylabel("Accepted / all submissions")
        if k == 2:
            bx.set_xlabel("ICLR year")
        if k == 0:
            panel_title(bx, "b", "Total gain by year")
        for _, r in d_.iterrows():
            rowsB.append({"feature": f, "year": r["year"], "total_gain": r["est"], "lo95": r["lo95"], "hi95": r["hi95"]})

    save(fig, "fig5_stage_gains", {"a_stage_gains_2024_26": pd.DataFrame(rowsA), "b_total_by_year": pd.DataFrame(rowsB)})

    H4a, H4b = r4["hypotheses"]["H4a"]["estimates"], r4["hypotheses"]["H4b"]["estimates"]
    sg = H4a["stage_gains_2024_26"]
    pt = H4a.get("tost") or H4a["pooled_2024_26_std"]
    ip = H4a["its_pools"]
    lu, ou = H4b["L_union_total"], H4b["O_union_total"]
    lpre = H4b["L_union_pre_2018_23_total"]
    return (f"Stage gains P(feature | passed stage) / P(feature | entered stage) for ICLR 2024-26 (year-standardised; "
            f"paper bootstrap stratified by year, B = 2000, 95% CIs). (a) Desk screen, author exit (withdrawal before "
            f"decision) and decision, and their product, the accepted/all ratio. NAME is slightly depleted before the "
            f"decision (exit {fci(sg['exit']['est'], sg['exit']['lo95'], sg['exit']['hi95'], d=3)}) and enriched at it "
            f"(decision {fci(sg['dec']['est'], sg['dec']['lo95'], sg['dec']['hi95'], d=3)}), netting to "
            f"{pt['est']:.3f} (90% CI {pt['lo90']:.3f}-{pt['hi90']:.3f}, inside the [0.90, 1.11] equivalence margin); "
            f"the 2024 slope break is similar in accepted, rejected and withdrawn pools (ORs {ip['ACC']['OR']:.2f} / "
            f"{ip['REJ']['OR']:.2f} / {ip['WD']['OR']:.2f}, equality p = {H4a['its_wald']['p']:.2f}). Outsider markers "
            f"are depleted ({fci(ou['est'], ou['lo95'], ou['hi95'], d=3)}), mostly at the decision stage, where "
            f"camera-ready reformatting cannot be excluded; LLM-style markers mildly so "
            f"({fci(lu['est'], lu['lo95'], lu['hi95'], d=3)}). (b) Accepted/all ratio by year (grey band: the "
            f"pre-registered [0.95, 1.10] band for NAME). The LLM-style union was enriched among accepted papers in "
            f"2018-23 ({fci(lpre['est'], lpre['lo95'], lpre['hi95'], d=3)}) and is not after 2023. Decision-stage gains "
            f"are not identified against camera-ready edits (Figure 6b).")


# ==============================================================================================
# Figure 6: published-only bias and the camera-ready bound (D4 H4e + WP4)
# ==============================================================================================
def fig6() -> str:
    at = rc(D4 / "atlas.csv")
    at = at[at["in_forest"].astype(bool)] if "in_forest" in at.columns else at
    tp = rc(SNAP / "T4_2_tipping_points.csv")
    sres = rj(SNAP / "results.json")
    r4 = rj(D4 / "results.json")
    cls_col = {"M": BLUE, "O": ORANGE, "L": AQUA}
    cls_name = {"M": "Mainstream", "O": "Outsider", "L": "LLM-style"}

    style()
    fig = plt.figure(figsize=(7.0, 4.6))
    ax = fig.add_axes([0.235, 0.2, 0.29, 0.73])
    bx = fig.add_axes([0.745, 0.2, 0.235, 0.73])
    # ---- a: atlas
    at = at.copy()
    at["cls"] = pd.Categorical(at["cls"], ["M", "O", "L"], ordered=True)
    at = at.sort_values(["cls"], kind="stable").reset_index(drop=True)
    n = len(at)
    ypos = []
    y = 0.0
    prev = None
    for _, r in at.iterrows():
        if prev is not None and r["cls"] != prev:
            y -= 0.6
        ypos.append(y)
        prev = r["cls"]
        y -= 1.0
    XMIN, XMAX = 0.5, 1.25
    ax.axvspan(0.9, 1.1, color=BAND_GREY, alpha=0.55, lw=0, zorder=0)
    ax.axvline(1, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    for yy, (_, r) in zip(ypos, at.iterrows()):
        col = cls_col[str(r["cls"])]
        e, lo, hi = r["ratio"], r["ratio_lo95"], r["ratio_hi95"]
        if e < XMIN:
            ax.plot([XMIN * 1.004], [yy], marker="<", ms=5.5, color=col, mec="white", mew=0.6, lw=0, zorder=4,
                    clip_on=False)
            ax.text(XMIN * 1.03, yy, f"{e:.2f}", fontsize=FS, color=TEXT2, va="center")
            continue
        dot_ci(ax, yy, e, max(lo, XMIN), min(hi, XMAX), col, ms=5, lw=1.4)
    lab = (at["label"].astype(str).str.replace(" prevalence", "", regex=False)
           .str.replace("RARE21 Kobak bound (2024-26 mean)", "Kobak LLM bound (F24)", regex=False)
           .str.replace("Colon premium OR, 2024-26 (decided-only)", "Colon premium OR", regex=False)
           .str.replace("Opener entropy, NAME-collapsed (rarefied)", "Opener entropy", regex=False)
           .str.replace("Lexical turnover JSD (rarefied)", "Lexical turnover (JSD)", regex=False)
           .str.replace("ITS slope-change OR (NAME)", "2024 slope-change OR", regex=False)
           .str.replace("LLM abbreviation-only share", "LLM-abbreviation names", regex=False)
           .str.replace("Style density (mean)", "Style density (abstract)", regex=False)
           .str.replace("Title typography", "LLM typography (title)", regex=False)
           .str.replace("O-union", "Outsider union", regex=False)
           .str.replace("L-union", "LLM-style union", regex=False)
           .replace({"R24": "R24 words (title)", "R26": "R26 words (title)", "F24": "F24 words (abstract)",
                     "F26": "F26 (abstract)", "Phrase-colon": "Phrase colon"}))
    ax.set_yticks(ypos, lab)
    hide_y_grid(ax)
    ax.set_ylim(min(ypos) - 0.7, 0.7)
    ax.set_xscale("log")
    ax.set_xlim(XMIN, XMAX)
    ax.set_xticks([0.5, 0.7, 0.9, 1.1], ["0.5", "0.7", "0.9", "1.1"])
    ax.minorticks_off()
    ax.set_xlabel("Accepted-only / all submissions (log)")
    ax.legend([Line2D([], [], color=cls_col[k], lw=1.4, marker="o", ms=5, mec="white") for k in ("M", "O", "L")]
              + [Patch(color=BAND_GREY, alpha=0.55, lw=0)],
              [cls_name[k] for k in ("M", "O", "L")] + ["±10%"], loc="upper center", bbox_to_anchor=(0.2, -0.115),
              ncol=4, frameon=False, columnspacing=0.8, handlelength=1.3, handletextpad=0.4)
    panel_title(ax, "a", "What a published-only study would see")

    # ---- b: audit net-flip DiD vs tipping point (auditable features only)
    fam_cls = {"M": "M", "ortho": "M", "O": "O", "L": "L", "casing": "O", "ctrl": None}
    tq = tp[tp["auditable"].astype(bool)].copy()
    ab = rc(SNAP / "abstract_audit.csv")
    ab = ab[ab["auditable"].astype(bool) & ab["feature"].isin(["F24"])]
    ab = pd.DataFrame({"feature": ab["feature"], "label": "F24 words (abstract)", "family": "L",
                       "did_pp": ab["tp_did_pp"], "did_lo_pp": ab["tp_did_lo_pp"], "did_hi_pp": ab["tp_did_hi_pp"],
                       "tip_dec_pp": ab["tp_tip_dec_pp"], "G_dec_obs": ab["tp_G_dec_obs"],
                       "G_dec_identified": ab["tp_G_dec_identified"]})
    tq = pd.concat([tq, ab], ignore_index=True)
    tq["cls"] = tq["family"].map(fam_cls)
    tq.loc[tq["feature"].isin(["F24", "L_abstract", "L_abs_words", "F24_2", "F26_words"]), "cls"] = "L"
    m = len(tq)
    rowsB = []
    for i, (_, r) in enumerate(tq.iterrows()):
        yy = m - 1 - i
        col = cls_col.get(r["cls"], GREY) if isinstance(r["cls"], str) else GREY
        dot_ci(bx, yy, r["did_pp"], r["did_lo_pp"], r["did_hi_pp"], col, ms=5, lw=1.4)
        bx.plot([r["tip_dec_pp"]], [yy], marker="D", ms=4.6, mfc="white", mec=TEXT, mew=1.1, lw=0, zorder=6)
        rowsB.append({"feature": r["feature"], "label": r["label"], "class": r["cls"], "did_pp": r["did_pp"],
                      "did_lo95_pp": r["did_lo_pp"], "did_hi95_pp": r["did_hi_pp"], "tip_dec_pp": r["tip_dec_pp"],
                      "G_dec_obs": r["G_dec_obs"], "G_dec_identified": r["G_dec_identified"]})
    bx.axvline(0, color=GREY, lw=0.8, ls=(0, (3, 2)), zorder=1)
    lbl = (tq["label"].astype(str).str.replace("NAME (primary)", "NAME", regex=False)
           .str.replace("F24 (RARE21 >= 1)", "F24 words (abstract)", regex=False)
           .str.replace("L-abstract union", "LLM abstract union", regex=False)
           .str.replace("F24 or F26 words", "F24 or F26 words (abstract)", regex=False)
           .str.replace("O-union", "Outsider union", regex=False))
    bx.set_yticks(range(m - 1, -1, -1), lbl)
    hide_y_grid(bx)
    bx.set_ylim(-0.7, m - 0.3)
    bx.set_xlabel("Net-flip DiD (pp)")
    bx.legend([Line2D([], [], color=BLUE, lw=1.4, marker="o", ms=5, mec="white"),
               Line2D([], [], lw=0, marker="D", ms=4.6, mfc="white", mec=TEXT, mew=1.1)],
              ["Audit DiD (95% CI)", "Tipping point D*"], loc="upper center", bbox_to_anchor=(0.35, -0.115), ncol=2,
              frameon=False, columnspacing=0.8, handlelength=1.3, handletextpad=0.4)
    panel_title(bx, "b", "Camera-ready audit")

    save(fig, "fig6_published_bias", {"a_atlas": at.assign(ypos=ypos), "b_audit": pd.DataFrame(rowsB)})

    H4e = r4["hypotheses"]["H4e"]["estimates"]
    bycls = {d_["cls"]: d_ for d_ in H4e["by_class"]}
    nm = tq.set_index("feature").loc["NAME"]
    meta = sres.get("meta", {})
    npair = meta.get("n_pairs_primary")
    sb2 = hyp(sres, "SB2")
    kob = at[at["label"].astype(str).str.contains("Kobak")]
    kob_txt = (f"; the accepted-only Kobak-style LLM bound is {kob.iloc[0]['ratio']:.2f} of the all-submission bound"
               if len(kob) else "")
    return (f"How far a study of accepted papers alone would be from the full submission pool (2024-26). (a) "
            f"Accepted-only / all-submission ratio for {len(at)} pre-registered fashion statistics (95% CIs; grey band "
            f"±10%). Mainstream statistics are within ±10% in {bycls['M']['within']}/{bycls['M']['n']} cases (median "
            f"|log ratio| {bycls['M']['median_abs_log']:.3f}); deviations concentrate in outsider "
            f"({bycls['O']['within']}/{bycls['O']['n']} within) and LLM-style markers ({bycls['L']['within']}/"
            f"{bycls['L']['n']}){kob_txt}. (b) arXiv camera-ready audit (pre-decision v1 vs stored title, or abstract for "
            f"F24; accepted minus rejected net flips; {'' if npair is None else f'{npair} pairs; '}auditable features "
            f"only; grey: the 'via' control word): the "
            f"decision-stage gain of a feature is identified only if its tipping point D* lies outside the 95% CI. For "
            f"NAME the DiD is {nm['did_pp']:+.2f} pp [{nm['did_lo_pp']:.2f}, {nm['did_hi_pp']:.2f}] against "
            f"D* = {nm['tip_dec_pp']:.2f} pp; {sb2['estimate']}. Acceptance associations of title features are therefore "
            f"associational and not separated from camera-ready editing.")


# ==============================================================================================
# Table 1: pre-registered hypotheses, estimates and verdicts
# ==============================================================================================
def _verdict(v) -> str:
    v = str(v).replace("_", " ").strip().strip('"')
    v = v.split(";")[0].strip()
    rep = {"not established year level": "not established (year level)",
           "supported on the pre-registered groups": "supported on pre-registered groups",
           "not supported": "not supported"}
    return rep.get(v, v)


def table1() -> str:
    r1 = rj(D1 / "results.json")
    r2 = rj(D2 / "results.json")
    r3 = rj(D3 / "results.json")
    r4 = rj(D4 / "results.json")
    rs = rj(SNAP / "results.json")
    rows = []

    def add(dirn, hid, pred, est, verdict, p):
        rows.append({"direction": dirn, "ID": hid, "Prediction": pred, "Estimate (95% CI)": est,
                     "Verdict": _verdict(verdict), "Holm p": p})

    D1n = "D1 The naming acceleration: content, composition or tool"
    a = r1["H1a"]
    add(D1n, "H1a", "Slope change at 2024, OR > 1; holds in NA pool; placebo breaks null",
        f"OR {fci(*a['year_level_U']['OR'], d=3)}/yr (year level); paper level {fci(*a['slope_change_OR_U'], d=3)}; "
        f"NA pool {fci(*a['year_level_NA']['OR'], d=3)}; sup-LR selects {a['supLR_selected']}",
        a["verdict"], fp(a["holm_adjusted_p"]))
    b = r1["H1b"]["shares"]
    add(D1n, "H1b", "Name-masked content share of the 2023→26 rise in [0.20, 0.50]; none ≥ 0.60",
        f"Fixed: R1 {fci(b['R1|fixed']['share'], *b['R1|fixed']['ci'])}, R3 {fnum(b['R3|fixed']['share'])}; "
        f"rolling: R1 {fci(b['R1|rolling']['share'], *b['R1|rolling']['ci'])}, R3 {fnum(b['R3|rolling']['share'])}",
        r1["H1b"]["verdict"], fp(r1["H1b"]["holm_adjusted_p"]))
    c = r1["H1c"]
    add(D1n, "H1c", "Unexplained drift u accelerates: mean u(2024–26) − mean u(2019–23) > 0, ratio ≥ 1.5",
        f"u {c['u_pre'] * 100:.2f} → {c['u_post'] * 100:.2f} pp/yr; diff {c['diff'] * 100:+.2f} pp "
        f"[{c['year_level_two_stage']['diff_ci'][0] * 100:.2f}, {c['year_level_two_stage']['diff_ci'][1] * 100:.2f}] "
        f"(year level); NA pool {c['replications']['R1|NA|primary|rolling']['diff'] * 100:+.2f} pp",
        c["verdict"], fp(c["holm_adjusted_p"]))
    d = r1["H1d"]
    dy = d["dfl_full_by_year"]
    add(D1n, "H1d", "Composition (team size × new keys × LLM topic) explains ≤ 30% (DFL)",
        f"DFL {dy['2024']['share']:.2f} / {dy['2025']['share']:.2f} / {fci(dy['2026']['share'], *dy['2026']['ci'])} "
        f"(2024/25/26)", d["verdict"], fp(d["holm_adjusted_p"]))
    e = r1["H1e"]
    f0 = e["f0_rise"]["F_d1"]["2026"]
    add(D1n, "H1e", "Tool bounded: F = 0 rise ≥ 85% of total; δ ≤ 5 pp; tool share at A = 0.39 < 0.25",
        f"F = 0 rise / total {fci(f0['ratio_F0_all'], *f0['ratio_ci'])}; δ {e['tool']['delta_primary']['delta'] * 100:+.1f} pp; "
        f"tool share {fci(e['tool_share_0.39_corrected_2026']['share'], e['tool_share_0.39_corrected_2026']['lo'], e['tool_share_0.39_corrected_2026']['hi'])}",
        e["verdict"], fp(e["holm_adjusted_p"]))

    D2n = "D2 Who carries the change (declared profile keys)"
    son = r2["shared_outcome_null"]["main"]
    nulls2 = [son[p_][k_]["est"] for p_ in ("last", "any") for k_ in ("null_Nfirst", "null_NRfirst")]
    h = hyp(r2, "H2a")["estimate"]
    add(D2n, "H2a", "Within-stayer share ≥ 0.70 (last position), ≥ 0.60 (any position)",
        f"ρ_last {fci(h['rho_last']['est'], h['rho_last']['lo'], h['rho_last']['hi'], d=3)}; ρ_any "
        f"{fci(h['rho_any']['est'], h['rho_any']['lo'], h['rho_any']['hi'], d=3)}; generational null "
        f"{min(nulls2):.2f}–{max(nulls2):.2f}",
        hyp(r2, "H2a")["verdict"], fp(hyp(r2, "H2a")["p_holm"]))
    h = hyp(r2, "H2b")["estimate"]
    add(D2n, "H2b", "First-position share lower than last by ≥ 0.2; entrant first keys above stayers",
        f"ρ_first {fci(h['rho_first']['est'], h['rho_first']['lo'], h['rho_first']['hi'], d=3)}; first − last "
        f"{fci(h['first_minus_last']['est'], h['first_minus_last']['lo'], h['first_minus_last']['hi'])}",
        hyp(r2, "H2b")["verdict"], fp(hyp(r2, "H2b")["p_holm"]))
    h = hyp(r2, "H2c")["estimate"]
    add(D2n, "H2c", "Stayer change at zero new co-author keys ≥ 0.5 × population change",
        f"{fci(h['ratio_i']['est'], h['ratio_i']['lo'], h['ratio_i']['hi'])} × population "
        f"({h['change_at_share_new0']['est'] * 100:.1f} of {h['population_change'] * 100:.1f} pp)",
        hyp(r2, "H2c")["verdict"], fp(hyp(r2, "H2c")["p_holm"]))
    h = hyp(r2, "H2d")["estimate"]
    add(D2n, "H2d", "Slope of within-stayer on population change ≈ 1; G larger for style than topic",
        f"slope {fci(h['slope_all']['est'], h['slope_all']['lo'], h['slope_all']['hi'])}; G_style "
        f"{fci(h['G_style']['est'], h['G_style']['lo'], h['G_style']['hi'])} vs G_topic "
        f"{fci(h['G_topic']['est'], h['G_topic']['lo'], h['G_topic']['hi'])}",
        hyp(r2, "H2d")["verdict"], fp(hyp(r2, "H2d")["p_holm"]))
    h = hyp(r2, "H2e")["estimate"]
    add(D2n, "H2e", "Pre-LLM (2018→20, email keys): ≥ 50% of the NAME rise within stayers",
        f"ρ_NAME {fci(h['name_any']['est'], h['name_any']['lo'], h['name_any']['hi'])}; literal Kitagawa share "
        f"{fnum(h['name_any_kitagawa_share']['est'])}", hyp(r2, "H2e")["verdict"], fp(hyp(r2, "H2e")["p_holm"]))

    D3n = "D3 The machine register"
    h = hyp(r3, "H3a")["estimates"]
    add(D3n, "H3a", "Meaning-fixed LLM slots: post OR ≥ 2; controls in [0.67, 1.5]; slot − control > 0",
        f"slots {fci(h['pooled_slots_post']['OR'], h['pooled_slots_post']['lo'], h['pooled_slots_post']['hi'])}; "
        f"controls {fci(h['controls_post']['OR'], h['controls_post']['lo'], h['controls_post']['hi'])}; stacked "
        f"{fci(h['stacked_interaction']['OR'], h['stacked_interaction']['lo'], h['stacked_interaction']['hi'])}",
        hyp(r3, "H3a")["verdict"], fp(hyp(r3, "H3a")["p_holm"]))
    h = hyp(r3, "H3b")["estimates"]
    add(D3n, "H3b", "2025→26 within area: R24 falls in ≥ 10/16, R26 rises in ≥ 12/16",
        f"R24 down {h['r24_down']}, R26 up {h['r26_up']}; rate per 1k R24 {h['rates_per_1k']['all|r24_any']['r2025']:.1f} → "
        f"{h['rates_per_1k']['all|r24_any']['r2026']:.1f}, R26 {h['rates_per_1k']['all|r26_any']['r2025']:.1f} → "
        f"{h['rates_per_1k']['all|r26_any']['r2026']:.1f}", hyp(r3, "H3b")["verdict"], fp(hyp(r3, "H3b")["p_holm"]))
    h = hyp(r3, "H3c")["estimates"]["primary"]
    add(D3n, "H3c", "Vintage alignment: OR(F24 → R24) > OR(F26 → R24), 2025–26",
        f"{fnum(h['OR_a'])} vs {fnum(h['OR_b'])}; ratio {fci(h['ratio'], *h['ratio_ci'])}",
        hyp(r3, "H3c")["verdict"], fp(hyp(r3, "H3c")["p_holm"]))
    h = hyp(r3, "H3d")["estimates"]["primary"]
    add(D3n, "H3d", "Lexical signature: OR(F → slot variant) ≥ 1.5 × OR(F → NAME)",
        f"{fci(h['OR_slot'], h['OR_slot_lo'], h['OR_slot_hi'])} vs {fci(h['OR_name'], h['OR_name_lo'], h['OR_name_hi'])}; "
        f"ratio {fci(h['ratio'], h['ratio_lo'], h['ratio_hi'])}", hyp(r3, "H3d")["verdict"], fp(hyp(r3, "H3d")["p_holm"]))
    h = hyp(r3, "H3e")["estimates"]["primary"]
    add(D3n, "H3e", "Exploratory: second-hand diffusion claimed only if U* > 0.8",
        f"U* {fci(h['U_star'], h['U_lo'], h['U_hi'])}; contamination-corrected {fnum(h['U_star_corrected'])}",
        "unresolved" if str(hyp(r3, "H3e")["verdict"]).startswith("not") else hyp(r3, "H3e")["verdict"], "expl.")

    D4n = "D4 The gatekeeper (2024–26 pooled)"
    H = r4["hypotheses"]
    h = H["H4a"]["estimates"]
    add(D4n, "H4a", "NAME accepted/all in [0.95, 1.10] every year; TOST in [0.90, 1.11]; equal break across pools",
        f"G_total {(h.get('tost') or h['pooled_2024_26_std'])['est']:.3f} (90% CI "
        f"{(h.get('tost') or h['pooled_2024_26_std'])['lo90']:.3f}–{(h.get('tost') or h['pooled_2024_26_std'])['hi90']:.3f}); "
        f"pool break ORs {h['its_pools']['ACC']['OR']:.2f} / "
        f"{h['its_pools']['REJ']['OR']:.2f} / {h['its_pools']['WD']['OR']:.2f}, p = {h['its_wald']['p']:.2f}",
        H["H4a"]["verdict"], "—")
    h = H["H4b"]["estimates"]
    add(D4n, "H4b", "LLM-style and outsider unions depleted (accepted/all < 1)",
        f"LLM-style {fci(h['L_union_total']['est'], h['L_union_total']['lo95'], h['L_union_total']['hi95'], d=3)}; "
        f"outsider {fci(h['O_union_total']['est'], h['O_union_total']['lo95'], h['O_union_total']['hi95'], d=3)}",
        H["H4b"]["verdict"], "—")
    h = H["H4c"]["estimates"]["ratio_acc_all"]
    add(D4n, "H4c", "Accepted-only Kobak LLM bound ≤ 0.85 × all-submission bound in each of 2024–26",
        f"ratios {h['2024']['ratio']:.2f} / {h['2025']['ratio']:.2f} / {h['2026']['ratio']:.2f} "
        f"(2024 CI [{h['2024']['lo95']:.2f}, {h['2024']['hi95']:.2f}])", H["H4c"]["verdict"], "—")
    h = H["H4d"]["estimates"]
    add(D4n, "H4d", "Withdrawn vs rejected: NAME > 0 across papers, ≤ 0 within last-position key",
        f"{h['cross_pp']['est']:+.2f} vs {h['within_pp']['est']:+.2f} pp; difference {h['diff_pp']['est']:.2f} pp "
        f"(se {h['diff_pp']['se']:.2f})", H["H4d"]["verdict"], "—")
    h = H["H4e"]["estimates"]
    bc = {x["cls"]: x for x in h["by_class"]}
    add(D4n, "H4e", "Descriptive: published-only atlas within ±10% for mainstream statistics",
        f"mainstream {bc['M']['within']}/{bc['M']['n']}, outsider {bc['O']['within']}/{bc['O']['n']}, "
        f"LLM-style {bc['L']['within']}/{bc['L']['n']} within ±10%", H["H4e"]["verdict"], "descr.")
    sb1, sb2 = hyp(rs, "SB1"), hyp(rs, "SB2")
    nm = rc(SNAP / "T4_2_tipping_points.csv").set_index("feature").loc["NAME"]
    add(D4n, "Gate", "A decision-stage gain enters the headline only if its tipping point lies outside the audit CI",
        f"NAME DiD {nm['did_pp']:+.2f} pp [{nm['did_lo_pp']:.2f}, {nm['did_hi_pp']:.2f}] vs D* {nm['tip_dec_pp']:.2f} pp; "
        f"{sb2['estimate'].split(';')[0]}", "no title feature passes", "—")

    df = pd.DataFrame(rows)
    write_table(df, "table1_hypotheses",
                "Pre-registered hypotheses: estimates and verdicts (all numbers regenerated in the harmonised pipeline).",
                "tab:hypotheses", "l p{3.9cm} p{5.7cm} p{2.3cm} r", group_col="direction",
                notes=("Holm p: one-sided, Holm-adjusted within each direction's confirmatory family (D1 uses the "
                       "year-level tests for H1a and H1c; the p-values test the falsification boundary). D4 reports no "
                       "Holm family (—); its tests are equivalence (TOST), bootstrap and Wald tests described in the text. "
                       "expl. = exploratory; descr. = descriptive. ρ = stayer-to-population change ratio; G = generational "
                       "increment; D* = tipping point of the camera-ready net-flip DiD."))
    return ("Pre-registered hypotheses H1a-H4e and the decision-stage gate: prediction, regenerated estimate with 95% CI, "
            "verdict under the pre-registered falsification rule, and Holm-adjusted one-sided p within each direction.")


# ==============================================================================================
# Table 2: the NAME acceleration across samples and definitions (D1 H1a + H1c)
# ==============================================================================================
def table2() -> str:
    its = rc(D1 / "T1_1_its.csv")
    yl = rc(D1 / "its_year_level.csv").set_index("population")
    r1 = rj(D1 / "results.json")
    rep = r1["H1c"]["replications"]
    sel = [  # (spec, pool, subset, years, outcome, topics, label, year-level key, H1c key)
        ("U, topic100 FE (primary)", "primary", "All submissions (primary)", "U", "R1|U|primary|rolling"),
        ("NA pool", "primary", "Camera-ready-free pool (NA)", "NA pool", "R1|NA|primary|rolling"),
        ("non-LLM subset", "primary", "Non-LLM-topic subset", "non-LLM subset", "R1|non_llm|primary|rolling"),
        ("NA pool x non-LLM", "primary", "NA pool × non-LLM", None, None),
        ("ACC pool", "primary", "Accepted pool", None, None),
        ("REJ pool", "primary", "Rejected pool", None, None),
        ("WD pool", "primary", "Withdrawn pool (2018–26)", None, None),
        ("excluding 2026", "primary", "Excluding 2026", "U excluding 2026", "excl2026"),
        ("without 2019", "primary", "Without 2019", None, "no2019"),
        ("U, topic100 FE", "strict", "NAME strict (one-token lead)", None, "R1|U|strict|rolling"),
        ("U, topic100 FE", "loose", "NAME loose (≤ 2-token lead)", None, "R1|U|loose|rolling"),
        ("U, topic100 FE", "compound", "Any colon or spaced dash", None, "R1|U|compound|rolling"),
        ("U, bge topic100 FE", "primary", "bge topic100 FE", None, None),
        ("U, no controls", "primary", "No controls, no topic FE", None, None),
    ]
    rows = []
    for spec, outc, lbl, ykey, ckey in sel:
        m = its[(its["spec"] == spec) & (its["outcome"] == outc)]
        if not len(m):
            continue
        r = m.iloc[0]
        yls = ""
        if ykey is not None and ykey in yl.index:
            q = yl.loc[ykey]
            yls = fci(q["OR_RE"], q["OR_RE_lo"], q["OR_RE_hi"], d=3)
        u = ""
        if ckey == "excl2026":
            q = r1["H1c"]["excluding_2026"]
            u = fci(q["diff"], *q["diff_ci"], d=2, signed=True, pct=True)
        elif ckey == "no2019":
            q = r1["H1c"]["without_2019"]
            u = fci(q["diff"], *q["diff_ci"], d=2, signed=True, pct=True)
        elif ckey is not None and ckey in rep:
            q = rep[ckey]
            u = fci(q["diff"], *q["diff_ci"], d=2, signed=True, pct=True)
        rows.append({"Sample / definition": lbl, "n": f"{int(r['nobs']):,}",
                     "NAME 2023→26 (%)": (f"{r['share_2023'] * 100:.1f} → {r['share_2026'] * 100:.1f}"
                                          if pd.notna(r["share_2026"]) else f"{r['share_2023'] * 100:.1f} → —"),
                     "Pre-trend OR/yr": fnum(r["pre_slope_OR"], 3),
                     "Slope change OR/yr": fci(r["slope_change_OR"], r["slope_change_OR_lo"], r["slope_change_OR_hi"], d=3),
                     "Year-level OR/yr": yls or "—",
                     "LPM slope change (pp/yr)": fci(r["lpm_slope_change_pp"], r["lpm_slope_change_pp_lo"],
                                                     r["lpm_slope_change_pp_hi"], d=2, signed=True),
                     "Δu (pp/yr)": u or "—"})
    df = pd.DataFrame(rows)
    write_table(df, "table2_acceleration",
                "The NAME acceleration across samples and definitions: segmented-logit ITS and content-unexplained drift.",
                "tab:acceleration", "l r l l l l l l", size=r"\scriptsize",
                notes=("Segmented logit NAME ~ (t-2023) + post + post·(t-2023) + log authors + LLM topic + topic100 FE, "
                       "2017-26; slope-change CIs clustered by topic100 (paper level); year-level ORs from a REML "
                       "random-effects meta-regression on adjusted year effects (t, 6 df). LPM: linear probability "
                       "analogue. Δu: mean content-unexplained annual change 2024-26 minus 2019-23 from the rolling "
                       "name-masked R1 content model (conditional paper bootstrap; the two-stage year-level CI for the "
                       "primary is in Table 1). — = not estimated for that sample."))
    prim = df.iloc[0]
    return ("The NAME acceleration across pools, subsets, years and NAME definitions: segmented-logit slope change "
            f"(primary {prim['Slope change OR/yr']}), its year-level analogue, the LPM slope change, and the "
            "acceleration of content-unexplained drift Δu.")


# ==============================================================================================
# Table 3: content-counterfactual representation bracket (D1 H1b, T1.2)
# ==============================================================================================
def table3() -> str:
    t = rc(D1 / "T1_2_representations.csv")
    reps = [("R1", "Masked abstract TF-IDF (primary)", "masked"), ("R3", "Masked abstract, bge embedding", "masked"),
            ("R5", "R1 minus rhetorical moves", "masked"), ("R1yfe", "R1 + training-year FE", "sensitivity"),
            ("R1@0.5", "R1 at the pilot's C = 0.5", "sensitivity"), ("R2", "Author keywords", "lower"),
            ("R6", "topic100 (MiniLM) + LLM topic", "coarse"), ("R6b", "topic100 (bge) + LLM topic", "coarse"),
            ("R4", "Unmasked abstract, bge", "upper (leaky)")]
    rows = []
    for rp, lbl, role in reps:
        sub = t[t["rep"] == rp].set_index("design")
        if not len(sub):
            continue

        def sh(dz):
            if dz not in sub.index or pd.isna(sub.loc[dz, "content_share"]):
                return "—"
            q = sub.loc[dz]
            return fci(q["content_share"], q["content_share_lo"], q["content_share_hi"])

        def au(dz):
            return fnum(sub.loc[dz, "auc_mean"], 3) if dz in sub.index else "—"

        ur = "—"
        if "rolling" in sub.index and pd.notna(sub.loc["rolling", "diff"]):
            q = sub.loc["rolling"]
            ur = fci(q["diff"], q["diff_lo"], q["diff_hi"], d=2, signed=True, pct=True)
        rows.append({"Rep.": rp, "Representation": lbl, "Role": role,
                     "Share, fixed window": sh("fixed"), "Share, rolling": sh("rolling"),
                     "Share, placebo (2023)": sh("placebo"),
                     "AUC fixed / rolling": f"{au('fixed')} / {au('rolling')}", "Δu (pp/yr)": ur})
    df = pd.DataFrame(rows)
    write_table(df, "table3_content_bracket",
                "Content-counterfactual bracket: share of the NAME rise predicted by abstract content, by representation and design.",
                "tab:content", "l l l l l l l l", size=r"\scriptsize",
                notes=("Fixed window: L2 logit trained on 2021-23, intercept recalibrated to 2023, share of the 2023-26 "
                       "rise. Rolling: one-step-ahead models trained on y-3..y-1, recalibrated to y-1; share of the summed "
                       "2024-26 annual changes. Placebo: trained 2018-20, share of the 2020-23 rise. C chosen by 5-fold CV "
                       "except R1@0.5. AUC: out-of-sample, mean over test years. CIs: conditional paper bootstrap "
                       "(B = 2000). Claims use the name-masked rows only (R1, R3, R5); R4 leaks names and is an upper "
                       "bound, R2 and R6 are coarse lower brackets."))
    return ("Content-counterfactual bracket: share of the NAME rise predicted by each abstract representation (name-masked "
            "R1/R3/R5, coarse and leaky brackets) in the fixed, rolling and placebo designs, with out-of-sample AUC and "
            "the implied acceleration of unexplained drift.")


# ==============================================================================================
# Table 4: stage gains and the camera-ready audit (D4 + WP4)
# ==============================================================================================
def table4() -> str:
    g = rc(D4 / "gains.csv")
    g = g[(g["variant"] == "primary") & (g["pooling"] == "std") & (g["period"] == "2024-26")].set_index(["feature", "gain"])
    pv = rc(D4 / "prevalence_by_stage.csv")
    pv = pv[(pv["variant"] == "primary") & (pv["pooling"] == "std") & (pv["period"] == "2024-26") &
            (pv["stage"] == "s0")].set_index("feature")["prev"]
    tp = rc(SNAP / "T4_2_tipping_points.csv").set_index("feature")
    ab = rc(SNAP / "abstract_audit.csv").set_index("feature")
    for f_, src in (("F24", "F24"), ("emdash", "abs_emdash")):   # abstract audit (arXiv v1 abstracts)
        if src in ab.index:
            q = ab.loc[src]
            tp.loc[f_, ["auditable", "did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp", "G_dec_identified"]] = [
                bool(q["auditable"]), q["tp_did_pp"], q["tp_did_lo_pp"], q["tp_did_hi_pp"], q["tp_tip_dec_pp"],
                bool(q["tp_G_dec_identified"])]
    feats = ["NAME", "compound", "phrase_colon", "mixed_case_name", "title_case", "all_caps_title", "sentence_case",
             "question_opener", "O_union", "title_typo", "R24", "R26", "F24", "F26", "emdash", "style_density", "L_union"]
    setname = {"M": "Mainstream (M)", "O": "Outsider (O)", "L": "LLM-style (L)"}
    rows = []
    for f in feats:
        if (f, "total") not in g.index:
            continue

        def gg(st, d=3):
            q = g.loc[(f, st)]
            return fnum(q["est"], d)

        tq = g.loc[(f, "total")]
        aud = tp.loc[f] if f in tp.index else None
        prev = pv.get(f, np.nan)
        rows.append({"set": setname[SET_OF[f]], "Feature": FEAT_LABEL[f],
                     "Share, all (%)": (f"{prev:.2f} (mean)" if f == "style_density" else f"{prev * 100:.1f}"),
                     "Desk": gg("desk"), "Exit": gg("exit"), "Decision": gg("dec"),
                     "Total (accepted/all)": fci(tq["est"], tq["lo95"], tq["hi95"], d=3),
                     "Audit": ("—" if aud is None else ("yes" if bool(aud["auditable"]) else "no")),
                     "Net-flip DiD (pp)": ("—" if aud is None else fci(aud["did_pp"], aud["did_lo_pp"], aud["did_hi_pp"],
                                                                     d=1, signed=True)),
                     "D* (pp)": ("—" if aud is None else fnum(aud["tip_dec_pp"], 2, signed=True)),
                     "G_dec identified": ("—" if aud is None else ("yes" if bool(aud["G_dec_identified"]) else "no"))})
    df = pd.DataFrame(rows)
    write_table(df, "table4_filter_audit",
                "Stage-wise filter gains, ICLR 2024-26, and the camera-ready audit of the decision stage.",
                "tab:filter", "l r r r r l l l l l", group_col="set", size=r"\scriptsize",
                notes=("Gains are P(feature | passed stage)/P(feature | entered stage), year-standardised over 2024-26; "
                       "total = accepted/all; 95% CIs from a paper bootstrap stratified by year (B = 2000). Style density "
                       "is a mean (words per abstract), its gains are ratios of means. Audit: pre-decision arXiv v1 vs "
                       "stored title (abstract for F24 and em dash), accepted minus rejected net flips (pseudo-flip Wald 95% CI); a feature "
                       "is auditable with >= 10 v1-present titles in both arms. D*: net-flip DiD that would bring the "
                       "decision gain to 1; the gain is identified only if D* lies outside the DiD CI. The abstract em "
                       "dash cannot be audited (arXiv renders TeX dashes). — = not audited (union, density or "
                       "typography-inclusive measures)."))
    return ("Stage-wise filter gains (desk, exit, decision, total) for mainstream, outsider and LLM-style features in "
            "2024-26, with the camera-ready audit's net-flip DiD and tipping point for each auditable feature.")


# ==============================================================================================
def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TAB_DIR.mkdir(parents=True, exist_ok=True)
    caps = {}
    for name, fn in (("fig1_naming_turn", fig1), ("fig2_decomposition", fig2), ("fig3_carriers", fig3),
                     ("fig4_register", fig4), ("fig5_stage_gains", fig5), ("fig6_published_bias", fig6),
                     ("table1_hypotheses", table1), ("table2_acceleration", table2),
                     ("table3_content_bracket", table3), ("table4_filter_audit", table4)):
        caps[name] = fn()
        print(f"[ok] {name}")
    manifest = {"generated": _dt.datetime.now().isoformat(timespec="seconds"),
                "script": "src/analyses/figures.py",
                "captions": caps,
                "rendered_size_in": {k: {"width": v[0], "height": v[1]} for k, v in WIDTHS.items()},
                "inputs_mtime": dict(sorted(_INPUTS.items()))}
    (FIG_DIR / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
    for k, v in caps.items():
        print(f"\n{k}: {v}")


if __name__ == "__main__":
    main()
