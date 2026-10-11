"""Smoke tests for WP0-WP2 (core helpers, features_v2, topics). Writes outputs/core/smoke_test.txt and two
example figures (outputs/features/fig_name_share_by_year.*, outputs/core/fig_style_check.*).

    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.smoke_test
"""
from __future__ import annotations

import io
import sys
import time
from contextlib import redirect_stdout

import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import features_v2 as FV


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        check.failed += 1


check.failed = 0


def main():
    t0 = time.time()
    # ---------------------------------------------------------------- tables
    u = C.load_universe()
    f = C.load_features()
    tb = C.load_topics_bge()
    check(len(u) == 43482 and u.submission_id.is_unique, f"universe rows {len(u)} unique ids")
    check(len(f) == len(u) and (f.submission_id.values == u.submission_id.values).all(), "features_v2 aligned to universe")
    check(len(tb) == len(u) and (tb.submission_id.values == u.submission_id.values).all(), "topics_bge aligned")
    check(u.title_nfkc.str.len().gt(0).all(), "no empty titles in U")
    check((u.NA == (u.REJ | u.WD | u.DR)).all(), "NA = REJ | WD | DR")
    check(not (u.ACC & u.NA).any(), "ACC disjoint from NA")
    check(int(u.wd_post.sum()) == 349, f"wd_post = {int(u.wd_post.sum())} (plan: 349)")
    check(int(u.inconsistent.sum()) == 27, f"inconsistent rows = {int(u.inconsistent.sum())} (README: 27)")
    check(int((u.ACC | u.REJ).sum()) == 32533, f"acceptance population in U = {int((u.ACC | u.REJ).sum())}")
    check((f.name_strict <= f.name_primary).all(), "name_strict subset of name_primary")
    check((f.name_primary <= f.name_compound).all(), "name_primary subset of compound")
    nm = f.name_primary
    check(int(f[nm].lead_survives_mask.sum()) == 0, "V4: lead string survives R3 mask in 0 NAME abstracts")
    df = u[["year"]].assign(name=f.name_primary.values)
    s23, s26 = df[df.year == 2023].name.mean(), df[df.year == 2026].name.mean()
    check(abs(s23 - 0.203) < 0.005 and abs(s26 - 0.405) < 0.005, f"NAME 2023 {s23:.3f} -> 2026 {s26:.3f} (plan 0.203 -> 0.405)")
    r = f.groupby("year").f24.mean()
    check(abs(r[2024] - 0.1915) < 0.01 and abs(r[2026] - 0.0914) < 0.01,
          f"RARE21 any: 2024 {r[2024]:.4f}, 2026 {r[2026]:.4f} (scout 0.1915, 0.0914)")
    check(len([c for c in f.columns if c.startswith("mk_")]) >= 40, "D2 style markers >= 40")

    # ---------------------------------------------------------------- masking
    ab = "We present Chameleon, a model. Chameleon-based agents beat GPT-4 and LLaMA-2 on MMLU; In-Context RL-based."
    m = FV.mask_abstract(ab, "Chameleon")
    check("Chameleon" not in m and "GPT-4" not in m and "In-Context" in m and "RL-based" in m, f"mask_abstract: {m}")
    ml = FV.mask_abstract_lower(ab, "Chameleon")
    check("chameleon" not in ml.lower() and "GPT" not in ml and ml == ml.lower(), f"mask_abstract_lower: {ml}")

    # ---------------------------------------------------------------- FE / pyfixest equivalence
    d = u[u.year >= 2024][["year", "topic100", "log_authors", "llm_topic", "area_h"]].copy()
    d["name"] = f.loc[d.index, "name_primary"].astype(float).values
    d["F"] = f.loc[d.index, "F_any"].astype(float).values
    d["llm_topic"] = d.llm_topic.astype(float)
    d["ty"] = C.fe_interact(d.topic100, d.year)
    t1 = time.time()
    res = C.feols(d, "name", ["F", "log_authors", "llm_topic"], fe=["ty"], cluster="topic100")
    t_in = time.time() - t1
    print(res.summary().round(4).to_string())
    if C.HAS_PYFIXEST:
        t1 = time.time()
        pf = C.pf_feols("name ~ F + log_authors + llm_topic | ty", d, vcov={"CRV1": "topic100"})
        t_pf = time.time() - t1
        diff_b = float(np.max(np.abs(pf.coef().values - res.params.values)))
        diff_se = float(np.max(np.abs(pf.se().values - res.se.values)))
        check(diff_b < 1e-8, f"feols vs pyfixest coef max diff {diff_b:.2e}")
        check(diff_se < 1e-6, f"feols vs pyfixest CRV1 se max diff {diff_se:.2e} (in-house {t_in:.2f}s, pyfixest {t_pf:.2f}s)")
        # two-way FE (alternating projections, not nested in cluster)
        d2 = d.dropna(subset=["area_h"])
        r2 = C.feols(d2, "name", ["F", "log_authors"], fe=["ty", "area_h"], cluster="topic100")
        p2 = C.pf_feols("name ~ F + log_authors | ty + area_h", d2, vcov={"CRV1": "topic100"})
        check(float(np.max(np.abs(p2.coef().values - r2.params.values))) < 1e-6,
              "two-way FE coefficients match pyfixest")
        check(float(np.max(np.abs(p2.se().values - r2.se.values))) < 1e-5, "two-way FE CRV1 SEs match pyfixest")
        r3 = C.feols(d, "name", ["F", "log_authors"], fe=None, vcov="hetero")
        p3 = C.pf_feols("name ~ F + log_authors", d, vcov="hetero")
        check(float(np.max(np.abs(p3.se().values - r3.se.values))) < 1e-6, "HC1 SEs match pyfixest (no FE)")

    # ---------------------------------------------------------------- logit
    lg = u[["year", "topic100", "log_authors", "llm_topic", "post", "t"]].copy()
    lg["name"] = f.name_primary.astype(int).values
    lg["llm_topic"] = lg.llm_topic.astype(int)
    res_l = C.logit("name ~ t + post + post:t + log_authors + llm_topic", lg, cluster="topic100")
    tab = C.or_table(res_l, ["post:t", "post", "t"])
    print(tab.round(3).to_string())
    check(np.isfinite(tab.OR).all(), f"segmented logit runs (slope-change OR {tab.loc['post:t', 'OR']:.3f})")

    # ---------------------------------------------------------------- bootstraps
    vals = np.column_stack([lg.name.values, lg.llm_topic.values]).astype(float)
    bm = C.boot_means(vals, n_boot=200, strata=lg.year.values, seed=1)
    check(bm.shape == (200, 2) and abs(bm[:, 0].mean() - vals[:, 0].mean()) < 0.003, "boot_means stratified")
    bc = C.boot_means(vals, n_boot=100, clusters=lg.topic100.values, seed=1)
    check(bc[:, 0].std() > bm[:, 0].std(), "cluster bootstrap wider than paper bootstrap")
    rng = np.random.default_rng(0)
    idx = C.boot_indices(len(lg), strata=lg.year.values, clusters=lg.topic100.values, rng=rng)
    check(idx.min() >= 0 and idx.max() < len(lg), "boot_indices (clustered, stratified) valid")
    bs = C.bootstrap(lg, lambda x: x.name.mean(), n_boot=50, strata="year", seed=2)
    print(C.boot_summary(lg.name.mean(), bs).round(4).to_string())

    # ---------------------------------------------------------------- centroids
    E = C.load_embedding(u.iloc[:2000], "abstract", "all-MiniLM-L6-v2")
    lab = C.assign_centroids(E, C.load_centroids("minilm_k100"))
    check((lab == u.topic100.values[:2000]).mean() > 0.999, "assign_centroids reproduces MiniLM topic100")
    Eb = C.load_embedding(u.iloc[:2000], "abstract", "bge-small-en-v1.5")
    labb = C.assign_centroids(Eb, C.load_centroids("bge_k100"))
    check((labb == tb.topic100_bge.values[:2000]).mean() > 0.99, "assign_centroids reproduces bge topic100")

    # ---------------------------------------------------------------- figures
    share = (u[["year"]].assign(primary=f.name_primary.values, strict=f.name_strict.values,
                                loose=f.name_loose.values, compound=f.name_compound.values)
             .groupby("year").mean().reset_index())
    fig, ax = C.new_fig("single", 2.4)
    series = [("compound", "Compound (any colon/dash)", C.GREY), ("loose", "Loose (<=2-token lead)", C.color(1)),
              ("primary", "NAME (primary)", C.color(0)), ("strict", "Strict (1-token lead)", C.color(2))]
    for col, lab_, colr in series:
        ax.plot(share.year, share[col] * 100, color=colr, marker="o", ms=4.5, label=lab_)
    ax.axvline(2023.5, color=C.GREY, lw=0.8, ls=":")
    ax.set_ylabel("Share of titles (%)")
    ax.set_xticks(range(2017, 2027, 3))
    ax.set_xlim(2016.6, 2026.4)
    ax.legend(loc="upper left", fontsize=7)
    C.save_fig(fig, "fig_name_share_by_year", "features", data=share)
    fig, ax = C.new_fig("single", 2.0)
    C.forest(ax, ["post:t", "post", "t"], tab.OR, tab.OR_lo, tab.OR_hi, colors=[C.color(0), C.GREY, C.GREY])
    ax.set_xlabel("Odds ratio (smoke test, not a result)")
    C.save_fig(fig, "fig_style_check", "core", data=tab.reset_index())
    check((C.OUT / "features" / "fig_name_share_by_year.pdf").exists(), "save_fig wrote PDF/PNG/CSV")
    print(f"elapsed {time.time() - t0:.1f}s; failures: {check.failed}")


if __name__ == "__main__":
    buf = io.StringIO()
    with redirect_stdout(buf):
        main()
    txt = buf.getvalue()
    (C.CORE / "smoke_test.txt").write_text(txt)
    print(txt)
    sys.exit(1 if check.failed else 0)
