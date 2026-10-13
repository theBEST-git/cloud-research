# Batch 19 — 100 items

## item_id: m_1801

TITLE: Learning to Jointly Understand Visual and Tactile Signals

ABSTRACT: Modeling and analyzing object and shape has been well studied in the past. However, manipulation of these complex tools and articulated objects remains difficult for autonomous agents. Our human hands, however, are dexterous and adaptive. We can easily adapt a manipulation skill on one object to all objects in the class and to other similar classes. Our intuition comes from that there is a close connection between manipulations and topology and articulation of objects. The possible articulation of objects indicates the types of manipulation necessary to operate the object. In this work, we aim to take a manipulation perspective to understand everyday objects and tools. We collect a multi-modal visual-tactile dataset that contains paired full-hand force pressure maps and manipulation videos. We also propose a novel method to learn a cross-modal latent manifold that allow for cross-modal prediction and discovery of latent structure in different data modalities. We conduct extensive experiments to demonstrate the effectiveness of our method.

## item_id: m_1802

TITLE: Adaptive Dataset Sampling by Deep Policy Gradient

ABSTRACT: Mini-batch SGD is a predominant optimization method in deep learning. Several works aim to improve naïve random dataset sampling, which appears typically in deep learning literature, with additional prior to allow faster and better performing optimization. This includes, but not limited to, importance sampling and curriculum learning. In this work, we propose an alternative way: we think of sampling as a trainable agent and let this external model learn to sample mini-batches of training set items based on the current status and recent history of the learned model. The resulting adaptive dataset sampler, named RLSampler, is a policy network implemented with simple recurrent neural networks trained by a policy gradient algorithm. We demonstrate RLSampler on image classification benchmarks with several different learner architectures and show consistent performance gain over the originally reported scores. Moreover, either a pre-sampled sequence of indices or a pre-trained RLSampler turns out to be more effective than naïve random sampling regardless of the network initialization and model architectures. Our analysis reveals the possible existence of a model-agnostic sample sequence that best represents the dataset under mini-batch SGD optimization framework.

## item_id: m_1803

TITLE: An old dog can learn (some) new tricks: A tale of a three-decade old architecture

ABSTRACT: Designing novel architectures often involves combining or extending familiar components such as convolutions and attention modules. However, this approach can obscure the fundamental design principles as the focus is usually on the entire architecture. Instead, this paper takes an unconventional approach, attempting to rejuvenate an old architecture with modern tools and techniques. Our primary objective is to explore whether a 30-year-old architecture can compete with contemporary models, when equipped with modern tools. Through experiments spanning image recognition datasets, we aim to understand what aspects of the architecture contribute to its performance. We find that while an ensemble of ingredients bears significance in achieving commendable performance, only a few pivotal components have a large impact. We contend that our discoveries offer valuable insights for creating cutting-edge architectures.

## item_id: m_1804

TITLE: Learning the Visualness of Text Using Large Vision-Language Models

ABSTRACT: Visual text evokes an image in a person's mind, while non-visual text fails to do so. A method to automatically detect visual text will unlock the ability to augment text with relevant images, as neural text-to-image generation and retrieval models operate on the implicit assumption that the input text is visual in nature. We curate a dataset of 3,620 English sentences and their visualness scores provided by multiple human annotators. Additionally, we use documents that contain text and visual assets to create a distantly supervised corpus of document text and associated images. We also propose a fine-tuning strategy that adapts large vision-language models like CLIP that assume a one-to-one correspondence between text and image to the task of scoring text visualness from text input alone. Our strategy involves modifying the model's contrastive learning objective to map text identified as non-visual to a common NULL image while matching visual text to their corresponding images in the document. We evaluate the proposed approach on its ability to (i) classify visual and non-visual text accurately, and (ii) attend over words that are identified as visual in psycholinguistic studies. Empirical evaluation indicates that our approach performs better than several heuristics and baseline models for the proposed task. Furthermore, to highlight the importance of modeling the visualness of text, we conduct qualitative analyses of text-to-image generation systems like DALL-E. We release the curated dataset and code.

## item_id: m_1805

TITLE: Video-LevelGauge: Investigating Contextual Positional Bias in Video Language Models.

ABSTRACT: Large video language models (LVLMs) have made notable progress in video understanding, spurring the development of corresponding evaluation benchmarks. However, existing benchmarks generally assess overall performance across entire video sequences, overlooking nuanced behaviors such as contextual positional bias, a critical yet under-explored aspect of LVLM performance. We present **Video-LevelGauge**, a dedicated benchmark designed to systematically assess positional bias in LVLMs. We employ standardized probes and customized contextual setups, allowing flexible control over context length, probe position, and contextual types to simulate diverse real-world scenarios. In addition, we introduce a comprehensive analysis method that combines statistical measures with bias pattern recognition to characterize bias. Our benchmark comprises 438 manually curated videos spanning multiple types, yielding 1,177 high-quality multiple-choice questions and 120 open-ended questions, validated for their effectiveness in exposing positional bias. Based on these, we evaluate 27 state-of-the-art LVLMs, including both commercial and open-source models. Our findings reveal significant positional biases in many leading open-source models, typically exhibiting head or neighbor-content preferences. In contrast, commercial models such as Gemini 2.5 Pro show impressive, consistent performance across entire video sequences. Further analyses on context variation, context length, model scale, and multi-modal reasoning provide insights for mitigating bias and guiding model enhancement.

## item_id: m_1806

TITLE: Machine Comprehension Using Match-LSTM and Answer Pointer

ABSTRACT: Machine comprehension of text is an important problem in natural language processing. A recently released dataset, the Stanford Question Answering Dataset (SQuAD), offers a large number of real questions and their answers created by humans through crowdsourcing. SQuAD provides a challenging testbed for evaluating machine comprehension algorithms, partly because compared with previous datasets, in SQuAD the answers do not come from a small set of candidate answers and they have variable lengths. We propose an end-to-end neural architecture for the task. The architecture is based on match-LSTM, a model we proposed previously for textual entailment, and Pointer Net, a sequence-to-sequence model proposed by Vinyals et al. (2015) to constrain the output tokens to be from the input sequences. We propose two ways of using Pointer Net for our tasks. Our experiments show that both of our two models substantially outperform the best results obtained by Rajpurkar et al. (2016) using logistic regression and manually crafted features. Besides, our boundary model also achieves the best performance on the MSMARCO dataset (Nguyen et al. 2016).

## item_id: m_1807

TITLE: The Curious Case of Neural Text Degeneration

ABSTRACT: Despite considerable advances in neural language modeling, it remains an open question what the best decoding strategy is for text generation from a language model (e.g. to generate a story). The counter-intuitive empirical observation is that even though the use of likelihood as training objective leads to high quality models for a broad range of language understanding tasks, maximization-based decoding methods such as beam search lead to degeneration — output text that is bland, incoherent, or gets stuck in repetitive loops.

To address this we propose Nucleus Sampling, a simple but effective method to draw considerably higher quality text out of neural language models than previous decoding strategies. Our approach avoids text degeneration by truncating the unreliable tail of the probability distribution, sampling from the dynamic nucleus of tokens containing the vast majority of the probability mass.

To properly examine current maximization-based and stochastic decoding methods, we compare generations from each of these methods to the distribution of human text along several axes such as likelihood, diversity, and repetition. Our results show that (1) maximization is an inappropriate decoding objective for open-ended text generation, (2) the probability distributions of the best current language models have an unreliable tail which needs to be truncated during generation and (3) Nucleus Sampling is currently the best available decoding strategy for generating long-form text that is both high-quality — as measured by human evaluation — and as diverse as human-written text.

## item_id: m_1808

TITLE: Learning more skills through optimistic exploration

ABSTRACT: Unsupervised skill learning objectives (Eysenbach et al., 2019; Gregor et al., 2016) allow agents to learn rich repertoires of behavior in the absence of extrinsic rewards. They work by simultaneously training a policy to produce distinguishable latent-conditioned trajectories, and a discriminator to evaluate distinguishability by trying to infer latents from trajectories. The hope is for the agent to explore and master the environment by encouraging each skill (latent) to reliably reach different states. However, an inherent exploration problem lingers: when a novel state is actually encountered, the discriminator will necessarily not have seen enough training data to produce accurate and confident skill classifications, leading to low intrinsic reward for the agent and effective penalization of the sort of exploration needed to actually maximize the objective. To combat this inherent pessimism towards exploration, we derive an information gain auxiliary objective that involves training an ensemble of discriminators and rewarding the policy for their disagreement. Our objective directly estimates the epistemic uncertainty that comes from the discriminator not having seen enough training examples, thus providing an intrinsic reward more tailored to the true objective compared to pseudocount-based methods (Burda et al., 2019). We call this exploration bonus discriminator disagreement intrinsic reward, or DISDAIN. We demonstrate empirically that DISDAIN improves skill learning both in a tabular grid world (Four Rooms) and the 57 games of the Atari Suite (from pixels). Thus, we encourage researchers to treat pessimism with DISDAIN.

## item_id: m_1809

TITLE: Generating universal language adversarial examples by understanding and enhancing the transferability across neural models

ABSTRACT: Deep neural network models are vulnerable to adversarial attacks. In many cases, malicious inputs intentionally crafted for one model can fool another model in the black-box attack setting. However, there is a lack of systematic studies on the transferability of adversarial examples and how to generate universal adversarial examples. In this paper, we systematically study the transferability of adversarial attacks for text classification models. In particular, we conduct extensive experiments to investigate how various factors, such as network architecture, input format, word embedding, and model capacity, affect the transferability of adversarial attacks. Based on these studies, we then propose universal black-box attack algorithms that can induce adversarial examples to attack almost all existing models. These universal adversarial examples reflect the defects of the learning process and the bias in the training dataset. Finally, we generalize these adversarial examples into universal word replacement rules that can be used for model diagnostics. 

## item_id: m_1810

TITLE: Consciousness-Aware Multi-Agent Reinforcement Learning

ABSTRACT: In cooperative multi-agent reinforcement learning, centralized training with decentralized execution (CTDE) shows great promise for a trade-off between independent Q-learning and joint action learning. However, vanilla CTDE methods assumed a fixed number of agents could hardly adapt to real-world scenarios where dynamic team compositions typically suffer from the dilemma of dramatic partial observability variance. Specifically, agents with extensive sight ranges are prone to be affected by trivial environmental substrates, dubbed the “attention distraction” issue; ones with limited observability can hardly sense their teammates, hindering the quality of cooperation. In this paper, we propose a Consciousness-Aware Multi-Agent reinforcement learning (CAMA) approach, which roots in a divide-and-conquer strategy to facilitate stable and sustainable teamwork. Concretely, CAMA targets dividing the input entities with controlled observability masks by an Entity Dividing Module (EDM) according to their execution relevance for consciousness learning. To tackle the attention distraction issue, the highly related entities are fed to a Consciousness Enhancement Module (CEM) for consciousness-aware representation extraction via action prediction with an inverse model. For better out-of-sight-range cooperation, the lowly related ones are compressed to brief messages by a Consciousness Replenishment Module (CRM) with a conditional mutual information estimator. Our CAMA outperforms the SOTA methods significantly on the challenging StarCraftII, MPE, and Traffic Junction benchmarks.

## item_id: m_1811

TITLE: Multi-view Generative Adversarial Networks

ABSTRACT: Learning over multi-view data is a challenging problem with strong practical applications. Most related studies focus on the classification point of view and assume that all the views are available at any time. We consider an extension of this framework in two directions. First, based on the BiGAN model, the Multi-view BiGAN (MV-BiGAN) is able to perform density estimation from multi-view inputs. Second, it can deal with missing views and is able to update its prediction when additional views are provided. We illustrate these properties on a set of experiments over different datasets.

## item_id: m_1812

TITLE: GraphPNAS: Learning Distribution of Good Neural Architectures via Deep Graph Generative Models

ABSTRACT: Neural architectures can be naturally viewed as computational graphs. Motivated by this perspective, we, in this paper, study neural architecture search (NAS) through the lens of learning random graph models. In contrast to existing NAS methods which largely focus on searching for a single best architecture, i.e, point estimation, we propose GraphPNAS a deep graph generative model that learns a distribution of well-performing architectures. Relying on graph neural networks (GNNs), our GraphPNAS can better capture topologies of good neural architectures and relations between operators therein. Moreover, our graph generator leads to a learnable probabilistic search method that is more flexible and efficient than the commonly used RNN generator and random search methods. Finally, we learn our generator via an efficient reinforcement learning formulation for NAS. To assess the effectiveness of our GraphPNAS, we conduct extensive experiments on three search spaces, including the challenging RandWire on TinyImageNet, ENAS on CIFAR10, and NAS-Bench-101. The complexity of RandWire is significantly larger than other search spaces in the literature. We show that our proposed graph generator consistently outperforms RNN-based one and achieves better or comparable performances than state-of-the-art NAS methods. 

