"""WP6 / D2 identification checks added in response to the D2 audit (outputs/audit/d2/fix_log.md).

A title is a paper-level outcome shared by every co-author, so a key-level decomposition cannot by itself say
who changed. This script adds the checks the audit asked for:

  1. Newcomer-free contrasts (audit ID-2, ID-3): NAME change E = 2022-23 -> L = 2025-26 on papers whose team
     composition excludes newcomers, under several definitions (all-stayer teams, last-position stayers without
     entrant co-authors, first and last both stayers, repeated stayer dyads, symmetric-lookback all-prior teams),
     each as a ratio to the matching population change. Last-position-key cluster bootstrap (1,000 reps); LPM
     versions with size-bin + topic100 FE against the same-model population change; NA-pool and email-era
     versions.
  2. First list position (audit ID-4): entrant-first minus stayer-first gap within the same last-position key,
     and a symmetric 2-year-lookback newcomer premium by year (2023-26) and change ratio of prior first keys.
  3. Two-way dependence (audit D2-C4, ID-9): SEs of the headline rho by key, paper and row bootstrap, the
     Cameron-Gelbach-Miller two-way SE sqrt(V_key + V_paper - V_row) and the conservative pigeonhole (key x paper)
     bootstrap.
  4. H2d benchmark (audit ID-5): slope and r of marker changes for random paper subsets with the stayers' E/L
     weights (the communal expectation), next to the shared-outcome-null slope (= the null rho for every marker).
  5. Family-structured removal (audit D2-C8): remove same-key cross-year paper pairs (resubmission-like) instead
     of independent papers, and compare with random removal.
  6. Figure F2.2 (audit D2-R9): rho with key-cluster and two-way CIs, IPW and shared-outcome-null benchmarks;
     Kitagawa and scenario shares in their own panel; newcomer-free contrasts; composition shift-share.

Outputs (outputs/d2_carriers/): T2_4_newcomer_free.csv, T2_1b_twoway_se.csv, h2b_first_position.csv,
h2b_newcomer_premium_by_year.csv, removal_family_sim.csv, h2d_random_subset.csv, ident_results.json,
fig_F2_2_decomposition.{pdf,png,csv}

Run (after d2_panel, d2_shiftshare, d2_markers):
    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_ident [n_boot]
"""
from __future__ import annotations

import itertools
import json
import sys
import time

import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys, groups_coded

OUTDIR = P.OUTDIR
N_BOOT = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
SEED = 20262
E_WIN, L_WIN = P.E_WIN, P.L_WIN


# --------------------------------------------------------------------------------------------
# Paper-level composition
# --------------------------------------------------------------------------------------------
def paper_comp(rows: pd.DataFrame, papers: pd.DataFrame, groups: pd.DataFrame, years) -> pd.DataFrame:
    """One row per paper with >= 1 panel key in `years`: group of the first/last key, counts by group."""
    r = rows[rows.year.isin(years)].copy()
    g = groups.reindex(np.arange(int(rows.key_code.max()) + 1)).fillna(False)
    kc = r.key_code.to_numpy()
    r["grp"] = np.select([g.S.to_numpy(bool)[kc], g.X.to_numpy(bool)[kc], g.N.to_numpy(bool)[kc],
                          g.R.to_numpy(bool)[kc]], ["S", "X", "N", "R"], "o")
    for c in "SXNR":
        r["n" + c] = r.grp.eq(c)
    pc = r.groupby("submission_id").agg(year=("year", "first"), n_pkeys=("key_code", "size"),
                                         list_len=("list_len", "first"), nS=("nS", "sum"), nX=("nX", "sum"),
                                         nN=("nN", "sum"), nR=("nR", "sum"))
    fk = r[r.is_first].drop_duplicates("submission_id").set_index("submission_id")
    lk = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id")
    pc["first_grp"] = fk.grp.reindex(pc.index).fillna("none")
    pc["last_grp"] = lk.grp.reindex(pc.index).fillna("none")
    pc["first_key"] = fk.key_code.reindex(pc.index)
    pc["last_key"] = lk.key_code.reindex(pc.index)
    pp = papers.set_index("submission_id")
    for c in ["name_primary", "name_compound", "NA", "size_bin", "topic100", "team_roll", "team_lag1", "team_fixed",
              "team_sym2"]:
        if c in pp.columns:
            pc[c] = pp[c].reindex(pc.index)
    pc["y"] = pc.name_primary.astype(float)
    pc["full_profile"] = pc.n_pkeys.eq(pc.list_len)
    cl = pc.last_key.to_numpy(dtype=float)
    pc["cl"] = np.where(np.isnan(cl), -1 - np.arange(len(pc)), cl).astype(np.int64)
    return pc


def repeated_dyad_papers(rows, groups, E, L) -> set:
    """Papers containing a pair of stayer keys that co-author at least one paper in E and one in L."""
    g = groups.reindex(np.arange(int(rows.key_code.max()) + 1)).fillna(False)
    r = rows[rows.year.isin(E + L)]
    r = r[g.S.to_numpy(bool)[r.key_code.to_numpy()]]
    per = dict(zip(r.submission_id, np.where(r.year.isin(L), 1, 0)))
    pairs = []
    for sid, ks in r.groupby("submission_id").key_code:
        ks = sorted(set(ks))
        if 2 <= len(ks) <= 25:
            pairs += [(a * 1_000_000 + b, sid) for a, b in itertools.combinations(ks, 2)]
    pr = pd.DataFrame(pairs, columns=["dyad", "submission_id"])
    pr["L"] = pr.submission_id.map(per)
    rep = pr.groupby("dyad").L.nunique()
    rep = set(rep.index[rep.eq(2)])
    return set(pr.loc[pr.dyad.isin(rep), "submission_id"])


