# `analyses` package: API and data contract (WP0 core, WP1 features v2, WP2 topics/encoders)

Plan: `research/titles/docs/PLAN.md` (§0 common definitions). Everything is read-only on `data/` and `cache/`.
Outputs live in `research/titles/outputs/<folder>/`.

## 1. How to run and load

Run every script as a module from `research/titles/src`, with at most 2 BLAS threads:

```bash
cd /home/user/cloud-research/research/titles/src
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses._core          # universe, counts, crosswalk, LLM clusters (~10 s)
OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.features_v2    # features_v2.parquet + lexicon hash (~80 s)
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.topics_bge     # bge topics, centroids, stability (~50 s)
nohup env OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.embed_masked 2 \
      > ../outputs/topics/embed_masked.log 2>&1 &                       # background, ~1-1.5 h, resumable
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.smoke_test     # assertions -> outputs/core/smoke_test.txt
```

Load the data in downstream scripts like this:

```python
from analyses import _core as C
df = C.load_analysis_frame()                         # universe (all cols) + features_v2 (all cols), 43,482 rows
df = C.load_analysis_frame(feature_cols=["name_primary", "F_any"],
                           universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "NA"],
                           with_bge_topics=True)     # adds topic50_bge, topic100_bge, llm_cluster_bge, llm_topic_bge
E = C.load_embedding(df, "abstract", "bge-small-en-v1.5")   # float32, rows aligned to df via df.emb_row
Em, found = C.load_masked_embedding(df)                      # name-masked bge (2018-26); found=False -> zero row
```

- All three tables (`universe.parquet`, `features_v2.parquet`, `topics_bge.parquet`) have one row per universe paper, in the same order (export order: year, then submission_id), keyed by `submission_id`.
- `emb_row` indexes the cache embeddings (`cache/emb_*.npy`, aligned to `data/submissions.csv.gz` order).
- **pandas 3 caveat.** String columns are pyarrow-backed. `Series.str.contains/.extract/.count` then use the RE2 engine: no look-behind, no `\u` escapes, ASCII `\b`. Use `C.rx_contains`, `C.rx_extract` and `C.rx_count`, which use Python `re`, for any regex in this study.
- Booleans are stored as `bool`. Slot and control-pair outcomes are `float` with values 1/0 and NaN when the slot is not filled. Cast with `.astype(int)` before formulas.

## 2. Universe and pools (PLAN §0)

**Universe U** = 43,516 discovery rows minus 34:
- 1 empty title (2017);
- 17 placeholder titles (`features.PLACEHOLDER_TITLES`: NA, N/A, withdraw(n), title, placeholder, xxx, xxxx, 111, …);
- 16 abstracts with fewer than 20 words (`features.is_placeholder`).

This leaves **43,482** rows. Per-year counts are in `outputs/core/universe_counts.csv`:

| year | rows | dropped | U | ACC | REJ | WD | DR | NA | wd_post | OTHER |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 385 | 1 | 384 | 149 | 194 | 0 | 0 | 194 | 0 | 41 |
| 2018 | 774 | 5 | 769 | 263 | 378 | 57 | 0 | 435 | 0 | 71 |
| 2019 | 1,255 | 7 | 1,248 | 412 | 713 | 123 | 0 | 836 | 0 | 0 |
| 2020 | 2,071 | 1 | 2,070 | 558 | 1,215 | 290 | 7 | 1,512 | 0 | 0 |
| 2021 | 2,364 | 4 | 2,360 | 678 | 1,341 | 327 | 14 | 1,682 | 0 | 0 |
| 2022 | 2,649 | 0 | 2,649 | 875 | 1,156 | 599 | 19 | 1,774 | 0 | 0 |
| 2023 | 3,872 | 0 | 3,872 | 1,256 | 1,717 | 883 | 16 | 2,616 | 0 | 0 |
| 2024 | 5,766 | 1 | 5,765 | 1,778 | 2,657 | 1,293 | 37 | 3,987 | 0 | 0 |
| 2025 | 8,960 | 7 | 8,953 | 2,904 | 3,674 | 2,322 | 53 | 6,049 | 0 | 0 |
| 2026 | 15,420 | 8 | 15,412 | 4,175 | 6,440 | 4,060 | 737 | 11,237 | 349 | 0 |
| total | 43,516 | 34 | 43,482 | 13,048 | 19,485 | 9,954 | 883 | 30,322 | 349 | 112 |

