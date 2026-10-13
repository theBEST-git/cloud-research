# Batch 34 — 100 items

## item_id: m_3301

TITLE: SALMONN: Towards Generic Hearing Abilities for Large Language Models

ABSTRACT: Hearing is arguably an essential ability of artificial intelligence (AI) agents in the physical world, which refers to the perception and understanding of general auditory information consisting of at least three types of sounds: speech, audio events, and music. In this paper, we propose SALMONN, a speech audio language music open neural network, built by integrating a pre-trained text-based large language model (LLM) with speech and audio encoders into a single multimodal model. SALMONN enables the LLM to directly process and understand general audio inputs and achieve competitive performances on a number of speech and audio tasks used in training, such as 
automatic speech recognition and translation, auditory-information-based question answering, emotion recognition, speaker verification, and music and audio captioning etc. SALMONN also has a diverse set of emergent abilities unseen in the training, which includes but is not limited to speech translation to untrained languages, speech-based slot filling, spoken-query-based question answering, audio-based storytelling, and speech audio co-reasoning etc. The presence of cross-modal emergent abilities is studied, and a novel few-shot activation tuning approach is proposed to activate such abilities. To our knowledge, SALMONN is the first model of its type and can be regarded as a step towards AI with generic hearing abilities. The source code, model checkpoints and data are available at https://github.com/bytedance/SALMONN.

## item_id: m_3302

TITLE: FILTER SHAPING FOR CONVOLUTIONAL NEURAL NETWORKS

ABSTRACT: Convolutional neural networks (CNNs) are powerful tools for classification of visual inputs. An important property of CNN is its restriction to local connections and sharing of local weights among different locations. In this paper, we consider the definition of appropriate local neighborhoods in CNN. We provide a theoretical analysis that justifies the traditional square filter used in CNN for analyzing natural images. The analysis also provides a principle for designing customized filter shapes for application domains that do not resemble natural images. We propose an approach that automatically designs multiple layers of different customized filter shapes by repeatedly solving lasso problems. It is applied to customize the filter shape for both bioacoustic applications and gene sequence analysis applications. In those domains with small sample sizes we demonstrate that the customized filters achieve superior classification accuracy, improved convergence behavior in training and reduced sensitivity to hyperparameters.

## item_id: m_3303

TITLE: Continual Learning In Low-coherence Subspace: A Strategy To Mitigate Learning Capacity Degradation

ABSTRACT: Methods using gradient orthogonal projection, an efficient strategy in continual learning, have achieved promising success in mitigating catastrophic forgetting. However, these methods often suffer from the learning capacity degradation problem following the increasing number of tasks. To address this problem, we propose to learn new tasks in low-coherence subspaces rather than orthogonal subspaces. Specifically, we construct a unified cost function involving regular DNN parameters and gradient projections on the Oblique manifold. We finally develop a gradient descent algorithm on a smooth manifold to jointly minimize the cost function and minimize both the inter-task and the intra-task coherence. Numerical experimental results show that the proposed method has prominent advantages in maintaining the learning capacity when tasks are increased, especially on a large number of tasks, compared with baselines.

## item_id: m_3304

TITLE: Concept-level Multimodal Reasoning via Semantic Representation for Intent Recognition

ABSTRACT: Multimodal intent recognition is a fundamental task in understanding human communication, aiming to infer intent from heterogeneous modalities and serving as a cornerstone for developing human-centric systems. However, existing methods face two key challenges. First, they rely on entangled and modality-specific features, which hinder the derivation of interpretable representations across modalities. Second, they lack explicit reasoning mechanisms, making it difficult to capture high-level semantic dependencies and systematically link multimodal evidence to complex intents. To address these issues, we propose a novel method (ConMR) that conducts concept-level multimodal reasoning by jointly learning semantic concept representations and modeling concept relations. Specifically, we first leverage the Large Language Model (LLM) to generate high-quality intent-related concepts, providing explicit semantic anchors beyond shallow features. By supervising multimodal feature mapping through activation alignment, these concepts yield interpretable and discriminative representations. Building on this foundation, the concept-level multimodal reasoning module models concept-to-intent relations through LLM-guided relevance scores and infers inter-concept relations from activation patterns. By jointly exploiting these relations, it guides transparent reasoning paths from concepts to intents, thereby enhancing both accuracy and interpretability. Extensive experiments on two challenging datasets show that ConMR outperforms state-of-the-art methods with superior robustness and interpretability, laying a new paradigm for multimodal intent recognition.

## item_id: m_3305

TITLE: A teacher-student framework to distill future trajectories

ABSTRACT: By learning to predict trajectories of dynamical systems, model-based methods can make extensive use of all observations from past experience. However, due to partial observability, stochasticity, compounding errors, and irrelevant dynamics, training to predict observations explicitly often results in poor models. Model-free techniques try to side-step the problem by learning to predict values directly. While breaking the explicit dependency on future observations can result in strong performance, this usually comes at the cost of low sample efficiency, as the abundant information about the dynamics contained in future observations goes unused. Here we take a step back from both approaches: Instead of hand-designing how trajectories should be incorporated, a teacher network learns to interpret the trajectories and to provide target activations which guide a student model that can only observe the present. The teacher is trained with meta-gradients to maximize the student's performance on a validation set. We show that our approach performs well on tasks that are difficult for model-free and model-based methods, and we study the role of every component through ablation studies.

## item_id: m_3306

TITLE: Dual Contradistinctive Generative Autoencoder

ABSTRACT: We present a new generative autoencoder model with dual contradistinctive losses to improve generative autoencoder that performs simultaneous inference (reconstruction) and synthesis (generation). We name our model dual contradistinctive generative autoencoder (DC-VAE) that integrates an instance-level discriminative loss (maintaining the instance-level fidelity for the reconstruction/synthesis) with a set-level adversarial loss (encouraging the set-level fidelity for the reconstruction/synthesis), both being contradistinctive.  There also exists a mathematical connection between the instance-based classification and instance-level conditional distribution. DC-VAE achieves competitive results in three tasks, including image synthesis, image reconstruction, and representation learning. DC-VAE is applicable to various tasks in computer vision and machine learning.

## item_id: m_3307

TITLE: Adversarial Machine Learning at Scale

ABSTRACT: Adversarial examples are malicious inputs designed to fool machine learning models.
They often transfer from one model to another, allowing attackers to mount black
box attacks without knowledge of the target model's parameters.
Adversarial training is the process of explicitly training a model on adversarial
examples, in order to make it more robust to attack or to reduce its test error
on clean inputs.
So far, adversarial training has primarily been applied to small problems.
In this research, we apply adversarial training to ImageNet.
Our contributions include:
(1) recommendations for how to succesfully scale adversarial training to large models and datasets,
(2) the observation that adversarial training confers robustness to single-step attack methods,
(3) the finding that multi-step attack methods are somewhat less transferable than single-step attack
      methods, so single-step attacks are the best for mounting black-box attacks,
      and
(4) resolution of a ``label leaking'' effect that causes adversarially trained models to perform
      better on adversarial examples than on clean examples, because the adversarial
      example construction process uses the true label and the model can learn to
      exploit regularities in the construction process.


## item_id: m_3308

TITLE: Relaxing Representation Alignment with Knowledge Preservation for Multi-Modal Continual Learning

ABSTRACT: In continual learning, developing robust representations that adapt to new distributions or classes while retaining prior knowledge is crucial. While most traditional approaches focus on single-modality data, multi-modal learning offers significant advantages by leveraging diverse sensory inputs, akin to human perception. However, transitioning to multi-modal continual learning introduces additional challenges as the model needs to effectively combine new information from different modalities while avoiding catastrophic forgetting. In this work, we propose a relaxed cross-modality representation alignment loss and utilize a dual-learner framework to preserve the relation between previously learned representations. We validate our framework using several multi-modal datasets that  encompass various types of input modalities. Results show that we consistently outperform baseline continual learning methods in both class incremental and domain incremental learning scenarios. Further analysis highlights the effectiveness of our solution in preserving prior knowledge while incorporating new information.

## item_id: m_3309

TITLE: Do We Really Achieve Fairness with Explicit Sensitive Attributes? 

ABSTRACT: Recently the wide usage of machine learning models for high-stake decision-making raises the concerns about the fairness and discrimination issue. Existing works found that sensitive information of a sample could be leaked completely by sensitive attributes or partially by non-sensitive attributes, thus removing the sensitive attributes directly from the original features can not achieve fairness. The current fairness practice is to leverage the explicit sensitive attributes (i.e., as regularization) to debias the prediction, based on a strong assumption that non-sensitive attributes of all samples leak the sensitive information totally. However, we investigate the distribution of leaked sensitive information from non-sensitive attributes and make interesting findings that 1) the sensitive information distinctly varies across different samples. 2) the violation of demographic parity for samples prone to leak sensitive information (high-sensitive) are worse than that for low-sensitive samples, indicating the failure of current demographic parity measurements. To this end, we propose a new group fairness ($\alpha$-Demographic Parity) to measure the demographic parity for samples with different levels of sensitive information leakage. Furthermore, we move one step forward and propose to achieve $\alpha$-demographic parity by encouraging the independence of the distribution of the sensitive information in non-sensitive attributes and that of  downstream task prediction, which is formulated as a cross-task knowledge distillation framework. Specifically, the sensitive teacher models the distribution of the sensitive information and the fair student models the distribution of the downstream task prediction. Then we encourage the independence between them by minimizing the Hilbert-Schmidt Independence Criterion. Our model can naturally tackle the limited sensitive attribution scenario since the teacher models can be trained with partial samples with sensitive attributes. Extensive experiments show the superior performance of our proposed method on the $\alpha$-demographic parity and performs well on limited sensitive attribute scenarios.

## item_id: m_3310

TITLE: Understanding & Generalizing AlphaGo Zero

ABSTRACT: AlphaGo Zero (AGZ) introduced a new {\em tabula rasa} reinforcement learning algorithm that has achieved superhuman performance in the games of Go, Chess, and Shogi with no prior knowledge other than the rules of the game. This success naturally begs the question whether it is possible to develop similar high-performance reinforcement learning algorithms for generic sequential decision-making problems (beyond two-player games), using only the constraints of the environment as the ``rules.'' To address this challenge, we start by taking steps towards developing a formal understanding of AGZ.  AGZ includes two key innovations: (1) it learns a policy (represented as a neural network) using {\em supervised learning} with cross-entropy loss from samples generated via Monte-Carlo Tree Search (MCTS); (2) it uses {\em self-play} to learn without training data. 

We argue that the self-play in AGZ corresponds to learning a Nash equilibrium for the two-player game; and the supervised learning with MCTS is attempting to learn the policy corresponding to the Nash equilibrium, by establishing a novel bound on the difference between the expected return achieved by two policies in terms of the expected KL divergence (cross-entropy) of their induced distributions. To extend AGZ to generic sequential decision-making problems, we introduce a {\em robust MDP} framework, in which the agent and nature effectively play a zero-sum game: the agent aims to take actions to maximize reward while nature seeks state transitions, subject to the constraints of that environment, that minimize the agent's reward. For a challenging network scheduling domain, we find that AGZ within the robust MDP framework provides near-optimal performance, matching one of the best known scheduling policies that has taken the networking community three decades of intensive research to develop.


## item_id: m_3311

TITLE: Memorization Precedes Generation: Learning Unsupervised GANs with Memory Networks

ABSTRACT: We propose an approach to address two issues that commonly occur during training of unsupervised GANs. First, since GANs use only a continuous latent distribution to embed multiple classes or clusters of data, they often do not correctly handle the structural discontinuity between disparate classes in a latent space. Second, discriminators of GANs easily forget about past generated samples by generators, incurring instability during adversarial training. We argue that these two infamous problems of unsupervised GAN training can be largely alleviated by a learnable memory network to which both generators and discriminators can access. Generators can effectively learn representation of training samples to understand underlying cluster distributions of data, which ease the structure discontinuity problem. At the same time, discriminators can better memorize clusters of previously generated samples, which mitigate the forgetting problem. We propose a novel end-to-end GAN model named memoryGAN, which involves a memory network that is unsupervisedly trainable and integrable to many existing GAN models. With evaluations on multiple datasets such as Fashion-MNIST, CelebA, CIFAR10, and Chairs, we show that our model is probabilistically interpretable, and generates realistic image samples of high visual fidelity. The memoryGAN also achieves the state-of-the-art inception scores over unsupervised GAN models on the CIFAR10 dataset, without any optimization tricks and weaker divergences.

## item_id: m_3312

TITLE: TRIDE: A Temporal, Robust, and Informative Data Augmentation Framework for Disease Progression Modeling

ABSTRACT: Modeling the progression of a target disease using electronic health records (EHRs), especially early predicting the onset of a disease, is critical for timely and accurate clinical interventions. While numerous deep learning-based prediction models have shown great success in handling sequential multivariate data such as EHRs, they often lack temporal robustness. This is problematic because they may not perform consistently well across different early prediction hours as training data become scarce upon targeting further future. Indeed, having even one weak point of time can significantly restrict the reliability of the models. In this work, we present TRIDE, a temporal, robust and informative data augmentation framework that can learn temporal representations of EHRs and use them to generate diverse and meaningful training samples by optimizing the level of data transformation. We validate TRIDE on modeling the progression of an extremely challenging disease, septic shock, by using real-world EHRs collected from two different medical systems. Our results show that TRIDE significantly outperforms strong baseline models across different prediction times and datasets, and thus enhances the temporal robustness. Further, we provide in-depth analyses of the generated samples and estimated model parameters to clarify the processes.

