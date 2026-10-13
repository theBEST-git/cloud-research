# Batch 17 — 100 items

## item_id: m_1601

TITLE: Semi-Supervised Semantic Segmentation via Marginal Contextual Information

ABSTRACT: We present a novel confidence refinement scheme that enhances pseudo-labels in semi-supervised semantic segmentation. Unlike current leading methods, which filter pixels with low-confidence predictions in isolation, our approach leverages the spatial correlation of labels in segmentation maps by grouping neighboring pixels and considering their pseudo-labels collectively. With this contextual information, our method, named S4MC, increases the amount of unlabeled data used during training while maintaining the quality of the pseudo-labels, all with negligible computational overhead. Through extensive experiments on standard benchmarks, we demonstrate that S4MC outperforms existing state-of-the-art semi-supervised learning approaches, offering a promising solution for reducing the cost of acquiring dense annotations. For example, S4MC achieves a  1.29 mIoU improvement over the prior state-of-the-art method on PASCAL VOC 12 with 366 annotated images. The code to reproduce our experiments is available at https://s4mcontext.github.io/

## item_id: m_1602

TITLE: Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer

ABSTRACT: Transformer-based video diffusion models (VDMs) deliver state-of-the-art video generation quality but are constrained by the quadratic cost of self-attention, making long sequences and high resolutions computationally expensive. While linear attention offers sub-quadratic complexity, prior attempts fail to match the expressiveness of softmax attention without costly retraining. We introduce Attention Surgery, an efficient framework for linearizing or hybridizing attention in pretrained VDMs without training from scratch. Inspired by recent advances in language models, our method combines a novel hybrid attention mechanism—mixing softmax and linear tokens—with a lightweight distillation and fine-tuning pipeline requiring only a few GPU-days. Additionally, we incorporate a cost-aware block-rate strategy to balance expressiveness and efficiency across layers. Applied to Wan2.1 1.3B, a state-of-the-art DiT-based VDM, Attention Surgery achieves the first competitive sub-quadratic attention video diffusion models, reducing attention cost by up to 40\% in terms of FLOPs, while maintaining generation quality as measured on the standard VBench and VBench-2.0 benchmarks.

## item_id: m_1603

TITLE: Long-Term 3D Point Tracking By Cost Volume Fusion

ABSTRACT: Long-term point tracking is essential to understand  non-rigid motion in the physical world better. Deep learning approaches have recently been incorporated into long-term point tracking, but most prior work predominantly functions in 2D. Although these methods benefit from the well-established backbones and matching frameworks, the motions they produce do not always make sense in the 3D physical world. In this paper, we propose the first deep learning framework for long-term point tracking in 3D that generalizes to new points and videos without requiring test-time fine-tuning. Our model contains a cost volume fusion module that effectively integrates multiple past appearances and motion information via a transformer architecture, significantly enhancing overall tracking performance. In terms of 3D tracking performance, our model significantly outperforms simple scene flow chaining and previous 2D point tracking methods, even if one uses ground truth depth and camera pose to backproject 2D point tracks in a synthetic scenario.

## item_id: m_1604

TITLE: Shape-Tailored Deep Neural Networks Using PDEs for Segmentation

ABSTRACT: We present Shape-Tailored Deep Neural Networks (ST-DNN). ST-DNN extend convolutional networks, which aggregate data from fixed shape (square) neighbor-hoods to compute descriptors, to be defined on arbitrarily shaped regions. This is useful for segmentation applications, where it is desired to have descriptors that aggregate data only within regions of segmentation to avoid mixing data from different regions, otherwise, the descriptors are difficult to group to a unique region.  We formulate these descriptors through partial differential equations (PDE) that naturally generalize convolution to arbitrary regions, and derive the methodology to jointly estimate the segmentation and ST-DNN descriptor. We also show that ST-DNN inherit covariance to translations and rotations from the PDE, a natural property of a segmentation method, which existing CNN based methods lack. ST-DNN are 3-4 order of magnitude smaller than typical CNN. We empirically show that they exceed segmentation performance compared to state-of-the-art CNN-based descriptors using 2-3 orders smaller training sets on the texture segmentation problem.

## item_id: m_1605

TITLE: Robust Text Classifier on Test-Time Budgets

ABSTRACT: In this paper, we design a generic framework for learning a robust text classification model that achieves accuracy comparable to standard full models under test-time
budget constraints. We take a different approach from existing methods and learn to dynamically delete a large fraction of unimportant words by a low-complexity selector such that the high-complexity classifier only needs to process a small fraction of important words. In addition, we propose a new data aggregation method to train the classifier, allowing it to make accurate predictions even on fragmented sequence of words. Our end-to-end method achieves state-of-the-art performance while its computational complexity scales linearly with the small fraction of important words in the whole corpus. Besides, a single deep neural network classifier trained by our framework can be dynamically tuned to different budget levels at inference time.

## item_id: m_1606

TITLE: ContextIF: Enhancing Instruction-Following through Context Reward

ABSTRACT: While supervised fine-tuning (SFT) and preference learning (PL) are widely used to enhance the instruction-following ability of Large Language Models (LLMs), they often struggle to generalize to novel or complex instructions and may compromise the models' general capabilities. In-Context Learning (ICL) emerges as a promising alternative due to its strong generalization without modifying the model's parameters, but its effectiveness is constrained by the reliance on high-quality, manually curated demonstration pools. To overcome this limitation, we propose ContextIF, a reinforcement learning (RL) framework for automatic context generation. Guided by comprehensive context reward, ContextIF is optimized by Group Relative Policy Optimization (GRPO). It aims to generate precise constraint summaries and optimal context demonstrations tailored to given instructions, thereby improving the instruction-following performance of target LLMs. We evaluate ContextIF on multiple representative instruction-following benchmarks using popular open-source LLMs. Experimental results demonstrate that ContextIF achieves substantial performance gains over existing SFT and ICL methods, while also generalizing effectively to unseen constraint conditions. Moreover, ContextIF preserves the parameters and general capabilities of the target models, offering strong adaptability and scalability. Our code is available at https://github.com/ECNU-Text-Computing/ContextIF.

## item_id: m_1607

TITLE: A sparse, fast, and stable representation for multiparameter topological data analysis

ABSTRACT: Topological data analysis (TDA) is a new area of geometric data analysis that focuses on using invariants from algebraic topology to provide multiscale shape descriptors for point clouds.  One of the most important shape descriptors is persistent homology, which studies the topological variations as a filtration parameter changes; a typical parameter is the feature scale.

For many data sets, it is useful to consider varying multiple filtration parameters at once, for example scale and density.  While the theoretical properties of one-parameter persistent homology are well understood, less is known about the multiparameter case.  Of particular interest is the problem of representing multiparameter persistent homology by elements of a vector space for integration with traditional machine learning.

Existing approaches to this problem either ignore most of the multiparameter information to reduce to the one-parameter case or are heuristic and potentially unstable in the face of noise.  In this article, we introduce a general representation framework for multiparameter persistent homology that encompasses previous approaches. We establish theoretical stability guarantees under this framework  as well as efficient algorithms for practical computation, making this framework an applicable and versatile tool for TDA practitioners. We validate our stability results and algorithms with numerical experiments that demonstrate statistical convergence, prediction accuracy, and fast running times on several real data sets. 

## item_id: m_1608

TITLE: Learning Graph Normalization for Graph Neural Networks

ABSTRACT: Graph Neural Networks (GNNs) have emerged as a useful paradigm to process graph-structured data. Usually, GNNs are stacked to multiple layers and the node representations in each layer are computed through propagating and aggre- gating the neighboring node features with respect to the graph. To effectively train a GNN with multiple layers, some normalization techniques are necessary. Though the existing normalization techniques have been shown to accelerate train- ing GNNs, the structure information on the graph is ignored yet. In this paper, we propose two graph-aware normalization methods to effectively train GNNs. Then, by taking into account that normalization methods for GNNs are highly task-relevant and it is hard to know in advance which normalization method is the best, we propose to learn attentive graph normalization by optimizing a weighted combination of multiple graph normalization methods at different scales. By op- timizing the combination weights, we can automatically select the best or the best combination of multiple normalization methods for a specific task. We con- duct extensive experiments on benchmark datasets for different tasks and confirm that the graph-aware normalization methods lead to promising results and that the learned weights suggest the more appropriate normalization methods for specific task

## item_id: m_1609

TITLE: Grafting Vision Transformers

ABSTRACT: Vision Transformers (ViTs) have recently become the state-of-the-art across many computer vision tasks. In contrast to convolutional networks (CNNs), ViTs enable global information sharing even within shallow layers of a network, i.e., among high-resolution features. However, this perk was later overlooked with the success of pyramid architectures such as Swin Transformer, which show better performance-complexity trade-offs. In this paper, we present a simple and efficient add-on component (termed GrafT) that considers global dependencies and multi-scale information throughout the network, in both high- and low-resolution features alike. GrafT can be easily adopted in both homogeneous and pyramid Transformers while showing consistent gains. It has the flexibility of branching- out at arbitrary depths, widening a network with multiple scales. This grafting operation enables us to share most of the parameters and computations of the backbone, adding only minimal complexity, but with a higher yield. In fact, the process of progressively compounding multi-scale receptive fields in GrafT enables communications between local regions. We show the benefits of the proposed method on multiple benchmarks, including image classification (ImageNet-1K), semantic segmentation (ADE20K), object detection and instance segmentation (COCO2017). Our code and models will be made available.

## item_id: m_1610

TITLE: Understanding Intrinsic Robustness Using Label Uncertainty

ABSTRACT: A fundamental question in adversarial machine learning is whether a robust classifier exists for a given task. A line of research has made some progress towards this goal by studying the concentration of measure, but we argue standard concentration fails to fully characterize the intrinsic robustness of a classification problem since it ignores data labels which are essential to any classification task. Building on a novel definition of label uncertainty, we empirically demonstrate that error regions induced by state-of-the-art models tend to have much higher label uncertainty than randomly-selected subsets. This observation motivates us to adapt a concentration estimation algorithm to account for label uncertainty, resulting in more accurate intrinsic robustness measures for benchmark image classification problems.

## item_id: m_1611

TITLE: Learning Object Affordance with Contact and Grasp Generation

ABSTRACT: Understanding object affordance can help in designing better and more robust robotic grasping. Existing work in the computer vision community formulates the object affordance understanding as a grasping pose generation problem, which treats the problem as a black box by learning a mapping between objects and the distributions of possible grasping poses for the objects. On the other hand, in the robotics community, estimating object affordance represented by contact maps is of the most importance as localizing the positions of the possible affordance can help the planning of grasping actions. In this paper, we propose to formulate the object affordance understanding as both contacts and grasp poses generation. we factorize the learning task into two sequential stages, rather than the black-box strategy: (1) we first reason the contact maps by allowing multi-modal contact generation; (2) assuming that grasping poses are fully constrained given contact maps, we learn a one-to-one mapping from the contact maps to the grasping poses. Further, we propose a penetration-aware partial optimization from the intermediate contacts. It combines local and global optimization for the refinement of the partial poses of the generated grasps exhibiting penetration. Extensive validations on two public datasets show our method outperforms state-of-the-art methods regarding grasp generation on various metrics.

## item_id: m_1612

TITLE: Cyclic Graph Dynamic Multilayer Perceptron for Periodic Signals

ABSTRACT: We propose a feature extraction for periodic signals. Virtually every mechanized transportation vehicle, power generation, industrial machine, and robotic system contains rotating shafts. It is possible to collect data about periodicity by mea- suring a shaft’s rotation. However, it is difficult to perfectly control the collection timing of the measurements. Imprecise timing creates phase shifts in the resulting data. Although a phase shift does not materially affect the measurement of any given data point collected, it does alter the order in which all of the points are col- lected. It is difficult for classical methods, like multi-layer perceptron, to identify or quantify these alterations because they depend on the order of the input vectors’ components. This paper proposes a robust method for extracting features from phase shift data by adding a graph structure to each data point and constructing a suitable machine learning architecture for graph data with cyclic permutation. Simulation and experimental results illustrate its effectiveness.

## item_id: m_1613

TITLE: Brain Mapping with Dense Features: Grounding Cortical Semantic Selectivity in Natural Images With Vision Transformers

ABSTRACT: We introduce BrainSAIL (Semantic Attribution and Image Localization), a method for linking neural selectivity with spatially distributed semantic visual concepts in natural scenes. BrainSAIL leverages recent advances in large-scale artificial neural networks, using them to provide insights into the functional topology of the brain. To overcome the challenge presented by the co-occurrence of multiple categories in natural images, BrainSAIL exploits semantically consistent, dense spatial features from pre-trained vision models, building upon their demonstrated ability to robustly predict neural activity. This method derives clean, spatially dense embeddings without requiring any additional training, and employs a novel denoising process that leverages the semantic consistency of images under random augmentations. By unifying the space of whole-image embeddings and dense visual features and then applying voxel-wise encoding models to these features, we enable the identification of specific subregions of each image which drive selectivity patterns in different areas of the higher visual cortex. This provides a powerful tool for dissecting the neural mechanisms that underlie semantic visual processing for natural images. We validate BrainSAIL on cortical regions with known category selectivity, demonstrating its ability to accurately localize and disentangle selectivity to diverse visual concepts. Next, we demonstrate BrainSAIL's ability to characterize high-level visual selectivity to scene properties and low-level visual features such as depth, luminance, and saturation, providing insights into the encoding of complex visual information. Finally, we use BrainSAIL to directly compare the feature selectivity of different brain encoding models across different regions of interest in visual cortex. Our innovative method paves the way for significant advances in mapping and decomposing high-level visual representations in the human brain.

