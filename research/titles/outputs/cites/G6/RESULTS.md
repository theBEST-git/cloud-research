# G6: catchy title templates and citations

**Code:** `src/cites/g6.py`. **Numbers:** `outputs/cites/G6/results.json`. **Figure:** `outputs/cites/G6/fig.png` (plotted values in `fig.csv`).
**Pre-registration:** `docs/CITES_PREREG.md` (frozen 2026-10-17). **Frozen core:** `src/cites/core.py` (not edited).

## Question

Among accepted ICLR papers from 2017 to 2025, do papers whose titles use a catchy template get more or fewer Semantic Scholar citations than accepted papers with similar content?

- **G6a meme templates** (n = 83): All You Need, Is Secretly, Free Lunch, Less Is More, Lost In, The Devil Is In, A Tale Of, To Rule Them All, Worth a Thousand / N Words, Matters, Do X Really …?, When X Meets Y. Examples: "Hopfield Networks is All You Need", "TabR: Tabular Deep Learning Meets Nearest Neighbors".
- **G6b tentative framings** (n = 500): Towards, Rethinking, Revisiting, Understanding, On the, Demystifying. Examples: "Towards Understanding Sycophancy in Language Models", "Rethinking Attention with Performers".

**Sample.**
- 8,602 accepted papers matched to an S2 venue record.
- 8,574 enter the regression; singleton year × topic50 cells are dropped.

**Features.**
- `G6a_meme` and `G6b_tentative` flag a title that matches any regex in `core.MEME` or `core.TENTATIVE`. The patterns are in `src/features.py` `TEMPLATES` and run on the lowercased title.
- Tentative openers also match right after a "NAME:" prefix (116 of the 500), except "On the", which matches only at the start of the title.
- 4 titles are in both groups.

**Timing.**
- Meme templates are recent: 14 of the 83 are from 2017–21, 69 are from 2022–25, and 31 (37%) are from 2025 alone.
- Tentative framings: 100 are from 2017–21 and 400 from 2022–25.

**Model.**
- Outcome: y = log(1 + citations), with citations retrieved 2026-10-17.
- Specification: `y ~ feature + log(team size) + log(abstract words) + 20 abstract-embedding PCs | year × topic50`.
- SEs clustered by topic50.
- Effect scale: % difference = exp(b) − 1.

## Primary estimates (pre-registered)

| | % difference in citations | 95% CI | p | Holm p (8 tests) | n | n with feature |
|---|---|---|---|---|---|---|
| G6a meme template | **+37.9%** | +2.9% to +84.8% | 0.037 | **0.183** | 8,574 | 83 |
| G6b tentative framing | **+3.7%** | −7.8% to +16.7% | 0.544 | **0.544** | 8,574 | 500 |

- The estimates and Holm p are taken from `outputs/cites/primary.json`.
- Re-computing both with `core.primary` reproduces them exactly: largest absolute difference 0, with the same n and n with feature.
- **Holm step.** G6a has the 4th-smallest of the 8 primary p-values, so its Holm threshold is 0.05/5 = 0.01, and Holm p = 5 × 0.0366 = 0.183. G6b has the largest p-value, so its Holm p equals its raw p.

## Robustness checks R1–R7 (pre-registered, `core.robustness`)

**G6a meme templates (83 papers)**

| Check | % difference | 95% CI | p | n |
|---|---|---|---|---|
| Primary | +37.9% | +2.9, +84.8 | 0.037 | 8,574 |
| R1 content-matched pairs (name-masked embedding, cosine ≥ 0.80) | +18.0% | −23.1, +83.0 | (bootstrap) | 83 pairs |
| R2 PPML on raw counts (sign check only) | +39.6% | −25.6, +162.1 | 0.30 | 8,574 |
| R3 influential-citation count | +23.4% | −1.9, +55.4 | 0.079 | 8,574 |
| R4 drop top 1% most-cited per year | +37.4% | +2.1, +84.7 | 0.041 | 8,481 |
| R5 2017–21 only (14 meme titles) | +44.2% | −19.5, +158.1 | 0.22 | 1,975 |
| R5 2022–25 only (69 meme titles) | +37.5% | −1.5, +92.0 | 0.068 | 6,599 |
| R6 2022–25 + team's prior ICLR acceptances | +36.9% | −2.7, +92.4 | 0.077 | 6,599 |
| R7 year + topic100 FE | +30.9% | −2.1, +75.1 | 0.075 | 8,602 |

- **All checks are positive.** R4–R7 are within 7 points of the primary.
- Only R4 excludes zero, as the primary does. The others have lower CI limits between −1.5% and −25.6%.
- R1 and R3 are smaller, at +18% and +23%.
- R2 (PPML on raw counts) is dominated by a few very highly cited papers (see diagnostic (a)).

**G6b tentative framings (500 papers)**

