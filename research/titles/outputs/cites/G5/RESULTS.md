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
- **R1 is shifted by the pairing procedure itself (correction added by the audit; diagnostic (g)).**
  - With the feature permuted within year, so that there is no association, the R1 statistic still averages −16.6% for G5a and −17.1% for G5b.
  - The reason is that nearest-neighbour controls are re-used "hub" papers, which sit above their cell's mean citations.
  - Calibrated against that null, R1 is −7.6% [−16.3, +2.0] for G5a and **+25.9% [+14.2, +38.9]** for G5b. The primary implies −6.3% and +17.1% at the same contrasts.
  - So raw R1 overstates the length association and understates the informativeness association. The verdict uses raw R1, as pre-registered.

## Verdict (pre-registered rule)

- **G5a length: "inconclusive."**
  - Holm p = 0.35, so it is not "fewer citations".
  - The 95% CI (−11.3%, +0.7%) is not inside ±10%, so it is not "no meaningful difference" either.
- **G5b informativeness: "more citations."** All three conditions hold:
  - Holm p = 1.8e-05;
  - R1 has the same sign (+4.4%);
  - R2 has the same sign (+1.8%).

  The rule checks only the sign of R1 and R2.
  - R2 is small, and its CI includes zero.
  - Raw R1 is also small, but only because the pairing procedure is shifted by about −17% when there is no association. Calibrated, R1 is +25.9% at a 2.06-SD contrast (audit, diagnostic (g)).
  - The size of the G5b association depends somewhat on the similarity model and on whether the title's topic vocabulary counts as informativeness (diagnostics (a), (b)).

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
- *Both centralities together* (added by the audit; already in `results.json`). With title and abstract centrality both controlled, G5b is **+7.3% [+3.5, +11.2]**.
  - So the drop to +3.0% with title centrality alone comes mostly from title centrality standing in for the abstract's (content) centrality.
  - With the topic-keyword share and abstract centrality both controlled, G5b is +5.6% [+2.7, +8.6].

**Reading (revised by the audit).** About a third to a half of G5b overlaps with a title written in its topic's keyword vocabulary:
- the topic-keyword share brings G5b to +4.5%, or +5.6% with abstract centrality also controlled;
- title centrality, once abstract centrality is held fixed, removes little (+7.3%).

This is a property of the title rather than of the abstract's content, as measured here. These data cannot separate it from unmeasured content.

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
  - *Audit correction.* The R1 sign reversal is an artefact of the pairing procedure (null mean −16.7%). Calibrated, the MiniLM R1 is +6.5% [−2.7, +16.5], the same sign as its primary.
  - R2 (−0.0%) would still fail the sign condition.
- **Both measures in one model.** bge given MiniLM: +11.7% [+6.9, +16.7]. MiniLM given bge: −4.4% [−8.8, +0.3].
- **Within groups (MiniLM).** Non-named +4.0% [+0.1, +7.9]; named +4.9% [−3.2, +13.6].
- **Reading.** The direction is positive in the regression under both models. The size, and the agreement with matched pairs, depend on the embedding model, and the association is carried by the part of bge similarity that MiniLM does not share.
  - The 20 content PCs in the frozen controls are also bge-based.
  - *Audit:* that does not drive the bge estimate. Replacing them with 20 MiniLM abstract PCs gives G5b +8.3% [+5.3, +11.3], and using 100 bge PCs gives +8.9% [+6.0, +11.9] (diagnostic (g)).

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
  - *Audit:* mostly an artefact (diagnostic (g)). The WP4 audit has 568 accepted 2023–25 papers in this sample that are known to have a pre-decision arXiv preprint.
  - Even so, 15% of their venue records lack an arXiv id. Those records have median 0 citations, against 30 for records with an id.
  - A missing id therefore mostly marks a split S2 record, not a paper absent from arXiv.
  - Camera-ready retitling raises the chance of a missing id by 14.8 pp [7.2, 22.4]. Longer titles are retitled more often: +10.5 pp per +5 words [3.4, 17.6].

