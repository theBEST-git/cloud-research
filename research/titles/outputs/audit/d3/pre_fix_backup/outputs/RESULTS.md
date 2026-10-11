# D3. The machine register: meaning-fixed slots, vintage turnover and a bounded second-hand diffusion test

WP7 results for PLAN.md §D3. Code is in `research/titles/src/analyses/`:
- `d3_slots.py`: freezes the slot inventory; H3a; T3.1; F3.1; camera-ready audit of opener words.
- `d3_register.py`: H3b; F3.2.
- `d3_vintage.py`: H3c; F3.3.
- `d3_signature_bound.py`: H3d, H3e; F3.4; supplementary S3.1.
- `d3_collect.py`: builds `results.json` (estimates, verdicts, Holm).

Run order, from `src`: `OMP_NUM_THREADS=2 python -m analyses.d3_slots`, then `d3_register`, `d3_vintage`, `d3_signature_bound` and `d3_collect`. Total runtime is about 5 minutes. All outputs are in `outputs/d3_register/`.

Three conventions hold throughout:
- All associations are associational.
- Titles of accepted papers may be camera-ready versions. Every key result is therefore repeated in the camera-ready-free NA pool.
- "LLM-favoured" names a word class defined before estimation. It is not a claim that a given title was machine-written.

## Summary

| Hypothesis | Pre-registered test | Result | Verdict (Holm p) |
|---|---|---|---|
| **H3a** slot break | Pooled slot post OR ≥ 2; controls in [0.67, 1.5]; slot − control > 0 | Slots **2.18 [1.41, 3.38]**; controls **0.87 [0.64, 1.18]**; stacked slot/control **2.55 [1.53, 4.25]** | **Supported** (p_Holm = 0.0009). Timing and control-pair caveats below. |
| **H3b** register turnover | 2025→26 within area: R24 down in ≥ 10/16, R26 up in ≥ 12/16 | R24 down in **14/16**; R26 up in **16/16**. Within-area RR 2026/2025: R24 **0.74 [0.65, 0.85]**, R26 **1.94 [1.69, 2.24]** | **Supported** (p_Holm = 0.004) |
| **H3c** vintage alignment | OR(F24→R24) / OR(F26→R24) > 1 | 1.11 [0.92, 1.34] vs 0.76 [0.64, 0.89]; ratio **1.46 [1.17, 1.83]** | **Supported** (p_Holm = 0.001), but driven by F26 papers avoiding R24, and weaker in the NA pool |
| **H3d** lexical vs structural signature | OR(F→LLM slot variant) ≥ 1.5 × OR(F→NAME), same papers | 1.42 [1.14, 1.79] vs 0.91 [0.72, 1.16]; ratio **1.55 [1.11, 2.21]** | **Supported** (p_Holm = 0.005). The ratio > 1 is established; the 1.5× margin is not (CI includes 1.11). |
| **H3e** second-hand diffusion (exploratory) | Claim only if U* > 0.8 | U* = **0.65 [0.50, 0.81]** (2024–25 vs 2022–23); 0.45 after F1-contamination correction | **Unresolved**: no second-hand-diffusion claim |

The four confirmatory tests are one-sided; Holm is applied over H3a–H3d (raw p 0.00024, 0.0021, 0.00045, 0.005; adjusted 0.0009, 0.0042, 0.0014, 0.005).

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

**Opener rule (primary).** Following the PLAN text, the slot word is the first word of the title, or of the subtitle when the title is "NAME: …".
- V2 found lower sense precision for titles that fill a slot only under the pilot's any-colon-lead rule (0.83 vs 0.90). That rule is a robustness row.
- Sample, 2018–26: **1,922 slot-filled titles from 1,920 papers**. By slot: improve 979, reveal 511, exploit 321, study-adj 111.
- Control-pair titles: 6,925 (towards/toward 1,250, novel/new 392, via/using 5,283).
- The pilot's n of 2,362 used the any-lead rule and the undropped lexicon. Those choices give 2,163 here.

