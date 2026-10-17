# G4: LLM-favoured title words and citations

**Code:** `src/cites/g4.py`. **Numbers:** `outputs/cites/G4/results.json`. **Figure:** `outputs/cites/G4/fig.png`.
**Pre-registration:** `docs/CITES_PREREG.md` (frozen 2026-10-17). **Frozen core:** `src/cites/core.py` (not edited).

## Question

Among accepted ICLR papers from 2017 to 2025, do papers whose titles use LLM-favoured words get more or fewer Semantic Scholar citations than accepted papers with similar content? The words are enhancing, leveraging, unveiling, unleashing, harnessing, empowering, elevating and boosting.

- **Feature.** `G4_llm_words` = `r24_any`. It is 1 when the title contains a word from any of 8 stem families: enhanc\*, leverag\*, unveil\*, unleash\*, harness\*, empower\*, elevat\*, boost\*.
- **Sample.** 8,602 accepted papers matched to an S2 venue record.
  - 8,574 papers enter the regression; singleton year × topic50 cells are dropped.
  - 273 papers (3.2%) have an LLM-favoured word.
  - These titles are recent: 241 of the 273 (88%) are from 2023–25, and 220 (81%) are from 2024–25.
  - Count by year, 2017–25: 0, 4, 3, 4, 12, 9, 21, 80, 140.
- **Outcome.** y = log(1 + citations), with citations retrieved 2026-10-17.
- **Model.** `y ~ G4 + log(team size) + log(abstract words) + 20 abstract-embedding PCs | year × topic50`, with SEs clustered by topic50.
- **Effect scale.** % difference = exp(b) − 1.

## Primary estimate (pre-registered)

| | % difference in citations | 95% CI | p | Holm p (8 tests) | n | n with feature |
|---|---|---|---|---|---|---|
| G4 LLM-favoured words | **−9.0%** | −20.7% to +4.3% | 0.18 | **0.36** | 8,574 | 273 |

- The estimate and Holm p are taken from `outputs/cites/primary.json`.
- Re-computing them with `core.primary` reproduces the estimate exactly: largest absolute difference 0, same n.

## Robustness checks R1–R7 (pre-registered, `core.robustness`)

| Check | % difference | 95% CI | p | n |
|---|---|---|---|---|
| Primary | −9.0% | −20.7, +4.3 | 0.18 | 8,574 |
| R1 content-matched pairs (name-masked embedding, cosine ≥ 0.80) | −30.5% | −43.9, −13.9 | (bootstrap) | 273 pairs |
| R2 PPML on raw counts (sign check only) | +2.1% | −30.7, +50.5 | 0.92 | 8,574 |
| R3 influential-citation count | −10.0% | −20.5, +1.9 | 0.10 | 8,574 |
| R4 drop top 1% most-cited per year | −10.9% | −22.2, +2.1 | 0.10 | 8,481 |
| R5 2017–21 only | −6.8% | −40.6, +46.1 | 0.76 | 1,975 |
| R5 2022–25 only | −9.0% | −21.0, +4.7 | 0.19 | 6,599 |
| R6 2022–25 + team's prior ICLR acceptances | −7.9% | −20.0, +5.9 | 0.25 | 6,599 |
| R7 year + topic100 FE | −11.8% | −24.0, +2.4 | 0.11 | 8,602 |

- **R3–R7.** All are between −7% and −12%, and every CI includes 0.
- **R2 (PPML, a sign check).** It is slightly positive, +2.1%, so its sign is opposite to the primary.
- **R1.** It is more than three times the size of the primary. The R1 calibration diagnostic (d) below shows that the R1 procedure itself is shifted by about −20% in this design: under no association it produces −20.5% on average. Corrected for this shift, R1 is −12.5% (−29.3, +8.4).

## Verdict (pre-registered rule)

**"Inconclusive."**

- **Not "fewer citations".** That label needs Holm p < 0.05, and Holm p is 0.36. The sign condition also fails: R2 PPML is +2.1%, against the primary's −9.0% (R1 does have the same sign).
- **Not "no meaningful difference".** That label needs the 95% CI to lie within ±10%. The CI is −20.7% to +4.3%, and its lower end is below −10%.

The data fit anything from about 21% fewer to 4% more citations. A modest negative association cannot be ruled out, and no difference cannot be established.

