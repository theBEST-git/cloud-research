# Batch 30 — 100 items

## item_id: m_2901

TITLE: Defense-GAN: Protecting Classifiers Against Adversarial Attacks Using Generative Models

ABSTRACT: In recent years, deep neural network approaches have been widely adopted for machine learning tasks, including classification. However, they were shown to be vulnerable to adversarial perturbations: carefully crafted small perturbations can cause misclassification of legitimate images. We propose Defense-GAN, a new framework leveraging the expressive capability of generative models to defend deep neural networks against such attacks. Defense-GAN is trained to model the distribution of unperturbed images. At inference time, it finds a close output to a given image which does not contain the adversarial changes. This output is then fed to the classifier. Our proposed method can be used with any classification model and does not modify the classifier structure or training procedure. It can also be used as a defense against any attack as it does not assume knowledge of the process for generating the adversarial examples. We empirically show that Defense-GAN is consistently effective against different attack methods and improves on existing defense strategies.

## item_id: m_2902

TITLE: Learn With Imagination: Safe Set Guided State-wise Constrained Policy Optimization

ABSTRACT: Deep reinforcement learning (RL) excels in various control tasks, yet the absence of safety guarantees hampers its real-world applicability. In particular, explorations during learning usually results in safety violations, while the RL agent learns from those mistakes. On the other hand, safe control techniques ensure persistent safety satisfaction but demand strong priors on system dynamics, which is usually hard to obtain in practice. To address these problems, we present Safe Set Guided State-wise Constrained Policy Optimization (S-3PO), a pioneering algorithm generating state-wise safe optimal policies with zero training violations, i.e., learning without mistakes. S-3PO first employs a safety-oriented monitor with black-box dynamics to ensure safe exploration. It then enforces a unique cost for the RL agent to converge to optimal behaviors within safety constraints.  S-3PO outperforms existing methods in high-dimensional robotics tasks, managing state-wise constraints with zero training violation. This innovation marks a significant stride towards real-world safe RL deployment.

## item_id: m_2903

TITLE: Contrastive Semi-Supervised Domain Adaptation with von Mises-Fisher for Class Imbalance Mitigation

ABSTRACT: In contrast to Unsupervised Domain Adaptation (UDA) methods that rely solely on unlabeled data, Semi-supervised Domain Adaptation (SSDA) aims to enhance classification accuracy and generalization by incorporating a small amount of labeled samples from the target domain. However, a central challenge in SSDA is effectively addressing the distributional discrepancy between the source and target domains, particularly when labeled target data is scarce. While existing SSDA approaches have alleviated this issue to some extent, the persistent problem of class imbalance remains a critical obstacle. To address this challenge, we propose a novel Contrastive Semi-Supervised Domain Adaptation (cSSDA) algorithm based on the von Mises-Fisher (vMF) distribution. The core idea is to integrate the vMF distribution into the contrastive learning framework to refine the contrastive loss, enabling the construction of an infinite number of contrastive pairs. This approach helps the model better handle the class imbalance inherent in SSDA. Specifically, the vMF distribution excels at modeling directional data in high-dimensional spaces, enhancing the model's ability to capture similarities and differences between source and target domains during contrastive learning. Extensive experiments conducted on two widely-used benchmark datasets demonstrate that our method consistently outperforms existing SSDA approaches.

## item_id: m_2904

TITLE: PeFoo-L: A General Framework for Preconditioned Enhanced Forward-Only Optimizer in LLM Fine-tuning on the Edge

ABSTRACT: Fine-tuning Large Language Models (LLMs) on resource-constrained edge devices is a critical but challenging task, primarily due to the prohibitive memory and computational costs of backpropagation. While forward-only optimizers like MeZO mitigate these costs by eliminating the backward pass, they often suffer from slow and unstable convergence, particularly on loss landscapes with heterogeneous curvature. To address this limitation, we introduce PeFoo, a general framework for preconditioner enhanced forward only optimizer. PeFoo integrates a carefully designed preconditioning strategy into the forward-only paradigm, corrects a fundamental source of bias and instability present in prior work HiZOO. Furthermore, to counteract the memory overhead introduced by the preconditioner itself, we propose PeFoo-L, which employs a layer-wise update strategy. This approach constrains preconditioner storage and weight updates to a single layer per iteration, reducing the overall memory footprint and data traffic.
Experimental results validate the effectiveness of our framework. On the OPT-1.3B model, PeFoo surpasses the accuracy of leading zeroth-order methods MeZO and HiZOO by 2.7\% and 2.1\%, respectively. Furthermore, PeFoo-L achieves a memory footprint reduction of over 2.73$\times$ and 1.75$\times$ compared to Adam and HiZOO, while delivering faster convergence speed compared to MeZO and HiZOO.

## item_id: m_2905

TITLE: Entropic gradient descent algorithms and wide flat minima

ABSTRACT: The properties of flat minima in the empirical risk landscape of neural networks have been debated for some time. Increasing evidence suggests they possess better generalization capabilities with respect to sharp ones. In this work we first discuss the relationship between alternative measures of flatness: The local entropy, which is useful for analysis and algorithm development, and the local energy, which is easier to compute and was shown empirically in extensive tests on state-of-the-art networks to be the best predictor of generalization capabilities. We show semi-analytically in simple controlled scenarios that these two measures correlate strongly with each other and with generalization. Then, we extend the analysis to the deep learning scenario by extensive numerical validations. We study two algorithms, Entropy-SGD and Replicated-SGD, that explicitly include the local entropy in the optimization objective. We devise a training schedule by which we consistently find flatter minima (using both flatness measures), and improve the generalization error for common architectures (e.g. ResNet, EfficientNet).

## item_id: m_2906

TITLE: E(n) Equivariant Topological Neural Networks

ABSTRACT: Graph neural networks excel at modeling pairwise interactions, but they cannot flexibly accommodate higher-order interactions and features. Topological deep learning (TDL) has emerged recently as a promising tool for addressing this issue. TDL enables the principled modeling of arbitrary multi-way, hierarchical higher-order interactions by operating on combinatorial topological spaces, such as simplicial or cell complexes, instead of graphs. However, little is known about how to leverage geometric features such as positions and velocities for TDL. This paper introduces E(n)-Equivariant Topological Neural Networks (ETNNs), which are E(n)-equivariant message-passing networks operating on combinatorial complexes, formal objects unifying graphs, hypergraphs, simplicial, path, and cell complexes. ETNNs incorporate geometric node features while respecting rotation, reflection, and translation equivariance. Moreover, being TDL models, ETNNs are natively ready for settings with heterogeneous interactions.  We provide a theoretical analysis to show the improved expressiveness of ETNNs over architectures for geometric graphs. We also show how E(n)-equivariant variants of TDL models can be directly derived from our framework. The broad applicability of ETNNs is demonstrated through two tasks of vastly different scales: i) molecular property prediction on the QM9 benchmark and ii) land-use regression for hyper-local estimation of air pollution with multi-resolution irregular geospatial data.  The results indicate that ETNNs are an effective tool for learning from diverse types of richly structured data, as they match or surpass SotA equivariant TDL models with a significantly smaller computational burden, thus highlighting the benefits of a principled geometric inductive bias. Our implementation of ETNNs can be found at https://github.com/NSAPH-Projects/topological-equivariant-networks.

## item_id: m_2907

TITLE: $Q$-learning with regularization converges with non-linear non-stationary features

ABSTRACT: The deep $Q$-learning architecture is a neural network composed of non-linear hidden layers that learn features of states and actions and a final linear layer that learns the $Q$-values of the features. The parameters of both components can possibly diverge. Regularization of the updates is known to solve the divergence problem of fully linear architectures, where features are stationary and known a priori. We propose a deep $Q$-learning scheme that uses regularization of the final linear layer of architecture, updating it along a faster time-scale, and stochastic full-gradient descent updates for the non-linear features at a slower time-scale. We prove the proposed scheme converges with probability 1. Finally, we provide a bound on the error introduced by regularization of the final linear layer of the architecture.

## item_id: m_2908

TITLE: Neural Causal Regularization under the Independence of Mechanisms Assumption

ABSTRACT: Neural networks provide a powerful framework for learning the association between input and response variables and making accurate predictions. However, in many applications such as healthcare, it is important to identify causal relationships between the inputs and the response variables to be able to change the response variables by intervention on the inputs. In pursuit of models whose predictive power comes maximally from causal variables, we propose a novel causal regularizer based on the independence of mechanisms assumption. We utilize the causal regularizer to steer deep neural network architectures towards causally-interpretable solutions. We perform a large-scale analysis of electronic health records. Employing expert's judgment as the causal ground-truth, we show that our causally-regularized algorithm outperforms its L1-regularized equivalence both in predictive performance as well as causal relevance. Finally, we show that the proposed causal regularizer can be used together with representation learning algorithms to yield up to 20% improvement in the causality score of the generated hypotheses.

## item_id: m_2909

TITLE: A General Computational Framework to Measure the Expressiveness of Complex Networks using a Tight Upper Bound of Linear Regions

ABSTRACT: The expressiveness of deep neural network (DNN) is a perspective to understand the surprising performance of DNN. The number of linear regions, i.e. pieces that a piece-wise-linear function represented by a DNN, is generally used to measure the expressiveness. And the upper bound of regions number partitioned by a rectifier network, instead of the number itself, is a more practical measurement of expressiveness of a rectifier DNN. In this work, we propose a new and tighter upper bound of regions number. Inspired by the proof of this upper bound and the framework of matrix computation in \citet{hinz2019framework}, we propose a general computational approach to compute a tight upper bound of regions number for theoretically any network structures (e.g. DNN with all kind of skip connections and residual structures). Our experiments show our upper bound is tighter than existing ones, and explain why skip connections and residual structures can improve network performance.

## item_id: m_2910

TITLE: Risk Aware Negative Sampling in Link Prediction

ABSTRACT: It is commonly believed that Message Passing Neural Networks (MPNNs) struggle in link prediction settings due to limitations in their expressive power. Recent work has focused on developing more expressive model classes, which are capable of learning link representations through techniques such as labeling tricks, the inclusion of structural features, or the use of subgraph methods. These approaches have yielded significant performance improvements across a range of benchmark datasets. However, an interesting question remains: have we fully wrung out the performance by optimizing the other aspects of the training process? In this work, we present results that indicate that significant amounts of model performance have been left on the table by the use of easy negative-samples during training. We theoretically explore the generalization gap and excess risk to quantify the performance loss caused by easy negatives. Motivated by this analysis, we introduce Risk Aware Negative Sampling in Link Prediction (RANS), which efficiently performs dynamic hard-negative-mining. Empirical results show that a simple GCN augmented by RANS realizes between 20\% and 50\% improvements in predictive accuracy when compared with the same model trained with standard negative samples.

## item_id: m_2911

TITLE: Never Revisit: Continuous Exploration in Multi-Agent Reinforcement Learning

ABSTRACT: Recently, intrinsic motivations are wildly used for exploration in multi-agent reinforcement learning. We discover that coming with intrinsic rewards is the issue of revisitation -- the relative values of intrinsic rewards fluctuate, causing a sub-space visited before becomes attractive after a period of exploration to other areas. Consequently, agents risk exploring some sub-spaces repeatedly. In this paper, we formally define the concept of revisitation, based on which we propose an observation-distribution matching approach to detect the appearance of revisitation. To avoid it, we add branches to agents' local Q-networks and the mixing network to separate sub-spaces which have already been revisited. Furthermore, to prevent adding branches excessively, we design intrinsic rewards to reduce the probability of and penalize the occurrence of revisitation. By virtue of these advances, our method achieves superior performance on three challenging Google Research Football (GRF) scenarios with sparse rewards. 

## item_id: m_2912

TITLE: DREAM: Domain-free Reverse Engineering Attributes of Black-box Model

ABSTRACT: Deep learning models are usually black boxes when deployed on machine learning platforms. Prior works have shown that the attributes (e.g., the number of convolutional layers) of a target black-box neural network can be exposed through a sequence of queries. There is a crucial limitation that these works assume the dataset used for training the target model to be known beforehand, and leverage this dataset for model attribute attack. However, it is difficult to access the training dataset of the target black-box model in reality. Therefore, whether the attributes of a target black-box model could be still revealed in this case is doubtful. In this paper, we investigate a new problem of Domain-free Reverse Engineering the Attributes of a black-box target Model, called DREAM, without requiring the model's training dataset available, and  put forward a general and principled framework by casting this problem as an out of distribution (OOD) generalization problem. At the heart of our framework, we devise a multi-discriminator generative adversarial network (MDGAN) to learn domain invariant features. Based on these features, we can learn a domain-free model to inversely infer the attributes of a target black-box model with unknown training data. This makes our method one of the kinds that can gracefully apply to an arbitrary domain for model attribute reverse engineering with good generalization ability.  Extensive experimental studies are conducted and the results validate the superiority of our proposed method over the baselines.

