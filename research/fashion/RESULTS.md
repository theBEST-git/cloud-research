# Research fashions at ICLR 2017–2026: results

All confirmatory tests follow `PREREGISTRATION.md`: hypotheses and decision rule as registered, plus a dated pre-run log
of every clarification, replacement and deviation, written before any RQ2/RQ3 estimate existed. RQ2 and RQ3 were run
once, by `run_frozen.py`, on code frozen in `FREEZE.json` (commit e08ece3, attempt 1). Its outputs are in
`output/frozen_run/` exactly as written; they were committed before interpretation.

All results are associations within topic and year. None is a causal effect of choosing a topic, a team or a
contribution type.

## Summary

| | Prediction | Main estimate (95% CI) | Holm p | Same sign as predicted in counted variants | Verdict |
|---|---|---|---|---|---|
| H1a | method ~ maturity (−) | −0.14 pp per log unit (−1.8, +1.5) | 1.0 | 78% | not supported |
| H1b | measurement ~ maturity (+) | +0.50 pp (−0.8, +1.8) | 1.0 | 89% | not supported |
| H1c | empirical ~ maturity (+) | −0.31 pp (−1.3, +0.7) | 1.0 | 0%; hindsight fails | not supported |
| **H1d** | **new architecture ~ prior FM adoption (−)** | **−8.0 pp for 0 → 100% FM (−12.1, −3.8)** | **0.001** | **100%** | **supported** |
| H1e | empirical or evaluation ~ prior FM adoption (+) | −0.6 pp (−3.6, +2.4) | 1.0 | 44% | not supported |
| H2a | incumbent ~ hot topic (−) | −0.73 pp (−2.68, +1.22) | 0.46 | 80%; hindsight fails | inconclusive |
| **H2b** | **method ~ newcomer (−)** | **+3.71 pp (+2.61, +4.80)** | **< 0.001** | **0%: all 10 positive** | **significant in the opposite direction** |
| **H2c** | **measurement ~ newcomer (+)** | **−1.70 pp (−2.46, −0.93)** | **< 0.001** | **0%: all 10 negative** | **significant in the opposite direction** |
| H3a | accepted ~ maturity (−) | −1.68 pp per log unit (−3.68, +0.32) | 0.20 | 100% | inconclusive (underpowered) |
| H3b | accepted ~ maturity × method (−) | −0.36 pp per log unit (−1.51, +0.79) | 0.53 | 91% | inconclusive |

H2d and H3c (buzzword use) were dropped before any estimate, because the measure failed its blind validation.
None of the five RQ2/RQ3 hypotheses is supported, and none is "equivalent to null": every 90% CI reaches beyond the
smallest effect of interest (E9).

- **Following fashions (RQ2).**
  - Newcomer papers (no author with an earlier ICLR submission in the same topic, any outcome; exact author IDs) are
    more often method papers than papers with at least one such author: +3.7 pp on a 75% base.
  - They are less often dataset, benchmark or evaluation papers: −1.7 pp on a 7.7% base, about a fifth fewer.
  - Both run against the registered predictions. Both hold, with the same sign and p < 0.05, in all ten counted
    variants, under two-way clustering and under the pre-declared stress sensitivity (a single-scenario bracket).
  - With team size controlled (S1), the measurement gap shrinks by about two-thirds, to −0.54 pp (p = 0.07). The
    method gap is unchanged.
  - H2a is inconclusive: no detectable difference in the share of incumbent papers between hot and other topics.
- **Reward (RQ3).**
  - H3a is inconclusive: −1.7 pp per log unit of prior papers (95% CI −3.7 to +0.3; p = 0.099, Holm p = 0.20). All 11
    counted variants are negative, but they re-estimate on the same papers. The test was underpowered (MDE80 about
    4 pp per log unit), so the result is uninformative about smaller effects. It is evidence neither of an effect nor
    of no effect.
  - H3b is inconclusive: whether method papers fare worse than other classes in mature topics cannot be told (−0.36 pp
    per log unit, 95% CI −1.51 to +0.79). Equivalence within ±1 pp is not established (TOST p = 0.14).
- **Exploratory (labelled, unadjusted).**
  - Within the same topic and year, all-newcomer papers are accepted 10 pp less often than papers with an incumbent
    author.
  - Papers building on foundation models are accepted 4.6 pp more often, and theory papers 8.9 pp more often than
    method papers.

