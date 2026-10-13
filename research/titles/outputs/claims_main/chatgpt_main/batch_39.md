# Batch 39 — 100 items

## item_id: m_3801

TITLE: COCO-Periph: Bridging the Gap Between Human and Machine Perception in the Periphery

ABSTRACT: Evaluating deep neural networks (DNNs) as models of human perception has given rich insights into both human visual processing and representational properties of DNNs. We extend this work by analyzing how well DNNs perform compared to humans when constrained by peripheral vision -- which limits human performance on a variety of tasks, but also benefits the visual system significantly. We evaluate this by (1) modifying the Texture Tiling Model (TTM), a well tested model of peripheral vision to be more flexibly used with DNNs, (2) generating a large dataset which we call COCO-Periph that contains images transformed to capture the information available in human peripheral vision, and (3) comparing DNNs to humans at peripheral object detection using a psychophysics experiment. Our results show that common DNNs underperform at object detection compared to humans when simulating peripheral vision with TTM. Training on COCO-Periph begins to reduce the gap between human and DNN performance and leads to small increases in corruption robustness, but DNNs still struggle to capture human-like sensitivity to peripheral clutter. Our work brings us closer to accurately modeling human vision, and paves the way for DNNs to mimic and sometimes benefit from properties of human visual processing.

## item_id: m_3802

TITLE: IRGS++: Robust Geometry, Material, and Light Decomposition with Accelerated Inter-Reflective Gaussian Splatting

ABSTRACT: The accurate evaluation of the rendering equation is a fundamental challenge in inverse rendering, as it governs the modeling of complex light-surface interactions. Existing 3DGS-based methods face a key trade-off: approaches using split-sum approximations fail to model secondary light effects, while those relying on heavy Monte Carlo integration suffer significant rendering slowdowns. To address this, we present IRGS++, an accelerated inter-reflective Gaussian splatting framework for inverse rendering that effectively handles both low-gloss and glossy materials. To reduce ray sampling in Monte Carlo integration, we implement multiple importance sampling with distinct distributions (cosine, GGX, and light sampling) to better capture light effects. We also apply a cross-bilateral filter to the Monte Carlo estimator, reducing noise while preserving quality with limited ray samples. Furthermore, we replace 2D Gaussian ray tracing with mesh-based ray tracing during relighting, cutting per-ray computations from hundreds of ray-splat checks to a single ray-triangle intersection. Extensive experiments demonstrate IRGS++'s superior performance among 3DGS-based competitors on both low-gloss and glossy datasets while achieving a 50-fold acceleration over IRGS.

## item_id: m_3803

TITLE: Unsupervised Document Representation using Partition Word-Vectors Averaging

ABSTRACT: Learning effective document-level representation is essential in many important NLP tasks such as document classification, summarization, etc. Recent research has shown that simple weighted averaging of word vectors is an effective way to represent sentences, often outperforming complicated seq2seq neural models in many tasks. While it is desirable to use the same method to represent documents as well, unfortunately, the effectiveness is lost when representing long documents involving multiple sentences. One reason for this degradation is due to the fact that a longer document is likely to contain words from many different themes (or topics), and hence creating a single vector while ignoring all the thematic structure is unlikely to yield an effective representation of the document. This problem is less acute in single sentences and other short text fragments where presence of a single theme/topic is most likely. To overcome this problem, in this paper we present PSIF, a partitioned word averaging model to represent long documents. P-SIF retains the simplicity of simple weighted word averaging while taking a document's thematic structure into account. In particular, P-SIF learns topic-specific vectors from a document and finally concatenates them all to represent the overall document. Through our experiments over multiple real-world datasets and tasks, we demonstrate PSIF's effectiveness compared to simple weighted averaging and many other state-of-the-art baselines. We also show that PSIF is particularly effective in representing long multi-sentence documents. We will release PSIF's embedding source code and data-sets for reproducing results.

## item_id: m_3804

TITLE: Continuous Convolutional Neural Network forNonuniform Time Series

ABSTRACT: Convolutional neural network (CNN) for time series data implicitly assumes that the data are uniformly sampled, whereas many event-based and multi-modal data are nonuniform or have heterogeneous sampling rates. Directly applying regularCNN to nonuniform time series is ungrounded, because it is unable to recognize and extract common patterns from the nonuniform input signals. Converting the nonuniform time series to uniform ones by interpolation preserves the pattern extraction capability of CNN, but the interpolation kernels are often preset and may be unsuitable for the data or tasks. In this paper, we propose the ContinuousCNN (CCNN), which estimates the inherent continuous inputs by interpolation, and performs continuous convolution on the continuous input. The interpolation and convolution kernels are learned in an end-to-end manner, and are able to learn useful patterns despite the nonuniform sampling rate. Besides, CCNN is a strict generalization to CNN. Results of several experiments verify that CCNN achieves abetter performance on nonuniform data, and learns meaningful continuous kernels

## item_id: m_3805

TITLE: Expert Proximity as Surrogate Rewards for Single Demonstration Imitation Learning

ABSTRACT: This study investigates the challenging single-demonstration imitation learning (IL) setting. In this context, the learning agent relies solely on a single expert demonstration and operates in an environment that lacks external reward signals, human feedback, or prior analogous knowledge, as obtaining multiple demonstrations or engineering complex reward functions is often infeasible. Given these constraints, the study introduces a methodology termed Transition Discriminator-based IL (TDIL). TDIL aims to augment the density of available reward signals and enhance agent performance by incorporating environmental dynamics. It posits that rather than strictly adhering to a limited expert demonstration, the agent should first aim to reach states proximal to expert behavior. The study introduces a surrogate reward function, approximated by a transition discriminator, to facilitate this process. TDIL demonstrates promise in addressing the sparse-reward problem common in single-demonstration IL, and stabilizing the learning process of the agent during training. A comprehensive set of experiments across multiple benchmarks validate the effectiveness of TDIL over existing IL methods.

## item_id: m_3806

TITLE: Improving Sampling from Generative Autoencoders with Markov Chains

ABSTRACT: We focus on generative autoencoders, such as variational or adversarial autoencoders, which jointly learn a generative model alongside an inference model. Generative autoencoders are those which are trained to softly enforce a prior on the latent distribution learned by the inference model. We call the distribution to which the inference model maps observed samples, the learned latent distribution, which may not be consistent with the prior. We formulate a Markov chain Monte Carlo (MCMC) sampling process, equivalent to iteratively decoding and encoding, which allows us to sample from the learned latent distribution. Since, the generative model learns to map from the learned latent distribution, rather than the prior, we may use MCMC to improve the quality of samples drawn from the generative model, especially when the learned latent distribution is far from the prior. Using MCMC sampling, we are able to reveal previously unseen differences between generative autoencoders trained either with or without a denoising criterion.

## item_id: m_3807

TITLE: Improving Sentence Representations with Multi-view Frameworks

ABSTRACT: Multi-view learning can provide self-supervision when different views are available of the same data. Distributional hypothesis provides another form of useful self-supervision from adjacent sentences which are plentiful in large unlabelled corpora. Motivated by the asymmetry in the two hemispheres of the human brain as well as the observation that different learning architectures tend to emphasise different aspects of sentence meaning, we present two multi-view frameworks for learning sentence representations in an unsupervised fashion. One framework uses a generative objective and the other a discriminative one. In both frameworks, the final representation is an ensemble of two views, in which, one view encodes the input sentence with a Recurrent Neural Network (RNN), and the other view encodes it with a simple linear model. We show that, after learning, the vectors produced by our multi-view frameworks provide improved representations over their single-view learnt counterparts, and the combination of different views gives representational improvement over each view and demonstrates solid transferability on standard downstream tasks.

## item_id: m_3808

TITLE: A Self-Organizing Memory Network

