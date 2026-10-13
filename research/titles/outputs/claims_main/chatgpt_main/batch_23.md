# Batch 23 — 100 items

## item_id: m_2201

TITLE: The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision

ABSTRACT: We propose the Neuro-Symbolic Concept Learner (NS-CL), a model that learns visual concepts, words, and semantic parsing of sentences without explicit supervision on any of them; instead, our model learns by simply looking at images and reading paired questions and answers. Our model builds an object-based scene representation and translates sentences into executable, symbolic programs. To bridge the learning of two modules, we use a neuro-symbolic reasoning module that executes these programs on the latent scene representation. Analogical to human concept learning, the perception module learns visual concepts based on the language description of the object being referred to. Meanwhile, the learned visual concepts facilitate learning new words and parsing new sentences. We use curriculum learning to guide the searching over the large compositional space of images and language. Extensive experiments demonstrate the accuracy and efficiency of our model on learning visual concepts, word representations, and semantic parsing of sentences. Further, our method allows easy generalization to new object attributes, compositions, language concepts, scenes and questions, and even new program domains. It also empowers applications including visual question answering and bidirectional image-text retrieval.

## item_id: m_2202

TITLE: Specialization of Sub-paths for Adaptive Depth Networks

ABSTRACT: We present a novel approach to anytime networks that can control network depths instantly at runtime to provide various accuracy-efficiency trade-offs. While controlling the depth of a network is an effective way to obtain actual inference speed-up, previous adaptive depth networks require either additional intermediate classifiers or decision networks, that are challenging to train properly. Unlike previous approaches, our adaptive depth networks require virtually no architectural changes from baseline networks. Instead, we introduce a novel training method that enforces some sub-paths of the baseline networks to have a special property, with which the sub-paths do not change the semantic level of input features, but only refine them to reduce prediction errors. Those specialized sub-paths can be skipped at test time, if needed, to save computation at marginal loss of prediction accuracy. We first formally present the rationale behind the sub-paths specialization, and based on that, we propose a simple and practical training method to specialize sub-paths for adaptive depth networks. While minimal architectural changes and training efforts are required, we demonstrate that our approach significantly outperforms non-adaptive baselines in various tasks, including ImageNet classification, COCO object detection and instance segmentation. Further, we show that the smallest sub-networks of our adaptive depth networks achieve competitive model compression effect compared to recent state-of-the-art techniques.

## item_id: m_2203

TITLE: A Statistical Framework for Personalized Federated Learning and Estimation: Theory, Algorithms, and Privacy

ABSTRACT: A distinguishing characteristic of federated learning is that the (local) client data could have statistical heterogeneity. This heterogeneity has motivated the design of personalized learning, where individual (personalized) models are trained, through collaboration. There have been various personalization methods proposed in literature, with seemingly very different forms and methods ranging from use of a single global model for local regularization and model interpolation, to use of multiple global models for personalized clustering, etc. In this work, we begin with a statistical framework that  unifies several different algorithms as well as suggest new algorithms.  We apply our framework to personalized estimation, and connect it to the classical empirical Bayes' methodology. We develop novel private personalized estimation under this framework. We then use our statistical framework to propose new personalized learning algorithms, including AdaPeD based on information-geometry regularization, which numerically outperforms several known algorithms. We develop privacy for personalized learning methods with guarantees for user-level privacy and composition. We numerically evaluate the performance as well as the privacy for both the estimation and learning problems, demonstrating the advantages of our proposed methods.

## item_id: m_2204

TITLE: Adversarial and Natural Perturbations for General Robustness

ABSTRACT: In this paper we aim to explore the general robustness of neural network classifiers by utilizing adversarial as well as natural perturbations. Different from previous works which mainly focus on studying the robustness of neural networks against adversarial perturbations, we also evaluate their robustness on natural perturbations before and after robustification. After standardizing the comparison between adversarial and natural perturbations, we demonstrate that although adversarial training improves the performance of the networks against adversarial perturbations, it leads to drop in the performance for naturally perturbed samples besides clean samples. In contrast, natural perturbations like elastic deformations, occlusions and wave does not only improve the performance against natural perturbations, but also lead to improvement in the performance for the adversarial perturbations. Additionally they do not drop the accuracy on the clean images.

## item_id: m_2205

TITLE: Learning Joint Wasserstein Auto-Encoders for Joint Distribution Matching

ABSTRACT: We study the joint distribution matching problem which aims at learning bidirectional mappings to match the joint distribution of two domains. This problem occurs in unsupervised image-to-image translation and video-to-video synthesis tasks, which, however, has two critical challenges: (i) it is difficult to exploit sufficient information from the joint distribution; (ii) how to theoretically and experimentally evaluate the generalization performance remains an open question. To address the above challenges, we propose a new optimization problem and design a novel Joint Wasserstein Auto-Encoders (JWAE) to minimize the Wasserstein distance of the joint distributions in two domains. We theoretically prove that the generalization ability of the proposed method can be guaranteed by minimizing the Wasserstein distance of joint distributions. To verify the generalization ability, we apply our method to unsupervised video-to-video synthesis by performing video frame interpolation and producing visually smooth videos in two domains, simultaneously. Both qualitative and quantitative comparisons demonstrate the superiority of our method over several state-of-the-arts.

## item_id: m_2206

TITLE: Toward learning better metrics for sequence generation training with policy gradient

ABSTRACT: Designing a metric manually for unsupervised sequence generation tasks, such as text generation, is essentially difficult. In a such situation, learning a metric of a sequence from data is one possible solution. The previous study, SeqGAN, proposed the framework for unsupervised sequence generation, in which a metric is learned from data, and a generator is optimized with regard to the learned metric with policy gradient, inspired by generative adversarial nets (GANs) and reinforcement learning. In this paper, we make two proposals to learn better metric than SeqGAN's: partial reward function and expert-based reward function training. The partial reward function is a reward function for a partial sequence of a certain length. SeqGAN employs a reward function for completed sequence only. By combining long-scale and short-scale partial reward functions, we expect a learned metric to be able to evaluate a partial correctness as well as a coherence of a sequence, as a whole. In expert-based reward function training, a reward function is trained to discriminate between an expert (or true) sequence and a fake sequence that is produced by editing an expert sequence. Expert-based reward function training is not a kind of GAN frameworks. This makes the optimization of the generator easier. We examine the effect of the partial reward function and expert-based reward function training on synthetic data and real text data, and show improvements over SeqGAN and the model trained with MLE. Specifically, whereas SeqGAN gains 0.42 improvement of NLL over MLE on synthetic data, our best model gains 3.02 improvement, and whereas SeqGAN gains 0.029 improvement of BLEU over MLE, our best model gains 0.250 improvement.

## item_id: m_2207

TITLE: Apprentice: Using Knowledge Distillation Techniques To Improve Low-Precision Network Accuracy

ABSTRACT: Deep learning networks have achieved state-of-the-art accuracies on computer vision workloads like image classification and object detection. The performant systems, however, typically involve big models with numerous parameters. Once trained, a challenging aspect for such top performing models is deployment on resource constrained inference systems -- the models (often deep networks or wide networks or both) are compute and memory intensive. Low precision numerics and model compression using knowledge distillation are popular techniques to lower both the compute requirements and memory footprint of these deployed models. In this paper, we study the combination of these two techniques and show that the performance of low precision networks can be significantly improved by using knowledge distillation techniques. We call our approach Apprentice and show state-of-the-art accuracies using ternary precision and 4-bit precision for many variants of ResNet architecture on ImageNet dataset. We study three schemes in which one can apply knowledge distillation techniques to various stages of the train-and-deploy pipeline.

## item_id: m_2208

TITLE: Interpretable Meta-Learning of Physical Systems

ABSTRACT: Machine learning methods can be a valuable aid in the scientific process, but they need to face challenging settings where data come from inhomogeneous experimental conditions. Recent meta-learning methods have made significant progress in multi-task learning, but they rely on black-box neural networks, resulting in high computational costs and limited interpretability. We introduce CAMEL, a new meta-learning architecture capable of learning efficiently from multiple environments, with an affine structure with respect to the learning task. We prove that CAMEL can identify the physical parameters of the system, enabling interpreable learning. We demonstrate the competitive generalization performance and the low computational cost of our method by comparing it to state-of-the-art algorithms on physical systems, ranging from toy models to complex, non-analytical systems. The interpretability of our method is illustrated with original applications to parameter identification and to adaptive control and system identification.

## item_id: m_2209

TITLE: Proto-CLIP: A Vision-Language Prototype Alignment Approach for Few-Shot Learning

ABSTRACT: We propose a novel framework for few-shot learning by leveraging large-scale vision-language models such as CLIP. Motivated by unimodal prototypical networks for few-shot learning, we introduce **Proto-CLIP** that utilizes image prototypes and text prototypes for few-shot learning. Specifically, Proto-CLIP adapts the image and text encoder embeddings from CLIP in a joint fashion using few-shot examples. The embeddings from the two encoders are used to compute the respective prototypes of image classes for classification. During adaptation, we propose aligning the image and text prototypes of the corresponding classes. Such alignment is beneficial for few-shot classification due to the reinforced contributions from both types of prototypes. **Proto-CLIP has both training-free and fine-tuned variants. We demonstrate the effectiveness of our method by conducting experiments on benchmark datasets for few-shot learning, as well as in the real world for robot perception.** Code will be released upon acceptance.

## item_id: m_2210

TITLE: NeRT: Implicit Neural Representation for Time Series

ABSTRACT: Time series is one of the most fundamental data types in real-world environments and there have been many different deep-learning models to effectively handle time series data, ranging from recurrent neural networks to Transformers to differential equation-based models. These existing models, however, tend to underperform due to irregular measurements, sensitivity to hyper-parameters (e.g., a window size), to name a few. Modeling time series as a continuous-in-time signal via implicit neural representations (INRs) can be an alternative approach to overcome such limitations. However, naïve adoptions of existing INR frameworks toward time series do not yield promising outcomes. To address this, we propose NeRT, a novel class of INRs tailored to handle time-series data; the core ideas are to design a new coordinate system, to employ learnable Fourier features, and to model periodic and scale components of time series separately. Thanks to the inherent characteristics of INRs, our model can learn from both regular and irregular time series in a continuous-time manner and perform time series forecasting and imputation at the same time with a single trained model. Moreover, we show that NeRT can be efficiently parameterized via latent modulation. Through extensive experiments with real-world and scientific datasets, we demonstrate that NeRT significantly outperforms baselines including popular INR-based methods and previous time series models.

## item_id: m_2211

TITLE: Provably efficient multi-task Reinforcement Learning in large state spaces

ABSTRACT: We study multi-task Reinforcement Learning where shared knowledge among different environments is distilled to enable scalable generalization to a variety of problem instances. In the context of general function approximation, Markov Decision Process (MDP) with low Bilinear rank encapsulates a wide range of structural conditions that permit polynomial sample complexity in large state spaces, where the Bellman errors are related to bilinear forms of features with low intrinsic dimensions. To achieve multi-task learning in MDPs, we propose online representation learning algorithms to capture the shared features in the different task-specific bilinear forms. We show that in the presence of low-rank structures in the features of the bilinear forms, the algorithms benefit from sample complexity improvements compared to single-task learning. Therefore, we achieve the first sample efficient multi-task reinforcement learning algorithm with general function approximation.

## item_id: m_2212

TITLE: Auto-Encoding Sequential Monte Carlo

ABSTRACT: We build on auto-encoding sequential Monte Carlo (AESMC): a method for model and proposal learning based on maximizing the lower bound to the log marginal likelihood in a broad family of structured probabilistic models. Our approach relies on the efficiency of sequential Monte Carlo (SMC) for performing inference in structured probabilistic models and the flexibility of deep neural networks to model complex conditional probability distributions. We develop additional theoretical insights and introduce a new training procedure which improves both model and proposal learning. We demonstrate that our approach provides a fast, easy-to-implement and scalable means for simultaneous model learning and proposal adaptation in deep generative models.

## item_id: m_2213

TITLE: Generalizing and Decoupling Neural Collapse via Hyperspherical Uniformity Gap

ABSTRACT: The neural collapse (NC) phenomenon describes an underlying geometric symmetry for deep neural networks, where both deeply learned features and classifiers converge to a simplex equiangular tight frame. It has been shown that both cross-entropy loss and mean square error can provably lead to NC. We remove NC's key assumption on the feature dimension and the number of classes, and then present a generalized neural collapse (GNC) hypothesis that effectively subsumes the original NC. Inspired by how NC characterizes the training target of neural networks, we decouple GNC into two objectives: minimal intra-class variability and maximal inter-class separability. We then use hyperspherical uniformity (which characterizes the degree of uniformity on the unit hypersphere) as a unified framework to quantify these two objectives. Finally, we propose a general objective -- hyperspherical uniformity gap (HUG), which is defined by the difference between inter-class and intra-class hyperspherical uniformity. HUG not only provably converges to GNC, but also decouples GNC into two separate objectives. Unlike cross-entropy loss that couples intra-class compactness and inter-class separability, HUG enjoys more flexibility and serves as a good alternative loss function. Empirical results show that HUG works well in terms of generalization and robustness.

