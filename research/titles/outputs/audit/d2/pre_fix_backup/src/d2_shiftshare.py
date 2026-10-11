"""WP6 / D2-H2a, H2b, H2c, H2e: communal vs generational change in NAME titles.

Statistics (PLAN D2). For a partition (last / first list position, any role) and windows E = 2022-23, L = 2025-26:
  * rho = (P_SL - P_SE) / (P_L - P_E): the within-stayer change as a share of the population change. This is
    the "within-stayer share" of H2a/H2b and the "within/pop" ratio of H2d; it is how the pilot numbers
    (last ~1.00, any 0.83, first 0.58) were computed. Under purely communal change rho = 1; under purely
    generational change (stayers keep their E style) rho = 0.
  * The exact Kitagawa three-term identity of the PLAN, reported alongside (T2.1):
        delta = s_bar (P_SL - P_SE) [within] + (1 - s_bar)(P_OL - P_XE) [replacement]
                + (s_L - s_E)(Pbar_S - Pbar_O) [weight shift]
    Its within term equals s_bar * rho * delta, so under purely communal change its share equals the stayer
    weight s_bar, not 1. The H2a/H2b thresholds were calibrated on rho (see RESULTS.md, deviation D2-1).
  * Bounds on the communal share of the E population's change: (a) exiters frozen at their E level
    = s_E * rho; (b) exiters given the entrants' L level = [s_E dS + (1 - s_E)(P_NL - P_XE)] / delta.
  * IPW: stayer keys reweighted by 1/P(stay | E-period covariates) (key-level logit).
  * CIs: key-cluster bootstrap (1,000 reps, the same key draws for every spec, so differences are joint).

Also: held-out-removal simulation (drop 20% of papers x 200, extrapolate coverage 0.8 -> 1.0), alias collapse,
NA pool, non-LLM papers, excluding 2026, 2023 -> 2026, top-1% trim, topic100 / size-bin adjusted outcomes,
partition-specific stayer status, team-type shift-share (rolling, fixed 2021-22 base, lag-1; x size bins),
H2c author-FE LPMs (T2.2) and the H2e email-key replication (2018 -> 2020).

Outputs (outputs/d2_carriers/): T2_1_decomposition.csv, decomposition_long.csv, team_type_shiftshare.csv,
team_type_rates.csv, removal_simulation.csv, ipw_balance.csv, T2_2_author_fe.csv, h2e_email.csv,
fig_F2_2_decomposition.{pdf,png,csv}, fig_F2_3_levels.{pdf,png,csv}, shiftshare_results.json

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_shiftshare [n_boot]
"""
from __future__ import annotations

import json
import sys
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d2_panel as P

OUTDIR = P.OUTDIR
E_WIN, L_WIN = P.E_WIN, P.L_WIN
NAMES = P.NAME_VARS
N_BOOT = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
SEED = 20260
COVERAGE = 0.80  # discovery share of each ICLR year (README / PLAN §4: held-out ~ 20%)


# --------------------------------------------------------------------------------------------
# Spec construction
# --------------------------------------------------------------------------------------------
def code_keys(prof: pd.DataFrame, key: str = "key") -> tuple[pd.DataFrame, pd.Index]:
    idx = pd.Index(sorted(prof[key].unique()))
    prof = prof.copy()
    prof["key_code"] = idx.get_indexer(prof[key])
    return prof, idx


def groups_coded(rows_for_presence: pd.DataFrame, E, L, idx: pd.Index, key: str = "key") -> pd.DataFrame:
    g = P.key_groups(rows_for_presence, E, L, key=key)
    g.index = idx.get_indexer(g.index)
    return g


def adjust_outcome(papers: pd.DataFrame, y: str, fe: str) -> pd.Series:
    """y net of `fe` composition: LPM y ~ year dummies + fe dummies on the given papers; returns
    y - fe_effect + mean(fe_effect), so year effects are kept and only the fe composition is removed."""
    d = papers[[y, fe, "year"]].dropna()
    Xy = pd.get_dummies(d.year.astype(str), dtype=float)
    Xf = pd.get_dummies(d[fe].astype(str), prefix="f", drop_first=True, dtype=float)
    X = np.hstack([Xy.to_numpy(), Xf.to_numpy()])
    beta, *_ = np.linalg.lstsq(X, d[y].to_numpy(float), rcond=None)
    eff = Xf.to_numpy() @ beta[Xy.shape[1]:]
    out = pd.Series(np.nan, index=papers.index)
    out.loc[d.index] = d[y].to_numpy(float) - eff + eff.mean()
    return out


def part_rows(prof: pd.DataFrame, papers: pd.DataFrame, E, L, partition: str, outcomes: list[str],
              weighting: str = "paper", paper_mask: pd.Series | None = None) -> pd.DataFrame:
    r = prof[prof.year.isin(E + L)]
    if partition == "last":
        r = r[r.is_last]
    elif partition == "first":
        r = r[r.is_first]
    elif partition != "any":
        raise ValueError(partition)
    pcols = ["submission_id"] + [o for o in outcomes if o in papers.columns]
    pp = papers if paper_mask is None else papers[paper_mask]
    r = r.merge(pp[list(dict.fromkeys(pcols))], on="submission_id", how="inner")
    r = r.dropna(subset=outcomes)
    r["period"] = np.where(r.year.isin(E), "E", "L")
    base_w = r.w_any if partition == "any" else pd.Series(1.0, index=r.index)
    if weighting == "paper":
        r["w"] = base_w.to_numpy()
    elif weighting == "author":
        n = r.groupby(["key_code", "period"]).key_code.transform("size")
        r["w"] = 1.0 / n
    else:
        raise ValueError(weighting)
    return r


