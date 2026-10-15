# Research-fashion analyses

Analyses for the paper on how research fashions rise, are followed, and are rewarded at ICLR (2017–2026).
The plan, hypotheses and decision rules are fixed in [PREREGISTRATION.md](PREREGISTRATION.md). Read it first.

| File | Purpose |
|---|---|
| `PREREGISTRATION.md` | hypotheses H1–H3, variables, models, decision rule, robustness, confirmation |
| `common.py` | paths, contribution classes, topic maps (k100 main; k75/k150 from the k sweep; balanced/early/middle_era/late from the hindsight check) |
| `topic_maturity.py` | topic-year maturity variables for every map → `output/topic_year_maturity.csv.gz` |
| `ols.py` | least squares with absorbed fixed effects and CR1 cluster-robust SE; matches statsmodels exactly |
| `rq1_rise.py` | RQ1 (H1a–e) with 9 robustness variants, including the two mandatory hindsight variants → `output/rq1_results.csv`, `output/rq1_summary.json` |
| `variables.py` | RQ2/RQ3 paper variables per map: incumbent / newcomer (and S3, S4 versions), hot topics, team size → `output/paper_variables.csv.gz` |
| `buzzwords.py` | buzzword measure (D5): hot keywords and atypical keyword use → `output/keyword_year.csv.gz`, `keyword_uses.csv.gz`, `paper_buzzword.csv.gz` |
| `resubmissions.py` | nearest earlier-year paper (centred SPECTER2 cosine), exact titles; with `--tau`, probable earlier versions (R1, S4) → `output/earlier_versions.csv.gz` |
| `annotation/` | blind LLM judging: H2d validation (`keyword_centrality/`) and τ calibration (`resubmission_pairs/`); seeded samplers (no key file), instructions, collector with transcript audit, scorers → `output/h2d_validation.json`, `output/resubmission_tau.json` |
| `panel.py`, `variants.py` | outcome-free analysis frame per map; the counted variant registry shared by RQ1–RQ3 |
| `analysis.py`, `logit.py`, `dgp.py` | estimation (LPM with absorbed FE, FE logit), the registered remedy (wild cluster restricted bootstrap) and S11 (two-way clustered SE), verdicts (Holm, 75% rule, hindsight, equivalence, fragile flag); synthetic outcomes for dry-runs |
| `outcomes.py` | the only file that reads acceptance or review columns: simulated, permuted, and (frozen runs only) real modes |
| `rq2_following.py`, `rq3_reward.py`, `exploratory.py` | H2a–c, H3a–b with counted and supplementary variants; planned exploratory analyses E1–E10 |
| `dryrun.py` | size, false support and power before the freeze → `output/dryrun/` (v2, which triggered the remedy for H2b/H2c: `output/dryrun_v2/`) |
| `freeze.py`, `run_frozen.py` | `FREEZE.json` (hashes and frozen settings); the single real run → `output/frozen_run/` |
| `tests/` | prospectivity, outcome lint, guards, sealed loader, estimators (vs statsmodels and brute force), variant registry (reproduces RQ1's n), protocol, remedy wiring |

## Run order

```text
python research/topics/annotation/contribution_types/llm_labeling/merge_labels.py <returned run dir>
python research/fashion/topic_maturity.py
python research/fashion/rq1_rise.py
# RQ2 / RQ3 (outcome-blind until run_frozen.py)
python research/fashion/buzzwords.py
python research/fashion/resubmissions.py
python research/fashion/annotation/keyword_centrality/sample.py        # then judge with annotation/judge_batches.js
python research/fashion/annotation/resubmission_pairs/sample.py
python research/fashion/annotation/collect.py <task dir> <workflow transcript dirs>
python research/fashion/annotation/keyword_centrality/score.py
python research/fashion/annotation/resubmission_pairs/score.py
python research/fashion/resubmissions.py --tau <tau>
python research/fashion/variables.py
python research/fashion/dryrun.py
python research/fashion/freeze.py --created <UTC time> --remedy bootstrap:H2b --remedy bootstrap:H2c   # commit, then:
python research/fashion/run_frozen.py
```

The merge writes `research/topics/output/paper_contributions.csv.gz` and checks the label-quality gate in the
pre-registration. Tests: `python -m unittest discover -s research/fashion/tests` (estimator tests need statsmodels).

## Dry-runs (before real labels)

`rq1_rise.py --labels <file> --out <dir>` was run only on synthetic labels:
- **Shuffled within year (no signal):** nothing passes the decision rule.
- **Planted negative effect of maturity on `method`:** detected in the main specification and in all 9
  robustness variants.

`ols.py` reproduces statsmodels' coefficient and its cluster-robust SE (under the same small-sample rule) on
simulated data.

## RQ1 results (pre-registered tests, real labels, 2026-10-15)

`output/rq1_results.csv`, `output/rq1_summary.json`. Linear probability models with topic and year fixed effects and
SE clustered by topic. 43,096 papers from 2018–2026; 100 topics.

| | Outcome ~ regressor | Main estimate (95% CI) | Robustness (same sign) | Verdict |
|---|---|---|---|---|
| H1a | method ~ maturity | −0.14 pp per log unit (−1.8, +1.5) | 78% | not supported |
| H1b | measurement ~ maturity | +0.50 pp (−0.8, +1.8) | 89% | not supported |
| H1c | empirical ~ maturity | −0.31 pp (−1.3, +0.7) | 0%, hindsight check fails | not supported |
| **H1d** | **model (new architecture) ~ prior FM adoption** | **−8.0 pp for 0 → 100% FM share (−12.1, −3.8); Holm p = 0.001** | **100%, both hindsight variants** | **supported** |
| H1e | empirical or evaluation ~ prior FM adoption | −0.6 pp (−3.6, +2.4) | 44% | not supported |

- **Maturity (H1a–c).** Within a topic, and net of field-wide year trends, the contribution mix does not move with
  how many papers the topic has accumulated. The intervals rule out more than about 1–2 points per log unit.
  - Exploratory only, not a pre-registered claim: under the prospective early map, the estimates point the
    predicted way (method −3.5 pp, measurement +4.0 pp per log unit). Whether lifecycles show up therefore depends
    on how topics are defined.
- **Foundation-model adoption (H1d–e).** When more of a topic's papers built on foundation models in the previous
  year, fewer of its papers propose new architectures. The effect ranges from −6.3 to −14.2 points across all
  9 variants, against a mean of 9.2%. The architecture share fell from 24.5% (2017) to 7.5% (2026), while the
  foundation-model share rose from 0% to 54%. The expected shift towards empirical and evaluation work (H1e) is
  not found.

## RQ2 and RQ3 results (single frozen run, 2026-10-15)

Full write-up: [RESULTS.md](RESULTS.md). Outputs: `output/frozen_run/` (committed before interpretation). Protocol:
`PREREGISTRATION.md` and `FREEZE.json`.

| | Outcome ~ regressor (prediction) | Main estimate (95% CI) | Verdict |
|---|---|---|---|
| H2a | incumbent ~ hot topic (−) | −0.73 pp (−2.68, +1.22) | inconclusive |
| **H2b** | **method ~ newcomer (−)** | **+3.71 pp (+2.61, +4.80)** | **significant in the opposite direction** |
| **H2c** | **measurement ~ newcomer (+)** | **−1.70 pp (−2.46, −0.93)** | **significant in the opposite direction** |
| H3a | accepted ~ maturity (−) | −1.68 pp per log unit (−3.68, +0.32) | inconclusive (underpowered) |
| H3b | accepted ~ maturity × method (−) | −0.36 pp per log unit (−1.51, +0.79) | inconclusive |

- Newcomer papers are more often method papers, and less often measurement papers (datasets, benchmarks,
  evaluation), than papers with at least one incumbent author. Newcomer means no author has an earlier ICLR
  submission in the same topic (any outcome; exact author IDs, so earlier work under another ID or at other venues
  is not seen).
  - Both findings hold in all ten counted variants (same sign, p < 0.05) and under two-way clustering.
  - With team size controlled (S1), the method gap is unchanged (+3.92 pp), but the measurement gap shrinks to
    −0.54 pp (p = 0.07).
- No reward hypothesis is supported. H3a points the predicted way in every counted variant, but the test was
  underpowered, so it is uninformative about effects below about 4 pp per log unit.
- H2d/H3c were dropped: the buzzword measure failed its blind validation.
- All results are associations within topic and year, not causal effects.
- The H2b/H2c p-values and CIs are approximate.
  - Under a simulated cross-map null the registered test rejected about 10–12% of the time at nominal 5%, and the
    bootstrap remedy did not fix this.
  - Family-wise error can also exceed 5% under such structure: 6.4% for any RQ2 support in the simulated case.
  - Both findings remain clear under two-way clustering, and under a pre-declared stress bracket from that one
    simulated scenario (Holm p 4 × 10⁻⁶ and 1 × 10⁻³). The bracket is not a correction.
