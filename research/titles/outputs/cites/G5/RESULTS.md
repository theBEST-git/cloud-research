# G5: title length and title informativeness and citations

**Code:** `src/cites/g5.py`. **Numbers:** `outputs/cites/G5/results.json`. **Figure:** `outputs/cites/G5/fig.png` (data in `fig.csv`).
**Pre-registration:** `docs/CITES_PREREG.md` (frozen 2026-10-17). **Frozen core:** `src/cites/core.py` (not edited; sha256 matches `prereg_hashes.json`).

## Question

Among accepted ICLR papers from 2017 to 2025, do papers with longer titles, or with titles closer in meaning to their abstract, get more or fewer Semantic Scholar citations than accepted papers with similar content?

- **G5a, length.** Title word count / 5, so effects are **per +5 words**. Median title 8 words; IQR 7–10.
- **G5b, informativeness.** Cosine similarity of the bge-small title and abstract embeddings, z-scored within year, so effects are **per +1 SD**.
- **Sample.** 8,602 accepted papers matched to an S2 venue record; 8,574 enter the regressions after singleton year × topic50 cells are dropped.
- **Outcome.** y = log(1 + citations), retrieved 2026-10-17.
- **Model.** `y ~ feature + log(team size) + log(abstract words) + 20 bge abstract PCs | year × topic50`, with SEs clustered by topic50.
  - G5a also controls for G1 (named title).
  - G5b also controls for G1 and G5a.
- **Effect scale.** % difference = exp(b) − 1.

## Primary estimates (pre-registered)

| | % difference in citations | 95% CI | p | Holm p (8 tests) | n |
|---|---|---|---|---|---|
| G5a title length, per +5 words | −5.5% | −11.3% to +0.7% | 0.087 | 0.35 | 8,574 |
| G5b informativeness, per +1 SD | **+8.0%** | +5.0% to +11.1% | 2.2e-06 | **1.8e-05** | 8,574 |

- Estimates and Holm p are taken from `outputs/cites/primary.json`.
- Re-computing both with `core.primary` reproduces them exactly: largest absolute difference 0, same n.

## Robustness checks R1–R7 (pre-registered, `core.robustness`)

R1 compares the top with the bottom within-year tercile, not a one-unit change. The matched pairs differ by 1.15 units in G5a (about 5.8 words) and by 2.06 SD in G5b; see diagnostic (d).

| Check | G5a length, per +5 words | G5b informativeness, per SD |
|---|---|---|
| Primary | −5.5% [−11.3, +0.7] | **+8.0% [+5.0, +11.1]** |
| R1 content-matched pairs, top vs bottom tercile | −23.0% [−28.4, −17.0], 2,547 pairs | +4.4% [−2.5, +12.4], 2,711 pairs |
| R2 PPML on raw counts (sign check) | −25.3% [−42.6, −2.8] | +1.8% [−9.5, +14.5] |
| R3 influential-citation count | −5.9% [−10.8, −0.8] | +4.5% [+2.0, +7.2] |
| R4 drop top 1% most-cited per year | −4.4% [−10.2, +1.8] | +7.7% [+4.6, +10.9] |
| R5 2017–21 only (n 1,975) | −12.5% [−22.5, −1.1] | +12.4% [+5.3, +19.9] |
| R5 2022–25 only (n 6,599) | −3.7% [−10.5, +3.7] | +6.8% [+3.2, +10.5] |
| R6 2022–25 + team's prior ICLR acceptances | −3.6% [−10.4, +3.8] | +7.1% [+3.5, +10.7] |
| R7 year + topic100 FE (n 8,602) | −7.5% [−12.6, −2.0] | +8.9% [+5.8, +12.0] |

**Reading.**
- **G5a.** Every check is negative. The sizes range from about −4% (R4, R5 2022–25, R6) to about −25% (R1, R2).
- **G5b.** Every check is positive. R3–R7 sit between +4.5% and +12.4%. The two checks the decision rule uses are weak:
  - R1 matched pairs: +4.4%, CI includes 0.
  - R2 PPML: +1.8%, CI includes 0.

## Verdict (pre-registered rule)

- **G5a length: "inconclusive."**
  - Holm p = 0.35, so it is not "fewer citations".
  - The 95% CI (−11.3%, +0.7%) is not inside ±10%, so it is not "no meaningful difference" either.
