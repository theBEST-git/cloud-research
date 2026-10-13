# Batch 16 — 100 items

## item_id: m_1501

TITLE: Efficient Wasserstein Natural Gradients for Reinforcement Learning

ABSTRACT: A novel optimization approach is proposed for application to policy gradient methods and evolution strategies for reinforcement learning (RL). The procedure uses a computationally efficient \emph{Wasserstein natural gradient} (WNG) descent that takes advantage of the geometry induced by a Wasserstein penalty to speed optimization. This method follows the recent theme in RL of including divergence penalties in the objective to establish trust regions. Experiments on challenging tasks demonstrate improvements in both computational cost and performance over advanced baselines. 


## item_id: m_1502

TITLE: HiFiSinger: Towards High-Fidelity Neural Singing Voice Synthesis

ABSTRACT: High-fidelity singing voices usually require higher sampling rate (e.g., 48kHz, compared with 16kHz or 24kHz in speaking voices) with large range of frequency to convey rich expression and emotion. However, higher sampling rate results in wider frequency band and longer waveform sequence with more fine-grained details and presents challenges for singing modeling in both frequency and time domains in singing voice synthesis (SVS). In this paper, we develop HiFiSinger, an SVS system towards high-fidelity singing voice using 48kHz sampling rate. HiFiSinger consists of a FastSpeech based neural acoustic model and a Parallel WaveGAN based neural vocoder to ensure fast training and inference and also high voice quality. To tackle the difficulty of singing modeling caused by high sampling rate (wider frequency band and longer waveform), we introduce multi-scale adversarial training in both the acoustic model and vocoder to improve singing modeling. Specifically, 1) To handle the larger range of frequencies caused by higher sampling rate (e.g., 48kHz vs. 24kHz), we introduce a novel sub-frequency GAN (SF-GAN) on mel-spectrogram generation, which splits the full 80-dimensional mel-frequency into multiple sub-bands (e.g. low, middle and high frequency bands) and models each sub-band with a separate discriminator. 2) To model longer waveform sequences caused by higher sampling rate, we introduce a multi-length GAN (ML-GAN) for waveform generation to model different lengths of waveform sequences with separate discriminators. 3) We also introduce several additional designs in HiFiSinger that are crucial for high-fidelity voices, such as adding F0 (pitch) and V/UV (voiced/unvoiced flag) as acoustic features, choosing an appropriate window and hop size for mel-spectrogram, and increasing the receptive field in vocoder for long vowel modeling in singing voices. Experiment results show that HiFiSinger synthesizes high-fidelity singing voices with much higher quality: 0.32/0.44 MOS gain over 48kHz/24kHz baseline and 0.83 MOS gain over previous SVS systems. Audio samples are available at https://hifisinger.github.io.

## item_id: m_1503

TITLE: Transformation-based Models of Video Sequences

ABSTRACT: In this work we propose a simple unsupervised approach for next frame prediction in video. Instead of directly predicting the pixels in a frame given past frames, we predict the transformations needed for generating the next frame in a sequence, given the transformations of the past frames. This leads to sharper results, while using a smaller prediction model.

In order to enable a fair comparison between different video frame prediction models, we also propose a new evaluation protocol. We use generated frames as input to a classifier trained with ground truth sequences. This criterion guarantees that models scoring high are those producing sequences which preserve discrim- inative features, as opposed to merely penalizing any deviation, plausible or not, from the ground truth. Our proposed approach compares favourably against more sophisticated ones on the UCF-101 data set, while also being more efficient in terms of the number of parameters and computational cost.

## item_id: m_1504

TITLE: Improved Language Modeling by Decoding the Past

ABSTRACT: Highly regularized LSTMs achieve impressive results on several benchmark datasets in language modeling. We propose a new regularization method based on decoding the last token in the context using the predicted distribution of the next token. This biases the model towards retaining more contextual information, in turn improving its ability to predict the next token. With negligible overhead in the number of parameters and training time, our Past Decode Regularization (PDR) method achieves a word level perplexity of 55.6 on the Penn Treebank and 63.5 on the WikiText-2 datasets using a single softmax. We also show gains by using PDR in combination with a mixture-of-softmaxes, achieving a word level perplexity of 53.8 and 60.5 on these datasets. In addition, our method achieves 1.169 bits-per-character on the Penn Treebank Character dataset for character level language modeling. These results constitute a new state-of-the-art in their respective settings.

## item_id: m_1505

TITLE: Gumbel-Matrix Routing for Flexible Multi-task Learning

ABSTRACT: This paper proposes a novel per-task routing method for multi-task applications. Multi-task neural networks can learn to transfer knowledge across different tasks by using parameter sharing. However, sharing parameters between unrelated tasks can hurt performance. To address this issue, routing networks can be applied to learn to share each group of parameters with a different subset of tasks to better leverage tasks relatedness. However, this use of routing methods requires to address the challenge of learning the routing jointly with the parameters of a modular multi-task neural network. We propose the Gumbel-Matrix routing, a novel multi-task routing method based on the Gumbel-Softmax, that is designed to learn fine-grained parameter sharing. When applied to the Omniglot benchmark, the proposed method improves the state-of-the-art error rate by 17%.

## item_id: m_1506

TITLE: IN-RIL: Interleaved Reinforcement and Imitation Learning for Policy Fine-Tuning

