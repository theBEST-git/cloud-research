# Batch 29 — 100 items

## item_id: m_2801

TITLE: Analyzing Populations of Neural Networks via Dynamical Model Embedding

ABSTRACT: A core challenge in the interpretation of deep neural networks is identifying commonalities between the underlying algorithms implemented by distinct networks trained for the same task.  Motivated by this problem, we introduce \textsc{Dynamo}, an algorithm that constructs low-dimensional manifolds where each point corresponds to a neural network model, and two points are nearby if the corresponding neural networks enact similar high-level computational processes. \textsc{Dynamo} takes as input a collection of pre-trained neural networks and outputs a \emph{meta-model} that emulates the dynamics of the hidden states as well as the outputs of any model in the collection.  The specific model to be emulated is determined by a \emph{model embedding vector} that the meta-model takes as input; these model embedding vectors constitute a manifold corresponding to the given population of models. We apply \textsc{Dynamo} to both RNNs and CNNs, and find that the resulting model embedding manifolds enable novel applications: clustering of neural networks on the basis of their high-level computational processes in a manner that is less sensitive to reparameterization; model averaging of several neural networks trained on the same task to arrive at a new, operable neural network with similar task performance; and semi-supervised learning via optimization on the model embedding manifold.  Using a fixed-point analysis of meta-models trained on populations of RNNs, we gain new insights into how similarities of the topology of RNN dynamics correspond to similarities of their high-level computational processes.

## item_id: m_2802

TITLE: Noise or Signal: The Role of Image Backgrounds in Object Recognition

ABSTRACT: We assess the tendency of state-of-the-art object recognition models to depend on signals from image backgrounds. We create a toolkit for disentangling foreground and background signal on ImageNet images, and find that (a) models can achieve non-trivial accuracy by relying on the background alone, (b) models often misclassify images even in the presence of correctly classified foregrounds--up to 88% of the time with adversarially chosen backgrounds, and (c) more accurate models tend to depend on backgrounds less. Our analysis of backgrounds brings us closer to understanding which correlations machine learning models use, and how they determine models' out of distribution performance.


## item_id: m_2803

TITLE: Towards Efficient Confidence Estimation for Large Language Model Reasoning

ABSTRACT: Recent advances have demonstrated the powerful reasoning capabilities of large language models (LLMs), and accurately measuring the confidence of reasoning paths is crucial for improving the performance and trustworthy of AI systems. Benefiting from consistency function for reasoning, the self-consistency method often provides an effective confidence estimation. However, it suffers from the variance issue, which extremely constrains the performance when the sampling is insufficient. Existing methods such as the temperature sampling cannot well resolve this problem as it not only necessitates a calibration set but also tends to sacrifice the reasoning capability of LLMs. In this paper, we propose a data-free, and highly sampling efficient method to control the variance. The merit of our approach lies in a reasonable integration of the LLM's probability estimation and the self-consistency confidence. Our theoretical analysis confirms the efficacy of our method by achieving a lower estimation error and a higher error reduction rate. Furthermore, an in-depth analysis of the error decomposition reveals an improved technique, which can significantly improve error reduction rate with only a small scale of bias induced. Experimental results across seven benchmark datasets demonstrate that our proposed approaches achieve superior confidence estimation, boosting the accuracy on both mathematical reasoning tasks and code generation tasks. Our code is provided in the supplementary material.

## item_id: m_2804

TITLE: Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning

ABSTRACT: For learning with noisy labels, the transition matrix, which explicitly models the relation between noisy label distribution and clean label distribution, has been utilized to achieve the statistical consistency of either the classifier or the risk. Previous researches have focused more on how to estimate this transition matrix well, rather than how to utilize it. We propose good utilization of the transition matrix is crucial and suggest a new utilization method based on resampling, coined RENT. Specifically, we first demonstrate current utilizations can have potential limitations for implementation. As an extension to Reweighting, we suggest the Dirichlet distribution-based per-sample Weight Sampling (DWS) framework, and compare reweighting and resampling under DWS framework. With the analyses from DWS, we propose RENT, a REsampling method with Noise Transition matrix. Empirically, RENT consistently outperforms existing transition matrix utilization methods, which includes reweighting, on various benchmark datasets. Our code is available at https://github.com/BaeHeeSun/RENT.

## item_id: m_2805

TITLE: Towards Modular Algorithm Induction

ABSTRACT: We present a modular neural network architecture MAIN that learns algorithms given a set of input-output examples. MAIN consists of a neural controller that interacts with a variable-length input tape and learns to compose modules together with their corresponding argument choices. Unlike previous approaches, MAIN uses a general domain-agnostic mechanism for selection of modules and their arguments. It uses a general input tape layout together with a parallel history tape to indicate most recently used locations. Finally, it uses a memoryless controller with a length-invariant self-attention based input tape encoding to allow for random access to tape locations. The MAIN architecture is trained end-to-end using reinforcement learning from a set of input-output examples. We evaluate MAIN on five algorithmic tasks and show that it can learn policies that generalizes perfectly to inputs of much longer lengths than the ones used for training.

## item_id: m_2806

TITLE: Towards Impartial Multi-task Learning

ABSTRACT: Multi-task learning (MTL) has been widely used in representation learning. However, naively training all tasks simultaneously may lead to the partial training issue, where specific tasks are trained more adequately than others. In this paper, we propose to learn multiple tasks impartially. Specifically, for the task-shared parameters, we optimize the scaling factors via a closed-form solution, such that the aggregated gradient (sum of raw gradients weighted by the scaling factors) has equal projections onto individual tasks. For the task-specific parameters, we dynamically weigh the task losses so that all of them are kept at a comparable scale. Further, we find the above gradient balance and loss balance are complementary and thus propose a hybrid balance method to further improve the performance. Our impartial multi-task learning (IMTL) can be end-to-end trained without any heuristic hyper-parameter tuning, and is general to be applied on all kinds of losses without any distribution assumption. Moreover, our IMTL can converge to similar results even when the task losses are designed to have different scales, and thus it is scale-invariant. We extensively evaluate our IMTL on the standard MTL benchmarks including Cityscapes, NYUv2 and CelebA. It outperforms existing loss weighting methods under the same experimental settings.

## item_id: m_2807

TITLE: Filling in the details: Perceiving from low fidelity visual input

ABSTRACT: Humans perceive their surroundings in great detail even though most of our visual field is reduced to low-fidelity color-deprived (e.g., dichromatic) input by the retina. In contrast, most deep learning architectures deploy computational resources homogeneously to every part of the visual input. Is such a prodigal deployment of resources necessary? In this paper, we present a framework for investigating the extent to which connectionist architectures can perceive an image in full detail even when presented with low acuity, distorted input. Our goal is to initiate investigations that will be fruitful both for engineering better networks and also for eventually testing hypotheses on the neural mechanisms responsible for our own visual system's ability to perceive missing information. We find that networks can compensate for low acuity input by learning global feature functions that allow the network to fill in some of the missing details. For example, the networks accurately perceive shape and color in the periphery, even when 75\% of the input is achromatic and low resolution. On the other hand, the network is prone to similar mistakes as humans; for example, when presented with a fully grayscale landscape image, it perceives the sky as blue when the sky is actually a red sunset. 

## item_id: m_2808

TITLE: Poisoning with A Pill: Circumventing Detection in Federated Learning

ABSTRACT: Federated learning (FL) protects data privacy by enabling distributed model training without direct access to client data. However, its distributed nature makes it vulnerable to model and data poisoning attacks. While numerous defenses filter malicious clients using statistical metrics, they overlook the role of model redundancy, where not all parameters contribute equally to the model/attack performance. Current attacks manipulate all model parameters uniformly, making them more detectable, while defenses focus on the overall statistics of client updates, leaving gaps for more sophisticated attacks. We propose an attack-agnostic augmentation method to enhance the stealthiness and effectiveness of existing poisoning attacks in FL, exposing flaws in current defenses and highlighting the need for fine-grained FL security. Our three-stage methodology—$\textit{pill construction}$, $\textit{pill poisoning}$, and $\textit{pill injection}$—injects poison into a compact subnet (i.e., pill) of the global model during the iterative FL training. Experimental results show that FL poisoning attacks enhanced by our method can bypass 8 state-of-the-art (SOTA) defenses, gaining an up to 7x error rate increase, as well as on average a more than 2x error rate increase on both IID and non-IID data, in both cross-silo and cross-device FL systems.

## item_id: m_2809

TITLE: Contextual Explanation Networks

ABSTRACT: We introduce contextual explanation networks (CENs)---a class of models that learn to predict by generating and leveraging intermediate explanations. CENs are deep networks that generate parameters for context-specific probabilistic graphical models which are further used for prediction and play the role of explanations. Contrary to the existing post-hoc model-explanation tools, CENs learn to predict and to explain jointly. Our approach offers two major advantages: (i) for each prediction, valid instance-specific explanations are generated with no computational overhead and (ii) prediction via explanation acts as a regularization and boosts performance in low-resource settings. We prove that local approximations to the decision boundary of our networks are consistent with the generated explanations. Our results on image and text classification and survival analysis tasks demonstrate that CENs are competitive with the state-of-the-art while offering additional insights behind each prediction, valuable for decision support.

## item_id: m_2810

TITLE: COALA: Convex Optimization for Alignment and Preference Learning on a Single GPU

ABSTRACT: Fine-tuning large language models (LLMs) to align with human preferences has driven the success of systems like ChatGPT and Gemini. 
However, methods like Reinforcement Learning from Human Feedback (RLHF) remain computationally expensive and complex. 
Direct Preference Optimization (DPO) offers a simpler alternative but has limitations such as inconsistent ranking accuracy, reliance on a frozen reference model, and high dependence on expensive GPU resources. 
We introduce COALA, a novel lightweight algorithm that leverages the convex optimization reformulation of neural networks (cvxNN).
By exploiting the expressiveness of cvxNN, COALA eliminates the need for a reference model and obtains significant reduction in both training time and VRAM consumption, thus enabling efficient training on a single GPU. 
Experiments across three datasets—including a 23,228-sample synthetic educational feedback dataset—and five models (including LLaMA-8B) demonstrate that COALA outperforms traditional preference alignment methods such as DPO and ORPO.
COALA exhibits stable, monotonically increasing rewards and reaches peak margins in significantly shorter time in comparison to competitors. 
To the best of our knowledge, this is the first time convex optimization has been successfully applied to preference fine-tuning of LLMs.

## item_id: m_2811

TITLE: Learning powerful policies and better dynamics models by encouraging consistency

ABSTRACT: Model-based reinforcement learning approaches have the promise of being sample efficient. Much of the progress in learning dynamics models in RL has been made by learning models via supervised learning. There is enough evidence that humans build a model of the environment, not only by observing the environment but also by interacting with the environment. Interaction with the environment allows humans to carry out  "experiments": taking actions that help uncover true causal relationships which can be used for building better dynamics models. Analogously, we would expect such interaction to be helpful for a learning agent while learning to model the environment dynamics. In this paper, we build upon this intuition, by using an auxiliary cost function to ensure consistency between what the agent observes (by acting in the real world) and what it imagines (by acting in the ``learned'' world). Our empirical analysis shows that the proposed approach helps to train powerful policies as well as better dynamics models.

## item_id: m_2812

TITLE: Quantifying the Cost of Reliable Photo Authentication via High-Performance Learned Lossy Representations

ABSTRACT: Detection of photo manipulation relies on subtle statistical traces, notoriously removed by aggressive lossy compression employed online. We demonstrate that end-to-end modeling of complex photo dissemination channels allows for codec optimization with explicit provenance objectives. We design a lightweight trainable lossy image codec, that delivers competitive rate-distortion performance, on par with best hand-engineered alternatives, but has lower computational footprint on modern GPU-enabled platforms. Our results show that significant improvements in manipulation detection accuracy are possible at fractional costs in bandwidth/storage. Our codec improved the accuracy from 37% to 86% even at very low bit-rates, well below the practicality of JPEG (QF 20). 

## item_id: m_2813

TITLE: Adaptive Dropout with Rademacher Complexity Regularization

ABSTRACT: We propose a novel framework to adaptively adjust the dropout rates for the deep neural network based on a Rademacher complexity bound. The state-of-the-art deep learning algorithms impose dropout strategy to prevent feature co-adaptation. However, choosing the dropout rates remains an art of heuristics or relies on empirical grid-search over some hyperparameter space. In this work, we show the network Rademacher complexity is bounded by a function related to the dropout rate vectors and the weight coefficient matrices. Subsequently, we impose this bound as a regularizer and provide a theoretical justified way to trade-off between model complexity and representation power. Therefore, the dropout rates and the empirical loss are unified into the same objective function, which is then optimized using the block coordinate descent algorithm. We discover that the adaptively adjusted dropout rates converge to some interesting distributions that reveal meaningful patterns.Experiments on the task of image and document classification also show our method achieves better performance compared to the state-of the-art dropout algorithms.

