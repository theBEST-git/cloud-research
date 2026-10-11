"""WP8 / D4-H4d: exit composition (withdrawn vs rejected) in the cross-section and within last-position keys,
plus the exploratory exit-timing (2025-26) and desk-rejection-timing (2026) checks.

H4d (PLAN D4; C3-H1). Population (primary): NA pool minus desk rejections, i.e. REJ u WD, 2024-26; outcome
wd = administrative_status == withdrawn (the 349 post-decision 2026 withdrawals count as withdrawn, as in the
pool definition and the pilot). Linear probability models:
    cross-section : wd ~ f + log_authors + llm_topic | year
    within        : wd ~ f + log_authors + llm_topic | year + last-position key
The last-position key is the declared profile key at the paper's last list position (max position of the full
declared list; papers whose last position is not a profile key drop out), as in D2. "Last list position" is a
partition label only; a declared profile key is not a verified person.
Both models are fitted on the same sample (papers whose key has >= 2 papers in the population, i.e. the sample
that identifies the within estimate); the full-sample cross-section is also reported. SEs are clustered by key.
The difference (cross - within) uses the joint key-clustered covariance from Frisch-Waugh-Lovell influence
functions (Hausman-type contrast); a 500-replicate key-cluster bootstrap checks the NAME contrast.
Prediction: cross > 0, within <= 0, and the difference > 0.
Robustness: wd_post counted as rejected; desk rejections kept in the population (pilot population); 2018-23;
the pilot's 'last profile key in the list' definition; topic100 FE added to both models.

Exploratory (not confirmatory):
  * exit timing 2025-26: withdrawal date = metadata modification_ms, validated against the review calendar
    (daily withdrawal spikes at review release and decision days). Phases: early (< review release), discussion
    (review release to 3 Dec), late (3 Dec to decision), post-decision (>= decision). Prevalence of NAME, O-union,
    L-union and F24 by phase vs rejected papers, Wilson 95% CIs.
  * early vs late 2026 desk rejections: tested only if modification_ms dates desk rejections (checked first).

Outputs (outputs/d4_filter/): exit_composition.csv, exit_timing.csv, exit_calendar.csv, exit_composition.json,
fig_F4_4_exit_arrows.{pdf,png,csv}, d4_exit_composition.log

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d4_exit_composition
"""
from __future__ import annotations

import time

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d4_stage_gains as S
from common import read_table

OUTDIR = S.OUTDIR
POST = S.POST
SEED = S.SEED + 2
ARROW_FEATURES = ["NAME", "compound", "phrase_colon", "mixed_case_name", "title_case", "all_caps_title",
                  "sentence_case", "question_opener", "O_union", "title_typo", "R24", "R26", "F24", "F26", "emdash",
                  "L_union"]
# ICLR calendar landmarks (review release validated against the daily withdrawal spike in main();
# decision dates as in arxiv_audit.DECISION_DATE)
CAL = {2025: dict(review="2024-11-12", disc_end="2024-12-03", decision="2025-01-22"),
       2026: dict(review="2025-11-12", disc_end="2025-12-03", decision="2026-01-26")}


def last_keys(sub_ids: set) -> pd.DataFrame:
    a = read_table("submission_authors")[["submission_id", "source_list_position", "native_id_kind",
                                          "declared_id_key"]]
    a = a[a.submission_id.isin(sub_ids)]
    pmax = a.groupby("submission_id").source_list_position.transform("max")
    last = a[a.source_list_position.eq(pmax) & a.native_id_kind.eq("profile") & a.declared_id_key.notna()]
    last = last.drop_duplicates("submission_id")[["submission_id", "declared_id_key"]].rename(
        columns={"declared_id_key": "key_last"})
    prof = a[a.native_id_kind.eq("profile") & a.declared_id_key.notna()].sort_values("source_list_position")
    lastprof = prof.groupby("submission_id").tail(1)[["submission_id", "declared_id_key"]].rename(
        columns={"declared_id_key": "key_lastprof"})
    return last.merge(lastprof, on="submission_id", how="outer")


