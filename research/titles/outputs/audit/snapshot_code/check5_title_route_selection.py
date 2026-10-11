"""Audit check 5: rejected papers are found via the title-match clause (abstract Jaccard < 0.45, title Jaccard >= 0.6
+ surname) ~8x more often than accepted ones. That clause selects papers whose LATEST arXiv title still matches the
stored title. Sensitivity: restrict both arms to abstract-matched pairs (Jaccard >= 0.45, a title-free criterion)."""
import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as S

pd.set_option("display.width", 250)
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
enl = S.read_jsonl(S.ENLARGE_PATH)
enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
keys_t = [k for k, *_ in S.TITLE_FEATS]
df = S.universe_frame()
sums = S.stage_prevalences(df, keys_t, n_boot=200)
Ppool, apool = S.pooled(sums, S.POST)

for lab, rec in [("original", orig), ("orig+enl(current)", pd.concat([orig, enl], ignore_index=True))]:
    Pr = S.build_pairs(rec, U, lab)
    aj = rec.set_index("submission_id").abstract_jaccard
    Pr["abs_j"] = Pr.submission_id.map(aj).astype(float)
    Pr["title_clause"] = Pr.abs_j < 0.45
    print(f"\n=== {lab}: usable pairs {len(Pr)}")
    print("share of usable pairs found only through the title clause:\n",
          Pr.groupby("decision").title_clause.agg(["sum", "mean"]).round(3))
    print("retitled (changed_norm) by decision x title_clause:\n",
          Pr.groupby(["decision", "title_clause"]).changed_norm.agg(["mean", "size"]).round(3))
    for sub, Q in [("all usable", Pr), ("abstract-matched only (Jacc>=0.45)", Pr[~Pr.title_clause])]:
        Q = Q.reset_index(drop=True)
        ft, db = S.flip_table(Q, keys_t, sub, Wb=S.boot_matrix(Q, n_boot=200))
        tp = S.tipping_table(Ppool, apool, keys_t, ft, db, "2024-26").set_index("feature")
        ra, rr = Q[Q.acc == 1].changed_norm.mean(), Q[Q.acc == 0].changed_norm.mean()
        f = ft.set_index("feature")
        print(f"  [{sub}] n={int((Q.acc==1).sum())}/{int((Q.acc==0).sum())} retitle acc {100*ra:.1f}% rej {100*rr:.1f}% "
              f"diff {100*(ra-rr):+.1f} pp; NAME DiD {100*f.loc['NAME'].did:+.2f} [{100*f.loc['NAME'].did_lo:+.2f}, "
              f"{100*f.loc['NAME'].did_hi:+.2f}]; NAME_strict {100*f.loc['NAME_strict'].did:+.2f} "
              f"[{100*f.loc['NAME_strict'].did_lo:+.2f}, {100*f.loc['NAME_strict'].did_hi:+.2f}]; "
              f"identified: {sorted(tp.index[tp.G_dec_identified])}")
