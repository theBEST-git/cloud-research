import json, numpy as np, pandas as pd
from analyses import _core as C
from analyses import d4_stage_gains as S
df = C.load_analysis_frame(feature_cols=["f24"], universe_cols=["submission_id","year","abstract","pool","ACC"])
sd_new, words_new = S.style_density(df)
sd_old = pd.read_parquet(S.OUTDIR/"style_density.parquet")
words_old = json.loads((S.OUTDIR/"style_density_words.json").read_text())
m = sd_new.merge(sd_old, on="submission_id", how="outer", suffixes=("_new","_old"), indicator=True)
print(m._merge.value_counts())
print("max abs diff xs_per100:", np.nanmax(np.abs(m.xs_per100_new - m.xs_per100_old)))
print({y: (len(words_new[y]), len(words_old[y]), words_new[y]==words_old[y]) for y in words_new})
fr = S.load_frame()
print("NaN xs_per100 in frame:", fr.xs_per100.isna().sum(), "rows", len(fr))
# overlap of density words with RARE21 / F24 list
print(words_old["2024"][:60])
