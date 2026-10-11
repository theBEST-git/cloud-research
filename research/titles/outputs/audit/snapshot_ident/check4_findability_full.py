"""Audit check 4: SB4 'findability depends neither on NAME nor title length' with orig + full enlargement, incl. acc x NAME."""
import numpy as np, pandas as pd, statsmodels.formula.api as smf
from analyses import snapshot_bounds as S
from analyses import _core as CORE
fv = CORE.load_features(["submission_id", "n_words", "name_primary"])
orig = S.read_jsonl(S.ORIG_PATH)
enl = S.read_jsonl(S.ENLARGE_PATH); enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
d = S.audit_frame(pd.concat([orig, enl], ignore_index=True), fv)
d = d[d.year.isin(S.AUDIT_YEARS)]
print("n", len(d), d.groupby("decision").found_i.mean().round(3).to_dict())
for f in ["found_i ~ C(year) + acc + log_nw + NAME", "usable_i ~ C(year) + acc + log_nw + NAME",
          "found_i ~ C(year) + acc * NAME + log_nw", "usable_i ~ C(year) + acc * NAME + log_nw"]:
    m = smf.logit(f, d).fit(disp=0)
    ci = np.exp(m.conf_int())
    print(f)
    for t in [x for x in m.params.index if x in ("acc", "NAME", "log_nw", "acc:NAME")]:
        print(f"   {t:10s} OR {np.exp(m.params[t]):.2f} [{ci.loc[t,0]:.2f}, {ci.loc[t,1]:.2f}] p={m.pvalues[t]:.3f}")
print(d.groupby(["decision", "NAME"]).agg(n=("found_i", "size"), found=("found_i", "mean"), usable=("usable_i", "mean")).round(3))
