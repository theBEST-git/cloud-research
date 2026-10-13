# Claim strength and rhetorical overreach in ML paper titles and abstracts — codebook v1.4 (calibrated on human decisions)

You are annotating the TITLE and ABSTRACT of machine-learning papers submitted to a conference. Judge only what is written. Do not use outside knowledge about the paper, its authors, whether its claims are true, or what happened to it later. Do not search the web. Do not write or run code to annotate: read every item yourself. All examples below are invented.

Work through the steps **in order** for each item.

**Core principle 1 — one anchor.** The title (Step 4) and the abstract (Step 6) are each judged against the same anchor: the *evidence* the abstract reports for the paper's own work (Step 2). Claims are not evidence. If the abstract repeats or amplifies the title's claim without evidence for it, the title is not "matched": both overreach.

**Core principle 2 — own contribution only.** Judge claims the paper makes about **its own** contribution, method, findings or results. Statements about prior work, the field or the problem's background ("existing methods fail to…", "LLMs are widely used…") are context: they are not scored in Steps 5–7, even if unsupported.

## Step 1 — Contribution type (one)
`method` (proposes a model, algorithm or training procedure) · `empirical` (studies existing methods or phenomena) · `theory` (main results are theorems) · `resource` (dataset, benchmark, tool) · `position` (argument, perspective, survey) · `other`.
Tie-break for mixed papers: follow the title's emphasis; if the title is neutral, use the first contribution the abstract states.

## Step 2 — Evidence list
List, in short phrases, the evidence the abstract reports for the paper's own claims: named benchmarks/datasets/tasks, models or baselines compared, settings, numbers, theorem statements and assumptions, ablations, human studies. Unnamed evidence ("extensive experiments on several benchmarks") is listed as **"unspecified experiments"**. Write "none reported" if there is no evidence at all.
How much unspecified experiments support: they support the *direction* of a result ("improves", "outperforms the baseline") but not its *breadth* ("across diverse tasks"), *magnitude* ("substantially", "state-of-the-art") or *generality*.

## Step 3 — Title claim strength (0–3)
Score what the title **asserts**. For idioms, puns or metaphors, first paraphrase the intended assertion in plain words, then score the paraphrase.
- **0 — no claim.** Names or describes a method, task, dataset or topic ("A Graph Approach to Protein Folding", "NAME: Sparse Attention for Long Documents"). Gerunds of activity verbs ("Learning to…", "Tackling…", "Leveraging…", "Exploring…"), their imperative forms ("Learn to Solve…", "Learn from…") and neutral nominalisations ("Average-Case Acceleration") are 0.
- **1 — implicit or tentative claim.** Evaluative attributes inside a noun phrase, anywhere in the title incl. after a colon ("Robust…", "Flexible…", "Universal…", "Optimal…"); gerunds of outcome verbs ("Improving…", "Boosting…", "Optimizing…") and their imperative forms that describe what the method does ("Improve X with Y"); purpose infinitives ("…to Improve X"); questions; exploratory framings ("Towards…", "Rethinking…", "Understanding…", "On the…", "When does X…"); hedged sentences ("X Is a Possible Y", "You May Need X").
- **2 — explicit claim.** An unhedged sentence or verb phrase asserting a result, or a prescriptive/contrastive imperative that recommends a practice ("Sparse Attention Reduces Memory in Translation", "Diffusion Models Are Few-Shot Learners", "Prune Heads, Not Layers", "Don't Do X").
- **3 — strong or general claim.** The asserted predicate is sufficiency, necessity, impossibility, universality, optimality or a solution ("…Is All You Need", "…Suffices", "X Needs Y", "…Is Not Necessary", "…But Not Both", "Solving…", "Overcoming…", "Eliminating…", "Any Model Can…", "All Roads Lead to X", "The Best Defense Is…"). Tentative forms ("Towards Overcoming…") are 1. Applies to scoped theorems too; a negated universal ("X Is Not Necessary") is supported by a single reported counterexample.
Words that are part of a fixed method or task name (a method called "Optimal-Float", the task "count everything") are not claims.

## Step 4 — Title versus evidence (NA if Step 3 = 0)
Compare the title's assertion with the evidence list only. Default is **matched**; when torn between matched and another level, choose matched.
- **understated** — a tentative title (question, "Towards…") whose answer the evidence establishes firmly and broadly.
- **matched** — the evidence supports the title as stated.
- **mild** — the title is broader, stronger or more certain than the evidence. Apply these rules:
  - *Class generalisation:* the title's subject is a class (e.g., "Diffusion Models", "Language Models", "Transformers", "DNN training") but the evidence covers one instance, one model family member, or one dataset → mild `scope`. Evidence spanning several instances of the class → matched.
  - *Evaluative attribute:* the title claims an attribute ("Flexible…", "Robust…", "Efficient…", "Fast…", "…for DNN Training") for a broader setting than the one tested (e.g., only CNNs on CIFAR-10) → mild `scope`. An attribute that the design makes plausible but the abstract never measures or demonstrates → mild `unsupported`.
  - *Theorems:* the title states a theorem's conclusion while dropping a condition the abstract states as necessary → mild `scope`.
  - *Strength 3 titles:* a sufficiency/solution/optimality claim backed only by improvements over baselines → mild `certainty`.
