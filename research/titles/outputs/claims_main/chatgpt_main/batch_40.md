# Batch 40 — 81 items

## item_id: m_3901

TITLE: Volumetric Convolution: Automatic Representation Learning in Unit Ball

ABSTRACT: Convolution is an efficient technique to obtain abstract feature representations using hierarchical layers in deep networks. Although performing convolution in Euclidean geometries is fairly straightforward, its extension to other topological spaces---such as a sphere S^2 or a unit ball B^3---entails unique challenges. In this work, we propose a novel `"volumetric convolution" operation that can effectively convolve arbitrary functions in B^3. We develop a theoretical framework for "volumetric convolution" based on Zernike polynomials and efficiently implement it as a differentiable and an easily pluggable layer for deep networks. Furthermore, our formulation leads to derivation of a  novel formula to measure the symmetry of a function in B^3 around an arbitrary axis, that is useful in 3D shape analysis tasks. We demonstrate the efficacy of proposed volumetric convolution operation on a possible use-case i.e., 3D object recognition task.

## item_id: m_3902

TITLE: TailMix: Overcoming the Label Sparsity for Extreme Multi-label Classification

ABSTRACT: Extreme multi-label classification (XMC) aims at finding the most relevant labels from a huge label set at the industrial scale. The XMC problem inherently poses two challenges: data scalability and label sparsity. This work introduces a new augmentation method, namely TailMix, to address the label sparsity issue, i.e., the long-tail labels in XMC have few positive instances. TailMix utilizes the context vector generated from the label attention layer in a label-wise manner instead of using the existing Mixup methods in a sample-wise manner. In this process, TailMix selectively chooses two context vectors and augments the most plausible positive instances to improve the accuracy for long-tail labels. Despite the simplicity of TailMix, extensive experimental results show that TailMix consistently improves the baseline models without TailMix and other Mixup-based methods on three benchmark datasets. Notably, TailMix is effective for improving the performance for long-tail labels on PSP@k and PSN@k, which are the common metrics that reflect the propensity of labels.

## item_id: m_3903

TITLE: Short and Deep: Sketching and Neural Networks

ABSTRACT: Data-independent methods for dimensionality reduction such as random projections, sketches, and feature hashing have become increasingly popular in recent years.  These methods often seek to reduce dimensionality while preserving the hypothesis class, resulting in inherent lower bounds on the size of projected data.  For example, preserving linear separability requires $\Omega(1/\gamma^2)$ dimensions, where $\gamma$ is the margin, and in the case of polynomial functions, the number of required dimensions has an exponential dependence on the polynomial degree.
                                                                                                                                                            
Despite these limitations, we show that the dimensionality can be reduced further while maintaining performance guarantees, using improper learning with a slightly larger hypothesis class. In particular, we show that any sparse polynomial function of a sparse binary vector can be computed from a compact sketch by a single-layer neural network, where the sketch size has a logarithmic dependence on the polynomial degree.
                                                                                                                                                           
A practical consequence is that networks trained on sketched data are compact, and therefore suitable for settings with memory and power constraints. We empirically show that our approach leads to networks with fewer parameters than related methods such as feature hashing, at equal or better performance.

## item_id: m_3904

TITLE: Improving Non-Transferable Representation Learning by Harnessing Content and Style

ABSTRACT: Non-transferable learning (NTL) aims to restrict the generalization of models toward the target domain(s). To this end, existing works learn non-transferable representations by reducing statistical dependence between the source and target domain. However, such statistical methods essentially neglect to distinguish between *styles* and *contents*, leading them to inadvertently fit (i) spurious correlation between *styles* and *labels*, and (ii) fake independence between *contents* and *labels*. Consequently, their performance will be limited when natural distribution shifts occur or malicious intervention is imposed. In this paper, we propose a novel method (dubbed as H-NTL) to understand and advance the NTL problem by introducing a causal model to separately model *content* and *style* as two latent factors, based on which we disentangle and harness them as guidances for learning non-transferable representations with intrinsically causal relationships. Speciﬁcally, to avoid fitting spurious correlation and fake independence, we propose a variational inference framework to disentangle the naturally mixed *content factors* and *style factors* under our causal model. Subsequently, based on dual-path knowledge distillation, we harness the disentangled two *factors* as guidances for non-transferable representation learning: (i) we constraint the source domain representations to fit *content factors* (which are the intrinsic cause of *labels*), and (ii) we enforce that the target domain representations fit *style factors* which barely can predict labels. As a result, the learned feature representations follow optimal untransferability toward the target domain and minimal negative influence on the source domain, thus enabling better NTL performance. Empirically, the proposed H-NTL signiﬁcantly outperforms competing methods by a large margin.

## item_id: m_3905

TITLE: UaiNets: From Unsupervised to Active Deep Anomaly Detection

ABSTRACT: This work presents a method for active anomaly detection which can be built upon existing deep learning solutions for unsupervised anomaly detection. We show that a prior needs to be assumed on what the anomalies are, in order to have performance guarantees in unsupervised anomaly detection. We argue that active anomaly detection has, in practice, the same cost of unsupervised anomaly detection but with the possibility of much better results. To solve this problem, we present a new layer that can be attached to any deep learning model designed for unsupervised anomaly detection to transform it into an active method, presenting results on both synthetic and real anomaly detection datasets.

## item_id: m_3906

TITLE: Adversarial Training using Contrastive Divergence

ABSTRACT: To protect the security of machine learning models against adversarial examples, adversarial training becomes the most popular and powerful strategy against various adversarial attacks by injecting adversarial examples into training data. However, it is time-consuming and requires high computation complexity to generate suitable adversarial examples for ensuring the robustness of models, which impedes the spread and application of adversarial training. In this work, we reformulate adversarial training as a combination of stationary distribution exploring, sampling, and training. Each updating of parameters of DNN is based on several transitions from the data samples as the initial states in a Hamiltonian system. Inspired by our new paradigm, we design a new generative method for adversarial training by using Contrastive Divergence (ATCD), which approaches the equilibrium distribution of adversarial examples with only few iterations by building from small modifications of the standard Contrastive Divergence (CD). Our adversarial training algorithm achieves much higher robustness than any other state-of-the-art adversarial training acceleration method on the ImageNet, CIFAR-10, and MNIST datasets and reaches a balance between performance and efficiency.

## item_id: m_3907

TITLE: Exploiting Invariant Structures for Compression in Neural Networks

ABSTRACT: Modern neural networks often require deep compositions of high-dimensional nonlinear functions (wide architecture) to achieve high test accuracy, and thus can have overwhelming number of parameters. Repeated high cost in prediction at test-time makes neural networks ill-suited for devices with constrained memory or computational power. We introduce an efficient mechanism, reshaped tensor decomposition, to compress neural networks by exploiting three types of invariant structures: periodicity, modulation and low rank. Our reshaped tensor decomposition method exploits such invariance structures using a technique called tensorization (reshaping the layers into higher-order tensors) combined with higher order tensor decompositions on top of the tensorized layers. Our compression method improves low rank approximation methods and can be incorporated to (is complementary to) most of the existing compression methods for neural networks to achieve better compression. Experiments on LeNet-5 (MNIST), ResNet-32 (CI- FAR10) and ResNet-50 (ImageNet) demonstrate that our reshaped tensor decomposition outperforms (5% test accuracy improvement universally on CIFAR10) the state-of-the-art low-rank approximation techniques under same compression rate, besides achieving orders of magnitude faster convergence rates.

## item_id: m_3908

TITLE: Bag of Tricks to Boost Adversarial Transferability

ABSTRACT: Deep neural networks are widely known to be vulnerable to adversarial examples. However, vanilla adversarial examples generated under the white-box setting often exhibit low transferability across different models. Since adversarial transferability poses more severe threats to practical applications, various approaches have been proposed for better transferability, including gradient-based, input transformation-based, and model-related attacks. In this work, we find that several tiny changes in the existing adversarial attacks can significantly affect the attack performance, e.g., the number of iterations and step size. Based on careful studies of existing adversarial attacks, we propose a bag of tricks to enhance adversarial transferability, including momentum initialization, scheduled step size, dual example, spectral-based input transformation, and several ensemble strategies. Extensive experiments on the ImageNet dataset validate the high effectiveness of our proposed tricks and show that combining them can further boost adversarial transferability. Our work provides practical insights and techniques to enhance adversarial transferability and offers guidance to improve the attack performance on real-world applications through simple adjustments.

## item_id: m_3909

TITLE: ESQA: Event Sequences Question Answering

ABSTRACT: Event sequences (ESs) arise in many practical domains including finance, retail, social networks, and healthcare. In the context of machine learning, event sequences can be seen as a special type of tabular data with annotated timestamps. Despite the importance of ESs modeling and analysis, little effort was made in adapting large language models (LLMs) to the ESs domain. In this paper, we highlight the common difficulties of ESs processing and propose a novel solution capable of solving multiple downstream tasks with little or no finetuning. In particular, we solve the problem of working with long sequences and improve time and numeric features processing. The resulting method, called ESQA, effectively utilizes the power of LLMs and, according to extensive experiments, achieves state-of-the-art results in the ESs domain.

## item_id: m_3910

TITLE: Hierarchical Complement Objective Training

ABSTRACT: Hierarchical label structures widely exist in many machine learning tasks, ranging from those with explicit label hierarchies such as image classification to the ones that have latent label hierarchies such as semantic segmentation. Unfortunately, state-of-the-art methods often utilize cross-entropy loss which in-explicitly assumes the independence among class labels. Motivated by the fact that class members from the same hierarchy need to be similar to each others, we design a new training diagram called Hierarchical Complement Objective Training (HCOT). In HCOT, in addition to maximizing the probability of the ground truth class, we also neutralize the probabilities of rest of the classes in a hierarchical fashion, making the model take advantage of the label hierarchy explicitly. We conduct our method on both image classification and semantic segmentation. Results show that HCOT outperforms state-of-the-art models in CIFAR100, Imagenet, and PASCAL-context. Our experiments also demonstrate that HCOT can be applied on tasks with latent label hierarchies, which is a common characteristic in many machine learning tasks. 

## item_id: m_3911

TITLE: Generative Adversarial Parallelization

ABSTRACT: Generative Adversarial Networks (GAN) have become one of the most studied frameworks for unsupervised learning due to their intuitive formulation. They have also been shown to be capable of generating convincing examples in limited domains, such as low-resolution images. However, they still prove difficult to train in practice and tend to ignore modes of the data generating distribution. Quantitatively capturing effects such as mode coverage and more generally the quality of the generative model still remain elusive. We propose Generative Adversarial Parallelization (GAP), a framework in which many GANs or their variants are trained simultaneously, exchanging their discriminators. This eliminates the tight coupling between a generator and discriminator, leading to improved convergence and improved coverage of modes. We also propose an improved variant of the recently proposed Generative Adversarial Metric and show how it can score individual GANs or their collections under the GAP model.

## item_id: m_3912

TITLE: Assessing Generalization of SGD via Disagreement

ABSTRACT: We empirically show that the test error of deep networks can be estimated by training the same architecture on the same training set but with two different runs of Stochastic Gradient Descent (SGD), and then measuring the disagreement rate between the two networks on unlabeled test data. This builds on -- and is a stronger version of -- the observation in Nakkiran&Bansal 20, which requires the runs to be on separate training sets. We further theoretically show that this peculiar phenomenon arises from the well-calibrated nature of ensembles of SGD-trained models. This finding not only provides a simple empirical measure to directly predict the test error using unlabeled test data, but also establishes a new conceptual connection between generalization and calibration.

## item_id: m_3913

TITLE: STaSy: Score-based Tabular data Synthesis

ABSTRACT: Tabular data synthesis is a long-standing research topic in machine learning. Many different methods have been proposed over the past decades, ranging from statistical methods to deep generative methods. However, it has not always been successful due to the complicated nature of real-world tabular data. In this paper, we present a new model named $\textbf{S}$core-based $\textbf{Ta}$bular data $\textbf{Sy}$nthesis ($\texttt{STaSy}$) and its training strategy based on the paradigm of score-based generative modeling. Despite the fact that score-based generative models have resolved many issues in generative models, there still exists room for improvement in tabular data synthesis. Our proposed training strategy includes a self-paced learning technique and a fine-tuning strategy, which further increases the sampling quality and diversity by stabilizing the denoising score matching training. Furthermore, we also conduct rigorous experimental studies in terms of the generative task trilemma: sampling quality, diversity, and time. In our experiments with 15 benchmark tabular datasets and 7 baselines, our method outperforms existing methods in terms of task-dependant evaluations and diversity.


## item_id: m_3914

TITLE: A PRIVACY-PRESERVING IMAGE CLASSIFICATION FRAMEWORK WITH A LEARNABLE OBFUSCATOR

ABSTRACT: Real world images often contain large amounts of private / sensitive information that should be carefully protected without reducing their utilities. In this paper, we propose a privacy-preserving deep learning framework with a learnable ob- fuscator for the image classification task. Our framework consists of three mod- els: learnable obfuscator, classifier and reconstructor. The learnable obfuscator is used to remove the sensitive information in the images and extract the feature maps from them. The reconstructor plays the role as an attacker, which tries to recover the image from the feature maps extracted by the obfuscator. In order to best protect users’ privacy in images, we design an adversarial training methodol- ogy for our framework to optimize the obfuscator. Through extensive evaluations on real world datasets, both the numerical metrics and the visualization results demonstrate that our framework is qualified to protect users’ privacy and achieve a relatively high accuracy on the image classification task.

## item_id: m_3915

TITLE: A Frank-Wolfe Framework for Efficient and Effective Adversarial Attacks

ABSTRACT: Depending on how much information an adversary can access to, adversarial attacks can be classified as white-box attack and black-box attack. In both cases, optimization-based attack algorithms can achieve relatively low distortions and high attack success rates. However, they usually suffer from poor time and query complexities, thereby limiting their practical usefulness. In this work, we focus on the problem of developing efficient and effective optimization-based adversarial attack algorithms. In particular, we propose a novel adversarial attack framework for both white-box and black-box settings based on the non-convex Frank-Wolfe algorithm. We show in theory that the proposed attack algorithms are efficient with an $O(1/\sqrt{T})$ convergence rate. The empirical results of attacking Inception V3 model and ResNet V2 model on the ImageNet dataset also verify the efficiency and effectiveness of the proposed algorithms. More specific, our proposed algorithms attain the highest attack success rate in both white-box and black-box attacks among all baselines, and are more time and query efficient than the state-of-the-art.

## item_id: m_3916

TITLE: Generating Biased Datasets for Neural Natural Language Processing

ABSTRACT: In a time where neural networks are increasingly adopted in sensitive applications, algorithmic bias has emerged as an issue with moral implications. While there are myriad ways that a system may be compromised by bias, systematically isolating and evaluating existing systems on such scenarios is non-trivial, i.e., bias may be subtle, natural and inherently difficult to quantify. To this end, this paper proposes the first systematic study of benchmarking state-of-the-art neural models against biased scenarios. More concretely, we postulate that the bias annotator problem can be approximated with neural models, i.e., we propose generative models of latent bias to deliberately and unfairly associate latent features to a specific class. All in all, our framework provides a new way for principled quantification and evaluation of models against biased datasets. Consequently, we find that state-of-the-art NLP models (e.g., BERT, RoBERTa, XLNET) are readily compromised by biased data. 

## item_id: m_3917

TITLE: The Crossword Puzzle: Simplifying Deep Neural Network Pruning with Fabulous Coordinates

ABSTRACT: Pruning is a promising technique to shrink the size of Deep Neural Network models with only negligible accuracy overheads. Recent efforts rely on experience-derived metric to guide pruning procedure, which heavily saddles with the effective generalization of pruning methods. We propose The Cross Puzzle, a new method to simplify this procedure by automatically deriving pruning metrics. The key insight behind our method is that: \textit{For Deep Neural Network Models, a Pruning-friendly Distribution of model's weights can be obtained, given a proper Coordinate}. We experimentally confirm the above insight, and denote the new Coordinate as the Fabulous Coordinates. Our quantitative evaluation results show that: the Crossword Puzzle can find a simple yet effective metric, which outperforms the state-of-the-art pruning methods by delivering no accuracy degradation on ResNet-56 (CIFAR-10)/-101 (ImageNet), while the pruning rate is raised to 70\%/50\% for the respective models.

## item_id: m_3918

TITLE: Neural Code Completion

ABSTRACT: Code completion, an essential part of modern software development, yet can bechallenging for dynamically typed programming languages.  In this paper we ex-plore the use of neural network techniques to automatically learn code completionfrom  a  large  corpus  of  dynamically  typed  JavaScript  code.   We  show  differentneural networks that leverage not only token level information but also structuralinformation,  and  evaluate  their  performance  on  different  prediction  tasks.   Wedemonstrate that our models can outperform the state-of-the-art approach, whichis based on decision tree techniques, on both next non-terminal and next terminalprediction tasks by 3.8 points and 0.5 points respectively.  We believe that neuralnetwork techniques can play a transformative role in helping software developersmanage the growing complexity of software systems, and we see this work as afirst step in that direction.

## item_id: m_3919

TITLE: Make Memory Buffer Stronger in Continual Learning: A Continuous Neural Transformation Approach

ABSTRACT: Continual learning (CL) focuses on learning non-stationary data distribution without forgetting previous knowledge. However, the most widely used memory-replay approach often suffers from memory overfitting. To mitigate the memory overfitting, we propose a continuous and reversible memory transformation method so that the memory data is hard to overfit, thus improving generalization. The transformation is achieved by optimizing a bi-level optimization objective that jointly learns the CL model and memory transformer. Specifically, we propose a deterministic continuous memory transformer (DCMT) modeled by an ordinary differential equation, allowing for infinite memory transformation and generating diverse and hard memory data. Furthermore, we inject uncertainty into the transformation function and propose a stochastic continuous memory transformer (SCMT) modeled by a stochastic differential equation, which substantially enhances the diversity of the transformed memory buffer. The proposed neural transformation approaches have significant advantages over existing ones: (1) we can obtain infinite many transformed data, thus significantly increasing the memory buffer diversity; (2) the proposed continuous transformations are reversible, i.e., the original raw memory data could be restored from the transformed memory data without the need to make a replica of the memory data. Extensive experiments on both task-aware and task-free CL show significant improvement with our approach compared to strong baselines.  

## item_id: m_3920

TITLE: TransDreamer: Reinforcement Learning with Transformer World Models

ABSTRACT: The Dreamer agent provides various benefits of Model-Based Reinforcement Learning (MBRL) such as sample efficiency, reusable knowledge, and safe planning. However, its world model and policy networks inherit the limitations of recurrent neural networks and thus an important question is how an MBRL framework can benefit from the recent advances of transformers and what the challenges are in doing so. In this paper, we propose a transformer-based MBRL agent, called TransDreamer. We first introduce the Transformer State-Space Model, a world model that leverages a transformer for dynamics predictions. We then share this world model with a transformer-based policy network and obtain stability in training a transformer-based RL agent. In experiments, we apply the proposed model to 2D visual RL and 3D first-person visual RL tasks both requiring long-range memory access for memory-based reasoning. We show that the proposed model outperforms Dreamer in these complex tasks.

## item_id: m_3921

TITLE: Neural Networks Playing Dough: Investigating Deep Cognition With a Gradient-Based Adversarial Attack

ABSTRACT: Discovering adversarial examples has shaken our trust in the reliability of deep learning. Even though brilliant works have been devoted to understanding and fixing this vulnerability, fundamental questions (e.g. the mysterious generalization of adversarial examples across models and training sets) remain unanswered. This paper tests the hypothesis that it is not the neural networks failing in learning that causes adversarial vulnerability, but their different perception of the presented data. And therefore, adversarial examples should be semantic-sensitive signals which can provide us with an exceptional opening to understanding neural network learning. To investigate this hypothesis, I performed a gradient-based attack on fully connected feed-forward and convolutional neural networks, instructing them to minimally evolve controlled inputs into adversarial examples for all the classes of the MNIST and Fashion-MNIST datasets. Then I abstracted adversarial perturbations from these examples. The perturbations unveiled vivid and recurring visual structures, unique to each class and persistent over parameters of abstraction methods, model architectures, and training configurations. Furthermore, these patterns proved to be explainable and derivable from the corresponding dataset. This finding explains the generalizability of adversarial examples by, semantically, tying them to the datasets. In conclusion, this experiment not only resists interpretation of adversarial examples as deep learning failure but on the contrary, demystifies them in the form of supporting evidence for the authentic learning capacity of neural networks.

## item_id: m_3922

TITLE: Conversational Time Series Foundation Models: Towards Explainable and Effective Forecasting

ABSTRACT: The proliferation of time series foundation models has created a landscape where no single method achieves consistent superiority, framing the central challenge not as finding the best model, but as orchestrating an optimal ensemble with interpliability.  While Large Language Models (LLMs) offer powerful reasoning capabilities, their direct application to time series forecasting has proven ineffective. We address this gap by repositioning the LLM as an intelligent judge that evaluates, explains, and strategically coordinates an ensemble of foundation models. To overcome the LLM's inherent lack of domain-specific knowledge on time series, we introduce an R1-style finetuning process, guided by SHAP-based faithfulness scores, which teaches the model to interpret ensemble weights as meaningful causal statements about temporal dynamics. The trained agent then engages in iterative, multi-turn conversations to perform forward-looking assessments, provide causally-grounded explanations for its weighting decisions, and adaptively refine the optimization strategy. 
Validated on the GIFT-Eval benchmark on 23 datasets across 97 settings, our approach significantly outperforms leading time series foundation models on both CRPS and MASE metrics, establishing new state-of-the-art results.

## item_id: m_3923

TITLE: Regularizing hard examples improves robustness

ABSTRACT: Recent studies have validated that pruning hard-to-learn examples from training improves the generalization performance of neural networks (NNs). In this study, we investigate this intriguing phenomenon—the negative effect of hard examples on generalization—in adversarial training. Particularly, we theoretically demonstrate that the increase in the difficulty of hard examples in adversarial training is significantly greater than the increase in the difficulty of easy examples. Furthermore, we verify that hard examples are only fitted through memorization of the label in adversarial training and that the memorization of hard examples is attributed to the significant increase in the difficulty of hard examples. We find that the increased difficulty of hard examples brings about the functioning of hard examples as label corrupted data in adversarial training, thereby leading to the memorization of those hard examples and deterioration of the robustness performance. Based upon these observations, we propose a new approach, difficulty proportional label smoothing (DPLS), to mitigate the negative effect of hard examples, thereby improving the adversarial robustness of NNs. Notably, our experimental result indicates that our method can successfully leverage hard examples while circumventing the negative effect.

## item_id: m_3924

TITLE: PROS: Towards Compute-Efficient RLVR via Rollout Prefix Reuse

ABSTRACT: Large reasoning models (LRMs) trained with *Reinforcement Learning with Verifiable Rewards* (RLVR) have achieved remarkable progress on complex reasoning tasks. However, RLVR heavily relies on on-policy rollout generation, whose cost grows rapidly with rollout length and model size, eventually becoming the training bottleneck. Our empirical analysis reveals that independent rollouts for the same query often share similar early steps, indicating substantial redundancy. To address this, we propose **Pros** (**P**refix **R**euse for **O**n-policy **S**ampling), a paradigm that reuses promising prefixes of historical rollouts in RLVR training. **Pros** appends these self-generated partial rollouts to the original queries to form *Augmented Queries*, which are then used as regular training inputs in subsequent iterations, thereby reducing redundant computation. To select training batch from augmented queries, **Pros** adopts a hierarchical Bayesian model to estimate their pass rates and prioritize those with the highest reward uncertainty. Experiments across diverse settings show that **Pros** consistently improves training efficiency and achieves higher accuracy than strong baselines. These results highlight **Pros** as a practical path toward scalable and compute-efficient RLVR.

## item_id: m_3925

TITLE: Learning Perceptual Compression of Facial Video

ABSTRACT: We propose in this paper a new paradigm for facial video compression. We leverage the generative capacity of GANs such as StyleGAN to represent and compress each video frame (intra compression), as well as the successive differences between frames (inter compression). Each frame is inverted in the latent space of StyleGAN, where the optimal compression is learned. To do so, a diffeomorphic latent representation is learned using a normalizing flows model, where an entropy model can be optimized for image coding. In addition, we propose a new perceptual loss that is more efficient than other counterparts (LPIPS, VGG16). Finally, an entropy model for inter coding with residual is also learned in the previously constructed latent space. Our method (SGANC) is simple, faster to train, and achieves competitive results for image and video coding compared to state-of-the-art codecs such as VTM, AV1, and recent deep learning techniques.

## item_id: m_3926

TITLE: Large Scale Optimal Transport and Mapping Estimation

ABSTRACT: This paper presents a novel two-step approach for the fundamental problem of learning an optimal map from one distribution to another. First, we learn an optimal transport (OT) plan, which can be thought as a one-to-many map between the two distributions. To that end, we propose a stochastic dual approach of regularized OT, and show empirically that it scales better than a recent related approach when the amount of samples is very large. Second, we estimate a Monge map as a deep neural network learned by approximating the barycentric projection of the previously-obtained OT plan. This parameterization allows generalization of the mapping outside the support of the input measure. We prove two theoretical stability results of regularized OT which show that our estimations converge to the OT and Monge map between the underlying continuous measures. We showcase our proposed approach on two applications: domain adaptation and generative modeling.

## item_id: m_3927

TITLE: On the Connection between Fisher's Criterion and Shannon's Capacity: Theoretical Concepts and Implementation

ABSTRACT: Fisher's criterion is arguably among the most widely used tools in machine learning for feature selection. The higher the value of Fisher's criterion, the more favorable a feature is. A rather different but nevertheless very important tool is Shannon's channel capacity. With Shannon’s capacity, one can determine the maximum rate at which information can flow across a channel. Fisher's criterion and Shannon’s capacity appear to be unrelated, yet both capture in their unique way the separation between probability distributions. In this study, we investigate whether Fisher's class separation criterion and Shannon’s capacity can be related to each other. We formulate our research problem as a binary classification task and derive analytic expressions to determine if there is a potential link between Fisher's criterion and Shannon's capacity. It turns out that Fisher's class separation criterion and Shannon’s channel capacity are intimately connected through two principal assumptions. Using this result, we develop a  divergence measure for feature selection. Additionally, we show how our results can be used to solve classification problems and conduct a proof-of-concept experiment to demonstrate the viability of our approach.

## item_id: m_3928

TITLE: Sparse Transformer: Concentrated Attention Through Explicit Selection

ABSTRACT: Self-attention-based Transformer has demonstrated the state-of-the-art performances in a number of natural language processing tasks. Self attention is able to model long-term dependencies, but it may suffer from the extraction of irrelevant information in the context. To tackle the problem, we propose a novel model called Sparse Transformer. Sparse Transformer is able to improve the concentration of attention on the global context through an explicit selection of the most relevant segments. Extensive experimental results on a series of natural language processing tasks, including neural machine translation, image captioning, and language modeling, all demonstrate the advantages of Sparse Transformer in model performance. 
  Sparse Transformer reaches the state-of-the-art performances in the IWSLT 2015 English-to-Vietnamese translation and IWSLT 2014 German-to-English translation. In addition, we conduct qualitative analysis to account for Sparse Transformer's superior performance. 

## item_id: m_3929

TITLE: Learning Representations in Model-Free Hierarchical Reinforcement Learning

ABSTRACT: Common approaches to Reinforcement Learning (RL) are seriously challenged by large-scale applications involving huge state spaces and sparse delayed reward feedback. Hierarchical Reinforcement Learning (HRL) methods attempt to address this scalability issue by learning action selection policies at multiple levels of temporal abstraction. Abstraction can be had by identifying a relatively small set of states that are likely to be useful as subgoals, in concert with the learning of corresponding skill policies to achieve those subgoals. Many approaches to subgoal discovery in HRL depend on the analysis of a model of the environment, but the need to learn such a model introduces its own problems of scale. Once subgoals are identified, skills may be learned through intrinsic motivation, introducing an internal reward signal marking subgoal attainment. In this paper, we present a novel model-free method for subgoal discovery using incremental unsupervised learning over a small memory of the most recent experiences of the agent. When combined with an intrinsic motivation learning mechanism, this method learns subgoals and skills together, based on experiences in the environment. Thus, we offer an original approach to HRL that does not require the acquisition of a model of the environment, suitable for large-scale applications. We demonstrate the efficiency of our method on two RL problems with sparse delayed feedback: a variant of the rooms environment and the ATARI 2600 game called Montezuma's Revenge.


## item_id: m_3930

TITLE: BAM: Bayes with Adaptive Memory

ABSTRACT: Online learning via Bayes' theorem allows new data to be continuously integrated into an agent's current beliefs. However, a naive application of Bayesian methods in non-stationary environments leads to slow adaptation and results in state estimates that may converge confidently to the wrong parameter value. A common solution when learning in changing environments is to discard/downweight past data; however, this simple mechanism of "forgetting" fails to account for the fact that many real-world environments involve revisiting similar states. We propose a new framework, Bayes with Adaptive Memory (BAM), that takes advantage of past experience by allowing the agent to choose which past observations to remember and which to forget. We demonstrate that BAM generalizes many popular Bayesian update rules for non-stationary environments. Through a variety of experiments, we demonstrate the ability of BAM to continuously adapt in an ever-changing world.

## item_id: m_3931

TITLE: Why In-Context Learning Models are Good Few-Shot Learners?

ABSTRACT: We explore in-context learning (ICL) models from a learning-to-learn perspective. Unlike studies that identify specific learning algorithms in ICL models, we compare ICL models with typical meta-learners to understand their superior performance. We theoretically prove the expressiveness of ICL models as learning algorithms and examine their learnability and generalizability. 
Our findings show that ICL with transformers 
can effectively construct data-dependent learning algorithms instead of directly follow existing ones 
(including gradient-based, metric-based, and amortization-based meta-learners). 
The construction of such learning algorithm is determined by the pre-training process, as a function fitting the training distribution, which raises generalizability as an important issue.
With above understanding, we propose strategies to transfer techniques for classical deep networks to meta-level to further improve ICL. As examples, we implement meta-level meta-learning for domain adaptability with limited data and meta-level curriculum learning for accelerated convergence during pre-training, demonstrating their empirical effectiveness.

## item_id: m_3932

TITLE: Query-Policy Misalignment in Preference-Based Reinforcement Learning

ABSTRACT: Preference-based reinforcement learning (PbRL) provides a natural way to align RL agents’ behavior with human desired outcomes, but is often restrained by costly human feedback. To improve feedback efficiency, most existing PbRL methods focus on selecting queries to maximally improve the overall quality of the reward model, but counter-intuitively, we find that this may not necessarily lead to improved performance. To unravel this mystery, we identify a long-neglected issue in the query selection schemes of existing PbRL studies: Query-Policy Misalignment. We show that the seemingly informative queries selected to improve the overall quality of reward model actually may not align with RL agents’ interests, thus offering little help on policy learning and eventually resulting in poor feedback efficiency. We show that this issue can be effectively addressed via policy-aligned query and a specially designed hybrid experience replay, which together enforce the bidirectional query-policy alignment. Simple yet elegant, our method can be easily incorporated into existing approaches by changing only a few lines of code. We showcase in comprehensive experiments that our method achieves substantial gains in both human feedback and RL sample efficiency, demonstrating the importance of addressing query-policy misalignment in PbRL tasks.

## item_id: m_3933

TITLE: Balancing Average and Worst-case Accuracy in Multitask Learning

ABSTRACT: When training and evaluating machine learning models on a large number of tasks, it is important to not only look at average task accuracy---which may be biased by easy or redundant tasks---but also worst-case accuracy (i.e. the performance on the task with the lowest accuracy). In this work, we show how to use techniques from the distributionally robust optimization (DRO) literature to improve worst-case performance in multitask learning. We highlight several failure cases of DRO when applied off-the-shelf and present an improved method, Lookahead-DRO (L-DRO), which mitigates these issues. The core idea of L-DRO is to anticipate the interaction between tasks during training in order to choose a dynamic re-weighting of the various task losses, which will (i) lead to minimal worst-case loss and (ii) train on as many tasks as possible. After demonstrating the efficacy of L-DRO on a small controlled synthetic setting, we evaluate it on two realistic benchmarks: a multitask version of the CIFAR-100 image classification dataset and a large-scale multilingual language modeling experiment. Our empirical results show that L-DRO achieves a better trade-off between average and worst-case accuracy with little computational overhead compared to several strong baselines.

## item_id: m_3934

TITLE: Partial Output Norm: Mitigating the Model Output Blow-up Effect of Cross Entropy Loss 

ABSTRACT: Cross entropy loss is a very popular optimization objective and has been successfully applied for diverse classification tasks. The discrepancy between cross entropy objective and real classification target is not fully studied because researchers usually think such discrepancy is a must-pay price to have a differentiable objective which can be optimized through gradient based methods. In this paper, we carefully study such discrepancy and find out such discrepancy leads to the side effect that the model output have certain useless growth tendency when the classification result is correct. We call such side effects as "model output blow-up effect". Such effect distracts CE objective from real effective update, which brings the negative influence on the model training. To mitigate such side effect, we introduce a partial normalization layer for regularizing model output to reduce its useless growth tendency. We further provide the theoretical analysis on our finds and our approaches. The experiment results shows that the proposed partial normalization layer improves the model training, and it could be combined with other method like weight decay to achieve big additional performance gain. 

## item_id: m_3935

TITLE: Don't Throw Away Your Beams: Improving Consistency-based Uncertainties in LLMs via Beam Search

ABSTRACT: Consistency-based methods have emerged as an effective approach to uncertainty quantification (UQ) in large language models. These methods typically rely on several generations obtained via multinomial sampling, measuring their agreement level. However, in short-form QA, multinomial sampling is prone to producing duplicates due to peaked distributions, and its stochasticity introduces considerable variance in uncertainty estimates across runs. We introduce a new family of methods that employ beam search to generate candidates for consistency-based UQ, yielding improved performance and reduced variance compared to multinomial sampling. We also provide a theoretical lower bound on the beam set probability mass under which beam search achieves a smaller error than multinomial sampling. We empirically evaluate our approach on six QA datasets and find that its consistent improvements over multinomial sampling lead to state-of-the-art UQ performance.

## item_id: m_3936

TITLE: When does preconditioning help or hurt generalization?

ABSTRACT: While second order optimizers such as natural gradient descent (NGD) often speed up optimization, their effect on generalization has been called into question. This work presents a more nuanced view on how the \textit{implicit bias} of optimizers affects the comparison of generalization properties. 
We provide an exact asymptotic bias-variance decomposition of the generalization error of preconditioned ridgeless regression in the overparameterized regime, and consider the inverse population Fisher information matrix (used in NGD) as a particular example. We determine the optimal preconditioner $\boldsymbol{P}$ for both the bias and variance, and find that the relative generalization performance of different optimizers depends on label noise and ``shape'' of the signal (true parameters): when the labels are noisy, the model is misspecified, or the signal is misaligned with the features, NGD can achieve lower risk; conversely, GD generalizes better under clean labels, a well-specified model, or aligned signal. 
Based on this analysis, we discuss several approaches to manage the bias-variance tradeoff, and the potential benefit of interpolating between first- and second-order updates. We then extend our analysis to regression in the reproducing kernel Hilbert space and demonstrate that preconditioning can lead to more efficient decrease in the population risk. Lastly, we empirically compare the generalization error of first- and second-order optimizers in neural network experiments, and observe robust trends matching our theoretical analysis. 

## item_id: m_3937

TITLE: Accurate Neural Training with 4-bit Matrix Multiplications at Standard Formats

ABSTRACT: Quantization of the weights and activations is one of the main methods to reduce the computational footprint of Deep Neural Networks (DNNs) training. Current methods enable 4-bit quantization of the forward phase. However, this constitutes only a third of the training process. Reducing the computational footprint of the entire training process requires the quantization of the neural gradients, i.e., the loss gradients with respect to the outputs of intermediate neural layers. 

Previous works separately showed that accurate 4-bit quantization of the neural gradients needs to (1) be unbiased and (2) have a log scale. However, no previous work aimed to combine both ideas, as we do in this work. Specifically, we examine the importance of having unbiased quantization in quantized neural network training, where to maintain it, and how to combine it with logarithmic quantization. Based on this, we suggest a $\textit{logarithmic unbiased quantization}$ (LUQ) method to quantize all both the forward and backward phase to 4-bit, achieving state-of-the-art results in 4-bit training without overhead. For example, in ResNet50 on ImageNet, we achieved a degradation of 1.1 %. We further improve this to degradation of only 0.32 % after three epochs of high precision fine-tunining, combined with a variance reduction method---where both these methods add overhead comparable to previously suggested methods. 
A reference implementation is supplied in the supplementary material.

## item_id: m_3938

TITLE: Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations

ABSTRACT: A major barrier to the practical deployment of large language models (LLMs) is their lack of reliability. Three situations where this is particularly apparent are correctness, hallucinations when given unanswerable questions, and safety where responses are harmful or offensive. In all three cases, models should ideally abstain from responding---much like humans refrain from answering questions when uncertain. Inspired by analogous approaches in classification, this study explores the feasibility and efficacy of LLMs abstaining when uncertain in the domain of question-answering. We investigate two kinds of uncertainties, statistical uncertainty metrics and a distinct verbalized measure, termed as In Dialogue Uncertainty (InDU), measuring hedge words such as `I don't know' in responses. Using these uncertainty measures combined with models with and without reinforcement learning with human feedback (RLHF), we show in all three situations, abstention based on the right kind of uncertainty measure can boost the reliability of LLMs. By abstaining for a few highly uncertain samples we improve correctness by up to 8\%, avoid 50\% of hallucinations by correctly identifying unanswerable questions, and in particular increase safety by 70-99\% with almost no additional computational overhead.

