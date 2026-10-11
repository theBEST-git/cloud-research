# D3 fix log (machine register; fixer pass after three audits)

Date: 2026-10-11. Scope: `src/analyses/d3_slots.py`, `d3_register.py`, `d3_vintage.py`, `d3_signature_bound.py`, `d3_collect.py` and `outputs/d3_register/`.
- Pre-fix copies of the five scripts and of every output are in `outputs/audit/d3/pre_fix_backup/` (`scripts/` and `outputs/`).
- PLAN.md, D1/D2/D4 files and `figures.py` were not modified. No git commands were run.
- Every issue was re-checked by running code before anything was changed. The auditors' scripts `d3_code/check3`, `check4`, `check7`, `check8` and `check9` were re-run, and the `d3_ident` numbers were reproduced inside the new direction code.

## Code changes

### `d3_slots.py` (C5, C6, R1, R7, R9, ID-3, ID-7)
- `ENLARGE_N = 1620`: the camera-ready audit reads only the first 1,620 lines of the append-only `cache/arxiv_audit_enlarge.jsonl`. The meta records the lines used and the file length at run time.
- `audit()`: the bootstrap DiD CI is replaced by exact Clopper–Pearson intervals for per-arm add and drop rates; the DiD is a point estimate with its number of flip events; a V7 auditability flag is added.
- `event_study()`: relabelled "trends estimated jointly", with a `trends` column.
- New `event_study_frozen()` / `_frozen_fit()`: trends fitted on 2018–22 only and passed as an offset; opener slots, controls, controls without via, and both contrasts. CIs come from a topic100-cluster bootstrap over both stages (300 draws); the conditional cluster CIs are kept as `OR_lo_cond` / `OR_hi_cond`.
- New `variant_rates()`: per-1,000-title rates of LLM-favoured and neutral variants per slot and pooled (all papers, NA pool, non-LLM subset), plus a quasi-Poisson level shift against the 2018–23 trend → `slot_variant_rates.csv`, `slot_variant_rate_shift.csv`.
- Robustness: a truly pilot-like row (any-lead rule + full lexicon); the old "pilot-like" row is relabelled "any-compound-lead opener rule (V2 drops kept)". T3.1 block D adds the pilot-like and level-contrast rows.
- `fig_f31()`: three panels (shares + pooled-slot line; per-1k rates; controls with Wilson bands), a legend below, and a note listing omitted cells with n < 10. The CSV keeps the `pooled_slots` / `pooled_controls` rows that `figures.py` reads.
- patsy fix: `dmatrix` is given an empty `EvalEnvironment`, because the module alias `C` shadows patsy's `C()`.

### `d3_register.py` (ID-1, ID-2, C8, R8)
- `neutral_benchmark()`: within-area RR 2026/2025 for N24 = improv*|utili[sz]*|exploit*, improv*, enhanc* and R24; the stacked R24-vs-N24 ratio of RRs; the within-slot LLM share 2026 vs 2025 (slot FE + area FE, topic100 clusters) with area up/down counts. All papers and NA pool → `register_neutral_benchmark.csv`.
- `word_churn()`: the 16-area sign count and Mantel–Haenszel RR for the 365 title words with ≥ 80 titles in 2025+26, plus 1,000 random rate-matched 4-word families → `register_word_churn.csv`.
- `context_reassigned()`: 2024 → 2025 area context with the 1,187 papers of the two new 2025 areas reassigned by a classifier trained on 2024 labels (bge embeddings). `context_2024_to_2025` is flagged `taxonomy_confounded`.
- `fig_f32()`: one colour scale for both panels with a colourbar each; cells with n < 100 shown grey with n; All-areas row `area_imputed=False`; caption rewritten.

