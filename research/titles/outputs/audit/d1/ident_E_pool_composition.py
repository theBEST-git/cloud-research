"""Audit D1 / identification, check E: pool-mix composition in the H1a ITS. The NA pool mixes REJ/WD/DR whose
proportions move across years (2026: 737 desk rejections under a new desk regime vs 53 in 2025; withdrawals rise).
Refit the primary ITS (logit, topic100 FE, controls, cluster topic100) with pool fixed effects, and report NAME share by
pool x year. Also drop 2026 desk rejections and 2026 post-decision withdrawals.
"""
import json, sys, warnings
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C
from analyses import d1_its as I
warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary"], universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "NA", "pool", "DR", "wd_post"])
for c in ["name_primary", "llm_topic", "NA", "DR", "wd_post"]:
    df[c] = df[c].astype(int)
tab = df[df.year >= 2021].pivot_table(index="year", columns="pool", values="name_primary", aggfunc="mean").round(3)
cnt = df[df.year >= 2021].pivot_table(index="year", columns="pool", values="name_primary", aggfunc="size")
print(tab); print(cnt)
res = {"name_share_by_pool_year": tab.reset_index().to_dict(orient="records")}
def fit(d, lab, extra=""):
    d = I._design(d, 2024)
    f = "name_primary ~ tc + post + post_t + log_authors + llm_topic + C(topic100)" + extra
    r = C.logit(f, d, cluster="topic100")
    t = C.or_table(r, ["post_t"]).iloc[0]
    res[lab] = {"OR": float(t.OR), "lo": float(t.OR_lo), "hi": float(t.OR_hi), "n": int(r.nobs)}
    print(lab, res[lab], flush=True)
fit(df, "U primary (replication)")
fit(df, "U + pool FE", " + C(pool)")
na = df[df.NA == 1]
fit(na, "NA (replication)")
fit(na, "NA + pool FE", " + C(pool)")
fit(df[~((df.year == 2026) & ((df.DR == 1) | (df.wd_post == 1)))], "U minus 2026 DR and wd_post")
fit(df[df.pool.isin(["REJ"])], "REJ only")
(OUT / "ident_E_pool_composition.json").write_text(json.dumps(res, indent=1, default=float))