## item_id: m_2214

TITLE: A STRUCTURED SELF-ATTENTIVE SENTENCE EMBEDDING

ABSTRACT: This paper proposes a new model for extracting an interpretable sentence embedding by introducing self-attention. Instead of using a vector, we use a 2-D matrix to represent the embedding, with each row of the matrix attending on a different part of the sentence. We also propose a self-attention mechanism and a special regularization term for the model. As a side effect, the embedding comes with an easy way of visualizing what specific parts of the sentence are encoded into the embedding. We evaluate our model on 3 different tasks: author profiling, sentiment classification and textual entailment. Results show that our model yields a significant performance gain compared to other sentence embedding methods in all of the 3 tasks.

## item_id: m_2215

TITLE: RAG$^C$: Towards Copyright Protection for Knowledge Bases of Retrieval-augmented Language Models

ABSTRACT: Large language models (LLMs) are increasingly integrated into real-world applications through retrieval-augmented generation (RAG) mechanisms to supplement their responses with up-to-date and domain-specific knowledge. However, the valuable and often proprietary nature of the knowledge bases used in RAG introduces the risk of unauthorized usage by adversaries. Existing methods that can be generalized as watermarking techniques to protect these knowledge bases typically involve backdoor or poisoning attacks, which introduce harmful behaviors (\eg, generating incorrect outputs for verification), thereby compromising the LLM's reliability. To address these challenges, we propose \name{} for harmless copyright protection of knowledge bases. Instead of manipulating the final output, \name{} implants distinct verification behaviors in the space of chain-of-thought (CoT) reasoning, maintaining the correctness of the final answer. Our approach involves three main stages: (1) \textbf{Generating CoTs}: For each verification question, we generate two CoTs, including a target CoT for building watermark behaviors; (2) \textbf{Optimizing Watermark Phrases and Target CoTs}: We optimize them to minimize retrieval errors under the black-box setting of suspicious LLM, ensuring that the watermarked verification queries activate the target CoTs without being activated in non-watermarked ones; (3) \textbf{Ownership Verification}: We exploit a pairwise Wilcoxon test to statistically verify whether a suspicious LLM is augmented with the protected knowledge base by comparing its responses to watermarked and benign verification queries. Our experiments on diverse benchmarks demonstrate that \name{} effectively protects knowledge bases against unauthorized usage while preserving the integrity and performance of the RAG.

## item_id: m_2216

TITLE: Dynamics-inspired Neuromorphic Representation Learning

ABSTRACT: This paper investigates the dynamics-inspired neuromorphic architecture for neural representation and learning following Hamilton's principle. The proposed approach converts weight-based neural structure to its dynamics-based form that consists of finite sub-models, whose mutual relations measured by computing path integrals amongst their dynamic states are equivalent to the typical neural weights. The feedback signals interpreted as stress forces amongst sub-models push them to move based on the entropy-reduction process derived from the Euler-Lagrange equations. We first train a dynamics-based neural model from scratch and observe that this model outperforms its corresponding feedforward neural networks on MNIST dataset. Then we convert several pre-trained neural structures (e.g., DenseNet, ResNet, Transformers, etc.) into dynamics-based forms, followed by fine-tuning via entropy-reduction to obtain the stabilized dynamic states. We observe consistent improvements of these transformed models on the ImageNet dataset in terms of computational complexity, the number of trainable units, testing accuracy, and robustness. Moreover, we demonstrate the correlation between the performance of a neural system and its structural entropy.

## item_id: m_2217

TITLE: Deep automodulators

ABSTRACT: We introduce a novel autoencoder model that deviates from traditional autoencoders by using the full latent vector to independently modulate each layer in the decoder. We demonstrate how such an 'automodulator' allows for a principled approach to enforce latent space disentanglement, mixing of latent codes, and a straightforward way to utilize prior information that can be construed as a scale-specific invariance. Unlike GANs, autoencoder models can directly operate on new real input samples. This makes our model directly suitable for applications involving real-world inputs. As the architectural backbone, we extend recent generative autoencoder models that retain input identity and image sharpness at high resolutions better than VAEs. We show that our model achieves state-of-the-art latent space disentanglement and achieves high quality and diversity of output samples, as well as faithfulness of reconstructions.

## item_id: m_2218

TITLE: Bayesian Neural Network Priors Revisited

ABSTRACT: Isotropic Gaussian priors are the de facto standard for modern Bayesian neural network inference. However, it is unclear whether these priors accurately reflect our true beliefs about the weight distributions or give optimal performance. To find better priors, we study summary statistics of neural network weights in networks trained using stochastic gradient descent (SGD). We find that convolutional neural network (CNN) and ResNet weights display strong spatial correlations, while fully connected networks (FCNNs) display heavy-tailed weight distributions. We show that building these observations into priors can lead to improved performance on a variety of image classification datasets. Surprisingly, these priors mitigate the cold posterior effect in FCNNs, but slightly increase the cold posterior effect in ResNets.

## item_id: m_2219

TITLE: Mitigating Adversarial Effects Through Randomization

ABSTRACT: Convolutional neural networks have demonstrated high accuracy on various tasks in recent years. However, they are extremely vulnerable to adversarial examples. For example, imperceptible perturbations added to clean images can cause convolutional neural networks to fail. In this paper, we propose to utilize randomization at inference time to mitigate adversarial effects. Specifically, we use two randomization operations: random resizing, which resizes the input images to a random size, and random padding, which pads zeros around the input images in a random manner.  Extensive experiments demonstrate that the proposed randomization method is very effective at defending against both single-step and iterative attacks. Our method provides the following advantages: 1) no additional training or fine-tuning, 2) very few additional computations, 3) compatible with other adversarial defense methods. By combining the proposed randomization method with an adversarially trained model,  it achieves a normalized score of 0.924 (ranked No.2 among 107 defense teams)  in the NIPS 2017 adversarial examples defense challenge, which is far better than using adversarial training alone with a normalized score of 0.773 (ranked No.56). The code is public available at https://github.com/cihangxie/NIPS2017_adv_challenge_defense.

## item_id: m_2220

TITLE: RenderGAN: Generating Realistic Labeled Data

ABSTRACT: Deep Convolutional Neuronal Networks (DCNNs) are showing remarkable performance on many computer vision tasks.  Due to their large parameter space, they require many labeled samples when trained in a supervised setting. The costs of annotating data manually can render the use of DCNNs infeasible.  We present a novel framework called RenderGAN that can generate large amounts of realistic, labeled images by combining a 3D model and the Generative Adversarial Network framework. In our approach, image augmentations (e.g. lighting, background, and detail) are learned from unlabeled data such that the generated images are strikingly realistic while preserving the labels known from the 3D model.  We apply the RenderGAN framework to generate images of barcode-like markers that are attached to honeybees. Training a DCNN on data generated by the RenderGAN yields considerably better performance than training it on various baselines. 

## item_id: m_2221

TITLE: Learning to reason over visual objects

ABSTRACT: A core component of human intelligence is the ability to identify abstract patterns inherent in complex, high-dimensional perceptual data, as exemplified by visual reasoning tasks such as Raven’s Progressive Matrices (RPM). Motivated by the goal of designing AI systems with this capacity, recent work has focused on evaluating whether neural networks can learn to solve RPM-like problems. Previous work has generally found that strong performance on these problems requires the incorporation of inductive biases that are specific to the RPM problem format, raising the question of whether such models might be more broadly useful. Here, we investigated the extent to which a general-purpose mechanism for processing visual scenes in terms of objects might help promote abstract visual reasoning. We found that a simple model, consisting only of an object-centric encoder and a transformer reasoning module, achieved state-of-the-art results on both of two challenging RPM-like benchmarks (PGM and I-RAVEN), as well as a novel benchmark with greater visual complexity (CLEVR-Matrices). These results suggest that an inductive bias for object-centric processing may be a key component of abstract visual reasoning, obviating the need for problem-specific inductive biases.

## item_id: m_2222

TITLE: The Curious Case of In-Training Compression of State Space Models

ABSTRACT: State Space Models (SSMs), developed to tackle long sequence modeling tasks efficiently, offer both parallelizable training and fast inference. At their core are recurrent dynamical systems that maintain a hidden state, with update costs scaling with the state dimension. A key design challenge is striking the right balance between maximizing expressivity and limiting this computational burden. Control theory, and more specifically Hankel singular value analysis, provides a potent framework for the measure of energy for each state, as well as the balanced truncation of the original system down to a smaller representation with performance guarantees. Leveraging the eigenvalue stability properties of Hankel matrices, we apply this lens to SSMs $\textit{during training}$, where only dimensions of high influence are identified and preserved. Our approach, CompreSSM, applies to Linear Time-Invariant SSMs such as Linear Recurrent Units, but is also extendable to selective models. Experiments show that in-training reduction significantly accelerates optimization while preserving expressivity, with compressed models retaining task-critical structure lost by models trained directly at smaller dimension. In other words, SSMs that begin large and shrink during training achieve computational efficiency while maintaining higher performance. Project code is available at https://github.com/camail-official/compressm.

## item_id: m_2223

TITLE: The Natural Language Decathlon: Multitask Learning as Question Answering

ABSTRACT: Deep learning has improved performance on many natural language processing (NLP) tasks individually.
However, general NLP models cannot emerge within a paradigm that focuses on the particularities of a single metric, dataset, and task.
We introduce the Natural Language Decathlon (decaNLP), a challenge that spans ten tasks:
question answering, machine translation, summarization, natural language inference, sentiment analysis, semantic role labeling, relation extraction, goal-oriented dialogue, semantic parsing, and commonsense pronoun resolution.
We cast all tasks as question answering over a context.
Furthermore, we present a new multitask question answering network (MQAN) that jointly learns all tasks in decaNLP without any task-specific modules or parameters more effectively than sequence-to-sequence and reading comprehension baselines.
MQAN shows improvements in transfer learning for machine translation and named entity recognition, domain adaptation for sentiment analysis and natural language inference, and zero-shot capabilities for text classification.
We demonstrate that the MQAN's multi-pointer-generator decoder is key to this success and that performance further improves with an anti-curriculum training strategy.
Though designed for decaNLP, MQAN also achieves state of the art results on the WikiSQL semantic parsing task in the single-task setting. 
We also release code for procuring and processing data, training and evaluating models, and reproducing all experiments for decaNLP.

## item_id: m_2224

TITLE: A-Loc: Efficient Alternating Iterative Methods for Locating the $k$ Largest/Smallest Elements in a Factorized Tensor

ABSTRACT: Tensors, especially higher-order tensors, are typically represented in low-rank formats to preserve the main information of the high-dimensional data while saving memory space.  Locating the largest/smallest elements in a tensor with the low-rank format is a fundamental task in a large variety of applications. However, existing algorithms often suffer from low computational efficiency or poor accuracy. In this work, we propose a general continuous optimization model for this task, on top of which an alternating iterative method combined with the maximum block increasing (MBI) approach is presented. Then we develop a novel block-search strategy to further improve the accuracy. The theoretical analysis of the convergence behavior of the alternating iterative algorithm is also provided. Numerical experiments with tensors from synthetic and real-world applications demonstrate that our proposed algorithms achieve significant improvements in both accuracy and efficiency over the existing works.

## item_id: m_2225

TITLE: Few-shot Cross-domain Image Generation via Inference-time Latent-code Learning

