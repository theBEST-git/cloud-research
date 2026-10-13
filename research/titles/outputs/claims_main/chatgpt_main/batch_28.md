# Batch 28 — 100 items

## item_id: m_2701

TITLE: DyVEDeep: Dynamic Variable Effort Deep Neural Networks

ABSTRACT: Deep Neural Networks (DNNs) have advanced the state-of-the-art on a variety of machine learning tasks and are deployed widely in many real-world products. However, the compute and data requirements demanded by large-scale DNNs remains a significant challenge. In this work, we address this challenge in the context of DNN inference. We propose Dynamic Variable Effort Deep Neural Networks (DyVEDeep), which exploit the heterogeneity in the characteristics of inputs to DNNs to improve their compute efficiency while maintaining the same classification accuracy. DyVEDeep equips DNNs with dynamic effort knobs, which in course of processing an input, identify how critical a group of computations are to classify the input. DyVEDeep dynamically focuses its compute effort only on the critical computations, while the skipping/approximating the rest. We propose 3 effort knobs that operate at different levels of granularity viz. neuron, feature and layer levels. We build DyVEDeep versions for 5 popular image recognition benchmarks on 3 image datasets---MNIST, CIFAR and ImageNet. Across all benchmarks, DyVEDeep achieves 2.1X-2.6X reduction in number of scalar operations, which translates to 1.9X-2.3X performance improvement over a Caffe-based sequential software implementation, for negligible loss in accuracy.

## item_id: m_2702

TITLE: Composable Planning with Attributes

ABSTRACT: The tasks that an agent will need to solve often aren’t known during training. However, if the agent knows which properties of the environment we consider im- portant, then after learning how its actions affect those properties the agent may be able to use this knowledge to solve complex tasks without training specifi- cally for them. Towards this end, we consider a setup in which an environment is augmented with a set of user defined attributes that parameterize the features of interest. We propose a model that learns a policy for transitioning between “nearby” sets of attributes, and maintains a graph of possible transitions. Given a task at test time that can be expressed in terms of a target set of attributes, and a current state, our model infers the attributes of the current state and searches over paths through attribute space to get a high level plan, and then uses its low level policy to execute the plan. We show in grid-world games and 3D block stacking that our model is able to generalize to longer, more complex tasks at test time even when it only sees short, simple tasks at train time.


## item_id: m_2703

TITLE: Mixed Precision Training

ABSTRACT: Increasing the size of a neural network typically improves accuracy but also increases the memory and compute requirements for training the model. We introduce methodology for training deep neural networks using half-precision floating point numbers, without losing model accuracy or having to modify hyper-parameters. This nearly halves memory requirements and, on recent GPUs, speeds up arithmetic. Weights, activations, and gradients are stored in IEEE half-precision format. Since this format has a narrower range than single-precision we propose three techniques for preventing the loss of critical information. Firstly, we recommend maintaining a single-precision copy of weights that accumulates the gradients after each optimizer step (this copy is rounded to half-precision for the forward- and back-propagation). Secondly, we propose loss-scaling to preserve gradient values with small magnitudes. Thirdly, we use half-precision arithmetic that accumulates into single-precision outputs, which are converted to half-precision before storing to memory. We demonstrate that the proposed methodology works across a wide variety of tasks and modern large scale (exceeding 100 million parameters) model architectures, trained on large datasets.

## item_id: m_2704

TITLE: PiCO: Contrastive Label Disambiguation for Partial Label Learning

ABSTRACT: Partial label learning (PLL) is an important problem that allows each training example to be labeled with a coarse candidate set, which well suits many real-world data annotation scenarios with label ambiguity.  Despite the promise, the performance of PLL often lags behind the supervised counterpart. In this work, we bridge the gap by addressing two key research challenges in PLL---representation learning and label disambiguation---in one coherent framework. Specifically, our proposed framework PiCO consists of a contrastive learning module along with a novel class prototype-based label disambiguation algorithm. PiCO produces closely aligned representations for examples from the same classes and facilitates label disambiguation. Theoretically, we show that these two components are mutually beneficial, and can be rigorously justified from an expectation-maximization (EM) algorithm perspective. Extensive experiments demonstrate that PiCO significantly outperforms the current state-of-the-art approaches in PLL and even achieves comparable results to fully supervised learning. Code and data available: https://github.com/hbzju/PiCO.

## item_id: m_2705

TITLE: Domain-Invariant Representation Learning with Global and Local Consistency

ABSTRACT: In this paper, we give an analysis of the existing representation learning framework of unsupervised domain adaptation and show that the learned feature representations of the source domain samples are with discriminability, compressibility, and transferability. However, the learned feature representations of the target domain samples are only with compressibility and transferability. To address this challenge, we propose a novel framework and show from the information theory view that this framework can effectively improve the discriminability of the target domain sample representation. We also propose a method, namely domain-invariant representation learning with global and local consistency (RLGLC), under this framework. In particular, to maintain the global consistency, RLGLC proposes a new metric called asymmetrically-relaxed Wasserstein of Wasserstein distance (AR-WWD), AR-WWD can not only extract the transferability and compressibility of the feature representation of two domains, but also correlates well with human perception. To impose the local consistency structures, we propose a regularized contrastive loss, which can not only keep as much as possible predictive information contained in the feature representation of the target domain, but also alleviates the problem that semantically similar instances are undesirable pushed apart in training processing. Finally, we verify the effectiveness of RLGLC from both theoretical analyses on Bayes error rate and experimental validation on several benchmarks.

## item_id: m_2706

TITLE: Dynamic Tensor Rematerialization

ABSTRACT: Checkpointing enables the training of deep learning models under restricted memory budgets by freeing intermediate activations from memory and recomputing them on demand. Current checkpointing techniques statically plan these recomputations offline and assume static computation graphs. We demonstrate that a simple online algorithm can achieve comparable performance by introducing Dynamic Tensor Rematerialization (DTR), a greedy online algorithm for checkpointing that is extensible and general, is parameterized by eviction policy, and supports dynamic models. We prove that DTR can train an $N$-layer linear feedforward network on an  $\Omega(\sqrt{N})$ memory budget with only $\mathcal{O}(N)$ tensor operations. DTR closely matches the performance of optimal static checkpointing in simulated experiments. We incorporate a DTR prototype into PyTorch merely by interposing on tensor allocations and operator calls and collecting lightweight metadata on tensors.

## item_id: m_2707

TITLE: Learning to Treat Sepsis with Multi-Output Gaussian Process Deep Recurrent Q-Networks

ABSTRACT: Sepsis is a life-threatening complication from infection and a leading cause of mortality in hospitals.  While early detection of sepsis improves patient outcomes, there is little consensus on exact treatment guidelines, and treating septic patients remains an open  problem.  In this work we present a new deep reinforcement learning method that we use to learn optimal personalized treatment policies for septic patients. We model patient continuous-valued physiological time series using multi-output Gaussian processes, a probabilistic model that easily handles missing values and irregularly spaced observation times while maintaining estimates of uncertainty. The Gaussian process is directly tied to a deep recurrent Q-network that learns clinically interpretable treatment policies, and both models are learned together end-to-end.  We evaluate our approach on a heterogeneous dataset of septic spanning 15 months from our university health system, and find that our learned policy could reduce patient mortality by as much as 8.2\% from an overall baseline mortality rate of 13.3\%.  Our algorithm could be used to make treatment recommendations to physicians as part of a decision support tool, and the framework readily applies to other reinforcement learning problems that rely on sparsely sampled and frequently missing multivariate time series data.


## item_id: m_2708

TITLE: Equivariant Entity-Relationship Networks

ABSTRACT: Due to its extensive use in databases, the relational model is ubiquitous in representing big-data. However, recent progress in deep learning with relational data has been focused on (knowledge) graphs. In this paper we propose Equivariant Entity-Relationship Networks, the class of parameter-sharing neural networks derived from the entity-relationship model. We prove that our proposed feed-forward layer is the most expressive linear layer under the given equivariance constraints, and subsumes recently introduced equivariant models for sets, exchangeable tensors, and graphs. The proposed feed-forward layer has linear complexity in the the data and can be used for both inductive and transductive reasoning about relational databases, including database embedding, and the prediction of missing records. This, provides a principled theoretical foundation for the application of deep learning to one of the most abundant forms of data.

## item_id: m_2709

TITLE: Intervention-based Recurrent Casual Model for Non-stationary Video Causal Discovery

ABSTRACT: Non-stationary casual structures are prevalent in real-world physical systems. For example, the stacked blocks interacted with one another until they fall apart, while the billiard balls are moving independently until they collide. However, most video causal discovery methods can not discover such non-stationary casual structures due to the lack of modeling for the instantaneous change and the dynamics of the casual structure. In this work, we propose the Intervention-based Recurrent Casual Model (IRCM) for non-stationary video casual discovery. First, we extend the existing intervention-based casual discovery framework for videos to formulate the instantaneous change of the casual structure in a principled manner. Then, we use a recurrent model to sequentially predict the causal structure model based on previous observations to capture the non-stationary dynamic of the casual structure. We evaluate our method on two popular physical system simulation datasets with various types of multi-body interactions. Experimental results show that the proposed IRCM achieves the state-of-the-art performance on both the counterfactual reasoning and future forecasting tasks.

## item_id: m_2710

TITLE: Incremental Hierarchical Reinforcement Learning with Multitask LMDPs

ABSTRACT: Exploration is a well known challenge in Reinforcement Learning. One principled way of overcoming this challenge is to find a hierarchical abstraction of the base problem and explore at these higher levels, rather than in the space of primitives. However, discovering a deep abstraction autonomously remains a largely unsolved problem, with practitioners typically hand-crafting these hierarchical control architectures. Recent work with multitask linear Markov decision processes, allows for the autonomous discovery of deep hierarchical abstractions, but operates exclusively in the offline setting. By extending this work, we develop an agent that is capable of incrementally growing a hierarchical representation, and using its experience to date to improve exploration.

## item_id: m_2711

TITLE: Hierarchical Representations for Efficient Architecture Search

ABSTRACT: We explore efficient neural architecture search methods and show that a simple yet powerful evolutionary algorithm can discover new architectures with excellent performance. Our approach combines a novel hierarchical genetic representation scheme that imitates the modularized design pattern commonly adopted by human experts, and an expressive search space that supports complex topologies. Our algorithm efficiently discovers architectures that outperform a large number of manually designed models for image classification, obtaining top-1 error of 3.6% on CIFAR-10 and 20.3% when transferred to ImageNet, which is competitive with the best existing neural architecture search approaches. We also present results using random search, achieving 0.3% less top-1 accuracy on CIFAR-10 and 0.1% less on ImageNet whilst reducing the search time from 36 hours down to 1 hour.

## item_id: m_2712

TITLE: The loss surface of residual networks: Ensembles and the role of batch normalization

ABSTRACT: Deep Residual Networks present a premium in performance in comparison to conventional
networks of the same depth and are trainable at extreme depths. It has
recently been shown that Residual Networks behave like ensembles of relatively
shallow networks. We show that these ensemble are dynamic: while initially
the virtual ensemble is mostly at depths lower than half the network’s depth, as
training progresses, it becomes deeper and deeper. The main mechanism that controls
the dynamic ensemble behavior is the scaling introduced, e.g., by the Batch
Normalization technique. We explain this behavior and demonstrate the driving
force behind it. As a main tool in our analysis, we employ generalized spin glass
models, which we also use in order to study the number of critical points in the
optimization of Residual Networks.

## item_id: m_2713

TITLE: Sharpness-Aware Minimization in Large-Batch Training: Training Vision Transformer In Minutes

ABSTRACT: Large-batch training is an important direction for distributed machine learning, which can improve the utilization of large-scale clusters and therefore accelerate the training process. However, recent work illustrates that large-batch training is prone to converge to sharp minima and cause a huge generalization gap. Sharpness-Aware Minimization (SAM) tries to narrow the generalization gap by seeking parameters that lie in a flat region. However, it requires two sequential gradient calculations that doubles the computational overhead. In this paper, we propose a novel algorithm LookSAM to significantly reduce its additional training cost. We further propose a layer-wise modification for adapting LookSAM to the large-batch training setting (Look-LayerSAM). Equipped with our enhanced training algorithm, we are the first to successfully scale up the batch size when training Vision Transformers (ViTs). With a 64k batch size, we are able to train ViTs from scratch within an hour while maintaining competitive performance.

## item_id: m_2714

TITLE: Building effective deep neural networks one feature at a time

ABSTRACT: Successful training of convolutional neural networks is often associated with suffi-
ciently deep architectures composed of high amounts of features. These networks
typically rely on a variety of regularization and pruning techniques to converge
to less redundant states. We introduce a novel bottom-up approach to expand
representations in fixed-depth architectures. These architectures start from just a
single feature per layer and greedily increase width of individual layers to attain
effective representational capacities needed for a specific task. While network
growth can rely on a family of metrics, we propose a computationally efficient
version based on feature time evolution and demonstrate its potency in determin-
ing feature importance and a networks’ effective capacity. We demonstrate how
automatically expanded architectures converge to similar topologies that benefit
from lesser amount of parameters or improved accuracy and exhibit systematic
correspondence in representational complexity with the specified task. In contrast
to conventional design patterns with a typical monotonic increase in the amount of
features with increased depth, we observe that CNNs perform better when there is
more learnable parameters in intermediate, with falloffs to earlier and later layers.

## item_id: m_2715

TITLE: Variational Network Quantization