## item_id: m_1813

TITLE: An Optimization-Based Framework for Adversarial Defence of Graph Neural Networks Via Adaptive Lipschitz Regularization

ABSTRACT: Graph Neural Networks (GNNs) have exhibited exceptional performance across diverse application domains by harnessing the inherent interconnectedness of data. However, the emergence of adversarial attacks targeting GNNs poses a substantial and pervasive threat, compromising their overall performance and learning capabilities. While recent efforts have focused on enhancing GNN robustness from both data and architectural perspectives, more attention should be given to overall network stability in the face of input perturbations. Prior methods addressing network stability have routinely employed gradient normalization as a fundamental technique. This study introduces a unifying approach, termed as AdaLip, for adversarial training of GNNs through an optimization framework that leverages the explicit Lipschitz constant. By seamlessly integrating graph denoising and network regularization, AdaLip offers a comprehensive and versatile solution, extending its applicability and enabling robust regularization for diverse neural network architectures. Further, we develop a provably convergent iterative algorithm, leveraging block majorization-minimization, graph learning, and alternate minimization techniques to solve the proposed optimization problem. Simulation results on real datasets demonstrate the efficacy of AdaLip over state-of-the-art defence methods across diverse classes of poisoning attacks. On select datasets, AdaLip demonstrates GCN performance improvements of up to 20\% against modification attacks and approximately 10\% against injection attacks. Remarkably, AdaLip achieves a similar performance gain on heterophily graph datasets.

## item_id: m_1814

TITLE: Variance Regularized Counterfactual Risk Minimization via Variational Divergence Minimization

ABSTRACT: Off-policy learning, the task of evaluating and improving policies using historic data collected from a logging policy, is important because on-policy evaluation is usually expensive and has adverse impacts. One of the major challenge of off-policy learning is to derive counterfactual estimators that also has low variance and thus low generalization error. 
In this work, inspired by learning bounds for importance sampling problems, we present a new counterfactual learning principle for off-policy learning with bandit feedbacks.Our method regularizes the generalization error by minimizing the distribution divergence between the logging policy and the new policy, and removes the need for iterating through all training samples to compute sample variance regularization in prior work. With neural network policies, our end-to-end training algorithms using variational divergence minimization showed significant improvement over conventional baseline algorithms and is also consistent with our theoretical results.

## item_id: m_1815

TITLE: Value Function Spaces: Skill-Centric State Abstractions for Long-Horizon Reasoning

ABSTRACT: Reinforcement learning can train policies that effectively perform complex tasks. However for long-horizon tasks, the performance of these methods degrades with horizon, often necessitating reasoning over and chaining lower-level skills. Hierarchical reinforcement learning aims to enable this by providing a bank of low-level skills as action abstractions. Hierarchies can further improve on this by abstracting the space states as well. We posit that a suitable state abstraction should depend on the capabilities of the available lower-level policies. We propose Value Function Spaces: a simple approach that produces such a representation by using the value functions corresponding to each lower-level skill. These value functions capture the affordances of the scene, thus forming a  representation that compactly abstracts task relevant information and robustly ignores distractors. Empirical evaluations for maze-solving and robotic manipulation tasks demonstrate that our approach improves long-horizon performance and enables better zero-shot generalization than alternative model-free and model-based methods.

## item_id: m_1816

TITLE: PRUNING WITH HINTS: AN EFFICIENT FRAMEWORK FOR MODEL ACCELERATION

ABSTRACT: In this paper, we propose an efficient framework to accelerate convolutional neural networks. We utilize two types of acceleration methods: pruning and hints. Pruning can reduce model size by removing channels of layers. Hints can improve the performance of student model by transferring knowledge from teacher model. We demonstrate that pruning and hints are complementary to each other. On one hand, hints can benefit pruning by maintaining similar feature representations. On the other hand, the model pruned from teacher networks is a good initialization for student model, which increases the transferability between two networks. Our approach performs pruning stage and hints stage iteratively to further improve the
performance. Furthermore, we propose an algorithm to reconstruct the parameters of hints layer and make the pruned model more suitable for hints. Experiments were conducted on various tasks including classification and pose estimation. Results on CIFAR-10, ImageNet and COCO demonstrate the generalization and superiority of our framework.

## item_id: m_1817

TITLE: Risk-Sensitive Variational Model-Based Policy Optimization

ABSTRACT: RL-as-inference casts reinforcement learning (RL) as Bayesian inference in a probabilistic graphical model. While this framework allows efficient variational approximations it is known that model-based RL-as-inference learns optimistic dynamics and risk-seeking policies that can exhibit catastrophic behavior.  By exploiting connections between the variational objective and a well-known risk-sensitive utility function we adaptively adjust policy risk based on the environment dynamics.  Our method, $\beta$-VMBPO, extends the variational model-based policy optimization (VMBPO) algorithm to perform dual descent on risk parameter $\beta$.   We provide a thorough theoretical analysis that fills gaps in the theory of model-based RL-as-inference by establishing a generalization of policy improvement, value iteration, and guarantees on policy determinism.  Our experiments demonstrate that this risk-sensitive approach yields improvements in simple tabular and complex continuous tasks, such as the DeepMind Control Suite.

## item_id: m_1818

TITLE: Deep Gradient Boosting -- Layer-wise Input Normalization of Neural Networks

ABSTRACT: Stochastic gradient descent (SGD) has been the dominant optimization method for training deep neural networks due to its many desirable properties. One of the more remarkable and least understood quality of SGD is that it generalizes relatively well
on unseen data even when the neural network has millions of parameters. We hypothesize that in certain cases it is desirable to relax its intrinsic generalization properties and introduce an extension of SGD called deep gradient boosting (DGB). The key idea of DGB is that back-propagated gradients inferred using the chain rule can be viewed as pseudo-residual targets of a gradient boosting problem. Thus at each layer of a neural network the weight update is calculated by solving the corresponding boosting problem using a linear base learner. The resulting weight update formula can also be viewed as a normalization procedure of the data that arrives at each layer during the forward pass. When implemented as a separate input normalization layer (INN) the new architecture shows improved performance on image recognition tasks when compared to the same architecture without normalization layers. As opposed to batch normalization (BN), INN has no learnable parameters however it matches its performance on CIFAR10 and ImageNet classification tasks.

## item_id: m_1819

TITLE: Variational Continual Learning

ABSTRACT: This paper develops variational continual learning (VCL), a simple but general framework for continual learning that fuses online variational inference (VI) and recent advances in Monte Carlo VI for neural networks. The framework can successfully train both deep discriminative models and deep generative models in complex continual learning settings where existing tasks evolve over time and entirely new tasks emerge. Experimental results show that VCL outperforms state-of-the-art continual learning methods on a variety of tasks, avoiding catastrophic forgetting in a fully automatic way.

## item_id: m_1820

TITLE: Active Learning with Partial Feedback

ABSTRACT: While many active learning papers assume that the learner can simply ask for a label and receive it, real annotation often presents a mismatch between the form of a label (say, one among many classes), and the form of an annotation (typically yes/no binary feedback). To annotate examples corpora for multiclass classification, we might need to ask multiple yes/no questions, exploiting a label hierarchy if one is available. To address this more realistic setting, we propose active learning with partial feedback (ALPF), where the learner must actively choose both which example to label and which binary question to ask. At each step, the learner selects an example, asking if it belongs to a chosen (possibly composite) class. Each answer eliminates some classes, leaving the learner with a partial label. The learner may then either ask more questions about the same example (until an exact label is uncovered) or move on immediately, leaving the first example partially labeled. Active learning with partial labels requires (i) a sampling strategy to choose (example, class) pairs, and (ii) learning from partial labels between rounds. Experiments on Tiny ImageNet demonstrate that our most effective method improves 26% (relative) in top-1 classification accuracy compared to i.i.d. baselines and standard active learners given 30% of the annotation budget that would be required (naively) to annotate the dataset. Moreover, ALPF-learners fully annotate TinyImageNet at 42% lower cost. Surprisingly, we observe that accounting for per-example annotation costs can alter the conventional wisdom that active learners should solicit labels for hard examples.

## item_id: m_1821

TITLE: Causally Constrained Data Synthesis For Private Data Release

ABSTRACT: Data privacy is critical in many decision-making contexts, such as healthcare and finance. A common mechanism is to create differentially private synthetic data using generative models. Such data generation reflects certain statistical properties of the original data, but often has an unacceptable privacy vs. utility trade-off. Since natural data inherently exhibits causal structure, we propose incorporating \emph{causal information} into the training process to favorably navigate the aforementioned trade-off. Under certain assumptions for linear gaussian models and a broader class of models, we theoretically prove that causally informed generative models provide better differential privacy guarantees than their non-causal counterparts. We evaluate our proposal using variational autoencoders, and demonstrate that the trade-off is mitigated through better utility for comparable privacy.

## item_id: m_1822

TITLE: Simultaneous Computation and Memory Efficient Zeroth-Order Optimizer for Fine-Tuning Large Language Models

ABSTRACT: Fine-tuning is powerful for adapting large language models to downstream tasks, but it often results in huge memory usages. 
A promising approach to mitigate this is using Zeroth-Order (ZO) optimization, which estimates gradients to replace First-Order (FO) gradient calculations, albeit with longer training time due to its stochastic nature. 
By revisiting the Memory-efficient ZO (MeZO) optimizer, we discover that the full-parameter perturbation and updating processes consume over 50\% of its overall fine-tuning time cost. 
Based on these observations, we introduce a novel layer-wise sparse computation and memory efficient ZO optimizer, named LeZO  
LeZO treats layers as fundamental units for sparsification and dynamically perturbs different parameter subsets in each step to achieve full-parameter fine-tuning. 
LeZO incorporates layer-wise parameter sparsity in the process of simultaneous perturbation stochastic approximation (SPSA) and ZO stochastic gradient descent (ZO-SGD). 
It achieves accelerated computation during perturbation and updating processes without additional memory overhead.
We conduct extensive experiments with the OPT model family on the SuperGLUE benchmark and two generative tasks. 
The experiments show that LeZO accelerates training without compromising the performance of ZO optimization.
Specifically, it achieves over $3 \times$ speedup compared to MeZO on the SST-2, BoolQ, and Copa tasks.

## item_id: m_1823

TITLE: Data-Efficient Image Recognition with Contrastive Predictive Coding

ABSTRACT: Human observers can learn to recognize new categories of objects from a handful of examples, yet doing so with machine perception remains an open challenge. We hypothesize that data-efficient recognition is enabled by representations which make the variability in natural signals more predictable, as suggested by recent perceptual evidence. We therefore revisit and improve Contrastive Predictive Coding, a recently-proposed unsupervised learning framework, and arrive at a representation which enables generalization from small amounts of labeled data. When provided with only 1% of ImageNet labels (i.e. 13 per class), this model retains a strong classification performance, 73% Top-5 accuracy, outperforming supervised networks by 28% (a 65% relative improvement) and state-of-the-art semi-supervised methods by 14%. We also find this representation to serve as a useful substrate for object detection on the PASCAL-VOC 2007 dataset, approaching the performance of representations trained with a fully annotated ImageNet dataset.

## item_id: m_1824

TITLE: Posthoc Privacy guarantees for neural network queries

ABSTRACT: Cloud based machine learning inference is an emerging paradigm where users share their data with a service provider. Due to increased concerns over data privacy, recent works have proposed using Adversarial Representation Learning (ARL) to learn a privacy-preserving encoding of sensitive user data before it is shared with an untrusted service provider. Traditionally, the privacy of these encodings is evaluated empirically as they lack formal guarantees. In this work, we develop a new framework that provides formal privacy guarantees for an arbitrarily trained neural network by linking its local Lipschitz constant with its local sensitivity. To utilize local sensitivity for guaranteeing privacy, we extend the Propose-Test-Release(PTR) framework to make it tractable for neural network based queries. We verify the efficacy of our framework experimentally on real-world datasets and elucidate the role of ARL in improving the privacy-utility tradeoff.

