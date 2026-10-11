"""WP5 / D1-H1d, H1e: people/composition (DFL reweighting, Shapley content x people) and the tool bound.

H1d  DFL: reweight year-y papers (y = 2024, 2025, 2026) to the 2023 joint distribution of team-size bins
     (1-2, 3, 4, 5, 6-7, 8+) x share-new-author bins (0, (0,.5], (.5,1]) x llm_topic; composition share of the
     2023->y rise = (obs_y - cf_y) / (obs_y - obs_2023), cf_y = sum_c P_2023(c) P_y(NAME|c).
     Shapley over (content -> people) and (people -> content): fixed-window logit models (train 2021-23,
     intercept recalibrated on cross-fitted 2023 scores) with content = R1, people = cell one-hot, both = R1+cells.
H1e  Tool: F = F24(>=2 RARE21 words, the D1 variant) | F26 | title typography.
     (i) NAME rise among F = 0 papers vs all; (ii) delta = LPM NAME ~ F + log_authors | topic100 x year, 2024-26,
     SE clustered by topic100; (iii) maximum tool share = delta x A_max / dNAME(2023->2026), A_max in 0.24-1.0.

Outputs (outputs/d1_break/): decompose.json, dfl_table.csv, shapley_table.csv, T1_3_tool_bound.csv,
tool_delta_models.csv, fig_F1_3_decomposition.{pdf,png,csv} (written by d1_summary once all parts exist).

Run:  cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.d1_decompose [fit|all]
"""
from __future__ import annotations

import json
import sys
import time
import warnings

import numpy as np
import pandas as pd
from scipy import sparse

from analyses import _core as C
from analyses import d1_content_cf as CF

OUTDIR = C.OUT / "d1_break"
SIZE_BINS = [(0, 2, "1-2"), (3, 3, "3"), (4, 4, "4"), (5, 5, "5"), (6, 7, "6-7"), (8, 10**6, "8+")]
A_MAX = (0.24, 0.39, 0.5, 0.75, 1.0)
A_POINT = 0.39


def size_bin(n: pd.Series) -> pd.Series:
    out = pd.Series(index=n.index, dtype=object)
    for lo, hi, lab in SIZE_BINS:
        out[(n >= lo) & (n <= hi)] = lab
    return out


def new_bin(s: pd.Series) -> pd.Series:
    # PLAN bins 0, (0, .5], (.5, 1) -- the last bin is read as (.5, 1] so all-new teams are kept (logged deviation)
    return pd.Series(np.select([s.eq(0), s.gt(0) & s.le(0.5), s.gt(0.5)], ["0", "(0,.5]", "(.5,1]"], "NA"),
                     index=s.index)


def exp_bin(s: pd.Series) -> pd.Series:
    return pd.cut(s.fillna(0), [-1, 0, 2, 9, 10**6], labels=["0", "1-2", "3-9", "10+"]).astype(str)


def load() -> pd.DataFrame:
    df = CF.load_frame()
    extra = C.load_analysis_frame(
        feature_cols=["f24_2", "f24", "f26", "title_typo", "F_any"],
        universe_cols=["submission_id", "area_h", "max_prior_subs", "llast_prior_accs"])
    df = df.merge(extra, on="submission_id", how="left", validate="1:1")
    for c in ["f24_2", "f24", "f26", "title_typo", "F_any"]:
        df[c] = df[c].astype(int)
    df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
    df["sizeb"] = size_bin(df.declared_name_count)
    df["newb"] = new_bin(df.share_new_authors)
    df["expb"] = exp_bin(df.max_prior_subs)
    df["cell"] = df.sizeb + "|" + df.newb + "|" + df.llm_topic.astype(str)
    return df


