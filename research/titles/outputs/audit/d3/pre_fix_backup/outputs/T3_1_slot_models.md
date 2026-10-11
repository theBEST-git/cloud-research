| Block | Row | Estimate (OR [95% CI] or pp) | one-sided p | BH q | n | n post |
|---|---|---|---|---|---|---|
| A. Primary (logit, 2018-26, slot FE + slot trends + llm_topic) | Pooled LLM slots: post-2024 level shift | 2.18 [1.41, 3.38] | 0.000237 |  | 1,922 | 1,508 |
| A. Primary (logit, 2018-26, slot FE + slot trends + llm_topic) | Pooled control pairs: post-2024 level shift | 0.87 [0.64, 1.18] | 0.818 |  | 6,925 | 5,087 |
| A. Primary (logit, 2018-26, slot FE + slot trends + llm_topic) | Stacked: post x LLM-slot (slot minus control) | 2.55 [1.53, 4.25] | 0.000165 |  | 8,847 | 6,595 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | S-improve | 2.63 [1.39, 4.97] | 0.00146 | 0.00583 | 979 | 795 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | S-reveal | 1.93 [0.74, 5.00] | 0.0886 | 0.177 | 511 | 350 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | S-exploit | 1.80 [0.55, 5.94] | 0.167 | 0.222 | 321 | 258 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | S-study-adj | -13.2 pp [-72.0, +45.6] | 0.67 | 0.67 | 111 | 105 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | towards/toward | 1.69 [0.82, 3.47] | 0.0771 | 0.179 | 1,250 | 949 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | novel/new | 1.58 [0.74, 3.36] | 0.119 | 0.179 | 392 | 274 |
| B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles) | via/using | 0.75 [0.53, 1.06] | 0.949 | 0.949 | 5,283 | 3,864 |
| C. Year-level (REML meta-regression on slot x year cells, group-year shocks) | slots_post | 2.76 [1.26, 6.03] | 0.00951 |  | 29 |  |
| C. Year-level (REML meta-regression on slot x year cells, group-year shocks) | controls_post | 1.02 [0.49, 2.14] | 0.473 |  | 26 |  |
| C. Year-level (REML meta-regression on slot x year cells, group-year shocks) | stacked_interaction | 2.97 [1.02, 8.62] | 0.023 |  | 55 |  |
| D. Robustness | topic100 FE: slots_post | 2.28 [1.40, 3.74] | 0.000503 |  | 1,886 | 1,487 |
| D. Robustness | topic100 FE: controls_post | 0.93 [0.68, 1.25] | 0.69 |  | 6,925 | 5,087 |
| D. Robustness | topic100 FE: stacked_interaction | 2.65 [1.54, 4.56] | 0.000217 |  | 8,847 | 6,595 |
| D. Robustness | NA pool (camera-ready-free): slots_post | 2.18 [1.28, 3.70] | 0.00198 |  | 1,406 | 1,110 |
| D. Robustness | NA pool (camera-ready-free): controls_post | 0.85 [0.60, 1.20] | 0.827 |  | 4,958 | 3,650 |
| D. Robustness | NA pool (camera-ready-free): stacked_interaction | 2.57 [1.40, 4.71] | 0.00113 |  | 6,364 | 4,760 |
| D. Robustness | non-LLM subset: slots_post | 2.59 [1.57, 4.28] | 9.61e-05 |  | 1,146 | 763 |
| D. Robustness | non-LLM subset: controls_post | 0.88 [0.63, 1.22] | 0.785 |  | 4,785 | 3,065 |
| D. Robustness | non-LLM subset: stacked_interaction | 2.96 [1.64, 5.34] | 0.00016 |  | 5,931 | 3,828 |
| D. Robustness | exclude titles whose abstract has the slot word: slots_post | 1.94 [1.03, 3.69] | 0.0208 |  | 913 | 737 |
| D. Robustness | exclude titles whose abstract has the slot word: controls_post | 0.87 [0.64, 1.18] | 0.818 |  | 6,925 | 5,087 |
| D. Robustness | exclude titles whose abstract has the slot word: stacked_interaction | 2.26 [1.13, 4.54] | 0.0109 |  | 7,838 | 5,824 |
| D. Robustness | any-compound-lead opener rule (pilot-like): slots_post | 2.49 [1.66, 3.74] | 4.99e-06 |  | 2,163 | 1,702 |
| D. Robustness | any-compound-lead opener rule (pilot-like): controls_post | 0.87 [0.64, 1.18] | 0.818 |  | 6,925 | 5,087 |
| D. Robustness | any-compound-lead opener rule (pilot-like): stacked_interaction | 2.91 [1.81, 4.69] | 5.79e-06 |  | 9,088 | 6,789 |
| D. Robustness | excluding 2026: slots_post | 2.27 [1.36, 3.80] | 0.0009 |  | 1,250 | 836 |
| D. Robustness | excluding 2026: controls_post | 1.00 [0.75, 1.35] | 0.494 |  | 4,207 | 2,369 |
| D. Robustness | excluding 2026: stacked_interaction | 2.42 [1.34, 4.37] | 0.00171 |  | 5,457 | 3,205 |
| D. Robustness | 2024-only post (2018-2024): slots_post | 2.38 [1.39, 4.07] | 0.000762 |  | 732 | 318 |
| D. Robustness | 2024-only post (2018-2024): controls_post | 0.98 [0.74, 1.32] | 0.541 |  | 2,774 | 936 |
| D. Robustness | 2024-only post (2018-2024): stacked_interaction | 2.62 [1.44, 4.79] | 0.00083 |  | 3,506 | 1,254 |
| D. Robustness | stacked with year FE: stacked_interaction | 3.16 [1.90, 5.25] | 4.45e-06 |  | 8,847 |  |
| D. Robustness | LPM: slots_post | +16.7 pp [+8.7, +24.7] | 2.07e-05 |  | 1,922 |  |
| D. Robustness | LPM: controls_post | -3.1 pp [-8.2, +2.1] | 0.878 |  | 6,925 |  |
| D. Robustness | LPM: stacked_interaction | +20.3 pp [+11.1, +29.5] | 7.95e-06 |  | 8,847 |  |
