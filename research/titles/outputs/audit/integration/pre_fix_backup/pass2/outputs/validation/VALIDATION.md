# Measurement validation (WP3b, PLAN.md section 3, V1-V6)

Produced by `src/analyses/validate_measures.py`. All numbers are regenerated from the blind annotation passes in `outputs/validation/labels/` and the frozen features (`features_v2.parquet`, lexicons v2.0). Annotation passes A and B are LLM annotators (different models and codebooks), blind to year, outcome and detector output. "Consensus" means the label both passes gave. Where they differed, the PI's delegate adjudicated from the title (or cluster) text alone; every adjudication is recorded in a CSV. Declared author IDs are "declared profile keys", not people.

## Summary

- **V1 agreement.** Passes A and B agree almost perfectly.
  - compound κ = 1.000, question κ = 1.000.
  - lead type κ = 0.949 (coined-name binary 0.936), orthography κ = 0.948, casing κ = 0.969.
  - All five labels clear the 0.80 target (lowest 0.948; lowest lower CI bound 0.933). 58 of 1,400 items needed adjudication. The spot check found 0 clear errors among 150 agreed items (95% CI 0–2.4%) and 5 borderline calls.
- **V1 NAME detector (primary), against the adjudicated consensus.** Population estimates over all years (post-stratified: main sample plus the two-token-lead hard cells):
  - precision 97.8 [97.5, 98.3]%;
  - recall 97.3 [96.1, 98.3]%;
  - specificity 99.1 [98.9, 99.3]%.
  - Precision by block runs from 97.3% (2024) to 98.6% (2023): a range of 1.2 pp.
  - Pass criterion < 5 pp: **met** on the point estimate. Six noisy block estimates spread by 0.8 pp (median) even with no drift; p = 0.15 for a range this large.
  - Post (2024–26) minus pre block mean: -0.2 pp [-1.3, +0.8].
- **V1 corrected ITS.** The block-specific misclassification-corrected slope-change OR is 1.090 [1.033, 1.151], against 1.098 [1.044, 1.154] uncorrected.
  - OR ratio 0.994: within 10% on the OR scale, **yes**. On the log-OR scale the change is -6.9% (within 10%).
- **V2 slots.** Words to drop (sense precision < 0.85): exploit/unlocking (0.29, n=7), exploit/enabling (0.00, n=21), reveal/decoding (0.39, n=8). Written to `slot_variants_dropped.json`.
- **V3.** LLM-polish ratings correlate weakly with the fingerprints: Spearman ρ = 0.25 for F, 0.31 for F24 and 0.10 for F26. This is weak convergent validity only.
  - False-positive rates in 2021–22: F24 2.9%, F26 3.2%, F 5.9%, title typography 0.04%.
  - No LaTeX or PDF artefacts among the 100 inspected typography titles.
- **V4.** The lead string (whole word) survives the R3 mask in 0 of 12,928 NAME abstracts (meets the 0% target) and the R1 mask in 22.
  - Variant spellings of the name do survive: LaTeX-wrapped, markdown, other Unicode hyphens, project URLs. That is 105 abstracts (0.81%) under R3 and 46 (0.36%) under R1.
- **V5.** The annotator's LM flag agrees with the regex LLM-cluster rule at κ = 0.86; all 5 disagreements are clusters the annotator calls LM but whose all-years regex share sits just below 0.5. MiniLM vs bge topic100 ARI = 0.421 (NMI 0.666).
- **V6.** 0 exact key-years exceed 40 papers (max 40); 7 alias-years do once trailing digits are stripped. Collapsing trailing digits changes 24.2% of 2022+ papers' share of new authors (mean 0.552 → 0.495).

## V1. NAME, compound, orthography and casing detectors

### Sample and agreement
- **Sample:**
  - 1,200 main items: 6 year blocks × (100 NAME-positive, spread over the 4 orthography classes; 50 phrase-colon compounds; 50 non-compound). Design weights are N_h/n_h.
  - 200 hard cases: two-token leads, LaTeX, dash compounds, genre and dictionary-word leads.
  - Population estimates combine the main sample with the two-token-lead hard strata by post-stratification (below). The other hard strata are diagnostics only.
- **Cohen's κ, pass A vs pass B** (item-bootstrap 95% CI):

| label | items | n | κ [95% CI] | agreement | n_disagree |
|---|---|---|---|---|---|
| compound | all | 1400 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| compound | main | 1200 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| compound | hard | 200 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| lead_type | all | 1400 | 0.949 [0.933, 0.963] | 96.8% | 45 |
| lead_type | main | 1200 | 0.961 [0.946, 0.974] | 97.6% | 29 |
| lead_type | hard | 200 | 0.878 [0.816, 0.932] | 92.0% | 16 |
| lead_orthography | all | 1400 | 0.948 [0.933, 0.962] | 96.5% | 49 |
| lead_orthography | main | 1200 | 0.960 [0.946, 0.973] | 97.2% | 33 |
| lead_orthography | hard | 200 | 0.867 [0.801, 0.929] | 92.0% | 16 |
| casing | all | 1400 | 0.969 [0.948, 0.985] | 99.3% | 10 |
| casing | main | 1200 | 0.967 [0.945, 0.986] | 99.2% | 9 |
| casing | hard | 200 | 0.978 [0.922, 1.000] | 99.5% | 1 |
| question | all | 1400 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| question | main | 1200 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| question | hard | 200 | 1.000 [1.000, 1.000] | 100.0% | 0 |
| coined_name (binary) | all | 1400 | 0.936 [0.916, 0.954] | 96.8% | 45 |
| coined_name (binary) | main 2017-19 | 200 | 0.950 [0.900, 0.990] | 97.5% | 5 |
| coined_name (binary) | main 2020-22 | 200 | 0.950 [0.900, 0.990] | 97.5% | 5 |
| coined_name (binary) | main 2023 | 200 | 0.940 [0.889, 0.980] | 97.0% | 6 |
| coined_name (binary) | main 2024 | 200 | 0.960 [0.920, 0.990] | 98.0% | 4 |
| coined_name (binary) | main 2025 | 200 | 0.970 [0.930, 1.000] | 98.5% | 3 |
| coined_name (binary) | main 2026 | 200 | 0.940 [0.888, 0.980] | 97.0% | 6 |
| lead_orthography | both coined | all | 670 | 0.992 [0.983, 0.998] | 99.4% | 4 |
| lead string | both compound | all | 1059 |  | 100.0% | 0 |

- Compound, lead string and question agree on every item. The disagreements concentrate on whether a multi-word lead is a coined name or a descriptive phrase.
- **Adjudication.**
  - 58 items, 104 label decisions; see `v1_adjudications.csv`.
  - Rule: lead_type: a lead is coined_name when it is, or is headed by, a proper-noun-like label: an invented or blended word or acronym, a dictionary word used as the name of one specific artefact (including existing techniques), a phrase followed by its parenthesised acronym or its own symbol, or a non-literal noun phrase that the subtitle presents as the paper's artefact. A lead made of ordinary words in their ordinary or standard technical senses is descriptive_phrase even when it is the paper's method name ('method description' in codebook A, 'approach in ordinary language' in codebook B), as is a lead in which a pre-existing name or family abbreviation only modifies a generic head (codebook A: 'LoRA Fine-Tuning at Scale'). Metaphors, puns and allusions that the subtitle does not present as an artefact are slogans (descriptive_phrase). This matches 239 of the 255 agreed plain multi-word leads (both passes descriptive). orthography: the codebook's ordered rules applied to the name (an initial article is not part of the name). casing: tokens the authors treat as names (coined names, acronym expansions, established architecture names) are set aside; field and family terms are counted.
  - Lead type: 45 disputes, resolved as coined_name in 6 and descriptive_phrase in 39.
  - Pass A had called coined_name in 39 of these, pass B in 6.
  - Because this boundary is the main source of disagreement, every detector metric is also reported against a lenient construct (coined in either pass) and a strict one (coined in both).
- **Spot check of agreed items.**
  - 150 random agreed items were checked: 0 clear errors and 5 borderline (2 lead type, 3 casing).
  - Estimated consensus error ≤ 2.4% (95% upper bound); 3.3% if borderline calls are counted as errors.
  - The checker is the adjudicator, so this is not an independent audit. Details in `v1_spotcheck.csv`.

### Detector accuracy against the consensus
- **Estimator (primary): post-stratified, main sample plus hard cases.**
  - Each main sampling stratum is split into the cell of two-token leads and the rest, using known population counts.
  - The rest is estimated from the main items.
  - Two-token cells are estimated per era and detector side from the pooled main and hard two-token items, which are random draws from exactly those cells.
- **Why:** the main sample, allocated by orthography, contains almost no two-token NAME leads in 2024–26 (none in 2026), yet the consensus calls most of them descriptive (table below). The main-only Horvitz–Thompson (HT) estimator is unbiased but misses this cell by chance, and its bootstrap CI cannot show it.
- CIs: stratified bootstrap of both samples (2,000 reps). Values are percentages. Items, FP and FN are unweighted counts in the main sample.

