"""Audit check 4: full current enlargement - NAME flips, point-corrected G_dec, gate per feature; abstract audit
(enlargement records carry v1_summary) for G3/G4, all years vs 2024-26."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S

pd.set_option("display.width", 250)
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
P = S.build_pairs(orig, U, "original")
enl = S.read_jsonl(S.ENLARGE_PATH)
enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
Pe = S.build_pairs(enl, U, "enlarge")
Pall = pd.concat([P, Pe], ignore_index=True)
keys_t = [k for k, *_ in S.TITLE_FEATS]
keys_a = [k for k, *_ in S.ABS_FEATS]
df = S.universe_frame()
sums = S.stage_prevalences(df, keys_t + keys_a)
Ppool, apool = S.pooled(sums, S.POST)
ft, db = S.flip_table(Pall, keys_t, "enlarged_full")
tp = S.tipping_table(Ppool[:, :len(keys_t)], apool, keys_t, ft, db, "2024-26")
cols = ["feature", "auditable", "G_dec_obs", "G_dec_lo95", "G_dec_hi95", "did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp",
        "G_dec_sel_point", "G_dec_audit_lo", "G_dec_audit_hi", "G_dec_identified", "claim_dec_passes_gate",
        "G_dec_corr_lo95", "G_dec_corr_hi95"]
print(tp[cols].round(3).to_string())
f = ft.set_index("feature").loc["NAME"]
print("NAME flips enlarged: acc v1-present", f.v1_present_acc, "adds", f.adds_acc, "drops", f.drops_acc, "n", f.n_acc,
      "| rej v1-present", f.v1_present_rej, "adds", f.adds_rej, "drops", f.drops_rej, "n", f.n_rej)

# abstract audit: original v1abs pairs + enlargement pairs (enlargement records include v1_summary)
v1a = S.read_jsonl(S.V1ABS_PATH)
v1a = v1a[v1a.error.isna()].drop_duplicates("submission_id", keep="last")
o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]],
                                                      on="submission_id", how="inner")
Pa = S.build_pairs(o2, U, "v1abs", v1_abstract=True)
Pae = S.build_pairs(enl, U, "enl_abs", v1_abstract=True)
for lab, Q in [("orig abs, all yrs", Pa), ("orig abs, 2024-26", Pa[Pa.year >= 2024]),
               ("orig+enl abs, all yrs", pd.concat([Pa, Pae])), ("orig+enl abs, 2024-26", pd.concat([Pa, Pae]).query("year >= 2024"))]:
    Q = Q.reset_index(drop=True)
    fa, dba = S.flip_table(Q, keys_a, lab)
    ta = S.tipping_table(Ppool[:, len(keys_t):], apool, keys_a, fa, dba, "2024-26").set_index("feature")
    fa = fa.set_index("feature")
    for k in ["F24", "L_abs_words"]:
        print(f"{lab:24s} {k:12s} n={int(fa.loc[k].n_acc)}/{int(fa.loc[k].n_rej)} v1pres={int(fa.loc[k].v1_present_acc)}/"
              f"{int(fa.loc[k].v1_present_rej)} adds/drops acc {int(fa.loc[k].adds_acc)}/{int(fa.loc[k].drops_acc)} rej "
              f"{int(fa.loc[k].adds_rej)}/{int(fa.loc[k].drops_rej)} DiD {100*fa.loc[k].did:+.2f} "
              f"[{100*fa.loc[k].did_lo:+.2f}, {100*fa.loc[k].did_hi:+.2f}] tip_total {ta.loc[k].tip_total_pp:+.2f} "
              f"G_total {ta.loc[k].G_total_obs:.3f} identified={bool(ta.loc[k].G_total_identified)}")
