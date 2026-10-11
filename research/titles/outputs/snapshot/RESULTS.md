# WP4 Results: camera-ready snapshot bounds (D4 decision-stage bound, V7 route validation, §4 gate)

Work package WP4. Pre-registered in `docs/PLAN.md` §D4 ("Decision-stage bound"), §3 V7 and §4 (Gate); common definitions §0.

**Scripts.**
- `src/analyses/snapshot_bounds.py` does the analysis (about 15 s).
- `src/analyses/audit_v2.py` does the arXiv re-query in the background (route validation, v1 abstracts, enlargement; resumable).

**Data.**
- Machine-readable estimates for every hypothesis and robustness check are in `results.json`.
- Tables and figures are in this folder.
- Every number below was regenerated from `cache/arxiv_audit.jsonl` and the new caches written by `audit_v2.py`.

**Language.**
- All acceptance statements are associational.
- Author information enters only through the first author's declared name, used as an arXiv search key; it is never treated as a verified person.

**Why the audit matters.** The export is a post-decision snapshot, so accepted papers may carry camera-ready titles. Rejected, withdrawn and desk-rejected papers keep submission-stage text.

**How the audit works.**
- Each audited paper's arXiv version 1, posted before the ICLR decision date, is compared with the stored title.
- Rejected papers' v1-vs-stored differences measure everything that is *not* camera-ready editing: arXiv-vs-OpenReview wording and rebuttal-period edits.
- The accepted-minus-rejected difference in net feature flips (the **net-flip DiD**, D) is the camera-ready excess. This excess can bias any acceptance association of a title feature.

**Tipping point.**
- A net camera-ready addition D raises P(f | accepted) by D and P(f | reviewed) by a₂·D, where a₂ = 0.403 is the accepted share of the reviewed set in 2024–26.
- The submission-stage gain is G_dec(D) = (P₃ − D)/(P₂ − a₂D).
- Setting this to 1 gives the tipping point D* = (P₃ − P₂)/(1 − a₂). This equals the accepted-minus-rest risk difference.
- A G_dec claim is **identified** only if the feature is auditable and D* lies beyond the audit 95% CI, on the side that would move G to 1.

---

## Verdict summary

| ID | Claim tested | Estimate (95% CI unless stated) | Criterion | Verdict |
|---|---|---|---|---|
| SB1 | PLAN D4: NAME G_dec is not identified by the current audit (pilot: tip ≈ 1.8 pp vs DiD +2.1, se 2.4) | DiD **+2.09 pp [−3.16, 7.33]**. Plain Wald se 2.37, CI [−2.57, 6.74]. Tip **D\* = 2.92 pp**. G_dec 1.050 [1.027, 1.073]; audit-implied submission-stage G_dec [0.917, 1.101] | Identified iff D\* > upper CI | **Supported** (not identified) |
| SB2 | Gate §4: some title feature's acceptance association (G_dec ≠ 1) survives the audit | **0 of 24** features pass. 10 are auditable; none is identified under any of 6 audit specifications | Auditable, D\* beyond the audit CI, and observed G_dec CI excludes 1 | **Not supported** |
| SB3 | V7: rare lexical features are unauditable (< 10 v1-present titles in an arm) | v1-present accepted/rejected: 'using' **4**/5, R24 6/3, R26 8/0, LLM slot word 6/2, title typography 0/0 | Pre-stated threshold of 10 per arm | **Supported** |
| SB4 | Accepted papers are more findable; IPW leaves the NAME bound unchanged | Found 88.6% vs 56.3%. OR(accepted) **6.16 [4.02, 9.44]**, OR(NAME) 1.37 [0.86, 2.20]. IPW × population NAME DiD 2.01 [−3.71, 7.74] | Not pre-registered; descriptive | **Supported** |
| SB5 | Camera-ready retitling: accepted papers retitle more than rejected ones | 29.6% vs 23.2%: **+6.4 pp [−3.6, 15.7]**. 2024–26: +10.1 pp [−1.2, 20.4] | CI excludes 0 | **Not supported** (direction as expected) |
| V7a | A title-free route finds papers at a similar rate; the findability gap is not a title-route artefact | n = 300 (150/150). Found by route A / route B: accepted 88.7% / 84.7%, rejected 52.7% / 48.7%. Gap 0.36 on both routes; difference 0.00 [−0.06, 0.06]. arXiv-id agreement 99.5% | Gap B CI > 0 and gap difference CI includes 0 | **Supported** |
| V7b | The title route does not select on title stability | Retitled: route A 24.4% (n = 160), route B 26.5% (n = 155). Papers only route B finds: 4 of 6 retitled. Union-route NAME DiD 1.25 [−4.10, 6.60] | Rule in `results.json` | **Partially supported** |
| G1 | Gate for D4-H4a: NAME neutrality (pooled 2024–26 G_total in [0.90, 1.11]) survives camera-ready uncertainty | G_total 1.021, 90% CI [1.001, 1.041]. Original audit: audit-implied [0.867, 1.081], **editing-corrected 90% CI [0.885, 1.069]** (fails). Partially enlarged audit (455 pairs): corrected 90% CI **[0.921, 1.066]** (passes). G_dec passes in both: [0.930, 1.089] and [0.962, 1.087] | Corrected 90% CI inside the margins | **Partially supported** (passes only with the enlarged audit) |
| G2 | Gate for D4-H4b: depletion of title LLM markers (L-title G_total < 1) survives the audit | G_total 0.915, 90% CI [0.872, 0.961]. L-title is unauditable (v1-present 14/3). Audit-implied [0.673, 1.159] | Identified and corrected CI < 1 | **Not supported** (not auditable) |
| G3 | Abstract audit (extension): depletion of arXiv-measurable abstract LLM markers (F24 or F26 words, G_total < 1) survives the audit | F24 or F26 words: G_total **0.998** [0.960, 1.034]; DiD +3.88 pp [−1.61, 9.38]; tip −0.06 pp. F24: G_total 0.963 [0.916, 1.007], tip −0.67 pp, DiD +3.55 [−1.62, 8.73]. Em dash unauditable (0 v1-present: arXiv writes TeX dashes) | Identified and corrected CI < 1 | **Not supported** (little pooled depletion to protect, and not identified) |
| G4 | D4-H4c direction assumption: camera-ready polishing does not *lower* accepted papers' RARE21 rates | F24 net flips: accepted +1.94 pp (8 adds / 4 drops; v1-present 20), rejected −1.61 pp (1 / 3; v1-present 13). **DiD +3.55 pp [−1.62, 8.73]** | Sign of DiD (CI > 0 = supported) | **Partially supported** (right sign, CI includes 0) |

