# Research fashions at ICLR 2017–2026: results

> **Update 2026-10-18: held-out replication and pooled re-run.** The registered tests ran once on 11,099 released
> former-holdout ICLR papers. This study never analysed them before the registration. The run is a pre-registered
> out-of-sample replication, not a certified untouched independent holdout. It is a split-sample replication within
> the same ICLR years. Tests are one-sided, with Holm within the registered families. All results are associations.
> The PH5 findings are post hoc in discovery; their held-out tests were registered before the run. Held-out estimates
> are in pp with 95% CIs, with two-sided p in parentheses; see "Held-out replication (registered, 2026-10-18)" below.
> The discovery sections that follow are unchanged and remain the registered record.
>
> **Replicated on held-out papers (registered primary and RQ tests, supported):**
> - H1d (fewer new-architecture papers in topics with more prior foundation-model adoption): −11.0 pp for 0 → 100% FM
>   [−18.1, −3.9]; one-sided p 0.0013 (two-sided 0.0027).
> - H2b′ (newcomer papers are more often method papers): +3.60 pp [+1.48, +5.71]; one-sided p 0.0007, Holm 0.001
>   (two-sided 0.0014).
> - H2c′ (newcomer papers are less often measurement papers): −2.10 pp [−3.35, −0.85]; one-sided p 0.0005, Holm 0.001
>   (two-sided 0.0010).
> - PH5 E1, primary (a far jump from the team's own earlier work goes with lower acceptance): −6.09 pp [−9.32, −2.86];
>   one-sided p 0.0025, Holm 0.005 (two-sided 0.0050).
>
> **Secondary PH5 tests supported (one-sided at 0.05, unadjusted; 6 secondary tests, so one false positive would not
> be surprising):**
> - E4 (within-author slope): +1.06 pp per +0.1 cosine [+0.23, +1.89]; one-sided p 0.006 (two-sided 0.012).
> - teams H1 (one topic insider vs none): +3.88 pp [+0.28, +7.47]; one-sided p 0.017 (two-sided 0.035).
> - kwtiming A1 (Emerging minus Mainstream keywords): +3.25 pp [−0.18, +6.69]; one-sided p 0.031 (two-sided 0.063;
>   the 95% CI includes 0) and null-frame p 0.020.
> - premia b (discovery-period topic acceptance edges carry over in part): slope 0.60 [0.32, 0.88], inside (0, 1);
>   intersection-union p 0.003.
> - premia EB D0 (new test, no discovery counterpart): the EB-shrunk discovery premia predict better than zero, D0 > 0;
>   one-sided p 0.005 (two-sided 0.010).
>
> Several supported tests (H1d, H2c′, teams H1, A1) were underpowered at the discovery effect, so their held-out
> estimates are likely inflated: they confirm the direction, not the size.
>
> **Did not replicate:**
> - PH5 P1b, primary (least-novel fifth vs the middle fifth): −0.13 pp [−3.50, +3.25]; one-sided p 0.47, Holm 0.47
>   (two-sided 0.94).
>   - The estimate is below the 5.4 pp MDE80, so by the registered reading rule the test is uninformative, not
>     evidence against discovery.
>   - Discovery's post hoc "two tails" of lower acceptance (`presentation/shortlist.md`, finding 1) are the
>     least-novel fifth of abstracts (P1b) and far jumps from the team's own record (E1). Only the own-record tail has
>     replicated; the field-novelty tail remains discovery-only.
> - PH5 P7, secondary (within-author novelty slope): +0.34 pp per 10 percentile points [−0.47, +1.16]; one-sided p 0.22
>   (two-sided 0.43). It was not Holm-significant in discovery either. It has no registered MDE80; a derived one
>   (post hoc, ≈ 1.0–1.1 pp) suggests low power.
>
> **Not confirmed or inconclusive:**
> - H3a (lower acceptance in mature topics): −1.51 pp per log unit [−5.20, +2.19]; one-sided p 0.21 (two-sided 0.42).
>   - Inconclusive again: the hindsight requirement fails.
>   - The estimate is below the 4.8 pp MDE80, so the test is uninformative.
> - H4-FL (federated-learning acceptance gap):
>   - level −4.9 pp [−15.4, +5.7], one-sided p 0.14 (two-sided 0.29), not supported. The estimate is below its MDE80
>     (14.5 pp), so by the registered rule the level test is uninformative; the MDE80 also exceeds the discovery gap
>     (−11.3 pp).
>   - trend (secondary) +3.2 pp per year [−3.3, +9.6], one-sided p 0.88 (two-sided 0.24), not supported: it has the
>     opposite sign to the prediction, and no MDE was computed for it.
>
> **Pooled re-run (exploratory; all 54,579 papers).** It contains the held-out papers, and about 80% of each pooled
> sample is discovery papers, so agreement with discovery is expected and confirms nothing. Pooling also changes
> discovery features. The headline estimates keep their sign: H1d −8.9 pp, H2b +3.46, H2c −1.65, PH5 E1 −5.53 and
> P1b −2.97, the last driven by the discovery papers. Sizes are not uniformly stable: the FL trend roughly halves
> (keyword −3.0 → −1.9 pp per year, topic −2.7 → −1.2). H3a gives −1.72 pp (Holm 0.098) and stays inconclusive.

All confirmatory tests follow `PREREGISTRATION.md`: hypotheses and decision rule as registered, plus a dated pre-run log
of every clarification, replacement and deviation, written before any confirmatory RQ2/RQ3 estimate existed. One
exploratory estimate (E7) was seen earlier by accident; see Reviews. RQ2 and RQ3 were run
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
- **Data sources:** an integrated, curated ICLR corpus. Primary source: our own official OpenReview snapshots
  (submission metadata, author lists from the selected official metadata, reviews, discussions). Reconciled with
  existing resources: Paper Copilot (Yang, Wei & Pei, 2025, arXiv:2510.13201; upstream provenance for archived
  metadata and reconstructed score pairs), Louis's ICLR archive (`MlouisBE/iclr-rebuttal-analysis`; archived
  observations, source comparisons, reconstructed score changes) and Re² (Zhang et al., 2025, arXiv:2505.07920;
  historical audit and validation reference). Our work: acquisition, source reconciliation, cleaning, deduplication,
  eligibility rules, provenance tracking and keyword preprocessing.