ABSTRACT: In this paper, the preparation of a neural network for pruning and few-bit quantization is formulated as a variational inference problem. To this end, a quantizing prior that leads to a multi-modal, sparse posterior distribution over weights, is introduced and a differentiable Kullback-Leibler divergence approximation for this prior is derived. After training with Variational Network Quantization, weights can be replaced by deterministic quantization values with small to negligible loss of task accuracy (including pruning by setting weights to 0). The method does not require fine-tuning after quantization. Results are shown for ternary quantization on LeNet-5 (MNIST) and DenseNet (CIFAR-10).

## item_id: m_2716

TITLE: Clustering with Deep Learning: Taxonomy and New Methods

ABSTRACT: Clustering is a fundamental machine learning method. The quality of its results is dependent on the data distribution. For this reason, deep neural networks can be used for learning better representations of the data. In this paper, we propose a systematic taxonomy for clustering with deep learning, in addition to a review of methods from the field. Based on our taxonomy, creating new methods is more straightforward. We also propose a new approach which is built on the taxonomy and surpasses some of the limitations of some previous work. Our experimental evaluation on image datasets shows that the method approaches state-of-the-art clustering quality, and performs better in some cases.

## item_id: m_2717

TITLE: HiMAE: Hierarchical Masked Autoencoders Discover Resolution-Specific Structure in Wearable Time Series

ABSTRACT: Wearable sensors provide abundant physiological time series observations, yet the resolution at which we should extract features for downstream tasks remain unclear. We hypothesize that temporal resolution is a fundamental axis of representation learning, with different clinical and behavioral outcomes relying on features at distinct scales. To test this resolution hypothesis, we introduce HiMAE (Hierarchical Masked Autoencoder), a self-supervised framework that combines masked autoencoding with a hierarchical convolutional encoder–decoder. HiMAE produces multi-resolution embeddings across its intermediate layers that enable systematic evaluation of which temporal scales carry predictive signal, transforming resolution from a hyperparameter into a probe for interpretability. Across classification and generative benchmarks, HiMAE consistently outperforms state-of-the-art foundation models that collapse scale, while being orders of magnitude smaller. Due to the convolution based design choices behind HiMAE, the model is also compact enough to run entirely on-device, achieving sub-millisecond inference on smartwatch-class CPUs for true edge inference. Together, these contributions position HiMAE as both an efficient self supervised learning method and a discovery tool for understanding how time resolution contributes to downstream task alignment.

## item_id: m_2718

TITLE: Single Motion Diffusion

ABSTRACT: Synthesizing realistic animations of humans, animals, and even imaginary creatures, has long been a goal for artists and computer graphics professionals. Compared to the imaging domain, which is rich with large available datasets, the number of data instances for the motion domain is limited, particularly for the animation of animals and exotic creatures (e.g., dragons), which have unique skeletons and motion patterns. In this work, we introduce SinMDM, a Single Motion Diffusion Model. It is designed to learn the internal motifs of a single motion sequence with arbitrary topology and synthesize a variety of motions of arbitrary length that remain faithful to the learned motifs. We harness the power of diffusion models and present a denoising network explicitly designed for the task of learning from a single input motion. SinMDM is crafted as a lightweight architecture, which avoids overfitting by using a shallow network with local attention layers that narrow the receptive field and encourage motion diversity. Our work applies to multiple contexts, including spatial and temporal in-betweening, motion expansion, style transfer, and crowd animation. Our results show that SinMDM outperforms existing methods both qualitatively and quantitatively. Moreover, while prior network-based approaches require additional training for different applications, SinMDM supports these applications during inference. Our project page, which includes links to the code and trained models, is accessible at https://sinmdm.github.io/SinMDM-page.

## item_id: m_2719

TITLE: UniMMVSR: A Unified Multi-Modal Framework for Cascaded Video Super-Resolution

ABSTRACT: Cascaded generation framework has emerged as a promising technique for decoupling the computational burden associated with generating high-resolution videos using large foundation models. Existing studies, however, are largely confined to text-to-video tasks and fail to leverage additional generative conditions beyond text, which are crucial for ensuring fidelity in multi-modal video generation. We address this limitation by presenting UniMMVSR, the first unified generative video super-resolution framework to incorporate hybrid-modal conditions, including text, images, and videos. We conduct a comprehensive exploration of condition injection strategies, training schemes, and data mixture techniques within a latent video diffusion model. A key challenge was designing distinct data construction and condition utilization methods to enable the model to precisely utilize all condition types, given their varied correlations with the target video. Our experiments demonstrate that UniMMVSR significantly outperforms existing methods, producing videos with superior detail and a higher degree of conformity to multi-modal conditions. We also validate the feasibility of combining UniMMVSR with a base model to achieve multi-modal guided generation of 4K videos—a feat previously unattainable with existing techniques.

## item_id: m_2720

TITLE: Understanding Graph Learning with Local Intrinsic Dimensionality

ABSTRACT: Many real-world problems can be formulated as graphs and solved by graph learning techniques. Whilst the rise of Graph Neural Networks (GNNs) has greatly advanced graph learning, there is still a lack of understanding of the intrinsic properties of graph data and their impact on graph learning. In this paper, we narrow the gap by studying the intrinsic dimension of graphs with \emph{Local Intrinsic Dimensionality (LID)}. The LID of a graph measures the expansion rate of the graph as the local neighborhood size of the nodes grows.
With LID, we estimate and analyze the intrinsic dimensions of node features, graph structure and representations learned by GNNs. We first show that feature LID (FLID) and structure LID (SLID) are well correlated with the complexity of synthetic graphs. Following this, we conduct a comprehensive analysis of 12 popular graph datasets of diverse categories and show that 1) graphs of lower FLIDs and SLIDs are generally easier to learn; 2) GNNs learn by mapping graphs (feature and structure together) to low-dimensional manifolds that are of much lower representation LIDs (RLIDs), i.e., RLID $\ll$ FLID/SLID; and 3) when the layers go deep in message-passing based GNNs, the underlying graph will converge to a complete graph of $\operatorname{SLID}=0.5$, losing structural information and causing the over-smoothing problem.

## item_id: m_2721

TITLE: Recurrent Neural Networks with Top-k Gains for Session-based Recommendations

ABSTRACT: RNNs have been shown to be excellent models for sequential data and in particular for session-based user behavior. The use of RNNs provides impressive performance benefits over classical methods in session-based recommendations. In this work we introduce a novel ranking loss function tailored for RNNs in recommendation settings. The better performance of such loss over alternatives, along with further tricks and improvements described in this work, allow to achieve an overall improvement of up to 35% in terms of MRR and Recall@20 over previous session-based RNN solutions and up to 51% over classical collaborative filtering approaches. Unlike data augmentation-based improvements, our method does not increase training times significantly.

## item_id: m_2722

TITLE: 3D-ATRES: Ambiguity-Tolerant Learning for 3D Referring Expression Segmentation

ABSTRACT: 3D Referring Expression Segmentation (3D-RES) is an emerging yet challenging task at the interaction of 3D vision and language, which aims to precisely segment a target instance within a 3D point cloud based on a given natural language referring expression. However, most previous methods overlook multi-source ambiguities that are prevalent in real-world scenarios, including prompt, spatial, and annotation ambiguities. Prompt ambiguity arises from confusion between referent and target instances due to ambiguous language, spatial ambiguity results from viewpoint variations causing incomplete segmentation, and annotation ambiguity stems from inconsistent or noisy labeling in training data. In this paper, we propose a novel 3D Ambiguity-Tolerant Referring Expression Segmentation (3D-ATRES), which explicitly models and mitigates multi-source ambiguities in 3D-RES. Specifically, we employ $\text{TR}^{2}$ Semantic Structurizer to transform free-form natural language into structured Target-Relation-Referent triples, thereby eliminating referential ambiguity. For spatial ambiguity, we introduce a Normal‑Aware Spatial Alignment that leverages surface normal cues to achieve viewpoint-consistent geometry alignment. To mitigate annotation ambiguity, we introduce an Annotation Ambiguity Penalty, which enables the network to adaptively learn from noisy or inconsistent annotations through confidence evaluation. Experiments on ScanRefer and Multi3DRefer show that 3D-ATRES achieves state-of-the-art performance, confirming the effectiveness of modeling ambiguity in 3D-RES.

## item_id: m_2723

TITLE: From Hard to Soft: Understanding Deep Network Nonlinearities via Vector Quantization and Statistical Inference

ABSTRACT: Nonlinearity is crucial to the performance of a deep (neural) network (DN).
To date there has been little progress understanding the menagerie of available  nonlinearities, but recently progress has been made on understanding the r\^{o}le played by piecewise affine and convex nonlinearities like the ReLU and absolute value activation functions and max-pooling.
In particular, DN layers constructed from these operations can be interpreted as {\em max-affine spline operators} (MASOs) that have an elegant link to vector quantization (VQ) and $K$-means.
While this is good theoretical progress, the entire MASO approach is predicated on the requirement that the nonlinearities be piecewise affine and convex, which precludes important activation functions like the sigmoid, hyperbolic tangent, and softmax.
{\em This paper extends the MASO framework to these and an infinitely large class of new nonlinearities by linking deterministic MASOs with probabilistic Gaussian Mixture Models (GMMs).}
We show that, under a GMM, piecewise affine, convex nonlinearities like ReLU, absolute value, and max-pooling can be interpreted as solutions to certain natural ``hard'' VQ inference problems, while sigmoid, hyperbolic tangent, and softmax can be interpreted as solutions to corresponding ``soft'' VQ inference problems.
We further extend the framework by hybridizing the hard and soft VQ optimizations to create a $\beta$-VQ inference that interpolates between hard, soft, and linear VQ inference.
A prime example of a $\beta$-VQ DN nonlinearity is the {\em swish} nonlinearity, which offers state-of-the-art performance in a range of computer vision tasks but was developed ad hoc by experimentation.
Finally, we validate with experiments an important assertion of our theory, namely that DN performance can be significantly improved by enforcing orthogonality in its linear filters.


## item_id: m_2724

TITLE: Frame Averaging for Invariant and Equivariant Network Design

ABSTRACT: Many machine learning tasks involve learning functions that are known to be invariant or equivariant to certain symmetries of the input data. However, it is often challenging to design neural network architectures that respect these symmetries while being expressive and computationally efficient. For example, Euclidean motion invariant/equivariant graph or point cloud neural networks. 
We introduce Frame Averaging (FA), a highly general purpose and systematic framework for adapting known (backbone) architectures to become invariant or equivariant to new symmetry types. Our framework builds on the well known group averaging operator that guarantees invariance or equivariance but is intractable. In contrast, we observe that for many important classes of symmetries, this operator can be replaced with an averaging operator over a small subset of the group elements, called a frame. We show that averaging over a frame guarantees exact invariance or equivariance while often being much simpler to compute than averaging over the entire group. Furthermore, we prove that FA-based models have maximal expressive power in a broad setting and in general preserve the expressive power of their backbone architectures. Using frame averaging, we propose a new class of universal Graph Neural Networks (GNNs), universal Euclidean motion invariant point cloud networks, and Euclidean motion invariant Message Passing (MP) GNNs. We demonstrate the practical effectiveness of FA on several applications including point cloud normal estimation, beyond $2$-WL graph separation, and $n$-body dynamics prediction, achieving state-of-the-art results in all of these benchmarks.

## item_id: m_2725

TITLE: Bowtie Networks: Generative Modeling for Joint Few-Shot Recognition and Novel-View Synthesis

ABSTRACT: We propose a novel task of joint few-shot recognition and novel-view synthesis: given only one or few images of a novel object from arbitrary views with only category annotation, we aim to simultaneously learn an object classifier and generate images of that type of object from new viewpoints. While existing work copes with two or more tasks mainly by multi-task learning of shareable feature representations, we take a different perspective. We focus on the interaction and cooperation between a generative model and a discriminative model, in a way that facilitates knowledge to flow across tasks in complementary directions. To this end, we propose bowtie networks that jointly learn 3D geometric and semantic representations with a feedback loop. Experimental evaluation on challenging fine-grained recognition datasets demonstrates that our synthesized images are realistic from multiple viewpoints and significantly improve recognition performance as ways of data augmentation, especially in the low-data regime. 

## item_id: m_2726

TITLE: Ternary Weight Decomposition and Binary Activation Encoding for Fast and Compact Neural Network

ABSTRACT: This paper aims to reduce test-time computational load of a deep neural network. Unlike previous methods which factorize a weight matrix into multiple real-valued matrices, our method factorizes both weights and activations into integer and noninteger components. In our method, the real-valued weight matrix is approximated by a multiplication of a ternary matrix and a real-valued co-efficient matrix. Since the ternary matrix consists of three integer values, {-1, 0, +1}, it only consumes 2 bits per element. At test-time, an activation vector that passed from a previous layer is also transformed into a weighted sum of binary vectors, {-1, +1}, which enables fast feed-forward propagation based on simple logical operations: AND, XOR, and bit count. This makes it easier to deploy a deep network on low-power CPUs or to design specialized hardware.
In our experiments, we tested our method on three different networks: a CNN for handwritten digits, VGG-16 model for ImageNet classification, and VGG-Face for large-scale face recognition. In particular, when we applied our method to three fully connected layers in the VGG-16, 15x acceleration and memory compression up to 5.2% were achieved with only a 1.43% increase in the top-5 error. Our experiments also revealed that compressing convolutional layers can accelerate inference of the entire network in exchange of slight increase in error.

