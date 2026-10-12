# WP4 Results: camera-ready snapshot bounds (D4 decision-stage bound, V7 route validation, §4 gate)

Work package WP4. Pre-registered in `docs/PLAN.md` §D4 ("Decision-stage bound"), §3 V7 and §4 (Gate); common definitions §0.

**Status: final.** Every number below comes from one frozen audit sample: the original 616-paper audit plus the complete enlargement (2,000 records without a network error, from the first 2,004 lines of `cache/arxiv_audit_enlarge.jsonl`; SHA-256 of those bytes `dd51d5faaa0a7937…`, full hash in `results.json` → `meta.audit_freeze`). This run supersedes the interim run on the first 254 enlargement records. That run's files are archived in `interim_254/`, and the audit response at the end of this file lists what changed.

**Scripts.**
- `src/analyses/snapshot_final.py` runs the analysis (about 45 s) and writes every table, figure and `results.json`.
- `src/analyses/snapshot_bounds.py` holds the building blocks (pairs, flip tables, tipping points, stage prevalences, findability, route validation). `snapshot_final.py` uses them unchanged. The file is hashed as required code in the pre-registration bundle (`outputs/prereg/bundle.sha256`), so it was not edited.
- `src/analyses/audit_v2.py` ran the arXiv re-queries in the background: route validation, v1 abstracts and the enlargement.
- `src/analyses/snapshot_final_report.py` writes this file from `results.json` and the tables.

**Language.** All acceptance statements are associational. Author information enters only through the first author's declared name, used as an arXiv search key. It is never treated as a verified person.

**Why the audit matters.** The export is a post-decision snapshot. Accepted papers may carry camera-ready titles, while rejected, withdrawn and desk-rejected papers keep submission-stage text.

**How the audit works.**
- Each audited paper's arXiv version 1, posted before the ICLR decision date, is compared with the stored title.
- Rejected papers' v1-vs-stored differences measure everything that is *not* camera-ready editing: arXiv-vs-OpenReview wording, rebuttal-period edits and pre-submission revisions.
- The accepted-minus-rejected difference in net feature flips is the **net-flip DiD**, D. It estimates the camera-ready excess, which can bias any acceptance association of a title feature. It does so only if the non-camera-ready drift is the same in both arms; §2 tests this by v1 timing.

**Tipping point.**
- A net camera-ready addition D raises P(f | accepted) = P₃ by D, and P(f | reviewed) = P₂ by a₂·D. Here a₂ = 0.403 is the accepted share of the reviewed set (2024–26, year-standardised).
- The submission-stage gain is G_dec(D) = (P₃ − D)/(P₂ − a₂D). Setting it to 1 gives the tipping point D\* = (P₃ − P₂)/(1 − a₂). G_total uses s0 and a₀ in the same way.
- Within a single year, D\* equals P₃ minus the prevalence among reviewed, non-accepted papers. With year-standardised pooling it differs from the accepted-minus-rejected risk difference (NAME: D\* 2.92 pp vs 3.27 pp).

**Auditable.** A feature is auditable when two conditions hold:
1. arXiv metadata can carry it. arXiv titles are never ALL-CAPS and never contain U+2011/U+2013 typography, and arXiv abstracts never contain an em dash. For such features the "net flip" is just the stored prevalence.
2. At least 10 titles in *each* arm have the feature in their v1 (pre-stated).

**Gate (G_dec acceptance associations).** A claim passes only if all three conditions hold:
1. The feature is auditable.
2. The editing-corrected 95% CI of G excludes 1. This CI pairs a universe-bootstrap replicate with an audit draw D ~ N(D̂, pseudo-flip SE).
3. Its one-sided identification p-value survives Holm across all 18 auditable title features at α = 0.025, the one-sided level of the PLAN's 95% CI rule (PLAN §0 requires Holm within a confirmatory family).

The identification p-value tests H₀ "the true DiD is at or beyond the tipping point". It uses z = (D\* − D̂)/√(se_D² + se_D\*²), where se_D is the pseudo-flip SE and se_D\* is the universe-bootstrap SE of the tipping point. The interim rule had no multiplicity control and ignored se_D\*: it required only the point tipping point beyond one audit 95% CI, plus an observed G CI excluding 1. That rule is reported as "uncorrected".

---

## Verdict summary

| ID | Claim tested | Estimate (95% CI unless stated) | Criterion | Verdict |
|---|---|---|---|---|
| SB1 | PLAN D4: NAME G_dec is not identified by the audit (pilot: tip ≈ 1.8 pp vs DiD +2.1, se 2.4) | DiD **+1.48 pp [−0.63, 3.59]** (803/508 pairs). Tip **D\* = 2.92 pp**; one-sided p = 0.127. Observed G_dec 1.050 [1.027, 1.073]; G_dec at the audit point estimate 1.025 | Identified iff D\* lies beyond the audit CI | **Supported** (not identified) |
| SB2 | Gate §4: some title feature's acceptance association (G_dec ≠ 1) survives the audit | **0 of 26** features pass (18 auditable). Smallest identification p: O-union w/o ALL-CAPS 0.016 (Holm 0.29); Compound 0.041 (Holm 0.69); Sentence case 0.044 (Holm 0.70). Uncorrected rule: 2 pass (O-union w/o ALL-CAPS, Compound) | Auditable, corrected 95% CI excludes 1, Holm p < 0.025 | **Not supported** (no claim survives multiplicity control) |
| SB3 | V7: rare lexical features are unauditable | v1-present accepted/rejected: 'using' 19/25, R24 31/17, R26 28/8, LLM slot word 23/5, title typography 0/0 (channel) | ≥ 10 per arm and arXiv-measurable | **Partially supported** ('using' and R24 became auditable as the audit grew) |
| SB4 | Accepted papers are more findable; IPW leaves the NAME bound unchanged | Found 86.5% vs 53.1% (2023–26, n = 1,300/1,300). Odds ratio (accepted) **5.68 [4.68, 6.89]**; OR(NAME) 1.00 [0.81, 1.22]. IPW × population NAME DiD +1.45 [−0.81, 3.71] | Not pre-registered; descriptive | **Supported** |
| SB5 | Camera-ready retitling: accepted papers retitle more than rejected ones | 23.8% vs 22.2%: **+1.5 pp [−3.2, 6.1]**. v1 posted during review: −2.7 [−7.8, 1.8]; v1 posted before the deadline: +8.6 [0.9, 16.1] | CI excludes 0 | **Not supported** |
| V7a | The findability gap is not specific to title search | n = 300 (150/150). Gap 0.36 (route A) vs 0.36 (route B); difference 0.00 [−0.06, 0.06]. Both routes share an abstract-similarity rule; near-miss bound on the gap 0.25 | Gap B CI > 0 and gap difference CI includes 0 | **Supported** (with the shared-rule caveat) |
| V7b | The title route does not select on title stability | Retitled: route A 24.4% (n = 160), route B 26.5% (n = 155); papers only route B finds: 4 of 6 retitled | Rule in `results.json` | **Partially supported** |
| G1 | Gate for D4-H4a: NAME neutrality (pooled 2024–26 G_total in [0.90, 1.11]) survives camera-ready uncertainty | G_total 1.021, 90% CI [1.001, 1.041]; audit-implied [0.948, 1.033]; **editing-corrected 90% CI [0.949, 1.031]**. 2024–26 pairs only: [0.926, 1.019]. Original audit only: [0.885, 1.069] (fails). G_dec: [0.988, 1.059] | Corrected 90% CI inside the margins | **Supported** |
| G2 | Gate for D4-H4b: L-title depletion (G_total < 1), audited as R24 or R26 | G_total 0.914, 90% CI [0.869, 0.963]; DiD −0.32 pp vs D\* −1.05; corrected 90% CI [0.834, 1.042]; Holm p 0.33 | Auditable, corrected 95% CI < 1, Holm p < 0.025 (3 H4b claims) | **Not supported** (not identified) |
| G2b | Gate for D4-H4b: O-union depletion (G_total < 1), audited without ALL-CAPS | G_total 0.908, 90% CI [0.850, 0.966]; DiD +1.09 pp vs D\* −0.73; corrected 90% CI [0.482, 0.978]; p 0.039, Holm 0.117 | As G2 | **Not supported** (fails even the uncorrected rule) |
| G3 | Abstract audit (extension): depletion of F24-or-F26 abstract words (G_total < 1) survives the audit | G_total 0.998, 90% CI [0.967, 1.029]; DiD +1.01 pp vs D\* −0.06; Holm p 0.33 | As G2 | **Not supported** (little pooled depletion to protect) |
| G4 | D4-H4c direction assumption: camera-ready polishing does not *lower* accepted papers' RARE21 rates | 2024–26 pairs (628/404): F24 DiD **+0.71 pp [−1.95, 3.36]**. 2023–26: +0.73 [−1.45, 2.90] | Sign of DiD (CI > 0 = supported) | **Partially supported** (sign as assumed, CI includes 0) |