def make_specs(prof, papers, idx, groups_main, E=E_WIN, L=L_WIN, tag="main", outcomes=None, weightings=("paper",),
               partitions=("last", "first", "any"), paper_mask=None, groups=None, ipw=None, part_groups=None,
               meta=None) -> list[P.Spec]:
    outcomes = outcomes or NAMES
    specs = []
    for part in partitions:
        for wt in weightings:
            r = part_rows(prof, papers, E, L, part, outcomes, wt, paper_mask)
            g = groups if groups is not None else groups_main
            if part_groups is not None:
                g = part_groups[part]
            specs.append(P.Spec(name=f"{tag}|{part}|{wt}", rows=r, weight="w", outcomes=outcomes, groups=g,
                                ipw=ipw, meta=dict(variant=tag, partition=part, weighting=wt,
                                                   E="-".join(map(str, E)), L="-".join(map(str, L)),
                                                   **(meta or {}))))
    return specs


# --------------------------------------------------------------------------------------------
# IPW for staying
# --------------------------------------------------------------------------------------------
def staying_ipw(prof, papers, idx, groups, E=E_WIN) -> tuple[pd.Series, pd.DataFrame, dict]:
    from sklearn.linear_model import LogisticRegression
    r = prof[prof.year.isin(E)].merge(papers[["submission_id", "name_primary", "log_authors", "llm_topic", "topic50",
                                               "ACC"]], on="submission_id")
    prior_acc = prof[prof.year <= max(E)].merge(papers[["submission_id", "ACC"]], on="submission_id") \
        .groupby("key_code").ACC.sum()
    k = r.groupby("key_code").agg(n=("submission_id", "size"), name=("name_primary", "mean"),
                                  lauth=("log_authors", "mean"), llm=("llm_topic", "mean"),
                                  last=("is_last", "mean"), first=("is_first", "mean"),
                                  topic=("topic50", lambda s: s.mode().iat[0]))
    k["acc"] = prior_acc.reindex(k.index).fillna(0)
    k["stay"] = groups.reindex(k.index).S.fillna(False).astype(int)
    X = pd.concat([np.log(k[["n"]]), np.log1p(k[["acc"]]), k[["name", "lauth", "llm", "last", "first"]],
                   pd.get_dummies(k.topic.astype(int), prefix="t", drop_first=True, dtype=float)], axis=1)
    Xs = (X - X.mean()) / X.std().replace(0, 1)
    m = LogisticRegression(C=10.0, max_iter=2000)
    m.fit(Xs.to_numpy(), k.stay.to_numpy())
    p = pd.Series(m.predict_proba(Xs.to_numpy())[:, 1], index=k.index).clip(0.02, 0.98)
    w = (1.0 / p)[k.stay.eq(1)]
    w = w.clip(upper=w.quantile(0.99))
    # balance: E-period covariate means, all E keys vs stayers raw vs stayers IPW
    bal = []
    for c in ["n", "acc", "name", "lauth", "llm", "last", "first"]:
        s = k.loc[k.stay.eq(1), c]
        bal.append(dict(covariate=c, all_E_keys=float(k[c].mean()), exiters=float(k.loc[k.stay.eq(0), c].mean()),
                        stayers_raw=float(s.mean()), stayers_ipw=float(np.average(s, weights=w.reindex(s.index)))))
    from sklearn.metrics import roc_auc_score
    info = dict(n_E_keys=int(len(k)), n_stayers=int(k.stay.sum()), auc=float(roc_auc_score(k.stay, p)),
                weight_p99_cap=float(w.max()), ess_stayers=float(w.sum() ** 2 / (w ** 2).sum()))
    return w, pd.DataFrame(bal), info


# --------------------------------------------------------------------------------------------
# Removal simulation
# --------------------------------------------------------------------------------------------
def removal_sim(prof, papers, E=E_WIN, L=L_WIN, fracs=(0.2,), n_sims=200, seed=SEED, y="name_primary") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = prof[prof.year.isin(P.PANEL_YEARS)].merge(papers[["submission_id", y]], on="submission_id")
    pcode, puniq = pd.factorize(r.submission_id)
    K = int(r.key_code.max()) + 1
    kc = r.key_code.to_numpy()
    yr = r.year.to_numpy()
    yy = r[y].to_numpy(float)
    inE_row, inL_row = np.isin(yr, E), np.isin(yr, L)
    before_row = (yr < min(L)) & ~inE_row
    parts = {"last": (r.is_last.to_numpy(), np.ones(len(r))), "first": (r.is_first.to_numpy(), np.ones(len(r))),
             "any": (np.ones(len(r), bool), r.w_any.to_numpy())}

    def rho_for(keep):
        pE = np.bincount(kc[keep & inE_row], minlength=K) > 0
        pL = np.bincount(kc[keep & inL_row], minlength=K) > 0
        S = pE & pL
        out = {}
        for nm, (pm, w) in parts.items():
            m = keep & pm
            Sr = S[kc]
            def tot(mask):
                return (w[mask] * yy[mask]).sum(), w[mask].sum()
            ySE, wSE = tot(m & inE_row & Sr); yE, wE = tot(m & inE_row)
            ySL, wSL = tot(m & inL_row & Sr); yL, wL = tot(m & inL_row)
            out[nm] = ((ySL / wSL) - (ySE / wSE)) / ((yL / wL) - (yE / wE))
            out[nm + "_sE"] = wSE / wE
        out["n_stayers"] = int(S.sum())
        return out

    rows = [dict(frac=0.0, sim=-1, **rho_for(np.ones(len(r), bool)))]
    for f in fracs:
        for s in range(n_sims):
            keep_p = rng.random(len(puniq)) >= f
            rows.append(dict(frac=f, sim=s, **rho_for(keep_p[pcode])))
    return pd.DataFrame(rows)