## Secondary analyses (pre-specified in prereg section 6; no multiplicity claim)

### Each word family separately

This is one model with all 8 family dummies, so the reference group is exactly the papers with no LLM-favoured word. 11 titles contain two families.

| Family | n (2023–25) | % difference vs no LLM word | 95% CI | p |
|---|---|---|---|---|
| enhanc\* | 131 (123) | +2.0% | −18.5, +27.7 | 0.86 |
| boost\* | 55 (41) | −30.2% | −47.7, −6.9 | 0.018 |
| leverag\* | 40 (34) | −33.5% | −50.3, −11.2 | 0.008 |
| empower\* (n < 20, not interpreted) | 19 (17) | +53.2% | −22.3, +202.2 | 0.22 |
| harness\* (n < 20, not interpreted) | 17 (15) | +14.4% | −30.2, +87.4 | 0.60 |
| unveil\* (n < 20, not interpreted) | 10 (10) | −50.7% | −80.7, +25.7 | 0.15 |
| unleash\* (n < 20, not interpreted) | 10 (10) | +7.9% | −29.7, +65.6 | 0.73 |
| elevat\* (n < 20, not interpreted) | 2 (2) | +136.3% | +44.8, +285.4 | 0.001 |

- **enhanc\*.** The most common family, about half of all G4 titles, shows no difference: +2.0% (−18.5, +27.7).
- **leverag\* and boost\*.** Both are negative (−34% and −30%), with nominal p < 0.05.
  - These secondary tests carry no multiplicity correction.
  - A descriptive Holm across the 8 families gives 0.057 for leverag\* and 0.11 for boost\*. Diagnostic (not pre-registered).
  - Calibrated content-matched pairs do not confirm either one (diagnostic (d)).
  - Treat them as hypotheses, not findings.
- **Families with n < 20** are reported but not interpreted. This is the same n ≥ 20 threshold the prereg uses for G6 templates. The elevat\* estimate rests on 2 papers.

### Pre-2023 vs 2023+

| Period | n | n G4 | % difference | 95% CI | p |
|---|---|---|---|---|---|
| 2017–2022 | 2,825 | 32 | −4.6% | −36.2, +42.7 | 0.82 |
| 2023–2025 | 5,749 | 241 | −9.1% | −21.7, +5.6 | 0.22 |

- **Difference (2023+ vs pre-2023).** Ratio of multipliers 0.95 (0.61, 1.48), p 0.83.
  - This is one pooled model with all controls interacted with period. Its point estimate equals the split-sample difference.
- The pre-2023 group has only 32 papers. These data cannot say whether the association changed once these words became associated with LLM writing.

### Joint model with all 8 primary features (all questions)

- G4 is −7.9% (−19.8, +5.7), p 0.25.
- Adjusting for the other title features (name, question, length, informativeness, templates) changes little.

### Heterogeneity by LLM-topic papers (all questions)

| Group | n G4 | % difference | 95% CI |
|---|---|---|---|
| LLM-topic papers | 92 | −1.4% | −25.9, +31.2 |
| other papers | 181 | −12.8% | −25.8, +2.4 |

The ratio of the two multipliers is 1.13 (0.80, 1.59), p 0.49, so there is no evidence of a difference.

## Diagnostics — diagnostic (not pre-registered)

### (a) Artefact check: S2 split records and arXiv ids

S2 sometimes keeps a venue record without an arXiv id separate from the arXiv record, and the arXiv record collects the citations. A record without an arXiv id is therefore under-counted, and G4 papers have fewer arXiv ids.

- **arXiv-id share among matched records.**
  - G4 70.7% (n 273) vs other 77.0% (n 8,329).
  - Within year: −5.6 pp (−10.2, −1.0), p 0.021.
  - With the primary controls: −5.4 pp (−9.9, −0.9), p 0.022.
  - Among years with many G4 papers, the gap is largest in 2025: 65.0% vs 73.6% (2024: 73.8% vs 80.4%).
- **Size of the arXiv-id gap in citations.** Records with an arXiv id have far more citations: +214% (+174, +260) with the primary controls.
  - This mixes the split-record artefact with the real difference between papers posted and not posted to arXiv.
  - In the QC sample (`qc_split_records.jsonl`), 7 of 30 records without an arXiv id were split. Only 1 of the 30 was a G4 paper, so the sample cannot compare by G4.