# ------------------------------------------------------------------------------------------------
# H1d: DFL reweighting with a stratified paper bootstrap
# ------------------------------------------------------------------------------------------------
def dfl(df: pd.DataFrame, cellcols, y="name_primary", ref=2023, targets=(2024, 2025, 2026), n_boot=2000, seed=0):
    d = df[df.year.isin((ref,) + tuple(targets))].copy()
    d = d[~d[cellcols].astype(str).isin(["NA", "nan"]).any(axis=1)]
    key = d[cellcols].astype(str).agg("|".join, axis=1)
    codes, uniq = pd.factorize(key)
    K = len(uniq)
    yrs = d.year.to_numpy()
    Y = d[y].to_numpy().astype(float)
    out = {}
    # point estimate + bootstrap via per-year weight matrices
    rng = np.random.default_rng(seed)
    idx = {yy: np.where(yrs == yy)[0] for yy in (ref,) + tuple(targets)}

    def stats_from(wref, wt, ir, it):
        # wref: (b x n_ref), wt: (b x n_t)
        Oref = np.zeros((wref.shape[0], K)); np.add.at(Oref.T, codes[ir], wref.T)
        Ot = np.zeros((wt.shape[0], K)); np.add.at(Ot.T, codes[it], wt.T)
        Nt = np.zeros((wt.shape[0], K)); np.add.at(Nt.T, codes[it], (wt * Y[it]).T)
        Nref = np.zeros((wref.shape[0], K)); np.add.at(Nref.T, codes[ir], (wref * Y[ir]).T)
        pref = Oref / Oref.sum(1, keepdims=True)
        pt = Ot / Ot.sum(1, keepdims=True)
        overall_t = Nt.sum(1) / Ot.sum(1)
        rate_t = np.where(Ot > 0, Nt / np.maximum(Ot, 1e-12), overall_t[:, None])  # empty cell -> year mean
        rate_ref = np.where(Oref > 0, Nref / np.maximum(Oref, 1e-12), (Nref.sum(1) / Oref.sum(1))[:, None])
        obs_t, obs_ref = overall_t, Nref.sum(1) / Oref.sum(1)
        cf = (pref * rate_t).sum(1)                       # DFL: y rates at 2023 composition
        expl_ref_rates = ((pt - pref) * rate_ref).sum(1)  # Oaxaca explained part with 2023 rates
        dlt = obs_t - obs_ref
        return obs_ref, obs_t, cf, (obs_t - cf) / dlt, expl_ref_rates / dlt, (Ot[:, :] == 0).sum(1)

    for t in targets:
        ir, it = idx[ref], idx[t]
        o_r, o_t, cf, sh, sh2, nempty = stats_from(np.ones((1, len(ir))), np.ones((1, len(it))), ir, it)
        bs, bs2 = [], []
        for start in range(0, n_boot, 500):
            b = min(500, n_boot - start)
            wr = rng.multinomial(len(ir), np.full(len(ir), 1 / len(ir)), size=b).astype(float)
            wt = rng.multinomial(len(it), np.full(len(it), 1 / len(it)), size=b).astype(float)
            r = stats_from(wr, wt, ir, it)
            bs.append(r[3]); bs2.append(r[4])
        bs, bs2 = np.concatenate(bs), np.concatenate(bs2)
        out[t] = {"obs_ref": float(o_r[0]), "obs": float(o_t[0]), "cf": float(cf[0]), "share": float(sh[0]),
                  "share_ci": CF.ci(bs), "p_share_ge_0_5": float(np.mean(bs >= 0.5)),
                  "p_share_ge_0_3": float(np.mean(bs >= 0.3)),
                  "share_oaxaca_ref_rates": float(sh2[0]), "share_oaxaca_ref_rates_ci": CF.ci(bs2),
                  "n_cells": int(K), "n_empty_target_cells": int(nempty[0]), "n_ref": int(len(ir)), "n_t": int(len(it))}
    return out


