# Batch 25 — 100 items

## item_id: m_2401

TITLE: Retro*: Optimizing LLMs for Reasoning-Intensive Document Retrieval

ABSTRACT: With the growing popularity of LLM agents and RAG, it has become increasingly important to retrieve documents that are essential for solving a task, even when their connection to the task is indirect or implicit. Addressing this problem requires fine-grained reasoning to accurately assess the relevance between the task and each candidate document. This capability, however, poses a significant challenge for existing IR techniques. Despite recent progress in reasoning-enhanced IR, existing approaches still face significant challenges in applicability, scalability, and efficiency. In this work, we propose **Retro\***, a novel approach for reasoning-intensive document retrieval. Our method introduces a rubric-based relevance **scoring mechanism**, enabling the model to reason about the relationship between a task and a document based on explicitly defined criteria, whereby producing a fine-grained, interpretable relevance score. Retro\* also supports **test-time scaling** by combining multiple reasoning trajectories via score integration, which produces more reliable relevance estimates. To optimize Retro\*'s reasoning capabilities, we introduce a novel **reinforcement learning** algorithm tailored for its relevance scoring mechanism, which employs two composite rewards to fully exploit the trajectories of each training sample. Our experiments show that Retro\* outperforms existing document retrieval methods with notable advantages, leading to **state-of-the-art** performance on the BRIGHT benchmark.

## item_id: m_2402

TITLE: Spectral Subgraph Localization

ABSTRACT: Several graph mining problems are based on some variant of the subgraph isomorphism problem: Given two graphs, G and Q, does G contain a subgraph isomorphic to Q? As this problem is NP-hard, many methods avoid addressing it explicitly. In this paper, we propose a method that solves the problem by localizing, i.e., finding the position of, Q in G, by means of an alignment among graph spectra. Finding a node correspondence from Q to G thereafter is relegated to a separate task, as an instance of the graph alignment problem. We demonstrate that our spectral approach outperforms a baseline based on the state-of-the-art method for graph alignment in terms of accuracy on real graphs and scales to hundreds of nodes as no other method does.

## item_id: m_2403

TITLE: Spherical CNNs on Unstructured Grids

ABSTRACT: We present an efficient convolution kernel for Convolutional Neural Networks (CNNs) on unstructured grids using parameterized differential operators while focusing on spherical signals such as panorama images or planetary signals. 
To this end, we replace conventional convolution kernels with linear combinations of differential operators that are weighted by learnable parameters. Differential operators can be efficiently estimated on unstructured grids using one-ring neighbors, and learnable parameters can be optimized through standard back-propagation. As a result, we obtain extremely efficient neural networks that match or outperform state-of-the-art network architectures in terms of performance but with a significantly lower number of network parameters. We evaluate our algorithm in an extensive series of experiments on a variety of computer vision and climate science tasks, including shape classification, climate pattern segmentation, and omnidirectional image semantic segmentation. Overall, we present (1) a novel CNN approach on unstructured grids using parameterized differential operators for spherical signals, and (2) we show that our unique kernel parameterization allows our model to achieve the same or higher accuracy with significantly fewer network parameters.

## item_id: m_2404

TITLE: Scalable Neural Network Kernels

ABSTRACT: We introduce the concept of scalable neural network kernels (SNNKs), the replacements of regular feedforward layers (FFLs), capable of approximating the latter, but with favorable computational properties. SNNKs effectively disentangle the inputs from the parameters of the neural network in the FFL, only to connect them in the final computation via the dot-product kernel. 
They are also strictly more expressive, as allowing to model complicated relationships beyond the functions of the dot-products of parameter-input vectors. We also introduce the neural network bundling process that applies SNNKs to compactify deep neural network architectures, resulting in additional compression gains. In its extreme version, it leads to the fully bundled network whose optimal parameters can be expressed via explicit formulae for several loss functions (e.g. mean squared error), opening a possibility to bypass backpropagation. As a by-product of our analysis, we introduce the mechanism of the universal random features (or URFs), applied to instantiate several SNNK variants, and interesting on its own in the context of scalable kernel methods. We provide rigorous theoretical analysis of all these concepts as well as an extensive empirical evaluation, ranging from point-wise kernel estimation to Transformers' fine-tuning with novel adapter layers inspired by SNNKs. Our mechanism provides up to 5x reduction in the number of trainable parameters, while maintaining competitive accuracy.

## item_id: m_2405

TITLE: Watermark-based Detection and Attribution of AI-Generated Image

ABSTRACT: Several companies--such as Google, Microsoft, and OpenAI--have deployed techniques to watermark  AI-generated images to enable proactive detection. However, existing literature mainly focuses on user-agnostic detection. Attribution aims to further trace back the user who generated a  detected  AI-generated image. Despite its growing importance, attribution is largely unexplored. In this work, we aim to bridge this gap by providing the first systematic study on watermark-based, user-aware detection and attribution of AI-generated images. Specifically, we theoretically study the detection and attribution performance via rigorous probabilistic analysis. Moreover, we develop an efficient algorithm to select watermarks for the users to enhance attribution performance. Both our theoretical  and empirical results show that watermark-based detection and attribution inherit the accuracy and (non-)robustness properties of the watermarking method.

## item_id: m_2406

TITLE: Temporal and Object Quantification Nets

ABSTRACT: We aim to learn generalizable representations for complex activities by quantifying over both entities and time, as in “the kicker is behind all the other players,” or “the player controls the ball until it moves toward the goal.”  Such a structural inductive bias of object relations, object quantification, and temporal orders will enable the learned representation to generalize to situations with varying numbers of agents, objects, and time courses. In this paper, we present Temporal and Object Quantification Nets (TOQ-Nets), which provide such structural inductive bias for learning composable action concepts from time sequences that describe the properties and relations of multiple entities. We evaluate TOQ-Nets on two benchmarks: trajectory-based soccer event detection, and 6D pose-based manipulation concept learning. We demonstrate that TOQ-Nets can generalize from small amounts of data to scenarios where there are more agents and objects than were present during training. The learned concepts are also robust with respect to temporally warped sequences and easily transfer to other prediction tasks in a similar domain.

## item_id: m_2407

TITLE: BERTScore: Evaluating Text Generation with BERT

ABSTRACT: We propose BERTScore, an automatic evaluation metric for text generation. Analogously to common metrics, BERTScore computes a similarity score for each token in the candidate sentence with each token in the reference sentence. However, instead of exact matches, we compute token similarity using contextual embeddings. We evaluate using the outputs of 363 machine translation and image captioning systems. BERTScore correlates better with human judgments and provides stronger model selection performance than existing metrics. Finally, we use an adversarial paraphrase detection task and show that BERTScore is more robust to challenging examples compared to existing metrics. 

## item_id: m_2408

TITLE: Synchronized Contrastive Pruning for Efficient Self-Supervised Learning

ABSTRACT: Various self-supervised learning (SSL) methods have demonstrated strong capability in learning visual representations from unlabeled data. However, the current state-of-the-art (SoTA) SSL methods largely rely on heavy encoders to achieve comparable performance as the supervised learning counterpart. Despite the well-learned visual representations, the large-sized encoders impede the energy efficient computation, especially for resource-constrained edge computing. Prior works have utilized the sparsity-induced asymmetry to enhance the contrastive learning of dense models, but the generality between asymmetric sparsity and self-supervised learning has not been fully discovered. Furthermore, transferring the supervised sparse learning to SSL is also largely under-explored. To address the research gap in prior works, this paper investigates the correlation between in-training sparsity and SSL. In particular, we propose a novel sparse SSL algorithm, embracing the benefits of contrastiveness while exploiting high sparsity during SSL training. The proposed framework is evaluated comprehensively  with various granularities of sparsity, including element-wise sparsity, GPU-friendly N:M structured fine-grained sparsity, and hardware-specific structured sparsity. Extensive experiments across multiple datasets are performed, where the proposed method shows superior performance against the SoTA sparse learning algorithms with various SSL frameworks. Furthermore, the training speedup aided by the proposed method is evaluated with an actual DNN training accelerator model. 

## item_id: m_2409

TITLE: Is High Variance Unavoidable in RL? A Case Study in Continuous Control

ABSTRACT: Reinforcement learning (RL) experiments have notoriously high variance, and minor details can have disproportionately large effects on measured outcomes. This is problematic for creating reproducible research and also serves as an obstacle when applying RL to sensitive real-world applications. In this paper, we investigate causes for this perceived instability. To allow for an in-depth analysis, we focus on a specifically popular setup with high variance -- continuous control from pixels with an actor-critic agent. In this setting, we demonstrate that poor outlier runs which completely fail to learn are an important source of variance, but that weight initialization and initial exploration are not at fault. We show that one cause for these outliers is unstable network parametrization which leads to saturating nonlinearities. We investigate several fixes to this issue and find that simply normalizing penultimate features is surprisingly effective. For sparse tasks, we also find that partially disabling clipped double Q-learning decreases variance. By combining fixes we significantly decrease variances, lowering the average standard deviation across 21 tasks by a factor >3 for a state-of-the-art agent. This demonstrates that the perceived variance is not necessarily inherent to RL. Instead, it may be addressed via simple modifications and we argue that developing low-variance agents is an important goal for the RL community.

## item_id: m_2410

TITLE: Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models

ABSTRACT: The dominant paradigm for RLHF is *online* and *on-policy* RL: synchronously generating from the large language model (LLM) policy, labelling with a reward model, and learning using feedback on the LLM's own outputs. While performant, this paradigm is computationally inefficient. Inspired by classical deep RL literature, we propose separating generation and learning in RLHF. This enables asynchronous generation of new samples while simultaneously training  on old samples, leading to faster training and more compute-optimal scaling. However, asynchronous training relies on an underexplored regime, online but *off-policy* RLHF: learning on samples from previous iterations of our model which give a worse training signal. We tackle the fundamental challenge in this regime: how much off-policyness can we tolerate for asynchronous training to speed up learning but maintain performance? Among several RLHF algorithms we test, online DPO is found to be most robust to off-policy data, and robustness increases with the scale of the policy model. We study further compute optimizations for asynchronous RLHF but find that they come at a performance cost, giving rise to a trade-off. We verify the scalability of asynchronous RLHF by training a general-purpose chatbot from LLaMA 3.1 8B on an instruction-following task $\sim$40\% faster than a synchronous run while matching final performance. Finally, we extend our results to math and reasoning to demonstrate asynchronous RL can finetune Rho 1B on GSM8k $\sim$70\% faster while matching synchronous accuracy.

## item_id: m_2411

TITLE: Unified Removal of Raindrops and Reflections: A New Benchmark and A Novel Pipeline

ABSTRACT: When capturing images through glass surfaces or windshields on rainy days, raindrops and reflections frequently co-occur to significantly reduce the visibility of captured images. Prior de-raindrop and de-reflection studies have failed to simultaneously remove both types of degradations from a single captured image, thereby limiting their application and robustness in real-world scenarios. In this work, we make the first attempt to explore this new task, \ie, unified removal of raindrops and reflections (UR$^3$). First of all, we set up an image acquisition platform to collect our own dataset, namely RainDrop and ReFlection (RDRF) dataset, which provides a new benchmark with substantial, high-quality, diverse image pairs. Within each pair, one has a clean foreground and the rest is corrupted by raindrops and reflections. Second, we propose a diffusion-based framework (\ie, DiffUR$^3$) to decouple the UR$^3$ task into a restoration stage and a conditional generation stage (with multiple conditions). By leveraging the powerful generative prior, DiffUR$^3$ successfully removes both degradations. Extensive experiments demonstrate that our method achieves state-of-the-art performance on our benchmark and on challenging in-the-wild images. The RDRF dataset and the codes will be made public upon acceptance.

## item_id: m_2412

TITLE: Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors

ABSTRACT: Existing data poisoning attacks on retrieval-augmented generation (RAG) systems scale poorly because they require costly optimization of poisoned documents for each target phrase. We introduce Eyes-on-Me, a modular attack that decomposes an adversarial document into reusable **Attention Attractors** and **Focus Regions**. Attractors are optimized to direct attention to the Focus Region. Attackers can then insert semantic baits for the retriever or malicious instructions for the generator, adapting to new targets at near zero cost. This is achieved by steering a small subset of attention heads that we empirically identify as strongly correlated with attack success. Across 18 end-to-end RAG settings (3 datasets $\times$ 2 retrievers $\times$ 3 generators), Eyes-on-Me raises average attack success rates from 21.9 to 57.8 (+35.9 points, 2.6$\times$ over prior work). A single optimized attractor transfers to unseen black box retrievers and generators without retraining. Our findings establish a scalable paradigm for RAG data poisoning and show that modular, reusable components pose a practical threat to modern AI systems. They also reveal a strong link between attention concentration and model outputs, informing interpretability research.

