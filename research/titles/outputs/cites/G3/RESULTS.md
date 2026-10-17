# G3: question titles and citations

**Code:** `src/cites/g3.py`. **Numbers:** `outputs/cites/G3/results.json`. **Figure:** `outputs/cites/G3/fig.png`.
**Pre-registration:** `docs/CITES_PREREG.md` (frozen 2026-10-17). **Frozen core:** `src/cites/core.py` (not edited).

## Question

Among accepted ICLR papers from 2017 to 2025, do papers whose title is a direct question, or contains one, get more or fewer Semantic Scholar citations than accepted papers with similar content? Examples: "How Powerful are Graph Neural Networks?" and "SWE-bench: Can Language Models Resolve Real-world Github Issues?".

- **Sample.** 8,602 accepted papers matched to an S2 venue record.
  - 8,574 papers enter the regression; singleton year × topic50 cells are dropped.
  - 223 of the papers (2.6%) have a question title.
  - 86 of the 223 (39%) are from 2025.
- **Feature.** `G3_question` = the title contains "?" (`features.py`).
- **Outcome.** y = log(1 + citations), with citations retrieved 2026-10-17.
- **Model.** `y ~ G3_question + log(team size) + log(abstract words) + 20 abstract-embedding PCs | year × topic50`, with SEs clustered by topic50.
- **Effect scale.** % difference = exp(b) − 1.

## Primary estimate (pre-registered)

| | % difference in citations | 95% CI | p | Holm p (8 tests) | n | n question |
|---|---|---|---|---|---|---|
| G3 question title | **+14.3%** | −2.8% to +34.5% | 0.113 | **0.348** | 8,574 | 223 |

- The estimate and Holm p are taken from `outputs/cites/primary.json`.
- Re-computing them with `core.primary` reproduces the estimate exactly: largest absolute difference 0, same n and n question.
- The Holm p is not 3 × 0.113 = 0.339. Holm's step-down monotonicity sets it equal to the adjusted p of the test ranked just before it (G5a, 0.348).

## Robustness checks R1–R7 (pre-registered, `core.robustness`)

| Check | % difference | 95% CI | p | n |
|---|---|---|---|---|
| Primary | +14.3% | −2.8, +34.5 | 0.113 | 8,574 |
| R1 content-matched pairs (name-masked embedding, cosine ≥ 0.80) | **−3.7%** | −26.1, +23.7 | (bootstrap) | 221 pairs |
| R2 PPML on raw counts (sign check only) | +21.3% | −33.2, +120.4 | 0.53 | 8,574 |
| R3 influential-citation count | +5.4% | −11.4, +25.5 | 0.55 | 8,574 |
| R4 drop top 1% most-cited per year | +11.0% | −5.1, +30.0 | 0.20 | 8,481 |
| R5 2017–21 only (39 question titles) | −2.7% | −33.5, +42.6 | 0.89 | 1,975 |
| R5 2022–25 only (184 question titles) | +15.8% | −1.8, +36.6 | 0.088 | 6,599 |
| R6 2022–25 + team's prior ICLR acceptances | +15.2% | −2.1, +35.5 | 0.094 | 6,599 |
| R7 year + topic100 FE | +14.9% | −3.1, +36.1 | 0.12 | 8,602 |

- **No check excludes zero.**
- R4, R6 and R7 are within about 3 points of the primary.
- R3 (influential citations) is smaller, at +5%.
- R1 (matched pairs) and R5 2017–21 have the opposite sign. Both rest on few papers, and their CIs span roughly ±25 to ±40 points.
  - The R1 procedure itself is shifted downward. With no true association it gives about −22% (audit diagnostic (f)).
  - Placebo-adjusted, R1 is **+23% (−4, +57)**, the same sign as the primary. This is a diagnostic; the verdict rule uses raw R1.
