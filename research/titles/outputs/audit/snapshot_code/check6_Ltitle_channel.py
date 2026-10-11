"""Audit check 6: arXiv v1 titles never carry U+2011/U+2013/U+2014, so every stored-title typography instance is
an 'add' by channel. L_title = title_typo | R24 | R26 inherits these artefact adds. Compare the G2 gate (L-title
G_total < 1) with L_title vs an arXiv-measurable L-title (R24 | R26) on original and current enlarged pairs."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S

U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
enl = S.read_jsonl(S.ENLARGE_PATH)
enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
P = S.build_pairs(orig, U, "o")
Pall = pd.concat([P, S.build_pairs(enl, U, "e")], ignore_index=True)

df = S.universe_frame()
df["L_title_words"] = df[["r24_any", "r26_any"]].astype(bool).any(axis=1)
S.FEAT_COL["L_title_words"] = "L_title_words"
keys = ["title_typo", "L_title", "L_title_words"]
sums = S.stage_prevalences(df, keys)
Ppool, apool = S.pooled(sums, S.POST)
for lab, Q in [("original", P), ("orig+enl current", Pall)]:
    Q = Q.copy()
    Q["L_title_words_or"] = Q[["R24_or", "R26_or"]].max(axis=1)
    Q["L_title_words_v1"] = Q[["R24_v1", "R26_v1"]].max(axis=1)
    ft, db = S.flip_table(Q, keys, lab)
    tp = S.tipping_table(Ppool, apool, keys, ft, db, "2024-26").set_index("feature")
    ft = ft.set_index("feature")
    for k in keys:
        f, t = ft.loc[k], tp.loc[k]
        print(f"{lab:18s} {k:14s} v1pres {int(f.v1_present_acc)}/{int(f.v1_present_rej)} adds {int(f.adds_acc)}/{int(f.adds_rej)} "
              f"drops {int(f.drops_acc)}/{int(f.drops_rej)} DiD {100*f.did:+.2f} [{100*f.did_lo:+.2f},{100*f.did_hi:+.2f}] "
              f"auditable={bool(f.auditable)} G_total {t.G_total_obs:.3f} tip_total {t.tip_total_pp:+.2f} "
              f"identified={bool(t.G_total_identified)} corr95 [{t.G_total_corr_lo95:.3f},{t.G_total_corr_hi95:.3f}] "
              f"G2_pass={bool(t.G_total_identified and t.G_total_corr_hi95 < 1)}")
