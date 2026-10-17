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
- **Split-record QC sample** (`qc_split_records.jsonl`, final: 30 records, `qc_split.log` ends with DONE; numbers corrected in the audit, see below).
  - 30 venue records without an arXiv id were checked, and 7 were split. The separate record always had more citations: the venue record had 0 against 11–20 (4 cases), 1 against 16, 12 against 82, and 46 against 599.
  - Split records occur among both groups: 6 of 24 unnamed papers and 1 of 6 named papers.
  - The sample is too small to compare by G1. It does show that the artefact is real but affects only the roughly 23% of records without an arXiv id, and that share does not differ by G1.
- **Match rate.** Named titles are matched to an S2 venue record less often.
  - Named 95.7% (n 2,200) vs other 97.4% (n 6,673) of accepted papers 2017–25.
  - With year FE the difference is −1.7 pp (−2.7, −0.8).
  - A Lee-style trimming bound treats the excess unmatched named papers as missing at either extreme of y. Trimming 127 papers, year by year, gives **+16.9% (+8.5, +25.9) to +33.0% (+23.1, +43.6)**.

**Reading.** The split-record artefact and the matching differences do not explain the association.

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
  - Reviewers are neutral to named titles, so the citation association is not a by-product of reviewers favouring them.
- **Exposure and outcome.**
  - The exposure is the camera-ready title. Citations for 2024–25 papers cover only 1–2 years.
  - Year FE absorb citation age, and R5 shows similar values in 2017–21 (+25.6%) and 2022–25 (+21.7%).
  - Counts are a single S2 snapshot (2026-10-17). About 3% of accepted papers from 2017–25 are unmatched: 4.3% of named vs 2.6% of other papers. The trimming bound is above.
- **Secondary analyses** (orthography, joint model, LLM heterogeneity) carry no multiplicity correction. **Diagnostics** were added after seeing the primary and are labelled as such. The orthography and method-paper contrasts are suggestive only.
- **Measurement.** G1 is the validated rule-based NAME detector (precision 97.8%, recall 97.3%; `outputs/SUMMARY.md`, V1). The method-paper regex is crude and unvalidated.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles lead with a coined method name ("NAME: subtitle") receive about 22% more citations on average (95% CI +13% to +32%; about +8% in content-matched pairs); this is an association, not evidence that adding a name would raise a given paper's citations.

## Audit (adversarial review, 2026-10-17)

### What was checked

- **Reproduction.** `core.primary(core.load(), "G1_name")` reproduces `primary.json` exactly: b 0.20264, SE 0.03884, n 8,574, 2,105 named.
  - Holm p 2.56e-05 is taken from `primary.json`.
  - That value is consistent with `core.holm` over the 8 frozen p-values. It was not recomputed for reporting.
- **Verdict.** Holm p < 0.05, R1 is +8.4% (same sign) and R2 is +38.0% (same sign). So "more citations" follows the pre-registered rule.
- **Feature definition.** `G1_name` is `name_primary` (`name_colon`), exactly as frozen in `core.load`.
  - The four orthography dummies partition `G1_name` exactly: no unnamed title carries an orthography flag. The secondary's reference group is therefore exactly "no name".
- **Frozen files.**
  - SHA-256 of `core.py`, `CITES_PREREG.md` and `matched_venue.parquet` match `prereg_hashes.json`.
  - `primary.json` is unchanged in git.
- **Numbers.** Every number in this file was compared with `results.json`. All match, except the split-record QC counts (fix 1).
- **Background claims.** Checked against `outputs/SUMMARY.md`:
  - NAME detector precision 97.8% and recall 97.3%;
  - NAME accepted/all ratio 1.021, editing-corrected 90% CI 0.949–1.031;
  - 0 of 18 auditable features pass.
- **Labels and wording.**
  - Every non-pre-registered block in `results.json` carries "diagnostic (not pre-registered)".
  - The advice sentence uses observational wording.

### What was changed

1. **Stale QC counts (error).**
   - The original run wrote `results.json` at 10:40. `qc_split_records.jsonl` was still being appended until 10:44, finishing at 30 records.
   - The text reported 24 checked, 5 split, "all on unnamed papers". The final file gives **30 checked, 7 split: 6 of 24 unnamed, 1 of 6 named**.
   - `g1.py` was re-run. The QC block was the only pre-existing value that changed, and every other number reproduced identically.
