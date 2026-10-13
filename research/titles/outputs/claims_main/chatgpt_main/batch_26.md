# Batch 26 — 100 items

## item_id: m_2501

TITLE: Representation Power of Graph Convolutions : Neural Tangent Kernel Analysis

ABSTRACT: The fundamental principle of Graph Neural Networks (GNNs) is to exploit the structural information of the data by aggregating the neighboring nodes using a `graph convolution’. Therefore, understanding its influence on the network performance is crucial. Convolutions based on graph Laplacian have emerged as the dominant choice with the symmetric normalization of the adjacency matrix $A$, defined as $D^{-1/2}AD^{−1/2}$, being the most widely adopted one, where $D$ is the degree matrix. However, some empirical studies show that row normalization $D^{−1}A$ outperforms it in node classification. Despite the widespread use of GNNs, there is no rigorous theoretical study on the representation power of these convolution operators, that could explain this behavior. In this work, we analyze the influence of the graph convolutions theoretically using Graph Neural Tangent Kernel in a semi-supervised node classification setting. Under a Degree Corrected Stochastic Block Model, we prove that: (i) row normalization preserves the underlying class structure better than other graph convolutions; (ii) performance degrades with network depth due to over-smoothing, but the loss in class information is the slowest in row normalization; (iii) skip connections retain the class information even at infinite depth, thereby eliminating over-smoothing. We finally validate our theoretical findings on real datasets.

## item_id: m_2502

TITLE: Mediater: Memory-efficient LLM Merging with Less Parameter Conflicts and Uncertainty Based Routing

ABSTRACT: Model merging aggregates Large Language Models (LLMs) finetuned on different tasks into a stronger one. However, parameter conflicts between models leads to performance degradation in averaging. While model routing addresses this issue by selecting individual models during inference, it imposes excessive storage and compute costs, and fails to leverage the common knowledge from different models. 
In this work, we observe that different layers exhibit varying levels of parameter conflicts. Building on this insight, we  average layers with minimal parameter conflicts and use a novel task-level expert routing for layers with significant conflicts.
To further reduce storage costs, inspired by task arithmetic sparsity, we decouple multiple fine-tuned experts into a dense expert and several sparse experts. Then, we select and merge appropriate experts based on the task uncertainty of the input data. 
We conduct extensive experiments on both LLaMA and Qwen with varying parameter scales, and evaluate on real-world reasoning tasks. Results demonstrate that our method consistently achieves significant performance improvements while requiring less system cost.

## item_id: m_2503

TITLE: Adversarial Robustness Against the Union of Multiple Perturbation Models

ABSTRACT: Owing to the susceptibility of deep learning systems to adversarial attacks, there has been a great deal of work in developing (both empirically and certifiably) robust classifiers, but the vast majority has defended against single types of attacks. Recent work has looked at defending against multiple attacks, specifically on the MNIST dataset, yet this approach used a relatively complex architecture, claiming that standard adversarial training can not apply because it "overfits" to a particular norm. In this work, we show that it is indeed possible to adversarially train a robust model against a union of norm-bounded attacks, by using a natural generalization of the standard PGD-based procedure for adversarial training to multiple threat models. With this approach, we are able to train standard architectures which are robust against l_inf, l_2, and l_1 attacks, outperforming past approaches on the MNIST dataset and providing the first CIFAR10 network trained to be simultaneously robust against (l_inf, l_2, l_1) threat models, which achieves adversarial accuracy rates of (47.6%, 64.3%, 53.4%) for (l_inf, l_2, l_1) perturbations with epsilon radius = (0.03,0.5,12).

## item_id: m_2504

TITLE: SeqSHAP: Subsequence Level Shapley Value Explanations for Sequential Predictions

ABSTRACT: With the increasing demands of interpretability in real-world applications, various methods for explainable artificial intelligence (XAI) have been proposed. However, most of them overlook the interpretability in sequential scenarios, which have a wide range of applications, e.g., online transactions and sequential recommendations. In this paper, we propose a Shapley value based explainer named SeqSHAP to explain the model predictions in sequential scenarios. Compared to existing methods, SeqSHAP provides more intuitive explanations at a subsequence level, which explicitly models the effect of contextual information among the related elements in a sequence. We propose to calculate subsequence-level feature attributions instead of element-wise attributions to utilize the information embedded in sequence structure, and provide a distribution-based segmentation method to obtain reasonable subsequences. Extensive experiments on two online transaction datasets from a real-world e-commerce platform show that the proposed method could provide valid and reliable explanations for sequential predictions.

## item_id: m_2505

TITLE: Metacontrol for Adaptive Imagination-Based Optimization

ABSTRACT: Many machine learning systems are built to solve the hardest examples of a particular task, which often makes them large and expensive to run---especially with respect to the easier examples, which might require much less computation. For an agent with a limited computational budget, this "one-size-fits-all" approach may result in the agent wasting valuable computation on easy examples, while not spending enough on hard examples. Rather than learning a single, fixed policy for solving all instances of a task, we introduce a metacontroller which learns to optimize a sequence of "imagined" internal simulations over predictive models of the world in order to construct a more informed, and more economical, solution. The metacontroller component is a model-free reinforcement learning agent, which decides both how many iterations of the optimization procedure to run, as well as which model to consult on each iteration. The models (which we call "experts") can be state transition models, action-value functions, or any other mechanism that provides information useful for solving the task, and can be learned on-policy or off-policy in parallel with the metacontroller. When the metacontroller, controller, and experts were trained with "interaction networks" (Battaglia et al., 2016) as expert models, our approach was able to solve a challenging decision-making problem under complex non-linear dynamics. The metacontroller learned to adapt the amount of computation it performed to the difficulty of the task, and learned how to choose which experts to consult by factoring in both their reliability and individual computational resource costs. This allowed the metacontroller to achieve a lower overall cost (task loss plus computational cost) than more traditional fixed policy approaches. These results demonstrate that our approach is a powerful framework for using rich forward models for efficient model-based reinforcement learning.

## item_id: m_2506

TITLE: A Coach-Player Framework for Dynamic Team Composition

ABSTRACT: In real-world multi-agent teams, agents with different capabilities may join or leave "on the fly" without altering the team's overarching goals. Coordinating teams with such dynamic composition remains a challenging problem: the optimal team strategy may vary with its composition. Inspired by real-world team sports, we propose a coach-player framework to tackle this problem. We assume that the players only have a partial view of the environment, while the coach has a complete view. The coach coordinates the players by distributing individual strategies. Specifically, we 1) propose an attention mechanism for both the players and the coach; 2) incorporate a variational objective to regularize  learning; and 3) design an adaptive communication method to let the coach decide when to communicate with different players. Our attention mechanism on the players and the coach allows for a varying number of heterogeneous agents, and can thus tackle the dynamic team composition.  We validate our methods on resource collection tasks in multi-agent particle environment. We demonstrate zero-shot generalization to new team compositions with varying numbers of heterogeneous  agents. The performance of our method is comparable or even better than the  setting where all players have a full view of the environment, but no coach. Moreover, we see that the performance stays nearly the same even when the coach communicates as little as 13% of the time using our adaptive communication strategy.  These results demonstrate   the significance of a coach to coordinate players in dynamic teams.

## item_id: m_2507

TITLE: Multi-objective antibody design with constrained preference optimization

ABSTRACT: Antibody design is crucial for developing therapies against diseases such as cancer and viral infections. Recent deep generative models have significantly advanced computational antibody design, particularly in enhancing binding affinity to target antigens. However, beyond binding affinity, antibodies should exhibit other favorable biophysical properties such as non-antigen binding specificity and low self-association, which are important for antibody developability and clinical safety. To address this challenge, we propose AbNovo, a framework that leverages constrained preference optimization for multi-objective antibody design. First, we pre-train an antigen-conditioned generative model for antibody structure and sequence co-design. Then, we fine-tune the model using binding affinity as a reward while enforcing explicit constraints on other biophysical properties. Specifically, we model the physical binding energy with continuous rewards rather than pairwise preferences and explore a primal-and-dual approach for constrained optimization. Additionally, we incorporate a structure-aware protein language model to mitigate the issue of limited training data. Evaluated on independent test sets, AbNovo outperforms existing methods in metrics of binding affinity such as Rosetta binding energy and evolutionary plausibility, as well as in metrics for other biophysical properties like stability and specificity.

## item_id: m_2508

TITLE: Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative

ABSTRACT: Diffusion policies for visuomotor robot manipulation tasks achieve remarkable dexterity and robustness while only training on a small number of task demonstrations.  However, the reason for this performance remains a mystery. In this paper, we offer a surprising hypothesis: diffusion policies essentially memorize an action lookup table---\emph{and this is beneficial}. We posit that, at runtime, diffusion policies find the closest training image to the test image in a latent space, and recall the associated training action  (i.e. action chunk), offering reactivity without the need for action generalization. This is effective in the sparse data regime, where there is not enough data density for the model to learn action generalization. We support this claim with systematic empirical evidence, showing that even when conditioned on highly out of distribution (OOD) images, Diffusion Policy still outputs an action chunk from the training data. We evaluate and compare three representative policy families on the same data set: Diffusion Policy, Action Chunking with Transformers (ACT), and GR00T, a pre-trained generalist Vision-Language-Action (VLA) model.  We show that Diffusion Policy gives strong action memorization giving surprising robustness in OOD regimes, ACT shows action interpolation with poor robustness in OOD regimes, and GR00T (benefiting from substantial pre-training) shows both action interpolation and OOD robustness. As a simple alternative to Diffusion Policy, we introduce the Action Lookup Table (ALT) policy, showing that an explicit lookup table policy can perform comparably in this low data regime. Despite its simplicity, ALT attains Diffusion Policy–level performance while also providing faster inference and explicit OOD detection via latent-distance thresholds. These results reframe diffusion policies for robot manipulation as reactive memory retrieval under data sparsity, and provide practical tools for interpreting, evaluating, and monitoring such policies. More information can be found at: \url{https://stanfordmsl.github.io/alt/}.

## item_id: m_2509

TITLE: Efficient Sharpness-aware Minimization for Improved Training of Neural Networks

ABSTRACT: Overparametrized Deep Neural Networks (DNNs) often achieve astounding performances, but may potentially result in severe generalization error. Recently, the relation between the sharpness of the loss landscape and the generalization error has been established by Foret et al. (2020), in which the Sharpness Aware Minimizer (SAM) was proposed to mitigate the degradation of the generalization. Unfortunately, SAM’s computational cost is roughly double that of base optimizers, such as Stochastic Gradient Descent (SGD). This paper thus proposes Efficient Sharpness Aware Minimizer (ESAM), which boosts SAM’s efficiency at no cost to its generalization performance. ESAM includes two novel and efficient training strategies—StochasticWeight Perturbation and Sharpness-Sensitive Data Selection. In the former, the sharpness measure is approximated by perturbing a stochastically chosen set of weights in each iteration; in the latter, the SAM loss is optimized using only a judiciously selected subset of data that is sensitive to the sharpness. We provide theoretical explanations as to why these strategies perform well. We also show, via extensive experiments on the CIFAR and ImageNet
datasets, that ESAM enhances the efficiency over SAM from requiring 100% extra computations to 40% vis-`a-vis base optimizers, while test accuracies are preserved or even improved.

## item_id: m_2510

TITLE: Secure Network Release with Link Privacy

ABSTRACT: Many data mining and analytical tasks rely on the abstraction of networks (graphs) to summarize relational structures among individuals (nodes). Since relational data are often sensitive, we aim to seek effective approaches to release utility-preserved yet privacy-protected structured data. In this paper, we leverage the differential privacy (DP) framework, to formulate and enforce rigorous privacy constraints on deep graph generation models, with a focus on edge-DP to guarantee individual link privacy. In particular, we enforce edge-DP by injecting Gaussian noise to the gradients of a link reconstruction based graph generation model, and ensure data utility by improving structure learning with structure-oriented graph comparison. Extensive experiments on two real-world network datasets show that our proposed DPGGAN model is able to generate networks with effectively preserved global structure and rigorously protected individual link privacy.

## item_id: m_2511

TITLE: Latent State Marginalization as a Low-cost Approach for Improving Exploration

ABSTRACT: While the maximum entropy (MaxEnt) reinforcement learning (RL) framework -- often touted for its exploration and robustness capabilities -- is usually motivated from a probabilistic perspective, the use of deep probabilistic models have not gained much traction in practice due to their inherent complexity. In this work, we propose the adoption of latent variable policies within the MaxEnt framework, which we can provably approximate any policy distribution, and additionally, naturally emerges under the use of world models with a latent belief state. 
We discuss why latent variable policies are difficult to train, how naive approaches can fail, and subsequently introduce a series of improvements centered around low-cost marginalization of the latent state, allowing us to make full use of the latent state at minimal additional cost. We instantiate our method under the actor-critic framework, marginalizing both the actor and critic. The resulting algorithm, referred to as Stochastic Marginal Actor-Critic (SMAC), is simple yet effective. We experimentally validate our method on continuous control tasks, showing that effective marginalization can lead to better exploration and more robust training. Our implementation is open sourced at https://github.com/zdhNarsil/Stochastic-Marginal-Actor-Critic.

## item_id: m_2512

TITLE: Bidirectional Attention Flow for Machine Comprehension

