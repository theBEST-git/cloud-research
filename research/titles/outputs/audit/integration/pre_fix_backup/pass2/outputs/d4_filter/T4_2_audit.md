# T4.2 Camera-ready audit: flip matrices and decision-stage tipping points

1311 arXiv pairs with a pre-decision v1 ({'accepted': 803, 'rejected': 508}). adds = absent in v1, present in the stored title; drops = the reverse; net = (adds - drops)/n. Pairs: WP4's frozen primary audit (original + complete enlargement, 2023-26). did_se and the DiD interval are WP4's pseudo-flip Wald (identical to the wp4_ columns from outputs/snapshot/T4_2_tipping_points.csv, 2026-10-11 21:43:21 UTC). auditable = WP4 rule (>= 10 v1-present titles per arm and measurable through arXiv). G_dec_identified / G_total_identified = uncorrected rule (tipping point beyond the 95% CI); wp4_p_holm_dec / wp4_passes_holm_dec = the multiplicity-controlled gate used for claims.

## Flip matrices (primary, all audit years)

| feature | n_acc | v1_present_acc | adds_acc | drops_acc | n_rej | v1_present_rej | adds_rej | drops_rej | net_acc | net_rej | did | did_se | auditable |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NAME | 803 | 256 | 20 | 16 | 508 | 155 | 4 | 9 | 0.0050 | -0.0098 | 0.0148 | 0.0108 | True |
| compound | 803 | 395 | 22 | 24 | 508 | 239 | 8 | 13 | -0.0025 | -0.0098 | 0.0074 | 0.0127 | True |
| phrase_colon | 803 | 139 | 12 | 18 | 508 | 84 | 7 | 7 | -0.0075 | 0.0000 | -0.0075 | 0.0105 | True |
| mixed_case_name | 803 | 167 | 10 | 11 | 508 | 96 | 4 | 13 | -0.0012 | -0.0177 | 0.0165 | 0.0104 | True |
| title_case | 803 | 755 | 9 | 15 | 508 | 475 | 5 | 17 | -0.0075 | -0.0236 | 0.0162 | 0.0115 | True |
| all_caps_title | 803 | 0 | 2 | 0 | 508 | 0 | 10 | 0 | 0.0025 | 0.0197 | -0.0172 | 0.0072 | False |
| sentence_case | 803 | 33 | 13 | 10 | 508 | 26 | 5 | 7 | 0.0037 | -0.0039 | 0.0077 | 0.0096 | True |
| question_opener | 803 | 17 | 1 | 2 | 508 | 14 | 1 | 1 | -0.0012 | 0.0000 | -0.0012 | 0.0048 | True |
| O_union | 803 | 46 | 16 | 10 | 508 | 39 | 14 | 7 | 0.0075 | 0.0138 | -0.0063 | 0.0115 | False |
| title_typo | 803 | 0 | 5 | 0 | 508 | 0 | 4 | 0 | 0.0062 | 0.0079 | -0.0016 | 0.0058 | False |
| R24 | 803 | 31 | 1 | 3 | 508 | 17 | 1 | 1 | -0.0025 | 0.0000 | -0.0025 | 0.0050 | True |
| R26 | 803 | 28 | 3 | 2 | 508 | 8 | 2 | 1 | 0.0012 | 0.0020 | -0.0007 | 0.0055 | False |
| L_title | 803 | 59 | 8 | 5 | 508 | 25 | 7 | 2 | 0.0037 | 0.0098 | -0.0061 | 0.0081 | False |
| NAME_strict | 803 | 245 | 20 | 15 | 508 | 152 | 4 | 11 | 0.0062 | -0.0138 | 0.0200 | 0.0110 | True |
| NAME_loose | 803 | 276 | 22 | 14 | 508 | 173 | 6 | 9 | 0.0100 | -0.0059 | 0.0159 | 0.0111 | True |
| allcaps_name | 803 | 66 | 12 | 7 | 508 | 46 | 6 | 3 | 0.0062 | 0.0059 | 0.0003 | 0.0086 | True |
| snowclone | 803 | 8 | 1 | 1 | 508 | 3 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0037 | False |
| llm_abbrev_only | 803 | 49 | 9 | 3 | 508 | 39 | 2 | 1 | 0.0075 | 0.0020 | 0.0055 | 0.0064 | True |

## Decision-stage bound (2024-26, year-standardised prevalences; DiD in pp)

