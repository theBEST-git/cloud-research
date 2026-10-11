# D4 fix log (gatekeeper: stage-wise filter gains, published-only bias)

This is the fixer pass after three audits:
- code (`audit/d4_code`, D4-1 to D4-12);
- identification (`audit/d4_ident`, I1 to I9);
- reporting (`audit/d4_reporting`, R1 to R25).

Each issue was re-checked with code before anything was changed. Pre-fix copies of all D4 scripts and outputs are in `pre_fix_backup/` (`src/`, `outputs/`).

## Re-runs

Every D4 script is fast, so all four were re-run in full (OMP_NUM_THREADS=2, same seeds). Every previously reported point estimate and CI reproduces exactly; only the quantities listed below are new or changed.

| Script | Runtime | What changed |
|---|---|---|
| `d4_stage_gains` | ~1.8 min | F26 abstract-only; L_noR24; 2018-22 period and `post_vs_pre_1822`; consistent post-decision-withdrawal variants (`wd_decided_in_s2`, `wd_postdec_ts`) replace the tautological `wd_rejected_in_s2`; style-density words re-selected in every bootstrap replicate (`density_reselect`); TOST bootstrap p; year-level ITS (`its_pools_yearlevel.csv`); BH q in T4.1; approximate CIs for adjusted totals; F4.1 / S4.1 relabelled |
| `d4_bias_atlas` | ~1 min | effect-scale (log-OR ratio) comparison for the ITS and colon premium; colon trend counted, level supplementary; entropy/JSD labelled as null bands and dropped from the 90%-CI count; camera-ready-free desk/exit columns; BH q; Kobak basic-bootstrap intervals, n, IUT p-values and the post hoc falsification flag; F4.2 / F4.3 redrawn |
| `d4_exit_composition` | ~45 s | consistent post-decision-withdrawal specs; topic100 FE co-primary (all features); key × year specs; single-paper-key cross-section; F4.4 adds the topic-FE NAME row, the full control list and n |
| `d4_collect` | seconds | rewritten: computed verdicts, Holm family, templated notes, WP4 canonical intervals side by side, auto-generated `summary_table.md` spliced into RESULTS.md between AUTO markers |