## item_id: m_2913

TITLE: Variance-Aware Sparse Linear Bandits

ABSTRACT: It is well-known that for sparse linear bandits, when ignoring the dependency on sparsity which is much smaller than the ambient dimension, the worst-case minimax regret is $\widetilde{\Theta}\left(\sqrt{dT}\right)$ where $d$ is the ambient dimension and $T$ is the number of rounds. On the other hand, in the benign setting where there is no noise and the action set is the unit sphere, one can use divide-and-conquer to achieve $\widetilde{\mathcal O}(1)$ regret, which is (nearly) independent of $d$ and $T$. In this paper, we present the first variance-aware regret guarantee for sparse linear bandits:  $\widetilde{\mathcal O}\left(\sqrt{d\sum_{t=1}^T \sigma_t^2} + 1\right)$, where $\sigma_t^2$ is the variance of the noise at the $t$-th round. This bound naturally interpolates the regret bounds for the worst-case constant-variance regime (i.e., $\sigma_t \equiv \Omega(1)$) and the benign deterministic regimes (i.e., $\sigma_t \equiv 0$). To achieve this variance-aware regret guarantee, we develop a general framework that converts any variance-aware linear bandit algorithm to a variance-aware algorithm for sparse linear bandits in a "black-box" manner. Specifically, we take two recent algorithms as black boxes to illustrate that the claimed bounds indeed hold, where the first algorithm can handle unknown-variance cases and the second one is more efficient.

## item_id: m_2914

TITLE: GeoLLM: Extracting Geospatial Knowledge from Large Language Models