## Data

- **Corpus:** the discovery split, 43,480 ICLR submissions (2017–2026) with a usable abstract.
- **Topics:**
  - 100 content-based middle-level topics (k100) form the main map;
  - k75, k150, a year-balanced map and an early (2017–2020) map serve as robustness and hindsight variants;
  - 198 fine topics are supplementary (S5).
- **Contribution labels:** one primary contribution type per paper, from a fixed LLM codebook (prompt v1).
  - Checked against 2,300 reference papers labelled by LLM annotators, not by human experts. Main-class agreement is
    95.8% overall (pilot 300, two annotators plus adjudication: 97.7%; training 200 double-labelled: 95.5%; training
    1,800 single-labelled: 95.6%). This shows consistency between LLM labellings more than human-level validity.
  - A blind second pass on 2,174 papers: κ 0.93 overall; method κ 0.933, measurement κ 0.949.
  - On the random reference stratum, the false-positive / false-negative rates are 0.084 / 0.011 for method and
    0.005 / 0.070 for measurement, relative to those LLM reference labels. S8 rescales the RQ2 estimates by them.
- **RQ2 population:** papers with at least one author ID, 2019–2026 (42,325 papers; 42,315 after dropping singleton
  topic-year cells for H2b/H2c).
- **RQ3 population:** the registered filter (ordinary submissions with a final accept/reject decision), 2018–2026,
  32,190 papers; 40.1% accepted.

## Constructed variables and their validity

- **Incumbent / newcomer.**
  - A paper is *incumbent* if at least one author ID has an earlier discovery submission (any outcome) in the same
    topic; it is a *newcomer* paper if none has. Exact author IDs only.
  - ICLR switched from email to profile author IDs in 2021–22, and the two are not linked. This hides pre-2021 history
    in all later years, turning some true incumbents into newcomers; registration D2 treats this as a bias towards
    zero. k100 incumbency falls from 18% (2020) to 0.5% (2021), then recovers to 18% (2022) and 33% (2026).
  - The counted R2 variant drops only the 2021–22 transition years.
- **Hot topic:** prior growth (share in t−1 over share in t−2) in the top fifth of topics that year. Among the topics
  with papers in a year, that is 20 per year, except 33 in 2019 (ties at the threshold) and 19 in 2022.
- **Buzzword use** (a fast-growing keyword used atypically) **failed its blind validation.** Three LLM judges rated
  flagged uses peripheral in 42% of cases (95% CI 33–52%), against 15% for matched non-flagged uses; the registered
  gate needed ≥ 50%. H2d and H3c were dropped before any estimate. Exploratory rows that use the measure are labelled
  as such and not interpreted.
- **Probable earlier versions** (R1, S4): 170 papers are flagged. 167 have an earlier paper at centred SPECTER2
  cosine ≥ τ = 0.90, and 3 more have an earlier paper with an identical normalised title. τ was calibrated by blind
  judges (yes-rates 10%, 48%, 90% and 100% across four cosine bins).

## Protocol

- **Pre-registration.**
  - Hypotheses, models, the support rule and robustness variants were registered before any full-corpus label
    existed (only the 2,300 validation papers had labels, and no RQ analysis had been run on them).
  - The registration also discloses earlier exploratory work on keyword popularity and acceptance in the same corpus.
  - Every later clarification, replacement and addition is a dated entry in the pre-run log of `PREREGISTRATION.md`,
    written before the frozen run. This includes the finer verdict labels for non-supported hypotheses and the fragile
    flag.
  - Logged deviations include:
    - full-corpus labels were produced with Claude Haiku (prompt v1 unchanged) instead of the planned external run;
    - the H2d and τ judges were Sonnet/Haiku instead of Opus/Sonnet;
    - two dry-run launches were stopped before any result was seen.
- **Outcome blindness.**
  - Only `outcomes.py` may read acceptance or review columns, enforced by a lint test.
  - Its real mode refuses to run unless the caller is `run_frozen.py`, `FREEZE.json`'s hashes match, the git tree is
    clean and no debugger is attached.
  - The real RQ2 labels are guarded the same way. Before the freeze, every analysis using them as an outcome ran on
    simulated values, with one disclosed exception (Reviews, below).