**Pools** (boolean columns in `universe.parquet`):
- `ACC` / `REJ`: the README acceptance population (`ordinary_submission`, `outcome_eligible==1`, decision accepted/rejected), split by decision.
- `WD`: `administrative_status=='withdrawn'`.
- `DR`: `administrative_status=='desk_rejected'`.
- `NA = REJ | WD | DR`: the camera-ready-free pool.
- `OTHER`: ordinary rows with an unknown decision (41 in 2017, 71 in 2018). These rows belong to no pool.
- The 27 inconsistent accepted-but-withdrawn/desk-rejected rows (`inconsistent`) are outside ACC/REJ but inside WD/DR.
- `wd_post` = withdrawn with decision 'rejected' in 2026 (349). `wd_decided` = any withdrawn row carrying an accept/reject decision, in any year (655). It is descriptive and can serve as a sensitivity flag.

**D4 stages:**
- `stage_s1` = not DR.
- `stage_s2` = s1 and (not WD or `wd_post`).
- `stage_s3` = ACC.
- s0 is U.
- OTHER rows sit in s2 without being accepted. Restrict D4 to 2018+ and/or drop OTHER if needed.

**Periods:**
- `post` = year ≥ 2024; `t` = year − 2023; `period` ∈ {pre, post}.
- `C.year_mask(df.year, which)` with `which` ∈ {all, pre (2017–23), pre_wd (2018–23), post (2024–26), post_excl2026 (2024–25), excl2026, no2019, 2018plus, early (2022–23), late (2025–26)}.

## 3. `universe.parquet` columns (`outputs/core/universe.parquet`)

| column | type | definition |
|---|---|---|
| submission_id | str | primary key |
| year | int | ICLR year |
| emb_row | int | row index into `cache/emb_*.npy` and `cache/embedding_ids.npy` |
| title | str | raw title (not normalised; use for typography) |
| title_nfkc | str | NFKC-normalised, stripped title (use for word features) |
| abstract | str | raw abstract |
| administrative_status, decision, outcome_eligible | str/str/int | as exported |
| primary_area | str/NaN | raw label; NaN before 2024 |
| area_h | str/NaN | harmonised area: 2024 labels mapped to 2025/26 labels (`outputs/core/area_crosswalk.csv`). 21 areas; 'foundation or frontier models, including LLMs' and 'learning on time series and dynamical systems' exist from 2025 only |
| area_short | str/NaN | short name of `area_h` |
| normalized_keywords_json | str/NaN | as exported (for D1 R2) |
| declared_name_count | int | declared author-list length |
| review_count | int | as exported |
| in_acc_pop | bool | README acceptance population |
| ACC, REJ, WD, DR, NA | bool | pools (section 2) |
| wd_post | bool | 2026 withdrawal with decision 'rejected' |
| wd_decided | bool | any withdrawn row with an accept/reject decision |
| inconsistent | bool | withdrawn/desk-rejected with decision 'accepted' |
| pool | str | ACC / REJ / WD / DR / OTHER |
| stage_s1, stage_s2, stage_s3 | bool | D4 stages (section 2) |
| post, t, period | int/int/str | period helpers |
| log_authors | float | log(max(declared_name_count, 1)) |
| topic50, topic100 | int | MiniLM abstract KMeans (cache/topics.parquet; fitted on all 43,516 rows) |
| llm_regex | bool | `C.LLM_TOPIC_REGEX` on title + abstract, case-insensitive. Identical to `cache/title_features.llm_topic` |
| llm_cluster | bool | paper in a MiniLM topic100 cluster where more than 50% of U papers (all years) match the regex. 20 clusters, listed in `outputs/core/llm_clusters.json` |
| llm_topic | bool | **PLAN §0 LLM topic = llm_regex OR llm_cluster** (this is the control) |
| non_llm | bool | not llm_topic (the non-LLM subset) |
| n_keys, max_prior_subs, max_prior_accs, sum_prior_accs, share_new_authors, profile_share, last_prior_subs, last_prior_accs, first_prior_subs, any_prior_acc | float/int | author covariates from exact declared-ID keys (`cache/author_features.parquet`). Counts are prior submissions/acceptances within the discovery export. They are "declared profile keys", not persons. 4 rows have no keys |
| lmax_prior_subs, lmax_prior_accs, llast_prior_accs, llast_prior_subs, lfirst_prior_subs, lsum_prior_accs | float | log1p of the counts |
| exp_valid | bool | year ≥ 2022 (experience covariates interpretable) |

