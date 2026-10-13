# Batch 02 — 100 items

## item_id: m_0101

TITLE: Non-Equilibrium Dynamics of Hybrid Continuous-Discrete Ground-State Sampling

ABSTRACT: We propose a general framework for a hybrid continuous-discrete algorithm that integrates continuous-time deterministic dynamics with Metropolis-Hastings (MH) steps to combine search dynamics that either preserve or break detailed balance. Our purpose is to study the non-equilibrium dynamics that leads to the ground state of rugged energy landscapes in this general setting. Our results show that MH-driven dynamics reach ``easy'' ground states more quickly, indicating a stronger bias toward these solutions in algorithms using reversible transition probabilities. To validate this, we construct a set of Ising problem instances with a controllable bias in the energy landscape that makes certain degenerate solutions more accessible than others. The constructed hybrid algorithm demonstrates significant improvements in convergence and ground-state sampling accuracy, achieving a 100x speedup on GPU compared to simulated annealing, making it well-suited for large-scale applications.

## item_id: m_0102

TITLE: RAPID: Retrieval Augmented Training of Differentially Private Diffusion Models

ABSTRACT: Differentially private diffusion models (DPDMs) harness the remarkable generative capabilities of diffusion models while enforcing differential privacy (DP) for sensitive data. However, existing DPDM training approaches often suffer from significant utility loss, large memory footprint, and expensive inference cost, impeding their practical uses.  
To overcome such limitations, we present RAPID: Retrieval Augmented PrIvate Diffusion model, a novel approach that integrates retrieval augmented generation (RAG) into DPDM training. Specifically, RAPID leverages available public data to build a knowledge base of sample trajectories; when training the diffusion model on private data, RAPID computes the early sampling steps as queries, retrieves similar trajectories from the knowledge base as surrogates, and focuses on training the later sampling steps in a differentially private manner. Extensive evaluation using benchmark datasets and models demonstrates that, with the same privacy guarantee, RAPID significantly outperforms state-of-the-art approaches by large margins in generative quality, memory footprint, and inference cost, suggesting that retrieval-augmented DP training represents a promising direction for developing future privacy-preserving generative models. The code is available at:  https://github.com/TanqiuJiang/RAPID

## item_id: m_0103

TITLE: Dense Morphological Network: An Universal Function Approximator

ABSTRACT: Artificial neural networks are built on the basic operation of linear combination and non-linear activation function. Theoretically this structure can approximate any continuous function with three layer architecture. But in practice learning  the parameters of such network can be hard. Also the choice of activation function can greatly impact the performance of the network. In this paper we are proposing to replace the basic linear combination operation with non-linear operations that do away with the need of additional non-linear activation function. To this end we are proposing the use of elementary  morphological operations (dilation and erosion) as the basic operation in neurons. We show that these networks (Denoted as Morph-Net) with morphological operations can approximate any smooth function requiring less number of parameters than what is necessary for normal neural networks. The results show that our network perform favorably when compared with similar structured network. We have carried out our experiments on  MNIST, Fashion-MNIST, CIFAR10 and CIFAR100.

## item_id: m_0104

TITLE: Multi-Resolution Continuous Normalizing Flows

ABSTRACT: Recent work has shown that Neural Ordinary Differential Equations (ODEs) can serve as generative models of images using the perspective of Continuous Normalizing Flows (CNFs). Such models offer exact likelihood calculation, and invertible generation/density estimation. In this work we introduce a Multi-Resolution variant of such models (MRCNF), by characterizing the conditional distribution over the additional information required to generate a fine image that is consistent with the coarse image. We introduce a transformation between resolutions that allows for no change in the log likelihood. We show that this approach yields comparable likelihood values for various image datasets, using orders of magnitude fewer parameters than the prior methods, in significantly less training time, using only one GPU.

## item_id: m_0105

TITLE: Stochastic Hyperparameter Optimization through Hypernetworks

ABSTRACT: Machine learning models are usually tuned by nesting optimization of model weights inside the optimization of hyperparameters.  We give a method to collapse this nested optimization into joint stochastic optimization of both weights and hyperparameters.  Our method trains a neural network to output approximately optimal weights as a function of hyperparameters.  We show that our method converges to locally optimal weights and hyperparameters for sufficiently large hypernets.  We compare this method to standard hyperparameter optimization strategies and demonstrate its effectiveness for tuning thousands of hyperparameters.

## item_id: m_0106

TITLE: DeepCoder: Learning to Write Programs

ABSTRACT: We develop a first line of attack for solving programming competition-style problems from input-output examples using deep learning. The approach is to train a neural network to predict properties of the program that generated the outputs from the inputs. We use the neural network's predictions to augment search techniques from the programming languages community, including enumerative search and an SMT-based solver. Empirically, we show that our approach leads to an order of magnitude speedup over the strong non-augmented baselines and a Recurrent Neural Network approach, and that we are able to solve problems of difficulty comparable to the simplest problems on programming competition websites.

## item_id: m_0107

TITLE: Global Optimality Conditions for Deep Neural Networks

ABSTRACT: We study the error landscape of deep linear and nonlinear neural networks with the squared error loss. Minimizing the loss of a deep linear neural network is a nonconvex problem, and despite recent progress, our understanding of this loss surface is still incomplete. For deep linear networks, we present necessary and sufficient conditions for a critical point of the risk function to be a global minimum. Surprisingly, our conditions provide an efficiently checkable test for global optimality, while such tests are typically intractable in nonconvex optimization. We further extend these results to deep nonlinear neural networks and prove similar sufficient conditions for global optimality, albeit in a more limited function space setting.

## item_id: m_0108

TITLE: Language Modeling with Graph Temporal Convolutional Networks

ABSTRACT: Recently, there have been some attempts to use non-recurrent neural models for language modeling. 
However, a noticeable performance gap still remains. 
We propose a non-recurrent neural language model, dubbed graph temporal convolutional network (GTCN), that relies on graph neural network blocks and convolution operations. While the standard recurrent neural network language models encode sentences sequentially without modeling higher-level structural information, our model regards sentences as graphs and processes input words within a message propagation framework, aiming to learn better syntactic information by inferring skip-word connections. Specifically, the graph network blocks operate in parallel and learn the underlying graph structures in sentences without any additional annotation pertaining to structure knowledge. Experiments demonstrate that the model without recurrence can achieve comparable perplexity results in language modeling tasks and successfully learn syntactic information.

## item_id: m_0109

TITLE: From Global Assessment to Local Selection: Efficiently Solving Traveling Salesman Problems of All Sizes

ABSTRACT: The Traveling Salesman Problem (TSP) is a well-known combinatorial optimization problem with broad real-world applications. Recent advancements in neural network-based TSP solvers have shown promising results. Nonetheless, these models often struggle to efficiently solve both small- and large-scale TSPs using the same set of pre-trained model parameters, limiting their practical utility. To address this issue, we introduce a novel neural TSP solver named GELD, built upon our proposed broad global assessment and refined local selection framework. Specifically, GELD integrates a lightweight Global-view Encoder (GE) with a heavyweight Local-view Decoder (LD) to enrich embedding representation while accelerating the decision-making process. Moreover, GE incorporates a novel low-complexity attention mechanism, allowing GELD to achieve low inference latency and scalability to larger-scale TSPs. Additionally, we propose a two-stage training strategy that utilizes training instances of different sizes to bolster GELD's generalization ability. Extensive experiments conducted on both synthetic and real-world datasets demonstrate that GELD outperforms seven state-of-the-art models considering both solution quality and inference speed. Furthermore, GELD can be employed as a post-processing method to exchange affordable computing time for significantly improved solution quality, capable of solving TSPs with up to 744,710 nodes without relying on divide-and-conquer strategies.

## item_id: m_0110

TITLE: Modeling Complex Mathematical Reasoning via Large Language Model based MathAgent

ABSTRACT: Large language models (LLMs) face challenges in solving complex mathematical problems that require comprehensive capacities to parse the statements, associate domain knowledge, perform compound logical reasoning, and integrate the intermediate rationales. Tackling all these problems once could be arduous for LLMs, thus leading to confusion in generation. In this work, we explore the potential of enhancing LLMs with agents by meticulous decomposition and modeling of mathematical reasoning process. Specifically, we propose a formal description of the mathematical solving and extend LLMs with an agent-based zero-shot framework named \textbf{P}lanner-\textbf{R}easoner-\textbf{E}xecutor-\textbf{R}eflector (PRER). We further provide and implement two MathAgents that define the logical forms and inherent relations via a pool of actions in different grains and orientations: MathAgent-M adapts its actions to LLMs, while MathAgent-H aligns with humankind. Experiments on miniF2F and MATH have demonstrated the effectiveness of PRER and proposed MathAgents, achieving an increase of 12.3% (53.9%$\rightarrow$66.2%) on MiniF2F, 9.2% (49.8%$\rightarrow$59.0%) on MATH, and 13.2% (23.2%$\rightarrow$35.4%) for level-5 problems of MATH against GPT-4. Further analytical results provide more insightful perspectives on exploiting the behaviors of LLMs as agents.

## item_id: m_0111

TITLE: Deconstructing the Regularization of BatchNorm

ABSTRACT: Batch normalization (BatchNorm) has become a standard technique in deep learning. Its popularity is in no small part due to its often positive effect on generalization. Despite this success, the regularization effect of the technique is still poorly understood. This study aims to decompose BatchNorm into separate mechanisms that are much simpler. We identify three effects of BatchNorm and assess their impact directly with ablations and interventions. Our experiments show that preventing explosive growth at the final layer at initialization and during training can recover a large part of BatchNorm's generalization boost. This regularization mechanism can lift accuracy by $2.9\%$ for Resnet-50 on Imagenet without BatchNorm. We show it is linked to other methods like Dropout and recent initializations like Fixup. Surprisingly, this simple mechanism matches the improvement of $0.9\%$ of the more complex Dropout regularization for the state-of-the-art Efficientnet-B8 model on Imagenet. This demonstrates the underrated effectiveness of simple regularizations and sheds light on directions to further improve generalization for deep nets.

## item_id: m_0112

TITLE: Identifiable State Disentanglement for Reinforcement Learning with Policy Optimality

ABSTRACT: Recent progress in reinforcement learning (RL) has demonstrated significant efficacy in the optimization of policies, in the presence of noise. These works, however, neglect the importance of independence between signal and noise in latent space, resulting in limited performance. To address this concern, we first analyze the identifiability result of latent signal and latent noise, which implicitly highlights that the independence between latent signal and latent noise is crucial in RL. We then convert the identifiability result into a novel method, which isolates signal from noise in latent space, by effectively integrating structural independence and statistical independence into a unified framework. Structurally, the proposed method respectively employs two different decoders on latent signal and latent noise, so that each decoder captures exclusive features specific to its own space. Statistically, the independence between latent signal and latent noise is enforced by a correlation-coefficients objective. Experiments on extensive benchmark control tasks demonstrate that the proposed approach surpasses existing algorithms in effectively disentangling signals from noise.

## item_id: m_0113

TITLE: Weighted Empirical Risk Minimization: Transfer Learning based on Importance Sampling

