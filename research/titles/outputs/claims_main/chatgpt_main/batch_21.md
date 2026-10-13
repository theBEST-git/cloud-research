# Batch 21 — 100 items

## item_id: m_2001

TITLE: Wavelet-Guided Attention Network for Spiking Image Reconstruction

ABSTRACT: Reconstructing high-quality images from spike data remains a challenging task, particularly under low-light and high-motion conditions where spike noise and motion blur are prominent. To tackle these challenges, we propose WaveAttNet, a novel Wavelet-Guided Attention Network for spiking image reconstruction. WaveAttNet comprises two ky components: (1) a Wavelet-Guided Attention (WGA) module that performs frequency-aware noise suppression by emphasizing informative subbands and suppressing noisy ones through discrete wavelet transform and attention weighting; and (2) a Multi-scale Temporal Attention (MTA) module that captures and fuses temporal features across multiple time scales to mitigate both short-exposure noise and long-exposure motion blur. Extensive experiments on both synthetic (Spike-REDS) and real-world (Real-Captured) spike datasets demonstrate that WaveAttNet outperforms state-of-the-art approaches in terms of perceptual quality and quantitative metrics.

## item_id: m_2002

TITLE: Dual Averaging is Surprisingly Effective for Deep Learning Optimization

ABSTRACT: First-order stochastic optimization methods are currently the most widely used class of methods for training deep neural networks. However, the choice of the optimizer has become an ad-hoc rule that can significantly affect the performance. For instance, SGD with momentum (SGD+M) is typically used in computer vision (CV) and Adam is used for training transformer models for Natural Language Processing (NLP). Using the wrong method can lead to significant performance degradation. Inspired by the dual averaging algorithm, we propose Modernized Dual Averaging (MDA), an optimizer that is able to perform as well as SGD+M in CV and as Adam in NLP. Our method is not adaptive and is significantly simpler than Adam. We show that MDA induces a decaying uncentered L 2 -regularization compared to vanilla SGD+M and hypothesize that this may explain why it works on NLP problems where SGD+M fails.

## item_id: m_2003

TITLE: Representation Stability as a Regularizer for Improved Text Analytics Transfer Learning

ABSTRACT: Although neural networks are well suited for sequential transfer learning tasks, the catastrophic forgetting problem hinders proper integration of prior knowledge. In this work, we propose a solution to this problem by using a multi-task objective based on the idea of distillation and a mechanism that directly penalizes forgetting at the shared representation layer during the knowledge integration phase of training. We demonstrate our approach on a Twitter domain sentiment analysis task with sequential knowledge transfer from four related tasks.  We show that our technique outperforms networks fine-tuned to the target task. Additionally, we show both through empirical evidence and examples that it does not forget useful knowledge from the source task that is forgotten during standard fine-tuning. Surprisingly, we find that first distilling a human made rule based sentiment engine into a recurrent neural network and then integrating the knowledge with the target task data leads to a substantial gain in generalization performance. Our experiments demonstrate the power of multi-source transfer techniques in practical text analytics problems when paired with distillation. In particular, for the SemEval 2016 Task 4 Subtask A (Nakov et al., 2016) dataset we surpass the state of the art established during the competition with a comparatively simple model architecture that is not even competitive when trained on only the labeled task specific data.

## item_id: m_2004

TITLE: Convolutions Through the Lens of Tensor Networks

ABSTRACT: Despite their simple intuition, convolutions are more tedious to analyze than dense layers, which complicates the transfer of theoretical and algorithmic ideas. We provide a simplifying perspective onto convolutions through tensor networks (TNs) which allow reasoning about the underlying tensor multiplications by drawing diagrams, and manipulating them to perform function transformations and sub-tensor access. We demonstrate this expressive power by deriving the diagrams of various autodiff operations and popular approximations of second-order information with full hyper-parameter support, batching, channel groups, and generalization to arbitrary convolution dimensions. Further, we provide convolution-specific transformations based on the connectivity pattern which allow to re-wire and simplify diagrams before evaluation. Finally, we probe computational performance, relying on established machinery for efficient TN contraction. Our TN implementation speeds up a recently-proposed KFAC variant up to 4.5x and enables new hardware-efficient tensor dropout for approximate backpropagation.

## item_id: m_2005

TITLE: Long Term Memory Network for Combinatorial Optimization Problems

ABSTRACT: This paper introduces a framework for solving combinatorial optimization problems by learning from input-output examples of optimization problems. We introduce a new memory augmented neural model in which the memory is not resettable (i.e the information stored in the memory after processing an input example is kept for the next seen examples). We used deep reinforcement learning to train a memory controller agent to store useful memories. Our model was able to outperform hand-crafted solver on Binary Linear Programming (Binary LP). The proposed model is tested on different Binary LP instances with large number of variables (up to 1000 variables) and constrains (up to 700 constrains).

## item_id: m_2006

TITLE: Neural Arithmetic Units

ABSTRACT: Neural networks can approximate complex functions, but they struggle to perform exact arithmetic operations over real numbers. The lack of inductive bias for arithmetic operations leaves neural networks without the underlying logic necessary to extrapolate on tasks such as addition, subtraction, and multiplication. We present two new neural network components: the Neural Addition Unit (NAU), which can learn exact addition and subtraction; and the Neural Multiplication Unit (NMU) that can multiply subsets of a vector. The NMU is, to our knowledge, the first arithmetic neural network component that can learn to multiply elements from a vector, when the hidden size is large. The two new components draw inspiration from a theoretical analysis of recently proposed arithmetic components. We find that careful initialization, restricting parameter space, and regularizing for sparsity is important when optimizing the NAU and NMU. Our proposed units NAU and NMU, compared with previous neural units, converge more consistently, have fewer parameters, learn faster, can converge for larger hidden sizes, obtain sparse and meaningful weights, and can extrapolate to negative and small values.

## item_id: m_2007

TITLE: Towards Efficient Posterior Sampling in Deep Neural Networks via Symmetry Removal

ABSTRACT: Bayesian inference in deep neural networks is challenging due to the high-dimensional, strongly multi-modal posterior landscape. Markov Chain Monte Carlo approaches asymptotically recover the true, intractable posterior but are prohibitively expensive for large modern architectures. Local posterior approximations, while often yielding satisfactory results in practice, crudely disregard the posterior geometry. We propose to exploit well-known parameter symmetries induced by neuron interchangeability and output activation to retrieve a drastically reduced -- yet exact -- posterior over uniquely identified parametrizations. To this end, we provide an algorithm for explicit symmetry removal and develop an upper bound on Monte Carlo samples required to capture the reduced posterior. Our experiments suggest that efficient sampling from the functionally relevant part of the posterior is indeed possible, opening up a promising path to faithful uncertainty quantification in deep learning.

## item_id: m_2008

TITLE: GQ-Net: Training Quantization-Friendly Deep Networks

ABSTRACT: Network quantization is a model compression and acceleration technique that has become essential to neural network deployment. Most quantization methods per- form fine-tuning on a pretrained network, but this sometimes results in a large loss in accuracy compared to the original network. We introduce a new technique to train quantization-friendly networks, which can be directly converted to an accurate quantized network without the need for additional fine-tuning. Our technique allows quantizing the weights and activations of all network layers down to 4 bits, achieving high efficiency and facilitating deployment in practical settings. Com- pared to other fully quantized networks operating at 4 bits, we show substantial improvements in accuracy, for example 66.68% top-1 accuracy on ImageNet using ResNet-18, compared to the previous state-of-the-art accuracy of 61.52% Louizos et al. (2019) and a full precision reference accuracy of 69.76%. We performed a thorough set of experiments to test the efficacy of our method and also conducted ablation studies on different aspects of the method and techniques to improve training stability and accuracy. Our codebase and trained models are available on GitHub.

## item_id: m_2009

TITLE: k-Nearest Neighbors by Means of Sequence to Sequence Deep Neural Networks and Memory Networks