ABSTRACT: Machine comprehension (MC), answering a query about a given context paragraph, requires modeling complex interactions between the context and the query. Recently, attention mechanisms have been successfully extended to MC. Typically these methods use attention to focus on a small portion of the context and summarize it with a fixed-size vector, couple attentions temporally, and/or often form a uni-directional attention. In this paper we introduce the Bi-Directional Attention Flow (BIDAF) network, a multi-stage hierarchical process that represents the context at different levels of granularity and uses bi-directional attention flow mechanism to obtain a query-aware context representation without early summarization. Our experimental evaluations show that our model achieves the state-of-the-art results in Stanford Question Answering Dataset (SQuAD) and CNN/DailyMail cloze test.

## item_id: m_2513

TITLE: A Hierarchical Language Model Design For Interpretable Graph Reasoning

ABSTRACT: Large language models (LLMs) have seen an increased adoption for tasks with implicit graphical structures, such as planning in robotics, multi-hop question answering, and knowledge probing. However, despite their remarkable success in text-based tasks, LLMs' capabilities in understanding explicit graph structures remain limited, preventing them from fully replacing Graph Neural Networks (GNNs) in graph-centric applications. In this work, we introduce a Hierarchical Language Model (HLM-G) Design that employs a two-block architecture to effectively capture local and global graph information, significantly enhancing graph structure understanding. Our model achieves a new state-of-the-art in graph understanding, outperforming both GNN and LLM baselines. It demonstrates robustness to variations in graph-descriptive prompts, overcoming a key limitation of existing LLMs. Furthermore, we demonstrate the interpretability of our model using intrinsic attention weights and established explainers. Comprehensive evaluations across diverse real-world datasets, covering node, link, and graph-level tasks, highlight our model's superior generalization capabilities, marking a significant advancement in the application of LLMs to graph-centric tasks.

## item_id: m_2514

TITLE: One-shot and few-shot learning of word embeddings

ABSTRACT: Standard deep learning systems require thousands or millions of examples to learn a concept, and cannot integrate new concepts easily. By contrast, humans have an incredible ability to do one-shot or few-shot learning. For instance, from just hearing a word used in a sentence, humans can infer a great deal about it, by leveraging what the syntax and semantics of the surrounding words tells us. Here, we draw inspiration from this to highlight a simple technique by which deep recurrent networks can similarly exploit their prior knowledge to learn a useful representation for a new word from little data. This could make natural language processing systems much more flexible, by allowing them to learn continually from the new words they encounter.

## item_id: m_2515

TITLE: BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese

ABSTRACT: As large language models (LLMs) evolve into web-interacting agents, their ability to retrieve and reason over real-time information has become a crucial benchmark for general intelligence. However, existing benchmarks such as BrowseComp focus solely on English, neglecting the linguistic, infrastructural, and retrieval-specific challenges posed by other information ecosystems—particularly the Chinese web. We present BrowseComp-ZH, a high-difficulty, natively-constructed benchmark designed to assess LLM agents’ web browsing abilities in Chinese. Rather than translating from English, all questions in BrowseComp-ZH are written from scratch by native speakers to reflect authentic information-seeking behaviors and cultural contexts. The dataset comprises 289 multi-hop questions across 11 diverse domains, each reverse-engineered from a short, verifiable answer and filtered through a twostage quality control pipeline to ensure retrieval hardness and answer uniqueness. We evaluate over 20 leading LLMs and agentic search systems. Despite strong language and retrieval abilities, most models perform poorly: many score below 10% accuracy, and only a few exceed 20%. Even the best system achieves just 42.9% accuracy. These results highlight the considerable difficulty of BrowseComp-ZH, where success requires not only robust retrieval strategies but also advanced multihop reasoning and information reconciliation—abilities that remain challenging for current models. BrowseComp-ZH thus serves as a stress test for web-interactive LLMs beyond English, offering a rigorous and linguistically diverse evaluation framework to guide future research on multilingual agent capabilities.

## item_id: m_2516

TITLE: MaskGAN: Better Text Generation via Filling in the _______

ABSTRACT: Neural text generation models are often autoregressive language models or seq2seq models. Neural autoregressive and seq2seq models that generate text by sampling words sequentially, with each word conditioned on the previous model, are state-of-the-art for several machine translation and summarization benchmarks. These benchmarks are often defined by validation perplexity even though this is not a direct measure of sample quality. Language models are typically trained via maximum likelihood and most often with teacher forcing. Teacher forcing is well-suited to optimizing perplexity but can result in poor sample quality because generating text requires conditioning on sequences of words that were never observed at training time. We propose to improve sample quality using Generative Adversarial Network (GANs), which explicitly train the generator to produce high quality samples and have shown a lot of success in image generation. GANs were originally to designed to output differentiable values, so discrete language generation is challenging for them. We introduce an actor-critic conditional GAN that fills in missing text conditioned on the surrounding context. We show qualitatively and quantitatively, evidence that this produces more realistic text samples compared to a maximum likelihood trained model.

## item_id: m_2517

TITLE: Understanding Graph Self-Supervised Pre-training under Distribution Shifts: A Scaling Law Perspective

ABSTRACT: Scaling laws have played a fundamental role in the development of foundation models for NLP and vision, but their applicability to large-scale pretrained graph-based models remains unclear—particularly under distribution shifts intrinsic to graph data. In this work, we systematically investigate how model capacity and data scale affect downstream performance in graph pre-training under distribution shifts. To disentangle how distribution shifts impact the scaling, we construct synthetic benchmarks based on contextual stochastic block models, with precise control over both structural and feature-level shifts across the pre-training and testing graphs. Our initial experiments on GCN, a standard Graph Neural Network (GNN) baseline, reveal a striking asymmetry: increasing model capacity consistently improves performance, while increasing data size often degrades it, even under mild shift. We show that this degradation is not inevitable; properly configuring the pretraining model with deeper, wider, and transformer-based architectures enables favorable data scaling, even when distribution shifts. As data scales, graph transformer models achieve up to +9\% gains over GCN, which holds for both synthetic and real-world graph domain adaptation tasks. To explain this phenomenon, we develop a theoretical framework based on Fisher separability and Wasserstein domain divergence, which formally characterizes how distribution shifts affect representation transferability. Our results highlight architecture- and shift-aware strategies as the key to unlock scalable graph-based model pre-training.

## item_id: m_2518

TITLE: Multi-Objective Molecular Design through Learning Latent Pareto Set

ABSTRACT: Molecular design inherently involves the optimization of multiple conflicting objectives, such as enhancing bio-activity and ensuring synthesizability. Evaluating these objectives often requires resource-intensive computations or physical experiments. Current molecular design methodologies typically approximate the Pareto set using a limited number of molecules. In this paper, we present an innovative approach, called Multi-Objective Molecular Design through Learning Latent Pareto Set (MLPS). MLPS initially utilizes an encoder-decoder model to seamlessly transform the discrete chemical space into a continuous latent space. We then employ local Bayesian optimization models to efficiently search for local optimal solutions (i.e., molecules) within predefined trust regions. Using surrogate objective values derived from these local models, we train a global Pareto set learning model to understand the mapping between direction vectors (called ``preferences'') in the objective space and the entire Pareto set in the continuous latent space. Both the global Pareto set learning model and local Bayesian optimization models collaborate to discover high-quality solutions and adapt the trust regions dynamically. Our work is the first endeavor towards learning the Pareto set for multi-objective molecular design, providing decision-makers with the capability to fine-tune their preferences and thoroughly explore the Pareto set. Experimental results demonstrate that MLPS achieves state-of-the-art performance across various multi-objective scenarios, encompassing diverse objective types and varying numbers of objectives.

## item_id: m_2519

TITLE: Generalizing Deep Multi-task Learning with Heterogeneous Structured Networks

ABSTRACT: Many real applications show a great deal of interest in learning multiple tasks from different data sources/modalities with unbalanced samples and dimensions. Unfortunately, existing cutting-edge deep multi-task learning (MTL) approaches cannot be directly applied to these settings, due to either heterogeneous input dimensions or the heterogeneity in the optimal network architectures of different tasks. It is thus demanding to develop knowledge-sharing mechanism to handle the intrinsic discrepancies among network architectures across tasks. To this end, we propose a flexible knowledge-sharing framework for jointly learning multiple tasks from distinct data sources/modalities. The proposed framework allows each task to own its task (data)-specific network design, via utilizing a compact tensor representation, while the sharing is achieved through the partially shared latent cores. By providing more elaborate sharing control with latent cores, our framework is effective in transferring task-invariant knowledge, yet also being efficient in learning task-specific features. Experiments on both single and multiple data sources/modalities settings display the promising results of the proposed method, especially favourable in insufficient data scenarios.

## item_id: m_2520

TITLE: PromptSFL: Improving Visual Prompt Tuning For Split Federated Learning

ABSTRACT: Conflict arises due to the disparity between the substantial resource demands of pre-trained models and the limited available resources of federated learning (FL) participants. Split learning presents a viable approach for adapting pre-trained models to FL, involving the allocation of a small portion of the pre-trained model to clients while deploying the remaining part on a server. Moreover, the application of Visual Prompt Tuning (VPT) to pre-trained models has shown state-of-the-art performances in parameter-efficient fine-tuning methods. However, VPT exhibits unsatisfactory performance in split federated learning (SFL) compared to its performance in centralized learning. In this paper, we first identify that VPT falls short of expectations in SFL due to the insufficient generalization capability of clients. To address this issue, we propose PromptSFL, which aligns the feature spaces of prompts between clients and the server to adapt VPT for SFL. PromptSFL transmits the final prompts in clients, termed skip prompts, to the first prompts in the server, enabling clients to extract more common features from the server. Additionally, we introduce a linear layer to map the prompts from clients to the feature space in the server during this skipping process, preventing the prompts of clients from overfitting to local datasets. Moreover, to enhance the convergence speed of SFL, PromptSFL employs an adaptive learning rate for clients. Extensive experiments demonstrate the effectiveness and efficiency of PromptSFL.

## item_id: m_2521

TITLE: Baseline-corrected space-by-time non-negative matrix factorization for decoding single trial population spike trains

ABSTRACT: Activity of populations of sensory neurons carries stimulus information in both the temporal and the spatial dimensions. This poses the question of how to compactly represent all the information that the population codes carry across all these dimensions. Here, we developed an analytical method to factorize a large number of retinal ganglion cells' spike trains into a robust low-dimensional representation that captures efficiently both their spatial and temporal information. In particular, we extended previously used single-trial space-by-time tensor decomposition based on non-negative matrix factorization to efficiently discount pre-stimulus baseline activity. On data recorded from retinal ganglion cells with strong pre-stimulus baseline, we showed that in situations were the stimulus elicits a strong change in firing rate, our extensions yield a boost in stimulus decoding performance. Our results thus suggest that taking into account the baseline can be important for finding a compact information-rich representation of neural activity.

## item_id: m_2522

TITLE: Opportunistic Actor-Critic (OPAC) with Clipped Triple Q-learning

ABSTRACT: Despite being the most successful model-free deep reinforcement learning (RL) algorithms in recent years, Soft Actor-Critic (SAC) and Twin Delayed Deep Deterministic Policy Gradient (TD3) have their respective downsides--TD3 performs well in simple tasks, while SAC does so in relatively complicated ones. However, they also suffer from underestimation due to Clipped Double Q-learning, i.e., taking a minimum of two Q-values. This paper introduces Opportunistic Actor-Critic (OPAC), an ensemble model-free deep RL algorithm that performs well in simple and complex tasks. OPAC combines the features of TD3 and SAC under one roof to retain their respective benefits. It also employs three critics and considers taking the mean of the smallest two Q-values for updating the shared target, dubbed Clipped Triple Q-learning. Our analytical results establish that Clipped Triple Q-learning incurs less underestimation than Clipped Double Q-learning. Furthermore, we have systematically evaluated OPAC in MuJoCo environments, and the empirical results indicate that OPAC attains higher average rewards than the current baselines.

## item_id: m_2523

TITLE: Self-supervised Visual Reinforcement Learning with Object-centric Representations

ABSTRACT: Autonomous agents need large repertoires of skills to act reasonably on new tasks that they have not seen before. However, acquiring these skills using only a stream of high-dimensional, unstructured, and unlabeled observations is a tricky challenge for any autonomous agent. Previous methods have used variational autoencoders to encode a scene into a low-dimensional vector that can be used as a goal for an agent to discover new skills. Nevertheless, in compositional/multi-object environments it is difficult to disentangle all the factors of variation into such a fixed-length representation of the whole scene. We propose to use object-centric representations as a modular and structured observation space, which is learned with a compositional generative world model.
We show that the structure in the representations in combination with goal-conditioned attention policies helps the autonomous agent to discover and learn useful skills. These skills can be further combined to address compositional tasks like the manipulation of several different objects.

## item_id: m_2524

TITLE: FeatUp: A Model-Agnostic Framework for Features at Any Resolution