ABSTRACT: Working memory requires information about external stimuli to be represented in the brain even after those stimuli go away. This information is encoded in the activities of neurons, and neural activities change over timescales of tens of milliseconds. Information in working memory, however, is retained for tens of seconds, suggesting the question of how time-varying neural activities maintain stable representations. Prior work shows that, if the neural dynamics are in the `  null space' of the representation - so that changes to neural activity do not affect the downstream read-out of stimulus information - then information can be retained for periods much longer than the time-scale of individual-neuronal activities. The prior work, however, requires precisely constructed synaptic connectivity matrices, without explaining how this would arise in a biological neural network. To identify mechanisms through which biological networks can self-organize to learn  memory function, we derived biologically plausible synaptic plasticity rules that dynamically modify the connectivity matrix to enable information storing. Networks implementing this plasticity rule can successfully learn to form memory representations even if only 10% of the synapses are plastic, they are robust to synaptic noise, and they can represent information about multiple stimuli. 

## item_id: m_3809

TITLE: HyPHEN: A Hybrid Packing Method and Optimizations for Homomorphic Encryption-Based Neural Network 

ABSTRACT: Private Inference (PI) enables users to enjoy secure AI inference services while companies comply with regulations. Fully Homomorphic Encryption (FHE) based Convolutional Neural Network (CNN) inference is promising as users can offload the whole computation process to the server while protecting the privacy of sensitive data. Recent advances in AI research have enabled HE-friendly deep CNN like ResNet. However, FHE-based CNN (HCNN) suffers from high computational overhead. 
Prior HCNN approaches rely on dense packing techniques that aggregate as many channels into the ciphertext to reduce element-wise operations like multiplication and bootstrapping.
However, these approaches require performing an excessive amount of homomorphic rotations to accumulate channels and maintain dense data organization, which takes up most of the runtime.
To overcome this limitation, we present HyPHEN, a deep HCNN implementation that drastically reduces the number of homomorphic rotations.
HyPHEN utilizes a novel convolution algorithm, RAConv, utilizing replication-based data organization, which leads to a significant reduction in rotation count.
Furthermore, we propose hybrid gap packing method for HyPHEN, which gathers sparse convolution results into a dense data organization with a marginal increase in the number of rotations.
HyPHEN explores the trade-off between the computational costs of rotations and other operations, and finds the optimal point minimizing the execution time.
With these optimizations, HyPHEN takes 3.8-4.9$\times$ less execution time than the state-of-the-art HCNN implementation and brings the runtimes of ResNet inference down to 1.38-14.86s using a GPU-accelerated HEAAN library.

## item_id: m_3810

TITLE: Improving Learning from Demonstrations by Learning from Experience

ABSTRACT:     How to make imitation learning more general when demonstrations are relative limited has been a persistent problem in reinforcement learning (RL). Poor demonstrations leads to narrow and biased date distribution, non-Markovian human expert demonstration makes it difficult for the agent to learn, and over-reliance on sub-optimal trajectories can make it hard for the agent to improve its performance. To solve these problems we propose a new algorithm named TD3fG that can smoothly transition from learning from experts to learning from experience. Our algorithm achieve good performance in mujoco environment with limited and sub-optimal demonstrations.
    We use behavior cloning to train network as a reference action generator and utilize it in terms of both loss function and exploration noise. This innovation can help agents extract a priori knowledge from demonstrations while reducing the detrimental effects of the poor Markovian properties of the demonstrations. It has better performance compared to the BC+ fine-tuning and DDPGfD approach, especially when the demonstrations are relatively limited. We call our method TD3fG meaning TD3 from a generator.

## item_id: m_3811

TITLE: The Conditional Entropy Bottleneck

ABSTRACT: We present a new family of objective functions, which we term the Conditional Entropy Bottleneck (CEB). These objectives are motivated by the Minimum Necessary Information (MNI) criterion. We demonstrate the application of CEB to classification tasks. We show that CEB gives: well-calibrated predictions; strong detection of challenging out-of-distribution examples and powerful whitebox adversarial examples; and substantial robustness to those adversaries. Finally, we report that CEB fails to learn from information-free datasets, providing a possible resolution to the problem of generalization observed in Zhang et al. (2016).

## item_id: m_3812

TITLE: JOOCI: A FRAMEWORK FOR LEARNING COMPREHENSIVE SPEECH REPRESENTATIONS

ABSTRACT: Information in speech can be divided into two categories: what is being said (content) and how it is expressed (other). Current state-of-the-art (SOTA) techniques model speech at fixed segments, usually 10-25 ms, using a single embedding. Given the orthogonal nature of other and content information, attempting to optimize both within a single embedding results in suboptimal solutions. This approach divides the model's capacity, limiting its ability to build complex hierarchical features effectively. In this work, we present an end-to-end speech representation learning framework designed to jointly optimize the other and \enquote{content} information (JOOCI) in speech. By using separate learnable parameters, JOOCI addresses this optimization challenge by modeling other and content information independently. Our results show that JOOCI consistently outperforms other SOTA models of similar size (100 million parameters) and pre-training data used (960 hours) by a significant margin when evaluated on a range of speech downstream tasks in the SUPERB benchmark. Code and models are available at TBA.

## item_id: m_3813

TITLE: The Close Relationship Between Contrastive Learning and Meta-Learning

ABSTRACT: Contrastive learning has recently taken off as a paradigm for learning from unlabeled data. In this paper, we discuss the close relationship between contrastive learning and meta-learning under a certain task distribution. We complement this observation by showing that established meta-learning methods, such as Prototypical Networks, achieve comparable performance to SimCLR when paired with this task distribution. This relationship can be leveraged by taking established techniques from meta-learning, such as task-based data augmentation, and showing that they benefit contrastive learning as well. These tricks also benefit state-of-the-art self-supervised learners without using negative pairs such as BYOL, which achieves 94.6\% accuracy on CIFAR-10 using a self-supervised ResNet-18 feature extractor trained with our meta-learning tricks.  We conclude that existing advances designed for contrastive learning or meta-learning can be exploited to benefit the other, and it is better for contrastive learning researchers to take lessons from the meta-learning literature (and vice-versa) than to reinvent the wheel. 

## item_id: m_3814

TITLE: Active Neural Localization

ABSTRACT: Localization is the problem of estimating the location of an autonomous agent from an observation and a map of the environment. Traditional methods of localization, which filter the belief based on the observations, are sub-optimal in the number of steps required, as they do not decide the actions taken by the agent. We propose "Active Neural Localizer", a fully differentiable neural network that learns to localize efficiently. The proposed model incorporates ideas of traditional filtering-based localization methods, by using a structured belief of the state with multiplicative interactions to propagate belief, and combines it with a policy model to minimize the number of steps required for localization. Active Neural Localizer is trained end-to-end with reinforcement learning. We use a variety of simulation environments for our experiments which include random 2D mazes, random mazes in the Doom game engine and a photo-realistic environment in the Unreal game engine. The results on the 2D environments show the effectiveness of the learned policy in an idealistic setting while results on the 3D environments demonstrate the model's capability of learning the policy and perceptual model jointly from raw-pixel based RGB observations. We also show that a model trained on random textures in the Doom environment generalizes well to a photo-realistic office space environment in the Unreal engine. 

## item_id: m_3815

TITLE: Universality, Robustness, and Detectability of Adversarial Perturbations under Adversarial Training

ABSTRACT: Classifiers such as deep neural networks have been shown to be vulnerable against adversarial perturbations on problems with high-dimensional input space. While adversarial training improves the robustness of classifiers against such adversarial perturbations, it leaves classifiers sensitive to them on a non-negligible fraction of the inputs. We argue that there are two different kinds of adversarial perturbations: shared perturbations which fool a classifier on many inputs and singular perturbations which only fool the classifier on a small fraction of the data. We find that adversarial training increases the robustness of classifiers against shared perturbations. Moreover, it is particularly effective in removing universal perturbations, which can be seen as an extreme form of shared perturbations. Unfortunately, adversarial training does not consistently increase the robustness against singular perturbations on unseen inputs. However, we find that adversarial training decreases robustness of the remaining perturbations against image transformations such as changes to contrast and brightness or  Gaussian blurring. It thus makes successful attacks on the classifier in the physical world less likely. Finally, we show that even singular perturbations can be easily detected and must thus exhibit generalizable patterns even though the perturbations are specific for certain inputs. 

## item_id: m_3816

TITLE: Trading Quality for Efficiency of Graph Partitioning: An Inductive Method across Graphs

ABSTRACT: Many applications of network systems can be formulated as several NP-hard combinatorial optimization problems regarding graph partitioning (GP), e.g., modularity maximization and NCut minimization. Due to the NP-hardness, to balance the quality and efficiency of GP remains a challenge. Existing methods use machine learning techniques to obtain high-quality solutions but usually have high complexity. Some fast GP methods adopt heuristic strategies to ensure low runtime but suffer from quality degradation. In contrast to conventional transductive GP methods applied to a static graph, we propose an inductive graph partitioning (IGP) framework across multiple evolving graph snapshots to alleviate the NP-hard challenge. IGP first conducts the offline training of a novel dual graph neural network on historical snapshots to capture the structural properties of a system. The trained model is then generalized to newly generated snapshots for fast high-quality online GP without additional optimization, where a better trade-off between quality and efficiency is achieved. IGP is also a generic framework that can capture the permutation invariant partitioning ground-truth of historical snapshots in the offline training and tackle the online GP on graphs with non-fixed number of nodes and clusters. Experiments on a set of benchmarks demonstrate that IGP achieves competitive quality and efficiency to various state-of-the-art baselines.

## item_id: m_3817

TITLE: Using Contrastive Learning with Generative Similarity to Learn Spaces that Capture Human Inductive Biases

ABSTRACT: Humans rely on strong inductive biases to learn from few examples and abstract useful information from sensory data. Instilling such biases in machine learning models has been shown to improve their performance on various benchmarks including few-shot learning, robustness, and alignment. However, finding effective training procedures to achieve that goal can be challenging as psychologically-rich training data such as human similarity judgments are expensive to scale, and Bayesian models of human inductive biases are often intractable for complex, realistic domains. Here, we address this challenge by introducing a Bayesian notion of generative similarity whereby two datapoints are considered similar if they are likely to have been sampled from the same distribution. This measure can be applied to complex generative processes, including probabilistic programs. We show that generative similarity can be used to define a contrastive learning objective even when its exact form is intractable, enabling learning of spatial embeddings that express specific inductive biases. We demonstrate the utility of our approach by showing that it can be used to capture human inductive biases for geometric shapes, distinguish different abstract drawing styles that are parameterized by probabilistic programs, and capture abstract high-level categories that enable generalization.

## item_id: m_3818

TITLE: LSTM-Based System-Call Language Modeling and Ensemble Method for Host-Based Intrusion Detection

ABSTRACT: In computer security, designing a robust intrusion detection system is one of the most fundamental and important problems. In this paper, we propose a system-call language-modeling approach for designing anomaly-based host intrusion detection systems. To remedy the issue of high false-alarm rates commonly arising in conventional methods, we employ a novel ensemble method that blends multiple thresholding classifiers into a single one, making it possible to accumulate `highly normal' sequences. The proposed system-call language model has various advantages leveraged by the fact that it can learn the semantic meaning and interactions of each system call that existing methods cannot effectively consider. Through diverse experiments on public benchmark datasets, we demonstrate the validity and effectiveness of the proposed method. Moreover, we show that our model possesses high portability, which is one of the key aspects of realizing successful intrusion detection systems.

## item_id: m_3819

TITLE: Highway and Residual Networks learn Unrolled Iterative Estimation

ABSTRACT: The past year saw the introduction of new architectures such as Highway networks and Residual networks which, for the first time, enabled the training of feedforward networks with dozens to hundreds of layers using simple gradient descent.
While depth of representation has been posited as a primary reason for their success, there are indications that these architectures defy a popular view of deep learning as a hierarchical computation of increasingly abstract features at each layer.

In this report, we argue that this view is incomplete and does not adequately explain several recent findings.
We propose an alternative viewpoint based on unrolled iterative estimation---a group of successive layers iteratively refine their estimates of the same features instead of computing an entirely new representation.
We demonstrate that this viewpoint directly leads to the construction of highway and residual networks. 
Finally we provide preliminary experiments to discuss the similarities and differences between the two architectures.

## item_id: m_3820

TITLE: AdaSpeech: Adaptive Text to Speech for Custom Voice

ABSTRACT: Custom voice, a specific text to speech (TTS) service in commercial speech platforms, aims to adapt a source TTS model to synthesize personal voice for a target speaker using few speech from her/him. Custom voice presents two unique challenges for TTS adaptation: 1) to support diverse customers, the adaptation model needs to handle diverse acoustic conditions which could be very different from source speech data, and 2) to support a large number of customers, the adaptation parameters need to be small enough for each target speaker to reduce memory usage while maintaining high voice quality. In this work, we propose AdaSpeech, an adaptive TTS system for high-quality and efficient customization of new voices. We design several techniques in AdaSpeech to address the two challenges in custom voice: 1) To handle different acoustic conditions, we model the acoustic information in both utterance and phoneme level. Specifically, we use one acoustic encoder to extract an utterance-level vector and another one to extract a sequence of phoneme-level vectors from the target speech during pre-training and fine-tuning; in inference, we extract the utterance-level vector from a reference speech and use an acoustic predictor to predict the phoneme-level vectors. 2) To better trade off the adaptation parameters and voice quality, we introduce conditional layer normalization in the mel-spectrogram decoder of AdaSpeech, and fine-tune this part in addition to speaker embedding for adaptation. We pre-train the source TTS model on LibriTTS datasets and fine-tune it on VCTK and LJSpeech datasets (with different acoustic conditions from LibriTTS) with few adaptation data, e.g., 20 sentences, about 1 minute speech. Experiment results show that AdaSpeech achieves much better adaptation quality than baseline methods, with only about 5K specific parameters for each speaker, which demonstrates its effectiveness for custom voice. The audio samples are available at https://speechresearch.github.io/adaspeech/.

## item_id: m_3821

TITLE: The Expressive Power of Deep Neural Networks with Circulant Matrices

ABSTRACT: Recent results from linear algebra stating that any matrix can be decomposed into products of diagonal and circulant matrices has lead to the design of compact deep neural network architectures that perform well in practice. In this paper, we bridge the gap between these good empirical results 
and the theoretical approximation capabilities of Deep diagonal-circulant ReLU networks. More precisely, we first demonstrate  that a Deep diagonal-circulant ReLU networks of
bounded width and small depth can approximate a deep ReLU network in which the dense matrices are
of low rank. Based on this result, we provide new bounds on the expressive power and universal approximativeness of this type of networks. We support our experimental results with thorough experiments on a large, real world video classification problem.

## item_id: m_3822

TITLE: OscillationInversion: Understand the structure of Large Flow Model through the Lens of Inversion Method

ABSTRACT: We investigate oscillation phenomena observed in inversion methods applied to large text-to-image diffusion models, particularly the ``Flux'' model. Using a fixed-point-inspired iteration method to invert real-world images, we find that the solution does not converge but instead oscillates between distinct clusters. Our results, validated both on real diffusion models and toy experiments, show that these oscillated clusters exhibit significant semantic coherence. 
We propose that this phenomenon arises from oscillatory solutions in dynamic systems, linking it to the structure of rectified flow models. The oscillated clusters serve as local latent distributions that allow for effective semantic-based image optimization.We provide theoretical insights, linking these oscillations to fixed-point dynamics and proving conditions for stable cluster formation and differentiation in flow models.

## item_id: m_3823

TITLE: Play by the Type Rules: Inferring Constraints for LLM Functions in Declarative Programs

ABSTRACT: Integrating LLM powered operators in declarative query languages allows for the combination of cheap and interpretable functions with powerful, generalizable language model reasoning. However, in order to benefit from the optimized execution of a database query language like SQL, generated outputs must align with the rules enforced by both type checkers and database contents. Current approaches address this challenge with orchestrations consisting of many LLM-based post-processing calls to ensure alignment between generated outputs and database values, introducing performance bottlenecks. We perform a study on the ability of various sized open-source language models to both parse and execute functions within a query language based on SQL, showing that small language models can excel as function executors over hybrid data sources. Then, we propose an efficient solution to enforce the well-typedness of LLM functions, demonstrating 7% accuracy improvement on a multi-hop question answering dataset with 53% improvement in latency over comparable solutions.

## item_id: m_3824

TITLE: Improving the Gating Mechanism of Recurrent Neural Networks

ABSTRACT: In this work, we revisit the gating mechanisms widely used in various recurrent and feedforward networks such as LSTMs, GRUs, or highway networks. These gates are meant to control information flow, allowing gradients to better propagate back in time for recurrent models. However, to propagate gradients over very long temporal windows, they need to operate close to their saturation regime. We propose two independent and synergistic modifications to the standard gating mechanism that are easy to implement, introduce no additional hyper-parameters, and are aimed at improving learnability of the gates when they are close to saturation. Our proposals are theoretically justified, and we show a generic framework that encompasses other recently proposed gating mechanisms such as chrono-initialization and master gates . We perform systematic analyses and ablation studies on the proposed improvements and evaluate our method on a wide range of applications including synthetic memorization tasks, sequential image classification, language modeling, and reinforcement learning.  Empirically, our proposed gating mechanisms robustly increase the performance of recurrent models such as LSTMs, especially on tasks requiring long temporal dependencies.