ABSTRACT: k-Nearest Neighbors is one of the most fundamental but effective classification models. In this paper, we propose two families of models built on a sequence to sequence model and a memory network model to mimic the k-Nearest Neighbors model, which generate a sequence of labels, a sequence of out-of-sample feature vectors and a final label for classification, and thus they could also function as oversamplers. We also propose `out-of-core' versions of our models which assume that only a small portion of data can be loaded into memory. Computational experiments show that our models outperform k-Nearest Neighbors, a feed-forward neural network and a memory network, due to the fact that our models must produce additional output and not just the label. As an oversampler on imbalanced datasets, the sequence to sequence kNN model often outperforms Synthetic Minority Over-sampling Technique and Adaptive Synthetic Sampling.


## item_id: m_2010

TITLE: It's All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization

ABSTRACT: Designing efficient and effective architectural backbones has been in the core of research efforts to enhance the capability of foundation models. Inspired by the human cognitive phenomenon of attentional bias—the natural tendency to prioritize certain events or stimuli—we reconceptualize neural architectures, including Transformers, Titans, and modern linear recurrent neural networks as associative memory modules with attentional bias. We define and formalize the concept of attentional bias as the internal memory objective deep learning architectures. We show that existing deep learning architectures leverage the same attentional bias based on $L_2$ loss function. Going beyond $L_2$ loss function, we present a set of alternative attentional bias configurations along with their effective approximations. We then reinterpret forgetting mechanisms in modern deep learning architectures as a form of retention regularization. Building upon these insights, we present Miras, a general framework to design deep learning architectures based on the choice of attentional bias objective, retention gate, associative memory architecture, and memory learning algorithm. Our experiments show different designs yield models with varying strengths. Furthermore, our special instances of Miras achieve exceptional performance in language modeling, commonsense reasoning, recall intensive, and time series tasks, outperforming Transformers and other modern linear recurrent models.

## item_id: m_2011

TITLE: Human Gaze is All You Need: Aligning Image Encoders with Human Attention

ABSTRACT: Replicating human-like perception in artificial systems requires capturing the attentional biases that shape human interpretation of visual scenes. While modern Vision-Language Models (VLMs) demonstrate strong multimodal reasoning, they often lack the behavioral priors that guide human attention. We address this gap with a framework that integrates human gaze patterns into the visual encoder of a state-of-the-art VLM. Aggregated attention heatmaps—collected from 29 participants in a visual description task—are incorporated via a cross-attention mechanism that refines the encoder’s latent space to prioritize human-salient regions. Aligning model attention with human gaze yields consistent improvements in both human-likeness and semantic accuracy of image descriptions. **METEOR** and **Cosine Similarity** increase by *29.6%* and *4.6%*, respectively. Our contributions are threefold: a lightweight, plug-in **architectural modification of VLM** for integrating behavioral priors without full model retraining; empirical evidence of **enhanced alignment** with human perception, especially in scenes with strong bottom-up saliency cues; and a **novel dataset** of 778 image–heatmap–caption triples to facilitate research on attention-conditioned generation. This work demonstrates that incorporating behavioral priors systematically enhances VLMs and contributes to the development of more human-aligned interpretative capabilities for social cognition and human–AI interaction.

## item_id: m_2012

TITLE: Prospect Pruning: Finding Trainable Weights at Initialization using Meta-Gradients

ABSTRACT: Pruning neural networks at initialization would enable us to find sparse models that retain the accuracy of the original network while consuming fewer computational resources for training and inference. However, current methods are insufficient to enable this optimization and lead to a large degradation in model performance. In this paper, we identify a fundamental limitation in the formulation of current methods, namely that their saliency criteria look at a single step at the start of training without taking into account the trainability of the network. While pruning iteratively and gradually has been shown to improve pruning performance, explicit consideration of the training stage that will immediately follow pruning has so far been absent from the computation of the saliency criterion. To overcome the short-sightedness of existing methods, we propose Prospect Pruning (ProsPr), which uses meta-gradients through the first few steps of optimization to determine which weights to prune. ProsPr combines an estimate of the higher-order effects of pruning on the loss and the optimization trajectory to identify the trainable sub-network. Our method achieves state-of-the-art pruning performance on a variety of vision classification tasks, with less data and in a single shot compared to existing pruning-at-initialization methods.

## item_id: m_2013

TITLE: FEVERLESS: Fast and Secure Vertical Federated Learning based on XGBoost for Decentralized Labels

ABSTRACT: Vertical Federated Learning (VFL) enables multiple clients to collaboratively train a global model over vertically partitioned data without revealing private local information. Tree-based models, like XGBoost and LightGBM, have been widely used in VFL to enhance the interpretation and efficiency of training. However, there is a fundamental lack of research on how to conduct VFL securely over distributed labels. This work is the first to fill this gap by designing a novel protocol, called FEVERLESS, based on XGBoost. FEVERLESS leverages secure aggregation via information masking technique and global differential privacy provided by a fairly and randomly selected noise leader to prevent private information from being leaked in the training process. Furthermore, it provides label and data privacy against honest-but-curious adversary even in the case of collusion of $n-2$ out of $n$ clients. We present a comprehensive security and efficiency analysis for our design, and the empirical experiment results demonstrate that FEVERLESS is fast and secure. In particular, it outperforms the solution based on additive homomorphic encryption in runtime cost and provides better accuracy than the local differential privacy approach.

## item_id: m_2014

TITLE: MDFL: A UNIFIED FRAMEWORK WITH META-DROPOUT FOR FEW-SHOT LEARNING

ABSTRACT: Conventional training of deep neural networks usually requires a substantial amount of data with expensive human annotations. In this paper, we utilize the idea of meta-learning to integrate two very different streams of few-shot learning, i.e., the episodic meta-learning-based and pre-train finetune-based few-shot learning, and form a unified meta-learning framework. In order to improve the generalization power of our framework, we propose a simple yet effective strategy named meta-dropout, which is applied to the transferable knowledge generalized from base categories to novel categories. The proposed strategy can effectively prevent neural units from co-adapting excessively in the meta-training stage. Extensive experiments on the few-shot object detection and few-shot image classification datasets, i.e., Pascal VOC, MS COCO, CUB, and mini-ImageNet, validate the effectiveness of our method.


## item_id: m_2015

TITLE: The Variational Bandwidth Bottleneck: Stochastic Evaluation on an Information Budget

ABSTRACT: In many applications, it is desirable to extract only the relevant information from complex input data, which involves making a decision about which input features are relevant.
The information bottleneck method formalizes this as an information-theoretic optimization problem by maintaining an optimal tradeoff between compression (throwing away irrelevant input information), and predicting the target. In many problem settings, including the reinforcement learning problems we consider in this work, we might prefer to compress only part of the input. This is typically the case when we have a standard conditioning input, such as a state observation, and a ``privileged'' input, which might correspond to the goal of a task, the output of a costly planning algorithm, or communication with another agent. In such cases, we might prefer to compress the privileged input, either to achieve better generalization (e.g., with respect to goals) or to minimize access to costly information (e.g., in the case of communication). Practical implementations of the information bottleneck based on variational inference require access to the privileged input in order to compute the bottleneck variable, so although they perform compression, this compression operation itself needs unrestricted, lossless access. In this work, we propose the variational bandwidth bottleneck, which decides for each example on the estimated value of the privileged information before seeing it, i.e., only based on the standard input, and then accordingly chooses stochastically, whether to access the privileged input or not. We formulate a tractable approximation to this framework and demonstrate in a series of reinforcement learning experiments that it can improve generalization and reduce access to computationally costly information.

## item_id: m_2016

TITLE: On the Convergence Direction of Gradient Descent

ABSTRACT: Gradient descent (GD) is a fundamental optimization method in deep learning, yet its asymptotic directional properties remain less understood. In this paper, we prove that if GD converges, its trajectory either aligns toward a fixed direction or oscillates along a specific line. The fixed-direction convergence occurs under small learning rates, while the oscillatory convergence behavior emerges for large learning rates. This result offers a new lens for understanding long-term GD dynamics. Experimentally, we find that this directional convergence behavior also appears in stochastic gradient descent (SGD) and Adam. Furthermore, we discuss how these theoretical findings regarding oscillatory convergence might offer a perspective on the sharpness dynamics observed in the Edge of Stability (EoS) regime. Our work provides both theoretical clarity and practical insight into the behavior of dynamics for multiple optimization methods.

## item_id: m_2017

TITLE: UltraHorizon: Benchmarking LLM-Agent Capabilities in Ultra Long-Horizon Scenarios

ABSTRACT: Autonomous agents have recently achieved remarkable progress across diverse domains, yet most evaluations focus on short-horizon, fully observable tasks. In contrast, many critical real-world tasks, such as large-scale software development, commercial investment, and scientific discovery, unfold in long-horizon and partially observable scenarios where success hinges on sustained reasoning, planning, memory management, and tool use. Existing benchmarks rarely capture these long-horizon challenges, leaving a gap in systematic evaluation. To bridge this gap, we introduce $\textbf{UltraHorizon}$, a novel benchmark that measures the foundational capabilities essential for complex real-world challenges. We use exploration as a unifying task across three distinct environments to validate these core competencies. Agents are designed in long-horizon discovery tasks where they must iteratively uncover hidden rules through sustained reasoning, planning, memory and tools management, and interaction with environments. Under the heaviest scale setting, trajectories average $\textbf{200k+}$ tokens and $\textbf{400+}$ tool calls, whereas in standard configurations they still exceed $\textbf{35k}$ tokens and involve more than $\textbf{60}$ tool calls on average. Our extensive experiments reveal that agents powered by state-of-the-art LLMs consistently underperform in these settings, whereas human participants achieve much higher scores, underscoring a persistent gap in agents' long-horizon exploration abilities. We also observe that simple scaling fails in our task. To better illustrate the failure of agents, we conduct an in-depth analysis of collected trajectories. We identify eight types of errors and attribute them to two primary causes: in-context locking and functional fundamental capability gaps.

## item_id: m_2018

TITLE: Reconstruction for Generation: Regularizing Motion Diffusion Models with Motion Reconstruction

ABSTRACT: Diffusion models have seen widespread adoption for text-driven human motion generation and related tasks due to their impressive generative capabilities and flexibility. However, current motion diffusion models face two major limitations: a representational gap caused by pre-trained text encoders that lack motion-specific information, and error accumulation during the iterative denoising process. This paper introduces MOtion Reconstruction for GENeration (MORGEN) to address these challenges. First, MORGEN leverages a motion latent space as intermediate supervision for text-to-motion generation. To this end, MORGEN co-trains a motion reconstruction branch with two key objective functions: self-regularization to enhance the discrimination of the motion space and motion-centric latent alignment to enable accurate mapping from text to the motion latent space. Second, we propose Reconstructive Error Guidance (REG), a testing-stage guidance mechanism that exploits the diffusion model's inherent self-correction ability to mitigate error accumulation. At each denoising step, REG uses the motion reconstruction branch to reconstruct the previous estimate, reproducing the prior error patterns. By amplifying the residual between the current prediction and the reconstructed estimate, REG highlights the improvements in the current prediction. Extensive experiments demonstrate that MORGEN achieves significant improvements and state-of-the-art performance. Our code will be released.

## item_id: m_2019

TITLE: Alleviating Exposure Bias in Diffusion Models through Sampling with Shifted Time Steps

ABSTRACT: Diffusion Probabilistic Models (DPM) have shown remarkable efficacy in the synthesis of high-quality images. However, their inference process characteristically requires numerous, potentially hundreds, of iterative steps, which could exaggerate the problem of exposure bias due to the training and inference discrepancy. Previous work has attempted to mitigate this issue by perturbing inputs during training, which consequently mandates the retraining of the DPM. In this work, we conduct a systematic study of exposure bias in DPM and, intriguingly, we find that the exposure bias could be alleviated with a novel sampling method that we propose, without retraining the model. We empirically and theoretically show that, during inference, for each backward time step t and corresponding state ˆxt, there might exist another time step $t_s$ which exhibits superior coupling with $\hat{x}_t$. Based on this finding, we introduce a sampling method
named Time-Shift Sampler. Our framework can be seamlessly integrated to existing sampling algorithms, such as DDPM, DDIM and other high-order solvers, inducing merely minimal additional computations. Experimental results show our method brings significant and consistent improvements in FID scores on different datasets and sampling methods. For example, integrating Time-Shift Sampler to F-PNDM yields a FID=3.88, achieving 44.49% improvements as compared to F-PNDM, on CIFAR-10 with 10 sampling steps, which is more performant than the vanilla DDIM with 100 sampling steps. Our code is available at https://github.com/Mingxiao-Li/TS-DPM.

## item_id: m_2020

TITLE: Reinforcement Learning with Predictive Consistent Representations

ABSTRACT: Learning informative representations from image-based observations is a fundamental problem in deep Reinforcement Learning (RL). However, data inefficiency remains a significant barrier. To this end, we investigate Predictive Consistent Representations (PCR) that enforces predictive consistency on a learned dynamic model. Unlike previous algorithms that simply exploit a forward dynamics model, the PCR agent is trained to predict the future state and retain consistency across the predicted state of observation and its multiple views, which is demonstrated through careful ablation experiments. We empirically show that PCR outperforms the current state-of-the-art baselines in terms of data efficiency on a series of pixel-based control tasks in the DeepMind control suite. Notably, on challenging tasks like Cheetah-run, PCR reaches a 47.4% improvement when environmental steps are limited to 100k steps.

## item_id: m_2021

TITLE: Feature Incay for Representation Regularization

ABSTRACT: Softmax-based loss is widely used in deep learning for multi-class classification, where each class is represented by a weight vector and each sample is represented as a feature vector. Different from traditional learning algorithms where features are pre-defined and only weight vectors are tunable through training, feature vectors are also tunable as representation learning in deep learning. Thus we investigate how to improve the classification performance by better adjusting the features. One main observation is that elongating the feature norm of both correctly-classified and mis-classified feature vectors improves learning: (1) increasing the feature norm of correctly-classified examples induce smaller training loss; (2) increasing the feature norm of mis-classified examples can upweight the contribution from hard examples. Accordingly, we propose feature incay to regularize representation learning by encouraging larger feature norm. In contrast to weight decay which shrinks the weight norm, feature incay is proposed to stretch the feature norm. Extensive empirical results on MNIST, CIFAR10, CIFAR100 and LFW demonstrate the effectiveness of feature incay. 

## item_id: m_2022

TITLE: Internal Purity: A Differential Entropy based Internal Validation Index for Clustering Validation

ABSTRACT: In an effective process of cluster analysis, it is indispensable to validate the goodness of different partitions after clustering. Existing internal validation indices are implemented based on distance, variance and model-selection. The indices based on distance or variance cannnot catpure the real ``density" of the cluster and the time complexity for distance based indices is usually too high to be applied for large datasets. Moreover, the indices based on model-selection tend to overestimate the number of cluster in clustering validation. Therefore, we propose a novel internal validation index based on the differential entropy, named \textit{internal purity} (IP). The proposed IP index can effectively measure the purity of a cluster without using the external cluster information, and successfully overcome the drawbacks of existing internal indices. Based on six powerful deep pre-trained models and without further fine-tuning using the experimental datasets, we use four different clustering algorithms to compare our index with thirteen other well-known internal indices on five text and five image datasets. The results show that, for 60 test cases in total, our IP index can return the optimal clustering results in 43 cases while the second best index can merely report the optimal partition in 17 cases, which demonstrates the significant superiority of our IP index when validating the goodness of the clustering results. Moreover, theoretical analysis for the effectiveness and efficiency of the proposed index are also provided.

## item_id: m_2023

TITLE: Density Estimation for Conservative Q-Learning

ABSTRACT: Batch Reinforcement Learning algorithms aim at learning the best policy from a batch of data without interacting with the environment. Within this setting, one difficulty is to correctly assess the value of state-action pairs that are far from the dataset. Indeed, the lack of information may provoke an overestimation of the value function, leading to non-desirable behaviors. A compromise between enhancing the behaviour policy's performance and staying close to it must be found. To alleviate this issue, most existing approaches introduce a regularization term to favor state-action pairs from the dataset. In this paper, we refine this idea by estimating the density of these state-action pairs to distinguish neighbourhoods. The resulting regularization guides the policy toward meaningful unseen regions, improving the learning process. We hence introduce Density Conservative Q-Learning (D-CQL), a batch-RL algorithm with strong theoretical guarantees that carefully penalizes the value function based on the amount of information collected in the state-action space. The performance of our approach is outlined on many classical benchmark in batch-RL.

## item_id: m_2024

TITLE: Learning to Navigate the Web

ABSTRACT: Learning in environments with large state and action spaces, and sparse rewards, can hinder a Reinforcement Learning (RL) agent’s learning through trial-and-error. For instance, following natural language instructions on the Web (such as booking a flight ticket) leads to RL settings where input vocabulary and number of actionable elements on a page can grow very large. Even though recent approaches improve the success rate on relatively simple environments with the help of human demonstrations to guide the exploration, they still fail in environments where the set of possible instructions can reach millions. We approach the aforementioned problems from a different perspective and propose guided RL approaches that can generate unbounded amount of experience for an agent to learn from. Instead of learning from a complicated instruction with a large vocabulary, we decompose it into multiple sub-instructions and schedule a curriculum in which an agent is tasked with a gradually increasing subset of these relatively easier sub-instructions. In addition, when the expert demonstrations are not available, we propose a novel meta-learning framework that generates new instruction following tasks and trains the agent more effectively. We train DQN, deep reinforcement learning agent, with Q-value function approximated with a novel QWeb neural network architecture on these smaller, synthetic instructions. We evaluate the ability of our agent to generalize to new instructions onWorld of Bits benchmark, on forms with up to 100 elements, supporting 14 million possible instructions. The QWeb agent outperforms the baseline without using any human demonstration achieving 100% success rate on several difficult environments.

## item_id: m_2025

TITLE: QueryStream: Advancing Streaming Video Understanding with Query-Aware Pruning and Proactive Response

ABSTRACT: The increasing demand for real-time interaction in online video scenarios necessitates a new class of efficient streaming video understanding models. However, existing approaches often rely on a query-agnostic ''change-is-important'' assumption, which conflates visual dynamics with semantic relevance, leading to computational redundancy and mistimed responses. To address this, we propose QueryStream, a novel framework that integrates query-awareness into the core of video processing and response scheduling. QueryStream features two synergistic components: (1) Query-Aware Differential Pruning (QDP), a policy that filters the token stream by jointly assessing semantic relevance to the query and temporal novelty against a dynamically smoothed history; and (2) Relevance-Triggered Active Response (RTAR), a dual-gated mechanism that schedules responses based on both high query relevance and significant information density. As a lightweight, training-free module, QueryStream achieves state-of-the-art performance on benchmarks such as StreamingBench and OVO-Bench under moderate pruning, and matches full-token baselines while pruning over 70\% of visual tokens. Notably, our pruning mechanism generalizes to offline tasks, where it serves as a context-denoising module that benefits long-form video understanding. This work not only reveals the vast semantic redundancy in video streams relative to user intent but also establishes a promising, intent-driven direction for efficient and robust online video understanding. Code is available at: https://github.com/Zhangkr2003/QueryStream.

## item_id: m_2026

TITLE: ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review

ABSTRACT: Peer review is the cornerstone of scientific publishing, yet it suffers from inconsistencies, reviewer subjectivity, and scalability challenges. 
We introduce **ReviewerToo**, a modular framework for studying and deploying AI-assisted peer review to complement human judgment with systematic and consistent assessments. ReviewerToo supports systematic experiments with specialized reviewer personas and structured evaluation criteria, and can be partially or fully integrated into real conference workflows. We validate ReviewerToo on a carefully curated dataset of 1,963 paper submissions from ICLR 2025, where our experiments with the gpt-oss-120b model achieves 79.3\% F1 for the task of categorizing a paper as accept/reject compared to 83.8\% for the average human reviewer. Additionally, ReviewerToo-generated reviews are rated as higher quality than the human average by an LLM judge, though still trailing the strongest expert contributions. Our analysis highlights domains where AI reviewers excel (e.g., fact-checking, literature coverage) and where they struggle (e.g., assessing methodological novelty and theoretical contributions), underscoring the continued need for human expertise. Based on these findings, we propose guidelines for integrating AI into peer-review pipelines, showing how AI can enhance consistency, coverage, and fairness while leaving complex evaluative judgments to domain experts. Our work provides a foundation for systematic, hybrid peer-review systems that scale with the growth of scientific publishing.

## item_id: m_2027

TITLE: LLaVA-Read: Enhancing Reading Ability of Multimodal Large Language Models

ABSTRACT: Multimodal large language models have demonstrated impressive capabilities in understanding and manipulating images. However, many of these models struggle with comprehending intensive textual contents embedded within the images, primarily due to the limited text recognition and layout understanding ability. To understand the sources of these limitations, we perform an exploratory analysis showing the drawbacks of classical visual encoders on visual text understanding. Hence, we present LLaVA-Read, a multimodal large language model that utilizes dual visual encoders along with a visual text encoder. Our model surpasses existing state-of-the-art models in various text-rich image understanding tasks, showcasing enhanced comprehension of textual content within images. Together, our research suggests visual text understanding remains an open challenge and an \textit{efficient} visual text encoder is crucial for future successful multimodal systems.

## item_id: m_2028

TITLE: Pretraining One Language Model for All With the Text-To-Text Framework Using Model-Generated Signals

ABSTRACT: Pretrained encoder-decoder language models provide the flexibility to unify various language scenarios into one text-to-text framework, but various recent studies raised concerns about their inferior pretraining efficiency and effectiveness compared to encoder only and decoder only models.  In this paper, we improve the performance of encoder-decoder language models in unifying NLP tasks by pretraining with ELECTRA-style model-generated signals. We first show the challenges of pretraining encoder-decoder models (such as T5) using model-generated signals, including ill-formed target, label leakage, and training instability. We then propose Metro-T5, a new formulation of the denoising pretraining task and multi-task learning loss for encoder-decoder models to incorporate ELECTRA-Style pretraining. Metro-T5 outperforms T5 on a variety of language tasks in standard fine-tuning and prompt-based zero/few-shot scenarios. Our analysis shows Metro-T5 achieves similar generalization ability with much better efficiency, outperforming T0 (3B) in prompt-based learning with only 8% parameters and T5 in all tasks with fewer GPU hours. Our pretraining code and model checkpoints will be open-sourced.

## item_id: m_2029

TITLE: Multiway Multislice PHATE: Visualizing Hidden Dynamics of RNNs through Training

ABSTRACT: Recurrent neural networks (RNNs) are a widely used tool for sequential data analysis, however, they are still often seen as black boxes of computation. Understanding the functional principles of these networks is key to developing ideal model architectures and optimization strategies. Previous studies often only emphasize the networks' representation post-training, overlooking their evolution process. Here, we present Multiway Multislice PHATE (MM-PHATE), a novel method for visualizing the evolution of RNNs' hidden states. MM-PHATE is a graph-based embedding using structured kernels across the multiple dimensions spanned by RNNs: time, training epoch, and units. We demonstrate on multiple datasets that MM-PHATE uniquely preserves hidden representation community structure among units and identifies information processing and compression phases during training. The embedding allows users to look under the hood of RNNs across training and provides an intuitive and comprehensive strategy to understanding the network's internal dynamics and draw conclusions, e.g., on why and how one model outperforms another or how a specific architecture might impact an RNN's learning ability.

## item_id: m_2030

TITLE: Learning Semantically Meaningful Representations Through Embodiment

ABSTRACT: How do humans acquire a meaningful understanding of the world with little to no supervision or semantic labels provided by the environment? Here we investigate embodiment and a closed loop between action and perception as one key component in this process. We take a close look at the representations learned by a deep reinforcement learning agent that is trained with visual and vector observations collected in a 3D environment with sparse rewards. We show that this agent learns semantically meaningful and stable representations of its environment without receiving any semantic labels. Our results show that the agent learns to represent the action relevant information extracted from pixel input in a wide variety of sparse activation patterns. The quality of the representations learned shows the strength of embodied learning and its advantages over fully supervised approaches with regards to robustness and generalizability.

## item_id: m_2031

TITLE: Enhancing Graph Tasks with a Dual-Block Graph Transformer: A Synergistic Approach to Local and Global Attention

ABSTRACT: In this work, we address the limitations of traditional Transformers in graph tasks. While some approaches predominantly leverage local attention mechanisms akin to Graph Neural Networks (GNNs), often neglecting the global attention capabilities inherent in the Transformer model. Conversely, other methods overly focus on the global attention aspect of the Transformer, ignoring the importance of local attention mechanisms in the context of graph structure. To this end, we propose a novel Message Passing Transformer with strategic modifications to the original Transformer, significantly enhancing its performance on graph tasks by improving the handling of local attention. Building on this, we further propose a novel Dual-Block Graph Transformer that synergistically integrates local and global attention mechanisms. This architecture comprises two distinct blocks inside each head: the Message Passing Block, designed to emulate local attention, and a second block that encapsulates the global attention mechanism. This dual-block design inside each head enables our model to capture both fine-grained local and high-level global interactions in graph tasks, leading to a more comprehensive and robust graph representation. We empirically validate our model on node classification tasks, particularly on heterophilic graphs, and graph classification tasks. The results demonstrate that our Dual-Block Graph Transformer significantly outperforms both GNN and Graph Transformer models. Remarkably, this superior performance is achieved without the necessity for complex positional encoding strategies, underscoring the efficacy of our approach.

## item_id: m_2032

TITLE: Distributionally Robust Model-Based Offline Reinforcement Learning with Near-Optimal Sample Complexity

ABSTRACT: This paper concerns the central issues of model robustness and sample efficiency in offline reinforcement learning (RL), which aims to learn to perform decision making from history data without active exploration. Due to uncertainties and variabilities of the environment, it is critical to learn a robust policy---with as few samples as possible---that performs well even when the deployed environment deviates from the nominal one used to collect the history dataset. We consider a distributionally robust formulation of offline RL, focusing on tabular robust Markov decision processes with an uncertainty set specified by the Kullback-Leibler divergence in both finite-horizon and infinite-horizon settings. To combat with sample scarcity, a model-based algorithm that combines distributionally robust value iteration with the principle of pessimism in the face of uncertainty is proposed, by penalizing the robust value estimates with a carefully designed data-driven penalty term. Under a mild and tailored assumption of the history dataset that measures distribution shift without requiring full coverage of the state-action space, we establish the finite-sample complexity of the proposed algorithm, and further show it is almost unimprovable in light of a nearly-matching information-theoretic lower bound up to a polynomial factor of the (effective) horizon length. To the best our knowledge, this provides the first provably near-optimal robust offline RL algorithm that learns under model uncertainty and partial coverage. 

## item_id: m_2033

TITLE: PR-VTON: Enhancing Detail Fidelity in Virtual Try-On with Refined Positional Encoding

ABSTRACT: Recent advancements in pre-trained diffusion models have significantly enhanced image-based virtual try-on, enabling the realistic synthesis of garments for simple textures. However, preserving high-frequency patterns and text consistency remains a formidable challenge, as existing methods often fail to retain fine-grained details. To address this, we introduce PR-VTON, a simple yet effective method that integrates a Position-Refined Positional Encoding (termed PRPE) and a lightweight positional relation learning module (termed PRL) to enhance detail preservation across diverse fabric designs. Specifically, PRPE leverages the inherent impact of positional encoding on attention mechanisms within the Diffusion Transformer (DiT) architecture, guiding attention maps with precise positional cues to achieve superior texture fidelity without additional modules or complex loss functions. Meanwhile, PRL explicitly models token-level correspondences between garments and target bodies, ensuring accurate spatial alignments. Extensive experiments on standard benchmarks demonstrate that PR-DIT surpasses existing baselines in both quantitative and qualitative metrics, with marked improvements in perceptually sensitive areas, such as textual logos. Furthermore, we critically reassess evaluation protocols for virtual try-on, highlighting deficiencies in existing metrics for capturing global consistency and fine detail fidelity,and propose a detail-focused metric loc-CMMD, establishing a more robust standard for high-resolution virtual try-on research.

## item_id: m_2034

TITLE: Decorrelated Double Q-learning

ABSTRACT: Q-learning with value function approximation may have the poor performance because of overestimation bias and imprecise estimate. Specifically, overestimation bias is from the maximum operator over noise estimate, which is exaggerated using the estimate of a subsequent state. Inspired by the recent advance of deep reinforcement learning and Double Q-learning, we introduce the decorrelated double Q-learning (D2Q). Specifically, we introduce the decorrelated regularization item to reduce the correlation between value function approximators, which can lead to less biased estimation and low variance. The experimental results on a suite of MuJoCo continuous control tasks demonstrate that our decorrelated double Q-learning can effectively improve the performance.

## item_id: m_2035

TITLE: Mixout: Effective Regularization to Finetune Large-scale Pretrained Language Models

ABSTRACT: In natural language processing, it has been observed recently that generalization could be greatly improved by finetuning a large-scale language model pretrained on a large unlabeled corpus. Despite its recent success and wide adoption, finetuning a large pretrained language model on a downstream task is prone to degenerate performance when there are only a small number of training instances available. In this paper, we introduce a new regularization technique, to which we refer as “mixout”, motivated by dropout. Mixout stochastically mixes the parameters of two models. We show that our mixout technique regularizes learning to minimize the deviation from one of the two models and that the strength of regularization adapts along the optimization trajectory. We empirically evaluate the proposed mixout and its variants on finetuning a pretrained language model on downstream tasks. More specifically, we demonstrate that the stability of finetuning and the average accuracy greatly increase when we use the proposed approach to regularize finetuning of BERT on downstream tasks in GLUE.

## item_id: m_2036

TITLE: EyeDAS: Securing Perception of Autonomous Cars Against the Stereoblindness Syndrome

ABSTRACT: The ability to detect whether an object is a 2D or 3D object is extremely important in autonomous driving, since a detection error can have life-threatening consequences, endangering the safety of the driver, passengers, pedestrians, and others on the road. 
Methods proposed to distinguish between 2 and 3D objects (e.g., liveness detection methods) are not suitable for autonomous driving, because they are object dependent or do not consider the constraints associated with autonomous driving (e.g., the need for real-time decision-making while the vehicle is moving).
In this paper, we present EyeDAS, a novel few-shot learning-based method aimed at securing an object detector (OD) against the threat posed by the stereoblindness syndrome (i.e., the inability to distinguish between 2D and 3D objects).
We evaluate EyeDAS's real-time performance using 2,000 objects extracted from seven YouTube video recordings of street views taken by a dash cam from the driver's seat perspective.
When applying EyeDAS to seven state-of-the-art ODs as a countermeasure, EyeDAS was able to reduce the 2D misclassification rate from 71.42-100% to 2.4% with a 3D misclassification rate of 0% (TPR of 1.0). 
We also show that EyeDAS outperforms the baseline method and achieves an AUC of over 0.999.

## item_id: m_2037

TITLE: Variational Multi-Task Learning

ABSTRACT: Multi-task learning aims to improve the overall performance of a set of tasks by leveraging their relatedness. When training data is limited using priors is pivotal, but currently this is done in ad-hoc ways. In this paper, we develop variational multi-task learning - VMTL, a general probabilistic inference framework for simultaneously learning multiple related tasks. We cast multi-task learning as a variational Bayesian inference problem, which enables task relatedness to be explored in a principled way by specifying priors. We introduce Gumbel-softmax priors to condition the prior of each task on related tasks. Each prior is represented as a mixture of variational posteriors of other related tasks and the mixing weights are learned in a data-driven manner for each individual task. The posteriors over representations and classifiers are inferred jointly for all tasks and individual tasks are able to improve their performance by using the shared inductive bias. Experimental results demonstrate that VMTL is able to tackle challenging multi-task learning with limited training data well, and it achieves state-of-the-art performance on four benchmarks, consistently surpassing previous methods.

## item_id: m_2038

TITLE: SpRePE: A Spherical Geometry-Aware Position Embedding for Vision Transformers

ABSTRACT: Position embedding (PE) is a key mechanism that breaks the permutation symmetry of tokens in Transformer, introducing a spatial inductive bias that enables attention to model locality, distances, and directional relations. 
Spherical data arise in many scientific domains, most notably in astronomy and meteorology, where Vision Transformers is increasingly adopted for the ability to capture long-range dependencies. However, conventional PEs are designed for linear sequences and cannot faithfully capture the sphere’s non-Euclidean geometry. 
Furthermore, existing designs for encoding spherical positional information rely on additional network modules or specialized network architectures, which introduce extra parameters and computational overhead.
These limitations motivate a geometry-aware and efficient embedding scheme that fully exploits spherical structure to advance Transformer-based modeling on the sphere.
We introduce \textbf{Spherical Reflection Position Embedding (SpRePE)}, a lightweight method efficiently leveraging spherical positional information for Vision Transformer.
SpRePE encodes the absolute position on the sphere using a Householder matrix and incorporates the explicit relative position dependency into the attention formulation, achieving both high computational efficiency and high accuracy without requiring substantial additional parameters and modifications to the overall model architecture.
We evaluate SpRePE on representative tasks, including spherical image classification and global weather forecasting. SpRePE consistently outperforms well-known baselines including APE, RPE, ALiBi and RoPE.
These results indicate that SpRePE offers an efficient and broadly applicable position embedding scheme for Transformer models on the sphere.

## item_id: m_2039

TITLE: ADAPTING PRETRAINED LANGUAGE MODELS FOR LONG DOCUMENT CLASSIFICATION

ABSTRACT: Pretrained language models (LMs) have shown excellent results in achieving human like performance on many language tasks. However, the most powerful LMs have one significant drawback: a fixed-sized input. With this constraint, these LMs are unable to utilize the full input of long documents. In this paper, we introduce a new framework to handle documents of arbitrary lengths. We investigate the addition of a recurrent mechanism to extend the input size and utilizing attention to identify the most discriminating segment of the input. We perform extensive validating experiments on patent and Arxiv datasets, both of which have long text. We demonstrate our method significantly outperforms state-of-the-art results reported in recent literature.

## item_id: m_2040

TITLE: Lie-Access Neural Turing Machines

ABSTRACT: 
  External neural memory structures have recently become a popular tool for
  algorithmic deep learning
  (Graves et al. 2014; Weston et al. 2014).  These models
  generally utilize differentiable versions of traditional discrete
  memory-access structures (random access, stacks, tapes) to provide
  the storage necessary for computational tasks.  In
  this work, we argue that these neural memory systems lack specific
  structure important for relative indexing, and propose an
  alternative model, Lie-access memory, that is explicitly designed
  for the neural setting.  In this paradigm, memory is accessed using
  a continuous head in a key-space manifold. The head is moved via Lie
  group actions, such as shifts or rotations, generated by a
  controller, and memory access is performed by linear smoothing in
  key space. We argue that Lie groups provide a natural generalization
  of discrete memory structures, such as Turing machines, as they
  provide inverse and identity operators while maintaining
  differentiability. To experiment with this approach, we implement
  a simplified Lie-access neural Turing machine (LANTM) with
  different Lie groups.  We find that this approach is able to perform
  well on a range of algorithmic tasks.

## item_id: m_2041

TITLE: Kernel Complexity Reduced Graph Contrastive Learning for Noisy Node Classification

ABSTRACT: Graph Neural Networks (GNNs) have achieved remarkable success in learning node representations and have demonstrated strong performance on node classification. However, their effectiveness can be substantially compromised by noise in real-world graph data. To address this challenge, we propose Kernel Complexity Reduced Graph Contrastive Learning (KCR-GCL), a principled framework for noisy node classification with a provable transductive generalization guarantee. KCR-GCL introduces a novel KCR-GCL encoder, which incorporates a new KCR self-attention layer that adaptively balances different frequency components of the graph inspired by generalized graph convolution and reduces the kernel complexity for provably improved generalization for transductive learning. The KCR-GCL encoder is optimized with a low-rank regularization term through the truncated nuclear norm (TNN) on the gram matrix of the learned features. The learned low-rank representations are then used to train a linear  classifier for transductive node classification in noisy graph data.
The design of KCR-GCL is inspired by the Low Frequency Property (LFP)  widely studied in general deep learning and node-level graph learning, and is further supported by a sharp generalization bound for transductive learning. To the best of our knowledge, KCR-GCL is among the first to theoretically reveal the benefits of low-rank regularization in transductive settings for noisy graph data. Experiments on standard benchmarks highlight the effectiveness and robustness of KCR-GCL in learning node representations under noisy conditions.
The code of KCR-GCL is available at \url{https://anonymous.4open.science/status/KCR-GCL}.

## item_id: m_2042

TITLE: Recurrent Inference Machines for Solving Inverse Problems

ABSTRACT: Inverse problems are typically solved by first defining a model and then choosing an inference procedure. With this separation of modeling from inference, inverse problems can be framed in a modular way. For example, variational inference can be applied to a broad class of models. The modularity, however, typically goes away after model parameters have been trained under a chosen inference procedure. During training, model and inference often interact in a way that the model parameters will ultimately be adapted to the chosen inference procedure, posing the two components inseparable after training. But if model and inference become inseperable after training, why separate them in the first place?

We propose a novel learning framework which abandons the dichotomy between model and inference. Instead, we introduce Recurrent Inference Machines (RIM), a class of recurrent neural networks (RNN) that directly learn to solve inverse problems.

We demonstrate the effectiveness of RIMs in experiments on various image reconstruction tasks. We show empirically that RIMs exhibit the desirable convergence behavior of classical inference procedures, and that they can outperform state-of- the-art methods when trained on specialized inference tasks.

Our approach bridges the gap between inverse problems and deep learning, providing a framework for fast progression in the field of inverse problems.

## item_id: m_2043

TITLE: Understanding Masked Image Modeling via Learning Occlusion Invariant Feature

ABSTRACT: Recently, Masked Image Modeling (MIM) achieves great success in self-supervised visual recognition. However, as a reconstruction-based framework, it is still an open question to understand how MIM works, since MIM appears very different from previous well-studied siamese approaches such as contrastive learning. In this paper, we propose a new viewpoint: MIM implicitly learns occlusion-invariant features, which is analogous to other siamese methods while the latter learns other invariance. By relaxing MIM formulation into an equivalent siamese form, MIM methods can be interpreted in a unified framework with conventional methods, among which only a) data transformations, i.e. what invariance to learn, and b) similarity measurements are different. Furthermore, taking MAE (He et al., 2021) as a representative example of MIM, we empirically find the success of MIM models relates a little to the choice of similarity functions, but the learned occlusion invariant feature introduced by masked image – it turns out to be a favored initialization for vision transformers, even though the learned feature could be less semantic. We hope our findings could inspire researchers to develop more powerful self-supervised methods in computer vision community.

## item_id: m_2044

TITLE: Training Federated GANs  with Theoretical Guarantees: A Universal Aggregation Approach

ABSTRACT: Recently, Generative Adversarial Networks (GANs) have demonstrated their potential in federated learning, i.e., learning a centralized model from data privately hosted by multiple sites. A federated GAN jointly trains a centralized generator and multiple private discriminators hosted at different sites. A major theoretical challenge for the federated GAN is the heterogeneity of the local data distributions. Traditional approaches cannot guarantee to learn the target distribution, which is a mixture of the highly different local distributions. This paper tackles this theoretical challenge, and for the first time, provides a provably correct framework for federated GAN. We propose a new approach called Universal Aggregation, which simulates a centralized discriminator via carefully aggregating the mixture of all private discriminators. We prove that a generator trained with this simulated centralized discriminator can learn the desired target distribution. Through synthetic and real datasets, we show that our method can learn the mixture of largely different distributions, when existing federated GAN methods fail to.

## item_id: m_2045

TITLE: Graph U-Net

ABSTRACT: We consider the problem of representation learning for graph data. Convolutional neural networks can naturally operate on images, but have significant challenges in dealing with graph data. Given images are special cases of graphs with nodes lie on 2D lattices, graph embedding tasks have a natural correspondence with image pixel-wise prediction tasks such as segmentation. While encoder-decoder architectures like U-Net have been successfully applied on many image pixel-wise prediction tasks, similar methods are lacking for graph data. This is due to the fact that pooling and up-sampling operations are not natural on graph data. To address these challenges, we propose novel graph pooling (gPool) and unpooling (gUnpool) operations in this work. The gPool layer adaptively selects some nodes to form a smaller graph based on their scalar projection values on a trainable projection vector. We further propose the gUnpool layer as the inverse operation of the gPool layer. The gUnpool layer restores the graph into its original structure using the position information of nodes selected in the corresponding gPool layer. Based on our proposed gPool and gUnpool layers, we develop an encoder-decoder model on graph, known as the graph U-Net. Our experimental results on node classification tasks demonstrate that our methods achieve consistently better performance than previous models.

## item_id: m_2046

TITLE: Dynamic Planning Networks

ABSTRACT: We introduce Dynamic Planning Networks (DPN), a novel architecture for deep reinforcement learning, that combines model-based and model-free aspects for online planning. Our architecture learns to dynamically construct plans using a learned state-transition model by selecting and traversing between simulated states and actions to maximize valuable information before acting. In contrast to model-free methods, model-based planning lets the agent efficiently test action hypotheses without performing costly trial-and-error in the environment. DPN learns to efficiently form plans by expanding a single action-conditional state transition at a time instead of exhaustively evaluating each action, reducing the required number of state-transitions during planning by up to 96%. We observe various emergent planning patterns used to solve environments, including classical search methods such as breadth-first and depth-first search. Learning To Plan shows improved data efficiency, performance, and generalization to new and unseen domains in comparison to several baselines.

## item_id: m_2047

TITLE: On the Linguistic Capacity of Real-time Counter Automata

ABSTRACT: While counter machines have received little attention in theoretical computer science since the 1960s, they have recently achieved a newfound relevance to the field of natural language processing (NLP). Recent work has suggested that some strong-performing recurrent neural networks utilize their memory as counters. Thus, one potential way to understand the sucess of these networks is to revisit the theory of counter computation. Therefore, we choose to study the abilities of real-time counter machines as formal grammars. We first show that several variants of the counter machine converge to express the same class of formal languages. We also prove that counter languages are closed under complement, union, intersection, and many other common set operations. Next, we show that counter machines cannot evaluate boolean expressions, even though they can weakly validate their syntax. This has implications for the interpretability and evaluation of neural network systems: successfully matching syntactic patterns does not guarantee that a counter-like model accurately represents underlying semantic structures. Finally, we consider the question of whether counter languages are semilinear. This work makes general contributions to the theory of formal languages that are of particular interest for the interpretability of recurrent neural networks.

## item_id: m_2048

TITLE: Compositional Attention Networks for Machine Reasoning

ABSTRACT: We present Compositional Attention Networks, a novel fully differentiable neural network architecture, designed to facilitate explicit and expressive reasoning. While many types of neural networks are effective at learning and generalizing from massive quantities of data, this model moves away from monolithic black-box architectures towards a design that provides a strong prior for iterative reasoning, enabling it to support explainable and structured learning, as well as generalization from a modest amount of data. The model builds on the great success of existing recurrent cells such as LSTMs: It sequences a single recurrent Memory, Attention, and Control (MAC) cell, and by careful design imposes structural constraints on the operation of each cell and the interactions between them, incorporating explicit control and soft attention mechanisms into their interfaces. We demonstrate the model's strength and robustness on the challenging CLEVR dataset for visual reasoning, achieving a new state-of-the-art 98.9% accuracy, halving the error rate of the previous best model. More importantly, we show that the new model is more computationally efficient, data-efficient, and requires an order of magnitude less time and/or data to achieve good results.

## item_id: m_2049

TITLE: Evaluation Metrics for Graph Generative Models: Problems, Pitfalls, and Practical Solutions

ABSTRACT: Graph generative models are a highly active branch of machine learning. Given the steady development of new models of ever-increasing complexity, it is necessary to provide a principled way to evaluate and compare them. In this paper, we enumerate the desirable criteria for such a comparison metric and provide an overview of the status quo of graph generative model comparison in use today, which predominantly relies on the maximum mean discrepancy (MMD). We perform a systematic evaluation of MMD in the context of graph generative model comparison, highlighting some of the challenges and pitfalls researchers inadvertently may encounter. After conducting a thorough analysis of the behaviour of MMD on synthetically-generated perturbed graphs as well as on recently-proposed graph generative models, we are able to provide a suitable procedure to mitigate these challenges and pitfalls. We aggregate our findings into a list of practical recommendations for researchers to use when evaluating graph generative models.

## item_id: m_2050

TITLE: Active View Selection for Scene-level Multi-view Crowd Counting and Localization with Limited Labels

ABSTRACT: Multi-view crowd counting and localization fuse the input multi-views for estimating the crowd number or locations on the ground. Existing methods mainly focus on accurately predicting on the crowd shown in the input views, which neglects the problem of choosing the `best' camera views to perceive all crowds well in the scene. Besides, existing view selection methods require massive labeled views and images, and lack the ability for cross-scene settings, reducing their application scenarios. Thus, in this paper, we study the view selection issue for better scene-level multi-view crowd counting and localization results with cross-scene ability and limited label demand, instead of input-view-level results. We first propose a baseline view selection method (IVS) that considers view and scene geometries in the view selection strategy and conducts the view selection, labeling, and downstream tasks independently. Based on IVS, we put forward an active view selection method (AVS) that jointly optimizes the view selection, labeling, and downstream tasks. In AVS, we actively select the labeled views and consider both the view/scene geometries and the predictions of the downstream task models in the view selection process. Experiments on multi-view counting and localization tasks demonstrate the cross-scene and the limited label demand advantages of the proposed active view selection method (AVS), outperforming existing methods and with wider application scenarios.

