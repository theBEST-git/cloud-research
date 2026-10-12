# D3. The machine register: meaning-fixed slots, vintage turnover and a bounded second-hand diffusion test

WP7 results for PLAN.md §D3, revised after three audits (code, identification, reporting; see "Audit response" at the end). Code is in `research/titles/src/analyses/`:
- `d3_slots.py`: freezes the slot inventory; H3a; T3.1; F3.1; camera-ready audit of opener words.
- `d3_register.py`: H3b; F3.2.
- `d3_vintage.py`: H3c; F3.3.
- `d3_signature_bound.py`: H3d, H3e; F3.4; supplementary S3.1.
- `d3_collect.py`: builds `results.json` (estimates, verdicts, Holm).

Run order, from `src`: `OMP_NUM_THREADS=2 python -m analyses.d3_slots`, then `d3_register`, `d3_vintage`, `d3_signature_bound` and `d3_collect`. Total runtime is about 10 minutes (`d3_signature_bound` takes about 7). All outputs are in `outputs/d3_register/`.

Four conventions hold throughout:
- **All estimates use the discovery split**, the same data on which the PLAN pilots were computed. The verdicts below are discovery-sample replications of pre-specified rules, not confirmations. Confirmation rests on the held-out tests CT4 (H3a), CT7 (H3c) and CT8 (H3b). Their projected probabilities of confirmation (`outputs/prereg/dryrun.json`) are 0.27 / 0.23 / 0.32 at α = 0.0083, and 0.56 / 0.51 / 0.62 at α = 0.05.
- All associations are associational.
- Titles of accepted papers may be camera-ready versions. Every key result is therefore repeated in the camera-ready-free NA pool.
- "LLM-favoured" names a word class defined before estimation. It is not a claim that a given title was machine-written.

## Summary

| Hypothesis | Pre-registered test | Result | Verdict (Holm p, pre-specified family) |
|---|---|---|---|
| **H3a** slot break | Pooled slot post OR ≥ 2; controls in [0.67, 1.5]; slot − control > 0 | Slots **2.18 [1.41, 3.38]**; controls **0.87 [0.64, 1.18]**; stacked slot/control **2.55 [1.53, 4.25]** | **Supported** (p_Holm = 0.0009). The rise is an addition of LLM-variant openers; OR ≥ 2 depends on "enhancing" (1.72 without it); the control null holds at 2024 only; not sharply dated against 2023. |
| **H3b** 2025→26 shift | Within area: R24 down in ≥ 10/16, R26 up in ≥ 12/16 | R24 down in **14/16**; R26 up in **16/16**. Within-area RR 2026/2025: R24 **0.74 [0.65, 0.85]**, R26 **1.94 [1.69, 2.24]**. Neutral synonyms N24 fell alike (0.69); R24/N24 1.08 [0.86, 1.36] | **Thresholds met; descriptive. No register turnover identified** (p_Holm = 0.004, not a valid test: R26 was selected in-sample) |
| **H3c** vintage contrast | OR(F24→R24) / OR(F26→R24) > 1 | 1.11 [0.92, 1.34] vs 0.76 [0.64, 0.89]; ratio **1.46 [1.17, 1.83]**; shared-lemma-free 1.32 [1.04, 1.66] with OR(F24) 1.00 | **Prediction met; vintage reading not established** (p_Holm = 0.0014). Driven by F26 papers avoiding R24; weaker in the NA pool (1.24 [0.94, 1.63]) and in 2026 alone (1.29 [0.97, 1.71]) |
| **H3d** lexical vs structural signature | OR(F→LLM slot variant) ≥ 1.5 × OR(F→NAME) | Same papers (PLAN): 1.42 [1.14, 1.79] vs 0.91 [0.72, 1.16], ratio 1.55 [1.11, 2.21]. **Population NAME comparator: 1.14 [1.08, 1.21], ratio 1.24 [0.99, 1.57]** | **Partially supported**. Same-paper test p_Holm = 0.005, but that comparator is collider-conditioned. Against the population, ratio > 1 is marginal (P(ratio ≤ 1) = 0.030) and 1.5× is not met |
| **H3e** second-hand diffusion (exploratory) | Claim only if U* > 0.8 | U* = **0.65 [0.50, 0.81]** (2024–25 vs 2022–23); 0.45 after F1-contamination correction | **Unresolved**: no second-hand-diffusion claim |

The four pre-specified discovery tests are one-sided; Holm is applied over H3a–H3d (raw p 0.00024, 0.0021, 0.00045, 0.005; adjusted 0.0009, 0.0042, 0.0014, 0.005). The H3b p-value is not a valid test, because R26 was chosen after the pilot saw it rise in this data. A sensitivity family drops H3b and uses the population comparator for H3d (raw p 0.00024, 0.00045, 0.030; adjusted 0.0007, 0.0009, 0.030).

**Bottom line.** LLM-favoured verb openers rose from 2024 in meaning-fixed slots, while the control pairs did not shift at the 2024 break. The tool's signature in titles is lexical more than structural, but the margin is small once NAME is measured in the population rather than on slot-filled papers. The 2026 changes in R24 and R26 are not a register turnover, and title–abstract vintage alignment is not established.

## 1. Measures and frozen inventory

**Slot inventory** (`slot_inventory.json`). The inventory was frozen before any D3 model was fitted.
- Start from the lexicons.json v2.0 slot words (SHA-256 `34ec8f93…7847`).
- Remove the three V2 failures (`outputs/validation/slot_variants_dropped.json`; sense precision < 0.85):
  - exploit/unlocking (0.29);
  - exploit/enabling (0.00);
  - reveal/decoding (0.39).
- A title opening with a dropped word counts as "slot not filled".
- The kept words are:

| Slot | LLM-favoured | Neutral |
|---|---|---|
| S-improve | enhancing, boosting, advancing, elevating, empowering | improving |
| S-reveal | unveiling, uncovering, unraveling/unravelling, demystifying | understanding, analyzing/analysing, investigating, characterizing/characterising, explaining |
| S-exploit | leveraging, harnessing, unleashing | exploiting, utilizing/utilising |
| S-study-adj | comprehensive | systematic, extensive, large-scale (before study/benchmark/evaluation/…) |

- The pre-V2 filter for "boosting" as the algorithm stays (1 title).
- The three borderline words (unleashing, harnessing, boosting) are kept and tested below.
- **Meaning is held approximately, not exactly, fixed.** V2 swap preservation (share of titles whose meaning survives when the other variant is swapped in; n = 29 per cell, swap κ = 0.784): S-improve LLM variant 0.99 (post) / 0.92 (pre); S-reveal LLM variant 0.75 / 0.83; S-exploit LLM variant 0.79 / 0.90 (and the neutral "exploiting" side only 0.47 / 0.70). VALIDATION.md already warns that reveal-slot shifts are partly shifts in what is claimed (`v2_slot_metrics.csv`).

**Opener rule (primary).** Following the PLAN text, the slot word is the first word of the title, or of the subtitle when the title is "NAME: …".
- V2 found lower sense precision for titles that fill a slot only under the pilot's any-colon-lead rule (0.83 vs 0.90). That rule is a robustness row.
- Sample, 2018–26: **1,922 slot-filled titles from 1,920 papers**. By slot: improve 979, reveal 511, exploit 321, study-adj 111.
- Control-pair titles: 6,925 (towards/toward 1,250, novel/new 392, via/using 5,283).
- **Pilot reconciliation.** The pilot's n of 2,362 used the any-lead rule *and* the undropped lexicon. The two analyst choices separately give 2,163 (any-lead rule, V2 drops kept; OR 2.49) and 2,059 (primary rule, full lexicon; OR 2.44). Together, the truly pilot-like row (any-lead rule + full lexicon) gives n = 2,321 and OR **2.80 [1.89, 4.15]**. The two choices together lower the pooled OR from 2.80 to 2.18. Both are conservative, and both are disclosed here.

**Register and fingerprints** (features_v2, unchanged):
- R24 = title contains any of enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*.
- R26 = any of unified, unifying, beyond, bridging.
- F24 = abstract has ≥ 1 RARE21 word.
- F26 = abstract has ≥ 1 of {principled, reframe*, genuine*, brittle, auditable, sharply, high-stakes}, or U+2011 / en-dash letter compounds in the title or abstract.
- F = F24 ∪ F26 ∪ title typography (`F_any`). D1 bounds the tool with a stricter fingerprint, F_d1 = F24 ≥ 2 words ∪ F26 ∪ title typography; §5 reports both.
- Prevalence of F in 2021–22 is 5.9% (pre-ChatGPT; treated as false positives). It is 21.1%, 17.6% and 26.2% in 2024–26.
- F24 prevalence falls from 19.2% (2024) to 9.1% (2026), consistent with recall decay as the model generation changes. F26 rises from 2.5% to 18.6%. Before 2026, F26 sits at its pre-LLM base rate: 3.4%, 2.9%, 2.4%, 2.5% and 2.7% in 2021–25 (`fingerprint_prevalence_by_year.csv`). F26 therefore marks the 2026 vintage only in 2026.