**Headline.**
- The current audit cannot identify the sign of any decision-stage acceptance association of a title feature.
  - For the mainstream markers the camera-ready band is several times wider than the tipping point. NAME, compound and Title Case have net-flip DiD CIs about ±5 pp, against tipping points of 2.6–3.2 pp.
  - Every lexical LLM marker and every outsider marker except the O-union is unauditable.
- What the audit does show:
  1. Accepted papers are found on arXiv six times more often (odds) than rejected ones. This depends neither on NAME nor on title length, nor on the retrieval route.
  2. Camera-ready editing moves features in both directions at similar rates. Accepted NAME: 7 adds and 6 drops among 206 pairs. There is no sign that review-stage acceptance is manufactured by post-decision renaming.
  3. D4-H4a's NAME G_total TOST fails on the original audit (editing-corrected 90% CI lower bound 0.885). It passes on the partially enlarged audit (0.921), so it rests on the enlargement. The G_dec form passes in both.
  4. Title-LLM-marker depletion (D4-H4b, decision-stage part) cannot be made audit-robust: the markers are too rare in v1 titles to audit.
- The non-identification of every acceptance association is unchanged under:
  - the 2024–26-only audit;
  - findability IPW, with and without population design weights;
  - a union of the two retrieval routes;
  - plain Wald and bootstrap CIs;
  - a partially enlarged audit of 455 pairs.

---

## 1. Audit sample and differential findability (`found_rates.csv`, `findability_models.csv`, Fig. S1a)

**Sample.** The original audit (`src/arxiv_audit.py`, title route) holds 616 papers:
- 75 per year × decision cell for 2023–2026;
- 16 accepted papers from 2022.

**Usable pair.** A paper counts as a usable pair when it is found on arXiv, has a v1 title, and its v1 date precedes the decision date of its conference year (`arxiv_audit.DECISION_DATE`).

| | n | Found | Found rate [95% Wilson] | Usable pre-decision pairs | Usable / found |
|---|---|---|---|---|---|
| Accepted, all years | 316 | 280 | 88.6% [84.6, 91.7] | 206 (65.2%) | 73.6% |
| Rejected, all years | 300 | 169 | 56.3% [50.7, 61.8] | 125 (41.7%) | 74.0% |
| Accepted, 2024–26 | 225 | 202 | 89.8% [85.1, 93.1] | 151 | 74.8% |
| Rejected, 2024–26 | 225 | 131 | 58.2% [51.7, 64.5] | 98 | 74.8% |

**Rates by year.**
- Found rates per year: accepted 85–91%, rejected 51–61%.
- Usable pairs rise from 2024 to 2026: OR 1.76 [1.09, 2.85] for 2026 vs 2023. More 2026 papers were on arXiv before the decision.

**Findability models** (logit, 2023–26, n = 600):
- OR(accepted) for being found = **6.16 [4.02, 9.44]**.
- NAME does not predict findability: OR 1.37 [0.86, 2.20]. Nor does title length: OR per log word 0.77 [0.41, 1.45].
- For being a usable pair, OR(accepted) = 2.76 [1.97, 3.86] and OR(NAME) = 1.43 [0.96, 2.14] (p = .08).
- Given found, having a pre-decision v1 does not depend on the decision: OR 1.04 [0.67, 1.63].
- The selection is therefore almost entirely "is the paper on arXiv at all", which differs by decision.
- IPW weights for the robustness specs: 1/P̂(usable | year, accepted, log title words, NAME), optionally times N_pop/n_sampled per year × decision.
  - Normalised weights range 0.71–1.40 without design weights and 0.46–1.61 with them.
  - Kish effective n with design weights: 176 of 197 accepted, 112 of 125 rejected.
  - Results are in §4.

## 2. Retitling between pre-decision v1 and stored title (`retitling.csv`, Fig. S1b)

**Measures** (on usable pairs):
- *Retitled*: the word sequence differs after lower-casing and stripping punctuation.
- *Major*: content-word Jaccard < 0.5.
- *Case/punctuation-only*: the raw string differs but the word sequence does not.

