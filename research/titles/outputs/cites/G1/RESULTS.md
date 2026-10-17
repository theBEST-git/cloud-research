# G1: coined method names ("NAME: subtitle") and citations

**Code:** `src/cites/g1.py`. **Numbers:** `outputs/cites/G1/results.json`. **Figure:** `outputs/cites/G1/fig.png`.
**Pre-registration:** `docs/CITES_PREREG.md` (frozen 2026-10-17). **Frozen core:** `src/cites/core.py` (not edited).

## Question

Among accepted ICLR papers from 2017 to 2025, do papers whose title leads with a coined method name ("LoRA: …", "CRISP: …") get more or fewer Semantic Scholar citations than accepted papers with similar content?

- **Sample.** 8,602 accepted papers matched to an S2 venue record.
  - 8,574 papers enter the regression; singleton year × topic50 cells are dropped.
  - 2,105 of the papers (24.5%) have a named title.
- **Outcome.** y = log(1 + citations), with citations retrieved 2026-10-17.
- **Model.** `y ~ G1_name + log(team size) + log(abstract words) + 20 abstract-embedding PCs | year × topic50`, with SEs clustered by topic50.
- **Effect scale.** % difference = exp(b) − 1.

## Primary estimate (pre-registered)

| | % difference in citations | 95% CI | p | Holm p (8 tests) | n | n named |
|---|---|---|---|---|---|---|
| G1 named title | **+22.5%** | +13.5% to +32.1% | 3.7e-06 | **2.6e-05** | 8,574 | 2,105 |

- The estimate and Holm p are taken from `outputs/cites/primary.json`.
- Re-computing them with `core.primary` reproduces the estimate exactly: largest absolute difference 0, same n.

## Robustness checks R1–R7 (pre-registered, `core.robustness`)

| Check | % difference | 95% CI | p | n |
|---|---|---|---|---|
| Primary | +22.5% | +13.5, +32.1 | 3.7e-06 | 8,574 |
| R1 content-matched pairs (name-masked embedding, cosine ≥ 0.80) | +8.4% | +0.2, +17.3 | (bootstrap) | 2,065 pairs |
| R2 PPML on raw counts (sign check only) | +38.0% | +8.1, +76.3 | 0.0098 | 8,574 |
| R3 influential-citation count | +24.4% | +15.6, +33.8 | 4.0e-07 | 8,574 |
| R4 drop top 1% most-cited per year | +19.6% | +11.2, +28.6 | 1.4e-05 | 8,481 |
| R5 2017–21 only | +25.6% | +2.3, +54.1 | 0.035 | 1,975 |
| R5 2022–25 only | +21.7% | +12.3, +31.9 | 1.5e-05 | 6,599 |
| R6 2022–25 + team's prior ICLR acceptances | +22.0% | +12.7, +32.0 | 1.0e-05 | 6,599 |
| R7 year + topic100 FE | +23.7% | +15.5, +32.6 | 2.0e-07 | 8,602 |

All checks have the same sign. R3–R7 are within about 4 points of the primary. R2 (PPML, a sign check) is larger. **R1 is about a third of the primary's size**, and its CI only just excludes zero (see the content-granularity diagnostic below).

## Verdict (pre-registered rule)

**"More citations."** The rule requires three things, and all three hold:
- Holm p = 2.6e-05 < 0.05.
- R1 matched pairs has the same sign (+8.4%).
- R2 PPML has the same sign (+38.0%).

The rule fixes the sign, not the size. The diagnostics below give a size range from about +5% to +25%, depending on how content is held fixed.

## Secondary analyses (pre-specified in prereg section 6; no multiplicity claim)

**Name orthography, each class vs no-name.** This is one model with all orthography dummies, so the reference group is exactly the papers with no name.

| Name orthography | n | % difference vs no-name | 95% CI | p |
|---|---|---|---|---|
| mixed case (e.g. LoRA, GPT-4V) | 1,355 | **+29.7%** | +18.1, +42.3 | 1.5e-06 |
| ALL CAPS (e.g. CRISP) | 608 | +8.5% | −3.6, +22.0 | 0.18 |
| ordinary word (e.g. Chameleon) | 134 | +28.7% | +4.2, +58.9 | 0.023 |
| phrase (ACRONYM), residual class, not interpreted | 8 | −22.5% | −73.0, +122.4 | 0.64 |