ABSTRACT: Deep features are a cornerstone of computer vision research, capturing image semantics and enabling the community to solve downstream tasks even in the zero- or few-shot regime. However, these features often lack the spatial resolution to directly perform dense prediction tasks like segmentation and depth prediction because models aggressively pool information over large areas. In this work, we introduce FeatUp, a task- and model-agnostic framework to restore lost spatial information in deep features. We introduce two variants of FeatUp: one that guides features with high-resolution signal in a single forward pass, and one that fits an implicit model to a single image to reconstruct features at any resolution. Both approaches use a multi-view consistency loss with deep analogies to NeRFs. Our features retain their original semantics and can be swapped into existing applications to yield resolution and performance gains even without re-training. We show that FeatUp significantly outperforms other feature upsampling and image super-resolution approaches in class activation map generation, transfer learning for segmentation and depth prediction, and end-to-end training for semantic segmentation.

## item_id: m_2525

TITLE: Scalable Influence and Fact Tracing for Large Language Model Pretraining

ABSTRACT: Training data attribution (TDA) methods aim to attribute model outputs back to specific training examples, and the application of these methods to large language model (LLM) outputs could significantly advance model transparency and data curation. However, it has been challenging to date to apply these methods to the full scale of LLM pretraining. In this paper, we refine existing gradient-based methods to work effectively at scale, allowing us to retrieve influential examples for an 8B-parameter language model from a pretraining corpus of over 160B tokens with no need for subsampling or pre-filtering. Our method combines several techniques, including optimizer state correction, a task-specific Hessian approximation, and normalized encodings, which we find to be critical for performance at scale. In quantitative evaluations on a fact tracing task, our method performs best at identifying examples that influence model predictions, but classical, model-agnostic retrieval methods such as BM25 still perform better at finding passages which explicitly contain relevant facts. These results demonstrate a misalignment between factual *attribution* and causal *influence*. With increasing model size and training tokens, we find that influence more closely aligns with factual attribution. Finally, we examine different types of examples identified as influential by our method, finding that while many directly entail a particular fact, others support the same output by reinforcing priors on relation types, common entities, and names. We release our prompt set and model outputs, along with a web-based visualization tool to explore influential examples for factual predictions, commonsense reasoning, arithmetic, and open-ended generation for an 8B-parameter LLM.

## item_id: m_2526

TITLE: Learning Parsimonious Deep Feed-forward Networks

ABSTRACT: Convolutional neural networks and recurrent neural networks are designed with network structures well suited to the nature of spacial and sequential data respectively. However, the structure of standard feed-forward neural networks (FNNs) is simply a stack of fully connected layers, regardless of the feature correlations in data. In addition, the number of layers and the number of neurons are manually tuned on validation data, which is time-consuming and may lead to suboptimal networks. In this paper, we propose an unsupervised structure learning method for learning parsimonious deep FNNs. Our method determines the number of layers, the number of neurons at each layer, and the sparse connectivity between adjacent layers automatically from data. The resulting models are called Backbone-Skippath Neural Networks (BSNNs). Experiments on 17 tasks show that, in comparison with FNNs,  BSNNs can achieve better or comparable classification performance with much fewer parameters. The interpretability of BSNNs is also shown to be better than that of FNNs.

## item_id: m_2527

TITLE: LIQT: Bridging Liquid Neural Dynamics and Human Perceptual Mechanisms for Blind Image Quality Assessment

ABSTRACT: Blind Image Quality Assessment (BIQA) seeks to predict perceptual quality in reference-free scenarios, yet conventional methods often hard to capture the human visual system's adaptive spatio-temporal integration of degradation patterns. Inspired by the adaptive temporal dynamics of biological neural circuits, we propose Liquid Image Quality Transformer (LIQT), a novel BIQA framework that integrates Liquid Neural Networks (LNNs) with Transformer-based architectures. LIQT incorporates Liquid Self-Attention (LSA) equipped with Closed-Form Continuous-Time Module (CFCTM), which reformulates liquid time-constant neurons into stable closed-form solutions through learnable decay rates and Padé approximation, thus enabling LIQT to dynamically modulates feature extraction based on local image features. To emulate multi-scale perceptual evaluation, a Multi-Scale Image Quality-Aware Decoder (MIQAD) aggregates multi-scale features from LIQT for comprehensive quality regression. This work pioneers the integration of biomimetic neural mechanisms into BIQA and experiments in six benchmark datasets that span various types of distortion and image content demonstrate the superior performance of LIQT over state-of-the-art methods.

## item_id: m_2528

TITLE: EgoMap: Projective mapping and structured egocentric memory for Deep RL

ABSTRACT: Tasks involving localization, memorization and planning in partially observable 3D environments are an ongoing challenge in Deep Reinforcement Learning. We present EgoMap, a spatially structured neural memory architecture. EgoMap augments a deep reinforcement learning agent’s performance in 3D environments on challenging tasks with multi-step objectives. The EgoMap architecture incorporates several inductive biases including a differentiable inverse projection of CNN feature vectors onto a top-down spatially structured map. The map is updated with ego-motion measurements through a differentiable affine transform. We show this architecture outperforms both standard recurrent agents and state of the art agents with structured memory. We demonstrate that incorporating these inductive biases into an agent’s architecture allows for stable training with reward alone, circumventing the expense of acquiring and labelling expert trajectories. A detailed ablation study demonstrates the impact of key aspects of the architecture and through extensive qualitative analysis, we show how the agent exploits its structured internal memory to achieve higher performance. 

## item_id: m_2529

TITLE: Semi-Supervised Medical Image Segmentation via Knowledge Mining from Large Models

ABSTRACT: Large-scale vision models like SAM possess extensive visual knowledge, but their application to specialized tasks like medical image segmentation is often hindered by their general nature and the computational challenges associated with training and finetuning. Locally hosted small models such as U-Net++, designed for specific tasks, struggle with limited performance due to sparse labeled datasets. This study introduces a strategic knowledge mining method as a novel interaction mechanism between large and small models. Our method utilizes SAM’s broad visual understanding to enhance the specialized capabilities of locally hosted small deep learning models. Specifically, we trained a U-Net++ model on a limited labeled dataset and extend its capabilities by converting outputs (masks) produced in unlabeled images into prompts, to extract relevant knowledge from SAM. This process not only harnesses SAM’s generalized visual knowledge but also iteratively improves SAM’s prediction to cater specialized medical segmentation tasks via UNet++. The mined knowledge, serving as ‘pseudo labels’, enriches the training dataset, enabling the fine-tuning of the local network. Applied to the Kvasir SEG and COVID-QU-Ex datasets which consist of gastrointestinal polyp and lung Xray images respectively, our proposed method consistently enhanced the segmentation performance on Dice by 3% and 1% respectively over the baseline U-Net++ model, when the same amount of labelled data were used during training (75% and 50% of labelled data). Remarkably, our proposed method surpassed the baseline U-Net++ model even when the latter was trained exclusively on labeled data (100% of labelled data). These results underscore the potential of knowledge mining to overcome data limitations in specialized models by leveraging the broad, albeit general, knowledge of large-scale models like SAM, all while maintaining operational efficiency essential for clinical applications.The code of our method is publicly available at https://anonymous.4open.science/r/Knowledge-Mining-from-Large-Models-C7FE.

## item_id: m_2530

TITLE: UniComposer: Band-Level Music Composition with Symbolic and Audio Unification

ABSTRACT: Multi-track deep music generation has largely focused on pre-specified structures and instruments. However, it remains a challenge to generate "band-level" full-length music that is capable of allocating instruments based on musical features, their expressive potential, and their performance characteristics differences. Moreover, the representations of symbolic music and audio music have been treated as distinct sub-areas, without a unified architecture to join their own advantages. In this work, we introduce $\textbf{UniComposer}$, a novel music generation pipeline that composes at the band level, utilizing a hierarchical multi-track music representation complemented by four cascaded diffusion models which progressively generate rhythm features, and unified features extracted from both symbolic and audio music by autoencoders. Experiments and analysis demonstrate that UniComposer achieves a unified latent space for symbolic and audio music, and is capable of generating band-level compositions with well structured multi-track arrangements, surpassing previous methods in performances.

## item_id: m_2531

TITLE: Composing Task-Agnostic Policies with Deep Reinforcement Learning

ABSTRACT: The composition of elementary behaviors to solve challenging transfer learning problems is one of the key elements in building intelligent machines. To date, there has been plenty of work on learning task-specific policies or skills but almost no focus on composing necessary, task-agnostic skills to find a solution to new problems. In this paper, we propose a novel deep reinforcement learning-based skill transfer and composition method that takes the agent's primitive policies to solve unseen tasks. We evaluate our method in difficult cases where training policy through standard reinforcement learning (RL) or even hierarchical RL is either not feasible or exhibits high sample complexity. We show that our method not only transfers skills to new problem settings but also solves the challenging environments requiring both task planning and motion control with high data efficiency.

## item_id: m_2532

TITLE: Memory-Driven Text-to-Image Generation

ABSTRACT: We introduce a memory-driven semi-parametric approach to text-to-image generation, which is based on both parametric and non-parametric techniques. The non-parametric component is a memory bank of image features constructed from a training set of images. The parametric component is a generative adversarial network. Given a new text description at inference time, the memory bank is used to selectively retrieve image features that are provided as basic information of target images, which enables the generator to produce realistic synthetic results. We also incorporate the content information into the discriminator, together with semantic features, allowing the discriminator to make a more reliable prediction. Experimental results demonstrate that the proposed memory-driven semi-parametric approach produces more realistic images than purely parametric approaches, in terms of both visual fidelity and text-image semantic consistency.


## item_id: m_2533

TITLE: Dense Recurrent Neural Network with Attention Gate

ABSTRACT: We propose the dense RNN, which has the fully connections from each hidden state to multiple preceding hidden states of all layers directly. As the density of the connection increases, the number of paths through which the gradient flows can be increased. It increases the magnitude of gradients, which help to prevent the vanishing gradient problem in time. Larger gradients, however, can also cause exploding gradient problem. To complement the trade-off between two problems, we propose an attention gate, which controls the amounts of gradient flows. We describe the relation between the attention gate and the gradient flows by approximation. The experiment on the language modeling using Penn Treebank corpus shows dense connections with the attention gate improve the model’s performance.

## item_id: m_2534

TITLE: FedDebias: Reducing the Local Learning Bias Improves Federated Learning on Heterogeneous Data

ABSTRACT: Federated Learning (FL) is a machine learning paradigm that learns from data kept locally to safeguard the privacy of clients, whereas local SGD is typically employed on the clients' devices to improve communication efficiency. However, such a scheme is currently constrained by the slow and unstable convergence induced by clients' heterogeneous data. 
In this work, we identify three under-explored phenomena of the biased local learning that may explain these challenges caused by local updates in supervised FL.
As a remedy, we propose FedDebias, a novel unified algorithm that reduces the local learning bias on features and classifiers to tackle these challenges. 
FedDebias consists of two components:
The first component alleviates the bias in the local classifiers by balancing the output distribution of models. 
The second component learns client invariant features that are close to global features but considerably distinct from those learned from other input distributions. 
In a series of experiments, we show that FedDebias consistently outperforms other SOTA FL and domain generalization (DG) baselines, in which both two components have individual performance gains.

## item_id: m_2535

TITLE: Hyperspherical embedding for novel class classification

ABSTRACT:   Deep neural networks proved to be useful to learn representations and perform classification on many different modalities of data. Traditional approaches work well on the closed set problem. For learning tasks involving novel classes, known as the open set problem, the metric learning approach has been proposed. However, while promising, common metric learning approaches require pairwise learning, which significantly increases training cost while adding additional challenges. In this paper we present a method in which the similarity of samples projected onto a feature space is enforced by a metric learning approach without requiring
pairwise evaluation. We compare our approach against known methods in different datasets, achieving results up to $81\%$ more accurate.

## item_id: m_2536

TITLE: Towards Relaxing the Unbiasedness Condition of Doubly Robust Estimators for Debiased Recommendation

ABSTRACT: Recommender system aims to recommend items or information that may be of interest to users based on their behaviors and preferences. However, there may be sampling selection bias in the process of data collection, i.e., the collected data is not a representative of the target population. Many debiasing methods are developed based on pseudo-labelings. Nevertheless, the effectiveness of these methods relies heavily on accurate pseudo-labelings (i.e., the imputed labels), which is difficult to satisfy in practice. In this paper, in contrast to the existing doubly robust estimators that take strictly accurate pseudo-labelings as an unbiasedness condition, we theoretically propose several novel doubly robust estimators that are unbiased when either (a) the pseudo-labelings deviate from the true labels with an arbitrary user-specific inductive bias, item-specific inductive bias, or a combination of both, or (b) the learned propensities are accurate. We further propose a principled propensity reconstruction learning approach that adaptively updates the constraint weights using an attention mechanism and effectively controls the variance. To summarize, the proposed methods greatly relax the unbiasedness condition of the widely-adopted doubly robust estimators, which empirically result in much lower bias. Extensive experiments show that our approach outperforms the state-of-the-art on one semi-synthetic dataset and three real-world datasets.

## item_id: m_2537

TITLE: Adversarially Regularized Autoencoders