- **Added 2026-10-18:**
  - Held-out corpus: the 11,099 released former-holdout papers with an abstract (of 11,113), used for the registered
    replication.
  - Pooled corpus: all 54,579 papers, used for the exploratory re-run.
  - Both use the frozen topic maps, a keyword lookup learned on discovery only, and the frozen labelling protocol.
  - Details are under "Held-out replication" and "Pooled re-run" below. Every number in the other sections is
    discovery-only.
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
    - the H2d judges were two Sonnet runs plus one Haiku run, instead of two Opus runs plus one Sonnet run;
    - the τ judges were two Haiku runs plus one Sonnet run; no model had been registered for them;
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
  - Rejected findings were documented rather than fixed, e.g. round B3's loader-circumvention point.
  - Findings downgraded by the verifiers were still acted on where cheap (rounds B7 and B8).
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
  - Under the prospective early map the method and measurement estimates point the predicted way: method −3.5 pp,
    measurement +4.0 pp per log unit (exploratory, unadjusted). The empirical estimate (H1c, −1.0 pp) does not.
  - Whether lifecycles appear therefore depends on how topics are defined.
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
  - The dry-run found H3a underpowered in its high-variance setting: 54% detection at 3 × SESOI, MDE80 4.1 pp per
    log unit. The low-variance setting gives 88% and 2.8 pp. The pre-declared reading uses the conservative
    4.1 pp.
  - As declared before the run, a non-supported H3a is uninformative about effects below about 4 pp per log unit. It
    is not evidence of no effect.
  - Neither of these is confirmatory evidence of an effect:
    - the consistent direction across counted variants, which re-estimate the same papers;
    - the nominally significant supplementary variants, whose p-values are unadjusted and outside the verdict.
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

## Post hoc: what goes with acceptance for newcomer papers? (PH1, exploratory)

This analysis was asked after the results and declared in `PREREGISTRATION.md` before it was run (`posthoc.py`,
outputs in `output/posthoc/`, figures `PH1_newcomer_what.png` and `PH1_newcomer_areas.png`). It is not
pre-registered: these are associations within topic and year, not effects. Holm is applied within each block and
only ranks the evidence.

- **Population:** the E2 population, 31,549 decided papers from 2019–2026 with an author ID.
  - 22,603 are newcomer papers, accepted 37.2% of the time; incumbent papers are accepted 47.3% of the time.
- **Among newcomer papers, within the same topic and year** (A2, relative to newcomer method papers):
  - theory papers +10.2 pp (95% CI +7.2 to +13.2; raw 44.9% vs 36.9%);
  - papers building on foundation models +4.1 pp (+2.0 to +6.2), about the same as for all papers (E1);
  - dataset/benchmark +2.4 pp and evaluation −0.5 pp, both n.s.;
  - empirical −3.1 pp (n.s.);
  - "other" −9.1 pp.
- **Team size is the strongest correlate** (A1, topic and year FE, relative to newcomer teams of 3–4 authors):
  - 1–2 authors: −8.5 pp;
  - 5–6 authors: +3.7 pp;
  - 7 or more authors: +11.1 pp.
- **Topic choice.**
  - Newcomer papers in more mature topics are accepted less often: −2.8 pp per log unit (Holm p = 0.02, A1).
  - Hot topics bring no advantage (+1.2 pp, n.s.).
- **The newcomer acceptance gap is present in every subgroup** (B, within topic × year). It is −10.2 pp overall, and
  ranges from:
  - −5.1 pp for theory papers and −6.4 pp for teams of 7 or more (the smallest);
  - to −14.6 pp for dataset/benchmark papers and −11.6 pp in the most mature topics (the largest).

  Team size therefore accounts for some of the gap, not all of it. Newcomer dataset/benchmark papers are rarer
  (H2c), and when written they show the largest gap.
- **By area (C):**
  - The within-topic-year newcomer gap is negative in all 20 coarse areas, from −3.8 to −20.8 pp.
  - Newcomer acceptance relative to the year's overall rate is near zero in computer vision, vision-language and LLM
    areas, and lowest in federated learning, adversarial robustness, graph neural networks and time series (about
    −9 pp).
  - No area or area × year cell survives Holm, so these are descriptive only.
- **Reading.** Newcomer papers that are theory papers, come from large teams or build on foundation models are
  accepted more often. The newcomer gap is smallest for theory papers and large teams.
  - Selection is likely: newcomer theory papers may come from established researchers in other fields, and large
    teams bring resources and seniority.
  - So these are not recommendations about what a newcomer should do.

## Post hoc: where do small or large teams do better? (PH2, exploratory)

`posthoc.py ph2`, declared before it was run; outputs in `output/posthoc/ph2_*`, figure `PH2_team_size.png`.
- **Population:** all 32,190 RQ3 papers, 2018–2026.
- **Model:** acceptance per doubling of team size, within topic × year, controlling class and FM. Team size is capped
  at 16.
- **Calibration:** in simulated nulls, the slope and band tests were sized about 5%. The nominal heterogeneity test
  was badly oversized (90% for areas), so its p-value is calibrated on the real design instead.

- **Overall the gradient is steep.**
  - Acceptance by team size: 1–2 authors 28.7%; 3–4 authors 37.6%; 5–6 authors 41.6%; 7 or more 49.0%.
  - Within topic and year: +8.8 pp per doubling (95% CI +8.0 to +9.7), and +7.8 pp with a newcomer control.
  - Relative to 3–4 authors: 1–2 authors −9.1 pp; 7 or more +10.8 pp.
- **By contribution class.**
  - Large teams gain most for dataset/benchmark and evaluation papers: +13.5 pp per doubling each. Benchmark papers by
    1–2 authors are accepted 21% of the time, against 52% with 7 or more.
  - Method papers +9.3 pp; empirical +5.5 pp.
  - Theory is the flattest: +3.3 pp, n.s. Theory papers by 1–2 authors are accepted 42% of the time, against 27% for
    method papers by 1–2 authors.
  - The joint test that all classes share one slope is not rejected (calibrated p = 0.13), so the class ranking is
    suggestive. The gap between theory and dataset/benchmark is the clearest contrast: their CIs do not overlap.
- **By area.** Areas do differ (calibrated p = 0.035).
  - **Steepest** (large teams most favoured):
    - neuroscience/spiking networks, +14.2 pp;
    - diffusion image/video generation, +12.9 pp (1–2 authors 25% vs 7 or more 59%);
    - VLM reasoning, +12.3 pp;
    - vision-language, +11.9 pp;
    - LLMs/NLP, +11.2 pp;
    - LLM efficiency, +10.3 pp;
    - embodied AI, +10.2 pp.
  - **Flattest** (small teams least disadvantaged):
    - federated learning/privacy, +4.0 pp (7 or more vs 3–4: +0.3 pp);
    - time series, +4.3 pp;
    - optimisation, scientific ML and probabilistic inference, +5.2 pp (7 or more vs 3–4: −1.0 pp);
    - causal inference/biomedical ML, +6.9 pp, n.s.
  - The slope is positive in every area. There is no area where small teams do better, only areas where they are less
    disadvantaged.
- **Reading.** Team size also stands for compute, data, engineering and seniority, which are plausibly what large
  benchmark, generation and LLM work needs. These are associations, not advice to add authors.

## Post hoc: is the newcomer gap about who the authors are? (PH3, exploratory)

`posthoc.py ph3`, declared before it was run; outputs in `output/posthoc/ph3_*`, figure `PH3_author_fe.png`. ICLR is
double-blind, so the gap need not reflect reviewers' treatment of newcomers: newcomer papers may simply be weaker. PH3
asks how much of the gap is about the authors.
- **Data:** one row per paper and author ID (160,222 rows; each paper weighs 1 in total).
- **Fixed effects:** topic × year and author.
- **Controls:** class, FM, team size and the author's earlier ICLR submissions.
- **Identification:** 15,579 authors have both newcomer and incumbent papers.