## item_id: m_3313

TITLE: MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences

ABSTRACT: Recent advancements in video generation have primarily leveraged diffusion models for short-duration content. However, these approaches often fall short in modeling complex narratives and maintaining character consistency over extended periods, which is essential for long-form video production like movies. We propose MovieDreamer, a novel hierarchical framework that integrates the strengths of autoregressive models with diffusion-based rendering to pioneer long-duration video generation with intricate plot progressions and high visual fidelity. Our approach utilizes autoregressive models for global narrative coherence, predicting sequences of visual tokens that are subsequently transformed into high-quality video frames through diffusion rendering. This method is akin to traditional movie production processes, where complex stories are factorized down into manageable scene capturing. Further, we employ a multimodal script that enriches scene descriptions with detailed character information and visual style, enhancing continuity and character identity across scenes. We present extensive experiments across various movie genres, demonstrating that our approach not only achieves superior visual and narrative quality but also effectively extends the duration of generated content significantly beyond current capabilities.

## item_id: m_3314

TITLE: Pretrained Language Models are Symbolic Mathematics Solvers too!

ABSTRACT: Solving symbolic mathematics has always been of in the arena of human ingenuity that needs compositional reasoning and recurrence. However, recent studies have shown that large scale language models such as transformers are universal and surprisingly can be trained as  a sequence-to-sequence task to solve complex mathematical equations. These large transformer models need humongous amounts of training data to generalize to unseen symbolic mathematics problems. In this paper, we present a sample efficient way of solving the symbolic tasks by first pretraining the transformer model with language translation and then fine-tuning the pretrained transformer model to solve the  downstream task of symbolic mathematics. We achieve comparable accuracy on the integration task with our pretrained model while using around $1.5$ orders of magnitude less number of training samples with respect to the state-of-the-art deep learning for symbolic mathematics. The test accuracy on differential equation tasks is considerably lower comparing with integration as they need higher order recursions that are not present in language translations. We pretrain our model with different pairs of language translations. Our results show language bias in solving symbolic mathematics tasks. Finally, we study the robustness of the fine-tuned model on symbolic math tasks against distribution shift, and our approach generalizes better in distribution shift scenarios for the function integration.

## item_id: m_3315

TITLE: Effect of Activation Functions on the Training of Overparametrized Neural Nets

ABSTRACT: It is well-known that overparametrized neural networks trained using gradient based methods quickly achieve small training error with appropriate hyperparameter settings. Recent papers have proved this statement theoretically for highly overparametrized networks under reasonable assumptions. These results either assume that the activation function is ReLU or they depend on the minimum eigenvalue of a certain Gram matrix. In the latter case, existing works only prove that this minimum eigenvalue is non-zero and do not provide quantitative bounds which require that this eigenvalue be large. Empirically, a number of alternative activation functions have been proposed which tend to perform better than ReLU at least in some settings but no clear understanding has emerged. This state of affairs underscores the importance of theoretically understanding the impact of activation functions on training. In the present paper, we provide theoretical results about the effect of activation function on the training of highly overparametrized 2-layer neural networks. A crucial property that governs the performance of an activation is whether or not it is smooth: 
• For non-smooth activations such as ReLU, SELU, ELU, which are not smooth because there is a point where either the ﬁrst order or second order derivative is discontinuous, all eigenvalues of the associated Gram matrix are large under minimal assumptions on the data. 
• For smooth activations such as tanh, swish, polynomial, which have derivatives of all orders at all points, the situation is more complex: if the subspace spanned by the data has small dimension then the minimum eigenvalue of the Gram matrix can be small leading to slow training. But if the dimension is large and the data satisﬁes another mild condition, then the eigenvalues are large. If we allow deep networks, then the small data dimension is not a limitation provided that the depth is sufﬁcient. 
We discuss a number of extensions and applications of these results.

## item_id: m_3316

TITLE: Image Animation with Refined Masking

ABSTRACT: We present a novel approach for image-animation of a source image by a driving video, both depicting the same type of object. We do not assume the existence of pose models and our method is able to animate arbitrary objects without knowledge of the object's structure. Furthermore, both the driving video and the source image are only seen during test-time. Our method is based on a shared mask generator, which separates the foreground object from its background, and captures the object’s general pose and shape. A mask-refinement module then replaces, in the mask extracted from the driver image, the identity of the driver with the identity of the source. Conditioned on the source image, the transformed mask is then decoded by a multi-scale generator that renders a realistic image, in which the content of the source frame is animated by the pose in the driving video. Our method is shown to greatly outperform the state of the art methods on multiple benchmarks. Our code and samples are attached as supplementary.

## item_id: m_3317

TITLE: Learnability Lock: Authorized Learnability Control Through Adversarial Invertible Transformations

ABSTRACT: Owing much to the revolution of information technology, recent progress of deep learning benefits incredibly from the vastly enhanced access to data available in various digital formats. Yet those publicly accessible information also raises a fundamental issue concerning Intellectual Property, that is, how to precisely control legal or illegal exploitation of a dataset for training commercial models. To tackle this issue, this paper introduces and investigates a new concept called ''learnability lock'' for securing the process of data authorization. In particular, we propose adversarial invertible transformation, that can be viewed as a mapping from image to image, to encrypt data samples so that they become ''unlearnable'' by machine learning models with negligible loss of visual features. Meanwhile, authorized clients can use a specific key to unlock the learnability of the protected dataset and train models normally. The proposed learnability lock leverages class-wise perturbation that applies a universal transformation function on data samples of the same label. This ensures that the learnability can be easily restored with a simple inverse transformation while remaining difficult to be detected or reverse-engineered. We empirically demonstrate the success and practicability of our method on visual classification tasks.  

## item_id: m_3318

TITLE: Thinking like a machine — generating visual rationales through latent space optimization

ABSTRACT: Interpretability and small labelled datasets are key issues in the practical application of deep learning, particularly in areas such as medicine. In this paper, we present a semi-supervised technique that addresses both these issues simultaneously. We learn dense representations from large unlabelled image datasets, then use those representations to both learn classifiers from small labeled sets and generate visual rationales explaining the predictions. Using chest radiography diagnosis as a motivating application, we show our method has good generalization ability by learning to represent our chest radiography dataset while training a classifier on an separate set from a different institution. Our method identifies heart failure and other thoracic diseases. For each prediction, we generate visual rationales for positive classifications by optimizing a latent representation to minimize the probability of disease while constrained by a similarity measure in image space. Decoding the resultant latent representation produces an image without apparent disease. The difference between the original and the altered image forms an interpretable visual rationale for the algorithm's prediction. Our method simultaneously produces visual rationales that compare favourably to previous techniques and a classifier that outperforms the current state-of-the-art.

## item_id: m_3319

TITLE: From Language to Goals: Inverse Reinforcement Learning for Vision-Based Instruction Following

ABSTRACT: Reinforcement learning is a promising framework for solving control problems, but its use in practical situations is hampered by the fact that reward functions are often difficult to engineer. Specifying goals and tasks for autonomous machines, such as robots, is a significant challenge: conventionally, reward functions and goal states have been used to communicate objectives. But people can communicate objectives to each other simply by describing or demonstrating them. How can we build learning algorithms that will allow us to tell machines what we want them to do? In this work, we investigate the problem of grounding language commands as reward functions using inverse reinforcement learning, and argue that language-conditioned rewards are more transferable than language-conditioned policies to new environments. We propose language-conditioned reward learning (LC-RL), which grounds language commands as a reward function represented by a deep neural network. We demonstrate that our model learns rewards that transfer to novel tasks and environments on realistic, high-dimensional visual environments with natural language commands, whereas directly learning a language-conditioned policy leads to poor performance.

## item_id: m_3320

TITLE: On the Effectiveness of Out-of-Distribution Data in Self-Supervised Long-Tail Learning.

