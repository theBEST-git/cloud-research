# Batch 04 — 25 items

## item_id: r2_075

TITLE: SafeReview: Building a Robust Deep Review Assistant Against Prompt Injection

ABSTRACT: As Large Language Models (LLMs) are increasingly integrated into academic peer review, their vulnerability to prompt injection—adversarial instructions embedded in submissions to manipulate outcomes—emerges as a critical threat to scholarly integrity. To counter this, we propose a novel adversarial framework where a Generator model, trained to create sophisticated attack prompts, is jointly optimized with a Defender model tasked with their detection. This system is trained using a loss function inspired by Information Retrieval Generative Adversarial Networks (IRGANs), which fosters a dynamic co-evolution between the two models, forcing the Defender to develop robust capabilities against continuously improving attack strategies. The resulting framework demonstrates significantly enhanced resilience to novel and evolving threats compared to static defenses, thereby establishing a critical foundation for securing the integrity of automated academic evaluation.

## item_id: r2_076

TITLE: One Perturbation is Enough: On Generating Universal Adversarial Perturbations against Vision-Language Pre-training Models

ABSTRACT: Vision-Language Pre-training (VLP) models have exhibited unprecedented capability in many applications by taking full advantage of the multimodal alignment. However, previous studies have shown they are vulnerable to maliciously crafted adversarial samples. Despite recent success, these methods are generally instance-specific and require generating perturbations for each input sample. In this paper, we reveal that VLP models are also vulnerable to the instance-agnostic universal adversarial perturbation (UAP). Specifically, we design a novel Contrastive-training Perturbation Generator with Cross-modal conditions (C-PGC) to achieve the attack. In light that the pivotal multimodal alignment is achieved through the advanced contrastive learning technique, we devise to turn this powerful weapon against themselves, i.e., employ a malicious version of contrastive learning to train the C-PGC based on our carefully crafted positive and negative image-text pairs for essentially destroying the alignment relationship learned by VLP models. Besides, C-PGC fully utilizes the characteristics of Vision-and-Language (V+L) scenarios by incorporating both unimodal and cross-modal information as effective guidance. Extensive experiments show that C-PGC successfully forces adversarial samples to move away from their original area in the VLP model's feature space, thus essentially enhancing attacks across various victim models and V+L tasks.

## item_id: r2_077

TITLE: Overparameterisation and worst-case generalisation: friend or foe?

ABSTRACT: Overparameterised neural networks have demonstrated the remarkable ability to perfectly fit training samples, while still generalising to unseen test samples. However, several recent works have revealed that such models' good average performance does not always translate to good worst-case performance: in particular, they may perform poorly on subgroups that are under-represented in the training set. In this paper, we show that in certain settings, overparameterised models' performance on under-represented subgroups may be improved via post-hoc processing. Specifically, such models' bias can be restricted to their classification layers, and manifest as structured prediction shifts for rare subgroups. We detail two post-hoc correction techniques to mitigate this bias, which operate purely on the outputs of standard model training. We empirically verify that with such post-hoc correction, overparameterisation can improve average and worst-case performance.

## item_id: r2_078

TITLE: Improved Generalization Risk Bounds for Meta-Learning with PAC-Bayes-kl Analysis

ABSTRACT:  By incorporating knowledge from observed tasks, PAC-Bayes meta-learning algorithms aim to construct a hyperposterior from which an informative prior is sampled for fast adaptation to novel tasks. The goal of PAC-Bayes meta-learning theory is thus to propose an upper bound on the generalization risk over a novel task of the learned hyperposterior. In this work, we first generalize the tight PAC-Bayes-kl bound from independently and identically distributed (i.i.d.) setting to non-i.i.d. meta-learning setting. Based on the extended PAC-Bayes-kl bound, we further provide three improved PAC-Bayes generalization bounds for meta-learning, leading to better asymptotic behaviour than existing results. By minimizing objective functions derived from the improved bounds, we develop three PAC-Bayes meta-learning algorithms for classification. Moreover, we employ localized PAC-Bayes analysis for meta-learning to yield insights into the role of hyperposterior for learning a novel task. In particular, we identify that when the number of training task is large, utilizing a prior generated from an informative hyperposterior can achieve the same order of PAC-Bayes-kl bound as that obtained through setting a localized distribution-dependent prior for a novel task. Experiments with deep neural networks show that minimizing our bounds can achieve competitive performance on novel tasks w.r.t. previous PAC-Bayes meta-learning methods as well as PAC-Bayes single-task learning methods with localized prior.