- **Decision rule.** A hypothesis is *supported* only if all of the following hold:
  - its main estimate has the predicted sign;
  - its Holm-adjusted p is below 0.05 within its family;
  - at least 75% of the counted variants have the predicted sign;
  - both hindsight variants have the predicted sign (year-balanced map; early map on 2021–2026 papers).

  Otherwise the verdict is one of:
  - "significant in the opposite direction": Holm p < 0.05 with the wrong sign;
  - "equivalent to null": 90% CI inside the smallest effect of interest (SESOI);
  - "inconclusive".

  A supported hypothesis is flagged *fragile* if a supplementary variant is significant against the prediction.
- **Dry-runs before the freeze.** Two runs of 12,400 simulated jobs each, with the same seeds, measured size, false
  support of the full rule, and power:
  - the RQ2 null scenarios are calibrated on the corpus's own topic-year structure;
  - the RQ3 nulls use fixed parameters (base rate 0.32, two variance settings), plus a within-year permutation of the
    real acceptance outcomes;
  - the power grids range from 0.5 to 6 times the SESOI.
- **Remedy.**
  - Under a null whose structure cuts across k100 topics, the main test of H2b/H2c rejected 12.6% / 10.0% of the time
    at nominal 5%.
  - As registered, their confirmatory p-values therefore come from a wild cluster restricted bootstrap (Rademacher by
    k100 topic, null imposed, 9,999 draws).
  - The validation run showed that the bootstrap does not fix this (12.4% / 9.6%). That result is reported, not
    hidden.
  - Two reporting checks were declared before any estimate, and neither changes a verdict:
    - S11, a two-way clustered re-estimate (k100 topic and early-map topic) that attaches a qualifier if it disagrees;
    - a stress sensitivity that brackets the H2b/H2c p-values using the one simulated scenario (below).
- **Reviews.** Nine adversarial review rounds (A, B, B2–B8) by fresh agents, covering prospectivity, blinding,
  conformance, numerics, data plumbing, remedy statistics, wiring, methodology and test strength.
  - Every reported blocker or major finding was checked by a separate verifier and logged.
  - Confirmed findings were fixed, and code fixes were mutation-tested.
  - Rejected or downgraded findings were documented rather than fixed, e.g. round B3's loader-circumvention point.
  - Two blinding incidents are disclosed in the log: during round B a reviewer saw one real exploratory estimate on
    the failed buzzword measure (E7), and the analyst once read the value sets of outcome columns.
- **One run.** `FREEZE.json` was committed first: the sha256 of 68 code and input files, the gate, τ, the variants,
  the SESOIs, MDE80, the remedies and the stress factors. `run_frozen.py` then ran once (attempt 1, 18 seconds).

## RQ1: rise (pre-registered, finished earlier)

`output/rq1_summary.json`. 43,096 papers from 2018–2026, 100 topics. Linear probability models with topic and year
fixed effects, SE clustered by topic.

- **Maturity (H1a–c).** Within a topic, the contribution mix does not move detectably with how many papers the topic
  has accumulated.
  - Net of field-wide year trends, the 95% intervals exclude effects larger than about 1–2 pp per log unit. This is a
    post hoc equivalence reading.
  - Under the prospective early map the estimates point the predicted way (exploratory), so whether lifecycles appear
    depends on how topics are defined.
- **Foundation models (H1d–e).** When more of a topic's papers built on foundation models in the previous year, fewer
  of its papers propose new architectures.
  - The main estimate is −8.0 pp for 0 → 100% FM share, and the variants range from −6.3 to −14.2 pp, against a mean
    of 9.2%.
  - The expected shift towards empirical and evaluation work (H1e) is not found.

## RQ2: following

`output/frozen_run/rq2_results.csv`, `summary.json`; Figure `output/figures/F1_forest.png`. Label reliability (D11):
second-pass κ 0.93 overall; method κ 0.933 (agreement 97.5%), measurement κ 0.949 (99.3%).
- **Model:** linear probability models with SE clustered by k100 topic (100 clusters), 2019–2026.
- **Fixed effects:** topic and year for H2a; topic × year cells for H2b/H2c.
- **Base rates:** incumbent 27.0%, hot 26.1%, method 75.0%, measurement 7.7%, newcomer 72.9%.