ABSTRACT: The application of machine learning (ML) in a range of geospatial tasks is increasingly common but often relies on globally available covariates such as satellite imagery that can either be expensive or lack predictive power.
Here we explore the question of whether the vast amounts of knowledge found in Internet language corpora, now compressed within large language models (LLMs), can be leveraged for geospatial prediction tasks. 
We first demonstrate that LLMs embed remarkable spatial information about locations, but 
naively querying LLMs using geographic coordinates alone is ineffective in predicting key indicators like population density. 
We then present GeoLLM, a novel method that can effectively extract geospatial knowledge from LLMs with auxiliary map data from OpenStreetMap.
We demonstrate the utility of our approach across multiple tasks of central interest to the international community, including the measurement of population density and economic livelihoods.
Across these tasks, our method demonstrates a 70\% improvement in performance (measured using Pearson's $r^2$) relative to baselines that use nearest neighbors or use information directly from the prompt, and performance equal to or exceeding satellite-based benchmarks in the literature.
With GeoLLM, we observe that GPT-3.5 outperforms Llama 2 and RoBERTa by 19\% and 51\% respectively, suggesting that the performance of our method scales well with the size of the model and its pretraining dataset.
Our experiments reveal that LLMs are remarkably sample-efficient, rich in geospatial information, and robust across the globe.
Crucially, GeoLLM shows promise in mitigating the limitations of existing geospatial covariates and complementing them well.
Code is available on the project website: https://rohinmanvi.github.io/GeoLLM

## item_id: m_2915

TITLE: Connecting Graph Convolution and Graph PCA

ABSTRACT: Graph convolution operator of the GCN model is originally motivated from a localized first-order approximation of spectral graph convolutions. This work stands on a different view; establishing a mathematical connection between graph convolution and graph-regularized PCA (GPCA). Based on this connection, the GCN architecture, shaped by stacking graph convolution layers, shares a close relationship with stacking GPCA. We empirically demonstrate that the unsupervised embeddings by GPCA paired with a 1- or 2-layer MLP achieves similar or even better performance than many sophisticated baselines on semi-supervised node classification tasks across five datasets including Open Graph Benchmark. This suggests that the prowess of graph convolution is driven by graph based regularization. In addition, we extend GPCA to the (semi-)supervised setting and show that it is equivalent to GPCA on a graph extended with “ghost” edges between nodes of the same label. Finally, we capitalize on the discovered relationship to design an effective initialization strategy based on stacking GPCA, enabling GCN to converge faster and achieve robust performance at large number of layers.

## item_id: m_2916

TITLE: Adversarial Policy Gradient for Alternating Markov Games

ABSTRACT: Policy gradient reinforcement learning has been applied to two-player alternate-turn zero-sum games, e.g., in AlphaGo, self-play REINFORCE was used to improve the neural net model after supervised learning. In this paper, we emphasize that two-player zero-sum games with alternating turns, which have been previously formulated as Alternating Markov Games (AMGs), are different from standard MDP because of their two-agent nature. We exploit the difference in associated Bellman equations, which leads to different policy iteration algorithms. As policy gradient method is a kind of generalized policy iteration, we show how these differences in policy iteration are reflected in policy gradient for AMGs. We formulate an adversarial policy gradient and discuss potential possibilities for developing better policy gradient methods other than self-play REINFORCE. The core idea is to estimate the minimum rather than the mean for the “critic”. Experimental results on the game of Hex show the modified Monte Carlo policy gradient methods are able to learn better pure neural net policies than the REINFORCE variants. To apply learned neural weights to multiple board sizes Hex, we describe a board-size independent neural net architecture. We show that when combined with search, using a single neural net model, the resulting program consistently beats MoHex 2.0, the state-of-the-art computer Hex player, on board sizes from 9×9 to 13×13. 

## item_id: m_2917

TITLE: Prior Convictions: Black-box Adversarial Attacks with Bandits and Priors

ABSTRACT: We study the problem of generating adversarial examples in a black-box setting in which only loss-oracle access to a model is available. We introduce a framework that conceptually unifies much of the existing work on black-box attacks, and demonstrate that the current state-of-the-art methods are optimal in a natural sense. Despite this optimality, we show how to improve black-box attacks by bringing a new element into the problem: gradient priors. We give a bandit optimization-based algorithm that allows us to seamlessly integrate any such priors, and we explicitly identify and incorporate two examples. The resulting methods use two to four times fewer queries and fail two to five times less than the current state-of-the-art. The code for reproducing our work is available at https://git.io/fAjOJ.

## item_id: m_2918

TITLE: All-but-the-Top: Simple and Effective Postprocessing for Word Representations

ABSTRACT: Real-valued word representations have transformed NLP applications; popular examples are word2vec and GloVe, recognized for their ability to capture linguistic regularities. In this paper, we demonstrate a {\em very simple}, and yet counter-intuitive, postprocessing technique -- eliminate the common mean vector and a few top dominating directions from the word vectors -- that renders off-the-shelf representations {\em even stronger}. The postprocessing is empirically validated on a variety of lexical-level intrinsic tasks (word similarity, concept categorization, word analogy) and sentence-level tasks (semantic textural similarity and text classification) on multiple datasets and with a variety of representation methods and hyperparameter choices in multiple languages; in each case, the processed representations are consistently better than the original ones. 

## item_id: m_2919

TITLE: An Inductive Bias for Distances: Neural Nets that Respect the Triangle Inequality

ABSTRACT: Distances are pervasive in machine learning. They serve as similarity measures, loss functions, and learning targets; it is said that a good distance measure solves a task. When defining distances, the triangle inequality has proven to be a useful constraint, both theoretically---to prove convergence and optimality guarantees---and empirically---as an inductive bias. Deep metric learning architectures that respect the triangle inequality rely, almost exclusively, on Euclidean distance in the latent space. Though effective, this fails to model two broad classes of subadditive distances, common in graphs and reinforcement learning: asymmetric metrics, and metrics that cannot be embedded into Euclidean space. To address these problems, we introduce novel architectures that are guaranteed to satisfy the triangle inequality. We prove our architectures universally approximate norm-induced metrics on $\mathbb{R}^n$, and present a similar result for modified Input Convex Neural Networks. We show that our architectures outperform existing metric approaches when modeling graph distances and have a better inductive bias than non-metric approaches when training data is limited in the multi-goal reinforcement learning setting.


## item_id: m_2920

TITLE: Weighted Risk Invariance for Density-Aware Domain Generalization

ABSTRACT: Learning how to generalize training performance to unseen test distributions is essential to building robust, practically useful models. To this end, many recent studies focus on learning invariant features from multiple domains. Our first observation is that the performance of existing invariant learning methods can degrade under covariate shift. To address this problem, we focus on finding invariant predictors from multiple, potentially shifted invariant feature distributions. We propose a novel optimization problem, Weighted Risk Invariance (WRI), and we show that the solution to this problem provably achieves out-of-distribution generalization. We also introduce an algorithm to practically solve the WRI problem that learns the density of invariant features and model parameters simultaneously, and we demonstrate our approach outperforms previous invariant learning methods under covariate shift in the invariant features. Finally, we show that the learned density over invariant features effectively detects when the features are out-of-distribution.

## item_id: m_2921

TITLE: An efficient algorithm for entropic optimal transport under martingale-type constraints

ABSTRACT: This work introduces novel computational methods for entropic optimal transport (OT) problems under martingale-type conditions.
The problems can map to a prevalent class of OT problems with structural constraints, encompassing the discrete martingale optimal transport (MOT) problem, as the (super-)martingale conditions are equivalent to row-wise (in-)equality constraints on the coupling matrix. Inspired by the recent empirical success of Sinkhorn-type algorithms, we propose an entropic formulation for the MOT problem and introduce Sinkhorn-type algorithms with sparse Newton iterations that utilize the (approximate) sparsity of the Hessian matrix of the dual objective. As exact martingale conditions are typically infeasible, we adopt entropic regularization to find an approximate constraint satisfied solution. We show that in practice the proposed algorithms enjoy both super-exponential convergence and robustness with controllable thresholds for total constraint violations.

## item_id: m_2922

TITLE: Trusting SVM for Piecewise Linear CNNs

ABSTRACT: We present a novel layerwise optimization algorithm for the learning objective of Piecewise-Linear Convolutional Neural Networks (PL-CNNs), a large class of convolutional neural networks. Specifically, PL-CNNs employ piecewise linear non-linearities such as the commonly used ReLU and max-pool, and an SVM classifier as the final layer. The key observation of our approach is that the prob- lem corresponding to the parameter estimation of a layer can be formulated as a difference-of-convex (DC) program, which happens to be a latent structured SVM. We optimize the DC program using the concave-convex procedure, which requires us to iteratively solve a structured SVM problem. This allows to design an opti- mization algorithm with an optimal learning rate that does not require any tuning. Using the MNIST, CIFAR and ImageNet data sets, we show that our approach always improves over the state of the art variants of backpropagation and scales to large data and large network settings.

## item_id: m_2923

TITLE: Dynamics-aware Skill Generation from Behaviourally Diverse Demonstrations

ABSTRACT: Learning from demonstrations (LfD) provides a data-efficient way for a robot to learn a task by observing humans performing the task, without the need for an explicit reward function. However, in many real-world scenarios (e.g., driving a car) humans often perform the same task in different ways, motivated not only by the primary objective of the task (e.g., reaching the destination safely) but also by their individual preferences (e.g., different driving behaviours), leading to a multi-modal distribution of demonstrations. In this work, we consider an LfD problem, where the reward function for the main objective of the task is known to the learning agent; however, the individual preferences leading to the variations in the demonstrations are unknown. We show that current LfD approaches learn policies that either track a single mode or the mean of the demonstration distribution. In contrast, we propose an algorithm to learn a diverse set of policies to perform the task, capturing the different modes in the demonstrations due to the diverse preferences of the individuals. We show that we can build a parameterised solution space that captures different behaviour patterns from the demonstrations. Then, a set of policies can be generated in solution space that generate a diverse range of behaviours that go beyond the provided demonstrations.

## item_id: m_2924

TITLE: Co-manifold learning with missing data

ABSTRACT:  Representation learning is typically applied to only one mode of a data matrix, either its rows or columns. Yet in many applications, there is an underlying geometry to both the rows and the columns. We propose utilizing this coupled structure to perform co-manifold learning: uncovering the underlying geometry of both the rows and the columns of a given matrix, where we focus on a missing data setting. Our unsupervised approach consists of three components.  We first solve a family of optimization problems to estimate a complete matrix at multiple scales of smoothness. We then use this collection of smooth matrix estimates to compute pairwise distances on the rows and columns based on a new multi-scale metric that implicitly introduces a coupling between the rows and the columns.  Finally, we construct row and column representations from these multi-scale metrics.  We demonstrate that our approach outperforms competing methods in both data visualization and clustering.  

## item_id: m_2925

TITLE: Hierarchical Adversarially Learned Inference

ABSTRACT: We propose a novel hierarchical generative model with a simple Markovian structure and a corresponding inference model. Both the generative and inference model are trained using the adversarial learning paradigm. We demonstrate that the hierarchical structure supports the learning of progressively more abstract representations as well as providing semantically meaningful reconstructions with different levels of fidelity. Furthermore, we show that minimizing the Jensen-Shanon divergence between the generative and inference network is enough to minimize the reconstruction error.  The resulting semantically meaningful hierarchical latent structure discovery is exemplified on the CelebA dataset.  There, we show that the features learned by our model in an unsupervised way outperform the best handcrafted features. Furthermore, the extracted features remain competitive when compared to several recent deep supervised approaches on an attribute prediction task on CelebA. Finally, we leverage the model's inference network to achieve state-of-the-art performance on a semi-supervised variant of the MNIST digit classification task. 

## item_id: m_2926

TITLE: Theoretical and Empirical Study of Adversarial Examples

ABSTRACT: Many techniques are developed to defend against adversarial examples at scale. So far, the most successful defenses generate adversarial examples during each training step and add them to the training data. Yet, this brings significant computational overhead.  In this paper, we investigate defenses against adversarial attacks. First, we propose feature smoothing, a simple data augmentation method with little computational overhead. Essentially, feature smoothing trains a neural network on virtual training data as an interpolation of features from a pair of samples, with the new label remaining the same as the dominant data point.  The intuition behind feature smoothing is to generate virtual data points as close as adversarial examples, and to avoid the computational burden of generating data during training. Our experiments on MNIST and CIFAR10 datasets explore different combinations of known regularization and data augmentation methods and show that feature smoothing with logit squeezing performs best for both adversarial and clean accuracy. Second, we propose an unified framework to understand the connections and differences among different efficient methods by analyzing the biases and variances of decision boundary. We show that under some symmetrical assumptions, label smoothing, logit squeezing, weight decay, mix up and feature smoothing all produce an unbiased estimation of the decision boundary with smaller estimated variance. All of those methods except weight decay are also stable when the assumptions no longer hold.

## item_id: m_2927

TITLE: Efficient Video Diffusion Models via Content-Frame Motion-Latent Decomposition

ABSTRACT: Video diffusion models have recently made great progress in generation quality, but are still limited by the high memory and computational requirements. This is because current video diffusion models often attempt to process high-dimensional videos directly. To tackle this issue, we propose content-motion latent diffusion model (CMD), a novel efficient extension of pretrained image diffusion models for video generation. Specifically, we propose an autoencoder that succinctly encodes a video as a combination of a content frame (like an image) and a low-dimensional motion latent representation. The former represents the common content, and the latter represents the underlying motion in the video, respectively. We generate the content frame by fine-tuning a pretrained image diffusion model, and we generate the motion latent representation by training a new lightweight diffusion model. A key innovation here is the design of a compact latent space that can directly utilizes a pretrained image diffusion model, which has not been done in previous latent video diffusion models. This leads to considerably better quality generation and reduced computational costs. For instance, CMD can sample a video 7.7$\times$ faster than prior approaches by generating a video of 512$\times$1024 resolution and length 16 in 3.1 seconds. Moreover, CMD achieves an FVD score of 238.3 on WebVid-10M, 18.5% better than the previous state-of-the-art of 292.4.

## item_id: m_2928

TITLE: Which Layer is Learning Faster? A Systematic Exploration of Layer-wise Convergence Rate for Deep Neural Networks

ABSTRACT: The deeply hierarchical structures enable deep neural networks (DNNs) to fit extremely complex target functions. However, the complex interaction between layers also makes the learning process of a particular layer poorly understood. This work demonstrates that the shallower layers of DNNs tend to converge faster than the deeper layers. We call this phenomenon Layer Convergence Bias. We also uncover the fundamental reason behind this phenomenon: Flatter local minima of shallower layers make their gradients more stable and predictive, allowing for faster training. Another surprising result is that the shallower layers tend to learn the low-frequency components of the target function, while the deeper layers usually learn the high-frequency components. It is consistent with the recent discovery that DNNs learn lower frequency objects faster.

## item_id: m_2929

TITLE: Deep Learning with Data Privacy via Residual Perturbation

ABSTRACT: Protecting data privacy in deep learning (DL) is at its urgency. Several celebrated privacy notions have been established and used for privacy-preserving DL. However, many of the existing mechanisms achieve data privacy at the cost of significant utility degradation. In this paper, we propose a stochastic differential equation principled \emph{residual perturbation} for privacy-preserving DL, which injects Gaussian noise into each residual mapping of ResNets. Theoretically, we prove that residual perturbation guarantees differential privacy (DP) and reduces the generalization gap for DL. Empirically, we show that residual perturbation outperforms the state-of-the-art DP stochastic gradient descent (DPSGD) in both membership privacy protection and maintaining the DL models' utility. For instance, in the process of training ResNet8 for the IDC dataset classification, residual perturbation obtains an accuracy of 85.7\% and protects the perfect membership privacy; in contrast, DPSGD achieves an accuracy of 82.8\% and protects worse membership privacy. 

## item_id: m_2930

TITLE: Parameter Space Noise for Exploration

ABSTRACT: Deep reinforcement learning (RL) methods generally engage in exploratory behavior through noise injection in the action space. An alternative is to add noise directly to the agent's parameters, which can lead to more consistent exploration and a richer set of behaviors. Methods such as evolutionary strategies use parameter perturbations, but discard all temporal structure in the process and require significantly more samples. Combining parameter noise with traditional RL methods allows to combine the best of both worlds. We demonstrate that both off- and on-policy methods benefit from this approach through experimental comparison of DQN, DDPG, and TRPO on high-dimensional discrete action environments as well as continuous control tasks.

## item_id: m_2931

TITLE: Feature Matters: A Stage-by-Stage Approach for Task Independent Knowledge Transfer

ABSTRACT: Convolutional Neural Networks (CNNs) become deeper and deeper in recent years, making the study of model acceleration imperative. It is a common practice to employ a shallow network, called student, to learn from a deep one, which is termed as teacher. Prior work made many attempts to transfer different types of knowledge from teacher to student, however, there are two problems remaining unsolved. Firstly, the knowledge used by existing methods is highly dependent on task and dataset, limiting their applications. Secondly, there lacks an effective training scheme for the transfer process, leading to degradation of performance. In this work, we argue that feature is the most important knowledge from teacher. It is sufficient for student to just learn good features regardless of the target task. From this discovery, we further present an efficient learning strategy to mimic features stage by stage. Extensive experiments demonstrate the importance of features and show that the proposed approach significantly narrows down the gap between student and teacher, outperforming the state-of-the-art methods.


## item_id: m_2932

TITLE: Unsupervised Control Through Non-Parametric Discriminative Rewards

ABSTRACT: Learning to control an environment without hand-crafted rewards or expert data remains challenging and is at the frontier of reinforcement learning research. We present an unsupervised learning algorithm to train agents to achieve perceptually-specified goals using only a stream of observations and actions. Our agent simultaneously learns a goal-conditioned policy and a goal achievement reward function that measures how similar a state is to the goal state. This dual optimization leads to a co-operative game, giving rise to a learned reward function that reflects similarity in controllable aspects of the environment instead of distance in the space of observations. We demonstrate the efficacy of our agent to learn, in an unsupervised manner, to reach a diverse set of goals on three domains -- Atari, the DeepMind Control Suite and DeepMind Lab.

## item_id: m_2933

TITLE: Learning how to explain neural networks: PatternNet and PatternAttribution

ABSTRACT: DeConvNet, Guided BackProp, LRP, were invented to better understand deep neural networks. We show that these methods do not produce the theoretically correct explanation for a linear model. Yet they are used on multi-layer networks with millions of parameters. This is a cause for concern since linear models are simple neural networks. We argue that explanation methods for neural nets should work reliably in the limit of  simplicity, the linear models. Based on our analysis of linear models we propose a generalization that yields two explanation techniques (PatternNet and PatternAttribution) that are theoretically sound for linear models and produce improved explanations for deep networks.


## item_id: m_2934

TITLE: Two-Step Offline Preference-Based Reinforcement Learning with Constrained Actions

ABSTRACT: Preference-based reinforcement learning (PBRL) in the offline setting has succeeded greatly in industrial applications such as chatbots. A two-step learning framework where one applies a reinforcement learning step after a reward modeling step has been widely adopted for the problem. However, such a method faces challenges from the risk of reward hacking and the complexity of reinforcement learning. To overcome the challenge, our insight is that both challenges come from the state-actions not supported in the dataset. Such state-actions are unreliable and increase the complexity of the reinforcement learning problem at the second step. Based on the insight, we develop a novel two-step learning method called PRC: preference-based reinforcement learning with constrained actions. The high-level idea is to limit the reinforcement learning agent to optimize over a constrained action space that excludes the out-of-distribution state-actions. We empirically verify that our method has high learning efficiency on various datasets in robotic control environments.

## item_id: m_2935

TITLE: Rethinking Backdoor Attacks on Dataset Distillation: A Kernel Method Perspective

ABSTRACT: Dataset distillation offers a potential means to enhance data efficiency in deep learning. Recent studies have shown its ability to counteract backdoor risks present in original training samples. In this study, we delve into the theoretical aspects of backdoor attacks and dataset distillation based on kernel methods. We introduce two new theory-driven trigger pattern generation methods specialized for dataset distillation. Following a comprehensive set of analyses and experiments, we show that our optimization-based trigger design framework informs effective backdoor attacks on dataset distillation. Notably, datasets poisoned by our designed trigger prove resilient against conventional backdoor attack detection and mitigation methods.  Our empirical results validate that the triggers developed using our approaches are proficient at executing resilient backdoor attacks.

## item_id: m_2936

TITLE: A Retrieve-and-Read Framework for Knowledge Graph Reasoning

ABSTRACT: Knowledge graph (KG) reasoning aims to infer new facts based on existing facts in the KG. Recent studies have shown that using the graph neighborhood of a node via graph neural networks (GNNs) provides more useful information compared to just using the query information. Conventional GNNs for KG reasoning follow the standard message-passing paradigm on the entire KG, which leads to over-smoothing of representations and also limits their scalability. At a large scale, it becomes computationally expensive to aggregate useful information from the entire KG for inference. To address limitations of existing KG reasoning frameworks, we propose a novel retrieve-and-read framework, which first retrieves a relevant subgraph context for the query and then jointly reasons over the context and the query with a high-capacity reader. As part of our exemplar instantiation for the new framework, we propose a novel Transformer-based GNN as the reader, which incorporates graph-based attention structure and cross-attention from deep fusing between query and context. This design enables the model to focus on salient subgraph information that is relevant to the query. Empirical experiments on two standard KG reasoning datasets demonstrate the competitive performance of the proposed method.

## item_id: m_2937

TITLE: DLVM: A modern compiler infrastructure for deep learning systems

ABSTRACT: Deep learning software demands reliability and performance. However, many of the existing deep learning frameworks are software libraries that act as an unsafe DSL in Python and a computation graph interpreter. We present DLVM, a design and implementation of a compiler infrastructure with a linear algebra intermediate representation, algorithmic differentiation by adjoint code generation, domain- specific optimizations and a code generator targeting GPU via LLVM. Designed as a modern compiler infrastructure inspired by LLVM, DLVM is more modular and more generic than existing deep learning compiler frameworks, and supports tensor DSLs with high expressivity. With our prototypical staged DSL embedded in Swift, we argue that the DLVM system enables a form of modular, safe and performant frameworks for deep learning.

## item_id: m_2938

TITLE: LEXA: Language-agnostic Cross-consistency Training for Question Answering Tasks

ABSTRACT: Cross-lingual information retrieval (CLIR) is a knowledge-intensive NLP task that requires a lot of domain-specific data in different languages. In previous works, authors were mostly using machine translation and iterative training for data mining. We considered the problem from another angle and present a novel cross-lingual pre-training and fine-tuning approach for CLIR tasks based on cross-lingual alignment. We present a new model LEXA-LM significantly improving cross-lingual knowledge transfer thus achieving new state-of-the-art in cross-lingual and monolingual question answering and cross-lingual sentence retrieval. Moreover, we show that our pre-training technique LEXA is a very powerful tool for a zero-shot scenario allowing to outperform some supervised methods.  

## item_id: m_2939

TITLE: Bootstrap3D: Improving Multi-view Diffusion Model with Synthetic Data

ABSTRACT: Recent years have witnessed remarkable progress in multi-view diffusion models for 3D content creation. However, there remains a significant gap in image quality and prompt-following ability compared to 2D diffusion models. A critical bottleneck is the scarcity of high-quality 3D data with detailed captions. To address this challenge, we propose Bootstrap3D, a novel framework that automatically generates an arbitrary quantity of multi-view images to assist in training multi-view diffusion models. Specifically, we introduce a data generation pipeline that employs (1) 2D and video diffusion models to generate multi-view images based on constructed text prompts, and (2) our fine-tuned 3D-aware MV-LLaVA for filtering high-quality data and rewriting inaccurate captions. Leveraging this pipeline, we have generated 1 million high-quality synthetic multi-view images with dense descriptive captions to address the shortage of high-quality 3D data. Furthermore, we present a Training Timestep Reschedule (TTR) strategy that leverages the denoising process to learn multi-view consistency while maintaining the original 2D diffusion prior. Extensive experiments demonstrate that Bootstrap3D can generate high-quality multi-view images with superior aesthetic quality, image-text alignment, and maintained view consistency.

## item_id: m_2940

TITLE: RotoGrad: Gradient Homogenization in Multitask Learning

ABSTRACT: Multitask learning is being increasingly adopted in applications domains like computer vision and reinforcement learning. However, optimally exploiting its advantages remains a major challenge due to the effect of negative transfer. Previous works have tracked down this issue to the disparities in gradient magnitudes and directions across tasks, when optimizing the shared network parameters. While recent work has acknowledged that negative transfer is a two-fold problem, existing approaches fall short as they only focus on either homogenizing the gradient magnitude across tasks; or greedily change the gradient directions, overlooking future conflicts. In this work, we introduce RotoGrad, an algorithm that tackles negative transfer as a whole: it jointly homogenizes gradient magnitudes and directions, while ensuring training convergence. We show that RotoGrad outperforms competing methods in complex problems, including multi-label classification in CelebA and computer vision tasks in the NYUv2 dataset. A Pytorch implementation can be found in https://github.com/adrianjav/rotograd.

## item_id: m_2941

TITLE: Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models

ABSTRACT: Reinforcement learning (RL) finetuning has become a key technique for enhancing the reasoning abilities of large language models (LLMs). However, its effectiveness critically depends on the selection of training data. Recent advances underscore the importance of online prompt selection methods, which typically concentrate training on partially solved or moderately challenging examples under the current policy, thereby yielding more effective model updates. While significantly accelerating RL finetuning in terms of training steps, they also incur substantial computational overhead by requiring extensive LLM rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To address this challenge, this work proposes Dynamics-Predictive Sampling (DPS), which online predicts and selects informative prompts by inferring their learning dynamics prior to costly rollouts. Specifically, we introduce a new perspective by modeling each prompt's solving progress during RL finetuning as a dynamical system, where the extent of solving is represented as the state and the transition is characterized by a hidden Markov model. Using historical rollout reward signals, we perform online Bayesian inference to estimate evolving state distributions, and the inference outcome provides a predictive prior for efficient prompt selection without rollout-intensive filtering. Empirical results across diverse reasoning tasks, including mathematics, planning, and visual geometry, demonstrate that DPS substantially reduces redundant rollouts, accelerates the training process, and achieves superior reasoning performance.

## item_id: m_2942

TITLE: Recurrent Normalization Propagation

ABSTRACT: We propose a LSTM parametrization  that preserves the means and variances of the hidden states and memory cells across time. While having training benefits similar to Recurrent Batch Normalization and Layer Normalization, it does not need to estimate statistics at each time step,  therefore, requiring fewer computations overall. We also investigate the parametrization impact on the gradient flows and  present a way of initializing the weights accordingly.

We evaluate our proposal on language modelling and image generative modelling tasks. We empirically show that it performs similarly or better than other recurrent normalization approaches, while being faster to execute.

## item_id: m_2943

TITLE: Rationality of Thought Improves Reasoning in Large Language Models

ABSTRACT: While the capabilities of large language models (LLMs) have been progressively advanced, their competence in addressing intricate reasoning tasks remains inadequate, primarily due to their insufficient cognitive capabilities. To explore the cognitive proficiency of models like GPT-4, we turn to methodologies from cognitive psychology: cognitive abilities reflect rational thinking skills, and cognitive bias tasks are often used to assess rational thinking levels. In this paper, we develop a cognitive bias dataset to measure the rational thinking and cognitive levels of LLMs. Our observations indicate that GPT-4, akin to humans, exhibits limitations in its rational thinking ability. We propose a new method, “Rationality of Thought” (RoT), to prompt LLMs into a rational thinking process during task execution. This method significantly improves the accuracy of GPT-4 on the cognitive bias task by 18.7\%. Cognitive capacity is also essential for tackling complex issues, therefore, we implement RoT across various reasoning tasks. Using only a zero-shot setting, RoT outperforms inference enhancement techniques such as CoT using few-shot, such as GSM8K (+0.4), AQUA-RAT (+4.8), ARC-c (+0.7) in multiple arithmetic and common sense reasoning tasks. Our empirical evaluation shows that RoT helps LLMs elevate their cognitive capabilities through rational thinking, thereby becoming more adept at navigating complex reasoning tasks.

## item_id: m_2944

TITLE: Testing the Limits of Jailbreaking with the Purple Problem

ABSTRACT: The rise of ''jailbreak'' attacks on language models has led to a flurry of defenses aimed at preventing undesirable responses. Nonetheless, most benchmarks remain to be solved, not to mention real-world safety problems. We critically examine the two stages of the defense pipeline: (i) defining what constitutes unsafe outputs, and (ii) enforcing the definition via methods such as fine-tuning or input preprocessing. To understand whether we fail because of definition or enforcement, we consider a simple and well-specified definition of unsafe outputs---outputs that contain the word ''purple''. Surprisingly, all existing fine-tuning and input defenses fail to enforce this definition under adaptive attacks and increasing compute, casting doubt on whether enforcement algorithms can be robust for more complicated definitions. We hope that this definition serves as a testbed to evaluate enforcement algorithms and prevent a false sense of security.

## item_id: m_2945

TITLE: Projective Subspace Networks For Few-Shot Learning

ABSTRACT: Generalization from limited examples, usually studied under the umbrella of meta-learning, equips learning techniques with the ability to adapt quickly in dynamical environments and proves to be an essential aspect of lifelong learning. In this paper, we introduce the Projective Subspace Networks (PSN), a deep learning paradigm that learns non-linear embeddings from limited supervision. In contrast to previous studies, the embedding in PSN deems samples of a given class to form an affine subspace. We will show that such modeling leads to robust solutions, yielding competitive results on supervised and semi-supervised few-shot classification. Moreover, our PSN approach has the ability of end-to-end learning. In contrast to previous works, our projective subspace can be thought of as a richer representation capturing higher-order information datapoints for modeling new concepts.

## item_id: m_2946

TITLE: DOM-Q-NET:  Grounded RL on Structured Language

ABSTRACT: Building agents to interact with the web would allow for significant improvements in knowledge understanding and representation learning. However, web navigation tasks are difficult for current deep reinforcement learning (RL) models due to the large discrete action space and the varying number of actions between the states. In this work, we introduce DOM-Q-NET, a novel architecture for RL-based web navigation to address both of these problems. It parametrizes Q functions with separate networks for different action categories: clicking a DOM element and typing a string input.  Our model utilizes a graph neural network to represent the tree-structured HTML of a standard web page.  We demonstrate the capabilities of our model on the MiniWoB environment where we can match or outperform existing work without the use of expert demonstrations. Furthermore, we show 2x improvements in sample efficiency when training in the multi-task setting, allowing our model to transfer learned behaviours across tasks. 

## item_id: m_2947

TITLE: Continual Pre-training of Language Models

ABSTRACT: Language models (LMs) have been instrumental for the rapid advance of natural language processing. This paper studies continual pre-training of LMs, in particular, continual domain-adaptive pre-training (or continual DAP-training). Existing research has shown that further pre-training an LM using a domain corpus to adapt the LM to the domain can improve the end-task performance in the domain. This paper proposes a novel method to continually DAP-train an LM with a sequence of unlabeled domain corpora to adapt the LM to these domains to improve their end-task performances. The key novelty of our method is a soft-masking mechanism that directly controls the update to the LM. A novel proxy is also proposed to preserve the general knowledge in the original LM. Additionally, it contrasts the representations of the previously learned domain knowledge (including the general knowledge in the pre-trained LM) and the knowledge from the current full network to achieve knowledge integration. The method not only overcomes catastrophic forgetting, but also achieves knowledge transfer to improve end-task performances. Empirical evaluation demonstrates the effectiveness of the proposed method.

## item_id: m_2948

TITLE: Overfitting Detection of Deep Neural Networks without a Hold Out Set

ABSTRACT: Overfitting is an ubiquitous problem in neural network training and usually mitigated using a holdout data set.
Here we challenge this rationale and investigate criteria for overfitting without using a holdout data set.
Specifically, we train a model for a fixed number of epochs multiple times with varying fractions of randomized labels and for a range of regularization strengths. 
A properly trained model should not be able to attain an accuracy greater than the fraction of properly labeled data points. Otherwise the model overfits. 
We introduce two criteria for detecting overfitting and one to detect underfitting. We analyze early stopping, the regularization factor, and network depth.
In safety critical applications we are interested in models and parameter settings which perform well and are not likely to overfit. The methods of this paper allow characterizing and identifying such models.

## item_id: m_2949

TITLE: StyleMorph: Disentangled 3D-Aware Image Synthesis with a 3D Morphable StyleGAN

ABSTRACT: We introduce StyleMorph, a 3D-aware generative model that disentangles 3D shape, camera pose, object appearance, and background appearance for high quality image synthesis. We account for shape variability by morphing a canonical 3D object template, effectively learning a 3D morphable model in an entirely unsupervised manner through backprop. We chain 3D morphable modelling with deferred neural rendering by performing an implicit surface rendering of “Template Object Coordinates” (TOCS), which can be understood as an unsupervised counterpart to UV maps. This provides a detailed 2D TOCS map signal that reflects the compounded geometric effects of non-rigid shape variation, camera pose, and perspective projection. We combine 2D TOCS maps with an independent appearance code to condition a StyleGAN-based deferred neural rendering (DNR) network for foreground image (object) synthesis; we use a separate code for background synthesis and do late fusion to deliver the final result. We show competitive synthesis results on 4 datasets (FFHQ faces, AFHQ Cats, Dogs, Wild), while achieving the joint disentanglement of shape, pose, object and background texture.

## item_id: m_2950

TITLE: Art-Free Generative Models: Exploring Art Creation Without Prior Artistic Knowledge

ABSTRACT: In this work, we explore the question: “How much prior art knowledge is needed to create art?” To investigate this, we propose a text-to-image generation model trained without access to art-related content. We then introduce a simple yet effective method to learn an art adaptor using only a few examples of selected artistic styles. Our experiments show that art generated using our method is perceived by users as comparable to art produced by models trained on large, art-rich datasets. Finally, through data attribution techniques, we illustrate how examples from both artistic and non-artistic datasets contributed to the creation of new artistic styles.

## item_id: m_2951

TITLE: E3D-Bench: A Benchmark for End-to-End 3D Geometric Foundation Models

ABSTRACT: Spatial intelligence, encompassing 3D reconstruction, perception, and reasoning, is fundamental to applications such as robotics, aerial imaging, and extended reality. A key enabler is the real‑time, accurate estimation of core 3D attributes (camera parameters, point clouds, depth maps, and 3D point tracks) from unstructured or streaming imagery. Inspired by the success of large foundation models in language and 2D vision, a new class of end‑to‑end 3D geometric foundation models (GFMs) has emerged, directly predicting dense 3D representations in a single feed‑forward pass, eliminating the need for slow or unavailable precomputed camera parameters.

Since late 2023, the field has exploded with diverse variants, but systematic evaluation is lacking. In this work, we present the first comprehensive benchmark for 3D GFMs, covering five core tasks: sparse‑view depth estimation, video depth estimation, 3D reconstruction, multi‑view pose estimation, novel view synthesis, and spanning both standard and challenging out‑of‑distribution datasets. Our standardized toolkit automates dataset handling, evaluation protocols, and metric computation to ensure fair, reproducible comparisons. We evaluate 17 state‑of‑the‑art GFMs, revealing their strengths and limitations across tasks and domains, and derive key insights to guide future model scaling and optimization. All code, evaluation scripts, and processed data will be publicly released to accelerate research in 3D spatial AI.

## item_id: m_2952

TITLE: Universal Graph Neural Networks without Message Passing

ABSTRACT: Message-Passing Graph Neural Networks (MP-GNNs) have become the de facto paradigm for learning on graph for years. Nevertheless, recent works also obtain promising empirical results with other kinds of architectures like global self-attention and even MLPs. This raises an important theoretical question: what is the minimal prerequisite for an expressive graph model? In this work, we theoretically show that when equipped with proper position encodings, even a simple Bag-of-Nodes (BoN) model (node-wise MLP followed by global readout) can be universal on graphs. We name this model as Universal Bag-of-Nodes (UBoN). Synthetic experiments on the EXP dataset show that UBoN indeed achieves expressive power beyond 1-WL test. On real-world graph classification tasks, UBoN also obtains comparable performance to MP-GNNs while enjoying better training and inference efficiency (50% less training time compared to GCN). We believe that our theoretical and empirical results might inspire more research on simple and expressive GNN architectures.


## item_id: m_2953

TITLE: Empirical Bayes Transductive Meta-Learning with Synthetic Gradients

ABSTRACT: We propose a meta-learning approach that learns from multiple tasks in a transductive setting, by leveraging the unlabeled query set in addition to the  support set to generate a more powerful model for each task. To develop our framework, we revisit the empirical Bayes formulation for multi-task learning.   The evidence lower bound of the marginal log-likelihood of empirical Bayes decomposes as a sum of local KL divergences between the variational posterior and the true posterior on the query set of each task.
We derive a novel amortized variational inference that couples all the variational posteriors via a meta-model, which consists of a synthetic gradient   network and an initialization network. Each variational posterior is derived from synthetic gradient descent to approximate the true posterior on the query  set, although where we do not have access to the true gradient.
Our results on the Mini-ImageNet and CIFAR-FS benchmarks for episodic few-shot classification outperform previous state-of-the-art methods. Besides, we conduct two zero-shot learning experiments to further explore the potential of the synthetic gradient.

## item_id: m_2954

TITLE: What Would pi* Do?: Imitation Learning via Off-Policy Reinforcement Learning

ABSTRACT: Learning to imitate expert actions given demonstrations containing image observations is a difficult problem in robotic control. The key challenge is generalizing behavior to out-of-distribution states that differ from those in the demonstrations. State-of-the-art imitation learning algorithms perform well in environments with low-dimensional observations, but typically involve adversarial optimization procedures, which can be difficult to use with high-dimensional image observations. We propose a remarkably simple alternative based on off-policy soft Q-learning, which we call soft Q imitation learning (SQIL, pronounced "skill"), that rewards the agent for matching demonstrated actions in demonstrated states. The key idea is initially filling the agent's experience replay buffer with demonstrations, where rewards are set to a positive constant, and setting rewards to zero in all additional experiences. We derive SQIL from first principles as a method for performing approximate inference under the MaxCausalEnt model of expert behavior. The approximate inference objective trades off between a pure behavioral cloning loss and a regularization term that incorporates information about state transitions via the soft Bellman error. Our experiments show that SQIL matches the state of the art in low-dimensional environments, and significantly outperforms prior work in playing video games from high-dimensional images.

## item_id: m_2955

TITLE: Mitigating Spurious Correlations in Zero-Shot Multimodal Models

ABSTRACT: Multimodal models or Vision Language Models (VLMs) have reshaped the paradigm in machine learning, offering zero-shot capabilities that require no additional training when adapted to new classification tasks. However, despite their advancements, spurious correlations still exist in VLMs. Existing approaches to tackle this issue often require target label annotations, contradicting the principle of zero-shot classification, or they primarily focus on a single modality, risking misalignment between text and image modalities. Others rely on extensive domain knowledge or large language models (LLMs) to characterize spurious features, making the performance sensitive to the generated prompts and undermining zero-shot capability. In response, we propose a new solution that tackles spurious correlations in VLMs within the zero-shot setting. Our approach utilizes a translation operation that preserves the latent space distribution to address issues of spurious correlations. In particular, our method is grounded in and inspired by a theoretical analysis, which identifies that the optimal translation directions are along the spurious vector. As VLMs unify two modalities, we compute spurious vectors from the text prompts and guide the translation for image embeddings, aligning the requirements for the fusion of different modalities in VLMs. We conducted experiments on benchmark datasets, which have shown significant improvements in worst-group accuracy. Additionally, our visualizations of VLMs further demonstrate the effectiveness of this intervention.

## item_id: m_2956

TITLE: Lossless Compression of Structured Convolutional Models via Lifting

ABSTRACT: Lifting is an efficient technique to scale up graphical models generalized to relational domains by exploiting the underlying symmetries. Concurrently, neural models are continuously expanding from grid-like tensor data into structured representations, such as various attributed graphs and relational databases. To address the irregular structure of the data, the models typically extrapolate on the idea of convolution, effectively introducing parameter sharing in their, dynamically unfolded, computation graphs. The computation graphs themselves then reflect the symmetries of the underlying data, similarly to the lifted graphical models. Inspired by lifting, we introduce a simple and efficient technique to detect the symmetries and compress the neural models without loss of any information. We demonstrate through experiments that such compression can lead to significant speedups of structured convolutional models, such as various Graph Neural Networks, across various tasks, such as molecule classification and knowledge-base completion.

## item_id: m_2957

TITLE: Towards the Decisive Factor of Symbolic Generalization of DNNs

ABSTRACT: The decisive factor that drives deep neural networks (DNNs) to learn non-generalizable representations (*i.e.,* non-generalizable interactions between input variables) has been a persistent challenge in the field of symbolic generalization. In this paper, we quantify the generalization power of such interactions encoded by DNNs, and we discover that DNNs usually learn non-generalizable interactions from a few samples, referred to as *confusing samples*. The emergence of confusing samples during the training process explains the overfitting of a DNN. We further discover that the composition of confusing samples is determined by the randomness of parameter initialization in the low layers of a DNN. In contrast, other factors, such as high-layer parameters and network architecture, have much less impact on the composition of confusing samples. Consequently, two DNNs initialized with different low-layer parameters will eventually learn entirely different sets of confusing samples, even though they have similar performance.

## item_id: m_2958

TITLE: ScoreFlow: Bridging Score and Neural ODE for Reversible Generative Modeling

ABSTRACT: Neural ordinary differential equations (ODEs) are commonly used in reversible generative models. However, training neural ODEs is computationally expensive for estimating the log-likelihood density and backpropagating through ODE solvers, leading to slow convergence and significant gradient estimation errors. This paper presents ScoreFlow, a novel generative model capable of reversible and controllable data transformations. Firstly, we formulate an ODE utilizing a score variant as the drift term to model transformations between two certain data distributions. Secondly, we suggest a path-constrained loss to reduce truncation errors, enhancing the model's capabilities in generating high-quality samples. Thirdly, ScoreFlow has the ability to employ a single model to achieve both conditional image generation and cross-class image translation tasks. The closed-form optimal solution for data transformation in ScoreFlow is theoretically proven, providing support for the model's efficient training. Furthermore, the effectiveness of our approach is empirically validated through image generation, translation, and interpolation experiments.

## item_id: m_2959

TITLE: Beyond Pruning: Neuro-inspired Sparse Training For Enhancing Model Performance, Convergence Speed, and Training Stability

ABSTRACT: Pruning often trades accuracy for efficiency, and sparse training is hard to do from scratch without performance loss. We introduce a simple, neuro-inspired sparse training (NIST) algorithm that simultaneously sparsifies, stabilizes, and strengthens neural networks without introducing computational overhead or complex optimizers. Our method achieves high sparsity while surprisingly enhancing model performance, accelerating convergence, and improving training stability across diverse architectures, and plugs directly into standard training pipelines. Empirically, it strengthens MLP-heavy architectures (e.g., VGG, AlexNet) by aggressively sparsifying them ($>$90\%) and counterintuitively, 8-10\% improving test accuracy. Additionally, NIST accelerates convergence and reduces variance in efficient CNNs such as MobileNet. It also enables transformer training directly from 50\% initial sparsity and up to 70\% final sparsity with negligible performance loss, while speeding up model convergence in the first 30 epochs. Our comprehensive experiments, ablations, and comparisons against state-of-the-art pruning and sparse-training methods reveal that these gains stem not from reduced parameter counts alone, but from improved optimization dynamics and more effective parameter reallocation. This study reframes sparse training as a performance-enhancing tool rather than a compromise.

## item_id: m_2960

TITLE: MILE: A Multi-Level Framework for Scalable Graph Embedding

ABSTRACT: Recently there has been a surge of interest in designing graph embedding methods. Few, if any, can scale to a large-sized graph with millions of nodes due to both computational complexity and memory requirements. In this paper, we relax this limitation by introducing the MultI-Level Embedding (MILE) framework – a generic methodology allowing contemporary graph embedding methods to scale to large graphs. MILE repeatedly coarsens the graph into smaller ones using a hybrid matching technique to maintain the backbone structure of the graph. It then applies existing embedding methods on the coarsest graph and refines the embeddings to the original graph through a novel graph convolution neural network that it learns. The proposed MILE framework is agnostic to the underlying graph embedding techniques and can be applied to many existing graph embedding methods without modifying them. We employ our framework on several popular graph embedding techniques and conduct embedding for real-world graphs. Experimental results on five large-scale datasets demonstrate that MILE significantly boosts the speed (order of magnitude) of graph embedding while also often generating embeddings of better quality for the task of node classification. MILE can comfortably scale to a graph with 9 million nodes and 40 million edges, on which existing methods run out of memory or take too long to compute on a modern workstation.

## item_id: m_2961

TITLE: The Benefits of Over-parameterization at Initialization in Deep ReLU Networks

ABSTRACT: It has been noted in existing literature that over-parameterization in ReLU networks generally improves performance. While there could be several factors involved behind this, we prove some desirable theoretical properties at initialization which may be enjoyed by ReLU networks. Specifically, it is known that He initialization in deep ReLU networks asymptotically preserves variance of activations in the forward pass and variance of gradients in the backward pass for infinitely wide networks, thus preserving the flow of information in both directions. Our paper goes beyond these results and shows novel properties that hold under He initialization: i) the norm of hidden activation of each layer is equal to the norm of the input, and, ii) the norm of weight gradient of each layer is equal to the product of norm of the input vector and the error at output layer. These results are derived using the PAC analysis framework, and hold true for finitely sized datasets such that the width of the ReLU network only needs to be larger than a certain finite lower bound. As we show, this lower bound depends on the depth of the network and the number of samples, and by the virtue of being a lower bound, over-parameterized ReLU networks are endowed with these desirable properties. For the aforementioned hidden activation norm property under He initialization, we further extend our theory and show that this property holds for a finite width network even when the number of data samples is infinite. Thus we overcome several limitations of existing papers, and show new properties of deep ReLU networks at initialization.

