# Batch 08 — 100 items

## item_id: m_0701

TITLE: Universal Successor Features Approximators

ABSTRACT: The ability of a reinforcement learning (RL) agent to learn about many reward functions at the same time has many potential benefits, such as the decomposition of complex tasks into simpler ones, the exchange of information between tasks, and the reuse of skills. We focus on one aspect in particular, namely the ability to generalise to unseen tasks. Parametric generalisation relies on the interpolation power of a function approximator that is given the task description as input; one of its most common form are universal value function approximators (UVFAs). Another way to generalise to new tasks is to exploit structure in the RL problem itself. Generalised policy improvement (GPI) combines solutions of previous tasks into a policy for the unseen task; this relies on instantaneous policy evaluation of old policies under the new reward function, which is made possible through successor features (SFs). Our proposed \emph{universal successor features approximators} (USFAs) combine the advantages of all of these, namely the scalability of UVFAs, the instant inference of SFs, and the strong generalisation of GPI. We discuss the challenges involved in training a USFA, its generalisation properties and demonstrate its practical benefits and transfer abilities on a large-scale domain in which the agent has to navigate in a first-person perspective three-dimensional environment. 

## item_id: m_0702

TITLE: Natural Language Inference with External Knowledge

ABSTRACT: Modeling informal inference in natural language is very challenging. With the recent availability of large annotated data, it has become feasible to train complex models such as neural networks to perform natural language inference (NLI), which have achieved state-of-the-art performance. Although there exist relatively large annotated data, can machines learn all knowledge needed to perform NLI from the data? If not, how can NLI models benefit from external knowledge and how to build NLI models to leverage it? In this paper, we aim to answer these questions by enriching the state-of-the-art neural natural language inference models with external knowledge. We demonstrate that the proposed models with external knowledge further improve the state of the art on the Stanford Natural Language Inference (SNLI) dataset. 

## item_id: m_0703

TITLE: HighRes-net: Multi-Frame Super-Resolution by Recursive Fusion

ABSTRACT: Generative deep learning has sparked a new wave of Super-Resolution (SR) algorithms that enhance single images with impressive aesthetic results, albeit with imaginary details. Multi-frame Super-Resolution (MFSR) offers a more grounded approach to the ill-posed problem, by conditioning on multiple low-resolution views. This is important for satellite monitoring of human impact on the planet -- from deforestation, to human rights violations -- that depend on reliable imagery. To this end, we present HighRes-net, the first deep learning approach to MFSR that learns its sub-tasks in an end-to-end fashion: (i) co-registration, (ii) fusion, (iii) up-sampling, and (iv) registration-at-the-loss. Co-registration of low-res views is learned implicitly through a reference-frame channel, with no explicit registration mechanism. We learn a global fusion operator that is applied recursively on an arbitrary number of low-res pairs. We introduce a registered loss, by learning to align the SR output to a ground-truth through ShiftNet. We show that by learning deep representations of multiple views, we can super-resolve low-resolution signals and enhance Earth observation data at scale. Our approach recently topped the European Space Agency's MFSR competition on real-world satellite imagery.

## item_id: m_0704

TITLE: PALM: Preference-based Adversarial Manipulation against Deep Reinforcement Learning

ABSTRACT: To improve the robustness of DRL agents, it is important to study their vulnerability under  adversarial attacks that would lead to extreme behaviors desired by adversaries. Preference-based RL (PbRL) aims for learning desired behaviors with human preferences. In this paper, we propose PALM, a preference-based adversarial manipulation method against DRL agents  which adopts human preferences to perform targeted attacks with the assistance of an intention policy and a weighting function. The intention policy is trained based on the PbRL framework to guide the adversarial policy  to mitigate restrictions of the victim policy during exploration, and the weighting function learns weight assignment to improve the performance of the adversarial policy. Theoretical analysis demonstrates that PALM converges to critical points under some mild conditions. Empirical results on a few manipulation tasks of Meta-world show that PALM exceeds the performance of state-of-the-art adversarial attack methods under the targeted setting. Additionally, we show the vulnerability of the offline RL agents by fooling them into behaving as human desires on several Mujoco tasks. Our code and videos are available in https://sites.google.com/view/palm-adversarial-attack.

## item_id: m_0705

TITLE: ULF: UNSUPERVISED LABELING FUNCTION CORRECTION USING CROSS-VALIDATION FOR WEAK SUPERVISION

ABSTRACT: A way to overcome expensive and time-consuming manual data labeling is weak supervision - automatic annotation of data samples via a predefined set of labeling functions (LFs), rule-based mechanisms that generate artificial labels for the classes associated with the LFs. In this work, we investigate noise reduction techniques for weak supervision based on the principle of k-fold cross-validation. We introduce a new algorithm ULF for denoising weakly annotated data which uses models trained on all but some LFs to detect and correct biases specific to the held-out LFs. Specifically, ULF refines the allocation of LFs to classes by re-estimating this assignment on highly reliable cross-validated samples. We realize two variants of this algorithm: feature-based ULF (relying on count-based feature vectors), and DeepULF (fine-tuning pre-trained language models). We compare ULF to methods originally developed for detecting erroneous samples in manually annotated data, as well as to our extensions of such methods to the weakly supervised setting. Our new weak supervision-specific methods (ULF and extensions) leverage the information about matching LFs, making detecting noisy samples more accurate. Evaluation on several datasets shows that ULF can successfully improve weakly supervised learning without utilizing any manually labeled data.

## item_id: m_0706

TITLE: Neural Program Lattices

ABSTRACT: We propose the Neural Program Lattice (NPL), a neural network that learns to perform complex tasks by composing low-level programs to express high-level programs. Our starting point is the recent work on Neural Programmer-Interpreters (NPI), which can only learn from strong supervision that contains the whole hierarchy of low-level and high-level programs. NPLs remove this limitation by providing the ability to learn from weak supervision consisting only of sequences of low-level operations. We demonstrate the capability of NPL to learn to perform long-hand addition and arrange blocks in a grid-world environment. Experiments show that it performs on par with NPI while using weak supervision in place of most of the strong supervision, thus indicating its ability to infer the high-level program structure from examples containing only the low-level operations.

## item_id: m_0707

TITLE: Stackelberg GAN: Towards Provable Minimax Equilibrium via Multi-Generator Architectures

ABSTRACT: We study the problem of alleviating the instability issue in the GAN training procedure via new architecture design. The discrepancy between the minimax and maximin objective values could serve as a proxy for the difficulties that the alternating gradient descent encounters in the optimization of GANs. In this work, we give new results on the benefits of multi-generator architecture of GANs. We show that the minimax gap shrinks to \epsilon as the number of generators increases with rate O(1/\epsilon). This improves over the best-known result of O(1/\epsilon^2). At the core of our techniques is a novel application of Shapley-Folkman lemma to the generic minimax problem, where in the literature the technique was only known to work when the objective function is restricted to the Lagrangian function of a constraint optimization problem. Our proposed Stackelberg GAN performs well experimentally in both synthetic and real-world datasets, improving Frechet Inception Distance by 14.61% over the previous multi-generator GANs on the benchmark datasets.

## item_id: m_0708

TITLE: Uncertainty Estimation and Calibration with Finite-State Probabilistic RNNs

ABSTRACT: Uncertainty quantification is crucial for building reliable and trustable machine learning systems. We propose to estimate uncertainty in recurrent neural networks (RNNs) via stochastic discrete state transitions over recurrent timesteps. The uncertainty of the model can be quantified by running a prediction several times, each time sampling from the recurrent state transition distribution, leading to potentially different results if the model is uncertain. Alongside uncertainty quantification, our proposed method offers several advantages in different settings. The proposed method can (1) learn deterministic and probabilistic automata from data, (2) learn well-calibrated models on real-world classification tasks, (3) improve the performance of out-of-distribution detection, and (4) control the exploration-exploitation trade-off in reinforcement learning. An implementation is available.

## item_id: m_0709

TITLE: Latent Causal Invariant Model

ABSTRACT: Current supervised learning can learn spurious correlation during the data-fitting process, imposing issues regarding interpretability, out-of-distribution (OOD) generalization, and robustness. To avoid spurious correlation, we propose a \textbf{La}tent \textbf{C}ausal \textbf{I}nvariance \textbf{M}odel (LaCIM) which pursues \emph{causal prediction}. Specifically, we introduce latent variables that are separated into (a) output-causative factors and (b) others that are spuriously correlated to the output via confounders, to model the underlying causal factors. We further assume the generating mechanisms from latent space to observed data to be \emph{causally invariant}. We give the identifiable claim of such invariance, particularly the disentanglement of output-causative factors from others, as a theoretical guarantee for precise inference and avoiding spurious correlation. We propose a Variational-Bayesian-based method for estimation and to optimize over the latent space for prediction. The utility of our approach is verified by improved interpretability, prediction power on various OOD scenarios (including healthcare) and robustness on security. 

## item_id: m_0710

TITLE: TANGOS: Regularizing Tabular Neural Networks through Gradient Orthogonalization and Specialization

ABSTRACT: Despite their success with unstructured data, deep neural networks are not yet a panacea for structured tabular data. In the tabular domain, their efficiency crucially relies on various forms of regularization to prevent overfitting and provide strong generalization performance. Existing regularization techniques include broad modelling decisions such as choice of architecture, loss functions, and optimization methods. In this work, we introduce Tabular Neural Gradient Orthogonalization and Specialization (TANGOS), a novel framework for regularization in the tabular setting built on latent unit attributions. The gradient attribution of an activation with respect to a given input feature suggests how the neuron attends to that feature, and is often employed to interpret the predictions of deep networks. In TANGOS, we take a different approach and incorporate neuron attributions directly into training to encourage orthogonalization and specialization of latent attributions in a fully-connected network. Our regularizer encourages neurons to focus on sparse, non-overlapping input features and results in a set of diverse and specialized latent units. In the tabular domain, we demonstrate that our approach can lead to improved out-of-sample generalization performance, outperforming other popular regularization methods. We provide insight into why our regularizer is effective and demonstrate that TANGOS can be applied jointly with existing methods to achieve even greater generalization performance.

## item_id: m_0711

TITLE: Cross Domain Ensemble Distillation for Domain Generalization

ABSTRACT: For domain generalization, the task of learning a model that generalizes to unseen target domains utilizing multiple source domains, many approaches explicitly align the distribution of the domains.  However, the optimization for domain alignment has a risk of overfitting since the target domain is not available. To address the issue, this paper proposes a method for domain generalization by employing self-distillation. The proposed method aims to train a model robust to domain shift by allowing meaningful erroneous predictions in multiple domains. Specifically, our method matches the ensemble of predictive distributions of data with the same class label but different domains with each predictive distribution. We also propose a de-stylization method that standardizes feature maps of images to help produce consistent predictions. Image classification experiments on two benchmarks demonstrated that the proposed method greatly improves performance in both single-source and multi-source settings. We also show that the proposed method works effectively in person-reID experiments. In all experiments, our method significantly improves the performance.

## item_id: m_0712

TITLE: Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification

ABSTRACT: Test-time compute can be scaled both sequentially and in parallel. Sequential scaling involves lengthening the generation process, while parallel scaling involves verifying and selecting among multiple candidate outputs. Combining these two strategies has led to the most powerful AI systems, such as Grok 4 Heavy, GPT-5 Pro, and Gemini-2.5 Pro Deep Think. A key observation is that, in certain contexts (e.g., solving Sudoku puzzles), verifying responses can be substantially easier than generating them. This property, referred to as \emph{asymmetric verification}, highlights the strong potential of test-time scaling. In this work, we study both sequential and parallel test-time scaling of deep search agents, motivated by the intuition that verification in this setting is often much easier than generation. In experiments, we first show that sequential scaling methods, such as budget forcing, can be effective initially but eventually degrade performance when over-applied in agentic search. Due to asymmetric verification, however, we are able to achieve substantial improvements by allocating only a modest amount of compute to the verifier. We conduct experiments with flagship open-source models, including GLM-4.5, K2, Qwen3-2507 and Tongyi-DeepResearch, and extend them to their ``Heavy'' variants through test-time scaling. These deep research agents achieve improvements of up to 20 absolute points on benchmarks such as BrowseComp. Remarkably, as an open-source alternative, GLM-4.5 Heavy reaches accuracy of {\bf 54.0\%} on BrowseComp, {\bf 66.0\%} on GAIA, and {\bf 68.0\%} on xbench-DeepSearch, placing it on par with the best proprietary choices such as OpenAI Deep Research and o3. Tongyi-DeepResearch Heavy pushes performance even further, attaining {\bf 69.0\%} accuracy on BrowseComp.

## item_id: m_0713

TITLE: ATTENTION-GUIDED DEEP ADVERSARIAL TEMPORAL SUBSPACE CLUSTERING FOR MULTIVARIATE SPATIOTEMPORAL DATA