## item_id: m_1614

TITLE: Long Short-Term Memory as a Dynamically Computed Element-wise Weighted Sum

ABSTRACT: Long short-term memory networks (LSTMs) were introduced to combat vanishing gradients in simple recurrent neural networks (S-RNNs) by augmenting them with additive recurrent connections controlled by gates. We present an alternate view to explain the success of LSTMs: the gates themselves are powerful recurrent models that provide more representational power than previously appreciated. We do this by showing that the LSTM's gates can be decoupled from the embedded S-RNN, producing a restricted class of RNNs where the main recurrence computes an element-wise weighted sum of context-independent functions of the inputs. Experiments on a range of challenging NLP problems demonstrate that the simplified gate-based models work substantially better than S-RNNs, and often just as well as the original LSTMs, strongly suggesting that the gates are doing much more in practice than just alleviating vanishing gradients.

## item_id: m_1615

TITLE: Conditional Networks

ABSTRACT: In this work we tackle the problem of out-of-distribution generalization through conditional computation. Real-world applications often exhibit a larger distributional shift between training and test data than most datasets used in research. On the other hand, training data in such applications often comes with additional annotation. We propose a method for leveraging this extra information by using an auxiliary network that modulates activations of the main network.  We show that this approach improves performance over a strong baseline on the Inria Aerial Image Labeling and the Tumor-Infiltrating Lymphocytes (TIL) Datasets, which by design evaluate out-of-distribution generalization in both semantic segmentation and image classification.

## item_id: m_1616

TITLE: Do GANs learn the distribution? Some Theory and Empirics

ABSTRACT: Do GANS (Generative Adversarial Nets) actually learn the target distribution? The foundational paper of Goodfellow et al. (2014) suggested they do, if they were given sufficiently large deep nets, sample size, and computation time. A recent theoretical analysis in Arora et al. (2017) raised doubts whether the same holds when discriminator has bounded size. It showed that the training objective can approach its optimum value even if the generated distribution has very low support. In other words, the training objective is unable to prevent mode collapse. The current paper makes two contributions. (1) It proposes a novel test for estimating support size using the birthday paradox of discrete probability. Using this  evidence is presented that well-known GANs approaches do learn distributions of fairly low support.  (2) It theoretically studies encoder-decoder GANs architectures (e.g., BiGAN/ALI), which were proposed to learn more meaningful features via GANs, and consequently to also solve the mode-collapse issue. Our result shows that such encoder-decoder training objectives also cannot guarantee learning of the full distribution because they cannot prevent serious mode collapse. More seriously, they cannot prevent learning meaningless codes for data, contrary to usual intuition.

## item_id: m_1617

TITLE: Explaining Contrastive Models using Exemplars: Explanation, Confidence, and Knowledge Limits

ABSTRACT: Explainable AI (XAI) provides human users with transparency and interpretability of powerful ``black-box'' models. Recent work on XAI has focused on explaining specific model responses by identifying key input features using attribution analysis. Another avenue for explaining AI decisions is to leverage exemplars of training data. However, there are limited investigations on using exemplars to establish metrics for confidence and knowledge limits. Recently, contrastive learning has received increased focus in computer vision, natural language, audio, and many other fields. However, there are very few explainability studies that could leverage the learning process to explain the contrastive models. In this paper, we advance post-hoc explainable AI for contrastive models. The main contributions include i) explaining the relation among test and training data samples using pairwise attribution analysis, ii) developing exemplar-based confidence metrics, and iii) establishing measures for the model knowledge limits. In the experimental evaluation, we evaluate the proposed techniques using the OpenAI CLIP model. The evaluation on ImageNet demonstrates that exemplars of training data can provide meaningful explanations for the decision-making of contrastive models. We observe that the proposed exemplar-based confidence score gives a more reliable, dataset-agnostic probability measure compared to the softmax score and temperature scaling. Furthermore, the OOD detection module of our framework shows significant improvement compared to other state-of-the-art methods (6.1\% and 9.6\% improvement in AUROC and FPR@95TPR, respectively). The three modules together can give a meaningful explanation of the model decisions made by a contrastive model. The proposed techniques extend the body of science of XAI for contrastive models and are expected to impact the explainability of future foundational models.

## item_id: m_1618

TITLE: Bayesian Metric Learning for Robust Training of Deep Models under Noisy Labels

ABSTRACT: Label noise is a natural event of data collection and annotation and has been shown to have significant impact on the performance of deep learning models regarding accuracy reduction and sample complexity increase. This paper aims to develop a novel theoretically sound Bayesian deep metric learning that is robust against noisy labels. 
Our proposed approach is inspired by a linear Bayesian large margin nearest neighbor classification, and is a combination of Bayesian learning, triplet loss-based deep metric learning and variational inference frameworks. We theoretically show the robustness under label noise of our proposed method. The experimental results on benchmark data sets that contain both synthetic and realistic label noise show a considerable improvement in the classification accuracy of our method compared to the linear Bayesian metric learning and the point estimate deep metric learning.

## item_id: m_1619

TITLE: T-MARS: Improving Visual Representations by Circumventing Text Feature Learning

ABSTRACT: Large web-crawled multimodal datasets have powered a slew of new methods for learning general-purpose visual representations, advancing the state of the art in computer vision and revolutionizing zero- and few-shot recognition. One crucial decision facing practitioners is how, if at all, to curate these ever-larger datasets. For example, the creators of the LAION-5B dataset chose to retain only image-caption pairs whose CLIP similarity score exceeded a designated threshold. In this paper, we propose a new state-of-the-art data filtering approach motivated by our observation that nearly $40\%$ of LAION's images contain text that overlaps significantly with the caption. Intuitively, such data could be wasteful as it incentivizes models to perform optical character recognition rather than learning visual features. However, naively removing all such data could also be wasteful, as it throws away images that contain visual features (in addition to overlapping text). Our simple and scalable approach, T-MARS (Text Masking and Re-Scoring), filters out only those pairs where the text dominates the remaining visual features---by first masking out the text and then filtering out those with a low CLIP similarity score of the masked image with original captions. Experimentally, T-MARS is the top ranked approach on Imagenet at ``medium scale'' of DataComp (a data filtering benchmark), and outperforms CLIP filtering by a margin of $6.5\%$ on ImageNet and $4.7\%$ on VTAB. Additionally, we show that the accuracy gains enjoyed by T-MARS linearly increase as data and compute are scaled exponentially.

## item_id: m_1620

TITLE: Dynamic Steerable Frame Networks

ABSTRACT: Filters in a convolutional network are typically parametrized in a pixel basis. As an orthonormal basis, pixels may represent any arbitrary vector in Rn. In this paper, we relax this orthonormality requirement and extend the set of viable bases to the generalized notion of frames. When applying suitable frame bases to ResNets on Cifar-10+ we demonstrate improved error rates by substitution only. By exploiting the transformation properties of such generalized bases, we arrive at steerable frames, that allow to continuously transform CNN filters under arbitrary Lie-groups. Further allowing us to locally separate pose from canonical appearance. We implement this in the Dynamic Steerable Frame Network, that dynamically estimates the transformations of filters, conditioned on its input. The derived method presents a hybrid of Dynamic Filter Networks and Spatial Transformer Networks that can be implemented in any convolutional architecture, as we illustrate in two examples. First, we illustrate estimation properties of steerable frames with a Dynamic Steerable Frame Network, compared to a Dynamic Filter Network on the task of edge detection, where we show clear advantages of the derived steerable frames. Lastly, we insert the Dynamic Steerable Frame Network as a module in a convolutional LSTM on the task of limited-data hand-gesture recognition from video and illustrate effective dynamic regularization and show clear advantages over Spatial Transformer Networks. In this paper, we have laid out the foundations of Frame-based convolutional networks and Dynamic Steerable Frame Networks while illustrating their advantages for continuously transforming features and data-efficient learning.

## item_id: m_1621

TITLE: Enhancing Event Camera Data Pretraining via Prompt-Tuning with Visual Models

ABSTRACT: The pretraining-finetuning paradigm has achieved remarkable success in natural language processing and computer vision, becoming the dominant approach in many downstream tasks. However, its application in the event camera domain has encountered significant challenges. First, the scarcity and sparsity of large-scale event datasets lead to issues like overfitting during extensive pretraining. Second, event data inherently contains both temporal and spatial information, making it difficult to directly transfer knowledge from image-based pretraining to event camera tasks.
In this paper, we propose a low-parameter-cost SpatioTemporal Information Fusion Prompting (STP) method to address these challenges. This method enables bidirectional fusion of event and image data while mitigating the risk of overfitting. Specifically, the key innovation lies in effectively integrating the spatio-temporal information of event data to align with pre-trained image models and reduce the impact of data sparsity.
To achieve this, we designed an Overlap Patch Embedding module within the STP, which employs wide receptive field to capture more local information and reduce the influence of sparse regions. Additionally, we introduce a Temporal Transformer that integrates both global and local information, facilitating the fusion of temporal and spatial data. Our approach significantly outperforms previous state-of-the-art methods across multiple downstream tasks, including classification, semantic segmentation, and optical flow estimation. For instance, it achieves a top-1 accuracy of 68.83% on N-ImageNet with fewer trainable parameters. Our code is available in the Supplement.

## item_id: m_1622

TITLE: A Bayes-Optimal View on Adversarial Examples

ABSTRACT: Adversarial attacks on CNN classifiers can make an imperceptible change to an input image and alter the classification result. The source of these failures is still poorly understood, and many explanations invoke the "unreasonably linear extrapolation" used by CNNs along with the geometry of high dimensions.
In this paper we show that similar attacks can be used against the Bayes-Optimal classifier for certain class distributions, while for others the optimal classifier is robust to such attacks. We present analytical results showing conditions on the data distribution under which all points can be made arbitrarily close to the optimal decision boundary and show that this can happen even when the classes are easy to separate, when the ideal classifier has a smooth decision surface and when the data lies in low dimensions. We introduce new datasets of realistic images of faces and digits where the Bayes-Optimal classifier can be calculated efficiently and show that for some of these datasets the optimal classifier is robust and for others it is vulnerable to adversarial examples. In systematic experiments with many such datasets, we find that standard CNN training consistently finds a vulnerable classifier even when the optimal classifier is robust while large-margin methods often find a robust classifier with the exact same training data. Our results suggest that adversarial vulnerability is not an unavoidable consequence of machine learning in high dimensions, and may often be a result of suboptimal training methods used in current practice.

## item_id: m_1623

TITLE: Agent as Scientist: Learning to Verify Hypotheses

ABSTRACT: In this paper, we formulate hypothesis verification as a reinforcement learning problem. Specifically, we aim to build an agent that, given a hypothesis about the dynamics of the world can take actions to generate observations which can help predict whether the hypothesis is true or false. Our first observation is that agents trained end-to-end with the reward fail to learn to solve this problem. In order to train the agents, we exploit the underlying structure in the majority of hypotheses -- they can be formulated as triplets (pre-condition, action sequence,  post-condition). Once the agents have been pretrained to verify hypotheses with this structure, they can be fine-tuned to verify more general hypotheses.  Our work takes a step towards a ``scientist agent'' that develops an understanding of the world by generating and testing hypotheses about its environment.

## item_id: m_1624

TITLE: Learn what you can't learn: Regularized Ensembles for Transductive out-of-distribution detection

ABSTRACT: Machine learning models are often used in practice once they achieve good generalization results on in-distribution (ID) holdout data. To predict test sets in the wild, they should detect samples they cannot predict well. We show that current out-of-distribution (OOD) detection algorithms for neural networks produce unsatisfactory results in a variety of OOD detection scenarios, e.g.\ when OOD data consists of unseen classes or corrupted measurements. This paper studies how such ``hard'' OOD scenarios can benefit from tuning the detection method after observing a batch of the test data. This \emph{transductive} setting is relevant when the advantage of even a slightly delayed OOD detection outweighs the financial cost for additional tuning. We propose a novel method that uses an artificial labeling scheme for the test data and early stopping regularization to obtain ensembles of models that produce contradictory predictions only on the OOD samples in a test batch. We show via comprehensive experiments that our approach is indeed able to significantly outperform both inductive and transductive baselines on difficult OOD detection scenarios, such as unseen classes on CIFAR-10/CIFAR-100, severe corruptions (CIFAR-C), and strong covariate shift ImageNet vs ObjectNet.

## item_id: m_1625

TITLE: Revisiting GNNs for Boolean Satisfiability

