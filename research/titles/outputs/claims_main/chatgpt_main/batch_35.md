# Batch 35 — 100 items

## item_id: m_3401

TITLE: A Neural Sandbox Framework for Discovering Spurious Concpets in LLM Decisions

ABSTRACT: We introduce a neural sandbox framework for text classification via self-referencing defined label concepts from an Large Language Model(LLM). The framework draws inspiration from the define-optimize alignment problem, in which the motivations of a model are described initially and then the model is optimized to align with these predefined objectives. In our case, we design our framework to perform text classification. We take a frozen LLM as a vector embedding generator for text and provide our framework with defined concept words based on the labels along with the input text. We then optimize an operator to classify the input text based on the relevance scores to the concept operator words(cop-words). In our experiments with multiple text classification datasets and LLM models, we find, incorporating our sandbox network generally improves the accuracy by a range of 0.12\% to 6.31\% in accuracy and 0.3\% to 8.82\% in macro f1 when compared to a baseline. The framework, not only serves as a classification tool but also as a descriptive tool for the model's decision of its prediction, based on the provided cop-words. Through further evaluations involving the injection of "foreign" cop-words, we showcase the sandbox framework's capacity to exhibit a coherent understanding of learned concepts and construct methodologies to discover potential spurious behaviors and biases within it. Despite witnessing results confirming our network's ability to capture domain knowledge, we show evidence that the model's secondary incentives do not match human decisions.

## item_id: m_3402

TITLE: Conditional Image Synthesis With Auxiliary Classifier GANs

ABSTRACT: Synthesizing high resolution photorealistic images has been a long-standing challenge in machine learning. In this paper we introduce new methods for the improved training of generative adversarial networks (GANs) for image synthesis. We construct a variant of GANs employing label conditioning that results in 128x128 resolution image samples exhibiting global coherence. We expand on previous work for image quality assessment to provide two new analyses for assessing the discriminability and diversity of samples from class-conditional image synthesis models. These analyses demonstrate that high resolution samples provide class information not present in low resolution samples. Across 1000 ImageNet classes, 128x128 samples are more than twice as discriminable as artificially resized 32x32 samples. In addition, 84.7% of the classes have samples exhibiting diversity comparable to real ImageNet data.

## item_id: m_3403

TITLE: Machine Learning For Elliptic PDEs: Fast Rate Generalization Bound, Neural Scaling Law and Minimax Optimality

ABSTRACT: In this paper, we study the statistical limits of deep learning techniques for solving elliptic partial differential equations (PDEs) from random samples using the Deep Ritz Method (DRM) and Physics-Informed Neural Networks (PINNs). To simplify the problem, we focus on a prototype elliptic PDE: the Schr\"odinger equation on a hypercube with zero Dirichlet boundary condition, which has wide application in the quantum-mechanical systems. We establish upper and lower bounds for both methods, which improves upon concurrently developed upper bounds for this problem via a fast rate generalization bound. We discover that the current Deep Ritz Methods is sub-optimal and propose a modified version of it. We also prove that PINN and the modified version of DRM can achieve minimax optimal bounds over Sobolev spaces. Empirically, following recent work which has shown that the deep model accuracy will improve with growing training sets according to a power law, we supply computational experiments to show a similar behavior of dimension dependent power law for deep PDE solvers.

## item_id: m_3404

TITLE: Semi-Supervised Learning via New Deep Network Inversion

ABSTRACT: We exploit a recently derived inversion scheme for arbitrary deep neural networks to develop a new semi-supervised learning framework that applies to a wide range of systems and problems.  
The approach reaches current state-of-the-art methods on MNIST and provides reasonable performances on SVHN and CIFAR10. Through the introduced method, residual networks are for the first time applied to semi-supervised tasks. Experiments with one-dimensional signals highlight the generality of the method. Importantly, our approach is simple, efficient, and requires no change in the deep network architecture.

## item_id: m_3405

TITLE: GUNet: A Graph Convolutional Network United Diffusion Model for Stable and Diversity Pose Generation

ABSTRACT: Pose skeleton images are an important reference in pose-controllable image generation. In order to enrich the source of skeleton images, recent works have investigated the generation of pose skeletons based on natural language. These methods are based on GANs. However, it remains challenging to perform diverse, structurally correct and aesthetically pleasing human pose skeleton generation with various textual inputs. To address this problem, we propose a framework with GUNet as the main model, PoseDiffusion. It is the first generative framework based on a diffusion model and also contains a series of variants fine-tuned based on a stable diffusion model. PoseDiffusion demonstrates several desired properties that outperform existing methods. 1) Correct Skeletons. GUNet, a denoising model of PoseDiffusion, is designed to incorporate graphical convolutional neural networks. It is able to learn the spatial relationships of the human skeleton by introducing skeletal information during the training process. 2) Diversity. We decouple the key points of the skeleton and characterise them separately, and use cross-attention to introduce textual conditions. Experimental results show that PoseDiffusion outperforms existing SoTA algorithms in terms of stability and diversity of text-driven pose skeleton generation. Qualitative analyses further demonstrate its superiority for controllable generation in Stable Diffusion.

## item_id: m_3406

TITLE: CaCuTe: Casual Cubic-Model Technique for Faster Optimization

ABSTRACT: We establish a local $\mathcal{O}(k^{-2})$ rate for the gradient update $x^{k+1}=x^k-\nabla f(x^k)/\sqrt{H\|\nabla f(x^k)\|}$ under a $2H$-Hessian--Lipschitz assumption. Regime detection relies on Hessian--vector products, avoiding Hessian formation or factorization.
Incorporating this certificate into cubic-regularized Newton (CRN) and an accelerated variant enables per-iterate switching between the cubic and gradient steps while preserving CRN’s global guarantees. The technique achieves the lowest wall-clock time among compared baselines in our experiments.
In the first-order setting, the technique yields a monotone, adaptive, parameter-free method that inherits the local $\mathcal{O}(k^{-2})$ rate. Despite backtracking, the method shows superior wall-clock performance. Additionally, we cover smoothness relaxations beyond classical gradient--Lipschitzness, enabling tighter bounds, including global $\mathcal{O}(k^{-2})$ rates. 
Finally, we generalize the technique to the stochastic setting.

## item_id: m_3407

TITLE: Tensorial Mixture Models

ABSTRACT: We introduce a generative model, we call Tensorial Mixture Models (TMMs) based on mixtures of basic
component distributions over local structures (e.g. patches in an image) where the dependencies between
the local-structures are represented by a "priors tensor" holding the prior probabilities of assigning a
component distribution to each local-structure.

In their general form, TMMs are intractable as the priors tensor is typically of exponential size. However,
when the priors tensor is decomposed it gives rise to an arithmetic circuit which in turn transforms the
TMM into a Convolutional Arithmetic Circuit (ConvAC). A ConvAC corresponds to a shallow (single hidden layer)
network when the priors tensor is decomposed by a CP (sum of rank-1) approach and corresponds to a
deep network when the decomposition follows the Hierarchical Tucker (HT) model.

The ConvAC representation of a TMM possesses several attractive properties. First, the inference is tractable
and is implemented by a forward pass through a deep network. Second, the architectural design of the model
follows the deep networks community design, i.e.,  the structure of TMMs is determined by just two easily
understood factors: size of pooling windows and number of channels. Finally, we demonstrate the effectiveness
of our model when tackling the problem of classification with missing data, leveraging TMMs unique ability of
tractable marginalization which leads to optimal classifiers regardless of the missingness distribution.

## item_id: m_3408

TITLE: RANDOM MASK: Towards Robust Convolutional Neural Networks

ABSTRACT: Robustness of neural networks has recently been highlighted by the adversarial examples, i.e., inputs added with well-designed  perturbations which are imperceptible to humans but can cause the network to give incorrect outputs. In this paper, we design a new CNN architecture that by itself has good robustness. We introduce a simple but powerful technique, Random Mask, to modify existing CNN structures. We show that CNN with Random Mask achieves state-of-the-art performance against black-box adversarial attacks without applying any adversarial training. We next investigate the adversarial examples which “fool” a CNN with Random Mask. Surprisingly, we find that these adversarial examples often “fool” humans as well. This raises fundamental questions on how to define adversarial examples and robustness properly.

## item_id: m_3409

TITLE: Tiny-CAD-Coder: Leveraging Pre-trained Code Models for Improved CAD Generation

ABSTRACT: Generative methods for Computer-Aided Design (CAD) are an emerging challenge with broad implications in engineering and manufacturing. Prior work has used direct tokenization or JSON representations and fine-tuned large language models (LLMs), but these approaches are limited to the text and image modalities of the LLM, rely on expensive feedback loops, and struggle with validity. We argue that CAD is inherently code-like: it consists of ordered command sequences with variable parameters, closely resembling programming languages. Building on this insight, we introduce Tiny-CAD-Coder, a framework that fine-tunes pre-trained code models for CAD generation and adapts to diverse input modalities through prefix tuning. By representing construction histories as Python code, our method exploits the syntactic and semantic priors of code models, while prefix embeddings provide a lightweight and extensible interface to condition on B-Rep, text, images, or other structured inputs that are not covered by LLMs used in prior works. Our experiments show that a 1B parameter code model matches or outperforms fine-tuned 7B-parameters LLMs and multi-shot prompting with 450B models. We also contribute a dataset of CAD code samples derived from Omni-CAD. Our results establish code models with prefix tuning as an efficient and general foundation for multi-modal CAD generation tasks.

## item_id: m_3410

TITLE: Supervision Complexity and its Role in Knowledge Distillation

ABSTRACT: Despite the popularity and efficacy of knowledge distillation, there is limited understanding of why it helps. In order to study the generalization behavior of a distilled student, we propose a new theoretical framework that leverages supervision complexity: a measure of alignment between teacher-provided supervision and the student's neural tangent kernel. The framework highlights a delicate interplay among the teacher's accuracy, the student's margin with respect to the teacher predictions, and the complexity of the teacher predictions. Specifically, it provides a rigorous justification for the utility of various techniques that are prevalent in the context of distillation, such as early stopping and temperature scaling. Our analysis further suggests the use of online distillation, where a student receives increasingly more complex supervision from teachers in different stages of their training. We demonstrate efficacy of online distillation and validate the theoretical findings on a range of image classification benchmarks and model architectures.

## item_id: m_3411

TITLE: Hadamard Product for Low-rank Bilinear Pooling

ABSTRACT: Bilinear models provide rich representations compared with linear models. They have been applied in various visual tasks, such as object recognition, segmentation, and visual question-answering, to get state-of-the-art performances taking advantage of the expanded representations. However, bilinear representations tend to be high-dimensional, limiting the applicability to computationally complex tasks. We propose low-rank bilinear pooling using Hadamard product for an efficient attention mechanism of multimodal learning. We show that our model outperforms compact bilinear pooling in visual question-answering tasks with the state-of-the-art results on the VQA dataset, having a better parsimonious property.

## item_id: m_3412

TITLE: Intrinsic Explanation of Random Subspace Method for Enhanced Security Applications

ABSTRACT: Random subspace method has wide security applications such as providing certified defenses against adversarial and backdoor attacks, and building robustly aligned LLM against jailbreaking attacks. However, the explanation of random subspace method lacks sufficient exploration. Existing state-of-the-art feature attribution methods such as Shapley value and LIME are computationally impractical and lacks security guarantee when applied to random subspace method. In this work, we propose EnsembleSHAP, an intrinsically faithful and secure feature attribution for random subspace method that reuses its computational byproducts. Specifically, our feature attribution method is 1) computationally efficient, 2) maintains essential properties of effective feature attribution (such as local accuracy), and 3) offers guaranteed protection against attacks on feature attribution methods. We perform comprehensive evaluations for our explanation's effectiveness when faced with different empirical attacks. Our experimental results demonstrates that our explanation not only faithfully reports the most important features, but also certifiably detects the harmful features embedded in the input sample.

## item_id: m_3413

TITLE: Stabilizing Adversarial Nets with Prediction Methods

ABSTRACT: Adversarial neural networks solve many important problems in data science, but are notoriously difficult to train. These difficulties come from the fact that optimal weights for adversarial nets correspond to saddle points, and not minimizers, of the loss function. The alternating stochastic gradient methods typically used for such problems do not reliably converge to saddle points, and when convergence does happen it is often highly sensitive to learning rates. We propose a simple modification of stochastic gradient descent that stabilizes adversarial networks. We show, both in theory and practice, that the proposed method reliably converges to saddle points. This makes adversarial networks less likely to "collapse," and enables faster training with larger learning rates.

## item_id: m_3414

TITLE: Constrained Decoding for Cross-lingual Label Projection