- **S2 match rate does not differ.** G4 97.5% (n 280) vs other 96.9% (n 8,593) of accepted papers 2017–25. Within year the difference is +0.6 pp (−1.3, +2.5), p 0.52.
- **Primary spec on records with an arXiv id only.** −11.5% (−24.2, +3.2), n 6,575, 193 G4.
- **Records without an arXiv id only.** +17.5% (−14.5, +61.5), n 1,926, 80 G4.
- **Difference between the two subsets, in one model.** Ratio 1.33 (0.92, 1.91), p 0.13. In this model the controls and FE are interacted with arXiv status, as in G1.
- **Primary spec plus an arXiv-id indicator.** −3.2% (−14.4, +9.5), p 0.61.

**Reading.**
- With an arXiv-id indicator, about two-thirds of the primary's (non-significant) negative point estimate disappears.
- Among arXiv-linked records alone, where split records are not an issue, the estimate is −11.5%, close to the primary. So the split-record artefact does not, by itself, produce the negative point estimate.
- No version is distinguishable from zero. The point estimate depends on how arXiv status is handled.

### (b) Topic composition

- **Share of LLM-topic papers.** 33.7% of G4 papers vs 22.1% of other papers.
  - Within year: +4.1 pp (−1.5, +9.8), p 0.16.
  - Within year × topic50: −0.1 pp (−2.7, +2.5), p 0.94.
  - So the raw gap comes from timing: G4 titles cluster in 2024–25, when LLM topics are common. The primary FE absorb it.
- **G4 rate per 1,000 titles.**
  - 2017–22: 11.0 in non-LLM papers (29 of 2,632) and 13.6 in LLM-topic papers (3 of 221).
  - 2023–25: 37.6 (152 of 4,039) and 52.0 (89 of 1,710).
- **Primary spec plus an llm_topic indicator.** −9.2% (−20.9, +4.4), unchanged. llm_topic varies within the FE cells that hold 218 of the 273 G4 papers.
- **Identification.**
  - All 273 G4 papers sit in year × topic50 cells that also contain papers without the feature (117 of 404 cells contain G4 papers). No cell holds more than 3.3% of the G4 papers.
  - The 5 topic50 clusters with the most G4 papers hold 23.1% of them and 16.3% of all papers.
  - The top cluster (topic 43, 81% LLM-topic, e.g. "MiniGPT-4: Enhancing Vision-Language Understanding…") has 15 G4 papers. That is 5.5% of G4 vs 2.4% of all papers.

**Reading.** Topic composition does not explain the estimate. G4 papers are compared within year × topic cells, and the association does not depend on the LLM-topic indicator.

### (c) Word sense

Some matches are technical terms, not style choices: the boosting algorithm family ("gradient boosting", "boosted trees") and "empowerment" in RL.

- **Recoding.** 14 such titles are recoded to G4 = 0 (listed in `results.json`). 10 of them date from before 2024.
  - G4 by stylistic sense: −7.3% (−19.6, +6.8), 259 G4, p 0.30.
  - The same, 2023+ only: −8.0% (−21.0, +7.0), 235 G4.
- **G4 without the boost\* and elevat\* families.** This is the `r24_noamb` variant used in D3: −3.6% (−18.3, +13.9), 219 G4, p 0.67.
- **boost\* split by sense in the family model.**
  - Stylistic sense (e.g. "Boosting X via Y"): −30.1% (−49.8, −2.7), n 43.
  - Technical sense: −30.5% (−60.1, +21.0), n 12.
  - The negative boost\* estimate therefore does not come from gradient-boosting papers.

### (d) R1 calibration: why is R1 more than three times the primary?

- **Placebo.** We took random papers without the feature, with the same counts per year as the 273 G4 papers, labelled them "treated" and ran the R1 matching on them. We repeated this 200 times.
  - With no true association, R1 should centre on 0. Instead it gives **−20.5% on average**, with a null 95% range of −34.7% to −0.4%.
  - The observed −30.5% lies inside that null range: placebo p = 0.22.
  - Placebo-adjusted R1 is **−12.5% (−29.3, +8.4)**. The approximate SE is the placebo SD of the R1 statistic.