## item_id: m_2814

TITLE: Successor Options : An Option Discovery Algorithm for Reinforcement Learning

ABSTRACT: Hierarchical Reinforcement Learning is a popular method to exploit temporal abstractions in order to tackle the curse of dimensionality. The options framework is one such hierarchical framework that models the notion of skills or options. However, learning a collection of task-agnostic transferable skills is a challenging task. Option discovery typically entails using heuristics, the majority of which revolve around discovering bottleneck states. In this work, we adopt a method complementary to the idea of discovering bottlenecks. Instead, we attempt to discover ``landmark" sub-goals which are prototypical states of well connected regions. These sub-goals are points from which densely connected set of states are easily accessible. We propose a new model called Successor options that leverages Successor Representations to achieve the same. We also design a novel pseudo-reward for learning the intra-option policies. Additionally, we describe an Incremental Successor options model that iteratively builds options and explores in environments where exploration through primitive actions is inadequate to form the Successor Representations. Finally, we demonstrate the efficacy of our approach on a collection of grid worlds and on complex high dimensional environments like Deepmind-Lab.


## item_id: m_2815

TITLE: Assessing Robustness via Score-based Adversarial Image Generation

ABSTRACT: Most adversarial attacks and defenses focus on perturbations within small $\ell_p$-norm constraints. However, $\ell_p$ threat models cannot capture all relevant semantic-preserving perturbations, and hence, the scope of robustness evaluations is limited.
In this work, we introduce Score-Based Adversarial Generation (ScoreAG), a novel framework that leverages the advancements in score-based generative models to generate adversarial examples beyond $\ell_p$-norm constraints, so-called unrestricted adversarial examples, overcoming their limitations. 
Unlike traditional methods, ScoreAG maintains the core semantics of images while generating realistic adversarial examples, either by transforming existing images or synthesizing new ones entirely from scratch. We further exploit the generative capability of ScoreAG to purify images, empirically enhancing the robustness of classifiers. Our extensive empirical evaluation demonstrates that ScoreAG matches the performance of state-of-the-art attacks and defenses across multiple benchmarks.
This work highlights the importance of investigating adversarial examples bounded by semantics rather than $\ell_p$-norm constraints. ScoreAG represents an important step towards more encompassing robustness assessments.

## item_id: m_2816

TITLE: Principled Hybrids of Generative and Discriminative Domain Adaptation

ABSTRACT: We propose a probabilistic framework for domain adaptation that blends both generative and discriminative modeling in a principled way. Under this framework, generative and discriminative models correspond to specific choices of the prior over parameters. This provides us a very general way to interpolate between generative and discriminative extremes through different choices of priors. By maximizing both the marginal and the conditional log-likelihoods, models derived from this framework can use both labeled instances from the source domain as well as unlabeled instances from \emph{both} source and target domains. Under this framework, we show that the popular reconstruction loss of autoencoder corresponds to an upper bound of the negative marginal log-likelihoods of unlabeled instances, where marginal distributions are given by proper kernel density estimations. This provides a way to interpret the empirical success of autoencoders in domain adaptation and semi-supervised learning. We instantiate our framework using neural networks, and build a concrete model,  \emph{DAuto}. Empirically, we demonstrate the effectiveness of DAuto on text, image and speech datasets, showing that it outperforms related competitors when domain adaptation is possible.


## item_id: m_2817

TITLE: Towards the Explainability of Temporal Graph Networks via Memory Backtracking

ABSTRACT: Temporal graphs are ubiquitous in real-world applications such as social networks and finance, where Temporal Graph Networks (TGNs) achieve superior predictive accuracy. Understanding which historical events drive specific
model predictions enhances trustworthiness of TGNs.  Existing explanation methods for TGNs overlook the memory module, the core component that records and updates node histories, leaving unexplored how past events shape memory dynamics and influence the current predictions. To address this challenge, we propose a framework that attributes TGNs predictions through the topology attribution tree and memory backtracking tree. The topology attribution tree captures neighbor influence, including the impact of their memory vectors. Then, we use the memory backtracking tree to quantify how historical events shape memory evolution. Our method satisfies a conservation principle, ensuring that the total contribution of events equals the model’s logits. Finally, we introduce optimization objectives to map logits to probabilities. Experiments on seven temporal graph datasets, spanning node property prediction and link prediction tasks, show that our method provides faithful explanations and consistently outperforms four state-of-the-art baselines.

## item_id: m_2818

TITLE: NRGBoost: Energy-Based Generative Boosted Trees

ABSTRACT: Despite the rise to dominance of deep learning in unstructured data domains, tree-based methods such as Random Forests (RF) and Gradient Boosted Decision Trees (GBDT) are still the workhorses for handling discriminative tasks on tabular data. We explore generative extensions of these popular algorithms with a focus on explicitly modeling the data density (up to a normalization constant), thus enabling other applications besides sampling. 
As our main contribution we propose an energy-based generative boosting algorithm that is analogous to the second-order boosting implemented in popular libraries like XGBoost. We show that, despite producing a generative model capable of handling inference tasks over any input variable, our proposed algorithm can achieve similar discriminative performance to GBDT on a number of real world tabular datasets, outperforming alternative generative approaches. At the same time, we show that it is also competitive with neural-network-based models for sampling.
Code is available at https://github.com/ajoo/nrgboost.

## item_id: m_2819

TITLE: Autoencoding Variational Inference For Topic Models

ABSTRACT: Topic models are one of the most popular methods for learning representations of
text, but a major challenge is that any change to the topic model requires mathematically
deriving a new inference algorithm. A promising approach to address
this problem is autoencoding variational Bayes (AEVB), but it has proven diffi-
cult to apply to topic models in practice. We present what is to our knowledge the
first effective AEVB based inference method for latent Dirichlet allocation (LDA),
which we call Autoencoded Variational Inference For Topic Model (AVITM). This
model tackles the problems caused for AEVB by the Dirichlet prior and by component
collapsing. We find that AVITM matches traditional methods in accuracy
with much better inference time. Indeed, because of the inference network, we
find that it is unnecessary to pay the computational cost of running variational
optimization on test data. Because AVITM is black box, it is readily applied
to new topic models. As a dramatic illustration of this, we present a new topic
model called ProdLDA, that replaces the mixture model in LDA with a product
of experts. By changing only one line of code from LDA, we find that ProdLDA
yields much more interpretable topics, even if LDA is trained via collapsed Gibbs
sampling.

## item_id: m_2820

TITLE: AutoM3L: Automated Multimodal Machine Learning with Large Language Model

ABSTRACT: Automated Machine Learning (AutoML) stands as a promising solution for automating machine learning (ML) training pipelines to reduce manual costs. However, most current AutoML frameworks are confined to unimodal scenarios and exhibit limitations when extended to challenging and complex multimodal settings. Recent advances show that large language models (LLMs) have exceptional abilities in reasoning, interaction, and code generation, which shows promise in automating the ML pipelines. Innovatively, we propose AutoM3L, an Automated Multimodal Machine Learning framework, where LLMs act as controllers to automate training pipeline assembling. Specifically, AutoM3L offers automation and interactivity by first comprehending data modalities and then automatically selecting appropriate models to construct training pipelines in alignment with user requirements. Furthermore, it streamlines user engagement and removes the need for intensive manual feature engineering and hyperparameter optimization. At each stage, users can customize the pipelines through directives, which are the capabilities lacking in previous rule-based AutoML approaches. We conduct quantitative evaluations on four multimodal datasets spanning classification, regression, and retrieval, which yields that AutoM3L can achieve competitive or even better performance than traditional rule-based AutoML methods. We show the user friendliness and usability of AutoM3L in the user study. Code is available at:
https://anonymous.4open.science/r/anonymization_code

## item_id: m_2821

TITLE: A Latent Morphology Model for Open-Vocabulary Neural Machine Translation

ABSTRACT: Translation into morphologically-rich languages challenges neural machine translation (NMT) models with extremely sparse vocabularies where atomic treatment of surface forms is unrealistic. This problem is typically addressed by either pre-processing words into subword units or performing translation directly at the level of characters. The former is based on word segmentation algorithms optimized using corpus-level statistics with no regard to the translation task. The latter learns directly from translation data but requires rather deep architectures. In this paper, we propose to translate words by modeling word formation through a hierarchical latent variable model which mimics the process of morphological inflection. Our model generates words one character at a time by composing two latent representations: a continuous one, aimed at capturing the lexical semantics, and a set of (approximately) discrete features, aimed at capturing the morphosyntactic function, which are shared among different surface forms. Our model achieves better accuracy in translation into three morphologically-rich languages than conventional open-vocabulary NMT methods, while also demonstrating a better generalization capacity under low to mid-resource settings.

## item_id: m_2822

TITLE: Deep Denoising: Rate-Optimal Recovery of Structured Signals with a Deep Prior

ABSTRACT: Deep neural networks provide state-of-the-art performance for image denoising, where the goal is to recover a near noise-free image from a noisy image.
The underlying principle is that neural networks trained on large datasets have empirically been shown to be able to generate natural images well from a low-dimensional latent representation of the image.
Given such a generator network, or prior, a noisy image can be denoised by finding the closest image in the range of the prior.
However, there is little theory to justify this success, let alone to predict the denoising performance as a function of the networks parameters.
In this paper we consider the problem of denoising an image from additive Gaussian noise, assuming the image is well described by a deep neural network with ReLu activations functions, mapping a k-dimensional latent space to an n-dimensional image.
We state and analyze a simple gradient-descent-like iterative algorithm that minimizes a non-convex loss function, and provably removes a fraction of (1 - O(k/n)) of the noise energy.
We also demonstrate in numerical experiments that this denoising performance is, indeed, achieved by generative priors learned from data.

## item_id: m_2823

TITLE: Exploring and Enhancing the Transferability of Adversarial Examples

ABSTRACT:  State-of-the-art deep neural networks are vulnerable to adversarial examples, formed by applying small but malicious perturbations to the original inputs. Moreover, the perturbations can \textit{transfer across models}: adversarial examples generated for a specific model will often mislead other unseen models. Consequently the adversary can leverage it to attack deployed systems without any query, which severely hinders the application of deep learning, especially in the safety-critical areas. In this work, we empirically study how two classes of factors those might influence the transferability of adversarial examples.  One is about model-specific factors, including network architecture, model capacity and test accuracy. The other is the local smoothness of loss surface for constructing adversarial examples.  Inspired by  these understandings on the transferability of adversarial examples,  we then propose a simple but effective strategy  to enhance the transferability, whose effectiveness is confirmed by a variety of experiments on both  CIFAR-10 and ImageNet datasets.

## item_id: m_2824

TITLE: DEPT: Decoupled Embeddings for Pre-training Language Models

ABSTRACT: Language Model pre-training uses broad data mixtures to enhance performance across domains and languages. However, training on such heterogeneous text corpora requires extensive and expensive efforts. Since these data sources vary significantly in lexical, syntactic, and semantic aspects, they cause negative interference or the ``curse of multilinguality''. To address these challenges we propose a communication-efficient pre-training framework, DEPT. Our method decouples embeddings from the transformer body while simultaneously training the latter on multiple data sources without requiring a shared vocabulary. DEPT can: (1) train robustly and effectively under significant data heterogeneity, (2) minimize token embedding parameters to only what the data source vocabulary requires, while cutting communication costs in direct proportion to both the communication frequency and the reduction in parameters, (3) enhance transformer body plasticity and generalization, improving both average perplexity (up to 20%) and downstream task performance, and (4) enable training with custom optimized vocabularies per data source. We demonstrate DEPT's potential via the first vocabulary-agnostic federated pre-training of billion-scale models, reducing communication costs by orders of magnitude and embedding memory by 4-5x.

## item_id: m_2825

TITLE: Resource Efficient Self-Supervised Learning for Speech Recognition

ABSTRACT: Representation learning from sequential data using self-supervised learning (SSL) has proven to be a powerful technique and improved state-of-the-art (SOTA) results when fine tuned for various downstream tasks, including Automatic Speech Recognition (ASR). So far the success of SSL frameworks, e.g., Wav2Vec-2.0, for sequence-to-sequence (seq2seq) modeling is primarily carried out by masking intermediate features and then solving a contrastive task in an end-to-end manner. Although very successful, the overall training time (for example, days or weeks) and demanding resource requirements for achieving SOTA performance remain a significant barrier to further improving ASR solutions using such approaches. In this work we show that non-contrastive learning, such as an extension of the Barlow–Twins methodology, when applied to seq2seq SSL modeling improves convergence, while reducing training time. Our results show that Wav2Vec-2.0 architecture pre-training with a non-contrastive SSL approach reduces the GPU training hours by 2.3 times, compared to masking based SSL approaches, while achieving a significant improvement (i.e., up to 6% relative WER decrease) in the model performance for the ASR task. We further demonstrate that a combination of both masking based SSL and non-contrastive SSL improves the ASR performance, e.g., up to 12% relative WER decrease, for all splits of LibriSpeech evaluation dataset.