# ------------------------------------------------------------------------------------------------
# Shapley content x people (fixed window, recalibrated)
# ------------------------------------------------------------------------------------------------
class RepsP(CF.Reps):
    def __init__(self, df):
        super().__init__(df, need=("R1",))
        self.cellcode = pd.factorize(df.cell)[0]

    def grid(self, rep):
        return CF.GRID_ONEHOT if rep == "P" else CF.GRID_SPARSE

    def _oh(self, idx):
        K = int(self.cellcode.max()) + 1
        return sparse.csr_matrix((np.ones(len(idx), dtype=np.float32), (np.arange(len(idx)), self.cellcode[idx])),
                                 shape=(len(idx), K))

    def build(self, rep, tr, te):
        if rep == "P":
            return self._oh(tr), self._oh(te), {"n_features": int(self.cellcode.max()) + 1}
        if rep == "R1P":
            Xtr, Xte, info = super().build("R1", tr, te)
            return (sparse.hstack([Xtr, self._oh(tr)]).tocsr(), sparse.hstack([Xte, self._oh(te)]).tocsr(),
                    {"n_features": info["n_features"] + int(self.cellcode.max()) + 1})
        return super().build(rep, tr, te)


def stage_fit():
    t0 = time.time()
    df = load()
    R = RepsP(df)
    CF.REP_INFO.setdefault("P", ("people cells", "people"))
    CF.REP_INFO.setdefault("R1P", ("R1 + people cells", "content+people"))
    for rep in ["P", "R1P"]:
        CF.run_fit(R, rep, "fixed")
        print(f"{rep} fixed done {time.time() - t0:.0f}s", flush=True)


def shapley(n_boot=2000, seed=11) -> dict:
    sets = {}
    for rep in ["R1", "P", "R1P"]:
        S, _ = CF.load_scores(rep, "U", "primary", "fixed")
        if S is None:
            return {"status": "pending"}
        P = CF.point_summary(S).set_index("year")
        Bt, _ = CF.boot_runs(S, n_boot=n_boot, seed=seed)
        sets[rep] = (P, Bt["fixed"])
    # joint bootstrap: same seed and same row sets -> identical weights; verify via obs
    for yv in CF.POST_Y:
        assert np.allclose(sets["R1"][1][yv]["obs"], sets["P"][1][yv]["obs"])
        assert np.allclose(sets["R1"][1][yv]["obs"], sets["R1P"][1][yv]["obs"])
    out = {}
    for yv in CF.POST_Y:
        P0 = sets["R1"][0]
        o0 = float(P0.loc[yv, "obs_calib"])
        dlt = float(P0.loc[yv, "obs"]) - o0
        v = {k: float(sets[k][0].loc[yv, "p_hat"]) - o0 for k in sets}
        vb = {k: sets[k][1][yv]["phat"] - sets[k][1][yv]["obs_calib"] for k in sets}
        db = sets["R1"][1][yv]["obs"] - sets["R1"][1][yv]["obs_calib"]
        phiC = 0.5 * (v["R1"] + v["R1P"] - v["P"])
        phiP = 0.5 * (v["P"] + v["R1P"] - v["R1"])
        phiCb = 0.5 * (vb["R1"] + vb["R1P"] - vb["P"])
        phiPb = 0.5 * (vb["P"] + vb["R1P"] - vb["R1"])
        out[yv] = {
            "delta": dlt, "v_content": v["R1"], "v_people": v["P"], "v_both": v["R1P"],
            "content_first": {"content": v["R1"] / dlt, "people": (v["R1P"] - v["R1"]) / dlt},
            "people_first": {"people": v["P"] / dlt, "content": (v["R1P"] - v["P"]) / dlt},
            "shapley_content_share": phiC / dlt, "shapley_content_share_ci": CF.ci(phiCb / db),
            "shapley_people_share": phiP / dlt, "shapley_people_share_ci": CF.ci(phiPb / db),
            "joint_share": v["R1P"] / dlt, "joint_share_ci": CF.ci(vb["R1P"] / db),
            "residual_share": 1 - v["R1P"] / dlt, "residual_share_ci": CF.ci(1 - vb["R1P"] / db),
            "auc_people": float(sets["P"][0].loc[yv, "auc"]), "auc_both": float(sets["R1P"][0].loc[yv, "auc"]),
        }
    return out