- R2 is positive but uninformative: its CI runs from −33% to +120%.
  - Its sign rests on one paper, GIN (10,670 citations). Without GIN, PPML gives −10.3% (−37.9, +29.6). With the top 1% per year dropped, it gives −19.0% (−36.2, +2.7) (audit diagnostic (g)).

## Verdict (pre-registered rule)

**"Inconclusive."**

- **"More citations" fails.** That verdict needs Holm p < 0.05, but Holm p = 0.348. R1 also has the opposite sign (−3.7%), so the sign condition fails too. R2 has the same sign.
  - Both sign checks are weak here. Raw R1 is shifted about −22% by construction, and R2's sign rests on GIN alone (audit diagnostics (f) and (g)).
  - The verdict does not depend on either, because Holm p fails.
- **"No meaningful difference" fails.** The 95% CI (−2.8% to +34.5%) is not inside ±10%.
- **That second verdict was unattainable here.** With 223 question titles, the 95% CI is wider than the ±10% band whatever the point estimate (see diagnostic (c)).

## Secondary analyses (pre-specified in prereg section 6; no multiplicity claim)

**Joint model with all 8 primary features.**

- G3 is **+27.2% (+6.6, +51.8)**, p 0.010, n 8,574.
- In this model the comparison group changes. G2 ("assertive") is defined as "assertive verb and not a question", so G2 and G3 never co-occur, and only 6% of question titles are named (G1) against 25% of other titles. G1 and G2 both go with more citations: +22% and +26% in their own primary models.
- So the joint model compares question titles with "plain" titles: not named, not assertive and without the other features. The primary compares them with all other titles.
- This is a secondary result without multiplicity control. The matched-pairs version of this comparison, diagnostic (e), does not reproduce it: −6.0%.
  - That matched-pairs figure is raw. It carries the same downward shift of about 22% as R1 (audit diagnostic (f)), so it is not evidence against the joint-model estimate either.

**Heterogeneity by LLM-topic papers.** Question titles are more common among LLM-topic papers: 36.8% of question titles vs 22.1% of other titles.

| Group | % difference | 95% CI | p | n question |
|---|---|---|---|---|
| LLM-topic papers | −1.9% | −23.2, +25.3 | 0.88 | 82 |
| other papers | +25.5% | +1.7, +55.0 | 0.040 | 141 |

The ratio of the two multipliers is 0.78 (0.56, 1.09), p 0.15, so there is no evidence of a difference between the groups. The p = 0.040 for non-LLM papers is one of several uncorrected subgroup tests and should not be read as a finding.

## Diagnostics — diagnostic (not pre-registered)

### (a) Artefact check: arXiv-id share by question status

S2 sometimes keeps a venue record without an arXiv id separate from the arXiv record, and the arXiv record collects the citations. A different share of such records in one group would bias the comparison.

| | Question titles | Other titles |
|---|---|---|
| Venue record has an arXiv id | **78.5%** (175/223; Wilson 72.6–83.4) | **76.8%** (6,435/8,379) |
| 2017–21 | 76.9% (30/39) | 79.0% |
| 2022–25 | 78.8% (145/184) | 76.1% |
| Zero citations | 3.6% (8/223) | 4.1% |
| Several S2 matches | 0% | 0.17% |

- **Adjusted difference in arXiv-id share** (primary controls and FE, linear probability): +0.9 pp (−4.4, +6.3), p 0.73.
- **Primary spec on records with an arXiv id only.** +15.7% (−3.1, +38.2), n 6,575, 175 question titles.
- **Records without an arXiv id only.** +9.9% (−26.9, +65.2), n 1,926, 48 question titles.
- **Primary spec plus an arXiv-id indicator.** +13.1% (−3.5, +32.6).
- **Difference between the two subsets, in one model.** Ratio 0.95 (0.64, 1.42), p 0.80. In this model the controls and FE are interacted with arXiv status, as in G1.
- **Split-record QC sample** (`qc_split_records.jsonl`, 30 records checked, 7 split). It contains a single question title, which is not split, so the sample cannot speak to G3.

