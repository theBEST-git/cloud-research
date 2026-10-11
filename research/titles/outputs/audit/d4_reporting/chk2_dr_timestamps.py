"""Reporting audit D4: 2026 desk-rejection timestamps (RESULTS claims 712 on 2026-02-12) and post-decision WD n."""
import pandas as pd
from analyses import _core as C
from common import read_table
u = C.load_universe(["submission_id","year","DR","WD","decision","wd_post"])
m = read_table("metadata_provenance")[["submission_id","modification_ms"]]
t = u[u.year.isin([2025,2026])].merge(m, on="submission_id", how="left")
t["mod"] = pd.to_datetime(t.modification_ms, unit="ms", errors="coerce")
dr = t[(t.year==2026)&(t.DR==1)]
print("2026 DR n", len(dr)); print(dr["mod"].dt.normalize().value_counts().head(5))
w = t[(t.year==2026)&(t.WD==1)]
post = w[w["mod"]>=pd.Timestamp("2026-01-26")]
print("2026 WD mod>=decision", len(post), "of which wd_post", int(post.wd_post.sum()), "; wd_post total", int(w.wd_post.sum()))
print(post.decision.value_counts())