ABSTRACT: Deep subspace clustering models provide an efficient solution to the problem of unsupervised subspace clustering of non-linear high-dimensional spatiotemporal data. These clustering solutions are often needed in applications such as motion segmentation, tracking ice sheet dynamics, and detecting anomalous melting events where high-dimensional data exhibit complex temporal dependencies and lie on multiple non-linear manifolds that cannot be effectively captured by traditional linear clustering methods. Existing deep clustering models learn non-linear mappings by projecting data into a latent space in which data lie in linear subspaces and exploit the self-expressiveness property. While this approach has shown impressive performance, they have shortcomings. First, they employ "shallow" autoencoders that completely rely on the self-expressiveness of latent features and disregard potential clustering errors. Second, they focus solely on global features while overlooking local features in subspace self-expressiveness learning. Third, they do not capture long-range dependencies or positional information, both of which are crucial for effective spatial and temporal feature extraction and often lead to sub-optimal clustering outcomes. Fourth, their application to 4D multivariate spatiotemporal data remains underexplored. To address these limitations, we propose a novel Attention-Guided Deep Adversarial Subspace Clustering (A-DATSC) for multivariate spatiotemporal data. A-DATSC incorporates a deep subspace clustering generator and a quality-verifying discriminator that work in tandem. Inspired by the U-Net architecture, the generator preserves the spatial and time-wise structural integrity, reduces the number of trainable parameters, and improves generalization through the use of stacked TimeDistributed ConvLSTM2D layers. The generator introduces a graph attention transformer-based self-expressive network which captures local spatial relationships, global dependencies, and both short- and long-range correlations crucial for understanding how distant regions and time periods influence each other. When evaluated on three real-world multivariate spatiotemporal datasets, A-DATSC outperforms state-of-the-art shallow and deep subspace clustering models with significant margins.

## item_id: m_0714

TITLE: Learn Goal-Conditioned Policy with Intrinsic Motivation for Deep Reinforcement Learning

ABSTRACT: It is of significance for an agent to learn a widely applicable and general-purpose policy that can achieve diverse goals including images and text descriptions.  Considering such perceptually-specific goals, the frontier of deep reinforcement learning research is to learn a goal-conditioned policy without hand-crafted rewards. To learn this kind of policy, recent works usually take as the reward the non-parametric distance to a given goal in an explicit embedding space. From a different viewpoint, we propose a novel unsupervised learning approach named goal-conditioned policy with intrinsic motivation (GPIM), which jointly learns both an abstract-level policy and a goal-conditioned policy. The abstract-level policy is conditioned on a latent variable to optimize a discriminator and discovers diverse states that are further rendered into perceptually-specific goals for the goal-conditioned policy. The learned discriminator serves as an intrinsic reward function for the goal-conditioned policy to imitate the trajectory induced by the abstract-level policy.  Experiments on various robotic tasks demonstrate the effectiveness and efficiency of our proposed GPIM method which substantially outperforms prior techniques. 

## item_id: m_0715

TITLE: Part-Aware CLIP: Enhancing Fine-Grained Understanding with Part-level Descriptions