ABSTRACT: While autoencoders are a key technique in representation learning for continuous structures, such as images or wave forms, developing general-purpose autoencoders for discrete structures, such as text sequence or discretized images, has proven to be more challenging. In particular, discrete inputs make it more difficult to learn a smooth encoder that preserves the complex local relationships in the input space. In this work, we propose an adversarially regularized autoencoder (ARAE) with the goal of learning more robust discrete-space representations. ARAE jointly trains both a rich discrete-space encoder, such as an RNN, and a simpler continuous space generator function, while using generative adversarial network (GAN) training to constrain the distributions to be similar. This method yields a smoother contracted code space that maps similar inputs to nearby codes, and also an implicit latent variable GAN model for generation. Experiments on text and discretized images demonstrate that the GAN model produces clean interpolations and captures the multimodality of the original space, and that the autoencoder produces improvements in semi-supervised learning as well as state-of-the-art results in unaligned text style transfer task using only a shared continuous-space representation.

## item_id: m_2538

TITLE: Disentangling Representations of Text by Masking Transformers

ABSTRACT: Representations in large language models such as BERT encode a range of features into a single vector, which are predictive in the context of a multitude of downstream tasks. In this paper, we explore whether it is possible to learn disentangled representations  by identifying subnetworks in pre-trained models that encode distinct, complementary aspects of the representation. Concretely, we learn binary masks over transformer weights or hidden units to uncover the subset of features that correlate with a specific factor of variation. This sidesteps the need to train a disentangled model from scratch within a particular domain. We evaluate the ability of this method to disentangle representations of syntax and semantics, and sentiment from genre in the context of movie reviews. By combining this method with magnitude pruning we find that we can identify quite sparse subnetworks. Moreover, we find that this disentanglement-via-masking approach performs as well as or better than previously proposed methods based on variational autoencoders and adversarial training. 

## item_id: m_2539

TITLE: Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models

ABSTRACT: Large Language Models (LLMs) have recently demonstrated a remarkable success across various tasks. However, efficiently serving LLMs has been a challenge due to its large memory bottleneck, specifically in small batch inference settings (e.g. mobile devices). Weight-only quantization can be a promising approach, but sub-4 bit quantization remains a challenge due to large-magnitude activation outliers. To mitigate the undesirable outlier effect, we first propose per-IC quantization, a simple yet effective method that creates quantization groups within each input channel (IC) rather than the conventional per-output channel (OC). Our method is motivated by the observation that activation outliers affect the input dimension of the weight matrix, so similarly grouping the weights in the IC direction can $\textit{isolate outliers to be within a group}$. We also find that activation outliers do not dictate quantization difficulty, and inherent weight sensitivities also exist. With per-IC quantization as a new outlier-friendly scheme, we then propose Adaptive Dimensions ($\textbf{AdaDim}$), a versatile quantization framework that can adapt to various weight sensitivity patterns. We demonstrate the effectiveness of AdaDim by augmenting prior methods such as Round-To-Nearest and GPTQ, showing significant improvements across various language modeling benchmarks for both base (up to $+4.7\%$ on MMLU) and instruction-tuned (up to $+10\%$ on HumanEval) LLMs.

## item_id: m_2540

TITLE: Reinforcement Learning from Imperfect Demonstrations

ABSTRACT: Robust real-world  learning should benefit from both demonstrations and interaction with the environment. Current approaches to learning from demonstration and reward perform supervised learning on expert demonstration data and use reinforcement learning  to further improve performance based on reward from the environment. These tasks have divergent losses which are difficult to jointly optimize; further, such methods can be very sensitive to noisy demonstrations. We propose a unified reinforcement learning algorithm that effectively normalizes the Q-function, reducing the Q-values of actions unseen in the demonstration data.  Our Normalized Actor-Critic (NAC) method can learn from demonstration data of arbitrary quality and also leverages rewards from an interactive environment.  NAC learns an initial policy network from demonstration and refines the policy in a real environment. Crucially, both learning from demonstration and interactive refinement use exactly the same objective, unlike prior approaches that combine distinct supervised and reinforcement losses. This makes NAC robust to suboptimal demonstration data, since the method is not forced to mimic all of the examples in the dataset. We show that our unified reinforcement learning algorithm can learn robustly and  outperform existing baselines when evaluated on several realistic driving games.

## item_id: m_2541

TITLE: Recurrent Experience Replay in Distributed Reinforcement Learning

ABSTRACT: Building on the recent successes of distributed training of RL agents, in this paper we investigate the training of RNN-based RL agents from distributed prioritized experience replay. We study the effects of parameter lag resulting in representational drift and recurrent state staleness and empirically derive an improved training strategy. Using a single network architecture and fixed set of hyper-parameters, the resulting agent, Recurrent Replay Distributed DQN, quadruples the previous state of the art on Atari-57, and matches the state of the art on DMLab-30. It is the first agent to exceed human-level performance in 52 of the 57 Atari games.

## item_id: m_2542

TITLE: Towards a Unified and Verified Understanding of Group-Operation Networks

ABSTRACT: A recent line of work in mechanistic interpretability has focused on reverse-engineering the computation performed by neural networks trained on the binary operation of finite groups. We investigate the internals of one-hidden-layer neural networks trained on this task, revealing previously unidentified structure and producing a more complete description of such models in a step towards unifying the explanations of previous works (Chughtai et al., 2023; Stander et al., 2024). Notably, these models approximate equivariance in each input argument. We verify that our explanation applies to a large fraction of networks trained on this task by translating it into a compact proof of model performance, a quantitative evaluation of the extent to which we faithfully and concisely explain model internals. In the main text, we focus on the symmetric group S5. For models trained on this group, our explanation yields a guarantee of model accuracy that runs 3x faster than brute force and gives a >=95% accuracy bound for 45% of the models we trained. We were unable to obtain nontrivial non-vacuous accuracy bounds using only explanations from previous works.

## item_id: m_2543

TITLE: Likelihood Training of Schrödinger Bridge using Forward-Backward SDEs Theory

ABSTRACT: Schrödinger Bridge (SB) is an entropy-regularized optimal transport problem that has received increasing attention in deep generative modeling for its mathematical flexibility compared to the Scored-based Generative Model (SGM). However, it remains unclear whether the optimization principle of SB relates to the modern training of deep generative models, which often rely on constructing log-likelihood objectives.This raises questions on the suitability of SB models as a principled alternative for generative applications. In this work, we present a novel computational framework for likelihood training of SB models grounded on Forward-Backward Stochastic Differential Equations Theory – a mathematical methodology appeared in stochastic optimal control that transforms the optimality condition of SB into a set of SDEs. Crucially, these SDEs can be used to construct the likelihood objectives for SB that, surprisingly, generalizes the ones for SGM as special cases. This leads to a new optimization principle that inherits the same SB optimality yet without losing applications of modern generative training techniques, and we show that the resulting training algorithm achieves comparable results on generating realistic images on MNIST, CelebA, and CIFAR10. Our code is available at https://github.com/ghliu/SB-FBSDE.

## item_id: m_2544

TITLE: Distilling the Knowledge of BERT for Text Generation

ABSTRACT: Large-scale pre-trained language model, such as BERT, has recently achieved great success in a wide range of language understanding tasks. However, it remains an open question how to utilize BERT for text generation tasks. In this paper, we present a novel approach to addressing this challenge in a generic sequence-to-sequence (Seq2Seq) setting. We first propose a new task, Conditional Masked Language Modeling (C-MLM), to enable fine-tuning of BERT on target text-generation dataset. The fine-tuned BERT (i.e., teacher) is then exploited as extra supervision to improve conventional Seq2Seq models (i.e., student) for text generation. By leveraging BERT's idiosyncratic bidirectional nature, distilling the knowledge learned from BERT can encourage auto-regressive Seq2Seq models to plan ahead, imposing global sequence-level supervision for coherent text generation. Experiments show that the proposed approach significantly outperforms strong baselines of Transformer on multiple text generation tasks, including machine translation (MT) and text summarization. Our proposed model also achieves new state-of-the-art results on the IWSLT German-English and English-Vietnamese MT datasets.

## item_id: m_2545

TITLE: C5T5: Controllable Generation of Organic Molecules with Transformers

ABSTRACT: Methods for designing organic materials with desired properties have high potential impact across fields such as medicine, renewable energy, petrochemical engineering, and agriculture. However, using generative models for this task is difficult because candidate compounds must satisfy many constraints, including synthetic accessibility, intellectual property attributes, ``chemical beauty'' (Bickerton et al., 2020), and other considerations that are intuitive to domain experts but can be challenging to quantify. We propose C5T5, a novel self-supervised pretraining method that works in tandem with domain experts by making zero-shot select-and-replace edits, altering organic substances towards desired property values. C5T5 operates on IUPAC names---a standardized molecular representation that intuitively encodes rich structural information for organic chemists but that has been largely ignored by the ML community. Our technique requires no edited molecule pairs to train and only a rough estimate of molecular properties, and it has the potential to model long-range dependencies and symmetric molecular structures more easily than graph-based methods. We demonstrate C5T5's effectiveness on four physical properties relevant for drug discovery, showing that it learns successful and chemically intuitive strategies for altering molecules towards desired property values.


## item_id: m_2546

TITLE: Mani-WM: An Interactive World Model for Real-Robot Manipulation

ABSTRACT: Scalable robot learning in the real world is limited by the cost and safety issues of real robots. In addition, rolling out robot trajectories in the real world can be time-consuming and labor-intensive. In this paper, we propose to learn an interactive world model for robot manipulation as an alternative. We present a novel method, Mani-WM, which leverages the power of generative models to generate realistic videos of a robot arm executing a given action trajectory, starting from an initial given frame. Mani-WM employs a novel frame-level conditioning technique to ensure precise alignment between actions and video frames and leverages a diffusion transformer for high-quality video generation. To validate the effectiveness of Mani-WM, we perform extensive experiments on four challenging real-robot datasets. Results show that Mani-WM outperforms all the comparing baseline methods and is more preferable in human evaluations. We further showcase the flexible action controllability of Mani-WM by controlling the virtual robots in datasets with trajectories 1) predicted by an autonomous policy and 2) collected by a keyboard or VR controller. Finally, we combine Mani-WM with model-based planning to showcase its usefulness on real-robot manipulation tasks. We hope that Mani-WM can serve as an effective and scalable approach to enhance robot learning in the real world. To promote research on manipulation world models, we opensource the code at https://anonymous.4open.science/r/Mani-WM.

## item_id: m_2547

TITLE: Trend/Seasonality based Causal Structure for Time Series Counterfactual Outcome Prediction

ABSTRACT: In the causal effect estimation, most models have focused on estimating counterfactual outcomes in the static setting, and it is still difficult to predict the outcomes in the longitudinal setting due to time-varying confounder. To resolve the time-varying confounder issue, while the balance representation learning-based approaches have been primarily proposed, they inherently introduces a certain degree of selection bias since the balance representations act as confounders for both treatment and outcomes. In this paper, a new trend/seasonality decomposition based causal structure is proposed for the counterfactual outcome prediction in the time-series setting. We leverage a decomposition methodology to reduce the selection bias further. Specifically, it extracts meaningful decomposed representations such as confounders and adjustment variables, which help to yield more accurate treatment effect estimation with low variance. Inspired by the fact, the proposed causal structure learns trend/seasonality representations as the confounders/adjustment variables in the direction of minimizing the selection bias, and those representations are effective in the counterfactual outcome prediction especially under the long time sequence and high time-varying confounding settings. We evaluate the proposed causal structure with several trend/seasonality decomposition algorithms on synthetic and real-world datasets. From various experiments, the proposed causal structure achieves superior performance over the state-of-the-art algorithms.

## item_id: m_2548

TITLE: Rethinking the Smaller-Norm-Less-Informative Assumption in Channel Pruning of Convolution Layers

ABSTRACT: Model pruning has become a useful technique that improves the computational efficiency of deep learning, making it possible to deploy solutions in resource-limited scenarios. A widely-used practice in relevant work assumes that a smaller-norm parameter or feature plays a less informative role at the inference time. In this paper, we propose a channel pruning technique for accelerating the computations of deep convolutional neural networks (CNNs) that does not critically rely on this assumption. Instead, it focuses on direct simplification of the channel-to-channel computation graph of a CNN without the need of performing a computationally difficult and not-always-useful task of making high-dimensional tensors of CNN structured sparse. Our approach takes two stages: first to adopt an end-to-end stochastic training method that eventually forces the outputs of some channels to be constant, and then to prune those constant channels from the original neural network by adjusting the biases of their impacting layers such that the resulting compact model can be quickly fine-tuned. Our approach is mathematically appealing from an optimization perspective and easy to reproduce. We experimented our approach through several image learning benchmarks and demonstrate its interest- ing aspects and competitive performance.

## item_id: m_2549

TITLE: Deep Goal-Oriented Clustering

ABSTRACT: Clustering and prediction are two primary tasks in the fields of unsupervised and supervised learning, respectively. Although much of the recent advances in machine learning have been centered around those two tasks, the interdependent, mutually beneficial relationship between them is rarely explored. One could reasonably expect appropriately clustering the data would aid the downstream prediction task and, conversely, a better prediction performance for the downstream task could potentially inform a more appropriate clustering strategy. In this work, we focus on the latter part of this mutually beneficial relationship. To this end, we introduce Deep Goal-Oriented Clustering (DGC), a probabilistic framework that clusters the data by jointly using supervision via side-information and unsupervised modeling of the inherent data structure in an end-to-end fashion. We show the effectiveness of our model on a range of datasets by achieving prediction accuracies comparable to the state-of-the-art, while, more importantly in our setting, simultaneously learning congruent clustering strategies.

## item_id: m_2550

