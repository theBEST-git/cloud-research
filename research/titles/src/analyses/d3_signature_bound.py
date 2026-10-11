"""WP7 / D3-H3d (lexical vs structural signature) and H3e (exploratory, bounded second-hand diffusion), PLAN.md D3.

H3d. 2024-26, slot-filled titles (frozen V2 inventory, primary opener rule; the four LLM slots stacked).
    LPM_slot: y_LLM-variant ~ F + slot FE + topic100 x year FE
    LPM_NAME: NAME ~ F + topic100 x year FE, on the same papers
F = F24 or F26 or title typography (features_v2 F_any). Each LPM coefficient is turned into an implied odds ratio at
the F=0 mean of its outcome in the estimation sample: OR = odds(p0 + delta) / odds(p0). Prediction: OR_slot >=
1.5 x OR_NAME; falsified if OR_slot <= OR_NAME. Inference: seemingly-unrelated cluster bootstrap (topic100 clusters
resampled, both LPMs refitted on the same draw; resampled clusters relabelled so duplicates form distinct FE groups),
1,000 draws; one-sided p = share of draws with OR_slot / OR_NAME <= 1.
Robustness: per year; NA pool; F without the RARE21 words that are also slot/R24 stems (harness, unveil); titles whose
abstract contains the slot word excluded; F24 / F26 / title typography separately; NAME on all 2024-26 papers (as D1
H1e-ii, with log authors); logit (slot FE + year FE + topic100 FE) and conditional logit within topic100 x year.

H3e (exploratory). U* = (p_F0,post - p_pre) / (p_F1,post - p_pre): the share of undetected LLM users among F = 0
papers needed to explain their post-2024 rise if non-users stayed at the pre level and users behaved like F = 1 papers.
Pooled over slots with common weights (post slot-title counts), so F0/F1 slot mix does not enter. Primary: post =
2024-25 (2026 not interpreted: fingerprint recall decays), p_pre = 2022-23 (the pilot's baseline; core EARLY).
Sensitivities: 2024, 2025, 2026, 2024-26; baselines 2023, 2018-23 and slot-specific logit trends 2018-23 extrapolated;
F1 contamination: U*_c = U* (1 - c), c = FPR / P(F=1), FPR = P(F=1) in 2021-22. 'Second-hand diffusion' is claimed
only if U* > 0.8 (point estimate, pre-registered rule); otherwise reported as unresolved. CIs: paper bootstrap
stratified by year, 2,000 draws.

Outputs (outputs/d3_register/): signature_models.csv, signature_results.json, secondhand_ustar.csv,
secondhand_shares.csv, fig_F3_4_signature.{pdf,png,csv}, fig_S3_1_secondhand.{pdf,png,csv}

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d3_signature_bound
"""
from __future__ import annotations

import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_vintage as V

warnings.filterwarnings("ignore")
OUTDIR = D3.OUTDIR
SEED = D3.SEED
N_BOOT = 1000
N_BOOT_SEC = 1000  # secondary specifications
N_BOOT_LOGIT = 300
N_BOOT_U = 2000


def implied_or(p0: float, delta: float) -> float:
    p1 = min(max(p0 + delta, 1e-6), 1 - 1e-6)
    p0 = min(max(p0, 1e-6), 1 - 1e-6)
    return (p1 / (1 - p1)) / (p0 / (1 - p0))


def _lpm(d: pd.DataFrame, y: str, x: str, fe: list[str], cluster: str = "topic100", extra=()):
    r = C.feols(d, y, [x, *extra], fe=fe, cluster=cluster)
    return float(r.params[x]), float(r.se[x]), int(r.nobs)


