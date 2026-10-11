"""D3 identification audit C (H3c) and D (H3d).
C1 genre test: same H3c logit (year FE, topic100 FE, log authors, llm_topic, log title length; topic100 clusters) with
   the NEUTRAL counterparts N24 = improv*|utili[sz]*|exploit* (title) as outcome. If F26 papers avoid N24 as much as R24,
   the F26 -> R24 avoidance is a genre/composition effect (fewer 'improvement' titles), not a vintage register.
   Also R24 conditional on the title having R24 or N24 (meaning-fixed share version of H3c).
C2 pre-LLM placebo: H3c logit on 2018-2023 (F24/F26 are false positives = writer/genre style).
C3 meaning-fixed vintage: slot-filled titles 2025-26, logit y_LLMvariant ~ F24 + F26 + slot FE + year FE + topic100 FE.
D1 H3d pre-LLM placebo: slot-filled titles 2018-2023, y ~ F_any + slot FE + year FE (+ llm_topic); and NAME ~ F_any.
D2 mechanical coupling: within 2024-26 slot-filled papers, NAME vs opener position cross-tab."""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_vintage as V

OUT = C.OUT / "audit" / "d3_ident"
df = V.prep(D3.load_frame())
tl = df.title_nfkc.fillna("").str.lower()
df["n24"] = C.rx_contains(tl, r"\b(improv\w*|utili[sz]\w*|exploit\w*)").astype(int)
df["imp"] = C.rx_contains(tl, r"\bimprov\w*").astype(int)
df["r24_or_n24"] = ((df.r24_any == 1) | (df.n24 == 1)).astype(int)
res = {}
def row(r, lab):
    keys = ["OR_a", "OR_a_lo", "OR_a_hi", "OR_b", "OR_b_lo", "OR_b_hi", "ratio", "ratio_lo", "ratio_hi", "p_one", "nobs", "n_y", "n_xa", "n_xb"]
    out = {k: (float(r[k]) if not isinstance(r[k], (int, np.integer)) else int(r[k])) for k in keys}
    print(f"{lab:60s} F24 {r['OR_a']:.2f} [{r['OR_a_lo']:.2f},{r['OR_a_hi']:.2f}]  F26 {r['OR_b']:.2f} [{r['OR_b_lo']:.2f},{r['OR_b_hi']:.2f}]  ratio {r['ratio']:.2f} [{r['ratio_lo']:.2f},{r['ratio_hi']:.2f}] n_y={r['n_y']} nF26={r['n_xb']}")
    return out
d2526 = df[df.year.isin([2025, 2026])].copy()
# C1
res["C1_R24_primary"] = row(V.fit(d2526, "r24_any", "f24", "f26", "R24"), "C1 R24 (replicates primary)")
res["C1_N24_neutral"] = row(V.fit(d2526, "n24", "f24", "f26", "N24"), "C1 N24 neutral counterparts improv/utiliz/exploit")
res["C1_improv_only"] = row(V.fit(d2526, "imp", "f24", "f26", "improv"), "C1 improv* only")
res["C1_N24_NApool"] = row(V.fit(d2526[d2526.NA == 1], "n24", "f24", "f26", "N24 NA"), "C1 N24, NA pool")
sub = d2526[d2526.r24_or_n24 == 1].copy()
res["C1_R24_given_R24orN24"] = row(V.fit(sub, "r24_any", "f24", "f26", "R24|R24 or N24"), "C1 R24 | title has R24 or N24 (meaning-fixed share)")
# C2 pre-LLM placebo
pre = df[df.year.between(2018, 2023)].copy()
print("pre-period counts: R24", int(pre.r24_any.sum()), "F24", int(pre.f24.sum()), "F26", int(pre.f26.sum()),
      "R24&F26", int(((pre.r24_any == 1) & (pre.f26 == 1)).sum()), "R24&F24", int(((pre.r24_any == 1) & (pre.f24 == 1)).sum()))