| | Without author FE | With author FE (same sample) |
|---|---|---|
| Newcomer paper, all authors | −5.4 pp (−7.1, −3.7) | −3.1 pp (−4.5, −1.6) |
| The author is new to the topic | −3.1 pp | −1.4 pp (−2.7, −0.0) |
| Newcomer paper, first-author FE | −4.7 pp | −2.2 pp (−4.8, +0.3) |
| Newcomer paper, last-author FE | −4.5 pp | −2.9 pp (−4.6, −1.1) |

- **Most of the gap is about who writes newcomer papers.**
  - The −10.2 pp gap (PH1) falls to about −6.7 pp once team size and the authors' ICLR experience are controlled.
  - Within the same authors it falls to about −3 pp.
  - The same person entering a topic new to them is accepted about 1.4 pp less often.
- **What remains is small and need not be reviewer bias.** Less familiarity with a topic's methods, baselines and
  framing can make the same person's paper weaker. The data cannot separate the two.
- **Review scores could separate the reviewer stage from the decision stage,** but they are not in this repository
  (see the post-run record).

## Post hoc: which areas are accepted more or less often, and why? (PH4, exploratory)

`posthoc.py ph4`, declared before it was run (with the mechanism probes PH4b, added before the run). Outputs:
`output/posthoc/ph4_*`; figures `PH4_keywords_map.png`, `PH4_topics_map.png`, `PH4_keyword_trends.png`,
`PH4_mechanisms.png`.

The question came from the user and their supervisor, after an earlier exploratory keyword × year grid suggested,
for example, that federated learning was falling out of favour. That grid predates the registration. PH4 is therefore
a systematic screen, not a test of the keywords already seen.

- **Population:** the RQ3 filter, 2018–2026, 32,190 decided papers.
- **Units:**
  - 68 author keywords (research areas, specific topics, properties and application domains, each used by ≥ 200
    submissions); these carry no topic-map hindsight;
  - the 100 k100 topics.
- **Estimands:** for each unit, its papers' acceptance minus that of all other papers of the same year:
  - level, 2018–2026;
  - recent level, 2024–2026;
  - trend, in pp per year.

  Benjamini–Hochberg is applied within each set.
- **No area survives the multiple-testing correction.** No keyword and no topic is flagged (q < 0.05) on level, recent
  level or trend.
  - The declared tests are conservative. In 200 within-year permutations of acceptance they rejected 0.5–1.4% of the
    time at nominal 5%, and no permutation produced a flag.
  - A non-flagged area is therefore not evidence of no difference.
- **Descriptively, areas differ by about ±10 pp.** Among keywords with at least 5 years of data:
  - highest: pre-training +9.9 pp, imitation learning +8.8, language models +8.0, generative models +6.4;
  - lowest: convolutional neural networks −14.2, federated learning −11.3, data augmentation −11.0, image
    classification −10.2, adversarial attack −7.4.

  Diffusion models are +8.6 pp (p = 0.02). Among topics:
  - highest: neural rendering +13.5, robot learning +11.0, diffusion formulation +10.6;
  - lowest: clinical ML −14.9, federated learning −13.5, recommender systems −13.5, graph representation learning
    −9.8.

  All p-values are unadjusted; every q ≥ 0.17.
- **Federated learning is low under both definitions.**

  | | Papers | Level 2018–26 (95% CI) | 2024–26 | Trend (pp/yr) | Adjusted level |
  |---|---|---|---|---|---|
  | Keyword | 475 | −11.3 (−17.9, −4.8); p = 0.005, q = 0.19 | −13.5 (p = 0.007) | −3.0 (−6.4, +0.5); p = 0.08 | −10.5 |
  | Topic m029 | 485 | −13.5 (−21.1, −5.9); p = 0.005, q = 0.17 | −14.1 (p = 0.012) | −2.7 (−7.0, +1.5); p = 0.16 | −12.1 |

  - The gap has been below average in every year since 2022, roughly −11 to −15 pp a year since 2023. FL papers'
    own acceptance went from 36% (2022) to 24% (2026).
  - The early premium (2020: n = 11) is too small to rely on. So "going downhill" describes FL's place in the field
    better than a steady decline in its acceptance gap.
  - Adjusting for contribution type, FM and team size barely changes the level (−10.5).