ABSTRACT: We introduce a number of enhancements for the training and inference procedure of Graph Neural Networks that are trained to predict solutions of combinatorial problems. We motivate these enhancements by pointing to possible connections to two approximation algorithms studied in the domain of Boolean Satisfiability: Belief Propagation and Semidefinite Programming Relaxations. The first significant enhancement is a curriculum training procedure, which incrementally increases the problem complexity in the training set together with increasing the number of message passing iterations of the Graph Neural Network. We show that the curriculum, together with several other optimizations, reduces training time by more than an order of magnitude compared to the baseline without the curriculum. Furthermore, we apply decimation and initial embedding sampling, which significantly increases the percentage of solved problems.

## item_id: m_1626

TITLE: How to prepare your task head for finetuning

ABSTRACT: In the era of deep learning, transferring information from a pretrained network to a downstream task by finetuning has many benefits. The choice of task head plays an important role in fine-tuning, as the pretrained and downstream tasks are usually different. Although there exist many different designs for finetuning, a full understanding of when and why these algorithms work has been elusive. We analyze how the choice of task head controls feature adaptation and hence influences the downstream performance.  By decomposing the feature's learning dynamics, we find the key aspect is the training accuracy and loss at the beginning of finetuning, which determines the "energy" available for the feature's adaptation. We identify a significant trend in the effect of changes in this initial energy on the resulting features after finetuning. Specifically, as the energy increases, the Euclidean and cosine distances between the resulting and original features increase, while their dot product (and the resulting features’ norm) first increases and then decreases. Inspired by this, we give several practical principles that lead to better downstream performance. We analytically prove this trend in an overparamterized linear setting and verify its applicability to different experimental settings.

## item_id: m_1627

TITLE: Exploring Sentence Vectors Through Automatic Summarization

ABSTRACT: Vector semantics, especially sentence vectors, have recently been used successfully in many areas of natural language processing. However, relatively little work has explored the internal structure and properties of spaces of sentence vectors. In this paper, we will explore the properties of sentence vectors by studying a particular real-world application: Automatic Summarization. In particular, we show that cosine similarity between sentence vectors and document vectors is strongly correlated with sentence importance and that vector semantics can identify and correct gaps between the sentences chosen so far and the document. In addition, we identify specific dimensions which are linked to effective summaries. To our knowledge, this is the first time specific dimensions of sentence embeddings have been connected to sentence properties. We also compare the features of different methods of sentence embeddings. Many of these insights have applications in uses of sentence embeddings far beyond summarization.

## item_id: m_1628

TITLE: Safe In-Context Reinforcement Learning

ABSTRACT: In-context reinforcement learning (ICRL) is an emerging RL paradigm where the agent, after some pretraining procedure, is able to adapt to out-of-distribution test tasks without any parameter updates.
The agent achieves this by continually expanding the input (i.e., the context) to its policy neural networks.
For example,
the input could be all the history experience that the agent has access to until the current time step. 
The agent's performance improves as the input grows, without any parameter updates.
In this work,
we propose the first method that promotes the safety of ICRL's adaptation process in the framework of constrained Markov Decision Processes.
In other words,
during the parameter-update-free adaptation process,
the agent not only maximizes the reward but also minimizes an additional cost function.
We also demonstrate\footnote{All the implementations will be made publicly available and are now located in the supplementary materials.} that our agent actively reacts to the threshold (i.e., budget) of the cost tolerance.
With a higher cost buget, the agent behaves more aggressively, and with a lower cost budget, the agent behaves more conservatively.

## item_id: m_1629

TITLE: On the Role of General Function Approximation in Offline Reinforcement Learning

ABSTRACT: We study offline reinforcement learning (RL) with general function approximation. General function approximation is a powerful tool for algorithm design and analysis, but its adaptation to offline RL encounters several challenges due to varying approximation targets and assumptions that blur the real meanings of function assumptions. In this paper, we try to formulate and clarify the treatment of general function approximation in offline RL in two aspects: (1) analyzing different types of assumptions and their practical usage, and (2) understanding its role as a restriction on underlying MDPs from information-theoretic perspectives. Additionally, we introduce a new insight for lower bound establishing: one can exploit model-realizability to establish general-purpose lower bounds that can be generalized into other functions. Building upon this insight, we propose two generic lower bounds that contribute to a better understanding of offline RL with general function approximation.

## item_id: m_1630

TITLE: LMSA: Low-relation Mutil-head Self-Attention Mechanism in Visual Transformer

ABSTRACT: The Transformer backbone network with the self-attention mechanism as the core has achieved great success in the field of natural language processing and computer vision. However, through the self-attention mechanism brings high performance, it also brings higher computational complexity compared to the classic visual feature extraction methods. To further reduce the complexity of self-attention mechanism and explore its lighter version in computer vision, in this paper, we design a novel lightweighted self-attention mechanism: Low-relation Mutil-head Self-Attention (LMSA), which is superior than the recent self-attention. Specifically, the proposed self-attention mechanism breaks the barrier of the dimensional consistency of the traditional self-attention mechanism, resulting in lower computational complexity and occupies less storage space. In addition, employing the new mechanism can release part of the computing consumption of the Transformer network and  make the best use of it. Experimental results show that the dimensional consistency inside the traditional self-attention mechanism is unnecessary. In particular, using Swin as the backbone model for training, the accuracy in CIFAR-10 image classification task is improved by 0.43$\%$, in the meanwhile, the consumption of a single self-attention resource is reduced by 64.58$\%$, and the number of model parameters and model size are reduced by more than 15$\%$. By appropriately compressing the dimensions of the self-attention relationship variables, the Transformer network can be more efficient and even perform better. The results prompt us to rethink the reason why the self-attention mechanism works.

## item_id: m_1631

TITLE: Structural Multi-agent Learning

ABSTRACT: In this paper, we propose a multi-agent learning framework to model communication in complex multi-agent systems. Most existing multi-agent reinforcement learning methods require agents to exchange information with the environment or global manager to achieve effective and efficient interaction. We model the multi-agent system with an online adaptive graph where all agents communicate with each other through the edges. We update the graph network with a relation system which takes the current graph network and the hidden variable of agents as input. Messages and rewards are shared through the graph network. Finally, we optimize the whole system via the policy gradient algorithm. Experimental results of several multi-agent systems show the efficiency of the proposed method and its strength compared to existing methods in cooperative scenarios.

## item_id: m_1632

TITLE: A   RECURRENT NEURAL CASCADE-BASED MODEL FOR CONTINUOUS-TIME DIFFUSION PROCESS

ABSTRACT: Many works have been proposed in the literature to capture the dynamics of diffusion in networks. While some of them define graphical markovian models to extract temporal relationships between node infections in networks, others consider diffusion episodes as sequences of infections via recurrent neural models. In this paper we propose a model at the crossroads of these two extremes, which embeds the history of diffusion in infected nodes as hidden continuous states. Depending on the trajectory followed by the content before reaching a given node, the distribution of influence probabilities may vary. However, content trajectories  are usually hidden in the data, which induces challenging learning problems. We propose a topological recurrent neural model which exhibits good experimental performances for diffusion modelling and prediction. 

## item_id: m_1633

TITLE: Debiasing Attention Mechanism in Transformer without Demographics

ABSTRACT: Although transformers demonstrate impressive capabilities in a variety of tasks, the fairness issue remains a significant concern when deploying these models. Existing works to address fairness issues in transformers require sensitive labels (such as age, gender, etc.), which can raise privacy concerns or violate legal regulations. An alternative way is through fairness without demographics. However, existing works that improve Rawlsian Max-Min fairness may impose overly restrictive constraints. Other methods that use auxiliary networks could be parameter inefficient. In this paper, we present a new approach to debiasing transformers by leveraging their inherent structure.  By reconsidering the roles of important components (queries, keys, and values) in the attention mechanism, we introduce a simple yet effective debiasing strategy from two perspectives: 1) Grounded in theoretical analysis, we normalize and apply absolute value operations to queries and keys to minimize the bias in attention weight allocation; 2) We reduce the bias within values through local alignment via contrastive learning. Throughout the entire process, our approach does not require any sensitive labels. Furthermore, to enhance memory efficiency in the training phase, we propose a strategy that debias only the last encoder to improve fairness in pre-trained models. We conduct experiments in computer vision and natural language processing tasks and show that our method is comparable and even outperforms the state-of-the-art method with substantially lower energy consumption.

## item_id: m_1634

TITLE: Curing the Transitivity Curse: Shortcut Logical Reasoning via A Priori Knowledge Compilation

ABSTRACT: While large language models (LLMs) have shown remarkable reasoning abilities, they often fail at multi-hop logical reasoning tasks that require chaining inferences, struggling to deduce transitive relations like $(P \to R)$ from $(P \to Q) \land (Q \to R)$. This fundamental limitation, which we term the \textbf{``Transitivity Curse''}, leads to brittle reasoning chains and significant error propagation. Existing reasoning frameworks, often based on Chain-of-Thought, attempt to traverse these long paths sequentially, a process that is both inefficient and prone to failure as complexity increases. To cure this curse, we introduce a novel mechanism designed to be integrated into existing logical reasoners. Our mechanism shifts the paradigm from passively traversing reasoning chains to proactively compiling them through a process we call \textbf{A Priori Knowledge Compilation (APKC)}. This process unfolds in two critical phases. First, it employs a goal-oriented backward analysis to identify a focused, relevant subgraph of the knowledge base. Subsequently, within this constrained boundary, our mechanism performs a systematic forward-chaining process to synthesize new knowledge in the form of both foundational \textbf{derived facts} and powerful \textbf{composite rules}. This compiled knowledge collapses multi-step inferences into fewer, more robust steps.By allowing a host framework to leverage this compiled knowledge, our mechanism enables a more direct form of \textbf{Shortcut Reasoning}, drastically reducing the required depth of runtime inference. Experiments show that when integrated into state-of-the-art reasoning frameworks, our mechanism consistently and significantly boosts their performance on several logical reasoning benchmarks. Our findings demonstrate that APKC, as a plug-in mechanism, is a critical component for making existing LLM-based reasoners more robust, efficient, and trustworthy.

## item_id: m_1635

TITLE: Recurrent Real-valued Neural Autoregressive Density Estimator for Online Density Estimation and Classification of Streaming Data

ABSTRACT: In contrast with the traditional offline learning, where complete data accessibility is assumed, many modern applications involve processing data in a streaming fashion. This online learning setting raises various challenges, including concept drift, hardware memory constraints, etc. In this paper, we propose the Recurrent Real-valued Neural Autoregressive Density Estimator (RRNADE), a flexible density-based model for online classification and density estimation. RRNADE combines a neural Gaussian mixture density module with a recurrent module. This combination allows RRNADE to exploit possible sequential correlations in the streaming task, which are often ignored in the classical streaming setting where each input is assumed to be independent from the previous ones. We showcase the ability of RRNADE to adapt to concept drifts on synthetic density estimation tasks. We also apply RRNADE to online classification tasks on both real world and synthetic datasets and compare it with multiple density based as well as nondensity based online classification methods. In almost all of these tasks, RRNADE outperforms the other methods. Lastly, we conduct an ablation study demonstrating the complementary benefits of the density and the recurrent modules.

## item_id: m_1636

TITLE: End-to-end Learning of a Convolutional Neural Network via Deep Tensor Decomposition

ABSTRACT: In this paper we study the problem of learning the weights of a deep convolutional neural network. We consider a network where convolutions are carried out over non-overlapping patches with a single kernel in each layer. We develop an algorithm for simultaneously learning all the kernels from the training data. Our approach dubbed Deep Tensor Decomposition (DeepTD) is based on a rank-1 tensor decomposition. We theoretically investigate DeepTD under a realizable model for the training data where the inputs are chosen i.i.d. from a Gaussian distribution and the labels are generated according to planted convolutional kernels. We show that DeepTD is data-efficient and provably works as soon as the sample size exceeds the total number of convolutional weights in the network. Our numerical experiments demonstrate the effectiveness of DeepTD and verify our theoretical findings.

## item_id: m_1637

TITLE: SOMA: Efficient Multi-turn LLM Serving via Small Language Model

ABSTRACT: Large Language Models (LLMs) are increasingly deployed in multi-turn dialogue settings where preserving conversational context across turns is essential. A standard serving practice concatenates the full dialogue history at every turn, which reliably maintains coherence but incurs substantial cost in latency, memory, and API expenditure, especially when queries are routed to large proprietary models. Existing approaches often struggle to balance the trade-off between response quality and efficiency. We propose a framework that exploits the early turns of a session to estimate a local response manifold and then adapt a smaller surrogate model to this local region for the remainder of the conversation. Concretely, we learn soft prompts that maximize semantic divergence between the large and surrogate small language models' responses to surface least-aligned local directions, stabilize training with anti-degeneration control, and distill the mined cases into localized LoRA fine-tuning so the surrogate runs without prompts at inference. A simple gate enables a one-time switch with rollback on drift. We further provide a theoretical analysis for key components in SOMA. Extensive experiments show the effectiveness of SOMA. The source code is provided at: https://anonymous.4open.science/r/SOMA-D377.