def signature(S: pd.DataFrame, x: str = "F_any", label: str = "", n_boot: int = N_BOOT, seed: int = SEED,
              A: pd.DataFrame | None = None, ctrl: tuple = ()) -> dict:
    """S: stacked slot rows (one per paper x filled LLM slot) for the chosen years. NAME LPM on unique papers (the
    PLAN's same-paper comparator) and, when A is given, on ALL papers of the same years/subset (population
    comparator, audit D3-C1/C7): same topic100 x year FE and the same controls `ctrl` on every side. The same-paper
    comparator is collider-conditioned (the opener rule lets NAME titles fill a slot more often, F raises filling too,
    with a negative interaction), which pushes OR_NAME below 1. Joint topic100-cluster bootstrap: one draw of topics
    resamples S, its papers and A together. Draws: topics of S first (so the same-paper draws reproduce the original
    run), then topics present only in A."""
    S = S.copy()
    S["ty"] = C.fe_interact(S.topic100, S.year)
    Pp = S.drop_duplicates("submission_id").copy()
    ctrl = list(ctrl)
    ds, ses, ns = _lpm(S, "y", x, ["slot", "ty"], extra=ctrl)
    dn, sen, nn = _lpm(Pp, "name_primary", x, ["ty"], extra=ctrl)
    p0s = float(S.loc[S[x] == 0, "y"].mean())
    p0n = float(Pp.loc[Pp[x] == 0, "name_primary"].mean())
    ors, orn = implied_or(p0s, ds), implied_or(p0n, dn)
    out = dict(label=label, x=x, controls="+".join(ctrl) or "none", n_slot_rows=ns, n_papers=nn,
               n_F1=int(Pp[x].sum()), p0_slot=p0s, p0_name=p0n,
               delta_slot_pp=100 * ds, se_slot_pp=100 * ses, delta_name_pp=100 * dn, se_name_pp=100 * sen,
               OR_slot=ors, OR_name=orn, ratio=ors / orn)
    if A is not None:
        A = A.copy()
        A["ty"] = C.fe_interact(A.topic100, A.year)
        da, sea, na = _lpm(A, "name_primary", x, ["ty"], extra=ctrl)
        p0a = float(A.loc[A[x] == 0, "name_primary"].mean())
        ora = implied_or(p0a, da)
        out.update(n_pop=na, n_pop_F1=int(A[x].sum()), p0_name_pop=p0a, delta_name_pop_pp=100 * da,
                   se_name_pop_pp=100 * sea, OR_name_pop=ora, ratio_pop=ors / ora)
    if n_boot:
        rng = np.random.default_rng(seed)
        S = S.reset_index(drop=True)
        Pp = Pp.reset_index(drop=True)
        topics = S.topic100.unique()
        if A is not None:
            A = A.reset_index(drop=True)
            topics = np.concatenate([topics, np.setdiff1d(A.topic100.unique(), topics)])
            A_ix = {t: np.flatnonzero(A.topic100.to_numpy() == t) for t in topics}
            Ax = A[["name_primary", x, "year", *ctrl]]
        S_ix = {t: np.flatnonzero(S.topic100.to_numpy() == t) for t in topics}
        P_ix = {t: np.flatnonzero(Pp.topic100.to_numpy() == t) for t in topics}
        Sx = S[["y", x, "slot", "year", *ctrl]]
        Px = Pp[["name_primary", x, "year", *ctrl]]
        bs = []
        for _ in range(n_boot):
            draw = rng.choice(topics, len(topics), replace=True)
            si = np.concatenate([S_ix[t] for t in draw])
            pi = np.concatenate([P_ix[t] for t in draw])
            Sb = Sx.iloc[si].reset_index(drop=True)
            Pb = Px.iloc[pi].reset_index(drop=True)
            Sb["ty"] = np.repeat(np.arange(len(draw)), [len(S_ix[t]) for t in draw]) * 10000 + Sb.year.to_numpy()
            Pb["ty"] = np.repeat(np.arange(len(draw)), [len(P_ix[t]) for t in draw]) * 10000 + Pb.year.to_numpy()
            if A is not None:
                ai = np.concatenate([A_ix[t] for t in draw])
                Ab = Ax.iloc[ai].reset_index(drop=True)
                Ab["ty"] = np.repeat(np.arange(len(draw)), [len(A_ix[t]) for t in draw]) * 10000 + Ab.year.to_numpy()
            if Sb[x].nunique() < 2 or Pb[x].nunique() < 2 or (A is not None and Ab[x].nunique() < 2):
                continue
            try:
                b_s = float(C.feols(Sb, "y", [x, *ctrl], fe=["slot", "ty"]).params[x])
                b_n = float(C.feols(Pb, "name_primary", [x, *ctrl], fe=["ty"]).params[x])
                b_a = float(C.feols(Ab, "name_primary", [x, *ctrl], fe=["ty"]).params[x]) if A is not None else np.nan
            except Exception:  # noqa: BLE001
                continue
            p0s_b = float(Sb.loc[Sb[x] == 0, "y"].mean())
            p0n_b = float(Pb.loc[Pb[x] == 0, "name_primary"].mean())
            o_s, o_n = implied_or(p0s_b, b_s), implied_or(p0n_b, b_n)
            o_a = implied_or(float(Ab.loc[Ab[x] == 0, "name_primary"].mean()), b_a) if A is not None else np.nan
            bs.append((o_s, o_n, o_s / o_n, 100 * b_s, 100 * b_n, o_a, o_s / o_a))
        bs = np.array(bs)
        lo, hi = np.nanquantile(bs, [0.025, 0.975], axis=0)
        out.update(n_boot=len(bs), OR_slot_lo=lo[0], OR_slot_hi=hi[0], OR_name_lo=lo[1], OR_name_hi=hi[1],
                   ratio_lo=lo[2], ratio_hi=hi[2], p_one_ratio_le1=float((bs[:, 2] <= 1).mean()),
                   p_ratio_lt_1p5=float((bs[:, 2] < 1.5).mean()),
                   delta_slot_lo=lo[3], delta_slot_hi=hi[3], delta_name_lo=lo[4], delta_name_hi=hi[4])
        if A is not None:
            out.update(OR_name_pop_lo=lo[5], OR_name_pop_hi=hi[5], ratio_pop_lo=lo[6], ratio_pop_hi=hi[6],
                       p_one_ratio_pop_le1=float((bs[:, 6] <= 1).mean()),
                       p_ratio_pop_ge_1p5=float((bs[:, 6] >= 1.5).mean()),
                       p_one_OR_slot_le1=float((bs[:, 0] <= 1).mean()))
    return out