**Headline.**
- **No title feature's decision-stage acceptance association survives the camera-ready audit once multiplicity is controlled.** This holds on the complete audit (803 accepted and 508 rejected pre-decision pairs, 4.0× the original 331).
  - Under the uncorrected interim rule, 2 associations would pass: O-union w/o ALL-CAPS (one-sided p 0.016), Compound (one-sided p 0.041). With Holm across 18 auditable features none passes; the smallest Holm-adjusted p is 0.29.
  - The set passing the uncorrected rule moves as records accrue (§4, freeze path). Sentence case passed it at 600, 1,000, 1,261 enlargement lines but not on the complete audit (margin −0.18 pp).
  - Outsider-casing depletion (O-union w/o ALL-CAPS, G_dec 0.882) comes closest. Editing runs the conservative way: accepted papers *gain* sentence case after v1 (net +0.4 vs −0.4 pp). This is a lead for the held-out test, not a finding.
- **NAME (the mainstream fashion).** The NAME acceptance association (G_dec 1.050) is not identified: DiD +1.48 pp [−0.63, 3.59] against D\* 2.92 pp.
  - The audit cannot rule out that post-decision renaming produces the NAME association. At the audit point estimate the submission-stage G_dec is 1.025 (NAME), 1.018 (strict) and 1.024 (loose), against an observed 1.050.
  - About 50% of the stored-title NAME excess is camera-ready at the point estimate (audit CI −21% to 124%). The CI spans both no editing effect and an editing effect larger than the whole association.
  - Accepted papers add NAME more often than rejected ones (add rate given v1-absent 3.7% vs 1.1%; 20 vs 4 adds). Drop rates are similar (6.2% vs 5.8%).
- **NAME neutrality (D4-H4a) is robust to editing.** The pooled 2024–26 G_total TOST passes on the complete audit (corrected 90% CI [0.949, 1.031]), on 2024–26 pairs only ([0.926, 1.019]) and on new records only. The corrected centre is 0.991, i.e. *below* the stored-title 1.021. A "peer review amplifies NAME" reading is therefore not supported. The original 331-pair audit alone did not pass ([0.885, 1.069]).
- **Findability.** Accepted papers have 5.7-fold higher odds of being found on arXiv (86.5% vs 53.1%). NAME does not predict findability (OR 1.00 [0.81, 1.22]). A title-free route gives the same gap, but both routes match on the latest arXiv abstract, so the routes are not independent checks.
- **No camera-ready retitling excess.** Accepted and rejected papers retitle at similar rates (+1.5 pp [−3.2, 6.1]). Where the v1 was posted during review, so that it is close to the submitted version, the difference is −2.7 pp [−7.8, 1.8]. An excess appears only where the v1 predates the deadline (+8.6 pp [0.9, 16.1]). Camera-ready edits would show up in both strata, so this most plausibly reflects how earlier drafts were revised before submission.
- **Channel limits.** Title typography (U+2011/U+2013), ALL-CAPS titles and the abstract em dash cannot be audited through arXiv at any sample size. D4's ALL-CAPS and typography depletion therefore stays unaudited.

---

## 1. Audit sample and differential findability (`found_rates.csv`, `findability_models.csv`, Fig. S1a)

**Sample.**
- **Original audit** (`src/arxiv_audit.py`, title route): 616 papers. 75 per year × decision cell for 2023–2026, plus 16 accepted papers from 2022.
- **Enlargement** (`audit_v2.py` phase 2): a fresh stratified random sample of 250 per cell for 2023–26, queried with the same title route. 2,000 records are complete; 4 lines are network-error rows superseded by a retry. Per cell: 250.
- **Primary audit:** usable pairs from both, 2023–26: **803 accepted / 508 rejected**. The 9 accepted 2022 pairs have no rejected counterpart; they enter only the `incl_2022` spec.

**Usable pair.** A paper is a usable pair when it is found on arXiv, has a v1 title, and its v1 predates the decision date of its conference year (`arxiv_audit.DECISION_DATE`).

| Sample | Decision | n | Found | Found rate [95% Wilson] | Usable pairs |
|---|---|---|---|---|---|
| Original (2022–26) | accepted | 316 | 280 | 88.6% [84.6, 91.7] | 206 (65.2%) |
| Original (2022–26) | rejected | 300 | 169 | 56.3% [50.7, 61.8] | 125 (41.7%) |
| Enlargement (2023–26) | accepted | 1,000 | 858 | 85.8% [83.5, 87.8] | 606 (60.6%) |
| Enlargement (2023–26) | rejected | 1,000 | 521 | 52.1% [49.0, 55.2] | 383 (38.3%) |
| Pooled 2023–26 | accepted | 1,300 | 1,124 | 86.5% [84.5, 88.2] | 803 (61.8%) |
| Pooled 2023–26 | rejected | 1,300 | 690 | 53.1% [50.4, 55.8] | 508 (39.1%) |

**Findability models** (logit with year FE, pooled 2023–26, n = 2,600):
- Found: odds ratio (accepted) **5.68 [4.68, 6.89]**. OR(NAME) 1.00 [0.81, 1.22] (p = 0.98). OR per log title word 0.75 [0.56, 0.99] (p = 0.043). Accepted × NAME interaction 1.19 [0.78, 1.83].
- Usable pair: OR(accepted) 2.55 [2.17, 2.99]; OR(NAME) 1.12 [0.94, 1.34] (p = 0.21).
- Pre-decision v1 given found: OR(accepted) 0.91 [0.73, 1.13].
- Original sample only (n = 600): OR(accepted) 6.16 [4.02, 9.44], OR(NAME) 1.37 [0.86, 2.20], usable-pair OR(NAME) 1.43 [0.96, 2.14] (p = 0.08). The interim text's "NAME does not predict findability" asserted a null on a CI reaching 2.2. The pooled sample now bounds the NAME effect near 1.
- The selection is therefore mostly "is the paper on arXiv at all", which differs strongly by decision. Longer titles are slightly less findable.
- IPW weights for the robustness specs: 1/P̂(usable | year, accepted, log title words, NAME), optionally times N_pop/n_sampled per year × decision. Normalised weights range 0.76–1.37 and 0.51–1.67 (with design weights). Kish effective n with design weights: 712 of 803 accepted, 449 of 508 rejected.
- **Title-clause admissions.** `arxiv_audit.find` also accepts a hit with title Jaccard ≥ 0.6 and a surname *substring* match when the abstract Jaccard is below 0.45. Among primary pairs this clause admits 9.1% of rejected but 1.6% of accepted pairs. The `abstract_matched` spec drops these pairs (§4). Surname matching cannot be redone at the whole-token level, because the caches do not store arXiv author lists. Dropping the clause covers that case.

## 2. Retitling between pre-decision v1 and stored title (`retitling.csv`, Fig. S1b)

**Measures** (on usable pairs):
- *Retitled*: the word sequence differs after lower-casing and stripping punctuation.
- *Major*: content-word Jaccard < 0.5.
- *Case/punctuation-only*: the raw string differs but the word sequence does not.

**v1 timing.** The v1 is classed *in review* when it was posted after the ICLR full-paper deadline (approximate public deadlines in `results.json` → `meta.submission_deadlines`), and *before deadline* otherwise.
- Primary pairs in review: accepted 54.3%, rejected 50.0% (Fisher p = 0.14).
- Median lag: +2.0 vs +0.5 days relative to the deadline.
- In the original 2023–26 pairs the mix differed: 49.2% vs 60.8% (p = 0.05).

| Sample | Years | Measure | Accepted | Rejected | Difference, Newcombe 95% CI |
|---|---|---|---|---|---|
| Primary | all | retitled | 191/803 = 23.8% | 113/508 = 22.2% | +1.5 [−3.2, 6.1] |
| Primary | all | major | 69/803 = 8.6% | 41/508 = 8.1% | +0.5 [−2.7, 3.5] |
| Primary | all | case/punct only | 71/803 = 8.8% | 46/508 = 9.1% | −0.2 [−3.5, 2.9] |
| Primary | 2024-26 | retitled | 145/628 = 23.1% | 85/404 = 21.0% | +2.0 [−3.2, 7.1] |
| Primary | 2023 | retitled | 46/175 = 26.3% | 28/104 = 26.9% | −0.6 [−11.6, 9.7] |
| v1 posted during review | all | retitled | 38/436 = 8.7% | 29/254 = 11.4% | −2.7 [−7.8, 1.8] |
| v1 posted during review | 2024-26 | retitled | 29/347 = 8.4% | 23/203 = 11.3% | −3.0 [−8.6, 2.0] |
| v1 posted before the deadline | all | retitled | 153/367 = 41.7% | 84/254 = 33.1% | +8.6 [0.9, 16.1] |
| Original audit (interim primary) | all | retitled | 61/206 = 29.6% | 29/125 = 23.2% | +6.4 [−3.6, 15.7] |
| Original audit (interim primary) | 2024-26 | retitled | 46/151 = 30.5% | 20/98 = 20.4% | +10.1 [−1.2, 20.4] |
| Original audit, v1 during review | all | retitled | 9/100 = 9.0% | 12/76 = 15.8% | −6.8 [−17.5, 2.9] |
| Original audit, v1 before the deadline | all | retitled | 52/106 = 49.1% | 17/49 = 34.7% | +14.4 [−2.4, 29.4] |

**Model and period contrast.**
- Logit with year FE: OR(accepted) = 1.09 [0.84, 1.42], p = 0.52.
- Period contrast: (acc − rej) in 2024–26 minus (acc − rej) in 2023 = +2.7 pp, bootstrap 95% CI [−9.5, 15.5]. The pre-period is 2023 only; the interim 2022–23 contrast mixed in accepted-only 2022 pairs.
- Title length does not change on average: Δwords +0.01 (accepted), +0.04 (rejected).