## item_id: m_2826

TITLE: PointARSim: Point-cloud–enhanced Generative Auto-Regressive Simulation for Closed-loop End-to-end Autonomous Driving Evaluation

ABSTRACT: End-to-end autonomous driving (E2E-AD) has garnered increasing attention in recent years. However, exist evaluation fails to simultaneously meet the requirements for both interactivity (e.g., CARLA) and realism (e.g., nuScenes). In this work, we introduce \textbf{\emph{PointARSim}}, an autoregressive generative simulation framework that leverages point cloud skeleton representation accumulated from offline datasets as conditions for diffusion models to synthesize multi-view images. Specifically, we separately aggregate foreground-background point cloud, facilitating utilization of visual geometry. To enable accurate control of the generated driving scene, we design a multi-conditioning ControlNet that integrates point cloud priors, previous-frame condition and optional backgrounds injection, 
 guided by a geometry-aware cycle loss. 
 Furthermore, to assess generative models’ fidelity when the ego-vehicle’s trajectory differs greatly from recorded offline logs, we introduce a new evaluation protocol based on the nuPlan dataset, called \textbf{\emph{nuPlan-SimGenEval}} benchmark.
 Extensive experiments on both nuScenes and nuPlan-SimGenEval demonstrate that the proposed approach significantly outperforms existing methods, highlighting its potential for next-generation closed-loop autonomous driving simulation.

## item_id: m_2827

TITLE: A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis

ABSTRACT: Pre-trained large language models (LLMs) have recently achieved better generalization and sample efficiency in autonomous web automation.
However, the performance on real-world websites has still suffered from (1) open domainness, (2) limited context length, and (3) lack of inductive bias on HTML.
We introduce WebAgent, an LLM-driven agent that learns from self-experience to complete tasks on real websites following natural language instructions.
WebAgent plans ahead by decomposing instructions into canonical sub-instructions, summarizes long HTML documents into task-relevant snippets, and acts on websites via Python programs generated from those.
We design WebAgent with Flan-U-PaLM, for grounded code generation, and HTML-T5, new pre-trained LLMs for long HTML documents using local and global attention mechanisms and a mixture of long-span denoising objectives, for planning and summarization.
We empirically demonstrate that our modular recipe improves the success on real websites by over 50%, and that HTML-T5 is the best model to solve various HTML understanding tasks; achieving 18.7% higher success rate than the prior method on MiniWoB web automation benchmark, and SoTA performance on Mind2Web, an offline task planning evaluation.

## item_id: m_2828

TITLE: Transferable Deep Clustering Model

ABSTRACT: Deep learning has shown remarkable success in the field of clustering recently. However, how to transfer a trained clustering model on a source domain to a target domain by leveraging the acquired knowledge to guide the clustering process remains challenging. Existing deep clustering methods often lack generalizability to new domains because they typically learn a group of fixed cluster centroids, which may not be optimal for the new domain distributions. In this paper, we propose a novel transferable deep clustering model that can automatically adapt the cluster centroids according to the distribution of data samples. Rather than learning a fixed set of centroids, our approach introduces a novel attention-based module that can adapt the centroids by measuring their relationship with samples. In addition, we theoretically show that our model is strictly more powerful than some classical clustering algorithms such as k-means or Gaussian Mixture Model (GMM). Experimental results on both synthetic and real-world datasets demonstrate the effectiveness and efficiency of our proposed transfer learning framework, which significantly improves the performance on target domain and reduces the computational cost.

## item_id: m_2829

TITLE: DART: A Principled Approach to Adversarially Robust Unsupervised Domain Adaptation

ABSTRACT: Distribution shifts and adversarial examples are two major challenges for deploying machine learning models. While these challenges have been studied individually, their combination is an important topic that remains relatively under-explored. In this work, we study the problem of adversarial robustness under a common setting of distribution shift – unsupervised domain adaptation (UDA). Specifically, given a labeled source domain $\mathcal{D}_S$ and an unlabeled target domain $\mathcal{D}_T$ with related but different distributions, the goal is to obtain an adversarially robust model for $\mathcal{D}_T$. The absence of target domain labels poses a unique challenge, as conventional adversarial robustness defenses cannot be directly applied to $\mathcal{D}_T$. To address this challenge, we first establish a generalization bound for the adversarial target loss, which consists of (i) terms related to the loss on the data, and (ii) a measure of worst-case domain divergence. Motivated by this bound, we develop a novel unified defense framework called *Divergence Aware adveRsarial Training* (DART), which can be used in conjunction with a variety of standard UDA  methods; e.g., DANN  (Ganin & Lempitsky, 2015). DART is applicable to general threat models, including the popular $\ell_p$-norm model, and does not require heuristic regularizers or architectural changes. We also release DomainRobust: a testbed for evaluating robustness of UDA models to adversarial attacks. DomainRobust consists of 4 multi-domain benchmark datasets (with 46 source-target pairs) and 7 meta-algorithms with a total of 11 variants. Our large-scale experiments demonstrate that on average, DART significantly enhances model robustness on all benchmarks compared to the state of the art, while maintaining competitive standard accuracy. The relative improvement in robustness from DART reaches up to 29.2% on the source-target domain pairs considered.

## item_id: m_2830

TITLE: High Probability Generalization Bounds with Fast Rates for Minimax Problems

ABSTRACT: Minimax problems are receiving an increasing amount of attention in a wide range of applications in machine learning (ML), for instance, reinforcement learning, robust optimization, adversarial learning, and distributed computing, to mention but a few. Current studies focus on the fundamental understanding of general minimax problems with an emphasis on convergence behavior. As a comparison, there is far less work to study the generalization performance. Additionally, existing generalization bounds are almost all derived in expectation, and the high probability bounds are all presented in the slow order $\mathcal{O}(1/\sqrt{n})$, where $n$ is the sample size. In this paper, we provide improved generalization analyses and obtain sharper high probability generalization bounds for most existing generalization measures of minimax problems. We then use the improved learning bounds to establish high probability generalization bounds with fast rates for classical empirical saddle point (ESP) solution and several popular gradient-based optimization algorithms, including gradient descent ascent (GDA), stochastic gradient descent ascent (SGDA), proximal point method (PPM), extra-gradient (EG), and optimistic gradient descent ascent (OGDA). In summary, we provide a systematical analysis of sharper generalization bounds of minimax problems.

## item_id: m_2831

TITLE: SNAP-UQ: Self-supervised Next-Activation Prediction for Single-Pass Uncertainty in TinyML

ABSTRACT: Reliable uncertainty estimation is a key missing piece for on-device monitoring in TinyML: microcontrollers must detect failures, distribution shift, or accuracy drops under strict flash/latency budgets, yet common uncertainty approaches (deep ensembles, MC dropout, early exits, temporal buffering) typically require multiple passes, extra branches, or state that is impractical on milliwatt hardware. This paper proposes a novel and practical method, SNAP-UQ, for single-pass, label-free uncertainty estimation based on depth-wise next-activation prediction. SNAP-UQ taps a small set of backbone layers and uses tiny int8 heads to predict the mean and scale of the next activation from a low-rank projection of the previous one; the resulting standardized prediction error forms a depth-wise surprisal signal that is aggregated and mapped through a lightweight monotone calibrator into an actionable uncertainty score. The design introduces no temporal buffers or auxiliary exits and preserves state-free inference, while increasing deployment footprint by only a few tens of kilobytes. Across vision and audio backbones, SNAP-UQ reduces flash and latency relative to early-exit and deep-ensemble baselines (typically $\sim$40--60% smaller and $\sim$25--35% faster), with several competing methods at similar accuracy often exceeding MCU memory limits. On corrupted streams, it improves accuracy-drop event detection by multiple AUPRC points and maintains strong failure detection (AUROC $\approx 0.9$) in a single forward pass. By grounding uncertainty in layer-to-layer dynamics rather than solely in output confidence, SNAP-UQ offers a novel, resource-efficient basis for robust TinyML monitoring. Our code is available at: https://github.com/Ism-ail11/SNAP-UQ

## item_id: m_2832

TITLE: PU-BENCH: A UNIFIED BENCHMARK FOR RIGOROUS AND REPRODUCIBLE PU LEARNING

ABSTRACT: Positive-Unlabeled (PU) learning, a challenging paradigm for training binary classifiers from only positive and unlabeled samples, is fundamental to many applications. While numerous PU learning methods have been proposed, the research is systematically hindered by the lack of a standardized and comprehensive benchmark for rigorous evaluation. Inconsistent data generation, disparate experimental settings, and divergent metrics have led to irreproducible findings and unsubstantiated performance claims. To address this foundational challenge, we introduce **PU-Bench**, the first unified open-source benchmark for PU learning. PU-Bench provides: 1) a unified data generation pipeline to ensure consistent input across configurable sampling schemes, label ratios and labeling mechanisms; 2) an integrated framework of 18 state-of-the-art PU methods; and 3) standardized protocols for reproducible assessment. Through a large-scale empirical study on 8 diverse datasets (**2880** evaluations in total), PU-Bench reveals a complex yet intuitive performance landscape, uncovering critical trade-offs between effectiveness and efficiency, and systematically mapping method robustness against variations in label frequency and selection bias. It is anticipated to serve as a foundational resource to catalyze reproducible, rigorous, and impactful research in the PU learning community. The source code is publicly available at <https://github.com/XiXiphus/PU-Bench>.

## item_id: m_2833

TITLE: A Hierarchy of Graph Neural Networks Based on Learnable Local Features

ABSTRACT: Graph neural networks (GNNs) are a powerful tool to learn representations on graphs by iteratively aggregating features from node neighbourhoods. Many variant models have been proposed, but there is limited understanding on both how to compare different architectures and how to construct GNNs systematically. Here, we propose a hierarchy of GNNs based on their aggregation regions. We derive theoretical results about the discriminative power and feature representation capabilities of each class. Then, we show how this framework can be utilized to systematically construct arbitrarily powerful GNNs. As an example, we construct a simple architecture that exceeds the expressiveness of the Weisfeiler-Lehman graph isomorphism test. We empirically validate our theory on both synthetic and real-world benchmarks, and demonstrate our example's theoretical power translates to state-of-the-art results on node classification, graph classification, and graph regression tasks. 

## item_id: m_2834

TITLE: ISAAC Newton: Input-based Approximate Curvature for Newton's Method

ABSTRACT: We present ISAAC (Input-baSed ApproximAte Curvature), a novel method that conditions the gradient using selected second-order information and has an asymptotically vanishing computational overhead, assuming a batch size smaller than the number of neurons. We show that it is possible to compute a good conditioner based on only the input to a respective layer without a substantial computational overhead. The proposed method allows effective training even in small-batch stochastic regimes, which makes it competitive to first-order as well as second-order methods.

## item_id: m_2835

TITLE: Discrete Representations Strengthen Vision Transformer Robustness

ABSTRACT: Vision Transformer (ViT) is emerging as the state-of-the-art architecture for image recognition. While recent studies suggest that ViTs are more robust than their convolutional counterparts, our experiments find that ViTs are overly reliant on local features (\eg, nuisances and texture) and fail to make adequate use of global context (\eg, shape and structure). As a result, ViTs fail to generalize to out-of-distribution, real-world data. To address this deficiency, we present a simple and effective architecture modification to ViT's input layer by adding discrete tokens produced by a vector-quantized encoder. Different from the standard continuous pixel tokens, discrete tokens are invariant under small perturbations and contain less information individually, which promote ViTs to learn global information that is invariant. Experimental results demonstrate that adding discrete representation on four architecture variants strengthens ViT robustness by up to 12\% across seven ImageNet robustness benchmarks while maintaining the performance on ImageNet.

## item_id: m_2836

TITLE: Manifold Learning via Data Topology Optimization: Gradient Method Application

ABSTRACT: The study of topological properties in data and their application to machine learning is a growing research area. While most methods operate in Euclidean space, alternative topologies (e.g., hyperbolic embeddings for recommender systems) often yield superior performance. However, real-world data sets lack a known intrinsic topology, which requires manual specification. We propose a novel method for inferring the underlying topological structure through joint optimization of a learnable distance matrix and embedding. Our approach combines the learning of neural networks with a differentiable Isomap implementation, enabling end-to-end optimization of both the metric and mapping. Experiments on synthetic non-Euclidean datasets demonstrate accurate topology recovery, suggesting broader applicability to real-world problems with unknown geometric structure, a claim we preliminarily validate on the MNIST dataset.

## item_id: m_2837

TITLE: Towards Building A Group-based Unsupervised Representation Disentanglement Framework