- **Why? (PH4b, federated learning only, since no trend was flagged.)**
  1. **Composition / influx.** *Not supported.* FL's authors became more experienced, not less:
     - papers with an author who had an earlier accepted ICLR paper went from 4% (2021) to about 60% (2023–2025);
     - keyword newcomers fell from 96% to 40–58%;
     - team size (4.3–4.9) and the share of method papers (about 85%) are stable;
     - adjusting acceptance for composition keeps 76% of the raw trend.
  2. **The field moved on (hype cycle).** *Supported, descriptively.* FL's share of all submissions peaked in 2023
     at 3.2% and fell to 1.1% by 2026.
  3. **FL papers judged more harshly** (reviewer scepticism or saturation of ideas; the supervisor's reading).
     *Consistent with the data, not testable here.*
     - The declining trend appears in every author group: established −1.6 pp/yr, others −3.2, keyword
       incumbents −1.8, keyword newcomers −4.3.
     - None is significant on its own, so the registered reading rule returns "mixed".
- **Reading.** The data fit a cooling of the field on FL: authors are leaving, and the papers that remain are
  accepted less often than other papers of the same year. This is not explained by who writes them, their type or
  their team size. Reviewers' reasons are not observed, so scepticism about FL's research value is a plausible
  explanation, not a tested one. The level difference is individually clear, but not after correcting for 68
  keywords. Its replication is registered (below).

## Limitations

- **Associations only.** Topic choice, team composition and contribution type are chosen jointly.
  - The newcomer gaps (H2b/H2c, E2) may reflect team size (as for H2c), seniority or resubmission, not newness itself.
- **Incumbency is undercounted** in every year after 2020, for two reasons:
  - pre-2021 email author IDs are not linked to later profile IDs, so earlier ICLR work is invisible;
  - earlier ICLR work in the held-out confirmation split is not seen.

  Both turn some true incumbents into newcomers, which registration D2 treats as a bias towards zero. The
  ID-consistent-years variant (R2) drops only the 2021–22 transition and gives the same results. It does not remove
  the undercount in 2023–2026.
- **Incumbency is ICLR-only by definition,** so experience at other venues is not captured.
- **Labels and measures.**
  - The contribution labels are LLM labels. S8's correction for misclassification enlarges the RQ2 estimates
    slightly.
  - "Measurement" is a rare class (7.7%).
- **Calibration.**
  - The H2b/H2c p-values and all CR1 intervals are approximate under topic structure that cuts across the k100 map
    (dry-run v3).
  - Family-wise error under such structure can exceed 5%: in the simulated case, 6.4% for any RQ2 support and 11.2%
    for any RQ2 directional claim.
- **RQ3 power.** H3a was underpowered in the high-variance dry-run setting (54% detection at 3 × SESOI; MDE80 4.1 pp
  per log unit; low-variance setting 88%, 2.8 pp), so its non-significance is uninformative about effects below about
  4 pp per log unit. H3b's MDE80 is 2.4 pp per log unit.
- **Selection.** RQ3 conditions on papers that reached a decision; the registered filter leaves out 9,986 withdrawn
  submissions.
  - Withdrawal after review rises with maturity (E3, exploratory: +1.6 pp per log unit), so this conditioning may
    attenuate H3a.
  - Counting withdrawals after review as rejections (S9, 9,631 more papers) gives −2.12 pp.
- **One venue.** All results are for ICLR. The confirmation split is a held-out part of the same ICLR corpus, so it
  tests whether the discovery results replicate on unseen ICLR papers, not whether they generalise to other venues.
- **Held-out replication and pooled re-run (2026-10-18).**
  - The released papers are not certified as an untouched, independent holdout.
  - It is a split-sample replication within the same ICLR years. It guards against analyst overfitting to the
    discovery papers, not against year- or reviewer-specific patterns:
    - the two splits share conference-years, topic-year cells, reviewer pools and authors, and their features are
      built jointly;
    - some probable resubmission pairs span the splits (39 held-out earlier versions point to discovery papers, 54
      discovery ones to held-out papers);
    - held-out newcomer status sees both splits' histories, so H2b′/H2c′ use a better-informed newcomer measure than
      discovery's H2b/H2c.
  - H4-FL's out-of-sample status cannot be verified, because the provenance of the earlier keyword grid is unknown.
  - Several held-out tests are underpowered. By the registered reading rule, H3a (MDE80 4.8 pp), H4-FL (14.5 pp,
    larger than the discovery gap) and P1b (5.4 pp; power 0.47 at the discovery effect) are uninformative. P7 has no
    registered MDE80; a derived one (post hoc, ≈ 1.0–1.1 pp) suggests low power.
  - Several supported held-out tests were also underpowered at the discovery effect: H1d (MDE80 12.0 vs −8.0 pp), H2c′
    (2.4 vs −1.70), teams H1 (derived ≈ 4.5 vs +3.42) and A1 (derived ≈ 4.3 vs +2.67). Supported held-out estimates
    are therefore likely inflated and confirm direction, not size.
  - The held-out text measures use post-decision abstracts, with no link-removal (cleantext) check.
  - The PH5 secondary tests are unadjusted.
  - The pooled re-run contains the held-out papers and changes discovery features, so it confirms nothing.

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
- **H4-FL (registered 2026-10-17, after PH4, before any confirmation data exist).** Papers listing "federated
  learning" are accepted less often than other papers of the same year: the PH4 level, one-sided, α = 0.05. Its
  trend is negative: secondary, one-sided. These use the same PH4 code and population definition on the confirmation
  split.

## Held-out replication (registered, 2026-10-18)

The registration is the 2026-10-18 entry of `PREREGISTRATION.md`, committed before the run, and
`FREEZE_CONFIRMATION.json` hashes the code and inputs. `run_confirmation.py` then ran once (attempt 1, 2026-10-18,
16:39–16:42 UTC), with the PH5 tests included. Its outputs are in `output_pooled/confirmation_run/`:
- `summary.json`, `stdout.txt`;
- `h1d.csv`, `rq2_rows.csv`, `rq3_rows.csv`;
- `h4fl.csv`, `h4fl_cells.csv`;
- `ph5/*.csv`.

### Design

- **Data status.**
  - The papers are the 11,099 released former-holdout papers with an abstract, out of 11,113: 105 in 2017, rising to
    3,942 in 2026. They were this study's confirmation split, and the study never analysed them before the
    registration.
  - Their source policy does not certify an untouched, independent holdout. Every result here is therefore a
    pre-registered out-of-sample replication on released former-holdout papers, not an independent confirmation.
  - It is a split-sample replication within the same ICLR years (2017–2026). It guards against analyst overfitting to
    the discovery papers, but not against year- or reviewer-specific patterns: the two splits share conference-years,
    topic-year cells, reviewer pools and authors.
  - The earlier keyword grid that first suggested the federated-learning (FL) pattern has unknown provenance, so
    H4-FL's out-of-sample status is not verified.
- **Features (D14).**
  - All features were built on discovery ∪ held-out papers (54,579) with the unchanged builders, then restricted to
    the held-out papers. `output_pooled/build_report.json` passed every gate.
  - Author histories, maturity, hot status, incumbency and probable earlier versions therefore see both splits.
    Held-out incumbency is 30.9%.
  - The newcomer definition therefore differs from discovery's registered one. Discovery H2b/H2c used discovery-only
    histories (incumbency 26.5%); under pooled histories 1,515 discovery papers would switch from newcomer to
    incumbent. H2b′/H2c′ use the better-informed pooled measure.
  - Some probable resubmission pairs span the splits: 39 held-out earlier versions point to discovery papers, and 54
    discovery earlier versions point to held-out papers (`build_report.json`).
  - The SPECTER2 centring mean and τ = 0.90 stay frozen.
  - Fixed effects are estimated among held-out rows. No discovery paper is in any test population.
- **Topic maps.**
  - k100, fine and coarse topics come from the frozen `topic_model.npz`.
  - For each of the nine alternative maps (k50, k75, k150, k200, seed refit, year-balanced, early, middle-era, late),
    the exact KMeans centres were re-derived from the frozen fits, and each held-out paper goes to the nearest one.
  - Gate: the re-derived centres must reproduce every saved discovery label exactly. All 9 passed, as did both
    stable-paper gates (the stable share is 0.792 in both splits). Report:
    `research/topics/output_pooled/pooled_topics_report.json`.
  - On every map, the held-out topic distribution differs from discovery by no more than sampling noise: the total
    variation distance is below the 95th percentile of the noise.
- **Keyword map.**
  - Held-out papers have raw author keywords only.
  - A lookup table learned on discovery papers alone maps them to the curated lists: 45,778 forms, 5,738 of them
    non-identity.
  - Cross-validated recall / precision (`research/topics/output_pooled/keyword_map_report.json`):
    - 759-keyword vocabulary: 98.6% / 99.96%;
    - the 68 PH4 keywords: 99.0% / 99.98%;
    - 'federated learning': 97.2% / 100%.
- **Labels.**
  - Haiku with prompt v1, unchanged, under the frozen batch protocol.
  - A blind second pass on 555 held-out papers gives:

    | Measure | Agreement | κ |
    |---|---|---|
    | Main class | 96.9% | 0.931 |
    | Method | 98.0% | 0.949 |
    | Measurement | 99.1% | 0.923 |
    | Foundation model | 98.2% | 0.960 |

    Source: `research/topics/output/contribution_labels_quality_released.json`.
  - The released abstracts are post-decision text. No link-removed (cleantext) vectors exist for these papers, so
    E1, E4, P1b and P7 have no cleantext check here.
- **One-sided rule and families.**
  - Every registered test is one-sided at α = 0.05: p1 = p/2 if the estimate has the predicted sign, otherwise
    1 − p/2.
  - Here p is the two-sided p of the discovery method:

    | p method | Tests |
    |---|---|
    | CR1, t(G − 1) | H1d, H3a, P1b, E4, teams H1 |
    | wild cluster restricted bootstrap | H2b′, H2c′ |
    | t(m − 1) | H4-FL |
    | max(CR1, calibrated) | PH5 E1 |
    | max(CR1, two-way, calibrated) | P7 |
    | two-way (keyword, topic) | A1 |
    | intersection-union test | premia b |
    | paired t | premia D0 |

  - Exception: premia b. Its prediction is 0 < b < 1, so its p1 is the intersection-union p, the larger of the
    one-sided p for b > 0 and for b < 1 (here 0.003, from b < 1). It is not half of a two-sided p: the two-sided p
    for b = 0 is 6.5 × 10⁻⁵. Premia D0 follows the rule (0.010 / 2 = 0.005).

  - Holm families: {H1d}, {H2b′, H2c′}, {H3a}, {H4-FL} and the PH5 primary pair {E1, P1b}.
  - The six PH5 secondary tests are each one-sided at 0.05, unadjusted, with no family claim. A1 also needs a
    one-sided null-frame p below 0.05.
- **Decision rule.**
  - The rule is unchanged (`analysis.decide`): the predicted sign, Holm p1 < 0.05, at least 75% of counted variants
    with the predicted sign, and both hindsight variants.
  - H4-FL and PH5 have no variants, so they need only the predicted sign and (Holm) p1 < 0.05.
  - H2b′ and H2c′ reverse the discovery predictions, so they are new hypotheses.
- **MDE80 and reading rules (computed and registered before the run).**
  - MDE80 is computed at each test's Holm first step from simulated outcomes (`confirmation_dryrun/mde.json`,
    `ph5_confirm/calibration.json`):

    | Test | MDE80 |
    |---|---|
    | H1d | 12.0 pp (0 → 100% FM) |
    | H2b′ | 2.8 pp |
    | H2c′ | 2.4 pp |
    | H3a | 4.8 pp per log unit |
    | H4-FL | 14.5 pp |
    | PH5 E1 | 4.9 pp |
    | P1b | 5.4 pp |

  - Power at the discovery effect is 0.89 for E1 with the CR1 p (slightly less under the registered max rule) and
    0.47 for P1b.
  - Reading rule: a non-supported H1d, H3a, H4-FL or P1b whose estimate is below its MDE80 is uninformative. It is
    not evidence of no association. The rule does not cover the PH5 secondary tests, which have no registered MDE80.

