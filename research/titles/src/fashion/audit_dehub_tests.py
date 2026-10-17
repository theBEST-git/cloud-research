"""Audit: H1-H6 with de-hubbed (centred-embedding) density, momentum and closeness (see audit_dehub.py).
Discovery data only. Writes outputs/fashion/explore/audit/results_dehub.csv.
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.audit_common import AUD, est, nn_resid, pctl
from fashion.audit_tests import lincomb
from fashion.audit_vars import with_variants

warnings.filterwarnings("ignore")
ROWS = []


def run(h, test, d, y, rhs, terms, fe="year"):
    r = est(d, y, rhs, fe=fe, terms=terms)
    for k, (b, se, p, n) in r.items():
        ROWS.append(dict(h=h, test=test, term=k, b=b, se=se, p=p, n=n))
    print(f"{h:4s} {test:50s} " + "  ".join(f"{k}={b:+.3f}({se:.3f})" for k, (b, se, p, n) in r.items()) + f"  n={n}")


def main():
    f = with_variants()
    f["l_team_prev"] = np.log1p(f.team_prev_n)
    c = pd.read_parquet(AUD / "loc_dehub.parquet").drop(columns="year")
    f = f.merge(c, on="submission_id", how="left")
    Nall = pd.read_parquet(C.OUT / "fashion" / "frame2.parquet", columns=["year"]).year.value_counts().to_dict()
    N1 = f.year.map(lambda y: Nall[y - 1]).astype(float)
    N2 = f.year.map(lambda y: Nall[y - 2]).astype(float)
    f["loc1_c"] = 1000 * f.c1_c / N1
    f["locmom_c"] = np.log((f.c1_c + 1) / N1) - np.log((f.c2_c + 1) / N2)
    f["size_p_c"], f["mom_p_c"] = pctl(f, "loc1_c"), pctl(f, "locmom_c")
    f["nnres_c"] = nn_resid(f, "nn_c", "loc1_c")
    f["nnr_p_c"] = pctl(f, "nnres_c")
    print("corr raw vs centred percentiles:", {k: round(f[[k, k + "_c"]].corr().iloc[0, 1], 3) for k in ["size_p", "mom_p", "nnr_p"]})
    print("corr with hub_p:", {k: round(f[[k, "hub_p"]].corr().iloc[0, 1], 3) for k in ["size_p", "size_p_c", "mom_p", "mom_p_c", "nnr_p", "nnr_p_c"]})
    acc = f[(f.ACC == 1) & (f.year <= 2025) & f.top10.notna()]
    rev = f[f.acc_rev.notna()]
    Rc = "size_p_c + mom_p_c + nnr_p_c + log_authors"
    Tc = ["size_p_c", "mom_p_c", "nnr_p_c"]
    run("H1", "centred", acc, "top10", Rc, Tc)
    run("H1", "centred + hub_p", acc, "top10", Rc + " + hub_p", Tc)
    run("H1", "centred, outcome cite_pct", acc, "cite_pct", Rc, ["mom_p_c"])
    run("H1", "centred, 2019-23", acc[acc.year <= 2023], "top10", Rc, ["mom_p_c"])
    run("H1", "centred, topic50 FE", acc, "top10", Rc, ["mom_p_c"], fe="year + topic50")
    run("H23", "centred", rev, "acc_rev", Rc, Tc)
    run("H23", "centred + hub_p", rev, "acc_rev", Rc + " + hub_p", Tc + ["hub_p"])
    run("H23", "raw + hub_p (hub coefficient)", rev, "acc_rev", "size_p + mom_p + nnr_p + log_authors + hub_p", ["size_p", "hub_p"])
    run("H23", "centred, ACC vs REJ", rev, "acc_rej", Rc, Tc)
    run("H23", "centred, topic100 FE", rev, "acc_rev", Rc, Tc, fe="year + topic100")
    r22 = rev[rev.year >= 2022]
    run("H23", "centred 2022+", r22, "acc_rev", Rc, Tc)
    run("H23", "centred 2022+ + lprior_acc + ins + ent", r22, "acc_rev", Rc + " + lprior_acc + ins + ent", Tc)
    # nonlinearity of the raw size effect: deciles (ref = decile 1)
    rr = rev.copy()
    rr["sdec"] = np.ceil(rr.size_p * 10).clip(1, 10).astype(int)
    rr["hdec"] = np.ceil(rr.hub_p * 10).clip(1, 10).astype(int)
    run("H23", "raw size deciles (ref d1)", rr, "acc_rev", "C(sdec) + mom_p + nnr_p + log_authors", None)
    run("H23", "hub deciles (ref d1)", rr, "acc_rev", "C(hdec) + log_authors", None)
    h4 = f[(f.year.between(2022, 2025)) & f.hit.notna()]
    H4c = "ins*mom_p_c + ent*mom_p_c + size_p_c + nnr_p_c + log_authors + lprior_acc + mom_p_c:C(year)"
    b, se, n = lincomb(h4, "hit", H4c, "year", {"ins:mom_p_c": 1, "ent:mom_p_c": -1})
    ROWS.append(dict(h="H4", test="centred + mom x year: ins-ent slope", term="contrast", b=b, se=se, p=np.nan, n=n))
    print(f"H4   centred + mom x year: ins-ent slope = {b:+.3f} ({se:.3f})")
    b, se, n = lincomb(h4, "hit", H4c + " + l_team_prev*mom_p_c", "year", {"ins:mom_p_c": 1, "ent:mom_p_c": -1})
    ROWS.append(dict(h="H4", test="centred + mom x year + l_team_prev*mom: ins-ent", term="contrast", b=b, se=se, p=np.nan, n=n))
    print(f"H4   centred + mom x year + l_team_prev*mom: ins-ent slope = {b:+.3f} ({se:.3f})")
    h5 = f[(f.year >= 2022) & f.acc_rev.notna()]
    b, se, n = lincomb(h5, "acc_rev", "ins + ent + size_p_c + mom_p_c + nnr_p_c + log_authors + lprior_acc", "year", {"ins": 1, "ent": -1})
    ROWS.append(dict(h="H5", test="centred heat ctrls", term="ins-ent", b=b, se=se, p=np.nan, n=n))
    print(f"H5   centred heat ctrls: ins-ent = {b:+.3f} ({se:.3f})")
    b, se, n = lincomb(h5, "acc_rev", "ins + ent + size_p + mom_p + nnr_p + log_authors + lprior_acc + hub_p", "year", {"ins": 1, "ent": -1})
    ROWS.append(dict(h="H5", test="+ hub_p", term="ins-ent", b=b, se=se, p=np.nan, n=n))
    print(f"H5   + hub_p: ins-ent = {b:+.3f} ({se:.3f})")
    run("H6", "centred + mom x year", acc, "top10", "G1_name*mom_p_c + size_p_c + nnr_p_c + log_authors + mom_p_c:C(year)",
        ["G1_name:mom_p_c"])
    run("NNR", "centred acc", rev, "acc_rev", Rc, ["nnr_p_c"])
    run("NNR", "centred top10", acc, "top10", Rc, ["nnr_p_c"])
    pd.DataFrame(ROWS).to_csv(AUD / "results_dehub.csv", index=False)


if __name__ == "__main__":
    main()
