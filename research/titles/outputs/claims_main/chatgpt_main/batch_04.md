# Batch 04 — 100 items

## item_id: m_0301

TITLE: Byte-Level Recursive Convolutional Auto-Encoder for Text

ABSTRACT: This article proposes to auto-encode text at byte-level using convolutional networks with a recursive architecture. The motivation is to explore whether it is possible to have scalable and homogeneous text generation at byte-level in a non-sequential fashion through the simple task of auto-encoding. We show that non-sequential text generation from a fixed-length representation is not only possible, but also achieved much better auto-encoding results than recurrent networks. The proposed model is a multi-stage deep convolutional encoder-decoder framework using residual connections, containing up to 160 parameterized layers. Each encoder or decoder contains a shared group of modules that consists of either pooling or upsampling layers, making the network recursive in terms of abstraction levels in representation. Results for 6 large-scale paragraph datasets are reported, in 3 languages including Arabic, Chinese and English. Analyses are conducted to study several properties of the proposed model.

## item_id: m_0302

TITLE: Feature-Wise Bias Amplification

ABSTRACT: We study the phenomenon of bias amplification in classifiers, wherein a machine learning model learns to predict classes with a greater disparity than the underlying ground truth. We demonstrate that bias amplification can arise via inductive bias in gradient descent methods resulting in overestimation of importance of moderately-predictive ``weak'' features if insufficient training data is available. This overestimation gives rise to feature-wise bias amplification -- a previously unreported form of bias that can be traced back to the features of a trained model. Through analysis and experiments, we show that the while some bias cannot be mitigated without sacrificing accuracy, feature-wise bias amplification can be mitigated through targeted feature selection. We present two new feature selection algorithms for mitigating bias amplification in linear models, and show how they can be adapted to convolutional neural networks efficiently. Our experiments on synthetic and real data demonstrate that these algorithms consistently lead to reduced bias without harming accuracy, in some cases eliminating predictive bias altogether while providing modest gains in accuracy.

## item_id: m_0303

TITLE: Coverage-centric Coreset Selection for High Pruning Rates

ABSTRACT: One-shot coreset selection aims to select a representative subset of the training data, given a pruning rate, that can later be used to train future models while retaining high accuracy. State-of-the-art coreset selection methods pick the highest importance examples based on an importance metric and are found to perform well at low pruning rates.  However, at high pruning rates, they suffer from a catastrophic accuracy drop, performing worse than even random sampling. This paper explores the reasons behind this accuracy drop both theoretically and empirically. We first propose a novel metric to measure the coverage of a dataset on a specific distribution by extending the classical geometric set cover problem to a distribution cover problem. This metric helps explain why coresets selected by SOTA methods at high pruning rates perform poorly compared to random sampling because of worse data coverage. We then propose a novel one-shot coreset selection method, Coverage-centric Coreset Selection (CCS), that jointly considers overall data coverage upon a distribution as well as the importance of each example. We evaluate CCS on five datasets and show that, at high pruning rates (e.g., 90%), it achieves significantly better accuracy than previous SOTA methods (e.g., at least 19.56% higher on CIFAR10) as well as random selection (e.g., 7.04% higher on CIFAR10) and comparable accuracy at low pruning rates.  We make our code publicly available at https://github.com/haizhongzheng/Coverage-centric-coreset-selection.

## item_id: m_0304

TITLE: Federated Learning with Partial Model Personalization

ABSTRACT: We propose and analyze a general framework of federated learning with  partial model personalization. Compared with full model personalization, partial model personalization relies on domain knowledge to select a small portion of the model to personalize, thus imposing a much smaller on-device memory footprint. We propose two federated optimization algorithms for training partially personalized models, where the shared and personal parameters are updated either simultaneously or alternately on each device, but only the shared parameters are communicated and aggregated at the server. We give convergence analyses of both algorithms for minimizing smooth nonconvex functions, providing theoretical support of them for training deep learning models. Our experiments on real-world image and text datasets demonstrate that (a) partial model personalization can obtain most of the benefit of full model personalization with a small fraction of personalized parameters, and, (b) the alternating update algorithm often outperforms the simultaneous update algorithm.

## item_id: m_0305

TITLE: How to Train your HIPPO: State Space Models with Generalized Orthogonal Basis Projections

ABSTRACT: Linear time-invariant state space models (SSM) are a classical model from engineering and statistics, that have recently been shown to be very promising in machine learning through the Structured State Space sequence model (S4). A core component of S4 involves initializing the SSM state matrix to a particular matrix called a HiPPO matrix, which was empirically important for S4's ability to handle long sequences. However, the specific matrix that S4 uses was actually derived in previous work for a particular *time-varying* dynamical system, and the use of this matrix as a *time-invariant* SSM had no known mathematical interpretation. Consequently, the theoretical mechanism by which S4 models long-range dependencies actually remains unexplained. We derive a more general and intuitive formulation of the HiPPO framework, which provides a simple mathematical interpretation of S4 as a decomposition onto exponentially-warped Legendre polynomials, explaining its ability to capture long dependencies. Our generalization introduces a theoretically rich class of SSMs that also lets us derive more intuitive S4 variants for other bases such as the Fourier basis, and explains other aspects of training S4, such as how to initialize the important timescale parameter. These insights improve S4's performance to 86% on the Long Range Arena benchmark, with 96% on the most difficult Path-X task.


## item_id: m_0306

TITLE: Deep Reasoning Networks:  Thinking Fast and Slow, for Pattern De-mixing

ABSTRACT: We introduce Deep Reasoning Networks (DRNets), an end-to-end framework that combines deep learning with reasoning for solving pattern de-mixing problems, typically in an unsupervised or weakly-supervised setting.  DRNets exploit problem structure and prior knowledge by tightly combining logic and constraint reasoning with stochastic-gradient-based neural network optimization.  We illustrate the power of DRNets on de-mixing overlapping hand-written Sudokus (Multi-MNIST-Sudoku) and on a substantially more complex task in scientific discovery that concerns inferring crystal structures of materials from X-ray diffraction data (Crystal-Structure-Phase-Mapping). DRNets significantly outperform the state of the art and experts' capabilities on Crystal-Structure-Phase-Mapping, recovering more precise and physically meaningful crystal structures. On Multi-MNIST-Sudoku, DRNets perfectly recovered the mixed Sudokus' digits, with 100% digit accuracy, outperforming the supervised state-of-the-art MNIST de-mixing models.

## item_id: m_0307

TITLE: Hard Masking for Explaining Graph Neural Networks

ABSTRACT: Graph Neural Networks (GNNs) are a flexible and powerful family of models that build nodes' representations on irregular graph-structured data. This paper focuses on explaining or interpreting the rationale underlying a given prediction of already trained graph neural networks for the node classification task. Existing approaches for interpreting GNNs try to find subsets of important features and nodes by learning a continuous mask. Our objective is to find discrete masks that are arguably more interpretable while minimizing the expected deviation from the underlying model's prediction. We empirically show that our explanations are both more predictive and sparse. Additionally, we find that multiple diverse explanations are possible, which sufficiently explain a prediction. Finally, we analyze the explanations to find the effect of network homophily on the decision-making process of GNNs.

## item_id: m_0308

TITLE: BLISS in Non-Isometric Embedding Spaces

ABSTRACT: Recent work on bilingual lexicon induction (BLI) has frequently depended either on aligned bilingual lexicons or on distribution matching, often with an assumption about the isometry of the two spaces. We propose a technique to quantitatively estimate this assumption of the isometry between two embedding spaces and  empirically show that this assumption weakens as the languages in question become increasingly etymologically distant. We then propose Bilingual Lexicon Induction with Semi-Supervision (BLISS) --- a novel semi-supervised approach that relaxes the isometric assumption while leveraging both limited aligned bilingual lexicons and a larger set of unaligned word embeddings, as well as a novel hubness filtering technique. Our proposed method improves over strong baselines for 11 of 14 on the MUSE dataset, particularly for languages whose embedding spaces do not appear to be isometric. In addition, we also show that adding supervision stabilizes the learning procedure, and is effective even with minimal supervision.

## item_id: m_0309

TITLE: Guide Actor-Critic for Continuous Control

ABSTRACT: Actor-critic methods solve reinforcement learning problems by updating a parameterized policy known as an actor in a direction that increases an estimate of the expected return known as a critic. However, existing actor-critic methods only use values or gradients of the critic to update the policy parameter. In this paper, we propose a novel actor-critic method called the guide actor-critic (GAC). GAC firstly learns a guide actor that locally maximizes the critic and then it updates the policy parameter based on the guide actor by supervised learning. Our main theoretical contributions are two folds. First, we show that GAC updates the guide actor by performing second-order optimization in the action space where the curvature matrix is based on the Hessians of the critic. Second, we show that the deterministic policy gradient method is a special case of GAC when the Hessians are ignored. Through experiments, we show that our method is a promising reinforcement learning method for continuous controls.


## item_id: m_0310

TITLE: Variational Diffusion Autoencoders with Random Walk Sampling

ABSTRACT: Variational inference (VI) methods and especially variational autoencoders (VAEs) specify scalable generative models that enjoy an intuitive connection to manifold learning --- with many default priors the posterior/likelihood pair $q(z|x)$/$p(x|z)$ can be viewed as an approximate homeomorphism (and its inverse) between the data manifold and a latent Euclidean space. However, these approximations are well-documented to become degenerate in training. Unless the subjective prior is carefully chosen, the topologies of the prior and data distributions often will not match.
Conversely, diffusion maps (DM) automatically \textit{infer} the data topology and enjoy a rigorous connection to manifold learning, but do not scale easily or provide the inverse homeomorphism.
In this paper, we propose \textbf{a)} a principled measure for recognizing the mismatch between data and latent distributions and \textbf{b)} a method that combines the advantages of variational inference and diffusion maps to learn a homeomorphic generative model. The measure, the \textit{locally bi-Lipschitz property}, is a sufficient condition for a homeomorphism and easy to compute and interpret. The method, the \textit{variational diffusion autoencoder} (VDAE), is a novel generative algorithm that first infers the topology of the data distribution, then models a diffusion random walk over the data. To achieve efficient computation in VDAEs, we use stochastic versions of both variational inference and manifold learning optimization. We prove approximation theoretic results for the dimension dependence of VDAEs, and that locally isotropic sampling in the latent space results in a random walk over the reconstructed manifold.
Finally, we demonstrate the utility of our method on various real and synthetic datasets, and show that it exhibits performance superior to other generative models.

## item_id: m_0311

TITLE: When Distance Distracts: Representation Distance Bias in BT-Loss for Reward Models

ABSTRACT: Reward models are central to Large Language Model (LLM) alignment within the framework of RLHF. The standard objective used in reward modeling is the Bradley-Terry (BT) loss, which learns from pairwise data consisting of a pair of chosen and rejected responses. In this work, we analyze the per-sample gradient of BT-loss and show that its norm scales with two distinct components: (1) the difference in predicted rewards between chosen and rejected responses, which reflects the prediction error, and critically, (2) representation distance between the pair measured in the output space of the final layer. While the first term captures the intended training signal, we show that the second term can significantly impact the update magnitude and misalign learning. Specifically, pairs with small representation distance often receive vanishingly weak updates, even when misranked, while pairs with large distance receive disproportionately strong updates. This leads to gradients from large-distance pairs to overshadow those from small-distance pairs, where fine-grained distinctions are especially important. To overcome this limitation, we propose NormBT, an adaptive pair-wise normalization scheme that balances representation-driven effects and focuses learning signals on prediction error. NormBT is a lightweight, drop-in integration to BT loss with negligible overhead. Across various LLM backbones and datasets, NormBT improves reward model performance consistently, with notable gains of over 5% on the Reasoning category of RewardBench, which contains numerous small-distance pairs. This work reveals a key limitation in the widely used BT objective and provides a simple, effective correction.

## item_id: m_0312

TITLE: Deep RL for Blood Glucose Control: Lessons, Challenges, and Opportunities