| Check | % difference | 95% CI | p | n |
|---|---|---|---|---|
| Primary | +3.7% | −7.8, +16.7 | 0.544 | 8,574 |
| R1 content-matched pairs (name-masked embedding, cosine ≥ 0.80) | **−13.1%** | −24.4, +0.6 | (bootstrap) | 497 pairs |
| R2 PPML on raw counts (sign check only) | +13.2% | −27.6, +76.9 | 0.59 | 8,574 |
| R3 influential-citation count | −1.3% | −13.1, +12.0 | 0.84 | 8,574 |
| R4 drop top 1% most-cited per year | +4.4% | −6.7, +16.7 | 0.46 | 8,481 |
| R5 2017–21 only (100 tentative titles) | +10.8% | −15.4, +45.1 | 0.46 | 1,975 |
| R5 2022–25 only (400 tentative titles) | +1.1% | −11.1, +14.9 | 0.87 | 6,599 |
| R6 2022–25 + team's prior ICLR acceptances | 0.0% | −12.2, +13.8 | 0.995 | 6,599 |
| R7 year + topic100 FE | +1.2% | −9.2, +12.8 | 0.83 | 8,602 |

- R3–R7 all lie between −1% and +11%, and none excludes zero.
- R1 has the opposite sign (−13.1%). Diagnostic (f) shows that the R1 procedure itself is shifted down by about 22% under the null.

## Verdict (pre-registered rule)

**G6a meme templates: "inconclusive."**
- **"More citations" fails.** It needs Holm p < 0.05, and Holm p = 0.183. The sign conditions hold: R1 is +18.0% and R2 is +39.6%.
- **"No meaningful difference" fails.** The 95% CI (+2.9% to +84.8%) is not inside ±10%.
- That verdict was also out of reach. With 83 papers, the CI is 0.59 log points wide, against a band width of 0.20.

**G6b tentative framings: "inconclusive."**
- **"More" / "fewer" fails.** Holm p is 0.544, and R1 has the opposite sign (−13.1%). R2 has the same sign.
- **"No meaningful difference" fails.** The upper CI limit, +16.7%, exceeds +10%.
- **That verdict was not attainable at this sample size.** The CI width is 0.236 log points against a band width of 0.201; it would need SE ≤ 0.051, while the observed SE is 0.060.

## Secondary analyses (pre-specified in prereg section 6; no multiplicity claim)

### Each template with n ≥ 20

Each row comes from two models:
- **(i)** the template dummy in the primary specification, so the reference is all other titles;
- **(ii)** the same, plus a dummy for "another template of the same family", so the reference is titles with no template of that family.

The two versions differ by at most 0.4 points.

| Template | Family | n (2022–25) | (i) % diff vs all other titles | 95% CI | p | (ii) % diff vs no template of family | 95% CI |
|---|---|---|---|---|---|---|---|
| When X Meets Y / X Meets Y | meme | 29 (25) | +29.8% | −6.2, +79.7 | 0.12 | +30.0% | −6.1, +79.9 |
| Towards | tentative | 217 (182) | −0.8% | −15.8, +16.9 | 0.92 | −0.5% | −15.8, +17.5 |
| On the | tentative | 104 (75) | −0.8% | −27.2, +35.2 | 0.96 | −0.5% | −26.9, +35.5 |
| Understanding | tentative | 72 (53) | −2.6% | −28.2, +32.1 | 0.87 | −2.2% | −28.1, +32.8 |
| Rethinking | tentative | 64 (57) | **+33.1%** | +4.0, +70.3 | 0.028 | +33.1% | +4.3, +69.8 |
| Revisiting | tentative | 35 (27) | +11.6% | −18.4, +52.6 | 0.50 | +11.9% | −18.0, +52.7 |

**Templates below n = 20** are shown with counts and the raw median within-year citation percentile only. These are descriptive; the median for papers without a template is 0.50.
- **Meme:** All You Need 18 (0.69), Matters 10 (0.32), Is Secretly 8 (0.63), Do X Really 7 (0.80), Devil In 4 (0.55), Free Lunch 2, Worth N Words 2, Less Is More 1, Tale Of 1, Rule Them All 1, Lost In 0.
- **Tentative:** Demystifying 9 (0.38).

**Reading.**
- No meme template other than When X Meets Y reaches n = 20, so the meme family cannot be split further at the pre-specified threshold.
- When X Meets Y (+30%) is close to the family estimate, with a CI that includes zero.
- Among the tentative templates, "Rethinking" alone is positive with a CI excluding zero (p = 0.028).
  - This is one of 6 template tests without multiplicity control; 6 × 0.028 = 0.17.
  - The three largest templates are all within ±3% of zero: Towards (217), On the (104) and Understanding (72).
  - Treat "Rethinking" as a hypothesis, not a finding.

### Joint model with all 8 primary features

| Feature | % difference | 95% CI | p |
|---|---|---|---|
| G6a meme | +30.7% | −4.2, +78.4 | 0.097 |
| G6b tentative | +7.2% | −5.0, +21.0 | 0.27 |

- **G6a shrinks from +37.9% to +30.7%.** Its largest overlap is with G2 ("assertive verb"). A G2 control alone gives +25.5% (diagnostic (c)).
- **G6b rises slightly, from +3.7% to +7.2%.** A G1 (named) control alone gives +5.3%: 13% of tentative titles are named, against 25% of other titles.

### Heterogeneity by LLM-topic papers