ABSTRACT: Disentangled representation learning is one of the major goals of deep learning, and is a key step for achieving explainable and generalizable models. The key idea of the state-of-the-art VAE-based unsupervised representation disentanglement methods is to minimize the total correlation of the joint distribution of the latent variables. However, it has been proved that their goal can not be achieved without introducing other inductive biases. The Group Theory based definition of representation disentanglement mathematically connects the data transformations to the representations using the formalism of group. In this paper, built on the group-based definition and inspired by the \emph{n-th dihedral group}, we first propose a theoretical framework towards achieving unsupervised representation disentanglement. We then propose a model based on existing VAE-based methods to tackle the unsupervised learning problem of the framework. In the theoretical framework, we prove three sufficient conditions on model, group structure, and data respectively in an effort to achieve, in an unsupervised way, disentangled representation per group-based definition. With these conditions, we offer an option, from the perspective of the group-based definition, for the inductive bias that existing VAE-based models lack. Experimentally, we train 1800 models covering the most prominent VAE-based methods on five datasets to verify the effectiveness of our theoretical framework. Compared to the original VAE-based methods, these Groupified VAEs consistently achieve better mean performance with smaller variances.

## item_id: m_2838

TITLE: Towards Understanding Regularization in Batch Normalization

ABSTRACT: Batch Normalization (BN) improves both convergence and generalization in training neural networks. This work understands these phenomena theoretically. We analyze BN by using a basic block of neural networks, consisting of a kernel layer, a BN layer, and a nonlinear activation function. This basic network helps us understand the impacts of BN in three aspects. First, by viewing BN as an implicit regularizer, BN can be decomposed into population normalization (PN) and gamma decay as an explicit regularization. Second, learning dynamics of BN and the regularization show that training converged with large maximum and effective learning rate. Third, generalization of BN is explored by using statistical mechanics. Experiments demonstrate that BN in convolutional neural networks share the same traits of regularization as the above analyses.

## item_id: m_2839

TITLE: Contextual memory bandit for pro-active dialog engagement

ABSTRACT: An objective of pro-activity in dialog systems is to enhance the usability of conversational
agents by enabling them to initiate conversation on their own. While
dialog systems have become increasingly popular during the last couple of years,
current task oriented dialog systems are still mainly reactive and users tend to
initiate conversations. In this paper, we propose to introduce the paradigm of contextual
bandits as framework for pro-active dialog systems. Contextual bandits
have been the model of choice for the problem of reward maximization with partial
feedback since they fit well to the task description. As a second contribution,
we introduce and explore the notion of memory into this paradigm. We propose
two differentiable memory models that act as parts of the parametric reward estimation
function. The first one, Convolutional Selective Memory Networks, uses
a selection of past interactions as part of the decision support. The second model,
called Contextual Attentive Memory Network, implements a differentiable attention
mechanism over the past interactions of the agent. The goal is to generalize
the classic model of contextual bandits to settings where temporal information
needs to be incorporated and leveraged in a learnable manner. Finally, we illustrate
the usability and performance of our model for building a pro-active mobile
assistant through an extensive set of experiments.

## item_id: m_2840

TITLE: On the Role of Self-supervision in Deep Multi-view Clustering

ABSTRACT: Self-supervised learning is a central component in many recent approaches to deep multi-view clustering (MVC). However, we find large variations in the motivation and design of self-supervision-based methods for deep MVC. To address this, we present DeepMVC, a new, unified framework for deep MVC. Crucially, we show that many recent methods can be regarded as instances of our framework -- allowing us to implement recent methods in a unified and consistent manner. We make key observations about the effect of self-supervision, and in particular, drawbacks of representation alignment. Motivated by these insights, we develop several new DeepMVC instances, with new forms of self-supervision. We conduct extensive experiments, and find that (i) the popular contrastive alignment degrades performance when the number of views becomes large; (ii) all methods benefit from some form of self-supervision; and (iii) our new instances outperform previous methods on several datasets. Based on our findings, we suggest several promising directions for future research. To enhance the openness of the field, we provide an open-source implementation of DeepMVC, including recent models and our new instances. Our implementation includes a consistent evaluation protocol, facilitating fair and accurate evaluation of methods and components.


## item_id: m_2841

TITLE: Contrastive Continuity on Augmentation Stability Rehearsal for Continual Self-Supervised Learning

ABSTRACT: Self-supervised learning has attracted a lot of attention recently, which is able to learn powerful representations without any manual annotations. In order to cope with a variety of real-world scenarios, it also needs to develop the ability to continuously learn, i.e. Continual Self-Supervised Learning (CSSL). However, simple rehearsal or regularization will bring some negative effects while alleviating catastrophic forgetting in CSSL, e.g. overfitting on the rehearsal samples or hindering from learning fresh knowledge. In order to address catastrophic forgetting without overfitting on the rehearsal samples, we propose Augmentation Stability Rehearsal (ASR) in this paper, which selects the most representative and discriminative samples by estimating the augmentation stability for rehearsal. Meanwhile, we design a matching strategy for ASR to dynamically update the rehearsal buffer. In addition, we further propose Contrastive Continuity on Augmentation Stability Rehearsal (C$^2$ ASR) based on ASR, which preserves as much information shared among seen task streams as possible to prevent catastrophic forgetting and dismisses the redundant information to free up the ability to learn fresh knowledge. Our method obtains a great achievement compared with state-of-the-art CSSL methods on a variety of CSSL benchmarks. The source code will be released soon. 

## item_id: m_2842

TITLE: Early Stopping for Deep Image Prior

ABSTRACT: Deep image prior (DIP) and its variants have shown remarkable potential for solving inverse problems in computational imaging (CI), needing no separate training data. Practical DIP models are often substantially overparameterized. During the learning process, these models learn the desired visual content first and then pick up the potential modeling and observational noise, i.e., overfitting. Thus, the practicality of DIP hinges on early stopping (ES) that captures the transition period. In this regard, the majority of prior DIP works for CI tasks only demonstrate the potential of the models---reporting the peak performance against the groundtruth but providing no clue about how to operationally obtain near-peak performance without access to the groundtruth. In this paper, we set to break this practicality barrier of DIP, and propose an efficient ES strategy that consistently detects near-peak performance across several CI tasks and DIP variants. Simply based on the running variance of DIP intermediate reconstructions, our ES method not only outpaces the existing ones---which only work in very narrow regimes, but also remains effective when combined with methods that try to mitigate overfitting.

## item_id: m_2843

TITLE: HalentNet: Multimodal Trajectory Forecasting with Hallucinative Intents

ABSTRACT: Motion forecasting is essential for making intelligent decisions in robotic navigation. As a result, the multi-agent behavioral prediction has become a core component of modern human-robot interaction applications such as autonomous driving. Due to various intentions and interactions among agents, agent trajectories can have multiple possible futures. Hence, the motion forecasting model's ability to cover possible modes becomes essential to enable accurate prediction. Towards this goal, we introduce HalentNet to better model the future motion distribution in addition to a traditional trajectory regression learning objective by incorporating generative augmentation losses. We model intents with unsupervised discrete random variables whose training is guided by a collaboration between two key signals: A discriminative loss that encourages intents' diversity and a hallucinative loss that explores intent transitions (i.e., mixed intents) and encourages their smoothness. This regulates the neural network behavior to be more accurately predictive on uncertain scenarios due to the active yet careful exploration of possible future agent behavior. Our model's learned representation leads to better and more semantically meaningful coverage of the trajectory distribution. Our experiments show that our method can improve over the state-of-the-art trajectory forecasting benchmarks, including vehicles and pedestrians, for about 20% on average FDE and 50% on road boundary violation rate when predicting 6 seconds future. We also conducted human experiments to show that our predicted trajectories received 39.6% more votes than the runner-up approach and 32.2% more votes than our variant without hallucinative mixed intent loss. The code will be released soon. 

## item_id: m_2844

TITLE: WaveFlow: A Compact Flow-based Model for Raw Audio

ABSTRACT: In this work, we present WaveFlow, a small-footprint generative flow for raw audio, which is trained with maximum likelihood without complicated density distillation and auxiliary losses as used in Parallel WaveNet.  It provides a unified view of flow-based models for raw audio, including autoregressive flow (e.g., WaveNet) and bipartite flow (e.g., WaveGlow) as special cases. We systematically study these likelihood-based generative models for raw waveforms in terms of test likelihood and speech fidelity. We demonstrate that WaveFlow can synthesize high-fidelity speech and obtain comparable likelihood as WaveNet, while only requiring a few sequential steps to generate very long waveforms.  In particular, our small-footprint WaveFlow has only 5.91M parameters and can generate 22.05kHz speech 15.39 times faster than real-time on a GPU without customized inference kernels.

## item_id: m_2845

TITLE: Generalized Tensor Models for Recurrent Neural Networks

ABSTRACT: Recurrent Neural Networks (RNNs) are very successful at solving challenging problems with sequential data. However, this observed efficiency is not yet entirely explained by theory. It is known that a certain class of multiplicative RNNs enjoys the property of depth efficiency --- a shallow network of exponentially large width is necessary to realize the same score function as computed by such an RNN. Such networks, however, are not very often applied to real life tasks. In this work, we attempt to reduce the gap between theory and practice by extending the theoretical analysis to RNNs which employ various nonlinearities, such as Rectified Linear Unit (ReLU), and show that they also benefit from properties of universality and depth efficiency. Our theoretical results are verified by a series of extensive computational experiments.

## item_id: m_2846

TITLE: Characterizing ResNet's Universal Approximation Capability

ABSTRACT: Since its debut in 2016, ResNet has become arguably the most favorable architecture in deep neural network (DNN) design. It effectively addresses the gradient vanishing issue in DNN training, allowing engineers to fully unleash DNN's potential in tackling challenging problems in various domains. Despite its practical success, an essential theoretical question remains largely open: how well can ResNet approximate functions? In this paper, we show that ResNet with bottleneck blocks (b-ResNet) can approximate any $d$-dimensional monomial with degree $p$ to any accuracy $\epsilon>0$ with $\mathcal{O}(dp\log (p/\epsilon))$ number of weights and we extend the results to polynomials, smooth functions, continuous functions. This is a factor of $d$ reduction in the number of training weights compared with the classical results for ReLU feedforward networks. Our results reveal that a continuous-depth network generated via a dynamical system possesses significant approximation capabilities even if its dynamics function is realized by a shallow ReLU network with absolute constant neurons. Furthermore, our achievability result is order-optimal in terms of $\epsilon$ as it matches the generalized lower bound. Besides, we apply ResNet can approximate a special function class based on Kolmogrovo Superposition Theorem with $\mathcal{O}(d^4\epsilon^{-1})$ tuning weights to overcome the curse of dimension. This work adds to the theoretical justifications for ResNet's stellar practical performance.

## item_id: m_2847

TITLE: On Bias-Variance Alignment in Deep Models

ABSTRACT: Classical wisdom in machine learning holds that the generalization error can be decomposed into bias and variance, and these two terms exhibit a \emph{trade-off}. However, in this paper, we show that for an ensemble of deep learning based classification models, bias and variance are \emph{aligned} at a sample level, where squared bias is approximately \emph{equal} to variance for correctly classified sample points. We present empirical evidence confirming this phenomenon in a variety of deep learning models and datasets. Moreover, we study this phenomenon from two theoretical perspectives: calibration and neural collapse. We first show theoretically that under the assumption that the models are well calibrated, we can observe the bias-variance alignment. Second, starting from the picture provided by the neural collapse theory, we show an approximate correlation between bias and variance.

## item_id: m_2848

TITLE: Deep Multi-task Representation Learning: A Tensor Factorisation Approach

ABSTRACT: Most contemporary multi-task learning methods assume linear models. This setting is considered shallow in the era of deep learning. In this paper, we present a new deep multi-task representation learning framework that learns cross-task sharing structure at every layer in a deep network. Our approach is based on generalising the matrix factorisation techniques explicitly or implicitly used by many conventional MTL algorithms to tensor factorisation, to realise automatic learning of end-to-end knowledge sharing in deep networks. This is in contrast to existing deep learning approaches that need a user-defined multi-task sharing strategy. Our approach applies to both homogeneous and heterogeneous MTL. Experiments demonstrate the efficacy of our deep multi-task representation learning in terms of both higher accuracy and fewer design choices.

## item_id: m_2849

TITLE: Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift

ABSTRACT: Statistical properties such as mean and variance often change over time in time series, i.e., time-series data suffer from a distribution shift problem. This change in temporal distribution is one of the main challenges that prevent accurate time-series forecasting. To address this issue, we propose a simple yet effective normalization method called reversible instance normalization (RevIN), a generally-applicable normalization-and-denormalization method with learnable affine transformation. The proposed method is symmetrically structured to remove and restore the statistical information of a time-series instance, leading to significant performance improvements in time-series forecasting, as shown in Fig. 1. We demonstrate the effectiveness of RevIN via extensive quantitative and qualitative analyses on various real-world datasets, addressing the distribution shift problem.