ABSTRACT: In this work, our objective is to adapt a Deep generative model trained on a large-scale source dataset to multiple target domains with scarce data. Specifically, we focus on adapting a pre-trained Generative Adversarial Network (GAN) to a target domain without re-training the generator. Our method draws the motivation from the fact that out-of-distribution samples can be `embedded' onto the latent space of a pre-trained source-GAN. We propose to train a small latent-generation network during the inference stage, each time a  batch of target samples is to be generated. These target latent codes are fed to the source-generator to obtain  novel target samples. Despite using the same small set of target samples and the source generator, multiple independent training episodes of the latent-generation network results in the diversity of the generated target samples. Our method, albeit simple, can be used to generate data from multiple target distributions using a generator trained on a single source distribution. We demonstrate the efficacy of our surprisingly simple method in generating multiple target datasets with only a single source generator and a few target samples.

## item_id: m_2226

TITLE: Stability of Stochastic Gradient Method with Momentum for Strongly Convex Loss Functions

ABSTRACT: While momentum-based methods, in conjunction with the stochastic gradient descent, are widely used when training machine learning models, there is little theoretical understanding on the generalization error of such methods. In practice, the momentum parameter is often chosen in a heuristic fashion with little theoretical guidance. In this work, we use the framework of algorithmic stability to provide an upper-bound on the generalization error for the class of strongly convex loss functions, under mild technical assumptions. Our bound decays to zero inversely with the size of the training set, and increases as the momentum parameter is increased. We also develop an upper-bound on the expected true risk,  in terms of the number of training steps, the size of the training set, and the momentum parameter.

## item_id: m_2227

TITLE: EqCo:   Equivalent Rules for Self-supervised Contrastive Learning

ABSTRACT: In this paper, we propose a method, named EqCo (Equivalent Rules for Contrastive Learning), to make self-supervised learning irrelevant to the number of negative samples in the contrastive learning framework. Inspired by the InfoMax principle, we point that the margin term in contrastive loss needs to be adaptively scaled according to the number of negative pairs in order to keep steady mutual information bound and gradient magnitude. EqCo bridges the performance gap among a wide range of negative sample sizes, so that for the first time, we can use only a few negative pairs (e.g. 16 per query) to perform self-supervised contrastive training on large-scale vision datasets like ImageNet, while with almost no accuracy drop. This is quite a contrast to the widely used large batch training or memory bank mechanism in current practices. Equipped with EqCo, our simplified MoCo (SiMo) achieves comparable accuracy with MoCo v2 on ImageNet (linear evaluation protocol) while only involves 16 negative pairs per query instead of 65536, suggesting that large quantities of negative samples might not be a critical factor in contrastive learning frameworks.

## item_id: m_2228

TITLE: Introducing Active Learning for CNN under the light of Variational Inference

ABSTRACT: One main concern of the deep learning community is to increase the capacity of
representation of deep networks by increasing their depth. This requires to scale
up the size of the training database accordingly. Indeed a major intuition lies in
the fact that the depth of the network and the size of the training set are strongly
correlated. However recent works tend to show that deep learning may be handled
with smaller dataset as long as the training samples are carefully selected (let us
mention for instance curriculum learning). In this context we introduce a scalable
and efficient active learning method that can be applied to most neural networks,
especially Convolutional Neural Networks (CNN). To the best of our knowledge,
this paper is the first of its kind to design an active learning selection scheme based
on a variational inference for neural networks. We also deduced a formulation of
the posterior and prior distributions of the weights using statistical knowledge on
the Maximum Likelihood Estimator.
We describe our strategy to come up with our active learning criterion. We assess its
consistency by checking the accuracy obtained by successive active learning steps
on two benchmark datasets MNIST and USPS. We also demonstrate its scalability
towards increasing training set size.

## item_id: m_2229

TITLE: DSTGN: Decoupled SpatioTemporal Graph Network for Multi-scenario Dynamics Learning

ABSTRACT: Machine Learning (ML) methods have played a pivotal role in a wide range of dynamics tasks, such as physical simulation, multi-modal interaction, and real-time prediction. Among them, Graph Neural Networks (GNNs) have emerged as effective surrogates for numerical solvers, thanks to their ability to model pairwise interactions between nodes and their neighboring edges. However, the inherent tendency of GNNs to perform local aggregation limits their expressiveness in capturing intricate global interactions. To address this limitation, we propose a general framework, Decoupled SpatioTemporal Graph Network (DSTGN), to enhance prediction performance across various downstream tasks. DSTGN enhances latent feature representations by decoupling spatial connectivity in both the physical and latent spaces. In parallel, it introduces a learnable temporal integration mechanism that decouples inter-step dynamics at each latent layer, effectively mitigating error accumulation during autoregressive inference. Extensive experiments on multiple types of benchmarks demonstrate that DSTGN consistently outperforms existing baselines in both accuracy and generalization, across regular and irregular domains, as well as static and dynamic meshes.

## item_id: m_2230

TITLE: Generative Pretrained Embedding and Hierarchical Representation to Unlock Human Rhythm in Activities of Daily Living

ABSTRACT: Within the evolving landscape of smart homes, the precise recognition of daily living activities using ambient sensor data stands paramount. This paper not only aims to bolster existing algorithms by evaluating two distinct pretrained embeddings suited for ambient sensor activations but also introduces a novel hierarchical architecture. We delve into an architecture anchored on Transformer Decoder-based pre-trained embeddings, reminiscent of the GPT design, and contrast it with the previously established state-of-the-art (SOTA) ELMo embeddings for ambient sensors. Our proposed hierarchical structure leverages the strengths of each pre-trained embedding, enabling the discernment of activity dependencies and sequence order, thereby enhancing classification precision. To further refine recognition, we incorporate into our proposed architecture an hour-of-the-day embedding. Empirical evaluations underscore the preeminence of the Transformer Decoder embedding in classification endeavors. Additionally, our innovative hierarchical design significantly bolsters the efficacy of both pre-trained embeddings, notably in capturing inter-activity nuances. The integration of temporal aspects subtly but distinctively augments classification, especially for time-sensitive activities. In conclusion, our GPT-inspired hierarchical approach, infused with temporal insights, outshines the SOTA ELMo benchmark.

## item_id: m_2231

TITLE: Deep Rewiring: Training very sparse deep networks

ABSTRACT: Neuromorphic hardware tends to pose limits on the connectivity of deep networks that one can run on them. But also generic hardware and software implementations of deep learning run more efficiently for sparse networks. Several methods exist for pruning connections of a neural network after it was trained without connectivity constraints. We present an algorithm, DEEP R, that enables us to train directly a sparsely connected neural network. DEEP R automatically rewires the network during supervised training so that connections are there where they are most needed for the task, while its total number is all the time strictly bounded. We demonstrate that DEEP R can be used to train very sparse feedforward and recurrent neural networks on standard benchmark tasks with just a minor loss in performance. DEEP R is based on a rigorous theoretical foundation that views rewiring as stochastic sampling of network configurations from a posterior.

## item_id: m_2232

TITLE: Rethinking deep active learning: Using unlabeled data at model training

ABSTRACT: Active learning typically focuses on training a model on few labeled examples alone, while unlabeled ones are only used for acquisition. In this work we depart from this setting by using both labeled and unlabeled data during model training across active learning cycles. We do so by using unsupervised feature learning at the beginning of the active learning pipeline and semi-supervised learning at every active learning cycle, on all available data. The former has not been investigated before in active learning, while the study of latter in the context of deep learning is scarce and recent findings are not conclusive with respect to its benefit. Our idea is orthogonal to acquisition strategies by using more data, much like ensemble methods use more models. By systematically evaluating on a number of popular acquisition strategies and datasets, we find that the use of unlabeled data during model training brings a spectacular accuracy improvement in image classification, compared to the differences between acquisition strategies. We thus explore smaller label budgets, even one label per class. 

## item_id: m_2233

TITLE: Fourier Neural Operator for Parametric Partial Differential Equations

ABSTRACT: The classical development of neural networks has primarily focused on learning mappings between finite-dimensional Euclidean spaces.  Recently, this has been generalized to neural operators that learn mappings between function spaces. For partial differential equations (PDEs), neural operators directly learn the mapping from any functional parametric dependence to the solution. Thus, they learn an entire family of PDEs, in contrast to classical methods which solve one instance of the equation. In this work, we formulate a new neural operator by parameterizing the integral kernel directly in Fourier space, allowing for an expressive and efficient architecture. We perform experiments on Burgers' equation, Darcy flow, and Navier-Stokes equation. The Fourier neural operator is the first ML-based method to successfully model turbulent flows with zero-shot super-resolution. It is up to three orders of magnitude faster compared to traditional PDE solvers. Additionally, it achieves superior accuracy compared to previous learning-based solvers under fixed resolution.

## item_id: m_2234

TITLE: Clustering Structure Identification With Ordering Graph

ABSTRACT: In machine learning, data is often presented in the form of a graph or similarity (or distance) values between samples. Graph-based clustering methods such as spectral clustering are defined for general weighted graphs to identify the clustering structure. Graph construction research has developed significantly for decades, but the graph-based partition study still requires more attention because of its poor performance. For example, spectral clustering needs a post-processing (e.g., K-Means) step to uncover the clustering indicators. Yet, K-Means is sensitive to the initial center setting and easily falls into a local optimum. In this paper, we investigate a new type of graph-based clustering approach. Firstly, we introduce a new algorithm for the purpose of cluster analysis which does not explicitly produce a clustering of a dataset but instead creates an augmented graph representing its density-based ordered clustering structure. This ordered graph contains information equivalent to density-based clustering corresponding to a broad range of parameter settings. Secondly, we found that the graph matrix is shown in a block-diagonal form because of the nature of ordering. We propose a partition method to learn the graph matrix's block-diagonal structure and identify the clustering directly. The global optimality is guaranteed theoretically. We test the proposed method on synthetic datasets and five high-dimensional datasets. Experimental results show that the proposed method outperforms state-of-the-art graph-based clustering methods and improves their performance by roughly 10%-50%. 

## item_id: m_2235

TITLE: Synthesizing realistic neural population activity patterns using Generative Adversarial Networks

ABSTRACT: The ability to synthesize realistic patterns of neural activity is crucial for studying neural information processing. Here we used the Generative Adversarial Networks (GANs) framework to simulate the concerted activity of a population of neurons.
We adapted the Wasserstein-GAN variant to facilitate the generation of unconstrained neural population activity patterns while still benefiting from parameter sharing in the temporal domain.
We demonstrate that our proposed GAN, which we termed Spike-GAN, generates spike trains that match accurately the first- and second-order statistics of datasets of tens of neurons and also approximates well their higher-order statistics. We applied Spike-GAN to a real dataset recorded from salamander retina and showed that it performs as well as state-of-the-art approaches based on the maximum entropy and the dichotomized Gaussian frameworks. Importantly, Spike-GAN does not require to specify a priori the statistics to be matched by the model, and so constitutes a more flexible method than these alternative approaches.
Finally, we show how to exploit a trained Spike-GAN  to construct 'importance maps' to detect the most relevant statistical structures present in a spike train. 
Spike-GAN provides a powerful, easy-to-use technique for generating realistic spiking neural activity and for describing the most relevant features of the large-scale neural population recordings studied in modern systems neuroscience.


## item_id: m_2236

TITLE: Towards Understanding The Winner-Take-Most Behavior Of Neural Network Representations

ABSTRACT: Understanding the generalization ability of neural networks is a long-standing goal of the machine learning community.
Despite sufficient representational complexity to memorize large data sets, modern neural networks are able to learn solutions to their optimization problem that generalize well to unseen data.
In this paper, we explore how the neuron-level representations of the training samples in a data set can be analyzed to differentiate between networks that have learned to generalize and networks that merely memorize.
For this purpose, we introduce a synthetic data set specifically crafted to allow for an easy comparison of how networks treat simple patterns.
We show that comparing how training samples presenting different patterns are represented by neurons can provide key insights as to what differentiates memorized and generalized networks.
We observe that the training process progressively increases the average pre-activation of the most activated patterns of a class and decreases the average pre-activation of the least activated patterns of said class in each neuron, a winner-take-most phenomenon.
In order to solve the classification problem, the network seems to apply a divide-and-conquer strategy, where different neurons specialize in the classification of different patterns of a class.
We also explore the effect of various parameters of our experimental configuration on these findings and describe three necessary conditions for it to appear.
Finally, we provide an intuitive explanation of why this phenomenon occurs, drawing links with existing work on sample difficulty, coherent gradients, and implicit clustering.

## item_id: m_2237

TITLE: On the complexity of nonsmooth automatic differentiation

ABSTRACT: Using the notion of conservative gradient, we provide a simple model to estimate the computational costs of the backward and forward modes of algorithmic differentiation for a wide class of nonsmooth programs. The complexity overhead of the backward mode turns out to be independent of the dimension when using programs with locally Lipschitz semi-algebraic or definable elementary functions. This extends considerably the Baur-Strassen's smooth cheap gradient principle. We illustrate our results by establishing fast backpropagation results of conservative gradients through feedforward neural networks with standard activation and  loss functions. Nonsmooth backpropagation's cheapness contrasts with concurrent forward approaches, which have, to this day, dimensional-dependent worst case  overhead estimates. We provide further results suggesting the superiority of backward propagation of conservative gradients. Indeed, we relate the complexity of computing a large number of directional derivatives to that of matrix multiplication, and we show that finding two subgradients in the Clarke subdifferential of a function is a NP-hard problem.

## item_id: m_2238

TITLE: Combining Learned Representations for Combinatorial Optimization

ABSTRACT: We propose a new approach to combine Restricted Boltzmann Machines (RBMs) that can be used to solve combinatorial optimization problems. This allows synthesis of larger models from smaller RBMs that have been pretrained, thus effectively bypassing the problem of learning in large RBMs, and creating a system able to model a large, complex multi-modal space. We validate this approach by using learned representations to create ``invertible boolean logic'', where we can use Markov chain Monte Carlo (MCMC) approaches to find the solution to large scale boolean satisfiability problems and show viability towards other combinatorial optimization problems. Using this method, we are able to solve 64 bit addition based problems, as well as factorize 16 bit numbers. We find that these combined representations can provide a more accurate result for the same sample size as compared to a fully trained model.  

## item_id: m_2239

TITLE: Enhancing LLM's interpretability for time series via multi-level aligned embeddings

ABSTRACT: The adaptation of large language models (LLMs) to time series forecasting poses unique challenges, as time series data is continuous in nature, while LLMs operate on discrete tokens. Despite the success of LLMs in natural language processing (NLP) and other structured domains, aligning time series data with language-based representations while maintaining both predictive accuracy and interpretability remains a significant hurdle. Existing methods have attempted to reprogram time series data into text-based forms, but these often fall short in delivering meaningful, interpretable results.
In this paper, we propose a multi-text alignment framework for time series forecasting using LLMs that not only improves prediction accuracy but also enhances the interpretability of time series representations. Our method decomposes time series into trend, seasonality, and residual components, which are then reprogrammed into component-specific text representations. 
We introduce a multi-level alignment mechanism, where component-specific embeddings are aligned with pre-trained word tokens, enabling more interpretable forecasts. 
Experiments on multiple datasets demonstrate that our method outperforms state-of-the-art models in accuracy while providing good interpretability.

## item_id: m_2240

TITLE: FairCal: Fairness Calibration for Face Verification

ABSTRACT: Despite being widely used, face recognition models suffer from bias: the probability of a false positive (incorrect face match) strongly depends on sensitive attributes such as the ethnicity of the face. As a result, these models can disproportionately and negatively impact minority groups, particularly when used by law enforcement. The majority of bias reduction methods have several drawbacks: they use an end-to-end retraining approach, may not be feasible due to privacy issues, and often reduce accuracy. An alternative approach is post-processing methods that build fairer decision classifiers using the features of pre-trained models, thus avoiding the cost of retraining. However, they still have drawbacks: they reduce accuracy (AGENDA, FTC), or require retuning for different false positive rates (FSN). In this work, we introduce the Fairness Calibration (FairCal) method, a post-training approach that simultaneously: (i) increases model accuracy (improving the state-of-the-art), (ii) produces fairly-calibrated probabilities, (iii) significantly reduces the gap in the false positive rates, (iv) does not require knowledge of the sensitive attribute, and (v) does not require retraining, training an additional model or retuning. We apply it to the task of Face Verification, and obtain state-of-the-art results with all the above advantages.

## item_id: m_2241

TITLE: Trajectory growth through random deep ReLU networks

ABSTRACT: This paper considers the growth in the length of one-dimensional trajectories as they are passed through deep ReLU neural networks,  which, among other things, is  one measure of the expressivity of deep networks. We generalise existing  results, providing an alternative, simpler method for lower bounding expected trajectory growth through random networks, for a more general class of weights distributions, including sparsely connected  networks. We illustrate this approach by deriving bounds for sparse-Gaussian, sparse-uniform, and sparse-discrete-valued random nets. We prove that trajectory growth can remain exponential in depth with these new distributions, including their sparse variants, with the sparsity parameter appearing in the base of the exponent.

## item_id: m_2242

TITLE: Graph View-Consistent Learning Network

ABSTRACT: Recent years, methods based on neural networks have made great achievements in solving large and complex graph problems. However, high efficiency of these methods depends on large training and validation sets, while the acquisition of ground-truth labels is expensive and time-consuming. In this paper, a graph view-consistent learning network (GVCLN) is specially designed for the semi-supervised learning when the number of the labeled samples is very small. We fully exploit the neighborhood aggregation capability of GVCLN and use dual views to obtain different representations. Although the two views have different viewing angles, their observation objects are the same, so their observation representations need to be consistent. For view-consistent representations between two views, two loss functions are designed besides a supervised loss. The supervised loss uses the known labeled set, while a view-consistent loss is applied to the two views to obtain the consistent representation and a pseudo-label loss is designed by using the common high-confidence predictions. GVCLN with these loss functions can obtain the view-consistent representations of the original feature. We also find that preprocessing the node features with specific filter before training is good for subsequent classification tasks. Related experiments have been done on the three citation network datasets of Cora, Citeseer, and PubMed. On several node classification tasks, GVCLN achieves state-of-the-art performance.

## item_id: m_2243

TITLE: Learning Human Habits with Rule-Guided Active Inference

ABSTRACT: Humans navigate daily life by combining two modes of behavior: deliberate planning in novel situations and fast, automatic responses in familiar ones. Modeling human decision-making therefore requires capturing how people switch between these modes. We present a framework for learning human habits with rule-guided active inference, extending the view of the brain as a prediction machine that minimizes mismatches between expectations and observations, and computationally modeling of human(-like) behavior and habits. In our approach, habits emerge as symbolic rules that serve as compact, interpretable shortcuts for action. To learn these rules alongside the human models, we design a biologically inspired wake--sleep algorithm. In the wake phase, the agent engages in active inference on real trajectories: reconstructing states, updating beliefs, and harvesting candidate rules that reliably reduce free energy. In the sleep phase, the agent performs generative replay with its world model, refining parameters and consolidating or pruning rules by minimizing joint free energy. This alternating rule–model consolidation lets the agent build a reusable habit library while preserving the flexibility to plan. Experiments on basketball player movements, car-following behavior, medical diagnosis, and visual game strategy demonstrate that our framework improves predictive accuracy and efficiency compared to logic-based, deep learning, LLM-based, model-based RL, and prior active inference baselines, while producing interpretable rules that mirror human-like habits.

## item_id: m_2244

TITLE: An inference-based policy gradient method for learning options

ABSTRACT: In the pursuit of increasingly intelligent learning systems, abstraction plays a vital role in enabling sophisticated decisions to be made in complex environments. The options framework provides formalism for such abstraction over sequences of decisions.  However most models require that options be given a priori, presumably specified by hand, which is neither efficient, nor scalable. Indeed, it is preferable to learn options directly from interaction with the environment. Despite several efforts, this remains a difficult problem: many approaches require access to a model of the environmental dynamics, and inferred options are often not interpretable, which limits our ability to explain the system behavior for verification or debugging purposes.  In this work we develop a novel policy gradient method for the automatic learning of policies with options.  This algorithm uses inference methods to simultaneously improve all of the options available to an agent, and thus can be employed in an off-policy manner, without observing option labels. Experimental results show that the options learned can be interpreted. Further, we find that the method presented here is more sample efficient than existing methods, leading to faster and more stable learning of policies with options.

## item_id: m_2245

TITLE: Functional Risk Minimization

ABSTRACT: In this work, we break the classic assumption of data coming from a single function $f_{\theta^*}(x)$ followed by some noise in output space $p(y|f_{\theta^*}(x))$. Instead, we model each data point $(x_i,y_i)$ as coming from its own function $f_{\theta_i}$. We show that this model subsumes Empirical Risk Minimization for many common loss functions, and provides an avenue for more realistic noise processes. We derive Functional Risk Minimization~(FRM), a general framework for scalable training objectives which results in better performance in small experiments in regression and reinforcement learning. We also show that FRM can be seen as finding the simplest model that memorizes the training data, providing an avenue towards understanding generalization in the over-parameterized regime.

## item_id: m_2246

TITLE: PRANC: Pseudo RAndom Networks for Compacting deep models

ABSTRACT: Compacting deep models has various applications where the communication and/or storage is expensive including multi-agent learning. We introduce a simple yet effective framework for compacting neural networks. In short, we train our network to be a linear combination of many pseudo-randomly generated frozen models. Then, one can reconstruct the model by communicating or storing the single `seed' scalar used to generate the pseudo-random `basis' networks along with the learned linear mixture coefficients. Our method, denoted as PRANC, learns almost $100\times$ fewer parameters than a deep model and still performs reasonably well on several datasets and architectures. PRANC enables 1) efficient communication of models between agents, 2) efficient model storage, and 3) memory-efficient inference by generating layer-wise weights on the fly. We test PRANC on CIFAR-10, CIFAR-100, tinyImageNet, and ImageNet-100 with various architectures like AlexNet, LeNet, ResNet18, ResNet20, and ResNet56 and demonstrate a massive reduction in the number of parameters while providing satisfactory performance on these benchmark datasets.

