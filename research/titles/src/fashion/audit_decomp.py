"""Audit follow-ups: control decompositions for H3 and H4, heterogeneity tests, permutation calibration of the
clustered SEs, empirical-Bayes shrinkage of the H6 title-feature family, and repeated random half-split stability.
Discovery data only. Appends to outputs/fashion/explore/audit/results_decomp.csv.
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from fashion.audit_common import AUD, est
from fashion.audit_tests import lincomb
from fashion.audit_vars import with_variants

warnings.filterwarnings("ignore")
ROWS = []
R = "size_p + mom_p + nnr_p + log_authors"
H4R = "ins*mom_p + ent*mom_p + size_p + nnr_p + log_authors + lprior_acc"
G = "G1_name*mom_p + size_p + nnr_p + log_authors"


def run(h, test, d, y, rhs, terms, fe="year", cluster="topic100"):
    r = est(d, y, rhs, fe=fe, cluster=cluster, terms=terms)
    for k, (b, se, p, n) in r.items():
        ROWS.append(dict(h=h, test=test, term=k, b=b, se=se, p=p, n=n))
    print(f"{h:4s} {test:50s} " + "  ".join(f"{k}={b:+.3f}({se:.3f})" for k, (b, se, p, n) in r.items()) + f"  n={n}")
    return r


def diff(h, test, d, y, rhs, w, fe="year"):
    b, se, n = lincomb(d, y, rhs, fe, w)
    ROWS.append(dict(h=h, test=test, term="contrast", b=b, se=se, p=np.nan, n=n))
    print(f"{h:4s} {test:50s} contrast = {b:+.3f} ({se:.3f})  n={n}")


def tstat(d, y, rhs, term, fe="year"):
    m = pf.feols(f"{y} ~ {rhs} | {fe}", data=d, vcov={"CRV1": "topic100"})
    return float(m.coef()[term] / m.se()[term])


def main():
    f = with_variants()
    f["l_team_prev"] = np.log1p(f.team_prev_n)
    u = C.load_universe(["submission_id", "lmax_prior_subs", "lsum_prior_accs", "share_new_authors"])
    f = f.merge(u, on="submission_id", how="left")
    acc = f[(f.ACC == 1) & (f.year <= 2025) & f.top10.notna()].copy()
    rev = f[f.acc_rev.notna()].copy()
    r22 = rev[rev.year >= 2022]
    h4 = f[(f.year.between(2022, 2025)) & f.hit.notna()].copy()
    T = ["size_p"]

    # ---- H3: which control removes the size effect? ----
    print("corr(size_p, hub_p) =", round(rev[["size_p", "hub_p"]].corr().iloc[0, 1], 3),
          " corr(size_p, log_abs_words) =", round(rev[["size_p", "log_abs_words"]].corr().iloc[0, 1], 3))
    for lab, extra in [("+ llm_topic", "llm_topic"), ("+ log_abs_words", "log_abs_words"), ("+ hub_p", "hub_p"),
                       ("+ log_abs_words + llm_topic", "log_abs_words + llm_topic")]:
        run("H3", lab, rev, "acc_rev", R + " + " + extra, T)
    run("H3", "+ hub_p, ACC vs REJ", rev, "acc_rej", R + " + hub_p", T)
    run("H3", "+ hub_p, topic100 FE", rev, "acc_rev", R + " + hub_p", T, fe="year + topic100")
    run("H3", "2022+ baseline", r22, "acc_rev", R, T)
    for lab, extra in [("+ lprior_acc", "lprior_acc"), ("+ ins + ent", "ins + ent"), ("+ resub", "resub"),
                       ("+ l_team_prev", "l_team_prev"), ("+ lsum_prior_accs + lmax_prior_subs", "lsum_prior_accs + lmax_prior_subs"),
                       ("+ lprior_acc + ins + ent", "lprior_acc + ins + ent")]:
        run("H3", "2022+ " + lab, r22, "acc_rev", R + " + " + extra, T)
    run("H3", "2022+ + lprior_acc (same-team-free size)", r22, "acc_rev",
        "size_p_nt + mom_p_nt + nnr_p_nt + log_authors + lprior_acc", ["size_p_nt"])
    run("H3", "2022+ newcomers only", r22[r22.entry == "newcomer"], "acc_rev", R, T)
    run("H3", "2022+ entrants only", r22[r22.entry == "entrant"], "acc_rev", R + " + lprior_acc", T)
    run("H3", "2022+ insiders only", r22[r22.entry == "insider"], "acc_rev", R + " + lprior_acc", T)
    run("H3", "2022+ all ctrls (+hub, words, llm, team)", r22, "acc_rev",
        R + " + hub_p + log_abs_words + llm_topic + lprior_acc + ins + ent + l_team_prev", T)
    # how much of size_p is explained by team experience?
    print("mean lprior_acc by size tercile (2022+):", r22.groupby("size3", observed=True).lprior_acc.mean().round(3).to_dict())
    print("insider share by size tercile (2022+):", r22.groupby("size3", observed=True).ins.mean().round(3).to_dict())

    # ---- H2: heterogeneity across years and equivalence ----
    m0 = pf.feols(f"acc_rev ~ {R} | year", data=rev, vcov={"CRV1": "topic100"})
    m1 = pf.feols("acc_rev ~ size_p + nnr_p + log_authors + mom_p:C(year) | year", data=rev, vcov={"CRV1": "topic100"})
    names = [n for n in m1.coef().index if "mom_p" in n and "year" in n]
    print("H2 by-year terms:", names)
    b = m1.coef()[names].to_numpy()
    idx = [list(m1.coef().index).index(n) for n in names]
    V = m1._vcov[np.ix_(idx, idx)]
    D = np.diff(np.eye(len(b)), axis=0)
    W = float((D @ b) @ np.linalg.solve(D @ V @ D.T, D @ b))
    from scipy import stats
    print(f"H2 year-heterogeneity Wald chi2({len(b) - 1}) = {W:.1f}, p = {stats.chi2.sf(W, len(b) - 1):.3g}")
    ROWS.append(dict(h="H2", test="year heterogeneity Wald", term=f"chi2({len(b) - 1})", b=W, se=np.nan,
                     p=float(stats.chi2.sf(W, len(b) - 1)), n=int(m1._N)))
    bm, sm = float(m0.coef()["mom_p"]), float(m0.se()["mom_p"])
    print(f"H2 90% CI for mom_p: [{bm - 1.645 * sm:+.3f}, {bm + 1.645 * sm:+.3f}] (TOST at margin 0.03: "
          f"{'equivalent' if (bm - 1.645 * sm > -0.03 and bm + 1.645 * sm < 0.03) else 'not shown'})")

    # ---- H1: heterogeneity by period ----
    a2 = acc.assign(post=(acc.year >= 2024).astype(float))
    run("H1", "mom_p x post2024", a2, "top10", R + " + mom_p:post", ["mom_p", "mom_p:post"])
    run("H1", "2019-23 + llm_topic + topic50 FE", acc[acc.year <= 2023], "top10", R + " + llm_topic", ["mom_p"], fe="year + topic50")
    run("H1", "2024-25 + llm_topic + topic50 FE", acc[acc.year >= 2024], "top10", R + " + llm_topic", ["mom_p"], fe="year + topic50")
    run("H1", "rolling-topic FE + llm_topic", acc, "top10", R + " + llm_topic", ["mom_p"], fe="r_topic")

    # ---- H4: decomposition (hit and top10|accepted) ----
    for y, d in [("hit", h4), ("top10", acc[acc.year >= 2022])]:
        base = H4R
        for lab, extra in [("baseline", ""), ("+ lprior_acc:mom_p", " + lprior_acc:mom_p"),
                           ("+ log_authors:mom_p", " + log_authors:mom_p"), ("+ l_team_prev*mom_p", " + l_team_prev*mom_p"),
                           ("+ lsum_prior_accs*mom_p", " + lsum_prior_accs*mom_p"),
                           ("+ team_area_acc*mom_p", " + team_area_acc*mom_p"),
                           ("+ l_team_prev*mom_p + lprior_acc:mom_p", " + l_team_prev*mom_p + lprior_acc:mom_p"),
                           ("+ l_team_prev*mom_p + team_area_acc*mom_p", " + l_team_prev*mom_p + team_area_acc*mom_p")]:
            diff("H4", f"[{y}] {lab}: ins-ent slope", d, y, base + extra, {"ins:mom_p": 1, "ent:mom_p": -1})
    ins = f[(f.entry == "insider") & f.year.between(2022, 2025)]
    print("share of insiders with accepted close prior (team_area_acc):", round(ins.team_area_acc.mean(), 3))
    print("median team_prev_n: insider", f[f.entry == "insider"].team_prev_n.median(), "entrant",
          f[f.entry == "entrant"].team_prev_n.median())
    # within team_prev_n strata (ins-ent slope in each stratum)
    h4s = h4[h4.entry != "newcomer"].copy()
    h4s["tp3"] = pd.qcut(h4s.team_prev_n, 3, labels=["lo", "mid", "hi"])
    for k, g in h4s.groupby("tp3", observed=True):
        run("H4", f"ins|ent, team_prev_n tercile {k}", g, "hit",
            "ins*mom_p + size_p + nnr_p + log_authors + lprior_acc", ["ins:mom_p"])

    # ---- H6: EB shrinkage across the title-feature x mom_p family ----
    fam = ["G1_name", "G2_assertive", "G3_question", "G4_llm_words", "G5a_length5", "G5b_informative", "G6a_meme",
           "G6b_tentative", "ortho_mixed_case", "ortho_all_caps", "ortho_word"]
    bs, ss = [], []
    for g in fam:
        d = acc.copy()
        d[g] = d[g].astype(float)
        d[g] = (d[g] - d[g].mean()) / d[g].std()  # standardise so effects are comparable
        r = est(d, "top10", f"{g}*mom_p + size_p + nnr_p + log_authors", terms=[f"{g}:mom_p"])[f"{g}:mom_p"]
        bs.append(r[0]); ss.append(r[1])
    bs, ss = np.array(bs), np.array(ss)
    tau2 = max(0.0, float(np.var(bs, ddof=1) - np.mean(ss ** 2)))
    shr = tau2 / (tau2 + ss[0] ** 2) if tau2 > 0 else 0.0
    print(f"H6 family (per-SD): G1 b={bs[0]:+.4f} se={ss[0]:.4f}; tau^2={tau2:.2e}; EB shrink factor={shr:.2f}; "
          f"|t| rank of G1 = {int((np.abs(bs / ss) >= abs(bs[0] / ss[0])).sum())}/{len(fam)}")
    ROWS.append(dict(h="H6", test="EB shrink factor (title family)", term="G1_name:mom_p", b=shr, se=np.nan, p=np.nan, n=len(fam)))

    # ---- permutation calibration of clustered SEs (null by construction) ----
    rng = np.random.default_rng(0)
    ts = []
    for _ in range(300):
        d = acc.copy()
        d["G1_name"] = d.groupby("year").G1_name.transform(lambda s: rng.permutation(s.to_numpy()))
        ts.append(tstat(d, "top10", G, "G1_name:mom_p"))
    ts = np.array(ts)
    t_obs = tstat(acc, "top10", G, "G1_name:mom_p")
    print(f"H6 permutation (G1 shuffled within year, 300 draws): sd(t)={ts.std():.2f}, share |t|>1.96={np.mean(np.abs(ts) > 1.96):.3f}, "
          f"perm p for t_obs={t_obs:.2f}: {np.mean(np.abs(ts) >= abs(t_obs)):.3f}")
    ROWS.append(dict(h="H6", test="permutation p (300)", term="G1_name:mom_p", b=t_obs, se=float(ts.std()),
                     p=float(np.mean(np.abs(ts) >= abs(t_obs))), n=300))
    ts = []
    for _ in range(300):
        d = acc.copy()
        d["mom_p"] = d.groupby("year").mom_p.transform(lambda s: rng.permutation(s.to_numpy()))
        ts.append(tstat(d, "top10", R, "mom_p"))
    ts = np.array(ts)
    print(f"H1 permutation (mom_p shuffled within year): sd(t)={ts.std():.2f}, share |t|>1.96={np.mean(np.abs(ts) > 1.96):.3f}")
    ROWS.append(dict(h="H1", test="permutation null sd(t) (300)", term="mom_p", b=float(ts.std()), se=np.nan,
                     p=float(np.mean(np.abs(ts) > 1.96)), n=300))

    # ---- repeated random half-splits: P(half B significant, same sign | full-sample spec) ----
    specs = {
        "H1": (acc, "top10", R, "mom_p", 1),
        "H2 (|b|<.03)": (rev, "acc_rev", R, "mom_p", 0),
        "H3": (rev, "acc_rev", R, "size_p", 1),
        "H6": (acc, "top10", G, "G1_name:mom_p", 1),
    }
    res = {k: [] for k in list(specs) + ["H4", "H5"]}
    h5 = f[(f.year >= 2022) & f.acc_rev.notna()]
    for s in range(100):
        r = np.random.default_rng(100 + s)
        for k, (d, y, rhs, term, sign) in specs.items():
            m = d[r.random(len(d)) < 0.5]
            e = est(m, y, rhs, terms=[term])[term]
            res[k].append((e[0] > 0 and e[2] < 0.05) if sign else (abs(e[0]) + 1.645 * e[1] < 0.03 and e[0] - 1.645 * e[1] > -0.03))
        m = h4[r.random(len(h4)) < 0.5]
        b, se, _ = lincomb(m, "hit", H4R, "year", {"ins:mom_p": 1, "ent:mom_p": -1})
        res["H4"].append(b / se > 1.96)
        m = h5[r.random(len(h5)) < 0.5]
        b, se, _ = lincomb(m, "acc_rev", "ins + ent + size_p + mom_p + nnr_p + log_authors + lprior_acc", "year", {"ins": 1, "ent": -1})
        res["H5"].append(b / se > 1.96)
    for k, v in res.items():
        print(f"half-sample replication rate {k}: {np.mean(v):.2f}")
        ROWS.append(dict(h=k, test="half-sample replication rate (100 splits)", term="", b=float(np.mean(v)), se=np.nan, p=np.nan, n=100))
    pd.DataFrame(ROWS).to_csv(AUD / "results_decomp.csv", index=False)


if __name__ == "__main__":
    main()
