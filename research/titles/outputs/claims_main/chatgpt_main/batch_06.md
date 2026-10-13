# Batch 06 — 100 items

## item_id: m_0501

TITLE: Depth-Adaptive Transformer

ABSTRACT: State of the art sequence-to-sequence models for large scale tasks perform a fixed number of computations for each input sequence regardless of whether it is easy or hard to process. In this paper, we train Transformer models which can make output predictions at different stages of the network and we investigate different ways to predict how much computation is required for a particular sequence. Unlike dynamic computation in Universal Transformers, which applies the same set of layers iteratively, we apply different layers at every step to adjust both the amount of computation as well as the model capacity. On IWSLT German-English translation our approach matches the accuracy of a well tuned baseline Transformer while using less than a quarter of the decoder layers.

## item_id: m_0502

TITLE: Geom-Erasing: Geometry-Driven Removal of Implicit Concept in Diffusion Models

ABSTRACT: Fine-tuning diffusion models through personalized datasets is an acknowledged method for improving generation quality across downstream tasks, which, however, often inadvertently generates unintended concepts such as watermarks and QR codes, attributed to the limitations in image sources and collecting methods within specific downstream tasks. Existing solutions suffer from eliminating these unintentionally learned implicit concepts, primarily due to the dependency on the model’s ability to recognize concepts that it actually cannot discern. In this work, we introduce GEOM-ERASING, a novel approach that successfully removes the implicit concepts with either an additional accessible classifier or detector model to encode geometric information of these concepts into the text domain. Moreover, we construct three distinct datasets, each imbued with specific implicit concepts (i.e., watermarks, QR codes, and text) for training and evaluation. Experimental results demonstrate that GEOM-ERASING not only identifies but also proficiently eradicates specific implicit concepts, revealing a significant improvement over the existing methods. The integration of geometric information marks a substantial progression in the precise removal of implicit concepts in diffusion models.

## item_id: m_0503

TITLE: BERT Wears GloVes: Distilling Static Embeddings from Pretrained Contextual Representations

ABSTRACT: Contextualized word representations such as ELMo and BERT have become the de facto starting point for incorporating pretrained representations for downstream NLP tasks. In these settings, contextual representations have largely made obsolete their static embedding predecessors such as Word2Vec and GloVe. However, static embeddings do have their advantages in that they are straightforward to understand and faster to use. Additionally, embedding analysis methods for static embeddings are far more diverse and mature than those available for their dynamic counterparts. In this work, we introduce simple methods for generating static lookup table embeddings from existing pretrained contextual representations and demonstrate they outperform Word2Vec and GloVe embeddings on a variety of word similarity and word relatedness tasks. In doing so, our results also reveal insights that may be useful for subsequent downstream tasks using our embeddings or the original contextual models. Further, we demonstrate the increased potential for analysis by applying existing approaches for estimating social bias in word embeddings. Our analysis constitutes the most comprehensive study of social bias in contextual word representations (via the proxy of our distilled embeddings) and reveals a number of inconsistencies in current techniques for quantifying social bias in word embeddings. We publicly release our code and distilled word embeddings to support reproducible research and the broader NLP community. 

## item_id: m_0504

TITLE: Resizable Neural Networks

ABSTRACT: 
In this paper, we present a deep convolutional neural network (CNN) which performs arbitrary resize operation on intermediate feature map resolution at stage-level. Motivated by weight sharing mechanism in neural architecture search, where a super-network is trained and sub-networks inherit the weights from the super-network, we present a novel CNN approach. We construct a spatial super-network which consists of multiple sub-networks, where each sub-network is a single scale network that obtain a unique spatial configuration, the convolutional layers are shared across all sub-networks. Such network, named as Resizable Neural Networks, are equivalent to training infinite single scale networks, but has no extra computational cost. Moreover, we present a training algorithm such that all sub-networks achieve better performance than individually trained counterparts. On large-scale ImageNet classification, we demonstrate its effectiveness on various modern network architectures such as MobileNet, ShuffleNet, and ResNet.


To go even further, we present three variants of resizable networks: 1) Resizable as Architecture Search (Resizable-NAS). On ImageNet, Resizable-NAS ResNet-50 attain 0.4% higher on accuracy and 44% smaller than the baseline model. 2) Resizable as Data Augmentation (Resizable-Aug). While we use resizable networks as a data augmentation technique, it obtains superior performance on ImageNet classification, outperform AutoAugment by 1.2% with ResNet-50. 3) Adaptive Resizable Network (Resizable-Adapt). We introduce the adaptive resizable networks as dynamic networks, which further improve the performance with less computational cost via data-dependent inference.

## item_id: m_0505

TITLE: Treating Neural Image Compression via Modular Adversarial Optimization: From Global Distortion to Local Artifacts

ABSTRACT: The rapid progress in neural image compression (NIC) led to the deployment of advanced codecs, such as JPEG AI, which significantly outperform conventional approaches. However, despite extensive research on the adversarial robustness of neural networks in various computer vision tasks, the vulnerability of NIC models to adversarial attacks remains underexplored. Moreover, the existing adversarial attacks on NIC are ineffective against modern codecs. In this paper, we introduce a novel adversarial attack targeting NIC models. Our approach is built upon two core stages: (1) optimization of global-local distortions, and (2) a selective masking strategy that enhances attack stealthiness. Experimental evaluations demonstrate that the proposed method outperforms prior attacks on both JPEG AI and other NIC models, achieving greater distortion on decoded images and lower perceptibility of adversarial images. We also provide a theoretical analysis and discuss the underlying reasons for the effectiveness of our attack, offering new insights into the security and robustness of learned image compression.

## item_id: m_0506

TITLE: Identifying and Controlling Important Neurons in Neural Machine Translation

ABSTRACT: Neural machine translation (NMT) models learn representations containing substantial linguistic information. However, it is not clear if such information is fully distributed or if some of it can be attributed to individual neurons. We develop unsupervised methods for discovering important neurons in NMT models. Our methods rely on the intuition that different models learn similar properties, and do not require any costly external supervision. We show experimentally that translation quality depends on the discovered neurons, and find that many of them capture common linguistic phenomena. Finally, we show how to control NMT translations in predictable ways, by modifying activations of individual neurons.

## item_id: m_0507

TITLE: Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding

ABSTRACT: The current large auto-regressive models can generate high-quality, high-resolution images, but these models require hundreds or even thousands of steps of next-token prediction during inference, resulting in substantial time consumption. In existing studies, Jacobi decoding, an iterative parallel decoding algorithm, has been used to accelerate the auto-regressive generation and can be executed without training. However, the Jacobi decoding relies on a deterministic criterion to determine the convergence of iterations. Thus, it works for greedy decoding but is incompatible with sampling-based decoding which is crucial for visual quality and diversity in the current auto-regressive text-to-image generation. In this paper, we propose a training-free probabilistic parallel decoding algorithm, Speculative Jacobi Decoding (SJD), to accelerate auto-regressive text-to-image generation. By introducing a probabilistic convergence criterion, our SJD accelerates the inference of auto-regressive text-to-image generation while maintaining the randomness in sampling-based token decoding and allowing the model to generate diverse images. Specifically, SJD facilitates the model to predict multiple tokens at each step and accepts tokens based on the probabilistic criterion, enabling the model to generate images with fewer steps than the conventional next-token-prediction paradigm. We also investigate the token initialization strategies that leverage the spatial locality of visual data to further improve the acceleration ratio under specific scenarios. We conduct experiments for our proposed SJD on multiple auto-regressive text-to-image generation models, showing the effectiveness of model acceleration without sacrificing the visual quality. The code of our work is available here: https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD/.

## item_id: m_0508

TITLE: Cortical-Inspired Open-Bigram Representation for Handwritten Word Recognition

ABSTRACT: Recent research in the cognitive process of reading hypothesized that we do
not read words by sequentially recognizing letters, but rather by identifing
open-bigrams, i.e. couple of letters that are not necessarily next
to each other. 
In this paper, we evaluate an handwritten word recognition method based on original
open-bigrams representation. We trained Long Short-Term Memory Recurrent Neural Networks
(LSTM-RNNs) to predict open-bigrams rather than characters, and we show that
such models are able to learn the long-range, complicated and intertwined dependencies
in the input signal, necessary to the prediction. 
For decoding, we decomposed each word of a large vocabulary into the set of
constituent bigrams, and apply a simple cosine similarity measure between this 
representation and the bagged RNN prediction to retrieve the vocabulary word. 
We compare this method to standard word recognition techniques based on 
sequential character recognition.
Experiments are carried out on two public databases of handwritten words
(Rimes and IAM), an the results with our bigram decoder are comparable 
to more conventional decoding methods based on sequences of letters.

## item_id: m_0509

TITLE: RPGAN: random paths as a latent space for GAN interpretability

ABSTRACT: In this paper, we introduce Random Path Generative Adversarial Network (RPGAN) --- an alternative scheme of GANs that can serve as a tool for generative model analysis. While the latent space of a typical GAN consists of input vectors, randomly sampled from the standard Gaussian distribution, the latent space of RPGAN consists of random paths in a generator network. As we show, this design allows to associate different layers of the generator with different regions of the latent space, providing their natural interpretability. With experiments on standard benchmarks, we demonstrate that RPGAN reveals several interesting insights about roles that different layers play in the image generation process. Aside from interpretability, the RPGAN model also provides competitive generation quality and allows efficient incremental learning on new data.

## item_id: m_0510

TITLE: Shaping latent representations using Self-Organizing Maps with Relevance Learning

ABSTRACT: Recent work indicates that Deep Clustering (DC) methods are a viable option for unsupervised representations learning of visual features. By combining representation learning and clustering, traditional approaches have been shown to build latent representations that capture essential features of the data while preserving topological characteristics. In this sense, models based on Self-Organizing Maps models with relevance learning (SOMRL) were considered as they perform well in clustering besides being able to create a map that learns the relevance of each input dimension for each cluster, preserving the original relations and topology of the data. We hypothesize that this type of model can produce a more intuitive and disentangled representation in the latent space by promoting smoother transitions between cluster points over time. This work proposes a representation learning framework that combines a new gradient-based SOMRL model and autoencoders. The SOMRL learns the relevance weights for each input dimension of each cluster. It creates a tendency to separate the information into subspaces. To achieve this, we designed a new loss function term that weighs these learned relevances and provides an estimated unsupervised error to be used in combination with a reconstruction loss. The model is evaluated in terms of clustering performance and quality of the learned representations and then compared with start-of-the-art models, showing competitive results.

## item_id: m_0511

TITLE: A comparison of second-order methods for deep convolutional neural networks

ABSTRACT: Despite many second-order methods have been proposed to train neural networks, most of the results were done on smaller single layer fully connected networks, so we still cannot conclude whether it's useful in training deep convolutional networks. In this study, we conduct extensive experiments to answer the question "whether second-order method is useful for deep learning?". In our analysis, we find out although currently second-order methods are too slow to be applied in practice, it can reduce training loss in fewer number of iterations compared with SGD. In addition, we have the following interesting findings: (1) When using a large batch size, inexact-Newton methods will converge much faster than SGD. Therefore inexact-Newton method could be a better choice in distributed training of deep networks. (2) Quasi-newton methods are competitive with SGD even when using ReLu activation function (which has no curvature) on residual networks. However, current methods are too sensitive to parameters and not easy to tune for different settings. Therefore, quasi-newton methods with more self-adjusting mechanisms might be more useful than SGD in training deeper networks. 


## item_id: m_0512

TITLE: scFormer: a universal representation learning approach for single-cell data using transformers

ABSTRACT: Single-cell sequencing has emerged as a promising technique to decode cellular heterogeneity and analyze gene functions. With the high throughput of modern techniques and resulting large-scale sequencing data, deep learning has been used extensively to learn representations of individual cells for downstream tasks. However, most existing methods rely on fully connected networks and are unable to model complex relationships between both cell and gene representations. We hereby propose scFormer, a novel transformer-based deep learning framework to jointly optimize cell and gene embeddings for single-cell biology in an unsupervised manner. By drawing parallels between natural language processing and genomics, scFormer applies self-attention to learn salient gene and cell embeddings through masked gene modelling. scFormer provides a unified framework to readily address a variety of downstream tasks such as data integration, analysis of gene function, and perturbation response prediction. Extensive experiments using scFormer show state-of-the-art performance on seven datasets across the relevant tasks. The scFormer model implementation is available at https://anonymous.4open.science/r/scFormer-E7E4/

## item_id: m_0513

TITLE: 3D-CoS: A New 3D Reconstruction Paradigm Based on VLM Code Synthesis

ABSTRACT: Most recent 3D reconstruction and editing systems operate on implicit and explicit representations such as NeRF, point clouds, or meshes. While these representations enable high-fidelity rendering, they are inherently low-level and hard to control automatically.
In contrast, we advocate a new \bfunderline{3D} reconstruction paradigm based on vision-language models (VLMs) \bfunderline{Co}de \bfunderline{S}ynthesis (\bfunderline{3D-CoS}), where 3D assets are constructed as executable Blender code, a programmatic and interpretable medium.
To assess how well current VLMs can use code to represent 3D objects, we evaluate leading open-source and closed-source VLMs in code-based reconstruction under a unified protocol. We further introduce advanced prompting strategies including a planning stage that produces a ratio-based, part-level blueprint before code synthesis, Retrieval-Augmented Generation (RAG) over well-organized Blender API documents, and in-context learning with geometric demonstrations.
To demonstrate the unique advantages of this representation, we also present an evaluation focused on localized, text-driven modifications, comparing our code-based edits to state-of-the-art mesh-editing methods. 
Our study shows that code as a 3D representation offers strong controllability and locality, exhibiting significant advantages in edit fidelity, identity preservation, and overall visual quality.
Our work also analyzes the potential of this paradigm and specifically delineates the current capability frontier of VLMs for programmatic 3D modeling, demonstrating the promising future of reconstruction by code.

