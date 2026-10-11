"""Identification audit D2, check 5: what is inside the rolling 'all-prior' teams of H2c(ii) in L?
Share of L all-prior (rolling) papers that contain a D2 entrant (N) key (first seen 2025, reappearing 2026) or a
returner, and the NAME change of all-prior teams split by whether they contain such keys."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
papers, prof, _ = P.load_panel()
g = P.key_groups(prof, P.E_WIN, P.L_WIN)
grp = pd.Series(np.select([g.S, g.X, g.N, g.R], ["S", "X", "N", "R"], "o"), index=g.index)
r = prof[prof.year.isin(P.E_WIN + P.L_WIN)].assign(grp=lambda x: x.key.map(grp).fillna("o"))
comp = r.groupby("submission_id").grp.agg(lambda s: "".join(sorted(set(s))))
pp = papers.set_index("submission_id")
d = pp[pp.year.isin(P.E_WIN + P.L_WIN) & pp.team_roll.eq("all_prior")].copy()
d["comp"] = comp.reindex(d.index)
d["L"] = d.year.isin(P.L_WIN)
d["hasN"] = d.comp.str.contains("N"); d["hasR"] = d.comp.str.contains("R"); d["onlyS"] = d.comp.eq("S")
print("E all-prior papers:", (~d.L).sum(), "NAME", round(d[~d.L].name_primary.mean(), 3))
x = d[d.L]
print("L all-prior papers:", len(x), "share with an entrant key", round(x.hasN.mean(), 3), "with returner", round(x.hasR.mean(), 3),
      "only stayers", round(x.onlyS.mean(), 3))
for lab, m in [("with entrant key", x.hasN), ("with returner, no entrant", x.hasR & ~x.hasN), ("only stayer keys", x.onlyS)]:
    print(f"  L all-prior {lab:28s} n={m.sum():5d} NAME={x[m].name_primary.mean():.3f}")