## item_id: m_2413

TITLE: Compressed-VFL: Communication-Efficient Learning with Vertically Partitioned Data

ABSTRACT: We propose Compressed Vertical Federated Learning (C-VFL) for communication-efficient training on vertically partitioned data. In C-VFL, a server and multiple parties collaboratively train a model on their respective features utilizing several local iterations and sharing compressed intermediate results periodically. Our work provides the first theoretical analysis of the effect message compression has on distributed training over vertically partitioned data. We prove convergence of non-convex objectives to a fixed point at a rate of $O(\frac{1}{\sqrt{T}})$ when the compression error is bounded over the course of training. We provide specific requirements for convergence with common compression techniques, such as quantization and top-$k$ sparsification. Finally, we experimentally show compression can reduce communication by over $90\%$ without a significant decrease in accuracy over VFL without compression.

## item_id: m_2414

TITLE: Bayesian Exploration for Lifelong Reinforcement Learning

ABSTRACT: A central question in reinforcement learning (RL) is how to leverage prior knowledge to accelerate learning in new tasks.  We propose a Bayesian exploration method for lifelong reinforcement learning (BLRL) that aims to learn a Bayesian posterior that distills the common structure shared across different tasks. We further derive a sample complexity analysis of BLRL in the finite MDP setting. To scale our approach, we propose a variational Bayesian Lifelong Learning (VBLRL) algorithm that is based on Bayesian neural networks, can be combined with recent model-based RL methods, and exhibits backward transfer. Experimental results on three challenging domains show that our algorithms adapt to new tasks faster than state-of-the-art lifelong RL methods.

## item_id: m_2415

TITLE: offline_rl_ope: A Python package for off-policy evaluation of offline RL models with real world data

ABSTRACT: offline_rl_ope is a fully unit tested and runtime type checked Python package for performing off-policy evaluation of offline RL models. offline_rl_ope has been designed for OPE workflows using real world data by: naturally handling uneven trajectory lengths; including novel convergence metrics which do not rely on OPE estimator ground truths; and providing a compute and data efficient API which can be integrated with many offline RL frameworks. This paper motivates and describes the core API design and functionality to enable ease of use and extension. The implementations of OPE methods have been benchmarked against existing implementations to ensure consistency and reproducibility. The offline_rl_ope source code can be found on GitHub at: REDACTED.

## item_id: m_2416

TITLE: Cross-Lingual Vision-Language Navigation

ABSTRACT: Vision-Language Navigation (VLN) is the task where an agent is commanded to navigate in photo-realistic unknown environments with natural language instructions. Previous research on VLN is primarily conducted on the Room-to-Room (R2R) dataset with only English instructions.  The ultimate goal of VLN, however, is to serve people speaking arbitrary languages. Towards multilingual VLN with numerous languages, we collect a cross-lingual R2R dataset, which extends the original benchmark with corresponding Chinese instructions. But it is time-consuming and expensive to collect large-scale human instructions for every existing language. Based on the newly introduced dataset, we propose a general cross-lingual VLN framework to enable instruction-following navigation for different languages. We first explore the possibility of building a cross-lingual agent when no training data of the target language is available. The cross-lingual agent is equipped with a meta-learner to aggregate cross-lingual representations and a visually grounded cross-lingual alignment module to align textual representations of different languages. Under the zero-shot learning scenario, our model shows competitive results even compared to a model trained with all target language instructions. In addition, we introduce an adversarial domain adaption loss to improve the transferring ability of our model when given a certain amount of target language data. Our methods and dataset demonstrate the potentials of building a cross-lingual agent to serve speakers with different languages.

## item_id: m_2417

TITLE: Modifying memories in a Recurrent Neural Network Unit

ABSTRACT: Long Short-Term Memory (LSTM) units have the ability to memorise and use long-term dependencies between inputs to generate predictions on time series data. We introduce the concept of modifying the cell state (memory) of LSTMs using rotation matrices parametrised by a new set of trainable weights. This addition shows significant increases of performance on some of the tasks from the bAbI dataset.

## item_id: m_2418

TITLE: LEARNING GENERATIVE MODELS FOR DEMIXING OF STRUCTURED SIGNALS FROM THEIR SUPERPOSITION USING GANS

ABSTRACT: Recently, Generative Adversarial Networks (GANs) have emerged as a popular alternative for modeling complex high dimensional distributions. Most of the existing works implicitly assume that the clean samples from the target distribution are easily available. However, in many applications, this assumption is violated. In this paper, we consider the problem of learning GANs under the observation setting when the samples from target distribution are given by the superposition of two structured components. We propose two novel frameworks: denoising-GAN and demixing-GAN. The denoising-GAN assumes access to clean samples from the second component and try to learn the other distribution, whereas demixing-GAN learns the distribution of the components at the same time. Through comprehensive numerical experiments, we demonstrate that proposed frameworks can generate clean samples from unknown distributions, and provide competitive performance in tasks such as denoising, demixing, and compressive sensing.

## item_id: m_2419

TITLE: Flow-based Recurrent Belief State Learning for POMDPs

ABSTRACT: Partially Observable Markov Decision Process (POMDP) provides a principled and generic framework to model real world sequential decision making processes but yet remains unsolved, especially for high dimensional continuous space and unknown models. The main challenge lies in how to accurately obtain the belief state, which is the probability distribution over the unobservable environment states given historical information. Accurately calculating this belief state is a precondition for obtaining an optimal policy of POMDPs. Recent advances in deep learning techniques show great potential to learn good belief states, but they assume the belief states follow certain types of simple distributions such as diagonal Gaussian, which imposes strong restrictions to precisely capture the real belief states. In this paper, we introduce the \textbf{F}l\textbf{O}w-based \textbf{R}ecurrent \textbf{BE}lief \textbf{S}tate model (FORBES), which incorporates normalizing flows into the variational inference to learn general continuous belief states for POMDPs. Furthermore, we show that the learned belief states can be plugged into downstream RL algorithms to improve performance. In experiments, we show that our methods successfully capture the complex belief states that enable multi-modal predictions as well as high quality reconstructions, and results on challenging visual-motor control tasks show that our method achieves superior performance and sample efficiency.

## item_id: m_2420

TITLE: Gaussian-Bernoulli RBMs Without Tears

ABSTRACT: We revisit the challenging problem of training Gaussian-Bernoulli restricted Boltzmann machines (GRBMs), introducing two innovations. We propose a novel Gibbs-Langevin sampling algorithm that outperforms existing methods like Gibbs sampling.
We propose a modified contrastive divergence (CD) algorithm so that one can generate images with GRBMs starting from noise.
This enables direct comparison of GRBMs with deep generative models, improving evaluation protocols in the RBM literature. 
Moreover, we show that modified CD and gradient clipping are enough to robustly train GRBMs with large learning rates, thus removing the necessity of various tricks in the literature.
Experiments on Gaussian Mixtures, MNIST, FashionMNIST, and CelebA show GRBMs can generate good samples, despite their single-hidden-layer architecture. 

## item_id: m_2421

TITLE: Graph2Seq: Graph to Sequence Learning with Attention-Based Neural Networks

ABSTRACT: The celebrated Sequence to Sequence learning (Seq2Seq) technique and its numerous variants achieve excellent performance on many tasks. However, many machine learning tasks have inputs naturally represented as graphs; existing Seq2Seq models face a significant challenge in achieving accurate conversion from graph form to the appropriate sequence. To address this challenge, we introduce a general end-to-end graph-to-sequence neural encoder-decoder architecture that maps an input graph to a sequence of vectors and uses an attention-based LSTM method to decode the target sequence from these vectors. Our method first generates the node and graph embeddings using an improved graph-based neural network with a novel aggregation strategy to incorporate edge direction information in the node embeddings. We further introduce an attention mechanism that aligns node embeddings and the decoding sequence to better cope with large graphs. Experimental results on bAbI, Shortest Path, and Natural Language Generation tasks demonstrate that our model achieves state-of-the-art performance and significantly outperforms existing graph neural networks, Seq2Seq, and Tree2Seq models; using the proposed bi-directional node embedding aggregation strategy, the model can converge rapidly to the optimal performance.

## item_id: m_2422

TITLE: The Benefits of Being Categorical Distributional: Uncertainty-aware Regularized Exploration in Reinforcement Learning

ABSTRACT: Despite the remarkable empirical performance of distributional reinforcement learning (RL), its theoretical advantages over classical RL are not fully understood. Starting with Categorical Distributional RL (CDRL), we propose that the potential superiority of distributional RL can be attributed to a derived distribution-matching regularization by applying a return density function decomposition technique. This less-studied regularization in the distributional RL context aims to capture additional knowledge of return distribution beyond only its expectation, contributing to an augmented reward signal in policy optimization. In contrast to the standard entropy regularization in MaxEnt RL, which explicitly encourages exploration by promoting diverse actions, the regularization derived from CDRL implicitly updates policies to align the learned policy with environmental uncertainty. Finally, extensive experiments substantiate the significance of this uncertainty-aware regularization derived from distributional RL on the empirical benefits over classical RL. Our study offers a new perspective from the exploration to explain the benefits of adopting distributional learning in RL.

## item_id: m_2423

TITLE: RotoGBML: Towards Out-of-Distribution Generalization for Gradient-Based Meta-Learning

ABSTRACT: Gradient-based meta-learning (GBML) algorithms are able to fast adapt to new tasks by transferring the learned meta-knowledge, while assuming that all tasks come from the same distribution (in-distribution, ID). However, in the real world, they often suffer from an out-of-distribution (OOD) generalization problem, where tasks come from different distributions. OOD exacerbates inconsistencies in magnitudes and directions of task gradients, which brings challenges for GBML to optimize the meta-knowledge by minimizing the sum of task gradients in each minibatch. To address this problem, we propose RotoGBML, a novel approach to homogenize OOD task gradients. RotoGBML uses reweighted vectors to dynamically balance diverse magnitudes to a common scale and uses rotation matrixes to rotate conflicting directions close to each other. To reduce overhead, we homogenize gradients with the features rather than the network parameters. On this basis, to avoid the intervention of non-causal features (e.g., backgrounds), we also propose an invariant self-information (ISI) module to extract invariant causal features (e.g., the outlines of objects). Finally, task gradients are homogenized based on these invariant causal features. Experiments show that RotoGBML outperforms other state-of-the-art methods on various few-shot image classification benchmarks.

## item_id: m_2424

TITLE: PISA: A Pragmatic Psych-Inspired Unified Memory System for Enhanced AI Agency