## item_id: m_1825

TITLE: Unifying Regularisation Methods for Continual Learning

ABSTRACT: Continual Learning addresses the challenge of learning a number of different distributions sequentially. The goal of maintaining knowledge of earlier distributions without re-accessing them starkly conflicts with standard SGD training for artificial neural networks. An influential method to tackle this are so-called regularisation approaches. They measure the importance of each parameter for modelling a given distribution and subsequently protect important parameters from large changes. In the literature, three ways to measure parameter importance have been put forward and they have inspired a large body of follow-up work. Here, we present strong theoretical and empirical evidence that these three methods, Elastic Weight Consolidation (EWC), Synaptic Intelligence (SI) and Memory Aware Synapses (MAS), all approximate the Fisher Information. Only EWC intentionally relies on the Fisher, while the other two methods stem from rather different motivations. We find that for SI the relation to the Fisher -- and in fact its performance -- is due to a previously unknown bias. Altogether, this unifies a large body of regularisation approaches. It also provides the first theoretical explanation for  the effectiveness of SI- and MAS-based algorithms and offers theoretically justified versions of these algorithms. From a practical viewpoint, our insights offer computational speed-ups and uncover conditions needed for different algorithms to work.

## item_id: m_1826

TITLE: And the Bit Goes Down: Revisiting the Quantization of Neural Networks

ABSTRACT: In this paper, we address the problem of reducing the memory footprint of convolutional network architectures. We introduce a vector quantization method that aims at preserving the quality of the reconstruction of the network outputs rather than its weights. The principle of our approach is that it minimizes the loss reconstruction error for in-domain inputs. Our method only requires a set of unlabelled data at quantization time and allows for efficient inference on CPU by using byte-aligned codebooks to store the compressed weights. We validate our approach by quantizing a high performing ResNet-50 model to a memory size of 5MB (20x compression factor) while preserving a top-1 accuracy of 76.1% on ImageNet object classification and by compressing a Mask R-CNN with a 26x factor.

## item_id: m_1827

TITLE: Attend, Adapt and Transfer: Attentive Deep Architecture for Adaptive Transfer from multiple sources in the same domain

ABSTRACT: Transferring knowledge from prior source tasks in solving a new target task can be useful in several learning applications. The application of transfer poses two serious challenges which have not been adequately addressed. First, the agent should be able to avoid negative transfer, which happens when the transfer hampers or slows down the learning instead of helping it. Second, the agent should be able to selectively transfer, which is the ability to select and transfer from different and multiple source tasks for different parts of the state space of the target task. We propose A2T (Attend Adapt and Transfer), an attentive deep architecture which adapts and transfers from these source tasks. Our model is generic enough to effect transfer of either policies or value functions. Empirical evaluations on different learning algorithms show that A2T is an effective architecture for transfer by being able to avoid negative transfer while transferring selectively from multiple source tasks in the same domain.

## item_id: m_1828

TITLE: Neural Program Search: Solving Data Processing Tasks from Description and Examples

ABSTRACT: We present a Neural Program Search, an algorithm to generate programs from natural language description and a small number of input / output examples. The algorithm combines methods from Deep Learning and Program Synthesis fields by designing rich domain-specific language (DSL) and defining efficient search algorithm guided by a Seq2Tree model on it. To evaluate the quality of the approach we also present a semi-synthetic dataset of descriptions with test examples and corresponding programs. We show that our algorithm significantly outperforms sequence-to-sequence model with attention baseline.

## item_id: m_1829

TITLE: Discriminator-Actor-Critic: Addressing Sample Inefficiency and Reward Bias in Adversarial Imitation Learning

ABSTRACT: We identify two issues with the family of algorithms based on the Adversarial Imitation Learning framework. The first problem is implicit bias present in the reward functions used in these algorithms. While these biases might work well for some environments, they can also lead to sub-optimal behavior in others. Secondly, even though these algorithms can learn from few expert demonstrations, they require a prohibitively large number of interactions with the environment in order to imitate the expert for many real-world applications. In order to address these issues, we propose a new algorithm called Discriminator-Actor-Critic that uses off-policy Reinforcement Learning to reduce policy-environment interaction sample complexity by an average factor of 10. Furthermore, since our reward function is designed to be unbiased, we can apply our algorithm to many problems without making any task-specific adjustments. 

## item_id: m_1830

TITLE: Energy-based Generative Adversarial Networks

ABSTRACT: We introduce the "Energy-based Generative Adversarial Network" model (EBGAN) which views the discriminator as an energy function that attributes low energies to the regions near the data manifold and higher energies to other regions. Similar to the probabilistic GANs, a generator is seen as being trained to produce contrastive samples with minimal energies, while the discriminator is trained to assign high energies to these generated samples. Viewing the discriminator as an energy function allows to use a wide variety of architectures and loss functionals in addition to the usual binary classifier with logistic output. Among them, we show one instantiation of EBGAN framework as using an auto-encoder architecture, with the energy being the reconstruction error, in place of the discriminator. We show that this form of EBGAN exhibits more stable behavior than regular GANs during training. We also show that a single-scale architecture can be trained to generate high-resolution images.

## item_id: m_1831

TITLE: Support Regularized Sparse Coding and Its Fast Encoder

ABSTRACT: Sparse coding represents a signal by a linear combination of only a few atoms of a learned over-complete dictionary. While sparse coding exhibits compelling performance for various machine learning tasks, the process of obtaining sparse code with fixed dictionary is independent for each data point without considering the geometric information and manifold structure of the entire data. We propose Support Regularized Sparse Coding (SRSC) which produces sparse codes that account for the manifold structure of the data by encouraging nearby data in the manifold to choose similar dictionary atoms. In this way, the obtained support regularized sparse codes capture the locally linear structure of the data manifold and enjoy robustness to data noise. We present the optimization algorithm of SRSC with theoretical guarantee for the optimization over the sparse codes. We also propose a feed-forward neural network termed Deep Support Regularized Sparse Coding (Deep-SRSC) as a fast encoder to approximate the sparse codes generated by SRSC. Extensive experimental results demonstrate the effectiveness of SRSC and Deep-SRSC.

## item_id: m_1832

TITLE: Hyperbolic Attention Networks

ABSTRACT: Recent approaches have successfully demonstrated the benefits of learning the parameters of shallow networks in hyperbolic space. We extend this line of work by imposing hyperbolic geometry on the embeddings used to compute the ubiquitous attention mechanisms for different neural networks architectures. By only changing the geometry of embedding of object representations, we can use the embedding space more efficiently without increasing the number of parameters of the model. Mainly as the number of objects grows exponentially for any semantic distance from the query, hyperbolic geometry  --as opposed to Euclidean geometry-- can encode those objects without having any interference. Our method shows improvements in generalization on neural machine translation on WMT'14 (English to German), learning on graphs (both on synthetic and real-world graph tasks) and visual question answering (CLEVR) tasks while keeping the neural representations compact.

## item_id: m_1833

TITLE: Understanding Zero-shot Adversarial Robustness for Large-Scale Models

ABSTRACT: Pretrained large-scale vision-language models like CLIP have exhibited strong generalization over unseen tasks. Yet imperceptible adversarial perturbations can significantly reduce CLIP's performance on new tasks. In this work, we identify and explore the problem of adapting large-scale models for zero-shot adversarial robustness. We first identify two key factors during model adaption--training losses and adaptation methods--that affect the model's zero-shot adversarial robustness. We then propose a text-guided contrastive adversarial training loss, which aligns the text embeddings and the adversarial visual features with contrastive learning on a small set of training data. We apply this training loss to two adaption methods, model finetuning and visual prompt tuning. We find that visual prompt tuning is more effective in the absence of texts, while finetuning wins in the existence of text guidance. Overall, our approach significantly improves the zero-shot adversarial robustness over CLIP, seeing an average improvement of 31 points over ImageNet and 15 zero-shot datasets. We hope this work can shed light on understanding the zero-shot adversarial robustness of large-scale models. 

## item_id: m_1834

TITLE: Towards Well-distributed Generative Networks Using Adversarial Autoencoders

ABSTRACT: In addition to perceptual quality, the usefulness of a generative model depends on how closely the generated distribution matches the training distribution. Previous efforts in adversarial generative models have focused on reducing "mode collapse", but this term, roughly meaning being unable to generate certain parts of the data distribution, is not clearly defined. In addition, being able to generate every image in the data distribution does not imply reproducing the correct distribution, which additionally requires that each image occur at the same frequency in the generated images as in the training data. Due to the lack of a precise definition and measurement, it has been difficult to evaluate the success of these efforts in producing the correct distribution. In this work we proposes an autoencoder-based adversarial training framework, which ensures that the density of the encoder's aggregate output distribution closely matches the prior latent distribution, which in turn ensures that the distribution of images generated from randomly sampled latent code will closely match the training data. To evaluate our method, we introduce the 3DShapeHD dataset, which has a moderate complexity that goes beyond simplistic toy datasets, but also a exactly known generating process and distribution of features, which enables precise measurements. Using the reduced chi-square statistic, we show significant improvement in the accuracy of the distribution of generated samples. The results also demonstrate that the enhanced diversity of our model improves the ability to generate uncommon features in real-world datasets.

## item_id: m_1835

TITLE: An Information Theoretic Approach to Distributed Representation Learning

ABSTRACT: The problem of distributed representation learning is one in which multiple sources of information X1,...,XK are processed separately so as to extract useful information about some statistically correlated ground truth Y. We investigate this problem from information-theoretic grounds. For both discrete memoryless (DM) and memoryless vector Gaussian models, we establish fundamental limits of learning in terms of optimal tradeoffs between accuracy and complexity. We also develop a variational bound on the optimal tradeoff that generalizes the evidence lower bound (ELBO) to the distributed setting. Furthermore, we provide a variational inference type algorithm that allows to compute this bound and in which the mappings are parametrized by neural networks and the bound approximated by Markov sampling and optimized with stochastic gradient descent. Experimental results on synthetic and real datasets are provided to support the efficiency of the approaches and algorithms which we develop in this paper.

## item_id: m_1836

TITLE: From Variational to Deterministic Autoencoders

ABSTRACT:  Variational Autoencoders (VAEs) provide a theoretically-backed and popular framework for deep generative models. However, learning a VAE from data poses still unanswered theoretical questions and considerable practical challenges. In this work, we propose an alternative framework for generative modeling that is simpler, easier to train, and deterministic, yet has many of the advantages of the VAE. We observe that sampling a stochastic encoder in a Gaussian VAE can be interpreted as simply injecting noise into the input of a deterministic decoder. We investigate how substituting this kind of stochasticity, with other explicit and implicit regularization schemes, can lead to an equally smooth and meaningful latent space without having to force it to conform to an arbitrarily chosen prior. To retrieve a generative mechanism to sample new data points, we introduce an ex-post density estimation step that can be readily applied to the proposed framework as well as existing VAEs, improving their sample quality. We show, in a rigorous empirical study, that the proposed regularized deterministic autoencoders are able to generate samples that are comparable to, or better than, those of VAEs and more powerful alternatives when applied to images as well as to structured data such as molecules. 

## item_id: m_1837

TITLE: Policy improvement by planning with Gumbel

ABSTRACT: AlphaZero is a powerful reinforcement learning algorithm based on approximate policy iteration and tree search. However, AlphaZero can fail to improve its policy network, if not visiting all actions at the root of a search tree. To address this issue, we propose a policy improvement algorithm based on sampling actions without replacement. Furthermore, we use the idea of policy improvement to replace the more heuristic mechanisms by which AlphaZero selects and uses actions, both at root nodes and at non-root nodes. Our new algorithms, Gumbel AlphaZero and Gumbel MuZero, respectively without and with model-learning, match the state of the art on Go, chess, and Atari, and significantly improve prior performance when planning with few simulations.

## item_id: m_1838

TITLE: Learnable Expansion of Graph Operators for Multi-Modal Feature Fusion