## item_id: m_3939

TITLE: Robust agents learn causal world models

ABSTRACT: It has long been hypothesised that causal reasoning plays a fundamental role in robust and general intelligence. However, it is not known if agents must learn causal models in order to generalise to new domains, or if other inductive biases are sufficient. We answer this question, showing that any agent capable of satisfying a regret bound for a large set of distributional shifts must have learned an approximate causal model of the data generating process, which converges to the true causal model for optimal agents. We discuss the implications of this result for several research areas including transfer learning and causal inference.

## item_id: m_3940

TITLE: Mutual Information Dynamics Learning: A New Paradigm for Unsupervised Reinforcement Learning

ABSTRACT: Unsupervised reinforcement learning (URL) aims to develop general-purpose agents that can adapt to unseen downstream tasks without relying on task-specific supervision. Existing approaches predominantly focus on learning diverse skills by maximizing mutual information, but they are often limited to simple navigation tasks and fail to scale to more complex domains such as robotic manipulation, where prior knowledge is typically required. In this work, we demonstrate that mutual information-based objectives can be leveraged far beyond skill learning. We propose a novel URL framework that trains exploratory skills to collect diverse transition data with distinct dynamics. This diverse dataset enables the training of a mixture of dynamic models, where each model captures the dynamics of a specific region. Collectively, these models provide comprehensive coverage of the dynamics required for a wide range of downstream tasks. Our straightforward and prior-free learning objective outperforms existing state-of-the-art skill discovery approaches in URL. Our results advocate a paradigm shift in URL, from skill learning toward dynamics learning, to acquire fully generalizable knowledge during pretraining.

