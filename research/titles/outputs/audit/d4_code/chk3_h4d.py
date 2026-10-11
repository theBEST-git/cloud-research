import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d4_stage_gains as S
from analyses import d4_exit_composition as E
df = S.load_frame(min_year=2018, density=False)
lk = E.last_keys(set(df.submission_id))
df = df.merge(lk, on="submission_id", how="left", validate="1:1")
df["wd"] = df.WD.astype(int)
ctr = ["log_authors", "llm_topic"]
base = df[((df.REJ == 1) | (df.WD == 1)) & df.year.isin(S.POST)].copy()
post_dec = (base.WD == 1) & base.decision.isin(["rejected", "accepted"])
print("post-decision withdrawals in pop by year:", base[post_dec].groupby("year").size().to_dict())
def show(lbl, d):
    r = E.contrast(d, "name_primary", "key_last", ctr)
    print(f"{lbl:45s} n={r['nobs']:6d} cross {r['cross_pp']:+.2f} ({r['cross_se_pp']:.2f}) within {r['within_pp']:+.2f} ({r['within_se_pp']:.2f}) diff {r['diff_pp']:.2f} ({r['diff_se_pp']:.2f})")
show("primary (reproduce)", base)
d = base.copy(); d["wd"] = (d.wd * (1 - post_dec.astype(int))).astype(int)
show("all decided withdrawals counted as rejected", d)
show("all decided withdrawals dropped", base[~post_dec])
show("only pre-decision WD vs REJ, 2024-25", base[~post_dec & base.year.isin([2024, 2025])])
show("2026 only", base[base.year.eq(2026)])
show("2024-25 only", base[base.year.isin([2024, 2025])])
