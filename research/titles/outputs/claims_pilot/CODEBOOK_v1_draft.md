# Claim strength and rhetorical overreach — codebook v1 (draft, after pilot round 1)

Changes from v0 are driven by round-1 agreement (`round1_agreement.json`), the 20 disagreements and the four annotators' ambiguity reports. Pending: literature check (may add categories from established schemes).

## Q0. Contribution type (one)
As v0. **Tie-break:** follow the title's emphasis; if the title is neutral, the first contribution stated in the abstract.

## Q1. Title claim strength (0–3)
Strength is about what the title **asserts** (its predicate), not which words it contains.
- **0 — no claim.** Names or describes a method, task, dataset or topic. Gerunds of activity verbs ("Learning to…", "Tackling…", "Leveraging…") are 0.
- **1 — implicit or tentative.** Evaluative attributes inside a noun phrase, anywhere in the title incl. a NAME: subtitle ("Robust…", "Universal…", "Optimal…", "Fast and Easy…") unless the word is part of a fixed method or task name; gerunds of outcome verbs ("Improving…", "Boosting…", "Accelerating…"); questions; exploratory framings ("Towards", "Rethinking", "Understanding", "On the…").
- **2 — explicit claim.** A sentence, verb phrase or prescriptive imperative asserting a result or recommendation ("X Improves Y", "Transformers are Sample-Efficient World Models", "Attend Pixel, not Channel"). Generic subjects without a stated setting are still 2; breadth is handled in Q3a.
- **3 — strong or general claim.** The predicate asserts sufficiency, necessity, impossibility, universality, optimality or solution ("…Is All You Need", "…Suffices", "…Is Not Necessary", "…But Not Both", "Solving Y", "Any Z Can…", "Can't Hide…"). Applies to scoped theorems too; whether it overreaches is Q3a.

## Q2. Abstract claim language (checklist replaces the 1–3 scale, which put ~86% of abstracts at 2)
Mark each that is present anywhere in the abstract:
- `hedge` — epistemic hedges on a result claim (may, might, suggest, indicate, preliminary, in some cases).
- `booster` — intensifiers on a result claim (significantly, substantially, dramatically, remarkably, overwhelming, greatly).
- `superlative` — best/state-of-the-art/outperforms all/first/largest/unprecedented.
- `universal` — universal quantifiers or generality claims (all, any, always, across tasks/domains, general, universal).
- `quantified` — at least one number for a result (%, x-fold, absolute score).
- `scoped` — names the benchmarks, datasets, models or settings of the evaluation (or states theorem assumptions).
Derived strength (for analysis, not annotated): (booster + superlative + universal) − hedge.

## Q3a. Title overreach (none / mild / clear / NA)
As v0, plus: **clear** also when the abstract contradicts the title, or reports no evidence for the title's claim. "Why X" titles: mild t:causal if the abstract only hypothesises a cause; none if it reports analysis supporting it.

## Q3b. Abstract overreach (none / mild / clear)
Any claim in the abstract counts, main or secondary. **mild** — some claim (incl. a concluding or motivating sentence) goes beyond the reported evidence. **clear** — the central claim does, or the abstract asserts results it does not report at all.

## Q4. Overreach types (multi-select; t: title, a: abstract)
`scope`, `certainty`, `novelty`, `causal` as v0; `unsupported` (new: claim with no reported evidence or contradicted). **`magnitude` (redefined):** an intensifier or superlative is overreach only if it exceeds the reported numbers ("overwhelming" for +3%) or compares more broadly than the evaluation ("outperforms all existing methods" with two baselines). An unquantified "significantly" with named benchmarks is **not** overreach (it is recorded as `booster` in Q2).

## Decision rules
1. Judge only what is written; no outside knowledge.
2. Words that are part of a fixed method or task name ("Block-wise Optimal Float", "Count Everything" as a task) do not count as claims.
3. When torn between adjacent levels choose the lower one, confidence ≤ 3.
