"""Identification audit D2, check 1: shared paper-level outcome.

Titles are paper-level outcomes shared by every co-author. A last-position stayer key's L papers mostly have
entrant first authors, so rho_last ~ 1 may be mechanical under purely generational (first-author) change.

(a) Decompose last-position stayer rows in L by co-author composition; recompute the stayer change on papers
    with NO entrant (group N) co-author, on papers whose first AND last keys are both stayers, on all-stayer
    teams (every declared position is a stayer profile key), and on repeated dyads (pairs of keys that
    co-author in both E and L).
(b) Mechanical null: replace NAME by its expectation under a DGP in which ONLY papers with an entrant first
    author change (all other papers keep P_E), calibrated to the observed population change; recompute
    rho_last / rho_any / rho_first with the original formulas.  Also a mixed DGP fitted to the paper-level
    change of non-entrant-first papers.
Run: cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python ../outputs/audit/d2_ident/chk01_shared_outcome.py
"""
import itertools
import numpy as np, pandas as pd
from analyses import d2_panel as P

rng = np.random.default_rng(7)
papers, prof, _ = P.load_panel()
E, L = P.E_WIN, P.L_WIN
g = P.key_groups(prof, E, L)
grp = pd.Series(np.select([g.S, g.X, g.N, g.R], ["S", "X", "N", "R"], "o"), index=g.index)
r = prof[prof.year.isin(E + L)].copy()
r["grp"] = r.key.map(grp).fillna("o")
r["per"] = np.where(r.year.isin(E), "E", "L")
y = papers.set_index("submission_id").name_primary
r["y"] = r.submission_id.map(y).astype(float)

# paper-level composition
pc = r.groupby("submission_id").agg(per=("per", "first"), year=("year", "first"), y=("y", "first"),
                                     n_pkeys=("key", "size"), list_len=("list_len", "first"),
                                     nN=("grp", lambda s: (s == "N").sum()), nS=("grp", lambda s: (s == "S").sum()))
fk = r[r.is_first].drop_duplicates("submission_id").set_index("submission_id")
lk = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id")
pc["first_grp"] = fk.grp.reindex(pc.index).fillna("none")
pc["last_grp"] = lk.grp.reindex(pc.index).fillna("none")
pc["first_key"] = fk.key.reindex(pc.index)
pc["last_key"] = lk.key.reindex(pc.index)
pc["full_profile"] = pc.n_pkeys.eq(pc.list_len)

PE = pc.loc[pc.per.eq("E"), "y"].mean(); PL = pc.loc[pc.per.eq("L"), "y"].mean(); D = PL - PE
print(f"population (papers with >=1 panel key): P_E={PE:.4f} P_L={PL:.4f} delta={D:.4f}")
lastpop = pc[pc.last_grp.ne("none")]
PEl, PLl = lastpop[lastpop.per.eq("E")].y.mean(), lastpop[lastpop.per.eq("L")].y.mean()
print(f"last-partition population: {PEl:.4f} -> {PLl:.4f}, delta {PLl-PEl:.4f}")

out = []
def add(label, mE, mL, base=D, cl=None):
    """change between the papers selected by mE (E) and mL (L); cluster bootstrap on last key."""
    a, b = pc[mE], pc[mL]
    est = b.y.mean() - a.y.mean()
    # bootstrap: resample last keys (papers without a last key are their own cluster)
    d = pd.concat([a.assign(L=0), b.assign(L=1)])
    clu = d.last_key.fillna(pd.Series(d.index, index=d.index)).to_numpy()
    codes, uniq = pd.factorize(clu)
    yy, LL = d.y.to_numpy(), d.L.to_numpy()
    bs = []
    for _ in range(300):
        w = rng.multinomial(len(uniq), np.full(len(uniq), 1 / len(uniq)))[codes].astype(float)
        bs.append((w * yy * LL).sum() / (w * LL).sum() - (w * yy * (1 - LL)).sum() / (w * (1 - LL)).sum())
    bs = np.array(bs)
    out.append(dict(sample=label, n_E=len(a), n_L=len(b), P_E=a.y.mean(), P_L=b.y.mean(), change=est,
                    lo=np.quantile(bs, .025), hi=np.quantile(bs, .975), ratio_to_pop=est / base,
                    ratio_lo=np.quantile(bs, .025) / base, ratio_hi=np.quantile(bs, .975) / base))

E_, L_ = pc.per.eq("E"), pc.per.eq("L")
add("all papers (population)", E_, L_)
add("last=S (reproduces rho_last numerator)", E_ & pc.last_grp.eq("S"), L_ & pc.last_grp.eq("S"))
add("last=S, L papers with NO entrant key", E_ & pc.last_grp.eq("S"), L_ & pc.last_grp.eq("S") & pc.nN.eq(0))
add("last=S, L papers WITH >=1 entrant key", E_ & pc.last_grp.eq("S"), L_ & pc.last_grp.eq("S") & pc.nN.gt(0))
add("last=S, L papers with entrant FIRST author", E_ & pc.last_grp.eq("S"), L_ & pc.last_grp.eq("S") & pc.first_grp.eq("N"))
two = pc.n_pkeys.ge(2) & pc.first_key.ne(pc.last_key)
add("first=S and last=S (both windows)", E_ & two & pc.first_grp.eq("S") & pc.last_grp.eq("S"),
    L_ & two & pc.first_grp.eq("S") & pc.last_grp.eq("S"))