# --------------------------------------------------------------------------------------------
# Contrasts with a last-key cluster bootstrap
# --------------------------------------------------------------------------------------------
def contrasts(pc: pd.DataFrame, defs: list[tuple], n_boot: int, seed: int, controlled: bool = True) -> pd.DataFrame:
    """defs: (label, mask_E, mask_L, pop_E, pop_L). Change of the subset and its ratio to the population change on
    the same bootstrap draw (clusters = last-position key). Optional LPM with size-bin + topic100 FE."""
    y = pc.y.to_numpy(float)
    cols = []
    for _, mE, mL, pE, pL in defs:
        for m in (mE, mL, pE, pL):
            m = np.asarray(m, bool)
            cols += [m.astype(float), m * y]
    A = np.column_stack(cols).astype(np.float64)

    def stat(T):
        T = np.atleast_2d(T)
        out = []
        for k in range(len(defs)):
            t = T[:, 8 * k:8 * k + 8]
            with np.errstate(divide="ignore", invalid="ignore"):
                ch = t[:, 3] / t[:, 2] - t[:, 1] / t[:, 0]
                pop = t[:, 7] / t[:, 6] - t[:, 5] / t[:, 4]
            out.append((ch, pop, ch / pop))
        return out
    st0 = stat(A.sum(0))
    bs = [stat(W.astype(np.float64) @ A) for W in C.boot_weights(len(pc), n_boot, clusters=pc.cl.to_numpy(),
                                                                   seed=seed, chunk=100)]
    rows = []
    for k, (lab, mE, mL, pE, pL) in enumerate(defs):
        ch = np.concatenate([b[k][0] for b in bs])
        rt = np.concatenate([b[k][2] for b in bs])
        ch, rt = ch[np.isfinite(ch)], rt[np.isfinite(rt)]
        mE, mL = np.asarray(mE, bool), np.asarray(mL, bool)
        row = dict(contrast=lab, n_E=int(mE.sum()), n_L=int(mL.sum()), P_E=float(y[mE].mean()), P_L=float(y[mL].mean()),
                   change=float(st0[k][0][0]), change_lo=float(np.quantile(ch, .025)),
                   change_hi=float(np.quantile(ch, .975)), pop_change=float(st0[k][1][0]), ratio=float(st0[k][2][0]),
                   ratio_lo=float(np.quantile(rt, .025)), ratio_hi=float(np.quantile(rt, .975)),
                   p_ratio_ge_0_5=float((np.sum(rt >= 0.5) + 1) / (len(rt) + 1)))
        if controlled:
            d = pc[mE | mL].assign(Lp=mL[mE | mL].astype(float))
            b = C.feols(d, "y", ["Lp"], fe=["size_bin", "topic100"], cluster="cl")
            dp = pc[np.asarray(pE, bool) | np.asarray(pL, bool)].assign(
                Lp=np.asarray(pL, bool)[np.asarray(pE, bool) | np.asarray(pL, bool)].astype(float))
            b0 = C.feols(dp, "y", ["Lp"], fe=["size_bin", "topic100"], cluster="cl")
            bb, se, bp = float(b.params["Lp"]), float(b.se["Lp"]), float(b0.params["Lp"])
            row.update(ctl_change=bb, ctl_se=se, ctl_pop_change=bp, ctl_ratio=bb / bp,
                       ctl_ratio_lo=(bb - 1.96 * se) / bp, ctl_ratio_hi=(bb + 1.96 * se) / bp)
        rows.append(row)
    return pd.DataFrame(rows)


def newcomer_free(prof, papers, g, dyads, n_boot, sample="all") -> pd.DataFrame:
    pc = paper_comp(prof, papers, g, E_WIN + L_WIN)
    if sample == "NA_pool":
        pc = pc[pc.NA.eq(1)].copy()
    E_, L_ = pc.year.isin(E_WIN).to_numpy(), pc.year.isin(L_WIN).to_numpy()
    E23 = pc.year.eq(2023).to_numpy()
    lS, fS = pc.last_grp.eq("S").to_numpy(), pc.first_grp.eq("S").to_numpy()
    noN = pc.nN.eq(0).to_numpy()
    noNR = (pc.nN.eq(0) & pc.nR.eq(0)).to_numpy()
    allS = (pc.full_profile & pc.nS.eq(pc.n_pkeys)).to_numpy()
    two = (pc.n_pkeys.ge(2) & pc.first_key.ne(pc.last_key)).to_numpy()
    dy = pc.index.isin(dyads)
    lag1 = pc.team_lag1.eq("all_prior").to_numpy()
    sym2 = pc.team_sym2.eq("all_prior").to_numpy()
    roll = pc.team_roll.eq("all_prior").to_numpy()
    fixed = pc.team_fixed.eq("all_prior").to_numpy()
    defs = [
        ("population (papers with >= 1 profile key)", E_, L_, E_, L_),
        ("last=S (rho_last numerator)", E_ & lS, L_ & lS, E_, L_),
        ("last=S; L papers with an entrant first author", E_ & lS, L_ & lS & pc.first_grp.eq("N").to_numpy(), E_, L_),
        ("last=S; L papers with >= 1 entrant key", E_ & lS, L_ & lS & ~noN, E_, L_),
        ("last=S; L papers with no entrant key", E_ & lS, L_ & lS & noN, E_, L_),
        ("last=S; L papers with no entrant or returner key", E_ & lS, L_ & lS & noNR, E_, L_),
        ("last=S; lag-1 all-prior team in both windows (symmetric)", E_ & lS & lag1, L_ & lS & lag1, E_, L_),
        ("last=S; 2-year-lookback all-prior team, E = 2023 (symmetric)", E23 & lS & sym2, L_ & lS & sym2, E23, L_),
        ("first=S and last=S (distinct keys)", E_ & two & fS & lS, L_ & two & fS & lS, E_, L_),
        ("all-stayer teams (every declared position a stayer key)", E_ & allS, L_ & allS, E_, L_),
        ("papers with a repeated stayer dyad", E_ & dy, L_ & dy, E_, L_),
        ("papers with a repeated stayer dyad; L without entrant key", E_ & dy, L_ & dy & noN, E_, L_),
        ("rolling all-prior teams (H2c(ii))", E_ & roll, L_ & roll, E_, L_),
        ("rolling all-prior; L teams containing an entrant key", E_ & roll, L_ & roll & ~noN, E_, L_),
        ("rolling all-prior; L teams with a returner, no entrant", E_ & roll, L_ & roll & noN & pc.nR.gt(0).to_numpy(), E_, L_),
        ("rolling all-prior; L teams of stayer keys only", E_ & roll, L_ & roll & pc.nS.eq(pc.n_pkeys).to_numpy(), E_, L_),
        ("lag-1 all-prior teams", E_ & lag1, L_ & lag1, E_, L_),
        ("2-year-lookback all-prior teams, E = 2023", E23 & sym2, L_ & sym2, E23, L_),
        ("fixed 2021-22-base all-prior teams, E = 2023", E23 & fixed, L_ & fixed, E23, L_),
    ]
    out = contrasts(pc, defs, n_boot, SEED, controlled=(sample == "all"))
    out.insert(0, "sample", sample)
    out.insert(1, "window", "E=2022-23 (or 2023), L=2025-26")
    return out