**Register and fingerprints** (features_v2, unchanged):
- R24 = title contains any of enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*.
- R26 = any of unified, unifying, beyond, bridging.
- F24 = abstract has ≥ 1 RARE21 word.
- F26 = abstract has ≥ 1 of {principled, reframe*, genuine*, brittle, auditable, sharply, high-stakes}, or U+2011 / en-dash letter compounds in the title or abstract.
- F = F24 ∪ F26 ∪ title typography.
- Prevalence of F in 2021–22 (pre-ChatGPT, so all false positives) is 5.9%. It is 21.1%, 17.6% and 26.2% in 2024–26. F24 falls from 19.2% (2024) to 9.1% (2026) while F26 rises from 2.5% to 18.6% (`fingerprint_prevalence_by_year.csv`).

## 2. H3a: LLM-favoured wording broke at 2024 in meaning-fixed slots; control pairs did not

**Descriptives (F3.1, `fig_F3_1_slot_shares`).**
- The pooled LLM-variant share of slot-filled titles was 0.06–0.34 in 2019–2023 (0.34 in 2023). It reached 0.54 in 2024, 0.64 in 2025 and 0.67 in 2026.
- S-improve ("Enhancing/Boosting… vs Improving…") moved from 0.25 (2018–23) to 0.71 (2024–26).
- S-reveal moved from 0.09 to 0.29; S-exploit from 0.62 to 0.84.
- The pooled control-pair share moved from 0.72 (2023) to 0.74 (2024). Among the controls, via/using is the only drifting pair: it rises gradually from 2018 and jumps in 2026 (0.78 → 0.90).

**Primary model (T3.1, block A).** Logit `y ~ slot FE + slot × (t − 2023) + post + llm_topic`, 2018–26, SEs clustered by topic100:
- Pooled slots: post OR **2.18 [1.41, 3.38]**, one-sided p = 0.0002 (n = 1,922; 1,508 post).
- Control pairs: post OR **0.87 [0.64, 1.18]** (n = 6,925). The point estimate is inside [0.67, 1.5]; the lower CI bound is slightly below 0.67.
- Stacked slot + control model, post × LLM-slot (the CT4 parameter): OR **2.55 [1.53, 4.25]**, p = 0.0002. LPM equivalent: +20.3 pp [+11.1, +29.5].
- The control-pair estimate reproduces the pilot (0.87 [0.64, 1.17]). The slot OR is smaller than the pilot's 2.69 [1.80, 4.01] because of the stricter opener rule and the V2 drops:
  - pilot-like any-lead rule: 2.49 [1.66, 3.74];
  - no V2 drops: 2.44 [1.61, 3.70].
- **Verdict:** the pooled OR is ≥ 2 and its CI excludes 1; the controls do not break; slot − control > 0. **Supported**; not falsified.

**Per slot (T3.1, block B; BH over the four slots).**

| Slot | Post OR | BH q |
|---|---|---|
| S-improve | 2.63 [1.39, 4.97] | 0.006 |
| S-reveal | 1.93 [0.74, 5.00] | 0.18 |
| S-exploit | 1.80 [0.55, 5.94] | 0.22 |
| S-study-adj | not identified | — |

- S-study-adj has only 6 pre-2024 titles, so its slot trend is not identified; the LPM gives −13 pp [−72, +46].
- Only the improve slot survives BH on its own. The pooled result is not carried by one word, though: leave-one-variant-out keeps the pooled OR between 1.72 (dropping "enhancing", CI [1.04, 2.84]) and 2.32, and every CI excludes 1 (`slot_loo.csv`).
- The pilot's "improve slot alone ≈ 4.3" does not reproduce under the slot-specific-trend model.

**Robustness (`slot_robustness.csv`).** Pooled slot OR / stacked OR:

| Specification | Pooled slot OR | Stacked OR |
|---|---|---|
| NA pool (camera-ready-free) | 2.18 [1.28, 3.70] | 2.57 [1.40, 4.71] |
| Non-LLM subset | 2.59 [1.57, 4.28] | 2.96 [1.64, 5.34] |
| topic100 FE | 2.28 [1.40, 3.74] | 2.65 [1.54, 4.56] |
| bge topic100 FE | 2.37 | 2.75 |
| Excluding titles whose abstract has the same verb (n = 913) | 1.94 [1.03, 3.69] | 2.26 [1.13, 4.54] |
| Title-start openers only | 2.38 [1.47, 3.87] | — |
| Post-NAME openers only (n = 728, few pre titles) | 1.70 [0.66, 4.38] | — |
| Excluding 2026 | 2.27 [1.36, 3.80] | 2.42 [1.34, 4.37] |
| 2024 as the only post year | 2.38 [1.39, 4.07] | 2.62 [1.44, 4.79] |
| With 2017 | 2.26 | 2.77 |
| Without 2019 | 2.37 | 3.00 |
| Unweighted V2 rule (also drops unleashing) | 2.15 [1.38, 3.33] | 2.50 |
| + log authors | 2.25 | 2.63 |
| Stacked with year FE (absorbs common year shocks) | — | 3.16 [1.90, 5.26] |
| Year-level REML meta-regression on slot × year cells, with group-year shocks; t(6) / t(12) | 2.76 [1.26, 6.03], p = 0.010 | 2.97 [1.02, 8.62], p = 0.023 |

- The accepted-only subsample is underpowered: 2.14 [0.81, 5.67].

**Caveats on timing and controls.** A skeptical reader should weigh three of them.

1. **The break is not sharply dated against 2023.**
   - A scan of the break year on the full data, 2020–25 (`slot_placebo_breaks.csv`):
     - The pooled-slot OR peaks at 2024: 0.65, 0.50, 1.00, 1.91, **2.18**, 1.04 for 2020–25.
     - The stacked contrast is as large at 2023 as at 2024: OR 3.21 vs 2.55, z 3.59 vs 3.59. With year FE: 3.75 vs 3.16, z 3.88 vs 4.44.
   - Randomization p over the six candidate years is therefore 1/6 for the pooled slots (the minimum attainable with six candidates) and 2/6 for the stacked contrast. Randomization inference alone cannot reach 0.05 here.
   - An event study of deviations from 2018–22 slot trends (`slot_event_study.csv`) gives these slot ORs: 2023 **2.41 [0.98, 5.93]** (p = 0.055); 2024 5.19 [1.74, 15.5]; 2025 7.02; 2026 8.71. For the slot − control contrast: 2023 2.79 [1.03, 7.55]; 2024 6.26 [1.93, 20.4].
   - So the deviation grows from 2024 on, but part of it may already start with the 2023 cohort, submitted in September 2022, two months before ChatGPT's release.
   - Pre-only placebo breaks (2018–23 data) are null: slot ORs 0.99 / 0.39 / 1.60 at 2020 / 2021 / 2022, all CIs including 1.
   - We therefore describe the shift as "accelerating from 2024". We do not describe it as a ChatGPT-dated step.
2. **The contrast leans on via/using.** via/using makes up 76% of the control titles. Without it, the remaining controls (towards, novel) give:
   - post OR 1.60 [0.98, 2.62] in the PLAN level-shift model, and a stacked contrast of only 1.41 [0.74, 2.68].
   - In the PLAN model the trend is shared between pre and post years. towards/toward declines after 2024 (0.92 → 0.82), which steepens the fitted trend and pushes up the level shift.
   - In the event study, whose trends are fitted on 2018–22 only, the towards/novel controls show no break (ORs 0.63–0.83 in 2023–25, all CIs including 1). There the slot − control contrast without via is 6.39 [1.68, 24.3] in 2024.
   - The pre-registered criterion is met. The slot-versus-control contrast is still specification-dependent once via is removed.
