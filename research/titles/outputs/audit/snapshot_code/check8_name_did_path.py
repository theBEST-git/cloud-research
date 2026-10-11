"""Audit check 8: NAME-family net-flip DiD and point-corrected G_dec as the enlargement accrues."""
import pandas as pd
from analyses import _core as C
from analyses import snapshot_bounds as S
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
P = S.build_pairs(orig, U, "o")
E = S.read_jsonl(S.ENLARGE_PATH)
keys = ["NAME", "NAME_strict", "NAME_loose"]
sums = S.stage_prevalences(S.universe_frame(), keys, n_boot=200)
Pp, ap = S.pooled(sums, S.POST)
for cap in [254, 600, 1000, 1261, len(E)]:
    enl = E.head(cap); enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
    Q = pd.concat([P, S.build_pairs(enl, U, "e")], ignore_index=True)
    ft, db = S.flip_table(Q, keys, str(cap), Wb=S.boot_matrix(Q, n_boot=200))
    tp = S.tipping_table(Pp, ap, keys, ft, db, "2024-26").set_index("feature")
    f = ft.set_index("feature")
    print(cap, f"n={int(f.loc['NAME'].n_acc)}/{int(f.loc['NAME'].n_rej)}", "; ".join(
        f"{k}: DiD {100*f.loc[k].did:+.2f} [{100*f.loc[k].did_lo:+.2f},{100*f.loc[k].did_hi:+.2f}] "
        f"Gdec obs {tp.loc[k].G_dec_obs:.3f} -> {tp.loc[k].G_dec_sel_point:.3f}" for k in keys))