def extrapolate(sim: pd.DataFrame, part: str, frac: float = 0.2, c0: float = COVERAGE) -> dict:
    r0 = float(sim.loc[sim.frac.eq(0), part].iat[0])
    rs = sim.loc[sim.frac.eq(frac), part]
    c1 = c0 * (1 - frac)
    slope = (r0 - rs.mean()) / (c0 - c1)
    return dict(partition=part, frac=frac, rho_observed=r0, rho_sim_mean=float(rs.mean()),
                rho_sim_sd=float(rs.std()), rho_sim_p2_5=float(rs.quantile(.025)), rho_sim_p97_5=float(rs.quantile(.975)),
                coverage_bias_per_unit=float(slope), rho_extrapolated_full=float(r0 + slope * (1 - c0)))


# --------------------------------------------------------------------------------------------
# Team-type shift-share (paper level)
# --------------------------------------------------------------------------------------------
def team_shiftshare(papers, prof, defs=("roll", "fixed", "lag1"), n_boot=N_BOOT, seed=SEED) -> tuple[pd.DataFrame, pd.DataFrame]:
    last_key = prof[prof.is_last].drop_duplicates("submission_id").set_index("submission_id").key_code
    rows, rates = [], []
    for d in defs:
        for E, L, tag in [((2023,) if d == "fixed" else E_WIN, L_WIN, "main"), ((2023,), (2026,), "2023to2026")]:
            pp = papers[papers.year.isin(E + L) & papers[f"team_{d}"].notna()].copy()
            pp["per"] = np.where(pp.year.isin(E), "E", "L")
            cl = last_key.reindex(pp.submission_id).to_numpy(dtype=float)
            pp["cl"] = np.where(np.isnan(cl), -1 - np.arange(len(pp)), cl).astype(int)
            for cell_by, lab in [([f"team_{d}"], "type"), ([f"team_{d}", "size_bin"], "type_x_size")]:
                pp["cell"] = pp[cell_by].astype(str).agg("|".join, axis=1)
                cells = sorted(pp.cell.unique())
                ci = pd.Index(cells).get_indexer(pp.cell)
                nC = len(cells)
                Ein = pp.per.eq("E").to_numpy()
                y = pp.name_primary.to_numpy(float)
                cols = []
                for per_m in (Ein, ~Ein):
                    Wc = np.zeros((len(pp), nC)); Wc[np.arange(len(pp)), ci] = per_m
                    cols.append(Wc); cols.append(Wc * y[:, None])
                A = np.hstack(cols).astype(np.float32)

                def stat(T):
                    T = np.atleast_2d(T)
                    wE, yE, wL, yL = (T[:, i * nC:(i + 1) * nC] for i in range(4))
                    with np.errstate(divide="ignore", invalid="ignore"):
                        sE, sL = wE / wE.sum(1, keepdims=True), wL / wL.sum(1, keepdims=True)
                        pE, pL = yE / wE, yL / wL
                        PE, PL = yE.sum(1) / wE.sum(1), yL.sum(1) / wL.sum(1)
                        D = PL - PE
                        dP = np.where(np.isfinite(pE) & np.isfinite(pL), pL - pE, 0.0)
                        within = (dP * (sE + sL) / 2).sum(1)
                    return dict(delta=D, within=within, within_share=within / D, P_E=PE, P_L=PL), (sE, sL, pE, pL)

                st0, (sE, sL, pE, pL) = stat(A.sum(0, dtype=np.float64))
                bs = []
                for W in C.boot_weights(len(pp), n_boot, clusters=pp.cl.to_numpy(), seed=seed, chunk=100):
                    bs.append(stat((W @ A).astype(np.float64))[0])
                b = {k: np.concatenate([x[k] for x in bs]) for k in bs[0]}
                for k in ["delta", "within_share"]:
                    rows.append(dict(definition=d, window=tag, E="-".join(map(str, E)), L="-".join(map(str, L)),
                                     cells=lab, stat=k, est=float(st0[k][0]), se=float(np.nanstd(b[k], ddof=1)),
                                     lo=float(np.nanquantile(b[k], .025)), hi=float(np.nanquantile(b[k], .975)),
                                     n_papers=len(pp), n_cells=nC))
                if lab == "type":
                    for j, c in enumerate(cells):
                        rates.append(dict(definition=d, window=tag, type=c, share_E=float(sE[0, j]),
                                          share_L=float(sL[0, j]), P_E=float(pE[0, j]), P_L=float(pL[0, j]),
                                          change=float(pL[0, j] - pE[0, j]),
                                          n_E=int(((ci == j) & Ein).sum()), n_L=int(((ci == j) & ~Ein).sum()),
                                          pop_change=float(st0["delta"][0])))
    return pd.DataFrame(rows), pd.DataFrame(rates)


