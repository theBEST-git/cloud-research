"""D3 audit C2: meaning-fixed H3c (R24 | title has R24 or neutral counterpart; slot-variant logit) in the NA pool and
by year; plus H3b-style within-slot 2026 vs 2025 LLM share in the NA pool."""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_vintage as V
OUT = C.OUT / "audit" / "d3_ident"
df = V.prep(D3.load_frame())
tl = df.title_nfkc.fillna("").str.lower()
df["n24"] = C.rx_contains(tl, r"\b(improv\w*|utili[sz]\w*|exploit\w*)").astype(int)
df["r24_or_n24"] = ((df.r24_any == 1) | (df.n24 == 1)).astype(int)
res = {}
for lab, m in [("NA 2025-26", df.year.isin([2025, 2026]) & (df.NA == 1)), ("2025", df.year == 2025), ("2026", df.year == 2026),
               ("non-LLM 2025-26", df.year.isin([2025, 2026]) & (df.non_llm == 1))]:
    sub = df[m & (df.r24_or_n24 == 1)]
    ctrl = V.CTRL if "-" in lab else V.CTRL.replace("C(year) + ", "")
    if "non-LLM" in lab: ctrl = ctrl.replace(" + llm_topic", "")
    r = V.fit(sub, "r24_any", "f24", "f26", lab, ctrl=ctrl)
    res[lab] = {k: float(r[k]) for k in ("OR_a", "OR_b", "ratio", "ratio_lo", "ratio_hi", "p_one")} | {"n": int(r["nobs"]), "nF26": int(r["n_xb"])}
    print(lab, res[lab])
inv = json.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
P = D3.slot_panel(df, inv, controls=False, years_from=2024).merge(df[["submission_id", "f24", "f26"]].rename(columns={"f24": "F24", "f26": "F26"}), on="submission_id")
S = P[P.year.isin([2025, 2026]) & (P.NA == 1)]
S = S[S.groupby("topic100").y.transform("std").fillna(0) > 0]
r = C.logit("y ~ F24 + F26 + C(slot) + C(year) + C(topic100) + llm_topic", S, cluster="topic100")
Vc = r.cov_params(); d_ = r.params["F24"] - r.params["F26"]; se = np.sqrt(Vc.loc["F24", "F24"] + Vc.loc["F26", "F26"] - 2 * Vc.loc["F24", "F26"])
res["slot_vintage_NA_2025_26"] = dict(n=int(r.nobs), OR_F24=float(np.exp(r.params["F24"])), OR_F26=float(np.exp(r.params["F26"])), ratio=float(np.exp(d_)), lo=float(np.exp(d_ - 1.96 * se)), hi=float(np.exp(d_ + 1.96 * se)))
print(res["slot_vintage_NA_2025_26"])
S = P[P.year.isin([2025, 2026]) & (P.NA == 1)].assign(y26=lambda x: (x.year == 2026).astype(int))
r = C.logit("y ~ C(slot) + y26 + llm_topic", S, cluster="topic100")
t = C.or_table(r, ["y26"]).iloc[0]
res["slot_share_2026_vs_2025_NA"] = [float(t.OR), float(t.OR_lo), float(t.OR_hi)]
print("slot share 2026 vs 2025 NA:", res["slot_share_2026_vs_2025_NA"])
json.dump(res, open(OUT / "ident_C2_vintage_na.json", "w"), indent=1)
