"""Audit D2/S2.2: brute-force recomputation of past/future exposure sets and the clean flag for random focal rows."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
from analyses.d2_support import exposure_sets
papers, prof, _ = P.load_panel()
S = exposure_sets(prof)
AP = prof[["key","submission_id","year"]]
by_key = AP.groupby("key")
key_papers = {k: g for k, g in by_key}
pap_keys = AP.groupby("submission_id").key.apply(set).to_dict()
pap_year = AP.drop_duplicates("submission_id").set_index("submission_id").year.to_dict()
kidx, pidx = S["kidx"], S["pidx"]
past = S["past_set"].groupby(["k","T"]).p2.apply(set).to_dict()
fut = S["fut_set"].groupby(["k","T"]).p2.apply(set).to_dict()
rows = S["rows"]
rng = np.random.default_rng(0)
cand = rows[rows["T"].between(2023, 2025)]
samp = cand.iloc[rng.choice(len(cand), 400, replace=False)]
bad = {"past": 0, "fut": 0, "clean": 0}
for _, r in samp.iterrows():
    k = kidx[r.k]; T = int(r["T"]); p = pidx[r.p]
    kp = key_papers[k]
    # collaborators by year
    def collabs(year):
        s = set()
        for q in kp.submission_id[kp.year == year]:
            s |= pap_keys[q]
        s.discard(k); return s
    own = set(kp.submission_id)
    cprev = collabs(T - 1)
    past_bf = set()
    for c in cprev:
        g = key_papers[c]; past_bf |= set(g.submission_id[g.year == T - 1]) - own
    # future: first co-authorship with k in T+1
    cnext = collabs(T + 1)
    earlier = set()
    for yy in range(2021, T + 1):
        earlier |= collabs(yy)
    fnew = cnext - earlier
    fut_bf = set()
    for c in fnew:
        g = key_papers[c]; fut_bf |= set(g.submission_id[g.year == T - 1]) - own
    cl_bf = len((pap_keys[p] - {k}) & cprev) == 0
    pc = {pidx[i] for i in past.get((r.k, T), set())}; fc = {pidx[i] for i in fut.get((r.k, T), set())}
    bad["past"] += pc != past_bf; bad["fut"] += fc != fut_bf; bad["clean"] += bool(r.clean) != cl_bf
print("mismatches in 400 sampled focal rows:", bad)