**Joint model with all 8 primary features.** G1 is +23.3% (+14.0, +33.3), p 3.2e-06. Holding the other title features fixed, including length and informativeness, leaves G1 unchanged.

**Heterogeneity by LLM-topic papers.**

| Group | % difference | 95% CI | n named |
|---|---|---|---|
| LLM-topic papers | +20.2% | +2.3, +41.1 | 698 |
| other papers | +23.7% | +13.4, +35.0 | 1,407 |

The ratio of the two multipliers is 0.97 (0.81, 1.17), p 0.76, so there is no evidence of a difference.

## Diagnostics — diagnostic (not pre-registered)

### (a) Artefact check: S2 split records and matching

S2 sometimes keeps a venue record without an arXiv id separate from the arXiv record, and the arXiv record collects the citations. If named papers had a different share of such records, the primary estimate would be biased.

- **arXiv-id share among matched records.** Named 77.5% vs other 76.6%. With the primary controls the difference is +1.0 pp (−1.6, +3.6), p 0.44. Records with several S2 matches are 0.19% vs 0.15%.
- **Primary spec on records with an arXiv id only.** **+20.6% (+11.2, +30.9)**, n 6,575, 1,631 named.
- **Records without an arXiv id only.** +16.7% (+1.7, +33.8), n 1,926, 474 named.
- **Difference between the two subsets, in one model.** Ratio 0.97 (0.83, 1.13), p 0.68.
  - In this model the controls and the year × topic50 FE are interacted with arXiv status.
  - A version that shared the FE across arXiv status gave a spurious difference (p 0.003). Having an arXiv id shifts y by about 1 log point, so that version was not used.
- **Primary spec plus an arXiv-id indicator.** +21.0% (+12.7, +29.9).
- **Split-record QC sample** (`qc_split_records.jsonl`; the file was still being appended during this run, so n will differ on a re-run).
  - 24 venue records without an arXiv id were checked, and 5 were split. The venue record had 0 citations against 11–20 on the other record, or 12 against 82.
  - All 5 split records were on unnamed papers: 5 of 21 unnamed, 0 of 3 named.
  - The sample is too small to compare by G1. It does show that the artefact is real but affects only the roughly 23% of records without an arXiv id, and that share does not differ by G1.
- **Match rate.** Named titles are matched to an S2 venue record less often.
  - Named 95.7% (n 2,200) vs other 97.4% (n 6,673) of accepted papers 2017–25.
  - With year FE the difference is −1.7 pp (−2.7, −0.8).
  - A Lee-style trimming bound treats the excess unmatched named papers as missing at either extreme of y. Trimming 127 papers, year by year, gives **+16.9% (+8.5, +25.9) to +33.0% (+23.1, +43.6)**.

**Reading.** The split-record artefact and the matching differences cannot explain the association.

### (b) Method-paper confound

The indicator is set when the abstract matches `we propose|we introduce|we present|this paper proposes`.

- **Share of such abstracts.** Named 82.7% vs other 62.7%. With the primary controls the difference is +8.7 pp (+6.6, +10.8).
- **Primary spec plus the indicator.** G1 is **+22.4% (+13.5, +32.0)**, unchanged. The indicator itself is unrelated to citations: +0.6% (−4.4, +5.8).
- **Within method-announcing abstracts.** +27.3% (+15.6, +40.1), n 5,773, 1,741 named.
- **Within other abstracts.** +8.2% (−4.2, +22.2), n 2,720, 364 named.
- **Interaction.** Ratio 1.17 (1.00, 1.37), p 0.056.

**Reading.** Being a "method paper", as this crude regex measures it, does not account for the association. There is a suggestive, not established, sign that the association is concentrated among papers that announce a method.

### (c) Team prior (pre-registered R6 compared with R5 on the same 2022–25 sample)

- Named-title teams have slightly more prior ICLR acceptances: mean log(1 + prior acceptances) 1.12 vs 1.01.
- The team-prior control predicts citations: +14.8% per log unit (+9.8, +19.9).
- Adding it leaves G1 unchanged:
  - without the control (R5): +21.7% (+12.3, +31.9);
  - with the control (R6): +22.0% (+12.7, +32.0);
  - change in b: +0.002.

### Orthography follow-ups

Pairwise ratios of citation multipliers between orthography classes, from the primary model:

| Comparison | Ratio | 95% CI | p |
|---|---|---|---|
| ALL CAPS vs mixed case | 0.84 | 0.73, 0.95 | 0.011 |
| word vs mixed case | 0.99 | 0.78, 1.26 | 0.95 |
| word vs ALL CAPS | 1.19 | 0.93, 1.52 | 0.18 |

Content-matched pairs, each class vs no-name (R1 method):

| Name orthography | % difference | 95% CI | Pairs |
|---|---|---|---|
| mixed case | **+15.8%** | +5.1, +28.0 | 1,326 |
| ALL CAPS | −2.5% | −15.3, +12.7 | 599 |
| word | −7.2% | −31.9, +26.3 | 132 |

**Reading.** Only mixed-case names are positive in both the regression and the matched pairs. ALL-CAPS names show no clear difference from unnamed titles. The ordinary-word estimate rests on 134 papers and is not supported by matched pairs.

### Content granularity: why is R1 smaller than the primary?

- **Reimplemented R1 pairing.** Reproduces core R1 exactly: 2,065 pairs, +8.38%.
- **Team size inside the pairs.** In the pairs, the named paper has a larger team: +0.088 log authors on average. R1 does not adjust for this.
  - Regressing the within-pair difference on the within-pair differences in log team size and log abstract words gives **+5.6% (−4.7, +17.0)**, p 0.30.
  - So adjusting for team size makes R1 smaller, not larger.
- **Tighter calipers.**
  - Cosine ≥ 0.85: +12.1% (+1.8, +22.6), 1,520 pairs.
  - Cosine ≥ 0.90: +25.2% (+2.6, +52.0), 313 pairs.
  - The matched estimate does not shrink steadily as content matching tightens.
- **More content PCs in the primary spec.**

  | PCs | Unmasked embedding | Name-masked embedding |
  |---|---|---|
  | 20 | +22.5% (+13.5, +32.1) | +20.8% (+12.1, +30.1) |
  | 50 | +20.0% (+11.4, +29.3) | +18.1% (+10.0, +26.9) |
  | 100 | +18.0% (+9.5, +27.1) | +17.4% (+9.2, +26.2) |

**Reading.** Finer content controls shrink the regression estimate modestly, from 22% to about 17–18%, and it stays clearly positive. Matched-pair estimates are smaller and noisier (6–12% at the pre-registered and 0.85 calipers; 25% at 0.90). The sign holds across methods. The size is uncertain, roughly +5% to +25%.

## Interpretation and caveats

- **Observational.** Authors choose titles. Teams that expect their method to be reused, or that promote it more (code releases, talks, social media), may both name it and get more citations. Content controls, matched pairs, the method-paper indicator and the team-prior control do not remove this. None of the above shows that adding a name would raise a given paper's citations.
- **Size depends on the content adjustment.** The pre-registered primary is +22.5%. Content-matched pairs give +8.4%, or +5.6% after a pair-level team-size adjustment, with a CI that includes zero. Quote the sign with confidence and the size as a range.
- **Selection into the sample.** Only accepted ICLR papers are included.
  - On the reviewer side, naming does not predict acceptance: NAME accepted/all ratio 1.02, editing-corrected 90% CI 0.949–1.031, from `outputs/SUMMARY.md`.
  - So differential acceptance of named titles is unlikely to create this association through selection. It does not rule out that named and unnamed accepted papers differ in unmeasured quality.
  - Titles that go with more citations are not titles that reviewers favour.
- **Exposure and outcome.**
  - The exposure is the camera-ready title. Citations for 2024–25 papers cover only 1–2 years.
  - Year FE absorb citation age, and R5 shows similar values in 2017–21 (+25.6%) and 2022–25 (+21.7%).
  - Counts are a single S2 snapshot (2026-10-17). About 3% of accepted papers from 2017–25 are unmatched: 4.3% of named vs 2.6% of other papers. The trimming bound is above.
- **Secondary analyses** (orthography, joint model, LLM heterogeneity) carry no multiplicity correction. **Diagnostics** were added after seeing the primary and are labelled as such. The orthography and method-paper contrasts are suggestive only.
- **Measurement.** G1 is the validated rule-based NAME detector (precision 97.8%, recall 97.3%; `outputs/SUMMARY.md`, V1). The method-paper regex is crude and unvalidated.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles lead with a coined method name ("NAME: subtitle") receive about 22% more citations on average (95% CI +13% to +32%; about +8% in content-matched pairs); this is an association, not evidence that adding a name would raise a given paper's citations.