- **G5b informativeness: "more citations."** All three conditions hold:
  - Holm p = 1.8e-05;
  - R1 has the same sign (+4.4%);
  - R2 has the same sign (+1.8%).

  The rule checks only the sign of R1 and R2. Both are small and their CIs include zero. The diagnostics below show that the size of the G5b association depends on the similarity model and on how content is held fixed.

## Secondary analyses (pre-specified in prereg section 6; no multiplicity claim)

**G5a length bins vs 10–12 words.** One model with four bin dummies replaces the linear term. Controls are `core.controls('G5a_length5')`.

| Title length | n | named | % difference vs 10–12 words | 95% CI | p | implied by the linear primary term |
|---|---|---|---|---|---|---|
| ≤6 words | 1,874 | 216 | **+10.4%** | +0.6, +21.1 | 0.042 | +6.7% |
| 7–9 words | 3,793 | 1,063 | −0.9% | −7.7, +6.3 | 0.80 | +3.1% |
| 10–12 words (reference) | 2,333 | 708 | — | — | — | — |
| 13–15 words | 504 | 108 | −5.0% | −17.4, +9.3 | 0.48 | −3.4% |
| ≥16 words | 98 | 10 | −8.8% | −31.0, +20.6 | 0.52 | −7.0% |

- Joint Wald test that all four bins are 0: χ²(4) = 9.35, p = 0.053 (F-version p = 0.068).
- The bins follow the linear term roughly. The only bin that differs clearly from 10–12 words is the shortest (≤6 words).

**Joint model with all 8 primary features.**

| | % difference | 95% CI | p |
|---|---|---|---|
| G5a, per +5 words | **−11.3%** | −17.3, −4.9 | 0.0014 |
| G5b, per SD | +8.7% | +5.6, +11.9 | 7.1e-07 |

Holding informativeness and the other title features fixed, the length association is about twice the primary's. This is because longer titles are more informative (r = 0.21), and informativeness goes with more citations.

**Heterogeneity by LLM-topic papers** (1,931 LLM-topic papers).

| | LLM-topic papers | other papers | ratio of multipliers | p |
|---|---|---|---|---|
| G5a, per +5 words | +3.7% [−11.4, +21.4] | −7.6% [−13.8, −0.9] | 1.12 [0.94, 1.34] | 0.20 |
| G5b, per SD | +7.1% [+2.5, +12.0] | +8.6% [+4.7, +12.5] | 0.99 [0.93, 1.05] | 0.67 |

## Diagnostics — diagnostic (not pre-registered)

None of these analyses was pre-registered. They involve many tests with no multiplicity correction, and they are reported to help interpret the results, not as findings.

### (a) What does G5b measure? Named titles, keywords, topic vocabulary

**Not a proxy for "non-named title".**
- Named titles score *higher* on G5b, not lower: +0.27 SD (0.22, 0.33) with the primary controls. The coined name usually reappears in the abstract.
- The association is present within each group:
  - non-named titles: **+6.6% [+3.1, +10.3]**, n 6,465;
  - named titles: +12.1% [+5.0, +19.7], n 2,032.
- In one fully interacted model, the ratio of the two slopes is 1.05 (0.98, 1.13), p 0.20.

**Name-masked variant: title vs the abstract with coined names and CamelCase/ALL-CAPS tokens replaced by `[NAME]`.**
- 2017 has no masked embedding and keeps the unmasked one (141 papers).
- After masking, named titles score lower than non-named titles: −0.11 vs +0.04 SD. This is the direction the prereg anticipated.
- The association is about halved:
  - all papers: **+4.3% [+0.9, +7.9]**;
  - non-named: +4.2% [+0.3, +8.3];
  - named: +3.4% [−3.6, +10.9].
- So part of G5b, especially among named titles, comes from names and acronyms appearing in both the title and the abstract.

**Lexical overlap**, defined as the share of title content words that occur in the abstract:
- Correlation with G5b: 0.37.
- Adding it as a control leaves G5b at +7.4% [+4.1, +10.7].
- Given G5b, lexical overlap itself shows no association: −0.0% [−3.3, +3.4].
- So G5b is not "reusing the abstract's words".

**Topic vocabulary.**
- *Topic-keyword share* is the share of title words among the top-30 c-TF-IDF words of the paper's topic50 cluster.
  - Correlation with G5b: 0.21.
  - On its own it is associated with +16.3% per SD [+12.2, +20.6].
  - Adding it as a control reduces G5b to **+4.5% [+1.6, +7.4]**.
- *Title centrality* is the cosine of the title embedding to the cluster's mean abstract embedding.
  - Correlation with G5b: 0.50.
  - Adding it as a control reduces G5b to **+3.0% [−0.4, +6.6]**.
