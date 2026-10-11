"""Audit D2: independent reproduction of main rho (last/first/any), Kitagawa identity, groups."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
papers, prof, email = P.load_panel()
E, L = P.E_WIN, P.L_WIN
# groups from any-role presence
ky = prof[["key","year"]].drop_duplicates()
inE = set(ky.key[ky.year.isin(E)]); inL = set(ky.key[ky.year.isin(L)])
S = inE & inL
r = prof[prof.year.isin(E+L)].merge(papers[["submission_id","name_primary"]], on="submission_id")
r["per"] = np.where(r.year.isin(E), "E", "L")
r["S"] = r.key.isin(S)
for part in ["last","first","any"]:
    x = r if part=="any" else r[r["is_"+part]]
    w = x.w_any if part=="any" else pd.Series(1.0, index=x.index)
    def m(mask): return np.average(x.name_primary[mask], weights=w[mask])
    PE = m(x.per.eq("E")); PL = m(x.per.eq("L"))
    PSE = m(x.per.eq("E") & x.S); PSL = m(x.per.eq("L") & x.S)
    print(part, "PE %.4f PL %.4f PSE %.4f PSL %.4f rho %.4f" % (PE, PL, PSE, PSL, (PSL-PSE)/(PL-PE)))
# check duplicated (key, paper)
print("dup key-paper:", prof.duplicated(["key","submission_id"]).sum())
print("w_any sums per paper:", prof.groupby("submission_id").w_any.sum().describe()[["min","max"]].to_dict())
# papers with multiple last-flag rows
nl = prof[prof.is_last].groupby("submission_id").size()
print("papers with >1 last row:", (nl>1).sum())
nf = prof[prof.is_first].groupby("submission_id").size()
print("papers with >1 first row:", (nf>1).sum())
# keys both first and last on the same paper
print("rows first&last:", (prof.is_first & prof.is_last).sum(), " of which list_len>1:", (prof.is_first & prof.is_last & (prof.list_len>1)).sum())