### Results for every registered test

Estimates are in pp unless stated. Discovery estimates are quoted from the registered discovery outputs
(`output/rq1_summary.json`, `output/frozen_run/`, `output/posthoc/ph4_*`, `output/posthoc/ph5_*`):
- discovery p are two-sided, Holm within the discovery family;
- the PH4 and PH5 discovery estimates are post hoc (declared before they were run), but their held-out tests were
  registered before the held-out run;
- the held-out H1d CI uses t(G − 1) quantiles, where discovery printed ±1.96 SE.

The A1 95% CI includes 0 although its one-sided p1 is below 0.05: a one-sided 5% test corresponds to a 90% interval.

| Test | Prediction | Discovery (95% CI) | Held-out [95% CI] | One-sided p (Holm) | Two-sided p | Verdict | MDE80 (registered unless marked) |
|---|---|---|---|---|---|---|---|
| **H1d** | new architecture ~ prior FM adoption (−), 0 → 100% FM | −8.0 (−12.1, −3.8); Holm 0.001 | **−11.0 [−18.1, −3.9]**; n 10,978 | 0.0013 (0.0013) | 0.0027 | **supported**: 9/9 variants, hindsight passes | 12.0 |
| **H2b′** | method ~ newcomer (+) | +3.71 (+2.61, +4.80); Holm < 0.001, opposite to H2b | **+3.60 [+1.48, +5.71]**; n 10,718 | 0.0007 (0.0010) | 0.0014 | **supported**: 10/10, hindsight passes, S11 agrees | 2.8 |
| **H2c′** | measurement ~ newcomer (−) | −1.70 (−2.46, −0.93); Holm < 0.001, opposite to H2c | **−2.10 [−3.35, −0.85]**; n 10,718 | 0.0005 (0.0010) | 0.0010 | **supported**: 10/10, hindsight passes, S11 agrees | 2.4 |
| H3a | accepted ~ maturity (−), per log unit | −1.68 (−3.68, +0.32); Holm 0.20 | −1.51 [−5.20, +2.19]; n 8,185 | 0.21 (0.21) | 0.42 | inconclusive: 9/11 variants, hindsight fails; uninformative | 4.8 |
| H4-FL level | FL keyword papers vs all others of the year (−) | −11.3 (−17.9, −4.8); p 0.005, q 0.19 | −4.9 [−15.4, +5.7]; 134 FL papers, 6 years with ≥ 10 | 0.14 (0.14) | 0.29 | not supported; uninformative | 14.5 |
| H4-FL trend (secondary) | yearly gap trend (−), pp per year | −3.0 (−6.4, +0.5); p 0.08 | +3.2 [−3.3, +9.6] | 0.88 | 0.24 | not supported (opposite sign) | not computed |
| **PH5 E1** (primary) | far jump: P(accept) at F_max p10 minus p50 (−) | −5.44 (−7.10, −3.78); Holm 1.3 × 10⁻⁸ | **−6.09 [−9.32, −2.86]**; 5,344 papers | 0.0025 (0.0050) | 0.0050 | **supported** | 4.9 |
| PH5 P1b (primary) | novelty: least-novel fifth minus middle fifth (−) | −3.27 (−4.93, −1.60); Holm 0.0014 | −0.13 [−3.50, +3.25]; 8,010 papers | 0.47 (0.47) | 0.94 | not supported; uninformative | 5.4 |
| **PH5 E4** (secondary) | within-author slope per +0.1 cosine (+) | +0.55 (+0.21, +0.90); Holm 0.006 | **+1.06 [+0.23, +1.89]**; 4,311 papers | 0.006 (two-way 0.004) | 0.012 | **supported** | not computed |
| PH5 P7 (secondary) | within-author slope per 10 novelty percentile points, 2023–26 (+) | +0.39 (+0.09, +0.69); Holm 0.105 | +0.34 [−0.47, +1.16]; 4,810 papers | 0.22 | 0.43 | not supported (no registered MDE80; the derived value suggests low power) | none registered; derived ≈ 1.0–1.1 (post hoc: 2.49 × CR1 / two-way SE) |
| **Teams H1** (secondary) | one topic insider vs none (+) | +3.42 (+1.18, +5.66); Holm 0.019 | **+3.88 [+0.28, +7.47]**; 6,243 papers | 0.017 | 0.035 | **supported** | none registered; derived ≈ 4.5 (post hoc: 2.49 × SE) |
| **Kwtiming A1** (secondary) | Emerging (young, rising) minus Mainstream (old, flat) keywords (+) | +2.67 (+0.76, +4.58); Holm 0.020 | **+3.25 [−0.18, +6.69]**; 5,741 papers | 0.031; null-frame 0.020 | 0.063 | **supported** | none registered; derived ≈ 4.3 (post hoc: 2.49 × SE) |
| **Premia b** (secondary) | slope of the held-out 2024–26 premia on the discovery 2018–22 premia, early map (0 < b < 1) | 0.38 (0.18, 0.58); Holm 0.001 (within discovery) | **0.60 [0.32, 0.88]**; 75 units | 0.003 (intersection-union) | not halved; for b = 0: 6.5 × 10⁻⁵ | **supported** | not computed |
| **Premia EB D0** (secondary) | EB-shrunk discovery premia predict better than 0 (> 0) | none: a new test, with no discovery counterpart | **1.71 [0.42, 3.01] × 10⁻³**; MSE 8.76 → 7.04 × 10⁻³ | 0.005 | 0.010 | **supported** | not computed |

