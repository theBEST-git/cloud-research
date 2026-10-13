# Batch 11 — 100 items

## item_id: m_1001

TITLE: ZerOmics: Toward General Models for Single-Cell Analysis with Instruction Tuning

ABSTRACT: A variety of analysis tasks in single-cell (SC) multi-omics are crucial for precision medicine and clinical research. To address these tasks, existing methods are typically pre-trained on large-scale datasets to obtain general representations, followed by fine-tuning on specific tasks and labeled datasets. However, their task-specific heads often lack generalizability, significantly limiting performance in zero-shot scenarios. Inspired by the success of large language models (LLMs), we propose ZerOmics, the first zero-shot method that guides LLMs to perform various SC tasks without relying on specific downstream data. To enable LLMs to establish a correct and comprehensive understanding of SC data, ZerOmics employs a dual-alignment strategy. Specifically, ZerOmics aligns SC expression data with the well-organized gene corpus, thereby generating robust SC embeddings. These embeddings are then incorporated into instructions designed for various SC analysis tasks to tune the LLM, achieving alignment between SC data and the LLM. Extensive experiments across various sequencing technologies and tissues demonstrate that ZerOmics provides a comprehensive and general solution for SC analysis, achieving performance comparable to or even surpassing the state-of-the-art (SOTA) supervised and fine-tuned methods.

## item_id: m_1002

TITLE: Forget Forgetting: Continual Learning in a World of Abundant Memory

ABSTRACT: Continual learning (CL) has traditionally focused on minimizing exemplar memory, a constraint often misaligned with modern systems where GPU time, not storage, is the primary bottleneck. This paper challenges this paradigm by investigating a more realistic regime: one where memory is abundant enough to mitigate forgetting, but full retraining from scratch remains prohibitively expensive. In this practical "middle ground", we find that the core challenge shifts from stability to plasticity, as models become biased toward prior tasks and struggle to learn new ones. Conversely, improved stability allows simple replay baselines to outperform the state-of-the-art methods at a fraction of the GPU cost. To address this newly surfaced trade-off, we propose Weight Space Consolidation, a lightweight method that combines (1) rank-based parameter resets to restore plasticity with (2) weight averaging to enhance stability. Validated on both class-incremental learning with image classifiers and continual instruction tuning with large language models, our approach outperforms strong baselines while matching the low computational cost of replay, offering a scalable alternative to expensive full-retraining. These findings challenge long-standing CL assumptions and establish a new, cost-efficient baseline for real-world CL systems where exemplar memory is no longer the limiting factor.

## item_id: m_1003

TITLE: Learning Independent Causal Mechanisms

ABSTRACT: Independent causal mechanisms are a central concept in the study of causality
with implications for machine learning tasks. In this work we develop
an algorithm to recover a set of (inverse) independent mechanisms relating
a distribution transformed by the mechanisms to a reference distribution.
The approach is fully unsupervised and based on a set of experts that compete
for data to specialize and extract the mechanisms. We test and analyze
the proposed method on a series of experiments based on image transformations.
Each expert successfully maps a subset of the transformed data
to the original domain, and the learned mechanisms generalize to other
domains. We discuss implications for domain transfer and links to recent
trends in generative modeling.

## item_id: m_1004

TITLE: Efficiently Troubleshooting Image Segmentation Models with Human-In-The-Loop

ABSTRACT: Image segmentation lays the foundation for many high-stakes vision applications such as autonomous driving and medical image analysis. It is, therefore, of great importance to not only improve the accuracy of segmentation models on well-established benchmarks, but also enhance their robustness in the real world so as to avoid sparse but fatal failures. In this paper, instead of chasing state-of-the-art performance on existing benchmarks, we turn our attention to a new challenging problem: how to efficiently expose failures of ``top-performing'' segmentation models in the real world and how to leverage such counterexamples to rectify the models. To achieve this with minimal human labelling effort, we first automatically sample a small set of images that are likely to falsify the target model from a large corpus of web images via the maximum discrepancy competition principle. We then propose a weakly labelling strategy to further reduce the number of false positives, before time-consuming pixel-level labelling by humans. Finally, we fine-tune the model to harness the identified failures, and repeat the whole process, resulting in an efficient and progressive framework for troubleshooting segmentation models. We demonstrate the feasibility of our framework using the semantic segmentation task in PASCAL VOC, and find that the fine-tuned model exhibits significantly improved generalization when applied to real-world images with greater content diversity. All experimental codes will be publicly released upon acceptance.

## item_id: m_1005

TITLE: TopoStreamer: Temporal Lane Segment Topology Reasoning in Autonomous Driving

ABSTRACT: Lane segment topology reasoning constructs a comprehensive road network by capturing the topological relationships between lane segments and their semantic types. This enables end-to-end autonomous driving systems to perform road-dependent maneuvers such as turning and lane changing. However, the limitations in consistent positional embedding and temporal multiple attribute learning in existing methods hinder accurate roadnet reconstruction. To address these issues, we propose TopoStreamer, an end-to-end temporal perception model for lane segment topology reasoning. Specifically, TopoStreamer introduces three key improvements: streaming attribute constraints, dynamic lane boundary positional encoding, and lane segment denoising. The streaming attribute constraints enforce temporal consistency in both centerline and boundary coordinates, along with their classifications. Meanwhile, dynamic lane boundary positional encoding enhances the learning of up-to-date positional information within queries, while lane segment denoising helps capture diverse lane segment patterns, ultimately improving model performance. Additionally, we assess the accuracy of existing models using a lane boundary classification metric, which serves as a crucial measure for lane-changing scenarios in autonomous driving. On the OpenLane-V2 dataset, TopoStreamer demonstrates considerable improvements over state-of-the-art methods, achieving substantial performance gains of +3.0 mAP in lane segment perception and +1.7 OLS in centerline perception tasks. Our code will be released.

## item_id: m_1006

TITLE: A Simple and Scalable Shape Representation for 3D Reconstruction

ABSTRACT: Deep learning applied to the reconstruction of 3D shapes has seen growing interest. A popular approach to 3D reconstruction and generation in recent years has been the CNN decoder-encoder model often applied in voxel space. However this often scales very poorly with the resolution limiting the effectiveness of these models. Several sophisticated alternatives for decoding to 3D shapes have been proposed typically relying on alternative deep learning architectures. We show however in this work that standard benchmarks in 3D reconstruction can be tackled with a surprisingly simple approach: a linear decoder obtained by principal component analysis on the signed distance transform of the surface. This approach allows easily scaling to larger resolutions. We show in multiple experiments it is competitive with state of the art methods and also allows the decoder to be fine-tuned on the target task using a loss designed for SDF transforms, obtaining further gains.    

## item_id: m_1007

TITLE: Learning Locality and Isotropy in Dialogue Modeling

ABSTRACT: Existing dialogue modeling methods have achieved promising performance on various dialogue tasks with the aid of Transformer and the large-scale pre-trained language models. However, some recent studies revealed that the context representations produced by these methods suffer the problem of anisotropy. In this paper, we find that the generated representations are also not conversational, losing the conversation structure information during the context modeling stage. To this end, we identify two properties in dialogue modeling, i.e., locality and isotropy, and present a simple method for dialogue representation calibration, namely SimDRC, to build isotropic and conversational feature spaces. Experimental results show that our approach significantly outperforms current state-of-the-art models on three open-domain dialogue tasks with eight benchmarks. More in-depth analyses further confirm the effectiveness of our proposed approach. We release the code at https://github.com/hahahawu/SimDRC.

## item_id: m_1008

TITLE: Biased Binary Attribute Classifiers Ignore the Majority Classes

ABSTRACT: To visualize the regions of interest that classifiers base their decisions on, different Class Activation Mapping (CAM) methods have been developed.
However, all of these techniques target categorical classifiers only, though most real-world tasks are binary classification.
In this paper, we extend gradient-based CAM techniques to work with binary classifiers and visualize the active regions for binary attribute classifiers.
When training an unbalanced binary classifier on a biased dataset, it is well-known that the majority class is mostly predicted much better than minority class.
In our experiments on the CelebA dataset, we verify these results, when training an unbalanced classifier to extract 40 facial attributes simultaneously.
One would expect that the biased classifier has learned to extract features mainly for the majority classes and that the proportional energy of the activations mainly reside in certain specific regions of the image where the attribute is located.
However, we find very little regular activation for samples of majority classes, while the active regions for minority classes seem mostly reasonable and overlap with our expectations.
These results suggest that biased classifiers only rely on bias activation for majority classes.
When training a balanced classifier on the unbalanced data by employing attribute-specific class weights, positive and negative classes are classified similarly well and show expected activations for almost all attributes.

## item_id: m_1009

TITLE: Learning Latent Representations in Neural Networks for Clustering through Pseudo Supervision and Graph-based Activity Regularization

ABSTRACT: In this paper, we propose a novel unsupervised clustering approach exploiting the hidden information that is indirectly introduced through a pseudo classification objective. Specifically, we randomly assign a pseudo parent-class label to each observation which is then modified by applying the domain specific transformation associated with the assigned label. Generated pseudo observation-label pairs are subsequently used to train a neural network with Auto-clustering Output Layer (ACOL) that introduces multiple softmax nodes for each pseudo parent-class. Due to the unsupervised objective based on Graph-based Activity Regularization (GAR) terms, softmax duplicates of each parent-class are specialized as the hidden information captured through the help of domain specific transformations is propagated during training. Ultimately we obtain a k-means friendly latent representation. Furthermore, we demonstrate how the chosen transformation type impacts performance and helps propagate the latent information that is useful in revealing unknown clusters. Our results show state-of-the-art performance for unsupervised clustering tasks on MNIST, SVHN and USPS datasets, with the highest accuracies reported to date in the literature.

## item_id: m_1010

TITLE: Conditional MAE: An Empirical Study of Multiple Masking in Masked Autoencoder

ABSTRACT: This work aims to study the subtle yet often overlooked element of masked autoencoder (MAE): masking. While masking plays a critical role in the performance of MAE, most current research employs fixed masking strategies directly on the input image. We introduce a masked autoencoder framework with multiple masking stages, termed Conditional MAE, where subsequent maskings are conditioned on previous unmasked representations, enabling a more flexible masking process in masked image modeling. By doing so, our study sheds light on how multiple masking affects the optimization in training and performance of pretrained models, e.g., introducing more locality to models, and summarizes several takeaways from our findings. Finally, we empirically evaluate the performance of our best-performing model (Conditional-MAE) with that of MAE in three folds including transfer learning, robustness, and scalability, demonstrating the effectiveness of our multiple masking strategy. We hope our findings will inspire further research in the field and code will be made available.

## item_id: m_1011

TITLE: Semi-supervised deep learning by metric embedding

ABSTRACT: Deep networks are successfully used as classification models yielding state-of-the-art results when trained on a large number of labeled samples. These models, however, are usually much less suited for semi-supervised problems because of their tendency to overfit easily when trained on small amounts of data. In this work we will explore a new training objective that is targeting a semi-supervised regime with only a small subset of labeled data. This criterion is based on a deep metric embedding over distance relations within the set of labeled samples, together with constraints over the embeddings of the unlabeled set. The final learned representations are discriminative in euclidean space, and hence can be used with subsequent nearest-neighbor classification using the labeled samples.

## item_id: m_1012

TITLE: Pruning Convolutional Neural Networks for Resource Efficient Inference

ABSTRACT: We propose a new formulation for pruning convolutional kernels in neural networks to enable efficient inference. We interleave greedy criteria-based pruning with fine-tuning by backpropagation-a computationally efficient procedure that maintains good generalization in the pruned network. We propose a new criterion based on Taylor expansion that approximates the change in the cost function induced by pruning network parameters. We focus on transfer learning, where large pretrained networks are adapted to specialized tasks. The proposed criterion demonstrates superior performance compared to other criteria, e.g. the norm of kernel weights or feature map activation, for pruning large CNNs after adaptation to fine-grained classification tasks (Birds-200 and Flowers-102) relaying only on the first order gradient information. We also show that pruning can lead to more than 10x theoretical reduction in adapted 3D-convolutional filters with a small drop in accuracy in a recurrent gesture classifier. Finally, we show results for the large-scale ImageNet dataset to emphasize the flexibility of our approach.

## item_id: m_1013

TITLE: Early Stop And Adversarial Training Yield Better surrogate Model: Very Non-Robust Features Harm Adversarial Transferability

ABSTRACT: The transferability of adversarial examples (AE); known as adversarial transferability, has attracted significant attention because it can be exploited for TransferableBlack-box Attacks (TBA). Most lines of works attribute the existence of the non-robust features improves the adversarial transferability. As a motivating example, we test the adversarial transferability on the early stopped surrogate models, which are known to be concentrated on robust features than non-robust features from prior works. We find that the early stopped models yield better adversarial transferability than the models at the final epoch, which leaves non-intuitive interpretation from the perspective of the robust and non-robust features (NRFs).  In this work, we articulate a novel Very Non-Robust Feature(VNRF) hypothesis that the VNRFslearned can harm the adversarial transferability to explain this phenomenon. This hypothesis is partly verified through zeroing some filters with highl1norm values. This insight further motivates us to adopt light adversarial training that mainly removes the VNRFs for significantly improving the transferability.

