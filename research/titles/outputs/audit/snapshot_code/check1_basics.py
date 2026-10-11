"""Audit checks 1: feature reproduction, merges, year composition, year-stratified DiD, outcome_eligible."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S
from common import load_submissions

U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ", "pool"])
orig = S.read_jsonl(S.ORIG_PATH)
print("orig records", len(orig))
# (3) audit records not in U
notU = ~orig.submission_id.isin(U.submission_id)
print("orig not in U:", int(notU.sum()), orig[notU][["submission_id", "year", "decision", "found"]].to_dict("records"))
# (4) audit decision vs universe pool
m = orig.merge(U[["submission_id", "pool"]], on="submission_id", how="left")
print("audit decision x universe pool\n", pd.crosstab(m.decision, m.pool.fillna("notU")))
s = load_submissions()
s = s[s.year.isin([2022, 2023, 2024, 2025, 2026]) & s.administrative_status.eq("ordinary_submission")
      & s.decision.isin(["accepted", "rejected"])]
print("ordinary acc/rej with outcome_eligible != 1:", int((s.outcome_eligible != 1).sum()))

P = S.build_pairs(orig, U, "original")
print("pairs", len(P))
print(pd.crosstab(P.year, P.decision))
# (1) stored-title feature reproduction
fv = C.load_features()
keys = [(k, c) for k, _, _, c in S.TITLE_FEATS]
fvd = S.derive(C.load_analysis_frame())
fvd = fvd.set_index("submission_id")
bad = {}
for k, c in keys:
    a = P[f"{k}_or"].to_numpy()
    b = fvd.loc[P.submission_id, c].astype(int).to_numpy()
    if (a != b).any():
        bad[k] = int((a != b).sum())
print("stored-title feature mismatches vs features_v2:", bad)

# (2) year-stratified DiD vs pooled
def net(g, k):
    return (g[f"{k}_or"] - g[f"{k}_v1"]).mean()

rows = []
for k in ["NAME", "compound", "title_case", "mixed_case_name", "O_union", "via", "phrase_colon", "NAME_loose"]:
    pooled = net(P[P.acc == 1], k) - net(P[P.acc == 0], k)
    # within-year DiD, weighted by number of pairs in the year (2023-26 only; 2022 has no rejected arm)
    ys, ds, ws, wpost = [], [], [], []
    for y in [2023, 2024, 2025, 2026]:
        g = P[P.year == y]
        d = net(g[g.acc == 1], k) - net(g[g.acc == 0], k)
        ys.append(y); ds.append(d); ws.append(len(g))
    ds, ws = np.array(ds), np.array(ws, float)
    strat = (ds * ws).sum() / ws.sum()
    strat_post = (ds[1:] * ws[1:]).sum() / ws[1:].sum()
    excl22 = P[P.year >= 2023]
    pooled23 = net(excl22[excl22.acc == 1], k) - net(excl22[excl22.acc == 0], k)
    rows.append(dict(feature=k, pooled_primary_pp=100 * pooled, pooled_excl2022_pp=100 * pooled23,
                     year_strat_2023_26_pp=100 * strat, year_strat_2024_26_pp=100 * strat_post,
                     by_year_pp=dict(zip(ys, np.round(100 * ds, 2)))))
print(pd.DataFrame(rows).to_string())
# net flip by year x decision for NAME
print(P.assign(net=P.NAME_or - P.NAME_v1).groupby(["year", "decision"]).net.agg(["mean", "size", "sum"]))