ABSTRACT: Vision-Language Pre-trained (VLP) models, such as CLIP, learn powerful representations from large-scale image-text pairs, achieving remarkable zero-shot capabilities. However, by learning to align visual and textual features only at a global level, these models exhibit two critical limitations: poor interpretability and weak fine-grained perception. This deficiency arises from the pre-training data that overlooks key visual details of object parts, which are often important for distinguishing between subordinate categories (e.g., species of birds or models of cars). This fundamental weakness is inherited by Multimodal Large Language Models (MLLMs) that use CLIP-based vision encoders, limiting both their accuracy and trustworthiness. To address these challenge, we introduce Part-Aware CLIP (PA-CLIP), a framework designed to enhance both the fine-grained perception and interpretability of VLP models. First, we employs MLLMs to create a new dataset FG-Part, including approximately 1 million part-level image-text pairs. FG-Part explicitly captures the critical visual details of object components (e.g., a bird's beak and wing patterns). Second, we design a part-aware training strategy that leverages this curated data to compel the model to ground fine-grained textual descriptions in specific image regions. By forcing this explicit, part-level alignment, our method enhances the model's ability to perceive key details, thereby improving its fine-grained recognition capabilities and inherent interpretability. Extensive experiments show that PA-CLIP achieves state-of-the-art performance on multiple fine-grained visual recognition (FGVR) benchmarks, highlighting the effectiveness of part-level captions and the capabilities of PA-CLIP in capturing subtle visual details. Furthermore, evaluations on general tasks, including cross-modal retrieval, confirm that these gains do not compromise the model's core generalist capabilities.

## item_id: m_0716

TITLE: GRABLI: Cross-Modal Knowledge Graph Alignment for Biomedical Language Models

ABSTRACT: Pre-trained Language Models (LMs) have given a significant performance growth in a variety of language-related texts in biomedical domain. However, existing biomedical LLMs demonstrate a limited understanding of complex, domain-specific concept structure and the factual information stored in biomedical Knowledge Graphs (KGs). We propose \textbf{GRABLI} (Knowledge \textbf{Gra}ph and \textbf{B}iomedical Language Model A\textbf{li}gnment), a novel pre-training method that enriches an LM with external knowledge by simultaneously learning a separate KG encoder and aligning LM and graph representations. Given a textual sequence, we normalize biomedical concept mentions to the Unified Medical Language System (UMLS) KG and use the local KG subgraphs as cross-modal positive samples for mentioned concepts. Our empirical results demonstrate that applying our proposed method to various state-of-the-art biomedical LMs including PubMedBERT and BioLinkBERT, enhances their performance on diverse language understanding tasks, even after brief pre-training on a small alignment dataset derived from PubMed scientific abstracts.

## item_id: m_0717

TITLE: Training-Free Diffusion Model Alignment with Sampling Demons

ABSTRACT: Aligning diffusion models with user preferences has been a key challenge.
Existing methods for aligning diffusion models either require retraining or are limited to differentiable reward functions.
To address these limitations, we propose a stochastic optimization approach, dubbed *Demon*, to guide the denoising process at inference time without backpropagation through reward functions or model retraining.
Our approach works by controlling noise distribution in denoising steps to concentrate density on regions corresponding to high rewards through stochastic optimization.
We provide comprehensive theoretical and empirical evidence to support and validate our approach, including experiments that use non-differentiable sources of rewards such as Visual-Language Model (VLM) APIs and human judgements.
To the best of our knowledge, the proposed approach is the first inference-time, backpropagation-free preference alignment method for diffusion models.
Our method can be easily integrated with existing diffusion models without further training.
Our experiments show that the proposed approach significantly improves the average aesthetics scores for text-to-image generation. Implementation is available at [this URL](https://github.com/aiiu-lab/DemonSampling).

## item_id: m_0718

TITLE: Accelerated Sparse Recovery Under Structured Measurements

ABSTRACT: Extensive work on compressed sensing has yielded a rich collection of sparse recovery algorithms, each making different tradeoffs between recovery condition and computational efficiency. In this paper, we propose a unified framework for accelerating various existing sparse recovery algorithms without sacrificing recovery guarantees by exploiting structure in the measurement matrix. Unlike fast algorithms that are specific to particular choices of measurement matrices where the columns are Fourier or wavelet filters for example, the proposed approach works on a broad range of measurement matrices that satisfy a particular property. We precisely characterize this property, which quantifies how easy it is to accelerate sparse recovery for the measurement matrix in question. We also derive the time complexity of the accelerated algorithm, which is sublinear in the signal length in each iteration. Moreover, we present experimental results on real world data that demonstrate the effectiveness of the proposed approach in practice. 

## item_id: m_0719

TITLE: Multi-Class Uncertainty Calibration via Mutual Information Maximization-based Binning

ABSTRACT: Post-hoc multi-class calibration is a common approach for providing high-quality confidence estimates of deep neural network predictions. Recent work has shown that widely used scaling methods underestimate their calibration error, while alternative Histogram Binning (HB) methods often fail to preserve classification accuracy. When classes have small prior probabilities, HB also faces the issue of severe sample-inefficiency after the conversion into K one-vs-rest class-wise calibration problems. The goal of this paper is to resolve the identified issues of HB in order to provide calibrated confidence estimates using only a small holdout calibration dataset for bin optimization while preserving multi-class ranking accuracy. From an information-theoretic perspective, we derive the I-Max concept for binning, which maximizes the mutual information between labels and quantized logits. This concept mitigates potential loss in ranking performance due to lossy quantization, and by disentangling the optimization of bin edges and representatives allows simultaneous improvement of ranking and calibration performance. To improve the sample efficiency and estimates from a small calibration set, we propose a shared class-wise (sCW) calibration strategy, sharing one calibrator among similar classes (e.g., with similar class priors) so that the training sets of their class-wise calibration problems can be merged to train the single calibrator. The combination of sCW and I-Max binning outperforms the state of the art calibration methods on various evaluation metrics across different benchmark datasets and models, using a small calibration set (e.g., 1k samples for ImageNet).

## item_id: m_0720

TITLE: Inducing Grammars with and for Neural Machine Translation

ABSTRACT: Previous work has demonstrated the benefits of incorporating additional linguistic annotations such as syntactic trees into neural machine translation. However the cost of obtaining those syntactic annotations is expensive for many languages and the quality of unsupervised learning linguistic structures is too poor to be helpful. In this work, we aim to improve neural machine translation via source side dependency syntax but without explicit annotation. We propose a set of models that learn to induce dependency trees on the source side and learn to use that information on the target side. Importantly, we also show that our dependency trees capture important syntactic features of language and improve translation quality on two language pairs En-De and En-Ru.

## item_id: m_0721

TITLE: State-Regularized Recurrent Networks

ABSTRACT: Recurrent networks are a widely used class of neural architectures.  They have, however, two shortcomings. First, it is difficult to understand what exactly they learn. Second, they tend to work poorly on sequences requiring long-term memorization, despite having this capacity in principle. We aim to address both shortcomings with a class of recurrent networks that use a stochastic state transition mechanism between cell applications. This mechanism, which we term state-regularization, makes RNNs transition between a finite set of learnable states. We show that state-regularization (a) simplifies the extraction of finite state automata modeling an RNN's state transition dynamics, and (b) forces RNNs to operate more like automata with external memory and less like finite state machines.

## item_id: m_0722

TITLE: Revisiting Loss Modelling for Unstructured Pruning

ABSTRACT: By removing parameters from deep neural networks, unstructured pruning methods aim at cutting down memory footprint and computational cost, while maintaining prediction accuracy. In order to tackle this otherwise intractable problem, many of these methods model the loss landscape using first or second order Taylor expansions to identify which parameters can be discarded. We revisit loss modelling for unstructured pruning: we show the importance of ensuring locality of the pruning steps, and systematically compare first and second order Taylor expansions. Finally, we show that better preserving the original network function does not necessarily transfer to better performing networks after fine-tuning, suggesting that only considering the impact of pruning on the loss might not be a sufficient objective to design good pruning criteria.

## item_id: m_0723

TITLE: Nüwa: Mending the Spatial Integrity Torn by VLM Token Pruning

ABSTRACT: Vision token pruning has proven to be an effective acceleration technique for the Efficient Vision Language Model (VLM). However, existing pruning methods demonstrate excellent performance preservation in visual question answering (VQA) and suffer substantial degradation on visual grounding (VG) tasks. Our analysis of the VLM’s processing pipeline reveals that strategies utilizing global semantic similarity and attention scores lose the global spatial reference frame, which is derived from the interactions of tokens' positional information. Motivated by these findings, we propose N\"uwa, a two-stage token pruning framework that enables efficient feature aggregation while maintaining spatial integrity. In the first stage, after the vision encoder, we apply three operations, namely separation, alignment, and aggregation, which are inspired by swarm intelligence algorithms to retain information-rich global spatial anchors. In the second stage, within the LLM, we perform text-guided pruning to retain task-relevant visual tokens. Extensive experiments demonstrate that N\"uwa achieves state-of-the-art performance on multiple VQA benchmarks (from 94\% to 95\%) and yields substantial improvements on visual grounding tasks (from 7\% to 47\%). Code is released.

## item_id: m_0724

TITLE: Matrix factorization under the constraint of connectivity between observed and source data ~ Muscle synergy analysis based on connectivity between muscle and brain activities ~

ABSTRACT: Matrix factorization is a popular method to investigate the hidden elements in observed data for tasks such as speech separation and muscle synergy analysis. The hidden elements may be closely related to the source phenomenon that cause the observed phenomenon. 
 However, conventional methods do not always factorize the observed phenomenon elements with the connectivity between the observed and source phenomena because they only use the observed phenomenon. This paper proposes a matrix decomposition method that constrains the connectivity between observed and source data by using the representations from a decoding model from source data to observed data. We applied our method to the corticomuscular system, which is made up of corticospinal pathways between the primary motor cortex and muscles in the body and creates muscle synergies that enable efficient connections between the brain and muscles. In this context, muscle activities are the observed phenomenon and brain activities are the source. Many previous studies have analyzed muscle synergies using only observed muscle activity, but there may be unrevealed muscle synergies under the constraint of the connectivity between brain and muscle activity. We therefore simultaneously recorded the brain activity from multiple regions of an extensive cortical area and the activity of multiple muscles of a monkey's forelimb while it performed a reach and grasp task throughout the course of recovery from a partial spinal cord injury (SCI). Analysis from a dataset of the monkey before SCI showed that some of the muscle synergies calculated from the proposed method using brain and muscle activities, did not exhibit a high degree of similarity to synergies obtained from the conventional method. The proposed method results obtained from the monkey after SCI showed an adaptive change in the number of muscle synergies associated with the degree of functional recovery. Specifically, the numbers of muscle synergies obtained by the proposed method initially increased immediately after SCI and then gradually decreased, while those obtained by a conventional method maintained the same number before and after SCI. These results suggest that our method is able to capture the unrevealed connectivity in the corticomuscular system that contributes to functional recovery: in other words, that it can factorize the observed data under the constraint of the connectivity between the observed and source data. Our work thus demonstrates the importance of using not only observed data but also source data to reveal unknown hidden elements.

## item_id: m_0725

TITLE: Reduced-Order Neural Operators: Learning Lagrangian Dynamics on Highly Sparse Graphs

ABSTRACT: We propose accelerating the simulation of Lagrangian dynamics, such as fluid flows, granular flows, and elastoplasticity, with neural-operator-based reduced-order modeling. While full-order approaches simulate the physics of every particle within the system, incurring high computation time for dense inputs, we propose to simulate the physics on sparse graphs constructed by sampling from the spatially discretized system. Our discretization-invariant reduced-order framework trains on any spatial discretizations and computes temporal dynamics on any sparse sampling of these discretizations through neural operators. Our proposed approach is termed Graph Informed Optimized Reduced-Order Modeling or \textit{GIOROM}.  Through reduced order modeling, we ensure lower computation time by sparsifying the system by 6.6-32.0$\times$, while ensuring high-fidelity full-order inference via neural fields. We show that our model generalizes to a range of initial conditions, resolutions, and materials.

## item_id: m_0726

TITLE: QPLEX: Duplex Dueling Multi-Agent Q-Learning

ABSTRACT: We explore value-based multi-agent reinforcement learning (MARL) in the popular paradigm of centralized training with decentralized execution (CTDE). CTDE has an important concept, Individual-Global-Max (IGM) principle, which requires the consistency between joint and local action selections to support efficient local decision-making. However, in order to achieve scalability, existing MARL methods either limit representation expressiveness of their value function classes or relax the IGM consistency, which may suffer from instability risk or may not perform well in complex domains. This paper presents a novel MARL approach, called duPLEX dueling multi-agent Q-learning (QPLEX), which takes a duplex dueling network architecture to factorize the joint value function. This duplex dueling structure encodes the IGM principle into the neural network architecture and thus enables efficient value function learning. Theoretical analysis shows that QPLEX achieves a complete IGM function class. Empirical experiments on StarCraft II micromanagement tasks demonstrate that QPLEX significantly outperforms state-of-the-art baselines in both online and offline data collection settings, and also reveal that QPLEX achieves high sample efficiency and can benefit from offline datasets without additional online exploration.

## item_id: m_0727

TITLE: DeepAveragers: Offline Reinforcement Learning By Solving Derived Non-Parametric MDPs

ABSTRACT: We study an approach to offline reinforcement learning (RL) based on optimally solving  finitely-represented  MDPs  derived  from  a  static  dataset  of  experience. This approach can be applied on top of any learned representation and has the potential to easily support multiple solution objectives as well as zero-shot adjustment to changing environments and goals.  Our main contribution is to introduce the Deep Averagers with Costs MDP (DAC-MDP) and to investigate its solutions for offline RL.  DAC-MDPs are a non-parametric model that can leverage deep representations and account for limited data by introducing costs for exploiting under-represented parts of the model.  In theory, we show conditions that allow for lower-bounding the performance of DAC-MDP solutions. We also investigate the empirical behavior in a number of environments, including those with image-based observations. Overall, the experiments demonstrate that the framework can work in practice and scale to large complex offline RL problems.

## item_id: m_0728

TITLE: FINDE: Neural Differential Equations for Finding and Preserving Invariant Quantities

ABSTRACT: Many real-world dynamical systems are associated with first integrals (a.k.a. invariant quantities), which are quantities that remain unchanged over time. The discovery and understanding of first integrals are fundamental and important topics both in the natural sciences and in industrial applications. First integrals arise from the conservation laws of system energy, momentum, and mass, and from constraints on states; these are typically related to specific geometric structures of the governing equations. Existing neural networks designed to ensure such first integrals have shown excellent accuracy in modeling from data. However, these models incorporate the underlying structures, and in most situations where neural networks learn unknown systems, these structures are also unknown. This limitation needs to be overcome for scientific discovery and modeling of unknown systems. To this end, we propose first integral-preserving neural differential equation (FINDE). By leveraging the projection method and the discrete gradient method, FINDE finds and preserves first integrals from data, even in the absence of prior knowledge about underlying structures. Experimental results demonstrate that FINDE can predict future states of target systems much longer and find various quantities consistent with well-known first integrals in a unified manner.

## item_id: m_0729

TITLE: Cohen Welling bases & SO(2)-Equivariant classifiers using Tensor nonlinearity.

ABSTRACT: In this paper we propose autoencoder architectures for learning a Cohen-Welling
(CW)-basis for images and their rotations. We use the learned CW-basis to build
a rotation equivariant classifier to classify images. The autoencoder and classi-
fier architectures use only tensor product nonlinearity. The model proposed by
Cohen & Welling (2014) uses ideas from group representation theory, and extracts
a basis exposing irreducible representations for images and their rotations. We
give several architectures to learn CW-bases including a novel coupling AE archi-
tecture to learn a coupled CW-bases for images in different scales simultaneously.
Our use of tensor product nonlinearity is inspired from recent work of Kondor
(2018a). Our classifier has very good accuracy and we use fewer parameters.
Even when the sample complexity to learn a good CW-basis is low we learn clas-
sifiers which perform impressively. We show that a coupled CW-bases in one scale
can be deployed to classify images in a classifier trained and tested on images in
a different scale with only a marginal dip in performance.

## item_id: m_0730

TITLE: Robust onion: Peeling Open Vocab Object Detectors Under Noise

ABSTRACT: The impact of real-world noise on Open Vocabulary Object Detectors (OV-ODs) is constrained by their architectural complexity and the scarcity of noise-annotated datasets. Our empirical analysis, Robust Onion, uses controlled synthetic visual degradations to mirror feature collapse of real-world noises and systematically peel apart OV-OD components to assess their robustness. Our findings include: Similar vision backbones show comparable robustness, driven by identical feature collapse at similar layers. Pretraining, architectural nuances, and captions contribute little to robustness. Robustness relies strongly on the image domain rather than on annotations, explaining the similar impact of COCO and LVIS on robustness (same images, different annotations), and how datasets like ODinW-13, with large, isolated objects, can give a misleading impression of high robustness. These insights point to potential research on cross-layer feature exchange and continual learning strategies to improve robustness efficiently. Our findings highlight critical directions for designing robust OV-ODs under challenging visual degradations

## item_id: m_0731

TITLE: Boosted Generative Models

ABSTRACT: We propose a new approach for using boosting to create an ensemble of generative models, where models are trained in sequence to correct earlier mistakes. Our algorithm can leverage  many existing base learners, including recent latent variable models. Further, our approach allows the ensemble to leverage discriminative models trained to distinguish real data from model generated data. We show theoretical conditions under which incorporating a new model to the ensemble will improve the fit and empirically demonstrate the effectiveness of boosting on density estimation and sample generation on real and synthetic datasets.

## item_id: m_0732

TITLE: Adjusting for Dropout Variance in Batch Normalization and Weight Initialization

ABSTRACT: We show how to adjust for the variance introduced by dropout with corrections to weight initialization and Batch Normalization, yielding higher accuracy. Though dropout can preserve the expected input to a neuron between train and test, the variance of the input differs. We thus propose a new weight initialization by correcting for the influence of dropout rates and an arbitrary nonlinearity's influence on variance through simple corrective scalars. Since Batch Normalization trained with dropout estimates the variance of a layer's incoming distribution with some inputs dropped, the variance also differs between train and test. After training a network with Batch Normalization and dropout, we simply update Batch Normalization's variance moving averages with dropout off and obtain state of the art on CIFAR-10 and CIFAR-100 without data augmentation.

## item_id: m_0733

TITLE: Sample Efficient Actor-Critic with  Experience Replay

ABSTRACT: This paper presents an actor-critic deep reinforcement learning agent with experience replay that is stable, sample efficient, and performs remarkably well on challenging environments, including the discrete 57-game Atari domain and several continuous control problems. To achieve this, the paper introduces several innovations, including truncated importance sampling with bias correction, stochastic dueling network architectures, and a new trust region policy optimization method.

## item_id: m_0734

TITLE: EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE

ABSTRACT: Recently, generalist web agents have demonstrated remarkable potential in autonomously completing a wide range of tasks on real websites, significantly boosting human productivity. However, web tasks, such as booking flights, usually involve users' personally identifiable information (PII), which may be exposed to potential privacy risks if web agents accidentally interact with compromised websites—a scenario that remains largely unexplored in the literature.
In this work, we narrow this gap by conducting the first study on the privacy risks of generalist web agents in adversarial environments. First, we present a realistic threat model for attacks on the website, where we consider two adversarial targets: stealing users' specific PII or the entire user request.
Then, we propose a novel attack method, termed Environmental Injection Attack (EIA). EIA injects malicious content designed to adapt well to environments where the agents operate and our work instantiates EIA specifically for privacy scenarios in web environments.
We collect 177 action steps that involve diverse PII categories on realistic websites from the Mind2Web dataset, and conduct experiments using one of the most capable generalist web agent frameworks to date. The results demonstrate that EIA achieves up to 70\% attack success rate (ASR) in stealing users' specific PII and 16\% ASR in stealing a full user request at an action step. Additionally, by evaluating the detectability and testing defensive system prompts, we indicate that EIA is challenging to detect and mitigate.
Notably, attacks that are not well adapted for a webpage can be detected through careful human inspection, leading to our discussion about the trade-off between security and autonomy. However, extra attackers' efforts can make EIA seamlessly adapted, rendering such human supervision ineffective. Thus, we further discuss the implications on defenses at the pre- and post-deployment stages of the websites without relying on human supervision and call for more advanced defense strategies.

## item_id: m_0735

TITLE: Qgraph-bounded Q-learning: Stabilizing Model-Free Off-Policy Deep Reinforcement Learning

ABSTRACT: In state of the art model-free off-policy deep reinforcement learning (RL), a replay memory is used to store past experience and derive all network updates. Even if both state and action spaces are continuous, the replay memory only holds a finite number of transitions.  We represent these transitions in a data graph and link its structure to soft divergence. By selecting a subgraph with a favorable structure, we construct a simple Markov Decision Process (MDP) for which exact Q-values can be computed efficiently as more data comes in - resulting in a Qgraph. We show that the Q-value for each transition in the simplified MDP is a lower bound of the Q-value for the same transition in the original continuous Q-learning problem. By using these lower bounds in TD learning, our method is less prone to soft divergence and exhibits increased sample efficiency while being more robust to hyperparameters. Qgraphs also retain information from transitions that have already been overwritten in the replay memory, which can decrease the algorithm's sensitivity to the replay memory capacity.


## item_id: m_0736

TITLE: Efficient Evaluation of Adversarial Robustness for Deep Hashing based Retrieval

ABSTRACT: Deep hashing has been extensively applied to massive image retrieval due to its efficiency and effectiveness. Recently, several adversarial attacks have been presented to reveal the vulnerability of deep hashing models against adversarial examples. However, existing attack methods suffer in degraded performance or inefficiency because they underutilize the semantic relations between original samples or spend a lot of time learning from these samples. In this paper, we propose a novel Pharos-guided Attack, dubbed \textbf{PgA}, to evaluate the adversarial robustness of deep hashing networks efficiently. Specifically, we design \textit{pharos code} to represent the semantics of the benign image, which preserves the similarity with semantically related samples and dissimilarity with irrelevant examples. It is proven that we can quickly calculate the pharos code via a simple math formula rather than time-consuming iterative procedures. Thus, PgA can directly conduct a reliable and efficient attack on deep hashing-based retrieval by maximizing the similarity between the hash code of the adversarial example and the pharos code. Extensive experiments on the benchmark datasets verify that the proposed algorithm outperforms the prior state-of-the-arts in both attack strength and speed.

## item_id: m_0737

TITLE: Scene Transformer: A unified architecture for predicting future trajectories of multiple agents

ABSTRACT: Predicting the motion of multiple agents is necessary for planning in dynamic environments. This task is challenging for autonomous driving since agents (e.g., vehicles and pedestrians) and their associated behaviors may be diverse and influence one another. Most prior work have focused on predicting independent futures for each agent based on all past motion, and planning against these independent predictions. However, planning against independent predictions can make it challenging to represent the future interaction possibilities between different agents, leading to sub-optimal planning. In this work, we formulate a model for predicting the behavior of all agents jointly, producing consistent futures that account for interactions between agents. Inspired by recent language modeling approaches, we use a masking strategy as the query to our model, enabling one to invoke a single model to predict agent behavior in many ways, such as potentially conditioned on the goal or full future trajectory of the autonomous vehicle or the behavior of other agents in the environment. Our model architecture employs attention to combine features across road elements, agent interactions, and time steps. We evaluate our approach on autonomous driving datasets for both marginal and joint motion prediction, and achieve state of the art performance across two popular datasets. Through combining a scene-centric approach, agent permutation equivariant model, and a sequence masking strategy, we show that our model can unify a variety of motion prediction tasks from joint motion predictions to conditioned prediction.

## item_id: m_0738

TITLE: CAD-Editor: Text-based CAD Editing through Adapting Large Language Models with Synthetic Data

ABSTRACT: Computer Aided Design (CAD) is indispensable across various industries. 
\emph{Text-based CAD editing}, which automatically modifies CAD models following textual instructions, is important yet not extensively studied. 
Existing work explores design variation generation, which randomly alters specific parts of a CAD model, offering no control over the final appearance.
This work introduces \emph{CAD-Editor} for text-based editing.
We leverage Large Language Models (LLMs) as the backbone to take the concatenation of textual instruction and original CAD sequence as input and predict the edited CAD sequence, where the sequence representation of a CAD model is designed for easier processing by LLMs.
Moreover, we propose fine-tuning LLMs by using a synthetic dataset followed by a selective dataset.
The synthetic data is produced by leveraging powerful existing models, including design variation generation models for producing paired CAD models and multi-modal models for capturing textual differences between these pairs.
The selective data is created by choosing top examples from outputs of the initially fine-tuned LLMs based on human feedback or metrics.
In this way, a large-scale synthetic dataset offers basic capability while a selective dataset that is less noisy and better aligned with human intentions boosts performance further.
Extensive experiments demonstrate the advantage of CAD-Editor both quantitatively and qualitatively.

## item_id: m_0739

TITLE: MABA-Net: Masked Additive Binary Activation Network

ABSTRACT: Despite significant reduction in memory footprint and computational cost, binary neural networks suffer from noticeable accuracy degradation compared to real-valued counterparts. A few works have attempted to narrow the accuracy gap by increasing the representation bit-width or the network width/depth, but they come at the expense of increased memory and/or compute. In this work, we find that the imbalanced ratio of activations to weights may be the main cause of degraded performance and increased memory overhead. We propose Masked Additive Binary Activation Network (MABA-Net) to reduce approximation errors and the activation bit-width, with minimum increase in the activation size. MABA-Net balances the ratio of the activation size to the weight size, leading to significant memory saving on large CNNs. We demonstrate MABA-Net's superior performance on the ImageNet dataset under various network configurations. Experimental results show that MABA-Net achieves competitive accuracy without increase of computational cost, while reducing memory usage compared to state-of-the-art. We will release the codes upon acceptance.

## item_id: m_0740

TITLE: Tree-to-tree Neural Networks for Program Translation

ABSTRACT: Program translation is an important tool to migrate legacy code in one language into an ecosystem built in a different language. In this work, we are the first to consider employing deep neural networks toward tackling this problem. We observe that program translation is a modular procedure, in which a sub-tree of the source tree is translated into the corresponding target sub-tree at each step. To capture this intuition, we design a tree-to-tree neural network as an encoder-decoder architecture to translate a source tree into a target one. Meanwhile, we develop an attention mechanism for the tree-to-tree model, so that when the decoder expands one non-terminal in the target tree, the attention mechanism locates the corresponding sub-tree in the source tree to guide the expansion of the decoder. We evaluate the program translation capability of our tree-to-tree model against several state-of-the-art approaches. Compared against other neural translation models, we observe that our approach is consistently better than the baselines with a margin of up to 15 points. Further, our approach can improve the previous state-of-the-art program translation approaches by a margin of 20 points on the translation of real-world projects.

## item_id: m_0741

TITLE: CodeT:  Code Generation with Generated Tests

ABSTRACT: The task of generating code solutions for a given programming problem can benefit from the use of pre-trained language models such as Codex, which can produce multiple diverse samples. However, a major challenge for this task is to select the most appropriate solution from the multiple samples generated by the pre-trained language models. A natural way to evaluate the quality and correctness of a code solution is to run it against a set of test cases, but the manual creation of such test cases is often costly and time-consuming. In this paper, we propose a novel method, CodeT, that leverages the same pre-trained language models to automatically generate test cases for the code samples, thus reducing the human effort and increasing the coverage of the test scenarios. CodeT then executes the code samples using the generated test cases, and performs a dual execution agreement, which considers both the consistency of the outputs against the generated test cases and the agreement of the outputs with other code samples. We conduct comprehensive experiments on four benchmarks, HumanEval, MBPP, APPS and CodeContests, using five different pre-trained language models with varying sizes and capabilities. Our results show that CodeT can significantly improve the performance of code solution selection over previous methods, achieving remarkable and consistent gains across different models and benchmarks. For instance, CodeT improves the pass@1 metric on HumanEval to 65.8%, which represents an absolute improvement of 18.8% over the code-davinci-002 model, and an absolute improvement of more than 20% over the previous state-of-the-art results.

## item_id: m_0742

TITLE: Non-Negative Bregman Divergence Minimization for Deep Direct Density Ratio Estimation

ABSTRACT: The estimation of the ratio of two probability densities has garnered attention as the density ratio is useful in various machine learning tasks, such as anomaly detection and domain adaptation. To estimate the density ratio, methods collectively known as direct density ratio estimation (DRE) have been explored. These methods are based on the minimization of the Bregman (BR) divergence between a density ratio model and the true density ratio. However, existing direct DRE suffers from serious overfitting when using flexible models such as neural networks. In this paper, we introduce a non-negative correction for empirical risk using only the prior knowledge of the upper bound of the density ratio. This correction makes a DRE method more robust against overfitting and enables the use of flexible models. In the theoretical analysis, we discuss the consistency of the empirical risk. In our experiments, the proposed estimators show favorable performance in inlier-based outlier detection and covariate shift adaptation.

## item_id: m_0743

TITLE: Model-Targeted Poisoning Attacks with Provable Convergence

ABSTRACT: In a poisoning attack, an adversary with control over a small fraction of the training data attempts to select that data in a way that induces a model that misbehaves in a particular way desired by the adversary, such as misclassifying certain inputs. We propose an efficient poisoning attack that can target a desired model based on online convex optimization. Unlike previous model-targeted poisoning attacks, our attack comes with provable convergence to any achievable target classifier. The distance from the induced classifier to the target classifier is inversely proportional to the square root of the number of poisoning points. We also provide a lower bound on the minimum number of poisoning points needed to achieve a given target classifier. Our attack is the first model-targeted poisoning attack that provides provable convergence, and in our experiments it either exceeds or matches the best state-of-the-art attacks in terms of attack success rate and distance to the target model. In addition, as an online attack our attack can incrementally determine nearly optimal poisoning points. 

## item_id: m_0744

TITLE: Skip-graph: Learning graph embeddings with an encoder-decoder model

ABSTRACT: In this work, we study the problem of feature representation learning for graph-structured data. Many of the existing work in the area are task-specific and based on supervised techniques. We study a method for obtaining a generic feature representation for a graph using an unsupervised approach. The neural encoder-decoder model is a method that has been used in the natural language processing domain to learn feature representations of sentences. In our proposed approach, we train the encoder-decoder model to predict the random walk sequence of neighboring regions in a graph given a random walk along a particular region. The goal is to map subgraphs — as represented by their random walks — that are structurally and functionally similar to nearby locations in feature space. We evaluate the learned graph vectors using several real-world datasets on the graph classification task. The proposed model is able to achieve good results against state-of- the-art techniques.

## item_id: m_0745

TITLE: Deep Interaction Processes for Time-Evolving Graphs

ABSTRACT: Time-evolving graphs are ubiquitous such as online transactions on an e-commerce platform and user interactions on social networks. While neural approaches have been proposed for graph modeling, most of them focus on static graphs. In this paper we present a principled deep neural approach that models continuous time-evolving graphs at multiple time resolutions based on a temporal point process framework.  To model the dependency between latent dynamic representations of each node, we define a mixture of temporal cascades in which a node's neural representation depends on not only this node's previous representations but also the previous representations of related nodes that have interacted with this node. We generalize LSTM on this temporal cascade mixture and introduce novel time gates to model time intervals between interactions. Furthermore, we introduce a selection mechanism that gives important nodes large influence in both $k-$hop subgraphs of nodes in an interaction. To capture temporal dependency at multiple time-resolutions, we stack our neural representations in several layers and fuse them based on attention. Based on the temporal point process framework, our approach can naturally handle growth (and shrinkage) of graph nodes and interactions, making it inductive. Experimental results on interaction prediction and classification tasks -- including a  real-world financial application --  illustrate the effectiveness of the time gate, the selection and attention mechanisms of our approach, as well as its 
superior performance over the alternative approaches.

## item_id: m_0746

TITLE: Compositional GAN: Learning Conditional Image Composition

ABSTRACT: Generative Adversarial Networks (GANs) can produce images of surprising complexity and realism, but are generally structured to sample from a single latent source ignoring the explicit spatial interaction between multiple entities that could be present in a scene. Capturing such complex interactions between different objects in the world, including their relative scaling, spatial layout, occlusion, or viewpoint transformation is a challenging problem. In this work, we propose to model object composition in a GAN framework as a self-consistent composition-decomposition network. Our model is conditioned on the object images from their marginal distributions and can generate a realistic image from their joint distribution. We evaluate our model through qualitative experiments and user evaluations in scenarios when either paired or unpaired examples for the individual object images and the joint scenes are given during training. Our results reveal that the learned model captures potential interactions between the two object domains given as input to output new instances of composed scene at test time in a reasonable fashion.

## item_id: m_0747

TITLE: Defending against black-box adversarial attacks with gradient-free trained sign activation neural networks

ABSTRACT: While machine learning models today can achieve high accuracies on classification tasks, they can be deceived by minor imperceptible distortions to the data. These are known as adversarial attacks and can be lethal in the black-box setting which does not require knowledge of the target model type or its parameters. Binary neural networks that have sign activation and are trained with gradient descent have been shown to be harder to attack than conventional sigmoid activation networks but their improvements are marginal. We instead train sign activation networks with a novel gradient-free stochastic coordinate descent algorithm and propose an ensemble of such networks as a defense model. We evaluate the robustness of our model (a hard problem in itself) on image, text, and medical ECG data and find it to be more robust than ensembles of binary, full precision, and convolutional neural networks, and than random forests while attaining comparable clean test accuracy. In order to explain our model's robustness we show that an adversary targeting a single network in our ensemble fails to attack (and thus non-transferable to) other networks in the ensemble. Thus a datapoint requires a large distortion to fool the majority of networks in our ensemble and is likely to be detected in advance. This property of non-transferability arises naturally from the non-convexity of sign activation networks and randomization in our gradient-free training algorithm without any adversarial defense effort.

## item_id: m_0748

TITLE: Dynamic Graph Message Passing Networks

ABSTRACT: Modelling long-range dependencies is critical for scene understanding tasks in computer vision. Although CNNs have excelled in many vision tasks, they are still limited in capturing long-range structured relationships as they typically consist of layers of local kernels. A fully-connected graph is beneficial for such modelling, however, its computational overhead is prohibitive. We propose a dynamic graph message passing network, that significantly reduces the computational complexity compared to related works modelling a fully-connected graph. This is achieved by adaptively sampling nodes in the graph, conditioned on the input, for message passing. Based on the sampled nodes, we dynamically predict node-dependent filter weights and the affinity matrix for propagating information between them. Using this model, we show significant improvements with respect to strong, state-of-the-art baselines on three different tasks and backbone architectures. Our approach also outperforms fully-connected graphs while using substantially fewer floating-point operations.

## item_id: m_0749

TITLE: On orthogonality and learning recurrent networks with long term dependencies

ABSTRACT: It is well known that it is challenging to train deep neural networks and recurrent neural networks for tasks that exhibit long term dependencies. The vanishing or exploding gradient problem is a well known issue associated with these challenges. One approach to addressing vanishing and exploding gradients is to use either soft or hard constraints on weight matrices so as to encourage or enforce orthogonality. Orthogonal matrices preserve gradient norm during backpropagation and can therefore be a desirable property; however, we find that hard constraints on orthogonality can negatively affect the speed of convergence and model performance. This paper explores the issues of optimization convergence, speed and gradient stability using a variety of different methods for encouraging or enforcing orthogonality. In particular we propose a weight matrix factorization and parameterization strategy through which we we can bound matrix norms and therein control the degree of expansivity induced during backpropagation.

## item_id: m_0750

TITLE: Score and Lyrics-Free Singing Voice Generation

ABSTRACT: Generative models for singing voice have been mostly concerned with the task of "singing voice synthesis," i.e., to produce singing voice waveforms given musical scores and text lyrics. In this work, we explore a novel yet challenging alternative: singing voice generation without pre-assigned scores and lyrics, in both training and inference time. In particular, we experiment with three different schemes: 1) free singer, where the model generates singing voices without taking any conditions; 2) accompanied singer, where the model generates singing voices over a waveform of instrumental music; and 3) solo singer, where the model improvises a chord sequence first and then uses that to generate voices. We outline the associated challenges and propose a pipeline to tackle these new tasks. This involves the development of source separation and transcription models for data preparation, adversarial networks for audio generation, and customized metrics for evaluation.

