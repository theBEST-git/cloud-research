# Batch 36 — 100 items

## item_id: m_3501

TITLE: Label-Focused Inductive Bias over Latent Object Features in Visual Classification

ABSTRACT: Most neural networks for classification primarily learn features differentiated by input-domain related information such as visual similarity of objects in an image. While this focus is natural behavior, it can inadvertently introduce an inductive bias that conflicts with unseen relations in an implicit output-domain determined by human labeling based on their own world knowledge. Such conflicts can limit generalization of models by potential dominance of the input-domain focused bias in inference.
To overcome this limitation without external resources, we introduce Output-Domain focused Biasing (ODB) training strategy that constructs inductive biases on features differentiated by only output labels. It has four steps: 1) it learns intermediate latent object features in an unsupervised manner; 2) it decouples their visual dependencies by assigning new independent embedding parameters; 3) it captures structured features optimized for the original classification task; and 4) it integrates the structured features with the original visual features for the final prediction.
We implement the ODB on a vision transformer architecture, and achieved significant improvements on image classification benchmarks. This paper offers a straightforward and effective method to obtain and utilize output-domain focused inductive bias for classification mapping two different domains.

## item_id: m_3502

TITLE: Localized Meta-Learning: A PAC-Bayes Analysis for Meta-Leanring Beyond Global Prior

ABSTRACT: Meta-learning methods learn the meta-knowledge among various training tasks and aim to promote the learning of new tasks under the task similarity assumption. However, such meta-knowledge is often represented as a fixed distribution, which is too restrictive to capture various specific task information. In this work, we present a localized meta-learning framework based on PAC-Bayes theory. In particular, we propose a LCC-based prior predictor that allows the meta learner adaptively generate local meta-knowledge for specific task. We further develop a pratical algorithm with deep neural network based on the bound. Empirical results on real-world datasets demonstrate the efficacy of the proposed method. 

## item_id: m_3503

TITLE: Absolute Policy Optimization

ABSTRACT: In recent years, trust region on-policy reinforcement learning has achieved impressive results in addressing complex control tasks and gaming scenarios. However, contemporary state-of-the-art algorithms within this category primarily emphasize improvement in expected performance, lacking the ability to control over the worst-case performance outcomes. To address this limitation, we introduce a novel objective function; by optimizing which, it will lead to guaranteed monotonic improvement in the lower bound of near-total performance samples (absolute performance). Considering this groundbreaking theoretical advancement, we then refine this theoretically grounded algorithm through a series of approximations, resulting in a practical solution called Absolute Policy Optimization (APO). 
Our experiments demonstrate the effectiveness of our approach across challenging continuous control benchmark tasks and extend its applicability to mastering Atari games. Our findings reveal that APO significantly outperforms state-of-the-art policy gradient algorithms, resulting in substantial improvements in both expected performance and worst-case performance.

## item_id: m_3504

TITLE: Three-Head Neural Network Architecture for AlphaZero Learning

ABSTRACT: The search-based reinforcement learning algorithm AlphaZero has been used as a general method for
mastering two-player games Go, chess and Shogi. One crucial ingredient in AlphaZero (and its predecessor AlphaGo Zero) is the two-head network architecture that outputs two estimates --- policy and value --- for one input game state. The merit of such an architecture is that letting policy and value learning share the same representation substantially improved generalization of the neural net.   
A three-head network architecture has been recently proposed that can learn a third action-value head on a fixed dataset the same as for two-head net. Also, using the action-value head in Monte Carlo tree search (MCTS) improved the search efficiency. 
However, effectiveness of the three-head network has not been investigated in an AlphaZero style learning paradigm. 
In this paper, using the game of Hex as a test domain, we conduct an empirical study of the three-head network architecture in AlpahZero learning. We show that the architecture is also advantageous at the zero-style iterative learning. Specifically, we find that three-head network can induce the following benefits: (1) learning can become faster as search takes advantage of the additional action-value head; (2) better prediction results than two-head architecture can be achieved when using additional action-value learning as an auxiliary task.

## item_id: m_3505

TITLE: DNCs require more planning steps

ABSTRACT: A Differentiable Neural Computer (DNC) is a memory-augmented neural computation model capable of learning to solve complex algorithmic tasks, from simple sorting algorithms, through graph problems, to text question answering. In previous works, it was always given a constant number of planning steps to complete its task.
In this work, we argue that the number of planning steps the model is allowed to take, which we call "planning budget", is a constraint that can cause the model to generalize poorly and hurt its ability to fully utilize its external memory.
By introducing an adaptive planning budget that scales with input size during training, the model is better able to utilize its memory space, and achieves substantially better accuracy on input sizes not seen during training.
We experiment with Graph Shortest Path search, which has been used as a benchmark to measure these models in the past, and with the Graph MinCut problem.
In both problems, our proposed approach improves performance and generalizes better compared to the standard planning budget.

## item_id: m_3506

TITLE: Is my Deep Learning Model Learning more than I want it to?

ABSTRACT: Existing deep learning approaches for learning visual features tend to extract more information than what is required for the task at hand. From a privacy preservation perspective, the input visual information is not protected from the model; enabling the model to become more intelligent than it is trained to be. Existing approaches for suppressing additional task learning assume the presence of ground truth labels for the tasks to be suppressed during training time. In this research, we propose a three-fold novel contribution: (i) a novel metric to measure the trust score of a trained deep learning model, (ii) a model-agnostic solution framework for trust score improvement by suppressing all the unwanted tasks, and (iii) a simulated benchmark dataset, PreserveTask, having five different fundamental image classification tasks to study the generalization nature of models. In the first set of experiments, we measure and improve the trust scores of five popular deep learning models: VGG16, VGG19, Inception-v1, MobileNet, and DenseNet and demonstrate that Inception-v1 is having the lowest trust score. Additionally, we show results of our framework on color-MNIST dataset and practical applications of face attribute preservation in Diversity in Faces (DiF) and IMDB-Wiki dataset.

## item_id: m_3507

TITLE: Learning to Query, Reason, and Answer Questions On Ambiguous Texts

ABSTRACT: A key goal of research in conversational systems is to train an interactive agent to help a user with a task. Human conversation, however, is notoriously incomplete, ambiguous, and full of extraneous detail. To operate effectively, the agent must not only understand what was explicitly conveyed but also be able to reason in the presence of missing or unclear information. When unable to resolve ambiguities on its own, the agent must be able to ask the user for the necessary clarifications and incorporate the response in its reasoning. Motivated by this problem we introduce QRAQ ("crack"; Query, Reason, and Answer Questions), a new synthetic domain, in which a User gives an Agent a short story and asks a challenge question. These problems are designed to test the reasoning and interaction capabilities of a learning-based Agent in a setting that requires multiple conversational turns. A good Agent should ask only non-deducible, relevant questions until it has enough information to correctly answer the User's question. We use standard and improved reinforcement learning based memory-network architectures to solve QRAQ problems in the difficult setting where the reward signal only tells the Agent if its final answer to the challenge question is correct or not. To provide an upper-bound to the RL results we also train the same architectures using supervised information that tells the Agent during training which variables to query and the answer to the challenge question. We evaluate our architectures on four QRAQ dataset types, and scale the complexity for each along multiple dimensions.

## item_id: m_3508

TITLE: AdaShift: Decorrelation and Convergence of Adaptive Learning Rate Methods

ABSTRACT: Adam is shown not being able to converge to the optimal solution in certain cases. Researchers recently propose several algorithms to avoid the issue of non-convergence of Adam, but their efficiency turns out to be unsatisfactory in practice. In this paper, we provide a new insight into the non-convergence issue of Adam as well as other adaptive learning rate methods. We argue that there exists an inappropriate correlation between gradient $g_t$ and the second moment term $v_t$ in Adam ($t$ is the timestep), which results in that a large gradient is likely to have small step size while a small gradient may have a large step size. We demonstrate that such unbalanced step sizes are the fundamental cause of non-convergence of Adam, and we further prove that decorrelating $v_t$ and $g_t$ will lead to unbiased step size for each gradient, thus solving the non-convergence problem of Adam. Finally, we propose AdaShift, a novel adaptive learning rate method that decorrelates $v_t$ and $g_t$ by temporal shifting, i.e., using temporally shifted gradient $g_{t-n}$ to calculate $v_t$. The experiment results demonstrate that AdaShift is able to address the non-convergence issue of Adam, while still maintaining a competitive performance with Adam in terms of both training speed and generalization. 

## item_id: m_3509

TITLE: Deep Convolutional Neural Network Design Patterns