## item_id: r2_079

TITLE: DEEPCAST : UNIVERSAL TIME-SERIES FORECASTER

ABSTRACT: Reliable and accurate time-series forecasting is critical in many fields including energy, finance, and manufacturing. Many time-series tasks, however, suffer from a limited amount of training data (i.e., the cold start problem) resulting in poor forecasting performance. Recently, convolutional neural networks (CNNs) have shown outstanding image classification performance even on tasks with small-scale training sets. The performance can be attributed to transfer learning through CNNs’ ability to learn rich mid-level image representations. However, no prior work exists on general transfer learning for time-series forecasting. In this paper, motivated by recent success of transfer learning in CNN model and image-related tasks, we for the first time show how time-series representations learned with Long Short Term Memory (LSTM) on large-scale datasets can be efficiently transferred to other time-series forecasting tasks with limited amount of training data. We also validate that despite differences in time-series statistics and tasks in the datasets, the transferred representation leads to significantly improved forecasting results outperforming majority of the best time-series methods on the public M3 and other datasets. Our online universal forecasting tool, DeepCast, will leverage transfer learning to provide accurate forecasts for a diverse set of time series where classical methods were computationally infeasible or inapplicable due to short training history.

## item_id: r2_080

TITLE: How Reliable Is Human Feedback For Aligning Large Language Models?

ABSTRACT: Most alignment research today focuses on designing new learning algorithms using datasets like Anthropic-HH, assuming human feedback data is inherently reliable. However, little attention has been given to the qualitative unreliability of human feedback and its impact on alignment. To address this gap, we conduct a comprehensive study and provide an in-depth analysis of human feedback data. We assess feedback reliability using a committee of gold reward models, revealing that over 25% of the dataset shows low or no agreement with these models, implying a high degree of unreliability. Through a qualitative analysis, we identify six key sources of unreliability, such as mis-labeling, subjective preferences, differing criteria and thresholds for helpfulness and harmlessness, etc. Lastly, to mitigate unreliability, we propose Source-Aware Cleaning, an automatic data-cleaning method guided by the insight of our qualitative analysis, to significantly improve data quality. Extensive experiments demonstrate that models trained on our cleaned dataset, HH-Clean, substantially outperform those trained on the original dataset. We release HH-Clean to support more reliable LLM alignment research in the future.

## item_id: r2_081

TITLE: Isometric Representations in Neural Networks Improve Robustness

ABSTRACT: Artificial and biological agents are unable to learn given completely random and unstructured data. The structure of data is encoded in the distance or similarity relationships between data points. In the context of neural networks, the neuronal activity within a layer forms a representation reflecting the transformation that the layer implements on its inputs. In order to utilize the structure in the data in a truthful manner, such representations should reflect the input distances and thus be continuous and isometric. Supporting this statement, recent findings in neuroscience propose that generalization and robustness are tied to neural representations being continuously differentiable. However, in machine learning, most algorithms lack robustness and are generally thought to rely on aspects of the data that differ from those that humans use, as is commonly seen in  adversarial attacks.

During cross-entropy classification,  the metric and structural properties of network representations are usually broken both between and within classes. This side effect from training can lead to instabilities under perturbations near locations where such structure is not preserved. One of the standard solutions to obtain robustness is to train specifically by introducing perturbations in the training data. This leads to networks that are particularly robust to specific training perturbations but not necessarily to general perturbations. While adding ad hoc regularization terms to improve robustness has become common practice, to our knowledge, forcing representations to preserve the metric structure of the input data as a stabilising mechanism has not yet been introduced.