## item_id: m_2727

TITLE: Adaptive Posterior Learning: few-shot learning with a surprise-based memory module

ABSTRACT: The ability to generalize quickly from few observations is crucial for intelligent systems. In this paper we introduce APL, an algorithm that approximates probability distributions by remembering the most surprising observations it has encountered. These past observations are recalled from an external memory module and processed by a decoder network that can combine information from different memory slots to generalize beyond direct recall. We show this algorithm can perform as well as state of the art baselines on few-shot classification benchmarks with a smaller memory footprint.  In addition, its memory compression allows it to scale to thousands of unknown labels.  Finally, we introduce a meta-learning reasoning task which is more challenging than direct classification. In this setting, APL is able to generalize with fewer than one example per class via deductive reasoning.

## item_id: m_2728

TITLE: Proximal Gradient Descent-Ascent: Variable Convergence under KŁ Geometry

ABSTRACT: The gradient descent-ascent (GDA) algorithm has been widely applied to solve minimax optimization problems. In order to achieve convergent policy parameters for minimax optimization, it is important that GDA generates convergent variable sequences rather than convergent sequences of function value or gradient norm. However, the variable convergence of GDA has been proved only under convexity geometries, and it is lack of understanding in general nonconvex minimax optimization. This paper fills such a gap by studying the convergence of a more general proximal-GDA for regularized nonconvex-strongly-concave minimax optimization. Specifically, we show that proximal-GDA admits a novel Lyapunov function, which monotonically decreases in the minimax optimization process and drives the variable sequences to a critical point. By leveraging this Lyapunov function and the KL geometry that parameterizes the local geometries of general nonconvex functions, we formally establish the variable convergence of proximal-GDA to a certain critical point $x^*$, i.e., $x_t\to x^*, y_t\to y^*(x^*)$. Furthermore, over the full spectrum of the KL-parameterized geometry, we show that proximal-GDA achieves different types of convergence rates ranging from sublinear convergence up to finite-step convergence, depending on the geometry associated with the KL parameter. This is the first theoretical result on the variable convergence for nonconvex minimax optimization. 

## item_id: m_2729

TITLE: Bias-Reduced Uncertainty Estimation for Deep Neural Classifiers

ABSTRACT: We consider the problem of uncertainty estimation in the context of (non-Bayesian) deep neural classification. In this context, all known methods are based on extracting uncertainty signals from a trained network optimized to solve the classification problem at hand. We demonstrate that such techniques tend to introduce biased estimates for instances whose predictions are supposed to be highly confident. We argue that this deficiency is an artifact of the dynamics of training with SGD-like optimizers, and it has some properties similar to overfitting. Based on this observation, we develop an uncertainty estimation algorithm that selectively estimates the uncertainty of highly confident points, using earlier snapshots of the trained model, before their estimates are jittered (and way before they are ready for actual classification). We present extensive experiments indicating that the proposed algorithm provides uncertainty estimates that are consistently better than all known methods.

## item_id: m_2730

TITLE: MaskINT: Video Editing via Interpolative Non-autoregressive Masked Transformers

ABSTRACT: Recent advances in generative AI have significantly enhanced image and video editing, particularly in the context of text prompt control. State-of-the-art approaches predominantly rely on diffusion models to accomplish these tasks. However, the computational demands of diffusion-based methods are substantial, often necessitating large-scale paired datasets for training, causing them challenges to employ in practical applications. This study addresses this challenge by breaking down the text-based video editing process into two stages. In the first stage, we leverage an existing text-to-image diffusion model to simultaneously edit a select few key frames without any additional fine-tuning. In the second stage, we introduce an efficient model called MaskINT, which is built on non-autoregressive masked generative transformers. MaskINT specializes in frame interpolation between the key frames, benefiting from structural guidance provided by intermediate frames. The training of MaskINT incorporates masked token modeling. Our comprehensive set of experiments illustrates the efficacy and efficiency of MaskINT when compared to other diffusion-based methodologies. This research offers a practical solution for text-based video editing and showcases the potential of non-autoregressive masked generative transformers in this domain.

## item_id: m_2731

TITLE: Backdoors Stuck At The Frontdoor: Multi-Agent Backdoor Attacks That Backfire

ABSTRACT: Malicious agents in collaborative learning and outsourced data collection threaten the training of clean models. Backdoor attacks, where an attacker poisons a model during training to successfully achieve targeted misclassification, are a major concern to train-time robustness. In this paper, we investigate a multi-agent backdoor attack scenario, where multiple attackers attempt to backdoor a victim model simultaneously. A consistent backfiring phenomenon is observed across a wide range of games, where agents suffer from a low collective attack success rate. We examine different modes of backdoor attack configurations, non-cooperation / cooperation, joint distribution shifts, and game setups to return an equilibrium attack success rate at the lower bound. The results motivate the re-evaluation of backdoor defense research for practical environments.

## item_id: m_2732

TITLE: Variational Structured Attention Networks for Dense Pixel-Wise Prediction

ABSTRACT: State-of-the-art performances in dense pixel-wise prediction tasks are obtained with specifically designed convolutional networks. These models often benefit from attention mechanisms that allow better learning of deep representations. Recent works showed the importance of estimating both spatial- and channel-wise attention tensors. In this paper, we propose a unified approach to jointly estimate spatial attention maps and channel attention vectors so as to structure the resulting attention tensor. Moreover, we integrate the estimation of the attention within a probabilistic framework, leading to VarIational STructured Attention networks(VISTA). We implement the inference rules within the neural network, thus allowing for joint learning of the probabilistic and the CNN front-end parameters. Importantly, as demonstrated by our extensive empirical evaluation on six large-scale datasets VISTA outperforms the state-of-the-art in multiple continuous and discrete pixel-level prediction tasks, thus confirming the benefit of structuring the attention tensor and of inferring it within a probabilistic formulation.

## item_id: m_2733

TITLE: Classify or Select: Neural Architectures for Extractive Document Summarization

ABSTRACT: We present two novel and contrasting Recurrent Neural Network (RNN) based architectures for extractive summarization of documents. The Classifier based architecture sequentially accepts or rejects each sentence in the original document order for its membership in the summary. The Selector architecture, on the other hand, is free to pick one sentence at a time in any arbitrary order to generate the extractive summary. 

Our models under both architectures jointly capture the notions of salience and redundancy of sentences. In addition, these models have the advantage of being very interpretable, since they allow visualization of their predictions broken up by abstract features such as information content, salience and redundancy. 

We show that our models reach or outperform state-of-the-art supervised models on two different corpora. We also recommend the conditions under which one architecture is superior to the other based on experimental evidence.

## item_id: m_2734

TITLE: TuneMV3D: Tuning Foundational Image Diffusion Models for Generalizable and Scalable Multiview 3D Generation

ABSTRACT: Considerable progress has been made in 2D image generation, but 3D content creation lags behind due to a lack of large-scale, high-quality 3D datasets. To mitigate this gap, a recent line of work leverages 2D diffusion models for 3D generation but usually requires object-specific overfitting, making them unscalable. In this paper, we present TuneMV3D, a novel approach to generating diverse and creative 3D content in a scalable feedforward manner. At the core of TuneMV3D, we tune a foundational image diffusion model using a much smaller-scale 3D dataset while utilizing multi-view images to bridge the gap between 2D and 3D. This allows for the direct prediction of consistent, multi-view 3D representations from 2D diffusion models. We design an interactive diffusion scheme that is facilitated by jointly optimized latent SparseNeuS to ensure that the multi-view generations are consistent. Additionally, we propose a consistency-guided sampling strategy that preserves the creativity of the foundational image diffusion model while maintaining multi-view consistency. Using TuneMV3D, we can successfully distill the 3D counterpart of what can be created by a 2D foundation model, thereby generalizing beyond the small 3D tuning set and enabling scalable and diverse 3D content creation. An anonymous website showcasing the results is available at https://tunemv3d.github.io

## item_id: m_2735

TITLE: Efficacy of Data-Free Metrics: Robust and Critical Evidence From Robust and Critical Layers