2. **Wording.**
   - "cannot explain" became "do not explain".
   - "Titles that go with more citations are not titles that reviewers favour" was replaced by a statement of what the reviewer-side evidence shows: neutrality.
3. **Audit diagnostics added.** These are the alternative explanations below.
   - Code: new module `src/cites/audit_g1g2.py`, called from `g1.py`.
   - Results: `results.json` → `diagnostics_not_preregistered.d_audit_alt_explanations`.

### Alternative explanations tested — diagnostic (not pre-registered)

Each re-fit uses the primary controls, year × topic50 FE and SEs clustered by topic50, unless stated otherwise.

| Alternative explanation | Test | Result for G1 |
|---|---|---|
| **Preprint exposure time.** Named papers might be on arXiv longer. | arXiv-id records. Months from first arXiv posting (from the id) to the conference, entered as FE bins. | Named papers are posted 6.8 vs 6.6 months before the conference (adjusted +0.08 months, p 0.56). G1 is +20.6% on arXiv-id records and **+19.0% [+10.4, +28.2]** with the lead-time FE. |
| **Promotion / code release.** | Abstract announces code or a URL. | Named 35.4% vs 17.3%. The indicator itself is +37.4% [+27.7, +48.0]. G1 with it: **+19.5% [+10.7, +29.0]**. Within code abstracts +15.4% [−1.0, +34.5] (745 named); within others +18.4% [+8.9, +28.8]. |
| **Paper type** (method vs findings paper). | Method and findings abstract indicators (crude regexes). | Named abstracts announce a method more often (82.7% vs 62.7%) and a finding less often (31.4% vs 51.1%). G1 with both indicators: **+23.2% [+14.2, +32.9]**. Within findings abstracts +21.0% [+8.2, +35.4]. |
| **Superstar outliers.** | Within-year citation percentile as the outcome. Drop the top 5% per year. Drop zero-citation records. | Percentile: **+3.8 points [+2.3, +5.3]**. Top 5% dropped: **+14.8% [+7.6, +22.4]**. Zero-citation records dropped: +20.3%. Named titles are 42% of each year's top 5% and 46% of the top 1%, against 24.5% overall. |
| **Retitling / reverse causation.** Early attention could lead authors to add a name at camera-ready. | WP4 audit pairs: arXiv v1 titles posted before the decision, for 568 accepted 2023–25 papers in this sample. | Name status changed for only 22 papers (3.9%): 10 added, 12 removed. On the same papers, the camera-ready exposure gives +7.4% [−24.9, +53.6] and the pre-decision v1 exposure gives +6.1% [−23.8, +47.7]. |
| **All of the above together.** | arXiv-id records; lead-time FE; code, method and findings indicators. | **+17.9% [+9.6, +26.8]** |

**Reading.**
- None of these explanations removes the association. The estimate stays between about +15% and +23% under every adjustment.
- **Heavy tail.** Part of the log-scale average comes from named papers being over-represented among the most-cited papers. Dropping the top 5% per year lowers it from +22.5% to +14.8%. The rank-based outcome (+3.8 percentile points) shows that the association is not only in the tail.
- **Retitling.** Retitling is too rare to drive the association. The name is almost always present in the pre-decision arXiv title.
- **The audited subsample.** The small G1 estimate in that subsample is imprecise, and it does not differ detectably from the rest of 2023–25: ratio 0.84 [0.64, 1.10], p 0.22. Pre-decision preprints across 2023–25 as a whole show +20.4% [+9.1, +32.9].
- **Code links.** Code-link abstracts absorb only a little: +22.5% falls to +19.5%. The indicator may partly be a consequence of naming and releasing a method, rather than a confounder.
- **Not testable with these data.** Lab reputation beyond prior ICLR acceptances, social-media promotion, and quality signals not reflected in the abstract.

### Confidence in the advice

- **Sign: high.** It survives the pre-registered rule, every robustness check and every alternative tested here.
- **Size: medium.**
  - The regression estimate is +22.5%.
  - It is +15% to +18% once outliers or promotion proxies are handled.
  - Content-matched pairs give +5.6% to +8.4%.
- The one-sentence advice stands as written, and the size should be quoted as a range (about +5% to +25%). It remains an association: it does not show that adding a name to a given paper would raise its citations.
