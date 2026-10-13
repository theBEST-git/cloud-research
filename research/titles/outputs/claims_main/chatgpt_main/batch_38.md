# Batch 38 — 100 items

## item_id: m_3701

TITLE: EXAGREE: Towards Explanation Agreement in Explainable Machine Learning

ABSTRACT: Explanations in machine learning are critical for trust, transparency, and fairness. Yet, complex disagreements among these explanations limit the reliability and applicability of machine learning models, especially in high-stakes environments. We formalize four fundamental ranking-based explanation disagreement problems and introduce a novel framework, EXplanation AGREEment (EXAGREE), to bridge diverse interpretations in explainable machine learning, particularly from stakeholder-centric perspectives. Our approach leverages a Rashomon set for attribution predictions and then optimizes within this set to identify Stakeholder-Aligned Explanation Models (SAEMs) that minimize disagreement with diverse stakeholder needs while maintaining predictive performance.  Rigorous empirical analysis on synthetic and real-world datasets demonstrates that EXAGREE reduces explanation disagreement and improves fairness across subgroups in various domains. EXAGREE not only provides researchers with a new direction for studying explanation disagreement problems but also offers data scientists a tool for making better-informed decisions in practical applications.

## item_id: m_3702

TITLE: Semi-Supervised Learning with Context-Conditional Generative Adversarial Networks

ABSTRACT: We introduce a simple semi-supervised learning approach for images based on in-painting using an adversarial loss. Images with random patches removed are presented to a generator whose task is to fill in the hole, based on the surrounding pixels. The in-painted images are then presented to a discriminator network that judges if they are real (unaltered training images) or not. This task acts as a regularizer for standard supervised training of the discriminator. Using our approach we are able to directly train large VGG-style networks in a semi-supervised fashion. We evaluate on STL-10 and PASCAL datasets, where our approach obtains performance comparable or superior to existing methods.


## item_id: m_3703

TITLE: MARLlib: Extending RLlib for Multi-agent Reinforcement Learning

ABSTRACT: Despite the fast development of multi-agent reinforcement learning (MARL) methods, there is a lack of commonly-acknowledged baseline implementation and evaluation platforms. As a result, an urgent need for MARL researchers is to develop an integrated library suite, similar to the role of RLlib in single-agent RL, that delivers reliable MARL implementation and replicable evaluation in various bechmarks. To fill such a research gap, in this paper, we propose Multi-Agent RLlib (MARLlib), a comprehensive MARL algorithm library that facilitates RLlib for solving multi-agent problems. With a novel design of agent-level distributed dataflow, MARLlib manages to unify tens of algorithms, including different types of independent learning, centralized critic, and value decomposition methods; this leads to a highly composable integration of MARL algorithms that are not possible to unify before. Furthermore, MARLlib goes beyond current work by integrating diverse environment interfaces and providing flexible parameter sharing strategies; this allows to create versatile solutions to  cooperative, competitive, and mixed tasks with minimal code modifications for end users. A plethora of experiments  are conducted to substantiate the correctness of our implementation, based on which we further derive new insights on the relationship between the  performance and the design of algorithmic components. With MARLlib, we expect researchers to be able to tackle broader real-world multi-agent problems with trustworthy solutions. Our code\footnote{\url{https://github.com/ICLR2023Paper4242/MARLlib}} and documentation\footnote{\url{https://iclr2023marllib.readthedocs.io/}} are released for reference.

## item_id: m_3704

TITLE: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

ABSTRACT: State-of-the-art machine learning methods exhibit limited compositional generalization. At the same time, there is a lack of realistic benchmarks that comprehensively measure this ability, which makes it challenging to find and evaluate improvements. We introduce a novel method to systematically construct such benchmarks by maximizing compound divergence while guaranteeing a small atom divergence between train and test sets, and we quantitatively compare this method to other approaches for creating compositional generalization benchmarks. We present a large and realistic natural language question answering dataset that is constructed according to this method, and we use it to analyze the compositional generalization ability of three machine learning architectures. We find that they fail to generalize compositionally and that there is a surprisingly strong negative correlation between compound divergence and accuracy. We also demonstrate how our method can be used to create new compositionality benchmarks on top of the existing SCAN dataset, which confirms these findings.


## item_id: m_3705

TITLE: Learning the Unlearnable: Adversarial Augmentations Suppress Unlearnable Example Attacks

ABSTRACT: Unlearnable example attacks are data poisoning techniques that can be used to safeguard public data against unauthorized use for training deep learning models. These methods add stealthy perturbations to the original image, thereby making it difficult for deep learning models to learn from these training data effectively. Current research suggests that adversarial training can, to a certain degree, mitigate the impact of unlearnable example attacks, while common data augmentation methods are not effective against such poisons. Adversarial training, however, demands considerable computational resources and can result in non-trivial accuracy loss. In this paper, we introduce the UEraser method, which outperforms current defenses against different types of state-of-the-art unlearnable example attacks through a combination of effective data augmentation policies and loss-maximizing adversarial augmentations. In stark contrast to the current SOTA adversarial training methods, UEraser uses adversarial augmentations, which extends beyond the confines of $\ell_p$ perturbation budget assumed by current unlearning attacks and defenses. It also helps to improve the model's generalization ability, thus protecting against accuracy loss. UEraser wipes out the unlearning effect with loss-maximizing adversarial augmentations, thus restoring trained model accuracies. Interestingly, UEraser-Lite, a fast variant without adversarial augmentations, is also highly effective in preserving clean accuracies. On challenging unlearnable CIFAR-10, CIFAR-100, SVHN, and ImageNet-subset datasets produced with various attacks, it achieves results that are comparable to those obtained during clean training. We also demonstrate its efficacy against possible adaptive attacks. Our code is open source and available to the deep learning community.

## item_id: m_3706

TITLE: Synthetic and Natural Noise Both Break Neural Machine Translation

ABSTRACT: Character-based neural machine translation (NMT) models alleviate out-of-vocabulary issues, learn morphology, and move us closer to completely end-to-end translation systems.  Unfortunately, they are also very brittle and easily falter when presented with noisy data. In this paper, we confront NMT models with synthetic and natural sources of noise. We find that state-of-the-art models fail to translate even moderately noisy texts that humans have no trouble comprehending. We explore two approaches to increase model robustness: structure-invariant word representations and robust training on noisy texts. We find that a model based on a character convolutional neural network is able to simultaneously learn representations robust to multiple kinds of noise. 

## item_id: m_3707

TITLE: Deep reinforced active learning for multi-class image classification

ABSTRACT: High accuracy medical image classification can be limited by the costs of acquiring more data as well as the time and expertise needed to label existing images. In this paper, we apply active learning to medical image classification, a method which aims to maximise model performance on a minimal subset from a larger pool of data. We present a new active learning framework, based on deep reinforcement learning, to learn an active learning query strategy to label images based on predictions from a convolutional neural network. Our framework modifies the deep-Q network formulation, allowing us to pick data based additionally on geometric arguments in the latent space of the classifier, allowing for high accuracy multi-class classification in a batch-based active learning setting, enabling the agent to label datapoints that are both diverse and about which it is most uncertain. We apply our framework to two medical imaging datasets and compare with standard query strategies as well as the most recent reinforcement learning based active learning approach for image classification.

## item_id: m_3708

TITLE: Generating Interpretable Images with Controllable Structure

ABSTRACT: We demonstrate improved text-to-image synthesis with controllable object locations using an extension of Pixel Convolutional Neural Networks (PixelCNN). In addition to conditioning on text, we show how the model can generate images conditioned on part keypoints and segmentation masks. The character-level text encoder and image generation network are jointly trained end-to-end via maximum likelihood. We establish quantitative baselines in terms of text and structure-conditional pixel log-likelihood for three data sets: Caltech-UCSD Birds (CUB), MPII Human Pose (MHP), and Common Objects in Context (MS-COCO).

## item_id: m_3709

TITLE: Improving Fairness via Federated Learning

ABSTRACT: Recently, lots of algorithms have been proposed for learning a fair classifier from centralized data. However, how to privately train a fair classifier on decentralized data has not been fully studied yet. In this work, we first propose a new theoretical framework, with which we analyze the value of federated learning in improving fairness. Our analysis reveals that federated learning can strictly boost model fairness compared with all non-federated algorithms. We then theoretically and empirically show that the performance tradeoff of FedAvg-based fair learning algorithms is strictly worse than that of a fair classifier trained on centralized data. To resolve this, we propose FedFB, a private fair learning algorithm on decentralized data with a modified FedAvg protocol. Our extensive experimental results show that FedFB significantly outperforms existing approaches, sometimes achieving a similar tradeoff as the one trained on centralized data.

## item_id: m_3710

TITLE: Multi-Representation Attention Framework for Underwater Bioacoustic Denoising and Recognition

ABSTRACT: Automated monitoring of marine mammals in the St. Lawrence Estuary faces extreme challenges: calls span low-frequency moans to ultrasonic clicks, often overlap, and are embedded in variable anthropogenic and environmental noise. We introduce a multi-representation, attention-guided framework that first segments spectrograms to generate soft masks of biologically relevant energy and then fuses these masks with the raw inputs for multi-band, denoised classification. Image and mask embeddings are integrated via mid-level fusion, enabling the model to focus on salient spectrogram regions while preserving global context. Using real-world recordings from the Saguenay–St. Lawrence Marine Park Research Station in Canada, we demonstrate that segmentation-driven attention and mid-level fusion improve signal discrimination, reduce false positive detections, and produce reliable representations for operational marine mammal monitoring across diverse environmental conditions and signal-to-noise ratios. Beyond in-distribution evaluation, we further assess the generalization of Mask-Guided Classification (MGC) under distributional shifts by testing on spectrograms generated with alternative acoustic transformations. While high-capacity baseline models lose accuracy in this Out-of-distribution (OOD) setting, MGC maintains stable performance, with even simple fusion mechanisms (gated, concat) achieving comparable results across distributions. This robustness highlights the capacity of MGC to learn transferable representations rather than overfitting to a specific transformation, thereby reinforcing its suitability for large-scale, real-world biodiversity monitoring. We show that in all experimental settings, the MGC framework consistently outperforms baseline architectures, yielding substantial gains in accuracy on both in-distribution and OOD data.

## item_id: m_3711

TITLE: Spatiotemporal Modeling of Multivariate Signals with Graph Neural Networks and Structured State Space Models

ABSTRACT: Multivariate signals are prevalent in various domains, such as healthcare, transportation systems, and space sciences. Modeling spatiotemporal dependencies in multivariate signals is challenging due to (1) long-range temporal dependencies and (2) complex spatial correlations between sensors. To address these challenges, we propose representing multivariate signals as graphs and introduce GraphS4mer, a general graph neural network (GNN) architecture that captures both spatial and temporal dependencies in multivariate signals. Specifically, (1) we leverage Structured State Spaces model (S4), a state-of-the-art sequence model, to capture long-term temporal dependencies and (2) we propose a graph structure learning layer in GraphS4mer to automatically learn the underlying graph structures in the data.  We evaluate our proposed model on three distinct tasks and show that GraphS4mer consistently improves over existing models, including (1) seizure detection from electroencephalography signals, outperforming a previous GNN with self-supervised pretraining by 3.1 points in AUROC; (2) sleep staging from polysomnography signals, a 4.1 points improvement in macro-F1 score compared to existing sleep staging models; and (3) traffic forecasting, reducing MAE by 8.8% compared to existing GNNs and by 1.4% compared to transformer-based models.

## item_id: m_3712

TITLE: Learning with Auxiliary Activation for Memory-Efficient Training

ABSTRACT: While deep learning has achieved great success in various fields, a large amount of memory is necessary to train deep neural networks, which hinders the development of massive state-of-the-art models. The reason is the conventional learning rule, backpropagation, should temporarily store input activations of all the layers in the network. To overcome this, recent studies suggested various memory-efficient implementations of backpropagation. However, those approaches incur computational overhead due to the recomputation of activations, slowing down neural network training. In this work, we propose a new learning rule which significantly reduces memory requirements while closely matching the performance of backpropagation. The algorithm combines auxiliary activation with output activation during forward propagation, while only auxiliary activation is used during backward propagation instead of actual input activation to reduce the amount of data to be temporarily stored. We mathematically show that our learning rule can reliably train the networks whose loss landscape is convex if the auxiliary activation satisfies certain conditions. Based on this observation, we suggest candidates of auxiliary activation that satisfy those conditions. Experimental results confirm that the proposed learning rule achieves competitive performance compared to backpropagation in various models such as ResNet, Transformer, BERT, ViT, and MLP-Mixer.

## item_id: m_3713

TITLE: Neuron as an Agent

ABSTRACT: Existing multi-agent reinforcement learning (MARL) communication methods have relied on a trusted third party (TTP) to distribute reward to agents, leaving them inapplicable in peer-to-peer environments. This paper proposes reward distribution using {\em Neuron as an Agent} (NaaA) in MARL without a TTP with two key ideas: (i) inter-agent reward distribution and (ii) auction theory. Auction theory is introduced because inter-agent reward distribution is insufficient for optimization. Agents in NaaA maximize their profits (the difference between reward and cost) and, as a theoretical result, the auction mechanism is shown to have agents autonomously evaluate counterfactual returns as the values of other agents. NaaA enables representation trades in peer-to-peer environments, ultimately regarding unit in neural networks as agents. Finally, numerical experiments (a single-agent environment from OpenAI Gym and a multi-agent environment from ViZDoom) confirm that NaaA framework optimization leads to better performance in reinforcement learning.

## item_id: m_3714

TITLE: Combining graph and sequence information to learn protein representations

ABSTRACT: Computational methods that infer the function of proteins are key to understanding life at the molecular level. In recent years, representation learning has emerged as a powerful paradigm to discover new patterns among entities as varied as images, words, speech, molecules. In typical representation learning, there is only one source of data or one level of abstraction at which the learned representation occurs. However, proteins can be described by their primary, secondary, tertiary, and quaternary structure or even as nodes in protein-protein interaction networks. Given that protein function is an emergent property of all these levels of interactions in this work, we learn joint representations from both amino acid sequence and multilayer networks representing tissue-specific protein-protein interactions. Using these representations, we train machine learning models that outperform existing methods on the task of tissue-specific protein function prediction on 10 out of 13 tissues. Furthermore, we outperform existing methods by 19% on average.

## item_id: m_3715

TITLE: Learning Time-Aware Assistance Functions for Numerical Fluid Solvers

ABSTRACT: Improving the accuracy of numerical methods remains a central challenge in many disciplines and is especially important for nonlinear simulation problems. A representative example of such problems is fluid flow, which has been thoroughly studied to arrive at efficient simulations of complex flow phenomena. This paper presents a data-driven approach that learns to improve the accuracy of numerical solvers. The proposed method utilizes an advanced numerical scheme with a fine simulation resolution to acquire reference data. We, then, employ a neural network that infers a correction to move a coarse thus quickly obtainable result closer to the reference data. We provide insights into the targeted learning problem with different learning approaches: fully supervised learning methods with a naive and an optimized data acquisition as well as an unsupervised learning method with a differentiable Navier-Stokes solver. While our approach is very general and applicable to arbitrary partial differential equation models, we specifically highlight gains in accuracy for fluid flow simulations.

## item_id: m_3716

TITLE: Blending Supervised and Reinforcement Fine-Tuning with Prefix Sampling

ABSTRACT: Existing post-training techniques for large language models are broadly categorized into Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT). Each paradigm presents a distinct trade-off: SFT excels at mimicking demonstration data but can lead to problematic generalization as a form of behavior cloning. Conversely, RFT can significantly enhance a model's performance but is prone to learn unexpected behaviors, and its performance is sensitive to the initial policy. In this paper, we propose a unified view of these methods and introduce Prefix-RFT, a hybrid approach that synergizes learning from both demonstration and exploration. Using mathematical reasoning problems as a testbed, we empirically demonstrate that Prefix-RFT is both simple and effective. Not only does it surpass the performance of standalone SFT and RFT, but it also outperforms parallel mixed-policy RFT methods. A key advantage is its seamless integration into existing open-source frameworks, requiring only minimal modifications to the standard RFT pipeline. Our analysis highlights the complementary nature of SFT and RFT, validating that Prefix-RFT effectively harmonizes these two learning paradigms. Furthermore, ablation studies confirm the method's robustness to variations in the quality and quantity of demonstration data. We hope this work offers a new perspective on LLM post-training, suggesting that a unified paradigm that judiciously integrates demonstration and exploration could be a promising direction for future research.

## item_id: m_3717

TITLE: Towards trustworthy predictions from deep neural networks with fast adversarial calibration

ABSTRACT: To facilitate a wide-spread acceptance of AI systems guiding decision making in real-world applications, trustworthiness of deployed models is key. That is, it is crucial for predictive models to be uncertainty-aware and yield well-calibrated (and thus trustworthy) predictions for both in-domain samples as well as under domain shift. Recent efforts to account for predictive uncertainty include post-processing steps for trained neural networks, Bayesian neural networks as well as alternative non-Bayesian approaches such as ensemble approaches and evidential deep learning. Here, we propose an efficient yet general modelling approach for obtaining well-calibrated, trustworthy probabilities for samples obtained after a domain shift. We introduce a new training strategy combining an entropy-encouraging loss term with an adversarial calibration loss term and demonstrate that this results in well-calibrated and technically trustworthy predictions for a wide range of perturbations. We comprehensively evaluate previously proposed approaches on different data modalities, a large range of data sets, network architectures and perturbation strategies and observe that our modelling approach substantially outperforms existing state-of-the-art approaches, yielding well-calibrated predictions for both in-domain and out-of domain samples. 

## item_id: m_3718

TITLE: MaxMin-Novelty: Maximizing Novelty via Minimizing the State-Action Values in Deep Reinforcement Learning

ABSTRACT: Reinforcement learning research has achieved high acceleration in its progress starting from the initial installation of deep neural networks as function approximators to learn policies that make sequential decisions in high-dimensional state representation MDPs. While several consecutive barriers have been broken in deep reinforcement learning research (i.e. learning from high-dimensional states, learning purely via self-play), several others still stand. On this line, the question of how to explore in high-dimensional complex MDPs is a well-understudied and ongoing open problem. To address this, in our paper we propose a unique exploration technique based on maximization of novelty via minimization of the state-action value function (MaxMin Novelty). Our method is theoretically well motivated, and comes with zero computational cost while leading to significant sample efficiency gains in deep reinforcement learning training. We conduct extensive experiments in the Arcade Learning Environment with high-dimensional state representation MDPs. We show that our technique improves the human normalized median scores of Arcade Learning Environment by 248% in the low-data regime.

## item_id: m_3719

TITLE: Learning temporal evolution of probability distribution with Recurrent Neural Network

ABSTRACT: We propose to tackle a time series regression problem by computing temporal evolution of a probability density function to provide a probabilistic forecast. A Recurrent Neural Network (RNN) based model is employed to learn a nonlinear operator for temporal evolution of a probability density function. We use a softmax layer for a numerical discretization of a smooth probability density functions, which transforms a function approximation problem to a classification task. Explicit and implicit regularization strategies are introduced to impose a smoothness condition on the estimated probability distribution. A Monte Carlo procedure to compute the temporal evolution of the distribution for a multiple-step forecast is presented. The evaluation of the proposed algorithm on three synthetic and two real data sets shows advantage over the compared baselines.

## item_id: m_3720

TITLE: Supervised Chain of Thought

ABSTRACT: Large Language Models (LLMs) have revolutionized the field of natural language processing and hold significant promise for advancements in Artificial Intelligence. However, the backbone architecture of most mainstream LLMs, the Transformer, has inherent limitations regarding computational depth, making them theoretically incapable of solving many reasoning tasks that require increasing depth. Chain of Thought (CoT) techniques, however, have been shown to mitigate these architectural limitations, as demonstrated by several theoretical works, offering a viable approach to solving complex reasoning tasks that were previously out of reach.
Despite its successes, CoT and its variants (such as Tree of Thought, Graph of Thought, etc.) follow a one-prompt-for-all-tasks approach. Specifically, they rely on a single prompt structure (e.g., "think step by step") for a wide range of tasks, from counting to sorting, and from solving mathematical problems to tackling algorithmic challenges. This creates significant challenges for the model to generate the correct steps template for different tasks, as it requires searching in large prompt template space.
In this work, we build on previous theoretical analyses of CoT to demonstrate how the "one-prompt-for-all-tasks" template can negatively impact the computability of LLMs. We divide the solution space into prompt space and answer space, showing that the CoT process requires task-specific supervision to accurately navigate the prompt space and achieve optimal performance. Through experiments with the latest  LLMs, we reveal a significant gap in reasoning ability when supervision is applied versus when it is not.
Our aim is to provide insights into the mechanisms behind CoT and to inspire the effective design of CoT variants. Additionally, we highlight the key limitations of traditional ``unsupervised'' prompting approaches, suggesting the need for more nuanced, task-specific "supervised" CoT for effective reasoning with LLMs.

## item_id: m_3721

TITLE: MobileKGQA: On-Device KGQA System on Dynamic Mobile Environments

ABSTRACT: Developing a mobile system capable of generating responses based on stored user data is a crucial challenge. Since user data is stored in the form of Knowledge Graphs, the field of knowledge graph question answering (KGQA) presents a promising avenue towards addressing this problem. However, existing KGQA systems face two critical limitations that preclude their on-device deployment: resource constraints and the inability to handle data accumulation. Therefore, we propose MobileKGQA, the first on-device KGQA system capable of adapting to evolving databases with minimal resource demands. MobileKGQA significantly reduces computational overhead through embedding hashing. Moreover, it successfully adapts to evolving databases under resource constraints through a novel annotation generation method. Its mobile applicability is validated on the NVIDIA Jetson Orin Nano edge-device platform, achieving 20.3% higher performance while using only 30.4% of the energy consumed by the SOTA (state-of-the-art). On standard KGQA benchmarks, using just 7.2% of the computation and 9% of the parameters, MobileKGQA demonstrates performance that is empirically indistinguishable from the SOTA and outperforms baselines under distribution shift scenarios.

## item_id: m_3722

TITLE:  Robust Constrained Reinforcement Learning

ABSTRACT: Constrained reinforcement learning is to maximize the reward subject to constraints on utilities/costs. However, in practice it is often the case  that the training environment is not the same as the test one, due to, e.g., modeling error, adversarial attack, non-stationarity, resulting in severe performance degradation and more importantly constraint violation in the test environment. To address this challenge, we formulate the framework of robust constrained reinforcement learning under model uncertainty, where the MDP is not fixed but lies in some uncertainty set. The goal is two fold: 1) to guarantee that constraints on utilities/costs are satisfied for all MDPs in the uncertainty set, and 2) to maximize the worst-case reward performance over the uncertainty set. We design a robust primal-dual approach, and further develop theoretical guarantee on its convergence, complexity and robust feasibility. We then investigate a concrete example of $\delta$-contamination uncertainty set, design an online and model-free algorithm and theoretically characterize its sample complexity. 