## item_id: m_3941

TITLE: MILA (MULTILINGUAL INDIC LANGUAGE ARCHIVE): A DATASET FOR EQUITABLE MULTILINGUAL LLMS

ABSTRACT: Large Language Models (LLMs) are structurally biased toward high-resource languages like English due to corpus skew, a problem particularly severe for Indic languages. To address this deficit, we introduce ***MILA***, the largest expert-curated Indic corpus to date, comprising ***7.5 trillion tokens*** across ***16 scheduled Indic languages*** and English. MILA is constructed via a multi-stage data engineering pipeline that integrates large-scale ***web acquisition***, script-sensitive ***OCR*** for under-digitized Indic writing systems, LLM-assisted post-correction for ***Translation*** fidelity, and ***targeted data distillation*** through the ***Indic-Persona Hub***. The pipeline further incorporates ***synthetic augmentation and rewriting***, followed by stringent ***quality, toxicity, language, and deduplication filtering***, and culminates in ***human-in-the-loop linguistic*** and cultural validation with comprehensive ***PII redaction*** and ensuring ***downstream task and benchmark-based decontamination***. This pipeline yields a distributionally stable, contamination-controlled, high-fidelity pretraining substrate. Alongside, we release ***Indic-MMLU***, a translated and verified adaptation of MMLU into 16 Indian languages, offering the first large-scale Indic multilingual benchmark for assessing LLMs and their extent of cross-lingual knowledge transfer. We further propose a ***Parity-based fairness Metric*** capturing cross-lingual performance asymmetries relative to English. Comprehensive experiments including controlled ablations of translation quality, OCR incorporation, synthetic SFT generation, and continual pretraining demonstrates that models trained on MILA achieve substantial gains on Indic-MMLU and materially narrow cross-lingual disparities. Collectively, MILA, Indic-MMLU, and the associated validation protocols establish a scalable foundation for equitable multilingual modeling in the Indic context. All resources are released anonymously for reproducibility.