# ------------------------------------------------------------------------------------------------
# H1e: tool bound
# ------------------------------------------------------------------------------------------------
def f0_rise(df, F="F_d1", y="name_primary", ref=2023, targets=(2024, 2025, 2026), n_boot=2000, seed=3):
    d = df[df.year.isin((ref,) + tuple(targets))]
    out = {}
    rng = np.random.default_rng(seed)
    for t in targets:
        a, b = d[d.year == ref], d[d.year == t]
        def stat(wa, wb):
            ya, yb = a[y].to_numpy(float), b[y].to_numpy(float)
            fa, fb = (a[F].to_numpy() == 0), (b[F].to_numpy() == 0)
            all_ = (wb @ yb) / wb.sum(-1) - (wa @ ya) / wa.sum(-1)
            f0 = (wb[..., fb] @ yb[fb]) / wb[..., fb].sum(-1) - (wa[..., fa] @ ya[fa]) / wa[..., fa].sum(-1)
            f1 = (wb[..., ~fb] @ yb[~fb]) / wb[..., ~fb].sum(-1) - (wa[..., ~fa] @ ya[~fa]) / wa[..., ~fa].sum(-1)
            return all_, f0, f1
        all_, f0, f1 = stat(np.ones(len(a)), np.ones(len(b)))
        bs = []
        for start in range(0, n_boot, 500):
            k = min(500, n_boot - start)
            wa = rng.multinomial(len(a), np.full(len(a), 1 / len(a)), size=k).astype(float)
            wb = rng.multinomial(len(b), np.full(len(b), 1 / len(b)), size=k).astype(float)
            r = stat(wa, wb)
            bs.append(r[1] / r[0])
        bs = np.concatenate(bs)
        out[t] = {"rise_all": float(all_), "rise_F0": float(f0), "rise_F1": float(f1), "ratio_F0_all": float(f0 / all_),
                  "ratio_ci": CF.ci(bs), "p_ratio_le_0_70": float(np.mean(bs <= 0.70)),
                  "p_ratio_lt_0_85": float(np.mean(bs < 0.85)),
                  "share_F_ref": float(a[F].mean()), "share_F_t": float(b[F].mean()),
                  "name_F0_ref": float(a.loc[a[F] == 0, y].mean()), "name_F0_t": float(b.loc[b[F] == 0, y].mean()),
                  "name_F1_ref": float(a.loc[a[F] == 1, y].mean()), "name_F1_t": float(b.loc[b[F] == 1, y].mean())}
    return out


