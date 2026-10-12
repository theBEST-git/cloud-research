# Research fashion in ICLR titles, 2017–2026

A pre-registered, audited study of how ICLR paper titles (with their abstracts) changed between 2017 and 2026. It
uses all 43,482 discovery submissions, including rejected, withdrawn and desk-rejected papers, not only the
accepted ones. The study asks four questions:

- **D1.** Did the "NAME: subtitle" fashion accelerate, and how much of the rise do content, team composition and
  detectable LLM drafting account for?
- **D2.** Who carried the change: the same declared profile keys, or entrants?
- **D3.** Did LLM-favoured wording rise in title slots where meaning is held fixed?
- **D4.** What do desk rejection, withdrawal and the accept decision do to title features, and how biased is a study
  of accepted papers alone? The camera-ready arXiv audit (WP4) bounds the decision stage.

**Status (2026-10-11).**
- Every direction was audited three times (code, identification, reporting), fixed, and then aligned in two
  integration passes.
- All estimates use the discovery split. The held-out confirmation split has **not** been requested.
- The confirmatory tests CT1–CT12 are frozen in the pre-registration bundle (revision 3), with hash
  `6853685bf21a08cdb40227d7fe5d94285c3ec023a9354ab3971faec75051ecd9`. Revision 3 came from a second integration pass
  that resolved 19 cross-direction consistency issues; the list is at the end of `outputs/SUMMARY.md`.
- **Start with [`outputs/SUMMARY.md`](outputs/SUMMARY.md).** It has the final verdict for every hypothesis, what the
  audits changed, the robust findings and the withdrawn claims. A machine-readable copy is
  `outputs/SUMMARY.json`.

## Data-use boundaries

These rules come from the repository README (`../../README.md`, `../../DATA_DICTIONARY.md`) and the study plan, and
they bind every output:

- **Inputs are read only.** The inputs are `../../data/` (43,516 discovery submissions, 219,719 declared author-list
  positions). Nothing in this study writes to `data/`. Read the CSVs with
  `pd.read_csv(path, keep_default_na=False, na_values=[r"\N"])`.
- **Only discovery rows.** All exported rows satisfy `discovery_allowed = 1`. Confirmation candidates are not an
  analysis population here. The held-out split may be requested only through `prereg_confirm heldout`, which runs
  once.
- **Keys are not persons.** A submission is not a paper family. A declared profile key (native author ID) is not a
  verified person, and repeated IDs support exact recorded-ID linkage only. Email identifiers are withheld; the opaque
  email key is not a profile.
- **List position is a label.** It is not seniority, career stage or supervision. "First/last list position" is a
  partition label only.
- **Acceptance analyses** apply outcome eligibility and the administrative-status filter explicitly. Withdrawal and
  desk rejection are kept separate from accept/reject. Missing outcomes are never turned into zeros.
- **Snapshot stage is not certified.** Accepted papers may carry camera-ready titles and abstracts. Every acceptance
  association is associational and subject to this camera-ready caveat, which the arXiv audit (WP4) bounds. The
  camera-ready-free pool (rejected ∪ withdrawn ∪ desk-rejected, "NA pool") uses submission-stage text.
- **Associational language.** No influence, supervisor or causal-tool claims are made. In particular, nothing is
  "caused by ChatGPT". Failed pre-registered predictions are reported as failed.
- **Source permissions remain source-specific.** No new blanket licence is assigned. The arXiv audit stores only
  public arXiv metadata: identifiers, version dates, v1 titles and v1 abstracts.

## Environment

- Python 3.13.16 in a virtualenv (`/home/user/venv` in the original session). CPU only.
- Install the pinned packages with `pip install -r requirements.txt`. It lists the packages the code imports, plus
  the parquet engine and the sentence-transformer stack. torch is the CPU wheel.
- **Threads.** Run every module from `src/` with `OMP_NUM_THREADS=2` (some steps use 1). Bootstraps use fixed seeds,
  so outputs reproduce exactly at the same thread count.
- **Models.** Two sentence-transformer encoders are downloaded from the Hugging Face hub on first use:
  `sentence-transformers/all-MiniLM-L6-v2` and `BAAI/bge-small-en-v1.5`.
- **Network.** Only the arXiv audit (`src/arxiv_audit.py`, `src/analyses/audit_v2.py`) uses the network, through
  `https://export.arxiv.org/api/query` (rate limits under step 4). Everything else runs offline once the models are
  cached.
- **Fonts.** Figures use the Inter font if it is installed, otherwise DejaVu Sans. Layout was checked with Inter.