| Feature | LLM-topic papers | other papers | Ratio of multipliers (95% CI), p |
|---|---|---|---|
| G6a meme | +54.2% (+2.1, +133.0), n 20 | +34.5% (−5.5, +91.6), n 63 | 1.15 (0.67, 1.97), p 0.62 |
| G6b tentative | +24.8% (−8.7, +70.6), n 99 | −0.2% (−12.0, +13.2), n 401 | 1.25 (0.90, 1.73), p 0.18 |

- There is no evidence of a difference between LLM-topic and other papers for either feature.
- The LLM-topic share is similar across groups: meme 24.1% vs 22.4% for other titles; tentative 19.8% vs 22.6%.

## Diagnostics — diagnostic (not pre-registered)

All analyses in this section were added after the primary estimates were seen.

### (a) Do 1–3 superstar papers drive G6a?

Citation counts among meme papers are very concentrated.
- **The top paper dominates.** "A Time Series is Worth 64 Words" (PatchTST, 2023) has 5,012 citations, **37.6%** of the 13,325 citations to all 83 meme papers.
- **The top 3 hold half.** The three most-cited hold **50.8%**. The median meme paper has 39 citations.

The log outcome compresses this, and the full list below shows the shift is broad:
- 63.9% of meme papers are above their year's citation median, against 49.9% of other papers.
- 15.7% are in their year's top decile, against 10.0%.
- Median within-year percentile: 0.64.

| Diagnostic (G6a) | % difference | 95% CI | p | n meme |
|---|---|---|---|---|
| Primary (pre-registered) | +37.9% | +2.9, +84.8 | 0.037 | 83 |
| Leave-one-out, range over all 83 papers | +32.4% to +43.0% | | max p 0.066 | 82 |
| Drop the most-cited (PatchTST) | +32.4% | −1.2, +77.4 | 0.066 | 82 |
| **Drop the 3 most-cited** (PatchTST, DrQ "Image Augmentation Is All You Need", "Hopfield Networks is All You Need") | **+25.7%** | −6.1, +68.3 | 0.13 | 80 |
| Drop the 5 most-cited | +17.8% | −11.5, +56.7 | 0.27 | 78 |
| Drop the 10 most-cited | +8.9% | −17.0, +42.7 | 0.54 | 73 |
| Drop the 3 highest within-year percentiles | +23.4% | −6.6, +63.0 | 0.15 | 80 |
| Trim 3 most- and 3 least-cited | +38.5% | +8.2, +77.3 | 0.013 | 77 |
| Trim 10 most- and 10 least-cited | +47.8% | +21.9, +79.2 | 0.0002 | 63 |
| Outcome = within-year citation percentile (×100) | **+7.3 percentile points** | +1.3, +13.3 | 0.021 | 83 |

**Calibrating "drop the top 3".** Dropping a group's most-cited members lowers its estimate by construction.
- **Placebo.** In 200 placebo draws, we picked 83 random papers without a meme template, matched the meme papers' per-year counts, and dropped their 3 most-cited.
- **Mechanical shift.** On average this lowers b by 0.086 log points (95% range 0.045–0.133).
- **The meme group's shift is ordinary.** Its shift is 0.092, at the 38th percentile of that placebo distribution.
- **Placebo-centred estimate.** Adding back the mean mechanical shift gives +36.9% (approximately +2.3, +83.4).

**Reading.**
- **No single paper, or set of three, drives the log-scale point estimate.**
  - Leave-one-out estimates stay between +32% and +43%.
  - The drop from +38% to +26% when the top 3 are removed is about what removing the top 3 of any random 83-paper group does.
  - The within-year-percentile outcome, which bounds each paper's influence, is still positive.
  - Trimming both tails raises the estimate, because the meme group also has several near-zero-citation 2024–25 papers.
- **The nominal significance is fragile.** Removing PatchTST alone moves the unadjusted p from 0.037 to 0.066. Every leave-one-out p is at most 0.066, and 73 of 83 are below 0.05. The pre-registered test already fails on Holm p.
- **On the raw-count scale, superstars dominate.** That is why R2 (PPML) has such a wide CI.
- **G6b has no superstar problem.** Its top 3 papers (Madry et al. 15,844; Zhang et al. 5,334; FedAvg 3,181) hold 31.5% of tentative-paper citations.
  - Dropping them gives +2.1% (−9.7, +15.5); dropping the top 10 gives −1.2%.
  - The within-year-percentile outcome is +0.9 points (−1.4, +3.2).

<details>
<summary>All 83 meme-template papers, by citations. LOO % = G6a primary estimate with that paper left out; G2 = also "assertive" (G2).</summary>

