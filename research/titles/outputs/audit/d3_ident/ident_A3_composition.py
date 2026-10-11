"""D3 audit A3: submitter-composition alternative for H3a. 2022-2025 slot panel, post = 2024+; pooled slot logit
(slot FE + post + llm_topic) within incumbent-only teams (share_new_authors == 0) vs teams with new keys; and with
share_new_authors + lmax_prior_subs controls. Keys are declared profile keys, not persons."""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
OUT = C.OUT / "audit" / "d3_ident"
df = D3.load_frame()
u = C.load_universe(["submission_id", "share_new_authors", "lmax_prior_subs", "exp_valid"])
inv = json.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
P = D3.slot_panel(df, inv, controls=True, years_from=2022).merge(u, on="submission_id")
P = P[P.year <= 2025]
res = {}
for lab, m in [("all", P.year > 0), ("incumbent_only_teams", P.share_new_authors == 0), ("any_new_key", P.share_new_authors > 0),
               ("majority_new", P.share_new_authors >= 0.5)]:
    d = P[m]
    out = {}
    for nm, dd, f, term in [("slots", d[d.llm_slot == 1], "y ~ C(slot) + post + llm_topic", "post"),
                            ("stacked", d, "y ~ C(slot) + post + post:llm_slot + llm_topic", "post:llm_slot")]:
        r = C.logit(f, dd, cluster="topic100"); t = C.or_table(r, [term]).iloc[0]
        out[nm] = [round(float(t.OR), 3), round(float(t.OR_lo), 3), round(float(t.OR_hi), 3), int(r.nobs)]
    out["share_pre_post"] = [float(d[(d.llm_slot == 1) & (d.post == 0)].y.mean()), float(d[(d.llm_slot == 1) & (d.post == 1)].y.mean())]
    res[lab] = out
    print(lab, out)
d = P[P.llm_slot == 1]
r = C.logit("y ~ C(slot) + post + llm_topic + share_new_authors + lmax_prior_subs", d, cluster="topic100")
t = C.or_table(r, ["post"]).iloc[0]
res["slots_with_experience_controls"] = [float(t.OR), float(t.OR_lo), float(t.OR_hi)]
print("with controls", res["slots_with_experience_controls"])
json.dump(res, open(OUT / "ident_A3_composition.json", "w"), indent=1)