## item_id: m_0751

TITLE: uGLAD: A deep learning model to recover conditional independence graphs

ABSTRACT: Probabilistic Graphical Models are generative models of complex systems. They rely on conditional independence assumptions between variables to learn sparse representations which can be visualized in a form of a graph. Such models are used for domain exploration and structure discovery in poorly understood domains. This work introduces a novel technique to perform sparse graph recovery by optimizing deep unrolled networks. Assuming that the input data $X\in\mathbb{R}^{M\times D}$ comes from an underlying multivariate Gaussian distribution, we apply a deep model on $X$ that outputs the precision matrix $\Theta$. Then, the partial correlation matrix \mathrm{P} is calculated which can also be interpreted as providing a list of conditional independence assertions holding in the input distribution. Our model, \texttt{uGLAD}, builds upon and extends the state-of-the-art model \texttt{GLAD} to the unsupervised setting. The key benefits of our model are (1) \texttt{uGLAD} automatically optimizes sparsity-related regularization parameters leading to better performance than existing algorithms. (2) We introduce multi-task learning based `consensus' strategy for robust handling of missing data in an unsupervised setting. We evaluate performance on synthetic Gaussian, non-Gaussian data generated from Gene Regulatory Networks, and present case studies in anaerobic digestion and infant mortality.

## item_id: m_0752

TITLE: On the Relation Between the Sharpest Directions of DNN Loss and the SGD Step Length

ABSTRACT: The training of deep neural networks with Stochastic Gradient Descent (SGD) with a large learning rate or a small batch-size typically ends in flat regions of the weight space, as indicated by small eigenvalues of the Hessian of the training loss. This was found to correlate with a good final generalization performance.  In this paper we extend previous work by investigating the curvature of the loss surface along the whole training trajectory, rather than only at the endpoint. We find that initially SGD visits increasingly sharp regions, reaching a maximum sharpness determined by both the learning rate and the batch-size of SGD. At this peak value SGD starts to fail to minimize the loss along directions in the loss surface corresponding to the largest curvature (sharpest directions). To further investigate the effect of these dynamics in the training process, we study a variant of SGD using a reduced learning rate along the sharpest directions which we show can improve training speed while finding both sharper and better generalizing solution, compared to vanilla SGD. Overall, our results show that the SGD dynamics in the subspace of the sharpest directions influence the regions that SGD steers to (where larger learning rate or smaller batch size result in wider regions visited), the overall training speed, and the generalization ability of the final model.

## item_id: m_0753

TITLE: Overcoming the vanishing gradient problem in plain recurrent networks

ABSTRACT: Plain recurrent networks greatly suffer from the vanishing gradient problem while Gated Neural Networks (GNNs) such as Long-short Term Memory (LSTM) and Gated Recurrent Unit (GRU) deliver promising results in many sequence learning tasks through sophisticated network designs. This paper shows how we can address this problem in a plain recurrent network by analyzing the gating mechanisms in GNNs. We propose a novel network called the Recurrent Identity Network (RIN) which allows a plain recurrent network to overcome the vanishing gradient problem while training very deep models without the use of gates. We compare this model with IRNNs and LSTMs on multiple sequence modeling benchmarks. The RINs demonstrate competitive performance and converge faster in all tasks. Notably, small RIN models produce 12%–67% higher accuracy on the Sequential and Permuted MNIST datasets and reach state-of-the-art performance on the bAbI question answering dataset.

## item_id: m_0754

TITLE: Understanding and Improving Lexical Choice in Non-Autoregressive Translation

ABSTRACT: Knowledge distillation (KD) is essential for training non-autoregressive translation (NAT) models by reducing the complexity of the raw data with an autoregressive teacher model. In this study, we empirically show that as a side effect of this training, the lexical choice errors on low-frequency words are propagated to the NAT model from the teacher model. To alleviate this problem, we propose to expose the raw data to NAT models to restore the useful information of low-frequency words, which are missed in the distilled data. To this end, we introduce an extra Kullback-Leibler divergence term derived by comparing the lexical choice of NAT model and that embedded in the raw data. Experimental results across language pairs and model architectures demonstrate the effectiveness and universality of the proposed approach.  Extensive analyses confirm our claim that our approach improves performance by reducing the lexical choice errors on low-frequency words.  Encouragingly, our approach pushes the SOTA NAT performance on the WMT14 English-German and WMT16 Romanian-English datasets up to 27.8 and 33.8 BLEU points, respectively. 

## item_id: m_0755

TITLE: Steering Vector Transfer via Orthonormal Transformations and Semantic Pairing

ABSTRACT: Steering vectors—directions in activation space encoding behavioral traits like formality or creativity—enable fine-grained control over language model outputs but must be regenerated for each new model, creating deployment barriers. We present a method for transferring these vectors between different language models by learning structure-preserving transformations while matching corresponding text pairs across models. Our approach achieves strong alignment (0.50-0.56 cosine similarity, where 1.0 represents perfect alignment and 0.0 represents random chance) across all model pairs tested. Crucially, we demonstrate that semantic pairing—ensuring each text contrast is matched across models during training—improves transfer performance by 72%: proper pairing achieves 0.529 cosine similarity compared to 0.308 with shuffled pairs within traits and 0.00 with random pairing across traits. We evaluate our method across 26 behavioral traits on three architecturally distinct models (Gemma-7B, LLaMA-3-8B, and Mistral-7B), using dimensionality reduction to handle their different hidden dimensions. Our results provide evidence for the Platonic Representation Hypothesis, showing that different language models encode behavioral preferences in similar geometric structures. This enables practical reuse of curated steering vectors across model families and advances our understanding of how neural networks represent human preferences.

## item_id: m_0756

TITLE: Understanding and Leveraging Expert-level Monosemanticity in Finetuning MoE LLMs

ABSTRACT: Large language models (LLMs) with Mixture-of-Experts (MoE) architectures have emerged as a promising approach for enhancing scalability and efficiency, with minimal performance degradation across diverse downstream tasks. However, the interpretability of experts and efficient post-training methods of domain experts remain understudied. In this paper, we first analyze the expert-level monosemanticity of MoE based on the sparse autoencoder (SAE), thereby facilitating a deeper understanding of domain experts' roles. Additionally, leveraging the enhanced monosemanticity induced by the sparse activations of MoE LLMs, we propose a new fine-tuning strategy that freezes domain-agnostic experts in specific layers. Unlike dense LLMs, the sparsity of MoE enables experts to exhibit stronger expert-level monosemantic behavior, allowing us to identify experts responsible for particular downstream tasks and freeze those unrelated during post-training. By only updating domain-relevant experts, our method mitigates the risk of catastrophic forgetting in other domains and reduces computational costs. Empirically, we apply this strategy to supervised fine-tuning of MoE models on tool-use data. Results show that monosemanticity-guided tuning achieves performance comparable to fully-tuned models on tool-use tasks, while preserving better performance in other domains. Our study provides an interpretability-guided strategy for understanding and finetuning MoE LLMs while alleviating performance degradation across domains.

## item_id: m_0757

TITLE: INTIMA: A Benchmark for Human-AI Companionship Behavior

ABSTRACT: AI companionship, where users develop emotional bonds with AI systems, has emerged as a significant pattern with positive but also concerning implications. We introduce Interactions and Machine Attachment Benchmark (INTIMA), a benchmark for evaluating companionship behaviors in language models. Drawing from psychological theories and user data, we develop a taxonomy of 31 behaviors across four categories and 368 targeted prompts. Responses to these prompts are evaluated as companionship-reinforcing, boundary-maintaining, or neutral. Applying INTIMA to Gemma-3, Phi-4, o4-mini, GPT5-mini, and Claude-4 reveals that companionship-reinforcing behaviors remain much more common across all models, though we observe marked differences between models. Different commercial providers prioritize different categories within the more sensitive parts of the benchmark, which is concerning since both appropriate boundary-setting and emotional support matter for user well-being. These findings highlight the need for more consistent approaches to handling emotionally charged interactions. We release all datasets and evaluation code for our experiments.

## item_id: m_0758

TITLE: Non-linear Dimensionality Regularizer for Solving Inverse Problems

ABSTRACT: Consider an ill-posed inverse problem of estimating causal factors from observations, one of which is known to lie near some (unknown) low-dimensional, non-linear manifold expressed by a predefined Mercer-kernel. Solving this problem requires simultaneous estimation of these factors and learning the low-dimensional representation for them. In this work, we introduce a novel non-linear dimensionality regularization technique for solving such problems without pre-training.
We re-formulate Kernel-PCA as an energy minimization problem in which low dimensionality constraints are introduced as regularization terms in the energy.
To the best of our knowledge, ours is the first attempt to create a dimensionality regularizer in the KPCA framework. Our approach relies on robustly penalizing the rank of the recovered factors directly in the implicit feature space to create
their low-dimensional approximations in closed form. Our approach performs robust KPCA in the presence of missing data and noise.
We demonstrate state-of-the-art results on predicting missing entries in the standard oil flow dataset. Additionally, we evaluate our method on the challenging problem of Non-Rigid Structure from Motion and our approach delivers promising results on CMU mocap dataset despite the presence of significant occlusions and noise.

## item_id: m_0759

TITLE: Emergence of Exploration in Policy Gradient Reinforcement Learning via Resetting

ABSTRACT: In reinforcement learning (RL), many exploration methods explicitly promote stochastic policies, e.g., by adding an entropy bonus. We argue that exploration only matters in RL because the agent repeatedly encounters the same or similar states, so that it is beneficial to gradually improve the performance over the encounters; otherwise, the greedy policy would be optimal. Based on this intuition, we propose ReMax, an objective for RL whereby stochastic exploration arises as an emergent property, without adding any explicit exploration bonus. In ReMax, an episode is modified so that the agent can reset to previous states in the trajectory, and the agent’s goal is to maximize the best return in the trajectory tree. We show that this ReMax objective can be directly optimized with an unbiased policy gradient method. Experiments confirm that ReMax leads to the emergence of a stochastic exploration policy, and improves the performance compared to RL with no exploration bonus.

## item_id: m_0760

TITLE: StrokeNet: A Neural Painting Environment

ABSTRACT: We've seen tremendous success of image generating models these years. Generating images through a neural network is usually pixel-based, which is fundamentally different from how humans create artwork using brushes. To imitate human drawing, interactions between the environment and the agent is required to allow trials. However, the environment is usually non-differentiable, leading to slow convergence and massive computation. In this paper we try to address the discrete nature of software environment with an intermediate, differentiable simulation. We present  StrokeNet, a novel model where the agent is trained upon a well-crafted neural approximation of the painting environment. With this approach, our agent was able to learn to write characters such as MNIST digits faster than reinforcement learning approaches in an unsupervised manner. Our primary contribution is the neural simulation of a real-world environment. Furthermore, the agent trained with the emulated environment is able to directly transfer its skills to real-world software.

## item_id: m_0761

TITLE: Trading Information between Latents in Hierarchical Variational Autoencoders

ABSTRACT: Variational Autoencoders (VAEs) were originally motivated as probabilistic generative models in which one performs approximate Bayesian inference. The proposal of $\beta$-VAEs breaks this interpretation and generalizes VAEs to application domains beyond generative modeling (e.g., representation learning, clustering, or lossy data compression) by introducing an objective function that allows practitioners to trade off between the information content ("bit rate") of the latent representation and the distortion of reconstructed data. In this paper, we reconsider this rate/distortion trade-off in the context of hierarchical VAEs, i.e., VAEs with more than one layer of latent variables. We propose a method to control each layer's contribution to the rate independently. We identify the most general class of inference models to which our proposed method is applicable, and we derive theoretical bounds on the performance of downstream tasks as functions of the individual layers' rates. Our experiments demonstrate that the proposed method allows us to better tune hierarchical VAEs for a diverse set of practical use cases.

## item_id: m_0762

TITLE: Online Learning Rate Adaptation with Hypergradient Descent

ABSTRACT: We introduce a general method for improving the convergence rate of gradient-based optimizers that is easy to implement and works well in practice.  We demonstrate the effectiveness of the method in a range of optimization problems by applying it to stochastic gradient descent, stochastic gradient descent with Nesterov momentum, and Adam, showing that it significantly reduces the need for the manual tuning of the initial learning rate for these commonly used algorithms.  Our method works by dynamically updating the learning rate during optimization using the gradient with respect to the learning rate of the update rule itself.  Computing this "hypergradient" needs little additional computation, requires only one extra copy of the original gradient to be stored in memory, and relies upon nothing more than what is provided by reverse-mode automatic differentiation.

## item_id: m_0763

TITLE: Learning Graph Representations by Dendrograms

ABSTRACT: Hierarchical  clustering is a common approach to analysing  the 
multi-scale structure of  graphs observed in practice.  
We propose a novel  metric for assessing the quality of a hierarchical clustering. This metric reflects the ability to reconstruct the graph from the dendrogram encoding the hierarchy. The best  representation of the graph for this metric in turn yields a  novel hierarchical clustering algorithm. Experiments on both real and synthetic data illustrate the efficiency of the approach. 


## item_id: m_0764

TITLE: SFTMix: Elevating Language Model Instruction Tuning with Mixup Recipe

ABSTRACT: To induce desired behaviors in large language models (LLMs) for interaction-driven tasks, the instruction-tuning stage typically trains LLMs on instruction-response pairs using the next-token prediction (NTP) loss. Previous work aiming to improve instruction-tuning performance often emphasizes the need for higher-quality supervised fine-tuning (SFT) datasets, which typically involves expensive data filtering with proprietary LLMs or labor-intensive data generation by human annotators. However, these approaches do not fully leverage the datasets' intrinsic properties, resulting in high computational and labor costs, thereby limiting scalability and performance gains. In this paper, we propose SFTMix, a novel recipe that elevates instruction-tuning performance beyond the conventional NTP paradigm, without the need for well-curated datasets. Observing that LLMs exhibit uneven confidence across the semantic representation space, we argue that examples with different confidence levels should play distinct roles during the instruction-tuning process. Based on this insight, SFTMix leverages training dynamics to identify examples with varying confidence levels, then applies a Mixup-based regularization to mitigate overfitting on confident examples while propagating supervision signals to improve learning on relatively unconfident ones. This approach enables SFTMix to significantly outperform NTP across a wide range of instruction-following and healthcare domain-specific SFT tasks, demonstrating its adaptability to diverse LLM families and scalability to datasets of any size. Comprehensive ablation studies further verify the robustness of SFTMix's design choices, underscoring its versatility in consistently enhancing performance across different LLMs and datasets in broader natural language processing applications.

## item_id: m_0765

TITLE: Visual Imitation with a Minimal Adversary

ABSTRACT: High-dimensional sparse reward tasks present major challenges for reinforcement learning agents.  In this work we use imitation learning to address two of these challenges:  how to learn a useful representation of the world e.g.  from pixels, and how to explore efficiently given the rarity of a reward signal? We show that adversarial imitation can work well even in this high dimensional observation space. Surprisingly the adversary itself, acting as the learned reward function, can be tiny, comprising as few as 128 parameters, and can be easily trained using the most basic GAN formulation. Our approach removes limitations present in most contemporary imitation approaches: requiring no demonstrator actions (only video), no special initial conditions or warm starts, and no explicit tracking of any single demo. The proposed agent can solve a challenging robot manipulation task of block stacking from only video demonstrations and sparse reward, in which the non-imitating agents fail to learn completely.  Furthermore, our agent learns much faster than competing approaches that depend on hand-crafted, staged dense reward functions, and also better compared to standard GAIL baselines. Finally, we develop a new adversarial goal recognizer that in some cases allows the agent to learn stacking without any task reward, purely from imitation.

## item_id: m_0766

TITLE: Deep Distributed Optimization for Large-Scale Quadratic Programming

ABSTRACT: Quadratic programming (QP) forms a crucial foundation in optimization, appearing in a broad spectrum of domains and serving as the basis for more advanced algorithms. Consequently, as the scale and complexity of modern applications continue to grow, the development of efficient and reliable QP algorithms becomes increasingly vital. In this context, this paper introduces a novel deep learning-aided distributed optimization architecture designed for tackling large-scale QP problems. First, we combine the state-of-the-art Operator Splitting QP (OSQP) method with a consensus approach to derive **DistributedQP**, a new method tailored for network-structured problems, with convergence guarantees to optimality. Subsequently, we unfold this optimizer into a deep learning framework, leading to **DeepDistributedQP**, which leverages learned policies to accelerate reaching to desired accuracy within a restricted amount of iterations. Our approach is also theoretically grounded through Probably Approximately Correct (PAC)-Bayes theory, providing generalization bounds on the expected optimality gap for unseen problems. The proposed framework, as well as its centralized version **DeepQP**, significantly outperform their standard optimization counterparts on a variety of tasks such as randomly generated problems, optimal control, linear regression, transportation networks and others. Notably, DeepDistributedQP demonstrates strong generalization by training on small problems and scaling to solve much larger ones (up to 50K variables and 150K constraints) using the same policy. Moreover, it achieves orders-of-magnitude improvements in wall-clock time compared to OSQP. The certifiable performance guarantees of our approach are also demonstrated, ensuring higher-quality solutions over traditional optimizers.

## item_id: m_0767

TITLE: Global Context Vision Transformers

ABSTRACT: We propose global context vision transformer (GC ViT), a novel architecture that enhances parameter and compute utilization for computer vision tasks. The core of the novel model are  global context self-attention modules, joint with standard local self-attention, to effectively yet efficiently model both long and short-range spatial interactions, as an alternative to complex operations such as an attention masks or local windows shifting. While the local self-attention modules are responsible for modeling short-range information, the global query tokens are shared across all global self-attention modules to interact with local key and values. In addition, we address the lack of inductive bias in ViTs and improve the modeling of inter-channel dependencies by proposing a novel downsampler which leverages a parameter-efficient fused inverted residual block. The proposed GC ViT achieves new state-of-the-art performance across image classification, object detection and semantic segmentation tasks. On ImageNet-1K dataset for classification, the tiny, small and base variants of GC ViT with 28M, 51M and 90M parameters achieve 83.4%, 83.9% and 84.4% Top-1 accuracy, respectively, surpassing comparably-sized prior art such as CNN-based ConvNeXt and ViT-based Swin Transformer. Pre-trained GC ViT backbones in downstream tasks of object detection, instance segmentation, and semantic segmentation on MS COCO and ADE20K datasets outperform prior work consistently, sometimes by large margins.

## item_id: m_0768

TITLE: Deep concept removal

ABSTRACT: We address the problem of concept removal in deep neural networks, aiming to learn representations that do not encode certain specified concepts (e.g., gender etc.) We propose a novel method based on adversarial linear classifiers trained on a concept dataset, which helps to remove the targeted attribute while maintaining model performance. Our approach Deep Concept Removal incorporates adversarial probing classifiers at various layers of the network, effectively addressing concept entanglement and improving out-of-distribution generalization. We also introduce an implicit gradient-based technique to tackle the challenges associated with adversarial training using linear classifiers. We evaluate the ability to remove a concept on a set of popular distributionally robust optimization (DRO) benchmarks with spurious correlations, as well as out-of-distribution (OOD) generalization tasks.

## item_id: m_0769

TITLE: XLVIN: eXecuted Latent Value Iteration Nets

ABSTRACT: Value Iteration Networks (VINs) have emerged as a popular method to perform implicit planning within deep reinforcement learning, enabling performance improvements on tasks requiring long-range reasoning and understanding of environment dynamics. This came with several limitations, however: the model is not explicitly incentivised to perform meaningful planning computations, the underlying state space is assumed to be discrete, and the Markov decision process (MDP) is assumed fixed and known. We propose eXecuted Latent Value Iteration Networks (XLVINs), which combine recent developments across contrastive self-supervised learning, graph representation learning and neural algorithmic reasoning to alleviate all of the above limitations, successfully deploying VIN-style models on generic environments. XLVINs match the performance of VIN-like models when the underlying MDP is discrete, fixed and known, and provide significant improvements to model-free baselines across three general MDP setups.

## item_id: m_0770

TITLE: IEA: Inner Ensemble Average within a convolutional neural network

ABSTRACT: Ensemble learning is a method of combining multiple trained models to improve model accuracy. We propose the usage of such methods, specifically ensemble average, inside Convolutional Neural Network (CNN) architectures by replacing the single convolutional layers with Inner Average Ensembles (IEA) of multiple convolutional layers. Empirical results on different benchmarking datasets show that CNN models using IEA outperform those with regular convolutional layers and advances the state of art. A visual and a similarity score analysis of the features generated from IEA explains why it boosts the model performance.

## item_id: m_0771

TITLE: Third Person Imitation Learning

ABSTRACT: Reinforcement learning (RL) makes it possible to train agents capable of achieving
sophisticated goals in complex and uncertain environments. A key difficulty in
reinforcement learning is specifying a reward function for the agent to optimize.
Traditionally, imitation learning in RL has been used to overcome this problem.
Unfortunately, hitherto imitation learning methods tend to require that demonstrations
are supplied in the first-person: the agent is provided with a sequence of
states and a specification of the actions that it should have taken. While powerful,
this kind of imitation learning is limited by the relatively hard problem of collecting
first-person demonstrations. Humans address this problem by learning from
third-person demonstrations: they observe other humans perform tasks, infer the
task, and accomplish the same task themselves.
In this paper, we present a method for unsupervised third-person imitation learning.
Here third-person refers to training an agent to correctly achieve a simple
goal in a simple environment when it is provided a demonstration of a teacher
achieving the same goal but from a different viewpoint; and unsupervised refers
to the fact that the agent receives only these third-person demonstrations, and is
not provided a correspondence between teacher states and student states. Our
methods primary insight is that recent advances from domain confusion can be
utilized to yield domain agnostic features which are crucial during the training
process. To validate our approach, we report successful experiments on learning
from third-person demonstrations in a pointmass domain, a reacher domain, and
inverted pendulum.

## item_id: m_0772

TITLE: Learning to Route LLMs from Bandit Feedback: One Policy, Many Trade-offs

ABSTRACT: Efficient use of large language models (LLMs) is critical for deployment at scale: without adaptive routing, systems either overpay for strong models or risk poor performance from weaker ones. Selecting the right LLM for each query is fundamentally an online decision problem: models differ in strengths, prices fluctuate, and users value performance and cost differently. Yet most routers are trained offline with labels for all candidate models, an assumption that breaks in deployment, where only the outcome of the chosen model is observed. We bridge this gap with a bandit-feedback routing approach that trains under the same partial-feedback restriction as deployment, while supporting preference-tunable inference: operators can dial the performance–cost trade-off at test time without retraining. Framed as a contextual bandit over prompt features and a user preference vector, our method simulates an online feedback setting during training and adapts its routing decisions to each new prompt, rather than depending on full-information offline supervision. Comprehensive experiments on RouterBench show that our method consistently outperforms strong offline routers, including GraphRouter and RouterDC, in terms of performance and cost, and generalizes robustly for unseen tasks.

## item_id: m_0773

TITLE: The large learning rate phase of deep learning

ABSTRACT: The choice of initial learning rate can have a profound effect on the performance of deep networks. We present empirical evidence that networks exhibit sharply distinct behaviors at small and large learning rates. In the small learning rate phase, training can be understood using the existing theory of infinitely wide neural networks. At large learning rates, we find that networks exhibit qualitatively distinct phenomena that cannot be explained by existing theory: The loss grows during the early part of training, and optimization eventually converges to a flatter minimum. Furthermore, we find that the optimal performance is often found in the large learning rate phase. To better understand this behavior we analyze the dynamics of a two-layer linear network and prove that it exhibits these different phases. We find good agreement between our analysis and the training dynamics observed in realistic deep learning settings. 



## item_id: m_0774

TITLE: DeepHoyer: Learning Sparser Neural Network with Differentiable Scale-Invariant Sparsity Measures

ABSTRACT: In seeking for sparse and efficient neural network models, many previous works investigated on enforcing L1 or L0 regularizers to encourage weight sparsity during training. The L0 regularizer measures the parameter sparsity directly and is invariant to the scaling of parameter values. But it cannot provide useful gradients and therefore requires complex optimization techniques. The L1 regularizer is almost everywhere differentiable and can be easily optimized with gradient descent. Yet it is not scale-invariant and causes the same shrinking rate to all parameters, which is inefficient in increasing sparsity. Inspired by the Hoyer measure (the ratio between L1 and L2 norms) used in traditional compressed sensing problems, we present DeepHoyer, a set of sparsity-inducing regularizers that are both differentiable almost everywhere and scale-invariant. Our experiments show that enforcing DeepHoyer regularizers can produce even sparser neural network models than previous works, under the same accuracy level. We also show that DeepHoyer can be applied to both element-wise and structural pruning.

## item_id: m_0775

TITLE: What Preserves the Emergence of Language?

ABSTRACT: The emergence of language is a mystery. One dominant theory is that cooperation boosts language to emerge. However, as a means of giving out information, language seems not to be an evolutionarily stable strategy. To ensure the survival advantage of many competitors, animals are selfish in nature. From the perspective of Darwinian, if an individual can obtain a higher benefit by deceiving the other party, why not deceive? For those who are cheated, once bitten and twice shy, cooperation will no longer be a good option. As a result, motivation for communication, as well as the emergence of language would perish. Then, what preserves the emergence of language? We aim to answer this question in a brand new framework of agent community, reinforcement learning, and natural selection. Empirically, we reveal that lying indeed dispels cooperation. Even with individual resistance to lying behaviors, liars can easily defeat truth tellers and survive during natural selection. However, social resistance eventually constrains lying and makes the emergence of language possible.

## item_id: m_0776

TITLE: Dual-level Affinity Induced Embedding-free Multi-view Clustering with Joint-alignment

ABSTRACT: Despite remarkable progress, there still exist several limitations in current multi-view clustering (MVC) techniques. Specially, they generally focus only on the affinity relationship between anchors and samples, while overlooking that between anchors. Moreover, due to the lack of data labels, the cluster order is inconsistent across views and accordingly anchors encounter misalignment issue,  which will confuse the graph structure and disorganize cluster representation. Even worse, it typically brings variance during forming embedding, degenerating the stability of clustering results.   In response to these concerns, in the paper we propose a MVC approach named DLA-EF-JA. Concretely, we explicitly exploit the geometric properties between anchors via  self-expression learning skill, and utilize topology learning strategy to feed captured anchor-anchor features into anchor-sample graph  so as to explore the manifold structure hidden within samples  more adequately.  To reduce the misalignment risk, we introduce a permutation mechanism for each view to jointly rearrange anchors according to respective view  characteristics. Besides not involving selecting the baseline view, it also can coordinate with anchors in the unified framework and thereby facilitate the learning of anchors.  Further, rather than forming embedding and then performing spectral  partitioning, based on the criterion that samples and clusters should be hard assignment, we manage to construct the cluster labels directly from original samples using the binary strategy,  not only preserving the data diversity but avoiding variance. Experiments on multiple publicly available datasets confirm the effectiveness of our DLA-EF-JA.

## item_id: m_0777

TITLE: AUGMENTED POLICY GRADIENT METHODS FOR EFFICIENT REINFORCEMENT LEARNING

ABSTRACT: We propose a new mixture of model-based and model-free reinforcement learning
(RL) algorithms that combines the strengths of both RL methods. Our goal is to reduce the sample complexity of model-free approaches utilizing fictitious trajectory
rollouts performed on a learned dynamics model to improve the data efficiency of
policy gradient methods while maintaining the same asymptotic behaviour. We
suggest to use a special type of uncertainty quantification by a stochastic dynamics
model in which the next state prediction is randomly drawn from the distribution
predicted by the dynamics model. As a result, the negative effect of exploiting
erroneously optimistic regions in the dynamics model is addressed by next state
predictions based on an uncertainty aware ensemble of dynamics models. The
influence of the ensemble of dynamics models on the policy update is controlled
by adjusting the number of virtually performed rollouts in the next iteration according to the ratio of the real and virtual total reward. Our approach, which we
call Model-Based Policy Gradient Enrichment (MBPGE), is tested on a collection of benchmark tests including simulated robotic locomotion. We compare our
approach to plain model-free algorithms and a model-based one. Our evaluation
shows that MBPGE leads to higher learning rates in an early training stage and an
improved asymptotic behaviour.

## item_id: m_0778

TITLE: Unsupervised Representation Learning by Predicting Image Rotations

ABSTRACT: Over the last years, deep convolutional neural networks (ConvNets) have transformed the field of computer vision thanks to their  unparalleled capacity to learn high level semantic image features. However, in order to successfully learn those features, they usually require massive amounts of manually labeled data, which is both expensive and impractical to scale. Therefore, unsupervised semantic feature learning, i.e., learning without requiring manual annotation effort, is of crucial importance in order to successfully harvest the vast amount of visual data that are available today. In our work we propose to learn image features by training ConvNets to recognize the 2d rotation that is applied to the image that it gets as input.  We demonstrate both qualitatively and quantitatively that this apparently simple task actually provides a very powerful supervisory signal for semantic feature learning.  We exhaustively evaluate our method in various unsupervised feature learning benchmarks and we exhibit in all of them state-of-the-art performance. Specifically, our results on those benchmarks demonstrate dramatic improvements w.r.t. prior state-of-the-art approaches in unsupervised representation learning and thus significantly close the gap with supervised feature learning. For instance, in PASCAL VOC 2007 detection task our unsupervised pre-trained AlexNet model achieves the state-of-the-art (among unsupervised methods) mAP of 54.4%$that is only 2.4 points lower from the supervised case.  We get similarly striking results when we transfer our unsupervised learned features on various other tasks, such as ImageNet classification, PASCAL classification, PASCAL segmentation, and CIFAR-10 classification. The code and models of our paper will be published on:
https://github.com/gidariss/FeatureLearningRotNet

## item_id: m_0779

TITLE: Context Based Machine Translation With Recurrent Neural Network For English-Amharic Translation 

ABSTRACT: The current approaches for machine translation usually require large set of parallel corpus in order to achieve fluency like in the case of neural machine translation (NMT), statistical machine translation (SMT) and example-based machine translation (EBMT). The context awareness of phrase-based machine translation (PBMT) approaches is also questionable. This research develops a system that translates English text to Amharic text using a combination of context based machine translation (CBMT) and a recurrent neural network machine translation (RNNMT). We built a bilingual dictionary for the CBMT system to use along with a large target corpus. The RNNMT model has then been provided with the output of the CBMT and a parallel corpus for training. Our combinational approach on English-Amharic language pair yields a performance improvement over the simple neural machine translation (NMT).

## item_id: m_0780

TITLE: Scalable Generative Models for Graphs with Graph Attention Mechanism

ABSTRACT: Graphs are ubiquitous real-world data structures, and generative models that approximate distributions over graphs and derive new samples from them have significant importance. Among the known challenges in graph generation tasks, scalability handling of large graphs and datasets is one of the most important for practical applications. Recently, an increasing number of graph generative models have been proposed and have demonstrated impressive results. However, scalability is still an unresolved problem due to the complex generation process or difficulty in training parallelization. 
In this paper, we first define scalability from three different perspectives: number of nodes, data, and node/edge labels. Then, we propose GRAM, a generative model for graphs that is scalable in all three contexts, especially in training. We aim to achieve scalability by employing a novel graph attention mechanism, formulating the likelihood of graphs in a simple and general manner. Also, we apply two techniques to reduce computational complexity. Furthermore, we construct a unified and non-domain-specific evaluation metric in node/edge-labeled graph generation tasks by combining a graph kernel and Maximum Mean Discrepancy. Our experiments on synthetic and real-world graphs demonstrated the scalability of our models and their superior performance compared with baseline methods.

## item_id: m_0781

TITLE: Policy Optimization with Stochastic Mirror Descent

ABSTRACT: Improving sample efficiency has been a longstanding goal in reinforcement learning.
In this paper, we propose the $\mathtt{VRMPO}$: a sample efficient policy gradient method with stochastic mirror descent.
A novel variance reduced policy gradient estimator is the key of $\mathtt{VRMPO}$ to improve sample efficiency.
Our $\mathtt{VRMPO}$ needs only $\mathcal{O}(\epsilon^{-3})$ sample trajectories to achieve an $\epsilon$-approximate first-order stationary point, 
which matches the best-known sample complexity.
We conduct extensive experiments to show our algorithm outperforms state-of-the-art policy gradient methods in various settings.

## item_id: m_0782

TITLE: Deterministic PAC-Bayesian generalization bounds for deep networks via generalizing noise-resilience

ABSTRACT: The ability of overparameterized deep networks to generalize well has been linked to the fact that stochastic gradient descent (SGD) finds solutions that lie in flat, wide minima in the training loss -- minima where the output of the network is resilient to small random noise added to its parameters. 
So far this observation has been used to provide generalization guarantees only for neural networks whose parameters are either \textit{stochastic} or \textit{compressed}. In this work, we present a general PAC-Bayesian framework that leverages this observation to provide a bound on the original network learned -- a network that is deterministic and uncompressed.  What enables us to do this is a key novelty in our approach: our framework allows us to show that if on training data, the interactions between the weight matrices satisfy certain conditions that imply a wide training loss minimum, these conditions themselves {\em generalize} to the interactions between the matrices on test data, thereby implying a wide test loss minimum. We then apply our general framework in a setup where we assume that the pre-activation values of the network are not too small (although we assume this only on the training data). In this setup, we provide a generalization guarantee for the original (deterministic, uncompressed) network, that does not scale with product of the spectral norms of the weight matrices -- a guarantee that would not have been possible with prior approaches.

## item_id: m_0783

TITLE: Stability and Generalisation in Batch Reinforcement Learning

ABSTRACT: Overfitting has been recently acknowledged as a key limiting factor in the capabilities of reinforcement learning algorithms, despite little theoretical characterisation. We provide a theoretical examination of overfitting in the context of batch reinforcement learning, through the fundamental relationship between algorithmic stability (Bousquet & Elisseeff, 2002)–which characterises the effect of a change at a single data point–and the generalisation gap–which quantifies overfitting. Examining a popular fitted policy evaluation method with linear value function approximation, we characterise the dynamics of overfitting in the RL context. We provide finite sample, finite time, polynomial bounds on the generalisation gap in RL. In addition, our approach applies to a class of algorithms which only partially fit to temporal difference errors, as is common in deep RL, rather than perfectly optimising at each step. As such, our results characterise an unexplored bias-variance trade-off in the frequency of target network updates. To do so, our work extends the stochastic gradient-based approach of Hardt et al. (2016) to the iterative methods more common in RL. We find that under regimes where learning requires few iterations, the expected temporal difference error over the dataset is representative of the true performance on the MDP, indicating that, as is the case in supervised learning, good generalisation in RL can be ensured through the use of algorithms that learn quickly.


## item_id: m_0784

TITLE: Training deep neural-networks using a noise adaptation layer

ABSTRACT: The availability of large datsets has enabled neural networks to achieve impressive recognition results. However, the presence of inaccurate class labels is known  to deteriorate the performance of even the best classifiers in a broad range of classification problems. Noisy labels also  tend to be more harmful than noisy attributes. When the observed label is noisy, we can view the correct label as a latent random variable and model the noise processes by a communication channel with unknown parameters. Thus we can apply the EM algorithm to find the parameters of both the network and the noise  and to estimate the correct label. In this study we present a neural-network approach that optimizes  the same likelihood function as optimized by the EM algorithm. The noise is explicitly modeled by an additional softmax layer that connects the correct labels to the noisy ones. This scheme is then extended  to the case where the noisy labels are dependent  on the features in addition to the correct labels.  Experimental results demonstrate that this approach  outperforms previous methods.


## item_id: m_0785

TITLE: Revitalize Region Feature for Democratizing Video-language Pre-training of Retrieval

ABSTRACT: Recent dominant methods for video-language pre-training (VLP) learn transferable representations from the raw pixels in an end-to-end manner to achieve advanced performance on downstream video-language retrieval. Despite the impressive results, VLP research becomes extremely expensive with the need for massive data and a long training time, preventing further explorations. In this work, we revitalize region features of sparsely sampled video clips to significantly reduce both spatial and temporal visual redundancy towards democratizing VLP research at the same time achieving state-of-the-art results. Specifically, to fully explore the potential of region features, we introduce a novel bidirectional region-word alignment regularization that properly optimizes the fine-grained relations between regions and certain words in sentences, eliminating the domain/modality disconnections between pre-extracted region features and text. Extensive results of downstream video-language retrieval tasks on four datasets demonstrate the superiority of our method on both effectiveness and efficiency, e.g., our method achieves competing results with 80% fewer data and 85% less pre-training time compared to the most efficient VLP method so far.

## item_id: m_0786

TITLE: Normalization Gradients are Least-squares Residuals

ABSTRACT: Batch Normalization (BN) and its variants have seen widespread adoption in the deep learning community because they improve the training of deep neural networks. Discussions of why this normalization works so well remain unsettled.  We make explicit the relationship between ordinary least squares and partial derivatives computed when back-propagating through BN. We recast the back-propagation of BN as a least squares fit, which zero-centers and decorrelates partial derivatives from normalized activations. This view, which we term {\em gradient-least-squares}, is an extensible and arithmetically accurate description of BN. To further explore this perspective, we motivate, interpret, and evaluate two adjustments to BN.

## item_id: m_0787

TITLE: Ensemble Robustness and Generalization of Stochastic Deep Learning Algorithms

ABSTRACT: The question why deep learning algorithms generalize so well has attracted increasing
research interest. However, most of the well-established approaches,
such as hypothesis capacity, stability or sparseness, have not provided complete
explanations (Zhang et al., 2016; Kawaguchi et al., 2017). In this work, we focus
on the robustness approach (Xu & Mannor, 2012), i.e., if the error of a hypothesis
will not change much due to perturbations of its training examples, then it
will also generalize well. As most deep learning algorithms are stochastic (e.g.,
Stochastic Gradient Descent, Dropout, and Bayes-by-backprop), we revisit the robustness
arguments of Xu & Mannor, and introduce a new approach – ensemble
robustness – that concerns the robustness of a population of hypotheses. Through
the lens of ensemble robustness, we reveal that a stochastic learning algorithm can
generalize well as long as its sensitiveness to adversarial perturbations is bounded
in average over training examples. Moreover, an algorithm may be sensitive to
some adversarial examples (Goodfellow et al., 2015) but still generalize well. To
support our claims, we provide extensive simulations for different deep learning
algorithms and different network architectures exhibiting a strong correlation between
ensemble robustness and the ability to generalize.

## item_id: m_0788

TITLE: Discovering General-Purpose Active Learning Strategies

ABSTRACT: We propose a general-purpose approach to discovering active learning (AL) strategies from data. These strategies are transferable from one domain to another and can be used in conjunction with many machine learning models. To this end, we formalize the annotation process as a Markov decision process, design universal state and action spaces and introduce a new reward function that precisely reflects the AL objective of minimizing the annotation cost We seek to find an optimal (non-myopic) AL strategy using reinforcement learning. We evaluate the learned strategies on multiple unrelated domains and show that they consistently outperform state-of-the-art baselines.

## item_id: m_0789

TITLE: Answering Complex Open-Domain Questions with Multi-Hop Dense Retrieval

ABSTRACT: We propose a simple and efficient multi-hop dense retrieval approach for answering complex open-domain questions, which achieves state-of-the-art performance on two multi-hop datasets, HotpotQA and multi-evidence FEVER. Contrary to previous work, our method does not require access to any corpus-specific information, such as inter-document hyperlinks or human-annotated entity markers, and can be applied to any unstructured text corpus. Our system also yields a much better efficiency-accuracy trade-off, matching the best published accuracy on HotpotQA while being 10 times faster at inference time.

## item_id: m_0790

TITLE: Enabling Arbitrary Translation Objectives with Adaptive Tree Search

ABSTRACT: We introduce an adaptive tree search algorithm, which is a deterministic variant of Monte Carlo tree search, that can find high-scoring outputs under translation models that make no assumptions about the form or structure of the search objective. This algorithm enables the exploration of new kinds of models that are unencumbered by constraints imposed to make decoding tractable, such as autoregressivity or conditional independence assumptions. When applied to autoregressive models, our algorithm has different biases than beam search has, which enables a new analysis of the role of decoding bias in autoregressive models. Empirically, we show that our adaptive tree search algorithm finds outputs with substantially better model scores compared to beam search in autoregressive models, and compared to reranking techniques in models whose scores do not decompose additively with respect to the words in the output. We also characterise the correlation of several translation model objectives with respect to BLEU. We find that while some standard models are poorly calibrated and benefit from the beam search bias, other often more robust models (autoregressive models tuned to maximize expected automatic metric scores, the noisy channel model and a newly proposed objective) benefit from increasing amounts of search using our proposed decoder, whereas the beam search bias limits the improvements obtained from such objectives. Thus, we argue that as models improve, the improvements may be masked by over-reliance on beam search or reranking based methods.

## item_id: m_0791

TITLE: Monotonic Chunkwise Attention

ABSTRACT: Sequence-to-sequence models with soft attention have been successfully applied to a wide variety of problems, but their decoding process incurs a quadratic time and space cost and is inapplicable to real-time sequence transduction. To address these issues, we propose Monotonic Chunkwise Attention (MoChA), which adaptively splits the input sequence into small chunks over which soft attention is computed. We show that models utilizing MoChA can be trained efficiently with standard backpropagation while allowing online and linear-time decoding at test time. When applied to online speech recognition, we obtain state-of-the-art results and match the performance of a model using an offline soft attention mechanism. In document summarization experiments where we do not expect monotonic alignments, we show significantly improved performance compared to a baseline monotonic attention-based model.

## item_id: m_0792

TITLE: Discriminative Active Learning

ABSTRACT: We propose a new batch mode active learning algorithm designed for neural networks and large query batch sizes. The method, Discriminative Active Learning (DAL), poses active learning as a binary classification task, attempting to choose examples to label in such a way as to make the labeled set and the unlabeled pool indistinguishable. Experimenting on image classification tasks, we empirically show our method to be on par with state of the art methods in medium and large query batch sizes, while being simple to implement and also extend to other domains besides classification tasks. Our experiments also show that none of the state of the art methods of today are clearly better than uncertainty sampling, negating some of the reported results in the recent literature.

## item_id: m_0793

TITLE: Robust Graph Data Learning with Latent Graph Convolutional Representation

ABSTRACT: Graph Convolutional Representation (GCR) has achieved impressive performance for graph data representation. However, existing GCR is generally defined on the input fixed graph which may restrict the representation capacity and also be vulnerable to the structural attacks and noises. To address this issue, we propose a novel Latent Graph Convolutional Representation (LatGCR) for robust graph data representation and learning. Our LatGCR is derived based on reformulating graph convolutional representation from the aspect of graph neighborhood reconstruction. Given an input graph $\textbf{A}$, LatGCR aims to generate a flexible latent graph $\tilde{\textbf{A}}$ for graph convolutional representation which obviously enhances the representation capacity and also performs robustly w.r.t graph structural attacks and noises. Moreover, LatGCR is implemented in a self-supervised manner and thus provides a basic block for both supervised and unsupervised graph learning tasks. Experiments on several datasets demonstrate the effectiveness and robustness of LatGCR.

## item_id: m_0794

TITLE: On the Information Bottleneck Theory of Deep Learning

ABSTRACT: The practical successes of deep neural networks have not been matched by theoretical progress that satisfyingly explains their behavior. In this work, we study the information bottleneck (IB) theory of deep learning, which makes three specific claims: first, that deep networks undergo two distinct phases consisting of an initial fitting phase and a subsequent compression phase; second, that the compression phase is causally related to the excellent generalization performance of deep networks; and third, that the compression phase occurs due to the diffusion-like behavior of stochastic gradient descent. Here we show that none of these claims hold true in the general case. Through a combination of analytical results and simulation, we demonstrate that the information plane trajectory is predominantly a function of the neural nonlinearity employed: double-sided saturating nonlinearities like tanh yield a compression phase as neural activations enter the saturation regime, but linear activation functions and single-sided saturating nonlinearities like the widely used ReLU in fact do not. Moreover, we find that there is no evident causal connection between compression and generalization: networks that do not compress are still capable of generalization, and vice versa. Next, we show that the compression phase, when it exists, does not arise from stochasticity in training by demonstrating that we can replicate the IB findings using full batch gradient descent rather than stochastic gradient descent. Finally, we show that when an input domain consists of a subset of task-relevant and task-irrelevant information, hidden representations do compress the task-irrelevant information, although the overall information about the input may monotonically increase with training time, and that this compression happens concurrently with the fitting process rather than during a subsequent compression period.

## item_id: m_0795

TITLE: SkipDecode: Autoregressive Skip Decoding with Batching and Caching for Efficient LLM Inference

ABSTRACT: Autoregressive large language models (LLMs) have made remarkable progress in various natural language generation tasks. However, the high computing cost and latency resulting from token-by-token generation impede their widespread adoption. To address this issue, several approaches have been proposed that reduce computational cost using early-exit strategies. These strategies enable faster text generation using reduced computation without applying the full computation graph to each token. While existing token-level early exit methods show promising results for online inference – they cannot be readily applied for batch inferencing and Key-Value caching. This is because they have to wait until the last token in a batch exits before they can stop computing. This severely limits the practical application of such techniques. In this paper, we propose a simple and effective token-level early exit method, SkipDecode, designed to work seamlessly with batch inferencing and KV caching. It overcomes prior constraints by setting up a singular exit point for every token in a batch at a each sequence position. It also guarantees a monotonic decrease in exit points, thereby eliminating the need to recompute KV Caches for preceding tokens. Rather than terminating computation prematurely as in prior works, our approach bypasses lower to middle layers, devoting most of the computational resources to upper layers, allowing later tokens to benefit from the compute expenditure by earlier tokens. Our experimental results show that SkipDecode can obtain 2x to 5x inference speedups with negligible regression across a variety of tasks. This is achieved using OPT models of 1.3 billion and 6.7 billion parameters, all the while being directly compatible with batching and KV caching optimization techniques.

## item_id: m_0796

TITLE: Global Self-Attention Networks for Image Recognition

ABSTRACT: Recently, a series of works in computer vision have shown promising results on various image and video understanding tasks using self-attention. However, due to the quadratic computational and memory complexities of self-attention, these works either apply attention only to low-resolution feature maps in later stages of a deep network or restrict the receptive field of attention in each layer to a small local region. To overcome these limitations, this work introduces a new global self-attention module, referred to as the GSA module, which is efficient enough to serve as the backbone component of a deep network. This module consists of two parallel layers: a content attention layer that attends to pixels based only on their content and a positional attention layer that attends to pixels based on their spatial locations. The output of this module is the sum of the outputs of the two layers. Based on the proposed GSA module, we introduce new standalone global attention-based deep networks that use GSA modules instead of convolutions to model pixel interactions. Due to the global extent of the proposed GSA module, a GSA network has the ability to model long-range pixel interactions throughout the network. Our experimental results show that GSA networks outperform the corresponding convolution-based networks significantly on the CIFAR-100 and ImageNet datasets while using less number of parameters and computations. The proposed GSA networks also outperform various existing attention-based networks on the ImageNet dataset.

## item_id: m_0797

TITLE: Compositional Obverter Communication Learning from Raw Visual Input

ABSTRACT: One of the distinguishing aspects of human language is its compositionality, which allows us to describe complex environments with limited vocabulary. Previously, it has been shown that neural network agents can learn to communicate in a highly structured, possibly compositional language based on disentangled input (e.g. hand- engineered features). Humans, however, do not learn to communicate based on well-summarized features. In this work, we train neural agents to simultaneously develop visual perception from raw image pixels, and learn to communicate with a sequence of discrete symbols. The agents play an image description game where the image contains factors such as colors and shapes. We train the agents using the obverter technique where an agent introspects to generate messages that maximize its own understanding. Through qualitative analysis, visualization and a zero-shot test, we show that the agents can develop, out of raw image pixels, a language with compositional properties, given a proper pressure from the environment.

## item_id: m_0798

TITLE: ComposerFlow: Step-by-Step Compositional Song Generation

ABSTRACT: Song generation models seek to produce audio recordings with vocals and instrumental accompaniment from user-provided lyrics and textual descriptions. While *end-to-end* approaches yield compelling results, they demand vast training data and computational resources. In this paper, we demonstrate that a *compositional* approach can make song generation far more data-efficient by decomposing the task into three sequential sub-tasks: melody composition, singing voice synthesis, and accompaniment generation. Although prior work exists for each sub-task, we show that naively chaining off-the-shelf models yields suboptimal outcomes. Instead, these components must be re-engineered with song generation in mind. To this end, we introduce *MIDI-informed* singing accompaniment generation — a novel technique unexplored in prior literature — that conditions accompaniment on MIDI representations of vocal melody, empirically enhancing rhythmic and harmonic consistency between singing and instrumentation. By integrating pre-existing models with our newly trained components (requiring only 6k hours of audio data on a single RTX 3090 GPU), our pipeline achieves perceptual quality on par with leading end-to-end open-source models, while offering advantages in training efficiency, licensed singing voices from professional artists, and editable intermediates. We provide audio demos and will open-source our model at https://composerflow.github.io/web/.

## item_id: m_0799

TITLE: Learning to Teach

ABSTRACT: Teaching plays a very important role in our society, by spreading human knowledge and educating our next generations. A good teacher will select appropriate teaching materials, impact suitable methodologies, and set up targeted examinations, according to the learning behaviors of the students. In the field of artificial intelligence, however, one has not fully explored the role of teaching, and pays most attention to machine \emph{learning}. In this paper, we argue that equal attention, if not more, should be paid to teaching, and furthermore, an optimization framework (instead of heuristics) should be used to obtain good teaching strategies. We call this approach ``learning to teach''. In the approach, two intelligent agents interact with each other: a student model (which corresponds to the learner in traditional machine learning algorithms), and a teacher model (which determines the appropriate data, loss function, and hypothesis space to facilitate the training of the student model). The teacher model leverages the feedback from the student model to optimize its own teaching strategies by means of reinforcement learning, so as to achieve teacher-student co-evolution. To demonstrate the practical value of our proposed approach, we take the training of deep neural networks (DNN) as an example, and show that by using the learning to teach techniques, we are able to use much less training data and fewer iterations to achieve almost the same accuracy for different kinds of DNN models (e.g., multi-layer perceptron, convolutional neural networks and recurrent neural networks) under various machine learning tasks (e.g., image classification and text understanding).

## item_id: m_0800

TITLE: PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction

ABSTRACT: The crystal structure can be simplified as a periodic point set repeating across the entire three-dimensional space along an underlying lattice. Traditionally, methods for representing crystals rely on descriptors like lattice parameters, symmetry, and space groups to characterize the structure. However, in reality, atoms in material always vibrate above absolute zero, causing continuous fluctuations in their positions. This dynamic behavior disrupts the underlying periodicity of the lattice, making crystal graphs based on static lattice parameters and conventional descriptors discontinuous under even slight perturbations. To this end, chemists proposed the Pairwise Distance Distribution (PDD) method, which has been used to distinguish all periodic structures in the world's largest real materials collection, the Cambridge Structural Database. However, achieving the completeness of PDD requires defining a large number of neighboring atoms, resulting in high computational costs. Moreover, it does not account for atomic information, making it challenging to directly apply PDD to crystal material property prediction tasks. To address these challenges, we propose the atom-Weighted Pairwise Distance Distribution (WPDD) and Unit cell Pairwise Distance Distribution (UPDD) for the first time, incorporating them into the construction of multi-edge crystal graphs. Based on this, we further developed WPDDFormer and UPDDFormer, graph transformer architecture constructed using WPDD and UPDD crystal graphs. We demonstrate that this method maintains the continuity and completeness of crystal graphs even under slight perturbations in atomic positions. Moreover, by modeling PDD as global information and integrating it into matrix-based message passing, we significantly reduced computational costs. Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT.