## item_id: m_3825

TITLE: Interpreting the Inner Mechanisms of Large Language Models in Mathematical Addition

ABSTRACT: Large language models (LLMs) have achieved stunning performance on various language tasks, but remain as mysterious as a black box. Understanding the internal mechanisms of LLMs could contribute to the development of more transparent and interpretable LLMs. To this end, we take the first attempt to reveal a specific mechanism relating to how LLMs implement the reasoning task of a mathematical addition, i.e., scenarios involving the addition of two integers. Through comprehensive experiments, we find that LLMs frequently involve a small fraction of attention heads (0.5% of all heads) when implementing the addition task. Meanwhile, knocking out these frequently involved heads significantly degrades the LLMs' performance on the same task. Surprisingly, these key heads identified for a specific model exhibit outstanding generalizability across multiple datasets related to the mathematical addition task. Moreover, we find an intuitive phenomenon that knocking out these key heads could also affect the performance of LLMs on mathematical subtraction, which shares the same spirit with human behavior. Our work serves as a preliminary exploration into the mathematical prowess of LLMs, laying a solid foundation to reveal more intricate capabilities.

## item_id: m_3826

TITLE: Towards Complete Expressiveness Capacity of Mixed Multi-Agent Q Value Function

ABSTRACT: Value decomposition is an efficient approach to achieving centralized training with decentralized execution in fully cooperative Multi-Agent Reinforcement Learning (MARL) problems. Recently, Strictly Monotonic Mixing Function (SMMF) has gained widespread application in value decomposition methods, but SMMF could suffer from convergence difficulties for the representational limitation. 
This paper investigates the circumstances under which the representational limitation occurs and presents approaches to overcome it. 
We begin our investigation with Linear Mixing Function (LMF), a simple case of SMMF.
Firstly, we prove that LMF is free from representational limitation only in a rare case of MARL problems.
Secondly, we propose a two-stage mixing framework, which includes a difference rescaling stage after SMMF to complete the representational capability.
However, the capacity could remain unrealized for the cross interference between the representation of different action-values. Finally, we introduce gradient shaping to address this problem. 
The experimental results validate the expressiveness of LMF and demonstrate the effectiveness of our proposed methods.

## item_id: m_3827

TITLE: Physics-as-Inverse-Graphics: Unsupervised Physical Parameter Estimation from Video

ABSTRACT: We propose a model that is able to perform physical parameter estimation of systems from video, where the differential equations governing the scene dynamics are known, but labeled states or objects are not available. Existing physical scene understanding methods require either object state supervision, or do not integrate with differentiable physics to learn interpretable system parameters and states. We address this problem through a \textit{physics-as-inverse-graphics} approach that brings together vision-as-inverse-graphics and differentiable physics engines, where objects and explicit state and velocity representations are discovered by the model. This framework allows us to perform long term extrapolative video prediction, as well as vision-based model-predictive control. Our approach significantly outperforms related unsupervised methods in long-term future frame prediction of systems with interacting objects (such as ball-spring or 3-body gravitational systems), due to its ability to build dynamics into the model as an inductive bias. We further show the value of this tight vision-physics integration by demonstrating data-efficient learning of vision-actuated model-based control for a pendulum system. We also show that the controller's interpretability provides unique capabilities in goal-driven control and physical reasoning for zero-data adaptation.

## item_id: m_3828

TITLE: Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

ABSTRACT: Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks. However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning. Both of these challenges severely limit the applicability of such methods to complex, real-world domains. In this paper, we propose soft actor-critic, an off-policy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework. In this framework, the actor aims to maximize expected reward while also maximizing entropy - that is, succeed at the task while acting as randomly as possible. Prior deep RL methods based on this framework have been formulated as either off-policy Q-learning, or on-policy policy gradient methods. By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods. Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds.

## item_id: m_3829

TITLE: Adversary A3C for Robust Reinforcement Learning

ABSTRACT: Asynchronous Advantage Actor Critic (A3C) is an effective Reinforcement Learning (RL) algorithm for a wide range of tasks, such as Atari games and robot control. The agent learns policies and value function through trial-and-error interactions with the environment until converging to an optimal policy. Robustness and stability are critical in RL; however, neural network can be vulnerable to noise from unexpected sources and is not likely to withstand very slight disturbances. We note that agents generated from mild environment using A3C are not able to handle challenging environments. Learning from adversarial examples, we proposed an algorithm called Adversary Robust A3C (AR-A3C) to improve the agent’s performance under noisy environments. In this algorithm, an adversarial agent is introduced to the learning process to make it more robust against adversarial disturbances, thereby making it more adaptive to noisy environments. Both simulations and real-world experiments are carried out to illustrate the stability of the proposed algorithm. The AR-A3C algorithm outperforms A3C in both clean and noisy environments. 

## item_id: m_3830

TITLE: A2BCD: Asynchronous Acceleration with Optimal Complexity

ABSTRACT: 	In this paper, we propose the Asynchronous Accelerated Nonuniform Randomized Block Coordinate Descent algorithm (A2BCD). We prove A2BCD converges linearly to a solution of the convex minimization problem at the same rate as NU_ACDM, so long as the maximum delay is not too large. This is the first asynchronous Nesterov-accelerated algorithm that attains any provable speedup. Moreover, we then prove that these algorithms both have optimal complexity. Asynchronous algorithms complete much faster iterations, and A2BCD has optimal complexity. Hence we observe in experiments that A2BCD is the top-performing coordinate descent algorithm, converging up to 4-5x faster than NU_ACDM on some data sets in terms of wall-clock time. To motivate our theory and proof techniques, we also derive and analyze a continuous-time analog of our algorithm and prove it converges at the same rate.

## item_id: m_3831

TITLE: FROM DEEP LEARNING TO DEEP DEDUCING: AUTOMATICALLY TRACKING DOWN NASH EQUILIBRIUM THROUGH AUTONOMOUS NEURAL AGENT, A POSSIBLE MISSING STEP TOWARD GENERAL A.I.

ABSTRACT: Contrary to most reinforcement learning studies, which emphasize on training a deep neural network to approximate its output layer to certain strategies, this paper proposes a reversed method for reinforcement learning. We call this “Deep Deducing”. In short, after adequately training a deep neural network according to a strategy-environment-to-payoff table, then we initialize randomized strategy
input and propagate the error between the actual output and the desired output back to the initially-randomized strategy input in the “input layer” of the trained deep neural network gradually to perform a task similar to “human deduction”. And we view the final strategy input in the “input layer” as the fittest strategy for a neural network when confronting the observed environment input from the world outside.

## item_id: m_3832

TITLE: Improving Neural Network Accuracy by Concurrently Training with a Twin Network

ABSTRACT: Recently within Spiking Neural Networks, a method called Twin Network Augmentation (TNA) has been introduced. This technique claims to improve the validation accuracy of a Spiking Neural Network simply by training two networks in conjunction and matching the logits via the Mean Squared Error loss. In this paper, we validate the viability of this method on a wide range of popular Convolutional Neural Network (CNN) benchmarks and compare this approach to existing Knowledge Distillation schemes. Next, we conduct a in-depth study of the different components that make up TNA and determine that its effectiveness is not solely situated in an increase of trainable parameters, but rather the effect of the training methodology. Finally, we analyse the representations learned by networks trained with TNA and highlight their superiority in a number of tasks, thus proving empirically the applicability of Twin Network Augmentation on CNN models.

## item_id: m_3833

TITLE: LLaMA Decoder As Vision Transformer

ABSTRACT: Using the same architecture for text and image is important for AI standardization. Recent multimodal models use a decoder-only Transformer to generate text and an encoder-only Transformer to extract image features. Can images use exactly the same language architecture? To answer this question, we aim at a LLaMa decoder as vision Transformer (ViT) classifier in this paper. Specifically, we start
our trajectory by “LLaMAfy” a standard ViT step-by-step, i.e., feed-forward net, normalization layer, causal self-attention and positional embedding, and point out a key issue—attention collapse—that result in the failure to the network training. Motivated by this observation, we propose post-sequence class token, enabling causal self-attention to efficiently capture the entire image’s information. To improve model optimization behavior and enhance performance, we then introduce a soft mask strategy to gradually transform the attention from bi-directional to causal mode. The tailored model, dubbed as image LLaMA (iLLaMA), maintains high consistency with LLaMA architecture, while matching up well against ViT, achieving 75.1% ImageNet top-1 accuracy with only 5.7M parameters. Scaling the model to ∼310M and pre-training on ImageNet-21K further enhances the accuracy to 86.0%. Its causal self-attention boosts computational efficiency and learns complex representation by elevating attention map ranks. Extensive experiments demonstrate iLLaMA’s reliable properties: shape-texture bias, calibration, quantization compatibility, ADE20K segmentation and CIFAR transfer learning. We hope our study can kindle fresh views to visual architectures in the era of LLMs and contributes to standardized AI models.

## item_id: m_3834

TITLE: The Invisible Leash? Why RLVR May or May Not Escape Its Origin

ABSTRACT: Recent advances in large reasoning models highlight Reinforcement Learning with Verifiable Rewards (RLVR) as a promising method for enhancing AI's capabilities, particularly in solving complex logical tasks. However, it remains unclear whether the current practice of RLVR truly expands a model's reasoning boundary or mainly amplifies high-reward outputs that the base model already knows for improved precision. This study presents an empirical investigation that provides fresh insights into the potential limits of the common practice of RLVR. We examine how, under current training conditions, RLVR can operate as a support-constrained optimization mechanism that may restrict the discovery of entirely original solutions, remaining constrained by the base model's initial distribution. We also identify an entropy–reward trade-off: while the current RLVR recipe reliably enhances precision, it may progressively narrow exploration and potentially overlook correct yet underrepresented solutions. Extensive empirical experiments validate that while the current RLVR recipe consistently improves \texttt{pass@1}, \textit{the shrinkage of empirical support generally outweighs the expansion of empirical support under larger sampling budgets}, failing to recover correct answers that were previously accessible to the base model. Interestingly, we also observe that while RLVR sometimes increases token-level entropy, it results in greater uncertainty at each generation step and declining answer-level entropy. This indicates that these seemingly more uncertain paths ultimately converge onto a smaller set of distinct answers. Taken together, we reveal potential limits of the current RLVR recipe in extending reasoning horizons. Breaking this invisible leash may require future algorithmic innovations such as explicit exploration mechanisms or hybrid strategies that seed probability mass into underrepresented solution regions.

## item_id: m_3835

TITLE: Effective Mechanism to Mitigate Injuries During NFL Plays 

ABSTRACT: NFL(American football),which is regarded as the premier sports icon of America, has been severely accused in the recent years of being exposed to dangerous injuries that prove to be a bigger crisis as the players' lives have been increasingly at risk. Concussions, which refer to the serious brain traumas experienced during the passage of NFL play, have displayed a  dramatic rise in the recent seasons concluding in an alarming rate in 2017/18. Acknowledging the potential risk, the NFL has been trying to fight via NeuroIntel AI mechanism as well as modifying existing  game rules and risky play practices to reduce the rate of concussions. As a remedy, we are suggesting an effective mechanism to extensively analyse the potential concussion risks by adopting predictive analysis to project injury risk percentage per each play and positional impact analysis to suggest safer team formation pairs to lessen injuries to offer a comprehensive study on NFL injury analysis. The proposed data analytical approach differentiates itself from the other similar approaches that were focused only on the descriptive analysis rather than going for a bigger context with predictive modelling and formation pairs mining that would assist in modifying existing rules to tackle injury concerns. The predictive model that works with Kafka-stream processor real-time inputs and risky formation pairs identification by designing FP-Matrix, makes this far-reaching solution to analyse injury data on various grounds wherever applicable.

## item_id: m_3836

TITLE: Joint Adaptation of Uni-modal Foundation Models for Multi-modal Alzheimer's Disease Diagnosis