**Reading.**
- The split-record artefact is not differential by question status, so it does not explain the estimate.
- It does add noise to the outcome: see the least-cited list in (b), where 13 of 15 records have no arXiv id.

### (b) Measure validity: most- and least-cited question titles

The ranking uses the within-year citation percentile among all 8,602 papers. Full records, with flags, are in `results.json`.

**Most cited (top 15):**

| Year | Citations | Pctile | Title |
|---|---|---|---|
| 2024 | 4,404 | 0.999 | SWE-bench: Can Language Models Resolve Real-world Github Issues? |
| 2019 | 10,670 | 0.998 | How Powerful are Graph Neural Networks? |
| 2022 | 2,162 | 0.993 | How Attentive are Graph Attention Networks? |
| 2024 | 1,286 | 0.991 | Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs |
| 2025 | 456 | 0.991 | Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge |
| 2025 | 322 | 0.986 | MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans? |
| 2022 | 727 | 0.970 | How Do Vision Transformers Work? |
| 2023 | 766 | 0.967 | When and Why Vision-Language Models Behave like Bags-Of-Words, and What to Do About It? |
| 2025 | 171 | 0.962 | Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs |
| 2022 | 526 | 0.959 | How Much Can CLIP Benefit Vision-and-Language Tasks? |
| 2025 | 142 | 0.951 | Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models |
| 2019 | 988 | 0.948 | What do you learn from context? Probing for sentence structure in contextualized word representations |
| 2025 | 133 | 0.945 | Round and Round We Go! What makes Rotary Positional Encodings useful? |
| 2019 | 917 | 0.943 | Do Deep Generative Models Know What They Don't Know? |
| 2024 | 304 | 0.937 | Can LLM-Generated Misinformation Be Detected? |

**Least cited (bottom 15):**

| Year | Citations | Pctile | arXiv id on record | Title |
|---|---|---|---|---|
| 2022 | 0 | 0.008 | no | Should We Be Pre-training? An Argument for End-task Aware Training as an Alternative |
| 2024 | 0 | 0.020 | no | When should we prefer Decision Transformers for Offline Reinforcement Learning? |
| 2021 | 3 | 0.025 | yes | What Can You Learn From Your Muscles? Learning Visual Representation from Human Interactions |
| 2025 | 0 | 0.042 | no | DSBench: How Far Are Data Science Agents from Becoming Data Science Experts? |
| 2025 | 0 | 0.042 | no | Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs |
| 2025 | 0 | 0.042 | no | Model Equality Testing: Which Model is this API Serving? |
| 2025 | 0 | 0.042 | no | Does Spatial Cognition Emerge in Frontier Models? |
| 2025 | 0 | 0.042 | no | What's the Move? Hybrid Imitation Learning via Salient Points |
| 2025 | 0 | 0.042 | no | SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? |
| 2024 | 1 | 0.049 | no | What does automatic differentiation compute for neural networks? |
| 2024 | 1 | 0.049 | no | What's In My Big Data? |
| 2022 | 5 | 0.066 | no | How Did the Model Change? Efficiently Assessing Machine Learning API Shifts |
| 2024 | 2 | 0.070 | no | Does Progress On Object Recognition Benchmarks Improve Generalization on Crowdsourced, Global Data? |
| 2023 | 4 | 0.084 | no | When to Make and Break Commitments? |
| 2023 | 4 | 0.084 | yes | How Informative is the Approximation Error from Tensor Decomposition for Neural Network Compression? |

**Reading.**
- **The feature is valid.** All 30 titles are genuine direct questions.
- **The feature is measured accurately.**
  - In the V1 validation (two blind LLM annotation passes, adjudicated consensus; all ICLR submissions 2017–26; `outputs/validation`), the "?" rule had 0 false positives among 24 detected questions and 2 false negatives among 1,400 items.
  - Both false negatives are titles that pose a question without a "?", for example "What About Taking Policy as Input of Value Function: …".
  - Unweighted Wilson 95% CIs on the consensus items: precision 100% (86–100%), recall 92% (76–98%). The stratified estimator's precision CI of 100–100% understates the uncertainty, because there are so few positive items.
  - No title has a "?" between two letters, which would suggest an encoding artefact. One title has two "?".