ABSTRACT: Memory systems are fundamental to AI agents, yet existing work often lacks adaptability to diverse tasks and overlooks the constructive and task-oriented role of AI agent memory.
Drawing from Piaget's theory of cognitive development, we propose PISA, a pragmatic, psych-inspired unified memory system that addresses these limitations by treating memory as a constructive and adaptive process. To enable continuous learning and adaptability, PISA introduces a trimodal adaptation mechanism (\textit{i.e.}, schema updation, schema evolution, and schema creation) that preserves coherent organization while supporting flexible memory updates. Building on these schema-grounded structures, we further design a hybrid memory access architecture that seamlessly integrates symbolic reasoning with neural retrieval, significantly improving retrieval accuracy and efficiency.
Our empirical evaluation, conducted on the existing LOCOMO benchmark and our newly proposed AggQA benchmark for data analysis tasks, confirms that PISA sets a new state-of-the-art by significantly enhancing adaptability and long-term knowledge retention.
The source code of PISA and data of AggQA are available at \url{https://anonymous.4open.science/r/PISA-421/}

## item_id: m_2425

TITLE: Reward Collapse in Aligning Large Language Models

ABSTRACT: The extraordinary capabilities of large language models (LLMs) such as ChatGPT and GPT-4 are in part unleashed by aligning them with reward models that are trained on human preferences represented as rankings of responses to prompts. In this paper, we document the phenomenon of reward collapse, an empirical observation where the prevailing ranking-based approach results in an identical reward distribution for diverse prompts during the terminal phase of training. This outcome is undesirable as open-ended prompts like write a short story about your best friend'' should yield a continuous range of rewards for their completions, while specific prompts like what is the capital city of New Zealand'' should generate either high or low rewards. Our theoretical investigation reveals that reward collapse is primarily due to the insufficiency of the ranking-based objective function to incorporate prompt-related information during optimization. This insight allows us to derive closed-form expressions for the reward distribution associated with a set of utility functions in an asymptotic setting. To overcome reward collapse, we introduce a prompt-aware optimization scheme that provably admits a prompt-dependent reward distribution within the interpolating regime. Our experimental results suggest that our proposed prompt-aware utility functions significantly alleviate reward collapse during the training of reward models.

## item_id: m_2426

TITLE: Filter Training and Maximum Response: Classification via Discerning

ABSTRACT: This report introduces a training and recognition scheme, in which classification is realized via class-wise discerning. Trained with datasets whose labels are randomly shuffled except for one class of interest, a neural network learns class-wise parameter values, and remolds itself from a feature sorter into feature filters, each of which discerns objects belonging to one of the classes only. Classification of an input can be inferred from the maximum response of the filters. A multiple check with multiple versions of filters can diminish fluctuation and yields better performance. This scheme of discerning, maximum response and multiple check is a method of general viability to improve performance of feedforward networks, and the filter training itself is a promising feature abstraction procedure. In contrast to the direct sorting, the scheme mimics the classification process mediated by a series of one component picking.

## item_id: m_2427

TITLE: How to train RNNs on chaotic data?

ABSTRACT: Recurrent neural networks (RNNs) are wide-spread machine learning tools for modeling sequential and time series data. They are notoriously hard to train because their loss gradients backpropagated in time tend to saturate or diverge during training. This is known as the exploding and vanishing gradient problem. Previous solutions to this issue either built on rather complicated, purpose-engineered architectures with gated memory buffers, or - more recently - imposed constraints that ensure convergence to a fixed point or restrict (the eigenspectrum of) the recurrence matrix. Such constraints, however, convey severe limitations on the expressivity of the RNN. Essential intrinsic dynamics such as multistability or chaos are disabled. This is inherently at disaccord with the chaotic nature of many, if not most, time series encountered in nature and society. Here we offer a comprehensive theoretical treatment of this problem by relating the loss gradients during RNN training to the Lyapunov spectrum of RNN-generated orbits. We mathematically prove that RNNs producing stable equilibrium or cyclic behavior have bounded gradients, whereas the gradients of RNNs with chaotic dynamics always diverge. Based on these analyses and insights, we offer an effective yet simple training technique for chaotic data and guidance on how to choose relevant hyperparameters according to the Lyapunov spectrum. 


## item_id: m_2428

TITLE: Why Gradient Clipping Accelerates Training: A Theoretical Justification for Adaptivity

ABSTRACT: We provide a theoretical explanation for the effectiveness of gradient clipping in training deep neural networks. The key ingredient is a new smoothness condition derived from practical neural network training examples. We observe that gradient smoothness, a concept central to the analysis of first-order optimization algorithms that is often assumed to be a constant, demonstrates significant variability along the training trajectory of deep neural networks. Further, this smoothness positively correlates with the gradient norm, and contrary to standard assumptions in the literature, it can grow with the norm of the gradient. These empirical observations limit the applicability of existing theoretical analyses of algorithms that rely on a fixed bound on smoothness. These observations motivate us to introduce a novel relaxation of gradient smoothness that is weaker than the commonly used Lipschitz smoothness assumption. Under the new condition, we prove that two popular methods, namely, gradient clipping and normalized gradient, converge arbitrarily faster than gradient descent with fixed stepsize. We further explain why such adaptively scaled gradient methods can accelerate empirical convergence and verify our results empirically in popular neural network training settings.

## item_id: m_2429

TITLE: Gradient Flow Provably Learns Robust Classifiers for Data from Orthonormal Clusters

ABSTRACT: Deep learning-based classifiers are known to be vulnerable to adversarial attacks. Existing methods for defending against such attacks require adding a defense mechanism or modifying the learning procedure (e.g., by adding adversarial examples). This paper shows that for certain data distribution one can learn a provably robust classifier using standard learning methods and without adding a defense mechanism. More specifically, this paper addresses the problem of finding a robust classifier for a binary classification problem in which the data comes from a mixture of Gaussian clusters with orthonormal cluster centers. First, we characterize the largest $\ell_2$-attack any classifier can defend against while maintaining high accuracy, and show the existence of optimal robust classifiers achieving this maximum $\ell_2$-robustness. Next, we show that given data sampled from the orthonormal cluster model, gradient flow on a two-layer network with a polynomial ReLU activation and without adversarial examples provably finds an optimal robust classifier.

## item_id: m_2430

TITLE: Provably More Efficient Q-Learning in the One-Sided-Feedback/Full-Feedback Settings

ABSTRACT: Motivated by the episodic version of the classical inventory control problem, we propose a new Q-learning-based algorithm, Elimination-Based Half-Q-Learning (HQL), that enjoys improved efficiency over existing algorithms for a wide variety of problems in the one-sided-feedback setting. We also provide a simpler variant of the algorithm, Full-Q-Learning (FQL), for the full-feedback setting. We establish that HQL incurs $ \tilde{\mathcal{O}}(H^3\sqrt{ T})$ regret and FQL incurs $\tilde{\mathcal{O}}(H^2\sqrt{ T})$ regret, where $H$ is the length of each episode and $T$ is the total length of the horizon. The regret bounds are not affected by the possibly huge state and action space. Our numerical experiments demonstrate the superior efficiency of HQL and FQL, and the potential to combine reinforcement learning with richer feedback models.

## item_id: m_2431

TITLE: Fuzzy paraphrases in learning word representations with a lexicon

ABSTRACT: A synonym of a polysemous word is usually only the paraphrase of one sense among many. When lexicons are used to improve vector-space word representations, such paraphrases are unreliable and bring noise to the vector-space. The prior works use a coefficient to adjust the overall learning of the lexicons. They regard the paraphrases equally. 
In this paper, we propose a novel approach that regards the paraphrases diversely to alleviate the adverse effects of polysemy. We annotate each paraphrase with a degree of reliability. The paraphrases are randomly eliminated according to the degrees when our model learns word representations. In this way, our approach drops the unreliable paraphrases, keeping more reliable paraphrases at the same time. The experimental results show that the proposed method improves the word vectors.
Our approach is an attempt to address the polysemy problem keeping one vector per word. It makes the approach easier to use than the conventional methods that estimate multiple vectors for a word. Our approach also outperforms the prior works in the experiments.

## item_id: m_2432

TITLE: Neural-Guided Deductive Search for Real-Time Program Synthesis from Examples

ABSTRACT: Synthesizing user-intended programs from a small number of input-output exam-
ples is a challenging problem with several important applications like spreadsheet
manipulation, data wrangling and code refactoring. Existing synthesis systems
either completely rely on deductive logic techniques that are extensively hand-
engineered or on purely statistical models that need massive amounts of data, and in
general fail to provide real-time synthesis on challenging benchmarks. In this work,
we propose Neural Guided Deductive Search (NGDS), a hybrid synthesis technique
that combines the best of both symbolic logic techniques and statistical models.
Thus, it produces programs that satisfy the provided specifications by construction
and generalize well on unseen examples, similar to data-driven systems. Our
technique effectively utilizes the deductive search framework to reduce the learning
problem of the neural component to a simple supervised learning setup. Further,
this allows us to both train on sparingly available real-world data and still leverage
powerful recurrent neural network encoders. We demonstrate the effectiveness
of our method by evaluating on real-world customer scenarios by synthesizing
accurate programs with up to 12× speed-up compared to state-of-the-art systems.

## item_id: m_2433

TITLE: Neural Sketch Learning for Conditional Program Generation

ABSTRACT: We study the problem of generating source code in a strongly typed,
Java-like programming language, given a label (for example a set of
API calls or types) carrying a small amount of information about the
code that is desired. The generated programs are expected to respect a
`"realistic" relationship between programs and labels, as exemplified
by a corpus of labeled programs available during training.

Two challenges in such *conditional program generation* are that
the generated programs must satisfy a rich set of syntactic and
semantic constraints, and that source code contains many low-level
features that impede learning.  We address these problems by training
a neural generator not on code but on *program sketches*, or
models of program syntax that abstract out names and operations that
do not generalize across programs. During generation, we infer a
posterior distribution over sketches, then concretize samples from
this distribution into type-safe programs using combinatorial
techniques.  We implement our ideas in a system for generating
API-heavy Java code, and show that it can often predict the entire
body of a method given just a few API calls or data types that appear
in the method.

## item_id: m_2434

TITLE: GeoSeq2Seq: Information Geometric Sequence-to-Sequence Networks

ABSTRACT: The Fisher information metric is an important foundation of information geometry, wherein it allows us to approximate the local geometry of a probability distribution. Recurrent neural networks such as the Sequence-to-Sequence (Seq2Seq) networks that have lately been used to yield state-of-the-art performance on speech translation or image captioning have so far ignored the geometry of the latent embedding, that they iteratively learn. We propose the information geometric Seq2Seq (GeoSeq2Seq) network which abridges the gap between deep recurrent neural networks and information geometry. Specifically, the latent embedding offered by a recurrent network is encoded as a Fisher kernel of a parametric Gaussian Mixture Model, a formalism common in computer vision. We utilise such a network to predict the shortest routes between two nodes of a graph by learning the adjacency matrix using the GeoSeq2Seq formalism; our results show that for such a problem the probabilistic representation of the latent embedding supersedes the non-probabilistic embedding by 10-15\%.

## item_id: m_2435

TITLE: Sharper Rates and Flexible Framework for Nonconvex SGD with Client and Data Sampling

ABSTRACT: We revisit the classical problem of finding an approximately stationary point of the average of $n$ smooth and possibly nonconvex functions. The optimal complexity of stochastic first-order methods in terms of the number of gradient evaluations of individual functions is $\mathcal{O}\left(n + n^{1/2}\varepsilon^{-1}\right)$, attained by the optimal SGD methods SPIDER (Cong Fang et al., 2018) and PAGE (Zhize Li et al., 2020), for example, where $\varepsilon$ is the error tolerance. However, i) the big-$\mathcal{O}$ notation hides crucial dependencies on the smoothness constants associated with the functions, and ii) the rates and theory in these methods assume simplistic sampling mechanisms that do not offer any flexibility. In this work we remedy the situation. First, we generalize the PAGE algorithm so that it can provably work with virtually any (unbiased) sampling mechanism. This is particularly useful in federated learning, as it allows us to construct and better understand the impact of various combinations of client and data sampling strategies. Second, our analysis is sharper as we make explicit use of certain novel inequalities  that capture the intricate interplay between the smoothness constants and the sampling procedure. Indeed, our analysis is better even for the simple sampling procedure analyzed in the PAGE paper. However, this already improved bound can be further sharpened by a different sampling scheme which we propose. In summary, we provide the most general and most accurate analysis of optimal SGD in the smooth nonconvex regime. Finally, our theoretical findings are supposed with carefully designed experiments.

## item_id: m_2436

TITLE: Sound in Sights: Deriving Visual Insights from Audio for Comprehensive Video Understanding with Large Multimodal Models

ABSTRACT: Video understanding is inherently multimodal, requiring both visual and auditory cues to form a complete representation of dynamic scenes. However, most existing video understanding models rely solely on visual content, overlooking informative audio cues, such as spoken instructions or environmental sounds, for scene understanding and event comprehension. Progress in audio-visual reasoning has been hindered by the lack of high-quality supervised fine-tuning (SFT) data that jointly considers video and audio. To address this gap, we introduce SoundInSight, a large-scale audio-visual question answering dataset comprising over 80k question–answer pairs from online videos, created via a multimodal large language model (MLLM)-assisted annotation pipeline. SoundInSight provides rich supervision for audio-visual reasoning, enabling MLLMs to be fine-tuned for audio understanding. We find that current video MLLMs heavily rely on visual information, hindering effective multimodal learning. To mitigate this, we propose an audio-only pretraining stage, which significantly improves audio-visual reasoning performance. Additionally, to evaluate audio-visual comprehension, we construct a high-quality, manually curated test set of 1,000 samples requiring joint audio-visual understanding, exceeding standard benchmarks in complexity. Models fine-tuned on SoundInSight with the proposed training strategy achieve substantial performance gains on this new benchmark. Moreover, on the challenging VideoMME evaluation, our approach significantly improves performance in Information Synopsis subcategory, demonstrating the efficacy of incorporating audio. The SoundInSight dataset and code will be publicly released to facilitate further research.

## item_id: m_2437

TITLE: Plant 'n' Seek: Can You Find the Winning Ticket?

ABSTRACT: The lottery ticket hypothesis has sparked the rapid development of pruning algorithms that aim to reduce the computational costs associated with deep learning during training and model deployment. Currently, such algorithms are primarily evaluated on imaging data, for which we lack ground truth information and thus the understanding of how sparse lottery tickets could be. To fill this gap, we develop a framework that allows us to plant and hide winning tickets with desirable properties in randomly initialized neural networks. To analyze the ability of state-of-the-art pruning to identify tickets of extreme sparsity, we design and hide such tickets solving four challenging tasks. In extensive experiments, we observe similar trends as in imaging studies, indicating that our framework can provide transferable insights into realistic problems. Additionally, we can now see beyond such relative trends and highlight limitations of current pruning methods. Based on our results, we conclude that the current limitations in ticket sparsity are likely of algorithmic rather than fundamental nature. We anticipate that comparisons to planted tickets will facilitate future developments of efficient pruning algorithms.

## item_id: m_2438

TITLE: Assisted Learning for Organizations with Limited Imbalanced Data

ABSTRACT: We develop an assisted learning framework for assisting organization-level learners to improve their learning performance with limited and imbalanced data. In particular, learners at the organization level usually have sufficient computation resource, but are subject to stringent collaboration policy and information privacy. Their limited imbalanced data often cause biased inference and sub-optimal decision-making. In our assisted learning framework, an organizational learner purchases assistance service from a service provider and aims to enhance its model performance within a few assistance rounds. We develop effective stochastic training algorithms for assisted deep learning and assisted reinforcement learning. Different from existing distributed algorithms that need to frequently transmit gradients or models, our framework allows the learner to only occasionally share information with the service provider, and still achieve a near-oracle model as if all the data were centralized.

## item_id: m_2439

TITLE: Generalizing Hamiltonian Monte Carlo with Neural Networks

ABSTRACT: We present a general-purpose method to train Markov chain Monte Carlo kernels, parameterized by deep neural networks, that converge and mix quickly to their target distribution. Our method generalizes Hamiltonian Monte Carlo and is trained to maximize expected squared jumped distance, a proxy for mixing speed. We demonstrate large empirical gains on a collection of simple but challenging distributions, for instance achieving a 106x improvement in effective sample size in one case, and mixing when standard HMC makes no measurable progress in a second. Finally, we show quantitative and qualitative gains on a real-world task: latent-variable generative modeling. Python source code will be open-sourced with the camera-ready paper.

## item_id: m_2440

TITLE: NatADiff: Adversarial Boundary Guidance for Natural Adversarial Diffusion

ABSTRACT: Adversarial samples exploit irregularities in the manifold "learned" by deep learning models to cause misclassifications. The study of these adversarial samples provides insight into the features a model uses to classify inputs, which can be leveraged to improve robustness against future attacks. However, much of the existing literature focuses on constrained adversarial samples, which do not accurately reflect test-time errors encountered in real-world settings. To address this, we propose `NatADiff', an adversarial sampling scheme that leverages denoising diffusion to generate natural adversarial samples. Our approach is based on the observation that natural adversarial samples frequently contain structural elements from the adversarial class. Deep learning models can exploit these structural elements to shortcut the classification process, rather than learning to genuinely distinguish between classes. To leverage this behavior, we guide the diffusion trajectory towards the intersection of the true and adversarial classes, combining time-travel sampling with augmented classifier guidance to enhance attack transferability while preserving image quality. Our method achieves comparable white-box attack success rates to current state-of-the-art techniques, while exhibiting significantly higher transferability across model architectures and improved alignment with natural test-time errors as measured by FID. These results demonstrate that NatADiff produces adversarial samples that not only transfer more effectively across models, but more faithfully resemble naturally occurring test-time errors when compared with other generative adversarial sampling schemes.

## item_id: m_2441

TITLE: Learning Self-Similarity in Space and Time as a Generalized Motion for Action Recognition

ABSTRACT: Spatio-temporal convolution often fails to learn motion dynamics in videos and thus an effective motion representation is required for video understanding in the wild. In this paper, we propose a rich and robust motion representation method based on spatio-temporal self-similarity (STSS). Given a sequence of frames, STSS represents each local region as similarities to its neighbors in space and time. By converting appearance features into relational values, it enables the learner to better recognize structural patterns in space and time. We leverage the whole volume of STSS and let our model learn to extract an effective motion representation from it. 
The proposed method is implemented as a neural block, dubbed SELFY, that can be easily inserted into neural architectures and learned end-to-end without additional supervision. With a sufficient volume of the neighborhood in space and time, it effectively captures long-term interaction and fast motion in the video, leading to robust action recognition.
Our experimental analysis demonstrates its superiority over previous methods for motion modeling as well as its complementarity to spatio-temporal features from direct convolution. On the standard action recognition benchmarks, Something-Something-V1 & V2, Diving-48, and FineGym, the proposed method achieves the state-of-the-art results.  

## item_id: m_2442

TITLE: Amata: An Annealing Mechanism for Adversarial Training Acceleration

ABSTRACT: Despite of the empirical success in various domains, it has been revealed that deep neural networks are vulnerable to maliciously perturbed input data that much degrade their performance. This is known as adversarial attacks. To counter adversarial attacks, adversarial training formulated as a form of robust optimization has been demonstrated to be effective. However, conducting adversarial training brings much computational overhead compared with standard training. In order to reduce the computational cost, we propose a simple yet effective modification to the commonly used projected gradient descent (PGD) adversarial training by increasing the number of adversarial training steps and decreasing the adversarial training step size gradually as training proceeds. We analyze the optimality of this annealing mechanism through the lens of optimal control theory, and we also prove the convergence of our proposed algorithm. Numerical experiments on standard datasets, such as MNIST and CIFAR10, show that our method can achieve similar or even better robustness with around 1/3 to 1/2 computation time compared with PGD.

## item_id: m_2443

TITLE: Connecting Data to Mechanisms with Meta Structual Causal Model

ABSTRACT: Recent years have seen impressive progress in theoretical and algorithmic developments of causal inference across various disciplines in science and engineering. However, there is still some unresolved theoretical problems, especially for cyclic causal relationships. In this article, we propose a meta structure causal model (Meta-SCM) framework inspired by understanding causality as information transfer. A key feature of our framework is the introduction of the concept of \emph{active mechanisms} to connect data and the collection of underlying causal mechanisms. We show that the Meta-SCM provides a novel approach to address the theoretical complications for modeling cyclic causal relations. In addition, we propose a \emph{sufficient activated mechanisms} assumption, and explain its relationship with existing assumptions in causal representation learning.  Finally, we conclude the main idea of the meta-SCM framework with an emphasis on its theoretical and conceptual novelty.

## item_id: m_2444

TITLE: LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable capabilities through pretraining and alignment. However, superior short-context LLMs may underperform in long-context scenarios due to insufficient long-context alignment. This alignment process remains challenging due to the impracticality of human annotation for extended contexts and the difficulty in balancing short- and long-context performance. To address these challenges, we introduce LongPO, that enables short-context LLMs to self-evolve to excel on long-context tasks by internally transferring short-context capabilities. LongPO harnesses LLMs to learn from self-generated short-to-long preference data, comprising paired responses generated for identical instructions with long-context inputs and their compressed short-context counterparts, respectively. This preference reveals capabilities and potentials of LLMs cultivated during short-context alignment that may be diminished in under-aligned long-context scenarios. Additionally, LongPO incorporates a short-to-long KL constraint to mitigate short-context performance decline during long-context alignment. When applied to Mistral-7B-Instruct-v0.2 from 128K to 512K context lengths, LongPO fully retains short-context performance and largely outperforms naive SFT and DPO in both long- and short-context tasks. Specifically, LongPO-trained models can achieve results on long-context benchmarks comparable to, or even surpassing, those of superior LLMs (e.g., GPT-4-128K) that involve extensive long-context annotation and larger parameter scales. Our code is available at https://github.com/DAMO-NLP-SG/LongPO.

## item_id: m_2445

TITLE: CLOOB: Modern Hopfield Networks with InfoLOOB Outperform CLIP

ABSTRACT: Contrastive learning with the InfoNCE objective is exceptionally successful in various self-supervised learning tasks. Recently, the CLIP model yielded impressive results on zero-shot transfer learning when using InfoNCE for learning visual representations from natural language supervision. However, InfoNCE as a lower bound on the mutual information has been shown to perform poorly for high mutual information. In contrast, the InfoLOOB upper bound (leave one out bound) works well for high mutual information but suffers from large variance and instabilities. We introduce "Contrastive Leave One Out Boost" (CLOOB), where modern Hopfield networks boost learning with the InfoLOOB objective. Modern Hopfield networks replace the original embeddings by retrieved embeddings in the InfoLOOB objective. The retrieved embeddings give InfoLOOB two assets. Firstly, the retrieved embeddings stabilize InfoLOOB, since they are less noisy and more similar to one another than the original embeddings. Secondly, they are enriched by correlations, since the covariance structure of embeddings is reinforced through retrievals. We compare CLOOB to CLIP after learning on the Conceptual Captions and the YFCC dataset with respect to their zero-shot transfer learning performance on other datasets. CLOOB consistently outperforms CLIP at zero-shot transfer learning across all considered architectures and datasets.

## item_id: m_2446

TITLE: Tartan: Accelerating Fully-Connected and Convolutional Layers in Deep Learning Networks by Exploiting Numerical Precision Variability

ABSTRACT: Tartan {TRT} a hardware accelerator for inference with Deep Neural Networks (DNNs) is presented and evaluated on Convolutional Neural Networks. TRT exploits the variable per layer precision requirements of DNNs to deliver execution time that is proportional to the precision p in bits used per layer for convolutional and fully-connected layers. Prior art has demonstrated an accelerator with the same execution performance only for convolutional layers. Experiments on image classification CNNs show that on average across all networks studied,  TRT outperforms a state-of-the-art bit-parallel accelerator by 1.90x without any loss in accuracy while it is 1.17x more energy efficient. TRT requires no network retraining while it enables trading off accuracy for additional improvements in execution performance and energy efficiency. For example, if a 1% relative loss in accuracy is acceptable, TRT is on average 2.04x faster and 1.25x more energy efficient than the bit-parallel accelerator.
This revision includes post-layout results and a better configuration that processes 2bits at time resulting in better efficiency and lower area overhead.

## item_id: m_2447

TITLE: Deep Asymmetric Multi-task Feature Learning

ABSTRACT: We propose Deep Asymmetric Multitask Feature Learning (Deep-AMTFL) which can learn deep representations shared across multiple tasks while effectively preventing negative transfer that may happen in the feature sharing process. Specifically, we introduce an asymmetric autoencoder term that allows reliable predictors for the easy tasks to have high contribution to the feature learning while suppressing the influences of unreliable predictors for more difficult tasks. This allows the learning of less noisy representations, and enables unreliable predictors to exploit knowledge from the reliable predictors via the shared latent features. Such asymmetric knowledge transfer through shared features is also more scalable and efficient than inter-task asymmetric transfer. We validate our Deep-AMTFL model on multiple benchmark datasets for multitask learning and image classification, on which it significantly outperforms existing symmetric and asymmetric multitask learning models, by effectively preventing negative transfer in deep feature learning.

## item_id: m_2448

TITLE: Learnable Behavior Control: Breaking Atari Human World Records via Sample-Efficient Behavior Selection

ABSTRACT: The exploration problem is one of the main challenges in deep reinforcement learning (RL). Recent promising works tried to handle the problem with population-based methods, which collect samples with diverse behaviors derived from a population of different exploratory policies. Adaptive policy selection has been adopted for behavior control. However, the behavior selection space is largely limited by the predefined policy population, which further limits behavior diversity.  In this paper, we propose a general framework called Learnable Behavioral Control (LBC) to address the limitation, which a) enables a significantly enlarged behavior selection space via formulating a hybrid behavior mapping from all policies; b) constructs a unified learnable process for behavior selection. We introduce LBC into distributed off-policy actor-critic methods and achieve behavior control via optimizing the selection of the behavior mappings with bandit-based meta-controllers. Our agents have achieved 10077.52% mean human normalized score and surpassed 24 human world records within 1B training frames in the Arcade Learning Environment, which demonstrates our significant state-of-the-art (SOTA) performance without degrading the sample efficiency.

