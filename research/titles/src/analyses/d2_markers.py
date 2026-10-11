"""WP6 / D2-H2d: style vs topic channel. Within-stayer change against population change per marker.

Markers (pre-stated before looking at outcomes; PLAN D2-H2d):
  * style: the 61 frozen title markers mk_* (lexicons.json -> d2_style_markers), keeping those with pooled
    paper prevalence >= 0.1% in E u L (the minimum count rule announced in API.md 4.6);
  * topic: MiniLM abstract topic100 clusters whose population share changes by >= 1 pp between E = 2022-23
    and L = 2025-26 (|delta share| >= 0.01), plus llm_topic.
For each marker m: within-stayer change dS_m = P_SL - P_SE and population change d_m = P_L - P_E
(partition any role, rows weighted 1/#keys = paper weighting; last and first position as robustness).

Statistics (key-cluster bootstrap, 1,000 reps, markers fixed):
  * slope of dS on d across all markers (OLS with intercept; pilot 0.97, r = .985), and r;
  * per channel, the through-origin slope b_g = sum(dS d) / sum(d^2) and the generational increment share
    G_g = 1 - b_g ("1 - within/pop"); the aggregate ratio sum(sign(d) dS) / sum(|d|) as a second summary;
  * G_style - G_topic (prediction > 0; falsified if topic is significantly larger).
Audit additions (D2-C5, D2-R14, D2-R19): the d^2 weight share of each marker in its channel's through-origin slope
(markers_weight_shares.csv); a variant dropping both llm_topic and the NAME family; an equal-weight version
(median per-marker rho = dS/d within each channel, over all markers and over markers with |d| >= 1 pp) with
bootstrap CIs; the count of markers on the generational side (|dS| < |d|); F2.1 labels the partition and the
three overlapping NAME variants.

Outputs: outputs/d2_carriers/markers_changes.csv, fig_F2_1_marker_scatter.{pdf,png,csv}, markers_results.json

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_markers [n_boot]
"""
from __future__ import annotations

import json
import sys
import time

import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys, groups_coded, make_specs

OUTDIR = P.OUTDIR
N_BOOT = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
SEED = 20261
MIN_PREV = 0.001
MIN_TOPIC_DSHARE = 0.01


def select_markers(papers: pd.DataFrame) -> tuple[list[str], list[str], pd.DataFrame]:
    EL = papers.year.isin(P.E_WIN + P.L_WIN)
    style_all = [c for c in papers.columns if c.startswith("mk_")]
    prev = papers.loc[EL, style_all].mean()
    style = [c for c in style_all if prev[c] >= MIN_PREV]
    sh = pd.crosstab(papers.loc[EL, "year"].isin(P.L_WIN), papers.loc[EL, "topic100"], normalize="index")
    dsh = sh.loc[True] - sh.loc[False]
    topics = sorted(int(k) for k in dsh.index[dsh.abs() >= MIN_TOPIC_DSHARE])
    sel = pd.DataFrame({"marker": style_all, "channel": "style", "prev_EL": prev.values,
                        "kept": [c in style for c in style_all]})
    sel = pd.concat([sel, pd.DataFrame({"marker": [f"topic_{k}" for k in topics] + ["llm_topic"], "channel": "topic",
                                        "prev_EL": [float((papers.loc[EL, "topic100"] == k).mean()) for k in topics]
                                        + [float(papers.loc[EL, "llm_topic"].mean())],
                                        "kept": True,
                                        "dshare_pop": [float(dsh[k]) for k in topics] + [np.nan]})], ignore_index=True)
    return style, [f"topic_{k}" for k in topics] + ["llm_topic"], sel


