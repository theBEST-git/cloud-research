"""Audit D3/H3d: is the 'same papers' NAME comparator collider-conditioned? P(slot filled) by NAME x F, 2024-26,
and the NAME LPM within topic100 x year on all papers vs slot-filled papers."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_signature_bound as SB

inv = D3.frozen_inventory()
df = D3.load_frame()
P = D3.slot_panel(df, inv, controls=False)
filled_ids = set(P.submission_id)
d = df[df.year >= 2024].copy()
d["filled"] = d.submission_id.isin(filled_ids).astype(int)
print(d.groupby(["name_primary", "F_any"]).filled.agg(["mean", "size"]))
d["ty"] = C.fe_interact(d.topic100, d.year)
r = C.feols(d, "filled", ["F_any", "name_primary"], fe=["ty"], cluster="topic100")
print("P(filled) ~ F + NAME within ty:", r.params.round(4).to_dict(), r.se.round(4).to_dict())
r2 = C.feols(d.assign(FxN=d.F_any * d.name_primary), "filled", ["F_any", "name_primary", "FxN"], fe=["ty"], cluster="topic100")
print("with interaction:", r2.params.round(4).to_dict())
# NAME ~ F on all vs filled
for lab, dd in [("all", d), ("filled", d[d.filled == 1]), ("not filled", d[d.filled == 0])]:
    rr = C.feols(dd, "name_primary", ["F_any"], fe=["ty"], cluster="topic100")
    print(lab, "NAME~F pp", round(100 * rr.params["F_any"], 2), "se", round(100 * rr.se["F_any"], 2), "n", rr.nobs)
# gerund opener (any) among F
d["gerund_any"] = 0