## item_id: m_1638

TITLE: Fair Mixup: Fairness via Interpolation

ABSTRACT: Training classifiers under fairness constraints such as group fairness, regularizes the disparities of predictions between the groups. Nevertheless, even though the constraints are satisfied during training, they might not generalize at evaluation time. To improve the generalizability of fair classifiers, we propose fair mixup, a new data augmentation strategy for imposing the fairness constraint. In particular, we show that fairness can be achieved by regularizing the models on paths of interpolated samples  between the groups. We use mixup, a powerful data augmentation strategy  to generate these interpolates. We analyze fair mixup and empirically show that it ensures a better generalization for both accuracy and fairness measurement in tabular, vision, and language benchmarks.

## item_id: m_1639

TITLE: ActiveDPO: Active Direct Preference Optimization for Sample-Efficient Alignment

ABSTRACT: The recent success in using human preferences to align large language models (LLMs) has significantly improved their performance in various downstream tasks, such as question answering, mathematical reasoning, and code generation. However, achieving effective LLM alignment depends on high-quality datasets of human preferences. Collecting these datasets requires human preference annotation, which is costly and resource-intensive, necessitating efficient active data selection methods. Existing methods either lack a strong theoretical foundation or depend on restrictive assumptions about the reward function, such as linear latent reward functions. To this end, we propose an algorithm, ActiveDPO, that uses a theoretically grounded data selection criterion for non-linear reward functions while directly leveraging the LLM itself to parameterize the reward model used for active data selection. As a result, ActiveDPO explicitly accounts for the LLM's influence on data selection, unlike methods that select data without considering the LLM that is being aligned, thereby leading to more effective and efficient data collection. Our extensive experiments demonstrate that ActiveDPO outperforms existing methods across various models and real-world preference datasets.

## item_id: m_1640

TITLE: ConfRAG: Confidence-Guided Retrieval-Augmenting Generation

ABSTRACT: Can Large Language Models (LLMs) be trained to avoid hallucinating factual statements, and can Retrieval-Augmented Generation (RAG) be triggered only when necessary to reduce retrieval and computation costs? In this work, we address both challenges simultaneously. We introduce ConfQA, a fine-tuning strategy that reduces hallucination rates from 20–40% to below 5% across multiple factuality benchmarks. The approach is simple: when the model answers correctly, it is trained to output the answer; otherwise, it is trained to respond with “I am unsure.” Two design choices make this training effective: (1) a dampening prompt (“answer only if you are confident”) that explicitly discourages overconfident hallucinations, and (2) training data drawn from atomic factual statements (e.g., knowledge graph attribute values), which calibrates model confidence and yields robust generalization across domains and question types. Building on ConfQA, we propose ConfRAG, a triggering strategy that invokes RAG only when the model responses with unsure. This framework achieves accuracy above 95% in ideal case while reducing unnecessary external retrievals by over 30%.

## item_id: m_1641

TITLE: IBEX: Information-Bottleneck-EXplored Coarse-to-Fine Molecular Generation under Limited Data

ABSTRACT: The potential of three-dimensional molecular generation for structure-based drug discovery is hampered by the scarcity of public protein-ligand complexes, which causes models to overfit and fail to learn generalizable geometric priors. To address this challenge, we employ the PAC-Bayes information bottleneck framework to systematically quantify the information density of three generation paradigms: Scaffold Hopping (SH), Side-Chain Decoration (SC), and De Novo Design (DN). Our analysis reveals that SH possesses the highest information density, which tightens the model's generalization bound and enhances its transferability compared to conventional de novo generation. Motivated by this finding, we propose IBEX, a novel decoupled generation framework. IBEX is trained exclusively on the information-rich SH task to structure its latent representation of chemical space, which is then directly applied to de novo generation in a zero-shot transfer setting. Subsequently, a rapid physical refinement module utilizes the L-BFGS algorithm to optimize each conformer's geometry and binding compatibility by adjusting five short-range interaction terms and six degrees of freedom. Evaluated in a rigorous zero-shot setting on the CBGBench CrossDocked2020-based dataset, IBEX demonstrates substantial improvements over the TargetDiff baseline. It increases the docking success rate from 53% to 64% and improves the average Dock score from -7.41 to -8.09 kcal/mol. Notably, IBEX achieves a superior median Vina energy in 57 out of 100 binding pockets. Furthermore, IBEX enhances drug-likeness by approximately 25% while maintaining state-of-the-art validity and diversity, all corresponding to a demonstrably reduced generalization error. Our results validate that this decoupled approach, which synergizes information-dense pre-training with physical refinement, enables robust zero-shot structure generation and cross-pocket generalization in data-limited regimes.

## item_id: m_1642

TITLE: UneVEn: Universal Value Exploration for Multi-Agent Reinforcement Learning

ABSTRACT: This paper focuses on cooperative value-based multi-agent reinforcement learning (MARL) in the paradigm of centralized training with decentralized execution (CTDE). Current state-of-the-art value-based MARL methods leverage CTDE to learn a centralized joint-action value function as a monotonic mixing of each agent's utility function, which enables easy decentralization. However, this monotonic restriction leads to inefficient exploration in tasks with nonmonotonic returns due to suboptimal approximations of the values of joint actions. To address this, we present a novel MARL approach called Universal Value Exploration (UneVEn), which uses universal successor features (USFs) to learn policies of tasks related to the target task, but with simpler reward functions in a sample efficient manner. UneVEn uses novel action-selection schemes between randomly sampled related tasks during exploration, which enables the monotonic joint-action value function of the target task to place more importance on useful joint actions. Empirical results on a challenging cooperative predator-prey task requiring significant coordination amongst agents show that UneVEn significantly outperforms state-of-the-art baselines.

## item_id: m_1643

TITLE: BenthIQ: a Transformer-Based Benthic Classification Model for Coral Restoration

ABSTRACT: Coral reefs are vital for marine biodiversity, coastal protection, and supporting human livelihoods globally. However, they are increasingly threatened by mass bleaching events, pollution, and unsustainable practices with the advent of climate change. Monitoring the health of these ecosystems is crucial for effective restoration and management. Current methods for creating benthic composition maps often compromise between spatial coverage and resolution. In this paper, we introduce BenthIQ, a multi-label semantic segmentation network designed for high-precision classification of underwater substrates, including live coral, algae, rock, and sand. Although commonly deployed CNNs are limited in learning long-range semantic information, transformer-based models have recently achieved state-of-the-art performance in vision tasks such as object detection and image classification. We integrate the hierarchical Swin Transformer as the backbone of a U-shaped encoder-decoder architecture for local-global semantic feature learning. Using a real-world case study in French Polynesia, we demonstrate that our approach outperforms traditional CNN and attention-based models on pixel-wise classification of shallow reef imagery.

## item_id: m_1644

TITLE: Change Detection for bi-temporal images classification based on Siamese Variational AutoEncoder and Transfer Learning

ABSTRACT: Siamese structures empower Deep Learning (DL) models to increase their efficiency by learning how to extract the relevant temporal features from the input data.  In this paper, a Siamese Variational Auto-Encoder (VAE) model based on transfer learning (TL) is applied for change detection (CD) using bi-temporal images. The introduced method is trained in a supervised strategy for classification tasks. Firstly, the suggested generative method utilizes two VAEs to extract features from bi-temporal images. Subsequently, concatenates them into a feature vector. To get a classification map of the source scene, the classifier receives this vector and the ground truth data as input. The source model is fine-tuned to be applied to the target scene with less ground truth data using a TL strategy. Experiments were carried out in two study areas in the arid regions of southern Tunisia. The obtained results reveal that the proposed method outperformed the Siamese Convolution Neural Network (SCNN) by achieving an accuracy of more than 98%, in the source scene, and increased the accuracy in the target scene by 1.25% by applying the TL strategy.

## item_id: m_1645

TITLE: Embedded-model flows: Combining the inductive biases of model-free deep learning and explicit probabilistic modeling

ABSTRACT: Normalizing flows have shown great success as general-purpose density estimators. However, many real world applications require the use of domain-specific knowledge, which normalizing flows cannot readily incorporate. We propose embedded-model flows (EMF), which alternate general-purpose transformations with structured layers that embed domain-specific inductive biases. These layers are automatically constructed by converting user-specified differentiable probabilistic models into equivalent bijective transformations. We also introduce gated structured layers, which allow bypassing the parts of the models that fail to capture the statistics of the data. We demonstrate that EMFs can be used to induce desirable properties such as multimodality and continuity. Furthermore, we show that EMFs enable a high performance form of variational inference where the structure of the prior model is embedded in the variational architecture. In our experiments, we show that this approach outperforms a large number of alternative methods in common structured inference problems.

## item_id: m_1646

TITLE: Déjà Vu: An Empirical Evaluation of the Memorization Properties of Convnets

ABSTRACT: Convolutional neural networks memorize part of their training data, which is why strategies such as data augmentation and drop-out are employed to mitigate over- fitting. This paper considers the related question of “membership inference”, where the goal is to determine if an image was used during training. We con- sider membership tests over either ensembles of samples or individual samples.
First, we show how to detect if a dataset was used to train a model, and in particular whether some validation images were used at train time. Then, we introduce a new approach to infer membership when a few of the top layers are not available or have been fine-tuned, and show that lower layers still carry information about the training samples. To support our findings, we conduct large-scale experiments on Imagenet and subsets of YFCC-100M with modern architectures such as VGG and Resnet.


## item_id: m_1647

TITLE: Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling

ABSTRACT: Recurrent neural networks have been very successful at predicting sequences of words in tasks such as language modeling. However, all such models are based on the conventional classification framework, where the model is trained against one-hot targets, and each word is represented both as an input and as an output in isolation. This causes inefficiencies in learning both in terms of utilizing all of the information and in terms of the number of parameters needed to train. We introduce a novel theoretical framework that facilitates better learning in language modeling, and show that our framework leads to tying together the input embedding and the output projection matrices, greatly reducing the number of trainable variables. Our framework leads to state of the art performance on the Penn Treebank with a variety of network models.

## item_id: m_1648

TITLE: Ergodic Measure Preserving Flows

ABSTRACT: Training probabilistic models with neural network components is intractable in most cases and requires to use approximations such as Markov chain Monte Carlo (MCMC), which is not scalable and requires significant hyper-parameter tuning, or mean-field variational inference (VI), which is biased. While there has been attempts at combining both approaches, the resulting methods have some important limitations in theory and in practice. As an alternative, we propose a novel method which is scalable, like mean-field VI, and, due to its theoretical foundation in ergodic theory, is also asymptotically accurate, like MCMC. We test our method on popular benchmark problems with deep generative models and Bayesian neural networks. Our results show that we can outperform existing approximate inference methods.

## item_id: m_1649

TITLE: FedX: Federated Learning for Compositional Pairwise Risk Optimization