## item_id: m_2247

TITLE: Label Propagation Networks

ABSTRACT: Graph networks have recently attracted considerable interest, and in particular in the context of semi-supervised learning. These methods typically work by generating node representations that are propagated throughout a given weighted graph.

Here we argue that for semi-supervised learning, it is more natural to consider propagating labels in the graph instead. Towards this end, we propose a differentiable neural version of the classic Label Propagation (LP) algorithm. This formulation can be used for learning edge weights, unlike other methods where weights are set heuristically. Starting from a layer implementing a single iteration of LP, we proceed by adding several important non-linear steps that significantly enhance the label-propagating mechanism.

Experiments in two distinct settings demonstrate the utility of our approach.


## item_id: m_2248

TITLE: Open-Vocabulary Object Detection upon Frozen Vision and Language Models

ABSTRACT: We present F-VLM, a simple open-vocabulary object detection method built uponFrozenVision andLanguageModels.  F-VLM simplifies the current multi-stage training pipeline by eliminating the need for knowledge distillation or detection-tailored pretraining.  Surprisingly, we observe that a frozen VLM: 1) retains the locality-sensitive features necessary for detection, and 2) is a strong region classifier.  We finetune only the detector head and combine the detector and VLM outputs for each region at inference time.  F-VLM shows compelling scaling behavior and achieves +6.5 mask AP improvement over the previous state of theart  on  novel  categories  of  LVIS  open-vocabulary  detection  benchmark. In addition, we demonstrate very competitive results on COCO open-vocabulary detection benchmark and cross-dataset transfer detection, in addition to significant training speed-up and compute savings. Code will be released.


## item_id: m_2249

TITLE: Subspace Regularizers for Few-Shot Class Incremental Learning

ABSTRACT: Few-shot class incremental learning---the problem of updating a trained classifier to discriminate among an expanded set of classes with limited labeled data---is a key challenge for machine learning systems deployed in non-stationary environments. Existing approaches to the problem rely on complex model architectures and training procedures that are difficult to tune and re-use. In this paper, we present an extremely simple approach that enables the use of ordinary logistic regression classifiers for few-shot incremental learning. The key to this approach is a new family of \textit{subspace regularization} schemes that encourage weight vectors for new classes to lie close to the subspace spanned by the weights of existing classes. When combined with pretrained convolutional feature extractors, logistic regression models trained with subspace regularization outperform specialized, state-of-the-art approaches to few-shot incremental image classification by up to 23\% on the \textit{mini}ImageNet dataset. Because of its simplicity, subspace regularization can be straightforwardly configured to incorporate additional background information about the new classes (including class names and descriptions specified in natural language); this offers additional control over the trade-off between existing and new classes. Our results show that simple geometric regularization of class representations offers an effective tool for continual learning.

## item_id: m_2250

TITLE: Provable Sim-to-real Transfer in Continuous Domain with Partial Observations

ABSTRACT:     Sim-to-real transfer, which trains RL agents in the simulated environments and then deploys them in the real world, has been widely used to overcome the limitations of gathering samples in the real world. Despite the empirical success of the sim-to-real transfer, its theoretical foundation is much less understood. In this paper, we study the sim-to-real transfer in continuous domain with partial observations, where the simulated environments and real-world environments are modeled by linear quadratic Gaussian (LQG) systems. We show that a popular robust adversarial training algorithm is capable of learning a policy from the simulated environment that is competitive to the optimal policy in the real-world environment. To achieve our results, we design a new algorithm for infinite-horizon average-cost LQGs and establish a regret bound that depends on the intrinsic complexity of the model class. Our algorithm crucially relies on a novel history clipping scheme, which might be of independent interest.

## item_id: m_2251

TITLE: Pure and Spurious Critical Points: a Geometric Study of Linear Networks

ABSTRACT: The critical locus of the loss function of a neural network is determined by the geometry of the functional space and by the parameterization of this space by the network's weights. We introduce a natural distinction between pure critical points, which only depend on the functional space, and spurious critical points, which arise from the parameterization. We apply this perspective to revisit and extend the literature on the loss function of linear neural networks. For this type of network, the functional space is either the set of all linear maps from input to output space, or a determinantal variety, i.e., a set of linear maps with bounded rank. We use geometric properties of determinantal varieties to derive new results on the landscape of linear networks with different loss functions and different parameterizations. Our analysis clearly illustrates that the absence of "bad" local minima in the loss landscape of linear networks is due to two distinct phenomena that apply in different settings: it is true for arbitrary smooth convex losses in the case of architectures that can express all linear maps ("filling architectures") but it holds only for the quadratic loss when the functional space is a determinantal variety ("non-filling architectures"). Without any assumption on the architecture, smooth convex losses may lead to landscapes with many bad minima.

## item_id: m_2252

TITLE: GROOT: Graph Edge Re-growth and Partitioning for the Verification of Large Designs in Logic Synthesis

