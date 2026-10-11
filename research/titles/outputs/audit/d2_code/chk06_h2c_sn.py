"""Audit D2/H2c: composition of share_new = 0 rows among stayer rows (solo-key vs all-prior co-authors), by year;
and H2c contrast re-estimated excluding solo-key rows."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys, groups_coded
papers, prof, _ = P.load_panel()
prof, idx = code_keys(prof)
g = groups_coded(prof, P.E_WIN, P.L_WIN, idx)
st = set(g.index[g.S])
r = prof[prof.key_code.isin(st) & prof.year.between(2022, 2026)].merge(
    papers[["submission_id","name_primary","log_authors","llm_topic","topic100","declared_name_count"]], on="submission_id")
r["solo"] = r.n_pkeys.eq(1)
r["sn0"] = r.share_new_coauth_roll.eq(0)
print(r.groupby("year").agg(rows=("key","size"), solo=("solo","mean"), sn0=("sn0","mean"), sn_mean=("share_new_coauth_roll","mean"),
      sn_lag1=("share_new_coauth_lag1","mean"), single_author=("declared_name_count", lambda s: (s==1).mean())).round(3))
print("share of sn=0 rows that are solo-key, E vs L:", r[r.sn0 & r.year.isin(P.E_WIN)].solo.mean(), r[r.sn0 & r.year.isin(P.L_WIN)].solo.mean())
def fit(d, lab):
    d = d.assign(post=(d.year>=2024).astype(int), sn=d.share_new_coauth_roll, llm_topic=d.llm_topic.astype(float))
    d["post_sn"] = d.post*d.sn
    for y in [2023,2024,2025,2026]: d[f"y{y}"] = (d.year==y).astype(int)
    res = C.feols(d, "name_primary", ["y2023","y2024","y2025","y2026","sn","post_sn","log_authors","llm_topic"], fe=["key_code","topic100"], cluster="key_code")
    c = pd.Series(0.0, index=res.params.index); c[["y2025","y2026"]] = .5; c["y2023"] = -.5
    est = c @ res.params; se = np.sqrt(c @ res.vcov @ c)
    print(lab, "n", res.nobs, "change@sn0 %.4f se %.4f ratio %.3f" % (est, se, est/0.182559), "post_sn %.4f" % res.params["post_sn"])
fit(r, "primary (reproduce)")
fit(r[~r.solo], "excluding solo-key rows")
# two-way clustering check: key and paper (CGM) for primary
