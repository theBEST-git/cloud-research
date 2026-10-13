# Idea-twin study: feasibility pilot (2026-10-13)

No decisions of candidate pairs were read at any stage. The power section uses only the pooled
acceptance rate among reviewed submissions (0.306).

## What was done
1. **Candidates** (`src/twins/candidates.py`): same-cycle pairs within each other's top-3 neighbours on name-masked bge abstracts (cos >= 0.86), plus top-3 MiniLM pairs. Pairs with shared author keys or names, near-identical titles (title cos >= 0.95) and desk-rejected/other members are excluded: 64,272 clean pairs (2026 alone 27,339).
2. **Known case**: the ICLR 2023 Flow Matching / Rectified Flow / Stochastic Interpolants trio has masked cosines 0.876-0.923, below a fixed 0.92/0.94 threshold, but it is found by top-3 retrieval.
3. **Pilot labels** (`src/twins/sample_pilot.py`, `RUBRIC.md`): 320 candidates (16 per band x era stratum), 3 known positives, 16 random same-topic pairs; two independent LLM labellers each, blind to titles and decisions, on name-masked abstracts.

## Results (`pilot_summary.json`, `pilot_precision_by_stratum.csv`)
- **Labels are reliable.** Agreement 92.9%; kappa 0.86 (4 classes), 0.70 (twin vs not), 0.90 (same problem or twin vs not). Random same-topic pairs: 14/16 labelled 'related only' by both, none 'twin'.
- **Known positives are not a valid check**: the rubric's twin example describes flow matching, so the trio was recognisable from the rubric. Fix for any rerun: no example drawn from the data.
- **True twins are rare.** Both labellers say 'twin' for 9/320 candidates (2.8%); either labeller 15/320. Even at masked cos >= 0.94 only 6% (strict) to 16% (lenient). 'Same problem, different idea' dominates the top bands: 84% at >= 0.94, 59% at 0.92-0.94.
- **Yield.** Projected strict twins in the two top bands (5,729 pairs): about 100 (0.94+: ~85; 0.92-0.94: ~16). Two hits in the 2018-23 0.86-0.88 stratum (N = 7,546) inflate the all-band projection to 1,044 +/- 626, which is not usable: twins below 0.92 are spread at ~1-3% over ~58k pairs and cannot be found economically.
- **Power.** Chance concordance (accept vs not) is 0.575. With ~100 twins the SE is 0.049 and the 80%-power MDE is ~14 pp. NeurIPS 2014/2021 same-paper experiments sit roughly 9-14 pp above chance; independent twins (different execution) should sit lower. The twin-concordance test is therefore underpowered; the within-twin title test (tens of discordant pairs) is not feasible.
- **Same-problem pairs are plentiful**: ~13.6k (+/- 1.7k) projected, ~5k in the top bands with 60-85% precision, enough for a different question (same-cycle competition on one problem), not for idea-level reliability.

## Verdict
The 'same idea, same fate?' design is not feasible at useful power with this corpus (80% discovery split, abstracts only). A same-problem competition design is feasible but answers a different, weaker question.