ABSTRACT: We consider statistical learning problems, when the distribution $P'$ of the training observations $Z'_1,\; \ldots,\; Z'_n$ differs from the distribution $P$ involved in the risk one seeks to minimize (referred to as the \textit{test distribution}) but is still defined on the same measurable space as $P$ and dominates it. In the unrealistic case where the likelihood ratio $\Phi(z)=dP/dP'(z)$ is known, one may straightforwardly extends the Empirical Risk Minimization (ERM) approach to this specific \textit{transfer learning} setup using the same idea as that behind Importance Sampling, by minimizing a weighted version of the empirical risk functional computed from the 'biased' training data $Z'_i$ with weights $\Phi(Z'_i)$. Although the \textit{importance function} $\Phi(z)$ is generally unknown in practice, we show that, in various situations frequently encountered in practice, it takes a simple form and can be directly estimated from the $Z'_i$'s and some auxiliary information on the statistical population $P$. By means of linearization techniques, we then prove that the generalization capacity of the approach aforementioned is preserved when plugging the resulting estimates of the $\Phi(Z'_i)$'s into the  weighted empirical risk. Beyond these theoretical guarantees, numerical results provide strong empirical evidence of the relevance of the approach promoted in this article.

## item_id: m_0114

TITLE: Grounded Contrastive Learning for Open-world Semantic Segmentation

ABSTRACT: Contrastive learning (CL) with large-scale image-text paired data has made great strides in open-world image recognition. The progress raises attraction to open-world semantic segmentation---aiming at learning to segment arbitrary visual concepts in images. Existing open-world segmentation methods adopt CL to learn diverse visual concepts and adapt its image-level understanding to the segmentation task. However, while CL-based existing methods have shown impressive results, conventional CL is limited in considering image-text level alignment without explicit optimization of region-text level alignment, thus leading to a sub-optimal solution for the segmentation task. In this paper, we propose a novel Grounded Contrastive Learning (GCL) framework to directly align a text and regions described by the text. Our method generates a segmentation mask associated with a given text, extracts grounded image embedding from the masked image region, and aligns it with text embedding via GCL. The framework encourages a model to directly improve the quality of generated segmentation masks. In addition, for a rigorous and fair comparison, we present a unified evaluation protocol with widely used 8 semantic segmentation datasets. GCL achieves state-of-the-art zero-shot segmentation performance with large margins in all datasets. The code will be released publicly available.

## item_id: m_0115

TITLE: Detecting Noisy Training Data with Loss Curves

ABSTRACT: This paper introduces a new method to discover mislabeled training samples and to mitigate their impact on the training process of deep networks. At the heart of our algorithm lies the Area Under the Loss (AUL) statistic, which can be easily computed for each sample in the training set. We show that the AUL can use training dynamics to differentiate between (clean) samples that benefit from generalization and (mislabeled) samples that need to be “memorized”. We demonstrate that the estimated AUL score conditioned on clean vs. noisy is approximately Gaussian distributed and can be well estimated with a simple Gaussian Mixture Model (GMM). The resulting GMM provides us with mixing coefficients that reveal the percentage of mislabeled samples in a data set as well as probability estimates that each individual training sample is mislabeled. We show that these probability estimates can be used to down-weight suspicious training samples and successfully alleviate the damaging impact of label noise. We demonstrate on the CIFAR10/100 datasets that our proposed approach is significantly more accurate and consistent across model architectures than all prior work.

## item_id: m_0116

TITLE: Testing For Typicality with Respect to an Ensemble of Learned Distributions

ABSTRACT: Good methods of performing anomaly detection on high-dimensional data sets are
needed, since algorithms which are trained on data are only expected to perform
well on data that is similar to the training data. There are theoretical results on the
ability to detect if a population of data is likely to come from a known base distribution, 
which is known as the goodness-of-fit problem, but those results require
knowing a model of the base distribution. The ability to correctly reject anomalous
data hinges on the accuracy of the model of the base distribution. For high dimensional 
data, learning an accurate-enough model of the base distribution such that
anomaly detection works reliably is very challenging, as many researchers have
noted in recent years. Existing methods for the goodness-of-fit problem do not ac-
count for the fact that a model of the base distribution is learned. To address that
gap, we offer a theoretically motivated approach to account for the density learning 
procedure. In particular, we propose training an ensemble of density models,
considering data to be anomalous if the data is anomalous with respect to any
member of the ensemble. We provide a theoretical justification for this approach,
proving first that a test on typicality is a valid approach to the goodness-of-fit
problem, and then proving that for a correctly constructed ensemble of models,
the intersection of typical sets of the models lies in the interior of the typical set
of the base distribution. We present our method in the context of an example on
synthetic data in which the effects we consider can easily be seen.

## item_id: m_0117

TITLE: Pseudo Numerical Methods for Diffusion Models on Manifolds

ABSTRACT: Denoising Diffusion Probabilistic Models (DDPMs) can generate high-quality samples such as image and audio samples. However, DDPMs require hundreds to thousands of iterations to produce a sample. Several prior works have successfully accelerated DDPMs through adjusting the variance schedule (e.g., Improved Denoising Diffusion Probabilistic Models) or the denoising equation (e.g., Denoising Diffusion Implicit Models (DDIMs)). However, these acceleration methods cannot maintain the quality of samples and even introduce new noise at high speedup rate, which limit their practicability. To accelerate the inference process while keeping the sample quality, we provide a new perspective that DDPMs should be treated as solving differential equations on manifolds. Under such a perspective, we propose pseudo numerical methods for diffusion models (PNDMs). Specifically, we figure out how to solve differential equations on manifolds and show that DDIMs are simple cases of pseudo numerical methods. We change several classical numerical methods to corresponding pseudo numerical methods and find that pseudo linear multi-step method is the best method in most situations. According to our experiments, by directly using pre-trained models on Cifar10, CelebA and LSUN, PNDMs can generate higher quality synthetic images with only 50 steps compared with 1000-step DDIMs (20x speedup), significantly outperform DDIMs with 250 steps (by around 0.4 in FID) and have good generalization on different variance schedules.

## item_id: m_0118

TITLE: Improved Detection of Adversarial Attacks via Penetration Distortion Maximization

ABSTRACT: This paper is concerned with the defense of deep models against adversarial at-
tacks. We develop an adversarial detection method, which is inspired by the cer-
tificate defense approach, and captures the idea of separating class clusters in the
embedding space so as to increase the margin. The resulting defense is intuitive,
effective, scalable and can be integrated into any given neural classification model.
Our method demonstrates state-of-the-art detection performance under all threat
models.

## item_id: m_0119

TITLE: On the Landscape of Sparse Linear Networks

ABSTRACT: Network pruning, or sparse network has a long history and practical significance in modern applications. Although the loss functions of neural networks may yield bad landscape due to non-convexity, we focus on linear activation which already owes benign landscape. With no unrealistic assumption, we conclude the following statements for the squared loss objective of general sparse linear neural networks: 1) every local minimum is a global minimum for scalar output with any sparse structure, or non-intersected sparse first layer and dense other layers with orthogonal training data; 2) sparse linear networks have sub-optimal local-min for only sparse first layer due to low rank constraint, or output larger than three dimensions due to the global minimum of a sub-network. Overall, sparsity breaks the normal structure, cutting out the decreasing path in original fully-connected networks.

## item_id: m_0120

TITLE: Controllable Data Generation via Iterative Data-Property Mutual Mappings

ABSTRACT: Deep generative models have been widely used for their ability to generate realistic data samples in various areas, such as images, molecules, text, and speech. One major goal of data generation is controllability, namely to generate new data with desired properties. Despite growing interest in the area of controllable generation, significant challenges still remain, including 1) Disentangling desired properties with unrelated latent variables, 2) out-of-distribution property control, and 3) objective optimization for out-of-distribution property control. To address these challenges, in this paper, we propose a general framework to enhance VAE-based data generators with property controllability and disentanglement ensure. Our proposed objective can be optimized on both data seen and unseen in the training set. We propose a training procedure to train the objective in a semi-supervised manner by iteratively conducting mutual mappings between the data and properties. The proposed framework is implemented on four VAE-based controllable generators to evaluate its performance on property error, disentanglement performance, generation quality, and training time. The results indicate that our proposed framework enables more precise control over the properties of generated samples in a short training time, ensuring the disentanglement stated above and keeping the validity of the generated samples.

## item_id: m_0121

TITLE: Zero-shot Cross Language Text Classification

ABSTRACT: Labeled text classification datasets are typically only available in a few select languages. In order to train a model for e.g news categorization in a language $L_t$ without a suitable text classification dataset there are two options. The first option is to create a new labeled dataset by hand, and the second option is to transfer label information from an existing labeled dataset in a source language $L_s$ to the target language $L_t$. In this paper we propose a method for sharing label information across languages by means of a language independent text encoder. The encoder will give almost identical representations to multilingual versions of the same text. This means that labeled data in one language can be used to train a classifier that works for the rest of the languages. The encoder is trained independently of any concrete classification task and can therefore subsequently be used for any classification task.  We show that it is possible to obtain good performance even in the case where only a comparable corpus of texts is available. 

## item_id: m_0122

TITLE: Learning to Cooperate with Humans through Theory-Informed Trust Beliefs

ABSTRACT: Real-world human--AI cooperation is challenging due to the wide range of interests and capabilities that each party brings. To maximize joint performance, cooperative AI must adapt its policies to the competence and incentives of its specific human partner. Prevailing approaches address this challenge by training on human data or simulated partners. In this paper, we pursue an orthogonal approach: grounded on theory from social science, we hypothesize that equipping agents with human-like trust beliefs enables them to adapt to human partners more effectively. We formulate the cooperative agent's problem as TrustPOMDP, a variant of POMDPs, and develop a trust model that captures three key factors known to shape human trust beliefs: ability, benevolence, and integrity (ABI). A key advantage of the approach is that it only requires minimal modifications to a POMDP agent. TrustPOMDPs can be trained with real or simulated partners, provided sufficient diversity in the three dimensions. Results from both simulated and human-subject experiments (N=106) show that TrustPOMDP-based agents adapt more rapidly and effectively to various partners, while baselines methods tend to over- or undertrust, reducing team performance. These findings highlight the promise of incorporating social science-informed trust models into RL agents to advance collaboration with humans.

## item_id: m_0123

TITLE: AestheticNet: Reducing bias in facial data sets under ethical considerations

ABSTRACT: Facial Beauty Prediction (FBP) aims to develop a machine that can automatically evaluate facial attractiveness. Usually, these results were highly correlated with human ratings, and therefore also reflected human bias in annotations. Everyone will have biases that are usually subconscious and not easy to notice. Unconscious bias deserves more attention than explicit discrimination. It affects moral judgement and can evade moral responsibility, and we cannot eliminate it completely. A new challenge for scientists is to provide training data and AI algorithms that can withstand distorted information. Our experiments prove that human aesthetic judgements are usually biased. In this work, we introduce AestheticNet, the most advanced attractiveness prediction network, with a Pearson correlation coefficient of 0.9601, which is significantly better than the competition. This network is then used to enrich the training data with synthetic images in order to overwrite the ground truth values with fair assessments.
We propose a new method to generate an unbiased CNN to improve the fairness of machine learning. Prediction and recommender systems based on Artificial Intelligence (AI) technology are widely used in various sectors of industry, such as intelligent recruitment, security, etc. Therefore, their fairness is very important. Our research provides a practical example of how to build a fair and trustable AI.

## item_id: m_0124

TITLE: Fast Conditional Intervention in Algorithmic Recourse with Reinforcement Learning

ABSTRACT: Explaining the decisions made by machine learning classifiers aids individuals in identifying critical factors and charting future plans. Recent studies have shown that incorporating causal graphs of input features provides more realistic explanations; however, this also introduces new challenges such as handling noisy graphs and efficiently performing inference with black-box classifiers. In this work, we tackle these issues by presenting an efficient reinforcement learning (RL)-based approach with an idea of conditional intervention. Our intervention method is theoretically preferable and considers both feature dependencies and incompleteness of graphs. Simultaneously, the RL-based method offers the capacity to learn the intervention process while guarantees computational complexity at inference stage. In the experiments, we showcase the efficiency and superior performance of our solution when compared to baseline methods on both synthetic and real datasets.

## item_id: m_0125

TITLE: KITE: A Kernel-based Improved Transferability Estimation Method

ABSTRACT: Transferability estimation has emerged as an important problem in transfer learning. A transferability estimation method takes as inputs a set of pre-trained models and decides which pre-trained model can deliver the best transfer learning performance. Existing methods tackle this problem by analyzing the output of the pre-trained model or by comparing the pre-trained model with a probe model trained on the target dataset. However, neither is sufficient to provide reliable and efficient transferability estimations. In this paper, we present a novel perspective and introduce \textsc{Kite}, as a \underline{K}ernel-based \underline{I}mproved \underline{T}ransferability \underline{E}stimation method. \textsc{Kite} is based on the key observations that the separability of the pre-trained features and the similarity of the pre-trained features to random features are two important factors for estimating transferability. Inspired by kernel methods, \textsc{Kite} adopts \emph{centered kernel alignment} as an effective way to assess feature separability and feature similarity. \textsc{Kite} is easy to interpret, fast to compute, and robust to the target dataset size. We evaluate the performance of \textsc{Kite} on a recently introduced large-scale model selection benchmark. The benchmark contains 8 source dataset, 6 target datasets and 4 architectures with a total of 32 pre-trained models. Extensive results show that \textsc{Kite} outperforms existing methods by a large margin for transferability estimation.

## item_id: m_0126

TITLE: Censoring Representations with Multiple-Adversaries over Random Subspaces

ABSTRACT: Adversarial feature learning (AFL) is one of the promising ways for explicitly constrains neural networks to learn desired representations; for example, AFL could help to learn anonymized representations so as to avoid privacy issues. AFL learn such a representations by training the networks to deceive the adversary that predict the sensitive information from the network, and therefore, the success of the AFL heavily relies on the choice of the adversary. This paper proposes a novel design of the adversary, {\em multiple adversaries over random subspaces} (MARS) that instantiate the concept of the {\em volunerableness}. The proposed method is motivated by an assumption that deceiving an adversary could fail to give meaningful information if the adversary is easily fooled, and adversary rely on single classifier suffer from this issues. 
In contrast, the proposed method is designed to be less vulnerable, by utilizing the ensemble of independent classifiers where each classifier tries to predict sensitive variables from a different {\em subset} of the representations. 
The empirical validations on three user-anonymization tasks show that our proposed method achieves state-of-the-art performances in all three datasets without significantly harming the utility of data. 
This is significant because it gives new implications about designing the adversary, which is important to improve the performance of AFL. 

## item_id: m_0127

TITLE: Cross-Modal Few-Shot Learning: a Generative Transfer Learning Framework

ABSTRACT: Most existing studies on few-shot learning focus on unimodal settings, where models are trained to generalize on unseen data using only a small number of labeled examples from the same modality. However, real-world data are inherently multi-modal, and unimodal approaches limit the practical applications of few-shot learning. To address this gap, this paper introduces the Cross-modal Few-Shot Learning (CFSL) task, which aims to recognize instances from multiple modalities when only a few labeled examples are available. 
This task presents additional challenges compared to classical few-shot learning due to the distinct visual characteristics and structural properties unique to each modality. To tackle these challenges, we propose a Generative Transfer Learning (GTL) framework consisting of two stages: the first stage involves training on abundant unimodal data, and the second stage focuses on transfer learning to adapt to novel data. Our GTL framework jointly estimates the latent shared concept across modalities and in-modality disturbance in both stages, while freezing the generative module during the transfer phase to maintain the stability of the learned representations and prevent overfitting to the limited multi-modal samples. Our finds demonstrate that GTL has superior performance compared to state-of-the-art methods across four distinct multi-modal datasets: Sketchy, TU-Berlin, Mask1K, and SKSF-A. Additionally, the results suggest that the model can estimate latent concepts from vast unimodal data and generalize these concepts to unseen modalities using only a limited number of available samples, much like human cognitive processes.