def logit_signature(S: pd.DataFrame, x: str = "F_any", n_boot: int = N_BOOT_LOGIT, seed: int = SEED) -> dict:
    """Logit ORs (slot FE + year FE + topic100 FE) for both outcomes, ratio by SUR cluster bootstrap; and
    conditional logit within topic100 x year (point estimates and model SEs)."""
    from statsmodels.discrete.conditional_models import ConditionalLogit
    S = S.copy()
    Pp = S.drop_duplicates("submission_id").copy()

    def fits(Sx, Px):
        Sx = Sx[Sx.groupby("topic100").y.transform("std").fillna(0) > 0]
        Px = Px[Px.groupby("topic100").name_primary.transform("std").fillna(0) > 0]
        rs = C.logit(f"y ~ {x} + C(slot) + C(year) + C(topic100)", Sx)
        rn = C.logit(f"name_primary ~ {x} + C(year) + C(topic100)", Px)
        return rs, rn
    rs, rn = fits(S, Pp)
    out = dict(OR_slot_logit=float(np.exp(rs.params[x])), OR_name_logit=float(np.exp(rn.params[x])))
    out["ratio_logit"] = out["OR_slot_logit"] / out["OR_name_logit"]
    rng = np.random.default_rng(seed + 1)
    topics = S.topic100.unique()
    S_by = {t: g for t, g in S.groupby("topic100")}
    P_by = {t: g for t, g in Pp.groupby("topic100")}
    bs = []
    for _ in range(n_boot):
        draw = rng.choice(topics, len(topics), replace=True)
        Sb = pd.concat([S_by[t].assign(topic100=i) for i, t in enumerate(draw)], ignore_index=True)
        Pb = pd.concat([P_by[t].assign(topic100=i) for i, t in enumerate(draw)], ignore_index=True)
        try:
            a, b = fits(Sb, Pb)
            bs.append((np.exp(a.params[x]), np.exp(b.params[x])))
        except Exception:  # noqa: BLE001
            continue
    bs = np.array(bs)
    r = bs[:, 0] / bs[:, 1]
    out.update(n_boot_logit=len(bs), OR_slot_logit_lo=float(np.quantile(bs[:, 0], 0.025)),
               OR_slot_logit_hi=float(np.quantile(bs[:, 0], 0.975)),
               OR_name_logit_lo=float(np.quantile(bs[:, 1], 0.025)),
               OR_name_logit_hi=float(np.quantile(bs[:, 1], 0.975)),
               ratio_logit_lo=float(np.quantile(r, 0.025)), ratio_logit_hi=float(np.quantile(r, 0.975)),
               p_one_ratio_logit_le1=float((r <= 1).mean()))
    # conditional logit within topic100 x year strata
    for nm, d, y, extra in [("slot", S, "y", ["slot"]), ("name", Pp, "name_primary", [])]:
        d = d.copy()
        d["ty"] = C.fe_interact(d.topic100, d.year)
        d = d[d.groupby("ty")[y].transform("std").fillna(0) > 0]
        X = d[[x]].astype(float)
        if extra:
            X = pd.concat([X, pd.get_dummies(d.slot, drop_first=True, dtype=float)], axis=1)
        m = ConditionalLogit(d[y].astype(float), X, groups=pd.factorize(d.ty)[0]).fit(disp=0)
        out[f"OR_{nm}_clogit"] = float(np.exp(m.params[x]))
        out[f"OR_{nm}_clogit_lo"] = float(np.exp(m.params[x] - 1.96 * m.bse[x]))
        out[f"OR_{nm}_clogit_hi"] = float(np.exp(m.params[x] + 1.96 * m.bse[x]))
        out[f"n_{nm}_clogit"] = int(len(d))
    out["ratio_clogit"] = out["OR_slot_clogit"] / out["OR_name_clogit"]
    return out


