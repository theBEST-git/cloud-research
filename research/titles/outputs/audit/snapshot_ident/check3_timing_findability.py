"""Audit check 3. (a) The net-flip DiD assumes v1-vs-OpenReview drift is the same in both arms. Test: v1 timing relative
to the submission deadline by arm, and the NAME DiD within timing strata (post-deadline v1 ~ the submitted version).
(b) V7a/SB4 alternative: both routes accept a hit only if the LATEST arXiv abstract resembles the stored abstract; rejected
papers are revised after rejection, so a decision-dependent share of on-arXiv papers may be censored by the matching rule.
Test: near-miss candidates (surname match, plausible date, Jaccard below the acceptance tiers) among unfound papers, and the
abstract-Jaccard density of found papers just above the 0.45 threshold. Read-only."""
from pathlib import Path
import json
import numpy as np, pandas as pd
from analyses import snapshot_bounds as S
from analyses import _core as CORE
OUT = Path(__file__).resolve().parent
U = CORE.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
enl = S.read_jsonl(S.ENLARGE_PATH); enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
P = pd.concat([S.build_pairs(orig, U, "original"), S.build_pairs(enl, U, "enlarge")], ignore_index=True)
# approximate ICLR full-paper submission deadlines
DL = {2022: "2021-10-05", 2023: "2022-09-28", 2024: "2023-09-28", 2025: "2024-10-01", 2026: "2025-09-24"}
P["lag_days"] = (pd.to_datetime(P.v1_date) - pd.to_datetime(P.year.map(DL))).dt.days
P["timing"] = pd.cut(P.lag_days, [-10000, -180, -1, 10000], labels=["v1 >6mo before deadline", "v1 0-6mo before", "v1 after deadline (in review)"])
print("v1 lag (days vs deadline) by arm:\n", P.groupby("decision").lag_days.describe().round(1))
print(pd.crosstab(P.decision, P.timing, normalize="index").round(3))
rows = []
for tm, g in P.groupby("timing", observed=True):
    a, r = g[g.acc == 1], g[g.acc == 0]
    def net(x, k): return 100 * (x[f"{k}_or"] - x[f"{k}_v1"]).mean()
    for k in ["NAME", "title_case", "sentence_case", "compound"]:
        rows.append(dict(timing=tm, feat=k, n_acc=len(a), n_rej=len(r), net_acc=net(a, k), net_rej=net(r, k), did=net(a, k) - net(r, k),
                         retitle_acc=100 * a.changed_norm.mean(), retitle_rej=100 * r.changed_norm.mean()))
T = pd.DataFrame(rows); pd.set_option("display.width", 250)
print(T.round(2).to_string())
# DiD on NAME in post-deadline stratum with pseudo-flip CI via flip_table
g = P[P.timing == "v1 after deadline (in review)"].reset_index(drop=True)
ft, _ = S.flip_table(g, ["NAME", "sentence_case", "title_case"], "post_deadline", Wb=np.ones((2, len(g))))
print(ft[["feature", "n_acc", "n_rej", "adds_acc", "drops_acc", "adds_rej", "drops_rej", "did", "did_lo", "did_hi"]].round(4).to_string())
T.to_csv(OUT / "check3_timing_strata.csv", index=False)

# (b) findability censoring
r = S.read_jsonl(S.ROUTE_PATH); r = r[r.error.isna()].drop_duplicates("submission_id", keep="last")
def near_miss(rec):
    best = 0.0
    for q in rec["queries"] or []:
        for c in q.get("cands") or []:
            if c.get("sn_ok") and c.get("tier") is None and c.get("pub") and \
               rec["year"] - 2 <= int(c["pub"][:4]) <= rec["year"] + 1:
                best = max(best, c.get("jac") or 0.0)
    return best
r["nm_best"] = [near_miss(x) for x in r.to_dict("records")]
r["unfound_both"] = ~r.found.astype(bool) & ~r.orig_found.astype(bool)
for thr in [0.05, 0.10, 0.15]:
    t = r[r.unfound_both].groupby("decision").apply(lambda d: pd.Series(dict(n_unfound=len(d), near_miss=int((d.nm_best >= thr).sum()))))
    t["share_of_all"] = t.near_miss / r.groupby("decision").size()
    print(f"near-miss candidates (surname match, date window, jac>={thr}, below tiers) among papers neither route found:\n", t)
# Jaccard density of accepted hits just above threshold (orig + enlarge title route, latest arXiv abstract vs stored)
A_ = pd.concat([orig, enl], ignore_index=True)
f = A_[A_.found.astype(bool)]
f["jbin"] = pd.cut(f.abstract_jaccard, [0, 0.45, 0.55, 0.65, 0.8, 1.01], right=False)
print("abstract Jaccard (latest arXiv vs stored) among found papers, by decision:\n",
      pd.crosstab(f.decision, f.jbin, normalize="index").round(3))
print("found papers whose latest arXiv title != stored:", f.assign(d=(f.latest_title.map(S.A.norm_title) != f.or_title.map(S.A.norm_title))).groupby("decision").d.mean().round(3).to_dict())
# is low-Jaccard (near threshold) associated with v1->stored NAME flips? (selection on the outcome dimension)
P2 = P.merge(A_[["submission_id", "abstract_jaccard"]].drop_duplicates("submission_id"), on="submission_id", how="left")
P2["lowj"] = P2.abstract_jaccard < 0.65
P2["flipNAME"] = (P2.NAME_or != P2.NAME_v1).astype(int)
print("NAME flip rate (any direction) and retitle rate by Jaccard band x decision:\n",
      P2.groupby(["decision", "lowj"]).agg(n=("flipNAME", "size"), flipNAME=("flipNAME", "mean"), retitle=("changed_norm", "mean")).round(3))
