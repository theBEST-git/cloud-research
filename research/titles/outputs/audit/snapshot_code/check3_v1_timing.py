"""Audit check 3: v1 timing (posted before the ICLR submission deadline vs during review) differs by decision
and strongly predicts retitling, so the arms' noise floors differ. Compute timing-stratified net-flip DiDs on
the original and on the original + current enlargement pairs."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S

# approximate ICLR full-paper submission deadlines (public CFPs)
SUB = {2022: "2021-10-05", 2023: "2022-09-28", 2024: "2023-09-28", 2025: "2024-10-01", 2026: "2025-09-24"}
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
P = S.build_pairs(orig, U, "original")
enl = S.read_jsonl(S.ENLARGE_PATH)
enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
Pe = S.build_pairs(enl, U, "enlarge")
Pall = pd.concat([P, Pe], ignore_index=True)


def did_se(g, k):
    a, r = g[g.acc == 1], g[g.acc == 0]
    na, nr = (a[f"{k}_or"] - a[f"{k}_v1"]), (r[f"{k}_or"] - r[f"{k}_v1"])
    d = na.mean() - nr.mean()
    se = np.sqrt(na.var(ddof=1) / len(na) + nr.var(ddof=1) / len(nr))
    return d, se, len(a), len(r)


for name, Q in [("original", P), ("original+enlarge(all current)", Pall)]:
    Q = Q[Q.year >= 2023].copy()
    Q["sub"] = pd.to_datetime(Q.year.map(SUB))
    Q["during_review"] = pd.to_datetime(Q.v1_date) > Q["sub"]
    print(f"\n=== {name}: n={len(Q)}")
    ct = pd.crosstab(Q.decision, Q.during_review, normalize="index").round(3)
    print("share of pairs whose v1 was posted during review (after submission deadline):\n", ct)
    print("retitle rate by decision x timing:\n",
          Q.groupby(["during_review", "decision"]).changed_norm.agg(["mean", "size"]).round(3))
    rows = []
    for k in ["NAME", "NAME_loose", "compound", "title_case", "sentence_case", "via", "O_union"]:
        d_all, se_all, na, nr = did_se(Q, k)
        d_dr, se_dr, na2, nr2 = did_se(Q[Q.during_review], k)
        d_ps, se_ps, na3, nr3 = did_se(Q[~Q.during_review], k)
        # timing-standardised: within-stratum DiDs weighted by the accepted arm's timing shares
        wa = Q[Q.acc == 1].during_review.mean()
        d_std = wa * d_dr + (1 - wa) * d_ps
        se_std = np.sqrt((wa * se_dr) ** 2 + ((1 - wa) * se_ps) ** 2)
        rows.append(dict(feature=k, pooled=f"{100*d_all:+.2f} ({100*se_all:.2f}) n={na}/{nr}",
                         during_review=f"{100*d_dr:+.2f} ({100*se_dr:.2f}) n={na2}/{nr2}",
                         pre_submission=f"{100*d_ps:+.2f} ({100*se_ps:.2f}) n={na3}/{nr3}",
                         timing_std=f"{100*d_std:+.2f} ({100*se_std:.2f})"))
    print(pd.DataFrame(rows).to_string())
