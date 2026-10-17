"""Shared helpers for the final post hoc round (PH5; PREREGISTRATION.md, declared before running).

Each PH5 analysis lives in its own module ph5_<slug>.py with
    compute(k: pd.DataFrame) -> dict[str, pd.DataFrame | dict]      # k = outcome_frame() or simulated_frame()
    plot(out_dir: Path) -> None                                     # reads only the saved outputs
and is run once, for real, by `python research/fashion/posthoc.py ph5 <slug>` (the only entry point that may read
real outcomes; outcomes.require_posthoc). Analyses that need no outcome may also expose compute_free().

During development, modules are built and tested on simulated_frame(): the real papers, topics, years, labels and
authors, with acceptance drawn at random (null), optionally with a planted effect, so a method can be checked for size
and for recovering a known effect without ever seeing a real outcome.
"""
from __future__ import annotations

from typing import Callable

import numpy as np
import pandas as pd

import panel

POSTHOC_COLUMNS = ["rq3", "accepted", "s9", "s9_accepted", "e3", "withdrawn_after_review", "withdrawn_before_review"]


def _attach(k: pd.DataFrame, out: pd.DataFrame) -> pd.DataFrame:
    assert (out.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    return k.assign(**{c: out[c].to_numpy() for c in POSTHOC_COLUMNS})


def outcome_frame() -> pd.DataFrame:
    """The k100 paper frame with every post hoc outcome column. Only works inside a gated posthoc.py run."""
    import outcomes
    k = panel.frame("k100").reset_index(drop=True)
    return _attach(k, outcomes.load("posthoc", k.submission_id))


def fake_outcomes(k: pd.DataFrame, seed: int = 0,
                  planted: Callable[[pd.DataFrame], np.ndarray] | None = None) -> pd.DataFrame:
    """Simulated outcome columns for the papers of k (no real outcome is read).

    rq3 (decided) ~ 74% of papers; withdrawals after/before review ~ 15% / 7%; acceptance ~ Bernoulli with a
    year-specific base rate (0.30-0.45) on the logit scale plus planted(k) (a log-odds shift per paper, default 0).
    """
    rng = np.random.default_rng(seed)
    n = len(k)
    years = k.year.to_numpy()
    base = {y: r for y, r in zip(range(2017, 2027), np.linspace(0.45, 0.32, 10))}
    logit = np.log([base.get(y, 0.4) / (1 - base.get(y, 0.4)) for y in years])
    if planted is not None:
        logit = logit + np.asarray(planted(k), float)
    y = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(float)
    u, w = rng.random(n), rng.random(n)
    out = pd.DataFrame({"submission_id": k.submission_id.to_numpy(), "year": years})
    out["rq3"] = u < 0.74
    out["accepted"] = np.where(out.rq3, y, np.nan)
    after = ~out.rq3 & (w < 0.58)
    out["s9"] = out.rq3 | after
    out["s9_accepted"] = np.where(out.rq3, y, np.where(after, 0.0, np.nan))
    out["e3"] = True
    out["withdrawn_after_review"] = after.astype(float)
    out["withdrawn_before_review"] = (~out.rq3 & ~after).astype(float)
    return out


def simulated_frame(seed: int = 0, planted: Callable[[pd.DataFrame], np.ndarray] | None = None) -> pd.DataFrame:
    """The real k100 paper frame with simulated outcome columns (development and tests only)."""
    k = panel.frame("k100").reset_index(drop=True)
    return _attach(k, fake_outcomes(k, seed, planted))


def bh(p: pd.Series) -> pd.Series:
    """Benjamini-Hochberg q-values; NaN stays NaN (same as posthoc.bh)."""
    ok = p.dropna()
    out = pd.Series(np.nan, index=p.index, dtype=float)
    if ok.empty:
        return out
    order = np.argsort(ok.to_numpy(), kind="stable")
    ps = ok.to_numpy()[order]
    m = len(ps)
    q = np.minimum.accumulate((ps * m / np.arange(1, m + 1))[::-1])[::-1].clip(max=1.0)
    adj = np.empty(m)
    adj[order] = q
    out.loc[ok.index] = adj
    return out
