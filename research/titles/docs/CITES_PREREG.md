# Pre-registration: which title choices go with more citations? (ICLR accepted papers, 2017–2025)

Status: **frozen 2026-10-17, before any title–citation association was estimated on real outcomes.**
The analysis core (`src/cites/core.py`) was checked only with outcomes permuted within year. Hashes are in `outputs/cites/prereg_hashes.json`.

## 1. Questions (each is one piece of advice for authors)

- **G1** Should you give your method a name ("NAME: subtitle")?
- **G2** Should the title state the finding (an assertive verb) rather than describe the method?
- **G3** Should the title be a question?
- **G4** Should you use LLM-favoured words (enhancing, leveraging, unveiling, unleashing, harnessing, empowering, elevating, boosting)?
- **G5** How long and how informative should a title be?
  - G5a: title length, per +5 words.
  - G5b: title–abstract semantic similarity, z-scored within year.
- **G6** Should you use catchy templates?
  - G6a: meme templates (All You Need, Is Secretly, Matters, When X Meets Y, …).
  - G6b: tentative framings (Towards, Rethinking, Revisiting, Understanding, On the, Demystifying).

## 2. Sample and outcome

- **Sample.** Accepted papers in the discovery universe, 2017–2025, matched to a Semantic Scholar venue record by normalised title (S2 year within the conference year minus 2 to the conference year).
  - 8,602 papers; match rates by year 94.6–97.8%.
  - 2026 is excluded: its venue records are not yet indexed (15 of 4,175 matched).
- **Design rationale.** Venue and review decision are held fixed: every paper is an accepted ICLR paper. The exposure is the published (camera-ready) title, which is what readers see.
- **Outcome.** y = log(1 + Semantic Scholar citation count, retrieved 2026-10-17). Citation age is absorbed by year fixed effects.

## 3. Primary model (identical for every question)

- **Model:**
  `y ~ feature + log(team size) + log(abstract words) + 20 PCs of the bge abstract embedding | year × topic50`
- **Standard errors:** clustered by topic50.
- **Extra controls:**
  - G5a also controls for G1 (named titles are shorter).
  - G5b also controls for G1 and G5a (named titles share fewer words with their abstracts).
- **Effect scale:** % difference in citations, exp(b) − 1.
- **Multiplicity:** Holm across the 8 primary tests (G1, G2, G3, G4, G5a, G5b, G6a, G6b).
- **Calibration.** 200 within-year permutations of the outcome give false-positive rates of 3.5–7.0% at α = 0.05 for all 8 tests (`outputs/cites/calibration_permutation.json`).

## 4. Pre-specified robustness checks (`core.robustness`)

| ID | Check |
|---|---|
| R1 | Content-matched pairs. Each paper with the feature (top tercile for continuous features) is matched to its nearest same-year paper without it (bottom tercile) on the name-masked abstract embedding, cosine ≥ 0.80. Reported: the mean within-pair difference. |
| R2 | PPML on raw counts. Heavy-tailed; used as a sign check only. |
| R3 | Influential-citation count. |
| R4 | Drop the top 1% most-cited papers per year. |
| R5 | By era: 2017–21 vs 2022–25. |
| R6 | 2022–25 sample with the team's prior ICLR acceptances added as a control. |
| R7 | Year + topic100 fixed effects instead of year × topic50. |

## 5. Decision rule (`core.verdict`)

- **"More citations" / "fewer citations":** Holm-adjusted p < 0.05, **and** the same sign in R1 (matched pairs) and R2 (PPML).
- **"No meaningful difference":** the 95% CI of the primary % effect lies within ±10%.
- **Otherwise "inconclusive."**

## 6. Pre-specified secondary analyses (reported, no multiplicity claim)

| Question | Secondary analysis |
|---|---|
| G1 | By name orthography (mixed case, ALL CAPS, word). |
| G2 | Validity of the rule-based measure against the claims-pilot LLM title-strength labels on overlapping items. |
| G4 | Each word family separately; pre-2023 vs 2023+. |
| G5a | Length bins (≤6, 7–9, 10–12, 13–15, ≥16 words). |
| G6 | Each template with n ≥ 20. |

Applying to all questions:
- A joint model with all 8 features.
- Heterogeneity by LLM-topic papers.

## 7. Interpretation limits (stated in advance)

- **Observational.** Authors choose titles, and stronger or better-promoted work may get both a certain title style and more citations. Content controls and matched pairs reduce but do not remove this. Results are stated as "among accepted papers with similar content, papers whose titles do X receive Y% more or fewer citations on average."
- **Accepted papers only.** Rejected papers are not yet included.
- **Data source.** Citation counts come from Semantic Scholar. A QC of split records (venue record vs separate arXiv record) is reported in `outputs/cites/qc_split_records.jsonl`.