ABSTRACT: Recent research in the deep learning field has produced a plethora of new architectures.  At the same time, a growing number of groups are applying deep learning to new applications.  Some of these groups are likely to be composed of inexperienced deep learning practitioners who are baffled by the dizzying array of architecture choices and therefore opt to use an older architecture (i.e., Alexnet).  Here we attempt to bridge this gap by mining the collective knowledge contained in recent deep learning research to discover underlying principles for designing neural network architectures.  In addition, we describe several architectural innovations, including Fractal of FractalNet network, Stagewise Boosting Networks, and Taylor Series Networks (our Caffe code and prototxt files are available at https://github.com/iPhysicist/CNNDesignPatterns). We hope others are inspired to build on our preliminary work.


## item_id: m_3510

TITLE: OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models

ABSTRACT: Large language models (LLMs) have revolutionized natural language processing tasks. However, their practical deployment is hindered by their immense memory and computation requirements. Although recent post-training quantization (PTQ) methods are effective in reducing memory footprint and improving the computational efficiency of LLM, they hand-craft quantization parameters, leading to low performance, especially in extremely low-bit quantization. To tackle this issue, we introduce an Omnidirectionally calibrated Quantization ($\textbf{OmniQuant}$) technique for LLMs, which achieves good performance in diverse quantization settings while maintaining the computational efficiency of PTQ by efficiently optimizing various quantization parameters. OmniQuant comprises two innovative components including Learnable Weight Clipping (LWC) and Learnable Equivalent Transformation (LET). LWC modulates the extreme values of weights by optimizing the clipping threshold. Meanwhile, LET tackles activation outliers by shifting the challenge of quantization from activations to weights. Operating within a differentiable framework using block-wise error minimization, OmniQuant can optimize the quantization process efficiently for both weight-only and weight-activation quantization. For instance, the LLaMA-2 model family size 7-70B can be processed with OmniQuant on a single A100-40G GPU within 1-16 hours using 128 samples. Extensive experiments validate OmniQuant's superior performance across diverse quantization configurations such as W4A4 (4-bit weight, 4-bit activation), W6A6, W4A16, W3A16, and W2A16. Additionally, OmniQuant demonstrates effectiveness in instruction-tuned models and delivers notable improvements in inference speed and memory reduction on real devices. Codes are available at 
\url{https://github.com/OpenGVLab/OmniQuant}.

## item_id: m_3511

TITLE: Causal Balancing for Domain Generalization

ABSTRACT: While machine learning models rapidly advance the state-of-the-art on various real-world tasks, out-of-domain (OOD) generalization remains a challenging problem given the vulnerability of these models to spurious correlations. We propose a balanced mini-batch sampling strategy to transform a biased data distribution into a spurious-free balanced distribution, based on the invariance of the underlying causal mechanisms for the data generation process. We argue that the Bayes optimal classifiers trained on such balanced distribution are minimax optimal across a diverse enough environment space. We also provide an identifiability guarantee of the latent variable model of the proposed data generation process, when utilizing enough train environments. Experiments are conducted on DomainBed, demonstrating empirically that our method obtains the best performance across 20 baselines reported on the benchmark.

## item_id: m_3512

TITLE: Latent Constraints: Learning to Generate Conditionally from Unconditional Generative Models

ABSTRACT: Deep generative neural networks have proven effective at both conditional and unconditional modeling of complex data distributions. Conditional generation enables interactive control, but creating new controls often requires expensive retraining. In this paper, we develop a method to condition generation without retraining the model. By post-hoc learning latent constraints, value functions identify regions in latent space that generate outputs with desired attributes, we can conditionally sample from these regions with gradient-based optimization or amortized actor functions. Combining attribute constraints with a universal “realism” constraint, which enforces similarity to the data distribution, we generate realistic conditional images from an unconditional variational autoencoder. Further, using gradient-based optimization, we demonstrate identity-preserving transformations that make the minimal adjustment in latent space to modify the attributes of an image. Finally, with discrete sequences of musical notes, we demonstrate zero-shot conditional generation, learning latent constraints in the absence of labeled data or a differentiable reward function.

## item_id: m_3513

TITLE: Transformers Can Learn Connectivity in Some Graphs but Not Others

ABSTRACT: Highly competent reasoning capability is essential to ensure the factual correctness of the responses of transformer-based Large Language Models (LLMs), and robust reasoning about transitive relations is instrumental in many settings, such as causal inference. Therefore, it is essential to investigate the capability of transformers in the task of inferring transitive relations (e.g., knowing A causes B and B causes C, we can infer that A causes C). The task of inferring transitive relations is *equivalent* to the task of connectivity in directed graphs (e.g., knowing there is a path from A to B, and there is a path from B to C, we can infer that there is a path from A to C). Past research focused on whether transformers can learn to infer transitivity from in-context examples provided in the input prompt. However, transformers' capability to infer transitive relations from training examples and how scaling affects this ability is unexplored. In this study, we endeavor to answer this question by generating directed graphs to train transformer models of varying sizes and evaluate their ability to infer transitive relations for various graph sizes. Our findings suggest that transformers are capable of learning connectivity on "grid-like'' directed graphs where each node can be embedded in a low-dimensional subspace, and connectivity is easily inferable from the embeddings of the nodes. We find that the dimensionality of the underlying grid graph is a strong predictor of transformers' ability to learn the connectivity task, where higher-dimensional grid graphs pose a greater challenge than low-dimensional grid graphs. In addition, we observe that increasing the model scale leads to increasingly better generalization to infer connectivity over grid graphs. However, if the graph is not a grid graph and contains many disconnected components, transformers struggle to learn the connectivity task, especially when the number of components is large. We also find that transformers benefit more from increasing the graph size than increasing the model size. The code of our experiments is publicly available at [github.com/anonymoususer437/transformers_graph_connectivity](https://github.com/anonymoususer437/transformers_graph_connectivity)

## item_id: m_3514

TITLE: Data De-Duplication and Semantic Enhancement for Contrastive Language-Image Pre-training

ABSTRACT: Benefiting from the countless image-text pairs in the web data, vision-language pre-training models (e.g. CLIP) have emerged as an efficient alternative in learning representations that are transferable across a wide range of downstream tasks.
However, we reveal that the web data are noisy, with significant scene redundancy and misalignment in the image-text pairs, which increase the training expenses and computing resources.
To alleviate these problems, this paper proposes a novel training strategy that comprises two dedicated components, namely Data De-Duplication ($\text{D}^3$) and Semantic Enhancement (SE).
$\text{D}^3$ leverages the pre-clustered data prototypes to decrease the training cost without reducing the data diversity by uniformly sampling a portion of image-text pairs at each training epoch. 
SE utilizes a large language model (LLM) and a visual large language model (VLLM) to refine and augment the text caption, which can help to form a one-to-multiple mapping relation between image and text. 
Furthermore, we employ a Diverse Captions Training Mechanism (DCTM) and a Modality Self-enhancement Training Mechanism (MSTM) for effective training. 
Experimental results indicate that the proposed method achieves state-of-the-art performance on various tasks including image classification, image-text retrieval, object detection, and segmentation (performance improvements varying from 0.2\% to 23.9\% for all datasets) with only half of the training time compared with original CLIP. 
Our code and generated data will be publicly available.

## item_id: m_3515

TITLE: The Comparative Power of ReLU Networks and Polynomial Kernels in the Presence of Sparse Latent Structure

ABSTRACT: There has been a large amount of interest, both in the past and particularly recently, into the relative advantage of different families of universal function approximators, for instance neural networks, polynomials, rational functions, etc. However, current research has focused almost exclusively on understanding this problem in a worst case setting: e.g. characterizing the best L1 or L_{infty} approximation in a box (or sometimes, even under an adversarially constructed data distribution.) In this setting many classical tools from approximation theory can be effectively used.

However, in typical applications we expect data to be high dimensional, but structured -- so, it would only be important to approximate the desired function well on the relevant part of its domain, e.g. a small manifold on which real input data actually lies. Moreover, even within this domain the desired quality of approximation may not be uniform; for instance in classification problems, the approximation needs to be more accurate near the decision boundary. These issues, to the best of our knowledge, have remain unexplored until now.
	
With this in mind, we analyze the performance of neural networks and polynomial kernels in a natural regression setting where the data enjoys sparse latent structure, and the labels depend in a simple way on the latent variables. We give an almost-tight theoretical analysis of the performance of both neural networks and polynomials for this problem, as well as verify our theory with simulations. Our results both involve new (complex-analytic) techniques, which may be of independent interest, and show substantial qualitative differences with what is known in the worst-case setting.

## item_id: m_3516

TITLE: Data Transfer Approaches to Improve Seq-to-Seq Retrosynthesis

ABSTRACT: Retrosynthesis is a problem to infer reactant compounds to synthesize a given
product compound through chemical reactions. Recent studies on retrosynthesis
focus on proposing more sophisticated prediction models, but the dataset to feed
the models also plays an essential role in achieving the best generalizing models.
Generally, a dataset that is best suited for a specific task tends to be small. In
such a case, it is the standard solution to transfer knowledge from a large or
clean dataset in the same domain. In this paper, we conduct a systematic and
intensive examination of data transfer approaches on end-to-end generative models,
in application to retrosynthesis. Experimental results show that typical data transfer
methods can improve test prediction scores of an off-the-shelf Transformer baseline
model. Especially, the pre-training plus fine-tuning approach boosts the accuracy
scores of the baseline, achieving the new state-of-the-art. In addition, we conduct a
manual inspection for the erroneous prediction results. The inspection shows that
the pre-training plus fine-tuning models can generate chemically appropriate or
sensible proposals in almost all cases.

## item_id: m_3517

TITLE: Empowering Test-Time Adaptation with Complementary Vision-Language Knowledge in Open-World Scenarios

ABSTRACT: Test-time adaptation in open-world scenarios (OWTTA), which addresses both domain discrepancy and semantic variance, has gained increasing attention for enabling models to adapt dynamically during inference. Existing approaches mainly rely on discriminative models, whose over-specialized knowledge restricts their adaptability in open-world settings. In contrast, vision-language models (VLMs), trained on diverse large-scale data, provide broader and more transferable knowledge, yet their role in OWTTA remains underexplored.
In this work, we propose a framework empowered by vision-language models, termed Vision-Language knowledge Boosted Open-world test-time adaptation (VLBO).
Specifically, by casting OWTTA into a probabilistic perspective, we first propose agreement-boosted filtering (AF), in which the discriminative model assumes the primary role of filtering out out-of-distribution samples, while the VLM provides a reinforcing signal to refine this process based on its agreement with the discriminative model. We then introduce semantics-boosted adaptation (SA), where VLM-extracted representations serve as semantic guidance to enhance the discriminative model’s adaptation to target domains.
This unified framework leverages the complementary strengths of vision-language models and discriminative counterparts, enabling robust and effective adaptation in open-world scenarios. Extensive experiments across multiple benchmarks demonstrate the consistent effectiveness of the proposed method.

## item_id: m_3518

TITLE: Curriculum Learning for Deep Generative Models with Clustering

ABSTRACT: Training generative models like Generative Adversarial Network (GAN)  is challenging for noisy data. A novel curriculum learning algorithm pertaining to clustering is proposed to address this issue in this paper. The curriculum construction is based on the centrality of underlying clusters in data points.  The data points of high centrality takes priority of being fed into generative models during training. To make our algorithm scalable to large-scale data, the active set is devised, in the sense that every round of training proceeds only on an active subset containing a small fraction of already trained data and the incremental data of lower centrality. Moreover, the geometric analysis is presented to interpret the necessity of cluster curriculum for generative models. The experiments on cat and human-face data validate that our algorithm is able to learn the optimal generative models (e.g. ProGAN) with respect to specified quality metrics for noisy data. An interesting finding is that the optimal cluster curriculum is closely related to the critical point of the geometric percolation process formulated in the paper.

## item_id: m_3519

TITLE: Coherence-based Label Propagation over Time Series for Accelerated Active Learning

ABSTRACT: Time-series data are ubiquitous these days, but lack of the labels in time-series data is regarded as a hurdle for its broad applicability. Meanwhile, active learning has been successfully adopted to reduce the labeling efforts in various tasks. Thus, this paper addresses an important issue, time-series active learning. Inspired by the temporal coherence in time-series data, where consecutive data points tend to have the same label, our label propagation framework, called TCLP, automatically assigns a queried label to the data points within an accurately estimated time-series segment, thereby significantly boosting the impact of an individual query. Compared with traditional time-series active learning, TCLP is shown to improve the classification accuracy by up to 7.1 times when only 0.8% of data points in the entire time series are queried for their labels.

## item_id: m_3520

TITLE: NEUROGENESIS-INSPIRED DICTIONARY LEARNING: ONLINE MODEL ADAPTION IN A CHANGING WORLD

ABSTRACT: In this paper, we focus on online representation learning in non-stationary environments which may require continuous adaptation of model’s architecture. We propose a novel online dictionary-learning (sparse-coding) framework which incorporates the addition and deletion of hidden units (dictionary elements), and is inspired by the adult neurogenesis phenomenon in the dentate gyrus of the hippocampus, known to be associated with improved cognitive function and adaptation to new environments. In the online learning setting, where new input instances arrive sequentially in batches, the “neuronal birth” is implemented by adding new units with random initial weights (random dictionary elements); the number of new units is determined by the current performance (representation error) of the dictionary, higher error causing an increase in the birth rate. “Neuronal death” is implemented by imposing l1/l2-regularization (group sparsity) on the dictionary within the block-coordinate descent optimization at each iteration of our online alternating minimization scheme, which iterates between the code and dictionary updates. Finally, hidden unit connectivity adaptation is facilitated by introducing sparsity in dictionary elements. Our empirical evaluation on several real-life datasets (images and language) as well as on synthetic data demonstrates that the proposed approach can considerably outperform the state-of-art fixed-size (nonadaptive) online sparse coding of Mairal et al. (2009) in the presence of nonstationary data. Moreover, we identify certain properties of the data (e.g., sparse inputs with nearly non-overlapping supports) and of the model (e.g., dictionary sparsity) associated with such improvements.

## item_id: m_3521

TITLE: Self-Supervised Learning of Object Motion Through Adversarial Video Prediction

ABSTRACT: Can we build models that automatically learn about object motion from raw, unlabeled videos? In this paper, we study the problem of multi-step video prediction, where the goal is to predict a sequence of future frames conditioned on a short context. We focus specifically on two aspects of video prediction: accurately modeling object motion, and producing naturalistic image predictions. Our model is based on a flow-based generator network with a discriminator used to improve prediction quality. The implicit flow in the generator can be examined to determine its accuracy, and the predicted images can be evaluated for image quality. We argue that these two metrics are critical for understanding whether the model has effectively learned object motion, and propose a novel evaluation benchmark based on ground truth object flow. Our network achieves state-of-the-art results in terms of both the realism of the predicted images, as determined by human judges, and the accuracy of the predicted flow. Videos and full results can be viewed on the supplementary website: \url{https://sites.google.com/site/omvideoprediction}.

## item_id: m_3522

TITLE: Divide and Conquer with Neural Networks

ABSTRACT: We consider the learning of algorithmic tasks by mere observation of input-output pairs. 
Rather than studying this as a black-box discrete regression problem with no assumption whatsoever 
on the input-output mapping, we concentrate on tasks that are amenable to the principle of divide and conquer, and study what are its implications in terms of learning. 

This principle creates a powerful inductive bias that we exploit with neural architectures that are defined recursively, by learning two scale-invariant atomic operators: how to split a given input into two disjoint sets, and how to merge two partially solved tasks into a larger partial solution. The scale invariance creates parameter sharing across all stages of the architecture, and the dynamic design creates architectures whose complexity can be tuned in a differentiable manner.

As a result, our model is trained by backpropagation not only to minimize the errors at the output, but also to do so as efficiently as possible, by enforcing shallower computation graphs. Moreover, thanks to the scale invariance, the model can be trained only with only input/output pairs, removing the need to know oracle intermediate split and merge decisions. As it turns out, accuracy and complexity are not independent qualities, and we verify empirically that when the learnt complexity matches the underlying complexity of the task, this results in higher accuracy and better generalization in two paradigmatic problems: sorting and finding planar convex hulls.

## item_id: m_3523

TITLE: Constructing Semantics-Aware Adversarial Examples with Probabilistic Perspective

ABSTRACT: In this study, we introduce a novel, probabilistic perspective for generating adversarial examples. Within this view, geometric constraints on adversarial examples are interpreted as distributions, facilitating the transition from geometric constraints to data-driven semantic constraints. Proceeding from this perspective, we develop an innovative approach for generating semantics-aware adversarial examples in a principled manner. Our approach empowers individuals to incorporate their personal comprehension of semantics into the model. Through human evaluation, we validate that our semantics-aware adversarial examples maintain their inherent meaning. Experimental findings on the MNIST, SVHN and CIFAR10 datasets demonstrate that our semantics-aware adversarial examples can effectively circumvent robust adversarial training methods tailored for traditional adversarial attacks.

## item_id: m_3524

TITLE: On the Tunability of Optimizers in Deep Learning

ABSTRACT: There is no consensus yet on the question whether adaptive gradient methods like Adam are easier to use than non-adaptive optimization methods like SGD. In this work, we fill in the important, yet ambiguous concept of ‘ease-of-use’ by defining an optimizer’s tunability:  How easy is it to find good hyperparameter configurations using automatic random hyperparameter search? We propose a practical and universal quantitative measure for optimizer tunability that can form the basis for a fair optimizer benchmark.  Evaluating a variety of optimizers on an extensive set of standard datasets and architectures, we find  that Adam is the most tunable for the majority of problems, especially with a low budget for hyperparameter tuning.

## item_id: m_3525

TITLE: Pushing the Limits of Fewshot Anomaly Detection in Industry Vision: Graphcore

ABSTRACT: In the area of few-shot anomaly detection (FSAD), efficient visual feature plays an essential role in the memory bank $\mathcal{M}$-based methods. However, these methods do not account for the relationship between the visual feature and its rotated visual feature, drastically limiting the anomaly detection performance. To push the limits, we reveal that rotation-invariant feature property has a significant impact on industrial-based FSAD. Specifically, we utilize graph representation in FSAD and provide a novel visual isometric invariant feature (VIIF) as an anomaly measurement feature. As a result, VIIF can robustly improve the anomaly discriminating ability and can further reduce the size of redundant features stored in $\mathcal{M}$ by a large amount. Besides, we provide a novel model GraphCore via VIIFs that can fast implement unsupervised FSAD training and improve the performance of anomaly detection. A comprehensive evaluation is provided for comparing GraphCore and other SOTA anomaly detection models under our proposed few-shot anomaly detection setting, which shows GraphCore can increase average AUC by 5.8%, 4.1%, 3.4%, and 1.6% on MVTec AD and by 25.5%, 22.0%, 16.9%, and 14.1% on MPDD for 1, 2, 4, and 8-shot cases, respectively.

## item_id: m_3526

TITLE: Reasoning to Learn from Latent Thoughts

ABSTRACT: Compute scaling for language model (LM) pretraining has outpaced the growth of human-written texts, leading to concerns that data will become the bottleneck to LM scaling. To continue scaling pretraining in this data-constrained regime, we propose that explicitly modeling and inferring the latent thoughts that underlie the text generation process can significantly improve pretraining data efficiency. Intuitively, our approach views web text as the compressed final outcome of a verbose human thought process and that the latent thoughts contain important contextual knowledge and reasoning steps that are critical to data-efficient learning. We empirically demonstrate the effectiveness of our approach through data-constrained continued pretraining for math. We first show that synthetic data approaches to inferring latent thoughts significantly improve data efficiency, outperforming training on the same amount of raw data. Furthermore, we demonstrate latent thought inference without a strong teacher, where an LM bootstraps its own performance by using an EM algorithm to iteratively improve the capability of the trained LM and the quality of thought-augmented pretraining data. We show that a 1B LM can bootstrap its performance across at least three iterations and significantly outperform baselines trained on raw data, with increasing gains from additional inference compute when performing the E-step. The gains from inference scaling and EM iterations suggest new opportunities for scaling data-constrained pretraining.

## item_id: m_3527

TITLE: Multi-label learning with the RNNs for Fashion Search

ABSTRACT: We build a large-scale visual search system which finds similar product images given a fashion item. Defining similarity among arbitrary fashion-products is still remains a challenging problem, even there is no exact ground-truth. To resolve this problem, we define more than 90 fashion-related attributes, and combination of these attributes can represent thousands of unique fashion-styles. We then introduce to use the recurrent neural networks (RNNs) recognising multi fashion-attributes with the end-to-end manner. To build our system at scale, these fashion-attributes are again used to build an inverted indexing scheme. In addition to these fashion-attributes for semantic similarity, we extract colour and appearance features in a region-of-interest (ROI) of a fashion item for visual similarity. By sharing our approach, we expect active discussion on that how to apply current deep learning researches into the e-commerce industry.

## item_id: m_3528

TITLE: Decoy-enhanced Saliency Maps 

ABSTRACT: Saliency methods can make deep neural network predictions more interpretable by identifying a set of critical features in an input sample, such as pixels that contribute most strongly to a prediction made by an image classifier. Unfortunately, recent evidence suggests that many saliency methods poorly perform, especially in situations where gradients are saturated, inputs contain adversarial perturbations, or predictions rely upon inter-feature dependence. To address these issues, we propose a framework that improves the robustness of saliency methods by following a two-step procedure. First, we introduce a perturbation mechanism that subtly varies the input sample without changing its intermediate representations. Using this approach, we can gather a corpus of perturbed data samples while ensuring that the perturbed and original input samples follow the same distribution. Second, we compute saliency maps for the perturbed samples and propose a new method to aggregate saliency maps. With this design, we offset the gradient saturation influence upon interpretation. From a theoretical perspective, we show that the aggregated saliency map not only captures inter-feature dependence but, more importantly, is robust against previously described adversarial perturbation methods. Following our theoretical analysis, we present experimental results suggesting that, both qualitatively and quantitatively, our saliency method outperforms existing methods, in a variety of applications.

## item_id: m_3529

TITLE: Learning Invariant Feature Spaces to Transfer Skills with Reinforcement Learning

ABSTRACT: People can learn a wide range of tasks from their own experience, but can also learn from observing other creatures. This can accelerate acquisition of new skills even when the observed agent differs substantially from the learning agent in terms of morphology. In this paper, we examine how reinforcement learning algorithms can transfer knowledge between morphologically different agents (e.g., different robots). We introduce a problem formulation where twp agents are tasked with learning multiple skills by sharing information. Our method uses the skills that were learned by both agents to train invariant feature spaces that can then be used to transfer other skills from one agent to another. The process of learning these invariant feature spaces can be viewed as a kind of ``analogy making,'' or implicit learning of partial correspondences between two distinct domains. We evaluate our transfer learning algorithm in two simulated robotic manipulation skills, and illustrate that we can transfer knowledge between simulated robotic arms with different numbers of links, as well as simulated arms with different actuation mechanisms, where one robot is torque-driven while the other is tendon-driven.

## item_id: m_3530

TITLE: On the Importance of Distraction-Robust Representations for Robot Learning

ABSTRACT: Representation Learning methods can allow the application of Reinforcement Learning algorithms when a high dimensionality in a robot's perceptions would otherwise prove prohibitive. Consequently, unsupervised Representation Learning components often feature in robot control algorithms that assume high-dimensional camera images as the principal source of information.
In their design and performance, these algorithms often benefit from the controlled nature of the simulation or laboratory conditions they are evaluated in. However, these settings fail to acknowledge the stochasticity of most real-world environments.
In this work, we introduce the concept of Distraction-Robust Representation Learning. We argue that environment noise and other distractions require learned representations to encode the robot's expected perceptions rather than the observed ones. Our experimental evaluations demonstrate that representations learned with a traditional dimensionality reduction algorithm are strongly susceptible to distractions in a robot's environment.
We propose an Encoder-Decoder architecture that produces representations that allow the learning outcomes of robot control tasks to remain unaffected by these distractions.

## item_id: m_3531

TITLE: EMPIR: Ensembles of Mixed Precision Deep Networks for Increased Robustness Against Adversarial Attacks

ABSTRACT: Ensuring robustness of Deep Neural Networks (DNNs) is crucial to their adoption in safety-critical applications such as self-driving cars, drones, and healthcare. Notably, DNNs are vulnerable to adversarial attacks in which small input perturbations can produce catastrophic misclassifications. In this work, we propose EMPIR, ensembles of quantized DNN models with different numerical precisions, as a new approach to increase robustness against adversarial attacks. EMPIR is based on the observation that quantized neural networks often demonstrate much higher robustness to adversarial attacks than full precision networks, but at the cost of a substantial loss in accuracy on the original (unperturbed) inputs. EMPIR overcomes this limitation to achieve the ``best of both worlds", i.e., the higher unperturbed accuracies of the full precision models combined with the higher robustness of the low precision models, by composing them in an ensemble. Further, as low precision DNN models have significantly lower computational and storage requirements than full precision models, EMPIR models only incur modest compute and memory overheads compared to a single full-precision model (<25% in our evaluations). We evaluate EMPIR across a suite of DNNs for 3 different image recognition tasks (MNIST, CIFAR-10 and ImageNet) and under 4 different adversarial attacks. Our results indicate that EMPIR boosts the average adversarial accuracies by 42.6%, 15.2% and 10.5% for the DNN models trained on the MNIST, CIFAR-10 and ImageNet datasets respectively, when compared to single full-precision models, without sacrificing accuracy on the unperturbed inputs.

## item_id: m_3532

TITLE: Amortised MAP Inference for Image Super-resolution

ABSTRACT: Image super-resolution (SR) is an underdetermined inverse problem, where a large number of plausible high resolution images can explain the same downsampled image. Most current single image SR methods use empirical risk minimisation, often with a pixel-wise mean squared error (MSE) loss.
However, the outputs from such methods tend to be blurry, over-smoothed and generally appear implausible. A more desirable approach would employ Maximum a Posteriori (MAP) inference, preferring solutions that always have a high probability under the image prior, and thus appear more plausible. Direct MAP estimation for SR is non-trivial, as it requires us to build a model for the image prior from samples. Here we introduce new methods for \emph{amortised MAP inference} whereby we calculate the MAP estimate directly using a convolutional neural network. We first introduce a novel neural network architecture that performs a projection to the affine subspace of valid SR solutions ensuring that the high resolution output of the network is always consistent with the low resolution input. We show that, using this architecture, the amortised MAP inference problem reduces to minimising the cross-entropy between two distributions, similar to training generative models. We propose three methods to solve this optimisation problem: (1) Generative Adversarial Networks (GAN) (2) denoiser-guided SR which backpropagates gradient-estimates from denoising to train the network, and (3) a baseline method using a maximum-likelihood-trained image prior. Our experiments show that the GAN based approach performs best on real image data. Lastly, we establish a connection between GANs and amortised variational inference as in e.g. variational autoencoders.

## item_id: m_3533

TITLE: JudgeAgent: Knowledge-wise and Dynamic LLM Evaluation with Agent-as-Interviewer

ABSTRACT: Current evaluation paradigms for large language models (LLMs) suffer from overestimated or biased evaluation and mismatched question difficulty, leading to incomplete evaluations of LLM's knowledge and capability boundaries, which hinder LLM's effective application and optimization. 
To address these challenges, we propose Agent-as-Interviewer, a dynamic evaluation paradigm that employs LLM agents to conduct multi-turn interactions for evaluation. 
Unlike current benchmarking or dynamic interaction paradigms, Agent-as-Interviewer utilizes agents to call knowledge tools for wider and deeper knowledge in the dynamic multi-turn question generation, achieving more complete evaluations of the LLM's knowledge boundaries. 
It also leverages agents to plan query strategies for adjustment of the question difficulty levels, enhancing the difficulty control to match the actual capabilities of target LLMs.
Based on this paradigm, we develop JudgeAgent, a knowledge-wise dynamic evaluation framework that employs knowledge-driven synthesis as the agent's tool, and uses difficulty scoring as strategy guidance, thereby finally providing valuable suggestions to help targets optimize themselves.
Extensive experiments validate the effectiveness of JudgeAgent's suggestions, demonstrating that Agent-as-Interviewer can accurately identify the knowledge and capability boundaries of target models.
The source code is available on https://anonymous.4open.science/r/JudgeAgent.

## item_id: m_3534

TITLE: Beyond Games: Bringing Exploration to Robots in Real-world

ABSTRACT: Exploration has been a long standing problem in both model-based and model-free learning methods for sensorimotor control. While there has been major advances over the years, most of these successes have been demonstrated in either video games or simulation environments. This is primarily because the rewards (even the intrinsic ones) are non-differentiable since they are function of the environment (which is a black-box). In this paper, we focus on the policy optimization aspect of the intrinsic reward function. Specifically, by using a local approximation, we formulate intrinsic reward as a differentiable function so as to perform policy optimization using likelihood maximization -- much like supervised learning instead of reinforcement learning. This leads to a significantly sample efficient exploration policy. Our experiments clearly show that our approach outperforms both on-policy and off-policy optimization approaches like REINFORCE and DQN respectively. But most importantly, we are able to implement an exploration policy on a robot which learns to interact with objects completely from scratch just using data collected via the differentiable exploration module. See project videos at https://doubleblindICLR.github.io/robot-exploration/

## item_id: m_3535

TITLE: Stochastic gradient descent performs variational inference, converges to limit cycles for deep networks

ABSTRACT: Stochastic gradient descent (SGD) is widely believed to perform implicit regularization when used to train deep neural networks, but the precise manner in which this occurs has thus far been elusive. We prove that SGD minimizes an average potential over the posterior distribution of weights along with an entropic regularization term. This potential is however not the original loss function in general. So SGD does perform variational inference, but for a different loss than the one used to compute the gradients. Even more surprisingly, SGD does not even converge in the classical sense: we show that the most likely trajectories of SGD for deep networks do not behave like Brownian motion around critical points. Instead, they resemble closed loops with deterministic components. We prove that such out-of-equilibrium behavior is a consequence of highly non-isotropic gradient noise in SGD; the covariance matrix of mini-batch gradients for deep networks has a rank as small as 1% of its dimension. We provide extensive empirical validation of these claims, proven in the appendix.

## item_id: m_3536

TITLE: Beyond Textual CoT: Interleaved Text-Image Chains with Deep Confidence Reasoning for Image Editing

ABSTRACT: Image editing with natural language has gained significant popularity, yet existing methods struggle with intricate object intersections and fine-grained spatial relationships due to the lack of an explicit reasoning process. While Chain-of-Thought (CoT) has been explored to enhance reasoning, purely textual CoT or CoT augmented with coordinate information is fundamentally limited in its ability to represent intricate visual layouts and lacks the necessary visual cues to guide the generation of fine-grained, pixel-level details. To address these challenges, we propose $\textbf{Mu}$ltimodal $\textbf{R}$easoning $\textbf{E}$dit ($\textbf{MURE}$), a novel framework that $\textit{shifts the visual editing process from purely text-based reasoning to a series of interleaved textual and visual rationales}$. Our framework performs image editing using a natively multimodal, interleaved text-image CoT. This approach generates a step-by-step chain of reasoning where a textual description is followed by a corresponding visual cue, such as a positional mask that defined intended edited regions or a representation of new content. Furthermore, to mitigate the hallucination phenomenon of large language models, we introduce $\textbf{M}$ulti$\textbf{m}$odal $\textbf{D}$eep $\textbf{C}$onfidence ($\textbf{MMDC}$) reasoning paradigm. This paradigm explores a tree of visual reasoning paths at each step. By pruning low-quality branches using a deep confidence score from a reward model, it ensures the model consistently follows a high-quality trajectory towards the final edited result. The proposed method decomposes complex editing tasks into interdependent sub-tasks, achieving greater precision at each stage and yielding high-fidelity edited results. We define the formulation for interleaved text-image chains and release the first CoT-Edit-14K dataset, comprising 14K high-quality editing examples. Extensive experiments show that our method yields significant improvements across three image editing benchmarks, establishing a more effective reasoning framework for visual editing.

## item_id: m_3537

TITLE: Diversely Stale Parameters for Efficient Training of Deep Convolutional Networks

ABSTRACT: The backpropagation algorithm is the most popular algorithm training neural networks nowadays. However, it suffers from the forward locking, backward locking and update locking problems, especially when a neural network is so large that its layers are distributed across multiple devices. Existing solutions either can only handle one locking problem or lead to severe accuracy loss or memory inefficiency. Moreover, none of them consider the straggler problem among devices. In this paper, we propose \textbf{Layer-wise Staleness} and a novel efficient training algorithm, \textbf{Diversely Stale Parameters} (DSP), which can address all these challenges without loss of accuracy nor memory issue. We also analyze the convergence of DSP with two popular gradient-based methods and prove that both of them are guaranteed to converge to critical points for non-convex problems. Finally, extensive experimental results on training deep convolutional neural networks demonstrate that our proposed DSP algorithm can achieve significant training speedup with stronger robustness and better generalization than compared methods.

## item_id: m_3538

TITLE: Convolutional Mesh Autoencoders for 3D Face Representation

ABSTRACT: Convolutional neural networks (CNNs) have achieved state of the art performance on recognizing and representing audio, images, videos and 3D volumes; that is, domains where the input can be characterized by a regular graph structure. 
However, generalizing CNNs to irregular domains like 3D meshes is challenging. Additionally, training data for 3D meshes is often limited. In this work, we generalize convolutional autoencoders to mesh surfaces. We perform spectral decomposition of meshes and apply convolutions directly in frequency space. In addition, we use max pooling and introduce upsampling within the network to represent meshes in a low dimensional space. We construct a complex dataset of 20,466 high resolution meshes with extreme facial expressions and encode it using our Convolutional Mesh Autoencoder. Despite limited training data, our method outperforms state-of-the-art PCA models of faces with 50% lower error,  while using 75% fewer parameters.

## item_id: m_3539

TITLE: Mechanistic Mode Connectivity

ABSTRACT: With the rise of pretrained models, fine-tuning has become of central importance in deep learning. However, unlike retraining from scratch, fine-tuning can fail to qualitatively change the behavior of a pre-trained network. For instance, we find in practice that naive fine-tuning does not eliminate a model’s sensitivity to spurious features. To understand and address this limitation, we study the geometry of neural network loss landscapes through the lens of mode-connectivity. Our work addresses two questions about mode-connectivity: 1) Are models trained on different data distributions mode-connected? 2) Can we fine tune a pre-trained model to switch modes? We define a notion of mechanistic mode-connectivity, and find that only models that already share the same invariances (which we call “mechanistically similar”) are mechanistically mode-connected. We hypothesize this property explains inability of naive fine-tuning methods to induce invariance to spurious features. Based on our analysis, we propose and validate a method of “mechanistic fine-tuning” called connectivity-based fine-tuning (CBFT)

## item_id: m_3540

TITLE: LVCap-Eval: Towards Holistic Long Video Caption Evaluation for Multimodal LLMs

ABSTRACT: Generating coherent and factually grounded captions for long-form videos is a critical yet underexplored challenge for multimodal large language models (MLLMs).
Existing benchmarks, which predominantly feature short clips, are insufficient for evaluating a model's ability to capture narrative structure and fine-grained details over extended durations.
To address this gap, we introduce LVCap-Eval, a benchmark for long-form video captioning. 
LVCap-Eval comprises 200 videos from six diverse domains, ranging from 2 to 20 minutes, and features a dual-dimension evaluation protocol that assesses both scene-level narrative coherence and event-level factual accuracy.
To facilitate model improvement, we also provide a pipeline for generating a training corpus, demonstrating that fine-tuning with as few as 7,000 samples yields substantial gains.
Our evaluation of existing MLLMs on this benchmark reveals a significant performance disparity:
while leading closed-source models (e.g., Gemini-2.5-Pro) perform robustly across various video durations, their open-source counterparts degrade sharply as video length increases. 
Finally, our analysis of these model failures highlights potential directions for improving the long-video comprehension of MLLMs.

## item_id: m_3541

TITLE: Black Box Recursive Translations for Molecular Optimization

ABSTRACT: Machine learning algorithms for generating molecular structures offer a promising new approach to drug discovery. We cast molecular optimization as a translation problem, where the goal is to map an input compound to a target compound with improved biochemical properties. Remarkably, we observe that when generated molecules are iteratively fed back into the translator, molecular compound attributes improve with each step. We show that this finding is invariant to the choice of translation model, making this a "black box" algorithm. We call this method Black Box Recursive Translation (BBRT), a new inference method for molecular property optimization. This simple, powerful technique operates strictly on the inputs and outputs of any translation model. We obtain new state-of-the-art results for molecular property optimization tasks using our simple drop-in replacement with well-known sequence and graph-based models. Our method provides a significant boost in performance relative to its non-recursive peers with just a simple "``for" loop. Further, BBRT is highly interpretable, allowing users to map the evolution of newly discovered compounds from known starting points. 

## item_id: m_3542

TITLE: Compact Neural Networks based on the Multiscale Entanglement Renormalization Ansatz

ABSTRACT: The goal of this paper is to demonstrate a method for tensorizing neural networks based upon an efficient way of approximating scale invariant quantum states, the Multi-scale Entanglement Renormalization Ansatz (MERA). We employ MERA as a replacement for linear layers in a neural network and test this implementation on the CIFAR-10 dataset. The proposed method outperforms factorization using tensor trains, providing greater compression for the same level of accuracy and greater accuracy for the same level of compression. We demonstrate MERA-layers with 3900 times fewer parameters and a reduction in accuracy of less than 1% compared to the equivalent fully connected layers.


## item_id: m_3543

TITLE: learning hierarchical multi-agent cooperation with long short-term intention

ABSTRACT: Communication is a significant method to relieve partial observable and non-stationary problems in Multi-Agent System. However, most of existing work needs to persistently communicate by exchanging partial observation or latent embeddings (intention) which is unrealistic in real-world settings. To overcome this problem, we propose learning hierarchical multi-agent cooperation with long short-term intention (HLSI), a hierarchical multi-agent cooperation framework. In our work, each agent communicates by sharing high-level policy's latent embeddings (long-term intention) which keeps contant until macro action change. To make the communication messages contain more useful content, we maximize mutual information between agent's macro action and agent's future trajectory conditioned on historical trajectory.  Agent integrates these messages through the attention mechanism. Then, long short-term intention fusion module will fuse the long-term intention received from other agents and short-term intention inferred by a behaivor inference network to approximate other agents' real short-term intention, which helps agent better understand others' next behavior. We provide comprehensive evaluation and ablations studies in multi-agent cooperative settings. The results show that our method achieves better performance than other multi-agent communication and hierarchical multi-agent reinforcement learning baselines.

## item_id: m_3544

TITLE: FAST OBJECT LOCALIZATION VIA SENSITIVITY ANALYSIS

ABSTRACT: Deep Convolutional Neural Networks (CNNs) have been repeatedly shown to perform well on image classification tasks, successfully recognizing a broad array of objects when given sufficient training data. Methods for object localization, however, are still in need of substantial improvement. Common approaches to this problem involve the use of a sliding window, sometimes at multiple scales, providing input to a deep CNN trained to classify the contents of the window. In general, these approaches are time consuming, requiring many classification calculations. In this paper, we offer a fundamentally different approach to the localization of recognized objects in images. Our method is predicated on the idea that a deep CNN capable of recognizing an object must implicitly contain knowledge about object location in its connection weights. We provide a simple method to interpret classifier weights in the context of individual classified images. This method involves the calculation of the derivative of network generated activation patterns, such as the activation of output class label units, with regard to each in- put pixel, performing a sensitivity analysis that identifies the pixels that, in a local sense, have the greatest influence on internal representations and object recognition. These derivatives can be efficiently computed using a single backward pass through the deep CNN classifier, producing a sensitivity map of the image. We demonstrate that a simple linear mapping can be learned from sensitivity maps to bounding box coordinates, localizing the recognized object. Our experimental results, using real-world data sets for which ground truth localization information is known, reveal competitive accuracy from our fast technique.

## item_id: m_3545

TITLE: Mirror Mean-Field Langevin Dynamics

ABSTRACT: The mean-field Langevin dynamics (MFLD) minimizes an entropy-regularized nonlinear convex functional on the Wasserstein space over $\mathbb{R}^d$, and has gained attention recently as a model for the gradient descent dynamics of interacting particle systems such as infinite-width two-layer neural networks. However, many problems of interest have constrained domains, which are not solved by existing mean-field algorithms due to the global diffusion term. We study the optimization of probability measures constrained to a convex subset of $\mathbb{R}^d$ by proposing the mirror mean-field Langevin dynamics (MMFLD), an extension of MFLD to the mirror Langevin framework. We obtain linear convergence guarantees for the continuous MMFLD via a uniform log-Sobolev inequality, and uniform-in-time propagation of chaos results for its time- and particle-discretized counterpart.

## item_id: m_3546

TITLE: Universal Approximation with Deep Narrow Networks

ABSTRACT: The classical Universal Approximation Theorem certifies that the universal approximation property holds for the class of neural networks of arbitrary width. Here we consider the natural `dual' theorem for width-bounded networks of arbitrary depth. Precisely, let $n$ be the number of inputs neurons, $m$ be the number of output neurons, and let $\rho$ be any nonaffine continuous function, with a continuous nonzero derivative at some point. Then we show that the class of neural networks of arbitrary depth, width $n + m + 2$, and activation function $\rho$, exhibits the universal approximation property with respect to the uniform norm on compact subsets of $\mathbb{R}^n$. This covers every activation function possible to use in practice; in particular this includes polynomial activation functions, making this genuinely different to the classical case. We go on to consider extensions of this result. First we show an analogous result for a certain class of nowhere differentiable activation functions. Second we establish an analogous result for noncompact domains, by showing that deep narrow networks with the ReLU activation function exhibit the universal approximation property with respect to the $p$-norm on $\mathbb{R}^n$. Finally we show that width of only $n + m + 1$ suffices for `most' activation functions.

## item_id: m_3547

TITLE: ADELT: Unsupervised Transpilation Between Deep Learning Frameworks

ABSTRACT: We propose Adversarial DEep Learning Transpiler (ADELT) for source-to-source transpilation between deep learning frameworks. Unlike prior approaches, ADELT formulates the transpilation problem as mapping API keyword (an API function name or a parameter name). Based on contextual embeddings extracted by a BERT for code, we train aligned API embeddings in a domain-adversarial setting, upon which we generate a dictionary for keyword translation. The model is trained on our unlabeled DL corpus from web crawl data, without using any hand-crafted rules and parallel data. Our method outperforms state-of-the-art transpilers on multiple transpilation pairs including PyTorch-Keras and PyTorch-MXNet. We make our code, corpus, and evaluation benchmark publicly available.

## item_id: m_3548

TITLE: Graph Neural Networks Provably Benefit from Structural Information: A Feature Learning Perspective

ABSTRACT: Graph neural networks (GNNs) have shown remarkable capabilities in learning from graph-structured data, outperforming traditional multilayer perceptrons (MLPs) in numerous graph applications. Despite these advantages, there has been limited theoretical exploration into why GNNs are so effective, particularly from the perspective of feature learning. This study aims to address this gap by examining the role of graph convolution in feature learning theory under a specific data generative model. We undertake a comparative analysis of the optimization and generalization between two-layer graph convolutional networks (GCNs) and their convolutional neural network (CNN) counterparts. Our findings reveal that graph convolution significantly enhances the regime of low test error over CNNs. This highlights a substantial discrepancy between GNNs and MLPs in terms of generalization capacity, a conclusion further supported by our empirical simulations on both synthetic and real-world datasets.

## item_id: m_3549

TITLE: FRACTAL CALIBRATION FOR LONG-TAILED OBJECT DETECTION

ABSTRACT: Real-world datasets follow an imbalanced distribution, which poses significant
challenges in rare-category object detection. Recent studies tackle this problem
by developing re-weighting and re-sampling methods, that utilise the class frequencies of the dataset. However, these techniques focus solely on the frequency statistics and ignore the distribution of the classes in image space, missing important information. In contrast to them, we propose Fractal CALibration (FRACAL): a novel post-calibration method for long-tailed object detection. FRACAL
devises a logit adjustment method that utilises the fractal dimension to estimate how uniformly classes are distributed in image space. During inference, it uses the fractal dimension to inversely downweight the probabilities of uniformly spaced class predictions achieving balance in two axes: between frequent and rare categories, and between uniformly spaced and sparsely spaced classes. FRACAL is a
post-processing method and it does not require any training, also it can be combined with many off-the-shelf models such as one-stage sigmoid detectors and two-stage instance segmentation models. FRACAL boosts the rare class performance by up to 8.6% and surpasses all previous methods on LVIS dataset, while showing good generalisation to other datasets such as COCO, V3Det and OpenImages. We provide the code in the Appendix.

## item_id: m_3550

TITLE: SSOLE: Rethinking Orthogonal Low-rank Embedding for Self-Supervised Learning

ABSTRACT: Self-supervised learning (SSL) aims to learn meaningful representations from unlabeled data. Orthogonal Low-rank Embedding (OLE) shows promise for SSL by enhancing intra-class similarity in a low-rank subspace and promoting inter-class dissimilarity in a high-rank subspace, making it particularly suitable for multi-view learning tasks. However, directly applying OLE to SSL poses significant challenges: (1) the virtually infinite number of "classes" in SSL makes achieving the OLE objective impractical, leading to representational collapse; and (2) low-rank constraints may fail to distinguish between positively and negatively correlated features, further undermining learning. To address these issues, we propose SSOLE (Self-Supervised Orthogonal Low-rank Embedding), a novel framework that integrates OLE principles into SSL by (1) decoupling the low-rank and high-rank enforcement to align with SSL objectives; and (2) applying low-rank constraints to feature deviations from their mean, ensuring better alignment of positive pairs by accounting for the signs of cosine similarities. Our theoretical analysis and empirical results demonstrate that these adaptations are crucial to SSOLE’s effectiveness. Moreover, SSOLE achieves competitive performance across SSL benchmarks without relying on large batch sizes, memory banks, or dual-encoder architectures, making it an efficient and scalable solution for self-supervised tasks. Code is available at https://github.com/husthuaan/ssole.

## item_id: m_3551

TITLE: Scalable Unbalanced Optimal Transport using Generative Adversarial Networks

ABSTRACT: Generative adversarial networks (GANs) are an expressive class of neural generative models with tremendous success in modeling high-dimensional continuous measures. In this paper, we present a scalable method for unbalanced optimal transport (OT) based on the generative-adversarial framework. We formulate unbalanced OT as a problem of simultaneously learning a transport map and a scaling factor that push a source measure to a target measure in a cost-optimal manner. We provide theoretical justification for this formulation, showing that it is closely related to an existing static formulation by Liero et al. (2018). We then propose an algorithm for solving this problem based on stochastic alternating gradient updates, similar in practice to GANs, and perform numerical experiments demonstrating how this methodology can be applied to population modeling.

## item_id: m_3552

TITLE: Don't encrypt the data; just approximate the model \ Towards Secure Transaction and Fair Pricing of Training Data

ABSTRACT: As machine learning becomes ubiquitous, deployed systems need to be as accu- rate as they can. As a result, machine learning service providers have a surging need for useful, additional training data that benefits training, without giving up all the details about the trained program. At the same time, data owners would like to trade their data for its value, without having to first give away the data itself be- fore receiving compensation. It is difficult for data providers and model providers to agree on a fair price without first revealing the data or the trained model to the other side. Escrow systems only complicate this further, adding an additional layer of trust required of both parties. Currently, data owners and model owners don’t have a fair pricing system that eliminates the need to trust a third party and training the model on the data, which 1) takes a long time to complete, 2) does not guarantee that useful data is paid valuably and that useless data isn’t, without trusting in the third party with both the model and the data. Existing improve- ments to secure the transaction focus heavily on encrypting or approximating the data, such as training on encrypted data, and variants of federated learning. As powerful as the methods appear to be, we show them to be impractical in our use case with real world assumptions for preserving privacy for the data owners when facing black-box models. Thus, a fair pricing scheme that does not rely on secure data encryption and obfuscation is needed before the exchange of data. This pa- per proposes a novel method for fair pricing using data-model efficacy techniques such as influence functions, model extraction, and model compression methods, thus enabling secure data transactions. We successfully show that without running the data through the model, one can approximate the value of the data; that is, if the data turns out redundant, the pricing is minimal, and if the data leads to proper improvement, its value is properly assessed, without placing strong assumptions on the nature of the model. Future work will be focused on establishing a system with stronger transactional security against adversarial attacks that will reveal details about the model or the data to the other party.