### (d) Putting R1 on the primary scale

- R1 pairing was reimplemented and reproduces `core` R1 exactly for G5a, G5b and the MiniLM measure.
- The adjusted slope comes from a pair-difference regression with no intercept and SEs clustered by control paper. It adjusts for the within-pair differences in log team size, log abstract words, G1, and (for G5b) G5a.

| | Feature contrast in pairs | Primary implied at that contrast | R1 (raw) | Adjusted slope, per unit (no intercept; biased, see below) | Same + arXiv status (biased) |
|---|---|---|---|---|---|
| G5a | 1.15 (≈ 5.8 words) | −6.3% [−12.9, +0.8] | −23.0% | −19.5% [−26.5, −11.9] | −14.9% [−21.6, −7.6] |
| G5b (bge) | 2.06 SD | +17.1% [+10.5, +24.1] | +4.4% | **+1.1% [−4.2, +6.8]** per SD | +2.0% [−2.9, +7.2] |
| G5b (MiniLM) | 2.14 SD | +9.0% [+2.0, +16.4] | −11.3% | −5.3% [−10.1, −0.3] per SD | −3.9% [−8.3, +0.7] |

**Reading (corrected by the audit; the original reading was wrong).**
- The original reading was that informativeness shows almost no association within content-matched pairs, that length shows a larger negative one, and that the two content-adjustment strategies disagree. Most of that comes from the R1 pairing procedure, not from the data.
- **Why the slopes are biased.** The two "adjusted slope" columns come from regressions with no intercept. They therefore absorb the procedure's own downward shift. With the feature permuted within year, these slopes average −11.8% per +5 words (G5a) and −6.8% per SD (G5b, bge) — that is, under no association at all.
- **Net of that null mean** they are:
  - G5a: −8.7% [−16.6, −0.0];
  - G5b (bge): **+8.5% [+2.8, +14.6]**;
  - G5b (MiniLM): +1.5% [−3.6, +6.8].

  The two bge values are close to the primary estimates.
- **Symmetric matching.** Matching each bottom-tercile paper to its nearest top-tercile paper shifts the null the other way, by about +21%. The average of the two directions has a null mean of about 0. Observed, it is:
  - G5a: −8.6% at about 1.15 units (the primary implies −6.3%);
  - G5b: **+22.2%** at about 2.06 SD (the primary implies +17.1%).
- **With an intercept**, which absorbs any constant shift, the slopes are imprecise: G5a −6.5% [−23.8, +14.6]; G5b −5.0% [−15.6, +6.9].
  - This is the one pair-based estimate that does not support the G5b primary.
  - It is identified only from differences in the size of the contrast across top-vs-bottom pairs. The pairs with the largest contrasts have the lowest-G5b controls, which are often catchy meme-style titles (see (e)).
- See diagnostic (g) in the Audit section below.

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
- **Measure dependence (G5b), revised by the audit.** The pre-registered verdict is "more citations" with the bge measure.
  - With MiniLM the regression estimate halves (+4.1%). Its raw matched pairs reverse sign, but calibrated they do not (+6.5%).
  - Within matched pairs, the null-corrected covariate-adjusted bge slope is +8.5%. The calibrated R1 (+25.9% at 2.06 SD) and the symmetric pairs (+22.2%) agree with the primary.
  - The one pair-based estimate that does not support it is the with-intercept slope (−5.0% [−15.6, +6.9]), and it is imprecise.
  - A reasonable reading is about **+3% to +9% per SD**. The range depends on the similarity model, and on whether the title's topic vocabulary and shared names count as part of informativeness.
  - The earlier "+0% to +8%" rested on the biased no-intercept pair slope (see (d)).
