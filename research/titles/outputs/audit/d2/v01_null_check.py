"""Fixer verification: shared-outcome null rho as a composition ratio (independent code path)."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
papers, prof, email = P.load_panel()
E, L = P.E_WIN, P.L_WIN
g = P.key_groups(prof, E, L)
grp = pd.Series(np.select([g.S, g.X, g.N, g.R], list("SXNR"), "o"), index=g.index)
r = prof[prof.year.isin(E + L)].copy()
r["grp"] = r.key.map(grp)
r["L"] = r.year.isin(L)
fg = r[r.is_first].drop_duplicates("submission_id").set_index("submission_id").grp
anyN = r.groupby("submission_id").grp.agg(lambda s: (s == "N").any())
r["Nfirst"] = r.submission_id.map(fg).eq("N") & r.L
r["NRfirst"] = r.submission_id.map(fg).isin(["N", "R"]) & r.L
r["anyN"] = r.submission_id.map(anyN) & r.L
y = papers.set_index("submission_id").name_primary
r["y"] = r.submission_id.map(y).astype(float)
for part, m, w in [("last", r.is_last, 1.0), ("any", np.ones(len(r), bool), r.w_any), ("first", r.is_first, 1.0)]:
    d = r[np.asarray(m)].assign(w=(w[np.asarray(m)] if not np.isscalar(w) else 1.0))
    S = d.grp.eq("S")
    def mean(x, c): return (x.w * x[c]).sum() / x.w.sum()
    obs = (mean(d[S & d.L], "y") - mean(d[S & ~d.L], "y")) / (mean(d[d.L], "y") - mean(d[~d.L], "y"))
    out = {c: mean(d[S & d.L], c) / mean(d[d.L], c) for c in ["Nfirst", "anyN", "NRfirst"]}
    print(part, "obs", round(obs, 3), {k: round(v, 3) for k, v in out.items()},
          "share of L stayer rows on N-first papers", round(mean(d[S & d.L], "Nfirst"), 3))