## item_id: m_3553

TITLE: A Convolutional Encoder Model for Neural Machine Translation

ABSTRACT: The prevalent approach to neural machine translation relies on bi-directional LSTMs to encode the source sentence.
In this paper we present a faster and simpler architecture based on a succession of convolutional layers. 
This allows to encode the entire source sentence simultaneously compared to recurrent networks for which computation is constrained by temporal dependencies.
On WMT'16 English-Romanian translation we achieve competitive accuracy to the state-of-the-art and we outperform several recently published results on the WMT'15 English-German task. 
Our models obtain almost the same accuracy as a very deep LSTM setup on WMT'14 English-French translation.
Our convolutional encoder speeds up CPU decoding by more than two times at the same or higher accuracy as a strong bi-directional LSTM baseline. 

## item_id: m_3554

TITLE: CATS: Cost-Augmented Tree Search for LLM-Assisted Planning

ABSTRACT: While large language models excel at open-ended reasoning, they often struggle with cost-sensitive planning, either treating all actions as having equal cost or failing to stay within strict budgets. In this paper, we introduce Cost-Augmented Tree Search (CATS), a novel search approach that brings explicit cost-awareness into LLM-guided planning. Tight cost constraints push the planner to quickly identify infeasible solutions, while looser constraints encourage optimization for minimal cost. We benchmark top LLMs such as GPT-4.1 and Claude-Opus-4.1 against our CATS planner to evaluate their performance on a cost-augmented variant of BlocksWorld, where each action is assigned a specific budget and tasks must be completed under an overall budget constraint. Our experiments show that raw LLMs, such as Claude-Opus-4.1, often falter under tight budgets, whereas CATS consistently delivers strong performance with higher task success rates and better budget utilization. CATS provides an effective solution for budget-aware planning by combining the reasoning power of LLMs with structured search.