## 2. H3a: LLM-favoured slot variants rose from 2023–24 onward, accelerating after 2024; pooled control pairs did not shift at 2024

**Descriptives (F3.1, `fig_F3_1_slot_shares`).**
- The pooled LLM-variant share of slot-filled titles was 0.06–0.34 in 2019–2023 (0.34 in 2023). It reached 0.54 in 2024, 0.64 in 2025 and 0.67 in 2026.
- S-improve ("Enhancing/Boosting… vs Improving…") moved from 0.25 (2018–23) to 0.71 (2024–26).
- S-reveal moved from 0.09 to 0.29; S-exploit from 0.62 to 0.84.
- The pooled control-pair share moved from 0.72 (2023) to 0.74 (2024). Among the controls, via/using is the only drifting pair: it rises gradually from 2018 and jumps in 2026 (0.78 → 0.90).
- Year cells with fewer than 10 slot-filled titles are not plotted (S-exploit 2018, 2019 and 2021; S-study-adj 2020–23; novel/new 2018–19). The figure also shows the pooled-slot share, the modelled outcome, and Wilson bands for the controls.

**Addition, not substitution (F3.1 panel b, `slot_variant_rates.csv`, `slot_variant_rate_shift.csv`).** The share is conditional on a slot being filled, and slot filling itself responds to the tool.
- LLM-variant slot titles per 1,000 titles (pooled slots): 7.6 (2022), 11.4 (2023), **30.0 (2024)**, 37.0 (2025), 29.1 (2026).
- Neutral-variant slot titles per 1,000: 26.0, 22.0, **25.2**, 20.9, 14.5.
- Quasi-Poisson level shift at 2024 against the 2018–23 trend: LLM variants RR **3.91 [1.84, 8.29]**; neutral variants 1.17 [0.70, 1.94]. The same holds in the NA pool (3.88 vs 1.20) and the non-LLM subset (4.05 vs 1.06).
- Improve slot: "Enhancing"-type openers rose from 4.9 to 17.0 per 1,000 from 2023 to 2024, while "Improving" stayed at 9.0 → 10.6.
- So in 2024 LLM-favoured verb openers were *added* without displacing their neutral synonyms. Substitution (a fall in neutral variants) appears only in 2025–26. The counterfactual title for many 2024 "Enhancing X" titles was not "Improving X" but a differently framed title. The slot design holds meaning approximately fixed *conditional on a slot being filled*; it does not hold fixed whether a title fills one.
- The 2023 rise in the share partly reflects a dip in neutral variants (26.0 → 22.0 per 1,000) rather than early LLM-variant growth (7.6 → 11.4).

**Primary model (T3.1, block A).** Logit `y ~ slot FE + slot × (t − 2023) + post + llm_topic`, 2018–26, SEs clustered by topic100:
- Pooled slots: post OR **2.18 [1.41, 3.38]**, one-sided p = 0.0002 (n = 1,922; 1,508 post).
- Control pairs: post OR **0.87 [0.64, 1.18]** (n = 6,925). The point estimate is inside [0.67, 1.5]; the lower CI bound is slightly below 0.67.
- Stacked slot + control model, post × LLM-slot (the CT4 parameter): OR **2.55 [1.53, 4.25]**, p = 0.0002. LPM equivalent: +20.3 pp [+11.1, +29.5].
- The control-pair estimate reproduces the pilot (0.87 [0.64, 1.17]). The slot OR is smaller than the pilot's 2.69 [1.80, 4.01] because of the stricter opener rule and the V2 drops (§1; the truly pilot-like row gives 2.80 [1.89, 4.15]).
- **Verdict:** the pooled OR is ≥ 2 and its CI excludes 1; slot − control > 0; the pooled control-pair level shift at 2024 is 0.87 [0.64, 1.18] under the shared-trend model. **The pre-specified rule is met (supported)**, with three qualifications:
  1. The same model finds significant control shifts at every other candidate break year (2020–23 and 2025; table below), towards/toward and novel/new individually sit above 1.5, and the level-contrast model gives controls 2.02 [1.73, 2.37]. The control criterion holds for the pre-registered 2024 specification only.
  2. The OR ≥ 2 margin depends on "enhancing", which the scout had already flagged as one of only two robust 2024 excess style words in these same titles (LITERATURE_BRIEF §3.3). Without it, the pooled OR is 1.72 [1.04, 2.84] (stacked 2.02 [1.14, 3.59]). The direction survives; the pre-registered magnitude does not. The held-out CT4 test is the real confirmation.
  3. The rise is an addition of LLM-variant openers (above), and it is not sharply dated against 2023 (caveats below).

**Per slot and per control pair (T3.1, block B; BH over the four slots and, separately, the three pairs).**

| Slot / pair | Post OR | BH q |
|---|---|---|
| S-improve | 2.63 [1.39, 4.97] | 0.006 |
| S-reveal | 1.93 [0.74, 5.00] | 0.18 |
| S-exploit | 1.80 [0.55, 5.94] | 0.22 |
| S-study-adj | not identified (LPM −13 pp [−72, +46]) | 0.67 |
| towards/toward (control) | 1.69 [0.82, 3.47] | 0.18 |
| novel/new (control) | 1.58 [0.74, 3.36] | 0.18 |
| via/using (control) | 0.75 [0.53, 1.06] | 0.95 |

- S-study-adj has only 6 pre-2024 titles, so its slot trend is not identified.
- Only the improve slot survives BH on its own. Leave-one-variant-out keeps the pooled OR between 1.72 (dropping "enhancing", CI [1.04, 2.84]) and 2.32, and every CI excludes 1 (`slot_loo.csv`); but see qualification 2.
- The pilot's "improve slot alone ≈ 4.3" does not reproduce under the slot-specific-trend model.
- Two of the three control pairs have point estimates above the PLAN's 1.5 upper bound when fitted alone; the pooled control null comes from via/using.

**Robustness (`slot_robustness.csv`).** Pooled slot OR / stacked OR (controls 0.80–1.00 in every row except where stated):

| Specification | Pooled slot OR | Stacked OR |
|---|---|---|
| NA pool (camera-ready-free) | 2.18 [1.28, 3.70] | 2.57 [1.40, 4.71] |
| Non-LLM subset | 2.59 [1.57, 4.28] | 2.96 [1.64, 5.34] |
| topic100 FE | 2.28 [1.40, 3.74] | 2.65 [1.54, 4.56] |
| bge topic100 FE | 2.37 [1.50, 3.74] | 2.75 [1.63, 4.65] |
| Excluding titles whose abstract has the same verb (n = 913) | 1.94 [1.03, 3.69] | 2.26 [1.13, 4.54] |
| Title-start openers only | 2.38 [1.47, 3.87] | 2.76 [1.55, 4.92] |
| Post-NAME openers only (n = 728, few pre titles) | 1.70 [0.66, 4.38] | 2.00 [0.78, 5.11] |
| Excluding 2026 | 2.27 [1.36, 3.80] | 2.42 [1.34, 4.37] |
| 2024 as the only post year | 2.38 [1.39, 4.07] | 2.62 [1.44, 4.79] |
| With 2017 | 2.26 [1.48, 3.46] | 2.77 [1.69, 4.55] |
| Without 2019 | 2.37 [1.52, 3.71] | 3.00 [1.78, 5.07] |
| Unweighted V2 rule (also drops unleashing) | 2.15 [1.38, 3.33] | 2.50 [1.49, 4.20] |
| Any-lead opener rule, V2 drops kept (n = 2,163) | 2.49 [1.66, 3.74] | 2.91 [1.81, 4.69] |
| Full lexicon, primary rule (n = 2,059) | 2.44 [1.61, 3.70] | 2.85 [1.75, 4.65] |
| **Pilot-like: any-lead rule + full lexicon (n = 2,321)** | **2.80 [1.89, 4.15]** | 3.27 [2.04, 5.24] |
| + log authors | 2.25 [1.45, 3.51] | 2.63 [1.56, 4.44] |
| **No slot trends (level contrast)**; controls **2.02 [1.73, 2.37]** | 4.40 [3.26, 5.93] | 2.46 [1.78, 3.41] |
| Stacked with year FE (absorbs common year shocks) | — | 3.16 [1.90, 5.25] |
| Year-level REML meta-regression on slot × year cells, with group-year shocks; t(6) / t(12) | 2.76 [1.26, 6.03], p = 0.010 | 2.97 [1.02, 8.62], p = 0.023 |

- The accepted-only subsample is underpowered: 2.14 [0.81, 5.67].
- Under a level contrast without slot trends the controls also shift (OR 2.02): the slot-versus-control contrast survives (2.46), but "controls flat" is a property of the trend model.