ABSTRACT: Alzheimer’s Disease (AD) is a progressive neurodegenerative disorder and a leading cause of dementia worldwide. Accurate diagnosis requires integrating diverse patient data modalities. With the rapid advancement of foundation models in neurobiology and medicine, integrating foundation models from various modalities has emerged as a promising yet underexplored direction for multi-modal AD diagnosis. A central challenge is enabling effective interaction among these models without disrupting the robust, modality-specific representations learned from large-scale pretraining. To address this, we propose a novel multi-modal framework for AD diagnosis that enables joint interaction among uni-modal foundation models through modality-anchored interaction. In this framework, one modality and its corresponding foundation model are designated as an anchor, while the remaining modalities serve as auxiliary sources of complementary information. To preserve the pre-trained representation space of the anchor model, we propose modality-aware Q-formers that selectively map auxiliary modality features into the anchor model’s feature space, enabling the anchor model to jointly process its own features together with the seamlessly integrated auxiliary features. We evaluate our method on AD diagnosis and progression prediction across four modalities: sMRI, fMRI, clinical records, and genetic data. Our framework consistently outperforms prior methods in two modality settings, and further demonstrates strong generalization to external datasets and other neurodegenerative diseases such as Parkinson’s disease.

## item_id: m_3837

TITLE: An Information Theoretic Perspective on Disentangled Representation Learning

ABSTRACT: Existing works on disentangled representation learning usually lie on a common assumption: all factors in a disentangled representation should be independent. We argue that this assumption is not sufficient and another assumption is vital for disentangled representation learning: information contained in each factor of a disentangled representation is irrelevant to others, i.e. the containing information about data of factors is isolated. We formulate this assumption into two equivalent equations via mutual information, and theoretically show its relation with independence and conditional independence of factors in a representation. Meanwhile, we prove that conditional independence is satisfied in encoders of VAEs due to ``no-sharing-parameter block" and reparameterization trick. To highlight the importance of the proposed assumption, we show in experiments that violating the assumption leads to decline of disentanglement. Based on this assumption, we further propose to split the deeper layers in encoder to ensure parameters in these layers are not shared for different factors. The proposed encoder, called \textit{Split Encoder}, can be applied into other models and shows significant improvement in unsupervised learning of disentangled representations and reconstructions.

## item_id: m_3838

TITLE: Domino: Discovering Systematic Errors with Cross-Modal Embeddings

ABSTRACT: Machine learning models that achieve high overall accuracy often make systematic errors on important subsets (or slices) of data. Identifying underperforming slices is particularly challenging when working with high-dimensional inputs (e.g. images, audio), where important slices are often unlabeled. In order to address this issue, recent studies have proposed automated slice discovery methods (SDMs), which leverage learned model representations to mine input data for slices on which a model performs poorly. To be useful to a practitioner, these methods must identify slices that are both underperforming and coherent (i.e. united by a human-understandable concept). However, no quantitative evaluation framework currently exists for rigorously assessing SDMs with respect to these criteria. Additionally, prior qualitative evaluations have shown that SDMs often identify slices that are incoherent. In this work, we address these challenges by first designing a principled evaluation framework that enables a quantitative comparison of SDMs across 1,235 slice discovery settings in three input domains (natural images, medical images, and time-series data).
Then, motivated by the recent development of powerful cross-modal representation learning approaches, we present Domino, an SDM that leverages cross-modal embeddings and a novel error-aware mixture model to discover and describe coherent slices. We find that Domino accurately identifies 36% of the 1,235 slices in our framework -- a 12 percentage point improvement over prior methods. Further, Domino is the first SDM that can provide natural language descriptions of identified slices, correctly generating the exact name of the slice in 35% of settings. 

## item_id: m_3839

TITLE: Tessellated 2D Convolution Networks: A Robust Defence against Adversarial Attacks

ABSTRACT: Data-driven (deep) learning approaches for image classification are prone to adversarial attacks. This means that an adversarial crafted image which is sufficiently close (visually indistinguishable) to its representative class can often be misclassified to be a member of a different class. A reason why deep neural approaches exhibits such vulnerability towards adversarial threats is mainly because the abstract representations learned in a data-driven manner often do not correlate well with human perceived features. To mitigate this problem, we propose the tessellated 2d convolution network, a novel divide-and-conquer based approach, which first independently learns the abstract representations of non-overlapping regions within an image, and then learns how to combine these representations to infer its class. It turns out that a non-uniform tiling of an image which ensures that the difference between the maximum and the minimum region sizes is not too large is the most robust way to construct such a tessellated 2d convolution network. This criterion can be achieved, among other schemes, by using a Mondrian tessellation of the input image. Our experiments demonstrate that our tessellated networks provides a more robust defence mechanism against gradient-based adversarial attacks in comparison to conventional deep neural models.

## item_id: m_3840

TITLE: Boosted Residual Networks

ABSTRACT: In this paper we present a new ensemble method, called Boosted Residual Networks,
which builds an ensemble of Residual Networks by growing the member
network at each round of boosting. The proposed approach combines recent developements
in Residual Networks - a method for creating very deep networks by
including a shortcut layer between different groups of layers - with the Deep Incremental
Boosting, which has been proposed as a methodology to train fast ensembles
of networks of increasing depth through the use of boosting. We demonstrate
that the synergy of Residual Networks and Deep Incremental Boosting has better
potential than simply boosting a Residual Network of fixed structure or using the
equivalent Deep Incremental Boosting without the shortcut layers.

## item_id: m_3841

TITLE: Normalized Direction-preserving Adam

ABSTRACT: Optimization algorithms for training deep models not only affects the convergence rate and stability of the training process, but are also highly related to the generalization performance of trained models. While adaptive algorithms, such as Adam and RMSprop, have shown better optimization performance than stochastic gradient descent (SGD) in many scenarios, they often lead to worse generalization performance than SGD, when used for training deep neural networks (DNNs). In this work, we identify two problems regarding the direction and step size for updating the weight vectors of hidden units, which may degrade the generalization performance of Adam. As a solution, we propose the normalized direction-preserving Adam (ND-Adam) algorithm, which controls the update direction and step size more precisely, and thus bridges the generalization gap between Adam and SGD. Following a similar rationale, we further improve the generalization performance in classification tasks by regularizing the softmax logits. By bridging the gap between SGD and Adam, we also shed some light on why certain optimization algorithms generalize better than others.

## item_id: m_3842

TITLE: Visualizing Deep Neural Network Decisions: Prediction Difference Analysis

ABSTRACT: This article presents the prediction difference analysis method for visualizing the response of a deep neural network to a specific input. When classifying images, the method highlights areas in a given input image that provide evidence for or against a certain class. It overcomes several shortcoming of previous methods and provides great additional insight into the decision making process of classifiers. Making neural network decisions interpretable through visualization is important both to improve models and to accelerate the adoption of black-box classifiers in application areas such as medicine. We illustrate the method in experiments on natural images (ImageNet data), as well as medical images (MRI brain scans).

## item_id: m_3843

TITLE: InCo: Enhance Domain Generalization in Noisy Environments

ABSTRACT: The Invariant Risk Minimization (IRM) approach aims to address the challenge of domain generalization by training a feature representation that remains invariant across multiple environments. However, in noisy environments, IRM-related techniques such as IRMv1 and VREx may be unable to achieve the optimal IRM solution due to incorrect optimization directions. To address this issue, we introduce InCo (short for Invariant Correlation), a novel approach that effectively tackles the aforementioned challenges in noisy environments. Additionally, we provide a case study to analyze why previous methods may lose ground while InCo can succeed. We offer theoretical analysis from a causal perspective, demonstrating that the invariant correlation of representation with labels across environments is a necessary condition for the optimal invariant predictor in noisy environments, whereas the optimization motivations for other methods may not be. Subsequently, we empirically demonstrate the usefulness of InCo by comparing it with other domain generalization methods on various noisy datasets.

## item_id: m_3844

TITLE: Open-Ended Content-Style Recombination Via Leakage Filtering

ABSTRACT: We consider visual domains in which a class label specifies the content of an image, and class-irrelevant properties that differentiate instances constitute the style.  We present a domain-independent method that permits the open-ended recombination of style of one image with the content of another. Open ended simply means that the method generalizes to style and content not present in the training data. The method starts by constructing a content embedding using an existing deep metric-learning technique. This trained content encoder is incorporated into a variational autoencoder (VAE), paired with a to-be-trained style encoder. The VAE reconstruction loss alone is inadequate to ensure a decomposition of the latent representation into style and content. Our method thus includes an auxiliary loss, leakage filtering, which ensures that no style information remaining in the content representation is used for reconstruction and vice versa. We synthesize novel images by decoding the style representation obtained from one image with the content representation from another. Using this method for data-set augmentation, we obtain state-of-the-art performance on few-shot learning tasks.

## item_id: m_3845

TITLE: ROGA: Random Over-sampling Based on Genetic Algorithm

ABSTRACT: When using machine learning to solve practical tasks, we often face the problem of class imbalance. Unbalanced classes will cause the model to generate preferences during the learning process, thereby ignoring classes with fewer samples. The oversampling algorithm achieves the purpose of balancing the difference in quantity by generating a minority of samples. The quality of the artificial samples determines the impact of the oversampling algorithm on model training. Therefore, a challenge of the oversampling algorithm is how to find a suitable sample generation space. However, too strong conditional constraints can make the generated samples as non-noise points as possible, but at the same time they also limit the search space of the generated samples, which is not conducive to the discovery of better-quality new samples. Therefore, based on this problem, we propose an oversampling algorithm ROGA based on genetic algorithm. Based on random sampling, new samples are gradually generated and the samples that may become noise are filtered out. ROGA can ensure that the sample generation space is as wide as possible, and it can also reduce the noise samples generated. By verifying on multiple datasets, ROGA can achieve a good result.

## item_id: m_3846

TITLE: BOND: Aligning LLMs with Best-of-N Distillation

ABSTRACT: Reinforcement learning from human feedback (RLHF) is a key driver of quality and safety in state-of-the-art large language models.
Yet, a surprisingly simple and strong inference-time strategy is Best-of-N sampling that selects the best generation among N candidates.
In this paper, we propose Best-of-N Distillation (BOND), a novel RLHF algorithm that seeks to emulate Best-of-N but without its significant computational overhead at inference time. Specifically, BOND is a distribution matching algorithm that forces the distribution of generations from the policy to get closer to the Best-of-N distribution. We use the Jeffreys divergence (a linear combination of forward and backward KL) to balance between mode-covering and mode-seeking behavior, and derive an iterative formulation that utilizes a moving anchor for efficiency. We demonstrate the effectiveness of our approach and several design choices through experiments on abstractive summarization and Gemma models.

## item_id: m_3847

TITLE: Meta-Learning via Classifier(-free) Guidance

ABSTRACT: State-of-the-art meta-learning techniques do not optimize for zero-shot adaptation to unseen tasks, a setting in which humans excel. On the contrary, meta-learning algorithms learn hyperparameters and weight initializations that explicitly optimize for few-shot learning performance. In this work, we take inspiration from recent advances in generative modeling and language-conditioned image synthesis to propose meta-learning techniques that use natural language guidance to achieve higher zero-shot performance compared to the state-of-the-art. We do so by recasting the meta-learning problem as a multi-modal generative modeling problem: given a task, we consider its adapted neural network weights and its natural language description as equivalent multi-modal task representations. We first train an unconditional generative hypernetwork model to produce neural network weights; then we train a second "guidance" model that, given a natural language task description, traverses the hypernetwork latent space to find high-performance task-adapted weights in a zero-shot manner. We explore two alternative approaches for latent space guidance: "HyperCLIP"-based classifier guidance and a conditional Hypernetwork Latent Diffusion Model ("HyperLDM"), which we show to benefit from the classifier-free guidance technique common in image generation. Finally, we demonstrate that our approaches outperform existing meta-learning methods with zero-shot learning experiments on our Meta-VQA dataset, which we specifically constructed to reflect the multi-modal meta-learning setting.

## item_id: m_3848

TITLE: Reinforcement Learning through Asynchronous Advantage Actor-Critic on a GPU

ABSTRACT: We introduce a hybrid CPU/GPU version of the Asynchronous Advantage Actor-Critic (A3C) algorithm, currently the state-of-the-art method in reinforcement learning for various gaming tasks. We analyze its computational traits and concentrate on aspects critical to leveraging the GPU's computational power. We introduce a system of queues and a dynamic scheduling strategy, potentially helpful for other asynchronous algorithms as well. Our hybrid CPU/GPU version of A3C, based on TensorFlow, achieves a significant speed up compared to a CPU implementation; we make it publicly available to other researchers at https://github.com/NVlabs/GA3C.

## item_id: m_3849

TITLE: Nonparametric Neural Networks