ABSTRACT: Zero-shot cross-lingual transfer utilizing multilingual LLMs has become a popular learning paradigm for low-resource languages with no labeled training data. However, for NLP tasks that involve fine-grained predictions on words and phrases, the performance of zero-shot cross-lingual transfer learning lags far behind supervised fine-tuning methods. Therefore, it is common to exploit translation and label projection to further improve the performance by (1) translating training data that is available in a high-resource language (e.g., English) together with the gold labels into low-resource languages, and/or (2) translating test data in low-resource languages to a high-source language to run inference on, then projecting the predicted span-level labels back onto the original test data. However, state-of-the-art marker-based label projection methods suffer from translation quality degradation due to the extra label markers injected in the input to the translation model. In this work, we explore a new direction that leverages constrained decoding for label projection to overcome the aforementioned issues. Our new method not only can preserve the quality of translated texts but also has the versatility of being applicable to both translating training and translating test data strategies. This versatility is crucial as our experiments reveal that translating test data can lead to a considerable boost in performance compared to translating only training data. We evaluate on two cross-lingual transfer tasks, namely Named Entity Recognition and Event Argument Extraction, spanning 20 languages. The results demonstrate that our approach outperforms the state-of-the-art marker-based method by a large margin and also shows better performance than other label projection methods that rely on external word alignment.

## item_id: m_3415

TITLE: Text2Model: Model Induction for Zero-shot Generalization Using Task Descriptions

ABSTRACT: We study the problem of generating a training-free task-dependent visual classifier from text descriptions without visual samples. This Text-to-Model (T2M) problem is closely related to zero-shot learning, but unlike previous work, a T2M model infers a model tailored to a task, taking into account all classes in the task. We analyze the symmetries of T2M, and characterize the equivariance and invariance properties of corresponding models. In light of these properties we design an architecture based on hypernetworks that given a set of new class descriptions predicts the weights for an object recognition model which classifies images from those zero-shot classes. 
We demonstrate the benefits of our approach compared to zero-shot learning from text descriptions in image and point-cloud classification using various types of text descriptions: From single words to rich text descriptions.

## item_id: m_3416

TITLE: Learning Approximate Distribution-Sensitive Data Structures

ABSTRACT: We present a computational model of mental representations as data-structures which are distribution sensitive, i.e., which exploit non-uniformity in their usage patterns to reduce time or space complexity.
Abstract data types equipped with axiomatic specifications specify classes of concrete data structures with equivalent logical behavior.
We extend this formalism to distribution-sensitive data structures with the concept of a probabilistic axiomatic specification, which is implemented by a concrete data structure only with some probability.
We employ a number of approximations to synthesize several distribution-sensitive data structures from probabilistic specification as deep neural networks, such as a stack, queue, natural number, set, and binary tree.

## item_id: m_3417

TITLE: Emb-GAM: an Interpretable and Efficient Predictor using Pre-trained Language Models

ABSTRACT: Deep learning models have achieved impressive prediction performance but often sacrifice interpretability, a critical consideration in high-stakes domains such as healthcare or policymaking. In contrast, generalized additive models (GAMs) can maintain interpretability, but often suffer from poor prediction performance due to their inability to effectively capture feature interactions. In this work, we aim to bridge this gap by using pre-trained large-language models to extract embeddings for each input before learning a linear model in the embedding space. The final model (which we call Emb-GAM) is a transparent, linear function of its input features and feature interactions.
Leveraging the language model allows Emb-GAM to learn far fewer linear coefficients, model larger interactions, and generalize well to novel inputs (e.g. unseen ngrams in text). Across a variety of natural-language-processing datasets, Emb-GAM achieves strong prediction performance without sacrificing interpretability. All code for using Emb-GAM and reproducing our results is made available on github.

## item_id: m_3418

TITLE: Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning

ABSTRACT: We propose a simple algorithm to train stochastic neural networks to draw samples from given target distributions for probabilistic inference. Our method is based on iteratively adjusting the neural network parameters so that the output changes along a Stein variational gradient that maximumly decreases the KL divergence with the target distribution. Our method works for any target distribution specified by their unnormalized density function, and can train any black-box architectures that are differentiable in terms of the parameters we want to adapt. As an application of our method, we propose an amortized MLE algorithm for training deep energy model, where a neural sampler is adaptively trained to approximate the likelihood function. Our method mimics an adversarial game between the deep energy model and the neural sampler, and obtains realistic-looking images competitive with the state-of-the-art results.

## item_id: m_3419

TITLE: Iterative Deep Compression : Compressing Deep Networks for Classification and Semantic Segmentation

ABSTRACT: Machine learning and in particular deep learning approaches have outperformed many traditional techniques in accomplishing complex tasks such as
image classfication, natural language processing or speech recognition. Most of the state-of-the art deep networks have complex architecture and use a vast number of parameters to reach this superior performance. Though these networks use a large number of learnable parameters, those parameters present significant redundancy. Therefore, it is possible to compress the network without much affecting its accuracy by eliminating those redundant and unimportant parameters.
In this work, we propose a three stage compression pipeline, which consists of pruning, weight sharing and quantization to compress deep neural networks.
Our novel pruning technique combines magnitude based ones with dense sparse dense ideas and iteratively finds for each layer its achievable sparsity instead of selecting a single threshold for the whole network.
Unlike previous works, where compression is only applied on networks performing classification, we evaluate and perform compression on networks for classification as well as semantic segmentation, which is greatly useful for understanding scenes in autonomous driving.
We tested our method on LeNet-5 and FCNs, performing classification and semantic segmentation, respectively. With LeNet-5 on MNIST, pruning reduces the number of parameters by 15.3 times and storage requirement from 1.7 MB to 0.006 MB with accuracy loss of 0.03%. With FCN8 on Cityscapes, we decrease the number of parameters by 8 times and reduce the storage requirement from 537.47 MB to 18.23 MB with class-wise intersection-over-union (IoU) loss of 4.93% on the validation data.

## item_id: m_3420

TITLE: SiNGER: A Clearer Voice Distills Vision Transformers Further

ABSTRACT: Vision Transformers are widely adopted as the backbone of vision foundation models, but they are known to produce high-norm artifacts that degrade representation quality.
When knowledge distillation transfers these features to students, high-norm artifacts dominate the objective, so students overfit to artifacts and underweight informative signals, diminishing the gains from larger models. Prior work attempted to remove artifacts but encountered an inherent trade-off between artifact suppression and preserving informative signals from teachers. To address this, we introduce Singular Nullspace-Guided Energy Reallocation (SiNGER), a novel distillation framework that suppresses artifacts while preserving informative signals.
The key idea is principled teacher feature refinement: during refinement, we leverage the nullspace-guided perturbation to preserve information while suppressing artifacts.
Then, the refined teacher's features are distilled to a student. 
We implement this perturbation efficiently with a LoRA-based adapter that requires minimal structural modification.
Extensive experiments show that SiNGER consistently improves student models, achieving state-of-the-art performance in multiple downstream tasks and producing clearer and more interpretable representations.

## item_id: m_3421

TITLE: Action Semantics Network: Considering the Effects of Actions in Multiagent Systems

ABSTRACT: In multiagent systems (MASs), each agent makes individual decisions but all of them contribute globally to the system evolution. Learning in MASs is difficult since each agent's selection of actions must take place in the presence of other co-learning agents. Moreover, the environmental stochasticity and uncertainties increase exponentially with the increase in the number of agents. Previous works borrow various multiagent coordination mechanisms into deep learning architecture to facilitate multiagent coordination. However, none of them explicitly consider action semantics between agents that different actions have different influences on other agents. In this paper, we propose a novel network architecture, named Action Semantics Network (ASN), that explicitly represents such action semantics between agents. ASN characterizes different actions' influence on other agents using neural networks based on the action semantics between them. ASN can be easily combined with existing deep reinforcement learning (DRL) algorithms to boost their performance. Experimental results on StarCraft II micromanagement and Neural MMO show ASN significantly improves the performance of state-of-the-art DRL approaches compared with several network architectures.

## item_id: m_3422

TITLE: Neural Approximation of an Auto-Regressive Process through Confidence Guided Sampling

ABSTRACT: We propose a generic confidence-based approximation that can be plugged in and simplify an auto-regressive generation process with a proved convergence. We first assume that the priors of future samples can be generated in an independently and identically distributed (i.i.d.) manner using an efficient predictor. Given the past samples and future priors, the mother AR model can post-process the priors while the accompanied confidence predictor decides whether the current sample needs a resampling or not. Thanks to the i.i.d. assumption, the post-processing can update each sample in a parallel way, which remarkably accelerates the mother model. Our experiments on different data domains including sequences and images show that the proposed method can successfully capture the complex structures of the data and generate the meaningful future samples with lower computational cost while preserving the sequential relationship of the data.}

## item_id: m_3423

TITLE: Hottel Zone Physics-Constrained Networks for Furnaces

ABSTRACT: This paper investigates a novel approach to improve the temperature profile prediction of furnaces in foundation industries, crucial for sustainable manufacturing. While existing methods like the Hottel Zone model are accurate, they lack real-time inference capabilities. Deep learning methods excel in speed and prediction but require careful generalization for real-world applications. We propose a regularization technique that leverages the Hottel Zone method to make deep neural networks physics-aware, improving prediction accuracy for furnace temperature profiles. Our approach demonstrates effectiveness on various neural network architectures, including Multi-Layer Perceptrons (MLP), Long Short-Term Memory (LSTM) and Kolmogorov-Arnold Networks (KANs). We also discussion the data generation involved.

## item_id: m_3424

TITLE: Adaptive Drug Interaction Prediction via Enhanced Graph Representation Learning

ABSTRACT: This paper presents a groundbreaking theoretical framework for drug-drug interaction (DDI) prediction that seamlessly integrates domain adaptation (DA) techniques with advanced mathematical concepts. We introduce GraphPharmNet, a novel architecture that operates on DDI-DA bundles, leveraging gauge-equivariant geometric deep learning to capture the intricate structure of drug interactions across domains. Our approach reformulates the DDI prediction problem using the language of differential geometry, optimal transport, and symplectic geometry, viewing domain adaptation as a Hamiltonian flow on a statistical manifold. We develop a cohomological interpretation of domain invariance, characterizing robust DDI prediction features through the lens of persistent homology and sheaf theory. The domain adaptation process is analyzed using a geometric renormalization group framework, revealing a profound connection between the DDI-DA bundle's geometry and the emergence of domain-invariant predictive features. We further elucidate the spectral properties of the DDI-DA Laplacian, providing insights into the topological stability of domain adaptation in DDI prediction. Extensive experiments on benchmark datasets demonstrate that GraphPharmNet significantly outperforms existing methods, particularly in scenarios with limited data or when transferring knowledge across disparate domains. Our results highlight the power of this unified mathematical framework in capturing complex drug interactions and adapting to new domains, paving the way for more accurate, robust, and interpretable DDI prediction models. This work not only advances the field of computational drug discovery but also establishes a rigorous theoretical foundation for domain adaptation in graph-structured data, with potential applications across a wide range of scientific disciplines. Our anonymous github link: \textbf{https://anonymous.4open.science/r/GraphPharmNet-C9D9}

## item_id: m_3425

TITLE: Accelerating 3D Molecule Generation via Jointly Geometric Optimal Transport

ABSTRACT: This paper proposes a new 3D molecule generation framework, called GOAT, for fast and effective 3D molecule generation based on the flow-matching optimal transport objective. Specifically, we formulate a geometric transport formula for measuring the cost of mapping multi-modal features (e.g., continuous atom coordinates and categorical atom types) between a base distribution and a target data distribution. Our formula is solved within a joint, equivariant, and smooth representation space. This is achieved by transforming the multi-modal features into a continuous latent space with equivariant networks. In addition, we find that identifying optimal distributional coupling is necessary for fast and effective transport between any two distributions. We further propose a mechanism for estimating and purifying optimal coupling to train the flow model with optimal transport. By doing so, GOAT can turn arbitrary distribution couplings into new deterministic couplings, leading to an estimated optimal transport plan for fast 3D molecule generation. The purification filters out the subpar molecules to ensure the ultimate generation quality. We theoretically and empirically prove that the proposed optimal coupling estimation and purification yield transport plan with non-increasing cost. Finally, extensive experiments show that GOAT enjoys the efficiency of solving geometric optimal transport, leading to a double speedup compared to the sub-optimal method while achieving the best generation quality regarding validity, uniqueness, and novelty.

## item_id: m_3426

TITLE: Guided-TTS:Text-to-Speech with Untranscribed Speech