def allprior_ratio(papers, prof, n_boot=N_BOOT, seed=SEED) -> list[dict]:
    """H2c(ii): NAME change of all-prior (rolling) teams relative to the population change (paper level)."""
    last_key = prof[prof.is_last].drop_duplicates("submission_id").set_index("submission_id").key_code
    out = []
    for E, L, tag in [(E_WIN, L_WIN, "main"), ((2023,), (2026,), "2023to2026")]:
        pp = papers[papers.year.isin(E + L) & papers.team_roll.notna()].copy()
        Ein = pp.year.isin(E).to_numpy()
        ap = pp.team_roll.eq("all_prior").to_numpy()
        y = pp.name_primary.to_numpy(float)
        A = np.column_stack([Ein, Ein * y, ~Ein, (~Ein) * y, Ein & ap, (Ein & ap) * y, (~Ein) & ap,
                             ((~Ein) & ap) * y]).astype(np.float32)
        cl = last_key.reindex(pp.submission_id).to_numpy(dtype=float)
        cl = np.where(np.isnan(cl), -1 - np.arange(len(pp)), cl).astype(int)

        def st(T):
            T = np.atleast_2d(T)
            D = T[:, 3] / T[:, 2] - T[:, 1] / T[:, 0]
            Dap = T[:, 7] / T[:, 6] - T[:, 5] / T[:, 4]
            return D, Dap, Dap / D
        D0, Dap0, r0 = st(A.sum(0, dtype=np.float64))
        bs = [st((W @ A).astype(np.float64)) for W in C.boot_weights(len(pp), n_boot, clusters=cl, seed=seed, chunk=100)]
        bD = np.concatenate([b[0] for b in bs]); bA = np.concatenate([b[1] for b in bs]); bR = np.concatenate([b[2] for b in bs])
        out.append(dict(window=tag, E="-".join(map(str, E)), L="-".join(map(str, L)),
                        pop_change=float(D0[0]), pop_lo=float(np.quantile(bD, .025)), pop_hi=float(np.quantile(bD, .975)),
                        allprior_change=float(Dap0[0]), allprior_lo=float(np.quantile(bA, .025)),
                        allprior_hi=float(np.quantile(bA, .975)), ratio=float(r0[0]),
                        ratio_lo=float(np.quantile(bR, .025)), ratio_hi=float(np.quantile(bR, .975)),
                        allprior_P_E=float(A[:, 5].sum() / A[:, 4].sum()), allprior_P_L=float(A[:, 7].sum() / A[:, 6].sum()),
                        n_allprior_E=int((Ein & ap).sum()), n_allprior_L=int(((~Ein) & ap).sum())))
    return out


# --------------------------------------------------------------------------------------------
# H2c author-FE LPMs (T2.2)
# --------------------------------------------------------------------------------------------
def h2c_models(prof, papers, groups, pop_change: float) -> pd.DataFrame:
    stay_codes = set(groups.index[groups.S])
    r = prof[prof.key_code.isin(stay_codes) & prof.year.between(2022, 2026)].merge(
        papers[["submission_id", "name_primary", "log_authors", "llm_topic", "topic100", "NA"]], on="submission_id")
    r["post"] = (r.year >= 2024).astype(int)
    for y in [2023, 2024, 2025, 2026]:
        r[f"y{y}"] = (r.year == y).astype(int)
    r["w_stay"] = 1.0 / r.groupby("submission_id").key_code.transform("size")
    out = []
    specs = [
        ("primary: key+topic100 FE, rolling new", "share_new_coauth_roll", ["key_code", "topic100"], None, None),
        ("lag-1 new-coauthor definition", "share_new_coauth_lag1", ["key_code", "topic100"], None, None),
        ("no topic100 FE", "share_new_coauth_roll", ["key_code"], None, None),
        ("rows weighted 1/#stayer keys on paper", "share_new_coauth_roll", ["key_code", "topic100"], "w_stay", None),
        ("NA-pool papers only", "share_new_coauth_roll", ["key_code", "topic100"], None, "NA"),
    ]
    for lab, sn, fe, wcol, filt in specs:
        d = r if filt is None else r[r[filt].eq(1)]
        d = d.assign(sn=d[sn], post_sn=d.post * d[sn])
        x = ["y2023", "y2024", "y2025", "y2026", "sn", "post_sn", "log_authors", "llm_topic"]
        d = d.assign(llm_topic=d.llm_topic.astype(float))
        res = C.feols(d, "name_primary", x, fe=fe, cluster="key_code", weights=wcol)
        cvec = pd.Series(0.0, index=res.params.index)
        cvec[["y2025", "y2026"]] = 0.5
        cvec["y2023"] = -0.5
        est = float(cvec @ res.params)
        se = float(np.sqrt(cvec @ res.vcov @ cvec))
        tcrit = stats.t.ppf(0.975, res.df_resid)
        out.append(dict(model=lab, nobs=res.nobs, n_keys=res.n_clusters, n_papers=int(d.submission_id.nunique()),
                        b_post_x_share_new=float(res.params["post_sn"]), se_post_x_share_new=float(res.se["post_sn"]),
                        b_share_new=float(res.params["sn"]), se_share_new=float(res.se["sn"]),
                        change_EtoL_at_share_new0=est, se_change=se, lo_change=est - tcrit * se, hi_change=est + tcrit * se,
                        p_change_le0=float(stats.t.sf(est / se, res.df_resid)),
                        pop_change=pop_change, ratio_to_pop=est / pop_change, ratio_lo=(est - tcrit * se) / pop_change,
                        ratio_hi=(est + tcrit * se) / pop_change,
                        **{f"b_{k}": float(res.params[k]) for k in ["y2023", "y2024", "y2025", "y2026"]},
                        mean_share_new_E=float(d.loc[d.year.isin(E_WIN), "sn"].mean()),
                        mean_share_new_L=float(d.loc[d.year.isin(L_WIN), "sn"].mean())))
    return pd.DataFrame(out)