- **The top of the list is mostly analysis, evaluation and benchmark papers.** 10 of the 15 are LLM-topic papers, 2 are benchmarks with a name prefix, and all 15 have an arXiv id. A few very large counts drive the mean: GIN has 10,670 citations and SWE-bench 4,404.
- **The bottom of the list is mostly a measurement problem with the outcome, not the feature.**
  - 13 of the 15 venue records have no arXiv id, and all 15 have 0–5 citations.
  - Several are papers we would expect to be cited, for example "SWE-bench Multimodal" and "What's In My Big Data?". That pattern matches the split-record artefact.
  - We did not verify this against external data, which the rules exclude. Per (a), the artefact is not differential by G3, so it widens the CI rather than shifting it.
- **Raw within-year percentile** (no controls): question titles have median 0.59, other titles 0.50.

Question forms, descriptive only (counts and raw median within-year percentile; cells are too small for inference):
- main-clause yes/no questions: 91 (0.55);
- main-clause wh- questions: 78 (0.64);
- other openers: 21 (0.55);
- questions after a colon, in the second part of the title: 33. Only 14 of these follow a coined name (e.g. "SWE-bench: Can …?"). The other 19 follow a descriptive phrase (e.g. "Permutation-Based SGD: Is Random Optimal?").
  - Audit correction: an earlier version called all 33 "questions after a 'NAME:' prefix".

### (c) Power and fragility (n = 223)

**Power.**
- **Precision of the primary.** SE(b) = 0.083, so the 95% CI half-width is 0.163 log points.
- **Minimum detectable effect at 80% power.**
  - +26% at α = 0.05;
  - +31% at α = 0.0167, the Holm threshold at G3's rank (6th of 8 p-values);
  - +35% at α = 0.00625 (Bonferroni).
  - In the negative direction: −21%, −24% and −26%.
- **Power for a true difference.**
  - True +20%: 59% (α 0.05), 42% (α 0.0167), 30% (α 0.00625).
  - True +10%: 21%, 11%, 6%.

**The ±10% "no meaningful difference" band was out of reach.**
- The 95% CI is 0.325 log points wide; the ±10% band is 0.201 wide. So the CI could not fit inside the band whatever the point estimate.
- For the CI to fit at all, SE ≤ 0.051 would be needed.
- For an 80% chance of the CI landing inside the band when the true difference is 0, SE ≈ 0.031 would be needed. That means roughly **1,600–2,800 question titles**, about 7–12 times as many as now.
  - This is a rough estimate. It assumes the SE scales as 1/√n, or with the empirical slope of −0.39 across the six binary primary features.
- At this sample size the realistic verdicts were "inconclusive", or "more/fewer" for differences of about 30% or more.

**Fragility.**
- **Dropping the k most-cited question titles.** This check is one-sided and biased downward by construction: k = 1: +12.8%; 3: +9.7%; 5: +7.0%; 10: +1.9%; 20: −5.8%.
- **Symmetric trim** (the k highest and the k lowest): k = 1: +15.1%; 3: +14.8%; 5: +15.7%; 10: +20.2% (+3.0, +40.3); 20: +22.7% (+3.7, +45.3).
- **Reading.**
  - The point estimate is sensitive to a handful of very highly cited question papers: removing 5 of 223 halves it.
  - The low tail, which the split-record artefact inflates, pulls the estimate down, so trimming both tails raises it.
  - These are post-hoc trims chosen after seeing the data. They show how fragile the estimate is, not that a positive association exists.

### (d) Overlap with other title features and paper type

