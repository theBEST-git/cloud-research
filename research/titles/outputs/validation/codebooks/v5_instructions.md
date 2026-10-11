# V5 topic-cluster labelling: instructions (version 1.0, one pass)

## Task
Papers from a machine-learning venue were grouped automatically into 100 clusters by the similarity of their
abstracts. Each line of the batch file describes one cluster:
`{"item_id": "...", "papers": [{"title": "...", "abstract_snippet": "..."}, ... 12 entries ...]}`.
The 12 papers are the most typical members of the cluster (closest to its centre), most typical first; each
`abstract_snippet` is the first 300 characters of that paper's abstract ("…" marks the cut). Use only what is
shown: no searching, no other files.

For each cluster give:
1. `label`: a short, specific, human-readable name for the shared research topic, at most 6 words
   (e.g. "Offline reinforcement learning", "Graph neural network expressivity", "Diffusion models for image
   editing"). Name the topic itself; do not write "Papers about ..." or list several unrelated topics. If the
   cluster is mixed, name what most of the shown papers share.
2. `about_lms`: "y" if the cluster is about language models, i.e. more than half of the 12 shown papers are
   centrally about building, training, evaluating, analysing, aligning, prompting or applying neural language
   models (large language models, BERT-style encoders, earlier neural language models, multimodal or
   vision-language models that read or generate text, and agents built on language models); "n" otherwise.
   A paper that mentions a language model only in passing, or uses one as a minor component, does not count.
3. `lm_papers`: the number of the 12 shown papers (an integer from 0 to 12) that are centrally about language
   models in the sense of point 2.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per cluster, one per line, in the input order, with no other
lines or commentary. Every object has exactly these four keys, in this order:

{"item_id": "<copied unchanged from the input>", "label": "<at most 6 words>", "about_lms": "y|n", "lm_papers": <integer 0-12>}

Consistency: about_lms = "y" exactly when lm_papers >= 7.

Example output line:
{"item_id": "example-1", "label": "Instruction tuning of language models", "about_lms": "y", "lm_papers": 11}
