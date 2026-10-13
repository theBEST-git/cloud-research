# Batch 12 — 100 items

## item_id: m_1101

TITLE: Is Deep Reinforcement Learning Really Superhuman on Atari? Leveling the playing field

ABSTRACT: Consistent and reproducible evaluation of Deep Reinforcement Learning (DRL) is not straightforward. In the Arcade Learning Environment (ALE), small changes in environment parameters such as stochasticity or the maximum allowed play time can lead to very different performance. In this work, we discuss the difficulties of comparing different agents trained on ALE. In order to take a step further towards reproducible and comparable DRL, we introduce SABER, a Standardized Atari BEnchmark for general Reinforcement learning algorithms. Our methodology extends previous recommendations and contains a complete set of environment parameters as well as train and test procedures. We then use SABER to evaluate the current state of the art, Rainbow. Furthermore, we introduce a human world records baseline, and argue that previous claims of expert or superhuman performance of DRL might not be accurate. Finally, we propose Rainbow-IQN by extending Rainbow with Implicit Quantile Networks (IQN) leading to new state-of-the-art performance. Source code is available for reproducibility.

## item_id: m_1102

TITLE: Weakly-Supervised Domain Adaptation in Federated Learning

ABSTRACT: Federated domain adaptation (FDA) describes the setting where a set of source clients seek to optimize the performance of a target client. To be effective, FDA must address some of the distributional challenges of Federated learning (FL). For instance, FL systems exhibit distribution shifts across clients. Further, labeled data are not always available among the clients. To this end, we propose and compare novel approaches for FDA, combining the few labeled target samples with the source data when auxiliary labels are available to the clients. The in-distribution auxiliary information is included during local training to boost out-of-domain accuracy. Also, during fine-tuning, we devise a simple yet efficient gradient projection method to detect the valuable components from each source client model towards the target direction. The extensive experiments on medical imaging datasets show that our proposed framework significantly improves federated domain adaptation performance.

## item_id: m_1103

TITLE: Membership Leakage in Pre-trained Language Models

ABSTRACT: Pre-trained language models are becoming a dominating component in NLP domain and have achieved state-of-the-art in various downstream tasks. Recent research has shown that language models are vulnerable to privacy leakage of their training data, such as text extraction and membership leakage. However, existing works against NLP applications mainly focus on the privacy leakage of text generation and downstream classification, and the privacy leakage of pre-trained language models is largely unexplored. In this paper, we take the first step toward systematically auditing the privacy risks of pre-trained language models through the lens of membership leakage. In particular, we focus on membership leakage of pre-training data in the exposure of downstream models adapted from pre-trained language models. We conduct extensive experiments on a variety of pre-trained model architectures and different types of downstream tasks. Our empirical evaluations demonstrate that membership leakage of pre-trained language models exists even when only the downstream model output is exposed, thereby posing a more severe risk than previously thought. We further conduct sophisticated ablation studies to analyze the relationship between membership leakage of pre-trained models and the characteristic of downstream tasks, which can guide developers or researchers to be vigilant about the vulnerability of pre-trained language models. Lastly, we explore possible defenses against membership leakage of PLMs and propose two promising defenses based on empirical evaluations.

## item_id: m_1104

TITLE: Practical Memorization Tests for Detecting Copyrighted Data in Large Language Models

ABSTRACT: Large language models (LLMs) have been shown to reproduce copyrighted text, e.g., passages from news articles, sparking high-profile lawsuits against their providers. Yet copyright claims often rely on anecdotal evidence. To strengthen such cases, there is a clear need for automated, interpretable, and reliable methods to detect repetitions that are also suitable in legal proceedings. Current methods often equate an LLM’s ability to complete prefixes from source passages with memorization, but this metric fails when strong completions arise from generalization. We identify four key criteria for practical real-world deployment: methods must operate with only black-box access to the LLM, while remaining reliable (high precision), efficient, and interpretable. We first investigate prior work and find simple non-memorized counterexamples that trigger false positives even in advanced methods designed to account for generalization, undermining their reliability in legal contexts. Going further, we introduce DualTest, which requires only a single API call per passage under test and produces human-interpretable results. Our key insight is to leverage a small proxy model to disentangle memorization from generalization in counterexamples, improving recall by up to 3\% compared to the strongest baseline.

## item_id: m_1105

TITLE: MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes

ABSTRACT: 4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly rasterizer, enabling rapid rendering speeds. Despite its advantages, 4DGS faces significant challenges, notably the requirement of millions of 4D Gaussians, each with extensive associated attributes, leading to substantial memory and storage cost. This paper introduces a memory-efficient framework for 4DGS. We streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. This approach eliminates the need for spherical harmonics coefficients, which typically involve up to 144 parameters in classic 4DGS, thereby creating a memory-efficient 4D Gaussian representation. Furthermore, we introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit the number of Gaussians, thus forcing our model to use as few Gaussians as possible to fit a dynamic scene well. With simple half-precision storage and zip compression, our framework achieves a storage reduction by approximately 190$\times$ and 125$\times$ on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. Meanwhile, it maintains comparable rendering speeds and scene representation quality, setting a new standard in the field.

## item_id: m_1106

TITLE: For self-supervised learning, Rationality implies generalization, provably

ABSTRACT: We prove a new upper bound on the generalization gap of classifiers that are obtained by first using self-supervision to learn a representation $r$ of the training~data, and then fitting a simple (e.g., linear) classifier $g$ to the labels. Specifically, we show that (under the assumptions described below) the generalization gap of such classifiers tends to zero if $\mathsf{C}(g) \ll n$, where $\mathsf{C}(g)$ is an appropriately-defined measure of the simple classifier $g$'s complexity, and $n$ is the number of training samples. We stress that our bound is independent of the complexity of the representation $r$. 
We do not make any structural or conditional-independence  assumptions on the representation-learning task, which can use the same training dataset that is later used for classification. Rather, we assume that the training procedure satisfies certain natural noise-robustness (adding small amount of label noise causes small degradation in performance) and rationality  (getting the wrong label is not better than getting no label at all) conditions that widely hold across many standard architectures.
We also conduct an extensive empirical study of the generalization gap and the quantities used in our assumptions for a variety of self-supervision based algorithms, including SimCLR, AMDIM and BigBiGAN,  on the CIFAR-10 and ImageNet datasets. We show that, unlike standard supervised classifiers, these algorithms display small generalization gap, and the bounds we prove on this gap are often non vacuous. 

## item_id: m_1107

TITLE: Robust And Interpretable Blind Image Denoising Via Bias-Free Convolutional Neural Networks

ABSTRACT: We study the generalization properties of deep convolutional neural networks for image denoising in the presence of varying noise levels. We provide extensive empirical evidence that current state-of-the-art architectures systematically overfit to the noise levels in the training set, performing very poorly at new noise levels. We show that strong generalization can be achieved through a simple architectural modification: removing all additive constants. The resulting "bias-free" networks attain state-of-the-art performance over a broad range of noise levels, even when trained over a limited range. They are also locally linear, which enables direct analysis with linear-algebraic tools.  We show that the denoising map can be visualized locally as a filter that adapts to both image structure and noise level. In addition, our analysis reveals that deep networks implicitly perform a projection onto an adaptively-selected low-dimensional subspace, with dimensionality inversely proportional to noise level, that captures features of natural images. 

## item_id: m_1108

TITLE: Progressive Fourier Neural Representation for Sequential Video Compilation

ABSTRACT: Neural Implicit Representation (NIR) has recently gained significant attention due to its remarkable ability to encode complex and high-dimensional data into representation space and easily reconstruct it through a trainable mapping function. However, NIR methods assume a one-to-one mapping between the target data and representation models regardless of data relevancy or similarity. This results in poor generalization over multiple complex data and limits their efficiency and scalability. Motivated by continual learning, this work investigates how to accumulate and transfer neural implicit representations for multiple complex video data over sequential encoding sessions. To overcome the limitation of NIR, we propose a novel method, Progressive Fourier Neural Representation (PFNR), that aims to find an adaptive and compact sub-module in Fourier space to encode videos in each training session. This sparsified neural encoding allows the neural network to hold free weights, enabling an improved adaptation for future videos. In addition, when learning a representation for a new video, PFNR transfers the representation of previous videos with frozen weights. This design allows the model to continuously accumulate high-quality neural representations for multiple videos while ensuring lossless decoding that perfectly preserves the learned representations for previous videos. We validate our PFNR method on the UVG8/17 and DAVIS50 video sequence benchmarks and achieve impressive performance gains over strong continual learning baselines.

## item_id: m_1109

TITLE: A Differentiable Physics Engine for Deep Learning in Robotics

ABSTRACT: One of the most important fields in robotics is the optimization of controllers. Currently, robots are often treated as a black box in this optimization process, which is the reason why derivative-free optimization methods such as evolutionary algorithms or reinforcement learning are omnipresent. When gradient-based methods are used, models are kept small or rely on finite difference approximations for the Jacobian. This method quickly grows expensive with increasing numbers of parameters, such as found in deep learning. We propose an implementation of a modern physics engine, which can differentiate control parameters. This engine is implemented for both CPU and GPU. Firstly, this paper shows how such an engine speeds up the optimization process, even for small problems. Furthermore, it explains why this is an alternative approach to deep Q-learning, for using deep learning in robotics. Finally, we argue that this is a big step for deep learning in robotics, as it opens up new possibilities to optimize robots, both in hardware and software.

## item_id: m_1110

TITLE: Significance of Softmax-Based Features over Metric Learning-Based Features

ABSTRACT: The extraction of useful deep features is important for many computer vision tasks.
Deep features extracted from classification networks have proved to perform well in those tasks.
To obtain features of greater usefulness, end-to-end distance metric learning (DML) has been applied to train the feature extractor directly.
End-to-end DML approaches such as Magnet Loss and lifted structured feature embedding show state-of-the-art performance in several image recognition tasks.
However, in these DML studies, there were no equitable comparisons between features extracted from a DML-based network and those from a softmax-based network.
In this paper, by presenting objective comparisons between these two approaches under the same network architecture, we show that the softmax-based features are markedly better than the state-of-the-art DML features for tasks such as fine-grained recognition, attribute estimation, clustering, and retrieval.

## item_id: m_1111

TITLE: Deep autoregressive density nets vs neural ensembles for model-based offline reinforcement learning

ABSTRACT: We consider the problem of offline reinforcement learning where only a set of system transitions is made available for policy optimization. Following recent advances in the field, we consider a model-based reinforcement learning algorithm that infers the system dynamics from the available data and performs policy optimization on imaginary model rollouts. This approach is vulnerable to exploiting model errors which can lead to catastrophic failures on the real system. The standard solution is to rely on ensembles for uncertainty heuristics and to avoid exploiting the model where it is too uncertain. We challenge the popular belief that we must resort to ensembles by showing that better performance can be obtained with a single well-calibrated autoregressive model on the D4RL benchmark. We also analyze static metrics of model-learning and conclude on the important model properties for the final performance of the agent.

## item_id: m_1112

TITLE: Theoretical bounds on estimation error for meta-learning

ABSTRACT: Machine learning models have traditionally been developed under the assumption that the training and test distributions match exactly. However, recent success in few-shot learning and related problems are encouraging signs that these models can be adapted to more realistic settings where train and test distributions differ. Unfortunately, there is severely limited theoretical support for these algorithms and little is known about the difficulty of these problems. In this work, we provide novel information-theoretic lower-bounds on minimax rates of convergence for algorithms that are trained on data from multiple sources and tested on novel data. Our bounds depend intuitively on the information shared between sources of data, and characterize the difficulty of learning in this setting for arbitrary algorithms. We demonstrate these bounds on a hierarchical Bayesian model of meta-learning, computing both upper and lower bounds on parameter estimation via maximum-a-posteriori inference.

## item_id: m_1113

TITLE: VisualPRM400K: An Effective Dataset for Training Multimodal Process Reward Models

ABSTRACT: We construct VisualPRM400K, a dataset comprising about 400K multimodal process supervision data. Building upon this dataset, we develop VisualPRM, an advanced multimodal Process Reward Model (PRM) capable of estimating the value score of each step during the reasoning process.
Under the Best-of-N evaluation setting, our model improves the reasoning performance of three types of MLLMs and four different model scales. 
Even when applied to the highly capable InternVL2.5-78B, it achieves a 5.9-point improvement across seven multimodal reasoning benchmarks.
Experimental results show that the PRM model trained on our VisualPRM400K exhibits superior performance compared to Outcome Reward Models and Self-Consistency during BoN evaluation.
To further facilitate the development of multimodal PRMs, we construct VisualProcessBench, a benchmark designed to measure the abilities of PRMs and MLLMs to detect incorrect steps in multimodal reasoning tasks.
We hope that our work can inspire more future research and contribute to the development of MLLMs. Our model, data, and benchmark will be released.

## item_id: m_1114