**Overlap with other title features.**
- 14 of 223 question titles are named (6.3%), against 25.0% of other titles.
- By definition, 0 are assertive (G2).
- 10 are meme templates, 7 of them "Do X really …?". 5 contain LLM-favoured words. 1 is tentative.

**Robustness to that overlap.**

| Variant | % difference | 95% CI | n question |
|---|---|---|---|
| + G6a meme control | +13.1% | −4.0, +33.2 | 223 |
| meme titles excluded | +12.0% | −5.7, +33.2 | 213 |
| + G1 named control | +18.3% | +0.5, +39.3 | 223 |
| named titles excluded | +16.4% | −2.7, +39.2 | 209 |
| assertive titles excluded (reference = neither question nor assertive) | +17.7% | −0.6, +39.4 | 223 |
| + method-paper indicator | +14.8% | −2.6, +35.2 | 223 |

**Paper type.**
- The method-paper indicator is set when the abstract says "we propose", "we introduce", "we present" or "this paper proposes" (regex from G1, crude and unvalidated).
- 44.8% of question-title abstracts announce a method, against 68.2% of other abstracts: −16.7 pp (−23.7, −9.7) with the primary controls. Question titles mark analysis, evaluation and benchmark papers.
- The indicator itself is unrelated to citations: +2.3% (−2.9, +7.7). Adding it leaves G3 unchanged.

**Reading.**
- The meme overlap ("Do X really …?") does not drive the estimate.
- Removing named or assertive titles from the comparison group raises the estimate by 2–4 points. This is the same reference-group effect seen in the joint model.

### (e) Why R1 (matched pairs) is below the primary

- **Reimplemented R1 pairing.** Reproduces core R1 exactly: 221 pairs, −3.70%.
- **Pair balance.**
  - Mean cosine 0.877; 55% of pairs are in the same topic50.
  - Team size difference −0.02 log; abstract length difference −0.02 log.
  - Matched controls are named at the base rate (24.0% vs 25.0%), while treated papers are 6.3% named. Controls are assertive at 4.5% (base rate 5.4%).
- **Pair-level regression adjustment.**
  - For team size and abstract length: −3.4% (−24.6, +23.5).
  - Adding named and assertive status: +1.4% (−21.6, +32.4).
- **Variants.**

  | Variant | % difference | 95% CI | Pairs |
  |---|---|---|---|
  | Caliper 0.85 | +9.1% | −17.5, +47.0 | 182 |
  | 2017–21 | +18.4% | −30.0, +101.9 | 39 |
  | 2022–25 | −7.9% | −32.1, +23.8 | 182 |
  | arXiv-id records only | −3.1% | −22.3, +20.1 | 174 |
  | Controls restricted to plain titles (not named, not assertive) | −6.0% | −26.8, +18.6 | 221 |

**Reading.**
- All matched-pairs estimates lie between −8% and +18%, with CIs about ±25 points or wider. Each CI overlaps the primary's.
- Raw, the matched design gives no support for a positive association, and no clear evidence against one.
- It does not reproduce the larger joint-model estimate: −6.0% against plain-title controls.
- **Audit correction.** An earlier version said that nothing in the pair balance explains the gap. The balance checks above cover team size, abstract length and title features. They miss how the controls are chosen.
  - The nearest-neighbour controls are embedding "hubs": on average each is the nearest neighbour of 3.0 papers, against 1.0 for all papers and 1.1 for the question papers.
  - Hubs are cited more than their content predicts. This holds with the primary controls and FE.
  - So raw R1 is biased downward by about 12–22%. Every hubness-corrected version of R1 is positive (+5% to +28%). Details are in audit diagnostic (f).

## Interpretation and caveats