MDE80 bases. The registered values (H1d to H4-FL from `confirmation_dryrun/mde.json`; E1 and P1b from
`ph5_confirm/calibration.json`) are one-sided and simulated at each test's Holm first step. The three derived values
are post hoc, analytic and one-sided at 0.05: (z0.95 + z0.80) × SE ≈ 2.49 × SE, using P7's CR1 SE (1.0) and its
larger two-way SE (1.1). The teams and kwtiming module files print two-sided values instead, about 2.80–2.83 × SE
(0.975 and 0.80 quantiles): teams H1 5.1 and A1 4.9 analytic, and A1 4.7 from the null-frame SD. None of the derived
values carries a registered reading rule.

- **H2b′ and H2c′.**
  - Base rates: method 75.0%, measurement 7.9%, newcomer 68.3%.
  - S11 (two-way clustering), Holm p1: 0.0010 (H2b′) and 0.0009 (H2c′), so S11 agrees.
  - Stress sensitivity, Holm p1: 0.0075 for both.
  - Exact one-sided bootstrap share: 0.0006 (H2b′) and 0.0004 (H2c′).
  - No S-variant is significant against the prediction, so neither is fragile.
  - With log team size controlled (S1), H2c′ shrinks to −0.98 pp (two-sided p 0.10), while H2b′ stays at +3.64 pp.
    The discovery pattern was the same: −0.54 pp and +3.92 pp.
- **H1d.**
  - All 9 counted variants are negative, from −5.4 to −15.2 pp.
  - The weakest is the prospective early-map variant (−5.4 pp, two-sided p 0.24; one-sided 0.12).
- **H3a.**
  - 9 of 11 counted variants are negative. Two have the wrong sign:
    - the early map on 2021–26 papers, +1.44 pp, which is a hindsight variant;
    - without 2026, +0.95 pp.
  - Equivalence is not established: TOST p 0.61, 90% CI −4.60 to +1.58.
  - S9 (2,463 more papers): −1.97 pp (two-sided p 0.19; one-sided 0.097).
  - Acceptance is 39.4%.
  - No withdrawn paper had an unknown review status, so the contingency rule was not used.
- **H4-FL by year.**
  - Yearly gaps:

    | Year | Gap (pp) | FL papers |
    |---|---|---|
    | 2021 | −20.0 | 14 |
    | 2022 | −16.9 | 13 |
    | 2023 | +6.4 | 19 |
    | 2024 | −3.6 | 34 |
    | 2025 | −11.3 | 16 |
    | 2026 | −0.2 | 36 |

  - The discovery pattern, a gap of about −11 to −15 pp in every year since 2023, does not appear.

**Not registered: reported and labelled, not interpreted.** These rows come out of the same calls. Their p are
two-sided and unadjusted.

| Row | Discovery | Held-out [95% CI] | p |
|---|---|---|---|
| H2a incumbent ~ hot topic (−) | −0.73 (−2.68, +1.22) | −2.55 [−5.59, +0.49] | 0.099 |
| H3b accepted ~ maturity × method (−) | −0.36 (−1.51, +0.79) | +1.34 [−1.26, +3.93] | 0.31 |
| H4-FL recent level, 2024–26 | −13.5 (p 0.007) | −3.6 [−17.2, +9.9] | 0.52 |
| H4-FL level adjusted for class, FM and team size | −10.5 | −3.4 | 0.42 |
| PH5 E2, near: F_max p90 minus p50 | +1.75 (−0.17, +3.66) | +2.34 [−1.01, +5.70] | 0.17 |
| PH5 E3, far jump in hot minus other topics | −0.35 (−3.13, +2.42) | −3.09 [−9.63, +3.45] | 0.35 |
| P1a, most-novel fifth minus middle fifth | +0.44 (−1.41, +2.28) | +2.54 [−1.40, +6.48] | 0.20 |
| P2, any concurrent same-year twin | +0.68 (−0.84, +2.20) | +3.69 [+0.90, +6.48] | 0.010 |
| P3, twin association, high minus low novelty | +0.18 (−3.46, +3.83) | +4.84 [−2.27, +11.95] | 0.19 |
| P4, twin association, hot minus other topics | −1.49 (−4.51, +1.52) | +1.47 [−3.65, +6.59] | 0.63 |
| P5, (Q5 − Q3) for newcomer minus incumbent papers | +1.32 (−2.63, +5.28) | −9.75 [−17.38, −2.12] | 0.030 |
| P6, (Q5 − Q3) for mature minus young topics | +4.69 (+0.21, +9.18) | +10.74 [+1.95, +19.53] | 0.030 |
| Teams H2, concavity | +2.95 (−1.41, +7.30) | +4.47 [−2.24, +11.18] | 0.19 |
| Premia b, k100 topics | 0.35 (0.17, 0.54) | 0.51 [0.23, 0.79]; 62 units | intersection-union 0.0004 |
| Premia b, PH4 keywords | 0.53 (0.10, 0.95) | 0.16 [−0.34, 0.66]; 35 units | intersection-union 0.26 |
| Premia b, areas | 0.20 (−0.49, 0.89) | 0.71 [0.09, 1.33]; 20 units | intersection-union 0.17 |
| Premia D = MSE(raw) − MSE(EB), early map (descriptive) | none | 0.37 [−1.31, +2.06] × 10⁻³ | one-sided 0.33 |

### Interpretation