## item_id: m_0514

TITLE: Non-Visible Light Data Synthesis: A Case Study for Synthetic Aperture Radar Imagery

ABSTRACT: Large-scale pre-trained image generation models such as Stable Diffusion and Imagen have achieved a nearly perfect synthesis of regular images. We explore their “hidden” application in non-visible light domains, taking Synthetic Aperture Radar (SAR) data for a case study. For SAR, due to the inherent challenges in capturing satellite data, acquiring ample training samples is problematic. For instance, for a particular category of ship in the open sea, we can collect only a few dozen SAR images which are too limited to derive effective ship recognition models. If pre-trained regular image models can be adapted to generate diverse SAR data, the problem is solved. In preliminary experiments, we found that directly fine-tuning these models with existing SAR data cannot generate meaningful or novel SAR data. The main challenge is the difficulty in capturing the two primary differences between SAR and regular images: structure and modality. To address this, we propose a 2-stage low-rank adaptation method, and we call it 2LoRA. In the first stage, the model is adapted using aerial-view regular image data (whose structure matches SAR), followed by the second stage where the base model from the first stage is further adapted using SAR modality data. Particularly in the second stage, we introduce a novel prototype LoRA (pLoRA), as an improved version of 2LoRA, to resolve the class imbalance problem in the original SAR dataset. For evaluation, we employ the resulting generation model (e.g., ControlNet+pLoRA) to synthesize additional SAR data. This augmentation, when integrated into the training process of SAR recognition models, yields notably improved performance for minor classes.

## item_id: m_0515

TITLE: Unlocking the Power of Representations in Long-term Novelty-based Exploration

ABSTRACT: We introduce Robust Exploration via Clustering-based Online Density Estimation (RECODE), a non-parametric method for novelty-based exploration that estimates visitation counts for clusters of states based on their similarity in a chosen embedding space. By adapting classical clustering to the nonstationary setting of Deep RL, RECODE can efficiently track state visitation counts over thousands of episodes. We further propose a novel generalization of the inverse dynamics loss, which leverages masked transformer architectures for multi-step prediction; which in conjunction with \DETOCS achieves a new state-of-the-art in a suite of challenging 3D-exploration tasks in DM-Hard-8. RECODE also sets new state-of-the-art in hard exploration Atari games, and is the first agent to reach the end screen in "Pitfall!"

## item_id: m_0516

TITLE: Training generative latent models  by variational f-divergence minimization

ABSTRACT: Probabilistic models are often trained by maximum likelihood, which corresponds to minimizing a specific form of f-divergence between the model and data distribution. We derive an upper bound that holds for all f-divergences, showing the intuitive result that the divergence between two joint distributions is at least as great as the divergence between their corresponding marginals. Additionally, the f-divergence is not formally defined when two distributions have different supports. We thus propose a noisy version of f-divergence which is well defined in such situations. We demonstrate how the bound and the new version of f-divergence can be readily used to train complex probabilistic generative models of data and that the fitted model can depend significantly on the particular divergence used.

## item_id: m_0517

TITLE: DCTD: Deep Conditional Target Densities for Accurate Regression

ABSTRACT: While deep learning-based classification is generally addressed using standardized approaches, a wide variety of techniques are employed for regression. In computer vision, one particularly popular such technique is that of confidence-based regression, which entails predicting a confidence value for each input-target pair (x, y). While this approach has demonstrated impressive results, it requires important task-dependent design choices, and the predicted confidences often lack a natural probabilistic meaning. We address these issues by proposing Deep Conditional Target Densities (DCTD), a novel and general regression method with a clear probabilistic interpretation. DCTD models the conditional target density p(y|x) by using a neural network to directly predict the un-normalized density from (x, y). This model of p(y|x) is trained by minimizing the associated negative log-likelihood, approximated using Monte Carlo sampling. We perform comprehensive experiments on four computer vision regression tasks. Our approach outperforms direct regression, as well as other probabilistic and confidence-based methods. Notably, our regression model achieves a 1.9% AP improvement over Faster-RCNN for object detection on the COCO dataset, and sets a new state-of-the-art on visual tracking when applied for bounding box regression.

## item_id: m_0518

TITLE: LLM-Enhanced Rumor Detection via Virtual Node Induced Edge Prediction

ABSTRACT: The proliferation of rumors on social networks poses significant challenges to information credibility and public trust. The dissemination of rumors forms complex networks, yet existing rumor detection methods exhibit several limitations, including a limited capacity to capture complex propagation features. Representing each node solely through its textual embeddings neglects the textual coherence across the entire rumor propagation path, which undermines the accuracy of rumor identification on social platforms. To address these challenges, this study proposes a novel framework for rumor detection on social media, which captures latent characteristics of rumor propagation and enhances contextual correlation within rumor graphs through large language models (LLMs). We introduce a novel paradigm for effectively leveraging LLMs, utilizing their powerful linguistic capabilities to analyze complete information flows within sub-chains, assign rumor probabilities, and guide the construction of connections between virtual nodes and selected sub-chain nodes. This enables the modification of the original graph structure, which is a critical advancement for capturing subtle rumor signals. Given the inherent limitations of LLMs in rumor identification, we develop a structured prompt framework to mitigate model biases and ensure robust graph learning performance. Additionally, the proposed framework is model-agnostic, meaning it is not constrained to any specific graph learning algorithm or LLMs. Its plug-and-play nature allows for seamless integration with further fine-tuned LLMs and graph techniques in the future, potentially enhancing predictive performance without modifying original algorithms.

## item_id: m_0519

TITLE: Stabilizing Gradients for Deep Neural Networks via Efficient SVD Parameterization

ABSTRACT: Vanishing and exploding gradients are two of the main obstacles in training deep neural networks, especially in capturing long range dependencies in recurrent neural networks (RNNs). In this paper, we present an efficient parametrization of the transition matrix of an RNN that allows us to stabilize the gradients that arise in its training. Specifically, we parameterize the transition matrix by its singular value decomposition (SVD), which allows us to explicitly track and control its singular values. We attain efficiency by using tools that are common in numerical linear algebra, namely Householder reflectors for representing the orthogonal matrices that arise in the SVD. By explicitly controlling the singular values, our proposed svdRNN method allows us to easily solve the exploding gradient problem and we observe that it empirically solves the vanishing gradient issue to a large extent. We note that the SVD parameterization can be used for any rectangular weight matrix, hence it can be easily extended to any deep neural network, such as a multi-layer perceptron. Theoretically, we demonstrate that our parameterization does not lose any expressive power, and show how it potentially makes the optimization process easier. Our extensive  experimental results also demonstrate that the proposed framework converges faster, and has good generalization, especially when the depth is large. 


## item_id: m_0520

TITLE: Deep Networks and the Multiple Manifold Problem

ABSTRACT: We study the multiple manifold problem, a binary classification task modeled on applications in machine vision, in which a deep fully-connected neural network is trained to separate two low-dimensional submanifolds of the unit sphere. We provide an analysis of the one-dimensional case, proving for a simple manifold configuration that when the network depth $L$ is large relative to certain geometric and statistical properties of the data, the network width $n$ grows as a sufficiently large polynomial in $L$, and the number of i.i.d. samples from the manifolds is polynomial in $L$, randomly-initialized gradient descent rapidly learns to classify the two manifolds perfectly with high probability. Our analysis demonstrates concrete benefits of depth and width in the context of a practically-motivated model problem: the depth acts as a fitting resource, with larger depths corresponding to smoother networks that can more readily separate the class manifolds, and the width acts as a statistical resource, enabling concentration of the randomly-initialized network and its gradients. The argument centers around the "neural tangent kernel" of Jacot et al. and its role in the nonasymptotic analysis of training overparameterized neural networks; to this literature, we contribute essentially optimal rates of concentration for the neural tangent kernel of deep fully-connected ReLU networks, requiring width $n \geq L\,\mathrm{poly}(d_0)$ to achieve uniform concentration of the initial kernel over a $d_0$-dimensional submanifold of the unit sphere $\mathbb{S}^{n_0-1}$, and a nonasymptotic framework for establishing generalization of networks trained in the "NTK regime" with structured data. The proof makes heavy use of martingale concentration to optimally treat statistical dependencies across layers of the initial random network. This approach should be of use in establishing similar results for other network architectures.

## item_id: m_0521

TITLE: Dataset Bias Prediction for Few-Shot Image Classification

ABSTRACT: One of the obstacles which negatively affect the image classification performance is dataset bias. In particular, if each class has only a few training data samples, the data are highly likely to have dataset bias. Therefore, dataset bias can be a serious issue in few-shot learning, but has rarely been studied so far. To address this issue, we propose a bias prediction network to help improve the performance of few-shot image classification models. Once the features are extracted from an image data, the bias prediction network tries to recover the bias of the raw image such as color from the features. However, if the bias prediction network can recover it easily, we can assume that the extracted features also contain the color bias. Therefore, in our proposed framework, the full model tries to extract features that are difficult for the bias prediction network to recover from. We validate our method by adding the bias prediction network to several existing models and evaluating the performance improvement. Our experimental results show that the bias prediction network can suppress the negative effect of the dataset color bias, resulting in the substantial improvements in existing few-shot classification models. The proposed bias prediction network, which can be integrated with other models very easily, could potentially benefit many existing models for various tasks.

## item_id: m_0522

TITLE: Agent²: An Agent-Generates-Agent Framework for Reinforcement Learning Automation

ABSTRACT: Reinforcement learning (RL) agent development traditionally requires substantial expertise and iterative effort, often leading to high failure rates and limited accessibility. This paper introduces Agent$^2$, an LLM-driven agent-generates-agent framework for fully automated RL agent design. Agent$^2$ autonomously translates natural language task descriptions and environment code into executable RL solutions without human intervention. 

The framework adopts a dual-agent architecture: a Generator Agent that analyzes tasks and designs agents, and a Target Agent that is automatically generated and executed. To better support automation, RL development is decomposed into two stages—MDP modeling and algorithmic optimization—facilitating targeted and effective agent generation. Built on the Model Context Protocol, Agent$^2$ provides a unified framework for standardized agent creation across diverse environments and algorithms, incorporating adaptive training management and intelligent feedback analysis for continuous refinement.

Extensive experiments on benchmarks including MuJoCo, MetaDrive, MPE, and SMAC show that Agent$^2$ outperforms manually designed baselines across all tasks, achieving up to 55\% performance improvement with consistent average gains. By enabling a closed-loop, end-to-end automation pipeline, this work advances a new paradigm in which agents can design and optimize other agents, underscoring the potential of agent-generates-agent systems for automated AI development.

## item_id: m_0523

TITLE: Multimodal Fusion with Relational Learning for Molecular Property Prediction

ABSTRACT: Graph-based molecular representation learning is essential for accurately predicting molecular properties in drug discovery and materials science; however, it faces significant challenges due to the intricate relationships among molecules and the limited chemical knowledge utilized during training. While contrastive learning is often employed to handle molecular relationships, its reliance on binary metrics is insufficient for capturing the complexity of these interactions. Multimodal fusion has gained attention for property reasoning, but previous work has explored only a limited range of modalities, and the optimal stages for fusing different modalities in molecular property tasks remain underexplored. In this paper, we introduce MMFRL (Multimodal Fusion with Relational Learning for Molecular Property Prediction), a novel framework designed to overcome these limitations. Our method enhances embedding initialization through multi-modal pre-training using relational learning. We also conduct a systematic investigation into the impact of modality fusion at different stages—early, intermediate, and late—highlighting their advantages and shortcomings. Extensive experiments on MoleculeNet benchmarks demonstrate that MMFRL significantly outperforms existing methods. Furthermore, MMFRL enables task-specific optimizations. Additionally, the explainability of MMFRL provides valuable chemical insights, emphasizing its potential to enhance real-world drug discovery applications.

## item_id: m_0524

TITLE: MURO: Deployment Constrained Reinforcement Learning with Model-based Uncertainty Regularized Batch Optimization

ABSTRACT: In many contemporary applications such as healthcare, finance, robotics, and recommendation systems, continuous deployment of new policies for data collection and online learning is either cost ineffective or impractical. We consider a setting that lies between pure offline reinforcement learning (RL) and pure online RL called deployment constrained RL in which the number of policy deployments for data sampling is limited. To solve this challenging task, we propose a novel algorithmic learning framework called Model-based Uncertainty Regularized batch Optimization (MURO). Our framework discovers novel and high quality samples for each deployment to enable efficient data collection. During each offline training session, we bootstrap the policy update by quantifying the amount of uncertainty within our collected data. In the high support region (low uncertainty), we encourage our policy by taking an aggressive update. In the low support region (high uncertainty) when the policy bootstraps into the out-of-distribution region, we downweight it by our estimated uncertainty quantification. Experimental results show that MURO achieves state-of-the-art performance in the deployment constrained RL setting.

## item_id: m_0525

TITLE: VL-JEPA: Joint Embedding Predictive Architecture for Vision-language

