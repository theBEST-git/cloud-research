# Idea-twin labelling rubric (v1, pilot)

You see two ML paper abstracts, A and B, submitted to the same conference cycle by different teams. Coined method names are masked as [NAME]. Judge only the research contribution described; ignore writing style.

Labels:
- **T — same idea (twin).** The core contribution is essentially the same: the same specific problem AND the same key mechanism or insight, such that each paper would count as "concurrent work" that substantially anticipates the other's main claim. Differences in experiments, scale, extensions or framing are allowed. Examples: two papers that independently propose regressing a vector field along straight probability paths for generative modelling; two papers that independently show that the same specific defense is broken by the same attack.
- **P — same problem, different idea.** Same specific task or research question, but the core method, mechanism or finding differs materially (e.g., both target KV-cache compression for long-context LLMs, one by quantization, the other by token eviction).
- **R — related only.** Same broad area or subfield, but different specific problems.
- **U — cannot tell.** Abstracts too vague to decide between T and P.

Decision rules:
1. Ask: "If both were published, would a careful reviewer of B say A already contains B's main idea?" If yes → T.
2. Same benchmark or same application alone is not T. Same general technique applied to different problems is not T.
3. Use T sparingly; when torn between T and P, choose P and give confidence ≤ 3.

For each pair output: label, confidence (1–5), the shared core in ≤ 15 words (for T/P), and the key difference in ≤ 15 words (for P/R).