## item_id: m_2051

TITLE: Distributed non-parametric deep and wide networks

ABSTRACT: In recent work, it was shown that combining multi-kernel based support vector machines (SVMs) can lead to near state-of-the-art performance on an action recognition dataset (HMDB-51 dataset). In the present work, we show that combining distributed Gaussian Processes with multi-stream deep convolutional neural networks (CNN) alleviate the need to augment a neural network with hand-crafted features. In contrast to prior work, we treat each deep neural convolutional network as an expert wherein the individual predictions (and their respective uncertainties) are combined into a Product of Experts (PoE) framework.

## item_id: m_2052

TITLE: DSPNet: Towards Slimmable Pretrained Networks based on Discriminative Self-supervised Learning

ABSTRACT: Self-supervised learning (SSL) has achieved promising downstream performance. However, when facing various resource budgets in real-world applications, it costs a huge computation burden to pretrain multiple networks of various sizes one by one. In this paper, we propose Discriminative-SSL-based Slimmable Pretrained Networks (DSPNet), which can be trained once and then slimmed to multiple sub-networks of various sizes, each of which faithfully learns good representation and can serve as good initialization for downstream tasks with various resource budgets. Specifically, we extend the idea of slimmable networks to a discriminative SSL paradigm, by integrating SSL and knowledge distillation gracefully. We show comparable or improved performance of DSPNet on ImageNet to the networks individually pretrained one by one under the linear evaluation and semi-supervised evaluation protocols, while reducing large training cost. The pretrained models also generalize well on downstream detection and segmentation tasks. Code will be made public.