ABSTRACT: In this paper, we tackle a novel federated learning (FL) problem for optimizing a family of compositional pairwise risks, to which no existing FL algorithms are applicable. In particular, the objective has the form of $\E_{\z\sim \mathcal S_1} f(\E_{\z'\sim\mathcal S_2} \ell(\w; \z, \z'))$, where two sets of data $\mathcal S_1, \mathcal S_2$ are distributed over multiple machines, $\ell(\cdot; \cdot,\cdot)$ is a pairwise loss that only depends on the prediction outputs of the input data pairs $(\z, \z')$, and $f(\cdot)$ is possibly a non-linear non-convex function. This problem has important applications in machine learning, e.g., AUROC maximization with a pairwise loss, and partial AUROC maximization with a compositional loss, etc. The challenges for designing a FL algorithm lie at the non-decomposability of the objective over multiple machines and the interdependency between different machines. We propose two provable FL algorithms (FedX) for handling linear and nolinear $f$, respectively. To tackle the challenges, we decouple the gradient's components with two types namely active parts and  lazy parts, where the {\it active} parts depend on local data that can be computed with the local model  and the {\it lazy} parts depend on other machines that are communicated/computed based on historical models. We develop a novel theoretical analysis to address the issue of latency of lazy parts and interdependency between the local gradient estimators and the involved data. We establish both iteration and communication complexities and exhibit that using the historical models for computing the lazy parts do not degrade the complexity results. We conduct empirical studies of FedX for AUROC and  partial AUROC maximization, and demonstrate their performance compared with multiple baselines.

## item_id: m_1650

TITLE: Predict Responsibly: Increasing Fairness by Learning to Defer

ABSTRACT: When machine learning models are used for high-stakes decisions, they should predict accurately, fairly, and responsibly. To fulfill these three requirements, a model must be able to output a reject option (i.e. say "``I Don't Know") when it is not qualified to make a prediction. In this work, we propose learning to defer, a method by which a model can defer judgment to a downstream decision-maker such as a human user. We show that learning to defer generalizes the rejection learning framework in two ways: by considering the effect of other agents in the decision-making process, and by allowing for optimization of complex objectives. We propose a learning algorithm which accounts for potential biases held by decision-makerslater in a pipeline. Experiments on real-world datasets demonstrate that learning
to defer can make a model not only more accurate but also less biased. Even when
operated by highly biased users, we show that
deferring models can still greatly improve the fairness of the entire pipeline.

## item_id: m_1651

TITLE: Spectral Synthesis for Satellite-to-Satellite Translation

ABSTRACT: Earth observing satellites carrying multi-spectral sensors are widely used to monitor the physical and biological states of the atmosphere, land, and oceans. These satellites have different vantage points above the earth and different spectral imaging bands resulting in inconsistent imagery from one to another. This presents challenges in building downstream applications. What if we could generate synthetic bands for existing satellites from the union of all domains? We tackle the problem of generating synthetic spectral imagery for multispectral sensors as an unsupervised image-to-image translation problem with partial labels and introduce a novel shared spectral reconstruction loss. Simulated experiments performed by dropping one or more spectral bands show that cross-domain reconstruction outperforms measurements obtained from a second vantage point. On a downstream cloud detection task, we show that generating synthetic bands with our model improves segmentation performance beyond our baseline. Our proposed approach enables synchronization of multispectral data and provides a basis for more homogeneous remote sensing datasets.

## item_id: m_1652

TITLE: Perceptual Deep Neural Networks: Adversarial Robustness Through Input Recreation

ABSTRACT: Adversarial examples have shown that albeit highly accurate, models learned by machines, differently from humans, have many weaknesses. However, humans’ perception is also fundamentally different from machines, because we do not see the signals which arrive at the retina but a rather complex recreation of them. In this paper, we explore how machines could recreate the input as well as investigate the benefits of such an augmented perception. In this regard, we propose Perceptual Deep Neural Networks (ϕDNN) which also recreate their own input before further processing. The concept is formalized mathematically and two variations of it are developed (one based on inpainting the whole image and the other based on a noisy resized super resolution recreation). Experiments reveal that ϕDNNs and their adversarial training variations can increase the robustness substantially, surpassing both state-of-the-art defenses and pre-processing types of defenses in 100% of the tests. ϕDNNs are shown to scale well to bigger image sizes, keeping a similar high accuracy throughout; while the state-of-the-art worsen up to 35%. Moreover, the recreation process intentionally corrupts the input image. Interestingly, we show by ablation tests that corrupting the input is, although counterintuitive, beneficial. Thus, ϕDNNs reveal that input recreation has strong benefits for artificial neural networks similar to biological ones, shedding light into the importance of purposely corrupting the input as well as pioneering an area of perception models based on GANs and autoencoders for robust recognition in artificial intelligence.

## item_id: m_1653

TITLE: Uncertainty Quantification via Stable Distribution Propagation

ABSTRACT: We propose a new approach for propagating stable probability distributions through neural networks. Our method is based on local linearization, which we show to be an optimal approximation in terms of total variation distance for the ReLU non-linearity. This allows propagating Gaussian and Cauchy input uncertainties through neural networks to quantify their output uncertainties. To demonstrate the utility of propagating distributions, we apply the proposed method to predicting calibrated confidence intervals and selective prediction on out-of-distribution data. The results demonstrate a broad applicability of propagating distributions and show the advantages of our method over other approaches such as moment matching.

## item_id: m_1654

TITLE: Solving Diverse Combinatorial Optimization Problems with a Unified Model

ABSTRACT: Combinatorial Optimization (CO) encompasses a wide range of problems that arise in many real-world scenarios. While significant progress has been made in developing learning-based methods for specialized CO problems, a unified model with a single architecture and parameter set for diverse CO problems remains elusive. Such a model would offer substantial advantages in terms of efficiency and convenience. In this paper, we introduce and formalize a unified model for solving various CO problems. Inspired by the success of next-token prediction, we frame each problem-solving process as a Markov Decision Process (MDP), tokenize the corresponding sequential trajectory data, and train the model using a transformer backbone. To reduce token length in the trajectory data, we propose a CO-prefix design that aggregates static problem features. To address the heterogeneity of state and action tokens within the MDP, we employ a two-stage self-supervised learning approach. In this approach, a dynamic prediction model is first trained and then serves as a pre-trained model for subsequent policy generation. Experiments across nine CO problems demonstrate the generic problem-solving capability of our unified model, highlighting its few-shot and even zero-shot ability to generalize to unseen problems through rapid fine-tuning. We believe our framework offers a valuable complement to existing neural CO methods that focus on optimizing performance for individual problems.

## item_id: m_1655

TITLE: Data-driven Feature Sampling for Deep Hyperspectral Classification and Segmentation

ABSTRACT: The high dimensionality of hyperspectral imaging forces unique challenges in scope, size and processing requirements.  Motivated by the potential for an in-the-field cell sorting detector, we examine a Synechocystis sp. PCC 6803 dataset wherein cells are grown alternatively in nitrogen rich or deplete cultures.  We use deep learning techniques to both successfully classify cells and generate a mask segmenting the cells/condition from the background. Further, we use the classification accuracy to guide a data-driven, iterative feature selection method, allowing the design neural networks requiring 90% fewer input features with little accuracy degradation.

## item_id: m_1656

TITLE: A cluster-to-cluster framework for neural machine translation

ABSTRACT: The quality of a machine translation system depends largely on the availability of sizable parallel corpora. For the recently popular Neural Machine Translation (NMT) framework, data sparsity problem can become even more severe. With large amount of tunable parameters, the NMT model may overfit to the existing language pairs while failing to understand the general diversity in language. In this paper, we advocate to broadcast every sentence pair as two groups of similar sentences to incorporate more diversity in language expressions, which we name as parallel cluster. Then we define a more general cluster-to-cluster correspondence score and train our model to maximize this score. Since direct maximization is difficult, we derive its lower-bound as our surrogate objective, which is found to generalize point-point Maximum Likelihood Estimation (MLE) and point-to-cluster Reward Augmented Maximum Likelihood (RAML) algorithms as special cases. Based on this novel objective function, we delineate four potential systems to realize our cluster-to-cluster framework and test their performances in three recognized translation tasks, each task with forward and reverse translation directions. In each of the six experiments, our proposed four parallel systems have consistently proved to outperform the MLE baseline, RL (Reinforcement Learning) and RAML systems significantly. Finally, we have performed case study to empirically analyze the strength of the cluster-to-cluster NMT framework. 

## item_id: m_1657

TITLE: Uncertainty in Gradient Boosting via Ensembles

ABSTRACT: For many practical, high-risk applications, it is essential to quantify uncertainty in a model's predictions to avoid costly mistakes. While predictive uncertainty is widely studied for neural networks, the topic seems to be under-explored for models based on gradient boosting. However, gradient boosting often achieves state-of-the-art results on tabular data. This work examines a probabilistic ensemble-based framework for deriving uncertainty estimates in the predictions of gradient boosting classification and regression models. We conducted experiments on a range of synthetic and real datasets and investigated the applicability of ensemble approaches to gradient boosting models that are themselves ensembles of decision trees. Our analysis shows that ensembles of gradient boosting models successfully detect anomalous inputs while having limited ability to improve the predicted total uncertainty. Importantly, we also propose a concept of a virtual ensemble to get the benefits of an ensemble via only one gradient boosting model, which significantly reduces complexity. 

## item_id: m_1658

TITLE: An Efficient Variational Method for Fitting Log-Gaussian Cox Processes

ABSTRACT: Log-Gaussian Cox Processes (LGCP) have been widely used for modeling spatial point patterns. However, fitting LGCP is computationally challenging due to a nested structure involving Poisson process and latent Gaussian random field. To address these issues, we first approximate the intractable LGCP likelihood  based on the Voronoi tessellation method. Then, using variational Gaussian approximation, we transform the problem of fitting LGCP into maximizing the evidence lower bound which admits an explicit expression. We design a novel coordinate ascent maximization algorithm which updates the parameter blocks by Newton method and fixed-point method, respectively. To further enhance the computational efficiency, we adopt a nearest neighbor Gaussian process as the prior for the latent Gaussian random field, and the cost of inverting large covariance matrices is greatly reduced via the Woodbury formula. Theoretically, we prove the existence and uniqueness of the optimal solution to the strongly concave objective function, and the convergence of the proposed algorithm is established. Numerical results demonstrate the computational and inferential benefits of our method in modeling log-intensity surface over competing methods.

## item_id: m_1659

TITLE: Stochastic Variational Video Prediction

ABSTRACT: Predicting the future in real-world settings, particularly from raw sensory observations such as images, is exceptionally challenging. Real-world events can be stochastic and unpredictable, and the high dimensionality and complexity of natural images requires the predictive model to build an intricate understanding of the natural world. Many existing methods tackle this problem by making simplifying assumptions about the environment. One common assumption is that the outcome is deterministic and there is only one plausible future. This can lead to low-quality predictions in real-world settings with stochastic dynamics. In this paper, we develop a stochastic variational video prediction (SV2P) method that predicts a different possible future for each sample of its latent variables. To the best of our knowledge, our model is the first to provide effective stochastic multi-frame prediction for real-world video. We demonstrate the capability of the proposed method in predicting detailed future frames of videos on multiple real-world datasets, both action-free and action-conditioned. We find that our proposed method produces substantially improved video predictions when compared to the same model without stochasticity, and to other stochastic video prediction methods. Our SV2P implementation will be open sourced upon publication.

## item_id: m_1660

TITLE: TACD-GRU: Time-Aware Context-Dependent Autoregressive Model for Irregularly Sampled Time Series

ABSTRACT: Multivariate time series data and their models are extremely important for under-
standing the behavior of various natural and man-made systems. Development of
accurate time series models often requires capturing intricate relationships among
the variables and their dynamics. Particularly challenging to model and learn
are time series with irregular and sparse observations, that may arise in domains
as diverse as healthcare, sensor and communication networks. In this work, we
propose and study TACD-GRU, a new Time- Aware Context-Dependent Gated
Recurrent Unit framework for multivariate time series prediction (or forecasting)
that accounts for irregularities in observation times of individual time series vari-
ables and their dependencies. Our framework defines a novel sequential unit that
is triggered by the arrival of a new observation to update its state, and a predic-
tion module that supports time series predictions at any future time. The current
prediction module consists of and combines two novel prediction models: (i) a
context-based model (TACD-GRU-CONTEXT) that relies on a set of tunable latent
decay functions of time and their linear combinations to support the prediction,
and (ii) an attention-based model (TACD-GRU-ATTENTION) that models depen-
dencies among variables and their most recent values using a temporal attention
mechanism. Our model shows highly competitive performance when powered by
both individual and combined prediction functions outperforming existing state-of-
the-art (SOTA) models on both single-step and multi-step prediction tasks across
three real-world datasets.

## item_id: m_1661

TITLE: A Generalized Framework of Sequence Generation with Application to Undirected Sequence Models

ABSTRACT: Undirected neural sequence models such as BERT (Devlin et al., 2019) have received renewed interest due to their success on discriminative natural language understanding tasks such as question-answering and natural language inference. 
The problem of generating sequences directly from these models has received relatively little attention, in part because generating from such models departs significantly from the conventional approach of monotonic generation in directed sequence models. We investigate this problem by first proposing a generalized model of sequence generation that unifies decoding in directed and undirected models. The proposed framework models the process of generation rather than a resulting sequence, and under this framework, we derive various neural sequence models as special cases, such as autoregressive, semi-autoregressive, and refinement-based non-autoregressive models. This unification enables us to adapt decoding algorithms originally developed for directed sequence models to undirected models. We demonstrate this by evaluating various decoding strategies for a cross-lingual masked translation model (Lample and Conneau, 2019). Our experiments show that generation from undirected sequence models, under our framework, is competitive with the state of the art on WMT'14 English-German translation. We also demonstrate that the proposed approach enables constant-time translation with similar performance to linear-time translation from the same model by rescoring hypotheses with an autoregressive model.

## item_id: m_1662

TITLE: Critical initialisation in continuous approximations of binary neural networks

ABSTRACT: The training of stochastic neural network models with binary ($\pm1$) weights and activations via continuous surrogate networks is investigated. We derive new surrogates using a novel derivation based on writing the stochastic neural network as a Markov chain. This derivation also encompasses existing variants of the surrogates presented in the literature. Following this, we theoretically study the surrogates at initialisation. We derive, using mean field theory, a set of scalar equations describing how input signals propagate through the randomly initialised networks. The equations reveal whether so-called critical initialisations exist for each surrogate network, where the network can be trained to arbitrary depth. Moreover, we predict theoretically and confirm numerically, that common weight initialisation schemes used in standard continuous networks, when applied to the mean values of the stochastic binary weights, yield poor training performance. This study shows that, contrary to common intuition, the means of the stochastic binary weights should be initialised close to $\pm 1$, for deeper networks to be trainable.

## item_id: m_1663

TITLE: PoNet: Pooling Network for Efficient Token Mixing in Long Sequences

ABSTRACT: Transformer-based models have achieved great success in various NLP, vision, and speech tasks. However, the core of Transformer, the self-attention mechanism, has a quadratic time and memory complexity with respect to the sequence length, which hinders applications of Transformer-based models to long sequences. Many approaches have been proposed to mitigate this problem, such as sparse attention mechanisms, low-rank matrix approximations and scalable kernels, and token mixing alternatives to self-attention. We propose a novel Pooling Network (PoNet) for token mixing in long sequences with linear complexity. We design multi-granularity pooling and pooling fusion to capture different levels of contextual information and combine their interactions with tokens. On the Long Range Arena benchmark, PoNet significantly outperforms Transformer and achieves competitive accuracy, while being only slightly slower than the fastest model, FNet, across all sequence lengths measured on GPUs. We also conduct systematic studies on the transfer learning capability of PoNet and observe that PoNet achieves 95.7 percent of the accuracy of BERT on the GLUE benchmark, outperforming FNet by 4.5 percent relative. Comprehensive ablation analysis demonstrates effectiveness of the designed multi-granularity pooling and pooling fusion for token mixing in long sequences and efficacy of the designed pre-training tasks for PoNet to learn transferable contextualized language representations.

## item_id: m_1664

TITLE: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

ABSTRACT: Neural network scaling has been critical for improving the model quality in many real-world machine learning applications with vast amounts of training data and compute. Although this trend of scaling is affirmed to be a sure-fire approach for better model quality, there are challenges on the path such as the computation cost,ease of programming, and efficient implementation on parallel devices.  In this paper we demonstrate conditional computation as a remedy to the above mentioned impediments, and demonstrate its efficacy and utility.  We make extensive use of GShard, a module composed of a set of lightweight annotation APIs and an extension to the XLA compiler to enable large scale models with up to trillions of parameters. GShard and conditional computation enable us to scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts. We demonstrate that such a giant model with 600 billion parameters can efficiently be trained on 2048 TPU v3 cores in 4 days to achieve far superior quality for translation from 100 languages to English compared to the prior art.

## item_id: m_1665

TITLE: Measuring Numerical Common Sense: Is A Word Embedding Approach Effective?

ABSTRACT: Numerical common sense (e.g., ``a person with a height of 2m is very tall'') is essential when deploying artificial intelligence (AI) systems in society. To predict ranges of small and large values for a given target noun and unit, 
previous studies have implemented a rule-based method that processed numeric values appearing in a natural language by using template matching. To obtain numerical knowledge, crawled textual data from web pages are frequently used as the input in the above method. Although this is an important task, few studies have addressed the availability of numerical common sense extracted from corresponding textual information. To this end, we first used a crowdsourcing service to obtain sufficient data for a subjective agreement on numerical common sense. Second, to examine whether common sense is attributed to current word embedding, we examined the performance of a regressor trained on the obtained data. In comparison with humans, the performance of an automatic relevance determination regression model was good, particularly when the unit was yen (a maximum correlation coefficient of 0.57). Although all the regression approach with word embedding does not predict values with high correlation coefficients, this word-embedding method could potentially contribute to construct numerical common sense for AI deployment.

## item_id: m_1666

TITLE: GSD: Generalized Stochastic Decoding

ABSTRACT: Although substantial progress has been made in various text generation tasks, there remains a vast gap between current generations and human languages. One reason is that virtually all decoding methods currently developed are pragmatic to address the text degeneration problem, which exists in both deterministic and stochastic decoding algorithms. So, why text generated from these algorithms are divergent? What is the critical difference between these algorithms? Moreover, is it possible to design a generalized framework where existing decoding algorithms can be naturally connected, uniformly described, and mutually inspired?
In this paper, we try to explore answers to these intriguing questions. Correctly, we propose a generalized decoding framework that can be used to describe and connect existing popular decoding algorithms. Based on the framework, we propose a novel implementation with a distinctive core from existing decoding algorithms. As far as we know, this is the first work trying to propose a generalized framework to bridge these decoding algorithms using formal theorems and concrete implementations. By setting up different conditions, our framework provides infinite space to develop new decoding algorithms. Experiments show that text produced by our method is closest to the characteristics of human languages. Source code and the generated text can be accessed from https://github.com/ginoailab/gsd.git.

## item_id: m_1667

TITLE: Exemplary Natural Images Explain CNN Activations Better than State-of-the-Art Feature Visualization

ABSTRACT: Feature visualizations such as synthetic maximally activating images are a widely used explanation method to better understand the information processing of convolutional neural networks (CNNs). At the same time, there are concerns that these visualizations might not accurately represent CNNs' inner workings. Here, we measure how much extremely activating images help humans to predict CNN activations.
Using a well-controlled psychophysical paradigm, we compare the informativeness of synthetic images by Olah et al. (2017) with a simple baseline visualization, namely exemplary natural images that also strongly activate a specific feature map. Given either synthetic or natural reference images, human participants choose which of two query images leads to strong positive activation. The experiment is designed to maximize participants' performance, and is the first to probe intermediate instead of final layer representations. We find that synthetic images indeed provide helpful information about feature map activations ($82\pm4\%$ accuracy; chance would be $50\%$). However, natural images --- originally intended to be a baseline --- outperform these synthetic images by a wide margin ($92\pm2\%$). Additionally, participants are faster and more confident for natural images, whereas subjective impressions about the interpretability of the feature visualizations by Olah et al. (2017) are mixed. The higher informativeness of natural images holds across most layers, for both expert and lay participants as well as for hand- and randomly-picked feature visualizations. Even if only a single reference image is given, synthetic images provide less information than natural images ($65\pm5\%$ vs. $73\pm4\%$). In summary, synthetic images from a popular feature visualization method are significantly less informative for assessing CNN activations than natural images. We argue that visualization methods should improve over this simple baseline.

## item_id: m_1668

TITLE: Interpretable Classification via Supervised Variational Autoencoders and Differentiable Decision Trees

ABSTRACT: As deep learning-based classifiers are increasingly adopted in real-world applications, the importance of understanding how a particular label is chosen grows. Single decision trees are an example of a simple, interpretable classifier, but are unsuitable for use with complex, high-dimensional data. On the other hand, the variational autoencoder (VAE) is designed to learn a factored, low-dimensional representation of data, but typically encodes high-likelihood data in an intrinsically non-separable way.  We introduce the differentiable decision tree (DDT) as a modular component of deep networks and a simple, differentiable loss function that allows for end-to-end optimization of a deep network to compress high-dimensional data for classification by a single decision tree.  We also explore the power of labeled data in a  supervised VAE (SVAE) with a Gaussian mixture prior, which leverages label information to produce a high-quality generative model with improved bounds on log-likelihood.  We combine the SVAE with the DDT to get our classifier+VAE (C+VAE), which is competitive in both classification error and log-likelihood, despite optimizing both simultaneously and using a very simple encoder/decoder architecture. 

## item_id: m_1669

TITLE: Model-based Causal Bayesian Optimization

ABSTRACT: How should we intervene on an unknown structural equation model to maximize a downstream variable of interest? This setting, also known as causal Bayesian optimization (CBO), has important applications in medicine, ecology, and manufacturing. Standard Bayesian optimization algorithms fail to effectively leverage the underlying causal structure. Existing CBO approaches assume noiseless measurements and do not come with guarantees. We propose the {\em model-based causal Bayesian optimization algorithm (MCBO)} that learns a full system model instead of only modeling intervention-reward pairs. MCBO propagates epistemic uncertainty about the causal mechanisms through the graph and trades off exploration and exploitation via the optimism principle. We bound its cumulative regret, and obtain the first non-asymptotic bounds for CBO. Unlike in standard Bayesian optimization, our acquisition function cannot be evaluated in closed form, so we show how the reparameterization trick can be used to apply gradient-based optimizers. The resulting practical implementation of MCBO compares favorably with state-of-the-art approaches empirically.

## item_id: m_1670

TITLE: LLBoost: Last Layer Perturbation to Boost Pre-trained Neural Networks

ABSTRACT:     While deep networks have produced state-of-the-art results in several domains from image classification to machine translation, hyper-parameter selection remains a significant computational bottleneck.  In order to produce the best possible model, practitioners often search across random seeds or use ensemble methods.  As models get larger, any method to improve neural network performance that involves re-training becomes intractable.  For example, computing the training accuracy of FixResNext-101 (829 million parameters) on ImageNet takes roughly 1~day when using 1~GPU.   
    In this work, we present LLBoost, a theoretically-grounded, computationally-efficient method to boost the validation accuracy of pre-trained over-parameterized models without impacting the original training accuracy.  LLBoost adjusts the last layer of a neural network by adding a term that is orthogonal to the training feature matrix, which is constructed by applying all layers but the last to the training data.  We provide an efficient implementation of LLBoost on the GPU and demonstrate that LLBoost, run using only 1 GPU, improves the test/validation accuracy of pre-trained models on CIFAR10, ImageNet32, and ImageNet.  In the over-parameterized linear regression setting, we prove that LLBoost reduces the generalization error of any interpolating solution with high probability without affecting training error.  

## item_id: m_1671

TITLE: Efficient, probabilistic analysis of combinatorial neural codes

ABSTRACT: Artificial and biological neural networks (ANNs and BNNs) can encode inputs in the form of combinations of individual neurons' activities. These combinatorial neural codes present a computational challenge for direct and efficient analysis due to their high dimensionality and often large volumes of data. Here we improve the computational complexity -- from factorial to quadratic time -- of direct algebraic methods previously applied to small examples and apply them to large neural codes generated by experiments. These methods provide a novel and efficient way of probing algebraic, geometric, and topological characteristics of combinatorial neural codes and provide insights into how such characteristics are related to learning and experience in neural networks. We introduce a procedure to perform hypothesis testing on the intrinsic features of neural codes using information geometry. We then apply these methods to neural activities from an ANN for image classification and a BNN for 2D navigation to, without observing any inputs or outputs, estimate the structure and dimensionality of the stimulus or task space. Additionally, we demonstrate how an ANN varies its internal representations across network depth and during learning.

## item_id: m_1672

TITLE: NEFTune: Noisy Embeddings Improve Instruction Finetuning

ABSTRACT: We show that language model finetuning can be improved, sometimes dramatically, with a simple augmentation. 
NEFTune adds noise to the embedding vectors during training.
Standard finetuning of LLaMA-2-7B using Alpaca achieves $29.79$\% on AlpacaEval, which rises to $64.69$\% using noisy embeddings. NEFTune also improves over strong baselines on modern instruction datasets.
Models trained with Evol-Instruct see a $10$\% improvement, with ShareGPT an $8$\% improvement, and with OpenPlatypus an $8$\% improvement. 
Even powerful models further refined with RLHF such as LLaMA-2-Chat benefit from additional training with NEFTune. Particularly, we see these improvements on the conversational abilities of the instruction model and not on traditional tasks like those on the OpenLLM Leaderboard, where performance is the same.

## item_id: m_1673

TITLE: Enhancing Human Body Generation in Diffusion Models with Dual-Level Prior Knowledge

ABSTRACT: The development of diffusion models (DMs) has greatly enhanced text-to-image generation, outperforming previous methods like generative adversarial networks (GANs) in terms of image quality and text alignment. However, accurately generating human body images remains challenging, often resulting in disproportionate figures and anatomical errors, which limits their practical applications in areas such as portrait generation. While previous methods such as HcP have shown promising results, limitations including wrongly kept prior, insufficient human-related knowledge, and limited generalization ability still exist due to the specific design of fully-supervised learning with only pose-related information. In this study, we introduce a novel method to enhance pretrained diffusion models for realistic human body generation by incorporating dual-level human prior knowledge. Our approach involves learning shape-level details with the human-related tokens in the original prompts, and learning pose-level prior by adding a learnable pose-aware token to each text prompt. We use a two-stage training strategy to rectify the cross attentions with a bind-then-generalize process, leveraging multiple novel objectives along with adversarial training. Our extensive experiments show that this method significantly improves the ability of SD1.5 and SDXL pretrained models to generate human bodies, reducing deformities and enhancing practical utility.

## item_id: m_1674

TITLE: Learn the Time to Learn: Replay Scheduling in Continual Learning

ABSTRACT: Replay methods are known to be successful at mitigating catastrophic forgetting in continual learning scenarios despite having limited access to historical data. However, storing historical data is cheap in many real-world settings, yet replaying all historical data is often prohibited due to processing time constraints. In such settings, we propose that continual learning systems should learn the time to learn and schedule which tasks to replay at different time steps. We first demonstrate the benefits of our proposal by using Monte Carlo tree search to find a proper replay schedule, and show that the found replay schedules can outperform fixed scheduling policies when combined with multiple replay methods in various continual learning settings. Additionally, we propose a framework for learning replay scheduling policies with reinforcement learning. We show that the learned policies can generalize better in new continual learning scenarios compared to equally replaying all seen tasks, without added computational cost. Our study reveals the importance of learning the time to learn in continual learning, which brings current research closer to real-world needs.

## item_id: m_1675

TITLE: Dynamic Integration of Background Knowledge in Neural NLU Systems

ABSTRACT: Common-sense or background knowledge is required to understand natural language, but in most neural natural language understanding (NLU) systems, the requisite background knowledge is indirectly acquired from static corpora. We develop a new reading architecture for the dynamic integration of explicit background knowledge in NLU models. A new task-agnostic reading module provides refined word representations to a task-specific NLU architecture by processing background knowledge in the form of free-text statements, together with the task-specific inputs. Strong performance on the tasks of document question answering (DQA) and recognizing textual entailment (RTE) demonstrate the effectiveness and flexibility of our approach. Analysis shows that our models learn to exploit knowledge selectively and in a semantically appropriate way.

## item_id: m_1676

TITLE: Wav2Letter: an End-to-End ConvNet-based Speech Recognition System

ABSTRACT: This paper presents a simple end-to-end model for speech recognition, combining a convolutional network based acoustic model and a graph decoding. It is trained to output letters, with transcribed speech, without the need for force alignment of phonemes. We introduce an automatic segmentation criterion for training from sequence annotation without alignment that is on par with CTC (Graves et al., 2006) while being simpler. We show competitive results in word error rate on the Librispeech corpus (Panayotov et al., 2015) with MFCC features, and promising results from raw waveform.

## item_id: m_1677

TITLE: WaveDiffusion: Exploring Full Waveform Inversion via Joint Diffusion in the Latent Space

ABSTRACT: Full Waveform Inversion (FWI) is a vital technique for reconstructing high-resolution subsurface velocity maps from seismic waveform data, governed by partial differential equations (PDEs) that model wave propagation. Traditional machine learning approaches typically map seismic data to velocity maps by encoding seismic waveforms into latent embeddings and decoding them into velocity maps. In this paper, we introduce a novel framework that reframes FWI as a joint diffusion process in a shared latent space, bridging seismic waveform data and velocity maps. Our approach has two key components: first, we merge the bottlenecks of two separate autoencoders—one for seismic data and one for velocity maps—into a unified latent space using vector quantization to establish a shared codebook. Second, we train a diffusion model in this latent space, enabling the simultaneous generation of seismic and velocity map pairs by sampling and denoising the latent representations, followed by decoding each modality with its respective decoder. Remarkably, our jointly generated seismic-velocity pairs approximately satisfy the governing PDE without any additional constraint, offering a new geometric interpretation of FWI. The diffusion process learns to score the latent space according to its deviation from the PDE, with higher scores representing smaller deviations from the true solutions. By following this diffusion process, the model traces a path from random initialization to a valid solution of the governing PDE. Our experiments on the OpenFWI dataset demonstrate that the generated seismic and velocity map pairs not only exhibit high fidelity and diversity but also adhere to the physical constraints imposed by the governing PDE.

## item_id: m_1678

TITLE: Off-Policy Actor-Critic with Shared Experience Replay

ABSTRACT: We investigate the combination of actor-critic reinforcement learning algorithms with uniform large-scale experience replay and propose solutions for two challenges: (a) efficient actor-critic learning with experience replay (b) stability of very off-policy learning. We employ those insights to accelerate hyper-parameter sweeps in which all participating agents run concurrently and share their experience via a common replay module.

To this end we analyze the bias-variance tradeoffs in V-trace, a form of importance sampling for actor-critic methods. Based on our analysis, we then argue for mixing experience sampled from replay with on-policy experience, and propose a new trust region scheme that scales effectively to data distributions where V-trace becomes unstable.

We provide extensive empirical validation of the proposed solution. We further show the benefits of this setup by demonstrating state-of-the-art data efficiency on Atari among agents trained up until 200M environment frames.

## item_id: m_1679

TITLE: LEARNING  TO LEARN  WITH  BETTER  CONVERGENCE

ABSTRACT: We consider the learning to learn problem, where the goal is to leverage deeplearning  models  to  automatically  learn  (iterative)  optimization  algorithms  for training machine learning models. A natural way to tackle this problem is to replace the human-designed optimizer by an LSTM network and train the parameters on some simple optimization problems (Andrychowicz et al., 2016).  Despite their success compared to traditional optimizers such as SGD on a short horizon, theselearnt (meta-) optimizers suffer from two key deficiencies: they fail to converge(or can even diverge) on a longer horizon (e.g., 10000 steps). They also often fail to generalize to new tasks. To address the convergence problem, we rethink the architecture design of the meta-optimizer and develop an embarrassingly simple,yet powerful form of meta-optimizers—a coordinate-wise RNN model. We provide insights into the problems with the previous designs of each component and re-design our SimpleOptimizer to resolve those issues. Furthermore, we propose anew mechanism to allow information sharing between coordinates which enables the meta-optimizer to exploit second-order information with negligible overhead.With these designs, our proposed SimpleOptimizer outperforms previous meta-optimizers and can successfully converge to optimal solutions in the long run.Furthermore, our empirical results show that these benefits can be obtained with much smaller models compared to the previous ones.

## item_id: m_1680

TITLE: Diffusion State-Guided Projected Gradient for Inverse Problems

ABSTRACT: Recent advancements in diffusion models have been effective in learning data priors for solving inverse problems. They leverage diffusion sampling steps for inducing a data prior while using a measurement guidance gradient at each step to impose data consistency. For general inverse problems, approximations are needed when an unconditionally trained diffusion model is used since the measurement likelihood is intractable, leading to inaccurate posterior sampling. In other words, due to their approximations, these methods fail to preserve the generation process on the data manifold defined by the diffusion prior, leading to artifacts in applications such as image restoration. To enhance the performance and robustness of diffusion models in solving inverse problems, we propose Diffusion State-Guided Projected Gradient (DiffStateGrad), which projects the measurement gradient onto a subspace that is a low-rank approximation of an intermediate state of the diffusion process. DiffStateGrad, as a module, can be added to a wide range of diffusion-based inverse solvers to improve the preservation of the diffusion process on the prior manifold and filter out artifact-inducing components. We highlight that DiffStateGrad improves the robustness of diffusion models in terms of the choice of measurement guidance step size and noise while improving the worst-case performance. Finally, we demonstrate that DiffStateGrad improves upon the state-of-the-art on linear and nonlinear image restoration inverse problems. Our code is available at https://github.com/Anima-Lab/DiffStateGrad.

## item_id: m_1681

TITLE: Learning Curve Prediction with Bayesian Neural Networks

ABSTRACT: Different neural network architectures, hyperparameters and training protocols lead to different performances as a function of time.
Human experts routinely inspect the resulting learning curves to quickly terminate runs with poor hyperparameter settings and thereby considerably speed up manual hyperparameter optimization. Exploiting the same information in automatic Bayesian hyperparameter optimization requires a probabilistic model of learning curves across hyperparameter settings. Here, we study the use of Bayesian neural networks for this purpose and improve their performance by a specialized learning curve layer.

## item_id: m_1682

TITLE: Systematic Analysis of Cluster Similarity Indices: How to Validate Validation Measures

ABSTRACT: There are many cluster similarity indices used to evaluate clustering algorithms, and choosing the best one for a particular task remains an open problem. We demonstrate that this problem is crucial: there are many disagreements among the indices, these disagreements do affect which algorithms are chosen in applications, and this can lead to degraded performance in real-world systems. We propose a theoretical solution to this problem: we develop a list of desirable properties and theoretically verify which indices satisfy them. This allows for making an informed choice: given a particular application, one can first make a selection of properties that are desirable for a given application and then identify indices satisfying these. We observe that many popular indices have significant drawbacks. Instead, we advocate using other ones that are not so widely adopted but have beneficial properties.

## item_id: m_1683

TITLE: Meta-Learning an Inference Algorithm for Probabilistic Programs

ABSTRACT: We present a meta-algorithm for learning a posterior-inference algorithm for restricted probabilistic programs. Our meta-algorithm takes a training set of probabilistic programs that describe models with observations, and attempts to learn an efficient method for inferring the posterior of a similar program.
A key feature of our approach is the use of what we call a white-box inference algorithm that extracts information directly from model descriptions themselves, given as programs. Concretely, our white-box inference algorithm is equipped with multiple neural networks, one for each type of atomic command, and computes an approximate posterior of a given probabilistic program by analysing individual atomic commands in the program using these networks. The parameters of these networks are then learnt from a training set by our meta-algorithm.
We empirically demonstrate that the learnt inference algorithm generalises well to programs that are new in terms of both parameters and structures, and report cases where our approach
has advantages over alternative approaches such as HMC in terms of test-time efficiency.
The overall results show the promise as well as remaining challenges of our approach.

## item_id: m_1684

TITLE: Trolley Problems for Large Language Models Across 100+ Languages

ABSTRACT: As large language models (LLMs) are becoming deployed in more and more systems, it is crucial to inspect the moral tendencies in their decision-making process. In this paper, we take the largest set of moral judgments collected to date, the trolley problems, to check the preferences stated in LLMs' responses, as well as their supporting reasons. We first conduct a large-scale inspection on over 10K trolley problem scenarios in English, and compare them with human preferences. Then we extend the questions to different cultures by changing the language of the prompts and positioning the questions for different persona. We discover that LLMs tend to generate more human-aligned responses for the English culture, but also show interesting tendencies on other cultures.

## item_id: m_1685

TITLE: I-PGD-AT: Efficient Adversarial Training via Imitating Iterative PGD Attack 

ABSTRACT: Adversarial training has been widely used in various machine learning paradigms to improve the robustness; while it would increase the training cost due to the perturbation optimization process. To improve the efficiency, recent studies leverage Fast Gradient Sign Method with Random Start (FGSM-RS) for adversarial training. However, such methods would lead to relatively low robustness and catastrophic overfitting, which means the robustness against iterative attacks (e.g. Projected Gradient Descent (PGD)) would suddenly drop to 0%. Different approaches have been proposed to address this problem, while later studies show that catastrophic overfitting still remains. In this paper, motivated by the fact that expensive iterative adversarial training methods achieve high robustness without catastrophic overfitting, we aim to ask: Can we perform iterative adversarial training in an efficient way? To this end, we first analyze the difference of perturbation generated by FGSM-RS and PGD and find that PGD tends to craft diverse discrete values instead of $\pm 1$ in FGSM-RS. Based on this observation, we propose an efficient single-step adversarial training method I-PGD-AT by adopting I-PGD attack for training, in which I-PGD imitates PGD virtually. Unlike FGSM that crafts the perturbation directly using the sign of gradient, I-PGD imitates the perturbation of PGD based on the magnitude of gradient. Extensive empirical evaluations on CIFAR-10 and Tiny ImageNet demonstrate that our I-PGD-AT can improve the robustness compared with the baselines and significantly delay catastrophic overfitting. Moreover, we explore and discuss the factors that affect catastrophic overfitting. Finally, to demonstrate the generality of I-PGD-AT, we integrate it into PGD adversarial training and show that it can even further improve the robustness.

## item_id: m_1686

TITLE: Finding a Jack-of-All-Trades: An Examination of Semi-supervised Learning in Reading Comprehension

ABSTRACT: Deep learning has proven useful on many NLP tasks including reading
comprehension. However it requires a lot of training data which are not
available in some domains of application. Hence we examine the possibility
of using data-rich domains to pre-train models and then apply them in
domains where training data are harder to get. Specifically, we train a
neural-network-based model on two context-question-answer datasets, the
BookTest and CNN/Daily Mail, and we monitor transfer to subsets of bAbI,
a set of artificial tasks designed to test specific reasoning abilities, and of
SQuAD, a question-answering dataset which is much closer to real-world
applications. Our experiments show very limited transfer if the model isn’t
shown any training examples from the target domain however the results
are promising if the model is shown at least a few target-domain examples.
Furthermore we show that the effect of pre-training is not limited to word
embeddings.

## item_id: m_1687

TITLE: Enhanced Model-agnostic Training of Deep Tabular Generation Models

ABSTRACT: Despite the active research for tabular data synthesis, state-of-the-art methods continue to face challenges arising from the complex distribution of tabular data. To this end, we claim that the difficulty can be alleviated by making the distribution simpler using Gaussian decomposition. In this paper, we propose a training method, Gaussian Decomposition-based Generation of Tabular data (GADGET), which can be applied to any generative models for tabular data. The method i) decomposes the complicated distribution of tabular data into a mixture of $K$ Gaussian distributions, ii) trains one model for each decomposed Gaussian distribution aided by our proposed self-paced learning algorithm. In other words, we do not stop at utilizing a Gaussian mixture model to discover $K$ simplified distributions but utilize their surrogate density functions for designing our self-paced learning algorithm. In our experiments with 11 datasets and 8 baselines, we show that GADGET greatly improves existing tabular data synthesis methods. In particular, a score-based generative model on our GADGET training framework achieves the state-of-the-art performance in terms of sampling quality and diversity.