- **clear** — the abstract contradicts the title, or reports no evidence at all for it.

## Step 5 — Abstract language checklist (own-contribution statements only; 1 if present, else 0)
- `hedge` — epistemic hedges on the paper's own results (may, might, suggest, indicate, preliminary, in some cases). Ability modals ("can") and frequency adverbs ("often") are not hedges.
- `booster` — intensifiers on own results (significantly, substantially, dramatically, remarkably, greatly). "Statistically significant" with a stated test is not a booster.
- `superlative` — own results claimed to be best or to reach/beat the state of the art ("achieves state-of-the-art", "outperforms state-of-the-art methods", "outperforms all baselines", "first", "largest", "unprecedented", "optimal"/"minimax-optimal" results). Naming state-of-the-art models only as things that were evaluated ("we test four state-of-the-art LLMs") does not count; "outperforms existing/baseline methods" without a best/SOTA claim does not count.
- `universal` — claims that the own method or finding holds **beyond the evaluated items** ("general-purpose", "universal", "for any model", "applicable to all architectures", "generalizes across domains", "always"). Quantifiers restricted to what was evaluated ("on all five benchmarks", "consistently across our experiments", "across diverse tasks we test") do not count.
- `quantified` — at least one number or formal bound for an own result (%, x-fold, score, O(·) rate). Numbers that only describe the setup (dataset size, resolution) do not count.
- `scoped` — names at least one specific benchmark, dataset, model or baseline used in the evaluation, or states a theorem's assumptions. Counts ("nine datasets") or categories ("image classification tasks") alone do not count.

## Step 6 — Abstract overreach (none / mild / clear) — own-contribution claims only
Judge independently of Step 4: the title and the abstract can both overreach.
- **none** — all own-contribution claims stay within the evidence list.
- **mild** — some own claim is broader, stronger or more certain than the evidence (incl. claims of breadth, magnitude or SOTA backed only by unspecified experiments; class generalisation from one instance).
- **clear** — the central own claim plainly exceeds the evidence, or the abstract asserts own results it does not report at all ("none reported").

## Step 6b — Calibration rules from human decisions (apply in Steps 4 and 6)
These rules were set by the human PI on contested cases; they override any looser reading above.
- **H1 Design rationale is not evidence.** A claimed benefit that follows only from the design ("which can reduce the variance", "enables faster training") with no reported experiment, measurement or theorem for it → mild `unsupported`.
- **H2 Class generalisation applies to the abstract too.** "Models trained with X are consistently safer" when only one model is reported → mild `scope`.
- **H3 Absolute wording.** "Eliminates", "solves", "fully", "entirely", "completely", "guarantees" applied to a problem when the evidence shows improvement, not elimination → mild `certainty`.
- **H4 Unspecified generality.** A claim that the method generalises or transfers ("across architectures", "across backbones", "to new domains") when the abstract does not name what was tested → mild `scope`, even if worded as describing the experiments.
- **H5 Priority claims need support.** An unhedged priority claim about own work ("the first benchmark for…", "the first method to…", "a new paradigm"), even when restricted to a specific domain, → mild `novelty`, because the abstract reports no evidence of priority. A hedged form ("to the best of our knowledge, the first…") is not overreach.
- **H6 Dropped conditions in titles.** A title verb that asserts an effect unconditionally ("Enables", "Improves", "Makes", "Needs") while the abstract states a necessary condition or restriction for it → mild `t:scope`.
- **H7 Necessity/solution titles backed by improvements.** "X Needs Y", "Solving…", "…Fixes…" supported only by gains over baselines → mild `t:certainty`; "fixes the problem entirely" in the abstract with improvement-only evidence → mild `a:certainty`.

## Step 7 — Overreach types (only for mild/clear in Step 4 or 6; prefix `t:` title, `a:` abstract; multi-select)
`scope` (beyond the tested settings or class) · `certainty` (definitive wording where evidence is partial) · `magnitude` (intensifier/superlative beyond the reported numbers, or broader comparison than evaluated; an unquantified "significantly" with named benchmarks is not overreach) · `novelty` (unhedged priority claims about own work; see H5) · `causal` (own mechanism or cause asserted without reported evidence) · `unsupported` (own claim with no reported evidence, or contradicted).

## Decision rules
1. Absence of numbers alone is never overreach.
2. "State-of-the-art on [named benchmarks]" is not overreach; "state-of-the-art across tasks" with two benchmarks is `scope`.
3. When torn between two adjacent levels choose the lower one (for Step 4: choose matched), confidence ≤ 3.

## Output (one JSON object per item, one per line, no other text)
{"item_id": "...", "type": "method", "evidence": "≤ 25 words", "title_strength": 0, "title_vs_evidence": "NA|understated|matched|mild|clear", "hedge": 0, "booster": 0, "superlative": 0, "universal": 0, "quantified": 0, "scoped": 0, "abstract_overreach": "none|mild|clear", "types": ["t:scope", "a:magnitude"], "rationale": "≤ 30 words", "confidence": 1}
Integers for strengths, flags and confidence (1 = guess … 5 = certain). `types` is [] when nothing is mild/clear.