### `d3_vintage.py` (C3, ID-5, R6, R9)
- New columns in `prep()`: n24, r24_or_n24, f26_y25, f26_y26, and the F26 components c26_*.
- New rows in `vintage_models.csv`:
  - F26 × 2026 arm (with and without the shared lemmas);
  - pre-LLM placebo 2018–23 and 2020–23;
  - genre benchmark (N24 outcome; all papers and NA pool);
  - meaning-fixed R24 | (R24 or N24) (all, NA pool, shared-lemma-free);
  - slot-based meaning-fixed contrast (`fit_slots`; all, NA pool, without harnessing/unveiling);
  - F26 components on R24 and on N24.
- `verdict_inputs`: logit n and dropped count, the shared-lemma-free co-primary, F26 × 2026, by-year rows, NA pool, placebo, genre and meaning-fixed rows, and F26 prevalence 2021–25.
- F3.3: the mirror is labelled F26/F24 (inverted CI), the panels are spaced wider, and the F26 legend notes that F26 sits at its base rate before 2026.

### `d3_signature_bound.py` (C1, C2, C4, C7, ID-4, R2, R12)
- `signature(..., A=None, ctrl=())`: the population NAME comparator, with the same topic100 × year FE and the same controls on every side. One joint topic100-cluster bootstrap resamples the slot rows, their papers and the population. Topics of S are drawn first, so the primary same-paper draws reproduce the original run exactly.
- New specs: F_d1 (D1's fingerprint), a pre-LLM 2018–23 row and "+ log authors on every side". Every spec gets its matching population subset (year, NA pool, non-LLM).
- Collider diagnostic: P(filled | NAME, F), the selection factor on the OR and the LPM with interaction → `signature_results.json` `collider_diagnostic`.
- `name_all_2024_26` is now the matched population comparator (no log authors, with bootstrap CI); the log-authors variant is nested.
- `ustar()`: a slot-year enters only if its baseline, F0 and F1 cells are non-empty in that draw, otherwise it is skipped in numerator, denominator and weights (same rule for the point estimate). New rows: opener slots only (no study_adj) and a topic100-cluster bootstrap. Per-slot U* uses the same function, with n_pre and n_F1. The share of draws with empty cells is saved.
- F3.4 shows three series (slot; NAME on the same papers; NAME on all papers) and both ratios per row.

### `d3_collect.py`
- H3a: control break scan, level contrast, frozen-trend event study, addition-vs-substitution rates, leave-out-"enhancing" and `verdict_detail`, all computed from the outputs.
- H3b: verdict "thresholds met (descriptive); register turnover not identified"; neutral benchmark, word churn and taxonomy-confounded context; a p_note saying the p is not a valid test of R26.
- H3c: verdict "prediction met; vintage reading not established"; co-primary and benchmark rows; fingerprint prevalence.
- H3d: verdict "partially supported" (rule: supported only if both comparators give ratio ≥ 1.5 with CI > 1; falsified only if both give ≤ 1); population comparator, collider diagnostic, population p.
- Holm: the pre-specified family is unchanged; a sensitivity family (H3a, H3c, H3d-population; H3b excluded) is added.
- New `sample_note`, `heldout_projected_power` (from `outputs/prereg/dryrun.json`) and `thesis_line_D3`. The deviations list is updated.

## Commands run

All from `research/titles/src` with `/home/user/venv/bin/python`, OMP_NUM_THREADS=2. Wall times in brackets.

1. Auditor checks re-run, with `PYTHONPATH=src`: `check3_collider` (3 s), `check8_fd1_positive_control`, `check9_event_trends`, `check7_pilot_n` (about 30 s together). All reproduced the audit numbers.
2. `-m analyses.d3_slots` (22 s; 71 s after adding the frozen-trend bootstrap). F3.1 was redrawn twice from the saved CSVs after layout tweaks.
3. `-m analyses.d3_register` (16 s). F3.2 was redrawn once from the saved CSVs after a layout tweak.
4. `-m analyses.d3_vintage`, run 4 times (33–42 s each): a column-name bug ("high-stakes"), then the shared-lemma-free meaning-fixed rows, then a legend label.
5. `-m analyses.d3_signature_bound` (442 s, background).
6. `-m analyses.d3_collect`, run 3 times (seconds each), for the thesis-line and deviation wording.
7. `figures.fig4()` and `figures.table1()` smoke test with FIG_DIR/TAB_DIR redirected to the scratchpad: both run. No study figure was overwritten.
8. `outputs/audit/d3/check_numbers.py`: **167 targeted checks of RESULTS.md against the output files, 0 missing**. The first run found 8 misses: 5 rounding slips in the text (e.g. 1.135 written as 1.14), fixed; 3 check-format issues, fixed in the checker.

## Key before → after

| Quantity | Before | After |
|---|---|---|
| H3a pooled / controls / stacked | 2.18 / 0.87 / 2.55 | unchanged |
| Pilot-like row | "2.49 (any-lead)" mislabelled | any-lead + full lexicon: 2.80 [1.89, 4.15], n = 2,321 |
| Event study 2024 (slots) | 5.19 [1.74, 15.5] "vs 2018–22 trends" | jointly estimated: same; frozen 2018–22: 4.82 [1.23, 19.3] |
| Camera-ready audit | 845 pairs, DiD −0.88 [−1.89, −0.19] | 1,127 pairs; accepted 22 LLM-v1, 0 adds, 4 drops; rejected 4 LLM-v1, 1 add; DiD −0.81 pp (no CI) |
| H3b verdict | supported | thresholds met (descriptive); register turnover not identified (R24/N24 1.08 [0.86, 1.36]; within-slot share OR 1.14 [0.87, 1.49]) |
| H3c verdict | supported | prediction met; vintage reading not established (shared-lemma-free 1.32 [1.04, 1.66], OR_F24 1.00) |
| H3c n | 24,365 (wrong for the logit) | 24,283 logit / 24,365 LPM |
| H3d verdict | supported (1.55 [1.11, 2.21]) | partially supported; population comparator 1.24 [0.99, 1.57], P(≤ 1) = 0.030 |
| H3d population ratio | 1.27 (mismatched controls, no CI) | 1.24 [0.99, 1.57]; with log authors on every side 1.23 [0.99, 1.58] |
| H3d with D1's F_d1 | not run | OR_slot 1.29 [0.92, 1.81]; ratio vs population 1.19 [0.84, 1.65] |
| U* | 0.647 [0.496, 0.811] | 0.647 [0.496, 0.811] (empty cells skipped; unchanged); no study_adj 0.61 [0.47, 0.76] |
| Holm (pre-specified) | 0.0009 / 0.0042 / 0.0014 / 0.005 | unchanged; sensitivity family 0.0007 / 0.0009 / 0.030 |

## Notes for other directions and the write-up (not changed here)

- **D1-H1e positive control** (D1 RESULTS still says "PENDING"): with D1's own fingerprint F_d1, the D3 slot uplift is not significant (OR 1.29 [0.92, 1.81]), and the ratio against the population NAME comparator is 1.19 [0.84, 1.65]. With F_any it is 1.42 [1.14, 1.79] vs NAME 1.14 [1.08, 1.21]. The positive control therefore does not validate the F_d1 bound.
- **`figures.py` fig4(c) and its caption** still show only the same-paper NAME comparator and quote ratio 1.55. `fig_F3_4_signature.csv` now also has the outcome "NAME title (all papers)" and the columns `ratio_pop*`, so the paper figure can show the population comparator. The H3b/H3d verdict strings in `table1` will now read "thresholds met (descriptive)" and "partially supported".
- **PLAN §1 thesis bullet 5** is stale. The replacement text is in RESULTS.md ("Thesis line for the study write-up") and in `results.json` → `thesis_line_D3`.

## Side effects

None outside `outputs/d3_register/`, the five D3 scripts and `outputs/audit/d3/`. Scratch files (draft RESULTS parts, figure smoke test) are in the session scratchpad.
