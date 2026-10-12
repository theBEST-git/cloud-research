# Integration fix log (cross-direction alignment after all audits)

Date: 2026-10-11. Scope: the cross-direction items each direction's fixer flagged as out of scope, the final
figures and tables, the pre-registration bundle, `outputs/SUMMARY.{md,json}` and the study README. PLAN.md and
`data/` were not modified; no git commands were run. Pre-change copies of every edited script and output are in the
session scratchpad (`integ_backup/`), not in the repository.

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