ABSTRACT: Traditional verification methods in chip design are highly time-consuming and computationally demanding, especially for large-scale circuits. Graph neural networks (GNNs) have gained popularity as a potential solution to improve verification efficiency. However, there lacks a joint framework that considers all chip design domain knowledge, graph theory, and GPU kernel designs. To address
this challenge, we introduce GROOT, an algorithm and system co-design framework that contains chip design domain knowledge, graph theory, and redesigned GPU kernels, to improve verification efficiency. More specifically, we redesign node features utilizing the circuit node types and the polarity of the connections between the input edges to nodes in And-Inverter Graphs (AIGs). We utilize a graph partitioning algorithm based on the observation that approximately only 10% of boundary edges (nodes) between clusters, to divide the large graphs into smaller sub-graphs for fast GPU processing. We carefully profile the EDA graph workloads and observe the uniqueness of their polarized distribution of high-degree (HD) nodes and low-degree (LD) nodes. We redesign two GPU kernels (HD-kernel and LD-kernel), to fit the EDA graph learning workload on a single GPU. We evaluate the performance of GROOT on large circuit designs, e.g., Carry Save Adder (CSA) multipliers, the 7nm technology-mapped CSA multipliers, and Booth Multipliers. We compare the results with state-of-the-art GNN-based GAMORA and the traditional ABC framework. Results show that GROOT achieves a significant reduction in memory footprint (59.38 %), with high accuracy (99.96%) for a very large CSA multiplier, i.e. 1,024 bits with a batch size of 16, which consists of 134,103,040 nodes and 268,140,544 edges. We also compare GROOT with state-of-the-art GPU-based GPU Kernel designs such as cuSPARSE, MergePath-SpMM, and GNNAdvisor. We achieve up to 1.104×, 5.796×, and 1.469× improvement in runtime, respectively.

## item_id: m_2253

TITLE: Neuro-Symbolic Program Synthesis

ABSTRACT: Recent years have seen the proposal of a number of neural architectures for the problem of Program Induction. Given a set of input-output examples, these architectures are able to learn mappings that generalize to new test inputs. While achieving impressive results, these approaches have a number of important limitations: (a) they are computationally expensive and hard to train, (b) a model has to be trained for each task (program) separately, and (c) it is hard to interpret or verify the correctness of the learnt mapping (as it is defined by a neural network). In this paper, we propose a novel technique, Neuro-Symbolic Program Synthesis, to overcome the above-mentioned problems. Once trained, our approach can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time. Our method is based on two novel neural modules. The first module, called the cross correlation I/O network, given a set of input-output examples, produces a continuous representation of the set of I/O examples. The second module, the Recursive-Reverse-Recursive Neural Network (R3NN), given the continuous representation of the examples, synthesizes a program by incrementally expanding partial programs. We demonstrate the effectiveness of our approach by applying it to the rich and complex domain of regular expression based string transformations. Experiments show that the R3NN model is not only able to construct programs from new input-output examples, but it is also able to construct new programs for tasks that it had never observed before during training.

## item_id: m_2254

TITLE: Hallucination Mitigation in Large Vision-Language Models via Adaptive Multi-Subspace Projection

ABSTRACT: Recent advances in large vision-language models (LVLMs) have enabled powerful multimodal reasoning by integrating visual encoders with large language models (LLMs). However, their reliability is frequently undermined by hallucinations—generated text that inaccurately describes the visual input. Although fine-tuning can mitigate this, it is computationally expensive and demands large, curated datasets, making training-free alternatives more appealing. Among training-free strategies, model-editing is a more promising solution than decoding-based approaches. While decoding methods can adapt outputs per-input, they introduce substantial computational overhead and instability. Model-editing, by contrast, modifies the model's internal representations offline, offering a more efficient and stable framework. However, the effectiveness of current model-editing techniques is limited. Existing methods typically rely on a single, global subspace to correct errors. This static, one-size-fits-all approach treats all test samples identically, failing to capture the diverse modes of hallucination that vary from one input to another. To overcome this specific limitation, we propose a training-free hallucination mitigation framework that performs dynamic, per-instance suppression at test time. Our method advances the model-editing paradigm by first constructing a set of Disentangled Hallucination Subspaces, where each subspace isolates a distinct hallucination mode. Then, at inference, our model adaptively calculates weights to determine how a given input relates to each subspace. These weights guide a dynamically combined projection that selectively suppresses the most probable hallucination directions for that specific instance while preserving image-grounded semantics. Extensive experiments across multiple vision-language benchmarks and LVLMs families demonstrate consistent improvements, highlighting the robustness, generalizability, and efficiency of our approach.

## item_id: m_2255

TITLE: Compact Embedding of Binary-coded Inputs and Outputs using Bloom Filters

ABSTRACT: The size of neural network models that deal with sparse inputs and outputs is often dominated by the dimensionality of those inputs and outputs. Large models with high-dimensional inputs and outputs are difficult to train due to the limited memory of graphical processing units, and difficult to deploy on mobile devices with limited hardware. To address these difficulties, we propose Bloom embeddings, a compression technique that can be applied to the input and output of neural network models dealing with sparse high-dimensional binary-coded instances. Bloom embeddings are computationally efficient, and do not seriously compromise the accuracy of the model up to 1/5 compression ratios. In some cases, they even improve over the original accuracy, with relative increases up to 12%. We evaluate Bloom embeddings on 7 data sets and compare it against 4 alternative methods, obtaining favorable results. We also discuss a number of further advantages of Bloom embeddings, such as 'on-the-fly' constant-time operation, zero or marginal space requirements, training time speedups, or the fact that they do not require any change to the core model architecture or training configuration.

## item_id: m_2256

TITLE: On the duality between contrastive and non-contrastive self-supervised learning

ABSTRACT: Recent approaches in self-supervised learning of image representations can be categorized into different families of methods and, in particular, can be divided into contrastive and non-contrastive approaches. While differences between the two families have been thoroughly discussed to motivate new approaches, we focus more on the theoretical similarities between them. By designing contrastive and covariance based non-contrastive criteria that can be related algebraically and shown to be equivalent under limited assumptions, we show how close those families can be. We further study popular methods and introduce variations of them, allowing us to relate this theoretical result to current practices and show the influence (or lack thereof) of design choices on downstream performance. Motivated by our equivalence result, we investigate the low performance of SimCLR and show how it can match VICReg's with careful hyperparameter tuning, improving significantly over known baselines. We also challenge the popular assumption that non-contrastive methods need large output dimensions. Our theoretical and quantitative results suggest that the numerical gaps between contrastive and non-contrastive methods in certain regimes can be closed given better network design choices and hyperparameter tuning. The evidence shows that unifying different SOTA methods is an important direction to build a better understanding of self-supervised learning.

## item_id: m_2257

TITLE: Influence-Based Reinforcement Learning for Intrinsically-Motivated Agents

ABSTRACT: Discovering successful coordinated behaviors is a central challenge in Multi-Agent Reinforcement Learning (MARL) since it requires exploring a joint action space that grows exponentially with the number of agents. In this paper, we propose a mechanism for achieving sufficient exploration and coordination in a team of agents. Specifically, agents are rewarded for contributing to a more diversified team behavior by employing proper intrinsic motivation functions. To learn meaningful coordination protocols, we structure agents’ interactions by introducing a novel framework, where at each timestep, an agent simulates counterfactual rollouts of its policy and, through a sequence of computations, assesses the gap between other agents’ current behaviors and their targets. Actions that minimize the gap are considered highly influential and are rewarded. We evaluate our approach on a set of challenging tasks with sparse rewards and partial observability that require learning complex cooperative strategies under a proper exploration scheme, such as the StarCraft Multi-Agent Challenge. Our methods show significantly improved performances over different baselines across all tasks.

## item_id: m_2258

TITLE: On Self Modulation for Generative Adversarial Networks

ABSTRACT: Training Generative Adversarial Networks (GANs) is notoriously challenging. We propose and study an architectural modification, self-modulation, which improves GAN performance across different data sets, architectures, losses, regularizers, and hyperparameter settings. Intuitively, self-modulation allows the intermediate feature maps of a generator to change as a function of the input noise vector. While reminiscent of other conditioning techniques, it requires no labeled data. In a large-scale empirical study we observe a relative decrease of 5%-35% in FID. Furthermore, all else being equal, adding this modification to the generator leads to improved performance in 124/144 (86%) of the studied settings. Self-modulation is a simple architectural change that requires no additional parameter tuning, which suggests that it can be applied readily to any GAN.

## item_id: m_2259

TITLE: Massively Scaling Heteroscedastic Classifiers

ABSTRACT: Heteroscedastic classifiers, which learn a multivariate Gaussian distribution over prediction logits, have been shown to perform well on image classification problems with hundreds to thousands of classes. However, compared to standard classifiers, they introduce extra parameters that scale linearly with the number of classes. This makes them infeasible to apply to larger-scale problems. In addition heteroscedastic classifiers introduce a critical temperature hyperparameter which must be tuned. We propose HET-XL, a heteroscedastic classifier whose parameter count when compared to a standard classifier scales independently of the number of classes. In our large-scale settings, we show that we can remove the need to tune the temperature hyperparameter, by directly learning it on the training data. On large image classification datasets with up to 4B images and 30k classes our method requires 14X fewer additional parameters, does not require tuning the temperature on a held-out set and performs consistently better than the baseline heteroscedastic classifier. HET-XL improves ImageNet 0-shot classification in a multimodal contrastive learning setup which can be viewed as a 3.5 billion class classification problem.

## item_id: m_2260

TITLE: An Empirical Investigation of the Role of Pre-training in Lifelong Learning

ABSTRACT: The lifelong learning paradigm in machine learning is an attractive alternative to the more prominent isolated learning scheme not only due to its resemblance to biological learning, but also its potential to reduce energy waste by obviating excessive model re-training. A key challenge to this paradigm is the phenomenon of catastrophic forgetting. With the increasing popularity and success of pre-trained models in machine learning, we pose the question: What role does pre-training play in lifelong learning, specifically with respect to catastrophic forgetting? We investigate existing methods in the context of large, pre-trained models and evaluate their performance on a variety of text and image classification tasks, including a large-scale study using a novel dataset of 15 diverse NLP tasks. Across all settings, we observe that generic pre-training implicitly alleviates the effects of catastrophic forgetting when learning multiple tasks sequentially compared to randomly initialized models. We then further investigate why pre-training alleviates forgetting in this setting. We study this phenomenon by analyzing the loss landscape, finding that pre-trained weights appear to ease forgetting by leading to wider minima. Based on this insight, we propose jointly optimizing for current task loss and loss basin sharpness in order to explicitly encourage wider basins during sequential fine-tuning. We show that this optimization approach leads to performance comparable to the state-of-the-art in task-sequential continual learning across multiple settings, without retaining a memory that scales in size with the number of tasks.

## item_id: m_2261

TITLE: On the Feasibility of Cross-Task Transfer with Model-Based Reinforcement Learning

ABSTRACT: Reinforcement Learning (RL) algorithms can solve challenging control problems directly from image observations, but they often require millions of environment interactions to do so. Recently, model-based RL algorithms have greatly improved sample-efficiency by concurrently learning an internal model of the world, and supplementing real environment interactions with imagined rollouts for policy improvement. However, learning an effective model of the world from scratch is challenging, and in stark contrast to humans that rely heavily on world understanding and visual cues for learning new skills. In this work, we investigate whether internal models learned by modern model-based RL algorithms can be leveraged to solve new, distinctly different tasks faster. We propose Model-Based Cross-Task Transfer (XTRA), a framework for sample-efficient online RL with scalable pretraining and finetuning of learned world models. By offline multi-task pretraining and online cross-task finetuning, we achieve substantial improvements over a baseline trained from scratch; we improve mean performance of model-based algorithm EfficientZero by 23%, and by as much as 71% in some instances. Project page: https://nicklashansen.github.io/xtra

## item_id: m_2262

TITLE: Novelty Detection with GAN

ABSTRACT: The ability of a classifier to recognize unknown inputs is important for many classification-based systems. We discuss the problem of simultaneous classification and novelty detection, i.e. determining whether an input is from the known set of classes and from which specific class, or from an unknown domain and does not belong to any of the known classes. We propose a method based on the Generative Adversarial Networks (GAN) framework. We show that a multi-class discriminator trained with a generator that generates samples from a mixture of nominal and novel data distributions is the optimal novelty detector. We approximate that generator with a mixture generator trained with the Feature Matching loss and empirically show that the proposed method outperforms conventional methods for novelty detection. Our findings demonstrate a simple, yet powerful new application of the GAN framework for the task of novelty detection.

## item_id: m_2263

TITLE: Learning the Representation of Behavior Styles with Imitation Learning

ABSTRACT: Imitation learning is one of the methods for reproducing expert demonstrations adaptively by learning a mapping between observations and actions. However, behavior styles such as motion trajectory and driving habit depend largely on the dataset of human maneuvers, and settle down to an average behavior style in most imitation learning algorithms. In this study, we propose a method named style behavior cloning (Style BC), which can not only infer the latent representation of behavior styles automatically, but also imitate different style policies from expert demonstrations. Our method is inspired by the word2vec algorithm and we construct a behavior-style to action mapping which is similar to the word-embedding to context mapping in word2vec. Empirical results on popular benchmark environments show that Style BC outperforms standard behavior cloning in prediction accuracy and expected reward significantly. Furthermore, compared with various baselines, our policy influenced by its assigned style embedding can better reproduce the expert behavior styles, especially in the complex environments or the number of the behavior styles is large.

## item_id: m_2264

TITLE: DSD: Dense-Sparse-Dense Training for Deep Neural Networks