## item_id: m_3555

TITLE: DeFINE: Deep Factorized Input Token Embeddings for Neural Sequence Modeling

ABSTRACT: For sequence models with large vocabularies, a majority of network parameters lie in the input and output layers. In this work, we describe a new method, DeFINE, for learning deep token representations efficiently. Our architecture uses a hierarchical structure with novel skip-connections which allows for the use of low dimensional input and output layers, reducing total parameters and training time while delivering similar or better performance versus existing methods. DeFINE can be incorporated easily in new or existing sequence models. Compared to state-of-the-art methods including adaptive input representations, this technique results in a 6% to 20% drop in perplexity. On WikiText-103, DeFINE reduces the total parameters of Transformer-XL by half with minimal impact on performance. On the Penn Treebank, DeFINE improves AWD-LSTM by 4 points with a 17% reduction in parameters, achieving comparable performance to state-of-the-art methods with fewer parameters. For machine translation, DeFINE improves the efficiency of the Transformer model by about 1.4 times while delivering similar performance.

## item_id: m_3556

TITLE: Memory-Modular Classification: Learning to Generalize with Memory Replacement

ABSTRACT: We introduce a memory-modular learner for image classification that externalizes
knowledge memorization from reasoning and thus effectively generalizes to new
classes by replacing memory contents. Instead of statically compiling the world
knowledge and task skills into model weights during training, the proposed model
stores the knowledge in an external memory of image/text data and learns to dy-
namically select relevant contents from the memory according to an input image.
The meta-learned model performs robust classification with a memory of noisy
web-crawled data and adapts to new classes without re-training when the memory
is replaced. Experimental results show the promising performance of our method
on diverse scenarios, including zero-shot/few-shot classification of unseen classes,
fine-grained classification, and class-incremental classification.