- **Findings supported in discovery and again on the held-out split.** This is a split-sample replication within the
  same ICLR years. All are associations within topic and year.
  - Where more of a topic's papers built on foundation models the year before, fewer of its papers propose new
    architectures (H1d): −8.0 pp in discovery, −11.0 pp held-out.
  - Newcomer papers are more often method papers and less often measurement papers (H2b′/H2c′): +3.7 / −1.7 pp in
    discovery, +3.6 / −2.1 pp held-out. The measurement gap again shrinks with team size controlled. The held-out
    newcomer measure sees both splits' histories, so it is better informed than discovery's.
  - Among papers with an experienced author, papers far from every experienced co-author's earlier ICLR work are
    accepted less often (PH5 E1): −5.4 pp in discovery, −6.1 pp held-out.
  - Four secondary associations also hold. Each is one-sided at 0.05 and unadjusted, so with six secondary tests one
    false positive at this level would not be surprising:
    - the within-author counterpart E4;
    - one topic insider vs none (teams H1);
    - Emerging vs Mainstream keywords (A1);
    - partial persistence of topic acceptance edges (premia b, 0 < b < 1, and EB D0 > 0).
  - Of these, A1 has a 95% CI that includes 0 (two-sided p 0.063). D0 is a new test with no discovery counterpart.
    The held-out premia slope (0.60) is a different comparison from the within-discovery 0.38.
  - The replication supports the direction, not the size. H1d, H2c′, teams H1 and A1 were underpowered at the
    discovery effect. Their MDE80s (12.0, 2.4 and the derived ≈ 4.5 and ≈ 4.3) exceed the discovery estimates
    (−8.0, −1.70, +3.42, +2.67).
    - Among underpowered tests, the significant ones tend to overstate the effect.
    - Held-out estimates larger than discovery's (H1d −11.0 vs −8.0, H2c′ −2.10 vs −1.70, E4 +1.06 vs +0.55; E4 has
      no MDE80) therefore do not show that the effect is as large or larger, and the sizes should not be compared as
      if they had replicated.
- **P1b did not replicate: only the own-record tail (E1) is supported out of sample; the field-novelty tail remains
  discovery-only.**
  - The "two tails" reading is a discovery post hoc summary. It is not reported in the discovery sections of this
    file; see `presentation/shortlist.md`, finding 1 (outputs `output/posthoc/ph5_position/` and
    `output/posthoc/ph5_pivot/`). Within topic and year, lower acceptance goes with two tails:
    - the least-novel fifth of abstracts, those most similar to earlier ICLR work (P1b, −3.3 pp);
    - far jumps from the team's own record (E1, −5.4 pp).
  - The held-out least-novel-fifth contrast is −0.13 pp (CI −3.50 to +3.25).
  - The test had power 0.47 at the discovery effect and an MDE80 of 5.4 pp, so by the registered rule it is
    uninformative: it is not evidence that the discovery association (−3.3 pp) is absent. The CI includes both 0 and
    −3.3 pp.
  - The field-novelty tail remains a discovery-only post hoc association and should not be presented as replicated.
    The pooled P1b (−3.0 pp) is driven by the discovery papers and does not change this.
  - P7, the within-author novelty slope, is not supported either.
    - It has no registered MDE80, and the registered reading rule does not cover it.
    - A derived MDE80 (post hoc, one-sided: ≈ 1.0–1.1 pp per 10 percentile points) exceeds both estimates (+0.39
      and +0.34), which suggests low power.
- **FL is not confirmed, and the held-out level test was underpowered.**
  - The held-out FL level is −4.9 pp (one-sided p 0.14). This is below its MDE80 (14.5 pp), so by the registered
    rule the level test is uninformative, not evidence of no gap. With 134 FL papers, the MDE80 also exceeds the
    discovery gap (−11.3 pp), so the test could easily miss a gap of the discovery size.
  - The secondary trend has the opposite sign to the prediction (+3.2 pp per year, one-sided p 0.88) and no MDE. In
    the pooled re-run the trend roughly halves, from −3.0 to −1.9 pp per year for the keyword.
  - The "falling out of favour" reading of PH4 therefore remains a discovery-only post hoc description.
- **H3a is inconclusive again.**
  - Discovery and held-out are both negative (−1.7 and −1.5 pp per log unit), and neither is significant.
  - The hindsight requirement fails on held-out papers.
  - The estimate is well below the MDE80 (4.8 pp), so the test is uninformative about effects of this size.
- **Unregistered rows.** The 17 rows are two-sided, unadjusted and not interpreted as findings. One quoting rule
  follows from them: discovery readings that rest on unregistered PH5 contrasts should not be quoted without the
  held-out and pooled rows. This applies in either direction:
  - P2, a concurrent same-year twin. Discovery found +0.7 pp, read as "no detectable acceptance gap"
    (`presentation/shortlist.md`, finding 3). Held-out: +3.7 pp (p 0.010). Pooled: +1.9 pp (p 0.009, Holm 0.063).
  - E2, near vs median closeness to the own record. Discovery found +1.75 pp (Holm 0.15), read as "more closeness
    shows no reliable further gain". Held-out: +2.3 pp (p 0.17). Pooled: +2.1 pp (Holm 0.036).
  - P5, the (Q5 − Q3) contrast for newcomer minus incumbent papers, changes sign: discovery +1.3 pp, held-out −9.8 pp
    (p 0.030), pooled +0.4 pp.
  - P6, the (Q5 − Q3) contrast for mature minus young topics, grows from +4.7 to +10.7 pp (p 0.030); pooled +3.9 pp.

## Pooled re-run (exploratory)

The pooled re-run ran after the held-out run had finished:
- `run_pooled.py` for RQ2, RQ3 and E1–E10;
- `run_pooled.py rq1` for RQ1;
- `ICLR_CORPUS=pooled posthoc.py` for PH1–PH4 and the six PH5 modules.

Outputs: `output_pooled/frozen_run/`, `output_pooled/rq1_results.csv`, `rq1_summary.json` and
`output_pooled/posthoc/`. Logs: `output_pooled/logs/`.

Caveats:
- **It confirms nothing.** It contains the 11,099 held-out papers, and about 80% of each pooled sample is discovery
  papers, so agreement with discovery is expected and is not replication. The verdict labels in its outputs are
  descriptive. The discovery outputs remain the registered record.
- **Pooling changes discovery features.** It is not "discovery plus held-out" on fixed features:
  - hot status changes for 8.1% of discovery papers (69 of 800 k100 topic-years);
  - discovery incumbency rises by 3.5 pp, from 26.5% to 30.0%;
  - probable earlier versions rise from 170 to 224;
  - maturity rises by about 0.22 log units.
- **Calibration.** The same caveats apply as in discovery: CR1 p-values are approximate under topic structure that
  cuts across the k100 map.