| feature | auditable | P_s2 | P_s3 | G_dec_obs | did_pp | did_lo95_pp | did_hi95_pp | tip_dec_pp | G_dec_interval_lo | G_dec_interval_hi | G_dec_identified | G_total_obs | tip_total_pp | G_total_interval_lo | G_total_interval_hi | G_total_identified | wp4_did_lo_pp | wp4_did_hi_pp | wp4_G_total_lo | wp4_G_total_hi | wp4_p_holm_dec | wp4_passes_holm_dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NAME | True | 0.346 | 0.364 | 1.050 | 1.482 | -0.629 | 3.594 | 2.916 | 0.988 | 1.061 | False | 1.021 | 1.036 | 0.948 | 1.033 | False | -0.629 | 3.594 | 0.948 | 1.033 | 1.000 | 0.000 |
| compound | True | 0.523 | 0.543 | 1.037 | 0.735 | -1.762 | 3.232 | 3.241 | 1.000 | 1.056 | True | 1.018 | 1.349 | 0.975 | 1.041 | False | -1.762 | 3.232 | 0.975 | 1.041 | 0.695 | 0.000 |
| phrase_colon | True | 0.177 | 0.179 | 1.011 | -0.747 | -2.811 | 1.316 | 0.324 | 0.966 | 1.099 | False | 1.012 | 0.313 | 0.959 | 1.119 | False | -2.811 | 1.316 | 0.959 | 1.119 | 1.000 | 0.000 |
| mixed_case_name | True | 0.226 | 0.246 | 1.087 | 1.647 | -0.389 | 3.683 | 3.286 | 0.989 | 1.096 | False | 1.059 | 1.947 | 0.945 | 1.071 | False | -0.389 | 3.683 | 0.945 | 1.071 | 1.000 | 0.000 |
| title_case | True | 0.930 | 0.945 | 1.017 | 1.615 | -0.630 | 3.860 | 2.593 | 0.992 | 1.021 | False | 1.018 | 2.308 | 0.988 | 1.022 | False | -0.630 | 3.860 | 0.988 | 1.022 | 1.000 | 0.000 |
| all_caps_title | False | 0.011 | 0.005 | 0.435 | -1.719 | -3.127 | -0.312 | -1.036 | 0.646 | 1.530 | False | 0.361 | -1.195 | 0.559 | 1.609 | False | -3.127 | -0.312 | 0.559 | 1.609 |  | 0.000 |
| sentence_case | True | 0.042 | 0.037 | 0.868 | 0.767 | -1.116 | 2.651 | -0.935 | 0.320 | 1.023 | False | 0.905 | -0.543 | 0.309 | 1.093 | False | -1.116 | 2.651 | 0.309 | 1.093 | 0.702 | 0.000 |
| question_opener | True | 0.017 | 0.016 | 0.911 | -0.125 | -1.066 | 0.817 | -0.258 | 0.542 | 1.223 | False | 0.899 | -0.250 | 0.503 | 1.278 | False | -1.066 | 0.817 | 0.502 | 1.278 | 1.000 | 0.000 |
| O_union | False | 0.068 | 0.056 | 0.812 | -0.631 | -2.876 | 1.614 | -2.148 | 0.637 | 1.054 | False | 0.807 | -1.879 | 0.615 | 1.091 | False | -2.876 | 1.614 | 0.615 | 1.091 |  | 0.000 |
| title_typo | False | 0.007 | 0.007 | 0.975 | -0.165 | -1.303 | 0.973 | -0.029 | -1.041 | 1.629 | False | 0.936 | -0.065 | -0.714 | 1.797 | False | -1.303 | 0.973 | 0.000 | 1.797 |  | 0.000 |
| R24 | True | 0.048 | 0.043 | 0.896 | -0.249 | -1.222 | 0.724 | -0.828 | 0.792 | 1.045 | False | 0.807 | -1.446 | 0.698 | 0.972 | True | -1.222 | 0.724 | 0.698 | 0.972 | 1.000 | 0.000 |
| R26 | False | 0.034 | 0.038 | 1.093 | -0.072 | -1.146 | 1.001 | 0.539 | 0.909 | 1.258 | False | 1.060 | 0.301 | 0.848 | 1.263 | False | -1.146 | 1.002 | 0.848 | 1.262 |  | 0.000 |
| L_title | False | 0.087 | 0.085 | 0.980 | -0.611 | -2.194 | 0.972 | -0.291 | 0.909 | 1.119 | False | 0.915 | -1.118 | 0.837 | 1.076 | False | -2.194 | 0.972 | 0.837 | 1.076 |  | 0.000 |
| NAME_strict | True | 0.336 | 0.354 | 1.053 | 2.001 | -0.165 | 4.166 | 2.987 | 0.978 | 1.056 | False | 1.023 | 1.133 | 0.936 | 1.026 | False | -0.165 | 4.166 | 0.936 | 1.026 | 1.000 | 0.000 |
| NAME_loose | True | 0.369 | 0.387 | 1.050 | 1.587 | -0.594 | 3.768 | 3.061 | 0.988 | 1.059 | False | 1.022 | 1.191 | 0.950 | 1.033 | False | -0.594 | 3.768 | 0.951 | 1.033 | 1.000 | 0.000 |
| allcaps_name | True | 0.102 | 0.099 | 0.966 | 0.032 | -1.661 | 1.725 | -0.587 | 0.855 | 1.059 | False | 0.922 | -1.181 | 0.799 | 1.030 | False | -1.661 | 1.725 | 0.799 | 1.030 | 1.000 | 0.000 |
| snowclone | False | 0.010 | 0.010 | 0.941 | 0.000 | -0.730 | 0.730 | -0.102 | 0.334 | 1.281 | False | 0.908 | -0.141 | 0.288 | 1.321 | False |  |  |  |  |  |  |
| llm_abbrev_only | True | 0.092 | 0.095 | 1.036 | 0.550 | -0.701 | 1.802 | 0.552 | 0.912 | 1.079 | False | 1.026 | 0.344 | 0.882 | 1.078 | False | -0.701 | 1.802 | 0.882 | 1.078 | 1.000 | 0.000 |