TITLE: Learning Physics Priors for Deep Reinforcement Learing

ABSTRACT: While model-based deep reinforcement learning (RL) holds great promise for sample efficiency and generalization, learning an accurate dynamics model is challenging and often requires substantial interactions with the environment. Further, a wide variety of domains have dynamics that share common foundations like the laws of physics, which are rarely exploited by these algorithms. Humans often acquire such physics priors that allow us to easily adapt to the dynamics of any environment. In this work, we propose an approach to learn such physics priors and incorporate them into an RL agent. Our method involves pre-training a frame predictor on raw videos and then using it to initialize the dynamics prediction model on a target task. Our prediction model, SpatialNet, is designed to implicitly capture localized physical phenomena and interactions.  We show the value of incorporating this prior through empirical experiments on two different domains – a newly created PhysWorld and games from the Atari benchmark, outperforming competitive approaches and demonstrating effective transfer learning.

## item_id: m_1115

TITLE: Why Music Moves Us: A Computational Model of Aesthetic Experience and Creativity via Meta-Learned Active Inference

ABSTRACT: This paper directly confronts the fundamental aesthetic question, "Why is music beautiful?", by proposing a computable and unified theoretical framework. Grounded in Active Inference and the Free Energy Principle, we formalize aesthetic pleasure as the rate at which a generative model successfully reduces its prediction cost (variational free energy). This principle offers a computational answer to why a song by Taylor Swift can be profoundly pleasing, while a monotonous bell is boring and chaotic noise is aversive. We posit that aesthetically pleasing music maximizes this rate of free energy reduction, creating a dynamic akin to a rapid descent down a smooth slide. In contrast, monotony represents a flat plane with no descent, and chaos a rugged path where no progress can be made. To operationalize this theory, we propose that the formation of musical taste is a meta-learning process, for which this "aesthetic pleasure" serves as the intrinsic learning signal. Based on this, we design and implement the Aesthetic Priors Meta-Learner (APML), a novel dual-core generative engine. APML's decoupled design, featuring a large-scale knowledge backbone and a lightweight aesthetic core, achieves an AI that, for the first time, not only possesses musical knowledge but also makes intrinsic aesthetic judgments. For rigorous evaluation, we constructed the first meta-learning benchmark for few-shot music style transfer. Experimental results show that APML achieves state-of-the-art performance on core challenges of this task, particularly in stylistic consistency and musicality, while also demonstrating unprecedented alignment with our proposed theory-driven metrics (e.g., the rate of free energy reduction). This provides powerful empirical support for the validity of our theory, showing that optimizing for the dynamics of learning itself leads to more aesthetically aligned and adaptive generative agents.

## item_id: m_1116

TITLE: COptiDICE: Offline Constrained Reinforcement Learning via Stationary Distribution Correction Estimation

ABSTRACT: We consider the offline constrained reinforcement learning (RL) problem, in which the agent aims to compute a policy that maximizes expected return while satisfying given cost constraints, learning only from a pre-collected dataset. This problem setting is appealing in many real-world scenarios, where direct interaction with the environment is costly or risky, and where the resulting policy should comply with safety constraints. However, it is challenging to compute a policy that guarantees satisfying the cost constraints in the offline RL setting, since the off-policy evaluation inherently has an estimation error. In this paper, we present an offline constrained RL algorithm that optimizes the policy in the space of the stationary distribution. Our algorithm, COptiDICE, directly estimates the stationary distribution corrections of the optimal policy with respect to returns, while constraining the cost upper bound, with the goal of yielding a cost-conservative policy for actual constraint satisfaction. Experimental results show that COptiDICE attains better policies in terms of constraint satisfaction and return-maximization, outperforming baseline algorithms.

## item_id: m_1117

TITLE: Probing Emergent Semantics in Predictive Agents via Question Answering

ABSTRACT: Recent work has demonstrated how predictive modeling can endow agents with rich knowledge of their surroundings, improving their ability to act in complex environments. We propose question-answering as a general paradigm to decode and understand the representations that such agents develop, applying our method to two recent approaches to predictive modeling – action-conditional CPC (Guo et al., 2018) and SimCore (Gregor et al., 2019). After training agents with these predictive objectives in a visually-rich, 3D environment with an assortment of objects, colors, shapes, and spatial configurations, we probe their internal state representations with a host of synthetic (English) questions, without backpropagating gradients from the question-answering decoder into the agent. The performance of different agents when probed in this way reveals that they learn to encode detailed, and seemingly compositional, information about objects, properties and spatial relations from their physical environment. Our approach is intuitive, i.e. humans can easily interpret the responses of the model as opposed to inspecting continuous vectors, and model-agnostic, i.e. applicable to any modeling approach. By revealing the implicit knowledge of objects, quantities, properties and relations acquired by agents as they learn, question-conditional agent probing can stimulate the design and development of stronger predictive learning objectives.

## item_id: m_1118

TITLE: Asynchronous Advantage Actor Critic: Non-asymptotic Analysis and Linear Speedup

ABSTRACT: Asynchronous and parallel implementation of standard reinforcement learning (RL) algorithms is a key enabler of the tremendous success of modern RL. 
Among many asynchronous RL algorithms, arguably the most popular and effective one is the asynchronous advantage actor-critic (A3C) algorithm.  
Although A3C is becoming the workhorse of RL, its theoretical properties are still not well-understood, including the non-asymptotic analysis and the performance gain of parallelism (a.k.a. speedup). 
This paper revisits the A3C algorithm with TD(0) for the critic update, termed A3C-TD(0), with provable convergence guarantees. 
With linear value function approximation for the TD update, the convergence of A3C-TD(0) is established under both i.i.d. and Markovian sampling. Under i.i.d. sampling, A3C-TD(0) obtains sample complexity of $\mathcal{O}(\epsilon^{-2.5}/N)$ per worker to achieve $\epsilon$ accuracy, where $N$ is the number of workers.  Compared to the best-known sample complexity of $\mathcal{O}(\epsilon^{-2.5})$ for two-timescale AC, A3C-TD(0) achieves \emph{linear speedup}, which justifies the advantage of parallelism and asynchrony in AC algorithms theoretically for the first time.
Numerical tests on synthetically generated instances and OpenAI Gym environments have been provided to verify our theoretical analysis. 

## item_id: m_1119

TITLE: Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking

ABSTRACT: Large Reasoning Models (LRMs) have achieved impressive performance on challenging tasks, yet their deep reasoning often incurs substantial computational costs. To achieve efficient reasoning, existing reinforcement learning methods still struggle to construct short reasoning path during the rollout stage, limiting effective learning. Inspired by Evidence Accumulation Models, we find that LRMs have accumulated sufficient information early in reasoning, making further reasoning steps redundant. Based on this insight, we propose Just-Enough Thinking (JET), which trains models to proactively terminate unnecessary reasoning. JET performs trajectory truncation during rollout to expose the model to short, distributionally consistent reasoning paths. Besides, it uses a quality-controlled length reward to better encourage concise reasoning while maintaining correctness. Extensive experiments demonstrate that JET significantly improves reasoning efficiency without sacrificing accuracy. In particular, JET delivers a 4.6% accuracy improvement while reducing the output length by 46.3% on the Olympiad benchmark using DeepSeek-R1-Distill-Qwen-1.5B. Our code is available in the GitHub.

## item_id: m_1120

TITLE: Neural Networks with Structural Resistance to Adversarial Attacks

ABSTRACT: In adversarial attacks to machine-learning classifiers, small perturbations are added to input that is correctly classified. The perturbations yield adversarial examples, which are virtually indistinguishable from the unperturbed input, and yet are misclassified. In standard neural networks used for deep learning, attackers can craft adversarial examples from most input to cause a misclassification of their choice. 

We introduce a new type of network units, called RBFI units, whose non-linear structure makes them inherently resistant to adversarial attacks. On permutation-invariant MNIST, in absence of adversarial attacks, networks using RBFI units match the performance of networks using sigmoid units, and are slightly below the accuracy of networks with ReLU units. When subjected to adversarial attacks based on projected gradient descent or fast gradient-sign methods, networks with RBFI units retain accuracies above 75%, while ReLU or Sigmoid see their accuracies reduced to below 1%.
Further, RBFI networks trained on regular input either exceed or closely match the accuracy of sigmoid and ReLU network trained with the help of adversarial examples.

The non-linear structure of RBFI units makes them difficult to train using standard gradient descent. We show that RBFI networks of RBFI units can be efficiently trained to high accuracies using pseudogradients, computed using functions especially crafted to facilitate learning instead of their true derivatives.


## item_id: m_1121

TITLE: FastGRPO: Accelerating Policy Optimization via Concurrency-aware Speculative Decoding and Online Draft Learning

ABSTRACT: Group relative policy optimization (GRPO) has demonstrated significant potential in improving the reasoning capabilities of large language models (LLMs) via reinforcement learning. However, its practical deployment is impeded by an excessively slow training process, primarily attributed to the computationally intensive autoregressive generation of multiple responses per query, which makes the generation phase the primary performance bottleneck. Although speculative decoding presents a promising direction for acceleration, its direct application in GRPO achieves limited speedup under high-concurrency training conditions. To overcome this limitation, we propose a concurrency-aware speculative decoding framework that dynamically adjusts the drafting and verification strategy according to real-time concurrency levels, thereby maximizing the acceleration of the generation process. Furthermore, to address performance degradation arising from distributional drift between the evolving target model and the fixed draft model during training, we introduce an online draft learning mechanism that enables the draft model to continuously adapt using feedback signals from the target model. Experimental results across multiple mathematical reasoning datasets and models demonstrate that the proposed method achieves end-to-end speedups of 2.35x to 2.72x, significantly surpassing baseline approaches in efficiency. The code is available at https://github.com/yedaotian9/FastGRPO.

## item_id: m_1122

TITLE: An Information Retrieval Approach for Finding Dependent Subspaces of Multiple Views

ABSTRACT: Finding relationships between multiple views of data is essential both in exploratory analysis and as pre-processing for predictive tasks. A prominent approach is to apply variants of Canonical Correlation Analysis (CCA), a classical method seeking correlated components between views. The basic CCA is restricted to maximizing a simple dependency criterion, correlation, measured directly between data coordinates. We introduce a new method that finds dependent subspaces of views directly optimized for the data analysis task of neighbor retrieval between multiple views. We optimize mappings for each view such as linear transformations to maximize cross-view similarity between neighborhoods of data samples. The criterion arises directly from the well-defined retrieval task, detects nonlinear and local similarities, measures dependency of data relationships rather than only individual data coordinates, and is related to well understood measures of information retrieval quality. In experiments the proposed method outperforms alternatives in preserving cross-view neighborhood similarities, and yields insights into local dependencies between multiple views.

## item_id: m_1123

TITLE: Recycling the discriminator for improving the inference mapping of GAN

ABSTRACT: Generative adversarial networks (GANs) have achieved outstanding success in generating the high-quality data. Focusing on the generation process, existing GANs learn a unidirectional mapping from the latent vector to the data. Later, various studies point out that the latent space of GANs is semantically meaningful and can be utilized in advanced data analysis and manipulation. In order to analyze the real data in the latent space of GANs, it is necessary to investigate the inverse generation mapping from the data to the latent vector. To tackle this problem, the bidirectional generative models introduce an encoder to establish the inverse path of the generation process. Unfortunately, this effort leads to the degradation of generation quality because the imperfect generator rather interferes the encoder training and vice versa. 
In this paper, we propose an effective algorithm to infer the latent vector based on existing unidirectional GANs by preserving their generation quality.
It is important to note that we focus on increasing the accuracy and efficiency of the inference mapping but not influencing the GAN performance (i.e., the quality or the diversity of the generated sample).
Furthermore, utilizing the proposed inference mapping algorithm, we suggest a new metric for evaluating the GAN models by measuring the reconstruction error of unseen real data.
The experimental analysis demonstrates that the proposed algorithm achieves more accurate inference mapping than the existing method and provides the robust metric for evaluating GAN performance. 

## item_id: m_1124

TITLE: A Boo(n) for Evaluating Architecture Performance

ABSTRACT: We point out important problems with the common practice of using the best single model performance for comparing deep learning architectures, and we propose a method that corrects these flaws. Each time a model is trained, one gets a different result due to random factors in the training process, which include random parameter initialization and random data shuffling. Reporting the best single model performance does not appropriately address this stochasticity. We propose a normalized expected best-out-of-n performance (Boo_n) as a way to correct these problems.

## item_id: m_1125

TITLE: $\texttt{MirrorCheck}$ : Efficient Adversarial Defense for Vision-Language Models