TITLE: Near-Optimal Representation Learning for Hierarchical Reinforcement Learning

ABSTRACT: We study the problem of representation learning in goal-conditioned hierarchical reinforcement learning. In such hierarchical structures, a higher-level controller solves tasks by iteratively communicating goals which a lower-level policy is trained to reach. Accordingly, the choice of representation -- the mapping of observation space to goal space -- is crucial. To study this problem, we develop a notion of sub-optimality of a representation, defined in terms of expected reward of the optimal hierarchical policy using this representation. We derive expressions which bound the sub-optimality and show how these expressions can be translated to representation learning objectives which may be optimized in practice. Results on a number of difficult continuous-control tasks show that our approach to representation learning yields qualitatively better representations as well as quantitatively better hierarchical policies, compared to existing methods.

## item_id: m_2551

TITLE: Communication Algorithms via Deep Learning

ABSTRACT: Coding theory is a central discipline underpinning wireline and wireless modems that are the workhorses of the information age. Progress in coding theory is largely driven by individual human ingenuity with sporadic breakthroughs over the past century. In this paper we study whether it is possible to automate the discovery of decoding algorithms via deep learning. We study a family of sequential codes parametrized by recurrent neural network (RNN) architectures. We show that cre- atively designed and trained RNN architectures can decode well known sequential codes such as the convolutional and turbo codes with close to optimal performance on the additive white Gaussian noise (AWGN) channel, which itself is achieved by breakthrough algorithms of our times (Viterbi and BCJR decoders, representing dynamic programing and forward-backward algorithms). We show strong gen- eralizations, i.e., we train at a specific signal to noise ratio and block length but test at a wide range of these quantities, as well as robustness and adaptivity to deviations from the AWGN setting.

## item_id: m_2552

TITLE: Skip Connections Eliminate Singularities

ABSTRACT: Skip connections made the training of very deep networks possible and have become an indispensable component in a variety of neural architectures. A completely satisfactory explanation for their success remains elusive. Here, we present a novel explanation for the benefits of skip connections in training very deep networks. The difficulty of training deep networks is partly due to the singularities caused by the non-identifiability of the model. Several such singularities have been identified in previous works: (i) overlap singularities caused by the permutation symmetry of nodes in a given layer, (ii) elimination singularities corresponding to the elimination, i.e. consistent deactivation, of nodes, (iii) singularities generated by the linear dependence of the nodes. These singularities cause degenerate manifolds in the loss landscape that slow down learning. We argue that skip connections eliminate these singularities by breaking the permutation symmetry of nodes, by reducing the possibility of node elimination and by making the nodes less linearly dependent. Moreover, for typical initializations, skip connections move the network away from the "ghosts" of these singularities and sculpt the landscape around them to alleviate the learning slow-down. These hypotheses are supported by evidence from simplified models, as well as from experiments with deep networks trained on real-world datasets.

## item_id: m_2553

TITLE: A Symbolic Framework for Evaluating Mathematical Reasoning with Transformers

ABSTRACT: This paper proposes a methodology for generating synthetic mathematical derivations via a computer algebra system to evaluate the generalisability of Transformers in symbolic and quantitative reasoning problems, and provides a general framework for building large-scale and high-quality benchmarks in the mathematical domain. In the context of classification tasks involving multi-step annotated derivations (spanning 18 mathematical operators), we leverage the framework to compare the mathematical capabilities of GPT-4, GPT-3.5, and a canon of fine-tuned BERT models, exploring the relationship between specific operators and generalisation failure. Surprisingly, the average in-distribution performance of BERT models surpasses GPT-3.5, and rivals GPT-4, yet simple data perturbations reduce BERT scores by up to 80 F1 points. The results suggest that the in-distribution performance and generalisability of smaller open-source models may potentially rival GPT in narrow mathematical domains by incorporating appropriately structured discourse-level relations during training, and highlight a shared weakness between BERT and GPT involving a relative inability to decode dependency relations involving indirect references to mathematical entities. We release the data generation framework along with all the resulting datasets and fine-tuned models\footnote{\url{https://github.com/anonymous/TBA}}.

## item_id: m_2554

TITLE: Learning Key Steps to Attack Deep Reinforcement Learning Agents

ABSTRACT: Deep reinforcement learning agents are known to be vulnerable to adversarial attacks. In particular, recent studies have shown that attacking a few key steps is effective for decreasing the agent's cumulative reward. However, all existing attacking methods find those key steps with human-designed heuristics, and it is not clear how more effective key steps can be identified. This paper introduces a novel reinforcement learning framework that learns more effective key steps through interacting with the agent. The proposed framework does not require any human heuristics nor knowledge, and can be flexibly coupled with any white-box or black-box adversarial attack scenarios. Experiments on benchmark Atari games across different scenarios demonstrate that the proposed framework is superior to existing methods for identifying more effective key steps.

## item_id: m_2555

TITLE: Stick-Breaking Variational Autoencoders

ABSTRACT: We extend Stochastic Gradient Variational Bayes to perform posterior inference for the weights of Stick-Breaking processes. This development allows us to define a Stick-Breaking Variational Autoencoder (SB-VAE), a Bayesian nonparametric version of the variational autoencoder that has a latent representation with stochastic dimensionality. We experimentally demonstrate that the SB-VAE, and a semi-supervised variant, learn highly discriminative latent representations that often outperform the Gaussian VAE’s.

## item_id: m_2556

TITLE: DAAS: Differentiable Architecture and Augmentation Policy Search

ABSTRACT: Neural architecture search (NAS) has been an active direction of automatic machine learning (Auto-ML), aiming to explore efficient network structures. The searched architecture is evaluated by training on datasets with fixed data augmentation policies. However, recent works on auto-augmentation show that the suited augmentation policies can vary over different structures. Therefore, this work considers the possible coupling between neural architectures and data augmentation and proposes an effective algorithm jointly searching for them. Specifically, 1) for the NAS task, we adopt a single-path based differentiable method with Gumbel-softmax reparameterization strategy due to its memory efficiency; 2) for the auto-augmentation task, we introduce a novel search method based on policy gradient algorithm, which can significantly reduce the computation complexity. Our approach achieves 97.91% accuracy on CIFAR-10 and 76.6% Top-1 accuracy on ImageNet dataset, showing the outstanding performance of our search algorithm.

## item_id: m_2557

TITLE: ZGS-Based Event-Driven Algorithms for Bayesian Optimization in Fully Distributed Multi-Agent Systems

ABSTRACT: Bayesian optimization (BO) is a well-established framework for globally optimizing expensive-to-evaluate black-box functions with impressive efficiency. Although numerous BO algorithms have been developed for the centralized machine learning setting and some recent works have extended BO to the tree-structured federated learning, no previous studies have investigated BO within a fully distributed multi-agent system (MAS) in the field of distributed learning (DL). Addressing this gap, we introduce and investigate a novel paradigm, Distributed Bayesian Optimization (DBO), in which agents cooperatively optimize the same costly-to-evaluate black-box objectives. An innovative generalized algorithm, Zero-Gradient-Sum-Based Event-Driven Distributed Lower Confidence Bound (ZGS-ED-DLCB), is proposed to overcome the significant challenges of DBO and DL: We (a) adopt a surrogate model based on random Fourier features as an approximate alternative to a typical Gaussian process to enable the exchange of local knowledge between neighboring agents, and (b) employ the event-driven mechanism to enhance communication efficiency in MASs. Moreover, we propose a novel generalized fully distributed convergence theorem, which represents a substantial theoretical and practical breakthrough wrt the ZGS-based DL. The performance of our proposed algorithm has been rigorously evaluated through theoretical analysis and extensive experiments, demonstrating substantial advantages over the state-of-the-art baselines.

## item_id: m_2558

TITLE: GENERATIVE LOW-SHOT NETWORK EXPANSION

ABSTRACT: Conventional deep learning classifiers are static in the sense that they are trained on
a predefined set of classes and learning to classify a novel class typically requires
re-training. In this work, we address the problem of Low-shot network-expansion
learning. We introduce a learning framework which enables expanding a pre-trained
(base) deep network to classify novel classes when the number of examples for the
novel classes is particularly small. We present a simple yet powerful distillation
method where the base network is augmented with additional weights to classify
the novel classes, while keeping the weights of the base network unchanged. We
term this learning hard distillation, since we preserve the response of the network
on the old classes to be equal in both the base and the expanded network. We
show that since only a small number of weights needs to be trained, the hard
distillation excels for low-shot training scenarios. Furthermore, hard distillation
avoids detriment to classification performance on the base classes. Finally, we
show that low-shot network expansion can be done with a very small memory
footprint by using a compact generative model of the base classes training data
with only a negligible degradation relative to learning with the full training set.

## item_id: m_2559

TITLE: Conditional Invertible Neural Networks for Guided Image Generation

ABSTRACT: In this work, we address the task of natural image generation guided by a conditioning input. We introduce a new architecture called conditional invertible neural network (cINN). It combines the purely generative INN model with an unconstrained feed-forward network, which efficiently pre-processes the conditioning input into useful features.  All parameters of a cINN are jointly optimized with a stable, maximum likelihood-based training procedure. Even though INNs and other normalizing flow models have received very little attention in the literature in contrast to GANs, we find that cINNs can achieve comparable quality, with some remarkable properties absent in cGANs, e.g.  apparent immunity to mode collapse. We demonstrate these properties for the tasks of MNIST digit generation and image colorization. Furthermore, we take advantage of our bidirectional cINN architecture to explore and manipulate emergent properties of the latent space, such as changing the image style in an intuitive way.

## item_id: m_2560

TITLE: On the Soft-Subnetwork for Few-Shot Class Incremental Learning

ABSTRACT: Inspired by Regularized Lottery Ticket Hypothesis, which states that competitive smooth (non-binary) subnetworks exist within a dense network, we propose a few-shot class-incremental learning method referred to as Soft-SubNetworks (SoftNet). Our objective is to learn a sequence of sessions incrementally, where each session only includes a few training instances per class while preserving the knowledge of the previously learned ones. SoftNet jointly learns the model weights and adaptive non-binary soft masks at a base training session in which each mask consists of the major and minor subnetwork; the former aims to minimize catastrophic forgetting during training, and the latter aims to avoid overfitting to a few samples in each new training session. We provide comprehensive empirical validations demonstrating that our SoftNet effectively tackles the few-shot incremental learning problem by surpassing the performance of state-of-the-art baselines over benchmark datasets.

## item_id: m_2561

TITLE: Deep Reinforcement Learning of Universal Policies with Diverse Environment Summaries

ABSTRACT: Deep reinforcement learning has enabled robots to complete complex tasks in simulation. However, the resulting policies do not transfer to real robots due to model errors in the simulator. One solution is to randomize the simulation environment, so that the resulting, trained policy achieves high performance in expectation over a variety of configurations that could represent the real-world. However, the distribution over simulator configurations must be carefully selected to represent the relevant dynamic modes of the system, as otherwise it can be unlikely to sample challenging configurations frequently enough. Moreover, the ideal distribution to improve the policy changes as the policy (un)learns to solve tasks in certain configurations. In this paper, we propose to use an inexpensive, kernel-based summarization method method that identifies configurations that lead to diverse behaviors. Since failure modes for the given task are naturally diverse, the policy trains on a mixture of representative and challenging configurations, which leads to more robust policies. In experiments, we show that the proposed method achieves the same performance as domain randomization in simple cases, but performs better when domain randomization does not lead to diverse dynamic modes.

## item_id: m_2562

TITLE: Pseudosaccades: A simple ensemble scheme for improving classification performance of deep nets

ABSTRACT: We describe a simple ensemble approach that, unlike conventional ensembles,
uses multiple random data sketches (‘pseudosaccades’) rather than multiple classifiers
to improve classification performance. Using this simple, but novel, approach
we obtain statistically significant improvements in classification performance on
AlexNet, GoogLeNet, ResNet-50 and ResNet-152 baselines on Imagenet data –
e.g. of the order of 0.3% to 0.6% in Top-1 accuracy and similar improvements in
Top-k accuracy – essentially nearly for free.

## item_id: m_2563

TITLE: Deconstructing Positional Information: From Attention Logits to Training Biases

ABSTRACT: Positional encodings, a mechanism for incorporating sequential information into the Transformer model, are central to contemporary research on neural architectures. Previous work has largely focused on understanding their function through the principle of distance attenuation, where proximity dictates influence. However, the interaction between positional and semantic information remains insufficiently explored, and the complexity of mainstream corpora hinders systematic, comparative studies of these methods. This paper addresses these challenges through a deconstruction of the attention-logit computation and a structured analysis of all mainstream positional encodings. A key focus is placed on Rotary Positional Embedding (RoPE), whose product-based structure uniquely facilitates a direct interaction between position and content. To probe this characteristic, we designed a novel synthetic task that explicitly demands a strong synthesis of positional and semantic information. As theoretically predicted, RoPE demonstrates a significant performance advantage over other encodings on this specialized task. Concurrently, this targeted evaluation uncovers an implicit training issue: a hidden bias manifesting as a distinct information aggregation phenomenon in the model's shallow layers, which we term the "single-head deposit pattern." Through subsequent ablation studies, we analyze this pattern and identify a method for its mitigation. These findings highlight the need for a deeper investigation into the training dynamics of positional encodings to bridge the gap between their theoretical design and practical implementation.

