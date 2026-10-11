# D1 fix log (fixer pass after the three audits)

Date: 2026-10-11. Scope: D1 naming break: `src/analyses/d1_its.py`, `d1_content_cf.py`, `d1_decompose.py`, `d1_summary.py` and `outputs/d1_break/`.
- Pre-fix copies of every json/csv, RESULTS.md and the four scripts are in `outputs/audit/d1/pre_fix_backup/`.
- The old rolling refit checkpoint is stored as `refit_boot_R1.{csv,json}.moved`.
- PLAN.md was not modified.

## Code changes

### `d1_content_cf.py`
- **D1-C1, fold-ensemble prediction.**
  - `cv_select` now returns the test-row scores of the five CV fold models at the chosen C.
  - `run_fit` stores them as `s0`–`s4`, with `score` = their mean.
  - New helpers `fold_scores` and `ens_prob` give p̂ = mean_k expit(s_k + c). They are used by `point_summary`, `boot_runs`, `new_topic_placebo` and the Shapley fits.
  - The full-data model is fitted only for the V4 feature list.
  - `stage_refit_boot` predicts with the same fold models; the old extra full-model fit was dropped. It asserts that the scores are fold-ensemble scores.
- **D1-C2 / ID-5, year-FE sensitivity.** New representations `R1yfe`, `R3yfe`, `R5yfe` (`Reps.build`):
  - training-year dummies, first year dropped, scaled ×5 so the L2 penalty on them is negligible;
  - test rows coded as the calibration year;
  - `base_rep()` maps them to their base features.
- **REP-9, slope-recalibration sensitivity.** `slope_recal_summary`: logistic intercept+slope recalibration on the calibration-year OOF scores. Reported for R1/R3/R5 and their year-FE versions.
- **D1-C8.** R2 is restricted to papers with keywords (`Reps.available`).
- **D1-C7.** `new_topic_placebo` was rewritten:
  - per-year absolute residuals, averaged with fast-cluster-count weights;
  - the bootstrap recomputes the recalibration (via `boot_runs(extra=...)`);
  - signed gaps are reported.

### `d1_its.py` (D1-C4, ID-1, ID-2, REP-15, REP-16)
- `year_level()`, applied to U, the NA pool, the non-LLM subset and U excluding 2026:
  - REML random-effects meta-regression (`re_metareg`, t with 6 df) on covariate-adjusted logit and LPM year effects;
  - quasi-binomial dispersion (`quasi_dispersion`);
  - GLS smooth-vs-break comparison (`smooth_vs_break`).
- New output `its_year_level.csv`. `its_results.json` gains `year_level`, `p_one_sided_year_level` and new criteria.
- Falsification is checked on both paper-level and year-level NA-pool CIs.
- `fig_its_scan`: log axis, and a second panel with both sup-LR scans.
- The CSV pool label is `NApool`.

### `d1_decompose.py` (D1-C5, D1-C6, D1-C9, ID-4, ID-6, REP-5, REP-10, REP-14, REP-16)
- **New-key share.** Fixed 2-year lookback (`new_key_share_lookback`), missing for years up to 2021. The growing-lookback version is kept as a DFL sensitivity.
- **DFL.** Reported per year, with Oaxaca CIs and n.
- **Labels.** "people" → "composition".
- **`stage_refit_boot`.** Fixed-window refit bootstrap for R1, P and R1P with shared weights → `refit_boot_fixed.{csv,json}`.
- **Tool.**
  - `misclass_factor` and the corrected `tool_table` (naive and corrected; A = 1 not identified);
  - year-matched 2026 δ;
  - DiD (F × post, 2021–26), pre-period placebo δ, per-year F_any δ, typography given an intra-word dash, typography 2026;
  - power of criterion (i) (`min_F1_gap_for_ratio_below_*`).

### `d1_summary.py` (D1-C3, ID-3, REP-1/2/3/4/6/11/15/17)
- Holm uses the year-level p for H1a and the two-stage p for H1c. `two_stage_refit` combines refit draws with year shocks e_y ~ N(0, (τ·p_y(1−p_y))²) on the telescoped endpoint years.
- The paper-level and randomization-p Holm families are also reported.
- H1c verdict: "supported" only if the year-level falsification rule is not met and the Holm-adjusted p < 0.05; otherwise "not_established_year_level".
- H1d is evaluated per year (IUT p).
- H1e uses the corrected, year-matched tool share. The positive control reads "PENDING".
- Figures: one colour per quantity; F1.1 adds the rolling cumulative counterfactual and "not a CI" legend entries; F1.2 adds content means and a whisker caption; F1.3 adds a divider, a rolling-content marker, the uncorrected-tool marker and relabelled bars.