# --------------------------------------------------------------------------------------------
# Yearly levels (F2.3)
# --------------------------------------------------------------------------------------------
def yearly_levels(prof, papers, groups, K, n_boot=N_BOOT, seed=SEED) -> pd.DataFrame:
    r = prof.merge(papers[["submission_id", "name_primary"]], on="submission_id")
    gS, gX, gN, gR = (groups.reindex(np.arange(K)).fillna(False)[c].astype(bool).to_numpy() for c in "SXNR")
    kc = r.key_code.to_numpy()
    grp = np.select([gS[kc], gX[kc], gN[kc], gR[kc]], ["stayers", "exiters", "entrants", "returners"], "other")
    cells, cols = [], []
    y = r.name_primary.to_numpy(float)
    for part, pm, w in [("last", r.is_last.to_numpy(), np.ones(len(r))), ("first", r.is_first.to_numpy(), np.ones(len(r))),
                        ("any", np.ones(len(r), bool), r.w_any.to_numpy())]:
        for yr in P.PANEL_YEARS:
            for g in ["stayers", "exiters", "entrants", "returners", "all"]:
                m = pm & (r.year.to_numpy() == yr) & ((grp == g) if g != "all" else True)
                if m.sum() == 0:
                    continue
                cells.append((part, yr, g, int(m.sum())))
                cols.append(np.bincount(kc[m], weights=w[m], minlength=K))
                cols.append(np.bincount(kc[m], weights=w[m] * y[m], minlength=K))
    A = np.column_stack(cols)
    tot = A.sum(0)
    est = tot[1::2] / tot[0::2]
    A32 = A.astype(np.float32)
    bs = []
    for W in C.boot_weights(K, n_boot, seed=seed + 7, chunk=50):
        T = (W @ A32).astype(np.float64)
        bs.append(T[:, 1::2] / T[:, 0::2])
    B = np.vstack(bs)
    out = pd.DataFrame(cells, columns=["partition", "year", "group", "rows"])
    out["NAME"] = est
    out["lo"] = np.nanquantile(B, .025, axis=0)
    out["hi"] = np.nanquantile(B, .975, axis=0)
    return out


# --------------------------------------------------------------------------------------------
# Figures
# --------------------------------------------------------------------------------------------
def fig_decomposition(summ: pd.DataFrame, team: pd.DataFrame):
    import matplotlib.pyplot as plt
    rows = []
    for part, lab in [("last", "Last list position"), ("any", "Any role (1/#keys)"), ("first", "First list position")]:
        g = lambda st: summ[(summ.spec == f"main|{part}|paper") & (summ.outcome == "name_primary") & (summ.stat == st)].iloc[0]
        rho, ipw, ba, bb = g("rho"), g("rho_ipw"), g("bound_a"), g("bound_b")
        rows.append(dict(label=lab, est=rho.est, lo=rho.lo, hi=rho.hi, ipw=ipw.est, ipw_lo=ipw.lo, ipw_hi=ipw.hi,
                         bound_a=ba.est, bound_b=bb.est, kind="stayer"))
    for d, lab in [("roll", "Team type, rolling"), ("fixed", "Team type, fixed 2021-22 base"),
                   ("lag1", "Team type, 1-year lookback")]:
        t = team[(team.definition == d) & (team.window == "main") & (team.cells == "type") & (team.stat == "within_share")].iloc[0]
        rows.append(dict(label=lab, est=t.est, lo=t.lo, hi=t.hi, ipw=np.nan, ipw_lo=np.nan, ipw_hi=np.nan,
                         bound_a=np.nan, bound_b=np.nan, kind="team"))
    t = team[(team.definition == "roll") & (team.window == "main") & (team.cells == "type_x_size") & (team.stat == "within_share")].iloc[0]
    rows.append(dict(label="Team type x size, rolling", est=t.est, lo=t.lo, hi=t.hi, ipw=np.nan, ipw_lo=np.nan,
                     ipw_hi=np.nan, bound_a=np.nan, bound_b=np.nan, kind="team"))
    d = pd.DataFrame(rows)
    fig, ax = C.new_fig("double", height=3.0)
    ypos = np.arange(len(d))[::-1]
    for yv, r in zip(ypos, d.itertuples()):
        if np.isfinite(r.bound_a):
            ax.plot([r.bound_a, r.bound_b], [yv - 0.22, yv - 0.22], color=C.GREY, lw=4, solid_capstyle="butt", alpha=0.55)
        col = C.COLORS[0] if r.kind == "stayer" else C.COLORS[2]
        ax.plot([r.lo, r.hi], [yv, yv], color=col, lw=2)
        ax.plot([r.est], [yv], "o", color=col, ms=6)
        if np.isfinite(r.ipw):
            ax.plot([r.ipw], [yv + 0.22], "D", color=C.COLORS[1], ms=5)
    ax.axvline(1.0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.axvline(0.0, color=C.TEXT2, lw=0.6, zorder=0)
    ax.set_yticks(ypos, d.label)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Share of the 2022-23 to 2025-26 NAME rise (within stayers / within team types)")
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=C.COLORS[0], marker="o", lw=2, label="Within-stayer share ρ (95% CI)"),
         Line2D([], [], color=C.COLORS[1], marker="D", lw=0, label="ρ with IPW for staying"),
         Line2D([], [], color=C.GREY, lw=4, alpha=0.55, label="Bounds: exiters frozen (left) / at entrant level (right)"),
         Line2D([], [], color=C.COLORS[2], marker="o", lw=2, label="Within-team-type share (95% CI)")]
    ax.legend(handles=h, loc="lower left", fontsize=7)
    xmin = min(0, np.nanmin(d[["lo", "bound_a"]].to_numpy()) - 0.05)
    ax.set_xlim(xmin, max(1.25, np.nanmax(d[["hi", "bound_b", "ipw"]].to_numpy()) + 0.05))
    C.save_fig(fig, "fig_F2_2_decomposition", OUTDIR, data=d)


