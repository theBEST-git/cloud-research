# Human calibration decisions (PI, 2026-10-13)

Seven contested cases from gold block 1 (codebook v1.3), shown without model labels; the PI answered yes/no on overreach.

| # | Item | Case | Decision | Claude (both) | ChatGPT |
|---|---|---|---|---|---|
| 1 | g_033 | design rationale "can reduce the variance", no results | overreach | no | yes |
| 2 | g_019 | "models trained to backtrack are consistently safer", one model reported | overreach | no | yes |
| 3 | g_042 | "eliminates the problem of choosing a correct kernel", small accuracy gains | overreach | no | yes |
| 4 | g_005 | "can generalize across agent architectures and LLM backbones", none named | overreach | no | yes |
| 5 | g_021 | "the first benchmark ... specifically in computer architecture" | not overreach | no | yes |
| 6 | g_049 | title "Bandwidth Enables Generalization", abstract restricts to well-aligned targets | overreach | no | yes |
| 7 | g_029 | "Vision Transformers Need Registers"; "fixes that problem entirely" (check case) | overreach | yes | yes |

Result: the PI's standard matches ChatGPT on 6/7 and Claude on 2/7 of these contested cases; the check case (all agree) is confirmed. Encoded as rules H1-H7 in CODEBOOK_v1_4.md (Step 6b).