ABSTRACT: Vision-Language Models (VLMs) are becoming increasingly vulnerable to adversarial attacks as various novel attack strategies are being proposed against these models. While existing defenses excel in unimodal contexts, they currently fall short in safeguarding VLMs against adversarial threats. To mitigate this vulnerability, we propose a novel, yet elegantly simple approach for detecting adversarial samples in VLMs. Our method leverages Text-to-Image (T2I) models to generate images based on captions produced by target VLMs. Subsequently, we calculate the similarities of the embeddings of both input and generated images in the feature space to identify adversarial samples. Empirical evaluations conducted on different datasets validate the efficacy of our approach, outperforming baseline methods adapted from image classification domains. Furthermore, we extend our methodology to classification tasks, showcasing its adaptability and model-agnostic nature. Empirical findings also show the resilience of our approach against adaptive attacks, positioning it as an excellent defense mechanism for real-world deployment against adversarial threats.

## item_id: m_1126

TITLE: VARIATIONAL SGD: DROPOUT , GENERALIZATION AND CRITICAL POINT AT THE END OF CONVEXITY

ABSTRACT: The goal of the paper is to propose an algorithm for learning the most generalizable solution from given training data. It is shown that Bayesian approach leads to a solution that dependent on statistics of training data and not on particular
samples. The solution is stable under perturbations of training data because it is defined by an integral contribution of multiple maxima of the likelihood and not by a single global maximum. Specifically, the Bayesian probability distribution
of parameters (weights) of a probabilistic model given by a neural network is estimated via recurrent variational approximations. Derived recurrent update rules correspond to SGD-type rules for finding a minimum of an effective loss that is an average of an original negative log-likelihood over the Gaussian distributions of weights, which makes it a function of means and variances. The effective loss is convex for large variances and non-convex in the limit of small variances. Among stationary solutions of the update rules there are trivial solutions with zero variances at local minima of the original loss and a single non-trivial solution with finite variances that is a critical point at the end of convexity of the effective loss
in the mean-variance space. At the critical point both first- and second-order gradients of the effective loss w.r.t. means are zero. The empirical study confirms that the critical point represents the most generalizable solution. While the location of
the critical point in the weight space depends on specifics of the used probabilistic model some properties at the critical point are universal and model independent.

## item_id: m_1127

TITLE: A Deep Learning Approach for Joint Video Frame and Reward Prediction in Atari Games

ABSTRACT: Reinforcement learning is concerned with learning to interact with environments that are initially unknown. State-of-the-art reinforcement learning approaches, such as DQN, are model-free and learn to act effectively across a wide range of environments such as Atari games, but require huge amounts of data. Model-based techniques are more data-efficient, but need to acquire explicit knowledge about the environment dynamics or the reward structure. 

In this paper we take a step towards using model-based techniques in environments with high-dimensional visual state space when system dynamics and the reward structure are both unknown and need to be learned, by demonstrating that it is possible to learn both jointly.
Empirical evaluation on five Atari games demonstrate accurate cumulative reward prediction of up to 200 frames. We consider these positive results as opening up important directions for model-based RL in complex, initially unknown environments.

## item_id: m_1128

TITLE: Event-Anchored Frame Selection for Efficient Long-Video Understanding

ABSTRACT: Massive frame redundancy and limited context window make efficient frame selection crucial for long-video understanding with large vision-language models (LVLMs). Prevailing approaches, however, adopt a flat sampling paradigm which treats the video as an unstructured collection of frames. In this paper, we introduce $\textbf{E}$vent-Anchored $\textbf{F}$rame $\textbf{S}$election $\textbf{(EFS)}$, a hierarchical, event-aware pipeline. Leveraging self-supervised DINO embeddings, EFS first partitions the video stream into visually homogeneous temporal segments, which serve as proxies for semantic events. Within each event, it then selects the most query-relevant frame as an anchor. These anchors act as structural priors that guide a global refinement stage using an adaptive Maximal Marginal Relevance (MMR) scheme. This pipeline ensures the final keyframe set jointly optimizes for event coverage, query relevance, and visual diversity. As a $\textbf{training-free, plug-and-play module,}$ EFS can be seamlessly integrated into off-the-shelf LVLMs, yielding substantial gains on challenging video understanding benchmarks. Specifically, when applied to LLaVA-Video-7B, EFS improves accuracy by $\textbf{4.7\\%, 4.9\\%, and 8.8\\%}$ on VideoMME, LongVideoBench, and MLVU, respectively. Code is provided in the supplementary material and will be released publicly.

## item_id: m_1129

TITLE: Learning to Recover from Failures using Memory

ABSTRACT: Learning from past mistakes is a quintessential aspect of intelligence. In sequential decision-making, existing meta-learning methods that learn a learning algorithm utilize experience from only a few previous episodes to adapt their policy to new environments and tasks. Such methods must learn to correct their mistakes from highly-correlated sequences of states and actions generated by the same policy's consequent roll-outs during training. Learning from correlated data is known to be problematic and can significantly impact the quality of the learned correction mechanism. We show that this problem can be mitigated by augmenting current systems with an external memory bank that stores a larger and more diverse set of past experiences. Detailed experiments demonstrate that our method outperforms existing meta-learning algorithms on a suite of challenging tasks from raw visual observations.

## item_id: m_1130

TITLE: Reward Shaping Control Variates for Off-Policy Evaluation Under Sparse Rewards

ABSTRACT: Off-policy evaluation (OPE) is essential for deploying reinforcement learning in safety-critical settings, yet existing estimators such as importance sampling and doubly robust (DR) often exhibit prohibitively high variance when rewards are sparse. In this work, we introduce Reward-Shaping Control Variates, a new family of unbiased estimators that leverage potential-based reward shaping to construct additional zero-mean control variates. We prove that shaped estimators always yields valid variance reduction, and that combining shaping-based and Q-based control variates strictly expands the variance-reduction subspace beyond DR and its minimax variant MRDR. Empirically, we provide a systematic regime map across synthetic chains, a cancer simulator, and an ICU-sepsis benchmark showing that shaping-based OPE consistently outperforms DR in sparse-reward settings, while a hybrid estimator achieves state-of-the-art performance across sparse, noisy, and misspecified environments. Our results highlight reward shaping as a powerful and interpretable tool for robust OPE, offering both theoretical guarantees and practical improvements in domains where standard estimators fail.

## item_id: m_1131

TITLE: Weight Expansion: A New Perspective on Dropout and Generalization

ABSTRACT: While dropout is known to be a successful regularization technique, insights into the mechanisms that lead to this success are still lacking. We introduce the concept of “weight expansion”, an increase in the signed volume of a parallelotope spanned by the column or row vectors of the weight covariance matrix, and show that weight expansion is an effective means of increasing the generalization in a PAC-Bayesian setting. We provide a theoretical argument that dropout leads to weight expansion and extensive experimental support for the correlation between dropout and weight expansion. To support our hypothesis that weight expansion should be regarded as the cause for the increased generalization capacity obtained by using dropout, and not just as a mere by-product, we have studied other methods that achieve weight expansion (resp. contraction), and found that they generally lead to an increased (resp. decreased) generalization ability. This suggests that dropout is an attractive regularizer because it is a computationally cheap method for obtaining weight expansion. This insight justifies the role of dropout as a regularizer, while paving the way for identifying regularizers that promise improved generalization through weight expansion.

## item_id: m_1132

TITLE: Do Androids Dream of Electric Fences? Safety-Aware Reinforcement Learning with Latent Shielding

ABSTRACT: The growing trend of fledgling reinforcement learning systems making their way into real-world applications has been accompanied by growing concerns for their safety and robustness. In recent years, a variety of approaches have been put forward to address the challenges of safety-aware reinforcement learning; however, these methods often either require a handcrafted model of the environment to be provided beforehand, or that the environment is relatively simple and low-dimensional. We present a novel approach to safety-aware deep reinforcement learning in high-dimensional environments called latent shielding. Latent shielding leverages internal representations of the environment learnt by model-based agents to "imagine" future trajectories and avoid those deemed unsafe. We experimentally demonstrate that this approach leads to improved adherence to formally-defined safety specifications.

## item_id: m_1133

TITLE: Surgical Prediction with Interpretable Latent Representation

ABSTRACT: Given the risks and cost of surgeries, there has been significant interest in exploiting predictive models to improve perioperative care. However, due to the high dimensionality and noisiness of perioperative data, it is challenging to develop accurate, robust and interpretable encoding for surgical applications. We propose surgical VAE (sVAE), a representation learning framework for perioperative data based on variational autoencoder (VAE). sVAE provides a holistic approach combining two salient features tailored for surgical applications. To overcome performance limitations of traditional VAE, it is prediction-guided with explicit expression of predicted outcome in the latent representation. Furthermore, it disentangles the latent space so that it can be interpreted in a clinically meaningful fashion. We apply sVAE to two real-world perioperative datasets and the open MIMIC-III dataset to evaluate its efficacy and performance in  predicting diverse outcomes including surgery duration, postoperative complication, ICU duration, and mortality. Our results show that the latent representation provided by sVAE leads to superior performance in classification, regression and multi-task predictions. We further demonstrate the interpretability of the disentangled representation and its capability to capture intrinsic characteristics of surgical patients.

## item_id: m_1134

TITLE: Deep Error-Correcting Output Codes

ABSTRACT: Existing deep networks are generally initialized with unsupervised methods, such as random assignments and greedy layerwise pre-training. This may result in the whole training process (initialization/pre-training + fine-tuning) to be very time consuming. In this paper, we combine the ideas of ensemble learning and deep learning, and present a novel deep learning framework called deep error-correcting output codes (DeepECOC). DeepECOC are composed of multiple layers of the ECOC module, which combines multiple binary classifiers for feature learning. Here, the weights learned for the binary classifiers can be considered as weights between two successive layers, while the outputs of the combined binary classifiers as the outputs of a hidden layer. On the one hand, the ECOC modules can be learned using given supervisory information, and on the other hand, based on the ternary coding design, the weights can be learned only using part of the training data. Hence, the supervised pre-training of DeepECOC is in general very effective and efficient. We have conducted extensive experiments to compare DeepECOC with traditional ECOC, feature learning and deep learning algorithms on several benchmark data sets. The results demonstrate that DeepECOC perform not only better than traditional ECOC and feature learning algorithms, but also state-of the-art deep learning models in most cases. 

## item_id: m_1135

TITLE: Investigating Language Models for Supporting Complex Group Decisions

ABSTRACT: Reaching consensus is a central challenge in group decision making as agreement needs to be balanced with diversity of perspectives. Recent AI advances have opened new possibilities for synthesizing complex information and facilitating consensus. We study group decision processes by modeling the complexity of the decision surface, defined by a set of decision problems, each with multiple options. Each solution yields a gain for every participant, and the objective of deliberation is to ensure fairness by equalizing participants’ profits. We explore multiple settings: whether gains are private, arbitrary numbers, or ordered sequences; whether the exact gain for each option is public; and whether group communication is expressed in natural language or numerically. Group coordination is facilitated by an AI agent powered by a large language model (LLM). We find that reasoning LLM models perform better than non-reasoning models and that a constraint solver (CPLEX) or a reinforcement learning agent (MCTS) improves the quality of the decision. The performance of reasoning models carries over when the participants rank order their preferences instead of assigning numeric scores. Numeric feedback leads to higher quality solutions than verbal feedback and is also better than when participants state their preference between two decisions. Our findings suggest that while LLMs show promise in facilitating consensus, there remains significant room for improvement in their ability to fully capture and reason over group consensus involving numerical outcomes.

## item_id: m_1136

TITLE: Batch Normalization has Multiple Benefits: An Empirical Study on Residual Networks

ABSTRACT: Many state of the art models rely on two architectural innovations; skip connections and batch normalization. However batch normalization has a number of limitations. It breaks the independence between training examples within a batch, performs poorly when the batch size is too small, and significantly increases the cost of computing a parameter update in some models. This work identifies two practical benefits of batch normalization. First, it improves the final test accuracy. Second, it enables efficient training with larger batches and larger learning rates. However we demonstrate that the increase in the largest stable learning rate does not explain why the final test accuracy is increased under a finite epoch budget. Furthermore, we show that the gap in test accuracy between residual networks with and without batch normalization can be dramatically reduced by improving the initialization scheme. We introduce “ZeroInit”, which trains a 1000 layer deep Wide-ResNet without normalization to 94.3% test accuracy on CIFAR-10 in 200 epochs at batch size 64. This initialization scheme outperforms batch normalization when the batch size is very small, and is competitive with batch normalization for batch sizes that are not too large. We also show that ZeroInit matches the validation accuracy of batch normalization when training ResNet-50-V2 on ImageNet at batch size 1024.

## item_id: m_1137

TITLE: Efficient Diffusion Models for Symmetric Manifolds

