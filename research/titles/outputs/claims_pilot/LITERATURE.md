# Literature check: claim strength and overreach (2026-10-13)

Compiled by a literature agent; the two closest works were re-verified by direct search.

## Closest prior work (verified)
- **Qiu, Chen & Li (2025), "Counterfactual LLM-based Framework for Measuring Rhetorical Style", arXiv:2512.19908.** 8,485 ICLR submissions 2017-2025; LLM personas rewrite the same content in different styles, pairwise LLM judging + Bradley-Terry gives a rhetorical-strength score. Rhetorical strength rises sharply after 2023 (linked to LLM writing help); visionary framing predicts citations and media attention controlling for peer-review evaluations. Agent reports near-zero correlation with mean reviewer score (rho = -0.015; not re-verified). No titles, no decisions/withdrawals, no evidence-relative overreach.
- **RIGOURATE (ACL Findings 2026), arXiv:2601.04350.** Evidence-aligned overstatement scores: claims in abstracts/introductions vs evidence retrieved from the paper body; >10K claim-evidence sets from ICLR/NeurIPS papers; eight LLM annotators calibrated against review comments, human evaluation. No trend or acceptance analysis.

## Other key works (agent-reported)
Sumner et al. 2014 BMJ (7-level causal strength, kappa 0.88); Yu, Li & Wang 2019 EMNLP (4-level claim strength, kappa 0.98); Yu et al. 2020 COLING (press-release exaggeration 22%); Wright & Augenstein 2021 (downplays/same/exaggerates; direct pair classification F1 ~0.47); Pei & Jurgens 2021 (6-pt certainty, alpha 0.67); Wuhrl et al. 2024 (multi-dimension distortion, low agreement when coded jointly); Boutron et al. 2010 JAMA (spin in 18% of titles vs 58% of abstract conclusions, kappa 0.47-0.64); Haber et al. 2022 (within-abstract recommendation vs finding gap); Millar et al. 2022 (hype adjectives, kappa ~0.8); Peng et al. 2024 PNAS (promotional language and funding); Kang et al. 2018 PeerRead ("state of the art" predicts ICLR 2017 acceptance); Jung et al. 2025 arXiv:2509.25701 (readability/tone vs ICLR acceptance); Oh 2026 arXiv:2605.17273 (SOTA claims in accepted AI abstracts). Methods: PPI (arXiv:2301.09633), DSL (arXiv:2306.04746), Ludwig et al. 2024, Gligoric et al. 2025, "LLM hacking" arXiv:2509.08825 (model/prompt choice flips ~31% of conclusions), Peters & Chin-Yee arXiv:2504.00025 (LLMs overgeneralise).

## Implications for our study
1. Abstract-level rhetoric vs review outcome is partly answered (Qiu et al.: ~null vs reviewer score). New: titles; title-vs-abstract gap; overreach relative to reported evidence (not style); decisions incl. withdrawals; overreach types.
2. Codebook: separate dimensions, directional comparison (understated / matched / over), list evidence first then judge claims, keep lexical hype separate from overreach, oversample likely cases with known probabilities for PPI/DSL.
3. Realistic human agreement for spin/overreach: kappa 0.47-0.64. Our LLM-LLM kappas (0.73-0.85) are likely inflated by shared model biases; the human gold set and a second model family are needed.
4. Risk: LLMs overgeneralise, so LLM annotators may under-detect scope overreach.
