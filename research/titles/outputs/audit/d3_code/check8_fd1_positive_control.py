"""Audit D3->D1 link: H3d slot effect with D1's fingerprint F_d1 (F24>=2 | F26 | title typography), the F that
D1-H1e actually bounds, vs F_any used in D3."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_signature_bound as SB
inv = D3.frozen_inventory()
df = D3.load_frame()
df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
P = D3.slot_panel(df, inv, controls=False).merge(df[["submission_id", "F_d1"]], on="submission_id")
S = P[P.year >= 2024].copy(); S["ty"] = C.fe_interact(S.topic100, S.year)
A = df[df.year >= 2024].copy(); A["ty"] = C.fe_interact(A.topic100, A.year)
for F in ["F_any", "F_d1"]:
    rs = C.feols(S, "y", [F], fe=["slot", "ty"], cluster="topic100")
    rn = C.feols(A, "name_primary", [F], fe=["ty"], cluster="topic100")
    p0s, p0n = S.loc[S[F] == 0, "y"].mean(), A.loc[A[F] == 0, "name_primary"].mean()
    print(F, "nF1 slot", int(S[F].sum()), "slot pp", round(100 * rs.params[F], 2), "+-", round(196 * rs.se[F], 2),
          "OR", round(SB.implied_or(p0s, rs.params[F]), 3), "| pop NAME pp", round(100 * rn.params[F], 2), "+-",
          round(196 * rn.se[F], 2), "OR", round(SB.implied_or(p0n, rn.params[F]), 3))