def email_newcomer_free(email, papers, n_boot) -> pd.DataFrame:
    em, idxE = code_keys(email)
    rows = []
    for E, L, tag in [((2018,), (2020,), "2018->2020"), ((2017, 2018), (2019, 2020), "2017-18->2019-20")]:
        g = groups_coded(em, E, L, idxE)
        pc = paper_comp(em, papers, g, E + L)
        E_, L_ = pc.year.isin(E).to_numpy(), pc.year.isin(L).to_numpy()
        lS = pc.last_grp.eq("S").to_numpy()
        noN = pc.nN.eq(0).to_numpy()
        allS = (pc.full_profile & pc.nS.eq(pc.n_pkeys)).to_numpy()
        defs = [("population (papers with >= 1 email key)", E_, L_, E_, L_),
                ("last=S", E_ & lS, L_ & lS, E_, L_),
                ("last=S; L papers with an entrant first author", E_ & lS, L_ & lS & pc.first_grp.eq("N").to_numpy(), E_, L_),
                ("last=S; L papers with no entrant key", E_ & lS, L_ & lS & noN, E_, L_),
                ("all-stayer teams", E_ & allS, L_ & allS, E_, L_)]
        o = contrasts(pc, defs, n_boot, SEED, controlled=False)
        o.insert(0, "sample", "email keys")
        o.insert(1, "window", tag)
        rows.append(o)
    return pd.concat(rows, ignore_index=True)


