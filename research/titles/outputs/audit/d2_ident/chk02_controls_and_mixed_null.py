"""Identification audit D2, check 2.

(a) Is the near-zero change on newcomer-free teams a composition artefact (team size, topic)?  LPM
    NAME ~ L + size_bin FE + topic100 FE on each restricted sample vs the same model on all papers.
    Samples: all-stayer teams (E=2022-23, L=2025-26); symmetric 2-year-lookback all-prior teams (E=2023 with
    lookback 2021-22; L=2025-26 with lookback y-2..y-1); last=S papers without entrant keys; papers containing a
    repeated stayer dyad AND no entrant key.
(b) Mixed null: every L paper rises by a (communal), papers with an entrant/returner first author rise by an
    extra b; a chosen so the implied rho_first equals the observed 0.525, b so the population change matches.
    What rho_last / rho_any does this ~50% communal world produce?
(c) H2b: entrant-first vs stayer-first L papers WITHIN the same last-position key (key FE), + size/topic FE,
    and the share of stayer-first L papers that are alphabetical or single-key.
"""
import itertools, json, re
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P
from common import read_table

papers, prof, _ = P.load_panel()
E, L = P.E_WIN, P.L_WIN
g = P.key_groups(prof, E, L)
grp = pd.Series(np.select([g.S, g.X, g.N, g.R], ["S", "X", "N", "R"], "o"), index=g.index)
pp = papers.set_index("submission_id")
r = prof.copy()
r["grp"] = r.key.map(grp).fillna("o")

def paper_comp(rr):
    pc = rr.groupby("submission_id").agg(year=("year", "first"), n_pkeys=("key", "size"), list_len=("list_len", "first"),
                                         nN=("grp", lambda s: (s == "N").sum()), nS=("grp", lambda s: (s == "S").sum()))
    fk = rr[rr.is_first].drop_duplicates("submission_id").set_index("submission_id")
    lk = rr[rr.is_last].drop_duplicates("submission_id").set_index("submission_id")
    pc["first_grp"] = fk.grp.reindex(pc.index).fillna("none"); pc["last_grp"] = lk.grp.reindex(pc.index).fillna("none")
    pc["first_key"] = fk.key.reindex(pc.index); pc["last_key"] = lk.key.reindex(pc.index)
    pc["first_name"] = fk.native_id.reindex(pc.index)
    for c in ["name_primary", "size_bin", "topic100", "NA"]:
        pc[c] = pp[c].reindex(pc.index)
    pc["full_profile"] = pc.n_pkeys.eq(pc.list_len)
    return pc

pc = paper_comp(r[r.year.isin(E + L)])
pc["Lp"] = pc.year.isin(L).astype(int)

def lcoef(d, controls=True):
    d = d.assign(one=1.0)
    fe = ["size_bin", "topic100"] if controls else []
    res = C.feols(d, "name_primary", ["Lp"], fe=fe, cluster="last_key_c")
    return float(res.params["Lp"]), float(res.se["Lp"]), int(res.nobs)

pc["last_key_c"] = pd.factorize(pc.last_key.fillna(pd.Series(pc.index, index=pc.index)))[0]
out = []
def add(label, m, base_mask=None):
    base = pc if base_mask is None else pc[base_mask]
    for ctl in (False, True):
        b0, s0, n0 = lcoef(base, ctl)
        b, s, n = lcoef(pc[m], ctl)
        out.append(dict(sample=label, controls="size_bin+topic100 FE" if ctl else "none", n=n, change=b, se=s,
                        pop_change=b0, ratio=b / b0, ratio_lo=(b - 1.96 * s) / b0, ratio_hi=(b + 1.96 * s) / b0))