## item_id: m_2053

TITLE: The Geometry of Adversarial Subspaces

ABSTRACT: Artificial neural networks (ANNs) are constructed using well-understood mathematical operations, and yet their high-dimensional, non-linear, and compositional nature has hindered our ability to provide an intuitive description of how and why they produce any particular output. A striking example of this lack of understanding is our inability to design networks that are robust to adversarial input perturbations, which are often imperceptible to a human observer but cause significant undesirable changes in the network’s response. The primary contribution of this work is to further our understanding of the decision boundary geometry of ANN classifiers by utilizing such adversarial perturbations. For this purpose, we define adversarial subspaces, which are spanned by orthogonal directions of minimal perturbation to the decision boundary from any given input sample. We find that the decision boundary lies close to input samples in a large subspace, where the distance to the boundary grows smoothly and sub-linearly as one increases the dimensionality of the subspace. We undertake analysis to characterize the geometry of the boundary, which is more curved within the adversarial subspace than within a random subspace of equal dimensionality. To date, the most widely used defense against test-time adversarial attacks is adversarial training, where one incorporates adversarial attacks into the training procedure. Using our analysis, we provide new insight into the consequences of adversarial training by quantifying the increase in boundary distance within adversarial subspaces, the redistribution of proximal class labels, and the decrease in boundary curvature.