def fig_levels(lev: pd.DataFrame):
    fig, axes = C.new_fig("double", height=2.5, ncols=3, sharey=True)
    cols = {"stayers": C.COLORS[0], "entrants": C.COLORS[1], "exiters": C.COLORS[2]}
    for ax, (part, lab) in zip(axes, [("last", "Last list position"), ("first", "First list position"),
                                       ("any", "Any role (1/#keys)")]):
        a = lev[(lev.partition == part) & (lev.group == "all")]
        ax.plot(a.year, a.NAME, color=C.GREY, lw=1.5, marker="o", ms=3.5, label="All panel rows", zorder=1)
        for g, c in cols.items():
            s = lev[(lev.partition == part) & (lev.group == g)].sort_values("year")
            ax.fill_between(s.year, s.lo, s.hi, color=c, alpha=0.15, lw=0)
            ax.plot(s.year, s.NAME, color=c, marker="o", ms=5, label=g.capitalize())
        ax.axvspan(2021.6, 2023.4, color="#f0efec", zorder=0, lw=0)
        ax.axvspan(2024.6, 2026.4, color="#f0efec", zorder=0, lw=0)
        tr = ax.get_xaxis_transform()
        ax.text(2022.5, 0.03, "E window", ha="center", va="bottom", color=C.TEXT2, fontsize=7, transform=tr)
        ax.text(2025.5, 0.03, "L window", ha="center", va="bottom", color=C.TEXT2, fontsize=7, transform=tr)
        ax.set_title(lab)
        ax.set_xticks(list(P.PANEL_YEARS), [str(y)[2:] if y not in (2021, 2026) else str(y) for y in P.PANEL_YEARS])
        ax.set_xlim(2020.6, 2026.4)
    axes[0].set_ylabel("NAME share of titles")
    axes[0].legend(loc="upper left", fontsize=7)
    C.save_fig(fig, "fig_F2_3_levels", OUTDIR, data=lev)