ABSTRACT: Imitation learning (IL) and reinforcement learning (RL) offer complementary strengths for robot learning, and yet each has severe limitations when used in isolation. Recent studies have proposed hybrid approaches to integrate IL with RL, but still face major challenges such as over-regularization  and  poor sample efficiency. Thus motivated, we develop IN-RIL, \textbf{IN}terleaved \textbf{R}einforcement learning and \textbf{I}mitation \textbf{L}earning, for policy fine-tuning, which periodically injects IL updates after multiple RL updates. In essence, IN-RIL  leverages
`alternating optimization' to exploit the strengths of both IL and RL without overly constraining the policy learning, and hence can benefit from both the stability of IL and the expert-guided exploration of RL accordingly. Since IL and RL involve different optimization objectives, we devise gradient separation mechanisms to prevent their interference. Furthermore, our rigorous analysis sheds light on how interleaving IL with RL stabilizes learning and improves iteration efficiency. We conduct extensive experiments on Robomimic, FurnitureBench, and Gym, and demonstrate that IN-RIL as a general plug-in compatible with various state-of-the-art RL algorithms, can improve RL sample efficiency, and mitigate performance collapse.

## item_id: m_1507

TITLE: Decoupling Strategy and Surface Realization for Task-oriented Dialogues

ABSTRACT: Task-oriented dialogue systems assist users in completing various tasks by generating appropriate responses. The key lies in effective strategy learning and surface realization, which are largely mixed together by the cutting-edge methods. They thus face two problems: a) the learning of high-level strategy could easily be misled by the detailed word sequence optimization, and b) directly emphasizing the agent's goal through reinforcement learning (RL) also leads to corrupted solutions like ungrammatical or repetitive responses. In this work, we propose to decouple the strategy learning and surface realization in a general framework, called DSSR. The core is to construct a latent content space for strategy optimization and disentangle the surface style from it. Specifically, we optimize the latent content distribution for strategy towards task completion, and assume that such distribution is shared across different surface style realizations. By further constructing an encoder-decoder scheme for the surface part, it not only facilitates decoupled optimization via RL for both strategy and surface asynchronously, but also supports controllable surface style transfer of responses. We test DSSR on the multi-domain dialogue datasets MultiWoz 2.0 and MultiWoz 2.1 in comparison with methods mixing strategy and surface realization in different levels, showing improvements in the performance evaluated by various evaluation metrics. Finally, we demonstrate the semantic meanings of latent content distributions to show the disentangling effect of DSSR, and show that it can do effective surface style transfer as by-products.

## item_id: m_1508

TITLE: A Goal-oriented Neural Conversation Model by Self-Play

ABSTRACT: Building chatbots that can accomplish goals such as booking a flight ticket is an unsolved problem in natural language understanding. Much progress has been made to build conversation models using techniques such as sequence2sequence modeling. One challenge in applying such techniques to building goal-oriented conversation models is that maximum likelihood-based models are not optimized toward accomplishing goals. Recently, many methods have been proposed to address this issue by optimizing a reward that contains task status or outcome. However, adding the reward optimization on the fly usually provides little guidance for language construction and the conversation model soon becomes decoupled from the language model. In this paper, we propose a new setting in goal-oriented dialogue system to tighten the gap between these two aspects by enforcing model level information isolation on individual models between two agents. Language construction now becomes an important part in reward optimization since it is the only way information can be exchanged. We experimented our models using self-play and results showed that our method not only beat the baseline sequence2sequence model in rewards but can also generate human-readable meaningful conversations of comparable quality. 

## item_id: m_1509

TITLE: Spending Your Winning Lottery Better After Drawing It

ABSTRACT: Lottery Ticket Hypothesis (LTH) (Frankle & Carbin, 2019) suggest suggests that a dense neural network contains a sparse sub-network that can match the performance of the original dense network when trained in isolation from scratch. Most works retrain the sparse sub-network with the same training protocols as its dense network, such as initialization, architecture blocks, and training recipes. However, till now it is unclear that whether these training protocols are optimal for sparse networks. 
In this paper, we demonstrate that it is unnecessary for spare retraining to strictly inherit those properties from the dense network. Instead, by plugging in purposeful "tweaks" of the sparse subnetwork architecture or its training recipe, its retraining can be significantly improved than the default, especially at high sparsity levels. Combining all our proposed "tweaks" can yield the new state-of-the-art performance of LTH, and these modifications can be easily adapted to other sparse training algorithms in general. Specifically, we have achieved a significant and consistent performance gain of 1.05% - 4.93% for ResNet18 on CIFAR-100 over vanilla-LTH. Moreover, our methods are shown to generalize across datasets (CIFAR10, CIFAR100, TinyImageNet) and architectures (Vgg16, ResNet-18/ResNet-34, MobileNet). All codes will be publicly available.

## item_id: m_1510

TITLE: Memory Augmented Control Networks

ABSTRACT: Planning problems in partially observable environments cannot be solved directly with convolutional networks and require some form of memory. But, even memory networks with sophisticated addressing schemes are unable to learn intelligent reasoning satisfactorily due to the complexity of simultaneously learning to access memory and plan. To mitigate these challenges we propose the Memory Augmented Control Network (MACN). The network splits planning into a hierarchical process. At a lower level, it learns to plan in a locally observed space. At a higher level, it uses a collection of policies computed on locally observed spaces to learn an optimal plan in the global environment it is operating in. The performance of the network is evaluated on path planning tasks in environments in the presence of simple and complex obstacles and in addition, is tested for its ability to generalize to new environments not seen in the training set.

## item_id: m_1511

TITLE: From Inpainting to Editing: A Self-Bootstrapping Paradigm for Context-Rich Visual Dubbing

ABSTRACT: Audio-driven visual dubbing aims to synchronize a video's lip movements with new speech, but is fundamentally challenged by the lack of ideal training data: paired videos where only a subject's lip movements differ while all other visual conditions are identical. Existing methods circumvent this with a mask-based inpainting paradigm, where an incomplete visual conditioning (i.e., masked video frames and misaligned appearance references) forces models to simultaneously hallucinate missing content and sync lips, leading to visual artifacts, identity drift, and poor synchronization. In this work, we propose a novel self-bootstrapping framework that reframes visual dubbing from an ill-posed inpainting task into a well-conditioned video-to-video editing problem. Our approach employs a Diffusion Transformer (DiT), first as a data _generator_, to synthesize ideal training data: a lip-altered companion video for each real sample, forming visually aligned video pairs. A DiT-based audio-driven _editor_ is then trained on these pairs end-to-end, leveraging the complete and aligned input video frames to focus solely on precise, audio-driven lip modifications. This complete, frame-aligned input conditioning forms a rich _``visual context"_ for the editor, providing it with complete identity cues, scene interactions (e.g., lighting and occlusions), and continuous spatiotemporal dynamics. Leveraging this rich context fundamentally enables our method to achieve highly accurate lip sync, faithful identity preservation, and exceptional robustness against challenging in-the-wild scenarios. We further introduce a timestep-adaptive multi-phase learning strategy as a necessary component to disentangle conflicting editing objectives across diffusion timesteps, thereby facilitating stable training and yielding enhanced lip synchronization and visual fidelity. Additionally, we propose ContextDubBench, a comprehensive benchmark dataset for robust evaluation in diverse and challenging practical application scenarios. Our visualizations are available at the anonymous page [x-dub-lab.github.io](https://x-dub-lab.github.io), and code will be released to benefit the community.

## item_id: m_1512

TITLE:  A Theoretical Framework for Robustness of (Deep) Classifiers against Adversarial Samples

ABSTRACT: Most machine learning classifiers, including deep neural networks, are vulnerable to adversarial examples. Such inputs are typically generated by adding small but purposeful modifications that lead to incorrect outputs while imperceptible to human eyes. The goal of this paper is not to introduce a single method, but to make theoretical steps toward fully understanding adversarial examples. By using concepts from topology, our theoretical analysis brings forth the key reasons why an adversarial example can fool a classifier ($f_1$) and adds its oracle ($f_2$, like human eyes) in such analysis. 
By investigating the topological relationship between two (pseudo)metric spaces corresponding to predictor $f_1$ and oracle $f_2$, we develop necessary and sufficient conditions that can determine if $f_1$ is always robust (strong-robust) against adversarial examples according to $f_2$. Interestingly our theorems indicate that just one unnecessary feature can make $f_1$ not strong-robust, and the right feature representation learning is the key to getting a classifier that is both accurate and strong robust.


## item_id: m_1513

TITLE: Reconstruction for disentanglement, Contrast for invariance

ABSTRACT:  Disentangled and invariant representation are two vital goals for representation learning and many approaches have been proposed to achieve one of them. However, those two goals are actually complementary to each other and we propose a framework to accomplish both of them together. We introduce weakly supervised signals to learn disentangled representation and use contrastive methods to enforce invariant representation. By experimenting on state-of-the-art datasets, the results show that our framework outperforms previous works on both tasks.





## item_id: m_1514

TITLE: The Variational Walkback Algorithm

ABSTRACT: A recognized obstacle to training undirected graphical models with latent variables such as Boltzmann machines is that the maximum likelihood training procedure requires sampling from Monte-Carlo Markov chains which may not mix well, in the inner loop of training, for each example.  We first propose the idea that it is sufficient to locally carve the energy function everywhere so that its gradient points in the "right" direction (i.e., towards generating the data). Following on previous work on contrastive divergence, denoising autoencoders, generative stochastic networks and unsupervised learning using non-equilibrium dynamics, we propose a variational bound on the marginal log-likelihood of the data which corresponds to a new learning procedure that first walks away from data points by following the model transition operator and then trains that operator to walk backwards for each of these steps, back towards the training example. The tightness of the variational bound relies on gradually increasing temperature as we walk away from the data, at each step providing a gradient on the parameters to maximize the probability that the transition operator returns to its previous state. Interestingly, this algorithm admits a variant where there is no explicit energy function, i.e., the parameters are used to directly define the transition operator. This also eliminates the explicit need for symmetric weights which previous Boltzmann machine or Hopfield net models require, and which makes these models less biologically plausible.

## item_id: m_1515

TITLE: Post-training for Deep Learning

ABSTRACT: One of the main challenges of deep learning methods is the choice of an appropriate training strategy. In particular, additional steps, such as unsupervised pre-training, have been shown to greatly improve the performances of deep structures. In this article, we propose an extra training step, called post-training, which only optimizes the last layer of the network. We show that this procedure can be analyzed in the context of kernel theory, with the first layers computing an embedding of the data and the last layer a statistical model to solve the task based on this embedding. This step makes sure that the embedding, or representation, of the data is used in the best possible way for the considered task. This idea is then tested on multiple architectures with various data sets, showing that it consistently provides a boost in performance.

## item_id: m_1516

TITLE: Online Adversarial Purification based on Self-supervised Learning

ABSTRACT: Deep neural networks are known to be vulnerable to adversarial examples, where a perturbation in the input space leads to an amplified shift in the latent network representation. In this paper, we combine canonical supervised learning with self-supervised representation learning, and present Self-supervised Online Adversarial Purification (SOAP), a novel defense strategy that uses a self-supervised loss to purify adversarial examples at test-time. Our approach leverages the label-independent nature of self-supervised signals and counters the adversarial perturbation with respect to the self-supervised tasks. SOAP yields competitive robust accuracy against state-of-the-art adversarial training and purification methods, with considerably less training complexity. In addition, our approach is robust even when adversaries are given the knowledge of the purification defense strategy. To the best of our knowledge, our paper is the first that generalizes the idea of using self-supervised signals to perform online test-time purification.

## item_id: m_1517

TITLE: Quadrature-based features for kernel approximation

ABSTRACT: We consider the problem of improving kernel approximation via feature maps. These maps arise as Monte Carlo approximation to integral representations of kernel functions and scale up kernel methods for larger datasets. We propose to use more efficient numerical integration technique to obtain better estimates of the integrals compared to the state-of-the-art methods. Our approach allows to use information about the integrand to enhance approximation and facilitates fast computations. We derive the convergence behavior and conduct an extensive empirical study that supports our hypothesis.

## item_id: m_1518

TITLE: SCI-Verifier: Scientific Verifier with Thinking

ABSTRACT: As large language models (LLMs) are increasingly applied to scientific reasoning, the complexity of answer formats and the diversity of equivalent expressions make answer verification a critical yet challenging task. Existing verification studies in scientific domains suffer from two major limitations: (a) the absence of systematic evaluation standards and insufficient disciplinary coverage, which hinders their comprehensive assessment; and (b) heavy reliance on cumbersome rule design or prompt engineering, which reduces their effectiveness in complex reasoning scenarios or limits their cross-disciplinary generalization. To address these challenges, we propose solutions at both the data and model levels. On the data side, we construct **SCI-VerifyBench**, a cross-disciplinary benchmark covering mathematics, physics, biology, chemistry, and general scientific QA. The benchmark is built from real LLM responses and enhanced with domain-specific equivalence transformations that generate challenging and realistic data. Model-based and expert annotations ensure both quality and diversity, enabling rigorous evaluation of verification ability. On the model side, we emphasize the importance of reasoning for verification and introduce **SCI-Verifier**, a unified reasoning-augmented verifier for scientific domains. Through post-training, SCI-Verifier demonstrates strong logical reasoning and equivalence judgment capabilities while maintaining concise and stable outputs. Together, SCI-VerifyBench and SCI-Verifier provide a principled framework for scientific verification, offering both systematic evaluation and practical pathways to enhance the reliability and applicability of LLMs in scientific domains.

## item_id: m_1519

TITLE: Shell Games: Control Protocols for Adversarial AI Agents

ABSTRACT: As more powerful AI agents are deployed with greater tool use and autonomy, it will become increasingly important to ensure they cannot take severely damaging actions. Recent work introduced "control evaluations," which study whether monitoring and security protocols intended to prevent dangerous actions are robust to intentional subversion by these AIs. In a control evaluation, a *red team* seeks to subvert the safety protocols built by the *blue team*. The blue team has access to a weaker *trusted* model and a limited amount of high-quality, trusted labor to attempt to safely extract work from a stronger *untrusted* model. Prior work conducted a control evaluation using competition programming problems with the red team objective of writing subtly incorrect (or "backdoored") solutions (Greenblatt et al. 2023). We extend this work by performing a control evaluation in a more realistic setting in which an untrusted LLM agent executes commands in a bash shell. The blue team seeks to use that agent to complete our novel dataset of 200 challenging multi-step tasks, each of which requires the agent to iteratively develop a bash script that passes test cases. The red team creates an attack policy that uses the untrusted model to covertly download and execute a dummy malware file while completing tasks without getting caught by the blue team's safety protocols. This agentic setting allows both teams to explore complex new strategies that have not been previously studied. We extend protocols from previous work to this agentic setting, propose novel protocols, and evaluate each on our safety and usefulness metrics. We find that our protocols substantially improve the Pareto frontier of usefulness and safety relative to simple baselines: one of our best protocols exhibits approximately a 2.5 times improvement in safety metrics with no statistically significant decrease in usefulness compared to our trusted monitoring baseline.

## item_id: m_1520

TITLE: Online Budget-Aware Guidance for Blockwise Discrete Text Diffusion

ABSTRACT: Diffusion language models (DLMs) are emerging as strong alternatives to autoregressive decoders, combining iterative refinement, global context access, and natural controllability. Yet controllable text diffusion remains underexplored: unlike vision, where plug-and-play guidance is central, existing methods for text rely on fixed or decaying step-size schedules that are brittle across prompts, constraints, and remasking strategies. The problem is amplified in modern blockwise DLMs, where gradient volatility and coverage fluctuate across spans, making schedule-based heuristics unstable. 
We present BALE(Budget-Aware Logit Editing), a plug-and-play controller that replaces heuristic schedules with an online, budget-aware rule. At each step, BALE fuses multi-constraint gradients and selects guidance strength by balancing a residual-targeted movement rule, stability caps based on an EMA Lipschitz proxy and a KL surrogate. Beyond per-step control, BALE allocates a fixed sequence-level budget across blocks and reallocates dynamically at boundaries. A discrete-time KL bound and a continuous-time SDE view explain why BALE stabilizes blockwise decoding. 
On LLaDa-8B, BALE improves lexical (must-have, forbidden), semantic (sentiment, formality), and combined controls over prompt tuning and schedule-based baselines, yielding higher satisfaction rates at matched or lower perplexity and stronger human/LLM preference. BALE is lightweight, scheduler-free, and advances controllable text diffusion toward practical deployment.

## item_id: m_1521

TITLE: Learning from Integral Losses in Physics Informed Neural Networks

ABSTRACT: This work proposes a solution for the problem of training physics-informed networks under partial integro-differential equations. These equations require an infinite or a large number of neural evaluations to construct a single residual for training.  As a result, accurate evaluation may be impractical, and we show that naive approximations at replacing these integrals with unbiased estimates lead to biased loss functions and solutions. To overcome this bias, we investigate three types of potential solutions: the deterministic sampling approach, the double-sampling trick, and the delayed target method. We consider three classes of PDEs for benchmarking; one defining Poisson problems with singular charges and weak solutions of up to 10 dimensions, another involving weak solutions on electro-magnetic fields and a Maxwell equation, and a third one defining a Smoluchowski coagulation problem. Our numerical results confirm the existence of the aforementioned bias in practice, and also show that our proposed delayed target approach can lead to accurate solutions with comparable quality to ones estimated with a large number of samples. Our implementation is open-source and available at https://anonymous.4open.science/r/btspinn.

## item_id: m_1522

TITLE: Sparse and Structured Visual Attention

ABSTRACT: Visual attention mechanisms have been widely used in image captioning models. In this paper, to better link the image structure with the generated text, we replace the traditional softmax attention mechanism by two alternative sparsity-promoting transformations: sparsemax and Total-Variation Sparse Attention (TVmax). With sparsemax, we obtain sparse attention weights, selecting relevant features.  In order to promote sparsity and encourage fusing of the related adjacent spatial locations, we propose TVmax.  By selecting relevant groups of features, the TVmax transformation improves interpretability. We present results in the Microsoft COCO and Flickr30k datasets, obtaining gains in comparison to softmax.  TVmax outperforms the other compared attention mechanisms in terms of human-rated caption quality and attention relevance.

## item_id: m_1523

TITLE: FlexDrive: Toward Trajectory Flexibility in Driving Scene Reconstruction and Rendering

ABSTRACT: Driving scene reconstruction and rendering have advanced significantly using the 3D Gaussian Splatting. However, most prior research has focused on the rendering quality along a pre-recorded vehicle path and struggles to generalize to out-of-path viewpoints, which is caused by the lack of high-quality supervision in those out-of-path views.  To address this issue, we introduce an Inverse View Warping technique to create compact and high-quality images as supervision for the reconstruction of the out-of-path views, enabling high-quality rendering results for those views. For accurate and robust inverse view warping, a depth bootstrap strategy is proposed to obtain on-the-fly dense depth maps during the optimization process, overcoming the sparsity and incompleteness of LiDAR depth data. Our method achieves superior in-path and out-of-path reconstruction and rendering performance on the widely adopted Waymo Open dataset. In addition, a simulator-based benchmark is proposed to obtain the out-of-path ground truth and quantitatively evaluate the performance of out-of-path rendering, where our method outperforms previous methods by a significant margin.

## item_id: m_1524

TITLE: A Causal Lens for Learning Long-term Fair Policies

ABSTRACT: Fairness-aware learning studies the development of algorithms that avoid discriminatory decision outcomes despite biased training data. While most studies have concentrated on immediate bias in static contexts, this paper highlights the importance of investigating long-term fairness in dynamic decision-making systems while simultaneously considering instantaneous fairness requirements. In the context of reinforcement learning, we propose a general framework where long-term fairness is measured by the difference in the average expected qualification gain that individuals from different groups could obtain. Then, through a causal lens, we decompose this metric into three components that represent the direct impact, the delayed impact, as well as the spurious effect the policy has on the qualification gain. We analyze the intrinsic connection between these components and an emerging fairness notion called benefit fairness that aims to control the equity of outcomes in decision-making. Finally, we develop a simple yet effective approach for balancing various fairness notions.

## item_id: m_1525

TITLE: Multimodal Unsupervised Domain Generalization by Retrieving Across the Modality Gap

ABSTRACT: Domain generalization (DG) is an important problem that learns a model which generalizes to unseen test domains leveraging one or more source domains, under the assumption of shared label spaces. However, most DG methods assume access to abundant source data in the target label space, a requirement that proves overly stringent for numerous real-world applications, where acquiring the same label space as the target task is prohibitively expensive. For this setting, we tackle the multimodal version of the unsupervised domain generalization (MUDG) problem, which uses a large task-agnostic unlabeled source dataset during finetuning. Our framework does not explicitly assume any relationship between the source dataset and target task. Instead, it relies only on the premise that the source dataset can be accurately and efficiently searched in a joint vision-language space. We make three contributions in the MUDG setting. Firstly, we show theoretically that cross-modal approximate nearest neighbor search suffers from low recall due to the large distance between text queries and the image centroids used for coarse quantization. Accordingly, we propose paired k-means, a simple clustering algorithm that improves nearest neighbor recall by storing centroids in query space instead of image space. Secondly, we propose an adaptive text augmentation scheme for target labels designed to improve zero-shot accuracy and diversify retrieved image data. Lastly, we present two simple but effective components to further improve downstream target accuracy. We compare against state-of-the-art name-only transfer, source-free DG and zero-shot (ZS) methods on their respective benchmarks and show consistent improvement in accuracy on 20 diverse datasets. Code is available: https://github.com/Chris210634/mudg

## item_id: m_1526

TITLE: Blending Imitation and Reinforcement Learning for Robust Policy Improvement

ABSTRACT: While reinforcement learning (RL) has shown promising performance, its sample complexity continues to be a substantial hurdle, restricting its broader application across a variety of domains. Imitation learning (IL) utilizes oracles to improve sample efficiency, yet it is often constrained by the quality of the oracles deployed. To address the demand for robust policy improvement in real-world scenarios, we introduce a novel algorithm, Robust Policy Improvement (RPI), which actively interleaves between IL and RL based on an online estimate of their performance. RPI draws on the strengths of IL, using oracle queries to facilitate exploration—an aspect that is notably challenging in sparse-reward RL—particularly during the early stages of learning. As learning unfolds, RPI gradually transitions to RL, effectively treating the learned policy as an improved oracle. This algorithm is capable of learning from and improving upon a diverse set of black-box oracles. Integral to RPI are Robust Active Policy Selection (RAPS) and Robust Policy Gradient (RPG), both of which reason over whether to perform state-wise imitation from the oracles or learn from its own value function when the learner’s performance surpasses that of the oracles in a specific state. Empirical evaluations and theoretical analysis validate that RPI excels in comparison to existing state-of-the-art methodologies, demonstrating superior performance across various benchmark domains.

## item_id: m_1527

TITLE: Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting

ABSTRACT: Probabilistic forecasting of multivariate time series is challenging due to non-stationarity, inter-variable dependencies, and distribution shifts. While recent diffusion and flow matching models have shown promise, they often ignore informative priors such as conditional means and covariances. In this work, we propose Conditionally Whitened Generative Models (CW-Gen), a framework that incorporates prior information through conditional whitening. Theoretically, we establish sufficient conditions under which replacing the traditional terminal distribution of diffusion models, namely the standard multivariate normal, with a multivariate normal distribution parameterized by estimators of the conditional mean and covariance improves sample quality. Guided by this analysis, we design a novel Joint Mean-Covariance Estimator (JMCE) that simultaneously learns the conditional mean and sliding-window covariance. Building on JMCE, we introduce Conditionally Whitened Diffusion Models (CW-Diff) and extend them to Conditionally Whitened Flow Matching (CW-Flow). Experiments on five real-world datasets with six state-of-the-art generative models demonstrate that CW-Gen consistently enhances predictive performance, capturing non-stationary dynamics and inter-variable correlations more effectively than prior-free approaches. Empirical results further demonstrate that CW-Gen can effectively mitigate the effects of distribution shift.

## item_id: m_1528

TITLE: Neural Tree Transducers for Tree to Tree Learning

ABSTRACT: We introduce a novel approach to tree-to-tree learning, the neural tree transducer (NTT), a top-down depth first context-sensitive tree decoder, which is paired with recursive neural encoders. Our method works purely on tree-to-tree manipulations rather than sequence-to-tree or tree-to-sequence and is able to encode and decode multiple depth trees. We compare our method to sequence-to-sequence models applied to serializations of the trees and show that our method outperforms previous methods for tree-to-tree transduction. 

## item_id: m_1529

TITLE: A probablistic automata learning approach for analyzing and sampling constrained LLM

ABSTRACT: We define a congruence that copes with null next-symbol probabilities that arise when the output of a language model is constrained by some means during text generation. We develop an algorithm for efficiently learning the quotient with respect to this congruence and evaluate it on case studies for analyzing statistical properties of LLM.

## item_id: m_1530

TITLE: Adapt-to-Learn: Policy Transfer in Reinforcement Learning

ABSTRACT: Efficient and robust policy transfer remains a key challenge in reinforcement learning. Policy transfer through warm initialization, imitation, or interacting over a large set of agents with randomized instances, have been commonly applied to solve a variety of Reinforcement Learning (RL) tasks. However, this is far from how behavior transfer happens in the biological world: Humans and animals are able to quickly adapt the learned behaviors between similar tasks and learn new skills when presented with new situations. Here we seek to answer the question: Will learning to combine adaptation reward with environmental reward lead to a more efficient transfer of policies between domains? We introduce a principled mechanism that can \textbf{``Adapt-to-Learn"}, that is adapt the source policy to learn to solve a target task with significant transition differences and uncertainties.  We show through theory and experiments that our method leads to a significantly reduced sample complexity of transferring the policies between the tasks.

## item_id: m_1531

TITLE: DeepRepoQA: Code Repository Question Answering with Deep Agent Exploration

ABSTRACT: Effectively answering developer questions about a software repository is a critical yet under-explored problem in software engineering. While existing repository understanding methods have advanced the field, they predominantly rely on surface-level code retrieval and lack the ability for deep reasoning over multiple files, complex software architectures, and grounding answers in long-range code dependencies. To address these limitations, we propose DeepRepoQA, a repository question answering (QA) approach in realistic code environments. DeepRepoQA builds on the agentic framework where LLM agents find answers through a systematic tree search over structured action spaces. Our key innovations include balanced exploration and exploitation via Monte Carlo Tree Search (MCTS) for multi-hop repository reasoning and LLM feedback that provides learned priors and values to reduce search depth and reduce drift. The system maintains structured memory paths that enable reliable evidence synthesis and traceable reasoning steps. Comprehensive experiments on SWE-QA demonstrate substantial performance gains over strong baselines, validating the effectiveness of systematic MCTS-guided exploration for multi-hop repository reasoning.

## item_id: m_1532

TITLE: Accelerated Inference and Reduced Forgetting: The Dual Benefits of Early-Exit Networks in Continual Learning

ABSTRACT: In the pursuit of a sustainable future for machine learning, energy-efficient neural network models are crucial. A practical approach to achieving this efficiency is through early-exit strategies. These strategies allow for swift predictions by making decisions early in the network, thereby conserving computation time and resources. However, so far the early-exit neural networks have only been developed
for stationary data distributions, which restricts their application in real-world scenarios where training data is derived from continuous non-stationary data. In this study, we aim to explore the continual training for early-exit networks. Specifically, we adapt the existing continual learning methods to fit early-exit architectures and introduce task-aware dynamic inference to improve the network accuracy for a given compute budgets. Finally, we evaluate continually those methods on the standard benchmarks to assess their accuracy and efficiency. Our work highlights the practical advantages of the early-exit networks in real-world continual learning scenarios.

## item_id: m_1533

TITLE: Objectives Are All You Need: Solving Deceptive Problems Without Explicit Diversity Maintenance

ABSTRACT: Navigating deceptive domains has often been a challenge in machine learning due to search algorithms getting stuck at sub-optimal local optima. Many algorithms have been proposed to navigate these domains by explicitly maintaining diversity or equivalently promoting exploration, such as Novelty Search or other so-called Quality Diversity algorithms. In this paper, we present an approach with promise to solve deceptive domains without explicit diversity maintenance by optimizing a potentially large set of defined objectives. These objectives can be extracted directly from the environment by sub-aggregating the raw performance of individuals in a variety of ways. We use lexicase selection to optimize for these objectives as it has been shown to implicitly maintain population diversity. We compare this technique with a varying number of objectives to a commonly used quality diversity algorithm, MAP-Elites, on a set of discrete optimization as well as reinforcement learning domains with varying degrees of deception. We find that decomposing objectives into many objectives and optimizing them outperforms MAP-Elites on the deceptive domains that we explore. Furthermore, we find that this technique results in competitive performance on the diversity-focused metrics of QD-Score and Coverage, without explicitly optimizing for these things. Our ablation study shows that this technique is robust to different sub-aggregation techniques. However, when it comes to non-deceptive, or ``illumination" domains, quality diversity techniques generally outperform our objective-based framework with respect to exploration (but not exploitation), hinting at potential directions for future work.

## item_id: m_1534

TITLE: Secure FLOATING - Scalable Federated Learning Framework for Real-time Trust in Mobility Data using Secure Multi-Party Computation and Blockchain

ABSTRACT: The safety of Connected and Autonomous Vehicles (CAVs), Micro-mobility devices (e-scooter, e-bikes) and  smartphone users rely on trusting the trajectory data they generate for navigation around each other. There is a need for real-time verification of mobility data from these devices without compromising privacy as malicious data used for navigation could be deadly, specially for vulnerable road users. In this paper, we propose Secure-FLOATING, a scalable framework leveraging federated learning and blockchain for nearby nodes to coordinate and learn to trust mobility data from nearby devices and store this information via consensus on a tamper-proof distributed ledger. We employ lightweight Secure Multi-party computation (SMPC) with reduced messages exchanges to preserve privacy of the users and ensure data validation in real-time. Secure-FLOATING is evaluated using realistic trajectories for up to 8,000 nodes (vehicles, micro-mobility devices and pedestrians) in New York City, and it shows to achieve lower delays and overhead, thereby accurately validating each others' mobility data in a scalable manner, with up to 75% successful endorsement for as high as 50% attacker penetration.

## item_id: m_1535

TITLE: Simplified Action Decoder for Deep Multi-Agent Reinforcement Learning

ABSTRACT: In recent years we have seen fast progress on a number of benchmark problems in AI, with modern methods achieving near or super human performance in Go, Poker and Dota. One common aspect of all of these challenges is that they are by design adversarial or, technically speaking, zero-sum. In contrast to these settings, success in the real world commonly requires humans to collaborate and communicate with others, in settings that are, at least partially, cooperative. In the last year, the card game Hanabi has been established as a new benchmark environment for AI to fill this gap. In particular, Hanabi is interesting to humans since it is entirely focused on theory of mind, i.e. the ability to effectively reason over the intentions, beliefs and point of view of other agents when observing their actions. Learning to be informative when observed by others is an interesting challenge for Reinforcement Learning (RL): Fundamentally, RL requires agents to explore in order to discover good policies. However, when done naively, this randomness will inherently make their actions less informative to others during training. We present a new deep multi-agent RL method, the Simplified Action Decoder (SAD), which resolves this contradiction exploiting the centralized training phase. During training SAD allows other agents to not only observe the (exploratory) action chosen, but agents instead also observe the greedy action of their team mates. By combining this simple intuition with an auxiliary task for state prediction and best practices for multi-agent learning, SAD establishes a new state of the art for 2-5 players on the self-play part of the Hanabi challenge.

## item_id: m_1536

TITLE: Optimistic Adaptive Acceleration for Optimization

ABSTRACT: This paper considers a new variant of AMSGrad called Optimistic-AMSGrad. AMSGrad is a popular adaptive gradient based optimization algorithm that is widely used in training deep neural networks. The new variant assumes that mini-batch gradients in consecutive iterations have some underlying structure, which makes the gradients sequentially predictable. By exploiting the predictability and some ideas from Optimistic Online learning, the proposed algorithm can accelerate the convergence and also enjoys a tighter regret bound. We evaluate Optimistic-AMSGrad and AMSGrad in terms of various performance measures (i.e., training loss, testing loss, and classification accuracy on training/testing data), which demonstrate that Optimistic-AMSGrad improves AMSGrad.

## item_id: m_1537

TITLE: QANet: Combining Local Convolution with Global Self-Attention for Reading Comprehension

ABSTRACT:  Current end-to-end machine reading and question answering (Q\&A) models are primarily based on recurrent neural networks (RNNs) with attention. Despite their success, these models are often slow for both training and inference due to the sequential nature of RNNs. We propose a new Q\&A architecture called QANet, which does not require recurrent networks:  Its encoder consists exclusively of convolution and self-attention, where convolution models local interactions and self-attention models global interactions. On the SQuAD dataset, our model is 3x to 13x faster in training and 4x to 9x faster in inference, while achieving equivalent accuracy to recurrent models. The speed-up gain allows us to train the model with much more data. We hence combine our model with data generated by backtranslation from a neural machine translation model. 
On the SQuAD dataset, our single model, trained with augmented data, achieves 84.6 F1 score on the test set, which is significantly better than the best published F1 score of 81.8.

## item_id: m_1538

TITLE: Debias your VLM with Counterfactuals: A Unified Approach

ABSTRACT: Recent advances in vision-language research have produced numerous foundation models that excel in tasks such as image classification, image-text retrieval, and image captioning. However, these models are shown to exploit spurious correlations in biased training data, raising fairness concerns for discrimination against underprivileged groups. 
In this work, we propose CVLD, a unified framework for quantifying and mitigating vision-language biases in a task and domain-agnostic setting. By defining a causal intervention module that produces counterfactual image-text pairs, we apply causal fairness metrics to capture the discrepancy between model predictions on original and counterfactual distributions.
Building on the universal fairness notion, we propose a set of bias-free adaptation techniques to mitigate the bias of pre-trained VL models by optimizing their robustness to interventions on the protected attribute, requiring minimal modification to the naive training pipeline. CVLD demonstrates robust debiasing results on image classification, retrieval and captioning using adaptation datasets of varying sizes, validating the importance of counterfactual data in studying vision-language bias.

## item_id: m_1539

TITLE: Learning Robust Models using the Principle of Independent Causal Mechanisms

ABSTRACT: Standard supervised learning breaks down under data distribution shift. However, the principle of independent causal mechanisms (ICM, Peters et al. (2017)) can turn this weakness into an opportunity: one can take advantage of distribution shift between different environments during training in order to obtain more robust models. We propose a new gradient-based learning framework whose objective function is derived from the ICM principle. We show theoretically and experimentally that neural networks trained in this framework focus on relations remaining invariant across environments and ignore unstable ones. Moreover, we prove that the recovered stable relations correspond to the true causal mechanisms under certain conditions. In both regression and classification, the resulting models generalize well to unseen scenarios where traditionally trained models fail.

## item_id: m_1540

TITLE: Blockwise Self-Attention for Long Document Understanding

ABSTRACT: We present BlockBERT, a lightweight and efficient BERT model that is designed to better modeling long-distance dependencies. Our model extends BERT by introducing sparse block structures into the attention matrix to reduce both memory consumption and training time, which also enables attention heads to capture either short- or long-range contextual information. We conduct experiments on several benchmark question answering datasets with various paragraph lengths. Results show that BlockBERT uses 18.7-36.1% less memory and reduces the training time by 12.0-25.1%, while having comparable and sometimes better prediction accuracy, compared to an advanced BERT-based model, RoBERTa.

## item_id: m_1541

TITLE: Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger

ABSTRACT: Per-example gradient clipping is a key algorithmic step that enables practical differential private (DP) training for deep learning models. The choice of clipping threshold $R$, however, is shown to be vital for achieving high accuracy under DP. We propose an easy-to-use replacement, called automatic clipping, that eliminates the need to tune $R$ for any DP optimizers, including DP-SGD, DP-Adam, DP-LAMB and many others.
The automatic variants are as private and computationally efficient as existing DP optimizers, but require no DP-specific hyperparameters and thus make DP training as amenable as the standard non-private training. We give a rigorous convergence analysis of automatic DP-SGD in the non-convex setting, which shows that it {can enjoy an asymptotic convergence rate that matches the standard SGD, under a symmetric gradient noise assumption of the per-sample gradients.} We also demonstrate on various language and vision tasks that automatic clipping outperforms or matches the state-of-the-art, and can be easily employed with minimal changes to existing codebases.

## item_id: m_1542

TITLE: Leveraging Diffusion Transformers for Stock Factor Augmentation in Financial Markets

ABSTRACT: Data scarcity poses a significant challenge in training machine learning models for stock forecasting, often leading to low signal-to-noise ratio (SNR) and data homogeneity that degrade model performance. To address these issues, we introduce DiffsFormer, a novel approach utilizing artificial intelligence-generated samples (AIGS) with a Transformer-based Diffusion Model. Initially trained on a large-scale source domain with conditional guidance to capture global joint distribution, DiffsFormer augments training by editing existing samples for specific downstream tasks, allowing control over the deviation of generated data from the target domain. We evaluate DiffsFormer on the CSI300 and CSI800 datasets using eight commonly used machine learning models, achieving relative improvements of 7.3\% and 22.1\% in annualized return ratio, respectively. Extensive experiments provide insights into DiffsFormer's functionality and its components, illustrating their role in mitigating data scarcity and enhancing model performance. Our findings demonstrate the potential of AIGS and DiffsFormer in addressing data limitations in stock forecasting, with the ability to generate realistic stock factors and control the editing process. These results validate our approach and contribute to a deeper understanding of its underlying mechanisms.

## item_id: m_1543

TITLE: On the relationship between topology and gradient propagation in deep networks

ABSTRACT: In this paper, we address two fundamental research questions in neural architecture design: (i) How does the architecture topology impact the gradient flow during training? (ii) Can certain topological characteristics of deep networks indicate a priori (i.e., without training) which models, with a different number of parameters/FLOPS/layers, achieve a similar accuracy? To this end, we formulate the problem of deep learning architecture design from a network science perspective and introduce a new metric called NN-Mass to quantify how effectively information flows through a given architecture. We establish a theoretical link between NN-Mass, a topological property of neural architectures, and gradient flow characteristics (e.g., Layerwise Dynamical Isometry). As such, NN-Mass can identify models with similar accuracy, despite having significantly different size/compute requirements. Detailed experiments on both synthetic and real datasets (e.g., MNIST, CIFAR-10, CIFAR-100, ImageNet) provide extensive evidence for our insights. Finally, we show that the closed-form equation of our theoretically grounded NN-Mass metric enables us to design efficient architectures directly without time-consuming training and searching.

## item_id: m_1544

TITLE: The Effectiveness of Pre-Trained Code Embeddings

ABSTRACT: Word embeddings are widely used in machine learning based natural language processing systems. It is common to use pre-trained word embeddings which provide benefits such as reduced training time and improved overall performance. There has been a recent interest in applying natural language processing techniques to programming languages. However, none of this recent work uses pre-trained embeddings on code tokens. Using extreme summarization as the downstream task, we show that using pre-trained embeddings on code tokens provides the same benefits as it does to natural languages, achieving: over 1.9x speedup, 5\% improvement in test loss, 4\% improvement in F1 scores, and resistance to over-fitting. We also show that the choice of language used for the embeddings does not have to match that of the task to achieve these benefits and that even embeddings pre-trained on human languages provide these benefits to programming languages.   

## item_id: m_1545

TITLE: Adversarial Driving Policy Learning by Misunderstanding the Traffic Flow

ABSTRACT: Acquiring driving policies that can transfer to unseen environments is essential for driving in dense traffic flows. Adversarial training is a promising path to improve robustness under disturbances. Most prior works leverage few agents to induce driving policy's failures. However, we argue that directly implementing this training framework into dense traffic flow degrades transferability in unseen environments. In this paper, we propose a novel robust policy training framework that is capable of applying adversarial training based on a coordinated traffic flow. We start by building up a coordinated traffic flow where agents are allowed to communicate Social Value Orientations (SVOs). Adversary emerges when the traffic flow misunderstands the SVO of driving agent. We utilize this property to formulate a minimax optimization problem where the driving policy maximizes its own reward and a spurious adversarial policy minimizes it. Experiments demonstrate that our adversarial training framework significantly improves zero-shot transfer performance of the driving policy in dense traffic flows compared to existing algorithms.

## item_id: m_1546

TITLE: Diffusion Probabilistic Modeling of Protein Backbones in 3D for the motif-scaffolding problem

ABSTRACT: Construction of a scaffold structure that supports a desired motif, conferring protein function, shows promise for the design of vaccines and enzymes. But a general solution to this motif-scaffolding problem remains open. Current machine-learning techniques for scaffold design are either limited to unrealistically small scaffolds (up to length 20) or struggle to produce multiple diverse scaffolds. We propose to learn a distribution over diverse and longer protein backbone structures via an E(3)-equivariant graph neural network. We develop SMCDiff to efficiently sample scaffolds from this distribution conditioned on a given motif; our algorithm is the first to theoretically guarantee conditional samples from a diffusion model in the large-compute limit. We evaluate our designed backbones by how well they align with AlphaFold2-predicted structures. We show that our method can (1) sample scaffolds up to 80 residues and (2) achieve structurally diverse scaffolds for a fixed motif.

## item_id: m_1547

TITLE: Contemplating Real-World Object Classification

ABSTRACT: Deep object recognition models have been very successful over benchmark
datasets such as ImageNet. How accurate and robust are they to distribution
shifts arising from natural and synthetic variations in datasets? Prior research on
this problem has primarily focused on ImageNet variations (e.g., ImageNetV2,
ImageNet-A). To avoid potential inherited biases in these studies, we take a
different approach. Specifically, we reanalyze the ObjectNet dataset recently
proposed by Barbu et al. containing objects in daily life situations. They showed
a dramatic performance drop of the state of the art object recognition models on
this dataset. Due to the importance and implications of their results regarding
the generalization ability of deep models, we take a second look at their analysis.
We find that applying deep models to the isolated objects, rather than the entire
scene as is done in the original paper, results in around 20-30% performance
improvement. Relative to the numbers reported in Barbu et al., around 10-15%
of the performance loss is recovered, without any test time data augmentation.
Despite this gain, however, we conclude that deep models still suffer drastically
on the ObjectNet dataset. We also investigate the robustness of models against
synthetic image perturbations such as geometric transformations (e.g., scale,
rotation, translation), natural image distortions (e.g., impulse noise, blur) as well
as adversarial attacks (e.g., FGSM and PGD-5). Our results indicate that limiting
the object area as much as possible (i.e., from the entire image to the bounding
box to the segmentation mask) leads to consistent improvement in accuracy and
robustness. Finally, through a qualitative analysis of ObjectNet data, we find that
i) a large number of images in this dataset are hard to recognize even for humans,
and ii) easy (hard) samples for models match with easy (hard) samples for humans.
Overall, our analysis shows that ObjecNet is still a challenging test platform that
can be used to measure the generalization ability of models. The code and data
are available in [masked due to blind review].

## item_id: m_1548

TITLE: Intelligible Language Modeling with Input Switched Affine Networks

ABSTRACT: The computational mechanisms by which nonlinear recurrent neural networks (RNNs) achieve their goals remains an open question.  There exist many problem domains where intelligibility of the network model is crucial for deployment. Here we introduce a recurrent architecture composed of input-switched affine transformations, in other words an RNN without any nonlinearity and with one set of weights per input.
We show that this architecture achieves near identical performance to traditional architectures on language modeling of Wikipedia text, for the same number of model parameters. 
It can obtain this performance with the potential for computational speedup compared to existing methods, by precomputing the composed affine transformations corresponding to longer input sequences. 
As our architecture is affine, we are able to understand the mechanisms by which it functions using linear methods. For example, we show how the network linearly combines contributions from the past to make predictions at the current time step. We show how representations for words can be combined in order to understand how context is transferred across word boundaries. Finally, we demonstrate how the system can be executed and analyzed in arbitrary bases to aid understanding.

## item_id: m_1549

TITLE: Training Compressed Fully-Connected Networks with a Density-Diversity Penalty

ABSTRACT: Deep models have achieved great success on a variety of challenging tasks. How- ever, the models that achieve great performance often have an enormous number of parameters, leading to correspondingly great demands on both computational and memory resources, especially for fully-connected layers. In this work, we propose a new “density-diversity penalty” regularizer that can be applied to fully-connected layers of neural networks during training. We show that using this regularizer results in significantly fewer parameters (i.e., high sparsity), and also significantly fewer distinct values (i.e., low diversity), so that the trained weight matrices can be highly compressed without any appreciable loss in performance. The resulting trained models can hence reside on computational platforms (e.g., portables, Internet-of-Things devices) where it otherwise would be prohibitive.

## item_id: m_1550

TITLE: Enhance Word Representation for Out-of-Vocabulary on Ubuntu Dialogue Corpus

ABSTRACT: Ubuntu dialogue corpus is the largest public available dialogue corpus to make it feasible to build end-to-end
deep neural network models directly from the conversation data. One challenge of Ubuntu dialogue corpus is 
the large number of out-of-vocabulary words. In this paper we proposed an algorithm which combines the general pre-trained word embedding vectors with those  generated on the task-specific training set to address this issue.  We integrated character embedding into Chen et al's Enhanced LSTM method (ESIM) and used it to evaluate the effectiveness of our proposed method. For the task of next utterance selection, the proposed method has demonstrated a significant performance improvement against original ESIM and the new model has achieved state-of-the-art results on both Ubuntu dialogue corpus and Douban conversation corpus. In addition, we investigated the performance impact of end-of-utterance and end-of-turn token tags. 

## item_id: m_1551

TITLE: Hallucinative Topological Memory for Zero-Shot Visual Planning

ABSTRACT: In visual planning (VP), an agent learns to plan goal-directed behavior from observations of a dynamical system obtained offline, e.g., images obtained from self-supervised robot interaction. VP algorithms essentially combine data-driven perception and planning, and are important for robotic manipulation and navigation domains, among others. A recent and promising approach to VP is the semi-parametric topological memory (SPTM) method, where image samples are treated as nodes in a graph, and the connectivity in the graph is learned using deep image classification. Thus, the learned graph represents the topological connectivity of the data, and planning can be performed using conventional graph search methods. However, training SPTM necessitates a suitable loss function for the connectivity classifier, which requires non-trivial manual tuning. More importantly, SPTM is constricted in its ability to generalize to changes in the domain, as its graph is constructed from direct observations and thus requires collecting new samples for planning. In this paper, we propose Hallucinative Topological Memory (HTM), which overcomes these shortcomings. In HTM, instead of training a discriminative classifier we train an energy function using contrastive predictive coding. In addition, we learn a conditional VAE model that generates samples given a context image of the domain, and use these hallucinated samples for building the connectivity graph, allowing for zero-shot generalization to domain changes. In simulated domains, HTM outperforms conventional SPTM and visual foresight methods in terms of both plan quality and success in long-horizon planning. 

## item_id: m_1552

TITLE: Pixel Deconvolutional Networks

ABSTRACT: Deconvolutional layers have been widely used in a variety of deep
models for up-sampling, including encoder-decoder networks for
semantic segmentation and deep generative models for unsupervised
learning. One of the key limitations of deconvolutional operations
is that they result in the so-called checkerboard problem. This is
caused by the fact that no direct relationship exists among adjacent
pixels on the output feature map. To address this problem, we
propose the pixel deconvolutional layer (PixelDCL) to establish
direct relationships among adjacent pixels on the up-sampled feature
map. Our method is based on a fresh interpretation of the regular
deconvolution operation. The resulting PixelDCL can be used to
replace any deconvolutional layer in a plug-and-play manner without
compromising the fully trainable capabilities of original models.
The proposed PixelDCL may result in slight decrease in efficiency,
but this can be overcome by an implementation trick. Experimental
results on semantic segmentation demonstrate that PixelDCL can
consider spatial features such as edges and shapes and yields more
accurate segmentation outputs than deconvolutional layers. When used
in image generation tasks, our PixelDCL can largely overcome the
checkerboard problem suffered by regular deconvolution operations.

## item_id: m_1553

TITLE: Can you Trust your Disentanglement?

ABSTRACT: There has been growing interest, in recent years, in learning disentangled representations of data. These are representations in which distinct features, such as size or shape, are represented by distinct neurons. Measuring disentanglement, i.e., quantifying the extent to which a given representation is disentangled, is not straightforward. Multiple metrics have been proposed. In this paper, we identify two failings of existing metrics, and show how they can assign a high score to a model which is still entangled. We then propose two new metrics which redress these problems. Additionally, we introduce the task of recognizing novel combinations of familiar features (NCFF), which we argue is doable if and only if the model is disentangled. As well as being desirable in itself, NCFF provides a tangible downstream task that can help focus the field of disentanglement research, in contrast to the set of bespoke metrics that are currently used. We then show empirically that existing methods perform poorly on our proposed metrics and fail at recognizing NCFF and so, we argue, are not disentangled.

## item_id: m_1554

TITLE: Graph Convolutional Network with Sequential Attention For Goal-Oriented Dialogue Systems

ABSTRACT: Domain specific goal-oriented dialogue systems typically require modeling three types of inputs, viz., (i) the knowledge-base associated with the domain, (ii) the history of the conversation, which is a sequence of utterances and (iii) the current utterance for which the response needs to be generated. While modeling these inputs, current state-of-the-art models such as Mem2Seq typically ignore the rich structure inherent in the knowledge graph and the sentences in the conversation context. Inspired by the recent success of structure-aware Graph Convolutional Networks (GCNs) for various NLP tasks such as machine translation, semantic role labeling and document dating, we propose a memory augmented GCN for goal-oriented dialogues. Our model exploits (i) the entity relation graph in a knowledge-base  and (ii) the dependency graph associated with an utterance to compute richer representations for words and entities. Further, we take cognizance of the fact that in certain situations, such as, when the conversation is in a code-mixed language, dependency parsers may not be available. We show that in such situations we could use the global word co-occurrence graph and use it to enrich the representations of utterances. We experiment with the modified DSTC2 dataset and its recently released code-mixed versions in four languages and show that our method outperforms existing state-of-the-art methods, using a wide range of evaluation metrics.

## item_id: m_1555

TITLE: Multivariate Probabilistic Time Series Forecasting via Conditioned Normalizing Flows

ABSTRACT: Time series forecasting is often fundamental to scientific and engineering problems and enables decision making. With ever increasing data set sizes, a trivial solution to scale up predictions is to assume independence between interacting time series. However, modeling statistical dependencies can improve accuracy and enable analysis of interaction effects. Deep learning methods are well suited for this problem, but multi-variate models often assume a simple parametric distribution and do not scale to high dimensions. In this work we model the multi-variate temporal dynamics of time series via an autoregressive deep learning model, where the data distribution  is represented by a conditioned normalizing flow. This combination retains the power of autoregressive models, such as good performance in extrapolation into the future, with the flexibility of flows as a general purpose high-dimensional distribution model, while remaining computationally tractable. We show that it improves over the state-of-the-art for standard metrics on many real-world data sets with several thousand interacting time-series.

## item_id: m_1556

TITLE:  Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

ABSTRACT: The capacity of a neural network to absorb information is limited by its number of parameters.  Conditional computation, where parts of the network are active on a per-example basis, has been proposed in theory as a way of dramatically increasing model capacity without a proportional increase in computation.  In practice, however, there are significant algorithmic and performance challenges.  In this work, we address these challenges and finally realize the promise of conditional computation, achieving greater than 1000x improvements in model capacity with only minor losses in computational efficiency on modern GPU clusters.  We introduce a Sparsely-Gated Mixture-of-Experts layer (MoE), consisting of up to thousands of feed-forward sub-networks.  A trainable gating network determines a sparse combination of these experts to use for each example.  We apply the MoE to the tasks of language modeling and machine translation, where model capacity is critical for absorbing the vast quantities of knowledge available in the training corpora.  We present model architectures in which a MoE with up to 137 billion parameters is applied convolutionally between stacked LSTM layers.  On large language modeling and machine translation benchmarks, these models achieve significantly better results than state-of-the-art at lower computational cost.

## item_id: m_1557

TITLE: Emergent Global OOD Performance in Multimodal Mammography Models

ABSTRACT: Out-of-distribution (OOD) generalization is a central barrier to deploying mam-
mography AI fairly across health systems, especially in LMICs. We test whether
parameter scale alone, within one architecture family and without adding ex-
tra images, yields emergent robustness in a CLIP-trained vision–language model
(VLM). Using EMBED-open (22k patients; 480k 2D views), we train on cohort-1
only (11k patients; 240k images) a CLIP VLM whose ViT patch-16 image tower
spans 6M, 22M, 86M, and 307M parameters; multimodality is limited to short,
de-identified captions (sex, age, ethnicity, manufacturer, view) with a frozen
biomedical text encoder, and downstream clinical targets are modeled via lin-
ear probes on learned embeddings. We evaluate zero-shot on five international
OOD cohorts—DMID (India), VinDr-Mammo (Vietnam), KAU-BCMD (Saudi
Arabia), CMMD (China), and INBreast (Portugal). In-domain performance in-
creases roughly linearly with log-parameters, whereas OOD performance shows
a modest upward trend with a pronounced knee at the largest scale on several
cohorts; gains are most visible at the most clinically relevant low-FPR operat-
ing points (pAUC@0–10% and TPR@5% FPR). Achieved without extra data,
task labels during training, or architectural changes, this pattern is consistent with
emergent global OOD robustness from scale in multimodal mammography mod-
els. Consequently, parameter scale should be a first-class design lever for globally
deployable VLMs, and downsizing via smaller models, pruning, or quantization
should be accompanied by OOD monitoring across international cohorts to avoid
eroding this scale-driven robustness.

## item_id: m_1558

TITLE: Adaptive Speech Duration Modification using a Deep-Generative Framework

ABSTRACT: We propose the first method to adaptively modify the duration of a given speechsignal.  Our approach uses a Bayesian framework to define a latent attention mapthat links frames of the input and target utterances. We train a masked convolu-tional encoder-decoder network to generate this attention map via a stochastic ver-sion of the mean absolute error loss function. Our model also predicts the lengthof the target speech signal using the encoder embeddings, which determines thenumber of time steps for the decoding operation. During testing, we generate theattention map as a proxy for the similarity matrix between the given input speechand an unknown target speech signal. Using this similarity matrix, we compute awarping path of alignment between the two signals. Our experiments demonstratethat this adaptive framework produces similar results to dynamic time warping,which relies on a known target signal, on both voice conversion and emotion con-version tasks. We also show that the modified speech utterances achieve high userquality ratings, thus highlighting the practical utility of our method. 

## item_id: m_1559

TITLE: Learning Diverse and Effective Policies with Non-Markovian Rewards

ABSTRACT: Learning a set of diverse and high-quantity policies is a difficult problem in Reinforcement Learning since the diversity of policies is demanded to be achieved without dampening their effectiveness. This problem becomes more challenging when the rewards are non-Markovian, i.e., the rewards depend on the history of states and actions, which are quite sparse and returned over a long period. The sparse supervision signals and the non-Markovian properties of the rewards hinder the learning of policy embeddings and thus the learning of diverse and high-quality policies. In this paper, we propose to use a diversity matrix to quantify policy diversity and theoretically prove that if the diversity matrix is positive definite, then the diversity of policies can be achieved without sacrificing their effectiveness. The policy diversity matrix stems from policy embeddings. To obtain high-quality embeddings, we adopt a transformer to capture mutual dependencies between states and actions and design pseudo tasks to overcome sparse rewards. Experimental results show that our method can achieve a set of policies with more effective diversity and better performance than multiple recently proposed baseline methods in a variety of non-Markovian and Markovian environments.

## item_id: m_1560

TITLE: Long-context Protein Language Model

ABSTRACT: Self-supervised training of language models (LMs) has seen great success for protein sequences in learning meaningful representations and for generative drug design. 
Most protein LMs are based on the Transformer architecture trained on individual proteins with short context lengths. Such protein LMs cannot extrapolate to longer proteins and protein complexes well. They also fail to account for the underlying biological mechanisms carried out by biomolecular interactions and dynamics i.e., proteins often interact with other proteins, molecules, and pathways in complex biological systems. 
In this work, we propose LC-PLM based on an alternative protein LM architecture, BiMamba-S, built off selective structured state-space models, to learn high-quality universal protein representations at the amino acid token level using masked language modeling. We also introduce its graph-contextual variant, LC-PLM-G, which contextualizes protein-protein interaction (PPI) graphs for a second stage of training. LC-PLM demonstrates favorable neural scaling laws, better length extrapolation capability, and a 7\% to 34\% improvement on protein downstream tasks than Transformer-based ESM-2. LC-PLM-G further trained within the context of PPI graphs shows promising results on protein structure and function prediction tasks. Our study demonstrates the benefit of increasing the context size with computationally efficient LM architecture (e.g. structured SSMs) in learning universal protein representations and incorporating molecular interaction contexts contained in biological graphs.

## item_id: m_1561

TITLE: On the Quantitative Analysis of Decoder-Based Generative Models

ABSTRACT: The past several years have seen remarkable progress in generative models which produce convincing samples of images and other modalities. A shared component of some popular models such as generative adversarial networks and generative moment matching networks, is a decoder network, a parametric deep neural net that defines a generative distribution. Unfortunately, it can be difficult to quantify the performance of these models because of the intractability of log-likelihood estimation, and inspecting samples can be misleading. We propose to use Annealed Importance Sampling for evaluating log-likelihoods for decoder-based models and validate its accuracy using bidirectional Monte Carlo. Using this technique, we analyze the performance of decoder-based models, the effectiveness of existing log-likelihood estimators, the degree of overfitting, and the degree to which these models miss important modes of the data distribution.

## item_id: m_1562

TITLE: A Lazy Hessian Evaluation Framework for Accelerating Stochastic Bilevel Optimization

ABSTRACT: Bilevel optimization has recently gained popularity because of its applicability in many machine learning applications.
Hypergradient-based algorithms have been widely used for solving bilevel optimization problems because of their strong theoretical and empirical performance in many applications. 
However, computing these hypergradients requires the evaluation of Hessians (or Hessian-vector products) of the lower-level objective, which presents a major computational bottleneck. 
To address this challenge, in this paper, we propose LazyBLO 
(**Lazy** Hessian Evaluation in **B**i**l**evel **O**ptimization), an algorithmic framework that allows infrequent Hessian computation during the execution of the algorithm for solving stochastic bilevel problems.
This allows the algorithm to execute faster compared to the state-of-the-art (SOTA) algorithms that evaluate either a single or multiple Hessians in each iteration. 
We theoretically establish the performance of vanilla SGD-based LazyBLO and show that, despite the additional errors incurred by the infrequent Hessian evaluations, LazyBLO surprisingly matches the computation complexity of the existing SGD-based bilevel algorithms.
Extensive experiments further demonstrate that LazyBLO enjoys significant gains in numerical performance compared to the SOTA approaches. 
To our knowledge, this is the first work to theoretically establish that multiple Hessian computations are not necessary within each iteration to guarantee the convergence of stochastic bilevel algorithms.

## item_id: m_1563

TITLE: SoftTarget Regularization: An Effective Technique to Reduce Over-Fitting in Neural Networks

ABSTRACT: Deep neural networks are learning models with a very high capacity and therefore prone to over-fitting. Many regularization techniques such as Dropout, DropConnect, and weight decay all attempt to solve the problem of over-fitting by reducing the capacity of their respective models (Srivastava et al., 2014), (Wan et al., 2013), (Krogh & Hertz, 1992). In this paper we introduce a new form of regularization that guides the learning problem in a way that reduces over-fitting without sacrificing the capacity of the model. The mistakes that models make in early stages of training carry information about the learning problem. By adjusting the labels of the current epoch of training through a weighted average of the real labels, and an exponential average of the past soft-targets we achieved a regularization scheme as powerful as Dropout without necessarily reducing the capacity of the model, and simplified the complexity of the learning problem. SoftTarget regularization proved to be an effective tool in various neural network architectures.

## item_id: m_1564

TITLE: Generative Modeling Helps Weak Supervision (and Vice Versa)

ABSTRACT: Many promising applications of supervised machine learning face hurdles in the acquisition of labeled data in sufficient quantity and quality, creating an expensive bottleneck. To overcome such limitations, techniques that do not depend on ground truth labels have been studied, including weak supervision and generative modeling. While these techniques would seem to be usable in concert, improving one another, how to build an interface between them is not well-understood. In this work, we propose a model fusing programmatic weak supervision and generative adversarial networks and provide theoretical justification motivating this fusion. The proposed approach captures discrete latent variables in the data alongside the weak supervision derived label estimate. Alignment of the two allows for better modeling of sample-dependent accuracies of the weak supervision sources, improving the estimate of unobserved labels. It is the first approach to enable data augmentation through weakly supervised synthetic images and pseudolabels. Additionally, its learned latent variables can be inspected qualitatively. The model outperforms baseline weak supervision label models on a number of multiclass image classification datasets, improves the quality of generated images, and further improves end-model performance through data augmentation with synthetic samples.

## item_id: m_1565

TITLE: VAENAS: Sampling Matters in Neural Architecture Search

ABSTRACT: Neural Architecture Search (NAS) aims at automatically finding neural network architectures within an enormous designed search space. The search space usually contains billions of network architectures which causes extremely expensive computing costs in searching for the best-performing architecture. One-shot and gradient-based NAS approaches have recently shown to achieve superior results on various computer vision tasks such as image recognition. With the weight sharing mechanism, these methods lead to efficient model search. Despite their success, however, current sampling methods are either fixed or hand-crafted and thus ineffective. In this paper, we propose a learnable sampling module based on variational auto-encoder (VAE) for neural architecture search (NAS), named as VAENAS, which can be easily embedded into existing weight sharing NAS framework, e.g., one-shot approach and gradient-based approach, and significantly improve the performance of searching results. VAENAS generates a series of competitive results on CIFAR-10 and ImageNet in NasNet-like search space. Moreover, combined with one-shot approach, our method achieves a new state-of-the-art result for ImageNet classification model under 400M FLOPs with 77.4\% in ShuffleNet-like search space. Finally, we conduct a thorough analysis of VAENAS on NAS-bench-101 dataset, which demonstrates the effectiveness of our proposed methods.


## item_id: m_1566

TITLE: Triple Wins: Boosting Accuracy, Robustness and Efficiency Together by Enabling Input-Adaptive Inference

ABSTRACT: Deep networks were recently suggested to face the odds between accuracy (on clean natural images) and robustness (on adversarially perturbed images) (Tsipras et al., 2019). Such a dilemma is shown to be rooted in the inherently higher sample complexity (Schmidt et al., 2018) and/or model capacity (Nakkiran, 2019), for learning a high-accuracy and robust classifier. In view of that, give a classification task, growing the model capacity appears to help draw a win-win between accuracy and robustness, yet at the expense of model size and latency, therefore posing challenges for resource-constrained applications. Is it possible to co-design model accuracy, robustness and efficiency to achieve their triple wins? This paper studies multi-exit networks associated with input-adaptive efficient inference, showing their strong promise in achieving a “sweet point" in co-optimizing model accuracy, robustness, and efficiency. Our proposed solution, dubbed Robust Dynamic Inference Networks (RDI-Nets), allows for each input (either clean or adversarial) to adaptively choose one of the multiple output layers (early branches or the final one) to output its prediction. That multi-loss adaptivity adds new variations and flexibility to adversarial attacks and defenses, on which we present a systematical investigation. We show experimentally that by equipping existing backbones with such robust adaptive inference, the resulting RDI-Nets can achieve better accuracy and robustness, yet with over 30% computational savings, compared to the defended original models.


## item_id: m_1567

TITLE: Sensitivity and Generalization in Neural Networks: an Empirical Study

ABSTRACT: In practice it is often found that large over-parameterized neural networks generalize better than their smaller counterparts, an observation that appears to conflict with classical notions of function complexity, which typically favor smaller models. In this work, we investigate this tension between complexity and generalization through an extensive empirical exploration of two natural metrics of complexity related to sensitivity to input perturbations. Our experiments survey thousands of models with different architectures, optimizers, and other hyper-parameters, as well as four different image classification datasets.

We find that trained neural networks are more robust to input perturbations in the vicinity of the training data manifold, as measured by the input-output Jacobian of the network, and that this correlates well with generalization. We further establish that factors associated with poor generalization -- such as full-batch training or using random labels -- correspond to higher sensitivity, while factors associated with good generalization  -- such as data augmentation and ReLU non-linearities -- give rise to more robust functions. Finally, we demonstrate how the input-output Jacobian norm can be predictive of generalization at the level of individual test points.

## item_id: m_1568

TITLE: Domain Generalization with MixStyle

ABSTRACT: Though convolutional neural networks (CNNs) have demonstrated remarkable ability in learning discriminative features, they often generalize poorly to unseen domains. Domain generalization aims to address this problem by learning from a set of source domains a model that is generalizable to any unseen domain. In this paper, a novel approach is proposed based on probabilistically mixing instance-level feature statistics of training samples across source domains. Our method, termed MixStyle, is motivated by the observation that visual domain is closely related to image style (e.g., photo vs.~sketch images). Such style information is captured by the bottom layers of a CNN where our proposed style-mixing takes place. Mixing styles of training instances results in novel domains being synthesized implicitly, which increase the domain diversity of the source domains, and hence the generalizability of the trained model. MixStyle fits into mini-batch training perfectly and is extremely easy to implement. The effectiveness of MixStyle is demonstrated on a wide range of tasks including category classification, instance retrieval and reinforcement learning.

## item_id: m_1569

TITLE: Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges

ABSTRACT: Large Language Models (LLMs) are increasingly employed as automated judges for evaluating generative models. 
However, their known *stylistic biases*, such as a preference for verbosity or specific sentence structures, present an underexplored *security vulnerability*. 
In this work, we introduce **BITE** (**BI**as explora**T**ion and **E**xploitation), a black-box adversarial framework that learns semantics-preserving edits to mislead the judgment and **artificially** inflate judged scores. 
We cast the selection of stylistic edits as a contextual bandit problem and use a LinUCB policy to adaptively choose edits that maximize the judge’s score without access to model parameters or gradients. 
Theoretically, we prove a formal regret guarantee for our BITE, demonstrating its ability to efficiently learn to manipulate a judge in the realistic setting of model misspecification.
Empirically, we test BITE across a diverse range of LLM judges and tasks, including both pointwise and pairwise comparisons on chatbot leaderboards and AI-reviewer benchmarks. BITE achieves an attack success rate \(>\!65\%\) and raises scores by \(+1\)–\(2\) on a 9-point scale, while maintaining semantic equivalence. 
We further uncover model-specific "vulnerability fingerprints": judges differ in sensitivity to sentiment, register, and structural cues (e.g., headers), limiting cross-model transferability. Finally, we evaluate stealthiness and show that BITE evades standard style-control and simple detection baselines.
Our findings expose a fundamental weakness in the LLM-as-a-judge paradigm and motivate robust, attack-aware evaluation, e.g., style normalization, randomized prompting, and adversarial training of judges.

## item_id: m_1570

TITLE: SongEcho: Towards Cover Song Generation via Instance-Adaptive Element-wise Linear Modulation

ABSTRACT: Cover songs constitute a vital aspect of musical culture, preserving the core melody of an original composition while reinterpreting it to infuse novel emotional depth and thematic emphasis. Although prior research has explored the reinterpretation of instrumental music through melody-conditioned text-to-music models, the task of cover song generation remains largely unaddressed. In this work, we reformulate our cover song generation as a conditional generation, which simultaneously generates new vocals and accompaniment conditioned on the original vocal melody and text prompts. To this end, we present SongEcho, which leverages Instance-Adaptive Element-wise Linear Modulation (IA-EiLM), a framework that incorporates controllable generation by improving both conditioning injection mechanism and conditional representation. To enhance the conditioning injection mechanism, we extend Feature-wise Linear Modulation (FiLM) to an Element-wise Linear Modulation (EiLM), to facilitate precise temporal alignment in melody control. For conditional representations, we propose Instance-Adaptive Condition Refinement (IACR), which refines conditioning features by interacting with the hidden states of the generative model, yielding instance-adaptive conditioning. Additionally, to address the scarcity of large-scale, open-source full-song datasets, we construct Suno70k, a high-quality AI song dataset enriched with comprehensive annotations. Experimental results across multiple datasets demonstrate that our approach generates superior cover songs compared to existing methods, while requiring fewer than 30% of the trainable parameters. The code, dataset, and demos are available at [https://github.com/lsfhuihuiff/SongEcho_ICLR2026](https://github.com/lsfhuihuiff/SongEcho_ICLR2026).

## item_id: m_1571

TITLE: Linear Time Complexity Deep Fourier Scattering Network and Extension to Nonlinear Invariants

ABSTRACT: In this paper we propose a scalable version of a state-of-the-art deterministic time-
invariant feature extraction approach based on consecutive changes of basis and
nonlinearities, namely, the scattering network. The first focus of the paper is to
extend the scattering network to allow the use of higher order nonlinearities as
well as extracting nonlinear and Fourier based statistics leading to the required in-
variants of any inherently structured input. In order to reach fast convolutions and
to leverage the intrinsic structure of wavelets, we derive our complete model in the
Fourier domain. In addition of providing fast computations, we are now able to
exploit sparse matrices due to extremely high sparsity well localized in the Fourier
domain. As a result, we are able to reach a true linear time complexity with in-
puts in the Fourier domain allowing fast and energy efficient solutions to machine
learning tasks. Validation of the features and computational results will be pre-
sented through the use of these invariant coefficients to perform classification on
audio recordings of bird songs captured in multiple different soundscapes. In the
end, the applicability of the presented solutions to deep artificial neural networks
is discussed.

## item_id: m_1572

TITLE: Generative Adversarial Self-Imitation Learning

ABSTRACT: This paper explores a simple regularizer for reinforcement learning by proposing Generative Adversarial Self-Imitation Learning (GASIL), which encourages the agent to imitate past good trajectories via generative adversarial imitation learning framework. Instead of directly maximizing rewards, GASIL focuses on reproducing past good trajectories, which can potentially make long-term credit assignment easier when rewards are sparse and delayed. GASIL can be easily combined with any policy gradient objective by using GASIL as a learned reward shaping function. Our experimental results show that GASIL improves the performance of proximal policy optimization on 2D Point Mass and MuJoCo environments with delayed reward and stochastic dynamics.

## item_id: m_1573

TITLE: HumanTOMATO: Text-aligned Whole-body Motion Generation

ABSTRACT: This work targets a novel text-driven **whole-body** motion generation task, which takes a given textual description as input and aims at generating high-quality, diverse, and coherent facial expressions, hand gestures, and body motions simultaneously.
Previous works on text-driven motion generation tasks mainly have two limitations: they ignore the key role of fine-grained hand and face controlling in vivid whole-body motion generation, and lack a good alignment between text and motion.
To address such limitations, we propose a Text-aligned whOle-body Motion generATiOn framework, named HumanTOMATO, which is the first attempt to our knowledge towards applicable holistic motion generation in this research area. 
To tackle this challenging task, our solution includes two key designs: (1) a Holistic Hierarchical VQ-VAE (aka H${}^{2}$VQ) and a Hierarchical-GPT for fine-grained body and hand motion reconstruction and generation with two structured codebooks; 
and (2) a pre-trained text-motion-alignment model to help generated motion align with the input textual description explicitly.
Comprehensive experiments verify that our model has significant advantages in both the quality of generated motions and their alignment with text.
Our project codes will be public. The demo video is available in the supplementary.

## item_id: m_1574

TITLE: M6-10T: A Sharing-Delinking Paradigm for Efficient Multi-Trillion Parameter Pretraining

ABSTRACT: Recent expeditious developments in deep learning algorithms, distributed training, and even hardware design for large models have enabled training extreme-scale models, say GPT-3 and Switch Transformer possessing hundreds of billions or even trillions of parameters. However, under limited resources, extreme-scale model training that requires enormous amounts of computes and memory footprint suffers from frustratingly low efficiency in model convergence. In this paper, we propose a simple training strategy called “Pseudo-to-Real” for high-memory-footprint-required large models. Pseudo-to-Real is compatible with large models with architecture of sequential layers. We demonstrate a practice of pretraining unprecedented 10-trillion-parameter model, an order of magnitude larger than the state-of-the-art, on solely 512 GPUs within 10 days. Besides demonstrating the application of Pseudo-to-Real, we also provide a technique, Granular CPU offloading, to manage CPU memory for training large model and maintain high GPU utilities. Fast training of extreme-scale models on a decent amount of resources can bring much smaller carbon footprint and contribute to greener AI.

## item_id: m_1575

TITLE: Neural Functional Programming

ABSTRACT: We discuss a range of modeling choices that arise when constructing an end-to-end differentiable programming language suitable for learning programs from input-output examples. Taking cues from programming languages research, we study the effect of memory allocation schemes, immutable data, type systems, and built-in control-flow structures on the success rate of learning algorithms. We build a range of models leading up to a simple differentiable functional programming language. Our empirical evaluation shows that this language allows to learn far more programs than existing baselines.

## item_id: m_1576

TITLE: Unified Anomaly Detection via Multi-Scale Contrasted Memory

ABSTRACT: Deep anomaly detection (AD) aims to provide robust and efficient classifiers for one-class (OC) and outlier-exposure (OE) settings. However current models still struggle on edge-case normal samples and are often unable to keep high performance over different scales of anomalies. Additionally, there is a lack of a unified framework that efficiently addresses both OC and OE settings. To address these limitations, we present a novel two-stage method which leverages multi-scale normal prototypes during training to compute an anomaly deviation score. First, we employ a novel memory-augmented contrastive learning (CL) to jointly learn representations and memory modules across multiple scales. This allows us to effectively capture subtle features of normal data while adapting to varying levels of anomaly complexity.
Then, we train an efficient anomaly distance-based detector that computes spatial deviation maps between the learned prototypes and incoming observations.
Our model outperforms the state-of-the-art on a wide range of anomalies, including object, style, and local anomalies, as well as face presentation attacks. Notably, it stands as the first model capable of maintaining exceptional performance across both OC and OE settings.

## item_id: m_1577

TITLE: An Actor-critic Algorithm for Learning Rate Learning

ABSTRACT: Stochastic gradient descent (SGD), which updates the model parameters by adding a local gradient times a learning rate at each step, is widely used in model training of machine learning algorithms such as neural networks. It is observed that the models trained by SGD are sensitive to learning rates and good learning rates are problem specific. To avoid manually searching of learning rates, which is tedious and inefficient, we propose an algorithm to automatically learn learning rates using actor-critic methods from reinforcement learning (RL). In particular, we train a policy network called actor to decide the learning rate at each step during training, and a value network called critic to give feedback about quality of the decision (e.g., the goodness of the learning rate outputted by the actor) that the actor made. Experiments show that our method leads to good convergence of SGD and can prevent overfitting to a certain extent, resulting in better performance than human-designed competitors.

## item_id: m_1578

TITLE: Path Integral Sampler: A Stochastic Control Approach For Sampling

ABSTRACT: We present Path Integral Sampler~(PIS), a novel algorithm to draw samples from unnormalized probability density functions. The PIS is built on the Schr\"odinger bridge problem which aims to recover the most likely evolution of a diffusion process given its initial distribution and terminal distribution. The PIS draws samples from the initial distribution and then propagates the samples through the Schr\"odinger bridge to reach the terminal distribution. Applying the Girsanov theorem, with a simple prior diffusion, we formulate the PIS as a stochastic optimal control problem whose running cost is the control energy and terminal cost is chosen according to the target distribution. By modeling the control as a neural network, we establish a sampling algorithm that can be trained end-to-end. We provide theoretical justification of the sampling quality of PIS in terms of Wasserstein distance when sub-optimal control is used. Moreover, the path integrals theory is used to compute importance weights of the samples to compensate for the bias induced by the sub-optimality of the controller and the time-discretization. We experimentally demonstrate the advantages of PIS compared with other start-of-the-art sampling methods on a variety of tasks.

## item_id: m_1579

TITLE: AlphaZero-based Proof Cost Network to Aid Game Solving

ABSTRACT: The AlphaZero algorithm learns and plays games without hand-crafted expert knowledge. However, since its objective is to play well, we hypothesize that a better objective can be defined for the related but separate task of solving games. This paper proposes a novel approach to solving problems by modifying the training target of the AlphaZero algorithm, such that it prioritizes solving the game quickly, rather than winning. We train a Proof Cost Network (PCN), where proof cost is a heuristic that estimates the amount of work required to solve problems. This matches the general concept of the so-called proof number from proof number search, which has been shown to be well-suited for game solving. We propose two specific training targets. The first finds the shortest path to a solution, while the second estimates the proof cost. We conduct experiments on solving 15x15 Gomoku and 9x9 Killall-Go problems with both MCTS-based and FDFPN solvers. Comparisons between using AlphaZero networks and PCN as heuristics show that PCN can solve more problems.

## item_id: m_1580

TITLE: Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences

ABSTRACT: Reward models (RMs) play a critical role in aligning AI behaviors with human preferences, yet they face two fundamental challenges: (1) Modality Imbalance, where most RMs are mainly focused on text and image modalities, offering limited support for video, audio, and other modalities; and (2) Preference Rigidity, where training on fixed binary preference pairs fails to capture the complexity and diversity of personalized preferences. To address the above challenges, we propose Omni-Reward, a step toward generalist omni-modal reward modeling with support for free-form preferences, consisting of: (1) Evaluation: We introduce Omni-RewardBench, the first omni-modal RM benchmark with free-form preferences, covering nine tasks across five modalities including text, image, video, audio, and 3D; (2) Data: We construct Omni-RewardData, a multimodal preference dataset comprising 248K general preference pairs and 69K instruction-tuning pairs for training generalist omni-modal RMs; (3) Model: We propose Omni-RewardModel, which includes both discriminative and generative RMs, and achieves strong performance on Omni-RewardBench as well as other widely used reward modeling benchmarks.

## item_id: m_1581

TITLE: Pipelined Training with Stale Weights of Deep Convolutional Neural Networks

ABSTRACT: The growth in the complexity of Convolutional Neural Networks (CNNs) is increasing interest in partitioning a network across multiple accelerators during training and pipelining the backpropagation computations over the accelerators. Existing approaches avoid or limit the use of stale weights through techniques such as micro-batching or weight stashing. These techniques either underutilize of accelerators or increase memory footprint. We explore the impact of stale weights on the statistical efficiency and performance in a pipelined backpropagation scheme that maximizes accelerator utilization and keeps memory overhead modest. We use 4 CNNs (LeNet-5, AlexNet, VGG and ResNet) and show that when pipelining is limited to early layers in a network, training with stale weights converges and results in models with comparable inference accuracies to those resulting from non-pipelined training on MNIST and CIFAR-10 datasets; a drop in accuracy of 0.4%, 4%, 0.83% and 1.45% for the 4 networks, respectively. However, when pipelining is deeper in the network, inference accuracies drop significantly. We propose combining pipelined and non-pipelined training in a hybrid scheme to address this drop. We demonstrate the implementation and performance of our pipelined backpropagation in PyTorch on 2 GPUs using ResNet, achieving speedups of up to 1.8X over a 1-GPU baseline, with a small drop in inference accuracy.

## item_id: m_1582

TITLE: TAB-DRW: A DFT-based Robust Watermark for Generative Tabular Data

ABSTRACT: The rise of generative AI has enabled the production of high-fidelity synthetic tabular data across fields such as healthcare, finance, and public policy, raising growing concerns about data provenance and misuse. Watermarking offers a promising solution to address these concerns by ensuring the traceability of synthetic data, but existing methods face many limitations: they are computationally expensive due to reliance on large diffusion models, struggle with mixed discrete-continuous data, or lack robustness to post-modifications. To address them, we propose TAB-DRW, an efficient and robust post-editing watermarking scheme for generative tabular data. TAB-DRW embeds watermark signals in the frequency domain: it normalizes heterogeneous features via the Yeo–Johnson transformation and standardization, applies the discrete Fourier transform (DFT), and adjusts the imaginary parts of adaptively selected entries according to precomputed pseudorandom bits. To further enhance robustness and efficiency, we introduce a novel rank-based pseudorandom bit generation method that enables row-wise retrieval without incurring storage overhead. Experiments on five benchmark tabular datasets show that TAB-DRW achieves strong detectability and robustness against common post-processing attacks, while preserving high data fidelity and fully supporting mixed-type features.

## item_id: m_1583

TITLE: Modelling Hierarchical Structure between Dialogue Policy and Natural Language Generator with Option Framework for Task-oriented Dialogue System

ABSTRACT: Designing task-oriented dialogue systems is a challenging research topic, since it needs not only to generate utterances fulfilling user requests but also to guarantee the comprehensibility. Many previous works trained end-to-end (E2E) models with supervised learning (SL), however, the bias in annotated system utterances remains as a bottleneck. Reinforcement learning (RL) deals with the problem through using non-differentiable evaluation metrics (e.g., the success rate) as rewards. Nonetheless, existing works with RL showed that the comprehensibility of generated system utterances could be corrupted when improving the performance on fulfilling user requests. In our work, we (1) propose modelling the hierarchical structure between dialogue policy and natural language generator (NLG) with the option framework, called HDNO, where the latent dialogue act is applied to avoid designing specific dialogue act representations; (2) train HDNO via hierarchical reinforcement learning (HRL), as well as suggest the asynchronous updates between dialogue policy and NLG during training to theoretically guarantee their convergence to a local maximizer; and (3) propose using a discriminator modelled with language models as an additional reward to further improve the comprehensibility. We test HDNO on MultiWoz 2.0 and MultiWoz 2.1, the datasets on multi-domain dialogues, in comparison with word-level E2E model trained with RL, LaRL and HDSA, showing improvements on the performance evaluated by automatic evaluation metrics and human evaluation. Finally, we demonstrate the semantic meanings of latent dialogue acts to show the explanability for HDNO.

## item_id: m_1584

TITLE: Empirical Study on Enhancing Efficiency in Masked Image Modeling Pre-training

ABSTRACT: The combination of transformers and masked image modeling (MIM) pre-training framework has shown remarkable potential in various vision tasks. However, the high computational cost of pre-training hinders the practical application of MIM.
   This paper introduces \emph{FastMIM}, a simple and versatile framework that expedites masked image modeling through two steps: (i) pre-training vision backbones using low-resolution input images and (ii) reconstructing Histograms of Oriented Gradients (HOG) feature instead of original RGB values of the input images.
   Furthermore, we propose \emph{FastMIM-P}, which progressively increases the input resolution during the pre-training stage to improve the transfer learning performance of models with high capacity. We point out that: (i) a wide range of input resolutions during pre-training can result in similar performances in fine-tuning and downstream tasks such as detection and segmentation; (ii) the shallow layers of encoder are more important during pre-training, and discarding the last few layers can speed up the training process without affecting fine-tuning performance; and (iii) HOG is more stable than RGB values when transferring resolution. Equipped with \emph{FastMIM}, any type of vision backbone can be efficiently pre-trained. For example, using ViT-B/Swin-B as backbones, we achieve 83.8\%/84.1\% top-1 accuracy on ImageNet-1K. Compared to previous approaches, our method can achieve better top-1 accuracy while accelerating the training procedure by 5×.

## item_id: m_1585

TITLE: Image Authenticity Detection using Eye Gazing Data:  A Performance Comparison Beyond Human Capabilities  via Attention Mechanism, ResNet, and Cascade  Strategies

ABSTRACT: In the digital age, determining the authenticity of images has become 
increasingly crucial. This study aims to explore the capability of machine 
learning models in identifying manipulated images using eye movement data and 
compares this with human judgment. We collected a series of both manipulated 
and unaltered images and conducted eye-tracking experiments on a set of 
participants. After data preprocessing, various machine learning models were 
trained and validated, including a simple classifier, cascade-optimized classifier, 
and models integrating attention mechanisms with ResNet architectures. Results 
indicate that all models outperformed the baseline set by human judgment. 
Specifically, the Attention-ResNet model achieved the highest accuracy at 0.685, 
making it the top-performing model. Our analysis delves further into the stability, 
generalization capabilities, and practical value of these models. Ultimately, this 
research underscores the immense potential of deep learning strategies in 
verifying image authenticity, providing valuable insights for future research and 
applications.

## item_id: m_1586

TITLE: Squeezing SGD Parallelization Performance in Distributed Training Using Delayed Averaging

ABSTRACT: State-of-the-art deep learning algorithms rely on distributed training to tackle the increasing model size and training data. Mini-batch Stochastic Gradient Descent (SGD) requires workers to halt forward/backward propagations, to wait for gradients synchronized among all workers before the next batch of tasks.  The synchronous execution model exposes the overhead of gradient communication among a large number of workers in a distributed training system.

To this end, we propose a new SGD algorithm with delayed averaging, namely DaSGD, which can fully parallelize SGD and forward/backward propagations to hide 100\% of gradient communication. By adjusting the gradient update scheme, this algorithm uses hardware resources more efficiently and reduces the reliance on high-throughput inter-connects. The theoretical analysis and experimental results conducted in this paper both show its convergence rate of $ O (1 / \sqrt {K} )$ stays the same as Mini-batch SGD. A analytical model shows that it enables linear performance scalability with the cluster size.

## item_id: m_1587

TITLE: Understanding trained CNNs by indexing neuron selectivity

ABSTRACT: The impressive performance and plasticity of convolutional neural networks to solve different vision problems are shadowed by their black-box nature and its consequent lack of full understanding. To reduce this gap we propose to describe the activity of individual neurons by quantifiyng their inherent selectivity to specific properties. Our approach is based on the definition of feature selectivity indexes that allow the ranking of neurons according to specific properties. Here we report the results of exploring selectivity indexes for: (a) an image feature (color); and (b) an image label (class membership). Our contribution is a framework to seek or classify neurons by indexing on these selectivity properties. It helps to find color selective neurons, such as a red-mushroom neuron in layer conv4 or class selective neurons such as dog-face neurons in layer conv5, and establishes a methodology to derive other selectivity properties.  Indexing on neuron selectivity can statistically draw how features and classes are represented through layers at a moment when the size of trained nets is growing and automatic tools to index can be helpful. 

## item_id: m_1588

TITLE: Actor-Critic Alignment for Offline-to-Online Reinforcement Learning

ABSTRACT: Deep offline reinforcement learning has recently demonstrated considerable promise in leveraging offline datasets, providing high-quality models that significantly reduce the online interactions required for fine-tuning. However, such a benefit is often diminished due to the marked state-action distribution shift, which causes significant bootstrap error and wipes out the good initial policy. Existing solutions resort to constraining the policy shift or balancing the sample replay based on their online-ness. However, they require online estimation of distribution divergence or density ratio. To avoid such complications, we propose deviating from existing actor-critic approaches that directly transfer the state-action value functions. Instead, we post-process them by aligning with the offline learned policy, so that the Q-values for actions *outside* the offline policy are also tamed. As a result, the online fine-tuning can be simply performed as in the standard actor-critic algorithms. We show empirically that the proposed method improves the performance of the fine-tuned robotic agents on various simulated tasks.

## item_id: m_1589

TITLE: Contrastive Corpus Attribution for Explaining Representations

ABSTRACT: Despite the widespread use of unsupervised models, very few methods are designed to explain them. Most explanation methods explain a scalar model output. However, unsupervised models output representation vectors, the elements of which are not good candidates to explain because they lack semantic meaning. To bridge this gap, recent works defined a scalar explanation output: a dot product-based similarity in the representation space to the sample being explained (i.e., an explicand). Although this enabled explanations of unsupervised models, the interpretation of this approach can still be opaque because similarity to the explicand's representation may not be meaningful to humans. To address this, we propose contrastive corpus similarity, a novel and semantically meaningful scalar explanation output based on a reference corpus and a contrasting foil set of samples. We demonstrate that contrastive corpus similarity is compatible with many post-hoc feature attribution methods to generate COntrastive COrpus Attributions (COCOA) and quantitatively verify that features important to the corpus are identified. We showcase the utility of COCOA in two ways: (i) we draw insights by explaining augmentations of the same image in a contrastive learning setting (SimCLR); and (ii) we perform zero-shot object localization by explaining the similarity of image representations to jointly learned text representations (CLIP).

## item_id: m_1590

TITLE: Thresholded Lexicographic Ordered Multi-Objective Reinforcement Learning

ABSTRACT: Lexicographic multi-objective problems, which impose  a  lexicographic importance order over the objectives, arise in many real-life scenarios. Existing Reinforcement Learning work  directly addressing lexicographic tasks has been scarce. The few proposed approaches were all noted to be heuristics without theoretical guarantees as the Bellman equation is not applicable to them. Additionally, the practical applicability of these prior approaches also  suffers from various issues such as not being able to reach the goal state.  While some of these issues have been known before, in this work we investigate further shortcomings, and propose fixes for improving practical performance in many cases. We also present a  policy optimization approach using our Lexicographic Projection Optimization (LPO) algorithm that has the potential to address these theoretical and practical concerns. Finally, we demonstrate our proposed algorithms on benchmark problems.

## item_id: m_1591

TITLE: Efficient Sampling for Generative Adversarial Networks with Reparameterized Markov Chains

ABSTRACT: Recently, sampling methods have been successfully applied to enhance the sample quality of Generative Adversarial Networks (GANs). However, in practice, they typically have poor sample efficiency because of the independent proposal sampling from the generator. In this work, we propose REP-GAN, a novel sampling method that allows general dependent proposals by REParameterizing the Markov chains into the latent space of the generator. Theoretically, we show that our reparameterized proposal admits a closed-form Metropolis-Hastings acceptance ratio. Empirically, extensive experiments on synthetic and real datasets demonstrate that our REP-GAN largely improves the sample efficiency and obtains better sample quality simultaneously.

## item_id: m_1592

TITLE: Efficient High-Dimensional Data Representation Learning via Semi-Stochastic Block Coordinate Descent Methods

ABSTRACT: With the increase of data volume and data dimension, sparse representation learning attracts more and more attention. For high-dimensional data, randomized block coordinate descent methods perform well because they do not need to calculate the gradient along the whole dimension. Existing hard thresholding algorithms evaluate gradients followed by a hard thresholding operation to update the model parameter, which leads to slow convergence. To address this issue, we propose a novel hard thresholding algorithm, called Semi-stochastic Block Coordinate Descent Hard Thresholding Pursuit (SBCD-HTP). Moreover, we present its sparse and asynchronous parallel variants. We theoretically analyze the convergence properties of our algorithms, which show that they have a significantly lower hard thresholding complexity than existing algorithms. Our empirical evaluations on real-world datasets and face recognition tasks demonstrate the superior performance of our algorithms for sparsity-constrained optimization problems.

## item_id: m_1593

TITLE: Fourier Sliced-Wasserstein Embedding for Multisets and Measures

ABSTRACT: We present the _Fourier Sliced-Wasserstein (FSW) embedding_—a novel method to embed multisets and measures over $\mathbb{R}^d$ into Euclidean space.

Our proposed embedding approximately preserves the sliced Wasserstein distance on distributions, thereby yielding geometrically meaningful representations that better capture the structure of the input. Moreover, it is injective on measures and _bi-Lipschitz_ on multisets—a significant advantage over prevalent methods based on sum- or max-pooling, which are provably not bi-Lipschitz, and, in many cases, not even injective.
The required output dimension for these guarantees is near-optimal: roughly $2 N d$, where $N$ is the maximal input multiset size.

Furthermore, we prove that it is _impossible_ to embed distributions over $\mathbb{R}^d$ into Euclidean space in a bi-Lipschitz manner. Thus, the metric properties of our embedding are, in a sense, the best possible.

Through numerical experiments, we demonstrate that our method yields superior multiset representations that improve performance in practical learning tasks. Specifically, we show that (a) a simple combination of the FSW embedding with an MLP achieves state-of-the-art performance in learning the (non-sliced) Wasserstein distance; and (b) replacing max-pooling with the FSW embedding makes PointNet significantly more robust to parameter reduction, with only minor performance degradation even after a 40-fold reduction.

## item_id: m_1594

TITLE: MANTA: Cross-Modal Semantic Alignment and Information-Theoretic Optimization for Long-form Multimodal Understanding

ABSTRACT: The fundamental challenge in multimodal understanding lies not merely in processing individual modalities, but in discovering optimal strategies for their semantic unification across vastly different representational spaces; current approaches maintain separate encoders for each modality, leading to semantic fragmentation and computational inefficiency, and we present MANTA (Multimodal Abstraction and Normalization via Textual Alignment), a theoretically grounded framework that reconceptualizes multimodal integration as an information-theoretic optimization problem with provable guarantees, showing that natural language serves as a universal semantic bridge and providing three theoretical contributions—(1) hierarchical linguistic projection achieves (1−ϵ)-optimal information preservation, (2) cross-modal contrastive alignment converges to maximal mutual information with rate O(1/√T), and (3) our retrieval mechanism achieves the best trade-off between relevance and diversity—while guiding practical algorithms for multi-scale representation learning, information-theoretic content selection, cross-modal semantic alignment, and retrieval-augmented generation, validated by extensive experiments on long-form video understanding with unprecedented gains (22.6% on Video-MME, 27.3% on videos over 30 minutes, 25.1% on cross-modal reasoning), establishing new theoretical foundations for linguistic abstraction as a unifying principle for multimodal AI with implications for robotics, embodied AI, and human-computer interaction.

## item_id: m_1595

TITLE: Gaitor: Learning a Unified Representation for Continuous Gait Transition and Terrain Traversal for Quadruped Robots

ABSTRACT: The current state-of-the-art in quadruped locomotion is able to produce robust motion for terrain traversal but requires the segmentation of a desired trajectory into a discrete set of skills such as trot, crawl and pace. This misses the opportunity to leverage commonalities between individual gait types for efficient learning and are unable to smoothly transition between them. Here we present Gaitor, which creates a learnt representation capturing correlations across multiple distinct gait types resulting in the discovery of smooth transitions between motions. In particular, this representation is compact meaning that information common to all gait types is shared. The emerging structure is interpretable in that it encodes phase correlations between the different gait types which can be leveraged to produce smooth gait transitions. In addition, foot swing characteristics are disentangled and directly addressable. Together with a rudimentary terrain encoding and a learned planner operating in this structured latent representation, Gaitor is able to take motion commands including gait type and characteristics from a user while reacting to uneven terrain. We evaluate Gaitor in both simulated and real-world settings, such as climbing over raised platforms, on an ANYmal C platform. To the best of our knowledge, this is the first work learning an interpretable unified-latent representation for multiple gaits, resulting in smooth and natural looking gait transitions between trot and crawl on a real quadruped robot.

## item_id: m_1596

TITLE: Beyond adversarial examples: sampling and repairing diverse failures with RADIUM

ABSTRACT: Recent years have seen large numbers of learning-enabled autonomous systems deployed in the real world. Unfortunately, increased deployment has seen a corresponding increase in accidents involving these systems. We must be able to predict the ways in which these systems might fail and take steps to prevent those failures \textit{before} deployment. Existing tools for failure prediction struggle to search over high-dimensional environmental parameters and provide little guidance on how to mitigate failures once they are discovered. In this paper, we develop a novel framework to efficiently predict failures and propose policy parameter updates to mitigate those failures. By re-framing adversarial optimization as a sequential inference problem, our approach is able to generate a more diverse set of challenging failures, which in turn lead to more robust repaired policies. We propose both gradient-free and gradient-based approaches to solving this inference problem, achieving state-of-the-art performance for policy repair, and we include a theoretical and empirical evaluation of the trade-offs between the two.

## item_id: m_1597

TITLE: Hierarchical Approach to Explaining Poisoned AI Models

ABSTRACT: This work presents a hierarchical approach to explaining poisoned artificial intelligence (AI) models. The motivation comes from the use of AI models in security and safety critical applications, for instance, the use of AI models for classification of road traffic signs in self-driving cars. Training images of traffic signs can be poisoned by adversaries to encode malicious triggers that change trained AI model prediction from a correct traffic sign to another traffic sign in a presence of such a physically realizable trigger (e.g., sticky note or Instagram filter).
We address the lack of AI model explainability by (a) designing utilization measurements of trained AI models and (b) explaining how training data are encoded in AI models based on those measurements at three hierarchical levels. The three levels are defined at graph node (computation unit), subgraph, and graph representations of  poisoned and clean AI models from the TrojAI Challenge.

## item_id: m_1598

TITLE: On Weight-Sharing and Bilevel Optimization in Architecture Search

ABSTRACT: Weight-sharing—the simultaneous optimization of multiple neural networks using the same parameters—has emerged as a key component of state-of-the-art neural architecture search. However, its success is poorly understood and often found to be surprising. We argue that, rather than just being an optimization trick, the weight-sharing approach is induced by the relaxation of a structured hypothesis space, and introduces new algorithmic and theoretical challenges as well as applications beyond neural architecture search. Algorithmically, we show how the geometry of ERM for weight-sharing requires greater care when designing gradient- based minimization methods and apply tools from non-convex non-Euclidean optimization to give general-purpose algorithms that adapt to the underlying structure. We further analyze the learning-theoretic behavior of the bilevel optimization solved by practical weight-sharing methods. Next, using kernel configuration and NLP feature selection as case studies, we demonstrate how weight-sharing applies to the architecture search generalization of NAS and effectively optimizes the resulting bilevel objective. Finally, we use our optimization analysis to develop a simple exponentiated gradient method for NAS that aligns with the underlying optimization geometry and matches state-of-the-art approaches on CIFAR-10.

## item_id: m_1599

TITLE: Rethinking Heavy Models in Multivariate Time Series Anomaly Detection

ABSTRACT: Multivariate time series anomaly detection (MTS-AD) is widely used, but real-world deployments often face tight computational budgets that limit the practicality of deep learning. We revisit whether heavy deep models (high-FLOPs architectures) are necessary to achieve strong detection performance in such settings. We conduct a systematic, compute-aware comparison of statistical, classical machine learning, and deep learning methods across diverse MTS-AD benchmarks, measuring detection with AUROC (threshold-free, thus application-agnostic) and cost with FLOPs (a hardware-agnostic proxy enabling fair cross-method comparison). We find that traditional approaches often match or surpass deep models, which appear less frequently among the top performers, and that the effectiveness-efficiency trade-off commonly favors non-deep alternatives under limited budgets. These results indicate that deep learning is not uniformly superior for MTS-AD and that heavy architectures can be counterproductive in resource-constrained deployments. These findings offer practical guidance for practitioners designing anomaly monitoring systems under compute constraints, highlighting cases where lightweight models are sufficient and heavy deep models may be worth the cost.

## item_id: m_1600

TITLE: Language Models as Semantic Indexers

ABSTRACT: Semantic identifier (ID) is an important concept in information retrieval that aims to preserve the semantics of objects such as documents and items inside their IDs. Previous studies typically adopt a two-stage pipeline to learn semantic IDs by first procuring embeddings using off-the-shelf text encoders and then deriving IDs based on the embeddings. However, each step introduces potential information loss and there is usually an inherent mismatch between the distribution of embeddings within the latent space produced by text encoders and the anticipated distribution required for semantic indexing. Nevertheless, it is non-trivial to design a method that can learn the document’s semantic representations and its hierarchical structure simultaneously, given that semantic IDs are discrete and sequentially structured, and the semantic supervision is deficient. In this paper, we introduce LMINDEXER, a self-supervised framework to learn semantic IDs with a generative language model. We tackle the challenge of sequential discrete ID by introducing a semantic indexer capable of generating neural sequential discrete representations with progressive training and contrastive learning. In response to the semantic supervision deficiency, we propose to train the model with a self-supervised document reconstruction objective. The learned semantic indexer can facilitate various downstream tasks, such as recommendation and retrieval. We conduct experiments on three tasks including recommendation, product search, and document retrieval on five datasets from various domains, where LMINDEXER outperforms competitive baselines significantly and consistently. Code is available at https://anonymous.4open.science/r/ICLR24-submit-B2E7/.
