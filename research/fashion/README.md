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

## Run order (after the full labels are merged)

```text
python research/topics/annotation/contribution_types/llm_labeling/merge_labels.py <returned run dir>
python research/fashion/topic_maturity.py
python research/fashion/rq1_rise.py
```

The merge writes `research/topics/output/paper_contributions.csv.gz` and checks the label-quality gate in the
pre-registration. RQ2 and RQ3 code follows the pre-registration and is added after RQ1.

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
