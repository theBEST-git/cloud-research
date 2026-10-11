# V1 title-form annotation: Codebook A (version 1.0)

## Task
You receive one batch file in JSONL format. Each line is an item of the form
`{"item_id": "...", "title": "..."}`. The title belongs to a machine-learning research paper and is shown
exactly as its authors typed it; LaTeX math such as `$\ell_1$` may appear. For every item you record six
labels that describe the form of the title.

Judge only the title in front of you. Do not search for the paper, do not open any other file, and do not try
to infer anything about the paper beyond what its title says. Label every item; never skip one. When unsure,
choose the best-fitting label and explain briefly in `note`.

## Labels

### 1. `compound` (y / n)
A title is compound when a separator splits it into an opening part (the lead) and a remainder (the subtitle).
Separators are:
- a colon, `:` or fullwidth `：` ("Lead: Remainder");
- a dash used as a break between two parts of the title. This is normally a hyphen, en dash, em dash or a run
  of hyphens with spaces on both sides ("Lead - Remainder", "Lead — Remainder", "Lead -- Remainder"). An en or em
  dash, or a run of hyphens, without spaces also counts when it clearly breaks the title into lead and remainder
  ("Lead—Remainder").

Not separators:
- hyphens or dashes inside a word or a compound term ("Pre-training", "Kolmogorov–Arnold Networks",
  "Vision–Language Models", "state-of-the-art", "High- and Low-Resource");
- colons inside numbers, ratios or mathematics ("1:1", "2:4 sparsity", `$f: X \to Y$`);
- question marks, exclamation marks, full stops, semicolons, commas, brackets and quotation marks.

If there are several separators, the lead is the text before the first one. A title that begins with a
separator is not compound.

### 2. `lead` (verbatim text)
If compound = y, copy the lead exactly as written: every character before the first separator, without the
separator and without surrounding spaces. If compound = n, write an empty string.

### 3. `lead_type`
- `coined_name`: the lead is a name, i.e. a label that identifies one particular artefact (a model, method,
  algorithm, architecture, system, agent, dataset, benchmark, library or framework) and works like a proper noun
  or a brand. It is usually invented by the authors, but names of existing artefacts also count. A name can be
  an ordinary English word used as a name ("Heron"), can carry a version number or size ("KoalaLM 2"), and can
  be a descriptive phrase followed by its acronym in parentheses ("Contrastive Patch Alignment (CPA)").
- `descriptive_phrase`: the lead tells what the paper is about in ordinary words: a topic, task, setting,
  method description, claim, slogan or question ("Rethinking Warmup", "Graph Neural Networks", "Less Is More",
  "When Do Transformers Fail?"). Generic abbreviations that name a whole field or family of methods (RL, GNNs,
  LLMs, NLP, AI) are descriptive, not names. A phrase that merely uses a name as a modifier ("BERT-based
  Ranking", "LoRA Fine-Tuning at Scale") is descriptive.
- `genre_label`: the lead only says what kind of paper this is, not its subject: "Position", "Survey",
  "A Survey", "Review", "Tutorial", "Perspective", "Opinion", "Case Study", "Technical Report", "Erratum",
  "Note". If the lead also states the subject ("A Survey of Graph Neural Networks"), it is a descriptive_phrase.
- `none`: the title is not compound.

### 4. `lead_orthography` (only when lead_type = coined_name, otherwise "na")
Classify the written shape of the name. Apply the first rule that fits:
1. `paren_acronym`: the lead is a phrase ending in an acronym in parentheses: "Contrastive Patch Alignment (CPA)".
2. `all_caps`: every letter of the name is a capital letter (at least two letters; digits, hyphens and spaces
   are ignored): "PRISM", "GPT-4", "SAM 2", "U-NET".
3. `mixed_case`: not all capitals, and the name has a capital letter after its first character, or contains a
   digit, or contains LaTeX math: "KoalaLM 2", "LoRA", "word2vec", "AlphaFold", "Llama 2", "GPT-4o".
4. `word`: everything else, i.e. written like an ordinary word, with at most its first letter capitalised and no
   digits: "Heron", "Prometheus", "Diffuser".

### 5. `casing` (the whole title)
Consider the content words of the whole title (nouns, verbs, adjectives, adverbs). Ignore the very first word
of the title, short function words (a, an, the, of, for, in, on, at, by, with, to, and, or, via, from, as, is,
are, ...), and tokens that are always capitalised (acronyms, coined names, proper nouns and adjectives such as
"Bayesian" or "Markov").
- `title_case`: almost all of these words (about three quarters or more) start with a capital letter:
  "Learning Sparse Features From Noisy Labels".
- `sentence_case`: almost none of them (about a quarter or fewer) start with a capital letter:
  "Learning sparse features from noisy labels". A capital letter right after the separator does not change
  this. Titles written entirely in lower case also count as sentence_case.
- `all_caps`: the whole title is written in capital letters: "LEARNING SPARSE FEATURES FROM NOISY LABELS".
- `other`: the capitalisation is inconsistent (roughly between a quarter and three quarters of these words
  capitalised), or there are fewer than two such words to judge.

### 6. `question` (y / n)
`y` if the title, or any part of it, is a direct question, which normally carries a question mark
("Can Small Models Plan?", "PRISM: Do Sparse Models Share Features?"). Indirect question phrases without a
question mark ("How Transformers Learn Syntax", "What Makes Pretraining Work") are `n`.

## Worked examples (invented titles, not from your batch)
- "PRISM: Probing Representations in Sparse Models": compound y, lead "PRISM", coined_name, all_caps,
  title_case, question n.
- "KoalaLM 2: Efficient Pretraining at Small Scale": compound y, lead "KoalaLM 2", coined_name, mixed_case,
  title_case, question n.
- "Heron: a lightweight planner for household robots": compound y, lead "Heron", coined_name, word,
  sentence_case, question n.
- "Contrastive Patch Alignment (CPA): Learning Dense Features without Labels": compound y, coined_name,
  paren_acronym, title_case, question n.
- "Rethinking Warmup: Why Learning-Rate Schedules Matter": compound y, descriptive_phrase, na, title_case,
  question n.
- "Survey: Graph Learning under Distribution Shift": compound y, genre_label, na, title_case, question n.
- "Can Small Models Plan?": compound n, lead "", none, na, title_case, question y.
- "Learning 2:4 Sparse Masks for Fast Inference": compound n (ratio colon), none, na, title_case, question n.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one object per line, in the same order as
the input file, with no other lines, headers or commentary. Every object has exactly these eight keys, in this
order, and every value is a string:

{"item_id": "<copied unchanged from the input>", "compound": "y|n", "lead": "<lead copied verbatim, or empty>", "lead_type": "coined_name|descriptive_phrase|genre_label|none", "lead_orthography": "all_caps|mixed_case|word|paren_acronym|na", "casing": "title_case|sentence_case|all_caps|other", "question": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Constraints that every line must satisfy:
- compound = "n"  =>  lead = "", lead_type = "none", lead_orthography = "na".
- compound = "y"  =>  lead is non-empty and lead_type is coined_name, descriptive_phrase or genre_label.
- lead_type != "coined_name"  =>  lead_orthography = "na".

Example output lines (for the invented examples above; your item_ids come from the batch file):
{"item_id": "example-1", "compound": "y", "lead": "PRISM", "lead_type": "coined_name", "lead_orthography": "all_caps", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-2", "compound": "y", "lead": "Rethinking Warmup", "lead_type": "descriptive_phrase", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-3", "compound": "n", "lead": "", "lead_type": "none", "lead_orthography": "na", "casing": "title_case", "question": "y", "note": ""}