- **Mechanism.** The nearest-neighbour controls are not typical papers.
  - On average they sit 0.27 log points above the mean (for papers without the feature) of their own year × topic50 cell, about 31% more citations. The G4 papers sit 0.07 below.
  - One reading: being a paper's nearest neighbour in the embedding selects papers from dense, well-cited regions. This was not tested further.
  - Only 64% of pairs share a topic50 cluster. There are 260 distinct controls for 273 pairs.
- **Pair-level adjustment.** Adjusting for within-pair differences in log team size, log abstract words and arXiv id gives −23.7% (−37.6, −6.6). This still carries the placebo shift; within pairs the G4 paper is 7.0 pp less likely to have an arXiv id.
- **Calipers.** Cosine ≥ 0.85 gives −29.1% (−44.9, −9.5) with 216 pairs. Cosine ≥ 0.90 gives −11.6% (−43.4, +38.2) with 75 pairs.
- **Families with n ≥ 20, same placebo.**

  | Family | Pairs | Observed R1 | Null mean | Placebo-adjusted | 95% CI | Placebo p |
  |---|---|---|---|---|---|---|
  | enhanc\* | 131 | −30.1% | −20.4% | −12.2% | −35.9, +20.2 | 0.46 |
  | leverag\* | 40 | −50.3% | −21.1% | −37.0% | −64.1, +10.6 | 0.14 |
  | boost\* | 55 | −49.1% | −19.8% | −36.6% | −61.5, +4.4 | 0.06 |

**Reading.**
- Raw R1 overstates the negative association. Once calibrated, R1 agrees with the primary in sign and rough size, and its CI includes 0.
- The verdict does not change: it already fails on Holm p.
- **The shift is a property of the R1 procedure, not of G4.** It likely affects R1 for every G-question: it pushes R1 down, so it understates positive associations and overstates negative ones. It should be checked wherever R1 is used as a verdict input.

### (e) Team prior (pre-registered R6 compared with R5 on the same 2022–25 sample)

- Without the team-prior control (R5): −9.0% (−21.0, +4.7).
- With it (R6): −7.9% (−20.0, +5.9). The change in b is +0.012.
- G4 teams have about the same prior ICLR record: mean log(1 + prior acceptances) 1.07 vs 1.04.

## Interpretation and caveats

- **Observational.** Authors choose titles. Teams that use these words may differ in ways the content controls do not capture: writing assistance, research community, promotion. None of the above shows that using or avoiding these words changes a given paper's citations.
- **Imprecise.** There are only 273 G4 papers, and 88% are from 2023–25. For 2024–25 papers (81% of G4), citations cover only 1–2 years. Year FE compare like with like, but the association may change as citations accrue.
- **Selection into the sample.** Only accepted papers are included.
  - On the reviewer side, no title feature's acceptance association survives the camera-ready audit (0 of 18 auditable features pass; `outputs/SUMMARY.md`).
  - For R24 words specifically, desk rejection and withdrawal deplete them before the decision, as they did before 2024: pre-decision ratio 0.900 [0.870, 0.931] (SUMMARY.md, finding 9).
  - Accepted G4 papers are therefore a filtered subset of G4 submissions. This study cannot say whether that filter removes weaker or stronger papers on citations.
  - Titles that go with fewer or more citations are not the same as titles that reviewers penalise.
- **Measurement.**
  - G4 is a stem regex on the camera-ready title, so it includes some technical uses (diagnostic (c)) and does not separate LLM-assisted writing from authors' own word choice.
  - The feature is not LLM-use detection.
- **Artefact sensitivity.** G4 papers have 5–6 pp fewer arXiv ids. With an arXiv-id indicator the point estimate moves from −9.0% to −3.2%, though among arXiv-linked records alone it is −11.5% (diagnostic (a)).
- **R1 is shifted negative by construction in this design** (diagnostic (d)). This matters beyond G4.
- **Labels.** Secondary analyses (families, era, joint model, LLM heterogeneity) carry no multiplicity correction. **Diagnostics** were added after seeing the primary and are labelled as such. The family-level contrasts for leverag\* and boost\* are hypotheses only.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles use LLM-favoured words (enhancing, leveraging, boosting, …) receive about 9% fewer citations on average, but the 95% CI runs from 21% fewer to 4% more and the pre-registered verdict is inconclusive, so these data neither establish nor rule out a modest citation shortfall for such titles.