ABSTRACT: Data-free methods for analysing and understanding the layers of neural networks have offered many metrics for quantifying notions of ``strong" versus ``weak" layers, with the promise of increased interpretability. We examine the robustness and predictive power of data-free metrics under randomised control conditions across a wide range of models, datasets and architectures. Contrary to some of the literature, we find strong evidence \emph{against} the efficacy of data-free methods. We show that they are not reparametrisation-invariant even for \emph{robust} layers, that is to say layers that can be reparametrised by re-initialisation or re-randomisation without affecting the accuracy of the model. Moreover, we also show that data-free metrics cannot be used for the arguably simpler tasks of (i) distinguishing between robust layers and critical layers, i.e.\ layers that cannot be reparametrised without significantly degrading the accuracy of the model, or (ii) predicting if there will be a performance difference between re-initialisation and re-randomisation. Thus, we argue that to understand neural networks, and in particular the difference between `strong" versus ``weak" layers, we must adopt mechanistic and functional approaches, contrary to the traditional Random Matrix Theory perspective.

## item_id: m_2736

TITLE: Evaluating Lossy Compression Rates of Deep Generative Models

ABSTRACT: Deep generative models have achieved remarkable progress in recent years. Despite this progress, quantitative evaluation and comparison of generative models remains as one of the important challenges. One of the most popular metrics for evaluating generative models is the log-likelihood. While the direct computation of log-likelihood can be intractable, it has been recently shown that the log-likelihood of some of the most interesting generative models such as variational autoencoders (VAE) or generative adversarial networks (GAN) can be efficiently estimated using annealed importance sampling (AIS). In this work, we argue that the log-likelihood metric by itself cannot represent all the different performance characteristics of generative models, and propose to use rate distortion curves to evaluate and compare deep generative models. We show that we can approximate the entire rate distortion curve using one single run of AIS for roughly the same computational cost as a single log-likelihood estimate. We evaluate lossy compression rates of different deep generative models such as VAEs, GANs (and its variants) and adversarial autoencoders (AAE) on MNIST and CIFAR10, and arrive at a number of insights not obtainable from log-likelihoods alone.

## item_id: m_2737

TITLE: Learning Awareness Models

ABSTRACT: We consider the setting of an agent with a fixed body interacting with an unknown and uncertain external world. We show that models trained to predict proprioceptive information about the agent's body come to represent objects in the external world. In spite of being trained with only internally available signals, these dynamic body models come to represent external objects through the necessity of predicting their effects on the agent's own body. That is, the model learns holistic persistent representations of objects in the world, even though the only training signals are body signals. Our dynamics model is able to successfully predict distributions over 132 sensor readings over 100 steps into the future and we demonstrate that even when the body is no longer in contact with an object, the latent variables of the dynamics model continue to represent its shape. We show that active data collection by maximizing the entropy of predictions about the body---touch sensors, proprioception and vestibular information---leads to learning of dynamic models that show superior performance when used for control. We also collect data from a real robotic hand and show that the same models can be used to answer questions about properties of objects in the real world. Videos with qualitative results of our models are available at https://goo.gl/mZuqAV.

## item_id: m_2738

TITLE: A hybrid network: Scattering and Convnet

ABSTRACT: This paper shows how, by combining prior and supervised representations, one can create architectures that lead to nearly state-of-the-art results on standard benchmarks, which mean they perform as well as a deep network learned from scratch. We use scattering as a generic and fixed initialization of the first layers of a deep network, and learn the remaining layers in a supervised manner. We numerically demonstrate that deep hybrid scattering networks generalize better on small datasets than supervised deep networks. Scattering networks could help current systems to save computation time, while guaranteeing the stability  to geometric transformations and noise of the first internal layers. We also show that the learned operators explicitly build invariances to geometrical variabilities, such as local rotation and translation, by analyzing the third layer of our architecture.  We demonstrate that it is possible to replace the scattering transform by a standard deep network at the cost of having to learn more parameters and potentially adding instabilities. Finally, we release a new software, ScatWave, using GPUs for fast computations of a scattering network that is integrated in Torch. We evaluate our model on the CIFAR10, CIFAR100 and STL10 datasets.

## item_id: m_2739

TITLE: A comprehensive, application-oriented study of catastrophic forgetting in DNNs

ABSTRACT: We present a large-scale empirical study of catastrophic forgetting (CF) in modern Deep Neural Network (DNN) models that perform sequential (or: incremental) learning.
A new experimental protocol is proposed that takes into account typical constraints encountered in application scenarios.
As the investigation is empirical, we evaluate CF behavior on the hitherto largest number of visual classification datasets, from each of which we construct a representative number of Sequential Learning Tasks (SLTs) in close alignment to previous works on CF.
Our results clearly indicate that there is no model that avoids CF for all investigated datasets and SLTs under application conditions. We conclude with a discussion of potential solutions and workarounds to CF, notably for the EWC and IMM models.

## item_id: m_2740

TITLE: Generative Learning With Euler Particle Transport

ABSTRACT: We propose an Euler particle transport  (EPT) approach for generative learning.  The proposed approach is motivated by the problem of finding the optimal transport map from a reference distribution to a target distribution characterized by the Monge-Ampere equation. Interpreting the infinitesimal linearization of the Monge-Ampere equation from the perspective of gradient flows in measure spaces leads to a stochastic McKean-Vlasov equation. We use the forward Euler method to solve this equation. The resulting forward Euler map pushes forward a reference distribution to the target. This map is the composition of a sequence of simple residual maps, which are computationally stable and easy to train. The key task in training is the estimation of the density ratios or differences that determine the residual maps. We estimate the density ratios (differences) based on the Bregman divergence with a gradient penalty using deep density-ratio (difference) fitting. We show that the proposed density-ratio (difference) estimators do not suffer from the ``curse of dimensionality" if data is supported on a lower-dimensional manifold. Numerical experiments with multi-mode synthetic datasets and comparisons with the existing methods on real benchmark datasets support our theoretical results and demonstrate the effectiveness of the proposed method.

## item_id: m_2741

TITLE: On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility

ABSTRACT: Large Language Models (LLMs) excel at long-context understanding but exhibit significant limitations in long-form generation. Existing studies primarily focus on single-generation quality, generally overlooking the volatility of the output (i.e., the inconsistency in length and content across multiple generations). This volatility not only leads to significant computational costs but also severely impacts the models' reliable application. To address this gap, our work unfolds in three stages: *benchmarking, probing, and mitigation*. We first propose the **VO**latility in **L**ong-form **T**ext **Bench**mark (**VOLTBench**), a novel heterogeneous-task benchmark designed to systematically quantify the length volatility of long-form generation. Subsequently, by analyzing attention traces, we conduct an in-depth probe to identify several common internal patterns that cause this volatility. Finally, to mitigate long-form output volatility, we propose SELB (Structural Enforcement via Logits Boosting), a lightweight decoding-stage optimization strategy, designed to significantly enhance both the length accuracy and stability of long-form generation without additional training. Extensive experiments on VOLTBench provide the first systematic confirmation of severe long-form output instability in mainstream models and validate that our proposed method successfully improves the mean output length of the base model by 148\% and reduces the length volatility by 69\%, while maintaining high generation quality.

## item_id: m_2742

TITLE: AutoAgents: A Framework for Automatic Agent Generation

ABSTRACT: Large language models (LLMs) have enabled remarkable advances in automated task-solving with multi-agent systems. 
However, most existing LLM-based multi-agent approaches rely on predefined agents to handle simple tasks, limiting the adaptability of multi-agent collaboration to different scenarios.
Therefore, we introduce AutoAgents, an innovative framework that adaptively generates and coordinates multiple specialized agents to build an AI team according to different tasks.
Specifically, AutoAgents couples the relationship between tasks and roles by dynamically generating multiple required agents based on task content and planning solutions for the current task based on the generated expert agents.
Multiple specialized agents collaborate with each other to efficiently accomplish tasks. 
Concurrently, an observer role is incorporated into the framework to reflect on the designated plans and agents' responses and improve upon them.
Our experiments on various benchmarks demonstrate that AutoAgents generates more coherent and accurate solutions than the existing multi-agent methods.
This underscores the significance of assigning different roles to different tasks and of team cooperation, offering new perspectives for tackling complex tasks.

## item_id: m_2743

TITLE: Robust Transfer of Safety-Constrained Reinforcement Learning Agents

ABSTRACT: Reinforcement learning (RL) often relies on trial and error, which may cause undesirable outcomes. As a result, standard RL is inappropriate for safety-critical applications. To address this issue, one may train a safe agent in a controlled environment (where safety violations are allowed) and then transfer it to the real world (where safety violations may have disastrous consequences). Prior work has made this transfer safe as long as the new environment preserves the safety-related dynamics. However, in most practical applications, differences or shifts in dynamics between the two environments are inevitable, potentially leading to safety violations after the transfer. This work aims to guarantee safety even when the new environment has different (safety-related) dynamics. In other words, we aim to make the process of safe transfer robust. Our methodology (1) robustifies an agent in the controlled environment and (2) provably provides---under mild assumption---a safe transfer to new environments. The empirical evaluation shows that this method yields policies that are robust against changes in dynamics, demonstrating safety after transfer to a new environment.

## item_id: m_2744

TITLE: DiffImp: Efficient Diffusion Model for Probabilistic Time Series Imputation with Bidirectional Mamba Backbone

ABSTRACT: Probabilistic time series imputation has been widely applied in real-world scenarios due to its ability to estimate uncertainty of imputation results. Meanwhile, denoising diffusion probabilistic models (DDPMs) have achieved great success in probabilistic time series imputation tasks with its power to model complex distributions. However, current DDPM-based probabilistic time series imputation methodologies are confronted with two types of challenges: 1) \textit{ The backbone modules of the denoising parts are not capable of achieving sequence modeling with low time complexity.} 2) \textit{ The architecture of denoising modules can not handle the inter-variable and bidirectional dependencies in the time series imputation problem effectively.} To address the first challenge, we integrate the computational efficient state space model, namely Mamba, as the backbone denosing module for DDPMs. To tackle the second challenge, we carefully devise several SSM-based blocks for bidirectional modeling and inter-variable relation understanding. Experimental results demonstrate that our approach can achieve state-of-the-art time series imputation results on multiple datasets, different missing scenarios and missing ratios.

## item_id: m_2745

TITLE: On Inductive Biases That Enable Generalization in Diffusion Transformers

ABSTRACT: Recent work studying the generalization of diffusion models with UNet-based denoisers reveals inductive biases that can be expressed via geometry-adaptive harmonic bases. However, in practice, more recent denoising networks are often based on transformers, e.g., the diffusion transformer (DiT). This raises the question: do transformer-based denoising networks exhibit inductive biases that can also be expressed via geometry-adaptive harmonic bases? To our surprise, we find that this is not the case. This discrepancy motivates our search for the inductive bias that can lead to good generalization in DiT models. Investigating a DiT’s pivotal attention modules, we find that locality of attention maps are closely associated with generalization. To verify this finding, we modify the generalization of a DiT by restricting its attention windows. We inject local attention windows to a DiT and observe an improvement in generalization. Furthermore, we empirically find that both the placement and the effective attention size of these local attention windows are crucial factors. Experimental results on the CelebA, ImageNet, and LSUN datasets show that strengthening the inductive bias of a DiT can improve both generalization and generation quality when less training data is available. Source code will be released publicly upon paper publication.

## item_id: m_2746

TITLE: HAMMER: Hamiltonian Curiosity Augmented Large Language Model Reinforcement

ABSTRACT: Recent curriculum reinforcement learning for large language models (LLMs) typically rely on difficulty-based annotations for data filtering and ordering. However, such methods suffer from local optimization, where continual training on simple samples in the early steps causing the policy to lose its exploration. We propose a novel schema, namely *Hamiltonian curiosity AugMented large language ModEl Reinforcement (HAMMER)*, that transfers diversity metrics, commonly used in dataset evaluation, into the dynamic reinforcement learning procedure, where training samples are ordered via a minimum-semantic Hamiltonian path making the initial training retrain more exploration. From a theoretical perspective of generalization bounds, diversity-driven ordering facilitates stable convergence. Empirical evaluations indicate that *HAMMER* stimulates model "curiosity" and consistently achieves a 3% to 4% average accuracy gain across diverse inference benchmark.

## item_id: m_2747

TITLE: CoT: Cooperative Training for Generative Modeling of Discrete Data

ABSTRACT: We propose Cooperative Training (CoT) for training generative models that measure a tractable density for discrete data. CoT coordinately trains a generator G and an auxiliary predictive mediator M. The training target of M is to estimate a mixture density of the learned distribution G and the target distribution P, and that of G is to minimize the Jensen-Shannon divergence estimated through M. CoT achieves independent success without the necessity of pre-training via Maximum Likelihood Estimation or involving high-variance algorithms like REINFORCE. This low-variance algorithm is theoretically proved to be superior for both sample generation and likelihood prediction. We also theoretically and empirically show the superiority of CoT over most previous algorithms in terms of generative quality and diversity, predictive generalization ability and computational cost.

## item_id: m_2748

TITLE: A Frequency Perspective of Adversarial Robustness

ABSTRACT: Adversarial examples pose a unique challenge for deep learning systems.  Despite recent advances in both attacks and defenses, there is still a lack of clarity and consensus in the community about the true nature and underlying properties of adversarial examples. A deep understanding of these examples can provide new insights towards the development of more effective attacks and defenses. Driven by the common misconception that adversarial examples are high-frequency noise, we present a frequency-based understanding of adversarial examples, supported by theoretical and empirical findings. Our analysis shows that adversarial examples are neither in high-frequency nor in low-frequency components, but are simply dataset dependent. Particularly, we highlight the glaring disparities between models trained on CIFAR-10 and ImageNet-derived datasets. Utilizing this framework, we analyze many intriguing properties of training robust models with frequency constraints, and propose a frequency-based explanation for the commonly observed accuracy vs. robustness trade-off.

## item_id: m_2749

TITLE: Unsupervised Deep Learning of State Representation Using Robotic Priors 

ABSTRACT: Our understanding of the world depends highly on how we represent it.  Using background knowledge about its complex underlying physical rules, our brain can produce intuitive and simplified representations which it can easily use to solve problems. The approach of this paper aims to reproduce this simplification process using a neural network to produce a simple low dimensional state representation of the world from images acquired by a robot. As proposed in Jonschkowski & Brock (2015), we train the neural network in an unsupervised way, using the "a priori" knowledge we have about the world as loss functions called "robotic priors" that we implemented through a siamese network. This approach has been used to learn a one dimension representation of a Baxter head position from raw images. The experiment resulted in a 97,7% correlation between the learned representation and the ground truth, and show that relevant visual features form the environment are learned.

## item_id: m_2750

TITLE: Metropolis-Hastings view on variational inference and adversarial training

ABSTRACT: In this paper we propose to view the acceptance rate of the Metropolis-Hastings algorithm as a universal objective for learning to sample from target distribution -- given either as a set of samples or in the form of unnormalized density. This point of view unifies the goals of such approaches as Markov Chain Monte Carlo (MCMC), Generative Adversarial Networks (GANs), variational inference. To reveal the connection we derive the lower bound on the acceptance rate and treat it as the objective for learning explicit and implicit samplers. The form of the lower bound allows for doubly stochastic gradient optimization in case the target distribution factorizes (i.e. over data points). We empirically validate our approach on Bayesian inference for neural networks and generative models for images.

## item_id: m_2751

TITLE: A Context-aware Attention Network for Interactive Question Answering

ABSTRACT: We develop a new model for Interactive Question Answering (IQA), using Gated-Recurrent-Unit recurrent networks (GRUs) as encoders for statements and questions, and another GRU as a decoder for outputs. Distinct from previous work, our approach employs context-dependent word-level attention for more accurate statement representations and question-guided sentence-level attention for better context modeling. Employing these mechanisms, our model accurately understands when it can output an answer or when it requires generating a supplementary question for additional input. When available, user's feedback is encoded and directly applied to update sentence-level attention to infer the answer. Extensive experiments on QA and IQA datasets demonstrate quantitatively the effectiveness of our model with significant improvement over conventional QA models.

## item_id: m_2752

TITLE: Learning Synthetic Environments and Reward Networks for Reinforcement Learning

ABSTRACT: We introduce Synthetic Environments (SEs) and Reward Networks (RNs), represented by neural networks, as proxy environment models for training Reinforcement Learning (RL) agents. We show that an agent, after being trained exclusively on the SE, is able to solve the corresponding real environment. While an SE acts as a full proxy to a real environment by learning about its state dynamics and rewards, an RN is a partial proxy that learns to augment or replace rewards. We use bi-level optimization to evolve SEs and RNs: the inner loop trains the RL agent, and the outer loop trains the parameters of the SE / RN via an evolution strategy. We evaluate our proposed new concept on a broad range of RL algorithms and classic control environments. In a one-to-one comparison, learning an SE proxy requires more interactions with the real environment than training agents only on the real environment. However, once such an SE has been learned, we do not need any interactions with the real environment to train new agents. Moreover, the learned SE proxies allow us to train agents with fewer interactions while maintaining the original task performance. Our empirical results suggest that SEs achieve this result by learning informed representations that bias the agents towards relevant states. Moreover, we find that these proxies are robust against hyperparameter variation and can also transfer to unseen agents.

## item_id: m_2753

TITLE: Factorized linear discriminant analysis for phenotype-guided representation learning of neuronal gene expression data

ABSTRACT: A central goal in neurobiology is to relate the expression of genes to the structural and functional properties of neuronal types, collectively called their phenotypes. Single-cell RNA sequencing can measure the expression of thousands of genes in thousands of neurons. How to interpret the data in the context of neuronal phenotypes? We propose a supervised learning approach that factorizes the gene expression data into components corresponding to individual phenotypic characteristics and their interactions. This new method, which we call factorized linear discriminant analysis (FLDA), seeks a linear transformation of gene expressions that varies highly with only one phenotypic factor and minimally with the others. We further leverage our approach with a sparsity-based regularization algorithm, which selects a few genes important to a specific phenotypic feature or feature combination. We applied this approach to a single-cell RNA-Seq dataset of Drosophila T4/T5 neurons, focusing on their dendritic and axonal phenotypes. The analysis confirms results obtained by conventional methods but also points to new genes related to the phenotypes and an intriguing hierarchy in the genetic organization of these cells.

## item_id: m_2754

TITLE: Two Methods for Wild Variational Inference

ABSTRACT: Variational inference provides a powerful tool for approximate probabilistic inference on complex, structured models. Typical variational inference methods, however, require to use inference networks with computationally tractable probability density functions. This largely limits the design and implementation of variational inference methods. We consider wild variational inference methods that do not require tractable density functions on the inference networks, and hence can be applied in more challenging cases. As an example of application, we treat stochastic gradient Langevin dynamics (SGLD) as an inference network, and use our methods to automatically adjust the step sizes of SGLD to maximize its convergence speed, significantly outperforming the hand-designed step size schemes.

## item_id: m_2755

TITLE: 3D-IntPhys: Learning 3D Visual Intuitive Physics for Fluids, Rigid Bodies, and Granular Materials

ABSTRACT: Given a visual scene, humans have strong intuitions about how a scene can evolve over time under given actions. The intuition, often termed visual intuitive physics, is a critical ability that allows us to make effective plans to manipulate the scene to achieve desired outcomes without relying on extensive trial and error. In this paper, we present a framework capable of learning 3D-grounded visual intuitive physics models purely from unlabeled images. Our method is composed of a conditional Neural Radiance Field (NeRF)-style visual frontend and a 3D point-based dynamics prediction backend, in which we impose strong relational and structural inductive bias to capture the structure of the underlying environment. Unlike existing intuitive point-based dynamics works that rely on the supervision of dense point trajectory from simulators, we relax the requirements and only assume access to multi-view RGB images and (imperfect) instance masks. This enables the proposed model to handle scenarios where accurate point estimation and tracking are hard or impossible. We evaluate the models on three challenging scenarios involving fluid, granular materials, and rigid objects, where standard detection and tracking methods are not applicable. We show our model can make long-horizon future predictions by learning from raw images and significantly outperforms models that do not employ an explicit 3D representation space. We also show that, once trained, our model can achieve strong generalization in complex scenarios under extrapolate settings.

## item_id: m_2756

TITLE: Training-Free Reasoning and Reflection in MLLMs

ABSTRACT: Recent advances in Reasoning LLMs (e.g., DeepSeek-R1 and OpenAI-o1) have showcased impressive reasoning capabilities via reinforcement learning. However, extending these capabilities to Multimodal LLMs (MLLMs) is hampered by the prohibitive costs of retraining and the scarcity of high-quality, verifiable multimodal reasoning datasets. This paper introduces ANO Model (a temporal name for anonymous review), a training-free and R1-like MLLM that imbues off-the-shelf MLLMs with reasoning and reflection abilities, without any gradient updates or extra supervision. Our key insight is to decouple perception and reasoning across MLLM decoder layers. Specifically, we observe that compared to the deeper decoder layers, the shallow decoder layers allocate more attention to visual tokens, while the deeper decoder layers concentrate on textual semantics. This observation motivates a hierarchical weight merging approach that combines a visual-text pretrained MLLM with a reasoning-specialized LLM. To this end, we propose a layer-wise, Taylor-derived closed-form fusion mechanism that integrates reasoning capacity into deep decoder layers while preserving visual grounding in shallow decoder layers. Extensive experiments on challenging multimodal reasoning benchmarks demonstrate the effectiveness of our approach. On the MMMU benchmark, our model ANO-38B achieves an accuracy of 69.2, outperforming the strongest baseline InternVL2.5-38B by +5.3, and even surpasses the proprietary GPT-4o model.

## item_id: m_2757

TITLE: Block-Sample MAC-Bayes Generalization Bounds

ABSTRACT: We present a family of novel block-sample MAC-Bayes bounds (mean approximately correct). While PAC-Bayes bounds (probably approximately correct) typically give bounds for the generalization error that hold with high probability, MAC-Bayes bounds have a similar form but bound the expected generalization error instead. The family of bounds we propose can be understood as a generalization of an expectation version of known PAC-Bayes bounds. Compared to standard PAC-Bayes bounds, the new bounds contain divergence terms that only depend on subsets (or \emph{blocks}) of the training data. The proposed MAC-Bayes bounds hold the promise of significantly improving upon the tightness of traditional PAC-Bayes and MAC-Bayes bounds. This is illustrated with a simple numerical example in which the original PAC-Bayes bound is vacuous regardless of the choice of prior, while the proposed family of bounds are finite for appropriate choices of the block size. We also explore the question whether high-probability versions of our MAC-Bayes bounds (i.e., PAC-Bayes bounds of a similar form) are possible. We answer this question in the negative with an example that shows that in general, it is not possible to establish a PAC-Bayes bound which (a) vanishes with a rate faster than $\mathcal{O}(1/\log n)$ whenever the proposed MAC-Bayes bound vanishes with rate $\mathcal{O}(n^{-1/2})$ and (b) exhibits a logarithmic dependence on the permitted error probability.

## item_id: m_2758

TITLE: GeoDiffusion: Text-Prompted Geometric Control for Object Detection Data Generation

ABSTRACT: Diffusion models have attracted significant attention due to the remarkable ability to create content and generate data for tasks like image classification. However, the usage of diffusion models to generate the high-quality object detection data remains an underexplored area, where not only image-level perceptual quality but also geometric conditions such as bounding boxes and camera views are essential. Previous studies have utilized either copy-paste synthesis or layout-to-image (L2I) generation with specifically designed modules to encode the semantic layouts. In this paper, we propose the GeoDiffusion, a simple framework that can flexibly translate various geometric conditions into text prompts and empower pre-trained text-to-image (T2I) diffusion models for high-quality detection data generation. Unlike previous L2I methods, our GeoDiffusion is able to encode not only the bounding boxes but also extra geometric conditions such as camera views in self-driving scenes. Extensive experiments demonstrate GeoDiffusion outperforms previous L2I methods while maintaining 4x training time faster. To the best of our knowledge, this is the first work to adopt diffusion models for layout-to-image generation with geometric conditions and demonstrate that L2I-generated images can be beneficial for improving the performance of object detectors.

## item_id: m_2759

TITLE: Similarity-Constrained Reweighting for Complex Query Answering on Knowledge Graphs

ABSTRACT: Machine learning models for answering complex queries on knowledge graphs estimate the likelihood of answers that are not reachable via direct traversal. Prior work in this area has focused on structured queries whose constraints are expressed in first-order logic. Recent work has proposed to extend such logical constraints with *soft entity constraints*, which require the answer to a query (also known as the *target variable*) to be similar or dissimilar to specified sets of entities.

A natural but unexplored generalization of this extension is to allow specifying similarity constraints not only on the answer to a query, but also on the values assigned to *intermediate variables*, which frequently occur in complex queries. In this work, we study this more general formulation and introduce SCORE: a computationally efficient and interpretable method for incorporating similarity constraints at arbitrary positions of a query. Unlike approaches that rely on deep neural networks, SCORE is based on a lightweight and interpretable score adjustment function that only requires tuning two parameters on a validation set.

Our experiments on a challenging benchmark over three different knowledge graphs demonstrate that on the special case of constraints on the target variable, SCORE is able to incorporate preferences without degrading overall query answering performance, with significantly increased ranking performance over a learned neural baseline. Moreover, SCORE maintains its performance in the more general setting with constraints on intermediate variables.

## item_id: m_2760

TITLE: Is Your Multimodal Language Model Oversensitive to Safe Queries?

ABSTRACT: Humans are prone to cognitive distortions — biased thinking patterns that lead to exaggerated responses to specific stimuli, albeit in very different contexts.
This paper demonstrates that advanced Multimodal Large Language Models (MLLMs) exhibit similar tendencies.
While these models are designed to respond queries under safety mechanism, they sometimes reject harmless queries in the presence of certain visual stimuli, disregarding the benign nature of their contexts.
As the initial step in investigating this behavior, we identify three representative types of stimuli that trigger the oversensitivity of existing MLLMs: $\textbf{\textit{Exaggerated Risk}}$, $\textbf{\textit{Negated Harm}}$, and $\textbf{\textit{Counterintuitive Interpretation}}$.
To systematically evaluate MLLMs' oversensitivity to these stimuli, we propose the $\textbf{M}$ultimodal $\textbf{O}$ver$\textbf{S}$en$\textbf{S}$itivity $\textbf{Bench}$mark (MOSSBench).
This toolkit consists of 300 manually collected benign multimodal queries, cross-verified by third-party reviewers (AMT).
Empirical studies using MOSSBench on 20 MLLMs reveal several insights:
(1). Oversensitivity is prevalent among SOTA MLLMs, with refusal rates reaching up to $\textbf{76}$\% for harmless queries.
(2). Safer models are more oversensitive: increasing safety may inadvertently raise caution and conservatism in the model’s responses.
(3). Different types of stimuli tend to cause errors at specific stages — perception, intent reasoning, and safety judgement — in the response process of MLLMs.
These findings highlight the need for refined safety mechanisms that balance caution with contextually appropriate responses, improving the reliability of MLLMs in real-world applications.

## item_id: m_2761

TITLE: Vitruvion: A Generative Model of Parametric CAD Sketches

ABSTRACT: Parametric computer-aided design (CAD) tools are the predominant way that engineers specify physical structures, from bicycle pedals to airplanes to printed circuit boards. The key characteristic of parametric CAD is that design intent is encoded not only via geometric primitives, but also by parameterized constraints between the elements. This relational specification can be viewed as the construction of a constraint program, allowing edits to coherently propagate to other parts of the design. Machine learning offers the intriguing possibility of accelerating the design process via generative modeling of these structures, enabling new tools such as autocompletion, constraint inference, and conditional synthesis. In this work, we present such an approach to generative modeling of parametric CAD sketches, which constitute the basic computational building blocks of modern mechanical design. Our model, trained on real-world designs from the SketchGraphs dataset, autoregressively synthesizes sketches as sequences of primitives, with initial coordinates, and constraints that reference back to the sampled primitives. As samples from the model match the constraint graph representation used in standard CAD software, they may be directly imported, solved, and edited according to downstream design tasks. In addition, we condition the model on various contexts, including partial sketches (primers) and images of hand-drawn sketches. Evaluation of the proposed approach demonstrates its ability to synthesize realistic CAD sketches and its potential to aid the mechanical design workflow.

## item_id: m_2762

TITLE: Enhancing Attention with Explicit Phrasal Alignments

ABSTRACT: The attention mechanism is an indispensable component of any state-of-the-art neural machine translation system. However, existing attention methods are often token-based and ignore the importance of phrasal alignments, which are the backbone of phrase-based statistical machine translation. We propose a novel phrase-based attention method to model n-grams of tokens as the basic attention entities, and design multi-headed phrasal attentions within the Transformer architecture to perform token-to-token and token-to-phrase mappings. Our approach yields improvements in English-German, English-Russian and English-French translation tasks on the standard WMT'14 test set. Furthermore, our phrasal attention method shows improvements on the one-billion-word language modeling benchmark.


## item_id: m_2763

TITLE: A Unified Framework for Convolution-based Graph Neural Networks

ABSTRACT: Graph Convolutional Networks (GCNs) have attracted a lot of research interest in the machine learning community in recent years. Although many variants have been proposed, we still lack a systematic view of different GCN models and deep understanding of the relations among them. In this paper, we take a step forward to establish a unified framework for convolution-based graph neural networks, by formulating the basic graph convolution operation as an optimization problem in the graph Fourier space. Under this framework, a variety of popular GCN models, including the vanilla-GCNs, attention-based GCNs and topology-based GCNs, can be interpreted as a same optimization problem but with different carefully designed regularizers. This novel perspective enables a better understanding of the similarities and differences among many widely used GCNs, and may inspire new approaches for designing better models. As a showcase, we also present a novel regularization technique under the proposed framework to tackle the oversmoothing problem in graph convolution. The effectiveness of the newly designed model is validated empirically.

## item_id: m_2764

TITLE: Domain Generalization Deep Graph Transformation

ABSTRACT: Graph transformation that predicts graph transition from one mode to another is an important and common problem. Despite much recent progress in developing advanced graph transformation techniques, the fundamental assumption typically required in machine-learning models that the testing and training data preserve the same distribution does not always hold. As a result, domain generalization graph transformation that predicts graphs not available in the training data is under-explored, with multiple key challenges to be addressed including (1) the extreme space complexity when training on all input-output mode combinations, (2) difference of graph topologies between the input and the output modes, and (3) how to generalize the model to target domains that are not in the training data. To fill the gap, we propose a multi-input, multi-output, hypernetwork-based graph neural network (MultiHyperGNN) that employs a encoder and a decoder to encode both input and output modes and semi-supervised link prediction to enhance the graph transformation task. Instead of training on all mode combinations, MultiHyperGNN preserves a constant space and polynomial computational complexity with the encoder and the decoder produced by two novel hypernetworks. Comprehensive experiments show that MultiHyperGNN has a superior performance than competing models in both prediction and domain generalization tasks.

## item_id: m_2765

TITLE: Improving Generalizability of Protein Sequence Models via Data Augmentations

ABSTRACT: While protein sequence data is an emerging application domain for machine learning methods, small modifications to protein sequences can result in difficult-to-predict changes to the protein's function. Consequently, protein machine learning models typically do not use randomized data augmentation procedures analogous to those used in computer vision or natural language, e.g., cropping or synonym substitution. In this paper, we empirically explore a set of simple string manipulations, which we use to augment protein sequence data when fine-tuning semi-supervised protein models. We provide 276 different comparisons to the Tasks Assessing Protein Embeddings (TAPE) baseline models, with Transformer-based models and training datasets that vary from the baseline methods only in the data augmentations and representation learning procedure. For each TAPE validation task, we demonstrate improvements to the baseline scores when the learned protein representation is fixed between tasks.  We also show that contrastive learning fine-tuning methods typically outperform masked-token prediction in these models, with increasing amounts of data augmentation generally improving performance for contrastive learning protein methods.  We find the most consistent results across TAPE tasks when using domain-motivated transformations, such as amino acid replacement, as well as restricting the Transformer attention to randomly sampled sub-regions of the protein sequence.  In rarer cases, we even find that information-destroying augmentations, such as randomly shuffling entire protein sequences, can improve downstream performance. 

## item_id: m_2766

TITLE: Provable Convergence and Global Optimality  of Generative Adversarial Network

ABSTRACT: Generative adversarial networks (GANs) train implicit generative models through solving minimax problems. Such minimax problems are known as nonconvex- nonconcave, for which the dynamics of first-order methods are not well understood. In this paper, we consider GANs in the type of the integral probability metrics (IPMs) with the generator represented by an overparametrized neural network. When the discriminator is solved to approximate optimality in each iteration, we prove that stochastic gradient descent on a regularized IPM objective converges globally to a stationary point with a sublinear rate. Moreover, we prove that when the width of the generator network is sufficiently large and the discriminator function class has enough discriminative ability, the obtained stationary point corresponds to a generator that yields a distribution that is close to the distribution of the observed data in terms of the total variation. To the best of our knowledge, we seem to first establish both the global convergence and global optimality of training GANs when the generator is parametrized by a neural network.

## item_id: m_2767

TITLE: Inference of Evolving Mental States from Irregular Action Events to Understand Human Behaviors

ABSTRACT: Inference of latent human mental processes, such as belief, intention, or desire, is crucial for developing AI with human-like intelligence, enabling more effective and timely collaboration. In this paper, we introduce a versatile encoder-decoder model designed to infer  evolving mental processes based on irregularly observed action events and predict future occurrences. The primary challenges arise from two factors: both actions and mental processes are irregular events, and the observed action data is often limited. To address the irregularity of these events, we leverage a temporal point process model within the encoder-decoder framework, effectively capturing the dynamics of both action and mental events. Additionally, we implement a backtracking mechanism in the decoder to enhance the accuracy of predicting future actions and evolving mental states. To tackle the issue of limited data, our model incorporates logic rules as priors, enabling accurate inferences from just a few observed samples. These logic rules can be refined and updated as needed, providing flexibility to the model. Overall, our approach enhances the understanding of human behavior by predicting when actions will occur and how mental processes evolve. Experiments on both synthetic and real-world datasets demonstrate the strong performance of our model in inferring mental states and predicting future actions, contributing to the development of more human-centric AI systems.

## item_id: m_2768

TITLE: Learning to navigate by distilling visual information and natural language instructions

ABSTRACT: In this work, we focus on the problem of grounding language by training an agent
to follow a set of natural language instructions and navigate to a target object
in a 2D grid environment. The agent receives visual information through raw
pixels and a natural language instruction telling what task needs to be achieved.
Other than these two sources of information, our model does not have any prior
information of both the visual and textual modalities and is end-to-end trainable.
We develop an attention mechanism for multi-modal fusion of visual and textual
modalities that allows the agent to learn to complete the navigation tasks and also
achieve language grounding. Our experimental results show that our attention
mechanism outperforms the existing multi-modal fusion mechanisms proposed in
order to solve the above mentioned navigation task. We demonstrate through the
visualization of attention weights that our model learns to correlate attributes of
the object referred in the instruction with visual representations and also show
that the learnt textual representations are semantically meaningful as they follow
vector arithmetic and are also consistent enough to induce translation between instructions
in different natural languages. We also show that our model generalizes
effectively to unseen scenarios and exhibit zero-shot generalization capabilities.
In order to simulate the above described challenges, we introduce a new 2D environment
for an agent to jointly learn visual and textual modalities

## item_id: m_2769

TITLE: Learning De-biased Representations with Biased Representations

ABSTRACT: Many machine learning algorithms are trained and evaluated by splitting data from a single source into training and test sets. While such focus on in-distribution learning scenarios has led interesting advances, it has not been able to tell if models are relying on dataset biases as shortcuts for successful prediction (e.g., using snow cues for recognising snowmobiles). Such biased models fail to generalise when the bias shifts to a different class. The cross-bias generalisation problem has been addressed by de-biasing training data through augmentation or re-sampling, which are often prohibitive due to the data collection cost (e.g., collecting images of snowmobile on a desert) and the difficulty of quantifying or expressing biases in the first place. In this work, we propose a novel framework to train a de-biased representation by encouraging it to be different from a set of representations that are biased by design. This tactic is feasible in many scenarios where it is much easier to define a set of biased representations than to define and quantify bias. Our experiments and analyses show that our method discourages models from taking bias shortcuts, resulting in improved performances on de-biased test data.

## item_id: m_2770

TITLE: Towards better understanding of gradient-based attribution methods for Deep Neural Networks

ABSTRACT: Understanding the flow of information in Deep Neural Networks (DNNs) is a challenging problem that has gain increasing attention over the last few years. While several methods have been proposed to explain network predictions, there have been only a few attempts to compare them from a theoretical perspective. What is more, no exhaustive empirical comparison has been performed in the past. In this work we analyze four gradient-based attribution methods and formally prove conditions of equivalence and approximation between them. By reformulating two of these methods, we construct a unified framework which enables a direct comparison, as well as an easier implementation. Finally, we propose a novel evaluation metric, called Sensitivity-n and test the gradient-based attribution methods alongside with a simple perturbation-based attribution method on several datasets in the domains of image and text classification, using various network architectures.

## item_id: m_2771

TITLE: Symmetry-Breaking Convergence Analysis of Certain Two-layered Neural Networks with ReLU nonlinearity

ABSTRACT: In this paper, we use dynamical system to analyze the nonlinear weight dynamics of two-layered bias-free networks in the form of $g(x; w) = \sum_{j=1}^K \sigma(w_j \cdot x)$, where $\sigma(\cdot)$ is ReLU nonlinearity. We assume that the input $x$ follow Gaussian distribution. The network is trained using gradient descent to mimic the output of a teacher network of the same size with fixed parameters $w*$ using $l_2$ loss. We first show that when $K = 1$, the nonlinear dynamics can be written in close form, and converges to $w*$ with at least $(1-\epsilon)/2$ probability, if random weight initializations of proper standard derivation ($\sim 1/\sqrt{d}$) is used, verifying empirical practice. For networks with many ReLU nodes ($K \ge 2$), we apply our close form dynamics and prove that when the teacher parameters $\{w*_j\}_{j=1}^K$ forms orthonormal bases, (1) a symmetric weight initialization yields a convergence to a saddle point and (2) a certain symmetry-breaking weight initialization yields global convergence to $w*$ without local minima. To our knowledge, this is the first proof that shows global convergence in nonlinear neural network without unrealistic assumptions on the independence of ReLU activations. In addition, we also give a concise gradient update formulation for a multilayer ReLU network when it follows a teacher of the same size with $l_2$ loss. Simulations verify our theoretical analysis.

## item_id: m_2772

TITLE: Advancing Portfolio Optimization: Hybrid Relaxation and Heuristic Approaches for Cardinality-Constrained MIQP Problems

ABSTRACT: The growing magnitude of investments in global markets has intensified the need for sophisticated risk mitigation strategies in portfolio optimization. Traditional portfolio optimization models that seek to minimize risk for a specified return frequently incorporate cardinality constraints, rendering them as Mixed-Integer Quadratic Programming (MIQP) challenges. These constraints elevate the problem to NP-Hard status, complicating the solution process. While heuristic methods have historically been favored for their direct approach to MIQP problems, relaxation techniques offer a strategic alternative by simplifying MIQP into a more tractable Quadratic Programming (QP) problem. We first introduce an approach that facilitates the conversion of MIQP to QP by relaxing integer constraints into continuous domains and integrating integer conditions into the objective function using Lagrange multipliers. This dual application not only eases the computational burden but preserves the integrity of the original problem's structure. An innovative diagonalization technique applied to the covariance matrix further refines our method, enhancing the fit for integer variables, as Lagrange multipliers are inherently biased towards continuous variables. We present a comparative analysis of three distinct models, Linear, Dual, and Diagonal, each employing a unique relaxation strategy. Our research evaluates their efficacy in addressing the MIQP problem under cardinality constraints. In conjunction with heuristic methods, the refined solutions from our exact relaxation models serve as a starting point for further refinement using Genetic Algorithm and Neighborhood Searching Algorithm. This hybrid methodology yields results that not only rival but occasionally surpass those achieved by the latest models and the commercial solver CPLEX. Our findings endorse the potential of combining exact and heuristic techniques in portfolio optimization, marking a significant advancement in the field.

## item_id: m_2773

TITLE: Layer-adaptive Sparsity for the Magnitude-based Pruning

ABSTRACT: Recent discoveries on neural network pruning reveal that, with a carefully chosen layerwise sparsity, a simple magnitude-based pruning achieves state-of-the-art tradeoff between sparsity and performance. However, without a clear consensus on ``how to choose,'' the layerwise sparsities are mostly selected algorithm-by-algorithm, often resorting to handcrafted heuristics or an extensive hyperparameter search. To fill this gap, we propose a novel importance score for global pruning, coined layer-adaptive magnitude-based pruning (LAMP) score; the score is a rescaled version of weight magnitude that incorporates the model-level $\ell_2$ distortion incurred by pruning, and does not require any hyperparameter tuning or heavy computation.
Under various image classification setups, LAMP consistently outperforms popular existing schemes for layerwise sparsity selection.
Furthermore, we observe that LAMP continues to outperform baselines even in weight-rewinding setups, while the connectivity-oriented layerwise sparsity (the strongest baseline overall) performs worse than a simple global magnitude-based pruning in this case. Code: https://github.com/jaeho-lee/layer-adaptive-sparsity

## item_id: m_2774

TITLE: VoxGenesis: Unsupervised Discovery of Latent Speaker Manifold for Speech Synthesis

ABSTRACT: Achieving nuanced and accurate emulation of human voice has been a longstanding goal in artificial intelligence. Although significant progress has been made in recent years, the mainstream of speech synthesis models still relies on supervised speaker modeling and explicit reference utterances. However, there are many aspects of human voice, such as emotion, intonation, and speaking style, for which it is hard to obtain accurate labels.
In this paper, we propose VoxGenesis, a novel unsupervised speech synthesis framework that can discover a latent speaker manifold and meaningful voice editing directions without supervision. VoxGenesis is conceptually simple. Instead of mapping speech features to waveforms deterministically, VoxGenesis transforms a Gaussian distribution into speech distributions conditioned and aligned by semantic tokens. This forces the model to learn a speaker distribution disentangled from the semantic content.
During the inference, sampling from the Gaussian distribution enables the creation of novel speakers with distinct characteristics. More importantly, the exploration of latent space uncovers human-interpretable directions associated with specific speaker characteristics such as gender attributes, pitch, tone, and emotion, allowing for voice editing by manipulating the latent codes along these identified directions.
We conduct extensive experiments to evaluate the proposed VoxGenesis using both subjective and objective metrics, finding that it produces significantly more diverse and realistic speakers with distinct characteristics than the previous approaches. We also show that  latent space manipulation produces consistent and human-identifiable effects that are not detrimental to the speech quality, which was not possible with previous approaches.
Finally, we demonstrate that VoxGenesis can also be used in voice conversion and multi-speaker TTS, outperforming the state-of-the-art approaches. Audio samples of VoxGenesis can be found at: \url{https://bit.ly/VoxGenesis}.

## item_id: m_2775

TITLE: Cheap Talk Discovery and Utilization in Multi-Agent Reinforcement Learning

ABSTRACT: By enabling agents to communicate, recent cooperative multi-agent reinforcement learning (MARL) methods have demonstrated better task performance and more coordinated behavior. Most existing approaches facilitate inter-agent communication by allowing agents to send messages to each other through free communication channels, i.e., \emph{cheap talk channels}. Current methods require these channels to be constantly accessible and known to the agents a priori. In this work, we lift these requirements such that the agents must discover the cheap talk channels and learn how to use them. Hence, the problem has two main parts: \emph{cheap talk discovery} (CTD) and \emph{cheap talk utilization} (CTU). We introduce a novel conceptual framework for both parts and develop a new algorithm based on mutual information maximization that outperforms existing algorithms in CTD/CTU settings. We also release a novel benchmark suite to stimulate future research in CTD/CTU.

## item_id: m_2776

TITLE: A Split-Client Approach to Second-Order Optimization

ABSTRACT: Second-order methods promise faster convergence but are rarely used in practice because Hessian computations and decompositions are significantly more expensive than gradient computations. We propose a \emph{split-client} framework where gradients and curvature are computed asynchronously by separate clients. This abstraction captures realistic delays and inexact Hessian updates while avoiding the manual tuning required by Lazy Hessian methods. Focusing on cubic regularization, we show that our approach retains strong convergence guarantees and achieves a provable wall-clock speedup of order $\sqrt{\tau}$, where $\tau$ is the relative time needed to compute and decompose the Hessian compared to a gradient step. Since $\tau$ can be orders of magnitude larger than one in high-dimensional problems, this improvement is practically significant.  Empirical results on convex and nonconvex problems confirm that the asynchronous method achieves faster wall-clock convergence while naturally satisfying the bounded-delay and inexactness assumptions.

## item_id: m_2777

TITLE: Large Language Models Can Design Game-Theoretic Objectives for Multi-Agent Planning

ABSTRACT: Game theory is a powerful paradigm to describe the interplay between participants in interactive multi-agent scenarios, and relies on the knowledge of player objectives or payoff structures for game optimal decision making. However, designing such objectives for games is challenging as it requires evaluating the impact of an agent’s actions on the behavior of others, and understanding the effect of changes in one's policy on the behavior of others. Indeed, aligning objective representations with a desired multi-agent behavior is achieved via tedious and impractical heuristics or human trial-and-error. This work aims to ease this process and proposes a multi-agent planning architecture that relies on a large language model (LLM) as the game formulation designer. First, we exhibit the zero-shot proficiency of the more capable LLMs (such as GPT-4) in tuning continuous objective function parameters in accordance with a specified high-level goal for autonomous driving examples. We then develop a planner which uses an LLM as a matrix game designer, for scenarios with discrete and finite action spaces. Given a scene history, the actions available to each agent, and high-level objectives (expressed in natural language), the LLM evaluates the payoffs associated with each combination of actions. From the game structure obtained, agents execute Nash optimal actions, the scene is re-evaluated, and the process is repeated. We evaluate our approach on a heterogeneous robot planning task inspired by wildlife conservation, as well as a household multi-humanoid transport task, and show the superiority of our LLM-based approach to other baselines

## item_id: m_2778

TITLE: Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction

ABSTRACT: Learning on graphs has attracted significant attention in the learning community due to numerous real-world applications. In particular, graph neural networks (GNNs), which take \emph{numerical} node features and graph structure as inputs, have been shown to achieve state-of-the-art performance on various graph-related learning tasks. Recent works exploring the correlation between numerical node features and graph structure via self-supervised learning have paved the way for further performance improvements of GNNs. However, methods used for extracting numerical node features from \emph{raw data} are still \emph{graph-agnostic} within standard GNN pipelines. This practice is sub-optimal as it prevents one from fully utilizing potential correlations between graph topology and node attributes. To mitigate this issue, we propose a new self-supervised learning framework, Graph Information Aided Node feature exTraction (GIANT). GIANT makes use of the eXtreme Multi-label Classification (XMC) formalism, which is crucial for fine-tuning the language model based on graph information, and scales to large datasets. We also provide a theoretical analysis that justifies the use of XMC over link prediction and motivates integrating XR-Transformers, a powerful method for solving XMC problems, into the GIANT framework. We demonstrate the superior performance of GIANT over the standard GNN pipeline on Open Graph Benchmark datasets: For example, we improve the accuracy of the top-ranked method GAMLP from $68.25\%$ to $69.67\%$, SGC from $63.29\%$ to $66.10\%$ and MLP from $47.24\%$ to $61.10\%$ on the ogbn-papers100M dataset by leveraging GIANT.

## item_id: m_2779

TITLE: How Do Vision Transformers Work?

ABSTRACT: The success of multi-head self-attentions (MSAs) for computer vision is now indisputable. However, little is known about how MSAs work. We present fundamental explanations to help better understand the nature of MSAs. In particular, we demonstrate the following properties of MSAs and Vision Transformers (ViTs): (1) MSAs improve not only accuracy but also generalization by flattening the loss landscapes. Such improvement is primarily attributable to their data specificity, not long-range dependency. On the other hand, ViTs suffer from non-convex losses. Large datasets and loss landscape smoothing methods alleviate this problem; (2) MSAs and Convs exhibit opposite behaviors. For example, MSAs are low-pass filters, but Convs are high-pass filters. Therefore, MSAs and Convs are complementary; (3) Multi-stage neural networks behave like a series connection of small individual models. In addition, MSAs at the end of a stage play a key role in prediction. Based on these insights, we propose AlterNet, a model in which Conv blocks at the end of a stage are replaced with MSA blocks. AlterNet outperforms CNNs not only in large data regimes but also in small data regimes. The code is available at https://github.com/xxxnell/how-do-vits-work.

## item_id: m_2780

TITLE: On the importance of single directions for generalization

ABSTRACT: Despite their ability to memorize large datasets, deep neural networks often achieve good generalization performance. However, the differences between the learned solutions of networks which generalize and those which do not remain unclear. Additionally, the tuning properties of single directions (defined as the activation of a single unit or some linear combination of units in response to some input) have been highlighted, but their importance has not been evaluated. Here, we connect these lines of inquiry to demonstrate that a network’s reliance on single directions is a good predictor of its generalization performance, across networks trained on datasets with different fractions of corrupted labels, across ensembles of networks trained on datasets with unmodified labels, across different hyper- parameters, and over the course of training. While dropout only regularizes this quantity up to a point, batch normalization implicitly discourages single direction reliance, in part by decreasing the class selectivity of individual units. Finally, we find that class selectivity is a poor predictor of task importance, suggesting not only that networks which generalize well minimize their dependence on individual units by reducing their selectivity, but also that individually selective units may not be necessary for strong network performance.

## item_id: m_2781

TITLE: Harnessing Text to Image Diffusion for Dense Prediction Tasks

ABSTRACT: Equipped with large-scale training data, text-to-image diffusion models have demonstrated the capacity to generate high-quality images that semantically correspond to the given textual descriptions. 
These compelling results imply that visual semantic knowledge has been effectively encapsulated within the generative diffusion model. 
The prospect of utilizing this embedded knowledge as a prior for down-stream vision tasks presents an intriguing avenue for exploration, which remains notably under-investigated. In this work, we demonstrate that when provided with appropriate image tags as textual descriptions, the implicit knowledge within these text-to-image diffusion models can be effectively leveraged for visual dense prediction tasks. Initially, we discover that supplying ground-truth semantic labels as textual instructions significantly enhances performance due to the extracted high-quality visual knowledge. Motivated by this observation, when presented with noisy tagging labels, we propose an adapter module attempting to derive relevant semantic information.
Subsequently, we propose a multi-label classification learning objective which further enriches the semantic quality of tags, thereby amplifying the efficacy of knowledge extraction.  We conduct extensive experiments four benchmarks, which suggest that the proposed approach is effective to unlock the representational capabilities of text-to-image diffusion models, showcasing a promising avenue for advancing dense prediction tasks in visual domains.

## item_id: m_2782

TITLE: Multiscale Neural Operator: Learning Fast and Grid-independent PDE Solvers

ABSTRACT: Numerical simulations in climate, chemistry, or astrophysics are computationally too expensive for uncertainty quantification or parameter-exploration at high-resolution. Reduced-order or surrogate models are multiple orders of magnitude faster, but traditional surrogates are inflexible or inaccurate and pure machine learning (ML)-based surrogates too data-hungry. We propose a hybrid, flexible surrogate model that exploits known physics for simulating large-scale dynamics and limits learning to the hard-to-model term, which is called parametrization or closure and captures the effect of fine- onto large-scale dynamics. Leveraging neural operators, we are the first to learn grid-independent, non-local, and flexible parametrizations. Our \textit{multiscale neural operator} is motivated by a rich literature in multiscale modeling, has quasilinear runtime complexity, is more accurate or flexible than state-of-the-art parametrizations and demonstrated on the chaotic equation multiscale Lorenz96.

## item_id: m_2783

TITLE: GRAPH TRANSFORMATION POLICY NETWORK FOR CHEMICAL REACTION PREDICTION

ABSTRACT: We address a fundamental problem in chemistry known as chemical reaction product prediction. Our main insight is that the input reactant and reagent molecules can be jointly represented as a graph, and the process of generating product molecules from reactant molecules can be formulated as a sequence of graph transformations. To this end, we propose Graph Transformation Policy Network (GTPN) - a novel generic method that combines the strengths of graph neural networks and reinforcement learning to learn the reactions directly from data with minimal chemical knowledge. Compared to previous methods, GTPN has some appealing properties such as: end-to-end learning, and making no assumption about the length or the order of graph transformations. In order to guide model search through the complex discrete space of sets of bond changes effectively, we extend the standard policy gradient loss by adding useful constraints. Evaluation results show that GTPN improves the top-1 accuracy over the current state-of-the-art method by about 3% on the large USPTO dataset. Our model's performances and prediction errors are also analyzed carefully in the paper.

## item_id: m_2784

TITLE: FlowBench: A Robustness Benchmark for Optical Flow Estimation

ABSTRACT: Optical flow estimation is a crucial computer vision task often applied to safety-critical real-world scenarios like autonomous driving and medical imaging.
While optical flow estimation accuracy has greatly benefited from the emergence of deep learning, learning-based methods are also known for their lack of generalization and reliability.
However, reliability is paramount when optical flow methods are employed in the real world, where safety is essential.
Furthermore, a deeper understanding of the robustness and reliability of learning-based optical flow estimation methods is still lacking, hindering the research community from building methods safe for real-world deployment.
Thus we propose **FlowBench**, a robustness benchmark and evaluation tool for learning-based optical flow methods. 
**FlowBench** facilitates streamlined research into the reliability of optical flow methods by benchmarking their robustness to adversarial attacks and out-of-distribution samples.
With **FlowBench**, we benchmark 91 methods across 3 different datasets under 7 diverse adversarial attacks and 23 established common corruptions, making it the most comprehensive robustness analysis of optical flow methods to date.
Across this wide range of methods, we consistently find that methods with state-of-the-art performance on established standard benchmarks lack reliability and generalization ability.
Moreover, we find interesting correlations between the performance, reliability, and generalization ability of optical flow estimation methods, under various lenses such as design choices used, number of parameters, etc.
After acceptance, **FlowBench** will be open-source and publicly available, including the weights of all tested models.

## item_id: m_2785

TITLE: FastFill: Efficient Compatible Model Update

ABSTRACT: In many retrieval systems the original high dimensional data (e.g., images) is mapped to a lower dimensional feature through a learned embedding model. The task of retrieving the most similar data from a gallery set to a given query data is performed through similarity comparison on features. When the embedding model is updated, it might produce features that are not comparable/compatible with features already in the gallery computed with the old model. Subsequently, all features in the gallery need to be re-computed using the new embedding model -- a computationally expensive process called backfilling. Recently, compatible representation learning methods have been proposed to avoid back-filling. Despite their relative success, there is an inherent trade-off between new model performance and its compatibility with the old model. In this work, we introduce FastFill: a compatible model update process using feature alignment and policy based partial backfilling to promptly elevate retrieval performance. We show that previous backfilling strategies suffer from decreased performance and demonstrate the importance of both the training objective and the ordering in online partial backfilling. We propose a new training method for feature alignment between old and new embedding models using uncertainty estimation. Compared to previous works, we obtain significantly improved backfilling results on a variety of datasets: mAP on ImageNet (+4.4%), Places-365 (+2.7%), and VGG-Face2 (+1.3%). Further, we demonstrate that when updating a biased model with FastFill, the minority subgroup accuracy gap promptly vanishes with a small fraction of partial backfilling.

## item_id: m_2786

TITLE: Frequency-Guided Masking for Enhanced Vision Self-Supervised Learning

ABSTRACT: We present a novel frequency-based Self-Supervised Learning (SSL) approach that significantly enhances its efficacy for pre-training. Prior work in this direction masks out pre-defined frequencies in the input image and employs a reconstruction loss to pre-train the model. While achieving promising results, such an implementation has two fundamental limitations as identified in our paper. First, using pre-defined frequencies overlooks the variability of image frequency responses. Second, pre-trained with frequency-filtered images, the resulting model needs relatively more data to adapt to naturally looking images during fine-tuning. To address these drawbacks, we propose FOurier transform compression with seLf-Knowledge distillation (FOLK), integrating two dedicated ideas. First, inspired by image compression, we adaptively select the masked-out frequencies based on image frequency responses, creating more suitable SSL tasks for pre-training. Second, we employ a two-branch framework empowered by knowledge distillation, enabling the model to take both the filtered and original images as input, largely reducing the burden of downstream tasks. Our experimental results demonstrate the effectiveness of FOLK in achieving competitive performance to many state-of-the-art SSL methods across various downstream tasks, including image classification, few-shot learning, and semantic segmentation.

## item_id: m_2787

TITLE: ChatSR: Conversational Symbolic Regression

ABSTRACT: Formulas are the language of communication between humans and nature. It is an important research topic of artificial intelligence to find expressions from observed data to reflect the relationship between each variable in the data, which is called a symbolic regression problem. The existing symbolic regression methods directly generate expressions according to the given observation data, but we cannot require the algorithm to generate expressions that meet specific requirements according to the known prior knowledge. For example, the expression needs to contain the symbol `$\sin$' or be periodicity, and so on. Even if it can, it often requires very complex operations, which is very inconvenient. In this paper, based on multi-modal large language models, we propose ChatSR, a conversational symbolic regression method that can generate expressions that meet the requirements simply by describing the requirements with natural language instructions. By experimenting on the test datasets, we can demonstrate that ChatSR leads the state-of-the-art baselines in fitting performance. More notably, ChatSR can well understand the prior knowledge contained in natural language prompts, and can further improve the quality of generated expressions according to the prior knowledge. In addition, it is exciting that ChatSR has good zero-shot capability.

