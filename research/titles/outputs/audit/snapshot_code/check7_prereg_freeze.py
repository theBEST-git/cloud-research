"""Audit check 7: WP4 outputs use the 254-line enlargement freeze; prereg froze 1,261 lines. What does WP4's own
gate say at the prereg freeze point (first 1,261 lines)?"""
import pandas as pd
from analyses import _core as C
from analyses import snapshot_bounds as S
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
P = S.build_pairs(orig, U, "o")
enl = S.read_jsonl(S.ENLARGE_PATH).head(1261)
enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
Pall = pd.concat([P, S.build_pairs(enl, U, "e")], ignore_index=True)
keys_t = [k for k, *_ in S.TITLE_FEATS]
sums = S.stage_prevalences(S.universe_frame(), keys_t)
Pp, ap = S.pooled(sums, S.POST)
ft, db = S.flip_table(Pall, keys_t, "enl1261")
tp = S.tipping_table(Pp, ap, keys_t, ft, db, "2024-26")
print("pairs", Pall.decision.value_counts().to_dict())
print(tp[tp.G_dec_identified | tp.claim_dec_passes_gate | tp.feature.isin(["NAME"])][[
    "feature", "auditable", "G_dec_obs", "G_dec_lo95", "G_dec_hi95", "did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp",
    "G_dec_identified", "claim_dec_passes_gate", "G_dec_corr_lo95", "G_dec_corr_hi95", "G_dec_corrboot_lo90", "G_dec_corrboot_hi90"]].round(3).to_string())