ABSTRACT: In computer vision tasks, features often come from diverse representations, domains (e.g., indoor and outdoor), and modalities (e.g., text, images, and videos). Effectively fusing these features is essential for robust performance, especially with the availability of powerful pre-trained models like vision-language models. However, common fusion methods, such as concatenation, element-wise operations, and non-linear techniques, often fail to capture structural relationships, deep feature interactions, and suffer from inefficiency or misalignment of features across domains or modalities. In this paper, we shift from high-dimensional feature space to a lower-dimensional, interpretable graph space by constructing relationship graphs that encode feature relationships at different levels, e.g., clip, frame, patch, token, etc. To capture deeper interactions, we expand graphs through iterative graph relationship updates and introduce a learnable graph fusion operator to integrate these expanded relationships for more effective fusion. Our approach is relationship-centric, operates in a homogeneous space, and is mathematically principled, resembling element-wise relationship score aggregation via multilinear polynomials. We demonstrate the effectiveness of our graph-based fusion method on video anomaly detection, showing strong performance across multi-representational, multi-modal, and multi-domain feature fusion tasks.

## item_id: m_1839

TITLE: Transformational Sparse Coding

ABSTRACT: 
A fundamental problem faced by object recognition systems is that
objects and their features can appear in different locations, scales
and orientations. Current deep learning methods attempt to achieve
invariance to local translations via pooling, discarding the locations
of features in the process.  Other approaches explicitly learn
transformed versions of the same feature, leading to representations
that quickly explode in size. Instead of discarding the rich and
useful information about feature transformations to achieve
invariance, we argue that models should learn object features
conjointly with their transformations to achieve equivariance.  We
propose a new model of unsupervised learning based on sparse coding
that can learn object features jointly with their affine
transformations directly from images. Results based on learning from
natural images indicate that our approach
matches the reconstruction quality of traditional sparse coding but
with significantly fewer degrees of freedom while simultaneously
learning transformations from data. These results open the door to
scaling up unsupervised learning to allow deep feature+transformation
learning in a manner consistent with the ventral+dorsal stream
architecture of the primate visual cortex.

## item_id: m_1840

TITLE: DppNet: Approximating Determinantal Point Processes with Deep Networks

ABSTRACT: Determinantal Point Processes (DPPs) provide an elegant and versatile way to sample sets of items that balance the point-wise quality with the set-wise diversity of selected items. For this reason, they have gained prominence in many machine learning applications that rely on subset selection. However, sampling from a DPP over a ground set of size N is a costly operation, requiring in general an O(N^3) preprocessing cost and an O(Nk^3) sampling cost for subsets of size k. We approach this problem by introducing DppNets: generative deep models that produce DPP-like samples for arbitrary ground sets.  We develop an inhibitive attention mechanism based on transformer networks that captures a notion of dissimilarity between feature vectors.  We show theoretically that such an approximation is sensible as it maintains the guarantees of inhibition or dissimilarity that makes DPP so powerful and unique.  Empirically, we demonstrate that samples from our model receive high likelihood under the more expensive DPP alternative.

## item_id: m_1841

TITLE: Learnability of Discrete Dynamical Systems under High Classification Noise

ABSTRACT: Due to the important role of discrete dynamical systems in modeling real-world cascading phenomena on networks, problems for learning such systems have garnered considerable attention in ML. However, existing studies on this topic typically assume that the training data is noise-free, an assumption that is often impractical. In this work, we address this gap by investigating a more realistic and challenging setting: learning discrete dynamical systems from data contaminated with noise. Towards this end, we present efficient noise-tolerant learning algorithms that provide provable performance guarantees under the PAC model, and establish tight bounds on sample complexity. We show that, even in the presence of noise, the proposed learner only needs a small training set to infer a system. Notably, the number of training samples required by the algorithm in the noisy setting is the same (to within a constant factor) as the information-theoretic upper bound in the noise-free scenario. Further, the number of noisy training samples used by the algorithm is only a logarithmic factor higher than the best-known lower bound. Through experimental studies, we evaluate the empirical performance of the algorithms on both synthetic and real-world networks.

## item_id: m_1842

TITLE: On Neurons Invariant to Sentence Structural Changes in Neural Machine Translation

ABSTRACT: To gain insight into the role neurons play, we study the activation patterns corresponding to meaning-preserving paraphrases (e.g., active-passive). We compile a dataset of controlled syntactic paraphrases in English with their reference German translations and demonstrate our model-agnostic approach with the Transformer translation model. First, we identify neurons that correlate across paraphrases and dissect the observed correlation into possible confounds. Although lower-level components are found as the cause of similar activations, no sentence-level semantics or syntax are detected locally. Later, we manipulate neuron activations to influence translation towards a particular syntactic form. We find that a simple value shift is effective, and more so when many neurons are modified. These suggest that complex syntactic constructions are indeed encoded in the model.  We conclude by discussing how to better manipulate it using the correlations we first obtained.

## item_id: m_1843

TITLE: Bootstrap Your Own Noise: Denoising Adaptive Noise in Diffusion Models for SSL

ABSTRACT: We introduce Bootstrap Your Own Noise (BYON), a self-supervised pretraining framework that unifies denoising diffusion with uncertainty-guided contrastive learning to enhance both local and global feature representations. BYON forms a self-reinforcing loop: contrastive learning improves reconstruction quality, and in turn, improved reconstructions refine feature alignment. A Semantic Uncertainty Estimation (SUE) module adaptively reweights contrastive updates based on reconstruction quality, while an Image-specific Adaptive Noise (IAN) adaptively modulates the noise intensity at the image level based on token saliency, perturbing more informative images more strongly.
BYON consistently boosts performance on image classification, semantic segmentation, object detection, instance segmentation, and fine-grained visual classification (FGVC) tasks. To ensure reproducibility, the code is available in the Supplementary material.

## item_id: m_1844

TITLE: CTRL: Graph condensation via crafting rational trajectory matching

ABSTRACT: Training on large-scale graphs has achieved remarkable results in graph representation learning, but its cost and storage have raised growing concerns. Generally,
existing graph distillation methods address these issues by employing gradient
matching, but these strategies primarily emphasize matching directions of the
gradients. We empirically demonstrate this can result in deviations in the matching
trajectories and disparities in the frequency distribution. Accordingly, we propose
CrafTing RationaL trajectory (CTRL), a novel graph dataset distillation method.
CTRL introduces gradient magnitude matching during the gradient matching process by incorporating the Euclidean distance into the criterion. Additionally, to
prevent the disregard for the evenness of feature distribution and the lack of variation that the naive random sampling initialization may introduce, we adopt a simple
initialization approach that ensures evenly distributed features. CTRL not only
achieves state-of-the-art performances in 34 cases of experiments on 12 datasets
with lossless performances on 5 datasets but can also be easily integrated into other
graph distillation methods based on gradient matching.

## item_id: m_1845

TITLE: MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models

ABSTRACT: Diffusion language models, as a promising alternative to traditional autoregressive (AR) models, enable faster generation and richer conditioning on bidirectional context. However, they suffer from a key discrepancy between training and inference: during inference, MDLMs progressively reveal the structure of the generated sequence by producing fewer and fewer masked tokens, whereas this structure is ignored in training as tokens are masked at random. Although this discrepancy between training and inference can lead to suboptimal performance, it has been largely overlooked by previous works, leaving closing this gap between the two stages an open problem. To address this, we frame the problem of learning effective denoising trajectories as a sequential decision-making problem and use the resulting framework to apply reinforcement learning. We propose a novel Masked Diffusion Policy Optimization (MDPO) to exploit the Markov property diffusion possesses and explicitly train the model under the same progressive refining schedule used at inference. MDPO matches the performance of the previous state-of-the-art (SOTA) method with 60× fewer gradient updates, while achieving average improvements of 9.6\% on MATH500 and 54.2\% on Countdown over SOTA when trained within the same number of weight updates. Additionally, we improve the remasking strategy of MDLMs as a plug-in inference replacement to overcome the limitation that the model cannot refine tokens flexibly. This training-free method, termed Running Confidence Remasking (RCR), consistently enhances performance and provides further improvements when used with MDPO. Our findings establish great potential for investigating the discrepancy between pre-training and inference of MDLMs. To support reproducibility, we will release code upon acceptance.

## item_id: m_1846

TITLE: Learning Robust Models by Countering Spurious Correlations

ABSTRACT: Machine learning has demonstrated remarkable prediction accuracy over i.i.d data, but the accuracy often drops when tested with data from another distribution. One reason behind this accuracy drop is the reliance of models on the features that are only associated with the label in the training distribution, but not the test distribution. This problem is usually known as spurious correlation, confounding factors, or dataset bias. In this paper, we formally study the generalization error bound for this setup with the knowledge of how the spurious features are associated with the label. We also compare our analysis to the widely-accepted domain adaptation error bound and show that our bound can be tighter, with more assumptions that we consider realistic. Further, our analysis naturally offers a set of solutions for this problem, linked to established solutions in various topics about robustness in general, and these solutions all require some understandings of how the spurious features are associated with the label. Finally, we also briefly discuss a method that does not require such an understanding.

## item_id: m_1847

TITLE: Distributed Transfer Learning for Deep Convolutional Neural Networks by Basic Probability Assignment

ABSTRACT: Transfer learning is a popular practice in deep neural networks, but fine-tuning of a large number of parameters is a hard challenge due to the complex wiring of neurons between splitting layers and imbalance class distributions of original and transferred domains. Recent advances in evidence theory show that in an imbalance multiclass learning problem, optimizing of proper objective functions based on contingency tables prevents biases towards high-prior classes. Transfer learning usually deals with highly non-convex objectives and local minima in deep neural architectures. We propose a novel distributed transfer learning to tackle both optimization complexity and class-imbalance problem jointly. Our solution imposes separated greedy regularization to each individual convolutional filter to make single-filter neural networks such that the minority classes perform as the majority ones. Then, basic probability assignment from evidence theory boosts these distributed networks to improve the recognition performance on the target domains. Our experiments on several standard datasets confirm the consistent improvement as a result of our distributed transfer learning strategy.

## item_id: m_1848

TITLE: End-to-end learning of pharmacological assays from high-resolution microscopy images

ABSTRACT: Predicting the outcome of pharmacological assays based on high-resolution microscopy
images of treated cells is a crucial task in drug discovery which tremendously
increases discovery rates. However, end-to-end learning on these images
with convolutional neural networks (CNNs) has not been ventured for this task
because it has been considered infeasible and overly complex. On the largest
available public dataset, we compare several state-of-the-art CNNs trained in an
end-to-end fashion with models based on a cell-centric approach involving segmentation.
We found that CNNs operating on full images containing hundreds
of cells perform significantly better at assay prediction than networks operating
on a single-cell level. Surprisingly, we could predict 29% of the 209 pharmacological
assays at high predictive performance (AUC > 0.9). We compared a
novel CNN architecture called “GapNet” against four competing CNN architectures
and found that it performs on par with the best methods and at the same time
has the lowest training time. Our results demonstrate that end-to-end learning on
high-resolution imaging data is not only possible but even outperforms cell-centric
and segmentation-dependent approaches. Hence, the costly cell segmentation and
feature extraction steps are not necessary, in fact they even hamper predictive performance.
Our work further suggests that many pharmacological assays could
be replaced by high-resolution microscopy imaging together with convolutional
neural networks.

## item_id: m_1849

TITLE: Toward Learning Generalized Cross-Problem Solving Strategies for Combinatorial Optimization

ABSTRACT: Combinatorial optimization (CO) problems are fundamental across various domains, with many sharing similarities in optimization objectives, decision variables, and constraints. Many traditional algorithms perform well on related problems using similar solution strategies, highlighting the commonality in solving different problems. However, most machine learning approaches treat each CO problem in isolation, failing to capitalize on the underlying relationships between problems. In this paper, we investigate the potential to learn generalized solving strategies that capture the shared structure among different CO problems, enabling easier adaptation to related tasks. To this end, we propose to first divide the model architecture into three components: a header, an encoder, and a decoder; where The header and decoder address problem-specific inputs and outputs, while the encoder is designed to learn shared strategies that generalize across different problems.  To ensure this, we enforce alignment in the optimization directions of the encoder across problems, maintaining consistency in both gradient directions and magnitudes to harmonize optimization processes. This is achieved by introducing the additional problem-specific rotation matrices and loss weights to steer the gradients, which are updated via a gradient consistency loss. Extensive experiments on six CO problems demonstrate that our method enhances the model's ability to capture shared solving strategies across problems. We show that the learned encoder on several problems can directly perform comparably on new problems to models trained from scratch, highlighting its potential to support developing the foundational model for combinatorial optimization. Source code will be made publicly available.

## item_id: m_1850

TITLE: PolarNet: Learning to Optimize Polar Keypoints for Keypoint Based Object Detection