### H2a: do hot topics have fewer incumbent papers? Inconclusive

- **Main estimate:** −0.73 pp (95% CI −2.68 to +1.22; p = 0.46).
- **Variants:** 8 of 10 have the predicted sign. Two have the wrong sign:
  - the year-balanced map, +1.05 pp. It is a hindsight variant, so the hindsight requirement fails.
  - k150, +0.37 pp.
  - The two early-map variants are negative and nominally significant: the early map −1.62 pp (p = 0.03), and the
    early map on 2021–2026 papers −1.55 pp (p = 0.045).
- **Equivalence:** not established (TOST p = 0.10; 90% CI −2.37 to +0.90 against ±2 pp).
- **Supplementary:** pool controls −1.43 pp (p = 0.09); two-year incumbency window, 2023–2026, +0.23 pp.
- **Reading:** no reliable difference. Effects down to about −2.4 pp (90% CI) cannot be excluded, and the dry-run
  MDE80 is 3.6 pp.

### H2b and H2c: newcomer papers are more often method papers and less often measurement papers (opposite to the predictions)

| | Main (95% CI) | Counted variants (all 10 same sign) | Two-way S11 (Holm p) | Stress sensitivity (Holm p) |
|---|---|---|---|---|
| H2b method | +3.71 pp (+2.61, +4.80); t = 6.7 | +2.16 to +3.87 pp, all p < 0.05 | +3.71 pp (4 × 10⁻⁸) | 4 × 10⁻⁶ |
| H2c measurement | −1.70 pp (−2.46, −0.93); t = −4.4 | −1.81 to −0.86 pp, all p < 0.05 | −1.70 pp (2 × 10⁻⁴) | 1 × 10⁻³ |

- **Confirmatory p-values:** wild cluster restricted bootstrap. No draw of 9,999 reached |t| for either hypothesis, so
  p < 1/9,999 and Holm p < 0.001. CR1 p is 1.1 × 10⁻⁹ (H2b) and 2.7 × 10⁻⁵ (H2c).
- **Verdict:** both are "significant in the opposite direction". The pre-declared S11 check agrees in each case, so no
  qualifier is attached.
- **Robustness:**
  - The two hindsight variants point the same (opposite) way. Year-balanced map: +3.10 / −1.41 pp. Early map on
    2021–26: +2.16 / −0.86 pp.
  - The supplementary variants also agree. In the output, these appear under `fragile_by`, which lists S-variants
    significant against the *prediction*, i.e. with the observed sign:
    - log team size (S1): H2b +3.92 pp;
    - fine topics (S5): +3.57 / −1.62 pp;
    - two-year window (S3): +3.20 / −1.77 pp;
    - excluding the paper's own earlier versions (S4): +3.77 / −1.69 pp;
    - label misclassification correction (S8): +4.09 / −1.84 pp. S8 rescales the main estimate by 1/(1 − FP − FN), so
      it can only enlarge it, and it assumes misclassification does not differ between newcomer and incumbent papers.
- **Team size and H2c.** With log team size controlled (S1), H2c shrinks to −0.54 pp (p = 0.07), while H2b is
  unchanged. Larger teams are mechanically more likely to contain an incumbent, so much of the measurement gap is
  accounted for by team size (in the statistical sense, within topic and year). It should be read as partly a
  difference between small all-new teams and larger mixed teams.
- **By era (E4, exploratory).**
  - H2b is positive in every era: 2019–20 +5.5 pp (p = 0.009); 2021–23 +3.4 pp (p = 0.008); 2024–26 +3.6 pp.
  - H2c is concentrated in 2024–26: −2.0 pp (p < 0.001), against −0.5 pp (n.s.) in each earlier era.
- **Hot topics (E5, exploratory).** There is no detectable difference in either gap between hot and other topics
  (newcomer × hot: −0.4 and −0.6 pp, both n.s.).
