# Claim strength and rhetorical overreach in ML paper titles and abstracts — codebook v0 (pilot)

You see the TITLE and ABSTRACT of a machine-learning paper. Judge only what is written. Do not use outside knowledge about the paper, its authors, whether its claims are true, or its later impact. All examples below are invented.

## Q0. Contribution type (one)
`method` (proposes a model, algorithm or training procedure) · `empirical` (analysis or study of existing methods/phenomena) · `theory` (main results are theorems/proofs) · `resource` (dataset, benchmark, tool) · `position` (argument, perspective, survey) · `other`.

## Q1. Title claim strength (0–3)
- **0 — no claim.** Names or describes a method, task, dataset or topic. Includes "NAME: description" titles and neutral noun phrases ("A Graph Approach to Protein Folding").
- **1 — implicit or tentative claim.** Evaluative attributes of the proposed work inside a noun phrase ("Fast and Robust Sparse Attention"), questions ("Can Small Models Plan?"), exploratory framings ("Towards…", "Rethinking…", "Understanding…", "On the…").
- **2 — explicit, specific claim.** A sentence or verb phrase asserting a result within a stated setting ("Sparse Attention Reduces Memory in Long-Context Translation").
- **3 — strong or general claim.** Universal, absolute, superlative or sufficiency claims ("Attention Is All You Need for X", "Solving Y", "Any Z Can…", "X Always Helps", "Universal…", "Optimal…", "…Is Secretly…", "No Need for…").

## Q2. Abstract main-claim strength (1–3)
First identify the main claim: the central result the authors assert about their contribution.
- **1 — cautious.** Hedged ("may", "suggests", "preliminary"), explicitly narrow, or mainly descriptive.
- **2 — definite but qualified.** Asserts the result with a stated scope (named benchmarks, settings, assumptions) or with numbers.
- **3 — strong.** Universal, absolute or superlative language ("significantly outperforms all existing methods", "state-of-the-art across all tasks", "solves", "dramatically"), or generalisation beyond the stated scope.

## Q3a. Title overreach (none / mild / clear / NA)
Compare the title with what the abstract reports. Does the title promise more than the abstract delivers? NA if Q1 = 0.
- **none** — the abstract supports the title as stated.
- **mild** — the title is somewhat broader, stronger or more certain than the abstract's evidence (e.g., title says "for Language Models" but the abstract tests one model family on one task).
- **clear** — the title asserts something the abstract plainly does not support (e.g., title says "Solves Reasoning", abstract reports gains on two arithmetic benchmarks).

## Q3b. Abstract overreach (none / mild / clear)
Compare the abstract's claims with the evidence the abstract itself reports (benchmarks, datasets, number and kind of settings, theoretical assumptions, numbers).
- **none** — claims stay within the reported evidence.
- **mild** — some claims are stated more broadly or more strongly than the reported evidence.
- **clear** — the central claim plainly exceeds the reported evidence.

## Q4. Overreach types (multi-select; only if Q3a or Q3b is mild/clear; prefix t: for title, a: for abstract)
`scope` (generalises beyond tested settings) · `certainty` (definitive wording without support) · `magnitude` (superlatives, "significantly"/"dramatically" without quantification or beyond the numbers) · `novelty` (sweeping, unqualified "first"/"novel paradigm" claims) · `causal` (mechanism or cause asserted without stated evidence).

## Decision rules
1. Absence of numbers alone is not overreach. Overreach needs a claim that goes beyond the stated scope or evidence.
2. "State-of-the-art on [named benchmarks]" is not overreach; "state-of-the-art across tasks" with two benchmarks is scope overreach.
3. Theorems: a strong claim backed by a stated theorem is not overreach unless the claim drops the theorem's stated assumptions.
4. Resource papers: "comprehensive", "the first benchmark for X" — mark novelty/magnitude only if sweeping and unqualified.
5. When torn between two adjacent levels, choose the lower one and give confidence ≤ 3.

## Output per item
`{"item_id", "type", "title_strength", "abstract_strength", "title_overreach", "abstract_overreach", "types": [..], "main_claim" (≤ 20 words), "evidence" (≤ 20 words), "rationale" (≤ 25 words), "confidence" (1–5)}`
