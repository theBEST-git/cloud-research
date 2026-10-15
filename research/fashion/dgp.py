"""Synthetic binary outcomes for dry-runs (PREREGISTRATION.md D12, D13). Uses no real outcome.

simulate(frame, dgp, rng): P(y = 1) = base + topic intercept + year effect + topic-specific linear trend
+ topic-year shock + sum_k delta_k * (x_k - mean x_k), clipped to [0.005, 0.995]. Topics and years come from the
frame's map, so clustered structure that the analysis map only partly captures can be simulated by choosing another
map. Planted effects (delta) are in probability points per unit of the regressor.
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


def simulate(frame: pd.DataFrame, dgp: DGP, rng: np.random.Generator) -> np.ndarray:
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
    return (rng.random(len(p)) < p).astype(float)
