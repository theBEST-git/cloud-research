"""Audit D3/H3a: event-study sensitivity to study_adj (6 pre titles) and convergence of the logits."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3

inv = D3.frozen_inventory()
df = D3.load_frame()
P = D3.slot_panel(df, inv)
print(P[(P.slot == "study_adj") & (P.year <= 2023)][["year", "y", "word"]].sort_values("year").to_string())
for lab, PP in [("all", P), ("no study_adj", P[P.slot != "study_adj"])]:
    es = D3.event_study(PP)
    print(lab); print(es[es.model.isin(["slots", "slot_minus_control"])].round(3).to_string())
# convergence of primary
r = C.logit(D3.POOLED, P[P.llm_slot == 1], cluster="topic100")
print("primary converged:", r.mle_retvals.get("converged"), "method", r.mle_settings.get("optimizer"))
print(r.params.round(3).to_string())