**Caveats on timing and controls.** A skeptical reader should weigh three of them.

1. **The break is not sharply dated against 2023.**
   - A scan of the break year on the full data, 2020–25 (`slot_placebo_breaks.csv`):

     | Break year | 2020 | 2021 | 2022 | 2023 | **2024** | 2025 |
     |---|---|---|---|---|---|---|
     | Pooled slots OR | 0.65 | 0.50 | 1.00 | 1.91 | **2.18** | 1.04 |
     | Pooled controls OR | 0.68 [0.47, 0.97] | 0.58 [0.43, 0.78] | 0.53 [0.37, 0.75] | 0.56 [0.42, 0.73] | **0.87 [0.64, 1.18]** | 1.46 [1.17, 1.83] |
     | Controls p (two-sided) | 0.036 | 0.0004 | 0.0003 | 3.5 × 10⁻⁵ | **0.36** | 0.0009 |
     | Stacked contrast OR (z) | 0.87 (−0.25) | 0.78 (−0.68) | 1.68 (1.38) | 3.21 (3.59) | **2.55 (3.59)** | 0.76 (−1.19) |

   - 2024 is the only candidate year at which the pooled controls show no significant level shift. The shared-trend control model appears misspecified (via/using drifts concavely), and the stacked 2023 contrast of 3.21 comes largely from the control dip. With year FE the stacked contrast is 3.75 at 2023 vs 3.16 at 2024 (z 3.88 vs 4.44).
   - Randomization p over the six candidate years is therefore 1/6 for the pooled slots (the minimum attainable with six candidates) and 2/6 for the stacked contrast. Randomization inference alone cannot reach 0.05 here.
   - **Event study, two versions** (`slot_event_study.csv`):
     - (i) Year deviations from slot trends *estimated jointly* with the 2023–26 year dummies (the original model; the relative slot slopes are partly identified from 2023–26 cross-slot differences, so these trends are not "fitted on 2018–22"). Slot ORs: 2023 **2.41 [0.98, 5.93]** (p = 0.055); 2024 5.19 [1.74, 15.5]; 2025 7.02 [1.68, 29.3]; 2026 8.71 [1.58, 48.0]. Slot − control: 2023 2.79 [1.03, 7.55]; 2024 6.26 [1.93, 20.4].
     - (ii) Trends *frozen* on 2018–22 (offset; opener slots, since S-study-adj has no 2018–22 trend; topic100-cluster bootstrap refitting both stages, 300 draws): slots 2023 **2.17 [0.74, 6.89]**; 2024 **4.82 [1.23, 19.3]**; 2025 6.02 [1.07, 40.2]; 2026 6.84 [0.87, 75.8]. Controls 0.85, 0.85, 0.95, 1.56 (all CIs include 1). Slot − control: 2023 2.55 [0.83, 9.00]; 2024 5.71 [1.47, 25.9].
   - Both versions agree that the slot deviation is clear from 2024 on, while the 2023 slot deviation (OR 2.2–2.4) has CIs that include 1. The 2023 slot − control contrast excludes 1 in the jointly estimated version (2.79 [1.03, 7.55]) but not with frozen trends (2.55 [0.83, 9.00]). Part of the shift may already start with the 2023 cohort, submitted in September 2022, two months before ChatGPT's release; in per-1,000 rates that 2023 step is small (above).
   - Pre-only placebo breaks (2018–23 data) are null: slot ORs 0.99 / 0.39 / 1.60 at 2020 / 2021 / 2022, all CIs including 1.
   - We therefore describe the shift as "accelerating from 2024". We do not describe it as a ChatGPT-dated step.
2. **The contrast leans on via/using.** via/using makes up 76% of the control titles. Without it, the remaining controls (towards, novel) give:
   - post OR 1.60 [0.98, 2.62] in the PLAN level-shift model, and a stacked contrast of only 1.41 [0.74, 2.68].
   - In the PLAN model the trend is shared between pre and post years. towards/toward declines after 2024 (0.92 → 0.82), which steepens the fitted trend and pushes up the level shift.
   - In the jointly estimated event study, the towards/novel controls show no break (ORs 0.63–0.83 in 2023–25, all CIs including 1), and the slot − control contrast without via is 6.39 [1.68, 24.3] in 2024. With trends frozen on 2018–22, the towards/novel first stage is too sparse (novel/new has fewer than 10 titles a year in 2018–19): point estimates are 0.68, 0.79, 0.59 in 2023–25, but the bootstrap CIs are degenerate, so this version is not informative.
   - The pre-registered criterion is met. The slot-versus-control contrast is still specification-dependent once via is removed.
3. **Camera-ready** (`slot_audit_flips.csv`). We matched **1,317** pre-decision arXiv v1 titles to the submitted titles: 810 accepted and 507 rejected. They come from the original audit plus the first 2,004 lines of the enlargement file, which is WP4's final freeze (SHA-256 checked against `outputs/snapshot/results.json → meta.audit_freeze`), the same sample D4 and the prereg use. D3's pairing rule (2022–26, v1 dated before the decision) differs slightly from WP4's primary pairs (2023–26: 803 / 508). *Integration pass 2:* the D3 fixer pass had read a pre-freeze pin of 1,620 lines (1,127 pairs, 694 / 433; LLM-slot v1 titles 22 / 4), and the original run 1,025 lines; the conclusion is unchanged.
   - Accepted: 23 v1 titles carry an LLM slot word; 0 additions, 4 drops. The addition rate among the 787 accepted pairs without an LLM slot word in v1 is 0 [exact 95% CI 0, 0.47%].
   - Rejected: 5 v1 titles carry an LLM slot word; 1 addition, 0 drops.
   - The rejected arm has only 5 LLM-slot v1 titles, below the V7 minimum of 10 per arm, so the slot words are unauditable by the study's rule (WP4 SB3 on its primary pairs: 23 / 5, unauditable). The DiD of net additions (accepted − rejected) is −0.69 pp, from 5 flip events; we give no CI for it.
   - The audit shows no sign that camera-ready editing added LLM slot words, but it is underpowered. What rules out camera-ready editing as the source of the break is the camera-ready-free NA pool, which gives the same OR (2.18 [1.28, 3.70]).

## 3. H3b: improvement-framed titles became less common in 2026 and unified/beyond/bridging rose; no register turnover is identified

**Large areas.** The 16 large areas are harmonised primary areas with ≥ 500 titles in 2025+2026 (the pilot rule).

**Rates per 1,000 titles (F3.2, `fig_F3_2_register_heatmap`; `register_summary.csv`).**
- R24 fell from 63.1 (2025) to 47.8 (2026) across all titles. In the large areas the rate was 65.4 in 2025 and 48.5 in 2026 once 2026 is standardised to the 2025 area mix.
- R26 doubled, from 23.3 to 46.4 (large areas, standardised: 23.5 → 45.5).
- F3.2 now uses one colour scale for both panels, with a colourbar each. Cells with fewer than 100 titles are not coloured; their rate and n are printed instead. The 2023 All-areas row is observed, not imputed.

**Sign tests (2025 → 2026, real area labels).**
- R24 fell in **14 of 16** large areas (one-sided sign test p = 0.002); 4 areas are individually significant at 0.05.
- R26 rose in **16 of 16** (p = 1.5 × 10⁻⁵); 7 individually significant.
- Both exceed the predictions (≥ 10 and ≥ 12) and the falsification line of 9.
- Across all 21 areas: R24 down in 15, R26 up in 20.
- The sign test measures how pervasive the shift is across areas. It is one year-pair, with a 2026-wide shock (15.4k submissions, new desk regime), so it cannot separate a register turnover from a 2026-wide change, and the 16 areas are not independent replicates.

**Poisson model** (area FE + year FE, log-titles offset; quasi-Poisson SEs; `register_poisson.csv`).
- Within-area RR 2026/2025: R24 **0.744 [0.652, 0.848]**; R26 **1.945 [1.686, 2.244]**.
- These are nearly identical across the 2023–26, 2024–26 and 2025–26 windows and the all-area variant (R24 RR 0.744–0.752; R26 1.944–1.959).
- The same model gives the full arc: R24 rose steeply into 2025 (RR 2023/2025 0.36 [0.28, 0.47]; 2024/2025 0.77 [0.65, 0.92]) and then fell; R26 was flat from 2023 to 2025 (RR 0.89, 1.06) and then doubled.
- **2024 → 2025 context, taxonomy-confounded.** From 2024 to 2025, R24 rose in 13 of 14 areas present in both years while R26 rose in only 4. This comparison crosses the 2025 taxonomy change: two new 2025 areas (foundation/frontier models, time series) absorbed papers that 2024 filed elsewhere. Reassigning the 1,187 papers of those two areas in 2025 to a 2024-taxonomy area (classifier on bge abstract embeddings trained on 2024 labels) gives R24 up in 12 of 14 and R26 up in 4 of 14 (R24 RR 2024/2025 0.78 [0.68, 0.89]). The context reading holds, but it is not a clean within-area comparison.