## item_id: m_0128

TITLE: A Fairness Analysis on Differentially Private Aggregation of Teacher Ensembles

ABSTRACT: Private Aggregation of Teacher Ensembles (PATE) is an important
private machine learning framework. It combines multiple
learning models used as teachers for a student model that
learns to predict an output chosen by noisy voting among the
teachers. The resulting model satisfies differential privacy and has
been shown effective in learning high-quality private models in
semi-supervised settings or when one wishes to protect the data
labels.

This paper asks whether this privacy-preserving framework introduces
or exacerbates unfairness and shows that PATE can introduce
accuracy disparity among individuals and groups of individuals. 
The paper analyzes
which algorithmic and data properties are responsible for the
disproportionate impacts, why these aspects are affecting different
groups disproportionately, and proposes guidelines to mitigate these
effects.

## item_id: m_0129

TITLE: Localized Generations with Deep Neural Networks for Multi-Scale Structured Datasets

ABSTRACT: Extracting the hidden structure of the external environment is an essential component of intelligent agents and human learning. The real-world datasets that we are interested in are often characterized by the locality: the change in the structural relationship between the data points depending on location in observation space. The local learning approach extracts semantic representations for these datasets by training the embedding model from scratch for each local neighborhood, respectively. However, this approach is only limited to use with a simple model, since the complex model, including deep neural networks, requires a massive amount of data and extended training time. In this study, we overcome this trade-off based on the insight that the real-world dataset often shares some structural similarity between each neighborhood. We propose to utilize the embedding model for the other local structure as a weak form of supervision. Our proposed model, the Local VAE, generalize the Variational Autoencoder to have the different model parameters for each local subset and train these local parameters by the gradient-based meta-learning. Our experimental results showed that the Local VAE succeeded in learning the semantic representations for the dataset with local structure, including the 3D Shapes Dataset, and generated high-quality images.

## item_id: m_0130

TITLE: Deep exploration by novelty-pursuit with maximum state entropy

ABSTRACT: Efficient exploration is essential to reinforcement learning in huge state space. Recent approaches to address this issue include the intrinsically motivated goal exploration process (IMGEP) and the maximum state entropy exploration (MSEE). In this paper, we disclose that goal-conditioned exploration behaviors in IMGEP can also maximize the state entropy, which bridges the IMGEP and the MSEE. From this connection, we propose a maximum entropy criterion for goal selection in goal-conditioned exploration, which results in the new exploration method novelty-pursuit. Novelty-pursuit performs the exploration in two stages: first, it selects a goal for the goal-conditioned exploration policy to reach the boundary of the explored region; then, it takes random actions to explore the non-explored region. We demonstrate the effectiveness of the proposed method in environments from simple maze environments, Mujoco tasks, to the long-horizon video game of SuperMarioBros. Experiment results show that the proposed method outperforms the state-of-the-art approaches that use curiosity-driven exploration.

## item_id: m_0131

TITLE: Vocabulary Selection Strategies for Neural Machine Translation

ABSTRACT: Classical translation models constrain the space of possible outputs by selecting a subset of translation rules based on the input sentence. Recent work on improving the efficiency of neural translation models adopted a similar strategy by restricting the output vocabulary to a subset of likely candidates given the source. In this paper we experiment with context and embedding-based selection methods and extend previous work by examining speed and accuracy trade-offs in more detail. We show that decoding time on CPUs can be reduced by up to 90% and training time by 25% on the WMT15 English-German and WMT16 English-Romanian tasks at the same or only negligible change in accuracy. This brings the time to decode with a state of the art neural translation system to just over 140 words per seconds on a single CPU core for English-German.

## item_id: m_0132

TITLE: LEARNING TO SHARE: SIMULTANEOUS PARAMETER TYING AND SPARSIFICATION IN DEEP LEARNING

ABSTRACT: Deep neural networks (DNNs) usually contain millions, maybe billions, of parameters/weights, making both storage and computation very expensive. This has motivated a large body of work to reduce the complexity of the neural network by using sparsity-inducing regularizers.  Another well-known approach for controlling the complexity of DNNs is parameter sharing/tying, where certain sets of weights are forced to share a common value. Some forms of weight sharing are hard-wired to express certain in- variances, with a notable example being the shift-invariance of convolutional layers. However, there may be other groups of weights that may be tied together during the learning process, thus further re- ducing the complexity of the network. In this paper, we adopt a recently proposed sparsity-inducing regularizer, named GrOWL (group ordered weighted l1), which encourages sparsity and, simulta- neously, learns which groups of parameters should share a common value. GrOWL has been proven effective in linear regression, being able to identify and cope with strongly correlated covariates. Unlike standard sparsity-inducing regularizers (e.g., l1 a.k.a. Lasso), GrOWL not only eliminates unimportant neurons by setting all the corresponding weights to zero, but also explicitly identifies strongly correlated neurons by tying the corresponding weights to a common value. This ability of GrOWL motivates the following two-stage procedure: (i) use GrOWL regularization in the training process to simultaneously identify significant neurons and groups of parameter that should be tied together; (ii) retrain the network, enforcing the structure that was unveiled in the previous phase, i.e., keeping only the significant neurons and enforcing the learned tying structure. We evaluate the proposed approach on several benchmark datasets, showing that it can dramatically compress the network with slight or even no loss on generalization performance.


## item_id: m_0133

TITLE: Meta-Transformer: A Unified Framework for Multimodal Learning

ABSTRACT: Multimodal learning aims to build models that can process and relate information from multiple modalities. Despite years of development in this field, it still remains challenging to design a unified network for processing various modalities ($\textit{e.g.}$ natural language, 2D images, 3D point clouds, audio, video, time series, tabular data) due to the inherent gaps among them. In this work, we propose a framework, named Meta-Transformer, that leverages a $\textbf{frozen}$ encoder to perform multimodal perception without any paired multimodal training data. In Meta-Transformer, the raw input data from various modalities are mapped into a shared token space, allowing a subsequent encoder with frozen parameters to extract high-level semantic features of the input data. Composed of three main components: a unified data tokenizer, a modality-shared encoder, and task-specific heads for downstream tasks, Meta-Transformer is the first framework to perform unified learning across 12 modalities with unpaired data. Experiments on different benchmarks reveal that Meta-Transformer can handle a wide range of tasks including fundamental perception (text, image, point cloud, audio, video), practical application (X-Ray, infrared, hyperspectral, and IMU), and data mining (graph, tabular, and time-series). Meanwhile, it also excels in multimodal understanding on cross-modal retrieval, referring segmentation, and grounding tasks. Meta-Transformer indicates a promising future for developing unified multimodal intelligence with transformers. We will release well-documented code and pretrained weights soon.

## item_id: m_0134

TITLE: Unsupervised Deep Structure Learning by Recursive Dependency Analysis

ABSTRACT: We introduce an unsupervised structure learning algorithm for deep, feed-forward, neural networks. We propose a new interpretation for depth and inter-layer connectivity where a hierarchy of independencies in the input distribution is encoded in the network structure. This results in structures allowing neurons to connect to neurons in any deeper layer skipping intermediate layers. Moreover, neurons in deeper layers encode low-order (small condition sets) independencies and have a wide scope of the input, whereas neurons in the first layers encode higher-order (larger condition sets) independencies and have a narrower scope. Thus, the depth of the network is automatically determined---equal to the maximal order of independence in the input distribution, which is the recursion-depth of the algorithm. The proposed algorithm constructs two main graphical models: 1) a generative latent graph (a deep belief network) learned from data and 2) a deep discriminative graph constructed from the generative latent graph. We prove that conditional dependencies between the nodes in the learned generative latent graph are preserved in the class-conditional discriminative graph. Finally, a deep neural network structure is constructed based on the discriminative graph. We demonstrate on image classification benchmarks that the algorithm replaces the deepest layers (convolutional and dense layers) of common convolutional networks, achieving high classification accuracy, while constructing significantly smaller structures. The proposed structure learning algorithm requires a small computational cost and runs efficiently on a standard desktop CPU.

## item_id: m_0135

TITLE: Variational Lossy Autoencoder

ABSTRACT: Representation learning seeks to expose certain aspects of observed data in a learned representation that's amenable to downstream tasks like classification. 
For instance, a good representation for 2D images might be one that describes only global structure and discards information about detailed texture. 
In this paper, we present a simple but principled method to learn such global representations by combining Variational Autoencoder (VAE) with neural autoregressive models such as RNN, MADE and PixelRNN/CNN. 
Our proposed VAE model allows us to have control over what the global latent code can learn and , by designing the architecture accordingly, we can force the global latent code to discard irrelevant information such as texture in 2D images, and hence the code only ``autoencodes'' data in a lossy fashion.
In addition, by leveraging autoregressive models as both prior distribution $p(z)$ and decoding distribution $p(x|z)$, we can greatly improve generative modeling performance of VAEs, achieving new state-of-the-art results on MNIST, OMNIGLOT and Caltech-101 as well as competitive results on CIFAR10.  


## item_id: m_0136

TITLE: Multi-Task Learning by a Top-Down Control Network

ABSTRACT: As the range of tasks performed by a general vision system expands, executing multiple tasks accurately and efﬁciently in  a single network has become an important and still open problem. Recent computer vision approaches address this problem by branching networks, or by a channel-wise modulation of the network feature-maps with task speciﬁc vectors. We present a novel architecture that uses a dedicated top-down control network to modify the activation of all the units in the main recognition network in a manner that depends on the selected task, image content, and spatial location. We show the effectiveness of our scheme by achieving signiﬁcantly better results than alternative state-of-the-art approaches on four datasets. We further demonstrate our advantages in terms of task selectivity, scaling the number of tasks and interpretability. 
Code is supplied in the supplementary materials and will be publicly available.

## item_id: m_0137

TITLE: Inverse Problems in Computer Vision using  Adversarial  Imagination Priors

ABSTRACT: Given an image,  humans  effortlessly run the image formation process backwards in their minds: they can tell albedo from shading,  foreground from background, and imagine the occluded parts of the scene behind foreground objects. In this work, we propose a weakly supervised inversion machine trained to generate similar imaginations that when rendered using differentiable, graphics-like decoders, produce the original visual input. We constrain the imagination spaces by providing exemplar memory repositories in the form of foreground segmented objects, albedo, shading, background scenes and imposing adversarial losses on the imagination spaces. Our model learns to perform such inversion with weak supervision, without ever having seen paired annotated data, that is, without having seen the image paired with the corresponding ground-truth imaginations. We demonstrate our method by applying it to three  Computer Vision tasks: image in-painting, intrinsic decomposition and object segmentation, each task having its own differentiable renderer.  Data driven adversarial imagination priors  effectively guide inversion,  minimize the need for hand designed priors of smoothness or good continuation, or the need for paired annotated data.

## item_id: m_0138

TITLE: Auto-Regressive Next-Token Predictors are Universal Learners

ABSTRACT: Large language models display remarkable capabilities in logical and mathematical reasoning, allowing them to solve complex tasks. Interestingly, these abilities emerge in networks trained on the simple task of next-token prediction. In this work, we present a theoretical framework for studying auto-regressive next-token predictors. We demonstrate that even simple models such as linear next-token predictors, trained on Chain-of-Thought (CoT) data, can approximate any function efficiently computed by a Turing machine. We introduce a new complexity measure---length complexity---which measures the number of intermediate tokens in a CoT sequence required to approximate some target function, and analyze the interplay between length complexity and other notions of complexity. Finally, we show experimentally that simple next-token predictors, such as linear networks and shallow Multi-Layer Perceptrons (MLPs), display non-trivial performance on text generation and arithmetic tasks. Our results demonstrate that the power of today's LLMs can be attributed, to a great extent, to the auto-regressive next-token training scheme, and not necessarily to a particular choice of architecture.

## item_id: m_0139

TITLE: Ada-K Routing: Boosting the Efficiency of MoE-based LLMs

ABSTRACT: In the era of Large Language Models (LLMs), Mixture-of-Experts (MoE) architectures offer a promising approach to managing computational costs while scaling up model parameters. Conventional MoE-based LLMs typically employ static Top-K routing, which activates a fixed and equal number of experts for each token regardless of their significance within the context. In this paper, we propose a novel Ada-K routing strategy that dynamically adjusts the number of activated experts for each token, thereby improving the balance between computational efficiency and model performance. Specifically, our strategy incorporates learnable and lightweight allocator modules that decide customized expert resource allocation tailored to the contextual needs for each token. These allocators are designed to be fully pluggable, making it broadly applicable across all mainstream MoE-based LLMs. We leverage the Proximal Policy Optimization (PPO) algorithm to facilitate an end-to-end learning process for this non-differentiable decision-making framework. Extensive evaluations on four popular baseline models demonstrate that our Ada-K routing method significantly outperforms conventional Top-K routing. Compared to Top-K, our method achieves over 25% reduction in FLOPs and more than 20% inference speedup while still improving performance across various benchmarks. Moreover, the training of Ada-K is highly efficient. Even for Mixtral-8x22B, a MoE-based LLM with more than 140B parameters, the training time is limited to 8 hours. Detailed analysis shows that harder tasks, middle layers, and content words tend to activate more experts, providing valuable insights for future adaptive MoE system designs. Both the training code and model checkpoints will be publicly available.

