"""Derived exploration variables shared by the fashion analyses (all within-year percentiles)."""
import numpy as np
import pandas as pd

from fashion.explore import load as _load


def prep(min_year=2019):
    f = _load()
    f = f[f.year >= min_year].copy()
    pct = lambda c: f.groupby("year")[c].transform(lambda s: s.rank(pct=True))
    f["size_p"], f["mom_p"] = pct("loc1"), pct("loc_mom")
    f["gcur"] = np.log((f.loc_cur + 1) / (f.loc1 + 1))
    f["gcur_p"] = pct("gcur")
    f["lloc1"] = np.log1p(f.loc1)
    f["nn_res"] = np.nan
    for _, g in f.groupby("year"):
        ok = g.nn_prev.notna()
        b = np.polyfit(g.lloc1[ok], g.nn_prev[ok], 2)
        f.loc[g.index[ok], "nn_res"] = g.nn_prev[ok] - np.polyval(b, g.lloc1[ok])
    f["nnr_p"] = pct("nn_res")
    ter = lambda c: pd.cut(f[c], [0, 1 / 3, 2 / 3, 1.0001], labels=["lo", "mid", "hi"], include_lowest=True)
    f["size3"], f["mom3"], f["nnr3"], f["gcur3"] = ter("size_p"), ter("mom_p"), ter("nnr_p"), ter("gcur_p")
    f["exp3"] = pd.cut(np.expm1(f.lprior_acc), [-1, 0, 2, 1000], labels=["0", "1-2", "3+"])
    return f