ABSTRACT: Modern deep neural networks have a large number of parameters, making them very hard to train. We propose DSD, a dense-sparse-dense training flow, for regularizing deep neural networks and achieving better optimization performance. In the first D (Dense) step, we train a dense network to learn connection weights and importance. In the S (Sparse) step, we regularize the network by pruning the unimportant connections with small weights and retraining the network given the sparsity constraint. In the final D (re-Dense) step, we increase the model capacity by removing the sparsity constraint, re-initialize the pruned parameters from zero and retrain the whole dense network. Experiments show that DSD training can improve the performance for a wide range of CNNs, RNNs and LSTMs on the tasks of image classification, caption generation and speech recognition. On ImageNet, DSD improved the Top1 accuracy of GoogLeNet by 1.1%, VGG-16 by 4.3%, ResNet-18 by 1.2% and ResNet-50 by 1.1%, respectively. On the WSJ’93 dataset, DSD improved DeepSpeech and DeepSpeech2 WER by 2.0% and 1.1%. On the Flickr-8K dataset, DSD improved the NeuralTalk BLEU score by over 1.7. DSD is easy to use in practice: at training time, DSD incurs only one extra hyper-parameter: the sparsity ratio in the S step. At testing time, DSD doesn’t change the network architecture or incur any inference overhead. The consistent and significant performance gain of DSD experiments shows the inadequacy of the current training methods for finding the best local optimum, while DSD effectively achieves superior optimization performance for finding a better solution. DSD models are available to download at https://songhan.github.io/DSD.

## item_id: m_2265

TITLE: Resolving Interference (RI): Disentangling Models for Improved Model Merging

ABSTRACT: Model merging has shown that multitask models can be created by directly combining the parameters of different models that are each specialized on tasks of interest. However, models trained independently on distinct tasks often exhibit interference that degrades the merged model's performance. To solve this problem, we formally define the notion of 'Cross-Task Interference' as the drift in the representation of the merged model to its constituent models. Reducing cross-task interference is the key to improving merging performance. To address this issue, we propose our method 'Resolving Interference (RI)', a light-weight framework which disentangles expert models to be functionally orthogonal to the space of other tasks, thereby reducing cross-task interference. RI does this whilst using only \textit{unlabeled auxiliary} data as input (i.e., no task-data is needed), allowing it to be applied to under data-scarce scenarios. RI consistently improves the performance of existing merging methods by up to 10% and generalization to unseen domains by up to 2.3%. We also find RI to be robust to the source of auxiliary input while being significantly less sensitive to tuning of merging hyperparameters.

## item_id: m_2266

TITLE: S4G: Breaking the Bottleneck on Graphs with Structured State Spaces

ABSTRACT: The majority of GNNs are based on message-passing mechanisms, however, message-passing neural networks (MPNN) have inherent limitations in capturing long-range interactions. The exponentially growing node information is compressed into fixed-size representations through multiple rounds of message passing, bringing the over-squashing problem, which severely hinders the flow of information on the graph and creates a bottleneck in graph learning. The natural idea of introducing global attention to point-to-point communication, as adopted in graph Transformers (GT), lacks inductive biases on graph structures and relies on complex positional encodings to enhance their performance in practical tasks. In this paper, we observe that the sensitivity between nodes in MPNN decreases exponentially with the shortest path distance. Contrarily, GT has a constant sensitivity, which leads to its loss of inductive bias. To address these issues, we introduce structured state spaces to capture the hierarchical structure of rooted-trees, achieving linear sensitivity with theoretical guarantees. We further propose a novel graph convolution based on the state-space model, resulting in a new paradigm that retains both the strong inductive biases from MPNN and the long-range modeling capabilities from GT. Extensive experimental results on long-range and general graph benchmarks demonstrate the superiority of our approach.

## item_id: m_2267

TITLE: Disentangled activations in deep networks

ABSTRACT: Deep neural networks have been tremendously successful in a number of tasks.
One of the main reasons for this is their capability to automatically
learn representations of data in levels of abstraction,
increasingly disentangling the data as the internal transformations are applied.
In this paper we propose a novel regularization method that penalize covariance between dimensions of the hidden layers in a network, something that benefits the disentanglement.
This makes the network learn nonlinear representations that are linearly uncorrelated, yet allows the model to obtain good results on a number of tasks, as demonstrated by our experimental evaluation.
The proposed technique can be used to find the dimensionality of the underlying data, because it effectively disables dimensions that aren't needed.
Our approach is simple and computationally cheap, as it can be applied as a regularizer to any gradient-based learning model.

## item_id: m_2268

TITLE: Learning Wasserstein Embeddings

ABSTRACT: The Wasserstein distance received a lot of attention recently in the community of machine learning, especially for its principled way of comparing distributions. It has found numerous applications in several hard problems, such as domain adaptation, dimensionality reduction or generative models. However, its use is still limited by a heavy computational cost. Our goal is to alleviate this problem by providing an approximation mechanism that allows to break its inherent complexity. It relies on the search of an embedding where the Euclidean distance mimics the Wasserstein distance. We show that such an embedding can be found with a siamese architecture associated with a decoder network that allows to move from the embedding space back to the original input space. Once this embedding has been found, computing optimization problems in the Wasserstein space (e.g. barycenters, principal directions or even archetypes) can be conducted extremely fast. Numerical experiments supporting this idea are conducted on image datasets, and show the wide potential benefits of our method.

## item_id: m_2269

TITLE: DeepDRK: Deep Dependency Regularized Knockoff for Feature Selection

ABSTRACT: Model-X knockoff, among various feature selection methods, received much attention recently due to its guarantee on false discovery rate (FDR) control. Subsequent to its introduction in parametric design, knockoff is advanced to handle arbitrary data distributions using deep learning-based generative modeling. However, we observed that current implementations of the deep Model-X knockoff framework exhibit limitations. Notably, the "swap property" that knockoffs necessitate frequently encounter challenges on sample level, leading to a diminished selection power. To overcome, we develop "Deep Dependency Regularized Knockoff (DeepDRK)", a distribution-free deep learning method that strikes a balance between FDR and power. In DeepDRK, a generative model grounded in a transformer architecture is introduced to better achieve the "swap property". Novel efficient regularization techniques are also proposed to reach higher power. Our model outperforms other benchmarks in synthetic, semi-synthetic, and real-world data, especially when sample size is small and data distribution is complex.

## item_id: m_2270

TITLE: Development of JavaScript-based deep learning platform and application to distributed training

ABSTRACT: Deep learning is increasingly attracting attention for processing big data.
Existing frameworks for deep learning must be set up to specialized computer systems. Gaining sufficient computing resources therefore entails high costs of deployment and maintenance.
In this work, we implement a matrix library and deep learning framework that uses JavaScript. It can run on web browsers operating on ordinary personal computers and smartphones.
Using JavaScript, deep learning can be accomplished in widely diverse environments without the necessity for software installation. Using GPGPU from WebCL framework, our framework can train large scale convolutional neural networks such as VGGNet and ResNet.
In the experiments, we demonstrate their practicality by training VGGNet in a distributed manner using web browsers as the client.


## item_id: m_2271

TITLE: MSTformer: Multiscale Spatiotemporal Motion-aware Transformer Network for Effective AI-Generated Video Detection

ABSTRACT: Recent AI-generated videos (e.g., Veo3) are growing increasingly realistic and indistinguishable from real videos. Current existing detectors usually rely on artifacts present in earlier or inferior generations, resulting in poor generalization to the newly published generators. To address the challenge of newly generated videos, we propose a novel dataset, AIDetection, for the AI-generated video detection task. The proposed AIDetection dataset contains 39,298 real and 19,731 generated videos from 27 diverse sources, specifically designed to evaluate cross-generator generalization under out-of-distribution settings. For the real videos, the motion of moving objects and the background show clear distinctions. Based on this observation, in this paper, we introduce a novel Multiscale Spatiotemporal motion modeling Transformer framework (MSTformer) for the AI-generated video detection task, which learns motion-aware discriminative representations from both local and global viewpoints. Specifically, a novel multiscale spatiotemporal downsampling mechanism is designed to capture local motion discrepancies between real and generated videos. Further, to prevent the discriminative cues from being weakened, we also employ a contrastive learning mechanism implemented on multiscale spatiotemporal features, enabling the model to maintain the global discriminative ability. Extensive experiments on three benchmark datasets (i.e. AIDetection, GVF, and GenVideo) demonstrate that MSTformer achieves the superior cross-domain generalization performance. In addition, ablation studies further confirm the effectiveness of multiscale temporal modeling and contrastive learning in enhancing robustness for AI-generated video detection.

## item_id: m_2272

TITLE: Shortest-Path Constrained Reinforcement Learning for Sparse Reward Tasks

ABSTRACT: We propose the k-Shortest-Path (k-SP) constraint: a novel constraint on the agent’s trajectory that improves the sample-efficiency in sparse-reward MDPs. We show that any optimal policy necessarily satisfies the k-SP constraint. Notably, the k-SP constraint prevents the policy from exploring state-action pairs along the non-k-SP trajectories (e.g., going back and forth).  However, in practice, excluding state-action pairs may hinder convergence of many RL algorithms. To overcome this, we propose a novel cost function that penalizes the policy violating SP constraint, instead of completely excluding it.  Our numerical experiment in a tabular RL setting demonstrate that the SP constraint can significantly reduce the trajectory space of policy. As a result, our constraint enables more sample efficient learning by suppressing redundant exploration and exploitation. Our empirical experiment results on MiniGrid and DeepMind Lab show that the proposed method significantly improves proximal policy optimization (PPO) and outperforms existing novelty-seeking exploration methods including count-based exploration, indicating that it improves the sample efficiency by preventing the agent from taking redundant actions.

## item_id: m_2273

TITLE: PopSGD: Decentralized Stochastic Gradient Descent in the Population Model

ABSTRACT: The population model is a standard way to represent large-scale decentralized
distributed systems, in which agents with limited computational power interact
in randomly chosen pairs, in order to collectively solve global computational
tasks. In contrast with synchronous gossip models, nodes are anonymous, lack a
common notion of time, and have no control over their scheduling. In this paper,
we examine whether large-scale distributed optimization can be performed in this
extremely restrictive setting. 

We introduce and analyze a natural decentralized variant of stochastic gradient
descent (SGD), called PopSGD, in which every node maintains a local parameter,
and is able to compute stochastic gradients with respect to this parameter. 
Every pair-wise node interaction performs a stochastic gradient step at each
agent, followed by averaging of the two models. We prove that, under standard
assumptions, SGD can converge even in this extremely loose, decentralized
setting, for both convex and non-convex objectives.  Moreover, surprisingly, in
the former case, the algorithm can achieve linear speedup in the number of nodes
n. Our analysis leverages a new technical connection between decentralized SGD
and randomized load balancing, which enables us to tightly bound the
concentration of node parameters. We validate our analysis through experiments,
showing that PopSGD can achieve convergence and speedup for large-scale
distributed learning tasks in a supercomputing environment.

## item_id: m_2274

TITLE: On the Implicit Bias Towards Depth Minimization in Deep Neural Networks

ABSTRACT: Recent results in the literature suggest that the penultimate (second-to-last) layer representations of neural networks that are trained for classification exhibit a clustering property called neural collapse (NC). We study the implicit bias of stochastic gradient descent (SGD) in favor of low-depth solutions when training deep neural networks. We characterize a notion of effective depth that measures the first layer for which sample embeddings are separable using the nearest-class center classifier. Furthermore, we hypothesize and empirically show that SGD implicitly selects neural networks of small effective depths. 

Secondly, while neural collapse emerges even when generalization should be impossible - we argue that the \emph{degree of separability} in the intermediate layers is related to generalization. We derive a generalization bound based on comparing the effective depth of the network with the minimal depth required to fit the same dataset with partially corrupted labels. Remarkably, this bound provides non-trivial estimations of the test performance. Finally, we empirically show that the effective depth of a trained neural network monotonically increases when increasing the number of random labels in data.

## item_id: m_2275

TITLE: AlignSep: Temporally-Aligned Video-Queried Sound Separation with Flow Matching

