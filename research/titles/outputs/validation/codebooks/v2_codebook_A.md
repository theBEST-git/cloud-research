# V2 title-word annotation: Codebook A (version 1.0)

## Task
Each line of the batch file is one item:
`{"item_id": "...", "title": "...", "target_word": "...", "target_occurrence": 1, "sense": "...", "swap_word": "..."}`

- `title`: a machine-learning paper title, as written by its authors.
- `target_word`: the word under study, exactly as it appears in the title. `target_occurrence` says which
  occurrence of that word is meant, counting whole-word matches from the start of the title and ignoring case
  (almost always 1).
- `sense`: the meaning to test (one of improve, reveal, exploit, study_adj; defined below).
- `swap_word`: an alternative word for the substitution test in question (b).

Use only the title. Do not look up the paper and do not open any other file. Label every item.

## (a) `slot_sense`: is the target word used in the given sense? (y / n)
Answer "y" if, in this title, the target word carries the meaning below; "n" if it carries another meaning
(for example it is part of a technical term, names a specific algorithm or operation, or is used literally).

- `improve`: the word says that the paper makes something better: it raises the performance, quality,
  robustness, efficiency, capability or reach of a model, method, system or person ("Improving sample
  efficiency of ...", "Enhancing robustness of ...", "Boosting reasoning in small models", "Empowering robots
  with ...", "Advancing molecular generation with ..."). Not this sense: the word is the name of a technique
  (e.g. boosting as the ensemble-learning method that the paper is about) or has a literal physical or temporal
  meaning.
- `reveal`: the word presents the paper as bringing something to light or making it understood, i.e. analysing,
  investigating, exposing or explaining how or why something works, behaves or fails ("Understanding the
  generalization of ...", "Uncovering hidden biases in ...", "Demystifying contrastive learning",
  "Characterizing the loss landscape of ..."); methods whose purpose is to explain a model's behaviour also
  count. Not this sense: the word names a technical operation, such as generating text from a model (decoding
  algorithms) or reading out signals or stimuli from recordings, or is a noun naming a task ("Language
  Understanding with ...").
- `exploit`: the word says that the paper makes use of, draws on, takes advantage of or puts to work something
  (a resource, model, signal, structure or property), including releasing its untapped potential, in order to
  achieve a goal ("Leveraging unlabeled data for ...", "Exploiting sparsity in ...", "Harnessing pretrained
  diffusion models for ...", "Utilizing auxiliary tasks to ...", "Unlocking the potential of ... for ...").
  Not this sense: the word mainly means something else, such as making something possible, or is used
  literally.
- `study_adj`: the adjective describes the scope, breadth or thoroughness of the study, benchmark, evaluation,
  analysis, survey, review or assessment that the paper itself presents ("A Comprehensive Study of ...",
  "A Systematic Evaluation of ...", "An Extensive Analysis of ...", "A Large-Scale Benchmark for ...").
  Not this sense: the adjective belongs to another term or describes something other than the paper's own
  study.

## (b) `swap_preserves`: does the substitution keep the meaning? (y / n)
Replace the indicated occurrence of the target word with `swap_word` (already in matching capitalisation),
leaving every other word unchanged. Would a researcher in the field read the new title as saying essentially
the same thing about what the paper does? Ignore differences in tone, emphasis, excitement or style:
"Unveiling" may sound more dramatic than "Understanding", but if both titles say the paper explains the same
thing, answer "y". Answer "n" if the new title says the paper does something different, becomes ungrammatical
or nonsensical, or breaks a technical term.

## Examples (invented)
- title "Enhancing Robustness of Vision Transformers via Patch Dropout", target "Enhancing", sense improve,
  swap "Improving" → slot_sense y, swap_preserves y.
- title "Boosting with Soft Margins: A Statistical View", target "Boosting", sense improve, swap "Improving" →
  slot_sense n (the ensemble method), swap_preserves n.
- title "Decoding Strategies for Faithful Summarization", target "Decoding", sense reveal, swap
  "Understanding" → slot_sense n (text generation), swap_preserves n.
- title "Understanding Overfitting in Adversarial Training", target "Understanding", sense reveal, swap
  "Unveiling" → slot_sense y, swap_preserves y.
- title "A Systematic Study of Data Augmentation for Speech", target "Systematic", sense study_adj, swap
  "Comprehensive" → slot_sense y, swap_preserves y.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one per line, in the input order, with no
other lines or commentary. Every object has exactly these four keys, in this order, and string values:

{"item_id": "<copied unchanged from the input>", "slot_sense": "y|n", "swap_preserves": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Answer both questions for every item, even when slot_sense is "n".

Example output line:
{"item_id": "example-1", "slot_sense": "y", "swap_preserves": "y", "note": ""}