- **How much to trust these p-values.**
  - Under a simulated null with topic structure cutting across k100 topics, the registered test rejects about 10–12%
    of the time at nominal 5%, and the bootstrap does not fix this.
  - The registered decision rule offers no extra protection against that structure. All main-specification false
    positives also passed the robustness and hindsight requirements.
  - The two opposite-direction findings are large relative to the inflation seen in simulation: t = 6.7 and −4.4.
    Dividing them by the t inflation in the one simulated cross-map scenario (1.31 and 1.22) still gives Holm p of
    4 × 10⁻⁶ and 1 × 10⁻³, and two-way clustering (S11) agrees. That inflation is a pre-declared bracket calibrated
    in-sample, not a correction.
  - How strong cross-k100 structure is in the real data is unknown, so these p-values remain approximate. Their CIs
    (CR1) are approximate in the same way.
  - Family-wise error can also exceed 5% under such structure. In the simulated cross-map null, some RQ2 hypothesis
    was supported in 6.4% of replications, and some directional claim (supported or opposite) was made in 11.2%
    (4.6% under the k100 null).

## RQ3: reward

`output/frozen_run/rq3_results.csv`; Figures `F1_forest.png`, `F4_dose_response.png`, `F7_acceptance_by_class.png`.
- **Model:** linear probability models of acceptance with topic and year fixed effects, contribution-class dummies
  (reference: method) and the foundation-model dummy, SE clustered by topic.
- **Sample:** 32,190 papers, 2018–2026, mean acceptance 40.1%.
- **Maturity scale:** maturity is log(1 + prior papers in the topic); the mean is 4.8, about 120 prior papers.

### H3a: are papers in mature topics accepted less often? Inconclusive, underpowered

- **Main estimate:** −1.68 pp per log unit (95% CI −3.68 to +0.32; p = 0.099; Holm p = 0.20).
  - One log unit is about 2.7 times as many prior papers.
- **Variants:** all 11 counted variants are negative.
  - The linear variants range from −2.53 to −1.31 pp.
  - The logit average marginal effect is −1.64 pp.
  - Both hindsight variants are negative.
- **Supplementary, all negative:**
  - log team size (S1): −2.04 pp (p = 0.04);
  - fine topics (S5): −2.42 pp (p = 0.005);
  - withdrawals after review counted as rejections (S9): −2.12 pp (p = 0.02; adds 9,631 papers);
  - newcomer control (S10): −2.99 pp (p = 0.003);
  - two-way clustering (S11): −1.68 pp (p = 0.07).
- **Power and pre-declared reading.**
  - The dry-run found H3a underpowered: 54% detection at 3 × SESOI, MDE80 4.1 pp per log unit.
  - As declared before the run, a non-supported H3a is uninformative about effects below about 4 pp per log unit. It
    is not evidence of no effect.
  - The consistent direction is suggestive, not a confirmatory finding.
- **By era (E4, exploratory):** −0.3, −6.5 and −2.9 pp per log unit in 2018–20, 2021–23 and 2024–26, all n.s.

### H3b: is the maturity–acceptance slope more negative for method papers? Inconclusive

- **Main estimate:** −0.36 pp per log unit for method relative to other classes (95% CI −1.51 to +0.79; p = 0.53).
- **Variants:** 10 of 11 negative (the early map gives +0.13 pp).
- **Equivalence:** not established (TOST p = 0.14; 90% CI −1.33 to +0.60 against ±1 pp).

## Exploratory analyses (planned, labelled; p-values unadjusted)

All are associations within the stated fixed effects, `output/frozen_run/exploratory_estimates.csv`.

| | Analysis | Estimate |
|---|---|---|
| E1 | acceptance of foundation-model papers, within topic × year, class controls | +4.62 pp (p < 0.001); +4.06 pp without class controls |
| E2 | acceptance of newcomer papers, within topic × year, class and FM controls | −10.2 pp (p < 0.001); −10.5 pp in ID-consistent years |
| E3 | withdrawal after review ~ maturity | +1.62 pp per log unit (p = 0.009); before review −0.07 pp (n.s.) |
| E4 | H2b, H2c, H3a, H3b by era | see above |
| E5 | newcomer × hot interaction (method, measurement, acceptance) | −0.4, −0.6, +0.2 pp, all n.s. |
| E6 | dose-response after removing fixed effects (H1d, H2a, H3a) | Figure F4 |
| E8 | acceptance of new-architecture papers × prior FM adoption | +8.3 pp for 0 → 100% FM (p = 0.02) |
| E9 | equivalence tests for non-supported hypotheses | none equivalent: TOST p H2a 0.10, H3a 0.75, H3b 0.14 (H2b/H2c are significant, not equivalent) |
| E10 | acceptance by class vs method, within topic × year | theory +8.9 pp, dataset/benchmark +3.9 pp, empirical −2.7 pp, evaluation −1.9 pp (n.s.), other −8.0 pp |

