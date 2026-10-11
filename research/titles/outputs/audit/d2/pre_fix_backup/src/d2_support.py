"""WP6 / D2 supporting tests (exploratory; PLAN D2 S2.1 and S2.2). Results feed T2.3.

S2.1 Within-paper retitling across resubmission.
  Pairs (earlier i, later j): share >= 1 declared-ID key (any kind), 1 <= year_j - year_i <= 2, both in U.
  Procedure as in the pilot (design/eng/b_resub.py, b3.py): candidate pairs with bge abstract cosine >= 0.75,
  sorted by bge cosine, one-to-one by greedy de-duplication on i then j; then the union rule
  bge >= 0.95 OR MiniLM >= 0.85; source i not accepted (NA pool: rejected, withdrawn, desk-rejected).
  The export keeps one submission per paper family (family_id is unique), so resubmissions that the upstream
  pipeline linked into a family are absent: the pairs found here are those the linkage missed, which is
  selected on retitling. We therefore report only "even among retitled papers, NAME is not added on net"
  against the population drift implied by each pair's years, never transition rates as behaviour.
  Purity: matches per source paper among accepted sources (which should not be resubmitted) relative to
  non-accepted sources, 2018-25 sources.

S2.2 Future-tie placebo (C15), author-year panel of profile keys, 2021-26.
  For focal key k with a paper j in year T: past exposure = outcome share among the T-1 papers of k's T-1
  collaborators that do not include k; future exposure = the same share among the T-1 papers (without k) of
  keys that first co-author with k in T+1 (never before within the panel). Clean sample: j has no T-1
  collaborator of k. Model (C15 operationalisation): y_j ~ past + future + own_prev + llm_topic + log authors
  | year + topic100, SEs clustered by key. Prediction: past <= future (homophily, not tie contagion).
  Positive control: the same design with llm_topic as outcome and exposure. MDE = 2.8 x SE (80% power,
  two-sided 5%). Framed only as falsifying a tie-contagion account; no influence claims.

Outputs: resub_pairs.parquet, s2_1_resubmission.csv, s2_2_future_tie.csv, T2_3_support.csv,
         fig_S2_2_future_tie.{pdf,png,csv}, support_results.json

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_support
"""
from __future__ import annotations

import json
import re
import time

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d2_panel as P
from common import read_table

OUTDIR = P.OUTDIR
MDE_K = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)  # 2.80