## 4. `features_v2.parquet` columns (`outputs/features/features_v2.parquet`)

Lexicons are in `analyses/lexicons.json` (v2.0, frozen). SHA-256 hashes of `lexicons.json`, `features.py` (v1) and `features_v2.py` are in `outputs/features/lexicon_hash.txt`. The v1 lock uses a content hash because git is not used here.

Text bases:
- "title" means the NFKC title, lower-cased, with LaTeX math replaced by `MATH`.
- "raw" means the unnormalised string. NFKC maps U+2011 to U+2010, so typography is always measured on raw text.
- Abstract word lists run on the NFKC lower-cased abstract.

### 4.1 v1 features (`features.title_features`, unchanged)

| column | type | definition |
|---|---|---|
| n_chars, n_words | int | title length (`features.tokens`) |
| compound | bool | lead before a colon (ratio colons excluded) or a spaced dash |
| name_colon | bool | **NAME (primary)**: the compound lead is a coined name (`features.is_coined_name`) |
| phrase_colon | bool | compound with a non-name lead |
| lead_segment | str | lead with math replaced by `MATH`; '' if not compound |
| name_orthography | str | for NAME titles: all_caps / mixed_case / word / paren_acronym, else '' |
| casing | str | title_case / sentence_case / all_caps / mixed / other |
| question, question_opener, exclamation, quoted, has_math, has_digit | bool | surface flags |
| first_word | str | first token, lower-case |
| action_opener | bool | v1 gerund-opener list (v1) |
| title_case_share | float | share of capitalised content words (NaN if < 2) |
| mentions_llm | bool | v1 LLM-mention regex |
| tpl_* (24) | bool | v1 template/snowclone regexes (`features.TEMPLATES`) |

### 4.2 NAME variants, orthography, casing

| column | type | definition |
|---|---|---|
| name_primary | bool | = name_colon |
| name_strict | bool | name_colon and the lead is a single whitespace token and not a genre word (`lexicons.genre_leads` ∪ `features.GENERIC_LEADS`). A subset of name_primary |
| name_loose | bool | compound lead of 1–2 tokens whose first token is not a function word (`features.FUNCTION_WORDS`) and with no genre word. **Not a superset of primary**: 55 long "(ACR)" leads are primary but not loose; 1,031 two-token descriptive leads are loose only |
| name_compound | bool | = compound (any colon or spaced dash) |
| lead_n_tokens | int | whitespace tokens in the lead (0 if none) |
| lead_is_genre | bool | lead is or contains a genre word |
| lead_raw | str | lead exactly as written (LaTeX kept); '' if none |
| ortho_all_caps, ortho_mixed_case, ortho_word, ortho_paren_acronym | bool | name_orthography dummies (False for non-NAME) |
| case_title_case, case_sentence_case, case_all_caps, case_mixed, case_other | bool | casing dummies |

### 4.3 LLM slots and control pairs (D3)

- **Opener** = the first word `[A-Za-z]+(-[A-Za-z]+)*` of the title. When the title is "NAME: …" (name_primary), it is the first word of the subtitle instead.