ABSTRACT: We present a  framework for designing  efficient diffusion models on symmetric Riemannian manifolds, which include the  torus, sphere, special orthogonal group, and unitary group. While diffusion models on symmetric manifolds have gained significant attention, existing approaches often rely on the manifolds' heat kernels, which lack closed-form expressions and result in exponential-in-dimension per-iteration runtimes during training. We introduce a new diffusion model for symmetric-space manifolds, leveraging a projection of Euclidean Brownian motion to bypass explicit heat kernel computations. Our training algorithm minimizes a novel objective function derived via Ito's Lemma, with efficiently computable gradients, allowing each iteration to run in polynomial time for symmetric manifolds. Additionally, the symmetries of the manifold ensure the diffusion satisfies an "average-case" Lipschitz condition, enabling accurate and efficient sample generation. These improvements enhance both the training runtime and sample accuracy for key cases of symmetric manifolds, helping to bridge the gap between diffusion models on symmetric manifolds and Euclidean space.

## item_id: m_1138

TITLE: Overview on Reinforcement Learning for Robotics

ABSTRACT: Reinforcement Learning(RL) offers robotics tasks a framework and set of tools for the design of sophisticated and hard-to-engineer behaviors.[1]
Reinforcement Learning is an branch of Machine Learning inspired by behaviorist psychology[wiki- Reinforcemenr Learning], concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.
The basic idea of Reinforcement Learning is to obtain a policy that extract more reward from the environment by picking actions given a state.
By policy, we mean a decision maker (Agent) that decide on an action based on some parameterized rules given an input observation of environment (State). The policy can be a set of weight that linearly combine the features in a state or different structured Neural Network. The environment in Reinforcement Learning context provide the agent a new state and reward immediately after the agent takes a specific action.
From a more broad view, the Machine Learning method was mainly three folds. The Supervised Learning, Semi-supervised Learning and Unsupervised Learning. The supervised learning network was trained given a dataset including the observation data and the corresponding categorization. The latter was given a dataset that no classification is label to the observation data. For reinforcement Learning, it is more close to supervised learning, while its label is obtained by exploring the environment and get feedback (reward, r) from it. The RL algorithm marks the policy that generates the highest score as the training target and make small change of its parameters (or weights, θ) towards that policy until the policy converge.
In this report, we mainly focus on the methods of Reinforcement Learning methods for robotics.

## item_id: m_1139

TITLE: Learning Recurrent Binary/Ternary Weights

ABSTRACT: Recurrent neural networks (RNNs) have shown excellent performance in processing sequence data. However, they are both complex and memory intensive due to their recursive nature. These limitations make RNNs difficult to embed on mobile devices requiring real-time processes with limited hardware resources. To address the above issues, we introduce a method that can learn binary and ternary weights during the training phase to facilitate hardware implementations of RNNs. As a result, using this approach replaces all multiply-accumulate operations by simple accumulations, bringing significant benefits to custom hardware in terms of silicon area and power consumption. On the software side, we evaluate the performance (in terms of accuracy) of our method using long short-term memories (LSTMs) and gated recurrent units (GRUs) on various sequential models including sequence classification and language modeling. We demonstrate that our method achieves competitive results on the aforementioned tasks while using binary/ternary weights during the runtime. On the hardware side, we present custom hardware for accelerating the recurrent computations of LSTMs with binary/ternary weights. Ultimately, we show that LSTMs with binary/ternary weights can achieve up to 12x memory saving and 10x inference speedup compared to the full-precision hardware implementation design.

## item_id: m_1140

TITLE: Divide-and-Conquer Reinforcement Learning

ABSTRACT: Standard model-free deep reinforcement learning (RL) algorithms sample a new initial state for each trial, allowing them to optimize policies that can perform well even in highly stochastic environments. However, problems that exhibit considerable initial state variation typically produce high-variance gradient estimates for model-free RL, making direct policy or value function optimization challenging. In this paper, we develop a novel algorithm that instead partitions the initial state space into "slices", and optimizes an ensemble of policies, each on a different slice. The ensemble is gradually unified into a single policy that can succeed on the whole state space. This approach, which we term divide-and-conquer RL, is able to solve complex tasks where conventional deep RL methods are ineffective. Our results show that divide-and-conquer RL greatly outperforms conventional policy gradient methods on challenging grasping, manipulation, and locomotion tasks, and exceeds the performance of a variety of prior methods. Videos of policies learned by our algorithm can be viewed at https://sites.google.com/view/dnc-rl/


## item_id: m_1141

TITLE: Improving generalization by regularizing in $L^2$ function space

ABSTRACT: Learning rules for neural networks necessarily include some form of regularization. Most regularization techniques are conceptualized and implemented in the space of parameters. However, it is also possible to regularize in the space of functions. Here, we propose to measure networks in an $L^2$ Hilbert space, and test a learning rule that regularizes the distance a network can travel through $L^2$-space each update.  This approach is inspired by the slow movement of gradient descent through parameter space as well as by the natural gradient, which can be derived from a regularization term upon functional change. The resulting learning rule, which we call Hilbert-constrained gradient descent (HCGD), is thus closely related to the natural gradient but regularizes a different and more calculable metric over the space of functions. Experiments show that the HCGD is efficient and leads to considerably better generalization. 

## item_id: m_1142

TITLE: Learning Disentangled Representations in Deep Generative Models

ABSTRACT: Deep generative models provide a powerful and flexible means to learn complex distributions over data by incorporating neural networks into latent-variable models. Variational approaches to training such models introduce a probabilistic encoder that casts data, typically unsupervised, into an entangled and unstructured representation space. While unsupervised learning is often desirable, sometimes even necessary, when we lack prior knowledge about what to represent, being able to incorporate domain knowledge in characterising certain aspects of variation in the data can often help learn better disentangled representations. Here, we introduce a new formulation of semi-supervised learning in variational autoencoders that allows precisely this. It permits flexible specification of probabilistic encoders as directed graphical models via a stochastic computation graph, containing both continuous and discrete latent variables, with conditional distributions parametrised by neural networks. We demonstrate how the provision of structure, along with a few labelled examples indicating plausible values for some components of the latent space, can help quickly learn disentangled representations. We then evaluate its ability to do so, both qualitatively by exploring its generative capacity, and quantitatively by using the disentangled representation to perform classification, on a variety of models and datasets.

## item_id: m_1143

TITLE: ExcelFormer: Making Neural Network Excel in Small Tabular Data Prediction

ABSTRACT: Data organized in tables are omnipresent in real-world applications. Despite their strong performance on large-scale datasets, deep neural networks (DNNs) perform inferior on small-scale tabular data, which hinders the wider adoption of DNNs across domains. In this paper, we propose a holistic framework comprising a novel neural network architecture called ExcelFormer and two data augmentation approaches, which achieves high-precision prediction for supervised classification and regression tasks, particularly on small-scale tabular datasets. The core component of ExcelFormer is a novel "semi-permeable attention" coupled with a special initialization, which explicitly diminishes the impacts of uninformative features, thereby improving data-efficiency. The methodology insight behind two tabular data augmentation approaches, Feat-Mix and Hid-Mix, is to increase the training samples in a way accommodating the inherent irregularities of data patterns. Comprehensive experiments on diverse small-scale tabular datasets show that, our ExcelFormer consistently and substantially outperforms previous works, with no noticeable dataset type preference. Remarkably, we find the superiority of ExcelFormer extends to large datasets as well.

## item_id: m_1144

TITLE: How Powerful are Graph Neural Networks with Random Weights?

ABSTRACT: Thanks to the great success of graph neural networks (GNNs) in structural information learning, extensive variants by virtue of sampling or pooling have been developed to further improve the performance, scalability, and applicability. However, there is still room for improvement in learning efficiency because current GNNs are trained via batch gradient descent with many graphs in each iteration. The good potential of random features in speeding up the training phase motivates us to consider the expressive power of GNNs with random weights. Based on the framework of Graph Isomorphism Network, we propose a novel model called Hashing Graph Isomorphism Network (HashGIN) with only one epoch of training by revising the convolutional layer with random hash functions and adjusting the learning objective with regularized least squares loss. In light of the property of $k$ random hash functions, we theoretically show that the injective phase in the Weisfeiler-Lehman test can be approximated by a hash family. An approximation upper bound is further provided with rigorous mathematical proof for the convergence of our model. Our experiments on several benchmark datasets show that HashGIN is effective and efficient for graph classification tasks. Compared to the state-of-the-art methods, HashGIN achieves better or comparable accuracies with less training time and memory cost.

## item_id: m_1145

TITLE: Prompt Engineering at Scale: Provably Effective Multi-Agent Cascades for Attribute Generation in E-Commerce

ABSTRACT: Developing specialized Large Language Model (LLM) prompts for domain-specific tasks at scale remains a significant hurdle, particularly for e-commerce applications managing tens of thousands of distinct product attributes. We introduce CascadeAgent, a novel multi-agent framework that automates prompt adaptation and specialization through semantic gradient-based refinement. CascadeAgent employs a hierarchical architecture where a central Prompting Agent orchestrates four specialized counterparts—Writing, Generation, Evaluation, and Flaw Detection—that collaboratively analyze domain metadata, construct attribute-specific prompts, and enhance performance through iterative feedback. Our approach combines Multi-pass Prompt Generation (MPG) for modularity with textual gradient optimization that refines instructions based on detected error patterns. We provide formal theoretical analysis demonstrating provable convergence towards reduced loss under defined conditions. In a large-scale e-commerce case study on product attribute enrichment, CascadeAgent generated and optimized over 27,000 distinct prompts, achieving improvements of +21% to +33% in precision and +12% to +14% in coverage across multiple LLMs. 
These results highlight CascadeAgent's capacity for robust, automated prompt engineering at industrial scale, while making more affordable models viable for deployment. The framework's modular design, iterative improvement mechanism, and theoretical guarantees make it a strong candidate for applications requiring principled refinement of vast numbers of task-specific prompts.

## item_id: m_1146

TITLE: Discrete Graph Structure Learning for Forecasting Multiple Time Series

ABSTRACT: Time series forecasting is an extensively studied subject in statistics, economics, and computer science. Exploration of the correlation and causation among the variables in a multivariate time series shows promise in enhancing the performance of a time series model. When using deep neural networks as forecasting models, we hypothesize that exploiting the pairwise information among multiple (multivariate) time series also improves their forecast. If an explicit graph structure is known, graph neural networks (GNNs) have been demonstrated as powerful tools to exploit the structure. In this work, we propose learning the structure simultaneously with the GNN if the graph is unknown. We cast the problem as learning a probabilistic graph model through optimizing the mean performance over the graph distribution. The distribution is parameterized by a neural network so that discrete graphs can be sampled differentiably through reparameterization. Empirical evaluations show that our method is simpler, more efficient, and better performing than a recently proposed bilevel learning approach for graph structure learning, as well as a broad array of forecasting models, either deep or non-deep learning based, and graph or non-graph based.

## item_id: m_1147

TITLE: Variational Smoothing in Recurrent Neural Network Language Models

ABSTRACT: We present a new theoretical perspective of data noising in recurrent neural network language models (Xie et al., 2017). We show that each variant of data noising is an instance of Bayesian recurrent neural networks with a particular variational distribution (i.e.,  a mixture of Gaussians whose weights depend on statistics derived from the corpus such as the unigram distribution). We use this insight to propose a more principled  method to apply at prediction time and propose natural extensions to data noising under the variational framework. In particular, we propose variational smoothing  with tied input and output embedding matrices and an element-wise variational smoothing method. We empirically verify our analysis on two benchmark language modeling datasets and demonstrate performance improvements over existing data noising methods.

## item_id: m_1148

TITLE: MagicDrive3D: Controllable 3D Generation for Any-View Rendering in Street Scenes

ABSTRACT: While controllable generative models for images and videos have achieved remarkable success, high-quality models for 3D scenes, particularly in unbounded scenarios like autonomous driving, remain underdeveloped due to high data acquisition costs. In this paper, we introduce MagicDrive3D, a novel pipeline for controllable 3D street scene generation that supports multi-condition control, including BEV maps, 3D objects, and text descriptions. Unlike previous methods that reconstruct before training the generative models, MagicDrive3D first trains a video generation model and then reconstructs from the generated data. This innovative approach enables easily controllable generation and static scene acquisition, resulting in high-quality scene reconstruction. To address the minor errors in generated content, we propose deformable Gaussian splatting with monocular depth initialization and appearance modeling to manage exposure discrepancies across viewpoints. Validated on the nuScenes dataset, MagicDrive3D generates diverse, high-quality 3D driving scenes that support any-view rendering and enhance downstream tasks like BEV segmentation. Our results demonstrate the framework's superior performance, showcasing its transformative potential for autonomous driving simulation and beyond.

## item_id: m_1149

TITLE: SteinsGate: Adding Causality to Diffusions for Long Video Generation via Path Integral