## item_id: m_3723

TITLE: Improving the Improved Training of Wasserstein GANs: A Consistency Term and Its Dual Effect

ABSTRACT: Despite being impactful on a  variety of problems and applications, the generative adversarial nets (GANs) are remarkably difficult to train. This issue is formally analyzed by \cite{arjovsky2017towards}, who also propose an alternative direction to avoid the caveats in the minmax two-player training of GANs. The corresponding algorithm, namely, Wasserstein GAN (WGAN) hinges on the 1-Lipschitz continuity of the discriminators. In this paper, we propose a novel approach for enforcing the Lipschitz continuity in the training procedure of WGANs. Our approach seamlessly connects WGAN with one of the recent semi-supervised learning approaches. As  a result, it gives rise to not only better photo-realistic samples  than the previous methods  but also state-of-the-art semi-supervised learning results.  In particular, to the best of our knowledge, our approach gives rise to the inception score of more than 5.0 with only 1,000 CIFAR10 images and is the first that exceeds the accuracy of 90\% the CIFAR10 datasets using only 4,000 labeled images.


## item_id: m_3724

TITLE: Large-scale Cloze Test Dataset Designed by Teachers

ABSTRACT: Cloze test is widely adopted in language exams to evaluate students' language proficiency. In this paper, we propose the first large-scale human-designed cloze test dataset CLOTH in which the questions were used in middle-school and high-school language exams. With the missing blanks carefully created by teachers and candidate choices purposely designed to be confusing, CLOTH requires a deeper language understanding and a wider attention span than previous automatically generated cloze datasets. We show humans outperform dedicated designed baseline models by a significant margin, even when the model is trained on sufficiently large external data. We investigate the source of the performance gap, trace model deficiencies to some distinct properties of CLOTH, and identify the limited ability of comprehending a long-term context to be the key bottleneck. In addition, we find that human-designed data leads to a larger gap between the model's performance and human performance when compared to automatically generated data. 

## item_id: m_3725

TITLE: TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning

ABSTRACT: Combining deep model-free reinforcement learning with on-line planning is a promising approach to building on the successes of deep RL. On-line planning with look-ahead trees has proven successful in environments where transition models are known a priori. However, in complex environments where transition models need to be learned from data, the deficiencies of learned models have limited their utility for planning. To address these challenges, we propose TreeQN, a differentiable, recursive, tree-structured model that serves as a drop-in replacement for any value function network in deep RL with discrete actions. TreeQN dynamically constructs a tree by recursively applying a transition model in a learned abstract state space and then aggregating predicted rewards and state-values using a tree backup to estimate Q-values. We also propose ATreeC, an actor-critic variant that augments TreeQN with a softmax layer to form a stochastic policy network. Both approaches are trained end-to-end, such that the learned model is optimised for its actual use in the tree. We show that TreeQN and ATreeC outperform n-step DQN and A2C on a box-pushing task, as well as n-step DQN and value prediction networks (Oh et al., 2017) on multiple Atari games. Furthermore, we present ablation studies that demonstrate the effect of different auxiliary losses on learning transition models.

## item_id: m_3726