E_, L_ = pc.year.isin(E), pc.year.isin(L)
add("all papers", E_ | L_)
add("last=S (rho_last numerator)", (E_ | L_) & pc.last_grp.eq("S"))
add("last=S; L restricted to no-entrant papers", (E_ & pc.last_grp.eq("S")) | (L_ & pc.last_grp.eq("S") & pc.nN.eq(0)))
add("all-stayer teams (full profile lists)", (E_ | L_) & pc.full_profile & pc.nS.eq(pc.n_pkeys))
add("all-stayer teams, >=2 keys", (E_ | L_) & pc.full_profile & pc.nS.eq(pc.n_pkeys) & pc.n_pkeys.ge(2))

# repeated stayer dyads on papers without entrants
rs = r[r.year.isin(E + L) & r.grp.eq("S")]
pairs = []
for sid, ks in rs.groupby("submission_id").key:
    ks = sorted(set(ks))
    if 2 <= len(ks) <= 25:
        pairs += [(a + "|" + b, sid) for a, b in itertools.combinations(ks, 2)]
pr = pd.DataFrame(pairs, columns=["dyad", "submission_id"]); pr["L"] = pr.submission_id.map(pc.Lp)
rep = pr.groupby("dyad").L.agg(lambda s: s.nunique() == 2); rep = set(rep.index[rep])
rp = set(pr.loc[pr.dyad.isin(rep), "submission_id"])
add("papers with a repeated stayer dyad", (E_ | L_) & pc.index.isin(rp))
add("papers with a repeated stayer dyad AND no entrant key (L)", (E_ & pc.index.isin(rp)) | (L_ & pc.index.isin(rp) & pc.nN.eq(0)))

# symmetric 2-year-lookback all-prior teams: E = 2023 (lookback 2021-22), L = 2025-26 (lookback y-2, y-1)
ky = set(zip(r.key, r.year))
r["prior2"] = [((k, y - 1) in ky) or ((k, y - 2) in ky) for k, y in zip(r.key, r.year)]
sub = r[r.year.isin([2023, 2025, 2026])]
ap = sub.groupby("submission_id").prior2.mean().eq(1.0)
pc2 = paper_comp(sub); pc2["Lp"] = pc2.year.isin(L).astype(int)
pc2["last_key_c"] = pd.factorize(pc2.last_key.fillna(pd.Series(pc2.index, index=pc2.index)))[0]
pc2["ap2"] = ap.reindex(pc2.index)
for ctl in (False, True):
    b0, s0, _ = lcoef(pc2, ctl); b, s, n = lcoef(pc2[pc2.ap2 & pc2.full_profile], ctl)
    out.append(dict(sample="2-yr-lookback all-prior teams, E=2023 vs L=2025-26 (full profile lists)",
                    controls="size_bin+topic100 FE" if ctl else "none", n=n, change=b, se=s, pop_change=b0,
                    ratio=b / b0, ratio_lo=(b - 1.96 * s) / b0, ratio_hi=(b + 1.96 * s) / b0))
    b, s, n = lcoef(pc2[pc2.ap2 & pc2.full_profile & pc2.n_pkeys.ge(2)], ctl)
    out.append(dict(sample="  same, >=2 keys", controls="size_bin+topic100 FE" if ctl else "none", n=n, change=b, se=s,
                    pop_change=b0, ratio=b / b0, ratio_lo=(b - 1.96 * s) / b0, ratio_hi=(b + 1.96 * s) / b0))
res = pd.DataFrame(out)
pd.set_option("display.width", 250)
print(res.round(3).to_string())
res.to_csv("../outputs/audit/d2_ident/chk02a_controls.csv", index=False)

# ---------------- (b) mixed null ----------------
rows = r[r.year.isin(E + L)].copy(); rows["per"] = np.where(rows.year.isin(E), "E", "L")
def rho_with(ypaper):
    rows["yy"] = rows.submission_id.map(ypaper)
    o = {}
    for part, m, w in [("last", rows.is_last.to_numpy(), np.ones(len(rows))), ("first", rows.is_first.to_numpy(), np.ones(len(rows))),
                       ("any", np.ones(len(rows), bool), rows.w_any.to_numpy())]:
        d = rows[m].assign(w=w[m])
        mean = lambda x: (x.w * x.yy).sum() / x.w.sum()
        o[part] = (mean(d[d.per.eq("L") & d.grp.eq("S")]) - mean(d[d.per.eq("E") & d.grp.eq("S")])) / (mean(d[d.per.eq("L")]) - mean(d[d.per.eq("E")]))
    return o