def channel_stats(dS: np.ndarray, d: np.ndarray, is_style: np.ndarray) -> dict:
    """dS, d: (B x M). Returns arrays (B,) of summary statistics."""
    out = {}
    dm, sm = d.mean(1, keepdims=True), dS.mean(1, keepdims=True)
    cov = ((d - dm) * (dS - sm)).sum(1)
    vx = ((d - dm) ** 2).sum(1)
    vy = ((dS - sm) ** 2).sum(1)
    out["slope_all"] = cov / vx
    out["intercept_all"] = sm[:, 0] - out["slope_all"] * dm[:, 0]
    out["r_all"] = cov / np.sqrt(vx * vy)
    out["slope0_all"] = (dS * d).sum(1) / (d ** 2).sum(1)
    for g, m in [("style", is_style), ("topic", ~is_style)]:
        x, y = d[:, m], dS[:, m]
        out[f"slope0_{g}"] = (x * y).sum(1) / (x ** 2).sum(1)
        out[f"G_{g}"] = 1 - out[f"slope0_{g}"]
        out[f"ratio_{g}"] = (np.sign(x) * y).sum(1) / np.abs(x).sum(1)
        out[f"Gratio_{g}"] = 1 - out[f"ratio_{g}"]
        xm, ym = x.mean(1, keepdims=True), y.mean(1, keepdims=True)
        out[f"slope_{g}"] = ((x - xm) * (y - ym)).sum(1) / ((x - xm) ** 2).sum(1)
    out["G_style_minus_topic"] = out["G_style"] - out["G_topic"]
    out["Gratio_style_minus_topic"] = out["Gratio_style"] - out["Gratio_topic"]
    return out


NAME_FAMILY = ["mk_name", "mk_name_strict", "mk_name_loose", "mk_compound", "mk_phrase_colon", "mk_name_mixed_case",
               "mk_name_all_caps", "mk_name_word", "mk_name_paren_acronym"]


def subset_stats(dS, d, markers, is_style) -> dict:
    """channel_stats on the full set plus two sensitivity subsets (prefixed)."""
    out = channel_stats(dS, d, is_style)
    m = np.array([x != "llm_topic" for x in markers])
    out.update({f"nollm__{k}": v for k, v in channel_stats(dS[:, m], d[:, m], is_style[m]).items()})
    m = np.array([x not in NAME_FAMILY for x in markers])
    out.update({f"nonamefam__{k}": v for k, v in channel_stats(dS[:, m], d[:, m], is_style[m]).items()})
    m = np.array([x not in NAME_FAMILY and x != "llm_topic" for x in markers])
    out.update({f"nollm_nonamefam__{k}": v for k, v in channel_stats(dS[:, m], d[:, m], is_style[m]).items()})
    # equal-weight summaries: median per-marker rho within channel (all markers; markers with |d| >= 1 pp)
    with np.errstate(divide="ignore", invalid="ignore"):
        rho = dS / d
    for g, cm in [("style", is_style), ("topic", ~is_style)]:
        out[f"median_rho_{g}"] = np.nanmedian(np.where(cm[None, :], rho, np.nan), axis=1)
        big = cm[None, :] & (np.abs(d) >= 0.01)
        out[f"median_rho_big_{g}"] = np.nanmedian(np.where(big, rho, np.nan), axis=1)
    out["median_rho_style_minus_topic"] = out["median_rho_style"] - out["median_rho_topic"]
    out["median_rho_big_style_minus_topic"] = out["median_rho_big_style"] - out["median_rho_big_topic"]
    return out


def summarize(point: dict, boot: dict) -> dict:
    res = {}
    for k, v in point.items():
        b = boot[k][np.isfinite(boot[k])]
        if len(b) < 2:
            continue
        res[k] = dict(est=float(v[0]), se=float(b.std(ddof=1)), lo=float(np.quantile(b, .025)),
                      hi=float(np.quantile(b, .975)), p_le0=float(np.mean(b <= 0)), p_ge0=float(np.mean(b >= 0)))
    return res