| column | type | definition |
|---|---|---|
| opener_word | str | the opener, lower-case |
| opener_pos | str | 'start' or 'post_name' |
| opener_word_al | str | opener after ANY compound lead (close to the pilot rule, which used any colon lead ≤ 40 characters) |
| opener_gerund | bool | opener ends in -ing, has more than 4 letters, and is not in a small stoplist (string, thing, during, …) |
| slot_improve, slot_reveal, slot_exploit | float 1/0/NaN | 1 = LLM-favoured variant, 0 = neutral variant, NaN = slot not filled. Opener-based, with the pre-V2 sense filter applied (NaN for 1 'Boosting' as algorithm and 7 LM/neural 'Decoding' titles) |
| slot_*_raw | float | same without the sense filter |
| slot_*_al | float | same using opener_word_al (no sense filter) |
| slot_study_adj (= slot_study_adj_raw) | float | first match anywhere in the title of {comprehensive (1) / systematic, extensive, large-scale (0)} followed by a study noun. Pilot regex: no trailing word boundary, so plural forms match |
| slot_study_adj_word | str | matched adjective |
| slot_word, slot_name | str | opener slot word and slot name ('' if none) |
| slot_sense_flag | str | sense rule that fired (boosting_algorithm / decoding_lm / decoding_neural) for slot words |
| slot_word_in_abstract, slot_study_adj_word_in_abstract | float 1/0/NaN | the abstract contains the same lemma (`lexicons.slot_word_stems`). Use this for the "exclude titles whose abstract has the verb" robustness check |
| slot_any_filled | bool | any of the four slots filled |
| ctrl_towards, ctrl_novel, ctrl_via | float 1/0/NaN | control pairs, decided by the first occurrence in the title: towards (1) vs toward (0); novel vs new; via vs using |

Slot words per lexicons.json (PLAN D3):
- improve: {enhancing, boosting, advancing, elevating, empowering} vs {improving}.
- reveal: {unveiling, uncovering, unraveling, unravelling, demystifying, decoding} vs {understanding, analyzing, analysing, investigating, characterizing, characterising, explaining}.
- exploit: {leveraging, harnessing, unleashing, unlocking} vs {exploiting, utilizing, utilising, enabling}.
- The British spellings unravelling, characterising and utilising were added; they affect 7 titles.

Filled counts (all years):

| slot | `slot_*` | `slot_*_al` |
|---|---|---|
| improve | 984 | 1,124 |
| reveal | 525 | 577 |
| exploit | 451 | 524 |
| study_adj | 111 | n/a |

### 4.4 Register families and fingerprints

| column | type | definition |
|---|---|---|
| r24_enhanc, r24_leverag, r24_unveil, r24_unleash, r24_harness, r24_empower, r24_elevat, r24_boost | bool | R24 stems (`\bstem\w*`) in title |
| r24_n, r24_any | int/bool | count and any of R24 |
| r26_unified, r26_unifying, r26_beyond, r26_bridging | bool | R26 words in title |
| r26_n, r26_any | int/bool | count and any of R26 |
| f24_n | int | number of distinct RARE21 words in the abstract (scout list: delve, intricate, showcase, pivotal, underscore, realm, meticulous, commendable, innovative, garner, harness, encompass, noteworthy, unveil, bolster, adept, formidable, endeavor, groundbreaking, multifaceted, unparalleled; inflections per lexicons.json) |
| f24 | bool | **F24** = f24_n ≥ 1 |
| f24_2 | bool | f24_n ≥ 2 (D1 variant) |
| f24_words | str | matched RARE21 words, '|'-joined |
| f26_words_n, f26_words, f26_words_list | int/bool/str | {principled, refram(e/es/ed/ing), genuine(ly/ness), brittle, auditable, sharply, high-stakes} in the abstract |
| title_nbhyphen, abs_nbhyphen | bool | U+2011 in the raw title / abstract |
| title_endash_compound, abs_endash_compound | bool | letter–en dash–letter in the raw title / abstract |
| title_emdash, abs_emdash, abs_emdash_n | bool/bool/int | em dash (D4 L set) |
| f26_typo | bool | U+2011 or en-dash letter compound in title or abstract |
| f26 | bool | **F26** = f26_words or f26_typo |
| title_typo | bool | title typography = v1 `LLM_TYPO` on the RAW title |
| llm_typography_v1 | bool | v1 value (computed after NFKC; misses U+2011). Reference only |
| F_any | bool | **F** = f24 or f26 or title_typo |

### 4.5 LLM mentions (abbreviation features)

| column | type | definition |
|---|---|---|
| llm_t_abbrev / llm_a_abbrev | bool | title / abstract contains LLM(s), VLM(s), MLLM(s), LVLM(s), LMM(s), SLM(s) or LM(s) (case-sensitive) |
| llm_t_spelled / llm_a_spelled | bool | "language model(s)" spelled out (any case, hyphen or space) |
| llm_t_named / llm_a_named | bool | named model (GPT-n, ChatGPT, LLaMA/Llama, Claude, Gemini, Mistral, Qwen, DeepSeek, PaLM) |
| llm_t_abbrev_only / llm_a_abbrev_only | bool | abbreviation and not spelled out (D4 atlas "LLM abbreviation-only share") |
| llm_t_any / llm_a_any | bool | any of the three |

