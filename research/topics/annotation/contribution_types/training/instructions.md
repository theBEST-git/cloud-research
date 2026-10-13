# Contribution-type codebook (v1, locked 2026-10-13)

Locked after a pilot on 300 papers not used to derive the categories (two independent annotators, then
adjudication; see "Pilot evidence" at the end). Do not change the types or rules without bumping the version.

Labels describe **what kind of contribution** a paper offers the research community, judged from its
title and abstract. They never describe the subject: "graph neural networks" or "LLMs" are subjects.
Categories come from open coding of 200 ICLR abstracts (see `open_coding_synthesis.json`).

For each paper record:
- **primary_type**: the paper's main contribution, one of the 12 types below
- **secondary_type**: one additional, clearly claimed contribution of a *different* type, or `none`
- **uncertain**: true if the choice between two types was a close call

## Types

| id | Name | The paper mainly offers… |
|---|---|---|
| `method` | New method or algorithm | a new procedure applied to models or data: training scheme, loss/objective, optimiser, learning, inference, decoding or prompting procedure, pruning/quantisation/acceleration technique, attack, defence, interpretability procedure |
| `model` | New model or architecture | a new model whose **structure** is the novelty: architecture, layer, module, attention/pooling component, model specification, representation format, released foundation model |
| `theory` | Theoretical analysis | mathematical results: proofs, bounds, convergence, approximation or sample-complexity results, theoretical explanations, formal models |
| `empirical` | Empirical analysis or finding | knowledge from experiments about existing methods, models or phenomena: systematic or comparative studies, discovered phenomena, failure diagnoses, demonstrated vulnerabilities, critiques |
| `system` | System or software artifact | an engineered whole: end-to-end system, agent framework, platform, library, toolkit, interpreter, code release valued as software |
| `dataset_benchmark` | Dataset, benchmark or data pipeline | data: new dataset or benchmark suite, (re-)annotation, pipelines that generate or curate training/evaluation data |
| `evaluation` | Evaluation methodology or metric | a new way of measuring: evaluation protocol or framework, metric, statistical assessment or certification procedure, diagnostic tool |
| `problem` | Problem formulation or new setting | a definition of what to solve: new task, learning setting, threat model, reformulation, formal definition of a notion |
| `application` | Domain application or domain insight | value outside ML: applying mostly existing ML to a concrete real-world problem, deployment or experience reports, findings about the domain itself |
| `recipe` | Practical recipe, guideline or baseline | actionable know-how from existing parts: training recipe, design guidelines, best practices, showing a simple baseline suffices |
| `perspective` | Unifying or conceptual perspective | a way of thinking: unifying existing methods, reframing a problem, connecting ML to another field, open questions |
| `survey_position` | Survey, review or position paper | a review of a literature, or an argued position, as the main contribution |

**Primary class used in analyses** (derived, not annotated): `model` → **method**; `system`, `problem`,
`application`, `recipe`, `perspective`, `survey_position` → **other**; `theory`, `empirical`,
`dataset_benchmark` and `evaluation` keep their id. That gives six classes: method, empirical, theory,
dataset_benchmark, evaluation, other. The fine type stays available (e.g. `model` as a "new architecture" flag).

## Choosing the primary type

1. Ask what a reader would reuse or cite the paper for, as the abstract presents it ("we propose…",
   "we introduce…", "we prove…", "we study…"). If two contributions compete, take the one the title or
   the abstract puts first.
2. The subject area never decides the type.

## Decision rules for close pairs

- **method vs model**: `model` only when the selling point is the structure (layers, modules, connectivity,
  model specification). A new way to train, run, optimise, prompt or adapt any model is `method`. A
  domain-specific technique is still `method`.
- **method vs system**: `system` when the work is presented as an integrated whole, platform, toolkit,
  library or released software, or stresses deployment/usability. One highlighted technique is `method`.
- **theory vs empirical**: by the evidence. Derivation → `theory`; experiments → `empirical`.
  Guarantees for a newly proposed method → `method` primary, `theory` secondary.
- **empirical vs method**: if a fix is proposed and is the focus → `method` primary, `empirical` secondary.
  If the paper is mainly an analysis and the fix is minor → `empirical` primary.
- **dataset_benchmark vs evaluation vs empirical**: reusable data or tasks → `dataset_benchmark`; a way to
  measure → `evaluation`; what the measurement showed → `empirical` (usually secondary).
  A data-generation step that is only part of a method → `method` primary, `dataset_benchmark` secondary.
- **problem**: a new task, setting or threat model. If it ships with a dataset or benchmark, the emphasised one
  is primary and the other secondary.
- **application**: primary only when the novelty is solving the domain problem with mostly existing ML. A new
  technique evaluated on domain data is `method` (add `application` secondary only for domain findings or claims).
- **recipe**: the takeaway is "do this in practice" or "a simple known approach suffices". Guidelines derived from
  a study → `empirical` or `theory` primary with `recipe` secondary.
- **perspective**: "X and Y are special cases of…", "we view X as…", "a connection to field Z". A proven
  unification is `theory` primary with `perspective` secondary.

## Secondary type

Give a secondary type only when the abstract **claims** a second contribution of a different type.
Routine validation is not a secondary: "experiments show our method outperforms baselines" does **not** add
`empirical`. `empirical` as secondary needs findings or insights beyond showing the method works; `theory`
as secondary needs stated proofs or guarantees.

## Foundation model (yes/no)

Also record `foundation_model` for the paper's main contribution, using this rule from facets codebook v1:

`yes` if the main contribution uses, adapts, prompts, fine-tunes, aligns, compresses, evaluates, analyses or
introduces a **large model pretrained on broad data and reused across many tasks**: LLMs (GPT, Llama, …),
BERT-style pretrained language models, vision-language models (CLIP, LLaVA, …), large text-to-image or video
diffusion models (Stable Diffusion, …), large general vision models (DINO, SAM, …), and large domain-general
pretrained models such as protein language models.

`no` if the work trains task-specific models from scratch, uses only small standard backbones (e.g. an
ImageNet-pretrained ResNet as ordinary transfer learning), or is theory not about such models.