def fwl(d: pd.DataFrame, y: str, x: str, controls: list[str], fe: list[str]) -> dict:
    """Coefficient on x after absorbing FE and partialling out controls; per-row influence function."""
    Z = C.demean(d[[y, x] + controls].to_numpy(float), [d[f].to_numpy() for f in fe])
    yt, xt, W = Z[:, 0], Z[:, 1], Z[:, 2:]
    if W.shape[1]:
        coef_y = np.linalg.lstsq(W, yt, rcond=None)[0]
        coef_x = np.linalg.lstsq(W, xt, rcond=None)[0]
        yt = yt - W @ coef_y
        xt = xt - W @ coef_x
    sxx = float(xt @ xt)
    b = float(xt @ yt) / sxx
    e = yt - b * xt
    return dict(b=b, IF=xt * e / sxx)


def cluster_cov(ifs: list[np.ndarray], cl: np.ndarray) -> np.ndarray:
    codes = pd.factorize(pd.Series(cl))[0]
    G = codes.max() + 1
    U = np.column_stack([np.bincount(codes, weights=f, minlength=G) for f in ifs])
    return U.T @ U * G / (G - 1)


def contrast(d: pd.DataFrame, col: str, key: str, controls: list[str], extra_fe: list[str] | None = None) -> dict:
    """Cross-section vs within-key LPM of wd on col, same sample; returns estimates in pp."""
    extra_fe = extra_fe or []
    d = d[d[key].notna()].copy()
    d["n_key"] = d.groupby(key)[key].transform("size")
    full = d.copy()
    d = d[d.n_key >= 2].copy()
    d["f_"] = d[col].astype(float)
    full["f_"] = full[col].astype(float)
    rc = C.feols(d, "wd", ["f_"] + controls, fe=["year"] + extra_fe, cluster=key)
    rw = C.feols(d, "wd", ["f_"] + controls, fe=["year", key] + extra_fe, cluster=key)
    rf = C.feols(full, "wd", ["f_"] + controls, fe=["year"] + extra_fe, cluster="topic100")
    fc = fwl(d, "wd", "f_", controls, ["year"] + extra_fe)
    fw = fwl(d, "wd", "f_", controls, ["year", key] + extra_fe)
    V = cluster_cov([fc["IF"], fw["IF"]], d[key].to_numpy())
    diff = fc["b"] - fw["b"]
    se_d = float(np.sqrt(V[0, 0] + V[1, 1] - 2 * V[0, 1]))
    keys_var = d.groupby(key).f_.std().fillna(0)
    out = dict(
        feature=col, nobs=int(rc.nobs), n_keys=int(d[key].nunique()), n_keys_with_variation=int((keys_var > 0).sum()),
        share_f=float(d.f_.mean()), wd_rate=float(d.wd.mean()),
        cross_pp=100 * float(rc.params["f_"]), cross_se_pp=100 * float(rc.se["f_"]),
        within_pp=100 * float(rw.params["f_"]), within_se_pp=100 * float(rw.se["f_"]),
        within_p_one_sided_gt0=float(stats.t.sf(float(rw.params["f_"]) / float(rw.se["f_"]), rw.df_resid)),
        full_cross_pp=100 * float(rf.params["f_"]), full_cross_se_pp=100 * float(rf.se["f_"]), full_nobs=int(rf.nobs),
        diff_pp=100 * diff, diff_se_pp=100 * se_d, diff_z=diff / se_d if se_d > 0 else np.nan,
        diff_p_one_sided=float(stats.norm.sf(diff / se_d)) if se_d > 0 else np.nan,
        b_cross_fwl_check=100 * fc["b"], b_within_fwl_check=100 * fw["b"],
    )
    out["cross_lo95_pp"] = out["cross_pp"] - 1.96 * out["cross_se_pp"]
    out["cross_hi95_pp"] = out["cross_pp"] + 1.96 * out["cross_se_pp"]
    out["within_lo95_pp"] = out["within_pp"] - 1.96 * out["within_se_pp"]
    out["within_hi95_pp"] = out["within_pp"] + 1.96 * out["within_se_pp"]
    out["cross_p_one_sided_gt0"] = float(stats.norm.sf(out["cross_pp"] / out["cross_se_pp"]))
    return out