ABSTRACT: A variety of anchor-free object detectors have been actively proposed as possible alternatives to the mainstream anchor-based detectors that often rely on complicated design of anchor boxes. Despite achieving promising performance on par with anchor-based detectors, the existing anchor-free detectors such as FCOS or CenterNet predict objects based on standard Cartesian coordinates, which often yield poor quality keypoints. Further, the feature representation is also scale-sensitive. In this paper, we propose a new anchor-free keypoint based detector ``PolarNet", where keypoints are represented as a set of Polar coordinates instead of Cartesian coordinates. The ``PolarNet" detector learns offsets pointing to the corners of objects in order to learn high quality keypoints. Additionally, PolarNet uses features of corner points to localize objects, making the localization scale-insensitive. Finally in our experiments, we show that PolarNet, an anchor-free detector, outperforms the existing anchor-free detectors, and it is able to achieve highly competitive result on COCO test-dev benchmark ($47.8\%$ and $50.3\%$ AP under the single-model single-scale and multi-scale testing) which is on par with the state-of-the-art two-stage anchor-based object detectors. The code and the models are available at https://github.com/XiongweiWu/PolarNetV1

## item_id: m_1851

TITLE: Test-Time Training for Out-of-Distribution Generalization

ABSTRACT: We introduce a general approach, called test-time training, for improving the performance of predictive models when test and training data come from different distributions. Test-time training turns a single unlabeled test instance into a self-supervised learning problem, on which we update the model parameters before making a prediction on the test sample. We show that this simple idea leads to surprising improvements on diverse image classification benchmarks aimed at evaluating robustness to distribution shifts. Theoretical investigations on a convex model reveal helpful intuitions for when we can expect our approach to help.

## item_id: m_1852

TITLE: Contractive error feedback for gradient compression

ABSTRACT: 
On-device memory concerns in distributed deep learning are becoming more severe due to i) the growth of model size in multi-GPU training, and ii) the adoption of neural networks for federated learning on IoT devices with limited storage. In such settings, this work deals with memory issues emerging with communication efficient methods. To tackle associated challenges, key advances are that i) instead of EFSGD that inefficiently manages memory, the sweet spot of convergence and memory usage can be attained via what is here termed contractive error feedback (ConEF); and, ii) communication efficiency in ConEF should be achieved by biased and allreducable gradient compression. ConEF is validated on various learning tasks that include image classification, language modeling, and machine translation. ConEF saves 80% – 90% of the extra memory in EFSGD with almost no loss on test performance, while also achieving 1.3x – 5x speedup of SGD.

## item_id: m_1853

TITLE: Reinforcement Learning for Control with Probabilistic Stability Guarantee

ABSTRACT: Reinforcement learning is promising to control dynamical systems for which the traditional control methods are hardly applicable. However, in control theory, the stability of a closed-loop system can be hardly guaranteed using the policy/controller learned solely from samples. In this paper, we will combine Lyapunov's method in control theory and stochastic analysis to analyze the mean square stability of MDP in a model-free manner. Furthermore, the finite sample bounds on the probability of stability are derived as a function of the number M and length T of the sampled trajectories. And we show that there is a lower bound on T and the probability is much more demanding for M than T. Based on the theoretical results, a REINFORCE like algorithm is proposed to learn the controller and the Lyapunov function simultaneously. 

## item_id: m_1854

TITLE: Unsupervised Adversarial Anomaly  Detection using One-Class Support Vector Machines

ABSTRACT: Anomaly detection discovers regular patterns in unlabeled data and identifies the non-conforming data points, which in some cases are the result of malicious attacks by adversaries. Learners such as One-Class Support Vector Machines (OCSVMs) have been successfully in anomaly detection, yet their performance may degrade significantly in the presence of sophisticated adversaries, who target the algorithm itself by compromising the integrity of the training data. With the rise in the use of machine learning in mission critical day-to-day activities where errors may have significant consequences, it is imperative that machine learning systems are made secure. To address this, we propose a defense mechanism that is based on a contraction of the data, and we test its effectiveness using OCSVMs. The proposed approach introduces a layer of uncertainty on top of the OCSVM learner, making it infeasible for the adversary to guess the specific configuration of the learner. We theoretically analyze the effects of adversarial perturbations on the separating margin of OCSVMs and provide empirical evidence on several benchmark datasets, which show that by carefully contracting the data in low dimensional spaces, we can successfully identify adversarial samples that would not have been identifiable in the original dimensional space. The numerical results show that the proposed method improves OCSVMs performance significantly (2-7%)

## item_id: m_1855

TITLE: TANGRAM: A Dataset for FPGA-Based Heterogeneous Systems-on-Chip Optimization

ABSTRACT: With the end of Moore's Law and Dennard Scaling, high-performance computing (HPC) architectures are evolving to include large Field Programmable Gate Arrays (FPGAs) to improve efficiency. Identifying the optimal configuration for such FPGAs, in terms of the number and type of CPUs, hardware accelerators, and memory channels, is crucial for the creation of efficient computing platforms. However, the complexity of the design space, the difficulty of modeling the interactions between the concurrently executed applications, and the strict time-to-market requirements fostered the use of heuristics to perform the exploration, thus leading to the identification of suboptimal solutions with no quality guarantees. To support the exploration of new systematic methodologies for the design of FPGA-based heterogeneous multi-core architectures, we present TANGRAM, a dataset composed of $40,000$ performance and resource consumption results of more than different designs, collected from two high-end FPGAs executing heterogeneous and concurrent applications. To assess the suitability of this dataset for machine-learning-based optimization strategies, we tested it with some baseline regression methodologies, showing the possibility of accurately predicting the performance of multiple applications running on the same system.

## item_id: m_1856

TITLE: Generalizing Cross Entropy Loss with a Beta Proper Composite Loss: An Improved Loss Function for Open Set Recognition

ABSTRACT: Open set recognition involves identifying data instances encountered during test time that do not belong to known classes in the training set. The majority of recent deep learning approaches to open set recognition use a cross entropy loss to train their networks. Surprisingly, other loss functions are seldom used. In our work, we explore generalizing cross entropy with a Beta loss. This Beta loss is a proper composite loss with a Beta weight function. This weight function adds the flexibility of putting more emphasis on different parts of the observation-conditioned class probability (i.e. $P(Y|X)$) range during training. We show that the flexibility gained through this is Beta loss function produces consistent improvements over cross entropy loss for open set recognition and produces state of the art results relative to recent methods.

## item_id: m_1857

TITLE: AntMan: Sparse Low-Rank Compression To Accelerate RNN Inference

ABSTRACT: Wide adoption of complex RNN based models is hindered by their inference performance, cost and memory requirements. To address this issue, we develop AntMan, combining structured sparsity with low-rank decomposition synergistically, to reduce model computation, size and execution time of RNNs while attaining desired accuracy. AntMan extends knowledge distillation based training to learn the compressed models efficiently. Our evaluation shows that AntMan offers up to 100x computation reduction with less than 1pt accuracy drop for language and machine reading comprehension models. Our evaluation also shows that for a given accuracy target, AntMan produces 5x smaller models than the state-of-art. Lastly, we show that AntMan offers super-linear speed gains compared to theoretical speedup, demonstrating its practical value on commodity hardware.

## item_id: m_1858

TITLE: QuAnt: Quantum Annealing with Learnt Couplings

ABSTRACT: Modern quantum annealers can find high-quality solutions to combinatorial optimisation objectives given as quadratic unconstrained binary optimisation (QUBO) problems. Unfortunately, obtaining suitable QUBO forms in computer vision remains challenging and currently requires problem-specific analytical derivations. Moreover, such explicit formulations impose tangible constraints on solution encodings. In stark contrast to prior work, this paper proposes to learn QUBO forms from data through gradient backpropagation instead of deriving them. As a result, the solution encodings can be  chosen flexibly and compactly. Furthermore, our methodology is general and virtually independent of the specifics of the target problem type. We demonstrate the advantages of learnt  QUBOs on the diverse problem types of graph matching, 2D point cloud alignment and 3D rotation estimation. Our results are competitive with the previous quantum state of the art while requiring much fewer logical and physical qubits, enabling our method to scale to larger problems. The code and the new dataset are available at https://4dqv.mpi-inf.mpg.de/QuAnt/.

## item_id: m_1859

TITLE: Tra-MoE: Scaling Trajectory Prediction Models for Adaptive Policy Conditioning

ABSTRACT: Scale is a primary factor that influences the performance and generalization of a robot learning system. In this paper, we aim to scale up the trajectory prediction model by using broad out-of-domain data to improve its robustness and generalization ability. Trajectory model is designed to predict any-point trajectories in the current frame given an instruction and can provide detailed control guidance for robotic policy learning. To handle the diverse out-of-domain data distribution, we propose a sparsely-gated MoE (\textbf{Top-1} gating strategy) architecture for trajectory model, coined as \textbf{Tra-MoE}. The sparse activation design enables good balance between parameter cooperation and specialization, effectively benefiting from large-scale out-of-domain data while maintaining constant FLOPs per token. In addition, we further introduce an adaptive policy conditioning technique by learning 2D mask representations for predicted trajectories, which is explicitly aligned with image observations to guide policy prediction more flexibly. We perform experiments on both simulation and real-world scenarios to verify the effectiveness of our Tra-MoE and adaptive policy conditioning technique. We jointly train the Tra-MoE model on all 130 tasks in the LIBERO benchmark and conduct a comprehensive empirical analysis, demonstrating that our Tra-MoE consistently exhibits superior performance compared to the dense baseline model, even when the latter is scaled to match Tra-MoE's parameter count.

## item_id: m_1860

TITLE: Meta-Learning with Individualized Feature Space for Few-Shot Classification

ABSTRACT: Meta-learning provides a promising learning framework to address few-shot classification tasks. In existing meta-learning methods, the meta-learner is designed to learn about model optimization, parameter initialization, or similarity metric. Differently, in this paper, we propose to learn how to create an individualized feature embedding specific to a given query image for better classifying, i.e., given a query image, a specific feature embedding tailored for its characteristics is created accordingly, leading to an individualized feature space in which the query image can be more accurately classified.  Specifically, we introduce a kernel generator as meta-learner to learn to construct feature embedding for query images. The kernel generator acquires meta-knowledge of generating adequate convolutional kernels for different query images during training, which can generalize to unseen categories without fine-tuning. In two standard few-shot classification data sets, i.e. Omniglot, and \emph{mini}ImageNet, our method shows highly competitive performance. 

## item_id: m_1861

TITLE: Histogram-Guided Source-Free Domain Adaptive Regression

ABSTRACT: Source-Free Domain Adaptation (SFDA) enables model adaptation under distribution shifts without access to source data, making it an appealing solution for privacy-sensitive applications. Despite being a fundamental problem in machine learning, regression remains largely underexplored in SFDA, where most existing work has focused predominantly on classification tasks. To bridge this gap, we propose a novel algorithm that leverages sample-wise, histogram-informed supervisory signals to refine pseudo-labels under an uncertainty-aware paradigm. This design simultaneously achieves pseudo-label refinement and uncertainty modeling, two key components that are critical for effective adaptation in classification but remain largely absent in regression. We further theoretically show that the resulting histograms exhibit robustness to potential perturbations, supporting reliable SFDA for regression. Empirical results across multiple benchmarks confirm the effectiveness of our method and reveal that histogram-guided learning promotes more compact and structured feature representations, mitigating the inherent challenges of adapting regression models under distribution shift.

## item_id: m_1862

TITLE: Quantization for Rapid Deployment of Deep Neural Networks

ABSTRACT: This paper aims at rapid deployment of the state-of-the-art deep neural networks (DNNs) to energy efficient accelerators without time-consuming fine tuning or the availability of the full datasets.  Converting DNNs in full precision to limited precision is essential in taking advantage of the accelerators with reduced memory footprint and computation power. However, such a task is not trivial since it often requires the full training and validation datasets for profiling the network statistics and fine tuning the networks to recover the accuracy lost after quantization. To address these issues, we propose a simple method recognizing channel-level distribution to reduce the quantization-induced accuracy loss and minimize the required image samples for profiling. We evaluated our method on eleven networks trained on the ImageNet classification benchmark and a network trained on the Pascal VOC object detection benchmark. The results prove that the networks can be quantized into 8-bit integer precision without fine tuning.

## item_id: m_1863

TITLE: ATLPA:ADVERSARIAL TOLERANT LOGIT PAIRING WITH ATTENTION FOR CONVOLUTIONAL NEURAL NETWORK