| Years | Measure | Accepted | Rejected | Difference, Newcombe 95% CI |
|---|---|---|---|---|
| all (2022–26) | retitled | 61/206 = 29.6% | 29/125 = 23.2% | **+6.4 pp [−3.6, 15.7]** |
| all | major | 12.6% | 8.8% | +3.8 [−3.5, 10.3] |
| all | case/punct only | 7.3% | 8.8% | −1.5 [−8.4, 4.3] |
| 2024–26 | retitled | 46/151 = 30.5% | 20/98 = 20.4% | +10.1 [−1.2, 20.4] |
| 2024–26 | major | 13.9% | 6.1% | +7.8 [−0.3, 15.0] |
| 2022–23 | retitled | 27.3% | 33.3% | −6.1 [−27.4, 13.5] |

**Model and period contrast.**
- Logit with year FE: OR(accepted) = 1.41 [0.84, 2.36], p = .19.
- The period DiD, (acc − rej) in 2024–26 minus (acc − rej) in 2022–23, is +16.1 pp. Its bootstrap 95% CI is [−7.2, 39.6].

**Interpretation.**
- About a quarter of rejected papers already carry a different title on arXiv v1 than on OpenReview. This is a large non-camera-ready noise floor.
- The camera-ready excess among accepted papers is positive in point estimate (+6 pp, +10 pp in 2024–26), but not distinguishable from 0 at this sample size.
- Title length does not change on average: Δwords +0.01 (accepted), −0.03 (rejected).

## 3. Flip matrices with feature-present v1 denominators (T4.2: `T4_2_flip_matrices.csv`, `T4_2_flip_multiclass.csv`, Fig. S4)

**Features.** All features are computed with `features_v2.build` on both titles. The stored-title features reproduce `features_v2.parquet` exactly.

**Column definitions.**
- Cells show *v1-present: +adds / −drops*.
- Net = (adds − drops)/n.
- DiD = net(accepted) − net(rejected).
- **Primary CI:** Wald with a pseudo-flip variance floor (one pseudo-add and one pseudo-drop per arm). Plain Wald SEs are 0 when an arm has no flips, which would let any tipping point look identified.
- **Auditable:** ≥ 10 v1-present titles in *both* arms (pre-stated).

| Feature | Accepted (n = 206) | Rejected (n = 125) | Net acc / rej (pp) | DiD (pp) [pseudo-flip 95% CI] | Plain Wald CI | Auditable |
|---|---|---|---|---|---|---|
| NAME (primary) | 52: +7/−6 | 42: +1/−3 | +0.5 / −1.6 | **+2.09 [−3.16, 7.33]** | [−2.57, 6.74] | yes |
| NAME strict | 50: +7/−5 | 41: +1/−3 | +1.0 / −1.6 | +2.57 [−2.59, 7.73] | [−1.98, 7.12] | yes |
| NAME loose | 57: +9/−6 | 46: +1/−3 | +1.5 / −1.6 | +3.06 [−2.35, 8.47] | [−1.79, 7.90] | yes |
| Compound | 93: +6/−8 | 63: +1/−4 | −1.0 / −2.4 | +1.43 [−4.11, 6.97] | [−3.56, 6.42] | yes |
| Phrase colon | 41: +2/−5 | 21: +1/−2 | −1.5 / −0.8 | −0.66 [−5.11, 3.80] | [−4.36, 3.05] | yes |
| Title Case | 196: +2/−3 | 117: +3/−5 | −0.5 / −1.6 | +1.11 [−4.36, 6.59] | [−3.81, 6.04] | yes |
| Mixed-case name | 37: +3/−3 | 22: +1/−3 | 0.0 / −1.6 | +1.60 [−3.02, 6.22] | [−2.31, 5.51] | yes |
| ALL-CAPS name | 13: +4/−2 | 15: +1/−1 | +1.0 / 0.0 | +0.97 [−3.11, 5.05] | [−2.25, 4.20] | yes |
| O-union | 12: +3/−2 | 10: +3/−4 | +0.5 / −0.8 | +1.29 [−3.97, 6.54] | [−3.39, 5.96] | yes |
| 'via' | 19: +7/−5 | 12: +1/−2 | +1.0 / −0.8 | +1.77 [−3.16, 6.70] | [−2.51, 6.05] | yes |
| Sentence case | 7: +3/−2 | 8: +0/−4 | +0.5 / −3.2 | +3.69 [−0.81, 8.18] | [−0.07, 7.45] | no |
| ALL-CAPS title | 0: +0/−0 | 0: +3/−0 | 0.0 / +2.4 | −2.40 [−6.08, 1.28] | [−5.09, 0.29] | no |
| LLM slot word | 6: +0/−2 | 2: +0/−0 | −1.0 / 0.0 | −0.97 [−3.85, 1.91] | [−2.31, 0.37] | no |
| Any slot filled | 8: +2/−2 | 4: +0/−0 | 0.0 / 0.0 | 0.00 [−3.18, 3.18] | [−1.91, 1.91] | no |
| R24 word | 6: +0/−0 | 3: +0/−0 | 0 / 0 | 0.00 [−2.56, 2.56] | [0, 0] | no |
| R26 word | 8: +1/−0 | 0: +0/−0 | +0.5 / 0 | +0.49 [−2.24, 3.21] | [−0.47, 1.44] | no |
| Title typography | 0: +1/−0 | 0: +1/−0 | +0.5 / +0.8 | −0.31 [−3.44, 2.81] | [−2.15, 1.52] | no |
| L-title union | 14: +1/−0 | 3: +1/−0 | +0.5 / +0.8 | −0.31 [−3.44, 2.81] | [−2.15, 1.52] | no |
| 'using' | 4: +1/−1 | 5: +0/−0 | 0 / 0 | 0.00 [−2.88, 2.88] | [−1.35, 1.35] | no |
| LLM abbrev-only | 11: +2/−0 | 8: +1/−0 | +1.0 / +0.8 | +0.17 [−3.09, 3.44] | [−1.89, 2.23] | no |