## item_id: m_2564

TITLE: DECap: Towards Generalized Explicit Caption Editing via Diffusion Mechanism

ABSTRACT: Explicit Caption Editing (ECE) --- refining reference image captions through a sequence of explicit edit operations (e.g., KEEP, DETELE words) --- has raised significant attention due to its explainable and human-like nature. After training with carefully designed reference and ground-truth caption pairs, state-of-the-art ECE models exhibit limited generalization ability beyond the original training data distribution, i.e., they are tailored to refine content details only in in-domain samples but fail to correct errors in out-of-domain samples. To this end, we propose a new Diffusion-based Explicit Caption editing method: DECap. Specifically, we reformulate the ECE task as a denoising process under the diffusion mechanism, and introduce innovative edit-based noising and denoising processes. The noising process can help to eliminate the need for meticulous paired data selection by directly introducing word-level noises (i.e., random words) for model training, learning diverse distribution over input reference captions. The denoising process involves the explicit predictions of edit operations and corresponding content words, refining reference captions through iterative step-wise editing. To further improve the inference speed for caption editing, DECap discards the prevalent multi-stage design, and directly generates edit operations and content words simultaneously. Extensive experiments have demonstrated the strong generalization ability of DECap in various caption editing scenarios. More interestingly, it also shows great potential in improving both the quality and controllability of caption generation.

## item_id: m_2565

TITLE: Learning to Plan Optimistically: Uncertainty-Guided Deep Exploration via Latent Model Ensembles

ABSTRACT: Learning complex behaviors through interaction requires coordinated long-term planning. Random exploration and novelty search lack task-centric guidance and waste effort on non-informative interactions. Instead, decision making should target samples with the potential to optimize performance far into the future, while only reducing uncertainty where conducive to this objective. This paper presents latent optimistic value exploration (LOVE), a strategy that enables deep exploration through optimism in the face of uncertain long-term rewards. We combine finite-horizon rollouts from a latent model with value function estimates to predict infinite-horizon returns and recover associated uncertainty through ensembling. Policy training then proceeds on an upper confidence bound (UCB) objective to identify and select the interactions most promising to improve long-term performance. We apply LOVE to continuous visual control tasks and demonstrate improved sample complexity on a selection of benchmarking tasks. 

## item_id: m_2566

TITLE: Learning Factorized Multimodal Representations

ABSTRACT: Learning multimodal representations is a fundamentally complex research problem due to the presence of multiple heterogeneous sources of information. Although the presence of multiple modalities provides additional valuable information, there are two key challenges to address when learning from multimodal data: 1) models must learn the complex intra-modal and cross-modal interactions for prediction and 2) models must be robust to unexpected missing or noisy modalities during testing. In this paper, we propose to optimize for a joint generative-discriminative objective across multimodal data and labels. We introduce a model that factorizes representations into two sets of independent factors: multimodal discriminative and modality-specific generative factors. Multimodal discriminative factors are shared across all modalities and contain joint multimodal features required for discriminative tasks such as sentiment prediction. Modality-specific generative factors are unique for each modality and contain the information required for generating data. Experimental results show that our model is able to learn meaningful multimodal representations that achieve state-of-the-art or competitive performance on six multimodal datasets. Our model demonstrates flexible generative capabilities by conditioning on independent factors and can reconstruct missing modalities without significantly impacting performance. Lastly, we interpret our factorized representations to understand the interactions that influence multimodal learning.

## item_id: m_2567

TITLE: Universal Approximation Theorem for Equivariant Maps by Group CNNs

ABSTRACT: Group symmetry is inherent in a wide variety of data distributions. Data processing that preserves symmetry is described as an equivariant map and often effective in achieving high performance. Convolutional neural networks (CNNs) have been known as models with equivariance and shown to approximate equivariant maps for some specific groups. However, universal approximation theorems for CNNs have been separately derived with individual techniques according to each group and setting. This paper provides a unified method to obtain universal approximation theorems for equivariant maps by CNNs in various settings. As its significant advantage, we can handle non-linear equivariant maps between infinite-dimensional spaces for non-compact groups.

## item_id: m_2568

TITLE: ModernVBERT: Towards Smaller Visual Document Retrievers

ABSTRACT: Retrieving specific information from a large corpus of documents is a widely prevalent industrial use case of modern AI, notably due to the popularity of Retrieval-Augmented Generation (RAG) systems. Although neural document retrieval models have historically operated exclusively in the text space, Visual Document Retrieval (VDR) models - large vision–language decoders repurposed as embedding models which directly work with page screenshots as inputs - are increasingly popular due to the performance and indexing latency gains they offer. In this work, we show that, while cost-efficient, this approach of repurposing generative models bottlenecks retrieval performance.
    
Through controlled experiments, we revisit the entire training pipeline, and establish a principled recipe for improving visual document retrieval models. We notably measure the impact of attention masking, image resolution, modality alignment data regimes, and late interaction centered contrastive objectives which emerge as central performance factors.
Building on these insights, we release ModernVBert, a compact 250M parameter vision–language encoder that outperforms recent models up to 10 times larger when fine-tuned on document retrieval tasks, enabling efficient inference on cheap CPU hardware and greatly reducing latency and costs while maintaining strong performance. Models, code and data are available in the public version of this work under an open license.

## item_id: m_2569

TITLE: Adversarial Meta-Learning

ABSTRACT: Meta-learning enables a model to learn from very limited data to undertake a new task. In this paper, we study the general meta-learning with adversarial samples. We present a meta-learning algorithm, ADML (ADversarial Meta-Learner), which leverages clean and adversarial samples to optimize the initialization of a learning model in an adversarial manner. ADML leads to the following desirable properties: 1) it turns out to be very effective even in the cases with only clean samples; 2) it is robust to adversarial samples, i.e., unlike other meta-learning algorithms, it only leads to a minor performance degradation when there are adversarial samples; 3) it sheds light on tackling the cases with limited and even contaminated samples. It has been shown by extensive experimental results that ADML outperforms several representative meta-learning algorithms in the cases involving adversarial samples generated by different attack mechanisms, on two widely-used image datasets, MiniImageNet and CIFAR100, in terms of both accuracy and robustness.

## item_id: m_2570

TITLE: Sample-Efficient Learning of POMDPs with Multiple Observations In Hindsight

ABSTRACT: This paper studies the sample-efficiency of learning in Partially Observable Markov Decision Processes (POMDPs), a challenging problem in reinforcement learning that is known to be exponentially hard in the worst-case. Motivated by real-world settings such as loading in game playing, we propose an enhanced feedback model called ``multiple observations in hindsight'', where after each episode of interaction with the POMDP, the learner may collect multiple additional observations emitted from the encountered latent states, but may not observe the latent states themselves. We show that sample-efficient learning under this feedback model is possible for two new subclasses of POMDPs: \emph{multi-observation revealing POMDPs} and \emph{distinguishable POMDPs}. Both subclasses generalize and substantially relax \emph{revealing POMDPs}---a widely studied subclass for which sample-efficient learning is possible under standard trajectory feedback. Notably, distinguishable POMDPs only require the emission distributions from different latent states to be \emph{different} instead of \emph{linearly independent} as required in revealing POMDPs.

## item_id: m_2571

TITLE: SALSA-TEXT : SELF ATTENTIVE LATENT SPACE BASED ADVERSARIAL TEXT GENERATION

ABSTRACT: Inspired by the success of self attention mechanism and Transformer architecture
in sequence transduction and image generation applications, we propose novel self
attention-based architectures to improve the performance of adversarial latent code-
based schemes in text generation. Adversarial latent code-based text generation
has recently gained a lot of attention due to their promising results. In this paper,
we take a step to fortify the architectures used in these setups, specifically AAE
and ARAE. We benchmark two latent code-based methods (AAE and ARAE)
designed based on adversarial setups. In our experiments, the Google sentence
compression dataset is utilized to compare our method with these methods using
various objective and subjective measures. The experiments demonstrate the
proposed (self) attention-based models outperform the state-of-the-art in adversarial
code-based text generation.

## item_id: m_2572

TITLE: Universally Optimal Watermarking Schemes for LLMs: from Theory to Practice

ABSTRACT: Large Language Models (LLMs) boosts human efficiency but also poses misuse risks, with watermarking serving as a reliable method to differentiate AI-generated content from human-created text. In this work, we propose a novel theoretical framework for watermarking LLMs. Particularly, we jointly optimize both the watermarking scheme and detector to maximize detection performance, while controlling the worst-case Type-I error and distortion in the watermarked text.  Within our framework, we characterize the _universally minimum Type-II error_, showing a fundamental trade-off between detection performance and distortion. More importantly, we identify the optimal type of detectors and watermarking schemes. Building upon our theoretical analysis, we introduce a practical, model-agnostic and computationally efficient token-level watermarking algorithm that invokes a surrogate model and the Gumbel-max trick. Empirical results on Llama-13B and Mistral-8$\times$7B demonstrate the effectiveness of our method. Furthermore, we also explore how robustness can be integrated into our theoretical framework, which provides a foundation for designing future watermarking systems with improved resilience to adversarial attacks.

## item_id: m_2573

TITLE: Generative Spoken Language Model based on continuous word-sized audio tokens

ABSTRACT: In NLP, text language models based on words or subwords are known to outperform their character-based counterparts. Yet, in the speech community, the standard input of spoken LMs are 20ms-long discrete units (shorter than a phoneme). Taking inspiration from word-based LM, we introduce a Generative Spoken Language Model (GSLM) based on word-size continuous-valued audio tokens that can generate diverse and expressive language output. This is obtained by replacing lookup table for lexical types with a Lexical Embedding function, the cross entropy loss by a contrastive loss, and multinomial sampling by k-NN sampling. The resulting model is the first generative language model based on word-size continuous tokens. Its performance is on par with discrete unit GSLMs regarding generation quality and zero resource challenge metrics. Moreover, it is five times more memory efficient because of its larger units. In addition, the embeddings before and after the Lexical Embedder are phonetically and semantically interpretable.

## item_id: m_2574

TITLE: ROPES: Robotic Pose Estimation via Score-based Causal Representation Learning

ABSTRACT: Causal representation learning (CRL) has emerged as a powerful unsupervised
framework that can (i) disentangle the latent generative factors underlying highdimensional data, and (ii) learn the cause-and-effect interactions among the disentangled variables. There have been extensive recent advances in the identifiability
aspects of CRL, accompanied by some practical progress. However, a substantial
gap remains between theory and real-world practice. This paper takes a step toward
closing that gap by bringing CRL into robotics, a domain that has motivated CRL.
Specifically, this paper addresses the well-defined robot pose estimation – the
recovery of position and orientation from raw images – by introducing RObotic
Pose Estimation via Score-Based CRL (ROPES). Being an unsupervised framework, ROPES embodies the essence of interventional CRL by identifying those
generative factors that are actuated: images are generated by intrinsic and extrinsic
latent factors (e.g., joint angles, arm/limb geometry, lighting, background, and
camera configuration) and the objective is to disentangle and recover the controllable latent variables, i.e., those that can be directly manipulated (intervened
upon) through actuation. Interventional CRL theory establishes that variables
that undergo variations induced by interventions can be identified. In robotics,
such interventions arise naturally by commanding actuators of various joints and
recording images under varied controls. Empirical evaluations in semi-synthetic
manipulator experiments demonstrate that ROPES successfully disentangles latent
generative factors with high fidelity with respect to the ground truth. Crucially, this
is achieved by leveraging only distributional changes, without using any labeled
data. The paper also includes a comparison with a baseline based on a recently
proposed semi-supervised framework. This paper concludes by positioning robot
pose estimation as a near-practical testbed for CRL.

## item_id: m_2575

TITLE: Transferred Discrepancy: Quantifying the Difference Between Representations

ABSTRACT: Understanding what information neural networks capture is an essential problem in deep learning, and studying whether different models capture similar features is an initial step to achieve this goal. Previous works sought to define metrics over the feature matrices to measure the difference between two models. However, different metrics sometimes lead to contradictory conclusions, and there has been no consensus on which metric is suitable to use in practice. In this work, we propose a novel metric that goes beyond previous approaches. Recall that one of the most practical scenarios of using the learned representations is to apply them to downstream tasks. We argue that we should design the metric based on a similar principle. For that, we introduce the transferred discrepancy (TD), a new metric that defines the difference between two representations based on their downstream-task performance. Through an asymptotic analysis, we show how TD correlates with downstream tasks and the necessity to define metrics in such a task-dependent fashion.  In particular, we also show that under specific conditions, the TD metric is closely related to previous metrics. Our experiments show that TD can provide fine-grained information for varied downstream tasks, and for the models trained from different initializations, the learned features are not the same in terms of downstream-task predictions. We find that TD may also be used to evaluate the effectiveness of different training strategies. For example, we demonstrate that the models trained with proper data augmentations that improve the generalization capture more similar features in terms of TD, while those with data augmentations that hurt the generalization will not. This suggests a training strategy that leads to more robust representation also trains models that generalize better. 

## item_id: m_2576

TITLE: EGraFFBench: Evaluation of Equivariant Graph Neural Network Force Fields for Atomistic Simulations