**Interpretation.**
- 22.2% of rejected papers already carry a different title on arXiv v1 than on OpenReview. This is the non-camera-ready noise floor. It is concentrated in v1s posted before the deadline (33.1%), against 11.4% for v1s posted during review.
- There is no camera-ready retitling excess. The in-review stratum, where v1 is close to the submitted version, gives −2.7 pp [−7.8, 1.8].
- The before-deadline stratum shows an accepted excess of +8.6 pp [0.9, 16.1], with a CI that excludes 0. Camera-ready retitling happens after the decision whatever the v1 date, so it should appear in both strata. If anything it should be harder to detect where the v1 was already retitled. The excess therefore most plausibly reflects pre-submission revision of earlier drafts that differs by eventual decision, e.g. papers resubmitted from another venue. This is an interpretation; the design cannot separate it from a camera-ready effect confined to early posters.
- The interim reading ("+6 pp, +10 pp in 2024–26 camera-ready excess") is withdrawn. In the original sample the excess sits in v1s posted before the deadline (+14.4 pp) and not in v1s posted during review (−6.8 pp). The original sample's timing mix also differed by decision.

## 3. Flip matrices with feature-present v1 denominators (T4.2: `T4_2_flip_matrices.csv`, `T4_2_flip_multiclass.csv`, Fig. S4)

**Features.** All features are computed with `features_v2.build` on both titles; the stored-title features reproduce `features_v2.parquet`. Two audited unions are new:
- *L-title words* = R24 or R26. This is the arXiv-measurable part of the L-title union, which also contains typography.
- *O-union w/o ALL-CAPS* = sentence case or question opener.

**Column definitions.**
- Cells show *v1-present: +adds/−drops*. Net = (adds − drops)/n. DiD = net(accepted) − net(rejected).
- **Primary CI:** Wald with a pseudo-flip variance floor (one pseudo-add and one pseudo-drop per arm).
- *Auditable:* "no (count)" means fewer than 10 v1-present titles in an arm; "no (channel)" means arXiv metadata cannot carry the feature.

| Feature | Accepted (n = 803) | Rejected (n = 508) | Net acc / rej (pp) | DiD (pp) [pseudo-flip 95% CI] | Plain Wald CI | Auditable |
|---|---|---|---|---|---|---|
| NAME (primary) | 256: +20/−16 | 155: +4/−9 | +0.5 / −1.0 | **+1.48 [−0.63, 3.59]** | [−0.54, 3.50] | yes |
| NAME strict | 245: +20/−15 | 152: +4/−11 | +0.6 / −1.4 | +2.00 [−0.16, 4.17] | [−0.08, 4.08] | yes |
| NAME loose | 276: +22/−14 | 173: +6/−9 | +1.0 / −0.6 | +1.59 [−0.59, 3.77] | [−0.51, 3.68] | yes |
| Compound | 395: +22/−24 | 239: +8/−13 | −0.2 / −1.0 | +0.74 [−1.76, 3.23] | [−1.69, 3.16] | yes |
| Phrase colon | 139: +12/−18 | 84: +7/−7 | −0.7 / +0.0 | −0.75 [−2.81, 1.32] | [−2.72, 1.22] | yes |
| Title Case | 755: +9/−15 | 475: +5/−17 | −0.7 / −2.4 | +1.62 [−0.63, 3.86] | [−0.55, 3.78] | yes |
| Mixed-case name | 167: +10/−11 | 96: +4/−13 | −0.1 / −1.8 | +1.65 [−0.39, 3.68] | [−0.29, 3.59] | yes |
| ALL-CAPS name | 66: +12/−7 | 46: +6/−3 | +0.6 / +0.6 | +0.03 [−1.66, 1.72] | [−1.54, 1.60] | yes |
| Word name | 22: +1/−1 | 11: +1/−0 | +0.0 / +0.2 | −0.20 [−1.02, 0.63] | [−0.71, 0.32] | yes |
| (ACR) name | 1: +0/−0 | 2: +1/−1 | +0.0 / +0.0 | +0.00 [−0.84, 0.84] | [−0.55, 0.55] | no (count) |
| Sentence case | 33: +13/−10 | 26: +5/−7 | +0.4 / −0.4 | +0.77 [−1.12, 2.65] | [−1.01, 2.54] | yes |
| ALL-CAPS title | 0: +2/−0 | 0: +10/−0 | +0.2 / +2.0 | −1.72 [−3.13, −0.31] | [−2.98, −0.46] | no (channel) |
| Mixed casing | 11: +3/−2 | 6: +4/−0 | +0.1 / +0.8 | −0.66 [−1.80, 0.48] | [−1.61, 0.28] | no (count) |
| Question opener | 17: +1/−2 | 14: +1/−1 | −0.1 / +0.0 | −0.12 [−1.07, 0.82] | [−0.82, 0.57] | yes |
| O-union | 46: +16/−10 | 39: +14/−7 | +0.7 / +1.4 | −0.63 [−2.88, 1.61] | [−2.79, 1.53] | no (channel) |
| LLM slot word | 23: +0/−4 | 5: +1/−0 | −0.5 / +0.2 | −0.69 [−1.59, 0.20] | [−1.32, −0.07] | no (count) |
| Any slot filled | 37: +4/−6 | 17: +1/−0 | −0.2 / +0.2 | −0.45 [−1.52, 0.63] | [−1.31, 0.42] | yes |
| R24 word | 31: +1/−3 | 17: +1/−1 | −0.2 / +0.0 | −0.25 [−1.22, 0.72] | [−0.98, 0.48] | yes |
| R26 word | 28: +3/−2 | 8: +2/−1 | +0.1 / +0.2 | −0.07 [−1.15, 1.00] | [−0.94, 0.79] | no (count) |
| Title typography | 0: +5/−0 | 0: +4/−0 | +0.6 / +0.8 | −0.16 [−1.30, 0.97] | [−1.11, 0.78] | no (channel) |
| L-title union | 59: +8/−5 | 25: +7/−2 | +0.4 / +1.0 | −0.61 [−2.19, 0.97] | [−2.06, 0.84] | no (channel) |
| 'using' | 19: +2/−3 | 25: +2/−2 | −0.1 / +0.0 | −0.12 [−1.27, 1.02] | [−1.07, 0.82] | yes |
| 'via' | 74: +12/−13 | 38: +6/−3 | −0.1 / +0.6 | −0.72 [−2.51, 1.08] | [−2.40, 0.97] | yes |
| LLM abbrev-only | 49: +9/−3 | 39: +2/−1 | +0.7 / +0.2 | +0.55 [−0.70, 1.80] | [−0.53, 1.63] | yes |
| L-title words (R24 or R26) | 59: +4/−5 | 25: +3/−2 | −0.1 / +0.2 | −0.32 [−1.62, 0.98] | [−1.45, 0.81] | yes |
| O-union w/o ALL-CAPS | 46: +14/−10 | 39: +5/−8 | +0.5 / −0.6 | +1.09 [−0.85, 3.03] | [−0.75, 2.92] | yes |

**Add and drop rates** (Fig. S4, Wilson CIs).
- NAME (primary): drop rate 6.2% vs 5.8%; add rate 3.7% vs 1.1% (accepted vs rejected).
- Compound: drop rate 6.1% vs 5.4%; add rate 5.4% vs 3.0% (accepted vs rejected).
- Title Case: drop rate 2.0% vs 3.6%; add rate 18.8% vs 15.2% (accepted vs rejected).
- Sentence case: drop rate 30.3% vs 26.9%; add rate 1.7% vs 1.0% (accepted vs rejected).
- 'via': drop rate 17.6% vs 7.9%; add rate 1.6% vs 1.3% (accepted vs rejected).
- Drop-rate CIs overlap across arms. The NAME DiD comes from adds: accepted papers add a coined name after v1 3.2× as often as rejected papers.

**Multi-class transitions** (primary; `T4_2_flip_multiclass.csv`):
- *Accepted.* Casing: title_case→sentence_case 11, sentence_case→title_case 9, title_case→all_caps 2, mixed→sentence_case 2, title_case→mixed 2, sentence_case→mixed 1. Name orthography: none→mixed_case 10, none→all_caps 9, mixed_case→none 8, all_caps→none 7, mixed_case→all_caps 3, none→word 1. Slot state: llm→none 4, none→neutral 4, neutral→none 2.
- *Rejected.* Casing: title_case→all_caps 9, sentence_case→title_case 5, title_case→sentence_case 5, title_case→mixed 3, sentence_case→mixed 1, sentence_case→all_caps 1. Name orthography: mixed_case→none 8, mixed_case→all_caps 4, none→mixed_case 2, none→all_caps 2, all_caps→mixed_case 1, all_caps→none 1. Slot state: none→llm 1.
- Every →all_caps transition (2 accepted, 10 rejected) is consistent with OpenReview form entry. arXiv titles are never ALL-CAPS, so these transitions say nothing about camera-ready editing.

**Examples of camera-ready NAME additions** (original audit, 2026): "Self-Augmented Visual Contrastive Decoding" → "Self-Aug: Query and Entropy Adaptive Decoding …"; "Scaled Inverse Graphics: …" → "Fused-Planes: …"; "Shortening the Trajectories: …" → "GAGA: …". Drops: "SeerAttention-R: …" → "Sparse Attention Adaptation for Long Reasoning"; "RSRM: …" → "Reinforcement Symbolic Regression Machine".