# ------------------------------------------------------------------------------------------------
# H3e
# ------------------------------------------------------------------------------------------------
def ustar_table(S: pd.DataFrame, fpr: float, pF: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """S: stacked LLM-slot rows 2018-26 with y, slot, year, F_any. Returns (U* table, cell shares)."""
    slots = D3.SLOTS
    post_sets = {"2024-25": (2024, 2025), "2024": (2024,), "2025": (2025,), "2026": (2026,),
                 "2024-26": (2024, 2025, 2026)}
    base_sets = {"2022-23": (2022, 2023), "2023": (2023,), "2018-23": tuple(range(2018, 2024))}
    S = S.reset_index(drop=True)
    yv = S.y.to_numpy(float)
    # trend-extrapolated baseline: per-slot logit on 2018-23 (llm_topic-free), predicted for each post year
    trend_pred = {}
    for s in slots:
        d = S[(S.slot == s) & (S.year <= 2023)]
        if d.y.nunique() < 2 or len(d) < 20:
            continue
        r = C.logit("y ~ t", d)
        for yr in (2024, 2025, 2026):
            trend_pred[(s, yr)] = float(1 / (1 + np.exp(-(r.params["Intercept"] + r.params["t"] * (yr - 2023)))))
    # indicator columns for cells
    cells = {}
    for s in slots:
        ms = (S.slot == s).to_numpy()
        for bn, yrs in base_sets.items():
            cells[(s, "pre", bn)] = ms & S.year.isin(yrs).to_numpy()
        for yr in (2024, 2025, 2026):
            for f in (0, 1):
                cells[(s, f"F{f}", yr)] = ms & (S.year == yr).to_numpy() & (S.F_any == f).to_numpy()
            cells[(s, "all", yr)] = ms & (S.year == yr).to_numpy()
    keys = list(cells)
    M = np.column_stack([cells[k] for k in keys]).astype(float)

    def stats_from(w):
        num = (w * yv) @ M
        den = w @ M
        return num, den
    num0, den0 = stats_from(np.ones(len(S)))
    W = []
    for Wb in C.boot_weights(len(S), N_BOOT_U, strata=S.year.to_numpy(), clusters=S.submission_id.to_numpy(),
                             seed=SEED):
        W.append(Wb.astype(float))
    W = np.vstack(W)
    NUM = (W * yv) @ M
    DEN = W @ M
    idx = {k: i for i, k in enumerate(keys)}

    def ustar(num, den, post, base, slots_=slots):
        """num/den: arrays (k,) or (B, k). Returns U*, numerator gap, denominator gap (pooled with common weights).
        A slot-year enters only if its baseline, F0 and F1 cells are non-empty (in that draw); otherwise it is skipped
        in numerator, denominator and weights alike (audit D3-C4: empty cells used to count as share 0)."""
        num, den = np.atleast_2d(num), np.atleast_2d(den)
        a = np.zeros(num.shape[0])
        b = np.zeros(num.shape[0])
        wsum = np.zeros(num.shape[0])

        def sh(key):
            i = idx[key]
            d_ = den[:, i]
            return np.where(d_ > 0, num[:, i] / np.maximum(d_, 1e-12), np.nan)
        for s_ in slots_:
            for yr in post:
                wy = den0[idx[(s_, "all", yr)]]  # fixed weights: observed post slot-title counts
                if wy == 0:
                    continue
                if base == "trend":
                    if (s_, yr) not in trend_pred:
                        continue
                    pp = np.full(num.shape[0], trend_pred[(s_, yr)])
                else:
                    pp = sh((s_, "pre", base))
                f0, f1 = sh((s_, "F0", yr)), sh((s_, "F1", yr))
                ok = np.isfinite(pp) & np.isfinite(f0) & np.isfinite(f1)
                a = a + np.where(ok, wy * (f0 - pp), 0.0)
                b = b + np.where(ok, wy * (f1 - pp), 0.0)
                wsum = wsum + np.where(ok, wy, 0.0)
        with np.errstate(invalid="ignore", divide="ignore"):
            u, ga, gb = a / b, a / wsum, b / wsum
        return (u[0], ga[0], gb[0]) if u.shape[0] == 1 else (u, ga, gb)
    rows = []
    for pn, post in post_sets.items():
        c = float(np.mean([fpr / pF[yr] for yr in post]))
        for bn in list(base_sets) + ["trend"]:
            u, ga, gb = ustar(num0, den0, post, bn)
            r = dict(post=pn, baseline=bn, U_star=float(u), gap_F0_pp=100 * float(ga), gap_F1_pp=100 * float(gb),
                     contamination_c=c, U_star_corrected=float(u) * (1 - c))
            if bn != "trend":
                ub, gab, gbb = ustar(NUM, DEN, post, bn)
                ub = np.asarray(ub)
                r.update(U_lo=float(np.nanquantile(ub, 0.025)), U_hi=float(np.nanquantile(ub, 0.975)),
                         p_U_gt_08=float(np.nanmean(ub > 0.8)), gap_F0_lo=100 * float(np.nanquantile(gab, 0.025)),
                         gap_F0_hi=100 * float(np.nanquantile(gab, 0.975)),
                         gap_F1_lo=100 * float(np.nanquantile(gbb, 0.025)),
                         gap_F1_hi=100 * float(np.nanquantile(gbb, 0.975)))
            rows.append(r)
    # sensitivities for the primary window/baseline: without study_adj (2022-23 baseline rests on 4 titles), and a
    # topic100-cluster bootstrap (as for the other D3 CIs) instead of the year-stratified paper bootstrap
    c = float(np.mean([fpr / pF[yr] for yr in (2024, 2025)]))
    op = [x for x in slots if x != "study_adj"]
    u, ga, gb = ustar(num0, den0, (2024, 2025), "2022-23", op)
    ub, _, _ = ustar(NUM, DEN, (2024, 2025), "2022-23", op)
    rows.append(dict(post="2024-25", baseline="2022-23", variant="opener slots only (no study_adj)", U_star=float(u),
                     gap_F0_pp=100 * float(ga), gap_F1_pp=100 * float(gb), contamination_c=c,
                     U_star_corrected=float(u) * (1 - c), U_lo=float(np.nanquantile(ub, 0.025)),
                     U_hi=float(np.nanquantile(ub, 0.975)), p_U_gt_08=float(np.nanmean(ub > 0.8))))
    Wc = np.vstack([w.astype(float) for w in C.boot_weights(len(S), N_BOOT_U, clusters=S.topic100.to_numpy(),
                                                            seed=SEED + 3)])
    ub, _, _ = ustar((Wc * yv) @ M, Wc @ M, (2024, 2025), "2022-23")
    u, ga, gb = ustar(num0, den0, (2024, 2025), "2022-23")
    rows.append(dict(post="2024-25", baseline="2022-23", variant="topic100-cluster bootstrap", U_star=float(u),
                     gap_F0_pp=100 * float(ga), gap_F1_pp=100 * float(gb), contamination_c=c,
                     U_star_corrected=float(u) * (1 - c), U_lo=float(np.nanquantile(ub, 0.025)),
                     U_hi=float(np.nanquantile(ub, 0.975)), p_U_gt_08=float(np.nanmean(ub > 0.8))))
    n_empty = {str(k): float((DEN[:, i] == 0).mean()) for k, i in idx.items()
               if k[1] != "all" and (DEN[:, i] == 0).any() and (k[1] != "pre" or k[2] == "2022-23")}
    # per-slot U* (2024-25 vs 2022-23)
    for s_ in slots:
        u, ga, gb = ustar(num0, den0, (2024, 2025), "2022-23", [s_])
        n_pre = den0[idx[(s_, "pre", "2022-23")]]
        n_f1 = sum(den0[idx[(s_, "F1", yr)]] for yr in (2024, 2025))
        rows.append(dict(post="2024-25", baseline="2022-23", slot=s_, U_star=float(u), gap_F0_pp=100 * float(ga),
                         gap_F1_pp=100 * float(gb), n_pre=int(n_pre), n_F1_post=int(n_f1)))
    U = pd.DataFrame(rows)
    U.attrs["empty_cell_share_of_draws"] = n_empty
    sh_rows = []
    for k, i in idx.items():
        sh_rows.append(dict(slot=k[0], group=k[1], period=str(k[2]), n=den0[i], share=num0[i] / den0[i]
                            if den0[i] else np.nan))
    return U, pd.DataFrame(sh_rows)


def fig_f34(rows: pd.DataFrame):
    import matplotlib.ticker as mticker
    from matplotlib.lines import Line2D
    fig, ax = C.new_fig("double", height=4.2)
    labels, est, lo, hi, cols, fd = [], [], [], [], [], []
    series = [("slot", "LLM slot variant | slot filled", C.COLORS[0]),
              ("name", "NAME title", C.GREY),
              ("name_pop", "NAME title (all papers)", C.COLORS[1])]
    for _, r in rows.iterrows():
        for key, nm, col in series:
            labels.append(f"{r.row}: {nm}")
            est.append(r[f"OR_{key}"])
            lo.append(r[f"OR_{key}_lo"])
            hi.append(r[f"OR_{key}_hi"])
            cols.append(col)
            fd.append(dict(row=r.row, outcome=nm, OR=r[f"OR_{key}"], lo=r[f"OR_{key}_lo"], hi=r[f"OR_{key}_hi"],
                           ratio=r.ratio, ratio_lo=r.ratio_lo, ratio_hi=r.ratio_hi, ratio_pop=r.ratio_pop,
                           ratio_pop_lo=r.ratio_pop_lo, ratio_pop_hi=r.ratio_pop_hi, n_papers=r.n_papers,
                           n_pop=r.n_pop))
    XMIN, XMAX = 0.4, 6.0
    C.forest(ax, labels, est, np.clip(lo, XMIN, XMAX), np.clip(hi, XMIN, XMAX), ref=1.0, log=True, colors=cols)
    ypos = np.arange(len(labels))[::-1]
    for yv, l_, h, col in zip(ypos, lo, hi, cols):
        if l_ < XMIN:
            ax.plot([XMIN], [yv], marker="<", color=col, ms=5, clip_on=False)
        if h > XMAX:
            ax.plot([XMAX], [yv], marker=">", color=col, ms=5, clip_on=False)
    mids, mlabs = [], []
    k3 = len(series)
    for k, (_, r) in enumerate(rows.iterrows()):
        mids.append(ypos[k3 * k + 1])
        mlabs.append(f"{r.row}\nratio, same papers {r.ratio:.2f} [{r.ratio_lo:.2f}, {r.ratio_hi:.2f}]"
                     f"\nratio, all papers {r.ratio_pop:.2f} [{r.ratio_pop_lo:.2f}, {r.ratio_pop_hi:.2f}]")
        if k:
            ax.axhline(ypos[k3 * k] + 0.5, color=C.GRID, lw=0.6)
    ax.set_yticks(mids, mlabs, fontsize=6.5)
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())
    ax.set_xticks([0.5, 0.75, 1, 1.5, 2, 3, 4], ["0.5", "0.75", "1", "1.5", "2", "3", "4"])
    ax.set_xlim(XMIN, XMAX)
    ax.set_xlabel("odds ratio for an abstract LLM fingerprint F (implied by the within topic100 x year LPM; "
                  "95% cluster-bootstrap CI)", fontsize=7.5)
    ax.legend(handles=[Line2D([], [], color=c, marker="o", lw=1.6, label=lab) for lab, c in [
        ("lexical: LLM-favoured slot variant (slot filled)", C.COLORS[0]),
        ("structural: NAME, same slot-filled papers (PLAN; collider-conditioned)", C.GREY),
        ("structural: NAME, all papers (population comparator)", C.COLORS[1])]],
              loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, fontsize=7)
    fig.tight_layout()
    return C.save_fig(fig, "fig_F3_4_signature", OUTDIR, data=pd.DataFrame(fd))