| # | Year | Citations | Within-year pctile | arXiv id | Template | G2 | LOO % | Title |
|---|---|---|---|---|---|---|---|---|
| 1 | 2023 | 5,012 | 0.998 | yes | Worth A Thousand / N Words | yes | +32.4 | A Time Series is Worth 64 Words: Long-term Forecasting with Transformers |
| 2 | 2021 | 980 | 0.961 | yes | X Is All You Need | yes | +33.5 | Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels |
| 3 | 2021 | 782 | 0.957 | yes | X Is All You Need | yes | +35.5 | Hopfield Networks is All You Need |
| 4 | 2020 | 695 | 0.912 | yes | X Is Secretly Y | yes | +33.6 | Your classifier is secretly an energy based model and you should treat it like one |
| 5 | 2023 | 602 | 0.957 | yes | When X Meets Y / X Meets Y |  | +34.1 | Spikformer: When Spiking Neural Network Meets Transformer |
| 6 | 2025 | 423 | 0.990 | yes | X Is Secretly Y |  | +33.1 | Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data |
| 7 | 2021 | 390 | 0.916 | yes | Free Lunch |  | +35.7 | Free Lunch for Few-shot Learning: Distribution Calibration |
| 8 | 2020 | 377 | 0.855 | yes | X Matters | yes | +37.1 | Skip Connections Matter: On the Transferability of Adversarial Examples Generated with ResNets |
| 9 | 2024 | 313 | 0.939 | yes | When X Meets Y / X Meets Y |  | +36.0 | When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method |
| 10 | 2017 | 260 | 0.472 | no | Do X Really ...? |  | +39.2 | Do Deep Convolutional Nets Really Need to be Deep and Convolutional? |
| 11 | 2023 | 258 | 0.915 | yes | Do X Really ...? |  | +35.6 | Do We Really Need Complicated Model Architectures For Temporal Networks? |
| 12 | 2019 | 229 | 0.729 | yes | When X Meets Y / X Meets Y |  | +38.0 | Defensive Quantization: When Efficiency Meets Robustness |
| 13 | 2024 | 211 | 0.908 | no | When X Meets Y / X Meets Y |  | +37.3 | Chain-of-Experts: When LLMs Meet Complex Operations Research Problems |
| 14 | 2022 | 162 | 0.838 | yes | When X Meets Y / X Meets Y |  | +36.5 | Robust Learning Meets Generative Models: Can Proxy Distributions Improve Adversarial Robustness? |
| 15 | 2025 | 140 | 0.950 | yes | X Is All You Need | yes | +35.0 | CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models |
| 16 | 2024 | 122 | 0.849 | yes | When X Meets Y / X Meets Y |  | +35.8 | Convolution Meets LoRA: Parameter Efficient Finetuning for Segment Anything Model |
| 17 | 2024 | 121 | 0.847 | yes | When X Meets Y / X Meets Y |  | +34.7 | TabR: Tabular Deep Learning Meets Nearest Neighbors |
| 18 | 2025 | 117 | 0.937 | yes | X Matters | yes | +35.6 | Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning |
| 19 | 2023 | 106 | 0.833 | yes | X Is All You Need | yes | +36.3 | H2RBox: Horizontal Box Annotation is All You Need for Oriented Object Detection |
| 20 | 2020 | 101 | 0.518 | no | X Is All You Need | yes | +38.5 | Sign Bits Are All You Need for Black-Box Attacks |
| 21 | 2024 | 95 | 0.815 | yes | When X Meets Y / X Meets Y |  | +38.1 | Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models |
| 22 | 2025 | 82 | 0.912 | yes | When X Meets Y / X Meets Y | yes | +36.3 | OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling |
| 23 | 2023 | 78 | 0.784 | yes | When X Meets Y / X Meets Y |  | +36.8 | When Source-Free Domain Adaptation Meets Learning with Noisy Labels |
| 24 | 2023 | 77 | 0.782 | yes | X Is All You Need | yes | +36.1 | Certified Training: Small Boxes are All You Need |
| 25 | 2021 | 75 | 0.553 | yes | When X Meets Y / X Meets Y | yes | +37.9 | Boost then Convolve: Gradient Boosting Meets Graph Neural Networks |
| 26 | 2022 | 74 | 0.700 | yes | X Is All You Need | yes | +37.8 | SphereFace2: Binary Classification is All You Need for Deep Face Recognition |
| 27 | 2022 | 73 | 0.695 | yes | To Rule Them All |  | +37.4 | No One Representation to Rule Them All: Overlapping Features of Training Methods |
| 28 | 2023 | 72 | 0.768 | yes | Free Lunch |  | +37.0 | Free Lunch for Domain Adversarial Training: Environment Label Smoothing |
| 29 | 2025 | 63 | 0.879 | yes | Do X Really ...? |  | +36.7 | Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist |
| 30 | 2023 | 63 | 0.734 | no | X Is All You Need | yes | +36.7 | Pink Noise Is All You Need: Colored Noise Exploration in Deep Reinforcement Learning |
| 31 | 2022 | 56 | 0.616 | yes | A Tale Of |  | +37.3 | A Tale of Two Flows: Cooperative Learning of Langevin Flow and Normalizing Flow Toward Energy-Based Model |
| 32 | 2024 | 52 | 0.719 | yes | When X Meets Y / X Meets Y |  | +37.6 | Zeroth-Order Optimization Meets Human Feedback: Provable Learning via Ranking Oracles |
| 33 | 2023 | 49 | 0.679 | no | X Is All You Need | yes | +37.3 | Loss Landscapes are All You Need: Neural Network Generalization Can Be Explained Without the Implicit Bias of Gradient Descent |
| 34 | 2025 | 48 | 0.837 | yes | X Is All You Need | yes | +34.5 | Standard Gaussian Process is All You Need for High-Dimensional Bayesian Optimization |
| 35 | 2021 | 47 | 0.393 | yes | X Matters | yes | +38.4 | Network Pruning That Matters: A Case Study on Retraining Variants |
| 36 | 2025 | 45 | 0.824 | yes | Do X Really ...? |  | +36.9 | Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book? |
| 37 | 2025 | 44 | 0.819 | yes | The Devil Is In |  | +36.6 | VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning |
| 38 | 2023 | 44 | 0.651 | yes | When X Meets Y / X Meets Y |  | +37.5 | When Data Geometry Meets Deep Function: Generalizing Offline Reinforcement Learning |
| 39 | 2025 | 43 | 0.815 | yes | X Is Secretly Y | yes | +36.2 | Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free |
| 40 | 2025 | 41 | 0.803 | yes | Do X Really ...? |  | +37.6 | Can Knowledge Editing Really Correct Hallucinations? |
| 41 | 2024 | 40 | 0.655 | no | The Devil Is In | yes | +39.2 | The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models |
| 42 | 2025 | 39 | 0.793 | yes | Do X Really ...? |  | +35.4 | Does SGD really happen in tiny subspaces? |
| 43 | 2024 | 38 | 0.641 | yes | When X Meets Y / X Meets Y |  | +36.5 | When Semantic Segmentation Meets Frequency Aliasing |
| 44 | 2023 | 38 | 0.608 | yes | X Is All You Need | yes | +37.6 | Copy is All You Need |
| 45 | 2023 | 37 | 0.601 | yes | X Is Secretly Y | yes | +37.4 | Your Contrastive Learning Is Secretly Doing Stochastic Neighbor Embedding |
| 46 | 2023 | 36 | 0.592 | yes | X Matters | yes | +38.6 | DAG Matters! GFlowNets Enhanced Explainer for Graph Neural Networks |
| 47 | 2023 | 35 | 0.582 | yes | When X Meets Y / X Meets Y |  | +38.1 | Transformer Meets Boundary Value Inverse Problems |
| 48 | 2023 | 33 | 0.561 | yes | X Matters | yes | +38.2 | Rethinking Graph Lottery Tickets: Graph Sparsity Matters |
| 49 | 2025 | 30 | 0.740 | yes | Do X Really ...? |  | +36.6 | Can In-context Learning Really Generalize to Out-of-distribution Tasks? |
| 50 | 2025 | 29 | 0.732 | yes | When X Meets Y / X Meets Y |  | +37.8 | NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation |
| 51 | 2023 | 29 | 0.513 | yes | X Is All You Need |  | +38.8 | Words are all you need? Language as an approximation for human similarity judgments |
| 52 | 2025 | 27 | 0.712 | yes | X Is All You Need | yes | +35.9 | A Single Goal is All You Need: Skills and Exploration Emerge from Contrastive RL without Rewards, Demonstrations, or Subgoals |
| 53 | 2019 | 26 | 0.136 | yes | When X Meets Y / X Meets Y | yes | +40.1 | Variance Networks: When Expectation Does Not Meet Your Expectations |
| 54 | 2023 | 23 | 0.435 | yes | The Devil Is In | yes | +38.2 | The Devil is in the Wrongly-classified Samples: Towards Unified Open-set Recognition |
| 55 | 2025 | 22 | 0.662 | yes | X Is Secretly Y | yes | +38.0 | Your Weak LLM is Secretly a Strong Teacher for Alignment |
| 56 | 2018 | 22 | 0.102 | no | X Matters | yes | +39.7 | Initialization matters: Orthogonal Predictive State Recurrent Neural Networks |
| 57 | 2024 | 20 | 0.474 | yes | When X Meets Y / X Meets Y |  | +38.1 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions |
| 58 | 2025 | 19 | 0.624 | yes | When X Meets Y / X Meets Y |  | +39.3 | Decision Information Meets Large Language Models: The Future of Explainable Operations Research |
| 59 | 2023 | 19 | 0.374 | no | Worth A Thousand / N Words |  | +40.9 | Is a Caption Worth a Thousand Images? A Study on Representation Learning |
| 60 | 2025 | 15 | 0.554 | yes | X Is Secretly Y | yes | +37.6 | Projection Head is Secretly an Information Bottleneck |
| 61 | 2019 | 15 | 0.053 | yes | X Is All You Need | yes | +40.8 | CBOW Is Not All You Need: Combining CBOW with the Compositional Matrix Space Model |
| 62 | 2024 | 12 | 0.320 | yes | The Devil Is In | yes | +38.4 | The Devil is in the Object Boundary: Towards Annotation-free Instance Segmentation using Foundation Models |
| 63 | 2021 | 12 | 0.097 | yes | When X Meets Y / X Meets Y |  | +40.5 | Deep Learning meets Projective Clustering |
| 64 | 2024 | 11 | 0.294 | yes | When X Meets Y / X Meets Y | yes | +39.6 | A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks |
| 65 | 2023 | 11 | 0.242 | yes | X Matters | yes | +38.5 | Calibration Matters: Tackling Maximization Bias in Large-scale Advertising Recommendation Systems |
| 66 | 2025 | 9 | 0.411 | yes | When X Meets Y / X Meets Y |  | +38.4 | State Space Model Meets Transformer: A New Paradigm for 3D Object Detection |
| 67 | 2025 | 8 | 0.383 | yes | When X Meets Y / X Meets Y |  | +40.2 | When Prompt Engineering Meets Software Engineering: CNL-P as Natural and Robust "APIs'' for Human-AI Interaction |
| 68 | 2025 | 8 | 0.383 | yes | X Is Secretly Y |  | +38.4 | Foundation Models Secretly Understand Neural Network Weights: Enhancing Hypernetwork Architectures with Foundation Models |
| 69 | 2025 | 7 | 0.350 | no | When X Meets Y / X Meets Y |  | +38.3 | Beyond Random Masking: When Dropout meets Graph Convolutional Networks |
| 70 | 2024 | 6 | 0.176 | no | Less Is More | yes | +40.0 | More is Better: when Infinite Overparameterization is Optimal and Overfitting is Obligatory |
| 71 | 2025 | 5 | 0.277 | yes | When X Meets Y / X Meets Y |  | +40.0 | Transformer Meets Twicing: Harnessing Unattended Residual Information |
| 72 | 2025 | 4 | 0.231 | yes | When X Meets Y / X Meets Y |  | +38.8 | qNBO: quasi-Newton Meets Bilevel Optimization |
| 73 | 2025 | 4 | 0.231 | yes | When X Meets Y / X Meets Y |  | +39.8 | When Graph Neural Networks Meet Dynamic Mode Decomposition |
| 74 | 2025 | 4 | 0.231 | yes | When X Meets Y / X Meets Y |  | +39.3 | When GNNs meet symmetry in ILPs: an orbit-based feature augmentation approach |
| 75 | 2025 | 4 | 0.231 | no | X Is All You Need | yes | +40.2 | Random Is All You Need: Random Noise Injection on Feature Statistics for Generalizable Deep Image Denoising |
| 76 | 2025 | 2 | 0.147 | yes | When X Meets Y / X Meets Y |  | +39.7 | Newton Meets Marchenko-Pastur: Massively Parallel Second-Order Optimization with Hessian Sketching and Debiasing |
| 77 | 2025 | 2 | 0.147 | yes | X Matters | yes | +42.3 | The Journey Matters: Average Parameter Count over Pre-training Unifies Sparse and Dense Scaling Laws |
| 78 | 2023 | 2 | 0.046 | no | X Matters | yes | +41.6 | Data Continuity Matters: Improving Sequence Modeling with Lipschitz Regularizer |
| 79 | 2025 | 0 | 0.042 | yes | X Is All You Need | yes | +42.2 | Support is All You Need for Certified VAE Training |
| 80 | 2025 | 0 | 0.042 | no | X Is All You Need | yes | +43.0 | Exposure Bracketing Is All You Need For A High-Quality Image |
| 81 | 2025 | 0 | 0.042 | no | X Matters | yes | +41.7 | Autocorrelation Matters: Understanding the Role of Initialization Schemes for State Space Models |
| 82 | 2024 | 0 | 0.020 | no | X Is Secretly Y | yes | +42.3 | Lion Secretly Solves a Constrained Optimization: As Lyapunov Predicts |
| 83 | 2024 | 0 | 0.020 | no | X Is All You Need | yes | +42.8 | Maximum Likelihood Estimation is All You Need for Well-Specified Covariate Shift |