### 4.6 D2 style markers (frozen, 61)

- Columns are named `mk_<name>`, defined in `lexicons.json → d2_style_markers` and all boolean.
- **Forms:** name, name_strict, name_loose, compound, phrase_colon, title_case, sentence_case, name_mixed_case, name_all_caps, name_word, name_paren_acronym, question, quoted, gerund_opener.
- **Hyphen suffixes:** aware, free, guided, based, driven.
- **Register words (anywhere in title):** enhanc, leverag, unveil, unleash, harness, empower, elevat, boost, unlock, bridg, unif, beyond, rethink, revisit, towards, via, using, through, demystif, navigat, mitigat, comprehensive, simple, effective, meets, really.
- **Snowclones (v1 templates):** all_you_need, less_is_more, devil_in, lost_in, tale_of, rule_them_all, free_lunch, at_scale, when_meets, worth_a_thousand, is_secretly, a_simple, on_the, learning_to, matters, empirical_study.
- Eight snowclones have prevalence below 0.1%. Weight by n, or drop them by a pre-stated minimum count, in H2d.

### 4.7 Name-mask diagnostics (V4)

| column | type | definition |
|---|---|---|
| lead_in_abstract | bool | the lead pattern occurs in the abstract (88.5% of NAME papers) |
| mask_lead_hits | int | lead occurrences replaced |
| mask_token_hits | int | CamelCase/ALLCAPS tokens replaced |
| lead_survives_mask | bool | `lead_raw` (case-insensitive, whole word) still in the R3-masked abstract. **0 of 12,962 NAME papers** (2017–26; 0 of 12,928 in 2018–26, the denominator VALIDATION V4, D1 and SUMMARY use) |

## 5. Topics and encoders (`outputs/topics/`)

| file | content |
|---|---|
| `topics_bge.parquet` | submission_id; `topic50_bge`, `topic100_bge` (KMeans with n_init=4, random_state=0 on bge-small 512-token abstract embeddings of U); `llm_cluster_bge` (more than 50% regex rule on bge topic100; 20 clusters in `llm_clusters_bge.json`); `llm_topic_bge` = llm_regex OR llm_cluster_bge |
| `centroids.npz` | `bge_k50`, `bge_k100` (KMeans centres); `minilm_k50`, `minilm_k100` (per-label means of MiniLM embeddings; these reproduce the cache labels for 100% of rows); `note`. Assign held-out papers with `C.assign_centroids(E, C.load_centroids('minilm_k100'))` |
| `topic_stability.csv` | ARI/NMI of MiniLM vs bge: k50 ARI 0.470 / NMI 0.642; k100 ARI 0.421 / NMI 0.666 |
| `llm_cluster_agreement.csv`, `llm_flags_by_year.csv` | agreement among the regex, MiniLM-cluster and bge-cluster LLM flags. MiniLM vs bge cluster flag: κ = 0.78. The union flags: κ = 0.93 |
| `central_papers_k100.csv` | 20 most central papers per topic100 cluster (MiniLM and bge), for V5 labelling |
| `masked_abstracts.parquet` (+ `.sha256`) | 2018–26 U abstracts after `mask_abstract` (R3 text), with lead and token hit counts |
| `emb_masked_bge.npy`, `emb_masked_bge_ids.npy` | float16, L2-normalised bge-small (max_seq_length 512) embeddings of the masked abstracts (43,098 rows, 2018–26). Written by the background job; `embed_masked.done` appears when finished. Progress is in `embed_masked.log`. Load with `C.load_masked_embedding(df)` |

## 6. Public functions

### `analyses._core`

