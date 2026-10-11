# WP4 fix log (camera-ready snapshot bounds)

Fixer pass over the three WP4 audits: code (`../snapshot_code`), identification (`../snapshot_ident`) and reporting
(`../snapshot_reporting`). Final numbers are in `outputs/snapshot/RESULTS.md` (section "Audit response") and in
`results.json`.

## Key decisions

1. **`snapshot_bounds.py` is not edited.**
   - The pre-registration bundle (`outputs/prereg/bundle.sha256`) hashes it as *required* code, because
     `prereg_confirm` imports it. Editing it would break `verify_bundle`.
   - All fixes live in the new `src/analyses/snapshot_final.py`, which imports its building blocks unchanged. The
     extra unions are registered only at runtime.
   - `src/analyses/snapshot_final_report.py` writes RESULTS.md from the outputs. It asserts every verdict-dependent
     sentence.
   - `check_numbers.py` (this folder) verifies three things: that verdicts and key numbers agree, that the freeze
     hash matches the cache bytes, and that `snapshot_bounds.py` still matches the bundle hash.
2. **One frozen audit sample.**
   - The analysis waited for the background enlargement to finish (2,000 lines, 21:39). The four HTTP-429 rows were
     retried once with `audit_v2 --skip-route --enlarge 250` (2,004 lines, 2,000 complete records). That flag
     leaves the route and v1-abstract caches the prereg froze untouched, so the one 503 row in the v1-abstract cache
     is still not retried.
   - The run uses all complete lines. The line count and the SHA-256 of exactly those bytes are in
     `results.json → meta.audit_freeze`; the hash convention matches `prereg_confirm._complete_jsonl`.
   - The interim outputs (254 records) are archived in `outputs/snapshot/interim_254/`.
3. **Primary audit** = original + enlargement pairs, 2023–26. The 2022 accepted-only pairs form a sensitivity spec.
4. **Gate:**
   - The feature is auditable: arXiv-channel measurable and ≥ 10 v1-present titles per arm.
   - The editing-corrected 95% CI excludes 1.
   - The Holm-adjusted one-sided identification p is below 0.025 across the auditable features. This p includes
     the tipping point's bootstrap SE.
   - The interim (uncorrected) rule is kept as a column.
5. **Channel rule.** None of the ~3,500 cached arXiv titles is ALL-CAPS or contains U+2011/U+2013 typography, and
   no arXiv v1 abstract contains an em dash (counts in `meta.channel_check`). L-title is audited as R24|R26, and the
   O-union as sentence case | question opener.

## Not done / out of scope

- **D4 and prereg consumers (C-I1 part 3).**
  - `d4_bias_atlas.py` (original audit only) and `prereg_confirm.freeze_audit` (1,261 enlargement lines, uncorrected
    gate) belong to other directions and are hashed by the prereg bundle, so they were not edited.
  - RESULTS §8 gives the `--enlarge-n` and hash to align them.
  - The prereg's own `audit_refreeze` rule is the sanctioned route.
  - At 1,261 lines the uncorrected gate passes compound, sentence case and the O-union w/o ALL-CAPS, so a prereg
    gate run as frozen would admit associations that the Holm gate rejects.
- **Last pre-decision arXiv version instead of v1 (C-I5).** This needs new network queries. It is handled by timing
  strata and a timing-standardised spec instead.
- **Whole-token surname matching (C-I9).** The caches do not store arXiv author lists, so it cannot be re-applied.
  The `abstract_matched` spec drops every title-clause admission instead.
- **D4's H4b text** (sentence case "unauditable") is in D4's RESULTS and is not edited here.

## Log

- Archived the interim outputs to `outputs/snapshot/interim_254/`.
- Wrote `snapshot_final.py`. A debug run on 1,902 lines went to the scratchpad. It confirmed that the corrected
  draws reproduce `tipping_table` exactly (assertion).
- Fixed the figures:
  - S1: legend below panel a, CIs on usable rates, n labels.
  - S2: D\* as a tick, ‡ for channel rows, abstract rows on G_total, observed-G CI, clipping footnote, shorter
    titles.
  - S3: k/n labels and an adaptive y-limit.
  - S4: renamed `fig_S4_flip_rates`, with an add-rate panel.
- After the enlargement finished and the errored rows were retried, ran
  `python -m analyses.snapshot_final --enlarge-n <all lines>`, then `snapshot_final_report`, then
  `check_numbers.py`.

## Final outcome (complete audit: 2,004 enlargement lines, SHA-256 dd51d5fa…; 803/508 primary pairs)

- **SB1** (NAME G_dec not identified): still supported.
  - DiD +1.48 pp [−0.63, 3.59] against D\* 2.92 pp; p = 0.127.
  - About 50% of the NAME excess is camera-ready at the point estimate (CI −21% to 124%).
- **SB2** (some acceptance association survives): not supported under the Holm gate. 0 of 26 pass; smallest Holm p
  0.29 (O-union w/o ALL-CAPS).
  - Under the uncorrected rule, compound and the O-union w/o ALL-CAPS pass.
  - Sentence case passed that rule at 600–1,261 lines but not on the complete audit.
- **G1** (H4a TOST): upgraded from partially supported to **supported**, corrected 90% CI [0.949, 1.031]. The
  corrected centre is 0.991.
- **SB3**: partially supported ('using' and R24 are now auditable).
- **SB5**: not supported. The camera-ready retitling excess is withdrawn: in-review stratum −2.7 pp; before-deadline
  stratum +8.6 pp [0.9, 16.1], interpreted as pre-submission revision.
- **G2, G2b and G3**: not supported.
- **G4**: partially supported. The magnitude fell from +3.55 to +0.71 pp, and the "LLM polishing" sentence is
  withdrawn.
- **V7a** is supported, with a shared-rule caveat and a near-miss bound (gap 0.33 → 0.25).
- **V7b**: partially supported.

## Checks (this folder)

- `check_channel.py`: arXiv titles and abstracts never carry ALL-CAPS, U+2011/U+2013 or U+2014.
- `check_independent.py`: NAME/O-union/sentence-case/compound DiDs, the tipping point, G at D̂, the editing share,
  Holm and the O-union p are recomputed with plain pandas; all match.
- `check_numbers.py`: RESULTS.md verdicts and key numbers vs results.json, the freeze hash vs the cache bytes, the
  `snapshot_bounds.py` hash vs the prereg bundle, and no placeholders. Result: OK.