ABSTRACT: Individuals with type 1 diabetes (T1D) lack the ability to produce the insulin their bodies need. As a result, they must continually make decisions about how much insulin to self-administer in order to adequately control their blood glucose levels. Longitudinal data streams captured from wearables, like continuous glucose monitors, can help these individuals manage their health, but currently the majority of the decision burden remains on the user. To relieve this burden, researchers are working on closed-loop solutions that combine a continuous glucose monitor and an insulin pump with a control algorithm in an `artificial pancreas.' Such systems aim to estimate and deliver the appropriate amount of insulin. Here, we develop reinforcement learning (RL) techniques for automated blood glucose control. Through a series of experiments, we compare the performance of different deep RL approaches to non-RL approaches. We highlight the flexibility of RL approaches, demonstrating how they can adapt to new individuals with little additional data. On over 21k hours of simulated data across 30 patients, RL approaches outperform baseline control algorithms (increasing time spent in normal glucose range from 71% to 75%) without requiring meal announcements. Moreover, these approaches are adept at leveraging latent behavioral patterns (increasing time in range from 58% to 70%). This work demonstrates the potential of deep RL for controlling complex physiological systems with minimal expert knowledge. 

## item_id: m_0313

TITLE: Generating Videos with Dynamics-aware Implicit Generative Adversarial Networks

ABSTRACT: In the deep learning era, long video generation of high-quality still remains challenging due to the spatio-temporal complexity and continuity of videos. Existing prior works have attempted to model video distribution by representing videos as 3D grids of RGB values, which impedes the scale of generated videos and neglects continuous dynamics. In this paper, we found that the recent emerging paradigm of implicit neural representations (INRs) that encodes a continuous signal into a parameterized neural network effectively mitigates the issue. By utilizing INRs of video, we propose dynamics-aware implicit generative adversarial network (DIGAN), a novel generative adversarial network for video generation. Specifically, we introduce (a) an INR-based video generator that improves the motion dynamics by manipulating the space and time coordinates differently and (b) a motion discriminator that efficiently identifies the unnatural motions without observing the entire long frame sequences. We demonstrate the superiority of DIGAN under various datasets, along with multiple intriguing properties, e.g., long video synthesis, video extrapolation, and non-autoregressive video generation. For example, DIGAN improves the previous state-of-the-art FVD score on UCF-101 by 30.7% and can be trained on 128 frame videos of 128x128 resolution, 80 frames longer than the 48 frames of the previous state-of-the-art method.

## item_id: m_0314

TITLE: Physiological Signal Embeddings (PHASE) via Interpretable Stacked Models

ABSTRACT: In health, machine learning is increasingly common, yet neural network embedding (representation) learning is arguably under-utilized for physiological signals.  This inadequacy stands out in stark contrast to more traditional computer science domains, such as computer vision (CV), and natural language processing (NLP).  For physiological signals, learning feature embeddings is a natural solution to data insufficiency caused by patient privacy concerns -- rather than share data, researchers may share informative embedding models (i.e., representation models), which map patient data to an output embedding.   Here, we present the PHASE (PHysiologicAl Signal Embeddings) framework, which consists of three components: i) learning neural network embeddings of physiological signals, ii) predicting outcomes based on the learned embedding, and iii) interpreting the prediction results by estimating feature attributions in the "stacked" models (i.e., feature embedding model followed by prediction model).  PHASE is novel in three ways: 1) To our knowledge, PHASE is the first instance of transferal of neural networks to create physiological signal embeddings. 2) We present a tractable method to obtain feature attributions through stacked models.  We prove that our stacked model attributions can approximate Shapley values -- attributions known to have desirable properties -- for arbitrary sets of models. 3) PHASE was extensively tested in a cross-hospital setting including publicly available data.  In our experiments, we show that PHASE significantly outperforms alternative embeddings -- such as raw, exponential moving average/variance, and autoencoder -- currently in use. Furthermore, we provide evidence that transferring neural network embedding/representation learners between distinct hospitals still yields performant embeddings and offer recommendations when transference is ineffective.

## item_id: m_0315

TITLE: Exploring Routing Strategies for Multilingual Mixture-of-Experts Models

ABSTRACT: Sparsely-Gated Mixture-of-Experts (MoE) has been a successful approach for scaling multilingual translation models to billions of parameters without a proportional increase in training computation. These models, however, are prohibitively large for serving deployment and there is no easy way to extract a sub-network to decode for a particular language pair. This work proposes improved strategies to route MoE models by tasks instead of tokens, thus enabling separation of network structures at decoding time while enjoying the benefits of scale and task sharing at training time.
We compare routing strategies at multiple levels (token, sentence, task) in both, the encoder and the decoder, and conduct extensive experiments on two benchmarks: the public WMT dataset of 30 language pairs and an in-house web-scale dataset of 200 language pairs. On WMT, with a Transformer base model with 32 experts, our task-level MoE outperforms the best performing token-level MoE model by +1.0 BLEU on average over all language pairs. When scaling up to Transformer big model with 128 experts on the large-scale massively multilingual benchmark, our task-level MoE is competitive with token-level MoE while being able to reduce the decoder model size by a factor of $32.34$ and increase peak throughput by 2.6 times at inference.

## item_id: m_0316

TITLE: Bayesian Prediction of Future Street Scenes using Synthetic Likelihoods

ABSTRACT: For autonomous agents to successfully operate in the real world, the ability to anticipate future scene states is a key competence. In real-world scenarios, future states become increasingly uncertain and multi-modal, particularly on long time horizons. Dropout based Bayesian inference provides a computationally tractable, theoretically well grounded approach to learn different hypotheses/models to deal with uncertain futures and make predictions that correspond well to observations -- are well calibrated. However, it turns out that such approaches fall short to capture complex real-world scenes, even falling behind in accuracy when compared to the plain deterministic approaches. This is because the used log-likelihood estimate discourages diversity. In this work, we propose a novel Bayesian formulation for anticipating future scene states which leverages synthetic likelihoods that encourage the learning of diverse models to accurately capture the multi-modal nature of future scene states. We show that our approach achieves accurate state-of-the-art predictions and calibrated probabilities through extensive experiments for scene anticipation on Cityscapes dataset. Moreover, we show that our approach generalizes across diverse tasks such as digit generation and precipitation forecasting.

## item_id: m_0317

TITLE: Safe Neurosymbolic Learning with Differentiable Symbolic Execution

ABSTRACT: We study the problem of learning verifiably safe parameters for programs that use neural networks as well as symbolic, human-written code. Such neurosymbolic programs arise in many safety-critical domains. However, because they need not be differentiable, it is hard to learn their parameters using existing gradient-based approaches to safe learning. Our method, Differentiable Symbolic Execution (DSE), samples control flow paths in a program, symbolically constructs worst-case "safety loss" along these paths, and backpropagates the gradients of these losses through program operations using a generalization of the REINFORCE estimator. We evaluate the method on a mix of synthetic tasks and real-world benchmarks. Our experiments show that DSE significantly outperforms the state-of-the-art DiffAI method on these tasks.  

## item_id: m_0318

TITLE: Classification in the dark using tactile exploration

ABSTRACT: Combining information from different sensory modalities to execute goal directed actions is a key aspect of human intelligence. Specifically, human agents are very easily able to translate the task communicated in one sensory domain (say vision) into a representation that enables them to complete this task when they can only sense their environment using a separate sensory modality (say touch). In order to build agents with similar capabilities, in this work we consider the problem of a retrieving a target object from a drawer. The agent is provided with an image of a previously unseen object and it explores objects in the drawer using only tactile sensing to retrieve the object that was shown in the image without receiving any visual feedback. Success at this task requires close integration of visual and tactile sensing. We present a method for performing this task in a simulated environment using an anthropomorphic hand. We hope that future research in the direction of combining sensory signals for acting will find the object retrieval from a drawer to be a useful benchmark problem

## item_id: m_0319

TITLE: DIFUSCO-LNS: Diffusion-Guided Large Neighbourhood Search for Integer Linear Programming

ABSTRACT: Integer Linear Programming (ILP) is a powerful and flexible framework for modeling and solving a variety of combinatorial optimization problems. This paper introduces a novel ILP solver, namely DIFUSCO-LNS, which combines the strengths of carefully engineered traditional solvers in symbolic reasoning and the generative power of a neural diffusion model in graph-based learning for the Large Neighborhood Search (LNS) approach. Our diffusion model treats the destroy policy in LNS as a generative problem in the discrete $\{0, 1\}$-vector space and is trained to imitate the high-quality Local Branching (LB) destroy heuristic through iterative denoising. Specifically, this addresses the unimodal limitation of other neural LNS solvers with its capability to capture the multimodal nature of optimal policies during variable selection.  Our evaluations span four representative MIP problems: MIS, CA, SC, and MVC. Experimental results reveal that DIFUSCO-LNS substantially surpasses prior neural LNS  solvers.

## item_id: m_0320

TITLE: A Sublinear Adversarial Training Algorithm

ABSTRACT: Adversarial training is a widely used strategy for making neural networks resistant to adversarial perturbations. For a neural network of width $m$, $n$ input training data in $d$ dimension, it takes $\Omega(mnd)$ time cost per training iteration for the forward and backward computation. In this paper we analyze the convergence guarantee of adversarial training procedure on a two-layer neural network with shifted ReLU activation, and shows that only $o(m)$ neurons will be activated for each input data per iteration. Furthermore, we develop an algorithm for adversarial training with time cost $o(m n d)$ per iteration by applying half-space reporting data structure.

## item_id: m_0321

TITLE: Uncertainty Sets for Image Classifiers using Conformal Prediction

ABSTRACT: Convolutional image classifiers can achieve high predictive accuracy, but quantifying their uncertainty remains an unresolved challenge, hindering their deployment in consequential settings. Existing uncertainty quantification techniques, such as Platt scaling, attempt to calibrate the network’s probability estimates, but they do not have formal guarantees. We present an algorithm that modifies any classifier to output a predictive set containing the true label with a user-specified probability, such as 90%. The algorithm is simple and fast like Platt scaling, but provides a formal finite-sample coverage guarantee for every model and dataset. Our method modifies an existing conformal prediction algorithm to give more stable predictive sets by regularizing the small scores of unlikely classes after Platt scaling. In experiments on both Imagenet and Imagenet-V2 with ResNet-152 and other classifiers, our scheme outperforms existing approaches, achieving coverage with sets that are often factors of 5 to 10 smaller than a stand-alone Platt scaling baseline.

## item_id: m_0322

TITLE: DisTop: Discovering a Topological representation to learn diverse and rewarding skills

ABSTRACT: An efficient way for a deep reinforcement learning agent to explore can be to learn a set of skills that achieves a uniform distribution of terminal states. Following this, we introduce DisTop, a new model that simultaneously learns diverse skills and focuses on improving rewarding skills. DisTop progressively builds a discrete topology of the environment using an unsupervised contrastive loss, a growing network and a goal-conditioned policy. Using this topology, a state-independent hierarchical policy can select where the agent has to keep discovering skills in the state space. In turn, the new set of visited states allows an improved learnt representation. If the agent gets overloaded by the number of skills, the agent can autonomously forget the skills unrelated to its eventual task.  Our experiments emphasize that DisTop is agnostic to the ground state representation and that the agent can discover the topology of its environment whether the states are high-dimensional binary data, images, or proprioceptive inputs. We demonstrate that this paradigm is competitive on MuJoCo benchmarks with state-of-the-art algorithms on both single-task dense rewards and diverse skill discovery without rewards. By combining these two aspects, we show that DisTop outperforms a state-of-the-art hierarchical reinforcement learning algorithm when rewards are sparse. We believe DisTop opens new perspectives by showing that bottom-up skill discovery combined with representation learning can tackle different complex state spaces and reward settings when it is endowed with the ability to explicitly select the skills to improve.

## item_id: m_0323

TITLE: IgSeek: Fast and Accurate Antibody Design via Structure Retrieval

ABSTRACT: Recent advancements in protein design have leveraged diffusion models to generate structural scaffolds, followed by a process known as protein inverse folding, which involves sequence inference on these scaffolds. However, these methodologies face significant challenges when applied to hyper-variable structures such as antibody Complementarity-Determining Regions (CDRs), where sequence inference frequently results in non-functional sequences due to hallucinations. Distinguished from prevailing protein inverse folding approaches, this paper introduces IgSeek, a novel structure-retrieval framework that infers CDR sequences by retrieving similar structures from a natural antibody database. Specifically, IgSeek employs a simple yet effective multi-channel equivariant graph neural network to generate high-quality geometric representations of CDR backbone structures. Subsequently, it aligns sequences of structurally similar CDRs and utilizes structurally conserved sequence motifs to enhance inference accuracy. Our experiments demonstrate that IgSeek not only proves to be highly efficient in structural retrieval but also outperforms state-of-the-art approaches in sequence recovery for both antibodies and T-Cell Receptors, offering a new retrieval-based perspective for therapeutic protein design.

## item_id: m_0324

TITLE: GraphGAN: Generating Graphs via Random Walks

ABSTRACT: We propose GraphGAN - the first implicit generative model for graphs that enables to mimic real-world networks.
We pose the problem of graph generation as learning the distribution of biased random walks over a single input graph.
Our model is based on a stochastic neural network that generates discrete output samples, and is trained using the Wasserstein GAN objective. GraphGAN enables us to generate sibling graphs, which have similar properties yet are not exact replicas of the original graph. Moreover, GraphGAN learns a semantic mapping from the latent input space to the generated graph's properties. We discover that sampling from certain regions of the latent space leads to varying properties of the output graphs, with smooth transitions between them. Strong generalization properties of GraphGAN are highlighted by its competitive performance in link prediction as well as promising results on node classification, even though not specifically trained for these tasks.

## item_id: m_0325

TITLE: Spectral Annealing for Scalable Ising Model Optimization

ABSTRACT: Large-scale Ising optimization underlies critical optimization and learning applications, including correlation clustering, MAP inference, and energy-based models. Existing methods face a fundamental efficiency-quality tradeoff: spectral relaxations achieve polynomial-time complexity but deliver approximate solutions with significant optimality gaps, while metaheuristics approach optimal solutions but scale poorly to large instances. The core limitation of spectral methods is their single-shot nature—they solve exactly one eigenvalue problem, providing no solution exploration and exhibiting acute sensitivity to normalization choices.
We introduce *spectral annealing* (SpecAnn), a new spectral paradigm that transforms spectral methods from single-shot approximations into systematic exploration-based optimization, annealing from the raw adjacency to full signed Laplacian normalization. We propose a *diagonal predictor* that exploits the algebraic structure of this continuation path for efficient traversal and an efficient *batched solution refinement*, leveraging massive parallelism from GPU-acceleration. Experiments on problems up to 8.4 million variables demonstrate that SpecAnn achieves near-optimal solutions with runtimes of 1--57 seconds, bridging fast but inaccurate spectral methods and slow but high-quality metaheuristics. SpecAnn delivers 83$\times$ speedup over recent GPU-accelerated methods while maintaining superior solution quality, and scales successfully beyond 262K variables where traditional metaheuristics fail.

## item_id: m_0326

TITLE: Zero-shot Cross-lingual Conversational Semantic Role Labeling

ABSTRACT: While conversational semantic role labeling (CSRL) has shown its usefulness on Chinese conversational tasks, it is still under-explored in non-Chinese languages due to the lack of multilingual CSRL annotations for the parser training. To avoid expensive data collection and error-propagation of translation-based methods, we present a simple but effective approach to perform zero-shot cross-lingual CSRL. Our model implicitly learns language-agnostic, conversational structure-aware and semantically rich representations with the hierarchical encoders and elaborately designed pre-training objectives. Through comprehensive experiments, we find that, our cross-lingual model not only outperforms baselines by large margins but it is also robust to low-resource scenarios. More impressively, we attempt to use CSRL information to help downstream English conversational tasks, including question-in-context rewriting and multi-turn dialogue response generation. Although we have obtained competitive performance on these tasks without CSRL information, substantial improvements are further achieved after introducing CSRL information, which indicates the effectiveness of our cross-lingual CSRL model and the usefulness of CSRL to English dialogue tasks.

## item_id: m_0327

TITLE: On Solving Minimax Optimization Locally: A Follow-the-Ridge Approach

ABSTRACT: Many tasks in modern machine learning can be formulated as finding equilibria in sequential games. In particular, two-player zero-sum sequential games, also known as minimax optimization, have received growing interest. It is tempting to apply gradient descent to solve minimax optimization given its popularity and success in supervised learning. However, it has been noted that naive application of gradient descent fails to find some local minimax and can converge to non-local-minimax points. In this paper, we propose Follow-the-Ridge (FR), a novel algorithm that provably converges to and only converges to local minimax. We show theoretically that the algorithm addresses the notorious rotational behaviour of gradient dynamics, and is compatible with preconditioning and positive momentum. Empirically, FR solves toy minimax problems and improves the convergence of GAN training compared to the recent minimax optimization algorithms. 

## item_id: m_0328

TITLE: Introspection:Accelerating Neural Network Training By Learning Weight Evolution

ABSTRACT: Neural Networks are function approximators that have achieved state-of-the-art accuracy in numerous machine learning tasks. In spite of their great success in terms of accuracy, their large training time makes it difficult to use them for various tasks. In this paper, we explore the idea of learning weight evolution pattern from a simple network for accelerating training of novel neural networks.

We use a neural network to learn the training pattern from MNIST classification and utilize it to accelerate training of neural networks used for CIFAR-10 and ImageNet classification. Our method has a low memory footprint and is computationally efficient. This method can also be used with other optimizers to give faster convergence. The results indicate a general trend in the weight evolution during training of neural networks.

## item_id: m_0329

TITLE: Generalizing and Tensorizing Subgraph Search in the Supernet

ABSTRACT: Recently, a special kind of graph, i.e., supernet, which allows two nodes connected by multi-choice edges, has exhibited its power in neural architecture search (NAS) by searching better architectures for computer vision (CV) and natural language processing (NLP) tasks. In this paper, we discover that the design of such discrete architectures also appears in many other important learning tasks, e.g., logical chain inference in knowledge graphs (KGs) and meta-path discovery in heterogeneous information networks (HINs). Thus, we are motivated to generalize the supernet search problem on a broader horizon. However, none of the existing works are effective since the supernet's topology is highly task-dependent and diverse. To address this issue, we propose to tensorize the supernet, i.e. unify the subgraph search problems by a tensor formulation and encode the topology inside the supernet by a tensor network. We further propose an efficient algorithm that admits both stochastic and deterministic objectives to solve the search problem. Finally, we perform extensive experiments on diverse learning tasks, i.e., architecture design for CV, logic inference for KG, and meta-path discovery for HIN. Empirical results demonstrate that our method leads to better performance and architectures.


## item_id: m_0330

TITLE: Deepström Networks

ABSTRACT: Recent work has focused on combining kernel methods and deep learning. With this in mind, we introduce Deepström networks -- a new architecture of neural networks which we use to replace top dense layers of standard convolutional architectures with an approximation of a kernel function by relying on the Nyström approximation. 
Our approach is easy highly flexible. It is compatible with any kernel function and it allows exploiting multiple kernels. 
We show that Deepström networks reach state-of-the-art performance on standard datasets like SVHN and CIFAR100. One benefit of the method lies in its limited number of learnable parameters which make it particularly suited for small training set sizes, e.g. from 5 to 20 samples per class. Finally we illustrate two ways of using multiple kernels, including a multiple Deepström  setting, that exploits a kernel on each feature map output by the convolutional part of the model.    

## item_id: m_0331

TITLE: FRAPPE: Fast RAG-Inspired Prompt Evaporator

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable performance in various tasks such as multi-document QA, summarization, and text classification. This has been achieved in part by recent advancements in prompt engineering and in-context learning (ICL), enabling LLMs to consume tens of thousands of input tokens as the supported context for the given query. However, this creates higher computational costs, longer latency, and potential performance degradation. To address these issues, we propose a task-agnostic and efficient approach called “Fast RAG Inspired Prompt Evaporator”, or FRAPPE, to significantly reduce LLMs’ latency, memory requirement, and computation by compressing input tokens. Unlike many other proposed approaches for prompt compression, our method does not rely on any large model for computing conditional probabilities, and data preparation is fast with negligible memory requirements. In particular, our approach first pre-processes the input data, categorizes and ranks phrases based on their informativeness, and finally selects the highest-ranked phrases to generate highly compressed and extractive input. We show the efficacy of our approach through a comprehensive set of experiments on public datasets and benchmarks. For instance, on the summarization task of the MeetingBank dataset, at a compression rate of 70%, our proposed approach achieves performance similar to the full context while performing compression up to 4 times faster than the contemporary state of the art compression algorithms.  We extend FRAPPE to create the Context-Aware FRAPPE algorithm, which incorporates task-specific information when ranking phrases, which further improves performance of downstream tasks using compressed text.  Additionally, we demonstrate that the use of FRAPPE can reduce toxicity by close to 50% relative to the original text by removing extraneous vitriolic phrases, in contrast to other compression methods, which often increase toxicity.

## item_id: m_0332

TITLE: Probabilistic Knowledge Graph Embeddings

ABSTRACT: We develop a probabilistic extension of state-of-the-art embedding models for link prediction in relational knowledge graphs. Knowledge graphs are collections of relational facts, where each fact states that a certain relation holds between two entities, such as people, places, or objects. We argue that knowledge graphs should be treated within a Bayesian framework because even large knowledge graphs typically contain only few facts per entity, leading effectively to a small data problem where parameter uncertainty matters. We introduce a probabilistic reinterpretation of the DistMult (Yang et al., 2015) and ComplEx (Trouillon et al., 2016) models and employ variational inference to estimate a lower bound on the marginal likelihood of the data. We find that the main benefit of the Bayesian approach is that it allows for efficient, gradient based optimization over hyperparameters, which would lead to divergences in a non-Bayesian treatment. Models with such learned hyperparameters improve over the state-of-the-art by a significant margin, as we demonstrate on several benchmarks.

## item_id: m_0333

TITLE: SWE-bench: Can Language Models Resolve Real-world Github Issues?

ABSTRACT: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories. Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks. Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model SWE-Llama can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous.

## item_id: m_0334

TITLE: Nonparametrically Learning Activation Functions in Deep Neural Nets

ABSTRACT: We provide a principled framework for nonparametrically learning activation functions in deep neural networks. Currently, state-of-the-art deep networks treat choice of activation function as a hyper-parameter before training. By allowing activation functions to be estimated as part of the training procedure, we expand the class of functions that each node in the network can learn. We also provide a theoretical justification for our choice of nonparametric activation functions and demonstrate that networks with our nonparametric activation functions generalize well. To demonstrate the power of our novel techniques, we test them on image recognition datasets and achieve up to a 15% relative increase in test performance compared to the baseline.

## item_id: m_0335

TITLE: Low-rank passthrough neural networks

ABSTRACT: Deep learning consists in training neural networks to perform computations that sequentially unfold in many steps over a time dimension or an intrinsic depth dimension. For large depths, this is usually accomplished by specialized network architectures that are designed to mitigate the vanishing gradient problem, e.g. LSTMs, GRUs, Highway Networks and Deep Residual Networks, which are based on a single structural principle: the state passthrough. We observe that these "Passthrough Networks" architectures enable the decoupling of the network state size from the number of parameters of the network, a possibility that is exploited in some recent works but not thoroughly explored. In this work we propose simple, yet effective, low-rank and low-rank plus diagonal matrix parametrizations for Passthrough Networks which exploit this decoupling property, reducing the data complexity and memory requirements of the network while preserving its memory capacity. We present competitive experimental results on several tasks, including a near state of the art result on sequential randomly-permuted MNIST classification, a hard task on natural data.

## item_id: m_0336

TITLE: Robustness of Classifiers to Universal Perturbations: A Geometric Perspective

ABSTRACT: Deep networks have recently been shown to be vulnerable to universal perturbations: there exist very small image-agnostic perturbations that cause most natural images to be misclassified by such classifiers. In this paper, we provide a quantitative analysis of the robustness of classifiers to universal perturbations, and draw a formal link between the robustness to universal perturbations, and the geometry of the decision boundary. Specifically, we establish theoretical bounds on the robustness of classifiers under two decision boundary models (flat and curved models). We show in particular that the robustness of deep networks to universal perturbations is driven by a key property of their curvature: there exist shared directions along which the decision boundary of deep networks is systematically positively curved. Under such conditions, we prove the existence of small universal perturbations. Our analysis further provides a novel geometric method for computing universal perturbations, in addition to explaining their properties.

## item_id: m_0337

TITLE: Neural Parameter Allocation Search

ABSTRACT: Training neural networks requires increasing amounts of memory. Parameter sharing can reduce memory and communication costs, but existing methods assume networks have many identical layers and utilize hand-crafted sharing strategies that fail to generalize. We introduce Neural Parameter Allocation Search (NPAS), a novel task where the goal is to train a neural network given an arbitrary, fixed parameter budget. NPAS covers both low-budget regimes, which produce compact networks, as well as a novel high-budget regime, where additional capacity can be added to boost performance without increasing inference FLOPs.  To address NPAS, we introduce Shapeshifter Networks (SSNs), which automatically learn where and how to share parameters in a network to support any parameter budget without requiring any changes to the architecture or loss function. NPAS and SSNs provide a complete framework for addressing generalized parameter sharing, and can also be combined with prior work for additional performance gains. We demonstrate the effectiveness of our approach using nine network architectures across four diverse tasks, including ImageNet classification and transformers.

## item_id: m_0338

TITLE: Advancing Spatiotemporal Representations in Spiking Neural Networks via Parametric Invertible Transformation

ABSTRACT: Spiking Neural Networks (SNNs) are regarded as energy-efficient neural architectures due to their event-driven, spike-based computation paradigm. However, existing SNNs suffer from two fundamental limitations: (1) the constrained representational space imposed by binary spike firing mechanisms, which restricts the network's capacity to encode complex spatiotemporal patterns, and (2) the ineffective design of surrogate gradient functions that leads to gradient mismatch issues and suboptimal learning dynamics. To address these challenges, we propose the Parametric Invertible Transformation (PIT), which operates in a conjugate manner with neuronal dynamics to achieve adaptive modulation and augmented spike representations simultaneously. Second, we design an auxiliary gradient correction term to mitigate the gradient mismatch issue and oscillation phenomena during training. Moreover, we introduce a theoretical framework for analyzing the spatiotemporal representation space of SNNs. Extensive experiments on both static and neuromorphic datasets demonstrate state-of-the-art performance with our proposed method. This approach lays the theoretical foundation for expanding the spatiotemporal representations of SNNs, offering a viable pathway for developing low-latency and high-performance neuromorphic processing systems in resource-constrained environments. The code is available at https://github.com/YinsongYan/ICLR26.

## item_id: m_0339

TITLE: Meta Auxiliary Labels with Constituent-based Transformer for Aspect-based Sentiment Analysis

ABSTRACT: Aspect based sentiment analysis (ABSA) is a challenging natural language processing task that could benefit from syntactic information. Previous work exploit dependency parses to improve performance on the task, but this requires the existence of good dependency parsers.  In this paper, we build a constituent-based transformer for ABSA that can induce constituents without constituent parsers. We also apply meta auxiliary learning to generate labels on edges between tokens, supervised by the objective of the ABSA task.  Without input from dependency parsers, our models outperform previous work on three Twitter data sets and match previous work closely on two review data sets.

## item_id: m_0340

TITLE: Deep Evolutionary Learning for Molecular Design

ABSTRACT: In this paper, we propose a deep evolutionary learning (DEL) process that integrates  fragment-based deep generative model and multi-objective evolutionary computation for molecular design. Our approach enables (1) evolutionary operations in the latent space of the generative model, rather than the structural space, to generate novel promising molecular structures for the next evolutionary generation, and (2) generative model fine-tuning using newly generated high-quality samples. Thus, DEL implements a data-model co-evolution concept which improves both sample population and generative model learning. Experiments on two public datasets indicate that sample population obtained by DEL exhibits improved property distributions, and dominates samples generated by multi-objective Bayesian optimization algorithms.

## item_id: m_0341

TITLE: Improving classifier decision boundaries using nearest neighbors

ABSTRACT: In this paper, we show that neural networks are not learning optimal decision boundaries. Decision boundaries go through areas of low training data density. They are impacted by few training samples which can easily lead to overfitting. We show that performing a weighted average of the prediction of a sample and its nearest neighbors' (computed in latent space) leads to a variety of minor favorable outcomes. In our evaluation, we employ various self-trained and pre-trained convolutional neural networks to show that our approach improves (i) resistance to label noise,  (ii) robustness against adversarial attacks, (iii) classification accuracy, and to some degree even (iv) interpretability. While improvements are not necessarily large in all four areas, our approach is conceptually simple, i.e., improvements come without any modification to network architecture, training procedure or dataset. Furthermore, they are in stark contrast to prior works that often require trade-offs among the four objectives or provides only non-actionable insights.

## item_id: m_0342

TITLE: Learning Temporally-Consistent Representations for Data-Efficient Reinforcement Learning

ABSTRACT: Deep reinforcement learning (RL) agents that exist in high-dimensional state spaces, such as those composed of images, have interconnected learning burdens. Agents must learn an action-selection policy that completes their given task, which requires them to learn a representation of the state space that discerns between useful and useless information. The reward function is the only supervised feedback that RL agents receive, which causes a representation learning bottleneck that can manifest in poor sample efficiency. We present $k$-Step Latent (KSL), a new representation learning method that enforces temporal consistency of representations via a self-supervised auxiliary task wherein agents learn to recurrently predict action-conditioned representations of the state space. The state encoder learned by KSL produces low-dimensional representations that make optimization of the RL task more sample efficient. Altogether, KSL produces state-of-the-art results in both data efficiency and asymptotic performance in the popular PlaNet benchmark suite. Our analyses show that KSL produces encoders that generalize better to new tasks unseen during training, and its representations are more strongly tied to reward, are more invariant to perturbations in the state space, and move more smoothly through the temporal axis of the RL problem than other methods such as DrQ, RAD, CURL, and SAC-AE.

## item_id: m_0343

TITLE: Conditional Expectation based Value Decomposition for Scalable On-Demand Ride Pooling

ABSTRACT: Owing to the benefits for customers (lower prices), drivers (higher revenues), aggregation companies (higher revenues) and the environment (fewer vehicles), on-demand ride pooling (e.g., Uber pool, Grab Share) has become quite popular. The significant computational complexity of matching vehicles to combinations of requests has meant that traditional ride pooling approaches are myopic in that they do not consider the impact of current matches on future value for vehicles/drivers.

Recently, Neural Approximate Dynamic Programming (NeurADP) has employed value decomposition with Approximate Dynamic Programming (ADP) to outperform leading approaches by considering the impact of an individual agent's (vehicle) chosen actions on the future value of that agent. However, in order to ensure scalability and facilitate city-scale ride pooling, NeurADP  completely ignores the impact of other agents actions on individual agent/vehicle value. As demonstrated in our experimental results, ignoring the impact of other agents actions on individual value can have a significant impact on the overall performance when there is increased competition among vehicles for demand. Our key contribution is a novel mechanism based on computing conditional expectations through joint conditional probabilities for capturing dependencies on other agents actions without increasing the complexity of training or decision making. We show that our new approach, Conditional Expectation based Value Decomposition (CEVD) outperforms NeurADP by up to 9.76$\% $in terms of overall requests served, which is a significant improvement on a city wide benchmark taxi dataset. 

## item_id: m_0344

TITLE: Video Deblurring with Adaptive High-frequency Extraction

ABSTRACT: State-of-the-art video deblurring methods use deep network architectures to recover sharpened video frames. Blurring especially degrades high-frequency information yet this aspect is often overlooked by recent models that focus more on enhancing architectural design. The recovery of high frequency detailing can be non-trivial, in part due to the spectral bias of neural networks. Neural networks are biased towards learning low frequency functions, making it to prioritize learning low frequency components. To enhance the learning of latent high frequencies, it is necessary to enforce explicit structures to capture the fine details or edges. This work merges the principles of the classic unsharp masking with a deep learning framework to emphasize the essential role of high-frequency information in deblurring. We generate an adaptive kernel, constructed from a convex combination of dynamic coefficients and predefined high-pass filtering kernels. This kernel is then employed in a spatio-temporal 3D convolution process to extract high-frequency components from the data. This method significantly improves video deblurring, achieving a noteworthy enhancement with an increase of up to 0.61dB in PSNR over top models on GORPO dataset. Additionally, it outpaces the majority of them in inference time.

## item_id: m_0345

TITLE: Igeood: An Information Geometry Approach to Out-of-Distribution Detection

ABSTRACT: Reliable out-of-distribution (OOD) detection is fundamental to implementing safer modern machine learning (ML)  systems. In this paper, we introduce Igeood, an effective method for detecting OOD samples. Igeood applies to any pre-trained neural network, works under various degrees of access to the ML model, does not require OOD samples or assumptions on the OOD data but can also benefit (if available) from OOD samples. By building on the geodesic (Fisher-Rao) distance between the underlying data distributions, our discriminator can combine confidence scores from the logits outputs and the learned features of a deep neural network. Empirically, we show that Igeood outperforms competing state-of-the-art methods on a variety of network architectures and datasets.

## item_id: m_0346

TITLE: Point Cloud Completion with Landau Distribution: A Probabilistic View

ABSTRACT: Point clouds are fundamental discrete representations used in computer vision, robotics, etc. Chamfer Distance (CD) is widely adopted as a metric and training loss to evaluate the similarity between two point clouds. However, the vanilla CD is sensitive to outliers, which means a few widely distributed points can disproportionately affect the final similarity score. Besides, CD calculates the simple average of distances of matched point pairs between two sets, which does not take into account the underlying point-wise distance distribution across two point clouds (same weights assigned for  short- and  long-distance pairs by using uniform distribution). To mitigate these issues, we analyze the effect of prioritizing short- and long-distance pairs with Gaussian distributions obtained with grid search, and based on the findings, we take an indirect approach to find Landau distribution, out of many distributions, fits in the form of bimodal Gaussian mixture model which balances two types of pairs. Based on this observation, we propose LandauCD, an innovative loss function grounded in the Landau distribution. We conduct comprehensive experiments using LandauCD and observe significant improvements consistently over all the popular baseline networks trained with CD-based losses, leading to new state-of-the-art results on several benchmarks (PCN, Shapet-55/34, ShapeNet-Part). We also delve into the theoretical explanation behind the consistent improvements of LandauCD.  Code and weights will be released upon acceptance.

## item_id: m_0347

TITLE: Spectrum Intelligence via Multi-Agent Hybrid Retrieval-Augmented Generation

ABSTRACT: Spectrum policy making requires reviewing large volumes of information from different sources, including technical reports, stakeholder filings and incumbent licenses, which makes the process slow and resource-intensive. To speed this process, we propose a Multi-Agent Hybrid Retrieval-Augmented Generation (RAG) system for analyzing spectrum proceeding documents and license data. Through customized prompts and tailored tools, the system demonstrates the ability to handle complex queries and perform multi-step retrieval and analysis. For evaluation, we built a benchmark dataset in the form of question-answer pairs and used it to compare our system with others. Extensive experimental results show that our Multi-Agent Hybrid RAG system significantly improves the understanding of spectrum data, providing more reliable and verifiable support for spectrum policy analysis. Our approach provides new insights into how agentic RAG can leverage heterogeneous structured and unstructured data sources to accomplish complex policy analysis tasks, highlighting its potential for broader applications in domain-specific decision support.

## item_id: m_0348

TITLE: Seq2SQL: Generating Structured Queries From Natural Language Using Reinforcement Learning 

ABSTRACT: Relational databases store a significant amount of the worlds data. However, accessing this data currently requires users to understand a query language such as SQL. We propose Seq2SQL, a deep neural network for translating natural language questions to corresponding SQL queries. Our model uses rewards from in the loop query execution over the database to learn a policy to generate the query, which contains unordered parts that are less suitable for optimization via cross entropy loss. Moreover, Seq2SQL leverages the structure of SQL to prune the space of generated queries and significantly simplify the generation problem. In addition to the model, we release WikiSQL, a dataset of 80654 hand-annotated examples of questions and SQL queries distributed across 24241 tables fromWikipedia that is an order of magnitude larger than comparable datasets. By applying policy based reinforcement learning with a query execution environment to WikiSQL, Seq2SQL outperforms a state-of-the-art semantic parser, improving execution accuracy from 35.9% to 59.4% and logical form accuracy from 23.4% to 48.3%.

## item_id: m_0349

TITLE: Short-Term Memory Convolutions

ABSTRACT: The real-time processing of time series signals is a critical issue for many real-life applications. The idea of real-time processing is especially important in audio domain as the human perception of sound is sensitive to any kind of disturbance in perceived signals, especially the lag between auditory and visual modalities. The rise of deep learning (DL) models complicated the landscape of signal processing. Although they often have superior quality compared to standard DSP methods, this advantage is diminished by higher latency. In this work we propose novel method for minimization of inference time latency and memory consumption, called Short-Term Memory Convolution (STMC) and its transposed counterpart. The main advantage of STMC is the low latency comparable to long short-term memory (LSTM) networks. Furthermore, the training of STMC-based models is faster and more stable as the method is based solely on convolutional neural networks (CNNs). In this study we demonstrate an application of this solution to a U-Net model for a speech separation task and GhostNet model in acoustic scene classification (ASC) task. In case of speech separation we achieved a 5-fold reduction in inference time and a 2-fold reduction in latency without affecting the output quality. The inference time for ASC task was up to 4 times faster while preserving the original accuracy.

## item_id: m_0350

TITLE: Deep Ensemble Kernel Learning

ABSTRACT: Gaussian processes (GPs) are nonparametric Bayesian models that are both flexible and robust to overfitting. One of the main challenges of GP methods is selecting the kernel. In the deep kernel learning (DKL) paradigm, a deep neural network or ``feature network'' is used to map inputs into a latent feature space, where a GP with a ``base kernel'' acts; the resulting model is then trained in an end-to-end fashion. In this work, we introduce the ``deep ensemble kernel learning'' (DEKL) model, which is a special case of DKL. In DEKL, a linear base kernel is used, enabling exact optimization of the base kernel hyperparameters and a scalable inference method that does not require approximation by inducing points. We also represent the feature network as a concatenation of an ensemble of learner networks with a common architecture, allowing for easy model parallelism. We show that DEKL is able to approximate any kernel if the number of learners in the ensemble is arbitrarily large. Comparing the DEKL model to DKL and deep ensemble (DE) baselines on both synthetic and real-world regression tasks, we find that DEKL often outperforms both baselines in terms of predictive performance and that the DEKL learners tend to be more diverse (i.e., less correlated with one another) compared to the DE learners.

## item_id: m_0351

TITLE: Label-Free Synthetic Pretraining of Object Detectors

ABSTRACT: We propose a new approach, Synthetic Optimized Layout with Instance Detection (SOLID), to pretrain object detectors with synthetic images. Our ``SOLID'' approach consists of two main components: (1) generating synthetic images using a collection of unlabelled 3D models with optimized scene arrangement; (2) pretraining an object detector on "instance detection" task - given a query image depicting an object, detecting all instances of the exact same object in a target image. Our approach does not need any semantic labels for pretraining and allows the use of arbitrary, diverse 3D models.  Experiments on COCO show that with optimized data generation and a proper pretraining task, synthetic data can be highly effective data for pretraining object detectors. In particular, pretraining on rendered images achieves performance competitive with pretraining on real images while using significantly less computing resources.

## item_id: m_0352

TITLE: Visual Question Answering From Another Perspective: CLEVR Mental Rotation Tests

ABSTRACT: Different types of \emph{mental rotation tests} have been used extensively in psychology to understand human visual reasoning and perception. Understanding what an object or visual scene would look like from another viewpoint is a challenging problem that is made even harder if it must be performed from a single image. 3D computer vision has a long history of examining related problems. However, often what one is most interested in is the answer to a relatively simple question posed in another visual frame of reference -- as opposed to creating a full 3D reconstruction. 
Mental rotations tests can also manifest as consequential questions in the real world such as: does the pedestrian that I see, see the car that I am driving?
We explore a controlled setting whereby questions are posed about the properties of a scene if the scene were observed from another viewpoint. To do this we have created a new version of the CLEVR VQA problem setup and dataset that we call CLEVR Mental Rotation Tests or CLEVR-MRT, where the goal is to answer questions about the original CLEVR viewpoint given a single image obtained from a different viewpoint of the same scene. Using CLEVR Mental Rotation Tests we examine standard state of the art methods, show how they fall short, then explore novel neural architectures that involve inferring representations encoded as feature volumes describing a scene. Our new methods use rigid transformations of feature volumes conditioned on the viewpoint camera. We examine the efficacy of different model variants through performing a rigorous ablation study. Furthermore, we examine the use of contrastive learning to infer a volumetric encoder in a self-supervised manner and find that this approach yields the best results of our study using CLEVR-MRT.

## item_id: m_0353

TITLE: Non-Redundant Graph Neural Networks with Improved Expressiveness

ABSTRACT: Message passing graph neural networks iteratively compute node embeddings by aggregating messages from all neighbors. This procedure can be viewed as a neural variant of the Weisfeiler-Leman method, which limits their expressive power. Moreover, oversmoothing and oversquashing restrict the number of layers these networks can effectively utilize. The repeated exchange and encoding of identical information in message passing amplifies oversquashing. We propose a novel aggregation scheme based on neighborhood trees, which allows for controlling the redundancy by pruning branches of the unfolding trees underlying standard message passing. We prove that reducing redundancy improves expressivity and experimentally show that it alleviates oversquashing. We investigate the interaction between redundancy in message passing and redundancy in computation and propose a compact representation of neighborhood trees, from which we compute node and graph embeddings via a neural tree canonization technique. Our method is provably more expressive than the Weisfeiler-Leman method, less susceptible to oversquashing than message passing neural networks, and provides high classification accuracy on widely-used benchmark datasets.

## item_id: m_0354

TITLE: Learning multi-scale local conditional probability models of images

ABSTRACT: Deep neural networks can learn powerful prior probability models for images, as evidenced by the high-quality generations obtained with recent score-based diffusion methods. But the means by which these networks capture complex global statistical structure, apparently without suffering from the curse of dimensionality, remain a mystery. To study this, we incorporate diffusion methods into a multi-scale decomposition, reducing dimensionality by assuming a stationary local Markov model for wavelet coefficients conditioned on coarser-scale coefficients. We instantiate this model using convolutional neural networks (CNNs) with local receptive fields, which enforce both the stationarity and Markov properties. Global structures are captured using a CNN with receptive fields covering the entire (but small) low-pass image. We test this model on a dataset of face images, which are highly non-stationary and contain large-scale geometric structures.
Remarkably, denoising, super-resolution, and image synthesis results all demonstrate that these structures can be captured with significantly smaller conditioning neighborhoods than required by a Markov model implemented in the pixel domain. Our results show that score estimation for large complex images can be reduced to low-dimensional Markov conditional models across scales,  alleviating the curse of dimensionality. 

## item_id: m_0355

TITLE: Off Policy Average Reward Actor Critic with Deterministic Policy Search

ABSTRACT: The average reward criterion is relatively less explored as most existing works in the Reinforcement Learning literature consider the discounted reward criterion. There are few recent works that present on-policy average reward actor-critic algorithms, but average reward off-policy actor-critic is relatively less explored. In this paper, we present both on-policy and off-policy deterministic policy gradient theorems for the average reward performance criterion. Using these theorems, we also present an Average Reward Off-Policy Deep Deterministic Policy Gradient (ARO-DDPG) Algorithm. We show a finite time analysis of the resulting three-timescale stochastic approximation scheme and obtain an $\epsilon$-optimal stationary policy with a sample complexity of $\Omega(\epsilon^{-2.5})$. We compare the average reward performance of our proposed algorithm and observe better empirical performance compared to state-of-the-art on-policy average reward actor-critic algorithms over MuJoCo based environments. 

## item_id: m_0356

TITLE: Exploring LOTS in Deep Neural Networks

ABSTRACT: Deep neural networks have recently demonstrated excellent performance on various tasks. Despite recent advances, our understanding of these learning models is still incomplete, at least, as their unexpected vulnerability to imperceptibly small, non-random perturbations revealed. The existence of these so-called adversarial examples presents a serious problem of the application of vulnerable machine learning models. In this paper, we introduce the layerwise origin-target synthesis (LOTS) that can serve multiple purposes. First, we can use it as a visualization technique that gives us insights into the function of any intermediate feature layer by showing the notion of a particular input in deep neural networks. Second, our approach can be applied to assess the invariance of the learned features captured at any layer with respect to the class of the particular input. Finally, we can also utilize LOTS as a general way of producing a vast amount of diverse adversarial examples that can be used for training to further improve the robustness of machine learning models and their performance as well.

## item_id: m_0357

TITLE: Local KL Convergence Rate for Stein Variational Gradient Descent with Reweighted Kernel

ABSTRACT:  We study convergence properties of Stein Variational Gradient Descent (SVGD) algorithm for sampling from a non-normalized probabilistic distribution $p_*({x})\propto\exp(-f_*({x}))$. Compared with Kernelized Stein Discrepancy (KSD) convergence analyzed in previous literature, KL convergence as a more convincing criterion can better explain the effectiveness of SVGD in real-world applications. In the population limit, SVGD performs smoothed gradient descent with kernel integral operator. Notably, SVGD with smoothing kernels suffers from gradient vanishing in low-density areas, which makes the error term between smoothed gradient and Wasserstein gradient not controllable. In this context, we introduce a reweighted kernel to amplify the smoothed gradient in low-density areas, which leads to a bounded error term to Wasserstein gradient. When the $p_*({x})$ satisfies log-Sobolev inequality, we develop the convergence rate for SVGD in KL divergence with the reweighted kernel. Our analysis points out the defects of conventional smoothing kernels in SVGD and provides the convergence rate for SVGD in KL divergence.

## item_id: m_0358

TITLE: Quantifying uncertainty with GAN-based priors

ABSTRACT: Bayesian inference is used extensively to quantify the uncertainty in an inferred field given the measurement of a related field when the two are linked by a mathematical model. Despite its many applications, Bayesian inference faces challenges when inferring fields that have discrete representations of large dimension, and/or have prior distributions that are difficult to characterize mathematically. In this work we demonstrate how the approximate distribution learned by a generative adversarial network (GAN) may be used as a prior in a Bayesian update to address both these challenges. We demonstrate the efficacy of this approach by inferring and quantifying uncertainty in inference problems arising in computer vision and  physics-based applications. In both instances we highlight the role of computing uncertainty in providing a measure of confidence in the solution, and in designing successive measurements to improve this confidence. 

## item_id: m_0359

TITLE: MCM: Masked Cell Modeling for Anomaly Detection in Tabular Data

ABSTRACT: This paper addresses the problem of anomaly detection in tabular data, which is usually implemented in an one-class classification setting where the training set only contains normal samples. Inspired by the success of masked image/language modeling in vision and natural language domains, we extend masked modeling methods to address this problem by capturing intrinsic correlations between features in training set. Thus, a sample deviate from such correlations is related to a high possibility of anomaly. To obtain multiple and diverse correlations, we propose a novel masking strategy which generates multiple masks by learning, and design a diversity loss to reduce the similarity of different masks. Extensive experiments show our method achieves state-of-the-art performance. We also discuss the interpretability from the perspective of each individual feature and correlations between features.

## item_id: m_0360

TITLE: Information Laundering for Model Privacy

ABSTRACT: In this work, we propose information laundering, a novel framework for enhancing model privacy. Unlike data privacy that concerns the protection of raw data information, model privacy aims to protect an already-learned model that is to be deployed for public use. The private model can be obtained from general learning methods, and its deployment means that it will return a deterministic or random response for a given input query. An information-laundered model consists of probabilistic components that deliberately maneuver the intended input and output for queries of the model, so the model's adversarial acquisition is less likely. Under the proposed framework, we develop an information-theoretic principle to quantify the fundamental tradeoffs between model utility and privacy leakage and derive the optimal design.

## item_id: m_0361

TITLE: Learning Continuous Semantic Representations of Symbolic Expressions

ABSTRACT: The question of how procedural knowledge is represented and inferred is a fundamental problem in machine learning and artificial intelligence. Recent work on program induction has proposed neural architectures, based on abstractions like stacks, Turing machines, and interpreters,  that operate on abstract computational machines or on execution traces. But the recursive abstraction that is central to procedural knowledge is perhaps most naturally represented by symbolic representations that have syntactic structure, such as logical expressions and source code. Combining abstract, symbolic reasoning with continuous neural reasoning is a grand challenge of representation learning. As a step in this direction, we propose a new architecture, called neural equivalence networks, for the problem of learning continuous semantic representations of mathematical and logical expressions. These networks are trained to represent semantic equivalence, even of expressions that are syntactically very different. The challenge is that semantic representations must be computed in a syntax-directed manner, because semantics is compositional, but at the same time, small changes in syntax can lead to very large changes in semantics, which can be difficult for continuous neural architectures. We perform an exhaustive evaluation  on the task of checking equivalence on a highly diverse class of symbolic algebraic and boolean expression types, showing that our model significantly outperforms existing architectures.


## item_id: m_0362

TITLE: Submodular Sum-product Networks for Scene Understanding

ABSTRACT: Sum-product networks (SPNs) are an expressive class of deep probabilistic models in which inference takes time linear in their size, enabling them to be learned effectively. However, for certain challenging problems, such as scene understanding, the corresponding SPN has exponential size and is thus intractable. In this work, we introduce submodular sum-product networks (SSPNs), an extension of SPNs in which sum-node weights are defined by a submodular energy function. SSPNs combine the expressivity and depth of SPNs with the ability to efficiently compute the MAP state of a combinatorial number of labelings afforded by submodular energies. SSPNs for scene understanding can be understood as representing all possible parses of an image over arbitrary region shapes with respect to an image grammar. Despite this complexity, we develop an efficient and convergent algorithm based on graph cuts for computing the (approximate) MAP state of an SSPN, greatly increasing the expressivity of the SPN model class. Empirically, we show exponential improvements in parsing time compared to traditional inference algorithms such as alpha-expansion and belief propagation, while returning comparable minima.


## item_id: m_0363

TITLE: Winograd Structured Pruning

ABSTRACT: Both Winograd convolution (\textit{WC}) and pruning can significantly reduce the computation of Convolutional Neural Network (CNN), but applying them simultaneously is challenging.
For example, applying fine-grained pruning to \textit{WC} eliminates the computational advantages from sparsity due to Winograd transformation.
Moreover, integrating \textit{WC} with filter pruning can lead to a reduction in network accuracy due to the use of large pruning unit size.
To address previous challenges, this paper proposes Adaptive Balanced Winograd Structured Pruning (ABWSP), a method specifically designed to prune weights in \textit{WC} networks executed on GPUs, which are widely used as computing devices for CNNs. 
ABWSP takes into account three crucial factors: pruning unit size, workload balance, and layer importance. 
First, ABWSP efficiently utilizes the computing units on GPUs by pruning grouped weights simultaneously.
Considering the computational characteristics of \textit{WC} on GPU, the group size can be minimized while maintaining a regular data pattern (i.e., WSP).
Secondly, the General Matrix Multiplications (GEMMs) of a layer are executed concurrently on GPU, and the execution time of the layer is determined by the longest GEMM operation.
To minimize the execution cycle for \textit{WC}, ABWSP maintains an equal pruning ratio between matrices of \textit{WC} (i.e., BWSP).
Lastly, applying BWSP to all layers results in a loss of accuracy.
Since the importance varies for each \textit{WC} layer, the accuracy loss and performance benefit due to BWSP are different.
To maintain accuracy with high speedup, ABWSP comprehensively evaluates both accuracy and speedup to determine the appropriate application of BWSP or WSP for each layer, automatically. 
By considering these factors, ABWSP optimizes the pruning process by effectively utilizing GPU computing units, minimizing execution cycles of each layer, and ensuring a balance between accuracy and speedup.

## item_id: m_0364

TITLE: Disentangling Writer and Character Styles for Handwriting Generation

ABSTRACT: Training machines for synthesizing diverse handwritings is an intriguing task. Recently, some RNN-based methods are proposed to generate stylized online Chinese characters. But these methods mainly focus on learning a person’s overall writing style and hence neglect the detailed style inconsistencies between characters from the same writer. For example, one person’s handwritings always appear an overall uniformity (e.g., character slant and aspect ratios) but there are still small style differences between local regions (e.g., stroke length and curvature) of characters. Motivated by this, in this paper, we propose to disentangle the style representations at both writer and character levels from individual handwritings. Specifically, we propose the style-disentangled transformer (SDT), equipped with two complementary contrastive objectives, to extract the overall writer-wise and detailed character-wise style representations, respectively, which boosts the generation quality of online handwritings. Extensive experiments on various language scripts verify the superiority of SDT. Particularly, we empirically find that the two learned style representations provide information with different frequency magnitudes, which demonstrates the necessity of separate style extraction.

## item_id: m_0365

TITLE: Compositional Hardness of Code in Large Language Models - A Probabilistic Perspective

ABSTRACT: A common practice in large language model (LLM) usage for complex analytical tasks such as code generation, is to sample a solution for the entire task within the model's context window. Previous works have shown that subtask decomposition within the model's context (chain of thought), is beneficial for solving such tasks. In this work, we point a limitation of LLMs' ability to perform several sub-tasks within the same context window - an in-context hardness of composition, pointing to an advantage for distributing a decomposed problem in a multi-agent system of LLMs. The hardness of composition is quantified by a generation complexity metric, i.e., the number of LLM generations required to sample at least one correct solution. We find a gap between the generation complexity of solving a compositional problem within the same context relative to distributing it among multiple agents, that increases exponentially with the solution's length. We prove our results theoretically and demonstrate them empirically.

## item_id: m_0366

TITLE: Espresso: Efficient Forward Propagation for Binary Deep Neural Networks

ABSTRACT:   There are many applications scenarios for which the computational
  performance and memory footprint of the prediction phase of Deep
  Neural Networks (DNNs) need to be optimized. Binary Deep Neural
  Networks (BDNNs) have been shown to be an effective way of achieving
  this objective. In this paper, we show how Convolutional Neural
  Networks (CNNs) can be implemented using binary
  representations. Espresso is a compact, yet powerful
  library written in C/CUDA that features all the functionalities
  required for the forward propagation of CNNs, in a binary file less
  than 400KB, without any external dependencies. Although it is mainly
  designed to take advantage of massive GPU parallelism, Espresso also
  provides an equivalent CPU implementation for CNNs. Espresso
  provides special convolutional and dense layers for BCNNs,
  leveraging bit-packing and bit-wise computations
  for efficient execution. These techniques provide a speed-up of
  matrix-multiplication routines, and at the same time, reduce memory
  usage when storing parameters and activations. We experimentally
  show that Espresso is significantly faster than existing
  implementations of optimized binary neural networks (~ 2
  orders of magnitude). Espresso is released under the Apache 2.0
  license and is available at http://github.com/organization/project.

## item_id: m_0367

TITLE: Benefit of Interpolation in Nearest Neighbor Algorithms

ABSTRACT: The over-parameterized models attract much attention in the era of data science and deep learning. It is empirically observed that although these models, e.g. deep neural networks, over-fit the training data, they can still achieve small testing error, and sometimes even outperform traditional algorithms which are designed to avoid over-fitting. The major goal of this work is to sharply quantify the benefit of data interpolation in the context of nearest neighbors (NN) algorithm. Specifically, we consider a class of interpolated weighting schemes and then carefully characterize their asymptotic performances. Our analysis reveals a U-shaped performance curve with respect to the level of data interpolation, and proves that a mild degree of data interpolation strictly improves the prediction accuracy and statistical stability over those of the (un-interpolated) optimal $k$NN algorithm. This theoretically justifies (predicts) the existence of the second U-shaped curve in the recently discovered double descent phenomenon. Note that our goal in this study is not to promote the use of interpolated-NN method, but to obtain theoretical insights on data interpolation inspired by the aforementioned phenomenon.

## item_id: m_0368

TITLE: Bit-Pragmatic Deep Neural Network Computing

ABSTRACT: We quantify a source of ineffectual computations when processing the multiplications of the convolutional layers in Deep Neural Networks (DNNs) and propose Pragrmatic (PRA), an architecture that exploits it improving performance and energy efficiency. 
The source of these ineffectual computations is best understood in the context of conventional multipliers which generate internally multiple terms, that is, products of the multiplicand and powers of two, which added together produce the final product. At runtime, many of these terms are zero as they are generated when the multiplicand is combined with the zero-bits of the multiplicator. While conventional bit-parallel multipliers calculate all terms in parallel to reduce individual product latency, PRA calculates only the non-zero terms resulting in a design whose execution time for convolutional layers is ideally proportional to the number of activation bits that are 1. Measurements demonstrate that for the convolutional layers on Convolutional Neural Networks and during inference, PRA improves performance by 4.3x over the DaDiaNao (DaDN) accelerator and by 4.5x when DaDN uses an 8-bit quantized representation. DaDN was reported to be 300x faster than commodity graphics processors. 



## item_id: m_0369

TITLE: IsoScore: Measuring the Uniformity of Vector Space Utilization

ABSTRACT: The recent success of distributed word representations has led to an increased interest in analyzing the properties of their spatial distribution. Current metrics suggest that contextualized word embedding models do not uniformly utilize all available dimensions when embedding tokens in vector space. Previous works argue that encouraging isotropy in embedding space corresponds to improved performance on downstream tasks. However, existing metrics---average random cosine similarity, for example---do not properly measure isotropy and tend to obscure the true spatial distribution of point clouds. To address this issue, we propose IsoScore: a novel metric that quantifies the degree to which a point cloud uniformly utilizes the ambient vector space. We demonstrate that IsoScore has several desirable properties, such as mean invariance and direct correspondence to the number of dimensions used that existing scores do not possess.
Furthermore, IsoScore is conceptually intuitive, making it well suited for analyzing the distribution of arbitrary point clouds in vector space, not necessarily limited to point clouds of word embeddings alone. We conclude by using IsoScore to demonstrate that a number of recent conclusions in the NLP literature that have been derived using brittle metrics of spatial distribution may be incomplete or altogether inaccurate.

## item_id: m_0370

TITLE: The Path-Driven Independence Testing (PIT) Algorithm

ABSTRACT: PC is an efficient constraint-based algorithm for learning the structure of a Bayesian network. However, the required number of conditional independent (CI) tests can make the algorithm practically infeasible or slow for large graphs. We developed a constrained-based algorithm, called the Path-Driven Independence Testing (PIT) Algorithm, which during the learning process, utilizes the information of the partially learned network to reduce the number of CI tests. The idea is that for each pair of variables $X$ and $Y$, instead of checking independence conditioned on every subset of all the neighbors of $X$ (resp. $Y$) as in PC, the search is restricted to only the common neighbors of $X$ and $Y$ and to neighbors connected to $Y$ (resp. $X$) by a path. Also, paths connecting $X$ and $Y$ without a descendant of a common neighbor can be blocked by observing two consecutive nodes on the path. Compared to PC, PIT is proven to conduct at most the same number of CI tests, and experimentally shown to be significantly (up to 7 times) faster and more accurate.

## item_id: m_0371

TITLE: Countdown Regression: Sharp and Calibrated Survival Predictions

ABSTRACT: Personalized probabilistic forecasts of time to event (such as mortality) can be crucial in decision making, especially in the clinical setting. Inspired by ideas from the meteorology literature, we approach this problem through the paradigm of maximizing sharpness of prediction distributions, subject to calibration. In regression problems, it has been shown that optimizing the continuous ranked probability score (CRPS) instead of maximum likelihood leads to sharper prediction distributions while maintaining calibration. We introduce the Survival-CRPS, a generalization of the CRPS to the time to event setting, and present right-censored and interval-censored variants. To holistically evaluate the quality of predicted distributions over time to event, we present the scale agnostic Survival-AUPRC evaluation metric, an analog to area under the precision-recall curve. We apply these ideas by building a recurrent neural network for mortality prediction, using an Electronic Health Record dataset covering millions of patients. We demonstrate signiﬁcant beneﬁts in models trained by the Survival-CRPS objective instead of maximum likelihood.

## item_id: m_0372

TITLE: Deep Variational Bayes Filters: Unsupervised Learning of State Space Models from Raw Data

ABSTRACT: We introduce Deep Variational Bayes Filters (DVBF), a new method for unsupervised learning and identification of latent Markovian state space models. Leveraging recent advances in Stochastic Gradient Variational Bayes, DVBF can overcome intractable inference distributions via variational inference. Thus, it can handle highly nonlinear input data with temporal and spatial dependencies such as image sequences without domain knowledge. Our experiments show that enabling backpropagation through transitions enforces state space assumptions and significantly improves information content of the latent embedding. This also enables realistic long-term prediction.


## item_id: m_0373

TITLE: Meta-Learning with Domain Adaptation for Few-Shot Learning under Domain Shift

ABSTRACT: Few-Shot Learning (learning with limited labeled data) aims to overcome the limitations of traditional machine learning approaches which require thousands of labeled examples to train an effective model. Considered as a hallmark of human intelligence, the community has recently witnessed several contributions on this topic, in particular through meta-learning, where a model learns how to learn an effective model for few-shot learning. The main idea is to acquire prior knowledge from a set of training tasks, which is then used to perform (few-shot) test tasks. Most existing work assumes that both training and test tasks are drawn from the same distribution, and a large amount of labeled data is available in the training tasks. This is a very strong assumption which restricts the usage of meta-learning strategies in the real world where ample training tasks following the same distribution as test tasks may not be available. In this paper, we propose a novel meta-learning paradigm wherein a few-shot learning model is learnt, which simultaneously overcomes domain shift between the train and test tasks via adversarial domain adaptation. We demonstrate the efficacy the proposed method through extensive experiments.

## item_id: m_0374

TITLE: Analyzing the Effects of Emulating on the Reinforcement Learning Manifold

ABSTRACT: Reinforcement learning has become a prominent research direction with the utilization of deep neural networks as state-action value function approximators enabling exploration and construction of functioning neural policies in MDPs with state representations in high dimensions. While reinforcement learning is currently being deployed in many different settings from medical to finance, the fact that reinforcement learning requires a reward signal from the MDP to learn a functioning policy can be restrictive for tasks in which the construction of the reward function is more or equally complex than learning it. In this line of research several studies proposed algorithms to learn a reward function or an optimal policy from observed optimal trajectories. In this paper, we focus on non-robustness of the state-of-the-art algorithms that accomplish learning without rewards in high dimensional state representation MDPs, and we demonstrate that the vanilla trained deep reinforcement learning policies are more resilient and value aligned than learning without rewards in MDPs with complex state representations.

## item_id: m_0375

TITLE: A Better Alternative to Error Feedback for Communication-Efficient Distributed Learning

ABSTRACT: Modern large-scale machine learning applications require stochastic optimization algorithms to be implemented on distributed computing systems. A key bottleneck of such systems is the communication overhead for exchanging information across the workers, such as stochastic gradients. Among the many techniques proposed to remedy this issue, one of the most successful is the framework of compressed communication with error feedback (EF). EF remains the only known technique that can deal with the error induced by contractive compressors which are not unbiased, such as Top-$K$ or PowerSGD.  In this paper, we propose a new and theoretically and practically better alternative to EF for dealing with contractive compressors. In particular, we propose a construction which can transform any contractive compressor into an induced unbiased compressor. Following this transformation, existing methods able to work with unbiased compressors can be applied. We show that our approach leads to vast improvements over EF, including reduced memory requirements, better communication complexity guarantees and fewer assumptions. We further extend our results to federated learning with partial participation following an arbitrary distribution over the nodes and demonstrate the benefits thereof. We perform several numerical experiments which validate our theoretical findings.

## item_id: m_0376

TITLE: The Predictron: End-To-End Learning and Planning

ABSTRACT: One of the key challenges of artificial intelligence is to learn models that are effective in the context of planning. In this document we introduce the predictron architecture. The predictron consists of a fully abstract model, represented by a Markov reward process, that can be rolled forward multiple "imagined" planning steps. Each forward pass of the predictron accumulates internal rewards and values over multiple planning depths. 
The predictron is trained end-to-end so as to make these accumulated values accurately approximate the true value function, thereby focusing the model upon the aspects of the environment most relevant to planning. We applied the predictron to procedurally generated random mazes and a simulator for the game of pool. The predictron yielded significantly more accurate predictions than conventional deep neural network architectures.

## item_id: m_0377

TITLE: SaliencyMix: A Saliency Guided Data Augmentation Strategy for Better Regularization

ABSTRACT: Advanced data augmentation strategies have widely been studied to improve the generalization ability of deep learning models. Regional dropout is one of the popular solutions that guides the model to focus on less discriminative parts by randomly removing image regions, resulting in improved regularization. However, such information removal is undesirable. On the other hand, recent strategies suggest to randomly cut and mix patches and their labels among training images, to enjoy the advantages of regional dropout without having any pointless pixel in the augmented images. We argue that such random selection strategies of the patches may not necessarily represent sufficient information about the corresponding object and thereby mixing the labels according to that uninformative patch enables the model to learn unexpected feature representation. Therefore, we propose SaliencyMix that carefully selects a representative image patch with the help of a saliency map and mixes this indicative patch with the target image, thus leading the model to learn more appropriate feature representation. SaliencyMix achieves the best known top-1 error of $21.26\%$ and $20.09\%$ for ResNet-50 and ResNet-101 architectures on ImageNet classification, respectively, and also improves the model robustness against adversarial perturbations. Furthermore, models that are trained with SaliencyMix, help to improve the object detection performance.  Source code is available at \url{https://github.com/SaliencyMix/SaliencyMix}.

## item_id: m_0378

TITLE: Deep unsupervised learning through spatial contrasting

ABSTRACT: Convolutional networks have marked their place over the last few years as the
best performing model for various visual tasks. They are, however, most suited
for supervised learning from large amounts of labeled data. Previous attempts
have been made to use unlabeled data to improve model performance by applying
unsupervised techniques. These attempts require different architectures and training methods.
In this work we present a novel approach for unsupervised training
of Convolutional networks that is based on contrasting between spatial regions
within images.  This criterion can be employed within conventional neural net-
works and trained using standard techniques such as SGD and back-propagation,
thus complementing supervised methods.

## item_id: m_0379

TITLE: On the Price of Differential Privacy for Hierarchical Clustering

ABSTRACT: Hierarchical clustering is a fundamental unsupervised machine learning task with the aim of organizing data into a hierarchy of clusters. Many applications of hierarchical clustering involve sensitive user information, therefore motivating recent studies on differentially private hierarchical clustering under the rigorous framework of Dasgupta's objective. However, it has been shown that any privacy-preserving algorithm under edge-level differential privacy necessarily suffers a large error. To capture practical applications of this problem, we focus on the weight privacy model, where each edge of the input graph is at least unit weight. We present a novel algorithm in the weight privacy model that shows significantly better approximation than known impossibility results in the edge-level DP setting. In particular, our algorithm achieves $O(\log^{1.5}n/\varepsilon)$ multiplicative error for $\varepsilon$-DP and runs in polynomial time, where $n$ is the size of the input graph, and the cost is never worse than the optimal additive error in existing work. We complement our algorithm by showing if the unit-weight constraint does not apply, the lower bound for weight-level DP hierarchical clustering is essentially the same as the edge-level DP, i.e. $\Omega(n^2/\varepsilon)$ additive error. As a result, we also obtain a new lower bound of $\tilde{\Omega}(1/\varepsilon)$ additive error for balanced sparsest cuts in the weight-level DP model, which may be of independent interest. Finally, we evaluate our algorithm on synthetic and real-world datasets. Our experimental results show that our algorithm performs well in terms of extra cost and has good scalability to large graphs.

## item_id: m_0380

TITLE: Sequenced-Replacement Sampling for Deep Learning

ABSTRACT: We propose sequenced-replacement sampling (SRS) for training deep neural networks. The basic idea is to assign a fixed sequence index to each sample in the dataset. Once a mini-batch is randomly drawn in each training iteration, we refill the original dataset by successively adding samples according to their sequence index. Thus we carry out replacement sampling but in a batched and sequenced way. In a sense, SRS could be viewed as a way of performing "mini-batch augmentation". It is particularly useful for a task where we have a relatively small images-per-class such as CIFAR-100. Together with a longer period of initial large learning rate, it significantly improves the classification accuracy in CIFAR-100 over the current state-of-the-art results. Our experiments indicate that training deeper networks with SRS is less prone to over-fitting. In the best case, we achieve an error rate as low as 10.10%.

## item_id: m_0381

TITLE: Neural implicit mapping via nested neighborhoods: real-time rendering of neural SDFs with textures

ABSTRACT: We introduce the nested neighborhood model, a framework to address the problem of real-time joint estimation of surface geometry and its attributes (normals and textures) from neural SDFs.
This problem was only partially approached by previous works, which do not support attributes nor dynamic surfaces in real-time.
The framework is built on the nesting condition, which establishes a criteria for the neighborhoods of zero-level sets of a sequence of neural SDFs to be nested. This allows mappings between such neighborhoods, enabling the definition of the multiscale sphere tracing, the neural attribute mapping, and the GEMM-based analytical normal computation algorithms, composing the nested neighborhood model.
Our framework does not use spatial data-structures and its components can be used to augment meshes with smooth neural normals and textures. The normal GEMM-based computation does not depend on auto-differentiation nor computational graphs, resulting in real-time performance.

## item_id: m_0382

TITLE: CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery

ABSTRACT: Large language models (LLMs) have demonstrated significant potential in advancing various fields of research and society. However, the current community of LLMs overly focuses on benchmarks for analyzing specific foundational skills (e.g. mathematics and code generation), neglecting an all-round evaluation of the computer science field. To bridge this gap, we introduce CS-Bench, the first multilingual (English, Chinese, French, German) benchmark dedicated to evaluating the performance of LLMs in computer science. CS-Bench comprises approximately 10K meticulously curated test samples, covering 26 subfields across 4 key areas of computer science, encompassing various task forms and divisions of knowledge and reasoning. Utilizing CS-Bench, we conduct a comprehensive evaluation of over 30 mainstream LLMs, revealing the relationship between CS performance and model scales. We also quantitatively analyze the reasons for failures in existing LLMs and highlight directions for improvements, including knowledge supplementation and CS-specific reasoning. Further cross-capability experiments show a high correlation between LLMs' capabilities in computer science and their abilities in mathematics and coding. Moreover, expert LLMs specialized in mathematics and coding also demonstrate strong performances in several CS subfields. Looking ahead, we envision CS-Bench serving as a cornerstone for LLM applications in the CS field and paving new avenues in assessing LLMs' diverse reasoning capabilities. Our project homepage is available at https://csbench.github.io/.

## item_id: m_0383

TITLE: Adapting Stepsizes by Momentumized Gradients Improves Optimization and Generalization

ABSTRACT: Adaptive gradient methods, such as Adam, have achieved tremendous success in machine learning. Scaling gradients by square roots of the running averages of squared past gradients, such methods are able to attain rapid training of modern deep neural networks. Nevertheless, they are observed to generalize worse than stochastic gradient descent (SGD) and tend to be trapped in local minima at an early stage during training. Intriguingly, we discover that substituting the gradient in the second moment estimation term with the momentumized version in Adam can well solve the issues. The intuition is that gradient with momentum contains more accurate directional information and therefore its second moment estimation is a better choice for scaling than that of the raw gradient. Thereby we propose AdaMomentum as a new optimizer reaching the goal of training fast while generalizing better. We further develop a theory to back up the improvement in optimization and generalization and provide convergence guarantees under both convex and nonconvex settings. Extensive experiments on a wide range of tasks and models demonstrate that AdaMomentum exhibits state-of-the-art performance consistently. The source code is available at https://anonymous.4open.science/r/AdaMomentum_experiments-6D9B.

## item_id: m_0384

TITLE: Small steps and giant leaps: Minimal Newton solvers for Deep Learning

ABSTRACT: We propose a fast second-order method that can be used as a drop-in replacement for current deep learning solvers. Compared to stochastic gradient descent (SGD), it only requires two additional forward-mode automatic differentiation operations per iteration, which has a computational cost comparable to two standard forward passes and is easy to implement. Our method addresses long-standing issues with current second-order solvers, which invert an approximate Hessian matrix every iteration exactly or by conjugate-gradient methods, procedures that are much slower than a SGD step. Instead, we propose to keep a single estimate of the gradient projected by the inverse Hessian matrix, and update it once per iteration with just two passes over the network. This estimate has the same size and is similar to the momentum variable that is commonly used in SGD. No estimate of the Hessian is maintained.
We first validate our method, called CurveBall, on small problems with known solutions (noisy Rosenbrock function and degenerate 2-layer linear networks), where current deep learning solvers struggle. We then train several large models on CIFAR and ImageNet, including ResNet and VGG-f networks, where we demonstrate faster convergence with no hyperparameter tuning. We also show our optimiser's generality by testing on a large set of randomly-generated architectures.

## item_id: m_0385

TITLE: From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs

ABSTRACT: Large Language Models (LLMs) can acquire deceptive behaviors through backdoor attacks, where the model executes prohibited actions whenever secret triggers appear in the input. Existing safety training methods largely fail to address this vulnerability, due to the inherent difficulty of uncovering hidden triggers implanted in the model. Motivated by recent findings on LLMs’ situational awareness, we propose a novel post-training framework that cultivates self-awareness of backdoor risks and enables models to articulate implanted triggers even when
they are absent from the prompt. At its core, our approach introduces an inversion-inspired reinforcement learning framework that encourages models to introspectively reason about their own behaviors and reverse-engineer the triggers responsible for misaligned outputs. Guided by curated reward signals, this process transforms a poisoned model into one capable of precisely identifying its implanted trigger. Surprisingly, we observe that such backdoor self-awareness emerges abruptly within a short training window, resembling a phase transition in capability. Building on this emergent property, we further present two complementary defense strategies for mitigating and detecting backdoor threats. Experiments on five backdoor attacks, compared against six baseline methods, demonstrate that our approach has strong potential to improve the robustness of LLMs against backdoor risks.

## item_id: m_0386

TITLE: VisualCoder: Guiding Vision Language Models in Code Execution with Fine-grained Chain-of-Thought Reasoning

ABSTRACT: Predicting program behavior and reasoning about code execution remain significant challenges in software engineering, particularly for large language models (LLMs) designed for code analysis. While these models excel at understanding static syntax, they often struggle with dynamic reasoning tasks. We introduce VisualCoder, a novel approach that enhances code reasoning by integrating multimodal Chain-of-Thought (CoT) reasoning with visual Control Flow Graphs (CFGs). By aligning code snippets with their corresponding CFGs, VisualCoder provides deeper insights into execution flow, enabling more accurate predictions of code behavior. Our experiments demonstrate that augmenting LLMs with visual CFGs significantly outperforms text-based CFG descriptions in code reasoning tasks. We address challenges in multimodal CoT integration through a reference mechanism, ensuring consistency between code and its execution path, thereby improving performance in program behavior prediction, error detection, and output generation.

## item_id: m_0387

TITLE: TIME-LAPSE: Learning to say “I don't know” through spatio-temporal uncertainty scoring

ABSTRACT: Safe deployment of trained ML models requires determining when input samples go out-of-distribution (OOD) and refraining from making uncertain predictions on them. Existing approaches inspect test samples in isolation to estimate their corresponding predictive uncertainty. However, in the real-world, deployed models typically see test inputs consecutively and predict labels continuously over time during inference. In this work, we propose TIME-LAPSE, a spatio-temporal framework for uncertainty scoring that examines the sequence of predictions prior to the current sample to determine its predictive uncertainty. Our key insight is that in-distribution samples will be more “similar” to each other compared to OOD samples, not just over the encoding latent-space but also across time. Specifically, (a) our spatial uncertainty score estimates how different OOD latent-space representations are from those of an in-distribution set using metrics such as Mahalanobis distance and cosine similarity and (b) our temporal uncertainty score determines deviations in correlations over time using representations of past inputs in a non-parametric, sliding-window based algorithm. We evaluate TIME-LAPSE on both audio and vision tasks using public datasets and further benchmark our approach on a challenging, real-world, electroencephalograms (EEG) dataset for seizure detection. We achieve state-of-the-art results for OOD detection in the audio and EEG domain and observe considerable gains in semantically corrected vision benchmarks. We show that TIME-LAPSE is more driven by semantic content compared to other methods, i.e., it is more robust to dataset statistics. We also propose a sequential OOD detection evaluation framework to emulate real-life drift settings and show that TIME-LAPSE outperforms spatial methods significantly.  

## item_id: m_0388

TITLE: Classically Approximating Variational Quantum Machine Learning with Random Fourier Features

ABSTRACT: Many applications of quantum computing in the near term rely on variational quantum circuits (VQCs). They have been showcased as a promising model for reaching a quantum advantage in machine learning with current noisy intermediate scale quantum computers (NISQ). It is often believed that the power of VQCs relies on their exponentially large feature space, and extensive works have explored the expressiveness and trainability of VQCs in that regard. In our work, we propose a classical sampling method that can closely approximate most VQCs with Hamiltonian encoding, given only the description of their architecture. It uses the seminal proposal of Random Fourier Features (RFF) and the fact that VQCs can be seen as large Fourier series. We show theoretically and experimentally that models built from exponentially large quantum feature space can be classically reproduced by sampling a few frequencies to build an equivalent low dimensional kernel. Precisely, we show that the number of required samples grows favourably with the size of the quantum spectrum. This tool therefore questions the hope for quantum advantage from VQCs in many cases, but conversely helps to narrow the conditions for their potential success. We expect VQCs with various and complex encoding Hamiltonians, or with large input dimension, to become more robust to classical approximations.

## item_id: m_0389

TITLE: A Teacher Student Network For Faster Video Classification

ABSTRACT: Over the past few years, various tasks involving videos such as classification, description, summarization and question answering have received a lot of attention. Current models for these tasks compute an encoding of the video by treating it as a sequence of images and going over every image in the sequence, which becomes computationally expensive for longer videos. In this paper, we focus on the task of video classification and aim to reduce the computational cost by using the idea of distillation. Specifically, we propose a Teacher-Student network wherein the teacher looks at all the frames in the video but the student looks at only a small fraction of the frames in the video. The idea is to then train the student to minimize  (i)  the difference between the final representation computed by the student and the teacher and/or (ii) the difference between the distributions predicted by the teacher and the student. This smaller student network which involves fewer computations but still learns to mimic the teacher can then be employed at inference time for video classification. We experiment with the YouTube-8M dataset and show  that the proposed student network can reduce the inference time by upto 30% with a negligent drop in the performance. 

## item_id: m_0390

TITLE: Neural Network Cost Landscapes as Quantum States

ABSTRACT: Quantum computers promise significant advantages over classical computers for a number of different applications. We show that the complete loss function landscape of a neural network can be represented as the quantum state output by a quantum computer. We demonstrate this explicitly for a binary neural network and, further, show how a quantum computer can train the network by manipulating this state using a well-known algorithm known as quantum amplitude amplification. We further show that with minor adaptation, this method can also represent the meta-loss landscape of a number of neural network architectures simultaneously. We search this meta-loss landscape with the same method to simultaneously train and design a binary neural network. 

## item_id: m_0391

TITLE: Predicting the Generalization Gap in Deep Networks with Margin Distributions

ABSTRACT: As shown in recent research, deep neural networks can perfectly fit randomly labeled data, but with very poor accuracy on held out data. This phenomenon indicates that loss functions such as cross-entropy are not a reliable indicator of generalization. This leads to the crucial question of how generalization gap should be predicted from the training data and network parameters. In this paper, we propose such a measure, and conduct extensive empirical studies on how well it can predict the generalization gap. Our measure is based on the concept of margin distribution, which are the distances of training points to the decision boundary. We find that it is necessary to use margin distributions at multiple layers of a deep network. On the CIFAR-10 and the CIFAR-100 datasets, our proposed measure correlates very strongly with the generalization gap. In addition, we find the following other factors to be of importance: normalizing margin values for scale independence, using characterizations of margin distribution rather than just the margin (closest distance to decision boundary), and working in log space instead of linear space (effectively using a product of margins rather than a sum).
Our measure can be easily applied to feedforward deep networks with any architecture and may point towards new training loss functions that could enable better generalization.

## item_id: m_0392

TITLE: Dynamic Token Normalization improves Vision Transformers

ABSTRACT: Vision Transformer (ViT) and its variants (e.g., Swin, PVT) have achieved great success in various computer vision tasks, owing to their capability to learn long-range contextual information. Layer Normalization (LN) is an essential ingredient in these models. However, we found that the ordinary LN  makes tokens at different positions similar in magnitude because it normalizes embeddings within each token. It is difficult for Transformers to capture inductive bias such as the positional context in an image with LN. We tackle this problem by proposing a new normalizer, termed Dynamic Token Normalization (DTN), where normalization is performed both within each token (intra-token) and across different tokens (inter-token). DTN has several merits. Firstly, it is built on a unified formulation and thus can represent various existing normalization methods. Secondly, DTN learns to normalize tokens in both intra-token and inter-token manners, enabling Transformers to capture both the global contextual information and the local positional context. Thirdly, by simply replacing LN layers, DTN can be readily plugged into various vision transformers, such as ViT, Swin, and PVT. Extensive experiments show that the transformer equipped with DTN consistently outperforms baseline model with minimal extra parameters and computational overhead. For example, DTN outperforms LN on small ViT by $1.1\%$ top-1 accuracy on ImageNet.

## item_id: m_0393

TITLE: Generalization of GANs and overparameterized models under Lipschitz continuity

ABSTRACT: Generative adversarial networks (GANs)  are really complex, and  little has been known about their generalization. The existing learning theories lack efficient tools to analyze generalization of GANs. To fill this gap, we introduce a novel tool to analyze generalization: Lipschitz continuity. We demonstrate its simplicity by showing generalization and consistency of overparameterized neural networks. We then use this tool to derive Lipschitz-based generalization bounds for GANs. In particular, our bounds show that penalizing the zero- and first-order informations of the GAN loss will improve generalization. Therefore, this work provides a unified theory for answering the long mystery of why imposing a Lipschitz constraint can help GANs to generalize well in practice. 

## item_id: m_0394

TITLE: Test-Time Training on Nearest Neighbors for Large Language Models

ABSTRACT: Many recent efforts augment language models with retrieval, by adding retrieved data to the input context. For this approach to succeed, the retrieved data must be added at both training and test time. Moreover, as input length grows linearly with the size of retrieved data, cost in computation and memory grows quadratically for modern Transformers. To avoid these complications, we simply fine-tune the model on retrieved data at test time, using its standard training setup. We build a large-scale distributed index based on text embeddings of the Pile dataset. For each test input, our system retrieves its neighbors and fine-tunes the model on their text. Surprisingly, retrieving and training on as few as 20 neighbors, each for only one gradient iteration, drastically improves performance across more than 20 language modeling tasks in the Pile. For example, test-time training with nearest neighbors significantly narrows the performance gap between a small GPT-2 and a GPT-Neo model more than 10 times larger. Sufficient index quality and size, however, are necessary. Our work establishes a first baseline of test-time training for language modeling.

## item_id: m_0395

TITLE: Function Space Particle Optimization for Bayesian Neural Networks

ABSTRACT: While Bayesian neural networks (BNNs) have drawn increasing attention, their posterior inference remains challenging, due to the high-dimensional and over-parameterized nature. To address this issue, several highly flexible and scalable variational inference procedures based on the idea of particle optimization have been proposed. These methods directly optimize a set of particles to approximate the target posterior. However, their application to BNNs often yields sub-optimal performance, as such methods have a particular failure mode on over-parameterized models. In this paper, we propose to solve this issue by performing particle optimization directly in the space of regression functions. We demonstrate through extensive experiments that our method successfully overcomes this issue, and outperforms strong baselines in a variety of tasks including prediction, defense against adversarial examples, and reinforcement learning.

## item_id: m_0396

TITLE: Learning to Attend On Essential Terms: An Enhanced Retriever-Reader Model for Open-domain Question Answering

ABSTRACT: Open-domain question answering remains a challenging task as it requires models that are capable of understanding questions and answers, collecting useful information, and reasoning over evidence. Previous work typically formulates this task as a reading comprehension or entailment problem given evidence retrieved from search engines. However, existing techniques struggle to retrieve indirectly related evidence when no directly related evidence is provided, especially for complex questions where it is hard to parse precisely what the question asks. In this paper we propose a retriever-reader model that learns to attend on essential terms during the question answering process. We build (1) an essential term selector which first identifies the most important words in a question, then reformulates the query and searches for related evidence; and (2) an enhanced reader that distinguishes between essential terms and distracting words to predict the answer. We evaluate our model on multiple open-domain QA datasets where it outperforms the existing state-of-the-art, notably leading to an improvement of 8.1% on the AI2 Reasoning Challenge (ARC) dataset.

## item_id: m_0397

TITLE: TaskSet: A Dataset of Optimization Tasks

ABSTRACT: We present TaskSet, a dataset of tasks for use in training and evaluating optimizers. TaskSet is unique in its size and diversity, containing over a thousand tasks ranging from image classification with fully connected or convolutional neural networks, to variational autoencoders, to non-volume preserving flows on a variety of datasets. As an example application of such a dataset we explore meta-learning an ordered list of hyperparameters to try sequentially. By learning this hyperparameter list from data generated using TaskSet we achieve large speedups in sample efficiency over random search. Next we use the diversity of the TaskSet and our method for learning hyperparameter lists to empirically explore the generalization of these lists to new optimization tasks in a variety of settings including ImageNet classification with Resnet50 and LM1B language modeling with transformers. As part of this work we have opensourced code for all tasks, as well as ~29 million training curves for these problems and the corresponding hyperparameters.

## item_id: m_0398

TITLE: Learn from Known Unknowns: A Unified Empirical Bayesian Framework for Improving Group Robustness

ABSTRACT: The lack of group robustness has emerged as a critical concern in machine learning, as conventional methods like Empirical Risk Minimization (ERM) can achieve high overall accuracy while yielding low worst-group accuracy in minority groups. This issue often stems from spurious correlations—non-essential features that models exploit as shortcuts—which can compromise deep learning models in high-stakes applications. Previous works have found that simply retraining classifiers with reweighted datasets or rebalanced samples could significantly improve robustness. However, existing methods lack a unified framework, as they often exhibit inconsistent performance across datasets, and sometimes rely heavily on hyperparameter tuning, making them impractical for real-world datasets. In this work, we first argue that existing methods can be unified as one Empirical Bayesian framework, where a priori of group information is not specified. We then propose our method \textit{Learn from Known Unknowns} under this framework by quantifying the epistemic uncertainty of biased ERM models and introducing a selective reweighting technique for retraining. Our empirical results demonstrate that this approach improves group robustness across diverse datasets and reduces reliance on hyperparameter tuning, offering a more efficient and scalable solution to spurious correlations.

## item_id: m_0399

TITLE: Learning Invariant Representations for Reinforcement Learning without Reconstruction

ABSTRACT: We study how representation learning can accelerate reinforcement learning from rich observations, such as images, without relying either on domain knowledge or pixel-reconstruction. Our goal is to learn representations that provide for effective downstream control and invariance to task-irrelevant details. Bisimulation metrics quantify behavioral similarity between states in continuous MDPs, which we propose using to learn robust latent representations which encode only the task-relevant information from observations. Our method trains encoders such that distances in latent space equal bisimulation distances in state space. We demonstrate the effectiveness of our method at disregarding task-irrelevant information using modified visual MuJoCo tasks, where the background is replaced with moving distractors and natural videos, while achieving SOTA performance. We also test a first-person highway driving task where our method learns invariance to clouds, weather, and time of day. Finally, we provide generalization results drawn from properties of bisimulation metrics, and links to causal inference.

## item_id: m_0400

TITLE: Detecting Adversarial Examples by Additional Evidence from Noise Domain

ABSTRACT: Deep neural networks are widely adopted powerful tools for perceptual tasks. However, recent research indicated that they are easily fooled by adversarial examples, which are produced by adding imperceptible adversarial perturbations to clean examples. In this paper, we utilize the steganalysis rich model (SRM) to generate noise feature maps, and combine them with RGB images to discover the difference between adversarial examples and clean examples. In particular, we propose a two-stream pseudo-siamese network and train it end-to-end to detect adversarial examples. Our approach fuses the subtle difference in RGB images with the noise inconsistency in noise features. The proposed method has strong detection capability and transferability, and can be combined with any classifier without modifying its architecture or training procedure. Our extensive empirical experiments show that, compared with the state-of-the-art detection methods, the proposed method achieves excellent performance in distinguishing adversarial samples generated by popular attack methods on different real datasets. Moreover, our method has good generalization, it trained by a specific adversary can generalize to other adversaries.