TITLE: Fengbo: a Clifford Neural Operator pipeline for 3D PDEs in Computational Fluid Dynamics

ABSTRACT: We introduce Fengbo, a pipeline entirely in Clifford Algebra to solve 3D partial differential equations (PDEs) specifically for computational fluid dynamics (CFD). Fengbo is an architecture composed of only 3D convolutional and Fourier Neural Operator (FNO) layers, all working in 3D Clifford Algebra. It models the PDE solution problem as an interpretable mapping from the geometry to the physics of the problem. Despite having just few layers, Fengbo achieves competitive accuracy, superior to 5 out of 6 proposed models reported in \cite{li2024geometry} for the $\emph{ShapeNet Car}$ dataset, and it does so with only 42 million trainable parameters, at a reduced computational complexity compared to graph-based methods, and estimating jointly pressure \emph{and} velocity fields. In addition, the output of each layer in Fengbo can be clearly visualised as objects and physical quantities in 3D space, making it a whitebox model.  
By leveraging Clifford Algebra and establishing a direct mapping from the geometry to the physics of the PDEs, Fengbo provides an efficient, geometry- and physics-aware approach to solving complex PDEs.

## item_id: m_3727

TITLE: SinkQ: Accurate 2-bit KV Cache Quantization with Dynamic Sink Tracking

ABSTRACT: The impressive capabilities of large language models (LLMs) come at the cost of substantial computational resources during deployment. While KV Cache can significantly reduce recomputation during inference, it also introduces additional memory overhead. KV Cache quantization presents a promising solution, striking a good balance between memory usage and accuracy.
Previous research has shown that the Keys are distributed by channel, while the Values are distributed by token. Consequently, the common practice is to apply channel-wise quantization to the Keys and token-wise quantization to the Values. However, our further investigation reveals that a small subset of unusual tokens exhibit unique characteristics that deviate from this pattern, which can substantially impact quantization accuracy. Furthermore, these tokens often have higher attention scores, exacerbating their quantization errors.
To address this, we develop a simple yet effective method to identify these tokens accurately during the decoding process and exclude them from quantization, significantly improving overall accuracy. Extensive experiments show that our method achieves significant accuracy improvements under 2-bit quantization and can deliver a 6.4× reduction in memory usage and a 2.3× increase in throughput. Our code will be released upon acceptance.

## item_id: m_3728

TITLE: Semantic Alignment for Effective Feature Fusion in Real-Time Object Detection

ABSTRACT: Feature fusion networks are essential components in modern object detectors, aggregating multi-scale features from hierarchical levels to detect objects of varying sizes. 
However, a significant challenge is that fusing features from different levels often leads to semantic inconsistency due to their distinct representations. 
While many prior works have attempted to address this, they often incur substantial computational and parameter overhead, limiting their real-time applicability, and in some cases lack generality across different detection architectures.
In this work, we propose a novel lightweight semantic alignment module called Feature Interaction NEtwork (FINE). 
This module refines low-level features by integrating high-level contextual cues via a cross-level attention mechanism prior to fusion. 
To minimize overhead, FINE combines a kernel-based linear attention with a novel spatial bottleneck design. 
This design drastically reduces the attention sequence length while preserving the channel-wise semantics essential for effective semantic alignment. 
FINE is generally applicable to various detectors, including Faster R-CNN, YOLO series, and RT-DETR, and 
consistently improves detection accuracy without compromising efficiency.

## item_id: m_3729

TITLE: Leveraging Uncertainty Estimates To Improve Classifier Performance

ABSTRACT: Binary classification typically involves predicting the label of an instance based on whether the model score for the positive class exceeds a threshold chosen based on the application requirements (e.g., maximizing recall for a precision bound). However, model scores are often not aligned with true positivity rate. This is especially true when the training involves a differential sampling of classes or there is distributional drift between train and test settings. In this paper, we provide theoretical analysis and empirical evidence of the dependence of estimation bias on both uncertainty and model score. Further, we  formulate the decision boundary selection using both model score and uncertainty, prove that it is NP-hard, and present  algorithms  based on dynamic programming and isotonic regression.  Evaluation of the proposed algorithms on three real-world datasets yield  25\%-40\%  improvement in recall at high precision bounds over the traditional approach of using model score alone, highlighting the benefits of leveraging uncertainty.

## item_id: m_3730

TITLE: Reinforcement and Imitation Learning for Diverse Visuomotor Skills

ABSTRACT: We propose a general deep reinforcement learning method and apply it to robot manipulation tasks. Our approach leverages demonstration data to assist a reinforcement learning agent in learning to solve a wide range of tasks, mainly previously unsolved. We train visuomotor policies end-to-end to learn a direct mapping from RGB camera inputs to joint velocities. Our experiments indicate that our reinforcement and imitation approach can solve contact-rich robot manipulation tasks that neither the state-of-the-art reinforcement nor imitation learning method can solve alone. We also illustrate that these policies achieved zero-shot sim2real transfer by training with large visual and dynamics variations.

## item_id: m_3731

TITLE: Modelling Relational Time Series using Gaussian Embeddings

ABSTRACT: We address the problem of modeling multiple simultaneous time series where the observations are correlated not only inside each series, but among the different series. This problem happens in many domains such as ecology, meteorology, etc.  We propose a new dynamical state space model, based on representation learning, for modeling the evolution of such series. The joint relational and temporal dynamics of the series are modeled as Gaussian distributions in a latent space. A decoder maps the latent representations to the observations. The two components (dynamic model and decoder) are jointly trained. Using stochastic representations allows us to model the uncertainty inherent to observations and to predict unobserved values together with a confidence in the prediction.

## item_id: m_3732

TITLE: SEA-SpeechBench: A Large-Scale Multitask Benchmark for Speech Understanding Across Southeast Asia

ABSTRACT: The rapid advancement of audio and multimodal large language models has unlocked transformative speech understanding capabilities, yet evaluation frameworks remain predominantly English-centric, leaving Southeast Asian (SEA) languages critically underrepresented. We introduce SEA-SpeechBench, the first large-scale multitask benchmark that evaluates speech understanding in 11 SEA languages through more than 97,000 samples and 597 hours of curated audio data. Our benchmark comprises 9 diverse tasks across 3 categories: speech processing (automatic speech recognition, speech translation, spoken question answering), paralinguistic analysis (emotion, gender, age, speaker recognition), and temporal understanding, a novel dimension featuring timestamped content queries and temporal localization within extended audio sequences up to 3 minutes. We implement multilingual prompting in both native SEA languages and English to reflect user interactions with audio-language models. 
Evaluation of leading open-source and proprietary systems reveals marked performance gaps. Across all models, performance remains underwhelming on temporal reasoning, emotion recognition, and speech translation, with most scores falling below 20. Prompting in low-resource languages such as Burmese, Lao, Tamil, and Khmer lag behind English by over 5%.
Our findings expose critical model limitations and underscore the need for inclusive model development.

## item_id: m_3733

TITLE: Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference

ABSTRACT: Lack of performance when it comes to continual learning over non-stationary distributions of data remains a major challenge in scaling neural network learning to more human realistic settings. In this work we propose a new conceptualization of the continual learning problem in terms of a temporally symmetric trade-off between transfer and interference that can be optimized by enforcing gradient alignment across examples. We then propose a new algorithm, Meta-Experience Replay (MER), that directly exploits this view by combining experience replay with optimization based meta-learning. This method learns parameters that make interference based on future gradients less likely and transfer based on future gradients more likely. We conduct experiments across continual lifelong supervised learning benchmarks and non-stationary reinforcement learning environments demonstrating that our approach consistently outperforms recently proposed baselines for continual learning. Our experiments show that the gap between the performance of MER and baseline algorithms grows both as the environment gets more non-stationary and as the fraction of the total experiences stored gets smaller. 

## item_id: m_3734

TITLE: Non-Gaussian Process Regression

ABSTRACT: Standard GPs offer a flexible modelling tool for well-behaved processes. However, deviations from Gaussianity are expected to appear in real world datasets, with structural outliers and shocks routinely observed. In these cases GPs can fail to model uncertainty adequately and may over-smooth inferences. Here we extend the GP framework into a new class of time-changed GPs that allow for straightforward modelling of heavy-tailed non-Gaussian behaviours, while retaining a tractable conditional GP structure through an infinite mixture of non-homogeneous GPs representation. The conditional GP structure is obtained by conditioning the observations on a latent transformed input space and the random evolution of the latent transformation is modelled using a Lévy process which allows Bayesian inference in both the posterior predictive density and the latent transformation function. We present  Markov chain Monte Carlo inference procedures for this model and demonstrate the potential benefits compared to a standard GP.

## item_id: m_3735

TITLE: A View From Somewhere: Human-Centric Face Representations

ABSTRACT: Few datasets contain self-identified demographic information, inferring demographic information risks introducing additional biases, and collecting and storing data on sensitive attributes can carry legal risks. Besides, categorical demographic labels do not necessarily capture all the relevant dimensions of human diversity. We propose to implicitly learn a set of continuous face-varying dimensions, without ever asking an annotator to explicitly categorize a person. We uncover the dimensions by learning on A View From Somewhere (AVFS) dataset of 638,180 human judgments of face similarity. We demonstrate the utility of our learned embedding space for predicting face similarity judgments, collecting continuous face attribute values, attribute classification, and comparative dataset diversity auditing. Moreover, using a novel conditional framework, we show that an annotator's demographics influences the \emph{importance} they place on different attributes when judging similarity, underscoring the \emph{need} for diverse annotator groups to avoid biases. Data and code are available at \url{https://github.com/SonyAI/a_view_from_somewhere}.

## item_id: m_3736

TITLE: Debiasing Concept-based Explanations with Causal Analysis

ABSTRACT: Concept-based explanation approach is a popular model interpertability tool because it expresses the reasons for a model's predictions in terms of concepts that are meaningful for the domain experts. In this work, we study the problem of the concepts being correlated with confounding information in the features. We propose a new causal prior graph for modeling the impacts of unobserved variables and a method to remove the impact of confounding information and noise using a two-stage regression technique borrowed from the instrumental variable literature. We also model the completeness of the concepts set and show that our debiasing method works when the concepts are not complete. Our synthetic and real-world experiments demonstrate the success of our method in removing biases and improving the ranking of the concepts in terms of their contribution to the explanation of the predictions.

## item_id: m_3737

TITLE: LEARNING DIFFICULT PERCEPTUAL TASKS WITH HODGKIN-HUXLEY NETWORKS

ABSTRACT: This paper demonstrates that a computational neural network model using ion channel-based conductances to transmit information can solve standard computer vision datasets at near state-of-the-art performance. Although not fully biologically accurate, this model incorporates fundamental biophysical principles underlying the control of membrane potential and the processing of information by Ohmic ion channels. The key computational step employs Conductance-Weighted Averaging (CWA) in place of the traditional affine transformation, representing a fundamentally different computational principle. 
Importantly, CWA based networks are self-normalizing and range-limited. We also demonstrate for the first time that a network with excitatory and inhibitory neurons and nonnegative synapse strengths can successfully solve computer vision problems. Although CWA models do not yet surpass the current state-of-the-art in deep learning, the results are competitive on CIFAR-10. There remain avenues for improving these networks, e.g. by more closely modeling ion channel function and connectivity patterns of excitatory and inhibitory neurons found in the brain.  

## item_id: m_3738

TITLE: Extensions and Limitations of the Neural GPU

ABSTRACT: The Neural GPU is a recent model that can learn algorithms such as multi-digit binary addition and binary multiplication in a way that generalizes to inputs of arbitrary length.  We show that there are two simple ways of improving the performance of the Neural GPU: by carefully designing a curriculum, and by increasing model size.  The latter requires a memory efficient implementation, as a naive implementation of the Neural GPU is memory intensive.  We find that these techniques increase the set of algorithmic problems that can be solved by the Neural GPU: we have been able to learn to perform all the arithmetic operations (and generalize to arbitrarily long numbers) when the arguments are given in the decimal representation (which, surprisingly, has not been possible before). We have also been able to train the Neural GPU to evaluate long arithmetic expressions with multiple operands that require respecting the  precedence order of the operands, although these have succeeded only in their binary representation, and not with perfect accuracy.

In addition, we gain insight into the Neural GPU by investigating its failure modes.  We find that Neural GPUs that correctly generalize to arbitrarily long numbers still fail to compute the correct answer on highly-symmetric, atypical inputs: for  example, a Neural GPU that achieves near-perfect generalization on decimal multiplication of up to 100-digit long numbers can fail on $000000\dots002 \times 000000\dots002$ while succeeding at $2 \times 2$.  These failure modes are reminiscent of adversarial examples.

## item_id: m_3739

TITLE: Language Decision Transformers with Exponential Tilt for Interactive Text Environments

ABSTRACT: Text-based game environments are challenging because agents must deal with long sequences of text, execute compositional actions using text, and learn from sparse rewards. We address these challenges by proposing Language Decision Transformers (LDTs), a framework that is based on transformer language models and decision transformers (DTs). Our LDTs extend DTs with 3 components: (1) exponential tilt to guide the agent towards high obtainable goals, (2) novel goal conditioning methods yielding better results than the traditional return-to-go (sum of all future rewards), and (3) a model of future observations that improves agent performance. LDTs are the first to address offline RL with DTs on these challenging games. Our experiments show that LDTs achieve the highest scores among many different types of agents on some of the most challenging Jericho games, such as Enchanter.