## item_id: m_1688

TITLE: Prompt-Guided Dynamic Network for Image Super Resolution

ABSTRACT: Existing single image super-resolution (SISR) methods learn the convolutional kernel solely from a single image modality. However, the SR performance is limited by the diversity of input modality and the insufficient image-level information in low-resolution images. In this paper, we seek to use multi-modal prompts (texts or images) to assist existing SR networks to learn more discriminative features, leading to superior SR performance. To this end, we develop the Dynamic Correlation Module in a plug-and-play form for existing SR networks, which learns meaningful semantic and textural information from multi-modal prompt embeddings extracted from a large-scale vision-language model (such as CLIP). Specifically, Spatially Multi-Modal Attention Module is proposed to generate the pixel-wise cross-modal attention mask which would highlight the interest regions given certain prompts. Moreover, to the best of our knowledge, we are the first ones that introduce multi-modal prompts into convolutional kernel estimation which can better handle spatial variants and retain cross-modal relevance. Extensive experiments and ablation studies demonstrate the effectiveness of the proposed Dynamic Correlation Module which exploits the discriminative prompt features to recover realistic high-resolution images, elevating existing SR performance by a notable gap.

## item_id: m_1689

TITLE: Leveraging MLLM Embeddings and Attribute Smoothing for Compositional Zero-Shot Learning