## item_id: m_1014

TITLE: Collaborative Filtering With A Synthetic Feedback Loop

ABSTRACT: We propose a novel learning framework for recommendation systems, assisting collaborative filtering with a synthetic feedback loop. The proposed framework consists of a ``recommender'' and a ``virtual user.'' The recommender is formulizd as a collaborative-filtering method, recommending items according to observed user behavior.  The virtual user estimates rewards from the recommended items and generates the influence of the rewards on observed user behavior.  The recommender connected with the virtual user constructs a closed loop, that recommends users with items and imitates the unobserved feedback of the users to the recommended items. The synthetic feedback is used to augment observed user behavior and improve recommendation results.  Such a model can be interpreted as the inverse reinforcement learning, which can be learned effectively via rollout (simulation). Experimental results show that the proposed framework is able to boost the performance of existing collaborative filtering methods on multiple datasets. 

## item_id: m_1015

TITLE: Learning Explainable Models Using Attribution Priors

ABSTRACT: Two important topics in deep learning both involve incorporating humans into the modeling process: Model priors transfer information from humans to a model by regularizing the model's parameters; Model attributions transfer information from a model to humans by explaining the model's behavior. Previous work has taken important steps to connect these topics through various forms of gradient regularization. We find, however, that existing methods that use attributions to align a model's behavior with human intuition are ineffective. We develop an efficient and theoretically grounded feature attribution method, expected gradients, and a novel framework, attribution priors, to enforce prior expectations about a model's behavior during training. We demonstrate that attribution priors are broadly applicable by instantiating them on three different types of data: image data, gene expression data, and health care data. Our experiments show that models trained with attribution priors are more intuitive and achieve better generalization performance than both equivalent baselines and existing methods to regularize model behavior.

## item_id: m_1016

TITLE: Towards shutdownable agents: stochastic choice in unseen gridworlds via DReST rewards

ABSTRACT: Misaligned artificial agents might resist shutdown. The POST-Agents Proposal (PAP) is an idea for ensuring that does not happen. The PAP recommends training agents with a novel reward function: Discounted Reward for Same-Length Trajectories (DReST). This DReST reward function penalizes agents for repeatedly choosing same-length trajectories. It thereby incentivizes agents to (1) choose stochastically between different trajectory-lengths (be 'NEUTRAL' about trajectory-lengths), and (2) pursue goals effectively conditional on each trajectory-length (be 'USEFUL'). In this paper, we use a DReST reward function to train deep RL agents to be NEUTRAL and USEFUL in hundreds of gridworlds. We find that these DReST agents generalize to being NEUTRAL and USEFUL in unseen gridworlds at test time. Indeed, DReST agents achieve 11\% (PPO) and 18\% (A2C) higher USEFULNESS on our test set than agents trained with a more conventional reward function. Our results provide some early evidence that DReST reward functions could be used to train more advanced agents to be USEFUL and NEUTRAL. Theoretical work suggests that these agents would be useful and shutdownable.

## item_id: m_1017

TITLE: Inverted Activations: Reducing Memory Footprint in Neural Network Training