## item_id: m_0140

TITLE: Empowering Graph Representation Learning with Test-Time Graph Transformation

ABSTRACT: As powerful tools for representation learning on graphs, graph neural networks (GNNs) have facilitated various applications from drug discovery to recommender systems. Nevertheless, the effectiveness of GNNs is immensely challenged by issues related to data quality, such as distribution shift, abnormal features and adversarial attacks. Recent efforts have been made on tackling these issues from a modeling perspective which requires additional cost of changing model architectures or re-training model parameters. In this work, we provide a data-centric view to tackle these issues and propose a graph transformation framework named GTrans which adapts and refines graph data at test time to achieve better performance. We provide theoretical analysis on the design of the framework and discuss why adapting graph data works better than adapting the model. Extensive experiments have demonstrated the effectiveness of GTrans on three distinct scenarios for eight benchmark datasets where suboptimal data is presented. Remarkably, GTrans performs the best in most cases with improvements up to 2.8%, 8.2% and 3.8% over the best baselines on three experimental settings. 

## item_id: m_0141

TITLE: Unsupervised Learning of the Set of Local Maxima

ABSTRACT: This paper describes a new form of unsupervised learning, whose input is a set of unlabeled points that are assumed to be local maxima of an unknown value function $v$ in an unknown subset of the vector space. Two functions are learned: (i) a set indicator $c$, which is a binary classifier, and (ii) a comparator function $h$ that given two nearby samples, predicts which sample has the higher value of the unknown function $v$. Loss terms are used to ensure that all training samples $\vx$ are a local maxima of $v$, according to $h$ and satisfy $c(\vx)=1$. Therefore, $c$ and $h$ provide training signals to each other: a point $\vx'$ in the vicinity of $\vx$ satisfies $c(\vx)=-1$ or is deemed by $h$ to be lower in value than $\vx$. We present an algorithm, show an example where it is more efficient to use local maxima as an indicator function than to employ conventional classification, and derive a suitable generalization bound. Our experiments show that the method is able to outperform one-class classification algorithms in the task of anomaly detection and also provide an additional signal that is extracted in a completely unsupervised way.


## item_id: m_0142

TITLE: Deep Audio Prior

ABSTRACT: Deep convolutional  neural networks are known to specialize in distilling compact and robust prior from a large amount of data. We are interested in applying deep networks in the absence of training dataset. In this paper, we introduce deep audio prior (DAP)  which leverages the structure of a network and the temporal information in a single audio file. Specifically, we demonstrate that a randomly-initialized neural network can be used with carefully designed audio prior to tackle challenging audio problems such as universal blind source separation, interactive audio editing, audio texture synthesis, and audio co-separation.

To understand the robustness of the deep audio prior, we construct a benchmark dataset Universal-150 for universal sound source separation with a diverse set of sources. We show superior audio results than previous work on both qualitatively and quantitative evaluations. We also perform thorough ablation study to validate our design choices.

## item_id: m_0143

TITLE: Zero-Shot Model Search via Text-to-Logit Matching

ABSTRACT: With the increasing number of publicly available models, there are pre-trained, online models for many tasks that users require. In practice, users cannot find the relevant models as current search methods are text-based using the documentation which most models lack of. This paper presents ProbeLog, a method for retrieving classification models that can recognize a target concept, such as "Dog", without access to model metadata or training data. Specifically, ProbeLog computes a descriptor for each output dimension (logit) of each model, by observing its responses to a fixed set of inputs (probes). Similarly, we compute how the target concept is related to each probe. By measuring the distance between the probe responses of logits and concepts, we can identify logits that recognize the target concept. This enables zero-shot, text-based model retrieval ("find all logits corresponding to dogs"). To prevent hubbing, we calibrate the distances of each logit, according to other closely related concepts. We demonstrate that ProbeLog achieves high retrieval accuracy, both in ImageNet and real-world fine-grained search tasks, while being scalable to full-size repositories.  Importantly, further analysis reveals that the retrieval order is highly correlated with model and logit accuracies, thus allowing ProbeLog to find suitable and accurate models for users tasks in a zero-shot manner.

## item_id: m_0144

TITLE: Neural Architecture Search with Reinforcement Learning

ABSTRACT: Neural networks are powerful and flexible models that work well for many difficult learning tasks in image, speech and natural language understanding. Despite their success, neural networks are still hard to design. In this paper, we use a recurrent network to generate the model descriptions of neural networks and train this RNN with reinforcement learning to maximize the expected accuracy of the generated architectures on a validation set. On the CIFAR-10 dataset, our method, starting from scratch, can design a novel network architecture that rivals the best human-invented architecture in terms of test set accuracy. Our CIFAR-10 model achieves a test error rate of 3.65, which is 0.09 percent better and 1.05x faster than the previous state-of-the-art model that used a similar architectural scheme. On the Penn Treebank dataset, our model can compose a novel recurrent cell that outperforms the widely-used LSTM cell, and other state-of-the-art baselines.  Our cell achieves a test set perplexity of 62.4 on the Penn Treebank, which is 3.6 perplexity better than the previous state-of-the-art model. The cell can also be transferred to the character language modeling task on PTB and achieves a state-of-the-art perplexity of 1.214.

## item_id: m_0145

TITLE: Rethinking Again the Value of Network Pruning -- A Dynamical Isometry Perspective

ABSTRACT: Several recent works questioned the value of inheriting weight in structured neural network pruning because they empirically found training from scratch can match or even outperform finetuning a pruned model. In this paper, we present evidences that this argument is actually \emph{inaccurate} because of using improperly small finetuning learning rates. With larger learning rates, our results consistently suggest pruning outperforms training from scratch on multiple networks (ResNets, VGG11) and datasets (MNIST, CIFAR10, ImageNet) over most pruning ratios. To deeply understand why finetuning learning rate holds such a critical role, we examine the theoretical reason behind through the lens of \emph{dynamical isometry}, a nice property of networks that can make the gradient signals preserve norm during propagation. Our results suggest that weight removal in pruning breaks dynamical isometry, \emph{which fundamentally answers for the performance gap between a large finetuning LR and~a small one}. Therefore, it is necessary to recover the dynamical isometry before finetuning. In this regard, we also present a regularization-based technique to do so, which is rather simple-to-implement yet effective in dynamical isometry recovery on modern residual convolutional neural networks.

## item_id: m_0146

TITLE: Solving single-objective tasks by preference multi-objective reinforcement learning

ABSTRACT: There ubiquitously exist many single-objective tasks in the real world that are inevitably related to some other objectives and influenced by them. We call such task as the objective-constrained task, which is inherently a multi-objective problem. Due to the conflict among different objectives, a trade-off is needed. A common compromise is to design a scalar reward function through clarifying the relationship among these objectives using the prior knowledge of experts. However, reward engineering is extremely cumbersome. This will result in behaviors that optimize our reward function without actually satisfying our preferences. In this paper, we explicitly cast the objective-constrained task as preference multi-objective reinforcement learning, with the overall goal of finding a Pareto optimal policy. Combined with Trajectory Preference Domination we propose, a weight vector that reflects the agent's preference for each objective can be learned. We analyzed the feasibility of our algorithm in theory, and further proved in experiments its better performance compared to those that design the reward function by experts.

## item_id: m_0147

TITLE: Policy Optimization by Local Improvement through Search

ABSTRACT: Imitation learning has emerged as a powerful strategy for learning initial policies that can be refined with reinforcement learning techniques. Most strategies in imitation learning, however, rely on per-step supervision either from expert demonstrations, referred to as behavioral cloning or from interactive expert policy queries such as DAgger. These strategies differ on the state distribution at which the expert actions are collected -- the former using the state distribution of the expert, the latter using the state distribution of the policy being trained. However, the learning signal in both cases arises from the expert actions. On the other end of the spectrum, approaches rooted in Policy Iteration, such as Dual Policy Iteration do not choose next step actions based on an expert, but instead use planning or search over the policy to choose an action distribution to train towards. However, this can be computationally expensive, and can also end up training the policy on a state distribution that is far from the current policy's induced distribution. In this paper, we propose an algorithm that finds a middle ground by using Monte Carlo Tree Search (MCTS) to perform local trajectory improvement over rollouts from the policy. We provide theoretical justification for both the proposed local trajectory search algorithm and for our use of MCTS as a local policy improvement operator. We also show empirically that our method (Policy Optimization by Local Improvement through Search or POLISH) is much faster than methods that plan globally, speeding up training by a factor of up to 14 in wall clock time. Furthermore, the resulting policy outperforms strong baselines in both reinforcement learning and imitation learning.

## item_id: m_0148

TITLE: AttTok: Marrying Attribute Tokens with Generative Pre-trained Vision-Language Models towards Medical Image Understanding

ABSTRACT: Recent generative pre-trained vision–language (GPTv) models have achieved remarkable success in multi-modal understanding, inspiring their adaptation to medical imaging tasks such as disease diagnosis and visual question answering (VQA). However, current instruction-tuned GPTv models suffer from two key challenges: (1) medical attributes (e.g., disease names, severity grades) are encoded as plain text tokens, collapsing semantically distinct concepts into nearly identical textual sequences; and (2) inadequate textual supervision weakens visual representation learning, leading to severe inter-attribute confusion and misaligned vision–language embeddings. To address these limitations, we introduce attribute tokens (AttTok), a set of pre‑defined special tokens that uniquely encode clinical attributes (e.g., imaging modality, diagnosis, severity) within a structured token space. Complemented by attribute‑centric embedding books, AttTok serves as anchor points for aligning both visual and textual modalities into a shared, discriminative representation space. Building on this foundation, we design two key components: an attribute‑centric cross attention (ACC) adapter, which breaks the vision‑to‑text information‑flow bottleneck and enriches the visual encoder with discriminative attribute knowledge, and an attribute‑centric matching (ACM) loss, which enforces robust multi‑modal alignment centered on the attribute tokens. Extensive experiments on five medical classification benchmarks and three VQA datasets demonstrate that AttTok substantially improves both discriminative accuracy and medical knowledge reasoning, establishing a new paradigm for medical GPTv models with clinically discriminative understanding.

## item_id: m_0149

TITLE: Neural Operator Variational Inference based on Regularized Stein Discrepancy for Deep Gaussian Processes

ABSTRACT: A Deep Gaussian Process (DGP) model is a hierarchical composition of GP models that provides a deep Bayesian nonparametric approach to infer the posterior. Exact Bayesian inference is usually intractable for DGPs, motivating the use of various approximations. We theoretically demonstrate that the traditional alternative of mean-field Gaussian assumptions across the hierarchy leads to lack of expressiveness and efficacy of DGP models, whilst stochastic approximation often incurs a significant computational cost. To address this issue, we propose Neural Operator Variational Inference (NOVI) for Deep Gaussian Processes, where a sampler is obtained from a neural generator through minimizing Regularized Stein Discrepancy in L2 space between the approximate distribution and true posterior. Wherein a minimax problem is obtained and solved by Monte Carlo estimation and subsampling stochastic optimization. We experimentally demonstrate the effectiveness and efficiency of the proposed model, by applying it to a more flexible and wider class of posterior approximations on data ranging in size from hundreds to tens of thousands. By comparison, NOVI is superior to previous methods in both classification and regression.

## item_id: m_0150

TITLE: PREDICTION OF POTENTIAL HUMAN INTENTION USING SUPERVISED COMPETITIVE LEARNING

ABSTRACT: We propose a learning method to quantify human intention. Generally, a human being will imagine several potential actions for a given scene, but only one of these actions will subsequently be taken. This makes it difficult to quantify human intentions.
To solve this problem, we apply competitive learning to human behavior prediction as supervised learning. In our approach, competitive learning generates several outputs that are then associated with several potential situations imagined by a human. We applied the proposed method to human driving behavior and extracted three potential driving patterns. Results showed a squared error is reduced to 1/25 that of a conventional method . We also found that competitive learning can distinguish valid data from disturbance data in order to train a model.

## item_id: m_0151

TITLE: Target-Embedding Autoencoders for Supervised Representation Learning

ABSTRACT: Autoencoder-based learning has emerged as a staple for disciplining representations in unsupervised and semi-supervised settings. This paper analyzes a framework for improving generalization in a purely supervised setting, where the target space is high-dimensional. We motivate and formalize the general framework of target-embedding autoencoders (TEA) for supervised prediction, learning intermediate latent representations jointly optimized to be both predictable from features as well as predictive of targets---encoding the prior that variations in targets are driven by a compact set of underlying factors. As our theoretical contribution, we provide a guarantee of generalization for linear TEAs by demonstrating uniform stability, interpreting the benefit of the auxiliary reconstruction task as a form of regularization. As our empirical contribution, we extend validation of this approach beyond existing static classification applications to multivariate sequence forecasting, verifying their advantage on both linear and nonlinear recurrent architectures---thereby underscoring the further generality of this framework beyond feedforward instantiations.

## item_id: m_0152

TITLE: How Much Over-parameterization Is Sufficient to Learn Deep ReLU Networks?