## item_id: m_2054

TITLE: Revealing Stochastic Noise of Policy Entropy in Reinforcement Learning

ABSTRACT: On-policy MARL remains attractive under non-stationarity but typically relies on a fixed entropy bonus that conflates useful exploration with stochastic fluctuations from concurrently learning agents. We present \emph{Policy Entropy Manipulation (PEM)}, a simple, drop-in alternative that treats entropy as a noisy measurement to be \emph{denoised} rather than uniformly maximized. PEM applies positive--negative momentum to \emph{entropy gradient} to form a high-pass, variance-controlled signal that preserves persistent exploratory trends while suppressing transient spikes. The method integrates seamlessly with heterogeneous, permutation-based on-policy algorithms, requires no critic or advantage changes, and uses a one-step warm start that recovers the standard entropy objective before momentum takes effect. Across benchmark tasks, PEM yields smoother and more stable learning curves, and improves coordination under heterogeneous observation/action spaces, resulting in stronger generalization than conventional entropy-regularized baselines. Our results indicate that noise-aware control of the entropy channel is an effective and principled way to stabilize exploration in cooperative MARL.

## item_id: m_2055

TITLE: Federated Learning with Data-Agnostic Distribution Fusion

ABSTRACT:     Federated learning has emerged as a promising distributed machine learning paradigm to preserve data privacy. One of the fundamental challenges of federated learning is that data samples across clients are usually not independent and identically distributed (non-IID), leading to slow convergence and severe performance drop of the aggregated global model. In this paper, we propose a novel data-agnostic distribution fusion based model aggregation method called \texttt{FedDAF} to optimize federated learning with non-IID local datasets, based on which the heterogeneous clients' data distributions can be represented by the fusion of several virtual components with different parameters and weights. We develop a variational autoencoder (VAE) method to derive the optimal parameters for the fusion distribution using the limited statistical information extracted from local models, which optimizes model aggregation for federated learning by solving a probabilistic maximization problem. Extensive experiments based on various federated learning scenarios with real-world datasets show that \texttt{FedDAF} achieves significant performance improvement compared to the state-of-the-art.


## item_id: m_2056

TITLE: Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity

ABSTRACT: Data-free continual model merging (DFCMM) aims to fuse independently fine-tuned models into a single backbone that evolves with incoming tasks without accessing task data.
This paper revisits two fundamental desiderata for DFCMM: stability, avoiding interference with earlier tasks, and plasticity, adapting faithfully to each new task. This poses a challenge that existing approaches fail to address: how to bridge data-level desiderata with parameter-space optimization to ensure stability and plasticity in the absence of task data.
To this end, we propose NUFILT(NUll-space FILTering) a data-free framework that directly links these desiderata into parameter-space optimization. Our key observation is that task vectors approximately align with representation subspaces, providing structural surrogates for enforcing stability and plasticity. 
Accordingly, we design a null-space projector that preserves prior responses by filtering overlapping components of new task vectors, ensuring stability.
We further introduce a lightweight LoRA adapter that injects complementary task-specific signals to enable plasticity.
The adapter is trained with a projection-based surrogate loss that preserves consistency with prior knowledge while introducing novel directions. 
This joint filtering–adaptation process enables the backbone to absorb new knowledge while retaining existing behaviors, with updates fused back in a layer-wise linear fashion without extra parameters or inference cost.
Theoretically, we establish approximate subspace alignment guarantees that justify null-space filtering. Empirically, NUFILT achieves state-of-the-art performance with minimal forgetting on both vision and NLP benchmarks, improving average accuracy by 4–7% over OPCM and WUDI-Merging, while narrowing the gap to fine-tuning and reducing computation overhead. The code is available at: https://github.com/zihuanqiu/NUFILT

## item_id: m_2057

TITLE: PD-FS:Surrogate-Enhanced Physical Data-Driven Framework for Rapid Deep Reinforcement Learning Control

ABSTRACT: While deep reinforcement learning (DRL) has demonstrated broad potential in se-
quential decision-making, its application to fluid–dynamic systems remains lim-
ited by the prohibitive cost of high-fidelity simulations and the difficulty of cap-
turing multi-scale unsteady behaviors. In this work, we focus specifically on
aquatic locomotion of fish-like robotic, where the control objective is to track spe-
cific target point while maintaining energy efficiency within the constrained time.
The agent observes low-dimensional kinematic states and flow-related signals,
and outputs oscillation frequency commands that drive body undulation. These
sensing–action constraints define a task that requires both accurate flow responses
and fast, iterative learning. Motivated by these domain-specific requirements, we
propose a task-oriented Physical Data-Driven Flow Simulation (PD-FS) frame-
work—a staged pipeline that couples lightweight neural surrogates with physics-
guided refinement in full-order CFD. PD-FS incorporates mode-conditioned sur-
rogate models with cycle-locked and memory-aware updates, enabling sample-
efficient training while faithfully reproducing critical frequency-switching dynam-
ics. Rather than claiming general applicability, we position PD-FS as an engineer-
ing integration tailored for fish swimming control under fluid–structure interac-
tion. Policies refined in the CFD solvers adapt to nonlinear flow responses without
relying on extensive domain randomization. In controlled fish-locomotion bench-
marks, PD-FS achieves nearly 50 times faster training compared with CFD-only
baselines, while reducing energy expenditure by over 20% at comparable success
rates. These results highlight PD-FS as a domain-specific surrogate to CFD work-
flow for efficient and physically consistent control of fish-like robotics.

## item_id: m_2058

TITLE: FractalNet: Ultra-Deep Neural Networks without Residuals

ABSTRACT: We introduce a design strategy for neural network macro-architecture based on self-similarity.  Repeated application of a simple expansion rule generates deep networks whose structural layouts are precisely truncated fractals.  These networks contain interacting subpaths of different lengths, but do not include any pass-through or residual connections; every internal signal is transformed by a filter and nonlinearity before being seen by subsequent layers.  In experiments, fractal networks match the excellent performance of standard residual networks on both CIFAR and ImageNet classification tasks, thereby demonstrating that residual representations may not be fundamental to the success of extremely deep convolutional neural networks.  Rather, the key may be the ability to transition, during training, from effectively shallow to deep.  We note similarities with student-teacher behavior and develop drop-path, a natural extension of dropout, to regularize co-adaptation of subpaths in fractal architectures.  Such regularization allows extraction of high-performance fixed-depth subnetworks.  Additionally, fractal networks exhibit an anytime property: shallow subnetworks provide a quick answer, while deeper subnetworks, with higher latency, provide a more accurate answer.

## item_id: m_2059

TITLE: LoRA: Low-Rank Adaptation of Large Language Models

ABSTRACT: An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible.
Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by a factor of 10,000 and the GPU memory requirement by a factor of 3. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at https://github.com/microsoft/LoRA.

## item_id: m_2060

TITLE: Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning

ABSTRACT: While great strides have been made in using deep learning algorithms to solve supervised learning tasks, the problem of unsupervised learning - leveraging unlabeled examples to learn about the structure of a domain - remains a difficult unsolved challenge. Here, we explore prediction of future frames in a video sequence as an unsupervised learning rule for learning about the structure of the visual world. We describe a predictive neural network ("PredNet") architecture that is inspired by the concept of "predictive coding" from the neuroscience literature. These networks learn to predict future frames in a video sequence, with each layer in the network making local predictions and only forwarding deviations from those predictions to subsequent network layers. We show that these networks are able to robustly learn to predict the movement of synthetic (rendered) objects, and that in doing so, the networks learn  internal representations that are useful for decoding latent object parameters (e.g. pose) that support object recognition with fewer training views. We also show that these networks can scale to complex natural image streams (car-mounted camera videos), capturing key aspects of both egocentric movement and the movement of objects in the visual scene, and the representation learned in this setting is useful for estimating the steering angle. These results suggest that prediction represents a powerful framework for unsupervised learning, allowing for implicit learning of object and scene structure.

## item_id: m_2061

TITLE: Inductive Bias of Deep Convolutional Networks through Pooling Geometry