def fig_scatter(ch: pd.DataFrame, st: dict):
    fig, axes = C.new_fig("double", height=3.3, ncols=2)
    d = ch[ch.partition.eq("any")].copy()
    d["x"], d["y"] = 100 * d.delta, 100 * d.delta_S
    lab_pts = {"mk_name": "NAME (3 overlapping variants)", "mk_compound": "compound", "mk_title_case": "Title Case",
               "mk_sentence_case": "sentence case", "llm_topic": "LLM topic", "mk_name_mixed_case": "mixed-case NAME",
               "mk_via": "via", "mk_using": "using", "mk_enhanc": "enhanc*", "mk_gerund_opener": "gerund opener",
               "mk_phrase_colon": "phrase colon"}
    for k, ax in enumerate(axes):
        dd = d if k == 0 else d[(d.x.abs() <= 6) & (d.y.abs() <= 6)]
        lim = [min(dd.x.min(), dd.y.min()) - 0.8, max(dd.x.max(), dd.y.max()) + 1.2]
        ax.plot(lim, lim, color=C.GREY, lw=0.8, ls="--", zorder=0)
        for g, c, lab in [("style", C.COLORS[0], "Title style markers"), ("topic", C.COLORS[1], "Abstract topic markers")]:
            s = dd[dd.channel.eq(g)]
            ax.errorbar(s.x, s.y, yerr=[s.y - 100 * s.dS_lo, 100 * s.dS_hi - s.y], fmt="none", ecolor=c, alpha=0.35,
                        lw=0.8)
            ax.plot(s.x, s.y, "o", color=c, ms=5 if k else 4.5, label=f"{lab} (n={len(d[d.channel.eq(g)])})",
                    alpha=0.9, mec="white", mew=0.4)
        keep = lab_pts if k == 0 else {m: v for m, v in lab_pts.items() if m in ("mk_title_case", "mk_sentence_case",
                                                                               "mk_via", "mk_using", "mk_phrase_colon")}
        nudge = {"mk_using": (6, 6), "mk_sentence_case": (6, -10), "mk_title_case": (6, 4), "mk_via": (6, -9),
                 "mk_phrase_colon": (6, 4)} if k == 1 else {}
        if k == 0:
            keep = {m: v for m, v in keep.items() if m in ("mk_name", "mk_compound", "llm_topic", "mk_name_mixed_case",
                                                         "mk_sentence_case")}
        for _, r in dd[dd.marker.isin(keep)].iterrows():
            left = r.marker == "llm_topic"
            off = nudge.get(r.marker, (-5 if left else 4, -6))
            ax.annotate(keep[r.marker], (r.x, r.y), xytext=off, textcoords="offset points",
                        fontsize=6.5, color=C.TEXT2, ha="right" if left else "left",
                        arrowprops=dict(arrowstyle="-", color=C.GREY, lw=0.4) if k == 1 else None)
        ax.set_xlim(lim); ax.set_ylim(lim)
        ax.set_xlabel("Population change, 2022-23 to 2025-26 (pp)")
        ax.set_title("All markers" if k == 0 else "Zoom: |change| \u2264 6 pp", fontsize=8.5)
    axes[0].set_ylabel("Within-stayer change (pp)")
    fig.suptitle("Any-role partition (rows weighted 1/#keys, paper-weighted), E = 2022-23 to L = 2025-26",
                 fontsize=8, color=C.TEXT2, y=1.0)
    fig.text(0.01, -0.02, "Vertical bars: 95% key-cluster bootstrap CIs of the within-stayer change (population change "
             "has its own CI in the CSV). NAME, NAME strict and NAME loose overlap at about (18, 15).",
             fontsize=6.5, color=C.TEXT2, ha="left", va="top")
    sa = st["any"]
    axes[0].text(0.03, 0.97, f"OLS slope {sa['slope_all']['est']:.2f} [{sa['slope_all']['lo']:.2f}, "
                 f"{sa['slope_all']['hi']:.2f}]\nr = {sa['r_all']['est']:.3f}"
                 f"\nStyle: 1 \u2212 b = {sa['G_style']['est']:.2f} [{sa['G_style']['lo']:.2f}, {sa['G_style']['hi']:.2f}]"
                 f"\nTopic: 1 \u2212 b = {sa['G_topic']['est']:.2f} [{sa['G_topic']['lo']:.2f}, {sa['G_topic']['hi']:.2f}]"
                 f"\nDashed: 45\u00b0 line", transform=axes[0].transAxes, va="top", fontsize=7, color=C.TEXT)
    axes[0].legend(loc="lower right", fontsize=6.5)
    C.save_fig(fig, "fig_F2_1_marker_scatter", OUTDIR, data=d)


