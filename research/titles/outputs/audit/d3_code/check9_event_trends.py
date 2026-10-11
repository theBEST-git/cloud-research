"""Audit D3/H3a event study: are slot trends 'fitted on 2018-22' (docstring) or also informed by 2023-26?
Compare slot-trend coefficients from the event-study model with a fit on 2018-22 only, and compute year deviations
with trends truly frozen on 2018-22 (offset approach)."""
import numpy as np, pandas as pd
from analyses import _core as CORE
from analyses import d3_slots as D3
inv = D3.frozen_inventory()
df = D3.load_frame()
P = D3.slot_panel(df, inv)
S = P[(P.llm_slot == 1) & (P.slot != "study_adj")].copy()
for y in (2023, 2024, 2025, 2026):
    S[f"d{y}"] = (S.year == y).astype(int)
es = CORE.logit("y ~ C(slot) + C(slot):t + d2023 + d2024 + d2025 + d2026 + llm_topic", S, cluster="topic100")
pre = CORE.logit("y ~ C(slot) + C(slot):t + llm_topic", S[S.year <= 2022], cluster="topic100")
tr = [k for k in es.params.index if ":t" in k]
print(pd.DataFrame({"event_study": es.params[tr], "fit_2018_22_only": pre.params[tr]}).round(3))
# frozen-trend deviations: offset = prediction from the 2018-22 fit; then logit y ~ year dummies with offset
import statsmodels.api as sm, patsy
X = patsy.dmatrix("C(slot) + C(slot):t + llm_topic", S, return_type="dataframe")
off = X[pre.params.index].to_numpy() @ pre.params.to_numpy()
D = S[["d2023", "d2024", "d2025", "d2026"]].astype(float)
m = sm.GLM(S.y.astype(float), D, family=sm.families.Binomial(), offset=off).fit(
    cov_type="cluster", cov_kwds={"groups": pd.factorize(S.topic100)[0]})
print("frozen-trend year ORs (opener slots):", np.exp(m.params).round(2).to_dict())
print("event-study year ORs (opener slots):", np.exp(es.params[["d2023", "d2024", "d2025", "d2026"]]).round(2).to_dict())