## item_id: m_3557

TITLE: Binarized Back-Propagation: Training Binarized Neural Networks with Binarized Gradients

ABSTRACT:  Binarized Neural networks (BNNs) have been shown to be effective in improving network efficiency during the inference phase, after the network has been trained. However, BNNs only binarize the model parameters and activations during propagations. Therefore, BNNs do not offer significant efficiency improvements during training, since the gradients are still propagated and used with high precision. 
 
 We show there is no inherent difficulty in training BNNs using "Binarized BackPropagation" (BBP), in which we also binarize the gradients. To avoid significant degradation in test accuracy, we simply increase the number of filter maps in a each convolution layer. Using BBP on dedicated hardware can potentially significantly improve the execution efficiency (\emph{e.g.}, reduce dynamic memory footprint, memory bandwidth and computational energy) and speed up the training process with an appropriate hardware support, even after such an increase in network size. Moreover, our method is ideal for distributed learning as it reduces the communication costs significantly (e.g., by ~32). Using this method, we demonstrate a minimal loss in classification accuracy on several datasets and topologies.

## item_id: m_3558

TITLE: Compute-efficient Evaluation of LLM Voting Accuracy

ABSTRACT: Test-time scaling methods, such as voting, have emerged as a powerful paradigm to dramatically improve the performance of large language models (LLMs).  Majority voting is often useful however to estimate the tradeoff between task performance (e.g., accuracy) and computational cost, as we vary the size of ensemble used in voting, denoted $M$; or as we vary hyperparameters, such as Temperature, in pursuit of a more favorable tradeoff. In the literature, evaluating voting accuracy performance is done using a purely empirical approach that requires many LLM evaluations and is highly computationally intensive. In this work we propose two methods to estimate the voting accuracy of an LLM with substantially less computational cost than current methods. Using a popular public benchmark datasets of LLM problems (MATH) we demonstrate that our two estimation approaches can closely approximate the true ensemble accuracy, with substantially less computational cost than current methods less computation than a purely empirical approach, especially as the number of votes grows larger.

## item_id: m_3559

TITLE: DEGREE: Decomposition Based Explanation for Graph Neural Networks

ABSTRACT: Graph Neural Networks (GNNs) are gaining extensive attention for their application in graph data. However, the black-box nature of GNNs prevents users from understanding and trusting the models, thus hampering their applicability. Whereas explaining GNNs remains a challenge, most existing methods fall into approximation based and perturbation based approaches with suffer from faithfulness problems and unnatural artifacts respectively. To tackle these problems, we propose DEGREE (Decomposition based Explanation for GRaph nEural nEtworks) to provide a faithful explanation for GNN predictions. By decomposing the information generation and aggregation mechanism of GNNs, DEGREE allows tracking the contributions of specific components of the input graph to the final prediction. Based on this, we further design a subgraph level interpretation algorithm to reveal complex interactions between graph nodes that are overlooked by previous methods. The efficiency of our algorithm can be further improved by utilizing GNN characteristics. Finally, we conduct quantitative and qualitative experiments on synthetic and real-world datasets to demonstrate the effectiveness of DEGREE on node classification and graph classification tasks.

## item_id: m_3560

TITLE: LayoutTransformer: Relation-Aware Scene Layout Generation

ABSTRACT: In the areas of machine learning and computer vision, text-to-image synthesis aims at producing image outputs given the input text. In particular, the task of layout generation requires one to describe the spatial information for each object component, with the ability to model their relationships. In this paper, we present a LayoutTransformer Network (LT-Net), which is a generative model for text-conditioned layout generation. By extracting semantics-aware yet object discriminative contextual features from the input, we utilize Gaussian mixture models to describe the layouts for each object with relation consistency enforced. Finally, a co-attention mechanism across textual and visual features is deployed to produce the final output. In our experiments, we conduct extensive experiments on both MS-COCO and Visual Genome (VG) datasets, and confirm the effectiveness and superiority of our LT-Net over recent text-to-image and layout generation models.

## item_id: m_3561

TITLE: MocoSFL: enabling cross-client collaborative self-supervised learning