# --------------------------------------------------------------------------------------------
# First list position (H2b)
# --------------------------------------------------------------------------------------------
def first_position(prof, papers, g, n_boot) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    pc = paper_comp(prof, papers, g, E_WIN + L_WIN)
    L_ = pc.year.isin(L_WIN)
    d = pc[L_ & pc.first_grp.isin(["N", "S"]) & pc.n_pkeys.ge(2) & pc.first_key.ne(pc.last_key)
           & pc.last_key.notna()].copy()
    d["entrant_first"] = d.first_grp.eq("N").astype(float)
    d["lk"] = pd.factorize(d.last_key)[0]
    gap = []
    for lab, fe in [("raw", []), ("size-bin + topic100 FE", ["size_bin", "topic100"]), ("last-key FE", ["lk"]),
                    ("last-key + size-bin + topic100 FE", ["lk", "size_bin", "topic100"])]:
        res = C.feols(d, "y", ["entrant_first"], fe=fe, cluster="lk")
        b, se = float(res.params["entrant_first"]), float(res.se["entrant_first"])
        gap.append(dict(analysis="L entrant-first minus stayer-first (D2 groups; multi-key papers, first key != last key)",
                        spec=lab, est=b, se=se, lo=b - 1.96 * se, hi=b + 1.96 * se, nobs=res.nobs,
                        n_lastkeys=int(d.lk.nunique())))
    # symmetric 2-year lookback newcomer premium by year
    r = prof.copy()
    ky = set(zip(r.key_code, r.year))
    r["new2"] = [not (((k, y - 1) in ky) or ((k, y - 2) in ky)) for k, y in zip(r.key_code, r.year)]
    lk = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id").key_code
    pp = papers.set_index("submission_id")
    f = r[r.is_first & r.year.between(2023, 2026)].drop_duplicates("submission_id").copy()
    f["last_key"] = f.submission_id.map(lk)
    f["y"] = f.submission_id.map(pp.name_primary).astype(float)
    f["size_bin"] = f.submission_id.map(pp.size_bin)
    f["topic100"] = f.submission_id.map(pp.topic100)
    f["new"] = f.new2.astype(float)
    cl = f.last_key.to_numpy(dtype=float)
    f["cl"] = np.where(np.isnan(cl), -1 - np.arange(len(f)), cl).astype(np.int64)
    fm = f[f.last_key.notna() & f.last_key.ne(f.key_code)].copy()
    fm["lk"] = pd.factorize(fm.last_key)[0]
    prem = []
    for yr in [2023, 2024, 2025, 2026]:
        dd = fm[fm.year.eq(yr)]
        row = dict(year=yr, n=len(dd), share_new_first=float(dd.new.mean()), NAME_new=float(dd[dd.new.eq(1)].y.mean()),
                   NAME_prior=float(dd[dd.new.eq(0)].y.mean()))
        for lab, fe in [("raw", []), ("lastkey_size_topic", ["lk", "size_bin", "topic100"])]:
            res = C.feols(dd, "y", ["new"], fe=fe, cluster="lk")
            row[f"premium_{lab}"] = float(res.params["new"]); row[f"se_{lab}"] = float(res.se["new"])
        prem.append(row)
    prem = pd.DataFrame(prem)
    dd = fm[fm.year.isin([2023, 2025, 2026])].assign(post=lambda x: x.year.ge(2025).astype(float))
    dd["new_post"] = dd.new * dd.post
    dd["yr"] = dd.year.astype(str)
    res = C.feols(dd, "y", ["new", "new_post"], fe=["lk", "yr", "size_bin", "topic100"], cluster="lk")
    gap.append(dict(analysis="symmetric 2-year-lookback newcomer premium at first position, change 2025-26 vs 2023",
                    spec="last-key + year + size-bin + topic100 FE", est=float(res.params["new_post"]),
                    se=float(res.se["new_post"]), lo=float(res.params["new_post"] - 1.96 * res.se["new_post"]),
                    hi=float(res.params["new_post"] + 1.96 * res.se["new_post"]), nobs=res.nobs,
                    n_lastkeys=int(dd.lk.nunique())))
    gap.append(dict(analysis="symmetric 2-year-lookback newcomer premium at first position, 2023",
                    spec="last-key + year + size-bin + topic100 FE", est=float(res.params["new"]),
                    se=float(res.se["new"]), lo=float(res.params["new"] - 1.96 * res.se["new"]),
                    hi=float(res.params["new"] + 1.96 * res.se["new"]), nobs=res.nobs, n_lastkeys=int(dd.lk.nunique())))
    # change of prior (non-new) first keys relative to the first-position population change, 2023 -> 2025-26
    a = f[f.year.isin([2023, 2025, 2026])]
    Lp = a.year.ge(2025).to_numpy()
    nw = a.new.to_numpy(bool)
    y = a.y.to_numpy(float)
    A = np.column_stack([~Lp, (~Lp) * y, Lp, Lp * y, ~Lp & ~nw, (~Lp & ~nw) * y, Lp & ~nw, (Lp & ~nw) * y,
                         ~Lp & nw, (~Lp & nw) * y, Lp & nw, (Lp & nw) * y]).astype(np.float64)

    def st(T):
        T = np.atleast_2d(T)
        D = T[:, 3] / T[:, 2] - T[:, 1] / T[:, 0]
        Dp = T[:, 7] / T[:, 6] - T[:, 5] / T[:, 4]
        Dn = T[:, 11] / T[:, 10] - T[:, 9] / T[:, 8]
        sE, sL = T[:, 8] / T[:, 0], T[:, 10] / T[:, 2]
        return D, Dp, Dp / D, Dn, sE, sL
    s0 = st(A.sum(0))
    bs = [st(W.astype(np.float64) @ A) for W in C.boot_weights(len(a), n_boot, clusters=a.cl.to_numpy(),
                                                                  seed=SEED, chunk=100)]
    br = np.concatenate([b[2] for b in bs])
    sym = dict(definition="first-position keys, prior = seen in y-1 or y-2 (symmetric 2-year lookback); "
                          "E = 2023, L = 2025-26; all papers with a profile first key",
               pop_change=float(s0[0][0]), prior_change=float(s0[1][0]), ratio_prior=float(s0[2][0]),
               ratio_prior_lo=float(np.quantile(br, .025)), ratio_prior_hi=float(np.quantile(br, .975)),
               new_change=float(s0[3][0]), newcomer_share_E=float(s0[4][0]), newcomer_share_L=float(s0[5][0]))
    return pd.DataFrame(gap), prem, sym


