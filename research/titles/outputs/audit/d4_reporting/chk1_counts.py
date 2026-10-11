"""Reporting audit D4: verify counts behind RESULTS.md claims (wd variant no-op, 2026 desk timestamps, post-decision n)."""
import pandas as pd, numpy as np
from analyses import _core as C
u = C.load_universe(["submission_id","year","administrative_status","decision","WD","DR","ACC","REJ","wd_post","pool","stage_s1","stage_s2","stage_s3"])
u = u[u.year>=2018]
print("WD x decision by year")
print(pd.crosstab(u[u.WD.astype(bool)].year, u[u.WD.astype(bool)].decision))
print("wd_post by year", u.groupby("year").wd_post.sum().to_dict())
print("pool OTHER by year", u[u.pool.eq("OTHER")].groupby("year").size().to_dict())
# stage sizes
print(u[u.pool.ne("OTHER")].groupby("year")[["stage_s1","stage_s2","stage_s3"]].sum())
print("s0", u[u.pool.ne("OTHER")].groupby("year").size().to_dict())
