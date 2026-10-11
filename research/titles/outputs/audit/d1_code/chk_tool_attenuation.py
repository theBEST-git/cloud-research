"""Audit D1-H1e: the 'maximum tool share' = delta * A / dNAME uses delta = E[NAME|F=1]-E[NAME|F=0] as if it were the
NAME uplift of LLM-drafted papers. With imperfect recall (and a 2.5% pre-LLM false-positive rate), F=0 contains
undrafted AND undetected drafted papers, so delta = tau * (P(L|F=1) - P(L|F=0)) < tau.  Correct the bound."""
import json
import numpy as np
dc = json.load(open("/home/user/cloud-research/research/titles/outputs/d1_break/decompose.json"))
t = dc["tool"]; d = t["delta_primary"]; dname = t["dNAME_2023_2026"]
f = t["detectable_only_contribution"]["share_F_2023"]; pF = t["detectable_only_contribution"]["share_F_2026"]
import pandas as pd
D = pd.read_csv("/home/user/cloud-research/research/titles/outputs/d1_break/tool_delta_models.csv")
d26 = D[D.spec == "F_d1, 2026 only"].iloc[0]
rows = []
for A in (0.24, 0.39, 0.5, 0.75, 0.9, 1.0):
    r = (pF - f * (1 - A)) / A           # implied recall of F among drafted papers in 2026
    ppv = A * r / pF                      # P(L=1 | F=1)
    npv_c = A * (1 - r) / (1 - pF)        # P(L=1 | F=0)
    k = ppv - npv_c
    for lab, dl, lo, hi in [("pooled 2024-26", d["delta"], d["lo"], d["hi"]), ("2026 only", d26.delta, d26.lo, d26.hi)]:
        rows.append(dict(A=A, delta_spec=lab, recall=r, P_L_given_F1=ppv, P_L_given_F0=npv_c, attenuation=k,
                         pipeline_share=dl * A / dname, pipeline_share_hi=hi * A / dname,
                         corrected_share=(dl / k * A / dname) if k > 0 else np.nan,
                         corrected_share_hi=(hi / k * A / dname) if k > 0 else np.nan))
R = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(R.round(4).to_string())
R.to_csv("/home/user/cloud-research/research/titles/outputs/audit/d1_code/tool_attenuation.csv", index=False)
