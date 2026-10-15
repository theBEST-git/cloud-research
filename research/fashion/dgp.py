"""Synthetic binary outcomes for dry-runs (PREREGISTRATION.md D12, D13). Uses no real outcome.

simulate(frame, dgp, rng): P(y = 1) = base + topic intercept + year effect + topic-specific linear trend
+ topic-year shock + sum_k delta_k * (x_k - mean x_k), clipped to [0.005, 0.995]. Topics and years come from the
frame's map, so clustered structure that the analysis map only partly captures can be simulated by choosing another
map. Planted effects (delta) are in probability points per unit of the regressor; because of clipping, the effect
actually planted is measured separately (the dry-run regresses the true probability on the regressor).

calibrate(frame, column): method-of-moments variance components of ONE observed binary column from its own topic-year
cell means (no regressor is involved): year effects, topic intercepts, topic-specific linear trends, and cell shocks
beyond binomial noise.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DGP:
    base: float
    sd_topic: float = 0.05
    sd_year: float = 0.02
    sd_trend: float = 0.008        # per year
    sd_cell: float = 0.02
    effects: dict = field(default_factory=dict, hash=False, compare=False)


def calibrate(frame: pd.DataFrame, column: str, years: tuple[int, int]) -> DGP:
    d = frame[frame.year.between(*years)].dropna(subset=[column])
    g = d.groupby(["topic", "year"])[column].agg(["mean", "size"]).reset_index()
    m, n = g["mean"].to_numpy(), g["size"].to_numpy(float)
    r = m.copy()
    a = pd.Series(0.0, index=g.topic.unique())
    b = pd.Series(0.0, index=sorted(g.year.unique()))
    for _ in range(50):                                        # weighted two-way demeaning of the cell means
        a = pd.Series(m - b.reindex(g.year).to_numpy()).groupby(g.topic.values).apply(
            lambda s_: np.average(s_, weights=n[s_.index]))
        b = pd.Series(m - a.reindex(g.topic).to_numpy()).groupby(g.year.values).apply(
            lambda s_: np.average(s_, weights=n[s_.index]))
    r = m - a.reindex(g.topic).to_numpy() - b.reindex(g.year).to_numpy()
    noise = m * (1 - m) / n
    slopes, resid = [], np.zeros_like(r)
    for t, idx in g.groupby("topic").groups.items():
        idx = np.asarray(idx)
        yy = g.year.to_numpy()[idx].astype(float)
        if len(idx) < 3:
            resid[idx] = r[idx]
            continue
        w = n[idx]
        xc = yy - np.average(yy, weights=w)
        c = np.sum(w * xc * r[idx]) / np.sum(w * xc ** 2)
        resid[idx] = r[idx] - c * xc
        slopes.append((c, w, xc, idx))
    keep = 1 - (len(a) + len(b) + len(slopes)) / len(r)      # share of variation left after the fitted terms
    var_cell = max(0.0, (np.sum(n * resid ** 2) - keep * np.sum(n * noise)) / (keep * np.sum(n)))
    cs = np.array([c for c, *_ in slopes])
    noise_c = np.array([np.sum(w ** 2 * xc ** 2 * (noise[idx] + var_cell)) / np.sum(w * xc ** 2) ** 2
                        for _, w, xc, idx in slopes])
    var_trend = max(0.0, cs.var() - noise_c.mean())
    return DGP(base=float(d[column].mean()), sd_topic=float(a.std()), sd_year=float(b.std()),
               sd_trend=float(np.sqrt(var_trend)), sd_cell=float(np.sqrt(var_cell)))


def simulate(frame: pd.DataFrame, dgp: DGP, rng: np.random.Generator, return_p: bool = False):
    topics, t_idx = np.unique(frame.topic.to_numpy(), return_inverse=True)
    years, y_idx = np.unique(frame.year.to_numpy(), return_inverse=True)
    cells, c_idx = np.unique(frame.topic.astype(str).to_numpy() + ":" + frame.year.astype(str).to_numpy(), return_inverse=True)
    p = (dgp.base + rng.normal(0, dgp.sd_topic, len(topics))[t_idx] + rng.normal(0, dgp.sd_year, len(years))[y_idx]
         + rng.normal(0, dgp.sd_trend, len(topics))[t_idx] * (frame.year.to_numpy() - frame.year.mean())
         + rng.normal(0, dgp.sd_cell, len(cells))[c_idx])
    for col, delta in dgp.effects.items():
        x = frame[col].to_numpy(float)
        p = p + delta * (np.nan_to_num(x, nan=np.nanmean(x)) - np.nanmean(x))
    p = np.clip(p, 0.005, 0.995)
    y = (rng.random(len(p)) < p).astype(float)
    return (y, p) if return_p else y