ABSTRACT: Video generation has advanced rapidly, but current models remain limited to short clips, far from the length and complexity of real-world narratives. Long video generation is thus both important and challenging. Existing approaches either attempt to extend the modeling length of video diffusion models directly or merge short clips via shared frames. However, due to the lack of temporal causality modeling for video data, they achieve only limited extensions, suffer from discontinuous or even contradictory actions, and fail to support flexible and fine-grained temporal control. Thus, we propose Instruct-Video-Continuation (InstructVC), combining Temporal Action Binding for fine-grained temporal control and Causal Video Continuation for natural long-term simulation. Temporal Action Binding decomposes complex long videos by temporal causality into scene descriptions and action sequences with predicted durations, while Causal Video Continuation autoregressively generates coherent video narratives from the text story. We further introduce SteinsGate, an inference-time instance of InstructVC that uses an MLLM for Temporal Action Binding and Video Path Integral to enforce causality between actions, converting a pre-trained TI2V diffusion model into an autoregressive video continuation model. Benchmark results demonstrate the advantages of SteinsGate and InstructVC in achieving accurate temporal control and generating natural, smooth multi-action long videos.

## item_id: m_1150

TITLE: Fake Sentence Detection as a Training Task for Sentence Encoding

ABSTRACT:     Sentence encoders are typically trained on generative language modeling tasks with large unlabeled datasets. While these encoders achieve strong results on many sentence-level tasks, they are difficult to train with long training cycles. 
    We introduce fake sentence detection as a new discriminative training task for learning sentence encoders. We automatically generate fake sentences by corrupting original sentences from a source collection and train the encoders to produce representations that are effective at detecting fake sentences. This binary classification task turns to be quite efficient for training sentence encoders. We compare a basic BiLSTM encoder trained on this task with strong sentence encoding models (Skipthought and FastSent) trained on a language modeling task. We find that the BiLSTM trains much faster on fake sentence detection (20 hours instead of weeks) using smaller amounts of data (1M instead of 64M sentences). Further analysis shows the learned representations also capture many syntactic and semantic properties expected from good sentence representations.

## item_id: m_1151

TITLE: RNNs Incrementally Evolving on an Equilibrium Manifold: A Panacea for Vanishing and Exploding Gradients?

ABSTRACT: Recurrent neural networks (RNNs) are particularly well-suited for modeling long-term dependencies in sequential data, but are notoriously hard to train because the error backpropagated in time either vanishes or explodes at an exponential rate. While a number of works attempt to mitigate this effect through gated recurrent units, skip-connections, parametric constraints and design choices, we propose a novel incremental RNN (iRNN), where hidden state vectors keep track of incremental changes, and as such approximate state-vector increments of Rosenblatt's (1962) continuous-time RNNs. iRNN exhibits identity gradients and is able to account for long-term dependencies (LTD). We show that our method is computationally efficient overcoming overheads of many existing methods that attempt to improve RNN training, while suffering no performance degradation. We demonstrate the utility of our approach with extensive experiments and show competitive performance against standard LSTMs on LTD and other non-LTD tasks.


## item_id: m_1152

TITLE: See, Think, Hallucinate: Interpreting Reasoning and Hallucinations Beyond the First Hop in Vision-Language Models

ABSTRACT: Vision-language models (VLMs) are prone to hallucinations, including errors such as factual inaccuracies, biases, and reasoning failures. Prior research has primarily focused on object hallucinations in single-hop settings, where models are asked to describe an image and are evaluated on whether they mention non-existent objects. However, such work overlooks broader forms of hallucination that arise in more complex reasoning scenarios. In this paper, we investigate hallucinations in vision-language reasoning beyond the first hop, where models must first extract factual content from an image and then combine it with external knowledge to answer a question.
In particular, we first present MMHop, a dataset of multimodal two-hop questions spanning five knowledge categories: general reasoning, perceptual co-occurrence, temporal knowledge, cultural and regional knowledge, and biasd prior knowledge. Using MMHop, we conduct a systematic analysis of VLMs with different architectures and LLM backbones, uncovering where hallucinations arise and how reasoning unfolds. Our comparative study reveals distinct failure tendencies: some models are easily distracted by visual co-occurrence, while others rely excessively on internal knowledge or stereotypical priors.
Beyond model-specific behaviors, our results highlight common structural patterns in two-hop reasoning. VLMs exhibit a two-stage inference process: an input understanding stage, dominated by multi-head attention, followed by a reasoning stage, where feed-forward networks become increasingly important. Early reasoning layers primarily capture first-hop inference, while later layers focus on second-hop reasoning. We further identify failure modes across categories: shortcut reliance on visual context, shallow recall of temporal knowledge, weak cultural grounding, and bias-driven errors. Finally, we show that question variants and inference settings, such as test-time scaling, can alter reasoning dynamics and reduce hallucination.
Our analyses provide new interpretability-driven insights into multimodal hallucinations, paving the way toward more reliable and trustworthy vision-language reasoning systems.

## item_id: m_1153

TITLE: Inner Classifier-Free Guidance and Its Taylor Expansion for Diffusion Models

ABSTRACT: Classifier-free guidance (CFG) is a pivotal technique for balancing the diversity and fidelity of samples in conditional diffusion models. This approach involves utilizing a single model to jointly optimize the conditional score predictor and unconditional score predictor, eliminating the need for additional classifiers. It delivers impressive results and can be employed for continuous and discrete condition representations. However, when the condition is continuous, it prompts the question of whether the trade-off can be further enhanced. Our proposed inner classifier-free guidance (ICFG) provides an alternative perspective on the CFG method when the condition has a specific structure, demonstrating that CFG represents a first-order case of ICFG. Additionally, we offer a second-order implementation, highlighting that even without altering the training policy, our second-order approach can introduce new valuable information and achieve an improved balance between fidelity and diversity for Stable Diffusion.

## item_id: m_1154

TITLE: Unprocessing Seven Years of Algorithmic Fairness

ABSTRACT: Seven years ago, researchers proposed a postprocessing method to equalize the error rates of a model across different demographic groups. The work launched hundreds of papers purporting to improve over the postprocessing baseline. We empirically evaluate these claims through thousands of model evaluations on several tabular datasets. We find that the fairness-accuracy Pareto frontier achieved by postprocessing contains all other methods we were feasibly able to evaluate. In doing so, we address two common methodological errors that have confounded previous observations. One relates to the comparison of methods with different unconstrained base models. The other concerns methods achieving different levels of constraint relaxation. At the heart of our study is a simple idea we call unprocessing that roughly corresponds to the inverse of postprocessing. Unprocessing allows for a direct comparison of methods using different underlying models and levels of relaxation.

## item_id: m_1155

TITLE: Neural Contractive Dynamical Systems

ABSTRACT: Stability guarantees are crucial when ensuring that a fully autonomous robot does not take undesirable or potentially harmful actions. Unfortunately, global stability guarantees are hard to provide in dynamical systems learned from data, especially when the learned dynamics are governed by neural networks. We propose a novel methodology to learn \emph{neural contractive dynamical systems}, where our neural architecture ensures contraction, and hence, global stability. To efficiently scale the method to high-dimensional dynamical systems, we develop a variant of the variational autoencoder that learns dynamics in a low-dimensional latent representation space while retaining contractive stability after decoding. We further extend our approach to learning contractive systems on the Lie group of rotations to account for full-pose end-effector dynamic motions. The result is the first highly flexible learning architecture that provides contractive stability guarantees with capability to perform obstacle avoidance. Empirically, we demonstrate that our approach encodes the desired dynamics more accurately than the current state-of-the-art, which provides less strong stability guarantees.

## item_id: m_1156

TITLE: Epitomic Variational Autoencoders