## item_id: m_2449

TITLE: Improved Uncertainty Post-Calibration via Rank Preserving Transforms

ABSTRACT: Modern machine learning models with high accuracy often exhibit poor uncertainty calibration: the output probabilities of the model do not reflect its accuracy, and tend to be over-confident. Existing post-calibration methods such as temperature scaling recalibrate a trained model using rather simple calibrators with one or few parameters, which can have a rather limited capacity. In this paper, we propose Neural Rank Preserving Transforms (NRPT), a new post-calibration method that adjusts the output probabilities of a trained classifier using a calibrator of higher capacity, while maintaining its prediction accuracy. NRPT learns a calibrator that preserves the rank of the probabilities through general monotonic transforms, individualizes to the original input, and allows learning with any loss function that encourages calibration. We show experimentally that NRPT improves the expected calibration error (ECE) significantly over existing post-calibration methods such as (local) temperature scaling on large-scale image and text classification tasks. The performance of NRPT can further match ensemble methods such as deep ensembles, while being much more parameter-efficient. We further demonstrate the improved calibration ability of NRPT beyond the ECE metric, such as accuracy among top-confidence predictions, as well as optimizing the tradeoff between calibration and sharpness.

## item_id: m_2450

TITLE: Backdoor Secrets Unveiled: Identifying Backdoor Data with Optimized Scaled Prediction Consistency

