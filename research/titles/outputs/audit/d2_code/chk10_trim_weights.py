"""Audit D2: trim_top1pct any-role spec keeps w_any = 1/#keys of the untrimmed paper; check renormalised weights
and the alternative of dropping whole papers that carry a trimmed key."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys, groups_coded
papers, prof, _ = P.load_panel()
prof, idx = code_keys(prof)
g = groups_coded(prof, P.E_WIN, P.L_WIN, idx)
npk = prof.groupby("key_code").size(); top = set(npk.index[npk > npk.quantile(0.99)])
S = set(g.index[g.S])
r = prof[prof.year.isin(P.E_WIN + P.L_WIN)].merge(papers[["submission_id","name_primary"]], on="submission_id")
r["E"] = r.year.isin(P.E_WIN); r["S"] = r.key_code.isin(S)
def rho(x, w):
    m = lambda msk: np.average(x.name_primary[msk], weights=w[msk])
    return (m(~x.E & x.S) - m(x.E & x.S)) / (m(~x.E) - m(x.E))
t = r[~r.key_code.isin(top)]
print("as coded (w_any not renormalised):", round(rho(t, t.w_any), 4))
print("renormalised 1/#remaining keys   :", round(rho(t, 1.0 / t.groupby("submission_id").key_code.transform("size")), 4))
bad = set(r.submission_id[r.key_code.isin(top)])
t2 = r[~r.submission_id.isin(bad)]
print("drop papers with any trimmed key :", round(rho(t2, t2.w_any), 4), " papers dropped share:", round(len(bad)/r.submission_id.nunique(),3))
tl = r[r.is_last & ~r.submission_id.isin(bad)]
print("last, drop papers with trimmed key:", round(rho(tl, pd.Series(1.0, index=tl.index)), 4))
