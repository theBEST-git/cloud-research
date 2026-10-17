"""Exploration on the FULL discovery set (no halves; PI decision 2026-10-17: data too small to split).
Claims that survive are frozen in docs/FASHION_PREREG.md and tested once on the held-out confirmation split.

Helpers: year-standardised conditional rates and LPMs with year FE, SEs clustered by topic100 (the unit at which
topic stage varies).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C

OUT = C.OUT / "fashion" / "explore"
STAGES = ["emerging", "growing", "hot_rising", "mature", "steady", "declining"]


def load():
    f = pd.read_parquet(C.OUT / "fashion" / "frame2.parquet")
    rs = pd.read_parquet(C.CACHE / "resubmissions.parquet")
    f["resub"] = f.submission_id.isin(rs.next_submission_id).astype(int)
    f["nov_t"] = f.groupby("year").nov_topic.transform(lambda s: s.rank(pct=True))
    f["nov_ter"] = pd.cut(f.nov_t, [0, 1 / 3, 2 / 3, 1], labels=["low", "mid", "high"])
    f["nov_dec"] = np.ceil(f.nov_t * 10).clip(1, 10)
    f["crowd_t"] = f.groupby("year").crowd_cycle.transform(lambda s: s.rank(pct=True))
    f["crowd_ter"] = pd.cut(f.crowd_t, [0, 1 / 3, 2 / 3, 1], labels=["low", "mid", "high"])
    f["low_cite"] = np.where(f.top10.notna(), (f.cite_pct <= 0.25).astype(float), np.nan)
    return f


def rates(f, by, outcomes=("acc_rev", "top10", "hit", "low_cite"), min_n=30):
    """Year-standardised rate of each outcome within each level of `by` (weights = outcome-population year mix)."""
    rows = []
    for o in outcomes:
        d = f[f[o].notna() & f[by].notna()]
        w = d.year.value_counts(normalize=True)
        g = d.groupby([by, "year"], observed=True)[o].agg(["mean", "size"]).reset_index()
        for lv, gg in g.groupby(by, observed=True):
            gg = gg[gg["size"] >= 1]
            ww = w.reindex(gg.year).to_numpy()
            rows.append({"by": by, "level": lv, "outcome": o, "rate": float((gg["mean"] * ww).sum() / ww.sum()),
                         "raw": float(d.loc[d[by] == lv, o].mean()), "n": int(gg["size"].sum())})
    r = pd.DataFrame(rows)
    return r[r.n >= min_n]


def lpm(d, y, rhs, fe="year", cluster="topic100"):
    m = pf.feols(f"{y} ~ {rhs} | {fe}", data=d, vcov={"CRV1": cluster})
    t = m.tidy()
    t["n"] = m._N
    return t[["Estimate", "Std. Error", "Pr(>|t|)", "2.5%", "97.5%", "n"]]
