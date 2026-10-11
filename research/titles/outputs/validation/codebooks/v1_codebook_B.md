# V1 title-form annotation: Codebook B (version 1.0)

## What you are doing
You are coding the surface form of research-paper titles from machine learning. The batch file has one JSON
object per line, `{"item_id": "...", "title": "..."}`, with the title exactly as submitted (it may contain
LaTeX between dollar signs). Answer the six questions below for every title, in order. Base every answer on
the title string alone: no web searches, no other files, no guesses about the paper's year, venue or fate.
Code every line. If a case is borderline, pick the closest answer and say why in `note`.

## Q1. Is the title split in two? → `compound`
Look for a separator that divides the title into an opening part (call it the lead) and a remainder.
Only two kinds of mark count:
- a colon (ASCII `:` or the fullwidth `：`);
- a dash acting as a break between two parts: a hyphen, en dash, em dash or several hyphens, typically with a
  space on each side ("Otter — Streaming Speech Recognition"). An unspaced en/em dash or run of hyphens counts
  only if it plainly acts as that break ("Otter—Streaming Speech Recognition").
These do not count: hyphens and dashes that join words or names ("Self-Supervised", "Navier–Stokes",
"Image–Text Retrieval", "Pre- and Post-Training"); colons in ratios, clock times or formulas ("N:M",
`$g:\mathbb{R}\to\mathbb{R}$`); and every other punctuation mark (?, !, ., ;, commas, brackets, quotes).
Several separators: only the first matters. A separator as the very first character: answer "n".
Answer "y" or "n".

## Q2. What exactly is the lead? → `lead`
When Q1 = "y", copy the characters that precede the first separator, character for character, trimmed of
spaces and without the separator. When Q1 = "n", leave it empty ("").

## Q3. What kind of lead is it? → `lead_type`
Work through these checks in order and stop at the first "yes":
(a) Q1 = "n"? → `none`.
(b) Does the lead do nothing but announce the type of paper (for example "Position", "Overview", "Primer",
    "Short Paper", "Lessons Learned", "Survey", "Erratum")? → `genre_label`. A type word plus subject matter
    ("Review of Diffusion Samplers") is not a genre label.
(c) Is the lead the name of one specific thing (a particular model, method, algorithm, architecture, dataset,
    benchmark, environment, toolkit or system) used the way a proper noun is used? Examples of the shape:
    "MAPLE-3D", "fastSeg", "Otter", "ViT-Giga", "Gated Linear Attention (GLA)". → `coined_name`. It does not
    matter whether the name is new or already known, whether it is a dictionary word ("Otter"), or whether it
    carries a version or size tag. A label for a whole field or family (DL, LMs, LLMs, RL, CV, GNN) is not the
    name of one specific thing. Nor is a phrase in which a name is just one modifier ("CLIP-Guided Editing",
    "Transformer Variants for Speech").
(d) Otherwise the lead describes, in ordinary language, a topic, approach, finding, claim or question
    ("Scaling Laws for Routing", "Sparse Attention Revisited", "Beyond Accuracy") → `descriptive_phrase`.

## Q4. How is the name written? → `lead_orthography`
Only when Q3 = `coined_name`; otherwise write "na". Take the first description that matches:
- `paren_acronym`: a phrase that ends with an acronym in brackets, e.g. "Gated Linear Attention (GLA)".
- `all_caps`: all letters in the name are upper case (two or more letters; ignore digits, spaces and
  punctuation), e.g. "MAPLE-3D", "DQN", "VQ-VAE".
- `mixed_case`: a letter after the first one is upper case, or the name includes a digit or a math expression,
  e.g. "fastSeg", "ViT-Giga", "MuZero", "T5", "Phi-3".
- `word`: plain word shape, where only the initial letter may be a capital and there are no digits, e.g.
  "Otter", "Hyena", "Mamba".

## Q5. Which capitalisation pattern does the whole title follow? → `casing`
Set aside the first word, the small function words (articles, prepositions, conjunctions, forms of "be": a,
the, of, for, on, in, with, and, or, to, via, by, from, is, are, ...), and any word that would be capitalised
anyway (acronyms, names, adjectives formed from names such as "Gaussian"). Among the words left:
- most of them (≈ 75% or more) begin with a capital → `title_case`;
- few of them (≈ 25% or less) begin with a capital → `sentence_case` (an all-lower-case title also goes here; a
  capital right after the separator is allowed);
- the entire title is in capitals → `all_caps`;
- anything in between, or fewer than two words left to judge → `other`.

## Q6. Is it a question? → `question`
"y" when the title contains a direct question, usually closed by "?" ("Are Sparse Experts Lazy?",
"Sparse Attention Revisited: When Does Locality Help?"). Clauses that start with how/why/what but are not
asked as questions and have no "?" ("Why Warmup Works") → "n".

## Examples (made up for this codebook)
- "MAPLE-3D: Multi-View Alignment for Point-Cloud Learning" → y, "MAPLE-3D", coined_name, all_caps, title_case, n
- "fastSeg: real-time segmentation on microcontrollers" → y, "fastSeg", coined_name, mixed_case, sentence_case, n
- "Otter — Streaming Speech Recognition with Bounded Memory" → y, "Otter", coined_name, word, title_case, n
- "Position: Benchmarks Should Report Variance" → y, "Position", genre_label, na, title_case, n
- "Sparse Attention Revisited: When Does Locality Help?" → y, "Sparse Attention Revisited", descriptive_phrase,
  na, title_case, y
- "LLMs: A Field Guide to Their Failure Modes" → y, "LLMs", descriptive_phrase, na, title_case, n
- "Navier–Stokes Surrogates with Spectral Operators" → n, "", none, na, title_case, n

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one object per line, in the same order as
the input file, with no other lines, headers or commentary. Every object has exactly these eight keys, in this
order, and every value is a string:

{"item_id": "<copied unchanged from the input>", "compound": "y|n", "lead": "<lead copied verbatim, or empty>", "lead_type": "coined_name|descriptive_phrase|genre_label|none", "lead_orthography": "all_caps|mixed_case|word|paren_acronym|na", "casing": "title_case|sentence_case|all_caps|other", "question": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Constraints that every line must satisfy:
- compound = "n"  =>  lead = "", lead_type = "none", lead_orthography = "na".
- compound = "y"  =>  lead is non-empty and lead_type is coined_name, descriptive_phrase or genre_label.
- lead_type != "coined_name"  =>  lead_orthography = "na".

Example output lines (made-up items):
{"item_id": "example-1", "compound": "y", "lead": "fastSeg", "lead_type": "coined_name", "lead_orthography": "mixed_case", "casing": "sentence_case", "question": "n", "note": ""}
{"item_id": "example-2", "compound": "y", "lead": "Position", "lead_type": "genre_label", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-3", "compound": "n", "lead": "", "lead_type": "none", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": "en dash joins two names"}