| | Discovery (registered record) | Pooled (exploratory) |
|---|---|---|
| H1a method ~ maturity, pp per log unit | −0.14 (−1.8, +1.5) | −0.59 (−2.0, +0.9); not supported |
| H1b measurement ~ maturity | +0.50 (−0.8, +1.8) | +0.81 (−0.3, +1.9); not supported |
| H1c empirical ~ maturity | −0.31 (−1.3, +0.7) | −0.24 (−1.1, +0.7); not supported |
| **H1d** new architecture ~ prior FM adoption, 0 → 100% | −8.0 (−12.1, −3.8); Holm 0.001 | −8.9 (−13.1, −4.7); Holm 3 × 10⁻⁴; supported |
| H1e empirical or evaluation ~ prior FM adoption | −0.6 (−3.6, +2.4) | −0.6 (−3.7, +2.6); not supported |
| H2a incumbent ~ hot | −0.73 (−2.68, +1.22) | −0.85 (−3.12, +1.42); inconclusive |
| **H2b** method ~ newcomer | +3.71 (+2.61, +4.80) | +3.46 (+2.38, +4.54); bootstrap p < 1/9,999; opposite to prediction |
| **H2c** measurement ~ newcomer | −1.70 (−2.46, −0.93) | −1.65 (−2.36, −0.94); bootstrap p < 1/9,999; opposite to prediction |
| H3a accepted ~ maturity, pp per log unit | −1.68 (−3.68, +0.32); Holm 0.20 | −1.72 (−3.44, −0.01); p 0.049, Holm 0.098; inconclusive |
| H3b accepted ~ maturity × method | −0.36 (−1.51, +0.79) | −0.03 (−1.08, +1.02); TOST p 0.034, "equivalent to null" |
| E1 acceptance of FM papers, topic × year | +4.62 (+2.79, +6.44) | +5.61 (+3.93, +7.29) |
| E2 acceptance of newcomer papers, topic × year | −10.2 (−11.8, −8.7) | −10.2 (−11.6, −8.9) |
| E8 new architecture × prior FM adoption, acceptance | +8.3 (+1.3, +15.4); p 0.02 | +9.4 (+2.3, +16.4); p 0.010 |
| PH2 acceptance per doubling of team size | +8.8 (+8.0, +9.7) | +8.8 (+8.0, +9.6) |
| PH3 newcomer gap with author FE | −3.1 (−4.5, −1.6) | −3.1 (−4.5, −1.7) |
| PH4 FL keyword, level | −11.3 (−17.9, −4.8); q 0.19 | −9.9 (−15.3, −4.5); q 0.14 |
| PH4 FL topic m029, level | −13.5 (−21.1, −5.9); q 0.17 | −12.8 (−17.4, −8.2); q 0.037, BH-flagged |
| PH4 FL keyword, trend, pp per year | −3.0 (−6.4, +0.5); p 0.08 | −1.9 (−5.1, +1.3); p 0.18 |
| PH4 FL topic m029, trend, pp per year | −2.7 (−7.0, +1.5); p 0.15 | −1.2 (−4.1, +1.7); p 0.34 |
| PH4 keyword extremes (≥ 5 years) | lowest CNNs −14.2, highest pre-training +9.9; none flagged | CNNs −12.8, pre-training +9.1; none flagged |
| PH4 topic extremes (≥ 5 years) | lowest clinical ML −14.9, highest neural rendering +13.5; none flagged | clinical ML −16.2 (q 0.037), neural rendering +16.6 (q 0.058); 4 topics flagged |
| PH5 E1 far jump, p10 minus p50 | −5.44 (−7.10, −3.78); Holm 1.3 × 10⁻⁸ | −5.53 (−7.09, −3.96); Holm 1.2 × 10⁻⁹ |
| PH5 E2 near, p90 minus p50 | +1.75 (−0.17, +3.66); Holm 0.148 | +2.10 (+0.37, +3.84); Holm 0.036 |
| PH5 P1b least-novel fifth minus middle | −3.27 (−4.93, −1.60); Holm 0.0014 | −2.97 (−4.42, −1.52); Holm 0.0008 |
| PH5 P2 any concurrent same-year twin | +0.68 (−0.84, +2.20); Holm 1.0 | +1.86 (+0.47, +3.24); p 0.009, Holm 0.063 |
| PH5 E4 within-author, per +0.1 cosine | +0.55 (+0.21, +0.90); Holm 0.006 | +0.78 (+0.50, +1.06); Holm 1 × 10⁻⁶ |
| PH5 P7 within-author, per 10 novelty percentile points | +0.39 (+0.09, +0.69); Holm 0.105 | +0.43 (+0.16, +0.70); Holm 0.063 |
| PH5 teams H1, one topic insider vs none | +3.42 (+1.18, +5.66); Holm 0.019 | +2.90 (+0.95, +4.85); Holm 0.024 |
| PH5 kwtiming A1, Emerging minus Mainstream | +2.67 (+0.76, +4.58); Holm 0.020 | +3.10 (+1.39, +4.81); Holm 0.0015 |
| PH5 premia b, early map, 2024–26 on 2018–22 | 0.38 (0.18, 0.58) | 0.45 (0.27, 0.64) |

- **RQ1–RQ3.**
  - Every hypothesis keeps its discovery sign and its descriptive verdict, except H3b: its estimate moves to zero and
    TOST now labels it "equivalent to null". The label is descriptive.
  - H3a's p falls to 0.049 (Holm 0.098), so it is still inconclusive.
- **PH4.**
  - Four k100 topics pass Benjamini–Hochberg in the pooled run: clinical ML −16.2 pp, FL −12.8 pp, graph
    representation learning −9.7 pp and robot learning +12.1 pp. No keyword passes.
  - These flags are exploratory. In particular, the registered held-out FL test was not supported.
  - The FL trend roughly halves (keyword −3.0 → −1.9 pp per year, p 0.18; topic −2.7 → −1.2, p 0.34). Its registered
    held-out test had the opposite sign (+3.2 pp per year).
- **PH5.**
  - Every headline estimate keeps its sign; this is expected, since about 80% of each pooled sample is discovery
    papers.
  - The pooled P1b is driven by the discovery papers: the held-out estimate is about zero.
  - Two unregistered rows that bear on discovery null readings move:
    - E2, near closeness, becomes Holm-significant (+2.1 pp, Holm 0.036; discovery 0.148);
    - P2, a concurrent twin, is +1.9 pp (p 0.009, Holm 0.063).
    These rows are exploratory too; see the quoting rule under "Unregistered rows" above.

## Reproduction

```text
python -m unittest discover -s research/fashion/tests      # statsmodels cross-checks run if importable
python research/fashion/dryrun.py                           # about 2 h on 4 cores -> output/dryrun/
python research/fashion/dryrun_diagnostics.py               # -> output/checks/dryrun_v3_diagnostics.json
python research/fashion/freeze.py --created <UTC> --remedy bootstrap:H2b --remedy bootstrap:H2c
python research/fashion/run_frozen.py                       # refuses unless FREEZE.json matches a clean tree
python research/fashion/figures.py                          # -> output/figures/F1-F7
```

Held-out replication and pooled re-run (2026-10-18; outputs under `output_pooled/`):

```text
python research/topics/keyword_map.py                       # keyword lookup learned on discovery only
ICLR_CORPUS=pooled python research/topics/pooled_topics.py  # frozen-map assignment of released papers + gates
ICLR_CORPUS=pooled python research/fashion/build_pooled.py  # pooled features, outcome-free -> build_report.json
python research/fashion/run_confirmation.py --simulate 1 --mde-reps 100   # simulated outcomes: plumbing, MDE80
python research/fashion/ph5_confirm.py calibrate            # PH5 E1/P1b calibration on simulated outcomes
python research/fashion/freeze_confirmation.py --created <UTC>             # commit, then:
python research/fashion/run_confirmation.py                 # once; refuses unless FREEZE_CONFIRMATION.json matches
python research/fashion/run_pooled.py                       # exploratory, only after the held-out run: RQ2, RQ3, E1-E10
python research/fashion/run_pooled.py rq1
ICLR_CORPUS=pooled python research/fashion/posthoc.py ph1   # also ph2, ph3, ph4; then ph5 <slug> for
                                                            # pivot, position, teams, kwtiming, premia, fmwave
```