ABSTRACT: Equivariant graph neural networks force fields (EGraFFs) have shown great promise in modelling complex interactions in atomic systems by exploiting the graphs’ inherent symmetries. Recent works have led to a surge in the development of novel architectures that incorporate equivariance-based inductive biases alongside architectural innovations like graph transformers and message passing to model atomic interactions. However, thorough evaluations of these deploying EGraFFs for the downstream task of real-world atomistic simulations, is lacking. To this end, here we perform a systematic benchmarking of 6 EGraFF algorithms (NequIP, Allegro, BOTNet, MACE, Equiformer, TorchMDNet), with the aim of understanding their capabilities and limitations for realistic atomistic simulations. In addition to our thorough evaluation and analysis on eight existing datasets based on the benchmarking literature, we release two new benchmark datasets, propose four new metrics, and three new challenging tasks. The new datasets and tasks evaluate the performance of EGraFF to out-of-distribution data, in terms of different crystal structures, temperatures, and new molecules. Interestingly, evaluation of the EGraFF models based on dynamic simulations reveals that having a lower error on energy or force does not guarantee stable or reliable simulation or faithful replication of the atomic structures. Moreover, we find that no model clearly outperforms other models on all datasets and tasks. Importantly, we show that the performance of all the models on out-of-distribution datasets is unreliable, pointing to the need for the development of a foundation model for force fields that can be used in real-world simulations. In summary, this work establishes a rigorous framework for evaluating machine learning force fields in the context of atomic simulations and points to open research challenges within this domain.

## item_id: m_2577

TITLE: Unsupervised Pretraining for Sequence to Sequence Learning

ABSTRACT: This work presents a general unsupervised learning method to improve
the accuracy of sequence to sequence (seq2seq) models. In our method, the
weights of the encoder and decoder of a seq2seq model are initialized
with the pretrained weights of two language models and then 
fine-tuned with labeled data. We apply this method to
challenging benchmarks in machine translation and abstractive
summarization and find that it significantly improves the subsequent
supervised models.  Our main result is that the pretraining
accelerates training and improves generalization of seq2seq models,
achieving state-of-the-art results on the WMT
English->German task, surpassing a range of methods using
both phrase-based machine translation and neural machine
translation. Our method achieves an improvement of 1.3 BLEU from the
previous best models on both WMT'14 and WMT'15
English->German. On summarization, our method beats
the supervised learning baseline.

## item_id: m_2578

TITLE: Not-So-Random Features

ABSTRACT: We propose a principled method for kernel learning, which relies on a Fourier-analytic characterization of translation-invariant or rotation-invariant kernels. Our method produces a sequence of feature maps, iteratively refining the SVM margin. We provide rigorous guarantees for optimality and generalization, interpreting our algorithm as online equilibrium-finding dynamics in a certain two-player min-max game. Evaluations on synthetic and real-world datasets demonstrate scalability and consistent improvements over related random features-based methods.

## item_id: m_2579

TITLE: Cluster Tree for Nearest Neighbor Search

ABSTRACT: Tree-based algorithms are an important and widely used class of algorithms for  Nearest Neighbor Search (NNS) with random partition (RP) tree being arguably the most well studied. However, in spite of possessing theoretical guarantees and strong practical performance, a major drawback of the RP tree is its lack of adaptability to the input dataset.

Inspired by recent theoretical and practical works for NNS, we attempt to remedy this by introducing ClusterTree, a new tree based algorithm. Our approach utilizes randomness as in RP trees while adapting to the underlying cluster structure of the dataset to create well-balanced and meaningful partitions. Experimental evaluations on real world datasets demonstrate improvements over RP trees and other tree based methods for NNS while maintaining efficient construction time. In addition, we show theoretically and empirically that ClusterTree finds partitions which are superior to those found by RP trees in preserving the cluster structure of the input dataset.

## item_id: m_2580

TITLE: Neural Fingerprints for Adversarial Attack Detection

ABSTRACT: Deep learning models for image classification have become standard tools in recent years. However, a well known
vulnerability of these models is their susceptibility to  adversarial examples. Adversarial examples are generated 
by slightly altering an image of a certain class in a way that is imperceptible to humans but causes the model to classify it wrongly as another class. Many algorithms have been proposed to address this problem, falling generally into one of two categories: (i) building robust classifiers (ii) directly detecting attacked images. Despite the very good performance of the proposed detectors, we argue that in a white-box setting, where the attacker knows the configuration and weights of the network and the detector, the attacker can overcome the detector by running many examples on a local copy, and sending only examples that were not detected to the actual model. This problem of addressing complete knowledge of the attacker is common in security applications where even a very good model is not sufficient to ensure safety. In this paper we propose to overcome this inherent limitation of any static defence with randomization. To do so, one must generate a very large family of detectors with consistent performance, and select one or more of them randomly for each input. For the individual detectors, we suggest the method of neural fingerprints. In the training phase, for each class we repeatedly sample a tiny random subset of neurons from certain layers of the network, and if their average is sufficiently different between clean and attacked images of the focal class they are considered a fingerprint and added to the detector bank. During test time, we sample fingerprints from the bank associated with the label predicted by the model, and detect attacks using a likelihood ratio test. We evaluate our detectors on ImageNet with different attack methods and model architectures, and show near-perfect detection with low rates of false detection.

## item_id: m_2581

TITLE: Locally Linear Unsupervised Feature Selection

ABSTRACT: The paper, interested in unsupervised feature selection, aims to retain the features best accounting for the local patterns in the data. The proposed approach, called Locally Linear Unsupervised Feature Selection, relies on a dimensionality reduction method to characterize such patterns; each feature is thereafter assessed according to its compliance w.r.t. the local patterns, taking inspiration from Locally Linear Embedding (Roweis and Saul, 2000). The experimental validation of the approach on the scikit-feature benchmark suite demonstrates its effectiveness compared to the state of the art.

## item_id: m_2582

TITLE: QuadCal: Calibration for In-Context Learning

ABSTRACT: Large language models (LLMs) are increasingly being applied to high-stakes domains with high consequences for errors such as healthcare, drug discovery, law, and finance. However, they are often unstable and highly sensitive to prompt design, which can introduce contextual bias into their predictions. To mitigate this bias, various calibration methods have been developed to prevent overconfident and incorrect predictions. Existing techniques are either confidence-based, relying on heuristics to quantify bias, or likelihood-based, which is theoretically grounded but introduces unnecessary computational overhead. In this work, we introduce QuadCal, a novel supervised likelihood-based calibration method that is up to 40% faster and outperforms the existing likelihood-based approach. Specifically, QuadCal leverages Quadratic Discriminant Analysis (QDA), a supervised algorithm that directly models class-conditioned distributions, making it more efficient. We evaluated calibration methods on GPT-2 models and the more recent Llama and Gemma’s instruction-tuned (IT) models, which are harder to calibrate. Empirically, we show that on average over seven different natural language classification datasets, QuadCal outperforms existing methods on GPT-2 models and is competitive with earlier methods on IT models.

## item_id: m_2583

TITLE: Cross-modal Graph Contrastive Learning with Cellular Images

ABSTRACT: Constructing discriminative representations of molecules lies at the core of a number of domains such as drug discovery, material science, and chemistry. State-of-the-art methods employ graph neural networks (GNNs) and self-supervised learning (SSL) to learn the structural representations from unlabeled data, which can then be fine-tuned for downstream tasks. Albeit powerful, these methods that are pre-trained solely on molecular structures cannot generalize well to the tasks involved in intricate biological processes. To cope with this challenge, we propose using high-content cell microscopy images to assist in learning molecular representation. The fundamental rationale of our method is to leverage the correspondence between molecular topological structures and the caused perturbations at the phenotypic level. By including cross-modal pre-training with different types of contrastive loss functions in a unified framework, our model can efficiently learn generic and informative representations from cellular images, which are complementary to molecular structures. Empirical experiments demonstrated that the model transfers non-trivially to a variety of downstream tasks and is often competitive with the existing SSL baselines, e.g., a 15.4\% absolute Hit@10 gains in graph-image retrieval task and a 4.0\% absolute AUC improvements in clinical outcome predictions. Further zero-shot case studies show the potential of the approach to be applied to real-world drug discovery. 

## item_id: m_2584

TITLE: A  Model Cortical Network for Spatiotemporal Sequence Learning and Prediction

ABSTRACT: In this paper we developed a hierarchical network model, called Hierarchical Prediction Network (HPNet) to understand how spatiotemporal memories might be learned and encoded in a representational hierarchy for predicting future video frames. The model is inspired by the feedforward, feedback and lateral recurrent circuits in the mammalian hierarchical visual system. It assumes that spatiotemporal memories are encoded in the recurrent connections within each level and between different levels of the hierarchy. The model contains a feed-forward path that  computes and encodes spatiotemporal features of successive complexity and a feedback path that projects interpretation from a higher level to the level below. Within each level, the feed-forward path and the feedback path intersect in a recurrent gated circuit that integrates their signals as well as the circuit's internal memory states to generate  a prediction of the incoming signals. The network learns by comparing the incoming signals with its prediction, updating its internal model of the world by minimizing the prediction errors at each level of the hierarchy in the style of {\em predictive self-supervised learning}. The network processes data in blocks of video  frames rather than  a frame-to-frame basis.  This allows it to learn relationships among movement patterns, yielding state-of-the-art performance in long range video sequence predictions in benchmark datasets. We observed that hierarchical interaction in the network introduces sensitivity to memories of global movement patterns even in the population representation of the units in the earliest level. Finally, we provided neurophysiological evidence, showing that neurons in the early visual cortex of awake monkeys exhibit very similar sensitivity and behaviors. These findings suggest that  predictive self-supervised learning might be an important principle for representational learning in the visual cortex.  

## item_id: m_2585

TITLE: Maximum Likelihood Constraint Inference for Inverse Reinforcement Learning

ABSTRACT: While most approaches to the problem of Inverse Reinforcement Learning (IRL) focus on estimating a reward function that best explains an expert agent’s policy or demonstrated behavior on a control task, it is often the case that such behavior is more succinctly represented by a simple reward combined with a set of hard constraints. In this setting, the agent is attempting to maximize cumulative rewards subject to these given constraints on their behavior. We reformulate the problem of IRL on Markov Decision Processes (MDPs) such that, given a nominal model of the environment and a nominal reward function, we seek to estimate state, action, and feature constraints in the environment that motivate an agent’s behavior. Our approach is based on the Maximum Entropy IRL framework, which allows us to reason about the likelihood of an expert agent’s demonstrations given our knowledge of an MDP. Using our method, we can infer which constraints can be added to the MDP to most increase the likelihood of observing these demonstrations. We present an algorithm which iteratively infers the Maximum Likelihood Constraint to best explain observed behavior, and we evaluate its efficacy using both simulated behavior and recorded data of humans navigating around an obstacle.

## item_id: m_2586

TITLE: Certified Robustness for Top-k Predictions against Adversarial Perturbations via Randomized Smoothing

