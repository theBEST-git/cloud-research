import numpy as np, pandas as pd
from analyses import d4_stage_gains as S
from analyses import d4_exit_composition as E
df = S.load_frame(min_year=2018, density=False)
df = df.merge(E.last_keys(set(df.submission_id)), on="submission_id", how="left", validate="1:1")
df["wd"] = df.WD.astype(int)
d = df[((df.REJ == 1) | (df.WD == 1)) & df.year.isin(S.POST) & df.key_last.notna()].copy()
n = d.groupby("key_last").size()
print("papers per key (pop):", n.describe().round(2).to_dict(), "keys>=20:", int((n >= 20).sum()), "papers in them:", int(n[n >= 20].sum()))
for cap in [None, 30, 15, 8]:
    dd = d if cap is None else d[d.key_last.map(n) <= cap]
    r = E.contrast(dd, "name_primary", "key_last", ["log_authors", "llm_topic"])
    print(cap, r["nobs"], round(r["cross_pp"], 2), round(r["within_pp"], 2), round(r["within_se_pp"], 2), round(r["diff_pp"], 2))
# key + year FE (key-year) as check: within key-year
d["key_year"] = d.key_last + "|" + d.year.astype(str)
r = E.contrast(d, "name_primary", "key_year", ["log_authors", "llm_topic"])
print("key-year FE:", r["nobs"], round(r["cross_pp"], 2), round(r["within_pp"], 2), round(r["within_se_pp"], 2))