res["C2_pre_2018_23_R24"] = row(V.fit(pre, "r24_any", "f24", "f26", "pre"), "C2 placebo 2018-23 R24")
res["C2_pre_2018_23_N24"] = row(V.fit(pre, "n24", "f24", "f26", "pre N24"), "C2 placebo 2018-23 N24")
pre2 = df[df.year.between(2020, 2023)].copy()
res["C2_pre_2020_23_R24"] = row(V.fit(pre2, "r24_any", "f24", "f26", "pre2"), "C2 placebo 2020-23 R24")
res["C2_2024_R24"] = row(V.fit(df[df.year == 2024], "r24_any", "f24", "f26", "2024", ctrl=V.CTRL.replace("C(year) + ", "")), "C2 2024 R24")
# F26 components in 2025-26: one at a time vs F24
comp = {}
for c, pat in [("principled", r"\bprincipled\b"), ("sharply", r"\bsharply\b"), ("brittle", r"\bbrittle\b"),
               ("genuine", r"\bgenuine\w*"), ("highstakes", r"\bhigh[-‐‑]stakes\b"), ("reframe", r"\brefram\w*")]:
    d2526[f"c_{c}"] = C.rx_contains(d2526.abstract.fillna("").map(C.nfkc).str.lower(), pat).astype(int)
    if d2526[f"c_{c}"].sum() >= 60:
        r = V.fit(d2526, "r24_any", "f24", f"c_{c}", c, extra_x=" + f26_typo_i")
        comp[c] = dict(n=int(d2526[f"c_{c}"].sum()), OR=float(r["OR_b"]), lo=float(r["OR_b_lo"]), hi=float(r["OR_b_hi"]))
        r2 = V.fit(d2526, "n24", "f24", f"c_{c}", c, extra_x=" + f26_typo_i")
        comp[c].update(OR_N24=float(r2["OR_b"]), lo_N24=float(r2["OR_b_lo"]), hi_N24=float(r2["OR_b_hi"]))
r = V.fit(d2526, "r24_any", "f24", "f26_typo_i", "typo", extra_x=" + f26_words_i"); comp["typography"] = dict(n=int(d2526.f26_typo_i.sum()), OR=float(r["OR_b"]), lo=float(r["OR_b_lo"]), hi=float(r["OR_b_hi"]))
r2 = V.fit(d2526, "n24", "f24", "f26_typo_i", "typo", extra_x=" + f26_words_i"); comp["typography"].update(OR_N24=float(r2["OR_b"]), lo_N24=float(r2["OR_b_lo"]), hi_N24=float(r2["OR_b_hi"]))
res["C1_F26_components"] = comp
print("F26 components (OR on R24 | OR on N24):", json.dumps(comp, indent=0))

# C3 meaning-fixed vintage contrast within slots, 2025-26
inv = json.loads((D3.OUTDIR / "slot_inventory.json").read_text())["inventory"]
P = D3.slot_panel(df, inv, controls=False, years_from=2018)
P = P.merge(df[["submission_id", "f24", "f26"]].rename(columns={"f24": "F24", "f26": "F26"}), on="submission_id")
S = P[P.year.isin([2025, 2026])].copy()
S = S[S.groupby("topic100").y.transform("std").fillna(0) > 0]
r = C.logit("y ~ F24 + F26 + C(slot) + C(year) + C(topic100) + llm_topic", S, cluster="topic100")
t = C.or_table(r, ["F24", "F26"])
Vc = r.cov_params(); diff = r.params["F24"] - r.params["F26"]; se = np.sqrt(Vc.loc["F24", "F24"] + Vc.loc["F26", "F26"] - 2 * Vc.loc["F24", "F26"])
res["C3_slot_vintage_2025_26"] = dict(n=int(r.nobs), nF24=int(S.F24.sum()), nF26=int(S.F26.sum()),
    OR_F24=float(t.loc["F24", "OR"]), OR_F24_ci=[float(t.loc["F24", "OR_lo"]), float(t.loc["F24", "OR_hi"])],
    OR_F26=float(t.loc["F26", "OR"]), OR_F26_ci=[float(t.loc["F26", "OR_lo"]), float(t.loc["F26", "OR_hi"])],
    ratio=float(np.exp(diff)), ratio_ci=[float(np.exp(diff - 1.96 * se)), float(np.exp(diff + 1.96 * se))])
