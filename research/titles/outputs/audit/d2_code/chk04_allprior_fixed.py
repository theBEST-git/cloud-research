"""Audit D2/H2c(ii): all-prior team ratio under the plan's censoring alternatives (fixed 2021-22 base, lag-1),
same estimator and last-key cluster bootstrap as d2_shiftshare.allprior_ratio."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys
papers, prof, _ = P.load_panel()
prof, idx = code_keys(prof)
last_key = prof[prof.is_last].drop_duplicates("submission_id").set_index("submission_id").key_code
out = []
for d in ["roll", "lag1", "fixed"]:
    for E, L, tag in [((2022, 2023), (2025, 2026), "main"), ((2023,), (2025, 2026), "E2023"), ((2023,), (2026,), "2023to2026")]:
        pp = papers[papers.year.isin(E + L) & papers[f"team_{d}"].notna()].copy()
        if not pp.year.isin(E).any():
            continue
        Ein = pp.year.isin(E).to_numpy(); ap = pp[f"team_{d}"].eq("all_prior").to_numpy(); y = pp.name_primary.to_numpy(float)
        A = np.column_stack([Ein, Ein*y, ~Ein, (~Ein)*y, Ein&ap, (Ein&ap)*y, (~Ein)&ap, ((~Ein)&ap)*y]).astype(np.float64)
        cl = last_key.reindex(pp.submission_id).to_numpy(dtype=float)
        cl = np.where(np.isnan(cl), -1 - np.arange(len(pp)), cl).astype(int)
        def st(T):
            T = np.atleast_2d(T); D = T[:,3]/T[:,2]-T[:,1]/T[:,0]; Da = T[:,7]/T[:,6]-T[:,5]/T[:,4]; return D, Da, Da/D
        D0, Da0, r0 = st(A.sum(0))
        bs = [st(W @ A) for W in C.boot_weights(len(pp), 1000, clusters=cl, seed=20260, chunk=100)]
        bR = np.concatenate([b[2] for b in bs]); bA = np.concatenate([b[1] for b in bs])
        out.append(dict(definition=d, window=tag, n_ap_E=int((Ein&ap).sum()), n_ap_L=int((~Ein&ap).sum()),
                        P_apE=A[:,5].sum()/A[:,4].sum(), P_apL=A[:,7].sum()/A[:,6].sum(), pop=D0[0], ap_change=Da0[0],
                        ap_lo=np.quantile(bA,.025), ap_hi=np.quantile(bA,.975), ratio=r0[0], lo=np.quantile(bR,.025), hi=np.quantile(bR,.975)))
o = pd.DataFrame(out); print(o.round(3).to_string()); o.to_csv("../outputs/audit/d2_code/chk04_allprior_fixed.csv", index=False)