## item_id: m_2850

TITLE: Why Is the Counterintuitive Phenomenon of Likelihood Rare in Tabular Anomaly Detection with Deep Generative Models?

ABSTRACT: Deep generative models with tractable and analytically computable likelihoods, exemplified by normalizing flows, offer an effective basis for anomaly detection through likelihood-based scoring. We demonstrate that, unlike in the image domain where deep generative models frequently assign higher likelihoods to anomalous data, such counterintuitive behavior occurs far less often in tabular settings. We first introduce a domain-agnostic formulation that enables consistent detection and evaluation of the counterintuitive phenomenon, addressing the absence of precise definition. Through extensive experiments on 47 tabular datasets and 10 CV/NLP embedding datasets in ADBench, benchmarked against 12 baseline models, we demonstrate that the phenomenon, as defined, is consistently rare in general tabular data. We further investigate this phenomenon from both theoretical and empirical perspectives, focusing on the roles of data dimensionality and feature correlation difference. We find that likelihood-only detection with normalizing flows offers a practical and reliable approach for anomaly detection in tabular domains.

## item_id: m_2851

TITLE: Learning Fast Samplers for Diffusion Models by Differentiating Through Sample Quality

ABSTRACT: Diffusion models have emerged as an expressive family of generative models rivaling GANs in sample quality and autoregressive models in likelihood scores. Standard diffusion models typically require hundreds of forward passes through the model to generate a single high-fidelity sample. We introduce Differentiable Diffusion Sampler Search (DDSS): a method that optimizes fast samplers for any pre-trained diffusion model by differentiating through sample quality scores. We also present Generalized Gaussian Diffusion Models (GGDM), a family of flexible non-Markovian samplers for diffusion models. We show that optimizing the degrees of freedom of GGDM samplers by maximizing sample quality scores via gradient descent leads to improved sample quality. Our optimization procedure backpropagates through the sampling process using the reparametrization trick and gradient rematerialization. DDSS achieves strong results on unconditional image generation across various datasets (e.g., FID scores on LSUN church 128x128 of 11.6 with only 10 inference steps, and 4.82 with 20 steps, compared to 51.1 and 14.9 with strongest DDPM/DDIM baselines). Our method is compatible with any pre-trained diffusion model without fine-tuning or re-training required.

## item_id: m_2852

TITLE: Target-Driven Policy Optimization for Sequential Counterfactual Outcome Control

ABSTRACT: Identifying optimal treatment sequences from offline data to guide temporal systems toward target outcomes is a critical challenge with profound implications for fields like personalized medicine. While existing methods are mostly evaluated in offline settings, practical applications demand online, adaptive strategies that can respond in real-time. To address this, we propose \textbf{G}oal-aware \textbf{I}ntervention via \textbf{F}actual-\textbf{T}arget Training (\textbf{GIFT}), a novel framework for learning sequential treatment policies from observational data. GIFT learns a goal-conditioned policy by applying variance-controlled importance weights, which serves as our reward-rescaling mechanism, to guide patient trajectories towards a desired target. Theoretically, our algorithm is guaranteed to converge, and we characterize its induced approximation bias by bounding the gap between our solution and the learned policy's true value. Experiments show GIFT significantly outperforms existing methods in creating goal-oriented policies for online deployment.

## item_id: m_2853

TITLE: Exploring Balanced Feature Spaces for Representation Learning

ABSTRACT: Existing self-supervised learning (SSL) methods are mostly applied for training representation models from artificially balanced datasets (e.g., ImageNet). It is unclear how well they will perform in the practical scenarios where datasets are often imbalanced w.r.t. the classes. Motivated by this question, we conduct a series of studies on the performance of self-supervised contrastive learning and supervised learning methods over multiple datasets where training instance distributions vary from a balanced one to a long-tailed one. Our findings are quite intriguing. Different from supervised methods with large performance drop, the self-supervised contrastive learning methods perform stably well even when the datasets are heavily imbalanced. This motivates us to explore the balanced feature spaces learned by contrastive learning, where the feature representations present similar linear separability w.r.t. all the classes. Our further experiments reveal that a representation model generating a balanced feature space can generalize better than that yielding an imbalanced one across multiple settings. Inspired by these insights, we develop a novel representation learning method, called $k$-positive contrastive learning. It effectively combines strengths of the supervised method and the contrastive learning method to learn representations that are both discriminative and balanced. Extensive experiments demonstrate its superiority on multiple recognition tasks. Remarkably, it achieves new state-of-the-art on challenging long-tailed recognition benchmarks. Code and models will be released.

## item_id: m_2854

TITLE: not-MIWAE: Deep Generative Modelling with Missing not at Random Data

ABSTRACT: When a missing process depends on the missing values themselves, it needs to be explicitly modelled and taken into account while doing likelihood-based inference. We present an approach for building and fitting deep latent variable models (DLVMs) in cases where the missing process is dependent on the missing data. Specifically, a deep neural network enables us to flexibly model the conditional distribution of the missingness pattern given the data. This allows for incorporating prior information about the type of missingness (e.g.~self-censoring) into the model. Our inference technique, based on importance-weighted variational inference, involves maximising a lower bound of the joint likelihood. Stochastic gradients of the bound are obtained by using the reparameterisation trick both in latent space and data space. We show on various kinds of data sets and missingness patterns that explicitly modelling the missing process can be invaluable.

## item_id: m_2855

TITLE: Unleashing Graph Transformers with Green and Martin Kernels

ABSTRACT: Graph Transformers (GTs) are rapidly emerging as superior models, surpassing traditional message-passing neural networks in graph-level tasks. For optimal performance, it is essential to design GT architectures that embed graph inductive biases and utilize global attention mechanisms through effective structural encodings (SEs). In this work, we introduce novel SEs derived from a rigorous theoretical analysis of random walks (RWs), specifically leveraging the Green and Martin kernels. The Green and Martin kernels are mathematical tools used to observe the long-term behavior of RWs on graphs. By integrating these kernels into the encoding process, we enhance their capability to accurately represent complex graph structures. Our empirical evaluations demonstrate that these approaches enable GTs to achieve state-of-the-art performance on 7 out of 8 benchmark datasets. These include molecular datasets characterized by intricate, non-aperiodic substructures such as benzene rings, and directed acyclic graphs common in the circuit domain. We attribute these performance improvement to the effective capture of the characteristics of non-aperiodic substructures and directed acyclic graphs by our extending encodings. The results not only validate the effectiveness of integrating the Green and Martin kernels into RW-based encodings but also underscore their potential to substantially enhance the learning capabilities of GTs across diverse applications.

## item_id: m_2856

TITLE: Paleo: A Performance Model for Deep Neural Networks

ABSTRACT: Although various scalable deep learning software packages have been proposed, it remains unclear how to best leverage parallel and distributed computing infrastructure to accelerate their training and deployment. Moreover, the effectiveness of existing parallel and distributed systems varies widely based on the neural network architecture and dataset under consideration.  In order to efficiently explore the space of scalable deep learning systems and quickly diagnose their effectiveness for a given problem instance, we introduce an analytical performance model called Paleo. Our key observation is that a neural network architecture carries with it a declarative specification of the computational requirements associated with its training and evaluation. By extracting these requirements from a given architecture and mapping them to a specific point within the design space of software, hardware and communication strategies, Paleo can efficiently and accurately model the expected scalability and performance of a putative deep learning system.  We show that Paleo is robust to the choice of network architecture, hardware, software, communication schemes, and parallelization strategies. We further demonstrate its ability to accurately model various recently published scalability results for CNNs such as NiN, Inception and AlexNet.

## item_id: m_2857

TITLE: RoMA: a Method for Neural Network Robustness Measurement and Assessment 

ABSTRACT: Neural network models have become the leading solution for various tasks, such
as classification, language processing, protein folding, and others. However, their
reliability is heavily plagued by adversarial inputs: small input perturbations that
cause the model to produce erroneous output, thus impairing the model’s robustness.
Adversarial inputs can occur naturally when the system’s environment behaves
randomly, even in the absence of a malicious adversary, and are thus a severe
cause for concern when attempting to deploy neural networks within critical
systems. In this paper, we present a new statistical method, called Robustness
Measurement and Assessment (RoMA), which can accurately measure the robustness
of a neural network model. Specifically, RoMA determines the probability
that a random input perturbation might cause misclassification. The method allows
us to provide formal guarantees regarding the expected number of errors a
trained model will have after deployment. Our approach can be implemented on
large-scale, black-box neural networks, which is a significant advantage compared
to recently proposed verification methods. We apply our approach in two ways:
comparing the robustness of different models, and measuring how a model’s robustness
is affected by the scale of adversarial perturbation. One interesting insight
obtained through this work is that, in a classification network, different output
labels can exhibit very different robustness levels. We term this phenomenon
Categorial Robustness. Our ability to perform risk and robustness assessments
on a categorial basis opens the door to risk mitigation, which may prove to be a
significant step towards neural network certification in safety-critical applications.

## item_id: m_2858

TITLE: Modeling Uncertainty with Hedged Instance Embeddings

ABSTRACT: Instance embeddings are an efficient and versatile image representation that facilitates applications like recognition, verification, retrieval, and clustering. Many metric learning methods represent the input as a single point in the embedding space. Often the distance between points is used as a proxy for match confidence. However, this can fail to represent uncertainty which can arise when the input is ambiguous, e.g., due to occlusion or blurriness. This work addresses this issue and explicitly models the uncertainty by “hedging” the location of each input in the embedding space. We introduce the hedged instance embedding (HIB) in which embeddings are modeled as random variables and the model is trained under the variational information bottleneck principle (Alemi et al., 2016; Achille & Soatto, 2018). Empirical results on our new N-digit MNIST dataset show that our method leads to the desired behavior of “hedging its bets” across the embedding space upon encountering ambiguous inputs. This results in improved performance for image matching and classification tasks, more structure in the learned embedding space, and an ability to compute a per-exemplar uncertainty measure which is correlated with downstream performance.

## item_id: m_2859

TITLE: A Learning Theoretic Perspective on Local Explainability

ABSTRACT: In this paper, we explore connections between interpretable machine learning and learning theory through the lens of local approximation explanations. First, we tackle the traditional problem of performance generalization and bound the test-time predictive accuracy of a model using a notion of how locally explainable it is.  Second, we explore the novel problem of explanation generalization which is an important concern for a growing class of finite sample-based local approximation explanations. Finally, we validate our theoretical results empirically and show that they reflect what can be seen in practice.

## item_id: m_2860

TITLE: Gaussian Prototypical Networks for Few-Shot Learning on Omniglot

ABSTRACT: We propose a novel architecture for k-shot classification on the Omniglot dataset. Building on prototypical networks, we extend their architecture to what we call Gaussian prototypical networks. Prototypical networks learn a map between images and embedding vectors, and use their clustering for classification. In our model, a part of the encoder output is interpreted as a confidence region estimate about the embedding point, and expressed as a Gaussian covariance matrix. Our network then constructs a direction and class dependent distance metric on the embedding space, using uncertainties of individual data points as weights. We show that Gaussian prototypical networks are a preferred architecture over vanilla prototypical networks with an equivalent number of parameters. We report results consistent with state-of-the-art performance in 1-shot and 5-shot classification both in 5-way and 20-way regime on the Omniglot dataset. We explore artificially down-sampling a fraction of images in the training set, which improves our performance. Our experiments therefore lead us to hypothesize that Gaussian prototypical networks might perform better in less homogeneous, noisier datasets, which are commonplace in real world applications.

## item_id: m_2861

TITLE: Towards Faithful Neural Network Intrinsic Interpretation with Shapley Additive Self-Attribution

ABSTRACT: Self-interpreting neural networks have garnered significant interest in research. Existing works in this domain often (1) lack a solid theoretical foundation ensuring genuine interpretability or (2) compromise model expressiveness. In response, we formulate a generic Additive Self-Attribution (ASA) framework. Observing the absence of Shapley value in Additive Self-Attribution, we propose Shapley Additive Self-Attributing Neural Network (SASANet), with theoretical guarantees for the self-attribution value equal to the output's Shapley values. Specifically, SASANet uses a marginal contribution-based sequential schema and internal distillation-based training strategies to model meaningful outputs for any number of features, resulting in un-approximated meaningful value function. Our experimental results indicate SASANet surpasses existing self-attributing models in performance and rivals black-box models. Moreover, SASANet is shown more precise and efficient than post-hoc methods in interpreting its own predictions.

## item_id: m_2862

TITLE: Information Dropout: learning optimal representations through noise