def fig_s31(sh: pd.DataFrame, S: pd.DataFrame):
    """Pooled-slot LLM-variant share by year for F=0 and F=1 papers (2024-26) and all papers (2018-23)."""
    fig, ax = C.new_fig("single", height=2.5)
    rows = []
    for yr in range(2018, 2027):
        d = S[S.year == yr]
        rows.append(dict(year=yr, group="all", n=len(d), share=d.y.mean()))
        if yr >= 2024:
            for f in (0, 1):
                g = d[d.F_any == f]
                rows.append(dict(year=yr, group=f"F{f}", n=len(g), share=g.y.mean()))
    t = pd.DataFrame(rows)
    t["lo"], t["hi"] = D3.wilson(t.share * t.n, t.n)
    a = t[t.group == "all"]
    ax.plot(a.year, a.share, color=C.GREY, marker="o", ms=5, lw=2, label="all slot titles")
    for f, col, lab in [(0, C.COLORS[0], "F = 0 (no abstract fingerprint)"), (1, C.COLORS[1], "F = 1 (fingerprinted)")]:
        g = t[t.group == f"F{f}"]
        ax.errorbar(g.year + (0.08 if f else -0.08), g.share, yerr=[g.share - g.lo, g.hi - g.share], color=col,
                    marker="o", ms=5, lw=2, capsize=0, elinewidth=1.2, label=lab)
    pre = S[S.year.isin([2022, 2023])].y.mean()
    ax.axhline(pre, color=C.GREY, lw=0.8, ls="--")
    ax.text(2021.2, pre + 0.02, "2022-23 level", color=C.TEXT2, fontsize=7)
    ax.set_xticks(range(2018, 2027), [str(y)[2:] if y not in (2018, 2026) else str(y) for y in range(2018, 2027)])
    ax.set_ylim(0, 1)
    ax.set_ylabel("LLM-variant share (pooled slots)")
    ax.legend(loc="upper left", fontsize=6.5)
    fig.tight_layout()
    return C.save_fig(fig, "fig_S3_1_secondhand", OUTDIR, data=t)