ABSTRACT: Automatically determining the optimal size of a neural network for a given task without prior information currently requires an expensive global search and training many networks from scratch. In this paper, we address the problem of automatically finding a good network size during a single training cycle. We introduce {\it nonparametric neural networks}, a non-probabilistic framework for conducting optimization over all possible network sizes and prove its soundness when network growth is limited via an $\ell_p$ penalty. We train networks under this framework by continuously adding new units while eliminating redundant units via an $\ell_2$ penalty. We employ a novel optimization algorithm, which we term ``Adaptive Radial-Angular Gradient Descent'' or {\it AdaRad}, and obtain promising results.

## item_id: m_3850

TITLE: Pix2Scene: Learning Implicit 3D Representations from Images

ABSTRACT: Modelling 3D scenes from 2D images is a long-standing problem in computer vision with implications in, e.g., simulation and robotics. We propose pix2scene, a deep generative-based approach that implicitly models the geometric properties of a scene from images. Our method learns the depth and orientation of scene points visible in images. Our model can then predict the structure of a scene from various, previously unseen view points. It relies on a bi-directional adversarial learning mechanism to generate scene representations from a latent code, inferring the 3D representation of the underlying scene geometry. We showcase a novel differentiable renderer to train the 3D model in an end-to-end fashion, using only images. We demonstrate the generative ability of our model qualitatively on both a custom dataset and on ShapeNet. Finally, we evaluate the effectiveness of the learned 3D scene representation in supporting a 3D spatial reasoning.

## item_id: m_3851

TITLE: BWCP: Probabilistic Learning-to-Prune Channels for ConvNets via Batch Whitening

ABSTRACT: This work presents a probabilistic channel pruning method to accelerate Convolutional Neural Networks (CNNs). Previous pruning methods often zero out unimportant channels in training in a deterministic manner, which reduces CNN's learning capacity and results in suboptimal performance. To address this problem, we develop a probability-based pruning algorithm, called batch whitening channel pruning (BWCP), which can stochastically discard unimportant channels by modeling the probability of a channel being activated. BWCP has several merits. (1) It simultaneously trains and prunes CNNs from scratch in a probabilistic way, exploring larger network space than deterministic methods. (2) BWCP is empowered by the proposed batch whitening tool, which is able to empirically and theoretically increase the activation probability of useful channels while reducing the probability of unimportant channels without adding any extra parameters and computational cost in inference. (3) Extensive experiments on CIFAR-10, CIFAR-100, and ImageNet with various network architectures show that BWCP outperforms its counterparts by achieving better accuracy given limited computational budgets. For example, ResNet50 pruned by BWCP has only 0.58% Top-1 accuracy drop on ImageNet, while reducing 42.9% FLOPs of the plain ResNet50.

## item_id: m_3852

TITLE: The role of Disentanglement in Generalisation

ABSTRACT: Combinatorial generalisation — the ability to understand and produce novel combinations of familiar elements — is a core capacity of human intelligence that current AI systems struggle with. Recently, it has been suggested that learning disentangled representations may help address this problem. It is claimed that such representations should be able to capture the compositional structure of the world which can then be combined to support combinatorial generalisation. In this study, we systematically tested how the degree of disentanglement affects various forms of generalisation, including two forms of combinatorial generalisation that varied in difficulty. We trained three classes of variational autoencoders (VAEs) on two datasets on an unsupervised task by excluding combinations of generative factors during training. At test time we ask the models to reconstruct the missing combinations in order to measure generalisation performance. Irrespective of the degree of disentanglement, we found that the models supported only weak combinatorial generalisation. We obtained the same outcome when we directly input perfectly disentangled representations as the latents, and when we tested a model on a more complex task that explicitly required independent generative factors to be controlled. While learning disentangled representations does improve interpretability and sample efficiency in some downstream tasks, our results suggest that they are not sufficient for supporting more difficult forms of generalisation.

## item_id: m_3853

TITLE: RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning

ABSTRACT: Deep reinforcement learning (deep RL) has been successful in learning sophisticated behaviors automatically; however, the learning process requires a huge number of trials. In contrast, animals can learn new tasks in just a few trials, benefiting from their prior knowledge about the world. This paper seeks to bridge this gap. Rather than designing a “fast” reinforcement learning algorithm, we propose to represent it as a recurrent neural network (RNN) and learn it from data. In our proposed method, RL^2, the algorithm is encoded in the weights of the RNN, which are learned slowly through a general-purpose (“slow”) RL algorithm. The RNN receives all information a typical RL algorithm would receive, including observations, actions, rewards, and termination flags; and it retains its state across episodes in a given Markov Decision Process (MDP). The activations of the RNN store the state of the “fast” RL algorithm on the current (previously unseen) MDP. We evaluate RL^2 experimentally on both small-scale and large-scale problems. On the small-scale side, we train it to solve randomly generated multi-arm bandit problems and finite MDPs. After RL^2 is trained, its performance on new MDPs is close to human-designed algorithms with optimality guarantees. On the large-scale side, we test RL^2 on a vision-based navigation task and show that it scales up to high-dimensional problems.

## item_id: m_3854

TITLE: Learning Semantic Similarities for Prototypical Classifiers

ABSTRACT: Recent metric learning approaches parametrize semantic similarity measures through the use of an encoder trained along with a similarity model, which operates over pairs of representations. We extend such a setting and enable its use in tasks including multi-class classification in order to tackle known issues observed in standard classifiers such as their lack of robustness to out-of-distribution data. We do so by further learning a set of class prototypes, each one representing a particular class. Training is carried out so that each encoded example is pushed towards the prototype corresponding to its class, and test instances are assigned to the class corresponding to the prototype they are closest to. We thus provide empirical evidence showing the proposed setting is able to match object recognition performance of standard classifiers on common benchmarks, while presenting much improved robustness to adversarial examples and distribution shifts. We further show such a model is effective for tasks other than classification, including those requiring pairwise comparisons such as verification and retrieval. Finally, we discuss a simple scheme for few-shot learning of new classes where only the set of prototypes needs to be updated, yielding competitive performance.

## item_id: m_3855

TITLE: Meta Learning with Fast/Slow Learners

ABSTRACT: Meta-learning has recently achieved success in many optimization problems. In general, a meta learner g(.) could be learned for a base model f(.) on a variety of tasks, such that it can be more efficient on a new task. In this paper, we make some key modifications to enhance the performance of meta-learning models. (1) we leverage different meta-strategies for different modules to optimize them separately: we use conservative “slow learners” on low-level basic feature representation layers and “fast learners” on high-level task-specific layers; (2) Furthermore, we provide theoretical analysis on why the proposed approach works, based on a case study on a two-layer MLP. We evaluate our model on synthetic MLP regression, as well as low-shot learning tasks on Omniglot and ImageNet benchmarks. We demonstrate that our approach is able to achieve state-of-the-art performance.

## item_id: m_3856

TITLE: Shap-CAM: Visual Explanations for Convolutional Neural Networks based on Shapley Value

ABSTRACT: Explaining deep convolutional neural networks has been recently drawing increasing attention since it helps to understand the networks' internal operations and why they make certain decisions. Saliency maps, which emphasize salient regions largely connected to the network's decision-making, are one of the most common ways for visualizing and analyzing deep networks in the computer vision community. However, saliency maps generated by existing methods cannot represent authentic information in images due to the unproven proposals about the weights of activation maps which lack solid theoretical foundation and fail to consider the relations between each pixels. In this paper, we develop a novel post-hoc visual explanation method called Shap-CAM based on class activation mapping. Unlike previous class activation mapping based approaches, Shap-CAM gets rid of the dependence on gradients by obtaining the importance of each pixels through Shapley value. We demonstrate that Shap-CAM achieves better visual performance and fairness for interpreting the decision making process. Our approach outperforms previous methods on both recognition and localization tasks.

## item_id: m_3857

TITLE: One-Prompt-One-Story: Free-Lunch Consistent Text-to-Image Generation Using a Single Prompt

ABSTRACT: Text-to-image generation models can create high-quality images from input prompts. However, they struggle to support the consistent generation of identity-preserving requirements for storytelling. Existing approaches to this problem typically require extensive training in large datasets or additional modifications to the original model architectures. This limits their applicability across different domains and diverse diffusion model configurations. In this paper, we first observe the inherent capability of language models, coined $\textit{context consistency}$, to comprehend identity through context with a single prompt. Drawing inspiration from the inherent $\textit{context consistency}$, we propose a novel $\textit{training-free}$ method for consistent text-to-image (T2I) generation, termed "One-Prompt-One-Story" ($\textit{1Prompt1Story}$). Our approach $\textit{1Prompt1Story}$ concatenates all prompts into a single input for T2I diffusion models, initially preserving character identities. We then refine the generation process using two novel techniques: $\textit{Singular-Value
Reweighting}$ and $\textit{Identity-Preserving Cross-Attention}$, ensuring better alignment with the input description for each frame. In our experiments, we compare our method against various existing consistent T2I generation approaches to demonstrate its effectiveness, through quantitative metrics and qualitative assessments. Code is available at https://github.com/byliutao/1Prompt1Story.

## item_id: m_3858

TITLE: Model-Based Robust Adaptive Semantic Segmentation

ABSTRACT: Semantic image segmentation enjoys a wide range of applications such as autonomous vehicles and medical imaging while it is typically accomplished by deep neural networks (DNNs). Nevertheless, DNNs are known to be fragile to input perturbations that are adversarially crafted or occur due to natural variations, such as changes in weather or lighting conditions. This issue of lack of robustness prevents the application of learning-based semantic segmentation methods on safety-critical applications. To mitigate this challenge, in this paper, we propose model-based robust adaptive training algorithm (MRTAdapt), a new training algorithm to enhance the robustness of DNN-based semantic segmentation methods against natural variations that leverages model-based robust training algorithms and generative adversarial networks. Natural variation effects are minimized from both image and label sides. We provide extensive experimental results on both real-world and synthetic datasets demonstrating that model-based robust adaptive training algorithm outperforms multiple state-of-the-art models under various natural variations. 

## item_id: m_3859

TITLE: $\epsilon$-Invariant Hierarchical Reinforcement Learning for Building Generalizable Policy

ABSTRACT: Goal-conditioned Hierarchical Reinforcement Learning (HRL) has shown remarkable potential for solving complex control tasks. However, existing methods struggle in tasks that require generalization since the learned subgoals are highly task-specific and therefore hardly reusable. In this paper, we propose a novel HRL framework called \textit{$\epsilon$-Invariant HRL} that uses abstract, task-agnostic subgoals reusable across tasks, resulting in a more generalizable policy. Although such subgoals are reusable, a transition mismatch problem caused by the inevitable incorrect value evaluation of subgoals can lead to non-stationary learning and even collapse. We mitigate this mismatch problem by training the high-level policy to be adaptable to the stochasticity manually injected into the low-level policy. As a result, our framework can leverage reusable subgoals to constitute a hierarchical policy that can effectively generalize to unseen new tasks. Theoretical analysis and experimental results in continuous control navigation tasks and challenging zero-shot generalization tasks show that our approach significantly outperforms state-of-the-art methods.

## item_id: m_3860

TITLE: DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION

ABSTRACT: Recent progress in pre-trained neural language models has significantly improved the performance of many natural language processing (NLP) tasks. In this paper we propose a new model architecture DeBERTa (Decoding-enhanced BERT with disentangled attention) that improves the BERT and RoBERTa models using two novel techniques. The first is the disentangled attention mechanism, where each word is represented using two vectors that encode its content and position, respectively, and the attention weights among words are computed using disentangled matrices on their contents and relative positions, respectively. Second, an enhanced mask decoder is used to incorporate absolute positions in the decoding layer to predict the masked tokens in model pre-training. In addition, a new virtual adversarial training method is used for fine-tuning to improve models’ 
 generalization. We show that these techniques significantly improve the efficiency of model pre-training and the performance of both natural language understand(NLU) and natural langauge generation (NLG) downstream tasks. Compared to RoBERTa-Large, a DeBERTa model trained on half of the training data performs consistently better on a wide range of NLP tasks, achieving improvements on MNLI by +0.9% (90.2% vs. 91.1%), on SQuAD v2.0 by +2.3% (88.4% vs. 90.7%) and RACE by +3.6% (83.2% vs. 86.8%). Notably, we scale up DeBERTa by training a larger version that consists of 48 Transform layers with 1.5 billion parameters. The significant performance boost makes the single DeBERTa model surpass the human performance on the SuperGLUE benchmark (Wang et al., 2019a) for the first time in terms of macro-average score (89.9 versus 89.8), and the ensemble DeBERTa model sits atop the SuperGLUE leaderboard as of January 6, 2021, outperforming the human baseline by a decent margin (90.3 versus
89.8). The pre-trained DeBERTa models and the source code were released at: https://github.com/microsoft/DeBERTa.