ABSTRACT: We introduce VL-JEPA, a vision-language model built on a Joint Embedding Predictive Architecture (JEPA). Instead of autoregressively generating tokens as in classical VLMs, VL-JEPA predicts continuous embeddings of the target texts. By learning in an abstract representation space, the model focuses on task-relevant semantics while abstracting away surface-level linguistic variability. In a strictly controlled comparison against standard token-space VLM training with the same vision encoder and training data, VL-JEPA achieves stronger performance while having 50% fewer trainable parameters. At inference time, a lightweight text decoder is invoked only when needed to translate VL-JEPA predicted embeddings into text. We show that VL-JEPA natively supports selective decoding that reduces the number of decoding operations by ~2.85× while maintaining similar performance compared to non-adaptive uniform decoding. Beyond generation, VL-JEPA's embedding space naturally supports open-vocabulary classification, text-to-video retrieval, and discriminative VQA without any architecture modification. On eight video classification and eight video retrieval datasets, the average performance of VL-JEPA surpasses that of CLIP, SigLIP2, and Perception Encoder. At the same time, the model achieves comparable performance to classical VLMs (InstructBLIP, QwenVL) on four VQA datasets—GQA, TallyQA, POPE, and POPEv2—despite having only 1.6B parameters.

## item_id: m_0526

TITLE: Model Selection of Anomaly Detectors in the Absence of Labeled Validation Data

ABSTRACT: Anomaly detection requires detecting abnormal samples in large unlabeled datasets. While progress in deep learning and the advent of foundation models has produced powerful unsupervised anomaly detection methods, their deployment in practice is often hindered by the lack of labeled data---without it, the detection accuracy of an anomaly detector cannot be evaluated reliably.
In this work, we propose a general-purpose framework for evaluating image-based anomaly detectors with synthetically generated validation data. Our method assumes access to a small support set of normal images which are processed with a pre-trained diffusion model (our proposed method requires no training or fine-tuning) to produce synthetic anomalies. When mixed with normal samples from the support set, the synthetic anomalies create detection tasks that compose a validation framework for anomaly detection evaluation and model selection. In an extensive empirical study, ranging from natural images to industrial applications, we find that our synthetic validation framework selects the same models and hyper-parameters as selection with a ground-truth validation set. 
In addition, we find that prompts selected by our method for CLIP-based anomaly detection outperforms all other prompt selection strategies, and leads to the overall best detection accuracy, even on the challenging MVTec-AD dataset.

## item_id: m_0527

TITLE: Pea-KD: Parameter-efficient and accurate Knowledge Distillation

ABSTRACT: How can we efficiently compress a model while maintaining its performance?  Knowledge Distillation (KD) is one of the widely known methods for model compression. In essence, KD trains a smaller student model based on a larger teacher model and tries to retain the teacher model's level of performance as much as possible. However, the existing KD methods suffer from the following limitations. First, since the student model is small in absolute size, it inherently lacks model complexity. Second, the absence of an initial guide for the student model makes it difficult for the student to imitate the teacher model to its fullest. Conventional KD methods yield low performance due to these limitations.

In this paper, we propose Pea-KD (Parameter-efficient and accurate Knowledge Distillation), a novel approach to KD. Pea-KD consists of two main parts: Shuffled Parameter Sharing (SPS) and Pretraining with Teacher's Predictions (PTP). Using this combination, we are capable of alleviating the KD's limitations. SPS is a new parameter sharing method that allows greater model complexity for the student model. PTP is a KD-specialized initialization method, which can act as a good initial guide for the student. When combined, this method yields a significant increase in student model's performance. Experiments conducted on different datasets and tasks show that the proposed approach improves the student model's performance by 4.4% on average in four GLUE tasks, outperforming existing KD baselines by significant margins.


## item_id: m_0528

TITLE: Discovering Diverse Multi-Agent Strategic Behavior via Reward Randomization

ABSTRACT: We propose a simple, general and effective technique, Reward Randomization for discovering diverse strategic policies in complex multi-agent games. Combining reward randomization and policy gradient, we derive a new algorithm, Reward-Randomized Policy Gradient (RPG). RPG is able to discover a set of multiple distinctive human-interpretable strategies in challenging temporal trust dilemmas, including grid-world games and a real-world game Agar.io, where multiple equilibria exist but standard multi-agent policy gradient algorithms always converge to a fixed one with a sub-optimal payoff for every player even using state-of-the-art exploration techniques. Furthermore, with the set of diverse strategies from RPG, we can (1) achieve higher payoffs by fine-tuning the best policy from the set; and (2) obtain an adaptive agent by using this set of strategies as its training opponents. 

## item_id: m_0529

TITLE: Learning to Represent Edits

ABSTRACT: We introduce the problem of learning distributed representations of edits. By combining a
"neural editor" with an "edit encoder", our models learn to represent the salient
information of an edit and can be used to apply edits to new inputs.
We experiment on natural language and source code edit data. Our evaluation yields
promising results that suggest that our neural network models learn to capture
the structure and semantics of edits. We hope that this interesting task and
data source will inspire other researchers to work further on this problem.

## item_id: m_0530

TITLE: Neural Photo Editing with Introspective Adversarial Networks

ABSTRACT: The increasingly photorealistic sample quality of generative image models suggests their feasibility in applications beyond image generation. We present the Neural Photo Editor, an interface that leverages the power of generative neural networks to make large, semantically coherent changes to existing images. To tackle the challenge of achieving accurate reconstructions without loss of feature quality, we introduce the Introspective Adversarial Network,  
a novel hybridization of the VAE and GAN. Our model efficiently captures long-range dependencies through use of a computational block based on weight-shared dilated convolutions, and improves generalization performance with Orthogonal Regularization, a novel weight regularization method. We validate our contributions on CelebA, SVHN, and CIFAR-100, and produce samples and reconstructions with high visual fidelity.

## item_id: m_0531

TITLE: Actor-Critic Policy Optimization in a Large-Scale Imperfect-Information Game

ABSTRACT: The deep policy gradient method has demonstrated promising results in many large-scale games, where the agent learns purely from its own experience. Yet, policy gradient methods with self-play suffer convergence problems to a Nash Equilibrium (NE) in multi-agent situations. Counterfactual regret minimization (CFR) has a convergence guarantee to a NE in 2-player zero-sum games, but it usually needs domain-specific abstractions to deal with large-scale games.  Inheriting merits from both methods, in this paper we extend the actor-critic algorithm framework in deep reinforcement learning to tackle a large-scale 2-player zero-sum imperfect-information game, 1-on-1 Mahjong, whose information set size and game length are much larger than poker. The proposed algorithm, named Actor-Critic Hedge (ACH), modifies the policy optimization objective from originally maximizing the discounted returns to minimizing a type of weighted cumulative counterfactual regret. This modification is achieved by approximating the regret via a deep neural network and minimizing the regret via generating self-play policies using Hedge. ACH is theoretically justified as it is derived from a neural-based weighted CFR, for which we prove the convergence to a NE under certain conditions. Experimental results on the proposed 1-on-1 Mahjong benchmark and benchmarks from the literature demonstrate that ACH outperforms related state-of-the-art methods. Also, the agent obtained by ACH defeats a human champion in 1-on-1 Mahjong.

## item_id: m_0532

TITLE: SpecRaGE: Robust and Generalizable Multi-view Spectral Representation Learning

ABSTRACT: Multi-view representation learning (MvRL) has garnered substantial attention in recent years, driven by the increasing demand for applications that can effectively process and analyze data from multiple sources. In this context, graph Laplacian-based MvRL methods have demonstrated remarkable success in representing multi-view data. However, these methods often struggle with generalization to new data and face challenges with scalability. Moreover, in many practical scenarios, multi-view data is contaminated by noise or outliers. In such cases, modern deep-learning-based MvRL approaches that rely on alignment or contrastive objectives can lead to misleading results, as they may impose incorrect consistency between clear and corrupted data sources. We introduce *SpecRaGE*, a novel fusion-based framework that integrates the strengths of graph Laplacian methods with the power of deep learning to overcome these challenges. SpecRage uses neural networks to learn parametric mapping that approximates a joint diagonalization of graph Laplacians. This solution bypasses the need for alignment while enabling generalizable and scalable learning of informative and meaningful representations. Moreover, it incorporates a meta-learning fusion module that dynamically adapts to data quality, ensuring robustness against outliers and noisy views. Our extensive experiments demonstrate that SpecRaGE outperforms state-of-the-art methods, particularly in scenarios with data contamination, paving the way for more reliable and efficient multi-view learning. Our code will be made publicly available upon acceptance.

## item_id: m_0533

TITLE: Linearizing Visual Processes with Deep Generative Models

ABSTRACT: This work studies the problem of modeling non-linear visual processes by leveraging deep generative architectures for learning linear, Gaussian models of observed sequences. We propose a joint learning framework, combining a multivariate autoregressive model and deep convolutional generative networks. After justification of theoretical assumptions of inearization, we propose an architecture that allows Variational Autoencoders and Generative Adversarial Networks to simultaneously learn the non-linear observation as well as the linear state-transition model from a sequence of observed frames. Finally, we demonstrate our approach on conceptual toy examples and dynamic textures.

## item_id: m_0534

TITLE: You Only Sample Once: Taming One-Step Text-to-Image Synthesis by Self-Cooperative Diffusion GANs

ABSTRACT: Recently, some works have tried to combine diffusion and Generative Adversarial Networks (GANs) to alleviate the computational cost of the iterative denoising inference in Diffusion Models (DMs). 
However, existing works in this line suffer from either training instability and mode collapse or subpar one-step generation learning efficiency. 
To address these issues, we introduce YOSO, a novel generative model designed for rapid, scalable, and high-fidelity one-step image synthesis with high training stability and mode coverage. 
Specifically, we smooth the adversarial divergence by the denoising generator itself, performing self-cooperative learning. We show that our method can serve as a one-step generation model training from scratch with competitive performance. 
Moreover, we extend our YOSO to one-step text-to-image generation based on pre-trained models by several effective training techniques (i.e., latent perceptual loss and latent discriminator for efficient training along with the latent DMs; the informative prior initialization (IPI), and the quick adaption stage for fixing the flawed noise scheduler). Experimental results show that YOSO achieves the state-of-the-art one-step generation performance even with Low-Rank Adaptation (LoRA) fine-tuning.
In particular, we show that the YOSO-PixArt-$\alpha$ can generate images in one step trained on 512 resolution, with the capability of adapting to 1024 resolution without extra explicit training, requiring only \textasciitilde10 A800 days for fine-tuning. Our code is available at:  [https://github.com/Luo-Yihong/YOSO](https://github.com/Luo-Yihong/YOSO)

## item_id: m_0535

TITLE: A Compare-Aggregate Model for Matching Text Sequences

ABSTRACT: Many NLP tasks including machine comprehension, answer selection and text entailment require the comparison between sequences. Matching the important units between sequences is a key to solve these problems. In this paper, we present a general "compare-aggregate" framework that performs word-level matching followed by aggregation using Convolutional Neural Networks. We particularly focus on the different comparison functions we can use to match two vectors. We use four different datasets to evaluate the model. We find that some simple comparison functions based on element-wise operations can work better than standard neural network and neural tensor network. 

## item_id: m_0536

TITLE: Denoising and Regularization via Exploiting the Structural Bias of Convolutional Generators

ABSTRACT: Convolutional Neural Networks (CNNs) have emerged as highly successful tools for image generation, recovery, and restoration. A major contributing factor to this success is that convolutional networks impose strong prior assumptions about natural images. A surprising experiment that highlights this architectural bias towards natural images is that one can remove noise and corruptions from a natural image without using any training data, by simply fitting (via gradient descent) a randomly initialized, over-parameterized convolutional generator to the corrupted image. While this over-parameterized network can fit the corrupted image perfectly, surprisingly after a few iterations of gradient descent it generates an almost uncorrupted image. This intriguing phenomenon enables state-of-the-art CNN-based denoising and regularization of other inverse problems. In this paper, we attribute this effect to a particular architectural choice of convolutional networks, namely convolutions with fixed interpolating filters. We then formally characterize the dynamics of fitting a two-layer convolutional generator to a noisy signal and prove that early-stopped gradient descent denoises/regularizes. Our proof relies on showing that convolutional generators fit the structured part of an image significantly faster than the corrupted portion. 

## item_id: m_0537

TITLE: Predicted Variables in Programming

ABSTRACT: We present Predicted Variables, an approach to making machine learning (ML) a first class citizen in programming languages.
There is a growing divide in approaches to building systems: using human experts (e.g. programming) on the one hand, and using behavior learned from data (e.g. ML) on the other hand. PVars aim to make using ML in programming easier by hybridizing the two. We leverage the existing concept of variables and create a new type, a predicted variable. PVars are akin to native variables with one important distinction: PVars determine their value using ML when evaluated. We describe PVars and their interface, how they can be used in programming, and demonstrate the feasibility of our approach on three algorithmic problems: binary search, QuickSort, and caches.
We show experimentally that PVars are able to improve over the commonly used heuristics and lead to a better performance than the original algorithms.
As opposed to previous work applying ML to algorithmic problems, PVars have the advantage that they can be used within the existing frameworks and do not require the existing domain knowledge to be replaced. PVars allow for a seamless integration of ML into existing systems and algorithms.
Our PVars implementation currently relies on standard Reinforcement Learning (RL) methods. To learn faster, PVars use the heuristic function, which they are replacing, as an initial function. We show that PVars quickly pick up the behavior of the initial function and then improve performance beyond that without ever performing substantially worse -- allowing for a safe deployment in critical applications.

## item_id: m_0538

TITLE: Multi-Domain Adversarial Learning

ABSTRACT: Multi-domain learning (MDL) aims at obtaining a model with minimal average risk across multiple domains. Our empirical motivation is automated microscopy data, where cultured cells are imaged after being exposed to known and unknown chemical perturbations, and each dataset displays significant experimental bias. This paper presents a multi-domain adversarial learning approach, MuLANN, to leverage multiple datasets with overlapping but distinct class sets, in a semi-supervised setting. Our contributions include: i) a bound on the average- and worst-domain risk in MDL, obtained using the H-divergence; ii) a new loss to accommodate semi-supervised multi-domain learning and domain adaptation; iii) the experimental validation of the approach, improving on the state of the art on two standard image benchmarks, and a novel bioimage dataset, Cell.