print("C3", res["C3_slot_vintage_2025_26"])

# D1 H3d pre-LLM placebo
Pp = P.merge(df[["submission_id", "F_any"]].rename(columns={"F_any": "Fx"}), on="submission_id")
for lab, yrs in [("pre_2018_23", range(2018, 2024)), ("pre_2020_23", range(2020, 2024)), ("post_2024_26", range(2024, 2027))]:
    S = Pp[Pp.year.isin(list(yrs))].copy()
    r = C.logit("y ~ Fx + C(slot) + C(year) + llm_topic", S, cluster="topic100")
    t = C.or_table(r, ["Fx"]).iloc[0]
    U = df[df.year.isin(list(yrs))]
    rn = C.logit("name_primary ~ F_any + C(year) + llm_topic + log_authors", U, cluster="topic100")
    tn = C.or_table(rn, ["F_any"]).iloc[0]
    Sp = S.drop_duplicates("submission_id")
    rn2 = C.logit("name_primary ~ Fx + C(year) + llm_topic", Sp, cluster="topic100")
    tn2 = C.or_table(rn2, ["Fx"]).iloc[0]
    res[f"D1_{lab}"] = dict(n_slot_rows=int(r.nobs), n_F1=int(S.Fx.sum()), share_F1=float(S.Fx.mean()),
        OR_slot=float(t.OR), OR_slot_ci=[float(t.OR_lo), float(t.OR_hi)], p=float(t.p),
        OR_name_all_papers=float(tn.OR), OR_name_all_ci=[float(tn.OR_lo), float(tn.OR_hi)],
        OR_name_slot_papers=float(tn2.OR), OR_name_slot_ci=[float(tn2.OR_lo), float(tn2.OR_hi)])
    print("D1", lab, res[f"D1_{lab}"])
# F24-only pre placebo (RARE21 false positives are 'flowery' writers)
S = Pp[Pp.year.between(2018, 2023)].copy()
r = C.logit("y ~ F24 + C(slot) + C(year) + llm_topic", S, cluster="topic100")
t = C.or_table(r, ["F24"]).iloc[0]
res["D1_pre_F24_only"] = dict(OR=float(t.OR), ci=[float(t.OR_lo), float(t.OR_hi)], nF24=int(S.F24.sum()))
print("D1 pre F24", res["D1_pre_F24_only"])

# D2 mechanical coupling NAME vs opener position, 2024-26 slot-filled LLM-slot rows
S = P[(P.year >= 2024)].copy()
S["is_study"] = (S.slot == "study_adj").astype(int)
ct = pd.crosstab([S.is_study, S.opener_pos], S.name_primary)
print(ct)
op = S[S.is_study == 0]
res["D2_opener_rows"] = int(len(op))
res["D2_share_NAME_eq_postname"] = float(((op.opener_pos == "post_name").astype(int) == op.name_primary).mean())
res["D2_LLMshare_by_pos"] = op.groupby("opener_pos").y.mean().to_dict()
res["D2_F_by_pos"] = op.merge(df[["submission_id", "F_any"]], on="submission_id").groupby("opener_pos").F_any_y.mean().to_dict() if "F_any_y" in op.merge(df[["submission_id", "F_any"]], on="submission_id") else None
print("D2", res["D2_share_NAME_eq_postname"], res["D2_LLMshare_by_pos"])
json.dump(res, open(OUT / "ident_C_vintage.json", "w"), indent=1, default=float)
