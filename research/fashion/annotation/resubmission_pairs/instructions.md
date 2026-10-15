# Is paper B a revised version of paper A?

Each item shows two conference submissions: paper A, submitted in an earlier year, and paper B, submitted later.
Decide whether **B is a revised version of A**: the same work submitted again.

- **yes**: B and A are the same paper in substance. B may have a new title, a rewritten abstract, extra
  experiments, new baselines, or a broader framing, but its core contribution is the same as A's: the same main
  method, model, dataset, theorem or finding, presented as the paper's contribution.
- **no**: B is a different paper, including:
  - another paper on the same topic or problem;
  - a follow-up that builds on A and claims a new main contribution (a new method, a new setting, a new theory);
  - a paper that uses the same technique for a different purpose;
  - a paper that only shares a dataset, benchmark or general approach with A.

## How to judge

- Judge only from the two titles and abstracts shown. Do not use outside knowledge.
- Compare the specific claims: what is proposed, what is shown, and on what. Topic overlap alone is never enough for
  `yes`.
- Judge each pair on its own. Pairs are in random order, and nothing about their order or ids carries meaning.
- Forced choice: every pair must be `yes` or `no`.
- `confidence`: `high` if the call is clear, `medium` if one reading favours your answer, `low` if it is close.
- `reason`: at most 20 words, naming the shared or differing core contribution.