- *Abstract centrality* is the same measure computed for the abstract instead of the title, so it is a content measure.
  - It is uncorrelated with G5b (−0.02) and leaves G5b unchanged (+8.3%).
  - Title centrality keeps an association after controlling for abstract centrality: +6.5% [+1.8, +11.4].

**Reading.** Much of what G5b picks up is a title written in the central vocabulary of its topic. This is a property of the title rather than of the abstract's content, as measured here. These data cannot separate it from unmeasured content.

### (b) Alternative measure: all-MiniLM-L6-v2 title–abstract cosine (z within year)

- **Agreement with bge.** Pearson 0.78 (0.76–0.87 within year), Spearman 0.75. 63% of papers fall in the same tercile under both measures.
- **Primary spec with MiniLM instead of bge.** **+4.1% [+0.9, +7.4]**, p 0.014, about half the bge estimate.
- **Full R1–R7 battery on the MiniLM measure.**

  | Check | % difference |
  |---|---|
  | R1 matched pairs | **−11.3% [−17.5, −4.8]**, opposite sign |
  | R2 PPML | −0.0% [−9.8, +10.8] |
  | R3 influential citations | +2.6% [−0.0, +5.4] |
  | R4 drop top 1% | +4.2% [+1.0, +7.5] |
  | R5 2017–21 | +12.9% [+7.0, +19.1] |
  | R5 2022–25 | +1.9% [−1.9, +5.8] |
  | R6 2022–25 + team prior | +2.3% [−1.4, +6.3] |
  | R7 year + topic100 FE | +4.7% [+1.4, +8.1] |

- With this measure, R1 and R2 do not share the primary's sign. Had MiniLM been the pre-registered measure, the rule would not have returned "more citations".
- **Both measures in one model.** bge given MiniLM: +11.7% [+6.9, +16.7]. MiniLM given bge: −4.4% [−8.8, +0.3].
- **Within groups (MiniLM).** Non-named +4.0% [+0.1, +7.9]; named +4.9% [−3.2, +13.6].
- **Reading.** The direction is positive in the regression under both models. The size, and the agreement with matched pairs, depend on the embedding model, and the association is carried by the part of bge similarity that MiniLM does not share.
  - The 20 content PCs in the frozen controls are also bge-based. Whether that interacts with the bge-specific component cannot be settled here.

### (c) S2 split-record and matching artefact

Venue records without an arXiv id can miss citations that S2 credits to a separate arXiv record. Here an arXiv id goes with +213% citations [+174, +258], with the primary controls.

| | bottom tercile | middle | top | with primary controls |
|---|---|---|---|---|
| G5b: arXiv-id share | 77.5% | 77.3% | 75.8% | −0.19 pp per SD [−1.20, +0.81] |
| G5b: S2 match rate (all 8,873 accepted) | 97.2% | 96.8% | 96.9% | −0.01 pp per SD [−0.37, +0.35] (year FE) |
| G5a: arXiv-id share | 80.3% | 75.9% | 74.6% | **−4.8 pp per +5 words [−6.5, −3.1]** |
| G5a: S2 match rate | 97.5% | 96.6% | 96.7% | −0.41 pp per SD [−0.78, −0.04] (year FE) |

**G5b is not explained by the artefact.**
- arXiv records only: +6.8% [+3.6, +10.2], n 6,575.
- Records without an arXiv id: +11.5% [+3.7, +19.8], n 1,926. The ratio between the two is 1.04 (0.97, 1.13), p 0.29.
- With an arXiv indicator added:
  - primary spec: +8.2% [+5.4, +11.1];
  - joint model: +8.9% [+6.0, +11.9].

**G5a is largely accounted for by arXiv-id status.**
- Longer titles less often have an arXiv id.
- Primary spec plus an arXiv indicator: **−0.2% [−6.0, +6.0]**.
- arXiv records only: −3.6% [−9.9, +3.0]. No-arXiv records: +9.9% [−3.9, +25.8].
- Joint model plus an arXiv indicator: −6.4% [−12.5, +0.2], p 0.06.
- These data cannot tell whether arXiv status works here as an S2 record artefact or as a real exposure channel, where papers that are not on arXiv are read less.

### (d) Putting R1 on the primary scale

- R1 pairing was reimplemented and reproduces `core` R1 exactly for G5a, G5b and the MiniLM measure.
- The adjusted slope comes from a pair-difference regression with no intercept and SEs clustered by control paper. It adjusts for the within-pair differences in log team size, log abstract words, G1, and (for G5b) G5a.

