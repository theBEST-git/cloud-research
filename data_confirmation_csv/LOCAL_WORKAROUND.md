# Released former-confirmation submissions in discovery CSV format

This directory contains 11,113 released former-confirmation ICLR submissions from 2017-2026, exported using the existing `scripts/export_dataset.py`. The three CSV headers are unchanged. Original `data/`, `data_confirmation/`, scripts, analyses and preregistration were not modified.

## Local selection/validation workaround

The sealed clean database has **zero** rows with `confirmation_allowed=1`. The 11,113 released records retain `split=confirmation`, `discovery_allowed=0`, `confirmation_allowed=0`. No database flags were changed.

`export_released_confirmation_csv.py` loads the unchanged exporter (pinned SHA-256 in `adapter_reproduction.json`) and makes two runtime-only adaptations:

1. The confirmation SQL predicate selects the exact frozen released IDs, with source split `confirmation`. IDs are independently reconciled between `data_confirmation/access_ledger.csv` and the JSONL submission shards; only identifier values are decoded for this reconciliation.
2. The validator's single access-flag guard checks membership and the unchanged per-ID source flags, instead of demanding `confirmation_allowed=1`. All its remaining checks are retained.

No AUTHOR_FIELDS, field construction, canonicalization, author-key hashing, email suppression, outcome correction, keyword assignment, storage limit or free-space reserve was changed. The key remains `native_ + sha256(canonical(["declared-id-v1", raw_id]))`, with no salt. Existing keyword assignments are reused only where present; missing assignments are not invented. The original manifest's split description is preserved for compatibility; source policy does not certify an untouched independent holdout.

The first export and the final build from the repository root produced byte-identical gzip tables. Source preservation is checked by the original exporter's receipts (small sealed files rehashed, large databases checked via existing seals/size/mtime); this is not a fresh checksum audit of the entire source databases.

## Reproduce / validate

Run from the repository root, supplying the existing local sealed inputs:

```text
python -B data_confirmation_csv/export_released_confirmation_csv.py build --script scripts/export_dataset.py --clean <eda.sqlite> --upstream <corpus.sqlite> --patch <outcomes.sqlite> --keywords <submission_keywords.csv> --output <new-directory>
python -B data_confirmation_csv/export_released_confirmation_csv.py validate --script scripts/export_dataset.py --output data_confirmation_csv
python -B data_confirmation_csv/check_confirmation_csv_ids_keys.py
```

Build refuses to overwrite an existing output directory. The identity/count/key-only check uses the existing discovery CSV files for disjointness and cross-split author-key linkage; it does not inspect or report outcome values. `id_key_checks.json` and `author_coverage_by_year.csv` contain checks a-e requested by the user. No outcome analysis, annotation, external data acquisition or model call was performed.