- **Inconclusive, not null.** The data are consistent with anything from slightly fewer citations (the primary CI reaches −3%) to substantially more (+35%). Raw R1's CI reaches −26%, but raw R1 is shifted downward by construction (audit (f)). Nothing here supports "question titles get more citations" or "question titles make no difference".
- **Observational.** Authors choose titles. Question titles mark a type of paper: analysis, evaluation or benchmark papers, less often method papers (45% vs 68%), and more often LLM-topic papers (37% vs 22%). Content controls, matched pairs and the method-paper indicator reduce but do not remove differences in what such papers are and how they are promoted. None of this shows that rephrasing a given title as a question would change its citations.
- **Small and recent.**
  - 223 question titles, of which only 39 are from 2017–21 and 86 (39%) are from 2025.
  - 2024–25 papers have only 1–2 years of citations. Year FE absorb age, but these papers contribute noisy outcomes.
- **Heavy upper tail.** The +14% point estimate leans on a few very highly cited papers (GIN, SWE-bench, GATv2). R4 (dropping the top 1% per year) gives +11%; dropping the 5 most-cited question titles gives +7%.
- **Outcome noise.** About 23% of venue records lack an arXiv id and may undercount citations (split records). This is not differential by question status: 78.5% vs 76.8% have an arXiv id. It widens CIs but does not, on these checks, bias the comparison.
- **Selection into the sample.** Only accepted ICLR papers are included.
  - On the reviewer side, no title feature's association with acceptance survives the camera-ready audit (0 of 18 auditable features; `outputs/SUMMARY.md`). For example, NAME-title accepted/all ratio is 1.02, editing-corrected 90% CI 0.949–1.031.
  - So selection on title style by reviewers is not evident. That does not rule out unmeasured quality differences between accepted question-title papers and the rest.
- **Exposure.** The exposure is the camera-ready title as indexed; counts are a single S2 snapshot (2026-10-17).
- **Multiplicity.** Secondary analyses and diagnostics carry no multiplicity correction.
  - The diagnostics were added after the primary was seen, and are labelled as such.
  - The joint-model estimate (+27%, p 0.010) and the non-LLM subgroup (+25.5%, p 0.040) are hypotheses for a future pre-registered test, not findings. The raw matched-pairs version of the joint-model comparison is −6%, but raw matched pairs are shifted downward (audit (f)).

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles are questions receive about 14% more citations on average in the pre-registered model, but the 95% CI runs from −3% to +35%, the estimate leans on a few very highly cited papers, and the pre-registered verdict is inconclusive; these data neither support nor rule out a question title, so we give no advice for or against one.

*(Audit, 2026-10-17: the earlier sentence cited "content-matched pairs show −4%" as counter-evidence. That raw R1 is shifted downward by about 22% by construction, and calibrated it is +23% (−4, +57); see the Audit section. The advice itself is unchanged.)*

## Audit (adversarial review, 2026-10-17)

### What was checked

- **Reproduction.** `core.primary(core.load(), "G3_question")` reproduces `primary.json` exactly: b 0.13388, SE 0.08298, p 0.113, n 8,574, 223 question titles.
  - Holm p 0.348 is taken from `primary.json`. It was not recomputed.
- **Verdict.** Holm p ≥ 0.05, R1 −3.7% (opposite sign), R2 +21.3% (same sign), CI not inside ±10%. So "inconclusive" follows the pre-registered rule (`core.verdict`).
- **Feature definition.** `G3_question` equals "the title contains '?'" for all 8,602 papers, as frozen in `core.load` and the prereg.
- **Frozen files.**
  - SHA-256 of `core.py`, `CITES_PREREG.md` and `matched_venue.parquet` match `prereg_hashes.json`.
  - `primary.json` is unchanged.
- **Leakage.** No control uses the outcome. The PCs, topic clusters and matching embedding are built from abstracts only.
- **Numbers.** Every number in this file was compared with `results.json`. They match, except the question-form label (fix 2).
- **Labels and wording.**
  - Every non-pre-registered block in `results.json` carries "diagnostic (not pre-registered)".
  - The text uses observational wording.
- **Re-run.** `g3.py` was re-run after the changes. Every pre-existing value in `results.json` reproduced identically. The only exception is the QC note text.

### What was changed

