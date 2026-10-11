import pandas as pd, numpy as np
from analyses import _core as C
from analyses import d4_bias_atlas as A
pairs = pd.read_csv(A.OUTDIR / "audit_pairs.csv", dtype={"submission_id": str})
f = C.load_features(["submission_id", "name_primary", "name_compound", "phrase_colon", "ortho_mixed_case", "case_title_case",
                     "case_all_caps", "case_sentence_case", "question_opener", "title_typo", "r24_any", "r26_any",
                     "name_strict", "name_loose", "ortho_all_caps", "llm_t_abbrev_only"])
m = pairs.merge(f, on="submission_id", how="left", validate="1:1")
for k, c in A.AUDIT_FEATURES:
    if c in m:
        diff = (m[f"{k}_or"] != m[c].astype(int)).sum()
        print(f"{k:18s} stored-title feature mismatches vs features_v2: {diff}")
print(len(pairs))