## 4. Tipping points and the decision-stage bound (T4.2: `T4_2_tipping_points.csv`, `T4_2_identification_by_spec.csv`, `T4_2_identified_anywhere.csv`, `T4_2_freeze_path.csv`, `T4_2_tipping_by_year.csv`, Fig. S2)

**Prevalences.** Universe prevalences are pooled over 2024–26 and year-standardised to s0 sizes, as in D4. The audit DiD is the primary 2023–26 estimate.

**Auditable features** (primary audit). p = one-sided identification p-value; Holm across the 18 auditable features.

| Feature | P₂ → P₃ | G_dec [95%] | DiD [95%] (pp) | D\* (pp) | p | Holm p | Uncorrected rule | G_dec at D̂ | Audit-implied G_dec |
|---|---|---|---|---|---|---|---|---|---|
| NAME (primary) | 34.6 → 36.4% | 1.050 [1.027, 1.073] | +1.48 [−0.63, 3.59] | +2.92 | 0.127 | 1.00 | no | 1.025 | [0.988, 1.061] |
| NAME strict | 33.6 → 35.4% | 1.053 [1.031, 1.077] | +2.00 [−0.16, 4.17] | +2.99 | 0.220 | 1.00 | no | 1.018 | [0.978, 1.056] |
| NAME loose | 36.9 → 38.7% | 1.050 [1.028, 1.071] | +1.59 [−0.59, 3.77] | +3.06 | 0.127 | 1.00 | no | 1.024 | [0.988, 1.059] |
| Compound | 52.3 → 54.3% | 1.037 [1.021, 1.051] | +0.74 [−1.76, 3.23] | +3.24 | 0.041 | 0.69 | passes | 1.029 | [1.000, 1.056] |
| Phrase colon | 17.7 → 17.9% | 1.011 [0.975, 1.045] | −0.75 [−2.81, 1.32] | +0.32 | 0.182 | 1.00 | no | 1.036 | [0.966, 1.099] |
| Title Case | 93.0 → 94.5% | 1.017 [1.012, 1.021] | +1.62 [−0.63, 3.86] | +2.59 | 0.206 | 1.00 | no | 1.006 | [0.992, 1.021] |
| Mixed-case name | 22.6 → 24.6% | 1.087 [1.055, 1.118] | +1.65 [−0.39, 3.68] | +3.29 | 0.086 | 1.00 | no | 1.045 | [0.989, 1.096] |
| ALL-CAPS name | 10.2 → 9.9% | 0.966 [0.919, 1.012] | +0.03 [−1.66, 1.72] | −0.59 | 0.259 | 1.00 | no | 0.964 | [0.855, 1.059] |
| Word name | 1.6 → 1.8% | 1.103 [0.972, 1.229] | −0.20 [−1.02, 0.63] | +0.27 | 0.150 | 1.00 | no | 1.168 | [0.843, 1.385] |
| Sentence case | 4.2 → 3.7% | 0.868 [0.797, 0.942] | +0.77 [−1.12, 2.65] | −0.94 | 0.044 | 0.70 | no | 0.740 | [0.320, 1.023] |
| Question opener | 1.7 → 1.6% | 0.911 [0.791, 1.030] | −0.12 [−1.07, 0.82] | −0.26 | 0.397 | 1.00 | no | 0.955 | [0.542, 1.223] |
| Any slot filled | 5.1 → 4.9% | 0.961 [0.896, 1.030] | −0.45 [−1.52, 0.63] | −0.34 | 0.568 | 1.00 | no | 1.012 | [0.882, 1.122] |
| R24 word | 4.8 → 4.3% | 0.896 [0.830, 0.968] | −0.25 [−1.22, 0.72] | −0.83 | 0.156 | 1.00 | no | 0.929 | [0.792, 1.045] |
| 'using' | 2.0 → 1.4% | 0.700 [0.597, 0.795] | −0.12 [−1.27, 1.02] | −1.00 | 0.075 | 1.00 | no | 0.743 | [0.239, 1.063] |
| 'via' | 10.6 → 11.1% | 1.048 [1.001, 1.095] | −0.72 [−2.51, 1.08] | +0.85 | 0.062 | 0.92 | no | 1.086 | [0.986, 1.173] |
| LLM abbrev-only | 9.2 → 9.5% | 1.036 [0.987, 1.088] | +0.55 [−0.70, 1.80] | +0.55 | 0.499 | 1.00 | no | 1.000 | [0.912, 1.079] |
| L-title words (R24 or R26) | 8.1 → 7.9% | 0.983 [0.929, 1.038] | −0.32 [−1.62, 0.98] | −0.23 | 0.548 | 1.00 | no | 1.007 | [0.906, 1.095] |
| O-union w/o ALL-CAPS | 5.8 → 5.1% | 0.882 [0.818, 0.945] | +1.09 [−0.85, 3.03] | −1.14 | 0.016 | 0.29 | passes | 0.750 | [0.452, 0.972] |

**Unauditable features.** These cannot enter a gate.

| Feature | Reason | G_dec [95%] | D\* (pp) | Audit CI (pp) | v1-present (acc/rej) |
|---|---|---|---|---|---|
| (ACR) name | fewer than 10 v1-present in an arm | 0.785 [0.416, 1.182] | −0.06 | [−0.84, 0.84] | 1/2 |
| ALL-CAPS title | arXiv titles are never ALL-CAPS | 0.435 [0.320, 0.559] | −1.04 | [−3.13, −0.31] | 0/0 |
| Mixed casing | fewer than 10 v1-present in an arm | 0.727 [0.608, 0.849] | −0.63 | [−1.80, 0.48] | 11/6 |
| O-union | contains ALL-CAPS title (channel-unauditable) | 0.812 [0.757, 0.869] | −2.15 | [−2.88, 1.61] | 46/39 |
| LLM slot word | fewer than 10 v1-present in an arm | 0.984 [0.901, 1.074] | −0.08 | [−1.59, 0.20] | 23/5 |
| R26 word | fewer than 10 v1-present in an arm | 1.093 [1.005, 1.178] | +0.54 | [−1.15, 1.00] | 28/8 |
| Title typography | arXiv titles never carry U+2011 / U+2013 typography | 0.975 [0.774, 1.173] | −0.03 | [−1.30, 0.97] | 0/0 |
| L-title union | contains title typography (channel-unauditable) | 0.980 [0.930, 1.032] | −0.29 | [−2.19, 0.97] | 59/25 |

**Notes on individual features.**
- **ALL-CAPS title.** The net-flip DiD (−1.72 pp) comes from 2 accepted and 10 rejected additions with no v1-present titles. arXiv titles are never ALL-CAPS, so the "DiD" is just the accepted-vs-rejected gap in stored ALL-CAPS prevalence among pairs. That gap is the association under test, not a measure of editing. The interim note that this DiD "exceeds the whole tipping point" is withdrawn. ALL-CAPS title is unauditable by channel; D4's decision-stage ALL-CAPS depletion cannot be separated from editing or form entry.
- **Sentence case** became auditable as the audit grew (v1-present 33/26). Editing runs the conservative way: accepted papers gain sentence case (net +0.4 pp vs −0.4 pp). The DiD lower bound is −1.12 pp against D\* = −0.94 pp: not identified (margin −0.18 pp), although it was identified at 600–1,261 enlargement lines. With the tipping point's own sampling error, p = 0.044 and Holm gives 0.70.
- **'using'** reached 19/25 v1-present titles and is now auditable; it is not identified. The PLAN example ("n = 4 accepted v1 titles") reproduces on the original 331 pairs.

**Robustness of the NAME bound** (D\* = 2.92 pp throughout):

| Audit specification | n acc / rej | DiD (pp) [95%] | p | Identified |
|---|---|---|---|---|
| Primary: original + enlargement, 2023–26 | 803 / 508 | +1.48 [−0.63, 3.59] | 0.127 | no |
| Including the 9 accepted-only 2022 pairs | 812 / 508 | +1.48 [−0.62, 3.58] | 0.125 | no |
| Year-standardised arms (within-year contrasts) | 803 / 508 | +1.45 [−0.67, 3.57] | 0.122 | no |
| 2024–26 pairs only | 628 / 404 | +2.35 [−0.10, 4.80] | 0.344 | no |
| Original audit only (interim primary) | 206 / 125 | +2.09 [−3.16, 7.33] | 0.381 | no |
| Enlargement records only (out of sample) | 606 / 383 | +1.28 [−1.05, 3.61] | 0.113 | no |
| Enlargement records only, 2024–26 | 477 / 306 | +2.15 [−0.57, 4.86] | 0.307 | no |
| IPW for findability | 803 / 508 | +1.45 [−0.69, 3.59] | 0.124 | no |
| IPW × population design weights | 803 / 508 | +1.45 [−0.81, 3.71] | 0.134 | no |
| Abstract-matched pairs only (drops title-clause admissions) | 790 / 462 | +1.59 [−0.65, 3.82] | 0.156 | no |
| v1 posted during review | 436 / 254 | +2.26 [−0.03, 4.56] | 0.313 | no |
| v1 posted before the deadline | 367 / 254 | +0.67 [−3.23, 4.56] | 0.141 | no |
| Timing-standardised arms (year × v1 timing) | 803 / 508 | +1.55 [−0.59, 3.69] | 0.141 | no |
| Union with route-B-only pairs (300-paper V7 subsample only) | 804 / 513 | +1.28 [−0.86, 3.41] | 0.098 | no |
| Plain Wald / bootstrap CI (primary pairs) | 803 / 508 | [−0.54, 3.50] / [−0.53, 3.44] | | no / no |