ABSTRACT: Our formal understanding of the inductive bias that drives the success of convolutional networks on computer vision tasks is limited. In particular, it is unclear what makes hypotheses spaces born from convolution and pooling operations so suitable for natural images. In this paper we study the ability of convolutional networks to model correlations among regions of their input. We theoretically analyze convolutional arithmetic circuits, and empirically validate our findings on other types of convolutional networks as well. Correlations are formalized through the notion of separation rank, which for a given partition of the input, measures how far a function is from being separable. We show that a polynomially sized deep network supports exponentially high separation ranks for certain input partitions, while being limited to polynomial separation ranks for others. The network's pooling geometry effectively determines which input partitions are favored, thus serves as a means for controlling the inductive bias. Contiguous pooling windows as commonly employed in practice favor interleaved partitions over coarse ones, orienting the inductive bias towards the statistics of natural images. Other pooling schemes lead to different preferences, and this allows tailoring the network to data that departs from the usual domain of natural imagery. In addition to analyzing deep networks, we show that shallow ones support only linear separation ranks, and by this gain insight into the benefit of functions brought forth by depth - they are able to efficiently model strong correlation under favored partitions of the input.

## item_id: m_2062

TITLE: Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!

ABSTRACT: Sparse Neural Networks (SNNs) have received voluminous attention predominantly due to growing computational and memory footprints of consistently exploding parameter count in large-scale models. Similar to their dense counterparts, recent SNNs generalize just as well and are equipped with numerous favorable benefits (e.g., low complexity, high scalability, and robustness), sometimes even better than the original dense networks. As research effort is focused on developing increasingly sophisticated sparse algorithms, it is startling that a comprehensive benchmark to evaluate the effectiveness of these algorithms has been highly overlooked. In absence of a carefully crafted evaluation benchmark, most if not all, sparse algorithms are evaluated against fairly simple and naive tasks (eg. CIFAR-10/100, ImageNet, GLUE, etc.), which can potentially camouflage many advantages as well unexpected predicaments of SNNs. In pursuit of a more general evaluation and unveiling the true potential of sparse algorithms, we introduce “Sparsity May Cry” Benchmark (SMC-Bench), a collection of carefully-curated 4 diverse tasks with 10 datasets, that accounts for capturing a wide range of domain-specific and sophisticated knowledge. Our systemic evaluation of the most representative sparse algorithms reveals an important obscured observation: the state-of-the-art magnitude- and/or gradient-based sparse algorithms seemingly fail to perform on SMC-Bench when applied out-of-the-box, sometimes at significantly trivial sparsity as low as 5%. The observations seek the immediate attention of the sparsity research community to reconsider the highly proclaimed benefits of SNNs. We further conduct a thorough investigation into the reasons for the failure of common SNNs. Our analysis points out that such failure is intimately related to the “lazy regime” of large model training, which hints us with stronger pruning recipes that alleviate the failure on SMC-Bench (though still more or less suffering). By incorporating these well-thought and diverse tasks, SMC-Bench is designed to favor and encourage the development of more scalable and generalizable sparse algorithms. We open-source SMC-Bench to assist researchers in building next-generation sparse algorithms that scale and generalize: https://github.com/VITA-Group/SMC-Bench.

## item_id: m_2063

TITLE: Pruning Parameterization with Bi-level Optimization for Efficient Semantic Segmentation on the Edge

ABSTRACT: With the ever-increasing popularity of edge devices, it is necessary to implement real-time segmentation on the edge for autonomous driving and many other applications. Vision Transformers (ViTs) have shown considerably stronger results for many vision tasks. However, ViTs with the full-attention mechanism usually consume a large number of computational resources, leading to difficulties for real-time inference on edge devices. In this paper, we aim to derive ViTs with fewer computations and fast inference speed to facilitate the dense prediction of semantic segmentation on edge devices. To achieve this, we propose a pruning parameterization method to formulate the pruning problem of semantic segmentation. Then we adopt a bi-level optimization method to solve this problem with the help of implicit gradients. Our experimental results demonstrate that we can achieve 38.9 mIoU on ADE20K val with a speed of 56.5 FPS on Samsung S21, which is the highest mIoU under the same computation constraint with real-time inference.

## item_id: m_2064

TITLE: Rethinking Optimal Transport in Offline Reinforcement Learning

ABSTRACT: We present a novel approach for offline reinforcement learning that bridges the gap between recent advances in neural optimal transport and reinforcement learning algorithms. Our key idea is to compute the optimal transport between states and actions with an action-value cost function and implicitly recover an optimal map that can serve as a policy. Building on this concept, we develop a new algorithm called Extremal Monge Reinforcement Learning that treats offline reinforcement learning as an extremal optimal transport problem. Unlike previous transport-based offline reinforcement learning algorithms, our method focuses on improving the policy beyond the behavior policy, rather than addressing the distribution shift problem. We evaluated the performance of our method on various continuous control problems and demonstrated improvements over existing algorithms.

## item_id: m_2065

TITLE: Domain Adaptation via Low-Rank Basis Approximation

ABSTRACT: Domain adaptation focuses on the reuse of supervised learning models in a new context. Prominent applications can be found in robotics, image processing or web mining. In these areas, learning scenarios change by nature, but often remain related and motivate the reuse of existing supervised models.
While the majority of symmetric and asymmetric domain adaptation algorithms utilize all available source and target domain data, we show that efficient domain adaptation requires only a substantially smaller subset from both domains. This makes it more suitable for real-world scenarios where target domain data is rare. The presented approach finds a target subspace representation for source and target data to address domain differences by orthogonal basis transfer. By employing a low-rank approximation, the approach remains low in computational time. 
The presented idea is evaluated in typical domain adaptation tasks with standard benchmark data.

## item_id: m_2066

TITLE: On the Global Convergence of Natural Actor-Critic with Neural Network Parametrization

ABSTRACT: Despite the empirical effectiveness of natural actor-critic (NAC) algorithms, their theoretical underpinnings remain relatively unexplored, especially with neural network parameterizations. In the existing literature, the non-asymptotic sample complexity bounds for NAC hold only when the critic is either tabular or are represented by a linear function. In this work, we relax such assumptions for  NAC and utilize multi-layer neural network parameterization of the critic and an arbitrary smooth function for the actor. We establish the non-asymptotic sample complexity bounds of $\tilde{\mathcal{O}}\left(\frac{1}{\epsilon^{4}(1-\gamma)^{4}}\right)$ for the global convergence of NAC algorithm. We obtain this result using our unique decomposition of the error incurred at each critic step. The critic error is decomposed into the error incurred in fitting the sampled data, the error incurred due to the lack of knowledge of the transition matrix as well as the error incurred due to the limited approximation power of the class of neural networks. In contrast to the existing works for NAC with neural network parameterization of the critic, our analysis does not require i.i.d sampling.

## item_id: m_2067

TITLE: Negative Sampling From the Ground Up: A Redesign for Graph-based Recommendations

ABSTRACT: Negative sampling is an important yet challenging component in self-supervised graph representation learning, particularly for recommendation systems where user-item interactions are modeled as bipartite graphs. Existing methods often rely on heuristics or human-specified principles to design negative sampling distributions. This potentially overlooks the usage of an underlying ``true'' negative distribution, which we might be able to access as an oracle despite not knowing its exact form. In this work, we shift the focus from manually designing negative sampling distributions to a more principled method that approximates and leverages the underlying true distribution. We expand this idea in the analysis of two scenarios: (1) when the observed graph is an unbiased sample from the true distribution, and (2) when the observed graph is biased with partially observable positive edges. The analysis result is the derivation of a sampling strategy as the numerical approximation of a well-established learning objective. Our theoretical findings are also empirically validated, and our new sampling methods achieve state-of-the-art performance on real-world datasets.

## item_id: m_2068

TITLE: Better Together: Resnet-50 accuracy with $13 \times $ fewer parameters and at $3 \times $ speed

ABSTRACT: Recent research on compressing deep neural networks has focused on reducing the number of parameters. Smaller networks are easier to export and deploy on edge-devices. We introduce Adjoined networks as a training approach that can regularize and compress any CNN-based neural architecture. Our one-shot learning paradigm trains both the original and the smaller networks together. The parameters of the smaller network are shared across both the architectures. We prove strong theoretical guarantees on the regularization behavior of the adjoint training paradigm. We complement our theoretical analysis by an extensive empirical evaluation of both the compression and regularization behavior of adjoint networks. For resnet-50 trained adjointly on Imagenet, we are able to achieve a $13.7 \times$ reduction in the number of parameters and a $3 \times$ improvement in inference time without any significant drop in accuracy. For the same architecture on CIFAR-100, we are able to achieve a $99.7 \times$ reduction in the number of parameters and a $5 \times$ improvement in inference time. On both these datasets, the original network trained in the adjoint fashion gains about $3\%$ in top-1 accuracy as compared to the same network trained in the standard fashion. 

## item_id: m_2069

TITLE: Multi-Advisor Reinforcement Learning

ABSTRACT: We consider tackling a single-agent RL problem by distributing it to $n$ learners. These learners, called advisors, endeavour to solve the problem from a different focus. Their advice, taking the form of action values, is then communicated to an aggregator, which is in control of the system. We show that the local planning method for the advisors is critical and that none of the ones found in the literature is flawless: the \textit{egocentric} planning overestimates values of states where the other advisors disagree, and the \textit{agnostic} planning is inefficient around danger zones. We introduce a novel approach called \textit{empathic} and discuss its theoretical aspects. We empirically examine and validate our theoretical findings on a fruit collection task.

## item_id: m_2070

TITLE: Interactive Agent Modeling by Learning to Probe

ABSTRACT: The ability of modeling the other agents, such as understanding their intentions and skills, is essential to an agent's interactions with other agents. Conventional agent modeling relies on passive observation from demonstrations. In this work, we propose an interactive agent modeling scheme enabled by encouraging an agent to learn to probe. In particular, the probing agent (i.e. a learner) learns to interact with the environment and with a target agent (i.e., a demonstrator) to maximize the change in the observed behaviors of that agent. Through probing, rich behaviors can be observed and are used for enhancing the agent modeling to learn a more accurate mind model of the target agent. Our framework consists of two learning processes: i) imitation learning for an approximated agent model and ii) pure curiosity-driven reinforcement learning for an efficient probing policy to discover new behaviors that otherwise can not be observed. We have validated our approach in four different tasks. The experimental results suggest that the agent model learned by our approach i) generalizes better in novel scenarios than the ones learned by passive observation, random probing, and other curiosity-driven approaches do, and ii) can be used for enhancing performance in multiple applications including distilling optimal planning to a policy net, collaboration, and competition. A video demo is available at https://www.dropbox.com/s/8mz6rd3349tso67/Probing_Demo.mov?dl=0

## item_id: m_2071

TITLE: Incorporating Symmetry into Deep Dynamics Models for Improved Generalization

ABSTRACT: Recent work has shown deep learning can accelerate the prediction of physical dynamics relative to numerical solvers. However, limited physical accuracy and an inability to generalize under distributional shift limit its applicability to the real world. We propose to improve accuracy and generalization by incorporating symmetries into convolutional neural networks. Specifically, we employ a variety of methods each tailored to enforce a different symmetry. Our models are both theoretically and experimentally robust to distributional shift by symmetry group transformations and enjoy favorable sample complexity. We demonstrate the advantage of our approach on a variety of physical dynamics including Rayleigh–Bénard convection and real-world ocean currents and temperatures. Compare with image or text applications, our work is a significant step towards applying equivariant neural networks to high-dimensional systems with complex dynamics.

## item_id: m_2072

TITLE: Distribution-Interpolation Trade off in Generative Models

ABSTRACT: We investigate the properties of multidimensional probability distributions in the context of latent space prior distributions of implicit generative models. Our work revolves around the phenomena arising while decoding linear interpolations between two random latent vectors -- regions of latent space in close proximity to the origin of the space are oversampled, which restricts the usability of linear interpolations as a tool to analyse the latent space. We show that the distribution mismatch can be eliminated completely by a proper choice of the latent probability distribution or using non-linear interpolations. We prove that there is a trade off between the interpolation being linear, and the latent distribution having even the most basic properties required for stable training, such as finite mean. We use the multidimensional Cauchy distribution as an example of the prior distribution, and also provide a general method of creating non-linear interpolations, that is easily applicable to a large family of commonly used latent distributions.

## item_id: m_2073

TITLE: Enhancing Robustness of Deep Networks Based on a Two-phase Model of Their Training with Noisy Labels

ABSTRACT: In this study we model explicitly the learning behavior of deep neural networks (DNNs) trained with noisy labels in image classification. Specifically, we show theoretically and experimentally that the training process can be divided into two phases: a learning phase in which the outputs of DNNs converge to a hidden noise distribution no matter whether the training samples are clean or noisy; and a memorization phase in which DNNs start to overfit until the output for each training sample converges to its corresponding noisy one-hot labels. This two-phase model enables us to develop two simple yet accurate methods that rely on the outputs of DNNs to estimate the noise transition matrix (NTM). It also enables us to resolve a pitfall of many existing methods for robust training under noisy labels based on the small-loss assumption, namely clean samples have smaller loss than noisy samples in the early training phase. We show that these methods fail when NTM is not a column diagonally-maximum matrix and that this pitfall can be fixed by modifying the small-loss assumption based on our NTM estimation methods.