In this work, we train neural networks to perform classification while simultaneously  maintaining the metric structure within each class, leading to continuous and isometric within-class representations. We show that such network representations turn out to be a beneficial component for making accurate and robust inferences about the world. By stacking layers with this property we provide the community with an network architecture that facilitates hierarchical manipulation of internal neural representations. Finally, we verify that our isometric regularization term improves the robustness to adversarial attacks on MNIST. 

## item_id: r2_082

TITLE: Identity Matters in Deep Learning

ABSTRACT: An emerging design principle in deep learning is that each layer of a deep
artificial neural network should be able to easily express the identity
transformation. This idea not only motivated various normalization techniques,
such as batch normalization, but was also key to the immense success of
residual networks.

In this work, we put the principle of identity parameterization on a more 
solid theoretical footing alongside further empirical progress. We first
give a strikingly simple proof that arbitrarily deep linear residual networks
have no spurious local optima. The same result for feed-forward networks in
their standard parameterization is substantially more delicate.  Second, we
show that residual networks with ReLu activations have universal finite-sample
expressivity in the sense that the network can represent any function of its
sample provided that the model has more parameters than the sample size.

Directly inspired by our theory, we experiment with a radically simple
residual architecture consisting of only residual convolutional layers and
ReLu activations, but no batch normalization, dropout, or max pool. Our model
improves significantly on previous all-convolutional networks on the CIFAR10,
CIFAR100, and ImageNet classification benchmarks.


## item_id: r2_083

TITLE: Large Language Models Are Not Robust Multiple Choice Selectors

ABSTRACT: Multiple choice questions (MCQs) serve as a common yet important task format in the evaluation of large language models (LLMs). This work shows that modern LLMs are vulnerable to option position changes in MCQs due to their inherent “selection bias”, namely, they prefer to select specific option IDs as answers (like “Option A”). Through extensive empirical analyses with 20 LLMs on three benchmarks, we pinpoint that this behavioral bias primarily stems from LLMs’ token bias, where the model a priori assigns more probabilistic mass to specific option ID tokens (e.g., A/B/C/D) when predicting answers from the option IDs. To mitigate selection bias, we propose a label-free, inference-time debiasing method, called PriDe, which separates the model’s prior bias for option IDs from the overall prediction distribution. PriDe first estimates the prior by permutating option contents on a small number of test samples, and then applies the estimated prior to debias the remaining samples. We demonstrate that it achieves interpretable and transferable debiasing with high computational efficiency. We hope this work can draw broader research attention to the bias and robustness of modern LLMs.

## item_id: r2_084

TITLE: Generalizing Few-Shot NAS with Gradient Matching

ABSTRACT: Efficient performance estimation of architectures drawn from large search spaces is essential to Neural Architecture Search. One-Shot methods tackle this challenge by training one supernet to approximate the performance of every architecture in the search space via weight-sharing, thereby drastically reducing the search cost. However, due to coupled optimization between child architectures caused by weight-sharing, One-Shot supernet's performance estimation could be inaccurate, leading to degraded search outcomes. To address this issue, Few-Shot NAS reduces the level of weight-sharing by splitting the One-Shot supernet into multiple separated sub-supernets via edge-wise (layer-wise) exhaustive partitioning. Since each partition of the supernet is not equally important, it necessitates the design of a more effective splitting criterion. In this work, we propose a gradient matching score (GM) that leverages gradient information at the shared weight for making informed splitting decisions. Intuitively, gradients from different child models can be used to identify whether they agree on how to update the shared modules, and subsequently to decide if they should share weight. Compared with exhaustive partitioning, the proposed criterion significantly reduces the branching factor per edge. This allows us to split more edges (layers) for a given budget, resulting in substantially improved performance as NAS search spaces usually include dozens of edges (layers). Extensive empirical evaluations of the proposed method on a wide range of search spaces (NASBench-201, DARTS, MobileNet Space), datasets (cifar10, cifar100, ImageNet) and search algorithms (DARTS, SNAS, RSPS, ProxylessNAS, OFA) demonstrate that it significantly outperforms its Few-Shot counterparts while surpassing previous comparable methods in terms of the accuracy of derived architectures. 
Our code is available at https://github.com/skhu101/GM-NAS.

