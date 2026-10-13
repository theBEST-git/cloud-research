# Batch 07 — 100 items

## item_id: m_0601

TITLE: Inverting Data Transformations via Diffusion Sampling

ABSTRACT: We study the problem of transformation inversion on general Lie groups: a datum is transformed by an unknown group element, and the goal is to recover an inverse transformation that maps it back to the original data distribution. Such unknown transformations arise widely in machine learning and scientific modeling, where they can significantly distort observations. As a key application, we focus on test-time equivariance, where the objective is to improve the robustness of pretrained neural networks to input transformations at inference time and without any (re)training. We take a probabilistic view and model the posterior over transformations as a Boltzmann distribution defined by an energy function in data space. To sample from this posterior, we introduce a diffusion process on Lie groups that keeps all updates on-manifold and only requires computations in the associated Lie algebra. Our method, Transformation-Inverting Energy Diffusion (TIED), relies on a new trivialized target-score identity that enables efficient score-based sampling of the transformation posterior. TIED naturally handles curved group geometries and rugged, multimodal energy landscapes, and it applies to a broad class of Lie groups and nonlinear actions without assuming compactness or a bi-invariant metric. Experiments on image homographies and PDE symmetries demonstrate that TIED can restore transformed inputs to the training distribution at test time, showing improved performance over strong canonicalization and sampling baselines.

## item_id: m_0602

TITLE: MutexMatch: Semi-supervised Learning with Mutex-based Consistency Regularization

ABSTRACT: The core issue in semi-supervised learning (SSL) lies in how to effectively leverage unlabeled data, whereas most existing methods usually concentrate on the utilization of high-confidence samples yet seldom fully explore the usage of low-confidence samples. Early SSL methods mostly require low-confidence samples to optimize the same loss function as high-confidence samples, but this setting might largely challenge the low-confidence samples especially at the early training stage. In this paper, we aim to utilize low-confidence samples in a novel way, which is realized by our proposed mutex-based consistency regularization, namely MutexMatch. To be specific, the high-confidence samples are required to exactly predict "What it is" by conventional True-Positive Classifier, while the low-confidence samples, for a much simpler goal, are employed to predict "What it is not" by True-Negative Classifier with ease. In this way, we not only mitigate the pseudo-labeling errors but also make full use of the low-confidence unlabeled data in the training stage. The proposed MutexMatch achieves superior performance on multiple benchmark datasets, i.e., CIFAR-10, CIFAR-100, SVHN, and STL-10. Particularly, our method shows further superiority under few quantities of labeled data, e.g., 91.77% accuracy with only 20 labeled data on CIFAR-10.

## item_id: m_0603

TITLE: Deep Active Learning for Named Entity Recognition

ABSTRACT: Deep learning has yielded state-of-the-art performance on many natural language processing tasks including named entity recognition (NER). However, this typically requires large amounts of labeled data. In this work, we demonstrate that the amount of labeled training data can be drastically reduced when deep learning is combined with active learning. While active learning is sample-efficient, it can be computationally expensive since it requires iterative retraining. To speed this up, we introduce a lightweight architecture for NER, viz., the CNN-CNN-LSTM model consisting of convolutional character and word encoders and a  long short term memory (LSTM) tag decoder. The model achieves nearly state-of-the-art performance on standard datasets for the task while being computationally much more efficient than best performing models. We carry out incremental active learning, during the training process, and are able to nearly match state-of-the-art performance with just 25\% of the original training data.

## item_id: m_0604

TITLE: Better Generalization by Efficient Trust Region Method

ABSTRACT: In this paper, we develop a trust region method for training deep neural networks. At each iteration, trust region method computes the search direction by solving a non-convex subproblem. Solving this subproblem is non-trivial---existing methods have only sub-linear convergence rate. In the first part, we show that a simple modification of gradient descent algorithm can converge to a global minimizer of the subproblem with an asymptotic linear convergence rate. Moreover, our method only requires Hessian-vector products, which can be computed efficiently by back-propagation in neural networks. In the second part, we apply our algorithm to train large-scale convolutional neural networks, such as VGG and MobileNets. Although trust region method is about 3 times slower than SGD in terms of running time, we observe it finds a model that has lower generalization (test) error than SGD, and this difference is even more significant in large batch training. 
We conduct several interesting experiments to support our conjecture that the trust region method can avoid sharp local minimas.

## item_id: m_0605

TITLE: Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models

ABSTRACT: Large language models (LLMs) excel at complex reasoning tasks such as mathematics and coding, yet they frequently struggle with simple interactive tasks that young children perform effortlessly. This discrepancy highlights a critical gap between declarative knowledge (knowing about something) and procedural knowledge (knowing how to do something).
Although traditional reinforcement learning (RL) agents can acquire procedural knowledge through environmental interaction, they often operate as black boxes and require substantial training data.
In contrast, LLMs possess extensive world knowledge and reasoning capabilities, but are unable to effectively convert this static knowledge into dynamic decision-making in interactive settings.
To address this challenge, we propose Think-In Games (TiG), a novel framework that empowers LLMs to develop procedural understanding through direct interaction with game environments, while retaining their inherent reasoning and explanatory abilities. Specifically, TiG reformulates RL-based decision-making as a language modeling task: LLMs generate language-guided policies, which are refined iteratively through online reinforcement learning based on environmental feedback.
Our experimental results show that TiG successfully bridges the gap between declarative and procedural knowledge, achieving competitive performance with dramatically lower data demands compared to conventional RL methods. Moreover, TiG provides step-by-step natural language explanations for its decisions, greatly improving transparency and interpretability in complex interactive tasks.

## item_id: m_0606

TITLE: GraphAF: a Flow-based Autoregressive Model for Molecular Graph Generation

ABSTRACT: Molecular graph generation is a fundamental problem for drug discovery and has been attracting growing attention. The problem is challenging since it requires not only generating chemically valid molecular structures but also optimizing their chemical properties in the meantime. Inspired by the recent progress in deep generative models, in this paper we propose a flow-based autoregressive model for graph generation called GraphAF. GraphAF combines the advantages of both autoregressive and flow-based approaches and enjoys: (1) high model flexibility for data density estimation; (2) efficient parallel computation for training; (3) an iterative sampling process, which allows leveraging chemical domain knowledge for valency checking. Experimental results show that GraphAF is able to generate 68\% chemically valid molecules even without chemical knowledge rules and 100\% valid molecules with chemical rules. The training process of GraphAF is two times faster than the existing state-of-the-art approach GCPN. After fine-tuning the model for goal-directed property optimization with reinforcement learning, GraphAF achieves state-of-the-art performance on both chemical property optimization and constrained property optimization. 

## item_id: m_0607

TITLE: Contrastive Self-Supervised Learning of Global-Local Audio-Visual Representations

ABSTRACT: Contrastive self-supervised learning has delivered impressive results in many audio-visual recognition tasks. However, existing approaches optimize for learning either global representations useful for high-level understanding tasks such as classification, or local representations useful for tasks such as audio-visual source localization and separation. While they produce satisfactory results in their intended downstream scenarios, they often fail to generalize to tasks that they were not originally designed for. In this work, we propose a versatile self-supervised approach to learn audio-visual representations that can generalize to both the tasks which require global semantic information (e.g., classification) and the tasks that require fine-grained spatio-temporal information (e.g. localization). We achieve this by optimizing two cross-modal contrastive objectives that together encourage our model to learn discriminative global-local visual information given audio signals. To show that our approach learns generalizable video representations, we evaluate it on various downstream scenarios including action/sound classification, lip reading, deepfake detection, and sound source localization. 

## item_id: m_0608

TITLE: Self-Paced Augmentations (SPAug) for Improving Model Robustness

ABSTRACT: Augmentations are crucial components in modern computer vision. While various augmentation techniques have been devised to enhance model generalization and robustness, they are conventionally applied uniformly to all dataset samples during training. In this paper, we introduce ``Self-Paced Augmentations (SPAug),'' a novel approach that dynamically adjusts the augmentation intensity for each sample based on its training statistics. Our approach incurs little to no computational overhead and can be effortlessly integrated with existing augmentation policies with just a few lines of code. We integrate our self-paced augmentations into established uniform augmentation policies such as AugMix, RandomAugment, and AutoAugment. Our experiments reveal sizeable improvements, with about 1\% enhancement on CIFAR10-C and CIFAR100-C datasets and a 1.81\% improvement on ImageNet-C over AugMix, all while maintaining the same natural accuracy. Furthermore, within the context of augmentations designed to enhance model generalization, we demonstrate a 0.4\% improvement over AutoAugment on CIFAR100, coupled with a 0.7\% enhancement in model robustness.

## item_id: m_0609

TITLE: Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs

ABSTRACT: Currently many benchmarks have been proposed to evaluate the perception ability of the Large Vision-Language Models (LVLMs).
However, most benchmarks conduct questions by selecting images from existing datasets, resulting in the potential data leakage. Besides, these benchmarks merely focus on evaluating LVLMs on the realistic style images and clean scenarios, leaving the multi-stylized images and noisy scenarios unexplored. In response to these challenges, we propose a dynamic and scalable benchmark named Dysca for evaluating LVLMs by leveraging synthesis images. Specifically, we leverage Stable Diffusion and design a rule-based method to dynamically generate novel images, questions and the corresponding answers. We consider 51 kinds of image styles and evaluate the perception capability in 20 subtasks. Moreover, we conduct evaluations under 4 scenarios (i.e., Clean, Corruption, Print Attacking and Adversarial Attacking) and 3 question types (i.e., Multi-choices, True-or-false and Free-form). Thanks to the generative paradigm, Dysca serves as a scalable benchmark for easily adding new subtasks and scenarios. A total of 24 advanced open-source LVLMs and 2 close-source LVLMs are evaluated on Dysca, revealing the drawbacks of current LVLMs. The benchmark is released in anonymous github page \url{https://github.com/Benchmark-Dysca/Dysca}.

## item_id: m_0610

TITLE: Optimal Regularization can Mitigate Double Descent

ABSTRACT: Recent empirical and theoretical studies have shown that many learning algorithms -- from linear regression to neural networks -- can have test performance that is non-monotonic in quantities such the sample size and model size. This striking phenomenon, often referred to as "double descent", has raised questions of if we need to re-think our current understanding of generalization. In this work, we study whether the double-descent phenomenon can be avoided by using optimal regularization. Theoretically, we prove that for certain linear regression models with isotropic data distribution, optimally-tuned $\ell_2$ regularization achieves monotonic test performance as we grow either the sample size or the model size.
We also demonstrate empirically that optimally-tuned $\ell_2$ regularization can mitigate double descent for more general models, including neural networks.
Our results suggest that it may also be informative to study the test risk scalings of various algorithms in the context of appropriately tuned regularization.

## item_id: m_0611

TITLE: Formalising Human-in-the-Loop: Computational Reductions, Failure Modes, and Legal-Moral Responsibility

ABSTRACT: We  use the notion of oracle machines and reductions from computability theory to formalise different Human-in-the-loop (HITL) setups for AI systems, distinguishing between trivial human monitoring (i.e., total functions), single endpoint human action (i.e., many-one reductions), and highly involved human-AI interaction (i.e., Turing reductions). We then proceed to show that the legal status and safety of different setups vary greatly. We present a taxonomy to categorise HITL failure modes, highlighting the practical limitations of  HITL setups. We then identify omissions in UK and EU legal frameworks, which focus on HITL setups that may not always achieve the desired ethical, legal, and sociotechnical outcomes. We suggest areas where the law should recognise the effectiveness of different HITL setups and assign responsibility in these contexts, avoiding human `scapegoating'. Our work shows an unavoidable trade-off between attribution of legal responsibility, and  technical explainability.  Overall, we show how HITL setups involve many technical design decisions, and can be prone to failures out of the humans' control. Our formalisation and taxonomy opens up a new analytic perspective on the challenges in creating HITL setups, helping inform AI developers and lawmakers on designing HITL setups to better achieve their desired outcomes.

## item_id: m_0612

TITLE: An Empirical Study on Post-processing Methods for Word Embeddings

ABSTRACT: Word embeddings learnt from large corpora have been adopted in various applications in natural language processing and served as the general input representations to learning systems. Recently, a series of post-processing methods have been proposed to boost the performance of word embeddings on similarity comparison and analogy retrieval tasks, and some have been adapted to compose sentence representations. The general hypothesis behind these methods is that by enforcing the embedding space to be more isotropic, the similarity between words can be better expressed. We view these methods as an approach to shrink the covariance/gram matrix, which is estimated by learning word vectors, towards a scaled identity matrix. By optimising an objective in the semi-Riemannian manifold with Centralised Kernel Alignment (CKA), we are able to search for the optimal shrinkage parameter, and provide a post-processing method to smooth the spectrum of learnt word vectors which yields improved performance on downstream tasks.

## item_id: m_0613

TITLE: Deep Classifiers with Label Noise Modeling and Distance Awareness

ABSTRACT: Uncertainty estimation in deep learning has recently emerged as a crucial area of interest to advance reliability and robustness in safety-critical applications. While there have been many proposed methods that either focus on distance-aware model uncertainties for out-of-distribution detection or on input-dependent label uncertainties for in-distribution calibration, both of these types of uncertainty are often necessary. In this work, we propose the HetSNGP method for jointly modeling the model and data uncertainty. We show that our proposed model affords a favorable combination between these two complementary types of uncertainty and thus outperforms the baseline methods on some challenging out-of-distribution datasets, including CIFAR-100C, Imagenet-C, and Imagenet-A. Moreover, we propose HetSNGP Ensemble, an ensembled version of our method which adds an additional type of uncertainty and also outperforms other ensemble baselines.

## item_id: m_0614

TITLE: Generative Feature Matching Networks

ABSTRACT: We propose a non-adversarial feature matching-based approach to train generative models. Our approach, Generative Feature Matching Networks (GFMN), leverages pretrained neural networks such as autoencoders and ConvNet classifiers to perform feature extraction. We perform an extensive number of experiments with different challenging datasets, including ImageNet. Our experimental results demonstrate that, due to the expressiveness of the features from pretrained ImageNet classifiers, even by just matching first order statistics, our approach can achieve state-of-the-art results for challenging benchmarks such as CIFAR10 and STL10.

## item_id: m_0615

TITLE: DelibGAN: Coarse-to-Fine Text Generation via Adversarial Network

ABSTRACT: In this paper, we propose a novel adversarial learning framework, namely DelibGAN, for generating high-quality sentences without supervision. Our framework consists of a coarse-to-fine generator, which contains a first-pass decoder and a second-pass decoder, and a multiple instance discriminator. And we propose two training mechanisms DelibGAN-I and DelibGAN-II. The discriminator is used to fine-tune the second-pass decoder in DelibGAN-I and further evaluate the importance of each word and tune the first-pass decoder in DelibGAN-II. We compare our models with several typical and state-of-the-art unsupervised generic text generation models on three datasets (a synthetic dataset, a descriptive text dataset and a sentimental text dataset). Both qualitative and quantitative experimental results show that our models produce more realistic samples, and DelibGAN-II performs best.

## item_id: m_0616

TITLE: Uncertainty-Aware Deep Video Compression with Ensembles

ABSTRACT: Deep learning-based video compression is a challenging task and many previous state-of-the-art learning-based video codecs use optical flows to exploit the temporal correlation between successive frames and then compress the residual error. Although these two-stage models are end-to-end optimized, errors in the intermediate errors are propagated to later stages and would harm the overall performance. In this work, we investigate the inherent uncertainty in these intermediate predictions and present an ensemble-based video compression model to capture the predictive uncertainty. We also propose an ensemble-aware loss to encourage the diversity between ensemble members and investigate the benefit of incorporating adversarial training in the video compression task. Experimental results on 1080p sequences show that our model can effectively save bits by more than 20% compared to DVC Pro.

## item_id: m_0617

TITLE: DASGrad: Double Adaptive Stochastic Gradient

ABSTRACT: Adaptive moment methods have been remarkably successful for optimization under the presence of high dimensional or sparse gradients, in parallel to this, adaptive sampling probabilities for SGD have allowed optimizers to improve convergence rates by prioritizing examples to learn efficiently. Numerous applications in the past have implicitly combined adaptive moment methods with adaptive probabilities yet the theoretical guarantees of such procedures have not been explored. We formalize double adaptive stochastic gradient methods DASGrad as an optimization technique and analyze its convergence improvements in a stochastic convex optimization setting, we provide empirical validation of our findings with convex and non convex objectives. We observe that the benefits of the method increase with the model complexity and variability of the gradients, and we explore the resulting utility in extensions to transfer learning. 

## item_id: m_0618

TITLE: Efficient Low-Rank Diffusion Model Training for Text-to-Image Generation

ABSTRACT: Recent advancements in text-to-image generation models have witnessed the success of large-scale diffusion-based generative models. However, exerting control over these models, particularly for structure-conditioned text-to-image generation, remains an open challenge. One straightforward way to achieve control is via fine-tuning, often coming at the cost of efficiency. In this work, we address this challenge by introducing ELR-Diffusion (Efficient Low-rank Diffusion), a method tailored for efficient structure-conditioned image generation. Our innovative approach leverages the low-rank decomposition of model weights, leading to a dramatic reduction in memory cost and model parameters — by up to 58\%, at the same time performing comparably to larger models trained with expansive datasets and more computational resources. At the heart of ELR-Diffusion lies a two-stage training scheme that resorts to the low-rank decomposition and knowledge distillation strategy. To provide a robust assessment of our model, we undertake a thorough comparative analysis in the controllable text-to-image generation domain. We employ a diverse array of evaluation metrics with various conditions, including edge maps, segmentation maps, and image quality measures, offering a holistic view of the model's capabilities. We believe that ELR-Diffusion has the potential to serve as an efficient foundation model for diverse user applications that demand accurate comprehension of inputs containing multiple conditional information.

## item_id: m_0619

TITLE: A Half-Space Stochastic Projected Gradient Method for Group Sparsity Regularization

ABSTRACT: Optimizing with group sparsity is significant in enhancing model interpretability in machining learning applications, e.g., feature selection, compressed sensing and model compression.  However, for large-scale stochastic training problems, effective group-sparsity exploration are typically hard to achieve. Particularly, the state-of-the-art stochastic optimization algorithms usually generate merely dense solutions. To overcome this shortage, we propose a stochastic method—Half-space Stochastic Projected Gradient method (HSPG) to search solutions of high group sparsity while maintain the convergence. Initialized by a simple Prox-SG Step, the HSPG method relies on a novel Half-Space Step to substantially boosts the sparsity level.  Numerically, HSPG demonstrates its superiority in deep neural networks, e.g., VGG16, ResNet18 and MobileNetV1, by computing solutions of higher group sparsity, competitive objective values and generalization accuracy.

## item_id: m_0620

TITLE: Playing the lottery with rewards and multiple languages: lottery tickets in RL and NLP

ABSTRACT: The lottery ticket hypothesis proposes that over-parameterization of deep neural networks (DNNs) aids training by increasing the probability of a “lucky” sub-network initialization being present rather than by helping the optimization process (Frankle& Carbin, 2019). Intriguingly, this phenomenon suggests that initialization strategies for DNNs can be improved substantially, but the lottery ticket hypothesis has only previously been tested in the context of supervised learning for natural image tasks. Here, we evaluate whether “winning ticket” initializations exist in two different domains: natural language processing (NLP) and reinforcement learning (RL).For NLP, we examined both recurrent LSTM models and large-scale Transformer models (Vaswani et al., 2017). For RL, we analyzed a number of discrete-action space tasks, including both classic control and pixel control. Consistent with workin supervised image classification, we confirm that winning ticket initializations generally outperform parameter-matched random initializations, even at extreme pruning rates for both NLP and RL. Notably, we are able to find winning ticket initializations for Transformers which enable models one-third the size to achieve nearly equivalent performance. Together, these results suggest that the lottery ticket hypothesis is not restricted to supervised learning of natural images, but rather represents a broader phenomenon in DNNs.

## item_id: m_0621

TITLE: A Brain-Inspired Regularizer for Adversarial Robustness

ABSTRACT: Convolutional Neural Networks (CNNs) excel in many visual tasks, but they tend to be sensitive to slight input perturbations that are imperceptible to the human eye, often resulting in task failures. Recent studies indicate that training CNNs with regularizers that promote brain-like representations, using neural recordings, can improve model robustness. However, the requirement to use neural data severely restricts the utility of these methods. Is it possible to develop regularizers that mimic the computational function of neural regularizers without the need for neural recordings, thereby expanding the usability and effectiveness of these techniques? In this work, we inspect a neural regularizer introduced in Li et al. to extract its underlying strength. The regularizer uses neural representational similarities, which we find also correlate with pixel similarities. Motivated by this finding, we introduce a new regularizer that retains the essence of the original but is computed using image pixel similarities, eliminating the need for neural recordings.  We show that our regularization method 1) significantly increases model robustness against a variety of black box attacks, 2) relies only on original, unaugmented datasets and 3) is computationally inexpensive. Our work explores how biologically motivated loss functions can be used to drive the performance of artificial neural networks.

## item_id: m_0622

TITLE: Need a Small Specialized Language Model? Plan Early!

ABSTRACT: Large language models are versatile tools but are not suitable for small inference budgets. Small models have more efficient inference, but their lower capacity means that their performance can be good only if one limits their scope to a specialized domain.  This paper explores how to get good specialized small language models using a large, generic, pretraining set and a limited amount of specialized data. We consider two scenarios, depending on whether (i) one can afford pretraining a model for each specialization task, or (ii) one wants to cheaply adapt a single pretrained model for each task. In the first scenario, we propose an effective solution based on importance sampling: we resample the pretraining set to imitate the specialization data and train a small model on it. In the second scenario, we propose a novel architecture, projected networks (PN). PN is a large network whose parameters can be linearly projected into a small network for specialization. For both scenarios, we demonstrate the empirical effectiveness of our solutions across various domains, training set sizes, and training budgets.

## item_id: m_0623

TITLE: Actions Speak Louder Than Words: Rate-Reward Trade-off in Markov Decision Processes

ABSTRACT: The impact of communication on decision-making systems has been extensively studied under the assumption of dedicated communication channels. We instead consider communicating through actions, where the message is embedded into the actions of an agent which interacts with the environment in a Markov decision process (MDP) framework. We conceptualize the MDP environment as a finite-state channel (FSC), where the actions of the agent serve as the channel input, while the states of the MDP observed by another agent (i.e., receiver) serve as the channel output. Here, we treat the environment as a communication channel over which the agent communicates through its actions, while at the same time, trying to maximize its reward. We first characterize the optimal information theoretic trade-off between the average reward and the rate of reliable communication in the infinite-horizon regime. Then, we propose a novel framework to design a joint control/coding policy, termed Act2Comm, which seamlessly embeds messages into actions. From a communication perspective, Act2Comm functions as a learning-based channel coding scheme for non-differentiable FSCs under input-output constraints. From a control standpoint, Act2Comm learns an MDP policy that incorporates communication capabilities, though at the cost of some control performance. Overall, Act2Comm effectively balances the dual objectives of control and communication in this environment. Experimental results validate Act2Comm's capability to enable reliable communication while maintaining a certain level of control performance.

## item_id: m_0624

TITLE: Harnessing Discrete Representations for Continual Reinforcement Learning

ABSTRACT: Reinforcement learning (RL) agents make decisions using nothing but observations from the environment, and consequently, heavily rely on the representations of those observations. Though some recent breakthroughs have used vector-based categorical representations of observations, often referred to as discrete representations, there is little work explicitly assessing the significance of such a choice. In this work, we provide a thorough empirical investigation of the advantages of representing observations as vectors of categorical values within the context of reinforcement learning. We perform evaluations on world-model learning, model-free RL, and ultimately continual RL problems, where the benefits best align with the needs of the problem setting. We find that, when compared to traditional continuous representations, world models learned over discrete representations accurately model more of the world with less capacity, and that agents trained with discrete representations learn better policies with less data. In the context of continual RL, these benefits translate into faster adapting agents. Additionally, our analysis suggests that the observed performance improvements can be attributed to the information contained within the latent vectors and potentially the encoding of the discrete representation itself.

## item_id: m_0625

TITLE: How Can LLMs Serve as Experts in Malicious Code Detection? A Graph Representation Learning Based Approach

ABSTRACT: Large Language Models (LLMs) excel in code processing yet encounter challenges in malicious code detection, primarily due to their limited ability to capture long-range dependencies within large and complex codebases. To address this limitation, we propose a graph representation learning-based attention acquisition framework to enhance LLMs’ malicious code detection capabilities. Specifically, our method constructs a graph representation of the codes, extracts semantic and structural features using an LLM, and trains a Graph Neural Network (GNN) with minimally labeled data. The GNN performs an initial detection and, through backtracking of its predictions, identifies key code sections that are most likely to contain malicious behavior. These identified sections then guide the attention of the LLM for in-depth analysis. By concentrating the LLM’s processing on these critical regions, our approach reduces the interference of redundant or irrelevant data, thereby improving detection accuracy and efficiency while maintaining low annotation costs.  Extensive evaluation on both custom-built and public datasets demonstrates that our approach consistently outperforms existing detection methods, highlighting its potential for practical deployment in software security scenarios.

## item_id: m_0626

TITLE: Episodic Exploration for Deep Deterministic Policies for StarCraft Micromanagement

ABSTRACT: We consider scenarios from the real-time strategy game StarCraft as benchmarks for reinforcement learning algorithms. We focus on micromanagement, that is, the short-term, low-level control of team members during a battle. We propose several scenarios that are challenging for reinforcement learning algorithms because the state- action space is very large, and there is no obvious feature representation for the value functions. We describe our approach to tackle the micromanagement scenarios with deep neural network controllers from raw state features given by the game engine. We also present a heuristic reinforcement learning algorithm which combines direct exploration in the policy space and backpropagation. This algorithm collects traces for learning using deterministic policies, which appears much more efficient than, e.g., ε-greedy exploration. Experiments show that this algorithm allows to successfully learn non-trivial strategies for scenarios with armies of up to 15 agents, where both Q-learning and REINFORCE struggle.

## item_id: m_0627

TITLE: FastText.zip: Compressing text classification models

ABSTRACT: We consider the problem of producing compact architectures for text classification, such that the full model fits in a limited amount of memory.  After considering different solutions inspired by the hashing literature, we propose a method built upon product quantization to store the word embeddings.  While the original technique leads to a loss in accuracy,  we adapt this method to circumvent the quantization artifacts. As a result, our approach produces a text classifier, derived from the fastText approach, which at test time requires only a fraction of the memory compared to the original one, without noticeably sacrificing the quality in terms of classification accuracy. Our experiments carried out on several benchmarks show that our approach typically requires two orders of magnitude less memory than fastText while being only slightly inferior with respect to accuracy. As a result, it outperforms the state of the art by a good margin in terms of the compromise between memory usage and accuracy.

## item_id: m_0628

TITLE: Decentralized Federated Learning Over Noisy Labels: A Majority Voting Method

ABSTRACT: Contrary to centralized federated learning (CFL), decentralized federated learning (DFL) allows clients to cooperate in training their local models without relying on a central parameter server. As different clients have varying annotation skills and preferences, noisy labels are inevitable in decentralized data ownership. In centralized learning (CL) and CFL settings, learning from noisy labels has been extensively explored; however, such methods cannot be directly applied in DFL settings due to limited computational resources or privacy requirements. This paper introduces DFLMV \textit{(majority voting based decentralized federated learning)}, a general DFL framework for learning from noisy data without relying on any assumptions about local client noise models while maintaining data privacy for all clients. Specifically, (1) Clients first use traditional DFL to train their local models until they become stable. (2) Clients use each of their neighbors' models to make a prediction of every data point in their training datasets, then correct the labels based on majority voting. (3) Clients further fine-tune their models based on their updated training dataset. A theoretical analysis of DFLMV is also provided. Extensive experiments conducted on MNIST, Fashion-MNIST, CIFA-10, CIFAR-10N, CIFAR-100N, Clothing1M, and ANIMAL-10N validate the effectiveness of our proposed approach at various noise levels and different data settings in mitigating the adverse effects of noisy labels.

## item_id: m_0629

TITLE: $p$-Laplacian Based Graph Neural Networks

ABSTRACT: Graph neural networks (GNNs) have demonstrated superior performance for semi-supervised node classification on graphs, as a result of their ability to exploit node features and topological information simultaneously. However, most GNNs implicitly assume that the labels of nodes and their neighbors in a graph are the same or consistent, which does not hold in heterophilic graphs, where the labels of linked nodes are likely to differ. Hence, when the topology is non-informative for label prediction, ordinary GNNs may work significantly worse than simply applying multi-layer perceptrons (MLPs) on each node. To tackle the above problem, we propose a new $p$-Laplacian based GNN model, termed as $^p$GNN, whose message passing mechanism is derived from a discrete regularization framework and could be theoretically explained as an approximation of a polynomial graph filter defined on the spectral domain of $p$-Laplacians. The spectral analysis shows that the new message passing mechanism works simultaneously as low-pass and high-pass filters, thus making $^p$GNNs effective on both homophilic and heterophilic graphs. Empirical studies on real-world and synthetic datasets validate our findings and demonstrate that $^p$GNNs significantly outperform several state-of-the-art GNN architectures on heterophilic benchmarks while achieving competitive performance on homophilic benchmarks. Moreover, $^p$GNNs can adaptively learn aggregation weights and are robust to noisy edges.

## item_id: m_0630

TITLE: An Exact Solver for Satisfiability Modulo Counting with Probabilistic Circuits

ABSTRACT: Satisfiability Modulo Counting (SMC) is a general language to reason about problems integrating statistical and symbolic artificial intelligence. An SMC formula is an SAT formula in which the truth values of a few Boolean predicates are determined by model counting, or equivalently, probabilistic inference. Existing solvers optimize surrogate objectives and hence provide no formal guarantee. Hence, an exact solver is desperately in need. However, the direct integration of satisfiability and probabilistic inference solvers results in slow SMC solving because of many back-and-forth invocations of both solvers. We develop KOCO-SMC, a fast exact SMC solver, exploiting the fact that many similar probabilistic inferences are needed throughout SMC solving. We compile the probabilistic inference part of SMC solving into probabilistic circuits, supporting efficient lower and upper-bound computation. Experiment results in several real-world applications demonstrate that our approach provides exact solutions, much better than those from approximate solvers, while is more efficient than direct integration with the current exact solvers.

## item_id: m_0631

TITLE: Training Neural Networks for and by Interpolation

ABSTRACT: In modern supervised learning, many deep neural networks are able to interpolate the data: the empirical loss can be driven to near zero on all samples simultaneously. In this work, we explicitly exploit this interpolation property for the design of a new optimization algorithm for deep learning. Specifically, we use it to compute an adaptive learning-rate in closed form at each iteration. This results in the Adaptive Learning-rates for Interpolation with Gradients (ALI-G) algorithm. ALI-G retains the main advantage of SGD which is a low computational cost per iteration. But unlike SGD, the learning-rate of ALI-G uses a single constant hyper-parameter and does not require a decay schedule, which makes it considerably easier to tune. We provide convergence guarantees of ALI-G in the stochastic convex setting. Notably, all our convergence results tackle the realistic case where the interpolation property is satisfied up to some tolerance. We provide experiments on a variety of architectures and tasks: (i) learning a differentiable neural computer; (ii) training a wide residual network on the SVHN data set; (iii) training a Bi-LSTM on the SNLI data set; and (iv) training wide residual networks and densely connected networks on the CIFAR data sets. ALI-G produces state-of-the-art results among adaptive methods, and even yields comparable performance with SGD, which requires manually tuned learning-rate schedules. Furthermore, ALI-G is simple to implement in any standard deep learning framework and can be used as a drop-in replacement in existing code.

## item_id: m_0632

TITLE: Plan-Based Relaxed Reward Shaping for Goal-Directed Tasks

ABSTRACT: In high-dimensional state spaces, the usefulness of Reinforcement Learning (RL) is limited by the problem of exploration. This issue has been addressed using potential-based reward shaping (PB-RS) previously. In the present work, we introduce Final-Volume-Preserving Reward Shaping (FV-RS). FV-RS relaxes the strict optimality guarantees of PB-RS to a guarantee of preserved long-term behavior. Being less restrictive, FV-RS allows for reward shaping functions that are even better suited for improving the sample efficiency of RL algorithms. In particular, we consider settings in which the agent has access to an approximate plan. Here, we use examples of simulated robotic manipulation tasks to demonstrate that plan-based FV-RS can indeed significantly improve the sample efficiency of RL over plan-based PB-RS.

## item_id: m_0633

TITLE: ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding

ABSTRACT: The rapid advancement of educational applications, artistic creation, and AI-generated content (AIGC) technologies has substantially increased practical requirements for comprehensive Image Aesthetics Assessment (IAA), particularly demanding methods capable of delivering both quantitative scoring and professional understanding. Multimodal Large Language Model (MLLM)-based IAA methods demonstrate stronger perceptual and generalization capabilities compared to traditional approaches, yet they suffer from modality bias (score-only or text-only) and lack fine-grained attribute decomposition, thereby failing to support further aesthetic assessment. In this paper, we present: (1) ArtiMuse, an innovative MLLM-based IAA model with Joint Scoring and Expert-Level Understanding capabilities; (2) ArtiMuse-10K, the first expert-curated image aesthetic dataset comprising 10,000 images spanning 5 main categories and 15 sub categories, each annotated by professional experts with 8-dimensional attributes analysis and a holistic score. Both the model and dataset will be made public to advance the field.

## item_id: m_0634

TITLE: Meta-learning Transferable Representations with a Single Target Domain

ABSTRACT: Recent works found that fine-tuning and joint training---two popular approaches for transfer learning---do not always improve accuracy on downstream tasks. First, we aim to understand more about when and why fine-tuning and joint training can be suboptimal or even harmful for transfer learning. We design semi-synthetic datasets where the source task can be solved by either source-specific features or transferable features. We observe that (1) pre-training may not have incentive to learn transferable features and (2) joint training may simultaneously learn source-specific features and  overfit to the target. Second, to improve over fine-tuning and joint training, we propose Meta Representation Learning MeRLin to learn transferable features. MeRLin meta-learns representations by ensuring that a head fit on top of the representations with target training data also performs well on target validation data. We also prove that MeRLin recovers the target ground-truth model with a quadratic neural net parameterization and a source distribution that contains both transferable and source-specific features. On the same distribution,  pre-training and joint training provably fail to learn transferable features. MeRLin empirically outperforms previous state-of-the-art transfer learning algorithms  on various real-world vision and NLP transfer learning benchmarks. 

## item_id: m_0635

TITLE: Modular Multitask Reinforcement Learning with Policy Sketches

ABSTRACT: We describe a framework for multitask deep reinforcement learning guided by
policy sketches. Sketches annotate each task with a sequence of named subtasks,
providing high-level structural relationships among tasks, but not providing the
detailed guidance required by previous work on learning policy abstractions for
RL (e.g. intermediate rewards, subtask completion signals, or intrinsic motivations).
Our approach associates every subtask with its own modular subpolicy,
and jointly optimizes over full task-specific policies by tying parameters across
shared subpolicies. This optimization is accomplished via a simple decoupled
actor–critic training objective that facilitates learning common behaviors from
dissimilar reward functions. We evaluate the effectiveness of our approach on a
maze navigation game and a 2-D Minecraft-inspired crafting game. Both games
feature extremely sparse rewards that can be obtained only after completing a
number of high-level subgoals (e.g. escaping from a sequence of locked rooms or
collecting and combining various ingredients in the proper order). Experiments
illustrate two main advantages of our approach. First, we outperform standard
baselines that learn task-specific or shared monolithic policies. Second, our
method naturally induces a library of primitive behaviors that can be recombined
to rapidly acquire policies for new tasks.

## item_id: m_0636

TITLE: Multimedia Generative Script Learning for Task Planning

ABSTRACT: Goal-oriented generative script learning aims to generate subsequent steps to reach a particular goal, which is an essential task to assist robots or humans in performing stereotypical activities in daily life. However, an important aspect of this process is the ability to capture historical states visually, which provides detailed information that is not covered by text and will guide subsequent steps. Therefore, we propose a new task, Multimedia Generative Script Learning, to generate subsequent steps by tracking historical states in both text and vision modalities, as well as presenting the first benchmark containing 5,652 tasks and 79,089 steps with descriptive images. This task is challenging in three aspects: the multimedia challenge of capturing the visual states in images, the induction challenge of performing unseen tasks, and the diversity challenge of covering different information in individual steps. We propose to encode visual state changes through a selective multimedia encoder to address the multimedia challenge, transfer knowledge from previously observed tasks using a retrieval-augmented decoder to overcome the induction challenge, and further present distinct information at each step by optimizing a diversity-oriented contrastive learning objective.  We define metrics to evaluate both generation quality and inductive quality. Experiment results demonstrate that our approach significantly outperforms strong baselines.

## item_id: m_0637

TITLE: Spontaneous Symmetry Breaking in Deep Neural Networks

ABSTRACT: We propose a framework to understand the unprecedented performance and robustness of deep neural networks using field theory. Correlations between the weights within the same layer can be described by symmetries in that layer, and networks generalize better if such symmetries are broken to reduce the redundancies of the weights. Using a two parameter field theory, we find that the network can break such symmetries itself towards the end of training in a process commonly known in physics as spontaneous symmetry breaking. This corresponds to a network generalizing itself without any user input layers to break the symmetry, but by communication with adjacent layers. In the layer decoupling limit applicable to residual networks (He et al., 2015), we show that the remnant symmetries that survive the non-linear layers are spontaneously broken based on empirical results. The Lagrangian for the non-linear and weight layers together has striking similarities with the one in quantum field theory of a scalar. Using results from quantum field theory we show that our framework is able to explain many experimentally observed phenomena, such as training on random labels with zero error (Zhang et al., 2017), the information bottleneck and the phase transition out of it (Shwartz-Ziv & Tishby, 2017), shattered gradients (Balduzzi et al., 2017), and many more.

## item_id: m_0638

TITLE: MatMamba: A Matryoshka State Space Model

ABSTRACT: State Space Models (SSMs) like Mamba2 are a promising alternative to Transformers, with faster theoretical training and inference times -- especially for long context lengths. Recent work on Matryoshka Representation Learning -- and its application to Transformer backbones in works like MatFormer --  showed how to introduce nested granularities of smaller submodels in one universal elastic model. In this work, we present MatMamba: a state space model which combines Matryoshka-style learning with Mamba2, by modifying the block to contain nested dimensions to enable joint training and adaptive inference. MatMamba allows for efficient and adaptive deployment across various model sizes. We train a single large MatMamba model and are able to get a number of smaller nested models for free -- while maintaining or improving upon the performance of a baseline smaller model trained from scratch. We train language and image models at a variety of parameter sizes from 35M to 1.4B. Our results on ImageNet and FineWeb show that MatMamba models scale comparably to Transformers, while having more efficient inference characteristics. This makes MatMamba a practically viable option for deploying large-scale models in an elastic way based on the available inference compute.

## item_id: m_0639

TITLE: Dynamic Graph Representation Learning via Graph Transformer Networks

ABSTRACT: Dynamic graph representation learning is an important task with widespread applications. Previous methods on dynamic graph learning are usually sensitive to noisy graph information such as missing or spurious connections, which can yield degenerated performance and generalization. To overcome this challenge, we propose a Transformer-based dynamic graph learning method named Dynamic Graph Transformer (DGT) with spatial-temporal encoding to effectively learn graph topology and capture implicit links. To improve the generalization ability, we introduce two complementary self-supervised pre-training tasks and show that jointly optimizing the two pre-training tasks results in a smaller Bayesian error rate via an information-theoretic analysis. We also propose a temporal-union graph structure and a target-context node sampling strategy for efficient and scalable training. Extensive experiments on real-world datasets illustrate that DGT presents superior performance compared with several state-of-the-art baselines.

## item_id: m_0640

TITLE: DeepZero: Scaling Up Zeroth-Order Optimization for Deep Model Training

ABSTRACT: Zeroth-order (ZO) optimization has become a popular technique for solving machine learning (ML) problems when first-order (FO) information is difficult or impossible to obtain. However, the scalability of ZO optimization remains an open problem: Its use has primarily been limited to relatively small-scale ML problems, such as sample-wise adversarial attack generation. To our best knowledge, no prior work has demonstrated the effectiveness of ZO optimization in training deep neural networks (DNNs) without a significant decrease in performance. To overcome this roadblock, we develop DeepZero, a principled and practical ZO deep learning (DL) framework that can scale ZO optimization to DNN training from scratch through three primary innovations. First, we demonstrate the advantages of coordinate-wise gradient estimation (CGE) over randomized vector-wise gradient estimation in training accuracy and computational efficiency. Second, we propose a sparsity-induced ZO training protocol that extends the model pruning methodology using only finite differences to explore and exploit the sparse DL prior in CGE. Third, we develop the methods of feature reuse and forward parallelization to advance the practical implementations of ZO training. Our extensive experiments show that DeepZero achieves state-of-the-art (SOTA) accuracy on ResNet-20 trained on CIFAR-10, approaching FO training performance for the first time. Furthermore, we show the practical utility of DeepZero in applications of certified adversarial defense and DL-based partial differential equation error correction, achieving 10-20% improvement over SOTA. We believe our results will inspire future research on scalable ZO optimization and contribute to advancing deep learning.

## item_id: m_0641

TITLE: Contrastive Implicit Representation Learning

ABSTRACT: Implicit Neural Representations have emerged as an interesting alternative to traditional array representations. The challenge of performing downstream tasks directly on implicit representations has been addressed by several methods. Overcoming this challenge would open the door to the application of implicit representations to a wide range of fields. Then again, self-supervised representation learning methods, such as the several contrastive learning frameworks which have been proven powerful representation learning methods. So far, the use of self-supervised learning for implicit representations has remained unexplored, mostly because of the difficulty of producing valid augmented views of implicit representations to be used for learning contrasts. In this work, we adapt the popular SimCLR algorithm to implicit representations that consist of multiplicative filters networks and SIRENs. While methods to obtain augmentations in SIREN have been studied in the literature, we provide methods for augmenting MFNs effectively. We show how MFNs lend themselves well to geometric augmentations. To the best of our knowledge, our work is the first to demonstrate that self-supervised learning on implicit representations of images is feasible and results in good downstream task performances.

## item_id: m_0642

TITLE: SOLAR: Deep Structured Representations for Model-Based Reinforcement Learning

ABSTRACT: Model-based reinforcement learning (RL) methods can be broadly categorized as global model methods, which depend on learning models that provide sensible predictions in a wide range of states, or local model methods, which iteratively refit simple models that are used for policy improvement. While predicting future states that will result from the current actions is difficult, local model methods only attempt to understand system dynamics in the neighborhood of the current policy, making it possible to produce local improvements without ever learning to predict accurately far into the future. The main idea in this paper is that we can learn representations that make it easy to retrospectively infer simple dynamics given the data from the current policy, thus enabling local models to be used for policy learning in complex systems. We evaluate our approach against other model-based and model-free RL methods on a suite of robotics tasks, including manipulation tasks on a real Sawyer robotic arm directly from camera images.

## item_id: m_0643

TITLE: Efficient Planning in a Compact Latent Action Space

ABSTRACT: Planning-based reinforcement learning has shown strong performance in tasks in discrete and low-dimensional continuous action spaces. However, planning usually brings significant computational overhead for decision making, so scaling such methods to high-dimensional action spaces remains challenging. To advance efficient planning for high-dimensional continuous control, we propose Trajectory Autoencoding Planner (TAP), which learns low-dimensional latent action codes with a state-conditional VQ-VAE. The decoder of the VQ-VAE thus serves as a novel dynamics model that takes latent actions and current state as input and reconstructs long-horizon trajectories. During inference time, given a starting state, TAP searches over discrete latent actions to find trajectories that have both high probability under the training distribution and high predicted cumulative reward. Empirical evaluation in the offline RL setting demonstrates low decision latency which is indifferent to the growing raw action dimensionality. For Adroit robotic hand manipulation tasks with high-dimensional continuous action space, TAP surpasses existing model-based methods by a large margin and also beats strong model-free actor-critic baselines.

## item_id: m_0644

TITLE: Encoding the LLM Vocabulary Bottleneck

ABSTRACT: Large Language Models (LLMs) have simplified natural language processing tasks by leveraging their ability to learn from massive volumes of data and generalise across a wide range of applications. However, as LLMs continue to scale in size and complexity, optimizing their computational efficiency  has become a critical challenge. One of the major contributors to this complexity is the decision layer (referred to as the \textit{Softmax layer}), consisting of a fully connected network matched with a Softmax activation function, which scales linearly with vocabulary size resulting in high computational costs. In this work, we first propose a framework based on Error Correcting Output Coding (ECOC), which enables the encoding of several decision boundary formulation techniques, including Softmax, to be plugged in as the decision layer of an LLM. Using this framework, we analyse the minimal design strategy for defining the simplest decision boundary with optimal computation efficiency, and propose and explore extensions to this strategy to study the accuracy-complexity trade-off compared to the Softmax-based strategy using both fine-tuning and pretraining settings. We show it is possible to maintain 90\% of the Softmax accuracy when pretraining is an option, and retain 83.38\% of the F1 score during fine-tuning, while using only 50\% of the decision layer parameter size in both cases. Further gains arise by extending codeword length with random bits, and by increasing the intermediate hidden dimensions in MTL-ECOC. Overall, this work establishes the viability of substantially reducing the computational and architectural complexity of the output layer, while formalizing the integration of the ECOC framework within LLMs.

## item_id: m_0645

TITLE: Effective Model Sparsification by Scheduled Grow-and-Prune Methods

ABSTRACT: Deep neural networks (DNNs) are effective in solving many real-world problems. Larger DNN models usually exhibit better quality (e.g., accuracy) but their excessive computation results in long inference time. Model sparsification can reduce the computation and memory cost while maintaining model quality. Most existing sparsification algorithms unidirectionally remove weights, while others randomly or greedily explore a small subset of weights in each layer for pruning. The limitations of these algorithms reduce the level of achievable sparsity. In addition, many algorithms still require pre-trained dense models and thus suffer from large memory footprint. In this paper, we propose a novel scheduled grow-and-prune (GaP) methodology without having to pre-train a dense model. It addresses the shortcomings of the previous works by repeatedly growing a subset of layers to dense and then pruning them back to sparse after some training. Experiments show that the models pruned using the proposed methods match or beat the quality of the highly optimized dense models at 80% sparsity on a variety of tasks, such as image classification, objective detection, 3D object part segmentation, and translation. They also outperform other state-of-the-art (SOTA) methods for model sparsification. As an example, a 90% non-uniform sparse ResNet-50 model obtained via  GaP achieves 77.9% top-1 accuracy on ImageNet, improving the previous SOTA results by 1.5%. Code available at: https://github.com/boone891214/GaP.

## item_id: m_0646

TITLE: Pyramidal Flow Matching for Efficient Video Generative Modeling

ABSTRACT: Video generation requires modeling a vast spatiotemporal space, which demands significant computational resources and data usage. To reduce the complexity, the prevailing approaches employ a cascaded architecture to avoid direct training with full resolution latent. Despite reducing computational demands, the separate optimization of each sub-stage hinders knowledge sharing and sacrifices flexibility. This work introduces a unified pyramidal flow matching algorithm. It reinterprets the original denoising trajectory as a series of pyramid stages, where only the final stage operates at the full resolution, thereby enabling more efficient video generative modeling. Through our sophisticated design, the flows of different pyramid stages can be interlinked to maintain continuity. Moreover, we craft autoregressive video generation with a temporal pyramid to compress the full-resolution history. The entire framework can be optimized in an end-to-end manner and with a single unified Diffusion Transformer (DiT). Extensive experiments demonstrate that our method supports generating high-quality 5-second (up to 10-second) videos at 768p resolution and 24 FPS within 20.7k A100 GPU training hours. All code and models are open-sourced at https://pyramid-flow.github.io.

## item_id: m_0647

TITLE: RankedDrop: Enhancing Deep Graph Convolutional Networks Training

ABSTRACT: Graph Neural Networks (GNNs) are playing a more and more important role for analyzing unstructured data from the complex real world. Introducing random edge dropping from the input graph at training epochs could reduce over-fitting and over-smoothing phenomenon and increase the depth of GNNs. However, such method relies strongly on the chosen randomness. It makes the accuracy depend on the initialization of the randomness, which let the selection of hyper-parameters be even more difficult. We propose in this paper RankedDrop a novel method with a spatial-aware dropping-edge selection. The selection takes account of graph global information using PageRank, and graph local neighborhood information with node degree. RankedDrop provides a more stable training results comparing to the state-of-the-art solution, by maintaining the advantages of random edge dropping. Furthermore, RankedDrop is a general method that can be deployed on a deep learning framework for enhancing performance of GNNs.

## item_id: m_0648

TITLE: Learning to Represent Action Values as a Hypergraph on the Action Vertices

ABSTRACT: Action-value estimation is a critical component of many reinforcement learning (RL) methods whereby sample complexity relies heavily on how fast a good estimator for action value can be learned. By viewing this problem through the lens of representation learning, good representations of both state and action can facilitate action-value estimation. While advances in deep learning have seamlessly driven progress in learning state representations, given the specificity of the notion of agency to RL, little attention has been paid to learning action representations. We conjecture that leveraging the combinatorial structure of multi-dimensional action spaces is a key ingredient for learning good representations of action. To test this, we set forth the action hypergraph networks framework---a class of functions for learning action representations in multi-dimensional discrete action spaces with a structural inductive bias. Using this framework we realise an agent class based on a combination with deep Q-networks, which we dub hypergraph Q-networks. We show the effectiveness of our approach on a myriad of domains: illustrative prediction problems under minimal confounding effects, Atari 2600 games, and discretised physical control benchmarks.

## item_id: m_0649

TITLE: MoReL: Multi-omics Relational Learning

ABSTRACT: Multi-omics data analysis has the potential to discover hidden molecular interactions, revealing potential regulatory and/or signal transduction pathways for cellular processes of interest when studying life and disease systems. One of critical challenges when dealing with real-world multi-omics data is that they may manifest heterogeneous structures and data quality as often existing data may be collected from different subjects under different conditions for each type of omics data. We propose a novel deep Bayesian generative model to efficiently infer a multi-partite graph encoding molecular interactions across such heterogeneous views, using a fused Gromov-Wasserstein (FGW) regularization between latent representations of corresponding views for integrative analysis. With such an optimal transport regularization in the deep Bayesian generative model, it not only allows incorporating view-specific side information, either with graph-structured or unstructured data in different views, but also increases the model flexibility with the distribution-based regularization. This allows efficient alignment of heterogeneous latent variable distributions to derive reliable interaction predictions compared to the existing point-based graph embedding methods. Our experiments on several real-world datasets demonstrate enhanced performance of MoReL in inferring meaningful interactions compared to existing baselines.

## item_id: m_0650

TITLE: Pessimistic Model Selection for Offline Deep Reinforcement Learning

ABSTRACT: Deep Reinforcement Learning (DRL) has demonstrated great potentials in solving sequential decision making problems in many applications. Despite its promising performance,  practical gaps exist when deploying DRL in real-world scenarios. One main barrier is the over-fitting issue that leads to poor generalizability of the policy learned by DRL. In particular, for offline DRL with observational data, model selection is a challenging task as there is no ground truth available for performance demonstration, in contrast with the online setting with simulated environments. In this work, we propose a pessimistic model selection (PMS) approach for offline DRL with a theoretical guarantee, which features a tuning-free framework for finding the best policy among a set of candidate models. Two refined approaches are also proposed to address the potential bias of DRL model in identifying the optimal policy. Numerical studies demonstrated the superior performance of our approach over existing methods.

## item_id: m_0651

TITLE: Encoding and Decoding Representations with Sum- and Max-Product Networks

ABSTRACT: Sum-Product networks (SPNs) are expressive deep architectures for representing probability distributions, yet allowing exact and efficient inference. SPNs have been successfully applied in several domains, however always as black-box distribution estimators. In this paper, we argue that due to their recursive definition, SPNs can also be naturally employed as hierarchical feature extractors and thus for unsupervised representation learning. Moreover, when converted into Max-Product Networks (MPNs), it is possible to decode such representations back into the original input space. In this way, MPNs can be interpreted as a kind of generative autoencoder, even if they were never trained to reconstruct the input data. We show how these learned representations, if visualized, indeed correspond to "meaningful parts" of the training data. They also yield a large improvement when used in structured prediction tasks. As shown in extensive experiments, SPN and MPN encoding and decoding schemes prove very competitive  against the ones employing RBMs and other stacked autoencoder architectures.

## item_id: m_0652

TITLE: Gradient Routing: Masking Gradients to Localize Computation in Neural Networks

ABSTRACT: Neural networks are trained primarily based on their inputs and outputs, without regard for their internal mechanisms. These neglected mechanisms determine properties that are critical for safety, like (i) transparency; (ii) the absence of sensitive information or harmful capabilities; and (iii) reliable generalization of goals beyond the training distribution. To address this shortcoming, we introduce gradient routing, a training method that isolates capabilities to specific subregions of a neural network. Gradient routing applies data-dependent, weighted masks to gradients during backpropagation. These masks are supplied by the user in order to configure which parameters are updated by which data points. We show that gradient routing can be used to (1) learn representations which are partitioned in an interpretable way; (2) enable robust unlearning via ablation of a pre-specified network subregion; and (3) achieve scalable oversight of a reinforcement learner by localizing modules responsible for different behaviors. Throughout, we find that gradient routing localizes capabilities even when applied to a limited, ad-hoc subset of the data. We conclude that the approach holds promise for challenging, real-world applications where quality data are scarce.

## item_id: m_0653

TITLE: DSPFusion: Degradation and Semantic Prior Dual-guided Framework for Image Fusion

ABSTRACT: Existing fusion methods are tailored for high-quality images but struggle with degraded images captured under harsh circumstances, thus limiting the practical potential of image fusion. In this work, we present a Degradation and Semantic Prior dual-guided framework for degraded image Fusion (DSPFusion), utilizing degradation priors and high-quality scene semantic priors restored via diffusion models to guide both information recovery and fusion in a unified model. In specific, it first individually extracts modality-specific degradation priors and jointly captures comprehensive low-quality semantic priors from cascaded source images. Subsequently, a diffusion model is developed to iteratively restore high-quality semantic priors in a compact latent space, enabling our method to be over $200 \times$ faster than mainstream diffusion model-based image fusion schemes. Finally, the degradation priors and high-quality semantic priors are employed to guide information enhancement and aggregation via the dual-prior guidance and prior-guided fusion modules. Extensive experiments demonstrate that DSPFusion mitigates most typical degradations while integrating complementary context with minimal computational cost, greatly broadening the application scope of image fusion.

## item_id: m_0654

TITLE: Modeling Student Learning with 3.8 Million Program Traces

ABSTRACT: As programmers write code, they often edit and retry multiple times, creating rich “interaction traces” that reveal how they approach coding tasks and provide clues about their level of skill development. For novice programmers in particular, these traces reflect the diverse reasoning processes they employ to code, such as exploratory behavior to understand how a programming concept works, re-strategizing in response to bugs, and personalizing stylistic choices. In this work, we explore what can be learned from training language models on such reasoning traces: not just about code, but about coders, and particularly students learning to program. We introduce a dataset of over 3.8 million programming reasoning traces from users of PENCIL CODE, a free online educational platform used by students to learn simple programming concepts. Compared to models trained only on final programs or on synthetically-generated traces, we find that models trained on real traces are stronger at modeling diverse student behavior. Through both behavioral and probing analyses, we also find that many properties of code traces, such as goal backtracking or number of comments, can be predicted from learned representations of the students who write them. Building on this result, we show that we can help students recover from mistakes by steering code generation models to identify a sequence of edits that will results in more correct code while remaining close to the original student’s style. Together, our results suggest that many properties of code are properties of individual students and that training on edit traces can lead to models that are both more steerable and predictive of student behavior, even when evaluated solely on final program states.

## item_id: m_0655

TITLE: Improving Sequence-to-Sequence Learning via Optimal Transport

ABSTRACT: Sequence-to-sequence models are commonly trained via maximum likelihood estimation (MLE). However, standard MLE training considers a word-level objective, predicting the next word given the previous ground-truth partial sentence. This procedure focuses on modeling local syntactic patterns, and may fail to capture long-range semantic structure. We present a novel solution to alleviate these issues. Our approach imposes global sequence-level guidance via new supervision based on optimal transport, enabling the overall characterization and preservation of semantic features. We further show that this method can be understood as a Wasserstein gradient flow trying to match our model to the ground truth sequence distribution. Extensive experiments are conducted to validate the utility of the proposed approach, showing consistent improvements over a wide variety of NLP tasks, including machine translation, abstractive text summarization, and image captioning.

## item_id: m_0656

TITLE: Don’t Say No: Jailbreaking LLM by Suppressing Refusal

ABSTRACT: Ensuring the safety alignment of Large Language Models (LLMs) is crucial to generating responses consistent with human values. Despite their ability to recognize and avoid harmful queries, LLMs are vulnerable to jailbreaking attacks, where carefully crafted prompts seduce them to produce toxic content. One category of jailbreak attacks is reformulating the task as an optimization by eliciting the LLM to generate affirmative responses. However, such optimization objective has its own limitations, such as the restriction on the predefined objectionable behaviors, leading to suboptimal attack performance. In this study, we first uncover the reason why vanilla target loss is not optimal, then we explore and enhance the loss objective and introduce the $\textit{DSN}$ (Don't Say No) attack, which achieves successful attack by suppressing refusal. Another challenge in studying jailbreak attacks is the evaluation, as it is difficult to directly and accurately assess the harmfulness of the responses. The existing evaluation such as refusal keyword matching reveals numerous false positive and false negative instances. To overcome this challenge, we propose an Ensemble Evaluation pipeline that novelly incorporates Natural Language Inference (NLI) contradiction assessment and two external LLM evaluators. Extensive experiments demonstrate the potential of the $\textit{DSN}$ and effectiveness of Ensemble Evaluation compared to baseline methods.

## item_id: m_0657

TITLE: Enhancing Detail Preservation for Customized Text-to-Image Generation: A Regularization-Free Approach

ABSTRACT: Recent text-to-image generation models have demonstrated impressive capability of generating text-aligned images with high fidelity. However, generating images of novel concepts specified by a reference image remains a challenging task. To address this problem, researchers have been exploring various methods for customizing pre-trained text-to-image generation models. Currently, most existing methods for customizing pre-trained text-to-image generation models involve the use of regularization techniques to prevent over-fitting. Although regularization will ease the challenge of customization and leads to successful content creation with respect to text guidance, it may restrict the model capability, resulting in the loss of detailed information and inferior performance. In this work, we propose ProFusion, a novel framework for customized text-to-image generation, which can tackle the over-fitting problem without the widely used regularization. Specifically, it consists of an encoder network and a novel sampling method. Given a single user-provided image from an arbitrary domain, the proposed framework can customize a pre-trained text-to-image generation model within half a minute. Empirical results demonstrate that our proposed framework outperforms existing methods.

## item_id: m_0658

TITLE: Gaussian Attention Model and Its Application to Knowledge Base Embedding and Question Answering

ABSTRACT: We propose the Gaussian attention model for content-based neural memory
access. With the proposed attention model, a neural network has the
additional degree of freedom to control the focus of its attention from
a laser sharp attention to a broad attention. It is applicable whenever
we can assume that the distance in the latent space reflects some notion
of semantics. We use the proposed attention model as a scoring function
for the embedding of a knowledge base into a continuous vector space and
then train a model that performs question answering about the entities
in the knowledge base. The proposed attention model can handle both the
propagation of uncertainty when following a series of relations and also
the conjunction of conditions in a natural way. On a dataset of soccer
players who participated in the FIFA World Cup 2014, we demonstrate that
our model can handle both path queries and conjunctive queries well.

## item_id: m_0659

TITLE: Learning to Remove, Not Repeat: Robust Object Removal in Cluttered Scenes using Diffusion Models

ABSTRACT: Object removal, a key image inpainting task, aims to erase specified objects and plausibly fill the resulting region. Although recent diffusion models excel at generating realistic content, when employed for the removal task, they often fail in cluttered scenes by replicating nearby objects or hallucinating semantically similar ones, an artifact of their powerful, yet context-agnostic, generative priors. To address this, we introduce a robust framework that Learns to Remove, Not Repeat (LRNR). Our approach has three key components. First, we propose the Scatter-Tile Object Removal (STORe) dataset, a large-scale synthetic dataset with unique scatter and tile configurations designed to make models robust to object replication. Second, we employ an efficient fine-tuning strategy that combines Low-Rank Adaptation (LoRA) with a learnable task prompt, which internalizes the concept of removal, thereby eliminating the need for manual text guidance. Third, we introduce Mask-Aware Scheduled Guidance (MASG), a training-free inference technique that spatially and temporally modulates classifier-free guidance to enhance inpainting quality and preserve background integrity. Our evaluations demonstrate that LRNR outperforms state-of-the-art approaches, particularly in terms of removal success rate in challenging scenes prone to object replication, leading to more reliable and semantically correct results. Our dataset, source code, and trained models will be publicly available.

## item_id: m_0660

TITLE: Pixel Redrawn For A Robust Adversarial Defense

ABSTRACT: Recently, an adversarial example becomes a serious problem to be aware of because it can fool trained neural networks easily.
To prevent the issue, many researchers have proposed several defense techniques such as adversarial training, input transformation, stochastic activation pruning, etc.
In this paper, we propose a novel defense technique, Pixel Redrawn (PR) method, which redraws every pixel of training images to convert them into distorted images.
The motivation for our PR method is from the observation that the adversarial attacks have redrawn some pixels of the original image with the known parameters of the trained neural network.
Mimicking these attacks, our PR method redraws the image without any knowledge of the trained neural network.
This method can be similar to the adversarial training method but our PR method can be used to prevent future attacks.
Experimental results on several benchmark datasets indicate our PR method not only relieves the over-fitting issue when we train neural networks with a large number of epochs, but it also boosts the robustness of the neural network.

## item_id: m_0661

TITLE: D-GAN: Divergent generative adversarial network for positive unlabeled learning and counter-examples generation

ABSTRACT: Positive Unlabeled (PU) learning consists in learning to distinguish samples of our class of interest, the positive class, from the counter-examples, the negative class, by using positive labeled and unlabeled samples during the training. Recent approaches exploit the GANs abilities to address the PU learning problem by generating relevant counter-examples. In this paper, we propose a new GAN-based PU learning approach named Divergent-GAN (D-GAN). The key idea is to incorporate a standard Positive Unlabeled learning risk inside the GAN discriminator loss function. In this way, the discriminator can ask the generator to converge towards the unlabeled samples distribution while diverging from the positive samples distribution. This enables the generator convergence towards the unlabeled counter-examples distribution without using prior knowledge, while keeping the standard adversarial GAN architecture. In addition, we discuss normalization techniques in the context of the proposed framework. Experimental results show that the proposed approach overcomes previous GAN-based PU learning methods issues, and it globally outperforms two-stage state of the art PU learning performances in terms of stability and prediction on both simple and complex image datasets.

## item_id: m_0662

TITLE: Distribution Shift Aware Neural Feature Transformation

ABSTRACT: Feature transformation, as a core task of Data-centric AI (DCAI), aims to improve the original feature set to enhance AI capabilities. In dynamic real-world environments, where there exists a distribution shift, feature knowledge may not be transferable between data. This matter prompts a distribution shift feature transformation (DSFT) problem. Prior research works for feature transformation either depend on domain expertise, rely on a linear assumption, prove inefficient for large feature spaces, or demonstrate vulnerability to imperfect data. Furthermore, existing techniques for addressing the distribution shift cannot be directly applied to discrete search problems. DSFT presents two primary challenges: 1) How can we reformulate and solve feature transformation as a learning problem? and 2) What mechanisms can integrate shift awareness into such a learning paradigm? To tackle these challenges, we leverage a unique Shift-aware Representation-Generation Perspective. To formulate a learning scheme, we construct a representation-generation framework: 1) representation step: encoding transformed feature sets into embedding vectors; 2) generation step: pinpointing the best embedding and decoding as a transformed feature set. To mitigate the issue of distribution shift, we propose three mechanisms: 1) shift-resistant representation, where embedding dimension decorrelation and sample reweighing are integrated to extract the true representation that contains invariant information under distribution shift; 2) flatness-aware generation, where several suboptimal embeddings along the optimization trajectory are averaged to obtain a robust optimal embedding, proving effective for diverse distribution; and 3) shift-aligned pre and post-processing, where normalizing and denormalizing align and recover distribution gaps between training and testing data. Ultimately, extensive experiments are conducted to indicate the effectiveness, robustness, and trackability of our proposed framework.

## item_id: m_0663

TITLE: Do Perceptually Aligned Gradients Imply Robustness?

ABSTRACT: Deep learning-based networks have achieved unprecedented success in numerous tasks, among which image classification. Despite these remarkable achievements, recent studies have demonstrated that such classification networks are easily fooled by small malicious perturbations, also known as adversarial examples. This security weakness led to extensive research aimed at obtaining robust models. Beyond the clear robustness benefits of such models, it was also observed that their gradients with respect to the input align with human perception. Several works have identified Perceptually Aligned Gradients (PAG) as a byproduct of robust training, but none have considered it as a standalone phenomenon nor studied its own implications. In this work, we focus on this trait and test whether \emph{Perceptually Aligned Gradients imply Robustness}. To this end, we develop a novel objective to directly promote PAG in training classifiers and examine whether models with such gradients are more robust to adversarial attacks. We present both heuristic and principled ways for obtaining target PAGs, which our method aims to learn. Specifically, we harness recent findings in score-based generative modeling as a source for PAG. Extensive experiments on CIFAR-10 and STL validate that models trained with our method have improved robust performance, exposing the surprising bidirectional connection between PAG and robustness.

## item_id: m_0664

TITLE: Zero-Cost Operation Scoring in Differentiable Architecture Search

ABSTRACT: Differentiable neural architecture search (NAS) has attracted significant attention in recent years due to its ability to quickly discover promising architectures of deep neural networks even in very large search spaces. Despite its success, many differentiable NAS methods lack robustness and may degenerate to trivial architectures with excessive parameter-free operations such as skip connections thus leading to inferior performance. In fact, selecting operations based on the magnitude of architectural parameters was recently proven to be fundamentally wrong, showcasing the need to rethink how operation scoring and selection occurs in differentiable NAS. To this end, we formalize and analyze a fundamental component of differentiable NAS: local "operation scoring" that occurs at each choice of operation.
When comparing existing operation scoring functions, we find that existing methods can be viewed as inexact proxies for accuracy.
We also find that existing methods perform poorly when analyzed empirically on NAS benchmarks. From this perspective, we introduce new training-free proxies to the context of differentiable NAS, and show that we can significantly speed up the search process while improving accuracy on multiple search spaces. We take inspiration from zero-cost proxies that were recently studied in the context of sample-based NAS but shown to degrade significantly for larger search spaces like DARTS. Our novel "perturbation-based zero-cost operation scoring" (Zero-Cost-PT) improves searching time and accuracy compared to the best available differentiable architecture search for many search space sizes, including very large ones. Specifically, we are able improve accuracy compared to the best current method (DARTS-PT) on the DARTS CNN search space while being over 40x faster (total searching time 25 minutes on a single GPU). Our code is available at: https://github.com/avail-upon-acceptance.

## item_id: m_0665

TITLE: DeepArchitect: Automatically Designing and Training Deep Architectures

ABSTRACT: In deep learning, performance is strongly affected by the choice of architecture
and hyperparameters. While there has been extensive work on automatic hyperpa-
rameter optimization for simple spaces, complex spaces such as the space of deep
architectures remain largely unexplored. As a result, the choice of architecture is
done manually by the human expert through a slow trial and error process guided
mainly by intuition. In this paper we describe a framework for automatically
designing and training deep models. We propose an extensible and modular lan-
guage that allows the human expert to compactly represent complex search spaces
over architectures and their hyperparameters. The resulting search spaces are tree-
structured and therefore easy to traverse. Models can be automatically compiled to
computational graphs once values for all hyperparameters have been chosen. We
can leverage the structure of the search space to introduce different model search
algorithms, such as random search, Monte Carlo tree search (MCTS), and sequen-
tial model-based optimization (SMBO). We present experiments comparing the
different algorithms on CIFAR-10 and show that MCTS and SMBO outperform
random search. We also present experiments on MNIST, showing that the same
search space achieves near state-of-the-art performance with a few samples. These
experiments show that our framework can be used effectively for model discov-
ery, as it is possible to describe expressive search spaces and discover competitive
models without much effort from the human expert. Code for our framework and
experiments has been made publicly available

## item_id: m_0666

TITLE: Code2Video: A Code-centric Paradigm for Educational Video Generation

ABSTRACT: While recent generative models advance pixel-space video synthesis, they remain limited in producing professional educational videos, which demand disciplinary knowledge, precise visual structures, and coherent transitions, limiting their applicability in educational scenarios. Intuitively, such requirements are better addressed through the manipulation of a renderable environment, which can be explicitly controlled via logical commands (*e.g.*, code). In this work, we propose **Code2Video**, a code-centric agent framework for generating educational videos via executable Python code. The framework comprises three collaborative agents: *(i) Planner*, which structures lecture content into temporally coherent flows and prepares corresponding visual assets; *(ii) Coder*, which converts structured instructions into executable Python codes while incorporating scope-guided auto-fix to enhance efficiency; and *(iii) Critic*, which leverages vision-language models (VLM) with visual anchor prompts to refine spatial layout and ensure clarity. To support systematic evaluation, we build **MMMC**, a benchmark of professionally produced, discipline-specific educational videos. We evaluate MMMC across diverse dimensions, including VLM-as-a-Judge aesthetic scores, code efficiency, and particularly, **TeachQuiz**, a novel end-to-end metric that quantifies how well a VLM, after unlearning, can recover knowledge by watching the generated videos. Our results demonstrate the potential of Code2Video as a scalable, interpretable, and controllable approach, achieving 40% improvement over direct code generation and producing videos comparable to human-crafted tutorials.

## item_id: m_0667

TITLE: TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting

ABSTRACT: Spiking Neural Networks (SNNs) offer a promising, biologically inspired approach for processing spatiotemporal data, particularly for time series forecasting.
However, conventional neuron models like the Leaky Integrate-and-Fire (LIF) struggle to capture long-term dependencies and effectively process multi-scale temporal dynamics.
To overcome these limitations, we introduce the Temporal Segment Leaky Integrate-and-Fire (TS-LIF) model, featuring a novel dual-compartment architecture.
The dendritic and somatic compartments specialize in capturing distinct frequency components, providing functional heterogeneity that enhances the neuron's ability to process both low- and high-frequency information.
Furthermore, the newly introduced direct somatic current injection reduces information loss during intra-neuronal transmission, while dendritic spike generation improves multi-scale information extraction.
We provide a theoretical stability analysis of the TS-LIF model and explain how each compartment contributes to distinct frequency response characteristics.
Experimental results show that TS-LIF outperforms traditional SNNs in time series forecasting, demonstrating better accuracy and robustness, even with missing data.
TS-LIF advances the application of SNNs in time-series forecasting, providing a biologically inspired approach that captures complex temporal dynamics and offers potential for practical implementation in diverse forecasting scenarios.

## item_id: m_0668

TITLE: Combining policy gradient and Q-learning

ABSTRACT: Policy gradient is an efficient technique for improving a policy in a reinforcement learning setting. However, vanilla online variants are on-policy only and not able to take advantage of off-policy data. In this paper we describe a new technique that combines policy gradient with off-policy Q-learning, drawing experience from a replay buffer. This is motivated by making a connection between the fixed points of the regularized policy gradient algorithm and the Q-values. This connection allows us to estimate the Q-values from the action preferences of the policy, to which we apply Q-learning updates. We refer to the new technique as ‘PGQL’, for policy gradient and Q-learning. We also establish an equivalency between action-value fitting techniques and actor-critic algorithms, showing that regularized policy gradient techniques can be interpreted as advantage function learning algorithms. We conclude with some numerical examples that demonstrate improved data efficiency and stability of PGQL. In particular, we tested PGQL on the full suite of Atari games and achieved performance exceeding that of both asynchronous advantage actor-critic (A3C) and Q-learning.               


## item_id: m_0669

TITLE: Finding Winning Tickets with Limited (or No) Supervision

ABSTRACT: The lottery ticket hypothesis argues that neural networks contain sparse subnetworks, which, if appropriately initialized (the winning tickets), are capable of matching the accuracy of the full network when trained in isolation. Empirically made in different contexts, such an observation opens interesting questions about the dynamics of neural network optimization and the importance of their initializations. However, the properties of winning tickets are not well understood, especially the importance of supervision in the generating process. In this paper, we aim to answer the following open questions: can we find winning tickets with few data samples or few labels? can we even obtain good tickets without supervision? Perhaps surprisingly, we provide a positive answer to both, by generating winning tickets with limited access to data, or with self-supervision---thus without using manual annotations---and then demonstrating the transferability of the tickets to challenging classification tasks such as ImageNet.


## item_id: m_0670

TITLE: Reshaping Model Output Space Via Deep Kernel Density Estimation Networks

ABSTRACT: Traditional classification models are typically optimized solely for their specific training task without considering the properties of the underlying probability distribution of their output space. As the use of these models for downstream tasks becomes more prevalent, it becomes advantageous to have a framework that can transform the output space of such models to a more convenient space without
sacrificing performance. In this paper, we introduce DeepKDE, a novel method which enables the transformation of arbitrary output spaces to match more desirable distributions, such as Normal and Gaussian Mixture Models. We explore the properties of the new method and test its effectiveness on ResNet-18 and vision transformers trained on CIFAR-10 and Fashion MNIST datasets. We show that DeepKDE models succeed in transforming the output spaces of the original models while outperforming them in terms of accuracy.

## item_id: m_0671

TITLE: DARA: Dynamics-Aware Reward Augmentation in Offline Reinforcement Learning

ABSTRACT: Offline reinforcement learning algorithms promise to be applicable in settings where a fixed dataset is available and no new experience can be acquired. However, such formulation is inevitably offline-data-hungry and, in practice, collecting a large offline dataset for one specific task over one specific environment is also costly and laborious. In this paper, we thus 1) formulate the offline dynamics adaptation by using (source) offline data collected from another dynamics to relax the requirement for the extensive (target) offline data, 2) characterize the dynamics shift problem in which prior offline methods do not scale well, and 3) derive a simple dynamics-aware reward augmentation (DARA) framework from both model-free and model-based offline settings. Specifically, DARA emphasizes learning from those source transition pairs that are adaptive for the target environment and mitigates the offline dynamics shift by characterizing state-action-next-state pairs instead of the typical state-action distribution sketched by prior offline RL methods. The experimental evaluation demonstrates that DARA, by augmenting rewards in the source offline dataset, can acquire an adaptive policy for the target environment and yet significantly reduce the requirement of target offline data. With only modest amounts of target offline data, our performance consistently outperforms the prior offline RL methods in both simulated and real-world tasks. 

## item_id: m_0672

TITLE: Spatially Decomposed Hinge Adversarial Loss by Local Gradient Amplifier

ABSTRACT: Generative Adversarial Networks (GANs) have achieved large attention and great success in various research areas, but it still suffers from training instability. Recently hinge adversarial loss for GAN is proposed that incorporates the SVM margins where real and fake samples falling within the margins contribute to the loss calculation. In a generator training step, however, fake samples outside of the margins that partially include unrealistic local patterns are ignored. In this work, we propose local gradient amplifier(LGA) which realizes spatially decomposed hinge adversarial loss for improved generator training. Spatially decomposed hinge adversarial loss applies different margins for different spatial regions extending overall margin space toward all fake samples asymmetrically. Our proposed method is evaluated on several public benchmark data sets compared to state of the art methods showing outstanding stability in training GANs.

## item_id: m_0673

TITLE: Compensating for Nonlinear Reduction with Linear Computations in Private Inference

ABSTRACT: Increasingly serious data privacy concerns and strict regulations have recently posed significant challenges to machine learning, a field that hinges on high-performance processing of massive user data.
Consequently, privacy-preserving machine learning (PPML) has emerged to securely execute machine learning tasks without violating privacy.
Unfortunately, the computational cost to securely execute nonlinear computations in PPML models remains significant, calling for new neural architecture designs with fewer nonlinear operations.
We propose Seesaw, a novel neural architecture search method tailored for PPML. 
Seesaw exploits a previously unexplored opportunity to leverage more linear computations and nonlinear result reuse, in order to compensate for the accuracy loss due to nonlinear reduction.
It also incorporates specifically designed pruning and search strategies to efficiently handle the much larger design space including both nonlinear and linear operators.
Compared to the previous state-of-the-art PPML for image classification on ImageNet, Seesaw achieves $1.68\times$ less latency at 71\% iso-accuracy, or 4.59\% higher accuracy at iso-latency of 1000K ReLU operations.

## item_id: m_0674

TITLE: QUANTILE-LSTM: A ROBUST LSTM FOR ANOMALY DETECTION

ABSTRACT: Anomalies refer to departure of systems and devices from their normal behaviour in standard operating conditions. An anomaly in an industrial device can indicate an upcoming failure, often in the temporal direction. In this paper, we make two contributions: 1) we estimate conditional quantiles, and consider three different ways to define anomalies based on the estimated quantiles and 2) use a new
learnable activation function in the popular Long Short Term Memory (LSTM) architecture to model temporal long-range dependency. In particular, we propose Parametrized Elliot Function (Parametric Elliot Function (PEF)) as an activation function inside LSTM, which saturates lately compared to sigmoid and tanh. The proposed algorithms are compared with other well known anomaly detection algorithms, such as Isolation Forest (iForest), Elliptic Envelope, Autoencoder,and modern Deep Learning models such as Deep Autoencoding Gaussian Mixture Model (DAGMM), Generative Adversarial Networks (GAN) etc. The algorithms are evaluated in terms of various performance metrics, such as precision and recall. The algorithms are experimented on multiple industrial timeseries datasets such as Yahoo, AWS, GE, and machine sensor. We have found the LSTM based quantile algorithms are very effective and outperformed the existing algorithms in identifying the anomalies.


## item_id: m_0675

TITLE: AROID: Improving Adversarial Robustness through Online Instance-wise Data Augmentation

ABSTRACT: Deep neural networks are vulnerable to adversarial examples. Adversarial training (AT) is an effective defense against adversarial examples. However, AT is prone to overfitting which degrades robustness substantially. Recently, data augmentation (DA) was shown to be effective in mitigating robust overfitting if appropriately designed and optimized for AT. This work proposes a new method to automatically learn online, instance-wise, DA policies to improve robust generalization for AT. This is the first automated DA method specific for robustness. A novel policy learning objective, consisting of Vulnerability, Affinity and Diversity, is proposed and shown to be sufficiently effective and efficient to be practical for automatic DA generation during AT. Importantly, our method dramatically reduces the cost of policy search from the 5000 hours of AutoAugment and the 412 hours of IDBH to 9 hours, making automated DA more practical to use for adversarial robustness.
This allows our method to efficiently explore a large search space for a more effective DA policy and evolve the policy as training progresses. Empirically, our method is shown to outperform all competitive DA methods across various model architectures (CNNs and ViTs) and datasets (CIFAR10/100, Imagenette, ImageNet, SVHN). Our DA policy reinforced vanilla AT to surpass several state-of-the-art AT methods regarding both accuracy and robustness. It can also be combined with those advanced AT methods to further boost robustness.

## item_id: m_0676

TITLE: A Unified View on Graph Neural Networks as Graph Signal Denoising

ABSTRACT: Graph Neural Networks (GNNs) have risen to prominence in learning representations for graph structured data. A single GNN layer typically consists of a feature transformation and a feature aggregation operation. The former normally uses feed-forward networks to transform features, while the latter aggregates the transformed features over the graph. Numerous recent works have proposed GNN models with different designs in the aggregation operation. In this work, we establish mathematically that the aggregation processes in a group of representative GNN models including GCN, GAT, PPNP, and APPNP can be regarded as (approximately) solving a graph denoising problem with a smoothness assumption. Such a unified view across GNNs not only provides a new perspective to understand a variety of aggregation operations but also enables us to develop a unified graph neural network framework UGNN. To demonstrate its promising potential, we instantiate a novel GNN model, ADA-UGNN, derived from UGNN, to handle graphs with adaptive smoothness across nodes. Comprehensive experiments show the effectiveness of ADA-UGNN. 

## item_id: m_0677

TITLE: Towards Provable Control for Unknown Linear Dynamical Systems

ABSTRACT: We study the control of symmetric linear dynamical systems with unknown dynamics and a hidden state. Using a recent spectral filtering technique for concisely representing such systems in a linear basis, we formulate optimal control in this setting as a convex program. This approach eliminates the need to solve the non-convex problem of explicit identification of the system and its latent state, and allows for provable optimality guarantees for the control signal. We give the first efficient algorithm for finding the optimal control signal with an arbitrary time horizon T, with sample complexity (number of training rollouts) polynomial only in log(T) and other relevant parameters.

## item_id: m_0678

TITLE: Convolutional Normalizing Flows

ABSTRACT: Bayesian posterior inference is prevalent in various machine learning problems. Variational inference provides one way to approximate the posterior distribution, however its expressive power is limited and so is the accuracy of resulting approximation. Recently, there has a trend of using neural networks to approximate the variational posterior distribution due to the flexibility of neural network architecture. One way to construct flexible variational distribution is to warp a simple density into a complex by normalizing flows, where the resulting density can be analytically evaluated. However, there is a trade-off between the flexibility of normalizing flow and computation cost for efficient transformation. In this paper, we propose a simple yet effective architecture of normalizing flows, ConvFlow, based on convolution over the dimensions of random input vector. Experiments on synthetic and real world posterior inference problems demonstrate the effectiveness and efficiency of the proposed method.

## item_id: m_0679

TITLE: Episodic Memory Representation for Long Video Understanding

ABSTRACT: Video Large Language Models (Video-LLMs) excel at general video understanding but struggle with long-form videos due to context-window limits. Consequently, recent approaches focus on keyframe retrieval, condensing lengthy videos into a small set of informative frames. Despite their practicality, these methods simplify the problem to static text-image matching, overlooking spatio-temporal relationships crucial for capturing scene transitions and contextual continuity, and may yield redundant keyframes with limited information, diluting salient cues essential for accurate video question answering. To address these limitations, we introduce Video-EM, a training-free framework inspired by the principles of human episodic memory, designed to facilitate robust and contextually grounded reasoning. Rather than treating keyframes as isolated visual entities, Video-EM explicitly models them as temporally ordered episodic events, capturing both spatial relationships and temporal dynamics necessary for accurately reconstructing the underlying narrative. Furthermore, the framework leverages chain-of-thought (CoT) thinking with LLMs to iteratively identify a minimal yet highly informative subset of episodic memories, enabling efficient and accurate question answering by Video-LLMs. Extensive evaluations on multiple mainstream long-video benchmarks demonstrate the superiority of Video-EM, which achieves highly competitive results while using fewer frames.

## item_id: m_0680

TITLE: Connecting the Dots Between MLE and RL for Sequence Prediction

ABSTRACT: Sequence prediction models can be learned from example sequences with a variety of training algorithms. Maximum likelihood learning is simple and efficient, yet can suffer from compounding error at test time. 
Reinforcement learning such as policy gradient addresses the issue but can have prohibitively poor exploration efficiency. A rich set of other algorithms, such as data noising, RAML, and softmax policy gradient, have also been developed from different perspectives. 
In this paper, we present a formalism of entropy regularized policy optimization, and show that the apparently distinct algorithms, including MLE, can be reformulated as special instances of the formulation. The difference between them is characterized by the reward function and two weight hyperparameters.
The unifying interpretation enables us to systematically compare the algorithms side-by-side, and gain new insights into the trade-offs of the algorithm design.
The new perspective also leads to an improved approach that dynamically interpolates among the family of algorithms, and learns the model in a scheduled way. Experiments on machine translation, text summarization, and game imitation learning demonstrate superiority of the proposed approach.

## item_id: m_0681

TITLE: Classless Association using Neural Networks

ABSTRACT: The goal of this paper is to train a model based on the relation between two instances that represent the same unknown class.  This scenario is inspired by the Symbol Grounding Problem and the association learning in infants.  We propose a novel model called Classless Association.  It has two parallel Multilayer Perceptrons (MLP) that uses one network as a target of the other network, and vice versa.  In addition, the presented model is trained based on an EM-approach, in which the output vectors are matched against a statistical distribution.  We generate four classless datasets based on MNIST, where the input is two different instances of the same digit.  In addition,  the digits have a uniform distribution.  Furthermore, our classless association model is evaluated against two scenarios: totally supervised and totally unsupervised.  In the first scenario, our model reaches a good performance in terms of accuracy and the classless constraint.  In the second scenario, our model reaches better results against two clustering algorithms.


## item_id: m_0682

TITLE: Parametric Manifold Learning Via Sparse Multidimensional Scaling

ABSTRACT: We propose a metric-learning framework for computing distance-preserving maps that generate low-dimensional embeddings for a certain class of manifolds. We employ Siamese networks to solve the problem of least squares multidimensional scaling for generating mappings that preserve geodesic distances on the manifold. In contrast to previous parametric manifold learning methods we show a substantial reduction in training effort enabled by the computation of geodesic distances in a farthest point sampling strategy. Additionally, the use of a network to model the distance-preserving map reduces the complexity of the multidimensional scaling problem and leads to an improved non-local generalization of the manifold compared to analogous non-parametric counterparts. We demonstrate our claims on point-cloud data and on image manifolds and show a numerical analysis of our technique to facilitate a greater understanding of the representational power of neural networks in modeling manifold data.

## item_id: m_0683

TITLE: Leveraging inductive bias of neural networks for learning without explicit human annotations

ABSTRACT: Classification problems today are typically solved by first collecting examples along with candidate labels, second obtaining clean labels from workers, 
and third training a large, overparameterized deep neural network on the clean examples. The second, labeling step is often the most expensive one as it requires manually going through all examples.
In this paper we skip the labeling step entirely and propose to directly train the deep neural network on the noisy raw labels and early stop the training to avoid overfitting.
With this procedure we exploit an intriguing property of large overparameterized neural networks: While they are capable of perfectly fitting the noisy data, gradient descent fits clean labels much faster than the noisy ones, thus early stopping resembles training on the clean labels.
Our results show that early stopping the training of standard deep networks such as ResNet-18 on part of the Tiny Images dataset, which does not involve any human labeled data, and of which only about half of the labels are correct, gives a significantly higher test performance than when trained on the clean CIFAR-10 training dataset, which is a labeled version of the Tiny Images dataset, for the same classification problem.
In addition, our results show that the noise generated through the label collection process is not nearly as adversarial for learning as the noise generated by randomly flipping labels, which is the noise most prevalent in works demonstrating noise robustness of neural networks.

## item_id: m_0684

TITLE: Pay Attention to Features, Transfer Learn Faster CNNs

ABSTRACT: Deep convolutional neural networks are now widely deployed in vision applications, but a limited size of training data can restrict their task performance. Transfer learning offers the chance for CNNs to learn with limited data samples by transferring knowledge from models pretrained on large datasets. Blindly transferring all learned features from the source dataset, however, brings unnecessary computation to CNNs on the target task. In this paper, we propose attentive feature distillation and selection (AFDS), which not only adjusts the strength of transfer learning regularization but also dynamically determines the important features to transfer. By deploying AFDS on ResNet-101, we achieved a state-of-the-art computation reduction at the same accuracy budget, outperforming all existing transfer learning methods. With a 10x MACs reduction budget, a ResNet-101 equipped with AFDS transfer learned from ImageNet to Stanford Dogs 120, can achieve an accuracy 11.07% higher than its best competitor.

## item_id: m_0685

TITLE: Making Sense of Reinforcement Learning and Probabilistic Inference

ABSTRACT: Reinforcement learning (RL) combines a control problem with statistical estimation: The system dynamics are not known to the agent, but can be learned through experience. A recent line of research casts ‘RL as inference’ and suggests a particular framework to generalize the RL problem as probabilistic inference. Our paper surfaces a key shortcoming in that approach, and clarifies the sense in which RL can be coherently cast as an inference problem. In particular, an RL agent must consider the effects of its actions upon future rewards and observations: The exploration-exploitation tradeoff. In all but the most simple settings, the resulting inference is computationally intractable so that practical RL algorithms must resort to approximation. We demonstrate that the popular ‘RL as inference’ approximation can perform poorly in even very basic problems. However, we show that with a small modification the framework does yield algorithms that can provably perform well, and we show that the resulting algorithm is equivalent to the recently proposed K-learning, which we further connect with Thompson sampling.


## item_id: m_0686

TITLE: Learning the Minimum Action Distance

ABSTRACT: This paper presents a state representation framework for Markov decision processes (MDPs) that can be learned solely from state trajectories, requiring neither reward signals nor the actions executed by the agent. We propose learning the $\textit{minimum action distance}$ (MAD), defined as the minimum number of actions required to transition between states, as a fundamental metric that captures the underlying structure of an environment. MAD naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping by providing a dense, geometrically meaningful measure of progress. Our self-supervised learning approach constructs an embedding space where the distances between embedded state pairs correspond to their MAD, accommodating both symmetric and asymmetric approximations. We evaluate the framework on a comprehensive suite of environments with known MAD values, encompassing both deterministic and stochastic dynamics, as well as discrete and continuous state spaces, and environments with noisy observations. Empirical results demonstrate that the proposed approach not only efficiently learns accurate MAD representations across these diverse settings but also significantly outperforms existing state representation methods in terms of representation quality.

## item_id: m_0687

TITLE: Aligning Agents like Large Language Models

ABSTRACT: Training agents to behave as desired in complex 3D environments from visual information is challenging. Imitation learning from diverse human behaviour provides a scalable mechanism for training an agent with generally sensible behaviours, but such an agent may not perform the specific behaviours of interest when deployed. To address this issue, we draw an analogy between the undesirable behaviours of imitation learning agents and the unhelpful responses of unaligned large language models (LLMs). We then investigate how the procedure for aligning LLMs can be applied to aligning agents from pixels in a complex 3D environment. For our analysis, we utilise an academically illustrative part of a modern console game in which the human behaviour distribution is diverse, but we would like our agent to imitate a single mode of this behaviour. We find that we can align our base agent to consistently perform the desired behaviour, providing a demonstration of a general approach for training agents to perform specific behaviours in complex environments.

## item_id: m_0688

TITLE: Compositional Image Generation and Manipulation with Latent Diffusion Models

ABSTRACT: We propose a principled method for compositional image generation and manipulation using diffusion probabilistic models. In particular, for any pre-trained generative model with a semantic latent space, we train a latent diffusion model and auxiliary latent classifiers to help navigate latent representations in a non-linear fashion. We show that such conditional generation achieved by latent classifier guidance provably maximizes a lower bound of the conditional log-likelihood during training, and can reduce to a simple latent arithmetic method with additional assumption, which is surprisingly under-studied in the context of compositionality. We then derive a new guidance term which is shown to be crucial for maintaining the original semantics when doing manipulation. Unlike previous methods, our method is agnostic to pre-trained generative models and latent spaces, while still achieving competitive performance on compositional image generation as well as sequential manipulation of real and synthetic images.

## item_id: m_0689

TITLE: Bridge the Inference Gaps of Neural Processes via Expectation Maximization

ABSTRACT: The neural process (NP) is a family of computationally efficient models for learning distributions over functions. However, it suffers from under-fitting and shows suboptimal performance in practice. Researchers have primarily focused on incorporating diverse structural inductive biases, e.g. attention or convolution, in modeling. The topic of inference suboptimality and an analysis of the NP from the optimization objective perspective has hardly been studied in earlier work. To fix this issue, we propose a surrogate objective of the target log-likelihood of the meta dataset within the expectation maximization framework. The resulting model, referred to as the Self-normalized Importance weighted Neural Process (SI-NP), can learn a more accurate functional prior and has an improvement guarantee concerning the target log-likelihood. Experimental results show the competitive performance of SI-NP over other NPs objectives and illustrate that structural inductive biases, such as attention modules, can also augment our method to achieve SOTA performance.

## item_id: m_0690

TITLE: Feature-map-level Online Adversarial Knowledge Distillation

ABSTRACT: Feature maps contain rich information about image intensity and spatial correlation. However, previous online knowledge distillation methods only utilize the class probabilities. Thus in this paper, we propose an online knowledge distillation method that transfers not only the knowledge of the class probabilities but also that of the feature map using the adversarial training framework. We train multiple networks simultaneously by employing discriminators to distinguish the feature map distributions of different networks. Each network has its corresponding discriminator which discriminates the feature map from its own as fake while classifying that of the other network as real. By training a network to fool the corresponding discriminator, it can learn the other network’s feature map distribution. Discriminators and networks are trained concurrently in a minimax two-player game. Also, we propose a novel cyclic learning scheme for training more than two networks together. We have applied our method to various network architectures on the classification task and discovered a significant improvement of performance especially in the case of training a pair of a small network and a large one.

## item_id: m_0691

TITLE: 3D Neural Embedding Likelihood for Robust Sim-to-Real Transfer in Inverse Graphics

ABSTRACT: A central challenge in 3D scene perception via inverse graphics is robustly modeling the gap between 3D graphics and real-world data. We propose a novel 3D Neural Embedding Likelihood (3DNEL) over RGB-D images to address this gap. 3DNEL uses neural embeddings to predict 2D-3D correspondences from RGB and combines this with depth in a principled manner. 3DNEL is trained entirely from synthetic images and generalizes to real-world data. To showcase this capability, we develop a multi-stage inverse graphics pipeline that uses 3DNEL for 6D object pose estimation from real RGB-D images. Our method outperforms the previous state-of-the-art in sim-to-real pose estimation on the YCB-Video dataset, and improves robustness, with significantly fewer large-error predictions. Unlike existing bottom-up, discriminative approaches that are specialized for pose estimation, 3DNEL adopts a probabilistic generative formulation that jointly models multi-object scenes. This generative formulation enables easy extension of 3DNEL to additional tasks like object and camera tracking from video, using principled inference in the same probabilistic model without task specific retraining.

## item_id: m_0692

TITLE: Lossy Image Compression with Compressive Autoencoders

ABSTRACT: We propose a new approach to the problem of optimizing autoencoders for lossy image compression. New media formats, changing hardware technology, as well as diverse requirements and content types create a need for compression algorithms which are more flexible than existing codecs. Autoencoders have the potential to address this need, but are difficult to optimize directly due to the inherent non-differentiabilty of the compression loss. We here show that minimal changes to the loss are sufficient to train deep autoencoders competitive with JPEG 2000 and outperforming recently proposed approaches based on RNNs. Our network is furthermore computationally efficient thanks to a sub-pixel architecture, which makes it suitable for high-resolution images. This is in contrast to previous work on autoencoders for compression using coarser approximations, shallower architectures, computationally expensive methods, or focusing on small images.

## item_id: m_0693

TITLE: POLICY DRIVEN GENERATIVE ADVERSARIAL NETWORKS FOR ACCENTED SPEECH GENERATION

ABSTRACT: In this paper, we propose the generation of accented speech using generative adversarial
networks. Through this work we make two main contributions a) The
ability to condition latent representations while generating realistic speech samples
b) The ability to efficiently generate long speech samples by using a novel
latent variable transformation module that is trained using policy gradients. Previous
methods are limited in being able to generate only relatively short samples
or are not very efficient at generating long samples. The generated speech samples
are validated through a number of various evaluation measures viz, a WGAN
critic loss and through subjective scores on user evaluations against competitive
speech synthesis baselines and detailed ablation analysis of the proposed model.
The evaluations demonstrate that the model generates realistic long speech samples
conditioned on accent efficiently.

## item_id: m_0694

TITLE: Non-Synergistic Variational Autoencoders

ABSTRACT: Learning disentangling representations of the independent factors of variations that explain the data in an unsupervised setting is still a major challenge. In the following paper we address the task of disentanglement and introduce a new state-of-the-art approach called Non-synergistic variational Autoencoder (Non-Syn VAE). Our model draws inspiration from population coding, where the notion of synergy arises when we describe the encoded information by neurons in the form of responses from the stimuli. If those responses convey more information together than separate as independent sources of encoding information, they are acting synergetically. By penalizing the synergistic mutual information within the latents we encourage information independence and by doing that disentangle the latent factors. Notably, our approach could be added to the VAE framework easily, where the new ELBO function is still a lower bound on the log likelihood. In addition, we qualitatively compare our model with Factor VAE and show that this one implicitly minimises the synergy of the latents.

## item_id: m_0695

TITLE: Debiasing Evidence Approximations: On Importance-weighted Autoencoders and Jackknife Variational Inference

ABSTRACT: The importance-weighted autoencoder (IWAE) approach of Burda et al. defines a sequence of increasingly tighter bounds on the marginal likelihood of latent variable models. Recently, Cremer et al. reinterpreted the IWAE bounds as ordinary variational evidence lower bounds (ELBO) applied to increasingly accurate variational distributions. In this work, we provide yet another perspective on the IWAE bounds. We interpret each IWAE bound as a biased estimator of the true marginal likelihood where for the bound defined on $K$ samples we show the bias to be of order O(1/K). In our theoretical analysis of the IWAE objective we derive asymptotic bias and variance expressions. Based on this analysis we develop jackknife variational inference (JVI),
a family of bias-reduced estimators reducing the bias to $O(K^{-(m+1)})$ for any given m < K while retaining computational efficiency. Finally, we demonstrate that JVI leads to improved evidence estimates in variational autoencoders. We also report first results on applying JVI to learning variational autoencoders.

Our implementation is available at https://github.com/Microsoft/jackknife-variational-inference

## item_id: m_0696

TITLE: AR-ELBO: Preventing Posterior Collapse Induced by Oversmoothing in Gaussian VAE

ABSTRACT: Variational autoencoders (VAEs) often suffer from posterior collapse, which is a phenomenon that the learned latent space becomes uninformative. This is related to local optima introduced by a fixed hyperparameter resembling the data variance in the objective function. We suggest that this variance parameter regularizes the VAE and affects its smoothness, which is the magnitude of its gradient. An inappropriate choice of this parameter causes oversmoothness and leads to posterior collapse. This is shown theoretically by analysis on the linear approximated objective function and empirically in general cases. We propose AR-ELBO, which stands for adaptively regularized ELBO~(Evidence Lower BOund). It controls the strength of regularization by adapting the variance parameter, and thus avoids oversmoothing the model. Generation models trained by proposed objectives show improved Fréchet inception distance~(FID) of images generated from the MNIST and CelebA datasets.

## item_id: m_0697

TITLE: Dimension-Free Bounds for Low-Precision Training

ABSTRACT: Low-precision training is a promising way of decreasing the time and energy cost of training machine learning models.
Previous work has analyzed low-precision training algorithms, such as low-precision stochastic gradient descent, and derived theoretical bounds on their convergence rates.
These bounds tend to depend on the dimension of the model $d$ in that the number of bits needed to achieve a particular error bound increases as $d$ increases.
This is undesirable because a motivating application for low-precision training is large-scale models, such as deep learning, where $d$ can be huge.
In this paper, we prove dimension-independent bounds for low-precision training algorithms that use fixed-point arithmetic, which lets us better understand what affects the convergence of these algorithms as parameters scale.
Our methods also generalize naturally to let us prove new convergence bounds on low-precision training with other quantization schemes, such as low-precision floating-point computation and logarithmic quantization.

## item_id: m_0698

TITLE: Machine Unlearning For Alleviating Negative Transfer In Partial-Set Source-Free Unsupervised Domain Adaptation

ABSTRACT: Source-free Unsupervised Domain Adaptation (SFUDA) aims to adjust a source model trained on a labeled source domain to a related but unlabeled target domain without accessing the source data. Many SFUDA methods are studied in closed-set scenarios where the target domain and source domain categories are perfectly aligned. However, a more practical scenario is a partial-set scenario where the source label space subsumes the target one. In this paper, we prove that reducing the differences between the source and target domains in the partial-set scenario helps to achieve domain adaptation. And we propose a simple yet effective SFUDA framework called the Machine Unlearning Framework to alleviate the negative transfer problem in the partial-set scenario, thereby allowing the model to focus on the target domain category. Specifically, we first generate noise samples for each category that only exists in the source domain and generate pseudo-labeled samples from the target domain. Then, in the forgetting stage, we use these samples to train the model, making it behave like the model has never seen the class that only exists in the source domain before. Finally, in the adaptation stage, we use only the pseudo-labeled samples to conduct self-supervised training on the model, making it more adaptable to the target domain. Our method is easy to implement and pluggable, suitable for various pre-trained models. Experimental results show that our method can well alleviate the negative transfer problem and improve model performance under various target domain category settings.

## item_id: m_0699

TITLE: A Memory-augmented Neural Network by Resembling Human Cognitive Process of Memorization

ABSTRACT: Memorization of long-term information is a core task in sequence learning of neural networks, and inspired by human cognitive process, we propose a sparse memory-augmented neural network (SMANN) to deal with it in this paper, which is composed of a two-layer neural controller and an external memory. In the first layer of the network, the information is divided into segments according to a sparse mask, which preserve immediate memory, and then in the second layer, the segmented information are collected and processed as short-term memory. For alleviation of gradient vanishing problem, constrained LSTM structures are utilized in both of the layers to make the chrono-initializer more reasonable. Lastly, the external memory is used to store long-term information, and its access rate is reduced sharply owing to the sparse mask. In experiments, we evaluate the network and its components like constrained LSTM and the neural controller independently, results on different tasks has demonstrated the superiorities of our networks compared with their counterparts.

## item_id: m_0700

TITLE: Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning

ABSTRACT: In this work, we address the problem of large language model (LLM) unlearning, aiming to remove unwanted data influences and associated model capabilities e.g., copyrighted data or harmful content generation) while preserving essential model utilities, without the need for retraining from scratch. Despite the growing need for LLM unlearning, a principled optimization framework remains lacking. To this end, we revisit the state-of-the-art approach, negative preference optimization (NPO), and identify the issue of reference model bias, which could undermine NPO's effectiveness, particularly when unlearning forget data of varying difficulty.  Given that, we propose a simple yet effective unlearning optimization framework, called SimNPO, showing that  `simplicity' in removing the reliance on a reference model (through the lens of simple preference optimization) benefits unlearning. We also provide deeper insights into SimNPO's advantages, supported by analysis using mixtures of Markov chains. Furthermore, we present extensive experiments validating    SimNPO's superiority over existing unlearning baselines in benchmarks like TOFU and MUSE, and robustness against relearning  attacks.