## item_id: m_3861

TITLE: Understanding the Effect of Bias in Deep Anomaly Detection

ABSTRACT: Anomaly detection presents a unique challenge in machine learning, due to the scarcity of labeled anomaly data. Recent work attempts to mitigate such problems by augmenting training of deep anomaly detection models with additional labeled anomaly samples. However, the labeled data often does not align with the target distribution and introduces harmful bias to the trained model. In this paper, we aim to understand the effect of a biased anomaly set on anomaly detection. We formally state the anomaly detection problem as a supervised learning task, and focus on the anomaly detector’s recall at a given false positive rate as the main performance metric. Given two different anomaly score functions, we formally define their difference in performance as the relative scoring bias of the anomaly detectors. Along this line, our work provides two key contributions. We establish the first finite sample rates for estimating the relative scoring bias for deep anomaly detection, and empirically validate our theoretical results on both synthetic and real-world datasets. We also provide extensive empirical study on how a biased training anomaly set affects the anomaly score function and therefore the detection performance on different anomaly classes. Our study demonstrates scenarios in which the biased anomaly set can be useful or problematic, and provides a solid benchmark for future research. 

## item_id: m_3862

TITLE: RotationOut as a Regularization Method for Neural Network

ABSTRACT: In this paper, we propose a novel regularization method, RotationOut, for neural networks. 
Different from Dropout that handles each neuron/channel independently, RotationOut regards its input layer as an entire vector and introduces regularization by randomly rotating the vector. 
RotationOut can also be used in convolutional layers and recurrent layers with a small modification.
We further use a noise analysis method to interpret the difference between RotationOut and Dropout in co-adaptation reduction. 
Using this method, we also show how to use RotationOut/Dropout together with Batch Normalization. 
Extensive experiments in vision and language tasks are conducted to show the effectiveness of the proposed method. 
Codes will be available.

## item_id: m_3863

TITLE: Improving GAN Training via Binarized Representation Entropy (BRE) Regularization

ABSTRACT: We propose a novel regularizer to improve the training of Generative Adversarial Networks (GANs). The motivation is that when the discriminator D spreads out its model capacity in the right way, the learning signals given to the generator G are more informative and diverse, which helps G to explore better and discover the real data manifold while avoiding large unstable jumps due to the erroneous extrapolation made by D . Our regularizer guides the rectifier discriminator D to better allocate its model capacity, by encouraging the binary activation patterns on selected internal layers of D to have a high joint entropy. Experimental results on both synthetic data and real datasets demonstrate improvements in stability and convergence speed of the GAN training, as well as higher sample quality. The approach also leads to higher classification accuracies in semi-supervised learning.


## item_id: m_3864

TITLE: GAFormer: Enhancing Timeseries Transformers Through Group-Aware Embeddings

ABSTRACT: Analyzing multivariate time series is important in many domains. However, it has been difficult to learn robust and generalizable representations within multivariate datasets due to complex inter-channel relationships and dynamic shifts. In this paper, we introduce a novel approach for learning spatiotemporal structure and using it to improve the application of transformers to timeseries datasets. Our framework learns a set of group tokens, and builds an instance-specific group embedding (GE) layer that assigns input tokens to a small number of group tokens to incorporate  structure into learning. We then introduce a novel architecture, Group-Aware transFormer (GAFormer), which incorporates both spatial and temporal group embeddings to achieve state-of-the-art performance on a number of time-series classification and regression tasks. In evaluations on a number of diverse timeseries datasets, we show that GE on its own can provide a nice enhancement to a number of backbones, and that by coupling spatial and temporal group embeddings, the GAFormer can outperform the existing baselines. Finally, we show how our approach discerns latent structures in data even without information about the spatial ordering of channels, and yields a more interpretable decomposition of spatial and temporal structure underlying complex multivariate datasets.

## item_id: m_3865

TITLE: Learning a Spatio-Temporal Embedding for Video Instance Segmentation

ABSTRACT: Understanding object motion is one of the core problems in computer vision. It requires segmenting and tracking objects over time. Significant progress has been made in instance segmentation, but such models cannot track objects, and more crucially, they are unable to reason in both 3D space and time.
We propose a new spatio-temporal embedding loss on videos that generates temporally consistent video instance segmentation. Our model includes a temporal network that learns to model temporal context and motion, which is essential to produce smooth embeddings over time. Further, our model also estimates monocular depth, with a self-supervised loss, as the relative distance to an object effectively constrains where it can be next, ensuring a time-consistent embedding. Finally, we show that our model can accurately track and segment instances, even with occlusions and missed detections, advancing the state-of-the-art on the KITTI Multi-Object and Tracking Dataset.

## item_id: m_3866

TITLE: TFGAN: Improving Conditioning for Text-to-Video Synthesis

ABSTRACT: Developing conditional generative models for text-to-video synthesis is an extremely challenging yet an important topic of research in machine learning. In this work, we address this problem by introducing Text-Filter conditioning Generative Adversarial Network (TFGAN), a GAN model with novel conditioning scheme that aids improving the text-video associations. With a combination of this conditioning scheme and a deep GAN architecture, TFGAN generates photo-realistic videos from text on very challenging real-world video datasets. In addition, we construct a benchmark synthetic dataset of moving shapes to systematically evaluate our conditioning scheme. Extensive experiments demonstrate that TFGAN significantly outperforms the existing approaches, and can also generate videos of novel categories not seen during training.


## item_id: m_3867

TITLE: FACE SUPER-RESOLUTION GUIDED BY 3D FACIAL PRIORS

ABSTRACT: State-of-the-art face super-resolution methods employ deep convolutional neural networks to learn a mapping between low- and high-resolution facial patterns by exploring local appearance knowledge. However, most of these methods do not well exploit facial structures and identity information, and struggle to deal with facial images that exhibit large pose variation and misalignment. In this paper, we propose a novel face super-resolution method that explicitly incorporates 3D facial priors which grasp the sharp facial structures. Firstly, the 3D face rendering branch is set up to obtain 3D priors of salient facial structures and identity knowledge. Secondly, the Spatial Attention Mechanism is used to better exploit this hierarchical information (i.e. intensity similarity, 3D facial structure, identity content) for the super-resolution problem. Extensive experiments demonstrate that the proposed algorithm achieves superior face super-resolution results and outperforms the state-of-the-art.

## item_id: m_3868

TITLE: EMFlow: Data Imputation in Latent Space via EM and Deep Flow Models

ABSTRACT: The presence of missing values within high-dimensional data is an ubiquitous problem for many applied sciences. A serious limitation of many available data mining and machine learning methods is their inability to handle partially missing values and so an integrated approach that combines imputation and model estimation is vital for down-stream analysis. A computationally fast algorithm, called EMFlow, is introduced that performs imputation in a latent space via an online version of Expectation-Maximization (EM) algorithm by using a normalizing flow (NF) model which maps the data space to a latent space. The proposed EMFlow algorithm is iterative, involving updating the parameters of online EM and NF alternatively. Extensive experimental results for high-dimensional multivariate and image datasets are presented to illustrate the superior performance of the EMFlow compared to a couple of recently available methods in terms of both predictive accuracy and speed of algorithmic convergence.

## item_id: m_3869

TITLE: Improving Invariance and Equivariance Properties of Convolutional Neural Networks

ABSTRACT: Convolutional Neural Networks (CNNs) learn highly discriminative representations from data, but how robust and structured are these representations? How does the data shape the internal network representation? We shed light on these questions by empirically measuring the invariance and equivariance properties of a large number of CNNs trained with various types of input transformations. We find that CNNs learn invariance wrt all 9 tested transformation types and that invariance extends to transformations outside the training range. We also measure the distance between CNN representations and show that similar input transformations lead to more similar internal representations. Transforms can be grouped by the way they affect the learned representation. Additionally, we also propose a loss function that aims to improve CNN equivariance.

## item_id: m_3870

TITLE: Asymmetric Factorized Bilinear Operation for Vision Transformer

ABSTRACT: As a core component of Transformer-like deep architectures, a feed-forward network (FFN) for channel mixing is responsible for learning features of each token. Recent works show channel mixing can be enhanced by increasing computational burden or can be slimmed at the sacrifice of performance. Although some efforts have been made, existing works are still struggling to solve the paradox of performance and complexity trade-offs. In this paper, we propose an Asymmetric Factorized Bilinear Operation (AFBO) to replace FFN of vision transformer (ViT), which attempts to efficiently explore rich statistics of token features for achieving better performance and complexity trade-off. Specifically, our AFBO computes second-order statistics via a spatial-channel factorized bilinear operation for feature learning, which replaces a simple linear projection in FFN and enhances the feature learning ability of ViT by modeling second-order correlation among token features. Furthermore, our AFBO presents two structured-sparsity channel mapping strategies, namely Grouped Cross Channel Mapping (GCCM) and Overlapped Cycle Channel Mapping (OCCM). They decompose bilinear operation into grouped channel features by considering information interaction between groups, significantly reducing computational complexity while guaranteeing model performance. Finally, our AFBO is built with GCCM and OCCM in an asymmetric way, aiming to achieve a better trade-off. Note that our AFBO is model-agnostic, which can be flexibly integrated with existing ViTs. Experiments are conducted with twenty ViTs on various tasks, and the results show our AFBO is superior to its counterparts while improving existing ViTs in terms of generalization and robustness.

## item_id: m_3871

TITLE: DHER: Hindsight Experience Replay for Dynamic Goals

ABSTRACT: Dealing with sparse rewards is one of the most important challenges in reinforcement learning (RL), especially when a goal is dynamic (e.g., to grasp a moving object). Hindsight experience replay (HER) has been shown an effective solution to handling  sparse rewards with fixed goals. However, it does not account for dynamic goals in its vanilla form and, as a result, even degrades the performance of existing off-policy RL algorithms when the goal is changing over time. 

In this paper, we present  Dynamic Hindsight Experience Replay (DHER), a novel approach for tasks with dynamic goals in the presence of sparse rewards. DHER automatically assembles successful experiences from two relevant failures and can be used to enhance an arbitrary off-policy RL algorithm when the tasks' goals are dynamic. We evaluate DHER on tasks of robotic manipulation and moving object tracking, and transfer the polices from simulation to physical robots. Extensive comparison and ablation studies demonstrate  the superiority of our approach, showing that DHER is a crucial ingredient to enable RL to solve tasks with dynamic goals in manipulation and grid world domains.

## item_id: m_3872

TITLE: Adversarially Robust Neural Networks via Optimal Control: Bridging Robustness with Lyapunov Stability

ABSTRACT: Deep neural networks are known to be vulnerable to adversarial perturbations. In this paper, we bridge adversarial robustness of neural nets with Lyapunov stability of dynamical systems. From this viewpoint, training neural nets is equivalent to finding an optimal control of the discrete dynamical system, which allows one to utilize methods of successive approximations, an optimal control algorithm based on Pontryagin's maximum principle, to train neural nets. This decoupled training method allows us to add constraints to the optimization, which makes the deep model more robust. The constrained optimization problem can be formulated as a semi-definite programming problem and hence can be solved efficiently. Experiments show that our method effectively improves deep model's adversarial robustness.

## item_id: m_3873

TITLE: Towards an automatic Turing test: Learning to evaluate dialogue responses

ABSTRACT: Automatically evaluating the quality of dialogue responses for unstructured domains is a challenging problem.
Unfortunately, existing automatic evaluation metrics are biased and correlate very poorly with human judgements of response quality (Liu et al., 2016). Yet having an accurate automatic evaluation procedure is crucial for dialogue research, as it allows rapid prototyping and testing of new models with fewer expensive human evaluations. In response to this challenge, we formulate automatic dialogue evaluation as a learning problem. We present an evaluation model (ADEM) that learns to predict human-like scores to input responses, using a new dataset of human response scores. We show that the ADEM model's predictions correlate significantly, and at level much higher than word-overlap metrics such as BLEU, with human judgements at both the utterance and system-level. We also show that ADEM can generalize to evaluating dialogue models unseen during training, an important step for automatic dialogue evaluation.

## item_id: m_3874

TITLE: Generating Differentially Private Datasets Using GANs