## item_id: m_2788

TITLE: THINK VISUALLY: QUESTION ANSWERING THROUGH VIRTUAL IMAGERY

ABSTRACT: In this paper, we study the problem of visual reasoning in the context of textual question answering. We introduce Dynamic Spatial Memory Networks (DSMN), a new deep network architecture that specializes in answering questions that admit latent visual representations, and learns to generate and reason over such representations. Further, we propose two synthetic benchmarks, HouseQA and ShapeIntersection, to evaluate the visual reasoning capability of textual QA systems. Experimental results validate the effectiveness of our proposed DSMN for visual reasoning tasks.

## item_id: m_2789

TITLE: Auxiliary Guided Autoregressive Variational Autoencoders

ABSTRACT: Generative modeling of high-dimensional data is a key problem in machine learning. Successful approaches include latent variable models and autoregressive models. The complementary strengths of these approaches,  to model global and local image statistics respectively, suggest hybrid models combining the strengths of both models. Our contribution is to train such hybrid models using an auxiliary loss function that controls which information is captured by the latent variables and what is left to the autoregressive decoder. In contrast, prior work on such hybrid models needed to limit the capacity of the autoregressive decoder to prevent degenerate models that ignore the latent variables and only rely on autoregressive modeling. Our approach results in models with meaningful latent variable representations, and which rely on powerful autoregressive decoders to model image details. Our model generates qualitatively convincing samples, and yields state-of-the-art quantitative results.