## item_id: m_3942

TITLE: GREmLN: A Cellular Graph Structure Aware Transcriptomics Foundation Model

ABSTRACT: The ever-increasing availability of large-scale single-cell profiles presents an opportunity to develop foundation models to capture cell properties and behavior. However, standard language models such as transformers benefits from sequentially structured data with well defined absolute or relative positional relationships, while single cell RNA data have orderless gene features. Molecular-interaction graphs, such as gene regulatory networks (GRN) or protein-protein interaction (PPI) networks, offer graph structure-based models that effectively encode both non-local gene token dependencies, as well as potential causal relationships. We introduce GREmLN (\textbf{G}ene \textbf{R}egulatory \textbf{Em}bedding-based \textbf{L}arge \textbf{N}eural model), a foundation model that leverages graph signal processing to embed gene token graph structure directly within its attention mechanism, producing biologically informed single cell specific gene embeddings. Our model faithfully captures transcriptomics landscapes and achieves superior performance relative to state-of-the-art baselines on cell type annotation, graph structure understanding, and fine-tuned reverse perturbation prediction tasks. It offers a unified and interpretable framework for learning high-capacity foundational representations that capture complex, long-range regulatory dependencies from high-dimensional single-cell transcriptomic data. Moreover, the incorporation of graph-structured inductive biases enables more parameter-efficient architectures and accelerates training convergence.