## item_id: m_2962

TITLE: Scalable Neural Methods for Reasoning With a Symbolic Knowledge   Base

ABSTRACT: We describe a novel way of representing a symbolic knowledge base (KB) called a sparse-matrix reified KB.  This representation enables neural modules that are fully differentiable, faithful to the original semantics of the KB, expressive enough to model multi-hop inferences, and scalable enough to use with realistically large KBs. The sparse-matrix reified KB can be distributed across multiple GPUs, can scale to tens of millions of entities and facts, and is orders of magnitude faster than naive sparse-matrix implementations.  The reified KB enables very simple end-to-end architectures to obtain competitive performance on several benchmarks representing two families of tasks: KB completion, and learning semantic parsers from denotations.

## item_id: m_2963

TITLE: kaBEDONN: posthoc eXplainable Artificial Intelligence with Data Ordered Neural Network

ABSTRACT: Different approaches to eXplainable Artificial Intelligence (XAI) have been explored including (1) the systematic study of the effect of individual training data sample on the final model (2) posthoc attribution methods that assign importance values to the components of each data sample. Combining concepts from both approaches, we introduce kaBEDONN, a system of ordered dataset coupled with a posthoc and model-agnostic method for querying \textit{relevant} training data samples. These \textit{relevant} data are intended as the explanations for model predictions that are both user-friendly and easily adjustable by developers. Explanations can thus be finetuned and damage control can be performed with ease.