# --------------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    papers, prof, email = P.load_panel()
    prof, idx = code_keys(prof)
    K = len(idx)
    papers = papers.copy()
    g_main = groups_coded(prof, E_WIN, L_WIN, idx)
    log = {}

    # ---------- IPW ----------
    ipw, bal, ipw_info = staying_ipw(prof, papers, idx, g_main)
    bal.to_csv(OUTDIR / "ipw_balance.csv", index=False)
    log["ipw"] = ipw_info
    print("IPW", ipw_info)

    # ---------- adjusted outcomes ----------
    EL = papers.year.isin(E_WIN + L_WIN)
    papers["name_adj_topic"] = np.nan
    papers.loc[EL, "name_adj_topic"] = adjust_outcome(papers[EL], "name_primary", "topic100")
    papers["name_adj_size"] = np.nan
    papers.loc[EL, "name_adj_size"] = adjust_outcome(papers[EL], "name_primary", "size_bin")

    # ---------- specs ----------
    specs = []
    specs += make_specs(prof, papers, idx, g_main, tag="main", weightings=("paper", "author"), ipw=ipw)
    specs += make_specs(prof, papers, idx, g_main, tag="NA_pool", paper_mask=papers.NA.eq(1), outcomes=["name_primary", "name_compound"])
    specs += make_specs(prof, papers, idx, g_main, tag="non_llm", paper_mask=papers.llm_topic.eq(0), outcomes=["name_primary", "name_compound"])
    g_x26 = groups_coded(prof, (2021, 2022), (2024, 2025), idx)
    specs += make_specs(prof, papers, idx, g_x26, E=(2021, 2022), L=(2024, 2025), tag="excl2026", outcomes=["name_primary", "name_compound"])
    for Lc in [(2025,), (2026,)]:  # PLAN §0: 2026 reported as a separate cohort
        g_c = groups_coded(prof, E_WIN, Lc, idx)
        specs += make_specs(prof, papers, idx, g_c, E=E_WIN, L=Lc, tag=f"L{Lc[0]}_only",
                            outcomes=["name_primary", "name_compound"])
    g_2326 = groups_coded(prof, (2023,), (2026,), idx)
    specs += make_specs(prof, papers, idx, g_2326, E=(2023,), L=(2026,), tag="2023to2026", outcomes=["name_primary", "name_compound"])
    # trim top 1% most prolific keys (total panel papers 2021-26)
    npk = prof.groupby("key_code").size()
    top = set(npk.index[npk > npk.quantile(0.99)])
    log["trim_top1pct"] = dict(threshold_papers=float(npk.quantile(0.99)), n_keys_trimmed=len(top))
    prof_trim = prof[~prof.key_code.isin(top)]
    specs += make_specs(prof_trim, papers, idx, g_main, tag="trim_top1pct", outcomes=["name_primary", "name_compound"])
    specs += make_specs(prof, papers, idx, g_main, tag="adj_topic100", outcomes=["name_adj_topic"])
    specs += make_specs(prof, papers, idx, g_main, tag="adj_size_bin", outcomes=["name_adj_size"])
    # partition-specific stayer status (key present in that partition in both windows)
    pg = {}
    for part in ["last", "first", "any"]:
        rr = prof if part == "any" else prof[prof["is_" + part]]
        pg[part] = groups_coded(rr, E_WIN, L_WIN, idx)
    specs += make_specs(prof, papers, idx, g_main, tag="partition_specific_stayers", part_groups=pg, outcomes=["name_primary", "name_compound"])
    print(f"{len(specs)} specs built; bootstrapping {N_BOOT} reps over {K} keys ...", flush=True)
    res = P.run_specs(specs, K, n_boot=N_BOOT, seed=SEED)
    summ = P.summarise(res)
    print(f"  done in {time.time() - t0:.0f}s", flush=True)

    # ---------- alias collapse (own key universe, own bootstrap) ----------
    profA, idxA = code_keys(prof.drop(columns=["key_code"]), key="alias")
    gA = groups_coded(profA, E_WIN, L_WIN, idxA, key="alias")
    profA = profA.assign(key_code=profA.key_code)
    # several profile keys of one alias on the same paper: keep one row per (alias, paper) for first/last/any
    profA = (profA.sort_values("pos").groupby(["submission_id", "key_code"], as_index=False)
             .agg(year=("year", "first"), is_first=("is_first", "max"), is_last=("is_last", "max"),
                  w_any=("w_any", "sum")))
    specsA = make_specs(profA, papers, idxA, gA, tag="alias_collapse", outcomes=["name_primary", "name_compound"])
    resA = P.run_specs(specsA, len(idxA), n_boot=N_BOOT, seed=SEED)
    summ = pd.concat([summ, P.summarise(resA)], ignore_index=True)
    log["alias"] = dict(n_alias_keys=len(idxA), stayers=int(gA.S.sum()), stayers_main=int(g_main.S.sum()))

    # ---------- joint differences (first - last) from the same bootstrap draws ----------
    def joint(spec_a, spec_b, o="name_primary", st="rho"):
        a, b = res[spec_a], res[spec_b]
        est = float(a["point"][o][st][0] - b["point"][o][st][0])
        bd = a["boot"][o][st] - b["boot"][o][st]
        bd = bd[np.isfinite(bd)]
        return dict(est=est, se=float(bd.std(ddof=1)), lo=float(np.quantile(bd, .025)), hi=float(np.quantile(bd, .975)),
                    p_ge0=float(np.mean(bd >= 0)), p_le0=float(np.mean(bd <= 0)))
    diffs = {
        "rho_first_minus_last": joint("main|first|paper", "main|last|paper"),
        "rho_first_minus_last_author_wt": joint("main|first|author", "main|last|author"),
        "rho_first_minus_last_NA": joint("NA_pool|first|paper", "NA_pool|last|paper"),
        "rho_first_minus_last_excl2026": joint("excl2026|first|paper", "excl2026|last|paper"),
        "rho_any_minus_last": joint("main|any|paper", "main|last|paper"),
    }
    log["joint_differences"] = diffs

    # ---------- removal simulation ----------
    t1 = time.time()
    sim = removal_sim(prof, papers, fracs=(0.1, 0.2, 0.3), n_sims=200)
    sim.to_csv(OUTDIR / "removal_simulation.csv", index=False)
    extr = [extrapolate(sim, p, f) for p in ["last", "first", "any"] for f in (0.1, 0.2, 0.3)]
    pd.DataFrame(extr).to_csv(OUTDIR / "removal_extrapolation.csv", index=False)
    log["removal"] = extr
    print(f"removal sim {time.time() - t1:.0f}s", flush=True)

    # ---------- team types ----------
    t1 = time.time()
    team, rates = team_shiftshare(papers, prof)
    team.to_csv(OUTDIR / "team_type_shiftshare.csv", index=False)
    rates.to_csv(OUTDIR / "team_type_rates.csv", index=False)
    ap = allprior_ratio(papers, prof)
    log["allprior_ratio"] = ap
    print(f"team types {time.time() - t1:.0f}s", flush=True)

    # ---------- H2c author-FE models ----------
    pop_any = float(summ[(summ.spec == "main|any|paper") & (summ.outcome == "name_primary") & (summ.stat == "delta")].est.iat[0])
    fe = h2c_models(prof, papers, g_main, pop_any)
    fe.to_csv(OUTDIR / "T2_2_author_fe.csv", index=False)
    print(fe[["model", "nobs", "change_EtoL_at_share_new0", "lo_change", "hi_change", "ratio_to_pop", "b_post_x_share_new", "se_post_x_share_new"]].to_string())

    # ---------- H2e email era ----------
    emailc, idxE = code_keys(email)
    emailc["w_any"] = 1.0 / emailc.groupby("submission_id").key_code.transform("size")
    hspecs = []
    for E, L, tag in [((2018,), (2020,), "email_2018to2020"), ((2017, 2018), (2019, 2020), "email_1718to1920")]:
        gE = groups_coded(emailc, E, L, idxE)
        hspecs += make_specs(emailc, papers, idxE, gE, E=E, L=L, tag=tag, outcomes=["name_primary", "name_compound"],
                             weightings=("paper", "author"))
    resE = P.run_specs(hspecs, len(idxE), n_boot=N_BOOT, seed=SEED)
    summE = P.summarise(resE)
    summE.to_csv(OUTDIR / "h2e_email.csv", index=False)
    summ = pd.concat([summ, summE], ignore_index=True)

    # ---------- yearly levels (F2.3) ----------
    lev = yearly_levels(prof, papers, g_main, K)
    summ.to_csv(OUTDIR / "decomposition_long.csv", index=False)

    # ---------- T2.1 (wide) ----------
    keep = ["P_E", "P_L", "delta", "s_E", "s_L", "P_SE", "P_SL", "P_XE", "P_NL", "P_RL", "rho", "kit_within_share",
            "kit_repl_share", "kit_shift_share", "bound_a", "bound_b", "rho_ipw", "gap_NS_L", "gap_XS_E", "rho_noR"]
    t21 = []
    for (spec, o), g in summ.groupby(["spec", "outcome"], sort=False):
        row = dict(spec=spec, outcome=o, variant=g.variant.iat[0], partition=g.partition.iat[0], weighting=g.weighting.iat[0],
                   E=g.E.iat[0], L=g.L.iat[0])
        gi = g.set_index("stat")
        for st in keep:
            if st in gi.index:
                row[st] = gi.loc[st, "est"]
                if st in ("rho", "delta", "rho_ipw", "gap_NS_L", "gap_XS_E", "kit_within_share", "bound_a", "bound_b"):
                    row[st + "_lo"] = gi.loc[st, "lo"] if "lo" in gi.columns else np.nan
                    row[st + "_hi"] = gi.loc[st, "hi"] if "hi" in gi.columns else np.nan
        allres = {**res, **resA, **resE}
        if spec in allres:
            row.update(allres[spec]["counts"])
        t21.append(row)
    t21 = pd.DataFrame(t21)
    t21.to_csv(OUTDIR / "T2_1_decomposition.csv", index=False)

    # ---------- figures ----------
    fig_decomposition(summ, team)
    fig_levels(lev)

    # ---------- results json ----------
    def pick(spec, st, o="name_primary"):
        r = summ[(summ.spec == spec) & (summ.outcome == o) & (summ.stat == st)]
        if r.empty:
            return None
        r = r.iloc[0]
        return {k: (float(r[k]) if k in r and pd.notna(r[k]) else None) for k in ["est", "se", "lo", "hi"]}
    out = dict(
        n_boot=N_BOOT, seed=SEED, windows=dict(E=E_WIN, L=L_WIN),
        groups_main={k: int(v) for k, v in g_main[["S", "X", "N", "R"]].sum().items()},
        main={part: {wt: {st: pick(f"main|{part}|{wt}", st) for st in keep} for wt in ("paper", "author")}
              for part in ("last", "first", "any")},
        variants={tag: {part: {st: pick(f"{tag}|{part}|paper", st) for st in ["rho", "delta", "P_SE", "P_SL", "gap_NS_L"]}
                        for part in ("last", "first", "any")}
                  for tag in ["NA_pool", "non_llm", "excl2026", "2023to2026", "trim_top1pct", "adj_topic100",
                              "adj_size_bin", "partition_specific_stayers", "alias_collapse", "L2025_only", "L2026_only"]},
        compound_main={part: {st: pick(f"main|{part}|paper", st, "name_compound") for st in ["rho", "delta"]}
                       for part in ("last", "first", "any")},
        name_defs={o: {part: pick(f"main|{part}|paper", "rho", o) for part in ("last", "first", "any")} for o in NAMES},
        h2e={tag: {o: {part: {st: pick(f"{tag}|{part}|paper", st, o) for st in ["rho", "delta", "P_SE", "P_SL"]}
                       for part in ("any", "last", "first")} for o in ("name_primary", "name_compound")}
             for tag in ["email_2018to2020", "email_1718to1920"]},
        h2e_counts={k: v["counts"] for k, v in resE.items()},
        team_types=team.to_dict(orient="records"), allprior=ap, author_fe=fe.to_dict(orient="records"),
        **log, elapsed_s=round(time.time() - t0, 1))
    (OUTDIR / "shiftshare_results.json").write_text(json.dumps(out, indent=1, default=float))
    # bootstrap draws of the key statistics (for Holm p-values in d2_collect)
    draws = {}
    for allres in (res, resA, resE):
        for spec, r in allres.items():
            if r["boot"] is None:
                continue
            for o in r["boot"]:
                if True:
                    for st in ("rho", "delta", "delta_S", "gap_NS_L", "gap_XS_E", "rho_ipw", "P_SL", "P_NL"):
                        if st in r["boot"][o]:
                            draws[f"{spec}::{o}::{st}"] = r["boot"][o][st].astype(np.float32)
    np.savez_compressed(OUTDIR / "shiftshare_boot_draws.npz", **draws)
    print(t21[t21.outcome.eq("name_primary")][["spec", "P_E", "P_L", "delta", "s_E", "s_L", "P_SE", "P_SL", "rho", "rho_lo", "rho_hi",
                                                "kit_within_share", "bound_a", "bound_b", "rho_ipw", "gap_NS_L"]].round(3).to_string())
    print(json.dumps(diffs, indent=1))
    print(f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