## item_id: m_3943

TITLE: Scaling Symbolic Methods using Gradients for Neural Model Explanation

ABSTRACT: Symbolic techniques based on Satisfiability Modulo Theory (SMT) solvers have been proposed for analyzing and verifying neural network properties, but their usage has been fairly limited owing to their poor scalability with larger networks. In this work, we propose a technique for combining gradient-based methods with symbolic techniques to scale such analyses and demonstrate its application for model explanation. In particular, we apply this technique to identify minimal regions in an input that are most relevant for a neural network's prediction. Our approach uses gradient information (based on Integrated Gradients) to focus on a subset of neurons in the first layer, which allows our technique to scale to large networks. The corresponding SMT constraints encode the minimal input mask discovery problem such that after masking the input, the activations of the selected neurons are still above a threshold. After solving for the minimal masks, our approach scores the mask regions to generate a relative ordering of the features within the mask. This produces a saliency map which explains" where a model is looking" when making a prediction. We evaluate our technique on three datasets-MNIST, ImageNet, and Beer Reviews, and demonstrate both quantitatively and qualitatively that the regions generated by our approach are sparser and achieve higher saliency scores compared to the gradient-based methods alone. Code and examples are at - https://github.com/google-research/google-research/tree/master/smug_saliency

## item_id: m_3944

TITLE: Automatic Measurement on Etched Structure in Semiconductor Using Deep Learning Approach

ABSTRACT: The fabrication of semiconductor involves etching process to remove selected areas from wafers. However, the measurement of etched structure in micro-graph heavily relies on time-consuming manual routines. Traditional image processing usually demands on large number of annotated data and the performance is still poor. We treat this challenge as segmentation problem and use deep learning approach to detect masks of objects in etched structure of wafer. Then, we use simple image processing to carry out automatic measurement on the objects. We attempt Generative Adversarial Network (GAN) to generate more data to overcome the problem of very limited dataset. We download 10 SEM (Scanning Electron Microscope) images of 4 types from Internet, based on which we carry out our experiments. Our deep learning based method demonstrates superiority over image processing approach with  mean accuracy reaching over 96% for the measurements, compared with the ground truth. To the best of our knowledge, it is the first time that deep learning has been applied in semiconductor industry for automatic measurement.

## item_id: m_3945

TITLE: The Scattering Compositional Learner: Discovering Objects, Attributes, Relationships in Analogical Reasoning

ABSTRACT: In this work, we focus on an analogical reasoning task that contains rich compositional structures, Raven's Progressive Matrices (RPM). To discover compositional structures of the data, we propose the Scattering Compositional Learner (SCL), an architecture that composes neural networks in a sequence. Our SCL achieves state-of-the-art performance on two RPM datasets, with a 48.7% relative improvement on Balanced-RAVEN and 26.4% on PGM over the previous state-of-the-art. We additionally show that our model discovers compositional representations of objects' attributes (e.g., shape color, size), and their relationships (e.g., progression, union). We also find that the compositional representation makes the SCL significantly more robust to test-time domain shifts and greatly improves zero-shot generalization to previously unseen analogies.

## item_id: m_3946

TITLE: Towards Scalable and Consistent 3D Editing

ABSTRACT: 3D editing—the task of locally modifying the geometry or appearance of a 3D asset—has wide applications in immersive content creation, digital entertainment, and AR/VR. However, unlike 2D editing, it remains challenging due to the need for cross-view consistency, structural fidelity, and fine-grained controllability. Existing approaches are often slow, prone to geometric distortions, or dependent on manual and accurate 3D masks that are error-prone and impractical.  To address these challenges, we advance both the data and model fronts. On the data side, we introduce 3DEditVerse, the largest paired 3D editing benchmark to date, comprising 116,309 high-quality training pairs and 1,500 curated test pairs. Built through complementary pipelines of pose-driven geometric edits and foundation model-guided appearance edits, 3DEditVerse ensures edit locality, multi-view consistency, and semantic alignment.  On the model side, we propose 3DEditFormer, a 3D-structure-preserving conditional transformer. By enhancing image-to-3D generation with dual-guidance attention and time-adaptive gating, 3DEditFormer disentangles editable regions from preserved structure, enabling precise and consistent edits without requiring auxiliary 3D masks.  Extensive experiments demonstrate that our framework outperforms state-of-the-art baselines both quantitatively and qualitatively, establishing a new standard for practical and scalable 3D editing. Dataset and code will be released. Project: https://anonymousresearch37.github.io/3DEditFormer/

## item_id: m_3947

TITLE: Modularized Morphing of Neural Networks

ABSTRACT: In this work we study the problem of network morphism, an effective learning scheme to morph a well-trained neural network to a new one with the network function completely preserved. Different from existing work where basic morphing types on the layer level were addressed, we target at the central problem of network morphism at a higher level, i.e., how a convolutional layer can be morphed into an arbitrary module of a neural network. To simplify the representation of a network, we abstract a module as a graph with blobs as vertices and convolutional layers as edges, based on which the morphing process is able to be formulated as a graph transformation problem. Two atomic morphing operations are introduced to compose the graphs, based on which modules are classified into two families, i.e., simple morphable modules and complex modules. We present practical morphing solutions for both of these two families, and prove that any reasonable module can be morphed from a single convolutional layer. Extensive experiments have been conducted based on the state-of-the-art ResNet on benchmark datasets, and the effectiveness of the proposed solution has been verified.

## item_id: m_3948

TITLE: Learnable Topological Features For Phylogenetic Inference via Graph Neural Networks

ABSTRACT: Structural information of phylogenetic tree topologies plays an important role in phylogenetic inference. However, finding appropriate topological structures for specific phylogenetic inference tasks often requires significant design effort and domain expertise. In this paper, we propose a novel structural representation method for phylogenetic inference based on learnable topological features. By combining the raw node features that minimize the Dirichlet energy with modern graph representation learning techniques, our learnable topological features can provide efficient structural information of phylogenetic trees that automatically adapts to different downstream tasks without requiring domain expertise. We demonstrate the effectiveness and efficiency of our method on a simulated data tree probability estimation task and a benchmark of challenging real data variational Bayesian phylogenetic inference problems.

## item_id: m_3949

TITLE: Variable Forward Regularization to Replace Ridge in Online Linear Regression

ABSTRACT: Forward regularization (-F) with unsupervised knowledge was proposed to replace canonical Ridge regularization (-R) in online linear learners, which achieves lower relative regret bounds. However, we observe that -F cannot perform as expected in practice, even possibly losing to -R for online learning tasks. We identify two main causes for this: (1) inappropriate intervention penalty; (2) potential non-i.i.d nature in online learning, both of which result in unstable posterior distribution and optima offset of the learner. To improve these, we propose Variable Forward regularization (-$k$F), a more general style with -F intensity modulated by a variable $k$. We further derive -$k$F algorithm to online learning tasks, which shows holistic recursive closed-form updates and superior performance compared to both -R and -F. Moreover, we theoretically establish the relative regrets of -$k$F in online learning, showing that it has a tighter upper bound than -F in adversarial settings. We also introduce an adaptive -$k$F, termed -$k$F-Bayes, to curb unstable penalties caused by non-i.i.d and mitigate intractable tuning of hard $k$ based on Bayesian learning for online learning. In experiments, we adapted -$k$F and -$k$F-Bayes into class incremental scenario, where it realized less forgetting and non-replay. Results distinctly demonstrate the efficacy of using -$k$F and -$k$F-Bayes.

## item_id: m_3950

TITLE: Leveraging Class Hierarchies with Metric-Guided Prototype Learning

ABSTRACT: In many classification tasks, the set of classes can be organized according to a meaningful hierarchy. This structure can be used to assess the severity of confusing each pair of classes, and summarized  under the form of a cost matrix which also defines a finite metric. We propose to integrate this metric in the supervision of a prototypical network in order to model the hierarchical class structure. Our method relies on jointly learning a feature-extracting network and a set of class representations, or prototypes, which incorporate the error metric into their relative arrangement in the embedding space. We show that this simultaneous training allows for consistent improvement of the severity of the network's errors with regard to the class hierarchy when compared to traditional methods and other prototype-based strategies. Furthermore, when the induced metric contains insight on the data structure, our approach improves the overall precision as well. Experiments on four different public datasets—from agricultural time series classification to depth image semantic segmentation—validate our approach.

## item_id: m_3951

TITLE: CROP: Certifying Robust Policies for Reinforcement Learning through Functional Smoothing

ABSTRACT: As reinforcement learning (RL) has achieved great success and been even adopted in safety-critical domains such as autonomous vehicles, a range of empirical studies have been conducted to improve its robustness against adversarial attacks. However, how to certify its robustness with theoretical guarantees still remains challenging. In this paper, we present the ﬁrst uniﬁed framework CROP (Certifying Robust Policies for RL) to provide robustness certiﬁcation on both action and reward levels. In particular, we propose two robustness certiﬁcation criteria: robustness of per-state actions and lower bound of cumulative rewards. We then develop a local smoothing algorithm for policies derived from Q-functions to guarantee the robustness of actions taken along the trajectory; we also develop a global smoothing algorithm for certifying the lower bound of a ﬁnite-horizon cumulative reward, as well as a novel local smoothing algorithm to perform adaptive search in order to obtain tighter reward certiﬁcation. Empirically, we apply CROP to evaluate several existing empirically robust RL algorithms, including adversarial training and different robust regularization, in four environments (two representative Atari games, Highway, and CartPole). Furthermore, by evaluating these algorithms against adversarial attacks, we demonstrate that our certiﬁcations are often tight. All experiment results are available at website https://crop-leaderboard.github.io.