ABSTRACT: A recent line of research on deep learning focuses on the extremely over-parameterized setting, and shows that when the network width is larger than a high degree polynomial of the training sample size $n$ and the inverse of the target error $\epsilon^{-1}$, deep neural networks learned by (stochastic) gradient descent enjoy nice optimization and generalization guarantees. Very recently, it is shown that under certain margin assumptions on the training data, a polylogarithmic width condition suffices for two-layer ReLU networks to converge and generalize (Ji and Telgarsky, 2020). However, whether deep neural networks can be learned with such a mild over-parameterization is still an open question. In this work, we answer this question affirmatively and establish sharper learning guarantees for deep ReLU networks trained by (stochastic) gradient descent. In specific, under certain assumptions made in previous work, our optimization and generalization guarantees hold with network width polylogarithmic in $n$ and $\epsilon^{-1}$. Our results push the study of over-parameterized deep neural networks towards more practical settings.

## item_id: m_0153

TITLE: Consolidator: Mergable Adapter with Group Connections for Visual Adaptation

ABSTRACT: Recently, transformers have shown strong ability as visual feature extractors, surpassing traditional convolution-based models in various scenarios. However, the success of vision transformers largely owes to their capacity to accommodate numerous parameters. As a result, new challenges for adapting a well-trained transformer to downstream tasks arise. On the one hand, classic fine-tuning tunes all parameters in a huge model for every downstream task and thus easily falls into an overfitting situation, leading to inferior performance. On the other hand, on resource-limited devices, fine-tuning stores a full copy of all parameters and thus is usually impracticable for the shortage of storage space. However, few works have focused on how to efficiently and effectively transfer knowledge in a vision transformer. Existing methods did not dive into the properties of visual features, leading to inferior performance. Moreover, some of them bring heavy inference cost though benefiting storage. To tackle these problems, we propose consolidator to achieve efficient transfer learning for large vision models. Our consolidator modifies the pre-trained model with the addition of a small set of tunable parameters to temporarily store the task-specific knowledge while freezing the backbone model during adaptation. Motivated by the success of group-wise convolution, we adopt grouped connections across the features extracted by fully connected layers to construct tunable parts in a consolidator. To further enhance the model's capacity to transfer knowledge under a constrained storage budget and keep inference efficient, we consolidate the parameters in two stages: 1. between adaptation and storage, and 2. between loading and inference. On a series of downstream visual tasks, our consolidator can reach up to 7.56 better accuracy than full fine-tuning with merely 0.35% parameters, and outperform state-of-the-art parameter-efficient tuning methods by a clear margin. Code is available at github.

## item_id: m_0154

TITLE: Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models

ABSTRACT: The standard practice for training large language models involves packing multiple documents together to optimize computational efficiency. However, the impact of this process on the models' capabilities remains largely unexplored. To address this gap, we investigate how different document-packing strategies influence the latent multi-hop reasoning abilities of LLMs. Our findings indicate that packing can improve model performance compared to training on individual documents, at the expense of more compute. To further understand the underlying mechanisms, we conduct an ablation study, identifying key factors that explain the advantages of packing. Ultimately, our research deepens the understanding of LLM training dynamics and provides practical insights for optimizing model development.

## item_id: m_0155

TITLE: Neuron-Enhanced Autoencoder based Collaborative filtering: Theory and Practice

ABSTRACT: This paper presents a novel recommendation method called neuron-enhanced autoencoder based collaborative filtering (NE-AECF). The method uses an additional neural network to enhance the reconstruction capability of autoencoder. Different from the main neural network implemented in a layer-wise manner, the additional neural network is implemented in an element-wise manner. They are trained simultaneously to construct an enhanced autoencoder of which the activation function in the output layer is learned adaptively to approximate possibly complicated response functions in real data. We provide theoretical analysis for NE-AECF to investigate the generalization ability of autoencoder and deep learning in collaborative filtering. We prove that the element-wise neural network is able to reduce the upper bound of the prediction error for the unknown ratings, the data sparsity is not problematic but useful, and the prediction performance is closely related to the difference between the number of users and the number of items.
Numerical results show that our NE-AECF has promising performance on a few benchmark datasets.

## item_id: m_0156

TITLE: Off-the-Grid MARL: Datasets with Baselines for Offline Multi-Agent Reinforcement Learning

ABSTRACT: Being able to harness the power of large datasets for developing cooperative multi-agent controllers promises to unlock enormous value for real-world applications. Many important industrial systems are multi-agent in nature and are difficult to model using bespoke simulators. However, in industry, distributed processes can often be recorded during operation, and large quantities of demonstrative data stored. Offline multi-agent reinforcement learning (MARL) provides a promising paradigm for building effective decentralised controllers from such datasets. However, offline MARL is still in its infancy and therefore lacks standardised benchmark datasets and baselines typically found in more mature subfields of reinforcement learning (RL). These deficiencies make it difficult for the community to sensibly measure progress. In this work, we aim to fill this gap by releasing off-the-grid MARL (OG-MARL): a growing repository of high-quality datasets with baselines for cooperative offline MARL research. Our datasets provide settings that are characteristic of real-world systems, including complex environment dynamics, heterogeneous agents, non-stationarity, many agents, partial observability, suboptimality, sparse rewards and demonstrated coordination. For each setting, we provide a range of different dataset types (e.g. Good, Medium, Poor, and Replay) and profile the composition of experiences for each dataset. We hope that OG-MARL will serve the community as a reliable source of datasets and help drive progress, while also providing an accessible entry point for researchers new to the field.

## item_id: m_0157

TITLE: The Cost of Reproducibility in Artificial Intelligence

ABSTRACT: **Background.** The reproducibility crisis has not left artificial intelligence untouched.
Lack of documentation in published research can make independent replication an
unnecessarily laborious task. We propose the cost of reproducibility as the labour
required to reproduce a method and its results due to lacking documentation.

**Objectives.** We aim to quantify the cost of reproducibility to determine significant
variation between venues. We hypothesise that studies published in venues with
strict reproducibility requirements in the review process are less costly to reproduce.

**Methods.** We propose five dimensions of the cost of reproducibility and evaluate
them on a scale of 1 to 10, using objective characteristics e.g., availability of code,
data, parameter values and experiment setup. We reviewed 1061 papers published
between 2022-2024 from AAAI, ICLR, ICML, IJCAI, JAIR, JMLR and NeurIPS.

**Results.** Machine learning conferences are up to 16.52% less costly to reproduce
than artificial intelligence conferences and 12.91% than journals. Award-winning
papers are not less costly to reproduce than average papers at the same venue.

**Conclusions.** By quantifying the reproducibility cost, we find that the effectiveness
of reproducibility standards depends on community support and strict enforcement
in the review process, to significantly lower cost. We encourage the publication
of appendices and reproducibility checklists, and a low cost as a key criterion for
paper awards to drive community changes with examples of best practices.
awards to drive community changes with examples of best practices.

## item_id: m_0158

TITLE: A-Bench: Are LMMs Masters at Evaluating AI-generated Images?

ABSTRACT: How to accurately and efficiently assess AI-generated images (AIGIs) remains a critical challenge for generative models. Given the high costs and extensive time commitments required for user studies, many researchers have turned towards employing large multi-modal models (LMMs) as AIGI evaluators, the precision and validity of which are still questionable. Furthermore, traditional benchmarks often utilize mostly natural-captured content rather than AIGIs to test the abilities of LMMs, leading to a noticeable gap for AIGIs. Therefore, we introduce **A-Bench** in this paper, a benchmark designed to diagnose *whether LMMs are masters at evaluating AIGIs*. Specifically, **A-Bench** is organized under two key principles: 1) Emphasizing both high-level semantic understanding and low-level visual quality perception to address the intricate demands of AIGIs. 2) Various generative models are utilized for AIGI creation, and various LMMs are employed for evaluation, which ensures a comprehensive validation scope. Ultimately, 2,864 AIGIs from 16 text-to-image models are sampled, each paired with question-answers annotated by human experts. We hope that **A-Bench** will significantly enhance the evaluation process and promote the generation quality for AIGIs.

## item_id: m_0159

TITLE: Better know nothing than half-know anything: A Precise and Efficient Dataset for Scientific Reasoning in Language Models

ABSTRACT: Large Language Models (LLMs) have achieved remarkable progress in reasoning tasks, i.e., coding and mathematics. However, their ability to perform scientific reasoning remains significantly limited, probably hampered by the scarcity of high-quality scientific reasoning datasets. Existing approaches either rely on LLM-generated synthetic data (suffering from noise and hallucinations) or human-compiled documents (facing scarcity and non-standardization). In this paper, we empirically verify that integrating precise knowledge from original scientific documents with formalized questions and consistent answers can mitigate the need for large-scale data. Based on this insight, we design PreciSci, a pipeline for constructing multi-disciplinary scientific reasoning datasets. This pipeline involves extracting knowledge from reliable sources, refining questions for completeness and precision, applying multi-stage filtering to eliminate redundancy and noise, and refining answers to ensure reliable supervision. Leveraging PreciSci, we build Open-Sci, a precise and knowledge-dense scientific reasoning dataset. Experimental evaluations show that despite Open-Sci being less than one-sixth the size of state-of-the-art scientific reasoning datasets, it enables LLMs to achieve approximately $\mathbf{4.49\%}$ better performance across diverse discipline-specific benchmarks.

## item_id: m_0160

TITLE: The Chosen Few: Sparse Adaptation for Large Models

ABSTRACT: Parameter-Efficient Fine-Tuning (PEFT) methods have become essential for adapting large pretrained models to downstream tasks, with Low-Rank Adaptation (LoRA) emerging as one of the most widely adopted solutions.
However, there remain several key limitations in  current LoRA-based PEFT methods:
(1) the low-rank feature space in LoRA is rigid, reducing its capacity for dynamic adaptation;
(2) the restricted dimensionality, coupled with dense and entangled representations, constrains the model’s capacity to generalize across multiple domains; 
and (3) the compression process limits the extent to which model behavior can be understood from the learned representations, making it difficult to interpret the functional role of task-relevant features.
In this paper, we argue that sparse adaptation offers a principled and more flexible alternative to low-rank adaptation, with the added benefit of enhancing interpretability.
Instead of compressing information into a low-rank subspace, sparse adaptation focuses on identifying and selectively activating a small subset of high-dimensional latent features, enabling a more decomposed and dynamic fine-tuning process.
Building on this paradigm, we propose STAN (Sparse adapTAtioN), a novel method that actualizes sparse adaptation by integrating dedicated Sparse Autoencoder (SAE) modules into frozen pretrained models. 
STAN learns to encode task-specific adaptations through sparse activations within the SAEs, thereby using sparse features as the mechanism for dynamic and robust adaptation.
Beyond the flexibility offered by input-dependent sparse combinations, the large latent space of the SAEs provides scalable capacity for cross-domain adaptation, while their inherent semantic decomposition structure supports more interpretable representations.
Through extensive experiments, we demonstrate that STAN outperforms state-of-the-art PEFT baselines across a range of benchmarks, while uniquely enabling inspection and analysis of the learned sparse activations. Our findings position sparse adaptation as a promising new direction in PEFT, advancing both the expressivity and interpretability of model adaptation.

## item_id: m_0161

TITLE: Mixture of Pre-processing Experts Model for Noise Robust Deep Learning on Resource Constrained Platforms

ABSTRACT: Deep learning on an edge device requires energy efficient operation due to ever diminishing power budget. Intentional low quality data during the data acquisition for longer battery life, and natural noise from the low cost sensor degrade the quality of target output which hinders adoption of deep learning on an edge device. To overcome these problems,  we propose simple yet efficient mixture of pre-processing experts (MoPE) model to handle various image distortions including low resolution and noisy images.  We also propose to use adversarially trained auto encoder as a pre-processing expert for the noisy images.  We evaluate our proposed method for various machine learning tasks including object detection on MS-COCO 2014 dataset, multiple object tracking problem on MOT-Challenge dataset, and human activity recognition on UCF 101 dataset. Experimental results show that the proposed method achieves better detection, tracking and activity recognition accuracies under noise without sacrificing accuracies for the clean images. The overheads of our proposed MoPE are 0.67% and 0.17% in terms of memory and computation compared to the baseline object detection network.

## item_id: m_0162

TITLE: Self-Organizing Intelligent Matter:  A blueprint for an AI generating algorithm

ABSTRACT: We propose an artificial life framework aimed at facilitating the emergence of intelligent organisms. In this framework there is no explicit notion of an agent: instead there is an environment made of atomic elements. These elements contain neural operations and interact through exchanges of information and through physics-like rules contained in the environment. We discuss how an evolutionary process can lead to the emergence of different organisms made of many such atomic elements which can coexist and thrive in the environment. We discuss how this forms the basis of a general AI generating algorithm. We provide a simplified implementation of such system and discuss what advances need to be made to scale it up further.

## item_id: m_0163

TITLE: Partial Simulation for Imitation Learning

ABSTRACT: Model-based imitation learning methods require full knowledge of the transition kernel for policy evaluation. In this work, we introduce the Expert Induced Markov Decision Process (eMDP) model as a formulation of solving imitation problems using Reinforcement Learning (RL), when only partial knowledge about the transition kernel is available. The idea of eMDP is to replace the unknown transition kernel with a synthetic kernel that: a) simulate the transition of state components for which the transition kernel is known (s_r), and b) extract from demonstrations the state components for which the kernel is unknown (s_u). The next state is then stitched from the two components: s={s_r,s_u}. We describe in detail the recipe for building an eMDP and analyze the errors caused by its synthetic kernel. Our experiments include imitation tasks in multiplayer games, where the agent has to imitate one expert in the presence of other experts for whom we cannot provide a transition model. We show that combining a policy gradient algorithm with our model achieves superior performance compared to the simulation-free alternative.

