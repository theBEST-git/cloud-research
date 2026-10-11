# Dataset dictionary

Version: `iclr-author-inputs-v1`. No external person matching or influence features
have been added. Rows and existing cleaning assignments are inherited from the
sealed corpus; reading these files does not require any earlier experiment.

## Common keys and encoding

- `submission_id`: reconciled submission instance; primary key in submissions.
- `family_id`: inherited effective paper-family assignment. Several submissions can
  share a family. Do not interpret submission counts as distinct-person or family counts.
- `year`: ICLR conference year, not necessarily writing, posting or capture year.
- `metadata_oid`: selected upstream official submission observation. Joins metadata
  provenance; every author position refers to this entire observation.
- CSV null is `\N`. JSON columns distinguish JSON `null`, empty lists, strings and
  malformed original values. UTF-8 text is not newly rewritten by this export.

## submissions.csv.gz

One row per discovery submission, ordered by year then submission ID.

| Fields | Meaning |
|---|---|
| `forum_ids` | Original forum aliases as an upstream JSON-encoded value |
| `title`, `abstract`, `primary_area` | Existing cleaned metadata; may be missing |
| `keywords` | Original keyword field retained as existing JSON serialization |
| `keyword_field_status` | Structural status: missing/null, empty list/string, text list/string, non-text or invalid JSON; not a semantic error label |
| `normalized_keywords_json` | Existing deduplicated canonical complete-keyword expressions; not inferred abstract topics or broad topic labels |
| `keyword_assignment_status` | Whether an existing frozen keyword-cleaning assignment joined successfully; missingness is preserved |
| `administrative_status` | Recorded ordinary/withdrawn/desk-rejected category accounting; not independently certified final administrative state |
| `decision`, `decision_evidence`, `outcome_eligible` | Observed outcome and its existing evidence/permission; unknown/conflicting outcomes are not rejection |
| `base_decision`, `base_outcome_eligible` | Original sealed clean values, before the additive 2019 correction |
| `outcome_source_release` | Clean release or documented 2019 correction supplying the outcome fields |
| `split`, `split_issue`, `discovery_allowed`, `confirmation_allowed` | Existing effective split and restrictions, preserved unchanged; only discovery is exported |
| `review_count`, `distinct_reviewers` | Existing selected-review accounting; no review bodies or individual numeric scores are bundled |
| `similarity_eligible`, `disagreement_eligible` | Existing module permissions; they are not newly validated by this export |
| `author_metadata_status`, `author_list_status` | Whether selected official metadata exists and its declared lists can be aligned |
| `declared_name_count`, `declared_id_count` | Lengths of native list-valued fields; non-list/missing fields are not forced into lists |
| `cohort` | Inherited main/separate-cohort reference; all years use the same export procedure |

The 2019 outcome exception uses the previously documented meta-review recommendation
rule. The underlying clean database is unchanged. Each corrected row retains base
values and the original correction evidence. Other years' outcomes are unchanged.

## submission_authors.csv.gz

Primary key: `(submission_id, source_list_position)`. Position is zero-based and
preserves the original lists. A list element is a declaration, not a verified author.

| Fields | Meaning |
|---|---|
| `declared_name_json` | Original name-position value serialized as JSON, preserving non-text/null values; email-shaped names are withheld |
| `native_id` | Original non-email string ID, including `~Profile_ID`; not inferred from a name |
| `native_id_kind` | Profile, email, other or missing |
| `declared_id_key` | SHA-256 of the exact original declared ID and a fixed namespace; identical IDs share keys, different IDs are not joined |
| `name_id_alignment` | `aligned_lists` only for nonempty equal-length lists; otherwise these are independent list positions, not verified name/ID pairs |
| `declared_id_state` | Text, non-text, explicit null or absent list position |
| `email_withheld` | At least one email-shaped ID/name at this position was withheld |

No cross-year alias resolution is asserted. Two profiles may belong to one person;
one ambiguous record may not identify any person. Non-list source fields are flagged
and retain their source pointer rather than creating guessed author rows. Names/IDs
are drawn from the selected metadata snapshot, with no fallback that silently combines
different dated observations. Last-author status does not establish a supervisor.

## metadata_provenance.csv.gz

One row for every exported submission, including explicit missing-source statuses.
Native source ID, note ID, snapshot ID and record location refer to the consumed
official observation. `captured`, `acquired`, `capture_status`, `stage_status`,
`creation_ms` and `modification_ms` retain available timing evidence; collection time
does not replace an event date. `content_hash` identifies upstream content.
`source_url`, `source_license` and `source_file_sha256` identify original source
receipts. `author_field_shape`/`authorid_field_shape` distinguish API2 value wrappers,
API1 direct values, absent fields and parse failures.

## Valid joins and analysis population

Join submissions to authors on `submission_id` (one-to-many), and to metadata
provenance on `submission_id` plus `metadata_oid` (one-to-one). Joining author rows
must not turn a paper-level count into an author-weighted count. Retain `family_id`
for repeated-paper handling. Topic memberships may overlap.

For an ordinary-submission acceptance population, require
`administrative_status == 'ordinary_submission'`, `outcome_eligible == 1` and
`decision in {'accepted','rejected'}`. This is a suggested data filter, not a completed
analysis. Research on influence additionally requires new, verified person/history
features and a declared historical cutoff; none are supplied as presumed ground truth.