## item_id: m_0539

TITLE: q-Neurons: Neuron Activations based on Stochastic Jackson's Derivative Operators

ABSTRACT: We propose a new generic type of stochastic neurons, called $q$-neurons, that considers activation functions based on Jackson's $q$-derivatives, with stochastic parameters $q$. Our generalization of neural network architectures with $q$-neurons is shown to be both scalable and very easy to implement. We demonstrate experimentally consistently improved performances over state-of-the-art standard activation functions, both on training and testing loss functions.


## item_id: m_0540

TITLE: Regularizing Predictions via Class-wise Self-knowledge Distillation

ABSTRACT: Deep neural networks with millions of parameters may suffer from poor generalizations due to overfitting. To mitigate the issue, we propose a new regularization method that penalizes the predictive distribution between similar samples. In particular, we distill the predictive distribution between different samples of the same label and augmented samples of the same source during training. In other words, we regularize the dark knowledge (i.e., the knowledge on wrong predictions) of a single network, i.e., a self-knowledge distillation technique, to force it output more meaningful predictions.  We demonstrate the effectiveness of the proposed method  via  experiments  on  various  image  classification  tasks:  it  improves  not only the generalization ability, but also the calibration accuracy of modern neural networks.

## item_id: m_0541

TITLE: Theoretical Analyses of Hyperparameter Selection in Graph-Based Semi-Supervised Learning

ABSTRACT: Graph-based semi-supervised learning is a powerful paradigm in machine learning for modeling and exploiting the underlying graph structure that captures the relationship between labeled and unlabeled data. A large number of classical as well as modern deep learning based algorithms have been proposed for this problem, often having tunable hyperparameters. We initiate a formal study of tuning algorithm hyperparameters from parameterized algorithm families for this problem. We obtain novel $O(\log n)$ pseudo-dimension upper bounds for hyperparameter selection in three classical label propagation-based algorithm families, where $n$ is the number of nodes, implying bounds on the amount of data needed for learning provably good parameters. We further provide matching $\Omega(\log n)$ pseudo-dimension lower bounds, thus asymptotically characterizing the learning-theoretic complexity of the parameter tuning problem. We extend our study to selecting architectural hyperparameters in modern graph neural networks. We bound the Rademacher complexity for tuning the self-loop weighting in recently proposed Simplified Graph Convolution (SGC) networks. We further propose a tunable architecture that interpolates graph convolutional neural networks (GCN) and graph attention networks (GAT) in every layer, and provide Rademacher complexity bounds for tuning the interpolation coefficient.

## item_id: m_0542

TITLE: The Power of Sparsity in Convolutional Neural Networks

ABSTRACT: Deep convolutional networks are well-known for their high computational and memory demands. Given limited resources, how does one design a network that balances its size, training time, and prediction accuracy? A surprisingly effective approach to trade accuracy for size and speed is to simply reduce the number of channels in each convolutional layer by a fixed fraction and retrain the network. In many cases this leads to significantly smaller networks with only minimal changes to accuracy. In this paper, we take a step further by empirically examining a strategy for deactivating connections between filters in convolutional layers in a way that allows us to harvest savings both in run-time and memory for many network architectures. More specifically, we generalize 2D convolution to use a channel-wise sparse connection structure and show that this leads to significantly better results than the baseline approach for large networks including VGG and Inception V3.

## item_id: m_0543

TITLE: Universal Attacks on Equivariant Networks

ABSTRACT: Adversarial attacks on neural networks perturb the input at test time in order to fool trained and deployed neural network models. Most attacks such as gradient-based Fast Gradient Sign Method (FGSM) by Goodfellow et al. 2015 and DeepFool by Moosavi-Dezfooli et al. 2016 are input-dependent, small, pixel-wise perturbations, and they give different attack directions for different inputs. On the other hand, universal adversarial attacks are input-agnostic and the same attack works for most inputs. Translation or rotation-equivariant neural network models provide one approach to prevent universal attacks based on simple geometric transformations. In this paper, we observe an interesting spectral property shared by all of the above input-dependent, pixel-wise adversarial attacks on translation and rotation-equivariant networks. We exploit this property to get a single universal attack direction that fools the model on most inputs. Moreover, we show how to compute this universal attack direction using principal components of the existing input-dependent attacks on a very small sample of test inputs. We complement our empirical results by a theoretical justification, using matrix concentration inequalities and spectral perturbation bounds. We also empirically observe that the top few principal adversarial attack directions are nearly orthogonal to the top few principal invariant directions.


## item_id: m_0544

TITLE: Warped Convolutions: Efficient Invariance to Spatial Transformations

ABSTRACT: Convolutional Neural Networks (CNNs) are extremely efficient, since they exploit the inherent translation-invariance of natural images. However, translation is just one of a myriad of useful spatial transformations. Can the same efficiency be attained when considering other spatial invariances? Such generalized convolutions have been considered in the past, but at a high computational cost. We present a construction that is simple and exact, yet has the same computational complexity that standard convolutions enjoy. It consists of a constant image warp followed by a simple convolution, which are standard blocks in deep learning toolboxes. With a carefully crafted warp, the resulting architecture can be made equivariant to a wide range of 2-parameters spatial transformations. We show encouraging results in realistic scenarios, including the estimation of vehicle poses in the Google Earth dataset (rotation and scale), and face poses in Annotated Facial Landmarks in the Wild (3D rotations under perspective).

## item_id: m_0545

TITLE: Generative Matching Units for Supervised Learning

ABSTRACT: We propose an alternative computational unit for feedforward supervised learning architectures, called Generative Matching Units (GMUs). To understand GMUs, we start with the standard perceptron unit and view it as an undirected symmetric measure of computation between the weights $W=[w_1,w_2,..w_d]$ and each input datapoint $X=[x_1,x_2,..,x_d]$. Perceptrons forward $W^TX+b$, which is usually followed by an activation function. In contrast, GMUs compute a directed asymmetric measure of computation that estimates the degree of functional dependency $f$ of the input elements $x_i$ of each datapoint to the weights $w_i$ in terms of latent generative variables $\theta$, i.e,  $f(w_i,\theta) \rightarrow x_i$.  In order to estimate the functional dependency, GMUs measure the minimum error $\sum (f(w_i,\theta)-x_i)^2$ incurred in the generation process by optimizing $\theta$ for each input datapoint. Subsequently, GMUs map the error into a functional dependency measure via an appropriate scalar function, and forward it to the next layer for further computation. In GMUs, the weights $[w_1,w_2,..,w_d]$ can therefore be interpreted as the $\textit{generative weights}$. We first compare the generalization ability of GMUs and multi-layered-perceptrons (MLPs) via comprehensive synthetic experiments across a range of diverse settings. The most notable finding is that when the input is a sparse linear combination of latent generating variables, GMUs generalize significantly better than MLPs. Subsequently, we evaluate Resnet MLP networks where the first feedforward layer is replaced by GMUs (GMU-MLP) on 30 tabular datasets and find that in most cases, GMU-MLPs generalize better than the MLP baselines. We also compare GMU-MLP to a set of other benchmarks, including TabNet, XGBoost, etc. Lastly, we evaluate GMU-CNNs on three standard vision datasets and find that in all cases they generalize better than the corresponding CNN baselines. We also find that GMU-CNNs are significantly more robust to test-time corruptions.

## item_id: m_0546

TITLE: Dynamic Differential-Privacy Preserving SGD

ABSTRACT: Differentially-Private Stochastic Gradient Descent (DP-SGD) prevents training-data privacy breaches by adding noise to the clipped gradient during SGD training to satisfy the differential privacy (DP) definition. On the other hand, the same clipping operation and additive noise across training steps results in unstable updates and even a ramp-up period,  which significantly reduces the model's accuracy. In this paper, we extend the Gaussian DP central limit theorem to calibrate the clipping value and the noise power for each individual step separately. We, therefore, are able to propose the dynamic DP-SGD, which has a lower privacy cost than the DP-SGD during updates until they achieve the same target privacy budget at a target number of updates.
Dynamic DP-SGD, in particular, improves model accuracy without sacrificing privacy by gradually lowering both clipping value and noise power while adhering to a total privacy budget constraint. Extensive experiments on a variety of deep learning tasks, including image classification, natural language processing, and federated learning, show that the proposed dynamic DP-SGD algorithm stabilizes updates and, as a result, significantly improves model accuracy in the strong privacy protection region when compared to DP-SGD.

## item_id: m_0547

TITLE: GradMix: Multi-source Transfer across Domains and Tasks

ABSTRACT: The machine learning and computer vision community is witnessing an unprecedented rate of new tasks being proposed and addressed, thanks to the power of deep convolutional networks to find complex mappings from X to Y. The advent of each task often accompanies the release of a large-scale human-labeled dataset, for supervised training of the deep network. However, it is expensive and time-consuming to manually label sufficient amount of training data. Therefore, it is important to develop algorithms that can leverage off-the-shelf labeled dataset to learn useful knowledge for the target task. While previous works mostly focus on transfer learning from a single source, we study multi-source transfer across domains and tasks (MS-DTT), in a semi-supervised setting. We propose GradMix, a model-agnostic method applicable to any model trained with gradient-based learning rule. GradMix transfers knowledge via gradient descent, by weighting and mixing the gradients from all sources during training. Our method follows a meta-learning objective, by assigning layer-wise weights to the source gradients, such that the combined gradient follows the direction that can minimize the loss for a small set of samples from the target dataset. In addition, we propose to adaptively adjust the learning rate for each mini-batch based on its importance to the target task, and a pseudo-labeling method to leverage the unlabeled samples in the target domain. We perform experiments on two MS-DTT tasks: digit recognition and action recognition, and demonstrate the advantageous performance of the proposed method against multiple baselines.

## item_id: m_0548

TITLE: Interpolate: How Resetting Active Neurons can also improve Generalizability in Online Learning

ABSTRACT: While neural networks have shown a significant gain in performance across a wide range of applications, they still struggle in non-stationary settings as they tend to lose their ability to adapt to new tasks — a phenomenon known as the loss of plasticity. The conventional approach to addressing this problem often involves resetting the most under-utilized or dormant parts of the network, suggesting that recycling such parameters is crucial for maintaining a model's plasticity. In this study, we explore whether this approach is the only way to address plasticity loss. We introduce a resetting approach based on model merging called Interpolate and show that contrary to previous findings, resetting even the most active parameters using our approach can also lead to better generalization. We further show that Interpolate can perform similarly or better compared to traditional resetting methods, offering a new perspective on training dynamics in non-stationary settings.

## item_id: m_0549

TITLE: Mirror Descent View For Neural Network Quantization

ABSTRACT: Quantizing large Neural Networks (NN) while maintaining the performance is highly desirable for resource-limited devices due to reduced memory and time complexity. NN quantization is usually formulated as a constrained optimization problem and optimized via a modified version of gradient descent. In this work, by interpreting the continuous parameters (unconstrained) as the dual of the quantized ones, we introduce a Mirror Descent (MD) framework (Bubeck (2015)) for NN quantization. Specifically, we provide conditions on the projections (i.e., mapping from continuous to quantized ones) which would enable us to derive valid mirror maps and in turn the respective MD updates. Furthermore, we discuss a numerically stable implementation of MD by storing an additional set of auxiliary dual variables (continuous). This update is strikingly analogous to the popular Straight Through Estimator (STE) based method which is typically viewed as a “trick” to avoid vanishing gradients issue but here we show that it is an implementation method for MD for certain projections. Our experiments on standard classification datasets (CIFAR-10/100, TinyImageNet) with convolutional and residual architectures show that our MD variants obtain fully-quantized networks with accuracies very close to the floating-point networks.

## item_id: m_0550

TITLE: Graph Neural Networks with Generated Parameters for Relation Extraction

ABSTRACT: Recently, progress has been made towards improving relational reasoning in machine learning field. Among existing models, graph neural networks (GNNs) is one of the most effective approaches for multi-hop relational reasoning. In fact, multi-hop relational reasoning is indispensable in many natural language processing tasks such as relation extraction. In this paper, we propose to generate the parameters of graph neural networks (GP-GNNs) according to natural language sentences, which enables GNNs to process relational reasoning on unstructured text inputs. We verify GP-GNNs in relation extraction from text. Experimental results on a human-annotated dataset and two distantly supervised datasets show that our model achieves significant improvements compared to the baselines. We also perform a qualitative analysis to demonstrate that our model could discover more accurate relations by multi-hop relational reasoning.

## item_id: m_0551

