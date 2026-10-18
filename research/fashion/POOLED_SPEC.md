# Integration spec: confirmation papers + pooled corpus (binding for every implementer)

Repo: /home/user/cloud-research. Venv python: /tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/venv/bin/python
Detailed subsystem maps (read the part for your component): /tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/final_round/pipeline_map.json

## Data
- Discovery: data/{submissions,submission_authors}.csv.gz; 43,480 papers with text; embeddings research/topics/cache/specter2.npy (+ specter2_ids.csv, order = sort by (year, submission_id)).
- Confirmation (released former holdout, 11,113; 11,099 with text >= 30 words): data_confirmation_csv/{submissions,submission_authors}.csv.gz (same schema as data/; normalized_keywords_json is missing; raw `keywords` present); embeddings research/topics/cache/specter2_released.npy (+ specter2_released_ids.csv, same order rule); labels research/topics/output/paper_contributions_released.csv.gz (same columns as paper_contributions.csv.gz; 100% coverage).
- Author keys link across splits (same unsalted hash). Authorised by the user for this analysis; never print, export or commit names/ids beyond what the existing analyses do; outputs are aggregates.

## D1. Switch
Environment variable ICLR_CORPUS in {unset|"discovery", "pooled"}. Unset => every path and behaviour byte-identical to today (all existing tests must still pass unchanged).
- research/topics/common.py when pooled: OUTPUT = research/topics/output_pooled. load_corpus() returns the union of CONTENT_COLUMNS from data/ and data_confirmation_csv/ plus a `split` column ("discovery"/"confirmation"), keywords = original normalized lists for discovery, keyword_map.normalize(raw) for confirmation; has_text as now. embedded_corpus() as now. load_embeddings() returns (vstack reindexed to pooled embedded order, ids). CACHE unchanged.
- research/fashion/common.py when pooled: TOPICS = research/topics/output_pooled; OUTPUT = research/fashion/output_pooled; DATA = research/fashion/output_pooled/inputs (git-ignored; holds submission_authors.csv.gz = discovery ∪ confirmation author rows, built deterministically by a script; its sha256 is recorded). Add module constant CORPUS. Assert OUTPUT != discovery output when pooled.
- POOLED ORDER P: stable sort of the union by (year, submission_id). Every pooled file is written in P order (embedded papers: 54,579 rows). Assert that the discovery subset of P equals the discovery order.

## D2. Topics for new papers (maps frozen; never refit PCA or maps)
- k100/fine/coarse: assign_topics.project + assign_projected with output/topic_model.npz (pre-registered). Discovery rows copied verbatim after asserting reproduction.
- Alternative maps (k75, k150, k50, k200 if cheap; balanced, early, middle_era, late; seed_refit): recover the EXACT frozen KMeans centroids by re-running the deterministic fits (same seeds, n_init, weights, era subsets) on discovery z; gate: argmax labels on discovery == saved labels (np.array_equal). New papers: argmax z·normalize(centres), raw integer label as saved. If a gate fails: fallback = normalised (weighted) mean of the map's FIT-POPULATION discovery members; log agreement. Report the share of new papers whose label differs between exact centres and fit-population member means.
- Stability (stable_papers variant): re-derive refits REFIT_SEEDS (mid level, as evaluate_topics.fit_hierarchy), assert discovery mid_stability reproduces exactly; new papers: label under each refit's exact centres, stay vs matched() best map frozen from discovery; mid_stability, stable as defined. Fallback: NaN (logged).
- mixed_topic / catalog inherited through k100 code; copy topic_catalog.csv, keyword_types.csv, topic_model.npz, hindsight_check.json byte-identically.

## D3. Keywords for confirmation papers
Lookup table T learned only from discovery (raw `keywords` vs normalized_keywords_json), rule in pipeline_map.json "Author keywords" A.1-A.8 (f = lower + collapse whitespace; identity evidence; single-residual pairs; two further passes; majority; ties -> identity, else alphabetical). Unseen forms keep f(raw). No ';' splitting. Discovery lists are never re-normalised. Write output_pooled/keyword_map.csv.gz + keyword_map_report.json (sha256, in-sample replication, 3x 80/20 CV recall/precision for V759, the 68 PH4 keywords and 'federated learning').

## D4. Labels
Pooled paper_contributions.csv.gz = discovery table ∪ released table in P order; assert 0 NaN in primary_type, primary_class, foundation_model, uncertain.

## D5. Fashion features (pooled; unchanged builders)
Under ICLR_CORPUS=pooled run topic_maturity, resubmissions (BUT load the frozen discovery output/specter2_centring_mean.npy and tau 0.90; never recompute or overwrite the mean), buzzwords (frozen 759 vocabulary; never write discovery outputs), variables. Copy h2d_validation.json, resubmission_tau.json, specter2_centring_mean.npy byte-identically into output_pooled. ph5_position.embeddings must use topic_layer().load_embeddings() (so it follows the switch). Guards: discovery rows' team_size/has_author_key identical to discovery; 54,579 rows per map; 0 NaN topics/labels; git status of research/*/output and every FREEZE-listed file unchanged.

## D6. Outcomes and runs
- outcomes.py: SOURCES {discovery: data/..., confirmation: data_confirmation_csv/...}; split-aware cached table read; `_read(ids, split)` refuses ids outside the split; real mode dispatch by entry script: run_frozen.py -> discovery (FREEZE.json), run_confirmation.py -> confirmation (FREEZE_CONFIRMATION.json, all hashes must match), run_pooled.py -> pooled (requires a finished confirmation attempt); posthoc mode under pooled reads pooled and requires the confirmation run to have finished. Keep the lint rules (sealed names only in outcomes.py / tests/test_sealed_loader.py; no 'submissions.csv' string, no literal permuted outside dryrun.py, no helper names that trip the lint).
- run_confirmation.py: activate pooled, run the registered tests ONCE on confirmation papers with pooled features (D14): H1d (rq1 fit, variants), H2b' (+), H2c' (-), H3a (-), H4-FL (primary level, secondary trend), PH5 E1/P1b (primary, Holm over the two) + secondary E4, P7, teams H1, kwtiming A1, premia out-of-sample, all one-sided where registered; attempts log output/confirmation_run/attempts.jsonl; --simulate SEED mode (no guards, simulated outcomes, writes output/confirmation_dryrun/) for plumbing and MDE.
- freeze_confirmation.py: writes FREEZE_CONFIRMATION.json (hashes of code, inputs incl. git-ignored caches and pooled authors file, PREREGISTRATION.md); refuses if a confirmation attempt exists.
- run_pooled.py (exploratory, after confirmation): pooled RQ2/RQ3/E1-E10 via run_frozen.main under the switch; pooled RQ1; posthoc.py under ICLR_CORPUS=pooled for PH1-PH5.
- Never run run_frozen.py, freeze.py, dryrun.py on discovery; never write FREEZE.json or research/fashion/output/{frozen_run,dryrun*,posthoc,figures,rq1_*} or research/topics/output/*.

## Global rules for implementers
- Do NOT read outcome values (decision/acceptance/review fields) of any split; outcomes only via outcomes.py in simulated/permuted test modes on synthetic data. Do not cross-tabulate confirmation labels with newcomer/fm_adoption/acceptance (leakage) — feature builds are fine.
- Do not commit; the lead commits. Do not edit files owned by another component. Match the surrounding code style (dense, documented, same idioms).
- Existing test suites must keep passing with ICLR_CORPUS unset.
