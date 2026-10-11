import pandas as pd, numpy as np
from analyses import _core as C
u = C.load_universe(["submission_id","year","pool","decision","administrative_status","ACC","REJ","WD","DR","wd_post","wd_decided","inconsistent","stage_s1","stage_s2","stage_s3"])
print(pd.crosstab(u.year, [u.WD, u.decision]).to_string())
print(pd.crosstab(u.year, u.pool))
print("WD & decision rejected by year:", u[u.WD & u.decision.eq("rejected")].groupby("year").size().to_dict())
print("WD & decision accepted by year:", u[u.WD & u.decision.eq("accepted")].groupby("year").size().to_dict())
print("DR & decision by year:", pd.crosstab(u[u.DR].year, u[u.DR].decision).to_string())