ABSTRACT: Though deep neural networks have achieved the state of the art performance in visual classification, recent studies have shown that they are all vulnerable to the attack of adversarial examples. To solve the problem, some regularization adversarial training methods, constraining the output label or logit, have been studied. In this paper, we propose a novel regularized adversarial training framework ATLPA,namely Adversarial Tolerant Logit Pairing with Attention. Instead of constraining a hard distribution (e.g., one-hot vectors or logit) in adversarial training, ATLPA uses Tolerant Logit which consists of confidence distribution on top-k classes and captures inter-class similarities at the image level. Specifically, in addition to minimizing the empirical loss, ATLPA encourages attention map for pairs of examples to be similar. When applied to clean examples and their adversarial counterparts, ATLPA improves accuracy on adversarial examples over adversarial training. We evaluate ATLPA with the state of the art algorithms, the experiment results show that our method outperforms these baselines with higher accuracy. Compared with previous work, our work is evaluated under highly challenging PGD attack: the maximum perturbation $\epsilon$ is 64 and 128 with 10 to 200 attack iterations.

## item_id: m_1864

TITLE: Evaluating and Inducing Personality in Pre-trained Language Models

ABSTRACT: Originated as a philosophical quest, personality discerns how individuals differ from each other in terms of thinking, feeling, and behaving. Toward building social machines that work with humans on a daily basis, we are motivated to ask: (1) Do existing Large Language Models (LLMs) possess personalities, akin to their human counterparts? (2) If so, how can we evaluate them? (3) Further, given this evaluation framework, how can we induce a certain personality in a fully controllable fashion? To tackle these three questions, we propose the Machine Personality Inventory (MPI) dataset for evaluating the machine personality; MPI follows standardized personality tests, built upon the Big Five Personality Factors (Big Five) theory and personality assessment inventories. By evaluating models with MPI, we provide the first piece of evidence showing the existence of personality in LLMs. We further devise a Chain Prompting method to induce LLMs with a specific personality in a controllable manner, capable of producing diversified behaviors. We hope to shed light on future studies by adopting personality as the essential guide for various downstream tasks, building more human-like and in situ dialogue agents.

## item_id: m_1865

TITLE:  Topologically faithful image segmentation via induced matching of persistence barcodes

ABSTRACT: Image segmentation is a largely researched field where neural networks find vast applications in many facets of technology.
Some of the most popular approaches to train segmentation networks employ loss functions optimizing pixel-overlap, an objective that is 
insufficient for many segmentation tasks. In recent years, their limitations fueled a growing interest in topology-aware methods, which aim to recover the correct topology of the segmented structures. However, so far, none of the existing approaches achieve a spatially correct matching between the topological features (persistence barcodes) of label (ground truth) and prediction (output of the neural network). 

In this work, we propose the first topologically and feature-wise accurate metric and loss function for supervised image segmentation, which we term TopoMatch. We show how induced matchings guarantee the spatially correct matching between barcodes in a segmentation setting. Furthermore, we propose an efficient algorithm to compute TopoMatch for images. We show that TopoMatch is an interpretable metric to evaluate the topological correctness of segmentations. Moreover, we demonstrate how induced matchings can be used to train segmentation networks and improve the topological correctness of the segmentations across all 6 baseline datasets while preserving volumetric segmentation performance. 

## item_id: m_1866

TITLE: BPRL: A Behavioral Approach to State Representation in Reinforcement Learning

ABSTRACT: Deep Reinforcement Learning (DRL) often suffers from poor sample efficiency and limited generalization in complex, high-dimensional environments. A key challenge is designing effective state representations, which typically requires manual, domain-specific feature engineering. We propose Behavioral Programming Reinforcement Learning (BPRL), a framework that automates the construction of compact, semantically rich state representations. BPRL leverages Behavioral Programming (BP)$-$a scenario-based modeling paradigm$-$to specify the environment's dynamics. The core contribution is that the very same BP model used to define the environment’s logic is also used to $\textit{automatically derive}$ the state representation for the DRL agent. This dual use of the BP model eliminates the need for manual feature design while ensuring that the extracted representations capture both high-level symbolic structure and temporal dependencies. By combining BP's modularity with structured observations, BPRL simplifies environment modeling and enhances agent learning. Experiments across multiple DRL algorithms on MiniGrid benchmarks demonstrate that BPRL substantially improves sample efficiency and asymptotic performance over standard baselines.

## item_id: m_1867

TITLE: Visual Grounding with attention-driven constraint balancing

ABSTRACT: Unlike Object Detection, Visual Grounding task necessitates the detection of an object described by complex free-form language. To simultaneously model such complex semantic and visual representations, recent state-of-the-art studies adopt transformer-based models to fuse features from both modalities, further introducing various modules that modulate visual features to align with the language expressions and eliminate the irrelevant redundant information. However, their loss function, still adopting common Object Detection losses, solely governs the bounding box regression output, failing to fully optimize for the above objectives. To tackle this problem, in this paper, we firstly analyze the attention mechanisms of transformer-based models. Building upon this, we further propose a novel framework named Attention-Driven Constraint Balancing (AttBalance) to optimize the behavior of visual features within language-relevant regions. Extensive experimental results show that our method brings impressive improvements. Specifically, we achieve uniform gains across five different models evaluated on four different benchmarks. Moreover, we attain a new state-of-the-art performance by integrating our method into QRNet.

## item_id: m_1868

TITLE: Cyclophobic Reinforcement Learning

ABSTRACT: In environments with sparse rewards finding a good inductive bias for exploration is crucial to the agent’s success. However, there are two competing goals: novelty search and systematic exploration. While existing approaches such as curiousity- driven exploration find novelty, they sometimes do not systematically explore the whole state space, akin to depth-first-search vs breadth-first-search. In this paper, we propose a new intrinsic reward that is cyclophobic, i.e. it does not reward novelty, but punishes redundancy by avoiding cycles. Augmenting the cyclophobic intrinsic reward with a sequence of hierarchical representations based on the agent’s cropped observations we are able to achieve excellent results in the MiniGrid and MiniHack environments. Both are particularly hard, as they require complex interactions with different objects in order to be solved. Detailed comparisons with previous approaches and thorough ablation studies show that our newly proposed cyclophobic reinforcement learning is vastly more efficient than other state of the art methods.

## item_id: m_1869

TITLE: Necessary and Sufficient Watermark for Large Language Models

ABSTRACT: In recent years, large language models (LLMs) have achieved remarkable performances in various NLP tasks. They can generate texts that are indistinguishable from those written by humans. Such remarkable performance of LLMs increases their risk of being used for malicious purposes, such as generating fake news articles. Therefore, it is necessary to develop methods for distinguishing texts written by LLMs from those written by humans. Watermarking is one of the most powerful methods for achieving this. Although existing watermarking methods have successfully detected text generated by LLMs, they significantly degrade the quality of the generated text. In this study, we propose the Necessary and Sufficient Watermark (NS-Watermark) for inserting watermarks into generated texts without degrading the text quality. More specifically, we derive minimum constraints required to be imposed on the generated texts to distinguish whether LLMs or humans write the texts. Then, we formulate NS-Watermark as a constrained optimization problem and propose an efficient algorithm to solve it. Through the experiments, we demonstrate that NS-Watermark can generate more natural texts than existing watermarking methods and distinguish more accurately between texts written by LLMs and those written by humans. Especially in machine translation tasks, the NS-Watermark can outperform the existing watermarking method by up to $30$ BLEU scores.

## item_id: m_1870

TITLE: Improved Architectures for Computer Go

ABSTRACT: AlphaGo trains policy networks with both supervised and reinforcement learning and makes different policy networks play millions of games so as to train a value network. The reinforcement learning part requires massive ammount of computation. We propose to train networks for computer Go so that given accuracy is reached with much less examples. We modify the architecture of the networks in order to train them faster and to have better accuracy in the end.

## item_id: m_1871

TITLE: Online Continual Learning for Interactive Instruction Following Agents

ABSTRACT: In learning an embodied agent executing daily tasks via language directives, the literature largely assumes that the agent learns all training data at the beginning. We argue that such a learning scenario is less realistic, since a robotic agent is supposed to learn the world continuously as it explores and perceives it. To take a step towards a more realistic embodied agent learning scenario, we propose two continual learning setups for embodied agents; learning new behaviors (Behavior Incremental Learning, Behavior-IL) and new environments (Environment Incremental Learning, Environment-IL) For the tasks, previous ‘data prior’ based continual learning methods maintain logits for the past tasks. However, the stored information is often insufficiently learned information and requires task boundary information, which might not always be available. Here, we propose to update them based on confidence scores without task boundary information (i.e., task-free) in a moving average fashion, named Confidence-Aware Moving Average (CAMA). In the proposed challenging Behavior-IL and Environment-IL setups, our simple CAMA outperforms prior arts in our empirical validations by noticeable margins.

## item_id: m_1872

TITLE: ShEPhERD: Diffusing shape, electrostatics, and pharmacophores for bioisosteric drug design

ABSTRACT: Engineering molecules to exhibit precise 3D intermolecular interactions with their environment forms the basis of chemical design. In ligand-based drug design, bioisosteric analogues of known bioactive hits are often identified by virtually screening chemical libraries with shape, electrostatic, and pharmacophore similarity scoring functions. We instead hypothesize that a generative model which learns the joint distribution over 3D molecular structures and their interaction profiles may facilitate 3D interaction-aware chemical design. We specifically design ShEPhERD, an SE(3)-equivariant diffusion model which jointly diffuses/denoises 3D molecular graphs and representations of their shapes, electrostatic potential surfaces, and (directional) pharmacophores to/from Gaussian noise. Inspired by traditional ligand discovery, we compose 3D similarity scoring functions to assess ShEPhERD’s ability to conditionally generate novel molecules with desired interaction profiles. We demonstrate ShEPhERD’s potential for impact via exemplary drug design tasks including natural product ligand hopping, protein-blind bioactive hit diversification, and bioisosteric fragment merging.

## item_id: m_1873

TITLE: Extracting and Transferring Abilities For Building Multi-lingual Ability-enhanced Large Language Models

ABSTRACT: Multi-lingual ability transfer has become increasingly important for the broad application of large language models~(LLMs). Existing work highly relies on training with the multi-lingual ability-related data, which may be not available for low-resource languages. To solve it,  we propose a $\textbf{M}$ulti-lingual $\textbf{A}$bility $\textbf{E}$xtraction and $\textbf{T}$ransfer approach, named as $\textbf{MAET}$. Our key idea is to decompose and extract language-agnostic ability-related weights from LLMs, and transfer them across different languages by simple addition and subtraction operations without training. Specially, our MAET consists of the extraction and transfer stages. In the extraction stage, we firstly locate key neurons that are highly related to specific abilities, and then employ them to extract the transferable ability-specific weights. In the transfer stage, we further select the ability-related parameter tensors, and design the merging strategy based on the linguistic and ability specific weights, to build the multi-lingual ability-enhanced LLM. To demonstrate the effectiveness of our proposed approach, we conduct extensive experiments on mathematical and scientific tasks in both high-resource lingual and low-resource lingual scenarios. Experiment results have shown that MAET can effectively and efficiently extract and transfer the advanced abilities, and outperform training-based baselines methods. Our code and data will be publicly released.

## item_id: m_1874

TITLE: On Detecting Adversarial Perturbations

ABSTRACT: Machine learning and  deep learning in particular has advanced tremendously on perceptual tasks in recent years. However, it remains vulnerable against adversarial perturbations of the input that have been crafted specifically to fool the system while being quasi-imperceptible to a human. In this work, we propose to augment deep neural networks with a small ``detector'' subnetwork which is trained on the binary classification task of distinguishing genuine data from data containing adversarial perturbations. Our method is orthogonal to prior work on addressing adversarial perturbations, which has mostly focused on making the classification network itself more robust.  We show empirically that adversarial perturbations can be detected surprisingly well even though they are quasi-imperceptible to humans. Moreover, while the detectors have been trained to detect only a specific adversary, they generalize to similar and weaker adversaries. In addition, we propose an adversarial attack that fools both the classifier and the detector and a novel training procedure for the detector that counteracts this attack. 

## item_id: m_1875

TITLE: Iterative Refinement for Machine Translation