ABSTRACT: Modern machine learning (ML) systems demand substantial training data, often resorting to external sources. Nevertheless, this practice renders them vulnerable to backdoor poisoning attacks. Prior backdoor defense strategies have primarily focused on the identification of backdoored models or poisoned data characteristics, typically operating under the assumption of access to clean data. In this work, we delve into a relatively underexplored challenge: the automatic identification of backdoor data within a poisoned dataset, all under realistic conditions, *i.e.*,  without the need for additional clean data or without manually defining a threshold for backdoor detection. We draw an inspiration from the scaled prediction consistency (SPC) technique, which exploits the prediction invariance of poisoned data to an input scaling factor. Based on this, we pose the backdoor data identification problem as a hierarchical data splitting optimization problem, leveraging a novel SPC-based loss function as the primary optimization objective. Our innovation unfolds in several key aspects. First, we revisit the vanilla SPC method, unveiling its limitations in addressing the proposed backdoor identification problem. Subsequently, we develop a bi-level optimization-based approach to precisely identify backdoor data by minimizing the advanced SPC loss. Finally, we demonstrate the efficacy of our proposal against a spectrum of backdoor attacks, encompassing basic label-corrupted attacks as well as more sophisticated clean-label attacks, evaluated across various benchmark datasets. Experiment results show that our approach often surpasses the performance of current baselines in identifying backdoor data points, resulting in about 4\%-36\% improvement in average AUROC. Codes are available at https://github.com/OPTML-Group/BackdoorMSPC.

## item_id: m_2451

TITLE: Localized Persistent Homologies for more Effective Deep Learning

ABSTRACT: Persistent Homologies have been successfully used to increase the performance of deep networks trained to detect curvilinear structures and to improve the topological quality of the results. However, existing methods are very global and ignore the location of topological features. In this paper, we introduce an approach that relies on a new filtration function to account for location during network training. We demonstrate experimentally on 2D images of roads and 3D image stacks of neural processes that networks trained in this manner are better at recovering the topology of the curvilinear structures they extract.

## item_id: m_2452

TITLE: Estimating Riemannian Metric with Noise-Contaminated Intrinsic Distance

ABSTRACT: We extend metric learning by studying the Riemannian manifold structure of the underlying data space induced by dissimilarity measures between data points. The key quantity of interest here is the Riemannian metric, which characterizes the Riemannian geometry and defines straight lines and derivatives on the manifold. Being able to estimate the Riemannian metric allows us to gain insights into the underlying manifold and compute geometric features such as the geodesic curves. We model the observed dissimilarity measures as noisy responses generated from a function of the intrinsic geodesic distance between data points. A new local regression approach is proposed to learn the Riemannian metric tensor and its derivatives based on a Taylor expansion for the squared geodesic distances. Our framework is general and accommodates different types of responses, whether they are continuous, binary, or comparative, extending the existing works which consider a single type of response at a time. We develop theoretical foundation for our method by deriving the rates of convergence for the asymptotic bias and variance of the estimated metric tensor. The proposed method is shown to be versatile in simulation studies and a real data application involving taxi trip time in New York City.

## item_id: m_2453

TITLE: Multi-Agent Cooperation and the Emergence of (Natural) Language

ABSTRACT: The current mainstream approach to train natural language systems is to expose them to large amounts of text. This passive learning is problematic if we are in- terested in developing interactive machines, such as conversational agents. We propose a framework for language learning that relies on multi-agent communi- cation. We study this learning in the context of referential games. In these games, a sender and a receiver see a pair of images. The sender is told one of them is the target and is allowed to send a message to the receiver, while the receiver must rely on it to identify the target. Thus, the agents develop their own language interactively out of the need to communicate. We show that two networks with simple configurations are able to learn to coordinate in the referential game. We further explore whether the “word meanings” induced in the game reflect intuitive semantic properties of the objects depicted in the image, and we present a simple strategy for grounding the agents’ code into natural language, a necessary step in developing machines that should eventually be able to communicate with humans.


## item_id: m_2454

TITLE: Fixup Initialization: Residual Learning Without Normalization

ABSTRACT: Normalization layers are a staple in state-of-the-art deep neural network architectures. They are widely believed to stabilize training, enable higher learning rate, accelerate convergence and improve generalization, though the reason for their effectiveness is still an active research topic. In this work, we challenge the commonly-held beliefs by showing that none of the perceived benefits is unique to normalization. Specifically, we propose fixed-update initialization (Fixup), an initialization motivated by solving the exploding and vanishing gradient problem at the beginning of training via properly rescaling a standard initialization. We find training residual networks with Fixup to be as stable as training with normalization -- even for networks with 10,000 layers. Furthermore, with proper regularization, Fixup enables residual networks without normalization to achieve state-of-the-art performance in image classification and machine translation.

## item_id: m_2455

TITLE: Protecting DNN from Evasion Attacks using Ensemble of High Focal Diversity

ABSTRACT: Edge AI continues to attract emerging applications that deploy well-trained DNN models on heterogeneous edge clients for real-time object detection. Recent studies have shown that evasion attacks on DNN object detection models at the test time are on the rise. Such evasion attacks generate deceptive queries using maliciously manipulated or out-of-distribution data, aiming to mislead high-quality object detectors during edge inference. This paper introduces ODEN, a novel approach to object detection ensemble, which combines a detection inconsistency solver with focal diversity-optimized ensemble pruning to defend against evasion attacks. The focal diversity ranking techniques enable ODEN to compose an ensemble from a pool of base object detectors with high failure independence, which strengthens the generalization performance of the ODEN ensemble in the presence of irregular query data and evasion attacks.  The ODEN inconsistency solver can detect and resolve three types of inconsistency by combining detection results from multiple DNN object detectors: the inconsistency of the object existence, the size and location inconsistency of the bounding boxes of detected objects, and the classification inconsistency of detected objects and their confidence. Extensive experiments on three benchmark vision datasets (OpenImages, COCO, and VOC) show that under no attack, ODEN can outperform existing ensemble methods by up to 9.33% of mAP. Compared to the low mAP of 2.64~18.07% under four evasion attacks, ODEN can maintain a high mAP of 58.97~86.00%, achieving up to an 82.44% increase in AI safety.

## item_id: m_2456

TITLE: OBSERVATIONAL DATA ONLY: Inferring Protein Signaling Pathways with Local Information- Rewarded Generative Flow Networks

ABSTRACT: Recovering causal influences in protein signaling networks on the basis of observational rather than interventional data is a key problem in systems biology.
Two established approaches for inferring protein signaling pathways are scoring based methods and constraint based methods. We observe that both approaches lacks learning ingredient and one could complement the other. Therefore, we consider integrating current advances in generative modeling of bayesian structures with a specialized designed information theory-based reward derived from constraints during network generation to combine the best of two approaches. Particularly the reward design considers both two-point and three-point mutual information scores corrected with complexity penalties. The signs and magnitudes of these quantities allow us to penalize or reward Bayesian networks as they are being built edge by edge by the GFlowNet sampler. This allows the search process to quickly focus on structures that are in agreement with mutual information signatures observed in the experimental data. Using this approach leads to better predictions compared to the standard practice of using Bayesian scores, which were previously explored with both GFlowNet and Monte Carlo sampling. Thus, our contribution amounts to a novel scheme for penalizing Bayesian networks that are inconsistent with the data early on in the sampling process based on constraints and integrates it with scoring based methods through generative modeling.

## item_id: m_2457

TITLE: FDNet: Focal Decomposed Network for Efficient, Robust and Practical time series forecasting

ABSTRACT: This paper presents FDNet: a Focal Decomposed Network for efficient, robust and practical time series forecasting. We break away from conventional deep time series forecasting formulas which obtain prediction results from universal feature maps of input sequences. In contrary, FDNet neglects universal correlations of input elements and only extracts fine-grained local features from input sequence. We show that: (1) Deep time series forecasting with only fine-grained local feature maps of input sequence is feasible and competitive upon theoretical basis. (2) By abandoning global coarse-grained feature maps, FDNet overcomes distribution shift problem caused by changing local dynamics of time series which is common in real-world applications. (3) FDNet is not dependent on any assumption or priori knowledge of time series except basic auto-regression, which makes it general and practical. Moreover, we propose focal input sequence decomposition method which decomposes input sequence in a focal manner for efficient and robust forecasting when facing LSTI problem. FDNet achieves promising forecasting performances on five benchmark datasets and reduces prediction MSE by 38.4% on average compared with other seven SOTA forecasting baselines.

## item_id: m_2458

TITLE: On the loss landscape of a class of deep neural networks with no bad local valleys

ABSTRACT: We identify a class of over-parameterized deep neural networks with standard activation functions and cross-entropy loss which provably have no bad local valley, in the sense that from any point in parameter space there exists a continuous path on which the cross-entropy loss is non-increasing and gets arbitrarily close to zero. This implies that these networks have no sub-optimal strict local minima.

## item_id: m_2459

TITLE: Binary Paragraph Vectors

ABSTRACT: Recently Le & Mikolov described two log-linear models, called Paragraph Vector, that can be used to learn state-of-the-art distributed representations of documents. Inspired by this work, we present Binary Paragraph Vector models: simple neural networks that learn short binary codes for fast information retrieval. We show that binary paragraph vectors outperform autoencoder-based binary codes, despite using fewer bits. We also evaluate their precision in transfer learning settings, where binary codes are inferred for documents unrelated to the training corpus. Results from these experiments indicate that binary paragraph vectors can capture semantics relevant for various domain-specific documents. Finally, we present a model that simultaneously learns short binary codes and longer, real-valued representations. This model can be used to rapidly retrieve a short list of highly relevant documents from a large document collection.

## item_id: m_2460

TITLE: ChunkAttention: Efficient Attention on KV Cache with Chunking Sharing and Batching

ABSTRACT: Self-attention is an essential component of GPT-style models and a significant cause of LLM inference latency for long sequences. In multi-tenant LLM inference servers, the compute and memory operation cost of self-attention can be amortized by making use of the probability that sequences from users may share long prompt prefixes. This paper introduces ChunkAttention, a unique self-attention kernel built on chunking, sharing the KV cache, and batching the attention computation. ChunkAttention recognizes matching prompt prefixes across several sequences and shares their KV cache in memory by chunking the KV cache and structuring it into the auxiliary prefix tree. To significantly improve the memory reuse of KV cache and consequently the speed of self-attention for long shared prompts, we design an efficient computation kernel on this new storage structure, where two-phased partitioning is implemented to reduce memory operations on shared KV cache during self-attention. Experiments show that ChunkAttention can speed up self-attention of long shared prompts 1.6-3 times, with lengths ranging from 1024 to 8192.

## item_id: m_2461

TITLE: Generative predecessor models for sample-efficient imitation learning

ABSTRACT: We propose Generative Predecessor Models for Imitation Learning (GPRIL), a novel imitation learning algorithm that matches the state-action distribution to the distribution observed in expert demonstrations, using generative models to reason probabilistically about alternative histories of demonstrated states. We show that this approach allows an agent to learn robust policies using only a small number of expert demonstrations and self-supervised interactions with the environment. We derive this approach from first principles and compare it empirically to a state-of-the-art imitation learning method, showing that it outperforms or matches its performance on two simulated robot manipulation tasks and demonstrate significantly higher sample efficiency by applying the algorithm on a real robot.

## item_id: m_2462

TITLE: Translate Policy to Language: Flow Matching Generated Rewards for LLM Explanations

ABSTRACT: As humans increasingly share environments with diverse agents powered by RL, LLMs, and beyond, the ability to explain agent policies in natural language is vital for reliable coexistence. We introduce a general-purpose framework that trains explanation-generating LLMs via reinforcement learning from AI feedback, with distributional rewards generated by generative continuous normalizing flows (CNFs). CNFs capture the pluralistic and probabilistic nature of human judgments about explanations. Moreover, under mild assumptions, CNFs provably bound deviations from true human reward distributions when trained on noisy proxy rewards from LLMs. We design a specialized CNF architecture that selectively attends to linguistic cues in decision context and explanations when generating rewards. Human and LLM evaluators find that our method delivers explanations that enable more accurate predictions of true agent decisions, exhibit greater logical soundness and actionability, and impose lower cognitive load than explanations trained with proxy LLM rewards or state-of-the-art RLHF and RLAIF baselines.

## item_id: m_2463