ABSTRACT: Compositional zero-shot learning (CZSL) aims to recognize novel compositions of attributes and objects learned from seen compositions. Previous works disentangle attribute and object by extracting shared and exclusive parts between image pairs sharing the same attribute (object), as well as aligning them with pretrained word embeddings to improve unseen attribute-object recognition. Despite the significant achievements of existing efforts, they are hampered by three limitations: (1) the efficacy of disentanglement is compromised due to the influence of the background and the intricate entanglement of attribute with object in the same parts. (2) existing word embeddings fail to capture complex multimodal semantic information. (3) overconfidence exhibited by existing models in seen compositions hinders their generalization to novel compositions. Being aware of these, we propose a novel framework named Multimodal Large Language Model (MLLM) embeddings and attribute smoothing guided disentanglement (TRIDENT) for CZSL. First, we leverage feature adaptive aggregation (FAA) modules to mitigate the impact of background, and utilize learnable condition masks to capture multi-granularity features for subsequent disentanglement. Then, the last hidden states of MLLM are employed as word embeddings for their superior representation capabilities. Moreover, we propose attribute smoothing through leveraging auxiliary attributes generated by Large Language Model (LLM) for each seen composition, addressing the issue of overconfidence by encouraging the model to learn more attributes in one given composition instead of just fitting a fixed attribute-object combination. Extensive experiments demonstrate that TRIDENT achieves state-of-the-art performance on three challenging datasets: MIT-States, C-GQA, and VAW-CZSL, respectively.