## item_id: r2_085

TITLE: Novel positional encodings to enable tree-structured transformers

ABSTRACT: With interest in program synthesis and similarly ﬂavored problems rapidly increasing, neural models optimized for tree-domain problems are of great value. In the sequence domain, transformers can learn relationships across arbitrary pairs of positions with less bias than recurrent models. Under the intuition that a similar property would be beneficial in the tree domain, we propose a method to extend transformers to tree-structured inputs and/or outputs. Our approach abstracts transformer's default sinusoidal positional encodings, allowing us to substitute in a novel custom positional encoding scheme that represents node positions within a tree. We evaluated our model in tree-to-tree program translation and sequence-to-tree semantic parsing settings, achieving superior performance over the vanilla transformer model on several tasks.


## item_id: r2_086

TITLE: Continuity-Regularized Flow Matching for Offline Reinforcement Learning

ABSTRACT: Flow-matching policies have recently emerged as a powerful class of generative models for offline reinforcement learning (RL), capable of capturing complex, multi-modal action distributions from static datasets. However, standard training objectives are largely agnostic to the global properties of the generative path, permitting learned vector fields that are irregular and unstable, which can hinder performance. In this work, we introduce PDE-regularized Q-Learning (PQL), a novel algorithm that addresses this limitation by imposing a principled structure on the entire probability flow. PQL makes two synergistic contributions: first, a partial differential equation based regularizer derived from the continuity equation enforces global smoothness and stability on the flow. Second, to solve the complex optimization problem introduced by this regularizer, we propose a Beta-distributed timestep sampling strategy that focuses learning on the critical trajectory segments where the trade-off between imitation and smoothness is most acute. Through extensive experiments, we demonstrate that by structuring the generative journey and not just its destination, PQL achieves state-of-the-art performance on a wide range of challenging offline RL tasks.

## item_id: r2_087

TITLE: Adversarial Weight Perturbation Improves Generalization in Graph Neural Networks

ABSTRACT: There is growing theoretical and empirical evidence that flatter local minima tend to improve generalization. An efficient and effective technique for finding such minima is Adversarial Weight Perturbation (AWP). The main idea is to minimize the loss w.r.t. a bounded worst-case perturbation of the model parameters by (approximately) solving an associated min-max problem. Intuitively, we favor local minima with a small loss in a neighborhood around them. The benefits of AWP, and more generally the connections between flatness and generalization, have been extensively studied for i.i.d. data such as images. In this paper we initiate the first study of this phenomenon for graph data. Along the way, we identify a vanishing-gradient issue with all existing formulations of AWP and we propose Weighted Truncated AWP (WT-AWP) to alleviate this issue. We show that regularizing graph neural networks with WT-AWP consistently improves both natural and robust generalization across many different graph learning tasks and models.

## item_id: r2_088

TITLE: SpaCE: The Spatial Confounding Environment

ABSTRACT: Spatial confounding poses a significant challenge in scientific studies involving spatial data, where unobserved spatial variables can influence both treatment and outcome, possibly leading to spurious associations. To address this problem, we introduce SpaCE: The Spatial Confounding Environment, the first toolkit to provide realistic benchmark datasets and tools for systematically evaluating causal inference methods designed to alleviate spatial confounding. Each dataset includes training data, true counterfactuals, a spatial graph with coordinates, and smoothness and confounding scores characterizing the effect of a missing spatial confounder. It also includes realistic semi-synthetic outcomes and counterfactuals, generated using state-of-the-art machine learning ensembles, following best practices for causal inference benchmarks. The datasets cover real treatment and covariates from diverse domains, including climate, health and social sciences. SpaCE facilitates an automated end-to-end pipeline, simplifying data loading, experimental setup, and evaluating machine learning and causal inference models. The SpaCE project provides several dozens of datasets of diverse sizes and spatial complexity. It is publicly available as a Python package, encouraging community feedback and contributions.