## Commands run

All commands were run from `research/titles/src`, using `/home/user/venv/bin/python -m`, with OMP_NUM_THREADS of 1–2. Wall times are given in brackets.

1. `analyses.d1_content_cf fit reps=R6` (test, 7 s).
2. Two background chains:
   - `fit reps=R1,R5,R1yfe,R5yfe` (15 min), then `fit reps=R1@0.5,R1n,R1u` (6 min);
   - `fit reps=R6b,R2,R4` (2 min), then `fit reps=R3,R3yfe` (4 min), then `fit variants` (8 min).
3. `analyses.d1_its` (71 s).
4. `analyses.d1_decompose fit` (32 s).
5. `analyses.d1_content_cf refit_boot 300 R1` (background, about 35 min).
6. `analyses.d1_decompose refit_boot 200` (background, about 10 min).
7. `analyses.d1_decompose all` (285 s).
8. `analyses.d1_content_cf summarise 2000` (622 s).
9. `analyses.d1_summary`, run twice; the second run added the Holm-informed H1c verdict.
10. Checks (in this folder):
    - `fix_numbers.py` dumps all quoted numbers to `fix_numbers.txt`;
    - `check_results_md.py`: 153 numeric strings re-derived from the outputs and matched in RESULTS.md. The 3 "not found" are 2 rows whose numbers carry bold markup and 1 row deliberately not printed.

**CSV relabelling after the run.** After `summarise` had run, the `NApool` relabel was added to its CSV writer. The same relabel was applied once, in place, to `cf_rolling_steps.csv` (8 rows) and `cf_fixed_paths.csv` (6 rows). The result is identical to a re-run and no estimates changed.

**Side effect, not cleaned up.** A first launch of chain 2b ran from the wrong working directory. It wrote three 148-byte error logs at the filesystem root: `/fit_fix_B1.log`, `/fit_fix_B2.log` and `/fit_fix_B3.log`, each containing "No module named analyses". A safety check blocked their removal; they are harmless and can be deleted by hand.

## Key before → after

| Quantity | Before | After |
|---|---|---|
| R1 / R5 / R3 rolling content share | 0.620 / 0.611 / 0.595 | 0.574 / 0.565 / 0.577 |
| R1 / R5 / R3 fixed 2026 share | 0.430 / 0.420 / 0.509 | 0.389 / 0.381 / 0.492 |
| Year-FE R1 / R5 / R3 (fixed; rolling) | n/a | 0.377 / 0.368 / 0.479; 0.544 / 0.533 / 0.551 |
| Slope-recal R1 / R5 / R3 rolling | n/a | 0.652 / 0.641 / 0.579 |
| H1b verdict | falsified | partially supported (not falsified; prediction fails) |
| H1a primary p (Holm) | 1.3e-4 (0.0006) | 0.035, year level (0.071) |
| H1c diff (ratio) | +1.17 pp (1.85) | +1.35 pp (1.89) |
| H1c CI used | refit [0.24, 2.00] | two-stage [0.03, 2.71]; Holm 0.067 |
| H1c verdict | supported | not established at the year level |
| H1d DFL 2024 / 25 / 26 | 0.251 / 0.297 / 0.246 | 0.287 / 0.316 / 0.261 |
| H1d verdict | supported | partially supported |
| Shapley content / composition / residual (2026) | 0.399 / 0.094 / 0.507 | 0.338 / 0.088 / 0.574 |
| Tool share at A = 0.39 | 3.1% [0.0, 6.2] | 7.1% [1.4, 12.9] (corrected, 2026 δ) |
| H1e verdict | supported | supported as pre-registered, not robust as a bound; positive control pending |

## Issues judged out of scope or not fully fixed

- **REP-7.** The thesis bullets are in PLAN.md §1, the locked pre-registration, and in DIRECTIONS.md and LITERATURE_BRIEF.md, which are outside D1. None was edited. RESULTS §9 gives the replacement text.
- **CT2 (PLAN §4) confirmatory design** (D1-C3 asks to revise it). The confirmatory plan is a PLAN-level document and was not edited. RESULTS states that a within-year paper bootstrap cannot test year-level acceleration, and the two-stage inference implemented here is the recommended replacement.
- **D1-C2 as primary.** Year-FE content models are reported as an audit sensitivity, not as the primary specification, because the pre-registered model has no year term. The H1b verdict is unchanged whether or not they are included: both versions give < 0.60.