</details>

**Measure check.** All 83 matches are recognisable uses of a template. One is borderline: a pun on "meet", in "Variance Networks: When Expectation Does Not Meet Your Expectations". Recall was not validated. For example, "A Graph is Worth 1-bit Spikes" is caught only through its "When … Meets …" subtitle.

### (b) Artefact check: arXiv-id share by status

S2 sometimes keeps a venue record without an arXiv id separate from the arXiv record, and the arXiv record collects the citations (`qc_split_records.jsonl`). A different share of such records in one group would bias the comparison.

| | Meme | Other | Tentative | Other |
|---|---|---|---|---|
| Venue record has an arXiv id | **80.7%** (67/83; Wilson 71.0–87.8) | 76.8% | **73.2%** (366/500; 69.2–76.9) | 77.1% |
| 2017–21 | 78.6% (11/14) | 79.0% | 80.0% (80/100) | 78.9% |
| 2022–25 | 81.2% (56/69) | 76.2% | 71.5% (286/400) | 76.5% |
| Adjusted difference (LPM, primary controls and FE) | +5.1 pp (−3.2, +13.3), p 0.23 | | −3.0 pp (−7.1, +1.0), p 0.15 | |
| Zero citations | 6.0% (5/83) | 4.1% | 3.4% | 4.2% |
| Several S2 matches | 0% | 0.16% | 0.2% | 0.16% |

