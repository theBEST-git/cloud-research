"""PH6 waves (post hoc; declared in PREREGISTRATION.md on 2026-10-28 before it was run; it uses the PH5 entry point,
`ICLR_CORPUS=pooled python research/fashion/posthoc.py ph5 waves`): does a keyword's acceptance gap fall after its
submission share has peaked? Exploratory association, not an effect of choosing a keyword.

Waves (outcome-free; frozen in WAVES and re-derived and asserted at run time):
  vocabulary  PH4's K set: author keywords typed research_area / specific_topic / property / application_domain used
              by >= 200 discovery submissions (68)
  share       share_k(t) = discovery submissions (with text) listing k in year t / all of them, t = 2018..2026
  wave        peak year p_k = argmax share in 2019..2024, min share before p_k <= 0.5 x peak, share in 2026 <= 0.5 x
              peak (a rise and a fall). 17 keywords. INSPECTED: the six whose per-year PH4 gaps were viewed before this
              declaration (they suggested the question)
Acceptance (gated): per split (discovery; confirmation = the released held-out papers), the RQ3 decided papers of
2018-2026. Per wave k and year t, gap g = acceptance of k's papers minus that of all other decided papers of the same
split and year, variance from rates shrunk to (k + 0.5) / (n + 1) (as PH4).
  Delta_k     paper-weighted mean gap over the years after the peak (t > p_k) minus that over the years up to it
  D           sum_k w_k Delta_k / sum_k w_k, w_k = N_pre N_post / (N_pre + N_post) (decided papers of k before / after)
  inference   PERMS within-year permutations of acceptance inside the split's population (seed SEED): one-sided
              p_less = (1 + #D_perm <= D) / (PERMS + 1), two-sided p = (1 + #|D_perm| >= |D|) / (PERMS + 1); 95%
              interval D +- 1.96 SD(D_perm); MDE80 (one-sided 0.05) = 2.486 SD(D_perm); binomial SE alongside
  variants    all 17 (primary); without the six INSPECTED; without federated learning
Declared test: held-out (confirmation) D < 0, one-sided p_less < 0.05 on all 17 waves; not supported with |D| below
its MDE80 = uninformative. Discovery D is reported but is not a test (the question came from discovery cells).
Descriptive: Delta_k per keyword and split; event-time profile (gap minus the keyword's own paper-weighted level, by
years since the peak, pooled over waves, paper-weighted).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from common import TOPICS, topic_layer

TYPES = ("research_area", "specific_topic", "property", "application_domain")
MIN_PAPERS, YEARS, PEAK_RANGE, RISE, FALL = 200, (2018, 2026), (2019, 2024), 0.5, 0.5
WAVES = ("adversarial attack", "semi-supervised learning", "robustness", "representation learning",
         "data augmentation", "adversarial robustness", "graph neural networks", "multi-agent reinforcement learning",
         "optimal transport", "vision transformer", "federated learning", "contrastive learning",
         "differential privacy", "offline reinforcement learning", "self-supervised learning", "fairness",
         "explainability")
INSPECTED = ("adversarial attack", "adversarial robustness", "graph neural networks", "federated learning",
             "contrastive learning", "self-supervised learning")
VARIANTS = {"all": (), "without_inspected": INSPECTED, "without_federated_learning": ("federated learning",)}
PERMS, SEED, MDE_FACTOR = 2000, 20261028, stats.norm.ppf(0.95) + stats.norm.ppf(0.80)
SPLITS = ("discovery", "confirmation")


def wave_table() -> pd.DataFrame:
    """Share profile of every vocabulary keyword over the discovery submissions with text. Reads no outcome."""
    kt = pd.read_csv(TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = kt[kt.type.isin(TYPES) & (kt.papers >= MIN_PAPERS)].sort_values("papers", ascending=False).keyword
    c = topic_layer().embedded_corpus()
    if "split" in c:
        c = c[c.split == "discovery"]
    c = c[c.year.between(*YEARS)]
    years = np.arange(YEARS[0], YEARS[1] + 1)
    total = c.groupby("year").size().reindex(years).to_numpy(float)
    rows = []
    for kw in vocab:
        n = c[c.keywords.apply(lambda s, kw=kw: kw in s)].groupby("year").size().reindex(years, fill_value=0)
        share = n.to_numpy(float) / total
        p, peak = int(years[np.argmax(share)]), float(share.max())
        pre = share[years < p]
        rows.append({"keyword": kw, "papers": int(n.sum()), "peak_year": p, "peak_share": peak,
                     "pre_min_ratio": float(pre.min()) / peak if len(pre) else np.nan,
                     "share_2026_ratio": float(share[-1]) / peak, **{f"share_{y}": s for y, s in zip(years, share)}})
    t = pd.DataFrame(rows)
    t["wave"] = t.peak_year.between(*PEAK_RANGE) & (t.pre_min_ratio <= RISE) & (t.share_2026_ratio <= FALL)
    return t


def gaps(member: np.ndarray, year_idx: np.ndarray, acc: np.ndarray, n_years: int):
    """Per wave and year: the wave's decided papers n1, the gap g and its variance (NaN where a side is empty)."""
    Y = np.zeros((len(year_idx), n_years))
    Y[np.arange(len(year_idx)), year_idx] = 1.0
    M = member.astype(float)
    n1, k1 = M.T @ Y, M.T @ (Y * acc[:, None])
    n0, k0 = Y.sum(axis=0) - n1, (Y * acc[:, None]).sum(axis=0) - k1
    ok = (n1 > 0) & (n0 > 0)
    s1, s0 = (k1 + 0.5) / (n1 + 1), (k0 + 0.5) / (n0 + 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(ok, k1 / n1 - k0 / n0, np.nan)
        var = np.where(ok, s1 * (1 - s1) / n1 + s0 * (1 - s0) / n0, np.nan)
    return np.where(ok, n1, 0.0), g, var


def delta(n1: np.ndarray, g: np.ndarray, var: np.ndarray, post: np.ndarray):
    """Delta_k (post minus pre paper-weighted mean gap), its binomial variance, and w_k; arrays over waves."""
    def side(mask):
        w = np.where(mask, n1, 0.0)
        N = w.sum(axis=1)
        with np.errstate(divide="ignore", invalid="ignore"):
            w = w / N[:, None]
        return np.nansum(w * np.nan_to_num(g), axis=1), np.nansum(w ** 2 * np.nan_to_num(var), axis=1), N
    pre_m, pre_v, N_pre = side(~post)
    post_m, post_v, N_post = side(post)
    with np.errstate(divide="ignore", invalid="ignore"):
        w = np.where((N_pre > 0) & (N_post > 0), N_pre * N_post / (N_pre + N_post), 0.0)
    return post_m - pre_m, pre_v + post_v, w, N_pre, N_post


def pooled(d: np.ndarray, v: np.ndarray, w: np.ndarray, keep: np.ndarray) -> tuple[float, float]:
    w = np.where(keep, w, 0.0)
    return float(np.sum(w * np.nan_to_num(d)) / w.sum()), float(np.sqrt(np.sum(w ** 2 * np.nan_to_num(v))) / w.sum())


def compute(k: pd.DataFrame) -> dict:
    table = wave_table()
    waves = tuple(table[table.wave].sort_values(["peak_year", "keyword"]).keyword)
    assert set(waves) == set(WAVES), f"wave list drifted: {sorted(set(waves) ^ set(WAVES))}"
    names = list(WAVES)
    peaks = table.set_index("keyword").peak_year.reindex(names).to_numpy()
    corpus = topic_layer().embedded_corpus().set_index("submission_id")
    kw = corpus.keywords.reindex(k.submission_id.to_numpy())
    split = (corpus.split.reindex(k.submission_id.to_numpy()).to_numpy() if "split" in corpus
             else np.full(len(k), "discovery"))
    years = np.arange(YEARS[0], YEARS[1] + 1)
    post = years[None, :] > peaks[:, None]
    rng = np.random.default_rng(SEED)
    tests, per_kw, cells, profile = [], [], [], []
    for s in SPLITS:
        pop = (k.rq3.to_numpy(bool) & k.year.between(*YEARS).to_numpy() & (split == s))
        if pop.sum() == 0:
            continue
        sub = k[pop]
        lists = kw[pop].to_numpy()
        M = np.array([[w in (x if isinstance(x, (set, list, tuple)) else ()) for w in names] for x in lists], dtype=bool)
        yi = sub.year.to_numpy() - YEARS[0]
        acc = sub.accepted.to_numpy(float)
        n1, g, var = gaps(M, yi, acc, len(years))
        d, v, w, N_pre, N_post = delta(n1, g, var, post)
        groups = [np.flatnonzero(yi == j) for j in range(len(years))]
        perm = np.empty((PERMS, len(names)))
        for r in range(PERMS):
            a = acc.copy()
            for idx in groups:
                a[idx] = acc[rng.permutation(idx)]
            pn1, pg, pv = gaps(M, yi, a, len(years))
            perm[r] = delta(pn1, pg, pv, post)[0]
        for variant, drop in VARIANTS.items():
            keep = ~np.isin(names, drop)
            D, se = pooled(d, v, w, keep)
            wk = np.where(keep, w, 0.0)
            Dp = (perm * wk[None, :]).sum(axis=1) / wk.sum()
            sd = float(Dp.std(ddof=1))
            tests.append({"split": s, "variant": variant, "waves": int(keep.sum()), "D": D, "se_binomial": se,
                          "sd_perm": sd, "ci95_lo": D - 1.96 * sd, "ci95_hi": D + 1.96 * sd,
                          "p_less": float((1 + np.sum(Dp <= D)) / (PERMS + 1)),
                          "p_two_sided": float((1 + np.sum(np.abs(Dp) >= abs(D))) / (PERMS + 1)),
                          "mde80": MDE_FACTOR * sd, "papers_pre": int(N_pre[keep].sum()),
                          "papers_post": int(N_post[keep].sum()), "decided_papers": int(pop.sum())})
        for i, name in enumerate(names):
            per_kw.append({"split": s, "keyword": name, "peak_year": int(peaks[i]), "inspected": name in INSPECTED,
                           "delta": d[i], "delta_se": float(np.sqrt(v[i])), "weight": w[i],
                           "papers_pre": int(N_pre[i]), "papers_post": int(N_post[i])})
            level = np.nansum(np.nan_to_num(g[i]) * n1[i]) / n1[i].sum() if n1[i].sum() > 0 else np.nan
            for j, y in enumerate(years):
                cells.append({"split": s, "keyword": name, "year": int(y), "rel_year": int(y - peaks[i]),
                              "papers": int(n1[i, j]), "gap": g[i, j], "gap_se": float(np.sqrt(var[i, j])),
                              "gap_minus_level": g[i, j] - level})
        c = pd.DataFrame(cells)
        c = c[(c.split == s) & (c.papers > 0)]
        for r, grp in c.groupby("rel_year"):
            profile.append({"split": s, "rel_year": int(r), "waves": int(grp.keyword.nunique()),
                            "papers": int(grp.papers.sum()),
                            "gap_minus_level": float(np.average(grp.gap_minus_level, weights=grp.papers))})
    tests = pd.DataFrame(tests)
    settings = {"waves": names, "inspected": list(INSPECTED), "perms": PERMS, "seed": SEED,
                "years": list(YEARS), "peak_range": list(PEAK_RANGE), "rise": RISE, "fall": FALL,
                "declared_test": "confirmation, variant all: D < 0, one-sided p_less < 0.05",
                "note": "post hoc (declared before the run); associations, not effects of keyword choice"}
    held = tests[(tests.split == "confirmation") & (tests.variant == "all")]
    if len(held):
        h = held.iloc[0]
        verdict = "supported" if (h.D < 0 and h.p_less < 0.05) else (
            "not supported (uninformative: |D| < MDE80)" if abs(h.D) < h.mde80 else "not supported")
        settings["held_out_verdict"] = verdict
    return {"tests": tests, "keywords": pd.DataFrame(per_kw), "cells": pd.DataFrame(cells),
            "profile": pd.DataFrame(profile), "wave_table": table, "settings": settings}


def plot(out_dir: Path) -> None:
    """Per-wave Delta (discovery, held-out) and the pooled event-time profile, from the saved outputs only."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    kw = pd.read_csv(out_dir / "keywords.csv")
    prof = pd.read_csv(out_dir / "profile.csv")
    tests = pd.read_csv(out_dir / "tests.csv")
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 5.2), gridspec_kw={"width_ratios": [1.25, 1]})
    order = kw[kw.split == "discovery"].sort_values("delta").keyword.tolist()
    for off, (s, colour) in zip((-0.18, 0.18), [("discovery", "#2a78d6"), ("confirmation", "#eb6834")]):
        part = kw[kw.split == s].set_index("keyword").reindex(order)
        if part.delta.isna().all():
            continue
        y = np.arange(len(order)) + off
        a.errorbar(100 * part.delta, y, xerr=196 * part.delta_se, fmt="o", ms=4, color=colour, lw=1,
                   label="held-out" if s == "confirmation" else s)
    a.axvline(0, color="#3a3a38", lw=1)
    a.set_yticks(np.arange(len(order)), [o + (" *" if o in INSPECTED else "") for o in order], fontsize=8)
    a.set_xlabel("Gap after peak minus gap up to peak (pp, 95% CI)")
    a.set_title("(a) Per wave (* = inspected before declaration)", fontsize=10, loc="left")
    a.legend(fontsize=8, frameon=False)
    for s, colour in [("discovery", "#2a78d6"), ("confirmation", "#eb6834")]:
        p = prof[(prof.split == s) & prof.rel_year.between(-5, 5)]
        if len(p):
            b.plot(p.rel_year, 100 * p.gap_minus_level, "o-", color=colour,
                   label="held-out" if s == "confirmation" else s)
    b.axhline(0, color="#3a3a38", lw=1)
    b.axvline(0.5, color="#7a7974", lw=1, ls=":")
    b.set_xlabel("Years since the wave's share peak")
    b.set_ylabel("Gap minus the wave's own level (pp)")
    b.set_title("(b) Pooled over waves (descriptive)", fontsize=10, loc="left")
    b.legend(fontsize=8, frameon=False)
    t = tests[tests.variant == "all"].set_index("split")
    note = "; ".join(f"{'held-out' if s == 'confirmation' else s} D = {100 * r.D:+.1f} pp (one-sided p {r.p_less:.3f})"
                     for s, r in t.iterrows())
    fig.suptitle(f"PH6 waves (post hoc): {note}", fontsize=10)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(out_dir / f"PH6_waves.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(json.dumps(tests.round(4).to_dict(orient="records"), indent=1))