add("all-stayer teams (every position a stayer key)", E_ & pc.full_profile & pc.nS.eq(pc.n_pkeys),
    L_ & pc.full_profile & pc.nS.eq(pc.n_pkeys))
add("all-stayer teams, >=2 keys", E_ & pc.full_profile & pc.nS.eq(pc.n_pkeys) & pc.n_pkeys.ge(2),
    L_ & pc.full_profile & pc.nS.eq(pc.n_pkeys) & pc.n_pkeys.ge(2))
add("L papers with no entrant key at all (any last grp)", E_, L_ & pc.nN.eq(0))

# repeated dyads: unordered key pairs co-authoring >=1 E paper and >=1 L paper; papers that contain one
pairs = []
for sid, ks in r[r.grp.eq("S")].groupby("submission_id").key:
    ks = sorted(set(ks))
    if 2 <= len(ks) <= 25:
        for a_, b_ in itertools.combinations(ks, 2):
            pairs.append((a_ + "|" + b_, sid))
pr = pd.DataFrame(pairs, columns=["dyad", "submission_id"])
pr["per"] = pr.submission_id.map(pc.per)
rep = pr.groupby("dyad").per.agg(lambda s: set(s) >= {"E", "L"})
rep = set(rep.index[rep])
rp = set(pr.loc[pr.dyad.isin(rep), "submission_id"])
add("papers containing a repeated (E and L) stayer dyad", E_ & pc.index.isin(rp), L_ & pc.index.isin(rp))
# dyad-weighted: each dyad's E mean vs L mean
dd = pr[pr.dyad.isin(rep)].assign(y=lambda x: x.submission_id.map(pc.y))
dm = dd.groupby(["dyad", "per"]).y.mean().unstack()
print(f"repeated dyads: {len(rep)}; dyad-weighted change {float((dm.L - dm.E).mean()):.4f} (E {dm.E.mean():.4f} -> L {dm.L.mean():.4f})")

res = pd.DataFrame(out)
pd.set_option("display.width", 250)
print(res.round(3).to_string())

# composition of last=S rows in L by first author group, vs population
cs = pc[L_ & pc.last_grp.eq("S")].groupby("first_grp").y.agg(["size", "mean"])
cs["share"] = cs["size"] / cs["size"].sum()
cp = pc[L_].groupby("first_grp").y.agg(["size", "mean"]); cp["share"] = cp["size"] / cp["size"].sum()
print("\nL papers with last=S, by first-author group:\n", cs.round(3))
print("All L papers by first-author group:\n", cp.round(3))
ce = pc[E_].groupby("first_grp").y.agg(["size", "mean"]); ce["share"] = ce["size"] / ce["size"].sum()
print("All E papers by first-author group:\n", ce.round(3))

# ---------------- (b) mechanical null ----------------
rows = r.copy()
def rho_with(ypaper):
    rows["yy"] = rows.submission_id.map(ypaper)
    res = {}
    for part, m, w in [("last", rows.is_last, np.ones(len(rows))), ("first", rows.is_first, np.ones(len(rows))),
                       ("any", np.ones(len(rows), bool), rows.w_any.to_numpy())]:
        d = rows[np.asarray(m)].assign(w=np.asarray(w)[np.asarray(m)])
        mean = lambda x: (x.w * x.yy).sum() / x.w.sum()
        Dp = mean(d[d.per.eq("L")]) - mean(d[d.per.eq("E")])
        DS = mean(d[d.per.eq("L") & d.grp.eq("S")]) - mean(d[d.per.eq("E") & d.grp.eq("S")])
        res[part] = DS / Dp
    return res

print("\nobserved:", {k: round(v, 3) for k, v in rho_with(pc.y).items()})
# null 1: only entrant-first L papers change
isNf = L_ & pc.first_grp.eq("N")
shareNf = isNf.sum() / L_.sum()
ynull = pd.Series(PE, index=pc.index)
ynull[isNf] = PE + D / shareNf
print(f"null1 (only papers with an entrant first author change; share {shareNf:.3f}):",
      {k: round(v, 3) for k, v in rho_with(ynull).items()})
# null 2: only papers with ANY entrant key change
isNa = L_ & pc.nN.gt(0)
shA = isNa.sum() / L_.sum()
ynull2 = pd.Series(PE, index=pc.index); ynull2[isNa] = PE + D / shA
print(f"null2 (only papers with any entrant key change; share {shA:.3f}):", {k: round(v, 3) for k, v in rho_with(ynull2).items()})
# null 3: the change is carried by the FIRST AUTHOR'S group only: entrant-first and returner-first papers rise; S-first flat
isNR = L_ & pc.first_grp.isin(["N", "R"])
sh3 = isNR.sum() / L_.sum()
ynull3 = pd.Series(PE, index=pc.index); ynull3[isNR] = PE + D / sh3
print(f"null3 (papers with entrant/returner first author change; share {sh3:.3f}):", {k: round(v, 3) for k, v in rho_with(ynull3).items()})
res.to_csv("../outputs/audit/d2_ident/chk01_shared_outcome.csv", index=False)
