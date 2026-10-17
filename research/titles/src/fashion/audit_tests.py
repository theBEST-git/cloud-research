"""Adversarial audit of the six candidate fashion findings (discovery data only; no confirmation data touched).

Run after audit_loc.py:  PYTHONPATH=. OMP_NUM_THREADS=4 python -m fashion.audit_tests
Writes outputs/fashion/explore/audit/results.csv (one row per hypothesis x test x term) and prints tables.
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from fashion.audit_common import AUD, est
from fashion.audit_vars import with_variants

warnings.filterwarnings("ignore")
ROWS = []


def run(h, test, d, y, rhs, terms, fe="year", cluster="topic100"):
    try:
        r = est(d, y, rhs, fe=fe, cluster=cluster, terms=terms)
    except Exception as e:  # keep going; record failure
        print(h, test, "FAILED", e)
        return
    for k, (b, se, p, n) in r.items():
        ROWS.append(dict(h=h, test=test, term=k, b=b, se=se, p=p, n=n))
    print(f"{h:4s} {test:45s} " + "  ".join(f"{k}={b:+.3f}({se:.3f})" for k, (b, se, p, n) in r.items()) + f"  n={n}")


def lincomb(d, y, rhs, fe, w, cluster="topic100"):
    """b and SE of a linear combination sum w_k * beta_k."""
    m = pf.feols(f"{y} ~ {rhs} | {fe}", data=d, vcov={"CRV1": cluster})
    b, V = m.coef(), m._vcov
    names = list(b.index)
    g = np.array([w.get(k, 0.0) for k in names])
    return float(g @ b.to_numpy()), float(np.sqrt(g @ V @ g)), int(m._N)


def main():
    AUD.mkdir(parents=True, exist_ok=True)
    f = with_variants()
    f["l_team_prev"] = np.log1p(f.team_prev_n)
    f["lloc_cur"], f["lloc_next"] = np.log1p(f.loc_cur), np.log1p(f.loc_next)
    u = C.load_universe(["submission_id", "lmax_prior_subs", "lsum_prior_accs", "share_new_authors"])
    f = f.merge(u, on="submission_id", how="left")
    acc = f[(f.ACC == 1) & (f.year <= 2025)].copy()          # H1, H6 sample (top10 defined)
    acc = acc[acc.top10.notna()]
    rev = f[f.acc_rev.notna()].copy()                        # H2, H3 sample
    h4 = f[(f.year.between(2022, 2025)) & f.hit.notna()].copy()
    h5 = f[(f.year >= 2022) & f.acc_rev.notna()].copy()
    R = "size_p + mom_p + nnr_p + log_authors"
    T = ["size_p", "mom_p", "nnr_p"]
    H4R = "ins*mom_p + ent*mom_p + size_p + nnr_p + log_authors + lprior_acc"
    H4T = ["ins:mom_p", "ent:mom_p"]
    H5R = "ins + ent + size_p + mom_p + nnr_p + log_authors + lprior_acc"
    H6R = "G1_name*mom_p + size_p + nnr_p + log_authors"

    def h4diff(d, rhs=H4R, test="", fe="year", mom="mom_p"):
        """insider slope minus entrant slope (and both slopes)."""
        try:
            b, se, n = lincomb(d, "hit", rhs, fe, {f"ins:{mom}": 1, f"ent:{mom}": -1})
            ROWS.append(dict(h="H4", test=test, term="ins-ent slope", b=b, se=se, p=np.nan, n=n))
            print(f"H4   {test:45s} ins-ent slope diff = {b:+.3f} ({se:.3f})")
        except Exception as e:
            print("H4diff failed", test, e)

    def h5diff(d, rhs=H5R, test="", fe="year", y="acc_rev"):
        try:
            b, se, n = lincomb(d, y, rhs, fe, {"ins": 1, "ent": -1})
            ROWS.append(dict(h="H5", test=test, term="ins-ent", b=b, se=se, p=np.nan, n=n))
            print(f"H5   {test:45s} ins-ent = {b:+.3f} ({se:.3f})  n={n}")
        except Exception as e:
            print("H5diff failed", test, e)

    # ---------------- 0. baseline replication ----------------
    run("H1", "baseline", acc, "top10", R, T)
    run("H23", "baseline", rev, "acc_rev", R, T)
    run("H4", "baseline", h4, "hit", H4R, H4T)
    h4diff(h4, test="baseline")
    h5diff(h5, test="baseline")
    run("H6", "baseline", acc, "top10", H6R, ["G1_name:mom_p", "mom_p"])

    # ---------------- 1. measurement variants ----------------
    for sfx, lab in [("_nt", "same-team nbrs removed"), ("_78", "tau 0.78"), ("_82", "tau 0.82"), ("_85", "tau 0.85"),
                     ("_13", "momentum t-3->t-1"), ("_nd", "nn excl. near-dups (nnr only)")]:
        Rv = f"size_p{sfx} + mom_p{sfx} + nnr_p{sfx} + log_authors"
        Tv = [f"size_p{sfx}", f"mom_p{sfx}", f"nnr_p{sfx}"]
        run("H1", f"var {lab}", acc, "top10", Rv, Tv)
        run("H23", f"var {lab}", rev, "acc_rev", Rv, Tv)
        H4v = f"ins*mom_p{sfx} + ent*mom_p{sfx} + size_p{sfx} + nnr_p{sfx} + log_authors + lprior_acc"
        run("H4", f"var {lab}", h4, "hit", H4v, [f"ins:mom_p{sfx}", f"ent:mom_p{sfx}"])
        h4diff(h4, H4v, f"var {lab}", mom=f"mom_p{sfx}")
        h5diff(h5, f"ins + ent + size_p{sfx} + mom_p{sfx} + nnr_p{sfx} + log_authors + lprior_acc", f"var {lab}")
        run("H6", f"var {lab}", acc, "top10", f"G1_name*mom_p{sfx} + size_p{sfx} + nnr_p{sfx} + log_authors",
            [f"G1_name:mom_p{sfx}"])

    # ---------------- 2. H1 attacks ----------------
    for y in range(2019, 2026):
        run("H1", f"year {y}", acc[acc.year == y].assign(one=1), "top10", R, ["mom_p"], fe="one")
    run("H1", "2019-2023 (mature citations)", acc[acc.year <= 2023], "top10", R, ["mom_p"])
    run("H1", "2024-2025 only", acc[acc.year >= 2024], "top10", R, ["mom_p"])
    run("H1", "outcome log1p cites", acc, "y", R, ["mom_p"])
    run("H1", "outcome cite percentile", acc, "cite_pct", R, ["mom_p"])
    top1 = acc.groupby("year").cite_pct.transform(lambda s: s > s.quantile(0.99))
    run("H1", "drop top 1% cited", acc[~top1], "top10", R, ["mom_p"])
    run("H1", "drop top 1% cited, log cites", acc[~top1], "y", R, ["mom_p"])
    run("H1", "+ llm_topic", acc, "top10", R + " + llm_topic", ["mom_p"])
    run("H1", "non-LLM topics only", acc[acc.llm_topic == 0], "top10", R, ["mom_p"])
    run("H1", "topic100 FE", acc, "top10", R, ["mom_p", "size_p"], fe="year + topic100")
    run("H1", "topic50 FE", acc, "top10", R, ["mom_p"], fe="year + topic50")
    run("H1", "rolling-topic FE (look-ahead free)", acc, "top10", R, ["mom_p"], fe="r_topic")
    run("H1", "topic100 x year FE", acc, "top10", R, ["mom_p"], fe="year^topic100")
    run("H1", "area_h x year FE (2024-25)", acc, "top10", R, ["mom_p"], fe="year^area_h")
    run("H1", "+ log_abs_words + hub_p", acc, "top10", R + " + log_abs_words + hub_p", ["mom_p"])
    run("H1", "+ title G1-G6", acc, "top10", R + " + G1_name + G2_assertive + G3_question + G4_llm_words + G5a_length5 + G6a_meme",
        ["mom_p"])
    run("H1", "n12 (c1+c2) >= 20", acc[acc.n12 >= 20], "top10", R, ["mom_p"])
    run("H1", "n12 (c1+c2) >= 50", acc[acc.n12 >= 50], "top10", R, ["mom_p"])
    run("H1", "n12 < 50", acc[acc.n12 < 50], "top10", R, ["mom_p"])
    run("H1", "excl resub & near-dup (nn>=.95)", acc[(acc.resub == 0) & (acc.nn_prev < 0.95)], "top10", R, ["mom_p"])
    run("H1", "cluster topic50", acc, "top10", R, ["mom_p"], cluster="topic50")
    run("H1", "cluster r_topic", acc, "top10", R, ["mom_p"], cluster="r_topic")
    run("H1", "+ team (2022+: lprior_acc, ins, ent)", acc[acc.year >= 2022], "top10", R + " + lprior_acc + ins + ent", ["mom_p"])
    run("H1", "2022+ without team controls", acc[acc.year >= 2022], "top10", R, ["mom_p"])
    run("H1", "mechanism: + loc_cur, loc_next (ex post)", acc, "top10", R + " + lloc_cur + lloc_next",
        ["mom_p"])
    # leave-one-topic50-out
    lo = []
    for k in sorted(acc.topic50.unique()):
        r = est(acc[acc.topic50 != k], "top10", R, terms=["mom_p"])["mom_p"]
        lo.append((k, r[0]))
    lo = pd.DataFrame(lo, columns=["topic50", "b"])
    ROWS.append(dict(h="H1", test="leave-one-topic50-out min", term="mom_p", b=lo.b.min(), se=np.nan, p=np.nan, n=len(lo)))
    ROWS.append(dict(h="H1", test="leave-one-topic50-out max", term="mom_p", b=lo.b.max(), se=np.nan, p=np.nan, n=len(lo)))
    print("H1 leave-one-topic50-out range", lo.b.min().round(3), lo.b.max().round(3), "most influential:",
          lo.loc[lo.b.idxmin(), "topic50"])
    # leave-one-year-out
    for y in range(2019, 2026):
        run("H1", f"leave out {y}", acc[acc.year != y], "top10", R, ["mom_p"])
    # S2 matching selection
    allacc = f[(f.ACC == 1) & (f.year <= 2025)].copy()
    allacc["matched"] = allacc.top10.notna().astype(float)
    run("H1", "selection: P(S2 matched | accepted)", allacc, "matched", R, ["mom_p"])

    # ---------------- 3. H2 / H3 attacks ----------------
    for y in range(2019, 2027):
        run("H23", f"year {y}", rev[rev.year == y].assign(one=1), "acc_rev", R, ["size_p", "mom_p"], fe="one")
    run("H23", "ACC vs REJ only (drop WD)", rev, "acc_rej", R, T)
    run("H23", "outcome: withdrawn", rev, "wd", R, T)
    run("H23", "topic100 FE", rev, "acc_rev", R, T, fe="year + topic100")
    run("H23", "topic50 FE", rev, "acc_rev", R, T, fe="year + topic50")
    run("H23", "rolling-topic FE", rev, "acc_rev", R, T, fe="r_topic")
    run("H23", "topic100 x year FE", rev, "acc_rev", R, T, fe="year^topic100")
    r24 = rev[rev.year >= 2024]
    run("H23", "2024-26 year FE (ref for area)", r24, "acc_rev", R, T)
    run("H23", "2024-26 area_h x year FE", r24, "acc_rev", R, T, fe="year^area_h")
    run("H23", "2024-26 area_h x year + topic100 FE", r24, "acc_rev", R, T, fe="year^area_h + topic100")
    run("H23", "+ llm_topic + log_abs_words + hub_p", rev, "acc_rev", R + " + llm_topic + log_abs_words + hub_p", T)
    run("H23", "2022+ year FE", rev[rev.year >= 2022], "acc_rev", R, T)
    run("H23", "2022+ + lprior_acc + entry + resub", rev[rev.year >= 2022], "acc_rev",
        R + " + lprior_acc + ins + ent + resub", T)
    run("H23", "n12 >= 20", rev[rev.n12 >= 20], "acc_rev", R, T)
    run("H23", "excl resub & near-dup", rev[(rev.resub == 0) & (rev.nn_prev < 0.95)], "acc_rev", R, T)
    run("H23", "excl 2026", rev[rev.year <= 2025], "acc_rev", R, T)
    run("H23", "size only (no mom/nnr)", rev, "acc_rev", "size_p + log_authors", ["size_p"])
    run("H23", "mom only", rev, "acc_rev", "mom_p + log_authors", ["mom_p"])
    run("H23", "cluster topic50", rev, "acc_rev", R, T, cluster="topic50")
    run("H23", "cluster r_topic", rev, "acc_rev", R, T, cluster="r_topic")
    # lower-is-better check: LPM on hit (accepted & top10) for the same RHS
    run("H23", "outcome hit (reviewed 2019-25)", f[f.hit.notna()], "hit", R, T)

    # ---------------- 4. H4 attacks ----------------
    run("H4", "+ team_area_acc*mom_p", h4, "hit", H4R + " + team_area_acc*mom_p", H4T + ["team_area_acc:mom_p"])
    h4diff(h4, H4R + " + team_area_acc*mom_p", "+ team_area_acc*mom_p")
    run("H4", "+ l_team_prev*mom_p", h4, "hit", H4R + " + l_team_prev*mom_p", H4T + ["mom_p:l_team_prev"])
    h4diff(h4, H4R + " + l_team_prev*mom_p", "+ l_team_prev*mom_p")
    full = H4R + " + lprior_acc:mom_p + log_authors:mom_p + l_team_prev*mom_p + team_area_acc*mom_p"
    run("H4", "+ all team x mom", h4, "hit", full, H4T)
    h4diff(h4, full, "+ all team x mom")
    run("H4", "+ ins/ent x size_p, nnr_p", h4, "hit", H4R + " + ins:size_p + ent:size_p + ins:nnr_p + ent:nnr_p", H4T)
    h4diff(h4, H4R + " + ins:size_p + ent:size_p + ins:nnr_p + ent:nnr_p", "+ ins/ent x size_p, nnr_p")
    h4m = h4.copy()
    h4m["ins_r"] = ((h4m.entry == "insider") & (h4m.team_area_cos >= 0.95)).astype(float)
    h4m["ins_f"] = ((h4m.entry == "insider") & (h4m.team_area_cos < 0.95)).astype(float)
    run("H4", "insider split: version(>=.95) vs follow-up", h4m, "hit",
        "ins_r*mom_p + ins_f*mom_p + ent*mom_p + size_p + nnr_p + log_authors + lprior_acc",
        ["ins_r:mom_p", "ins_f:mom_p", "ent:mom_p"])
    run("H4", "excl resub & team_area_cos>=.95", h4[(h4.resub == 0) & ~(h4.team_area_cos >= 0.95)], "hit", H4R, H4T)
    h4diff(h4[(h4.resub == 0) & ~(h4.team_area_cos >= 0.95)], test="excl resub & team_area_cos>=.95")
    run("H4", "outcome acc_rev (2022-25)", h4, "acc_rev", H4R, H4T)
    h4a = acc[acc.year >= 2022]
    run("H4", "outcome top10 | accepted (2022-25)", h4a, "top10", H4R, H4T)
    for y in range(2022, 2026):
        run("H4", f"year {y}", h4[h4.year == y].assign(one=1), "hit", H4R, H4T, fe="one")
    run("H4", "2023-25", h4[h4.year >= 2023], "hit", H4R, H4T)
    h4diff(h4[h4.year >= 2023], test="2023-25")
    run("H4", "non-LLM", h4[h4.llm_topic == 0], "hit", H4R, H4T)
    h4diff(h4[h4.llm_topic == 0], test="non-LLM")
    run("H4", "topic100 FE", h4, "hit", H4R, H4T, fe="year + topic100")
    h4diff(h4, test="topic100 FE", fe="year + topic100")
    run("H4", "n12 >= 20", h4[h4.n12 >= 20], "hit", H4R, H4T)
    h4diff(h4[h4.n12 >= 20], test="n12 >= 20")
    run("H4", "ins|ent only, + l_team_prev, lsum_prior_accs", h4[h4.entry != "newcomer"], "hit",
        "ins*mom_p + size_p + nnr_p + log_authors + lprior_acc + l_team_prev*mom_p + lsum_prior_accs*mom_p", ["ins:mom_p"])
    # same-team-free momentum + all team interactions + resub exclusion (the strictest)
    strict = ("ins*mom_p_nt + ent*mom_p_nt + size_p_nt + nnr_p_nt + log_authors + lprior_acc + "
              "lprior_acc:mom_p_nt + l_team_prev*mom_p_nt + team_area_acc*mom_p_nt")
    hs = h4[(h4.resub == 0) & ~(h4.team_area_cos >= 0.95)]
    run("H4", "strict (nt + team x mom + no versions)", hs, "hit", strict, ["ins:mom_p_nt", "ent:mom_p_nt"])
    h4diff(hs, strict, "strict (nt + team x mom + no versions)", mom="mom_p_nt")

    # ---------------- 5. H5 attacks ----------------
    h5diff(h5, H5R + " + l_team_prev", "+ l_team_prev")
    h5["tp_bin"] = pd.cut(h5.team_prev_n, [-1, 0, 1, 2, 4, 8, 16, 32, 1e6]).astype(str)
    h5diff(h5, H5R, "team_prev_n bin FE", fe="year + tp_bin")
    h5diff(h5, H5R + " + lmax_prior_subs + lsum_prior_accs + share_new_authors", "+ more experience ctrls")
    h5diff(h5, H5R + " + l_team_prev + lmax_prior_subs + lsum_prior_accs + share_new_authors", "+ all experience ctrls",
           fe="year + tp_bin")
    run("H5", "+ team_area_acc", h5, "acc_rev", H5R + " + team_area_acc", ["ins", "ent", "team_area_acc"])
    h5diff(h5, H5R + " + team_area_acc", "+ team_area_acc")
    h5diff(h5[(h5.resub == 0) & ~(h5.team_area_cos >= 0.95)], test="excl resub & versions (cos>=.95)")
    h5x = h5.copy()
    h5x["ins_acc"] = ((h5x.entry == "insider") & (h5x.team_area_acc == 1)).astype(float)
    h5x["ins_noacc"] = ((h5x.entry == "insider") & (h5x.team_area_acc == 0)).astype(float)
    run("H5", "insider split by prior close paper accepted", h5x, "acc_rev",
        "ins_acc + ins_noacc + ent + size_p + mom_p + nnr_p + log_authors + lprior_acc", ["ins_acc", "ins_noacc", "ent"])
    b, se, n = lincomb(h5x, "acc_rev", "ins_acc + ins_noacc + ent + size_p + mom_p + nnr_p + log_authors + lprior_acc",
                       "year", {"ins_noacc": 1, "ent": -1})
    ROWS.append(dict(h="H5", test="insider w/o accepted close paper - entrant", term="ins_noacc-ent", b=b, se=se, p=np.nan, n=n))
    print(f"H5   insider w/o accepted close paper - entrant = {b:+.3f} ({se:.3f})")
    # dose-response in team_area_cos among non-newcomers
    nn = h5[h5.entry != "newcomer"].copy()
    nn["cosbin"] = pd.cut(nn.team_area_cos, [-1, 0.6, 0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.01]).astype(str)
    run("H5", "dose: acc by team_area_cos bin (ref <.6)", nn, "acc_rev",
        "C(cosbin) + size_p + mom_p + nnr_p + log_authors + lprior_acc + l_team_prev", None)
    for tau in (0.75, 0.78, 0.82, 0.85, 0.90):
        h5t = h5.copy()
        h5t["ins"] = np.where(h5t.entry == "newcomer", 0.0, (h5t.team_area_cos >= tau).astype(float))
        h5t["ent"] = np.where(h5t.entry == "newcomer", 0.0, (h5t.team_area_cos < tau).astype(float))
        h5diff(h5t, H5R + " + l_team_prev", f"insider threshold {tau} (+l_team_prev)")
    for y in range(2022, 2027):
        h5diff(h5[h5.year == y].assign(one=1), H5R, f"year {y}", fe="one")
    h5diff(h5[h5.year.between(2023, 2025)], test="2023-25")
    h5diff(h5[h5.llm_topic == 0], test="non-LLM")
    h5diff(h5, test="ACC vs REJ", y="acc_rej")
    h5diff(h5, test="topic100 FE", fe="year + topic100")
    h5diff(h5[h5.year >= 2024], test="2024-26 area_h x year FE", fe="year^area_h")
    h5diff(h5, H5R.replace("size_p + mom_p + nnr_p", "size_p_nt + mom_p_nt + nnr_p_nt"), "same-team-free heat ctrls")
    h5diff(h5, "ins + ent + log_authors", "no controls but log_authors")
    run("H5", "outcome withdrawn", h5, "wd", H5R, ["ins", "ent"])
    h5s = h5[(h5.resub == 0) & ~(h5.team_area_cos >= 0.95)]
    h5diff(h5s, H5R.replace("size_p + mom_p + nnr_p", "size_p_nt + mom_p_nt + nnr_p_nt")
           + " + l_team_prev + lmax_prior_subs + lsum_prior_accs + share_new_authors", "strict (all ctrls, no versions)",
           fe="year + tp_bin")

    # ---------------- 6. H6 attacks ----------------
    G = "G1_name*mom_p + size_p + nnr_p + log_authors"
    run("H6", "+ G5a, G2, llm_topic", acc, "top10", G + " + G5a_length5 + G2_assertive + llm_topic", ["G1_name:mom_p"])
    run("H6", "+ G5a, G2, llm_topic, topic50 FE", acc, "top10", G + " + G5a_length5 + G2_assertive + llm_topic",
        ["G1_name:mom_p"], fe="year + topic50")
    ctl_x = " + (G5a_length5 + G2_assertive + llm_topic + log_authors + G3_question + G4_llm_words)*mom_p"
    run("H6", "+ controls x mom_p, topic50 FE", acc, "top10", G + ctl_x, ["G1_name:mom_p"], fe="year + topic50")
    run("H6", "+ controls x mom_p, topic100 x year FE", acc, "top10", G + ctl_x, ["G1_name:mom_p"], fe="year^topic100")
    run("H6", "+ G1 x size_p, G1 x nnr_p", acc, "top10", G + " + G1_name:size_p + G1_name:nnr_p", ["G1_name:mom_p"])
    run("H6", "non-LLM", acc[acc.llm_topic == 0], "top10", G, ["G1_name:mom_p"])
    run("H6", "outcome log1p cites", acc, "y", G, ["G1_name:mom_p"])
    run("H6", "outcome cite_pct", acc, "cite_pct", G, ["G1_name:mom_p"])
    run("H6", "drop top 1% cited", acc[~top1], "top10", G, ["G1_name:mom_p"])
    run("H6", "2019-2023", acc[acc.year <= 2023], "top10", G, ["G1_name:mom_p"])
    run("H6", "2024-2025", acc[acc.year >= 2024], "top10", G, ["G1_name:mom_p"])
    for y in range(2019, 2026):
        run("H6", f"year {y}", acc[acc.year == y].assign(one=1), "top10", G, ["G1_name:mom_p"], fe="one")
    run("H6", "n12 >= 20", acc[acc.n12 >= 20], "top10", G, ["G1_name:mom_p"])
    run("H6", "cluster topic50", acc, "top10", G, ["G1_name:mom_p"], cluster="topic50")
    run("H6", "2022+ + lprior_acc, ins, ent", acc[acc.year >= 2022], "top10", G + " + lprior_acc + ins + ent",
        ["G1_name:mom_p"])
    run("H6", "2022+ (no team ctrls)", acc[acc.year >= 2022], "top10", G, ["G1_name:mom_p"])
    run("H6", "mom_p tercile: G1 effect in hi vs lo", acc, "top10", "G1_name*C(mom3) + size_p + nnr_p + log_authors", None)
    # placebo family: every other binary/continuous title feature x mom_p
    for g in ["G2_assertive", "G3_question", "G4_llm_words", "G5a_length5", "G5b_informative", "G6a_meme", "G6b_tentative",
              "ortho_mixed_case", "ortho_all_caps", "ortho_word"]:
        dd = acc.copy()
        dd[g] = dd[g].astype(float)
        run("H6", f"family: {g} x mom_p", dd, "top10", f"{g}*mom_p + size_p + nnr_p + log_authors", [f"{g}:mom_p"])

    # ---------------- 7. nnr_p exploratory ----------------
    run("NNR", "acc baseline", rev, "acc_rev", R, ["nnr_p"])
    run("NNR", "top10 baseline", acc, "top10", R, ["nnr_p"])
    for sfx, lab in [("_nt", "non-team nn"), ("_nd", "nn excl near-dup")]:
        run("NNR", f"acc {lab}", rev, "acc_rev", f"size_p + mom_p + nnr_p{sfx} + log_authors", [f"nnr_p{sfx}"])
        run("NNR", f"top10 {lab}", acc, "top10", f"size_p + mom_p + nnr_p{sfx} + log_authors", [f"nnr_p{sfx}"])
    run("NNR", "acc excl resub/near-dup/insider-version", rev[(rev.resub == 0) & (rev.nn_prev < 0.95) & ~(rev.team_area_cos >= 0.95)],
        "acc_rev", R, ["nnr_p"])
    run("NNR", "top10 excl resub/near-dup/insider-version", acc[(acc.resub == 0) & (acc.nn_prev < 0.95) & ~(acc.team_area_cos >= 0.95)],
        "top10", R, ["nnr_p"])
    run("NNR", "acc + hub_p, log_abs_words", rev, "acc_rev", R + " + hub_p + log_abs_words", ["nnr_p"])
    run("NNR", "top10 + hub_p, log_abs_words", acc, "top10", R + " + hub_p + log_abs_words", ["nnr_p"])
    run("NNR", "acc mom x nnr", rev, "acc_rev", "size_p + mom_p*nnr_p + log_authors", ["nnr_p", "mom_p:nnr_p"])
    run("NNR", "top10 mom x nnr", acc, "top10", "size_p + mom_p*nnr_p + log_authors", ["nnr_p", "mom_p:nnr_p"])
    run("NNR", "acc mom x nnr (nt)", rev, "acc_rev", "size_p_nt + mom_p_nt*nnr_p_nt + log_authors", ["nnr_p_nt", "mom_p_nt:nnr_p_nt"])
    run("NNR", "top10 mom x nnr (nt)", acc, "top10", "size_p_nt + mom_p_nt*nnr_p_nt + log_authors", ["nnr_p_nt", "mom_p_nt:nnr_p_nt"])
    run("NNR", "acc topic100 FE", rev, "acc_rev", R, ["nnr_p"], fe="year + topic100")
    run("NNR", "top10 topic100 FE", acc, "top10", R, ["nnr_p"], fe="year + topic100")

    out = pd.DataFrame(ROWS)
    out.to_csv(AUD / "results.csv", index=False)
    print("wrote", AUD / "results.csv", len(out))


if __name__ == "__main__":
    main()
