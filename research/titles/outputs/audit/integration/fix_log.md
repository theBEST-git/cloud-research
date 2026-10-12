# Integration fix log (cross-direction alignment after all audits)

Date: 2026-10-11. Scope: the cross-direction items each direction's fixer flagged as out of scope, the final
figures and tables, the pre-registration bundle, `outputs/SUMMARY.{md,json}` and the study README. PLAN.md and
`data/` were not modified; no git commands were run. Pre-change copies of every edited script and output were kept in the
session scratchpad (`integ_backup/`); the second integration pass copied them into the repository, at
`outputs/audit/integration/pre_fix_backup/pass1/` (revision-1 frozen files that are byte-identical to the committed
ones are omitted).

## 1. D1: positive control from D3 (D1 fix log "PENDING")

- `d1_summary.py`: new `positive_control_d3()` reads `outputs/d3_register/signature_models.csv` and `results.json`
  and writes `results.json → H1e.positive_control_D3` (H3a slot break; H3d slot uplift with D1's fingerprint F_d1
  and with D3's F_any). `H1e.verdict_note` updated. Re-run (4 s); every other field of `results.json` and every
  F1.x figure CSV is byte-identical (checked by diff).
- Result: with F_d1 the slot uplift is OR 1.29 [0.92, 1.81] (one-sided p 0.072), ratio against the population NAME
  comparator 1.19 [0.84, 1.65]; with F_any 1.42 [1.14, 1.79] against NAME 1.14 [1.08, 1.21].
- `RESULTS.md`: verdict row, headline, §5 positive-control paragraph, §9 thesis table, REP-4 row and "claims
  weakened" updated: H1e is "supported as pre-registered, not robust as a bound, and not validated by a positive
  control on its own fingerprint". `outputs/audit/d1/check_results_md.py`: 153 checks, the same 3 documented misses.

## 2. D4: complete camera-ready audit

WP4 re-ran on the complete enlargement (21:43 UTC) after D4's fixer read it (17:11 UTC).
- `d4_bias_atlas.py`: `audit_pairs("complete")` takes WP4's frozen primary pairs (`outputs/snapshot/audit_pairs.csv`,
  1,311 pairs, 2023–26); D4's features are recomputed on them. `flip_table` adds WP4's pseudo-flip variance floor
  (primary CI), WP4's auditability rule (≥ 10 v1-present per arm and arXiv-channel measurable) and keeps D4's old
  rule as `auditable_d4rule`. The original 331-pair audit is a sensitivity spec. An assertion checks that the DiD and
  CI equal WP4's `T4_2_flip_matrices.csv` (17 shared features; max |diff| 1e-16). F4.2 marks off-scale editing
  whiskers. Re-run 46 s.
- `d4_collect.py`: reads WP4's Holm gate (`passes_holm_dec`, `p_holm_dec`) and editing-corrected TOST rows;
  audit-dependent wording (H4a qualifier and notes, gate row, T4.2 header, deviation 8) is generated from flags.
  Verdicts unchanged; H4a qualifier changes from "review-stage neutrality not identified" to "robust to camera-ready
  editing; a small decision-stage premium not identified" (selection-only G_total 0.948–1.033, corrected 90% CI
  0.949–1.031).
- `RESULTS.md`: integration note, H4a camera-ready paragraph and verdict, data-section rebuttal note, H4b O-recasing
  note, T4.2 section (rewritten), H4c abstract-audit note (+0.71 pp instead of +3.55), H4e whiskers, deviation 8,
  limitations, thesis line, new audit-response row. `outputs/audit/d4/v02_check_numbers.py`: 108 checks, 0 failures.
- D4's own uncorrected rule now flags compound G_dec and R24 G_total; these are reported as uncorrected only.

## 3. WP4 report

- `snapshot_final_report.py`: the "consumers" paragraph of §8 and the C-I1 audit-response line now record that D4
  and the prereg are aligned to the freeze. Regenerated; `outputs/audit/wp4/check_numbers.py`: OK.