3. **Camera-ready.** We matched 845 pre-decision arXiv v1 titles to the submitted titles: 528 accepted and 317 rejected, from the original audit plus 1,025 enlargement records (`slot_audit_flips.csv`).
   - Only 15 accepted and 3 rejected v1 titles carry an LLM slot word, below the V7 threshold of 10 per arm.
   - Accepted titles lost LLM slot words (3 drops, 0 additions) and never gained one. The net-add DiD is −0.88 pp [−1.89, −0.19].
   - Camera-ready editing therefore cannot have created the break, and the NA-pool estimate is unchanged at 2.18.

## 3. H3b: the 2024 register turned over in 2026, within areas

**Large areas.** The 16 large areas are harmonised primary areas with ≥ 500 titles in 2025+2026 (the pilot rule).

**Rates per 1,000 titles (F3.2, `fig_F3_2_register_heatmap`; `register_summary.csv`).**
- R24 fell from 63.1 (2025) to 47.8 (2026); standardised to the 2025 area mix, from 65.4 to 48.5.
- R26 doubled, from 23.3 to 46.4 (std 23.5 → 45.5).

**Sign tests (2025 → 2026, real area labels).**
- R24 fell in **14 of 16** large areas (one-sided sign test p = 0.002); 4 areas are individually significant at 0.05.
- R26 rose in **16 of 16** (p = 1.5 × 10⁻⁵); 7 individually significant.
- Both exceed the predictions (≥ 10 and ≥ 12) and the falsification line of 9.
- Across all 21 areas: R24 down in 15, R26 up in 20.

**Poisson model** (area FE + year FE, log-titles offset; quasi-Poisson SEs; `register_poisson.csv`).
- Within-area RR 2026/2025: R24 **0.744 [0.652, 0.848]**; R26 **1.945 [1.686, 2.244]**.
- These are identical across the 2023–26, 2024–26 and 2025–26 windows and the all-area variant.
- The same model gives the full arc:
  - R24 rose steeply into 2025 (RR 2023/2025 0.36 [0.28, 0.47]; 2024/2025 0.77 [0.65, 0.92]) and then fell.
  - R26 was flat from 2023 to 2025 (RR 0.89, 1.06) and then doubled.
- From 2024 to 2025, R24 rose in 13 of 14 areas present in both years while R26 rose in only 4. The 2026 swap is a turnover, not a continuation.

**Robustness.**

| Variant | R24 down | R26 up |
|---|---|---|
| NA pool | 12/16 (p = 0.038) | 15/16 |
| Non-LLM subset | 14/16 | 14/16 |
| R24 without the sense-ambiguous stems boost*/elevat* | 12/16 | — |
| R24 without harness/unveil | 14/16 | — |
| Word counts instead of title indicators | 14/16 | 16/16 |

- Single words: enhanc* 40.3 → 29.8 per 1k (down in 12/16); unified 9.0 → 20.0 (up in 12/16); beyond 9.2 → 16.6 (12/16); bridging 3.7 → 7.0 (15/16).
- The plan's pilot quoted enhanc* 36.7 → 25.6 and unified 11.2 → 23.1. The v2 stems count enhanced/enhancement, and R26 excludes "unify", so the levels differ; the direction does not.

**Verdict: supported.**

**2023 column (deviation).** `primary_area` does not exist before 2024. 2023 areas in the heat map and in the 2023–26 Poisson model were imputed:
- Method: multinomial logistic regression on bge abstract embeddings, trained on 2025.
- Accuracy: 5-fold CV 0.56; 0.50 on 2024 true labels (a pessimistic check, because 2024 lacks two areas).
- Use: imputed areas never enter the H3b test. Area-level 2023 cells should be read as approximate.

## 4. H3c: title register lines up with the abstract's LLM vintage