## item_id: m_2964

TITLE: Continual Backprop: Stochastic Gradient Descent with Persistent Randomness

ABSTRACT: The Backprop algorithm for learning in neural networks utilizes two mechanisms: first, stochastic gradient descent and second, initialization with small random weights, where the latter is essential to the effectiveness of the former. We show that in continual learning setups, Backprop performs well initially, but over time its performance degrades. Stochastic gradient descent alone is insufficient to learn continually; the initial randomness enables only initial learning but not continual learning. To the best of our knowledge, ours is the first result showing this degradation in Backprop’s ability to learn. To address this issue, we propose an algorithm that continually injects random features alongside gradient descent using a new generate-and-test process. We call this the Continual Backprop algorithm. We show that, unlike Backprop, Continual Backprop is able to continually adapt in both supervised and reinforcement learning problems. We expect that as continual learning becomes more common in future applications, a method like Continual Backprop will be essential where the advantages of random initialization are present throughout learning.

## item_id: m_2965

TITLE: Learning with Random Learning Rates.

ABSTRACT: Hyperparameter tuning is a bothersome step in the training of deep learning mod- els. One of the most sensitive hyperparameters is the learning rate of the gradient descent. We present the All Learning Rates At Once (Alrao) optimization method for neural networks: each unit or feature in the network gets its own learning rate sampled from a random distribution spanning several orders of magnitude. This comes at practically no computational cost. Perhaps surprisingly, stochastic gra- dient descent (SGD) with Alrao performs close to SGD with an optimally tuned learning rate, for various architectures and problems. Alrao could save time when testing deep learning models: a range of models could be quickly assessed with Alrao, and the most promising models could then be trained more extensively. This text comes with a PyTorch implementation of the method, which can be plugged on an existing PyTorch model.