## 4. Pre-registration revision 2 (`prereg_confirm.py`)

- New stage `refreeze_final`: `freeze_audit` rebuilt on `snapshot_final`'s builders and WP4's freeze
  (`--enlarge-n` = 2,004 lines, SHA-256 `dd51d5fa…` asserted); title gate = WP4 primary pairs (1,311), abstract gate =
  WP4's 2024–26 v1-abstract pairs (1,032); both asserted to reproduce WP4's tables exactly. Only `audit_flips.csv`,
  `audit_did_boot.npz`, `audit_state.json`, `params.json` (new `audit`, `audit_revision_1`, `revision`) and
  `rules.json` changed; R1 models, centroids, lexicons, slot inventory and DFL cells are byte-identical.
- Gate: WP4's multiplicity-controlled rule. Association claims (CT6 G_total, CT10) need auditability (count and
  channel), an editing-corrected 95% interval beyond the boundary and a Holm-adjusted identification p < 0.025
  (`decide()`); equivalence claims (CT5, CT11) keep the editing-corrected interval rules. `audit_refreeze` is closed.
- `check` re-run: 0 mismatches over 55 columns. `dryrun` re-run (77 s): every CT statistic, CI and p is identical to
  revision 1; gate changes: CT10 fails (identification p 0.041, corrected upper bound 0.918 > 0.90), so CT10 is "not
  confirmed (gate)"; CT5 passes with [0.949, 1.031]; CT11's b_max is 0.092.
- `prereg.md`: revision line, gate rule, audit state, closed refreeze rule, reading notes for CT3/CT7/CT8/CT9
  (what a confirmation would and would not show; rules unchanged), revision history.
- Bundle: 73 files, hash **853827a92e85ad56ee85376e8b90a881c4f4ca1e46a861e80ed21a04e883d922**; supersedes
  f69fdb468702fe11e336b81476869531a71acb1d4f922b8bd1d479934bbac628 (revision 1). `verify`: ok, no mismatches.
- `.gitignore`: the frozen `.npz`/`.npy` parameters under `outputs/prereg/frozen/` are now excluded from the
  `outputs/**/*.npz|npy` ignore rules, because the bundle hash covers them and they must be committed.

## 5. Figures and tables (`figures.py`)

