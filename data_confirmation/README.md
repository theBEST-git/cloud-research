# Released former confirmation corpus — 18 October 2026

The project user explicitly authorized exploratory use and GitHub publication of the original held-out population. **11,113 submissions are released; the enlarged local exploratory corpus contains 54,629 submissions.** The 1,309 pending family/link cases remain excluded. The former split is no longer an untouched independent confirmation set.

Original databases, source splits, eligibility flags, exposure history and sealed analytical releases are unchanged. This release adds a permission layer and a compressed export; it does not rerun keyword, acceptance, area or research-fashion analyses. The approved keyword preprocessing still covers only the original 43,516 discovery submissions.

## Contents

`released_data/*.jsonl.gz` contains one canonical UTF-8 JSON object per line, with deterministic gzip metadata. `export_manifest.json` lists all tables, columns, row counts, files and checksums. No external database or Python package is needed to read it.

| Table | Included records | Main identifiers |
|---|---|---|
| submissions | All 11,113 released submissions, with existing metadata, title, abstract, keywords, primary area, administrative status, corrected outcomes and source eligibility | submission_id, family_id, metadata_oid |
| notes | Selected existing observations only (`is_primary=1`): reviews, discussion, meta-reviews, decisions, administrative notes and title/abstract submission notes | oid, submission_id, native_key, source_id, nid |
| scores | All selected-observation numeric-score records, including missing/invalid/ineligible states; no missing value is filled | score_id, oid, submission_id, dimension |
| edges | Graph entries for selected observations; missing-parent, topology and time restrictions retained | oid, submission_id, parent_nid |
| score_changes | Existing reconstructed/source-comparison pair records for released papers; ineligible records retained for coverage, separately identified | pair_id, source_oid, official_oid, before_score_id, after_score_id |
| selection_ledger | Existing selection/provenance metadata for observations of released papers; no additional historical text | oid, chosen_oid, status |
| issues | Existing cleaning/eligibility issue metadata for released papers | issue_id, submission_id, oid |

Raw JSON-valued columns such as `keywords`, `clean_sections`, `original_sections`, `form_ids` and `raw_json` retain their source string representation; parse them separately when required. Empty strings, JSON null, missing-value flags and eligibility reasons are not reinterpreted.

Join submissions to other tables on `submission_id`; join selected score and graph records to notes on `oid`. Use `family_id` for related-paper handling. Native note IDs are not global observation identifiers. Missing graph parents, metadata references or reconstructed-pair source IDs can refer to observations outside the selected export; do not silently invent a matching row. The pair table retains its before/after values and provenance together and is not a replacement for official snapshot ratings.

The export contains no PDF/manuscript text, local credentials, new acquisition, new model outputs or unselected prose histories. Submission-note text is the existing title/abstract representation, not the paper body. Local source paths in provenance are historical identifiers, not downloaded files included in this package.

## Read or verify a GitHub download

Download/clone this directory with all adjacent data shards. From this directory:

```powershell
python -B verify_download.py
```

This verifies every published file, row count, unique key and released-population membership without the multi-gigabyte source database. To read a table:

```python
import gzip, json
from pathlib import Path
for path in sorted(Path('released_data').glob('submissions-*.jsonl.gz')):
    with gzip.open(path, 'rt', encoding='utf-8') as stream:
        for line in stream:
            submission = json.loads(line)
            # Analyze only fields and records eligible for your chosen module.
```

The preserved `split='confirmation'`, `discovery_allowed=0` and `confirmation_allowed=0` record the original policy. For this export, `analysis_allowed=1` and `released_from_confirmation=1` on submissions record the new authorization. Join that permission to the observation tables rather than filtering them out using the old flags. The published shards contain only the newly released population, not the original discovery corpus.

## Local access and reconstruction

See [active access instructions](../CORPUS_ACCESS.md) and `../corpus_access.py`. Pass `--corpus-root` if the source repository is outside the default location. Required sources are the existing sealed `eda_ready_20260913T143255Z` corpus and `outcome_repair_20260923T104907Z` outcome correction; no data is downloaded.

For an unsealed new output copy, the production sequence is:

```powershell
python -B corpus_access.py build --corpus-root <local-corpus-root>
python -B test_access.py
python -B test_export.py
python -B export_released.py export --corpus-root <local-corpus-root>
python -B export_released.py validate --corpus-root <local-corpus-root>
python -B corpus_access.py seal --corpus-root <local-corpus-root>
python -B corpus_access.py validate --corpus-root <local-corpus-root>
python -B verify_download.py
```

Do not rebuild into this sealed directory. The export resumes completed tables after checksum verification and refuses concurrent export runs; incomplete-table shards are deterministically rewritten. A stale lock after a hard process crash requires verifying that its owner has exited before removing it. Successful output is validated against the read-only source, not merely against an earlier model output.

The source connection attaches immutable read-only SQLite files, creates temporary in-memory views, and blocks network operations in build/export/validation commands. The export streams one record at a time, uses a 32 MiB uncompressed shard target and a 48 MiB compressed-file ceiling, and requires at least 50 GiB free space before starting. Source receipts verify the consumed small sealed files and 2019 correction, plus recorded clean-database hash/size/mtime/WAL; **this is not a fresh checksum audit of the entire raw corpus or 11 GiB database**.

## Eligibility and interpretation

New access is not a blanket quality certificate. Continue using selected observations, valid dimensions and scales, reliable within-paper reviewer identities, year/form-specific scores, minimum reviewer counts, module-specific missingness and outcome eligibility. Withdrawals and desk rejects are not automatically rejections. Author-specific 2017 and timing-specific 2018 restrictions remain. The existing sealed correction supplies 2019 outcomes. Retain 2026 as an identifiable cohort when analysis requires process or score comparability. Do not infer causal effects, reviewer identity across papers or verified scientific quality.

`access_ledger.csv` covers all 55,938 submission identities and records why 54,629 are accessible and 1,309 remain restricted; it is not a substantive data table. `coverage_by_year.csv`, `summary.json` and `live_access_check.json` reconcile the access counts. `exposure_receipt.json` retires the original holdout claim. Tests, validation, source receipts, runtime identity and initial Git status are adjacent. Pre-existing unrelated uncommitted work is preserved and excluded from this publication.

## Publication limits

The destination is the existing private repository `theBEST-git/sci-research-project`, branch `codex/keywords-topic`. [GitHub documents](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) a warning above 50 MiB and a block above 100 MiB per regular Git file; [one push is limited to 2 GiB](https://docs.github.com/en/get-started/using-git/troubleshooting-the-2-gb-push-limit). The exact measured package and largest shard are recorded in the manifest and publication checks. Git LFS and paid storage are not required for this export.

## Measured export

69 compressed shards; **261.82 MiB total**, largest 8.68 MiB. The export contains 856392 rows across seven tables. These are different counting units and must not be summed as papers.

| Table | Rows |
|---|---:|
| submissions | 11,113 |
| notes | 174,402 |
| scores | 192,933 |
| edges | 174,402 |
| score_changes | 67,607 |
| selection_ledger | 174,402 |
| issues | 61,533 |