ABSTRACT: We introduce Information Dropout, a generalization of dropout that is motivated by the Information Bottleneck principle and highlights the way in which injecting noise in the activations can help in learning optimal representations of the data. Information Dropout is rooted in information theoretic principles, it includes as special cases several existing dropout methods, like Gaussian Dropout and Variational Dropout, and, unlike classical dropout, it can learn and build representations that are invariant to nuisances of the data, like occlusions and clutter. When the task is the reconstruction of the input, we show that the information dropout method yields a variational autoencoder as a special case, thus providing a link between representation learning, information theory and variational inference. Our experiments validate the theoretical intuitions behind our method, and we find that information dropout achieves a comparable or better generalization performance than binary dropout, especially on smaller models, since it can automatically adapt the noise to the structure of the network, as well as to the test sample.

## item_id: m_2863

TITLE: Reduced-Rank Online Gaussian Process Modeling With Uncertain Inputs

ABSTRACT: Gaussian Process (GP) is an increasingly popular modeling approach. In its classical formulation, the inputs are supposed to be perfectly known. However, in some use cases, this assumption is not true: the inputs as well as the outputs can be corrupted by noise. Some methods already insert these uncertainties in GP modeling but the only currently existing online algorithm (i.e.  that incrementally updates the model each time a measure is acquired) still lacks in robustness and precision. In this article we propose a novel online Gaussian Process (GP) modeling approach for vector field mapping with uncertain inputs. They are included into the GP through a complete second-order Taylor approximation with a better estimation of variances. Our experiments prove that our algorithm is more accurate and robust than the previous online method for a shorter computing time. Moreover, for high input uncertainties, our method achieves better performance than both online and offline state of the art methods on simulated data. This algorithm can also be applied to diverse real scenarios which require precise estimation of unknown functions from a small set of corrupted datapoints, as we show in the challenging problem of indoor localization, mapping magnetic fields.

## item_id: m_2864

TITLE: Regularizing and Optimizing LSTM Language Models

ABSTRACT: In this paper, we consider the specific problem of word-level language modeling and investigate strategies for regularizing and optimizing LSTM-based models. We propose the weight-dropped LSTM, which uses DropConnect on hidden-to-hidden weights, as a form of recurrent regularization. Further, we introduce NT-ASGD, a non-monotonically triggered  (NT) variant of the averaged stochastic gradient method (ASGD), wherein the averaging trigger is determined using a NT condition as opposed to being tuned by the user. Using these and other regularization strategies, our ASGD Weight-Dropped LSTM (AWD-LSTM) achieves state-of-the-art word level perplexities on two data sets: 57.3 on Penn Treebank and 65.8 on WikiText-2. In exploring the effectiveness of a neural cache in conjunction with our proposed model, we achieve an even lower state-of-the-art perplexity of 52.8 on Penn Treebank and 52.0 on WikiText-2. We also explore the viability of the proposed regularization and optimization strategies in the context of the quasi-recurrent neural network (QRNN) and demonstrate comparable performance to the AWD-LSTM counterpart. The code for reproducing the results is open sourced and is available at https://github.com/salesforce/awd-lstm-lm.

## item_id: m_2865

TITLE: Solving Non-Stationary Bandit Problems with an RNN and an Energy Minimization Loss

ABSTRACT: We consider a Multi-Armed Bandit problem in which the rewards are non-stationary and are dependent on past actions and potentially on past contexts. At the heart of our method, we employ a recurrent neural network, which models these sequences. 
In order to balance between exploration and exploitation, we present an energy minimization term that prevents the neural network from becoming too confident in support of a certain action. This term provably limits the gap between the maximal and minimal probabilities assigned by the network. In a diverse set of experiments, we demonstrate that our method is at least as effective as methods suggested to solve the sub-problem of Rotting Bandits, can solve intuitive extensions of various benchmark problems, and is effective in a real-world recommendation system scenario.

## item_id: m_2866

TITLE: Effective Certification of Monotone Deep Equilibrium Models

ABSTRACT: Monotone Operator Equilibrium Models (monDEQs) represent a class of models that combine the powerful deep equilibrium paradigm with convergence guarantees. As monDEQs are inherently robust to adversarial perturbations, investigating new methods to certify their robustness is a promising research direction. Unfortunately, existing certification approaches are either imprecise or severely limited in their scalability. In this work, we propose the first scalable \emph{and} precise monDEQ verifier, based on two key ideas: (i) a novel convex relaxation which enables efficient inclusion checks, and (ii) non-trivial mathematical insights characterizing the fixpoint operations at the heart of monDEQs on sets rather than concrete inputs. An extensive evaluation of our verifier demonstrates that on the challenging $\ell_\infty$ perturbations it exceeds state-of-the-art performance in terms of speed (two orders of magnitude) and scalability (an order of magnitude) while yielding 25\% higher certified accuracies on the same networks.

## item_id: m_2867

TITLE: A Stable and Scalable Method for Solving Initial Value PDEs with Neural Networks

ABSTRACT: Unlike conventional grid and mesh based methods for solving partial differential equations (PDEs), neural networks have the potential to break the curse of dimensionality, providing approximate solutions to problems where using classical solvers is difficult or impossible. While global minimization of the PDE residual over the network parameters works well for boundary value problems, catastrophic forgetting impairs applicability to initial value problems (IVPs). In an alternative local-in-time approach, the optimization problem can be converted into an ordinary differential equation (ODE) on the network parameters and the solution propagated forward in time; however, we demonstrate that current methods based on this approach suffer from two key issues. First, following the ODE produces an uncontrolled growth in the conditioning of the problem, ultimately leading to unacceptably large numerical errors. Second, as the ODE methods scale cubically with the number of model parameters, they are restricted to small neural networks, significantly limiting their ability to represent intricate PDE initial conditions and solutions. Building on these insights, we develop Neural-IVP, an ODE based IVP solver which prevents the network from getting ill-conditioned and runs in time linear in the number of parameters, enabling us to evolve the dynamics of challenging PDEs with neural networks.

## item_id: m_2868

TITLE: Understanding the effects of data parallelism and sparsity on neural network training

ABSTRACT: We study two factors in neural network training: data parallelism and sparsity; here, data parallelism means processing training data in parallel using distributed systems (or equivalently increasing batch size), so that training can be accelerated; for sparsity, we refer to pruning parameters in a neural network model, so as to reduce computational and memory cost. Despite their promising benefits, however, understanding of their effects on neural network training remains elusive. In this work, we first measure these effects rigorously by conducting extensive experiments while tuning all metaparameters involved in the optimization. As a result, we find across various workloads of data set, network model, and optimization algorithm that there exists a general scaling trend between batch size and number of training steps to convergence for the effect of data parallelism, and further, difficulty of training under sparsity. Then, we develop a theoretical analysis based on the convergence properties of stochastic gradient methods and smoothness of the optimization landscape, which illustrates the observed phenomena precisely and generally, establishing a better account of the effects of data parallelism and sparsity on neural network training.

## item_id: m_2869

TITLE: Incorporating Implicit Regularization to Enhance the Transition Matrix Method for Effective Handling of Diverse Label Noise

ABSTRACT: Among various methods for learning with noisy labels, the transition matrix method has attracted sustained attention due to its simplicity and statistical consistency. However, estimating the transition matrix for each sample may be unidentifiable and computationally expensive in the case of instance-dependent label noise and real-world situations. In this paper, we propose a concise method that only requires estimating a global matrix, combining with implicit regularization, to replace the estimation of the individual transition matrix for each sample. Specifically, by estimating the transition matrix, we can determine the overall probability transfer from correct labels to noisy labels and use implicit regularization to adjust the sparse form representation of the difference between the estimated posterior probability distribution and the noisy label distribution. This approach can be applied to diverse types of noise as well as alleviating the problem of inaccurate posterior probability estimation. We theoretically analyze the consistency and generalization results of the proposed method and conduct experiments on synthetic and real-world datasets with different types of label noise. The experimental results show that our method significantly outperforms previous transition matrix methods and has a wider range of applicability. Additionally, our method achieves impressive results without the need for additional auxiliary techniques. Our code will be open source and put on Github.

## item_id: m_2870

TITLE: MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning

ABSTRACT: The recently released GPT-4 Code Interpreter has demonstrated remarkable proficiency in solving challenging math problems, primarily attributed to its ability to seamlessly reason with natural language, generate code, execute code, and continue reasoning based on the execution output. In this paper, we present a method to fine-tune open-source language models, enabling them to use code for modeling and deriving math equations and, consequently, enhancing their mathematical reasoning abilities. We propose a method of generating novel and high-quality datasets with math problems and their code-based solutions, referred to as MathCodeInstruct. Each solution interleaves $\textit{natural language}$, $\textit{code}$, and $\textit{execution results}$. We also introduce a customized supervised fine-tuning and inference approach. This approach yields the MathCoder models, a family of models capable of generating code-based solutions for solving challenging math problems. Impressively, the MathCoder models achieve state-of-the-art scores among open-source LLMs on the MATH (45.2%) and GSM8K (83.9%) datasets, substantially outperforming other open-source alternatives. Notably, the MathCoder model not only surpasses ChatGPT-3.5 and PaLM-2 on GSM8K and MATH but also outperforms GPT-4 on the competition-level MATH dataset. The proposed dataset and models will be released upon acceptance.

## item_id: m_2871

TITLE: Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias

ABSTRACT: Large language models (LLMs) are highly vulnerable to input confirmation bias. When a prompt implies a preferred answer, models often reinforce that bias rather than explore alternatives. 
This phenomenon remains underexplored, yet it is already harmful in base models and poses an even greater risk in multi-agent debate, where echo chambers reinforce bias instead of correction.
We introduce \emph{\textbf{M}ixture \textbf{o}f \textbf{La}tent \textbf{C}oncept \textbf{E}xperts (\textbf{MoLaCE})}, a framework that directly addresses confirmation bias through a mixture of hidden experts.
Our method identifies a latent direction in the model internal representations that reflects confirmation bias, instantiates experts as different activation strengths along this direction, and employs a gating mechanism to adaptively mix their predictions. 
This design enables a single LLM to emulate the benefits of debate internally while remaining lightweight and scalable. 
It can also be integrated into multi-agent debate frameworks to diversify perspectives and reduce correlated errors. 
We empirically show that it consistently reduces confirmation bias, improves robustness, and matches or surpasses multi-agent debate while requiring only a fraction of the computation.

## item_id: m_2872

TITLE: Search-Guided, Lightly-supervised Training of  Structured Prediction Energy Networks

ABSTRACT:  In structured output prediction tasks, labeling ground-truth training output is often expensive. However, for many tasks, even when the true output is unknown, we can evaluate predictions using a scalar reward function, which may be easily assembled from human knowledge or non-differentiable pipelines.  But searching through the entire output space to find the best output with respect to this reward function is typically intractable.  In this paper, we instead use efficient truncated randomized search in this reward function to train structured prediction energy networks (SPENs), which provide efficient test-time inference using gradient-based search on a smooth, learned representation of the score landscape, and have previously yielded state-of-the-art results in structured prediction.  In particular, this truncated randomized search in the reward function yields previously unknown local improvements, providing effective supervision to SPENs, avoiding their traditional need for labeled training data. 

## item_id: m_2873

TITLE: Fast topological clustering with Wasserstein distance

ABSTRACT: The topological patterns exhibited by many real-world networks motivate the development of topology-based methods for assessing the similarity of networks. However, extracting topological structure is difficult, especially for large and dense networks whose node degrees range over multiple orders of magnitude. In this paper, we propose a novel and computationally practical topological clustering method that clusters complex networks with intricate topology using principled theory from persistent homology and optimal transport. Such networks are aggregated into clusters through a centroid-based clustering strategy based on both their topological and geometric structure, preserving correspondence between nodes in different networks. The notions of topological proximity and centroid are characterized using a novel and efficient approach to computation of the Wasserstein distance and barycenter for persistence barcodes associated with connected components and cycles. The proposed method is demonstrated to be effective using both simulated networks and measured functional brain networks.

## item_id: m_2874

TITLE: The (Un)reliability of saliency methods

ABSTRACT: Saliency methods aim to explain the predictions of deep neural networks. These methods lack reliability when the explanation is sensitive to factors that do not contribute to the model prediction. We use a simple and common pre-processing step ---adding a mean shift to the input data--- to show that a transformation with no effect on the model can cause numerous methods to incorrectly attribute. We define input invariance as the requirement that a saliency method mirror the sensitivity of the model with respect to transformations of the input. We show, through several examples, that saliency methods that do not satisfy a input invariance property are unreliable and can lead to misleading and inaccurate attribution.

## item_id: m_2875

TITLE: IgGM: A Generative Model for Functional Antibody and Nanobody Design

