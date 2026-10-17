"""Shared loader and model helpers for the adversarial audit of the fashion findings (discovery data only).

load() = prep() (2019+) merged with insider.parquet, ins/ent dummies, area_h, and optional recomputed locality
measures from the audit cache (scratch parquet written by audit_loc.py).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from fashion._prep import prep

AUD = C.OUT / "fashion" / "explore" / "audit"
RHS = "size_p + mom_p + nnr_p + log_authors"


def load():
    f = prep()
    ins = pd.read_parquet(C.OUT / "fashion" / "insider.parquet")
    f = f.merge(ins, on="submission_id", how="left")
    f["ins"] = (f.entry == "insider").astype(float)
    f["ent"] = (f.entry == "entrant").astype(float)
    f["new"] = (f.entry == "newcomer").astype(float)
    for c in ["ins", "ent", "new"]:
        f.loc[f.entry.isna(), c] = np.nan
    u = C.load_universe(["submission_id", "area_h"])
    f = f.merge(u, on="submission_id", how="left")
    f["acc_rej"] = np.where(f.ACC | f.REJ, f.ACC.astype(float), np.nan)
    f["llm_topic"] = f.llm_topic.astype(int)
    f["ly"] = f.y  # log1p citations among accepted matched
    f["cy_p"] = f.cite_pct
    return f


def est(d, y, rhs, fe="year", cluster="topic100", terms=None):
    """Return dict term -> (b, se, p, n)."""
    m = pf.feols(f"{y} ~ {rhs} | {fe}", data=d, vcov={"CRV1": cluster})
    t = m.tidy()
    out = {}
    for k in (terms or t.index):
        if k in t.index:
            out[k] = (float(t.loc[k, "Estimate"]), float(t.loc[k, "Std. Error"]), float(t.loc[k, "Pr(>|t|)"]), int(m._N))
        else:
            out[k] = (np.nan, np.nan, np.nan, int(m._N))
    return out


def fmt(r):
    b, se, p, n = r
    return f"{b:+.3f} ({se:.3f})"


def pctl(f, c):
    return f.groupby("year")[c].transform(lambda s: s.rank(pct=True))


def nn_resid(f, nn="nn_prev", loc="loc1"):
    """Within-year residual of nn on a quadratic in log1p(loc), as in _prep."""
    out = pd.Series(np.nan, index=f.index)
    ll = np.log1p(f[loc])
    for _, g in f.groupby("year"):
        ok = g[nn].notna() & ll[g.index].notna()
        idx = g.index[ok]
        b = np.polyfit(ll[idx], g.loc[idx, nn], 2)
        out[idx] = g.loc[idx, nn] - np.polyval(b, ll[idx])
    return out