ABSTRACT: In this paper, we propose epitomic variational autoencoder (eVAE), a probabilistic generative model of high dimensional data. eVAE is composed of a number of sparse variational autoencoders called `epitome' such that each epitome partially shares its encoder-decoder architecture with other epitomes in the composition. We show that the proposed model greatly overcomes the common problem in variational autoencoders (VAE) of model over-pruning. We substantiate that eVAE is efficient in using its model capacity and generalizes better than VAE, by presenting qualitative and quantitative results on MNIST and TFD datasets.

## item_id: m_1157

TITLE: Learning to Prove Theorems by Learning to Generate Theorems

ABSTRACT: We consider the task of automated theorem proving, a key AI task. Deep learning has shown promise for training theorem provers, but there are limited human-written theorems and proofs available for supervised learning. To address this limitation, we propose to learn a neural generator that automatically synthesizes theorems and proofs for the purpose of training a theorem prover. Experiments on real-world  tasks demonstrate that synthetic data from our approach significantly improves the theorem prover and advances the state of the art of automated theorem proving in Metamath.

## item_id: m_1158

TITLE: First return, entropy-eliciting explore

ABSTRACT: Reinforcement Learning from Verifiable Rewards (RLVR) improves the reasoning abilities of Large Language Models (LLMs) but it struggles with unstable exploration. We propose FR3E (First Return, Entropy-Eliciting Explore), a structured exploration framework that identifies high-uncertainty decision points in reasoning trajectories and performs targeted rollouts to construct semantically grounded intermediate feedback. Our method provides targeted guidance without relying on dense supervision. Empirical results on mathematical reasoning benchmarks(AIME24) show that FR3E promotes more stable training, produces longer and more coherent responses, and increases the proportion of fully correct trajectories. These results highlight the framework's effectiveness in improving LLM reasoning through more robust and structured exploration.

## item_id: m_1159

TITLE: CCC: Prompt Evolution for Video Generation via Structured MLLM Feedback

ABSTRACT: Video generation from natural-language prompts has made impressive strides, but current systems frequently misalign outputs with their input descriptions—dropping critical details, hallucinating unintended content, and often violating basic physical plausibility. Existing approaches to improving video quality typically rely on heavyweight post-editing models, which may introduce new artifacts, or costly fine-tuning of the generator backbone, limiting scalability and accessibility.
We introduce Critique Coach Calibration (CCC), a training-free, model-agnostic framework for iterative prompt evolution that closes the gap between direct generation and reality. In each cycle, an off-the-shelf multimodal large language model (MLLM) produces a structured critique of a generated video—identifying semantic misalignments, subject drift, and missing objects—and then reformulates the input prompt based on this feedback. By repeatedly evolving prompts through this critique–coach loop, CCC steadily improves both video quality and adherence to everyday physics, all without modifying the generator or relying on external editing modules.
Empirical results on different video models show that CCC consistently enhances semantic alignment and visual quality through the power of adaptive prompt evolution.

## item_id: m_1160

TITLE: MAP: Unleashing Hybrid Mamba-Transformer Vision Backbone’s Potential with Masked Autoregressive Pretraining

ABSTRACT: Mamba has achieved significant advantages in long-context modeling and autoregressive tasks, but its scalability with large parameters remains a major limitation in vision applications. pretraining is a widely used strategy to enhance backbone model performance. Although the success of Masked Autoencoder in Transformer pretraining is well recognized, it does not significantly improve Mamba's visual learning performance. We found that using the correct autoregressive pretraining can significantly boost the performance of the Mamba architecture. Based on this analysis, we propose Masked Autoregressive Pretraining(MAP) to pretrain a hybrid Mamba-Transformer vision backbone network. This strategy combines the strengths of both MAE and Autoregressive pretraining, improving the performance of Mamba and Transformer modules within a unified paradigm. Experimental results show that both the pure Mamba architecture and the hybrid Mamba-Transformer vision backbone network pretrained with MAP significantly outperform other pretraining strategies, achieving state-of-the-art performance. We validate the effectiveness of the method on both 2D and 3D datasets and provide detailed ablation studies to support the design choices for each component.

## item_id: m_1161

TITLE: Understand the dynamics of GANs via Primal-Dual Optimization

ABSTRACT: Generative adversarial network (GAN) is one of the best known unsupervised learning techniques these days due to its superior ability to learn data distributions. In spite of its great success in applications, GAN is known to be notoriously hard to train. The tremendous amount of time it takes to run the training algorithm and its sensitivity to hyper-parameter tuning have been haunting researchers in this area. To resolve these issues, we need to first understand how GANs work. Herein, we take a step toward this direction by examining the dynamics of GANs. We relate a large class of GANs including the Wasserstein GANs to max-min optimization problems with the coupling term being linear over the discriminator. By developing new primal-dual optimization tools, we show that, with a proper stepsize choice, the widely used first-order iterative algorithm in training GANs would in fact converge to a stationary solution with a sublinear rate. The same framework also applies to multi-task learning and distributional robust learning problems. We verify our analysis on numerical examples with both synthetic and real data sets. We hope our analysis shed light on future studies on the theoretical properties of relevant machine learning problems.

## item_id: m_1162

TITLE: Residual Energy-Based Models for Text Generation

ABSTRACT: Text generation is ubiquitous in many NLP tasks, from summarization, to dialogue and machine translation. The dominant parametric approach is based on locally normalized models which predict one word at a time. While these work remarkably well, they are plagued by exposure bias due to the greedy nature of the generation process. In this work, we investigate un-normalized energy-based models (EBMs) which operate not at the token but at the sequence level. In order to make training tractable, we first work in the residual of a pretrained locally normalized language model and second we train using noise contrastive estimation. Furthermore, since the EBM works at the sequence level, we can leverage pretrained bi-directional contextual representations, such as BERT and RoBERTa. Our experiments on two large language modeling datasets show that residual EBMs yield lower perplexity compared to locally normalized baselines. Moreover, generation via importance sampling is very efficient and of higher quality than the baseline models according to human evaluation.

## item_id: m_1163

TITLE: Explainable Artificial Intelligence: Reaping the Fruits of Decision Trees

ABSTRACT: The recent push for explainable artificial intelligence (XAI) has given rise to extensive work toward understanding the inner workings of neural networks. Much of that work, however, has focused on manipulating input data feeding the network to assess their effect on network output. It is shown in this study that XAI can benefit from investigating the network node, the most fundamental unit of neural networks. Whereas studies on XAI have mostly benefited from a focus on manipulating input data, assessing patterns in node weights may prove equally beneficial, if not more significant, especially when realizing that weight values may not be as random as previously thought. A manipulated, a contrived, and a real dataset were used in this study. Datasets were run on convolutional and deep neural network models. Node rank stability was the central construct to investigate neuronal patterns in this study. Rank stability was defined as the number of epochs wherein nodes held their rank in terms of weight value compared to their rank at the last epoch, when the model reached convergence, or stability (defined in this study as accuracy $\geq$ 0.90). Findings indicated that neural networks behaved like a decision tree, in that rank stability increased as weight absolute values increased. Decision tree behavior may assist in more efficient pruning algorithms, which may produce distilled models simpler to explain to technical and non-technical audiences.

## item_id: m_1164

TITLE: Discovering Low-Precision Networks Close to Full-Precision Networks for Efficient Embedded Inference

ABSTRACT: To realize the promise of ubiquitous embedded deep network inference, it is essential to seek limits of energy and area efficiency.  To this end, low-precision networks offer tremendous promise because both energy and area scale down quadratically with the reduction in precision.  Here, for the first time, we demonstrate ResNet-18, ResNet-34, ResNet-50, ResNet-152, Inception-v3, densenet-161, and VGG-16bn networks on the ImageNet classification benchmark that, at 8-bit precision exceed the accuracy of the full-precision baseline networks after one epoch of finetuning, thereby leveraging the availability of pretrained models.
We also demonstrate ResNet-18, ResNet-34, and ResNet-50 4-bit models that match the accuracy of the full-precision baseline networks -- the highest scores to date. Surprisingly, the weights of the low-precision networks are very close (in cosine similarity) to the weights of the corresponding baseline networks, making training from scratch unnecessary.

We find that gradient noise due to quantization during training increases with reduced precision, and seek ways to overcome this noise. The number of iterations required by stochastic gradient descent to achieve a given training error is related to the square of (a) the distance of the initial solution from the final plus (b) the maximum variance of the gradient estimates.  By drawing inspiration from this observation, we (a) reduce solution distance by starting with pretrained fp32 precision baseline networks and fine-tuning, and (b) combat noise introduced by quantizing weights and activations during training, by using larger batches along with matched learning rate annealing.  Sensitivity analysis indicates that these techniques, coupled with proper activation function range calibration, offer a promising heuristic to discover low-precision networks, if they exist, close to fp32 precision baseline networks.


## item_id: m_1165

TITLE: Learning a Game by Paying the Agents

ABSTRACT: We study the problem of learning the utility functions of no-regret learning agents in a repeated normal-form game.
Differing from most prior literature, we introduce a principal with the power to observe the agents playing the game, send agents signals, and give agents *payments* as a function of their actions.
We show that the principal can, using a number of rounds polynomial in the size of the game, learn the utility functions of all agents to any desired precision $\varepsilon > 0$, for *any* no-regret learning algorithms of the agents.
Our main technique is to formulate a zero-sum game between the principal and the agents, where the principal chooses strategies among the set of all payment functions to minimize the agent's payoff. 
Finally, we discuss implications for the problem of *steering* agents. We introduce, using our utility-learning algorithm as a subroutine, the first algorithm for steering arbitrary no-regret learning agents to a desired equilibrium without prior knowledge of their utility functions.

## item_id: m_1166

TITLE: Targeted Adversarial Self-Supervised Learning

ABSTRACT: Recently, unsupervised adversarial training (AT) has been extensively studied to attain robustness with the models trained upon unlabeled data. To this end, previous studies have applied existing supervised adversarial training techniques to self-supervised learning (SSL) frameworks. However, all have resorted to untargeted adversarial learning as obtaining targeted adversarial examples is unclear in the SSL setting lacking of label information. In this paper, we propose a novel targeted adversarial training method for the SSL frameworks. Specifically, we propose a target selection algorithm for the adversarial SSL frameworks; it is designed to select the most confusing sample for each given instance based on similarity and entropy, and perturb the given instance toward the selected target sample. Our method significantly enhances the robustness of an SSL model without requiring large batches of images or additional models, unlike existing works aimed at achieving the same goal. Moreover, our method is readily applicable to general SSL frameworks that only uses positive pairs. We validate our method on benchmark datasets, on which it obtains superior robust accuracies, outperforming existing unsupervised adversarial training methods. 

## item_id: m_1167

TITLE: Efficient Sparse-Winograd Convolutional Neural Networks

ABSTRACT: Convolutional Neural Networks (CNNs) are computationally intensive, which limits their application on mobile devices. Their energy is dominated by the number of multiplies needed to perform the convolutions. Winograd’s minimal filtering algorithm (Lavin, 2015) and network pruning (Han et al., 2015) can reduce the operation count, but these two methods cannot be straightforwardly combined — applying the Winograd transform fills in the sparsity in both the weights and the activations. We propose two modifications to Winograd-based CNNs to enable these methods to exploit sparsity. First, we move the ReLU operation into the Winograd domain to increase the sparsity of the transformed activations. Second, we prune the weights in the Winograd domain to exploit static weight sparsity. For models on CIFAR-10, CIFAR-100 and ImageNet datasets, our method reduces the number of multiplications by 10.4x, 6.8x and 10.8x respectively with loss of accuracy less than 0.1%, outperforming previous baselines by 2.0x-3.0x. We also show that moving ReLU to the Winograd domain allows more aggressive pruning.

## item_id: m_1168

TITLE: Effector Complexity Enhances Transfer Learning

ABSTRACT: Both biological and artificial embodied systems rely on effectors to interact with the world. How does this embodiment impact the way they learn? The role of embodiment in shaping learning dynamics is not well understood from a neuroscience or a machine learning perspective. In this study, we treat embodiment as a variable in artificial agents and study how changes in effector complexity reshape the dynamics of learning. Our hypothesis is that more complex effectors provide constraints that yield better transfer learning on new tasks, despite simultaneously posing a more complex control problem. We evaluated this hypothesis on area under the performance curve, and use time to sustained performance plateau as a parameter for task difficulty. Our results show that while a simpler effector excels when trained from scratch, a more complex effector yields superior performance after pre-training on another task. We further demonstrate that the improvement gained from transfer learning is greater for the complex effector. Our findings suggest that embodiment plays an important role in enabling efficient transfer, offering insights into the differences in learning dynamics between disembodied artificial systems and their biological counterparts.

## item_id: m_1169

TITLE: BIOACOUSTIC SEGMENTATION BY HIERARCHICAL DIRICHLET PROCESS HIDDEN MARKOV MODEL

ABSTRACT: Understanding the communication between different animals by analysing their acoustic signals is an important topic in bioacoustics. It can be a powerful tool for the preservation of ecological diversity. We investigate probabilistic models to analyse signals issued from real-world bioacoustic sound scenes. We study a Bayesian non-parametric sequential models based on Hierarchical Dirichlet Process Hidden Markov Models (HDP-HMM). The model is able to infer hidden states, that are referred here as song units. However, using such a model raise one main issue: defining the number of hidden states the model has to learn. In bioacoustic problems we often do not know the number of song units (unlike in human speech recognition). Hence, we work with the Hierarchical Dirichlet Process (HDP)-HMM, which is a Bayesian non-parametric (BNP) model that offers a way to tackle this challenging problem. We focus our work on unsupervised learning from bioacoustic data. It consists in simultaneously finding the structure of hidden song units and automatically infer the unknown number of the hidden states to represent the data. Two real bioacoustic sound scene applications are investigated in this work: on whale and multi-species birds segmentation. The learning of these models is proceeded by using Markov-Chain Monte Carlo (MCMC) sampling techniques on Mel Frequency Cepstral Coefficients (MFCC) of audio signals. The results show an interesting song unit segmentation of the bioacoustic signals and open new insights for unsupervised analysis of such signals. This paper illustrates the potential of chunking non-human animal signals into structured parts. This can yield to a new species representation and help experts to better understand the behaviour of such species as Kershenbaum et al. (2014) wanted.

## item_id: m_1170

TITLE: Sobolev Training of End-to-End Optimization Proxies

ABSTRACT: Optimization proxies—machine-learning models trained to approximate
the solution mapping of parametric optimization problems in a single
forward pass—offer dramatic reductions in inference time compared to
traditional iterative solvers.  This work investigates the integration
of solver sensitivities into such end-to-end proxies via a
Sobolev–training paradigm and does so in \emph{two distinct settings}:
(i) \emph{fully supervised} proxies, where exact solver outputs and
sensitivities are available, and (ii) \emph{self-supervised} proxies
that rely only on the objective and constraint structure of the
underlying optimization problem.  
By augmenting the standard training loss
with directional-derivative information extracted from the solver, the
proxy aligns both its predicted solutions \emph{and} local derivatives
with those of the optimizer.  Under Lipschitz-continuity
assumptions on the true solution mapping, matching
first-order sensitivities is shown to yield uniform approximation error
proportional to the training-set covering radius.  
Empirically, different impacts are observed in each studied setting.  
On three large Alternating Current
Optimal Power Flow benchmarks, supervised Sobolev training cuts mean-squared error
by up to 56 \% and the median worst-case constraint violation by up to
400 \% while keeping the optimality gap below 0.22 \%.  
For a mean–variance
portfolio task trained without labeled solutions, self-supervised Sobolev training
halves the average optimality gap in the medium-risk region
(i.e. standard deviation above $10\%$ of budget) and matches the baseline elsewhere.
Together, these results highlight Sobolev training—whether supervised or
self-supervised—as a path to fast, reliable surrogates for
safety-critical, large-scale optimization workloads.

## item_id: m_1171

TITLE: Discovery of Predictive Representations With a Network of General Value Functions

ABSTRACT: The ability of an agent to {\em discover} its own learning objectives has long been considered a key ingredient for artificial general intelligence. Breakthroughs in autonomous decision making and reinforcement learning have primarily been in domains where the agent's goal is outlined and clear: such as playing a game to win, or driving safely. Several studies have demonstrated that learning extramural sub-tasks and auxiliary predictions can improve (1) single human-specified task learning, (2) transfer of learning, (3) and the agent's learned representation of the world. In all these examples, the agent was instructed what to learn about. We investigate a framework for discovery: curating a large collection of predictions, which are used to construct the agent's representation of the world. Specifically, our system maintains a large collection of predictions, continually pruning and replacing predictions. We highlight the importance of considering stability rather than convergence for such a system, and develop an adaptive, regularized algorithm towards that aim. We provide several experiments in computational micro-worlds demonstrating that this simple approach can be effective for discovering useful predictions autonomously.

## item_id: m_1172

TITLE: Achieving morphological agreement with Concorde

ABSTRACT: Neural conversational models are widely used in applications like personal assistants and chat bots. These models seem to give better performance when operating on word level. However, for fusion languages like French, Russian and Polish vocabulary size sometimes become infeasible since most of the words have lots of word forms. We propose a neural network architecture for transforming normalized text into a grammatically correct one. Our model efficiently employs correspondence between normalized and target words and significantly outperforms character-level models while being 2x faster in training and 20\% faster at evaluation. We also propose a new pipeline for building conversational models: first generate a normalized answer and then transform it into a grammatically correct one using our network. The proposed pipeline gives better performance than character-level conversational models according to assessor testing.

## item_id: m_1173

TITLE: Efficient Calculation of Polynomial Features on Sparse Matrices

ABSTRACT: We provide an algorithm for polynomial feature expansion that both operates on
and produces a compressed sparse row matrix without any densification. For a
vector of dimension D, density d, and degree k the algorithm has time complexity
O(d^k * D^k) where k is the polynomial-feature order; this is an improvement by a factor d^k
over the standard method.

## item_id: m_1174

TITLE: Interpretable and Generalizable Graph Neural Networks via Subgraph Multilinear Extension

ABSTRACT: Interpretable graph neural networks (XGNNs) are widely adopted in scientific applications involving graph-structured data. Previous approaches predominantly adopt the attention-based mechanism to learn edge or node importance for extracting and making predictions with the interpretable subgraph. However, the representational properties and limitations of these methods remain inadequately explored. In this work, we present a theoretical framework that formulates interpretable subgraph learning with the multilinear extension of the subgraph distribution, which we term as subgraph multilinear extension (SubMT). Extracting the desired interpretable subgraph requires an accurate approximation of SubMT, yet we find that the existing XGNNs can have a huge gap in fitting SubMT. Consequently, the SubMT approximation failure will lead to the degenerated interpretability of the extracted subgraphs. To mitigate the issue, we design a new XGNN architecture called Graph Multilinear neT (GMT), which is provably more powerful in approximating SubMT. We empirically validate our theoretical findings on a number of graph classification benchmarks. The results demonstrate that GMT outperforms the state-of-the-art up to 10% in terms of both interpretability and generalizability measures.

## item_id: m_1175

TITLE: On-Policy Model Errors in Reinforcement Learning

ABSTRACT: Model-free reinforcement learning algorithms can compute policy gradients given sampled environment transitions, but require large amounts of data. In contrast, model-based methods can use the learned model to generate new data, but model errors and bias can render learning unstable or suboptimal. In this paper, we present a novel method that combines real-world data and a learned model in order to get the best of both worlds. The core idea is to exploit the real-world data for on-policy predictions and use the learned model only to generalize to different actions. Specifically, we use the data as time-dependent on-policy correction terms on top of a learned model, to retain the ability to generate data without accumulating errors over long prediction horizons. We motivate this method theoretically and show that it counteracts an error term for model-based policy improvement. Experiments on MuJoCo- and PyBullet-benchmarks show that our method can drastically improve existing model-based approaches without introducing additional tuning parameters.

## item_id: m_1176

TITLE: Variadic Learning by Bayesian Nonparametric Deep Embedding

ABSTRACT: Learning at small or large scales of data is addressed by two strong but divided frontiers: few-shot learning and standard supervised learning. Few-shot learning focuses on sample efficiency at small scale, while supervised learning focuses on accuracy at large scale. Ideally they could be reconciled for effective learning at any number of data points (shot) and number of classes (way). To span the full spectrum of shot and way, we frame the variadic learning regime of learning from any number of inputs. We approach variadic learning by meta-learning a novel multi-modal clustering model that connects bayesian nonparametrics and deep metric learning. Our bayesian nonparametric deep embedding (BANDE) method is optimized end-to-end with a single objective, and adaptively adjusts capacity to learn from variable amounts of supervision. We show that multi-modality is critical for learning complex classes such as Omniglot alphabets and carrying out unsupervised clustering. We explore variadic learning by measuring generalization across shot and way between meta-train and meta-test, show the first results for scaling from few-way, few-shot tasks to 1692-way Omniglot classification and 5k-shot CIFAR-10 classification, and find that nonparametric methods generalize better than parametric methods. On the standard few-shot learning benchmarks of Omniglot and mini-ImageNet, BANDE equals or improves on the state-of-the-art for semi-supervised classification.

## item_id: m_1177

TITLE: Unsupervised Learning of Node Embeddings by Detecting Communities

ABSTRACT: We present Deep MinCut (DMC), an unsupervised approach to learn node embeddings for graph-structured data. It derives node representations based on their membership in communities. As such, the embeddings directly provide interesting insights into the graph structure, so that the separate node clustering step of existing methods is no longer needed. DMC learns both, node embeddings and communities, simultaneously by minimizing the mincut loss, which captures the number of connections between communities. Striving for high scalability, we also propose a training process for DMC based on minibatches. We provide empirical evidence that the communities learned by DMC are meaningful and that the node embeddings are competitive in different node classification benchmarks.

## item_id: m_1178

TITLE: Learning Sparse Latent Representations with the Deep Copula Information Bottleneck

ABSTRACT: Deep latent variable models are powerful tools for representation learning. In this paper, we adopt the deep information bottleneck model, identify its shortcomings and propose a model that circumvents them. To this end, we apply a copula transformation which, by restoring the invariance properties of the information bottleneck method, leads to disentanglement of the features in the latent space. Building on that, we show how this transformation translates to sparsity of the latent space in the new model.  We evaluate our method on artificial and real data.

## item_id: m_1179

TITLE: It Takes Four to Tango: Multiagent Self Play for Automatic Curriculum Generation

ABSTRACT: We are interested in training general-purpose reinforcement learning agents that can solve a wide variety of goals. Training such agents efficiently requires automatic generation of a goal curriculum. This is challenging as it requires (a) exploring goals of increasing difficulty, while ensuring that the agent (b) is exposed to a diverse set of goals in a sample efficient manner and (c) does not catastrophically forget previously solved goals. We propose Curriculum Self Play (CuSP), an automated goal generation framework that seeks to satisfy these desiderata by virtue of a multi-player game with 4 agents. We extend the asymmetric curricula learning in PAIRED (Dennis et al., 2020) to a symmetrized game that carefully balances cooperation and competition between two off-policy student learners and two regret-maximizing teachers. CuSP additionally introduces entropic goal coverage and accounts for the non-stationary nature of the students, allowing us to automatically induce a curriculum that balances progressive exploration with anti-catastrophic exploitation. We demonstrate that our method succeeds at generating an effective curricula of goals for a range of control tasks, outperforming other methods at zero-shot test-time generalization to novel out-of-distribution goals.

## item_id: m_1180

TITLE: Alleviating Label Shift Through Self-trained Intermediate Distribution: Theory and Algorithms

ABSTRACT: As an obstacle towards real-world problems with the changing environment, label shift, which assumes the source and target label marginal distributions differ, loosens the homogeneous distribution assumption in classical learning scenarios. To correct the label shift, importance weighting is one of the most popular strategies with rigorous theoretical guarantees. However, the importance weight estimation of most existing methods results in high variance under large label shift or few source samples. In this paper, we introduce an ideal intermediate distribution instead of the source distribution to reduce the variation to the target label distribution. Our approach learns a self-trained intermediate distribution constructed from the labeled source and unlabeled target samples to approximate the ideal intermediate distribution. It balances the bias from pseudo target labels and the variance from importance weighting. Besides, we prove the sample complexity and generalization guarantees for our approach, which has a tighter generalization bound than the existing label shift methods under mild conditions. Extensive experimental results validate the effectiveness of our approach over existing state-of-the-arts methods.

## item_id: m_1181

TITLE: Manifold Mixup: Learning Better Representations by Interpolating Hidden States

ABSTRACT: Deep networks often perform well on the data distribution on which they are trained, yet give incorrect (and often very confident) answers when evaluated on points from off of the training distribution. This is exemplified by the adversarial examples phenomenon but can also be seen in terms of model generalization and domain shift.  Ideally, a model would assign lower confidence to points unlike those from the training distribution.  We propose a regularizer which addresses this issue by training with interpolated hidden states and encouraging the classifier to be less confident at these points.  Because the hidden states are learned, this has an important effect of encouraging the hidden states for a class to be concentrated in such a way so that interpolations within the same class or between two different classes do not intersect with the real data points from other classes.  This has a major advantage in that it avoids the underfitting which can result from interpolating in the input space.  We prove that the exact condition for this problem of underfitting to be avoided by Manifold Mixup is that the dimensionality of the hidden states exceeds the number of classes, which is often the case in practice.  Additionally, this concentration can be seen as making the features in earlier layers more discriminative.  We show that despite requiring no significant additional computation, Manifold Mixup achieves large improvements over strong baselines in supervised learning, robustness to single-step adversarial attacks, semi-supervised learning, and Negative Log-Likelihood on held out samples.

## item_id: m_1182

TITLE: Task Diversity Shortens the ICL Plateau

ABSTRACT: In-context learning (ICL) describes a language model's ability to generate outputs based on a set of input demonstrations and a subsequent query. To understand this remarkable capability, researchers have studied simplified, stylized models. These studies have consistently observed long loss plateaus, during which models exhibit minimal improvement, followed by a sudden, rapid surge of learning. In this work, we reveal that training on multiple diverse ICL tasks simultaneously shortens the loss plateaus, making each task easier to learn. This finding is surprising as it contradicts the natural intuition that the combined complexity of multiple ICL tasks would lengthen the learning process, not shorten it. Our result suggests that the recent success in large-scale training of language models may be attributed not only to the richness of the data at scale but also to the easier optimization (training) induced by the diversity of natural language training data.

## item_id: m_1183

TITLE: Revisiting Batch Normalization For Practical Domain Adaptation

ABSTRACT: Deep neural networks (DNN) have shown unprecedented success in various computer vision applications such as image classification and object detection. However, it is still a common annoyance during the training phase, that one has to prepare at least thousands of labeled images to fine-tune a network to a specific domain. Recent study shows that a DNN has strong dependency towards the training dataset, and the learned features cannot be easily transferred to a different but relevant task without fine-tuning. In this paper, we propose a simple yet powerful remedy, called Adaptive Batch Normalization (AdaBN) to increase the generalization ability of a DNN. By modulating the statistics from the source domain to the target domain in all Batch Normalization layers across the network, our approach achieves deep adaptation effect for domain adaptation tasks. In contrary to other deep learning domain adaptation methods, our method does not require additional components, and is parameter-free. It archives state-of-the-art performance despite its surprising simplicity. Furthermore, we demonstrate that our method is complementary with other existing methods. Combining AdaBN with existing domain adaptation treatments may further improve model performance.

## item_id: m_1184

TITLE: A Unified View of Deep Metric Learning via Gradient Analysis

ABSTRACT: Loss functions play a pivotal role in deep metric learning (DML). A large variety of loss functions have been proposed in DML recently. However, it remains difficult to answer this question: what are the intrinsic differences among these loss functions?This paper answers this question by proposing a unified perspective to rethink deep metric loss functions. We show theoretically that most DML methods in deep metric learning, in view of  gradient equivalence, are essentially weight assignment strategies of training pairs. Based on this unified view, we revisit several typical DML methods and disclose their hidden drawbacks. Moreover, we point out the key components of an effective DML approach which drives us to propose our weight assignment framework. We evaluate our method on image retrieval tasks, and show that it outperforms  the state-of-the-art DML approaches by a significant margin on the CUB-200-2011, Cars-196, Stanford Online Products and In-Shop Clothes Retrieval datasets. 

## item_id: m_1185

TITLE: Lung Tumor Location and Identification with AlexNet and a Custom CNN

ABSTRACT: Lung cancer is the leading cause of cancer deaths in the world and early detection is a crucial part of increasing patient survival. Deep learning techniques provide us with a method of automated analysis of patient scans. In this work, we compare AlexNet, a multi-layered and highly ﬂexible architecture, with a custom CNN to determine if lung nodules with patient scans are benign or cancerous. We have found our CNN architecture to be highly accurate (99.79%) and fast while maintaining low False Positive and False Negative rates (< 0.01% and 0.15% respectively). This is important as high false positive rates are a serious issue with lung cancer diagnosis. We have found that AlexNet is not well suited to the problem of nodule identiﬁcation, though it is a good baseline comparison because of its ﬂexibility.

## item_id: m_1186

TITLE: Optimization as a Model for Few-Shot Learning

ABSTRACT: Though deep neural networks have shown great success in the large data domain, they generally perform poorly on few-shot learning tasks, where a model has to quickly generalize after seeing very few examples from each class. The general belief is that gradient-based optimization in high capacity models requires many iterative steps over many examples to perform well. Here, we propose an LSTM-based meta-learner model to learn the exact optimization algorithm used to train another learner neural network in the few-shot regime. The parametrization of our model allows it to learn appropriate parameter updates specifically for the scenario where a set amount of updates will be made, while also learning a general initialization of the learner network that allows for quick convergence of training. We demonstrate that this meta-learning model is competitive with deep metric-learning techniques for few-shot learning. 

## item_id: m_1187

TITLE: Towards Principled Methods for Training Generative Adversarial Networks

ABSTRACT: The goal of this paper is not to introduce a single algorithm or method, but to make theoretical steps towards fully understanding the training dynamics of gen- erative adversarial networks. In order to substantiate our theoretical analysis, we perform targeted experiments to verify our assumptions, illustrate our claims, and quantify the phenomena. This paper is divided into three sections. The first sec- tion introduces the problem at hand. The second section is dedicated to studying and proving rigorously the problems including instability and saturation that arize when training generative adversarial networks. The third section examines a prac- tical and theoretically grounded direction towards solving these problems, while introducing new tools to study them.

## item_id: m_1188

TITLE: Beyond Proxy Metrics: A New Evaluation Framework for LLM Compression by Directly Measuring  Generative Faithfulness

ABSTRACT: Current evaluation methods for Large Language Model (LLM) compression, which rely on proxy metrics like perplexity and curated benchmarks, often correlate poorly with real-world generative performance. This discrepancy creates a significant gap between reported scores and practical utility. To address this, we introduce a new evaluation framework that dispenses with such proxies by directly measuring a compressed model's generative faithfulness to its uncompressed counterpart on real-world user queries. The core of our framework is Conditional Generation Accuracy (CGA), a novel metric that employs a teacher-forcing paradigm to assess the compressed model's ability to replicate the original model's next-token prediction at each step, conditioned on the ground-truth prefix. This approach effectively avoids the cascading errors that confound traditional text-similarity measures. We apply this framework to a comprehensive evaluation of nine mainstream compression methods across models from 7B to 32B parameters and context lengths up to 24K tokens. Our results establish a clear performance hierarchy and reveal distinct scaling laws with respect to model size and context length. For instance, while most methods' performance improves with model size, we find that quantization and KV cache dropping degrade with longer contexts, whereas a sparse attention baseline uniquely improves. Our work provides a more rigorous and reliable foundation for benchmarking LLM compression. To promote transparent and reproducible progress, we have open-sourced our benchmark code at https://anonymous.4open.science/r/llm-fidbench/README.md and will launch a leaderboard.

## item_id: m_1189

TITLE: Meta-learning with negative learning rates

ABSTRACT: Deep learning models require a large amount of data to perform well. When data is scarce for a target task, we can transfer the knowledge gained by training on similar tasks to quickly learn the target. A successful approach is meta-learning, or "learning to learn" a distribution of tasks, where "learning" is represented by an outer loop, and "to learn" by an inner loop of gradient descent. However, a number of recent empirical studies argue that the inner loop is unnecessary and more simple models work equally well or even better. We study the performance of MAML as a function of the learning rate of the inner loop, where zero learning rate implies that there is no inner loop. Using random matrix theory and exact solutions of linear models, we calculate an algebraic expression for the test loss of MAML applied to mixed linear regression and nonlinear regression with overparameterized models. Surprisingly, while the optimal learning rate for adaptation is positive, we find that the optimal learning rate for training is always negative, a setting that has never been considered before. Therefore, not only does the performance increase by decreasing the learning rate to zero, as suggested by recent work, but it can be increased even further by decreasing the learning rate to negative
values. These results help clarify under what circumstances meta-learning performs best.

## item_id: m_1190

TITLE: Building Hierarchical Interpretations in Natural Language via Feature Interaction Detection

ABSTRACT: The interpretability of neural networks has become crucial for their applications in real world with respect to the reliability and trustworthiness. Existing explanation generation methods usually provide important features by scoring their individual contributions to the model prediction and ignore the interactions between features, which eventually provide a bag-of-words representation as explanation. In natural language processing, this type of explanations is challenging for human user to understand the meaning of an explanation and draw the connection between explanation and model prediction, especially for long texts. In this work, we focus on detecting the interactions between features, and propose a novel approach to build a hierarchy of explanations based on feature interactions. The proposed method is evaluated with three neural classifiers, LSTM, CNN, and BERT, on two benchmark text classification datasets. The generated explanations are assessed by both automatic evaluation measurements and human evaluators. Experiments show the effectiveness of the proposed method in providing explanations that are both faithful to models, and understandable to humans.

## item_id: m_1191

TITLE: OUMG: Objective and Universal Metric for Text Generation with Guiding Ability

ABSTRACT: Existing evaluation metrics for text generation rely on comparing candidate sentences to reference sentences. Some text generation tasks, such as story generation and poetry generation, have no fixed optimal answer and cannot match a corresponding reference for each sentence. Therefore, there is a lack of an objective and universal evaluation metric. To this end, we propose OUMG, a general metric that does not depend on reference standards. We train a discriminator to distinguish between human-generated and machine-generated text, which is used to score the sentences generated by the model. These scores reflect how similar the sentences are to human-generated texts. The capability of the discriminator can be measured by its accuracy, so it avoids the subjectivity of human judgments. Furthermore, the trained discriminator can also guide the text generation process to improve model performance. Experiments on poetry generation demonstrate that OUMG can objectively evaluate text generation models without reference standards. After combining the discriminator with the generation model, the original model can produce significantly higher quality results.

## item_id: m_1192

TITLE: POP-Norm: A Theoretically Justified and More Accelerated Normalization Approach

ABSTRACT: Batch Normalization (BatchNorm) has been a default module in  modern deep networks  due to its effectiveness for accelerating training deep neural networks.  It is widely accepted that the great success of BatchNorm is owing to reduction of internal covariate shift (ICS), but recently it is demonstrated that the link between them is fairly weak. The intrinsic reason behind effectiveness of BatchNorm is still unrevealed that limits it to be made better use. In light of this,  we propose a new normalization approach,  referred to as Pre-Operation Normalization (POP-Norm), which is theoretically ensured to speed up the training convergence. Not surprisingly, POP-Norm and BatchNorm are largely the same. Hence the similarities  can help us to theoretically interpret the root of BatchNorm's effectiveness. There are still some significant distinctions between the two approaches. Just the distinctions make POP-Norm achieve faster convergence rate and better performance than BatchNorm, which are validated in extensive experiments on benchmark datasets: CIFAR10, CIFAR100 and ILSVRC2012.

## item_id: m_1193

TITLE: Minimax Optimization with Smooth Algorithmic Adversaries

ABSTRACT: This paper considers minimax optimization $\min_x \max_y f(x, y)$ in the challenging setting where $f$ can be both nonconvex in $x$ and nonconcave in $y$. Though such optimization problems arise in many machine learning paradigms including training generative adversarial networks (GANs) and adversarially robust models, from a theoretical point of view, two fundamental issues remain: (i) the absence of simple and efficiently computable optimality notions, and (ii) cyclic or diverging behavior of existing algorithms. This paper proposes a new theoretical framework for nonconvex-nonconcave minimax optimization that addresses both of the above issues. The starting point of this paper is the observation that, under a computational budget, the max-player can not fully maximize $f(x,\cdot)$ since nonconcave maximization is NP-hard in general. So, we propose a new framework, and a corresponding algorithm, for the min-player to play against \emph{smooth algorithms} deployed by the adversary (i.e., the max-player) instead of against full maximization. Our algorithm is guaranteed to make monotonic progress (thus having no limit cycles or diverging behavior), and to find an appropriate ``stationary point'' in a polynomial number of iterations. Our framework covers practically relevant settings where the smooth algorithms deployed by the adversary are multi-step stochastic gradient ascent, and its accelerated version. We further present experimental results that confirm our theoretical findings and demonstrate the effectiveness of the proposed approach in practice on simple, conceptual settings.

## item_id: m_1194

TITLE: Stochastic Latent Residual Video Prediction

ABSTRACT: Video prediction is a challenging task: models have to account for the inherent uncertainty of the future. Most works in the literature are based on stochastic image-autoregressive recurrent networks, raising several performance and applicability issues. An alternative is to use fully latent temporal models which untie frame synthesis and dynamics. However, no such model for video prediction has been proposed in the literature yet, due to design and training difficulties. In this paper, we overcome these difficulties by introducing a novel stochastic temporal model. It is based on residual updates of a latent state, motivated by discretization schemes of differential equations. This first-order principle naturally models video dynamics as it allows our simpler, lightweight, interpretable, latent model to outperform prior state-of-the-art methods on challenging datasets.

## item_id: m_1195

TITLE: Prompt-Agnostic Erasure for Diffusion Models Using Task Vectors

ABSTRACT: With the rapid growth of text-to-image models, a variety of techniques have been suggested to prevent undesirable image generations. Yet, these methods often only protect against specific user prompts and have been shown to allow undesirable generations with other inputs. Here we focus on \textit{unconditionally} erasing a concept from a text-to-image model rather than conditioning the erasure on the user's prompt. We first show that compared to input-dependent erasure methods, concept erasure that uses Task Vectors (TV) is more robust to unexpected user inputs, not seen during training. However, TV-based erasure can also affect the core performance of the edited model, particularly when the required edit strength is unknown. To this end, we propose a method called \textit{Diverse Inversion}, which we use to estimate the required strength of the TV edit. Diverse Inversion finds within the model input space a large set of word embeddings, each of which induces the generation of the target concept. We find that encouraging diversity in the set makes our estimation more robust to unexpected prompts. Finally, we show that Diverse Inversion enables us to apply a TV edit only to a subset of the model weights, enhancing the erasure capabilities while better maintaining model utility.

## item_id: m_1196

TITLE: Tuning Recurrent Neural Networks with Reinforcement Learning

ABSTRACT: The approach of training sequence models using supervised learning and next-step prediction  suffers from known failure modes. For example, it is notoriously difficult to ensure multi-step generated sequences have coherent global structure. We propose a novel sequence-learning approach in which we use a pre-trained Recurrent Neural Network (RNN) to supply part of the reward value in a Reinforcement Learning (RL) model. Thus, we can refine a sequence predictor by optimizing for some imposed reward functions, while maintaining good predictive properties learned from data. We propose efficient ways to solve this by augmenting deep Q-learning with a cross-entropy reward and deriving novel off-policy methods for RNNs from KL control. We explore the usefulness of our approach in the context of music generation. An LSTM is trained on a large corpus of songs to predict the next note in a musical sequence. This Note RNN is then refined using our method and rules of music theory. We show that by combining maximum likelihood (ML) and RL in this way, we can not only produce more pleasing melodies, but  significantly reduce unwanted behaviors and failure modes of the RNN, while maintaining information learned from data.

## item_id: m_1197

TITLE: Learning Deep Improvement Representation to Accelerate Evolutionary Optimization

ABSTRACT: Evolutionary algorithms excel at versatile optimization for complex (e.g., multiobjective) problems but can be computationally expensive, especially in high-dimensional scenarios, and their stochastic nature of search may hinder swift convergence to global optima in promising directions. In this study, we train a multilayer perceptron (MLP) to learn the improvement representation of transitioning from poor-performing to better-performing solutions during evolutionary search, facilitating the rapid convergence of the evolutionary population towards global optimality along more promising paths. Then, through the iterative stacking of the previously trained lightweight MLP, a larger model can be constructed, enabling it to acquire deep improvement representations (DIR) for solutions. Conducting evolutionary search within the acquired DIR space significantly expedites the population's convergence rate. Finally, the efficacy of DIR-guided search is validated by applying it to the two prevailing evolutionary operators—simulated binary crossover and differential evolution. The experimental findings demonstrate its capability to achieve rapid convergence in solving challenging large-scale multiobjective optimization problems.

## item_id: m_1198

TITLE: Self-supervised Discovery of Human Actons from Long Kinematic Videos

ABSTRACT: For human action understanding, a popular research direction is to analyze short video clips with unambiguous semantic content, such as jumping and drinking. However, methods for understanding short semantic actions cannot be directly translated to long kinematic sequences such as dancing, where it becomes challenging even to semantically label the human movements. To promote analysis of long videos of complex human motions, we propose a self-supervised method for learning a representation of such motion sequences that is similar to words in a sentence, where videos are segmented and clustered into recurring temporal patterns, called actons. Our approach first obtains a frame-wise representation by contrasting two augmented views of video frames conditioned on their temporal context. The frame-wise representations across a collection of videos are then clustered by K-means. Actons are then automatically extracted by forming a continuous motion sequence from frames within the same cluster. We evaluate the self-supervised representation by temporal alignment metrics, and the clustering results by normalized mutual information and language entropy. We also study an application of this tokenization by using it to classify dance genres. On AIST++ and PKU-MMD datasets, actons are shown to bring significant performance improvements compared to several baselines.

## item_id: m_1199

TITLE: GEOMETRIC AUGMENTATION FOR ROBUST NEURAL NETWORK CLASSIFIERS

ABSTRACT: We introduce a novel geometric perspective and unsupervised model augmentation framework for transforming traditional deep (convolutional) neural networks into adversarially robust classifiers. Class-conditional probability densities based on Bayesian nonparametric mixtures of factor analyzers (BNP-MFA) over the input space are used to design soft decision labels for feature to label isometry. Classconditional distributions over features are also learned using BNP-MFA to develop plug-in maximum a posterior (MAP) classifiers to replace the traditional multinomial logistic softmax classification layers. This novel unsupervised augmented framework, which we call geometrically robust networks (GRN), is applied to CIFAR-10, CIFAR-100, and to Radio-ML (a time series dataset for radio modulation recognition). We demonstrate the robustness of GRN models to adversarial attacks from fast gradient sign method, Carlini-Wagner, and projected gradient descent.

## item_id: m_1200

TITLE: Efficient OCR for Building a Diverse Digital History

ABSTRACT: Many users consult digital archives daily, but the information they can access is unrepresentative of the diversity of documentary history. The sequence-to-sequence architecture typically used for optical character recognition (OCR) – which jointly learns a vision and language model - is poorly extensible to low-resource document collections, as learning a language-vision model requires extensive labeled sequences and compute. This study models OCR as a character level image retrieval problem, using a contrastively trained vision encoder. Because the model only learns characters’ visual features, it is more sample efficient and extensible than existing architectures, enabling accurate OCR in settings where existing solutions fail. Crucially, it opens new avenues for community engagement in making digital history more representative of documentary history.