def delta_models(df) -> pd.DataFrame:
    post = df[df.year.isin(CF.POST_Y)].copy()
    post["ty"] = C.fe_interact(post.topic100, post.year)
    post["ay"] = C.fe_interact(post.area_h.fillna("NA"), post.year)
    post["ty_bge"] = C.fe_interact(post.topic100_bge, post.year)
    rows = []
    specs = [
        ("primary: F_d1, topic100 x year FE", "F_d1", post, ["ty"], ["log_authors"]),
        ("F_d1 + llm_topic control", "F_d1", post, ["ty"], ["log_authors", "llm_topic"]),
        ("F_d1, topic100 x year + area x year FE", "F_d1", post, ["ty", "ay"], ["log_authors"]),
        ("F_d1, bge topic100 x year FE", "F_d1", post, ["ty_bge"], ["log_authors"]),
        ("F_any (F24 >= 1 word), topic100 x year FE", "F_any", post, ["ty"], ["log_authors"]),
        ("F24 (>=2) only", "f24_2", post, ["ty"], ["log_authors"]),
        ("F26 only", "f26", post, ["ty"], ["log_authors"]),
        ("title typography only", "title_typo", post, ["ty"], ["log_authors"]),
        ("F_d1, NA pool", "F_d1", post[post.NA == 1], ["ty"], ["log_authors"]),
        ("F_d1, non-LLM subset", "F_d1", post[post.non_llm == 1], ["ty"], ["log_authors"]),
        ("F_d1, excluding 2026 (2024-25)", "F_d1", post[post.year <= 2025], ["ty"], ["log_authors"]),
    ]
    for yv in CF.POST_Y:
        specs.append((f"F_d1, {yv} only", "F_d1", post[post.year == yv], ["ty"], ["log_authors"]))
    for lab, F, d, fe, ctr in specs:
        clv = "topic100_bge" if "bge" in lab else "topic100"
        r = C.feols(d, "name_primary", [F] + ctr, fe=fe, cluster=clv)
        ci = r.conf_int()
        rows.append(dict(spec=lab, F=F, nobs=r.nobs, n_clusters=r.n_clusters, share_F=float(d[F].mean()),
                         delta=float(r.params[F]), se=float(r.se[F]), lo=float(ci.loc[F, "lo"]),
                         hi=float(ci.loc[F, "hi"]), p=float(r.pvalue[F])))
    # logit adjOR comparable with the pilot (topic100 FE + year FE)
    for F in ["F_d1", "F_any"]:
        res = C.logit(f"name_primary ~ {F} + log_authors + C(year) + C(topic100)", post, cluster="topic100")
        t = C.or_table(res, [F]).iloc[0]
        rows.append(dict(spec=f"logit adjOR {F}, topic100 FE + year FE", F=F, nobs=int(res.nobs), n_clusters=100,
                         share_F=float(post[F].mean()), delta=np.nan, se=np.nan, lo=np.nan, hi=np.nan, p=float(t.p),
                         OR=float(t.OR), OR_lo=float(t.OR_lo), OR_hi=float(t.OR_hi)))
    return pd.DataFrame(rows)


def tool_table(D: pd.DataFrame, dname: float) -> pd.DataFrame:
    rows = []
    for _, r in D[D.delta.notna()].iterrows():
        if not (r.spec.startswith("primary") or r.spec.startswith("F_any") or "area" in r.spec
                or "llm_topic control" in r.spec):
            continue
        for A in A_MAX:
            rows.append(dict(spec=r.spec, A_max=A, delta=r.delta, delta_lo=r.lo, delta_hi=r.hi, dNAME=dname,
                             tool_share=r.delta * A / dname, tool_share_lo=r.lo * A / dname,
                             tool_share_hi=r.hi * A / dname))
    return pd.DataFrame(rows)


