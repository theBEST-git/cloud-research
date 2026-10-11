"""Audit D3/H3c: pre-LLM placebo. Same H3c logit (R24 ~ F24 + F26 + year FE + topic100 FE + log authors +
llm_topic + lnw) on 2018-23 and 2021-23, when neither fingerprint can reflect LLM vintage. If the F24/F26 ratio is
already > 1 pre-LLM, the H3c contrast reflects writer type (hype vs rigour vocabulary), not model generation."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_vintage as V

df = V.prep(D3.load_frame())
for lab, yrs in [("2018-23", range(2018, 2024)), ("2021-23", range(2021, 2024)), ("2025-26 (primary)", (2025, 2026)),
                 ("2025 only", (2025,)), ("2026 only", (2026,))]:
    d = df[df.year.isin(list(yrs))]
    ctrl = V.CTRL if len(list(yrs)) > 1 else V.CTRL.replace("C(year) + ", "")
    for y in ("r24_any",):
        r = V.fit(d, y, "f24", "f26", lab, ctrl=ctrl)
        print(f"{lab:18s} n={r['nobs']:6d} nY={r['n_y']:5d} nF24={r['n_xa']:5d} nF26={r['n_xb']:5d} "
              f"OR_F24 {r['OR_a']:.2f} [{r['OR_a_lo']:.2f},{r['OR_a_hi']:.2f}] OR_F26 {r['OR_b']:.2f} "
              f"[{r['OR_b_lo']:.2f},{r['OR_b_hi']:.2f}] ratio {r['ratio']:.2f} [{r['ratio_lo']:.2f},{r['ratio_hi']:.2f}]")
# F26 words only (no typography), pre-LLM
d = df[df.year.isin(range(2018, 2024))]
r = V.fit(d, "r24_any", "f24", "f26_words_i", "2018-23 words", extra_x=" + f26_typo_i")
print("2018-23 F26 words only:", round(r["OR_b"], 2), [round(r["OR_b_lo"], 2), round(r["OR_b_hi"], 2)], "ratio", round(r["ratio"], 2),
      [round(r["ratio_lo"], 2), round(r["ratio_hi"], 2)])
# 2025 F26 prevalence vs pre-LLM
print(df.groupby("year")[["f26_words_i", "f26_typo_i", "f26"]].mean().loc[2021:].round(4))