ABSTRACT: Most neural text-to-speech (TTS) models require $\langle$speech, transcript$\rangle$ paired data from the desired speaker for high-quality speech synthesis, which limits the usage of large amounts of untranscribed data for training. In this work, we present Guided-TTS, a high-quality TTS model that learns to generate speech from untranscribed speech data. Guided-TTS combines an unconditional diffusion probabilistic model with a separately trained phoneme classifier for text-to-speech. By modeling the unconditional distribution for speech, our model can utilize the untranscribed data for training. For text-to-speech synthesis, we guide the generative process of the unconditional DDPM via phoneme classification to produce mel-spectrograms from the conditional distribution given transcript. We show that Guided-TTS achieves comparable performance with the existing methods without any transcript for LJSpeech. Our results further show that a single speaker-dependent phoneme classifier trained on multispeaker large-scale data can guide unconditional DDPMs for various speakers to perform TTS.

## item_id: m_3427

TITLE: HyperDet: Generalizable Detection of Synthesized Images by Generating and Merging A Mixture of Hyper LoRAs

ABSTRACT: The emergence of diverse generative vision models has recently enabled the synthesis of visually realistic images, underscoring the critical need for effectively detecting these generated images from real photos. Despite advances in this field, existing detection approaches often struggle to accurately identify synthesized images generated by different generative models. In this work, we introduce a novel and generalizable detection framework termed HyperDet, which innovatively captures and integrates shared knowledge from a collection of functionally distinct and lightweight expert detectors. HyperDet leverages a large pretrained vision model to extract general detection features while simultaneously capturing and enhancing task-specific features. To achieve this, HyperDet first groups SRM filters into five distinct groups to efficiently capture varying levels of pixel artifacts based on their different functionality and complexity. Then, HyperDet utilizes a hypernetwork to generate LoRA model weights with distinct embedding parameters. Finally, we merge the LoRA networks to form an efficient model ensemble. Also, we propose a novel objective function that balances the pixel and semantic artifacts effectively. Extensive experiments on the UnivFD and Fake2M datasets demonstrate the effectiveness of our approach, achieving state-of-the-art performance. Moreover, our work paves a new way to establish generalizable domain-specific fake image detectors based on pretrained large vision models. {Our codes are available at \url{https://anonymous.4open.science/r/HyperDet-3053}}.

## item_id: m_3428

TITLE: Enforcing constraints on outputs with unconstrained inference

ABSTRACT:   Increasingly, practitioners apply neural networks to complex
  problems in natural language processing (NLP), such as syntactic
  parsing, that have rich output structures. Many such applications
  require deterministic constraints on the output values; for example,
  requiring that the sequential outputs encode a valid tree. While
  hidden units might capture such properties, the network is not
  always able to learn them from the training data alone, and
  practitioners must then resort to post-processing. In this paper, we
  present an inference method for neural networks that enforces
  deterministic constraints on outputs without performing
  post-processing or expensive discrete search over the feasible
  space. Instead, for each input, we nudge the continuous weights
  until the network's unconstrained inference procedure generates an
  output that satisfies the constraints. We find that our method
  reduces the number of violating outputs by up to 81\%, while
  improving accuracy.

## item_id: m_3429

TITLE: Identifying Generalization Properties in Neural Networks

ABSTRACT: While it has not yet been proven, empirical evidence suggests that model generalization is related to local properties of the optima which can be described via the Hessian. We connect model generalization with the local property of a solution under the PAC-Bayes paradigm. In particular, we prove that model generalization ability is related to the Hessian, the higher-order "smoothness" terms characterized by the Lipschitz constant of the Hessian, and the scales of the parameters. Guided by the proof, we propose a metric to score the generalization capability of the model, as well as an algorithm that optimizes the perturbed model accordingly. 

## item_id: m_3430

TITLE: EVaDE : Event-Based Variational Thompson Sampling for Model-Based Reinforcement Learning

ABSTRACT: Posterior Sampling for Reinforcement Learning (PSRL) is a well-known algorithm that augments model-based reinforcement learning (MBRL) algorithms with Thompson sampling. PSRL maintains posterior distributions of the environment transition dynamics and the reward function to procure posterior samples that are used to generate data for training the controller. Maintaining posterior distributions over all possible transition and reward functions for tasks with high dimensional state and action spaces is intractable. Recent works show that dropout used in conjunction with neural networks induce variational distributions that can approximate these posteriors.  In this paper, we propose Event-based Variational Distributions for Exploration (EVaDE), variational distributions that are useful for MBRL, especially when the underlying domain is object-based. We leverage the general domain knowledge of object-based domains to design three types of event-based convolutional layers to direct exploration, namely the noisy event interaction layer, the noisy event weighting layer and the noisy event translation layer respectively. These layers rely on Gaussian dropouts and are inserted in between the layers of the deep neural network model to help facilitate variational Thompson sampling. We empirically show the effectiveness of EVaDE equipped Simulated Policy Learning (SimPLe) on a randomly selected suite of Atari games, where the number of agent environment interactions is limited to 100K. 

## item_id: m_3431

TITLE: A Robust Fuel Optimization Strategy For Hybrid Electric Vehicles: A Deep Reinforcement Learning Based Continuous Time Design Approach

ABSTRACT: This paper deals with the fuel optimization problem for hybrid electric vehicles in reinforcement learning framework. Firstly, considering the hybrid electric vehicle as a completely observable non-linear system with uncertain dynamics, we solve an open-loop  deterministic optimization problem. This is followed by the design of a  deep reinforcement learning based optimal controller for the non-linear system using concurrent learning based system identifier such that the actual states and the control policy are able to track the optimal trajectory and optimal policy, autonomously even in the presence of external disturbances, modeling errors, uncertainties and noise and signigicantly reducing the computational complexity at the same time, which is in sharp contrast to the conventional methods like PID and Model Predictive Control (MPC) as well as traditional RL approaches like ADP, DDP and DQN that mostly depend on a set of pre-defined rules and provide sub-optimal solutions under similar conditions. The low value of the H-infinity ($H_{\infty})$ performance index of the proposed optimization algorithm addresses the robustness issue. The optimization technique thus proposed is compared with the traditional fuel optimization strategies for hybrid electric vehicles to illustate the efficacy of the proposed method.

## item_id: m_3432

TITLE: NEWSQA: A MACHINE COMPREHENSION DATASET

ABSTRACT: We present NewsQA, a challenging machine comprehension dataset of over 100,000 question-answer pairs. Crowdworkers supply questions and answers based on a set of over 10,000 news articles from CNN, with answers consisting in spans of text from the corresponding articles. We collect this dataset through a four- stage process designed to solicit exploratory questions that require reasoning. A thorough analysis confirms that NewsQA demands abilities beyond simple word matching and recognizing entailment. We measure human performance on the dataset and compare it to several strong neural models. The performance gap between humans and machines (25.3% F1) indicates that significant progress can be made on NewsQA through future research. The dataset is freely available at datasets.maluuba.com/NewsQA.

## item_id: m_3433

TITLE: Safety Alignment Should be Made More Than Just a Few Tokens Deep

ABSTRACT: The safety alignment of current Large Language Models (LLMs) is vulnerable. Simple attacks, or even benign fine-tuning, can jailbreak aligned models. We note that many of these vulnerabilities are related to a shared underlying issue: safety alignment can take shortcuts, wherein the alignment adapts a model's generative distribution primarily over only its very first few output tokens. We unifiedly refer to this issue as shallow safety alignment. In this paper, we present case studies to explain why shallow safety alignment can exist and show how this issue universally contributes to multiple recently discovered vulnerabilities in LLMs, including the susceptibility to adversarial suffix attacks, prefilling attacks, decoding parameter attacks, and fine-tuning attacks. The key contribution of this work is that we demonstrate how this consolidated notion of shallow safety alignment sheds light on promising research directions for mitigating these vulnerabilities. We show that deepening the safety alignment beyond the first few tokens can meaningfully improve robustness against some common exploits. We also design a regularized fine-tuning objective that makes the safety alignment more persistent against fine-tuning attacks by constraining updates on initial tokens. Overall, we advocate that future safety alignment should be made more than just a few tokens deep.

## item_id: m_3434

TITLE: Learning to Act by Predicting the Future

ABSTRACT: We present an approach to sensorimotor control in immersive environments. Our approach utilizes a high-dimensional sensory stream and a lower-dimensional measurement stream. The cotemporal structure of these streams provides a rich supervisory signal, which enables training a sensorimotor control model by interacting with the environment. The model is trained using supervised learning techniques, but without extraneous supervision. It learns to act based on raw sensory input from a complex three-dimensional environment. The presented formulation enables learning without a fixed goal at training time, and pursuing dynamically changing goals at test time. We conduct extensive experiments in three-dimensional simulations based on the classical first-person game Doom. The results demonstrate that the presented approach outperforms sophisticated prior formulations, particularly on challenging tasks. The results also show that trained models successfully generalize across environments and goals. A model trained using the presented approach won the Full Deathmatch track of the Visual Doom AI Competition, which was held in previously unseen environments.

## item_id: m_3435

TITLE: SCALE-UP: An Efficient Black-box Input-level Backdoor Detection via Analyzing Scaled Prediction Consistency

ABSTRACT: Deep neural networks (DNNs) are vulnerable to backdoor attacks, where adversaries embed a hidden backdoor trigger during the training process for malicious prediction manipulation. These attacks pose great threats to the applications of DNNs under the real-world machine learning as a service (MLaaS) setting, where the deployed model is fully black-box while the users can only query and obtain its predictions. Currently, there are many existing defenses to reduce backdoor threats. However, almost all of them cannot be adopted in MLaaS scenarios since they require getting access to or even modifying the suspicious models. In this paper, we propose a simple yet effective black-box input-level backdoor detection, called SCALE-UP, which requires only the predicted labels to alleviate this problem. Specifically, we identify and filter malicious testing samples by analyzing their prediction consistency during the pixel-wise amplification process. Our defense is motivated by an intriguing observation (dubbed \emph{scaled prediction consistency}) that the predictions of poisoned samples are significantly more consistent compared to those of benign ones when amplifying all pixel values. Besides, we also provide theoretical foundations to explain this phenomenon. Extensive experiments are conducted on benchmark datasets, verifying the effectiveness and efficiency of our defense and its resistance to potential adaptive attacks. Our codes are available at \url{https://github.com/JunfengGo/SCALE-UP}.

## item_id: m_3436

TITLE: Flow Annealed Importance Sampling Bootstrap

ABSTRACT: Normalizing flows are tractable density models that can approximate complicated target distributions, e.g. Boltzmann distributions of physical systems. However, current methods for training flows either suffer from mode-seeking behavior, use samples from the target generated beforehand by expensive MCMC methods, or use stochastic losses that have high variance. To avoid these problems, we augment flows with annealed importance sampling (AIS) and minimize the mass-covering $\alpha$-divergence with $\alpha=2$, which minimizes importance weight variance. Our method, Flow AIS Bootstrap (FAB), uses AIS to generate samples in regions where the flow is a poor approximation of the target, facilitating the discovery of new modes. We apply FAB to multimodal targets and show that we can approximate them very accurately where previous methods fail. To the best of our knowledge, we are the first to learn the Boltzmann distribution of the alanine dipeptide molecule using only the unnormalized target density, without access to samples generated via Molecular Dynamics (MD) simulations: FAB produces better results than training via maximum likelihood on MD samples while using 100 times fewer target evaluations. After reweighting the samples, we obtain unbiased histograms of dihedral angles that are almost identical to the ground truth.

## item_id: m_3437

TITLE: Learning a neural response metric for retinal prosthesis

ABSTRACT: Retinal prostheses for treating incurable blindness are designed to electrically stimulate surviving retinal neurons,  causing them to send artificial visual signals to the brain. However, electrical stimulation generally cannot precisely reproduce  normal patterns of neural activity in the retina. Therefore, an electrical stimulus must be selected that produces a neural response as close as possible to the desired response. This requires a technique for computing a distance between the desired response and the achievable response that is meaningful in terms of the visual signal being conveyed. Here we propose a method to learn such a metric on neural responses, directly from recorded light responses of a population of retinal ganglion cells (RGCs) in the primate retina. The learned metric produces a measure of similarity of RGC population responses that accurately reflects the similarity of the visual input. Using data from electrical stimulation experiments, we demonstrate that this metric may improve the performance of a prosthesis.

## item_id: m_3438

TITLE: Learning to Play in a Day: Faster Deep Reinforcement Learning by Optimality Tightening

ABSTRACT: We propose a novel training algorithm for reinforcement learning which combines the strength of deep Q-learning with a constrained optimization approach to tighten optimality and encourage faster reward propagation. Our novel technique makes deep reinforcement learning more practical by drastically reducing the training time.  We evaluate the performance of our approach on the 49 games of the challenging Arcade  Learning Environment, and report significant improvements in both training time and accuracy.

## item_id: m_3439

TITLE: Reinforced active learning for image segmentation

ABSTRACT: Learning-based approaches for semantic segmentation have two inherent challenges. First, acquiring pixel-wise labels is expensive and time-consuming. Second, realistic segmentation datasets are highly unbalanced: some categories are much more abundant than others, biasing the performance to the most represented ones. In this paper, we are interested in focusing human labelling effort on a small subset of a larger pool of data, minimizing this effort while maximizing performance of a segmentation model on a hold-out set. We present a new active learning strategy for semantic segmentation based on deep reinforcement learning (RL). An agent learns a policy to select a subset of small informative image regions -- opposed to entire images -- to be labeled, from a pool of unlabeled data. The region selection decision is made based on predictions and uncertainties of the segmentation model being trained. Our method proposes a new modification of the deep Q-network (DQN) formulation for active learning, adapting it to the large-scale nature of semantic segmentation problems. We test the proof of concept in CamVid and provide results in the large-scale dataset Cityscapes. On Cityscapes, our deep RL region-based DQN approach requires roughly 30% less additional labeled data than our most competitive baseline to reach the same performance. Moreover, we find that our method asks for more labels of under-represented categories compared to the baselines, improving their performance and helping to mitigate class imbalance.

## item_id: m_3440

TITLE: Fairness with Wasserstein Adversarial Networks

ABSTRACT: Quantifying, enforcing and implementing fairness emerged as a major topic in machine learning. We investigate these questions in the context of deep learning. Our main algorithmic and theoretical tool is the computational estimation of similarities between probability, ``\`a la Wasserstein'', using adversarial networks. This idea is flexible enough to investigate different fairness constrained learning tasks, which we model by specifying properties of the underlying data generative process. The first setting considers bias in the generative model which should be filtered out. The second model is related to the presence of nuisance variables in the observations producing an unwanted bias for the learning task.  For both models, we devise a learning algorithm based on approximation of Wasserstein distances using adversarial networks. We provide formal arguments describing the fairness enforcing properties of these algorithm in relation with the underlying fairness generative processes. Finally we perform experiments, both on synthetic and real world data, to demonstrate empirically the superiority of our approach compared to state of the art fairness algorithms as well as concurrent GAN type adversarial architectures based on Jensen divergence.

## item_id: m_3441

TITLE: Hyperbolic Deep Reinforcement Learning

ABSTRACT: In deep reinforcement learning (RL), useful information about the state is inherently tied to its possible future successors. Consequently, encoding features that capture the hierarchical relationships between states into the model's latent representations is often conducive to recovering effective policies. In this work, we study a new class of deep RL algorithms that promote encoding such relationships by using hyperbolic space to model latent representations. However, we find that a naive application of existing methodology from the hyperbolic deep learning literature leads to fatal instabilities due to the non-stationarity and variance characterizing common gradient estimators in RL. Hence, we design a new general method that directly addresses such optimization challenges and enables stable end-to-end learning with deep hyperbolic representations. We empirically validate our framework by applying it to popular on-policy and off-policy RL algorithms on the Procgen and Atari 100K benchmarks, attaining near universal performance and generalization benefits. Given its natural fit, we hope this work will inspire future RL research to consider hyperbolic representations as a standard tool.

## item_id: m_3442

TITLE: Leveraging Grammar and Reinforcement Learning for Neural Program Synthesis

ABSTRACT: Program synthesis is the task of automatically generating a program consistent with
a specification. Recent years have seen proposal of a number of neural approaches
for program synthesis, many of which adopt a sequence generation paradigm similar
to neural machine translation, in which sequence-to-sequence models are trained to
maximize the likelihood of known reference programs. While achieving impressive
results, this strategy has two key limitations. First, it ignores Program Aliasing: the
fact that many different programs may satisfy a given specification (especially with
incomplete specifications such as a few input-output examples). By maximizing
the likelihood of only a single reference program, it penalizes many semantically
correct programs, which can adversely affect the synthesizer performance. Second,
this strategy overlooks the fact that programs have a strict syntax that can be
efficiently checked. To address the first limitation, we perform reinforcement
learning on top of a supervised model with an objective that explicitly maximizes
the likelihood of generating semantically correct programs. For addressing the
second limitation, we introduce a training procedure that directly maximizes the
probability of generating syntactically correct programs that fulfill the specification.
We show that our contributions lead to improved accuracy of the models, especially
in cases where the training data is limited.

## item_id: m_3443

TITLE: AUTOMATA GUIDED HIERARCHICAL REINFORCEMENT LEARNING FOR ZERO-SHOT SKILL COMPOSITION

ABSTRACT: An obstacle that prevents the wide adoption of (deep) reinforcement learning (RL) in control systems is its need for a large number of interactions with the environment in order to master a skill. The learned skill usually generalizes poorly across domains and re-training is often necessary when presented with a new task. We present a framework that combines techniques in \textit{formal methods} with \textit{hierarchical reinforcement learning} (HRL). The set of techniques we provide allows for the convenient specification of tasks with logical expressions, learns hierarchical policies (meta-controller and low-level controllers) with well-defined intrinsic rewards using any RL methods and is able to construct new skills from existing ones without additional learning. We evaluate the proposed methods in a simple grid world simulation as well as simulation on a Baxter robot. 

## item_id: m_3444

TITLE: On the Adversarial Robustness against Natural Weather Perturbations

ABSTRACT: Several algorithms are proposed to improve the robustness of deep neural networks against adversarial perturbations beyond $\ell_p$ cases, i.e. weather perturbations. However, evaluations of existing robust training algorithms are over-optimistic. This is in part due to the lack of a standardized evaluation protocol across various robust training algorithms, leading to ad-hoc methods that test robustness on either random perturbations or the adversarial samples from generative models that are used for robust training, which is either uninformative of the worst case, or is heavily biased.
In this paper, we identify such evaluation bias in these existing works and propose the first standardized and fair evaluation that compares various robust training algorithms by using physics simulators for common adverse weather effects i.e. rain and snow. Additionally, our framework identified the lack of diversity in existing robust training algorithms. As a step to address this, we propose a light-weight generative adversarial network (GAN) with improved diverse weather effects controlled by latent codes that can be used in robust training.
The proposed robust training algorithm is evaluated on two streetview classification datasets (BIC\_GSV, Places365), where it outperforms other robust training approaches based on generative models for worst-case adversarial rain and snow attacks.

## item_id: m_3445

TITLE: The Ability of Large Language Models to Evaluate Constraint-satisfaction in Agent Responses to Open-ended Requests

ABSTRACT: Generative AI agents are often expected to respond to complex user requests that have No One Right Answer (NORA), e.g., "design a vegetarian meal plan below 1800 calories". Such requests may entail a set of constraints that the agent should adhere to. To successfully develop agents for NORA scenarios, an accurate automatic evaluation framework is essential, and specifically - one capable of validating the satisfaction of constraints in the agent's response. Recently, large language models (LLMs) have been adopted as versatile evaluators for many NORA tasks, but their ability to evaluate constraint-satisfaction in generated text remains unclear. To study this, we develop and release a novel Arithmetic Constraint-Satisfaction (ACS) benchmarking dataset. The dataset consists of complex user requests with corresponding constraints, agent responses and human labels indicating each constraint's satisfaction level in the response. A unique property of this dataset is that validating many of its constraints requires reviewing the response as a whole (in contrast to many other benchmarks that require the validation of a single independent item). Moreover, it assesses LLMs in performing reasoning, in-context data extraction, arithmetic calculations, and counting. We then benchmark both open and proprietary LLMs on evaluating constraint-satisfaction, and show that most models still have a significant headroom for improvement, and that errors primarily stem from reasoning issues. In addition, most models exhibit a skewed constraint-satisfaction prediction pattern, with higher accuracy where the ground-truth label is "satisfied". Lastly, few-shot prompting for our task proved to be rather challenging, since many of the studied models showed a degradation in performance when it was introduced.

## item_id: m_3446

TITLE: Differentiable Learning-to-Normalize via Switchable Normalization

ABSTRACT: We address a learning-to-normalize problem by proposing Switchable Normalization (SN), which learns to select different normalizers for different normalization layers of a deep neural network. SN employs three distinct scopes to compute statistics (means and variances) including a channel, a layer, and a minibatch. SN switches between them by learning their importance weights in an end-to-end manner. It has several good properties. First, it adapts to various network architectures and tasks (see Fig.1). Second, it is robust to a wide range of batch sizes, maintaining high performance even when small minibatch is presented (e.g. 2 images/GPU). Third, SN does not have sensitive hyper-parameter, unlike group normalization that searches the number of groups as a hyper-parameter. Without bells and whistles, SN outperforms its counterparts on various challenging benchmarks, such as ImageNet, COCO, CityScapes, ADE20K, and Kinetics. Analyses of SN are also presented. We hope SN will help ease the usage and understand the normalization techniques in deep learning. The code of SN will be released.

## item_id: m_3447

TITLE: Self-Supervised Variational Auto-Encoders

ABSTRACT: Density estimation, compression, and data generation are crucial tasks in artificial intelligence. Variational Auto-Encoders (VAEs) constitute a single framework to achieve these goals. Here, we present a novel class of generative models, called self-supervised Variational Auto-Encoder (selfVAE), that utilizes deterministic and discrete transformations of data. This class of models allows performing both conditional and unconditional sampling while simplifying the objective function. First, we use a single self-supervised transformation as a latent variable, where a transformation is either downscaling or edge detection. Next, we consider a hierarchical architecture, i.e., multiple transformations, and we show its benefits compared to the VAE. The flexibility of selfVAE in data reconstruction finds a particularly interesting use case in data compression tasks, where we can trade-off memory for better data quality, and vice-versa. We present the performance of our approach on three benchmark image data (Cifar10, Imagenette64, and CelebA).

## item_id: m_3448

TITLE: Visual Reasoning by Progressive Module Networks

ABSTRACT: Humans learn to solve tasks of increasing complexity by building on top of previously acquired knowledge. Typically, there exists a natural progression in the tasks that we learn – most do not require completely independent solutions, but can be broken down into simpler subtasks. We propose to represent a solver for each task as a neural module that calls existing modules (solvers for simpler tasks) in a functional program-like manner. Lower modules are a black box to the calling module, and communicate only via a query and an output. Thus, a module for a new task learns to query existing modules and composes their outputs in order to produce its own output. Our model effectively combines previous skill-sets, does not suffer from forgetting, and is fully differentiable. We test our model in learning a set of visual reasoning tasks, and demonstrate improved performances in all tasks by learning progressively. By evaluating the reasoning process using human judges, we show that our model is more interpretable than an attention-based baseline.


## item_id: m_3449

TITLE: Quantized Optimistic Dual Averaging with Adaptive Layer-wise Compression

ABSTRACT: We develop a general layer-wise and adaptive compression framework with applications to solving variational inequality problems (VI) in a large-scale and distributed setting where multiple nodes have access to local stochastic dual vectors. This framework encompasses a broad range of applications, spanning from distributed optimization to games. We establish tight error bounds and code-length bounds for adaptive layer-wise quantization that generalize  previous bounds for global quantization. We also propose Quantized and Generalized Optimistic Dual Averaging (QODA) with adaptive learning rates, which achieves optimal rate of convergence for distributed monotone VIs. We empirically show that the adaptive layer-wise compression achieves up to a 150% speedup in end-to-end training time for training Wasserstein GAN on 12+ GPUs.

## item_id: m_3450

TITLE: Video Action Segmentation with Hybrid Temporal Networks

ABSTRACT: Action segmentation as a milestone towards building automatic systems to understand untrimmed videos has received considerable attention in the recent years. It is typically being modeled as a sequence labeling problem but contains intrinsic and sufficient differences than text parsing or speech processing. In this paper, we introduce a novel hybrid temporal convolutional and recurrent network (TricorNet), which has an encoder-decoder architecture: the encoder consists of a hierarchy of temporal convolutional kernels that capture the local motion changes of different actions; the decoder is a hierarchy of recurrent neural networks that are able to learn and memorize long-term action dependencies after the encoding stage. Our model is simple but extremely effective in terms of video sequence labeling. The experimental results on three public action segmentation datasets have shown that the proposed model achieves superior performance over the state of the art.

## item_id: m_3451

TITLE: Laconic Image Classification: Human vs. Machine Performance

ABSTRACT: We propose laconic classification as a novel way to understand and compare the performance of diverse image classifiers. The goal in this setting is to minimise the amount of information (aka. entropy) required in individual test images to maintain correct classification. Given a classifier and a test image, we compute an approximate minimal-entropy positive image for which the classifier provides a correct classification, becoming incorrect upon any further reduction. The notion of entropy offers a unifying metric that allows to combine and compare the effects of various types of reductions (e.g., crop, colour reduction, resolution reduction) on classification performance, in turn generalising similar methods explored in previous works. Proposing two complementary frameworks for computing the minimal-entropy positive images of both human and machine classifiers, in experiments over the ILSVRC test-set, we find that machine classifiers are more sensitive entropy-wise to reduced resolution (versus cropping or reduced colour for machines, as well as reduced resolution for humans), supporting recent results suggesting a texture bias in the ILSVRC-trained models used. We also find, in the evaluated setting, that humans classify the minimal-entropy positive images of machine models with higher precision than machines classify those of humans.

## item_id: m_3452

TITLE: Robust LLM Unlearning via Post Judgment and Multi-round Thinking

ABSTRACT: The unlearning capability of LLMs is vital for ensuring compliance and safety, especially when removing sensitive knowledge from deployed models. Pre-filtering methods, enabling rapid deployment without parameter changes, are a prominent unlearning approach. However, they exhibit significant robustness deficiencies against adversarial attacks: in the worst case, simple prefix attacks can induce up to a 1,150-fold surge in information leakage for fictitious entity knowledge, while composite question attacks can cause accuracy on hazardous knowledge to rebound from the 24.9% random-guess baseline to as high as 67.0%. To address this, we propose a new unlearning framework via post judgment and multi-round thinking (PoRT), which consists of three key modules. First, a data cleaning module compiles a dynamic few-shot prompt that instructs the LLM to simultaneously generate both a cleaned version of the user's query and a corresponding initial response, supported by an extensible demonstration library for adaptive defense. Second, unlike existing pre-filtering methods that typically judge based solely on prompts, our post-judgment module jointly evaluates cleaned prompts and their corresponding responses to better detect non-compliant outputs. Finally, a selective multi-round thinking process is employed to trigger LLM's self-correction for low-confidence outputs, enhancing reliability and result quality. Extensive experiments on benchmarks demonstrate PoRT's superior robustness against adversarial attacks and strong unlearning effectiveness without compromising general model utility. Code is available at https://github.com/ChnIRuI/PoRT_LLM_Unlearning

## item_id: m_3453

TITLE: Adversarial examples for generative models

ABSTRACT: We explore methods of producing adversarial examples on deep generative models such as the variational autoencoder (VAE) and the VAE-GAN. Deep learning architectures are known to be vulnerable to adversarial examples, but previous work has focused on the application of adversarial examples to classification tasks. Deep generative models have recently become popular due to their ability to model input data distributions and generate realistic examples from those distributions. We present three classes of attacks on the VAE and VAE-GAN architectures and demonstrate them against networks trained on MNIST, SVHN and CelebA. Our first attack leverages classification-based adversaries by attaching a classifier to the trained encoder of the target generative model, which can then be used to indirectly manipulate the latent representation. Our second attack directly uses the VAE loss function to generate a target reconstruction image from the adversarial example. Our third attack moves beyond relying on classification or the standard loss for the gradient and directly optimizes against differences in source and target latent representations. We also motivate why an attacker might be interested in deploying such techniques against a target generative network.

## item_id: m_3454

TITLE: MxPool: Multiplex Pooling for Hierarchical Graph Representation Learning

ABSTRACT: Graphs are known to have complicated structures and have myriad applications. How to utilize deep learning methods for graph classification tasks has attracted considerable research attention in the past few years. Two properties of graph data have imposed significant challenges on existing graph learning techniques. (1) Diversity: each graph has a variable size of unordered nodes and diverse node/edge types. (2) Complexity: graphs have not only node/edge features but also complex topological features. These two properties motivate us to use multiplex structure to learn graph features in a diverse way. In this paper, we propose a simple but effective approach, MxPool, which concurrently uses multiple graph convolution networks and graph pooling networks to build hierarchical learning structure for graph representation learning tasks. Our experiments on numerous graph classification benchmarks show that our MxPool has marked superiority over other state-of-the-art graph representation learning methods. For example, MxPool achieves 92.1% accuracy on the D&D dataset while the second best method DiffPool only achieves 80.64% accuracy.

## item_id: m_3455

TITLE: Complex- and Real-Valued Neural Network Architectures

ABSTRACT: Complex-value neural networks are not a new concept, however, the use of real-values has often been favoured over complex-values due to difficulties in training and accuracy of results. Existing literature ignores the number of parameters used. We compared complex- and real-valued neural networks using five activation functions. We found that when real and complex neural networks are compared using simple classification tasks, complex neural networks perform equal to or slightly worse than real-value neural networks. However, when specialised architecture is used, complex-valued neural networks outperform real-valued neural networks. Therefore, complex–valued neural networks should be used when the input data is also complex or it can be meaningfully to the complex plane,  or when the network architecture uses the structure defined by using complex numbers.

## item_id: m_3456

TITLE: In Search of the Long-Tail: Systematic Generation of Long-Tail Knowledge via Logical Rule Induced Search

ABSTRACT: Since large language models (LLMs) have approached human-level performance on many tasks, it has become increasingly harder for researchers to find tasks that are still challenging to the models. Failure cases usually come from the long-tail distribution -- data to which an oracle language model could assign a probability on the lower end of its distribution. Systematically finding evaluation data in the long-tail distribution is important, but current methodology such as prompt engineering or crowdsourcing are insufficient because coming up with long-tail examples is also hard for humans due to our cognitive bias. In this paper, we propose a Logic-Induced-Knowledge-Search (LINK) framework for systematically generating long-tail knowledge statements. Grounded by a symbolic logic rule, we search for long-tail values for each variable of the rule by first prompting a large language model, then verifying the correctness of the values with a critic, and lastly pushing for the long-tail distribution with a reranker. Using this framework we construct a dataset, Logic-Induced-Long-Tail (LINT [https://doi.org/10.5281/zenodo.8384878]), consisting of 200 symbolic rules and 40K knowledge statements spanning across four different domains. Human annotations find that 89% of the statements in LINT are factually correct. In contrast, ChatGPT and GPT4 struggle with directly generating long-tail statements under the guidance of logic rules, each only getting 61% and 79% of their statements correct. Moreover, their ``long-tail" generations in fact fall into the higher likelihood range, and thus are not really long-tail. Our findings suggest that LINK is effective for generating data in the long-tail distribution while enforcing quality. To demonstrate how the community can utilize LINT for systematically evaluating LLMs' capabilities in the long-tail distribution, we challenge the models with a simple entailment classification task using samples from LINT. We find that ChatGPT and GPT4 performances drop by 2% and 4% when reasoning on long-tail knowledge statements compared to on head distribution statements. We hope our work can inspire future research on generating evaluation data in the long-tail distribution.

## item_id: m_3457

TITLE: D2KE: From Distance to Kernel and Embedding via Random Features For Structured Inputs

ABSTRACT: We present a new methodology that constructs a family of \emph{positive definite kernels} from any given dissimilarity measure on structured inputs whose elements are either real-valued time series or discrete structures such as strings, histograms, and graphs. 
Our approach, which we call D2KE (from Distance to Kernel and Embedding), draws from the literature of Random Features.
However, instead of deriving random feature maps from a user-defined kernel to approximate kernel machines, we build a kernel from a random feature map, that we specify given the distance measure. 
We further propose use of a finite number of random objects to produce a random feature embedding of each instance.
We provide a theoretical analysis showing that D2KE enjoys better generalizability than universal Nearest-Neighbor estimates. 
On one hand, D2KE subsumes the widely-used \emph{representative-set method} as a special case, and relates to the well-known \emph{distance substitution kernel} in a limiting case. 
On the other hand, D2KE generalizes existing \emph{Random Features methods} applicable only to vector input representations to complex structured inputs of variable sizes. 
We conduct classification experiments over such disparate domains as time series, strings, and histograms (for texts and images), for which our proposed framework compares favorably to existing distance-based learning methods in terms of both testing accuracy and computational time.

## item_id: m_3458

TITLE: SMASH: One-Shot Model Architecture Search through HyperNetworks

ABSTRACT: Designing architectures for deep neural networks requires expert knowledge and substantial computation time. We propose a technique to accelerate architecture selection by learning an auxiliary HyperNet that generates the weights of a main model conditioned on that model's architecture. By comparing the relative validation performance of networks with HyperNet-generated weights, we can effectively search over a wide range of architectures at the cost of a single training run. To facilitate this search, we develop a flexible mechanism based on memory read-writes that allows us to define a wide range of network connectivity patterns, with ResNet, DenseNet, and FractalNet blocks as special cases. We validate our method (SMASH) on CIFAR-10 and CIFAR-100, STL-10, ModelNet10, and Imagenet32x32, achieving competitive performance with similarly-sized hand-designed networks.

## item_id: m_3459

TITLE: Latte: Latent Attention for Linear Time Transformers

ABSTRACT: The time complexity of the standard attention mechanism in transformers scales quadratically with sequence length. We propose a probabilistic framework for attention, enabling us to derive a novel low-rank linear re-parameterisation of both bidirectional and causal cases, based on defining a latent variable model. Our method can be seamlessly integrated as a drop-in replacement for the standard attention mechanism. Additionally, this framework provides a natural extension for combining local standard attention with our global linear attention. This approach allows us to extend the context length of existing large pre-trained models with only a few additional training steps. The resulting ``Latte Transformer'' achieves performance comparable to standard attention and other state-of-the-art models, while maintaining linear time and memory complexity, along with constant-time next-token prediction during inference.

## item_id: m_3460

TITLE: FAME: Formal Abstract Minimal Explanation for Neural Networks

ABSTRACT: We propose $\textbf{FAME}$ (Formal Abstract Minimal Explanations), a new class of abductive explanations grounded in abstract interpretation. FAME is the first method to scale to large neural networks while reducing explanation size. Our main contribution is the design of dedicated perturbation domains that eliminate the need for traversal order. FAME progressively shrinks these domains and leverages LiRPA-based bounds to discard irrelevant features, ultimately converging to a $\textbf{formal abstract minimal explanation}$.  To assess explanation quality, we introduce a procedure that measures the worst-case distance between an abstract minimal explanation and a true minimal explanation. This procedure combines adversarial attacks with an optional $VERI{\large X}+$ refinement step. We benchmark FAME against $VERI{\large X}+$ and demonstrate consistent gains in both explanation size and runtime on medium- to large-scale neural networks.

## item_id: m_3461

TITLE: A Sign-aware Graph Transformer with Prototypical Objectives for Signed Link Prediction

ABSTRACT: Signed link prediction focused on bipartite graphs is a fundamental task with wide-ranging applications, yet it poses significant challenges. Current Graph Neural Networks are inherently local due to their message-passing nature, preventing them from capturing the long-range dependencies crucial for accurate prediction. Furthermore, they often fail to model complex real-world data distributions characterized by severe class imbalance and rich intra-class multimodality.To overcome these limitations, we propose the Hierarchical Prototypical Contrastive Sign-aware Graph Transformer (HPC-SGT), designed specifically for the bipartite setting. At its core, our framework features a Sign-aware Graph Transformer that operates on the line graph dual, leveraging novel spectral and motif-based inductive priors to learn structurally-aware global representations. This expressive encoder is optimized via a hierarchical prototypical objective, which learns a geometrically structured embedding space. It couples a class-balanced contrastive loss to robustly handle data imbalance with clustering and separation regularizers to explicitly model multi-modal class structures. The framework is unified by a cross-view consistency mechanism that grounds the learned semantic representations in the graph's foundational topology, bridging the structure-semantics gap. Extensive experiments on challenging benchmarks, including scenarios with severe class imbalance, show that HPC-SGT significantly outperforms a wide range of state-of-the-art methods. Ablation studies further validate the contribution of each component, establishing HPC-SGT as a new, powerful, and principled solution for signed link prediction. Our code is available in the supplementary materials.

## item_id: m_3462

TITLE: Optimizing Backward Policies in GFlowNets via Trajectory Likelihood Maximization

ABSTRACT: Generative Flow Networks (GFlowNets) are a family of generative models that learn to sample objects with probabilities proportional to a given reward function. The key concept behind GFlowNets is the use of two stochastic policies: a forward policy, which incrementally constructs compositional objects, and a backward policy, which sequentially deconstructs them. Recent results show a close relationship between GFlowNet training and entropy-regularized reinforcement learning (RL) problems with a particular reward design. However, this connection applies only in the setting of a fixed backward policy, which might be a significant limitation. As a remedy to this problem, we introduce a simple backward policy optimization algorithm that involves direct maximization of the value function in an entropy-regularized Markov Decision Process (MDP) over intermediate rewards. We provide an extensive experimental evaluation of the proposed approach across various benchmarks in combination with both RL and GFlowNet algorithms and demonstrate its faster convergence and mode discovery in complex environments.

## item_id: m_3463

TITLE: On the Implicit Bias of Adam

ABSTRACT: In previous literature, backward error analysis was used to find ordinary differential equations (ODEs) approximating the gradient descent trajectory. It was found that finite step sizes implicitly regularize solutions because terms appearing in the ODEs penalize the two-norm of the loss gradients. We prove that the exis- tence of similar implicit regularization in RMSProp and Adam depends on their hyperparameters and the training stage, but with a different “norm” involved: the corresponding ODE terms either penalize the (perturbed) one-norm of the loss gradients or, on the contrary, hinder its decrease (the latter case being typical). We also conduct numerical experiments and discuss how the proven facts can influence generalization.

## item_id: m_3464

TITLE: Learning to Understand Goal Specifications by Modelling Reward

ABSTRACT: Recent work has shown that deep reinforcement-learning agents can learn to follow language-like instructions from infrequent environment rewards. However, this places on environment designers the onus of designing language-conditional reward functions which may not be easily or tractably implemented as the complexity of the environment and the language scales. To overcome this limitation, we present a framework within which instruction-conditional RL agents are trained using rewards obtained not from the environment, but from reward models which are jointly trained from expert examples.  As reward models improve, they learn to accurately reward agents for completing tasks for environment configurations---and for instructions---not present amongst the expert data. This framework effectively separates the representation of what instructions require from how they can be executed.
In a simple grid world, it enables an agent to learn a range of commands requiring interaction with blocks and understanding of spatial relations and underspecified abstract arrangements. We further show the method allows our agent to adapt to changes in the environment without requiring new expert examples.

## item_id: m_3465

TITLE: Chaos of Learning Beyond Zero-sum and Coordination via Game Decompositions

ABSTRACT: It is of primary interest for ML to understand how agents learn and interact dynamically in competitive environments and games (e.g. GANs). But this has been a difficult task, as irregular behaviors are commonly observed in such systems. This can be explained theoretically, for instance, by the works of Cheung and Piliouras (COLT 2019; NeurIPS 2020), which showed that in two-person zero-sum games, if agents employ one of the most well-known learning algorithms, Multiplicative Weights Update (MWU), then Lyapunov chaos occurs everywhere in the payoff space. In this paper, we study how persistent chaos can occur in the more general normal game settings, where the agents might have the motivation to coordinate (which is not true for zero-sum games) and the number of agents can be arbitrary.

We characterize bimatrix games where MWU, its optimistic variant (OMWU) or Follow-the-Regularized-Leader (FTRL) algorithms are Lyapunov chaotic almost everywhere in the payoff space. Technically, our characterization is derived by extending the volume-expansion argument of Cheung and Piliouras via the canonical game decomposition into zero-sum and coordination components. Interestingly, the two components induce opposite volume-changing behaviors, so the overall behavior can be analyzed by comparing the strengths of the components against each other. The comparison is done via our new notion of "matrix domination" or via a linear program. For multi-player games, we present a local equivalence of volume change between general games and graphical games, which is used to perform volume and chaos analyses of MWU and OMWU in potential games.

## item_id: m_3466

TITLE: Semantic Video Synthesis from Video Scene Graphs

ABSTRACT: Video synthesis has recently attracted a lot of attention, as the natural extension to the image synthesis task. Most image synthesis works use class labels or text as guidance. However, neither labels nor text can provide explicit temporal guidance, such as when action starts or ends. To overcome this limitation, we introduce video scene graphs as input for video synthesis, as they represent the spatial and temporal relationships between objects in the scene. Since video scene graphs are usually temporally discrete annotations, we propose a video scene graph (VSG) encoder that not only encodes the existing video scene graphs but also predicts the graph representations for unlabeled frames. The VSG encoder is pre-trained with different contrastive multi-modal losses. A video scene graph-to-video synthesis framework (SGVS) based on the pre-trained VSG encoder, VQ-VAE, and auto-regressive Transformer is proposed to synthesize a semantic video given an initial scene image and a non-fixed number of video scene graphs. We evaluate SGVS and other state-of-the-art video synthesis models on Action Genome dataset and demonstrate the positive significance of video scene graphs in video synthesis.

## item_id: m_3467

TITLE: On the Convergence of Projected Alternating Maximization for Equitable and Optimal Transport

ABSTRACT: This paper studies the equitable and optimal transport (EOT) problem, which has many applications such as fair division problems and optimal transport with multiple agents etc. In the discrete distributions case, the EOT problem can be formulated as a linear program (LP). Since this LP is prohibitively large for general LP solvers, Scetbon \etal suggests to perturb the problem by adding an entropy regularization. They proposed a projected alternating maximization algorithm (PAM) to solve the dual of the entropy regularized EOT. In this paper, we provide the first convergence analysis of PAM. A novel rounding procedure is proposed to help construct the primal solution for the original EOT problem. We also propose a variant of PAM by incorporating the extrapolation technique that can numerically improve the performance of PAM. Results in this paper may shed lights on block coordinate (gradient) descent methods for general optimization problems. 

## item_id: m_3468

TITLE: Augmented Cyclic Adversarial Learning for Low Resource Domain Adaptation

ABSTRACT: Training a model to perform a task typically requires a large amount of data from the domains in which the task will be applied.
However, it is often the case that data are abundant in some domains but scarce in others. Domain adaptation deals with the challenge of adapting a model trained from a data-rich source domain to perform well in a data-poor target domain. In general, this requires learning plausible mappings between domains. CycleGAN is a powerful framework that efficiently learns to map inputs from one domain to another using adversarial training and a cycle-consistency constraint. However, the conventional approach of enforcing cycle-consistency via reconstruction may be overly restrictive in cases where one or more domains have limited training data. In this paper, we propose an augmented cyclic adversarial learning model that enforces the cycle-consistency constraint via an external task specific model, which encourages the preservation of task-relevant content as opposed to exact reconstruction. We explore digit classification in a low-resource setting in supervised, semi and unsupervised situation, as well as high resource unsupervised. In low-resource supervised setting, the results show that our approach improves absolute performance by 14% and 4% when adapting SVHN to MNIST and vice versa, respectively, which outperforms unsupervised domain adaptation methods that require high-resource unlabeled target domain.  Moreover, using only few unsupervised target data, our approach can still outperforms many high-resource unsupervised models. Our model also outperforms on USPS to MNIST and synthetic digit to SVHN for high resource unsupervised adaptation. In speech domains, we similarly adopt a speech recognition model from each domain as the task specific model. Our approach improves absolute performance of speech recognition by 2% for female speakers in the TIMIT dataset, where the majority of training samples are from male voices.

## item_id: m_3469

TITLE: Automated Generation of Multilingual Clusters for the Evaluation of Distributed Representations

ABSTRACT: We propose a language-agnostic way of automatically generating sets of semantically similar clusters of entities along with sets of "outlier" elements, which may then be used to perform an intrinsic evaluation of word embeddings in the outlier detection task. We used our methodology to create a gold-standard dataset, which we call WikiSem500, and evaluated multiple state-of-the-art embeddings. The results show a correlation between performance on this dataset and performance on sentiment analysis.

## item_id: m_3470

TITLE: Decoupling Concept Bottleneck Model

ABSTRACT: Concept Bottleneck Model (CBM) is a kind of powerful interpretable neural network, which utilizes high-level concepts to explain model decisions and interact with humans. However, CBM cannot always work as expected due to the troublesome collection and commonplace insufficiency of high-level concepts in real-world scenarios. In this paper, we theoretically reveal that insufficient concept information will induce the mixture of explicit and implicit information, which further leads to the inherent dilemma of concept and label distortions in CBM. Motivated by the proposed theorem, we present Decoupling Concept Bottleneck Model (DCBM), a novel concept-based model decoupling heterogeneous information into explicit and implicit concepts, while still retaining high prediction performance and interpretability. Extensive experiments expose the success in the alleviation of concept/label distortions, where DCBM achieves state-of-the-art performances in both concept and label learning tasks. Especially for situations where concepts are insufficient, DCBM significantly outperforms other models based on concept bottleneck and respectively achieves error rates 24.95% and 20.09% lower than other CBMs on concept/label prediction. Moreover, to express effective human-machine interactions for DCBM, we devise two algorithms based on mutual information (MI) estimation, including forward intervention and backward rectification, which can automatically correct labels and trace back to wrong concepts. The construction of the interaction regime can be formulated as a light min-max optimization problem achieved within minutes. Multiple experiments show that such interactions can effectively promote concept/label accuracy.


## item_id: m_3471

TITLE: Noise-Resilient Quantum Neural Networks via Zero-Noise Knowledge Distillation

ABSTRACT: Quantum neural networks (QNNs) show promise for learning on noisy intermediate-scale quantum (NISQ) devices, but two-qubit gate noise remains a significant barrier to practical implementation. Zero-noise extrapolation (ZNE) reduces errors by running circuits with scaled noise levels and extrapolating to the zero-noise limit, although it needs many evaluations per input and is susceptible to time-varying noise. We propose zero-noise knowledge distillation (ZNKD), a training-time technique that involves a ZNE-augmented teacher QNN supervising a compact student QNN. Variational learning is used to optimize the student's ability to duplicate the teacher's extrapolated outputs, resulting in robustness without the need for inference extrapolation. We additionally present a formal analysis that demonstrates how robustness flows from the ZNE teacher to the distilled student, with proofs regarding noise scaling, extrapolation error, and student generalization. In dynamic-noise simulations (IBM-style $T_1/T_2$, depolarizing, readout), ZNE-guided distillation lowers student MSE by $0.06$-$0.12$ ($\approx$10-20\%) across Fashion-MNIST, AG News, UCI Wine, and UrbanSound8K, keeping students within $2\%$--$4\%$ accuracy of the teacher and achieving $6{:}2$-$8{:}3$ ratio of teacher to student.  ZNKD, which amortizes ZNE to training, provides an efficient way to drift-resilient QNNs on NISQ hardware without per-input folding or extrapolation.

## item_id: m_3472

TITLE: Offline Reinforcement Learning via Weighted $f$-divergence

ABSTRACT: One of the major challenges of offline reinforcement learning (RL) is dealing with distribution shifts that stem from the mismatch between the trained policy and the data collection policy. Prior offline RL algorithms have addressed this issue by regularizing the policy optimization with $f$-divergence between the state-action visitation distributions of the data collection policy and the optimized policy. While such regularization provides a theoretical lower bound on performance and has had some practical success, it is not affected by the optimality of state-actions and can be overly pessimistic, especially when valuable state-actions are rare in the dataset. To mitigate the problem, we introduce and analyze a weighted $f$-divergence regularized RL framework that can less regularize valuable but rare state-actions as long as sampling error allows. This leads to an offline RL algorithm with iterative stationary distribution correction estimation while jointly re-adjusting the regularization for each state-action. We show that the presented algorithm with weighted $f$-divergence performs competitively with the state-of-the-art methods.

## item_id: m_3473

TITLE: Learning Priors for Adversarial Autoencoders

ABSTRACT: Most deep latent factor models choose simple priors for simplicity, tractability
or not knowing what prior to use. Recent studies show that the choice of
the prior may have a profound effect on the expressiveness of the model,
especially when its generative network has limited capacity. In this paper, we propose to learn a proper prior from data for adversarial autoencoders
(AAEs). We introduce the notion of code generators to transform manually selected
simple priors into ones that can better characterize the data distribution. Experimental results show that the proposed model can generate better image quality and learn better disentangled representations than
AAEs in both supervised and unsupervised settings. Lastly, we present its
ability to do cross-domain translation in a  text-to-image synthesis task.

## item_id: m_3474

TITLE: Consistent Instance Classification for Unsupervised Representation Learning

ABSTRACT: In this paper, we address the problem of learning the representations from images without human annotations. We study the instance classification solution, which regards each instance as a category, and improve the optimization and feature quality. The proposed consistent instance classification (ConIC) approach simultaneously optimizes the classification loss and an additional consistency loss explicitly penalizing the feature dissimilarity between the augmented views from the same instance. The benefit of optimizing the consistency loss is that the learned features for augmented views from the same instance are more compact and accordingly the classification loss optimization becomes easier, thus boosting the quality of the learned representations. This differs from InstDisc and MoCo that use an estimated prototype as the classifier weight to ease the optimization. Different from SimCLR that directly compares different instances, our approach does not require large batch size. Experimental results demonstrate competitive performance for linear evaluation and better performance than InstDisc, MoCo and SimCLR at downstream tasks, such as detection and segmentation, as well as competitive or superior performance compared to other methods with stronger training setting.

## item_id: m_3475

TITLE: Avoiding degradation in deep feed-forward networks by phasing out skip-connections

ABSTRACT: A widely observed phenomenon in deep learning is the degradation problem: increasing
the depth of a network leads to a decrease in performance on both test and training data. Novel architectures such as ResNets and Highway networks have addressed this issue by introducing various flavors of skip-connections or gating mechanisms. However, the degradation problem persists in the context of plain feed-forward networks. In this work we propose a simple method to address this issue. The proposed method poses the learning of weights in deep networks as a constrained optimization problem where the presence of skip-connections is penalized by Lagrange multipliers. This allows for skip-connections to be introduced during the early stages of training and subsequently phased out in a principled manner. We demonstrate the benefits of such an approach with experiments on MNIST, fashion-MNIST, CIFAR-10 and CIFAR-100 where the proposed method is shown to greatly decrease the degradation effect (compared to plain networks) and is often competitive with ResNets.

## item_id: m_3476

TITLE: Consequentialist conditional cooperation in social dilemmas with imperfect information

ABSTRACT: Social dilemmas, where mutual cooperation can lead to high payoffs but participants face incentives to cheat, are ubiquitous in multi-agent interaction. We wish to construct agents that cooperate with pure cooperators, avoid exploitation by pure defectors, and incentivize cooperation from the rest. However, often the actions taken by a partner are (partially) unobserved or the consequences of individual actions are hard to predict. We show that in a large class of games good strategies can be constructed by conditioning one's behavior solely on outcomes (ie. one's past rewards). We call this consequentialist conditional cooperation. We show how to construct such strategies using deep reinforcement learning techniques and demonstrate, both analytically and experimentally, that they are effective in social dilemmas beyond simple matrix games. We also show the limitations of relying purely on consequences and discuss the need for understanding both the consequences of and the intentions behind an action.

## item_id: m_3477

TITLE: Schur's Positive-Definite Network: Deep Learning in the SPD cone with structure

ABSTRACT: Estimating matrices in the symmetric positive-definite (SPD) cone is of interest for many applications ranging from computer vision to graph learning. While there exist various convex optimization-based estimators, they remain limited in expressivity due to their model-based approach. The success of deep learning motivates the use of learning-based approaches to estimate SPD matrices with neural networks in a data-driven fashion. However, designing effective neural architectures for SPD learning is challenging, particularly when the task requires
additional structural constraints, such as element-wise sparsity. Current approaches either do not ensure that the output meets all desired properties or lack expressivity. In this paper, we introduce SpodNet, a novel and generic learning module that guarantees SPD outputs and supports additional structural constraints. Notably, it solves the challenging task of learning jointly SPD and
sparse matrices. Our experiments illustrate the versatility and relevance of SpodNet layers for such applications.

## item_id: m_3478

TITLE: Learning Two-layer Neural Networks with Symmetric Inputs

ABSTRACT: We give a new algorithm for learning a two-layer neural network under a very general class of input distributions. Assuming there is a ground-truth two-layer network 
y = A \sigma(Wx) + \xi,
where A, W are weight matrices, \xi represents noise, and the number of neurons in the hidden layer is no larger than the input or output,  our algorithm is guaranteed to recover the parameters A, W of the ground-truth network. The only requirement on the input x is that it is symmetric, which still allows highly complicated and structured input. 

Our algorithm is based on the method-of-moments framework and extends several results in tensor decompositions. We use spectral algorithms to avoid the complicated non-convex optimization in learning neural networks. Experiments show that our algorithm can robustly learn the ground-truth neural network with a small number of samples for many symmetric input distributions.

## item_id: m_3479

TITLE: Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks

ABSTRACT: Recent papers have shown that neural networks obtain state-of-the-art performance on several different sequence tagging tasks. One appealing property of such systems is their generality, as excellent performance can be achieved with a unified architecture and without task-specific feature engineering.  However, it is unclear if such systems can be used for tasks without large amounts of training data. In this paper we explore the problem of transfer learning for neural sequence taggers, where a source task with plentiful annotations (e.g., POS tagging on Penn Treebank) is used to improve performance on a target task with fewer available annotations (e.g., POS tagging for microblogs). We examine the effects of transfer learning for deep hierarchical recurrent networks across domains, applications, and languages, and show that significant improvement can often be obtained.  These improvements lead to improvements over the current state-of-the-art on several well-studied tasks.

## item_id: m_3480

TITLE: Generalizable Features From Unsupervised Learning

ABSTRACT: Humans learn a predictive model of the world and use this model to reason about future events and the consequences of actions. In contrast to most machine predictors, we exhibit an impressive ability to generalize to unseen scenarios and reason intelligently in these settings.  One important aspect of this ability is physical intuition(Lake et al., 2016). In this work, we explore the potential of unsupervised learning to find features that promote better generalization to settings outside the supervised training distribution.  Our task is predicting the stability of towers of square blocks. We demonstrate that an unsupervised model, trained to predict future frames of a video sequence of stable and unstable block configurations, can yield features that support extrapolating stability prediction to blocks configurations outside the training set distribution

## item_id: m_3481

TITLE: DOMAIN-GROUNDING OF NEURAL NETWORKS FOR SPATIOTEMPORAL REASONING

ABSTRACT: Neural Networks are powerful approximators for learning to reason from raw data (e.g., pixels, text) in spatio-temporal domains (e.g., traffic-scene understanding). However, several recent studies have shown that neural networks are prone to erroneous or sometimes absurd reasoning that lacks domain-grounding (e.g., adhering to intuitive physics and causality). Incorporating comprehensive symbolic representation for domain understanding as part of a consolidated architecture offers a promising solution. In this paper, we take a dynamical systems perspective of a neural network and its training process, and formulate domain knowledge-dependent constraints over its internal structures (parameters and inductive biases) during training. This is inspired by \textit{control barrier function}, a constraint specification method from control theory. In particular, we specify the domain knowledge using Knowledge Graphs in our approach. To demonstrate the effectiveness of our approach, we apply it to two benchmark datasets focused on spatiotemporal reasoning: CLEVRER and CLEVRER-Humans, both centered around the task of question answering. Furthermore, we propose novel ways to evaluate if domain-grounding is achieved using our method. Our results show that the proposed methodology improves domain-grounding and question-answering accuracy while endowing the model with enhanced interpretability - an interpretability score that specifies to which extent the domain constraints are followed or violated.

## item_id: m_3482

TITLE: Retrieval-based Controllable Molecule Generation

ABSTRACT: Generating new molecules with specified chemical and biological properties via generative models has emerged as a promising direction for drug discovery. However, existing methods require extensive training/fine-tuning with a large dataset, often unavailable in real-world generation tasks. In this work, we propose a new retrieval-based framework for controllable molecule generation. We use a small set of exemplar molecules,  i.e., those that (partially) satisfy the design criteria, to steer the pre-trained generative model towards synthesizing molecules that satisfy the given design criteria. We design a retrieval mechanism that retrieves and fuses the exemplar molecules with the input molecule, which is trained by a new self-supervised objective that predicts the nearest neighbor of the input molecule. We also propose an iterative refinement process to dynamically update the generated molecules and retrieval database for better generalization. Our approach is agnostic to the choice of generative models and requires no task-specific fine-tuning. On various tasks ranging from simple design criteria to a challenging real-world scenario for designing lead compounds that bind to the SARS-CoV-2 main protease, we demonstrate our approach extrapolates well beyond the retrieval database, and achieves better performance and wider applicability than previous methods.

## item_id: m_3483

TITLE: Robust Reinforcement Learning with Distributional Risk-averse formulation

ABSTRACT: The purpose of robust reinforcement learning is to make predictions more robust to changes in the dynamics or rewards of the system. This problem is particularly important when dynamics and rewards of the environment are estimated from the data. However, without constraints, this problem is intractable. In this paper, we approximate the Robust Reinforcement Learning constrained with a $f$-divergence using an approximate Risk-Averse formulation. We show that the classical Reinforcement Learning formulation can be robustified using a standard deviation penalization of the objective. Two algorithms based on Distributional Reinforcement Learning, one for discrete and one for continuous action spaces, are proposed and tested in a classical Gym environment to demonstrate the robustness of the algorithms.

## item_id: m_3484

TITLE: Decoupling regularization from the action space

ABSTRACT: Regularized reinforcement learning (RL), particularly the entropy-regularized kind, has gained traction in optimal control and inverse RL. While standard unregularized RL methods remain unaffected by changes in the number of actions, we show that it can severely impact their regularized counterparts. This paper demonstrates the importance of decoupling the regularizer from the action space: that is, to maintain a consistent level of regularization regardless of how many actions are involved to avoid over-regularization. Whereas the problem can be avoided by introducing a task-specific temperature parameter, it is often undesirable and cannot solve the problem when action spaces are state-dependent. In the state-dependent action context, different states with varying action spaces are regularized inconsistently. We introduce two solutions: a static temperature selection approach and a dynamic counterpart, universally applicable where this problem arises. Implementing these changes improves performance on the DeepMind control suite in static and dynamic temperature regimes and a biological design task.

## item_id: m_3485

TITLE: Neural Latent Traversal with Semantic Constraints

ABSTRACT: Whilst Generative Adversarial Networks (GANs) generate visually appealing high resolution images, the latent representations (or codes) of these models do not allow controllable changes on the semantic attributes of the generated images. Recent approaches proposed to learn linear models to relate the latent codes with the attributes to enable adjustment of the attributes. However, as the latent spaces of GANs are learnt in an unsupervised manner and are semantically entangled, the linear models are not always effective. In this study, we learn multi-stage neural transformations of latent spaces of pre-trained GANs that enable more accurate modeling of the relation between the latent codes and the semantic attributes. To ensure identity preservation of images, we propose a sparsity constraint on the latent space transformations that is guided by the mutual information between the latent and the semantic space. We demonstrate our method on two face datasets (FFHQ and CelebA-HQ) and show that it outperforms current state-of-the-art baselines based on FID score and other numerical metrics.

## item_id: m_3486

TITLE: DaSeGAN: Domain Adaptation for Segmentation Tasks via Generative Adversarial Networks

ABSTRACT: A weakness of deep learning methods is that they can fail when there is a mismatch between source and target data domains. In medical image applications, this is a common situation when data from new vendor devices or different hospitals is available. Domain adaptation techniques aim to fill this gap by generating mappings between image domains when unlabeled data from the new target domain is available. In other cases, no target domain data (labeled or unlabeled) is available during training. In this latter case, domain generalization methods focus on learning domain-invariant representations which are more robust to new domains. In this paper, a combination of domain adaptation and generalization techniques is proposed by leveraging domain-invariant image translations for image segmentation problems. This is achieved by adversarially training a generator that transforms source images to a universal domain. To preserve the semantic consistency between the source and universal domains a segmentation consistency loss between the source and universal predictions is used. Our method was validated on the M&Ms dataset, a multi-source unsupervised domain adaptation, and generalization problem, outperforming previous methods. Particularly, our method significantly boosts the test results over the unlabeled and unseen domains without hurting source-labeled domains.

## item_id: m_3487

TITLE: Multi-Step Decentralized Domain Adaptation

ABSTRACT: Despite the recent breakthroughs in unsupervised domain adaptation (uDA), no prior work has studied the challenges of applying these methods in practical machine learning scenarios. In this paper, we highlight two significant bottlenecks for uDA, namely excessive centralization and poor support for distributed domain datasets. Our proposed framework, MDDA, is powered by a novel collaborator selection algorithm and an effective distributed adversarial training method, and allows for uDA methods to work in a decentralized and privacy-preserving way.  


## item_id: m_3488

TITLE: PISA: Compressive Sensing Adaptation of Large Language Models

ABSTRACT: In this paper, we introduce a novel perspective on Parameter-Efficient Fine-Tuning (PEFT) by viewing the weight update matrix as a k-sparse approximation in the spatial domain, departing from the commonly used low-rank structure assumption. We propose a compressive sensing-based approach that leverages under-complete measurement matrices to analyze the approximation capabilities of the weight update matrix. Our method ensures bounded error in the reconstruction of the weight updates, as guaranteed by theoretical results in compressive sensing.
However, the vectorization of the weight update matrix leads to a high-dimensional problem (d^2), which can potentially result in large error bounds. To address this issue, we introduce a block-structured approximation scheme that partitions the weight update matrix into smaller blocks and applies the k-sparse approximation to each block independently. We theoretically analyze the approximation error bounds of our approach and demonstrate that the block-structured scheme achieves tighter error bounds compared to the non-block approach.
Empirically, we validate the effectiveness of our proposed method on various downstream NLP tasks, showcasing its ability to achieve competitive performance with a reduced number of trainable parameters. Our approach offers a new direction for parameter-efficient fine-tuning of large language models. Notably, our experiments demonstrate competitive performance with only 500 learnable parameters, while offering greater memory and computational efficiency than LoRA in a rank-1 setting.

## item_id: m_3489

TITLE: Synthetic Pre-Training Tasks for Neural Machine Translation

ABSTRACT: Pre-training is an effective technique for ensuring robust performance on a variety of machine learning tasks. It typically depends on large-scale crawled corpora that can result in toxic or biased models. Such data can also be problematic with respect to copyright, attribution, and privacy. Pre-training with synthetic tasks and data is a promising way of alleviating such concerns since no real-world information is ingested by the model. Our goal in this paper is to understand what makes for a good pre-trained model when using synthetic resources. We answer this question in the context of neural machine translation by considering two novel approaches to translation model pre-training. Our first approach studies the effect of pre-training on obfuscated data derived from a parallel corpus by mapping words to a vocabulary of `nonsense' tokens. Our second approach explores the effect of pre-training on procedurally generated synthetic parallel data that does not depend on any real human language corpus. Our empirical evaluation on multiple language pairs shows that, to a surprising degree, the benefits of pre-training can be realized even with obfuscated or purely synthetic parallel data. In our analysis, we consider the extent to which obfuscated and synthetic pre-training techniques can be used to mitigate the issue of hallucinated model toxicity.

## item_id: m_3490

TITLE: LLM-QAT: Data-Free Quantization Aware Training for Large Language Models

ABSTRACT: Several post-training quantization methods have been applied to large language models (LLMs), and have been shown to perform well down to 8-bits.  We find that these methods break down at lower bit precision, and investigate quantization aware training for LLMs (LLM-QAT) to push quantization levels even further.  We propose a data-free distillation method that leverages generations produced by the pre-trained model, which better preserves the original output distribution and allows quantizing any generative model independent of its training data, similar to post-training quantization methods.  In addition to quantizing weights and activations, we also quantize the KV cache, which is critical for increasing throughput and support long sequence dependencies at current model sizes.  We experiment with LLaMA models of sizes 7B, 13B, and 30B, at quantization levels down to 4-bits.  We observe large improvements over training-free methods, especially in the low-bit settings.

## item_id: m_3491

TITLE: Learning Representations of Categorical Feature Combinations via Self-Attention

ABSTRACT: Self-attention has been widely used to model the sequential data and achieved remarkable results in many applications. Although it can be used to model dependencies without regard to positions of sequences, self-attention is seldom applied to non-sequential data. In this work, we propose to learn representations of multi-field categorical data in prediction tasks via self-attention mechanism, where features are orderless but have intrinsic relations over different fields. In most current DNN based models, feature embeddings are simply concatenated for further processing by networks. Instead, by applying self-attention to transform the embeddings, we are able to relate features in different fields and automatically learn representations of their combinations, which are known as the factors of many prevailing linear models. To further improve the effect of feature combination mining, we modify the original self-attention structure by restricting the similarity weight to have at most k non-zero values, which additionally regularizes the model. We experimentally evaluate the effectiveness of our self-attention model on non-sequential data. Across two click through rate prediction benchmark datasets, i.e., Cretio and Avazu, our model with top-k restricted self-attention achieves the state-of-the-art performance. Compared with the vanilla MLP, the gain by adding self-attention is significantly larger than that by modifying the network structures, which most current works focus on.

## item_id: m_3492

TITLE: Q-map: a Convolutional Approach for Goal-Oriented Reinforcement Learning

ABSTRACT: Goal-oriented learning has become a core concept in reinforcement learning (RL), extending the reward signal as a sole way to define tasks. However, as parameterizing value functions with goals increases the learning complexity, efficiently reusing past experience to update estimates towards several goals at once becomes desirable but usually requires independent updates per goal.
Considering that a significant number of RL environments can support spatial coordinates as goals, such as on-screen location of the character in ATARI or SNES games, we propose a novel goal-oriented agent called Q-map that utilizes an autoencoder-like neural network to predict the minimum number of steps towards each coordinate in a single forward pass. This architecture is similar to Horde with parameter sharing and allows the agent to discover correlations between visual patterns and navigation. For example learning how to use a ladder in a game could be transferred to other ladders later.
We show how this network can be efficiently trained with a 3D variant of Q-learning to update the estimates towards all goals at once. While the Q-map agent could be used for a wide range of applications, we propose a novel exploration mechanism in place of epsilon-greedy that relies on goal selection at a desired distance followed by several steps taken towards it, allowing long and coherent exploratory steps in the environment.
We demonstrate the accuracy and generalization qualities of the Q-map agent on a grid-world environment and then demonstrate the efficiency of the proposed exploration mechanism on the notoriously difficult Montezuma's Revenge and Super Mario All-Stars games.

## item_id: m_3493

TITLE: Adaptive Generalization for Semantic Segmentation

ABSTRACT: Out-of-distribution robustness remains a salient weakness of current state-of-the-art models for semantic segmentation. Until recently, research on generalization followed a restrictive assumption that the model parameters remain fixed after the training process. In this work, we empirically study an adaptive inference strategy for semantic segmentation that adjusts the model to the test sample before producing the final prediction. We achieve this with two complementary techniques. Using Instance-adaptive Batch Normalization (IaBN), we modify normalization layers by combining the feature statistics acquired at training time with those of the test sample. We next introduce a test-time training (TTT) approach for semantic segmentation, Seg-TTT, which adapts the model parameters to the test sample using a self-supervised loss. Relying on a more rigorous evaluation protocol compared to previous work on generalization in semantic segmentation, our study shows that these techniques consistently and significantly outperform the baseline and attain a new state of the art, substantially improving in accuracy over previous generalization methods.

## item_id: m_3494

TITLE: Trajectory Prediction using Equivariant Continuous Convolution

ABSTRACT: Trajectory prediction is a critical part of many AI applications, for example, the safe operation of autonomous vehicles. However, current methods are prone to making inconsistent and physically unrealistic predictions. We leverage insights from  fluid dynamics to overcome this limitation by considering internal symmetry in real-world trajectories. We propose a novel model, Equivariant Continous COnvolution (ECCO) for improved trajectory prediction.  ECCO uses rotationally-equivariant continuous convolutions to embed the symmetries of the system. On both vehicle and pedestrian trajectory datasets, ECCO attains competitive accuracy  with significantly fewer parameters. It is also more sample efficient, generalizing automatically from few data points in any orientation.  Lastly, ECCO improves generalization with equivariance, resulting in more physically consistent predictions.   Our method provides a fresh perspective towards increasing trust and transparency in deep learning models. Our code and data can be found at https://github.com/Rose-STL-Lab/ECCO.

## item_id: m_3495

TITLE: Self-explainable Molecular Property Prediction via Multi-view Hypergraph Learning

ABSTRACT: Explainable molecular property prediction plays a critical role in drug discovery and materials science. Existing graph neural network (GNN)-based approaches usually rely on pairwise atomic interactions for molecular modeling and interpretation. However, such atom-centered modeling often neglects the cooperative effects of atomic groups and lacks the guidance of chemical rules, thereby limiting both prediction accuracy and interpretability. To address these challenges, we propose a multi-view **Hyper**graph learning method for **S**elf-**E**xplainable **M**olecular property prediction(HyperSEM). Our method introduces a hyperedge-driven explanation paradigm, where atomic groups are explicitly modeled as hyperedges to capture high-order cooperative effects, and multi-view hypergraphs are constructed to jointly integrate chemical rules and data-driven signals. Furthermore, we design a molecular structure-informed hypergraph convolution to preserve both high-order atomic-group interactions and low-order structural features, and an information-bottleneck-guided self explanation to jointly generate predictions and explanations. Extensive experimental results show that HyperSEM outperforms existing state-of-the-art methods on seven benchmark datasets, demonstrating dual advantages in prediction accuracy and interpretability.

## item_id: m_3496

TITLE: CAUSAL REASONING WITH LARGE FOUNDATION MOD- ELS TO GUIDE DYNAMIC SYSTEM FORECASTING

ABSTRACT: Prevailing data-driven models for spatio-temporal forecasting excel at interpolating within known patterns but often falter in critical real-world scenarios. This failure stems from a fundamental flaw: they learn \textbf{spurious correlations} from raw data, bypassing the underlying semantic and physical principles that form the true causal pathways. To address this, we introduce \textbf{\method{}} (Physics-informed Reasoning and Interpretation for Spatio-temporal Modeling), a framework that performs a \textbf{principled causal intervention}. \method{} employs a Vision-Language Model (VLM) to interpret spatio-temporal snapshots into semantic narratives, and a Large Language Model (LLM) to reason with these narratives and explicit physical laws, generating a causally-informed textual guidance. This guidance is then encoded to steer a downstream numerical predictor. Extensive experiments across fluid dynamics, weather forecasting, and urban traffic demonstrate that this intervention significantly enhances model capabilities. By repairing the causal chain,  boosts \textit{out-of-distribution (OOD) generalization}, improves \textit{prediction under data sparsity}, and sharpens \textit{extreme event prediction}. Our work pioneers a new paradigm that unifies the pattern recognition of traditional models with the causal reasoning of large foundation models, paving the way for more reliable AI in science.

## item_id: m_3497

TITLE: Dynamic Evaluation of Neural Sequence Models

ABSTRACT: We present methodology for using dynamic evaluation to improve neural sequence models. Models are adapted to recent history via a gradient descent based mechanism, causing them to assign higher probabilities to re-occurring sequential patterns. Dynamic evaluation outperforms existing adaptation approaches in our comparisons. Dynamic evaluation improves the state-of-the-art word-level perplexities on the Penn Treebank and WikiText-2 datasets to 51.1 and 44.3 respectively, and the state-of-the-art character-level cross-entropies on the text8 and Hutter Prize datasets to 1.19 bits/char and 1.08 bits/char respectively.

## item_id: m_3498

TITLE: The Role of Pretrained Representations for the OOD Generalization of RL Agents

ABSTRACT: Building sample-efficient agents that generalize out-of-distribution (OOD) in real-world settings remains a fundamental unsolved problem on the path towards achieving higher-level cognition. One particularly promising approach is to begin with low-dimensional, pretrained representations of our world, which should facilitate efficient downstream learning and generalization. By training 240 representations and over 10,000 reinforcement learning (RL) policies on a simulated robotic setup, we evaluate to what extent different properties of pretrained VAE-based representations affect the OOD generalization of downstream agents. We observe that many agents are surprisingly robust to realistic distribution shifts, including the challenging sim-to-real case. In addition, we find that the generalization performance of a simple downstream proxy task reliably predicts the generalization performance of our RL agents under a wide range of OOD settings. Such proxy tasks can thus be used to select pretrained representations that will lead to agents that generalize.

## item_id: m_3499

TITLE: Explanation-Assisted Data Augmentation  for Graph Learning

ABSTRACT: This work introduces a novel class of Data Augmentation (DA) techniques in the context of graph learning. In general, DA refers to techniques that enlarge the training set using label-preserving transformations.  Such techniques enable increased robustness and generalization, especially when the size of the original training set is limited. A fundamental idea in DA is that 
labels are invariant to domain-specific transformations of the input samples. 
However, it is challenging to identify such transformations in learning over graphical input domains due to the complex nature of graphs and the need to preserve their structural and semantic properties.
In this work, we propose explanation-assisted DA (EA-DA) for Graph Neural Networks (GNNs). A graph explanation is a subgraph which is an `almost sufficient' statistic of the input graph with respect to its classification label. Consequently, the classification label is invariant, with high probability, to perturbations of graph edges not belonging to its explanation subgraph. We develop EA-DA techniques leveraging such perturbation invariances. First, we show analytically that the sample complexity of explanation-assisted learning can be arbitrarily smaller than explanation-agnostic learning. On the other hand, we show that if the training set is enlarged using EA-DA techniques and
the learning rule does not distinguish between the augmented data and the original data, then the sample complexity can be worse than that of explanation-agnostic learning. We identify the main reason for the potential increase in sample complexity as the out-of-distribution nature of graph perturbations. 
We conclude that theoretically EA-DA may improve sample complexity, and that the learning rule must distinguish between the augmented data and the original data. Subsequently, we build upon these theoretical insights, introduce practically implementable EA-DA techniques and associated learning mechanisms, and perform extensive empirical evaluations.

## item_id: m_3500

TITLE: Preferences Implicit in the State of the World

ABSTRACT: Reinforcement learning (RL) agents optimize only the features specified in a reward function and are indifferent to anything left out inadvertently. This means that we must not only specify what to do, but also the much larger space of what not to do. It is easy to forget these preferences, since these preferences are already satisfied in our environment. This motivates our key insight: when a robot is deployed in an environment that humans act in, the state of the environment is already optimized for what humans want. We can therefore use this implicit preference information from the state to fill in the blanks. We develop an algorithm based on Maximum Causal Entropy IRL and use it to evaluate the idea in a suite of proof-of-concept environments designed to show its properties. We find that information from the initial state can be used to infer both side effects that should be avoided as well as preferences for how the environment should be organized. Our code can be found at https://github.com/HumanCompatibleAI/rlsp.