The (ACR)-name, word-name, mixed-casing and question-opener rows are in the CSV; all are unauditable.

**Drop rates given v1-present** (Fig. S4) are similar across arms:
- NAME: 11.5% vs 7.1%.
- Compound: 8.6% vs 6.3%.
- Title Case: 1.5% vs 4.3%.
- via: 26% vs 17%.

**Multi-class matrices** (`T4_2_flip_multiclass.csv`).

*Accepted:*
- Casing: 2 sentence→Title Case and 3 Title Case→sentence.
- Name orthography: none→ALL-CAPS 4, none→mixed-case 3, mixed-case→none 3, ALL-CAPS→none 2, word→none 1.
- Slot state: LLM→none 2, none→neutral 2. No camera-ready additions of an LLM-favoured slot word.
- via/using: neither→via 7, via→neither 5, neither→using 1, using→neither 1.

*Rejected:*
- 3 Title Case→ALL-CAPS and 2 Title Case→mixed. These are OpenReview titles typed in capitals while the arXiv v1 is not, so they are form-entry artefacts.
- 3 sentence→Title Case.

**Examples of real camera-ready NAME additions in 2026.**
- "Self-Augmented Visual Contrastive Decoding" → "Self-Aug: Query and Entropy Adaptive Decoding …".
- "Scaled Inverse Graphics: …" → "Fused-Planes: …".
- "Shortening the Trajectories: …" → "GAGA: …".

**Examples of drops.**
- "SeerAttention-R: …" → "Sparse Attention Adaptation for Long Reasoning".
- "RSRM: …" → "Reinforcement Symbolic Regression Machine".

## 4. Tipping points and the decision-stage bound (T4.2: `T4_2_tipping_points.csv`, `T4_2_identification_by_spec.csv`, `T4_2_tipping_by_year.csv`, Fig. S2)

**Prevalences.** Universe prevalences are pooled over 2024–26 and year-standardised to s0 sizes, as in D4.
- They reproduce D4's interim table (`d4_filter/T4_2_decision_bound.csv`) to 5 decimals for every shared feature.
- The audit DiD is the primary all-years estimate.
- The combined CI pairs a universe bootstrap replicate (2,000, stratified by year) with an independent audit draw, D ~ N(D̂, pseudo-flip SE), clipped to the feasible range [P₃ − 1, P₃].

**Auditable features.**

| Feature | P(f \| reviewed) → P(f \| accepted) | G_dec [95%] | DiD [95%] (pp) | Tipping D\* (pp) | Audit-implied G_dec | Identified | n-multiplier needed if true D = 0 |
|---|---|---|---|---|---|---|---|
| NAME | 34.6 → 36.4% | 1.050 [1.027, 1.073] | +2.09 [−3.16, 7.33] | **2.92** | [0.917, 1.101] | no | 3.2× |
| NAME strict | 33.6 → 35.4% | 1.053 [1.031, 1.077] | +2.57 [−2.59, 7.73] | 2.99 | [0.907, 1.096] | no | 3.0× |
| NAME loose | 36.9 → 38.7% | 1.050 [1.028, 1.071] | +3.06 [−2.35, 8.47] | 3.06 | [0.903, 1.086] | no | 3.1× |
| Compound | 52.3 → 54.3% | 1.037 [1.021, 1.051] | +1.43 [−4.11, 6.97] | 3.24 | [0.955, 1.081] | no | 2.9× |
| Phrase colon | 17.7 → 17.9% | 1.011 [0.975, 1.045] | −0.66 [−5.11, 3.80] | 0.32 | [0.872, 1.164] | no | 188× |
| Title Case | 93.0 → 94.5% | 1.017 [1.012, 1.021] | +1.11 [−4.36, 6.59] | 2.59 | [0.974, 1.044] | no | 4.5× |
| Mixed-case name | 22.6 → 24.6% | 1.087 [1.055, 1.118] | +1.60 [−3.02, 6.22] | 3.29 | [0.913, 1.158] | no | 2.0× |
| ALL-CAPS name | 10.2 → 9.9% | 0.966 [0.919, 1.012] | +0.97 [−3.11, 5.05] | −0.59 | [0.590, 1.131] | no | 48× |
| O-union | 6.8 → 5.6% | 0.812 [0.757, 0.869] | +1.29 [−3.97, 6.54] | −2.15 | [0.000, 1.129] | no | 6.0× |
| 'via' | 10.6 → 11.1% | 1.048 [1.001, 1.095] | +1.77 [−3.16, 6.70] | 0.85 | [0.555, 1.202] | no | 34× |

**Unauditable features with strong stored-title associations.** None is identified. In each case the camera-ready band cannot be bounded with the present v1 denominators.