NAME G_dec is identified in no specification under any CI type.

**Where any feature is identified under the uncorrected rule** (`T4_2_identified_anywhere.csv`, G_dec, 14 specs × 3 CI types). No identification survives Holm in any spec.

| Feature | Specs identified (pseudo-flip CI) | Additional specs (Wald or bootstrap only) | Smallest margin (pp) |
|---|---|---|---|
| Compound | 5: abstract_matched, incl_2022, ipw_find, primary, union_route_v7sub | year_std | 0.01 |
| Word name | 0: – | incl_2022, ipw_find, primary, timing_std, union_route_v7sub, year_std | 0.02 |
| O-union w/o ALL-CAPS | 10: abstract_matched, incl_2022, ipw_find, ipw_find_pop, original_only, primary, timing_std, union_route_v7sub, v1_before_deadline, year_std | post_2024_26 | 0.02 |
| 'using' | 0: – | timing_std, year_std | 0.02 |
| 'via' | 4: ipw_find_pop, new_records_2024_26, new_records_only, post_2024_26 | union_route_v7sub | 0.03 |
| Sentence case | 0: – | abstract_matched | 0.07 |

Notes:
- The interim text claimed "no feature is identified in any specification, under any CI type". That was already false at the interim freeze: in the `ipw_find_pop` spec the O-union was identified under the Wald and bootstrap CIs.
- Word-name identifications occur under the bootstrap only. Its bootstrap DiD is nearly degenerate, because flips are rare.
- 'via' (a control word) is identified only in ipw_find_pop, new_records_2024_26, new_records_only, post_2024_26. In the primary its upper CI (+1.08 pp) exceeds D\* (+0.85 pp), and its observed G_dec CI lower bound is 1.001.

**Freeze path** (`T4_2_freeze_path.csv`): the same primary definition, re-run on the original 2023–26 pairs plus the first N enlargement lines.

| Enlargement lines | Pairs acc/rej | Auditable features | NAME DiD [95%] | NAME G_total corrected 90% CI | Pass uncorrected rule | Pass Holm | Smallest p |
|---|---|---|---|---|---|---|---|
| 254 | 271/175 | 10 | +1.31 [−2.92, 5.53] | [0.919, 1.067] | O-union w/o ALL-CAPS | none | 0.015 (O-union w/o ALL-CAPS) |
| 600 | 374/236 | 12 | +0.16 [−3.28, 3.59] | [0.956, 1.077] | Compound, Sentence case, O-union w/o ALL-CAPS | none | 0.005 (O-union w/o ALL-CAPS) |
| 1,000 | 510/311 | 15 | +1.16 [−1.66, 3.98] | [0.945, 1.048] | Compound, Sentence case, O-union w/o ALL-CAPS | none | 0.003 (O-union w/o ALL-CAPS) |
| 1,261 | 589/367 | 17 | +1.50 [−0.99, 3.98] | [0.943, 1.036] | Compound, Sentence case, O-union w/o ALL-CAPS | none | 0.010 (O-union w/o ALL-CAPS) |
| 2,004 | 803/508 | 18 | +1.48 [−0.63, 3.59] | [0.949, 1.031] | Compound, O-union w/o ALL-CAPS | none | 0.016 (O-union w/o ALL-CAPS) |

- Under the uncorrected rule, the set of passing features changes as records accrue. The interim "0 of 24 pass" (uncorrected rule, original + 254 records) therefore was not a stable verdict; only the multiplicity-controlled gate gives the same answer at every freeze.
- Under Holm, nothing passes at any freeze. NAME is never identified. The H4a G_total TOST passes at every freeze with the enlargement.

**Per-year bounds** (`T4_2_tipping_by_year.csv`).
- Every year 2023–2026 has its own audit: 175–220 accepted and 104–152 rejected pairs. NAME CI half-widths are 3.9–5.8 pp. Example: NAME in 2024, DiD +5.0 [−0.8, 10.8] vs D\* 2.2 pp.
- Identified per year under the uncorrected rule: NAME loose in 2023 (margin 0.086 pp). These are 104 year × feature tests without multiplicity control, so isolated identifications are not interpreted.
- H4a's per-year claims for 2018–2022 have no audit. 2022 has 9 accepted pairs and no rejected ones.

**Comparison with the PLAN pilot.**
- The PLAN's 1.8 pp tipping point is P₃ − P₂ = 1.74 pp. It omits the 1/(1 − a₂) factor: camera-ready edits also shift P(f | reviewed), because accepted papers are part of the reviewed set. With the factor, D\* = 2.92 pp.
- The year-standardised pooling is the same in both. The interim text attributed the difference to pooling, which was wrong.
- The original-audit DiD and SE reproduce the pilot: +2.09 pp vs +2.1 (Wald se 2.37 vs 2.4).

**How large an audit would identify NAME G_dec?** The primary pseudo-flip se is 1.08 pp.
- If the true DiD were 0, the CI would clear D\* with 50% probability at 0.52× the current pairs and with 80% probability at 1.07× (≈ 1,405 pairs). The complete audit therefore has more than 50% but less than 80% power in that case.
- For comparison, the interim plan ("the full enlargement would suffice") quoted only the 50% multiplier (3.2× of 331 pairs) and assumed a 54% usable rate. The enlargement's realised usable rate was 49.5%.
- If the true DiD equals the observed +1.48 pp (1.43 pp below D\*), the 95% CI clears D\* only at about 2.2× the current pairs (≈ 2,844 pairs, with 50% probability).
- The interim statement "no audit size would identify NAME G_dec" was false; the point estimate was below D\* then too.

## 5. Gate for D4 claims (PLAN §4; `gate.csv`)

**H4a (NAME neutrality, pooled 2024–26).** The rule is a TOST on the editing-corrected 90% CI within [0.90, 1.11].

| Audit | G_total corrected 90% CI | Passes | G_dec corrected 90% CI | Passes |
|---|---|---|---|---|
| Primary: original + enlargement, 2023–26 | [0.949, 1.031] | yes | [0.988, 1.059] | yes |
| 2024–26 pairs only | [0.926, 1.019] | yes | [0.967, 1.048] | yes |
| Enlargement records only (out of sample) | [0.950, 1.038] | yes | [0.989, 1.065] | yes |
| v1 posted during review | [0.930, 1.018] | yes | [0.971, 1.048] | yes |
| Original audit only (interim primary) | [0.885, 1.069] | no | [0.930, 1.089] | yes |

- G_total is more editing-sensitive than G_dec, because accepted papers are a smaller share of s0 (a₀ = 0.294) than of s2 (a₂ = 0.403).
- The corrected point estimate (G_total at D̂) is 0.991. The editing-corrected submission-stage NAME ratio is therefore about 0.97–0.99 across the primary and 2024–26 audits, not the stored-title 1.021.
- The literal §4 rule ("tipping point exceeds the audit upper CI") is written for association claims. For NAME G_total it is not met (D\*_total 1.04 pp vs upper CI 3.59 pp). The H4a equivalence claim is gated by the corrected-CI TOST instead (Deviation 11).

**H4b (depletion of LLM and outsider markers).** One family of three claims, Holm at one-sided 0.025.
- L-title, audited as R24 or R26 (G2): G_total 0.914; DiD −0.32 pp vs D\* −1.05; corrected 90% CI [0.834, 1.042]; p 0.165, Holm 0.331; uncorrected rule fails; **does not pass**.
- O-union, audited without ALL-CAPS (G2b): G_total 0.908; DiD +1.09 pp vs D\* −0.73; corrected 90% CI [0.482, 0.978]; p 0.039, Holm 0.117; uncorrected rule fails; **does not pass**.
- F24-or-F26 abstract words (G3): G_total 0.998; DiD +1.01 pp vs D\* −0.06; corrected 90% CI [0.857, 1.050]; p 0.240, Holm 0.331; uncorrected rule fails; **does not pass**.
- The original L-title union (with typography) and O-union (with ALL-CAPS) are channel-unauditable and listed in `gate.csv` for transparency only.
- H4b's audit-free component, G_desk × G_exit on submission-stage text, is unaffected.

**Acceptance associations.** 0 of 26 title features pass. Diachronic and NA-pool results do not depend on the audit (PLAN §4).

## 6. Abstract audit (extension; `abstract_audit.csv`)

**Design.**
- arXiv v1 abstracts come from two sources:
  - the 330 original pre-decision pairs, re-fetched by `audit_v2.py` (one 503 error is not retried, to keep the file the prereg froze unchanged);
  - every enlargement record, which already carries its v1 abstract.
- Re-fetched v1 titles match the original audit for 100% of pairs.
- **Primary sample: 2024–26 pairs**, the H4b/H4c scope. Sensitivities: 2023–26, original only, enlargement only.
- Content-word Jaccard between v1 and stored abstract:
  - pooled 2023–26: accepted 0.82 vs rejected 0.83, difference −0.008 [−0.032, 0.018];
  - original pairs: 0.77 vs 0.83, −0.056 [−0.113, 0.005].
  - Accepted abstracts do not change measurably more than rejected ones.

