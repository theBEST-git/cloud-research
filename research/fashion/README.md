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