**Primary model.** 2025–26 papers (n = 24,365): logit of R24 in the title on F24 and F26, with year FE, topic100 FE, log authors, llm_topic and log title length, clustered by topic100 (F3.3, `fig_F3_3_vintage_forest`; `vintage_models.csv`).
- OR(F24 → R24) = **1.11 [0.92, 1.34]**.
- OR(F26 → R24) = **0.76 [0.64, 0.89]**.
- Ratio **1.46 [1.17, 1.83]**, one-sided p = 0.0005.
- The prediction (ratio > 1) holds and the falsification (≤ 1) is rejected. **Supported.**
- The LPM with topic100 × year FE agrees: F24 +0.52 pp, F26 −1.21 pp, difference +1.73 pp [+0.55, +2.91], against a base rate of 5.3%.

**How to read it.**
- The contrast comes mainly from F26 papers (2026-generation abstract markers) *avoiding* the 2024 register, not from F24 papers using it more.
- F24 → R24 is strong in 2024, the generation's own year: OR 1.96 [1.49, 2.58]; exploratory, since F26 is nearly absent in 2024.
- It decays to 1.19 in 2025 and 1.00 in 2026.
- In cells (`vintage_cells.csv`), 2026 R24 rates per 1k are 53 for F24-only abstracts, 38 for F26-only and 49 for neither.

**Robustness (ratio [95% CI]).**

| Variant | Ratio |
|---|---|
| 2025 only | 2.13 [1.04, 4.38] |
| 2026 only | 1.29 [0.97, 1.71] |
| **NA pool** | **1.24 [0.94, 1.63], p = 0.065** |
| Non-LLM subset | 1.37 [0.96, 1.96] |
| bge topics | 1.49 [1.15, 1.94] |
| F24 ≥ 2 words | 1.88 [1.24, 2.86] |
| F26 words only | 1.62 [1.16, 2.25] |
| F26 typography only | 1.32 [1.01, 1.71] |
| Exclusive F24-only vs F26-only | 1.47 [1.17, 1.85] |

- RARE21 contains "harness" and "unveil", which are also R24 stems. Removing them from F24, from R24, or from both gives ratios of 1.33 [1.06, 1.68], 1.36 [1.07, 1.73] and 1.32 [1.04, 1.66]. Same-word repetition is not the driver.
- **Pilot reconciliation.** With the pilot's own lexicons (19-term regex, -ing forms) the pilot reproduces exactly: 1.30 [1.09, 1.54] vs 0.83 [0.66, 1.05], ratio 1.55 [1.19, 2.04]. The v2 lexicons weaken the F24 arm.
- **Mirror (exploratory).** For R26 the contrast is null: OR(F26 → R26) 1.21 [1.01, 1.45] vs OR(F24 → R26) 1.16 [0.94, 1.44]; ratio F26/F24 1.05 [0.79, 1.39].

**Assessment.** Supported on the pre-registered test. It is weaker in the camera-ready-free pool (CI includes 1) and in single years, and it is asymmetric: F26 papers avoid R24, but no matching F26 → R26 preference appears.

## 5. H3d: the tool leaves a lexical, not a structural, signature

**Primary model.** On the 1,506 slot-filled papers of 2024–26 (1,508 slot rows; 381 with F = 1), two LPMs within topic100 × year (F3.4, `fig_F3_4_signature`; `signature_models.csv`):
- LLM slot variant: +8.0 pp [cluster-bootstrap 95% CI +3.1, +13.1], implied OR **1.42 [1.14, 1.79]** at the F = 0 mean of 0.61.
- NAME: −2.2 pp [−7.7, +3.7], implied OR **0.91 [0.72, 1.16]** at the F = 0 mean of 0.41.
- Ratio **1.55 [1.11, 2.21]** (seemingly-unrelated topic100-cluster bootstrap, 1,000 draws). P(ratio ≤ 1) = 0.005.
- The prediction (≥ 1.5) is met by the point estimate and the falsification (≤ 1) is rejected. **Supported**, with a caveat: the data exclude ratio ≤ 1 but not ratios between 1.1 and 1.5.

**Robustness (ratio).**