## item_id: m_0164

TITLE: Adapting to Reward Progressivity via Spectral Reinforcement Learning

ABSTRACT: In this paper we consider reinforcement learning tasks with progressive rewards; that is, tasks where the rewards tend to increase in magnitude over time. We hypothesise that this property may be problematic for value-based deep reinforcement learning agents, particularly if the agent must first succeed in relatively unrewarding regions of the task in order to reach more rewarding regions. To address this issue, we propose Spectral DQN, which decomposes the reward into frequencies such that the high frequencies only activate when large rewards are found. This allows the training loss to be balanced so that it gives more even weighting across small and large reward regions. In two domains with extreme reward progressivity, where standard value-based methods struggle significantly, Spectral DQN is able to make much farther progress. Moreover, when evaluated on a set of six standard Atari games that do not overtly favour the approach, Spectral DQN remains more than competitive: While it underperforms one of the benchmarks in a single game, it comfortably surpasses the benchmarks in three games. These results demonstrate that the approach is not overfit to its target problem, and suggest that Spectral DQN may have advantages beyond addressing reward progressivity.

## item_id: m_0165

TITLE: Total Style Transfer with a Single Feed-Forward Network

ABSTRACT: Recent image style transferring methods achieved arbitrary stylization with input content and style images. To transfer the style of an arbitrary image to a content image, these methods used a feed-forward network with a lowest-scaled feature transformer or a cascade of the networks with a feature transformer of a corresponding scale. However, their approaches did not consider either multi-scaled style in their single-scale feature transformer or dependency between the transformed feature statistics across the cascade networks. This shortcoming resulted in generating partially and inexactly transferred style in the generated images.
To overcome this limitation of partial style transfer, we propose a total style transferring method which transfers multi-scaled feature statistics through a single feed-forward process. First, our method transforms multi-scaled feature maps of a content image into those of a target style image by considering both inter-channel correlations in each single scaled feature map and inter-scale correlations between multi-scaled feature maps. Second, each transformed feature map is inserted into the decoder layer of the corresponding scale using skip-connection. Finally, the skip-connected multi-scaled feature maps are decoded into a stylized image through our trained decoder network.

## item_id: m_0166

TITLE: Regularization Cocktails for Tabular Datasets

ABSTRACT: The regularization of prediction models is arguably the most crucial ingredient that allows Machine Learning solutions to generalize well on unseen data. Several types of regularization are popular in the Deep Learning community (e.g., weight decay, drop-out, early stopping, etc.), but so far these are selected on an ad-hoc basis, and there is no systematic study as to how different regularizers should be combined into the best “cocktail”. In this paper, we fill this gap, by considering the cocktails of 13 different regularization methods and framing the question of how to best combine them as a standard hyperparameter optimization problem. We perform a large-scale empirical study on 40 tabular datasets, concluding that, firstly, regularization cocktails substantially outperform individual regularization methods, even if the hyperparameters of the latter are carefully tuned; secondly, the optimal regularization cocktail depends on the dataset; and thirdly, regularization cocktails yield the state-of-the-art in classifying tabular datasets by outperforming Gradient-Boosted Decision Trees.

## item_id: m_0167

TITLE: Overcoming Weak Visual-Textual Alignment for Video Moment Retrieval

ABSTRACT: Video moment retrieval (VMR) identifies a specific moment in an untrimmed video for a given natural language query.
This task is prone to suffer the weak visual-textual alignment problem innate in the video datasets. 
Due to the ambiguity, a query does not fully cover the relevant details of the corresponding moment, or the moment may contain misaligned and irrelevant frames, potentially limiting further performance gains and generalization capability.
To tackle this problem, we propose a background-aware moment detection transformer (BM-DETR).
Our model adopts a contrastive approach, carefully utilizing the negative queries matched to other moments in the video.
Specifically, our model learns to predict the target moment from the joint probability of each frame given the positive query and the complement of negative queries.
This leads to efficient and effective use of the surrounding background, improving moment sensitivity and enhancing overall alignments in videos.
Our approach is efficient and outperforms previous methods, including contrastive learning-based, on multiple datasets with significantly reduced computational costs.

## item_id: m_0168

TITLE: GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering

ABSTRACT: We present GI-GS, a novel inverse rendering framework that leverages 3D Gaussian Splatting (3DGS) and deferred shading to achieve photo-realistic novel view synthesis and relighting. In inverse rendering, accurately modeling the shading processes of objects is essential for achieving high-fidelity results. Therefore, it is critical to incorporate global illumination to account for indirect lighting that reaches an object after multiple bounces across the scene. Previous 3DGS-based methods have attempted to model indirect lighting by characterizing indirect illumination as learnable lighting volumes or additional attributes of each Gaussian, while using baked occlusion to represent shadow effects. These methods, however, fail to accurately model the complex physical interactions between light and objects, making it impossible to construct realistic indirect illumination during relighting. To address this limitation, we propose to calculate indirect lighting using efficient path tracing with deferred shading. In our framework, we first render a G-buffer to capture the detailed geometry and material properties of the scene. Then, we perform physically-based rendering (PBR) only for direct lighting. With the G-buffer and previous rendering results, the indirect lighting can be calculated through a lightweight path tracing. Our method effectively models indirect lighting under any given lighting conditions, thereby achieving better novel view synthesis and competitive relighting. Quantitative and qualitative results show that our GI-GS outperforms existing baselines in both rendering quality and efficiency. Project page: https://stopaimme.github.io/GI-GS-site/.

## item_id: m_0169

TITLE: Fake It Until You Make It : Towards Accurate Near-Distribution Novelty Detection

ABSTRACT: We aim for image-based novelty detection. Despite considerable progress, existing models either fail or face dramatic drop under the so-called ``near-distribution" setup, where the differences between normal and anomalous samples are subtle. We first demonstrate existing methods could experience up to 20\% decrease in their AUCs in the near-distribution setting. Next, we propose to exploit a score-based generative model to produce synthetic near-distribution anomalous data. Our model is then fine-tuned to distinguish such data from the normal samples. We make quantitative as well as qualitative evaluation of this strategy, and compare the results with a variety of GAN-based models.  Effectiveness of our method for both near-distribution and standard novelty detection is assessed through extensive experiments on datasets in diverse applications such as medical images, object classification, and quality control. This reveals that our method significantly improves upon existing models, and consistently decreases the gap between the near-distribution and standard novelty detection AUCs by a considerable amount.

## item_id: m_0170

TITLE: Observable Propagation: Uncovering Feature Vectors in Transformers

ABSTRACT: A key goal of current mechanistic interpretability research in NLP is to find linear features (also called "feature vectors") for transformers:  directions in activation space corresponding to concepts that are used by a given model in its computation. Present state-of-the-art methods for finding linear features require large amounts of labelled data -- both laborious to acquire and computationally expensive to utilize. In this work, we introduce a novel method, called "observable propagation" (in short: "ObsProp"), for finding linear features used by transformer language models in computing a given task -- using almost no data. Our paradigm centers on the concept of "observables", linear functionals corresponding to given tasks. We then introduce a mathematical theory for the analysis of feature vectors: we prove that LayerNorm nonlinearities in high dimensions do not affect the direction of feature vectors; we also introduce a similarity metric between feature vectors called the "coupling coefficient", and prove that it accurately estimates the degree to which one feature's output correlates with another's. Armed with these tools, we use observable propagation to investigate the features that cause gendered occupational bias in a large language model. In our experiments, we identify the specific features used by the model for predicting occupation based on a gendered name, and find that some of the same features are used by the model for predicting grammatical gender. Our results suggest that observable propagation can be used to better understand the mechanisms responsible for bias in large language models.

## item_id: m_0171

TITLE: BETANAS: Balanced Training and selective drop for Neural Architecture Search

ABSTRACT: Automatic neural architecture search techniques are becoming increasingly important in machine learning area recently.  Especially, weight sharing methods have shown remarkable potentials on searching good network architectures with few computational resources. However, existing weight sharing methods mainly suffer limitations on searching strategies: these methods either uniformly train all network paths to convergence which introduces conflicts between branches and wastes a large amount of computation on unpromising candidates, or selectively train branches with different frequency which leads to unfair evaluation and comparison among paths. To address these issues, we propose a novel neural architecture search method  with balanced training strategy to ensure fair comparisons and a selective drop mechanism to reduces conflicts among candidate paths. The experimental results show that our proposed method can achieve a leading performance of 79.0% on ImageNet under mobile settings, which outperforms other state-of-the-art methods in both accuracy and efficiency.

## item_id: m_0172

TITLE: Aggregating explanation methods for neural networks stabilizes explanations

ABSTRACT: 	Despite a growing literature on explaining neural networks, no consensus has been reached on how to explain a neural network decision or how to evaluate an explanation.
	Our contributions in this paper are twofold. First, we investigate schemes to combine explanation methods and reduce model uncertainty to obtain a single aggregated explanation. The aggregation is more robust and aligns better with the neural network than any single explanation method..
	Second, we propose a new approach to evaluating explanation methods that circumvents the need for manual evaluation and is not reliant on the alignment of neural networks and humans decision processes. 

## item_id: m_0173

TITLE: Bilevel Reinforcement Learning for Stock Data with A Conservative TD Ensemble

ABSTRACT: Reinforcement learning (RL) has shown significant promise in stock trading. A typical solution involves optimizing cumulative returns using historical offline data. However, it may produce less generalizable policies that merely "memorize" optimal buying and selling actions from the offline data while neglecting the non-stationary nature of the financial market. We frame stock trading as a specific type of offline RL problem. Our method, MetaTrader, presents two key contributions. First, it introduces a novel bilevel actor-critic method that spans both the original stock data and its transformations. The fundamental idea is that an effective policy should be generalizable across out-of-distribution data. Second, we propose a novel variant of conservative TD learning, utilizing an ensemble-based TD target to mitigate value overestimation, particularly in scenarios with limited offline data. Our empirical findings across two publicly available datasets demonstrate the superior performance of MetaTrader over existing methods, including both RL-based approaches and stock prediction models.

## item_id: m_0174

TITLE: When Robustness Doesn’t Promote Robustness: Synthetic vs. Natural Distribution Shifts on ImageNet

ABSTRACT: We conduct a large experimental comparison of various robustness metrics for image classification. The main question of our study is to what extent current synthetic robustness interventions (lp-adversarial examples, noise corruptions, etc.) promote robustness under natural distribution shifts occurring in real data. To this end, we evaluate 147 ImageNet models under 199 different evaluation settings. We find that no current robustness intervention improves robustness on natural distribution shifts beyond a baseline given by standard models without a robustness intervention. The only exception is the use of larger training datasets, which provides a small increase in robustness on one natural distribution shift. Our results indicate that robustness improvements on real data may require new methodology and more evaluations on natural distribution shifts.

## item_id: m_0175

TITLE: Combating Deep Reinforcement Learning's Sisyphean Curse with Intrinsic Fear

ABSTRACT: To use deep reinforcement learning in the wild, we might hope for an agent that can avoid catastrophic mistakes. Unfortunately, even in simple environments, the popular deep Q-network (DQN) algorithm is doomed by a Sisyphean curse. Owing to the use of function approximation, these agents eventually forget experiences as they become exceedingly unlikely under a new policy. Consequently, for as long as they continue to train, DQNs may periodically relive catastrophic mistakes. Many real-world environments where people might be injured exhibit a special structure. We know a priori that catastrophes are not only bad, but that agents need not ever get near to a catastrophe state. In this paper, we exploit this structure to learn a reward-shaping that accelerates learning and guards oscillating policies against repeated catastrophes. First, we demonstrate unacceptable performance of DQNs on two toy problems. We then introduce intrinsic fear, a new method that mitigates these problems by avoiding dangerous states. Our approach incorporates a second model trained via supervised learning to predict the probability of catastrophe within a short number of steps. This score then acts to penalize the Q-learning objective, shaping the reward function away from catastrophic states.

## item_id: m_0176

TITLE: Towards Understanding Multimodal Fine-Tuning: A Case Study into Spatial Features

ABSTRACT: Contemporary Vision–Language Models (VLMs) achieve strong performance on a wide range of tasks by pairing a vision encoder with a pre-trained language model, fine-tuned for visual–text inputs. Yet despite these gains, it remains unclear how language backbone representations adapt during multimodal training and when vision-specific capabilities emerge. In this work, we present the first mechanistic analysis of VLMs adaptation process. Using stage-wise model diffing, a technique that isolates representational changes introduced during multimodal fine-tuning, we reveal how a language model learns to "see". We first identify vision-preferring features that emerge or reorient during fine-tuning. We then show that a selective subset of these features reliably encodes spatial relations, revealed through controlled shifts to spatial prompts. Finally, we trace the causal activation of these features to a small group of attention heads. Our findings show that stage-wise model diffing reveals when and where spatially-grounded multimodal features arise. It also provides a clearer view of modality fusion by showing how visual grounding reshapes features that were previously text-only. This methodology enhances the interpretability of multimodal training and provides a foundation for understanding and refining how pretrained language models acquire vision-grounded capabilities.

## item_id: m_0177

TITLE: LatTe Flows: Latent Temporal Flows for Multivariate Sequence Analysis 