ABSTRACT: In this paper, we present a technique for generating artificial datasets that retain statistical properties of the real data while providing differential privacy guarantees with respect to this data. We include a Gaussian noise layer in the discriminator of a generative adversarial network to make the output and the gradients differentially private with respect to the training data, and then use the generator component to synthesise privacy-preserving artificial dataset. Our experiments show that under a reasonably small privacy budget we are able to generate data of high quality and successfully train machine learning models on this artificial data.

## item_id: m_3875

TITLE: Better Generalization with On-the-fly Dataset Denoising

ABSTRACT: Memorization in over-parameterized neural networks can severely hurt generalization in the presence of mislabeled examples. However, mislabeled examples are to hard avoid in extremely large datasets. We address this problem using the implicit regularization effect of stochastic gradient descent with large learning rates, which we find to be able to separate clean and mislabeled examples with remarkable success using loss statistics. We leverage this to identify and on-the-fly discard mislabeled examples using a threshold on their losses. This leads to On-the-fly Data Denoising (ODD), a simple yet effective algorithm that is robust to mislabeled examples, while introducing almost zero computational overhead. Empirical results demonstrate the effectiveness of ODD on several datasets containing artificial and real-world mislabeled examples.

## item_id: m_3876

TITLE: Sublinear Least-Squares Value Iteration via Locality Sensitive Hashing

ABSTRACT: We present the first provable Least-Squares Value Iteration (LSVI) algorithm that achieves runtime complexity sublinear in the number of actions.  We formulate the value function estimation procedure in value iteration as an approximate maximum inner product search problem and propose a locality sensitive hashing (LSH) type data structure to solve this problem with sublinear time complexity. Moreover, we build the connections between the theory of approximate maximum inner product search and the regret analysis of reinforcement learning. We prove that, with our choice of approximation factor, our Sublinear LSVI algorithms maintain the same regret as the original LSVI algorithms while reducing the runtime complexity to sublinear in the number of actions. To the best of our knowledge, this is the first work that combines LSH with reinforcement learning that resulting in provable improvements.  We hope that our novel way of combining data structures and iterative algorithm will open the door for further study into the cost reduction in optimization.

## item_id: m_3877

TITLE: The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

ABSTRACT: Neural network pruning techniques can reduce the parameter counts of trained networks by over 90%, decreasing storage requirements and improving computational performance of inference without compromising accuracy. However, contemporary experience is that the sparse architectures produced by pruning are difficult to train from the start, which would similarly improve training performance.

We find that a standard pruning technique naturally uncovers subnetworks whose initializations made them capable of training effectively. Based on these results, we articulate the "lottery ticket hypothesis:" dense, randomly-initialized, feed-forward networks contain subnetworks ("winning tickets") that - when trained in isolation - reach test accuracy comparable to the original network in a similar number of iterations. The winning tickets we find have won the initialization lottery: their connections have initial weights that make training particularly effective.

We present an algorithm to identify winning tickets and a series of experiments that support the lottery ticket hypothesis and the importance of these fortuitous initializations. We consistently find winning tickets that are less than 10-20% of the size of several fully-connected and convolutional feed-forward architectures for MNIST and CIFAR10. Above this size, the winning tickets that we find learn faster than the original network and reach higher test accuracy.

## item_id: m_3878

TITLE: Network Reparameterization for Unseen Class Categorization

ABSTRACT: Many problems with large-scale labeled training data have been impressively solved by deep learning. However, Unseen Class Categorization (UCC) with minimal information provided about target classes is the most commonly encountered setting in industry, which remains a challenging research problem in machine learning. Previous approaches to UCC either fail to generate a powerful discriminative feature extractor or fail to learn a flexible classifier that can be easily adapted to unseen classes. In this paper, we propose to address these issues through network reparameterization, \textit{i.e.}, reparametrizing the learnable weights of a network as a function of other variables, by which we decouple the feature extraction part and the classification part of a deep classification model to suit the special setting of UCC, securing both strong discriminability and excellent adaptability. Extensive experiments for UCC on several widely-used benchmark datasets in the settings of zero-shot and few-shot learning demonstrate that, our method with network reparameterization achieves state-of-the-art performance.

## item_id: m_3879

TITLE: Training wide residual networks for deployment using a single bit for each weight

ABSTRACT: For fast and energy-efficient deployment of trained deep neural networks on resource-constrained embedded hardware,  each learned weight parameter should ideally be represented and stored using a single bit.  Error-rates usually increase when this requirement is imposed. Here, we report large improvements in error rates on multiple datasets, for deep convolutional neural networks deployed with 1-bit-per-weight. Using wide residual networks as our main baseline, our approach simplifies existing methods that binarize weights by applying the sign function in training; we apply  scaling factors for each layer with constant unlearned values equal to the layer-specific standard deviations used for initialization. For CIFAR-10, CIFAR-100 and ImageNet, and models with 1-bit-per-weight requiring less than 10 MB of parameter memory, we achieve error rates of 3.9%, 18.5% and 26.0% / 8.5% (Top-1 / Top-5) respectively. We also considered MNIST, SVHN and ImageNet32, achieving 1-bit-per-weight test results of 0.27%, 1.9%, and 41.3% / 19.1%  respectively. For CIFAR, our error rates halve previously reported values, and are within about 1% of our error-rates for the same network with full-precision weights. For networks that overfit, we also show significant improvements in error rate by not learning batch normalization scale and offset parameters. This applies to both full precision and 1-bit-per-weight networks. Using a warm-restart learning-rate schedule, we found that training for 1-bit-per-weight is just as fast as full-precision networks, with better accuracy than standard schedules, and achieved about 98%-99% of peak performance in just 62 training epochs for CIFAR-10/100. For full training code and trained models in MATLAB, Keras and PyTorch see https://github.com/McDonnell-Lab/1-bit-per-weight/ .

## item_id: m_3880

TITLE: Scale-Invariant Teaching for Semi-Supervised Object Detection

ABSTRACT: Recent Semi-Supervised Object Detection methods are mainly based on self-training, i.e., generating hard pseudo-labels by a teacher model on unlabeled data as supervisory signals. Although they achieved certain success, the massive False Negative samples and inferior localization precision lack consideration. Furthermore, the limited annotations in semi-supervised learning scale up the challenges: large variance of object sizes and class imbalance (i.e., the extreme ratio between background and object), hindering the performance of prior arts. We address these challenges by introducing a novel approach, Scale-Invariant Teaching (SIT), which is a simple yet effective end-to-end knowledge distillation framework robust to large object size variance and class imbalance. SIT has several appealing benefits compared to previous works.
(1) SIT imposes a consistency regularization to reduce the prediction discrepancy between objects with different sizes. 
(2) The soft pseudo-label alleviates the noise problem from the False Negative samples and inferior localization precision.
(3) A re-weighting strategy can implicitly screen the potential foreground regions from unlabeled data to reduce the effect of class imbalance. 
Extensive experiments show that SIT consistently outperforms the recent state-of-the-art methods and baseline on different datasets with significant margins. For example, it surpasses the supervised counterpart by more than 10 mAP when using 5% and 10% labeled data on MS-COCO.

## item_id: m_3881

TITLE: Adversarial Training and Provable Defenses: Bridging the Gap

ABSTRACT: We present COLT, a new method to train neural networks based on a novel combination of adversarial training and provable defenses. The key idea is to model neural network training as a procedure which includes both, the verifier and the adversary. In every iteration, the verifier aims to certify the network using convex relaxation while the adversary tries to find inputs inside that convex relaxation which cause verification to fail. We experimentally show that this training method, named convex layerwise adversarial training (COLT), is promising and achieves the best of both worlds -- it produces a state-of-the-art neural network with certified robustness of 60.5% and accuracy of 78.4% on the challenging CIFAR-10 dataset with a 2/255 L-infinity perturbation. This significantly improves over the best concurrent results of 54.0% certified robustness and 71.5% accuracy.
   


## item_id: m_3882

TITLE: Integer Networks for Data Compression with Latent-Variable Models

ABSTRACT: We consider the problem of using variational latent-variable models for data compression. For such models to produce a compressed binary sequence, which is the universal data representation in a digital world, the latent representation needs to be subjected to entropy coding. Range coding as an entropy coding technique is optimal, but it can fail catastrophically if the computation of the prior differs even slightly between the sending and the receiving side. Unfortunately, this is a common scenario when floating point math is used and the sender and receiver operate on different hardware or software platforms, as numerical round-off is often platform dependent. We propose using integer networks as a universal solution to this problem, and demonstrate that they enable reliable cross-platform encoding and decoding of images using variational models.

## item_id: m_3883

TITLE: Continuous Wasserstein-2 Barycenter Estimation without Minimax Optimization

ABSTRACT: Wasserstein barycenters provide a geometric notion of the weighted average of probability measures based on optimal transport. In this paper, we present a scalable algorithm to compute Wasserstein-2 barycenters given sample access to the input measures, which are not restricted to being discrete. While past approaches rely on entropic or quadratic regularization, we employ input convex neural networks and cycle-consistency regularization to avoid introducing bias. As a result, our approach does not resort to minimax optimization. We provide theoretical analysis on error bounds as well as empirical evidence of the effectiveness of the proposed approach in low-dimensional qualitative scenarios and high-dimensional quantitative experiments.

## item_id: m_3884

TITLE: PointGrow: Autoregressively Learned Point Cloud Generation with Self-Attention

ABSTRACT: A point cloud is an agile 3D representation, efficiently modeling an object's surface geometry. However, these surface-centric properties also pose challenges on designing tools to recognize and synthesize point clouds. This work presents a novel autoregressive model, PointGrow, which generates realistic point cloud samples from scratch or conditioned from given semantic contexts. Our model operates recurrently, with each point sampled according to a conditional distribution given its previously-generated points. Since point cloud object shapes are typically encoded by long-range interpoint dependencies, we augment our model with dedicated self-attention modules to capture these relations. Extensive evaluation demonstrates that PointGrow achieves satisfying performance on both unconditional and conditional point cloud generation tasks, with respect to fidelity, diversity and semantic preservation. Further, conditional PointGrow learns a smooth manifold of given images where 3D shape interpolation and arithmetic calculation can be performed inside.

## item_id: m_3885

TITLE: Newton Residual Learning

ABSTRACT: A plethora of computer vision tasks, such as optical flow and image alignment, can be formulated as non-linear optimization problems. Before the resurgence of deep learning, the dominant family for solving such optimization problems was numerical optimization, e.g, Gauss-Newton (GN). More recently, several attempts were made to formulate learnable GN steps as cascade regression architectures. In this paper, we investigate recent machine learning architectures, such as deep neural networks with residual connections, under the above perspective. To this end, we first demonstrate how residual blocks (when considered as discretization of ODEs) can be viewed as GN steps. Then, we go a step further and propose a new residual block, that is reminiscent of Newton's method in numerical optimization and exhibits faster convergence. We thoroughly evaluate the proposed Newton-ResNet by conducting experiments on image and speech classification and image generation, using 4 datasets. All the experiments demonstrate that Newton-ResNet requires less parameters to achieve the same performance with the original ResNet.

## item_id: m_3886

TITLE: A Step-Wise Weighting Approach for Controllable Text Generation

ABSTRACT: We study the problem of controllable text generation (CTG): steering a language model (LM) to generate text with a desired attribute. Many existing approaches either require extensive training/fine-tuning of the LM for each single attribute under control or are slow to generate text. To this end, we first propose a framework based on step-wise energy-based models (EBMs) that is efficient in sampling and flexible in a wide range of practical CTG scenarios. Indeed, a number of existing CTG methods are special instances of our framework with a specific EBM design. In different control scenarios, we then design the respective energy functions that strategically up- or down-weigh the probabilities of keywords associated with a certain control attribute at each generation step. In experiments, we show that our simple and efficient approach is surprisingly competitive against more computationally expensive strong baselines, and even achieving new state-of-the-art performances in several cases. Our framework also provides a tuning hyper-parameter that nicely trades off generation quality and control satisfaction, enabling practitioners to easily adjust it to meet their needs.

## item_id: m_3887

TITLE: CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction

ABSTRACT: Human electroencephalography (EEG) is a brain monitoring modality that senses cortical neuroelectrophysiological activity in high-temporal resolution. One of the greatest challenges posed in applications of EEG is the unstable signal quality susceptible to inevitable artifacts during recordings. To date, most existing techniques for EEG artifact removal and reconstruction are applicable to offline analysis solely, or require individualized training data to facilitate online reconstruction. We have proposed CLEEGN, a novel convolutional neural network for plug-and-play automatic EEG reconstruction. CLEEGN is based on a subject-independent pre-trained model using existing data and can operate on a new user without any further calibration. The performance of CLEEGN was validated using multiple evaluations including waveform observation, reconstruction error assessment, and decoding accuracy on well-studied labeled datasets. The results of simulated online validation suggest that, even without any calibration, CLEEGN can largely preserve inherent brain activity and outperforms leading online/offline artifact removal methods in the decoding accuracy of reconstructed EEG data. In addition, visualization of model parameters and latent features exhibit the model behavior and reveal explainable insights related to existing knowledge of neuroscience. We foresee pervasive applications of CLEEGN in prospective works of online plug-and-play EEG decoding and analysis.