## item_id: m_2074

TITLE: Preventing Collapse in Contrastive Learning with Orthonormal Prototypes (CLOP)

ABSTRACT: Contrastive learning has emerged as a powerful method in deep learning, excelling at learning effective representations through contrasting samples from different distributions. However, dimensional collapse, where embeddings converge into a lower-dimensional space, poses a significant challenge, especially in semi-supervised and self-supervised setups. In this paper, we first theoretically analyze the effect of large learning rates on contrastive losses that solely rely on the cosine similarity metric, and derive a theoretical bound to mitigate this collapse. Building on these insights, we propose CLOP, a novel semi-supervised loss function designed to prevent dimensional collapse by promoting the formation of orthogonal linear subspaces among class embeddings. Unlike prior approaches that enforce a simplex ETF structure, CLOP focuses on subspace separation, leading to more distinguishable embeddings. Through extensive experiments on real and synthetic datasets, we demonstrate that CLOP enhances performance, providing greater stability across different learning rates and batch sizes.

## item_id: m_2075

TITLE: Provable Hierarchy-Based Meta-Reinforcement Learning

ABSTRACT: Hierarchical reinforcement learning (HRL) has seen widespread interest as an approach to tractable learning of complex modular behaviors. However, existing work either assume access to expert-constructed hierarchies, or use hierarchy-learning heuristics with no provable guarantees. To address this gap, we analyze HRL in the meta-RL setting, where a learner learns latent hierarchical structure during meta-training for use in a downstream task. We consider a tabular setting where natural hierarchical structure is embedded in the transition dynamics. Analogous to supervised meta-learning theory, we provide “diversity conditions” which, together with a tractable optimism-based algorithm, guarantee sample-efficient recovery of this natural hierarchy. Furthermore, we provide regret bounds on a learner using the recovered hierarchy to solve a meta-test task. Our bounds incorporate common notions in HRL literature such as temporal and state/action abstractions, suggesting that our setting and analysis capture important features of HRL in practice.

## item_id: m_2076

TITLE: Towards Antisymmetric Neural Ansatz Separation

ABSTRACT: We study separations between two fundamental models (or \emph{Ansätze}) of antisymmetric functions, that is, functions $f$ of the form $f(x_{\sigma(1)}, \ldots, x_{\sigma(N)}) = \text{sign}(\sigma)f(x_1, \ldots, x_N)$, where $\sigma$ is any permutation. 
These arise in the context of quantum chemistry, and are the basic modeling tool for wavefunctions of Fermionic systems. 
Specifically, we consider two popular antisymmetric Ansätze: the Slater representation, which leverages the alternating structure of determinants, and the Jastrow ansatz, which augments Slater determinants with a product by an arbitrary symmetric function. We construct an antisymmetric function that can be more efficiently expressed in Jastrow form, yet provably cannot be approximated by Slater determinants unless there are exponentially (in $N^2$) many terms. This represents the first explicit quantitative separation between these two Ansätze.

## item_id: m_2077

TITLE: IMPLICIT VARIATIONAL REJECTION SAMPLING

ABSTRACT: Variational Inference (VI) is a cornerstone technique in Bayesian machine learning, employed to approximate complex posterior distributions. However, traditional VI methods often rely on mean-field assumptions, which may inadequately capture the true posterior's complexity. To address this limitation, recent advancements have utilized neural networks to model implicit distributions, thereby offering increased flexibility. Despite this, the practical constraints of neural network architectures can still result in inaccuracies in posterior approximations. In this work, we introduce a novel method called Implicit Variational Rejection Sampling (IVRS), which integrates implicit distributions with rejection sampling to enhance the approximation of the posterior distribution. Our method employs neural networks to construct implicit proposal distributions and utilizes rejection sampling with a meticulously designed acceptance probability function. A discriminator network is employed to estimate the density ratio between the implicit proposal and the true posterior, thereby refining the approximation. We propose the Implicit Resampling Evidence Lower Bound (IR-ELBO) as a metric to characterize the quality of the resampled distribution, enabling the derivation of a tighter variational lower bound. Experimental results demonstrate that our method outperforms traditional variational inference techniques in terms of both accuracy and efficiency, leading to significant improvements in inference performance. This work not only showcases the effective combination of implicit distributions and rejection sampling but also offers a novel perspective and methodology for advancing variational inference.

## item_id: m_2078

TITLE: Large Margin Neural Language Models

ABSTRACT: Neural language models (NLMs) are generative, and they model the distribution of grammatical sentences. Trained on huge corpus, NLMs are pushing the limit of modeling accuracy. Besides, they have also been applied to supervised learning tasks that decode text, e.g., automatic speech recognition (ASR). By re-scoring the n-best list, NLM can select grammatically more correct candidate among the list, and significantly reduce word/char error rate. However, the generative nature of NLM may not guarantee a discrimination between “good” and “bad” (in a task-specific sense) sentences, resulting in suboptimal performance. This work proposes an approach to adapt a generative NLM to a discriminative one. Different from the commonly used maximum likelihood objective, the proposed method aims at enlarging the margin between the “good” and “bad” sentences. It is trained end-to-end and can be widely applied to tasks that involve the re-scoring of the decoded text. Significant gains are observed in both ASR and statistical machine translation (SMT) tasks.

## item_id: m_2079

TITLE: TransINT: Embedding Implication Rules in Knowledge Graphs with Isomorphic Intersections of Linear Subspaces

ABSTRACT: Knowledge Graphs (KG), composed of entities and relations, provide a structured representation of knowledge. For easy access to statistical approaches on relational data, multiple methods to embed a KG as components of R^d have been introduced. We propose TransINT, a novel and interpretable KG embedding method that isomorphically preserves the implication ordering among relations in the embedding space. TransINT maps set of entities (tied by a relation) to continuous sets of vectors that are inclusion-ordered isomorphically to relation implications. With a novel parameter sharing scheme, TransINT enables automatic training on missing but implied facts without rule grounding. We achieve new state-of-the-art performances with signficant margins in Link Prediction and Triple Classification on FB122 dataset, with boosted performance even on test instances that cannot be inferred by logical rules. The angles between the continuous sets embedded by TransINT provide an interpretable way to mine semantic relatedness and implication rules among relations. 

## item_id: m_2080

TITLE: A Statistical Approach for Controlled Training Data Detection

ABSTRACT: Detecting training data for large language models (LLMs) is receiving growing attention, especially in applications requiring high reliability. While numerous efforts have been made to address this issue, they typically focus on accuracy without ensuring controllable results.
To fill this gap, we propose **K**nockoff Inference-based **T**raining data **D**etector (KTD), a novel method that achieves rigorous false discovery rate (FDR) control in training data detection. Specifically, KTD generates synthetic knockoff samples that seamlessly replace original data points without compromising contextual integrity. A novel knockoff statistic, which incorporates multiple knockoff draws, is then calculated to ensure FDR control while maintaining high power. 
Our theoretical analysis demonstrates KTD's asymptotic optimality in terms of FDR control and power. Empirical experiments on real-world datasets such as WikiMIA, XSum and Real Time BBC News further validate KTD's superior performance compared to existing methods.

## item_id: m_2081

TITLE: Quick-Tune: Quickly Learning Which Pretrained Model to Finetune and How

ABSTRACT: With the ever-increasing number of pretrained models, machine learning practitioners are continuously faced with which pretrained model to use, and how to finetune it for a new dataset. In this paper, we propose a methodology that jointly searches for the optimal pretrained model and the hyperparameters for finetuning it. Our method transfers knowledge about the performance of many pretrained models with multiple hyperparameter configurations on a series of datasets. To this aim, we evaluated over 20k hyperparameter configurations for finetuning 24 pretrained image classification models on 87 datasets to generate a large-scale meta-dataset. We meta-learn a gray-box performance predictor on the learning curves of this meta-dataset and use it for fast hyperparameter optimization on new datasets. We empirically demonstrate that our resulting approach can quickly select an accurate pretrained model for a new dataset together with its optimal hyperparameters.

## item_id: m_2082

TITLE: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control

ABSTRACT: Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model.  This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. Code and videos: https://lift-humanoid.github.io

## item_id: m_2083

TITLE: Causal Information Prioritization for Efficient Reinforcement Learning

ABSTRACT: Current Reinforcement Learning (RL) methods often suffer from sample-inefficiency, resulting from blind exploration strategies that neglect causal relationships among states, actions, and rewards. Although recent causal approaches aim to address this problem, they lack grounded modeling of reward-guided causal understanding of states and actions for goal-orientation, thus impairing learning efficiency. To tackle this issue, we propose a novel method named Causal Information Prioritization (CIP) that improves sample efficiency by leveraging factored MDPs to infer causal relationships between different dimensions of states and actions with respect to rewards, enabling the prioritization of causal information. Specifically, CIP identifies and leverages causal relationships between states and rewards to execute counterfactual data augmentation to prioritize high-impact state features under the causal understanding of the environments. Moreover, CIP integrates a causality-aware empowerment learning objective, which significantly enhances the agent's execution of reward-guided actions for more efficient exploration in complex environments. 
To fully assess the effectiveness of CIP, we conduct extensive experiments across $39$ tasks in $5$ diverse continuous control environments, encompassing both locomotion and manipulation skills learning with pixel-based and sparse reward settings. Experimental results demonstrate that CIP consistently outperforms existing RL methods across a wide range of scenarios.

## item_id: m_2084

TITLE: Zero-Mean Regularized Spectral Contrastive Learning: Implicitly Mitigating Wrong Connections in Positive-Pair Graphs

ABSTRACT: Contrastive learning has emerged as a popular paradigm of self-supervised learning that learns representations by encouraging representations of positive pairs to be similar while representations of negative pairs to be far apart. The spectral contrastive loss, in synergy with the notion of positive-pair graphs, offers valuable theoretical insights into the empirical successes of contrastive learning. In this paper, we propose incorporating an additive factor into the term of spectral contrastive loss involving negative pairs. This simple modification can be equivalently viewed as introducing a regularization term that enforces the mean of representations to be zero, which thus is referred to as *zero-mean regularization*. It intuitively relaxes the orthogonality of representations between negative pairs and implicitly alleviates the adverse effect of wrong connections in the positive-pair graph, leading to better performance and robustness. To clarify this, we thoroughly investigate the role of zero-mean regularized spectral contrastive loss in both unsupervised and supervised scenarios with respect to theoretical analysis and quantitative evaluation. These results highlight the potential of zero-mean regularized spectral contrastive learning to be a promising approach in various tasks.

## item_id: m_2085

TITLE: Learning Internal Dense But External Sparse Structures of Deep Neural Network

ABSTRACT: Recent years have witnessed two seemingly opposite developments of deep convolutional neural networks (CNNs). On one hand, increasing the density of CNNs by adding cross-layer connections achieve higher accuracy. On the other hand, creating sparsity structures through regularization and pruning methods enjoys lower computational costs. In this paper, we bridge these two by proposing a new network structure with locally dense yet externally sparse connections. This new structure uses dense modules, as basic building blocks and then sparsely connects these modules via a novel algorithm during the training process. Experimental results demonstrate that the locally dense yet externally sparse structure could acquire competitive performance on benchmark tasks (CIFAR10, CIFAR100, and ImageNet) while keeping the network structure slim.

## item_id: m_2086

TITLE: Neural Data Filter for Bootstrapping Stochastic Gradient Descent

ABSTRACT: Mini-batch based Stochastic Gradient Descent(SGD) has been widely used to train deep neural networks efficiently. In this paper, we design a general framework to automatically and adaptively select training data for SGD. The framework is based on neural networks and we call it \emph{\textbf{N}eural \textbf{D}ata \textbf{F}ilter} (\textbf{NDF}). In Neural Data Filter, the whole training process of the original neural network is monitored and supervised by a deep reinforcement network, which controls whether to filter some data in sequentially arrived mini-batches so as to maximize future accumulative reward (e.g., validation accuracy). The SGD process accompanied with NDF is able to use less data and converge faster while achieving comparable accuracy as the standard SGD trained on the full dataset. Our experiments show that NDF bootstraps SGD training for different neural network models including Multi Layer Perceptron Network and Recurrent Neural Network trained on various types of tasks including image classification and text understanding.

## item_id: m_2087

TITLE: On Dropout, Overfitting, and Interaction Effects in Deep Neural Networks

ABSTRACT: We examine Dropout through the perspective of interactions. Given $N$ variables, there are $\mathcal{O}(N^2)$ possible pairwise interactions, $\mathcal{O}(N^3)$ possible 3-way interactions, i.e. $\mathcal{O}(N^k)$ possible interactions of $k$ variables. Conversely, the probability of an interaction of $k$ variables surviving Dropout at rate $p$ is $\mathcal{O}((1-p)^k)$. In this paper, we show that these rates cancel, and as a result, Dropout selectively regularizes against learning higher-order interactions. We prove this new perspective analytically for Input Dropout and empirically for Activation Dropout. This perspective on Dropout has several practical implications: (1) higher Dropout rates should be used when we need stronger regularization against spurious high-order interactions, (2) caution must be used when interpreting Dropout-based feature saliency measures, and (3) networks trained with Input Dropout are biased estimators, even with infinite data. We also compare Dropout to regularization via weight decay and early stopping and find that it is difficult to obtain the same regularization against high-order interactions with these methods.

