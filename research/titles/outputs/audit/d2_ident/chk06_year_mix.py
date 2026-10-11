"""Identification audit D2, check 6: is the small change on newcomer-free L papers a 2025/2026 year-mix artefact?
Per-L-year changes vs E for last=S papers without entrant keys and for all-stayer teams, against the per-year
population change."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
papers, prof, _ = P.load_panel()
g = P.key_groups(prof, P.E_WIN, P.L_WIN)
grp = pd.Series(np.select([g.S, g.X, g.N, g.R], ["S", "X", "N", "R"], "o"), index=g.index)
r = prof[prof.year.isin(P.E_WIN + P.L_WIN)].assign(grp=lambda x: x.key.map(grp).fillna("o"))
pp = papers.set_index("submission_id")
pc = r.groupby("submission_id").agg(year=("year", "first"), n=("key", "size"), ll=("list_len", "first"),
                                     nN=("grp", lambda s: (s == "N").sum()), nS=("grp", lambda s: (s == "S").sum()))
pc["lg"] = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id").grp.reindex(pc.index)
pc["y"] = pp.name_primary.reindex(pc.index)
E = pc[pc.year.isin(P.E_WIN)]
popE, sE, asE = E.y.mean(), E[E.lg.eq("S")].y.mean(), E[E.nS.eq(E.n) & E.n.eq(E.ll)].y.mean()
for yr in (2025, 2026):
    Ly = pc[pc.year.eq(yr)]
    d = Ly.y.mean() - popE
    a = Ly[Ly.lg.eq("S") & Ly.nN.eq(0)]
    b = Ly[Ly.nS.eq(Ly.n) & Ly.n.eq(Ly.ll)]
    print(f"{yr}: pop change {d:.3f}; last=S no-entrant n={len(a)} change {a.y.mean()-sE:.3f} (ratio {(a.y.mean()-sE)/d:.2f}); "
          f"all-stayer teams n={len(b)} change {b.y.mean()-asE:.3f} (ratio {(b.y.mean()-asE)/d:.2f})")
