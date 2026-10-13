# Topic layer

Content-based research topics for every discovery submission, built for research-fashion analyses.
Each paper with a real abstract (43,480 of 43,516) gets a **broad** (20), **middle** (100) and
**fine** (198) topic, derived from what its title and abstract say rather than from its author keywords.
Generic labels such as "deep learning" can therefore be broken down into the topics their papers
actually cover. Author keywords are also typed (generic field, research area, specific topic, …).

The whole layer is **outcome-blind**: no acceptance, decision or review field is read by any script here
(`validate_outputs.py` checks this), so topics are fixed before any outcome analysis.

## Outputs (`output/`)

| File | Unit | Contents |
|---|---|---|
| `topic_assignments.csv.gz` | paper | `fine`, `mid`, `coarse` topic codes; `mid_similarity` and `mid_margin` (how clearly the paper belongs to its middle topic); `fine_similarity` |
| `topic_catalog.csv` | topic | name, one-line description, parents, papers per year, coherence flag, stability, blind-check result, keyword signature, example titles |
| `paper_topic_stability.csv.gz` | paper | share of seed refits in which the paper stays with its topic, per level |
| `topic_year_panel.csv` | topic × year | submissions, share of that year's papers, change vs previous year |
| `generic_keyword_breakdown.csv` | keyword × era × level × topic | what papers using broad labels (any non-specific type, ≥300 papers) are about |
| `keyword_types.csv` | keyword | type of each keyword used by ≥20 papers, both annotators' labels, adjudication reason |
| `paper_keyword_profile.csv.gz` | paper | number of keywords of each type (keywords used by <20 papers are `rare_untyped`) |
| `quality_metrics.json`, `name_check.json`, `keyword_types_agreement.json`, `topic_stability.csv` | — | quality evidence (below) |
| `topic_model.npz` | — | frozen projection and centroids; `assign_topics.py` places new papers with it |
| `topic_catalog_auto.csv` | topic | pre-naming catalog produced by `build_topics.py` |

```python
import pandas as pd
topics = pd.read_csv("research/topics/output/topic_assignments.csv.gz")
catalog = pd.read_csv("research/topics/output/topic_catalog.csv", keep_default_na=False)
topics["mid_name"] = topics.mid.map(catalog.set_index("topic").name)
subs = pd.read_csv("data/submissions.csv.gz", keep_default_na=False, na_values=[r"\N"])
df = subs.merge(topics, on=["submission_id", "year"], how="left")   # 36 papers without a usable abstract have no topic
```

## Which level to use

- **Middle (m001–m100)** is the analysis level: 127–1,121 papers per topic, and 91 topics (94% of papers)
  have ≥30 papers in ≥3 years, enough to follow a topic over time.
- **Fine (f001–f198)** describes what is inside a middle topic (65–365 papers each).
- **Broad (c01–c20)** is an overview layer for figures. Seven of the 20 group unrelated middle topics
  (e.g. "Federated learning, privacy and decision making"); no alternative grouping scored better.

Recommended robustness checks for any topic-level result: repeat it (1) on papers with
`mid_stability >= 2/3`, (2) without topics whose `stability_jaccard < 0.5` or `coherence == "mixed"`,
and (3) at the fine level. For the held-out confirmation split, place papers with `assign_topics.py`;
never refit.

## How it was built

1. **Embeddings.** `title [SEP] abstract` embedded with SPECTER2 (`allenai/specter2_base` + proximity
   adapter, revisions pinned in `embed_specter2.py`). The 36 papers with abstracts under 30 words get no
   topic: 34 are placeholders ("We have withdrawn our paper."), 2 are genuine but one sentence long or
   with their spaces stripped.
2. **Middle topics.** Unit-length PCA(128) projection (93% of variance), then spherical k-means with
   k = 100 (best of 3 seeds × 20 initialisations).
3. **Broad topics.** Ward merge of the 100 middle centroids into 20 groups.
4. **Fine topics.** Each middle topic split by k-means in proportion to its size (~200 in total); pieces
   under 60 papers are folded into their nearest sibling, leaving 198.
5. **Names.** Five annotators named the topics top-down from distinctive keywords and example titles
   (`annotation/naming_batch_*.md`), with a coherence flag per topic; one reviewer then read all names
   together and made 21 revisions for duplicates and vague or non-distinguishing names.
6. **Keyword types.** The 912 keywords used by ≥20 papers were typed with one codebook
   (`annotation/keyword_types/annotation_workflow.js`) by two independent annotators; one adjudicator
   resolved the 31 disagreements.

Annotators were Claude agents run from a Claude Code session (October 2026). Their exact inputs, prompts
and outputs are in `annotation/`.

## Quality evidence

Same fitting procedure on SPECTER2 vs a word-count baseline (TF-IDF + LSA of title and abstract):