## item_id: r2_089

TITLE: HyperReal:  Complex-Valued Layer Functions For Complex-Valued Scaling Invariance

ABSTRACT: Complex-valued measurements in MRI and SAR imaging often have complex-valued scaling ambiguity, calling for models that are invariant to complex-valued scaling of pixels. Deep Complex Networks (DCN) extends real-valued algebra to complex-valued algebra in neural networks, but it does not address the issue of complex-valued scaling. SurReal complex-valued networks adopt a manifold view of complex numbers and derive a distance metric that is invariant to complex scaling. With distance features, it achieves complex-scaling invariance. However, rich complex-valued information is lost in this representation, and additionally,  SurReal is also prevented from using complex-valued non-linearity, limiting its expressive power. We simplify the manifold formulation of SurReal and propose a new layer function that achieves complex-scaling invariance within the complex domain.  We can then build hierarchical complex-valued features with complex-scaling invariance.  Our so-called HyperReal model results in a much leaner model with better generalization. Benchmarked on MSTAR, HyperReal beats DCN (and matches SurReal) with only 3%(40%) of their respective parameter counts.

## item_id: r2_090

TITLE: LCS: Learning Compressible Subspaces for Adaptive Network Compression at Inference Time

ABSTRACT: When deploying deep learning models to a device, it is traditionally assumed that available computational resources (compute, memory, and power) remain static. However, real-world computing systems do not always provide stable resource guarantees. Computational resources need to be conserved when load from other processes is high or battery power is low. Inspired by recent works on neural network subspaces, we propose a method for training a "compressible subspace" of neural networks that contains a fine-grained spectrum of models that range from highly efficient to highly accurate. Our models require no retraining, thus our subspace of models can be deployed entirely on-device to allow adaptive network compression at inference time. We present results for achieving arbitrarily fine-grained accuracy-efficiency trade-offs at inference time for structured and unstructured sparsity. We achieve accuracies on-par with standard models when testing our uncompressed models, and maintain high accuracy for sparsity rates above 90% when testing our compressed models. We also demonstrate that our algorithm extends to quantization at variable bit widths, achieving accuracy on par with individually trained networks.

## item_id: r2_091

TITLE: Lost Domain Generalization Is a Natural Consequence of Lack of Training Domains

ABSTRACT: We show a hardness result for the number of training domains required to achieve a small population error in the test domain. Although many domain generalization algorithms have been developed under various domain-invariance assumptions, there is significant evidence to indicate that out-of-distribution (o.o.d.) test accuracy of state-of-the-art o.o.d. algorithms is on par with empirical risk minimization and random guess on the domain generalization benchmarks such as DomainBed. In this work, we analyze its cause and attribute the lost domain generalization to the lack of training domains. We show that, in a minimax lower bound fashion, \emph{any} learning algorithm that outputs a classifier with an $\epsilon$ excess error to the Bayes optimal classifier requires at least $\mathrm{poly}(1/\epsilon)$ number of training domains, even though the number of training data sampled from each training domain is large. Experiments on the DomainBed benchmark demonstrate that o.o.d. test accuracy is monotonically increasing as the number of training domains increases. Our result sheds light on the intrinsic hardness of domain generalization and suggests benchmarking o.o.d. algorithms by the datasets with a sufficient number of training domains.

## item_id: r2_092

TITLE: Forget Unlearning: Towards True Data-Deletion in Machine Learning