TITLE: Deterministic Variational Inference for Robust Bayesian Neural Networks

ABSTRACT: Bayesian neural networks (BNNs) hold great promise as a flexible and principled solution to deal with uncertainty when learning from finite data. Among approaches to realize probabilistic inference in deep neural networks, variational Bayes (VB) is theoretically grounded, generally applicable, and computationally efficient. With wide recognition of potential advantages, why is it that variational Bayes has seen very limited practical use for BNNs in real applications? We argue that variational inference in neural networks is fragile: successful implementations require careful initialization and tuning of prior variances, as well as controlling the variance of Monte Carlo gradient estimates. We provide two innovations that aim to turn VB into a robust inference tool for Bayesian neural networks: first, we introduce a novel deterministic method to approximate moments in neural networks, eliminating gradient variance; second, we introduce a hierarchical prior for parameters and a novel Empirical Bayes procedure for automatically selecting prior variances. Combining these two innovations, the resulting method is highly efficient and robust. On the application of heteroscedastic regression we demonstrate good predictive performance over alternative approaches.

## item_id: m_0552

TITLE: Automated curriculum generation through setter-solver interactions

ABSTRACT: Reinforcement learning algorithms use correlations between policies and rewards to improve agent performance.   But in dynamic or sparsely rewarding environments these correlations are often too small,  or rewarding events are too infrequent to make learning feasible. Human education instead relies on curricula –the breakdown of tasks into simpler, static challenges with dense rewards– to build up to complex behaviors.  While curricula are also useful for artificial agents, hand-crafting them is time consuming.  This has lead researchers to explore automatic curriculum generation. Here we explore automatic curriculum generation in rich,dynamic environments.  Using a setter-solver paradigm we show the importance of considering goal validity, goal feasibility, and goal coverage to construct useful curricula.  We demonstrate the success of our approach in rich but sparsely rewarding 2D and 3D environments, where an agent is tasked to achieve a single goal selected from a set of possible goals that varies between episodes, and identify challenges for future work.  Finally, we demonstrate the value of a novel technique that guides agents towards a desired goal distribution. Altogether, these results represent a substantial step towards applying automatic task curricula to learn complex,  otherwise unlearnable goals,  and to our knowledge are the first to demonstrate automated curriculum generation for goal-conditioned agents in environments where the possible goals vary between episodes.

## item_id: m_0553

TITLE: Generative Adversarial Networks for Extreme Learned Image Compression

ABSTRACT: We propose a framework for extreme learned image compression based on Generative Adversarial Networks (GANs), obtaining visually pleasing images at significantly lower bitrates than previous methods. This is made possible through our GAN formulation of learned compression combined with a generator/decoder which operates on the full-resolution image and is trained in combination with a multi-scale discriminator. Additionally, if a semantic label map of the original image is available, our method can fully synthesize unimportant regions in the decoded image such as streets and trees from the label map, therefore only requiring the storage of the preserved region and the semantic label map. A user study confirms that for low bitrates, our approach is preferred to state-of-the-art methods, even when they use more than double the bits.

## item_id: m_0554

TITLE: Group Sparse CNNs for Question Sentence Classification with Answer Sets

ABSTRACT: Classifying question sentences into their corresponding categories is an important task with wide applications, for example in many websites' FAQ sections. 
However, traditional question classification techniques do not fully utilize the well-prepared answer data which has great potential for improving question sentence representations which could lead to better classification performance. In order to encode answer information into question representation, we first introduce novel group sparse autoencoders which could utilize the group information in the answer set to refine question representation. We then propose a new group sparse convolutional neural network which could naturally learn the question representation with respect to their corresponding answers by implanting the group sparse autoencoders into the traditional convolutional neural network. The proposed model show significant improvements over strong baselines on four datasets.  

## item_id: m_0555

TITLE: SFW sampling for diffusion models via external conditioning

ABSTRACT: Score-based generative models (SBM), also known as diffusion models, are the de facto state of the art for image synthesis. Despite their unparalleled performance, SBMs have recently been in the spotlight for being tricked into creating not-safe-for-work (NSFW) content, such as violent images and non-consensual nudity. This article proposes a safe-for-work (SFW) sampler for SBMs implementing a Conditional Trajectory Correction step that guides the samples away from undesired regions in the ambient space using external multimodal models as the source of conditioning. Furthermore, using Contrastive Language Image Pre-training (CLIP), our method admits user-defined NSFW classes, which can vary in different settings. Our experiments on the text-to-image SBM Stable Diffusion validate that the proposed SFW sampler effectively reduces the generation of explicit content, as assessed via independent NSFW detectors. Furthermore, the proposed correction comes at a minor cost in image quality and has an almost null effect on samples that do not need correction. Our study confirms the suitability of the SFW sampler towards aligned SBM models.

## item_id: m_0556

TITLE: PUMA: Empowering Unified MLLM with Multi-granular Visual Generation

ABSTRACT: Recent advancements in multimodal foundation models have yielded significant progress in vision-language understanding. Initial attempts have also explored the potential of multimodal large language models (MLLMs) for visual content generation. However, existing works have insufficiently addressed the varying granularity demands of different image generation tasks within a unified MLLM paradigm — from the diversity required in text-to-image generation to the precise controllability needed in image manipulation. In this work, we propose PUMA, emPowering Unified MLLM with Multi-grAnular visual generation. PUMA unifies multi-granular visual features as both inputs and outputs of MLLMs, elegantly addressing the different granularity requirements of various image generation tasks within a unified MLLM framework. Following multimodal pretraining and task-specific instruction tuning, PUMA demonstrates proficiency in a wide range of multimodal tasks, including image understanding, diverse text-to-image generation, editing, inpainting, colorization, and conditional generation. This work represents a significant step towards a truly unified MLLM capable of adapting to the granularity demands of various visual tasks.

## item_id: m_0557

TITLE: An Information-Theoretic Metric of Transferability for Task Transfer Learning

ABSTRACT: An important question in task transfer learning is to determine task transferability, i.e. given a common input domain, estimating to what extent representations learned from a source task can help in learning a target task. Typically, transferability is either measured experimentally or inferred through task relatedness, which is often defined without a clear operational meaning. In this paper, we present a novel metric, H-score, an easily-computable evaluation function that estimates the performance of transferred representations from one task to another in classification problems. Inspired by a principled information theoretic approach, H-score has a direct connection to the asymptotic error probability of the decision function based on the transferred feature. This formulation of transferability can further be used to select a suitable set of source tasks in task transfer learning problems or to devise efficient transfer learning policies. Experiments using both synthetic and real image data show that not only our formulation of transferability is meaningful in practice, but also it can generalize to inference problems beyond classification, such as recognition tasks for 3D indoor-scene understanding.

## item_id: m_0558

TITLE: A prototype-oriented clustering for domain shift with source privacy

ABSTRACT: Unsupervised clustering under domain shift (UCDS) studies how to transfer the knowledge from abundant unlabeled data from multiple source domains to learn the representation of the unlabeled data in a target domain. In this paper, we introduce Prototype-oriented Clustering with Distillation (PCD) to not only improve the performance and applicability of existing methods for UCDS, but also address the concerns on protecting the privacy of both the data and model of the source domains. PCD first constructs a source clustering model by aligning the distributions of prototypes and data. It then distills the knowledge to the target model through cluster labels provided by the source model while simultaneously clustering the target data. Finally, it refines the target model on the target domain data without guidance from the source model. Experiments across multiple benchmarks show the effectiveness and generalizability of our source-private clustering method.

## item_id: m_0559

TITLE: Enhancing Molecular Property Predictions by Learning from Bond Modelling and Interactions

ABSTRACT: Molecule representation learning is crucial for understanding and predicting molecular properties. However, conventional atom-centric models, which treat chemical bonds merely as pairwise interactions, often overlook complex bond-level phenomena like resonance and stereoselectivity. This oversight limits their predictive accuracy for nuanced chemical behaviors. To address this limitation, we introduce \textbf{DeMol}, a dual-graph framework whose architecture is motivated by a rigorous information-theoretic analysis demonstrating the information gain from a bond-centric perspective. DeMol explicitly models molecules through parallel atom-centric and bond-centric channels. These are synergistically fused by multi-scale Double-Helix Blocks designed to learn intricate atom-atom, atom-bond, and bond-bond interactions. The framework's geometric consistency is further enhanced by a regularization term based on covalent radii to enforce chemically plausible structures. Comprehensive evaluations on diverse benchmarks, including PCQM4Mv2, OC20 IS2RE, QM9, and MoleculeNet, show that DeMol establishes a new state-of-the-art, outperforming existing methods. These results confirm the superiority of explicitly modelling bond information and interactions, paving the way for more robust and accurate molecular machine learning.

## item_id: m_0560

TITLE: Analyzing and Improving Generative Adversarial Training for Generative Modeling and Out-of-Distribution Detection

ABSTRACT: Generative adversarial training (GAT) is a recently introduced adversarial defense method. Previous works have focused on empirical evaluations of its application to training robust predictive models. In this paper we focus on theoretical understanding of the GAT method and extending its application to generative modeling and out-of-distribution detection. We analyze the optimal solutions of the maximin formulation employed by the GAT objective, and make a comparative analysis of the minimax formulation employed by GANs. We use theoretical analysis and 2D simulations to understand the convergence property of the training algorithm. Based on these results, we develop an unconstrained GAT algorithm, and conduct comprehensive evaluations of the algorithm's application to image generation and adversarial out-of-distribution detection. Our results suggest that generative adversarial training is a promising new direction for the above applications.

## item_id: m_0561

TITLE: Parametrized Hierarchical Procedures for Neural Programming

ABSTRACT: Neural programs are highly accurate and structured policies that perform algorithmic tasks by controlling the behavior of a computation mechanism. Despite the potential to increase the interpretability and the compositionality of the behavior of artificial agents, it remains difficult to learn from demonstrations neural networks that represent computer programs. The main challenges that set algorithmic domains apart from other imitation learning domains are the need for high accuracy, the involvement of specific structures of data, and the extremely limited observability. To address these challenges, we propose to model programs as Parametrized Hierarchical Procedures (PHPs). A PHP is a sequence of conditional operations, using a program counter along with the observation to select between taking an elementary action, invoking another PHP as a sub-procedure, and returning to the caller. We develop an algorithm for training PHPs from a set of supervisor demonstrations, only some of which are annotated with the internal call structure, and apply it to efficient level-wise training of multi-level PHPs. We show in two benchmarks, NanoCraft and long-hand addition, that PHPs can learn neural programs more accurately from smaller amounts of both annotated and unannotated demonstrations.

## item_id: m_0562

TITLE: Sentence Ordering using Recurrent Neural Networks

ABSTRACT: Modeling the structure of coherent texts is a task of great importance in NLP. The task of organizing a given set of sentences into a coherent order has been
commonly used to build and evaluate models that understand such structure. In this work we propose an end-to-end neural approach based on the recently proposed
set to sequence mapping framework to address the sentence ordering problem. Our model achieves state-of-the-art performance in the order discrimination task
on two datasets widely used in the literature. We also consider a new interesting task of ordering abstracts from conference papers and research proposals and
demonstrate strong performance against recent methods. Visualizing the sentence representations learned by the model shows that the model has captured high
level logical structure in these paragraphs. The model also learns rich semantic sentence representations by learning to order texts, performing comparably to
recent unsupervised representation learning methods in the sentence similarity and paraphrase detection tasks.

## item_id: m_0563

TITLE: InfoBatch: Lossless Training Speed Up by Unbiased Dynamic Data Pruning

ABSTRACT: Data pruning aims to obtain lossless performances with less overall cost. A common approach is to filter out samples that make less contribution to the training. This could lead to gradient expectation bias compared to the original data. To solve this problem, we propose InfoBatch, a novel framework aiming to achieve lossless training acceleration by unbiased dynamic data pruning. Specifically, InfoBatch
randomly prunes a portion of less informative samples based on the loss distribution and rescales the gradients of the remaining samples to approximate the original gradient. As a plug-and-play and architecture-agnostic framework, InfoBatch consistently obtains lossless training results on classification, semantic segmentation, vision pertaining, and instruction fine-tuning tasks. On CIFAR10/100, ImageNet-
1K, and ADE20K, InfoBatch losslessly saves 40% overall cost. For pertaining MAE and diffusion model, InfoBatch can respectively save 24.8% and 27% cost. For LLaMA instruction fine-tuning, combining InfoBatch and the recent coreset selection method (DQ) can achieve 10 times acceleration. Our results encourage more exploration on the data efficiency aspect of large model training. Code is publicly available at NUS-HPC-AI-Lab/InfoBatch.

## item_id: m_0564

TITLE: Deep Layers as Stochastic Solvers

ABSTRACT: We provide a novel perspective on the forward pass through a block of layers in a deep network. In particular, we show that a forward pass through a standard dropout layer followed by a linear layer and a non-linear activation is equivalent to optimizing a convex objective with a single iteration of a $\tau$-nice Proximal Stochastic Gradient method. We further show that replacing standard Bernoulli dropout with additive dropout is equivalent to optimizing the same convex objective with a variance-reduced proximal method. By expressing both fully-connected and convolutional layers as special cases of a high-order tensor product, we unify the underlying convex optimization problem in the tensor setting and derive a formula for the Lipschitz constant $L$ used to determine the optimal step size of the above proximal methods. We conduct experiments with standard convolutional networks applied to the CIFAR-10 and CIFAR-100 datasets and show that replacing a block of layers with multiple iterations of the corresponding solver, with step size set via $L$, consistently improves classification accuracy.