| Level | Space | Stability (ARI across seeds) | Agreement with ICLR primary areas (NMI, 2024–26) | Synonym overlap | Keyword coherence |
|---|---|---|---|---|---|
| Broad | SPECTER2 | 0.52 | **0.278** | 0.82 | 0.21 |
| Broad | word counts | 0.53 | 0.245 | 0.85 | 0.22 |
| Middle | SPECTER2 | 0.66 (0.63–0.69) | **0.302** | **0.67** | 0.29 |
| Middle | word counts | 0.67 | 0.272 | 0.46 | 0.34 |
| Fine | SPECTER2 | 0.53 | **0.295** | **0.64** | 0.31 |
| Fine | word counts | 0.64 | 0.272 | 0.44 | 0.37 |

Synonym overlap measures whether near-synonymous keywords ("large language models" / "language models")
land in the same topics; keyword coherence favours word counts partly because keywords tend to appear
verbatim in titles and abstracts.

- **Blind name check.** One random paper per fine topic, shown (title + abstract opening) to two checkers
  who saw only the fine-topic names within the paper's broad topic: right fine topic for **61%** of papers
  (chance 10%), right middle topic for **80%**.
- **Coherence flags.** Mixed: 3 of 100 middle and 9 of 198 fine topics (listed in the catalog with a note).
- **Keyword types.** Annotators agreed on 96.6% of keywords (Cohen's κ = 0.93). Both annotators were the
  same model, so this shows consistency more than validity.
- **Per-topic stability.** Median middle-topic Jaccard with its best match across refits is 0.66;
  26 middle topics score below 0.5, usually because a refit splits or merges them differently.

### Sensitivity to k (`k_sensitivity.py`)

k = 100 for the middle level was a design choice, not tuned. The middle level was refitted with k = 50–200 using
the same procedure; k = 100 reproduces the published topics exactly. Output: `output/k_sensitivity.json`, plus
`output/k_sensitivity_assignments.csv.gz` (topic per paper for each k, for rerunning analyses).

| k | Papers in trackable topics | NMI with primary areas | Stability (ARI) | Synonym overlap | Keyword coherence | NMI with k = 100 |
|---|---|---|---|---|---|---|
| 50 | 100% | 0.294 | 0.77 | 0.77 | 0.26 | 0.72 |
| 75 | 97% | 0.302 | 0.74 | 0.72 | 0.27 | 0.80 |
| **100** | **94%** | **0.302** | **0.68** | **0.67** | **0.29** | 1 |
| 150 | 76% | 0.301 | 0.62 | 0.67 | 0.31 | 0.78 |
| 200 | 53% | 0.302 | 0.57 | 0.64 | 0.33 | 0.75 |

- Agreement with ICLR's primary areas does not depend on k (0.294–0.302).
- Larger k gives more specific topics (keyword coherence up) at the cost of stability and trackability. No metric
  singles out one k. Roughly k = 75–100 keeps nearly all papers in topics trackable over time (≥30 papers in
  ≥3 years); k = 100 is the finer end of that range, chosen before the sweep and not tuned. Report main results
  at k = 75, 100 and 150.
- Label-free fashion measures barely move with k:
  - effective number of topics per year, divided by k, rises from 2017 to 2025 and dips in 2026 at every k;
  - 28–33% of topics are emerging (2024–26 share ≥3× the 2017–20 share), and they hold 40–44% of 2024–26 papers.

  The 2017 values are biased low by the small number of papers that year.
- Adjacent solutions nest only partly: 76–82% of a finer topic's papers sit in one coarser topic. Topic-level
  results should therefore be rerun at several k, not just at k = 100.

## Limitations

- Topics partition a continuous space, so boundaries move between refits (see stability above).
- Names, coherence flags and keyword types are model annotations. They were checked for consistency,
  by review and by the blind check, but not by human experts; auditing a sample is advisable.
- Text is the title and abstract in the September 2026 snapshot, which may differ from what was submitted.
- Topics are fitted on the discovery split only.
- Keywords used by fewer than 20 papers (47% of keyword uses) are untyped.

## Reproduce

```text
pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
pip install -r research/topics/requirements.txt
python research/topics/embed_specter2.py      # ~2.5 h on 4 CPUs; resumable; writes cache/ (git-ignored)
python research/topics/build_topics.py        # ~2 min
python research/topics/evaluate_topics.py     # ~15 min
python research/topics/k_sensitivity.py       # ~40 min
python research/topics/naming_inputs.py       # naming material; names come from the annotation workflow
python research/topics/finalize_catalog.py
python research/topics/derive_features.py
python research/topics/validate_outputs.py
```

Results are deterministic for the same library versions and hardware; embeddings can differ in the last
floating-point digits across machines, which can move papers that sit on a topic boundary.