ABSTRACT: We introduce Latent Temporal Flows (\emph{LatTe-Flows}), a method for probabilistic multivariate time-series analysis tailored for high dimensional systems whose temporal dynamics are driven by variations in a lower-dimensional discriminative subspace. We perform indirect learning from hidden traits of observed sequences by assuming that the random vector representing the data is generated from an unobserved low-dimensional latent vector. \emph{LatTe-Flows} jointly learns auto-encoder mappings to a latent space and learns the temporal distribution of lower-dimensional embeddings of input sequences. Since encoder networks retain only the essential information to generate a latent manifold, the temporal distribution transitions can be more efficiently uncovered by time conditioned Normalizing Flows. The learned latent effects can then be directly transferred into the observed space through the decoder network. We demonstrate that the proposed method significantly outperforms the state-of-the-art on multi-step forecasting benchmarks, while enjoying reduced computational complexity on several real-world datasets. We apply {\emph{LatTe-Flows}} to a challenging sensor-signal forecasting task, using multivariate time-series measurements collected by wearable devices, an increasingly relevant health application.


## item_id: m_0178

TITLE: Adversarial robustness against multiple $l_p$-threat models at the price of one and how to quickly fine-tune robust models to another threat model

ABSTRACT: Adversarial training (AT) in order to achieve adversarial robustness wrt single $l_p$-threat models has been discussed extensively. However, for safety-critical systems adversarial robustness should be achieved wrt all $l_p$-threat models simultaneously. In this paper we develop a simple and efficient training scheme to achieve adversarial robustness against the union of $l_p$-threat models. Our novel E-AT scheme is based on geometric considerations of the different $l_p$-balls and costs as much as normal adversarial training against a single $l_p$-threat model. Moreover, we show that using our E-AT scheme one can fine-tune with just 3 epochs \emph{any} $l_p$-robust model (for $p \in \{1,2,\infty\}$) and achieve multiple norm adversarial robustness. In this way we boost the state-of-the-art for multiple-norm robustness to more than $51\%$ on CIFAR-10 and report up to our knowledge the first ImageNet models with multiple norm robustness. Moreover, we study the general transfer of adversarial robustness between different threat models and in this way boost the previous SOTA $l_1$-robustness on CIFAR-10 by almost $10\%$.

## item_id: m_0179

TITLE: HAPPIER: Hierarchical Polyphonic Music Generative RNN

ABSTRACT: Generating polyphonic music with coherent global structure is a major challenge for automatic composition algorithms. The primary difficulty arises due to the inefficiency of models to recognize underlying patterns beneath music notes across different levels of time scales and remain long-term consistency while composing. Hierarchical architectures can capture and represent learned patterns in different temporal scales and maintain consistency over long time spans, and this corresponds to the hierarchical structure in music. Motivated by this, focusing on leveraging the idea of hierarchical models and improve them to fit the sequence modeling problem, our paper proposes HAPPIER: a novel HierArchical PolyPhonic musIc gEnerative RNN. In HAPPIER, A higher `measure level' learns correlations across measures and patterns for chord progressions, and a lower `note level' learns a conditional distribution over the notes to generate within a measure. The two hierarchies operate at different clock rates: the higher one operates on a longer timescale and updates every measure, while the lower one operates on a shorter timescale and updates every unit duration. The two levels communicate with each other, and thus the entire architecture is trained jointly end-to-end by back-propagation. HAPPIER, profited from the strength of the hierarchical structure, generates polyphonic music with long-term dependencies compared to the state-of-the-art methods.

## item_id: m_0180

TITLE: Unsupervised Perceptual Rewards for Imitation Learning

ABSTRACT: Reward function design and exploration time are arguably the biggest obstacles to the deployment of reinforcement learning (RL) agents in the real world. In many real-world tasks, designing a suitable reward function takes considerable manual engineering and often requires additional and potentially visible sensors to be installed just to measure whether the task has been executed successfully. Furthermore, many interesting tasks consist of multiple steps that must be executed in sequence. Even when the final outcome can be measured, it does not necessarily provide useful feedback on these implicit intermediate steps or sub-goals.
To address these issues, we propose leveraging the abstraction power of intermediate visual representations learned by deep models to quickly infer perceptual reward functions from small numbers of demonstrations. We present a method that is able to identify the key intermediate steps of a task from only a handful of demonstration sequences, and automatically identify the most discriminative features for identifying these steps. This method makes use of the features in a pre-trained deep model, but does not require any explicit sub-goal supervision. The resulting reward functions, which are dense and smooth, can then be used by an RL agent to learn to perform the task in real-world settings. To evaluate the learned reward functions, we present qualitative results on two real-world tasks and a quantitative evaluation against a human-designed reward function. We also demonstrate that our method can be used to learn a complex real-world door opening skill using a real robot, even when the demonstration used for reward learning is provided by a human using their own hand. To our knowledge, these are the first results showing that complex robotic manipulation skills can be learned directly and without supervised labels from a video of a human performing the task.


## item_id: m_0181

TITLE: Witches' Brew: Industrial Scale Data Poisoning via Gradient Matching

ABSTRACT: Data Poisoning attacks modify training data to maliciously control a model trained on such data.
In this work, we focus on targeted poisoning attacks which cause a reclassification of an unmodified test image and as such breach model integrity. We consider a
particularly malicious poisoning attack that is both ``from scratch" and ``clean label", meaning we analyze an attack that successfully works against new, randomly initialized models, and is nearly imperceptible to humans, all while perturbing only a small fraction of the training data. 
Previous poisoning attacks against deep neural networks in this setting have been limited in scope and success, working only in simplified settings or being prohibitively expensive for large datasets.
The central mechanism of the new attack is matching the gradient direction of malicious examples. We analyze why this works, supplement with practical considerations. and show its threat to real-world practitioners, finding that it is the first poisoning method to cause targeted misclassification in modern deep networks trained from scratch on a full-sized, poisoned ImageNet dataset.
Finally we demonstrate the limitations of existing defensive strategies against such an attack, concluding that data poisoning is a credible threat, even for large-scale deep learning systems.

## item_id: m_0182

TITLE: Differentiable Architecture Compression

ABSTRACT: In many learning situations, resources at inference time are significantly more constrained than resources at training time. This paper studies a general paradigm, called Differentiable ARchitecture Compression (DARC), that combines model compression and architecture search to learn models that are resource-efficient at inference time. Given a resource-intensive base architecture, DARC utilizes the training data to learn which sub-components can be replaced by cheaper alternatives. The high-level technique can be applied to any neural architecture, and we report experiments on state-of-the-art convolutional neural networks for image classification. For a WideResNet with 97.2% accuracy on CIFAR-10, we improve single-sample inference speed by 2.28X and memory footprint by 5.64X, with no accuracy loss. For a ResNet with 79.15% Top-1 accuracy on ImageNet, we improve batch inference speed by 1.29X and memory footprint by 3.57X with 1% accuracy loss. We also give theoretical Rademacher complexity bounds in simplified cases, showing how DARC avoids over-fitting despite over-parameterization.

## item_id: m_0183

TITLE: OmniInput: A Model-centric Evaluation Framework through Output Distribution

ABSTRACT: We propose a novel model-centric evaluation framework, OmniInput, to evaluate the quality of an AI/ML model's predictions on all possible inputs (including human-unrecognizable ones), which is crucial for AI safety and reliability. Unlike traditional data-centric evaluation based on pre-defined test sets, the test set in OmniInput is self-constructed by the model itself and the model quality is evaluated by investigating its output distribution. We employ an efficient sampler to obtain representative inputs and the output distribution of the trained model, which, after selective annotation, can be used to estimate the model's precision and recall at different output values and a comprehensive precision-recall curve. Our experiments demonstrate that OmniInput enables a more fine-grained comparison between models, especially when their performance is almost the same on pre-defined test sets, leading to new findings and insights for how to train more robust, generalizable models.

## item_id: m_0184

TITLE: DETRDistill: A Simple Knowledge Distillation Framework for DETR-Families

ABSTRACT: Transformer-based detectors (DETRs) have attracted great attention due to their sparse training paradigm and the removal of post-processing operations, but the huge model can be computationally time-consuming and difficult to be deployed in real-world applications. To tackle this problem, knowledge distillation (KD) can be employed to compress the huge model by constructing a simple teacher-student learning framework. Different from the traditional CNN detectors, where the distillation targets can be naturally aligned through the feature map, DETR regards object detection as a set prediction problem, leading to an unclear relationship between teacher and student during distillation. In this paper, we propose DETRDistill, a novel knowledge distillation dedicated to DETR-families. We first explore a sparse matching paradigm with progressive stage-by-stage instance distillation. Considering the diverse attention mechanisms adopted in different DETRs, we propose attention-agnostic feature distillation module to overcome the ineffectiveness of conventional feature imitation. Finally, to fully leverage the intermediate products from the teacher, we introduce teacher-assisted assignment distillation, which greatly alleviates the instability of label assignment caused by bipartite graph matching. Extensive experiments demonstrate that our distillation method achieves significant improvement on various competitive DETR approaches, without introducing extra consumption in the inference phase. To the best of our knowledge, this is the first systematic study to explore a general distillation method for DETR-style detectors.

## item_id: m_0185

TITLE: The Bures Metric for Taming Mode Collapse in Generative Adversarial Networks

ABSTRACT: Generative Adversarial Networks (GANs) are performant generative methods yielding high-quality samples. However, under certain circumstances, the training of GANs can lead to mode collapse or mode dropping, i.e. the generative models not being able to sample from the entire probability distribution. To address this problem, we use the last layer of the discriminator as a feature map to study the distribution of the real and the fake data. During training, we propose to match the real batch diversity to the fake batch diversity by using the Bures distance between covariance matrices in feature space. The computation of the Bures distance can be conveniently done in either feature space or kernel space in terms of the covariance and kernel matrix respectively. We observe that diversity matching reduces mode collapse substantially and has a positive effect on the sample quality. On the practical side, a very simple training procedure, that does not require additional hyperparameter tuning, is proposed and assessed on several datasets.  

## item_id: m_0186

TITLE: Emotion-o1: Adaptive Long Reasoning for Emotion Understanding in LLMs

ABSTRACT: Long chain-of-thought (CoT) reasoning has shown great promise in enhancing the emotion understanding performance of large language models (LLMs). However, current fixed-length CoT methods struggle to balance reasoning depth and efficiency. Simple tasks (e.g., sentiment classification) are over-reasoned, while complex tasks (e.g., sarcasm understanding) lack depth. To fill this gap, we present Emotion-o1, an adaptive CoT framework that dynamically adjusts reasoning length based on task complexity. Emotion-o1 is trained by distilling adaptive CoT patterns from a large reasoning model (LRM), followed by supervised fine-tuning and reinforcement learning with a four-part reward targeting accuracy, brevity, structure, and redundancy. Experimental results on four emotion tasks highlight: (1) Emotion-o1 demonstrates significant improvements over its backbone, with F1 score increases of 11\%↑(Sentiment), 14\%↑(Emotion), 18\%↑(Humor), and 27\%↑(Sarcasm). (2) In sentiment and emotion tasks, our 8B model demonstrates superior performance against SoTA LLMs, outperforming Grok‑3 by 2.1\% in sentiment and within 1\% of OpenAI‑o1 in emotion. (3) The framework maintains accuracy while reducing reasoning length by 83\% compared to OpenAI-o1, demonstrating effective precision-efficiency optimization. From a lower-cost perspective, the framework also empowers SLMs to achieve reasoning capabilities comparable to larger ones.

## item_id: m_0187

TITLE: LAVAE: Disentangling Location and Appearance

ABSTRACT: We propose a probabilistic generative model for unsupervised learning of structured, interpretable, object-based representations of visual scenes. We use amortized variational inference to train the generative model end-to-end. The learned representations of object location and appearance are fully disentangled, and objects are represented independently of each other in the latent space. Unlike previous approaches that disentangle location and appearance, ours generalizes seamlessly to scenes with many more objects than encountered in the training regime. We evaluate the proposed model on multi-MNIST and multi-dSprites data sets.

## item_id: m_0188

TITLE: EinSteinVI: General and Integrated Stein Variational Inference

ABSTRACT: Stein variational inference is a technique for approximate Bayesian inference that has recently gained popularity because it combines the scalability of variational inference (VI) with the flexibility of non-parametric inference methods.  While there has been considerable progress in developing algorithms for Stein variational inference,  integration in existing probabilistic programming languages (PPLs) with an easy-to-use interface is currently lacking.  EinSteinVI is a lightweight compostable library that integrates the latest Stein variational inference method with the PPL NumPyro (Phan et al., 2019).  EinSteinVI provides ELBO-within-Stein to support the use of custom inference programs (guides), implementations of a wide range of kernels, non-linear scaling of the repulsion force (Wang & Liu,2019b), and second-order gradient updates using matrix-valued kernels (Wang et al.,2019b). We illustrate EinSteinVI using toy examples and show results on par with or better than existing state-of-the-art methods for real-world problems. These include Bayesian neural networks for regression and a Stein-mixture deep Markov model, which shows EinSteinVI scales to large models with more than 500,000 parameters.

## item_id: m_0189

TITLE: Perception-Driven Curiosity with Bayesian Surprise