## item_id: m_2966

TITLE: Towards Robust Domain Generalization in 2D Neural Audio Processing

ABSTRACT: While using two-dimensional convolutional neural networks (2D-CNNs) in image processing, it is possible to manipulate domain information using channel statistics, and instance normalization has been a promising way to get domain-invariant features. Although 2D image features represent spatial information, 2D audio features like log-Mel spectrogram represent two different temporal and spectral information. Unlike image processing, we analyze that domain-relevant information in the audio feature is dominant in frequency statistics rather than channel statistics. Motivated by our analysis, we introduce RFN, a plug-and-play, explicit normalization module along the frequency axis, eliminating instance-specific domain discrepancy in the audio feature while relaxing undesirable loss of useful discriminative information. Empirically, simply adding RFN to networks shows clear margins compared to previous domain generalization approaches on acoustic scene classification, keyword spotting, and speaker verification tasks and yields improved robustness to audio-device, speaker-ID, or genre.

## item_id: m_2967

TITLE: Self-Supervision is All You Need for Solving Rubik's Cube

ABSTRACT: While combinatorial problems are of great academic and practical importance, previous approaches like explicit heuristics and reinforcement learning have been complex and costly. To address this, we developed a simple and robust method to train a Deep Neural Network (DNN) through self-supervised learning for solving a goal-predefined combinatorial problem. Assuming that more optimal moves occur more frequently as a path of random moves connecting two problem states, the DNN can approximate an optimal solver by learning to predict the last move of a random scramble based on the problem state. Tested on 1,000 scrambled Rubik's Cube instances, a Transformer-based model could solve all of them near-optimally using a breadth-first search;  with a maximum breadth of $10^3$, the mean solution length was $20.5$ moves. The proposed method may apply to other goal-predefined combinatorial problems, though it has a few constraints.

## item_id: m_2968

TITLE: Composing Human Object Interaction with Decoupled Prototype for Zero-shot Learning

ABSTRACT: Zero-shot Human-Object Interaction (HOI) detection is a daunting problem, largely stemming from the combinatorial explosion of potential action-object pairs. 
Current studies predominantly address this issue by transferring knowledge from large-scale pre-trained models (e.g., CLIP), yet ignore a more straightforward idea, i.e., mimic the powerful compositional generalization ability of human intelligence based on past cases. 
Besides, they simplify this combinatorial challenge by operating under the assumption that knowledge about unseen compositions is accessible, which is usually impractical in reality.
In this work, we extend prior Closed-World zero-shot setting to an Open-World scenario, where the search space for HOI compositions is entirely unrestricted.
For this challenging task, we introduce ProtoHOI, a fresh prototype-based framework for zero-shot HOI detection, which consists of: 
i) distill a set of prototypes from HOI proposal embeddings to model the inherent properties of objects and actions in the context of HOI.
ii) recalibrate the representation space learned by the HOI detector based on these derived prototypes in a decoupled manner, thereby facilitating the prediction of unseen HOI compositions. 
Extensive experiments on two standard benchmarks demonstrate the superiority of ProtoHOI over the state-of-the-art methods across all zero-shot settings. The source code will be released.

## item_id: m_2969

TITLE: CuPID: Leveraging Masked Single-Lead ECG Modelling for Enhancing the Representations

ABSTRACT: Wearable sensing devices, such as electrocardiogram (ECG) heart-rate monitors, will play a crucial role in the future of digital health. This constant monitoring leads to massive unlabeled datasets, making the development of unsupervised learning frameworks essential to associate these single-lead ECG signals with their anticipated clinical outcomes. While Masked Data Modelling (MDM) methods have enjoyed wide use, the idiosyncrasies of single-lead ECG data make its direct application impractical. In this paper, we present Cueing the Predictor Increments the Detailing (CuPID), a novel Self-Supervised Learning (SSL) method that adapts MDM methods for use on single-lead ECG signal data. CuPID accomplishes this via cueing spectrogram-derived context to the predictors, thus incentivizing the encoder to produce more detailed representations. This leads the class token to accommodate fine-grained information. We demonstrate that CuPID outperforms state-of-the-art methods in a variety of downstream tasks and databases, increasing the accuracy for each task from 3.6 % to 9.7%.

## item_id: m_2970

TITLE: Uniform Manifold Approximation with Two-phase Optimization

ABSTRACT: We present a dimensionality reduction algorithm called Uniform Manifold Approximation with Two-phase Optimization (UMATO) which produces less biased global structures in the embedding results and is robust over diverse initialization methods than previous methods such as $t$-SNE and UMAP. We divide the optimization into two phases to alleviate the bias by establishing the global structure early using the representatives of the high-dimensional structures. The phases are 1) global optimization to obtain the overall skeleton of data and 2) local optimization to identify the regional characteristics of local areas. In our experiments with one synthetic and three real-world datasets, UMATO outperformed widely-used baseline algorithms, such as PCA, red, $t$-SNE, UMAP, topological autoencoders and Anchor $t$-SNE, in terms of quality metrics and 2D projection results.

## item_id: m_2971

TITLE: The Gambler's Problem and Beyond

ABSTRACT: We analyze the Gambler's problem, a simple reinforcement learning problem where the gambler has the chance to double or lose their bets until the target is reached. This is an early example introduced in the reinforcement learning textbook by Sutton and Barto (2018), where they mention an interesting pattern of the optimal value function with high-frequency components and repeating non-smooth points. It is however without further investigation. We provide the exact formula for the optimal value function for both the discrete and the continuous cases. Though simple as it might seem, the value function is pathological: fractal, self-similar, derivative taking either zero or infinity, not smooth on any interval, and not written as elementary functions. It is in fact one of the generalized Cantor functions, where it holds a complexity that has been uncharted thus far. Our analyses could lead insights into improving value function approximation, gradient-based algorithms, and Q-learning, in real applications and implementations.

## item_id: m_2972

TITLE: Multi-Modal Point Cloud Completion with Intra- and Inter-Graph Transformer

ABSTRACT: Multi-modal point cloud completion aims to leverage complementary image information to assist point cloud completion. Existing multi-modal approaches predominantly employ Transformers to facilitate interactions between different modalities. However, fully-connected attention-based Transformers lead to high computational cost and redundancy, and often fail to fully capture the complex relations between these modalities. To address these issues, we propose the Intra- and Inter-Graph Transformer (I$^{2}$GraphFormer), which leverages sparse graph connections to restrict attention to neighboring nodes both within and across modalities. I$^{2}$GraphFormer enhances interactions in terms of efficiency and expressiveness. Specifically, we model relations from both intra-graph and inter-graph perspectives, obtaining more expressive representations and producing higher-quality completion results. Extensive quantitative and qualitative experiments demonstrate that I$^{2}$GraphFormer outperforms state-of-the-art multi-modal approaches across various evaluation scenarios with low complexity.

## item_id: m_2973

TITLE: Connectome-constrained Latent Variable Model of Whole-Brain Neural Activity

ABSTRACT: The availability of both anatomical connectivity and brain-wide neural activity measurements in C. elegans make the worm a promising system for learning detailed, mechanistic models of an entire nervous system in a data-driven way. However, one faces several challenges when constructing such a model. We often do not have direct experimental access to important modeling details such as single-neuron dynamics and the signs and strengths of the synaptic connectivity. Further, neural activity can only be measured in a subset of neurons, often indirectly via calcium imaging, and significant trial-to-trial variability has been observed. To address these challenges, we introduce a connectome-constrained latent variable model (CC-LVM) of the unobserved voltage dynamics of the entire C. elegans nervous system and the observed calcium signals. We used the framework of variational autoencoders to fit parameters of the mechanistic simulation constituting the generative model of the LVM to calcium imaging observations. A variational approximate posterior distribution over latent voltage traces for all neurons is efficiently inferred using an inference network, and constrained by a prior distribution given by the biophysical simulation of neural dynamics. We applied this model to an experimental whole-brain dataset, and found that connectomic constraints enable our LVM to predict the activity of neurons whose activity were withheld significantly better than models unconstrained by a connectome. We explored models with different degrees of biophysical detail, and found that models with realistic conductance-based synapses provide markedly better predictions than current-based synapses for this system.

## item_id: m_2974

TITLE: Oracle Efficient Algorithms for Groupwise Regret

ABSTRACT: We study the problem of online prediction, in which at each time step $t \in \{1,2, \cdots T\}$, an individual $x_t$ arrives, whose label we must predict. Each individual is associated with various groups, defined based on their features such as age, sex, race etc., which may intersect. Our goal is to make predictions that have regret guarantees not just overall but also simultaneously on each sub-sequence comprised of the members of any single group. Previous work such as  [Blum & Lykouris][1] and [Lee et al][2] provide attractive regret guarantees for these problems; however, these are computationally intractable on large model classes (e.g., the set of all linear models, as used in linear regression). We show that a simple modification of the sleeping experts technique of [Blum & Lykouris][1] yields an efficient *reduction* to the well-understood problem of obtaining diminishing external regret *absent group considerations*. 
Our approach gives similar regret guarantees compared to [Blum & Lykouris][1]; however, we run in time linear in the number of groups, and are oracle-efficient in the hypothesis class. This in particular implies that our algorithm is efficient whenever the number of groups is  polynomially bounded and the external-regret problem can be solved efficiently, an improvement on [Blum & Lykouris][1]'s stronger condition that the model class must be small. Our approach can handle online linear regression and online combinatorial optimization problems like online shortest paths. Beyond providing theoretical regret bounds, we evaluate this algorithm with an extensive set of experiments on synthetic data and on two real data sets --- Medical costs and the Adult income dataset, both instantiated with intersecting groups defined in terms of race, sex, and other demographic characteristics. 
We find that uniformly across groups, our algorithm gives substantial error improvements compared to running a standard online linear regression algorithm with no groupwise regret guarantees.

## item_id: m_2975

TITLE: SemiFL: Communication Efficient Semi-Supervised Federated Learning with Unlabeled Clients

ABSTRACT: Federated Learning allows training machine learning models by using the computation and private data resources of many distributed clients such as smartphones and IoT devices. Most existing works on Federated Learning (FL) assume the clients have ground-truth labels. However, in many practical scenarios, clients may be unable to label task-specific data, e.g., due to a lack of expertise. This work considers a server that hosts a labeled dataset and wishes to leverage clients with unlabeled data for supervised learning. We propose a new Federated Learning framework referred to as SemiFL to address Semi-Supervised Federated Learning (SSFL). In SemiFL, clients have completely unlabeled data, while the server has a small amount of labeled data. SemiFL is communication efficient since it separates the training of server-side supervised data and client-side unsupervised data. We demonstrate several strategies of SemiFL that enhance efficiency and prediction and develop intuitions of why they work. In particular, we provide a theoretical understanding of the use of strong data augmentation for Semi-Supervised Learning (SSL), which can be interesting in its own right.
Extensive empirical evaluations demonstrate that our communication efficient method can significantly improve the performance of a labeled server with unlabeled clients. Moreover, we demonstrate that SemiFL can outperform many existing FL results trained with fully supervised data, and perform competitively with the state-of-the-art centralized SSL methods. For instance, in standard communication efficient scenarios, our method can perform $93\%$ accuracy on the CIFAR10 dataset with only $4000$ labeled samples at the server. Such accuracy is only $2\%$ away from the result trained from $50000$ fully labeled data, and it improves about $30\%$ upon existing SSFL methods in the communication efficient setting.

## item_id: m_2976

TITLE: Variable Computation in Recurrent Neural Networks

ABSTRACT: Recurrent neural networks (RNNs) have been used extensively and with increasing success to model various types of sequential data. Much of this progress has been achieved through devising recurrent units and architectures with the flexibility to capture complex statistics in the data, such as long range dependency or localized attention phenomena. However, while many sequential data (such as video, speech or language) can have highly variable information flow, most recurrent models still consume input features at a constant rate and perform a constant number of computations per time step, which can be detrimental to both speed and model capacity. In this paper, we explore a modification to existing recurrent units which allows them to learn to vary the amount of computation they perform at each step, without prior knowledge of the sequence's time structure. We show experimentally that not only do our models require fewer operations, they also lead to better performance overall on evaluation tasks.

## item_id: m_2977

TITLE: The asymptotic spectrum of the Hessian of DNN throughout training

ABSTRACT: The dynamics of DNNs during gradient descent is described by the so-called Neural Tangent Kernel (NTK). In this article, we show that the NTK allows one to gain precise insight into the Hessian of the cost of DNNs: we obtain a full characterization of the asymptotics of the spectrum of the Hessian, at initialization and during training. 