Two-token lead cells (compound title, lead of exactly 2 tokens; main + hard items):

| era | detector | N_population | n_main | n_hard | coined | share coined [Wilson 95%] |
|---|---|---|---|---|---|---|
| pre | NAME | 76 | 9 | 12 | 12 | 0.57 [0.37, 0.76] |
| pre | not NAME | 334 | 38 | 13 | 13 | 0.25 [0.16, 0.39] |
| post | NAME | 265 | 5 | 12 | 3 | 0.18 [0.06, 0.41] |
| post | not NAME | 813 | 23 | 13 | 10 | 0.28 [0.16, 0.44] |

| detector vs construct | block | precision | recall | specificity | items | FP | FN |
|---|---|---|---|---|---|---|---|
| NAME primary (name_colon) vs consensus coined name | 2017-19 | 97.5 [96.3, 98.7] | 93.7 [91.0, 96.6] | 99.7 [99.5, 99.8] | 200 | 3 | 3 |
|  | 2020-22 | 97.5 [96.5, 98.6] | 96.1 [94.4, 97.9] | 99.5 [99.3, 99.7] | 200 | 7 | 4 |
|  | 2023 | 98.6 [97.8, 99.3] | 95.1 [91.4, 97.9] | 99.6 [99.4, 99.8] | 200 | 2 | 5 |
|  | 2024 | 97.3 [96.7, 98.0] | 97.7 [96.5, 98.8] | 99.0 [98.8, 99.3] | 200 | 5 | 4 |
|  | 2025 | 97.4 [96.7, 98.1] | 96.6 [94.0, 98.5] | 98.7 [98.4, 99.0] | 200 | 4 | 2 |
|  | 2026 | 98.2 [97.8, 98.6] | 98.1 [97.1, 99.1] | 98.7 [98.5, 99.0] | 200 | 3 | 2 |
|  | all | 97.8 [97.5, 98.3] | 97.3 [96.1, 98.3] | 99.1 [98.9, 99.3] | 1200 | 24 | 20 |
| NAME strict vs consensus coined name | 2017-19 | 100.0 [100.0, 100.0] | 90.1 [87.4, 93.1] | 100.0 [100.0, 100.0] | 200 | 0 | 6 |
|  | 2020-22 | 99.0 [98.1, 99.8] | 93.9 [92.1, 95.7] | 99.8 [99.6, 100.0] | 200 | 5 | 10 |
|  | 2023 | 99.8 [99.3, 100.0] | 93.0 [89.3, 95.7] | 99.9 [99.8, 100.0] | 200 | 1 | 11 |
|  | 2024 | 99.7 [99.2, 100.0] | 96.8 [95.5, 98.0] | 99.9 [99.7, 100.0] | 200 | 2 | 10 |
|  | 2025 | 99.8 [99.4, 100.0] | 95.7 [93.1, 97.6] | 99.9 [99.7, 100.0] | 200 | 1 | 16 |
|  | 2026 | 100.0 [100.0, 100.0] | 97.4 [96.4, 98.5] | 100.0 [100.0, 100.0] | 200 | 0 | 20 |
|  | all | 99.8 [99.7, 99.9] | 96.2 [95.0, 97.3] | 99.9 [99.9, 100.0] | 1200 | 9 | 73 |
| NAME strict vs consensus single-token coined name | 2017-19 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2020-22 | 99.0 [98.1, 99.8] | 100.0 [100.0, 100.0] | 99.8 [99.6, 100.0] | 200 | 5 | 0 |
|  | 2023 | 99.8 [99.3, 100.0] | 100.0 [100.0, 100.0] | 99.9 [99.8, 100.0] | 200 | 1 | 0 |
|  | 2024 | 99.7 [99.2, 100.0] | 100.0 [100.0, 100.0] | 99.9 [99.7, 100.0] | 200 | 2 | 0 |
|  | 2025 | 99.8 [99.4, 100.0] | 100.0 [100.0, 100.0] | 99.9 [99.7, 100.0] | 200 | 1 | 0 |
|  | 2026 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | all | 99.8 [99.7, 99.9] | 100.0 [100.0, 100.0] | 99.9 [99.9, 100.0] | 1200 | 9 | 0 |
| NAME loose vs consensus coined name | 2017-19 | 82.5 [79.9, 85.2] | 98.7 [97.2, 99.7] | 97.2 [96.8, 97.6] | 200 | 13 | 2 |
|  | 2020-22 | 87.8 [86.0, 89.7] | 99.0 [98.1, 99.7] | 97.2 [96.8, 97.7] | 200 | 19 | 5 |
|  | 2023 | 91.5 [90.2, 92.8] | 96.7 [93.1, 99.2] | 97.6 [97.2, 98.0] | 200 | 7 | 8 |
|  | 2024 | 92.9 [91.6, 94.3] | 99.6 [99.6, 99.6] | 97.3 [96.7, 97.8] | 200 | 5 | 6 |
|  | 2025 | 92.8 [91.5, 94.3] | 98.6 [96.4, 99.6] | 96.2 [95.5, 96.9] | 200 | 8 | 14 |
|  | 2026 | 94.5 [93.5, 95.6] | 99.7 [99.7, 99.8] | 96.1 [95.4, 96.9] | 200 | 8 | 18 |
|  | all | 92.8 [91.8, 93.9] | 99.2 [98.6, 99.6] | 96.7 [96.3, 97.2] | 1200 | 60 | 53 |
| NAME compound vs consensus coined name | 2017-19 | 50.0 [48.4, 51.5] | 100.0 [100.0, 100.0] | 86.4 [86.1, 86.8] | 200 | 50 | 0 |
|  | 2020-22 | 57.5 [56.2, 58.7] | 100.0 [100.0, 100.0] | 85.2 [84.8, 85.5] | 200 | 53 | 0 |
|  | 2023 | 64.6 [62.6, 67.2] | 100.0 [100.0, 100.0] | 85.4 [84.7, 86.3] | 200 | 47 | 0 |
|  | 2024 | 64.5 [63.7, 65.4] | 100.0 [100.0, 100.0] | 80.2 [79.8, 80.6] | 200 | 51 | 0 |
|  | 2025 | 67.0 [65.6, 68.8] | 100.0 [100.0, 100.0] | 75.3 [74.6, 76.4] | 200 | 52 | 0 |
|  | 2026 | 67.6 [66.9, 68.3] | 100.0 [100.0, 100.0] | 67.4 [66.9, 67.9] | 200 | 51 | 0 |
|  | all | 65.3 [64.6, 66.1] | 100.0 [100.0, 100.0] | 77.3 [76.9, 77.7] | 1200 | 304 | 0 |
| compound vs consensus compound | 2017-19 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2020-22 | 99.9 [99.7, 100.0] | 100.0 [100.0, 100.0] | 100.0 [99.9, 100.0] | 200 | 1 | 0 |
|  | 2023 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2024 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2025 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2026 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | all | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 1200 | 1 | 0 |
| question vs consensus question | 2017-19 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2020-22 | 100.0 [100.0, 100.0] | 82.3 [0.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 1 |
|  | 2023 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2024 | 100.0 [100.0, 100.0] | 69.0 [0.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 1 |
|  | 2025 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | 2026 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 200 | 0 | 0 |
|  | all | 100.0 [100.0, 100.0] | 96.8 [89.6, 100.0] | 100.0 [100.0, 100.0] | 1200 | 0 | 2 |
| NAME primary vs coined by either pass (lenient) | 2017-19 | 98.6 [97.5, 99.7] | 85.4 [79.7, 91.0] | 99.8 [99.7, 100.0] | 200 | 3 | 8 |
|  | 2020-22 | 98.1 [97.1, 99.1] | 91.0 [86.1, 95.0] | 99.6 [99.4, 99.8] | 200 | 6 | 7 |
|  | 2023 | 99.1 [98.4, 99.7] | 91.8 [87.6, 95.5] | 99.8 [99.6, 99.9] | 200 | 1 | 9 |
|  | 2024 | 98.2 [97.4, 98.9] | 94.9 [92.4, 96.9] | 99.3 [99.0, 99.6] | 200 | 3 | 5 |
|  | 2025 | 98.2 [97.4, 99.0] | 93.1 [89.8, 95.9] | 99.1 [98.7, 99.5] | 200 | 4 | 5 |
|  | 2026 | 98.8 [98.3, 99.3] | 94.8 [91.8, 97.2] | 99.2 [98.8, 99.5] | 200 | 3 | 8 |
|  | all | 98.5 [98.0, 99.1] | 93.6 [91.8, 95.4] | 99.4 [99.1, 99.6] | 1200 | 20 | 42 |
| NAME primary vs coined by both passes (strict) | 2017-19 | 97.5 [96.3, 98.7] | 94.1 [91.6, 97.0] | 99.7 [99.5, 99.8] | 200 | 3 | 3 |
|  | 2020-22 | 97.3 [96.2, 98.4] | 96.4 [94.8, 98.2] | 99.5 [99.3, 99.7] | 200 | 8 | 4 |
|  | 2023 | 98.6 [97.8, 99.3] | 96.4 [93.5, 98.5] | 99.6 [99.4, 99.8] | 200 | 2 | 4 |
|  | 2024 | 97.3 [96.7, 98.0] | 98.1 [96.9, 99.2] | 99.0 [98.8, 99.3] | 200 | 5 | 3 |
|  | 2025 | 97.4 [96.7, 98.1] | 97.1 [94.6, 98.9] | 98.7 [98.4, 99.0] | 200 | 4 | 2 |
|  | 2026 | 98.2 [97.8, 98.6] | 98.5 [97.5, 99.4] | 98.7 [98.5, 99.0] | 200 | 3 | 2 |
|  | all | 97.8 [97.4, 98.3] | 97.7 [96.7, 98.7] | 99.1 [98.9, 99.3] | 1200 | 25 | 18 |

Main-only HT estimates for the primary detector, for comparison:

| block | precision (HT) | recall (HT) | specificity (HT) |
|---|---|---|---|
| 2017-19 | 96.0 [91.3, 100.0] | 93.7 [87.3, 100.0] | 99.5 [98.9, 100.0] |
| 2020-22 | 97.2 [93.1, 99.5] | 94.1 [88.7, 98.5] | 99.4 [98.6, 99.9] |
| 2023 | 98.0 [94.2, 100.0] | 94.2 [89.2, 98.8] | 99.5 [98.5, 100.0] |
| 2024 | 94.7 [87.8, 99.7] | 95.6 [91.3, 98.9] | 98.1 [95.7, 99.9] |
| 2025 | 97.4 [92.6, 100.0] | 98.0 [94.9, 100.0] | 98.7 [96.5, 100.0] |
| 2026 | 100.0 [99.9, 100.0] | 98.1 [95.4, 100.0] | 100.0 [99.9, 100.0] |
| all | 98.3 [96.8, 99.4] | 97.1 [95.4, 98.5] | 99.3 [98.7, 99.7] |

- **Precision drift (primary, PS).**
  - By block: 2017-19 97.5, 2020-22 97.5, 2023 98.6, 2024 97.3, 2025 97.4, 2026 98.2.
  - Range 1.2 pp (bootstrap 95% CI 1.0–2.4).
  - Under a common precision, sampling noise alone gives a median range of 0.8 pp; p = 0.15 for a range at least this large.
  - Post (2024–26) minus pre (2017–23) block mean: -0.2 pp [-1.3, +0.8].
  - Recall by block: 2017-19 93.7, 2020-22 96.1, 2023 95.1, 2024 97.7, 2025 96.6, 2026 98.1; range 4.4 pp.
- **Error patterns of the primary detector** (all 1,400 items, main and hard; rule-based categories; full lists in `v1_name_false_positives.csv` and `v1_name_false_negatives.csv`):
  - False positives (40):
    - all-caps title: 2 (e.g. 'ANYTIME MINIBATCH'; 'ARCHITECTURE MATTERS').
    - one-word descriptive lead: 9 (e.g. 'Multi-attacks'; 'Cramming'; 'Stiffness'; 'Attention').
    - parenthesis read as an acronym: 6 (e.g. 'Why Less is More (Sometimes)'; 'Death of the Novel(ty)'; 'Do as I do (Safely)'; 'Improving Block-Wise LLM Quantization by 4-bit Block-Wise Optimal Float (BOF4)').
    - separator misread (spaced hyphen inside a word): 1 (e.g. 'Uncertainty').
    - two-token descriptive lead with a hyphenated or capitalised modifier: 22 (e.g. 'LoRA Recycle'; 'GAN Dissection'; 'Human-Prior Correction'; 'f-Domain-Adversarial Learning').
  - False negatives (29):
    - lead of 3+ tokens headed by a name: 4 (e.g. 'Sorted eigenvalue comparison $d_{\mathsf{Eig}}$'; 'Neural Slot Interpreters'; 'Contrastive Value Learning'; 'Param$\Delta$ for Direct Mixing').
    - lead starts with an article or function word: 3 (e.g. 'The Predictron'; 'The GANfather'; 'CAN').
    - ordinary first word + coined token: 7 (e.g. 'Visual TransforMatcher'; 'Continual LLaVA'; 'Secure FLOATING'; 'Deep FlexQP').
    - two ordinary words used as a name: 15 (e.g. 'Contrastive Quant'; 'Feature Shapley'; 'Snapshot Ensembles'; 'Skill Machines').

**Hard cases** (unweighted; the two-token strata enter the PS estimator; the others are diagnostics only):

| stratum | n | det_name | cons_name | agree_name | det_compound | cons_compound | agree_compound |
|---|---|---|---|---|---|---|---|
| hard|dash|dash_detected | 25 | 9 | 11 | 0.92 | 25 | 24 | 0.96 |
| hard|dash|dash_undetected | 25 | 0 | 0 | 1.00 | 0 | 4 | 0.84 |
| hard|genre_lead|dict_word_lead | 30 | 30 | 29 | 0.97 | 30 | 30 | 1.00 |
| hard|genre_lead|genre_word_lead | 20 | 1 | 0 | 0.95 | 20 | 20 | 1.00 |
| hard|latex|latex_post | 25 | 12 | 13 | 0.96 | 16 | 16 | 1.00 |
| hard|latex|latex_pre | 25 | 11 | 11 | 1.00 | 16 | 16 | 1.00 |
| hard|two_token_lead|name_post | 12 | 12 | 2 | 0.17 | 12 | 12 | 1.00 |
| hard|two_token_lead|name_pre | 12 | 12 | 8 | 0.67 | 12 | 12 | 1.00 |
| hard|two_token_lead|nonname_post | 13 | 0 | 3 | 0.77 | 13 | 13 | 1.00 |
| hard|two_token_lead|nonname_pre | 13 | 0 | 3 | 0.77 | 13 | 13 | 1.00 |

**Orthography** (items where the detector and the consensus both say NAME; design-weighted, %):

| cls | 2017-19 | 2020-22 | 2023 | 2024 | 2025 | 2026 | all |
|---|---|---|---|---|---|---|---|
| (accuracy) | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| all_caps precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| all_caps recall | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| mixed_case precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| mixed_case recall | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [99.9, 100.0] | 100.0 [100.0, 100.0] |
| paren_acronym precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 94.7 [82.4, 100.0] | 98.1 [93.8, 100.0] |
| paren_acronym recall | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| word precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| word recall | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |

Confusion matrix (rows: detector, columns: consensus; unweighted counts):

| detector | all_caps | mixed_case | paren_acronym | word |
|---|---|---|---|---|
| all_caps | 180 | 0 | 0 | 0 |
| mixed_case | 0 | 179 | 0 | 0 |
| paren_acronym | 0 | 1 | 51 | 0 |
| word | 0 | 0 | 0 | 165 |

**Casing** (all main items; the detector's 'mixed' and 'other' both map to 'other'; design-weighted, %):

| cls | 2017-19 | 2020-22 | 2023 | 2024 | 2025 | 2026 | all |
|---|---|---|---|---|---|---|---|
| (accuracy) | 97.7 [94.3, 99.6] | 95.2 [89.8, 99.4] | 99.2 [98.3, 100.0] | 99.4 [98.7, 100.0] | 99.7 [99.0, 100.0] | 99.9 [99.8, 100.0] | 98.8 [98.0, 99.5] |
| all_caps precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| all_caps recall | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] |
| other precision | 4.6 [0.0, 34.8] | 67.0 [25.8, 96.3] | 64.1 [0.0, 100.0] | 97.2 [0.0, 100.0] | 91.6 [60.0, 100.0] | 87.4 [0.0, 99.4] | 78.3 [57.3, 90.9] |
| other recall | 100.0 [100.0, 100.0] | 27.2 [6.2, 100.0] | 79.6 [0.0, 100.0] | 52.7 [0.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 69.9 [43.1, 95.9] |
| sentence_case precision | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 87.2 [56.5, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 99.3 [97.4, 100.0] |
| sentence_case recall | 80.1 [50.5, 96.8] | 82.8 [56.6, 99.6] | 92.2 [50.7, 100.0] | 99.1 [95.9, 100.0] | 93.4 [72.5, 100.0] | 97.8 [89.8, 99.9] | 89.4 [78.0, 96.9] |
| title_case precision | 100.0 [100.0, 100.0] | 95.1 [89.1, 100.0] | 99.7 [99.2, 100.0] | 99.7 [99.1, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 99.2 [98.2, 99.9] |
| title_case recall | 100.0 [100.0, 100.0] | 100.0 [99.9, 100.0] | 99.7 [99.2, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [99.9, 100.0] |

Confusion matrix (rows: detector, columns: consensus; unweighted counts):

| detector | all_caps | other | sentence_case | title_case |
|---|---|---|---|---|
| all_caps | 34 | 0 | 0 | 0 |
| other | 0 | 20 | 22 | 2 |
| sentence_case | 0 | 1 | 69 | 0 |
| title_case | 0 | 5 | 1 | 1046 |

### Rogan–Gladen corrected yearly prevalence
- **Formula:** p_RG = (p_obs + Sp_b − 1)/(Se_b + Sp_b − 1), with block-specific Se/Sp from the PS estimator.
- **CI:** validation-sample uncertainty only.
- **Checks:** "PPV/NPV" is the calibration estimator p_obs·PPV + (1 − p_obs)(1 − NPV). "RG (HT)" uses main-only Se/Sp.

| detector | year | observed % | Se | Sp | RG-corrected % [95% CI] | PPV/NPV % | RG (HT) % |
|---|---|---|---|---|---|---|---|
| name_primary | 2017 | 8.9 | 0.937 | 0.997 | 9.1 [8.8, 9.4] | 9.4 | 8.9 |
|  | 2018 | 10.0 | 0.937 | 0.997 | 10.4 [10.0, 10.7] | 10.5 | 10.2 |
|  | 2019 | 13.1 | 0.937 | 0.997 | 13.7 [13.3, 14.2] | 13.6 | 13.5 |
|  | 2020 | 15.7 | 0.961 | 0.995 | 15.9 [15.6, 16.3] | 16.0 | 16.2 |
|  | 2021 | 15.0 | 0.961 | 0.995 | 15.2 [14.9, 15.6] | 15.3 | 15.5 |
|  | 2022 | 18.3 | 0.961 | 0.995 | 18.7 [18.3, 19.1] | 18.5 | 19.0 |
|  | 2023 | 20.3 | 0.951 | 0.996 | 21.0 [20.4, 21.9] | 21.0 | 21.1 |
|  | 2024 | 26.6 | 0.977 | 0.990 | 26.5 [26.2, 26.9] | 26.5 | 26.4 |
|  | 2025 | 33.1 | 0.966 | 0.987 | 33.4 [32.7, 34.3] | 33.4 | 32.9 |
|  | 2026 | 40.5 | 0.981 | 0.987 | 40.5 [40.1, 40.9] | 40.5 | 41.2 |
| name_strict | 2017 | 8.3 | 1.000 | 1.000 | 8.3 [8.3, 8.3] | 8.3 | 8.3 |
|  | 2018 | 9.2 | 1.000 | 1.000 | 9.2 [9.2, 9.2] | 9.2 | 9.2 |
|  | 2019 | 12.4 | 1.000 | 1.000 | 12.4 [12.4, 12.4] | 12.4 | 12.4 |
|  | 2020 | 15.1 | 1.000 | 0.998 | 14.9 [14.8, 15.0] | 14.9 | 14.9 |
|  | 2021 | 14.4 | 1.000 | 0.998 | 14.2 [14.1, 14.4] | 14.3 | 14.2 |
|  | 2022 | 17.7 | 1.000 | 0.998 | 17.6 [17.4, 17.7] | 17.6 | 17.6 |
|  | 2023 | 19.6 | 1.000 | 0.999 | 19.6 [19.5, 19.6] | 19.6 | 19.6 |
|  | 2024 | 25.7 | 1.000 | 0.999 | 25.7 [25.5, 25.7] | 25.7 | 25.7 |
|  | 2025 | 32.0 | 1.000 | 0.999 | 31.9 [31.8, 32.0] | 31.9 | 31.9 |
|  | 2026 | 39.4 | 1.000 | 1.000 | 39.4 [39.4, 39.4] | 39.4 | 39.4 |
| name_loose | 2017 | 10.2 | 0.987 | 0.972 | 7.6 [7.2, 8.1] | 8.5 | 7.2 |
|  | 2018 | 12.7 | 0.987 | 0.972 | 10.3 [9.9, 10.8] | 10.7 | 10.0 |
|  | 2019 | 16.3 | 0.987 | 0.972 | 14.0 [13.6, 14.5] | 13.6 | 13.7 |
|  | 2020 | 18.0 | 0.990 | 0.972 | 15.8 [15.4, 16.2] | 16.0 | 14.2 |
|  | 2021 | 17.3 | 0.990 | 0.972 | 15.2 [14.7, 15.6] | 15.4 | 13.5 |
|  | 2022 | 20.8 | 0.990 | 0.972 | 18.8 [18.4, 19.2] | 18.4 | 17.1 |
|  | 2023 | 22.2 | 0.967 | 0.976 | 21.0 [20.4, 21.9] | 21.0 | 21.5 |
|  | 2024 | 28.5 | 0.996 | 0.973 | 26.6 [26.2, 27.0] | 26.6 | 27.2 |
|  | 2025 | 35.6 | 0.986 | 0.962 | 33.6 [32.9, 34.5] | 33.5 | 33.3 |
|  | 2026 | 42.6 | 0.997 | 0.961 | 40.4 [40.0, 40.9] | 40.4 | 39.5 |
| name_compound | 2017 | 19.3 | 1.000 | 1.000 | 19.3 [19.3, 19.3] | 19.3 | 19.3 |
|  | 2018 | 22.9 | 1.000 | 1.000 | 22.9 [22.9, 22.9] | 22.9 | 22.9 |
|  | 2019 | 25.9 | 1.000 | 1.000 | 25.9 [25.9, 25.9] | 25.9 | 25.9 |
|  | 2020 | 26.7 | 1.000 | 1.000 | 26.6 [26.6, 26.7] | 26.6 | 26.6 |
|  | 2021 | 28.2 | 1.000 | 1.000 | 28.2 [28.1, 28.2] | 28.2 | 28.2 |
|  | 2022 | 31.7 | 1.000 | 1.000 | 31.7 [31.6, 31.7] | 31.7 | 31.7 |
|  | 2023 | 32.6 | 1.000 | 1.000 | 32.6 [32.6, 32.6] | 32.6 | 32.6 |
|  | 2024 | 41.1 | 1.000 | 1.000 | 41.1 [41.1, 41.1] | 41.1 | 41.1 |
|  | 2025 | 49.8 | 1.000 | 1.000 | 49.8 [49.8, 49.8] | 49.8 | 49.8 |
|  | 2026 | 59.9 | 1.000 | 1.000 | 59.9 [59.9, 59.9] | 59.9 | 59.9 |

- **Corrected 2023 → 2026 rise (primary):** 21.0% → 40.5% (+19.4 pp), against 20.3% → 40.5% observed (+20.2 pp).
  - Against the lenient construct: 21.9% → 42.2% (+20.3 pp).
  - Against the strict construct: 20.8% → 40.3% (+19.6 pp).

### D1 ITS with block-specific misclassification
- **Model:**
  - D1 specification: U 2017–26, `name_primary ~ tc + post + post×tc + log_authors + llm_topic + topic100 FE`, CRV1 by topic100.
  - Fitted by maximum likelihood with P(observed = 1 | x) = (1 − Sp_b) + (Se_b + Sp_b − 1)·expit(x′β), Se/Sp by year block.
  - Uncertainty: the corrected CI adds the between-draw variance from refitting on 200 stratified-bootstrap draws of (Se_b, Sp_b) to the sandwich variance.
- **Reproduction check:** the in-house uncorrected fit gives OR 1.0975; the D1 file (`its_results.json`) gives 1.0975.

| outcome (construct) | Se/Sp draws | uncorrected OR [95% CI] | corrected OR [95% CI] | OR ratio | log-OR change | within 10% (OR) | within 10% (log OR) |
|---|---|---|---|---|---|---|---|
| name_primary | 200 | 1.098 [1.044, 1.154] | 1.090 [1.033, 1.151] | 0.994 | -6.9% | yes | yes |
| name_loose | 100 | 1.112 [1.060, 1.166] | 1.069 [1.011, 1.129] | 0.961 | -37.3% | yes | no |
| name_strict | 0 | 1.098 [1.043, 1.155] | 1.100 [1.045, 1.158] | 1.002 | +2.1% | yes | yes |
| name_compound | 0 | 1.231 [1.176, 1.289] | 1.231 [1.176, 1.289] | 1.000 | -0.0% | yes | yes |
| name_primary|lenient | 100 | 1.098 [1.044, 1.154] | 1.114 [1.044, 1.188] | 1.015 | +16.0% | yes | no |
| name_primary|strict | 100 | 1.098 [1.044, 1.154] | 1.094 [1.037, 1.154] | 0.997 | -3.6% | yes | yes |

- **Main-only (HT) Se/Sp check:** corrected OR 1.119 (sandwich CI 1.061–1.180).
- **Cross-detector consistency:** the loose detector, corrected against the same NAME construct, gives 1.069 [1.011, 1.129].
  - Uncorrected, loose gives 1.112.
  - If misclassification is non-differential within blocks, both detectors should recover the same latent slope change.
  - The two corrected CIs overlap.
- **Bootstrap draws:** 100% of corrected ORs lie within 10% of the uncorrected OR. Draw quantiles of the corrected OR: 1.074 / 1.090 / 1.103.
- **Aggregate cross-check:** WLS on the logit of 10 yearly shares gives a slope change of 0.169 (observed) and 0.168 (RG-corrected); OR ratio 0.999.
- **Reading:**
  - The correction assumes misclassification is non-differential within a block (independent of topic, team size and llm_topic) and that the consensus is the truth.
  - The "within 10%" criterion is pre-registered on the OR scale. Because the OR is close to 1, the log-OR change is the more demanding comparison and is reported next to it.

Figures: `fig_v1_name_detector_precision_recall.{pdf,png,csv}`, `fig_v1_name_share_corrected.{pdf,png,csv}`.

## V2. Slot sense and swap preservation
- **Sample:** 400 slot-filled titles, 2018+, stratified by slot × variant × era × word.
- **Agreement:** slot_sense κ = 0.925 [0.851, 0.984] (5 disagreements); swap_preserves κ = 0.784 [0.672, 0.872] (18 disagreements).
  - The swap test is the more subjective judgement, as expected.
  - 20 items were adjudicated (`v2_adjudications.csv`). Rule: swap preserves meaning when the new title describes the same kind of contribution about the same object, ignoring tone. 'Unveiling X' fails when X is not hidden or when it implies discovering rather than analysing X.

**Per word.** Columns:
- "weighted": design-weighted sense precision over eras (weights N/n); this is the drop rule, < 0.85.
- "k/n [Wilson]": unweighted sampled share with its Wilson 95% CI.

| slot | variant | word | weighted | k/n [Wilson] | after pre-V2 filter | pre / post | swap preserves | N_population | DROP |
|---|---|---|---|---|---|---|---|---|---|
| exploit | llm | harnessing | 0.97 | 13/15 [0.62, 0.96] | 0.97 | 0.75 (n=8) / 1.00 (n=7) | 0.97 | 60 | borderline |
| exploit | llm | leveraging | 1.00 | 24/24 [0.86, 1.00] | 1.00 | 1.00 (n=16) / 1.00 (n=8) | 1.00 | 198 |  |
| exploit | llm | unleashing | 0.97 | 10/12 [0.55, 0.95] | 0.97 | 0.60 (n=5) / 1.00 (n=7) | 0.70 | 59 | borderline |
| exploit | llm | unlocking | 0.29 | 2/7 [0.08, 0.64] | 0.29 |  (n=0) / 0.29 (n=7) | 0.29 | 87 | **drop** |
| exploit | neutral | enabling | 0.00 | 0/21 [0.00, 0.15] | 0.00 | 0.00 (n=11) / 0.00 (n=10) | 0.00 | 73 | **drop** |
| exploit | neutral | exploiting | 1.00 | 22/22 [0.85, 1.00] | 1.00 | 1.00 (n=12) / 1.00 (n=10) | 1.00 | 67 |  |
| exploit | neutral | utilizing | 1.00 | 15/15 [0.80, 1.00] | 1.00 | 1.00 (n=6) / 1.00 (n=9) | 1.00 | 17 |  |
| improve | llm | advancing | 1.00 | 9/9 [0.70, 1.00] | 1.00 | 1.00 (n=3) / 1.00 (n=6) | 1.00 | 106 |  |
| improve | llm | boosting | 0.97 | 16/18 [0.67, 0.97] | 0.97 | 0.83 (n=12) / 1.00 (n=6) | 0.97 | 125 | borderline |
| improve | llm | elevating | 1.00 | 5/5 [0.57, 1.00] | 1.00 |  (n=0) / 1.00 (n=5) | 1.00 | 10 |  |
| improve | llm | empowering | 1.00 | 9/9 [0.70, 1.00] | 1.00 | 1.00 (n=3) / 1.00 (n=6) | 0.84 | 51 |  |
| improve | llm | enhancing | 1.00 | 17/17 [0.82, 1.00] | 1.00 | 1.00 (n=11) / 1.00 (n=6) | 1.00 | 433 |  |
| improve | neutral | improving | 1.00 | 58/58 [0.94, 1.00] | 1.00 | 1.00 (n=29) / 1.00 (n=29) | 1.00 | 434 |  |
| reveal | llm | decoding | 0.39 | 3/8 [0.14, 0.69] | 0.63 | 0.33 (n=3) / 0.40 (n=5) | 0.39 | 16 | **drop** |
| reveal | llm | demystifying | 1.00 | 13/13 [0.77, 1.00] | 1.00 | 1.00 (n=8) / 1.00 (n=5) | 1.00 | 39 |  |
| reveal | llm | uncovering | 1.00 | 10/10 [0.72, 1.00] | 1.00 | 1.00 (n=4) / 1.00 (n=6) | 0.67 | 43 |  |
| reveal | llm | unraveling | 1.00 | 6/6 [0.61, 1.00] | 1.00 | 1.00 (n=1) / 1.00 (n=5) | 1.00 | 13 |  |
| reveal | llm | unravelling | 1.00 | 2/2 [0.34, 1.00] | 1.00 |  (n=0) / 1.00 (n=2) | 1.00 | 2 |  |
| reveal | llm | unveiling | 1.00 | 8/8 [0.68, 1.00] | 1.00 | 1.00 (n=2) / 1.00 (n=6) | 0.68 | 45 |  |
| reveal | neutral | analysing | 1.00 | 3/3 [0.44, 1.00] | 1.00 | 1.00 (n=2) / 1.00 (n=1) | 1.00 | 3 |  |
| reveal | neutral | analyzing | 1.00 | 10/10 [0.72, 1.00] | 1.00 | 1.00 (n=5) / 1.00 (n=5) | 0.80 | 47 |  |
| reveal | neutral | characterising | 1.00 | 6/6 [0.61, 1.00] | 1.00 | 1.00 (n=2) / 1.00 (n=4) | 0.83 | 6 |  |
| reveal | neutral | characterizing | 1.00 | 9/9 [0.70, 1.00] | 1.00 | 1.00 (n=5) / 1.00 (n=4) | 0.77 | 31 |  |
| reveal | neutral | explaining | 1.00 | 10/10 [0.72, 1.00] | 1.00 | 1.00 (n=5) / 1.00 (n=5) | 0.80 | 51 |  |
| reveal | neutral | investigating | 1.00 | 10/10 [0.72, 1.00] | 1.00 | 1.00 (n=5) / 1.00 (n=5) | 0.80 | 46 |  |
| reveal | neutral | understanding | 1.00 | 10/10 [0.72, 1.00] | 1.00 | 1.00 (n=5) / 1.00 (n=5) | 1.00 | 306 |  |
| study_adj | llm | comprehensive | 1.00 | 32/32 [0.89, 1.00] | 1.00 | 1.00 (n=3) / 1.00 (n=29) | 1.00 | 69 |  |
| study_adj | neutral | extensive | 1.00 | 4/4 [0.51, 1.00] | 1.00 |  (n=0) / 1.00 (n=4) | 1.00 | 4 |  |
| study_adj | neutral | large-scale | 1.00 | 12/12 [0.76, 1.00] | 1.00 |  (n=0) / 1.00 (n=12) | 1.00 | 14 |  |
| study_adj | neutral | systematic | 0.93 | 14/15 [0.70, 0.99] | 0.93 | 1.00 (n=3) / 0.92 (n=12) | 0.93 | 22 |  |

**Per slot side and era** (design-weighted):

| slot | variant | era | n | precision_w | swap_w | precision_w_after_drops |
|---|---|---|---|---|---|---|
| exploit | neutral | post | 29 | 0.47 | 0.47 | 1.00 |
| exploit | neutral | pre | 29 | 0.70 | 0.70 | 1.00 |
| exploit | llm | post | 29 | 0.83 | 0.79 | 1.00 |
| exploit | llm | pre | 29 | 0.90 | 0.90 | 0.90 |
| improve | neutral | post | 29 | 1.00 | 1.00 | 1.00 |
| improve | neutral | pre | 29 | 1.00 | 1.00 | 1.00 |
| improve | llm | post | 29 | 1.00 | 0.99 | 1.00 |
| improve | llm | pre | 29 | 0.92 | 0.92 | 0.92 |
| reveal | neutral | post | 29 | 1.00 | 0.92 | 1.00 |
| reveal | neutral | pre | 29 | 1.00 | 0.92 | 1.00 |
| reveal | llm | post | 29 | 0.94 | 0.75 | 1.00 |
| reveal | llm | pre | 18 | 0.89 | 0.83 | 1.00 |
| study_adj | neutral | post | 28 | 0.96 | 0.96 | 0.96 |
| study_adj | neutral | pre | 3 | 1.00 | 1.00 | 1.00 |
| study_adj | llm | post | 29 | 1.00 | 1.00 | 1.00 |
| study_adj | llm | pre | 3 | 1.00 | 1.00 | 1.00 |

**By opener rule of the sampled title:**

| source | n | sense | swap |
|---|---|---|---|
| al_only | 66 | 0.83 | 0.77 |
| primary | 271 | 0.90 | 0.86 |
| study_adj | 63 | 0.98 | 0.98 |

- **Notes:**
  - 'enabling' (exploit, neutral side) is never used in the exploit sense: it means making something possible.
  - 'unlocking' mostly means enabling a capability.
  - 'decoding' is mostly the technical operation, even after the pre-V2 filter.
  - **Borderline (kept):** unweighted or single-era precision is below 0.85. exploit/harnessing: weighted 0.97, unweighted 0.87, pre 0.75 (n=8), post 1.00 (n=7); exploit/unleashing: weighted 0.97, unweighted 0.83, pre 0.60 (n=5), post 1.00 (n=7); improve/boosting: weighted 0.97, unweighted 0.89, pre 0.83 (n=12), post 1.00 (n=6).
    - In each case the sense failures sit in the pre era, on the LLM-favoured side. That inflates the pre-2024 LLM share and biases the slot break toward zero. D3 should run leave-one-variant-out on these words.
  - **Unweighted-rule sensitivity:** the drop set would be exploit: enabling, unleashing, unlocking; reveal: decoding.
  - **Swap preservation:** the reveal slot is the weakest (LLM side 0.79, neutral side 0.92, weighted mean over eras). Swapping 'Unveiling' for 'Understanding' often changes the claim (discovering vs explaining), so reveal-slot shifts are partly shifts in what is claimed, not only in wording.
  - **Opener rule:** titles that fill a slot only under the any-lead rule (`_al`) have lower sense precision (0.83, n=66) than titles filled under the primary rule (0.90, n=271). This supports the primary opener rule in D3.

## V3. Fingerprints and register
### Convergent validity (weak; not ground truth)
- **Design:** one LLM rater, blind to the fingerprint words, rated 300 abstracts from 2024–26 (25 per year × fingerprint stratum) on a 1–5 scale of how likely the abstract is LLM-written or LLM-polished.
- **Circularity caveat:** the rubric does not name the RARE21 words, but an LLM rater is likely to know them. Part of the F24 correlation may therefore be mechanical.

| fingerprint | Spearman ρ [95% CI] | auc | mean_rating_pos | mean_rating_neg |
|---|---|---|---|---|
| F_any | 0.25 [0.14, 0.35] | 0.66 | 2.67 | 2.03 |
| f24 | 0.31 [0.21, 0.41] | 0.67 | 2.85 | 2.17 |
| f24_n | 0.32 [0.20, 0.42] |  | 2.85 | 2.17 |
| f26 | 0.10 [-0.01, 0.22] | 0.56 | 2.64 | 2.38 |
| f26_words | 0.06 [-0.06, 0.17] | 0.54 | 2.62 | 2.43 |
| f26_typo | 0.10 [-0.01, 0.20] | 0.59 | 2.79 | 2.47 |
| title_typo | 0.09 [0.03, 0.15] | 0.72 | 3.25 | 2.50 |

Mean rating by year × fingerprint stratum:

| year | F0 | F24_and_F26typo | F24_only | F26typo_only |
|---|---|---|---|---|
| 2024 | 1.64 | 2.40 | 2.72 | 1.52 |
| 2025 | 1.92 | 2.96 | 2.56 | 2.12 |
| 2026 | 2.52 | 3.56 | 2.92 | 3.28 |

- **Within-year Spearman ρ (F vs rating):** 2024: 0.27, 2025: 0.26, 2026: 0.27.
  - Design-weighted Pearson r(F, rating) over 2024–26 = 0.29.
- **Ratings of unfingerprinted (F = 0) abstracts rise with year** (Spearman ρ = 0.34, p = 0.003).
  - This is consistent with undetected LLM use growing among unflagged papers (fingerprint recall decays), or with general register drift. Either way it supports the plan's position that recall is unknown and tool estimates are bounds.

### Specificity: fingerprint rates in 2021–22 (pre-ChatGPT, so every hit is a false positive)

| flag | hits_2021_22 | FPR % [95% CI] | rate_2024 | rate_2025 | rate_2026 | excess share 2024–26 |
|---|---|---|---|---|---|---|
| f24 | 145 | 2.89 [2.45, 3.40] | 19.15 | 15.31 | 9.15 | 0.78 |
| f24_2 | 2 | 0.04 [0.00, 0.14] | 4.77 | 2.52 | 0.73 | 0.98 |
| f26_words | 143 | 2.85 [2.41, 3.35] | 2.32 | 2.41 | 10.09 | 0.55 |
| abs_nbhyphen | 0 | 0.00 [0.00, 0.07] | 0.00 | 0.00 | 1.25 | 1.00 |
| abs_endash_compound | 16 | 0.32 [0.18, 0.52] | 0.23 | 0.29 | 8.18 | 0.93 |
| f26_typo | 17 | 0.34 [0.20, 0.54] | 0.23 | 0.32 | 9.94 | 0.94 |
| f26 | 159 | 3.17 [2.71, 3.70] | 2.55 | 2.74 | 18.56 | 0.71 |
| title_typo | 2 | 0.04 [0.00, 0.14] | 0.00 | 0.06 | 1.36 | 0.94 |
| title_nbhyphen | 0 | 0.00 [0.00, 0.07] | 0.00 | 0.00 | 0.39 | 1.00 |
| title_endash_compound | 2 | 0.04 [0.00, 0.14] | 0.00 | 0.06 | 1.01 | 0.92 |
| F_any | 298 | 5.95 [5.31, 6.64] | 21.09 | 17.61 | 26.22 | 0.74 |

- **Columns:**
  - rate_YYYY: share of U papers flagged in that year.
  - Excess share: 1 − FPR / (2024–26 rate), the share of 2024–26 hits above the pre-LLM baseline.
- **Most frequent RARE21 words in 2021–22 hits:** showcase (48), encompass (18), harness (10), intricate (10), endeavor (9), pivotal (8), unveil (8), innovative (7), multifaceted (6), garner (4).

### Manual inspection of title typography hits
- **Sample:** 50 of the 60 U+2011 titles and 50 of the 158 letter–en dash–letter titles without U+2011, drawn at random. All 218 hits are in `v3_typography_inspection.csv` as sampled.

| class | n | description |
|---|---|---|
| nbh_compound | 49 | U+2011 inside ordinary hyphenated words or compound modifiers (e.g. Source-Free, End-to-End) |
| nbh_in_name | 1 | U+2011 only inside a coined name |
| en_eponym | 7 | en dash between personal names (Kolmogorov-Arnold, Weisfeiler-Leman): standard typography |
| en_relation | 34 | en dash between parallel terms (Vision-Language, Teacher-Student, Actor-Critic): standard typography |
| en_open_compound | 6 | en dash joining an open compound to a modifier (Sliding Window-Based): Chicago-style |
| en_nonstandard | 3 | en dash where a hyphen is standard (Anchor-MoE, GraphIP-Bench, Land-Surface) |

- **Result:** none of the 100 shows a LaTeX or PDF conversion artefact. There is no math, line-break hyphenation, soft hyphen or ligature damage, and no hit sits inside a LaTeX span.
- **U+2011 hits:**
  - Every one is an ordinary hyphenated compound (Source‑Free, End‑to‑End). LaTeX and PDF text extraction do not produce U+2011 for a typed hyphen.
  - 16 of 50 also contain an ASCII hyphen elsewhere in the same title, which points to pasted fragments rather than a whole-title conversion.
  - U+2011 is absent from every title before 2026.
- **En-dash hits:**
  - 7 of 50 join personal names (Kolmogorov–Arnold). This is standard typography, typical of LaTeX `--` pasted from a PDF, and the kind of hit that also occurs before 2024. These are false positives for an LLM marker.
  - 34 join parallel terms (Vision–Language). This is standard style, compatible with LaTeX, careful human typing or LLM output.
  - 6 are Chicago-style open-compound modifiers and 3 are nonstandard.
- **No export-level conversion:** ASCII `--` between letters persists in 2026 titles and abstracts (table below), so the 2026 spike is not a blanket `--` → en dash conversion by the export.

| year | n | title_endash_letters | title_u2011 | title_ascii_dd_letters | abstract_ascii_dd_letters | abstract_endash_letters | abstract_u2011 |
|---|---|---|---|---|---|---|---|
| 2017 | 384 | 0 | 0 | 0 | 0 | 3 | 0 |
| 2018 | 769 | 0 | 0 | 0 | 1 | 2 | 0 |
| 2019 | 1248 | 0 | 0 | 0 | 1 | 1 | 0 |
| 2020 | 2070 | 1 | 0 | 2 | 10 | 5 | 0 |
| 2021 | 2360 | 2 | 0 | 0 | 13 | 6 | 0 |
| 2022 | 2649 | 0 | 0 | 0 | 10 | 10 | 0 |
| 2023 | 3872 | 0 | 0 | 0 | 9 | 9 | 0 |
| 2024 | 5765 | 0 | 0 | 0 | 17 | 13 | 0 |
| 2025 | 8953 | 5 | 0 | 0 | 45 | 26 | 0 |
| 2026 | 15412 | 155 | 60 | 6 | 174 | 1261 | 193 |

Title hits before 2026 (all of them):

| submission_id | year | title |
|---|---|---|
| HJeIrlSFDH | 2020 | Resolving Lexical Ambiguity in English–Japanese Neural Machine Translation |
| H-AAaJ9v_lE | 2021 | Legendre Deep Neural Network (LDNN) and its application for approximation of nonlinear Volterra–Fredholm–Hammerstein integral equations |
| gIHd-5X324 | 2021 | Rethinking Soft Labels for Knowledge Distillation: A Bias–Variance Tradeoff Perspective |
| Odtr1rzQMq | 2025 | Nonasymptotic Analysis of Stochastic Gradient Descent with the Richardson–Romberg Extrapolation |
| q5zMyAUhGx | 2025 | Generalization Bounds and Model Complexity for Kolmogorov–Arnold Networks |
| qkBBHixPow | 2025 | PIORF: Physics-Informed Ollivier-Ricci Flow for Long–Range Interactions in Mesh Graph Neural Networks |
| udfjje2xXb | 2025 | Kolmogorov–Arnold Graph Neural Networks |
| zf777Odl6J | 2025 | KA-GAT: Kolmogorov–Arnold based Graph Attention Networks |

- **Implication:** the en-dash part of the typography marker carries a non-LLM component (eponym pairs, standard relation dashes). The U+2011 part has no pre-2026 baseline at all.

## V4. Name-masking leakage
- **R3 mask** (bge input; lead + CamelCase/ALLCAPS tokens → [NAME]):
  - The lead survives (case-insensitive, whole word) in **0 of 12,928** NAME abstracts from 2018–26 (0.00%). The features_v2 column gives 0.
  - Target 0%: **met**.
- **R1 mask** (TF-IDF input; lead dropped, lowercase tokens kept): the lead survives in 22 (0.17%).
  - Examples: 'ResGrad', 'FluidLab', 'MARLlib', 'DrS', 'AvatarStudio', 'UniAudio', 'FairSeg', 'Skills-in-Context Prompting'.
  - As D1 found, these are leads whose lowercase letter run survives in a URL or with a digit suffix (e.g. 'resgrad1' → 'resgrad').
- **Unchecked leads:** 2 leads have fewer than 2 alphanumeric characters (e.g. 'Q*') and cannot be checked by string match.
- **Stricter substring test** (lead core of ≥ 3 characters anywhere in the alphanumeric masked text, no word boundary): 245 hits for R3 and 175 for R1.
  - URL or handle containing the lead: 74 (e.g. JAX MD → github.com/jaxmd/[name]; BBRefinement → https://gitlab.com/irafm-ai/bb-refinement.; FastSpeech 2 → https://speechresearch.github.io/fastspeech2/.; ResGrad → \url{https://resgrad1.github.io/}.).
  - lead letters + suffix (mostly ordinary words: flow-based, stitching, divergence): 81 (e.g. Flow++ → flow-based; CAMOU → camouflage; CrossNorm → cross-normalization.; MetaPoison → meta-poisoning).
  - lead letters inside a longer word (coincidental: space, complex): 59 (e.g. ACE → space; TED → generated; PLEX → complex; Xi-learning → $\xi$-learning,).
  - variant spelling of the lead (LaTeX, markdown, Unicode hyphen; or its plural): 31 (e.g. q-Neurons → $q$-neurons,; h-detach → (\textit{h}-detach); Kanerva++ → kanerva; $i$-Mix → i-mix,).
  - **Leak (variant spellings).** The 'variant spelling' and 'URL' categories are real leaks: the name survives in a variant spelling the whole-word lead pattern does not match. Such variants are LaTeX-wrapped (`$q$-neurons`), markdown-emphasised, use a different Unicode hyphen, or sit inside a project URL.
    - R3: about 105 NAME abstracts (0.81%).
    - R1: about 46 (0.36%).
    - The counts are approximate in both directions. LaTeX-symbol spellings (`$\pi$-light`, `$\xi$-learning`) escape the string test, while a few hits mention a base name the lead builds on ('adam' for 'Adam$^+$').
    - The pre-registered whole-word test (0%) is therefore met, but the masks are not leak-free.
    - The leak is small, but D1 R3 should note it. Masking URLs and matching on a normalised form (LaTeX and markdown stripped, hyphens unified) would close most of it.
  - **Not leaks:** the 'lead letters' categories are ordinary words that share the lead's letters. The full list is `v4_r3_substring_hits.csv`.
- **Masked-vs-unmasked AUC gap** (from D1 `T1_2_representations.csv`): R1u-R1: fixed +0.004, placebo -0.002, rolling +0.003; R4-R3: fixed +0.014, placebo +0.025, rolling +0.019.
- **Name fragments among the top-200 R1 features:** 21 (adopt, agent, attention, code, control, cost, design, etc, first, great, large, most, pose, scale, search, self).
  - This is a token match against NAME lead strings. Matches are ordinary words that are also used as names, not leaked identifiers.
- **Not masked:** 34 NAME papers from 2017 are outside the masked set (R3 covers 2018–26).

## V5. Topics
- **Labels:** one LLM pass labelled all 100 MiniLM topic100 clusters from their 12 most central papers. The table is `topic100_labels.csv`.
- **Annotator LM flag vs the regex LLM-cluster rule** (> 50% of the cluster's U papers match the LLM regex): κ = 0.857 [0.707, 0.968], raw agreement 95%.

|  | annotator: about LMs | annotator: not |
|---|---|---|
| regex rule: LLM cluster | 20 | 0 |
| regex rule: not | 5 | 75 |

- **All 5 disagreements go the same way:** the annotator says 'about LMs', the rule says no.
  - These clusters' all-years regex shares are 0.45, 0.45, 0.34, 0.47, 0.39.
  - Their 2024–26 regex shares are 0.48, 0.59, 0.63, 0.54, 0.53.
  - The central papers shown skew recent, so the annotator sees the clusters' current, LLM-heavier composition. The two flags measure the same thing at different time windows.
- **Rank agreement:** Spearman ρ(regex share, annotator LM count) = 0.85. Paper by paper on the same 12 shown papers, ρ(regex hits, annotator count) = 0.92. The regex count exceeds the annotator's count by +0.32 papers per cluster on average.
- **Manual check of 10 clusters** (the 5 disagreements and 5 random agreements; `topic100_labels.csv`, manual_* columns):

| topic100 | label | about_lms | lm_papers | llm_regex_share | manual_label_verdict | manual_lm_verdict | manual_note |
|---|---|---|---|---|---|---|---|
| 4 | LLM mathematical and logical reasoning | y | 8 | 0.45 | accurate | agree | my count 8-9 LM papers |
| 18 | Neural PDE solvers and operators | n | 0 | 0.02 | accurate | agree | no LM papers |
| 35 | Multimodal LLMs and modality integration | y | 7 | 0.45 | too narrow | borderline | about half the shown papers are general multimodal learning without LMs; my count 6-7 |
| 45 | Vision-language-action models for robotics | y | 11 | 0.47 | accurate | agree | VLA/VLM robotics; my count 10-11 |
| 62 | Protein and biological sequence modeling | n | 2 | 0.37 | accurate | agree | protein LMs are not natural-language LMs under the codebook; 2 LLM papers |
| 66 | Low-bit neural network quantization | y | 7 | 0.39 | accurate | borderline | half LLM post-training quantization, half general DNN quantization; my count 6-7 |
| 67 | Robust deep image classification | n | 0 | 0.01 | slightly off | agree | 'robust' is over-specific; 'image classification and visual representations' fits better |
| 87 | Sentence embeddings and text representations | y | 7 | 0.34 | accurate | borderline | older sentence/word-embedding papers are not LM papers; my count about 7 |
| 94 | Knowledge distillation for model compression | n | 4 | 0.18 | accurate | agree | my count 4-5 |
| 98 | Geometric manifold representation learning | n | 0 | 0.02 | accurate | agree | no LM papers |

- **Topic stability, MiniLM vs bge (recomputed on U):**
  - k=100: ARI 0.421, NMI 0.666.
  - k=50: ARI 0.470, NMI 0.642.
  - Paper-level LLM flags: cluster flag κ = 0.780, union flag (llm_topic) κ = 0.927.
  - Partitions agree only moderately, but the LLM flag that enters the models is stable across encoders.

## V6. Author keys
Keys are exact declared-ID keys (SHA-256 of the declared ID). They are declared profile keys, not people.

| year | native_id_kind | n_keys | mean | median | p90 | p99 | max | share_single | over_40 |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | email | 1177 | 1.20 | 1.00 | 2.00 | 4.00 | 6 | 0.86 | 0 |
| 2017 | other | 1 | 1.00 | 1.00 | 1.00 | 1.00 | 1 | 1.00 | 0 |
| 2018 | email | 2341 | 1.20 | 1.00 | 2.00 | 4.00 | 9 | 0.86 | 0 |
| 2018 | other | 18 | 1.00 | 1.00 | 1.00 | 1.00 | 1 | 1.00 | 0 |
| 2019 | email | 3939 | 1.25 | 1.00 | 2.00 | 4.00 | 20 | 0.84 | 0 |
| 2019 | profile | 3 | 1.00 | 1.00 | 1.00 | 1.00 | 1 | 1.00 | 0 |
| 2020 | email | 6585 | 1.28 | 1.00 | 2.00 | 5.00 | 20 | 0.83 | 0 |
| 2020 | profile | 4 | 1.00 | 1.00 | 1.00 | 1.00 | 1 | 1.00 | 0 |
| 2021 | email | 1400 | 1.05 | 1.00 | 1.00 | 2.00 | 4 | 0.96 | 0 |
| 2021 | other | 14 | 1.00 | 1.00 | 1.00 | 1.00 | 1 | 1.00 | 0 |
| 2021 | profile | 5943 | 1.39 | 1.00 | 2.00 | 6.00 | 24 | 0.78 | 0 |
| 2022 | email | 640 | 1.02 | 1.00 | 1.00 | 2.00 | 4 | 0.98 | 0 |
| 2022 | profile | 8107 | 1.35 | 1.00 | 2.00 | 5.00 | 17 | 0.80 | 0 |
| 2023 | email | 828 | 1.02 | 1.00 | 1.00 | 2.00 | 2 | 0.98 | 0 |
| 2023 | profile | 12040 | 1.40 | 1.00 | 2.00 | 6.00 | 24 | 0.78 | 0 |
| 2024 | email | 233 | 1.04 | 1.00 | 1.00 | 2.00 | 2 | 0.96 | 0 |
| 2024 | profile | 19162 | 1.45 | 1.00 | 2.00 | 7.00 | 27 | 0.77 | 0 |
| 2025 | profile | 31643 | 1.50 | 1.00 | 3.00 | 7.00 | 31 | 0.75 | 0 |
| 2026 | profile | 54156 | 1.61 | 1.00 | 3.00 | 8.00 | 40 | 0.72 | 0 |

- **Key-years with more than 40 papers:** 0 in total, listed in `v6_keys_over40.csv` (key prefix only; profile IDs are not printed).
  - The largest exact key-year count is 40 papers (2026).
  - After the alias collapse below, 7 alias-years exceed 40 (max 64). These are homonym merges, not plausible single authors.

**Alias sensitivity** (profile IDs with trailing digits removed; this merges homonymous profiles and duplicate profiles of one person, so it over-links and is an upper bound on missed linkage):

| year | profile_keys | aliases | keys_per_alias | alias_over_40 | key_over_40 | alias_max_papers |
|---|---|---|---|---|---|---|
| 2019 | 3 | 3 | 1.000 | 0 | 0 | 1 |
| 2020 | 4 | 4 | 1.000 | 0 | 0 | 1 |
| 2021 | 5943 | 5834 | 1.019 | 0 | 0 | 24 |
| 2022 | 8107 | 7953 | 1.019 | 0 | 0 | 18 |
| 2023 | 12040 | 11600 | 1.038 | 0 | 0 | 24 |
| 2024 | 19162 | 18190 | 1.053 | 0 | 0 | 40 |
| 2025 | 31643 | 29458 | 1.074 | 1 | 0 | 41 |
| 2026 | 54156 | 48363 | 1.120 | 6 | 0 | 64 |

- **Merging:** over 2021–26, 89,116 profile keys collapse to 78,256 aliases.
  - 5,399 aliases merge two or more keys; they hold 20.6% of profile author rows.
- **Effect on 2022+ paper covariates** (36,650 papers):
  - r(log max_prior_subs) exact vs alias = 0.882; max_prior_subs changes for 25.8% of papers.
  - r(share_new_authors) = 0.929; share_new_authors changes for 24.2% of papers, with mean 0.552 → 0.495.

**Email-key vs profile-key eras** (positions by ID kind; mean paper-level share of new authors from exact keys):

| year | n | mean_share_new | mean_max_prior_subs | positions | with_key | email | missing | other | profile |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 384 | 1.000 | 0.000 | 1423 | 0.997 | 0.996 | 0.003 | 0.001 | 0.000 |
| 2018 | 769 | 0.842 | 0.744 | 2870 | 0.986 | 0.980 | 0.014 | 0.006 | 0.000 |
| 2019 | 1248 | 0.758 | 1.655 | 4961 | 0.991 | 0.990 | 0.009 | 0.000 | 0.001 |
| 2020 | 2070 | 0.699 | 2.390 | 8482 | 0.994 | 0.994 | 0.006 | 0.000 | 0.000 |
| 2021 | 2360 | 0.996 | 0.025 | 9749 | 1.000 | 0.151 | 0.000 | 0.001 | 0.848 |
| 2022 | 2649 | 0.680 | 2.327 | 11605 | 1.000 | 0.056 | 0.000 | 0.000 | 0.944 |
| 2023 | 3872 | 0.594 | 4.188 | 17644 | 1.000 | 0.048 | 0.000 | 0.000 | 0.952 |
| 2024 | 5765 | 0.562 | 5.920 | 27999 | 1.000 | 0.009 | 0.000 | 0.000 | 0.991 |
| 2025 | 8953 | 0.533 | 7.863 | 47467 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2026 | 15412 | 0.525 | 9.702 | 87398 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 |

- **2021 break:** ID kind switches from email to profile, so 2021 keys have no history. The share of new authors jumps in 2021 and is not comparable across the switch, which is why the experience covariates are used from 2022 on (`exp_valid`).

## Deviations from PLAN.md section 3 and notes
- Annotation passes are LLM subagents (as planned). V3 and V5 have one pass each (as planned); V1 and V2 have two.
- V1 consensus error: the 150 spot checks were done by the adjudicator (PI's delegate), not an independent reviewer.
- V1 precision/recall use the main stratified sample with design weights; the 200 hard cases are reported separately (they overlap the main strata, so pooling would double-count).
- V1 ITS correction uses year-BLOCK-specific Se/Sp (2017-19, 2020-22, 2023, 2024, 2025, 2026), because the validation sample was stratified by block; the plan says 'year-specific'.
- V1 'within 10%' is evaluated on the OR scale as pre-registered; the log-OR change is reported alongside.
- V2 drop rule applied to the design-weighted sense precision of each slot word over the population sampled by WP3a (2018+, either opener rule, before the heuristic pre-V2 filter); post-filter precision is also reported.
- V3: 2021-22 used as the pre-ChatGPT specificity window (ICLR 2023 submissions closed in September 2022, before ChatGPT's release, so 2023 could also serve).
- V5 used 12 central papers per cluster (WP3a deviation); 'LLM topic' agreement compares the annotator's flag with the MiniLM >50% regex cluster rule (llm_cluster), not with llm_topic (which is paper-level).
- V6 key-year flags print key prefixes only; profile IDs are not printed.

## Files
- `VALIDATION.md`
- `annotate_manifest.json`
- `fig_v1_name_detector_precision_recall.csv`
- `fig_v1_name_detector_precision_recall.pdf`
- `fig_v1_name_detector_precision_recall.png`
- `fig_v1_name_share_corrected.csv`
- `fig_v1_name_share_corrected.pdf`
- `fig_v1_name_share_corrected.png`
- `sample_design.csv`
- `slot_variants_dropped.json`
- `topic100_labels.csv`
- `v1_adjudications.csv`
- `v1_casing_metrics.csv`
- `v1_consensus.csv`
- `v1_detector_metrics.csv`
- `v1_hard_cases.csv`
- `v1_kappa.csv`
- `v1_name_false_negatives.csv`
- `v1_name_false_positives.csv`
- `v1_orthography_metrics.csv`
- `v1_rogan_gladen.csv`
- `v1_spotcheck.csv`
- `v1_two_token_cells.csv`
- `v2_adjudications.csv`
- `v2_consensus.csv`
- `v2_slot_metrics.csv`
- `v2_word_metrics.csv`
- `v3_dash_codepoints_by_year.csv`
- `v3_fingerprint_rates_by_year.csv`
- `v3_fpr_2021_22.csv`
- `v3_ratings.csv`
- `v3_typography_inspection.csv`
- `v4_mask_checks.csv`
- `v4_r3_substring_hits.csv`
- `v6_alias_covariate_effect.csv`
- `v6_alias_sensitivity.csv`
- `v6_email_profile_eras.csv`
- `v6_keys_over40.csv`
- `v6_papers_per_key.csv`
- `validation.json`