# --------------------------------------------------------------------------------------------
# S2.1 resubmission pairs
# --------------------------------------------------------------------------------------------
def resub_pairs() -> tuple[pd.DataFrame, dict]:
    u = C.load_analysis_frame(feature_cols=["name_primary", "name_compound", "mk_title_case"],
                              universe_cols=["submission_id", "year", "emb_row", "title", "ACC", "NA", "REJ", "WD",
                                             "DR", "pool"])
    a = read_table("submission_authors")[["submission_id", "year", "declared_id_key"]]
    a = a[a.declared_id_key.notna() & a.submission_id.isin(set(u.submission_id))].drop_duplicates()
    nk = a.groupby("declared_id_key").submission_id.transform("size")
    a = a[nk.between(2, 300)]
    m = a.merge(a, on="declared_id_key", suffixes=("_i", "_j"))
    m = m[(m.year_j - m.year_i).between(1, 2)]
    shared = m.groupby(["submission_id_i", "submission_id_j"]).size().rename("shared_keys").reset_index()
    pos = pd.Series(np.arange(len(u)), index=u.submission_id)
    I = pos.reindex(shared.submission_id_i).to_numpy()
    J = pos.reindex(shared.submission_id_j).to_numpy()
    out = {}
    for nm, model in [("bge", "bge-small-en-v1.5"), ("minilm", "all-MiniLM-L6-v2")]:
        E = C.load_embedding(u, "abstract", model)
        E /= np.linalg.norm(E, axis=1, keepdims=True)
        out[nm] = np.einsum("ij,ij->i", E[I], E[J])
        del E
    T = C.load_embedding(u, "title", "bge-small-en-v1.5")
    T /= np.linalg.norm(T, axis=1, keepdims=True)
    tcos = np.einsum("ij,ij->i", T[I], T[J])
    df = pd.DataFrame(dict(i=I, j=J, acos=out["bge"], mcos=out["minilm"], tcos=tcos,
                           shared_keys=shared.shared_keys.to_numpy()))
    n_cand = len(df)
    df = df[df.acos >= 0.75].sort_values("acos", ascending=False).drop_duplicates("i").drop_duplicates("j")
    yr = u.year.to_numpy()
    df["yi"], df["yj"] = yr[df.i], yr[df.j]
    df["src_pool"] = u.pool.to_numpy()[df.i]
    df["src_NA"] = u.NA.to_numpy()[df.i]
    df["union"] = (df.acos >= 0.95) | (df.mcos >= 0.85)
    df["strict"] = (df.acos >= 0.97) | (df.mcos >= 0.90)
    for c in ["name_primary", "name_compound", "mk_title_case"]:
        v = u[c].astype(int).to_numpy()
        df[c + "_i"], df[c + "_j"] = v[df.i], v[df.j]
        df["d_" + c] = df[c + "_j"] - df[c + "_i"]
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()
    titles = u.title.map(norm).to_numpy()
    df["same_title"] = titles[df.i] == titles[df.j]
    df["sid_i"], df["sid_j"] = u.submission_id.to_numpy()[df.i], u.submission_id.to_numpy()[df.j]
    pop = u.groupby("year")[["name_primary", "name_compound", "mk_title_case"]].mean()
    for c in ["name_primary", "name_compound", "mk_title_case"]:
        df["drift_" + c] = pop[c].reindex(df.yj).to_numpy() - pop[c].reindex(df.yi).to_numpy()
    # same shared keys' OTHER papers in yj vs yi (context: within-key drift on new papers)
    sel = df[df.union].copy()
    sel["pair"] = np.arange(len(sel))
    pk = m.merge(sel[["sid_i", "sid_j", "pair", "yi", "yj"]], left_on=["submission_id_i", "submission_id_j"],
                 right_on=["sid_i", "sid_j"])[["pair", "declared_id_key", "yi", "yj", "sid_i", "sid_j"]].drop_duplicates()
    kp = a[["declared_id_key", "submission_id", "year"]]
    nm_ = u.set_index("submission_id").name_primary.astype(int)
    for side, ycol, excl in [("j", "yj", "sid_j"), ("i", "yi", "sid_i")]:
        x = pk.merge(kp, left_on=["declared_id_key", ycol], right_on=["declared_id_key", "year"])
        x = x[x.submission_id != x[excl]][["pair", "submission_id"]].drop_duplicates()
        x["nm"] = nm_.reindex(x.submission_id).to_numpy()
        sel[f"other_name_{side}"] = x.groupby("pair").nm.mean().reindex(sel.pair).to_numpy()
        sel[f"other_n_{side}"] = x.groupby("pair").size().reindex(sel.pair).fillna(0).to_numpy()
    df = df.merge(sel[["i", "j", "other_name_i", "other_name_j", "other_n_i", "other_n_j"]], on=["i", "j"], how="left")
    # purity
    src = pd.Series(u.pool.to_numpy(), index=np.arange(len(u)))
    base = src[(yr >= 2018) & (yr <= 2025)].map(lambda p: "ACC" if p == "ACC" else ("NA" if p in ("REJ", "WD", "DR") else "OTHER"))
    pur = {}
    for rule in ["union", "strict"]:
        x = df[df[rule] & (df.yi >= 2018)]
        sc = x.src_pool.map(lambda p: "ACC" if p == "ACC" else ("NA" if p in ("REJ", "WD", "DR") else "OTHER"))
        r_acc = (sc == "ACC").sum() / (base == "ACC").sum()
        r_na = (sc == "NA").sum() / (base == "NA").sum()
        pur[rule] = dict(match_rate_acc=float(r_acc), match_rate_na=float(r_na), purity_na=float(1 - r_acc / r_na),
                         n_acc_matches=int((sc == "ACC").sum()), n_na_matches=int((sc == "NA").sum()))
    info = dict(n_candidate_pairs=int(n_cand), n_after_greedy=int(len(df)), purity=pur)
    return df, info


