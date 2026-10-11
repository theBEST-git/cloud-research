"""Reporting audit: IPW normalised weight ranges and Kish n (RESULTS section 1)."""
import numpy as np
from analyses import _core as C
from analyses import snapshot_bounds as SB
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
fv = C.load_features(["submission_id", "n_words", "name_primary"])
orig = SB.read_jsonl(SB.ORIG_PATH)
d = SB.audit_frame(orig, fv)
fm, fits = SB.findability_models(d)
P = SB.build_pairs(orig, U, "original")
fit = fits["usable_i ~ C(year) + acc + log_nw + NAME"]
for pop in (False, True):
    p, w = SB.ipw_weights(d, P, fit, pop=pop, U=U)
    acc = p.acc.to_numpy() == 1
    kish = {g: float(w[m].sum() ** 2 / (w[m] ** 2).sum()) for g, m in (("acc", acc), ("rej", ~acc))}
    print(f"pop={pop}: range {w.min():.3f}-{w.max():.3f}; kish {kish}; n {acc.sum()}/{(~acc).sum()}")