**Decisive check: neutral synonyms and meaning-fixed shares** (`register_neutral_benchmark.csv`; added after the identification audit).
- If the 2024 register turned over, R24 should fall *relative to* its neutral synonyms, or the LLM-favoured share *within* meaning-fixed slots should fall. Neither happens.
- Within-area quasi-Poisson RR 2026/2025 (16 large areas, area FE):
  - R24: 0.744 [0.642, 0.862], down in 14/16.
  - N24 = improv* | utili[sz]* | exploit* (neutral counterparts): **0.689 [0.585, 0.811]**, down in 15/16.
  - improv* alone: 0.613 [0.508, 0.739]; enhanc* alone: 0.735 [0.592, 0.912].
  - R24 relative to N24 (stacked, area × family FE), ratio of RRs: **1.08 [0.86, 1.36]**: no differential decline. NA pool: 1.05 [0.83, 1.34].
- Within meaning-fixed slots, the LLM-variant share *rose* from 0.641 (2025) to 0.668 (2026): logit with slot FE + area FE, OR **1.14 [0.87, 1.49]**, up in 7 and down in 9 of 16 areas. NA pool: 0.642 → 0.676, OR 1.16 [0.85, 1.58].
- What fell in 2026 is how often titles are framed as improving or exploiting something. LLM-favoured and neutral words fell alike. The per-1,000 rate test cannot separate lexical choice from what titles are about.

**How informative is the 16-area sign test? Word-churn benchmark** (`register_word_churn.csv`).
- The same statistics for all 365 title words with ≥ 80 titles in 2025+2026 (large areas):
  - Of the 38 words with an area-stratified RR ≥ 1.5, 58% are up in ≥ 12 of 16 areas. Of the 85 words with RR ≤ 0.8, 56% are down in ≥ 10 of 16.
  - Among frequent words (≥ 20 per 1,000 in 2025), 64% pass one of the two H3b thresholds.
  - Words up in 16 of 16 areas include "framework", "when", "via" and "for"; up in 15 of 16 include "reasoning", "test-time", "multimodal" and "LLMs".
- R26's RR of 1.95 is in the top 3.6% of words, and no random 4-word family matched on the 2025 rate reached it (0 of 1,000). That is what selection on the outcome produces: R26 = {unified, unifying, beyond, bridging} was chosen after the scout and pilot saw these words rise from 2025 to 2026 in this same discovery data (LITERATURE_BRIEF §3.3; PLAN H3b quotes the pilot).
- The R26 rise is real and diffuse (the identification audit finds topic100-FE RR 1.98 [1.68, 2.32], with the top 10 topics carrying 43% of the excess). It is not a pre-registered confirmation, and it is not an LLM register: the vintage mirror (§4) is null.

**Robustness.**

| Variant | R24 down | R26 up |
|---|---|---|
| NA pool | 12/16 (p = 0.038) | 15/16 |
| Non-LLM subset | 14/16 | 14/16 |
| R24 without the sense-ambiguous stems boost*/elevat* | 12/16 | — |
| R24 without harness/unveil | 14/16 | — |
| Word counts instead of title indicators | 14/16 | 16/16 |
| Neutral counterparts N24 (benchmark) | 15/16 | — |

- Single words: enhanc* 40.3 → 29.8 per 1k (down in 12/16); unified 9.0 → 20.0 (up in 12/16); beyond 9.2 → 16.6 (12/16); bridging 3.7 → 7.0 (15/16).
- The plan's pilot quoted enhanc* 36.7 → 25.6 and unified 11.2 → 23.1. The v2 stems count enhanced/enhancement, and R26 excludes "unify", so the levels differ; the direction does not.

**Verdict: the pre-specified sign thresholds are met, but the result is descriptive and no register turnover is identified.** The R24 fall is shared with neutral synonyms, the within-slot LLM share did not fall, and R26 was selected in-sample. Its p-value (and the H3b entry in the Holm family) is not a valid test of R26. Inference is deferred to held-out CT8.

**2023 column (deviation).** `primary_area` does not exist before 2024. 2023 areas in the heat map and in the 2023–26 Poisson model were imputed:
- Method: multinomial logistic regression on bge abstract embeddings, trained on 2025.
- Accuracy: 5-fold CV 0.56; 0.50 on 2024 true labels (a pessimistic check, because 2024 lacks two areas).
- Use: imputed areas never enter the H3b test. Area-level 2023 cells should be read as approximate.

## 4. H3c: F26-marked abstracts are less likely to carry the 2024 register; the F24 arm (beyond shared words) and the R26 mirror are null on the pre-registered outcome

**Primary model.** 2025–26 papers: logit of R24 in the title on F24 and F26, with year FE, topic100 FE, log authors, llm_topic and log title length, clustered by topic100 (F3.3, `fig_F3_3_vintage_forest`; `vintage_models.csv`). Logit n = **24,283**: the 82 papers in topic100 cells without R24 variation drop out; the LPM uses all 24,365.
- OR(F24 → R24) = **1.11 [0.92, 1.34]**.
- OR(F26 → R24) = **0.76 [0.64, 0.89]**.
- Ratio **1.46 [1.17, 1.83]**, one-sided p = 0.0005.
- The pre-registered prediction (ratio > 1) holds and the falsification (≤ 1) is rejected.
- The LPM with topic100 × year FE agrees: F24 +0.52 pp, F26 −1.21 pp, difference +1.73 pp [+0.55, +2.91], against a base rate of 5.3%.

**What carries the contrast.**
- **Shared lemmas (co-primary).** RARE21 contains "harness" and "unveil", which are also R24 stems. With both removed from F24 and R24, OR(F24 → R24) = **1.00 [0.81, 1.23]**, OR(F26 → R24) = 0.76 [0.63, 0.91], ratio **1.32 [1.04, 1.66]**, p = 0.011. (F24 only: 1.33 [1.06, 1.68]; R24 only: 1.36 [1.07, 1.73].) There is no positive F24 → R24 association beyond the shared words. What survives is that F26 papers avoid R24.
- **F26 marks the 2026 vintage only in 2026.** In 2025 its prevalence (2.7%) equals the 2021–24 base rate, so 2025 F26 papers are base-rate users of "principled", "sharply" and similar words. Yet the pooled model draws part of its contrast from 2025, where OR(F26) = 0.56 [0.28, 1.12] (n_F26 = 236).
  - By year: 2025 ratio 2.13 [1.04, 4.38]; **2026 ratio 1.29 [0.97, 1.71]**, with OR(F24) = 1.00 and OR(F26) = 0.78.
  - F26 arm restricted to 2026 (F26 × 2026 as the arm, F26 × 2025 as a covariate, F24 pooled): ratio 1.43 [1.13, 1.81]; also without the shared lemmas: 1.28 [1.00, 1.64].
- **F24 in its own year.** F24 → R24 is strong in 2024: OR 1.96 [1.49, 2.58] (exploratory, since F26 is nearly absent in 2024). It decays to 1.19 in 2025 and 1.00 in 2026.
- **Camera-ready-free pool.** NA pool ratio 1.24 [0.94, 1.63], p = 0.065.
- In cells (`vintage_cells.csv`), 2026 R24 rates per 1k are 53 for F24-only abstracts, 38 for F26-only and 49 for neither.

**Alternatives.**
- **Genre / composition.** If F26 papers simply wrote fewer "improvement" titles, they would avoid the neutral synonyms too. They do not: OR(F26 → N24) = **1.04 [0.81, 1.34]**, with N24 = improv* | utili[sz]* | exploit* as the outcome; OR(F24 → N24) = 0.74 [0.55, 1.00]. Conditional on meaning, the contrast is larger:
  - R24 among titles that have R24 or N24: F24 1.55 [1.12, 2.14] vs F26 0.66 [0.47, 0.93], ratio **2.34 [1.48, 3.71]**. Without harness/unveil: F24 1.39 [0.98, 1.97] vs F26 0.65 [0.46, 0.92], ratio 2.13 [1.33, 3.40]. NA pool: 1.70 [1.00, 2.90].
  - LLM slot variant given a filled slot (slot FE): F24 1.96 [1.27, 3.02] vs F26 0.85 [0.51, 1.45], ratio 2.29 [1.14, 4.63]. Without harness/unveil: F24 1.86 [1.15, 3.01], ratio 2.28 [1.07, 4.85]. NA pool: 2.50 [1.02, 6.12].
  - So once meaning is held approximately fixed, F24 papers do choose the LLM-favoured variant more, even without the shared words. The genre alternative does not explain the contrast.