1. **R1 used as counter-evidence (interpretation error).**
   - The advice sentence and several readings cited raw content-matched pairs (−3.7%; −6.0% against plain titles) as evidence against a positive association.
   - Raw R1 is shifted about −22% by construction (diagnostic (f) below), so it cannot carry that weight. Those passages now say so.
   - The advice is unchanged: no advice for or against.
   - The reading of (e), "nothing in the pair balance explains the gap", was wrong and is corrected.
2. **Question-form label (error).** "Questions after a 'NAME:' prefix: 33" counted every question after a colon. Only 14 of the 33 follow a coined name.
3. **R2 sign.** Its dependence on a single paper is now stated (diagnostic (g)).
4. **QC note.** The split-record QC run has finished: its log ends "DONE" at 30 records. The counts (30 checked, 7 split, 1 question title) are final. The earlier caveat that the file was still growing no longer applies.
5. **Audit diagnostics added.**
   - Code: new module `src/cites/audit_g3g4.py`, called from `g3.py`.
   - Results: `results.json` → `diagnostics.f_audit_r1_calibration` and `diagnostics.g_audit_alt_explanations`.
   - Figure: one added row, "R1 placebo-adjusted (diagnostic)".

### (f) R1 calibration — diagnostic (not pre-registered)

| Check | Result |
|---|---|
| **Placebo null of R1.** 200 draws of random non-question papers, with the same per-year counts as the 223 question titles, run through the R1 procedure. | Null mean **−21.7%**; null 95% range −39.5% to −3.7%. Observed −3.7%, at the top edge of that range: placebo p 0.07. **Placebo-adjusted R1 +23.0% (−3.7, +57.1).** |
| **Mechanism: who are the matched controls?** | On average each matched control is the nearest same-year neighbour of **3.0** papers, against 1.0 for all papers and 1.1 for question papers. Controls are also in denser regions: +0.86 SD of local density, against +0.36 SD for question papers. |
| **Are hubs cited more?** Primary controls and FE. | +27.8% (+20.7, +35.3) per unit of log(1 + times-a-nearest-neighbour). +40.5% (+34.3, +47.0) per SD of local density. |
| **Residual decomposition.** Residual from the primary model fitted on non-question papers. | Question papers sit +0.128 log points above their content prediction. Their matched controls also sit +0.128 above. R1 with the controls' excess removed: **+9.4%**. |
| **Hub-penalised (CSLS-style) matching.** | Raw +14.5% (−10.8, +47.5), 220 pairs. Its own null is −10.8%, so calibrated it is **+28.4% (+0.5, +64.1)**. |
| **Pair-level adjustment** for the hubness difference. | **+5.5% (−23.2, +45.2)** |
| **Does the primary miss hubness?** | Primary + hubness: +13.7% (−3.0, +33.4). Primary + density: +10.7% (−5.5, +29.8). |

**Reading.**
- Nearest-neighbour matching picks hub papers as controls. Hubs sit in dense, well-cited regions, and are cited more than the 20 PCs and year × topic50 FE predict.
- This pushes R1 down for any feature. G4 shows the same: null −20.5%.
- Every hubness-corrected version of R1 for G3 is positive, from +5% to +28%. So the opposite sign of raw R1 is most likely an artefact of the procedure, not evidence against the primary.
- The corrected versions are themselves imprecise: most CIs include 0. They support "consistent with the primary", not "confirms it".
- Question papers are only slightly more hub-like than other papers: k-occurrence 1.1 vs 1.0, density +0.36 SD. Adding hubness or density to the primary moves G3 only to +11–14%, so the primary is not driven by it.

### (g) Alternative explanations tested — diagnostic (not pre-registered)

Each re-fit uses the primary controls, year × topic50 FE and SEs clustered by topic50.

