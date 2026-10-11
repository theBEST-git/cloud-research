# ICLR corpus inputs

Minimal inputs for a fresh research session, published in
[theBEST-git/cloud-research](https://github.com/theBEST-git/cloud-research).
The data export is independent of the original project's Git remote.

Contains **43,516 discovery submissions** and **219,719 declared author-list
positions**, covering **2017–2026**. Compressed data total approximately **49 MiB**.
These positions are not a count of distinct or verified people.

## Start here

1. Read [DATA_DICTIONARY.md](DATA_DICTIONARY.md).
2. Read [data/manifest.json](data/manifest.json) for versions, counts and source checksums.
3. Load the three compressed CSV tables in `data/`.

| File | Unit | Contents |
|---|---|---|
| `submissions.csv.gz` | One discovery submission | Years 2017–2026, title, abstract, original and cleaned keywords, status, outcome evidence, families, splits and eligibility |
| `submission_authors.csv.gz` | One original author-list position | Declared names, public native profile IDs, exact declared-ID keys, list alignment and missingness |
| `metadata_provenance.csv.gz` | One discovery submission | Selected official metadata observation, source pointers, capture/event times and original source license |

These are existing corpus data, not new annotations or research findings. Review
bodies, manuscripts, external author histories, impact metrics, experimental
predictions, earlier experiments and confirmation candidates are absent. Existing
keyword cleaning assignments and the documented 2019 outcome correction are retained.

The gzip files are ordinary UTF-8 CSVs. JSON-valued columns require `json.loads`.
CSV null is the explicit sentinel `\N`; an empty string is distinct from null.

```python
import csv, gzip, json

with gzip.open("data/submissions.csv.gz", "rt", encoding="utf-8", newline="") as f:
    for raw in csv.DictReader(f):
        row = {k: None if v == "\\N" else v for k, v in raw.items()}
        keywords = json.loads(row["normalized_keywords_json"]) if row["normalized_keywords_json"] is not None else None
        # Define a research question and analysis population before analyzing outcomes.
```

If using pandas: `pd.read_csv(path, keep_default_na=False, na_values=[r"\N"])`.
Pandas is optional; validation needs only Python's standard library.

## Important boundaries

- All exported submissions already satisfy `discovery_allowed=1`. Confirmation
  candidates and pending families are not an independent analysis population here.
- A submission is not a distinct paper family, and a native author ID is not a
  verified person. Repeated IDs support exact recorded-ID linkage only.
- Name/ID lists with different lengths are not paired by assumption. Author order
  does not establish seniority, career stage or supervisory relationships.
- Email identifiers are withheld. An opaque key retains exact-ID equality; it is
  not an OpenReview profile or an external-service lookup ID. An email-shaped name
  is also withheld. Original evidence remains addressable by `metadata_oid`.
- Metadata and scores describe dated observations. Snapshot stage is not certified.
  Keep years and venue processes identifiable, including 2026.
- Withdrawal and desk rejection are separate from acceptance/rejection evidence.
  For acceptance analyses, explicitly apply outcome eligibility and the intended
  administrative-status filter. Never turn missing outcomes or histories into zero.
- Existing source permissions remain source-specific; this package assigns no new
  blanket license to the underlying records.

## Validate without connecting to any service

```text
python -B scripts/export_dataset.py validate --output data
python -B -m unittest discover -s tests
```

## Re-export from the original local inputs

The supplied tables are self-contained for reading. The large source databases are
not bundled. Reproduction requires these existing releases:

- `eda_ready_20260913T143255Z/eda.sqlite`
- `harmonized_20260910T125430Z/corpus.sqlite`
- `outcome_repair_20260923T104907Z/outcomes.sqlite`
- `keyword_completion_20260926_v4/final/submission_keywords.csv`

```text
python -B scripts/export_dataset.py build --clean <eda.sqlite> --upstream <corpus.sqlite> --patch <outcomes.sqlite> --keywords <submission_keywords.csv> --output <new-folder>
```

Export uses an explicit field allowlist, read-only SQLite connections, bounded
streaming and disabled network/subprocess operations. It refuses to overwrite an
existing export. Small consumed files are fully checksum verified; large database
preservation is checked through sealed manifests, size and mtime, not a new full
raw-corpus checksum audit. See `validation.json` and `reproduction.json` in `data/`.

## Derived layers

- [research/topics/](research/topics/README.md): outcome-blind content topics for every discovery paper
  (20 broad / 100 middle / 198 fine), typed author keywords and a breakdown of generic keywords. Built on
  top of this package; not part of the sealed export.