- **Writer type.** F26 is dominated by "principled" (n = 1,076; OR 0.67 [0.49, 0.92] on R24, with typography as a covariate) and "brittle" (n = 146; 0.38 [0.15, 0.98]). Both were in use long before LLMs. Authors who signal rigour may simply avoid hype verbs. Other F26 components: genuine* 0.61 [0.34, 1.10]; high-stakes 0.73 [0.38, 1.40]; sharply 0.94; reframe* 1.04 (all small).
- **Pre-LLM placebo** (2018–23, where F24 and F26 are false positives, i.e. writer or genre style): OR(F24 → R24) 1.35 [0.74, 2.47], OR(F26 → R24) 1.27 [0.57, 2.81], ratio 1.07 [0.37, 3.09]; 2020–23: F24 1.47 [0.80, 2.68], ratio 1.48 [0.51, 4.25]. The placebo is null but has almost no power. The F24 arm in 2025–26 (1.11) is no larger than the pre-LLM writer-style association (1.35–1.47). Only the F26-avoidance side carries LLM-era information, and the placebo cannot rule out that it is a writer-type effect.

**Robustness (ratio [95% CI]).**

| Variant | Ratio |
|---|---|
| **Shared-lemma-free (co-primary)** | **1.32 [1.04, 1.66]** |
| 2025 only | 2.13 [1.04, 4.38] |
| 2026 only | 1.29 [0.97, 1.71] |
| F26 arm = F26 × 2026 | 1.43 [1.13, 1.81] |
| **NA pool** | **1.24 [0.94, 1.63], p = 0.065** |
| Non-LLM subset | 1.37 [0.96, 1.96] |
| bge topics | 1.49 [1.15, 1.94] |
| F24 ≥ 2 words | 1.88 [1.24, 2.86] |
| F26 words only | 1.62 [1.16, 2.25] |
| F26 typography only | 1.32 [1.01, 1.71] |
| Exclusive F24-only vs F26-only | 1.47 [1.17, 1.85] |
| Meaning-fixed (R24 among R24-or-N24 titles) | 2.34 [1.48, 3.71] |
| Meaning-fixed, slot-based | 2.29 [1.14, 4.63] |
| Pre-LLM placebo 2018–23 | 1.07 [0.37, 3.09] |

- **Pilot reconciliation.** With the pilot's own lexicons (19-term regex, -ing forms) the pilot reproduces exactly: 1.30 [1.09, 1.54] vs 0.83 [0.66, 1.05], ratio 1.55 [1.19, 2.04]. The v2 lexicons weaken the F24 arm.
- **Mirror (exploratory).** For R26 the contrast is null: OR(F26 → R26) 1.21 [1.01, 1.45] vs OR(F24 → R26) 1.16 [0.94, 1.44]; ratio F26/F24 1.05 [0.79, 1.39]. F3.3 now labels the mirror F26/F24, the predicted direction.

**Assessment.** The prediction is met by the pre-registered test. The contrast is driven by F26 papers avoiding R24 (in 2025 F26 is not yet a 2026-vintage marker), and there is no positive F24 → R24 alignment beyond shared words on the pre-registered outcome. It is weaker in the NA pool and in 2026 alone (CIs include 1), and the R26 mirror is null. Conditional on meaning, F24 papers prefer the LLM-favoured variant and F26 papers do not (ratio ≈ 2.1–2.3), so the genre alternative fails. The writer-type alternative is not ruled out: the pre-LLM placebo has no power, and the F26 arm rests on "principled" and "brittle". **We do not read H3c as "title register lines up with the abstract's LLM vintage".**

## 5. H3d: abstract fingerprints go with lexical slot choice somewhat more than with NAME structure; the margin is small against the population comparator

**Same-paper comparator (PLAN).** On the 1,506 slot-filled papers of 2024–26 (1,508 slot rows; 381 with F = 1), two LPMs within topic100 × year (F3.4, `fig_F3_4_signature`; `signature_models.csv`):
- LLM slot variant: +8.0 pp [cluster-bootstrap 95% CI +3.1, +13.1], implied OR **1.42 [1.14, 1.79]** at the F = 0 mean of 0.61.
- NAME, same papers: −2.2 pp [−7.7, +3.7], implied OR **0.91 [0.72, 1.16]** at the F = 0 mean of 0.41.
- Ratio **1.55 [1.11, 2.21]** (seemingly-unrelated topic100-cluster bootstrap, 1,000 draws). P(ratio ≤ 1) = 0.005, but P(ratio < 1.5) = 0.42: the 1.5× prediction is met by the point estimate only.

**Why the same-paper comparator is biased.** It is fitted on papers selected on a common effect of F and NAME.
- The opener rule reads the subtitle of a NAME title, so NAME titles fill a slot more often. F raises filling too, and the two interact negatively. P(slot filled | NAME, F), 2024–26: 4.33% (0, 0), 5.47% (NAME 0, F 1), 5.78% (1, 0), 5.74% (1, 1). In the LPM within topic100 × year: F +1.18 pp, NAME +1.33 pp, F × NAME −1.26 pp.
- Conditioning on a filled slot multiplies the F–NAME odds ratio by 0.0574 · 0.0433 / (0.0578 · 0.0547) = **0.79**. The population NAME OR of 1.14 times 0.79 gives 0.90, the observed same-paper value (0.91).
- On the same papers, NAME is also the slot word's position: among opener-slot rows, "after a NAME lead" and NAME coincide in every case. OR_NAME there measures where F papers put the verb, not structural NAME fashion.

**Population comparator (co-primary after the audit).** NAME on all 30,130 papers of 2024–26, the same topic100 × year FE and the same (no further) controls as the slot LPM, with a joint topic100-cluster bootstrap that resamples the slot rows, their papers and the population together (1,000 draws):
- OR(F → NAME), all papers: **1.14 [1.08, 1.21]** (+3.1 pp, SE 0.64). F is associated with NAME; the CI excludes 1.
- Ratio OR_slot / OR_NAME: **1.24 [0.99, 1.57]**; P(ratio ≤ 1) = 0.030; P(ratio ≥ 1.5) = 0.066.
- With log authors on every side: OR_NAME 1.12 [1.06, 1.18], ratio 1.23 [0.99, 1.58]. (The earlier reported population ratio of 1.27 mixed a log-authors NAME model with a slot model without it, and had no interval.)

**Verdict: partially supported.** The PLAN's same-paper test passes (ratio ≥ 1.5 by the point estimate, CI excluding 1), but that comparator is collider-conditioned. Against the population comparator, the ratio > 1 is marginal (CI [0.99, 1.57]) and the 1.5× prediction is not met. "Barely moves NAME (OR ≈ 0.9–1.1)" is withdrawn: in the population, fingerprinted abstracts go with NAME titles (OR 1.12–1.14).

**Robustness** (OR_slot, OR_NAME on the same papers, OR_NAME in the population, and both ratios; 95% cluster-bootstrap CIs):