| Marker | Sample | Accepted: v1-present, +adds/−drops, n | Rejected | DiD (pp) [pseudo-flip 95%] | Auditable |
|---|---|---|---|---|---|
| F24 (RARE21 >= 1) | 2024–26 | 81, +18/−12, 628 | 48, +8/−7, 404 | +0.71 [−1.95, 3.36] | yes |
| F24 (RARE21 >= 1) | 2023–26 | 87, +21/−12, 803 | 50, +9/−7, 507 | +0.73 [−1.45, 2.90] | yes |
| F24 (RARE21 >= 1) | original | 20, +8/−4, 206 | 13, +1/−3, 124 | +3.55 [−1.62, 8.73] | yes |
| RARE21 >= 2 | 2024–26 | 12, +2/−2, 628 | 11, +1/−1, 404 | +0.00 [−1.23, 1.23] | yes |
| F26 words | 2024–26 | 41, +8/−2, 628 | 23, +2/−0, 404 | +0.46 [−0.98, 1.90] | yes |
| Abstract em dash | 2024–26 | 0, +62/−0, 628 | 0, +31/−0, 404 | +2.20 [−1.37, 5.77] | no (channel) |
| F24 or F26 words | 2024–26 | 118, +25/−14, 628 | 70, +9/−6, 404 | +1.01 [−1.80, 3.82] | yes |
| F24 or F26 words | 2023–26 | 127, +28/−14, 803 | 74, +10/−6, 507 | +0.95 [−1.34, 3.25] | yes |
| F24 or F26 words | original | 25, +12/−4, 206 | 16, +2/−2, 124 | +3.88 [−1.61, 9.38] | yes |

**Em dash.** No arXiv v1 abstract contains an em dash (0 of 1,709). arXiv writes TeX `--`/`---` or a plain hyphen, e.g. "interactions--such as" vs the stored "interactions—such as".
- The 62 + 31 em-dash "adds" are therefore channel artefacts.
- The em dash, and by the same mechanism U+2011/en-dash typography in titles (0 of 3,659 arXiv titles), **cannot be audited through arXiv**.

**Tipping points** (pooled 2024–26, year-standardised):
- F24: G_dec 0.989, G_total 0.963 [0.916, 1.007]. D\*_total −0.67 pp vs DiD +0.71 [−1.95, 3.36]. Not identified.
- F24-or-F26 words: G_total 0.998. Not identified.

**Readings.**
1. On stored abstracts, the accepted/all *prevalence* ratio for RARE21 is close to 1 (0.96 pooled 2024–26).
   - D4's H4c contrast is larger because the Kobak bound subtracts a pre-2024 baseline from both sets.
   - A prevalence-scale depletion of a few percent cannot be made audit-robust: the tipping points are below 1 pp, against an audit band of about ±2.7 pp.
2. The abstract-editing DiD is **positive but small and not significant**: +0.71 pp [−1.95, 3.36] on 2024–26 pairs, and +0.73 pp on 2023–26 pairs.
   - Both arms gain F24 words between v1 and the stored abstract (accepted +0.96 pp, rejected +0.25 pp).
   - The interim estimate fell from +3.55 pp (330 original pairs) to +0.71 pp.
   - The sign matches H4c's assumption, so the accepted-only understatement is not reversed by editing (G4 partially supported).
   - The interim sentence calling the accepted additions "consistent with LLM-assisted camera-ready polishing" is withdrawn.

## 7. V7: retrieval-route validation (`route_validation.csv`, `route_pairs.csv`, Fig. S3)

**Design.**
- Sample: a random subsample of the original audit, 150 accepted + 150 rejected (seed 20261011). Complete: n = 300.
- **Route B** never uses the title. It queries `au:<first-author surname> AND abs:w1 AND abs:w2 AND abs:w3`.
  - The w's are the three abstract words with the lowest document frequency among all exported ICLR abstracts, excluding words in the stored title. A fallback query uses the surname and the next two words.
  - Acceptance tiers: A, abstract Jaccard ≥ 0.45; B, surname match and Jaccard ≥ 0.30; C, surname match, Jaccard ≥ 0.15, plausible v1 year and a 3-word query.

| | Accepted (n = 150) | Rejected (n = 150) | All (n = 300) |
|---|---|---|---|
| Found, route A (title) | 88.7% [82.6, 92.8] | 52.7% [44.7, 60.5] | 70.7% |
| Found, route B (surname + abstract) | 84.7% [78.0, 89.6] | 48.7% [40.8, 56.6] | 66.7% |
| Found, route B strict tiers | 84.7% [78.0, 89.6] | 47.3% [39.5, 55.3] | 66.0% |
| Found, A or B | 89.3% [83.4, 93.3] | 56.0% [48.0, 63.7] | 72.7% |
| A only / B only / neither | 7 / 1 / 16 | 11 / 5 / 66 | 18 / 6 / 82 (McNemar p = 0.023) |
| Same arXiv id when both found | 100.0% | 98.5% | 99.5% |
| v1 retitled vs stored, route A | 27/102 = 26.5% | 12/58 = 20.7% | 24.4% |
| v1 retitled vs stored, route B | 27/98 = 27.6% | 14/57 = 24.6% | 26.5% |
| Latest arXiv title ≠ stored, route A | 7/133 = 5.3% | 20/79 = 25.3% | 12.7% |
| Latest arXiv title ≠ stored, route B | 7/127 = 5.5% | 21/73 = 28.8% | 14.0% |

**Findability (V7a).**
- The accepted–rejected findability gap is the same on both routes: 0.36; difference 0.00 [−0.06, 0.06]. So the gap is not specific to title search.
- **The routes are not independent.** Both accept a hit only if the *latest* arXiv abstract resembles the stored abstract. Route A's third attempt is also already title-free (surname + abstract words). Rejected papers rewritten after rejection can be missed by both routes.
- Near-miss bound (Jaccard ≥ 0.10): among papers neither route found, 1 accepted and 14 rejected have a same-surname, date-plausible candidate below the acceptance tiers. Counting them as found moves the rejected found rate from 56.0% to 65.3%, and the gap from 0.33 to 0.25.
- Near-miss bound (Jaccard ≥ 0.05): among papers neither route found, 5 accepted and 28 rejected have a same-surname, date-plausible candidate below the acceptance tiers. Counting them as found moves the rejected found rate from 56.0% to 74.7%, and the gap from 0.33 to 0.18.
- A substantial gap remains under either bound. Differential findability is consistent with arXiv posting differing by decision, plus some censoring of heavily revised rejected papers.

**Title stability (V7b).**
- Retitling rates differ by 2.1 pp between routes (24.4% vs 26.5%; no CI is computed because the routes share most papers).
- The papers found only by route B are disproportionately retitled: 4 of 6.
- Adding the route-B-only pairs, which exist only for the 300-paper subsample, moves the NAME DiD from +1.48 to +1.28 pp. On the interim 331 pairs the same 6 pairs moved it by 0.83 pp; a full-sample union could move it more.
- Dropping title-clause admissions (abstract-matched pairs only) gives a NAME DiD of +1.59 [−0.65, 3.82] pp.
- Rejected papers' *latest* arXiv titles differ from the stored title in 25.3% of cases (accepted: 5.3%). This is retitling after rejection.

## 8. Enlargement and freeze (`audit_v2.py` phase 2)