| Primary spec on … | G6a meme | G6b tentative |
|---|---|---|
| records with an arXiv id only | +37.7% (+6.0, +78.8), 67 meme | +4.1% (−8.3, +18.1), 366 tentative |
| records without an arXiv id only | +14.9% (−47.7, +152.4), 16 meme | +26.3% (−2.5, +63.6), 134 tentative |
| all records + arXiv-id indicator | +30.1% (+2.3, +65.3) | +7.4% (−3.7, +19.8) |
| difference between subsets (ratio; controls and FE interacted with arXiv status) | 0.84 (0.37, 1.88), p 0.66 | 1.21 (0.91, 1.62), p 0.20 |

- **Split-record QC sample.** 30 records were checked and 7 were split. The sample contains 1 meme record and 2 tentative records, none of them split, so it cannot speak to G6.

**Reading.**
- **Neither difference in arXiv-id share is distinguishable from zero.**
- **G6a.**
  - The estimate on records with an arXiv id alone (+37.7%) equals the primary, so the split-record artefact does not explain G6a.
  - Adding an arXiv-id indicator lowers G6a to +30%. Having an arXiv preprint goes with more citations, through the artefact or through real visibility, and meme papers have slightly more preprints.
- **G6b.** Tentative-title records have slightly fewer arXiv ids. If anything, that biases G6b downward: the estimate is +7.4% with the indicator.