| Variant | OR_slot | OR_NAME, same papers | OR_NAME, all papers | Ratio, same papers | Ratio, all papers |
|---|---|---|---|---|---|
| 2024–26 pooled (primary) | 1.42 [1.14, 1.79] | 0.91 [0.72, 1.16] | 1.14 [1.08, 1.21] | 1.55 [1.11, 2.21] | 1.24 [0.99, 1.57] |
| 2024 | 1.64 [1.02, 2.86] | 0.62 [0.26, 1.27] | 1.17 [1.00, 1.37] | 2.66 [1.28, 6.43] | 1.39 [0.86, 2.50] |
| 2025 | 1.83 [1.20, 2.81] | 1.27 [0.72, 2.13] | 1.15 [1.03, 1.29] | 1.44 [0.83, 2.91] | 1.60 [1.02, 2.51] |
| 2026 | 1.13 [0.80, 1.61] | 0.85 [0.58, 1.19] | 1.13 [1.05, 1.23] | 1.32 [0.84, 2.20] | 0.99 [0.71, 1.45] |
| 2024–25 (excluding 2026) | 1.75 [1.29, 2.43] | 0.98 [0.65, 1.55] | 1.16 [1.05, 1.26] | 1.78 [1.08, 2.94] | 1.52 [1.08, 2.14] |
| NA pool | 1.54 [1.23, 1.96] | 1.02 [0.78, 1.34] | 1.15 [1.08, 1.22] | 1.51 [1.02, 2.23] | 1.34 [1.07, 1.74] |
| Non-LLM subset | 2.03 [1.43, 3.19] | 0.81 [0.57, 1.12] | 1.10 [1.02, 1.21] | 2.51 [1.65, 4.07] | 1.83 [1.25, 2.93] |
| F without harness/unveil | 1.41 [1.15, 1.73] | 0.91 [0.70, 1.16] | 1.15 [1.09, 1.22] | 1.54 [1.13, 2.09] | 1.22 [0.99, 1.53] |
| Abstract lacks the slot word | 1.39 [0.97, 2.10] | 0.71 [0.47, 1.06] | 1.14 [1.08, 1.21] | 1.95 [1.13, 3.50] | 1.21 [0.84, 1.86] |
| Word fingerprints only | 1.43 [1.13, 1.84] | 0.89 [0.70, 1.14] | 1.12 [1.05, 1.19] | 1.60 [1.15, 2.24] | 1.28 [1.00, 1.69] |
| Opener slots only | 1.46 [1.15, 1.90] | 0.90 [0.71, 1.14] | 1.14 [1.08, 1.21] | 1.62 [1.17, 2.28] | 1.28 [1.00, 1.66] |
| Improve slot only | 1.47 [1.01, 2.64] | 0.85 [0.56, 1.24] | 1.14 [1.08, 1.20] | 1.73 [1.03, 3.44] | 1.29 [0.88, 2.31] |
| F24 as F | 1.73 [1.35, 2.23] | 0.87 [0.64, 1.20] | 1.21 [1.13, 1.30] | 1.98 [1.32, 2.93] | 1.43 [1.10, 1.86] |
| F26 as F | 0.93 [0.68, 1.35] | 1.02 [0.66, 1.52] | 1.06 [0.98, 1.15] | 0.92 [0.60, 1.48] | 0.88 [0.64, 1.26] |
| **F_d1 (D1's fingerprint)** | 1.29 [0.92, 1.81] | 1.07 [0.74, 1.54] | 1.08 [1.01, 1.16] | 1.20 [0.78, 1.84] | 1.19 [0.84, 1.65] |
| Pre-LLM 2018–23 (F = false positives; 26 F = 1 slot rows) | 1.62 [0.65, 3.26] | not estimable | 0.88 [0.71, 1.07] | — | 1.85 [0.73, 3.87] |

- Logit with slot, year and topic100 FE (same papers): OR_slot 1.58 [1.15, 2.12], OR_NAME 0.87, ratio 1.80 [1.15, 2.69]. Conditional logit within topic100 × year: 1.52 vs 0.90, ratio 1.68.
- **By year.** On the same papers the ratio is largest in 2024 because F papers used NAME less there (OR_NAME 0.62). The slot association itself is 1.64 [1.02, 2.86] in 2024, 1.83 [1.20, 2.81] in 2025 and 1.13 [0.80, 1.61] in 2026. Against the population comparator the signature is clearest in 2024–25 (ratio 1.52 [1.08, 2.14]) and absent in 2026 (0.99). The signature belongs to the F24 generation: F24 as F gives 1.43 [1.10, 1.86] against the population, F26 as F gives 0.88.
- **Title-specific choice.** OR_slot loses significance once titles whose abstract repeats the slot word are excluded (1.39 [0.97, 2.10]). Its same-paper ratio of 1.95 comes from a lower OR_NAME (0.71); against the population it is 1.21 [0.84, 1.86].
- **Pre-LLM baseline.** In 2018–23, when every fingerprint is a false positive (writer style), F already went with the LLM slot variant (OR 1.62 [0.65, 3.26]; 26 F = 1 rows) and not with NAME (0.88 [0.71, 1.07]). The pre-period slot estimate is too noisy for a difference-in-differences. Taken at face value, F → NAME moved more from pre to post (0.88 → 1.14) than F → slot did (1.62 → 1.42). The data give no evidence that the lexical association *grew* more than the structural one.
- Title typography alone appears in only 5 slot papers and is not estimable.

**Link to D1.** D1-H1e bounds the tool with F_d1 = F24 (≥ 2 RARE21 words) ∪ F26 ∪ title typography, while H3d's primary uses F_any = F24 (≥ 1 RARE21 word) ∪ F26 ∪ title typography. The two fingerprints differ only in the F24 threshold, which is what the contrast below isolates. With F_d1, the slot uplift is not significant (OR 1.29 [0.92, 1.81]) and the ratio against the population NAME comparator is 1.19 [0.84, 1.65]. The D3 positive control therefore does **not** validate D1's F_d1 bound. With F_any, the fingerprint detects a lexical association (OR 1.42) that is modestly larger than its association with NAME in the population (OR 1.14).

## 6. H3e (exploratory): second-hand diffusion stays unresolved

**Descriptives.** In the pooled slots the LLM-variant share was about 0.29 in 2022–23. In 2024 it was 0.49 [0.43, 0.56] for F = 0 papers and 0.68 [0.58, 0.77] for F = 1 papers; in 2025, 0.61 vs 0.75 (`fig_S3_1_secondhand`). Unfingerprinted papers broke too.

**Estimate** (`secondhand_ustar.csv`; pooled over slots with common post weights):
- U* = (p_F0 − p_pre)/(p_F1 − p_pre) = **0.65 [0.50, 0.81]**, for 2024–25 against the 2022–23 baseline (fixed in advance). P(U* > 0.8) = 0.034, so the upper CI bound just reaches 0.81.
- F = 0 papers rose by 23.9 pp [16.5, 31.2]; F = 1 papers by 37.0 pp [28.1, 45.9].
- **Empty bootstrap cells (fixed).** The S-study-adj cells are tiny: its 2022–23 baseline holds 4 titles and its 2024 F = 1 cell 3. They are empty in 1.7% and 4.65% of the 2,000 bootstrap draws. Empty cells used to count as share 0; they are now skipped in numerator and denominator alike. The CI is unchanged to three decimals.
- Sensitivities:
  - without S-study-adj (baseline on 4 titles): 0.61 [0.47, 0.76];
  - topic100-cluster bootstrap instead of the year-stratified paper bootstrap: 0.65 [0.50, 0.81];
  - baseline 2023 only: 0.58; baseline 2018–23: 0.69; slot-specific pre-trends extrapolated: 0.55;
  - 2024 alone: 0.60 [0.32, 0.98]; 2024–26: 0.76 [0.63, 0.89] (P(U* > 0.8) = 0.25);
  - per slot (2024–25): improve 0.56, reveal 0.62, exploit **1.07** (above 0.8; 36 baseline titles), study-adj −1.95 (not interpretable: 4 baseline titles; F = 1 papers fell).
- F1 contamination: FPR 5.9% against P(F = 1) of 0.18–0.21 implies 28–34% false positives among F = 1. Correcting for it gives U*_c = 0.45.
- 2026 (U* = 0.91) is not interpreted: F24 prevalence falls from 19.2% to 9.1% (consistent with recall decay), and the gap mechanically closes.

**Verdict.** U* < 0.8, so by the pre-registered rule **no second-hand-diffusion claim is made**.
- The F = 0 rise could be explained if about half to two thirds of unfingerprinted slot titles came from undetected LLM users. Fingerprint recall is unknown, so this is plausible.
- The data cannot separate undetected tool use from humans copying the wording. One slot (exploit) and the 2024–26 window come close to or exceed 0.8, so the verdict is "unresolved", not "rejected".

## 7. Deviations from PLAN.md

1. **Inventory.** The V2 drops and the frozen inventory are described in §1. The primary opener rule is the PLAN text, not the pilot's rule. Both choices lower the OR (pilot-like 2.80 vs primary 2.18).
2. **Added break-timing analyses for H3a.** These are randomization over break years, a year-level REML meta-regression (study convention, §0) and the event study. The event study and the year-FE break scan were added after the scan showed a comparable stacked OR at 2023. The controls-without-via rows were added in the adversarial pass. The frozen-trend event study, the per-1,000 variant rates and the pilot-like row were added in the fixer pass. All are reported; none replaces the primary test.
3. **H3b.**
   - 2023 areas are imputed (heat map and Poisson only).
   - The test uses family rates; the pilot quoted single words.
   - Large areas follow the pilot's ≥ 500 rule.
   - Fixer pass: the neutral-synonym benchmark, within-slot shares, the word-churn benchmark and the taxonomy-reassigned 2024 → 2025 context were added. H3b is now reported as descriptive.
4. **H3c.** Frozen v2 lexicons, not the pilot's (§4); the pilot lexicons are rerun only as reconciliation. Fixer pass: a shared-lemma-free co-primary, an F26 × 2026 arm, pre-LLM placebos, genre (N24) and meaning-fixed benchmarks, and F26 components.
5. **H3d.**
   - LPM coefficients are converted to implied ORs at the F = 0 means.
   - The NAME comparator is fitted on the same papers, as the PLAN says. After the audit, the population NAME comparator (same FE, same controls, joint bootstrap) is co-primary, because the same-paper comparator is collider-conditioned.
   - Logit and conditional-logit versions are added; so are D1's fingerprint F_d1, a pre-LLM row and a log-authors row.
6. **H3e.**
   - The window (2024–25) and baseline (2022–23) were fixed before estimation.
   - Slots are pooled with common weights.
   - The contamination correction is an added sensitivity.
   - Fixer pass: empty bootstrap cells are skipped instead of counted as share 0; no-study-adj and topic100-cluster-bootstrap sensitivities.
7. **Camera-ready audit.** It uses the original audit plus WP4's frozen enlargement sample (the first 2,004 lines, SHA-256 checked; `d3_slots.wp4_enlarge_freeze`). The D3 fixer pass had pinned 1,620 lines while the enlargement was still running; integration pass 2 moved D3 to the final freeze (prereg revision 3, because `d3_slots.py` is required code). It is reported as counts with exact intervals, without a bootstrap CI.
8. **Holm.** The pre-specified family H3a–H3d is kept as registered. A sensitivity family (H3b excluded, H3d with the population comparator) is reported next to it.

## 8. Limitations

- **Discovery data only.** The pre-registered thresholds were set from pilots on these same rows, and two key words were chosen after looking at them: "enhancing" (H3a) and R26 (H3b). Held-out CT4/CT7/CT8 are the confirmation; their projected power is modest (0.23–0.32 at the Holm/BH thresholds).
- **Small pre-period cells.** Before 2024, the slots hold 26–129 titles a year. The slot-specific trends are noisy, and S-study-adj's trend is unidentified. The slot-versus-control contrast survives a level contrast (2.46), but the controls also shift under it (OR 2.02). The break is not sharply dated and may start with the 2023 cohort, which predates ChatGPT.
- **Addition, not substitution.** In 2024 LLM-favoured openers were added without displacing neutral synonyms. The share measure is conditional on a slot being filled, and slot filling responds to the tool.
- **Controls.** The control contrast depends on via/using, which is itself a drifting LLM-associated word; it is a control for 2024 only. towards/novel alone are too sparse to anchor the contrast under the PLAN's shared-trend model, and the pooled controls shift significantly at every candidate break year except 2024.
- **Meaning is held approximately fixed.** V2 swap preservation is 0.75–0.79 for the reveal and exploit LLM variants in the post period.
- **Fingerprints are bounds.** Recall is unknown and decays across model generations; specificity is 94% (2021–22).
  - H3c and H3d therefore compare noisy proxies.
  - Non-differential misclassification of a single fingerprint attenuates its OR. With two correlated fingerprints in one model (F24 and F26 in H3c), or a ratio of two ORs (H3d), the bias in the ratio can go either way. V2 precision is also era-dependent for borderline words (unleashing 0.60 pre vs 1.00 post).
- **Associational.** The comparisons are within topic100 × year, but who uses fingerprinted abstracts is not random. A writer-type confound (people who like "enhancing" also like "showcase") would produce H3c and H3d without any tool. In 2018–23, before LLMs, fingerprint false positives already went with the LLM slot variant (OR 1.62, noisy). The slot design holds meaning approximately fixed, not the author.
- **Camera-ready.** Accepted titles may be post-decision. The NA-pool replications (H3a 2.18; H3b 12/16 and 15/16; H3d population ratio 1.34) avoid this, but H3c is weaker there (ratio 1.24 [0.94, 1.63]). The arXiv audit (WP4's final freeze) holds too few slot-word titles in the rejected arm (5) to bound decision-stage editing by the V7 rule. The edits it does see remove LLM slot words.
- **Areas.** Area labels change taxonomy in 2025, and 2023 is imputed. The H3b test uses 2025–26 only, where labels are native; the 2024 → 2025 context is taxonomy-confounded.

## Thesis line for the study write-up (replaces PLAN §1 bullet 5)

PLAN §1 still reads "LLM-favoured verbs jump at 2024 (pooled OR ≈ 2.7) … Their register turns over in step with the model generation whose markers appear in the same paper's abstract." That line predates these results and is overstated. PLAN.md is locked and was not edited. The write-up should use:

> In meaning-fixed title slots, LLM-favoured verb openers rose from 2024 (pooled OR 2.2 [1.4, 3.4]; accelerating from 2024, not sharply dated against 2023; carried mainly by the improve slot; an addition of new openers rather than a swap of synonyms) while control pairs stayed flat at the 2024 break. Fingerprinted abstracts go with the LLM-favoured slot variant somewhat more than with NAME titles (1.24× [0.99, 1.57] against the population NAME comparator), so the lexical-over-structural margin is small. The 2026 fall of R24 is shared by its neutral synonyms, so no register turnover is identified.

(The same text is in `results.json` → `thesis_line_D3`.)

## Files

**Scripts.** `src/analyses/d3_slots.py`, `d3_register.py`, `d3_vintage.py`, `d3_signature_bound.py`, `d3_collect.py`.

**Outputs** (`outputs/d3_register/`).
- Results and inventory: `results.json`, `slot_inventory.json`.
- Tables: `T3_1_slot_models.{csv,md}`.
- Figures, each as `.pdf`, `.png` and `.csv`:
  - `fig_F3_1_slot_shares`: (a) shares per slot and pooled, (b) per-1,000 rates of LLM and neutral variants, (c) control pairs;
  - `fig_F3_2_register_heatmap`;
  - `fig_F3_3_vintage_forest`;
  - `fig_F3_4_signature`, with both NAME comparators;
  - `fig_S3_1_secondhand`.
- H3a: `slots_results.json`, `slot_robustness.csv`, `slot_loo.csv`, `slot_per_slot.csv`, `slot_placebo_breaks.csv`, `slot_event_study.csv` (both trend versions), `slot_year_level.csv`, `slot_shares_by_year.csv`, `slot_variant_rates.csv`, `slot_variant_rate_shift.csv`, `slot_audit_pairs.csv`, `slot_audit_flips.csv`.
- H3b: `register_results.json`, `register_rates.csv`, `register_area_tests.csv`, `register_summary.csv`, `register_poisson.csv`, `register_neutral_benchmark.csv`, `register_word_churn.csv`, `area_imputation.json`.
- H3c: `vintage_results.json`, `vintage_models.csv`, `vintage_lpm.csv`, `vintage_cells.csv`, `fingerprint_prevalence_by_year.csv`.
- H3d and H3e: `signature_results.json`, `signature_models.csv`, `secondhand_ustar.csv`, `secondhand_shares.csv`.
- Logs: `d3_slots.log`, `d3_register.log`, `d3_vintage.log`, `d3_signature_bound.log`, `d3_collect.log`.
- Audit and fixer files: `outputs/audit/d3_code/`, `outputs/audit/d3_ident/`, `outputs/audit/d3_register/`, `outputs/audit/d3/` (fix log, number check, pre-fix backup).


## Audit response

Three audits (code, identification, reporting) raised 28 issues. Each was re-checked by running code before anything was changed (the auditors' scripts in `outputs/audit/d3_code/` and `d3_ident/` reproduce). All 28 were judged valid, two of them only in part (D3-C9: PLAN.md is locked; D3-C3: one sub-claim reversed by a new check, see the row). Every primary estimate reproduces exactly. Three things moved: the bootstrap CIs of the H3d subset rows (per year, improve-only), because the joint bootstrap now also draws topics present only in the population (e.g. 2024 OR_slot [0.995, 2.79] → [1.02, 2.86]); the camera-ready audit, which now reads a pinned, larger slice of the enlargement file (WP4's final freeze since integration pass 2); and the U* bootstrap tails, under the empty-cell fix. Everything else is added analyses, new comparators and rewording. Details and commands are in `outputs/audit/d3/fix_log.md`.

| Issue | Valid? | What changed | Claim weakened |
|---|---|---|---|
| D3-C1 (H3d collider) | Yes. P(filled \| NAME, F) reproduced: 4.33 / 5.47 / 5.78 / 5.74%; selection factor 0.79 | `signature()` now also fits NAME on all papers of the same years/subset (same topic100 × year FE, same controls), with a joint topic100-cluster bootstrap (same draws for the slot rows, their papers and the population). Reported as co-primary, with a collider diagnostic. Verdict changed to "partially supported". | Yes. H3d is "partially supported": population ratio 1.24 [0.99, 1.57], P(≤ 1) = 0.030, 1.5× not met. "Barely move NAME (OR ≈ 0.9–1.1)" and "lexical, not structural" are withdrawn. OR_slot loses significance when the abstract lacks the slot word. |
| D3-C2 (F_d1 vs F_any) | Yes | H3d now has an F_d1 row: OR_slot 1.29 [0.92, 1.81], population ratio 1.19 [0.84, 1.65]. "The same fingerprints" is deleted. §5 states that the D3 control uses F_any and does not validate D1's F_d1 bound. | Yes: the positive control for D1 is not established with D1's fingerprint. |
| D3-C3 (H3c vintage reading) | Yes, except one sub-claim. "No positive F24 alignment beyond shared words" holds on the pre-registered outcome but not conditional on meaning (new rows). | Shared-lemma-free co-primary (ratio 1.32 [1.04, 1.66], OR_F24 1.00); by-year reporting; an F26 × 2026 arm (1.43 [1.13, 1.81]); pre-LLM placebos added to `vintage_models.csv`; n fixed to 24,283. Verdict changed to "prediction met; vintage reading not established". | Yes. The heading "title register lines up with the abstract's LLM vintage" is withdrawn. |
| D3-C4 (U* empty cells) | Yes. 1.7% / 4.65% of draws have an empty cell | `ustar()` skips a slot-year when a cell is empty, in point and bootstrap alike. Added rows without study-adj (0.61 [0.47, 0.76]) and with a topic100-cluster bootstrap (0.65 [0.50, 0.81]). | No (verdict unchanged; CI unchanged to three decimals) |
| D3-C5 (pilot n) | Yes | The sentence is corrected. The truly pilot-like row (any-lead + full lexicon: n = 2,321, OR 2.80 [1.89, 4.15]) is in `slot_robustness.csv` and T3.1; the old "pilot-like" label is now "any-lead rule (V2 drops kept)". | Disclosure: the two analyst choices lower the OR from 2.80 to 2.18 (conservative). |
| D3-C6 (event-study trends) | Yes | `event_study` is relabelled "trends estimated jointly". New `event_study_frozen` fits trends on 2018–22 only and uses them as an offset, with a topic100-cluster bootstrap over both stages: 2023 2.17 [0.74, 6.89], 2024 4.82 [1.23, 19.3]. | No (conclusions unchanged) |
| D3-C7 (control sets) | Yes | Folded into C1: no log authors on either side by default, plus a row with log authors on every side (ratio 1.23 [0.99, 1.58]). Both have bootstrap intervals. | The population ratio is 1.24, not 1.27, and now has a CI. |
| D3-C8 (2024 → 2025 taxonomy) | Yes | Labelled taxonomy-confounded. Added a sensitivity that reassigns the 1,187 papers in the two new 2025 areas to 2024-taxonomy areas: R24 up in 12/14 (was 13/14), R26 up in 4/14. | Slightly (context only) |
| D3-C9 (PLAN thesis line) | Yes (stale), in part: PLAN.md is locked and is not a direction file | The corrected line is in RESULTS ("Thesis line…") and in `results.json` (`thesis_line_D3`): pooled OR 2.2 [1.4, 3.4], accelerating from 2024, improve slot, addition not substitution, small lexical margin, no turnover. PLAN.md is not edited. | Yes, in the write-up line |
| D3-ID-1 (H3b is genre, not register) | Yes. Reproduced: R24 0.744 vs N24 0.689; ratio 1.08 [0.86, 1.36]; within-slot share OR 1.14 [0.87, 1.49] | `d3_register.neutral_benchmark` (all papers and NA pool) feeds §3 as the decisive check. The H3b heading, verdict and thesis wording are recast. | Yes. "Register turned over in 2026" and "in step with the model generation" are withdrawn. |
| D3-ID-2 (R26 selected in-sample; sign test) | Yes | `d3_register.word_churn` added: 58% / 56% of large movers pass the thresholds; R26 is in the top 3.6% of words and 0/1,000 random families reach it. H3b is labelled descriptive, and its p is flagged as not a valid test. The sensitivity Holm family excludes H3b. | Yes: H3b is no longer a confirmatory result, and R26 is not called an LLM register. |
| D3-ID-3 (addition vs substitution) | Yes. Reproduced: LLM variants RR 3.91 [1.84, 8.29] vs neutral 1.17 [0.70, 1.94] | `d3_slots.variant_rates` writes per-1,000 rates and level shifts (all papers, NA pool, non-LLM subset); F3.1 gains panel (b). §2 is rephrased. | Yes. "Where meaning is held fixed … broke" becomes "conditional on a slot being filled"; slot entry itself responds to the tool. |
| D3-ID-4 (H3d comparator, pre-LLM, years) | Yes | Same changes as C1, plus a NAME ⇔ post-NAME position check (1,403/1,403 opener rows), a pre-LLM 2018–23 row and population ratios by year (2024–25 1.52 [1.08, 2.14]; 2026 0.99). | Yes: "more lexical than structural, by a small margin". No evidence that the lexical association grew more than the structural one from pre to post. |
| D3-ID-5 (H3c writer type) | Yes | Pre-LLM placebo rows, F26 components (principled 0.67 [0.49, 0.92], n = 1,076; brittle 0.38) and genre benchmarks added. The writer-type alternative is stated in the H3c assessment. The meaning-fixed rows were added too; they strengthen the contrast (2.1–2.3), and F24 is positive there. | Yes (vintage reading); partly offset by the meaning-fixed rows |
| D3-ID-6 ("enhancing" selected in-sample) | Yes | Stated in the H3a verdict, Summary and Limitations: without "enhancing" the OR is 1.72 [1.04, 2.84]. | Yes: OR ≥ 2 depends on an in-sample word. |
| D3-ID-7 (camera-ready wording) | Yes | "Cannot have created" is removed. The conclusion is attributed to the NA-pool replication; the audit is described as directionally consistent but underpowered. | Yes (wording) |
| D3-R1 (control evidence omitted) | Yes | §2 adds the control break-scan row (2020–25), the level-contrast row (controls 2.02 [1.73, 2.37]) and per-pair control ORs. `results.json` H3a gains `control_break_scan` and `level_contrast_no_slot_trends`. The verdict text and Limitations are revised. | Yes: the control null holds for the pre-registered 2024 specification only. |
| D3-R2 (H3d table) | Yes | The table now shows OR_slot, both OR_NAMEs and both ratios. "Clearest in 2024" is replaced by the per-year slot ORs. The summary phrase "(CI includes 1.11)" is replaced. | Yes |
| D3-R3 (discovery vs confirmation) | Yes | Discovery-split statement and projected held-out power (0.27 / 0.23 / 0.32 at α 0.0083) added to the header and `results.json`. "Confirmatory tests" becomes "pre-specified discovery tests". | Yes (framing) |
| D3-R4 (causal headings) | Yes | The §2, §4 and §5 headings and "toolkit detects LLM influence" are rewritten; "cannot have created the break" is replaced. | Yes (wording) |
| D3-R5 (swap preservation) | Yes | V2 swap-preservation numbers are added to §1; Limitations now say meaning is held approximately fixed. | Yes (wording) |
| D3-R6 (n, rounding) | Yes | Logit n = 24,283 (82 dropped), LPM n = 24,365; summary p_Holm = 0.0014. | No |
| D3-R7 (audit stale, false precision) | Yes | The enlargement read is pinned (`ENLARGE_N = 1,620`, recorded in `slots_results.json`). Reported as counts with exact Clopper–Pearson intervals; the bootstrap DiD CI is dropped. Now 1,127 pairs; rejected arm 4 LLM-v1 titles (below V7). *Superseded in integration pass 2:* D3 now reads WP4's final freeze (2,004 lines): 1,317 pairs, rejected arm 5 LLM-v1 titles (still below V7). | Yes (wording; the qualitative conclusion holds) |
| Integration pass 2 (audit versions; F_any wording) | Yes | `d3_slots` reads WP4's frozen enlargement sample (2,004 lines, SHA-256 checked) instead of the 1,620-line pre-freeze pin, so D3, D4, WP4 and the prereg use one audit freeze (prereg revision 3). §5 "Link to D1" now defines F_any in full. `results.json` stores H3e's verdict code as "unresolved" (was "not_supported"; the wording was already "unresolved"). | No (audit: rejected arm 5 < 10, still unauditable) |
| D3-R8 (F3.2 scaling) | Yes | One colour scale across panels with a colourbar each; cells with n < 100 greyed with n printed; All-areas row not flagged as imputed; caption updated. | No |
| D3-R9 (F3.3, F3.1) | Yes | F3.3 mirror labelled F26/F24 with a wider gap. F3.1 lists the omitted cells, has control Wilson bands and adds the pooled-slot line. | No |
| D3-R10 (H3b wording) | Yes | "Nearly identical (R24 0.744–0.752; R26 1.944–1.959)"; "large-area rate 65.4 (2025) → 48.5 (2026, standardised)"; sign-test caveat added. | Yes (wording) |
| D3-R11 (fingerprint wording) | Yes | "(pre-ChatGPT; treated as false positives)"; "F24 prevalence falls …, consistent with recall decay"; the misclassification sentence is corrected for two correlated fingerprints. | Yes (wording) |
| D3-R12 (omitted estimates) | Yes | Per-slot U* (exploit 1.07 > 0.8), the 2024–26 window (0.76) and the U* upper bound 0.81 are reported; the stacked opener-position cells are filled (2.76; 2.00 [0.78, 5.11]); the logs list is complete. | Slightly (H3e is "unresolved", not "rejected") |

**Verdict changes.** H3b: supported → "thresholds met (descriptive); register turnover not identified". H3c: supported → "prediction met; vintage reading not established". H3d: supported → "partially supported". H3a ("supported") and H3e ("unresolved") keep their labels with added qualifications.