ABSTRACT: Intrinsic rewards in reinforcement learning provide a powerful algorithmic capability for agents to learn how to interact with their environment in a task-generic way. However, increased incentives for motivation can come at the cost of increased fragility to stochasticity. We introduce a method for computing an intrinsic reward for curiosity using metrics derived from sampling a latent variable model used to estimate dynamics. Ultimately, an estimate of the conditional probability of observed states is used as our intrinsic reward for curiosity. In our experiments, a video game agent uses our model to autonomously learn how to play Atari games using our curiosity reward in combination with extrinsic rewards from the game to achieve improved performance on games with sparse extrinsic rewards. When stochasticity is introduced in the environment, our method still demonstrates improved performance over the baseline.

## item_id: m_0190

TITLE: Predicting Infectiousness for Proactive Contact Tracing

ABSTRACT: The COVID-19 pandemic has spread rapidly worldwide, overwhelming manual contact tracing in many countries and resulting in widespread lockdowns for emergency containment. Large-scale digital contact tracing (DCT) has emerged as a potential solution to resume economic and social activity while minimizing spread of the virus. Various DCT methods have been proposed, each making trade-offs be-tween privacy, mobility restrictions, and public health. The most common approach, binary contact tracing (BCT), models infection as a binary event, informed only by an individual’s test results, with corresponding binary recommendations that either all or none of the individual’s contacts quarantine. BCT ignores the inherent uncertainty in contacts and the infection process, which could be used to tailor messaging to high-risk individuals, and prompt proactive testing or earlier warnings. It also does not make use of observations such as symptoms or pre-existing medical conditions, which could be used to make more accurate infectiousness predictions. In this paper, we use a recently-proposed COVID-19 epidemiological simulator to develop and test methods that can be deployed to a smartphone to locally and proactively predict an individual’s infectiousness (risk of infecting others) based on their contact history and other information, while respecting strong privacy constraints. Predictions are used to provide personalized recommendations to the individual via an app, as well as to send anonymized messages to the individual’s contacts, who use this information to better predict their own infectiousness, an approach we call proactive contact tracing (PCT). Similarly to other works, we find that compared to no tracing, all DCT methods tested are able to reduce spread of the disease and thus save lives, even at low adoption rates, strongly supporting a role for DCT methods in managing the pandemic. Further, we find a deep-learning based PCT method which improves over BCT for equivalent average mobility, suggesting PCT could help in safe re-opening and second-wave prevention.

## item_id: m_0191

TITLE: Experience replay for continual learning

ABSTRACT: Continual learning is the problem of learning new tasks or knowledge while protecting old knowledge and ideally generalizing from old experience to learn new tasks faster. Neural networks trained by stochastic gradient descent often degrade on old tasks when trained successively on new tasks with different data distributions. This phenomenon, referred to as catastrophic forgetting, is considered a major hurdle to learning with non-stationary data or sequences of new tasks, and prevents networks from continually accumulating knowledge and skills. We examine this issue in the context of reinforcement learning, in a setting where an agent is exposed to tasks in a sequence. Unlike most other work, we do not provide an explicit indication to the model of task boundaries, which is the most general circumstance for a learning agent exposed to continuous experience. While various methods to counteract catastrophic forgetting have recently been proposed, we explore a straightforward, general, and seemingly overlooked solution - that of using experience replay buffers for all past events - with a mixture of on- and off-policy learning, leveraging behavioral cloning. We show that this strategy can still learn new tasks quickly yet can substantially reduce catastrophic forgetting in both Atari and DMLab domains, even matching the performance of methods that require task identities. When buffer storage is constrained, we confirm that a simple mechanism for randomly discarding data allows a limited size buffer to perform almost as well as an unbounded one.

## item_id: m_0192

TITLE: Accelerating Diffusion Language Models Inference via Local Determinism Propagation

ABSTRACT: Diffusion large language models (dLLMs) represent a significant advancement in text generation, offering parallel token decoding capabilities. However, existing open-source implementations suffer from quality-speed trade-offs that impede their practical deployment. Conservative sampling strategies typically decode only the most confident token per step to ensure quality (i.e., greedy decoding), at the cost of inference efficiency due to repeated redundant refinement iterations--a phenomenon we term delayed decoding. Through systematic analysis of dLLM decoding dynamics, we characterize this delayed decoding behavior and propose a training-free adaptive parallel decoding strategy, named LocalLeap, to address these inefficiencies. LocalLeap is built on two fundamental empirical principles: local determinism propagation centered on high-confidence anchors and progressive spatial consistency decay. By applying these principles, LocalLeap identifies anchors and performs localized relaxed parallel decoding within bounded neighborhoods, achieving substantial inference step reduction through early commitment of already-determined tokens without compromising output quality. Comprehensive evaluation on various benchmarks demonstrates that LocalLeap achieves 6.94$\times$ throughput improvements and reduces decoding steps to just 14.2\% of the original requirement, achieving these gains with negligible performance impact.

## item_id: m_0193

TITLE: SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models

ABSTRACT: Evaluating the response quality of large language models (LLMs) for open-ended questions poses a significant challenge, especially given the subjectivity and multi-dimensionality of "quality" in natural language generation. Existing LLM evaluators often neglect that different scenarios require distinct evaluation criteria. In this work, we propose **SaMer**, a scenario-aware multi-dimensional evaluator designed to provide both overall and fine-grained assessments of LLM-generated responses. Unlike fixed-dimension evaluation approaches, SaMer adapts to different scenarios by automatically identifying and prioritizing relevant evaluation dimensions tailored to the given query. To achieve this, we construct a large-scale fine-grained preference dataset spanning multiple real-world scenarios, each with distinct evaluation dimensions. We then leverage a text embedding model combined with three specialized heads to predict the appropriate evaluation dimensions and corresponding scores, as well as the respective weights that contribute to the overall score. The resulting model offers fine-grained and interpretable evaluations and shows robust adaptability across diverse scenarios. Extensive experiments on eight single rating and pairwise comparison datasets demonstrate that SaMer outperforms existing baselines in a variety of evaluation tasks, showcasing its robustness, versatility, and generalizability.

## item_id: m_0194

TITLE: Structural Fairness-aware Active Learning for Graph Neural Networks

ABSTRACT: Graph Neural Networks (GNNs) have seen significant achievements in semi-supervised node classification. Yet, their efficacy often hinges on access to high-quality labeled node samples, which may not always be available in real-world scenarios. While active learning is commonly employed across various domains to pinpoint and label high-quality samples based on data features, graph data present unique challenges due to their intrinsic structures that render nodes non-i.i.d. Furthermore, biases emerge from the positioning of labeled nodes; for instance, nodes closer to the labeled counterparts often yield better performance. To better leverage graph structure and mitigate structural bias in active learning, we present a unified optimization framework (SCARCE), which is also easily incorporated with node features.  Extensive experiments demonstrate that the proposed method not only improves the GNNs performance but also paves the way for more fair results.

## item_id: m_0195

TITLE: A Graph Neural Network Approach to Automated Model Building in Cryo-EM Maps

ABSTRACT: Electron cryo-microscopy (cryo-EM) produces three-dimensional (3D) maps of the electrostatic potential of biological macromolecules, including proteins. At sufficient resolution, the cryo-EM maps, along with some knowledge about the imaged molecules, allow de novo atomic modelling. Typically, this is done through a laborious manual process. Recent advances in machine learning applications to protein structure prediction show potential for automating this process. Taking inspiration from these techniques, we have built ModelAngelo for automated model building of proteins in cryo-EM maps. ModelAngelo first uses a residual convolutional neural network (CNN) to initialize a graph representation with nodes assigned to individual amino acids of the proteins in the map and edges representing the protein chain. The graph is then refined with a graph neural network (GNN) that combines the cryo-EM data, the amino acid sequence data and prior knowledge about protein geometries. The GNN refines the geometry of the protein chain and classifies the amino acids for each of its nodes. The final graph is post-processed with a hidden Markov model (HMM) search to map each protein chain to entries in a user provided sequence file. Application to 28 test cases shows that ModelAngelo outperforms state-of-the-art and approximates manual building for cryo-EM maps with resolutions better than 3.5 A.

## item_id: m_0196

TITLE: How vulnerable is my learned policy? Adversarial attacks on modern behavioral cloning policies

ABSTRACT: Learning from Demonstration (LfD) algorithms have shown promising results in robotic manipulation tasks, but their vulnerability to adversarial attacks remains underexplored. This paper presents a comprehensive study of adversarial attacks on both classic and recently proposed algorithms, including Behavior Cloning (BC), LSTM-GMM, Implicit Behavior Cloning (IBC), Diffusion Policy (DP), and VQ-Behavior Transformer (VQ-BET). We study the vulnerability of these methods to untargeted, targeted and universal adversarial perturbations. While explicit policies, such as BC, LSTM-GMM and VQ-BET can be attacked in the same manner as standard computer vision models, we find that attacks for implicit and denoising policy models are nuanced and require developing novel attack methods.
Our experiments on several simulated robotic manipulation tasks reveal that most of the current methods are highly vulnerable to adversarial perturbations. We also investigate the transferability of attacks across algorithms, architectures, and tasks and provide insights into the generalizability of adversarial perturbations in LfD. We find that the success rate of the transfer attacks is highly dependent on the task, raising necessity for more fine-grained metrics that capture both the task difficulties and baseline performance of the algorithms. In summary, our findings highlight the vulnerabilities of modern BC algorithms, paving way for future work in addressing such limitations.

## item_id: m_0197

TITLE: Palu: KV-Cache Compression with Low-Rank Projection

ABSTRACT: Post-training KV-Cache compression methods typically either sample a subset of effectual tokens or quantize the data into lower numerical bit width. However, these methods cannot exploit redundancy in the hidden dimension of the KV tenors. This paper presents a hidden dimension compression approach called Palu, a KV-Cache compression framework that utilizes low-rank projection to reduce inference-time LLM memory usage. Palu decomposes the linear layers into low-rank matrices, caches compressed intermediate states, and reconstructs the full keys and values on the fly. To improve accuracy, compression rate, and efficiency, Palu further encompasses (1) a medium-grained low-rank decomposition scheme, (2) an efficient rank search algorithm, (3) low-rank-aware quantization compatibility enhancements, and (4) an optimized GPU kernel with matrix fusion. Extensive experiments with popular LLMs show that Palu compresses KV-Cache by 50% while maintaining strong accuracy and delivering up to 1.89× speedup on the RoPE-based attention module. When combined with quantization, Palu’s
inherent quantization-friendly design yields small to negligible extra accuracy degradation while saving additional memory than quantization-only methods and achieving up to 2.91× speedup for the RoPE-based attention. Moreover, it maintains comparable or even better accuracy (up to 1.19 lower perplexity) compared to quantization-only methods. These results demonstrate Palu’s superior capability to effectively address the efficiency and memory challenges of LLM inference posed by KV-Cache. Our code is publicly available at: https://github.com/shadowpa0327/Palu.

## item_id: m_0198

TITLE: On the Need for Topology-Aware Generative Models for Manifold-Based Defenses

ABSTRACT: ML algorithms or models, especially deep neural networks (DNNs), have shown significant promise in several areas. However, recently researchers have demonstrated that ML algorithms, especially DNNs, are vulnerable to adversarial examples (slightly perturbed samples that cause mis-classification). Existence of adversarial examples has hindered deployment of ML algorithms in safety-critical sectors, such as security. Several defenses for adversarial examples exist in the literature. One of the important classes of defenses are manifold-based defenses, where a sample is "pulled back" into the data manifold before classifying. These defenses rely on the manifold assumption (data lie in a manifold of lower dimension than the input space). These defenses use a generative model to approximate the input distribution. This paper asks the following question: do the generative models used in manifold-based defenses need to be topology-aware? Our paper suggests the answer is yes. We provide theoretical and empirical evidence to support our claim.

## item_id: m_0199

TITLE: Beyond Deep Learning: An Evolutionary Feature Engineering Approach to Tabular Data Classification

ABSTRACT: In recent years, deep learning has achieved impressive performance in the computer vision and natural language processing domains. In the tabular data classification scenario, with the emergence of the transformer architecture, a number of algorithms have been reported to yield better results than conventional tree-based models. Most of these methods attribute the success of deep learning methods to the expressive feature construction capability of neural networks. Nonetheless, in real practice, manually designed high-order features with traditional machine learning methods are still widely used because neural-network-based features can be easy to over-fitting. In this paper, we propose an evolution-based feature engineering algorithm to imitate the manual feature construction process through trial and improvement. Importantly, the evolutionary method provides an opportunity to optimize cross-validation loss, where gradient methods fail to do so. On a large-scale classification benchmark of 119 datasets, the experimental results demonstrate that the proposed method outperforms existing fine-tuned state-of-the-art tree-based and deep-learning-based classification algorithms.

## item_id: m_0200

TITLE: Deep Unsupervised Clustering with Gaussian Mixture Variational Autoencoders

ABSTRACT: We study a variant of the variational autoencoder model (VAE) with a Gaussian mixture as a prior distribution, with the goal of performing unsupervised clustering through deep generative models. We observe that the known problem of over-regularisation that has been shown to arise in regular VAEs also manifests itself in our model and leads to cluster degeneracy. We show that a heuristic called minimum information constraint that has been shown to mitigate this effect in VAEs can also be applied to improve unsupervised clustering performance with our model. Furthermore we analyse the effect of this heuristic and provide an intuition of the various processes with the help of visualizations. Finally, we demonstrate the performance of our model on synthetic data, MNIST and SVHN, showing that the obtained clusters are distinct, interpretable and result in achieving competitive performance on unsupervised clustering to the state-of-the-art results.