TITLE: Evading Adversarial Example Detection Defenses with Orthogonal Projected Gradient Descent

ABSTRACT: Evading adversarial example detection defenses requires finding adversarial examples that must simultaneously (a) be misclassified by the model and (b) be detected as non-adversarial. We find that existing attacks that attempt to satisfy multiple simultaneous constraints often over-optimize against one constraint at the cost of satisfying another. We introduce Selective Projected Gradient Descent and Orthogonal Projected Gradient Descent, improved attack techniques to generate adversarial examples that avoid this problem by orthogonalizing the gradients when running standard gradient-based attacks. We use our technique to evade four state-of-the-art detection defenses, reducing their accuracy to 0% while maintaining a 0% detection rate.

## item_id: m_2464

TITLE: DDI-Gaussian: Distributed Dynamic Instance Gaussian for Autonomous Driving

ABSTRACT: Current dynamic 3D Gaussian approaches attempt to decompose scene motion by using purely implicit features or additional 3D annotations. However, these strategies hinder fine-grained and interpretable control over Gaussians and overlook the inherent instance consistency, spatial continuity, and local rigidity in scene motion. To this end, we propose a novel framework that achieves MLP-free Gaussian instance distinction and effectively disentangles dynamic urban street scenes. Specifically, we assign each Gaussian a compact multi-hot instance feature, enabling direct differentiation without relying on an additional network. To model transient motions, we initialize sparse control points at the instance level and construct the motion field from coarse to fine by leveraging spatiotemporal relationships. Additionally, we introduce two instance-level losses: an instance-level region loss and an instance-semantic loss. The former, combined with the opacity rendering pipeline, enables precise instance-level rendering and suppresses ghosting artifacts. The latter enforces cross-view feature consistency and optimizes the spatial positions of instances. Notably, our framework avoids costly 3D instance annotations by instead utilizing 2D pseudo-labels generated by Segment Anything Model (SAM) for supervision. Our demo video and code are available in the anonymous repository at  https://anonymous.4open.science/r/DDI-GS-750E/.

## item_id: m_2465

TITLE: Brain2GAN; Reconstructing perceived faces from the primate brain via StyleGAN3

ABSTRACT: Neural coding characterizes the relationship between stimuli and their corresponding neural responses. The usage of synthesized yet photorealistic reality by generative adversarial networks (GANs) allows for superior control over these data: the underlying feature representations that account for the semantics in synthesized data are known a priori and their relationship is perfect rather than approximated post-hoc by feature extraction models. We exploit this property in neural decoding of multi-unit activity responses that we recorded from the primate brain upon presentation with synthesized face images in a passive fixation experiment. The face reconstructions we acquired from brain activity were astonishingly similar to the originally perceived face stimuli. This provides strong evidence that the neural face manifold and the disentangled w-latent space conditioned on StyleGAN3 (rather than the z-latent space of arbitrary GANs or other feature representations we encountered so far) share how they represent the high-level semantics of the high-dimensional space of faces.

## item_id: m_2466

TITLE: Transferrable End-to-End Learning for Protein Interface Prediction

ABSTRACT: While there has been an explosion in the number of experimentally determined, atomically detailed structures of proteins, how to represent these structures in a machine learning context remains an open research question.  In this work we demonstrate that representations learned from raw atomic coordinates can outperform hand-engineered structural features while displaying a much higher degree of transferrability.  To do so, we focus on a central problem in biology: predicting how proteins interact with one another—that is, which surfaces of one protein bind to which surfaces of another protein.  We present Siamese Atomic Surfacelet Network (SASNet), the first end-to-end learning method for protein interface prediction.  Despite using only spatial coordinates and identities of atoms as inputs, SASNet outperforms state-of-the-art methods that rely on hand-engineered, high-level features.  These results are particularly striking because we train the method entirely on a significantly biased data set that does not account for the fact that proteins deform when binding to one another.  Demonstrating the first successful application of transfer learning to atomic-level data, our network maintains high performance, without retraining, when tested on real cases in which proteins do deform.

## item_id: m_2467

TITLE: Neumann Optimizer: A Practical Optimization Algorithm for Deep Neural Networks

ABSTRACT: Progress in deep learning is slowed by the days or weeks it takes to train large models. The natural solution of using more hardware is limited by diminishing returns, and leads to inefficient use of additional resources. In this paper, we present a large batch, stochastic optimization algorithm that is both faster than widely used algorithms for fixed amounts of computation, and also scales up substantially better as more computational resources become available. Our algorithm implicitly computes the inverse Hessian of each mini-batch to produce descent directions; we do so without either an explicit approximation to the Hessian or Hessian-vector products. We demonstrate the effectiveness of our algorithm by successfully training large ImageNet models (InceptionV3, ResnetV1-50, ResnetV1-101 and InceptionResnetV2) with mini-batch sizes of up to 32000 with no loss in validation error relative to current baselines, and no increase in the total number of steps. At smaller mini-batch sizes, our optimizer improves the validation error in these models by 0.8-0.9\%. Alternatively, we can trade off this accuracy to reduce the number of training steps needed by roughly 10-30\%. Our work is practical and easily usable by others -- only one hyperparameter (learning rate) needs tuning, and furthermore, the algorithm is as computationally cheap as the commonly used Adam optimizer.

## item_id: m_2468

TITLE: Approximating Instance-Dependent Noise via Instance-Confidence Embedding

ABSTRACT: Label noise in multiclass classification is a major obstacle to the deployment of learning systems. However, unlike the widely used class-conditional noise (CCN) assumption that the noisy label is independent of the input feature given the true label, label noise in real-world datasets can be aleatory and heavily dependent on individual instances. In this work, we investigate the instance-dependent noise (IDN) model and propose an efficient approximation of IDN to capture the instance-specific label corruption. Concretely, noting the fact that most columns of the IDN transition matrix have only limited influence on the class-posterior estimation, we propose a variational approximation that uses a single-scalar confidence parameter. To cope with the situation where the mapping from the instance to its confidence value could vary significantly for two adjacent instances, we suggest using instance embedding that assigns a trainable parameter to each instance. The resulting instance-confidence embedding (ICE) method not only performs well under label noise but also can effectively detect ambiguous or mislabeled instances. We validate its utility on various image and text classification tasks.

## item_id: m_2469

TITLE: Group-Disentangling Conditional Shift

ABSTRACT: We propose a novel group disentanglement method called the Context-Aware Variational Autoencoder (CxVAE). Our model can learn disentangled representations on datasets with conditional shift. This phenomenon occurs when the conditional distribution of the instance-level latent variable $\mathbf{z}$ given the input observation $\mathbf{x}$ changes from one group to another (i.e. $p_i(\mathbf{z}|\mathbf{x}) \neq p_j(\mathbf{z}|\mathbf{x})$, where $i,j$ are two different groups). We show that existing methods fail to learn disentangled representations under this scenario because they infer the group $\mathbf{u}$ and instance $\mathbf{z}$ variables separately. CxVAE overcomes this limitation by conditioning the instance inference on the group variable $q(\mathbf{z}|\mathbf{x},\mathbf{u})$. Our model has the novel ability to disentangle ambiguous observations (those with incomplete information about the generative factors), which we evaluate on the task of fair comparisons between student test scores. Additionally, we demonstrate empirically that conditional shift is the cause of our model's improved performance.

## item_id: m_2470

TITLE: Maximum Entropy Flow Networks

ABSTRACT: Maximum entropy modeling is a flexible and popular framework for formulating statistical models given partial knowledge. In this paper, rather than the traditional method of optimizing over the continuous density directly, we learn a smooth and invertible transformation that maps a simple distribution to the desired maximum entropy distribution. Doing so is nontrivial in that the objective being maximized (entropy) is a function of the density itself.  By exploiting recent developments in normalizing flow networks, we cast the maximum entropy problem into a finite-dimensional constrained optimization, and solve the problem by combining stochastic optimization with the augmented Lagrangian method. Simulation results demonstrate the effectiveness of our method, and applications to finance and computer vision show the flexibility and accuracy of using maximum entropy flow networks.

## item_id: m_2471

TITLE: Enhancing Large Language Models in Coding Through Multi-Perspective Self-Consistency

ABSTRACT: Large language models (LLMs) have exhibited remarkable ability in textual generation. However, in complex reasoning tasks such as code generation, generating the correct answer in a single attempt remains a formidable challenge for LLMs. Previous research has explored solutions by aggregating multiple outputs, leveraging the consistency among them. However, none of them have comprehensively captured this consistency from different perspectives. 
In this paper, we propose the Multi-Perspective Self-Consistency (MPSC) framework, a novel decoding strategy for LLM that incorporates both inter-consistency across outputs from multiple perspectives and intra-consistency within a single perspective. Specifically, we ask LLMs to sample multiple diverse outputs from various perspectives for a given query and then construct a multipartite graph based on them. With two predefined measures of consistency, we embed both inter- and intra-consistency information into the graph. The optimal choice is then determined based on consistency analysis in the graph.
We conduct comprehensive evaluation on the code generation task by introducing solution, specification and test case as three perspectives. We leverage a code interpreter to quantitatively measure the inter-consistency and propose several intra-consistency measure functions. Our MPSC framework significantly boosts the performance on various popular benchmarks, including HumanEval (+17.60%), HumanEval Plus (+17.61%), MBPP (+6.50%) and CodeContests (+11.82%) in Pass$@1$, when compared to original outputs generated from ChatGPT, and even surpassing GPT-4.

## item_id: m_2472

TITLE: DeepOPF-GAF: Graph Self-Attention Framework for N-1 Security-Constrained Optimal Power Flow

ABSTRACT: N-1 Security-Constrained Optimal Power Flow (N-1 SCOPF) extends the conventional Optimal Power Flow (OPF) problem by ensuring secure and stable operation in all single-contingency scenarios. Solving OPF directly in large-scale power systems imposes a high computational burden, whereas compact approximation models, particularly multilayer perceptrons, have been introduced to improve efficiency. However, existing small-scale DNN-based models fail to meet the demands of highly dynamic grid topologies and multi-contingency solution requirements, due to their limited adaptability to topological changes and insufficient fitting capability. To bridge this gap, this paper proposes a graph self-attention-enhanced framework to optimize N-1 SCOPF solving. Specifically, a residual-based graph self-attention architecture is proposed to enable topological variation adaptation and scalable network expansion in depth and width. Furthermore, the Explained Variance Score (EVS) is introduced as a direct quantitative metric to evaluate the fitting performance of the proposed framework. Experimental results on the IEEE 9, 118, 300, and 2000-bus systems demonstrate that increasing the scale of the graph self-attention framework effectively enhances its fitting performance on N-1 SCOPF problems.

## item_id: m_2473

TITLE: From Vulnerability to Defense: Understanding and Mitigating MASK-Based Attacks in dLLMs

ABSTRACT: Diffusion large language models extend diffusion process to discrete domains such as text, demonstrating strong performance in many tasks. 
However, their bidirectional and parallel decoding architecture introduce unique safety risks that bypass existing safeguards. 
We show that dLLMs are highly vulnerable to **MASK**-based jailbreaks, where adversarial prompts exploit masked tokens to get fluent but unsafe completions. 
Through rigorous theoretical analysis and formal proofs, we identify margin accumulation and scheduling advantages as fundamental causes of this vulnerability. 
To address these risks, we introduce a two-stage data synthesis framework together with a Reject-MASK training strategy. 
Experimental results demonstrate that our approach consistently suppresses attack success rates from above 90\% to nearly single-digit levels, while retaining competitive utility across diverse benchmarks. 
By grounding defense design in rigorous theoretical analysis, our work not only establishes a principled foundation for the safety of diffusion-based large language models, but also provides a scalable and practical alignment framework that advances their secure deployment in real-world applications.

## item_id: m_2474

TITLE: Smoothing the Geometry of Probabilistic Box Embeddings

ABSTRACT: There is growing interest in geometrically-inspired embeddings for learning hierarchies, partial orders, and lattice structures, with natural applications to transitive relational data such as entailment graphs. Recent work has extended these ideas beyond deterministic hierarchies to probabilistically calibrated models, which enable learning from uncertain supervision and inferring soft-inclusions among concepts, while maintaining the geometric inductive bias of hierarchical embedding models. We build on the Box Lattice model of Vilnis et al. (2018), which showed promising results in modeling soft-inclusions through an overlapping hierarchy of sets, parameterized as high-dimensional hyperrectangles (boxes). However, the hard edges of the boxes present difficulties for standard gradient based optimization; that work employed a special surrogate function for the disjoint case, but we find this method to be fragile.  In this work, we present a novel hierarchical embedding model, inspired by a relaxation of box embeddings into parameterized density functions using Gaussian convolutions over the boxes. Our approach provides an alternative surrogate to the original lattice measure that improves the robustness of optimization in the disjoint case, while also preserving the desirable properties with respect to the original lattice. We demonstrate increased or matching performance on WordNet hypernymy prediction, Flickr caption entailment, and a MovieLens-based market basket dataset. We show especially marked improvements in the case of sparse data, where many conditional probabilities should be low, and thus boxes should be nearly disjoint.