# --------------------------------------------------------------------------------------------
# Two-way dependence: key / paper / row / pigeonhole bootstraps for the headline rho
# --------------------------------------------------------------------------------------------
def twoway_se(prof, papers, g, n_boot=500) -> pd.DataFrame:
    r = prof[prof.year.isin(E_WIN + L_WIN)].merge(papers[["submission_id", "name_primary", "null_Nfirst"]],
                                                    on="submission_id")
    gg = g.reindex(np.arange(int(prof.key_code.max()) + 1)).fillna(False)
    S = gg.S.to_numpy(bool)[r.key_code.to_numpy()]
    Lp = r.year.isin(L_WIN).to_numpy()
    y = r.name_primary.to_numpy(float)
    yn = r.null_Nfirst.to_numpy(float)
    cols, names = [], []
    for part, pm, w in [("last", r.is_last.to_numpy(), np.ones(len(r))), ("first", r.is_first.to_numpy(), np.ones(len(r))),
                        ("any", np.ones(len(r), bool), r.w_any.to_numpy())]:
        for cell, m in [("E", ~Lp), ("L", Lp), ("SE", ~Lp & S), ("SL", Lp & S)]:
            mm = (pm & m) * w
            cols += [mm, mm * y, mm * yn]
            names += [f"{part}_{cell}_w", f"{part}_{cell}_y", f"{part}_{cell}_n"]
    A = np.column_stack(cols).astype(np.float32)
    ix = {n: i for i, n in enumerate(names)}

    def stats(T):
        T = np.atleast_2d(T).astype(np.float64)
        c = lambda n: T[:, ix[n]]
        o = {}
        for part in ("last", "first", "any"):
            def P(cell, v="y"):
                return c(f"{part}_{cell}_{v}") / c(f"{part}_{cell}_w")
            o[f"rho_{part}"] = (P("SL") - P("SE")) / (P("L") - P("E"))
            o[f"null_{part}"] = (P("SL", "n") - P("SE", "n")) / (P("L", "n") - P("E", "n"))
            o[f"rho_minus_null_{part}"] = o[f"rho_{part}"] - o[f"null_{part}"]
        o["first_minus_last"] = o["rho_first"] - o["rho_last"]
        o["any_minus_last"] = o["rho_any"] - o["rho_last"]
        return o
    pt = stats(A.sum(0, dtype=np.float64))
    kc = r.key_code.to_numpy()
    pc_, _ = pd.factorize(r.submission_id)
    K, NP, N = int(kc.max()) + 1, int(pc_.max()) + 1, len(r)
    rng = np.random.default_rng(SEED)
    draws = {s: [] for s in ("key", "paper", "row", "pigeonhole")}
    chunk = 25
    for start in range(0, n_boot, chunk):
        b = min(chunk, n_boot - start)
        wk = rng.multinomial(K, np.full(K, 1 / K), size=b).astype(np.float32)
        wp = rng.multinomial(NP, np.full(NP, 1 / NP), size=b).astype(np.float32)
        wr = rng.multinomial(N, np.full(N, 1 / N), size=b).astype(np.float32)
        for s, W in [("key", wk[:, kc]), ("paper", wp[:, pc_]), ("row", wr), ("pigeonhole", wk[:, kc] * wp[:, pc_])]:
            draws[s].append(stats(W @ A))
    rows = []
    for stat in pt:
        row = dict(stat=stat, est=float(pt[stat][0]))
        for s in draws:
            v = np.concatenate([d[stat] for d in draws[s]])
            v = v[np.isfinite(v)]
            row[f"se_{s}"] = float(v.std(ddof=1))
            if s == "pigeonhole":
                row["pig_lo"], row["pig_hi"] = float(np.quantile(v, .025)), float(np.quantile(v, .975))
        v2 = row["se_key"] ** 2 + row["se_paper"] ** 2 - row["se_row"] ** 2
        row["se_cgm"] = float(np.sqrt(v2)) if v2 > 0 else max(row["se_key"], row["se_paper"])
        row["cgm_lo"], row["cgm_hi"] = row["est"] - 1.96 * row["se_cgm"], row["est"] + 1.96 * row["se_cgm"]
        row["n_boot"] = n_boot
        rows.append(row)
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
# H2d: random-subset benchmark
# --------------------------------------------------------------------------------------------
def h2d_benchmark(prof, papers, g, n_draws=200) -> tuple[pd.DataFrame, dict]:
    mres = json.loads((OUTDIR / "markers_results.json").read_text())
    markers = mres["style_markers"] + mres["topic_markers"]
    pp = papers.copy()
    for k in [m for m in markers if m.startswith("topic_")]:
        pp[k] = (pp.topic100 == int(k.split("_")[1])).astype(int)
    EL = pp[pp.year.isin(E_WIN + L_WIN)]
    isL = EL.year.isin(L_WIN).to_numpy()
    Y = EL[markers].to_numpy(float)
    gg = g.reindex(np.arange(int(prof.key_code.max()) + 1)).fillna(False)
    rr = prof[prof.year.isin(E_WIN + L_WIN)]
    Sr = gg.S.to_numpy(bool)[rr.key_code.to_numpy()]
    ws = rr[Sr].groupby("submission_id").w_any.sum().reindex(EL.submission_id).fillna(0).to_numpy()
    wall = rr.groupby("submission_id").w_any.sum().reindex(EL.submission_id).fillna(0).to_numpy()

    def chg(w):
        return (Y[isL] * w[isL, None]).sum(0) / w[isL].sum() - (Y[~isL] * w[~isL, None]).sum(0) / w[~isL].sum()
    dpop = chg(wall)

    def slope_r(dsub):
        b = np.cov(dpop, dsub)[0, 1] / np.var(dpop, ddof=1)
        return float(b), float(np.corrcoef(dpop, dsub)[0, 1])
    obs = slope_r(chg(ws))
    rng = np.random.default_rng(SEED)
    pE, pL = ws[~isL].sum() / wall[~isL].sum(), ws[isL].sum() / wall[isL].sum()
    sims = []
    for i in range(n_draws):
        u = rng.random(len(EL))
        wr = np.where(isL, u < pL, u < pE).astype(float) * wall
        sims.append(dict(draw=i, **dict(zip(["slope", "r"], slope_r(chg(wr))))))
    sims = pd.DataFrame(sims)
    info = dict(observed_slope=obs[0], observed_r=obs[1], random_subset_slope_mean=float(sims.slope.mean()),
                random_subset_slope_lo=float(sims.slope.quantile(.025)),
                random_subset_slope_hi=float(sims.slope.quantile(.975)),
                random_subset_r_mean=float(sims.r.mean()), random_subset_r_lo=float(sims.r.quantile(.025)),
                stayer_weight_share_E=float(pE), stayer_weight_share_L=float(pL), n_draws=n_draws,
                note="Under the shared-outcome generational null every marker has dS/d = the null rho, so the slope "
                     "equals the any-role null rho (ident_results.json -> null_rho_any).")
    return sims, info