ABSTRACT: Immunoglobulins are crucial proteins produced by the immune system to identify and bind to foreign substances, playing an essential role in shielding organisms from infections and diseases. Designing specific antibodies opens new pathways for disease treatment. With the rise of deep learning, AI-driven drug design has become possible, leading to several methods for antibody design. However, many of these approaches require additional conditions that differ from real-world scenarios, making it challenging to incorporate them into existing antibody design processes. Here, we introduce IgGM, a generative model for the de novo design of immunoglobulins with functional specificity. IgGM simultaneously generates antibody sequences and structures for a given antigen, consisting of three core components: a pre-trained language model for extracting sequence features, a feature learning module for identifying pertinent features, and a prediction module that outputs designed antibody sequences and the predicted complete antibody-antigen complex structure. IgGM effectively predicts structures and designs novel antibodies and nanobodies. This makes it highly applicable in a wide range of practical situations related to antibody and nanobody design. Code is available at: https://github.com/TencentAI4S/IgGM.

## item_id: m_2876

TITLE: Stable Rank Normalization for Improved Generalization in Neural Networks and GANs

ABSTRACT: Exciting new work on generalization bounds for neural networks (NN) given by Bartlett et al. (2017); Neyshabur et al. (2018) closely depend on two parameter- dependant quantities: the Lipschitz constant upper bound and the stable rank (a softer version of rank). Even though these bounds typically have minimal practical utility, they facilitate questions on whether controlling such quantities together could improve the generalization behaviour of NNs in practice. To this end, we propose stable rank normalization (SRN), a novel, provably optimal, and computationally efficient weight-normalization scheme which minimizes the stable rank of a linear operator. Surprisingly we find that SRN, despite being non-convex, can be shown to have a unique optimal solution. We provide extensive analyses across a wide variety of NNs (DenseNet, WideResNet, ResNet, Alexnet, VGG), where applying SRN to their linear layers leads to improved classification accuracy, while simultaneously showing improvements in genealization, evaluated empirically using—(a) shattering experiments (Zhang et al., 2016); and (b) three measures of sample complexity by Bartlett et al. (2017), Neyshabur et al. (2018), & Wei & Ma. Additionally, we show that, when applied to the discriminator of GANs, it improves Inception, FID, and Neural divergence scores, while learning mappings with low empirical Lipschitz constant.

## item_id: m_2877

TITLE: Private Learning Fast and Slow: Two Algorithms for Prediction with Expert Advice Under Local Differential Privacy

ABSTRACT: We study the classic problem of prediction with expert advice under the constraint of differential privacy (DP). In contrast to earlier work in this area, we are interested in distributed settings with no trusted central curator. In this context, we first show that a classical online learning algorithm naturally satisfies DP and then design two new algorithms that extend and improve it: (1) RW-AdaBatch, which provides a novel form of privacy amplification at negligible utility cost, and (2) RW-Meta, which improves utility on non-adversarial data with zero privacy cost. Our theoretical analysis is supported by an empirical evaluation using real-world data reported by hospitals during the COVID-19 pandemic. RW-Meta outperforms the classical baseline at predicting which hospitals will report a high density of COVID-19 cases by a factor of more than 2$\times$ at realistic privacy levels.

## item_id: m_2878

TITLE: Task-Agnostic Graph Neural Explanations

ABSTRACT: Graph Neural Networks (GNNs) have emerged as powerful tools to encode graph structured data. Due to their broad applications, there is an increasing need to develop tools to explain how GNNs make decisions given graph structured data. Existing learning-based GNN explanation approaches are task-specific in training and hence suffer from crucial drawbacks. Specifically, they are incapable of producing explanations for a multitask prediction model with a single explainer. They are also unable to provide explanations in cases where the GNN is trained in a self-supervised manner, and the resulting representations are used in future down-stream tasks. To address these limitations,  we propose a Task-Agnostic Graph Neural Explainer (TAGE) trained under self-supervision without knowledge about downstream tasks.   TAGE enables the explanation of GNN embedding models without downstream tasks and allows efficient explanation of multitask models. Our extensive experiments show that TAGE can significantly speed up the explanation efficiency while achieving explanation quality as good as or even better than current state-of-the-art GNN explanation approaches.

## item_id: m_2879

TITLE: A Unified Wasserstein Distributional Robustness Framework for Adversarial Training

ABSTRACT: It is well-known that deep neural networks (DNNs) are susceptible to adversarial attacks, exposing a severe fragility of deep learning systems. As the result, adversarial training (AT) method, by incorporating adversarial examples during training, represents a natural and effective approach to strengthen the robustness of a DNN-based classifier. However, most AT-based methods, notably PGD-AT and TRADES, typically seek a pointwise adversary that generates the worst-case adversarial example by independently perturbing each data sample, as a way to ``probe'' the vulnerability of the classifier. Arguably, there are unexplored benefits in considering such adversarial effects from an entire distribution. To this end, this paper presents a unified framework that connects Wasserstein distributional robustness with current state-of-the-art AT methods. We introduce a new Wasserstein cost function and a new series of risk functions, with which we show that standard AT methods are special cases of their counterparts in our framework. This connection leads to an intuitive relaxation and generalization of existing AT methods and facilitates the development of a new family of distributional robustness AT-based algorithms. Extensive experiments show that our distributional robustness AT algorithms robustify further their standard AT counterparts in various settings.

## item_id: m_2880

TITLE: On the State of the Art of Evaluation in Neural Language Models

ABSTRACT: Ongoing innovations in recurrent neural network architectures have provided a steady influx of apparently state-of-the-art results on language modelling benchmarks. However, these have been evaluated using differing codebases and limited computational resources, which represent uncontrolled sources of experimental variation. We reevaluate several popular architectures and regularisation methods with large-scale automatic black-box hyperparameter tuning and arrive at the somewhat surprising conclusion that standard LSTM architectures, when properly regularised, outperform more recent models. We establish a new state of the art on the Penn Treebank and Wikitext-2 corpora, as well as strong baselines on the Hutter Prize dataset.


## item_id: m_2881

TITLE: Discrete Autoencoders for Sequence Models

ABSTRACT: Recurrent models for sequences have been recently successful at many tasks, especially for language modeling
and machine translation. Nevertheless, it remains challenging to extract good representations from
these models. For instance, even though language has a clear hierarchical structure going from characters
through words to sentences, it is not apparent in current language models.
We propose to improve the representation in sequence models by
augmenting current approaches with an autoencoder that is forced to compress
the sequence through an intermediate discrete latent space. In order to propagate gradients
though this discrete representation we introduce an improved semantic hashing technique.
We show that this technique performs well on a newly proposed quantitative efficiency measure.
We also analyze latent codes produced by the model showing how they correspond to
words and phrases. Finally, we present an application of the autoencoder-augmented
model to generating diverse translations.

## item_id: m_2882

TITLE: Transport with Support: Data-Conditional Diffusion Bridges

ABSTRACT: The dynamic Schrödinger bridge problem provides an appealing setting for posing optimal transport problems as learning non-linear diffusion processes and enables efficient iterative solvers. Recent works have demonstrated state-of-the-art results (eg, in modelling single-cell embryo RNA sequences or sampling from complex posteriors) but are typically limited to learning bridges with only initial and terminal constraints. Our work extends this paradigm by proposing the Iterative Smoothing Bridge (ISB). We combine learning diffusion models with Bayesian filtering and optimal control, allowing for constrained stochastic processes governed by sparse observations at intermediate stages and terminal constraints. We assess the effectiveness of our method on synthetic and real-world data and show that the ISB generalises well to high-dimensional data, is computationally efficient, and provides accurate estimates of the marginals at intermediate and terminal times. 

## item_id: m_2883

TITLE: DiffraNet: Automatic Classification of Serial Crystallography Diffraction Patterns

ABSTRACT: Serial crystallography is the field of science that studies the structure and properties of crystals via diffraction patterns. In this paper, we introduce a new serial crystallography dataset generated through the use of a simulator; the synthetic images are labeled and they are both scalable and accurate. The resulting synthetic dataset is called DiffraNet, and it is composed of 25,000 512x512 grayscale labeled images. We explore several computer vision approaches for classification on DiffraNet such as standard feature extraction algorithms associated with Random Forests and Support Vector Machines but also an end-to-end CNN topology dubbed DeepFreak tailored to work on this new dataset. All implementations are publicly available and have been fine-tuned using off-the-shelf AutoML optimization tools for a fair comparison. Our best model achieves 98.5% accuracy. We believe that the DiffraNet dataset and its classification methods will have in the long term a positive impact in accelerating discoveries in many disciplines, including chemistry, geology, biology, materials science, metallurgy, and physics.

## item_id: m_2884

TITLE: Measuring Massive Multitask Language Understanding

ABSTRACT: We propose a new test to measure a text model's multitask accuracy. The test covers 57 tasks including elementary mathematics, US history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem solving ability. We find that while most recent models have near random-chance accuracy, the very largest GPT-3 model improves over random chance by almost 20 percentage points on average. However, on every one of the 57 tasks, the best models still need substantial improvements before they can reach expert-level accuracy. Models also have lopsided performance and frequently do not know when they are wrong. Worse, they still have near-random accuracy on some socially important subjects such as morality and law. By comprehensively evaluating the breadth and depth of a model's academic and professional understanding, our test can be used to analyze models across many tasks and to identify important shortcomings.

## item_id: m_2885

TITLE: Riemannian Optimization for Skip-Gram Negative Sampling

ABSTRACT: Skip-Gram Negative Sampling (SGNS) word embedding model, well known by its implementation in "word2vec" software, is usually optimized by stochastic gradient descent. It can be shown that optimizing for SGNS objective can be viewed as an optimization problem of searching for a good matrix with the low-rank constraint. The most standard way to solve this type of problems is to apply Riemannian optimization framework to optimize the SGNS objective over the manifold of required low-rank matrices. In this paper, we propose an algorithm that optimizes SGNS objective using Riemannian optimization and demonstrates its superiority over popular competitors, such as the original method to train SGNS and SVD over SPPMI matrix.

## item_id: m_2886

TITLE: Forced Apart: Discovering Disentangled Representations Without Exhaustive Labels

ABSTRACT: Learning a better representation with neural networks is a challenging problem, which has been tackled from different perspectives in the past few years. In this work, we focus on learning a representation that would be useful in a clustering task. We introduce two novel loss components that substantially improve the quality of produced clusters, are simple to apply to arbitrary models and cost functions, and do not require a complicated training procedure. We perform an extensive set of experiments, supervised and unsupervised, and evaluate the proposed loss components on two most common types of models, Recurrent Neural Networks and Convolutional Neural Networks, showing that the approach we propose consistently improves the quality of KMeans clustering in terms of mutual information scores and outperforms previously proposed methods.

## item_id: m_2887

TITLE: Defining Expertise: Applications to Treatment Effect Estimation

ABSTRACT: Decision-makers are often experts of their domain and take actions based on their domain knowledge. Doctors, for instance, may prescribe treatments by predicting the likely outcome of each available treatment. Actions of an expert thus naturally encode part of their domain knowledge, and can help make inferences within the same domain: Knowing doctors try to prescribe the best treatment for their patients, we can tell treatments prescribed more frequently are likely to be more effective. Yet in machine learning, the fact that most decision-makers are experts is often overlooked, and “expertise” is seldom leveraged as an inductive bias. This is especially true for the literature on treatment effect estimation, where often the only assumption made about actions is that of overlap. In this paper, we argue that expertise—particularly the type of expertise the decision-makers of a domain are likely to have—can be informative in designing and selecting methods for treatment effect estimation. We formally define two types of expertise, predictive and prognostic, and demonstrate empirically that: (i) the prominent type of expertise in a domain significantly influences the performance of different methods in treatment effect estimation, and (ii) it is possible to predict the type of expertise present in a dataset, which can provide a quantitative basis for model selection.

## item_id: m_2888

TITLE: Kernel Graph Convolutional Neural Nets

ABSTRACT: Graph kernels have been successfully applied to many graph classification problems. Typically, a kernel is first designed, and then an SVM classifier is trained based on the features defined implicitly by this kernel. This two-stage approach decouples data representation from learning, which is suboptimal. On the other hand, Convolutional Neural Networks (CNNs) have the capability to learn their own features directly from the raw data during training. Unfortunately, they cannot handle irregular data such as graphs. We address this challenge by using graph kernels to embed meaningful local neighborhoods of the graphs in a continuous vector space. A set of filters is then convolved with these patches, pooled, and the output is then passed to a feedforward network. With limited parameter tuning, our approach outperforms strong baselines on 7 out of 10 benchmark datasets, and reaches comparable performance elsewhere. Code and data are publicly available.

## item_id: m_2889

TITLE: Understanding Self-supervised Learning with Dual Deep Networks

ABSTRACT: We propose a novel theoretical framework to understand self-supervised learning methods that employ dual pairs of deep ReLU networks (e.g., SimCLR, BYOL). First, we prove that in each SGD update of SimCLR, the weights at each layer are updated by a \emph{covariance operator} that specifically amplifies initial random selectivities that vary across data samples but survive averages over data augmentations. We show this leads to the emergence of hierarchical features, if the input data are generated from a hierarchical latent tree model. With the same framework, we also show analytically that in BYOL, the combination of BatchNorm and a predictor network creates an implicit contrastive term, acting as an approximate covariance operator. Additionally, for linear architectures we derive exact solutions for BYOL that provide conceptual insights into how BYOL can learn useful non-collapsed representations without any contrastive terms that separate negative pairs.  Extensive ablation studies justify our theoretical findings. 