- **Status:** complete. 2,000 of 2,000 sampled papers queried without a network error (2,004 lines; errored rows were retried and the retry superseded them).
- Throughput is about 375–430 papers per hour. Each paper needs 2–4 requests at ≥ 3.2 s apart, so the PLAN's "1k papers/hour" is not achievable within the rate limit.
- **Findability replicates out of sample:** found 85.8% [83.5, 87.8] accepted vs 52.1% [49.0, 55.2] rejected.
- **Pairs:** 989 new usable pairs; primary 1,311 (803/508).
- **Reproducing the freeze:** `python -m analyses.snapshot_final --enlarge-n 2004`, then check `meta.audit_freeze.enlargement.sha256_of_lines_used`.
- **Consumers of this freeze** (aligned in the integration passes, after this work package's own audit):
  - `d4_bias_atlas.py` builds D4's flip tables on this freeze's primary pairs (`audit_pairs.csv`) with the same auditability rule and pseudo-flip CI, and asserts that they equal `T4_2_flip_matrices.csv`. Before the integration pass it used the original audit only.
  - `prereg_confirm` (pre-registration revision 2) re-froze its gate audit on this freeze (same line count, SHA-256 checked) and adopted the multiplicity-controlled gate. Revision 1 had frozen the original audit plus 1,261 enlargement lines and gated with the uncorrected rule in `snapshot_bounds.tipping_table`. Revision 3 keeps this audit unchanged.
  - `d3_slots.py` (D3's camera-ready audit of LLM slot words) reads this freeze's enlargement lines (same line count, SHA-256 checked) with D3's own pairing rule (2022-26). Until the second integration pass it read a pre-freeze pin of 1,620 lines (1,127 pairs; LLM-slot v1 titles 22 accepted / 4 rejected). On this freeze the slot words stay unauditable (SB3: 23 / 5 v1-present; rejected arm below 10).
  - At 1,261 lines the uncorrected rule passes Compound, Sentence case, O-union w/o ALL-CAPS (see the freeze path); that is why the prereg gate was revised before any held-out data were requested.

---

## Deviations from PLAN.md (logged)

1. **CI for the net-flip DiD.** The PLAN does not fix the CI type. The primary CI is Wald with a pseudo-flip variance floor, because plain Wald SEs are 0 for zero-flip arms. Plain Wald and a stratified bootstrap (2,000 replicates, year × decision strata) are reported. Under the Holm gate no verdict changes between them. Under the uncorrected rule the identified set differs by CI type and spec (§4).
2. **Auditability rule.** ≥ 10 v1-present titles in *both* arms, plus arXiv-channel measurability. The channel criterion was added after the interim run: arXiv titles were never ALL-CAPS or Unicode-typographic (0 of 3,659), and v1 abstracts never contained an em dash.
3. **Tipping point regenerated at 2.92 pp** against the pilot's 1.8 pp. The pilot omitted the 1/(1 − a₂) factor (§4).
4. **V7 retrieval key.**
   - PLAN: "surname plus the first abstract sentence". Phrase search on a full sentence fails after any rewording, so three corpus-rare abstract words are used, excluding title words, with a 2-word fallback.
   - Tier C was added after a pilot query; its false-positive rate in validation was 1 of 2, so strict-tier results are reported.
   - Route B uses an ASCII-transliterating surname helper. The enlargement keeps the original helper so that it can be pooled with the original audit.
5. **Extension: arXiv v1 abstracts** audit abstract markers (F24, F26, em dash). This is not in the PLAN.
6. **Enlargement.** 250 per year × decision cell for 2023–26, interleaved queue, written to a separate file. The PLAN's rate is infeasible under the 3.2 s rate limit.
7. **IPW models** are fitted on 2023–26, because 2022 has accepted papers only.
8. **G intervals clip D** to the feasible range [P₃ − 1, P₃].
9. **Per-year tipping points** exist for 2023–2026 only. 2018–2022 have no audit.
10. **Note for D4.** `d4_filter/audit_pairs.csv` reads `arxiv_id` with `pd.read_json`, which parses ids as floats. This does not affect D4's features.
11. **Gate operationalisation** (set after the interim run, in response to the audit).
    - For association claims, PLAN §4 ("tipping point exceeds the audit's upper CI") is applied with the tipping point's sampling error and Holm across auditable features (PLAN §0), plus an editing-corrected 95% CI that excludes 1.
    - For the H4a equivalence claim, the §4 rule is replaced by a TOST on the editing-corrected 90% CI. Under the literal rule NAME G_total is not identified.
    - The G4 four-way rule and the V7b rule were set after seeing the pilot.
    - The interim G1 "partially supported when only the enlarged audit passes" rule is dropped, because the enlarged audit is now the primary.
12. **Primary audit** = original + complete enlargement, 2023–26 (interim: original only, 2022–26). The PLAN asked for the enlargement before confirmation; dropping the 9 accepted-only 2022 pairs follows the code audit. Retitling's period contrast uses 2023 as the pre-period.
13. **Audited unions.** L-title is audited as R24 or R26, and the O-union as sentence case or question opener. The PLAN's unions contain channel-unauditable components.
14. **Abstract audit primary sample** is 2024–26 pairs (the H4b/H4c scope), with 2023–26 as a sensitivity.
15. **v1 timing strata** use approximate public full-paper deadlines.
16. **Code.** The fixes live in `snapshot_final.py`, because `snapshot_bounds.py` is hashed by the prereg bundle.

## Limitations

- **Sample size.** Even with 803/508 pairs, the NAME CI (±2.1 pp) is wider than the gap between D̂ and D\*. "Not identified" is a statement about the audit, not evidence that editing explains the association.
- **arXiv v1 is not the submitted OpenReview title.** 47% of v1s predate the submission deadline. These earlier drafts retitle 2.9–4.8× as often as in-review v1s. The DiD removes this drift only if it is the same in both arms. The timing mix is similar in the primary sample, and neither the in-review nor the timing-standardised spec identifies NAME (§4). Fetching the last pre-decision arXiv version instead of v1 would remove most of this noise; it was not done.
- **Selection.** Findability IPW corrects for year, decision, title length and NAME only. Unobserved differences between arXiv-posting and non-posting rejected papers remain. So does censoring of heavily revised rejected papers by the abstract-similarity matching rule (near-miss bound, §7).
- **Channel.** Typography, ALL-CAPS titles and the em dash cannot be audited through arXiv at any sample size.
- **Abstract audit caveats.** The arXiv v1 abstract may differ from the OpenReview submission abstract for reasons common to both arms.
- **Gate verdicts depend on 2024–26 pooling.** Per-year bounds are wide.

## Interface for D4 (WP8) and the prereg

- `T4_2_flip_matrices.csv`, rows `spec == 'primary'`: the canonical net-flip DiD per feature. Columns `did`, `did_lo`, `did_hi` (pseudo-flip 95%), `did_lo_wald`/`did_hi_wald`, `did_lo_boot`/`did_hi_boot`, `auditable` (channel + count), `auditable_count`, `channel_ok`.
- `T4_2_tipping_points.csv`: G_dec and G_total, tipping points and their SEs, identification p-values (`p_ident_*`, `p_holm_dec`), gate flags (`passes_holm_dec`, `passes_uncorrected_dec`), editing shares, audit-size multipliers, audit-implied and corrected intervals.
- `gate.csv`: gate verdicts for H4a (by audit spec), H4b and every acceptance association.
- `results.json` → `meta.audit_freeze`: the line count and SHA-256 to pass as `--enlarge-n` for any consumer.

## Files

- **Scripts:** `src/analyses/snapshot_final.py`, `src/analyses/snapshot_final_report.py`, `src/analyses/snapshot_bounds.py` (unchanged), `src/analyses/audit_v2.py`.
- **Caches** (written by `audit_v2.py`): `cache/arxiv_audit_route.jsonl`, `cache/arxiv_audit_v1abs.jsonl`, `cache/arxiv_audit_enlarge.jsonl`; background log `outputs/snapshot/audit_v2.log`.
- **Tables:** `audit_pairs.csv` (primary pairs), `found_rates.csv`, `findability_models.csv`, `retitling.csv`, `T4_2_flip_matrices.csv`, `T4_2_flip_multiclass.csv`, `T4_2_tipping_points.csv`, `T4_2_tipping_by_year.csv`, `T4_2_identification_by_spec.csv`, `T4_2_identified_anywhere.csv`, `T4_2_freeze_path.csv`, `abstract_audit.csv`, `gate.csv`, `route_validation.csv`, `route_pairs.csv`, `results.json`, `snapshot_final.log`.
- **Figures** (each as PDF + PNG + CSV):
  - **Fig. S1** `fig_S1_findability_retitling`: findability and retitling by year × decision, pooled audit.
  - **Fig. S2** `fig_S2_tipping_points`: net-flip DiD vs tipping point, observed G with CI, audit-implied G.
  - **Fig. S3** `fig_S3_route_validation`: V7.
  - **Fig. S4** `fig_S4_flip_rates`: drop and add rates with feature-present denominators (replaces `fig_S4_drop_rates`).
- **Interim run** (254 enlargement records): `interim_254/`.


## Audit response

Three independent audits reviewed the interim run:
- the code audit (`outputs/audit/snapshot_code/`), issues C-I1 to C-I10;
- the identification audit (`outputs/audit/snapshot_ident/`), issues S-I1 to S-I9;
- the reporting audit (`outputs/audit/snapshot_reporting/`), issues R1 to R18.

Each issue was re-checked before it was fixed. Fixes live in `src/analyses/snapshot_final.py` and `snapshot_final_report.py`. `snapshot_bounds.py` is unchanged, because the prereg bundle hashes it. The fix log is `outputs/audit/wp4/fix_log.md`.

**Claims weakened or withdrawn, in one place.**
1. "No sign that review-stage acceptance is manufactured by post-decision renaming" is withdrawn. At the audit point estimate about 50% of the NAME G_dec excess is camera-ready (CI −21% to 124%).
2. "Camera-ready editing moves features in both directions at similar rates" is withdrawn. Drop rates are similar, but accepted papers add NAME 3.2× as often as rejected papers.
3. The camera-ready retitling excess (+6.4 pp; +10.1 pp in 2024–26) is withdrawn. It is +1.5 pp on the complete audit and −2.7 pp where the v1 was posted during review.
4. The G4 magnitude falls from +3.55 pp to +0.71 pp (2024–26 pairs). The "consistent with LLM-assisted polishing" sentence is withdrawn.
5. "Findability depends neither on NAME nor title length nor route" is rewritten. Longer titles are slightly less findable, and the two routes share an abstract-similarity rule.
6. The interim "0 of 24 pass" was right only by accident of the 254-record freeze. Under the interim rule 2 features pass on the complete audit; only the new multiplicity-controlled gate yields 0.

**Claims strengthened.**
- G1 (H4a NAME neutrality survives editing) moves from "partially supported" to **supported**: corrected 90% CI [0.949, 1.031].
- The editing-corrected NAME G_total at the audit point estimate is 0.991, below the stored-title 1.021.

### Code audit

- **C-I1 (major) — valid, fixed.**
  - What was wrong: the interim run froze the enlargement at 254 of 2,000 records, and D4 and the prereg use different audit samples.
  - Change: the analysis now runs on the complete enlargement (2,000 records, 2,004 lines, SHA-256 in `meta.audit_freeze`). That sample is the primary audit, and a freeze path reports the verdicts at 254, 600, 1,000 and 1,261 lines.
  - Not done in this work package: D4 (`d4_bias_atlas.py`) and the prereg (`prereg_confirm.freeze_audit`, 1,261 lines) are other directions' frozen files. Both were aligned to this freeze in the later integration pass (§8). D3's slot-word audit (`d3_slots.py`, 1,620 lines) was aligned in the second integration pass.
  - What a prereg gate run would currently admit: at 1,261 lines the uncorrected rule passes Compound, Sentence case, O-union w/o ALL-CAPS.
- **C-I2 (major) — valid, fixed.** The gate is now: auditable, editing-corrected 95% CI excludes 1, and the Holm-adjusted one-sided identification p (with the tipping point's sampling error) < 0.025 across 18 auditable features. p-values and Holm values are in `gate.csv` and `T4_2_tipping_points.csv`. Result: 0 pass; smallest Holm p 0.29. The uncorrected rule is kept as a column.
- **C-I3 (major) — valid, fixed.**
  - Both sentences are withdrawn.
  - G at the audit point estimate is now reported: NAME 1.025, strict 1.018, loose 1.024, against observed 1.050.
  - NAME flips on the complete audit: accepted +20/−16, rejected +4/−9. DiD +1.48 [−0.63, 3.59] pp.
- **C-I4 (minor) — valid, fixed.** arXiv titles carry no U+2011/U+2013 typography (0 of 3,659) and are never ALL-CAPS. Title typography, ALL-CAPS title, the L-title union and the O-union are flagged channel-unauditable. G2 now audits R24 or R26: DiD −0.32 pp, not identified.
- **C-I5 (minor) — valid, fixed by stratification.**
  - Original sample: retitling difference +14.4 pp before the deadline vs −6.8 pp during review.
  - Primary: v1 in review for 54.3% of accepted vs 50.0% of rejected pairs.
  - New specs `v1_in_review`, `v1_before_deadline` and `timing_std`: NAME DiD +2.26, +0.67 and +1.55 pp. The limitation is reworded.
  - Not done: fetching the last pre-decision arXiv version would need new network queries.
- **C-I6 (minor) — valid, fixed.** The abstract audit pools the enlargement's v1 abstracts. G4 is primary on 2024–26 pairs (628/404): +0.71 [−1.95, 3.36]. On 2023–26 pairs it is +0.73. Verdict partially supported, unchanged.
- **C-I7 (minor) — valid, fixed.** The pilot's 1.8 pp is P₃ − P₂ = 1.74 pp without the 1/(1 − a₂) factor. Deviation 3 and §4 are corrected.
- **C-I8 (minor) — valid, fixed.** Every note in `results.json` is generated from the tables. RESULTS.md is generated by `snapshot_final_report.py`, with assertions on every verdict-dependent sentence.
- **C-I9 (minor) — valid, fixed in wording and specs.**
  - V7a and the headline are softened.
  - New `abstract_matched` spec: NAME DiD +1.59 pp.
  - The union spec is renamed `union_route_v7sub` and its scope (the 300-paper subsample) is stated.
  - Not done: whole-token surname matching cannot be re-applied, because the caches do not store arXiv author lists. The abstract-matched spec removes every title-clause admission instead (rejected 9.1% vs accepted 1.6% of primary pairs).
- **C-I10 (minor) — valid, fixed.** The primary is 2023–26. The 9 accepted-only 2022 pairs form the `incl_2022` spec (NAME +1.48 pp), plus a `year_std` spec (+1.45 pp). The retitling period contrast is 2024–26 vs 2023.

### Identification audit

- **S-I1 (critical) — valid in substance; the remedy differs.**
  - On the complete audit, sentence case is auditable and fails the *uncorrected* gate (margin −0.18 pp). Passing it on the complete audit: the O-union w/o ALL-CAPS, Compound.
  - Sentence case passed the uncorrected gate at 600, 1,000, 1,261 enlargement lines, as the auditor found. It fails the multiplicity-controlled gate that PLAN §0 requires at every freeze; on the complete audit p = 0.044, Holm 0.70. It is therefore not reported as an audit-robust association. The closest lead is the O-union w/o ALL-CAPS (p 0.016, Holm 0.29).
  - SB2, the headline, §5 and the unauditable table are rewritten. D4's own H4b text is not edited here (other direction).
- **S-I2 (major) — valid, fixed** (as C-I3).
  - Editing share of the NAME excess at the point estimate: 50%; 2024–26 pairs: 80%.
  - Corrected submission-stage NAME G_total: 0.991 (primary) and 0.973 (2024–26).
  - "Peer review amplifies NAME" is explicitly rejected in the headline.
- **S-I3 (major) — valid, fixed.** SB3 is restated with final counts, and the freeze path shows auditability rising with n (10, 12, 15, 17, 18 auditable features). Verdict: partially supported.
- **S-I4 (major) — valid, fixed** (as C-I4). The channel criterion is part of the auditability rule. The ALL-CAPS "DiD exceeds the tipping point" sentence is deleted.
- **S-I5 (major) — valid, fixed in wording plus a bound.**
  - V7a now states that both routes share a latest-abstract similarity rule.
  - Near-miss bound (Jaccard ≥ 0.10): 1 accepted vs 14 rejected near-misses. The gap moves from 0.33 to 0.25.
  - The censoring is listed as a limitation of the rejected arm's noise floor.
- **S-I6 (minor) — valid, fixed** (as C-I5). The in-review stratum is reported as the cleanest camera-ready comparison: retitling −2.7 pp, NAME DiD +2.26 pp.
- **S-I7 (minor) — valid, fixed** (as C-I2).
  - Identification margins by CI type, and stability across 14 specs, are in `T4_2_identified_anywhere.csv` and §4.
  - 'via' is identified only in 2024–26 and out-of-sample specs and passes no gate.
- **S-I8 (minor) — valid, fixed** (as C-I6). The LLM-polishing sentence is withdrawn. G4 is reported as point ≥ 0 with a CI including 0.
- **S-I9 (minor) — valid, fixed.** G1 is upgraded to supported on the complete audit (corrected 90% CI [0.949, 1.031]). The corrected centre (0.991) and the 2024–26-pairs interval are reported, and the interim caveat is removed.

### Reporting audit

- **R1 (major) — valid, fixed.** The "no feature identified under any CI type" sentences are replaced by a generated table of every (spec, feature, CI type) identification (§4). Deviation 1 is reworded.
- **R2 (major) — valid, fixed** (as C-I1). The analysis is no longer interim, and the freeze path replaces the fragility note.
- **R3 (major) — valid, fixed** (as C-I3). The suggested wording is adopted, with final numbers.
- **R4 (major) — valid, fixed.** The false sentence is replaced. At the observed DiD the CI clears D\* at about 2.2× the current 1,311 pairs.
- **R5 (major) — valid, fixed.** The G2 row bug read the L_title G_dec row; the interim results.json showed 0.980 [0.938, 1.024]. G2 now reads the H4b G_total claim row by name, which is now the R24-or-R26 audit.
- **R6 (major) — valid, fixed.** The unauditable-features text no longer says "none is identified". Sentence case is now auditable and discussed with its margin. L-title is no longer called a strong association.
- **R7 (minor) — valid, fixed.** 50% and 80% power multipliers are reported (0.52× and 1.07× of the complete audit). So is the realised usable rate.
- **R8 (minor) — valid, fixed.** 2023 is audited per year. The unaudited range is 2018–2022, and pair counts and half-widths are generated.
- **R9 (minor) — valid, fixed.** The text now says "odds ratio" with both found rates. The NAME null is stated with its CI, and the interim CI reaching 2.2 is noted.
- **R10 (minor) — valid, fixed.** The abstract-Jaccard difference is reported with a bootstrap CI; it is not significant in either sample.
- **R11 (minor) — valid, fixed.** Deviation 11 records the gate operationalisation and the literal §4 result for NAME G_total.
- **R12 (minor) — valid, fixed** (as S-I4). The wording is "consistent with form entry".
- **R13 (minor) — valid, fixed.** The identity is stated for a single year; with pooling, D\* 2.92 vs RD 3.27 pp.
- **R14 (minor) — valid, fixed** (as C-I9). The text says "differ by" with the value, and the union spec is renamed.
- **R15 (minor) — valid, fixed.** The "partial n = 300 of 300" wording is gone.
- **R16 (minor) — valid, fixed.**
  - Fig. S2 draws D\* as a vertical tick under the DiD dot.
  - Channel-unauditable rows (incl. the L-abstract union) are grey with ‡.
  - Abstract rows use D\*_total and G_total, labelled.
  - Observed G carries its 95% CI, the legend shows both colours, and a footnote explains clipping.
- **R17 (minor) — valid, fixed.**
  - S1: per-panel legends, CIs on usable-pair rates, n per point.
  - S3: k/n on every point and an adaptive y-limit.
  - S4 (now `fig_S4_flip_rates`): add rates beside drop rates, with † and ‡ marking unauditable rows.
  - The text says drop rates overlap while add rates differ.
- **R18 (minor) — valid, fixed.** The "shrinks as data accrue" sentence is removed. The complete-audit estimate is reported with its CI.