## item_id: m_1690

TITLE: Cross-Iteration Batch Normalization

ABSTRACT: A well-known issue of Batch Normalization is its significantly reduced effectiveness in the case of small mini-batch sizes. When a mini-batch contains few examples, the statistics upon which the normalization is defined cannot be reliably estimated from it during a training iteration. To address this problem, we present Cross-Iteration Batch Normalization (CBN), in which examples from multiple recent iterations are jointly utilized to enhance estimation quality. A challenge of computing statistics over multiple iterations is that the network activations from different iterations are not comparable to each other due to changes in network weights. We thus compensate for the network weight changes via a proposed technique based on Taylor polynomials, so that the statistics can be accurately estimated and batch normalization can be effectively applied. On object detection and image classification with small mini-batch sizes, CBN is found to outperform the original batch normalization and a direct calculation of statistics over previous iterations without the proposed compensation technique.

## item_id: m_1691

TITLE: MiniFold: Simple, Fast and Accurate Protein Structure Prediction

ABSTRACT: Protein structure prediction has emerged as a powerful tool for biologists and drug makers. However, the computational toll associated with state-of-the-art models, such as AlphaFold2 or ESMFold, hinders their use in large-scale applications like virtual screening or mutational scanning, where a single experiment may involve processing millions of protein sequences. In an effort to develop a more efficient model, we aimed to understand which of the complex architectural choices proposed in AlphaFold2 were essential to achieve high performance, and which could be omitted without significantly compromising accuracy. This analysis culminated in a simple, yet highly expressive architecture for protein structure prediction. Our model, MiniFold, consists of a minimal Evoformer variant, a parameter-free coordinate recovery algorithm, and a custom hardware-optimized implementation composed of newly designed GPU kernels. When compared against ESMFold, MiniFold achieves over 100x speedup and shows improved scalability to long protein sequences while conserving over 95% of the original performance, making it a promising candidate for large-scale applications.

## item_id: m_1692

TITLE: Generative Adversarial User Privacy in Lossy Single-Server Information Retrieval

ABSTRACT: We consider the problem of information retrieval from a dataset of files stored on a single server under both a user distortion and a user privacy constraint. Specifically, a user requesting a file from the dataset should be able to reconstruct the requested file with a prescribed distortion, and in addition, the identity of the requested file should be kept private from the server with a prescribed privacy level. The proposed model can be seen as an extension of the well-known concept of private information retrieval by allowing for distortion in the retrieval process and relaxing the perfect privacy requirement. We initiate the study of the tradeoff between download rate, distortion, and user privacy leakage, and show that the optimal rate-distortion-leakage tradeoff is convex and that it allows for a concise information-theoretical formulation in terms of mutual information in the limit of large file sizes. Moreover, we propose a new data-driven framework by leveraging recent advancements in generative adversarial models which allows a user to learn efficient schemes in terms of download rate from the data itself. Learning the scheme is formulated as a constrained minimax game between a user which desires to keep the identity of the requested file private and an adversary that tries to infer which file the user is interested in under a distortion constraint. In general, guaranteeing a certain privacy level leads to a higher rate-distortion tradeoff curve, and hence a sacrifice in either download rate or distortion. We evaluate the performance of the scheme on a synthetic Gaussian dataset as well as on the MNIST dataset. For the MNIST dataset, the data-driven approach significantly outperforms a proposed general achievable scheme combining source coding with the download of multiple files.

## item_id: m_1693

TITLE: Density Constrained Reinforcement Learning

ABSTRACT: Constrained reinforcement learning (CRL) plays an important role in solving safety-critical and resource-limited tasks. However, existing methods typically rely on tuning reward or cost parameters to encode the constraints, which can be tedious and tend to not generalize well. Instead of building sophisticated cost functions for constraints, we present a pioneering study of imposing constraints directly on the state density function of the system. Density functions have clear physical meanings and can express a variety of constraints in a straightforward fashion. We prove the duality between the density function and Q function in CRL and use it to develop an effective primal-dual algorithm to solve density constrained reinforcement learning problems. We provide theoretical guarantees of the optimality of our approach and use a comprehensive set of case studies including standard benchmarks to show that our method outperforms other leading CRL methods in terms of achieving higher reward while respecting the constraints.

## item_id: m_1694

TITLE: STYLE EXAMPLE-GUIDED TEXT GENERATION USING GENERATIVE ADVERSARIAL TRANSFORMERS

ABSTRACT: We introduce a language generative model framework for generating a styled paragraph based on a context sentence and a style reference example. The framework consists of a style encoder and a texts decoder. The style encoder extracts a style code from the reference example, and the text decoder generates texts based on the style code and the context. We propose a novel objective function to train our framework. We also investigate different network design choices. We conduct extensive experimental validation with comparison to strong baselines to validate the effectiveness of the proposed framework using a newly collected dataset with diverse text styles. Both code and dataset will be released upon publication.

## item_id: m_1695

TITLE: On Random Deep Weight-Tied Autoencoders: Exact Asymptotic Analysis, Phase Transitions, and Implications to Training

ABSTRACT: We study the behavior of weight-tied multilayer vanilla autoencoders under the assumption of random weights. Via an exact characterization in the limit of large dimensions, our analysis reveals interesting phase transition phenomena when the depth becomes large. This, in particular, provides quantitative answers and insights to three questions that were yet fully understood in the literature. Firstly, we provide a precise answer on how the random deep weight-tied autoencoder model performs “approximate inference” as posed by Scellier et al. (2018), and its connection to reversibility considered by several theoretical studies. Secondly, we show that deep autoencoders display a higher degree of sensitivity to perturbations in the parameters, distinct from the shallow counterparts. Thirdly, we obtain insights on pitfalls in training initialization practice, and demonstrate experimentally that it is possible to train a deep autoencoder, even with the tanh activation and a depth as large as 200 layers, without resorting to techniques such as layer-wise pre-training or batch normalization. Our analysis is not specific to any depths or any Lipschitz activations, and our analytical techniques may have broader applicability.

## item_id: m_1696

TITLE: HyperTransformer: Attention-Based CNN Model Generation from Few Samples

ABSTRACT: In this work we propose a HyperTransformer, a transformer based model that generates all weights of a CNN model directly from the support samples. This approach allows to use a high-capacity model for encoding task-dependent variations in the weights of a smaller model. We show for multiple few-shot benchmarks with different architectures and datasets that our method beats or matches that of the traditional learning methods in a few-shot regime. Specifically, we show that for very small target models, our method can generate significantly better performing models than traditional few-shot learning methods. For larger models we discover that applying generation to the last layer only, allows to produce competitive or better results while being end-to-end differentiable. Finally, we extend our approach to semi-supervised regime utilizing unlabeled samples in the support set and further improving few-shot performance in the presence of unlabeled data.

## item_id: m_1697

TITLE: PRNet: A Progressive Regression Network for No-Reference User-Generated-Content Video Quality Assessment

ABSTRACT: Non-professional video, commonly known as User Generated Content (UGC) has become very popular in today’s video sharing applications. However, objectively perceptual quality assessment of UGC-videos is still a challenge problem, which is arose from many reasons. First, the pristine sources of UGC-videos are not available, which makes the appropriate technique is the no-reference NR video quality assessment VQA (NR-VQA). Another factor leads the NR-UGC-VQA to a challenge is that subjective mean option scores (MOS) of all the UGC-datasets are not uniformly distributed. The largest UGC video dataset---YouTube-UGC still faces a problem that the database has right-skewed MOS distribution. In addition, authentic degradations occurred in the videos are not unique, therefore, not predicable. For example, an over- or under-exposure image/video, brightness and contrast static information is important for evaluation. Only employing verified priori statistic knowledge or generalized learning knowledge may not cover all possible distortions. To solve these problems, we introduce a novel NR-VQA framework---Progressive Regress Network (PRNet) in this paper. For the skewed MOS problem, a progressive regression model is proposed, which utilizes the coarse-to-fine strategy during the training process. This strategy can turn sparse subjective human rating scores into integers with denser samples, which can solve the in-balanced sample problem and make the training progress smoother. For the unpredictable distortions problem, a wide and deep model based on our PRNet is developed, which employs both low-level features generated from natural scene statistics (NSS) and high-level semantic features extracted by deep neural networks, to fuse memorizing priori knowledge and generalizing learning features. Our experimental results demonstrate that our proposed method PRNet achieves state-of-the-art performance in currently three main popular UGC-VQA datasets (KoNVid-1K, LIVE-VQC, and YouTube-UGC).

## item_id: m_1698

TITLE: Gradient Imbalance and solution in Online Continual learning

ABSTRACT: Most existing techniques for online continual learning are based on experience-replay. In this approach, a memory buffer is used to save some data from past tasks for dealing with catastrophic forgetting. In training, a small batch of data from the data stream of the current task and some sampled data from a memory buffer are used jointly to update or train the current model. In this paper, we study the experience replay-based approach from a new angle, gradient imbalance. We first investigate and analyze this phenomenon experimentally from two perspectives: imbalance of samples introduced by experience replay and sequence of classes introduced by incremental learning. To our knowledge, this problem has not been studied before and it significantly limits the performance of online continual learning. Based on observations from experiments and theoretical analysis, a new learning strategy and a new loss are proposed to deal with the problem. Empirical evaluation shows that GAD helps improve the online CL performance by more than 11% in accuracy.

## item_id: m_1699

TITLE: Simple and Effective VAE Training with Calibrated Decoders

ABSTRACT: Variational autoencoders (VAEs) provide an effective and simple method for modeling complex distributions. However, training VAEs often requires considerable hyperparameter tuning to determine the optimal amount of information retained by the latent variable. We study the impact of calibrated decoders, which learn the uncertainty of the decoding distribution and can determine this amount of information automatically, on the VAE performance. While many methods for learning calibrated decoders have been proposed, many of the recent papers that employ VAEs rely on heuristic hyperparameters and ad-hoc modifications instead. We perform the first comprehensive comparative analysis of calibrated decoder and provide recommendations for simple and effective VAE training. Our analysis covers a range of datasets and several single-image and sequential VAE models. We further propose a simple but novel modification to the commonly used Gaussian decoder, which computes the prediction variance analytically. We observe empirically that using heuristic modifications is not necessary with our method.

## item_id: m_1700

TITLE: Investigating Human Priors for Playing Video Games

ABSTRACT: What makes humans so good at solving seemingly complex video games?  Unlike computers, humans bring in a great deal of prior knowledge about the world, enabling efficient decision making. This paper investigates the role of human priors for solving video games. Given a sample game, we conduct a series of ablation studies to quantify the importance of various priors. We do this by modifying the video game environment to systematically mask different types of visual information that could be used by humans as priors. We find that removal of some prior knowledge causes a drastic degradation in the speed with which human players solve the game, e.g. from 2 minutes to over 20 minutes. Furthermore, our results indicate that general priors, such as the importance of objects and visual consistency, are critical for efficient game-play.