ABSTRACT: Video Query Sound Separation (VQSS) aims to isolate target sounds conditioned on visual queries while suppressing off-screen interference—a task central to audiovisual understanding. However, existing methods often fail under conditions of homogeneous interference and overlapping soundtracks, due to limited temporal modeling and weak audiovisual alignment.
We propose \textbf{AlignSep}, the first generative VQSS model based on flow matching, designed to address common issues such as spectral holes and incomplete separation. To better capture cross-modal correspondence, we introduce a series of temporal consistency mechanisms that guide the vector field estimator toward learning robust audiovisual alignment, enabling accurate and resilient separation in complex scenes.
As a \textit{multi-conditioned generation} task, VQSS presents unique challenges that differ fundamentally from traditional flow matching setups. We provide an in-depth analysis of these differences and their implications for generative modeling. To systematically evaluate performance under realistic and difficult conditions, we further construct \textbf{VGGSound-Hard}, a challenging benchmark composed entirely of separation cases with homogeneous interference and strong reliance on temporal visual cues.
Extensive experiments across multiple benchmarks demonstrate that AlignSep achieves state-of-the-art performance both quantitatively and perceptually, validating its practical value for real-world applications. More results and audio examples are available at: \url{https://AlignSep.github.io}.

## item_id: m_2276

TITLE: EBES: Easy Benchmarking for Event Sequences

ABSTRACT: Event sequences, characterized by irregular sampling intervals and a mix of categorical and numerical features, are common data structures in various real-world domains such as healthcare, finance, and user interaction logs. Despite advances in temporal data modeling techniques, there is no standardized benchmarks for evaluating their performance on event sequences. This complicates result comparison across different papers due to varying evaluation protocols, potentially misleading progress in this field.
We introduce EBES, a comprehensive benchmarking tool with standardized evaluation scenarios and  protocols, focusing on regression and classification problems with sequence-level targets. Our library~\footnote{We attach an archive with the code. The code will be publicly available after the conference decision.}  simplifies benchmarking, dataset addition, and method integration through a unified interface. It includes a novel synthetic dataset and provides preprocessed real-world datasets, including the largest publicly available banking dataset.
Our results provide an in-depth analysis of datasets, identifying some as unsuitable for model comparison. We investigate the importance of modeling temporal and sequential components, as well as the robustness and scaling properties of the models. These findings highlight potential directions for future research. Our benchmark aim is to facilitate reproducible research, expediting progress and increasing real-world impacts.

## item_id: m_2277

TITLE: Revisiting Classifier Two-Sample Tests

ABSTRACT: The goal of two-sample tests is to assess whether two samples, $S_P \sim P^n$ and $S_Q \sim Q^m$, are drawn from the same distribution.  Perhaps intriguingly, one relatively unexplored method to build two-sample tests is the use of binary classifiers. In particular, construct a dataset by pairing the $n$ examples in $S_P$ with a positive label, and by pairing the $m$ examples in $S_Q$ with a negative label. If the null hypothesis ``$P = Q$'' is true, then the classification accuracy of a binary classifier on a held-out subset of this dataset should remain near chance-level.  As we will show, such \emph{Classifier Two-Sample Tests} (C2ST) learn a suitable representation of the data on the fly, return test statistics in interpretable units, have a simple null distribution, and their predictive uncertainty allow to interpret where $P$ and $Q$ differ.

The goal of this paper is to establish the properties, performance, and uses of C2ST.  First, we analyze their main theoretical properties.  Second, we compare their performance against a variety of state-of-the-art alternatives.  Third, we propose their use to evaluate the sample quality of generative models with intractable likelihoods, such as Generative Adversarial Networks (GANs).  Fourth, we showcase the novel application of GANs together with C2ST for causal discovery.

## item_id: m_2278

TITLE: Federated Natural Policy Gradient Methods for Multi-task Reinforcement Learning

ABSTRACT: Federated reinforcement learning (RL) enables collaborative decision making of multiple distributed agents without sharing local data trajectories. In this work, we consider a multi-task setting, in which each agent has its own private reward function corresponding to different tasks, while sharing the same transition kernel of the environment. Focusing on infinite-horizon tabular Markov decision processes, the goal is to learn a globally optimal policy that maximizes the sum of the discounted total rewards of all the agents in a decentralized manner, where each agent only communicates with its neighbors over some prescribed graph topology. 


We develop federated vanilla and entropy-regularized natural policy gradient (NPG) methods under softmax parameterization, where gradient tracking is applied to the global Q-function to mitigate the impact of imperfect information sharing. We establish non-asymptotic global convergence guarantees under exact policy evaluation, which are nearly independent of the size of the state-action space and illuminate the impacts of network size and connectivity. To the best of our knowledge, this is the first time that global convergence is established for federated multi-task RL using policy optimization. Moreover, the convergence behavior of the proposed algorithms is robust against inexactness of policy evaluation.

## item_id: m_2279

TITLE: Topology and Geometry of Half-Rectified Network Optimization

ABSTRACT: The loss surface of deep neural networks has recently attracted interest 
in the optimization and machine learning communities as a prime example of 
high-dimensional non-convex problem. Some insights were recently gained using spin glass 
models and mean-field approximations, but at the expense of strongly simplifying the nonlinear nature of the model.

In this work, we do not make any such approximation and study conditions 
on the data distribution and model architecture that prevent the existence 
of bad local minima. Our theoretical work quantifies and formalizes two 
important folklore facts: (i) the landscape of deep linear networks has a radically different topology 
from that of deep half-rectified ones, and (ii) that the energy landscape 
in the non-linear case is fundamentally controlled by the interplay between the smoothness of the data distribution and model over-parametrization. Our main theoretical contribution is to prove that half-rectified single layer networks are asymptotically connected, and we provide explicit bounds that reveal the aforementioned interplay.

The conditioning of gradient descent is the next challenge we address. 
We study this question through the geometry of the level sets, and we introduce
an algorithm to efficiently estimate the regularity of such sets on large-scale networks. 
Our empirical results show that these level sets remain connected throughout 
all the learning phase, suggesting a near convex behavior, but they become 
exponentially more curvy as the energy level decays, in accordance to what is observed in practice with 
very low curvature attractors.

## item_id: m_2280

TITLE: Representation Learning for Remote Sensing: An Unsupervised Sensor Fusion Approach

ABSTRACT: In the application of machine learning to remote sensing, labeled data is often scarce or expensive, which impedes the training of powerful models like deep convolutional neural networks. Although unlabeled data is abundant, recent self-supervised learning approaches are ill-suited to the remote sensing domain. In addition, most remote sensing applications currently use only a small subset of the multi-sensor, multi-channel information available, motivating the need for fused multi-sensor representations. We propose a new self-supervised training objective, Contrastive Sensor Fusion, which exploits coterminous data from multiple sources to learn useful representations of every possible combination of those sources. This method uses information common across multiple sensors and bands by training a single model to produce a representation that remains similar when any subset of its input channels is used. Using a dataset of 47 million unlabeled coterminous image triplets, we train an encoder to produce semantically meaningful representations from any possible combination of channels from the input sensors. These representations outperform fully supervised ImageNet weights on a remote sensing classification task and improve as more sensors are fused.

## item_id: m_2281

TITLE: Tracking objects that change in appearance with phase synchrony

ABSTRACT: Objects we encounter often change appearance as we interact with them. Changes in illumination (shadows), object pose, or the movement of non-rigid objects can drastically alter available image features. How do biological visual systems track objects as they change? One plausible mechanism involves attentional mechanisms for reasoning about the locations of objects independently of their appearances --- a capability that prominent neuroscience theories have associated with computing through neural synchrony. Here, we describe a novel deep learning circuit that can learn to precisely control attention to features separately from their location in the world through neural synchrony: the complex-valued recurrent neural network (CV-RNN). Next, we compare object tracking in humans, the CV-RNN, and other deep neural networks (DNNs), using FeatureTracker: a large-scale challenge that asks observers to track objects as their locations and appearances change in precisely controlled ways. While humans effortlessly solved FeatureTracker, state-of-the-art DNNs did not. In contrast, our CV-RNN behaved similarly to humans on the challenge, providing a computational proof-of-concept for the role of phase synchronization as a neural substrate for tracking appearance-morphing objects as they move about.

## item_id: m_2282

TITLE: Shift-tolerant Perceptual Similarity Metric

ABSTRACT: Existing perceptual similarity metrics assume an image and its reference are well aligned. As a result, these metrics are often sensitive to a small alignment error that is imperceptible to the human eyes. This paper studies the effect of small misalignment, specifically a small shift between the input and reference image, on existing metrics, and accordingly develops a shift-tolerant similarity metric. This paper builds upon LPIPS, a widely used learned perceptual similarity metric and explores architectural design considerations to make it robust against imperceptible misalignment. Specifically, we study a wide spectrum of neural network elements, such as anti-aliasing filtering, pooling, striding, padding, and skip connection, and discuss their roles in making a robust metric. Based on our studies, we develop a new deep neural network-based perceptual similarity metric. Our experiments show that our metric is tolerant to imperceptible shifts while being consistent with the human similarity judgment.

## item_id: m_2283

TITLE: Expand Neurons, Not Parameters

ABSTRACT: This work demonstrates how increasing the number of neurons in a network without increasing its number of non-zero parameters improves performance. We show that this gain corresponds with a decrease in interference between multiple features that would otherwise share the same neurons. On symbolic tasks, specifically Boolean code problems, splitting each neuron into sparser sub-neurons with knowledge of the clauses systematically reduces polysemanticity metrics and yields higher task accuracy. Notably, even random splits of neuron weights approximate these gains, indicating that reduced collisions, not precise assignment, are a primary driver. Consistent with the superposition hypothesis, the benefits of this framework grow with increasing interference: when polysemantic load is high, accuracy improvements are the largest. Transferring these insights to real models—classifiers over CLIP embeddings, CNNs, and deeper multilayer networks—we find that widening networks while maintaining a constant non-zero parameter count consistently increases accuracy. These results identify an interpretability-grounded mechanism to leverage width against superposition, improving performance without increasing the number of non-zero parameters. Such a direction is well matched to modern accelerators, where memory movement of non-zero parameters, rather than raw compute, is often the dominant bottleneck.

## item_id: m_2284

TITLE: What a difference a pixel makes: An empirical examination of features used by CNNs for categorisation

ABSTRACT: Convolutional neural networks (CNNs) were inspired by human vision and, in some settings, achieve a performance comparable to human object recognition. This has lead to the speculation that both systems use similar mechanisms to perform recognition. In this study, we conducted a series of simulations that indicate that there is a fundamental difference between human vision and CNNs: while object recognition in humans relies on analysing shape, CNNs do not have such a shape-bias. We teased apart the type of features selected by the model by modifying the CIFAR-10 dataset so that, in addition to containing objects with shape, the images concurrently contained non-shape features, such as a noise-like mask. When trained on these modified set of images, the model did not show any bias towards selecting shapes as features. Instead it relied on whichever feature allowed it to perform the best prediction -- even when this feature was a noise-like mask or a single predictive pixel amongst 50176 pixels. We also found that regularisation methods, such as batch normalisation or Dropout, did not change this behaviour and neither did past or concurrent experience with images from other datasets.

## item_id: m_2285

TITLE: Distilled Agent DQN for Provable Adversarial Robustness

ABSTRACT: As deep neural networks have become the state of the art for solving complex reinforcement learning tasks, susceptibility to perceptual adversarial examples have become a concern. The transferability of adversarial examples is known to enable attacks capable of tricking the agent into bad states. In this work we demonstrate a simple poisoning attack able to keep deep RL from learning, and into fooling it when trained with defense methods commonly used for classification tasks. We then propose an algorithm called DadQN, based on deep Q-networks, which enables the use of stronger defenses, including defenses enabling the first ever on-line robustness certification of a deep RL agent.

## item_id: m_2286

TITLE: Lifelong Learning with Output Kernels

ABSTRACT: Lifelong learning poses considerable challenges in terms of effectiveness (minimizing prediction errors for all tasks) and overall computational tractability for real-time performance.  This paper addresses continuous lifelong multitask learning by jointly re-estimating the inter-task relations (\textit{output} kernel) and the per-task model parameters at each round, assuming data arrives in a streaming fashion. We propose a novel algorithm called  \textit{Online Output Kernel Learning Algorithm} (OOKLA) for lifelong learning setting. To avoid the memory explosion, we propose a robust budget-limited versions of the proposed algorithm that efficiently utilize the relationship between the tasks to bound the total number of representative examples in the support set.  In addition, we propose a two-stage budgeted scheme for efficiently tackling the task-specific budget constraints in lifelong learning. Our empirical results over three datasets indicate superior AUC performance for OOKLA and its budget-limited cousins over strong baselines.

## item_id: m_2287

TITLE: Learning Intrinsic Sparse Structures within Long Short-Term Memory

ABSTRACT: Model compression is significant for the wide adoption of Recurrent Neural Networks (RNNs) in both user devices possessing limited resources and business clusters requiring quick responses to large-scale service requests. This work aims to learn structurally-sparse Long Short-Term Memory (LSTM) by reducing the sizes of basic structures within LSTM units, including input updates, gates, hidden states, cell states and outputs. Independently reducing the sizes of basic structures can result in inconsistent dimensions among them, and consequently, end up with invalid LSTM units. To overcome the problem, we propose Intrinsic Sparse Structures (ISS) in LSTMs. Removing a component of ISS will simultaneously decrease the sizes of all basic structures by one and thereby always maintain the dimension consistency. By learning ISS within LSTM units, the obtained LSTMs remain regular while having much smaller basic structures. Based on group Lasso regularization, our method achieves 10.59x speedup without losing any perplexity of a language modeling of Penn TreeBank dataset. It is also successfully evaluated through a compact model with only 2.69M weights for machine Question Answering of SQuAD dataset. Our approach is successfully extended to non- LSTM RNNs, like Recurrent Highway Networks (RHNs). Our source code is available.

## item_id: m_2288

TITLE: Generalized Multimodal ELBO

ABSTRACT: Multiple data types naturally co-occur when describing real-world phenomena and learning from them is a long-standing goal in machine learning research. However, existing self-supervised generative models approximating an ELBO are not able to fulfill all desired requirements of multimodal models: their posterior approximation functions lead to a trade-off between the semantic coherence and the ability to learn the joint data distribution. We propose a new, generalized ELBO formulation for multimodal data that overcomes these limitations. The new objective encompasses two previous methods as special cases and combines their benefits without compromises. In extensive experiments, we demonstrate the advantage of the proposed method compared to state-of-the-art models in self-supervised, generative learning tasks.

## item_id: m_2289

TITLE: Residual Gated Graph ConvNets

ABSTRACT: Graph-structured data such as social networks, functional brain networks, gene regulatory networks, communications networks have brought the interest in generalizing deep learning techniques to graph domains. In this paper, we are interested to design neural networks for graphs with variable length in order to solve learning problems such as vertex classification, graph classification, graph regression, and graph generative tasks. Most existing works have focused on recurrent neural networks (RNNs) to learn meaningful representations of graphs, and more recently new convolutional neural networks (ConvNets) have been introduced. In this work, we want to compare rigorously these two fundamental families of architectures to solve graph learning tasks. We review existing graph RNN and ConvNet architectures, and propose natural extension of LSTM and ConvNet to graphs with arbitrary size. Then, we design a set of analytically controlled experiments on two basic graph problems, i.e. subgraph matching and graph clustering, to test the different architectures.  Numerical results show that the proposed graph ConvNets are 3-17% more accurate and 1.5-4x faster than graph RNNs. Graph ConvNets are also 36% more accurate than variational (non-learning) techniques. Finally, the most effective graph ConvNet architecture uses gated edges and residuality. Residuality plays an essential role to learn multi-layer architectures as they provide a 10% gain of performance.

## item_id: m_2290

TITLE: On the Use of Word Embeddings Alone to Represent Natural Language Sequences

ABSTRACT: To construct representations for natural language sequences, information from two main sources needs to be captured: (i) semantic meaning of individual words, and (ii) their compositionality. These two types of information are usually represented in the form of word embeddings and compositional functions, respectively. For the latter, Recurrent Neural Networks (RNNs) and Convolutional Neural Networks (CNNs) have been considered. There has not been a rigorous evaluation regarding the relative importance of each component to different text-representation-based tasks; i.e., how important is the modeling capacity of word embeddings alone, relative to the added value of a compositional function? In this paper, we conduct an extensive comparative study between Simple Word Embeddings-based Models (SWEMs), with no compositional parameters, relative to employing word embeddings within RNN/CNN-based models. Surprisingly, SWEMs exhibit comparable or even superior performance in the majority of cases considered. Moreover, in a new SWEM setup, we propose to employ a max-pooling operation over the learned word-embedding matrix of a given sentence. This approach is demonstrated to extract complementary features relative to the averaging operation standard to SWEMs, while endowing our model with better interpretability. To further validate our observations, we examine the information utilized by different models to make predictions, revealing interesting properties of word embeddings.


## item_id: m_2291

TITLE: SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size

ABSTRACT: Recent research on deep neural networks has focused primarily on improving accuracy. For a given accuracy level, it is typically possible to identify multiple DNN architectures that achieve that accuracy level. With equivalent accuracy, smaller DNN architectures offer at least three advantages: (1) Smaller DNNs require less communication across servers during distributed training. (2) Smaller DNNs require less bandwidth to export a new model from the cloud to an autonomous car. (3) Smaller DNNs are more feasible to deploy on FPGAs and other hardware with limited memory. To provide all of these advantages, we propose a small DNN architecture called SqueezeNet. SqueezeNet achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters. Additionally, with model compression techniques we are able to compress SqueezeNet to less than 0.5MB (510x smaller than AlexNet).

## item_id: m_2292

TITLE: The Geometry of Categorical and Hierarchical Concepts in Large Language Models

ABSTRACT: The linear representation hypothesis is the informal idea that semantic concepts are encoded as linear directions in the representation spaces of large language models (LLMs). Previous work has shown how to make this notion precise for representing binary concepts that have natural contrasts (e.g., {male, female}) as _directions_ in representation space. However, many natural concepts do not have natural contrasts (e.g., whether the output is about an animal). In this work, we show how to extend the formalization of the linear representation hypothesis to represent features (e.g., is_animal) as _vectors_. This allows us to immediately formalize the representation of categorical concepts as polytopes in the representation space. Further, we use the formalization to prove a relationship between the hierarchical structure of concepts and the geometry of their representations. We validate these theoretical results on the Gemma and LLaMA-3 large language models, estimating representations for 900+ hierarchically related concepts using data from WordNet.

## item_id: m_2293

TITLE: Self-supervised Contrastive Zero to Few-shot Learning from Small, Long-tailed Text data

ABSTRACT: For natural language processing (NLP) ‘text-to-text’ tasks, prevailing approaches heavily rely on pretraining large self-supervised models on massive external datasources.  However, this methodology is being critiqued for: exceptional compute and pretraining data requirements; diminishing returns on both large and small datasets; and importantly, favourable evaluation settings that overestimate performance differences.  The core belief behind current methodology, coined 'the bitter lesson' by R. Sutton, is that 'compute scale-up beats data and compute-efficient algorithms', neglecting that progress in compute hardware scale-up is based almost entirely on the miniaturisation of resource consumption.  We thus approach pretraining from a miniaturisation perspective, such as not to require massive external data sources and models, or learned translations from continuous input embeddings to discrete labels.  To minimise overly favourable evaluation, we examine learning on a long-tailed, low-resource, multi-label text classification dataset with noisy, highly sparse labels and many rare concepts.  To this end, we propose a novel 'dataset-internal' contrastive autoencoding approach to self-supervised pretraining and demonstrate marked improvements in zero-shot, few-shot and solely supervised learning performance; even under an unfavorable low-resource scenario, and without defaulting to large-scale external datasets for self-supervision.  We also find empirical evidence that zero and few-shot learning markedly benefit from adding more 'dataset-internal', self-supervised training signals, which is of practical importance when retrieving or computing on large external sources of such signals is infeasible.

## item_id: m_2294

TITLE: StructViT: Learning Correlation Structures for Vision Transformers

ABSTRACT: We introduce the structural self-attention (StructSA) mechanism that leverages structural patterns of query-key correlation for visual representation learning. StructSA generates attention by recognizing space-time structures of correlations and performs long-range interactions across entire locations, effectively capturing structural patterns, e.g., spatial layouts, motion, or inter-object relations in images and videos. Using StructSA as a main building block, we develop the structural vision transformer (StructViT) and evaluate its effectiveness on both image and video classification tasks, achieving state-of-the-art results on ImageNet-1K, Kinetics-400, Something-Something V1 & V2, Diving-48, and FineGym.

## item_id: m_2295

TITLE: Role of Locality and Weight Sharing in Image-Based Tasks: A Sample Complexity Separation between CNNs, LCNs, and FCNs

ABSTRACT: Vision tasks are characterized by the properties of locality and translation invariance. 
    The superior performance of convolutional neural networks (CNNs) on these tasks is widely attributed to the inductive bias of locality and weight sharing baked into their architecture.
    Existing attempts to quantify the statistical benefits of these biases in CNNs over locally connected convolutional neural networks (LCNs) and fully connected neural networks (FCNs) fall into one of the following categories: either they disregard the optimizer and only provide uniform convergence upper bounds with no separating lower bounds, 
    or they consider simplistic tasks that do not truly mirror the locality and translation invariance as found in real-world vision tasks.
    To address these deficiencies, we introduce the Dynamic Signal Distribution (DSD) classification task that models an image as consisting of $k$ patches, each of dimension $d$, and the label is determined by a $d$-sparse signal vector that can freely appear in any one of the $k$ patches. 
    On this task, for any orthogonally equivariant algorithm like gradient descent, we prove that CNNs require $\tilde{O}(k+d)$ samples, whereas LCNs require $\Omega(kd)$ samples, establishing the statistical advantages of weight sharing in translation invariant tasks. 
    Furthermore, LCNs need $\tilde{O}(k(k+d))$ samples, compared to $\Omega(k^2d)$ samples for FCNs, showcasing the benefits of locality in local tasks.
    Additionally, we develop information theoretic tools for analyzing randomized algorithms, which may be of interest for statistical research.

## item_id: m_2296

TITLE: Cost-Effective Interactive Neural Attention Learning

ABSTRACT: We propose a novel interactive attention learning framework which we refer to as Interactive Attention Learning (IAL), in which the human annotators interactively manipulate the allocated attentions to correct the model’s behavior, by updating the attention-generating model without having to retrain the network. For efficient update of the attention generator without retraining, we propose a novel attention mechanism Neural Attention Process (NAP), which can generate stochastic attentions based on scarce training instances, and can incorporate new training instances without retraining. Further, to minimize human interaction cost, we propose a cost-effective algorithm that selects the most negative training instances that yield incorrect and non-intuitive interpretation with influence function and re-rank the attentions on the input features by their uncertainties, such that the annotators label the instances and attentions that are more influential to the prediction first. We validate IAL on multiple datasets from the healthcare domain, on which it not only significantly outperforms other baselines, but also achieves explicitly trained attention for interpretability that agrees well with human interpretation without expensive human labeling procedure.

## item_id: m_2297

TITLE: Orthogonalising gradients to speedup neural network optimisation

ABSTRACT: The optimisation of neural networks can be sped up by orthogonalising the gradients before the optimisation step, ensuring the diversification of the learned representations. We hypothesize that components in the same layer learn the same representations at the beginning of learning. To prevent this we orthogonalise the gradients of the components with respect to each other.
Our method of orthogonalisation allows the weights to be used more flexibly, in contrast to restricting the weights to an orthogonalised sub-space. We tested this method on ImageNet and CIFAR-10 resulting in a large decrease in learning time, and also obtain a speed-up on the semi-supervised learning BarlowTwins. We obtain similar accuracy to SGD without fine-tuning and better accuracy for naïvely chosen hyper-parameters.


## item_id: m_2298

TITLE: Consistency-Based Semi-Supervised Active Learning: Towards Minimizing Labeling Budget

ABSTRACT: Active learning (AL) aims to integrate data labeling and model training in a unified way, and to minimize the labeling budget by prioritizing the selection of high value data that can best improve model performance. Readily-available unlabeled data are used to evaluate selection mechanisms, but are not used for model training in conventional pool-based AL. To minimize the labeling budget, we unify unlabeled sample selection and model training based on two principles. First, we exploit both labeled and unlabeled data using semi-supervised learning (SSL) to distill information from unlabeled data that improves representation learning and sample selection. Second, we propose a simple yet effective selection metric that is coherent with the training objective such that the selected samples are effective at improving model performance. Our experimental results demonstrate superior performance with our proposed principles for limited labeled data compared to alternative AL and SSL combinations.  In addition, we study the AL phenomena of `cold start', which is becoming an increasingly more important factor to enable optimal unification of data labeling, model training and labeling budget minimization.  We propose a measure that is found to be empirically correlated with the AL target loss. This measure can be used to assist in determining the proper start size.

## item_id: m_2299

TITLE: Leveraging Large Language Models for Optimised Coordination in Textual Multi-Agent Reinforcement Learning

ABSTRACT: Cooperative multi-agent reinforcement learning (MARL) presents unique challenges, amongst which fostering general cooperative behaviour across various tasks is critical. Recently, large language models (LLMs) have excelled at dealing with challenges in the general RL paradigm, showcasing remarkable sample efficiency and adaptability across tasks through domain specific fine-tuning, or functional alignment. However, neither LLMs nor these fine-tuning approaches are designed with coordination-centric solutions in mind, and the challenge of how to achieve greater coordination, and hence performance, with LLMs in MARL has not yet been tackled. To address this, we introduce the 'Functionally-Aligned Multi-Agents' (FAMA) framework. FAMA harnesses LLMs' inherent knowledge for cooperative decision-making via two primary mechanisms. Firstly, it aligns the LLM with the necessary functional knowledge through a centralised on-policy MARL update rule. Secondly, it recognises the pivotal role of communication in coordination and exploits the linguistic strengths of LLMs for intuitive, natural language inter-agent message-passing. Evaluations of FAMA in two multi-agent textual environments, namely BabyAI-Text and an autonomous driving junction environment, over four coordination tasks show it consistently outperforms independent learning LLMs and traditional symbolic RL methods.

## item_id: m_2300

TITLE: Spatial Variational Auto-Encoding via Matrix-Variate Normal Distributions

ABSTRACT: The key idea of variational auto-encoders (VAEs) resembles that of traditional auto-encoder models in which spatial information is supposed to be explicitly encoded in the latent space. However, the latent variables in VAEs are vectors, which can be interpreted as multiple feature maps of size 1x1. Such representations can only convey spatial information implicitly when coupled with powerful decoders. In this work, we propose spatial VAEs that use feature maps of larger size as latent variables to explicitly capture spatial information. This is achieved by allowing the latent variables to be sampled from matrix-variate normal (MVN) distributions whose parameters are computed from the encoder network. To increase dependencies among locations on latent feature maps and reduce the number of parameters, we further propose spatial VAEs via low-rank MVN distributions. Experimental results show that the proposed spatial VAEs outperform original VAEs in capturing rich structural and spatial information.