ABSTRACT: Though Self-supervised learning (SSL) has been widely studied as a promising technique for representation learning, it doesn't generalize well on long-tailed datasets due to the majority classes dominating the feature space. Recent work shows that the long-tailed learning performance could be boosted by sampling extra in-domain (ID) data for self-supervised training, however, large-scale ID data which can rebalance the minority classes are expensive to collect. In this paper, we propose an alternative but easy-to-use and effective solution, \textbf{C}ontrastive with \textbf{O}ut-of-distribution (OOD) data for \textbf{L}ong-\textbf{T}ail learning (COLT), which can effectively exploit OOD data to dynamically re-balance the feature space. We empirically identify the counter-intuitive usefulness of OOD samples in SSL long-tailed learning and principally design a novel SSL method. Concretely, we first localize the `\emph{head}' and `\emph{tail}' samples by assigning a tailness score to each OOD sample based on its neighborhoods in the feature space. Then, we propose an online OOD sampling strategy to dynamically re-balance the feature space. Finally, we enforce the model to be capable of distinguishing ID and OOD samples by a distribution-level supervised contrastive loss. Extensive experiments are conducted on various datasets and several state-of-the-art SSL frameworks to verify the effectiveness of the proposed method. The results show that our method significantly improves the performance of SSL on long-tailed datasets by a large margin, and even outperforms previous work which uses external ID data. Our code is available at \url{https://github.com/JianhongBai/COLT}.

## item_id: m_3321

TITLE: Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model Fine-tuning

ABSTRACT: When using agent-task datasets to enhance agent capabilities for Large Language Models (LLMs), current methodologies often treat all tokens within a sample equally. 
However, we argue that tokens serving different roles—specifically, reasoning tokens versus boilerplate tokens (e.g., those governing output format)—differ significantly in importance and learning complexity, necessitating their disentanglement and distinct treatment. 
To address this, we propose a novel Shuffle-Aware Discriminator (SHAD) for adaptive token discrimination.
SHAD classifies tokens by exploiting predictability differences observed after shuffling input-output combinations across samples: boilerplate tokens, due to their repetitive nature among samples, maintain predictability, whereas reasoning tokens do not.
Using SHAD, we propose the Reasoning-highlighted Fine-Tuning (RFT) method, which adaptively emphasizes reasoning tokens during fine-tuning, yielding notable performance gains over common Supervised Fine-Tuning (SFT).

## item_id: m_3322

TITLE: Link Weight Prediction with Node Embeddings

ABSTRACT: Application of deep learning has been successful in various domains such as im-
age recognition, speech recognition and natural language processing. However,
the research on its application in graph mining is still in an early stage. Here we
present the first generic deep learning approach to the graph link weight prediction
problem based on node embeddings. We evaluate this approach with three differ-
ent node embedding techniques experimentally and compare its performance with
two state-of-the-art non deep learning baseline approaches. Our experiment re-
sults suggest that this deep learning approach outperforms the baselines by up to
70% depending on the dataset and embedding technique applied. This approach
shows that deep learning can be successfully applied to link weight prediction to
improve prediction accuracy.

## item_id: m_3323

TITLE: Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D Reconstruction

ABSTRACT: Reconstructing dynamic 3D scenes from monocular input is fundamentally under-constrained, with ambiguities arising from occlusion and extreme novel views. While dynamic Gaussian Splatting offers an efficient representation, vanilla models optimize all Gaussian primitives uniformly, ignoring whether they are well or poorly observed. This limitation leads to motion drifts under occlusion and degraded synthesis when extrapolating to unseen views. We argue that uncertainty matters: Gaussians with recurring observations across views and time act as reliable anchors to guide motion, whereas those with limited visibility are treated as less reliable. To this end, we introduce USplat4D, a novel Uncertainty-aware dynamic Gaussian Splatting framework that propagates reliable motion cues to enhance 4D reconstruction. Our approach estimates time-varying per-Gaussian uncertainty and leverages it to construct a spatio-temporal graph for uncertainty-aware optimization. Experiments on diverse real and synthetic datasets show that explicitly modeling uncertainty consistently improves dynamic Gaussian Splatting models, yielding more stable geometry under occlusion and high-quality synthesis at extreme viewpoints. Project page: https://tamu-visual-ai.github.io/usplat4d/.

## item_id: m_3324

TITLE: Multi-Domain Active Learning: A Comparative Study

ABSTRACT: Multi-domain learning (MDL) refers to learning a set of models simultaneously, with each one specialized to perform a task in a certain domain. Generally, high labeling effort is required in MDL, as data need to be labeled by human experts for every domain. Active learning (AL), which reduces labeling effort by only using the most informative data, can be utilized to address the above issue. The resultant paradigm is termed multi-domain active learning (MDAL). However, currently little research has been done in MDAL, not to mention any off-the-shelf solution. To fill this gap, we present a comprehensive comparative study of 20 different MDAL algorithms, which are established by combining five representative MDL models under different information-sharing schemes and four well-used AL strategies belonging to different categories. We evaluate the algorithms on five datasets, involving textual and visual classification tasks. We find that the models which capture both domain-dependent and domain-specific information are more likely to perform well in the whole AL loops. Besides, the simplest informativebased uncertainty strategy surprisingly performs well on most datasets. As our off-the-shelf recommendation, the combination of Multinomial Adversarial Networks (MAN) with the best vs second best (BvSB) uncertainty strategy shows its superiority in most cases, and this combination is also robust across datasets and domains.

## item_id: m_3325

TITLE: Context-adaptive Entropy Model for End-to-end Optimized Image Compression

ABSTRACT: We propose a context-adaptive entropy model for use in end-to-end optimized image compression. Our model exploits two types of contexts, bit-consuming contexts and bit-free contexts, distinguished based upon whether additional bit
allocation is required. Based on these contexts, we allow the model to more accurately estimate the distribution of each latent representation with a more generalized form of the approximation models, which accordingly leads to an
enhanced compression performance. Based on the experimental results, the proposed method outperforms the traditional image codecs, such as BPG and JPEG2000, as well as other previous artificial-neural-network (ANN) based approaches, in terms of the peak signal-to-noise ratio (PSNR) and multi-scale structural similarity (MS-SSIM) index. The test code is publicly available at https://github.com/JooyoungLeeETRI/CA_Entropy_Model.

## item_id: m_3326

TITLE: Generative Fairness Teaching

ABSTRACT: Increasing evidences has shown that data biases towards sensitive features such as gender or race are often inherited or even amplified by machine learning models. Recent advancements in fairness mitigate such biases by adjusting the predictions across sensitive groups during the training. Such a correction, however, can only take advantage of samples in a fixed dataset, which usually has limited amount of samples for the minority groups. We propose a generative fairness teaching framework that provides a model with not only real samples but also synthesized samples to compensate the data biases during training. We employ such a teaching strategy by implementing a Generative Fairness Teacher (GFT) that dynamically adjust the proportion of training data for a biased student model. Experimental results indicated that our teacher model is capable of guiding a wide range of biased models by improving  the fairness and performance trade-offs significantly.

## item_id: m_3327

TITLE: Verification of Non-Linear Specifications for Neural Networks

ABSTRACT: Prior work on neural network verification has focused on specifications that are linear functions of the output of the network, e.g., invariance of the classifier output under adversarial perturbations of the input. In this paper, we extend verification algorithms to be able to certify richer properties of neural networks. To do this we introduce the class of convex-relaxable specifications, which constitute nonlinear specifications that can be verified using a convex relaxation. We show that a number of important properties of interest can be modeled within this class, including conservation of energy in a learned dynamics model of a physical system; semantic consistency of a classifier's output labels under adversarial perturbations and bounding errors in a system that predicts the summation of handwritten digits. Our experimental evaluation shows that our method is able to effectively verify these specifications. Moreover, our evaluation exposes the failure modes in models which cannot be verified to satisfy these specifications. Thus, emphasizing the importance of training models not just to fit training data but also to be consistent with specifications.

## item_id: m_3328

TITLE: Semi-supervised Regression with Generative Adversarial Networks for End to End Learning in Autonomous Driving

ABSTRACT: This research concerns solving the semi-supervised learning problem with generative adversarial networks for regression. In contrast to classification, where only a limited number of distinct classes is given, the regression task is defined as predicting continuous labels for a given dataset. Semi-supervised learning is of vital importance for the applications where a small number of labeled samples is available, or labeling samples is difficult or expensive to collect. A case in point is autonomous driving in which obtaining sufficient labeled samples covering all driving conditions is costly. In this context, we can take advantage of semi-supervised learning techniques with groundbreaking generative models, such as generative adversarial networks. However, almost all proposed GAN-based semi-supervised techniques in the literature are focused on solving the classification problem. Hence, developing a GAN-based semi-supervised method for the regression task is still an open problem. In this work, two different architectures will be proposed to address this problem. In summary, our introduced method is able to predict continuous labels for a training dataset which has only a limited number of labeled samples. Moreover, the application of this technique for solving the end-to-end task in autonomous driving will be presented.  
We performed several experiments over a publicly available driving dataset to evaluate our proposed method, and the results are very promising. The results show that our approach generates images with high quality, gives smaller label prediction error and leads to a more stable training compared with the state-of-the-art Improved GAN technique~\citep{ImprovedGAN2016}.

## item_id: m_3329

TITLE: RainProof: An Umbrella to Shield Text Generator from Out-Of-Distribution Data

ABSTRACT: As more and more conversational and translation systems are deployed in production, it is essential to implement and develop effective control mechanisms to ensure their proper functioning and security. An essential component to ensure the safe behavior of the system is out-of-distribution (OOD) detection, which aims to detect whether an input sample is statistically far from the training distribution. While OOD detection is a widely covered topic in classification tasks, it has received much less attention in text generation. This paper addresses the problem of OOD detection for machine translation and dialog generation from an operational perspective. Our contribution includes (i) RAINPROOF a Relative informAItioN Projection Out OF distribution detection framework and (ii) a more operational evaluation setting for OOD detection. Surprisingly, we find that OOD detection is not necessarily aligned with task-specific measures. The OOD detector may filter out samples that are well processed by the model and keep samples that are not, leading to weaker performance. Our results show that RAINPROOF breaks this curse and achieve good results in OOD detection while increasing system performance.

## item_id: m_3330

TITLE: The power of deeper networks for expressing natural functions

ABSTRACT: It is well-known that neural networks are universal approximators, but that deeper networks tend in practice to be more powerful than shallower ones. We shed light on this by proving that the total number of neurons m required to approximate natural classes of multivariate polynomials of n variables grows only linearly with n for deep neural networks, but grows exponentially when merely a single hidden layer is allowed. We also provide evidence that when the number of hidden layers is increased from 1 to k, the neuron requirement grows exponentially not with n but with n^{1/k}, suggesting that the minimum number of layers required for practical expressibility grows only logarithmically with n.

## item_id: m_3331

TITLE: RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers

ABSTRACT: When translating natural language questions into SQL queries to answer questions from a database, contemporary semantic parsing models struggle to generalize to unseen database schemas.  The generalization challenge lies in (a) encoding the database relations in an accessible way for the semantic parser, and (b) modeling alignment between database columns and their mentions in a given query.  We present a unified framework, based on the relation-aware self-attention mechanism,to address schema encoding, schema linking, and feature representation within a text-to-SQL encoder. On the challenging Spider dataset this framework boosts the exact match accuracy to 53.7%, compared to 47.4% for the previous state-of-the-art model unaugmented with BERT embeddings. In addition, we observe qualitative improvements in the model’s understanding of schema linking and alignment.

## item_id: m_3332

TITLE: The Devil is in the Object Boundary: Towards Annotation-free Instance Segmentation using Foundation Models

ABSTRACT: Foundation models, pre-trained on a large amount of data have demonstrated impressive zero-shot capabilities in various downstream tasks. However, in object detection and instance segmentation, two fundamental computer vision tasks heavily reliant on extensive human annotations, foundation models such as SAM and DINO struggle to achieve satisfactory performance. 
In this study, we reveal that the devil is in the object boundary, $\textit{i.e.}$, these foundation models fail to discern boundaries between individual objects. 
For the first time, we probe that CLIP, which has never accessed any instance-level annotations, can provide a highly beneficial and strong instance-level boundary prior in the clustering results of its particular intermediate layer. Following this surprising observation, we propose $\textbf{\textit{Zip}}$ which $\textbf{Z}$ips up CL$\textbf{ip}$ and SAM in a novel classification-first-then-discovery pipeline, enabling annotation-free, complex-scene-capable, open-vocabulary object detection and instance segmentation. 
Our Zip significantly boosts SAM's mask AP on COCO dataset by 12.5\% and establishes state-of-the-art performance in various settings, including training-free, self-training, and label-efficient finetuning. Furthermore, annotation-free Zip even achieves comparable performance to the best-performing open-vocabulary object detecters using base annotations. Code is released at https://github.com/ChengShiest/Zip-Your-CLIP

## item_id: m_3333

TITLE: Weakly-supervised Camera Localization by Ground-to-satellite Image Registration

ABSTRACT: The ground-to-satellite image matching/retrieval was initially proposed for city-scale ground camera localization. Recently, more and more attention has been paid to increasing the camera pose accuracy by ground-to-satellite image matching, once a coarse location and orientation has been obtained from the city-scale retrieval.  This paper addresses the same scenario. 
However, existing learning-based methods for solving this task require accurate GPS labels of ground images for network training. 
Unfortunately, obtaining such accurate GPS labels is not always possible, often requiring an expensive RTK setup and suffering from signal occlusion, multi-path signal disruptions, \etc. 
To address this issue, this paper proposes a weakly-supervised learning strategy for ground-to-satellite image registration. It does not require highly accurate ground truth (GT)
pose labels for ground images in the training dataset. Instead, a coarse location and orientation label, either derived from the city-scale retrieval or noisy sensors (GPS, compass, \etc), is sufficient. 
Specifically, we present a pseudo image pair creation strategy for cross-view rotation estimation network training, and a novel method that leverages deep metric learning for translation estimation between ground-and-satellite image pairs.
Experimental results show that our weakly-supervised learning strategy achieves the best performance on cross-area evaluation, compared to the recent state-of-the-art methods that require accurate pose labels for supervision, and shows comparable performance on same-area evaluation.

## item_id: m_3334

TITLE: Deep Autoencoding Gaussian Mixture Model for Unsupervised Anomaly Detection

ABSTRACT: Unsupervised anomaly detection on multi- or high-dimensional data is of great importance in both fundamental machine learning research and industrial applications, for which density estimation lies at the core. Although previous approaches based on dimensionality reduction followed by density estimation have made fruitful progress, they mainly suffer from decoupled model learning with inconsistent optimization goals and incapability of preserving essential information in the low-dimensional space. In this paper, we present a Deep Autoencoding Gaussian Mixture Model (DAGMM) for unsupervised anomaly detection. Our model utilizes a deep autoencoder to generate a low-dimensional representation and reconstruction error for each input data point, which is further fed into a Gaussian Mixture Model (GMM). Instead of using decoupled two-stage training and the standard Expectation-Maximization (EM) algorithm, DAGMM jointly optimizes the parameters of the deep autoencoder and the mixture model simultaneously in an end-to-end fashion, leveraging a separate estimation network to facilitate the parameter learning of the mixture model. The joint optimization, which well balances autoencoding reconstruction, density estimation of latent representation, and regularization, helps the autoencoder escape from less attractive local optima and further reduce reconstruction errors, avoiding the need of pre-training. Experimental results on several public benchmark datasets show that, DAGMM significantly outperforms state-of-the-art anomaly detection techniques, and achieves up to 14% improvement based on the standard F1 score.

## item_id: m_3335

TITLE: Layer Recurrent Neural Networks

ABSTRACT: In this paper, we propose a Layer-RNN (L-RNN) module that is able to learn contextual information adaptively using within-layer recurrence. Our contributions are three-fold: 
(i) we propose a hybrid neural network architecture that interleaves traditional convolutional layers with L-RNN module for learning long- range dependencies at multiple levels; 
(ii) we show that a L-RNN module can be seamlessly inserted into any convolutional layer of a pre-trained CNN, and the entire network then fine-tuned, leading to a boost in performance; 
(iii) we report experiments on the CIFAR-10 classification task, showing that a network with interleaved convolutional layers and L-RNN modules, achieves comparable results (5.39% top1 error) using only 15 layers and fewer parameters to ResNet-164 (5.46%); and on the PASCAL VOC2012 semantic segmentation task, we show that the performance of a pre-trained FCN network can be boosted by 5% (mean IOU) by simply inserting Layer-RNNs.

## item_id: m_3336

TITLE: Azimuthal Rotational Equivariance in Spherical CNNs

ABSTRACT: In this work, we analyze linear operators from $L^2(S^2) \rightarrow L^2(S^2)$ which are equivariant to azimuthal rotations, that is, rotations around the z-axis. Several high-performing neural networks defined on the sphere are indeed equivariant to azimuthal rotations, but not $SO(3)$. Our main result is to show that a linear operator acting on band-limited functions on the sphere is equivariant to azimuthal rotations if and only if it can be realized as a block-diagonal matrix acting on the spherical harmonic expansion coefficients of its input. Further, we show that such an operation can be interpreted as a convolution or equivalently a correlation. Our theoretical findings are backed up with experimental results demonstrating that a state-of-the-art pipeline can be improved by making it fully equivariant to azimuthal rotations.

## item_id: m_3337

TITLE: HolStep: A Machine Learning Dataset for Higher-order Logic Theorem Proving

ABSTRACT: Large computer-understandable proofs consist of millions of intermediate
logical steps. The vast majority of such steps originate from manually
selected and manually guided heuristics applied to intermediate goals.
So far, machine learning has generally not been used to filter or
generate these steps. In this paper, we introduce a new dataset based on
Higher-Order Logic (HOL) proofs, for the purpose of developing new
machine learning-based theorem-proving strategies. We make this dataset
publicly available under the BSD license. We propose various machine
learning tasks that can be performed on this dataset, and discuss their
significance for theorem proving. We also benchmark a set of simple baseline
machine learning models suited for the tasks (including logistic regression
convolutional neural networks and recurrent neural networks). The results of our
baseline models show the promise of applying machine learning to HOL
theorem proving.


## item_id: m_3338

TITLE: N-BEATS: Neural basis expansion analysis for interpretable time series forecasting

ABSTRACT: We focus on solving the univariate times series point forecasting problem using deep learning. We propose a deep neural architecture based on backward and forward residual links and a very deep stack of fully-connected layers. The architecture has a number of desirable properties, being interpretable, applicable without modification to a wide array of target domains, and fast to train. We test the proposed architecture on several well-known datasets, including M3, M4 and TOURISM competition datasets containing time series from diverse domains. We demonstrate state-of-the-art performance for two configurations of N-BEATS for all the datasets, improving forecast accuracy by 11% over a statistical benchmark and by 3% over last year's winner of the M4 competition, a domain-adjusted hand-crafted hybrid between neural network and statistical time series models. The first configuration of our model does not employ any time-series-specific components and its performance on heterogeneous datasets strongly suggests that, contrarily to received wisdom, deep learning primitives such as residual blocks are by themselves sufficient to solve a wide range of forecasting problems. Finally, we demonstrate how the proposed architecture can be augmented to provide outputs that are interpretable without considerable loss in accuracy.

## item_id: m_3339

TITLE: IMPACT: Importance Weighted Asynchronous Architectures with Clipped Target Networks

ABSTRACT: The practical usage of reinforcement learning agents is often bottlenecked by the duration of training time. To accelerate training, practitioners often turn to distributed reinforcement learning architectures to parallelize and accelerate the training process. However, modern methods for scalable reinforcement learning (RL) often tradeoff between the throughput of samples that an RL agent can learn from (sample throughput) and the quality of learning from each sample (sample efficiency). In these scalable RL architectures, as one increases sample throughput (i.e. increasing parallelization in IMPALA (Espeholt et al., 2018)), sample efficiency drops significantly. To address this, we propose a new distributed reinforcement learning algorithm, IMPACT. IMPACT extends PPO with three changes: a target network for stabilizing the surrogate objective, a circular buffer, and truncated importance sampling. In discrete action-space environments, we show that IMPACT attains higher reward and, simultaneously, achieves up to 30% decrease in training wall-time than that of IMPALA. For continuous control environments, IMPACT trains faster than existing scalable agents while preserving the sample efficiency of synchronous PPO.

## item_id: m_3340

TITLE: Efficient Synthetic Network Generation via Latent Embedding Reconstruction

ABSTRACT: Network data are ubiquitous across the social sciences, biology, and information systems. Generating realistic synthetic network data has broad applications, from network simulation to scientific  discovery. However, many existing black-box approaches for network generation tend to overfit observed data while overlooking characteristic network structure, and incur substantial computational overhead at scale. These practical challenges call for synthetic network generation methods that are both efficient and capable of capturing structural properties of networks. In this paper, we introduce Synthetic Network Generation via Latent Embedding Reconstruction (SyNGLER), a general and efficient framework for synthetic network generation that builds on latent space network models. Given an observed network, SyNGLER first learns low-dimensional latent node embeddings via a latent space network model and then reconstructs the latent space by building a distribution-free generator over these embeddings. For generation, SyNGLER first samples (or resamples) node embeddings from the generator in the latent space and then produces synthetic networks using the latent space network model. Through the latent space framework, SyNGLER preserves unique characteristics in networks such as sparsity and node degree heterogeneity, while allowing for efficient training with lower computational cost than many existing deep architectures. We provide theoretical guarantees by developing consistency results regarding the distance between the true and synthetic edge distributions. Empirical studies further demonstrate the effectiveness of SyNGLER, where SyNGLER efficiently produces networks that better preserve key network characteristics such as network moments and degree distributions compared with existing approaches.

## item_id: m_3341

TITLE: Transfer Learning with Deep Tabular Models

ABSTRACT: Recent work on deep learning for tabular data demonstrates the strong performance of deep tabular models, often bridging the gap between gradient boosted decision trees and neural networks. Accuracy aside, a major advantage of neural models is that they are easily fine-tuned in new domains and learn reusable features. This property is often exploited in computer vision and natural language applications, where transfer learning is indispensable when task-specific training data is scarce. In this work, we explore the benefits that representation learning provides for knowledge transfer in the tabular domain. We conduct experiments in a realistic medical diagnosis test bed with limited amounts of downstream data and find that transfer learning with deep tabular models provides a definitive advantage over gradient boosted decision tree methods. We further compare the supervised and self-supervised pretraining strategies and provide practical advice on transfer learning with tabular models. Finally, we propose a pseudo-feature method for cases where the upstream and downstream feature sets differ, a tabular-specific problem widespread in real-world applications.

## item_id: m_3342

TITLE: Influence-Directed Explanations for Deep Convolutional Networks

ABSTRACT: We study the problem of explaining a rich class of behavioral properties of deep neural networks. Our influence-directed explanations approach this problem by peering inside the network to identify neurons with high influence on the property of interest using an axiomatically justified influence measure, and then providing an interpretation for the concepts these neurons represent. We evaluate our approach by training convolutional neural networks on Pubfig, ImageNet, and Diabetic Retinopathy datasets.  Our evaluation demonstrates that influence-directed explanations (1) localize features used by the network, (2) isolate features distinguishing related instances, (3) help extract the essence of what the network learned about the class, and (4) assist in debugging misclassifications.


## item_id: m_3343

TITLE: A Proposed Hierarchy of Deep Learning Tasks

ABSTRACT: As the pace of deep learning innovation accelerates, it becomes increasingly important to organize the space of problems by relative difficultly.  Looking to other fields for inspiration, we see analogies to the Chomsky Hierarchy in computational linguistics and time and space complexity in theoretical computer science.

As a complement to prior theoretical work on the data and computational requirements of learning, this paper presents an empirical approach. We introduce a methodology for measuring validation error scaling with data and model size and test tasks in natural language, vision, and speech domains. We find that power-law validation error scaling exists across a breadth of factors and that model size scales sublinearly with data size, suggesting that simple learning theoretic models offer insights into the scaling behavior of realistic deep learning settings, and providing a new perspective on how to organize the space of  problems. 

We measure the power-law exponent---the "steepness" of the learning curve---and propose using this metric to sort problems by degree of difficulty.  There is no data like more data, but some tasks are more effective at taking advantage of more data.  Those that are more effective are easier on the proposed scale. 

Using this approach, we can observe that studied tasks in speech and vision domains scale faster than those in the natural language domain, offering insight into the observation that progress in these areas has proceeded more rapidly than in natural language.

## item_id: m_3344

TITLE: Metric-Driven Attributions for Vision Transformers

ABSTRACT: Attribution algorithms explain computer vision models by attributing the model response to pixels within the input. Existing attribution methods generate explanations by combining transformations of internal model representations such as class activation maps, gradients, attention, or relevance scores. The effectiveness of an attribution map is measured using attribution quality metrics. This leads us to pose the following question: if attribution methods are assessed using attribution quality metrics, why are the metrics not used to generate the attributions? In response to this question, we propose a Metric-Driven Attribution for explaining Vision Transformers (ViT) called MDA. Guided by attribution quality metrics, the method creates attribution maps by performing patch order and patch magnitude optimization across all patch tokens. The first step orders the patches in terms of importance and the second step assigns the magnitude to each patch while preserving the patch order. Moreover, MDA can provide a smooth trade-off between sparse and dense attributions by modifying the optimization objective. Experimental evaluation demonstrates the proposed MDA method outperforms $7$ existing ViT attribution methods by an average of $12\%$ across $12$ attribution metrics on the ImageNet dataset for the ViT-base $16 \times 16$, ViT-tiny $16 \times 16$, and ViT-base $32 \times 32$ models. Code is publicly available at https://github.com/chasewalker26/MDA-Metric-Driven-Attributions-for-ViT.

## item_id: m_3345

TITLE: Smooth Real-time Rendering via Implicit Nested Neighborhoods

ABSTRACT: Implicit neural representations (INRs) for surfaces have been mostly used as intermediary representations before triangle mesh extraction. Extracting meshes is not a real-time task and introduces unnecessary discretization to rendering, making it difficult to fully use the smoothness of INRs in applications. Smooth INRs are broadly used for approximating surface \textit{signed distance functions} (SDFs) through an implicit regularization (Eikonal equation) using their available high-order derivatives. Such property also makes it easier to integrate those INRs in pipelines that explore differentiable properties of the underlying surface. The current real-time state-of-the-art approach uses grid-based data-structures that introduce discretization, resulting in a non-smooth representation.

We propose an end-to-end smooth ($C^{\infty}$) INR framework to represent and render surfaces in real-time using neural SDFs endowed with smooth attributes such as normals and textures. Our approach leverages from a novel localized SDF training based on nested neighborhoods, a multiscale surface representation, and residual training. The framework does not depend on spatial data-structures, nor surface extraction. We show that our representation renders detailed smooth surfaces in real-time while the previous works can only render coarse non-smooth surfaces. We also present applications of our representation, including integration with a pipeline for dynamic surfaces and a way to improve performance of surface extraction via marching cubes.

## item_id: m_3346

TITLE: Ruminating Word Representations with Random Noise Masking

ABSTRACT: We introduce a training method for better word representation and performance, which we call \textbf{GraVeR} (\textbf{Gra}dual \textbf{Ve}ctor \textbf{R}umination). The method is to gradually and iteratively add random noises and bias to word embeddings after training a model, and re-train the model from scratch but initialize with the noised word embeddings. Through the re-training process, some noises can be compensated and other noises can be utilized to learn better representations. As a result, we can get word representations further fine-tuned and specialized in the task. On six text classification tasks, our method improves model performances with a large gap. When GraVeR is combined with other regularization techniques, it shows further improvements. Lastly, we investigate the usefulness of GraVeR.

## item_id: m_3347

TITLE: Zero-Shot Reward Specification via Grounded Natural Language

ABSTRACT: Reward signals in reinforcement learning can be expensive signals in many tasks and often require access to direct state. The alternative to reward signals are usually demonstrations or goal images which can be labor intensive to collect. Goal text description is a low effort way of communicating the desired task. Goal text conditioned policies so far though have been trained with reward signals that have access to state or labelled expert demonstrations. We devise a model that leverages CLIP to ground objects in a scene described by the goal text paired with spatial relationship rules to provide an off-the-shelf reward signal on only raw pixels to learn a set of robotic manipulation tasks. We distill the policies learned with this reward signal on several tasks to produce one goal text conditioned policy.

## item_id: m_3348

TITLE: Looking Beyond the Top-1: Transformers Determine Top Tokens in Order

ABSTRACT: Understanding the inner workings of Transformers is crucial for achieving more
accurate and efficient predictions. In this work, we analyze the computation performed
by Transformers in the layers after the top-1 prediction has become fixed, which has been
previously referred to as the “saturation event”. We expand the concept of saturation events
for top-k tokens, demonstrating that similar saturation events occur across language, vision, 
and speech models. We find that these saturation events happen in order of the 
corresponding tokens’ ranking, i.e., the model first decides on the top ranking token, then 
the second highest ranking token, and so on. This phenomenon seems intrinsic to the 
Transformer architecture, occurring across different architectural variants (decoder-only, 
encoder-only, and to a lesser extent full-Transformer), and even in untrained Transformers.
We propose an underlying mechanism of task transition for this sequential saturation, where 
task k corresponds to predicting the k-th most probable token, and the saturation events are 
in fact discrete transitions between the tasks. In support of this we show that it is possible to 
predict the current task from hidden layer embedding. Furthermore, using an intervention 
method we demonstrate that we can cause the model to switch from one task to the next. 
Finally, leveraging our findings, we introduce a novel token-level early-exit strategy, which 
surpasses existing methods in balancing performance and efficiency.

## item_id: m_3349

TITLE: Structured Exploration via Hierarchical Variational Policy Networks

ABSTRACT: Reinforcement learning in environments with large state-action spaces is challenging, as exploration can be highly inefficient. Even if the dynamics are simple, the optimal policy can be combinatorially hard to discover. In this work, we propose a hierarchical approach to structured exploration to improve the sample efficiency of on-policy exploration in large state-action spaces. The key idea is to model a stochastic policy as a hierarchical latent variable model, which can learn low-dimensional structure in the state-action space, and to define exploration by sampling from the low-dimensional latent space. This approach enables lower sample complexity, while preserving policy expressivity. In order to make learning tractable, we derive a joint learning and exploration strategy by combining hierarchical variational inference with actor-critic learning. The benefits of our learning approach are that 1) it is principled, 2) simple to implement, 3) easily scalable to settings with many actions and 4) easily composable with existing deep learning approaches. We demonstrate the effectiveness of our approach on learning a deep centralized multi-agent policy, as multi-agent environments naturally have an exponentially large state-action space. In this setting, the latent hierarchy implements a form of multi-agent coordination during exploration and execution (MACE). We demonstrate empirically that MACE can more efficiently learn optimal policies in challenging multi-agent games with a large number (~20) of agents, compared to conventional baselines. Moreover, we show that our hierarchical structure leads to meaningful agent coordination.

## item_id: m_3350

TITLE: Expressive Power of Invariant and Equivariant Graph Neural Networks

ABSTRACT: Various classes of Graph Neural Networks (GNN) have been proposed and shown to be successful in a wide range of applications with graph structured data. In this paper, we propose a theoretical framework able to compare the expressive power of these GNN architectures. The current universality theorems only apply to intractable classes of GNNs. Here, we prove the first approximation guarantees for practical GNNs, paving the way for a better understanding of their generalization. Our theoretical results are proved for invariant GNNs computing a graph embedding (permutation of the nodes of the input graph does not affect the output) and equivariant GNNs computing an embedding of the nodes (permutation of the input permutes the output). We show that Folklore Graph Neural Networks (FGNN), which are tensor based GNNs augmented with matrix multiplication are the most expressive architectures proposed so far for a given tensor order. We illustrate our results on the Quadratic Assignment Problem (a NP-Hard combinatorial problem) by showing that FGNNs are able to learn how to solve the problem, leading to much better average performances than existing algorithms (based on spectral, SDP or other GNNs architectures). On a practical side, we also implement masked tensors to handle batches of graphs of varying sizes. 

## item_id: m_3351

TITLE: Egocentric Spatial Memory Network

ABSTRACT: Inspired by neurophysiological discoveries of navigation cells in the mammalian
brain, we introduce the first deep neural network architecture for modeling Egocentric
Spatial Memory (ESM). It learns to estimate the pose of the agent and
progressively construct top-down 2D global maps from egocentric views in a spatially
extended environment. During the exploration, our proposed ESM network
model updates belief of the global map based on local observations using a recurrent
neural network. It also augments the local mapping with a novel external
memory to encode and store latent representations of the visited places based on
their corresponding locations in the egocentric coordinate. This enables the agents
to perform loop closure and mapping correction. This work contributes in the
following aspects: first, our proposed ESM network provides an accurate mapping
ability which is vitally important for embodied agents to navigate to goal locations.
In the experiments, we demonstrate the functionalities of the ESM network in
random walks in complicated 3D mazes by comparing with several competitive
baselines and state-of-the-art Simultaneous Localization and Mapping (SLAM)
algorithms. Secondly, we faithfully hypothesize the functionality and the working
mechanism of navigation cells in the brain. Comprehensive analysis of our model
suggests the essential role of individual modules in our proposed architecture and
demonstrates efficiency of communications among these modules. We hope this
work would advance research in the collaboration and communications over both
fields of computer science and computational neuroscience.

## item_id: m_3352

TITLE: Randomized Automatic Differentiation

ABSTRACT: The successes of deep learning, variational inference, and many other fields have been aided by specialized implementations of reverse-mode automatic differentiation (AD) to compute gradients of mega-dimensional objectives. The AD techniques underlying these tools were designed to compute exact gradients to numerical precision, but modern machine learning models are almost always trained with stochastic gradient descent. Why spend computation and memory on exact (minibatch) gradients only to use them for stochastic optimization? We develop a general framework and approach for randomized automatic differentiation (RAD), which can allow unbiased gradient estimates to be computed with reduced memory in return for variance. We examine limitations of the general approach, and argue that we must leverage problem specific structure to realize benefits. We develop RAD techniques for a variety of simple neural network architectures, and show that for a fixed memory budget, RAD converges in fewer iterations than using a small batch size for feedforward networks, and in a similar number for recurrent networks. We also show that RAD can be applied to scientific computing, and use it to develop a low-memory stochastic gradient method for optimizing the control parameters of a linear reaction-diffusion PDE representing a fission reactor.

## item_id: m_3353

TITLE: How to Train Your MAML to Excel in Few-Shot Classification

ABSTRACT: Model-agnostic meta-learning (MAML) is arguably one of the most popular meta-learning algorithms nowadays.
Nevertheless, its performance on few-shot classification is far behind many recent algorithms dedicated to the problem. In this paper, we point out several key facets of how to train MAML to excel in few-shot classification. First, we find that MAML needs a large number of gradient steps in its inner loop update, which contradicts its common usage in few-shot classification. Second, we find that MAML is sensitive to the class label assignments during meta-testing. Concretely, MAML meta-trains the initialization of an $N$-way classifier. These $N$ ways, during meta-testing, then have "$N!$" different permutations to be paired with a few-shot task of $N$ novel classes. We find that these permutations lead to a huge variance of accuracy, making MAML unstable in few-shot classification. Third, we investigate several approaches to make MAML permutation-invariant, among which meta-training a single vector to initialize all the $N$ weight vectors in the classification head performs the best. On benchmark datasets like MiniImageNet and TieredImageNet, our approach, which we name UNICORN-MAML, performs on a par with or even outperforms many recent few-shot classification algorithms, without sacrificing MAML's simplicity.

## item_id: m_3354

TITLE: Adversarial-Guided Diffusion for Robust and High-Fidelity Multimodal LLM Attacks

ABSTRACT: Recent diffusion-based adversarial attack methods have shown promising results in generating natural adversarial images. However, these methods often lack fidelity by inducing significant distortion on the original image with even small perturbations on the latent representation. In this paper, we propose Adversarial-Guided Diffusion (AGD), a novel diffusion-based generative adversarial attack framework, which introduces adversarial noise during the reverse sampling of conditional diffusion models. 
AGD uses editing-friendly inversion sampling to faithfully reconstruct images without significantly distorting them through gradients on the latent representation. In addition, AGD enhances latent representations by intelligently choosing sampling steps, thereby injecting adversarial semantics more smoothly. Extensive experiments demonstrate that our method outperforms state-of-the-art methods in both the effectiveness of generating adversarial images for targeted attacks on multimodal large language models (MLLMs) and image quality, successfully misleading the MLLM's responses. We argue that the security concerns surrounding the adversarial robustness of MLLMs deserve increased attention from the research community.

## item_id: m_3355

TITLE: Cross-Domain Few-Shot Learning by Representation Fusion

ABSTRACT: In order to quickly adapt to new data, few-shot learning aims at learning from few examples, often by using already acquired knowledge. The new data often differs from the previously seen data due to a domain shift, that is, a change of the input-target distribution. While several methods perform well on small domain shifts like new target classes with similar inputs, larger domain shifts are still challenging. Large domain shifts may result in abstract concepts that are not shared between the original and the new domain. However, low-level concepts like edges in images might still be shared and useful. For cross-domain few-shot learning, we suggest representation fusion to unify different abstraction levels of a deep neural network into one representation. We propose Cross-domain Hebbian Ensemble Few-shot learning (CHEF), which consists of representation fusion by an ensemble of Hebbian learners acting on different layers of a deep neural network that was trained on the original domain. On the few-shot datasets miniImagenet and tieredImagenet, where the domain shift is small, CHEF is competitive with state-of-the-art methods. On cross-domain few-shot benchmark challenges with larger domain shifts, CHEF obtains state-of-the-art results in all categories. We further apply CHEF on a real-world cross-domain application in drug discovery. We consider a domain shift from bioactive molecules to environmental chemicals and drugs with twelve associated toxicity prediction tasks. On these tasks that are highly relevant for computational drug discovery, CHEF significantly outperforms all its competitors. 

## item_id: m_3356

TITLE: Relational Surrogate Loss Learning

ABSTRACT: Evaluation metrics in machine learning are often hardly taken as loss functions, as they could be non-differentiable and non-decomposable, e.g., average precision and F1 score. This paper aims to address this problem by revisiting the surrogate loss learning, where a deep neural network is employed to approximate the evaluation metrics. Instead of pursuing an exact recovery of the evaluation metric through a deep neural network, we are reminded of the purpose of the existence of these evaluation metrics, which is to distinguish whether one model is better or worse than another. In this paper, we show that directly maintaining the relation of models between surrogate losses and metrics suffices, and propose a rank correlation-based optimization method to maximize this relation and learn surrogate losses. Compared to previous works, our method is much easier to optimize and enjoys significant efficiency and performance gains. Extensive experiments show that our method achieves improvements on various tasks including image classification and neural machine translation, and even outperforms state-of-the-art methods on human pose estimation and machine reading comprehension tasks. Code is available at: https://github.com/hunto/ReLoss.

## item_id: m_3357

TITLE: AIR-Net: Adaptive and Implicit Regularization Neural Network for matrix completion

ABSTRACT: Conventionally, the matrix completion (MC) model aims to recover a matrix from partially observed elements. Accurate recovery necessarily requires a regularization encoding priors of the unknown matrix/signal properly. However, encoding the priors accurately for the complex natural signal is difficult, and even then, the model might not generalize well outside the particular matrix type. This work combines adaptive and implicit low-rank regularization that captures the prior dynamically according to the current recovered matrix. Furthermore, we aim to answer the question: how does adaptive regularization affect implicit regularization? We utilize neural networks to represent Adaptive and Implicit Regularization and named the proposed model \textit{AIR-Net}. Theoretical analyses show that the adaptive part of the AIR-Net enhances implicit regularization. In addition, the adaptive regularizer vanishes at the end, thus can avoid saturation issues. Numerical experiments for various data demonstrate the effectiveness of AIR-Net, especially when the locations of missing elements are not randomly chosen. With complete flexibility to select neural networks for matrix representation, AIR-Net can be extended to solve more general inverse problems.

## item_id: m_3358

TITLE: MGAN: Training Generative Adversarial Nets with Multiple Generators

ABSTRACT: We propose in this paper a new approach to train the Generative Adversarial Nets (GANs) with a mixture of generators to overcome the mode collapsing problem. The main intuition is to employ multiple generators, instead of using a single one as in the original GAN. The idea is simple, yet proven to be extremely effective at covering diverse data modes, easily overcoming the mode collapsing problem and delivering state-of-the-art results. A minimax formulation was able to establish among a classifier, a discriminator, and a set of generators in a similar spirit with GAN. Generators create samples that are intended to come from the same distribution as the training data, whilst the discriminator determines whether samples are true data or generated by generators, and the classifier specifies which generator a sample comes from. The distinguishing feature is that internal samples are created from multiple generators, and then one of them will be randomly selected as final output similar to the mechanism of a probabilistic mixture model. We term our method Mixture Generative Adversarial Nets (MGAN). We develop theoretical analysis to prove that, at the equilibrium, the Jensen-Shannon divergence (JSD) between the mixture of generators’ distributions and the empirical data distribution is minimal, whilst the JSD among generators’ distributions is maximal, hence effectively avoiding the mode collapsing problem. By utilizing parameter sharing, our proposed model adds minimal computational cost to the standard GAN, and thus can also efficiently scale to large-scale datasets. We conduct extensive experiments on synthetic 2D data and natural image databases (CIFAR-10, STL-10 and ImageNet) to demonstrate the superior performance of our MGAN in achieving state-of-the-art Inception scores over latest baselines, generating diverse and appealing recognizable objects at different resolutions, and specializing in capturing different types of objects by the generators.

## item_id: m_3359

TITLE: Interpreting Layered Neural Networks via Hierarchical Modular Representation

ABSTRACT: Interpreting the prediction mechanism of complex models is currently one of the most important tasks in the machine learning field, especially with layered neural networks, which have achieved high predictive performance with various practical data sets. To reveal the global structure of a trained neural network in an interpretable way, a series of clustering methods have been proposed, which decompose the units into clusters according to the similarity of their inference roles. The main problems in these studies were that (1) we have no prior knowledge about the optimal resolution for the decomposition, or the appropriate number of clusters, and (2) there was no method with which to acquire knowledge about whether the outputs of each cluster have a positive or negative correlation with the input and output dimension values. 
In this paper, to solve these problems, we propose a method for obtaining a hierarchical modular representation of a layered neural network. The application of a hierarchical clustering method to a trained network reveals a tree-structured relationship among hidden layer units, based on their feature vectors defined by their correlation with the input and output dimension values. 

## item_id: m_3360

TITLE: Efficient Wasserstein and Sinkhorn Policy Optimization

ABSTRACT: Trust-region methods based on Kullback-Leibler divergence are pervasively used to stabilize policy optimization in reinforcement learning. In this paper, we examine two natural extensions of policy optimziation with Wasserstein and Sinkhorn trust regions, namely Wasserstein policy optimization (WPO) and Sinkhorn policy optimization (SPO). Instead of restricting the policy to a parametric distribution class, we directly optimize the policy distribution and derive their close-form policy updates based on the Lagrangian duality. Theoretically, we show that WPO guarantees a monotonic performance improvement, and SPO provably converges to WPO as the entropic regularizer diminishes. Experiments across tabular domains and robotic locomotion tasks further demonstrate the performance improvement of both approaches, more robustness of WPO to sample insufficiency, and faster convergence of SPO, over state-of-art policy gradient methods.

## item_id: m_3361

TITLE: MMHU: A Massive-Scale Multimodal Benchmark for Human Behavior Understanding in Autonomous Driving

ABSTRACT: Humans are integral components of the transportation ecosystem, and understanding their behaviors is crucial to facilitating the development of safe driving systems. Although recent progress has explored various aspects of human behavior---such as motion, trajectories, and intention---a comprehensive benchmark for evaluating human behavior understanding in autonomous driving remains unavailable. In this work, we propose \textbf{MMHU}, a large-scale benchmark for human behavior analysis featuring rich annotations, such as human motion and trajectories, text description for human motions, human intention, and critical behavior labels relevant to driving safety. Our dataset encompasses 57k human motion clips and 1.73M frames gathered from diverse sources, including established driving datasets such as Waymo, in-the-wild videos from YouTube, and self-collected data. A human-in-the-loop annotation pipeline is developed to generate rich behavior captions. We provide a thorough dataset analysis and benchmark multiple tasks—ranging from motion prediction to motion generation and human behavior question answering—thereby offering a broad evaluation suite. Our dataset will be released to promote further human-centric research in this vital area of autonomous driving.

## item_id: m_3362

TITLE: Self-learning Compositional Representations for Zero-shot Chinese Character Recognition

ABSTRACT: Chinese character recognition has been a longstanding research topic and remains essential in visual tasks like ancient manuscript recognition. Chinese character recognition faces numerous challenges, particularly the issue of zero-shot characters. Existing Chinese zero-shot character recognition methods primarily focus on the radical or stroke decomposition. However, radical-based methods still struggle to solve zero-shot radicals, while stroke-based ones are hard to perceive fine-grained information. Besides, previous methods can hardly generalize to characters of other languages. In this paper, we propose a novel Self-learning Compositional Representation method for zero-shot Chinese Character Recognition (SCR-CCR). SCR-CCR learns compositional components automatically from the data, which are not aligned with human-defined radical or stroke decomposition methods. SCR-CCR follows the pretraining-inference paradigm. First, we train a Character Slot Attention (ChSA) via pure feature reconstruction loss to parse appropriate components from character images. Then we recognize zero-shot characters without finetuning or retraining in the inference stage by comparing components between input and example images. To evaluate the proposed method, we conduct experiments of zero-shot character recognition. The experiments illustrate that SCR-CCR outperforms previous methods in most cases of character and radical zero-shot settings. In particular, visualization experiments indicate that the components learned by SCR-CCR reflect the structure of characters in an interpretable way, and can be used to recognize Japanese and Korean characters.

## item_id: m_3363

TITLE: Taming the Judge: Deconflicting AI Feedback for Stable Reinforcement Learning

ABSTRACT: Aligning language models using LLM judge feedback offers a scalable alternative to human annotation, yet is plagued by judgment inconsistencies that destabilize reinforcement learning. While prior work has focused on judge accuracy, the critical issue of logical coherence—particularly preference cycles ($A \succ B \succ C \succ A$)—has been largely unaddressed. To address this gap, this work introduces an end-to-end framework to systematically detect and resolve these inconsistencies within the reinforcement learning training loop. Our framework features two core contributions: the \textbf{Conflict Detection Rate (CDR)}, a novel metric to quantify judgment conflicts, and \textbf{Deconflicted Graph Rewards (DGR)}, a signal-purification framework that eliminates cycles before policy optimization. DGR constructs preference graphs from raw judgments, transforms them into conflict-free Directed Acyclic Graphs (DAGs), and generates a logically coherent reward signal compatible with any policy optimizer. Experiments confirm that our framework significantly improves training stability and model performance over strong baselines, establishing logical consistency as a crucial and now-addressable dimension of AI feedback. The code for our method is available at \url{https://anonymous.4open.science/status/DGR-E5DA}.

## item_id: m_3364

TITLE: GANITE: Estimation of Individualized Treatment Effects using Generative Adversarial Nets

ABSTRACT: Estimating individualized treatment effects (ITE) is a challenging task due to the need for an individual's potential outcomes to be learned from biased data and without having access to the counterfactuals. We propose a novel method for inferring ITE based on the Generative Adversarial Nets (GANs) framework. Our method, termed Generative Adversarial Nets for inference of Individualized Treatment Effects (GANITE), is motivated by the possibility that we can capture the uncertainty in the counterfactual distributions by attempting to learn them using a GAN. We generate proxies of the counterfactual outcomes using a counterfactual generator, G, and then pass these proxies to an ITE generator, I, in order to train it. By modeling both of these using the GAN framework, we are able to infer based on the factual data, while still accounting for the unseen counterfactuals. We test our method on three real-world datasets (with both binary and multiple treatments) and show that GANITE outperforms state-of-the-art methods.

## item_id: m_3365

TITLE: Empirical Analysis of the Hessian of Over-Parametrized Neural Networks

ABSTRACT: We study the properties of common loss surfaces through their Hessian matrix. In particular, in the context of deep learning, we empirically show that the spectrum of the Hessian is composed of two parts: (1) the bulk centered near zero, (2) and outliers away from the bulk. We present numerical evidence and mathematical justifications to the following conjectures laid out by Sagun et. al. (2016): Fixing data, increasing the number of parameters merely scales the bulk of the spectrum; fixing the dimension and changing the data (for instance adding more clusters or making the data less separable) only affects the outliers. We believe that our observations have striking implications for non-convex optimization in high dimensions. First, the *flatness* of such landscapes (which can be measured by the singularity of the Hessian) implies that classical notions of basins of attraction may be quite misleading. And that the discussion of wide/narrow basins may be in need of a new perspective around over-parametrization and redundancy that are able to create *large* connected components at the bottom of the landscape. Second, the dependence of a small number of large eigenvalues to the data distribution can be linked to the spectrum of the covariance matrix of gradients of model outputs. With this in mind, we may reevaluate the connections within the data-architecture-algorithm framework of a model, hoping that it would shed light on the geometry of high-dimensional and non-convex spaces in modern applications. In particular, we present a case that links the two observations: small and large batch gradient descent appear to converge to different basins of attraction but we show that they are in fact connected through their flat region and so belong to the same basin.

## item_id: m_3366

TITLE: Opening the vocabulary of  neural language models with character-level word representations

ABSTRACT: This paper introduces an architecture for an open-vocabulary neural language model. Word representations are computed on-the-fly by a convolution network followed by pooling layer. This allows the model to consider any word, in the context or for the prediction. The training objective is derived from the Noise-Contrastive Estimation to circumvent the lack of vocabulary. We test the ability of our model to build representations of unknown words on the MT task of IWSLT-2016 from English to Czech, in a reranking setting. Experimental results show promising results, with a gain up to 0.7 BLEU point. They also emphasize the difficulty and instability when training such models with character-based representations for the predicted words.

## item_id: m_3367

TITLE: FFT-Accelerated Auxiliary Variable MCMC for Fermionic Lattice Models: A Determinant-Free Approach with $O(N \log N)$ Complexity

ABSTRACT: We introduce a Markov Chain Monte Carlo (MCMC) algorithm that dramatically accelerates the simulation of quantum many-body systems, a grand challenge in computational science. State-of-the-art methods for these problems are severely limited by $O(N^3)$ computational complexity. Our method avoids this bottleneck, achieving near-linear \textbf{$O(N \log N)$} scaling per sweep.

Our approach samples a joint probability measure over two coupled variable sets: (1) particle trajectories of the fundamental fermions, and (2) auxiliary variables that decouple fermion interactions. The key innovation is a novel transition kernel for particle trajectories formulated in the Fourier domain, revealing the transition probability as a convolution that enables massive acceleration via the Fast Fourier Transform (FFT). The auxiliary variables admit closed-form, factorized conditional distributions, enabling efficient exact Gibbs sampling update.

We validate our algorithm on benchmark quantum physics problems, accurately reproducing known theoretical results and matching traditional $O(N^3)$ algorithms on $32\times 32$ lattice simulations at a fraction of the wall-clock time, empirically demonstrating $N \log N$ scaling. By reformulating a long-standing physics simulation problem in machine learning language, our work provides a powerful tool for large-scale probabilistic inference and opens avenues for physics-inspired generative models.

## item_id: m_3368

TITLE: Critical Points in Quantum Generative Models

ABSTRACT: One of the most important properties of neural networks is the clustering of local minima of the loss function near the global minimum, enabling efficient training. Though generative models implemented on quantum computers are known to be more expressive than their traditional counterparts, it has empirically been observed that these models experience a transition in the quality of their local minima. Namely, below some critical number of parameters, all local minima are far from the global minimum in function value; above this critical parameter count, all local minima are good approximators of the global minimum. Furthermore, for a certain class of quantum generative models, this transition has empirically been observed to occur at parameter counts exponentially large in the problem size, meaning practical training of these models is out of reach. Here, we give the first proof of this transition in trainability, specializing to this latter class of quantum generative model. We use techniques inspired by those used to study the loss landscapes of classical neural networks. We also verify that our analytic results hold experimentally even at modest model sizes.

## item_id: m_3369

TITLE: ACCELERATING VARIATIONAL QUANTUM ALGORITHMS WITH MULTIPLE QUANTUM PROCESSORS

ABSTRACT: Variational quantum algorithms (VQAs) are prime contenders that exploit near-term quantum machines to gain computational advantages over classical algorithms. As such, how to accelerate the optimization of modern VQAs has attracted great attention in past years. Here we propose a \texttt{QU}antum \texttt{DI}stributed \texttt{O}ptimization scheme (abbreviated as QUDIO) to address this issue. Conceptually, QUDIO utilizes a classical central server to partition the learning problem into multiple subproblems and allocate them to a set of quantum local nodes. In the training stage, all local nodes proceed with parallel training and the classical server synchronizes optimization information among local nodes timely. In doing so, we prove a sublinear convergence rate of QUDIO in the number of global iterations under the ideal scenario. Moreover, when the imperfection of the quantum system is considered, we prove that an increased synchronization time leads to a degraded convergence rate or even incurs divergent optimization. Numerical results on standard benchmarks illustrate that QUDIO can surprisingly reach a superlinear clock-time speedup in terms of the number of local nodes. Our proposal can be readily mixed with other advanced VQAs-based techniques to narrow the gap between the state of the art and applications with the quantum advantage. 

## item_id: m_3370

TITLE: Self-Organization adds application robustness to deep learners

ABSTRACT: While self-organizing principles have motivated much of early learning models, such principles have rarely been included in deep learning architectures. Indeed, from a supervised learning perspective it seems that topographic constraints are rather decremental to optimal performance. Here we study a network model that incorporates self-organizing maps into a supervised network and show how gradient learning results in a form of a self-organizing learning rule. Moreover, we show that such a model is robust in the sense of its application to a variety of  areas, which is believed to be a hallmark of biological learning systems. 

## item_id: m_3371

TITLE: On the Geometric Selection of Landmarks for Low-Rank Self-Attention Approximation

ABSTRACT: Nystr{\"o}m-based approximation is a prominent strategy for achieving linear-time self-attention, yet its standard reliance on uniform random sampling is often misaligned with the non-uniform spectral properties of learned token embeddings. This work provides a rigorous basis for a data-aware, geometric sampling strategy that directly exploits this structure. We introduce and formalize \textit{block-coherence}, a spectral property of matrices where statistical leverage is concentrated within discoverable clusters. We then prove our main theoretical result: for matrices exhibiting this property, landmark selection via \textit{k-means clustering} achieves a provably tighter Frobenius norm approximation bound than uniform sampling. Our proof establishes a formal connection between the variance-minimizing k-means objective and the concentration of leverage scores, showing that k-means acts as an effective proxy for adaptive importance sampling. A multi-tiered empirical study validates our theory. We first verify that block-coherence is a consistent, emergent property of diverse architectures (BERT, Llama, ViT). We then demonstrate that this structure yields a 25-35\% reduction in Nystr{\"o}m reconstruction error over random sampling. Finally, our algorithmic realization, \textit{Geometric Progressive Attention (GPA)}, achieves state-of-the-art performance among efficient methods on the Long Range Arena (LRA) benchmark, demonstrating that superior approximation quality translates directly to improved downstream performance.

## item_id: m_3372

TITLE: Simultaneous Best-Response Dynamics in Random Potential Games

ABSTRACT: This paper examines the convergence behaviour of simultaneous best-response dynamics in random potential games and random near-potential games. We provide a theoretical result showing that, for two-player games with sufficiently many actions, the dynamics converge quickly to a cycle of length two. This cycle lies within the intersection of the neighbourhoods of two distinct Nash equilibria. For three players or more, simulations show that the dynamics converge quickly to a Nash equilibrium with high probability. Furthermore, we show that all these results are robust, in the sense that they hold in non-potential games, provided the players' payoffs are sufficiently correlated.
We also compare these dynamics to gradient-based learning methods in near-potential games with three players or more, and observe that simultaneous best-response dynamics converge to a Nash equilibrium of comparable payoff substantially faster.

## item_id: m_3373

TITLE: Neural Machine Translation with Latent Semantic of Image and Text

ABSTRACT: Although attention-based Neural Machine Translation have achieved great success, attention-mechanism cannot capture the entire meaning of the source sentence because the attention mechanism generates a target word depending heavily on the relevant parts of the source sentence. The report of earlier studies has introduced a latent variable to capture the entire meaning of sentence and achieved improvement on attention-based Neural Machine Translation. We follow this approach and we believe that the capturing meaning of sentence benefits from image information because human beings understand the meaning of language not only from textual information but also from perceptual information such as that gained from vision. As described herein, we propose a neural machine translation model that introduces a continuous latent variable containing an underlying semantic extracted from texts and images. Our model, which can be trained end-to-end, requires image information only when training. Experiments conducted with an English–German translation task show that our model outperforms over the baseline.

## item_id: m_3374

TITLE: FUNCTIONAL VARIATIONAL BAYESIAN NEURAL NETWORKS

ABSTRACT: Variational Bayesian neural networks (BNN) perform variational inference over weights, but it is difficult to specify meaningful priors and approximating posteriors in a high-dimensional weight space. We introduce functional variational Bayesian neural networks (fBNNs), which maximize an Evidence Lower BOund (ELBO) defined directly on stochastic processes, i.e. distributions over functions. We prove that the KL divergence between stochastic processes is equal to the supremum of marginal KL divergences over all finite sets of inputs. Based on this, we introduce a practical training objective which approximates the functional ELBO using finite measurement sets and the spectral Stein gradient estimator. With fBNNs, we can specify priors which entail rich structure, including Gaussian processes and implicit stochastic processes. Empirically, we find that fBNNs extrapolate well using various structured priors, provide reliable uncertainty estimates, and can scale to large datasets.

## item_id: m_3375

TITLE: Burstormer: Burst Image Restoration and Enhancement Transformer

ABSTRACT: On a shutter press, modern handheld cameras capture multiple images in rapid succession and merge them to generate a single image. However, individual frames in a burst are misaligned due to inevitable motions and contain multiple degradations. The challenge is to properly align the successive image shots and merge their complimentary information to achieve high-quality outputs. Towards this direction, we propose Burstormer: a novel transformer-based architecture for burst image restoration and enhancement. In comparison to existing works, our approach exploits multi-scale local and non-local features to achieve improved alignment and feature fusion. Our key idea is to enable inter-frame communication in the burst neighborhoods for information aggregation and progressive fusion while modeling the burst-wide context. However, the input burst frames need to be properly aligned before fusing their information. Therefore, we propose an enhanced deformable alignment module for aligning burst features with regards to the reference frame. Unlike existing techniques, the proposed alignment module not only aligns burst features but also exchanges feature information and maintains focused communication with the reference frame through the proposed reference-based feature enrichment mechanism. This additional exchange of information helps in aligning multi-frame features under complex motions. After multi-level alignment and enrichment, we re-emphasize on inter-frame communication within burst frames using a new cyclic burst sampling technique. Finally, the inter-frame information is aggregated using our proposed burst feature fusion module followed by progressive increase in the spatial resolution by shuffling the feature information available in burst frames. The proposed Burstormer outperforms the existing state-of-the-art approaches on three popular tasks of burst super-resolution, burst denoising and burst low-light enhancement. Our codes will
be made public.

## item_id: m_3376

TITLE: Opportunistic Learning: Budgeted Cost-Sensitive Learning from Data Streams

ABSTRACT: In many real-world learning scenarios, features are only acquirable at a cost constrained under a budget. In this paper, we propose a novel approach for cost-sensitive feature acquisition at the prediction-time. The suggested method acquires features incrementally based on a context-aware feature-value function. We formulate the problem in the reinforcement learning paradigm, and introduce a reward function based on the utility of each feature. Specifically, MC dropout sampling is used to measure expected variations of the model uncertainty which is used as a feature-value function. Furthermore, we suggest sharing representations between the class predictor and value function estimator networks. The suggested approach is completely online and is readily applicable to stream learning setups. The solution is evaluated on three different datasets including the well-known MNIST dataset as a benchmark as well as two cost-sensitive datasets: Yahoo Learning to Rank and a dataset in the medical domain for diabetes classification. According to the results, the proposed method is able to efficiently acquire features and make accurate predictions. 

## item_id: m_3377

TITLE: ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution

ABSTRACT: Recently, large language models (LLMs) have shown remarkable reasoning abilities by producing long reasoning traces. However, as the sequence length grows, the key-value (KV) cache expands linearly, incurring significant memory and computation costs. Existing cache eviction methods mitigate this issue by discarding less important KV pairs, but often fail to capture complex KV dependencies, resulting in performance degradation. To better balance efficiency and performance, we introduce ForesightKV, a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations. We first design the Golden Eviction algorithm, which identifies the optimal eviction KV pairs at each step using future attention scores. These traces and the scores at each step are then distilled via supervised training with a Pairwise Ranking Loss. Furthermore, we formulate cache eviction as a Markov Decision Process and apply the GRPO algorithm to mitigate the significant language modeling loss increase on low-entropy tokens.  Experiments on AIME2024 and AIME2025 benchmarks with Qwen3-1.7B and Qwen3-4B demonstrate that ForesightKV consistently outperforms prior methods under only half the cache budget, while benefiting synergistically from both supervised and reinforcement learning approaches.

## item_id: m_3378

TITLE: Query-Reduction Networks for Question Answering

ABSTRACT: In this paper, we study the problem of question answering when reasoning over multiple facts is required. We propose Query-Reduction Network (QRN), a variant of Recurrent Neural Network (RNN) that effectively handles both short-term (local) and long-term (global) sequential dependencies to reason over multiple facts. QRN considers the context sentences as a sequence of state-changing triggers, and reduces the original query  to a more informed query as it observes each trigger (context sentence) through time. Our experiments show that QRN produces the state-of-the-art results in  bAbI QA and dialog tasks, and in a real goal-oriented dialog dataset. In addition, QRN formulation allows parallelization on RNN's time axis, saving an order of magnitude in time complexity for training and inference.  

## item_id: m_3379

TITLE: A Local Graph Limits Perspective on Sampling-Based GNNs

ABSTRACT: We propose a theoretical framework for training Graph Neural Networks (GNNs) on large input graphs via training on small, fixed-size sampled subgraphs. This framework is applicable to a wide range of models, including popular sampling-based GNNs, such as GraphSAGE and FastGCN.
Leveraging the theory of graph local limits, we prove that under mild assumptions, parameters learned from training sampling-based GNNs on small samples of a large input graph are within an $\epsilon$-neighborhood of the outcome of training the same architecture on the whole graph. We derive bounds on the number of samples, the size of the graph, and the training steps required as a function of $\epsilon$. Our results give a novel theoretical understanding for using sampling in training GNNs. They also suggest that by training GNNs on small samples of the input graph, practitioners can identify and select the best models, hyperparameters, and sampling algorithms more efficiently.
We empirically demonstrate our results on a node classification task on large citation graphs, observing that sampling-based GNNs trained on local subgraphs 12$\times$ smaller than the original graph achieve comparable performance to those trained on the input graph.

## item_id: m_3380

TITLE: Knowledge Distillation with Multi-granularity Mixture of Priors for Image Super-Resolution

ABSTRACT: Knowledge distillation (KD) is a promising yet challenging model compression approach that transmits rich learning representations from robust but resource-demanding teacher models to efficient student models. Previous methods for image super-resolution (SR) are often tailored to specific teacher-student architectures, limiting their potential for improvement and hindering broader applications. This work presents a novel KD framework for SR models, the multi-granularity Mixture of Priors Knowledge Distillation (MiPKD), which can be universally applied to a wide range of architectures at both feature and block levels. The teacher’s knowledge is effectively integrated with the student's feature via the Feature Prior Mixer, and the reconstructed feature propagates dynamically in the training phase with the Block Prior Mixer. Extensive experiments illustrate the significance of the proposed MiPKD technique.

## item_id: m_3381

TITLE: Randomized Entity-wise Factorization for Multi-Agent Reinforcement Learning

ABSTRACT: Real world multi-agent tasks often involve varying types and quantities of agents and non-agent entities; however, agents within these tasks rarely need to consider all others at all times in order to act effectively. Factored value function approaches have historically leveraged such independences to improve learning efficiency, but these approaches typically rely on domain knowledge to select fixed subsets of state features to include in each factor. We propose to utilize value function factoring with random subsets of entities in each factor as an auxiliary objective in order to disentangle value predictions from irrelevant entities. This factoring approach is instantiated through a simple attention mechanism masking procedure. We hypothesize that such an approach helps agents learn more effectively in multi-agent settings by discovering common trajectories across episodes within sub-groups of agents/entities. Our approach, Randomized Entity-wise Factorization for Imagined Learning (REFIL), outperforms all strong baselines by a significant margin in challenging StarCraft micromanagement tasks.

## item_id: m_3382

TITLE: Learning Robust Representations by Projecting Superficial Statistics Out

ABSTRACT: Despite impressive performance as evaluated on i.i.d. holdout data, deep neural networks depend heavily on superficial statistics of the training data and are liable to break under distribution shift. For example, subtle changes to the background or texture of an image can break a seemingly powerful classifier. Building on previous work on domain generalization, we hope to produce a classifier that will generalize to previously unseen domains, even when domain identifiers are not available during training. This setting is challenging because the model may extract many distribution-specific (superficial) signals together with distribution-agnostic (semantic) signals. To overcome this challenge, we incorporate the gray-level co-occurrence matrix (GLCM) to extract patterns that our prior knowledge suggests are superficial: they are sensitive to the texture but unable to capture the gestalt of an image. Then we introduce two techniques for improving our networks' out-of-sample performance. The first method is built on the reverse gradient method that pushes our model to learn representations from which the GLCM representation is not predictable. The second method is built on the independence introduced by projecting the model's representation onto the subspace orthogonal to GLCM representation's.
We test our method on the battery of standard domain generalization data sets and, interestingly, achieve comparable or better performance as compared to other domain generalization methods that explicitly require samples from the target distribution for training.

## item_id: m_3383

TITLE: Zero-Resource Multilingual Model Transfer: Learning What to Share

ABSTRACT: Modern natural language processing and understanding applications have enjoyed a great boost utilizing neural networks models. However, this is not the case for most languages especially low-resource ones with insufficient annotated training data. Cross-lingual transfer learning methods improve the performance on a low-resource target language by leveraging labeled data from other (source) languages, typically with the help of cross-lingual resources such as parallel corpora. In this work, we propose a zero-resource multilingual transfer learning model that can utilize training data in multiple source languages, while not requiring target language training data nor cross-lingual supervision. Unlike most existing methods that only rely on language-invariant features for cross-lingual transfer, our approach utilizes both language-invariant and language-specific features in a coherent way. Our model leverages adversarial networks to learn language-invariant features and mixture-of-experts models to dynamically exploit the relation between the target language and each individual source language. This enables our model to learn effectively what to share between various languages in the multilingual setup. It results in significant performance gains over prior art, as shown in an extensive set of experiments over multiple text classification and sequence tagging tasks including a large-scale real-world industry dataset.

## item_id: m_3384

TITLE: Realtime query completion via deep language models

ABSTRACT: Search engine users nowadays heavily depend on query completion and correction to shape their queries.  Typically, the completion is done by database lookup which does not understand the context and cannot generalize to prefixes not in the database. In the paper, we propose to use unsupervised deep language models to complete and correct the queries given an arbitrary prefix.  We show how to address two main challenges that renders this method practical for large-scale deployment: 1) we propose a method for integrating error correction into the language model completion via a edit-distance potential and a variant of beam search that can exploit these potential functions; and 2) we show how to efficiently perform CPU-based computation to complete the queries, with error correction, in real time (generating top 10 completions within 16 ms). Experiments show that the method substantially increases hit rate over standard approaches, and is capable of handling tail queries.


## item_id: m_3385

TITLE: What does it take to generate natural textures?

ABSTRACT: Natural image generation is currently one of the most actively explored fields in Deep Learning. Many approaches, e.g. for state-of-the-art artistic style transfer or natural texture synthesis, rely on the statistics of hierarchical representations in supervisedly trained deep neural networks. It is, however, unclear what aspects of this feature representation are crucial for natural image generation: is it the depth, the pooling or the training of the features on natural images? We here address this question for the task of natural texture synthesis and show that none of the above aspects are indispensable. Instead, we demonstrate that natural textures of high perceptual quality can be generated from networks with only a single layer, no pooling and random filters.

## item_id: m_3386

TITLE: Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts

ABSTRACT: As large language models (LLMs) are deployed in safety-critical settings, it is essential to ensure that their responses comply with safety standards. Prior research has revealed that LLMs often fail to grasp the notion of safe behaviors, resulting in either unjustified refusals to harmless prompts or the generation of harmful content. While substantial efforts have been made to improve their robustness, existing defenses often rely on costly fine-tuning of model parameters or employ suboptimal heuristic techniques. In this work, we take a novel approach to safeguard LLMs by learning to adapt the system prompts in instruction-tuned LLMs. While LLMs are typically pre-trained to follow a fixed system prompt, we investigate the impact of tailoring the system prompt to each specific user input on the safety of the responses. To this end, we propose Sysformer, a transformer model that updates an initial system prompt to a more robust system prompt in the LLM input embedding space while attending to the user prompt. While keeping the LLM parameters frozen, the Sysformer is trained to refuse to respond to a set of harmful prompts while responding ideally to a set of safe ones. Through extensive experiments on 5 LLMs from different families and 2 recent benchmarks, we demonstrate that Sysformer can significantly enhance the robustness of LLMs, leading to upto 80% gain in the refusal rate on harmful prompts while enhancing the compliance with the safe prompts by upto 90%. Results also generalize well to sophisticated jailbreaking attacks, making LLMs upto 100% more robust against different attack strategies. We hope our findings lead to cheaper safeguarding of LLMs and motivate future investigations into designing variable system prompts.

## item_id: m_3387

TITLE: CONTENT2VEC: SPECIALIZING JOINT REPRESENTATIONS OF PRODUCT IMAGES AND TEXT FOR THE TASK OF PRODUCT RECOMMENDATION

ABSTRACT: We propose a unified product embedded representation that is optimized for the task of retrieval-based product recommendation. We generate this representation using Content2Vec, a new deep architecture that merges product content infor- mation such as text and image and we analyze its performance on hard recom- mendation setups such as cold-start and cross-category recommendations. In the case of a normal recommendation regime where collaborative information signal is available we merge the product co-occurence information and propose a sec- ond architecture Content2vec+ and show its lift in performance versus non-hybrid approaches.

## item_id: m_3388

TITLE: CAUSAL NEURAL NETWORKS FOR CONTINUOUS TREATMENT EFFECT ESTIMATION

ABSTRACT: Causal inference have wide applications in medical decision-making, evaluating advertising, and voucher distribution. The exist of confounding effect makes it difficult to have an unbiased uplift estimation. 
Traditional methods focuses on the ordering of the problem. Little attention have been paid to the response performance, either on the evaluation metric, nor the modeling. 
In this work, an end-to-end multi-task deep neural network is proposed to capture the relations between the treatment propensity and the treatment effect, where the treatment can be continuous. 
The performance of the proposal is tested over large scale semi-synthetic and real-world data. 
The result shows that the proposal balances the estimation of response performance and individual treatment effect. 
The online environment implementation suggests the proposal can boost up the market scale and achieve 4.8% higher return over investment (ROI).

## item_id: m_3389

TITLE: Constraint-Driven Explanations of Black-Box ML Models

ABSTRACT: Modern machine learning techniques have enjoyed widespread success, but are plagued by lack of transparency in their decision making, which has led to the emergence of the field of explainable AI.  One popular approach called LIME, seeks to explain an opaque model's behavior, by training a surrogate interpretable model to be locally faithful on perturbed instances. 
Despite being model-agnostic and easy-to-use, it is known that LIME's explanations can be unstable and are susceptible to adversarial attacks as a result of Out-Of-Distribution (OOD) sampling. Quality of explanations is also calculated heuristically, and lacks a strong theoretical foundation. In spite of numerous attempts to remedy some of these issues, making the LIME framework more trustworthy and reliable remains an open problem.

In this work, we demonstrate that the OOD sampling problem stems  from rigidity of the perturbation procedure.  To resolve this issue, we propose a theoretically sound framework based on uniform sampling of user-defined subspaces. Through logical constraints, we afford the end-user the flexibility to delineate the precise subspace of the input domain to be explained. This not only helps mitigate the problem of OOD sampling, but also allow experts to drill down and uncover bugs deep inside the model. For testing the quality of generated explanations, we develop an efficient estimation algorithm that is able to certifiably measure the true value of metrics such as fidelity up to any desired degree of accuracy, which can help in building trust in the generated explanations. Our framework called CLIME can be applied to any ML model, and extensive experiments demonstrate its versatility on real-world problems.


## item_id: m_3390

TITLE: Learning Generative Image Object Manipulations from Language Instructions

ABSTRACT: The use of adequate feature representations is essential for achieving high performance in high-level human cognitive tasks in computational modeling. Recent developments in deep convolutional and recurrent neural networks architectures enable learning powerful feature representations from both images and natural language text. Besides, other types of networks such as Relational Networks (RN) can learn relations between objects and Generative Adversarial Networks (GAN) have shown to generate realistic images. In this paper, we combine these four techniques to acquire a shared feature representation of the relation between objects in an input image and an object manipulation action description in the form of human language encodings to generate an image that shows the resulting end-effect the action would have on a computer-generated scene. The system is trained and evaluated on a simulated dataset and experimentally used on real-world photos.

## item_id: m_3391

TITLE: SHADOWCAST: Controllable Graph Generation with Explainability

ABSTRACT: We introduce the problem of explaining graph generation, formulated as controlling the generative process to produce desired graphs with explainable structures. By directing this generative process, we can explain the observed outcomes. We propose SHADOWCAST, a controllable generative model capable of mimicking networks and directing the generation, as an approach to this novel problem. The proposed model is based on a conditional generative adversarial network for graph data. We design it with the capability to control the conditions using a simple and transparent Markov model. Comprehensive experiments on three real-world network datasets demonstrate our model's competitive performance in the graph generation task. Furthermore, we control SHADOWCAST to generate graphs of different structures to show its effective controllability and explainability. As the first work to pose the problem of explaining generated graphs by controlling the generation, SHADOWCAST paves the way for future research in this exciting area.

## item_id: m_3392

TITLE: Inductive Biases and Variable Creation in Self-Attention Mechanisms

ABSTRACT: Self-attention, an architectural motif designed to model long-range interactions in sequential data, has driven numerous recent breakthroughs in natural language processing and beyond. This work provides a theoretical analysis of the inductive biases of self-attention modules, where our focus is to rigorously establish which functions and long-range dependencies self-attention blocks prefer to represent. We show that bounded-norm Transformer layers create sparse variables: they can represent sparse Lipschitz functions of the input sequence, with sample complexity scaling only logarithmically with the context length. We propose new experimental protocols to support the analysis and guide the practice of training Transformers, built around the rich theory of learning sparse Boolean functions.

## item_id: m_3393

TITLE: Capacity of Deep Neural Networks under Parameter Quantization

ABSTRACT: Most deep neural networks (DNNs) require complex models to achieve high performance. Parameter quantization is widely used for reducing the implementation complexities. Previous studies on quantization were mostly based on extensive simulation using training data. We choose a different approach and attempt to measure the per-parameter capacity of DNN models and interpret the results to obtain insights on optimum quantization of parameters. This research uses artificially generated data and generic forms of fully connected DNNs, convolutional neural networks, and recurrent neural networks. We conduct memorization and classification tests to study the effects of the number and precision of the parameters on the performance. The model and the per-parameter capacities are assessed by measuring the mutual information between the input and the classified output. We also extend the memorization capacity measurement results to image classification and language modeling tasks. To get insight for parameter quantization when performing real tasks, the training and test performances are compared.

## item_id: m_3394

TITLE: Diet Networks: Thin Parameters for Fat Genomics

ABSTRACT: Learning tasks such as those involving genomic data often poses a serious challenge: the number of input features can be orders of magnitude larger than the number of training examples, making it difficult to avoid overfitting, even when using the known regularization techniques. We focus here on tasks in which the input is a description of the genetic variation specific to a patient, the single nucleotide polymorphisms (SNPs), yielding millions of ternary inputs. Improving the ability of deep learning to handle such datasets could have an important impact in medical research, more specifically in precision medicine, where high-dimensional data regarding a particular patient is used to make predictions of interest. Even though the amount of data for such tasks is increasing, this mismatch between the number of examples and the number of inputs remains a concern. Naive implementations of classifier neural networks involve a huge number of free parameters in their first layer (number of input features times number of hidden units): each input feature is associated with as many parameters as there are hidden units. We propose a novel neural network parametrization which considerably reduces the number of free parameters. It is based on the idea that we can first learn or provide a distributed representation for each input feature (e.g. for each position in the genome where variations are observed in data), and then learn (with another neural network called the parameter prediction network) how to map a feature's distributed representation (based on the feature's identity not its value) to the vector of parameters specific to that feature in the classifier neural network (the weights which link the value of the feature to each of the hidden units). This approach views the problem of producing the parameters associated with each feature as a multi-task learning problem. We show experimentally on a population stratification task of interest to medical studies that the proposed approach can significantly reduce both the number of parameters and the error rate of the classifier.

## item_id: m_3395

TITLE: Learning Canonical Embedding for Non-rigid Shape Matching

ABSTRACT: This paper provides a novel framework that learns canonical embeddings for non-rigid shape matching. In contrast to prior work in this direction, our framework is trained end-to-end and thus avoids instabilities and constraints associated with the commonly-used Laplace-Beltrami basis or sequential optimization schemes. On multiple datasets, we demonstrate that learning self symmetry maps with a deep functional map projects 3D shapes into a low dimensional canonical embedding that facilitates non-rigid shape correspondence via a simple nearest neighbor search. Our framework outperforms multiple recent learning based methods on FAUST and SHREC benchmarks while being computationally cheaper, data-efficient, and robust.

## item_id: m_3396

TITLE: Data Valuation using Reinforcement Learning

ABSTRACT: Quantifying the value of data is a fundamental problem in machine learning. Data valuation has multiple important use cases: (1) building insights about the learning task, (2) domain adaptation, (3) corrupted sample discovery, and (4) robust learning. To adaptively learn data values jointly with the target task predictor model, we propose a meta learning framework which we name Data Valuation using Reinforcement Learning (DVRL). We employ a data value estimator (modeled by a deep neural network) to learn how likely each datum is used in training of the predictor model. We train the data value estimator using a reinforcement signal of the reward obtained on a small validation set that reflects performance on the target task. We demonstrate that DVRL yields superior data value estimates compared to alternative methods across different types of datasets and in a diverse set of application scenarios. The corrupted sample discovery performance of DVRL is close to optimal in many regimes (i.e. as if the noisy samples were known apriori), and for domain adaptation and robust learning DVRL significantly outperforms state-of-the-art by 14.6% and 10.8%, respectively. 

## item_id: m_3397

TITLE: Anytime Neural Network: a Versatile Trade-off Between Computation and Accuracy

ABSTRACT: We present an approach for anytime predictions in deep neural networks (DNNs). For each test sample, an anytime predictor produces a coarse result quickly, and then continues to refine it until the test-time computational budget is depleted. Such predictors can address the growing computational problem of DNNs by automatically adjusting to varying test-time budgets. In this work, we study a \emph{general} augmentation to feed-forward networks to form anytime neural networks (ANNs) via auxiliary predictions and losses. Specifically, we point out a blind-spot in recent studies in such ANNs: the importance of high final accuracy. In fact, we show on multiple recognition data-sets and architectures that by having near-optimal final predictions in small anytime models, we can effectively double the speed of large ones to reach corresponding accuracy level. We achieve such speed-up with simple weighting of anytime losses that oscillate during training. We also assemble a sequence of exponentially deepening ANNs, to achieve both theoretically and practically near-optimal anytime results at any budget, at the cost of a constant fraction of additional consumed budget.

## item_id: m_3398

TITLE: ScheduleNet: Learn to Solve MinMax mTSP Using Reinforcement Learning with Delayed Reward

ABSTRACT: Combinatorial Optimization (CO) problems are theoretically challenging yet crucial in practice. Numerous works used Reinforcement Learning (RL) to tackle these CO problems. As current approaches mainly focus on single-worker CO problems such as the famous Travelling Salesman Problem (TSP), we focus on more practical extension of TSP to multi-worker (salesmen) setting, specifically MinMax mTSP. From the RL perspective, Minmax mTSP raises several significant challenges, such as the cooperation of multiple workers and the need for a well-engineered reward function. In this paper, we present the RL framework with (1) worker-task heterograph and type-aware Graph Neural Network, and (2) the RL training method that is stable, has fast convergence speed, and directly optimizes the objective of MinMax mTSP in a delayed reward setting. We achieve comparable performance to a highly optimized meta-heuristic baseline, OR-Tools, and outperforms it in 10% of the cases, both on in-training and out-of-training problem distributions. Moreover, our problem formulation enables us to solve problems with any number of salesmen (workers) and cities.

## item_id: m_3399

TITLE: Multi-Precision Policy Enforced Training (MuPPET) : A precision-switching strategy for quantised fixed-point training of CNNs

ABSTRACT: Large-scale convolutional neural networks (CNNs) suffer from very long training times,  spanning from hours to weeks, limiting the productivity and experimentation of deep learning practitioners.  As networks grow in size and complexity one approach  of  reducing  training  time  is  the  use  of  low-precision  data  representation and computations during the training stage.  However, in doing so the final accuracy suffers due to the problem of vanishing gradients.  Existing state-of-the-art methods combat this issue by means of a mixed-precision approach employing two different precision levels, FP32 (32-bit floating-point precision) and FP16/FP8 (16-/8-bit floating-point precision), leveraging the hardware support of recent GPU architectures for FP16 operations to obtaining performance gains. This work pushes the boundary of quantised training by employing a multilevel optimisation approach that utilises multiple precisions including low-precision fixed-point representations.  The training strategy, named MuPPET, combines the use of  multiple  number  representation regimes  together  with  a  precision-switching mechanism that decides at run time the transition between different precisions. Overall, the proposed strategy tailors the training process to the hardware-level capabilities of the utilised hardware architecture and yields improvements in training time and energy efficiency compared to state-of-the-art approaches. Applying MuPPET on the training of AlexNet, ResNet18 and GoogLeNet on ImageNet (ILSVRC12) and targeting an NVIDIA Turing GPU, the proposed method achieves the same accuracy as the standard full-precision training with an average training-time speedup of 1.28× across the networks.

## item_id: m_3400

TITLE: Rethinking Knowledge Distillation via Cross-Entropy

ABSTRACT: Knowledge Distillation (KD) has developed extensively and boosted various tasks. The classical KD method adds the KD loss to the original cross-entropy (CE) loss. We try to decompose the KD loss to explore its relation with the CE loss. Surprisingly, we find it can be regarded as a combination of the CE loss and an extra loss which has the identical form as the CE loss. However, we notice the extra loss forces the student's relative probability to learn the teacher's absolute probability. Moreover, the sum of the two probabilities is different, making it hard to optimize. To address this issue, we revise the formulation and propose a distributed loss. In addition, we utilize teachers' target output as the soft target, proposing the soft loss. Combining the soft loss and the distributed loss, we propose a new KD loss (NKD). Furthermore, we smooth students' target output to treat it as the soft target for training without teachers and propose a teacher-free new KD loss (tf-NKD). Our method achieves state-of-the-art performance on CIFAR-100 and ImageNet. For example, with ResNet-34 as the teacher, we boost the ImageNet Top-1 accuracy of ResNet18 from 69.90% to 71.96%. In training without teachers, MobileNet, ResNet-18 and SwinTransformer-Tiny achieve 70.04%, 70.76%, and 81.48%, which are 0.83%, 0.86%, and 0.30% higher than the baseline, respectively.