ABSTRACT: Existing machine translation decoding algorithms generate translations in a strictly monotonic fashion and never revisit previous decisions. As a result, earlier mistakes cannot be corrected at a later stage. In this paper, we present a translation scheme that starts from an initial guess and then makes iterative improvements that may revisit previous decisions. We parameterize our model as a convolutional neural network that predicts discrete substitutions to an existing translation based on an attention mechanism over both the source sentence as well as the current translation output. By making less than one modification per sentence, we improve the output of a phrase-based translation system by up to 0.4 BLEU on WMT15 German-English translation.

## item_id: m_1876

TITLE: GRAND++: Graph Neural Diffusion with A Source Term

ABSTRACT: We propose GRAph Neural Diffusion with a source term (GRAND++) for graph deep learning with a limited number of labeled nodes, i.e., low-labeling rate. GRAND++ is a class of continuous-depth graph deep learning architectures whose theoretical underpinning is the diffusion process on graphs with a source term. The source term guarantees two interesting theoretical properties of GRAND++: (i) the representation of graph nodes, under the dynamics of GRAND++, will not converge to a constant vector over all nodes even as the time goes to infinity, which mitigates the over-smoothing issue of graph neural networks and enables graph learning in very deep architectures. (ii) GRAND++ can provide accurate classification even when the model is trained with a very limited number of labeled training data. We experimentally verify the above two advantages on various graph deep learning benchmark tasks, showing a significant improvement over many existing graph neural networks.

## item_id: m_1877

TITLE: Demystifying Graph Neural Network Via Graph Filter Assessment

ABSTRACT: Graph Neural Networks (GNNs) have received tremendous attention recently due to their power in handling graph data for different downstream tasks across different application domains. The key of GNN is its graph convolutional filters, and recently various kinds of filters are designed. However, there still lacks in-depth analysis on (1) Whether there exists a best filter that can perform best on all graph data; (2) Which graph properties will influence the optimal choice of graph filter; (3) How to design appropriate filter adaptive to the graph data. In this paper, we focus on addressing the above three questions. We first propose a novel assessment tool to evaluate the effectiveness of graph convolutional filters for a given graph. Using the assessment tool, we find out that there is no single filter as a `silver bullet' that perform the best on all possible graphs. In addition, different graph structure properties will influence the optimal graph convolutional filter's design choice. Based on these findings, we develop Adaptive Filter Graph Neural Network (AFGNN), a simple but powerful model that can adaptively learn task-specific filter. For a given graph, it leverages graph filter assessment as regularization and learns to combine from a set of base filters. Experiments on both synthetic and real-world benchmark datasets demonstrate that our proposed model can indeed learn an appropriate filter and perform well on graph tasks.

## item_id: m_1878

TITLE: METRA: Scalable Unsupervised RL with Metric-Aware Abstraction

ABSTRACT: Unsupervised pre-training strategies have proven to be highly effective in natural language processing and computer vision. Likewise, unsupervised reinforcement learning (RL) holds the promise of discovering a variety of potentially useful behaviors that can accelerate the learning of a wide array of downstream tasks. Previous unsupervised RL approaches have mainly focused on pure exploration and mutual information skill learning. However, despite the previous attempts, making unsupervised RL truly scalable still remains a major open challenge: pure exploration approaches might struggle in complex environments with large state spaces, where covering every possible transition is infeasible, and mutual information skill learning approaches might completely fail to explore the environment due to the lack of incentives. To make unsupervised RL scalable to complex, high-dimensional environments, we propose a novel unsupervised RL objective, which we call Metric-Aware Abstraction (METRA). Our main idea is, instead of directly covering the entire state space, to only cover a compact latent space $\mathcal{Z}$ that is metrically connected to the state space $\mathcal{S}$ by temporal distances. By learning to move in every direction in the latent space, METRA obtains a tractable set of diverse behaviors that approximately cover the state space, being scalable to high-dimensional environments. Through our experiments in five locomotion and manipulation environments, we demonstrate that METRA can discover a variety of useful behaviors even in complex, pixel-based environments, being the first unsupervised RL method that discovers diverse locomotion behaviors in pixel-based Quadruped and Humanoid. Our code and videos are available at https://seohong.me/projects/metra/

## item_id: m_1879

TITLE: SEArch: A Self-Evolving Framework for Network Architecture Optimization

ABSTRACT: This paper studies a fundamental network optimization problem that finds a network architecture with optimal performance (low losses) under given resource budgets (small parameter size and/or fast inference). Different from existing network optimization approaches such as network pruning, knowledge distillation (KD), and network architecture search (NAS), in this work we introduce a novel self-evolving pipeline to perform network optimization. In this framework, a simple network iteratively and adaptively modifies its structures by using the guidance from the teacher network, until it reaches the resource budget. An attention module is introduced to transfer the knowledge from teacher network to student network. The splitting edge scheme helps the student model find an optimal macro architecture. The proposed framework combines the advantages of pruning, KD, and NAS, and hence, can efficiently generate networks with flexible structure and desirable performance. Extensive experiments on CIFAR-10, CIFAR-100 and ImageNet demonstrated that our framework achieves state-of-the-art performance in this network architecture optimization task.

## item_id: m_1880

TITLE: Conservative Uncertainty Estimation By Fitting  Prior Networks

ABSTRACT: Obtaining high-quality uncertainty estimates is essential for many applications of deep neural networks. In this paper, we theoretically justify a scheme for estimating uncertainties, based on sampling from a prior distribution. Crucially, the uncertainty estimates are shown to be conservative in the sense that they never underestimate a posterior uncertainty obtained by a hypothetical Bayesian algorithm. We also show concentration, implying that the uncertainty estimates converge to zero as we get more data. Uncertainty estimates obtained from random priors can be adapted to any deep network architecture and trained using standard supervised learning pipelines. We provide experimental evaluation of random priors on calibration and out-of-distribution detection on typical computer vision tasks, demonstrating that they outperform deep ensembles in practice.

## item_id: m_1881

TITLE: Factor Normalization for Deep Neural Network Models

ABSTRACT: Deep neural network (DNN) models often involve features of high dimensions. In most cases, the high-dimensional features can be decomposed into two parts. The first part is a low-dimensional factor. The second part is the residual feature, with much-reduced variability and inter-feature correlation. This leads to a number of interesting theoretical findings for deep neural network training. Accordingly, we are inspired to develop a new factor normalization method for better performance. The proposed method leads to a new deep learning model with two important features. First, it allows factor related feature extraction. Second, it allows adaptive learning rates for factors and residuals, respectively. This leads to fast convergence speed on both training and validation datsets. A number of empirical experiments are presented to demonstrate its superior performance. The code is available at https://github.com/HazardNeo4869/FactorNormalization

## item_id: m_1882

TITLE: Global Convergence in Neural ODEs: Impact of Activation Functions

ABSTRACT: Neural Ordinary Differential Equations (ODEs) have been successful in various applications due to their continuous nature and parameter-sharing efficiency. However, these unique characteristics also introduce challenges in training, particularly with respect to gradient computation accuracy and convergence analysis. In this paper, we address these challenges by investigating the impact of activation functions. We demonstrate that the properties of activation functions—specifically smoothness and nonlinearity—are critical to the training dynamics. Smooth activation functions guarantee globally unique solutions for both forward and backward ODEs, while sufficient nonlinearity is essential for maintaining the spectral properties of the Neural Tangent Kernel (NTK) during training. Together, these properties enable us to establish the global convergence of Neural ODEs under gradient descent in overparameterized regimes. Our theoretical findings are validated by numerical experiments, which not only support our analysis but also provide practical guidelines for scaling Neural ODEs, potentially leading to faster training and improved performance in real-world applications.

## item_id: m_1883

TITLE: Conditional set generation using Seq2seq models

ABSTRACT: Conditional set generation learns a mapping from an input sequence of tokens to a set. Several popular natural language processing (NLP) tasks, such as entity typing and dialogue emotion tagging, are instances of set generation. Sequence-to-sequence models are a popular choice to model set generation but this typical approach of treating a set as a sequence does not fully leverage its key properties, namely order-invariance and cardinality. We propose a novel data augmentation approach that recovers informative orders for labels using their dependence information. Further, we jointly model the set cardinality and output by listing the set size as the first element and taking advantage of the autoregressive factorization used by seq2seq models. Our experiments in simulated settings and on three diverse NLP datasets show that our method improves over strong seq2seq baselines by about 9% on absolute F1 score. We will release all code and data upon acceptance.

## item_id: m_1884

TITLE: EDUCE: Explaining model Decision through Unsupervised Concepts Extraction

ABSTRACT: Providing explanations along with predictions is crucial in some text processing tasks. Therefore, we propose a new self-interpretable model that performs output prediction and simultaneously provides an explanation in terms of the presence of particular concepts in the input. To do so, our model's prediction relies solely on a low-dimensional binary representation of the input, where each feature denotes the presence or absence of concepts. The presence of a concept is decided from an excerpt i.e. a small sequence of consecutive words in the text. Relevant concepts for the prediction task at hand are automatically defined by our model, avoiding the need for concept-level annotations. To ease interpretability, we enforce that for each concept, the corresponding excerpts share similar semantics and are differentiable from each others. We experimentally demonstrate the relevance of our approach on text classification and multi-sentiment analysis tasks.

## item_id: m_1885

TITLE: Trivialized Momentum Facilitates Diffusion Generative Modeling on Lie Groups

ABSTRACT: The generative modeling of data on manifolds is an important task, for which diffusion models in flat spaces typically need nontrivial adaptations. This article demonstrates how a technique called `trivialization' can transfer the effectiveness of diffusion models in Euclidean spaces to Lie groups. In particular, an auxiliary momentum variable was algorithmically introduced to help transport the position variable between data distribution and a fixed, easy-to-sample distribution. Normally, this would incur further difficulty for manifold data because momentum lives in a space that changes with the position. However, our trivialization technique creates a new momentum variable that stays in a simple fixed vector space. This design, together with a manifold preserving integrator, simplifies implementation and avoids inaccuracies created by approximations such as projections to tangent space and manifold, which were typically used in prior work, hence facilitating generation with high-fidelity and efficiency. The resulting method achieves state-of-the-art performance on protein and RNA torsion angle generation and sophisticated torus datasets. We also, arguably for the first time, tackle the generation of data on high-dimensional Special Orthogonal and Unitary groups, the latter essential for quantum problems. Code is available at https://github.com/yuchen-zhu-zyc/TDM.

## item_id: m_1886

TITLE: Traditional and Heavy Tailed Self Regularization in Neural Network Models

ABSTRACT: Random Matrix Theory (RMT) is applied to analyze the weight matrices of Deep Neural Networks (DNNs), including both production quality, pre-trained models such as AlexNet and Inception, and smaller models trained from scratch, such as LeNet5 and a miniature-AlexNet.  Empirical and theoretical results clearly indicate that the empirical spectral density (ESD) of DNN layer matrices displays signatures of traditionally-regularized statistical models, even in the absence of exogenously specifying traditional forms of regularization, such as Dropout or Weight Norm constraints.  Building on recent results in RMT, most notably its extension to Universality classes of Heavy-Tailed matrices, we develop a theory to identify 5+1 Phases of Training, corresponding to increasing amounts of Implicit Self-Regularization.  For smaller and/or older DNNs, this Implicit Self-Regularization is like traditional Tikhonov regularization, in that there is a "size scale" separating signal from noise.  For state-of-the-art DNNs, however, we identify a novel form of Heavy-Tailed Self-Regularization, similar to the self-organization seen in the statistical physics of disordered systems.  This implicit Self-Regularization can depend strongly on the many knobs of the training process.  By exploiting the generalization gap phenomena, we demonstrate that we can cause a small model to exhibit all 5+1 phases of training simply by changing the batch size.

## item_id: m_1887

TITLE: Combinatorial Attacks on Binarized Neural Networks

ABSTRACT: Binarized Neural Networks (BNNs) have recently attracted significant interest due to their computational efficiency. Concurrently, it has been shown that neural networks may be overly sensitive to ``attacks" -- tiny adversarial changes in the input -- which may be detrimental to their use in safety-critical domains. Designing attack algorithms that effectively fool trained models is a key step towards learning robust neural networks.
The discrete, non-differentiable nature of BNNs, which distinguishes them from their full-precision counterparts, poses a challenge to gradient-based attacks. In this work, we study the problem of attacking a BNN through the lens of combinatorial and integer optimization. We propose a Mixed Integer Linear Programming (MILP) formulation of the problem. While exact and flexible, the MILP quickly becomes intractable as the network and perturbation space grow. To address this issue, we propose IProp, a decomposition-based algorithm that solves a sequence of much smaller MILP problems. Experimentally, we evaluate both proposed methods against the standard gradient-based attack (PGD) on MNIST and Fashion-MNIST, and show that IProp performs favorably compared to PGD, while scaling beyond the limits of the MILP.