## item_id: m_2978

TITLE: Parallel Federated Learning over Heterogeneous Devices

ABSTRACT: Federated Learning (FL) is a cutting-edge distributed machine learning framework that enables multiple devices to collaboratively train a shared model without exposing their own data. In the scenario of device heterogeneity, the synchronous FL suffers from latency bottleneck induced by network stragglers, which hampers the training efficiency significantly. In addition, due to the diverse structures and sizes of local models, the simple and fast averaging aggregation is not feasible anymore. Instead, complicated aggregation operation, such as knowledge distillation, is required. The time cost for complicated aggregation becomes a new bottleneck that limits the computational efficiency of FL. 
In this work, we claim that the cause root of training latency actually lies in the aggregation-then-broadcasting workflow of the server. By swapping the computational order of aggregation and broadcasting, we propose a new parallel federated learning (PFL) framework, which unlocks the edge nodes during global computation and the central server during local computation. This fully asynchronous and parallel pipeline enables handling device heterogeneity and network stragglers, allowing flexible device participation as well as achieving scalability in computation.
We theoretically prove that PFL can achieve the similar convergence rate as synchronous FL, and empirically show that our framework can tolerate both stragglers and complicated aggregation tasks, which brings $1.77\times$ to $7.32\times$ speedup.

## item_id: m_2979

TITLE: LEAF: A Learnable Frontend for Audio Classification

ABSTRACT: Mel-filterbanks are fixed, engineered audio features which emulate human perception and have been used through the history of audio understanding up to today. However, their undeniable qualities are counterbalanced by the fundamental limitations of handmade representations. In this work we show that we can train a single learnable frontend that outperforms mel-filterbanks on a wide range of audio signals, including speech, music, audio events and animal sounds, providing a general-purpose learned frontend for audio classification. To do so, we introduce a new principled, lightweight, fully learnable architecture that can be used as a drop-in replacement of mel-filterbanks. Our system learns all operations of audio features extraction, from filtering to pooling, compression and normalization, and can be integrated into any neural network at a negligible parameter cost. We perform multi-task training on eight diverse audio classification tasks, and show consistent improvements of our model over mel-filterbanks and previous learnable alternatives. Moreover, our system outperforms the current state-of-the-art learnable frontend on Audioset, with orders of magnitude fewer parameters.

## item_id: m_2980

TITLE: Training-free Long Video Generation with Chain of Diffusion Model Experts

ABSTRACT: Video generation models hold substantial potential in areas such as filmmaking. However, current video diffusion models need high computational costs and produce suboptimal results due to high complexity of video generation task. In this paper, we propose \textbf{ConFiner}, an efficient high-quality video generation framework that decouples video generation into easier subtasks: structure \textbf{con}trol and spatial-temporal re\textbf{fine}ment. It can generate high-quality videos with chain of off-the-shelf diffusion model experts, each expert responsible for a decoupled subtask. During the refinement, we introduce coordinated denoising, which can merge multiple diffusion experts' capabilities into a single sampling. Furthermore, we design ConFiner-Long framework, which can generate long coherent video with three constraint strategies on ConFiner. Experimental results indicate that with only 10\% of the inference cost, our ConFiner surpasses representative models like Lavie and Modelscope across all objective and subjective metrics. And ConFiner-Long can generate high-quality and coherent videos with up to 600 frames.

## item_id: m_2981

TITLE: RandProx: Primal-Dual Optimization Algorithms with Randomized Proximal Updates

ABSTRACT: Proximal splitting algorithms are well suited to solving large-scale nonsmooth optimization problems, in particular those arising in machine learning. We propose a new primal–dual algorithm, in which the dual update is randomized; equivalently, the proximity operator of one of the function in the problem is replaced by a stochastic oracle. For instance, some randomly chosen dual variables, instead of all, are updated at each iteration. Or, the proximity operator of a function is called with some small probability only. A nonsmooth variance-reduction technique is implemented so that the algorithm finds an exact minimizer of the general problem involving smooth and nonsmooth functions, possibly composed with linear operators. We derive linear convergence results in presence of strong convexity; these results are new even in the deterministic case, when our algorithms reverts to the recently proposed Primal–Dual Davis–Yin algorithm. Some randomized algorithms of the literature are also recovered as particular cases (e.g., Point-SAGA). But our randomization technique is general and encompasses many unbiased mechanisms beyond sampling and probabilistic updates, including compression. Since the convergence speed depends on the slowest among the primal and dual contraction mechanisms, the iteration complexity might remain the same when randomness is used. On the other hand, the computation complexity can be significantly reduced. Overall, randomness helps getting faster algorithms. This has long been known for stochastic-gradient-type algorithms, and our work shows that this fully applies in the more general primal–dual setting as well.

## item_id: m_2982

TITLE: CSRv2: Unlocking Ultra-Sparse Embeddings

ABSTRACT: In the era of large foundation models, the quality of embeddings has become a central determinant of downstream task performance and overall system capability. 
Yet widely used dense embeddings are often extremely high-dimensional (e.g., 4096), incurring substantial costs in storage, memory, and inference latency. 
To address these, Contrastive Sparse Representation (CSR) is recently proposed as a promising direction, mapping dense embeddings into high-dimensional but $k$-sparse vectors, in contrast to compact dense embeddings such as Matryoshka Representation Learning (MRL). 
Despite its promise, CSR suffers severe degradation in the ultra-sparse regime (e.g., $k \leq 4$), where over 80\% of neurons remain inactive, leaving much of its efficiency potential unrealized.
In this paper, we introduce CSRv2, a principled training approach designed to make ultra-sparse embeddings viable. 
CSRv2 stabilizes sparsity learning through progressive $k$-annealing, enhances representational quality via supervised contrastive objectives, and ensures end-to-end adaptability with full backbone finetuning. 
CSRv2 reduces dead neurons from 80\% to 20\% and delivers a 14\% accuracy gain at $k=2$, bringing ultra-sparse embeddings on par with CSR at $k=8$ and MRL at 32 dimensions, all with only two active features. 
While maintaining comparable performance, CSRv2 delivers a 7$\times$ speedup over MRL, and yields up to 300$\times$ improvements in compute and memory efficiency relative to dense embeddings in e5-mistral-7b-instruct-based text representation.
Extensive experiments across text (MTEB, multiple state-of-the-art LLM embeddings (Qwen and e5-Mistral-7B), SPLADEv3, GraphRAG) and vision (ImageNet-1k) demonstrate that CSRv2 makes ultra-sparse embeddings practical without compromising performance, where CSRv2 achieves 7\%/4\% improvement over CSR when $k=4$ and further increases this gap to 14\%/6\% when $k=2$ in text/vision representation.
By making extreme sparsity viable, CSRv2 broadens the design space for large-scale, real-time, and edge-deployable AI systems where both embedding quality and efficiency are critical. 
Code is available at https://github.com/Y-Research-SBU/CSRv2.

## item_id: m_2983

TITLE: Charged Point Normalization: An Efficient Solution to the Saddle Point Problem

ABSTRACT: Recently, the problem of local minima in very high dimensional non-convex optimization has been challenged and the problem of saddle points has been introduced. This paper introduces a dynamic type of normalization that forces the system to escape saddle points. Unlike other saddle point escaping algorithms, second order information is not utilized, and the system can be trained with an arbitrary gradient descent learner. The system drastically improves learning in a range of deep neural networks on various data-sets in comparison to non-CPN neural networks.

## item_id: m_2984

TITLE: Conditional Network Embeddings

ABSTRACT: Network Embeddings (NEs) map the nodes of a given network into $d$-dimensional Euclidean space $\mathbb{R}^d$. Ideally, this mapping is such that 'similar' nodes are mapped onto nearby points, such that the NE can be used for purposes such as link prediction (if 'similar' means being 'more likely to be connected') or classification (if 'similar' means 'being more likely to have the same label'). In recent years various methods for NE have been introduced, all following a similar strategy: defining a notion of similarity between nodes (typically some distance measure within the network), a distance measure in the embedding space, and a loss function that penalizes large distances for similar nodes and small distances for dissimilar nodes.

A difficulty faced by existing methods is that certain networks are fundamentally hard to embed due to their structural properties: (approximate) multipartiteness, certain degree distributions, assortativity, etc. To overcome this, we introduce a conceptual innovation to the NE literature and propose to create \emph{Conditional Network Embeddings} (CNEs); embeddings that maximally add information with respect to given structural properties (e.g. node degrees, block densities, etc.). We use a simple Bayesian approach to achieve this, and propose a block stochastic gradient descent algorithm for fitting it efficiently.

We demonstrate that CNEs are superior for link prediction and multi-label classification when compared to state-of-the-art methods, and this without adding significant mathematical or computational complexity. Finally, we illustrate the potential of CNE for network visualization.

## item_id: m_2985

TITLE: Back2Future: Leveraging Backfill Dynamics for Improving Real-time Predictions in Future

ABSTRACT: For real-time forecasting in domains like public health and macroeconomics, data collection is a non-trivial and demanding task. Often after being initially released, it undergoes several revisions later (maybe due to human or technical constraints) - as a result, it may take weeks until the data reaches a stable value. This so-called ‘backfill’ phenomenon and its effect on model performance have been barely addressed in the prior literature. In this paper, we introduce the multi-variate backfill problem using COVID-19 as the motivating example. 
We construct a detailed dataset composed of relevant signals over the past year of the pandemic. 
We then systematically characterize several patterns in backfill dynamics and leverage our observations for formulating a novel problem and neural framework, Back2Future, that aims to refines a given model's predictions in real-time. Our extensive experiments demonstrate that our method refines the performance of the diverse set of top models for COVID-19 forecasting and GDP growth forecasting. Specifically, we show that Back2Future refined top COVID-19 models by 6.65% to 11.24% and yield an 18% improvement over non-trivial baselines. In addition, we show that our model improves model evaluation too; hence policy-makers can better understand the true accuracy of forecasting models in real-time.

## item_id: m_2986

TITLE: Cross-Modal Semantic Anchoring: Unsupervised Consistency Verification for Aerial Imagery and Maps via Multimodal LLMs

ABSTRACT: Up-to-date maps are crucial for urban living, enabling navigation, planning, and decision-making. The increasing accessibility of aerial imagery provides a cost-effective solution for updating map semantics, particularly the representation of buildings, which reflects ongoing urban renewal through construction and demolition. However, aligning heterogeneous modalities—aerial images and maps—remains challenging due to the significant modality gap. While previous works focus on low-level visual feature matching, we argue that these methods ignore the semantic correspondence between the map and aerial imagery. Therefore, we propose U-CSA, an unsupervised cross-modal semantic anchoring framework powered by multimodal large language models (MLLMs). Unlike conventional contrastive pre-training approaches that rely on large paired datasets, U-CSA exploits the world knowledge and cross-modal reasoning capabilities of MLLMs to generate high-level semantic anchors—interpretable descriptions of salient geo-entities and spatial structures. These anchors provide a unified semantic space, guiding dual-branch image encoders to align visual features through anchored contrastive learning. The semantically enriched encoders are then incorporated into an adversarial matching network, where dynamically generated sample pairs enable fine-grained discrimination between matched and unmatched regions. Extensive experiments demonstrate the superiority of U-CSA over other state-of-the-art approaches.

## item_id: m_2987

TITLE: Trojans and Adversarial Examples: A Lethal Combination

ABSTRACT: In this work, we naturally unify adversarial examples and Trojan backdoors into a new stealthy attack, that is activated only when 1) adversarial perturbation is injected into the input examples and 2) a Trojan backdoor is used to poison the training process simultaneously. Different from traditional attacks, we leverage adversarial noise in the input space to move Trojan-infected examples across the model decision boundary, thus making it difficult to be detected. Our attack can fool the user into accidentally trusting the infected model as a robust classifier against adversarial examples. We perform a thorough analysis and conduct an extensive set of experiments on several benchmark datasets to show that our attack can bypass existing defenses with a success rate close to 100%.

## item_id: m_2988

TITLE: On the Difficulties of Video Summarization: Structure and Subjectivity

ABSTRACT: Video summarization, aiming at selecting a representative set of frames from a video in a limited budget, is a challenging problem in computer vision. First, to summarize a video with complex contents, understanding the storytelling structure is essential, but this fundamental step is still largely under-utilized. Also, summarization is in nature subjective, since each annotator may have different views on what the most important part is within a video. To tackle these difficulties, we propose Hierarchical model for video Summarization (HiSum), discovering semantic hierarchy structure of a video by event boundary detection and taking advantage of it for important frame selection. From extensive experiments on two standard benchmarks and three other new datasets specially designed to take part in subjectivity, we demonstrate that our model achieves the state-of-the-art performance.

## item_id: m_2989

