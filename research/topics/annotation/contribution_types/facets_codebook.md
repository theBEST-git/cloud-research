# Facets codebook (v1, locked 2026-10-13)

Three facets that complement the contribution type (codebook.md). Judge from title and abstract only.
They describe the paper's **main contribution** (the one its primary type refers to). Never decide a facet
from the subject alone.

For each paper record `stage`, `goal`, `foundation_model` (yes/no) and `uncertain` (true if any facet was a
close call).

## Stage: where in the ML pipeline the main contribution acts

| id | Acts on… | Examples |
|---|---|---|
| `data` | the data a model learns from or is evaluated on | synthetic data generation, augmentation, data selection/filtering, labelling, dataset distillation, poisoning |
| `architecture` | the model's structure | new layers, attention variants, modules, network design, tokenisers/input representations, model specification |
| `training` | how a model is trained or pre-trained | losses, objectives, regularisers, learning and RL algorithms, self-supervised objectives, optimisers, schedules, initialisation, distributed/federated or continual training |
| `post_training` | an already-trained model, changing its weights | fine-tuning, PEFT/LoRA, instruction tuning, RLHF/preference optimisation, model editing, merging, unlearning, distillation into a smaller model, quantisation/pruning of trained models |
| `inference` | the use of a model without (or only briefly) changing it | prompting, in-context learning, decoding, sampling, search/planning at test time, test-time compute or adaptation, retrieval augmentation, post-hoc calibration/conformal prediction, inference-time attacks and defences |
| `evaluation` | measuring or examining models or methods | benchmarks, metrics, evaluation protocols, probing and interpretability analyses of trained models |
| `system` | a whole pipeline spanning several stages | agent frameworks, end-to-end systems, platforms, toolkits |
| `general` | no single stage | learning theory not about one stage, problem formulations, perspectives |

Rules:
- Pick the stage the contribution **changes**. A new loss used to fine-tune a pretrained model is `post_training`;
  the same loss for training from scratch is `training`.
- Empirical analyses and theory take the stage they study: a study of training dynamics is `training`, a study of
  in-context learning is `inference`, an expressivity result about an architecture is `architecture`.
- Benchmarks, datasets for evaluation and metrics are `evaluation`; datasets built to train models are `data`.
- Interpretability *methods* that explain a trained model are `evaluation`.

## Goal: the main property the contribution improves or examines

| id | The paper mainly claims to improve or examine… |
|---|---|
| `capability` | task performance, accuracy, quality or new abilities (the default when the claim is "better results") |
| `efficiency` | compute, memory, latency, energy, parameter count or communication cost |
| `data_efficiency` | learning from fewer labels or samples: few-shot, semi/self/weak supervision, noisy labels, active learning, sample efficiency |
| `generalization` | out-of-distribution generalisation, domain shift, transfer, continual learning without forgetting, compositionality |
| `robustness_security` | adversarial robustness, attacks and defences, backdoors, poisoning, watermarking, model stealing |
| `safety_alignment` | harmful or unsafe behaviour, jailbreaks, alignment with human preferences or values, honesty, refusal |
| `understanding` | explaining models or learning phenomena: interpretability, mechanistic insight, why or when methods work |
| `reliability` | calibration, uncertainty quantification, out-of-distribution or anomaly detection, hallucination, factuality |
| `privacy_fairness` | differential privacy, membership or data leakage, unlearning for privacy, fairness and bias |

Rules:
- Take the property the title or abstract foregrounds. "Same accuracy at lower cost" is `efficiency`; "higher
  accuracy" is `capability`.
- Benchmarks and analyses take the property they evaluate: an agent-capability benchmark is `capability`, a
  jailbreak benchmark `safety_alignment`, a study of why transformers generalise `understanding`.
- Theory explaining why a method works is `understanding`; a guarantee about a new method's speed is `efficiency`.

## Foundation model (yes/no)

`yes` if the main contribution uses, adapts, prompts, fine-tunes, aligns, compresses, evaluates, analyses or
introduces a **large model pretrained on broad data and reused across many tasks**: LLMs (GPT, Llama, …),
BERT-style pretrained language models, vision-language models (CLIP, LLaVA, …), large text-to-image or video
diffusion models (Stable Diffusion, …), large general vision models (DINO, SAM, …), and large domain-general
pretrained models such as protein language models.

`no` if the work trains task-specific models from scratch, uses only small standard backbones (e.g. an
ImageNet-pretrained ResNet as ordinary transfer learning), or is theory not about such models.

## Pilot evidence (v0.9 → v1, no rule changes)

Same 300 pilot papers as the contribution-type pilot, two independent annotators (the same model, so agreement
shows consistency more than human-level validity), 21 papers adjudicated (`pilot_gold_facets.csv`).

| Facet | Agreement | Cohen's κ | Main confusions |
|---|---|---|---|
| Stage | 96.0% | 0.95 | architecture vs training, system vs training |
| Goal | 96.3% | 0.95 | capability vs generalization, capability vs efficiency |
| Foundation model | 99.7% | 0.99 | one paper |

Among the 240 random papers: stage training 32%, architecture 24%, post-training 14%, inference 13%,
evaluation 8%, data 5%, general 3%, system 2%; goal capability 47%, efficiency 15%, understanding 10%,
generalization 8%, data efficiency 8%, robustness/security 5%, reliability 3%, safety/alignment 2%,
privacy/fairness 2%; foundation model 30%. The foundation-model share rises from 0% of pilot papers in
2017–2020 to 57% in 2026. Within method papers, no stage × goal combination exceeds 19%.