| Feature | G_dec [95%] | Tip D\* (pp) | Audit CI (pp) | v1-present (acc/rej) | Audit-implied G_dec |
|---|---|---|---|---|---|
| ALL-CAPS title | 0.435 [0.320, 0.559] | −1.04 | [−6.08, 1.28] | 0/0 | [0.00, 1.85] |
| 'using' | 0.700 [0.597, 0.795] | −1.00 | [−2.88, 2.88] | 4/5 | [0.00, 1.36] |
| Mixed casing | 0.727 [0.608, 0.849] | −0.63 | [−6.08, 1.28] | 2/0 | [0.00, 1.85] |
| Sentence case | 0.868 [0.797, 0.942] | −0.94 | [−0.81, 8.18] | 7/8 | [0.00, 0.98] |
| R24 word | 0.896 [0.830, 0.968] | −0.83 | [−2.56, 2.56] | 6/3 | [0.46, 1.18] |
| R26 word | 1.093 [1.005, 1.178] | +0.54 | [−2.24, 3.21] | 8/0 | [0.26, 1.38] |
| L-title union | 0.980 [0.930, 1.032] | −0.29 | [−3.44, 2.81] | 14/3 | [0.76, 1.19] |

**Notes on individual features.**
- **ALL-CAPS title.** The point estimate of the camera-ready DiD (−2.4 pp) exceeds the whole tipping point (−1.04 pp) in magnitude. The 3 rejected Title Case→ALL-CAPS flips show that ALL-CAPS is partly an OpenReview form-entry habit. Proceedings editing could normalise it for accepted papers. The D4 "ALL-CAPS depletion" at the decision stage is therefore not separable from editing.
- **Sentence case.** Editing points the other way: accepted papers gain sentence case. If it were auditable, the depletion would be conservative.
- **'using'.** The PLAN's example (C20, "n = 4 accepted v1 titles") reproduces exactly with the v2 detector.

**Robustness of the NAME bound** (`T4_2_identification_by_spec.csv`; the tipping point is 2.92 pp throughout):

| Audit specification | n acc / rej | DiD (pp) [95%] | Identified |
|---|---|---|---|
| Primary (all usable pairs, 2022–26) | 206 / 125 | +2.09 [−3.16, 7.33] | no |
| 2024–26 pairs only | 151 / 98 | +3.01 [−3.35, 9.36] | no |
| IPW for findability | 197 / 125 | +2.29 [−3.16, 7.74] | no |
| IPW × population design weights (2023–26) | 197 / 125 | +2.01 [−3.71, 7.74] | no |
| Union of retrieval routes (adds route-B-only pairs) | 207 / 130 | +1.25 [−4.10, 6.60] | no |
| Original + enlargement (partial: first 254 enlargement records) | 280 / 175 | +1.29 [−2.87, 5.44] | no |
| Plain Wald / bootstrap CI (primary pairs) | 206 / 125 | [−2.57, 6.74] / [−2.57, 6.94] | no / no |

No feature is identified in any specification, under any CI type.

**Per-year bounds** (`T4_2_tipping_by_year.csv`).
- Year-specific DiDs use 27–56 pairs per arm, so their CIs are about ±9–18 pp. Example: NAME in 2025, DiD +2.9 [−9.9, 15.8] against a tip of 4.5 pp.
- No per-year acceptance association is identified.
- **H4a's per-year G_total claims for 2018–2023 have no audit at all.** No decision dates were used before 2022, and pre-2023 cells are tiny.

**Comparison with the PLAN pilot.**
- The DiD and SE reproduce: +2.09 pp, Wald se 2.37, against +2.1 and 2.4.
- The tipping point is 2.92 pp, not 1.8 pp. It is computed with D4's year-standardised 2024–26 prevalences and is identical to D4's interim value. The pilot used a different pooling.
- The conclusion is unchanged: NAME G_dec is **not identified**.
- How large an audit would be needed:
  - If the true DiD were 0, about 3.2× the current number of usable pairs (≈ 1,070) would be required. With the partial enlargement the multiplier falls to 2.0×. The planned 2,000-paper enlargement would add about 1,080 usable pairs at the observed 54% usable rate, about 4.3× the current pairs in total, which would suffice.
  - At the observed point estimate (+2.1 pp, close to D\*), no audit size would identify NAME G_dec.

## 5. Gate for D4 claims (PLAN §4; `gate.csv`)

**H4a (NAME neutrality, pooled 2024–26).**
- G_dec passes TOST after editing correction: corrected 90% CI [0.930, 1.089] lies within [0.90, 1.11].
- G_total does not: corrected 90% CI [0.885, 1.069].
  - A net camera-ready NAME addition at the audit's upper bound (+7.3 pp) would put the submission-stage G_total at 0.867.
  - G_total is more editing-sensitive than G_dec because accepted papers are a smaller share of s0 (a₀ = 0.29) than of s2 (a₂ = 0.40).
- So H4a's G_total TOST is **not robust to camera-ready editing on the original audit**. It becomes robust once the audit is enlarged: with the partial enlargement (280/175 pairs), the corrected 90% CI is [0.921, 1.066] (G_dec [0.962, 1.087]). The G_dec form passes in both.
- This verdict should be re-checked when the enlargement finishes; see §8 on fragility.