## item_id: m_3952

TITLE: Hierarchical Graph Latent Diffusion Model for Molecule Generation

ABSTRACT: Recently, generative models based on the diffusion process have emerged as a promising direction for automating the design of molecules. However, directly adding continuous Gaussian noise to discrete graphs leads to the problem of the final noisy data not conforming to the standard Gaussian distribution. Current graph diffusion models either corrupt discrete data through a transition matrix or relax the discrete data to continuous space for the diffusion process. These approaches not only require significant computation resources due to the inclusion of the bond type matrix but also cannot easily perform scalable conditional generation, such as adding cross-attention layers, due to the lack of embedding representations. In this paper, we first introduce the Graph Latent Diffusion Model (GLDM), a novel variant of latent diffusion models that overcomes the mismatch problem of continuous diffusion space and discrete data space. Meanwhile, the latent diffusion framework avoids the issues of computational resource consumption and lack of embeddings for conditional generation faced by current graph diffusion models. However, it only utilizes graph-level embeddings for molecule generation, losing node-level and structural information. Therefore, we further ex- tend the GLDM to the Hierarchical Graph Latent Diffusion Model (HGLDM). By including node embeddings and subgraph embeddings that contain structural in- formation, our model significantly reduces computation time compared to the cur- rent graph diffusion models. We evaluate our model on three benchmarks through unconditional generation and conditional generation tasks, which demonstrate its superior performance.

## item_id: m_3953

TITLE: Concept-level Debugging of Part-Prototype Networks

ABSTRACT: Part-prototype Networks (ProtoPNets) are concept-based classifiers designed to achieve the same performance as black-box models without compromising transparency. ProtoPNets compute predictions based on similarity to class-specific part-prototypes learned to recognize parts of training examples, making it easy to faithfully determine what examples are responsible for any target prediction and why. However, like other models, they are prone to picking up confounders and shortcuts from the data, thus suffering from compromised prediction accuracy and limited generalization. We propose ProtoPDebug, an effective concept-level debugger for ProtoPNets in which a human supervisor, guided by the model’s explanations, supplies feedback in the form of what part-prototypes must be forgotten or kept, and the model is fine-tuned to align with this supervision. Our experimental evaluation shows that ProtoPDebug outperforms state-of-the-art debuggers for a fraction of the annotation cost. An online experiment with laypeople confirms the simplicity of the feedback requested to the users and the effectiveness of the collected feedback for learning confounder-free part-prototypes. ProtoPDebug is a promising tool for trustworthy interactive learning in critical applications, as suggested by a preliminary evaluation on a medical decision making task.

## item_id: m_3954

TITLE: Large Scale Multi-Domain Multi-Task Learning with MultiModel

ABSTRACT: Deep learning yields great results across many fields,
from speech recognition, image classification, to translation.
But for each problem, getting a deep model to work well involves
research into the architecture and a long period of tuning.

We present a single model that yields good results on a number
of problems spanning multiple domains. In particular, this single model
is trained concurrently on ImageNet, multiple translation tasks,
image captioning (COCO dataset), a speech recognition corpus,
and an English parsing task. 

Our model architecture incorporates building blocks from multiple
domains. It contains convolutional layers, an attention mechanism,
and sparsely-gated layers.

Each of these computational blocks is crucial for a subset of
the tasks we train on. Interestingly, even if a block is not
crucial for a task, we observe that adding it never hurts performance
and in most cases improves it on all tasks.

We also show that tasks with less data benefit largely from joint
training with other tasks, while performance on large tasks degrades
only slightly if at all.

## item_id: m_3955

TITLE: MoCa: Modeling Object Consistency for 3D Camera Control in Video Generation

ABSTRACT: Camera control is important in text-to-video generation for achieving realistic scene navigation and view synthesis. 
This control is defined by parameters that describe movement through 3D space, thereby introducing 3D consistency into the generation process.
A core challenge for existing methods is achieving 3D consistency within the 2D pixel domain.  Strategies that directly integrate camera conditions into text-to-video models often produce artifacts, while those relying on explicit 3D supervision face challenges with generalization. 
Both limitations originate from the gap between the 2D pixel space and the underlying 3D world.
The key insight is that the projection of a smooth 3D camera movement produces consistency in object view, appearance, and motion across 2D frames. Inspired by this insight, we propose MoCa, a dual-branch framework that bridges this gap by modeling object consistency to implicitly learn 3D relationships between the camera and the scene.
To ensure view consistency, we design a Spatial-Temporal Camera Encoder with Plücker embedding, which encodes camera trajectories into a geometrically grounded latent representation. For appearance consistency, we introduce a semantic guidance strategy that leverages persistent vision-language features to maintain object identity and texture across frames. To address motion consistency, we propose an object-aware motion disentanglement mechanism that separates object dynamics from global camera movement, ensuring precise camera control and natural object motion.
Experiments show that MoCa achieves accurate camera control while preserving video quality, offering a practical and effective solution for camera-controllable video generation.

## item_id: m_3956

TITLE: PoGDiff: Product-of-Gaussians Diffusion Models for Imbalanced Text-to-Image Generation

ABSTRACT: Diffusion models have made significant advancements in recent years. However, their performance often deteriorates when trained or fine-tuned on imbalanced datasets. This degradation is largely due to the disproportionate representation of majority and minority data in image-text pairs. In this paper, we propose a general fine-tuning approach, dubbed PoGDiff, to address this challenge. Rather than directly minimizing the KL divergence between the predicted and ground-truth distributions, PoGDiff replaces the ground-truth distribution with a Product of Gaussians (PoG), which is constructed by combining the original ground-truth targets with the predicted distribution conditioned on a neighboring text embedding. Experiments on real-world datasets demonstrate that our method effectively addresses the imbalance problem in diffusion models, improving both generation accuracy and quality.

## item_id: m_3957

TITLE: Capsule Graph Neural Network

ABSTRACT: The high-quality node embeddings learned from the Graph Neural Networks (GNNs) have been applied to a wide range of node-based applications and some of them have achieved state-of-the-art (SOTA) performance. However, when applying node embeddings learned from GNNs to generate graph embeddings, the scalar node representation may not suffice to preserve the node/graph properties efficiently, resulting in sub-optimal graph embeddings.

Inspired by the Capsule Neural Network (CapsNet), we propose the Capsule Graph Neural Network (CapsGNN), which adopts the concept of capsules to address the weakness in existing GNN-based graph embeddings algorithms. By extracting node features in the form of capsules, routing mechanism can be utilized to capture important information at the graph level. As a result, our model generates multiple embeddings for each graph to capture graph properties from different aspects. The attention module incorporated in CapsGNN is used to tackle graphs with various sizes which also enables the model to focus on critical parts of the graphs.

Our extensive evaluations with 10 graph-structured datasets demonstrate that CapsGNN has a powerful mechanism that operates to capture macroscopic properties of the whole graph by data-driven. It outperforms other SOTA techniques on several graph classification tasks, by virtue of the new instrument.

## item_id: m_3958

TITLE: Top-Down Neural Model For Formulae

ABSTRACT: We present a simple neural model that given a formula and a property tries to answer the question whether the formula has the given property, for example whether a propositional formula is always true. The structure of the formula is captured by a feedforward neural network recursively built for the given formula in a top-down manner. The results of this network are then processed by two recurrent neural networks. One of the interesting aspects of our model is how propositional atoms are treated. For example, the model is insensitive to their names, it only matters whether they are the same or distinct.

## item_id: m_3959

TITLE: Generalization and Regularization in DQN

ABSTRACT: Deep reinforcement learning (RL) algorithms have shown an impressive ability to learn complex control policies in high-dimensional environments. However, despite the ever-increasing performance on popular benchmarks like the Arcade Learning Environment (ALE), policies learned by deep RL algorithms can struggle to generalize when evaluated in remarkably similar environments. These results are unexpected given the fact that, in supervised learning, deep neural networks often learn robust features that generalize across tasks. In this paper, we study the generalization capabilities of DQN in order to aid in understanding this mismatch between generalization in deep RL and supervised learning methods. We provide evidence suggesting that DQN overspecializes to the domain it is trained on. We then comprehensively evaluate the impact of traditional methods of regularization from supervised learning, $\ell_2$ and dropout, and of reusing learned representations to improve the generalization capabilities of DQN. We perform this study using different game modes of Atari 2600 games, a recently introduced modification for the ALE which supports slight variations of the Atari 2600 games used for benchmarking in the field. Despite regularization being largely underutilized in deep RL, we show that it can, in fact, help DQN learn more general features. These features can then be reused and fine-tuned on similar tasks, considerably improving the sample efficiency of DQN.

## item_id: m_3960

TITLE: Logically-Constrained Neural Fitted Q-iteration

ABSTRACT: This paper proposes a method for efficient training of Q-function for continuous-state Markov Decision Processes (MDP), such that the traces of the resulting policies satisfy a Linear Temporal Logic (LTL) property. LTL, a modal logic, can express a wide range of time-dependent logical properties including safety and liveness. We convert the LTL property into a limit deterministic Buchi automaton with which a synchronized product MDP is constructed. The control policy is then synthesised by a reinforcement learning algorithm assuming that no prior knowledge is available from the MDP. The proposed method is evaluated in a numerical study to test the quality of the generated control policy and is compared against conventional methods for policy synthesis such as MDP abstraction (Voronoi quantizer) and approximate dynamic programming (fitted value iteration). 

## item_id: m_3961

TITLE: Characterizing Structural Regularities of Labeled Data in Overparameterized Models

ABSTRACT: Humans are accustomed to environments that contain both regularities and exceptions. For example, at most gas stations, one pays prior to pumping, but the occasional rural station does not accept payment in advance.
Likewise, deep neural networks can generalize across instances that share common patterns or structures yet have the capacity to memorize rare or irregular forms. We analyze how individual instances are treated by a model via  a consistency score. The score characterizes the expected accuracy for a held-out instance given training sets of varying size sampled from the data distribution. We obtain empirical estimates of this score for individual instances in multiple data-sets, and we show that the score identifies out-of-distribution and mislabeled examples at one end of the continuum and strongly regular examples at the other end. We identify computationally inexpensive proxies to the consistency score using statistics collected during training. We apply the score toward understanding the dynamics of representation learning and to filter outliers during training, and we discuss other potential applications including curriculum learning and active data collection.

