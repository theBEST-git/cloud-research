"""Audit D2/H2c: two-way (key, paper) CGM clustered SE for the change at share_new = 0 vs key-only clustering."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_shiftshare import code_keys, groups_coded
papers, prof, _ = P.load_panel()
prof, idx = code_keys(prof)
g = groups_coded(prof, P.E_WIN, P.L_WIN, idx)
r = prof[prof.key_code.isin(set(g.index[g.S])) & prof.year.between(2022, 2026)].merge(
    papers[["submission_id","name_primary","log_authors","llm_topic","topic100"]], on="submission_id")
r = r.assign(post=(r.year>=2024).astype(int), sn=r.share_new_coauth_roll, llm_topic=r.llm_topic.astype(float))
r["post_sn"] = r.post*r.sn
for y in [2023,2024,2025,2026]: r[f"y{y}"] = (r.year==y).astype(int)
r["pid"] = pd.factorize(r.submission_id)[0]; r["rowid"] = np.arange(len(r))
x = ["y2023","y2024","y2025","y2026","sn","post_sn","log_authors","llm_topic"]
V = {}
for cl in ["key_code","pid","rowid"]:
    res = C.feols(r, "name_primary", x, fe=["key_code","topic100"], cluster=cl)
    V[cl] = res.vcov; b = res.params
c = pd.Series(0.0, index=b.index); c[["y2025","y2026"]] = .5; c["y2023"] = -.5
se = {k: float(np.sqrt(c @ v @ c)) for k, v in V.items()}
se["cgm"] = float(np.sqrt(c @ (V["key_code"] + V["pid"] - V["rowid"]) @ c))
print("est", float(c @ b), se)
