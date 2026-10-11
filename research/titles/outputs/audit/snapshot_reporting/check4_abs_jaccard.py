"""Reporting audit: CI for the v1-vs-stored abstract Jaccard difference (RESULTS section 6, 0.77 vs 0.83)."""
import numpy as np
from analyses import _core as C
from analyses import snapshot_bounds as SB
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = SB.read_jsonl(SB.ORIG_PATH)
v1a = SB.read_jsonl(SB.V1ABS_PATH)
v1a = v1a[v1a.error.isna()] if "error" in v1a else v1a
v1a = v1a.drop_duplicates("submission_id", keep="last")
o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]],
                                                      on="submission_id", how="inner")
Pa = SB.build_pairs(o2, U, "v1abs", v1_abstract=True)
a = Pa[Pa.acc == 1].abs_jacc.to_numpy(); r = Pa[Pa.acc == 0].abs_jacc.to_numpy()
rng = np.random.default_rng(7)
bs = [rng.choice(a, len(a)).mean() - rng.choice(r, len(r)).mean() for _ in range(4000)]
print(len(a), len(r), round(a.mean(), 4), round(r.mean(), 4), "diff", round(a.mean() - r.mean(), 4), np.quantile(bs, [.025, .975]).round(4))
print("median", np.median(a).round(3), np.median(r).round(3))
for y in sorted(Pa.year.unique()):
    m = Pa.year == y
    print(y, Pa[m & (Pa.acc == 1)].abs_jacc.mean().round(3), Pa[m & (Pa.acc == 0)].abs_jacc.mean().round(3))