def main():
    t0 = time.time()
    inv = D3.frozen_inventory()
    df = V.prep(D3.load_frame())
    df["F_noshared"] = ((df.f24_noshared == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
    df["F_words"] = ((df.f24 == 1) | (df.f26_words_i == 1)).astype(int)
    # D1's fingerprint (d1_decompose: F24 >= 2 words | F26 | title typography), for the cross-direction link (D3-C2)
    df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
    P = D3.slot_panel(df, inv, controls=False)
    # attach extra fingerprint columns
    extra = df[["submission_id", "f24_noshared", "f26_words_i", "f26_typo_i", "f24_2", "lnw", "F_noshared", "F_words",
                "F_d1"]]
    P = P.merge(extra, on="submission_id", how="left")
    post = P[P.year >= 2024].copy()
    acols = ["submission_id", "year", "topic100", "name_primary", "NA", "non_llm", "log_authors", "F_any",
             "F_noshared", "F_words", "F_d1", "f24", "f26", "title_typo"]
    allp = df.loc[df.year >= 2024, acols].copy()
    pre = P[P.year.between(2018, 2023)].copy()
    allpre = df.loc[df.year.between(2018, 2023), acols].copy()

    # ---- H3d: same-paper comparator (PLAN) and population comparator (audit D3-C1), joint bootstrap
    sig = []
    specs = [("2024-26 pooled (primary)", post, "F_any", allp),
             ("2024", post[post.year == 2024], "F_any", allp[allp.year == 2024]),
             ("2025", post[post.year == 2025], "F_any", allp[allp.year == 2025]),
             ("2026", post[post.year == 2026], "F_any", allp[allp.year == 2026]),
             ("2024-25 (excluding 2026)", post[post.year <= 2025], "F_any", allp[allp.year <= 2025]),
             ("NA pool", post[post.NA == 1], "F_any", allp[allp.NA == 1]),
             ("non-LLM subset", post[post.non_llm == 1], "F_any", allp[allp.non_llm == 1]),
             ("F without harness/unveil (shared lemmas)", post, "F_noshared", allp),
             ("abstract lacks the slot word", post[post.in_abs != 1], "F_any", allp),
             ("F24 only as F", post, "f24", allp), ("F26 only as F", post, "f26", allp),
             ("title typography only as F", post, "title_typo", allp),
             ("word fingerprints only (no typography)", post, "F_words", allp),
             ("improve slot only", post[post.slot == "improve"], "F_any", allp),
             ("opener slots only (no study_adj)", post[post.slot != "study_adj"], "F_any", allp),
             ("F_d1 = F24>=2 | F26 | typography (D1 fingerprint)", post, "F_d1", allp),
             ("pre-LLM 2018-23 (fingerprints are false positives)", pre, "F_any", allpre)]
    for k, (lab, d, x, A) in enumerate(specs):
        r = signature(d, x=x, label=lab, n_boot=N_BOOT if k == 0 else N_BOOT_SEC, seed=SEED + k, A=A)
        sig.append(r)
        print(f"  {lab:42s} OR_slot {r['OR_slot']:.2f} [{r.get('OR_slot_lo', np.nan):.2f},{r.get('OR_slot_hi', np.nan):.2f}]"
              f"  OR_name {r['OR_name']:.2f} [{r.get('OR_name_lo', np.nan):.2f},{r.get('OR_name_hi', np.nan):.2f}]"
              f"  ratio {r['ratio']:.2f} [{r.get('ratio_lo', np.nan):.2f},{r.get('ratio_hi', np.nan):.2f}]"
              f"  | pop OR_name {r['OR_name_pop']:.3f} [{r.get('OR_name_pop_lo', np.nan):.3f},"
              f"{r.get('OR_name_pop_hi', np.nan):.3f}] ratio_pop {r['ratio_pop']:.2f} "
              f"[{r.get('ratio_pop_lo', np.nan):.2f},{r.get('ratio_pop_hi', np.nan):.2f}]"
              f"  p(ratio<=1) {r.get('p_one_ratio_le1', np.nan):.3f} p(ratio_pop<=1) "
              f"{r.get('p_one_ratio_pop_le1', np.nan):.3f} n={r['n_papers']}", flush=True)
    # same controls on every side, with log authors (sensitivity; D1 H1e-ii uses log authors)
    r = signature(post, x="F_any", label="2024-26 pooled, + log authors on every side", n_boot=N_BOOT_SEC,
                  seed=SEED + 99, A=allp, ctrl=("log_authors",))
    sig.append(r)
    print("  + log authors:", {k: round(v, 3) for k, v in r.items() if k.startswith(("OR", "ratio"))})
    sig = pd.DataFrame(sig)
    sig["estimable"] = sig.n_F1 >= 30  # fingerprint must occur in >= 30 slot papers
    prim = sig.iloc[0]
    # population NAME comparator (primary spec, no log authors, matching the slot LPM) and the D1 H1e-ii variant
    ab = sig[sig.label == "2024-26 pooled, + log authors on every side"].iloc[0]
    name_all = dict(spec="all 2024-26 papers, NAME ~ F_any within topic100 x year (no further controls; matches the "
                         "slot LPM)", delta_pp=float(prim.delta_name_pop_pp),
                    lo_pp=float(prim.delta_name_pop_pp - 1.96 * prim.se_name_pop_pp),
                    hi_pp=float(prim.delta_name_pop_pp + 1.96 * prim.se_name_pop_pp), p0=float(prim.p0_name_pop),
                    OR=float(prim.OR_name_pop), OR_lo_boot=float(prim.OR_name_pop_lo),
                    OR_hi_boot=float(prim.OR_name_pop_hi), nobs=int(prim.n_pop),
                    ratio_primary_slot_over_population_name=float(prim.ratio_pop),
                    ratio_lo=float(prim.ratio_pop_lo), ratio_hi=float(prim.ratio_pop_hi),
                    with_log_authors_every_side=dict(OR_slot=float(ab.OR_slot), OR_name_pop=float(ab.OR_name_pop),
                                                     OR_name_pop_lo=float(ab.OR_name_pop_lo),
                                                     OR_name_pop_hi=float(ab.OR_name_pop_hi),
                                                     ratio_pop=float(ab.ratio_pop), ratio_pop_lo=float(ab.ratio_pop_lo),
                                                     ratio_pop_hi=float(ab.ratio_pop_hi)))
    print("NAME all 2024-26:", name_all)
    # collider diagnostic: P(slot filled | NAME, F) in 2024-26 (all papers)
    filled = set(P.submission_id)
    dd = allp.assign(filled=allp.submission_id.isin(filled).astype(int))
    cell = dd.groupby(["name_primary", "F_any"]).filled.agg(["mean", "size"])
    sel_factor = float(cell.loc[(1, 1), "mean"] * cell.loc[(0, 0), "mean"] /
                       (cell.loc[(1, 0), "mean"] * cell.loc[(0, 1), "mean"]))
    dd["ty"] = C.fe_interact(dd.topic100, dd.year)
    rf = C.feols(dd.assign(FxN=dd.F_any * dd.name_primary), "filled", ["F_any", "name_primary", "FxN"], fe=["ty"],
                 cluster="topic100")
    collider = dict(p_filled_by_NAME_F={f"NAME{int(a)}_F{int(b)}": float(v) for (a, b), v in cell["mean"].items()},
                    n_by_NAME_F={f"NAME{int(a)}_F{int(b)}": int(v) for (a, b), v in cell["size"].items()},
                    selection_factor_on_OR=sel_factor,
                    lpm_filled_within_ty_pp={k: 100 * float(v) for k, v in rf.params.items()},
                    lpm_filled_within_ty_se_pp={k: 100 * float(v) for k, v in rf.se.items()},
                    note="OR(F,NAME | filled) = OR(F,NAME) x selection factor when selection depends on F and NAME only")
    print("collider:", collider)
    lg = logit_signature(post)
    print("logit / clogit:", lg)
    sig.to_csv(OUTDIR / "signature_models.csv", index=False)

    rows = sig[sig.label.isin(["2024-26 pooled (primary)", "2024", "2025", "2026", "NA pool",
                               "F without harness/unveil (shared lemmas)", "abstract lacks the slot word"])].copy()
    rows["row"] = rows.label.replace({"2024-26 pooled (primary)": "2024-26 pooled",
                                      "F without harness/unveil (shared lemmas)": "F without harness/unveil",
                                      "abstract lacks the slot word": "abstract lacks slot word"})
    fig_f34(rows)

    # ---- H3e
    S_all = P[P.year >= 2018].copy()
    pF = {yr: float(df.loc[df.year == yr, "F_any"].mean()) for yr in (2024, 2025, 2026)}
    fpr = float(df.loc[df.year.isin([2021, 2022]), "F_any"].mean())
    U, shares = ustar_table(S_all, fpr, pF)
    empty_cells = dict(U.attrs.get("empty_cell_share_of_draws", {}))
    print("empty bootstrap cells (share of draws):", empty_cells)
    U.to_csv(OUTDIR / "secondhand_ustar.csv", index=False)
    shares.to_csv(OUTDIR / "secondhand_shares.csv", index=False)
    print(U.to_string())
    fig_s31(shares, S_all)

    up = U[(U.post == "2024-25") & (U.baseline == "2022-23") & U.get("slot", pd.Series(np.nan, index=U.index)).isna()
           & U.get("variant", pd.Series(np.nan, index=U.index)).isna()]
    up = up.iloc[0]
    claim = bool(up.U_star > 0.8)
    verdict_d = dict(OR_slot=prim.OR_slot, OR_slot_lo=prim.OR_slot_lo, OR_slot_hi=prim.OR_slot_hi,
                     OR_name=prim.OR_name, OR_name_lo=prim.OR_name_lo, OR_name_hi=prim.OR_name_hi,
                     ratio=prim.ratio, ratio_lo=prim.ratio_lo, ratio_hi=prim.ratio_hi,
                     p_one_ratio_le1=prim.p_one_ratio_le1, p_ratio_lt_1p5=prim.p_ratio_lt_1p5,
                     prediction_ratio_ge_1p5=bool(prim.ratio >= 1.5), falsified=bool(prim.ratio <= 1),
                     # population comparator (co-primary after the audit; same FE, same controls, joint bootstrap)
                     OR_name_pop=prim.OR_name_pop, OR_name_pop_lo=prim.OR_name_pop_lo,
                     OR_name_pop_hi=prim.OR_name_pop_hi, ratio_pop=prim.ratio_pop, ratio_pop_lo=prim.ratio_pop_lo,
                     ratio_pop_hi=prim.ratio_pop_hi, p_one_ratio_pop_le1=prim.p_one_ratio_pop_le1,
                     p_ratio_pop_ge_1p5=prim.p_ratio_pop_ge_1p5,
                     prediction_ratio_pop_ge_1p5=bool(prim.ratio_pop >= 1.5),
                     ratio_pop_CI_excludes_1=bool(prim.ratio_pop_lo > 1), falsified_pop=bool(prim.ratio_pop <= 1),
                     collider_selection_factor=collider["selection_factor_on_OR"])
    verdict_e = dict(U_star=up.U_star, U_lo=up.U_lo, U_hi=up.U_hi, U_star_corrected=up.U_star_corrected,
                     claim_secondhand_diffusion=claim, lower_CI_above_08=bool(up.U_lo > 0.8),
                     fpr_2021_22=fpr, pF_by_year=pF)
    res = dict(hypotheses=["H3d", "H3e"], signature=sig.to_dict(orient="records"), name_all_2024_26=name_all,
               collider_diagnostic=collider, logit_signature=lg, ustar=U.to_dict(orient="records"),
               ustar_empty_cell_share_of_draws=empty_cells,
               verdict_inputs_H3d=verdict_d, verdict_inputs_H3e=verdict_e, runtime_s=round(time.time() - t0, 1))
    D3.write_json(res, OUTDIR / "signature_results.json")
    print("H3d", verdict_d)
    print("H3e", verdict_e, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