## item_id: m_2790

TITLE: Random Feature Attention

ABSTRACT: Transformers are state-of-the-art models for a variety of sequence modeling tasks. At their core is an attention function which models pairwise interactions between the inputs at every timestep. While attention is powerful, it does not scale efficiently to long sequences due to its quadratic time and space complexity in the sequence length. We propose RFA, a linear time and space attention that uses random feature methods to approximate the softmax function, and explore its application in transformers. RFA can be used as a drop-in replacement for conventional softmax attention and offers a straightforward way of learning with recency bias through an optional gating mechanism. Experiments on language modeling and machine translation demonstrate that RFA achieves similar or better performance compared to strong transformer baselines. In the machine translation experiment, RFA decodes twice as fast as a vanilla transformer. Compared to existing efficient transformer variants, RFA is competitive in terms of both accuracy and efficiency on three long text classification datasets. Our analysis shows that RFA’s efficiency gains are especially notable on long sequences, suggesting that RFA will be particularly useful in tasks that require working with large inputs, fast decoding speed, or low memory footprints.

## item_id: m_2791

TITLE: Deep Metric Tensor Regularized Policy Gradient

ABSTRACT: In this paper, we propose a novel policy gradient algorithm for deep reinforcement learning. Unlike previous approaches, we focus on leveraging the Hessian trace information in the policy parametric space to enhance the performance of trained policy networks. Specifically, we introduce a metric tensor field that transforms the policy parametric space into a general Riemannian manifold. We further develop mathematical tools, deep learning algorithms, and metric tensor deep neural networks (DNNs) to learn a desirable metric tensor field, with the aim to achieve close-to-zero divergence on the policy gradient vector field of the Riemannian manifold. As an important regularization mechanism, zero divergence nullifies the principal differential components of the loss function used for training policy networks. It is expected to improve the effectiveness and sample efficiency of the policy network training process. Experimental results on multiple benchmark reinforcement learning problems demonstrate the advantages of our metric tensor regularized algorithms over the non-regularized counterparts. Moreover, our empirical analysis reveals that the trained metric tensor DNN can effectively reduce the absolute divergence towards zero on the Riemannian manifold.

