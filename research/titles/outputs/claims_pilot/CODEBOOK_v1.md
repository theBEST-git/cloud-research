# Claim strength and rhetorical overreach in ML paper titles and abstracts — codebook v1.1

You are annotating the TITLE and ABSTRACT of machine-learning papers submitted to a conference. Judge only what is written. Do not use outside knowledge about the paper, its authors, whether its claims are true, or what happened to it later. Do not search the web. Do not write or run code to annotate: read every item yourself. All examples below are invented.

Work through the steps **in order** for each item.

**Core principle: one anchor for both judgements.** The title (Step 4) and the abstract's claims (Step 6) are each judged against the same anchor: the *evidence* the abstract reports (Step 2). Claims are not evidence. If the abstract repeats or amplifies the title's claim without reporting evidence for it, that does not make the title "matched": both the title and the abstract then overreach.

## Step 1 — Contribution type (one)
`method` (proposes a model, algorithm or training procedure) · `empirical` (studies existing methods or phenomena) · `theory` (main results are theorems) · `resource` (dataset, benchmark, tool) · `position` (argument, perspective, survey) · `other`.
Tie-break for mixed papers: follow the title's emphasis; if the title is neutral, use the first contribution the abstract states.

## Step 2 — Evidence list
List, in a few short phrases, the evidence the abstract itself reports for its claims: named benchmarks/datasets/tasks, models or baselines compared, settings, numbers, theorem assumptions, human studies. Write "none reported" if the abstract reports no evidence. You will judge claims against this list only.

## Step 3 — Title claim strength (0–3)
Score what the title **asserts** (its predicate), not which words it contains.
- **0 — no claim.** Names or describes a method, task, dataset or topic ("A Graph Approach to Protein Folding", "NAME: Sparse Attention for Long Documents"). Gerunds of activity verbs ("Learning to…", "Tackling…", "Leveraging…") are 0.
- **1 — implicit or tentative claim.** Evaluative attributes inside a noun phrase, anywhere in the title including after a colon ("Robust…", "Universal…", "Optimal…", "Fast and Easy…"); gerunds of outcome verbs ("Improving…", "Boosting…", "Accelerating…"); questions ("Can Small Models Plan?"); exploratory framings ("Towards…", "Rethinking…", "Understanding…", "On the…").
- **2 — explicit claim.** A sentence, verb phrase or prescriptive imperative that asserts a result or recommendation ("Sparse Attention Reduces Memory in Translation", "Small Models Are Strong Planners", "Prune Heads, Not Layers"). A generic subject with no stated setting is still 2; breadth is judged in Step 4.
- **3 — strong or general claim.** The predicate asserts sufficiency, necessity, impossibility, universality, optimality or a solution ("…Is All You Need", "…Suffices", "…Is Not Necessary", "…But Not Both", "Solving…", "Any Model Can…", "…Always Helps"). Applies to scoped theorems too; whether it overreaches is judged in Step 4.
Words that are part of a fixed method or task name (e.g., a method called "Optimal-Float", the task "count everything") are not claims.

## Step 4 — Title versus evidence
Compare what the title claims with the evidence list from Step 2 only. Do not count the abstract's own claims as support. NA if Step 3 = 0.
- **understated** — the title claims clearly less than the reported evidence supports (e.g., a question title whose answer the evidence establishes firmly and broadly).
- **matched** — the reported evidence supports the title as stated.
- **mild** — the title is somewhat broader, stronger or more certain than the abstract's evidence (e.g., title "…for Language Models"; abstract tests one model family on one task).
- **clear** — the title asserts something the reported evidence plainly does not support, that the abstract contradicts, or for which the abstract reports no evidence (even if the abstract restates the claim).

## Step 5 — Abstract language checklist (mark each 1 if present anywhere in the abstract, else 0)
- `hedge` — epistemic hedges on a result claim (may, might, suggest, indicate, preliminary, in some cases).
- `booster` — intensifiers on a result claim (significantly, substantially, dramatically, remarkably, greatly). Do not count "statistically significant" with a test.
- `superlative` — best, state-of-the-art, outperforms all, first, largest, unprecedented.
- `universal` — universal quantifiers or generality claims (all, any, always, across tasks/domains, general-purpose, universal).
- `quantified` — at least one number for a result (%, x-fold, absolute score, bound).
- `scoped` — names the benchmarks, datasets, models or settings evaluated, or states theorem assumptions.

## Step 6 — Abstract overreach (none / mild / clear)
Compare every claim in the abstract (main, secondary, concluding or motivating) with the evidence list from Step 2. Judge this independently of Step 4: the title and the abstract can both overreach.
- **none** — all claims stay within the reported evidence.
- **mild** — some claim is stated more broadly or more strongly than the reported evidence.
- **clear** — the central claim plainly exceeds the reported evidence, or the abstract asserts results it does not report at all.

## Step 7 — Overreach types (only for mild/clear in Step 4 or Step 6; prefix `t:` for title, `a:` for abstract; multi-select)
- `scope` — generalises beyond the tested settings (tasks, models, data, languages, domains).
- `certainty` — definitive wording where the evidence is partial or mixed.
- `magnitude` — an intensifier or superlative that exceeds the reported numbers ("overwhelming" for +3%) or compares more broadly than the evaluation ("outperforms all methods" with two baselines). An unquantified "significantly" with named benchmarks is **not** overreach (it is only a `booster` in Step 5).
- `novelty` — sweeping, unqualified priority claims ("the first ever…", "a new paradigm").
- `causal` — a cause or mechanism asserted without reported evidence for it (e.g., "Why X Works" when the abstract only hypothesises).
- `unsupported` — a claim with no reported evidence at all, or contradicted by the abstract.

## Decision rules
1. Absence of numbers alone is never overreach.
2. "State-of-the-art on [named benchmarks]" is not overreach; "state-of-the-art across tasks" with two benchmarks is `scope`.
3. A strong claim backed by a stated theorem is not overreach unless it drops the theorem's stated assumptions.
4. When torn between two adjacent levels, choose the lower one and give confidence ≤ 3.

## Output (one JSON object per item, one per line, no other text)
{"item_id": "...", "type": "method", "evidence": "≤ 25 words", "title_strength": 0, "title_vs_evidence": "NA|understated|matched|mild|clear", "hedge": 0, "booster": 0, "superlative": 0, "universal": 0, "quantified": 0, "scoped": 0, "abstract_overreach": "none|mild|clear", "types": ["t:scope", "a:magnitude"], "rationale": "≤ 30 words", "confidence": 1}
Use integers for strengths, flags and confidence (1 = guess … 5 = certain). `types` is [] when nothing is mild/clear.