TITLE: Self-Imitation Learning via Trajectory-Conditioned Policy for Hard-Exploration Tasks

ABSTRACT: Imitation learning from human-expert demonstrations has been shown to be greatly helpful for challenging reinforcement learning problems with sparse environment rewards. However, it is very difficult to achieve similar success without relying on expert demonstrations. Recent works on self-imitation learning showed that imitating the agent's own past good experience could indirectly drive exploration in some environments, but these methods often lead to sub-optimal and myopic behavior. To address this issue, we argue that exploration in diverse directions by imitating diverse trajectories, instead of focusing on limited good trajectories, is more desirable for the hard-exploration tasks. We propose a new method of learning a trajectory-conditioned policy to imitate diverse trajectories from the agent's own past experiences and show that such self-imitation helps avoid myopic behavior and increases the chance of finding a globally optimal solution for hard-exploration tasks, especially when there are misleading rewards. Our method significantly outperforms existing self-imitation learning and count-based exploration methods on various hard-exploration tasks with local optima. In particular, we report a state-of-the-art score of more than 20,000 points on Montezumas Revenge without using expert demonstrations or resetting to arbitrary states.

## item_id: m_2990

TITLE: Semi-Supervised Generative Modeling for Controllable Speech Synthesis

ABSTRACT: We present a novel generative model that combines state-of-the-art neural text- to-speech (TTS) with semi-supervised probabilistic latent variable models. By providing partial supervision to some of the latent variables, we are able to force them to take on consistent and interpretable purposes, which previously hasn’t been possible with purely unsupervised methods. We demonstrate that our model is able to reliably discover and control important but rarely labelled attributes of speech, such as affect and speaking rate, with as little as 1% (30 minutes) supervision. Even at such low supervision levels we do not observe a degradation of synthesis quality compared to a state-of-the-art baseline. We will release audio samples at https://google.github.io/tacotron/publications/semisupervised_generative_modeling_for_controllable_speech_synthesis/.

## item_id: m_2991

TITLE: Temporal Ensembling for Semi-Supervised Learning

ABSTRACT: In this paper, we present a simple and efficient method for training deep neural networks in a semi-supervised setting where only a small portion of training data is labeled. We introduce self-ensembling, where we form a consensus prediction of the unknown labels using the outputs of the network-in-training on different epochs, and most importantly, under different regularization and input augmentation conditions. This ensemble prediction can be expected to be a better predictor for the unknown labels than the output of the network at the most recent training epoch, and can thus be used as a target for training. Using our method, we set new records for two standard semi-supervised learning benchmarks, reducing the (non-augmented) classification error rate from 18.44% to 7.05% in SVHN with 500 labels and from 18.63% to 16.55% in CIFAR-10 with 4000 labels, and further to 5.12% and 12.16% by enabling the standard augmentations. We additionally obtain a clear improvement in CIFAR-100 classification accuracy by using random images from the Tiny Images dataset as unlabeled extra inputs during training. Finally, we demonstrate good tolerance to incorrect labels.


## item_id: m_2992

TITLE: Playing Atari with Capsule Networks: A systematic comparison of CNN and CapsNets-based agents.

ABSTRACT: In recent years, Capsule Networks (CapsNets) have achieved promising results in tasks in the object recognition task thanks to their invariance characteristics towards pose and lighting.
They have been proposed as an alternative to relational insensitive and translation invariant Convolutional Neural Networks (CNN). 
It has been empirically proven that CapsNets are capable of achieving competitive performance while requiring significantly fewer parameters.
This is a desirable characteristic for Deep reinforcement learning which is known to be sample-inefficient during training.
In this paper, we conduct a systematic analysis to explore the potential of CapsNets-based agents in the deep reinforcement learning setting.
More specifically, we compare the performance of a CNN-based agent with a CapsNets-based agent in a deep Q-network using the Atari suite as the testbed of our analysis. 
To the best of our knowledge, this work constitutes the first CapsNets based deep reinforcement learning model to learn state-action value functions without the need of task-specific adaptation.
Our results show that, in this setting, CapsNets-based architectures require 92% fewer parameters compared to their CNN-based counterparts.
Moreover, despite their smaller size, the CapsNets-based agents provide significant boosts in performance (score), ranging between 10% - 77%.
This is supported by our empirical results which shows that CapsNets-based agents outperform the CNN-based agent, in a Double-DQN with Prioritized experience replay setting, in eight out of the nine selected environments.

## item_id: m_2993

TITLE: Inhibited Softmax for Uncertainty Estimation in Neural Networks

ABSTRACT: We present a new method for uncertainty estimation and out-of-distribution detection in neural networks with softmax output. We extend softmax layer with an additional constant input. The corresponding additional output is able to represent the uncertainty of the network. The proposed method requires neither additional parameters nor multiple forward passes nor input preprocessing nor out-of-distribution datasets. We show that our method performs comparably to more computationally expensive methods and outperforms baselines on our experiments from image recognition and sentiment analysis domains.

## item_id: m_2994

TITLE: Self-Augmented Preference Optimization: Off-Policy Paradigms for Language Model Alignment

ABSTRACT: Traditional language model alignment methods, such as Direct Preference Optimization (DPO), are limited by their dependence on static, pre-collected paired preference data, which restricts their adaptability and practical applicability. To address this limitation, we introduce Self-Augmented Preference Optimization (SAPO), an effective and scalable training paradigm without the need of existing paired data. Built upon the self-play concept that autonomously generate negative responses, we further involve the off-policy learning pipeline to improve the data exploration and exploitation. Specifically, we employ an Exponential Moving Average (EMA) model along with a replay buffer to enable dynamic updates of response segments, effectively integrating real-time feedback with historical data insights. Our comprehensive evaluations of the LLaMA3-8B and Mistral-7B models across benchmarks—including the Open LLM Leaderboard, IFEval, AlpacaEval 2.0, and MT-Bench—demonstrate that SAPO matches or surpasses established offline contrastive baselines, such as DPO and Odds Ratio Preference Optimization (ORPO), and outperforms offline self-play methods like SPIN.

## item_id: m_2995

TITLE: What Is the Best Practice for CNNs Applied to Visual Instance Retrieval?

ABSTRACT: Previous work has shown that feature maps of deep convolutional neural networks (CNNs)
can be interpreted as feature representation of a particular image region. Features aggregated from
these feature maps have been exploited for image retrieval tasks and achieved state-of-the-art performances in
recent years. The key to the success of such methods is the feature representation. However, the different
factors that impact the effectiveness of features are still not explored thoroughly. There are much less
discussion about the best combination of them.

The main contribution of our paper is the thorough evaluations of the various factors that affect the
discriminative ability of the features extracted from CNNs. Based on the evaluation results, we also identify 
the best choices for different factors and propose a new multi-scale image feature representation method to 
encode the image effectively. Finally, we show that the proposed method generalises well and outperforms 
the state-of-the-art methods on four typical datasets used for visual instance retrieval.

## item_id: m_2996

TITLE: Representation and Bias in Multilingual NLP: Insights from Controlled Experiments on Conditional Language Modeling

ABSTRACT: Inspired by the phenomenon of performance disparity between languages in machine translation, we investigate whether and to what extent languages are equally hard to "conditional-language-model". Our goal is to improve our understanding and expectation of the relationship between language, data representation, size, and performance. We study one-to-one, bilingual conditional language modeling through a series of systematically controlled experiments with the Transformer and the 6 languages from the United Nations Parallel Corpus. We examine character, byte, and word models in 30 language directions and 5 data sizes, and observe indications suggesting a script bias on the character level, a length bias on the byte level, and a word bias that gives rise to a hierarchy in performance across languages. We also identify two types of sample-wise non-monotonicity --- while word-based representations are prone to exhibit Double Descent, length can induce unstable performance across the size range studied in a novel meta phenomenon which we term "erraticity". By eliminating statistically significant performance disparity on the character and byte levels by normalizing length and vocabulary in the data, we show that, in the context of computing with the Transformer, there is no complexity intrinsic to languages other than that related to their statistical attributes and that performance disparity is not a necessary condition but a byproduct of word segmentation. Our application of statistical comparisons as a fairness measure also serves as a novel rigorous method for the intrinsic evaluation of languages, resolving a decades-long debate on language complexity. While these quantitative biases leading to disparity are mitigable through a shallower network, we find room for a human bias to be reflected upon. We hope our work helps open up new directions in the area of language and computing that would be fairer and more flexible and foster a new transdisciplinary perspective for DL-inspired scientific progress.

## item_id: m_2997

TITLE: BBRefinement: an universal scheme to improve precision of box object detectors

ABSTRACT: We present a conceptually simple yet powerful and flexible scheme for refining predictions of bounding boxes. Our approach is trained standalone on GT boxes and can then be combined with an object detector to improve its predictions. The method, called BBRefinement, uses mixture data of image information and the object's class and center. Due to the transformation of the problem into a domain where BBRefinement does not care about multiscale detection, recognition of the object's class, computing confidence, or multiple detections, the training is much more effective. It results in the ability to refine even COCO's ground truth labels into a more precise form. BBRefinement improves the performance of SOTA architectures up to 2mAP points on the COCO dataset in the benchmark. The refinement process is fast; it adds 50-80ms overhead to a standard detector using RTX2080, so it can run in real-time on standard hardware. The code is available at https://gitlab.com/irafm-ai/bb-refinement.

## item_id: m_2998

TITLE: Scaling Speech-Text Pre-training with Synthetic Interleaved Data

ABSTRACT: Speech language models (SpeechLMs) accept speech input and produce speech output, allowing for more natural human-computer interaction compared to text-based large language models (LLMs).
Traditional approaches for developing SpeechLMs are constrained by the limited availability of unsupervised speech data and parallel speech-text data, which are significantly less abundant compared to text pre-training data, thereby limiting their scalability as LLMs.
We propose a novel approach to scaling speech-text pre-training by leveraging large-scale synthetic interleaved data derived from text corpora, eliminating the need for parallel speech-text datasets.
Our method efficiently constructs speech-text interleaved data by sampling text spans from existing text corpora and synthesizing corresponding speech spans using a text-to-token model, bypassing the need to generate actual speech.
We also employ a supervised speech tokenizer derived from an automatic speech recognition (ASR) model  by incorporating a vector-quantized bottleneck into the encoder. This supervised training approach results in discrete speech tokens with strong semantic preservation even at lower sampling rates (e.g. 12.5Hz), while still maintaining speech reconstruction quality.
Starting from a pre-trained language model and scaling our pre-training to 1 trillion tokens (with 600B synthetic interleaved speech-text data), we achieve state-of-the-art performance in both speech language modeling and spoken question answering, improving performance on spoken questions tasks from the previous SOTA of 13\% (Moshi) to 31\%.
We further demonstrate that by fine-tuning the pre-trained model with speech dialogue data, we can develop an end-to-end spoken chatbot that achieves competitive performance comparable to existing baselines in both conversational abilities and speech quality, even operating exclusively in the speech domain.

## item_id: m_2999

TITLE: Provable weak-to-strong generalization via benign overfitting

ABSTRACT: The classic teacher-student model in machine learning posits that a strong teacher supervises a weak student to improve the student's capabilities.
    We instead consider the inverted situation, where a weak teacher supervises a strong student with imperfect pseudolabels. 
    This paradigm was recently brought forth by \citet{burns2023weak} and termed \emph{weak-to-strong generalization}. 
    We theoretically investigate weak-to-strong generalization for binary and multilabel classification in a stylized overparameterized spiked covariance model with Gaussian covariates where the weak teacher's pseudolabels are asymptotically like random guessing.
    Under these assumptions, we provably identify two asymptotic phases of the strong student's generalization after weak supervision: (1) successful generalization and (2) random guessing. 
    Our techniques should eventually extend to weak-to-strong multiclass classification. 
    Towards doing so, we prove a tight lower tail inequality for the maximum of correlated Gaussians, which may be of independent interest.
    Understanding the multilabel setting reinforces the value of using logits for weak supervision when they are available.

## item_id: m_3000

TITLE: SubMix: Practical Private Prediction for Large-scale Language Models

ABSTRACT: Recent data-extraction attacks have exposed that language models can memorize some training samples verbatim. This is a vulnerability that can compromise the privacy of the model’s training data. In this work, we introduce SubMix a practical protocol for private next-token prediction designed to prevent privacy violations by language models that were fine-tuned on a private corpus after pre-training on a public corpus. We show that SubMix limits the leakage of information that is unique to any individual user in the private corpus via a relaxation of group differentially private prediction. Importantly, SubMix admits a tight, data-dependent privacy accounting mechanism, which allows it to thwart existing data-extraction attacks while maintaining the utility of the language model. SubMix is the first protocol that maintains privacy even when publicly releasing tens of thousands of next-token predictions made by large transformer-based models such as GPT-2.