**Constants**
- `YEARS`, `PRE`, `PRE_WD`, `POST`, `POST_EXCL_2026`, `EARLY`, `LATE`, `BREAK_YEAR`.
- `LLM_TOPIC_REGEX`, `LLM_CLUSTER_THRESHOLD`.
- `CONTROLS_BASE = ['log_authors', 'llm_topic']`.
- `CONTROLS_EXP = ['max_prior_subs', 'max_prior_accs', 'share_new_authors', 'last_prior_accs']`.
- `AREA_CROSSWALK_2024`, `AREA_SHORT`.
- Paths: `CORE`, `FEAT_DIR`, `TOPIC_DIR`, `UNIVERSE_PATH`, `FEATURES_PATH`, `TOPICS_BGE_PATH`, `CENTROIDS_PATH`, `MASKED_EMB_PATH`, `MASKED_IDS_PATH`, plus `OUT`, `CACHE`, `DATA` re-exported from `common`.

**Universe, pools and periods**
- `build_universe()` → `(universe_df, counts_df, llm_cluster_meta)`. `main()` writes the files.
- `pool_flags(submissions_df)` → pool and stage booleans for any submissions subset.
- `period_columns(year)` → `post`, `t`, `period`.
- `year_mask(year, which)` → boolean mask for a named year set.
- `harmonise_area(area, year)` → harmonised area label.
- `area_crosswalk_table()` → the crosswalk with counts.
- `llm_regex_flag(title, abstract)`.
- `llm_clusters(topic, llm_regex, threshold=0.5)` → list of cluster ids.
- `placeholder_reason(title, abstract)`.
- `nfkc(text)`.
- `rx_contains(s, pattern, flags=0)`, `rx_extract(s, pattern, group=1)`, `rx_count(s, pattern)`: Python-`re` regex on Series.

**Loaders**
- `load_universe(columns=None)`.
- `load_features(columns=None)`: always includes submission_id.
- `load_topics_bge()`.
- `load_analysis_frame(feature_cols=None, universe_cols=None, with_bge_topics=False)`: a 1:1 merge on submission_id; duplicate feature columns are dropped in favour of the universe.
- `load_embedding(df, field='abstract'|'title', model='bge-small-en-v1.5'|'all-MiniLM-L6-v2')` → float32 array aligned to `df.emb_row`.
- `load_masked_embedding(df)` → `(E, found)`.
- `load_centroids(name)`.
- `assign_centroids(E, C)` → nearest centroid (Euclidean, as in KMeans).

**Controls**
- `controls(df, experience=False, log_counts=True)` → control column names.
- With `experience=True`, it adds `lmax_prior_subs`, `lmax_prior_accs`, `share_new_authors` and `llast_prior_accs` (raw counts if `log_counts=False`). It raises if any year < 2022.
- Title length is never a control in trend models.

**FE linear models (LPM)**
- `demean(X, fe_list, weights=None, tol=1e-10, maxiter=10000)`: alternating-projection within transform. Exact in one sweep for a single FE.
- `feols(data, y, x, fe=None, cluster=None, weights=None, vcov=None)` → `FEResult`.
  - `FEResult` exposes `.params`, `.se`, `.vcov`, `.tstat`, `.pvalue`, `.conf_int(level)`, `.summary()`, `.nobs`, `.n_clusters`, `.df_resid` and `.r2_within`.
  - `vcov` is `'CRV1'` (the default when `cluster` is given), `'hetero'`/`'HC1'` or `'iid'`.
  - The small-sample factor is (N−1)/(N−K)·G/(G−1), where K counts the slopes plus FE levels not nested in the cluster. p-values use t(G−1). This matches pyfixest defaults: the smoke test shows coefficient differences below 1e-14 and SE differences below 3e-7, for one- and two-way FE.
  - Rows with NaN in any used column are dropped. Interact FEs beforehand with `fe_interact(df.topic100, df.year)`.
- `pf_feols(fml, data, vcov=None, **kw)`: thin wrapper around `pyfixest.feols`. pyfixest 0.60.0 is installed in `/home/user/venv`; `HAS_PYFIXEST` flags it. Example: `pf_feols('y ~ F + log_authors | topic100^year', df, vcov={'CRV1': 'topic100'})`.

**Logit**
- `logit(formula, data, cluster=None, maxiter=300, method='newton', freq_weights=None)`: a patsy-formula `sm.Logit` with cluster-robust SEs. Missing rows are dropped consistently with the cluster column. Falls back to BFGS when Newton fails. `.model_rows` gives the rows used.
- `or_table(res, terms=None, level=0.95)` → coef, se, z, p, lo, hi, OR, OR_lo, OR_hi, nobs.