### (c) Overlap with other title features, and paper type

**G6a and G2 ("assertive") overlap heavily.**
- G2's rule-based ASSERT regex matches "is", "are", "matters" and "need(s)". So most "X Is All You Need", "X Matters" and "X Is Secretly Y" titles are also G2: 42 of 83 meme titles (51%), against 4.9% of other titles.
- G2's own primary is +26% (Holm p 0.038).

| Variant (G6a) | % difference | 95% CI | p | n meme |
|---|---|---|---|---|
| Primary | +37.9% | +2.9, +84.8 | 0.037 | 83 |
| + G2 control | +25.5% | −7.4, +70.1 | 0.15 | 83 |
| + G1, G2, G3 controls | +25.5% | −7.3, +70.0 | 0.15 | 83 |
| within non-assertive titles (When X Meets Y, Do X Really, Free Lunch, …) | +65.7% | +21.6, +126.0 | 0.002 | 41 |
| within assertive titles (reference = other assertive titles; 381 papers in non-singleton cells) | +23.1% | −38.7, +147.0 | 0.56 | 42 |
| G2 coefficient with a G6a control (G2 primary: +26.1%) | +23.6% | +5.2, +45.2 | 0.013 | — |

**Reading.**
- About 30% of the G6a coefficient (in log points) is shared with G2: b falls from 0.321 to 0.227.
- The G6a association is not just G2 under another name. The non-assertive meme titles show a larger point estimate, and G2 barely changes when G6a is controlled.
- The within-subset estimates are post-hoc splits of small groups and are not findings.

**G6b and named titles (G1).**
- 66 of 500 tentative titles are named (13.2% vs 25.2%). Many have the form "NAME: Towards …".
- + G1 control: +5.3% (−6.4, +18.4).
- Within non-named titles: +6.7% (−5.4, +20.4), 434 tentative.
- Within named titles: −2.1% (−27.9, +32.9), 66 tentative.

**Paper type.**
- The method-paper indicator is set when the abstract says "we propose", "we introduce", "we present" or "this paper proposes" (regex from `g1.py`, crude and unvalidated).
- **Tentative framings mark analysis papers.** 56.0% of tentative-title abstracts announce a method, against 68.3% of others: adjusted −6.0 pp (−9.5, −2.5).
- **Meme titles:** 57.8% vs 67.7%, adjusted −7.3 pp (−18.3, +3.6).
- Adding the indicator leaves both estimates unchanged: G6a +38.1%, G6b +3.9%.

### (d) Power

| | G6a meme (n 83) | G6b tentative (n 500) |
|---|---|---|
| SE(b) | 0.149 | 0.060 |
| Minimum detectable effect, 80% power, α = 0.05 | +52.0% / −34.2% | +18.4% / −15.5% |
| Same at the Holm step α (0.01 for G6a; 0.05 for G6b) | +66.6% / −40.0% | +18.4% / −15.5% |
| Power for a true +10% / +20% at α = 0.05 | 10% / 23% | 35% / 86% |
| Power for a true +38% (the G6a point estimate) at the Holm step α | 34% | — |
| ±10% band attainable at this SE? | no (needs SE ≤ 0.051) | no (needs SE ≤ 0.051) |

**Reading.**
- **G6a.** Even if the true association were the observed +38%, the pre-registered test would reach Holm p < 0.05 only about a third of the time.
- **G6b.** It could detect about ±16–18% but not ±10%. Under 1/√n scaling, about 1.4 times as many tentative titles would be needed for its CI to fit inside the ±10% band at all.

### (e) Measure spot-check (G6b)