## item_id: m_3962

TITLE: Principled Federated Domain Adaptation: Gradient Projection and Auto-Weighting

ABSTRACT: Federated Domain Adaptation (FDA) describes the federated learning (FL) setting where source clients and a server work collaboratively to improve the performance of a target client where limited data is available. The domain shift between the source and target domains, coupled with limited data of the target client, makes FDA a challenging problem, e.g., common techniques such as federated averaging and fine-tuning fail due to domain shift and data scarcity. 
To theoretically understand the problem, we introduce new metrics that characterize the FDA setting and a theoretical framework with novel theorems for analyzing the performance of server aggregation rules. Further, we propose a novel lightweight aggregation rule, Federated Gradient Projection ($\texttt{FedGP}$), which significantly improves the target performance with domain shift and data scarcity. Moreover, our theory suggests an $\textit{auto-weighting scheme}$ that finds the optimal combinations of the source and target gradients. This scheme improves both $\texttt{FedGP}$ and a simpler heuristic aggregation rule. Extensive experiments verify the theoretical insights and illustrate the effectiveness of the proposed methods in practice.

## item_id: m_3963

TITLE: Adversarial Training Methods for Semi-Supervised Text Classification

ABSTRACT: Adversarial training provides a means of regularizing supervised learning algorithms while virtual adversarial training is able to extend supervised learning algorithms to the semi-supervised setting.
However, both methods require making small perturbations to numerous entries of the input vector, which is inappropriate for sparse high-dimensional inputs such as one-hot word representations.
We extend adversarial and virtual adversarial training to the text domain by applying perturbations to the word embeddings in a recurrent neural network rather than to the original input itself.
The proposed method achieves state of the art results on multiple benchmark semi-supervised and purely supervised tasks.
We provide visualizations and analysis showing that the learned word embeddings have improved in quality and that while training, the model is less prone to overfitting.


## item_id: m_3964

TITLE: Generative Models and Model Criticism via Optimized Maximum Mean Discrepancy

ABSTRACT: We propose a method to optimize the representation and distinguishability of samples from two probability distributions, by maximizing the estimated power of a statistical test based on the maximum mean discrepancy (MMD). This optimized MMD is applied to the setting of unsupervised learning by generative adversarial networks (GAN), in which a model attempts to generate realistic samples, and a discriminator attempts to tell these apart from data samples. In this context, the MMD may be used in two roles: first, as a discriminator, either directly on the samples, or on features of the samples. Second, the MMD can be used to evaluate the performance of a generative model, by testing the model’s samples against a reference data set. In the latter role, the optimized MMD is particularly helpful, as it gives an interpretable indication of how the model and data distributions differ, even in cases where individual model samples are not easily distinguished either by eye or by classifier.

## item_id: m_3965

TITLE: Online Black-Box Prompt Optimization with Regret Guarantees under Noisy Feedback

ABSTRACT: Generative AI excels in various tasks through advanced language modeling techniques, with its performance heavily influenced by input prompts. This has driven significant research into prompt optimization, particularly in commercial generative AI platforms, where prompt optimization is treated as a black-box optimization problem. Most existing research on black-box prompt optimization primarily focuses on offline learning and overlooks the randomness in outputs. However, in real-world applications, black-box prompt optimization typically operates in an online learning setting, which remains largely unexplored, especially given the noisy outputs. To address these challenges, we propose an \textbf{A}daptive \textbf{O}nline \textbf{Z}eroth-order \textbf{P}rompt \textbf{T}uning (AOZPT) approach which integrates zeroth-order optimization with online learning in the non-convex setting. Specifically, we developed an uncertainty-scale-adjustment mechanism to mitigate the noise inherent in generative AI and the high variance associated with zeroth-order estimates. We conducted a comprehensive regret analysis of the AOZPT approach, and the results indicate that sublinear regret convergence is achievable. Extensive generative experiments demonstrate that AOZPT outperforms existing black-box prompt tuning methods, particularly in terms of stability in online scenarios.

## item_id: m_3966

TITLE: FedEve: On Bridging the Client Drift and Period Drift for Cross-device Federated Learning

ABSTRACT: Federated learning (FL) is a machine learning paradigm that allows multiple clients to collaboratively train a shared model without exposing their private data. Data heterogeneity is a fundamental challenge in FL, which can result in poor convergence and performance degradation. \textit{Client drift} has been recognized as one of the factors contributing to this issue resulting from the multiple local updates in \fedavg. However, in cross-device FL, a different form of drift arises due to the partial client participation, but it has not been studied well. This drift, we referred as \textit{period drift},  occurs as participating clients at each communication round may exhibit distinct data distribution that deviates from that of all clients. It could be more harmful than client drift since the optimization objective shifts with every round. 
In this paper, we investigate the interaction between period drift and client drift, finding that period drift can have a particularly detrimental effect on cross-device FL as the degree of data heterogeneity increases. To tackle these issues, we propose a predict-observe framework and present an instantiated method, \fedeve, where these two types of drift can counteract each other to mitigate their overall impact. We provide theoretical evidence that our approach can reduce the variance of model updates. Extensive experiments demonstrate that our method outperforms alternatives on non-iid data in cross-device settings.

## item_id: m_3967

TITLE: Learning Protein Structure with a Differentiable Simulator

ABSTRACT: The Boltzmann distribution is a natural model for many systems, from brains to materials and biomolecules, but is often of limited utility for fitting data because Monte Carlo algorithms are unable to simulate it in available time. This gap between the expressive capabilities and sampling practicalities of energy-based models is exemplified by the protein folding problem, since energy landscapes underlie contemporary knowledge of protein biophysics but computer simulations are challenged to fold all but the smallest proteins from first principles. In this work we aim to bridge the gap between the expressive capacity of energy functions and the practical capabilities of their simulators by using an unrolled Monte Carlo simulation as a model for data. We compose a neural energy function with a novel and efficient simulator based on Langevin dynamics to build an end-to-end-differentiable model of atomic protein structure given amino acid sequence information. We introduce techniques for stabilizing backpropagation under long roll-outs and demonstrate the model's capacity to make multimodal predictions and to, in some cases, generalize to unobserved protein fold types when trained on a large corpus of protein structures.

## item_id: m_3968

TITLE: Off-Dynamics Reinforcement Learning: Training for Transfer with Domain Classifiers

ABSTRACT: We propose a simple, practical, and intuitive approach for domain adaptation in reinforcement learning. Our approach stems from the idea that the agent's experience in the source domain should look similar to its experience in the target domain. Building off of a probabilistic view of RL, we achieve this goal by compensating for the difference in dynamics by modifying the reward function. This modified reward function is simple to estimate by learning auxiliary classifiers that distinguish source-domain transitions from target-domain transitions. Intuitively, the agent is penalized for transitions that would indicate that the agent is interacting with the source domain, rather than the target domain. Formally, we prove that applying our method in the source domain is guaranteed to obtain a near-optimal policy for the target domain, provided that the source and target domains satisfy a lightweight assumption. Our approach is applicable to domains with continuous states and actions and does not require learning an explicit model of the dynamics. On discrete and continuous control tasks, we illustrate the mechanics of our approach and demonstrate its scalability to high-dimensional~tasks.

## item_id: m_3969

TITLE: TEN-DM: Topology-Enhanced Diffusion Model for Spatio-Temporal Event Prediction

ABSTRACT: Spatio-temporal point process (STPP) data appear in many domains. A natural way to model them is to describe how the instantaneous event rate varies over space and time given the observed history which enables interpretation, interaction detection, and forecasting. Traditional parametric kernel-based models, while historically dominant, struggle to capture complex nonlinear patterns. In contrast, deep learning methods leverage the representational power of neural networks to aggregate historical events and integrate spatio-temporal point processes. However, existing deep learning methods often process space and time independently, overlooking the spatio-temporal dependencies. To address this limitation, we propose a novel method called Topology-ENhanced Diffusion Model (TEN-DM), including two key components namely spatio-temporal graph construction and multimodal topological feature representation learning. Further, we use temporal query technique to effectively capture periodic temporal patterns for learning effective temporal representations. Extensive experiments show the effectiveness of TEN-DM on multiple STPP datasets compared to state-of-the-art methods.

## item_id: m_3970

TITLE: Learning to Make Analogies by Contrasting Abstract Relational Structure

ABSTRACT: Analogical reasoning has been a principal focus of various waves of AI research. Analogy is particularly challenging for machines because it requires relational structures to be represented such that they can be flexibly applied across diverse domains of experience. Here, we study how analogical reasoning can be induced in neural networks that learn to perceive and reason about raw visual data. We find that the critical factor for inducing such a capacity is not an elaborate architecture, but rather, careful attention to the choice of data and the manner in which it is presented to the model. The most robust capacity for analogical reasoning is induced when networks learn analogies by contrasting abstract relational structures in their input domains, a training method that uses only the input data to force models to learn about important abstract features. Using this technique we demonstrate capacities for complex, visual and symbolic analogy making and generalisation in even the simplest neural network architectures.

## item_id: m_3971

TITLE: Learning Less-Overlapping Representations

ABSTRACT: In representation learning (RL), how to make the learned representations easy to interpret and less overfitted to training data are two important but challenging issues. To address these problems, we study a new type of regularization approach that encourages the supports of weight vectors in RL models to have small overlap, by simultaneously promoting near-orthogonality among vectors and sparsity of each vector. We apply the proposed regularizer to two models: neural networks (NNs) and sparse coding (SC), and develop an efficient ADMM-based algorithm for regularized SC. Experiments on various datasets demonstrate that weight vectors learned under our regularizer are more interpretable and have better generalization performance.

## item_id: m_3972

TITLE: Distributionally Robust Policy Learning under Concept Drifts

ABSTRACT: Distributionally robust policy learning aims to find a policy that performs well 
    under the worst-case distributional shift, and yet most existing methods for 
    robust policy learning consider the worst-case {\em joint} distribution of 
    the covariate and the outcome. The joint-modeling strategy can be unnecessarily conservative
    when we have more information on the source of distributional shifts. This paper studies
    a more nuanced problem --- robust policy learning under the \emph{concept drift}, 
    when only the conditional relationship between the outcome and the covariate changes. 
    To this end, we first provide a doubly-robust estimator for evaluating
    the worst-case average reward of a given policy under a set of perturbed conditional distributions. 
    We show that the policy value estimator enjoys asymptotic normality even if the nuisance parameters 
    are estimated with a slower-than-root-$n$ rate.
    We then propose a learning algorithm that outputs the policy maximizing the 
    estimated policy value within a given policy class $\Pi$, and show
    that the sub-optimality gap of the proposed algorithm is of the order 
    $\kappa(\Pi)n^{-1/2}$, with $\kappa(\Pi)$ is the entropy integral of $\Pi$ under the Hamming distance
    and $n$ is the sample size. A matching lower bound is provided to show the optimality of the rate.
    The proposed methods are implemented and evaluated in numerical studies, 
    demonstrating substantial improvement compared with existing benchmarks.

