"""Identification audit D2, check 4.
(a) Camera-ready-free replication of the newcomer-free comparisons (NA-pool papers only, both windows).
(b) H2e email era (E=2018, L=2020): purely generational null (only papers with an entrant first author change)
    -> implied rho_any / rho_last; and all-stayer teams.
"""
import numpy as np, pandas as pd
from analyses import d2_panel as P

papers, prof, email = P.load_panel()
pp = papers.set_index("submission_id")

def analyse(rows, E, L, mask_papers=None, label=""):
    g = P.key_groups(rows, E, L)
    grp = pd.Series(np.select([g.S, g.X, g.N, g.R], ["S", "X", "N", "R"], "o"), index=g.index)
    r = rows[rows.year.isin(E + L)].copy()
    r["grp"] = r.key.map(grp).fillna("o")
    r["per"] = np.where(r.year.isin(E), "E", "L")
    if mask_papers is not None:
        r = r[r.submission_id.isin(mask_papers)]
    r["y"] = r.submission_id.map(pp.name_primary).astype(float)
    pc = r.groupby("submission_id").agg(per=("per", "first"), y=("y", "first"), n=("key", "size"),
                                         list_len=("list_len", "first"), nN=("grp", lambda s: (s == "N").sum()),
                                         nS=("grp", lambda s: (s == "S").sum()))
    fk = r[r.is_first].drop_duplicates("submission_id").set_index("submission_id").grp
    lk = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id").grp
    pc["fg"] = fk.reindex(pc.index).fillna("none"); pc["lg"] = lk.reindex(pc.index).fillna("none")
    E_, L_ = pc.per.eq("E"), pc.per.eq("L")
    D = pc[L_].y.mean() - pc[E_].y.mean()
    def ch(mE, mL):
        return pc[mE].y.mean(), pc[mL].y.mean(), pc[mL].y.mean() - pc[mE].y.mean(), int(mE.sum()), int(mL.sum())
    print(f"\n== {label}: population {pc[E_].y.mean():.3f} -> {pc[L_].y.mean():.3f} (delta {D:.4f})")
    for lab, mE, mL in [
        ("last=S", E_ & pc.lg.eq("S"), L_ & pc.lg.eq("S")),
        ("last=S, L no entrant", E_ & pc.lg.eq("S"), L_ & pc.lg.eq("S") & pc.nN.eq(0)),
        ("all-stayer teams", E_ & pc.nS.eq(pc.n) & pc.n.eq(pc.list_len), L_ & pc.nS.eq(pc.n) & pc.n.eq(pc.list_len))]:
        a, b, c, nE, nL = ch(mE, mL)
        print(f"  {lab:24s} {a:.3f} -> {b:.3f} change {c:+.4f} ratio {c / D:.2f} (n_E {nE}, n_L {nL})")
    # null
    rr = r.copy()
    def rho(yp):
        rr["yy"] = rr.submission_id.map(yp)
        o = {}
        for part, m, w in [("last", rr.is_last.to_numpy(), np.ones(len(rr))), ("first", rr.is_first.to_numpy(), np.ones(len(rr))),
                           ("any", np.ones(len(rr), bool), rr.w_any.to_numpy())]:
            d = rr[m].assign(w=w[m]); mean = lambda x: (x.w * x.yy).sum() / x.w.sum()
            o[part] = round(float((mean(d[d.per.eq("L") & d.grp.eq("S")]) - mean(d[d.per.eq("E") & d.grp.eq("S")])) /
                                  (mean(d[d.per.eq("L")]) - mean(d[d.per.eq("E")]))), 3)
        return o
    PE = pc[E_].y.mean()
    for nm, gm in [("entrant-first", L_ & pc.fg.eq("N")), ("entrant/returner-first", L_ & pc.fg.isin(["N", "R"]))]:
        yn = pd.Series(PE, index=pc.index); yn[gm] = PE + D / (gm.sum() / L_.sum())
        print(f"  pure-generational null ({nm} papers change only):", rho(yn))
    print("  observed:", rho(pc.y))

na = set(pp.index[pp.NA.eq(1)])
analyse(prof, P.E_WIN, P.L_WIN, na, "profile panel, NA-pool papers only (camera-ready-free)")
em = email.copy()
em["w_any"] = 1.0 / em.groupby("submission_id").key.transform("size")
analyse(em, (2018,), (2020,), None, "email era 2018 -> 2020 (H2e)")
analyse(em, (2017, 2018), (2019, 2020), None, "email era 2017-18 -> 2019-20")
