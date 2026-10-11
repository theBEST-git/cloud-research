"""Audit check 9: one-sided identification p-values (audit DiD beyond the tipping point, pseudo-flip SE) with Holm
across auditable title features, at the WP4 freeze (254), prereg freeze (1261) and all current lines."""
import numpy as np
import pandas as pd
from scipy import stats
from analyses import _core as C
from analyses import snapshot_bounds as S
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
P = S.build_pairs(S.read_jsonl(S.ORIG_PATH), U, "o")
E = S.read_jsonl(S.ENLARGE_PATH)
keys_t = [k for k, *_ in S.TITLE_FEATS]
sums = S.stage_prevalences(S.universe_frame(), keys_t, n_boot=200)
Pp, ap = S.pooled(sums, S.POST)
for cap in [254, 1261, len(E)]:
    enl = E.head(cap); enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
    Q = pd.concat([P, S.build_pairs(enl, U, "e")], ignore_index=True)
    ft, db = S.flip_table(Q, keys_t, str(cap), Wb=S.boot_matrix(Q, n_boot=200))
    tp = S.tipping_table(Pp, ap, keys_t, ft, db, "2024-26")
    t = tp[tp.auditable].copy()
    se = (t.did_hi_pp - t.did_lo_pp) / (2 * S.Z)
    z = np.where(t.G_dec_obs >= 1, (t.tip_dec_pp - t.did_pp) / se, (t.did_pp - t.tip_dec_pp) / se)
    t["p_one"] = stats.norm.sf(z)
    t = t.sort_values("p_one")
    m = len(t)
    t["holm_thr"] = 0.025 / (m - np.arange(m))  # one-sided 2.5% to match the 95% two-sided CI rule
    rej = (t.p_one.to_numpy() < t.holm_thr.to_numpy())
    t["holm_pass"] = np.cumprod(rej).astype(bool)
    print(f"lines {cap}: {m} auditable; code-rule identified: {sorted(tp.feature[tp.G_dec_identified])}; "
          f"Holm-identified: {sorted(t.feature[t.holm_pass])}")
    print(t[["feature", "did_pp", "tip_dec_pp", "p_one", "holm_thr"]].head(4).round(4).to_string())