## item_id: m_2475

TITLE: OptSHAP: Explaining Dimensionality Reduction-based Models for Tabular Data via Optimization

ABSTRACT: Dimensionality Reduction-based Models (DRbMs), which couple a dimensionality reduction technique with a predictive model, are commonly used to mitigate overfitting and reduce computational complexity regarding high-dimensional tabular data. However, their two-stage architecture presents considerable challenges for explainability, as the projection obscures the original feature space, thus making the model output difficult to interpret in terms of the input features. Model-agnostic explanation methods are applicable to DRbMs but typically rely on sampling-based approximations, leading to instability and low-faithfulness explanations. To address these limitations, we introduce OptSHAP, the first optimization-based attribution specifically designed for DRbMs. Our method leverages reduced-space attributions and then redistributes them back to the original feature space through a transformation that satisfies the principle of efficiency. Additionally, we propose a novel evaluation metric, the $k$-Local Stability Score (LSS), which quantifies the stability of feature attribution methods by averaging their distances to local explanations. Extensive empirical evaluations across high-dimensional datasets, various dimensionality reduction techniques, and multiple machine learning models demonstrate that OptSHAP outperforms state-of-the-art attribution methods, achieving up to $24\times$ stability and $2\times$ fidelity on key benchmarks.

## item_id: m_2476

TITLE: SGDEM: stochastic gradient descent with energy and momentum

ABSTRACT: In this paper, we propose SGDEM, Stochastic Gradient Descent with Energy and Momentum to solve a large class of general nonconvex stochastic optimization problems, based on the AEGD method that originated in the work [AEGD: Adaptive Gradient Descent with Energy. arXiv: 2010.05109]. SGDEM incorporates both energy and momentum at the same time so as to inherit their dual advantages. We show that SGDEM features an unconditional energy stability property, and derive energy-dependent convergence rates in the general nonconvex stochastic setting, as well as a regret bound in the online convex setting. A lower threshold for the energy variable is also provided. Our experimental results show that SGDEM converges faster than AEGD and generalizes better or at least as well as SGDM in training some deep neural networks.

## item_id: m_2477

TITLE: Gradient Estimators for Implicit Models

ABSTRACT: Implicit models, which allow for the generation of samples but not for point-wise evaluation of probabilities, are omnipresent in real-world problems tackled by machine learning and a hot topic of current research. Some examples include data simulators that are widely used in engineering and scientific research, generative adversarial networks (GANs) for image synthesis, and hot-off-the-press approximate inference techniques relying on implicit distributions. The majority of existing approaches to learning implicit models rely on approximating the intractable distribution or optimisation objective for gradient-based optimisation, which is liable to produce inaccurate updates and thus poor models. This paper alleviates the need for such approximations by proposing the \emph{Stein gradient estimator}, which directly estimates the score function of the implicitly defined distribution. The efficacy of the proposed estimator is empirically demonstrated by examples that include meta-learning for approximate inference and entropy regularised GANs that provide improved sample diversity.

## item_id: m_2478

TITLE: Hierarchical Memory Networks

ABSTRACT: Memory networks are neural networks with an explicit memory component that can be both read and written to by the network. The memory is often addressed in a soft way using a softmax function, making end-to-end training with backpropagation possible. However, this is not computationally scalable for applications which require the network to read from extremely large memories. On the other hand, it is well known that hard attention mechanisms based on reinforcement learning are challenging to train successfully. In this paper, we explore a form of hierarchical memory network, which can be considered as a hybrid between hard and soft attention memory networks. The memory is organized in a hierarchical structure such that reading from it is done with less computation than soft attention over a flat memory, while also being easier to train than hard attention over a flat memory. Specifically, we propose to incorporate Maximum Inner Product Search (MIPS) in the training and inference procedures for our hierarchical memory network. We explore the use of various state-of-the art approximate MIPS techniques and report results on SimpleQuestions, a challenging large scale factoid question answering task.


## item_id: m_2479

TITLE: SHAMANN: Shared Memory Augmented Neural Networks

ABSTRACT: Current state-of-the-art methods for semantic segmentation use deep neural networks to learn the segmentation mask from the input image signal as an image-to-image mapping. While these methods effectively exploit global image context, the learning and computational complexities are high. We propose shared memory augmented neural network actors as a dynamically scalable alternative. Based on a decomposition of the image into a sequence of local patches, we train such actors to sequentially segment each patch. To further increase the robustness and better capture shape priors, an external memory module is shared between different actors, providing an implicit mechanism for image information exchange. Finally, the patch-wise predictions are aggregated to a complete segmentation mask. We demonstrate the benefits of the new paradigm on a challenging lung segmentation problem based on chest X-Ray images, as well as on two synthetic tasks based on the MNIST dataset. On the X-Ray data, our method achieves state-of-the-art accuracy with a significantly reduced model size compared to reference methods. In addition, we reduce the number of failure cases by at least half.

## item_id: m_2480

TITLE: Deep Variational Canonical Correlation Analysis

ABSTRACT: We present deep variational canonical correlation analysis (VCCA), a deep multi-view learning model that extends the latent variable model interpretation of linear CCA~\citep{BachJordan05a} to nonlinear observation models parameterized by deep neural networks (DNNs). Computing the marginal data likelihood, as well as inference of the latent variables, are intractable under this model. We derive a variational lower bound of the data likelihood by parameterizing the posterior density of the latent variables with another DNN, and approximate the lower bound via Monte Carlo sampling. Interestingly, the resulting model resembles that of multi-view autoencoders~\citep{Ngiam_11b}, with the key distinction of an additional sampling procedure at the bottleneck layer. We also propose a variant of VCCA called VCCA-private which can, in addition to the ``common variables'' underlying both views, extract the ``private variables'' within each view. We demonstrate that VCCA-private is able to disentangle the shared and private information for multi-view data without hard supervision.

## item_id: m_2481

TITLE: Dataset Inference: Ownership Resolution in Machine Learning

ABSTRACT: With increasingly more data and computation involved in their training,  machine learning models constitute valuable intellectual property. This has spurred interest in model stealing, which is made more practical by advances in learning with partial, little, or no supervision. Existing defenses focus on inserting unique watermarks in a model's decision surface, but this is insufficient:  the watermarks are not sampled from the training distribution and thus are not always preserved during model stealing. In this paper, we make the key observation that knowledge contained in the stolen model's training set is what is common to all stolen copies. The adversary's goal, irrespective of the attack employed, is always to extract this knowledge or its by-products. This gives the original model's owner a strong advantage over the adversary: model owners have access to the original training data. We thus introduce $\textit{dataset inference}$, the process of identifying whether a suspected model copy has private knowledge from the original model's dataset, as a defense against model stealing. We develop an approach for dataset inference that combines statistical testing with the ability to estimate the distance of multiple data points to the decision boundary. Our experiments on CIFAR10, SVHN, CIFAR100 and ImageNet show that model owners can claim with confidence greater than 99% that their model (or dataset as a matter of fact) was stolen, despite only exposing 50 of the stolen model's training points. Dataset inference defends against state-of-the-art attacks even when the adversary is adaptive. Unlike prior work, it does not require retraining or overfitting the defended model.

## item_id: m_2482

TITLE: Breaking the Limits of Open-Weight CLIP: An Optimization Framework for Self-supervised Fine-tuning of CLIP

ABSTRACT: CLIP has become a cornerstone of multimodal representation learning, yet improving its performance typically requires a prohibitively costly process of training from scratch on billions of samples. We ask a different question: *Can we improve the performance of open-weight CLIP models across various downstream tasks using only existing self-supervised datasets?* Unlike supervised fine-tuning, which adapts a pretrained model to a single downstream task, our setting seeks to improve general performance across various tasks.  However, as both our experiments and prior studies reveal, simply applying standard training protocols starting from an open-weight CLIP model often fails, leading to performance degradation.  In this paper, we introduce **TuneCLIP**, a self-supervised fine-tuning framework that overcomes the performance degradation. TuneCLIP has two key components: (1) a warm-up stage of recovering optimization statistics to reduce cold-start bias, inspired by theoretical analysis, and (2) a fine-tuning stage of optimizing a new contrastive loss to mitigate the penalization on false negative pairs. Our extensive experiments show that TuneCLIP consistently improves performance across model architectures and scales. Notably, it elevates leading open-weight models like SigLIP (ViT-B/16), achieving gains of up to +2.5\% on ImageNet and related out-of-distribution benchmarks, and +1.2\% on the highly competitive DataComp benchmark, setting a new strong baseline for efficient post-pretraining adaptation.

## item_id: m_2483

TITLE: A PAC-Bayesian Approach to Spectrally-Normalized Margin Bounds for Neural Networks

ABSTRACT: We present a generalization bound for feedforward neural networks in terms of the product of the spectral norm of the layers and the Frobenius norm of the weights.  The generalization bound is derived using a PAC-Bayes analysis.

## item_id: m_2484

TITLE: CoLES: Contrastive learning for event sequences with self-supervision

ABSTRACT: We address the problem of self-supervised learning on discrete event sequences generated by real-world users. Self-supervised learning incorporates complex information from the raw data in low-dimensional fixed-length vector representations that could be easily applied in various downstream machine learning tasks. In this paper, we propose a new method CoLES, which adopts contrastive learning, previously used for audio and computer vision domains, to the discrete event sequences domain in a self-supervised setting. Unlike most previous studies, we theoretically justify under mild conditions that the augmentation method underlying CoLES provides representative samples of discrete event sequences. We evaluated CoLES on several public datasets and showed that CoLES representations consistently outperform other methods on different downstream tasks.


## item_id: m_2485

TITLE: Calibrating Energy-based Generative Adversarial Networks

ABSTRACT: In this paper, we propose to equip Generative Adversarial Networks with the ability to produce direct energy estimates for samples.
Specifically, we propose a flexible adversarial training framework, and prove this framework not only ensures the generator converges to the true data distribution, but also enables the discriminator to retain the density information at the global optimal.
We derive the analytic form of the induced solution, and analyze the properties.
In order to make the proposed framework trainable in practice, we introduce two effective approximation techniques.
Empirically, the experiment results closely match our theoretical analysis, verifying the discriminator is able to recover the energy of data distribution.

## item_id: m_2486

TITLE: Understanding and Preventing Capacity Loss in Reinforcement Learning

ABSTRACT: The reinforcement learning (RL) problem is rife with sources of non-stationarity that can destabilize or inhibit learning progress.
We identify a key mechanism by which this occurs in agents using neural networks as function approximators: \textit{capacity loss}, whereby networks trained to predict a sequence of target values lose their ability to quickly fit new functions over time.
We demonstrate that capacity loss occurs in a broad range of RL agents and environments, and is particularly damaging to learning progress in sparse-reward tasks. We then present a simple regularizer, Initial Feature Regularization (InFeR), that mitigates this phenomenon by regressing a subspace of features towards its value at initialization, improving performance over a state-of-the-art model-free algorithm in the Atari 2600 suite. Finally, we study how this regularization affects different notions of capacity and evaluate other mechanisms by which it may improve performance.

## item_id: m_2487

TITLE: Deep Learning with Sets and Point Clouds

ABSTRACT: We introduce a simple permutation equivariant layer for deep learning with set structure. This type of layer, obtained by parameter-sharing, has a simple implementation and linear-time complexity in the size of each set. We use deep permutation-invariant networks to perform point-could classification and MNIST digit summation, where in both cases the output is invariant to permutations of the input. In a semi-supervised setting, where the goal is make predictions for each instance within a set, we demonstrate the usefulness of this type of layer in set-outlier detection as well as semi-supervised learning with clustering side-information.

## item_id: m_2488

TITLE: Evo-NAS: Evolutionary-Neural Hybrid Agent for Architecture Search

ABSTRACT: Neural Architecture Search has shown potential to automate the design of neural networks. Deep Reinforcement Learning based agents can learn complex architectural patterns, as well as explore a vast and compositional search space. On the other hand, evolutionary algorithms offer higher sample efficiency, which is critical for such a resource intensive application. In order to capture the best of both worlds, we propose a class of Evolutionary-Neural hybrid agents (Evo-NAS). We show that the Evo-NAS agent outperforms both neural and evolutionary agents when applied to architecture search for a suite of text and image classification benchmarks. On a high-complexity architecture search space for image classification, the Evo-NAS agent surpasses the accuracy achieved by commonly used agents with only 1/3 of the search cost.