**H4b (depletion of LLM and outsider markers).**
- The title parts (L-title, ALL-CAPS title, sentence case) are unauditable, so their decision-stage parts cannot pass the gate.
- The O-union is auditable but not identified.
- H4b's audit-free component, G_desk × G_exit on submission-stage text, is unaffected.

**Acceptance associations.** 0 of 24 title features pass.

**Diachronic and NA-pool results** do not depend on the audit (PLAN §4).

## 6. Abstract audit (extension; `abstract_audit.csv`)

**Design.**
- For the 330 original pre-decision pairs (206 accepted, 124 rejected; one 503 error is retried on rerun), `audit_v2.py` re-fetched the arXiv v1 record and cached its abstract.
- The v1 titles re-fetched match the original audit for 100% of pairs.
- Abstract LLM markers are computed with `features_v2.build` on the v1 abstract and on the stored abstract.
- Content-word Jaccard between v1 and stored abstract: accepted 0.77, rejected 0.83. Accepted abstracts change more between arXiv v1 and the stored version.

| Marker | Accepted (n = 206): v1-present, +adds/−drops; prevalence v1 → stored | Rejected (n = 124) | DiD (pp) [pseudo-flip 95%] | Auditable |
|---|---|---|---|---|
| F24 (RARE21 ≥ 1) | 20, +8/−4; 9.7% → 11.7% | 13, +1/−3; 10.5% → 8.9% | **+3.55 [−1.62, 8.73]** | yes |
| RARE21 ≥ 2 | 3, +1/−1 | 4, 0/0 | 0.00 [−2.90, 2.90] | no |
| F26 words | 6, +4/−0; 2.9% → 4.9% | 3, +2/−0; 2.4% → 4.0% | +0.33 [−3.53, 4.18] | no |
| Abstract em dash | 0, +16/−0 | 0, +11/−0 | −1.10 [−7.74, 5.53] | no (channel) |
| F24 or F26 words | 25, +12/−4; 12.1% → 16.0% | 16, +2/−2; 12.9% → 12.9% | +3.88 [−1.61, 9.38] | yes |

**Em dash.** No arXiv v1 abstract contains an em dash. arXiv abstracts carry dashes as TeX `--`/`---` or a plain hyphen, e.g. "interactions--such as" vs the stored "interactions—such as". The em dash, and by the same mechanism U+2011 / en-dash typography, **cannot be audited through arXiv**. The L-abstract union that includes the em dash is reported in the CSV but not interpreted.

**Tipping points** (pooled 2024–26, year-standardised):
- F24: G_dec 0.989 [0.945, 1.031], G_total 0.963 [0.916, 1.007]. Tipping points −0.23 pp (dec) and −0.67 pp (total). Audit-implied G_total [0.357, 1.050]. Not identified.
- F24 or F26 words: G_total 0.998 [0.960, 1.034]. Not identified.

**Readings.**
1. On stored abstracts, the accepted/all *prevalence* ratio for RARE21 is close to 1: 0.93 (2024), 0.94 (2025), 1.02 (2026); 0.96 pooled.
   - D4's H4c contrast is larger because the Kobak bound subtracts a pre-2024 baseline from both sets. D4 `kobak_bounds.csv` gives accepted/all bound ratios of 0.80 (2024) and 0.71 (2025).
   - A prevalence-scale depletion of 3–7% cannot be made audit-robust with 206 accepted pairs: the tipping points are below 1 pp, against a ±5 pp audit band.
2. The sign of the abstract-editing DiD is **positive**: accepted papers *gain* RARE21 words between the arXiv v1 and the stored abstract (+1.9 pp net), while rejected papers lose them (−1.6 pp).
   - This is the direction H4c assumes, so the accepted-only understatement is conservative.
   - The CI includes 0.
   - The 8 accepted RARE21 additions (vs 4 drops) are consistent with LLM-assisted camera-ready polishing, but do not demonstrate it.

## 7. V7: retrieval-route validation (`route_validation.csv`, `route_pairs.csv`, Fig. S3)

**Design.**
- Sample: a random subsample of the original audit, 150 accepted + 150 rejected (seed 20261011), processed in random order. **Complete: n = 300.**
- **Route B** never uses the title. It queries `au:<first-author surname> AND abs:w1 AND abs:w2 AND abs:w3`.
  - The w's are the three abstract words with the lowest document frequency among all exported ICLR abstracts, excluding any word in the stored title.
  - A fallback query uses the surname and the next two words.
- **Acceptance tiers:**
  - A: abstract Jaccard ≥ 0.45.
  - B: surname among the arXiv authors and Jaccard ≥ 0.30.
  - C: surname match, Jaccard ≥ 0.15, v1 year in [year − 2, year + 1], and a 3-word query.
- Hits: 192 tier A, 6 tier B, 2 tier C. One tier-C hit was a different paper by the same first author (the only arXiv-id disagreement), so the strict rule (A or B) is reported as well.