## item_id: m_3740

TITLE: Human-like Clustering with Deep Convolutional Neural Networks

ABSTRACT: Classification and clustering have been studied separately in machine learning and computer vision. Inspired by the recent success of deep learning models in solving various vision problems (e.g., object recognition, semantic segmentation) and the fact that humans serve as the gold standard in assessing clustering algorithms, here, we advocate for a unified treatment of the two problems and suggest that hierarchical frameworks that progressively build complex patterns on top of the simpler ones (e.g., convolutional neural networks) offer a promising solution. We do not dwell much on the learning mechanisms in these frameworks as they are still a matter of debate, with respect to biological constraints. Instead, we emphasize on the compositionality of the real world structures and objects. In particular, we show that CNNs, trained end to end using back propagation with noisy labels, are able to cluster data points belonging to several overlapping shapes, and do so much better than the state of the art algorithms. The main takeaway lesson from our study is that mechanisms of human vision, particularly the hierarchal organization of the visual ventral stream should be taken into account in clustering algorithms (e.g., for learning representations in an unsupervised manner or with minimum supervision) to reach human level clustering performance. This, by no means, suggests that other methods do not hold merits. For example, methods relying on pairwise affinities (e.g., spectral clustering) have been very successful in many cases but still fail in some cases (e.g., overlapping clusters).

## item_id: m_3741

TITLE: Compute- and Memory-Efficient Reinforcement Learning with Latent Experience Replay

ABSTRACT: Recent advances in off-policy deep reinforcement learning (RL) have led to impressive success in complex tasks from visual observations. Experience replay improves sample-efficiency by reusing experiences from the past, and convolutional neural networks (CNNs) process high-dimensional inputs effectively. However, such techniques demand high memory and computational bandwidth. In this paper, we present Latent Vector Experience Replay (LeVER), a simple modification of existing off-policy RL methods, to address these computational and memory requirements without sacrificing the performance of RL agents. To reduce the computational overhead of gradient updates in CNNs, we freeze the lower layers of CNN encoders early in training due to early convergence of their parameters. Additionally, we reduce memory requirements by storing the low-dimensional latent vectors for experience replay instead of high-dimensional images, enabling an adaptive increase in the replay buffer capacity, a useful technique in constrained-memory settings. In our experiments, we show that LeVER does not degrade the performance of RL agents while significantly saving computation and memory across a diverse set of DeepMind Control environments and Atari games. Finally, we show that LeVER is useful for computation-efficient transfer learning in RL because lower layers of CNNs extract generalizable features, which can be used for different tasks and domains.

## item_id: m_3742

TITLE: SSoC: Learning Spontaneous and Self-Organizing Communication for Multi-Agent Collaboration

ABSTRACT: Multi-agent collaboration is required by numerous real-world problems. Although distributed setting is usually adopted by practical systems, local range communication and information aggregation still matter in fulfilling complex tasks. For multi-agent reinforcement learning, many previous studies have been dedicated to design an effective communication architecture. However, existing models usually suffer from an ossified communication structure, e.g., most of them predefine a particular communication mode by specifying a fixed time frequency and spatial scope for agents to communicate regardless of necessity. Such design is incapable of dealing with multi-agent scenarios that are capricious and complicated, especially when only partial information is available. Motivated by this, we argue that the solution is to build a spontaneous and self-organizing communication (SSoC) learning scheme. By treating the communication behaviour as an explicit action, SSoC learns to organize communication in an effective and efficient way. Particularly, it enables each agent to spontaneously decide when and who to send messages based on its observed states. In this way, a dynamic inter-agent communication channel is established in an online and self-organizing manner. The agents also learn how to adaptively aggregate the received messages and its own hidden states to execute actions. Various experiments have been conducted to demonstrate that SSoC really learns intelligent message passing among agents located far apart. With such agile communications, we observe that effective collaboration tactics emerge which have not been mastered by the compared baselines.

## item_id: m_3743

TITLE: Sparse Coding with Gated Learned ISTA

ABSTRACT: In this paper, we study the learned iterative shrinkage thresholding algorithm (LISTA) for solving sparse coding problems.  Following assumptions made by prior works, we first discover that the code components in its estimations may be lower than expected, i.e., require gains, and to address this problem, a gated mechanism amenable to theoretical analysis is then introduced. Specific design of the gates is inspired by convergence analyses of the mechanism and hence its effectiveness can be formally guaranteed. In addition to the gain gates, we further introduce overshoot gates for compensating insufficient step size in LISTA. Extensive empirical results confirm our theoretical findings and verify the effectiveness of our method.

## item_id: m_3744

TITLE: Measuring the Interpretability of Unsupervised Representations via Quantized Reversed Probing

