# Claude handoff: released former-confirmation corpus

The requested data is now in this repository on `claude/clever-edison-oe9pzv`, under `data_confirmation/`. No access to the private source repository or the user's Windows machine is required.

## Start here without examining outcomes

1. Read this document, `export_manifest.json`, `policy.json` and `TRANSFER_RECEIPT.json`.
2. Inspect table column names/counts in the manifest. Outcome-bearing data is present: `decision`, `decision_evidence`, `outcome_eligible`, plus numeric scores and review/discussion text. Do not load these values merely to confirm receipt.
3. Run `python -B data_confirmation/verify_delivery.py` from the repository root. It hashes sealed files as bytes and does not decode scientific rows or outcome values. The original `verify_download.py` additionally parses the records, so use the hash-only verifier first if the current protocol requires outcome blinding.

This is **11,113 original former-confirmation submissions**, not a second copy of the 43,516 discovery submissions already in `data/`. It includes all years 2017-2026, all existing administrative statuses, 69 compressed JSONL shards and the documented module eligibility flags. Pending family/link cases remain excluded. For acceptance analyses, withdrawals and desk rejects must not automatically become rejections.

## Important status and schema differences

The source access policy explicitly sets `independent_confirmation_available=false`. The user previously authorized release for exploratory access and publication. Original `split='confirmation'` labels remain as provenance, not as a new certification of an untouched independent holdout. Exposure and release status are documented in `policy.json` and `exposure_receipt.json`. This transfer does not itself analyze scientific outcomes or modify the current study's preregistration. Assess exposure history before making an independent-confirmation claim; do not retroactively change this history.

The original `data/` export is unchanged. Its CSV schema is different from this JSONL package: new submission keywords are the existing source values, not newly approved spelling/concept assignments. Existing discovery-only topic, contribution-type and foundation-model annotations were not automatically assigned to the new submissions. Do not fill missing controls with zero or silently append these records to the discovery CSVs. No decision about relabeling, model calls or a reduced-control specification was made by this transfer.

Join on stable `submission_id`/`family_id`; selected score/graph observations use `oid`. Preserve original source and eligibility fields. Numeric rating dimensions are year/form-specific. The data dictionary and original methods are in `README.md`. Some original reproduction links refer to the source project's layout and database; those inputs are not needed to read this standalone export or run `verify_delivery.py`.

## Retrieval options

- Branch folder: https://github.com/theBEST-git/cloud-research/tree/claude/clever-edison-oe9pzv/data_confirmation
- Public ZIP: https://github.com/theBEST-git/cloud-research/releases/download/released-former-confirmation-20261018-v1/released_confirmation_2017_2026_20261018_v1.zip
- ZIP SHA-256: `a8c79acc5a1f34166189a2596382cc98a173db8d22c07cde0e8ff1ea6ac223b7`.

If this cloud checkout predates the transfer, fetch `origin/claude/clever-edison-oe9pzv` and update safely while preserving local work. The public ZIP also works without GitHub App access or a token. Do not place any personal access token into the cloud chat.

The source release files were copied byte-for-byte and their SHA-256 values checked. Delivery notes and the hash-only helper are additions outside the original source seal. No manuscripts, credentials, newly acquired data, new labels or new scientific results were added.