ABSTRACT: The scaling of neural networks with increasing data and model sizes necessitates the development of more efficient deep learning algorithms. 
    A significant challenge in neural network training is the memory footprint associated with activation tensors, particularly in pointwise nonlinearity layers that traditionally save the entire input tensor for the backward pass, leading to substantial memory consumption.
    
    In this paper, we propose a modification to the handling of activation tensors in pointwise nonlinearity layers. 
    Our method involves saving the output tensor instead of the input tensor during the forward pass. Since the subsequent layer typically also saves its input tensor, this approach reduces the total memory required by storing only one tensor between layers instead of two. This optimization is especially beneficial for transformer-based architectures like GPT, BERT, Mistral, and Llama.

    To enable this approach, we utilize the inverse function of the nonlinearity during the backward pass. As the inverse cannot be computed analytically for most nonlinearities, we construct accurate approximations using simpler functions. 
    Experimental results demonstrate that our method significantly reduces memory usage without affecting training accuracy or computational performance.

    Our implementation is provided as a drop-in replacement for standard nonlinearity layers in the PyTorch framework, facilitating easy adoption without requiring architectural modifications. The code is available at \url{https://github.com/removed/for/anonimity}.

## item_id: m_1018

TITLE: Graph Convolutional Memory using Topological Priors

ABSTRACT: Solving partially-observable Markov decision processes (POMDPs) is critical when applying reinforcement learning to real-world problems, where agents have an incomplete view of the world. We present graph convolutional memory (GCM), the first hybrid memory model for solving POMDPs using reinforcement learning. GCM uses either human-defined or data-driven topological priors to form graph neighborhoods, combining them into a larger network topology using dynamic programming. We query the graph using graph convolution, coalescing relevant memories into a context-dependent belief. When used without human priors, GCM performs similarly to state-of-the-art methods. When used with human priors, GCM outperforms these methods on a variety of tasks while using significantly fewer parameters.

## item_id: m_1019

TITLE: Network Signatures from Image Representation of Adjacency Matrices: Deep/Transfer Learning for Subgraph Classification

ABSTRACT: We propose a novel subgraph image representation for classification of network fragments with the target being their parent networks. The graph image representation is based on 2D image embeddings of adjacency matrices. We use this image representation in two modes. First, as the input to a machine learning algorithm. Second, as the input to a pure transfer learner. Our conclusions from multiple datasets are that
1. deep learning using structured image features performs the best compared to graph kernel and classical features based methods; and,
2. pure transfer learning works effectively with minimum interference from the user and is robust against small data.


## item_id: m_1020

TITLE: Gray-Box Gaussian Processes for Automated Reinforcement Learning

ABSTRACT: Despite having achieved spectacular milestones in an array of important real-world applications, most Reinforcement Learning (RL) methods are very brittle concerning their hyperparameters. Notwithstanding the crucial importance of setting the hyperparameters in training state-of-the-art agents, the task of hyperparameter optimization (HPO) in RL is understudied. In this paper, we propose a novel gray-box Bayesian Optimization technique for HPO in RL, that enriches Gaussian Processes with reward curve estimations based on generalized logistic functions. In a very large-scale experimental protocol, comprising 5 popular RL methods (DDPG, A2C, PPO, SAC, TD3), dozens of environments (Atari, Mujoco), and 7 HPO baselines, we demonstrate that our method significantly outperforms current HPO practices in RL.

## item_id: m_1021

TITLE: Resolving label uncertainty with implicit generative models

ABSTRACT: In prediction problems, coarse and imprecise sources of input can provide rich information about labels, but are not readily used by discriminative learners. In this work, we propose a method for jointly inferring labels across a collection of data samples, where each sample consists of an observation and a prior belief about the label. By implicitly assuming the existence of a generative model for which a differentiable predictor is the posterior, we derive a training objective that allows learning under weak beliefs. This formulation unifies various machine learning settings: the weak beliefs can come in the form of noisy or incomplete labels, likelihoods given by a different prediction mechanism on auxiliary input, or common-sense priors reflecting knowledge about the structure of the problem at hand. We demonstrate the proposed algorithms on diverse problems: classification with negative training examples, learning from rankings, weakly and self-supervised aerial imagery segmentation, co-segmentation of video frames, and coarsely supervised text classification.

## item_id: m_1022

TITLE: Chess Game Concepts Emerge under Weak Supervision: A Case Study of Tic-tac-toe

ABSTRACT: This paper explores the possibility of learning chess game concepts under weak supervision with convolutional neural networks, which is a topic that has not been visited to the best of our knowledge. We put this task in three different backgrounds: (1) deep reinforcement learning has shown an amazing capability to learn a mapping from visual inputs to most rewarding actions, without knowing the concepts of a video game. But how could we confirm that the network understands these concepts or it just does not? (2) cross-modal supervision for visual representation learning draws much attention recently. Is this methodology still applicable when it comes to the domain of game concepts and actions? (3) class activation mapping is widely recognized as a visualization technique to help us understand what a network has learnt. Is it possible for it to activate at non-salient regions? With the simplest chess game tic-tac-toe, we report interesting results as answers to those three questions mentioned above. All codes, pre-processed datasets and pre-trained models will be released.

## item_id: m_1023

TITLE: Modeling Label Space Interactions in Multi-label Classification using Box Embeddings

ABSTRACT: Multi-label classification is a challenging structured prediction task in which a set of output class labels are predicted for each input. Real-world datasets often have natural or latent taxonomic relationships between labels, making it desirable for models to employ label representations capable of capturing such taxonomies. Most existing multi-label classification methods do not do so, resulting in label predictions that are inconsistent with the taxonomic constraints, thus failing to accurately represent the fundamentals of problem setting. In this work, we introduce the multi-label box model (MBM), a multi-label classification method that combines the encoding power of neural networks with the inductive bias and probabilistic semantics of box embeddings (Vilnis, et al 2018).  Box embeddings can be understood as trainable Venn-diagrams based on hyper-rectangles.  Representing labels by boxes rather than vectors, MBM is able to capture taxonomic relations among labels.  Furthermore, since box embeddings allow these relations to be learned by stochastic gradient descent from data, and to be read as calibrated conditional probabilities, our model is endowed with a high degree of interpretability. This interpretability also facilitates the injection of partial information about label-label relationships into model training, to further improve its consistency. We provide theoretical grounding for our method and show experimentally the model's ability to learn the true latent taxonomic structure from data. Through extensive empirical evaluations on both small and large-scale multi-label classification datasets, we show that BBM can significantly improve taxonomic consistency while preserving or surpassing the state-of-the-art predictive performance.

## item_id: m_1024

TITLE: Combating inherent noise for direct preference optimization

ABSTRACT: Direct Preference Optimization (DPO) has recently gained traction as a promising approach to align large models with human feedback. It is notable for its effectiveness and ease of application across various models, including Large Language Models (LLMs) and Diffusion Models (DMs). However, the quality of preference data used in DPO training has been largely overlooked. Current datasets, whether annotated by deep learning metrics or crowd-sourced human judgments, often contain noisy labels. This noise can adversely affect the performance of DPO. 
To address this issue, we propose a novel approach that incorporates a noise-aware metric into the DPO objective. This metric, which includes intra-annotator confidence and inter-annotator stability, helps identify and mitigate the impact of noisy data. We introduce an Adaptive-DPO loss function which improves the DPO loss in two ways: one aims to reduce the influence of noisy samples, while the other is to amplify the impact of clean samples. Our experiments demonstrate that this method effectively handles both synthetic and natural noisy data, leading to improved performance in visual and textual generation tasks. This underscores the practical value of our approach in enhancing model robustness amidst noisy preference data.

## item_id: m_1025

TITLE: CcGAN: Continuous Conditional Generative Adversarial Networks for Image Generation

ABSTRACT: This work proposes the continuous conditional generative adversarial network (CcGAN), the first generative model for image generation conditional on continuous, scalar conditions (termed regression labels). Existing conditional GANs (cGANs) are mainly designed for categorical conditions (e.g., class labels); conditioning on a continuous label is mathematically distinct and raises two fundamental problems: (P1) Since there may be very few (even zero) real images for some regression labels, minimizing existing empirical versions of cGAN losses (a.k.a. empirical cGAN losses) often fails in practice; (P2) Since regression labels are scalar and infinitely many, conventional label input methods (e.g., combining a hidden map of the generator/discriminator with a one-hot encoded label) are not applicable. The proposed CcGAN solves the above problems, respectively, by (S1) reformulating existing empirical cGAN losses to be appropriate for the continuous scenario; and (S2) proposing a novel method to incorporate regression labels into the generator and the discriminator. The reformulation in (S1) leads to two novel empirical discriminator losses, termed the hard vicinal discriminator loss (HVDL) and the soft vicinal discriminator loss (SVDL) respectively, and a novel empirical generator loss. The error bounds of a discriminator trained with HVDL and SVDL are derived under mild assumptions in this work. A new benchmark dataset, RC-49, is also proposed for generative image modeling conditional on regression labels. Our experiments on the Circular 2-D Gaussians, RC-49, and UTKFace datasets show that CcGAN is able to generate diverse, high-quality samples from the image distribution conditional on a given regression label. Moreover, in these experiments, CcGAN substantially outperforms cGAN both visually and quantitatively.

## item_id: m_1026

TITLE: A New, Physics-Based Continuous-Time Reinforcement Learning Algorithm with Performance Guarantees

ABSTRACT: We introduce a new, physics-based continuous-time reinforcement learning (CT-RL) algorithm for control of affine nonlinear systems, an area that enables a plethora of well-motivated applications. Based on fundamental input/output control mechanisms, our approach uses reference command input (RCI) as probing noise in learning. With known physical dynamics of the environment, and by leveraging on the Kleinman algorithm structure, our RCI-based CT-RL algorithm not only provides theoretical guarantees such as learning convergence, solution optimality, and closed-loop stability, but also well-behaved dynamic system responses with data efficiency during learning. Our results are therefore an advance from the two currently available classes of approaches to CT-RL. The first school of adaptive dynamic programming (ADP) methods features elegant theoretical results stemming from adaptive and optimal control. Yet, they have not been shown effectively synthesizing meaningful controllers. The second school of fitted value iteration (FVI) methods, also the state-of-the-art (SOTA) deep RL (DRL) design, has shown impressive learning solutions, yet theoretical guarantees are still to be developed. We provide several evaluations to demonstrate that our RCI-based design leads to new, SOTA CT-RL results.

## item_id: m_1027

TITLE: Feint in Multi-Player Games

ABSTRACT: This paper introduces the first formalization, implementation and quantitative evaluation of \feint in Multi-Player Games. Our work first formalizes \feint from the perspective of Multi-Player Games, in terms of the temporal, spatial and their collective impacts. The formalization is built upon \textit{Non-transitive Active Markov Game Model}, where \feint can have a considerable amount of impacts. Then, our work considers practical implementation details of \feint in Multi-Player Games, under the state-of-the-art progress of multi-agent modeling to date (namely Multi-Agent Reinforcement Learning). Finally, our work quantitatively examines the effectiveness of our design, and the results show that our design of Feint can (1) greatly improve the reward gains from the game; (2) significantly improve the diversity of Multi-Player Games; and (3) only incur negligible overheads in terms of time consumption. We conclude that our design of Feint is effective and practical, to make Multi-Player Games more interesting.

## item_id: m_1028

TITLE: Programming With a Differentiable Forth Interpreter

ABSTRACT: There are families of neural networks that can learn to compute any function, provided sufficient training data. However, given that in practice training data is scarce for all but a small set of problems, a core question is how to incorporate prior knowledge into a model. Here we consider the case of prior procedural knowledge, such as knowing the overall recursive structure of a sequence transduction program or the fact that a program will likely use arithmetic operations on real numbers to solve a task. To this end we present a differentiable interpreter for the programming language Forth. Through a neural implementation of the dual stack machine that underlies Forth, programmers can write program sketches with slots that can be filled with behaviour trained from program input-output data. As the program interpreter is end-to-end differentiable, we can optimize this behaviour directly through gradient descent techniques on user specified objectives, and also integrate the program into any larger neural computation graph. We show empirically that our interpreter is able to effectively leverage different levels of prior program structure and learn complex transduction tasks such as sequence sorting or addition with substantially less data and better generalisation over problem sizes. In addition, we introduce neural program optimisations based on symbolic computation and parallel branching that lead to significant speed improvements. 

## item_id: m_1029

TITLE: Rethinking Compressed Convolution Neural Network from a Statistical Perspective

ABSTRACT: Many designs have recently been proposed to improve the model efficiency of convolutional neural networks (CNNs) at a fixed resource budget, while there is a lack of theoretical analysis to justify them. This paper first formulates CNNs with high-order inputs into statistical models, which have a special "Tucker-like" formulation. This makes it possible to further conduct the sample complexity analysis to CNNs as well as compressed CNNs via tensor decomposition. Tucker and CP decompositions are commonly adopted to compress CNNs in the literature. The low rank assumption is usually imposed on the output channels, which according to our study, may not be beneficial to obtain a computationally efficient model while a similar accuracy can be maintained. Our finding is further supported by ablation studies on CIFAR10, SVNH and UCF101 datasets.

## item_id: m_1030

TITLE: Phase-Aware Speech Enhancement with Deep Complex U-Net

ABSTRACT: Most deep learning-based models for speech enhancement have mainly focused on estimating the magnitude of spectrogram while reusing the phase from noisy speech for reconstruction. This is due to the difficulty of estimating the phase of clean speech. To improve speech enhancement performance, we tackle the phase estimation problem in three ways. First, we propose Deep Complex U-Net, an advanced U-Net structured model incorporating well-defined complex-valued building blocks to deal with complex-valued spectrograms. Second, we propose a polar coordinate-wise complex-valued masking method to reflect the distribution of complex ideal ratio masks. Third, we define a novel loss function, weighted source-to-distortion ratio (wSDR) loss, which is designed to directly correlate with a quantitative evaluation measure. Our model was evaluated on a mixture of the Voice Bank corpus and DEMAND database, which has been widely used by many deep learning models for speech enhancement. Ablation experiments were conducted on the mixed dataset showing that all three proposed approaches are empirically valid. Experimental results show that the proposed method achieves state-of-the-art performance in all metrics, outperforming previous approaches by a large margin.

## item_id: m_1031

TITLE: SAFENet: A Secure, Accurate and Fast Neural Network Inference

ABSTRACT: The advances in neural networks have driven many companies to provide prediction services to users in a wide range of applications. However, current prediction systems raise privacy concerns regarding the user's private data. A cryptographic neural network inference service is an efficient way to allow two parties to execute neural network inference without revealing either party’s data or model. Nevertheless, existing cryptographic neural network inference services suffer from huge running latency; in particular, the latency of communication-expensive cryptographic activation function is 3 orders of magnitude higher than plaintext-domain activation function. And activations are the necessary components of the modern neural networks. Therefore, slow cryptographic activation has become the primary obstacle of efficient cryptographic inference. 

In this paper, we propose a new technique, called SAFENet, to enable a Secure, Accurate and Fast nEural Network inference service. To speedup secure inference and guarantee inference accuracy, SAFENet includes channel-wise activation approximation with multiple-degree options. This is implemented by keeping the most useful activation channels and replacing the remaining, less useful, channels with various-degree polynomials. SAFENet also supports mixed-precision activation approximation by automatically assigning different replacement ratios to various layer; further increasing the approximation ratio and reducing inference latency. Our experimental results show SAFENet obtains the state-of-the-art inference latency and performance, reducing latency by $38\% \sim 61\%$ or improving accuracy by $1.8\% \sim 4\%$ over prior techniques on various encrypted datasets.

## item_id: m_1032

TITLE: Rethinking Evaluation of Sparse Autoencoders through the Representation of Polysemous Words

ABSTRACT: Sparse autoencoders (SAEs) have gained a lot of attention as a promising tool to improve the interpretability of large language models (LLMs) by mapping the complex superposition of *polysemantic* neurons into *monosemantic* features and composing a sparse dictionary of words.

However, traditional performance metrics like Mean Squared Error and $\mathrm{L}_{0}$ sparsity ignore the evaluation of the semantic representational power of SAEs - whether they can acquire interpretable monosemantic features while preserving the semantic relationship of words.For instance, it is not obvious whether a learned sparse feature could distinguish different meanings in one word.

In this paper, we propose a suite of evaluations for SAEs to analyze the quality of monosemantic features by focusing on polysemous words.
Our findings reveal that SAEs developed to improve the MSE-$\mathrm{L}_0$ Pareto frontier may confuse interpretability, which does not necessarily enhance the extraction of monosemantic features.
The analysis of SAEs with polysemous words can also figure out the internal mechanism of LLMs; deeper layers and the Attention module contribute to distinguishing polysemy in a word.

Our semantics-focused evaluation offers new insights into the polysemy and the existing SAE objective and contributes to the development of more practical SAEs.

## item_id: m_1033

TITLE: Mitigating Bias in Natural Language Inference Using Adversarial Learning

ABSTRACT: Recognizing the relationship between two texts is an important aspect of natural language understanding (NLU), and a variety of neural network models have been proposed for solving NLU tasks. Unfortunately, recent work showed that the datasets these models are trained on often contain biases that allow models to achieve non-trivial performance without possibly learning the relationship between the two texts. We propose a framework for building robust models by using adversarial learning to encourage models to learn latent, bias-free representations. We test our approach in a Natural Language Inference (NLI) scenario, and show that our adversarially-trained models learn robust representations that ignore known dataset-specific biases. Our experiments demonstrate that our models are more robust to new NLI datasets. 

## item_id: m_1034

TITLE: Communication-Efficient and Drift-Robust Federated Learning via Elastic Net

ABSTRACT: Federated learning (FL) is a distributed method to train a global model over a set of local clients while keeping data localized, which reduces risks of privacy and security. FL framework faces important challenges including expensive communication cost and client drift problem. Leveraging the elastic net, we propose a communication-efficient and drift-robust FL framework to improve the communication efficiency and resolve the client drift problem. We repurpose two types of the elastic net regularizers (i.e., $\ell_1$ and $\ell_2$ penalties on the local model updates): (1) the $\ell_1$-norm regularizer sparsifies the local updates to enhance the communication efficiency and (2) the $\ell_2$-norm regularizer attempts to resolve the client drift problem by limiting the impact of drifting local updates due to data heterogeneity. Our framework is general; hence, it can be integrated with prior FL techniques, e.g., FedAvg, FedProx, SCAFFOLD, and FedDyn. We show that our framework effectively resolves the communication cost problem and the client drift problem simultaneously.

## item_id: m_1035

TITLE: MetaOptimize: A Framework for Optimizing Step Sizes and Other Meta-parameters

ABSTRACT: We address the challenge of optimizing meta-parameters (i.e., hyperparameters) in machine learning algorithms, a critical factor influencing training efficiency and model performance. Moving away from the computationally expensive traditional meta-parameter search methods, we introduce MetaOptimize framework that dynamically adjusts meta-parameters, particularly step sizes (also known as learning rates), during training. More specifically, MetaOptimize can wrap around any first-order optimization algorithm, tuning step sizes on the fly to minimize a specific form of regret that accounts for long-term effect of step sizes on training, through a discounted sum of future losses.  We also introduce low complexity variants of MetaOptimize that, in  conjunction with its adaptability to multiple optimization algorithms, demonstrate performance competitive to those of best hand-crafted learning-rate schedules across various machine learning applications.

## item_id: m_1036

TITLE: Cut-and-Paste Neural Rendering

ABSTRACT: Cut-and-paste methods take an object from one image and insert it into another.   Doing so often results in unrealistic looking images because the inserted object's shading is inconsistent with the target scene's shading. Existing reshading methods require a geometric and physical model of the inserted object, which is then rendered using environment parameters. Accurately constructing such a model only from a single image is beyond the current understanding of computer vision.

We describe an alternative procedure -- cut-and-paste neural rendering, to render the inserted fragment's shading field consistent with the target scene.  We use a Deep Image Prior (DIP) as a neural renderer trained to render an image with consistent image decomposition inferences.  The resulting rendering from DIP should have an albedo consistent with composite albedo; it should have a shading field that, outside the inserted fragment, is the same as the target scene's shading field; 
and composite surface normals are consistent with the final rendering's shading field. 
The result is a simple procedure that produces convincing and realistic shading. Moreover, our procedure does not require rendered images or image-decomposition from real images in the training or labeled annotations. In fact, our only use of simulated ground truth is our use of a pre-trained normal estimator. Qualitative results are strong, supported by a user study comparing against state-of-the-art image harmonization baseline.

## item_id: m_1037

TITLE: Partially Observed Trajectory Inference using Optimal Transport and a Dynamics Prior

ABSTRACT: Trajectory inference seeks to recover the temporal dynamics of a population from snapshots of its (uncoupled) temporal marginals, i.e. where observed particles are \emph{not} tracked over time. Prior works addressed this challenging problem under a stochastic differential equation (SDE) model with a gradient-driven drift in the observed space, introducing a minimum entropy estimator relative to the Wiener measure and a practical grid-free mean-field Langevin (MFL) algorithm using Schr\"odinger bridges. Motivated by the success of observable state space models in the traditional paired trajectory inference problem (e.g. target tracking), we extend the above framework to a class of latent SDEs in the form of \emph{observable state space models}.    
 In this setting, we use partial observations to infer trajectories in the latent space under a specified dynamics model (e.g. the constant velocity/acceleration models from target tracking). We introduce the PO-MFL algorithm to solve this latent trajectory inference problem and provide theoretical guarantees to the partially observed setting. Experiments validate the robustness of our method and the exponential convergence of the MFL dynamics, and demonstrate significant outperformance over the latent-free baseline in key scenarios.

## item_id: m_1038

TITLE: MonoFlow: A Unified Generative Modeling Framework for GAN Variants

ABSTRACT: Generative adversarial networks (GANs) play a minmax two-player game via adversarial training. The conventional understanding of adversarial training is that the discriminator is trained to estimate a divergence and the generator learns to minimize this divergence. We argue that despite the fact that many variants of GANs are developed following this paradigm, the existing theoretical understanding of GANs and the practical algorithms are inconsistent. In order to gain deeper theoretical insights and algorithmic inspiration for these GAN variants, we leverage Wasserstein gradient flows which characterize the evolution of particles in the sample space. Based on this, we introduce a unified generative modeling framework – MonoFlow: the particle evolution is rescaled via an arbitrary monotonically increasing mapping. Under our framework, adversarial training can be viewed as a procedure first obtaining MonoFlow's vector field via the discriminator and then the generator learns to parameterize the flow defined by the corresponding vector field. We also reveal the fundamental difference between variational divergence minimization and adversarial training. These analysis help us to identify what types of generator loss functions can lead to the successful training of GANs and suggest that GANs may have more loss designs beyond those developed in the literature, e.g., non-saturated loss, as long as they realize MonoFlow. Consistent empirical studies are also included to validate the effectiveness of our framework.

## item_id: m_1039

TITLE: Reachability Traces for Curriculum Design in Reinforcement Learning

ABSTRACT: The objective in goal-based reinforcement learning is to learn a policy to reach a particular goal state within the environment. However, the underlying reward function may be too sparse for the agent to efficiently learn useful behaviors. Recent studies have demonstrated that reward sparsity can be overcome by instead learning a curriculum of simpler subtasks. In this work, we design an agent's curriculum by focusing on the aspect of goal reachability, and introduce the idea of a reachability trace, which is used as a basis to determine a sequence of intermediate subgoals to guide the agent towards its primary goal. We discuss several properties of the trace function, and in addition, validate our proposed approach empirically in a range of environments, while comparing its performance against appropriate baselines.

## item_id: m_1040

TITLE: Efficient Causal Decision Making with One-sided Feedback

ABSTRACT: We study a class of decision-making problems with one-sided feedback, where outcomes are only observable for specific actions. A typical example is bank loans, where the repayment status is known only if a loan is approved and remains undefined if rejected. In such scenarios, conventional approaches to causal decision evaluation and learning from observational data are not directly applicable. In this paper, we introduce a novel value function to evaluate decision rules that addresses the issue of undefined counterfactual outcomes. Without assuming no unmeasured confounders, we establish the identification of the value function using shadow variables. Furthermore, leveraging semiparametric theory, we derive the efficiency bound for the proposed value function and develop efficient methods for decision evaluation and learning. Numerical experiments and a real-world data application demonstrate the empirical performance of our proposed methods.

## item_id: m_1041

TITLE: Learning to Understand: Incorporating Local Contexts with Global Attention for Sentiment Classification

ABSTRACT: Recurrent neural networks have shown their ability to construct sentence or paragraph representations. Variants such as LSTM overcome the problem of vanishing gradients to some degree, thus being able to model long-time dependency. Still, these recurrent based models lack the ability of capturing complex semantic compositions. To address this problem, we propose a model which can incorporate local contexts with the guide of global context attention. Both the local and global contexts are obtained through LSTM networks. The working procedure of this model is just like how we human beings read a text and then answer a related question. Empirical studies show that the proposed model can achieve state of the art on some benchmark datasets. Attention visualization also verifies our intuition. Meanwhile, this model does not need pretrained embeddings to get good results.

## item_id: m_1042

TITLE: DiffMove: Human Trajectory Recovery via Conditional Diffusion Model

ABSTRACT: Recovering human trajectories from incomplete or missing data is crucial for many mobility-based urban applications, e.g., urban planning, transportation, and location-based services. Existing methods mainly rely on recurrent neural networks or attention mechanisms. Though promising, they encounter limitations in capturing complex spatial-temporal dependencies in low-sampling trajectories. Recently, diffusion models show potential in content generation. However, most of proposed methods are used to generate contents in continuous numerical representations, which cannot be directly adapted to the human location trajectory recovery. In this paper, we introduce a conditional diffusion-based trajectory recovery method, namely, DiffMove. It first transforms locations in trajectories into the embedding space, in which the embedding denoising is performed, and then missing locations are recovered by an embedding decoder. DiffMove not only improves accuracy by introducing high-quality generative methods in the trajectory recovery, but also carefully models the transition, periodicity, and temporal patterns in human mobility. Extensive experiments based on two representative real-world mobility datasets are conducted, and the results show significant improvements (an average of 11% in recall) over the best baselines.

## item_id: m_1043

TITLE: Playing Nondeterministic Games through Planning with a Learned Model

ABSTRACT: The MuZero algorithm is known for achieving high-level performance on traditional zero-sum two-player games of perfect information such as chess, Go, and shogi, as well as visual, non-zero sum, single-player environments such as the Atari suite. Despite lacking a perfect simulator and employing a learned model of environmental dynamics,  MuZero produces game-playing agents comparable to its predecessor AlphaZero. However, the current implementation of MuZero is restricted only to deterministic environments. This paper presents Nondeterministic MuZero (NDMZ), an extension of MuZero for nondeterministic, two-player, zero-sum games of perfect information. Borrowing from Nondeterministic Monte Carlo Tree Search and the theory of extensive-form games, NDMZ formalizes chance as a player in the game and incorporates it into the MuZero network architecture and tree search. Experiments show that NDMZ is capable of learning effective strategies and an accurate model of the game.

## item_id: m_1044

TITLE: Multiplicative LSTM for sequence modelling

ABSTRACT: We introduce multiplicative LSTM (mLSTM), a novel recurrent neural network architecture for sequence modelling that combines the long short-term memory (LSTM) and multiplicative recurrent neural network architectures. mLSTM is characterised by its ability to have different recurrent transition functions for each possible input, which we argue makes it more expressive for autoregressive density estimation. We demonstrate empirically that mLSTM outperforms standard LSTM and its deep variants for a range of character level modelling tasks, and that this improvement increases with the complexity of the task. This model achieves a test error of 1.19 bits/character on the last 4 million characters of the Hutter prize dataset when combined with dynamic evaluation.

## item_id: m_1045

TITLE: Generative Adversarial Networks as Variational Training of Energy Based Models

ABSTRACT: In this paper, we study deep generative models for effective unsupervised learning. We propose VGAN, which works by minimizing a variational lower bound of the negative log likelihood (NLL) of an energy based model (EBM), where the model density $p(\mathbf{x})$ is approximated by a variational distribution $q(\mathbf{x})$ that is easy to sample from. The training of VGAN takes a two step procedure: given $p(\mathbf{x})$, $q(\mathbf{x})$ is updated to maximize the lower bound; $p(\mathbf{x})$ is then updated one step with samples drawn from $q(\mathbf{x})$ to decrease the lower bound. VGAN is inspired by the generative adversarial networks (GANs), where $p(\mathbf{x})$ corresponds to the discriminator and $q(\mathbf{x})$ corresponds to the generator, but with several notable differences. We hence name our model variational GANs (VGANs). VGAN provides a practical solution to training deep EBMs in high dimensional space, by eliminating the need of MCMC sampling. From this view, we are also able to identify causes to the difficulty of training GANs and propose viable solutions.

## item_id: m_1046

TITLE: Variational Recurrent Models for Solving Partially Observable Control Tasks

ABSTRACT: In partially observable (PO) environments, deep reinforcement learning (RL) agents often suffer from unsatisfactory performance, since two problems need to be tackled together: how to extract information from the raw observations to solve the task, and how to improve the policy. In this study, we propose an RL algorithm for solving PO tasks. Our method comprises two parts: a variational recurrent model (VRM) for modeling the environment, and an RL controller that has access to both the environment and the VRM. The proposed algorithm was tested in two types of PO robotic control tasks, those in which either coordinates or velocities were not observable and those that require long-term memorization. Our experiments show that the proposed algorithm achieved better data efficiency and/or learned more optimal policy than other alternative approaches in tasks in which unobserved states cannot be inferred from raw observations in a simple manner.

## item_id: m_1047

TITLE: NormSoftmax: Normalize the Input of Softmax to Accelerate and Stabilize Training

ABSTRACT: Softmax is a basic function that normalizes a vector to a probability distribution and is widely used in machine learning, most notably in cross-entropy loss function and dot product attention operations. However, optimization of softmax-based models is sensitive to the input statistics change. We observe that the input of softmax changes significantly during the initial training stage, causing slow and unstable convergence when training the model from scratch. To remedy the optimization difficulty of softmax, we propose a simple yet effective substitution, named NormSoftmax, where the input vector is first normalized to unit variance and then fed to the standard softmax function. Similar to other existing normalization layers in machine learning models, NormSoftmax can stabilize and accelerate the training process, and also increase the robustness of the training procedure against hyperparameters. Experiments on Transformer-based models and convolutional neural networks validate that our proposed NormSoftmax is an effective plug-and-play module to stabilize and speed up the optimization of neural networks with cross-entropy loss or dot-product attention operations.

## item_id: m_1048

TITLE: Generative Latent Flow

ABSTRACT: In this work, we propose the Generative Latent Flow (GLF), an algorithm for generative modeling of the data distribution. GLF uses an Auto-encoder (AE) to learn latent representations of the data, and a normalizing flow to map the distribution of the latent variables to that of simple i.i.d noise. In contrast to some other Auto-encoder based generative models, which use various regularizers that encourage the encoded latent distribution to match the prior distribution, our model explicitly constructs a mapping between these two distributions, leading to better density matching while avoiding over regularizing the latent variables. We compare our model with several related techniques, and show that it has many relative advantages including fast convergence, single stage training and minimal reconstruction trade-off. We also study the relationship between our model and its stochastic counterpart, and show that our model can be viewed as a vanishing noise limit of VAEs with flow prior.  Quantitatively, under standardized evaluations, our method achieves state-of-the-art sample quality and diversity among AE based models on commonly used datasets, and is competitive with GANs' benchmarks. 

## item_id: m_1049

TITLE: LanczosNet: Multi-Scale Deep Graph Convolutional Networks

ABSTRACT: We propose Lanczos network (LanczosNet) which uses the Lanczos algorithm to construct low rank approximations of the graph Laplacian for graph convolution.
Relying on the tridiagonal decomposition of the Lanczos algorithm, we not only efficiently exploit multi-scale information via fast approximated computation of matrix power but also design learnable spectral filters.
Being fully differentiable, LanczosNet facilitates both graph kernel learning as well as learning node embeddings. 
We show the connection between our LanczosNet and graph based manifold learning, especially diffusion maps.
We benchmark our model against $8$ recent deep graph networks on citation datasets and QM8 quantum chemistry dataset. 
Experimental results show that our model achieves the state-of-the-art performance in most tasks.

## item_id: m_1050

TITLE: A Synaptic Neural Network and Synapse Learning

ABSTRACT: A Synaptic Neural Network (SynaNN) consists of synapses and neurons. Inspired by the synapse research of neuroscience, we built a synapse model with a nonlinear synapse function of excitatory and inhibitory channel probabilities. Introduced the concept of surprisal space and constructed a commutative diagram, we proved that the inhibitory probability function -log(1-exp(-x)) in surprisal space is the topologically conjugate function of the inhibitory complementary probability 1-x in probability space. Furthermore, we found that the derivative of the synapse over the parameter in the surprisal space is equal to the negative Bose-Einstein distribution. In addition, we constructed a fully connected synapse graph (tensor) as a synapse block of a synaptic neural network. Moreover, we proved the gradient formula of a cross-entropy loss function over parameters, so synapse learning can work with the gradient descent and backpropagation algorithms. In the proof-of-concept experiment, we performed an MNIST training and testing on the MLP model with synapse network as hidden layers.

## item_id: m_1051

TITLE: Unsupervised Generative 3D Shape Learning from Natural Images

ABSTRACT: In this paper we present, to the best of our knowledge, the first method to learn a generative model of 3D shapes from natural images in a fully unsupervised way. For example, we do not use any ground truth 3D or 2D annotations, stereo video, and ego-motion during the training. Our approach follows the general strategy of Generative Adversarial Networks, where an image generator network learns to create image samples that are realistic enough to fool a discriminator network into believing that they are natural images. In contrast, in our approach the image gen- eration is split into 2 stages. In the first stage a generator network outputs 3D ob- jects. In the second, a differentiable renderer produces an image of the 3D object from a random viewpoint. The key observation is that a realistic 3D object should yield a realistic rendering from any plausible viewpoint. Thus, by randomizing the choice of the viewpoint our proposed training forces the generator network to learn an interpretable 3D representation disentangled from the viewpoint. In this work, a 3D representation consists of a triangle mesh and a texture map that is used to color the triangle surface by using the UV-mapping technique. We provide analysis of our learning approach, expose its ambiguities and show how to over- come them. Experimentally, we demonstrate that our method can learn realistic 3D shapes of faces by using only the natural images of the FFHQ dataset.

## item_id: m_1052

TITLE: DeepTwist: Learning Model Compression via Occasional Weight Distortion

ABSTRACT: Model compression has been introduced to reduce the required hardware resources while maintaining the model accuracy. Lots of techniques for model compression, such as pruning, quantization, and low-rank approximation, have been suggested along with different inference implementation characteristics. Adopting model compression is, however, still challenging because the design complexity of model compression is rapidly increasing due to additional hyper-parameters and computation overhead in order to achieve a high compression ratio. In this paper, we propose a simple and efficient model compression framework called DeepTwist which distorts weights in an occasional manner without modifying the underlying training algorithms. The ideas of designing weight distortion functions are intuitive and straightforward given formats of compressed weights. We show that our proposed framework improves compression rate significantly for pruning, quantization, and low-rank approximation techniques while the efforts of additional retraining and/or hyper-parameter search are highly reduced. Regularization effects of DeepTwist are also reported.

## item_id: m_1053

TITLE: Less is Not Worse: Effective Reasoning Without Complete Reasoning Traces

ABSTRACT: Large language models (LLMs) often produce lengthy reasoning traces with substantial token redundancy.
While reasoning processes are widely adopted to tune LLMs as a post-training regime, it has been underexplored whether LLMs truly learn from the complete trajectory, particularly in supervised fine-tuning (SFT). We argue that, for mid-size LLMs commonly trained with SFT for reasoning, using full reasoning trajectories may harm performance because their limited capacity increases susceptibility to redundant intermediate steps.
To investigate, we first analyze the redundancy in thinking trajectories through attention maps and controlled token-removal studies, both of which show that intermediate tokens contribute minimally to reasoning quality.
Our analyses suggest that the most redundant segments typically appear in the middle of reasoning traces, whereas the earlier and later segments are crucial for generating high-quality final outcomes.
We further posit that avoiding redundant intermediate information leads to exploiting the capability of LLMs to infer concise and coherent intermediate steps by utilizing the known start and end points.
Based on the insights, we propose MidCut, a method that removes redundant middle steps during both training and inference. We demonstrate the effectiveness of MidCut in two scenarios for LLM reasoning: (1) SFT trained on s1K and OpenThoughts datasets for reasoning; and (2) decoding strategy for a test-time application.

## item_id: m_1054

TITLE: OccuQuest: Mitigating Occupational Bias for Inclusive Large Language Models

ABSTRACT: The emergence of large language models (LLMs) has revolutionized natural language processing tasks.
However, existing instruction-tuning datasets suffer from occupational bias: the majority of data relates to only a few occupations, which hampers the instruction-tuned LLMs to generate helpful responses to professional queries from practitioners in specific fields.
To mitigate this issue and promote occupation-inclusive LLMs, we create an instruction-tuning dataset named \emph{OccuQuest}, which contains 110,000+ prompt-completion pairs and 30,000+ dialogues covering over 1,000 occupations in 26 occupational categories.
We systematically request ChatGPT, organizing queries hierarchically based on Occupation, Responsibility, Topic, and Question, to ensure a comprehensive coverage of occupational specialty inquiries.
By comparing with three commonly used datasets (Dolly, ShareGPT, and WizardLM), we observe that OccuQuest exhibits a more balanced distribution across occupations.
Furthermore, we assemble three test sets for comprehensive evaluation, an occu-test set covering 25 occupational categories, an estate set focusing on real estate, and an occu-quora set containing real-world questions from Quora.
We then fine-tune LLaMA on OccuQuest to obtain OccuLLaMA, which significantly outperforms state-of-the-art LLaMA variants (Vicuna, Tulu, and WizardLM) on professional questions in GPT-4 and human evaluations.
Notably, on the occu-quora set, OccuLLaMA reaches a high win rate of 86.4\% against WizardLM.
Furthermore, we demonstrate the potential of combining OccuQuest with other instruction-tuning datasets to enhance the overall performance of LLMs.
By fine-tuning LLaMA on a mixture of OccuQuest and Tulu datasets, we introduce ProLLaMA, which excels in addressing occupational questions and exhibits superior performance in comprehensive evaluations such as MMLU, GSM8K, BBH, and HumanEval.
Among the different LLaMA variants, the 7B and 13B ProLLaMA models achieve the highest performance on MMLU and GSM8K, with the 7B ProLLaMA model demonstrating an improvement of more than 4 points over the other 7B variants on GSM8K.

## item_id: m_1055

TITLE: BALTO: fast tensor program optimization with diversity-based active learning

ABSTRACT: Tensor program optimization (TPO) based on pre-trained models can effectively reduce the computing time of deep neural networks. However, training of such models is prohibitively expensive, which highly depends on a large-scale dataset and thus requires tremendous time-consuming performance measurements (more than 1 million) on target platforms. In this paper, we propose BALTO, a fast TPO approach with biased-diversity-based active learning, aiming at reducing much lower training costs under similar optimization accuracy.The key insight is that random sampling of existing approaches suffers from a heavy redundancy of low-performance programs, which incurs tremendous duplicated time-consuming measurements. Inspired by this, BALTO removes such redundancy by introducing active learning (AL) to TPO for a much lower training cost. However, applying AL with a brute-force way in BALTO can lead to an overestimation problem. To address this, we further propose a biased-diversity-based diversity scheme specially designed for BALTO. We compare BALTO against TenSet on $6$ typical hardware platforms over $2$ learning models. Experimental results show that, on average, BALTO only requires 5% of the total performance measurements of TenSet to achieve the same or higher model accuracy. Moreover, the optimized tensor programs even outperform that of TenSet by 1.06% due to higher model accuracy.

## item_id: m_1056

TITLE: TimelyFL: Heterogeneity-aware Asynchronous Federated Learning with Adaptive Partial Training 

ABSTRACT: In cross-device Federated Learning (FL) environments, scaling synchronous FL methods is challenging as stragglers hinder the training process. Moreover, the availability of each client to join the training is highly variable over time due to system heterogeneities and intermittent connectivity. Recent asynchronous FL methods (e.g., FedBuff) have been proposed to overcome these issues by allowing slower users to continue their work on local training based on stale models and to contribute to aggregation when ready. However, we show empirically that this method can lead to a substantial drop in training accuracy as well as a slower convergence rate. The primary reason is that fast-speed devices contribute to many more rounds of aggregation while others join more intermittently or not at all, and with stale model updates. To overcome this barrier, we propose TimelyFL, a heterogeneity-aware asynchronous FL framework with adaptive partial training. During the training, TimelyFL adjusts the local training workload based on the real-time resource capabilities of each client, aiming to allow more available clients to join in the global update without staleness. We demonstrate the performance benefits of TimelyFL by conducting extensive experiments on various datasets (e.g., CIFAR-10, Google Speech, and Reddit) and models (e.g., ResNet20, VGG11, and ALBERT). We also validate the feasibility of TimelyFL by deploying it on an Android-based mobile device testbed. In comparison with the state-of-the-art (i.e., FedBuff), our evaluations reveal that TimelyFL improves participation rate by 21.13%, harvests 1.28x - 2.89x more efficiency on convergence rate, and provides a 6.25% increment on test accuracy.

## item_id: m_1057

TITLE: Mixed Precision Training With 8-bit Floating Point

ABSTRACT: Reduced precision computation is one of the key areas addressing the widening’compute gap’, driven by an exponential growth in deep learning applications. In recent years, deep neural network training has largely migrated to 16-bit precision,with significant gains in performance and energy efficiency. However, attempts to train DNNs at 8-bit precision have met with significant challenges, because of the higher precision and dynamic range requirements of back-propagation.   In this paper,  we  propose  a  method  to  train  deep  neural  networks  using  8-bit  floating point representation for weights, activations, errors, and gradients.  We demonstrate state-of-the-art accuracy across multiple data sets (imagenet-1K, WMT16)and a broader set of workloads (Resnet-18/34/50, GNMT, and Transformer) than previously reported.   We propose an enhanced loss scaling method to augment the reduced subnormal range of 8-bit floating point, to improve error propagation.We also examine the impact of quantization noise on generalization, and propose a stochastic rounding technique to address gradient noise. As a result of applying all these techniques,  we report slightly higher validation accuracy compared to full precision baseline.

## item_id: m_1058

TITLE: Congested bandits: Optimal routing via short-term resets

ABSTRACT: For traffic routing platforms, the choice of which route to recommend to a user depends on the congestion on these routes -- indeed, an individual's utility depends on the number of people using the recommended route at that instance. Motivated by this, we introduce the problem of Congested Bandits where each arm's reward is allowed to depend on the number of times it was played in the past $\Delta$ timesteps. This dependence on past history of actions leads to a dynamical system where an algorithm's present choices also affect its future pay-offs, and requires an algorithm to plan for this. We study the congestion aware formulation in the  multi-armed bandit (MAB) setup and in the  contextual bandit setup with linear rewards. For the multi-armed setup, we propose a UCB style algorithm  and show that its policy regret scales as $\tilde{O}(\sqrt{K \Delta T})$. For the linear contextual bandit setup, our algorithm, based on an iterative least squares planner, achieves policy regret $\tilde{O}(\sqrt{dT} + \Delta)$. From an experimental standpoint, we corroborate the no-regret properties of our algorithms via a simulation study.

## item_id: m_1059

TITLE: Alpha-divergence bridges maximum likelihood and reinforcement learning in neural sequence generation

ABSTRACT: Neural sequence generation is commonly approached by using maximum- likelihood (ML) estimation or reinforcement learning (RL). However, it is known that they have their own shortcomings; ML presents training/testing discrepancy, whereas RL suffers from sample inefficiency. We point out that it is difficult to resolve all of the shortcomings simultaneously because of a tradeoff between ML and RL. In order to counteract these problems, we propose an objective function for sequence generation using α-divergence, which leads to an ML-RL integrated method that exploits better parts of ML and RL. We demonstrate that the proposed objective function generalizes ML and RL objective functions because it includes both as its special cases (ML corresponds to α → 0 and RL to α → 1). We provide a proposition stating that the difference between the RL objective function and the proposed one monotonically decreases with increasing α. Experimental results on machine translation tasks show that minimizing the proposed objective function achieves better sequence generation performance than ML-based methods.

## item_id: m_1060

TITLE: Variational Component Decoder for Source Extraction from Nonlinear Mixture

ABSTRACT: In many practical scenarios of signal extraction from a nonlinear mixture, only one (signal) source is intended to be extracted. However, modern methods involving Blind Source Separation are inefficient for this task since they are designed to recover all sources in the mixture. In this paper, we propose supervised Variational Component Decoder (sVCD) as a method dedicated to extracting a single source from nonlinear mixture. sVCD leverages the sequence-to-sequence (Seq2Seq) translation ability of a specially designed neural network to approximate a nonlinear inverse of the mixture process, assisted by priors of the interested source. In order to maintain the robustness in the face of real-life samples, sVCD combines Seq2Seq with variational inference to form a deep generative model, and it is trained by optimizing a variant of variational bound on the data likelihood concerning only the interested source. We demonstrate that sVCD has superior performance on nonlinear source extraction over a state-of-the-art method on diverse datasets, including artificially generated sequences, radio frequency (RF) sensing data, and electroencephalogram (EEG) results.

## item_id: m_1061

TITLE: Towards Deep Learning Models Resistant to Adversarial Attacks

ABSTRACT: Recent work has demonstrated that neural networks are vulnerable to adversarial examples, i.e., inputs that are almost indistinguishable from natural data and yet classified incorrectly by the network. To address this problem, we study the adversarial robustness of neural networks through the lens of robust optimization. This approach provides us with a broad and unifying view on much prior work on this topic. Its principled nature also enables us to identify methods for both training and attacking neural networks that are reliable and, in a certain sense, universal. In particular, they specify a concrete security guarantee that would protect against a well-defined class of adversaries. These methods let us train networks with significantly improved resistance to a wide range of adversarial attacks. They also suggest robustness against a first-order adversary as a natural security guarantee. We believe that robustness against such well-defined classes of adversaries is an important stepping stone towards fully resistant deep learning models.

## item_id: m_1062

TITLE: SCAR: Shapley Credit Assignment for More Efficient RLHF

ABSTRACT: Reinforcement Learning from Human Feedback (RLHF) is a widely used technique for aligning Large Language Models (LLMs) with human preferences, yet it often suffers from sparse reward signals, making effective credit assignment challenging. In typical setups, the reward model provides a single scalar score for an entire generated sequence, offering little insight into which token or span-level decisions were responsible for the outcome. To address this, we propose Shapley Credit Assignment Rewards (SCAR), a novel method that leverages Shapley values in cooperative game theory. SCAR distributes the total sequence-level reward among constituent tokens or text spans based on their principled marginal contributions. This creates dense reward signals, crucially, without necessitating the training of auxiliary critique models or recourse to fine-grained human annotations at intermediate generation stages. Unlike prior dense reward methods, SCAR offers a game-theoretic foundation for fair credit attribution. Theoretically, we demonstrate that SCAR preserves the original optimal policy, and empirically, across diverse tasks including sentiment control, text summarization, and instruction tuning, we show that SCAR converges significantly faster and achieves higher final reward scores compared to standard RLHF and attention-based dense reward baselines. Our findings suggest that SCAR provides a more effective and theoretically sound method for credit assignment in RLHF, leading to more efficient alignment of LLMs.

## item_id: m_1063

TITLE: Generative Adversarial Networks using Adaptive Convolution

ABSTRACT: Most existing GANs architectures that generate images use transposed convolution or resize-convolution as their upsampling algorithm from lower to higher resolution feature maps in the generator. We argue that this kind of fixed operation is problematic for GANs to model objects that have very different visual appearances. We propose a novel adaptive convolution method that learns the upsampling algorithm based on the local context at each location to address this problem. We modify a baseline GANs architecture by replacing normal convolutions with adaptive convolutions in the generator. Experiments on CIFAR-10 dataset show that our modified models improve the baseline model by a large margin. Furthermore, our models achieve state-of-the-art performance on CIFAR-10 and STL-10 datasets in the unsupervised setting.

## item_id: m_1064

TITLE: Test Time Learning for Time Series Forecasting

ABSTRACT: We propose the use of Test-Time Training (TTT) modules in a cascade architecture to enhance performance in long-term time series forecasting. Through extensive experiments on standard benchmark datasets, we demonstrate that TTT modules consistently outperform state-of-the-art models, including Mamba-based TimeMachine, particularly in scenarios involving extended sequence and prediction lengths. Our results show significant improvements, especially on larger datasets such as Electricity, Traffic, and Weather, underscoring the effectiveness of TTT in capturing long-range dependencies. Additionally, we explore various convolutional architectures within the TTT framework, showing that convolutional blocks as hidden layer architectures can achieve competitive results.

## item_id: m_1065

TITLE: Invariance-based Learning of Latent Dynamics

ABSTRACT: We propose a new model class aimed at predicting dynamical trajectories from high-dimensional empirical data. This is done by combining variational autoencoders and (spatio-)temporal transformers within a  framework designed to enforce certain scientifically-motivated invariances. The models allow inference of system behavior at any continuous time and generalization well beyond the data distributions seen during training. Furthermore, the models do not require an explicit neural ODE formulation, making them efficient and highly scalable in practice. We study  behavior through simple theoretical analyses and  extensive empirical experiments. The latter investigate  the ability to predict the trajectories of complicated  systems based on finite data and show that the proposed approaches can outperform existing neural-dynamical models. We study also more general inductive bias in the context of transfer to data obtained under entirely novel system interventions. Overall, our results provide a new framework for efficiently learning complicated dynamics in a data-driven manner, with potential applications in a wide range of fields including physics, biology, and engineering.

## item_id: m_1066

TITLE: MambaVC: Exploring Selective State Spaces for Learned Visual Compression

ABSTRACT: Learned visual compression is an important and active task in multimedia. Existing approaches have explored various CNN- and Transformer-based designs to model content distribution and eliminate redundancy, where balancing efficacy (i.e., rate-distortion trade-off) and efficiency remains a challenge. Recently, state-space models (SSMs) have shown promise due to their long-range modeling capacity and efficiency. Inspired by this, we take the first step to explore SSMs for visual compression. We introduce MambaVC, a simple, strong and efficient compression network based on SSM. MambaVC develops a visual state space (VSS) block with a 2D selective scanning (2DSS) module as the nonlinear activation function after each downsampling, which helps to capture informative global contexts and enhances compression. On compression benchmark datasets, MambaVC achieves superior rate-distortion performance with lower computational and memory overheads. Specifically, it outperforms CNN and Transformer variants by 7.2% and 15.2% on Kodak, respectively, while reducing computation by 42% and 24%, and saving 12% and 71% of memory. MambaVC shows even greater improvements with high-resolution images, highlighting its potential and scalability in real-world applications. We also provide a comprehensive comparison of different network designs, underscoring MambaVC's advantages. Code is available at https://anonymous.4open.science/r/MambaVC-408 and will be open-sourced.

## item_id: m_1067

TITLE: MermaidFlow: Redefining Agentic Workflow Generation via Safety-Constrained Evolutionary Programming

ABSTRACT: Despite the promise of autonomous agentic reasoning, existing workflow generation methods frequently produce fragile, unexecutable plans due to unconstrained LLM-driven construction. We propose MermaidFlow, a framework that redefines the agentic search space through safety-constrained graph evolution. At its core, MermaidFlow represent workflows as a verifiable intermediate representation using Mermaid, a structured and human-interpretable graph language. We formulate domain-aware evolutionary operators, i.e., crossover,  mutation, insertion, and deletion, to preserve semantic correctness while promoting structural diversity, enabling efficient exploration of a high-quality, statically verifiable workflow space. Without modifying task settings or evaluation protocols, MermaidFlow achieves consistent improvements in success rates and faster convergence to executable plans on the agent reasoning benchmark. The experimental results demonstrate that safety-constrained graph evolution offers a scalable, modular foundation for robust and interpretable agentic reasoning systems.

## item_id: m_1068

TITLE: Completion Consistency for Point Cloud Completion Enhancement

ABSTRACT: Point cloud completion networks are conventionally trained to minimize the disparities between the completed point cloud and the ground-truth counterpart. However, an incomplete object-level point cloud can have multiple valid completion solutions when it is examined in isolation. This one-to-many mapping issue can cause contradictory supervision signals to the network, because the loss function may produce various values for identical input-output pairs of the network. And in many cases, this issue could adversely impact the network optimization process. In this work, we propose to enhance the conventional learning objective using a novel completion consistency loss to mitigate the one-to-many mapping problem. Specifically, the proposed consistency loss imposes a constraint to ensure that a point cloud completion network generates a consistent completion solution for incomplete objects originating from the same source point cloud. Experimental results across multiple well-established datasets and benchmarks demonstrate the excellent capability of the proposed completion consistency loss to enhance the completion performance of various existing networks without any modification to the design of the networks.

## item_id: m_1069

TITLE: Learning Efficient Parameter Server Synchronization Policies for Distributed SGD

ABSTRACT: We apply a reinforcement learning (RL) based approach to learning optimal synchronization policies used for Parameter Server-based distributed training of machine learning models with Stochastic Gradient Descent (SGD). Utilizing a formal synchronization policy description in the PS-setting, we are able to derive a suitable and compact description of states and actions, allowing us to efficiently use the standard off-the-shelf deep Q-learning algorithm. As a result, we are able to learn synchronization policies which generalize to different cluster environments, different training datasets and small model variations and (most importantly) lead to considerable decreases in training time when compared to standard policies such as bulk synchronous parallel (BSP), asynchronous parallel (ASP), or stale synchronous parallel (SSP). To support our claims we present extensive numerical results obtained from experiments performed in simulated cluster environments. In our experiments training time is reduced by 44 on average and learned policies generalize to multiple unseen circumstances.

## item_id: m_1070

TITLE: GM-DDPM: Denoising diffusion probabilistic models with Gaussian Mixture Noise

ABSTRACT: Denoising diffusion probabilistic models (DDPM) have shown impressive performance in various domains as a class of deep generative models. In this paper, we introduce the Gaussian Mixture noise-based DDPM (GM-DDPM), which considers the Markov diffusion posterior as a Gaussian mixture model. Specifically, GM-DDPM randomly selects a Gaussian component and then add the chosen Gaussian noise, which can be demonstrated as more efficient way to perturb the signals into a simple known distribution. We further define the reverse probabilistic model as a parameterized Gaussian mixture kernel. Due to the intractability in calculating the KL divergence between Gaussian mixture models, we derive a variational bound to maximize the likelihood, offering a concise formulation for optimizing the denoising model and valuable insights for designing the sampling strategies. Our theoretical derivation highlights that GM-DDPM only requires the inclusion of a random offset in both the diffusion and reverse processes, which can be efficiently implemented with just several lines of code. Furthermore, we present three streamlined sampling strategies that interface with diverse fast dedicated solvers for diffusion ordinary differential equations, boosting the efficacy of image representation in the sampling phase and alleviating the issue of slow generation speed, thereby enhancing both efficiency and accuracy. Extensive experiments on benchmark datasets demonstrate the effectiveness of GM-DDPM and its superiority over the original DDPM.

## item_id: m_1071

TITLE: Minimal Value-Equivalent Partial Models for Scalable and Robust Planning in Lifelong Reinforcement Learning

ABSTRACT: Learning models of the environment from pure interaction is often considered an essential component of building lifelong reinforcement learning agents. However, the common practice in model-based reinforcement learning is to learn models that model every aspect of the agent's environment, regardless of whether they are important in coming up with optimal decisions or not. In this paper, we argue that such models are not particularly well-suited for performing scalable and robust planning in lifelong reinforcement learning scenarios and we propose new kinds of models that only model the relevant aspects of the environment, which we call minimal value-equivalent partial models. After providing the formal definitions of these models, we provide theoretical results demonstrating the scalability advantages of performing planning with minimal value-equivalent partial models and then perform experiments to empirically illustrate our theoretical results. Finally, we provide some useful heuristics on how to learn such models with deep learning architectures and empirically demonstrate that models learned in such a way can allow for performing planning that is robust to distribution shifts and compounding model errors. Overall, both our theoretical and empirical results suggest that minimal value-equivalent partial models can provide significant benefits to performing scalable and robust planning in lifelong reinforcement learning scenarios. 

## item_id: m_1072

TITLE: A Neural Network MCMC sampler that maximizes Proposal Entropy

ABSTRACT: Markov Chain Monte Carlo (MCMC) methods sample from unnormalized probability distributions and offer guarantees of exact sampling. However, in the continuous case, unfavorable geometry of the target distribution can greatly limit the efficiency of MCMC methods. Augmenting samplers with neural networks can potentially improve their efficiency. Previous neural network based samplers were trained with objectives that either did not explicitly encourage exploration, or used a L2 jump objective which could only be applied to well structured distributions. Thus it seems promising to instead maximize the proposal entropy for adapting the proposal to distributions of any shape. To allow direct optimization of the proposal entropy, we propose a neural network MCMC sampler that has a flexible and tractable proposal distribution. Specifically, our network architecture utilizes the gradient of the target distribution for generating proposals. Our model achieves significantly higher efficiency than previous neural network MCMC techniques in a variety of sampling tasks. Further, the sampler is applied on training of a convergent energy-based model of natural images. The learned sampler achieves significantly higher proposal entropy and sample quality compared to Langevin dynamics sampler.

## item_id: m_1073

TITLE: V-MPO: On-Policy Maximum a Posteriori Policy Optimization for Discrete and Continuous Control

ABSTRACT: Some of the most successful applications of deep reinforcement learning to challenging domains in discrete and continuous control have used policy gradient methods in the on-policy setting. However, policy gradients can suffer from large variance that may limit performance, and in practice require carefully tuned entropy regularization to prevent policy collapse. As an alternative to policy gradient algorithms, we introduce V-MPO, an on-policy adaptation of Maximum a Posteriori Policy Optimization (MPO) that performs policy iteration based on a learned state-value function. We show that V-MPO surpasses previously reported scores for both the Atari-57 and DMLab-30 benchmark suites in the multi-task setting, and does so reliably without importance weighting, entropy regularization, or population-based tuning of hyperparameters. On individual DMLab and Atari levels, the proposed algorithm can achieve scores that are substantially higher than has previously been reported. V-MPO is also applicable to problems with high-dimensional, continuous action spaces, which we demonstrate in the context of learning to control simulated humanoids with 22 degrees of freedom from full state observations and 56 degrees of freedom from pixel observations, as well as example OpenAI Gym tasks where V-MPO achieves substantially higher asymptotic scores than previously reported.

## item_id: m_1074

TITLE: Conditional Support Alignment for Domain Adaptation with Label Shift

ABSTRACT: Unsupervised domain adaptation (UDA) refers to a domain adaptation framework in which a learning model is trained based on the labeled samples on the source domain and unlabelled ones in the target domain. The dominant existing methods in the field that rely on the classical covariate shift assumption to learn domain-invariant feature representation have yielded suboptimal performance under label distribution shift. In this paper, we propose a novel conditional adversarial support alignment (CASA) whose aim is to minimize the conditional symmetric support divergence between the source's and target domain's feature representation distributions, aiming at a more discriminative representation for the classification task. We also introduce a novel theoretical target risk bound, which justifies the merits of aligning the supports of conditional feature distributions compared to the existing marginal support alignment approach in the UDA settings. We then provide a complete training process for learning in which the objective optimization functions are precisely based on the proposed target risk bound. Our empirical results demonstrate that CASA outperforms other state-of-the-art methods on different UDA benchmark tasks under different label shift conditions.

## item_id: m_1075

TITLE: The Convex Information Bottleneck Lagrangian

ABSTRACT: The information bottleneck (IB) problem tackles the issue of obtaining relevant compressed representations T of some random variable X for the task of predicting Y. It is defined as a constrained optimization problem which maximizes the information the representation has about the task, I(T;Y), while ensuring that a minimum level of compression r is achieved (i.e., I(X;T) <= r). For practical reasons the problem is usually solved by maximizing the IB Lagrangian for many values of the Lagrange multiplier, therefore drawing the IB curve (i.e., the curve of maximal I(T;Y) for a given I(X;Y)) and selecting the representation of desired predictability and compression. It is known when Y is a deterministic function of X, the IB curve cannot be explored and other Lagrangians have been proposed to tackle this problem (e.g., the squared IB Lagrangian). In this paper we (i) present a general family of Lagrangians which allow for the exploration of the IB curve in all scenarios; (ii) prove that if these Lagrangians are used, there is a one-to-one mapping between the Lagrange multiplier and the desired compression rate r for known IB curve shapes, hence, freeing from the burden of solving the optimization problem for many values of the Lagrange multiplier.

## item_id: m_1076

TITLE: SpectralNet: Spectral Clustering using Deep Neural Networks

ABSTRACT: Spectral clustering is a leading and popular technique in unsupervised data analysis.  Two of its major limitations are scalability and generalization of the spectral embedding (i.e., out-of-sample-extension). In this paper we introduce a deep learning approach to spectral clustering that overcomes the above shortcomings. Our network, which we call SpectralNet, learns a map that embeds input data points into the eigenspace of their associated graph Laplacian matrix and subsequently clusters them. We train SpectralNet using a procedure that involves constrained stochastic optimization. Stochastic optimization allows it to scale to large datasets, while the constraints, which are implemented using a special purpose output layer, allow us to keep the network output orthogonal. Moreover, the map learned by SpectralNet naturally generalizes the spectral embedding to unseen data points. To further improve the quality of the clustering, we replace the standard pairwise Gaussian affinities with affinities leaned from unlabeled data using a Siamese network.  Additional improvement can be achieved by applying the network to code representations produced, e.g., by standard autoencoders. Our end-to-end learning procedure is fully unsupervised. In addition, we apply VC dimension theory to derive a lower bound on the size of  SpectralNet.  State-of-the-art clustering results are reported for both the MNIST and Reuters datasets.


## item_id: m_1077

TITLE: Beyond Laplace and Gaussian: Exploring the Generalized Gaussian Mechanism for Private Machine Learning

ABSTRACT: Differential privacy (DP) is obtained by randomizing a data analysis algorithm, which necessarily introduces a tradeoff between its utility and privacy. Many DP mechanisms are built upon one of two underlying tools: Laplace and Gaussian additive noise mechanisms. We expand the search space of algorithms by investigating the Generalized Gaussian (GG) mechanism, which samples the additive noise term $x$ with probability proportional to $e^{-\frac{| x |}{\sigma}^{\beta} }$ for some $\beta \geq 1$. The Laplace and Gaussian mechanisms are special cases of GG for $\beta=1$ and $\beta=2$ respectively. 

In this work, we prove that all members of the GG family satisfy differential privacy, and provide an extension to an existing numerical accountant (the PRV accountant) to do privacy accounting. We apply the GG mechanism to two canonical tools for private machine learning, PATE and DP-SGD; we show that $\beta$ has a weak relationship with test-accuracy, and that $\beta=2$ (Gaussian) is often a near-optimal value of $\beta$ for the privacy-accuracy tradeoff of both algorithms. This provides justification for the widespread adoption of the Gaussian mechanism in DP learning. That said, we do observe a minor improvement in the utility of both algorithms for $\beta\neq 2$, suggesting that further exploration of general families of noise distributions may be a worthy pursuit to improve performance in DP mechanisms.

## item_id: m_1078

TITLE: SHAQ: Incorporating Shapley Value Theory into Multi-Agent Q-Learning

ABSTRACT: Value factorisation proves to be a useful technique in multi-agent reinforcement learning (MARL), but the underlying mechanism is not yet fully understood. This paper explores a theoretical framework for value factorisation with interpretability. We generalise Shapley value in coalitional game theory to Markov convex game (MCG) and use it as a value factorisation method for MARL. We show that the generalised Shapley value possesses several features such as (1) efficiency: the sum of optimal local values is equal to the optimal global value, (2) fairness in factorisation of the global value, and (3) sensitiveness to dummy agents. Moreover, we show that MCG with the grand coalition and the generalised Shapley value is within $\epsilon$-core, which means no agents would deviate from the grand coalition. Since MCG with the grand coalition is equivalent to global reward game, it is the first time that Shapley value is rigorously proved to be rationally applied as a value factorisation method for global reward game. Moreover, extending from the Bellman operator we propose Shapley-Q operator that is proved to converge to the optimal generalised Shapley value. With stochastic approximation, a new MARL algorithm called Shapley Q-learning (SHAQ) is yielded. We show the performance of SHAQ on Predator-Prey for modelling relative overgeneralisation and StarCraft Multi-Agent Challenge (SMAC). In experiments, we also demonstrate the interpretability of SHAQ that is lacking in other state-of-the-art baselines.

## item_id: m_1079

TITLE: Fine-Grained Urban Traffic Forecasting on Metropolis-Scale Road Networks

ABSTRACT: Traffic forecasting on road networks is a complex task of significant practical importance that has recently attracted considerable attention from the machine learning community, with spatiotemporal graph neural networks (GNNs) becoming the most popular approach. The proper evaluation of traffic forecasting methods requires realistic datasets, but current publicly available benchmarks have significant drawbacks, including the absence of information about road connectivity for road graph construction, limited information about road properties, and a relatively small number of road segments that falls short of real-world applications. Further, current datasets mostly contain information about intercity highways with sparsely located sensors, while city road networks arguably present a more challenging forecasting task due to much denser roads and more complex urban traffic patterns. In this work, we provide a more complete, realistic, and challenging benchmark for traffic forecasting by releasing datasets representing the road networks of two major cities, with the largest containing almost 100,000 road segments (more than a 10-fold increase relative to existing datasets). Our datasets contain rich road features and provide fine-grained data about both traffic volume and traffic speed, allowing for building more holistic traffic forecasting systems. We show that most current implementations of neural spatiotemporal models for traffic forecasting have problems scaling to datasets of our size. To overcome this issue, we propose an alternative approach to neural traffic forecasting that uses a GNN without a dedicated module for temporal sequence processing, thus achieving much better scalability, while also demonstrating stronger forecasting performance. We hope our datasets and modeling insights will serve as a valuable resource for research in traffic forecasting and, more generally, urban computing and smart city development.

## item_id: m_1080

TITLE: Federated Semi-Supervised Learning with Inter-Client Consistency & Disjoint Learning

ABSTRACT: While existing federated learning approaches mostly require that clients have fully-labeled data to train on, in realistic settings, data obtained at the client-side often comes without any accompanying labels. Such deficiency of labels may result from either high labeling cost, or difficulty of annotation due to the requirement of expert knowledge. Thus the private data at each client may be either partly labeled, or completely unlabeled with labeled data being available only at the server, which leads us to a new practical federated learning problem, namely Federated Semi-Supervised Learning (FSSL). In this work, we study two essential scenarios of FSSL based on the location of the labeled data. The first scenario considers a conventional case where clients have both labeled and unlabeled data (labels-at-client), and the second scenario considers a more challenging case, where the labeled data is only available at the server (labels-at-server). We then propose a novel method to tackle the problems, which we refer to as Federated Matching (FedMatch). FedMatch improves upon naive combinations of federated learning and semi-supervised learning approaches with a new inter-client consistency loss and decomposition of the parameters for disjoint learning on labeled and unlabeled data. Through extensive experimental validation of our method in the two different scenarios, we show that our method outperforms both local semi-supervised learning and baselines which naively combine federated learning with semi-supervised learning.

## item_id: m_1081

TITLE: Variational Autoencoder with Arbitrary Conditioning

ABSTRACT: We propose a single neural probabilistic model based on variational autoencoder that can be conditioned on an arbitrary subset of observed features and then sample the remaining features in "one shot". The features may be both real-valued and categorical. Training of the model is performed by stochastic variational Bayes. The experimental evaluation on synthetic data, as well as feature imputation and image inpainting problems, shows the effectiveness of the proposed approach and diversity of the generated samples.

## item_id: m_1082

TITLE: Discovering Novel Customer Features with Recurrent Neural Networks for Personality Based Financial Services

ABSTRACT: The micro-segmentation of customers in the finance sector is a non-trivial task and has been an atypical omission from recent scientific literature. Where traditional segmentation classifies customers based on coarse features such as demographics, micro-segmentation depicts more nuanced differences between individuals, bringing forth several advantages including the potential for improved personalization in financial services. AI and representation learning offer a unique opportunity to solve the problem of micro-segmentation. Although ubiquitous in many industries, the proliferation of AI in sensitive industries such as finance has become contingent on the imperatives of responsible AI. We had previously solved the micro-segmentation problem by extracting temporal features from the state space of a recurrent neural network (RNN). However, due to the inherent opacity of RNNs our solution lacked an explanation - one of the imperatives of responsible AI. In this study, we address this issue by extracting an explanation for and providing an interpretation of our temporal features. We investigate the state space of our RNN and through a linear regression model reconstruct the trajectories in the state space with high fidelity. We show that our linear regression coefficients have not only learned the rules used to create the RNN’s output data but have also learned the relationships that were not directly evident in the raw data.

## item_id: m_1083

TITLE: GAETS: A Graph Autoencoder Time Series Approach Towards Battery Parameter Estimation

ABSTRACT:  Lithium-ion batteries are powering the ongoing transportation electrification revolution. Lithium-ion batteries possess higher energy density and favourable electrochemical properties which make it a preferable energy source for electric vehicles. Precise estimation of battery parameters (Charge capacity, voltage etc) is vital to estimate the available range in an electric vehicle. Graph-based estimation techniques enable us to understand the variable dependencies underpinning them to improve estimates. In this paper we employ Graph Neural Networks for battery parameter estimation, we introduce a unique graph autoencoder time series estimation approach. Variables in battery measurements are known to have an underlying relationship with each other in a certain causal structure. Therefore, we include ideas from the field of causal structure learning as a regularisation to our learned adjacency matrix technique. We use graph autoencoder based on a non-linear version of NOTEARS Zheng et al. (2018) as this allowed us to perform gradient-descent in learning the structure (instead of treating it as a combinatorial optimisation problem). The proposed architecture outperforms the state-of-the-art Graph Time Series  (GTS) Shang et al. (2021a)   architecture for battery parameter estimation. We call our method GAETS (Graph AutoEncoder Time Series).

## item_id: m_1084

TITLE: MolEBM: Molecule Generation and Design by Latent Space Energy-Based Modeling

ABSTRACT: Generation of molecules with desired chemical and biological properties such as high drug-likeness, high binding affinity to target proteins, is critical in drug discovery. In this paper, we propose a probabilistic generative model to capture the joint distribution of molecules and their properties. Our model assumes an energy-based model (EBM) in the latent space. Given the latent vector sampled from the latent space EBM, both molecules and molecular properties are conditionally sampled via a top-down molecule generator model and a property regression model respectively. The EBM in a low dimensional latent space allows our model to capture complex chemical rules implicitly but efficiently and effectively. Due to the joint modeling with chemical properties, molecule design can be conveniently and naturally achieved by conditional sampling from our learned model given desired properties, in both single-objective and multi-objective optimization settings. The latent space EBM, top-down molecule generator, and property regression model are learned jointly by maximum likelihood, while optimization of properties is accomplished by gradual shifting of the model distribution towards the region supported by molecules with high property values. Our experiments show that our model outperforms state-of-the-art models on various molecule design tasks. 

## item_id: m_1085

TITLE: Stein Latent Optimization for Generative Adversarial Networks

ABSTRACT: Generative adversarial networks (GANs) with clustered latent spaces can perform conditional generation in a completely unsupervised manner. In the real world, the salient attributes of unlabeled data can be imbalanced. However, most of existing unsupervised conditional GANs cannot cluster attributes of these data in their latent spaces properly because they assume uniform distributions of the attributes. To address this problem, we theoretically derive Stein latent optimization that provides reparameterizable gradient estimations of the latent distribution parameters assuming a Gaussian mixture prior in a continuous latent space. Structurally, we introduce an encoder network and novel unsupervised conditional contrastive loss to ensure that data generated from a single mixture component represent a single attribute. We confirm that the proposed method, named Stein Latent Optimization for GANs (SLOGAN), successfully learns balanced or imbalanced attributes and achieves state-of-the-art unsupervised conditional generation performance even in the absence of attribute information (e.g., the imbalance ratio). Moreover, we demonstrate that the attributes to be learned can be manipulated using a small amount of probe data.

## item_id: m_1086

TITLE: DreamBench++: A Human-Aligned Benchmark for Personalized Image Generation

ABSTRACT: Personalized image generation holds great promise in assisting humans in everyday work and life due to its impressive function in creatively generating personalized content. However, current evaluations either are automated but misalign with humans or require human evaluations that are time-consuming and expensive. In this work, we present DreamBench++, a human-aligned benchmark that advanced multimodal GPT models automate. Specifically, we systematically design the prompts to let GPT be both human-aligned and self-aligned, empowered with task reinforcement. Further, we construct a comprehensive dataset comprising diverse images and prompts. By benchmarking 7 modern generative models, we demonstrate that \dreambench results in significantly more human-aligned evaluation, helping boost the community with innovative findings.

## item_id: m_1087

TITLE: Dissecting Causal Biases

ABSTRACT: Accurately measuring discrimination in machine learning-based automated decision systems is required to address the vital issue of fairness between subpopulations and/or individuals. Any bias in measuring discrimination can lead to either amplification or underestimation of the true value of discrimination. This paper focuses on a class of bias originating in the way training data is generated and/or collected.  We call such class causal biases and use tools from the field of causality to formally define and analyze such biases. Four sources of bias are considered, namely, confounding, selection, measurement, and interaction. The main contribution of this paper is to provide, for each source of bias, a closed-form expression in terms of the model parameters. This makes it possible to analyze the behavior of each source of bias, in particular, in which cases they are absent and in which other cases they are maximized. We hope that the provided characterizations help the community better understand the sources of bias in machine learning applications.

## item_id: m_1088

TITLE: Grounding Language to Entities for Generalization in Reinforcement Learning

ABSTRACT: In this paper, we consider the problem of leveraging textual descriptions to improve generalization of control policies to new scenarios. Unlike prior work in this space, we do not assume access to any form of prior knowledge connecting text and state observations, and learn both symbol grounding and control policy simultaneously. This is challenging due to a lack of concrete supervision, and incorrect groundings can result in worse performance than policies that do not use the text at all. 
We develop a new model, EMMA (Entity Mapper with Multi-modal Attention) which uses a multi-modal entity-conditioned attention module that allows for selective focus over relevant sentences in the manual for each entity in the environment. EMMA is end-to-end differentiable and can learn a latent grounding of entities and dynamics from text to observations using environment rewards as the only source of supervision.
To empirically test our model, we design a new framework of 1320 games and collect text manuals with free-form natural language via crowd-sourcing. We demonstrate that EMMA achieves successful zero-shot generalization to unseen games with new dynamics, obtaining significantly higher rewards compared to multiple baselines. The grounding acquired by EMMA is also robust to noisy descriptions and linguistic variation.

## item_id: m_1089

TITLE: Probabilistic Recursive Reasoning for Multi-Agent Reinforcement Learning

ABSTRACT: Humans are capable of attributing latent mental contents such as beliefs, or intentions to others. The social skill is critical in everyday life to reason about the potential consequences of their behaviors so as to plan ahead. It is known that humans use this reasoning ability recursively, i.e. considering what others believe about their own beliefs.  In this paper, we start  from level-$1$ recursion and introduce a probabilistic recursive reasoning (PR2) framework for multi-agent reinforcement learning. Our hypothesis is that it is beneficial for each agent to account for how the opponents would react to its future behaviors. Under the PR2 framework, we adopt variational Bayes methods to approximate the opponents' conditional policy, to which each agent finds the  best response and then improve their own policy. We develop  decentralized-training-decentralized-execution  algorithms, PR2-Q and PR2-Actor-Critic, that are proved to converge in the self-play scenario when there is one Nash equilibrium. Our methods are tested on both the matrix game and the differential game, which have a non-trivial equilibrium where common gradient-based methods fail to converge. Our experiments show that it is critical to reason about how the opponents believe about what the agent believes. We expect our work to contribute a new idea of modeling the opponents to the multi-agent reinforcement learning community.  


## item_id: m_1090

TITLE: Distilled embedding: non-linear embedding factorization using knowledge distillation

ABSTRACT: Word-embeddings are a vital component of Natural Language Processing (NLP) systems and have been extensively researched. Better representations of words have come at the cost of huge memory footprints, which has made deploying NLP models on edge-devices challenging due to memory limitations. Compressing embedding matrices without sacrificing model performance is essential for successful commercial edge deployment. In this paper, we propose Distilled Embedding, an (input/output) embedding compression method based on low-rank matrix decomposition with an added non-linearity. First, we initialize the weights of our decomposition by learning to reconstruct the full word-embedding and then fine-tune on the downstream task employing knowledge distillation on the factorized embedding. We conduct extensive experimentation with various compression rates on machine translation, using different data-sets with a shared word-embedding matrix for both embedding and vocabulary projection matrices. We show that the proposed technique outperforms conventional low-rank matrix factorization, and other recently proposed word-embedding matrix compression methods. 


## item_id: m_1091

TITLE: Loss Functions for Multiset Prediction

ABSTRACT: We study the problem of multiset prediction. The goal of multiset prediction is to train a predictor that maps an input to a multiset consisting of multiple items. Unlike existing problems in supervised learning, such as classification, ranking and sequence generation, there is no known order among items in a target multiset, and each item in the multiset may appear more than once, making this problem extremely challenging. In this paper, we propose a novel multiset loss function by viewing this problem from the perspective of sequential decision making. The proposed multiset loss function is empirically evaluated on two families of datasets, one synthetic and the other real, with varying levels of difficulty, against various baseline loss functions including reinforcement learning, sequence, and aggregated distribution matching loss functions. The experiments reveal the effectiveness of the proposed loss function over the others.

## item_id: m_1092

TITLE: SplitRegex: Faster Regex Synthesis via Neural Example Splitting

ABSTRACT: Due to the practical importance of regular expressions (regexes, for short), there has been a lot of research to automatically generate regexes from positive and negative string examples. A basic idea of learning a regex is a search-and-repair; search for a correct regex and repair it if incorrect. The problem is known to be PSPACE-complete and the main issue is to obtain a regex quickly within a time limit. 
While classical regex learning methods do not perform well, recent approaches using deep neural networks show better performance
with respect to the accuracy of the resulting regexes. However, all these approaches including SOTA models are often extremely slow because of the slow searching mechanism, and do not produce desired regexes within a given time limit. 
We tackle the problem of learning regexes faster from positive and negative strings by relying on a novel approach called `neural example splitting'. Our approach essentially split up example strings into multiple parts using a neural network trained to group similar substrings from positive strings. This helps to learn a regex faster and, thus, more accurately since we now learn from several short-length strings.
We propose an effective regex synthesis framework called `SplitRegex' that synthesizes subregexes from `split' positive substrings and produces the final regex by concatenating the synthesized subregexes. For the negative sample, we exploit pre-generated subregexes during the subregex synthesis process and perform the matching against negative strings. Then the final regex becomes consistent with all negative strings. SplitRegex is a divided-and-conquer framework for learning target regexes; split (=divide) positive strings and infer partial regexes for multiple parts, which is much more accurate than the whole string inferring, and concatenate (=conquer) inferred regexes while satisfying negative strings. We empirically demonstrate that the proposed SplitRegex framework substantially improves the previous regex synthesis approaches over four benchmark datasets. 

## item_id: m_1093

TITLE: FedSumUp:Secure Federated Learning Without Client-Side Training for Resource-Constrained Edge Devices

ABSTRACT: Horizontal Federated Learning (HFL) enables multiple clients with private data to collaboratively train a global model without sharing their local data. As a research branch of HFL, Federated Data Condensation with Distribution Matching (FDCDM) introduces a novel collaborative paradigm where clients upload small synthetic datasets instead of gradients and parameters. FDCDM faces two key challenges: privacy leakage risk, where synthetic data may leak the privacy of real data; and high computational cost on the client side, which limits the deployment capability of FDCDM on resource-constrained devices. To address these challenges, we propose FedSumUp, an improved FDCDM method. The core designs of FedSumUp include: generating initial data templates based on a Variational Autoencoder (VAE); and migrating the entire synthetic data optimization process to the server side, requiring clients only to upload distilled synthetic data and the mean of raw data features without exposing the original data itself. Experimental results on multiple real-world datasets demonstrate that FedSumUp achieves notable advantages in the following aspects: drastically reducing the visual similarity between synthetic and real data, and effectively resisting membership inference attacks; significantly lowering client-side computational overhead, making it deployable on edge devices. FedSumUp is the first work to systematically analyze privacy risks in FDCDM from the perspective of data similarity, providing a new direction for building efficient and privacy-preserving federated learning frameworks.

## item_id: m_1094

TITLE: Analyzing Federated Learning through an Adversarial Lens

ABSTRACT: Federated learning distributes model training among a multitude of agents, who, guided by privacy concerns, perform training using their local data but share only model parameter updates, for iterative aggregation at the server. In this work, we explore the threat of model poisoning attacks on federated learning initiated by a single, non-colluding malicious agent where the adversarial objective is to cause the model to misclassify a set of chosen inputs with high confidence. We explore a number of strategies to carry out this attack, starting with simple boosting of the malicious agent's update to overcome the effects of other agents' updates. To increase attack stealth, we propose an alternating minimization strategy, which alternately optimizes for the training loss and the adversarial objective. We follow up by using parameter estimation for the benign agents' updates to improve on attack success. Finally, we use a suite of interpretability techniques to generate visual explanations of model decisions for both benign and malicious models and show that the explanations are nearly visually indistinguishable. Our results indicate that even a highly constrained adversary can carry out model poisoning attacks while simultaneously maintaining stealth, thus highlighting the vulnerability of the federated learning setting and the need to develop effective defense strategies.

## item_id: m_1095

TITLE: How Neural Networks Extrapolate: From Feedforward to Graph Neural Networks

ABSTRACT: We study how neural networks trained by gradient descent  extrapolate, i.e., what they learn outside the support of the training distribution. Previous works report mixed empirical results when extrapolating with neural networks: while feedforward neural networks, a.k.a. multilayer perceptrons (MLPs), do not extrapolate well in certain simple tasks, Graph Neural Networks (GNNs) -- structured networks with MLP modules -- have shown some success in more complex tasks.  Working towards a theoretical explanation, we identify conditions under which MLPs and GNNs extrapolate well. First, we quantify the observation that ReLU MLPs quickly converge to linear functions along any direction from the origin, which implies that ReLU MLPs do not extrapolate most nonlinear functions. But, they can provably learn a linear target function when the training distribution is sufficiently diverse. Second, in connection to analyzing the successes and limitations of GNNs, these results suggest a hypothesis for which we provide theoretical and empirical evidence: the success of GNNs in extrapolating algorithmic tasks to new data (e.g., larger graphs or edge weights) relies on encoding task-specific non-linearities in the architecture or features. Our theoretical analysis builds on a connection of over-parameterized networks to the neural tangent kernel.  Empirically, our theory holds across different training settings.

## item_id: m_1096

TITLE: Long-time asymptotics of noisy SVGD outside the population limit

ABSTRACT: Stein Variational Gradient Descent (SVGD) is a widely used sampling algorithm that has been successfully applied in several areas of Machine Learning. SVGD operates by iteratively moving a set of $n$ interacting particles (which represent the samples) to approximate the target distribution. Despite recent studies on the complexity of SVGD and its variants, their long-time asymptotic behavior (i.e., after numerous iterations $k$) is still not understood in the finite number of particles regime. We study the long-time asymptotic behavior of a noisy variant of SVGD. First, we establish that the limit set of noisy SVGD for large $k$ is well-defined. We then characterize this limit set, showing that it approaches the target distribution as $n$ increases. In particular, noisy SVGD avoids the variance collapse observed for SVGD. Our approach involves demonstrating that the trajectories of noisy SVGD closely resemble those described by a McKean-Vlasov process.

## item_id: m_1097

TITLE: Decentralized Learning for Overparameterized Problems: A Multi-Agent Kernel Approximation Approach

ABSTRACT: This work develops a novel framework for communication-efficient distributed learning where the models to be learned are overparameterized. We focus on a class of kernel learning problems (which includes the popular neural tangent kernel (NTK) learning as a special case) and propose a novel {\it multi-agent kernel approximation} technique that allows the agents to distributedly estimate the full kernel function, and subsequently perform decentralized optimization, without directly exchanging any local data or parameters. The proposed framework is a significant departure from the classical consensus-based approaches, because the agents do not exchange problem parameters, and no consensus is required. We analyze the optimization and the generalization performance of the proposed framework for the $\ell_2$ loss. We show that with $M$ agents and $N$ total samples when certain generalized inner-product kernels (resp. the random features kernel) are used, each agent needs to communicate $\mathcal{O}\big({N^2}/{M}\big)$ bits (resp. $\mathcal{O}\big(N \sqrt{N}/M \big)$ real values) to achieve minimax optimal generalization performance. We validate the theoretical results on 90 UCI benchmarking datasets (with average data size $N \approx 1000$) and show that each agent needs to share a total of $200N/M$ bits (resp. $3N/M$ real values) to closely match the performance of the centralized algorithms, and these numbers are independent of parameter and feature dimensions. 

## item_id: m_1098

TITLE: Dialogue Learning With Human-in-the-Loop

ABSTRACT: An important aspect of developing conversational agents is to give a bot the ability to improve through communicating with humans and to learn from the mistakes that it makes.  Most research has focused on learning from fixed training sets of labeled data rather than interacting with a dialogue partner in an online fashion. In this paper we explore this direction in a reinforcement learning setting where the bot improves its question-answering ability from feedback a teacher gives following its generated responses. We build a simulator that tests various aspects of such learning in a synthetic environment, and introduce models that work in this regime.  Finally, real experiments with Mechanical Turk validate the approach.


## item_id: m_1099

TITLE: Learning the Hidden Set Locally

ABSTRACT: Learning elements of the hidden set(s), also known as group testing (GT), is a well-established area in which one party tries to discover elements hidden by the other party by asking queries and analyzing feedback. The feedback is a function of the intersection of the query with the hidden set -- in our case, it is a classical double-threshold function, which returns $i$ if the intersection is a singleton $i\in [n]$ and "null" otherwise (i.e., when the intersection is empty or of size at least $2$). In this work, we introduce a local framework to this problem: each hidden element is an "autonomous" element and can analyze feedback itself, but only for the queries which this element is a part of. The goal is to design a deterministic non-adaptive sequence of queries that allows each non-hidden element to learn about all other hidden agents. We show that, surprisingly, this task requires substantially more queries than the classic group testing -- by proving a super-qubic (in terms of the number of hidden elements) lower bound and constructing a specific sequence of slightly longer length. We also extend the results to the model, where agents belong to various clusters and selection must be done in queries avoiding elements from ``interfering'' clusters. Our algorithms could be generalized to other feedback functions, to adversarial/stochastic fault-prone scenarios and applied to codes.

## item_id: m_1100

TITLE: Semantic Inference Network for Few-shot Streaming Label Learning

ABSTRACT: Streaming label learning aims to model newly emerged labels for multi-label classification systems, which requires plenty of new label data for training. However, in changing environments, only a small amount of new label data can practically be collected. In this work, we formulate and study few-shot streaming label learning (FSLL), which models emerging new labels with only a few annotated examples by utilizing the knowledge learned from past labels. We propose a meta-learning framework, Semantic Inference Network (SIN), which can learn and infer the semantic correlation between new labels and past labels to adapt FSLL tasks from a few examples effectively. SIN leverages label semantic representation to regularize the output space and acquires label-wise meta-knowledge based on the gradient-based meta-learning. Moreover, SIN incorporates a novel label decision module with a meta-threshold loss to find the optimal confidence thresholds for each new label. Theoretically, we demonstrate that the proposed semantic inference mechanism could constrain the complexity of hypotheses space to reduce the risk of overfitting and achieve better generalizability. Experimentally, extensive empirical results and ablation studies illustrate the superior performance of SIN over the prior state-of-the-art methods on FSLL.