**Not changed (prereg dependency).** `prereg_confirm.py` imports `BINARY_L`, `stage_sums`, `pooled_prev`, `its_pools`, `_clean` and `SEED` from `d4_stage_gains`, and `kobak_from_prev` from `d4_bias_atlas`. An AST comparison against the backup shows these unchanged, and `BINARY_L` (hence CT6's L-union) is identical. The source files themselves changed, so if the prereg bundle hashes the D4 files, the hash no longer matches the working tree. The frozen test definitions are unaffected.

**PLAN.md was not edited** (it is locked). The suggested replacement for the PLAN §1 thesis bullet is in RESULTS.md, under "Implications for the study thesis".

## Verification scripts (this folder)

- `v01_density_reselect_check.py`: row 0 of the re-selection bootstrap reproduces the cached style-density gains exactly (total 0.9649).
- `v02_check_numbers.py`: 108 targeted checks of RESULTS.md numbers against gains.csv, atlas.csv, kobak_bounds.csv, exit_composition.csv, T4.1, its_pools*.csv and results.json. 0 failures.
  - It found 4 hand-typed errors, now fixed: L-union desk·exit is 0.981, not 0.982 (0.98146); the single-key topic-FE se is 1.33; L_abstract upper CI 1.023; question opener lower bound 0.776.
- `v03_name_heterogeneity.py` / `.txt`: NAME G_total by LLM topic (0.996 vs 1.033) and by harmonised area (20 areas with ≥ 300 papers: 0.38–1.48, IQR 0.91–1.05).

## Verdict changes

| Hypothesis | Before | After | Why |
|---|---|---|---|
| H4a | supported | supported (Holm p 0.0015), qualified | Only the observed NAME share. Review-stage neutrality is not identified (WP4 selection-only G_total 0.867–1.081 crosses 0.90). Yearly CIs are inside the band only for 2024–26. Pool-break equivalence is not shown (year-level). |
| H4b | supported | **partially supported** (Holm p 0.059) | The L-union total fails Holm. The pre-decision L depletion is R24-driven and pre-dates 2024 (R24 post/pre 0.99; L without R24 0.998). The O depletion sits at the unidentified decision stage (camera-ready-free O 1.035). |
| H4c | partially supported | partially supported, with a stronger qualifier | ≥ 15% magnitude not established (IUT p 0.209); falsification condition met under the post hoc baseline (0.9005 / 0.9011). |
| H4d | supported | **partially supported** | Topic100-FE cross-section +0.84 [−1.05, 2.74]; residual excess with single-paper keys (+5.60 with topic FE); "between authors" removed. |
| H4e | supported | **partially supported** (descriptive) | M 11/11 → 9/11 on the effect scale. ITS break 0.50 (−0.15 to 1.16); colon trend 0.89. |

## Issue by issue

| id | valid? | change |
|---|---|---|
| D4-1 | yes | ITS and colon premium on the effect scale with delta-method CIs from the joint IF covariance. Colon trend counted (0.892 [0.66, 1.12]); level supplementary (2.88; s0 log-OR 0.018, se 0.031, so the ratio is ill-conditioned; difference +0.034 [0.009, 0.058]). M 9/11, accepted-only 9/10. |
| D4-2 | yes | Holm over {H4a–H4d} with IUT p (H4a TOST 0.0005 floored; H4b max of 0.0295 / 0.0005 / 0.0005; H4c 0.209; H4d 1.3e-5). H4b adjusted p 0.059. The L-union pre-decision sub-test and the O total pass at H4b's Holm step; the L total does not. |
| D4-3 | yes | "Exact" / "needs no audit" removed. Camera-ready-free desk/exit in gains.csv and atlas.csv (`log_desk_crf`, `log_exit_crf`). O-union camera-ready-free pre-decision 1.035 [1.000, 1.072] reported. |
| D4-4 | yes | Reversal stated only on pre-decision and camera-ready-free gains; 2018-22 baseline added. Camera-ready-free L post/pre 0.952 (vs 2018-23) / 0.969 [0.925, 1.020] (vs 2018-22). Decision part (0.889) labelled unidentified; "pre-LLM" → "pre-2024". |
| D4-5 | yes | Consistent post-decision withdrawals: decided withdrawals in any year (66 / 107 / 355 in 2024–26), plus 2025–26 timestamp ≥ decision date (299 / 403). 2024 timestamps are all post-decision (bulk update), so they are unusable. L-union desk·exit 0.981 → 0.985; R24 exit 0.901 → 0.920. The primary keeps the `_core` / PLAN §0 / CT6 definition. The tautological G_total line was removed. |
| D4-6 | yes | H4d `wd_post_as_rejected` uses the consistent definition (+3.38 / −1.47 / 4.86); new `wd_postdec_dropped` (+3.58 / −1.15 / 4.72). |
| D4-7 | yes | `d4_collect` computes verdicts and notes from the JSONs. The RESULTS label is fixed: 0.946 is camera-ready-free desk·exit; camera-ready-free exit is 0.950. |
| D4-8 | yes | Null bands labelled, excluded from `ci90_within_10pct` (NaN), dashed in F4.2. |
| D4-9 | yes | BH q over 83 T4.1 tests and over the atlas. NAME desk q = 0.065 and F24 exit q = 0.052 are no longer called notable. |
| D4-10 | yes | Checked: 104 of 3,253 F26 papers via title only; the title part is a subset of `title_typo` (0 exceptions), so the L-union is unchanged. F26 is abstract-only in the L set; `f26` kept as `F26_incl_title`. |
| D4-11 | yes | Re-selection inside every bootstrap replicate. Total CI 0.955–0.975 → 0.956–0.980; camera-ready-free 0.957–0.971. Median re-selected list sizes 115 / 145 / 200; Jaccard 0.71–0.78. T4.1 density ORs still use the full-sample list (stated). |
| D4-12 | yes | P(ratio ≥ 0.85) = 0.209 / 0.078 / 0.079 and P(ratio ≥ 0.9) = 0.0495 / 0.018 / 0.042 reported; H4c in Holm. |
| I1 | yes | L_noR24 (total 0.998 [0.972, 1.027]); per-marker post/pre against 2018-23 and 2018-22; H4b reworded; CT6 caveat. One refinement to the auditor: L_noR24 post/pre total is 0.814 [0.752, 0.886], so the non-R24 markers did lose a pre-2024 advantage. The camera-ready-free part (0.943) loses significance against 2018-22 (0.968 [0.921, 1.023]). |
| I2 | yes | O verdict descriptive; identified O depletion restricted to ALL-CAPS at exit (camera-ready-free 0.901 [0.817, 0.984], not new: post/pre 0.951). |
| I3 | yes | Thesis rewrite proposed in RESULTS (PLAN not edited). |
| I4 | yes | Topic100 FE co-primary; single- vs multi-paper split (+6.91 / +5.60 with topic FE, n = 7,234); key × year ± topic FE (within −2.65 [−5.20, −0.11] with topic FE). "Between authors" removed. |
| I5 | yes | Same fix as D4-1. |
| I6 | yes | `its_pools_yearlevel.csv`: per-pool year-level ORs 1.154 / 1.174 / 1.176; ACC−REJ −0.017 [−0.109, 0.074] (90% CI inside ±0.1); ACC−WD and REJ−WD about ±0.27, uninformative. |
| I7 | yes | Heterogeneity computed (v03); thesis wording proposed. |
| I8 | yes | Same as D4-3; F4.2 hatches every decision part as not separable and keeps editing only as an audit-interval whisker. |
| I9 | partly | No revision history in the data (`metadata_provenance` has only creation and last modification), so the suggested test is impossible. Caveat added. Re-counted: 4 of 8 rejected sentence-case v1 titles were dropped in the stored title (the auditor said 3). |
| R1 | yes | WP4 abstract audit cited (F24 DiD +3.55 [−1.62, 8.73]; tipping points −0.23 / −0.67; em dash unauditable); Limitations updated. |
| R2 | yes | The post hoc baseline meets the falsification condition; wording changed. |
| R3 | yes | Summary verdicts qualified (auto-generated table). |
| R4 | yes | Same as D4-1. ACC slope-change p = 0.18 vs REJ 0.004 reported. |
| R5 | yes | Same as I4; topic-FE difference reported as 2.58. |
| R6 | yes | Adjusted stage gains reported as not agreeing (NAME exit 0.993 [0.981, 1.005], decision 1.019 [0.993, 1.044]); title typography 0.87 → 0.99. |
| R7 | partly | LITERATURE_BRIEF §3.5 shows the pilot was whole-title ALL-CAPS ("ALL-CAPS titles ... accepted at 16.5% vs 40.5%"). The casing class is therefore the right comparison and Deviation 3 was wrong; Deviation 3 is corrected. allcaps_name 0.922 is kept as secondary. |
| R8 | yes | Same as D4-2. |
| R9 | yes | H4e retitled; knife-edge cases noted. |
| R10 | yes | F4.2 panel b: every decision part hatched "not separable"; editing shown only as an audit whisker; grey stage palette distinct from the class colours. |
| R11 | yes | F4.1: hollow decision markers, axis label covers the ratio of means, off-scale values with CIs, camera-ready footnote. |
| R12 | yes | F4.3: panel a from 0; panel b below 0 (2026 accepted CI visible); ratio CIs annotated; legend moved. |
| R13 | yes | "CIs inside the band only for 2024–26"; S4.1 axis "(log scale)"; band "NAME only". |
| R14 | yes | F4.4: legend lists the controls; topic100-FE NAME row; n caption. |
| R15–R18, R20–R23 | yes | Text fixes as listed in RESULTS "Audit response". Added: n per cell in Kobak / by-year tables; 2019 variant (NAME 1.021 [0.962, 1.082]; L-union 1.170 [1.082, 1.258]); approximate CIs for adjusted totals; atlas counted as 26 rows / 24 ratios. |
| R19 | yes | WP4 canonical intervals in T4_2_audit.md (`wp4_*` columns), results.json and the gate statements. Deviation 8 rewritten. |
| R24 | yes | Basic-bootstrap intervals in kobak_bounds.csv. The 2026 ratio interval is [0.071, 1.084] and includes 1; downward bias of the max() baseline noted. |
| R25 | yes | "Fixed before any estimate" qualified; verdicts computed. |

## Open dependency

**WP4 may revise its intervals.** The WP4 snapshot (`outputs/snapshot/`) has a fixer queued (snapshot_final.py, enlarged audit). D4 reads WP4's canonical intervals programmatically, as of `T4_2_tipping_points.csv` mtime 2026-10-11 17:11 UTC.

If WP4 changes:
1. Re-run `python -m analyses.d4_collect`. This updates results.json, T4_2_audit.md and the AUTO summary table.
2. Update the hand-written WP4 numbers in the RESULTS.md body: H4a decision-stage paragraph, T4.2 table, H4c abstract-audit lines.