ABSTRACT: Existing collaborative self-supervised learning (SSL) schemes are not suitable for cross-client applications because of their expensive computation and large local data requirements. To address these issues, we propose MocoSFL, a collaborative SSL framework based on Split Federated Learning (SFL) and Momentum Contrast (MoCo). In MocoSFL, the large backbone model is split into a small client-side model and a large server-side model, and only the small client-side model is processed locally on the client's local devices. MocoSFL has three key components: (i) vector concatenation which enables the use of small batch size and reduces computation and memory requirements by orders of magnitude; (ii) feature sharing that helps achieve high accuracy regardless of the quality and volume of local data; (iii) frequent synchronization that helps achieve better non-IID performance because of smaller local model divergence. For a 1,000-client case with non-IID data (each client only has data from 2 random classes of CIFAR-10), MocoSFL can achieve over 84% accuracy with ResNet-18 model. Next we present TAResSFL module that significantly improves the resistance to privacy threats and communication overhead with small sacrifice in accuracy for a MocoSFL system. On a Raspberry Pi 4B device, the MocoSFL-based scheme requires less than 1MB of memory and less than 40MB of communication, and consumes less than 5W power. The code is available at https://github.com/SonyAI/MocoSFL.

## item_id: m_3562

TITLE: Flow++: Improving Flow-Based Generative Models  with  Variational Dequantization and Architecture Design  

ABSTRACT: Flow-based generative models are powerful exact likelihood models with efficient sampling and inference. 
Despite their computational efficiency, flow-based models generally have much worse density modeling performance compared to state-of-the-art autoregressive models. In this paper, we investigate and improve upon three limiting design choices employed by flow-based models in prior work: the use of uniform noise for dequantization, the use of inexpressive affine flows, and the use of purely convolutional conditioning networks in coupling layers. Based on our findings, we propose Flow++, a new flow-based model that is now the state-of-the-art non-autoregressive model for unconditional density estimation on standard image benchmarks. Our work has begun to close the significant performance gap that has so far existed between autoregressive models and flow-based models.

## item_id: m_3563

TITLE: NeurQuRI: Neural Question Requirement Inspector for Answerability Prediction in Machine Reading Comprehension

ABSTRACT: Real-world question answering systems often retrieve potentially relevant documents to a given question through a keyword search, followed by a machine reading comprehension (MRC) step to find the exact answer from them. In this process, it is essential to properly determine whether an answer to the question exists in a given document. This task often becomes complicated when the question involves multiple different conditions or requirements which are to be met in the answer. For example, in a question "What was the projection of sea level increases in the fourth assessment report?", the answer should properly satisfy several conditions, such as "increases" (but not decreases) and "fourth" (but not third). To address this, we propose a neural question requirement inspection model called NeurQuRI that extracts a list of conditions from the question, each of which should be satisfied by the candidate answer generated by an MRC model. To check whether each condition is met, we propose a novel, attention-based loss function. We evaluate our approach on SQuAD 2.0 dataset by integrating the proposed module with various MRC models, demonstrating the consistent performance improvements across a wide range of state-of-the-art methods.

## item_id: m_3564

TITLE: Bayesian Policy Optimization for Model Uncertainty

ABSTRACT: Addressing uncertainty is critical for autonomous systems to robustly adapt to the real world. We formulate the problem of model uncertainty as a continuous Bayes-Adaptive Markov Decision Process (BAMDP), where an agent maintains a posterior distribution over latent model parameters given a history of observations and maximizes its expected long-term reward with respect to this belief distribution. Our algorithm, Bayesian Policy Optimization, builds on recent policy optimization algorithms to learn a universal policy that navigates the exploration-exploitation trade-off to maximize the Bayesian value function. To address challenges from discretizing the continuous latent parameter space, we propose a new policy network architecture that encodes the belief distribution independently from the observable state. Our method significantly outperforms algorithms that address model uncertainty without explicitly reasoning about belief distributions and is competitive with state-of-the-art Partially Observable Markov Decision Process solvers.

## item_id: m_3565

TITLE: An Unsupervised Deep Learning Approach for Real-World Image Denoising

ABSTRACT: Designing an unsupervised image denoising approach in practical applications is a challenging task due to the complicated data acquisition process. In the real-world case, the noise distribution is so complex that the simplified additive white Gaussian (AWGN) assumption rarely holds, which significantly deteriorates the Gaussian denoisers' performance. To address this problem, we apply a deep neural network that maps the noisy image into a latent space in which the AWGN assumption holds, and thus any existing Gaussian denoiser is applicable. More specifically, the proposed neural network consists of the encoder-decoder structure and approximates the likelihood term in the Bayesian framework. Together with a Gaussian denoiser, the neural network can be trained with the input image itself and does not require any pre-training in other datasets. Extensive experiments on real-world noisy image datasets have shown that the combination of neural networks and Gaussian denoisers improves the performance of the original Gaussian denoisers by a large margin. In particular, the neural network+BM3D method significantly outperforms other unsupervised denoising approaches and is competitive with supervised networks such as DnCNN, FFDNet, and CBDNet.

## item_id: m_3566

TITLE: At Which Training Stage Does Code Data Help LLMs Reasoning?

ABSTRACT: Large Language models (LLMs) have exhibited remarkable reasoning capabilities and become the foundation of language technologies. Inspired by the great success of code data in training LLMs, we naturally wonder at which training stage introducing code data can really help LLMs reasoning. To this end, this paper systematically explores the impact of code data on LLMs at different stages. Concretely, we introduce the code data at the pre-training stage, instruction-tuning stage, and both of them, respectively. Then, the reasoning capability of LLMs is comprehensively and fairly evaluated via six reasoning tasks. We critically analyze the experimental results and provide conclusions with insights. First, pre-training LLMs with the mixture of code and text can significantly enhance LLMs' general reasoning capability almost without negative transfer on other tasks. Besides, at the instruction-tuning stage, code data endows LLMs the task-specific reasoning capability. Moreover, the dynamic mixing strategy of code and text data assists LLMs to learn reasoning capability step-by-step during training. These insights deepen the understanding of LLMs regarding reasoning ability for their application, such as scientific question answering, legal support, etc.

## item_id: m_3567

TITLE: Physics-Informed Neural Operator for  Learning Partial Differential Equations

ABSTRACT: Machine learning methods have recently shown promise in solving partial differential equations (PDEs). They can be classified into two broad categories: solution function approximation, and operator learning. The Physics-Informed Neural Network (PINN) is an example of the former while the Fourier neural operator (FNO) is an example of the latter. Both these approaches have shortcomings. The optimization in PINN is challenging and prone to failure, especially on multi-scale dynamic systems. FNO does not suffer from this optimization issue since it carries out supervised learning on a given dataset, but obtaining such data may be too expensive or infeasible. In this work, we propose the physics-informed neural operator (PINO), where we combine the operating-learning and function-optimization frameworks, and this improves convergence rates and accuracy over both PINN and FNO models. In the operator-learning phase, PINO learns the solution operator over multiple instances of the parametric PDE family. In the test-time optimization phase, PINO optimizes the pre-trained operator ansatz for the querying instance of the PDE. Experiments show PINO outperforms previous ML methods on many popular PDE families while retaining the extraordinary speed-up of FNO compared to solvers. In particular, PINO accurately solves long temporal transient flows and chaotic Kolmogorov flows, while PINN and other methods fail to converge to a reasonable accuracy.  

## item_id: m_3568

TITLE: UNCERTAINTY QUANTIFICATION USING VARIATIONAL INFERENCE FOR BIOMEDICAL IMAGE SEGMENTATION

ABSTRACT: Deep learning motivated by convolutional neural networks has been highly successful in a range of medical imaging problems like image classification, image
segmentation, image synthesis etc. However for validation and interpretability, not
only do we need the predictions made by the model but also how confident it is
while making those predictions. This is important in safety critical applications
for the people to accept it. In this work, we used an encoder decoder architecture
based on variational inference techniques for segmenting brain tumour images. We
evaluate our work on the publicly available BRATS dataset using Dice Similarity
Coefficient (DSC) and Intersection Over Union (IOU) as the evaluation metrics.
Our model is able to segment brain tumours while taking into account both aleatoric
uncertainty and epistemic uncertainty in a principled bayesian manner.

## item_id: m_3569

TITLE: Fast Differentiable Matrix Square Root

ABSTRACT: Computing the matrix square root or its inverse in a differentiable manner is important in a variety of computer vision tasks. Previous methods either adopt the Singular Value Decomposition (SVD) to explicitly factorize the matrix or use the Newton-Schulz iteration (NS iteration) to derive the approximate solution. However, both methods are not computationally efficient enough in either the forward pass or in the backward pass. In this paper, we propose two more efficient variants to compute the differentiable matrix square root. For the forward propagation, one method is to use Matrix Taylor Polynomial (MTP), and the other method is to use Matrix Pad\'e Approximants (MPA). The backward gradient is computed by iteratively solving the continuous-time Lyapunov equation using the matrix sign function. Both methods yield considerable speed-up compared with the SVD or the Newton-Schulz iteration. Experimental results on the de-correlated batch normalization and second-order vision transformer demonstrate that our methods can also achieve competitive and even slightly better performances. The code is available at \href{https://github.com/KingJamesSong/FastDifferentiableMatSqrt}{https://github.com/KingJamesSong/FastDifferentiableMatSqrt}.

## item_id: m_3570

TITLE: Improve Object Detection with Feature-based Knowledge Distillation: Towards Accurate and Efficient Detectors

ABSTRACT: Knowledge distillation, in which a student model is trained to mimic a teacher model, has been proved as an effective technique for model compression and model accuracy boosting. However, most knowledge distillation methods, designed for image classification, have failed on more challenging tasks, such as object detection. In this paper, we suggest that the failure of knowledge distillation on object detection is mainly caused by two reasons: (1) the imbalance between pixels of foreground and background and (2) lack of distillation on the relation between different pixels. Observing the above reasons, we propose attention-guided distillation and non-local distillation to address the two problems, respectively.  Attention-guided distillation is proposed to find the crucial pixels of foreground objects with attention mechanism and then make the students take more effort to learn their features. Non-local distillation is proposed to enable students to learn not only the feature of an individual pixel but also the relation between different pixels captured by non-local modules. Experiments show that our methods achieve excellent AP improvements on both one-stage and two-stage, both anchor-based and anchor-free detectors. For example, Faster RCNN (ResNet101 backbone) with our distillation achieves 43.9 AP on COCO2017, which is 4.1 higher than the baseline. Codes have been released on Github.

## item_id: m_3571

TITLE: Motion Forecasting with Unlikelihood Training

ABSTRACT: Motion forecasting is essential for making safe and intelligent decisions in robotic applications such as autonomous driving. State-of-the-art methods formulate it as a sequence-to-sequence prediction problem, which is solved in an encoder-decoder framework with a maximum likelihood estimation objective. In this paper, we show that the likelihood objective itself results in a model assigning too much probability to trajectories that are unlikely given the contextual information such as maps and states of surrounding agents. This is despite the fact that many state-of-the-art models do take contextual information as part of their input. We propose a new objective, unlikelihood training, which forces generated trajectories that conflicts with contextual information to be assigned a lower probability by our model. We demonstrate that our method can significantly improve state-of-art models’ performance on challenging real-world trajectory forecasting datasets (nuScenes and Argoverse) by 8% and reduce the standard deviation by up to 50%. The code will be made available.

## item_id: m_3572

TITLE: Action as a Modality: Turning Multi-Modal LLMs to General Action Planners

ABSTRACT: Large Language Models (LLMs) have demonstrated strong reasoning capabilities and possess extensive common knowledge. This enables them to adapt to a variety of complex tasks in a zero-shot manner, including functioning as controllers to manipulate automated systems and produce executable action sequences. However, a significant challenge in the existing framework is the misalignment between the general pre-trained LLM and the action space of specific control tasks. This misalignment necessitates extensive efforts in designing task-specific prompts, which are less generalizable and do not ensure consistent output when prompting a pre-trained LLM to generate the desired action sequences. To address this issue, we propose a novel solution, ActionVerse, which encodes action candidates into a series of modality tokens, coupled with an efficient alignment technique to synchronize the action tokens with the LLM's language space. By leveraging this approach, the proposed ActionVerse successfully transforms a chat-based multi-modal LLM into a general action executor capable of handling tasks requiring step-by-step execution of various actions. Experiments on several sequential action tasks demonstrate the effectiveness of the proposed framework.

## item_id: m_3573

TITLE: RewardMap: Tackling Sparse Rewards in Fine-grained Visual Reasoning via Multi-Stage Reinforcement Learning

ABSTRACT: Fine-grained visual reasoning remains a core challenge for multimodal large language models (MLLMs). The recently introduced ReasonMap highlights this gap by showing that even advanced MLLMs struggle with spatial reasoning in structured and information-rich settings such as transit maps, a task of clear practical and scientific importance. However, standard reinforcement learning (RL) on such tasks is impeded by sparse rewards and unstable optimization. To address this, we first construct ReasonMap-Plus, an extended dataset that introduces dense reward signals through Visual Question Answering (VQA) tasks, enabling effective cold-start training of fine-grained visual understanding skills. Next, we propose RewardMap, a multi-stage RL framework designed to improve both visual understanding and reasoning capabilities of MLLMs. RewardMap incorporates two key designs. First, we introduce a difficulty-aware reward design that incorporates detail rewards, directly tackling the sparse rewards while providing richer supervision. Second, we propose a multi-stage RL scheme that bootstraps training from simple perception to complex reasoning tasks, offering a more effective cold-start strategy than conventional Supervised Fine-Tuning (SFT). Experiments on ReasonMap and ReasonMap-Plus demonstrate that each component of RewardMap contributes to consistent performance gains, while their combination yields the best results. Moreover, models trained with RewardMap achieve an average improvement of 3.47% across 6 benchmarks spanning spatial reasoning, fine-grained visual reasoning, and general tasks beyond transit maps, underscoring enhanced visual understanding and reasoning capabilities.