**Bootstrap**
- `boot_weights(n, n_boot, strata=None, clusters=None, seed=0, chunk=200)` yields (b × n) frequency-weight matrices: a paper or cluster bootstrap, stratified when strata are given.
- `boot_means(values, n_boot=2000, strata=None, clusters=None, seed=0)` → (n_boot × k) bootstrap means. NaN is treated as missing. Vectorised.
- `boot_indices(n, strata=None, clusters=None, rng=None)` → one draw of row indices.
- `bootstrap(data, stat, n_boot=1000, strata=None, cluster=None, seed=0)` → generic loop; `stat(df)` returns a float or an array.
- `percentile_ci(samples, level)`.
- `boot_summary(est, samples, level)` → est, se, lo, hi, p_le0.

**Figures** (the PLAN figure style)
- Constants:
  - `COLORS` holds the 8 categorical colours in their fixed order; `color(i)` raises an error past 8 rather than cycling.
  - Other colours: `GREY` (#8a8984, for controls and reference series), `TEXT`, `TEXT2`, `GRID`, `BG`.
  - `DIVERGING`; `diverging_cmap()` builds blue ↔ grey ↔ red.
- `set_style()` sets the rcParams:
  - Inter font (DejaVu Sans fallback), 8–9 pt.
  - No top/right spines; light grid at 0.6 pt.
  - 2 pt lines, 5 pt markers; PDF fonttype 42.
- `new_fig(width='single'|'double'|inches, height=None, nrows=1, ncols=1)` creates a figure at 3.4 in (single column) or 7 in (double column).
- `label_end(ax, x, y, text, color)` adds a direct label at the end of a series.
- `forest(ax, labels, est, lo, hi, ref=1.0, log=True, colors=None)` draws a forest plot.
- `save_fig(fig, name, folder, data=None, close=True)` writes `<OUT>/<folder>/<name>.pdf`, `.png` (300 dpi) and `.csv`.
  - A dict passed as `data` writes `<name>__<key>.csv` files.
  - A relative folder resolves under `outputs/`.

### `analyses.features_v2`

**Lexicon**
- `lexicon()`: the frozen lexicons.json as a dict.
- `sha256(path)`.
- `write_hashes(path)`.

**Builder**
- `build(u)` → features DataFrame for universe rows; needs submission_id, year, title, title_nfkc and abstract.

**Name masking**
- `mask_abstract(abstract, lead, token='[NAME]', min_len=3, return_counts=False)`: the **R3 mask**.
  1. Every occurrence of the title's compound lead is replaced. Matching is case-insensitive and hyphen-optional, and LaTeX in the lead is matched. For "(ACR)" leads the acronym and the long form are also replaced.
  2. Every CamelCase or ALLCAPS token is replaced: an alphanumeric token whose hyphen-piece has at least 3 characters and either ≥ 2 capitals or a lower→upper transition, e.g. GPT-4, LLaMA-2, ImageNet, MMLU. 'In-Context', 'RL-based' and 'U-Net' are kept.
  - The lead is masked for all compound titles, not only NAME titles.
- `mask_abstract_lower(abstract, lead)`: the **R1 mask**. It drops the lead (same patterns) and keeps only all-lowercase tokens `[A-Za-z][A-Za-z-]+`.
- `lead_patterns(lead)` → compiled regexes.
- `raw_lead(title)` → lead with LaTeX kept.
- `lead_survives(masked, lead_raw)` → V4 check.

**Title helpers**
- `name_variants(lead, name_colon)`.
- `opener(title_nfkc, lead, rest, name_colon)`.
- `first_word(text)`.

### `analyses.topics_bge`, `analyses.embed_masked`, `analyses.smoke_test`

These are scripts (`main()`). `embed_masked.masked_table()` returns the masked-text table. `MIN_YEAR = 2018`.

## 7. Deviations from PLAN.md and pilots (logged)

1. **`llm_topic` is the §0 union.** It is regex OR an LLM cluster. In `cache/title_features.parquet`, `llm_topic` is regex-only; that version is kept here as `llm_regex`. The pilots used regex-only.
   - The 20 MiniLM LLM clusters include pre-LLM NLP: they contain 5–8% of 2017–2022 papers, while the regex flags 1.5–4%. The non-LLM subset therefore also drops older language-model/NLP papers.
2. **v1 typography bug.** `features.title_features` computes `llm_typography` after NFKC, which rewrites U+2011 as U+2010. It therefore misses non-breaking hyphens: 60 titles, all in 2026.
   - v2 `title_typo` uses the raw title: 210 titles in 2026, against 155 in v1.
   - The v1 value is kept as `llm_typography_v1`. `features.py` was not edited.
3. **Slot opener.** Per the PLAN text, the opener comes after an optional **NAME** lead. The H3a pilot (`design/pi/slot_power.py`) used any colon lead of 40 characters or less.
   - Primary slot n (all years): 2,071.
   - The `_al` variant, using any compound lead, gives 2,336, close to the pilot's 2,362 (2018+).
   - D3 should choose and state which is primary.
4. **Slot inventory.**
   - The British spellings unravelling, characterising and utilising were added (7 titles).
   - A heuristic pre-V2 sense filter blanks 8 titles: 1 'Boosting Methods…' and 7 LM- or neural-decoding 'Decoding…' titles. Raw columns keep them.
   - V2 drops must be recorded in `outputs/validation/`, not by editing lexicons.json.
5. **study_adj** keeps the pilot regex: no trailing word boundary, so plural and -ing forms of the study nouns match.
6. **R24 = the stems in the PLAN** (enhanc*, …, boost*), so enhanced and enhancement count. The vintage pilot used -ing forms only.
   - enhanc* per 1k titles: 2024 26.5, 2025 40.3, 2026 29.8 (pilot: 36.7 → 25.6 for 2025 → 2026).
   - boost* also matches the algorithm sense, and elevat* matches elevation.
7. **RARE21 is the scout list** (`scout_abstract-llm-vocab/lexicon.py`: RARE plus the FAM regexes), unambiguous at 21 words. It reproduces the scout shares: 19.15% (2024) and 9.15% (2026, scout 9.14%).
   - The vintage pilot (`design/pi/vintage_check.py`), behind the H3c pilot ORs, used a different 19-term regex (with tapestry, boast, invaluable, seamless, surpass, notabl*). H3c numbers will not match the pilot exactly.
8. **F26 words.**
   - `reframe*` is implemented as refram(e|es|ed|ing); the pilot's `reframe\w*` missed "reframing".
   - genuine covers genuine/genuinely/genuineness.
   - high-stakes accepts any hyphen character.
   - Word lists run on the NFKC lower-cased abstract. The scout used the raw lower-cased abstract; F24 is unchanged.
9. **Masking.**
   - The lead is removed for every compound title, case-insensitively. The R1 pilot used case-sensitive `str.replace`.
   - **Leakage caveat for R3:** the "[NAME]" token itself carries signal. A NAME paper whose lead is a plain word (e.g. 'Chameleon') gets extra [NAME] tokens. D1/V4 should report the masked-vs-unmasked AUC gap and could compare a token-deletion variant (`mask_abstract(..., token='')`).
10. **Area crosswalk judgement.** The 2024 label 'metric learning, kernel learning, and sparse coding' (26 papers) maps to representation learning.
    - The 2024 labels 'societal considerations…' and 'visualization or interpretation…' map to the broader 2025 labels.
    - 'Foundation or frontier models' and 'time series' have no 2024 counterpart. Prefer year×area FE (the PLAN default) over pooled area FE.
11. **`wd_post`** follows the PLAN (2026 only, 349 rows). Another 306 withdrawn rows also carry an accept/reject decision: 300 from 2018–2025 and 6 accepted ones from 2026. They are flagged `wd_decided` for sensitivity.
12. **Version lock.** `features.py` is locked by SHA-256 content hash, not a commit hash, because git is not run here.
13. **Topics.**
    - The bge KMeans was fitted on U (43,482 rows). The cached MiniLM topics were fitted on all 43,516 rows; they are kept unchanged for comparability with the pilots.
    - MiniLM centroids are label means, since the fitted model was not cached.
14. **Masked embeddings** cover U papers from 2018–26 (43,098 rows). They are encoded in length-sorted chunks (order restored on save) using the bge-small max_seq_length of 512.