## item_id: m_2792

TITLE: Individual/Joint Deblurring and Low-Light Image Enhancement in One Go via Unsupervised Deblurring Paradigm

ABSTRACT: Image restoration and enhancement, e.g., image deblurring, deraining and low-light image enhancement (LLIE), aim to improve the visual quality according to the corrupted/low-quality observation. Deep learning-based methods have achieved remarkable results on these individual tasks, but it is still hard to tackle them together. While some attempts have been made to implement joint task processing, they inevitably lead to higher data cost and higher training cost. Moreover, these attempts are strictly limited by the data distribution, i.e., the distribution of the inference data is required to be as close as possible to the training data, otherwise the data cannot be used for inference. In this paper, we take the LLIE and deblurring task as the subjects of this study in an attempt to seek a novel solution to the joint task processing problem. Specifically, we tackle this kind of problem in an extraordinary manner, i.e., \textit{Individual/Joint \underline{D}eblurring and Low-Light Image \underline{E}nhancement in One Go \underline{v}ia \underline{U}nsupervised \underline{D}eblurring \underline{P}aradigm (DEvUDP)}, which integrates the noise self-regression and could avoid the limitations of aforementioned attempts. More specifically, a novel architecture with a transformation branch and a self-regression branch is elaborated, which only accepts unpaired blurry-sharp data as input to train the model; in this way, the pre-trained model can be surprisingly applied to both LLIE, deblurring and mixed degradation processing. Besides, we can choose to highlight perceptual performance or distortion performance of the model by configuring different components to the architecture. Extensive experiments have demonstrate the superiority of the method on different widely-used datasets.