## item_id: m_3574

TITLE: Disentangled Generative Causal Representation Learning

ABSTRACT: This paper proposes a Disentangled gEnerative cAusal Representation (DEAR) learning method. Unlike existing disentanglement methods that enforce independence of the latent variables, we consider the general case where the underlying factors of interests can be causally correlated. We show that previous methods with independent priors fail to disentangle causally related factors. Motivated by this finding, we propose a new disentangled learning method called DEAR that enables causal controllable generation and causal representation learning. The key ingredient of this new formulation is to use a structural causal model (SCM) as the prior for a bidirectional generative model. A generator is then trained jointly with an encoder using a suitable GAN loss. Theoretical justification on the proposed formulation is provided, which guarantees disentangled causal representation learning under appropriate conditions. We conduct extensive experiments on both synthesized and real datasets to demonstrate the effectiveness of DEAR in causal controllable generation, and the benefits of the learned representations for downstream tasks in terms of sample efficiency and distributional robustness.

## item_id: m_3575

TITLE: DRESS: Disentangled Representation-based Self-Supervised Meta-Learning for Diverse Tasks

ABSTRACT: Meta-learning represents a strong class of approaches for solving few-shot learning tasks. Nonetheless, recent research suggests that simply pre-training a generic encoder can potentially surpass meta-learning algorithms. In this paper, we hypothesize that the reason meta-learning fails to stand out in popular few-shot learning benchmarks is the lack of diversity among the few-shot learning tasks. We propose DRESS, a task-agnostic Disentangled REpresentation-based Self-Supervised meta-learning approach that enables fast model adaptation on highly diversified few-shot learning tasks. Specifically, DRESS utilizes disentangled representation learning to create self-supervised tasks that can fuel the meta-training process. We validate the effectiveness of DRESS through experiments on datasets with multiple factors of variation and varying complexity. The results suggest that DRESS is able to outperform competing methods on the majority of the datasets and task setups. Through this paper, we advocate for a re-examination of how task adaptation studies are conducted, and aim to reignite interest in the potential of meta-learning for solving few-shot learning tasks via disentangled representations.

## item_id: m_3576

TITLE: Diverse and Consistent Multi-view Networks for Semi-supervised Regression

ABSTRACT: Label collection is costly in many applications, which poses the need for label-efficient learning. In this work, we present Diverse and Consistent Multi-view Networks (DiCoM) — a novel semi-supervised regression technique based on a multi-view learning framework. DiCoM combines diversity with consistency — two seemingly opposing yet complementary principles of multi-view learning - based on underlying probabilistic graphical assumptions. Given multiple deep views of the same input, DiCoM encourages a negative correlation among the views' predictions on labeled data, while simultaneously enforces their agreement on unlabeled data. DiCoM can utilize either multi-network or multi-branch architectures to make a trade-off between computational cost and modeling performance. Under realistic evaluation setups, DiCoM outperforms competing methods on tabular and image data. Our ablation studies confirm the importance of having both consistency and diversity.

## item_id: m_3577

TITLE: Semi-supervised Learning with Multi-Domain Sentiment Word Embeddings

ABSTRACT: Word embeddings are known to boost performance of many NLP tasks such as text classification, meanwhile they can be enhanced by labels at the document level to capture nuanced meaning such as sentiment and topic. Can one combine these two research directions to benefit from both? In this paper, we propose to jointly train a text classifier with a label-enhanced and domain-aware word embedding model, using an unlabeled corpus and only a few labeled data from non-target domains. The embeddings are trained on the unlabed corpus and enhanced by pseudo labels coming from the classifier, and at the same time are used by the classifier as input and training signals. We formalize this symbiotic cycle in a variational Bayes framework, and show that our method improves both the embeddings and the text classifier, outperforming state-of-the-art domain adaptation and semi-supervised learning techniques. We conduct detailed ablative tests to reveal gains from important components of our approach. The source code and experiment data will be publicly released.

## item_id: m_3578

TITLE: Optimizing Dynamic Treatment Strategies with Reinforcement Learning and Dual-Hawkes Process in Clinical Environments

ABSTRACT: Modeling the timing of critical events and controlling associated risks through treatment options are crucial aspects of healthcare. However, current methods fall short in optimizing dynamic treatment plans to improve clinical outcomes. A key challenge lies in modeling the intensity functions of critical events throughout disease progression and capturing the dynamic interactions between patient conditions and treatments. To address this, we propose integrating reinforcement learning with a Generative Adversarial Network (GAN) and a dual-Hawkes process model to develop intelligent agents capable of delivering personalized and adaptive treatment strategies. The dual-Hawkes process allows us to model the intensity of both disease progression and recovery, while accounting for long-term dependencies. The GAN simulates real-world clinical environments using raw time-to-event data, without requiring detailed treatment annotations. By interacting with GAN, our model-based reinforcement learning agent learns an optimal dynamic policy that leverages long-term historical dependencies. When applied to the MIMIC-III dataset, our approach significantly increased the duration that patients remained in a healthy state, outperforming established machine learning policies.

## item_id: m_3579

TITLE: Playing SNES in the Retro Learning Environment

ABSTRACT: Mastering a video game requires skill, tactics and strategy. While these attributes may be acquired naturally by human players, teaching them to a computer program is a far more challenging task. In recent years, extensive research was carriedout in the field of reinforcement learning and numerous algorithms were introduced, aiming to learn how to perform human tasks such as playing video games. As a result, the Arcade Learning Environment (ALE) (Bellemare et al., 2013) has become a commonly used benchmark environment allowing algorithms to train on various Atari 2600 games. In many games the state-of-the-art algorithms outperform humans. In this paper we introduce a new learning environment, the Retro Learning Environment — RLE, that can run games on the Super Nintendo Entertainment System (SNES), Sega Genesis and several other gaming consoles. The environment is expandable, allowing for more video games and consoles to be easily added to the environment, while maintaining the same interface as ALE. Moreover, RLE is compatible with Python and Torch. SNES games pose a significant challenge to current algorithms due to their higher level of complexity and versatility.

## item_id: m_3580

TITLE: Contact-guided Real2Sim from Monocular Video with Planar Scene Primitives