| | Feature contrast in pairs | Primary implied at that contrast | R1 | Adjusted slope, per unit | Adjusted slope + arXiv status |
|---|---|---|---|---|---|
| G5a | 1.15 (≈ 5.8 words) | −6.3% [−12.9, +0.8] | −23.0% | −19.5% [−26.5, −11.9] | −14.9% [−21.6, −7.6] |
| G5b (bge) | 2.06 SD | +17.1% [+10.5, +24.1] | +4.4% | **+1.1% [−4.2, +6.8]** per SD | +2.0% [−2.9, +7.2] |
| G5b (MiniLM) | 2.14 SD | +9.0% [+2.0, +16.4] | −11.3% | −5.3% [−10.1, −0.3] per SD | −3.9% [−8.3, +0.7] |

**Reading.** Within content-matched pairs, informativeness shows almost no association once length, G1, team size and abstract length are adjusted for. Length shows a *larger* negative association in pairs than in the regression. The two content-adjustment strategies (20 PCs + year × topic50 FE vs nearest-neighbour pairs) disagree for both features, in opposite directions.

### (e) Shape of the G5b association

Within-year fifths of G5b, compared with the middle fifth:

| Fifth | % difference vs middle fifth |
|---|---|
| Q1 (mean cosine 0.79) | −13.4% [−19.9, −6.4] |
| Q2 | −6.7% [−12.9, −0.0] |
| Q4 | +3.1% [−4.9, +11.9] |
| Q5 (mean cosine 0.91) | +10.4% [+2.5, +18.8] |

- Joint test χ²(4) = 33.0, p 1.2e-06.
- The pattern is roughly monotone, so it is not driven by one tail.
- Dropping the 92 papers with |z| > 3 gives +9.4% [+5.6, +13.3].
- The lowest-scoring titles are catchy templates, for example "Copy is All You Need", "Let's Verify Step by Step" and "Is Attention All That NeRF Needs?". So G5b partly measures the opposite of G6a/G2/G3-style titles. Holding those features fixed in the joint model gives +8.7%.

### (f) Team prior (pre-registered R6 compared with R5 on the same 2022–25 sample)

Adding the team's prior ICLR acceptances changes neither feature:

| | R5, without the control | R6, with the control |
|---|---|---|
| G5a | −3.7% | −3.6% |
| G5b | +6.8% | +7.1% |

## Caveats

- **Observational.** Authors choose titles, and the same choice may go with stronger or better-promoted work. The statements below are "papers whose titles do X receive Y% more or fewer citations on average, among accepted papers with similar content", not effects of retitling.
- **Measure dependence (G5b).** The pre-registered verdict is "more citations" with the bge measure.
  - With MiniLM the regression estimate halves (+4.1%), and the matched pairs reverse sign.
  - Within matched pairs, the covariate-adjusted bge slope is near 0.
  - The size of the association is therefore uncertain. A reasonable reading is "+0% to +8% per SD, depending on how content and similarity are measured".
- **What G5b captures.** Much of G5b overlaps with titles written in the topic's central vocabulary, and with names and acronyms shared between the title and the abstract. It is not a pure measure of "how much the title tells you".
- **Length.** The verdict is inconclusive. The estimate ranges from about 0% (with an arXiv-id control) to −11% (joint model) to about −20% (matched pairs), depending on the adjustment. Only titles of 6 or fewer words differ clearly from 10–12-word titles in the pre-specified bins.
- **Diagnostics are many and uncorrected.** They are labelled "diagnostic (not pre-registered)" and are meant for interpretation only.
- **Construction of some diagnostic measures.**
  - The topic-keyword and centrality measures use in-sample cluster statistics that include the paper's own abstract.
  - The name mask also masks non-name CamelCase/ALL-CAPS tokens, such as model names.
- **Sample and source.** Accepted papers only. Citation counts are from Semantic Scholar as of 2026-10-17, and 2022–25 papers have had less time to accumulate citations.
- **Reviewer side.** On the reviewer side, no auditable title feature predicts acceptance once camera-ready edits are accounted for (`outputs/SUMMARY.md`). Length and title–abstract similarity are not among the audited features listed there, so selection at acceptance on these two features is not directly ruled out.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles state what the paper does in their topic's usual vocabulary (higher title–abstract similarity) receive on average up to about 8% more citations per SD, and less under other similarity and content measures, whereas title length shows no reliable association.