| Alternative explanation | Test | Result for G3 |
|---|---|---|
| **S2 split records** (venue record without an arXiv id under-counts) | arXiv-id records only; arXiv-id indicator (diagnostic (a)) | +15.7% (−3.1, +38.2) on arXiv-id records; +13.1% with the indicator. Share with an arXiv id: 78.5% vs 76.8%. |
| **Preprint exposure time** | Months from first arXiv posting to the conference; arXiv-id records with lead-month FE bins | Posted 6.9 vs 6.6 months before. **+12.8% (−5.3, +34.3)** |
| **Promotion / code release** | Abstract announces code or a URL | 21.1% vs 21.7%. With the indicator: +15.3% (−2.0, +35.5). |
| **Paper type: analysis / findings / benchmark** | Method, findings and benchmark-paper indicators (crude regexes) | Findings abstracts 63% vs 46%; benchmark papers 10.8% vs 6.3%. With all three: **+13.7% (−3.4, +34.0)**. Benchmark papers excluded: +19.5% (+1.1, +41.2), 199 question titles. Within findings abstracts: +14.4% (−5.7, +38.7). |
| **LLM-topic composition** | + llm_topic indicator | +14.8% (−2.6, +35.3) |
| **LLM-assisted writing** | + F24 abstract fingerprint | 9.9% vs 9.8%. +14.3%. |
| **Team prior success** | Pre-registered R6 (2022–25) | +15.2% (−2.1, +35.5) |
| **Superstar outliers** | Within-year citation percentile outcome; drop the top 5% per year; drop zero-citation records | Percentile: +3.0 points (−0.5, +6.4), p 0.10. Top 5% dropped: +18.6% (+0.3, +40.3). Zero-citation records dropped: +11.1% (−4.9, +29.8). |
| **R2 sign** | PPML after dropping the most-cited question paper(s); PPML with the top 1% per year dropped | GIN dropped: −10.3% (−37.9, +29.6). Top 1% per year dropped: −19.0% (−36.2, +2.7). |
| **Retitling** | WP4 audit pairs: arXiv v1 title, posted before the decision, vs camera-ready; 568 accepted 2023–25 papers | 19 question titles on each version: 2 added at camera-ready, 2 removed. Too few for an estimate. |

**Reading.**
- On the log scale, none of these explanations removes or reverses the point estimate. It stays between +11% and +20%. Excluding benchmark papers and dropping the top 5% per year both raise it slightly.
- Most CIs include 0, as the primary's does. A few just exclude it (benchmark papers excluded; top 5% dropped). These are post-hoc and uncorrected, so they are not findings.
- **Count scale.** On raw counts the comparison has no stable sign. The mean is carried by GIN, and with the top 1% per year removed PPML is negative.
  - The log-scale primary describes the typical paper. Question-title papers are shifted up modestly in the middle of the distribution (percentile +3 points), but no more often among the very top papers.
- **Retitling** is rare (4 of 21 changes in the audited subsample), so the camera-ready exposure is close to the pre-decision one.
- **Not testable with these data.** Lab reputation beyond prior ICLR acceptances, social-media promotion, and quality signals not reflected in the abstract.

### Confidence in the advice

- **"No advice for or against": high.** Holm p is 0.35, the CI spans −3% to +35%, and the pre-registered ±10% band was unattainable at n = 223.
- **Direction of the point estimate: low to medium.**
  - It is positive under every log-scale adjustment and under every hubness-corrected matched-pairs version.
  - It is sensitive to a few very highly cited papers: dropping the 10 most-cited question titles gives +2%.
  - It has no stable sign on the count scale.
- The one-sentence advice stands, with the R1 clause replaced. It remains an association: it does not show that rephrasing a given title as a question would change its citations.
- **Cross-cutting note for the integrator.** Raw R1 (`core.matched_pairs`) is shifted about −20% under the null for both G3 and G4. The cause is hub selection by nearest-neighbour matching. Any G-question whose write-up quotes raw R1 as a size estimate or as counter-evidence should be re-read with this in mind. For example, G1's audit quotes R1 (+5.6% to +8.4%) as the low end of its size range.