- **What G5b captures.** About a third to a half of G5b overlaps with titles written in their topic's keyword vocabulary, and with names and acronyms shared between the title and the abstract. It is not a pure measure of "how much the title tells you".
- **Length.** The verdict is inconclusive.
  - The estimate ranges from about 0% (with an arXiv-id control) to −11% (joint model).
  - The raw matched pairs' −23% is mostly the pairing procedure's own shift. Calibrated, it is about −8%.
  - The arXiv-id link with length looks mostly like an S2 split-record artefact. Longer titles are retitled at camera-ready more often, and retitled papers more often have their citations split off to a separate arXiv record (audit (g)).
  - Only titles of 6 or fewer words differ clearly from 10–12-word titles in the pre-specified bins.
- **Diagnostics are many and uncorrected.** They are labelled "diagnostic (not pre-registered)" and are meant for interpretation only.
- **Construction of some diagnostic measures.**
  - The topic-keyword and centrality measures use in-sample cluster statistics that include the paper's own abstract.
  - The name mask also masks non-name CamelCase/ALL-CAPS tokens, such as model names.
- **Sample and source.** Accepted papers only. Citation counts are from Semantic Scholar as of 2026-10-17, and 2022–25 papers have had less time to accumulate citations.
- **Reviewer side.** On the reviewer side, no auditable title feature predicts acceptance once camera-ready edits are accounted for (`outputs/SUMMARY.md`). Length and title–abstract similarity are not among the audited features listed there, so selection at acceptance on these two features is not directly ruled out.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles are closer in meaning to their abstracts (higher title–abstract similarity) receive on average about 8% more citations per SD (about 3% to 9% across alternative similarity measures and content adjustments), whereas title length shows no reliable association.

*(Revised by the audit. The earlier sentence read "papers whose titles state what the paper does in their topic's usual vocabulary … receive on average up to about 8% more citations per SD, and less under other similarity and content measures". Its lower end rested on a biased matched-pair slope, and the "topic vocabulary" gloss describes only part of the measure.)*

## Audit (adversarial review, 2026-10-17)

### What was checked

- **Reproduction.** `core.primary(core.load(), F)` reproduces `primary.json` exactly for both features (n 8,574):
  - G5a: b −0.05676, SE 0.03249;
  - G5b: b 0.07685, SE 0.01434.
- **Holm p.** The values are taken from `primary.json` (G5a 0.348, G5b 1.79e-05). They are consistent with `core.holm` over the 8 frozen p-values and were not recomputed for reporting.
- **Verdicts.** `core.verdict` on the frozen inputs gives the reported verdicts.
  - G5a is "inconclusive": Holm p 0.35, and the CI is not inside ±10%.
  - G5b is "more citations": Holm p < 0.05, with R1 +4.4% and R2 +1.8% both of the same sign.
- **Feature definitions** match prereg §3 and `core.load` / `core.EXTRA_CONTROLS`.
  - G5a = `n_words` / 5. Median 8 and IQR 7–10 were verified.
  - G5b = bge title–abstract cosine, z-scored within year.
  - Extra controls: G1 for G5a; G1 and G5a for G5b.
- **Frozen files.**
  - SHA-256 of `core.py`, `CITES_PREREG.md` and `matched_venue.parquet` match `prereg_hashes.json`.
  - `primary.json` has no git diff. None of these files was edited.
- **Numbers.** Every table in this file was compared with `results.json`, and all matched.
  - Re-running `g5.py` reproduced every pre-existing value in `results.json`. The largest difference was 5e-9, in R7 standard errors (numerical).
- **Labels and scope.**
  - The secondary analyses are exactly those in prereg §6: G5a length bins, the joint 8-feature model, and LLM-topic heterogeneity.
  - Every other block carries "diagnostic (not pre-registered)".
- **Wording.** Observational throughout.

### Errors found and what was changed