ABSTRACT: It is well-known that  classifiers are vulnerable to adversarial perturbations. To defend against adversarial perturbations, various certified robustness results have been derived. However, existing certified robustnesses are limited to top-1 predictions. In many real-world applications, top-$k$ predictions are more relevant. In this work, we aim to derive certified robustness for top-$k$ predictions. In particular, our certified robustness is based on randomized smoothing, which turns any classifier to a new classifier via adding noise to an input example. We adopt randomized smoothing because it is scalable to large-scale neural networks and applicable to any classifier. We derive a tight robustness in $\ell_2$ norm for top-$k$ predictions  when using randomized smoothing with Gaussian noise. We find that generalizing the certified robustness  from top-1 to top-$k$ predictions faces significant technical challenges. We also empirically evaluate our method on CIFAR10 and ImageNet. For example, our method can obtain an ImageNet classifier with a certified top-5 accuracy of 62.8\% when the $\ell_2$-norms of the adversarial perturbations are less than 0.5 (=127/255). Our code is publicly available at: \url{https://github.com/jjy1994/Certify_Topk}. 

## item_id: m_2587

TITLE: Learning to play slot cars and Atari 2600 games in just minutes

ABSTRACT: Machine learning algorithms for controlling devices will need to learn quickly, with few trials. Such a goal can be attained with concepts borrowed from continental philosophy and formalized using tools from the mathematical theory of categories. Illustrations of this approach are presented on a cyberphysical system: the slot car game, and also on Atari 2600 games.

## item_id: m_2588

TITLE: Describe-to-Score: Text-Guided Efficient Image Complexity Assessment

ABSTRACT: Accurately assessing image complexity (IC) is essential for many vision tasks, yet existing approaches rely almost exclusively on visual features and therefore fail to capture the high-level semantics that humans often use when judging complexity. We introduce a multimodal perspective for IC modeling by integrating visual representations with caption-derived textual semantics. This integration enriches the representational space and provides complementary structural cues that are difficult to infer from vision alone. From an information theoretic and representation viewpoint, we offer an idealized analysis suggesting how semantic guidance can regularize the hypothesis space and support more stable generalization. We present D2S (Describe-to-Score), a framework that generates natural-language descriptions using a pretrained vision–language model and aligns the visual encoder with textual structure through feature alignment and entropy distribution alignment. These mechanisms encourage the visual backbone to internalize semantic regularities during training. Importantly, D2S employs text only during training and maintains a vision-only inference pipeline with no additional computational overhead. Experiments show that D2S achieves state-of-the-art performance on the IC9600 benchmark and remains competitive on no-reference image quality assessment (NR-IQA) tasks. Additional studies demonstrate robustness across captioners and prompt designs, and improved semantic transferability on downstream probing tasks, highlighting the effectiveness of multimodal guidance for complexity-related modeling.

## item_id: m_2589

TITLE: InvBench: Can LLMs Accelerate Program Verification with Invariant Synthesis?

ABSTRACT: Program verification relies on loop invariants, yet automatically discovering strong invariants remains a long-standing challenge. We introduce a principled framework for evaluating LLMs on invariant synthesis. Our approach uses a verifier-based decision procedure with a formal soundness guarantee and assesses not only correctness but also the speedup that invariants provide in verification. We evaluate 7 state-of-the-art LLMs, and existing LLM-based verifiers against the traditional solver UAutomizer. While LLM-based verifiers represent a promising direction, they do not yet offer a significant advantage over UAutomizer. Model capability also proves critical, as shown by sharp differences in speedups across models, and our benchmark remains an open challenge for current LLMs. Finally, we show that supervised fine-tuning and Best-of-N sampling can improve performance: fine-tuning on 3589 instances raises the percentage of speedup cases for Qwen3- Coder-480B from 8% to 29.2%, and Best-of-N sampling with N=16 improves Claude-sonnet-4 from 8.8% to 22.1%. We release our dataset for training and evaluation at https://anonymous.4open.science/r/InvBench/.

## item_id: m_2590

TITLE: Ask the Right Questions: Active Question Reformulation with Reinforcement Learning

ABSTRACT: We frame Question Answering (QA) as a Reinforcement Learning task, an approach that we call Active Question Answering. 

We propose an agent that sits between the user and a black box QA system and learns to reformulate questions to elicit the best possible answers. The agent probes the system with, potentially many, natural language reformulations of an initial question and aggregates the returned evidence to yield the best answer. 

The reformulation system is trained end-to-end to maximize answer quality using policy gradient. We evaluate on SearchQA, a dataset of complex questions extracted from Jeopardy!. The agent outperforms a state-of-the-art base model, playing the role of the environment, and other benchmarks.

We also analyze the language that the agent has learned while interacting with the question answering system. We find that successful question reformulations look quite different from natural language paraphrases. The agent is able to discover non-trivial reformulation strategies that resemble classic information retrieval techniques such as term re-weighting (tf-idf) and stemming.

## item_id: m_2591

TITLE: Soft Weight-Sharing for Neural Network Compression

ABSTRACT: The success of deep learning in numerous application domains created the desire to run and train them on mobile devices. This however, conflicts with their computationally, memory and energy intense nature, leading to a growing interest in compression.
Recent work by Han et al. (2016) propose a pipeline that involves retraining, pruning and quantization of neural network weights, obtaining state-of-the-art compression rates.
In this paper, we show that competitive compression rates can be achieved by using a version of "soft weight-sharing" (Nowlan & Hinton, 1991). Our method achieves both quantization and pruning in one simple (re-)training procedure. 
This point of view also exposes the relation between compression and the minimum description length (MDL) principle. 

## item_id: m_2592

TITLE: Ecological Reinforcement Learning

ABSTRACT: Reinforcement learning algorithms have been shown to effectively learn tasks in a variety of static, deterministic, and  simplistic environments, but their application to environments which are characteristic of dynamic lifelong settings encountered in the real world has been limited. Understanding the impact of specific environmental properties on the learning dynamics of reinforcement learning algorithms is important as we want to align the environments in which we develop our algorithms with the real world, and this is strongly coupled with the type of intelligence which can be learned. In this work, we study what we refer to as ecological reinforcement learning: the interaction between properties of the environment and the reinforcement learning agent. To this end, we introduce environments with characteristics that we argue better reflect natural environments: non-episodic learning, uninformative ``fundamental drive'' reward signals, and natural dynamics that cause the environment to change even when the agent fails to take intelligent actions. We show these factors can have a profound effect on the learning progress of reinforcement learning algorithms. Surprisingly, we find that these seemingly more challenging learning conditions can often make reinforcement learning agents learn more effectively. Through this study, we hope to shift the focus of the community towards learning in realistic, natural environments with dynamic elements.

## item_id: m_2593

TITLE: Entropy-SGD: Biasing Gradient Descent Into Wide Valleys

ABSTRACT: This paper proposes a new optimization algorithm called Entropy-SGD for training deep neural networks that is motivated by the local geometry of the energy landscape. Local extrema with low generalization error have a large proportion of almost-zero eigenvalues in the Hessian with very few positive or negative eigenvalues. We leverage upon this observation to construct a local-entropy-based objective function that favors well-generalizable solutions lying in large flat regions of the energy landscape, while avoiding poorly-generalizable solutions located in the sharp valleys. Conceptually, our algorithm resembles two nested loops of SGD where we use Langevin dynamics in the inner loop to compute the gradient of the local entropy before each update of the weights. We show that the new objective has a smoother energy landscape and show improved generalization over SGD using uniform stability, under certain assumptions. Our experiments on convolutional and recurrent neural networks demonstrate that Entropy-SGD compares favorably to state-of-the-art techniques in terms of generalization error and training time.

## item_id: m_2594

TITLE: Inefficiency of stochastic gradient descent with larger mini-batches (and more learners)

ABSTRACT: Stochastic Gradient Descent (SGD) and its variants are the most important optimization algorithms used in large scale machine learning. Mini-batch version of stochastic gradient is often used in practice for taking advantage of hardware parallelism. In this work, we analyze the effect of mini-batch size over SGD convergence for the case of general non-convex objective functions. Building on the past analyses, we justify mathematically that there can often be a large difference between the convergence guarantees provided by small and large mini-batches (given each instance processes equal number of training samples), while providing experimental evidence for the same. Going further to distributed settings, we show that an analogous effect holds with popular Asynchronous Gradient Descent (\asgd): there can be a large difference between convergence guarantees with increasing number of learners given that the cumulative number of training samples processed remains the same. Thus there is an inherent (and similar) inefficiency introduced in the convergence behavior when we attempt to take advantage of parallelism, either by increasing mini-batch size or by increase the number of learners.

## item_id: m_2595

TITLE: Sufficient Context: A New Lens on Retrieval Augmented Generation Systems

ABSTRACT: Augmenting LLMs with context leads to improved performance across many applications. Despite much research on Retrieval Augmented Generation (RAG) systems, an open question is whether errors arise because LLMs fail to utilize the context from retrieval or the context itself is insufficient to answer the query. To shed light on this, we develop a new notion of sufficient context, along with a method to classify instances that have enough information to answer the query. We then use sufficient context to analyze several models and datasets. By stratifying errors based on context sufficiency, we find that larger models with higher baseline performance (Gemini 1.5 Pro, GPT 4o, Claude 3.5) excel at answering queries when the context is sufficient, but often output incorrect answers instead of abstaining when the context is not. On the other hand, smaller models with lower baseline performance (Llama 3.1, Mistral 3, Gemma 2) hallucinate or abstain often, even with sufficient context. We further categorize cases when the context is useful, and improves accuracy, even though it does not fully answer the query and the model errs without the context. Building on our findings, we explore ways to reduce hallucinations in RAG systems, including a new selective generation method that leverages sufficient context information for guided abstention. Our method improves the fraction of correct answers among times where the model responds by 2--10% for Gemini, GPT, and Gemma. Code for our selective generation method and the prompts used in our autorater analysis are available on our [github](https://github.com/hljoren/sufficientcontext).

## item_id: m_2596

TITLE: Equivariant Vector Field Network for Many-body System Modeling

ABSTRACT: Modeling many-body systems has been a long-standing challenge in science, from classical and quantum physics to computational biology. Equivariance is a critical physical symmetry for many-body dynamic systems, which enables robust and accurate prediction under arbitrary reference transformations. In light of this, great efforts have been put on encoding this symmetry into deep neural networks, which significantly boosts the prediction performance of down-streaming tasks. Some general equivariant models which are computationally efficient have been proposed, however, these models have no guarantee on the approximation power and may have information loss. In this paper, we leverage insights from the scalarization technique in differential geometry to model many-body systems by learning the gradient vector fields, which are SE(3) and permutation equivariant. Specifically, we propose the Equivariant Vector Field Network (EVFN), which is built on a novel tuple of equivariant basis and the associated scalarization and vectorization layers. Since our tuple equivariant basis forms a complete basis, learning the dynamics with our EVFN has no information loss. We evaluate our method on predicting trajectories of simulated Newton mechanics systems with both full and partially observed data, as well as the equilibrium state of small molecules (molecular conformation) evolving as a statistical mechanics system. Experimental results across multiple tasks demonstrate that our model achieves best or competitive performance on baseline models in various types of datasets.

## item_id: m_2597

TITLE: Deep Active Learning for Object Detection with Mixture Density Networks

ABSTRACT: Active learning aims to reduce the labeling costs by selecting only samples that are informative to improve the accuracy of the network. Few existing works have addressed the problem of active learning for object detection, and most of them estimate the informativeness of an image based only on the classification head, neglecting the influence of the localization head. In this paper, we propose a novel deep active learning approach for object detection. Our approach relies on mixture density networks to provide a mixture distribution for every output parameter. Based on these distributions, our approach is able to compute, separately and in a single forward pass of a single model, the epistemic and aleatoric uncertainty. We further propose a more efficient approach to reduce the computational cost of the mixture model. For active learning, we propose a scoring function that aggregates uncertainties from both the classification and the localization outputs of the network. Our extensive set of experiments on PASCAL VOC and COCO demonstrates that our modification to the object detection network yields better accuracy compared to the original one and, for active learning, our approach outperforms single-model based methods and performs on par when compared to methods using multiple models while requiring significantly lower computational cost. In addition, we show that our approach scales to different object detection networks and datasets acquired actively using our approach to transfer to different networks.

## item_id: m_2598

TITLE: MMD GAN with Random-Forest Kernels

ABSTRACT: In this paper, we propose a novel kind of kernel, random forest kernel, to enhance the empirical performance of MMD GAN. Different from common forests with deterministic routings, a probabilistic routing variant is used in our innovated random-forest kernel, which is possible to merge with the CNN frameworks. Our proposed random-forest kernel has the following advantages: From the perspective of random forest, the output of GAN discriminator can be viewed as feature inputs to the forest, where each tree gets access to merely a fraction of the features, and thus the entire forest benefits from ensemble learning. In the aspect of kernel method, random-forest kernel is proved to be characteristic, and therefore suitable for the MMD structure. Besides, being an asymmetric kernel, our random-forest kernel is much more flexible, in terms of capturing the differences between distributions. Sharing the advantages of CNN, kernel method, and ensemble learning, our random-forest kernel based MMD GAN obtains desirable empirical performances on CIFAR-10, CelebA and LSUN bedroom data sets. Furthermore, for the sake of completeness, we also put forward comprehensive theoretical analysis to support our experimental results.

## item_id: m_2599

TITLE: Streamlining EM into Auto-Encoder Networks

ABSTRACT: We present a new deep neural network architecture, named EDGaM, for deep clustering. This architecture can seamlessly learn deep auto-encoders and capture common group features of complex inputs in the encoded latent space. The key idea is to introduce a differentiable Gaussian mixture neural network between an encoder and a decoder. In particular, EDGaM streamlines the iterative Expectation-Maximum (EM) algorithm of the Gaussian mixture models into network design and replaces the alternative update with a forward-backward optimization. Being differentiable, both network weights and clustering centroids in EDGaM can be learned simultaneously in an end-to-end manner through standard stochastic gradient descent. To avoid preserving too many sample-specific details, we use both the clustering centroid and the original latent embedding for decoding. Meanwhile, we distill the soft clustering assignment for each sample via entropy minimization such that a clear cluster structure is exhibited. Our experiments show that our method outperforms state-of-the-art unsupervised clustering techniques in terms of both efficiency and clustering performance. 

## item_id: m_2600

TITLE: Aligning Artificial Neural Networks to the Brain yields Shallow Recurrent Architectures

ABSTRACT: Deep artificial neural networks with spatially repeated processing (a.k.a., deep convolutional ANNs) have been established as the best class of candidate models of visual processing in the primate ventral visual processing stream. Over the past five years, these ANNs have evolved from a simple feedforward eight-layer architecture in AlexNet to extremely deep and branching NASNet architectures, demonstrating increasingly better object categorization performance. Here we ask, as ANNs have continued to evolve in performance, are they also strong candidate models for the brain? To answer this question, we developed Brain-Score, a composite of neural and behavioral benchmarks for determining how brain-like a model is, together with an online platform where models can receive a Brain-Score and compare against other models. 
Despite high scores, typical deep models from the machine learning community are often hard to map onto the brain's anatomy due to their vast number of layers and missing biologically-important connections, such as recurrence. To further map onto anatomy and validate our approach, we built CORnet-S: an ANN guided by Brain-Score with the anatomical constraints of compactness and recurrence. Although a shallow model with four anatomically mapped areas and recurrent connectivity, CORnet-S is a top model on Brain-Score and outperforms similarly compact models on ImageNet. Analyzing CORnet-S circuitry variants revealed recurrence as the main predictive factor of both Brain-Score and ImageNet top-1 performance.

