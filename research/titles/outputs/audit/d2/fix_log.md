# D2 fix log (communal vs generational change)

Fixer pass after three audits: code (`audit/d2_code`), identification (`audit/d2_ident`) and reporting (`audit/d2_reporting`). Each issue was re-checked by running code before it was changed.

Pre-fix copies of the scripts and outputs are in `pre_fix_backup/`.

## Re-runs

All runs used OMP_NUM_THREADS=2 and the same seeds as before, so every previously reported estimate reproduces exactly:

| Script | Runtime | What changed |
|---|---|---|
| `d2_shiftshare` | ~3.5 min | null outcomes, restricted alias, email-position variant, ρ_noR CIs, generalized H2c(ii), two-way H2c(i), F2.3 |
| `d2_markers` | ~1 min | drop-both variant, weight shares, equal-weight medians, F2.1 labels |
| `d2_ident` (new) | ~1 min | newcomer-free contrasts, H2b first position, two-way SEs, H2d benchmark, family removal, F2.2 |
| `d2_support` | ~0.5 min | S2.1 content-fixed benchmarks, S2.2 figure |
| `d2_collect` | seconds | verdict logic, Holm at falsification boundaries, auto-generated summary table spliced into RESULTS.md |

`d2_panel` was not re-run, and the panel files are unchanged.

## Verification scripts

- `v01_null_check.py` computes the shared-outcome null ρ as a composition ratio through an independent code path. It reproduces 0.882 / 0.776 / 0 (last / any / first) for the entrant-first null, and 0.927 / 0.822 for the entrant- or returner-first null.
- `v02_check_numbers.py` runs 206 targeted checks of RESULTS.md against the output files.
  - New RESULTS.md: 0 failures.
  - Pre-fix RESULTS.md: 123 failures. Most come from the new statistics; the rest are the stale H2c(ii) CIs and rounding.
  - A global "number appears anywhere" check could not detect the stale CIs, so it was replaced by these targeted checks.

## Issue by issue