ABSTRACT: We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human--scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion-tracking policies with scene interactions to fail. In contrast, our key insight is to fit simulation-ready convex planar primitives to a depth-based point cloud reconstruction of the scene via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we use human--scene contact modeling (e.g., using human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion-tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering 43\% faster RL simulation throughput. This demonstrates CRISP's ability to generate physically valid human motion and interaction environments at scale, advancing real-to-sim applications for robotics. Code and interactive demos are available at our project website: https://crisp-real2sim.github.io/CRISP-Real2Sim

## item_id: m_3581

TITLE: LancBiO: Dynamic Lanczos-aided Bilevel Optimization via Krylov Subspace

ABSTRACT: Bilevel optimization, with broad applications in machine learning, has an intricate hierarchical structure. Gradient-based methods have emerged as a common approach to large-scale bilevel problems. However, the computation of the hyper-gradient, which involves a Hessian inverse vector product, confines the efficiency and is regarded as a bottleneck. To circumvent the inverse, we construct a sequence of low-dimensional approximate Krylov subspaces with the aid of the Lanczos process. As a result, the constructed subspace is able to dynamically and incrementally approximate the Hessian inverse vector product with less effort and thus leads to a favorable estimate of the hyper-gradient. Moreover, we propose a provable subspace-based framework for bilevel problems where one central step is to solve a small-size tridiagonal linear system. To the best of our knowledge, this is the first time that subspace techniques are incorporated into bilevel optimization. This successful trial not only enjoys $\mathcal{O}(\epsilon^{-1})$ convergence rate but also demonstrates efficiency in a synthetic problem and two deep learning tasks.

## item_id: m_3582

TITLE: Capacity and Trainability in Recurrent Neural Networks

ABSTRACT: Two potential bottlenecks on the expressiveness of recurrent neural networks (RNNs) are their ability to store information about the task in their parameters, and to store information about the input history in their units. We show experimentally that all common RNN architectures achieve nearly the same per-task and per-unit capacity bounds with careful training, for a variety of tasks and stacking depths. They can store an amount of task information which is linear in the number of parameters, and is approximately 5 bits per parameter. They can additionally store approximately one real number from their input history per hidden unit. We further find that for several tasks it is the per-task parameter capacity bound that determines performance. These results suggest that many previous results comparing RNN architectures are driven primarily by differences in training effectiveness, rather than differences in capacity. Supporting this observation, we compare training difficulty for several architectures, and show that vanilla RNNs are far more difficult to train, yet have slightly higher capacity. Finally, we propose two novel RNN architectures, one of which is easier to train than the LSTM or GRU for deeply stacked architectures.

## item_id: m_3583

TITLE: Minimizing FLOPs to Learn Efficient Sparse Representations

ABSTRACT: Deep representation learning has become one of the most widely adopted approaches for visual search, recommendation, and identification. Retrieval of such  representations from a large database is however computationally challenging. Approximate methods based on learning compact representations, have been widely explored for this problem, such as locality sensitive hashing, product quantization, and PCA. In this work, in contrast to learning compact representations, we propose to learn high dimensional and sparse representations that have similar representational capacity as dense embeddings while being more efficient due to sparse matrix multiplication operations which can be much faster than dense multiplication. Following the key insight that the number of operations decreases quadratically with the sparsity of embeddings provided the non-zero entries are distributed uniformly across dimensions, we propose a novel approach to learn such distributed sparse embeddings via the use of a carefully constructed regularization function that directly minimizes a continuous relaxation of the number of floating-point operations (FLOPs) incurred during retrieval. Our experiments show that our approach is competitive to the other baselines and yields a similar or better speed-vs-accuracy tradeoff on practical datasets.

## item_id: m_3584

TITLE: Thermodynamics-inspired Structure Hallucination for Protein-protein Interaction Modeling

ABSTRACT: Modeling protein-protein interactions (PPI) represents a central challenge within the field of biology, and accurately predicting the consequences of mutations in this context is crucial for various applications, such as drug design and protein engineering. Recent advances in deep learning (DL) have shown promise in forecasting the effects of such mutations. However, the effectiveness of these models is hindered by two primary constraints. First and foremost, obtaining the structures of mutant proteins is a persistent challenge, as they are often elusive to acquire. Secondly, interactions take place dynamically, but thermodynamics is rarely integrated into the DL architecture design. To address these obstacles, we present a novel framework known as Refine-PPI, which incorporates two key enhancements. On the one hand, we introduce a structure refinement module that is trained by a mask mutation modeling (MMM) task on available wide-type structures and then is transferred to hallucinate the inaccessible mutant protein structures. Additionally, we employ a new kind of geometric networks to capture the dynamic 3D variations and encode the uncertainty associated with PPI. Through comprehensive experiments conducted on the established benchmark dataset SKEMPI, our results substantiate the superiority of the Refine-PPI framework. These findings underscore the effectiveness of our hallucination strategy to address the absence of mutant protein structure and hope to shed light on the prediction of the free energy change.

## item_id: m_3585

TITLE: Self-ensembling for visual domain adaptation

ABSTRACT: This paper explores the use of self-ensembling for visual domain adaptation problems. Our technique is derived from the mean teacher variant (Tarvainen et. al 2017) of temporal ensembling (Laine et al. 2017), a technique that achieved state of the art results in the area of semi-supervised learning. We introduce a number of modifications to their approach for challenging domain adaptation scenarios and evaluate its effectiveness. Our approach achieves state of the art results in a variety of benchmarks, including our winning entry in the VISDA-2017 visual domain adaptation challenge. In small image benchmarks, our algorithm not only outperforms prior art, but can also achieve accuracy that is close to that of a classifier trained in a supervised fashion.

## item_id: m_3586

TITLE: A Simple yet Effective Method to Prune Dense Layers of Neural Networks

ABSTRACT: Neural networks are usually over-parameterized with significant redundancy in the number of required neurons which results in unnecessary computation and memory usage at inference time. One common approach to address this issue is to prune these big networks by removing extra neurons and parameters while maintaining the accuracy. In this paper, we propose NoiseOut, a fully automated pruning algorithm based on the correlation between activations of neurons in the hidden layers. We prove that adding additional output neurons with entirely random targets results into a higher correlation between neurons which makes pruning by NoiseOut even more efficient. Finally, we test our method on various networks
and datasets. These experiments exhibit high pruning rates while maintaining the accuracy of the original network.

## item_id: m_3587

TITLE: Human perception in computer vision

ABSTRACT: Computer vision has made remarkable progress in recent years. Deep neural network (DNN) models optimized to identify objects in images exhibit unprecedented task-trained accuracy and, remarkably, some generalization ability: new visual problems can now be solved more easily based on previous learning. Biological vision (learned in life and through evolution) is also accurate and general-purpose. Is it possible that these different learning regimes converge to similar problem-dependent optimal computations? We therefore asked whether the human system-level computation of visual perception has DNN correlates and considered several anecdotal test cases. We found that perceptual sensitivity to image changes has DNN mid-computation correlates, while sensitivity to segmentation, crowding and shape has DNN end-computation correlates. Our results quantify the applicability of using DNN computation to estimate perceptual loss, and are consistent with the fascinating theoretical view that properties of human perception are a consequence of architecture-independent visual learning.

## item_id: m_3588

TITLE: Explaining Neural Networks Semantically and Quantitatively

ABSTRACT: This paper presents a method to explain the knowledge encoded in a convolutional neural network (CNN) quantitatively and semantically. How to analyze the specific rationale of each prediction made by the CNN presents one of key issues of understanding neural networks, but it is also of significant practical values in certain applications. In this study, we propose to distill knowledge from the CNN into an explainable additive model, so that we can use the explainable model to provide a quantitative explanation for the CNN prediction. We analyze the typical bias-interpreting problem of the explainable model and develop prior losses to guide the learning of the explainable additive model. Experimental results have demonstrated the effectiveness of our method.

## item_id: m_3589

TITLE: Unsupervised Cross-Domain Image Generation

ABSTRACT: We study the problem of transferring a sample in one domain to an analog sample in another domain. Given two related domains, S and T, we would like to learn a generative function G that maps an input sample from S to the domain T, such that the output of a given representation function f, which accepts inputs in either domains, would remain unchanged. Other than f, the training data is unsupervised and consist of a set of samples from each domain, without any mapping between them. The Domain Transfer Network (DTN) we present employs a compound loss function that includes a multiclass GAN loss, an f preserving component, and a regularizing component that encourages G to map samples from T to themselves. We apply our method to visual domains including digits and face images and demonstrate its ability to generate convincing novel images of previously unseen entities, while preserving their identity.

## item_id: m_3590

TITLE: Discovering Evolution Strategies via Meta-Black-Box Optimization

ABSTRACT: Optimizing functions without access to gradients is the remit of black-box meth- ods such as evolution strategies. While highly general, their learning dynamics are often times heuristic and inflexible — exactly the limitations that meta-learning can address. Hence, we propose to discover effective update rules for evolution strategies via meta-learning. Concretely, our approach employs a search strategy parametrized by a self-attention-based architecture, which guarantees the update rule is invariant to the ordering of the candidate solutions. We show that meta-evolving this system on a small set of representative low-dimensional analytic optimization problems is sufficient to discover new evolution strategies capable of generalizing to unseen optimization problems, population sizes and optimization horizons. Furthermore, the same learned evolution strategy can outperform established neuroevolution baselines on supervised and continuous control tasks. As additional contributions, we ablate the individual neural network components of our method; reverse engineer the learned strategy into an explicit heuristic form, which remains highly competitive; and show that it is possible to self-referentially train an evolution strategy from scratch, with the learned update rule used to drive the outer meta-learning loop.

## item_id: m_3591

TITLE: Evaluating the Goal-Directedness of Large Language Models

ABSTRACT: LLM-based agents may transform AI and society in the near future. Along with opportunities for automation and increased productivity come novel safety and ethics concerns. This means both researchers and regulators need good ways to keep track of progress and properties of LLM-based agents. A key feature of agentic behaviour is goal-directedness, which has so far received limited attention in the context of AI agents. In this work we define the concept of goal-directedness for LLM agents, and develop a framework for evaluating it empirically on tasks involving information gathering, information processing, and execution. Results on state-of-the-art LLM agents indicate a lack of goal-directedness, meaning models often fail to fully deploy capabilities that they evidently have. This raises the question of how we can elicit the full capabilities of LLM-based agents, as well as what policies should be in place for future more goal-directed systems.

## item_id: m_3592

TITLE: Learning One-hidden-layer Neural Networks on Gaussian Mixture Models with Guaranteed Generalizability

ABSTRACT: We analyze the learning problem of fully connected neural networks with the sigmoid activation function for binary classification in the teacher-student setup, where the outputs are assumed to be generated by a ground-truth teacher neural network with unknown parameters, and the learning objective is to estimate the teacher network model by minimizing a non-convex cross-entropy risk function of the training data over a student neural network. This paper analyzes a  general and practical scenario that the input features follow a Gaussian mixture model of a finite number of Gaussian distributions of various mean and variance. We propose a gradient descent algorithm with a tensor initialization approach and show that our algorithm converges linearly to a critical point that has a  diminishing distance to the ground-truth model with guaranteed generalizability. We characterize the required number of samples for successful convergence, referred to as the sample complexity,  as a function of the parameters of the Gaussian mixture model. We prove analytically that when any mean or variance in the mixture model is large, or when all variances are close to zero, the sample complexity increases, and the convergence slows down, indicating a more challenging learning problem. Although focusing on one-hidden-layer neural networks, to the best of our knowledge, this paper provides the first explicit characterization of the impact of the parameters of the input distributions on the sample complexity and learning rate.

## item_id: m_3593

TITLE: Is There Mode Collapse? A Case Study on Face Generation and Its Black-box Calibration

ABSTRACT: Generative adversarial networks (GANs) nowadays are capable of producing im-ages of incredible realism.   One concern raised is whether the state-of-the-artGAN’s learned distribution still suffers from mode collapse. Existing evaluation metrics for image synthesis focus on low-level perceptual quality. Diversity tests of samples from GANs are usually conducted qualitatively on a small scale. In this work, we devise a set of statistical tools, that are broadly applicable to quantitatively measuring the mode collapse of GANs. Strikingly, we consistently observe strong mode collapse on several state-of-the-art GANs using our toolset.  We analyze possible causes, and for the first time present two simple yet effective “black-box” methods to calibrate the GAN learned distribution, without accessing either model parameters or the original training data.

## item_id: m_3594

TITLE: 6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering

ABSTRACT: Novel view synthesis has advanced significantly with the development of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS). However, achieving high quality without compromising real-time rendering remains challenging, particularly for physically-based rendering using ray/path tracing with view-dependent effects. Recently, N-dimensional Gaussians (N-DG) introduced a 6D spatial-angular representation to better incorporate view-dependent effects, but the Gaussian representation and control scheme are sub-optimal. In this paper, we revisit 6D Gaussians and introduce 6D Gaussian Splatting (6DGS), which enhances color and opacity representations and leverages the additional directional information in the 6D space for optimized Gaussian control. Our approach is fully compatible with the 3DGS framework and significantly improves real-time radiance field rendering by better modeling view-dependent effects and fine details. Experiments demonstrate that 6DGS significantly outperforms 3DGS and N-DG, achieving up to a 15.73 dB improvement in PSNR with a reduction of 66.5\% Gaussian points compared to 3DGS. The project page is: https://gaozhongpai.github.io/6dgs/.

## item_id: m_3595

TITLE: Hyperbolic Self-paced Learning for Self-supervised Skeleton-based Action Representations

ABSTRACT: Self-paced learning has been beneficial for tasks where some initial knowledge is available, such as weakly supervised learning and domain adaptation, to select and order the training sample sequence, from easy to complex. However its applicability remains unexplored in unsupervised learning, whereby the knowledge of the task matures during training.
We propose a novel HYperbolic Self-Paced model (HYSP) for learning skeletonbased action representations. HYSP adopts self-supervision: it uses data augmentations to generate two views of the same sample, and it learns by matching one (named online) to the other (the target). We propose to use hyperbolic uncertainty to determine the algorithmic learning pace, under the assumption that less uncertain samples should be more strongly driving the training, with a larger weight and pace. Hyperbolic uncertainty is a by-product of the adopted hyperbolic neural networks, it matures during training and it comes with no extra cost, compared to the established Euclidean SSL framework counterparts.
When tested on three established skeleton-based action recognition datasets, HYSP outperforms the state-of-the-art on PKU-MMD I, as well as on 2 out of 3 downstream tasks on NTU-60 and NTU-120. Additionally, HYSP only uses positive pairs and bypasses therefore the complex and computationally-demanding mining procedures required for the negatives in contrastive techniques.
Code is available at https://github.com/paolomandica/HYSP.

## item_id: m_3596

TITLE: Flatness is a False Friend

ABSTRACT: Hessian based measures of flatness, such as the trace, Frobenius and spectral norms, have been argued, used and shown to relate to generalisation. In this paper we demonstrate that, for feed-forward neural networks under the cross-entropy loss, low-loss solutions with large neural network weights have small Hessian based measures of flatness. This implies that solutions obtained without L2 regularisation should be less sharp than those with despite generalising worse. We show this to be true for logistic regression, multi-layer perceptrons, simple convolutional, pre-activated and wide residual networks on the MNIST and CIFAR-$100$ datasets. Furthermore, we show that adaptive optimisation algorithms using iterate averaging, on the VGG-$16$ network and CIFAR-$100$ dataset, achieve superior generalisation to SGD but are $30 \times$ sharper. These theoretical and experimental results further advocate the need to use flatness in conjunction with the weights scale to measure generalisation \citep{neyshabur2017exploring,dziugaite2017computing}. 

## item_id: m_3597

TITLE: Domain Generalization via Heckman-type Selection Models 

ABSTRACT: The domain generalization (DG) setup considers the problem where models are trained on data sampled from multiple domains and evaluated on test domains unseen during training. In this paper, we formulate DG as a sample selection problem where each domain is sampled from a common underlying population through non-random sampling probabilities that correlate with both the features and the outcome. Under this setting, the fundamental iid assumption of the empirical risk minimization (ERM) is violated, so it often performs worse on test domains whose non-random sampling probabilities differ from the domains in the training dataset. We propose a Selection-Guided DG (SGDG) framework to learn the selection probability of each domain and the joint distribution of the outcome and domain selection variables. The proposed SGDG is domain generalizable as it intends to minimize the risk under the population distribution. We theoretically proved that, under certain regular conditions, SGDG can achieve smaller risk than ERM. Furthermore, we present a class of parametric SGDG (HeckmanDG) estimators applicable to continuous, binary, and multinomial outcomes. We also demonstrated its efficacy empirically through simulations and experiments on a set of benchmark datasets comparing with other well-known DG methods.

## item_id: m_3598

TITLE: Variational image compression with a scale hyperprior

ABSTRACT: We describe an end-to-end trainable model for image compression based on variational autoencoders. The model incorporates a hyperprior to effectively capture spatial dependencies in the latent representation. This hyperprior relates to side information, a concept universal to virtually all modern image codecs, but largely unexplored in image compression using artificial neural networks (ANNs). Unlike existing autoencoder compression methods, our model trains a complex prior jointly with the underlying autoencoder. We demonstrate that this model leads to state-of-the-art image compression when measuring visual quality using the popular MS-SSIM index, and yields rate--distortion performance surpassing published ANN-based methods when evaluated using a more traditional metric based on squared error (PSNR). Furthermore, we provide a qualitative comparison of models trained for different distortion metrics.

## item_id: m_3599

TITLE: A Gradient Flow Framework For Analyzing Network Pruning

ABSTRACT: Recent network pruning methods focus on pruning models early-on in training. To estimate the impact of removing a parameter, these methods use importance measures that were originally designed to prune trained models. Despite lacking justification for their use early-on in training, such measures result in surprisingly low accuracy loss. To better explain this behavior, we develop a general framework that uses gradient flow to unify state-of-the-art importance measures through the norm of model parameters. We use this framework to determine the relationship between pruning measures and evolution of model parameters, establishing several results related to pruning models early-on in training: (i) magnitude-based pruning removes parameters that contribute least to reduction in loss, resulting in models that converge faster than magnitude-agnostic methods; (ii) loss-preservation based pruning preserves first-order model evolution dynamics and its use is therefore justified for pruning minimally trained models; and (iii) gradient-norm based pruning affects second-order model evolution dynamics, such that increasing gradient norm via pruning can produce poorly performing models. We validate our claims on several VGG-13, MobileNet-V1, and ResNet-56 models trained on CIFAR-10/CIFAR-100.

## item_id: m_3600

TITLE: Future Language Modeling from Temporal Document History

ABSTRACT: Predicting the future is of great interest across many aspects of human activity.  Businesses are interested in future trends, traders are interested in future stock prices, and companies are highly interested in future technological breakthroughs.  While there are many automated systems for predicting future numerical data, such as weather, stock prices, and demand for products, there is relatively little work in automatically predicting textual data.  Humans are interested in textual data predictions because it is a natural format for our consumption, and experts routinely make predictions in a textual format (Christensen et al., 2004; Tetlock & Gardner, 2015; Frick, 2015). However, there has been relatively little formalization of this general problem in the machine learning or natural language processing communities.  To address this gap, we introduce the task of future language modeling: probabilistic modeling of texts in the future based on a temporal history of texts.  To our knowledge, our work is the first work to formalize the task of predicting the future in this way.  We show that it is indeed possible to build future language models that improve upon strong non-temporal language model baselines, opening the door to working on this important, and widely applicable problem.
