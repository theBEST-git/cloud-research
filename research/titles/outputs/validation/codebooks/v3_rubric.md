# V3 abstract style rating: rubric (version 1.0, one pass)

## Task
Each line of the batch file is `{"item_id": "...", "abstract": "..."}`: the abstract of a machine-learning
research paper. For each abstract, rate from 1 to 5 how likely it is that the text was written or substantially
polished by a large language model (LLM) such as a chat assistant. Judge the prose only; do not search for the
paper, do not open any other file, and do not try to guess the paper's year or venue. Rate every item.

## Scale
- 1: almost certainly human-written, with no LLM polishing.
- 2: probably human-written.
- 3: cannot tell; signals are absent or point both ways.
- 4: probably LLM-written or LLM-polished.
- 5: almost certainly LLM-written or heavily LLM-polished.

## How to judge
Machine-learning abstracts are formulaic by tradition ("We propose X, a novel method that ... Experiments on
... show ..."). That template alone is not evidence of LLM use. Weigh the prose as a whole and do not let the
presence of any single word or punctuation mark decide the rating.

Cues that tend to raise the rating (several together matter more than any one):
- an elevated, promotional or ornate register out of step with the technical content; stacked evaluative
  adjectives and adverbs;
- generic framing sentences that could open almost any paper, and broad closing claims of impact or of
  "paving the way" with little that is specific to this work;
- uniformly smooth, evenly paced sentences of similar length and shape; neat parallel lists (often of three);
  paired constructions such as "not only ... but also";
- high-level summaries that restate the contribution several times in different words instead of adding
  concrete detail.

Cues that tend to lower the rating:
- idiosyncratic or non-native phrasing, small grammatical slips, typos or awkward but natural constructions;
- terse, dense technical writing with specific details (numbers, named datasets, precise mechanisms);
- uneven rhythm, informal asides, field jargon used naturally and economically.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one per line, in the input order, with no
other lines or commentary. Every object has exactly these three keys, in this order:

{"item_id": "<copied unchanged from the input>", "rating": <integer 1-5>, "cues": "<the main cues behind the rating, at most 15 words>"}

Example output line:
{"item_id": "example-1", "rating": 2, "cues": "terse technical detail, specific numbers, slightly awkward phrasing"}