- **E2 is the largest association in the study.** Papers with no incumbent author are accepted 10 pp less often
  (base 40%). Experience, team size, reviewer familiarity and resubmission are all candidate explanations; this
  analysis cannot separate them.
- **E8 (exploratory, unadjusted p = 0.02):** in topics with more prior foundation-model adoption, new-architecture
  papers are accepted relatively more often. Together with H1d (they become rarer there), one possible explanation is
  scarcity rather than a penalty. That is a hypothesis, not a test.
- **E7 and the buzzword rows of E3** use the failed buzzword measure. They are reported in the output, labelled, and
  not interpreted.

## Limitations

- **Associations only.** Topic choice, team composition and contribution type are chosen jointly.
  - The newcomer gaps (H2b/H2c, E2) may reflect team size (as for H2c), seniority or resubmission, not newness itself.
- **Incumbency is undercounted** in every year after 2020, for two reasons:
  - pre-2021 email author IDs are not linked to later profile IDs, so earlier work is invisible;
  - earlier work in the held-out confirmation split, or at other venues, is not seen.

  Both turn some true incumbents into newcomers, which registration D2 treats as a bias towards zero. The
  ID-consistent-years variant (R2) drops only the 2021–22 transition and gives the same results. It does not remove
  the undercount in 2023–2026.
- **Labels and measures.**
  - The contribution labels are LLM labels. S8's correction for misclassification enlarges the RQ2 estimates
    slightly.
  - "Measurement" is a rare class (7.7%).
- **Calibration.**
  - The H2b/H2c p-values and all CR1 intervals are approximate under topic structure that cuts across the k100 map
    (dry-run v3).
  - Family-wise error under such structure can exceed 5%: in the simulated case, 6.4% for any RQ2 support and 11.2%
    for any RQ2 directional claim.
- **RQ3 power.** H3a was underpowered (54% detection at 3 × SESOI; MDE80 4.1 pp per log unit), so its
  non-significance is uninformative about effects below about 4 pp per log unit. H3b's MDE80 is 2.4 pp per log unit.
- **Selection.** RQ3 conditions on papers that reached a decision; the registered filter leaves out 9,986 withdrawn
  submissions.
  - Withdrawal after review rises with maturity (E3, exploratory: +1.6 pp per log unit), so this conditioning may
    attenuate H3a.
  - Counting withdrawals after review as rejections (S9, 9,631 more papers) gives −2.12 pp.
- **One venue.** All results are for ICLR. The confirmation split is a held-out part of the same ICLR corpus, so it
  tests whether the discovery results replicate on unseen ICLR papers, not whether they generalise to other venues.

## Registered for the confirmation split

These were added after the discovery run (see the post-run record in `PREREGISTRATION.md`).

Supported discovery hypotheses are tested on the confirmation split, as registered: H1d, one-sided. Three more are
registered post hoc, from the discovery results, before any confirmation data exist. They use the same frozen code,
variants and decision rule, on the same model as their discovery counterpart, with one-sided tests at α = 0.05.
H2b′ and H2c′ reverse the discovery predictions because discovery found the opposite, so they are new hypotheses and
are labelled as such.
- **H2b′:** newcomer papers are more likely to be method papers.
- **H2c′:** newcomer papers are less likely to be measurement papers.
- **H3a:** acceptance decreases with topic maturity, the registered direction.

## Reproduction

```text
python -m unittest discover -s research/fashion/tests      # statsmodels cross-checks run if importable
python research/fashion/dryrun.py                           # about 2 h on 4 cores -> output/dryrun/
python research/fashion/dryrun_diagnostics.py               # -> output/checks/dryrun_v3_diagnostics.json
python research/fashion/freeze.py --created <UTC> --remedy bootstrap:H2b --remedy bootstrap:H2c
python research/fashion/run_frozen.py                       # refuses unless FREEZE.json matches a clean tree
python research/fashion/figures.py                          # -> output/figures/F1-F7
```
