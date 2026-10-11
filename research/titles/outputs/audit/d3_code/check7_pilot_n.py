"""Audit D3: which inventory/opener combination gives n=2,163 vs the pilot's 2,362 (RESULTS section 1 claim)."""
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import features_v2 as FV
inv = D3.frozen_inventory()
lx = FV.lexicon()["slots"]
inv_all = {s: {side: list(lx[s][side]) for side in ("llm", "neutral")} for s in D3.SLOTS}
df = D3.load_frame()
for lab, i, rule, sense in [("primary rule, V2 drops", inv, "primary", True), ("any-lead, V2 drops", inv, "al", True),
                            ("primary, full lexicon", inv_all, "primary", True), ("any-lead, full lexicon", inv_all, "al", True),
                            ("any-lead, full lexicon, no sense", inv_all, "al", False)]:
    P = D3.slot_panel(df, i, rule=rule, sense=sense, controls=False)
    r = [x for x in D3.fit_set(P, lab, stacked=False) if x["model"] == "slots_post"][0]
    print(f"{lab:36s} n={len(P)}  OR {r['OR']:.2f} [{r['OR_lo']:.2f}, {r['OR_hi']:.2f}]")