ABSTRACT: Unlearning has emerged as a technique to efficiently erase information of deleted records from learned models. We show, however, that the influence created by the original presence of a data point in the training set can still be detected after running certified unlearning algorithms (which can result in its reconstruction by an adversary). Thus, under realistic assumptions about the dynamics of model releases over time and in the presence of adaptive adversaries, we show that unlearning is not equivalent to data deletion and does not guarantee the "right to be forgotten." We then propose a more robust data-deletion guarantee and show that it is necessary to satisfy differential privacy to ensure true data deletion. Under our notion, we propose an accurate, computationally efficient, and secure data-deletion machine learning algorithm in the online setting based on noisy gradient descent algorithm.

## item_id: r2_093

TITLE: Predicate Hierarchies Improve Few-Shot State Classification

ABSTRACT: State classification of objects and their relations is core to many long-horizon tasks, particularly in robot planning and manipulation. However, the combinatorial explosion of possible object-predicate combinations, coupled with the need to adapt to novel real-world environments, makes it a desideratum for state classification models to generalize to novel queries with few examples. To this end, we propose PHIER, which leverages predicate hierarchies to generalize effectively in few-shot scenarios. PHIER uses an object-centric scene encoder, self-supervised losses that infer semantic relations between predicates, and a hyperbolic distance metric that captures hierarchical structure; it learns a structured latent space of image-predicate pairs that guides reasoning over state classification queries. We evaluate PHIER in the CALVIN and BEHAVIOR robotic environments and show that PHIER significantly outperforms existing methods in few-shot, out-of-distribution state classification, and demonstrates strong zero- and few-shot generalization from simulated to real-world tasks. Our results demonstrate that leveraging predicate hierarchies improves performance on state classification tasks with limited data.

## item_id: r2_094

TITLE: Disentangling Improves VAEs' Robustness to Adversarial Attacks

ABSTRACT: This paper is concerned with the robustness of VAEs to adversarial attacks. We highlight that conventional VAEs are brittle under attack but that methods recently introduced for disentanglement such as β-TCVAE (Chen et al., 2018) improve robustness, as demonstrated through a variety of previously proposed adversarial attacks (Tabacof et al. (2016); Gondim-Ribeiro et al. (2018); Kos et al.(2018)). This motivated us to develop Seatbelt-VAE, a new hierarchical disentangled VAE that is designed to be significantly more robust to adversarial attacks than existing approaches, while retaining high quality reconstructions.

## item_id: r2_095

TITLE: AUL is a better optimization metric  in PU learning

ABSTRACT: Traditional binary classification models are trained and evaluated with fully labeled data which is not common in real life. In non-ideal dataset, only a small fraction of positive data are labeled. Training a model from such partially labeled data is named as positive-unlabeled (PU) learning. A naive solution of PU learning is treating unlabeled samples as negative. However, using biased data, the trained model may converge to non-optimal point and its real performance cannot be well estimated. Recent works try to recover the unbiased result by estimating the proportion of positive samples with mixture proportion estimation (MPE) algorithms, but the model performance is still limited and heavy computational cost is introduced (particularly for big datasets). In this work, we theoretically prove that Area Under Lift curve (AUL) is an unbiased metric in PU learning scenario, and the experimental evaluation on 9 datasets shows that the average absolute error of AUL estimation is only 1/6 of AUC estimation. By experiments we also find that, compared with state-of-the-art AUC-optimization algorithm, AULoptimization algorithm can not only significantly save the computational cost, but also improve the model performance by up to 10%.

## item_id: r2_096

TITLE: PINNsFormer: A Transformer-Based Framework For Physics-Informed Neural Networks

