# V2 title-word annotation: Codebook B (version 1.0)

## Overview
You will make two yes/no judgements about one word in each research-paper title. Every input line looks like
`{"item_id": "...", "title": "...", "target_word": "...", "target_occurrence": 1, "sense": "...", "swap_word": "..."}`.
The word to judge is `target_word`; if it occurs more than once, `target_occurrence` tells you which one
(1 = first occurrence, case ignored). `sense` names the meaning you must check and `swap_word` is the
replacement for the second judgement. Rely on the title text only (no searching, no other files), and give
both judgements for every line.

## Judgement 1, `slot_sense`: does the word mean what `sense` says?
"y" when the word, as used in this title, has the meaning described for its `sense`; "n" otherwise.

- improve: "to make better or stronger". The paper raises how well, how robustly, how efficiently or how
  widely something (a model, algorithm, system, agent or user) performs. Typical: "Improving Calibration under
  Shift", "Elevating Small-Model Reasoning", "Advancing Protein Design with Equivariant Priors", "Empowering
  Agents with Memory". Answer "n" when the word is the proper name of a learning technique the paper studies
  (the boosting family of ensemble methods, for instance) or is meant physically or in time.
- reveal: "to bring to light or to make understood". The paper sets out to find out, analyse, expose or
  explain why or how something happens, including producing explanations of a model's behaviour. Typical:
  "Analyzing Attention Sinks", "Unraveling the Dynamics of Grokking", "Investigating Label Noise in Medical
  Imaging", "Explaining Classifier Decisions with Counterfactuals". Answer "n" when the word is a technical
  operation, as in generating output tokens from a sequence model or decoding signals from neural or other
  recordings, or when it is a noun naming a task ("Scene Understanding Benchmarks ...").
- exploit: "to make use of". The paper draws on, takes advantage of, or puts to work something it already has
  (data, a pretrained model, a structural property, a signal), including tapping its latent potential. Typical:
  "Harnessing Weak Labels for Segmentation", "Utilizing Symmetry for Sample-Efficient Control", "Unleashing
  Pretrained Encoders for Retrieval". Answer "n" when the word chiefly means something other than using, for
  example making something possible, or is meant literally.
- study_adj: an adjective that rates how broad or thorough the paper's own study, benchmark, evaluation,
  analysis, survey, review or assessment is. Typical: "An Extensive Evaluation of Optimizers", "A Comprehensive
  Benchmark for Tabular Learning". Answer "n" when the adjective is part of some other term or qualifies
  something other than the paper's own study.

## Judgement 2, `swap_preserves`: does `swap_word` say the same thing?
Mentally rewrite the title with the indicated occurrence of the target word replaced by `swap_word`
(capitalisation already matched) and nothing else changed. "y" if the rewritten title makes essentially the
same claim about what the paper contributes; differences of flavour, register or hype do not matter
("Harnessing" vs "Exploiting" can both mean "making use of"). "n" if the contribution described changes, the
title stops making sense or becomes ungrammatical, or a fixed technical term is broken.

## Examples (made up)
- "Leveraging Synthetic Captions for Zero-Shot Retrieval", target "Leveraging", sense exploit, swap
  "Exploiting" → slot_sense y, swap_preserves y.
- "Exploiting Label Hierarchies for Few-Shot Classification", target "Exploiting", sense exploit, swap
  "Leveraging" → slot_sense y, swap_preserves y.
- "Decoding Visual Stimuli from fMRI with Diffusion Priors", target "Decoding", sense reveal, swap
  "Understanding" → slot_sense n (reading out signals), swap_preserves n.
- "Advancing Fronts in Level-Set Segmentation", target "Advancing", sense improve, swap "Improving" →
  slot_sense n (literal motion), swap_preserves n.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one per line, in the input order, with no
other lines or commentary. Every object has exactly these four keys, in this order, and string values:

{"item_id": "<copied unchanged from the input>", "slot_sense": "y|n", "swap_preserves": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Answer both questions for every item, even when slot_sense is "n".

Example output line:
{"item_id": "example-1", "slot_sense": "n", "swap_preserves": "n", "note": "technical term: neural decoding"}