## item_id: m_1888

TITLE: Curvature Graph Network

ABSTRACT: Graph-structured data is prevalent in many domains. Despite the widely celebrated success of deep neural networks, their power in graph-structured data is yet to be fully explored. We propose a novel network architecture that incorporates advanced graph structural features. In particular, we leverage discrete graph curvature, which measures how the neighborhoods of a pair of nodes are structurally related. The curvature of an edge (x, y) defines the distance taken to travel from neighbors of x to neighbors of y, compared with the length of edge (x, y). It is a much more descriptive feature compared to previously used features that only focus on node specific attributes or limited topological information such as degree. Our curvature graph convolution network outperforms state-of-the-art on various synthetic and real-world graphs, especially the larger and denser ones.

## item_id: m_1889

TITLE: Z-score Normalized SAC Plus Behavioural Cloning for Offline Reinforcement Learning

ABSTRACT: Reinforcement learning (RL) defines the task that optimize a policy to maximize the cumulative reward function. Online learning collects data samples by interacting with the environment of task. Instead, Offline RL learns effective policies from a prior demonstrated dataset, which has the potential to transfer the successes between tasks. The main challenge encountered by offline RL is the inaccurate value estimates from out-of-distribution (OOD) actions, and applying vanilla off-policy algorithms to offline setting will cause severe overestimation bias for actions beyond the dataset distribution, because of the disability to correct value estimation errors via observations from the environment. To tackle this problem, the behavior regularization has been adopted in the literature to prevent the selected actions far away from the distribution of dataset so that the learned policy can be optimized within the support set of dataset. One simple method is combining RL with the behavioural cloning (BC) linearly.
By making a right balance of the relative weight between RL and BC, the pre-existing off-policy algorithms are able to work efficiently offline at the minimal cost of complexity. Overly large BC term will limit the agent’s potential to explore better policy, and oversize RL term will cause more OOD actions, both of which are undesired.
Simulated by TD3-BC, this paper aim to make a more efficient offline RL algorithm at the cost of minimal changes and light complexity. We find that the BC term can be added to the policy update of SAC algorithm to get extensively better performance with proper weight adjustment and normalization. The proposed SAC-BC algorithm is evaluated on the D4RL benchmark and proved to converge to much higher levels due to better exploration provided by tuned maximum entropy.

## item_id: m_1890

TITLE: Effective dimension of machine learning models

ABSTRACT: Making statements about the performance of trained models on tasks involving new data is one of the primary goals of machine learning, i.e., to understand the generalization power of a model. Various capacity measures try to capture this ability, but usually fall short in explaining important characteristics of models that we observe in practice. In this study, we propose the local effective dimension as a capacity measure which seems to correlate well with generalization error on standard data sets. Importantly, we prove that the local effective dimension bounds the generalization error and discuss the aptness of this capacity measure for machine learning models.

## item_id: m_1891

TITLE: Video Decomposition Prior: Editing Videos Layer by Layer

ABSTRACT: In the evolving landscape of video editing methodologies, a majority of  deep learning techniques are often reliant on extensive datasets of observed input and ground truth sequence pairs for optimal performance. Such reliance often falters when acquiring data becomes challenging, especially in tasks like video dehazing and relighting, where replicating identical motions and camera angles in both corrupted and ground truth sequences is complicated. Moreover, these conventional methodologies perform best when the test distribution closely mirrors the training distribution. Recognizing these challenges, this paper introduces a novel video decomposition prior `VDP' framework which derives inspiration from professional video editing practices. Our methodology does not mandate task-specific external data corpus collection, instead pivots to utilizing the motion and appearance of the input video. VDP framework decomposes a video sequence into a set of multiple RGB layers and associated opacity levels. These set of layers are then manipulated individually to obtain the desired results. We addresses tasks such as video object segmentation, dehazing, and relighting. Moreover, we introduce a novel logarithmic video decomposition formulation for video relighting tasks, setting a new benchmark over the existing methodologies. We evaluate our approach on standard video datasets like DAVIS, REVIDE, & SDSD and show qualitative results on a diverse array of internet videos.

## item_id: m_1892

TITLE: IID-GAN: an IID Sampling Perspective for Regularizing Mode Collapse

ABSTRACT: Despite its success, generative adversarial networks (GANs) still suffer from mode collapse, namely the generator can only map latent variables to a partial set of modes of the target distribution. In this paper, we analyze and try to regularize this issue with an independent and identically distributed (IID) sampling perspective and emphasize that holding the IID property for generation for target distribution (i.e. real distribution) can naturally avoid mode collapse. This is based on the basic IID assumption for real data in machine learning. However, though the source samples $\mathbf{z}$ obey IID, the generation $G(\mathbf{z})$ may not necessarily be IID from the target distribution.  Based on this observation, we propose a necessary condition of IID generation and provide a new loss to encourage the closeness between the inverse source of real data and the Gaussian source in the latent space to regularize the generation to be IID from the target distribution. The logic is that the inverse samples from target data should also be IID in the source distribution. Experiments on both synthetic and real-world data show the effectiveness of our model.

## item_id: m_1893

TITLE: Curiosity-driven Exploration by Bootstrapping Features

ABSTRACT: We introduce CBF, an exploration method that works in the absence of rewards or end of episode signal. CBF is based on intrinsic reward derived from the error of a dynamics model operating in feature space. It was inspired by (Pathak et al., 2017), is easy to implement, and can achieve results such as passing four levels of Super Mario Bros, navigating VizDoom mazes and passing two levels of SpaceInvaders. We investigated the effect of combining the method with several auxiliary tasks, but find inconsistent improvements over the CBF baseline.


## item_id: m_1894

TITLE: Ontology-Driven Semantic Alignment of Artificial Neurons and Visual Concepts

ABSTRACT: Semantic alignment methods attempt to establish a link between human-level concepts and the units of an artificial neural network. Current approaches evaluate the emergence of such meaningful neurons by analyzing the effect of semantically annotated inputs on their activations. In doing so, they often understate two aspects that characterize neural representations and semantic concepts, namely the distributed nature of the former and the existence of semantic relationships binding the latter. In this work, we explicitly tackle this interrelatedness, both at a neural and a conceptual level, by providing a novel semantic alignment framework that builds on aligning a structured ontology with the distributed neural representations. The ontology introduces semantic relations between concepts, enabling the clustering of topologically related units into semantically rich and meaningful neural circuits. Our empirical analysis on notable convolutional models for image classification discusses the emergence of such neural circuits. It also validates their meaningfulness by studying how the selected units are pivotal for the accuracy of classes that are semantically related to the aligned concepts. We also contribute by releasing the code implementing our alignment framework.

## item_id: m_1895

TITLE: Neural Networks for irregularly observed continuous-time Stochastic Processes

ABSTRACT: Designing neural networks for continuous-time stochastic processes is challenging, especially when observations are made irregularly. In this article, we analyze neural networks from a frame theoretic perspective to identify the sufficient conditions that enable smoothly recoverable representations of signals in L^2(R). Moreover, we show that, under certain assumptions, these properties hold even when signals are irregularly observed. As we converge to the family of (convolutional) neural networks that satisfy these conditions, we show that we can optimize our convolution filters while constraining them so that they effectively compute a Discrete Wavelet Transform. Such a neural network can efficiently divide the time-axis of a signal into orthogonal sub-spaces of different temporal scale and localization. We evaluate the resulting neural network on an assortment of synthetic and real-world tasks: parsimonious auto-encoding, video classification, and financial forecasting.

## item_id: m_1896

TITLE: A Universal Music Translation Network

ABSTRACT: We present a method for translating music across musical instruments and styles. This method is based on unsupervised training of a multi-domain wavenet autoencoder, with a shared encoder and a domain-independent latent space that is trained end-to-end on waveforms. Employing a diverse training dataset and large net capacity, the single encoder allows us to translate also from musical domains that were not seen during training. We evaluate our method on a dataset collected from professional musicians, and achieve convincing translations. We also study the properties of the obtained translation and demonstrate translating even from a whistle, potentially enabling the creation of instrumental music by untrained humans. 

## item_id: m_1897

TITLE: Language Style Transfer from Non-Parallel Text with Arbitrary Styles

ABSTRACT: Language style transfer is the problem of migrating the content of a source sentence to a target style. In many applications, parallel training data are not available and source sentences to be transferred may have arbitrary and unknown styles. In this paper, we present an encoder-decoder framework under this problem setting. Each sentence is encoded into its content and style latent representations. By recombining the content with the target style, we can decode a sentence aligned in the target domain. To adequately constrain the encoding and decoding functions, we couple them with two loss functions. The first is a style discrepancy loss, enforcing that the style representation accurately encodes the style information guided by the discrepancy between the sentence style and the target style. The second is a cycle consistency loss, which ensures that the transferred sentence should preserve the content of the original sentence disentangled from its style. We validate the effectiveness of our proposed model on two tasks: sentiment modification of restaurant reviews, and dialog response revision with a romantic style.

## item_id: m_1898

TITLE: Drop-Bottleneck: Learning Discrete Compressed Representation for Noise-Robust Exploration

ABSTRACT: We propose a novel information bottleneck (IB) method named Drop-Bottleneck, which discretely drops features that are irrelevant to the target variable. Drop-Bottleneck not only enjoys a simple and tractable compression objective but also additionally provides a deterministic compressed representation of the input variable, which is useful for inference tasks that require consistent representation. Moreover, it can jointly learn a feature extractor and select features considering each feature dimension's relevance to the target task, which is unattainable by most neural network-based IB methods. We propose an exploration method based on Drop-Bottleneck for reinforcement learning tasks. In a multitude of noisy and reward sparse maze navigation tasks in VizDoom (Kempka et al., 2016) and DMLab (Beattie et al., 2016), our exploration method achieves state-of-the-art performance. As a new IB framework, we demonstrate that Drop-Bottleneck outperforms Variational Information Bottleneck (VIB) (Alemi et al., 2017) in multiple aspects including adversarial robustness and dimensionality reduction.

## item_id: m_1899

TITLE: Fast Task Adaptation for Few-Shot Learning

ABSTRACT: Few-shot classification is a challenging task due to the scarcity of training examples for each class. The key lies in generalization of prior knowledge learned from large-scale base classes and fast adaptation of the classifier to novel classes. In this paper, we introduce a two-stage framework. In the first stage, we attempt to learn task-agnostic feature on base data with a novel Metric-Softmax loss. The Metric-Softmax loss is trained against the whole label set and learns more discriminative feature than episodic training. Besides, the Metric-Softmax classifier can be applied to base and novel classes in a consistent manner, which is critical for the generalizability of the learned feature. In the second stage, we design a task-adaptive transformation which adapts the classifier to each few-shot setting very fast within a few tuning epochs. Compared with existing fine-tuning scheme, the scarce examples of novel classes are exploited more effectively. Experiments show that our approach outperforms current state-of-the-arts by a large margin on the commonly used mini-ImageNet and CUB-200-2011 benchmarks.

## item_id: m_1900

TITLE: CBOW Is Not All You Need: Combining CBOW with the Compositional Matrix Space Model

ABSTRACT: Continuous Bag of Words (CBOW) is a powerful text embedding method. Due to its strong capabilities to encode word content, CBOW embeddings perform well on a wide range of downstream tasks while being efficient to compute. However, CBOW is not capable of capturing the word order. The reason is that the computation of CBOW's word embeddings is commutative, i.e., embeddings of XYZ and ZYX are the same. In order to address this shortcoming, we propose a
learning algorithm for the Continuous Matrix Space Model, which we call Continual Multiplication of Words (CMOW). Our algorithm is an adaptation of word2vec, so that it can be trained on large quantities of unlabeled text. We empirically show that CMOW better captures linguistic properties, but it is inferior to CBOW in memorizing word content. Motivated by these findings, we propose a hybrid model that combines the strengths of CBOW and CMOW. Our results show that the hybrid CBOW-CMOW-model retains CBOW's strong ability to memorize word content while at the same time substantially improving its ability to encode other linguistic information by 8%. As a result, the hybrid also performs better on 8 out of 11 supervised downstream tasks with an average improvement of 1.2%.