| | Accepted (n = 150) | Rejected (n = 150) | All (n = 300) |
|---|---|---|---|
| Found, route A (title) | 88.7% [82.6, 92.8] | 52.7% [44.7, 60.5] | 70.7% |
| Found, route B (surname + abstract) | 84.7% [78.0, 89.6] | 48.7% [40.8, 56.6] | 66.7% |
| Found, route B strict tiers | 84.7% | 47.3% | 66.0% |
| Found, A or B | 89.3% | 56.0% | 72.7% |
| A only / B only / neither | 7 / 1 / 16 | 11 / 5 / 66 | 18 / 6 / 82 (McNemar p = .023) |
| Same arXiv id when both found | 100% | 98.5% | 99.5% |
| Usable pairs, route A / route B | 102 / 98 | 58 / 57 | 160 / 155 |
| v1 retitled vs stored, route A | 26.5% | 20.7% | 24.4% |
| v1 retitled vs stored, route B | 27.6% | 24.6% | 26.5% |
| v1 retitled vs stored, route B strict tiers | 27.6% | 23.6% | 26.1% |
| Latest arXiv title ≠ stored, route A / route B | 5.3% / 5.5% | 25.3% / 28.8% | 12.7% / 14.0% |

**Findability (V7a).**
- The title route finds slightly *more* papers than the title-free route. Part of the reason is that its third attempt already uses the surname plus abstract words.
- The accepted–rejected findability gap is identical on both routes: 0.36; difference 0.00 [−0.06, 0.06].
- Differential findability is therefore a property of which papers are on arXiv, not of how they are searched.

**Title stability (V7b).**
- Retitling rates agree within 2 pp between routes.
- The 6 papers found only by route B are disproportionately retitled: 4 of 6. Two examples:
  - "Deep Network Partition Density Exhibits Double Descent", whose arXiv v1 is "Training Dynamics of Deep Network Linear Regions".
  - "Boosting Neural Combinatorial Optimization for Large-Scale V…", whose v1 is "Self-Improved Learning for Scalable Neural Combinatorial Optimization".
- So the title route under-finds some retitled papers, but they are about 2% of the sample. Adding them moves the NAME DiD from +2.09 to +1.25 pp, well inside its CI.
- Rejected papers' *latest* arXiv titles differ from the stored title in about a quarter of cases (accepted: 5%). This is retitling after rejection, which the title route mostly still finds through its abstract-based fallback.

## 8. Enlarged audit (partial; `audit_v2.py` phase 2)

**Status at the analysis freeze.**
- Done: 254 of the 2,000 queued papers. They are interleaved across the 8 year × decision cells, 23–43 per cell.
- Same title route as the original audit; written to `cache/arxiv_audit_enlarge.jsonl`.
- The job continues in the background. It is resumable and rate-limited, and the lock file prevents a second instance.
- `snapshot_bounds.py` picks up whatever has finished. `--enlarge-n N` freezes a run; the reported run used `--enlarge-n 254`.
- Throughput is about 375 papers per hour. Each paper needs 2–4 requests at ≥ 3.2 s apart, so the PLAN's "1k papers/hour" is not achievable within the rate limit.

**Findability replicates out of sample.**
- New papers: found 81.2% [73.2, 87.2] accepted vs 50.4% [42.1, 58.6] rejected.
- Pooled with the original (2023–26, n = 854):
  - OR(accepted) 5.47 [3.89, 7.69];
  - OR(NAME) 1.27 [0.86, 1.85];
  - OR(log title words) 0.93 [0.56, 1.53];
  - pre-decision v1 given found, OR(accepted) 1.11 [0.76, 1.62].

**Pairs.** 124 new usable pairs (74 accepted, 50 rejected), giving **455 pooled pairs (280 / 175)**.

**Retitling (pooled).** 28.2% vs 25.1%: +3.1 pp [−5.4, 11.1]. For 2024–26: +4.4 pp [−5.4, 13.6]. The accepted excess shrinks as data accrue.

**Flips (pooled).**

| Feature | Net-flip DiD (pp) [95%] | Note |
|---|---|---|
| NAME | **+1.29 [−2.87, 5.44]** | Accepted 71 v1-present, +9/−7; rejected 53, +2/−3. Tip 2.92 pp, so **not identified**. Audit-implied G_dec [0.953, 1.097] |
| Compound | −0.86 [−5.56, 3.85] | |
| Title Case | +1.21 [−3.14, 5.57] | |
| Mixed-case name | +1.14 [−2.34, 4.63] | |
| 'via' | +1.29 [−2.30, 4.87] | |
| O-union | +1.07 [−3.00, 5.14] | |

**Auditability.**
- The same 10 features are auditable.
- 'using' (5/8), R26 (8/0) and title typography (0/0) remain unauditable.
- R24 (11/4) and the LLM slot word (10/2) now reach 10 accepted v1 titles but not 10 rejected ones.
- **No acceptance association is identified.**

**Gate.** The H4a NAME G_total gate passes with the enlarged audit (§5).

**Fragility.** Flips are rare events. Between a run with the first 248 and the first 254 enlargement records, the NAME DiD moved from +1.89 [−2.17, 5.94] to +1.29 [−2.87, 5.44] pp. Results that use the partial enlargement are interim; rerun `snapshot_bounds.py` when the background job completes.

---

## Deviations from PLAN.md (logged)

1. **CI for the net-flip DiD.**
   - The PLAN does not fix the CI type.
   - The primary CI is a Wald interval with a pseudo-flip variance floor, because plain Wald SEs are 0 for zero-flip arms.
   - Plain Wald and a stratified bootstrap (2,000 replicates, year × decision strata) are reported. No identification verdict changes between them.
2. **Auditability rule.**
   - This module uses ≥ 10 v1-present titles in *both* arms.
   - D4's interim rule (≥ 10 accepted v1-present and ≥ 10 accepted stored-present) also admits L-title and LLM-abbrev-only. Neither would be identified under it either.