def s2_1_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for rule in ["union", "strict"]:
        x = df[df[rule] & df.src_NA.astype(bool)]
        for lab, g in [("dest>=2024", x[x.yj >= 2024]), ("dest<=2023", x[x.yj <= 2023]),
                       *[(f"dest={y}", x[x.yj == y]) for y in range(2019, 2027)]]:
            if len(g) < 5:
                continue
            r = dict(rule=rule, sample=lab, n_pairs=len(g), same_title_share=float(g.same_title.mean()),
                     mean_title_cos=float(g.tcos.mean()))
            for c in ["name_primary", "name_compound", "mk_title_case"]:
                dv = g["d_" + c]
                dd = dv - g["drift_" + c]
                se = dv.std(ddof=1) / np.sqrt(len(g))
                r.update({f"{c}_src_share": float(g[c + "_i"].mean()), f"{c}_dst_share": float(g[c + "_j"].mean()),
                          f"{c}_mean_change": float(dv.mean()), f"{c}_se": float(se),
                          f"{c}_lo": float(dv.mean() - 1.96 * se), f"{c}_hi": float(dv.mean() + 1.96 * se),
                          f"{c}_adds": int((dv == 1).sum()), f"{c}_drops": int((dv == -1).sum()),
                          f"{c}_implied_drift": float(g["drift_" + c].mean()),
                          f"{c}_change_minus_drift": float(dd.mean()),
                          f"{c}_change_minus_drift_se": float(dd.std(ddof=1) / np.sqrt(len(g))),
                          f"{c}_p_change_minus_drift": float(2 * stats.t.sf(abs(dd.mean() / (dd.std(ddof=1) / np.sqrt(len(g)))), len(g) - 1)),
                          f"{c}_mde": float(MDE_K * se)})
            ok = g.other_name_i.notna() & g.other_name_j.notna()
            od = (g.other_name_j - g.other_name_i)[ok]
            r.update(samekey_other_papers_pairs=int(ok.sum()), samekey_other_papers_name_change=float(od.mean()),
                     samekey_other_papers_se=float(od.std(ddof=1) / np.sqrt(max(ok.sum(), 1))),
                     within_pair_minus_samekey=float((g.d_name_primary[ok] - od).mean()),
                     within_pair_minus_samekey_se=float((g.d_name_primary[ok] - od).std(ddof=1) / np.sqrt(max(ok.sum(), 1))))
            rows.append(r)
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
# S2.2 future-tie placebo
# --------------------------------------------------------------------------------------------
def exposure_sets(prof: pd.DataFrame) -> dict:
    AP = prof[["key", "submission_id", "year"]].rename(columns={"key": "k", "submission_id": "p", "year": "t"})
    kc, kidx = pd.factorize(AP.k)
    pc, pidx = pd.factorize(AP.p)
    AP = pd.DataFrame({"k": kc.astype(np.int32), "p": pc.astype(np.int32), "t": AP.t.to_numpy(np.int16)})
    CO = AP.merge(AP, on=["p", "t"], suffixes=("", "_c"))
    CO = CO[CO.k != CO.k_c]
    coyear = CO[["k", "k_c", "t"]].drop_duplicates()
    first_co = coyear.groupby(["k", "k_c"]).t.min().rename("t_first").reset_index()
    own = AP[["k", "p"]].rename(columns={"p": "p2"}).assign(own=True)
    APc = AP.rename(columns={"k": "k_c", "p": "p2"})
    # past: collaborators in T-1, their T-1 papers without k
    past = coyear.merge(APc, on=["k_c", "t"])
    past = past.merge(own, on=["k", "p2"], how="left")
    past = past[past.own.isna()]
    past_set = past.assign(T=past.t + 1)[["k", "T", "p2"]].drop_duplicates()
    # future: keys first co-authoring with k in T+1; their T-1 papers without k
    fut = coyear.merge(first_co, on=["k", "k_c"])
    fut = fut[fut.t == fut.t_first]
    fut = fut.assign(T=fut.t - 1, tprev=fut.t - 2)
    fut = fut.merge(APc.rename(columns={"t": "tprev"}), on=["k_c", "tprev"])
    fut = fut.merge(own, on=["k", "p2"], how="left")
    fut = fut[fut.own.isna()]
    fut_set = fut[["k", "T", "p2"]].drop_duplicates()
    # clean flag for focal rows (k, p, T): no T-1 collaborator of k among p's authors
    prevco = coyear.assign(t=coyear.t + 1)[["k", "k_c", "t"]].assign(prev=True)
    x = CO.merge(prevco, on=["k", "k_c", "t"], how="left")
    dirty = x[x.prev.notna()][["k", "p"]].drop_duplicates().assign(dirty=True)
    rows = AP.merge(dirty, on=["k", "p"], how="left")
    rows["clean"] = rows.dirty.isna()
    rows = rows.drop(columns="dirty").rename(columns={"t": "T"})
    n_coll = coyear.assign(T=coyear.t + 1).groupby(["k", "T"]).size().rename("n_past_collab")
    n_fut = fut[["k", "T", "k_c"]].drop_duplicates().groupby(["k", "T"]).size().rename("n_future_collab")
    return dict(AP=AP, rows=rows, past_set=past_set, fut_set=fut_set, pidx=pidx, kidx=kidx,
                n_coll=n_coll, n_fut=n_fut)