## item_id: m_0565

TITLE: Generate-then-Test: Automated Test Case Generation for WebAssembly Using Large Language Models

ABSTRACT: The reliability and security of WebAssembly (Wasm) binaries are crucial for modern web development, yet effective testing methodologies remain undeveloped. This paper addresses the gap in Wasm binary testing by proposing a novel approach for test cases generation, leveraging Large Language Models (LLMs) to enhance test coverage and bug detection. Traditional testing approaches typically require access to source code, which is often unavailable for Wasm binaries. Our generate-then-test methodology overcomes this limitation by generating equivalent C++ code to simulate expected Wasm behavior, creating and mutating test cases in C++, and compiling these tests to evaluate them against the Wasm binary. Key contributions include automated test case generation using LLMs and improved code coverage through type-aware mutations, with comprehensive evaluation demonstrating the effectiveness of our approach in detecting subtle bugs in Wasm binaries, thereby ensuring more reliable Wasm applications.

## item_id: m_0566

TITLE: On Representation Learning in the First Layer of Deep CNNs and the Dynamics of Gradient Descent

ABSTRACT: It has previously been reported that the representation that is learned in the first layer of deep CNNs is very different from the initial representation and highly consistent across initialization and architecture. In this work, we quantify this consistency by considering the set of filters as a filter bank and measuring its energy distribution. We find that the energy distribution is remarkably consistent and try to determine the source of this consistency. We show that this consistency cannot be explained by the fact that CNNs learn a representation that is useful for recognition and that CNNs trained with fixed, random filters in the first layer yield comparable recognition performance to full learning. We then show that similar behavior occurs in simple, linear CNNs and obtain an analytical characterization of the energy profile of linear CNNs trained with gradient descent. Our analysis shows that the energy profile is determined by two factors (1) the correlation of the average patch and the class label and (2) an implicit bias given  the dynamics of gradient descent. Finally, we show that in commonly used image recognition datasets the correlation between the average patch and the class label is very low and it is the implicit bias that best explains the consistency of representations observed in real-world CNNs.

## item_id: m_0567

TITLE: Learning from Between-class Examples for Deep Sound Recognition

ABSTRACT: Deep learning methods have achieved high performance in sound recognition tasks. Deciding how to feed the training data is important for further performance improvement. We propose a novel learning method for deep sound recognition: Between-Class learning (BC learning). Our strategy is to learn a discriminative feature space by recognizing the between-class sounds as between-class sounds. We generate between-class sounds by mixing two sounds belonging to different classes with a random ratio. We then input the mixed sound to the model and train the model to output the mixing ratio. The advantages of BC learning are not limited only to the increase in variation of the training data; BC learning leads to an enlargement of Fisher’s criterion in the feature space and a regularization of the positional relationship among the feature distributions of the classes. The experimental results show that BC learning improves the performance on various sound recognition networks, datasets, and data augmentation schemes, in which BC learning proves to be always beneficial. Furthermore, we construct a new deep sound recognition network (EnvNet-v2) and train it with BC learning. As a result, we achieved a performance surpasses the human level.

## item_id: m_0568

TITLE: Behind the Scenes of Gradient Descent: A Trajectory Analysis via Basis Function Decomposition

ABSTRACT: This work analyzes the solution trajectory of gradient-based algorithms via a novel basis function decomposition. We show that, although solution trajectories of gradient-based algorithms may vary depending on the learning task, they behave almost monotonically when projected onto an appropriate orthonormal function basis. Such projection gives rise to a basis function decomposition of the solution trajectory. Theoretically, we use our proposed basis function decomposition to establish the convergence of gradient descent (GD) on several representative learning tasks. In particular, we improve the convergence of GD on symmetric matrix factorization and provide a completely new convergence result for the orthogonal symmetric tensor decomposition. Empirically, we illustrate the promise of our proposed framework on realistic deep neural networks (DNNs) across different architectures, gradient-based solvers, and datasets. Our key finding is that gradient-based algorithms monotonically learn the coefficients of a particular orthonormal function basis of DNNs defined as the eigenvectors of the conjugate kernel after training.

## item_id: m_0569

TITLE: Zero-Round Active Learning

ABSTRACT: Active learning (AL) aims at reducing labeling efforts by identifying the most valuable unlabeled data points from a large pool. Traditional AL frameworks have two limitations: First, they perform data selection in a multi-round manner, which is time-consuming and impractical. Second, they usually assume that there are a small amount of labeled data points available \emph{in the same domain as} the data in the unlabeled pool. 
Our paper investigates a new setting in active learning---how to conduct active learning without relying on pre-labeled data, which is an under-explored yet of great practical value.
Besides, we propose $D^2ULO$ as a solution that solves both issues, which leverages the idea of domain adaptation (DA) to train a data utility model that can effectively predict the utility for any given unlabeled data in the target domain once labeled. The trained data utility model can then be used to select high-utility data and at the same time, provide an estimate for the utility of the selected data. Our algorithm does not rely on any feedback from annotators in the target domain and hence, which is able to not only work standalone but also benefit existing multi-round active learning algorithms by providing a warm-start. 
Our experiments show that $D^2ULO$ outperforms the existing state-of-the-art AL strategies equipped with domain adaptation over various domain shift settings (e.g., real-to-real data and synthetic-to-real data). Particularly, $D^2ULO$ is applicable to the scenario where source and target labels have mismatch, which is not supported by the existing works. 

## item_id: m_0570

TITLE: Representing inferential uncertainty in deep neural networks through sampling

ABSTRACT: As deep neural networks (DNNs) are applied to increasingly challenging problems, they will need to be able to represent their own uncertainty. Modelling uncertainty is one of the key features of Bayesian methods. Bayesian DNNs that use dropout-based variational distributions and scale to complex tasks have recently been proposed. We evaluate Bayesian DNNs trained with Bernoulli or Gaussian multiplicative masking of either the units (dropout) or the weights (dropconnect). We compare these Bayesian DNNs ability to represent their uncertainty about their outputs through sampling during inference. We tested the calibration of these Bayesian fully connected and convolutional DNNs on two visual inference tasks (MNIST and CIFAR-10). By adding different levels of Gaussian noise to the test images, we assessed how these DNNs represented their uncertainty about regions of input space not covered by the training set. These Bayesian DNNs represented their own uncertainty more accurately than traditional DNNs with a softmax output. We find that sampling of weights, whether Gaussian or Bernoulli, led to more accurate representation of uncertainty compared to sampling of units. However, sampling units using either Gaussian or Bernoulli dropout led to increased convolutional neural network (CNN) classification accuracy. Based on these findings we use both Bernoulli dropout and Gaussian dropconnect concurrently, which approximates the use of a spike-and-slab variational distribution. We find that networks with spike-and-slab sampling combine the advantages of the other methods: they classify with high accuracy and robustly represent the uncertainty of their classifications for all tested architectures.

## item_id: m_0571

TITLE: Domain Transfer with Large Dynamics Shift in Offline Reinforcement Learning

ABSTRACT: The domain transfer problem with large dynamics shift commonly exists when using offline reinforcement learning (RL) in real-world applications, where the source dataset collected from one domain needs to be reused to accelerate training the target domain agent with offline RL. The large dynamics shift issue arises when there are unpredictable changes in the target domain’s environment. Existing works typically assume that each state-action pair in the target domain should be at least covered in the source domain, which is often unrealistic and limited to small dynamics shift transfers. To tackle the large dynamics shift problem, we propose to use the source domain data not only for offline policy training but also for safe and efficient data collection in the target domain, thus relaxing the above requirement. Specifically, the source data will play two roles, one is to serve as augmentation data by compensating for the difference in dynamics with modified reward. Another is to form prior knowledge for the behaviour policy to collect a small amount of new data in the target domain safely and efficiently. The target domain policy is trained using offline RL with the source data and modest amounts of newly collected target data. We justify our method in gridworld and autonomous driving environments. Results show that our method requires fewer target domain data and collecting the data in a safer manner compared with prior methods.

## item_id: m_0572

TITLE: Enabling Efficient Equivariant Operations in the Fourier Basis via Gaunt Tensor Products

ABSTRACT: Developing equivariant neural networks for the E(3) group plays an important role in modeling 3D data across real-world applications. Enforcing this equivariance primarily involves the tensor products of irreducible representations (irreps). However, the computational complexity of such operations increases significantly as higher-order tensors are used. In this work, we propose a systematic approach to substantially accelerate the computation of the tensor products of irreps. We mathematically connect the commonly used Clebsch-Gordan coefficients to the Gaunt coefficients, which are integrals of products of three spherical harmonics. Through Gaunt coefficients, the tensor product of irreps becomes equivalent to the multiplication between spherical functions represented by spherical harmonics. This perspective further allows us to change the basis for the equivariant operations from spherical harmonics to a 2D Fourier basis. Consequently, the multiplication between spherical functions represented by a 2D Fourier basis can be efficiently computed via the convolution theorem and Fast Fourier Transforms. This transformation reduces the complexity of full tensor products of irreps from $\mathcal{O}(L^6)$ to $\mathcal{O}(L^3)$, where $L$ is the max degree of irreps. Leveraging this approach, we introduce the Gaunt Tensor Product, which serves as a new method to construct efficient equivariant operations across different model architectures. Our experiments on the Open Catalyst Project and 3BPA datasets demonstrate both the increased efficiency and improved performance of our approach. The code and models will be made publicly available at https://github.com/lsj2408/Gaunt-Tensor-Product.

## item_id: m_0573

TITLE: Low Bias Gradient Estimates for Very Deep Boolean Stochastic Networks

ABSTRACT: Stochastic neural networks with discrete random variables are an important class of models for their expressivity and interpretability. Since direct differentiation and backpropagation is not possible, Monte Carlo gradient estimation techniques have been widely employed for training such models. Efficient stochastic gradient estimators, such Straight-Through and Gumbel-Softmax, work well for shallow models with one or two stochastic layers. Their performance, however, suffers with increasing model complexity.
In this work we focus on stochastic networks with multiple layers of Boolean latent variables. To analyze such such networks, we employ the framework of harmonic analysis for Boolean functions.  We use it to derive an analytic formulation for the source of bias in the biased Straight-Through estimator. Based on the analysis we propose \emph{FouST}, a simple gradient estimation algorithm that relies on three simple bias reduction steps. Extensive experiments show that FouST performs favorably compared to state-of-the-art biased estimators, while being much faster than unbiased ones. To the best of our knowledge FouST is the first gradient estimator to train up very deep stochastic neural networks, with up to 80 deterministic and 11 stochastic layers. 

## item_id: m_0574

TITLE: Deep Learning for Two-Sided Matching

ABSTRACT: We initiate the study of deep learning for the automated design of two-sided matching mechanisms. What is of most interest is to  use machine learning to understand  the possibility of new tradeoffs between *strategy-proofness* and *stability*.  These properties cannot be achieved simultaneously, but the efficient frontier is not understood. We introduce novel differentiable surrogates for quantifying ordinal strategy-proofness and stability and use them to train differentiable matching mechanisms that map discrete preferences to valid randomized matchings. We demonstrate that the efficient frontier characterized by these learned mechanisms is substantially better than that achievable through a convex combination of baselines of *deferred acceptance* (stable and strategy-proof for only one side of the market), *top trading cycles* (strategy-proof for one side, but not stable), and *randomized serial dictatorship* (strategy-proof for both sides, but not stable). This gives a new target for economic theory and opens up new possibilities for machine learning pipelines in matching market design.

## item_id: m_0575

TITLE: The  Price of Amortized inference in Sparse Autoencoders