## item_id: m_2890

TITLE: Machine Solver for Physics Word Problems

ABSTRACT: We build a machine solver for word problems on the physics of a free
falling object under constant acceleration of gravity.  Each problem
consists of a formulation part, describing the setting, and a question
part asking for the value of an unknown.  Our solver consists of
two long short-term memory recurrent neural networks and a numerical
integrator. The first neural network (the labeler) labels each
word of the problem, identifying the physical parameters and the
question part of the problem. The second neural network (the 
classifier) identifies what is being asked in the question. Using
the information extracted by both networks, the numerical integrator
computes the solution.  We observe that the classifier is resilient
to errors made by the labeler, which does a better job of identifying
the physics parameters than the question. Training, validation and test
sets of problems are generated from a grammar, with validation and test
problems structurally different from the training problems. The overall
accuracy of the solver on the test cases is 99.8%.

## item_id: m_2891

TITLE: A Simple yet Effective $\Delta\Delta G$ Predictor is An Unsupervised Antibody Optimizer and Explainer

ABSTRACT: The proteins that exist today have been optimized over billions of years of natural evolution, during which nature creates random mutations and selects them. The discovery of functionally promising mutations is challenged by the limited evolutionary accessible regions, i.e., only a small region on the fitness landscape is beneficial. There have been numerous priors used to constrain protein evolution to regions of landscapes with high-fitness variants, among which the change in binding free energy ($\Delta\Delta G$) of protein complexes upon mutations is one of the most commonly used priors. However, the huge mutation space poses two challenges: (1) how to improve the efficiency of $\Delta\Delta G$ prediction for fast mutation screening; and (2) how to explain mutation preferences and efficiently explore accessible evolutionary regions. To address these challenges, we propose a lightweight $\Delta\Delta G$ predictor (Light-DDG), which adopts a structure-aware Transformer as the backbone and enhances it by knowledge distilled from existing powerful but computationally heavy $\Delta\Delta G$ predictors. Additionally, we augmented, annotated, and released a large-scale dataset containing millions of mutation data for pre-training Light-DDG. We find that such a simple yet effective Light-DDG can serve as a good unsupervised antibody optimizer and explainer. For the target antibody, we propose a novel Mutation Explainer to learn mutation preferences, which accounts for the marginal benefit of each mutation per residue. To further explore accessible evolutionary regions, we conduct preference-guided antibody optimization and evaluate antibody candidates quickly using Light-DDG to identify desirable mutations. Extensive experiments have demonstrated the effectiveness of Light-DDG in terms of test generalizability, noise robustness, and inference practicality, e.g., 89.7$\times$ inference acceleration and 15.45\% performance gains over previous state-of-the-art baselines. A case study of SARS-CoV-2 further demonstrates the crucial role of Light-DDG for mutation explanation and antibody optimization.

## item_id: m_2892

TITLE: Learning from Demonstration with Weakly Supervised Disentanglement

ABSTRACT: Robotic manipulation tasks, such as wiping with a soft sponge, require control from multiple rich sensory modalities. Human-robot interaction, aimed at teach- ing robots, is difficult in this setting as there is potential for mismatch between human and machine comprehension of the rich data streams. We treat the task of interpretable learning from demonstration as an optimisation problem over a probabilistic generative model. To account for the high-dimensionality of the data, a high-capacity neural network is chosen to represent the model. The latent variables in this model are explicitly aligned with high-level notions and concepts that are manifested in a set of demonstrations. We show that such alignment is best achieved through the use of labels from the end user, in an appropriately restricted vocabulary, in contrast to the conventional approach of the designer picking a prior over the latent variables. Our approach is evaluated in the context of two table-top robot manipulation tasks performed by a PR2 robot – that of dabbing liquids with a sponge (forcefully pressing a sponge and moving it along a surface) and pouring between different containers. The robot provides visual information, arm joint positions and arm joint efforts. We have made videos of the tasks and data available - see supplementary materials at: https://sites.google.com/view/weak-label-lfd.

## item_id: m_2893

TITLE: Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings

ABSTRACT: Spiking Neural Networks (SNNs) are a promising research direction for building power-efficient information processing systems, especially for temporal tasks such as speech recognition. In SNNs, delays refer to the time needed for one spike to travel from one neuron to another. These delays matter because they influence the spike arrival times, and it is well-known that spiking neurons respond more strongly to coincident input spikes. More formally, it has been shown theoretically that plastic delays greatly increase the expressivity in SNNs. Yet, efficient algorithms to learn these delays have been lacking. Here, we propose a new discrete-time algorithm that addresses this issue in deep feedforward SNNs using backpropagation, in an offline manner. To simulate delays between consecutive layers, we use 1D convolutions across time. The kernels contain only a few non-zero weights – one per synapse – whose positions correspond to the delays. These positions are learned together with the weights using the recently proposed Dilated Convolution with Learnable Spacings (DCLS). We evaluated our method on three datasets: the Spiking Heidelberg Dataset (SHD), the Spiking Speech Commands (SSC) and its non spiking version Google Speech Commands v0.02 (GSC) benchmarks, which require detecting temporal patterns. We used feedforward SNNs with two or three hidden fully connected layers, and vanilla leaky integrate-and-fire neurons. We showed that fixed random delays help and that learning them helps even more. Furthermore, our method outperformed the state-of-the-art in the three datasets without using recurrent connections and with substantially fewer parameters. Our work demonstrates the potential of delay learning in developing accurate and precise models for temporal data processing. Our code is based on PyTorch / SpikingJelly and available at: https://github.com/Thvnvtos/SNN-delays

## item_id: m_2894

TITLE: ThreadsGAN: Enhancing Coherence and Diversity in Discussion Thread Generation

ABSTRACT: Current research on generating discussion threads faces challenges in coherence, interactivity, and multi-topic handling, which are crucial for meaningful responses. This paper introduces threadsGAN, a model that enhances thread generation by incorporating multi-topic and social response intention tags. By leveraging BERT and Transformer, threadsGAN ensures contextual coherence and manages topic consistency. Additionally, it employs conditional generation to align responses with specific discussion contexts, and its CNN-based discriminator assesses response quality by evaluating similarity between generated and real responses, improving overall performance in generating realistic and contextually appropriate discussion threads.

## item_id: m_2895

TITLE: Taking Apart Autoencoders: How do They Encode Geometric Shapes ?

ABSTRACT: We study the precise mechanisms which allow autoencoders to encode and decode a simple geometric shape, the disk. In this carefully controlled setting, we are able to describe the specific form of the optimal solution to the minimisation problem of the training step. We show that the autoencoder indeed approximates this solution during training. Secondly, we identify a clear failure in the generalisation capacity of the autoencoder, namely its inability to interpolate data. Finally, we explore several regularisation schemes to resolve the generalisation problem. Given the great attention that has been recently given to the generative capacity of neural networks, we believe that studying in depth simple geometric cases sheds some light on the generation process and can provide a minimal requirement experimental setup for more complex architectures. 


## item_id: m_2896

TITLE: Learning Dynamical Systems with Helmholtz-Hodge Decomposition and Gaussian Processes

ABSTRACT: Machine learning models provide alternatives for efficiently recognizing complex patterns from data, but two main concerns in applying them to modeling physical systems stem from their physics-agnostic design and lack of interpretability. This paper mitigates these concerns by encoding the Helmholtz-Hodge decomposition into a Gaussian process model, leading to a versatile framework that simultaneously learns the curl-free and divergence-free components of a dynamical system. Learning a predictive model in this form facilitates the exploitation of symmetry priors. In addition to improving predictive power, these priors link the identified features to comprehensible scientific properties of the system, thus complex responses can be modeled while retaining interpretability. We show that compared to baseline models, our model achieves better predictive performance on several benchmark dynamical systems while allowing accurate estimation of the energy evolution of the systems from noisy and sparse data.

## item_id: m_2897

TITLE: Three Mechanisms of Weight Decay Regularization

ABSTRACT: Weight decay is one of the standard tricks in the neural network toolbox, but the reasons for its regularization effect are poorly understood, and recent results have cast doubt on the traditional interpretation in terms of $L_2$ regularization.
Literal weight decay has been shown to outperform $L_2$ regularization for optimizers for which they differ. 
We empirically investigate weight decay for three optimization algorithms (SGD, Adam, and K-FAC) and a variety of network architectures. We identify three distinct mechanisms by which weight decay exerts a regularization effect, depending on the particular optimization algorithm and architecture: (1) increasing the effective learning rate, (2) approximately regularizing the input-output Jacobian norm, and (3) reducing the effective damping coefficient for second-order optimization. 
Our results provide insight into how to improve the regularization of neural networks.

## item_id: m_2898

TITLE: SliceGPT: Compress Large Language Models by Deleting Rows and Columns

ABSTRACT: Large language models have become the cornerstone of natural language processing, but their use comes with substantial costs in terms of compute and memory resources. Sparsification provides a solution to alleviate these resource constraints, and recent works have shown that trained models can be sparsified post-hoc. Existing sparsification techniques face challenges as they need additional data structures and offer constrained speedup with current hardware. In this paper we present SliceGPT, a new post-training sparsification scheme which replaces each weight matrix with a smaller (dense) matrix, reducing the embedding dimension of the network. Through extensive experimentation we show that SliceGPT can remove up to 25% of the model parameters (including embeddings) for LLAMA-2 70B, OPT 66B and Phi-2 models while maintaining 99%, 99% and 90% zero-shot task performance of the dense model respectively. Our sliced models run on fewer GPUs and run faster without any additional code optimization: on 24GB consumer GPUs we reduce the total compute for inference on LLAMA-2 70B to 64% of that of the dense model; on 40GB A100 GPUs we reduce it to 66%. We offer a new insight, computational invariance in transformer networks, which enables SliceGPT and we hope it will inspire and enable future avenues to reduce memory and computation demands for pre-trained models.

## item_id: m_2899

TITLE: ETSformer: Exponential Smoothing Transformers for Time-series Forecasting

ABSTRACT: Transformers have recently been actively studied for time-series forecasting. While often showing promising results in various scenarios, traditional Transformers are not designed to fully exploit the characteristics of time-series data and thus suffer some fundamental limitations, e.g., they are generally not decomposable or interpretable, and are neither effective nor efficient for long-term forecasting. In this paper, we propose ETSformer, a novel time-series Transformer architecture, which exploits the principle of exponential smoothing methods in improving Transformers for time-series forecasting. Specifically, ETSformer leverages a novel level-growth-seasonality decomposed Transformer architecture which leads to more interpretable and disentangled decomposed forecasts. We further propose two novel attention mechanisms -- the exponential smoothing attention and frequency attention, which are specially designed to overcome the limitations of the vanilla attention mechanism for time-series data. Extensive experiments on various time-series benchmarks validate the efficacy and advantages of the proposed method. Code is attached in the supplementary material, and will be made publicly available.  

## item_id: m_2900

TITLE: HGMD: Rethinking Hard Sample Distillation for GNN-to-MLP Knowledge Distillation

ABSTRACT: To bridge the gaps between powerful Graph Neural Networks (GNNs) and lightweight Multi-Layer Perceptron (MLPs), GNN-to-MLP Knowledge Distillation (KD) proposes to distill knowledge from a well-trained teacher GNN into a student MLP. A counter-intuitive observation is that ``better teacher, better student" does not always hold true for GNN-to-MLP KD, which inspires us to explore what are the criteria for better GNN knowledge samples (nodes). In this paper, we revisit the knowledge samples in teacher GNNs from the perspective of hardness rather than correctness, and identify that hard sample distillation may be a major performance bottleneck of existing KD algorithms. The GNN-to-MLP KD involves two different types of hardness, one student-free knowledge hardness describing the inherent complexity of GNN knowledge, and the other student-dependent distillation hardness describing the difficulty of teacher-to-student distillation. In this paper, we propose a novel Hardness-aware GNN-to-MLP Distillation (HGMD) framework, which models both knowledge and distillation hardness and then extracts a hardness-aware subgraph for each sample separately, where a harder sample will be assigned a larger subgraph. Finally, two hardness-aware distillation schemes (i.e., HGMD-weight and HGMD-mixup) are devised to distill subgraph-level knowledge from teacher GNNs into the corresponding nodes of student MLPs. As non-parametric distillation, HGMD does not involve any additional learnable parameters beyond the student MLPs, but it still outperforms most of the state-of-the-art competitors. For example, HGMD-mixup improves over the vanilla MLPs by 12.95% and outperforms its teacher GNNs by 2.48% averaged over seven real-world datasets and three GNN architectures.