## Pipeline

Run the commands from `research/titles/src` unless stated otherwise. `py` stands for
`OMP_NUM_THREADS=2 /home/user/venv/bin/python`. The runtimes are wall-clock times from the original run on 2 CPU
threads. Dependencies:
- Steps 5–8 depend on steps 1–3.
- **D3 and D4 also need step 4 and the archived arXiv caches.** `d3_slots` (D3's camera-ready slot-word audit) reads
  WP4's frozen enlargement sample from `cache/arxiv_audit*.jsonl`, and `d4_bias_atlas` reads `cache/arxiv_audit.jsonl`
  for its original-audit sensitivity; both stop with an error if the caches are missing.
- **`d1_summary` runs after step 7.** It reads D3's outputs for the H1e positive control. On a fresh run before D3 it
  writes the positive control as PENDING, and Fig. 2, Table 1, D1's `results.json` and the ledger would inherit that.
- Otherwise D1 (without `d1_summary`), D2, D3 and D4 can run in parallel.

### 1. Shared cache → `cache/` (gitignored)

```bash
py embed.py                    # MiniLM title + abstract embeddings (~30 min)
py embed_long.py               # bge-small 512-token embeddings (~1.5-2 h; background)
py author_features.py          # exact-key author-experience covariates (seconds)
py build_cache.py              # title_features, topics (KMeans k=50/100 on MiniLM), resubmission pairs (~2 min)
```

### 2. Foundation → `outputs/core/`, `outputs/features/`, `outputs/topics/`

```bash
py -m analyses._core           # universe (43,482), pools, area crosswalk, LLM clusters (~10 s)
OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.features_v2   # features_v2.parquet + lexicon hash (~80 s)
py -m analyses.topics_bge      # bge topic50/100, centroids, stability (~50 s)
nohup env OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.embed_masked 2 \
      > ../outputs/topics/embed_masked.log 2>&1 &     # name-masked bge embeddings, resumable (~75 min, background)
py -m analyses.smoke_test      # assertions -> outputs/core/smoke_test.txt (in-house FE vs pyfixest)
```

Data contract and loaders: [`src/analyses/API.md`](src/analyses/API.md).

### 3. Measurement validation → `outputs/validation/`

```bash
py -m analyses.annotate_sample    # blinded, stratified samples + codebooks (deterministic, byte-identical re-runs)
# two blind annotation passes (LLM annotators, different codebooks) write outputs/validation/labels/*.jsonl;
# this step is not scripted, so the committed labels are the record
py -m analyses.validate_measures  # kappa, precision/recall, Rogan-Gladen, corrected ITS, V2-V6 (minutes; the
                                  # bootstrap of the misclassification-corrected ITS dominates)
```

`validate_measures` writes `slot_variants_dropped.json`, which D3 needs before its slot inventory is frozen.

### 4. Camera-ready arXiv audit (WP4) → `cache/arxiv_audit*.jsonl`, `outputs/snapshot/`

The audit uses the network. Rate limit and safety rules:
- At least 3.2 s between requests, through one shared clock.
- Exponential back-off on errors.
- One instance at a time (lock file).
- Network errors are recorded as errors, never as "not found", and are retried on the next run.

Realised throughput is about 375–430 papers per hour.

```bash
py arxiv_audit.py --n-per-cell 75 --years 2023 2024 2025 2026
      # original audit, title route: 600 papers (~1 h); the file also holds 16 accepted 2022 papers from an
      # earlier pilot call, 616 in all (cache/arxiv_audit.log: '16 cached, 600 to query')
nohup env OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.audit_v2 --enlarge 250 \
      > ../outputs/snapshot/audit_v2.log 2>&1 &
      # phase 1 route validation (300 papers) and phase 1b v1 abstracts (330 papers): roughly 0.5-1 h each;
      # phase 2 enlargement: 2,000 papers, ~5 h; re-run with --skip-route --enlarge 250 to retry errored rows
py -m analyses.snapshot_final --enlarge-n 2004   # frozen complete audit; tables, gate, figures (~45 s)
py -m analyses.snapshot_final_report             # writes outputs/snapshot/RESULTS.md from results.json
```

- **Freeze.** The frozen sample is the first 2,004 lines of `cache/arxiv_audit_enlarge.jsonl` (2,000 complete
  records). Their SHA-256 is in `outputs/snapshot/results.json → meta.audit_freeze`.
- **Building blocks.** `snapshot_bounds.py` holds them; its own CLI produced the superseded interim run in
  `outputs/snapshot/interim_254/`. Do not edit it: the pre-registration bundle hashes it as required code.
- **Archived caches.** The arXiv caches are gitignored in `cache/`, and re-querying arXiv will not reproduce them
  byte for byte: papers get re-posted, retitled and withdrawn. The exact caches used for every reported number are
  therefore archived in the repository as `outputs/snapshot/arxiv_cache/*.jsonl.gz` (public arXiv metadata only:
  identifiers, version dates, titles and version-1 abstracts), with `SHA256SUMS` of the uncompressed files.
  Restore them before regenerating WP4, D3 or D4:
  `for f in outputs/snapshot/arxiv_cache/*.jsonl.gz; do gunzip -c "$f" > "cache/$(basename "$f" .gz)"; done`
  and check with `cd cache && sha256sum -c ../outputs/snapshot/arxiv_cache/SHA256SUMS` (paths in the file are `cache/...`;
  run it from the study root as `sha256sum -c outputs/snapshot/arxiv_cache/SHA256SUMS`). Without the caches, WP4 (step 4), D3's slot-word audit (`d3_slots`, which reads the
  first 2,004 enlargement lines and checks their SHA-256 against WP4's freeze) and D4's `d4_bias_atlas` (its
  "original audit only" sensitivity) cannot be regenerated; `d3_slots` and `d4_bias_atlas` stop with an error. D4's
  flip tables themselves are built from the committed `outputs/snapshot/audit_pairs.csv`.

### 5. D1: naming acceleration → `outputs/d1_break/`

```bash
py -m analyses.d1_its                                # H1a ITS, year-level inference (~1 min)
py -m analyses.d1_content_cf fit reps=R1,R5,R6,R6b   # content models (~5 min)
py -m analyses.d1_content_cf fit reps=R4,R2,R1u      # (~5 min)
py -m analyses.d1_content_cf fit reps=R1@0.5,R1n     # (~3 min)
py -m analyses.d1_content_cf fit variants            # NA pool, non-LLM, strict/loose/compound (~8 min)
py -m analyses.d1_content_cf fit reps=R3,R3yfe       # needs outputs/topics/emb_masked_bge.npy (~4 min)
py -m analyses.d1_content_cf fit reps=R1yfe,R5yfe    # year-FE sensitivities (~10 min)
py -m analyses.d1_decompose fit                      # composition and R1+composition fits (~30 s)
py -m analyses.d1_content_cf summarise 2000          # bootstraps, T1.2, new-topic placebo, V4 (~10 min)
py -m analyses.d1_content_cf refit_boot 300 R1       # refit bootstrap for H1c (~35 min, checkpointed)
py -m analyses.d1_decompose refit_boot 200           # (~10 min)
py -m analyses.d1_decompose all                      # DFL, Shapley, tool bound (~5 min)
```

`d1_summary` (D1's `results.json`, Holm, F1.x) is run after step 7, because it reads D3's outputs; see the end of
step 7.

### 6. D2: carriers → `outputs/d2_carriers/`

```bash
py -m analyses.d2_panel        # key-year panel, partitions, team types (~10 s)
py -m analyses.d2_shiftshare   # decomposition, nulls, IPW, bounds, removal simulation (~2.5-3.5 min)
py -m analyses.d2_markers      # H2d style vs topic markers (~1 min)
py -m analyses.d2_ident        # newcomer-free contrasts, two-way SEs, H2b (~35 s-1 min)
py -m analyses.d2_support      # S2.1 resubmissions, S2.2 future-tie placebo (~15 s)
py -m analyses.d2_collect      # results.json, verdicts, Holm, summary table in RESULTS.md (seconds)
```

### 7. D3: machine register → `outputs/d3_register/` (after step 4; needs the arXiv caches)

```bash
py -m analyses.d3_slots              # frozen slot inventory, H3a, T3.1, F3.1, slot-word camera-ready audit (~70 s)
py -m analyses.d3_register           # H3b, neutral benchmark, word churn, F3.2 (~16 s)
py -m analyses.d3_vintage            # H3c, F3.3 (~40 s)
py -m analyses.d3_signature_bound    # H3d, H3e, F3.4 (~7.5 min; background)
py -m analyses.d3_collect            # results.json, verdicts, Holm (seconds)
py -m analyses.d1_summary            # needs step 5 too: D1 results.json, Holm, F1.x; D3 positive control (~5 s)
```

Run `d1_summary` again whenever D3 is re-run.

### 8. D4: gatekeeper → `outputs/d4_filter/` (after step 4; `d4_bias_atlas` needs the arXiv caches)

```bash
py -m analyses.d4_stage_gains        # H4a, H4b, T4.1, F4.1 (~1.7 min)
py -m analyses.d4_bias_atlas         # H4c, H4e, T4.2 on WP4's frozen pairs, F4.2, F4.3 (~45 s)
py -m analyses.d4_exit_composition   # H4d, F4.4, exploratory timing (~40 s)
py -m analyses.d4_collect            # results.json, verdicts, Holm, WP4 gate, summary table (seconds)
```

### 9. Pre-registration (WP9) → `outputs/prereg/`

```bash
py -m analyses.prereg_confirm verify          # re-hash the committed bundle (expected: ok)
# how the committed bundle was produced (do NOT re-run on the committed state):
#   freeze (~5 min) -> check (~30 s) -> dryrun (~1.5 min) -> bundle         revision 1
#   refreeze_final (~15 s) -> check -> dryrun -> bundle                     revision 2
#   revise (~1 s) -> dryrun (compared with the previous dryrun.json) -> bundle   revision 3 (current)
# confirmation, once, after the bundle is committed:
#   py -m analyses.prereg_confirm heldout <heldout_submissions.csv.gz> <heldout_submission_authors.csv.gz>
```

- `prereg.md` documents the tests, the gate rule, the dry run and the revision history.
- `bundle.sha256` lists 73 files: code, frozen parameters and reference inputs. Its SHA-256 is the bundle hash.
- **Revision 2.** Revision 1 (`f69fdb46…`) was superseded before any held-out data were requested, for three
  reasons:
  - post-audit code fixes changed hashed files;
  - the gate audit was re-frozen on WP4's complete audit;
  - the gate adopted WP4's Holm-controlled rule.
- **Revision 3 (current).** Revision 2 (`853827a9…`) was superseded in the second integration pass, again before any
  held-out data were requested:
  - reading notes for CT1, CT2, CT4, CT6 and CT12 (the decision rules are unchanged);
  - required code outside the tests changed (`d3_slots.py`: the slot-word audit reads WP4's final freeze;
    `d4_bias_atlas.py`: atlas prevalence ratios reuse the stage-gain bootstrap seed);
  - frozen parameters other than `params.json` (revision record) and `rules.json` are byte-identical, and the re-run
    dry run reproduces every statistic.
- `audit_refreeze` is closed.
- **What `verify` checks.** `bundle.sha256` hashes all of `src/analyses/*.py` and `*.json`, five files in `src/`, the
  frozen parameters and the reference inputs. Two classes are strict:
  - the frozen parameters under `outputs/prereg/frozen/`;
  - the **required code**, which is every module file the tests load, as returned by
    `prereg_confirm.required_code()`: `src/{common,features,arxiv_audit}.py`, `src/analyses/__init__.py`,
    `_core.py`, `features_v2.py`, `d1_its.py`, `d1_content_cf.py`, `d2_panel.py`, `d3_slots.py`, `d3_register.py`,
    `d3_vintage.py`, `d4_stage_gains.py`, `d4_bias_atlas.py`, `snapshot_bounds.py`, `snapshot_final.py`,
    `prereg_confirm.py`, `lexicons.json` and `d4_lexicon.json` (19 files).
  A mismatch in either makes `verify` fail and blocks `heldout`. Any other hashed file (for example `figures.py`,
  `summary_ledger.py`, the `d*_collect.py` scripts or the gitignored reference inputs) only produces a
  `mismatched_other` warning.
- **Rule for later edits.** A change to required code needs a logged bundle revision (`revise` with a new
  `REVISION` record, then dryrun, compared with the previous `dryrun.json`, then bundle and verify), and is allowed only
  while no held-out data have been requested (no `heldout_started.json`). A change to other hashed code should be
  followed by `bundle` and `verify`, or its `mismatched_other` warning recorded.
- The frozen `.npz`/`.npy` parameters are deliberately not gitignored (see `.gitignore`).

### 10. Paper figures, tables and the ledger

```bash
py -m analyses.figures          # outputs/figures/fig1-6 (+ CSVs, manifest.json with captions), outputs/tables/ (~20 s)
py -m analyses.summary_ledger   # outputs/SUMMARY.json and SUMMARY.md (seconds; run after figures and the prereg bundle)
```

**Full re-run time.** About 10–12 h end to end, most of it in background jobs: the arXiv enlargement (~5 h), bge
embeddings (~2 h) and masked embeddings (~1.3 h). Without the network and embedding steps, the analysis steps 5–10
take about 2 h, most of it in D1's content models and refit bootstraps.

## Gitignored and regenerated

`.gitignore` excludes the following. The scripts above regenerate them deterministically, except where noted.

| Path pattern | What | Regenerated by |
|---|---|---|
| `cache/` | MiniLM/bge embeddings, title features, topics, resubmission pairs, author features, **arXiv audit caches** | step 1; the arXiv caches only by re-querying (not byte-identical; archive them) |
| `outputs/**/*.parquet` | universe, features_v2, topics_bge, masked abstracts, D1 scores and R1 text cache, D2 panel, D4 style density | steps 2, 5, 6, 8 |
| `outputs/**/*.npy`, `*.npz` | masked embeddings, centroids, bootstrap draws | steps 2, 6; **except** `outputs/prereg/frozen/*.npz|npy`, which are committed |
| `outputs/**/*.log`, `*.pkl`, `*.joblib`, `outputs/topics/embed_masked.done`, `__pycache__/` | logs and markers | any run |

- **Bundle inputs.** The pre-registration bundle also hashes some gitignored inputs: `universe.parquet`,
  `features_v2.parquet` and the D1 R1 text cache. `verify` treats a mismatch in these as a warning, not a failure;
  the frozen parameters and the code the tests execute must match exactly.
- **Interim backups.** `outputs/audit/<dir>/pre_fix_backup/` keeps pre-fix copies for the audit trail. The integration
  passes keep theirs in `outputs/audit/integration/pre_fix_backup/pass1/` (first pass, including the revision-1
  prereg files) and `pass2/` (second pass, including the revision-2 prereg files).

## File map

```
research/titles/
├── README.md, requirements.txt, .gitignore
├── docs/
│   ├── PLAN.md                  locked pre-registered plan (never edited)
│   ├── DIRECTIONS.md            direction design record (candidates, judging)
│   └── LITERATURE_BRIEF.md      citation-checked literature; §7 is the only citable reference list
├── paper/related_work.md        related-work draft
├── src/
│   ├── common.py, features.py   data loading (README NA convention), v1 title features (version-locked)
│   ├── embed.py, embed_long.py, author_features.py, build_cache.py      step 1
│   ├── arxiv_audit.py           original camera-ready audit (network)
│   └── analyses/
│       ├── API.md               data contract for the analysis package
│       ├── _core.py, features_v2.py, lexicons.json, d4_lexicon.json, topics_bge.py, embed_masked.py, smoke_test.py
│       ├── annotate_sample.py, validate_measures.py                       measurement validation
│       ├── audit_v2.py, snapshot_bounds.py, snapshot_final.py, snapshot_final_report.py     WP4
│       ├── d1_*.py, d2_*.py, d3_*.py, d4_*.py                             directions
│       ├── prereg_confirm.py    CT1-CT12, dry run, bundle, held-out runner
│       ├── figures.py           paper figures and tables
│       └── summary_ledger.py    consolidated ledger
├── cache/                       (gitignored) embeddings, topics, arXiv caches
└── outputs/
    ├── SUMMARY.md, SUMMARY.json final ledger: verdicts, robust findings, withdrawn claims
    ├── core/, features/, topics/            foundation tables and checks
    ├── validation/              VALIDATION.md, annotation batches/keys/labels, metrics
    ├── d1_break/, d2_carriers/, d3_register/, d4_filter/   RESULTS.md (with Audit response), results.json, tables, figures
    ├── snapshot/                WP4 RESULTS.md, results.json (audit freeze), tables, figures; interim_254/
    ├── prereg/                  prereg.md, bundle.sha256, dryrun.json, pipeline_check.json, frozen/
    ├── figures/, tables/        paper figures (fig1-6, PDF/PNG/CSV, manifest.json) and tables (CSV/TeX)
    └── audit/                   auditors' check scripts (<dir>_code, _ident, _reporting), fixer logs (<dir>/fix_log.md),
                                 integration/fix_log.md
```

## Reading the results

- **Verdicts.** Each direction's `RESULTS.md` opens with a verdict table and ends with an "Audit response" listing
  every audit issue and what changed. `outputs/SUMMARY.md` collects all verdicts in one place.
- **Families.** Holm-adjusted p-values are within each direction's confirmatory family (PLAN §0). The D1 and D4
  p-values test falsification boundaries or intersection-union combinations of the pre-registered sub-tests.
- **Camera-ready gate.** A decision-stage acceptance association enters a headline only if the feature is auditable
  through arXiv, its editing-corrected 95% CI excludes 1, and its identification p-value survives Holm across the
  auditable features. None does.