## item_id: m_2489

TITLE: Variational Intrinsic Control Revisited

ABSTRACT: In this paper, we revisit variational intrinsic control (VIC), an unsupervised reinforcement learning method for finding the largest set of intrinsic options available to an agent. In the original work by Gregor et al. (2016), two VIC algorithms were proposed: one that represents the options explicitly, and the other that does it implicitly. We show that the intrinsic reward used in the latter is subject to bias in stochastic environments, causing convergence to suboptimal solutions. To correct this behavior, we propose two methods respectively based on the transitional probability model and Gaussian Mixture Model. We substantiate our claims through rigorous mathematical derivations and experimental analyses. 

## item_id: m_2490

TITLE: Incremental Sequence Learning

ABSTRACT: Deep learning research over the past years has shown that by increasing the scope or difficulty of the learning problem over time, increasingly complex learning problems can be addressed. We study incremental learning in the context of sequence learning, using generative RNNs in the form of multi-layer recurrent Mixture Density Networks. While the potential of incremental or curriculum learning to enhance learning is known, indiscriminate application of the principle does not necessarily lead to improvement, and it is essential therefore to know which forms of incremental or curriculum learning have a positive effect. This research contributes to that aim by comparing three instantiations of incremental or curriculum learning.

We introduce Incremental Sequence Learning, a simple incremental approach to sequence learning. Incremental Sequence Learning starts out by using only the first few steps of each sequence as training data. Each time a performance criterion has been reached, the length of the parts of the sequences used for training is increased.

We introduce and make available a novel sequence learning task and data set: predicting and classifying MNIST pen stroke sequences. We find that Incremental Sequence Learning greatly speeds up sequence learning and reaches the best test performance level of regular sequence learning 20 times faster, reduces the test error by 74%, and in general performs more robustly; it displays lower variance and achieves sustained progress after all three comparison methods have stopped improving. The other instantiations of curriculum learning do not result in any noticeable improvement. A trained sequence prediction model is also used in transfer learning to the task of sequence classification, where it is found that transfer learning realizes improved classification performance compared to methods that learn to classify from scratch.


## item_id: m_2491

TITLE: Program Synthesis for Character Level Language Modeling

ABSTRACT: We propose a statistical model applicable to character level language modeling and show that it is a good fit for both, program source code and English text. The model is parameterized by a program from a domain-specific language (DSL) that allows expressing non-trivial data dependencies. Learning is done in two phases: (i) we synthesize a program from the DSL, essentially learning a good representation for the data, and (ii) we learn parameters from the training data - the process is done via counting, as in simple language models such as n-gram.

Our experiments show that the precision of our model is comparable to that of neural networks while sharing a number of advantages with n-gram models such as fast query time and the capability to quickly add and remove training data samples. Further, the model is parameterized by a program that can be manually inspected, understood and updated, addressing a major problem of neural networks.

## item_id: m_2492

TITLE: Semantic Hierarchy Emerges in the Deep Generative Representations for Scene Synthesis

ABSTRACT: Despite the success of Generative Adversarial Networks (GANs) in image synthesis, there lacks enough understanding on what networks have learned inside the deep generative representations and how photo-realistic images are able to be composed from random noises. In this work, we show that highly-structured semantic hierarchy emerges from the generative representations as the variation factors for synthesizing scenes. By probing the layer-wise representations with a broad set of visual concepts at different abstraction levels, we are able to quantify the causality between the activations and the semantics occurring in the output image. Such a quantification identifies the human-understandable variation factors learned by GANs to compose scenes. The qualitative and quantitative results suggest that the generative representations learned by GAN are specialized to synthesize different hierarchical semantics: the early layers tend to determine the spatial layout and configuration, the middle layers control the categorical objects, and the later layers finally render the scene attributes as well as color scheme. Identifying such a set of manipulatable latent semantics facilitates semantic scene manipulation.

## item_id: m_2493

TITLE: Scale-Aware Contrastive Reverse Distillation for Unsupervised Medical Anomaly Detection

ABSTRACT: Unsupervised anomaly detection using deep learning has garnered significant research attention due to its broad applicability, particularly in medical imaging where labeled anomalous data are scarce. While earlier approaches leverage generative models like autoencoders and generative adversarial networks (GANs), they often fall short due to overgeneralization. Recent methods explore various strategies, including memory banks, normalizing flows, self-supervised learning, and knowledge distillation, to enhance discrimination. Among these, knowledge distillation, particularly reverse distillation, has shown promise. Following this paradigm, we propose a novel scale-aware contrastive reverse distillation model that addresses two key limitations of existing reverse distillation methods: insufficient feature discriminability and inability to handle anomaly scale variations. Specifically, we introduce a contrastive student-teacher learning approach to derive more discriminative representations by generating and exploring out-of-normal distributions. Further, we design a scale adaptation mechanism to softly weight contrastive distillation losses at different scales to account for the scale variation issue. Extensive experiments on benchmark datasets demonstrate state-of-the-art performance, validating the efficacy of the proposed method. The code will be made publicly available.

## item_id: m_2494

TITLE: Pareto-Guided Regional Sampling for Adaptive Collocation in Physics-Informed Neural Networks

ABSTRACT: Physics-informed neural networks (PINNs) provide a powerful framework for solving both forward and inverse problems of differential equations by embedding physical constraints in the loss function. However, in regions that exhibit localized stiffness or sharp gradients, conventional PINN training using uniformly sampled collocation points often leads to suboptimal training efficiency and predictive accuracy. To address this challenge, this work proposes a Pareto-guided regional sampling (PaRS) framework for adaptive collocation point sampling and tuning. The proposed method integrates three key components: residual decomposition, adaptive loss weighting, and dynamic resampling. Specifically, the spatial domain of collocation points is first partitioned into multiple subregions, and the training objectives, such as residuals from different subregions, are treated as competing objectives. As a result, a Pareto front is constructed to capture trade-offs among competing residual and other losses. Subsequently, a novel Pareto-guided weighting method is developed to assign adaptive weights to each objective, informed by training progress and information across the Pareto front. These weights further guide the resampling of collocation points in each region, which increases the sampling density in underexplored or error-prone regions. The results of the experiment demonstrate that the proposed PaRS-PINN performs better than standard PINNs and state-of-the-art adaptive collocation point methods.

## item_id: m_2495

TITLE: Human-in-the-Loop Targeted Molecule Design Informed by Transcriptomes

ABSTRACT: Transcriptome-guided targeted molecule design contributes to the advancement of precision medicine. However, the fragmented and poorly integrated nature of existing datasets limits the ability of transcriptome-aware approaches to meet the design expectations of chemists, often requiring additional expert intervention after molecular generation. To address this gap, we propose HiTGen, a human-in-the-loop targeted molecule generation framework informed by transcriptomes. Specifically, HiTGen operates in two phases: i) Transcriptomes are served as the central biological driver and are fused with expert a posteriori knowledge via a tailored bidirectional attention mechanism, enabling biochemically grounded guidance for diffusion-based generation of molecule candidates. ii) An expert-guided human-in-the-loop optimization mechanism is employed by HiTGen to refine these candidates toward desired molecular targets. Extensive experiments demonstrate that HiTGen consistently outperforms state-of-the-art models across ten evaluation metrics, yielding chemist-aligned targeted molecules with potential for precision medicine. The code will be released upon acceptance of the paper.

## item_id: m_2496

TITLE: Enabling Binary Neural Network Training on the Edge

ABSTRACT: The ever-growing computational demands of increasingly complex machine learning models frequently necessitate the use of powerful cloud-based infrastructure for their training. Binary neural networks are known to be promising candidates for on-device inference due to their extreme compute and memory savings over higher-precision alternatives. In this paper, we demonstrate that they are also strongly robust to gradient quantization, thereby making the training of modern models on the edge a practical reality. We introduce a low-cost binary neural network training strategy exhibiting sizable memory footprint reductions and energy savings vs Courbariaux & Bengio's standard approach. Against the latter, we see coincident memory requirement and energy consumption drops of 2--6$\times$, while reaching similar test accuracy, across a range of small-scale models trained to classify popular datasets. We also showcase ImageNet training of ResNetE-18, achieving a 3.12$\times$ memory reduction over the aforementioned standard. Such savings will allow for unnecessary cloud offloading to be avoided, reducing latency and increasing energy efficiency while also safeguarding user privacy.

## item_id: m_2497

TITLE: Learning Out-of-distribution Detection without Out-of-distribution Data

ABSTRACT: Deep neural networks have attained remarkable performance when applied to data that comes from the same distribution as that of the training set, but can significantly degrade otherwise. Therefore, detecting whether an example is out-of-distribution (OOD) is crucial to enable a system that can reject such samples or alert users. Recent works have made significant progress on OOD benchmarks consisting of small image datasets. However, such methods rely on training or tuning with both in-distribution and out-of-distribution data. The latter is generally hard to define \textit{a-priori}, and its selection can easily bias the learning. In this work, we focus on the feasibility of learning OOD detection without OOD data, proposing two strategies for the problem. We specifically propose to decompose confidence scoring as well as a modified input pre-processing method. We show that both of these significantly help detection performance, all without tuning to any out-of-distribution data during training. Our further analysis on a larger scale image dataset shows that the two types of distribution shifts, specifically semantic shift and non-semantic shift, present a significant difference in the difficulty of the problem, providing an analysis of when the proposed strategies do or do not work.

## item_id: m_2498

TITLE: The Unbalanced Gromov Wasserstein Distance: Conic Formulation and Relaxation

ABSTRACT: Comparing metric measure spaces (i.e. a metric space endowed with a probability distribution) is at the heart of many machine learning problems. This includes for instance predicting properties of molecules in quantum chemistry or generating graphs with varying connectivity. The most popular distance between such metric measure spaces is the Gromov-Wasserstein (GW) distance, which is the solution of a quadratic assignment problem. This distance has been successfully applied to supervised learning and generative modeling, for applications as diverse as quantum chemistry or natural language processing. The GW distance is however limited to the comparison of metric measure spaces endowed with a probability distribution. This strong limitation is problematic for many applications in ML where there is no a priori natural normalization on the total mass of the data. Furthermore, imposing an exact conservation of mass across spaces is not robust to outliers and often leads to irregular matching. To alleviate these issues, we introduce two Unbalanced Gromov-Wasserstein formulations: a distance and a more tractable upper-bounding relaxation. They both allow the comparison of metric spaces equipped with arbitrary positive measures up to isometries. The first formulation is a positive and definite divergence based on a relaxation of the mass conservation constraint using a novel type of quadratically-homogeneous divergence.This divergence works hand in hand with the entropic regularization approach which is popular to solve large scale optimal transport problems. We show that the underlying non-convex optimization problem can be efficiently tackled using a highly parallelizable and GPU-friendly iterative scheme. The second formulation is a distance between mm-spaces up to isometries based on a conic lifting. Lastly, we provide numerical simulations to highlight the salient features of the unbalanced divergence and its potential applications in ML.

## item_id: m_2499

TITLE: Bolstering Stochastic Gradient Descent with Model Building

ABSTRACT: Stochastic gradient descent method and its variants constitute the core optimization algorithms that achieve good convergence rates for solving machine learning problems. These rates are obtained especially when these algorithms are fine-tuned for the application at hand. Although this tuning process can require large computational costs, recent work has shown that these costs can be reduced by line search methods that iteratively adjust the stepsize. We propose an alternative approach to stochastic line search by using a new algorithm based on forward step model building. This model building step incorporates a second-order information that allows adjusting not only the stepsize but also the search direction. Noting that deep learning model parameters come in groups (layers of tensors), our method builds its model and calculates a new step for each parameter group.  This novel diagonalization approach makes the selected step lengths adaptive. We provide convergence rate analysis, and experimentally show that the proposed algorithm achieves faster convergence and better generalization in most problems. Moreover, our experiments show that the proposed method is quite robust as it converges for a wide range of initial stepsizes.

## item_id: m_2500

TITLE: Topology-Aware Segmentation Using Discrete Morse Theory

ABSTRACT: In the segmentation of fine-scale structures from natural and biomedical images, per-pixel accuracy is not the only metric of concern. Topological correctness, such as vessel connectivity and membrane closure, is crucial for downstream analysis tasks. In this paper, we propose a new approach to train deep image segmentation networks for better topological accuracy. In particular, leveraging the power of discrete Morse theory (DMT), we identify global structures, including 1D skeletons and 2D patches, which are important for topological accuracy. Trained with a novel loss based on these global structures, the network performance is significantly improved especially near topologically challenging locations (such as weak spots of connections and membranes). On diverse datasets, our method achieves superior performance on both the DICE score and topological metrics.