# --------------------------------------------------------------------------------------------
# Family-structured removal simulation
# --------------------------------------------------------------------------------------------
def family_removal(prof, papers, frac=0.2, pis=(0.0, 0.5, 1.0), n_sims=100, seed=SEED) -> pd.DataFrame:
    """Remove `frac` of panel papers; a share pi of them in same-key pairs 1-2 years apart (both papers of a pair
    removed together, resubmission-like), the rest independently at random. rho recomputed as in removal_sim."""
    rng = np.random.default_rng(seed)
    r = prof[prof.year.isin(P.PANEL_YEARS)].merge(papers[["submission_id", "name_primary"]], on="submission_id")
    pcode, puniq = pd.factorize(r.submission_id)
    NPp = len(puniq)
    K = int(r.key_code.max()) + 1
    kc, yr, yy = r.key_code.to_numpy(), r.year.to_numpy(), r.name_primary.to_numpy(float)
    inE, inL = np.isin(yr, E_WIN), np.isin(yr, L_WIN)
    parts = {"last": (r.is_last.to_numpy(), np.ones(len(r))), "first": (r.is_first.to_numpy(), np.ones(len(r))),
             "any": (np.ones(len(r), bool), r.w_any.to_numpy())}
    kp = pd.DataFrame({"k": kc, "p": pcode, "t": yr}).drop_duplicates()
    m = kp.merge(kp, on="k", suffixes=("", "2"))
    m = m[(m.t2 - m.t).between(1, 2)]
    pairs = np.unique(m[["p", "p2"]].to_numpy(np.int64), axis=0)

    def rho_for(keep_p):
        keep = keep_p[pcode]
        pE = np.bincount(kc[keep & inE], minlength=K) > 0
        pL = np.bincount(kc[keep & inL], minlength=K) > 0
        Sr = (pE & pL)[kc]
        out = {}
        for nm, (pm, w) in parts.items():
            mm = keep & pm

            def mean(mask):
                return (w[mask] * yy[mask]).sum() / w[mask].sum()
            out[nm] = (mean(mm & inL & Sr) - mean(mm & inE & Sr)) / (mean(mm & inL) - mean(mm & inE))
        out["n_stayers"] = int((pE & pL).sum())
        return out
    rows = [dict(pi=np.nan, sim=-1, **rho_for(np.ones(NPp, bool)))]
    target = int(round(frac * NPp))
    for pi in pis:
        for s in range(n_sims):
            removed = np.zeros(NPp, bool)
            n_pair_target = int(round(pi * target))
            order = rng.permutation(len(pairs))
            for start in range(0, len(order), 20000):
                if removed.sum() >= n_pair_target:
                    break
                pr = pairs[order[start:start + 20000]]
                ok = ~removed[pr[:, 0]] & ~removed[pr[:, 1]]
                pr = pr[ok]
                # take pairs one batch at a time until the target is reached (pairs may overlap within a batch)
                need = n_pair_target - removed.sum()
                pr = pr[: max(1, int(need // 2))]
                removed[pr[:, 0]] = True
                removed[pr[:, 1]] = True
            rest = target - removed.sum()
            if rest > 0:
                cand = np.where(~removed)[0]
                removed[rng.choice(cand, size=rest, replace=False)] = True
            rows.append(dict(pi=pi, sim=s, frac_removed=float(removed.mean()), **rho_for(~removed)))
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
# Figure F2.2
# --------------------------------------------------------------------------------------------
def fig_decomposition(t21, tw, nf, team, null_rho):
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    C.set_style()
    fig = plt.figure(figsize=(C.DOUBLE_W, 7.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.5], hspace=0.95, wspace=0.75)
    axA, axB, axC, axD = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    parts = [("last", "Last list position"), ("any", "Any role (1/#keys)"), ("first", "First list position")]
    plot_rows = []
    # (a) rho
    for i, (part, lab) in enumerate(parts):
        yv = 2 - i
        r = t21[(t21.spec == f"main|{part}|paper") & (t21.outcome == "name_primary")].iloc[0]
        w = tw[tw.stat == f"rho_{part}"].iloc[0]
        axA.plot([w.cgm_lo, w.cgm_hi], [yv - 0.13] * 2, color=C.COLORS[0], lw=0.9)
        axA.plot([r.rho_lo, r.rho_hi], [yv, yv], color=C.COLORS[0], lw=2.6)
        axA.plot([r.rho], [yv], "o", color=C.COLORS[0], ms=6)
        axA.plot([r.rho_ipw_lo, r.rho_ipw_hi], [yv + 0.25] * 2, color=C.COLORS[1], lw=1.2)
        axA.plot([r.rho_ipw], [yv + 0.25], "D", color=C.COLORS[1], ms=4.5)
        n1 = null_rho["main"][part]["null_Nfirst"]["est"]
        n3 = null_rho["main"][part]["null_NRfirst"]["est"]
        axA.plot([n1], [yv - 0.3], "x", color=C.TEXT, ms=6, mew=1.4)
        axA.plot([n3], [yv - 0.3], "+", color=C.TEXT, ms=7, mew=1.4)
        plot_rows.append(dict(panel="a_rho", label=lab, est=r.rho, lo=r.rho_lo, hi=r.rho_hi, lo_2way=w.cgm_lo,
                              hi_2way=w.cgm_hi, ipw=r.rho_ipw, ipw_lo=r.rho_ipw_lo, ipw_hi=r.rho_ipw_hi,
                              null_Nfirst=n1, null_NRfirst=n3))
    axA.set_yticks([2, 1, 0], [p[1] for p in parts])
    axA.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0); axA.axvline(0, color=C.TEXT2, lw=0.6, zorder=0)
    axA.set_xlim(-0.08, 1.2)
    axA.set_title("(a) Stayer-to-population change ratio ρ", loc="left", fontsize=8.5)
    axA.set_xlabel("(P_SL − P_SE) / (P_L − P_E)")
    axA.legend(handles=[Line2D([], [], color=C.COLORS[0], marker="o", lw=2.6, label="ρ, key-cluster 95% CI"),
                        Line2D([], [], color=C.COLORS[0], lw=0.9, label="two-way (key, paper) 95% CI"),
                        Line2D([], [], color=C.COLORS[1], marker="D", lw=1.2, label="ρ with IPW for staying"),
                        Line2D([], [], color=C.TEXT, marker="x", lw=0, label="null: only entrant-first papers change"),
                        Line2D([], [], color=C.TEXT, marker="+", lw=0, label="null: entrant/returner-first papers")],
               fontsize=6, loc="upper left", bbox_to_anchor=(-0.55, -0.3), ncol=2, columnspacing=1.0)
    # (b) Kitagawa and scenario shares
    for i, (part, lab) in enumerate(parts):
        yv = 2 - i
        r = t21[(t21.spec == f"main|{part}|paper") & (t21.outcome == "name_primary")].iloc[0]
        axB.plot([r.kit_within_share_lo, r.kit_within_share_hi], [yv + 0.18] * 2, color=C.COLORS[2], lw=2)
        axB.plot([r.kit_within_share], [yv + 0.18], "o", color=C.COLORS[2], ms=5)
        axB.plot([r.bound_a_lo, r.bound_a_hi], [yv - 0.18] * 2, color=C.GREY, lw=2)
        axB.plot([r.bound_a], [yv - 0.18], "<", color=C.GREY, ms=5)
        axB.plot([r.bound_b], [yv - 0.18], ">", color=C.GREY, ms=5, mfc="white")
        plot_rows.append(dict(panel="b_shares", label=lab, kit_within=r.kit_within_share, kit_lo=r.kit_within_share_lo,
                              kit_hi=r.kit_within_share_hi, scenario_a=r.bound_a, scenario_a_lo=r.bound_a_lo,
                              scenario_a_hi=r.bound_a_hi, scenario_b=r.bound_b))
    axB.set_yticks([2, 1, 0], [p[1] for p in parts])
    axB.set_xlim(0, 1.05)
    axB.set_title("(b) Shares of the population change", loc="left", fontsize=8.5)
    axB.set_xlabel("Share of P_L − P_E")
    axB.legend(handles=[Line2D([], [], color=C.COLORS[2], marker="o", lw=2, label="Kitagawa within-stayer term (literal PLAN statistic)"),
                        Line2D([], [], color=C.GREY, marker="<", lw=2, label="scenario: exiters frozen at E level"),
                        Line2D([], [], color=C.GREY, marker=">", mfc="white", lw=0, label="scenario: exiters at entrants' L level")],
               fontsize=6, loc="upper left", bbox_to_anchor=(-0.45, -0.3))
    # (c) newcomer-free contrasts
    sel = [("all-stayer teams (every declared position a stayer key)", "All-stayer teams"),
           ("fixed 2021-22-base all-prior teams, E = 2023", "All keys seen 2021-22 (E = 2023)"),
           ("last=S; L papers with no entrant key", "Last=S, L without entrant key"),
           ("papers with a repeated stayer dyad; L without entrant key", "Repeated stayer dyad, no entrant"),
           ("2-year-lookback all-prior teams, E = 2023", "All keys seen in prior 2 years (E = 2023)"),
           ("first=S and last=S (distinct keys)", "First and last both stayers"),
           ("rolling all-prior teams (H2c(ii))", "Rolling all-prior teams (H2c(ii))"),
           ("lag-1 all-prior teams", "All keys seen the year before"),
           ("last=S (rho_last numerator)", "Last=S, all papers (ρ_last)"),
           ("last=S; L papers with an entrant first author", "Last=S, L with entrant first author")]
    d = nf[nf["sample"].eq("all")].set_index("contrast")
    n = len(sel)
    for i, (key, lab) in enumerate(sel):
        r = d.loc[key]
        yv = n - 1 - i
        col = C.COLORS[4] if i < 8 else C.COLORS[0]
        axC.plot([r.ratio_lo, r.ratio_hi], [yv, yv], color=col, lw=2)
        axC.plot([r.ratio], [yv], "o", color=col, ms=5)
        axC.text(1.62, yv, f"{int(r.n_L):,}", va="center", ha="right", fontsize=6, color=C.TEXT2)
        plot_rows.append(dict(panel="c_newcomer_free", label=lab, est=r.ratio, lo=r.ratio_lo, hi=r.ratio_hi,
                              n_E=r.n_E, n_L=r.n_L))
    axC.text(1.62, n - 0.55, "n_L", va="center", ha="right", fontsize=6, color=C.TEXT2)
    axC.set_yticks(list(range(n - 1, -1, -1)), [s[1] for s in sel], fontsize=7)
    axC.set_ylim(-0.6, n - 0.2)
    axC.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0); axC.axvline(0, color=C.TEXT2, lw=0.6, zorder=0)
    axC.axvline(0.5, color=C.GREY, lw=0.6, ls=":", zorder=0)
    axC.set_xlim(-0.5, 1.65)
    axC.set_title("(c) Change on newcomer-free teams / population change", loc="left", fontsize=8.5)
    axC.set_xlabel("Ratio (last-key cluster bootstrap 95% CI)")
    # (d) composition shift-share
    tsel = [("roll", "type", "Rolling"), ("fixed", "type", "Fixed 2021-22 base (E = 2023)"), ("lag1", "type", "Lag-1"),
            ("roll", "type_x_size", "Rolling × size bin"), ("fixed", "type_x_size", "Fixed × size bin (E = 2023)"),
            ("lag1", "type_x_size", "Lag-1 × size bin")]
    for i, (dfn, cells, lab) in enumerate(tsel):
        t = team[(team.definition == dfn) & (team.window == "main") & (team.cells == cells) &
                 (team.stat == "within_share")].iloc[0]
        yv = len(tsel) - 1 - i
        axD.plot([t.lo, t.hi], [yv, yv], color=C.COLORS[2], lw=2)
        axD.plot([t.est], [yv], "o", color=C.COLORS[2], ms=5)
        plot_rows.append(dict(panel="d_composition", label=lab, est=t.est, lo=t.lo, hi=t.hi))
    axD.set_yticks(list(range(len(tsel) - 1, -1, -1)), [s[2] for s in tsel], fontsize=7)
    axD.set_xlim(0.6, 1.05)
    axD.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0)
    axD.set_title("(d) Rise within team-type cells (composition shift-share)", loc="left", fontsize=8.5)
    axD.set_xlabel("Within-cell share of the paper-level rise")
    for ax in (axA, axB, axC, axD):
        ax.grid(axis="y", visible=False); ax.tick_params(axis="y", length=0)
    fig.text(0.0, -0.01, "E = 2022-23, L = 2025-26, NAME (primary). (a) Null markers: ρ that stayers would show if "
             "only papers led by newcomer first keys had changed (titles are shared by co-authors); thin line below each ρ: two-way (key, paper) CI. "
             "(b) Scenario values are not bounds on ρ. (c) Pink: teams without newcomers (fixed-base and 2-year rows use "
             "E = 2023); blue: reference contrasts. (d) Accounting only.", fontsize=6.3, color=C.TEXT2, ha="left", va="top", wrap=True)
    C.save_fig(fig, "fig_F2_2_decomposition", OUTDIR, data=pd.DataFrame(plot_rows))


