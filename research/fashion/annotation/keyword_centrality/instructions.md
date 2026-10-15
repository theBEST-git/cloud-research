# Is the keyword central to the paper's contribution?

Each item is one paper (title and abstract) together with **one keyword** that its authors listed. Decide whether
the keyword names something **central** to the paper's contribution or something **peripheral** to it.

- **central**: the main contribution proposes, studies, or is chiefly evaluated on what the keyword names.
  - The paper builds a new X, analyses X, or improves X, where X is the keyword.
  - Or the paper's main experiments are on X, and X is what the results are about.
- **peripheral**: anything else, including:
  - background or motivation only (X is mentioned as context or as the reason the problem matters);
  - a minor component (X is one ingredient among several, not what the paper is about);
  - an application mentioned in passing (X appears as a possible use, or in one secondary experiment);
  - an umbrella label the paper does not specifically address (X is a broad area the paper belongs to only loosely,
    and nothing in the abstract engages with X itself).

## How to judge

- Judge only from the title and abstract shown. Do not use outside knowledge of the paper.
- Read the keyword literally. A broad keyword (for example "large language models") is central if the paper is
  about such models themselves, or its method and experiments are built on and about them. It is peripheral if such
  models appear only as a motivation, a tool in one step, or one application among others.
- Judge each item on its own. Items are in random order, and nothing about their order or ids carries meaning.
- Forced choice: every item must be `central` or `peripheral`.
- `confidence`: `high` if the call is clear, `medium` if one reading favours your answer, `low` if it is close.
- `reason`: at most 20 words, naming what the paper is chiefly about and how the keyword relates to it.
