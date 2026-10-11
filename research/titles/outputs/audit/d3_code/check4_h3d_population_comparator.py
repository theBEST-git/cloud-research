"""Audit D3/H3d: ratio OR_slot / OR_NAME with the population NAME comparator (all 2024-26 papers, same FE, no
log authors to match the slot LPM), joint topic100-cluster bootstrap (same draws for both outcomes)."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_signature_bound as SB

inv = D3.frozen_inventory()
df = D3.load_frame()
P = D3.slot_panel(df, inv, controls=False)
S = P[P.year >= 2024].copy().reset_index(drop=True)
A = df[df.year >= 2024][["submission_id", "topic100", "year", "name_primary", "F_any"]].reset_index(drop=True)
S["ty"] = C.fe_interact(S.topic100, S.year); A["ty"] = C.fe_interact(A.topic100, A.year)
bs_ = C.feols(S, "y", ["F_any"], fe=["slot", "ty"]).params["F_any"]
bn_ = C.feols(A, "name_primary", ["F_any"], fe=["ty"]).params["F_any"]
p0s, p0n = S.loc[S.F_any == 0, "y"].mean(), A.loc[A.F_any == 0, "name_primary"].mean()
ors, orn = SB.implied_or(p0s, bs_), SB.implied_or(p0n, bn_)
print(f"point: OR_slot {ors:.3f} OR_name_pop {orn:.3f} ratio {ors/orn:.3f}")
rng = np.random.default_rng(1)
topics = np.union1d(S.topic100.unique(), A.topic100.unique())
S_ix = {t: np.flatnonzero(S.topic100.to_numpy() == t) for t in topics}
A_ix = {t: np.flatnonzero(A.topic100.to_numpy() == t) for t in topics}
out = []
for b in range(500):
    draw = rng.choice(topics, len(topics), replace=True)
    si = np.concatenate([S_ix[t] for t in draw]); ai = np.concatenate([A_ix[t] for t in draw])
    Sb = S.iloc[si][["y", "F_any", "slot", "year"]].reset_index(drop=True)
    Ab = A.iloc[ai][["name_primary", "F_any", "year"]].reset_index(drop=True)
    Sb["ty"] = np.repeat(np.arange(len(draw)), [len(S_ix[t]) for t in draw]) * 10000 + Sb.year.to_numpy()
    Ab["ty"] = np.repeat(np.arange(len(draw)), [len(A_ix[t]) for t in draw]) * 10000 + Ab.year.to_numpy()
    o_s = SB.implied_or(Sb.loc[Sb.F_any == 0, "y"].mean(), C.feols(Sb, "y", ["F_any"], fe=["slot", "ty"]).params["F_any"])
    o_n = SB.implied_or(Ab.loc[Ab.F_any == 0, "name_primary"].mean(),
                        C.feols(Ab, "name_primary", ["F_any"], fe=["ty"]).params["F_any"])
    out.append((o_s, o_n, o_s / o_n))
out = np.array(out)
print("CI OR_slot", np.quantile(out[:, 0], [.025, .975]).round(3), "OR_name_pop", np.quantile(out[:, 1], [.025, .975]).round(3),
      "ratio", np.quantile(out[:, 2], [.025, .975]).round(3), "P(ratio<=1)", (out[:, 2] <= 1).mean(),
      "P(ratio>=1.5)", (out[:, 2] >= 1.5).mean())