def key_bootstrap(d: pd.DataFrame, col: str, key: str, controls: list[str], n_boot: int = 500) -> dict:
    d = d[d[key].notna()].copy()
    d["n_key"] = d.groupby(key)[key].transform("size")
    d = d[d.n_key >= 2].reset_index(drop=True)
    d["f_"] = d[col].astype(float)
    rng = np.random.default_rng(SEED)
    diffs, cs, ws = [], [], []
    for _ in range(n_boot):
        idx = C.boot_indices(len(d), clusters=d[key].to_numpy(), rng=rng)
        b = d.iloc[idx].copy()
        # a drawn cluster's rows are contiguous in idx; give each draw its own FE id (adjacent repeat draws of the
        # same key merge into one group, which leaves the within estimate unchanged)
        cl = d[key].to_numpy()[idx]
        starts = np.r_[True, cl[1:] != cl[:-1]]
        b["kb"] = np.cumsum(starts)
        c = fwl(b, "wd", "f_", controls, ["year"])["b"]
        w = fwl(b, "wd", "f_", controls, ["year", "kb"])["b"]
        cs.append(c)
        ws.append(w)
        diffs.append(c - w)
    diffs, cs, ws = map(np.array, (diffs, cs, ws))
    return dict(n_boot=n_boot, diff_pp_lo95=100 * float(np.quantile(diffs, .025)),
                diff_pp_hi95=100 * float(np.quantile(diffs, .975)), diff_p_le0=float(np.mean(diffs <= 0)),
                within_pp_lo95=100 * float(np.quantile(ws, .025)), within_pp_hi95=100 * float(np.quantile(ws, .975)),
                cross_pp_lo95=100 * float(np.quantile(cs, .025)), cross_pp_hi95=100 * float(np.quantile(cs, .975)),
                within_p_gt0=float(np.mean(ws > 0)))


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return np.nan, np.nan
    z = 1.96
    p = k / n
    den = 1 + z ** 2 / n
    c = (p + z ** 2 / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / den
    return c - h, c + h


def fig_arrows(tab: pd.DataFrame):
    import matplotlib.pyplot as plt
    t = tab.set_index("key").reindex(ARROW_FEATURES).reset_index()
    n = len(t)
    fig, ax = C.new_fig("double", height=0.24 * n + 1.0)
    y = np.arange(n)[::-1].astype(float)
    rows = []
    for yv, r in zip(y, t.itertuples()):
        ax.plot([r.cross_lo95_pp, r.cross_hi95_pp], [yv + 0.13, yv + 0.13], color=C.COLORS[0], lw=1.3)
        ax.plot([r.within_lo95_pp, r.within_hi95_pp], [yv - 0.13, yv - 0.13], color=C.COLORS[1], lw=1.3)
        ax.annotate("", xy=(r.within_pp, yv - 0.13), xytext=(r.cross_pp, yv + 0.13),
                    arrowprops=dict(arrowstyle="-|>", color=C.GREY, lw=1.0, shrinkA=3, shrinkB=3, mutation_scale=8))
        ax.plot([r.cross_pp], [yv + 0.13], "o", color=C.COLORS[0], ms=5)
        ax.plot([r.within_pp], [yv - 0.13], "s", color=C.COLORS[1], ms=5)
        rows.append(dict(feature=r.key, label=r.label, cross_pp=r.cross_pp, cross_lo95=r.cross_lo95_pp,
                         cross_hi95=r.cross_hi95_pp, within_pp=r.within_pp, within_lo95=r.within_lo95_pp,
                         within_hi95=r.within_hi95_pp, diff_pp=r.diff_pp, diff_se_pp=r.diff_se_pp, y=yv))
    ax.axvline(0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_yticks(y, t.label)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    lo = min(t.cross_lo95_pp.min(), t.within_lo95_pp.min())
    hi = max(t.cross_hi95_pp.max(), t.within_hi95_pp.max())
    ax.set_xlim(max(lo - 1, -25), min(hi + 1, 25))
    ax.set_xlabel("Withdrawal vs rejection, LPM coefficient (pp), 2024-26, 95% CI")
    ax.plot([], [], "o-", color=C.COLORS[0], ms=5, lw=1.3, label="Cross-section (year FE)")
    ax.plot([], [], "s-", color=C.COLORS[1], ms=5, lw=1.3, label="Within last-position key (year + key FE)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    for i in range(1, n):
        if S.FEAT_SET[t.key[i]] != S.FEAT_SET[t.key[i - 1]]:
            ax.axhline(y[i] + 0.5, color=C.GRID, lw=0.8)
    return fig, pd.DataFrame(rows)


def main():
    t0 = time.time()
    fh = open(OUTDIR / "d4_exit_composition.log", "w")
    log = lambda m: S.log(m, fh)  # noqa: E731
    df = S.load_frame(min_year=2018, density=True)
    lk = last_keys(set(df.submission_id))
    df = df.merge(lk, on="submission_id", how="left", validate="1:1")
    df["wd"] = df.WD.astype(int)
    ctr = ["log_authors", "llm_topic"]
    log(f"frame {len(df)}; last-position profile key present {df.key_last.notna().mean():.3f}")

    specs = {
        "primary": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1)], years=POST, key="key_last"),
        "wd_post_as_rejected": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1)].assign(wd=lambda x: x.wd * (1 - x.wd_post)),
                                    years=POST, key="key_last"),
        "with_desk_rejections": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1) | (d.DR == 1)], years=POST,
                                     key="key_last"),
        "years_2018_23": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1)], years=S.PRE, key="key_last"),
        "pilot_last_profile_key": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1)], years=POST, key="key_lastprof"),
        "topic100_FE": dict(pop=lambda d: d[(d.REJ == 1) | (d.WD == 1)], years=POST, key="key_last",
                            extra_fe=["topic100"]),
    }
    rows = []
    for spec, cfg in specs.items():
        d = cfg["pop"](df)
        d = d[d.year.isin(cfg["years"])].copy()
        feats = ARROW_FEATURES if spec == "primary" else ["NAME", "O_union", "L_union"]
        for k in feats:
            r = contrast(d, S.FEAT_COL[k], cfg["key"], ctr, cfg.get("extra_fe"))
            r.update(spec=spec, key=k, label=S.FEAT_LABEL[k], set=S.FEAT_SET[k])
            rows.append(r)
        log(f"{spec}: done ({time.time() - t0:.0f}s)")
    tab = pd.DataFrame(rows)
    tab.to_csv(OUTDIR / "exit_composition.csv", index=False)
    log(tab[["spec", "key", "nobs", "n_keys", "cross_pp", "cross_se_pp", "within_pp", "within_se_pp", "diff_pp",
             "diff_se_pp", "full_cross_pp", "full_cross_se_pp"]].round(3).to_string())

    # NAME key-cluster bootstrap check (primary)
    d = specs["primary"]["pop"](df)
    d = d[d.year.isin(POST)].copy()
    kb = key_bootstrap(d, "name_primary", "key_last", ctr, n_boot=500)
    log(f"NAME key bootstrap: {kb} ({time.time() - t0:.0f}s)")

    prim = tab[(tab.spec == "primary") & (tab.key == "NAME")].iloc[0].to_dict()
    h4d = dict(
        primary=prim, key_bootstrap=kb,
        cross_gt0=bool(prim["cross_lo95_pp"] > 0), within_le0_point=bool(prim["within_pp"] <= 0),
        within_ci_excludes_positive_1pp=bool(prim["within_hi95_pp"] < 1.0),
        differ=bool(prim["diff_p_one_sided"] < 0.05),
        falsified=bool(prim["within_pp"] >= prim["cross_pp"]),
        robustness=tab[(tab.key == "NAME") & (tab.spec != "primary")].to_dict(orient="records"),
        other_features=tab[(tab.spec == "primary") & (tab.key != "NAME")].to_dict(orient="records"),
    )

    fig, data = fig_arrows(tab[tab.spec == "primary"])
    C.save_fig(fig, "fig_F4_4_exit_arrows", OUTDIR, data=data)

    # ---------------- exploratory: timing
    m = read_table("metadata_provenance")[["submission_id", "modification_ms"]]
    t = df[df.year.isin([2025, 2026])].merge(m, on="submission_id", how="left")
    t["mod"] = pd.to_datetime(t.modification_ms, unit="ms", errors="coerce")
    cal_rows = []
    for y in [2025, 2026]:
        w = t[(t.year == y) & (t.WD == 1)]
        daily = w["mod"].dt.normalize().value_counts().sort_index()
        nov = daily[(daily.index.month == 11)]
        spike = nov.idxmax()
        dec = pd.Timestamp(CAL[y]["decision"])
        post_dec = daily[daily.index >= dec - pd.Timedelta(days=3)]
        cal_rows.append(dict(year=y, review_release_calendar=CAL[y]["review"], max_nov_withdrawal_day=str(spike.date()),
                             max_nov_count=int(nov.max()), median_daily_withdrawals=float(daily.median()),
                             decision_calendar=CAL[y]["decision"],
                             max_withdrawal_day_near_decision=str(post_dec.head(10).idxmax().date()),
                             count_near_decision=int(post_dec.head(10).max())))
        dr = t[(t.year == y) & (t.DR == 1)]
        cal_rows[-1].update(dr_n=int(len(dr)), dr_mod_min=str(dr["mod"].min()), dr_mod_median=str(dr["mod"].median()),
                            dr_share_after_decision=float((dr["mod"] >= dec).mean()))
    cal = pd.DataFrame(cal_rows)
    cal.to_csv(OUTDIR / "exit_calendar.csv", index=False)
    log("calendar validation:\n" + cal.T.to_string())

    def phase(r):
        c = CAL[r.year]
        if r["mod"] < pd.Timestamp(c["review"]):
            return "1 early (before reviews)"
        if r["mod"] < pd.Timestamp(c["disc_end"]):
            return "2 discussion"
        if r["mod"] < pd.Timestamp(c["decision"]):
            return "3 late (before decision)"
        return "4 post-decision"
    w = t[t.WD == 1].copy()
    w["phase"] = w.apply(phase, axis=1)
    w["week1"] = (w["mod"] >= w.year.map(lambda y: pd.Timestamp(CAL[y]["review"]))) & \
        (w["mod"] < w.year.map(lambda y: pd.Timestamp(CAL[y]["review"]) + pd.Timedelta(days=7)))
    rej = t[(t.REJ == 1)].copy()
    rej["phase"] = "0 rejected (reference)"
    acc = t[t.ACC == 1].copy()
    acc["phase"] = "5 accepted (reference)"
    wk = w[w.week1].copy()
    wk["phase"] = "2a first week after reviews"
    allp = pd.concat([w, wk, rej, acc])
    trows = []
    for (y, ph), g in allp.groupby(["year", "phase"]):
        r = dict(year=int(y), phase=ph, n=int(len(g)))
        for k in ["NAME", "O_union", "L_union", "F24", "title_typo", "all_caps_title"]:
            c = S.FEAT_COL[k]
            kk = int(g[c].sum())
            lo, hi = wilson(kk, len(g))
            r[f"{k}"] = kk / len(g)
            r[f"{k}_lo95"], r[f"{k}_hi95"] = lo, hi
        trows.append(r)
    timing = pd.DataFrame(trows)
    timing.to_csv(OUTDIR / "exit_timing.csv", index=False)
    log("exit timing:\n" + timing[["year", "phase", "n", "NAME", "O_union", "L_union", "F24"]].round(3).to_string())
    # 2026 desk-rejection timing test feasibility
    dr26 = cal[cal.year == 2026].iloc[0]
    desk_timing = dict(testable=bool(dr26.dr_share_after_decision < 0.5),
                       reason=(f"{dr26.dr_share_after_decision:.1%} of 2026 desk rejections carry a modification "
                               f"timestamp on/after the decision date (median {dr26.dr_mod_median}); the timestamp "
                               f"records a bulk post-decision update, not the desk-rejection date"))
    log(f"2026 desk-rejection timing: {desk_timing}")

    S.write_json(dict(H4d=h4d, calendar=cal.to_dict(orient="records"), exit_timing=timing.to_dict(orient="records"),
                      desk_timing_2026=desk_timing, runtime_s=round(time.time() - t0, 1)),
                 OUTDIR / "exit_composition.json")
    log(f"done in {time.time() - t0:.0f}s")
    fh.close()


if __name__ == "__main__":
    main()