| Variant | Ratio |
|---|---|
| Logit with slot, year and topic100 FE | 1.80 [1.15, 2.69] (OR_slot 1.58, OR_NAME 0.87) |
| Conditional logit within topic100 × year | 1.68 (1.52 vs 0.90) |
| NA pool | 1.51 [1.02, 2.23] |
| Non-LLM subset | 2.51 [1.65, 4.07] |
| F without the shared lemmas harness/unveil | 1.54 [1.13, 2.09] |
| Abstract lacks the slot word | 1.95 [1.14, 3.49] |
| Word fingerprints only | 1.60 [1.15, 2.24] |
| Opener slots only | 1.62 [1.17, 2.28] |
| Improve slot only | 1.73 [1.04, 3.27] |
| 2024 | 2.66 [1.26, 7.67] |
| 2025 | 1.44 [0.77, 2.72] |
| 2026 | 1.32 [0.81, 2.23] |
| F24 as F | 1.98 [1.32, 2.93] |
| F26 as F | 0.92 [0.60, 1.48] |

- The signature is a 2024-vintage (F24) phenomenon. It is clearest in 2024 and fades by 2026, in line with H3b/H3c.
- Title typography alone appears in only 5 slot papers and is not estimable.

**Comparator choice.** The PLAN specifies NAME on the same papers. On all 30,130 papers of 2024–26 (D1 H1e-ii specification), the NAME uplift is +2.5 pp [1.3, 3.8], OR 1.12 [1.06, 1.18]. Against that comparator the ratio is 1.27, which still exceeds 1 but not 1.5.

**Link to D1.** As the positive control for D1-H1e, the same fingerprints that barely move NAME (OR ≈ 0.9–1.1) shift the meaning-fixed slot choice (OR ≈ 1.4–1.6). The toolkit detects LLM influence where the outcome is lexical.

## 6. H3e (exploratory): second-hand diffusion stays unresolved

**Descriptives.** In the pooled slots the LLM-variant share was about 0.29 in 2022–23. In 2024 it was 0.49 [0.43, 0.56] for F = 0 papers and 0.68 [0.58, 0.77] for F = 1 papers; in 2025, 0.61 vs 0.75 (`fig_S3_1_secondhand`). Unfingerprinted papers broke too.

**Estimate** (`secondhand_ustar.csv`; pooled over slots with common post weights):
- U* = (p_F0 − p_pre)/(p_F1 − p_pre) = **0.65 [0.50, 0.81]**, for 2024–25 against the 2022–23 baseline (fixed in advance).
- F = 0 papers rose by 23.9 pp [16.5, 31.2]; F = 1 papers by 37.0 pp [28.1, 45.7].
- Sensitivities:
  - baseline 2023 only: 0.58;
  - baseline 2018–23: 0.69;
  - slot-specific pre-trends extrapolated: 0.55;
  - 2024 alone: 0.60 [0.33, 0.98].
- F1 contamination: FPR 5.9% against P(F = 1) of 0.18–0.21 implies 28–34% false positives among F = 1. Correcting for it gives U*_c = 0.45.
- 2026 (U* = 0.91) is not interpreted, because RARE21 recall decays (19.2% → 9.1%) and the gap mechanically closes.

**Verdict.** U* < 0.8, so by the pre-registered rule **no second-hand-diffusion claim is made**.
- The F = 0 rise could be explained if about half to two thirds of unfingerprinted slot titles came from undetected LLM users. Fingerprint recall is unknown, so this is plausible.
- The data cannot separate undetected tool use from humans copying the wording.

## 7. Deviations from PLAN.md

1. **Inventory.** The V2 drops and the frozen inventory are described in §1. The primary opener rule is the PLAN text, not the pilot's rule.
2. **Added break-timing analyses for H3a.** These are randomization over break years, a year-level REML meta-regression (study convention, §0) and the event study. The event study and the year-FE break scan were added after the scan showed a comparable stacked OR at 2023. The controls-without-via rows were added in the adversarial pass. All are reported, none replaces the primary test.
3. **H3b.**
   - 2023 areas are imputed (heat map and Poisson only).
   - The test uses family rates; the pilot quoted single words.
   - Large areas follow the pilot's ≥ 500 rule.