1. **Matched-pair diagnostics were biased by the R1 procedure (error).**
   - `g4.py` had shown that R1 is shifted downward when there is no association. G5 interpreted raw R1 and two no-intercept pair-difference slopes without checking this.
   - **The null.** With the feature permuted within year (200 times; terciles and the core R1 pairing rebuilt), the R1 statistic averages:
     - −16.6% for G5a (null 95% range −24.4 to −9.1);
     - −17.1% for G5b (−26.1 to −9.3);
     - −16.7% for MiniLM.
   - **The mechanism.** Nearest-neighbour controls are re-used: 1,387 unique controls serve 2,711 G5b pairs. Under the null they sit +0.15 to +0.16 log points above their year × topic50 cell mean, against about +0.01 for the treated papers.
   - **Calibrated R1:**
     - G5a −7.6% [−16.3, +2.0], placebo p 0.15;
     - G5b **+25.9% [+14.2, +38.9]**, placebo p 0.010;
     - MiniLM +6.5% [−2.7, +16.5].
   - **A check that needs no calibration.** Matching in the reverse direction (each bottom-tercile paper to its nearest top-tercile paper) is shifted by about +21% under the null. The average of the two directions has a null mean of about 0. Observed, that average is −8.6% for G5a and **+22.2%** for G5b. The primary implies −6.3% and +17.1% at these contrasts.
   - **The no-intercept pair slopes** have null means of −11.8% (G5a) and −6.8% (G5b). Net of those, they are −8.7% [−16.6, −0.0] and +8.5% [+2.8, +14.6].
   - **With-intercept slopes** are imprecise: G5a −6.5% [−23.8, +14.6]; G5b −5.0% [−15.6, +6.9].
   - **Changed:**
     - the (d) reading was rewritten;
     - a calibration note was added under the robustness table and the verdict;
     - the MiniLM paragraph, the caveats and the advice sentence were corrected;
     - `results.json` `d_R1_scale.audit_note` was added.
2. **Selective reporting of the centrality control (error in (a)).**
   - The text said that title centrality cuts G5b to +3.0%. It did not report the model already in `results.json` that also controls for abstract (content) centrality: +7.3% [+3.5, +11.2].
   - **Changed:** the (a) bullets and reading, and the "what G5b captures" caveat ("about a third to a half" overlaps with topic-keyword vocabulary).
3. **"Cannot be settled" claims that can be tested.**
   - The bge-PC concern (diagnostic (b)) is now tested: with MiniLM abstract PCs in place of the bge PCs, G5b is +8.3%.
   - The arXiv-id reading (diagnostic (c)) is now tested: mostly a split-record artefact (see below).
   - Both paragraphs were annotated.
4. **Advice sentence.**
   - Replaced the "topic's usual vocabulary" gloss and the "and less under other measures" lower end with a range: about +3% to +9% per SD.
   - The old sentence is kept in italics for the record.
5. **Code.**
   - New module `src/cites/audit_g5g6.py`.
   - `g5.py` adds diagnostic block (g), `diagnostics_not_preregistered.g_audit`, labelled "diagnostic (not pre-registered; added by the adversarial audit)".
   - `g5.py` was re-run. Nothing pre-registered changed.

### Alternative explanations tested — diagnostic (not pre-registered)

Each re-fit uses the primary controls, year × topic50 FE and SEs clustered by topic50, unless stated otherwise. All values are in `results.json` → `diagnostics_not_preregistered.g_audit`.