- **Random sample.** A seeded random sample of 20 tentative titles (`results.json`) contains only genuine tentative openers, for example "Understanding the failure modes of out-of-distribution generalization" and "Revisiting Link Prediction: a data perspective".
- **Most-cited.**
  - "Towards Deep Learning Models Resistant to Adversarial Attacks" (15,844 citations);
  - "Understanding deep learning requires rethinking generalization" (5,334);
  - "On the Convergence of FedAvg on Non-IID Data" (3,181);
  - "Rethinking Attention with Performers" (2,542).
- **Least-cited.** These are mostly 2023–24 theory and RL papers with 0–5 citations, for example "On the Convergence of the Monte Carlo Exploring Starts Algorithm for Reinforcement Learning".

### (f) Why R1 (matched pairs) differs from the primary

G4 found that the R1 procedure is shifted downward even when there is no association. We repeated its placebo here.
- **Method.** Draw 200 groups of random papers without the feature, with the same per-year counts as the real group, and match them with the R1 rule.
- **Reimplementation check.** Our reimplementation of the R1 pairing reproduces core R1 exactly for both features.

| | Observed R1 | Null mean (95% null range) | Placebo p | Placebo-adjusted R1 (approx. 95% CI) |
|---|---|---|---|---|
| G6a meme (83 pairs) | +18.0% | −22.0% (−49.2, +11.3) | 0.050 | +51.3% (+2.1, +124.2) |
| G6b tentative (497 pairs) | −13.1% | −22.2% (−33.6, −11.1) | 0.16 | +11.6% (−4.6, +30.7) |

**Mechanism.** The nearest-neighbour controls sit above their own year × topic50 cell mean for papers without the feature:
- G6a controls: +0.09 log points, against +0.36 for the meme papers;
- G6b controls: +0.15 log points, against +0.03 for the tentative papers.

**Reading.**
- **G6b.** Its negative R1 lies inside the null range, so it is what the procedure produces with no association. Calibrated, R1 has the same sign as the primary.
- **G6a.** The calibrated R1 is larger than the primary, and its approximate CI excludes zero.
- **The verdicts do not change.** The pre-registered rule uses raw R1, and both verdicts already fail on Holm p.

## Interpretation and caveats

- **Inconclusive, not null.**
  - **G6a.** Meme-template papers sit at a higher citation level in every pre-registered check (point estimates +18% to +44%) and in the within-year-percentile outcome (+7 points). Only aggressive one-sided drops of the 10 most-cited papers bring it near zero (+6% to +9%), and those are biased downward by construction. But the pre-registered test does not pass multiplicity correction (Holm p 0.183), and most robustness CIs include zero. The data are consistent with anything from no difference to substantially more citations.
  - **G6b.** Tentative framings are close to zero in the primary and in R3–R7 (−1% to +11%). The CI still reaches +17%, so a meaningful positive association is not ruled out, and the ±10% "no difference" verdict was not reachable with 500 titles.
- **Observational.**
  - Authors choose titles, and a meme title may go with confident, well-promoted, preprinted work. Meme papers have slightly more arXiv ids, and adding that indicator lowers G6a to +30%.
  - Content controls and matched pairs reduce but do not remove such differences. None of this shows that renaming a given paper "X Is All You Need" would change its citations.
- **Overlap with G2.** Half the meme titles are also "assertive" titles (G2), and about 30% of the G6a coefficient is shared with G2. G6a and G2 are not independent pieces of evidence.
- **Small, recent and heavy-tailed (G6a).**
  - 83 papers, 37% of them from 2025, which have only about 1 year of citations.
  - One paper holds 38% of all meme citations. It does not drive the log-scale estimate, but it does drive raw-count summaries and the nominal p = 0.037.
- **Outcome noise.** About 23% of venue records lack an arXiv id and may undercount citations. This is not clearly differential: +5.1 pp for meme and −3.0 pp for tentative, with both CIs including zero.
- **Measurement.**
  - The template regexes were spot-checked for precision: all 83 meme matches and a random 20 tentative matches are genuine.
  - Recall was not validated. Snowclone variants outside the listed patterns are counted as non-template titles.
- **Selection into the sample.**
  - Only accepted ICLR papers are included.
  - On the reviewer side, no title feature's association with acceptance survives the camera-ready audit (0 of 18 auditable features; `outputs/SUMMARY.md`). So selection on title style by reviewers is not evident. That does not rule out unmeasured quality differences among accepted papers.
- **Exposure.** The exposure is the camera-ready title as indexed; counts are a single S2 snapshot (2026-10-17).
- **Multiplicity.**
  - Secondary analyses and diagnostics carry no multiplicity correction.
  - The "Rethinking" estimate (+33%, p 0.028), the non-assertive meme subgroup (+66%) and the placebo-adjusted R1 for G6a are hypotheses for a future pre-registered test, not findings.

## One-sentence advice for authors (observational)

Among accepted ICLR papers with similar content, papers whose titles use a meme template ("X Is All You Need", "When X Meets Y", …) receive about 38% more citations on average (95% CI +3% to +85%), not significant after the pre-registered multiplicity correction (Holm p 0.18), and papers with tentative framings ("Towards", "Rethinking", "On the", …) receive about the same as others (+4%, −8% to +17%), so these data give no citation-based reason to adopt or avoid either style.