## item_id: m_2088

TITLE: Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data

ABSTRACT: Some machine learning applications involve training data that is sensitive, such
as the medical histories of patients in a clinical trial. A model may
inadvertently and implicitly store some of its training data; careful analysis
of the model may therefore reveal sensitive information.

To address this problem, we demonstrate a generally applicable approach to
providing strong privacy guarantees for training data: Private Aggregation of Teacher Ensembles (PATE). The approach combines, in
a black-box fashion, multiple models trained with disjoint datasets, such as
records from different subsets of users. Because they rely directly on sensitive
data, these models are not published, but instead used as ''teachers'' for a ''student'' model. 
The student learns to predict an output chosen by noisy voting
among all of the teachers, and cannot directly access an individual teacher or
the underlying data or parameters. The student's privacy properties can be
understood both intuitively (since no single teacher and thus no single dataset
dictates the student's training) and formally, in terms of differential privacy.
 These properties hold even if an adversary can not only query the student but
also inspect its internal workings.

Compared with previous work, the approach imposes only weak assumptions on how
teachers are trained: it applies to any model, including non-convex models like
DNNs. We achieve state-of-the-art privacy/utility trade-offs on MNIST and SVHN
thanks to an improved privacy analysis and semi-supervised learning.


## item_id: m_2089

TITLE: Adversarial Agent Collaboration for C to Rust Translation

ABSTRACT: Translating C to memory-safe languages, like Rust, prevents critical memory safety vulnerabilities that are prevalent in legacy C software.
Existing approaches for C to safe Rust translation, including LLM-assisted ones, do not generalize on larger ($> 500$ LoC) C codebases because they depend on complex program analyses that frequently break.
In this work, we present ACToR (**A**dversarial **C** **To** **R**ust translator), a simple LLM agent-based approach. 
Inspired by GANs, ACToR pits a generator agent against a discriminator agent, which collaborate to iteratively generate a Rust translation. 
On each iteration, the translator agent synthesizes and refines a Rust translation to pass an existing suite of tests, and then the discriminator agent finds new failing tests.
We demonstrate that ACToR translates all of the 63 real-world command-line utilities considered in our benchmarks, which have an average size of 473 lines of code, and it achieves over 90\% test pass rate with zero human intervention during translation.
To our knowledge, it is the first work to show evidence that an agent-centric approach can reliably and automatically convert standalone command-line C programs at this scale.
Furthermore, ACToR improves translation correctness by up to 25.1\% compared to baseline, non-adversarial approaches.

## item_id: m_2090

TITLE: Coarse-to-fine Knowledge Graph Domain Adaptation based on Distantly-supervised Iterative Training

ABSTRACT: Modern supervised learning neural network models require a large amount of manually labeled data, which makes the construction of domain-specific knowledge graphs time-consuming and labor-intensive. In parallel, although there has been much research on named entity recognition and relation extraction based on distantly supervised learning, constructing a domain-specific knowledge graph from large collections of textual data without manual annotations is still an urgent problem to be solved. In response, we propose an integrated framework for adapting and re-learning knowledge graphs from one coarse domain (biomedical) to a finer-define domain (oncology). In this framework, we apply distant-supervision on cross-domain knowledge graph adaptation. Consequently, no manual data annotation is required to train the model. We introduce a novel iterative training strategy to facilitate the discovery of domain-specific named entities and triples.  Experimental results indicate that the proposed framework can perform domain adaptation and construction of knowledge graph efficiently.

## item_id: m_2091

TITLE: Probabilistic modeling the hidden layers of deep neural networks

ABSTRACT: In this paper, we demonstrate that the parameters of Deep Neural Networks (DNNs) cannot satisfy the i.i.d. prior assumption and activations being i.i.d. is not valid for all the hidden layers of DNNs. Hence, the Gaussian Process cannot correctly explain all the hidden layers of DNNs. Alternatively, we introduce a novel probabilistic representation for the hidden layers of DNNs in two aspects: (i) a hidden layer formulates a Gibbs distribution, in which neurons define the energy function, and (ii) the connection between two adjacent layers can be modeled by a product of experts model. Based on the probabilistic representation, we demonstrate that the entire architecture of DNNs can be explained as a Bayesian hierarchical model. Moreover, the proposed probabilistic representation indicates that DNNs have explicit regularizations defined by the hidden layers serving as prior distributions. Based on the Bayesian explanation for the regularization of DNNs, we propose a novel regularization approach to improve the generalization performance of DNNs. Simulation results validate the proposed theories. 

## item_id: m_2092

TITLE: Understanding the Mechanics and Dynamics of Memorisation in Large Language Models: A Case Study with Random Strings

ABSTRACT: Understanding whether and to what extent large language models (LLMs) have memorised training data has important implications for the privacy of its training data and the reliability of its generated output. In this work, we focus on the more foundational question of how LLMs memorise training data. To this end, we systematically train LLMs of different sizes to memorise random token strings of different lengths and different entropies (i.e., sampled from different alphabet distributions) and study their ability to recall the strings. We observe many striking memorisation dynamics including (i) memorisation in phases with the alphabet distributions in the random strings being learnt before their relative positions in the string are memorised and (ii) memorisation in parts at the granularity of individual tokens, but not necessarily in the order in which they appear in the string. Next, we investigate memorisation mechanics by checking to what extent different parts of a token’s prefix in the string are necessary and sufficient to recollect the token. We leverage our insights to explain the dynamics of memorising strings and we conclude by discussing the implications of our findings for quantifying memorisation.

## item_id: m_2093

TITLE: SMITE: Segment Me In TimE

ABSTRACT: Segmenting an object in a video presents significant challenges. Each pixel must be accurately labeled, and these labels must remain consistent across frames. The difficulty increases when the segmentation is with arbitrary granularity, meaning the number of segments can vary arbitrarily, and masks are defined based on only one or a few sample images. In this paper, we address this issue by employing a
pre-trained text to image diffusion model supplemented with an additional tracking mechanism. We demonstrate that our approach can effectively manage various segmentation scenarios and outperforms state-of-the-art alternatives. The project page is available at https://segment-me-in-time.github.io/

## item_id: m_2094

TITLE: Principled Weight Initialization for Hypernetworks

ABSTRACT: Hypernetworks are meta neural networks that generate weights for a main neural network in an end-to-end differentiable manner. Despite extensive applications ranging from multi-task learning to Bayesian deep learning, the problem of optimizing hypernetworks has not been studied to date. We observe that classical weight initialization methods like Glorot & Bengio (2010) and He et al. (2015), when applied directly on a hypernet, fail to produce weights for the mainnet in the correct scale. We develop principled techniques for weight initialization in hypernets, and show that they lead to more stable mainnet weights, lower training loss, and faster convergence.

## item_id: m_2095

TITLE: Stacking for Transfer Learning

ABSTRACT: In machine learning tasks, overtting frequently crops up when the number of samples of target domain is insufﬁcient, for the generalization ability of the classiﬁer is poor in this circumstance. To solve this problem, transfer learning utilizes the knowledge of similar domains to improve the robustness of the learner. The main idea of existing transfer learning algorithms is to reduce the dierence between domains by sample selection or domain adaptation. However, no matter what transfer learning algorithm we use, the difference always exists and the hybrid training of source and target data leads to reducing ﬁtting capability of the learner on target domain. Moreover, when the relatedness between domains is too low, negative transfer is more likely to occur. To tackle the problem, we proposed a two-phase transfer learning architecture based on ensemble learning, which uses the existing transfer learning algorithms to train the weak learners in the ﬁrst stage, and uses the predictions of target data to train the ﬁnal learner in the second stage. Under this architecture, the ﬁtting capability and generalization capability can be guaranteed at the same time. We evaluated the proposed method on public datasets, which demonstrates the effectiveness and robustness of our proposed method.

## item_id: m_2096

TITLE: Multi-modal Variational Encoder-Decoders

ABSTRACT: Recent advances in neural variational inference have facilitated efficient training of powerful directed graphical models with continuous latent variables, such as variational autoencoders. However, these models usually assume simple, uni-modal priors — such as the multivariate Gaussian distribution — yet many real-world data distributions are highly complex and multi-modal. Examples of complex and multi-modal distributions range from topics in newswire text to conversational dialogue responses. When such latent variable models are applied to these domains, the restriction of the simple, uni-modal prior hinders the overall expressivity of the learned model as it cannot possibly capture more complex aspects of the data distribution. To overcome this critical restriction, we propose a flexible, simple prior distribution which can be learned efficiently and potentially capture an exponential number of modes of a target distribution. We develop the multi-modal variational encoder-decoder framework and investigate the effectiveness of the proposed prior in several natural language processing modeling tasks, including document modeling and dialogue modeling.

## item_id: m_2097

TITLE: ELICIT: LLM Augmentation Via External In-context Capability

ABSTRACT: Enhancing the adaptive capabilities of large language models is a critical pursuit in both research and application.
Traditional fine-tuning methods require substantial data, computational resources, and specific capabilities, while in-context learning is limited by the need for appropriate demonstrations and efficient token usage.
    Inspired by the expression of in-context learned capabilities through task vectors and the concept of modular capability or knowledge, we propose ELICIT, a framework consisting of two modules designed to effectively store and reuse task vectors to enhance the diverse adaptive capabilities of models without additional training or inference tokens.
    Our comprehensive experiments and analysis demonstrate that our pipeline is highly transferable across different input formats, tasks, and model architectures.
    Externally storing and reusing vectors that represent in-context learned capabilities not only shows the potential to extract modular capabilities but also significantly enhances the performance, versatility, adaptability, and scalability of large language models, paving the way for more efficient and effective use of these models in a wide range of applications.

## item_id: m_2098

TITLE: Understanding the Initial Condensation of Convolutional Neural Networks

ABSTRACT: Previous research has shown that fully-connected neural networks with small initialization and gradient-based training methods exhibit a phenomenon known as condensation during training. This phenomenon refers to the input weights of hidden neurons condensing into isolated orientations during training, revealing an implicit bias towards simple solutions in the parameter space. However, the impact of neural network structure on condensation remains unknown. In this study, we study convolutional neural networks (CNNs) as the starting point to explore the distinctions in the condensation behavior compared to fully-connected neural networks. Theoretically, we firstly demonstrate that under gradient descent (GD) and the small initialization scheme, the convolutional kernels of a two-layer CNN condense towards a specific direction determined by the training samples within a given time period. Subsequently, we conduct a series of systematic experiments to substantiate our theory and confirm condensation in more general settings. These findings contribute to a preliminary understanding of the non-linear training behavior exhibited by CNNs.

## item_id: m_2099

TITLE: Linear Mode Connectivity in Multitask and Continual Learning

ABSTRACT: Continual (sequential) training and multitask (simultaneous) training are often attempting to solve the same overall objective: to find a solution that performs well on all considered tasks. The main difference is in the training regimes, where continual learning can only have access to one task at a time, which for neural networks typically leads to catastrophic forgetting. That is, the solution found for a subsequent task does not perform well on the previous ones anymore. 
    However, the relationship between the different minima that the two training regimes arrive at is not well understood. What sets them apart? Is there a local structure that could explain the difference in performance achieved by the two different schemes? 
    Motivated by recent work showing that different minima of the same task are typically connected by very simple curves of low error, we investigate whether multitask and continual solutions are similarly connected. We empirically find that indeed such connectivity can be reliably achieved and, more interestingly, it can be done by a linear path, conditioned on having the same initialization for both. We thoroughly analyze this observation and discuss its significance for the continual learning process.
    Furthermore, we exploit this finding to propose an effective algorithm that constrains the sequentially learned minima to behave as the multitask solution.  We show that our method outperforms several state of the art continual learning algorithms on various vision benchmarks.

## item_id: m_2100

TITLE: Robustness to Pruning Predicts Generalization in Deep Neural Networks

ABSTRACT: Why over-parameterized neural networks generalize as well as they do is a central concern of theoretical analysis in machine learning today. Following Occam's razor, it has long been suggested that simpler networks generalize better than more complex ones. Successfully quantifying this principle has proved difficult given that many measures of simplicity, such as parameter norms, grow with the size of the network and thus fail to capture the observation that larger networks tend to generalize better in practice.
In this paper, we introduce a new, theoretically motivated measure of a network's simplicity: the smallest fraction of the network's parameters that can be kept while pruning without adversely affecting its training loss. We show that this measure is highly predictive of a model's generalization performance across a large set of convolutional networks trained on CIFAR-10. Lastly, we study the mutual information between the predictions of our new measure and strong existing measures based on models' margin, flatness of minima and optimization speed. We show that our new measure is similar to -- but more predictive than -- existing flatness-based measures.