ABSTRACT: Physics-Informed Neural Networks (PINNs) have emerged as a promising deep learning framework for approximating numerical solutions to partial differential equations (PDEs). However, conventional PINNs, relying on multilayer perceptrons (MLP), neglect the crucial temporal dependencies inherent in practical physics systems and thus fail to propagate the initial condition constraints globally and accurately capture the true solutions under various scenarios. In this paper, we introduce a novel Transformer-based framework, termed PINNsFormer, designed to address this limitation. PINNsFormer can accurately approximate PDE solutions by utilizing multi-head attention mechanisms to capture temporal dependencies. PINNsFormer transforms point-wise inputs into pseudo sequences and replaces point-wise PINNs loss with a sequential loss. Additionally, it incorporates a novel activation function, \texttt{Wavelet}, which anticipates Fourier decomposition through deep neural networks. Empirical results demonstrate that PINNsFormer achieves superior generalization ability and accuracy across various scenarios, including PINNs failure modes and high-dimensional PDEs. Moreover, PINNsFormer offers flexibility in integrating existing learning schemes for PINNs, further enhancing its performance.

## item_id: r2_097

TITLE: Average-case Acceleration for Bilinear Games and Normal Matrices

ABSTRACT: Advances in generative modeling and adversarial learning have given rise to renewed interest in smooth games. However, the absence of symmetry in the matrix of second derivatives poses challenges that are not present in the classical minimization framework. While a rich theory of average-case analysis has been developed for minimization problems, little is known in the context of smooth games. In this work we take a first step towards closing this gap by developing average-case optimal first-order methods for a subset of smooth games. 
We make the following three main contributions. First, we show that for zero-sum bilinear games the average-case optimal method is the optimal method for the minimization of the Hamiltonian. Second, we provide an explicit expression for the optimal method corresponding to normal matrices, potentially non-symmetric. Finally, we specialize it to matrices with eigenvalues located in a disk and show a provable speed-up compared to worst-case optimal algorithms. We illustrate our findings through benchmarks with a varying degree of mismatch with our assumptions.

## item_id: r2_098

TITLE: Block-operations: Creating an Inductive Bias to Route Data and Reuse Subnetworks

ABSTRACT: Feed Forward Neural Networks (FNNs) often suffer from poor generalization due to their inability to effectively develop and reuse subnetworks for related tasks. Csordás et al. (2020) suggest that this may be because FNNs are more likely to learn new mappings than to copy and route activation patterns without altering them. To tackle this problem, we propose the concept of block-operations: Learnable functions that group neurons into larger semantic units and operate on these blocks, with routing as a primitive operation. As a first step, we introduce the Multiplexer, a new architectural component that enhances the FNN by adding block-operations to it. We experimentally verified that the Multiplexer exhibits several desirable properties, as compared to the FNN which it replaces: It represents concepts consistently with the same neuron activation patterns throughout the network, suffers less from negative interference, shows an increased propensity for specialization and transfer learning, can more easily reuse learned subnetworks for new tasks, and is particularly effective at learning algorithmic tasks with conditional logics. In several cases, the Multiplexer achieved 100% OOD-generalization on our tasks, where FNNs only learned correlations that failed to generalize. Our results suggest that block-operations are a promising direction for future research. Adapting more complex architectures than the FNN to make use of them could lead to increased compositionality and better generalization.

## item_id: r2_099

TITLE: GenExam: A Multidisciplinary Text-to-Image Exam

ABSTRACT: Exams are a fundamental test of expert-level intelligence and require integrated understanding, reasoning, and generation. Existing exam-style benchmarks mainly focus on understanding and reasoning tasks, and current generation benchmarks emphasize the illustration of world knowledge and visual concepts, neglecting the evaluation of rigorous drawing exams. We introduce GenExam, the first benchmark for multidisciplinary text-to-image exams, featuring 1,000 samples across 10 subjects with exam-style prompts organized under a four-level taxonomy. Each problem is equipped with ground-truth images and fine-grained scoring points to enable a precise evaluation of semantic correctness and visual plausibility. Experiments show that even state-of-the-art models such as GPT-Image-1 and Gemini-2.5-Flash-Image achieve less than 15% strict scores, and most models yield almost 0%, suggesting the great challenge of GenExam. By framing image generation as an exam, GenExam offers a rigorous assessment of models' ability to integrate understanding, reasoning, and generation, providing insights on the path to general AGI. Our benchmark and evaluation code will be released.