- Fig. 4: panel (c) uses the population NAME comparator (all papers, same FE; ratio column) plus a row for D1's
  fingerprint; the collider-conditioned same-paper comparator is dropped; panel (b) adds the neutral synonyms N24
  (computed from the universe with D3's regex) and drops the "generation" labels; one shared legend; caption rewritten.
- Fig. 5: decision-stage markers hollow ("not identified"); the ALL-CAPS off-scale note moved off the intervals;
  caption updated (adjusted stage gains ≈ 1; L depletion R24-driven; KeyError on the renamed D4 field fixed).
- Fig. 6: atlas rows on the effect scale (hollow diamonds) with null bands dashed; panel (b) shows the complete
  audit with a Holm-p column; caption updated.
- Fig. 2: caption reports DFL by year and the failed positive control.
- Table 1: final post-audit verdicts with reviewed wording (fails loudly on any upstream verdict change), D4 Holm p,
  H3d population comparator, rows for S2.1, S2.2 and the gate. Table 4: WP4's abstract spec and Holm gate column.
- All PNGs were opened and checked for overlaps, clipping and misleading axes; two stale fig4 CSVs removed.

## 6. New outputs

- `src/analyses/summary_ledger.py` → `outputs/SUMMARY.json`, `outputs/SUMMARY.md` (ledger of every hypothesis, WP4
  gates, CT1–CT12 dry run, validation, robust findings, withdrawn claims).
- `README.md` and `requirements.txt` at the study root.

---

# Second integration pass (cross-direction consistency, issues X1–X19)

Date: 2026-10-11. Input: a cross-direction check of SUMMARY, the D1–D4 and WP4 reports, results.json files, the prereg,
tables, figure captions and README (19 issues). Every issue was re-checked against the outputs before it was changed;
all 19 were valid (X15 with a different cause, see below). PLAN.md and `data/` were not modified; no git commands
were run. Pre-change copies of every edited file: `outputs/audit/integration/pre_fix_backup/pass2/`.

## Re-checks and fixes

| Issue | Re-check | Fix | Re-run |
|---|---|---|---|
| X1 robust finding 9 / withdrawn row vs D4 | `gains.csv`: F24 CRF desk·exit 0.965 [0.939, 0.993], style density 0.963 [0.957, 0.970], F24 post/pre 0.914 [0.849, 0.988]; R24 pre-decision 0.900 [0.870, 0.931], CRF 0.892 [0.850, 0.937], decision 0.896 (not identified). Confirmed. | `summary_ledger.py`: finding 9 rewritten on pre-decision gains (numbers read from D4 results and T4.1), F24/density depletion added to it and to the withdrawn row. D4's summary bullets and `d4_collect`'s auto H4b verdict text no longer call the other L markers neutral. Table 1 H4b wording (figures.py `FINAL_VERDICT`) adds the F24/density depletion. | d4_collect, figures, summary_ledger |
| X2 D4 thesis line | L-union decision 0.994 [0.970, 1.017]; R24 decision 0.896; T4.1 decision R24 0.837 (q 0.015), density 0.939 (q 0.013); H4c P(ratio ≥ 0.85) 0.209/0.078/0.079. Confirmed. | D4 RESULTS thesis line replaced as proposed; Kobak part "point estimates of 20–50% (≥ 15% not established in any year)". Audit-response row added. | — |
| X3 D3 pre-freeze audit pin | `slots_results.json`: 1,620 lines, 1,127 pairs (694/433), LLM-slot v1 22/4. Confirmed. | Re-run option: `d3_slots.py` reads WP4's freeze (`wp4_enlarge_freeze()`, SHA-256 asserted), stale "still growing" comment removed, clear error if the caches are missing. D3: 1,317 pairs (810/507; D3's pairing rule includes 2022 and differs slightly from WP4's 803/508), LLM-slot v1 23/5 (= SB3), DiD −0.69 pp from 5 flip events; still unauditable. Every other D3 output identical (only `slot_audit_*`, `slots_results.json → audit`, runtime and PDF metadata changed; F3.1 CSV differs in the 16th digit). D3 RESULTS §2/§7/§8 and audit response, d3_collect deviation, WP4 §8 consumer list (snapshot_final_report.py), SUMMARY H3a updated. | d3_slots (67 s), d3_collect, snapshot_final_report |
| X4 F_any description | features_v2 line 328: `F_any = f24 | f26 | title_typo`. Confirmed. | Full definition in D1 RESULTS (fingerprint paragraph, H1e(i) table, δ table, positive control), D3 §5, `d1_summary` docstring and `results.json`, Fig. 4 caption. | d1_summary, figures |
| X5 CT1/CT2 readings | D1: H1a year-level p 0.035 (Holm 0.071) vs paper-level 1.3e-4; H1c two-stage CI [0.03, 2.71] pp, Holm 0.067; CT2 dry-run CI [0.020, 2.701]. Confirmed. | `prereg_confirm.audit_interpretation_notes()` adds CT1 and CT2 readings (numbers read from D1 results.json and the dry run); ledger readings. Rules unchanged. | prereg revision 3 |
| X6 CT4/CT6/CT12 readings | D3: without via/using stacked 1.41 [0.74, 2.68]; without enhancing 1.72 [1.04, 2.84]; control break scan significant at 2020–23 and 2025. D2: within-last-key gap 4.9 [2.2, 7.6] pp; symmetric-lookback 0.86 [0.72, 1.01]. D4: R24 total 0.807 vs 0.815 (2018–23); L without R24 0.998. Confirmed. | Readings for CT4, CT6, CT12 in prereg.md and SUMMARY §3 (read from the direction outputs). CT9 note now follows the positive-control flag. | prereg revision 3 |
| X7 README dependencies | `d1_summary.positive_control_d3()` returns PENDING without D3; `d3_slots.audit()` with no caches raised a KeyError; `d4_bias_atlas.audit_pairs("original")` also reads `cache/arxiv_audit.jsonl` unconditionally. Confirmed (and the D4 claim in the README was also too optimistic). | README: dependency list (D3 and D4 need step 4 and the caches; `d1_summary` moved to the end of step 7); "Archive the caches" bullet lists WP4, D3 and D4. | — |
| X8 compound/sentence-case row | WP4 freeze path: sentence case passes the uncorrected rule at 600/1,000/1,261 lines, not at 2,004; `passes_uncorrected_dec` = {compound, O_union_arxiv}. Confirmed. | Row rewritten; `summary_ledger` asserts both facts against the WP4 tables. | summary_ledger |
| X9 H3e code; verdict_code vocabulary | D3 results.json H3e verdict "not_supported". Confirmed. | `d3_collect`: "unresolved" (or "supported" if U* > 0.8). `summary_ledger`: `VERDICT_VOCAB` (8 codes, defined in SUMMARY.json `verdict_vocabulary`), `NORMALISE` (fails loudly on an unknown upstream code), `verdict_code_upstream` kept. | d3_collect, summary_ledger |
| X10 Table 4 channel rows; F24 D* | Table 4 printed DiDs for ALL-CAPS, O-union, typography, em dash; F24 D* −0.23 (G_dec) vs Fig. 6b −0.67 (G_total). Confirmed. | Channel-unauditable rows show "— (channel)" (from WP4's `channel_ok`); Audit column "no (channel)" / "no (count)"; column renamed "D* for G_dec (pp)"; notes give F24's G_total tipping point and the sub-union gates G2/G2b. F24/em-dash gate column uses WP4's claim flag. Fig. 6b caption labels both tipping-point definitions. | figures |
| X11 atlas CIs vs G_total CIs | `d4_bias_atlas.SEED = S.SEED + 1` for prevalence_stats. Confirmed. | `PREV_SEED = S.SEED` in `prevalence_stats` (Kobak keeps SEED, which CT10 reproduces). Atlas prevalence CIs now equal `gains.csv` G_total CIs exactly (checked for NAME, O-union, R24, L-union, ALL-CAPS, sentence case, question opener, F24, compound). Only prevalence-row CIs, their p/q values and F4.2/Fig. 6a changed; `within_10pct` and `ci90_within_10pct` unchanged; T4.2 and Kobak files identical. D4 H4e numbers updated; note added. | d4_bias_atlas (44 s), d4_collect, figures |
| X12 pool windows | D1 ITS 2017–26 for ACC/REJ (no 2017 withdrawals in U), D4 2018–26. Confirmed. | Table 2 rows labelled and noted; D1 RESULTS pool rows labelled; Table 1 H4a, D4 auto summary and Fig. 5 say "ITS 2018–26". | figures, d4_collect |
| X13 FPR baseline | `check_fpr_baseline.py` (this folder): F_d1 2023 2.51% (accepted 3.11%, n = 1,256; others 2.22%), 2021–22 3.19%; corrected 2026 tool share at A = 0.39: 7.1% [1.4, 12.9] (2023), 7.4% [1.4, 13.4] (2021–22), 7.0% [1.4, 12.7] (2023 non-accepted). | Sentence and sensitivities in D1 §5 (iii); audit-response row. | check script |
| X14 Fig. 3a reference row | CSV row 1.0015 [0.945, 1.057] is T2.4's ratio to the paper-level change (18.3 pp); ρ_last 0.995 divides by P_L − P_E. Confirmed. | Tick label "Last stayer, all papers"; CSV label "Last-position stayer keys, all L papers (ratio to paper-level change)"; caption explains. PNG checked. | figures |
| X15 V4 denominator | Both counts are on universe U (43,482 rows). The 34-row difference is the 34 NAME papers of 2017 (no R3 mask), **not** placeholder rows; all 22 R1 survivors are 2023–26. | D1 RESULTS uses 22 of 12,928 (2018–26) and explains the 12,962 in `results.json`; API.md note. VALIDATION and SUMMARY already used 12,928. | — |
| X16 hard-coded positive-control reading | Confirmed. | `d1_summary`: reading and `verdict_note` generated from `validates_F_d1_bound` / F_any flag; Fig. 2 and Fig. 4 captions and the prereg CT9 note likewise. Re-run: only the reading text and two new fields changed; F1.x CSVs byte-identical. | d1_summary, figures |
| X17 person-language | Confirmed (D2 RESULTS lines 13, 32, 159; VALIDATION V6). | "entrant first-position key", "entrant co-author key(s)", "new-key share" in D2 RESULTS, `d2_collect` (H2c statement, summary table), VALIDATION.md and the matching `validate_measures.py` strings. Machine-readable contrast keys in D2's CSV/JSON (e.g. "last=S; L papers with an entrant first author") were left unchanged because figures and checks look them up. | d2_collect |
| X18 small items | Confirmed. | (a) "discovery split (~80%)"; (b) D4 R1/I9 rows marked original-audit, with complete-audit values; (c) D4 T4.2 bullet points to G2/G2b; (d) Fig. 6 caption: 24 statistics incl. beyond-PLAN O/L rows, full gate rule incl. the editing-corrected CI. | figures, summary_ledger |
| X19 audit trail; required code | Confirmed. | `integ_backup/` copied to `pre_fix_backup/pass1/`; this pass in `pass2/`; README §9 lists the 19 required-code files and the revision rule. | — |

## Pre-registration revision 3

- Required code edited: `prereg_confirm.py` (reading notes, `REVISION` record with history, new stage `revise`,
  generalised revision text in `prereg.md`), `d3_slots.py` (X3) and `d4_bias_atlas.py` (X11). No held-out data have
  been requested (no `heldout_started.json`, no `heldout.json`).
- Commands (from `src/`): `prereg_confirm revise` → `dryrun` (75 s) → `bundle` → `verify`.
- Frozen files: only `params.json` (revision record) and `rules.json` (revision field) changed; all others
  byte-identical (checked with `cmp` against pass2 backups; `verify` ok).
- Dry run: compared field by field with the revision-2 `dryrun.json`; the only differences are runtimes and the
  bundle-hash fields. Every statistic, CI, p-value, gate field and verdict is unchanged.
- Bundle: 73 files, hash **6853685bf21a08cdb40227d7fe5d94285c3ec023a9354ab3971faec75051ecd9** (supersedes revision 2,
  `853827a92e85ad56ee85376e8b90a881c4f4ca1e46a861e80ed21a04e883d922`). `verify`: ok, no mismatched_required, no
  mismatched_other. The bundle was written after the last code edit of this pass.

## Checks after the pass

- `outputs/audit/d1/check_results_md.py`: 153 checks, the same 3 documented misses.
- `outputs/audit/d2/v02_check_numbers.py`: 206 checks, 0 failed.
- `outputs/audit/d3/check_numbers.py`: 167 checks, 0 not found.
- `outputs/audit/d4/v02_check_numbers.py`: 108 checks, 0 failures.
- `outputs/audit/wp4/check_numbers.py`: OK.
- Figures: fig3 and fig6 PNGs opened and checked (labels, no overlap); the other PNGs are byte-identical.
- `summary_ledger` asserts the H3a audit note, the X8 facts and every verdict code against the outputs.