3. **Tipping point regenerated at 2.92 pp** against the pilot's 1.8 pp. The cause is pooling: year-standardised 2024–26, as in D4.
4. **V7 retrieval key.**
   - PLAN: "surname plus the first abstract sentence". The task brief: "surname plus distinctive abstract words".
   - Phrase search on a full sentence fails after any rewording, so three corpus-rare abstract words are used. Title words are excluded to keep the route title-free, with a 2-word fallback.
   - Tier C was added after a pilot query showed that OpenReview abstracts are often rewritten (Jaccard 0.18 for a correct hit). Its false-positive rate in validation was 1 of 2, so strict-tier results are reported.
   - Route B uses an ASCII-transliterating surname helper. The original helper splits accented names, e.g. "Bošnjak" becomes "njak". The enlargement keeps the original helper so that it can be pooled with the original audit.
5. **Extension: arXiv v1 abstracts** were fetched for the original pre-decision pairs to audit abstract markers (F24, F26, em dash). This is not in the PLAN. arXiv cannot carry Unicode dash typography, so only the word markers are auditable this way.
6. **Enlargement.**
   - Target: 250 per year × decision cell for 2023–26 (2,000 papers), title route identical to the original.
   - Written to a new file, `cache/arxiv_audit_enlarge.jsonl`; `cache/arxiv_audit.jsonl` is untouched.
   - The queue is interleaved across cells so that a partial run stays balanced.
   - At the freeze, 254 of 2,000 papers were done. The job keeps running in the background.
   - The PLAN's enlargement rate (~1k papers/hour) is infeasible under the 3.2 s rate limit; the observed rate is about 375 papers/hour.
7. **IPW models** are fitted on 2023–26 (600 papers), because 2022 has accepted papers only.
8. **G intervals clip D to the feasible range** [P₃ − 1, P₃]. Without this, rare features produce negative or undefined G values.
9. **Tipping points for H4a's per-year claims 2018–2023 are not computable.** The audit covers 2022–26 only.
10. **Note for D4.** `d4_filter/audit_pairs.csv` reads `arxiv_id` with `pd.read_json`, which parses ids as floats: 2309.02390 becomes 2309.0239. This does not affect D4's features. This module reads the JSONL with the `json` module.

## Limitations

- **Sample size.** With 206 accepted and 125 rejected usable pairs, the audit's net-flip CIs (about ±5 pp) are wider than every mainstream tipping point (0.3–3.3 pp). "Not identified" is a statement about the audit, not evidence that editing explains the associations.
- **arXiv v1 is not the submitted OpenReview title.**
  - v1 can predate submission, as an earlier draft, or be posted during review.
  - The rejected arm absorbs this only if the v1-vs-OpenReview divergence is the same for accepted and rejected papers. Accepted papers may post earlier or later.
  - Pre-decision v1 timing given found does not differ by decision (OR 1.04), which supports, but does not prove, comparability.
- **Selection on observables only.** Findability IPW corrects for year, decision, title length and NAME. Unobserved differences between arXiv-posting and non-posting rejected papers (e.g. resubmission plans) remain.
- **Abstract audit caveats.** The arXiv v1 abstract may differ from the OpenReview submission abstract for reasons common to both arms. The DiD removes common noise but not decision-specific posting behaviour.
- **Gate verdicts depend on 2024–26 pooling.** Per-year bounds are uninformative at the current size.

## Interface for D4 (WP8)

- `T4_2_flip_matrices.csv`, rows `spec == 'primary'`: the canonical net-flip DiD per feature. Columns `did`, `did_lo`, `did_hi` (pseudo-flip 95%), `did_lo_wald` / `did_hi_wald`, `did_lo_boot` / `did_hi_boot`, `auditable`.
- `T4_2_tipping_points.csv`: G_dec and G_total, tipping points, audit-implied intervals, combined corrected CIs, identification flags. 2024–26 pooled, year-standardised as in D4.
- `gate.csv`: gate verdicts for the H4a and H4b claims.

## Files

**Scripts:**
- `src/analyses/snapshot_bounds.py`
- `src/analyses/audit_v2.py`

**Caches** (written by `audit_v2.py`):
- `cache/arxiv_audit_route.jsonl`
- `cache/arxiv_audit_v1abs.jsonl`
- `cache/arxiv_audit_enlarge.jsonl`
- background log: `outputs/snapshot/audit_v2.log`

**Tables:**
- `audit_pairs.csv`, `found_rates.csv`, `findability_models.csv`, `retitling.csv`
- `T4_2_flip_matrices.csv`, `T4_2_flip_multiclass.csv`
- `T4_2_tipping_points.csv`, `T4_2_tipping_by_year.csv`, `T4_2_identification_by_spec.csv`
- `abstract_audit.csv`, `gate.csv`
- `route_validation.csv`, `route_pairs.csv`
- `results.json`, `snapshot_bounds.log`

**Figures** (each as PDF + PNG + CSV):
- **Fig. S1** `fig_S1_findability_retitling`: findability and retitling by year × decision.
- **Fig. S2** `fig_S2_tipping_points`: T4.2 visual, net-flip DiD vs tipping point, and audit-implied G_dec.
- **Fig. S3** `fig_S3_route_validation`: V7.
- **Fig. S4** `fig_S4_drop_rates`: drop rates with feature-present denominators.
