"""Audit check 2: is the G1 (H4a NAME G_total) gate verdict stable as the enlargement cache grows?
Re-uses snapshot_bounds functions read-only; writes nothing in outputs/snapshot."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S

U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
P = S.build_pairs(orig, U, "original")
keys_t = [k for k, *_ in S.TITLE_FEATS]
df = S.universe_frame()
sums = S.stage_prevalences(df, keys_t)
Ppool, apool = S.pooled(sums, S.POST)
enl_all = S.read_jsonl(S.ENLARGE_PATH)
print("enlarge records now:", len(enl_all))

rows = []
for cap in [None, 248, 254, 400, 600, 800, 1000, 1200, len(enl_all)]:
    if cap is None:
        Pall = P.copy(); tag = "original only"
    else:
        enl = enl_all.head(cap)
        enl = enl[enl.error.isna()] if "error" in enl else enl
        enl = enl.drop_duplicates("submission_id", keep="last")
        Pe = S.build_pairs(enl, U, "enlarge")
        Pall = pd.concat([P, Pe], ignore_index=True); tag = f"orig+enl[:{cap}]"
    for yrs, lab in [((2022, 2023, 2024, 2025, 2026), "all yrs"), ((2024, 2025, 2026), "2024-26")]:
        Q = Pall[Pall.year.isin(yrs)].reset_index(drop=True)
        ft, db = S.flip_table(Q, keys_t, tag)
        tp = S.tipping_table(Ppool, apool, keys_t, ft, db, "2024-26").set_index("feature")
        f = ft.set_index("feature").loc["NAME"]
        n = tp.loc["NAME"]
        rows.append(dict(spec=tag, years=lab, n_acc=int(f.n_acc), n_rej=int(f.n_rej),
                         did_pp=round(100 * f.did, 2), did_lo=round(100 * f.did_lo, 2), did_hi=round(100 * f.did_hi, 2),
                         Gtot_corr90=f"[{n.G_total_corr_lo90:.3f}, {n.G_total_corr_hi90:.3f}]",
                         Gtot_pass=bool(0.90 <= n.G_total_corr_lo90 and n.G_total_corr_hi90 <= 1.11),
                         Gdec_corr90=f"[{n.G_dec_corr_lo90:.3f}, {n.G_dec_corr_hi90:.3f}]",
                         Gdec_pass=bool(0.90 <= n.G_dec_corr_lo90 and n.G_dec_corr_hi90 <= 1.11),
                         n_identified=int(tp.G_dec_identified.sum()),
                         identified=sorted(tp.index[tp.G_dec_identified]),
                         n_auditable=int(ft.auditable.sum())))
pd.set_option("display.width", 250)
print(pd.DataFrame(rows).to_string())
