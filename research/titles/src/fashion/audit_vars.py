"""Audit: build alternative heat measures from audit/loc_variants.parquet (see audit_loc.py).

Suffixes: _nt = same-team neighbours removed (shared declared author key in t-1/t-2; nn = closest non-team
predecessor); _78/_82/_85 = cosine threshold; _13 = momentum t-3 -> t-1 (instead of t-2 -> t-1); _nd = closest
predecessor below cos 0.95 (no near-duplicates).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.audit_common import AUD, load, nn_resid, pctl


def with_variants():
    f = load()
    v = pd.read_parquet(AUD / "loc_variants.parquet").drop(columns="year")
    f = f.merge(v, on="submission_id", how="left")
    Nall = pd.read_parquet(C.OUT / "fashion" / "frame2.parquet", columns=["year"]).year.value_counts().to_dict()
    N1 = f.year.map(lambda y: Nall[y - 1]).astype(float)
    N2 = f.year.map(lambda y: Nall[y - 2]).astype(float)
    N3 = f.year.map(lambda y: Nall.get(y - 3, np.nan)).astype(float)
    f["c1_nt"], f["c2_nt"] = f.c1_80 - f.c1_team, f.c2_80 - f.c2_team
    f["n12"] = f.c1_80 + f.c2_80

    def build(sfx, c1, c2, nn):
        f[f"loc1{sfx}"] = 1000 * c1 / N1
        f[f"locmom{sfx}"] = np.log((c1 + 1) / N1) - np.log((c2 + 1) / N2)
        f[f"size_p{sfx}"] = pctl(f, f"loc1{sfx}")
        f[f"mom_p{sfx}"] = pctl(f, f"locmom{sfx}")
        f[f"nnres{sfx}"] = nn_resid(f, nn, f"loc1{sfx}")
        f[f"nnr_p{sfx}"] = pctl(f, f"nnres{sfx}")

    build("_nt", f.c1_nt, f.c2_nt, "nn_nt")
    for tau in (78, 82, 85):
        build(f"_{tau}", f[f"c1_{tau}"], f[f"c2_{tau}"], "nn_prev")
    # t-3 -> t-1 momentum (2020+); size and nn as in the main frame
    f["locmom_13"] = np.log((f.c1_80 + 1) / N1) - np.log((f.c3_80 + 1) / N3)
    f["mom_p_13"] = pctl(f, "locmom_13")
    f["size_p_13"], f["nnr_p_13"] = f.size_p, f.nnr_p
    # near-duplicate-free nearest predecessor
    f["nnres_nd"] = nn_resid(f, "nn_nd", "loc1")
    f["nnr_p_nd"] = pctl(f, "nnres_nd")
    f["size_p_nd"], f["mom_p_nd"] = f.size_p, f.mom_p
    f["hub_p"] = pctl(f, "hub1")
    return f