| id | valid? | change |
|---|---|---|
| D2-C1 | yes | Stale H2c(ii) CIs replaced: 0.66 [0.49, 0.85]; +12.1 pp [8.9, 15.6]; 2023→2026 0.60 [0.37, 0.79]. `d2_collect` now writes the summary table into RESULTS.md between AUTO markers. |
| D2-C2 | yes | `allprior_ratio` now covers the rolling, lag-1, fixed and symmetric two-year definitions, E = 2023 and NA-pool samples (`T2_2b_allprior.csv`). The fixed base gives −0.07 [−0.42, 0.24]. The verdict is now "not supported". |
| D2-C3 | yes | `h2c_models` uses CGM two-way (key, paper) SEs: 1.38 pp, against 0.82 pp key-only. The p-value is taken at the 0.3× falsification line (p = 0.31); the prediction test against 0.5× gives p = 0.015. Ratio CIs are given for all variants, plus a version with the uncertainty of the population change. Holm was re-run. |
| D2-C4 | yes | `d2_ident.twoway_se` gives key / paper / row / CGM / pigeonhole SEs for ρ, first − last and observed − null (`T2_1b_twoway_se.csv`). CGM is within about 15% of the key-cluster SEs; pigeonhole is about 1.6× and labelled conservative. |
| D2-C5 | yes | `d2_markers` adds d² weight shares (`markers_weight_shares.csv`), a variant without both llm_topic and the NAME family (0.19 [0.13, 0.26]) and the equal-weight median ρ (style − topic −0.21 [−0.26, −0.14]). The contrast survives. |
| D2-C6 | yes | The S2.2 verdict requires the positive control to be detected in the same specification and to differ from NAME. It is now "inconclusive". The upper bound of past − future (−0.003) is reported. |
| D2-C7 | yes | S2.1 now has topic100-adjusted drift (−4.8 pp, p = 0.057) and within-topic drift (−3.9 pp, p = 0.12) benchmarks, plus the same-key contrast (−3.4 pp, p = 0.33). The claim that retitled papers lag the drift is weakened. |
| D2-C8 | yes | `d2_ident.family_removal` adds same-key pair removal: ρ shifts by up to −0.048 / −0.035 / −0.039. The random-removal assumption is stated, and "negligible" is withdrawn. |
| D2-C9 | yes | The literal Kitagawa share is shown in the H2a summary row and verdict: not met (0.61 / 0.35). |
| D2-C10 | yes | Lag-1 is reported next to rolling (ratio 0.38; post × share_new 4.4 pp vs 7.9 pp). Mean share_new by year is reported, and the censoring is stated. |
| D2-C11 | yes | A restricted alias collapse was added (≤ 3 keys, ≤ 40 papers per alias-year): first − last −0.39 [−0.51, −0.28]. The full collapse is labelled an extreme upper bound and removed from the variant table. |
| D2-C12 | yes | A `no_email_papers` variant drops papers with any email-keyed position: ρ 0.995 / 0.820 / 0.536. The issue is in Limitations. |
| D2-C13 | yes | The H2e verdict uses both outcomes, with an intersection-union p (0.061; Holm 0.122). The verdict is now "inconclusive". |
| ID-1 | yes | Null outcomes (`null_Nfirst`, `null_NRfirst`, `null_anyN`) were added to the main, NA-pool and email specs, with observed − null differences on the same draws. H2a is now "not identified", and the "same keys / same people" wording is withdrawn. |
| ID-2 | yes, one point qualified | Newcomer-free contrasts are in `T2_4_newcomer_free.csv` and F2.2c, with selection named as the alternative. The auditor's "0.03–0.4" omits the symmetric definitions (lag-1 0.70, two-year 0.53), so RESULTS reports a tenure gradient instead. |
| ID-3 | yes | The composition of rolling all-prior L teams is reported: 41% contain an entrant key; stayer-only teams changed 0.19×. The H2c verdict is now "not supported". |
| ID-4 | yes | Added the within-last-key gap (4.9 pp [2.2, 7.6]), the symmetric-lookback newcomer premium by year (change +4.3 pp [0.3, 8.4]) and the symmetric prior-first ratio (0.86 [0.72, 1.01]). H2b is now "supported on the pre-registered groups; magnitude not robust". |
| ID-5 | yes | The random-subset slope (1.00 [0.96, 1.04]) and the null slope (0.78) are reported. The slope criterion is marked non-diagnostic. |
| ID-6 | yes, in part | The email-era null is 0.69 / 0.76. The observed NAME ρ exceeds the entrant-first null by 0.51 [0.02, 1.07], a marginal margin. H2e is "inconclusive", and "general mode" is withdrawn. |
| ID-7 | yes | S2.1 is reworded: no NAME is added within a project, so any change runs through new projects. |
| ID-8 | yes | S2.2 is reworded: the primary specification does not detect the control, and the detected control shows the same ordering. |
| ID-9 | yes | Two-way CIs are reported. CGM CIs are close to the key-cluster CIs; the 1.7× figure is the conservative pigeonhole bootstrap, also reported. |
| D2-R1 | yes | H2e was added to D2-1. The literal shares (0.26 / 0.25 < 0.3) are in the table, with the s̄ = 0.22 cap explained. |
| D2-R2 | yes | Both statistics are shown in the H2a cell. "The one shortfall" was removed. ρ is renamed "stayer-to-population change ratio". |
| D2-R3 | yes | The first summary sentence was replaced, with the Kitagawa shares 61 / 35 / 17%. |
| D2-R4 | yes | Same fix as D2-C1. The header claim was replaced. |
| D2-R5 | yes | Same fix as D2-C2. |
| D2-R6 | yes | (i) is reported as contradicted. The margin above 0.3× is not significant. Ratio CIs are given for every variant. |
| D2-R7 | yes | The same-key benchmark and strict-rule gap are now in the summary and §2.7. |
| D2-R8 | yes | "Fits homophily" was removed. The past − future MDE (0.10) is reported. |
| D2-R9 | yes | F2.2 was redrawn as four panels. The scenario values are labelled "not bounds"; IPW and two-way CIs are added; fixed-base rows are marked E = 2023. Scenario (a) is given as 0.75 [0.71, 0.79]. |
| D2-R10 | yes | Author-weighted email-era rows were added. The verdict now accounts for the compound CI. |
| D2-R11 | yes | Same fix as D2-C11. The variant table text was rewritten. |
| D2-R12 | yes | The NA-pool statement now lists what was and was not re-run. NA-pool versions of H2c(ii) and the newcomer-free contrasts were added. |
| D2-R13 | yes | The trim wording is quantitative and non-causal. |
| D2-R14 | yes | The H2d wording is qualified: partition named, weights stated, "small negative" topic increment, 22 of 33 markers. |
| D2-R15 | yes | Coverage corrected: last 10.1 / 4.8 / 3.6%, first 6.7 / 1.7 / 1.2%. |
| D2-R16 | yes | "Exactly" was replaced. |
| D2-R17 | yes | Same fix as D2-C8. The per-unit extrapolation instability is stated, and extrapolated rows are marked point only. |
| D2-R18 | yes | F2.3 now plots returners, with a caption (bootstrap bands) and the y-axis starting at 0. |
| D2-R19 | yes | F2.1 has a partition title, the label "NAME (3 overlapping variants)", an error-bar note and nudged labels. |
| D2-R20 | yes | The S2.2 figure has a shared x-axis, MDE bands and the past − future MDE in the caption. |
| D2-R21 | yes | Wording replacements, including the API.md §4.6 attribution. |
| D2-R22 | yes | ρ_noR CIs added (T2.1). Removal extrapolation is marked point only. H2c ratio CIs are given for all variants, including the population-uncertainty version. |

## Verdicts before → after

| Hypothesis | Before | After |
|---|---|---|
| H2a | supported | not identified |
| H2b | supported | supported on the pre-registered groups; magnitude not robust |
| H2c | partially supported | not supported (not falsified) |
| H2d | supported | supported (channel contrast); slope criterion not diagnostic |
| H2e | supported | inconclusive |
| S2.1 | supported | NAME not added on net; lag behind content-fixed drift not established |
| S2.2 | supported | inconclusive |

## Downstream

The PLAN §1 thesis bullet "The same people changed … mostly within incumbent authors" is not supported by D2. It must be reworded in the paper write-up. PLAN.md itself was not edited.