## item_id: m_3888

TITLE: Optimal Binary Autoencoding with Pairwise Correlations

ABSTRACT: We formulate learning of a binary autoencoder as a biconvex optimization problem which learns from the pairwise correlations between encoded and decoded bits. Among all possible algorithms that use this information, ours finds the autoencoder that reconstructs its inputs with worst-case optimal loss. The optimal decoder is a single layer of artificial neurons, emerging entirely from the minimax loss minimization, and with weights learned by convex optimization. All this is reflected in competitive experimental results, demonstrating that binary autoencoding can be done efficiently by conveying information in pairwise correlations in an optimal fashion. 

## item_id: m_3889

TITLE: Parallel Stochastic Gradient Descent with Sound Combiners

ABSTRACT: Stochastic gradient descent (SGD) is a well-known method for regression and classification tasks. However, it is an inherently sequential algorithm — at each step, the processing of the current example depends on the parameters learned from the previous examples. Prior approaches to parallelizing SGD, such as Hogwild! and AllReduce, do not honor these dependences across threads and thus can potentially suffer poor convergence rates and/or poor scalability. This paper proposes SymSGD, a parallel SGD algorithm that retains the sequential semantics of SGD in expectation. Each thread in this approach learns a local model and a probabilistic model combiner that allows the local models to be combined to produce the same result as what a sequential SGD would have produced, in expectation. This SymSGD approach is applicable to any linear learner whose update rule is linear. This paper evaluates SymSGD’s accuracy and performance on 9 datasets on a shared-memory machine shows up-to 13× speedup over our heavily optimized sequential baseline on 16 cores.

## item_id: m_3890

TITLE: XD: Cross-lingual Knowledge Distillation for Polyglot Sentence Embeddings

ABSTRACT: Current state-of-the-art results in multilingual natural language inference (NLI) are based on tuning XLM (a pre-trained polyglot language model) separately for each language involved, resulting in multiple models. We reach significantly higher NLI results with a single model for all languages via multilingual tuning. Furthermore, we introduce cross-lingual knowledge distillation (XD), where the same polyglot model is used both as teacher and student across languages to improve its sentence representations without using the end-task labels. When used alone, XD beats multilingual tuning for some languages and the combination of them both results in a new state-of-the-art of 79.2% on the XNLI dataset, surpassing the previous result by absolute 2.5%. The models and code for reproducing our experiments will be made publicly available after de-anonymization.

## item_id: m_3891

TITLE: Conformal Risk Control

ABSTRACT: We extend conformal prediction to control the expected value of any monotone loss function. The algorithm generalizes split conformal prediction together with its coverage guarantee. Like conformal prediction, the conformal risk control procedure is tight up to an $\mathcal{O}(1/n)$ factor. We also introduce extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. Worked examples from computer vision and natural language processing demonstrate the usage of our algorithm to bound the false negative rate, graph distance, and token-level F1-score.

## item_id: m_3892

TITLE: Action-Sufficient State Representation Learning for Control with Structural Constraints

ABSTRACT: Perceived signals in real-world scenarios are usually high-dimensional and noisy, and finding and using their representation that contains essential and sufficient information required by downstream decision-making tasks will help improve computational efficiency and generalization ability in the tasks. In this paper, we focus on partially observable environments and propose to learn a minimal set of state representations that capture sufficient information for decision-making, termed \textit{Action-Sufficient state Representations} (ASRs). We build a generative environment model for the structural relationships among variables in the system and present a principled way to characterize ASRs based on structural constraints and the goal of maximizing cumulative reward in policy learning. We then develop a structured sequential Variational Auto-Encoder to estimate the environment model and extract ASRs. Our empirical results on CarRacing and VizDoom demonstrate a clear advantage of learning and using ASRs for policy learning. Moreover, the estimated environment model and ASRs allow learning behaviors from imagined outcomes in the compact latent space to improve sample efficiency.

## item_id: m_3893

TITLE: Dynamically Scaled Activation Steering

ABSTRACT: Activation steering has emerged as a powerful method for guiding the behavior of generative models towards desired outcomes such as toxicity mitigation. However, most existing methods apply interventions uniformly across all inputs, degrading model performance when steering is unnecessary. We introduce Dynamically Scaled Activation Steering (DSAS), a method-agnostic steering framework that decouples when to steer from how to steer. DSAS adaptively modulates the strength of existing steering transformations across layers and inputs, intervening strongly only when undesired behavior is detected. At generation time, DSAS computes context-dependent scaling factors that selectively adjust the strength of any steering method. We also show how DSAS can be jointly optimized end-to-end together with the steering function. When combined with existing steering methods, DSAS consistently improves the Pareto front with respect to steering alone, achieving a better trade-off between toxicity mitigation and utility preservation. We further demonstrate DSAS’s generality by applying it to a text-to-image diffusion model, showing how adaptive steering allows the modulation of specific concepts. Finally, DSAS introduces minimal computational overhead while improving interpretability, pinpointing which tokens require steering and by how much.

## item_id: m_3894

TITLE: SimpleTM: A Simple Baseline for Multivariate Time Series Forecasting

ABSTRACT: The versatility of large Transformer-based models has led to many efforts focused on adaptations to other modalities, including time-series data. For instance, one could start from a pre-trained checkpoint of a large language model and attach adapters to recast 
the new modality (e.g., time-series) as ``language''. Alternatively, one can use a suitably large Transformer-based model, and make some modifications for time-series data. These ideas offer good performance across available benchmarks. But temporal data are quite heterogeneous (e.g., wearable sensors, physiological measurements in healthcare), and unlike text/image corpus, much of it is not publicly available. So, these models need a fair bit of domain-specific fine-tuning to achieve good performance -- this is often expensive or difficult with limited resources. In this paper, we study and characterize the performance profile of a non-generalist approach: our SimpleTM model is specialized for multivariate time-series forecasting. By simple, we mean that the model is lightweight. It is restricted to tokenization based on textbook signal processing ideas (shown to be effective in vision) which are then allowed to attend/interact: via self-attention but also via ways that are a bit more general than dot-product attention, accomplished via basic geometric algebra operations. We show that even a single- or two-layer model gives results that are competitive with much bigger models, including large transformer-based architectures,
on most benchmarks commonly reported in the literature.

## item_id: m_3895

TITLE: AntisymmetricRNN: A Dynamical System View on Recurrent Neural Networks

ABSTRACT: Recurrent neural networks have gained widespread use in modeling sequential data. Learning long-term dependencies using these models remains difficult though, due to exploding or vanishing gradients. In this paper, we draw connections between recurrent networks and ordinary differential equations. A special form of recurrent networks called the AntisymmetricRNN is proposed under this theoretical framework, which is able to capture long-term dependencies thanks to the stability property of its underlying differential equation. Existing approaches to improving RNN trainability often incur significant computation overhead.  In comparison, AntisymmetricRNN achieves the same goal by design.  We showcase the advantage of this new architecture through extensive simulations and experiments. AntisymmetricRNN exhibits much more predictable dynamics. It outperforms regular LSTM models on tasks requiring long-term memory and matches the performance on tasks where short-term dependencies dominate despite being much simpler.

## item_id: m_3896

TITLE: Zero-Shot Recommender Systems

ABSTRACT: Performance of recommender systems (RecSys) relies heavily on the amount of training data available. This poses a chicken-and-egg problem for early-stage products, whose amount of data, in turn, relies on the performance of their RecSys. In this paper, we explore the possibility of zero-shot learning in RecSys, to enable generalization from an old dataset to an entirely new dataset. We develop an algorithm, dubbed ZEro-Shot Recommenders (ZESRec), that is trained on an old dataset and generalize to a new one where there are neither overlapping users nor overlapping items, a setting that contrasts typical cross-domain RecSys that has either overlapping users or items. Different from previous methods that use categorical item indices (i.e., item ID), ZESRec uses items' generic features, such as natural-language descriptions, product images, and videos, as their continuous indices, and therefore naturally generalizes to any unseen items. In terms of users, ZESRec builds upon recent advances on sequential RecSys to represent users using their interactions with items, thereby generalizing to unseen users as well. We study three pairs of real-world RecSys datasets and demonstrate that ZESRec can successfully enable recommendations in such a zero-shot setting, opening up new opportunities for resolving the chicken-and-egg problem for data-scarce startups or early-stage products.

## item_id: m_3897

TITLE: Robust Simulation-Based Inference under Missing Data via Neural Processes

ABSTRACT: Simulation-based inference (SBI) methods typically require fully observed data to infer parameters of models with intractable likelihood functions. However, datasets often contain missing values due to incomplete observations, data corruptions (common in astrophysics), or instrument limitations (e.g., in high-energy physics applications). In such scenarios, missing data must be imputed before applying any SBI method. We formalize the problem of missing data in SBI and demonstrate that naive imputation methods can introduce bias in the estimation of SBI posterior. We also introduce a novel amortized method that addresses this issue by jointly learning the imputation model and the inference network within a neural posterior estimation (NPE) framework. Extensive empirical results on SBI benchmarks show that our approach provides robust inference outcomes compared to standard baselines for varying levels of missing data. Moreover, we demonstrate the merits of our imputation model on two real-world bioactivity datasets (Adrenergic and Kinase assays).  Code is available at https://github.com/Aalto-QuML/RISE.

## item_id: m_3898

TITLE: INTRABENCH: Interactive Radiological Benchmark

ABSTRACT: Current interactive segmentation approaches, inspired by the success of META’s Segment Anything model, have achieved notable advancements, however they come with substantial limitations that hinder their practical application in real clinical scenarios. These include unrealistic human interaction requirements, such as slice-by-slice operations for 2D models on 3D data, a lack of iterative refinement, and insufficient evaluation experiments. These shortcomings prevent accurate assessment of model performance and lead to inconsistent outcomes across studies. IntRaBench overcomes these challenges by offering a comprehensive and reproducible framework for evaluating interactive segmentation methods in realistic, clinically relevant scenarios. It includes diverse datasets, target structures, and segmentation models, and provides a flexible codebase that allows seamless integration of new models and prompting strategies. Additionally, we introduce advanced techniques to minimize clinician interaction, ensuring fair comparisons between 2D and 3D models. By open-sourcing IntRaBench, we invite the research community to integrate their models and prompting techniques, ensuring continuous and transparent evaluation of interactive segmentation models in 3D medical
imaging.

## item_id: m_3899

TITLE: Finite-time Analysis of Single-timescale Actor-Critic on Linear Quadratic Regulator

ABSTRACT: Actor-critic (AC) methods have achieved state-of-the-art performance in many challenging tasks. However, their convergence in most practical applications are still poorly understood. Existing works mostly consider the uncommon double-loop or two-timescale stepsize variants for the ease of analysis. We investigate the practical yet more challenging vanilla single-sample single-timescale AC for solving the canonical linear quadratic regulator problem. Specifically, the actor and the critic update only once with a single sample in each iteration using proportional stepsizes. We prove that the vanilla AC can attain an $\epsilon$-optimal solution with a sample complexity of $\tilde{\mathcal{O}}(\epsilon^{-2})$, which elucidates on the practical efficiency of single-sample single-timescale AC. We develop a novel analysis framework that directly bounds the whole interconnected iteration system without the conservative decoupling commonly adopted in previous analysis of AC. Our work presents the first finite-time analysis of single-sample single-timescale AC with a global optimality guarantee.

## item_id: m_3900

TITLE: Gated ConvNets for Letter-Based ASR

ABSTRACT: In this paper we introduce a new speech recognition system, leveraging a simple letter-based ConvNet acoustic model. The acoustic model requires only audio transcription for training -- no alignment annotations, nor any forced alignment step is needed. At inference, our decoder takes only a word list and a language model, and is fed with letter scores from the acoustic model -- no phonetic word lexicon is needed. Key ingredients for the acoustic model are Gated Linear Units and high dropout. We show near state-of-the-art results in word error rate on the LibriSpeech corpus with MFSC features, both on the clean and other configurations.