## item_id: m_3973

TITLE: Grammar-Induced Geometry for Data-Efficient Molecular Property Prediction

ABSTRACT: The prediction of molecular properties is a crucial task in the field of material and drug discovery. The potential benefits of using deep learning techniques are reflected in the wealth of recent literature. Still, these techniques are faced with a common challenge in practice: Labeled data are limited by the cost of manual extraction from literature and laborious experimentation. In this work, we propose a data-efficient property predictor by utilizing a learnable hierarchical molecular grammar that can generate molecules from grammar production rules. Such a grammar induces an explicit geometry of the space of molecular graphs, which provides an informative prior on molecular structural similarity. The property prediction is performed using graph neural diffusion over the grammar-induced geometry. On both small and large datasets, our evaluation shows that this approach outperforms a wide spectrum of baselines, including supervised and pre-trained graph neural networks. We include a detailed ablation study and further analysis of our solution, showing its effectiveness in cases with extremely limited data (only ${\sim}100$ samples), and its extension to application in molecular generation.

## item_id: m_3974

TITLE: PhysERL-Inv: A Physics-Encoded Inverse Modeling Approach for Arctic Snow Depth Prediction

ABSTRACT: The accurate estimation of Arctic snow depth ($h_s$) remains a critical time-varying inverse problem due to the extreme scarcity and noise inherent in associated sea ice parameters. Existing process-based and data-driven models are either highly sensitive to sparse data or lack the physical interpretability required for climate-critical applications. To address this gap, we introduce PhysE-Inv, a novel framework that integrates a sophisticated sequential architecture, an LSTM Encoder-Decoder with Multi-head Attention and physics-guided contrastive learning, with physics-guided inference.Our core innovation lies in a surjective, physics-constrained inversion methodology. This methodology first leverages the hydrostatic balance forward model as a target-formulation proxy, enabling effective learning in the absence of direct $h_s$ ground truth; second, it uses reconstruction physics regularization over a latent space to dynamically discover hidden physical parameters from noisy, incomplete time-series input. Evaluated against state-of-the-art baselines, PhysE-Inv significantly improves prediction performance, reducing error by 20\% while demonstrating superior physical consistency and resilience to data sparsity compared to empirical methods. This approach pioneers a path for noise-tolerant, interpretable inverse modeling, with wide applicability in geospatial and cryospheric domains.

## item_id: m_3975

TITLE: Offline Deep models calibration with bayesian neural networks

ABSTRACT: We apply Bayesian Neural Networks to improve calibration of state-of-the-art deep
neural networks. We show that, even with the most basic amortized approximate
posterior distribution, and fast fully connected neural network for the likelihood,
the Bayesian framework clearly outperforms other simple maximum likelihood
based solutions that have recently shown very good performance, as temperature
scaling. As an example, we reduce the Expected Calibration
Error (ECE) from 0.52 to 0.24 on CIFAR-10 and from 4.28 to 2.456 on CIFAR-100
on two Wide ResNet with 96.13% and 80.39% accuracy respectively, which are
among the best results published for this task. We demonstrate our robustness and
performance with experiments on a wide set of state-of-the-art computer vision
models. Moreover, our approach acts off-line, and thus can be applied to any
probabilistic model regardless of the limitations that the model may present during
training. This make it suitable to calibrate systems that make use of pre-trained
deep neural networks that are expensive to train for a specific task, or to directly
train a calibrated deep convolutional model with Monte Carlo Dropout approximations, among others. However,
our method is still complementary with any Bayesian Neural Network for further
improvement.

## item_id: m_3976

TITLE: A Generative Model For Electron Paths

ABSTRACT: Chemical reactions can be described as the stepwise redistribution of electrons in molecules. As such, reactions are often depicted using "arrow-pushing" diagrams which show this movement as a sequence of arrows. We propose an electron path prediction model (ELECTRO) to learn these sequences directly from raw reaction data. Instead of predicting product molecules directly from reactant molecules in one shot, learning a model of electron movement has the benefits of (a) being easy for chemists to interpret, (b) incorporating constraints of chemistry, such as balanced atom counts before and after the reaction, and (c) naturally encoding the sparsity of chemical reactions, which usually involve changes in only a small number of atoms in the reactants. We design a method to extract approximate reaction paths from any dataset of atom-mapped reaction SMILES strings. Our model achieves excellent performance on an important subset of the USPTO reaction dataset, comparing favorably to the strongest baselines. Furthermore, we show that our model recovers a basic knowledge of chemistry without being explicitly trained to do so.

## item_id: m_3977

TITLE: Interpreting Reinforcement Policies through Local Behaviors

ABSTRACT: Many works in explainable AI have focused on explaining black-box classification models. Explaining deep reinforcement learning (RL) policies in a manner that could be understood by domain users has received much less attention. In this paper, we propose a novel perspective to understanding RL policies based on identifying important states from automatically learned meta-states. The key conceptual difference between our approach and many previous ones is that we form meta-states based on locality governed by the expert policy dynamics rather than based on similarity of actions, and that we do not assume any particular knowledge of the underlying topology of the state space. Theoretically, we show that our algorithm to find meta-states converges and the objective that selects important states from each meta-state is submodular leading to efficient high quality greedy selection. Experiments on three domains (four rooms, door-key and minipacman) and a carefully conducted user study illustrate that our perspective leads to better understanding of the policy. We conjecture that this is a result of our meta-states being more intuitive in that the corresponding important states are strong indicators of tractable intermediate goals that are easier for humans to interpret and follow.

## item_id: m_3978

TITLE: Simplicity Bias of SGD via Sharpness Minimization

ABSTRACT: The remarkable generalization ability of neural networks is usually attributed to the implicit bias of SGD, which often yields models with lower complexity using simpler (e.g. linear) and low-rank features (Huh et al., 2021). Recent works have provided empirical and theoretical evidence for the bias of particular variants of SGD (such as label noise SGD) towards flatter regions of the loss landscape. 
Despite the folklore intuition that flat solutions are 'simple', the connection with the simplicity of the final trained model (e.g. low rank) is not well understood. 
In this work, we take a step towards bridging this gap by studying the simplicity structure that arises from minimizers of the sharpness for a class of two-layer neural networks.
We show that, for any high dimensional training data and certain activations, with small enough step size, label noise SGD always converges to a network that replicates a single linear feature across all neurons; thereby implying a simple rank one feature matrix. To obtain this result, our main technical contribution is to show that label noise SGD always minimizes the sharpness on the manifold of models with zero loss for two-layer networks. 
Along the way, we discover a novel property --- a local geodesic convexity --- of the trace of Hessian of the loss at approximate stationary points on the manifold of zero loss, which links sharpness to the geometry of the manifold. This tool may be of independent interest.

## item_id: m_3979

TITLE: Efficient Facial Landmark Detection via Prior Knowledge-Guided Agents

ABSTRACT: We present a highly efficient, agent-based framework for facial landmark detection that prioritizes model compactness and computational efficiency over maximum accuracy. Unlike conventional approaches that rely on large, fully supervised models, our method assigns each agent to a specific landmark, enabling it to infer its position solely from local observations and prior knowledge without explicit location awareness or inter-agent communication. Prior knowledge is modeled in two embedding spaces—feature and coordinate—using class-conditional Gaussian distributions. Agents navigate by minimizing deviations from these priors via a lightweight policy network. To enhance representation learning, we introduce a proximity-weighted contrastive learning strategy that incorporates spatial proximity into the training objective. A multi-stage detection strategy further reduces redundant computation by detecting sub-landmarks relative to core landmarks. While our method produces slightly higher normalized mean error than state-of-the-art (SoTA) methods, it achieves over $16\times$ and $41\times$ improvements in space and time complexities, respectively, compared to the SoTA lightweight model, running at $4.19$ and $1.29$ frames per second on an i5 CPU (2.5 GHz) for the COFW and 300W datasets, respectively.

## item_id: m_3980

TITLE: Rememory-Based SimSiam for Unsupervised Continual Learning

ABSTRACT: Unsupervised continual learning (UCL) has started to draw attention from the continual learning community, motivated by the practical need of representation learning with unlabeled data on sequential tasks. However, most of recent UCL methods focus on mitigating the catastrophic forgetting problem with a replay buffer to store previous data (i.e., rehearsal-based strategy), which needs much extra storage and thus limits their practical applications. To overcome this drawback, based on contrastive learning via SimSiam, we propose a novel rememory-based SimSiam (RM-SimSiam) method to reduce the dependency on replay buffer under the UCL setting. The core idea of our RM-SimSiam is to store and remember the old knowledge with a data-free historical module instead of replay buffer. Specifically, this historical module is designed to store the historical average model of all previous models (i.e., the memory process) and then transfer the knowledge of the historical average model to the new model (i.e., the rememory process). To further improve the rememory ability of our RM-SimSiam, we devise an enhanced SimSiam-based contrastive loss by aligning the representations outputted by the historical and new models. Extensive experiments on three benchmarks demonstrate the effectiveness of our RM-SimSiam under the UCL setting. 

## item_id: m_3981

TITLE: Unsupervised Few Shot Learning via Self-supervised Training

ABSTRACT: Learning from limited exemplars (few-shot learning) is a fundamental, unsolved problem that has been laboriously explored in the machine learning community. However, current few-shot learners are mostly supervised and rely heavily on a large amount of labeled examples. Unsupervised learning is a more natural procedure for cognitive mammals and has produced promising results in many machine learning tasks. In the current study, we develop a method to learn an unsupervised few-shot learner via self-supervised training (UFLST), which can effectively generalize to novel but related classes. The proposed model consists of two alternate processes, progressive clustering and episodic training. The former generates pseudo-labeled training examples for constructing  episodic tasks; and the later trains the few-shot learner using the generated episodic tasks which further optimizes the feature representations of data. The two processes facilitate with each other, and eventually produce a high quality few-shot learner. Using the benchmark dataset Omniglot, we show that our model outperforms other unsupervised few-shot learning methods to a large extend and approaches to the performances of supervised methods. Using the benchmark dataset Market1501, we further demonstrate the feasibility of our model to a real-world application on person re-identification.