def main():
    t0 = time.time()
    papers, prof, _ = P.load_panel()
    prof, idx = code_keys(prof)
    K = len(idx)
    style, topic, sel = select_markers(papers)
    for k in [m for m in topic if m.startswith("topic_")]:
        papers[k] = (papers.topic100 == int(k.split("_")[1])).astype(int)
    markers = style + topic
    is_style = np.array([m in style for m in markers])
    g = groups_coded(prof, P.E_WIN, P.L_WIN, idx)
    specs = make_specs(prof, papers, idx, g, tag="markers", outcomes=markers, partitions=("any", "last", "first"))
    print(f"{len(style)} style + {len(topic)} topic markers; {K} keys; bootstrapping {N_BOOT} ...", flush=True)
    res = P.run_specs(specs, K, n_boot=N_BOOT, seed=SEED, chunk=25)
    rows, stats_out, draws = [], {}, {}
    for part in ("any", "last", "first"):
        r = res[f"markers|{part}|paper"]
        dS0 = np.array([[r["point"][m]["delta_S"][0] for m in markers]])
        d0 = np.array([[r["point"][m]["delta"][0] for m in markers]])
        dSb = np.column_stack([r["boot"][m]["delta_S"] for m in markers])
        db = np.column_stack([r["boot"][m]["delta"] for m in markers])
        bst = subset_stats(dSb, db, markers, is_style)
        stats_out[part] = summarize(subset_stats(dS0, d0, markers, is_style), bst)
        draws.update({f"{part}::{k}": v.astype(np.float32) for k, v in bst.items()})
        for j, m in enumerate(markers):
            pt = r["point"][m]
            rows.append(dict(partition=part, marker=m, channel="style" if is_style[j] else "topic",
                             P_E=pt["P_E"][0], P_L=pt["P_L"][0], delta=d0[0, j], delta_S=dS0[0, j],
                             P_SE=pt["P_SE"][0], P_SL=pt["P_SL"][0], rho=pt["rho"][0],
                             d_lo=np.quantile(db[:, j], .025), d_hi=np.quantile(db[:, j], .975),
                             dS_lo=np.quantile(dSb[:, j], .025), dS_hi=np.quantile(dSb[:, j], .975),
                             gap_NS_L=pt["gap_NS_L"][0]))
    ch = pd.DataFrame(rows)
    ch.to_csv(OUTDIR / "markers_changes.csv", index=False)
    ws = []
    for (part, chn), gch in ch.groupby(["partition", "channel"]):
        w2 = gch.delta ** 2
        for _, r in gch.assign(w=w2 / w2.sum()).sort_values("w", ascending=False).iterrows():
            ws.append(dict(partition=part, channel=chn, marker=r.marker, delta=r.delta, delta_S=r.delta_S,
                           weight_share_d2=r.w, generational_side=bool(abs(r.delta_S) < abs(r.delta))))
    ws = pd.DataFrame(ws)
    ws.to_csv(OUTDIR / "markers_weight_shares.csv", index=False)
    sel.to_csv(OUTDIR / "markers_selection.csv", index=False)
    fig_scatter(ch, stats_out)
    out = dict(n_boot=N_BOOT, min_prevalence=MIN_PREV, min_topic_dshare=MIN_TOPIC_DSHARE,
               n_style=len(style), n_topic=len(topic), style_markers=style, topic_markers=topic,
               dropped_style=[m for m in sel.marker[sel.channel.eq("style") & ~sel.kept]],
               stats=stats_out,
               weight_shares_any={chn: {r.marker: round(float(r.weight_share_d2), 4)
                                        for r in ws[(ws.partition == "any") & (ws.channel == chn)].head(6).itertuples()}
                                  for chn in ("style", "topic")},
               n_generational_side={part: {chn: dict(n=int(len(g_)), generational_side=int(g_.generational_side.sum()))
                                           for chn, g_ in ws[ws.partition == part].groupby("channel")}
                                    for part in ("any", "last", "first")},
               elapsed_s=round(time.time() - t0, 1))
    (OUTDIR / "markers_results.json").write_text(json.dumps(out, indent=1))
    np.savez_compressed(OUTDIR / "markers_boot_draws.npz", **draws)
    for part in ("any", "last", "first"):
        s = stats_out[part]
        print(part, {k: (round(v["est"], 3), round(v["lo"], 3), round(v["hi"], 3)) for k, v in s.items()})
    print(f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