ABSTRACT: Self-supervised visual representation learning has recently attracted significant research interest. While a common way to evaluate self-supervised representations is through transfer to various downstream tasks, we instead investigate the problem of measuring their interpretability, i.e. understanding the semantics encoded in raw representations. We formulate the latter as estimating the mutual information between the representation and a space of manually labelled concepts. To quantify this we introduce a decoding bottleneck: information must be captured by simple predictors, mapping concepts to clusters in representation space. This approach, which we call reverse linear probing, provides a single number sensitive to the semanticity of the representation. This measure is also able to detect when the representation contains combinations of concepts (e.g., "red apple'') instead of just individual attributes ("red'' and "apple'' independently). Finally, we propose to use supervised classifiers to automatically label large datasets in order to enrich the space of concepts used for probing. We use our method to evaluate a large number of self-supervised representations, ranking them by interpretability, highlight the differences that emerge compared to the standard evaluation with linear probes and discuss several qualitative insights. Code at: https://github.com/iro-cp/ssl-qrp.

## item_id: m_3745

TITLE: An analytic theory of generalization dynamics and transfer learning in deep linear networks

ABSTRACT: Much attention has been devoted recently to the generalization puzzle in deep learning: large, deep networks can generalize well, but existing theories bounding generalization error are exceedingly loose, and thus cannot explain this striking performance. Furthermore, a major hope is that knowledge may transfer across tasks, so that multi-task learning can improve generalization on individual tasks. However we lack analytic theories that can quantitatively predict how the degree of knowledge transfer depends on the relationship between the tasks. We develop an analytic theory of the nonlinear dynamics of generalization in deep linear networks, both within and across tasks. In particular, our theory provides analytic solutions to the training and testing error of deep networks as a function of training time, number of examples, network size and initialization, and the task structure and SNR. Our theory reveals that deep networks progressively learn the most important task structure first, so that generalization error at the early stopping time primarily depends on task structure and is independent of network size. This suggests any tight bound on generalization error must take into account task structure, and explains observations about real data being learned faster than random data. Intriguingly our theory also reveals the existence of a learning algorithm that proveably out-performs neural network training through gradient descent. Finally, for transfer learning, our theory reveals that knowledge transfer depends sensitively, but computably, on the SNRs and input feature alignments of pairs of tasks.

## item_id: m_3746

TITLE: Diminishing Batch Normalization

ABSTRACT: In this paper, we propose a generalization of the BN algorithm, diminishing batch normalization (DBN), where we update the BN parameters in a diminishing moving average way. Batch normalization (BN) is very effective in accelerating the convergence of a neural network training phase that it has become a common practice. 
Our proposed DBN algorithm remains the overall structure of the original BN algorithm while introduces a weighted averaging update to some trainable parameters. 
We provide an analysis of the convergence of the DBN algorithm that converges to a stationary point with respect to trainable parameters. Our analysis can be easily generalized for original BN algorithm by setting some parameters to constant. To the best knowledge of authors, this analysis is the first of its kind for convergence with Batch Normalization introduced. We analyze a two-layer model with arbitrary activation function. 
The primary challenge of the analysis is the fact that some parameters are updated by gradient while others are not. 
The convergence analysis applies to any activation function that satisfies our common assumptions.
For the analysis, we also show the sufficient and necessary conditions for the stepsizes and diminishing weights to ensure the convergence. 
In the numerical experiments, we use more complex models with more layers and ReLU activation. We observe that DBN outperforms the original BN algorithm on Imagenet, MNIST, NI and CIFAR-10 datasets with reasonable complex FNN and CNN models.

## item_id: m_3747

TITLE: RNAS: Robust Network Architecture Search beyond DARTS

ABSTRACT: The vulnerability of Deep Neural Networks (DNNs) (i.e., susceptibility to adversarial attacks) severely limits the application of DNNs. Most of the existing methods improve the robustness of the model from weights optimization, such as adversarial training and regularization. However, the architecture of DNNs is also a key factor to robustness, which is often neglected or underestimated. We propose a Robust Network Architecture Search (RNAS) to address this problem. In our method, we define a network vulnerability metric based on the features’ deviation between clean examples and adversarial examples. Through constraining this vulnerability, we search the robust architecture and solve it by iterative optimization. The extensive experiments conducted on CIFAR-10/100 and SVHN show that our model achieves the best performance under various adversarial attacks compared with extensive baselines and state-of-the-art methods.

## item_id: m_3748

TITLE: Hierarchical compositional feature learning

ABSTRACT: We introduce the hierarchical compositional network (HCN), a directed generative model able to discover and disentangle, without supervision, the building blocks of a set of binary images. The building blocks are binary features defined hierarchically as a composition of some of the features in the layer immediately below, arranged in a particular manner. At a high level, HCN is similar to a sigmoid belief network with pooling. Inference and learning in HCN are very challenging and existing variational approximations do not work satisfactorily. A main contribution of this work is to show that both can be addressed using max-product message passing (MPMP) with a particular schedule (no EM required). Also, using MPMP as an inference engine for HCN makes new tasks simple: adding supervision information, classifying images, or performing inpainting all correspond to clamping some variables of the model to their known values and running MPMP on the rest. When used for classification, fast inference with HCN has exactly the same functional form as a convolutional neural network (CNN) with linear activations and binary weights. However, HCN’s features are qualitatively very different.

## item_id: m_3749

TITLE: STay-On-the-Ridge (STON'R): Guaranteed Convergence to Local Minimax Equilibrium in Nonconvex-Nonconcave Games

ABSTRACT: Min-max optimization problems involving nonconvex-nonconcave objectives have found important applications in adversarial training and other multi-agent learning settings. Yet, no known gradient descent-based method is guaranteed to converge to (even local notions of) min-max equilibrium in the nonconvex-nonconcave setting. For all known methods, there exist relatively simple objectives for which they cycle or exhibit other undesirable behavior different from converging to a point, let alone to some game-theoretically meaningful one [Flokas et al. '19, Hsieh et al. '21]. The only known convergence guarantees hold under the strong assumption that the initialization is very close to a local min-max equilibrium [Wang et al. '19]. Moreover, the afore-described challenges are not just theoretical curiosities. All known methods are  unstable in practice, even in simple settings.
  
We propose the first method that is guaranteed to converge to a local min-max equilibrium for smooth nonconvex-nonconcave objectives. Our method is second-order and provably escapes limit cycles as long as it is initialized at an easy-to-find initial point. Both the definition of our method and its convergence analysis are motivated by the topological nature of the problem. In particular, our method is not designed to decrease some potential function, such as the distance of its iterate from the set of local min-max equilibria or the projected gradient of the objective, but is designed to satisfy a topological property that guarantees the avoidance of cycles and implies its convergence. 

## item_id: m_3750

TITLE: PointConvFormer: Revenge of the Point-Based Convolution

ABSTRACT: We introduce PointConvFormer, a novel building block for point cloud based deep network architectures. Inspired by generalization theory, PointConvFormer combines ideas from point convolution, where filter weights are only based on relative position, and Transformers which utilize feature-based attention. In PointConvFormer, attention computed from feature difference between points in the neighborhood is used to modify the convolutional weights at each point. Hence, we preserved the invariances from point convolution, whereas attention helps to select relevant points in the neighborhood for convolution. We experiment on both semantic segmentation and scene flow estimation tasks on point clouds with multiple datasets including ScanNet, SemanticKitti, FlyingThings3D and KITTI. Our results show that PointConvFormer substantially outperforms classic convolutions, regular transformers, and voxelized sparse convolution approaches with much smaller and faster networks. Visualizations show that PointConvFormer performs similarly to convolution on flat areas, whereas the neighborhood selection effect is stronger on object boundaries, showing that it has got the best of both worlds. The code will be available with the final version.

## item_id: m_3751

TITLE: Momentum Contrastive Autoencoder: Using Contrastive Learning for Latent Space Distribution Matching in WAE

ABSTRACT: Wasserstein autoencoder (WAE) shows that matching two distributions is equivalent to minimizing a simple autoencoder (AE) loss under the constraint that the latent space of this AE matches a pre-specified prior distribution. This latent space distribution matching is a core component of WAE, and a challenging task. In this paper, we propose to use the contrastive learning framework that has been shown to be effective for self-supervised representation learning, as a means to resolve this problem. We do so by exploiting the fact that contrastive learning objectives optimize the latent space distribution to be uniform over the unit hyper-sphere, which can be easily sampled from. 
We show that using the contrastive learning framework to optimize the WAE loss achieves faster convergence and more stable optimization compared with existing popular algorithms for WAE. This is also reflected in the FID scores on CelebA and CIFAR-10 datasets, and the realistic generated image quality on the CelebA-HQ dataset.

## item_id: m_3752

TITLE: LAVITA: Latent Video Diffusion Models with Spatio-temporal Transformers

ABSTRACT: Video generation is a challenging task as it requires effective modeling of rich spatio-temporal information from high-dimensional video data. To tackle this challenge, we propose a novel architecture, the LAtent VIdeo diffusion model with spatio-temporal TrAnsformers, referred to as LAVITA, which integrates the Transformer architecture into diffusion models for the first time within the realm of video generation. Conceptually, LATIVA models spatial and temporal information separately to accommodate their inherent disparities as well as to reduce the computational complexity. Following this design strategy, we design several Transformer-based model variants to integrate spatial and temporal information harmoniously. Moreover, we identify the best practices in architectural choices and learning strategies for LAVITA through rigorous empirical analysis. Our comprehensive evaluation demonstrates that LAVITA achieves state-of-the-art performance across several standard video generation benchmarks, including FaceForensics, SkyTimelapse, UCF101, and Taichi-HD, outperforming current best models. We strongly believe that LAVITA provides valuable insights for future research on incorporating Transformers into diffusion models for video generation.

## item_id: m_3753

TITLE: Collaborative Gym: A Framework for Enabling and Evaluating Human-Agent Collaboration

ABSTRACT: While the advancement of large language models has spurred the development of AI agents to automate tasks, numerous use cases inherently require agents to collaborate with humans due to humans' latent preferences, domain expertise, or the need for control. To facilitate the study of human-agent collaboration, we introduce Collaborative Gym (Co-Gym), an open framework for developing and evaluating collaborative agents that engage in bidirectional communication with humans while interacting with task environments. We describe how the framework enables the implementation of new task environments and coordination between humans and agents through a flexible, non-turn-taking interaction paradigm, along with an evaluation suite that assesses both collaboration outcomes and processes. Our framework provides both a simulated condition with a reliable user simulator and a real-world condition with an interactive web application. Initial benchmark experiments across three representative tasks-creating travel plans, writing related work sections, and analyzing tabular data-demonstrate the benefits of human-agent collaboration: The best-performing collaborative agents consistently outperform their fully autonomous counterparts in task performance, achieving win rates of 86% in Travel Planning, 74% in Tabular Analysis, and 66% in Related Work when evaluated by real users. Despite these improvements, our evaluation reveals persistent limitations in current language models and agents, with communication and situational awareness failures observed in 65% and 40% of cases in the real condition, respectively. Released under the permissive MIT license, Co-Gym supports the addition of new task environments and can be used to develop collaborative agent applications, while its evaluation suite enables assessment and improvement of collaborative agents.

## item_id: m_3754

TITLE: Learning from multiscale wavelet superpixels using GNN with spatially heterogeneous pooling

ABSTRACT: Neural networks have become the standard for image classification tasks. On one hand, convolutional neural networks (CNNs) achieve state-of-the-art performance by learning from a regular grid representation of images. On the other hand, graph neural networks (GNNs) have shown promise in learning image classification from an embedded superpixel graph. However, in the latter, studies have been restricted to SLIC superpixels, where 1) a single target number of superpixels is arbitrarily defined for an entire dataset irrespective of differences across images and 2) the superpixels in a given image are of similar size despite intrinsic multiscale structure. In this study, we investigate learning from a new principled representation in which individual images are represented by an image-specific number of multiscale superpixels. We propose WaveMesh, a wavelet-based superpixeling algorithm, where the number and sizes of superpixels in an image are systematically computed based on the image content. We also present WavePool, a spatially heterogeneous pooling scheme tailored to WaveMesh superpixels. We study the feasibility of learning from the WaveMesh superpixel representation using SplineCNN, a state-of-the-art network for image graph classification. We show that under the same network architecture and training settings, SplineCNN with original Graclus-based pooling learns from WaveMesh superpixels on-par with SLIC superpixels. Additionally, we observe that the best performance is achieved when replacing Graclus-based pooling with WavePool while using WaveMesh superpixels.

## item_id: m_3755

TITLE: Learning Self-Correctable Policies and Value Functions from Demonstrations with Negative Sampling

ABSTRACT: Imitation learning, followed by reinforcement learning algorithms, is a promising paradigm to solve complex control tasks sample-efficiently. However, learning from demonstrations often suffers from the covariate shift problem, which results
in cascading errors of the learned policy. We introduce a notion of conservatively extrapolated value functions, which provably lead to policies with self-correction. We design an algorithm Value Iteration with Negative Sampling (VINS) that practically learns such value functions with conservative extrapolation. We show that VINS can correct mistakes of the behavioral cloning policy on simulated robotics benchmark tasks. We also propose the algorithm of using VINS to initialize a reinforcement learning algorithm, which is shown to outperform prior works in sample efficiency.

## item_id: m_3756

TITLE: Learning with Mixture of Prototypes for Out-of-Distribution Detection

ABSTRACT: Out-of-distribution (OOD) detection aims to detect testing samples far away from the in-distribution (ID) training data, which is crucial for the safe deployment of machine learning models in the real world. Distance-based OOD detection methods have emerged with enhanced deep representation learning. They identify unseen OOD samples by measuring their distances from ID class centroids or prototypes. However, existing approaches learn the representation relying on oversimplified data assumptions, e.g. modeling ID data of each class with one centroid class prototype or using loss functions not designed for OOD detection, which overlook the natural diversities within the data. Naively enforcing data samples of each class to be compact around only one prototype leads to inadequate modeling of realistic data and limited performance. To tackle these issues, we propose PrototypicAl Learning with a Mixture of prototypes (PALM) that models each class with multiple prototypes to capture the sample diversities, which learns more faithful and compact samples embeddings for enhanching OOD detection. Our method automatically identifies and dynamically updates prototypes, assigning each sample to a subset of prototypes via reciprocal neighbor soft assignment weights. To learn embeddings with multiple prototypes, PALM optimizes a maximum likelihood estimation (MLE) loss to encourage the sample embeddings to compact around the associated prototypes, as well as a contrastive loss on all prototypes to enhance intra-class compactness and inter-class discrimination at the prototype level. Compared to previous methods with prototypes, the proposed mixture prototype modeling of PALM promotes the representations of each ID class to be more compact and separable from others and the unseen OOD samples, resulting in more reliable OOD detection. Moreover, the automatic estimation of prototypes enables our approach to be extended to the challenging OOD detection task with unlabelled ID data. Extensive experiments demonstrate the superiority of PALM over previous methods, achieving state-of-the-art average AUROC performance of 93.82 on the challenging CIFAR-100 benchmark.

## item_id: m_3757

TITLE: Cognitive Alignment in Personality Reasoning: Leveraging Prototype Theory for MBTI Inference

ABSTRACT: Personality recognition from text is typically cast as hard-label classification, which obscures the graded, prototype-like nature of human personality judgments. We present \textsc{ProtoMBTI}, a cognitively aligned framework for MBTI inference that operationalizes prototype theory within an LLM-based pipeline. First, we construct a balanced, quality-controlled corpus via LLM-guided multi-dimensional augmentation (semantic, linguistic, sentiment). Next, we LoRA-fine-tune a lightweight ($\leq$2B) encoder to learn discriminative embeddings and to standardize a bank of ``personality prototypes''. At inference, we retrieve top-$k$ prototypes for a query post and perform a retrieve–reuse–revise–retain cycle: the model aggregates prototype evidence via prompt-based voting, revises when inconsistencies arise, and, upon correct prediction, retains the sample to continually enrich the prototype library. Across Kaggle and Pandora benchmarks, \textsc{ProtoMBTI} improves over baselines on both the four MBTI dichotomies and the full 16-type task, and exhibits robust cross-dataset generalization. Our results indicate that aligning the inference process with psychological prototype reasoning yields gains in accuracy, interpretability, and transfer for text-based personality modeling.

## item_id: m_3758

TITLE: Parameters vs. Context: Fine-Grained Control of Knowledge Reliance in Language Models

ABSTRACT: Retrieval-Augmented Generation (RAG) mitigates hallucinations in Large Language Models (LLMs) by integrating external knowledge. However, conflicts between parametric knowledge and retrieved context pose challenges, particularly when retrieved information is unreliable or the model's internal knowledge is outdated. In such cases, LLMs struggle to determine whether to rely more on their own parameters or the conflicted context. To address this, we propose CK-PLUG, a plug-and-play method for controlling LLMs' reliance on parametric and contextual knowledge. We introduce a novel knowledge consistency metric, Confidence Gain, which detects knowledge conflicts by measuring entropy shifts in token probability distributions after context insertion. CK-PLUG then enables fine-grained control over knowledge preference by adjusting the probability distribution of tokens with negative confidence gain through a single tuning parameter. Experiments demonstrate CK-PLUG's ability to significantly regulate knowledge reliance in counterfactual RAG scenarios while maintaining generation fluency and knowledge accuracy. For instance, on LLaMA3-8B, memory recall (MR) of RAG response can be adjusted within a broad range (9.9%-71.9%), compared to the baseline of 42.1%. Moreover, CK-PLUG supports adaptive control based on the model's confidence in both internal and external knowledge, achieving consistent performance improvements across various general RAG tasks. Our code is available at: https://anonymous.4open.science/r/CK-PLUG-Ano-8E62

## item_id: m_3759

TITLE: A Compositional Object-Based Approach to Learning Physical Dynamics

ABSTRACT: We present the Neural Physics Engine (NPE), a framework for learning simulators of intuitive physics that naturally generalize across variable object count and different scene configurations. We propose a factorization of a physical scene into composable object-based representations and a neural network architecture whose compositional structure factorizes object dynamics into pairwise interactions. Like a symbolic physics engine, the NPE is endowed with generic notions of objects and their interactions; realized as a neural network, it can be trained via stochastic gradient descent to adapt to specific object properties and dynamics of different worlds. We evaluate the efficacy of our approach on simple rigid body dynamics in two-dimensional worlds. By comparing to less structured architectures, we show that the NPE's compositional representation of the structure in physical interactions improves its ability to predict movement, generalize across variable object count and different scene configurations, and infer latent properties of objects such as mass.

## item_id: m_3760

TITLE: Learning Partially Observed PDE Dynamics with Neural Networks

ABSTRACT: Spatio-Temporal processes bear a central importance in many applied scientific fields. Generally, differential equations are used to describe these processes. In this work, we address the problem of learning spatio-temporal dynamics with neural networks when only partial information on the system's state is available. Taking inspiration from the dynamical system approach, we outline a general framework in which complex dynamics generated by families of differential equations  can be learned in a principled way. Two models are derived from this framework. We demonstrate how they can be applied in practice by considering the problem of forecasting fluid flows. We show how the underlying equations fit into our formalism and evaluate our method by comparing with standard baselines.

## item_id: m_3761

TITLE: Hyperband: Bandit-Based Configuration Evaluation for Hyperparameter Optimization

ABSTRACT: Performance of machine learning algorithms depends critically on identifying a good set of hyperparameters.  While recent approaches use Bayesian Optimization to adaptively select configurations, we focus on speeding up random search through adaptive resource allocation.  We present Hyperband,  a novel algorithm for hyperparameter optimization that is simple, flexible, and theoretically sound.  Hyperband is a principled early-stoppping method that adaptively allocates a predefined resource, e.g., iterations, data samples or number of features, to randomly sampled configurations.  We compare Hyperband with state-of-the-art Bayesian Optimization methods on several hyperparameter optimization problems.  We observe that Hyperband can provide over an order of magnitude speedups over competitors on a variety of neural network and kernel-based learning problems.  

## item_id: m_3762

TITLE: Detecting Out-of-distribution with Insights from Neural Collapse

ABSTRACT: Out-of-distribution (OOD) detection is essential for the safe deployment of AI. 
Particularly, OOD detectors should generalize effectively across diverse scenarios. 
To improve upon the generalizability of existing OOD detectors, we introduce a highly versatile OOD detector, called Neural Collapse inspired OOD detector (NC-OOD). 
We extend the prevalent observation that in-distribution (ID) features tend to form clusters, whereas OOD features are far away. 
Particularly, based on the recent observation, Neural Collapse, we further demonstrate that ID features tend to cluster in proximity to weight vectors. 
From our extended observation, we propose to detect OOD based on feature proximity to weight vectors. 
To further rule out OOD samples, we leverage the observation that OOD features tend to reside closer to the origin than ID features. Extensive experiments show that our approach enhances the generalizability of existing work and can consistently achieve state-of-the-art OOD detection performance across a wide range of OOD Benchmarks over different classification tasks, training losses, and model architectures.

## item_id: m_3763

TITLE: Augmenting Non-Collaborative Dialog Systems with Explicit Semantic and Strategic Dialog History

ABSTRACT: We study non-collaborative dialogs, where two agents have a conflict of interest but must strategically communicate to reach an agreement (e.g., negotiation). This setting poses new challenges for modeling dialog history because the dialog's outcome relies not only on the semantic intent, but also on tactics that convey the intent.  We propose to model both semantic and tactic history using finite state transducers (FSTs). Unlike RNN, FSTs can explicitly represent dialog history through all the states traversed, facilitating interpretability of dialog structure. We train FSTs on a set of strategies and tactics used in negotiation dialogs. The trained FSTs show plausible tactic structure and can be generalized to other non-collaborative domains (e.g., persuasion). We evaluate the FSTs by incorporating them in an automated negotiating system that attempts to sell products and a persuasion system that persuades people to donate to a charity. Experiments show that explicitly modeling both semantic and tactic history is an effective way to improve both dialog policy planning and generation performance. 

## item_id: m_3764

TITLE: Learning Discrete Weights Using the Local Reparameterization Trick

ABSTRACT: Recent breakthroughs in computer vision make use of large deep neural networks, utilizing the substantial speedup offered by GPUs. For applications running on limited hardware, however, high precision real-time processing can still be a challenge.  One approach to solving this problem is training networks with binary or ternary weights, thus removing the need to calculate multiplications and significantly reducing memory size. In this work, we introduce LR-nets (Local reparameterization networks), a new method for training neural networks with discrete weights using stochastic parameters. We show how a simple modification to the local reparameterization trick, previously used to train Gaussian distributed weights, enables the training of discrete weights. Using the proposed training we test both binary and ternary models on MNIST, CIFAR-10 and ImageNet benchmarks and reach state-of-the-art results on most experiments.

## item_id: m_3765

TITLE: Rethinking Cross-Lingual Gaps From A Statistical Viewpoint

ABSTRACT: Any piece of knowledge is usually expressed in one or a handful of natural languages on the web or in any large corpus. Large Language Models (LLMs) act as a bridge by acquiring knowledge from a source language and making it accessible when queried from target languages. Prior research has pointed to a cross-lingual gap, viz., a drop in accuracy when the knowledge is queried in a target language compared to when the query is in the source language. Existing research has rationalized divergence in latent representations in source and target languages as the source of cross-lingual gap. In this work, we take an alternative view and hypothesize that the variance of responses in the target language is the main cause of this gap. For the first time, we formalize the cross-lingual gap in terms of bias-variance decomposition. We present extensive experimental evidence which support proposed formulation and hypothesis. We then reinforce our hypothesis through multiple inference-time interventions that control the variance and reduce the cross-lingual performance gap.

## item_id: m_3766

TITLE: Rectified Factor Networks for Biclustering

ABSTRACT: Biclustering is evolving into one of the major tools for analyzing large datasets given as matrix of samples times features. Biclustering has several noteworthy applications and has been successfully applied in life sciences and e-commerce for drug design and recommender systems, respectively.

FABIA is one of the most successful biclustering methods and is used by companies like Bayer, Janssen, or Zalando. FABIA is a generative model that represents each bicluster by two sparse membership vectors: one for the samples and one for the features. However, FABIA is restricted to about 20 code units because of the high computational complexity of computing the posterior. Furthermore, code units are sometimes insufficiently decorrelated. Sample membership is difficult to determine because vectors do not have exact zero entries and can have both large positive and large negative values.

We propose to use the recently introduced unsupervised Deep Learning approach Rectified Factor Networks (RFNs) to overcome the drawbacks of existing biclustering methods. RFNs efficiently construct very sparse, non-linear, high-dimensional representations of the input via their posterior means. RFN learning is a generalized alternating minimization algorithm based on the posterior regularization method which enforces non-negative and normalized posterior means. Each code unit represents a bicluster, where samples for which the code unit is active belong to the bicluster and features that have activating weights to the code unit belong to the bicluster.

On 400 benchmark datasets with artificially implanted biclusters, RFN significantly outperformed 13 other biclustering competitors including FABIA. In biclustering experiments on three gene expression datasets with known clusters that were determined by separate measurements, RFN biclustering was two times significantly better than the other 13 methods and once on second place. On data of the 1000 Genomes Project, RFN could identify DNA segments which indicate, that interbreeding with other hominins starting already before ancestors of modern humans left Africa.

## item_id: m_3767

TITLE: Learning Neuron Non-Linearities with Kernel-Based Deep Neural Networks

ABSTRACT: The effectiveness of deep neural architectures has been widely supported in terms of both experimental and foundational principles. There is also clear evidence that the activation function (e.g. the rectiﬁer and the LSTM units) plays a crucial role in the complexity of learning. Based on this remark, this paper discusses an optimal selection of the neuron non-linearity in a functional framework that is inspired from classic regularization arguments. A representation theorem is given which indicates that the best activation function is a kernel expansion in the training set, that can be effectively approximated over an opportune set of points modeling 1-D clusters. The idea can be naturally extended to recurrent networks, where the expressiveness of kernel-based activation functions turns out to be a crucial ingredient to capture long-term dependencies. We give experimental evidence of this property by a set of challenging experiments, where we compare the results with neural architectures based on state of the art LSTM cells.

## item_id: m_3768

TITLE: Reverse engineering learned optimizers reveals known and novel mechanisms

ABSTRACT: Learned optimizers are algorithms that can themselves be trained to solve optimization problems. In contrast to baseline optimizers (such as momentum or Adam) that use simple update rules derived from intuitive principles, learned optimizers use flexible, high-dimensional, nonlinear parameterizations. Although this can lead to optimizers with better performance in certain settings, their inner workings remain a mystery. How is it that a learned optimizer is able to outperform a well tuned baseline? Has it learned a sophisticated method for combining existing optimization techniques, or is it implementing completely new behavior? In this work, we address these questions by visualizing and understanding learned optimizers. We study learned optimizers trained from scratch on three disparate tasks, and discovered that they have learned interpretable mechanisms, including: momentum, gradient clipping, schedules, and a new form of learning rate adaptation. Moreover, we show how the dynamics of trained learned optimizers enables these behaviors. Our results elucidate the previously murky understanding of what learned optimizers learn, and establishes tools for interpreting future learned optimizers.

## item_id: m_3769

TITLE: A Brain-Inspired Machine Learning Paradigm for Nature-Powered Equation Solving

ABSTRACT: Solving equations is fundamental to human understanding of the world. While modern machine learning methods are powerful equation solvers, their escalating complexity and extreme operational costs hinder sustainable development. In contrast, nature effortlessly solves complex equations through dynamical systems that instinctively evolve to low-energy states without explicit instructions. However, existing attempts to leverage dynamical systems are limited by low expressivity and a lack of training support. To this end, we propose DS-Solver, a nature-powered AI paradigm employing an expressive, self-trainable dynamical system capable of accurately solving a wide spectrum of equations with extraordinary efficiency. (1) We enhance system expressivity by enriching node dynamics with coupled real-valued and polarized shadow nodes, capturing complex interactions inherent in the real world. (2) We propose an on-device learning method that leverages intrinsic electrical signals as loss, enabling the dynamical system to instantly train itself at negligible cost. Experimental results across key equations from diverse domains demonstrate that DS-Solver achieves 42\% higher accuracy than current SOTA -- while offering orders-of-magnitude improvements in speed and energy efficiency over traditional neural network solutions on GPUs for both inference and training, showcasing its broader impact in overcoming persistent computational bottlenecks across various critical fields.

## item_id: m_3770

TITLE: Attacking Binarized Neural Networks

ABSTRACT: Neural networks with low-precision weights and activations offer compelling
efficiency advantages over their full-precision equivalents. The two most
frequently discussed benefits of quantization are reduced memory consumption,
and a faster forward pass when implemented with efficient bitwise
operations. We propose a third benefit of very low-precision neural networks:
improved robustness against some adversarial attacks, and in the worst case,
performance that is on par with full-precision models. We focus on the very
low-precision case where weights and activations are both quantized to $\pm$1,
and note that stochastically quantizing weights in just one layer can sharply
reduce the impact of iterative attacks. We observe that non-scaled binary neural
networks exhibit a similar effect to the original \emph{defensive distillation}
procedure that led to \emph{gradient masking}, and a false notion of security.
We address this by conducting both black-box and white-box experiments with
binary models that do not artificially mask gradients.

## item_id: m_3771

TITLE: SOAR: Second-Order Adversarial Regularization

ABSTRACT: Adversarial training is a common approach to improving the robustness of deep neural networks against adversarial examples. In this work, we propose a novel regularization approach as an alternative. To derive the regularizer, we formulate the adversarial robustness problem under the robust optimization framework and approximate the loss function using a second-order Taylor series expansion. Our proposed second-order adversarial regularizer (SOAR) is an upper bound based on the Taylor approximation of the inner-max in the robust optimization objective. We empirically show that the proposed method improves the robustness of networks against the $\ell_\infty$ and $\ell_2$ bounded perturbations on CIFAR-10 and SVHN.

## item_id: m_3772

TITLE: Modeling Dynamics of Biological Systems with Deep Generative Neural Networks

ABSTRACT: Biological data often contains measurements of dynamic entities such as cells or organisms in various states of progression. However, biological systems are notoriously difficult to describe analytically due to their many interacting components, and in many cases, the technical challenge of taking longitudinal measurements. This leads to difficulties in studying the features of the dynamics, for examples the drivers of the transition. To address this problem, we present a deep neural network framework we call Dynamics Modeling Network or DyMoN. DyMoN is a neural network framework trained as a deep generative Markov model whose next state is a probability distribution based on the current state. DyMoN is well-suited to the idiosyncrasies of biological data, including noise, sparsity, and the lack of longitudinal measurements in many types of systems. Thus, DyMoN can be trained using probability distributions derived from the data in any way, such as trajectories derived via dimensionality reduction methods, and does not require longitudinal measurements. We show the advantage of learning deep models over shallow models such as Kalman filters and hidden Markov models that do not learn representations of the data, both in terms of learning embeddings of the data and also in terms training efficiency, accuracy and ability to multitask. We perform three case studies of applying DyMoN to different types of biological systems and extracting features of the dynamics in each case by examining the learned model. 

## item_id: m_3773

TITLE: Neural Rendering Model: Joint Generation and Prediction for Semi-Supervised Learning

ABSTRACT: Unsupervised and semi-supervised learning are important problems that are especially challenging with complex data like natural images. Progress on these problems would accelerate if we had access to appropriate generative models under which to pose the associated inference tasks. Inspired by the success of Convolutional Neural Networks (CNNs) for supervised prediction in images, we design the Neural Rendering Model (NRM), a new hierarchical probabilistic generative model whose inference calculations correspond to those in a CNN. The NRM introduces a small set of latent variables at each level of the model and enforces dependencies among all the latent variables via a conjugate prior distribution. The conjugate prior yields a new regularizer for learning based on the paths rendered in the generative model for training CNNs–the Rendering Path Normalization (RPN). We demonstrate that this regularizer improves generalization both in theory and in practice. Likelihood estimation in the NRM yields the new Max-Min cross entropy training loss, which suggests a new deep network architecture–the Max- Min network–which exceeds or matches the state-of-art for semi-supervised and supervised learning on SVHN, CIFAR10, and CIFAR100.

## item_id: m_3774

TITLE: On the Out-of-Distribution Generalization of Self-Supervised Learning

ABSTRACT: In this paper, we focus on the out-of-distribution (OOD) generalization of self-supervised learning (SSL). By analyzing the mini-batch construction during SSL training phase, we first give one plausible explanation for SSL having OOD generalization. Then, from the perspective of data generation and causal inference, we analyze and conclude that SSL learns spurious correlations during the training process, which leads to a reduction in OOD generalization. To address this issue, we propose a post-intervention distribution (PID) grounded in the Structural Causal Model. PID offers a scenario where the relationships between variables are free from the influence of spurious correlations. Besides, we demonstrate that if each mini-batch during SSL training satisfies PID, the resulting SSL model can achieve optimal worst-case OOD performance. This motivates us to develop a batch sampling strategy that enforces PID constraints through the learning of a latent variable model. Through theoretical analysis, we demonstrate the identifiability of the latent variable model and validate the effectiveness of the proposed sampling strategy. Experiments conducted on various downstream OOD tasks demonstrate the effectiveness of the proposed sampling strategy.

## item_id: m_3775

TITLE: Statistical Inference for Deep Learning via Stochastic Modeling

ABSTRACT: Deep learning has revolutionized big data analysis in modern data science, however, how to make statistical inference for deep neural networks remains largely unclear. To this end, we explore a stochastic 
variant of the deep neural network known as the stochastic neural network (StoNet). Firstly, we show that the StoNet falls into the framework of statistical modeling. It not only enables us to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, but also provides with us a platform for transferring the theory and methods developed for linear models to the realm of deep learning. Specifically, we show how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models; establish that the sparse StoNet is consistent in network structure selection; and provides a recursive method to quantify the prediction uncertainty for the Stonet. Furthermore, we extend this result to the DNN by its asymptotic equivalence with the StoNet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. Additionally, we propose to remodel the last hidden layer output and the target output of a well-trained DNN model using a StoNet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet. The proposed method has been compared with conformal inference on extensive examples, and numerical results suggests its superiority.

## item_id: m_3776

TITLE: Attentive Neural Processes

ABSTRACT: Neural Processes (NPs) (Garnelo et al., 2018) approach regression by learning to map a context set of observed input-output pairs to a distribution over regression functions. Each function models the distribution of the output given an input, conditioned on the context. NPs have the benefit of fitting observed data efficiently with linear complexity in the number of context input-output pairs, and can learn a wide family of conditional distributions; they learn predictive distributions conditioned on context sets of arbitrary size. Nonetheless, we show that NPs suffer a fundamental drawback of underfitting, giving inaccurate predictions at the inputs of the observed data they condition on. We address this issue by incorporating attention into NPs, allowing each input location to attend to the relevant context points for the prediction. We show that this greatly improves the accuracy of predictions, results in noticeably faster training, and expands the range of functions that can be modelled. 

## item_id: m_3777

TITLE: Corpus Based Amharic Sentiment Lexicon Generation

ABSTRACT: Sentiment classification is an active research area with several applications including analysis of political opinions, classifying comments, movie reviews, news reviews and product reviews. To employ rule based sentiment classification, we require sentiment lexicons. However, manual construction of sentiment lexicon is time consuming and costly for resource-limited languages. To bypass manual development time and costs, we tried to build Amharic Sentiment Lexicons relying on corpus based approach. The intention of this approach is to handle sentiment terms specific to Amharic language from Amharic Corpus. Small set of seed terms are manually prepared from three parts of speech such as noun, adjective and verb. We developed algorithms for constructing Amharic sentiment lexicons automatically from Amharic news corpus. Corpus based approach is proposed relying on the word co-occurrence distributional embedding including frequency based embedding (i.e. Positive Point-wise Mutual Information PPMI). First we build word-context unigram frequency count matrix and transform it to point-wise mutual Information matrix. Using this matrix, we computed the cosine distance of mean vector of seed lists and each word in the corpus vocabulary. Based on the threshold value, the top closest words to the mean vector of seed list are added to the lexicon. Then the mean vector of the new sentiment seed list is updated and process is repeated until we get sufficient terms in the lexicon. Using PPMI with threshold value of 100 and 200, we got corpus based Amharic Sentiment lexicons of size 1811 and 3794 respectively by expanding 519 seeds. Finally, the lexicon generated in corpus based approach is evaluated.


## item_id: m_3778

TITLE: AdvLoRA: Adversarial Low-Rank Adaptation of Vision-Language Models

ABSTRACT: Vision-Language Models (VLMs) are a significant technique for Artificial General Intelligence (AGI). With the fast growth of AGI, the security problem become one of the most important challenges for VLMs. In this paper, through extensive experiments, we demonstrate the vulnerability of the conventional adaptation methods for VLMs, which may bring significant security risks. In addition, as the size of the VLMs increases, performing conventional adversarial adaptation techniques on VLMs results in high computational costs. To solve these problems, we propose a parameter-efficient \underline{Adv}ersarial adaptation method named \underline{AdvLoRA} by \underline{Lo}w-\underline{R}ank \underline{A}daptation. At first, we investigate and reveal the intrinsic low-rank property during the adversarial adaptation for VLMs. Different from LoRA, we improve the efficiency and robustness of adversarial adaptation by designing a novel reparameterizing method based on parameter clustering and parameter alignment. In addition, an adaptive parameter update strategy is proposed to further improve the robustness. By these settings, our proposed AdvLoRA alleviates the model security and high resource waste problems. Extensive experiments demonstrate the effectiveness and efficiency of the AdvLoRA.

## item_id: m_3779

TITLE: OwLore: Outlier-weighed Layerwise Sampled Low-Rank Projection for Memory-Efficient LLM Fine-tuning

ABSTRACT: The rapid advancements in Large Language Models (LLMs) have revolutionized various natural language processing tasks. However, the substantial size of LLMs presents significant challenges in training or fine-tuning. While parameter-efficient approaches such as low-rank adaptation (LoRA) have gained popularity, they often compromise performance compared to full-rank fine-tuning. In this paper, we propose Outlier-weighed Layerwise Sampled Low-Rank Projection (OwLore), a new memory-efficient fine-tuning approach, inspired by the layerwise outlier distribution of LLMs. Unlike LoRA, which adds extra adapters to all layers, OwLore strategically assigns higher sampling probabilities to layers with more outliers, selectively sampling only a few layers and fine-tuning their pre-trained weights. To further increase the number of fine-tuned layers without a proportional rise in memory costs, we incorporate gradient low-rank projection, further boosting the approach’s performance. Our extensive experiments across various architectures, including LLaMa2, LLaMa3, and Mistral, demonstrate that OwLore consistently outperforms baseline approaches, including full fine-tuning. Specifically, it achieves up to a 1.1% average accuracy gain on the Commonsense Reasoning benchmark, a 3.0% improvement on MMLU, and a notable 10% boost on MT-Bench, while being more memory efficient. OwLore allows us to fine-tune LLaMa2-7B with only 21GB of memory. Our code is submitted.

## item_id: m_3780

TITLE: EigenLoRAx: Efficient Low Rank Adaptation Using Recycled Principal Subspaces

ABSTRACT: The rapid growth of large models has raised concerns about their environmental impact and equity in accessibility due to significant computational costs. Low-Rank Adapters (LoRA) offer a lightweight solution for finetuning large models, resulting in an abundance of publicly available adapters tailored to diverse domains. We ask: Can these pretrained adapters be leveraged to further streamline adaptation to new tasks while addressing these challenges? We introduce EigenLoRAx, a parameter-efficient finetuning method that recycles existing adapters to create a principal subspace aligned with their shared domain knowledge which can be further augmented with orthogonal basis vectors in low-resource scenarios. This enables rapid adaptation to new tasks by learning only lightweight coefficients on the principal components of the subspace, eliminating the need to finetune entire adapters. EigenLoRAx requires significantly fewer parameters and memory, improving efficiency for both training and inference. Our method demonstrates strong performance across diverse domains and tasks, offering a scalable solution for edge-based applications and equitable deployment of large models in resource-constrained environments.

## item_id: m_3781

TITLE: Self-supervised Continual Learning based on Batch-mode Novelty Detection

ABSTRACT: Continual learning (CL) plays a key role in dynamic systems in order to adapt to new tasks, while preserving previous knowledge. Most existing CL approaches focus on learning new knowledge in a supervised manner, while leaving the data gathering phase to the novelty detection (ND) algorithm. Such presumption limits the practical usage where new data needs to be quickly learned without being labeled. In this paper, we propose a unified approach of CL and ND, in which each new class of the out-of-distribution (ODD) data is first detected and then added to previous knowledge. Our method has three unique features: (1) a unified framework seamlessly tackling both ND and CL problems; (2) a self-supervised method for model adaptation, without the requirement of new data annotation; (3) batch-mode data feeding that maximizes the separation of new knowledge vs. previous learning, which in turn enables high accuracy in continual learning. By learning one class at each step, the new method achieves robust continual learning and consistently outperforms state-of-the-art CL methods in the single-head evaluation on MNIST, CIFAR-10, CIFAR-100 and TinyImageNet datasets.

## item_id: m_3782

TITLE: A Quality-Diversity Controllable GAN for Text Generation

ABSTRACT: Text generation is a critical and difficult natural language processing task. Maximum likelihood estimate (MLE) based models have been arguably suffered from exposure bias in the inference stage and thus varieties of language generative adversarial networks (GANs) bypassing this problem have emerged. However, recent study has demonstrated that MLE models can constantly outperform GANs models over quality-diversity space under several metrics. In this paper, we propose a quality-diversity controllable language GAN.

## item_id: m_3783

TITLE: ATTENTION INCORPORATE NETWORK: A NETWORK CAN ADAPT VARIOUS DATA SIZE

ABSTRACT: In traditional neural networks for image processing, the inputs of the neural networks should be the same size such as 224×224×3. But how can we train the neural net model with different input size? A common way to do is image deformation which accompany a problem of information loss (e.g. image crop or wrap). In this paper we propose a new network structure called Attention Incorporate Network(AIN). It solve the problem of different size of input images and extract the key features of the inputs by attention mechanism, pay different attention depends on the importance of the features not rely on the data size. Experimentally, AIN achieve a higher accuracy, better convergence comparing to the same size of other network structure.

## item_id: m_3784

TITLE: Show or Tell? Effectively prompting Vision-Language Models for semantic segmentation

ABSTRACT: Large Vision-Language Models (VLMs) are increasingly being regarded as foundation models that can be instructed to solve diverse tasks by prompting, without task-specific training.
We examine the seemingly obvious question: \emph{how to effectively prompt VLMs for semantic segmentation}.
To that end, we systematically evaluate the segmentation performance of several recent models guided by either text or visual prompts on the diverse MESS dataset collection.
We introduce a scalable prompting scheme, \emph{few-shot prompted semantic segmentation}, inspired by open-vocabulary segmentation and few-shot learning.
It turns out that even the most advanced VLMs lag far behind specialist models trained for a specific segmentation task, by about 30\% on average on the Intersection-over-Union metric.
Moreover, we find that text prompts and visual prompts are complementary: each one of the two modes fails on many examples that the other one can solve.
Our analysis suggests that being able to anticipate the most effective prompt modality can lead to a 11\% improvement in performance.
Motivated by our findings, we propose PromptMatcher, a remarkably simple baseline that combines both text and visual prompts, achieving state-of-the-art results for training-free semantic segmentation.

## item_id: m_3785

TITLE: Hierarchical Image Transformer Based on the Segment Anything Model

ABSTRACT: We propose a hierarchical image transformer generation Model based on Segment Anything Model (SAM), and explore a new research paradigm of customized large-scale model for transformer image generation. samformer applies a fine-tuning strategy based on Low rank (LoRA) to SAM image encoders, Together with self-attention, hierarchical vae encoders, mask transformer decoders, and predictive head transformer, it is fine-tuned on Imagenet-like image datasets. SAM is chosen based on its semantic mask for the image level. Specifically, in the first stage, we use SAM-based segmentation features for hierarchical encoding using attention and decoding through reconstruction losses, and the first stage algorithm achieves better performance in both vector quantization and image generation. The second phase of the mask transformer predicts masks by focusing on markers in all directions at each layer in parallel. We also observed that the warm-up fine-tuning strategy resulted in samformer successfully converging and reducing losses. Unlike SAM, samformer can perform both unconditional and class-conditional image generation tasks. Our trained B-size samformer model achieves fid scores of 3.58 and 4.28 for unconditional image generation on ffhq data set and class conditional image generation on imagenet data set respectively, which is comparable to the most advanced methods and reduces the pre-training time of large models by 3 times; The M-sized pre-trained model also achieves results that are competitive with the most advanced methods. We conducted a large number of experiments to verify the effectiveness of our design. In addition, we demonstrate the effectiveness of the proposed method in multiple generation tasks, such as unconditional image generation, class conditional image generation, text conditional image generation, etc. Because samformer updates only a small number of SAM parameters, its training costs are quite insignificant compared to other large generation models.

## item_id: m_3786

TITLE: MARNET: Backdoor Attacks against Value-Decomposition Multi-Agent Reinforcement Learning

ABSTRACT: Recent works have revealed that backdoor attacks against Deep Reinforcement Learning (DRL) could lead to abnormal action selection of the agent, which may result in failure or even catastrophe in crucial decision processes. However, existing attacks only consider single-agent RL systems, in which the only agent can observe the global state and have full control of the decision process. In this paper, we explore a new backdoor attack paradigm in cooperative multi-agent reinforcement learning (CMARL) scenarios, where a group of agents coordinate with each other to achieve a common goal, while each agent can only observe the local state, e.g., StarCraft II (Vinyals et al. (2017)). In the proposed MARNet attack framework, we carefully design a pipeline of trigger design, action poisoning and reward hacking modules to accommodate the cooperative multi-agent momentums. In particular, as only a subset of agents can observe the triggers in their local observations, we maneuver their actions to the worst actions suggested by an expert policy model. Since the global reward in CMARL is aggregated by individual rewards from all agents, we propose to modify the reward in a way that boosts the bad actions of poisoned agents (agents who observe the triggers) but mitigates the influence on non-poisoned agents. We conduct extensive experiments on two classical MARL algorithms VDN (Sunehag et al. (2018)) and QMIX (Rashid et al. (2018)), in two popular CMARL games Predator Prey (Boehmer et al. (2020)) and SMAC (Samvelyan et al. (2019)). The results show that MARNet outperforms baselines extended from single-agent DRL backdoor attacks TrojDRL (Kiourti et al. (2020)) and Multitasking learning (Ashcraft & Karra (2021)) by reducing the utility under attack by as much as 100%. We apply fine-tuning as a defense against MARNet, and demonstrate that fine-tuning cannot entirely eliminate the effect of the attack.

## item_id: m_3787

TITLE: Learning Antidote Data to Individual Unfairness

ABSTRACT: Fairness is an essential factor for machine learning systems deployed in high-stake applications. Among all fairness notions, individual fairness, following a consensus that `similar individuals should be treated similarly,' is a vital notion to guarantee fair treatment for individual cases. Previous methods typically characterize individual fairness as a prediction-invariant problem when perturbing sensitive attributes, and solve it by adopting the Distributionally Robust Optimization (DRO) paradigm. However, adversarial perturbations along a direction covering sensitive information do not consider the inherent feature correlations or innate data constraints, and thus mislead the model to optimize at off-manifold and unrealistic samples. In light of this, we propose a method to learn and generate antidote data that approximately follows the data distribution to remedy individual unfairness. These on-manifold antidote data can be used through a generic optimization procedure with original training data, resulting in a pure pre-processing approach to individual unfairness, or can also fit well with the in-processing DRO paradigm. Through extensive experiments, we demonstrate our antidote data resists individual unfairness at a minimal or zero cost to the model's predictive utility.

## item_id: m_3788

TITLE: Confidence Scoring Using Whitebox Meta-models with Linear Classifier Probes

ABSTRACT: We propose a confidence scoring mechanism for multi-layer neural networks based on a paradigm of a base model and a meta-model. The confidence score is learned by the meta-model using features derived from the base model – a deep neural network considered a whitebox. As features, we investigate linear classifier probes inserted between the various layers of the base model and trained using each layer’s intermediate activations. Experiments show that this approach outperforms various baselines in a filtering task, i.e., task of rejecting samples with low confidence. Experimental results are presented using CIFAR-10 and CIFAR-100 dataset with and without added noise exploring various aspects of the method.

## item_id: m_3789

TITLE: Abstract Visual Reasoning by Self-supervised Contrastive Learning

ABSTRACT: Neuro-symbolic models of artificial intelligence (AI) have been recently developed to perform tasks involving abstract visual reasoning that is a hallmark of human intelligence but remains challenging for deep neural network methods. However, most of the current neuro-symbolic models also rely on supervised learning and auxiliary annotations, different from human cognitive processes that are much dependent on the general cognitive abilities of entity and rule recognitions, rather than learning how to solve the specific tasks from examples. In this work, we propose a neuro-symbolic model by self-supervised contrastive learning (NS-SSCL) with unique and invariant representations of entities and rules in the perception and reasoning modules, respectively, to solve Raven’s Progressive Matrices (RPMs) and its variant, a typical type of visual reasoning task used to test human intelligence. The perception module parses each object into invariant representations of attributes. The reasoning module grounds the representations of object attributes to form the latent rule representations also through SSCL. Further, the relationships between the neural representations of object attributes and symbols used for rule reasoning are coherently mapped. Finally, the scene generation engine aggregates all attribute and rule representation distributions to produce a probabilistic representation of the target. NS-SSCL obtains state-of-the-art performance in unsupervised models to solve the RAVEN and V-PROM benchmarks, even better than most of the supervised models. The success of the proposed model suggests that construction of general cognitive abilities like humans may render the AI algorithms to solve complex tasks involving higher-level cognition such as abstract reasoning in a human-like manner.

## item_id: m_3790

TITLE: Deep Reinforcement Learning with Causality-based Intrinsic Reward

ABSTRACT: Reinforcement Learning (RL) has shown great potential to deal with sequential decision-making problems. However, most RL algorithms do not explicitly consider the relations between entities in the environment. This makes the policy learning suffer from the problems of efficiency, effectivity and interpretability.  In this paper, we propose a novel deep reinforcement learning algorithm, which firstly learns the causal structure of the environment and then leverages the learned causal information to assist policy learning. The proposed algorithm learns a graph to encode the environmental structure by calculating Average Causal Effect (ACE) between different categories of entities, and an intrinsic reward is given to encourage the agent to interact more with entities belonging to top-ranked categories, which significantly boosts policy learning.  Several experiments are conducted on a number of simulation environments to demonstrate the effectiveness and better interpretability of our proposed method.

## item_id: m_3791

TITLE: PaAno: Patch-Based Representation Learning for Time-Series Anomaly Detection

ABSTRACT: Although recent studies on time-series anomaly detection have increasingly adopted ever-larger neural network architectures such as transformers and foundation models, they incur high computational costs and memory usage, making them impractical for real-time and resource-constrained scenarios. Moreover, they often fail to demonstrate significant performance gains over simpler methods under rigorous evaluation protocols. In this study, we propose Patch-based representation learning for time-series Anomaly detection (PaAno), a lightweight yet effective method for fast and efficient time-series anomaly detection. PaAno extracts short temporal patches from time-series training data and uses a 1D convolutional neural network to embed each patch into a vector representation. The model is trained using a combination of triplet loss and pretext loss to ensure the embeddings capture informative temporal patterns from input patches. During inference, the anomaly score at each time step is computed by comparing the embeddings of its surrounding patches to those of normal patches extracted from the training time-series. Evaluated on the TSB-AD benchmark, PaAno achieved state-of-the-art performance, significantly outperforming existing methods, including those based on heavy architectures, on both univariate and multivariate time-series anomaly detection across various range-wise and point-wise performance measures.

## item_id: m_3792

TITLE: Addressing Label Shift in Distributed Learning via Entropy Regularization​

ABSTRACT: We address the challenge of minimizing "true risk" in multi-node distributed learning.\footnote{We use the term node to refer to a client, FPGA, APU, CPU, GPU, or worker.} These systems are frequently exposed to both inter-node and intra-node "label shifts", which present a critical obstacle to effectively optimizing model performance while ensuring that data remains confined to each node.
To tackle this, we propose the Versatile Robust Label Shift (VRLS) method, which enhances the maximum likelihood estimation of the test-to-train label importance ratio. VRLS incorporates Shannon entropy-based regularization and adjusts the importance ratio during training  to better handle label shifts at the test time.
In multi-node learning environments, VRLS further extends its capabilities by learning and adapting importance ratios across nodes, effectively mitigating label shifts and improving overall model performance. Experiments conducted on MNIST, Fashion MNIST, and CIFAR-10 demonstrate the effectiveness of VRLS, outperforming baselines by up to 20\% in imbalanced settings. These results highlight the significant improvements VRLS offers in addressing label shifts. Our theoretical analysis further supports this by establishing high-probability bounds on estimation errors.

## item_id: m_3793

TITLE: Efficient Representation of Low-Dimensional Manifolds using Deep Networks

ABSTRACT: We consider the ability of deep neural networks to represent data that lies near a low-dimensional manifold in a high-dimensional space.  We show that deep networks can efficiently extract the intrinsic, low-dimensional coordinates of such data.  Specifically we show that the first two layers of a deep network can exactly embed points lying on a monotonic chain, a special type of piecewise linear manifold, mapping them to a low-dimensional Euclidean space.  Remarkably, the network can do this using an almost optimal number of parameters. We also show that this network projects nearby points onto the manifold and then embeds them with little error. Experiments demonstrate that training with stochastic gradient descent can indeed find efficient representations similar to the one presented in this paper.

## item_id: m_3794

TITLE: VECoDeR - Variational Embeddings for Community Detection and Node Representation

ABSTRACT: In this paper, we study how to simultaneously learn two highly correlated tasks of graph analysis, i.e., community detection and node representation learning. We propose an efficient generative model called VECoDeR for jointly learning Variational Embeddings for COmmunity DEtection and node Representation. VECoDeR assumes that every node can be a member of one or more communities. The node embeddings are learned in such a way that connected nodes are not only ``closer" to each other but also share similar community assignments. A joint learning framework leverages community-aware node embeddings for better community detection. We demonstrate on several graph datasets that VECoDeR effectively outperforms many competitive baselines on all three tasks i.e. node classification, overlapping community detection and non-overlapping community detection. We also show that VECoDeR is computationally efficient and has quite robust performance with varying hyperparameters.

## item_id: m_3795

TITLE: Interpolating Compressed Parameter Subspaces

ABSTRACT: Though distribution shifts have caused growing concern for machine learning scalability, solutions tend to specialize towards a specific type of distribution shift. Methods for label shift may not succeed against domain or task shift, and vice versa. We learn that constructing a Compressed Parameter Subspaces (CPS), a geometric structure representing distance-regularized parameters mapped to a set of train-time distributions, can maximize average accuracy over a broad range of distribution shifts concurrently. We show sampling parameters within a CPS can mitigate backdoor, adversarial, permutation, stylization and rotation perturbations. We also show training a hypernetwork representing a CPS can adapt to seen tasks as well as unseen interpolated tasks.

## item_id: m_3796

TITLE: Deep unsupervised feature selection

ABSTRACT: Unsupervised feature selection involves finding a small number of highly informative features, in the absence of a specific supervised learning task. Selecting a small number of features is an important problem in many scientific domains with high-dimensional observations. Here, we propose the restricted autoencoder (RAE) framework for selecting features that can accurately reconstruct the rest of the features. We justify our approach through a novel proof that the reconstruction ability of a set of features bounds its performance in downstream supervised learning tasks. Based on this theory, we present a learning algorithm for RAEs that iteratively eliminates features using learned per-feature corruption rates. We apply the RAE framework to two high-dimensional biological datasets—single cell RNA sequencing and microarray gene expression data, which pose important problems in cell biology and precision medicine—and demonstrate that RAEs outperform nine baseline methods, often by a large margin.

## item_id: m_3797

TITLE: CycleAug: Cycle-Consistent Visual Augmentation for Large Multimodal Models

ABSTRACT: Training multimodal large language models (MLLMs) requires high-quality image-question-answer (IQA) triplets, which are labour-intensive to curate and often lack diversity. We propose a novel data augmentation framework for visual instruction tuning that efficiently generates diverse synthetic images based on existing IQA anchor triplets. To ensure that the generated images align with their associated QA pairs, we propose CycleAug --- cycle-consistency visual augmentation which involves synthesizing images from text (text $\rightarrow$ image) and then performing a verification step to confirm that the answers derived from the synthetic images match the original answers (image $\rightarrow$ text), ensuring consistency across images, questions, and answers. By combining synthetic images with high-quality real data in the training phase, we demonstrate these synthetic triplets act as an implicit regularization, which improves the robustness of MLLMs and enables analogical reasoning. Extensive experiments show that our approach improves model performance on multiple visual question-answering benchmarks without additional real-world data. This work highlights the potential of leveraging visual foundational models to enhance visual instruction tuning in MLLMs.

## item_id: m_3798

TITLE: Prototypical Networks for Few-shot Learning

ABSTRACT: A recent approach to few-shot classification called matching networks has demonstrated the benefits of coupling metric learning with a training procedure that mimics test. This approach relies on a complicated fine-tuning procedure and an attention scheme that forms a distribution over all points in the support set, scaling poorly with its size. We propose a more streamlined approach, prototypical networks, that learns a metric space in which few-shot classification can be performed by computing Euclidean distances to prototype representations of each class, rather than individual points. Our method is competitive with state-of-the-art one-shot classification approaches while being much simpler and more scalable with the size of the support set. We empirically demonstrate the performance of our approach on the Omniglot and mini-ImageNet datasets. We further demonstrate that a similar idea can be used for zero-shot learning, where each class is described by a set of attributes, and achieve state-of-the-art results on the Caltech UCSD bird dataset.

## item_id: m_3799

TITLE: Vanishing Privacy: Fast Gradient Leakage Threat to Federated Learning

ABSTRACT: In the federated learning (FL) framework, clients participate in collaborative learning tasks under the coordination of a central server. Clients train local submodels using their own data and share gradients with the server, which aggregates the gradients to achieve privacy protection. However, recent research has revealed that gradient inversion attacks (GIAs) can leak private data from the shared gradients. 
Prior work has only demonstrated the feasibility of recovering input data from gradients under highly restrictive conditions, such as when dealing with high-resolution face datasets, where GIAs often struggle to initiate attacks effectively, and on object datasets like Imagenet, where they encounter limitations, primarily manifested in their ability to handle only small batch sizes and high time costs.
As a result, we believe that implementing GIAs on high-resolution face datasets with large batch sizes is a challenging task. In this work, we introduce \textbf{F}ast \textbf{G}radient \textbf{L}eakage (FGL), which enables rapid image recovery across various network models on complex datasets, including the CelebA face dataset (1000 classes, 224$\times $224 px).
We also introduced StyleGAN as prior knowledge for images and achieved FGL with a batch size of 60 in experiments (constrained by experimental hardware).
We further propose a joint gradient matching loss, where multiple distinct matching losses collectively contribute to clarifying the attack direction and enhancing the efficiency of the optimization process.
Extensive experimentation validates the feasibility of our approach. We anticipate that our proposed method can serve as a valuable tool to advance the development of privacy defense techniques.

## item_id: m_3800

TITLE: One Objective for All Models --- Self-supervised Learning for Topic Models

ABSTRACT: Self-supervised learning has significantly improved the performance of many NLP tasks. In this paper, we highlight a key advantage of self-supervised learning - when applied to data generated by topic models, self-supervised learning can be oblivious to the specific model, and hence is less susceptible to model mis-specification. In particular, we prove that commonly used self-supervised objectives based on reconstruction or contrastive samples can both recover useful posterior information for general topic models. Empirically, we show that the same objectives can perform competitively against posterior inference using the correct model, while outperforming posterior inference using mis-specified model.
