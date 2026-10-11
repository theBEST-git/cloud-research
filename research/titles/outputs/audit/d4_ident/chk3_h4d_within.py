"""D4 identification audit, check 3 (H4d): is the NAME withdrawal excess 'between authors' or 'between topics',
and is the within-key null an artefact of the multi-paper-key sample or cross-year comparisons?
Variants of the D4 contrast (LPM, key-clustered):
  A  reproduction (year FE vs year + key FE), multi-paper keys
  B  topic100 FE added to both (as in D4 robustness)
  C  within key x year (same review cycle, same last-position key) vs cross-section with year FE on that sample
  D  cross-section with/without topic100 FE on the FULL sample and on single-paper keys only (who carries the excess?)
  E  measurement-error bound: share of NAME variance that is within key (detector accuracy ~0.985)
"""
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C  # noqa: E402
from analyses import d4_stage_gains as S  # noqa: E402
from analyses import d4_exit_composition as E  # noqa: E402

df = S.load_frame(min_year=2018, density=False)
lk = E.last_keys(set(df.submission_id))
df = df.merge(lk, on="submission_id", how="left", validate="1:1")
df["wd"] = df.WD.astype(int)
ctr = ["log_authors", "llm_topic"]
base = df[((df.REJ == 1) | (df.WD == 1)) & df.year.isin(S.POST)].copy()
base = base[base.key_last.notna()].copy()
base["n_key"] = base.groupby("key_last").key_last.transform("size")
base["f_"] = base.name_primary.astype(float)
base["key_year"] = base.key_last + "|" + base.year.astype(str)
base["n_ky"] = base.groupby("key_year").key_year.transform("size")


def fit(d, fe, label, cl="key_last"):
    r = C.feols(d, "wd", ["f_"] + ctr, fe=fe, cluster=cl)
    b, se = 100 * r.params["f_"], 100 * r.se["f_"]
    print(f"{label:70s} n={int(r.nobs):6d} b={b:+6.2f} se={se:5.2f}  [{b - 1.96 * se:+6.2f},{b + 1.96 * se:+6.2f}]")
    return b, se


multi = base[base.n_key >= 2]
print("A reproduction")
fit(multi, ["year"], "cross, year FE, multi-paper keys")
fit(multi, ["year", "key_last"], "within key, multi-paper keys")
print("B topic100 FE")
fit(multi, ["year", "topic100"], "cross, year+topic FE, multi-paper keys")
fit(multi, ["year", "key_last", "topic100"], "within key + topic FE, multi-paper keys")
print("C same-cycle within key x year")
ky = base[base.n_ky >= 2]
fit(ky, ["year"], "cross, year FE, key-years with >=2 papers")
fit(ky, ["year", "topic100"], "cross, year+topic FE, key-years with >=2 papers")
fit(ky, ["key_year"], "within key x year")
fit(ky, ["key_year", "topic100"], "within key x year + topic FE")
print("D who carries the cross-sectional excess")
full = df[((df.REJ == 1) | (df.WD == 1)) & df.year.isin(S.POST)].copy()
full["f_"] = full.name_primary.astype(float)
fit(full, ["year"], "cross, year FE, full", cl="topic100")
fit(full, ["year", "topic100"], "cross, year+topic FE, full", cl="topic100")
single = base[base.n_key == 1]
fit(single, ["year"], "cross, year FE, single-paper keys", cl="topic100")
fit(single, ["year", "topic100"], "cross, year+topic FE, single-paper keys", cl="topic100")
fit(multi, ["year", "topic100"], "cross, year+topic FE, multi-paper keys (topic-cl)", cl="topic100")
print("E within-key share of NAME variance (multi-paper keys)")
v_tot = multi.f_.var()
v_within = (multi.f_ - multi.groupby("key_last").f_.transform("mean")).pow(2).sum() / (len(multi) - 1)
err = 0.015 * 0.985  # variance of a ~1.5% misclassification noise term (V1 accuracy 0.985)
print(f"var total {v_tot:.4f}, within {v_within:.4f} ({v_within / v_tot:.2%}); "
      f"implied attenuation within ~{1 - err / v_within:.3f}, cross ~{1 - err / v_tot:.3f}")
print("withdrawal rate by NAME x topic-withdrawal tercile (full sample):")
full["topic_wd"] = full.groupby("topic100").wd.transform("mean") if "wd" in full else np.nan
full["wd"] = full.WD.astype(int)
full["topic_wd"] = full.groupby("topic100").wd.transform("mean")
full["topic_name"] = full.groupby("topic100").f_.transform("mean")
print("corr(topic NAME share, topic withdrawal rate) across topic100 (paper-weighted):",
      round(np.corrcoef(full.topic_name, full.topic_wd)[0, 1], 3))
tt = full.groupby("topic100").agg(n=("wd", "size"), wd=("wd", "mean"), name=("f_", "mean"), llm=("llm_topic", "mean"))
print("topic-level (unweighted) corr name~wd:", round(tt[["name", "wd"]].corr().iloc[0, 1], 3),
      " name~llm:", round(tt[["name", "llm"]].corr().iloc[0, 1], 3), " wd~llm:", round(tt[["wd", "llm"]].corr().iloc[0, 1], 3))