def future_tie(S: dict, papers: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pp = papers.set_index("submission_id").reindex(S["pidx"])
    pv = {c: pp[c].astype(float).to_numpy() for c in ["name_primary", "name_compound", "llm_topic"]}
    rows = S["rows"].copy()
    rows["log_authors"] = pp.log_authors.to_numpy()[rows.p]
    rows["llm_topic"] = pv["llm_topic"][rows.p]
    rows["topic100"] = pp.topic100.to_numpy()[rows.p]
    rows = rows.merge(S["n_coll"].reset_index(), on=["k", "T"], how="left")
    rows = rows.merge(S["n_fut"].reset_index(), on=["k", "T"], how="left")
    AP = S["AP"]
    out, panel = [], []
    for yname in ["name_primary", "name_compound", "llm_topic"]:
        y = pv[yname]
        d = rows.copy()
        d["y"] = y[d.p]
        for nm, st in [("past", S["past_set"]), ("future", S["fut_set"])]:
            e = st.assign(v=y[st.p2]).groupby(["k", "T"]).v.agg(["mean", "size"]).rename(
                columns={"mean": f"expo_{nm}", "size": f"n_{nm}_papers"}).reset_index()
            d = d.merge(e, on=["k", "T"], how="left")
        ownp = AP.assign(v=y[AP.p], T=AP.t + 1).groupby(["k", "T"]).v.mean().rename("own_prev").reset_index()
        d = d.merge(ownp, on=["k", "T"], how="left")
        ctr = ["own_prev", "log_authors"] + ([] if yname == "llm_topic" else ["llm_topic"])
        specs = [
            ("placebo: clean, T 2023-25, year+topic100 FE", ["expo_past", "expo_future"], d.clean & d["T"].between(2023, 2025), ["T", "topic100"]),
            ("placebo: clean, no topic FE (pilot spec)", ["expo_past", "expo_future"], d.clean & d["T"].between(2023, 2025), ["T"]),
            ("placebo: full sample (not clean)", ["expo_past", "expo_future"], d["T"].between(2023, 2025), ["T", "topic100"]),
            ("past only: clean, T 2023-26", ["expo_past"], d.clean & d["T"].between(2023, 2026), ["T", "topic100"]),
            ("past only: full, T 2023-26", ["expo_past"], d["T"].between(2023, 2026), ["T", "topic100"]),
        ]
        for lab, x, msk, fe in specs:
            dd = d[msk].dropna(subset=x + ctr + ["y"])
            res = C.feols(dd, "y", x + ctr, fe=fe, cluster="k")
            r = dict(outcome=yname, model=lab, nobs=res.nobs, n_keys=res.n_clusters, n_papers=int(dd.p.nunique()),
                     y_mean=float(dd.y.mean()))
            for v in x + ["own_prev"]:
                r[f"b_{v}"] = float(res.params[v]); r[f"se_{v}"] = float(res.se[v])
                r[f"mde_{v}"] = float(MDE_K * res.se[v])
            if "expo_future" in x:
                cvec = pd.Series(0.0, index=res.params.index); cvec["expo_past"] = 1; cvec["expo_future"] = -1
                diff = float(cvec @ res.params); se = float(np.sqrt(cvec @ res.vcov @ cvec))
                r.update(past_minus_future=diff, se_diff=se, lo_diff=diff - 1.96 * se, hi_diff=diff + 1.96 * se,
                         p_diff_gt0=float(stats.norm.sf(diff / se)), mde_diff=float(MDE_K * se))
            out.append(r)
        panel.append(d.assign(outcome=yname))
    return pd.DataFrame(out), pd.concat(panel, ignore_index=True)


def fig_future_tie(ft: pd.DataFrame):
    labs = {"name_primary": "NAME", "name_compound": "Compound (colon/dash)", "llm_topic": "LLM topic (positive control)"}
    panels = [("placebo: clean, T 2023-25, year+topic100 FE", "Year + topic100 FE (primary)"),
              ("placebo: clean, no topic FE (pilot spec)", "Year FE only (pilot specification)")]
    rows = []
    for model, ptitle in panels:
        sub = ft[ft.model.eq(model)].set_index("outcome")
        for o in labs:
            r = sub.loc[o]
            for kind in ("past", "future"):
                b, se = r[f"b_expo_{kind}"], r[f"se_expo_{kind}"]
                rows.append(dict(spec=ptitle, outcome=labs[o], exposure=kind, est=b, lo=b - 1.96 * se, hi=b + 1.96 * se,
                                 nobs=int(r.nobs)))
    d = pd.DataFrame(rows)
    fig, axes = C.new_fig("double", height=2.4, ncols=2, sharey=True)
    cols = {"past": C.COLORS[0], "future": C.COLORS[1]}
    for ax, (_, ptitle) in zip(axes, panels):
        for i, o in enumerate(labs.values()):
            for kind in ("past", "future"):
                r = d[(d.spec == ptitle) & (d.outcome == o) & (d.exposure == kind)].iloc[0]
                yv = (2 - i) + (0.15 if kind == "past" else -0.15)
                ax.plot([r.lo, r.hi], [yv, yv], color=cols[kind], lw=2)
                ax.plot([r.est], [yv], "o", color=cols[kind], ms=5.5,
                        label=f"{kind.capitalize()} collaborators' T-1 papers" if i == 0 else None)
        ax.axvline(0, color=C.GREY, lw=0.8, ls="--", zorder=0)
        ax.set_title(ptitle, fontsize=8.5)
        ax.grid(axis="y", visible=False); ax.tick_params(axis="y", length=0)
        ax.set_xlabel("LPM coefficient on exposure share (clean sample)")
        ax.set_ylim(-0.6, 2.6)
    axes[0].set_yticks([2, 1, 0], list(labs.values()))
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=2, fontsize=7.5, bbox_to_anchor=(0.55, 0.99))
    C.save_fig(fig, "fig_S2_2_future_tie", OUTDIR, data=d)


