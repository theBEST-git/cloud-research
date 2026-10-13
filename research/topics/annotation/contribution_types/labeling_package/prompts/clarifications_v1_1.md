## Clarifications (v1.1)

These sharpen three boundaries of the rules above. They do not change any definition.

- **A named framework is usually `method`.** Most method papers name their approach and call it a "framework",
  "pipeline", "agent" or "system", often with several components. Those words do not make a paper `system`.
  If the novelty is a technique (how the components learn, reason, generate or work together), the primary type
  is `method` (`model` if the novelty is the architecture), also when the paper builds a dataset or benchmark
  along the way. Use `system` only when the engineered artifact itself is the contribution: a platform, library,
  toolkit, infrastructure, or an end-to-end tool valued for integrating existing components, for usability or
  for deployment rather than for a new technique.
- **`evaluation` is about assessing models, methods, data or outputs.** A new metric, protocol, statistical test
  or diagnostic for judging how good something is → `evaluation`. A new distance, divergence, similarity or
  "metric" that serves as a learning or modelling tool (for example a learned similarity used to choose among
  models, or a distance between probability distributions) → `method`, or `theory` if the contribution is its
  mathematical properties.
- **Foundation model: judge what the work uses or studies, not what it mentions.** Answer `no` when LLMs or other
  foundation models appear only as motivation or context while the work studies small models trained from
  scratch (for example transformers on synthetic tasks), and when the pretrained models involved are small or
  narrow (for example a pretrained small-molecule encoder). If the abstract does not indicate that a model is
  large and broadly pretrained (for example it says only "pre-trained diffusion models"), answer `no`.
