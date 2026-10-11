"""WP4 final (audit response): camera-ready snapshot bounds on the frozen, complete arXiv audit.

Why a separate module
    `snapshot_bounds.py` is hashed as *required* code in the pre-registration bundle (`outputs/prereg/bundle.sha256`;
    `prereg_confirm` imports it), so it is kept byte-identical. This module imports its building blocks unchanged
    (build_pairs, flip_table, tipping_table, stage_prevalences, pooled, retitling_table, findability models, IPW
    weights, route validation) and implements the fixes requested by the three WP4 audits
    (outputs/audit/snapshot_{code,ident,reporting}; log in outputs/audit/wp4/fix_log.md).

What changes relative to the interim run (`snapshot_bounds.py --enlarge-n 254`, archived in outputs/snapshot/interim_254/)
    1. One frozen audit sample: the original 616-paper audit plus the COMPLETE enlargement cache. The number of lines
       used and the SHA-256 of exactly those bytes are written to results.json (meta.audit_freeze), so D4 and the
       prereg can pass the same --enlarge-n and check the hash.
    2. Primary audit = original + enlargement usable pairs, 2023-26. The 9 accepted-only 2022 pairs have no rejected
       counterpart and are a sensitivity spec (incl_2022); the retitling period contrast is 2024-26 vs 2023.
    3. Auditability = arXiv-channel-measurable AND >= 10 v1-present titles in both arms. arXiv titles never carry
       U+2011/U+2013 typography or ALL-CAPS casing, and arXiv abstracts never carry the em dash (verified on every
       cached arXiv record), so for those features the "net flip" is the stored prevalence itself. The audited
       L-title is R24 or R26 (L_title_words) and the audited O-union is sentence case or question opener
       (O_union_arxiv); the original unions are kept and flagged channel-contaminated.
    4. Gate (PLAN section 4 + section 0 multiplicity): a G_dec acceptance association passes only if the feature is
       auditable, the editing-corrected (universe bootstrap x audit draw) 95% CI excludes 1, and its one-sided
       identification p-value survives Holm across all auditable title features at alpha = 0.025 (the one-sided level
       of the PLAN's 95% CI rule). The p-value tests H0 "true net-flip DiD at or beyond the tipping point"
       with z = (D* - D)/sqrt(se_D^2 + se_D*^2), where se_D is the pseudo-flip SE and se_D* the universe-bootstrap SE
       of the tipping point. The uncorrected interim rule is reported alongside.
    5. v1 timing: v1 posted before the ICLR submission deadline vs during review (approximate public full-paper
       deadlines, SUB_DEADLINE). Retitling and flips are reported by stratum; a timing-standardised spec reweights
       each arm to the pooled year x timing distribution.
    6. Abstract audit pools the enlargement's cached v1 abstracts; G3/G4 use 2024-26 pairs (the H4b/H4c scope) as
       primary and 2023-26 / original-only as sensitivities.
    7. New specs: year-standardised, abstract-matched only (drops pairs admitted only through the title-Jaccard
       clause of arxiv_audit.find), v1-in-review / v1-before-deadline, timing-standardised, new records only, and
       the union with route-B-only pairs (over the 300-paper V7 subsample only).
    8. Reported quantities added: editing share of the NAME excess at the audit point estimate (G at D-hat),
       audit-size multipliers for 50% and 80% power and at the observed point estimate, identification margins,
       a freeze path (verdicts at 254 / 600 / 1,000 / 1,261 / all lines), near-miss bound for V7a, abstract
       Jaccard difference with a bootstrap CI.
    9. Every note in results.json is generated from the tables (no hard-coded conclusions).

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.snapshot_final [--enlarge-n N]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import snapshot_bounds as S

A = S.A
OUTDIR = S.OUTDIR
SEED, N_BOOT, Z, MIN_V1 = S.SEED, S.N_BOOT, S.Z, S.MIN_V1
POST, AUDIT_YEARS = S.POST, S.AUDIT_YEARS
ENLARGE_TARGET = 2000
ALPHA1 = 0.025
Z80 = float(stats.norm.ppf(0.80))
FREEZE_CAPS = (254, 600, 1000, 1261)
# approximate ICLR full-paper submission deadlines (public calls for papers)
SUB_DEADLINE = {2022: "2021-10-05", 2023: "2022-09-28", 2024: "2023-09-28", 2025: "2024-10-01", 2026: "2025-09-24"}

EXTRA_FEATS = [("L_title_words", "L-title words (R24 or R26)", "L", "L_title_words"),
               ("O_union_arxiv", "O-union w/o ALL-CAPS", "O", "O_union_arxiv")]
for _k, _lab, _fam, _col in EXTRA_FEATS:  # runtime registration only; snapshot_bounds.py is not modified
    S.FEAT_LABEL[_k], S.FEAT_FAMILY[_k], S.FEAT_COL[_k] = _lab, _fam, _col
KEYS_T = [k for k, *_ in S.TITLE_FEATS] + [k for k, *_ in EXTRA_FEATS]
KEYS_A = [k for k, *_ in S.ABS_FEATS]
CHANNEL = {
    "title_typo": "arXiv titles never carry U+2011 / U+2013 typography",
    "all_caps_title": "arXiv titles are never ALL-CAPS",
    "L_title": "contains title typography (channel-unauditable)",
    "O_union": "contains ALL-CAPS title (channel-unauditable)",
    "abs_emdash": "arXiv abstracts carry TeX dashes, never U+2014",
    "L_abstract": "contains the em dash (channel-unauditable)",
}
LABEL = dict(S.FEAT_LABEL)

_LOG: list[str] = []


def log(msg: str):
    print(msg, flush=True)
    _LOG.append(msg)


def f2(x, d=2):
    return "nan" if x is None or not np.isfinite(x) else f"{x:.{d}f}"


def pp(x, d=2, sign=True):
    """fraction -> percentage-point string"""
    if x is None or not np.isfinite(x):
        return "nan"
    return f"{100 * x:+.{d}f}" if sign else f"{100 * x:.{d}f}"


# ------------------------------------------------------------------------------------------------
# frozen inputs
# ------------------------------------------------------------------------------------------------
def read_frozen(path: Path, n_lines: int | None = None) -> tuple[pd.DataFrame, int, str]:
    """Complete (newline-terminated) lines of an append-only jsonl, optionally the first n; same convention and
    hash as prereg_confirm._complete_jsonl (SHA-256 of exactly the bytes used)."""
    if not path.exists():
        return pd.DataFrame(), 0, ""
    raw = [ln for ln in path.read_bytes().splitlines(keepends=True) if ln.endswith(b"\n")]
    if n_lines is not None:
        raw = raw[:n_lines]
    recs = []
    for ln in raw:
        try:
            recs.append(json.loads(ln))
        except ValueError:
            continue
    return pd.DataFrame(recs), len(raw), hashlib.sha256(b"".join(raw)).hexdigest()


def clean(rec: pd.DataFrame) -> pd.DataFrame:
    if rec.empty:
        return rec
    r = rec[rec.error.isna()] if "error" in rec else rec
    return r.drop_duplicates("submission_id", keep="last").reset_index(drop=True)


def add_extra(P: pd.DataFrame) -> pd.DataFrame:
    if P.empty:
        return P
    P = P.copy()
    for s in ("or", "v1"):
        P[f"L_title_words_{s}"] = (P[f"R24_{s}"].astype(bool) | P[f"R26_{s}"].astype(bool)).astype(int)
        P[f"O_union_arxiv_{s}"] = (P[f"sentence_case_{s}"].astype(bool) |
                                   P[f"question_opener_{s}"].astype(bool)).astype(int)
    lag = (pd.to_datetime(P.v1_date) - pd.to_datetime(P.year.map(SUB_DEADLINE))).dt.days
    P["v1_lag_days"] = lag
    P["v1_in_review"] = (lag > 0).astype(int)
    return P


def pairs(rec: pd.DataFrame, U: pd.DataFrame, source: str, v1_abstract: bool = False) -> pd.DataFrame:
    P = S.build_pairs(rec, U, source, v1_abstract=v1_abstract)
    if P.empty:
        return P
    P = add_extra(P)
    aj = rec.drop_duplicates("submission_id", keep="last").set_index("submission_id").abstract_jaccard
    P["abstract_jaccard_latest"] = P.submission_id.map(aj).astype(float)
    return P


# ------------------------------------------------------------------------------------------------
# flips, tipping, gate
# ------------------------------------------------------------------------------------------------
def std_weights(P: pd.DataFrame, strata: pd.Series) -> np.ndarray:
    """Reweight each arm to the pooled distribution of `strata` (each stratum must occur in both arms)."""
    s = strata.astype(str).reset_index(drop=True)
    share = s.value_counts(normalize=True)
    w = np.empty(len(P))
    for arm in (1, 0):
        m = (P.acc.to_numpy() == arm)
        sa = s[m].value_counts(normalize=True)
        w[m] = s[m].map(share / sa).to_numpy()
    if not np.isfinite(w).all():
        raise ValueError("a stratum is missing from one arm")
    return w


def flips(P: pd.DataFrame, keys: list[str], label: str, w: np.ndarray | None = None) -> tuple[pd.DataFrame, np.ndarray]:
    P = P.reset_index(drop=True)
    ft, db = S.flip_table(P, keys, label, w=w, Wb=S.boot_matrix(P))
    ft["auditable_count"] = ft.auditable
    ft["channel_ok"] = ~ft.feature.isin(CHANNEL)
    ft["channel_note"] = ft.feature.map(CHANNEL).fillna("")
    ft["auditable"] = ft.auditable_count & ft.channel_ok
    return ft, db


def holm(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    adj = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    idx = np.where(ok)[0][np.argsort(p[ok])]
    m, run = len(idx), 0.0
    for i, j in enumerate(idx):
        run = max(run, min(1.0, (m - i) * p[j]))
        adj[j] = run
    return adj


def tipping(Pt: np.ndarray, apool: np.ndarray, keys: list[str], ft: pd.DataFrame, db: np.ndarray,
            period: str) -> pd.DataFrame:
    """snapshot_bounds.tipping_table plus identification p-values, editing shares and audit-size multipliers."""
    tp = S.tipping_table(Pt, apool, keys, ft, db, period)
    fl = ft.set_index("feature")
    nb = min(Pt.shape[0] - 1, db.shape[0])
    for name, k_idx, a_idx in [("dec", 1, 1), ("total", 0, 0)]:
        cols = {c: [] for c in ["tip_se_pp", "z_ident", "p_ident", "p_ident_draw", "excess_share_edit",
                                "excess_share_edit_lo", "excess_share_edit_hi", "n_mult_D0_50", "n_mult_D0_80",
                                "n_mult_obs_50", "corr_check"]}
        for j, k in enumerate(keys):
            b, ab = Pt[1:nb + 1, j], apool[1:nb + 1]
            with np.errstate(invalid="ignore", divide="ignore"):
                tip_b = (b[:, 2] - b[:, k_idx]) / (1 - ab[:, a_idx])
            se_tip = float(np.nanstd(tip_b, ddof=1))
            r = tp.iloc[j]
            tip, Gobs = r[f"tip_{name}_pp"] / 100, r[f"G_{name}_obs"]
            D, se = float(fl.loc[k, "did"]), float(fl.loc[k, "did_se"])
            sgn = 1.0 if Gobs >= 1 else -1.0
            z = sgn * (tip - D) / np.sqrt(se ** 2 + se_tip ** 2)
            # corrected draws exactly as in snapshot_bounds.tipping_table (same seeds) -> draw-based p
            rng = np.random.default_rng(SEED + 31 * j + (0 if name == "dec" else 1))
            Dc = np.clip(rng.normal(D, se, nb), b[:, 2] - 1, b[:, 2])
            den = b[:, k_idx] - ab[:, a_idx] * Dc
            with np.errstate(invalid="ignore", divide="ignore"):
                Gc = np.where(den > 0, (b[:, 2] - Dc) / np.where(den > 0, den, 1), np.nan)
            wrong = (Gc <= 1) if Gobs >= 1 else (Gc >= 1)
            wrong |= ~np.isfinite(Gc)
            q_ = float(np.nanquantile(Gc, .025)) if np.isfinite(Gc).any() else np.nan
            ref_ = r[f"G_{name}_corr_lo95"]
            cols["corr_check"].append(bool((np.isnan(q_) and np.isnan(ref_)) or abs(q_ - ref_) < 1e-12))
            cols["tip_se_pp"].append(100 * se_tip)
            cols["z_ident"].append(float(z))
            cols["p_ident"].append(float(stats.norm.sf(z)))
            cols["p_ident_draw"].append(float((1 + wrong.sum()) / (nb + 1)))
            ex = Gobs - 1
            g_at = r[f"G_{name}_sel_point"]
            if abs(ex) > 1e-9 and np.isfinite(g_at):
                cols["excess_share_edit"].append(float((Gobs - g_at) / ex))
                lo_, hi_ = (Gobs - r[f"G_{name}_audit_hi"]) / ex, (Gobs - r[f"G_{name}_audit_lo"]) / ex
                cols["excess_share_edit_lo"].append(float(min(lo_, hi_)))
                cols["excess_share_edit_hi"].append(float(max(lo_, hi_)))
            else:
                for c in ["excess_share_edit", "excess_share_edit_lo", "excess_share_edit_hi"]:
                    cols[c].append(np.nan)
            same = sgn * tip > 0
            cols["n_mult_D0_50"].append(float((Z * se / tip) ** 2) if same else np.nan)
            cols["n_mult_D0_80"].append(float(((Z + Z80) * se / tip) ** 2) if same else np.nan)
            gap = sgn * (tip - D)
            cols["n_mult_obs_50"].append(float((Z * se / gap) ** 2) if gap > 0 else np.nan)
        for c, v in cols.items():
            tp[f"{c}_{name}" if not c.startswith("tip_se") else f"tip_{name}_se_pp"] = v
        assert all(cols["corr_check"]), "corrected draws do not reproduce snapshot_bounds.tipping_table"
    tp = tp.drop(columns=[c for c in tp.columns if c.startswith("corr_check")])
    return tp


def gate_dec(tp: pd.DataFrame) -> pd.DataFrame:
    """Multiplicity-controlled gate for G_dec acceptance associations (family = auditable features in `tp`)."""
    tp = tp.copy()
    aud = tp.auditable.to_numpy(bool)
    p = np.where(aud, tp.p_ident_dec, np.nan)
    tp["p_holm_dec"] = holm(p)
    excl = np.where(tp.G_dec_obs >= 1, tp.G_dec_corr_lo95 > 1, tp.G_dec_corr_hi95 < 1)
    tp["G_dec_corr_ci_excl1_side"] = excl
    tp["passes_uncorrected_dec"] = tp.claim_dec_passes_gate.astype(bool)
    tp["passes_holm_dec"] = aud & excl & (tp.p_holm_dec < ALPHA1)
    tp["holm_family_size"] = int(aud.sum())
    return tp


# ------------------------------------------------------------------------------------------------
# small helpers
# ------------------------------------------------------------------------------------------------
def boot_diff_mean(x: np.ndarray, acc: np.ndarray, n_boot: int = N_BOOT, seed: int = SEED) -> tuple[float, float, float]:
    rng = np.random.default_rng(seed)
    a, r = x[acc], x[~acc]
    bs = [rng.choice(a, len(a)).mean() - rng.choice(r, len(r)).mean() for _ in range(n_boot)]
    return float(a.mean() - r.mean()), float(np.quantile(bs, .025)), float(np.quantile(bs, .975))


def near_miss_bound(route: pd.DataFrame) -> dict:
    """V7a: papers neither route found that have a same-surname, date-plausible candidate below the tiers."""
    r = clean(route)
    if r.empty:
        return {}

    def best(rec):
        out = 0.0
        for q in rec.get("queries") or []:
            for c in q.get("cands") or []:
                if c.get("sn_ok") and c.get("tier") is None and c.get("pub") and \
                        int(rec["year"]) - 2 <= int(str(c["pub"])[:4]) <= int(rec["year"]) + 1:
                    out = max(out, c.get("jac") or 0.0)
        return out
    r["nm"] = [best(x) for x in r.to_dict("records")]
    r["foundA"] = r.orig_found.astype(bool)
    r["foundB"] = r.found.astype(bool)
    r["acc"] = r.decision.eq("accepted")
    out = {}
    for thr in (0.10, 0.05):
        row = {}
        for dec, g in r.groupby("decision"):
            un = ~g.foundA & ~g.foundB
            nm = int((un & (g.nm >= thr)).sum())
            row[dec] = dict(n=int(len(g)), union_found=int((g.foundA | g.foundB).sum()), near_miss=nm,
                            union_rate=float((g.foundA | g.foundB).mean()),
                            bound_rate=float(((g.foundA | g.foundB) | (un & (g.nm >= thr))).mean()))
        row["gap_union"] = row["accepted"]["union_rate"] - row["rejected"]["union_rate"]
        row["gap_bound"] = row["accepted"]["bound_rate"] - row["rejected"]["bound_rate"]
        out[f"jac_ge_{thr:.2f}"] = row
    return out


# ------------------------------------------------------------------------------------------------
# figures
# ------------------------------------------------------------------------------------------------
def fig_findability(fr: pd.DataFrame, rt: pd.DataFrame):
    fig, axes = C.new_fig("double", 3.1, ncols=2)
    f = fr[(fr.source == "original+enlarge") & fr.year.isin(AUDIT_YEARS)].copy()
    f["year"] = f.year.astype(int)
    rows = []
    h = rt[(rt.spec == "primary") & (rt.measure == "changed_norm") & rt.years.isin([str(y) for y in AUDIT_YEARS])]
    h = h.assign(year=h.years.astype(int)).sort_values("year")
    for i, (dec, lab, col) in enumerate([("accepted", "Accepted", "acc"), ("rejected", "Rejected", "rej")]):
        g = f[f.decision == dec].sort_values("year")
        off = -0.07 if i == 0 else 0.07
        ax = axes[0]
        ax.errorbar(g.year + off, g.found_rate, yerr=[g.found_rate - g.found_lo, g.found_hi - g.found_rate],
                    color=C.color(i), marker="o", ms=5, lw=2, capsize=0, elinewidth=1.0, label=f"{lab}: found")
        ax.errorbar(g.year + off, g.usable_rate, yerr=[g.usable_rate - g.usable_lo, g.usable_hi - g.usable_rate],
                    color=C.color(i), marker="s", ms=4.5, lw=1.2, ls="--", capsize=0, elinewidth=0.8,
                    label=f"{lab}: usable pre-decision pair")
        for _, rr in g.iterrows():
            for ser, v, lo, hi in [("found", rr.found_rate, rr.found_lo, rr.found_hi),
                                   ("usable", rr.usable_rate, rr.usable_lo, rr.usable_hi)]:
                rows.append(dict(panel="a", series=f"{dec}_{ser}", year=rr.year, value=v, lo=lo, hi=hi, n=rr.n))
        ax = axes[1]
        ax.errorbar(h.year + off, h[f"rate_{col}"], yerr=[h[f"rate_{col}"] - h[f"rate_{col}_lo"],
                                                        h[f"rate_{col}_hi"] - h[f"rate_{col}"]],
                    color=C.color(i), marker="o", ms=5, lw=2, capsize=0, elinewidth=1.0, label=lab)
        for _, rr in h.iterrows():
            ax.annotate(f"{int(rr[f'n_{col}'])}", (rr.year + off, rr[f"rate_{col}_lo"]), xytext=(0, -9),
                        textcoords="offset points", ha="center", fontsize=6, color=C.color(i))
            rows.append(dict(panel="b", series=f"{dec}_retitled", year=rr.year, value=rr[f"rate_{col}"],
                             lo=rr[f"rate_{col}_lo"], hi=rr[f"rate_{col}_hi"], n=rr[f"n_{col}"]))
    axes[0].set_ylim(0, 1.02)
    axes[0].set_ylabel("Share of audited papers")
    axes[0].set_title("a  arXiv findability (title route), 95% CI", loc="left")
    axes[1].set_ylim(0, max(0.6, float(h[["rate_acc_hi", "rate_rej_hi"]].max().max()) + 0.05))
    axes[1].set_ylabel("Share of usable pairs retitled")
    axes[1].set_title("b  v1 title differs from stored title (n = pairs)", loc="left")
    axes[1].legend(title="Share of usable pairs retitled", loc="upper left", fontsize=7, title_fontsize=7)
    for ax in axes:
        ax.set_xticks(list(AUDIT_YEARS))
        ax.set_xlabel("ICLR year")
    hh, ll = axes[0].get_legend_handles_labels()
    axes[0].legend(hh, ll, loc="upper center", bbox_to_anchor=(0.5, -0.24), fontsize=6.5, ncol=2, frameon=False)
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    C.save_fig(fig, "fig_S1_findability_retitling", OUTDIR, data=pd.DataFrame(rows))


def fig_tipping(tp: pd.DataFrame, tpa: pd.DataFrame):
    t = pd.concat([tp.assign(kind="title"), tpa.assign(kind="abstract")], ignore_index=True)
    t["tip_pp"] = np.where(t.kind == "title", t.tip_dec_pp, t.tip_total_pp)
    t["Gobs"] = np.where(t.kind == "title", t.G_dec_obs, t.G_total_obs)
    t["Glo"] = np.where(t.kind == "title", t.G_dec_lo95, t.G_total_lo95)
    t["Ghi"] = np.where(t.kind == "title", t.G_dec_hi95, t.G_total_hi95)
    t["Galo"] = np.where(t.kind == "title", t.G_dec_audit_lo, t.G_total_audit_lo)
    t["Gahi"] = np.where(t.kind == "title", t.G_dec_audit_hi, t.G_total_audit_hi)
    t["chan"] = t.feature.isin(CHANNEL)
    t["mark"] = np.where(t.chan, "‡ ", np.where(t.auditable, "", "† "))
    t["ylabel"] = t.mark + t.label.astype(str) + np.where(t.kind == "abstract", " [abs, total]", "")
    n = len(t)
    fig, axes = C.new_fig("double", 0.17 * n + 1.5, ncols=2, sharey=True)
    ypos = np.arange(n)[::-1]
    ax = axes[0]
    for yv, (_, r) in zip(ypos, t.iterrows()):
        c = C.color(0) if r.auditable else C.GREY
        ax.plot([r.did_lo_pp, r.did_hi_pp], [yv, yv], color=c, lw=1.8, solid_capstyle="butt", zorder=2)
        ax.plot([r.tip_pp], [yv], "|", color=C.color(1), ms=11, mew=2.2, zorder=3)
        ax.plot([r.did_pp], [yv], "o", color=c, ms=4.5, mec="white", mew=0.6, zorder=4)
    ax.axvline(0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_yticks(ypos, list(t.ylabel))
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Percentage points")
    ax.set_title("a  Net-flip DiD (95% CI) vs D*", loc="left")
    ax.plot([], [], color=C.color(0), lw=1.8, marker="o", ms=4.5, label="Net-flip DiD (95% CI), auditable")
    ax.plot([], [], color=C.GREY, lw=1.8, marker="o", ms=4.5, label="Net-flip DiD, † too few v1 / ‡ channel")
    ax.plot([], [], "|", color=C.color(1), ms=11, mew=2.2, label="D* (titles: G_dec = 1; abstracts: G_total = 1)")
    lim = np.nanmax(np.abs(np.r_[t.did_lo_pp, t.did_hi_pp, t.tip_pp])) * 1.08
    ax.set_xlim(-lim, lim)
    ax = axes[1]
    for yv, (_, r) in zip(ypos, t.iterrows()):
        c = C.color(0) if r.auditable else C.GREY
        if np.isfinite(r.Galo) and np.isfinite(r.Gahi):
            ax.plot([r.Galo, r.Gahi], [yv, yv], color=c, lw=1.8, solid_capstyle="butt", alpha=0.85, zorder=2)
        ax.plot([r.Glo, r.Ghi], [yv + 0.28] * 2, color=C.TEXT, lw=0.9, zorder=3)
        ax.plot([r.Gobs], [yv + 0.28], "o", color=C.TEXT, ms=3.5, zorder=4)
    ax.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_xlim(0, 2.5)
    ax.set_xlabel("G = P(f | accepted) / P(f | reviewed or all)")
    ax.set_title("b  Observed and audit-implied G", loc="left")
    ax.plot([], [], "o-", color=C.TEXT, ms=3.5, lw=0.9, label="Observed G, stored text (95% CI)")
    ax.plot([], [], color=C.color(0), lw=1.8, label="Submission-stage G over the audit CI, auditable")
    ax.plot([], [], color=C.GREY, lw=1.8, label="Same, unauditable (not interpreted)")
    ax.grid(axis="y", visible=False)
    h0, l0 = axes[0].get_legend_handles_labels()
    h1, l1 = axes[1].get_legend_handles_labels()
    fig.legend(h0 + h1, l0 + l1, loc="lower center", ncol=3, fontsize=6.5, bbox_to_anchor=(0.5, 0.02))
    fig.text(0.01, 0.003, "Audit-implied intervals clip D to the feasible range [P3 - 1, P3]; a bound of 0 is a "
             "clipping artefact. Titles: primary audit (2023-26 pairs), G_dec. Abstracts: 2024-26 pairs, G_total.",
             fontsize=6, color=C.GREY)
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    C.save_fig(fig, "fig_S2_tipping_points", OUTDIR,
               data=t[["feature", "label", "kind", "auditable", "chan", "did_pp", "did_lo_pp", "did_hi_pp", "tip_pp",
                       "Gobs", "Glo", "Ghi", "Galo", "Gahi"]])


def fig_route(rv: pd.DataFrame):
    if rv.empty:
        return
    fig, axes = C.new_fig("double", 2.4, ncols=2)
    rows = []
    g = rv[rv.decision.isin(["accepted", "rejected"])].set_index("decision")
    routes = [("A_found", "Title route (A)"), ("B_found", "Surname + abstract (B)"), ("union_found", "A or B")]
    ms = [("A_changed", "A_changed"), ("B_changed", "B_changed"), ("A_latest_diff", "A_latest_diff"),
          ("B_latest_diff", "B_latest_diff")]
    top = 0.0
    for i, dec in enumerate(["accepted", "rejected"]):
        r = g.loc[dec]
        xs = np.arange(len(routes)) + (-0.1 if i == 0 else 0.1)
        v = [r[f"{c}_rate"] for c, _ in routes]
        axes[0].errorbar(xs, v, yerr=[[r[f"{c}_rate"] - r[f"{c}_lo"] for c, _ in routes],
                                      [r[f"{c}_hi"] - r[f"{c}_rate"] for c, _ in routes]],
                         color=C.color(i), marker="o", ms=5, lw=0, elinewidth=1.4, label=dec.capitalize())
        for (c, _), x_, vv in zip(routes, xs, v):
            axes[0].annotate(f"{int(r[c])}/{int(r.n)}", (x_, r[f"{c}_lo"]), xytext=(0, -9), textcoords="offset points",
                             ha="center", fontsize=5.5, color=C.color(i))
            rows.append(dict(panel="a", decision=dec, measure=c, value=vv, lo=r[f"{c}_lo"], hi=r[f"{c}_hi"],
                             k=int(r[c]), n=int(r.n)))
        xs2 = np.arange(len(ms)) + (-0.1 if i == 0 else 0.1)
        v2 = [r[f"{c}_rate"] for c, _ in ms]
        axes[1].errorbar(xs2, v2, yerr=[[r[f"{c}_rate"] - r[f"{c}_lo"] for c, _ in ms],
                                        [r[f"{c}_hi"] - r[f"{c}_rate"] for c, _ in ms]],
                         color=C.color(i), marker="o", ms=5, lw=0, elinewidth=1.4, label=dec.capitalize())
        for (c, _), x_, vv in zip(ms, xs2, v2):
            top = max(top, r[f"{c}_hi"])
            axes[1].annotate(f"{int(r[f'{c}_k'])}/{int(r[f'{c}_n'])}", (x_, r[f"{c}_lo"]), xytext=(0, -9),
                             textcoords="offset points", ha="center", fontsize=5.5, color=C.color(i))
            rows.append(dict(panel="b", decision=dec, measure=c, value=vv, lo=r[f"{c}_lo"], hi=r[f"{c}_hi"],
                             k=int(r[f"{c}_k"]), n=int(r[f"{c}_n"])))
    axes[0].set_xticks(range(len(routes)), [lab for _, lab in routes])
    axes[0].set_ylim(0, 1.02)
    axes[0].set_ylabel("Found on arXiv (k/n)")
    axes[0].set_title("a  Found rate by retrieval route", loc="left")
    axes[1].set_xticks(range(4), ["v1\nroute A", "v1\nroute B", "latest\nroute A", "latest\nroute B"])
    axes[1].set_xlabel("arXiv title compared with the stored title")
    axes[1].set_ylim(-0.04, top + 0.05)
    axes[1].set_ylabel("Share with a different title (k/n)")
    axes[1].set_title("b  Title stability by route", loc="left")
    for ax in axes:
        ax.grid(axis="x", visible=False)
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=7, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    C.save_fig(fig, "fig_S3_route_validation", OUTDIR, data=pd.DataFrame(rows))


def fig_flip_rates(fl: pd.DataFrame):
    """Drop rate given v1-present and add rate given v1-absent, by decision (primary audit)."""
    t = fl[(fl.spec == "primary") & fl.feature.isin(KEYS_T)].iloc[::-1].reset_index(drop=True)
    n = len(t)
    fig, axes = C.new_fig("double", 0.17 * n + 1.0, ncols=2, sharey=True)
    ypos = np.arange(n)
    rows = []
    for p_i, (kind, xl, xmax) in enumerate([("drop", "Drop rate: P(absent in stored | present in v1)", 1.0),
                                            ("add", "Add rate: P(present in stored | absent in v1)", None)]):
        ax = axes[p_i]
        for i, (dec, g) in enumerate([("accepted", "acc"), ("rejected", "rej")]):
            off = 0.15 if i == 0 else -0.15
            for yv, (_, r) in zip(ypos, t.iterrows()):
                v = r[f"{kind}_rate_{g}"]
                if not np.isfinite(v):
                    continue
                ax.plot([r[f"{kind}_rate_lo_{g}"], r[f"{kind}_rate_hi_{g}"]], [yv + off] * 2, color=C.color(i), lw=1.3)
                ax.plot([v], [yv + off], "o", color=C.color(i), ms=4)
                den = r[f"v1_present_{g}"] if kind == "drop" else r[f"n_{g}"] - r[f"v1_present_{g}"]
                rows.append(dict(feature=r.feature, decision=dec, kind=kind, rate=v, lo=r[f"{kind}_rate_lo_{g}"],
                                 hi=r[f"{kind}_rate_hi_{g}"], k=r[f"{kind}s_{g}"], n=den))
            ax.plot([], [], "o-", color=C.color(i), ms=4, lw=1.3, label=dec.capitalize())
        ax.set_xlabel(xl, fontsize=7)
        ax.grid(axis="y", visible=False)
        ax.tick_params(axis="y", length=0)
        if xmax:
            ax.set_xlim(0, xmax)
        else:
            ax.set_xlim(0, None)
    lab = [("‡ " if r.feature in CHANNEL else "" if r.auditable else "† ") + f"{r.label} ({r.v1_present_acc}/{r.v1_present_rej})"
           for _, r in t.iterrows()]
    axes[0].set_yticks(ypos, lab)
    axes[0].set_title("a  Drops (v1-present n: acc/rej)", loc="left", fontsize=8.5)
    axes[1].set_title("b  Adds (95% Wilson CI)", loc="left", fontsize=8.5)
    axes[1].legend(loc="lower right", fontsize=7)
    fig.text(0.01, 0.005, "† fewer than 10 v1-present titles in an arm; ‡ not carried by arXiv metadata "
             "(channel-unauditable).", fontsize=6, color=C.GREY)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    C.save_fig(fig, "fig_S4_flip_rates", OUTDIR, data=pd.DataFrame(rows))


# ------------------------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------------------------
def main(enlarge_n: int | None = None):
    t0 = time.time()
    U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
    fv = C.load_features(["submission_id", "n_words", "name_primary"])

    # ---------------- frozen inputs
    orig_raw, n_o, h_o = read_frozen(S.ORIG_PATH)
    enl_raw, n_e, h_e = read_frozen(S.ENLARGE_PATH, enlarge_n)
    v1a_raw, n_a, h_a = read_frozen(S.V1ABS_PATH)
    route_raw, n_r, h_r = read_frozen(S.ROUTE_PATH)
    orig, enl, v1a = clean(orig_raw), clean(enl_raw), clean(v1a_raw)
    n_err = int(enl_raw.error.notna().sum()) if "error" in enl_raw else 0
    freeze = dict(
        original=dict(path="cache/arxiv_audit.jsonl", n_lines=n_o, sha256=h_o, n_records=len(orig)),
        enlargement=dict(path="cache/arxiv_audit_enlarge.jsonl", n_lines_used=n_e, sha256_of_lines_used=h_e,
                         enlarge_n_arg=enlarge_n, n_records_ok=len(enl), n_error_lines=n_err,
                         target=ENLARGE_TARGET, complete=bool(len(enl) >= ENLARGE_TARGET),
                         by_cell={f"{y}_{d}": int(v) for (y, d), v in enl.groupby(["year", "decision"]).size().items()}),
        v1_abstracts=dict(path="cache/arxiv_audit_v1abs.jsonl", n_lines=n_a, sha256=h_a, n_records_ok=len(v1a)),
        route=dict(path="cache/arxiv_audit_route.jsonl", n_lines=n_r, sha256=h_r),
        note="pass --enlarge-n n_lines_used and compare sha256_of_lines_used to reproduce this audit sample "
             "(same convention as prereg_confirm._complete_jsonl)")
    log(f"audit freeze: {json.dumps(freeze)}")

    # ---------------- channel check (arXiv metadata never carries these)
    arx_titles = pd.concat([orig_raw.get("v1_title", pd.Series(dtype=object)),
                            enl_raw.get("v1_title", pd.Series(dtype=object)),
                            orig_raw.get("latest_title", pd.Series(dtype=object)),
                            enl_raw.get("latest_title", pd.Series(dtype=object))]).dropna().astype(str)
    import features as F  # noqa: E402  (src/features.py, on sys.path via snapshot_bounds)
    chan = dict(n_arxiv_titles=int(len(arx_titles)),
                n_typo=int(arx_titles.map(lambda s: bool(F.LLM_TYPO.search(s))).sum()),
                n_unicode_dash=int(arx_titles.str.contains("[‐-―]", regex=True).sum()),
                n_all_caps=int((arx_titles.map(F.casing_style) == "all_caps").sum()))
    abs_txt = pd.concat([v1a.get("v1_summary", pd.Series(dtype=object)),
                         enl.get("v1_summary", pd.Series(dtype=object))]).dropna().astype(str)
    chan.update(n_arxiv_v1_abstracts=int(len(abs_txt)), n_abs_emdash=int(abs_txt.str.contains("—").sum()))
    log(f"channel check: {chan}")

    # ---------------- pairs
    Po_all = pairs(orig, U, "original")
    Pe = pairs(enl, U, "enlarge")
    Po = Po_all[Po_all.year >= 2023].reset_index(drop=True)
    P = pd.concat([Po, Pe], ignore_index=True)                      # PRIMARY
    P22 = pd.concat([Po_all, Pe], ignore_index=True)                # incl. 2022 accepted-only pairs
    log(f"pairs: original {len(Po_all)} (2023-26: {len(Po)}), enlargement {len(Pe)}, primary {len(P)} "
        f"{P.decision.value_counts().to_dict()}; by year {P.groupby(['year', 'decision']).size().to_dict()}")

    # ---------------- findability (original; original + enlargement 2023-26)
    d_o = S.audit_frame(orig, fv)
    d_e = S.audit_frame(enl, fv)
    d_all = pd.concat([d_o, d_e], ignore_index=True)
    d_all = d_all[d_all.year.isin(AUDIT_YEARS)].reset_index(drop=True)
    fr = pd.concat([S.found_rate_table(d_o, "original"), S.found_rate_table(d_e, "enlarge"),
                    S.found_rate_table(d_all, "original+enlarge")], ignore_index=True)
    fm_o, _ = S.findability_models(d_o)
    fm_o["sample"] = "original"
    fm_a, fits_a = S.findability_models(d_all)
    fm_a["sample"] = "original+enlarge"
    res_int = C.logit("found_i ~ C(year) + acc * NAME + log_nw", d_all)
    fm_i = C.or_table(res_int).reset_index().rename(columns={"index": "term"})
    fm_i["outcome"], fm_i["formula"], fm_i["sample"] = "found_i", "found_i ~ C(year) + acc * NAME + log_nw", "original+enlarge"
    fm = pd.concat([fm_o, fm_a, fm_i], ignore_index=True)
    log("findability (original+enlarge):\n" + fm[(fm["sample"] == "original+enlarge") &
                                                 fm.term.isin(["acc", "NAME", "log_nw", "acc:NAME"])][
        ["outcome", "formula", "term", "OR", "OR_lo", "OR_hi", "p", "nobs"]].round(3).to_string())

    # title-clause admissions (arxiv_audit.find accepts title Jaccard >= 0.6 + surname substring when the latest
    # abstract Jaccard < 0.45)
    tclause = P.assign(tc=P.abstract_jaccard_latest < 0.45).groupby("decision").tc.agg(["mean", "sum", "size"])

    # ---------------- v1 timing
    tim = pd.crosstab(P.decision, P.v1_in_review)
    fisher_p = float(stats.fisher_exact(tim.to_numpy())[1]) if tim.shape == (2, 2) else np.nan
    timing = dict(share_in_review={d: float(P[P.decision == d].v1_in_review.mean()) for d in ["accepted", "rejected"]},
                  n_in_review={d: int(P[P.decision == d].v1_in_review.sum()) for d in ["accepted", "rejected"]},
                  median_lag_days={d: float(P[P.decision == d].v1_lag_days.median()) for d in ["accepted", "rejected"]},
                  fisher_p=fisher_p, deadlines=SUB_DEADLINE,
                  title_clause_share={d: float(tclause.loc[d, "mean"]) for d in tclause.index})
    Po_t = Po.copy()
    timing["original_share_in_review"] = {d: float(Po_t[Po_t.decision == d].v1_in_review.mean())
                                          for d in ["accepted", "rejected"]}
    to = pd.crosstab(Po_t.decision, Po_t.v1_in_review)
    timing["original_fisher_p"] = float(stats.fisher_exact(to.to_numpy())[1])
    log(f"v1 timing: {json.dumps(timing)}")

    # ---------------- retitling
    Wb = S.boot_matrix(P)
    rt, rt_extra = S.retitling_table(P, Wb, "primary")
    rt = rt[rt.years != "2022-23"]  # no 2022 pairs in the primary: the pre-period row equals the 2023 row
    rt_extra["did_period_post_minus_pre"]["note"] = "(acc-rej retitle rate) 2024-26 minus 2023"
    rts, rt_x = [rt], {"primary": rt_extra}
    P_in, P_pre = P[P.v1_in_review == 1].reset_index(drop=True), P[P.v1_in_review == 0].reset_index(drop=True)
    for lab, Q in [("v1_in_review", P_in), ("v1_before_deadline", P_pre), ("original_only", Po_all),
                   ("original_in_review", Po_all[Po_all.v1_in_review == 1]),
                   ("original_before_deadline", Po_all[Po_all.v1_in_review == 0])]:
        t_, e_ = S.retitling_table(Q.reset_index(drop=True), S.boot_matrix(Q.reset_index(drop=True)), lab)
        if not lab.startswith("original"):
            t_ = t_[t_.years != "2022-23"]
            e_["did_period_post_minus_pre"]["note"] = "(acc-rej retitle rate) 2024-26 minus 2023"
        rts.append(t_)
        rt_x[lab] = e_
    rt = pd.concat(rts, ignore_index=True)
    log("retitling:\n" + rt[(rt.measure == "changed_norm") & rt.years.isin(["all", "2024-26", "2023"])][
        ["spec", "years", "n_acc", "rate_acc", "n_rej", "rate_rej", "diff", "diff_lo", "diff_hi"]].round(3).to_string())

    # ---------------- flip specs
    specs = {}
    specs["primary"] = flips(P, KEYS_T, "primary")
    specs["incl_2022"] = flips(P22, KEYS_T, "incl_2022")
    specs["year_std"] = flips(P, KEYS_T, "year_std", w=std_weights(P, P.year))
    specs["post_2024_26"] = flips(P[P.year.isin(POST)], KEYS_T, "post_2024_26")
    specs["original_only"] = flips(Po_all, KEYS_T, "original_only")
    specs["new_records_only"] = flips(Pe, KEYS_T, "new_records_only")
    specs["new_records_2024_26"] = flips(Pe[Pe.year.isin(POST)], KEYS_T, "new_records_2024_26")
    fit_u = fits_a["usable_i ~ C(year) + acc + log_nw + NAME"]
    Pi, wi = S.ipw_weights(d_all, P, fit_u, pop=False, U=U)
    specs["ipw_find"] = flips(Pi, KEYS_T, "ipw_find", w=wi)
    Pp, wp = S.ipw_weights(d_all, P, fit_u, pop=True, U=U)
    specs["ipw_find_pop"] = flips(Pp, KEYS_T, "ipw_find_pop", w=wp)
    kish = {lab: {dec: float(w[(Q.decision == dec).to_numpy()].sum() ** 2 / (w[(Q.decision == dec).to_numpy()] ** 2).sum())
                  for dec in ["accepted", "rejected"]} for lab, Q, w in [("ipw_find", Pi, wi), ("ipw_find_pop", Pp, wp)]}
    wrange = {lab: [float(w.min()), float(w.max())] for lab, w in [("ipw_find", wi), ("ipw_find_pop", wp)]}
    specs["abstract_matched"] = flips(P[P.abstract_jaccard_latest >= 0.45], KEYS_T, "abstract_matched")
    specs["v1_in_review"] = flips(P_in, KEYS_T, "v1_in_review")
    specs["v1_before_deadline"] = flips(P_pre, KEYS_T, "v1_before_deadline")
    specs["timing_std"] = flips(P, KEYS_T, "timing_std",
                                w=std_weights(P, P.year.astype(str) + "_" + P.v1_in_review.astype(str)))

    # V7 route validation + union with route-B-only pairs (300-paper subsample only)
    rv, rpairs, rv_sum = S.route_validation(orig, U)
    nmb = near_miss_bound(route_raw)
    rv_sum["near_miss_bound"] = nmb
    bo = rpairs[rpairs.B_only & rpairs.B_usable].copy() if not rv.empty else pd.DataFrame()
    if len(bo):
        bo_rec = bo[["submission_id", "year", "decision", "or_title", "arxiv_id", "v1_title", "v1_date"]].copy()
        bo_rec["found"], bo_rec["abstract_jaccard"] = True, np.nan
        Pb = pairs(bo_rec, U, "route_B_only")
        Pb = Pb[Pb.year >= 2023]
        specs["union_route_v7sub"] = flips(pd.concat([P, Pb], ignore_index=True), KEYS_T, "union_route_v7sub")
        rv_sum["n_B_only_pairs_added"] = int(len(Pb))
        rv_sum["B_only_pairs_changed_rate"] = float(Pb.changed_norm.mean()) if len(Pb) else None
    log(f"route summary: {json.dumps(S.jsonable(rv_sum))}")

    # ---------------- universe prevalences, tipping
    df = S.universe_frame()
    df["L_title_words"] = df.r24_any.astype(bool) | df.r26_any.astype(bool)
    df["O_union_arxiv"] = df.case_sentence_case.astype(bool) | df.question_opener.astype(bool)
    keys_all = KEYS_T + KEYS_A
    sums = S.stage_prevalences(df, keys_all)
    Ppool, apool = S.pooled(sums, POST)
    Pt = Ppool[:, :len(KEYS_T)]
    ft_p, db_p = specs["primary"]
    tp = gate_dec(tipping(Pt, apool, KEYS_T, ft_p, db_p, "2024-26"))
    log("tipping (primary):\n" + tp[["feature", "auditable", "G_dec_obs", "did_pp", "did_lo_pp", "did_hi_pp",
                                     "tip_dec_pp", "p_ident_dec", "p_holm_dec", "passes_uncorrected_dec",
                                     "passes_holm_dec", "G_dec_sel_point", "excess_share_edit_dec"]].round(4).to_string())

    id_rows = []
    for sname, (ftab, db) in specs.items():
        t_ = gate_dec(tipping(Pt, apool, KEYS_T, ftab, db, "2024-26"))
        t_["spec"] = sname
        fi = ftab.set_index("feature")
        t_["n_acc"] = fi.loc[t_.feature, "n_acc"].to_numpy()
        t_["n_rej"] = fi.loc[t_.feature, "n_rej"].to_numpy()
        t_["v1_present_acc"] = fi.loc[t_.feature, "v1_present_acc"].to_numpy()
        t_["v1_present_rej"] = fi.loc[t_.feature, "v1_present_rej"].to_numpy()
        id_rows.append(t_)
    idt = pd.concat(id_rows, ignore_index=True)
    ident_any = []
    for _, r in idt.iterrows():
        for nm_, tag in [("dec", ""), ("total", " (G_total)")]:
            tip_, up = r[f"tip_{nm_}_pp"], r[f"G_{nm_}_obs"] >= 1
            for ci, col, lo_c, hi_c in [("pseudo-flip", f"G_{nm_}_identified", "did_lo_pp", "did_hi_pp"),
                                        ("Wald", f"G_{nm_}_identified_wald", "did_lo_wald_pp", "did_hi_wald_pp"),
                                        ("bootstrap", f"G_{nm_}_identified_boot", "did_lo_boot_pp", "did_hi_boot_pp")]:
                if bool(r[col]):
                    ident_any.append(dict(spec=r.spec, feature=r.feature, ci=ci + tag, did_pp=r.did_pp, tip_pp=tip_,
                                          ci_lo_pp=r[lo_c], ci_hi_pp=r[hi_c],
                                          margin_pp=(tip_ - r[hi_c]) if up else (r[lo_c] - tip_),
                                          p_ident=r[f"p_ident_{nm_}"],
                                          passes_holm=bool(r.passes_holm_dec) if nm_ == "dec" else False))
    ident_any = pd.DataFrame(ident_any)
    log("identified anywhere:\n" + (ident_any.round(3).to_string() if len(ident_any) else "none"))

    # freeze path (verdicts as the enlargement accrued)
    path_rows = []
    caps = [c for c in FREEZE_CAPS if c < n_e] + [n_e]
    for cap in caps:
        e_c = clean(read_frozen(S.ENLARGE_PATH, cap)[0])
        Q = pd.concat([Po, pairs(e_c, U, "enlarge")], ignore_index=True)
        fq, dq = flips(Q, KEYS_T, f"cap_{cap}")
        tq = gate_dec(tipping(Pt, apool, KEYS_T, fq, dq, "2024-26")).set_index("feature")
        nm = tq.loc["NAME"]
        path_rows.append(dict(
            enlarge_lines=cap, n_acc=int(fq.n_acc.iloc[0]), n_rej=int(fq.n_rej.iloc[0]),
            n_auditable=int(tq.auditable.sum()), auditable=",".join(tq.index[tq.auditable]),
            NAME_did_pp=nm.did_pp, NAME_lo_pp=nm.did_lo_pp, NAME_hi_pp=nm.did_hi_pp,
            NAME_G_dec_sel_point=nm.G_dec_sel_point,
            NAME_G_total_corr_lo90=nm.G_total_corr_lo90, NAME_G_total_corr_hi90=nm.G_total_corr_hi90,
            identified_uncorrected=",".join(tq.index[tq.G_dec_identified]),
            passes_uncorrected=",".join(tq.index[tq.passes_uncorrected_dec]),
            passes_holm=",".join(tq.index[tq.passes_holm_dec]),
            min_p_ident=float(np.nanmin(np.where(tq.auditable, tq.p_ident_dec, np.nan))),
            min_p_feature=str(tq[tq.auditable].p_ident_dec.idxmin()),
            sentence_case_did_pp=tq.loc["sentence_case", "did_pp"], sentence_case_lo_pp=tq.loc["sentence_case", "did_lo_pp"],
            sentence_case_tip_pp=tq.loc["sentence_case", "tip_dec_pp"],
            sentence_case_v1=f"{int(fq.set_index('feature').loc['sentence_case', 'v1_present_acc'])}/"
                             f"{int(fq.set_index('feature').loc['sentence_case', 'v1_present_rej'])}"))
    fpath = pd.DataFrame(path_rows)
    log("freeze path:\n" + fpath.drop(columns=["auditable"]).round(3).to_string())

    # per-year (primary pairs)
    by_year = []
    for y in AUDIT_YEARS:
        Py_ = P[P.year == y].reset_index(drop=True)
        fy, dby = flips(Py_, KEYS_T, f"year_{y}")
        Pyy, ayy = S.pooled(sums, (y,))
        t_y = tipping(Pyy[:, :len(KEYS_T)], ayy, KEYS_T, fy, dby, str(y))
        t_y["n_acc"], t_y["n_rej"] = int(Py_.acc.sum()), int((Py_.acc == 0).sum())
        by_year.append(t_y)
    tpy = pd.concat(by_year, ignore_index=True)

    # ---------------- abstract audit (original v1 abstracts + enlargement's cached v1 abstracts)
    o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(
        v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]], on="submission_id", how="inner")
    Pa_o = pairs(o2, U, "v1abs", v1_abstract=True)
    Pa_e = pairs(enl, U, "enlarge", v1_abstract=True)
    Pa_all = pd.concat([Pa_o[Pa_o.year >= 2023], Pa_e], ignore_index=True)
    Pa_post = Pa_all[Pa_all.year.isin(POST)].reset_index(drop=True)
    Pa_t = Ppool[:, len(KEYS_T):]
    abs_specs = {}
    for lab, Q in [("abs_2024_26", Pa_post), ("abs_2023_26", Pa_all), ("abs_original_only", Pa_o),
                   ("abs_new_records_only", Pa_e)]:
        fa, dba = flips(Q, KEYS_A, lab)
        ta = tipping(Pa_t, apool, KEYS_A, fa, dba, "2024-26")
        ta["spec"] = lab
        abs_specs[lab] = (fa, ta)
    fla, tpa = abs_specs["abs_2024_26"]
    jac = {}
    for lab, Q in [("original", Pa_o), ("abs_2023_26", Pa_all), ("abs_2024_26", Pa_post)]:
        d_, lo_, hi_ = boot_diff_mean(Q.abs_jacc.to_numpy(float), Q.acc.to_numpy() == 1)
        jac[lab] = dict(acc=float(Q[Q.acc == 1].abs_jacc.mean()), rej=float(Q[Q.acc == 0].abs_jacc.mean()),
                        diff=d_, lo=lo_, hi=hi_, n_acc=int(Q.acc.sum()), n_rej=int((Q.acc == 0).sum()))
    chk = Pa_o.merge(orig[["submission_id", "v1_title"]], on="submission_id", suffixes=("", "_orig"))
    abs_info = dict(n_pairs={k: int(len(v[0]) and v[0].n_acc.iloc[0] + v[0].n_rej.iloc[0]) for k, v in abs_specs.items()},
                    v1_title_consistent=float((chk.v1_title.map(A.norm_title) == chk.v1_title_orig.map(A.norm_title)).mean()),
                    abstract_jaccard=jac)
    log(f"abstract audit: {json.dumps(S.jsonable(abs_info))}")
    for lab, (fa, ta) in abs_specs.items():
        log(f"abstract {lab}:\n" + fa[["feature", "n_acc", "v1_present_acc", "adds_acc", "drops_acc", "n_rej",
                                        "v1_present_rej", "adds_rej", "drops_rej", "did", "did_lo", "did_hi",
                                        "auditable"]].round(4).to_string())

    # ---------------- gate table
    tpi = tp.set_index("feature")
    gate = []

    def tost_row(r, nm_, col, tag):
        return dict(claim=f"H4a NAME {nm_} within [0.90, 1.11] (2024-26 pooled; audit: {tag})", feature="NAME",
                    observed=r[f"G_{col}_obs"], obs_ci90=f"[{r[f'G_{col}_lo90']:.3f}, {r[f'G_{col}_hi90']:.3f}]",
                    audit_interval=f"[{r[f'G_{col}_audit_lo']:.3f}, {r[f'G_{col}_audit_hi']:.3f}]",
                    corrected_ci90=f"[{r[f'G_{col}_corr_lo90']:.3f}, {r[f'G_{col}_corr_hi90']:.3f}]",
                    tip_pp=r[f"tip_{col}_pp"], did_pp=r.did_pp, p_ident=np.nan, p_holm=np.nan,
                    passes_uncorrected=np.nan,
                    passes=bool(0.90 <= r[f"G_{col}_corr_lo90"] and r[f"G_{col}_corr_hi90"] <= 1.11),
                    rule="editing-corrected 90% CI (universe bootstrap x Normal(D, pseudo-flip se)) inside the TOST "
                         "margins [0.90, 1.11]")
    for col, nm_ in [("total", "G_total"), ("dec", "G_dec")]:
        gate.append(tost_row(tpi.loc["NAME"], nm_, col, "primary"))
        for sname in ["post_2024_26", "original_only", "new_records_only", "v1_in_review"]:
            r = idt[(idt.spec == sname) & (idt.feature == "NAME")].iloc[0]
            gate.append(tost_row(r, nm_, col, sname))
    nmr = tpi.loc["NAME"]
    gate.append(dict(claim="H4a NAME G_total: literal PLAN section 4 rule (tipping point beyond the audit upper CI)",
                     feature="NAME", observed=nmr.G_total_obs, obs_ci90="", audit_interval="", corrected_ci90="",
                     tip_pp=nmr.tip_total_pp, did_pp=nmr.did_pp, p_ident=np.nan, p_holm=np.nan,
                     passes_uncorrected=np.nan, passes=bool(nmr.tip_total_pp > nmr.did_hi_pp),
                     rule="informational: the section 4 'tipping point exceeds the audit upper CI' rule; not defined "
                          "for an equivalence claim"))
    for k in KEYS_T:
        r = tpi.loc[k]
        gate.append(dict(claim=f"acceptance association of {k} (G_dec != 1)", feature=k, observed=r.G_dec_obs,
                         obs_ci90=f"[{r.G_dec_lo90:.3f}, {r.G_dec_hi90:.3f}]",
                         audit_interval=f"[{r.G_dec_audit_lo:.3f}, {r.G_dec_audit_hi:.3f}]",
                         corrected_ci90=f"[{r.G_dec_corr_lo90:.3f}, {r.G_dec_corr_hi90:.3f}]",
                         tip_pp=r.tip_dec_pp, did_pp=r.did_pp, p_ident=r.p_ident_dec, p_holm=r.p_holm_dec,
                         passes_uncorrected=bool(r.passes_uncorrected_dec), passes=bool(r.passes_holm_dec),
                         rule=f"auditable (channel + >= 10 v1-present per arm), editing-corrected 95% CI excludes 1, "
                              f"Holm one-sided p < {ALPHA1} across the {int(r.holm_family_size)} auditable features"))
    # H4b family: L-title words, O-union (arXiv-measurable), abstract L words (2024-26 abstract pairs); G_total < 1
    tpa_i = tpa.set_index("feature")
    h4b = [("H4b L-title G_total < 1 (2024-26; audited as R24 or R26)", tpi.loc["L_title_words"], "L_title_words"),
           ("H4b O-union G_total < 1 (2024-26; audited without ALL-CAPS)", tpi.loc["O_union_arxiv"], "O_union_arxiv"),
           ("H4b/abstract F24 or F26 words G_total < 1 (2024-26)", tpa_i.loc["L_abs_words"], "L_abs_words")]
    p_h = np.array([r.p_ident_total if (r.auditable and r.G_total_obs < 1) else np.nan for _, r, _ in h4b])
    adj = holm(p_h)
    for (claim, r, k), pa in zip(h4b, adj):
        gate.append(dict(claim=claim, feature=k, observed=r.G_total_obs,
                         obs_ci90=f"[{r.G_total_lo90:.3f}, {r.G_total_hi90:.3f}]",
                         audit_interval=f"[{r.G_total_audit_lo:.3f}, {r.G_total_audit_hi:.3f}]",
                         corrected_ci90=f"[{r.G_total_corr_lo90:.3f}, {r.G_total_corr_hi90:.3f}]",
                         tip_pp=r.tip_total_pp, did_pp=r.did_pp, p_ident=r.p_ident_total, p_holm=pa,
                         passes_uncorrected=bool(r.G_total_identified and r.G_total_corr_hi95 < 1),
                         passes=bool(r.auditable and r.G_total_obs < 1 and r.G_total_corr_hi95 < 1 and pa < ALPHA1),
                         rule="auditable, corrected 95% CI below 1, Holm one-sided p < 0.025 across the 3 H4b claims"))
    for k in ["L_title", "O_union"]:
        r = tpi.loc[k]
        gate.append(dict(claim=f"H4b {k} G_total < 1 (2024-26; original union)", feature=k, observed=r.G_total_obs,
                         obs_ci90=f"[{r.G_total_lo90:.3f}, {r.G_total_hi90:.3f}]",
                         audit_interval=f"[{r.G_total_audit_lo:.3f}, {r.G_total_audit_hi:.3f}]",
                         corrected_ci90=f"[{r.G_total_corr_lo90:.3f}, {r.G_total_corr_hi90:.3f}]",
                         tip_pp=r.tip_total_pp, did_pp=r.did_pp, p_ident=r.p_ident_total, p_holm=np.nan,
                         passes_uncorrected=bool(r.G_total_identified and r.G_total_corr_hi95 < 1), passes=False,
                         rule=f"not auditable: {CHANNEL[k]}"))
    gate = pd.DataFrame(gate)
    log("gate:\n" + gate[["claim", "observed", "corrected_ci90", "p_ident", "p_holm", "passes_uncorrected",
                          "passes"]].round(4).to_string())

    # ---------------- write tables
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fl_all = pd.concat([s[0] for s in specs.values()], ignore_index=True)
    P.to_csv(OUTDIR / "audit_pairs.csv", index=False)
    fr.to_csv(OUTDIR / "found_rates.csv", index=False)
    fm.to_csv(OUTDIR / "findability_models.csv", index=False)
    rt.to_csv(OUTDIR / "retitling.csv", index=False)
    fl_all.to_csv(OUTDIR / "T4_2_flip_matrices.csv", index=False)
    mc = [S.multiclass_table(P, "primary"), S.multiclass_table(Po_all, "original_only")]
    pd.concat(mc, ignore_index=True).to_csv(OUTDIR / "T4_2_flip_multiclass.csv", index=False)
    tp.to_csv(OUTDIR / "T4_2_tipping_points.csv", index=False)
    tpy.to_csv(OUTDIR / "T4_2_tipping_by_year.csv", index=False)
    idt.to_csv(OUTDIR / "T4_2_identification_by_spec.csv", index=False)
    ident_any.to_csv(OUTDIR / "T4_2_identified_anywhere.csv", index=False)
    fpath.to_csv(OUTDIR / "T4_2_freeze_path.csv", index=False)
    gate.to_csv(OUTDIR / "gate.csv", index=False)
    pd.concat([pd.concat([fa, ta.drop(columns=["feature"]).add_prefix("tp_")], axis=1)
               for fa, ta in abs_specs.values()], ignore_index=True).to_csv(OUTDIR / "abstract_audit.csv", index=False)
    if not rv.empty:
        rv.to_csv(OUTDIR / "route_validation.csv", index=False)
        keep = ["submission_id", "year", "decision", "route", "surname_b", "A_found", "B_found", "B_found_strict",
                "tier", "abstract_jaccard", "same_id", "A_usable", "B_usable", "A_changed", "B_changed",
                "A_latest_diff", "B_latest_diff", "orig_arxiv_id", "arxiv_id", "hit_query"]
        rpairs[[c for c in keep if c in rpairs]].to_csv(OUTDIR / "route_pairs.csv", index=False)
    for ext in ("png", "pdf", "csv"):  # renamed: S4 now shows drop and add rates (fig_S4_flip_rates)
        (OUTDIR / f"fig_S4_drop_rates.{ext}").unlink(missing_ok=True)

    # ---------------- figures
    fig_findability(fr, rt)
    fig_tipping(tp, tpa)
    fig_route(rv)
    fig_flip_rates(fl_all)

    # ---------------- results.json
    core = dict(
        meta=dict(script="analyses/snapshot_final.py (building blocks: analyses/snapshot_bounds.py, unchanged)",
                  n_boot=N_BOOT, seed=SEED, min_v1_present=MIN_V1, alpha_one_sided=ALPHA1,
                  decision_dates=S.DEC, submission_deadlines=SUB_DEADLINE, audit_freeze=freeze, channel_check=chan,
                  n_pairs=dict(primary=int(len(P)), primary_by_decision=P.decision.value_counts().to_dict(),
                               original_all_years=int(len(Po_all)), original_2023_26=int(len(Po)),
                               enlargement=int(len(Pe)), incl_2022=int(len(P22))),
                  primary_definition="usable pre-decision pairs, original + enlargement audit, 2023-26",
                  ipw=dict(kish_neff=kish, weight_range=wrange), abstract_audit=abs_info, timing=timing,
                  runtime_s=None),
        findability=dict(rates=fr.to_dict(orient="records"),
                         models=fm[fm.term.isin(["acc", "log_nw", "NAME", "acc:NAME"])].to_dict(orient="records")),
        retitling=dict(table=rt.to_dict(orient="records"), extra=rt_x),
        flips={s: v[0].to_dict(orient="records") for s, v in specs.items()},
        tipping_2024_26={k: {c: v for c, v in tpi.loc[k].items() if not isinstance(v, str) or c in ("label", "family")}
                         for k in KEYS_T},
        tipping_by_year=tpy.to_dict(orient="records"),
        identification_by_spec=idt[["spec", "feature", "auditable", "did_pp", "did_lo_pp", "did_hi_pp",
                                    "did_lo_wald_pp", "did_hi_wald_pp", "did_lo_boot_pp", "did_hi_boot_pp",
                                    "tip_dec_pp", "tip_dec_margin_pp", "G_dec_identified", "G_dec_identified_wald",
                                    "G_dec_identified_boot", "G_total_identified", "p_ident_dec", "p_holm_dec",
                                    "passes_uncorrected_dec", "passes_holm_dec", "n_acc", "n_rej"]]
        .to_dict(orient="records"),
        identified_anywhere=ident_any.to_dict(orient="records"),
        freeze_path=fpath.to_dict(orient="records"),
        abstract_audit={lab: dict(flips=fa.to_dict(orient="records"), tipping=ta.to_dict(orient="records"))
                        for lab, (fa, ta) in abs_specs.items()},
        route_validation=dict(table=rv.to_dict(orient="records") if not rv.empty else [], summary=rv_sum),
        gate=gate.to_dict(orient="records"),
    )
    core = compose(core, tp=tp, specs=specs, fm=fm, fr=fr, rt=rt, rt_x=rt_x, idt=idt, ident_any=ident_any, rv=rv,
                   rv_sum=rv_sum, gate=gate, abs_specs=abs_specs, fpath=fpath, timing=timing, tpy=tpy)
    core["meta"]["runtime_s"] = round(time.time() - t0, 1)
    (OUTDIR / "results.json").write_text(json.dumps(S.jsonable(core), indent=1))
    log(f"done in {time.time() - t0:.0f}s")
    (OUTDIR / "snapshot_final.log").write_text("\n".join(_LOG) + "\n")
    return core


# ------------------------------------------------------------------------------------------------
# hypotheses (every note generated from the tables)
# ------------------------------------------------------------------------------------------------
def _ci(x, lo, hi, d=2):
    return f"{pp(x, d)} pp [{pp(lo, d)}, {pp(hi, d)}]"


def _group_ident(ident_any: pd.DataFrame) -> str:
    if ident_any.empty:
        return ""
    q = ident_any[~ident_any.ci.str.contains("G_total")]
    out = []
    for k, g in q.groupby("feature", sort=False):
        pf = sorted(set(g[g.ci == "pseudo-flip"].spec))
        oth = sorted(set(g.spec) - set(pf))
        out.append(f"{k}: pseudo-flip CI in {len(pf)} specs ({', '.join(pf) or '-'})" +
                   (f"; Wald/bootstrap only in {', '.join(oth)}" if oth else ""))
    return "; ".join(out)


def compose(core, tp, specs, fm, fr, rt, rt_x, idt, ident_any, rv, rv_sum, gate, abs_specs, fpath, timing, tpy):
    T = tp.set_index("feature")
    Fl = specs["primary"][0].set_index("feature")
    hyps, rob = [], []

    def ident_list(feature=None, total=False):
        if ident_any.empty:
            return []
        q = ident_any if feature is None else ident_any[ident_any.feature == feature]
        q = q[q.ci.str.contains("G_total")] if total else q[~q.ci.str.contains("G_total")]
        return [f"{r.spec}/{r.feature}/{r.ci}" for _, r in q.iterrows()]

    # SB1
    nm, nf = T.loc["NAME"], Fl.loc["NAME"]
    il = ident_list("NAME")
    hyps.append(dict(
        id="SB1", statement="PLAN D4 decision-stage bound: the NAME acceptance association (G_dec, 2024-26) is not "
        "identified by the audit (tipping point inside the audit 95% CI of the net-flip DiD).",
        verdict="supported" if not nm.G_dec_identified else "not_supported",
        estimate=(f"net-flip DiD {_ci(nf.did, nf.did_lo, nf.did_hi)} (pseudo-flip; plain Wald "
                  f"[{pp(nf.did_lo_wald)}, {pp(nf.did_hi_wald)}], bootstrap [{pp(nf.did_lo_boot)}, {pp(nf.did_hi_boot)}]); "
                  f"D*_dec {f2(nm.tip_dec_pp)} pp; one-sided p(DiD < D*) {f2(nm.p_ident_dec, 3)}; observed G_dec "
                  f"{f2(nm.G_dec_obs, 3)} [{f2(nm.G_dec_lo95, 3)}, {f2(nm.G_dec_hi95, 3)}]; G_dec at the audit point "
                  f"estimate {f2(nm.G_dec_sel_point, 3)}; share of the G_dec excess attributable to editing at the "
                  f"point estimate {f2(100 * nm.excess_share_edit_dec, 0)}% (audit CI {f2(100 * nm.excess_share_edit_lo_dec, 0)}"
                  f"% to {f2(100 * nm.excess_share_edit_hi_dec, 0)}%); audit-implied G_dec [{f2(nm.G_dec_audit_lo, 3)}, "
                  f"{f2(nm.G_dec_audit_hi, 3)}]; n = {int(nf.n_acc)}/{int(nf.n_rej)} pairs (v1-present "
                  f"{int(nf.v1_present_acc)}/{int(nf.v1_present_rej)})"),
        notes=("NAME G_dec identified in no spec under any CI type" if not il else
               "NAME G_dec identified in: " + "; ".join(il)) +
              f" ({idt.spec.nunique()} specs x 3 CI types, T4_2_identification_by_spec.csv)."))
    # SB2
    aud = T[T.auditable]
    n_holm, n_unc = int(T.passes_holm_dec.sum()), int(T.passes_uncorrected_dec.sum())
    top = aud.sort_values("p_ident_dec").head(3)
    hyps.append(dict(
        id="SB2", statement="Gate (PLAN section 4, Holm per section 0): at least one title feature's acceptance "
        "association (G_dec != 1, 2024-26) survives the audit: auditable (arXiv-measurable, >= 10 v1-present titles "
        "per arm), editing-corrected 95% CI excludes 1, Holm-adjusted one-sided identification p < 0.025.",
        verdict="supported" if n_holm > 0 else "not_supported",
        estimate=(f"{n_holm} of {len(T)} title features pass ({len(aud)} auditable); passing: "
                  f"{sorted(T.index[T.passes_holm_dec]) or 'none'}. Smallest identification p: " +
                  "; ".join(f"{k} p = {f2(r.p_ident_dec, 4)} (Holm {f2(r.p_holm_dec, 3)}), DiD {pp(r.did_pp / 100)} vs "
                            f"D* {pp(r.tip_dec_pp / 100)} pp" for k, r in top.iterrows()) +
                  f". Uncorrected interim rule: {n_unc} pass {sorted(T.index[T.passes_uncorrected_dec]) or ''}"),
        notes=("Uncorrected identification of G_dec (tipping point beyond one 95% CI type), by feature: " +
               (_group_ident(ident_any) or "none") + f" (of {idt.spec.nunique()} specs; T4_2_identified_anywhere.csv). "
               "Freeze path (T4_2_freeze_path.csv): " +
               "; ".join(f"{int(r.enlarge_lines)} lines: uncorrected [{r.passes_uncorrected}], Holm [{r.passes_holm}]"
                         for _, r in fpath.iterrows()))))
    # SB3
    rare = ["using", "R24", "R26", "slot_llm", "title_typo"]
    n_aud = sum(bool(Fl.loc[k].auditable) for k in rare)
    hyps.append(dict(
        id="SB3", statement="V7: rare lexical title features ('using', R24, R26, LLM slot words, title typography) "
        "are unauditable (fewer than 10 v1-present titles in an arm, or not carried by arXiv metadata).",
        verdict="supported" if n_aud == 0 else ("partially_supported" if n_aud < len(rare) else "not_supported"),
        estimate="; ".join(f"{k}: v1-present {int(Fl.loc[k].v1_present_acc)}/{int(Fl.loc[k].v1_present_rej)}"
                           f"{' (channel)' if k in CHANNEL else ''}, auditable={bool(Fl.loc[k].auditable)}" for k in rare),
        notes="Auditability is a function of audit size: auditable features by enlargement lines used: " +
              "; ".join(f"{int(r.enlarge_lines)}: {int(r.n_auditable)}" for _, r in fpath.iterrows()) +
              ". Original 331-pair audit: 'using' 4/5 v1-present (the PLAN example reproduces)."))
    # SB4
    sel = lambda frm, term, smp="original+enlarge": fm[(fm.term == term) & (fm.formula == frm) & (fm["sample"] == smp)].iloc[0]  # noqa: E731
    f_full = "found_i ~ C(year) + acc + log_nw + NAME"
    u_full = "usable_i ~ C(year) + acc + log_nw + NAME"
    fa, fn, fl_ = sel(f_full, "acc"), sel(f_full, "NAME"), sel(f_full, "log_nw")
    ua, un = sel(u_full, "acc"), sel(u_full, "NAME")
    fpre = fm[(fm.term == "acc") & (fm.outcome == "usable_given_found") & (fm["sample"] == "original+enlarge")].iloc[0]
    fint = fm[(fm.term == "acc:NAME") & (fm["sample"] == "original+enlarge")].iloc[0]
    fra = fr[(fr.source == "original+enlarge") & (fr.year.astype(str) == "all")].set_index("decision")
    ipw = idt[(idt.spec == "ipw_find_pop") & (idt.feature == "NAME")].iloc[0]
    hyps.append(dict(
        id="SB4", statement="Differential findability: accepted papers are found on arXiv more often than rejected "
        "papers; reweighting usable pairs by 1/P(usable | year, decision, title length, NAME) leaves the NAME bound "
        "unchanged (not identified).",
        verdict="supported" if (fa.OR_lo > 1 and not bool(ipw.G_dec_identified)) else "partially_supported",
        estimate=(f"original + enlargement 2023-26: found {f2(100 * fra.loc['accepted', 'found_rate'], 1)}% vs "
                  f"{f2(100 * fra.loc['rejected', 'found_rate'], 1)}% (n {int(fra.loc['accepted', 'n'])}/"
                  f"{int(fra.loc['rejected', 'n'])}); odds ratio(accepted) {f2(fa.OR)} [{f2(fa.OR_lo)}, {f2(fa.OR_hi)}]; "
                  f"usable pair OR(accepted) {f2(ua.OR)} [{f2(ua.OR_lo)}, {f2(ua.OR_hi)}]; IPW x population NAME DiD "
                  f"{f2(ipw.did_pp)} pp [{f2(ipw.did_lo_pp)}, {f2(ipw.did_hi_pp)}], identified={bool(ipw.G_dec_identified)}"),
        notes=(f"Generated: found OR(NAME) {f2(fn.OR)} [{f2(fn.OR_lo)}, {f2(fn.OR_hi)}], p = {f2(fn.p, 3)}; found "
               f"OR(log title words) {f2(fl_.OR)} [{f2(fl_.OR_lo)}, {f2(fl_.OR_hi)}]; usable-pair OR(NAME) {f2(un.OR)} "
               f"[{f2(un.OR_lo)}, {f2(un.OR_hi)}], p = {f2(un.p, 3)}; acc x NAME interaction for found "
               f"{f2(fint.OR)} [{f2(fint.OR_lo)}, {f2(fint.OR_hi)}]; pre-decision v1 given found OR(accepted) "
               f"{f2(fpre.OR)} [{f2(fpre.OR_lo)}, {f2(fpre.OR_hi)}].")))
    # SB5
    g = lambda spec, yrs: rt[(rt.spec == spec) & (rt.years == yrs) & (rt.measure == "changed_norm")].iloc[0]  # noqa: E731
    r_all, r_post, r_in, r_pre = g("primary", "all"), g("primary", "2024-26"), g("v1_in_review", "all"), g("v1_before_deadline", "all")
    dp = rt_x["primary"]["did_period_post_minus_pre"]
    hyps.append(dict(
        id="SB5", statement="Camera-ready retitling: accepted papers' stored titles differ from the pre-decision "
        "arXiv v1 more often than rejected papers' (descriptive; no pre-registered threshold).",
        verdict="supported" if r_all.diff_lo > 0 else "not_supported",
        estimate=(f"retitled {f2(100 * r_all.rate_acc, 1)}% acc (n={int(r_all.n_acc)}) vs {f2(100 * r_all.rate_rej, 1)}% "
                  f"rej (n={int(r_all.n_rej)}): {_ci(r_all['diff'], r_all.diff_lo, r_all.diff_hi, 1)}; 2024-26 "
                  f"{_ci(r_post['diff'], r_post.diff_lo, r_post.diff_hi, 1)}; v1 posted during review "
                  f"{f2(100 * r_in.rate_acc, 1)}% vs {f2(100 * r_in.rate_rej, 1)}%: {_ci(r_in['diff'], r_in.diff_lo, r_in.diff_hi, 1)}; "
                  f"v1 posted before the deadline {f2(100 * r_pre.rate_acc, 1)}% vs {f2(100 * r_pre.rate_rej, 1)}%: "
                  f"{_ci(r_pre['diff'], r_pre.diff_lo, r_pre.diff_hi, 1)}; logit OR(acc | year FE) "
                  f"{f2(rt_x['primary']['logit_acc_OR']['OR'])} [{f2(rt_x['primary']['logit_acc_OR']['lo'])}, "
                  f"{f2(rt_x['primary']['logit_acc_OR']['hi'])}]; period contrast (2024-26 minus 2023) "
                  f"{_ci(dp['est'], dp['lo'], dp['hi'], 1)}"),
        notes=(f"Rejected papers retitle too; the in-review stratum (v1 close to the submitted version) is the cleanest "
               f"camera-ready comparison. Share of pairs with v1 in review: acc {f2(100 * timing['share_in_review']['accepted'], 1)}%, "
               f"rej {f2(100 * timing['share_in_review']['rejected'], 1)}% (Fisher p = {f2(timing['fisher_p'], 3)}).")))
    # V7a / V7b
    if not rv.empty:
        gg = rv.set_index("decision")
        nmb = rv_sum.get("near_miss_bound", {}).get("jac_ge_0.10", {})
        hyps.append(dict(
            id="V7a", statement="Route validation (findability): the accepted-rejected findability gap is not specific to "
            "title search: a title-free route (first-author surname + distinctive abstract words) gives the same gap. "
            "Both routes accept a hit by similarity between the stored and the latest arXiv abstract, so they are not "
            "independent of post-rejection rewriting.",
            verdict="supported" if (rv_sum["gap_B"]["lo"] > 0 and rv_sum["gap_B_minus_A"]["lo"] < 0 <
                                    rv_sum["gap_B_minus_A"]["hi"]) else "partially_supported",
            estimate=(f"n = {rv_sum['n']} (acc {rv_sum['n_acc']}, rej {rv_sum['n_rej']}); found A/B: acc "
                      f"{f2(gg.loc['accepted', 'A_found_rate'], 3)}/{f2(gg.loc['accepted', 'B_found_rate'], 3)}, rej "
                      f"{f2(gg.loc['rejected', 'A_found_rate'], 3)}/{f2(gg.loc['rejected', 'B_found_rate'], 3)}; gap A "
                      f"{f2(rv_sum['gap_A']['est'], 3)}, gap B {f2(rv_sum['gap_B']['est'], 3)}, B - A "
                      f"{f2(rv_sum['gap_B_minus_A']['est'], 3)} [{f2(rv_sum['gap_B_minus_A']['lo'], 3)}, "
                      f"{f2(rv_sum['gap_B_minus_A']['hi'], 3)}]; arXiv-id agreement {f2(gg.loc['all', 'same_id_rate'], 3)}"),
            notes=(f"Near-miss bound (same-surname, date-plausible candidate with abstract Jaccard >= 0.10 below the "
                   f"acceptance tiers, among papers neither route found): accepted {nmb.get('accepted', {}).get('near_miss')}, "
                   f"rejected {nmb.get('rejected', {}).get('near_miss')}; counting them as found, the union gap moves from "
                   f"{f2(nmb.get('gap_union', np.nan), 3)} to {f2(nmb.get('gap_bound', np.nan), 3)}. Title-clause-only "
                   f"admissions among primary pairs: acc {f2(100 * timing['title_clause_share']['accepted'], 1)}%, rej "
                   f"{f2(100 * timing['title_clause_share']['rejected'], 1)}%.")))
        bo_n = int(gg.loc["all", "Bonly_changed_n"])
        am = idt[(idt.spec == "abstract_matched") & (idt.feature == "NAME")].iloc[0]
        un_ = idt[(idt.spec == "union_route_v7sub") & (idt.feature == "NAME")]
        hyps.append(dict(
            id="V7b", statement="Route validation (title stability): the title route does not select on title "
            "stability; retitling among route-B pairs matches route-A pairs, and adding papers only route B finds "
            "leaves the flip DiDs unchanged.",
            verdict=S._v7b_verdict(gg, bo_n),
            estimate=(f"retitled v1 vs stored: route A {f2(gg.loc['all', 'A_changed_rate'], 3)} "
                      f"(n={int(gg.loc['all', 'A_changed_n'])}), route B {f2(gg.loc['all', 'B_changed_rate'], 3)} "
                      f"(n={int(gg.loc['all', 'B_changed_n'])}), difference "
                      f"{f2(100 * (gg.loc['all', 'B_changed_rate'] - gg.loc['all', 'A_changed_rate']), 1)} pp; B-only usable "
                      f"pairs {bo_n} ({int(gg.loc['all', 'Bonly_changed_k'])} retitled); NAME DiD with B-only pairs (300-paper "
                      f"subsample) {f2(un_.did_pp.iloc[0]) if len(un_) else 'nan'} pp; abstract-matched pairs only "
                      f"{f2(am.did_pp)} pp [{f2(am.did_lo_pp)}, {f2(am.did_hi_pp)}]"),
            notes="Verdict rule (set after the pilot design, descriptive): supported if route-level retitling rates "
                  "differ by < 5 pp and route-B-only pairs are not retitled > 20 pp more often; partially supported if "
                  "only the first holds; not testable with fewer than 5 B-only pairs."))
    # G1
    gt = gate.set_index("claim")
    k1 = "H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: primary)"
    k2 = "H4a NAME G_dec within [0.90, 1.11] (2024-26 pooled; audit: primary)"
    others = [c for c in gt.index if c.startswith("H4a NAME G_total") and "primary" not in c and "literal" not in c]
    lit = gt.loc["H4a NAME G_total: literal PLAN section 4 rule (tipping point beyond the audit upper CI)"]
    hyps.append(dict(
        id="G1", statement="Gate for D4-H4a: NAME neutrality (pooled 2024-26 G_total inside [0.90, 1.11]) survives "
        "camera-ready uncertainty (editing-corrected 90% CI combining universe bootstrap and audit).",
        verdict="supported" if bool(gt.loc[k1, "passes"]) else "not_supported",
        estimate=(f"G_total observed {f2(gt.loc[k1, 'observed'], 3)} 90% CI {gt.loc[k1, 'obs_ci90']}; audit-implied "
                  f"{gt.loc[k1, 'audit_interval']}; corrected 90% CI {gt.loc[k1, 'corrected_ci90']}; G at the audit point "
                  f"estimate {f2(T.loc['NAME'].G_total_sel_point, 3)}. G_dec corrected 90% CI {gt.loc[k2, 'corrected_ci90']}"),
        notes="Other audit specs: " + "; ".join(
            f"{c.split('audit: ')[1].rstrip(')')}: {gt.loc[c, 'corrected_ci90']} passes={bool(gt.loc[c, 'passes'])}"
            for c in others) + f". Literal section 4 rule (D*_total {f2(lit.tip_pp)} pp vs audit upper CI "
            f"{f2(T.loc['NAME'].did_hi_pp)} pp): {'met' if bool(lit.passes) else 'not met'}."))
    # G2 / G2b / G3 (H4b family)
    for hid, claim, key, extra in [
            ("G2", "H4b L-title G_total < 1 (2024-26; audited as R24 or R26)", "L_title_words",
             "the original L-title union contains title typography, which arXiv cannot carry"),
            ("G2b", "H4b O-union G_total < 1 (2024-26; audited without ALL-CAPS)", "O_union_arxiv",
             "ALL-CAPS titles cannot be audited (arXiv titles are never ALL-CAPS)"),
            ("G3", "H4b/abstract F24 or F26 words G_total < 1 (2024-26)", "L_abs_words",
             "em dash and Unicode typography are unauditable through arXiv")]:
        r = gt.loc[claim]
        src = T if key in T.index else abs_specs["abs_2024_26"][1].set_index("feature")
        fsrc = Fl if key in Fl.index else abs_specs["abs_2024_26"][0].set_index("feature")
        hyps.append(dict(
            id=hid, statement=f"Gate for D4-H4b: {claim} survives the camera-ready audit.",
            verdict="supported" if bool(r.passes) else "not_supported",
            estimate=(f"G_total {f2(r.observed, 3)}, 90% CI {r.obs_ci90}; net-flip DiD {f2(r.did_pp)} pp "
                      f"[{f2(src.loc[key].did_lo_pp)}, {f2(src.loc[key].did_hi_pp)}] vs D*_total {f2(r.tip_pp)} pp; "
                      f"audit-implied {r.audit_interval}; corrected 90% CI {r.corrected_ci90}; one-sided p "
                      f"{f2(r.p_ident, 3)}, Holm {f2(r.p_holm, 3)}; auditable={bool(fsrc.loc[key].auditable)} "
                      f"(v1-present {int(fsrc.loc[key].v1_present_acc)}/{int(fsrc.loc[key].v1_present_rej)})"),
            notes=f"Holm across the three H4b claims (G2, G2b, G3); {extra}. G_desk x G_exit uses submission-stage "
                  "text and needs no audit (D4)."))
    # G4
    for lab, primary in [("abs_2024_26", True), ("abs_2023_26", False)]:
        f24 = abs_specs[lab][0].set_index("feature").loc["F24"]
        v4 = ("supported" if f24.did_lo > 0 else "falsified" if f24.did_hi < 0 else
              "partially_supported" if f24.did >= 0 else "not_supported")
        hyps.append(dict(
            id="G4" if primary else "G4_sens", statement="D4-H4c direction assumption: camera-ready polishing does not "
            "lower accepted papers' abstract RARE21/F24 rates relative to rejected papers (net-flip DiD >= 0)" +
            (" [2024-26 pairs, primary]" if primary else " [2023-26 pairs, sensitivity]"),
            verdict=v4,
            estimate=(f"F24 net flips: accepted {pp(f24.net_acc)} pp ({int(f24.adds_acc)} adds / {int(f24.drops_acc)} "
                      f"drops, v1-present {int(f24.v1_present_acc)}, n {int(f24.n_acc)}), rejected {pp(f24.net_rej)} pp "
                      f"({int(f24.adds_rej)} / {int(f24.drops_rej)}, v1-present {int(f24.v1_present_rej)}, n {int(f24.n_rej)}); "
                      f"DiD {_ci(f24.did, f24.did_lo, f24.did_hi)}"),
            notes="supported = CI above 0; partially = point >= 0 and CI includes 0; not_supported = point < 0 and CI "
                  "includes 0; falsified = CI below 0."))
    # robustness
    for sname in idt.spec.unique():
        t = idt[(idt.spec == sname) & (idt.feature == "NAME")].iloc[0]
        rob.append(dict(check=f"NAME bound under audit spec '{sname}'",
                        result=f"DiD {f2(t.did_pp)} pp [{f2(t.did_lo_pp)}, {f2(t.did_hi_pp)}], D* {f2(t.tip_dec_pp)} pp, "
                               f"identified={bool(t.G_dec_identified)}, p={f2(t.p_ident_dec, 3)}, n={int(t.n_acc)}/{int(t.n_rej)}"))
    rob.append(dict(check="Auditable title features (primary)", result=sorted(Fl.index[Fl.auditable])))
    rob.append(dict(check="Count rule met but channel-unauditable", result=sorted(Fl.index[Fl.auditable_count & ~Fl.channel_ok])))
    yr = tpy.set_index(["period", "feature"])
    hw = [(float(r.did_hi_pp) - float(r.did_lo_pp)) / 2 for _, r in tpy[tpy.feature == "NAME"].iterrows()]
    rob.append(dict(check="Per-year audits (primary pairs)",
                    result=f"pairs per arm {int(tpy.n_acc.min())}-{int(tpy.n_acc.max())} acc / {int(tpy.n_rej.min())}-"
                           f"{int(tpy.n_rej.max())} rej; NAME CI half-widths {min(hw):.1f}-{max(hw):.1f} pp; G_dec "
                           f"identified (any feature, pseudo-flip): {sorted(set(tpy.feature[tpy.G_dec_identified]))}"))
    del yr
    core["hypotheses"] = hyps
    core["robustness"] = rob
    return core


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="WP4 final snapshot bounds (frozen complete audit)")
    ap.add_argument("--enlarge-n", type=int, default=None,
                    help="use only the first N complete lines of cache/arxiv_audit_enlarge.jsonl (default: all)")
    main(ap.parse_args().enlarge_n)
