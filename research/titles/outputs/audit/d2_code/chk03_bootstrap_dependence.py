"""Audit D2: does the key-only cluster bootstrap understate uncertainty (papers shared across keys)?
Compares key-cluster, paper-cluster and two-way (pigeonhole: key x paper multinomial weights) bootstraps
for rho (last/first/any) and rho_first - rho_last, groups held fixed as in the original code."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
B = 300
papers, prof, _ = P.load_panel()
E, L = P.E_WIN, P.L_WIN
ky = prof[["key","year"]].drop_duplicates()
S = set(ky.key[ky.year.isin(E)]) & set(ky.key[ky.year.isin(L)])
r = prof[prof.year.isin(E+L)].merge(papers[["submission_id","name_primary"]], on="submission_id")
kc, _ = pd.factorize(r.key); pc, _ = pd.factorize(r.submission_id)
K, Pn = kc.max()+1, pc.max()+1
isE = r.year.isin(E).to_numpy(); Sr = r.key.isin(S).to_numpy(); y = r.name_primary.to_numpy(float)
parts = {"last": (r.is_last.to_numpy(), np.ones(len(r))), "first": (r.is_first.to_numpy(), np.ones(len(r))),
         "any": (np.ones(len(r), bool), r.w_any.to_numpy())}
def stats(rw):
    out = {}
    for nm, (pm, w0) in parts.items():
        w = w0 * rw * pm
        def m(mask): return (w[mask]*y[mask]).sum()/w[mask].sum()
        D = m(~isE) - m(isE); DS = m(~isE & Sr) - m(isE & Sr)
        out[nm] = DS / D
    out["first_minus_last"] = out["first"] - out["last"]
    return out
rng = np.random.default_rng(1)
res = {"key": [], "paper": [], "twoway": []}
for b in range(B):
    wk = rng.multinomial(K, np.full(K, 1/K)).astype(float)
    wp = rng.multinomial(Pn, np.full(Pn, 1/Pn)).astype(float)
    res["key"].append(stats(wk[kc]))
    res["paper"].append(stats(wp[pc]))
    res["twoway"].append(stats(wk[kc]*wp[pc]))
pt = stats(np.ones(len(r)))
rows = []
for scheme, L_ in res.items():
    d = pd.DataFrame(L_)
    for c in d.columns:
        rows.append(dict(scheme=scheme, stat=c, est=pt[c], se=d[c].std(ddof=1), lo=d[c].quantile(.025), hi=d[c].quantile(.975)))
out = pd.DataFrame(rows).pivot(index="stat", columns="scheme", values="se")
print(pd.DataFrame(rows).round(4).to_string())
print(out.round(4))
pd.DataFrame(rows).to_csv("../outputs/audit/d2_code/chk03_bootstrap_dependence.csv", index=False)