def stage_all(n_boot=2000):
    t0 = time.time()
    df = load()
    res = {}
    # ---------------- H1d DFL ----------------
    variants = {
        "size": ["sizeb"],
        "size_x_llm": ["sizeb", "llm_topic"],
        "size_x_new": ["sizeb", "newb"],
        "full (size x new x llm_topic)": ["sizeb", "newb", "llm_topic"],
        "full + experience bins": ["sizeb", "newb", "llm_topic", "expb"],
    }
    dfl_rows = []
    res["dfl"] = {}
    for pop, d in [("U", df), ("NA", df[df.NA == 1]), ("non_llm", df[df.non_llm == 1])]:
        for name, cols in variants.items():
            if pop == "non_llm" and "llm_topic" in cols:
                cols = [c for c in cols if c != "llm_topic"]
            r = dfl(d, cols, n_boot=n_boot)
            res["dfl"][f"{pop}|{name}"] = r
            for t, v in r.items():
                dfl_rows.append(dict(pop=pop, variant=name, target_year=t, **{k: v[k] for k in
                                ["obs_ref", "obs", "cf", "share", "share_oaxaca_ref_rates", "n_cells",
                                 "n_empty_target_cells", "p_share_ge_0_5"]},
                                share_lo=v["share_ci"][0], share_hi=v["share_ci"][1]))
        print(f"DFL {pop} {time.time() - t0:.0f}s", flush=True)
    DFL = pd.DataFrame(dfl_rows)
    DFL.to_csv(OUTDIR / "dfl_table.csv", index=False)
    print(DFL[DFL.target_year == 2026].round(3).to_string(), flush=True)

    # composition descriptives
    comp = df[df.year.isin([2023, 2024, 2025, 2026])].groupby("year").agg(
        mean_authors=("declared_name_count", "mean"), share_new=("share_new_authors", "mean"),
        llm_topic=("llm_topic", "mean"), name=("name_primary", "mean"))
    res["composition_descriptives"] = comp.round(4).reset_index().to_dict(orient="records")

    # ---------------- Shapley ----------------
    res["shapley"] = shapley(n_boot=n_boot)
    if res["shapley"].get("status") != "pending":
        sh = []
        for yv, v in res["shapley"].items():
            sh.append(dict(target_year=yv, delta=v["delta"], content_first_content=v["content_first"]["content"],
                           content_first_people=v["content_first"]["people"],
                           people_first_people=v["people_first"]["people"],
                           people_first_content=v["people_first"]["content"],
                           shapley_content=v["shapley_content_share"], shapley_content_lo=v["shapley_content_share_ci"][0],
                           shapley_content_hi=v["shapley_content_share_ci"][1],
                           shapley_people=v["shapley_people_share"], shapley_people_lo=v["shapley_people_share_ci"][0],
                           shapley_people_hi=v["shapley_people_share_ci"][1],
                           residual=v["residual_share"], residual_lo=v["residual_share_ci"][0],
                           residual_hi=v["residual_share_ci"][1]))
        pd.DataFrame(sh).to_csv(OUTDIR / "shapley_table.csv", index=False)
        print(pd.DataFrame(sh).round(3).to_string(), flush=True)

    # ---------------- H1e tool ----------------
    res["f0_rise"] = {"F_d1": f0_rise(df, "F_d1", n_boot=n_boot), "F_any": f0_rise(df, "F_any", n_boot=n_boot),
                      "F_d1|NA": f0_rise(df[df.NA == 1], "F_d1", n_boot=n_boot)}
    D = delta_models(df)
    D.to_csv(OUTDIR / "tool_delta_models.csv", index=False)
    print(D.round(4).to_string(), flush=True)
    dname = float(df.loc[df.year == 2026, "name_primary"].mean() - df.loc[df.year == 2023, "name_primary"].mean())
    T13 = tool_table(D, dname)
    T13.to_csv(OUTDIR / "T1_3_tool_bound.csv", index=False)
    prim = D.iloc[0]
    res["tool"] = {
        "F_definition": "F_d1 = f24_2 (>= 2 distinct RARE21 words in abstract) | f26 | title_typo",
        "delta_primary": {"delta": prim.delta, "se": prim.se, "lo": prim.lo, "hi": prim.hi, "p": prim.p,
                          "nobs": int(prim.nobs), "share_F_2024_26": prim.share_F},
        "dNAME_2023_2026": dname,
        "tool_share_at_A": {str(A): {"share": prim.delta * A / dname, "lo": prim.lo * A / dname,
                                     "hi": prim.hi * A / dname} for A in A_MAX},
        "detectable_only_contribution": {
            "share_F_2023": float(df.loc[df.year == 2023, "F_d1"].mean()),
            "share_F_2026": float(df.loc[df.year == 2026, "F_d1"].mean()),
            "delta_x_dshareF_over_dNAME": float(prim.delta * (df.loc[df.year == 2026, "F_d1"].mean()
                                                             - df.loc[df.year == 2023, "F_d1"].mean()) / dname)},
        "A_point": A_POINT,
        "A_note": "A_max = 0.39 is the PLAN's held-out greedy abstract bound for 2026 (taken as given; not "
                  "re-estimated in D1); sensitivity range 0.24-1.0",
    }
    print(json.dumps(res["f0_rise"]["F_d1"], indent=1), flush=True)
    print(json.dumps(res["tool"], indent=1, default=float), flush=True)
    (OUTDIR / "decompose.json").write_text(json.dumps(res, indent=1, default=lambda x: float(x) if np.isscalar(x) else str(x)))
    print(f"done {time.time() - t0:.0f}s")


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage == "fit":
        stage_fit()
    elif stage == "all":
        stage_all(int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
    else:
        raise SystemExit(stage)