4. **H3c.** Frozen v2 lexicons, not the pilot's (§4). The pilot lexicons are rerun only as reconciliation.
5. **H3d.**
   - LPM coefficients are converted to implied ORs at the F = 0 means.
   - The NAME comparator is fitted on the same papers, as the PLAN says; the population NAME OR is reported too.
   - Logit and conditional-logit versions are added.
6. **H3e.**
   - The window (2024–25) and baseline (2022–23) were fixed before estimation.
   - Slots are pooled with common weights.
   - The contamination correction is an added sensitivity.
7. **Camera-ready audit.** It uses the original audit plus the still-running enlargement file as it stood at run time (1,025 lines). Rerunning `d3_slots` later will add pairs.

## 8. Limitations

- **Small pre-period cells.** Before 2024, the slots hold 26–129 titles a year. The slot-specific trends are noisy, and S-study-adj's trend is unidentified. The break is robust as a level contrast but not sharply dated. It may start with the 2023 cohort, which predates ChatGPT.
- **Controls.** The control contrast depends on via/using, which is itself a drifting LLM-associated word; it is a control for 2024 only. towards/novel alone are too sparse to anchor the contrast under the PLAN's shared-trend model.
- **Fingerprints are bounds.** Recall is unknown and decays across model generations; specificity is 94% (2021–22).
  - H3c and H3d therefore compare noisy proxies.
  - Their contrasts are attenuated, not inflated, by non-differential misclassification.
  - That does not hold if the fingerprint vintages differ in quality.
- **Associational.** The comparisons are within topic100 × year, but who uses fingerprinted abstracts is not random. A writer-type confound (people who like "enhancing" also like "showcase") would produce H3c/H3d without any tool. The slot design holds meaning fixed, not the author.
- **Camera-ready.** Accepted titles may be post-decision. The NA-pool replications (H3a 2.18; H3b 12/16 and 15/16; H3d 1.51) avoid this, but H3c is weaker there (ratio 1.24 [0.94, 1.63]). The arXiv audit holds too few slot-word titles to bound decision-stage editing; the edits it does see remove LLM slot words.
- **Areas.** Area labels change taxonomy in 2025, and 2023 is imputed. The H3b test uses 2025–26 only, where labels are native.

## Files

**Scripts.** `src/analyses/d3_slots.py`, `d3_register.py`, `d3_vintage.py`, `d3_signature_bound.py`, `d3_collect.py`.

**Outputs** (`outputs/d3_register/`).
- Results and inventory: `results.json`, `slot_inventory.json`.
- Tables: `T3_1_slot_models.{csv,md}`.
- Figures:
  - `fig_F3_1_slot_shares`, `fig_F3_2_register_heatmap`, `fig_F3_3_vintage_forest`, `fig_F3_4_signature`, `fig_S3_1_secondhand`, each as `.pdf`, `.png` and `.csv`.
- H3a: `slots_results.json`, `slot_robustness.csv`, `slot_loo.csv`, `slot_per_slot.csv`, `slot_placebo_breaks.csv`, `slot_event_study.csv`, `slot_year_level.csv`, `slot_shares_by_year.csv`, `slot_audit_pairs.csv`, `slot_audit_flips.csv`.
- H3b: `register_results.json`, `register_rates.csv`, `register_area_tests.csv`, `register_summary.csv`, `register_poisson.csv`, `area_imputation.json`.
- H3c: `vintage_results.json`, `vintage_models.csv`, `vintage_lpm.csv`, `vintage_cells.csv`, `fingerprint_prevalence_by_year.csv`.
- H3d and H3e: `signature_results.json`, `signature_models.csv`, `secondhand_ustar.csv`, `secondhand_shares.csv`.
- Logs: `d3_slots.log`, `d3_signature_bound.log`.