def main():
    t0 = time.time()
    df, info = resub_pairs()
    df.to_parquet(OUTDIR / "resub_pairs.parquet", index=False)
    s21 = s2_1_table(df)
    s21.to_csv(OUTDIR / "s2_1_resubmission.csv", index=False)
    print(info)
    print(s21[["rule", "sample", "n_pairs", "same_title_share", "name_primary_mean_change", "name_primary_se",
               "name_primary_adds", "name_primary_drops", "name_primary_implied_drift", "name_primary_change_minus_drift",
               "name_primary_mde", "samekey_other_papers_name_change", "samekey_other_papers_pairs"]].round(3).to_string())
    print(f"S2.1 {time.time() - t0:.0f}s", flush=True)

    papers, prof, _ = P.load_panel()
    S = exposure_sets(prof)
    ft, panel = future_tie(S, papers)
    ft.to_csv(OUTDIR / "s2_2_future_tie.csv", index=False)
    fig_future_tie(ft)
    print(ft[["outcome", "model", "nobs", "b_expo_past", "se_expo_past", "b_expo_future", "se_expo_future",
              "past_minus_future", "se_diff", "mde_expo_past"]].round(4).to_string())

    # T2.3 (compact)
    t = []
    for _, r in s21[s21["sample"].isin(["dest>=2024", "dest<=2023"])].iterrows():
        t.append(dict(test="S2.1 retitling", sample=f"{r['rule']} {r['sample']}", n=r.n_pairs,
                      estimate=r.name_primary_mean_change, se=r.name_primary_se,
                      comparison=f"implied drift {r.name_primary_implied_drift:+.3f}",
                      contrast=r.name_primary_change_minus_drift, contrast_se=r.name_primary_change_minus_drift_se,
                      mde=r.name_primary_mde,
                      note=f"adds {r.name_primary_adds} / drops {r.name_primary_drops}; same-key other papers "
                           f"{r.samekey_other_papers_name_change:+.3f} (n={r.samekey_other_papers_pairs})"))
    for _, r in ft[ft.model.str.startswith("placebo")].iterrows():
        t.append(dict(test=f"S2.2 future-tie ({r.outcome})", sample=r.model, n=r.nobs, estimate=r.b_expo_past,
                      se=r.se_expo_past, comparison=f"future {r.b_expo_future:.3f} (se {r.se_expo_future:.3f})",
                      contrast=r.past_minus_future, contrast_se=r.se_diff, mde=r.mde_expo_past,
                      note=f"keys {r.n_keys}; MDE of past-minus-future {r.mde_diff:.3f}"))
    pd.DataFrame(t).to_csv(OUTDIR / "T2_3_support.csv", index=False)
    pr = lambda s: (panel[(panel.outcome == "name_primary") & panel.clean & panel["T"].between(2023, 2025)]
                    .dropna(subset=["expo_past", "expo_future"])[s].describe().to_dict())
    out = dict(s2_1=dict(info=info, table=s21.to_dict(orient="records")),
               s2_2=dict(table=ft.to_dict(orient="records"),
                         sample_n_past_collab=pr("n_past_collab"), sample_n_future_collab=pr("n_future_collab")),
               mde_multiplier=float(MDE_K), elapsed_s=round(time.time() - t0, 1))
    (OUTDIR / "support_results.json").write_text(json.dumps(out, indent=1, default=float))
    print(f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