| Alternative explanation | Test | G5b informativeness (per SD) | G5a length (per +5 words) |
|---|---|---|---|
| R1 procedure artefact | Within-year permutation null; calibrated R1; two-direction (symmetric) pairs | Calibrated R1 +25.9% [+14.2, +38.9]; symmetric +22.2% (null ≈ 0), both at 2.06 SD | Calibrated R1 −7.6% [−16.3, +2.0]; symmetric −8.6% at 1.15 units |
| **S2 split-record artefact** | arXiv-id records only; + arXiv-id indicator (from (c)); mechanism on WP4 pairs | +6.8% [+3.6, +10.2]; +8.2% | −3.6% [−9.9, +3.0]; **−0.2% [−6.0, +6.0]** |
| Content leakage / bge-based PCs | 50 or 100 bge abstract PCs; 20 MiniLM PCs instead of bge | +8.5%, +8.9%, **+8.3% [+5.3, +11.3]** | −6.6%, −6.5%, −5.6% |
| Preprint exposure time | arXiv-id records; months from first arXiv posting to the conference as FE bins | +7.5% [+4.3, +10.8]; lead time unrelated (−0.08 months per SD, p 0.16) | −3.7% [−9.9, +2.8] |
| Promotion / code release | + abstract announces code or a URL | +7.9% [+4.9, +11.0] | −5.0% [−10.8, +1.2] |
| Paper type (method vs findings) | + method and findings indicators; within method / non-method abstracts | +8.0%; +8.0% / +6.3% | −5.5%; −5.6% / −5.5% |
| Superstars / zero-citation records | Within-year percentile outcome; drop top 5% per year; drop zero-citation records | +1.6 points [+1.0, +2.2]; +8.5%; +6.8% | −1.1 points [−2.3, +0.2]; −4.5%; −5.2% |
| Camera-ready retitling | Feature rebuilt on the pre-decision arXiv v1 title, 540 accepted 2023–25 papers (151 retitled; CR–v1 correlation 0.92 / 0.90) | Camera-ready +7.5% [−7.9, +25.6] vs v1 +3.2% [−10.4, +18.8]; same years, full sample +6.0% | Camera-ready −8.0% vs v1 −5.2% (CIs ±30%) |
| Team prior success | R6 vs R5, already pre-registered | +7.1% vs +6.8% | −3.6% vs −3.7% |
| LLM-topic composition | Pre-specified secondary | ratio 0.99 (p 0.67) | ratio 1.12 (p 0.20) |
| All together | arXiv-id records; lead-time FE; code, method and findings indicators | **+7.5% [+4.3, +10.8]** | −3.6% [−9.7, +2.8] |

**The split-record mechanism (WP4 audit pairs, 568 accepted 2023–25 papers, all with a pre-decision arXiv v1).**
- 15.0% of their S2 venue records still have no arXiv id.
- Those records have median 0 citations, against 30 for records with an id. The gap is 2.57 log points [2.25, 2.88] with year FE.
- Retitled papers have an arXiv id less often: 73.5% vs 89.2%, or −14.8 pp [−22.4, −7.2] with year FE.
- Longer titles are retitled more often: +10.5 pp per +5 words [+3.4, +17.6].
- So a missing arXiv id mostly marks a split S2 record, which loses citations, rather than a paper that readers could not find on arXiv. Part of the negative G5a primary is consistent with this measurement artefact.

**Reading.**
- **G5b.**
  - The positive association is not explained by any of the alternatives tested. Every adjusted estimate lies between +6.8% and +8.9%.
  - The matched pairs agree with the primary once the R1 procedure's shift is removed.
  - The remaining uncertainty is about *what* the measure captures: the MiniLM measure gives +4.1%, the name-masked variant +4.3%, and the topic-keyword control +4.5%. The data do not show that a confounder produces it.
  - The retitling test is too small to be informative.
- **G5a.**
  - Every adjustment keeps it between about 0% and −7%.
  - The calibrated matched pairs no longer suggest a large negative association.
  - The arXiv-id control, which plausibly corrects a split-record artefact, brings it to about 0.
- **Not testable with these data.** Lab reputation beyond prior ICLR acceptances, social-media promotion, and quality signals not reflected in the abstract.

### Confidence in the advice

- **G5b sign: high.**
  - It survives the pre-registered rule, R3–R7, the calibrated and symmetric matched pairs, and every alternative explanation tested.
  - One pair-based estimate disagrees: the with-intercept within-pair slope, −5.0% [−15.6, +6.9]. It is imprecise.
- **G5b size: medium.** About +3% to +9% per SD, depending on the similarity model and on whether shared names and topic keywords count as informativeness.
- **G5a: high confidence that these data show no reliable length association.** The verdict stays "inconclusive". The small negative primary is partly an S2 split-record artefact.
- **The revised one-sentence advice stands.** It remains an association. It does not show that rewriting a given title to be closer to its abstract would raise its citations.