# --------------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    papers, prof, email = P.load_panel()
    prof, idx = code_keys(prof)
    g = groups_coded(prof, E_WIN, L_WIN, idx)
    from analyses.d2_shiftshare import add_team_sym2, with_nulls
    papers = add_team_sym2(with_nulls(papers, prof, g, E_WIN, L_WIN), prof)
    out = {}

    dy = repeated_dyad_papers(prof, g, E_WIN, L_WIN)
    nf = pd.concat([newcomer_free(prof, papers, g, dy, N_BOOT, "all"),
                    newcomer_free(prof, papers, g, dy, N_BOOT, "NA_pool"),
                    email_newcomer_free(email, papers, N_BOOT)], ignore_index=True)
    # all-prior team rows duplicate H2c(ii) in T2_2b_allprior.csv (d2_shiftshare): take their bootstrap CIs from
    # there so that every table reports one CI per statistic (point estimates are identical by construction)
    ap = pd.read_csv(OUTDIR / "T2_2b_allprior.csv", keep_default_na=False)
    amap = {"rolling all-prior teams (H2c(ii))": ("roll", "main"), "lag-1 all-prior teams": ("lag1", "main"),
            "2-year-lookback all-prior teams, E = 2023": ("sym2", "E2023"),
            "fixed 2021-22-base all-prior teams, E = 2023": ("fixed", "E2023")}
    nf["ci_source"] = "d2_ident (seed %d)" % SEED
    for i, r in nf.iterrows():
        if r.contrast in amap and r["sample"] in ("all", "NA_pool"):
            a = ap[(ap.definition == amap[r.contrast][0]) & (ap.window == amap[r.contrast][1]) & (ap["sample"] == r["sample"])].iloc[0]
            assert abs(a.ratio - r.ratio) < 1e-9, (r.contrast, a.ratio, r.ratio)
            nf.loc[i, ["change_lo", "change_hi", "ratio_lo", "ratio_hi", "p_ratio_ge_0_5"]] = [
                a.allprior_lo, a.allprior_hi, a.ratio_lo, a.ratio_hi, a.p_ratio_ge_0_5]
            nf.loc[i, "ci_source"] = "T2_2b_allprior.csv (d2_shiftshare, seed 20260)"
    nf.to_csv(OUTDIR / "T2_4_newcomer_free.csv", index=False)
    out["newcomer_free"] = nf.to_dict(orient="records")
    print(nf[["sample", "window", "contrast", "n_E", "n_L", "P_E", "P_L", "change", "ratio", "ratio_lo", "ratio_hi",
              "ctl_ratio", "ctl_ratio_lo", "ctl_ratio_hi"]].round(3).to_string(), flush=True)
    print(f"newcomer-free {time.time() - t0:.0f}s", flush=True)

    gap, prem, sym = first_position(prof, papers, g, N_BOOT)
    gap.to_csv(OUTDIR / "h2b_first_position.csv", index=False)
    prem.to_csv(OUTDIR / "h2b_newcomer_premium_by_year.csv", index=False)
    out["h2b_first_position"] = dict(gaps=gap.to_dict(orient="records"), premium_by_year=prem.to_dict(orient="records"),
                                     symmetric_prior_first=sym)
    print(gap.round(4).to_string()); print(prem.round(4).to_string()); print(sym, flush=True)

    tw = twoway_se(prof, papers, g, n_boot=500)
    tw.to_csv(OUTDIR / "T2_1b_twoway_se.csv", index=False)
    out["twoway_se"] = tw.to_dict(orient="records")
    print(tw.round(4).to_string(), flush=True)
    print(f"two-way {time.time() - t0:.0f}s", flush=True)

    sims, h2d = h2d_benchmark(prof, papers, g)
    sims.to_csv(OUTDIR / "h2d_random_subset.csv", index=False)
    ss = json.loads((OUTDIR / "shiftshare_results.json").read_text())
    h2d["null_rho_any"] = ss["null_rho"]["main"]["any"]
    out["h2d_benchmark"] = h2d
    print(h2d, flush=True)

    fam = family_removal(prof, papers)
    fam.to_csv(OUTDIR / "removal_family_sim.csv", index=False)
    base = fam[fam.sim.eq(-1)].iloc[0]
    fsum = []
    for pi, gpi in fam[fam.sim.ge(0)].groupby("pi"):
        for part in ("last", "any", "first"):
            fsum.append(dict(pi_pairs=float(pi), partition=part, rho_observed=float(base[part]),
                             rho_sim_mean=float(gpi[part].mean()), rho_sim_sd=float(gpi[part].std()),
                             shift=float(gpi[part].mean() - base[part]),
                             stayers_sim_mean=float(gpi.n_stayers.mean()), stayers_observed=int(base.n_stayers)))
    out["family_removal"] = fsum
    print(pd.DataFrame(fsum).round(4).to_string(), flush=True)

    t21 = pd.read_csv(OUTDIR / "T2_1_decomposition.csv")
    team = pd.read_csv(OUTDIR / "team_type_shiftshare.csv")
    fig_decomposition(t21, tw, nf, team, ss["null_rho"])
    out["elapsed_s"] = round(time.time() - t0, 1)
    (OUTDIR / "ident_results.json").write_text(json.dumps(out, indent=1, default=float))
    print(f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