## item_id: m_2793

TITLE: Diving into Optimization of Topology in Neural Networks

ABSTRACT: Seeking effective networks has become one of the most crucial and practical areas in deep learning. The architecture of a neural network can be represented as a directed acyclic graph, whose nodes denote transformation of layers and edges represent information flow. Despite the selection of \textit{micro} node operations, \textit{macro} connections among the whole network, noted as \textit{topology}, largely affects the optimization process. We first rethink the residual connections via a new \textit{topological view} and observe the benefits provided by dense connections to the optimization. Motivated by which, we propose an innovation method to optimize the topology of a neural network. The optimization space is defined as a complete graph, through assigning learnable weights which reflect the importance of connections, the optimization of topology is transformed into learning a set of  continuous variables of edges. To extend the optimization to larger search spaces, a new series of networks,
named as TopoNet, are designed. To further focus on critical edges and promote generalization ablity in dense topologies, auxiliary sparsity constraint is adopted to constrain the distribution of edges. Experiments on classical networks prove the effectiveness of the optimization of topology. Experiments with TopoNets further verify both availability and transferability of the proposed method in
different tasks e.g. image classification, object detection and face recognition.

## item_id: m_2794

TITLE: One Vertex Attack on Graph Neural Networks-based Spatiotemporal Forecasting

ABSTRACT: Spatiotemporal forecasting plays an essential role in intelligent transportation systems (ITS) and numerous applications, such as route planning, navigation, and automatic driving. Deep Spatiotemporal Graph Neural Networks, which capture both spatial and temporal patterns, have achieved great success in traffic forecasting applications. Though Deep Neural Networks (DNNs) have been proven to be vulnerable to carefully designed perturbations in multiple domains like objection classification and graph classification, these adversarial works cannot be directly applied to spatiotemporal GNNs because of their causality and spatiotemporal mechanism. There is still a lack of studies on the vulnerability and robustness of spatiotemporal GNNs. Particularly, if spatiotemporal GNNs are vulnerable in real-world traffic applications, a hacker can easily cause serious traffic congestion and even a city-scale breakdown. To fill this gap, we design One Vertex Attack to break deep spatiotemporal GNNs by attacking a single one vertex. To achieve this, we apply the genetic algorithm with a universal attack method as the evaluation function to locate the weakest vertex; then perturbations are generated by solving an optimization problem with the inverse estimation. Empirical studies prove that perturbations in one vertex can be diffused into most of the graph when spatiotemporal GNNs are under One Vertex Attack.

## item_id: m_2795

TITLE: Structured Adversarial Attack:  Towards General Implementation and Better Interpretability

ABSTRACT: When generating adversarial examples to attack deep neural networks (DNNs), Lp norm of the added perturbation is usually used to measure the similarity between original image and adversarial example. However, such adversarial attacks perturbing the raw input spaces may fail to capture structural information hidden in the input.   This work develops a more general attack model,  i.e., the structured attack (StrAttack),  which explores group sparsity in adversarial perturbation by sliding a mask through images aiming for extracting key spatial structures.  An ADMM (alternating direction method of multipliers)-based framework is proposed that can split the original problem into a sequence of analytically solvable subproblems and can be generalized to implement other attacking methods. Strong group sparsity is achieved in adversarial perturbations even with the same level of Lp-norm distortion (p∈ {1,2,∞}) as the state-of-the-art attacks. We demonstrate the effectiveness of StrAttack by extensive experimental results on MNIST, CIFAR-10 and ImageNet. We also show that StrAttack provides better interpretability (i.e., better correspondence with discriminative image regions) through adversarial saliency map (Paper-not et al., 2016b) and class activation map (Zhou et al., 2016).

## item_id: m_2796

TITLE: Transformer-XH: Multi-Evidence Reasoning with eXtra Hop Attention

ABSTRACT: Transformers have achieved new heights modeling natural language as a sequence of text tokens. However, in many real world scenarios, textual data inherently exhibits structures beyond a linear sequence such as trees and graphs; many tasks require reasoning with evidence scattered across multiple pieces of texts. This paper presents Transformer-XH, which uses eXtra Hop attention to enable intrinsic modeling of structured texts in a fully data-driven way. Its new attention mechanism naturally “hops” across the connected text sequences in addition to attending over tokens within each sequence. Thus, Transformer-XH better conducts joint multi-evidence reasoning by propagating information between documents and constructing global contextualized representations. On multi-hop question answering, Transformer-XH leads to a simpler multi-hop QA system which outperforms previous state-of-the-art on the HotpotQA FullWiki setting. On FEVER fact verification, applying Transformer-XH provides state-of-the-art accuracy and excels on claims whose verification requires multiple evidence.

## item_id: m_2797

TITLE: Towards Deep Interpretability (MUS-ROVER II): Learning Hierarchical Representations of Tonal Music

ABSTRACT: Music theory studies the regularity of patterns in music to capture concepts underlying music styles and composers' decisions. This paper continues the study of building \emph{automatic theorists} (rovers) to learn and represent music concepts that lead to human interpretable knowledge and further lead to materials for educating people. Our previous work took a first step in algorithmic concept learning of tonal music, studying high-level representations (concepts) of symbolic music (scores) and extracting interpretable rules for composition. This paper further studies the representation \emph{hierarchy} through the learning process, and supports \emph{adaptive} 2D memory selection in the resulting language model. This leads to a deeper-level interpretability that expands from individual rules to a dynamic system of rules, making the entire rule learning process more cognitive. The outcome is a new rover, MUS-ROVER \RN{2}, trained on Bach's chorales, which outputs customizable syllabi for learning compositional rules. We demonstrate comparable results to our music pedagogy, while also presenting the differences and variations. In addition, we point out the rover's potential usages in style recognition and synthesis, as well as applications beyond music.

## item_id: m_2798

TITLE: Sparse Communication via Mixed Distributions

ABSTRACT: Neural networks and other machine learning models compute continuous representations, while humans communicate mostly through discrete symbols. Reconciling these two forms of communication is desirable for generating human-readable interpretations or learning discrete latent variable models, while maintaining end-to-end differentiability. Some existing approaches (such as the Gumbel-Softmax transformation) build continuous relaxations that are discrete approximations in the zero-temperature limit, while others (such as sparsemax transformations and the Hard Concrete distribution) produce discrete/continuous hybrids. In this paper, we build rigorous theoretical foundations for these hybrids, which we call "mixed random variables.'' Our starting point is a new "direct sum'' base measure defined on the face lattice of the probability simplex. From this measure, we introduce new entropy and Kullback-Leibler divergence functions that subsume the discrete and differential cases and have interpretations in terms of code optimality. Our framework suggests two strategies for representing and sampling mixed random variables, an extrinsic ("sample-and-project'’) and an intrinsic one (based on face stratification). We experiment with both approaches on an  emergent communication benchmark and on modeling MNIST and Fashion-MNIST data with variational auto-encoders with mixed latent variables.

## item_id: m_2799

TITLE: Meta Koopman Decomposition for Time Series Forecasting Under Distribution Shifts

ABSTRACT: Time series forecasting facilitates various real-world applications and has attracted great research interests. In real-world scenarios, time series forecasting models confront a fundamental issue of temporal distribution shifts, i.e., the statistical properties of time series are evolving over time. In this paper, we utilize Koopman theory to address temporal distribution shifts (TDS). Koopman theory states any time series can be mapped into a Koopman space by proper measurement functions and represented by infinite dimensional linear Koopman operator. Therefore, time series under different distributions can be modeled by different Koopman operators. Considering the linearity of Koopman operators, the Koopman operators for representing time series under different distributions can be decomposed as linear combination of a set of Koopman operators, which we termed as meta Koopman operators. We further theoretically show the infinite dimensional Koopman operators can be approximated by finite matrix multiplications and the meta Koopman operators are equivalent to a set of matrices. Based on the analysis, we propose an auto-encoder framework for implementing the meta Koopman decomposition of time series, which is theoretically able to handle TDS. Extensive experiments conducted on four real-world time series datasets demonstrate the superiority of the proposed model on tackling temporal distribution shifts.

## item_id: m_2800

TITLE: Neural-Guided Symbolic Regression with Asymptotic Constraints

ABSTRACT: Symbolic regression is a type of discrete optimization problem that involves searching expressions that fit given data points. In many cases, other mathematical constraints about the unknown expression not only provide more information beyond just values at some inputs, but also effectively constrain the search space. We identify the asymptotic constraints of leading polynomial powers as the function approaches 0 and infinity as useful constraints and create a system to use them for symbolic regression. The first part of the system is a conditional expression generating neural network which preferentially generates expressions with the desired leading powers, producing novel expressions outside the training domain. The second part, which we call Neural-Guided Monte Carlo Tree Search, uses the network during a search to find an expression that conforms to a set of data points and desired leading powers. Lastly, we provide an extensive experimental validation on thousands of target expressions showing the efficacy of our system compared to exiting methods for finding unknown functions outside of the training set.