PE = pc.loc[E_, "name_primary"].mean(); D = pc.loc[L_, "name_primary"].mean() - PE
gen = L_ & pc.first_grp.isin(["N", "R"]); sh = gen.sum() / L_.sum()
print(f"\npopulation delta {D:.4f}; share of L papers with entrant/returner first author {sh:.3f}")
for frac in [0.0, 0.25, 0.4, 0.5, 0.525, 0.6, 0.75, 1.0]:
    a = frac * D
    b = (D - a) / sh
    yn = pd.Series(PE, index=pc.index); yn[L_] = PE + a; yn[gen] = PE + a + b
    print(f"communal share a/D = {frac:.3f}:", {k: round(float(v), 3) for k, v in rho_with(yn).items()})
print("observed:", {k: round(float(v), 3) for k, v in rho_with(pc.name_primary).items()})

# ---------------- (c) H2b within last key ----------------
Lf = pc[L_ & pc.first_grp.isin(["N", "S"]) & pc.first_key.ne(pc.last_key) & pc.last_key.notna()].copy()
Lf["entrant_first"] = Lf.first_grp.eq("N").astype(float)
Lf["lk"] = pd.factorize(Lf.last_key)[0]
for lab, fe in [("raw", []), ("size+topic FE", ["size_bin", "topic100"]), ("last-key FE", ["lk"]),
                ("last-key + size + topic FE", ["lk", "size_bin", "topic100"])]:
    res = C.feols(Lf, "name_primary", ["entrant_first"], fe=fe, cluster="lk")
    print(f"H2b gap entrant-first minus stayer-first (L, multi-key papers) [{lab}]: "
          f"{res.params['entrant_first']:.4f} (se {res.se['entrant_first']:.4f}), n={res.nobs}")
# single-key / solo share and alphabetical ordering
a = read_table("submission_authors")[["submission_id", "source_list_position", "declared_name_json"]]
a = a[a.submission_id.isin(set(pc.index))]
a["nm"] = a.declared_name_json.astype(str).str.strip('"')
a["last_tok"] = a.nm.str.split().str[-1].str.lower()
alpha = a.sort_values(["submission_id", "source_list_position"]).groupby("submission_id").last_tok.agg(
    lambda s: len(s) >= 3 and list(s) == sorted(s))
pc["alpha3"] = alpha.reindex(pc.index).fillna(False)
pc["solo_key"] = pc.n_pkeys.eq(1)
for lab, m in [("L, stayer first", L_ & pc.first_grp.eq("S")), ("L, entrant first", L_ & pc.first_grp.eq("N")),
               ("E, stayer first", E_ & pc.first_grp.eq("S")), ("E, exiter first", E_ & pc.first_grp.eq("X"))]:
    d = pc[m]
    print(f"{lab:20s} n={len(d):6d} NAME={d.name_primary.mean():.3f} solo_key={d.solo_key.mean():.3f} "
          f"first==last key={d.first_key.eq(d.last_key).mean():.3f} alphabetical(>=3)={d.alpha3.mean():.3f} "
          f"mean list_len={d.list_len.mean():.2f} NA={d.NA.mean():.3f}")
d = pc[L_ & pc.first_grp.isin(["N", "S"]) & ~pc.alpha3 & pc.n_pkeys.ge(2)]
print("L gap entrant-first minus stayer-first, excluding alphabetical and single-key papers:",
      round(d[d.first_grp.eq('N')].name_primary.mean() - d[d.first_grp.eq('S')].name_primary.mean(), 4))