ABSTRACT: Polysemy has long been a major challenge in Mechanistic Interpretability (MI), with Sparse Autoencoders (SAEs) emerging as a promising solution. SAEs employ a shared encoder to map inputs to sparse codes, thereby amortizing inference costs across all instances. However, this parameter-sharing paradigm inherently conflicts with the MI community’s emphasis on instance-level optimality, including the consistency and stitchability of monosemantic features. We first reveal the trade-off relationships among various pathological phenomena, including feature absorption, feature splitting, dead latents, and dense latents under global reconstruction-sparsity constraints from the perspective of training dynamics, finding that increased sparsity typically exacerbates multiple pathological phenomena, and attribute this trade-off relationship to amortized inference. By reducing reliance on amortized inference through the introduction of semi-amortized and non-amortized approaches, we observed that various pathological indicators were significantly mitigated, thereby validating our hypothesis. As the first step in this direction, we propose Local Amortized SAE (LocA-SAE), a method that groups polysemantically close latents based on the angular variance. This method is designed to balance the computational cost
of per-sample optimization with the limitations of amortized inference. Our work provides insights for understanding SAEs and advocates for a paradigm shift in future research on polysemy disentanglement. The code is available \url{https://github.com/wenjie1835/Local_Amotized_SAEs}.

## item_id: m_0576

TITLE: VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models

ABSTRACT: Large language models (LLMs) often exhibit subtle yet distinctive characteristics in their outputs that users intuitively recognize, but struggle to quantify. These "vibes" -- such as tone, formatting, or writing style -- influence user preferences, yet traditional evaluations focus primarily on the singular vibe of correctness.
We introduce $\textbf{VibeCheck}$, a system for automatically comparing a pair of LLMs by discovering identifying traits of a model ("vibes") that are well-defined, differentiating, and user-aligned. VibeCheck iteratively discovers vibes from model outputs and then utilizes a panel of LLM judges to quantitatively measure the utility of each vibe. 
We validate that the vibes generated by VibeCheck align with those found in human discovery and run VibeCheck on pairwise preference data from real-world user conversations with Llama-3-70b vs GPT-4. VibeCheck reveals that Llama has a friendly, funny, and somewhat controversial vibe. These vibes predict model identity with 80% accuracy and human preference with 61% accuracy. Lastly, we run VibeCheck on a variety of models and tasks, including summarization, math, and captioning to provide insight into differences in model behavior. VibeCheck discovers vibes like Command X prefers to add concrete intros and conclusions when summarizing in comparison to TNGL, Llama-405b often overexplains its thought process on math problems compared to GPT-4o, and GPT-4 prefers to focus on the mood and emotions of the scene when captioning compared to Gemini-1.5-Flash.

## item_id: m_0577

TITLE: CNN Based Analysis of the Luria’s Alternating Series Test for Parkinson’s Disease Diagnostics

ABSTRACT: Deep-learning based image classification is applied in this studies to the Luria's alternating series tests to support diagnostics of the Parkinson's disease. Luria's alternating series tests belong to the family of fine-motor drawing tests and been used in neurology and psychiatry for nearly a century. Introduction of the digital tables and later tablet PCs has allowed deviating from the classical paper and pen setting, and observe kinematic and pressure parameters describing the test. While such setting has led to a highly accurate machine learning models, the visual component of the tests is left unused. Namely, the shapes of the drawn lines are not used to classify the drawings, which eventually has caused the shift in the assessment paradigm from visual-based to the numeric parameters based. The approach proposed in this paper allows combining two assessment paradigms by augmenting initial drawings by the kinematic and pressure parameters. The paper demonstrates that the resulting network has the accuracy similar to those of human practitioner.

## item_id: m_0578

TITLE: Translation Memory Guided Neural Machine Translation

ABSTRACT: Many studies have proven that Translation Memory (TM) can help improve the translation quality of neural machine translation (NMT). Existing ways either employ extra encoder to encode information from TM or concatenate source sentence and TM sentences as encoder's input. These previous methods don't model the semantic relationship between the source sentence and TM sentences. Meanwhile, the training corpus related to TM is limited, and the sentence level retrieval approach further limits its scale. 
In this paper, we propose a novel method to combine the strengths of both TM and NMT. We treat the matched sentence pair of TM as the additional signal and apply one encoder enhanced by the pre-trained language model (PLM) to encode the TM information and source sentence together. Additionally, we extend the sentence level retrieval method to the n-gram retrieval method that we don't need to calculate the similarity score. Further, we explore new methods to manipulate the information flow from TM to the NMT decoder. We validate our proposed methods on a mixed test set of multiple domains. Experiment results demonstrate that the proposed methods can significantly improve the translation quality and show strong adaptation for an unknown or new domain.

## item_id: m_0579

TITLE: GREAT Score: Global Robustness Evaluation of Adversarial Perturbation using Generative Models

ABSTRACT: Current studies on adversarial robustness mainly focus on aggregating \textit{local} robustness results from a set of data samples to evaluate and rank different models. However, the local statistics may not well represent the true \textit{global} robustness of the underlying unknown data distribution. To address this challenge, this paper makes the first attempt to present a new framework, called \textit{GREAT Score}, for global robustness evaluation of adversarial perturbation using generative models. Formally, GREAT Score carries the physical meaning of  a global statistic capturing a mean certified attack-proof perturbation level over all samples drawn from a generative model. For finite-sample evaluation, we also derive a probabilistic guarantee on the sample complexity and the difference between the sample mean and the true mean. GREAT Score has several advantages: (1) Robustness evaluations using GREAT Score are efficient and scalable to large models, by sparing the need of running adversarial attacks. In particular, we show high correlation and significantly reduced computation cost of GREAT Score when compared to the attack-based model ranking on RobustBench \cite{croce2021robustbench}.
(2) The use of generative models facilitates the approximation of the unknown data distribution. In our ablation study with different generative adversarial networks (GANs), we observe consistency between global robustness evaluation and the quality of GANs. (3) GREAT Score can be used for remote auditing of privacy-sensitive black-box models, as demonstrated by our robustness evaluation on several online facial recognition services.

## item_id: m_0580

TITLE: Autoencoders as Cross-Modal Teachers: Can Pretrained 2D Image Transformers Help 3D Representation Learning?

ABSTRACT: The success of deep learning heavily relies on large-scale data with comprehensive labels, which is more expensive and time-consuming to fetch in 3D compared to 2D images or natural languages. This promotes the potential of utilizing models pretrained with data more than 3D as teachers for cross-modal knowledge transferring. In this paper, we revisit masked modeling in a unified fashion of knowledge distillation, and we show that foundational Transformers pretrained with 2D images or natural languages can help self-supervised 3D representation learning through training Autoencoders as Cross-Modal Teachers (ACT). The pretrained Transformers are transferred as cross-modal 3D teachers using discrete variational autoencoding self-supervision, during which the Transformers are frozen with prompt tuning for better knowledge inheritance. The latent features encoded by the 3D teachers are used as the target of masked point modeling, wherein the dark knowledge is distilled to the 3D Transformer students as foundational geometry understanding. Our ACT pretrained 3D learner achieves state-of-the-art generalization capacity across various downstream benchmarks, e.g., 88.21% overall accuracy on ScanObjectNN. Codes have been released at https://github.com/RunpeiDong/ACT.

## item_id: m_0581

TITLE: Initialization and Regularization of Factorized Neural Layers

ABSTRACT: Factorized layers—operations parameterized by products of two or more matrices—occur in a variety of deep learning contexts, including compressed model training, certain types of knowledge distillation, and multi-head self-attention architectures. We study how to initialize and regularize deep nets containing such layers, examining two simple, understudied schemes, spectral initialization and Frobenius decay, for improving their performance. The guiding insight is to design optimization routines for these networks that are as close as possible to that of their well-tuned, non-decomposed counterparts; we back this intuition with an analysis of how the initialization and regularization schemes impact training with gradient descent, drawing on modern attempts to understand the interplay of weight-decay and batch-normalization. Empirically, we highlight the benefits of spectral initialization and Frobenius decay across a variety of settings. In model compression, we show that they enable low-rank methods to significantly outperform both unstructured sparsity and tensor methods on the task of training low-memory residual networks; analogs of the schemes also improve the performance of tensor decomposition techniques. For knowledge distillation, Frobenius decay enables a simple, overcomplete baseline that yields a compact model from over-parameterized training without requiring retraining with or pruning a teacher network. Finally, we show how both schemes applied to multi-head attention lead to improved performance on both translation and unsupervised pre-training.

## item_id: m_0582

TITLE: How Much Space Has Been Explored? Measuring the Chemical Space Covered by Databases and Machine-Generated Molecules

ABSTRACT: Forming a molecular candidate set that contains a wide range of potentially effective compounds is crucial to the success of drug discovery. While most databases and machine-learning-based generation models aim to optimize particular chemical properties, there is limited literature on how to properly measure the coverage of the chemical space by those candidates included or generated. This problem is challenging due to the lack of formal criteria to select good measures of the chemical space. In this paper, we propose a novel evaluation framework for measures of the chemical space based on two analyses: an axiomatic analysis with three intuitive axioms that a good measure should obey, and an empirical analysis on the correlation between a measure and a proxy gold standard. Using this framework, we are able to identify #Circles, a new measure of chemical space coverage, which is superior to existing measures both analytically and empirically. We further evaluate how well the existing databases and generation models cover the chemical space in terms of #Circles. The results suggest that many generation models fail to explore a larger space over existing databases, which leads to new opportunities for improving generation models by encouraging exploration. 


## item_id: m_0583

TITLE: An Active Learning Framework for Efficient Robust Policy Search

ABSTRACT: Robust Policy Search is the problem of learning policies that do not degrade in performance when subject to unseen environment model parameters. It is particularly relevant for transferring policies learned in a simulation environment to the real world. Several existing approaches involve sampling large batches of trajectories which reflect the differences in various possible environments, and then selecting some subset of these to learn robust policies, such as the ones that  result in the worst performance. We propose an active learning based framework, EffAcTS, to selectively choose model parameters for this purpose so as to collect only as much data as necessary to select such a subset. We apply this framework to an existing method, namely EPOpt, and experimentally validate the gains in sample efficiency and the performance of our approach on standard continuous control tasks. We also present a Multi-Task Learning perspective to the problem of Robust Policy Search, and draw connections from our proposed framework to existing work on Multi-Task Learning.

## item_id: m_0584

TITLE: How can we generalise learning distributed representations of graphs?

ABSTRACT: We propose a general framework to construct unsupervised models capable of learning distributed representations of discrete structures such as graphs based on R-Convolution kernels and distributed semantics research. Our framework combines the insights and observations of Deep Graph Kernels and Graph2Vec towards a unified methodology for performing similarity learning on graphs of arbitrary size. This is exemplified by our own instance G2DR which extends Graph2Vec from labelled graphs towards unlabelled graphs and tackles issues of diagonal dominance through pruning of the subgraph vocabulary composing graphs. These changes produce new state of the art results in the downstream application of G2DR embeddings in graph classification tasks over datasets with small labelled graphs in binary classification to multi-class classification on large unlabelled graphs using an off-the-shelf support vector machine. 

## item_id: m_0585

TITLE: Bilevel ZOFO: Bridging Parameter-Efficient and Zeroth-Order Techniques for Efficient LLM Fine-Tuning and Meta-Training

ABSTRACT: Fine-tuning pre-trained Large Language Models (LLMs) for downstream tasks using First-Order (FO) optimizers presents significant computational challenges. Parameter-Efficient Fine-Tuning (PEFT) methods have been proposed to address these challenges by freezing most model parameters and training only a small subset. While PEFT is efficient, it may not outperform full fine-tuning when high task-specific performance is required.
Zeroth-Order (ZO) methods offer an alternative for fine-tuning the entire pre-trained model by approximating gradients using only the forward pass, thus eliminating the computational burden of back-propagation in first-order methods. However, when implementing ZO methods, it is crucial to ensure prompt-based text alignment, and relying on simple, fixed hard prompts may not be optimal. In this paper, we propose a bilevel optimization framework that complements ZO methods with PEFT to mitigate sensitivity to hard prompts while efficiently and effectively fine-tuning LLMs. Our Bilevel ZOFO (Zeroth-Order-First-Order) method employs a double-loop optimization strategy, where only the gradient of the PEFT model and the forward pass of the base model are required. We provide convergence guarantees for Bilevel ZOFO. Empirically, we demonstrate that Bilevel ZOFO outperforms both PEFT and ZO methods in single-task settings. Additionally, we show its strong potential for multitask learning. Compared to current first-order meta-training algorithms for multitask learning, our method has significantly lower computational demands while maintaining or improving performance.

## item_id: m_0586

TITLE: Defensive Quantization: When Efficiency Meets Robustness

ABSTRACT: Neural network quantization is becoming an industry standard to efficiently deploy deep learning models on hardware platforms, such as CPU, GPU, TPU, and FPGAs. However, we observe that the conventional quantization approaches are vulnerable to adversarial attacks. This paper aims to raise people's awareness about the security of the quantized models, and we designed a novel quantization methodology to jointly optimize the efficiency and robustness of deep learning models. We first conduct an empirical study to show that vanilla quantization suffers more from adversarial attacks. We observe that the inferior robustness comes from the error amplification effect, where the quantization operation further enlarges the distance caused by amplified noise. Then we propose a novel Defensive Quantization (DQ) method by controlling the Lipschitz constant of the network during quantization, such that the magnitude of the adversarial noise remains non-expansive during inference. Extensive experiments on CIFAR-10 and SVHN datasets demonstrate that our new quantization method can defend neural networks against adversarial examples, and even achieves superior robustness than their full-precision counterparts, while maintaining the same hardware efficiency as vanilla quantization approaches. As a by-product, DQ can also improve the accuracy of quantized models without adversarial attack. 

## item_id: m_0587

TITLE: Gradients of Counterfactuals

ABSTRACT: Gradients have been used to quantify feature importance in machine learning models. Unfortunately, in nonlinear deep networks, not only individual neurons but also the whole network can saturate, and as a result an important input feature can have a tiny gradient. We study various networks, and observe that this phenomena is indeed widespread, across many inputs.

We propose to examine interior gradients, which are gradients of counterfactual inputs constructed by scaling down the original input. We apply our method to the GoogleNet architecture for object recognition in images, as well as a ligand-based virtual screening network with categorical features and an LSTM based language model for the Penn Treebank dataset. We visualize how interior gradients better capture feature importance. Furthermore, interior gradients are applicable to a wide variety of deep networks, and have the attribution property that the feature importance scores sum to the the prediction score. 

Best of all, interior gradients can be computed just as easily as gradients. In contrast, previous methods are complex to implement, which hinders practical adoption.

## item_id: m_0588

TITLE: Scale-Equivariant Steerable Networks

ABSTRACT: The effectiveness of Convolutional Neural Networks (CNNs) has been substantially attributed to their built-in property of translation equivariance. However, CNNs do not have embedded mechanisms to handle other types of transformations. In this work, we pay attention to scale changes, which regularly appear in various tasks due to the changing distances between the objects and the camera. First, we introduce the general theory for building scale-equivariant convolutional networks with steerable filters. We develop scale-convolution and generalize other common blocks to be scale-equivariant. We demonstrate the computational efficiency and numerical stability of the proposed method. We compare the proposed models to the previously developed methods for scale equivariance and local scale invariance. We demonstrate state-of-the-art results on the MNIST-scale dataset and on the STL-10 dataset in the supervised learning setting.

## item_id: m_0589

TITLE: Reward Model Boosting for RLHF

ABSTRACT: Reinforcement Learning from Human Feedback (RLHF) is a powerful technique for aligning large language models (LLMs) with human preference. However, it often suffers from the reward hacking issue, where policy optimization improves the proxy reward model while actually degrading performance with respect to the true human preference, due to the imperfection of the proxy. To address this, we propose Reward Model Boosting (RMB), a novel approach that enhances the robustness and reliability of the reward signal for RLHF. RMB first trains a set of reward models with a diverse-promoting regularizer. This encourages each model to learn complementary aspects of the reward landscape. Then, RMB learns a lightweight aggregator in the principle of boosting to aggregate the outputs of the diverse reward models into a more accurate and robust reward signal. Our extensive experiments demonstrate that RMB significantly improves reward accuracy on both in-distribution and out-of-distribution datasets, substantially mitigating the reward hacking issue and ultimately improving RLHF performance.

## item_id: m_0590

TITLE: Multi-Action Self-Improvement For Neural Combinatorial Optimization

ABSTRACT: Self-improvement has emerged as a state-of-the-art paradigm in Neural Combinatorial Optimization (NCO), where models iteratively refine their policies by generating and imitating high-quality solutions. Despite strong empirical performance, existing methods face key limitations. Training is computationally expensive, as policy updates require sampling numerous candidate solutions per instance to extract a single expert trajectory. More fundamentally, these approaches fail to exploit the structure of combinatorial problems involving the coordination of multiple agents, such as vehicles in min-max routing or machines in scheduling. By supervising on single-action trajectories,  they fail to exploit agent-permutation symmetries, where distinct sequences of actions yield identical solutions, hindering generalization and the ability to learn coordinated behavior.

We address these challenges by extending self-improvement to operate over joint multi-agent actions. Our model architecture predicts complete agent-task assignments jointly at each decision step. To explicitly leverage symmetries, we employ a set-prediction loss, which supervises the policy on multiple expert assignments for any given state. This approach enhances sample efficiency and the model's ability to learn coordinated behavior. Furthermore, by generating multi-agent actions in parallel, it drastically accelerates the solution generation phase of the self-improvement loop. Empirically, we validate our method on several combinatorial problems, demonstrating consistent improvements in the quality of the final solution and a reduced generation latency compared to standard self-improvement.

## item_id: m_0591

TITLE: Stochastically Controlled Compositional Gradient for the Composition problem

ABSTRACT: We consider  composition problems of the form  $\frac{1}{n}\sum\nolimits_{i= 1}^n F_i(\frac{1}{n}\sum\nolimits_{j = 1}^n G_j(x))$. Composition optimization arises in many important machine learning applications: reinforcement learning, variance-aware learning, nonlinear embedding, and many others. Both gradient descent and stochastic gradient descent are straightforward solution, but both require to  compute $\frac{1}{n}\sum\nolimits_{j = 1}^n{G_j( x )} $ in each single iteration, which is inefficient-especially when $n$ is large. Therefore, with the aim of significantly reducing the query complexity of such problems, we designed a stochastically controlled compositional gradient algorithm that incorporates two kinds of variance reduction techniques, and works in both strongly convex and non-convex settings. The strategy is also accompanied by a mini-batch version of the proposed method that improves query complexity with respect to the size of the mini-batch. Comprehensive experiments demonstrate the superiority of the proposed method over existing methods.

## item_id: m_0592

TITLE: Frustratingly Short Attention Spans in Neural Language Modeling

ABSTRACT: Current language modeling architectures often use recurrent neural networks. Recently, various methods for incorporating differentiable memory into these architectures have been proposed. When predicting the next token, these models query information from a memory of the recent history and thus can facilitate learning mid- and long-range dependencies. However, conventional attention models produce a single output vector per time step that is used for predicting the next token as well as the key and value of a differentiable memory of the history of tokens. In this paper, we propose a key-value attention mechanism that produces separate representations for the key and value of a memory, and for a representation that encodes the next-word distribution. This usage of past memories outperforms existing memory-augmented neural language models on two corpora. Yet, we found that it mainly utilizes past memory only of the previous five representations. This led to the unexpected main finding that a much simpler model which simply uses a concatenation of output representations from the previous three-time steps is on par with more sophisticated memory-augmented neural language models.

## item_id: m_0593

TITLE: TimeInf: Time Series Data Contribution via Influence Functions

ABSTRACT: Evaluating the contribution of individual data points to a model's prediction is critical for interpreting model predictions and improving model performance. Existing data contribution methods have been applied to various data types, including tabular data, images, and text; however, their primary focus has been on i.i.d. settings. Despite the pressing need for principled approaches tailored to time series datasets, the problem of estimating data contribution in such settings remains under-explored, possibly due to challenges associated with handling inherent temporal dependencies. This paper introduces TimeInf, a model-agnostic data contribution estimation method for time-series datasets. By leveraging influence scores, TimeInf attributes model predictions to individual time points while preserving temporal structures between the time points. Our empirical results show that TimeInf effectively detects time series anomalies and outperforms existing data attribution techniques as well as state-of-the-art anomaly detection methods. Moreover, TimeInf offers interpretable attributions of data values, allowing us to distinguish diverse anomalous patterns through visualizations. We also showcase a potential application of TimeInf in identifying mislabeled anomalies in the ground truth annotations.

## item_id: m_0594

TITLE: Expressive power of recurrent neural networks

ABSTRACT: Deep neural networks are surprisingly efficient at solving practical tasks,
but the theory behind this phenomenon is only starting to catch up with
the practice. Numerous works show that depth is the key to this efficiency.
A certain class of deep convolutional networks – namely those that correspond
to the Hierarchical Tucker (HT) tensor decomposition – has been
proven to have exponentially higher expressive power than shallow networks.
I.e. a shallow network of exponential width is required to realize
the same score function as computed by the deep architecture. In this paper,
we prove the expressive power theorem (an exponential lower bound on
the width of the equivalent shallow network) for a class of recurrent neural
networks – ones that correspond to the Tensor Train (TT) decomposition.
This means that even processing an image patch by patch with an RNN
can be exponentially more efficient than a (shallow) convolutional network
with one hidden layer. Using theoretical results on the relation between
the tensor decompositions we compare expressive powers of the HT- and
TT-Networks. We also implement the recurrent TT-Networks and provide
numerical evidence of their expressivity.

## item_id: m_0595

TITLE: Learning to Ground VLMs without Forgetting

ABSTRACT: Spatial awareness is key to enable embodied multimodal AI systems. Yet, without vast amounts of spatial supervision, current Visual Language Models (VLMs) struggle at this task. In this paper, we introduce LynX, a framework that equips pretrained VLMs with visual grounding ability without forgetting their existing image and language understanding skills.
To this end, we propose a Dual Mixture of Experts module that modifies only the decoder layer of the language model, using one frozen Mixture of Experts (MoE) pre-trained on image and language understanding and another learnable MoE for new grounding capabilities. This allows the VLM to retain previously learned knowledge and skills, while acquiring what is missing.
To train the model effectively, we generate a high-quality synthetic dataset we call SCouT, which mimics human reasoning in visual grounding. This dataset provides rich supervision signals, describing a step-by-step multimodal reasoning process, thereby simplifying the task of visual grounding. We evaluate LynX on several object detection and visual grounding datasets, demonstrating strong performance in object detection, zero-shot localization and grounded reasoning while maintaining its original image and language understanding capabilities on seven standard benchmark datasets.

## item_id: m_0596

TITLE: Laplacian Networks: Bounding Indicator Function Smoothness for Neural Networks Robustness

ABSTRACT:   For the past few years, Deep Neural Network (DNN) robustness has become a question of paramount importance. As a matter of fact, in sensitive settings misclassification can lead to dramatic consequences. Such misclassifications are likely to occur when facing adversarial attacks, hardware failures or limitations, and imperfect signal acquisition. To address this question, authors have proposed different approaches aiming at increasing the robustness of DNNs, such as adding regularizers or training using noisy examples. In this paper we propose a new regularizer built upon the Laplacian of similarity graphs obtained from the representation of training data at each layer of the DNN architecture. This regularizer penalizes large changes (across consecutive layers in the architecture) in the distance between examples of different classes, and as such enforces smooth variations of the class boundaries. Since it is agnostic to the type of deformations that are expected when predicting with the DNN, the proposed regularizer can be combined with existing ad-hoc methods. We provide theoretical justification for this regularizer and demonstrate its effectiveness to improve robustness of DNNs on classical supervised learning vision datasets.


## item_id: m_0597

TITLE: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning

ABSTRACT: A promising approach for improving reasoning in large language models is to use process reward models (PRMs). PRMs provide feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains. With the goal of using PRMs to improve a *base* policy via test-time search and reinforcement learning (RL), we ask: ``How should we design process rewards?'' Our key insight is that, to be effective, the process reward for a step should measure 
 *progress*: a change in the likelihood of producing a correct response in the future, before and after taking the step, as measured under a *prover* policy distinct from the base policy. Such progress values can {distinguish} good and bad steps generated by the base policy, even though the base policy itself cannot.  Theoretically, we show that even weaker provers can improve the base policy, as long as they distinguish steps without being too misaligned with the base policy. Our results show that process rewards defined as progress under such provers improve the efficiency of exploration during test-time search and online RL. We empirically validate our claims by training  **process advantage verifiers (PAVs)** to measure progress under such provers and show that compared to ORM, they are >8% more accurate, and 1.5-5x more compute-efficient. Equipped with these insights, our PAVs enable **one of the first results** showing a 6x gain in sample efficiency for a policy trained using online RL with PRMs vs. ORMs.

## item_id: m_0598

TITLE: Sparsely-Connected Neural Networks: Towards Efficient VLSI Implementation of Deep Neural Networks

ABSTRACT: Recently deep neural networks have received considerable attention due to their ability to extract and represent high-level abstractions in data sets. Deep neural networks such as fully-connected and convolutional neural networks have shown excellent performance on a wide range of recognition and classification tasks. However, their hardware implementations currently suffer from large silicon area and high power consumption due to the their high degree of complexity. The power/energy consumption of neural networks is dominated by memory accesses, the majority of which occur in fully-connected networks. In fact, they contain most of the deep neural network parameters. In this paper, we propose sparsely-connected networks, by showing that the number of connections in fully-connected networks can be reduced by up to 90% while improving the accuracy performance on three popular datasets (MNIST, CIFAR10 and SVHN). We then propose an efficient hardware architecture based on linear-feedback shift registers to reduce the memory requirements of the proposed sparsely-connected networks. The proposed architecture can save up to 90% of memory compared to the conventional implementations of fully-connected neural networks. Moreover, implementation results show up to 84% reduction in the energy consumption of a single neuron of the proposed sparsely-connected networks compared to a single neuron of fully-connected neural networks.

## item_id: m_0599

TITLE: TimeSynth: A Framework for Uncovering Systematic Biases in Time Series Forecasting

ABSTRACT: Time series forecasting is a fundamental tool with wide-ranging applications, yet recent debates question whether complex nonlinear architectures truly outperform simple linear models. Prior claims of dominance of the linear model often stem from benchmarks that lack diverse temporal dynamics and employ biased evaluation protocols. We revisit this debate through TimeSynth, a structured framework that emulates key properties of real-world time series—including non-stationarity, periodicity, trends, and phase modulation—by creating synthesized signals whose parameters are derived from real-world time series. Evaluating four model families—Linear, Multi Layer Perceptrons (MLP), Convolutional Neural Networks (CNNs), and Transformers—we find a systematic bias in linear models: they collapse to simple oscillation regardless of signal complexity. Nonlinear models avoid this collapse and gain clear advantages as signal complexity increases. Notably, Transformers and CNN-based models exhibit slightly greater adaptability to complex modulated signals compared to MLPs. Beyond clean forecasting, the framework highlights robustness differences under distribution and noise shifts and removes biases of prior benchmarks by using independent instances for train, test, and validation for each signal family. Collectively, TimeSynth provides a principled foundation for understanding when different forecasting approaches succeed or fail, moving beyond oversimplified claims of model equivalence.

## item_id: m_0600

TITLE: Character-aware Attention Residual Network for Sentence Representation

ABSTRACT: Text classification in general is a well studied area. However, classifying short and noisy text remains challenging. Feature sparsity is a major issue. The quality of document representation here has a great impact on the classification accuracy. Existing methods represent text using bag-of-word model, with TFIDF or other weighting schemes. Recently word embedding and even document embedding are proposed to represent text. The purpose is to capture features at both word level and sentence level. However, the character level information are usually ignored. In this paper, we take word morphology and word semantic meaning into consideration, which are represented by character-aware embedding and word distributed embedding. By concatenating both character-level and word distributed embedding together and arranging words in order, a sentence representation matrix could be obtained. To overcome data sparsity problem of short text, sentence representation vector is then derived based on different views from sentence representation matrix. The various views contributes to the construction of an enriched sentence embedding. We employ a residual network on the sentence embedding to get a consistent and refined sentence representation. Evaluated on a few short text datasets, our model outperforms state-of-the-art models.
