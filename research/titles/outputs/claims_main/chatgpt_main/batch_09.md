# Batch 09 — 100 items

## item_id: m_0801

TITLE: Bi-Directional Block Self-Attention for Fast and Memory-Efficient Sequence Modeling

ABSTRACT: Recurrent neural networks (RNN), convolutional neural networks (CNN) and self-attention networks (SAN) are commonly used to produce context-aware representations. RNN can capture long-range dependency but is hard to parallelize and not time-efficient. CNN focuses on local dependency but does not perform well on some tasks. SAN can model both such dependencies via highly parallelizable computation, but memory requirement grows rapidly in line with sequence length. In this paper, we propose a model, called "bi-directional block self-attention network (Bi-BloSAN)", for RNN/CNN-free sequence encoding. It requires as little memory as RNN but with all the merits of SAN. Bi-BloSAN splits the entire sequence into blocks, and applies an intra-block SAN to each block for modeling local context, then applies an inter-block SAN to the outputs for all blocks to capture long-range dependency. Thus, each SAN only needs to process a short sequence, and only a small amount of memory is required. Additionally, we use feature-level attention to handle the variation of contexts around the same word, and use forward/backward masks to encode temporal order information. On nine benchmark datasets for different NLP tasks, Bi-BloSAN achieves or improves upon state-of-the-art accuracy, and shows better efficiency-memory trade-off than existing RNN/CNN/SAN. 

## item_id: m_0802

TITLE: Learning Dynamics Feature Representation via Policy Attention for Dynamic Path Planning in Urban Road Networks

ABSTRACT: Dynamic Path Planning (DPP) in urban road networks faces fundamental challenges, as traffic conditions change rapidly over time and often render planned routes ineffective. Reinforcement Learning (RL) provides an effective way to adaptively handle such uncertainties by incorporating traffic dynamics into state, but its performance crucially depends on how these dynamics are represented. Existing approaches either rely on global traffic information, which ensures decision completeness but suffers from redundancy and high computational cost, or oversimplified local features, which are efficient but often omit critical dynamics and lead to suboptimal paths. To address this, we propose a Dynamics Feature Representation (DFR) framework that progressively refines global traffic dynamics into compact features for RL-based DPP. Specifically, we introduce a policy attention mechanism that identifies a core subset of global dynamics by extracting the top-k shortest paths, and further constructs node-related local features by intersecting with n-hop neighborhoods, enabling near-optimal policy learning. Theoretical analysis demonstrates that DFR guarantees state completeness, while empirical results confirm that, compared to classical baselines and standard RL methods, DFR significantly improves path planning performance and accelerates convergence. This work highlights the central role of feature representation in RL-based DPP and proposes a general framework that balances information sufficiency with computational efficiency, paving the way for scalable dynamic decision-making in real-world transportation systems.

## item_id: m_0803

TITLE: Improving Corruption Robustness with Adversarial Feature Alignment Transformers

ABSTRACT: Despite their success, vision transformers still remain vulnerable to image corruptions, such as noise or blur. Indeed, we find that the vulnerability mainly stems from the unstable self-attention mechanism, which is inherently built upon patch-based inputs and often becomes overly sensitive to the corruptions across patches. For example, when we only occlude a small number of patches with random noise (e.g., 10%), these patch-based corruptions would lead to severe accuracy drops and greatly mislead the intermediate features as well as the corresponding attentions over them. To alleviate this issue, we seek to explicitly reduce the sensitivity of attention layers to patch-based corruptions and improve the overall robustness of transformers. In this paper, we propose the Adversarial Feature Alignment Transformer (AFAT) that aligns the features between clean examples and patch-based corruptions. To construct these corrupted examples, we build a patch corruption model to identify and occlude the patches that could severely distract the intermediate attention layers. We highlight that the corruption model is trained adversarially to the following feature alignment process, which is essentially different from existing methods. In experiments, AFAT greatly improves the stability of attention layers and consistently yields better robustness on various benchmarks, including CIFAR-10/100-C, ImageNet-A, ImageNet-C, and ImageNet-P.

## item_id: m_0804

TITLE: Leveraging Redundancy in Attention with Reuse Transformers

ABSTRACT: Pairwise dot product-based attention allows Transformers to exchange information between tokens in an input-dependent way, and is key to their success across diverse applications in language and vision. However, a typical Transformer model computes such pairwise attention scores repeatedly for the same sequence, in multiple heads in multiple layers. We systematically analyze the empirical similarity of these scores across heads and layers and find them to be considerably redundant, especially adjacent layers showing high similarity. Motivated by these findings, we propose a novel architecture that reuses attention scores computed in one layer in multiple subsequent layers. Experiments on a number of standard benchmarks show that reusing attention delivers performance equivalent to or better than standard transformers, while reducing both compute and memory usage.

## item_id: m_0805

TITLE: Binarized Convolutional Neural Networks with Channel Quadrupling and Smooth Downsampling

ABSTRACT: This paper proposes novel binarized convolutional neural networks (BCNNs) named **QB-Net** and **QSB-Net**, specifically designed to **Q**uadruple the number of channels and incorporate a so-called **S**mooth downsampling in **B**CNNs for low-cost mobile environments. The proposed models combine FP32 depthwise separable (DS) convolutions with binarized $1 \times 1$ pointwise convolutions, offering reduced computational costs in the pointwise convolutions. To enhance the degraded performance of the above naive combination, the proposed models start with a small number of channels in shallow layers and expand them during downsampling by a factor of four, effectively managing model complexity in the downsampling. The proposed model structure maintains low computational costs in the shallow blocks and increases model complexity in the deep blocks, providing a wider dynamic range to manage information in the frequency domain. As a result, the proposed models overcome the limitations of existing BCNNs, delivering improved performance while reducing the total computational costs. For further performance enhancements, we propose a novel smooth downsampling with heightwise and widthwise sequential downsampling steps, doubling the number of channels at each step. Besides, we show that the channelwise self-attention (SE) is applicable with minimal additional computational costs in the proposed models. Besides, multiple binarized convolutions in the fully-connected (FC) layer reduce storage costs without requiring 8-bit quantized convolutions. Experimental results demonstrate the efficiency of the proposed models in terms of performance, computational costs, and inference latency on real hardware. Notably, the QSB-Net-Large with SE achieve 71.2\% Top-1 accuracy on ImageNet-1K and 69.2 mean intersection over union (mIoU) in the semantic segmentation on the PASCAL VOC dataset, outperforming other counterparts.

## item_id: m_0806

TITLE: Regression from Upper One-side Labeled Data

ABSTRACT: We address a regression problem from weakly labeled data that are correctly labeled only above a regression line, i.e., upper one-side labeled data.
The label values of the data are the results of sensing the magnitude of some phenomenon.
In this case, the labels often contain missing or incomplete observations whose values are lower than those of correct observations and are also usually lower than the regression line. It follows that data labeled with lower values than the estimations of a regression function (lower-side data) are mixed with data that should originally be labeled above the regression line (upper-side data).
When such missing label observations are observed in a non-negligible amount, we thus should assume our lower-side data to be unlabeled data that are a mix of original upper- and lower-side data.
We formulate a regression problem from these upper-side labeled and lower-side unlabeled data. We then derive a learning algorithm in an unbiased and consistent manner to ordinary regression that is learned from data labeled correctly in both upper- and lower-side cases. Our key idea is that we can derive a gradient that requires only upper-side data and unlabeled data as the equivalent expression of that for ordinary regression. We additionally found that a specific class of losses enables us to learn unbiased solutions practically. In numerical experiments on synthetic and real-world datasets, we demonstrate the advantages of our algorithm.

## item_id: m_0807

TITLE: INVOCMAP: MAPPING METHOD NAMES TO METHOD INVOCATIONS VIA MACHINE LEARNING

ABSTRACT: Implementing correct method invocation is an important task for software developers. However, this is challenging work, since the structure of method invocation can be complicated. In this paper, we propose InvocMap, a code completion tool allows developers to obtain an implementation of multiple method invocations from a list of method names inside code context. InvocMap is able to predict the nested method invocations which their names didn’t appear in the list of input method names given by developers. To achieve this, we analyze the Method Invocations by four levels of abstraction. We build a Machine Translation engine to learn the mapping from the first level to the third level of abstraction of multiple method invocations, which only requires developers to manually add local variables from generated expression to get the final code. We evaluate our proposed approach on six popular libraries: JDK, Android, GWT, Joda-Time, Hibernate, and Xstream. With the training corpus of 2.86 million method invocations extracted from 1000 Java Github projects and the testing corpus extracted from 120 online forums code snippets, InvocMap achieves the accuracy rate up to 84 in F1- score depending on how much information of context provided along with method names, that shows its potential for auto code completion.

## item_id: m_0808

TITLE: Scalable Neural Theorem Proving on Knowledge Bases and Natural Language

ABSTRACT: Reasoning over text and Knowledge Bases (KBs) is a major challenge for Artificial Intelligence, with applications in machine reading, dialogue, and question answering.  Transducing text to logical forms which can be operated on is a brittle and error-prone process. Operating directly on text by jointly learning representations and transformations thereof by means of neural architectures that lack the ability to learn and exploit general rules can be very data-inefficient and not generalise correctly. These issues are addressed by Neural Theorem Provers (NTPs) (Rocktäschel & Riedel, 2017), neuro-symbolic systems based on a continuous relaxation of Prolog’s backward chaining algorithm, where symbolic unification between atoms is replaced by a differentiable operator computing the similarity between their embedding representations. In this paper, we first propose Neighbourhood-approximated Neural Theorem Provers (NaNTPs) consisting of two extensions toNTPs, namely a) a method for drastically reducing the previously prohibitive time and space complexity during inference and learning, and b) an attention mechanism for improving the rule learning process, deeming them usable on real-world datasets. Then, we propose a novel approach for jointly reasoning over KB facts and textual mentions, by jointly embedding them in a shared embedding space. The proposed method is able to extract rules and provide explanations—involving both textual patterns and KB relations—from large KBs and text corpora. We show that NaNTPs perform on par with NTPs at a fraction of a cost, and can achieve competitive link prediction results on challenging large-scale datasets, including WN18, WN18RR, and FB15k-237 (with and without textual mentions) while being able to provide explanations for each prediction and extract interpretable rules.

## item_id: m_0809

TITLE: Rethinking Label Smoothing as a Tool for Embedding Perturbation Uncertainty

ABSTRACT: Model robustness is the ability of a machine learning model to perform well when confronted with unexpected distributional shifts during inference. While various augmentation-based methods exist to improve common corruption robustness, they often rely on predefined image operations, and the untapped potential of perturbation-based strategies still exists. In response to these limitations, we repurpose label smoothing as a tool for embedding the uncertainty of perturbations. By correlating confidence levels with a monotonically decreasing function to the intensity of isotropic perturbations, we demonstrate that the model eventually acquires the increased boundary thickness and flatter minima. These metrics have strong relationships with general model robustness, extending beyond the resistance to common corruption. Our evaluations on CIFAR-10/100, Tiny-ImageNet, and ImageNet benchmarks confirm that our approach not only bolsters robustness on its own but also complements existing augmentation strategies effectively. Notably, our method enhances both common corruption and adversarial robustness in all experimental cases, a feature not observed with prior augmentations.

## item_id: m_0810

TITLE: Scalable and Equivariant Spherical CNNs by Discrete-Continuous (DISCO) Convolutions

ABSTRACT: No existing spherical convolutional neural network (CNN) framework is both computationally scalable and rotationally equivariant.  Continuous approaches capture rotational equivariance but are often prohibitively computationally demanding.  Discrete approaches offer more favorable computational performance but at the cost of equivariance. We develop a hybrid discrete-continuous (DISCO) group convolution that is simultaneously equivariant and computationally scalable to high-resolution. While our framework can be applied to any compact group, we specialize to the sphere.  Our DISCO spherical convolutions exhibit $\text{SO}(3)$ rotational equivariance, where $\text{SO}(n)$ is the special orthogonal group representing rotations in $n$-dimensions.  When restricting rotations of the convolution to the quotient space $\text{SO}(3)/\text{SO}(2)$ for further computational enhancements, we recover a form of asymptotic $\text{SO}(3)$ rotational equivariance.  Through a sparse tensor implementation we achieve linear scaling in number of pixels on the sphere for both computational cost and memory usage.  For 4k spherical images we realize a saving of $10^9$ in computational cost and $10^4$ in memory usage when compared to the most efficient alternative equivariant spherical convolution. We apply the DISCO spherical CNN framework to a number of benchmark dense-prediction problems on the sphere, such as semantic segmentation and depth estimation, on all of which we achieve the state-of-the-art performance.

## item_id: m_0811

TITLE: Generative Krylov Subspace Representations for Scalable Quantum Eigensolvers

ABSTRACT: Predicting ground state energies of quantum many-body systems is one of the central computational challenges in quantum chemistry, physics, and materials science. Krylov subspace methods, such as Krylov Quantum Diagonalization (KQD) and Sample-based Krylov Quantum Diagonalization (SKQD), are promising approaches for this task on near-term quantum computers. However, both require repeated quantum circuit executions for each Krylov subspace and for every new Hamiltonian, posing a major bottleneck under noisy hardware constraints. We introduce Generative Krylov Subspace Representations (GenKSR), a framework that learns a classical generative representation of the entire Krylov diagonalization process. To enable effective modeling of quantum systems, GenKSR leverages a conditional generative model (CGM) framework. We investigate two representative backbone architectures, the standard Transformer and the Mamba state-space model. While Transformers provide a strong baseline, Mamba offers a more computationally efficient alternative due to its linear-time complexity. By learning the distribution of measurement outcomes conditioned on Hamiltonian parameters and evolution time, GenKSR generates Krylov subspace samples for unseen Hamiltonians and for larger subspace dimensions than those used in training. This enables full energy reconstruction purely from the classical model, without additional quantum experiments. We validate our approach through simulations of 15-qubit 1D and 16-qubit 2D Heisenberg models, as well as a hardware experiment on a 20-qubit XXZ chain executed on an IBM quantum processor. Our model successfully learns the distribution from experimental data and generates a high-fidelity representation of the quantum process. This representation enables classical reproduction of experimental outcomes, supports reliable energy estimates for unseen Hamiltonians, and significantly reduces the need for further quantum computation.

## item_id: m_0812

TITLE: End-to-End Multi-Lingual Multi-Speaker Speech Recognition

ABSTRACT: The expressive power of end-to-end automatic speech recognition (ASR) systems enables direct estimation of the character or word label sequence from  a sequence of acoustic features. Direct optimization of the whole system is advantageous because it not only eliminates the internal linkage necessary for hybrid systems,  but also extends the scope of potential application use cases by training the model for multiple objectives. Several multi-lingual ASR systems were recently proposed based on a monolithic neural network architecture without language-dependent modules, showing that modeling of multiple languages is well within the capabilities of an end-to-end framework. There has also been growing interest in multi-speaker speech recognition, which enables generation of multiple label sequences from single-channel mixed speech. In particular, a multi-speaker end-to-end ASR system that can directly model one-to-many mappings without additional auxiliary clues was recently proposed. In this paper, we propose an all-in-one end-to-end multi-lingual multi-speaker ASR system that integrates the capabilities of these two systems.  The proposed model is evaluated using mixtures of two speakers generated by using 10 languages, including mixed-language utterances. 

## item_id: m_0813

TITLE: Model Specialization for Inference Via End-to-End Distillation, Pruning, and Cascades

ABSTRACT: The availability of general-purpose reference and benchmark datasets such as
ImageNet have spurred the development of general-purpose popular reference
model architectures and pre-trained weights. However, in practice, neural net-
works are often employed to perform specific, more restrictive tasks, that are
narrower in scope and complexity. Thus, simply fine-tuning or transfer learn-
ing from a general-purpose network inherits a large computational cost that may
not be necessary for a given task. In this work, we investigate the potential for
model specialization, or reducing a model’s computational footprint by leverag-
ing task-specific knowledge, such as a restricted inference distribution. We study
three methods for model specialization—1) task-aware distillation, 2) task-aware
pruning, and 3) specialized model cascades—and evaluate their performance on
a range of classification tasks. Moreover, for the first time, we investigate how
these techniques complement one another, enabling up to 5× speedups with no
loss in accuracy and 9.8× speedups while remaining within 2.5% of a highly ac-
curate ResNet on specialized image classification tasks. These results suggest that
simple and easy-to-implement specialization procedures may benefit a large num-
ber practical applications in which the representational power of general-purpose
networks need not be inherited.

## item_id: m_0814

TITLE: Learning by Exclusion: An Evidential Contrapositive Framework for Zero-Shot OOD Detection

ABSTRACT: Out-of-Distribution (OOD) detection is critical for deploying vision-language models in safety-sensitive settings. While recent approaches such as CLIPN rely solely on margin-based cosine similarity for separating in- and out-of-distribution samples, this reliance provides limited safeguards against overconfident representations. We introduce the Evidential Contrapositive Framework (ECF), a principled approach that integrates logical negation into vision-language alignment to explicitly model what a class is not. Unlike prior work that enforces separation through heuristic margins, ECF specifically introduces (i) exclusion via contrapositive loss, (ii) decoupling via negative prompt alignment, and (iii) logical consistency via contrapositive similarity regularization. To further enhance reliability, we couple this framework with evidential uncertainty modeling using a Dirichlet distribution, enabling simultaneous estimation of aleatoric and epistemic uncertainty. This combination yields interpretable uncertainty-aware decision boundaries and robust rejection of OOD inputs without requiring access to OOD samples during training. Extensive experiments on large-scale benchmarks demonstrate that ECF significantly outperforms state-of-the-art zero-shot OOD methods, both in detection accuracy and in uncertainty calibration, validating the advantage of principled contrapositive reasoning over margin-based objectives.

## item_id: m_0815

TITLE: Generalizing Skills with Semi-Supervised Reinforcement Learning

ABSTRACT: Deep reinforcement learning (RL) can acquire complex behaviors from low-level inputs, such as images. However, real-world applications of such methods require generalizing to the vast variability of the real world. Deep networks are known to achieve remarkable generalization when provided with massive amounts of labeled data, but can we provide this breadth of experience to an RL agent, such as a robot? The robot might continuously learn as it explores the world around it, even while it is deployed and performing useful tasks. However, this learning requires access to a reward function, to tell the agent whether it is succeeding or failing at its task. Such reward functions are often hard to measure in the real world, especially in domains such as robotics and dialog systems, where the reward could depend on the unknown positions of objects or the emotional state of the user. On the other hand, it is often quite practical to provide the agent with reward functions in a limited set of situations, such as when a human supervisor is present, or in a controlled laboratory setting. Can we make use of this limited supervision, and still benefit from the breadth of experience an agent might collect in the unstructured real world? In this paper, we formalize this problem setting as semi-supervised reinforcement learning (SSRL), where the reward function can only be evaluated in a set of “labeled” MDPs, and the agent must generalize its behavior to the wide range of states it might encounter in a set of “unlabeled” MDPs, by using experience from both settings. Our proposed method infers the task objective in the unlabeled MDPs through an algorithm that resembles inverse RL, using the agent’s own prior experience in the labeled MDPs as a kind of demonstration of optimal behavior. We evaluate our method on challenging, continuous control tasks that require control directly from images, and show that our approach can improve the generalization of a learned deep neural network policy by using experience for which no reward function is available. We also show that our method outperforms direct supervised learning of the reward.

## item_id: m_0816

TITLE: Semantic Structure in Large Language Model Embeddings

ABSTRACT: Psychological research consistently finds that human ratings of words across diverse semantic scales can be reduced to a low-dimensional form with relatively little information loss. We find that the semantic associations encoded in the embedding matrices of large language models (LLMs) exhibit a similar structure. We show that the projections of words on semantic directions defined by antonym pairs (e.g. kind - cruel) correlate highly with human ratings, and further find that these projections effectively reduce to a 3-dimensional subspace within LLM embeddings, closely resembling the patterns derived from human survey responses. Moreover, we find that shifting tokens along one semantic direction causes off-target effects on geometrically aligned features proportional to their cosine similarity. These findings suggest that semantic features are entangled within LLMs similarly to how they are interconnected in human language, and a great deal of semantic information, despite its apparent complexity, is surprisingly low-dimensional. Furthermore, accounting for this semantic structure may prove essential for avoiding unintended consequences when steering features.

## item_id: m_0817

TITLE: Network robustness as a mathematical property: training, evaluation and attack

ABSTRACT: Neural networks are widely used in AI for their ability to detect general patterns in noisy data. Paradoxically, by default they are also known to not be particularly robust, i.e. moving a small distance in the input space can result in the network's output changing significantly.
Many methods for improving neural network robustness have been proposed recently. This growing body of research gave rise to numerous explicit or implicit notions of robustness.  Connections between these notions are often subtle, and a systematic comparison of these different definitions was lacking in the literature.
In this paper we attempt to address this gap by performing an in-depth comparison of the different definitions of robustness, by analysing their relationships, assumptions, interpretability and verifiability.
By abstracting robustness as a stand-alone mathematical property, we are able to show that, having a choice of several  definitions of robustness, one can combine them in a modular way when defining training modes, evaluation metrics, and attacks on neural networks.
We also perform experiments to compare the applicability and efficacy of different training methods for ensuring the network obeys these different definitions.

## item_id: m_0818

TITLE: Analysing Features Learned Using Unsupervised Models on Program Embeddings

ABSTRACT: In this paper, we propose a novel approach for analyzing and evaluating how a deep neural network is autonomously learning different features related to programs on different input representations.
We trained a simple autoencoder having 5 hidden layers on a dataset containing Java programs, and we tested the ability of each of its neurons in detecting different program features using only unlabeled data for the training phase. For doing that, we designed two binary classification problems having different scopes: while the first one is based on the program cyclomatic complexity, the other one is defined starting from the identifiers chosen by the programmers, making it more related to the functionality (and thus, to some extent, to the semantic) of the program than to its structure. Using different program vector representations as input, we performed experiments considering the two problems, showing how some neurons can be effectively used as classifiers for programs on different binary tasks. We also discuss how the program representation chosen as input affects the classification performance, stating that new and customized program embeddings could be designed in order to obtain models able to solve different tasks guided by the proposed benchmarking approach.

## item_id: m_0819

TITLE: On the Discrimination-Generalization Tradeoff in GANs

ABSTRACT: Generative adversarial training can be generally understood as minimizing certain moment matching loss defined by a set of discriminator functions, typically  neural networks. The discriminator set should be large enough to be able to uniquely identify the true distribution (discriminative), and also be small enough to go beyond memorizing samples (generalizable). In this paper, we show that a discriminator set is guaranteed to be discriminative whenever its linear span is dense in the set of bounded continuous functions. This is a very mild condition satisfied even by neural networks with a single neuron. Further, we develop generalization bounds between the learned distribution and true distribution under different evaluation metrics. When evaluated with neural distance, our bounds show that generalization is guaranteed as long as the discriminator set is small enough, regardless of the size of the generator or hypothesis set. When evaluated with KL divergence, our bound provides an explanation on the counter-intuitive behaviors of testing likelihood in GAN training. Our analysis sheds lights on understanding the practical performance of GANs.

## item_id: m_0820

TITLE: ResBinNet: Residual Binary Neural Network

ABSTRACT: Recent efforts on training light-weight binary neural networks offer promising execution/memory efficiency. This paper introduces ResBinNet, which is a composition of two interlinked methodologies aiming to address the slow convergence speed and limited accuracy of binary convolutional neural networks. The first method, called residual binarization, learns a multi-level binary representation for the features within a certain neural network layer. The second method, called temperature adjustment, gradually binarizes the weights of a particular layer. The two methods jointly learn a set of soft-binarized parameters that improve the convergence rate and accuracy of binary neural networks. We corroborate the applicability and scalability of ResBinNet by implementing a prototype hardware accelerator. The accelerator is reconfigurable in terms of the numerical precision of the binarized features, offering a trade-off between runtime and inference accuracy.


## item_id: m_0821

TITLE: Towards Understanding Link Predictor Generalizability Under Distribution Shifts

ABSTRACT: State-of-the-art link prediction (LP) models demonstrate impressive benchmark
results. However, popular benchmark datasets often assume that training, validation, and testing samples are representative of the overall dataset distribution. In
real-world situations, this assumption is often incorrect; since uncontrolled factors
lead to the problem where new dataset samples come from different distributions
than training samples. The vast majority of recent work focuses on dataset shift
affecting node- and graph-level tasks, largely ignoring link-level tasks. To bridge
this gap, we introduce a novel splitting strategy, known as LPShift, which utilizes
structural properties to induce a controlled distribution shift. We verify the effect of LPShift through empirical evaluation of SOTA LP methods on 16 LPShift
generated splits of Open Graph Benchmark (OGB) datasets. When benchmarked
with LPShift datasets, GNN4LP methods frequently generalize worse than heuristics or basic GNNs. Furthermore, LP-specific generalization techniques do little
to improve performance under LPShift. Finally, further analysis provides insight
on why LP models lose much of their architectural advantages under LPShift.

## item_id: m_0822

TITLE: A Neural Knowledge Language Model

ABSTRACT: Current language models have significant limitations in their ability to encode and decode knowledge. This is mainly because they acquire knowledge based on statistical co-occurrences, even if most of the knowledge words are rarely observed named entities. In this paper, we propose a Neural Knowledge Language Model (NKLM) which combines symbolic knowledge provided by a knowledge graph with the RNN language model. At each time step, the model predicts a fact on which the observed word is to be based. Then, a word is either generated from the vocabulary or copied from the knowledge graph. We train and test the model on a new dataset, WikiFacts. In experiments, we show that the NKLM significantly improves the perplexity while generating a much smaller number of unknown words. In addition, we demonstrate that the sampled descriptions include named entities which were used to be the unknown words in RNN language models.


## item_id: m_0823

TITLE: NeuralMark: Advancing White-Box Neural Network Watermarking

ABSTRACT: As valuable digital assets, deep neural networks require ownership protection, making neural network watermarking (NNW) a promising solution. In this paper, we propose a *NeuralMark* method to advance white-box NNW, which can be seamlessly integrated into various network architectures. NeuralMark first establishes a hash mapping between the secret key and the watermark, enabling resistance to forging attacks. The watermark then functions as a filter to select model parameters for embedding, providing resilience against overwriting attacks. Furthermore, NeuralMark utilizes average pooling to defend against fine-tuning and pruning attacks. Theoretically, we analyze its security boundary. Empirically, we verify its effectiveness across 14 distinct Convolutional and Transformer architectures, covering five image classification tasks and one text generation task. The source codes are available at https://anonymous.4open.science/r/NeuralMark.

## item_id: m_0824

TITLE: An Ensemble of Retrieval-Based and Generation-Based Human-Computer Conversation Systems.

ABSTRACT: Human-computer conversation systems have attracted much attention in Natural Language Processing. Conversation systems can be roughly divided into two categories: retrieval-based and generation-based systems. Retrieval systems search a user-issued utterance (namely a query) in a large conversational repository and return a reply that best matches the query. Generative approaches synthesize new replies. Both ways have certain advantages but suffer from their own disadvantages. We propose a novel ensemble of retrieval-based and generation-based conversation system. The retrieved candidates, in addition to the original query, are fed to a reply generator via a neural network, so that the model is aware of more information. The generated reply together with the retrieved ones then participates in a re-ranking process to find the final reply to output. Experimental results show that such an ensemble system outperforms each single module by a large margin.


## item_id: m_0825

TITLE: Learning Recurrent Span Representations for Extractive Question Answering

ABSTRACT: The reading comprehension task, that asks questions about a given evidence document, is a central problem in natural language understanding. Recent formulations of this task have typically focused on answer selection from a set of candidates pre-defined manually or through the use of an external NLP pipeline. However, Rajpurkar et al. (2016) recently released the SQUAD dataset in which the answers can be arbitrary strings from the supplied text. In this paper, we focus on this answer extraction task, presenting a novel model architecture that efficiently builds fixed length representations of all spans in the evidence document with a recurrent network. We show that scoring explicit span representations significantly improves performance over other approaches that factor the prediction into separate predictions about words or start and end markers. Our approach improves upon the best published results of Wang & Jiang (2016) by 5% and decreases the error of Rajpurkar et al.’s baseline by > 50%.

## item_id: m_0826

TITLE: Exploration using Distributional RL and UCB

ABSTRACT:     We establish the relation between Distributional RL and the Upper Confidence Bound (UCB) approach to exploration.
    In this paper we show that the density of the Q function estimated by Distributional RL can be successfully used for the estimation of UCB. This approach does not require counting and, therefore, generalizes well to the Deep RL. We also point to the asymmetry of the empirical densities estimated by the Distributional RL algorithms like QR-DQN. This observation leads to the reexamination of the variance's performance in the UCB type approach to exploration. We introduce truncated variance as an alternative estimator of the UCB and a novel algorithm based on it. We empirically show that newly introduced algorithm achieves better performance in multi-armed bandits setting. Finally, we extend this approach to high-dimensional setting and test it on the Atari 2600 games. New approach achieves better performance compared to QR-DQN in 26 of games, 13 ties out of 49 games.

## item_id: m_0827

TITLE: PF-GNN: Differentiable particle filtering based approximation of universal graph representations

ABSTRACT: Message passing Graph Neural Networks (GNNs) are known to be limited in expressive power by the 1-WL color-refinement test for graph isomorphism. Other more expressive models either are computationally expensive or need preprocessing to extract structural features from the graph. In this work, we propose to make GNNs universal by guiding the learning process with exact isomorphism solver techniques which operate on the paradigm of $\textit{Individualization and refinement}$ (IR), a method to artificially introduce asymmetry and further refine the coloring when 1-WL stops. Isomorphism solvers generate a search-tree of colorings whose leaves uniquely identify the graph. However, the tree grows exponentially large and needs hand-crafted pruning techniques which are not desirable from a learning perspective. We take a probabilistic view and approximate the search tree of colorings ( i.e. embeddings) by sampling multiple paths from root to leaves of the search-tree. To learn more discriminative representations, we guide the sampling process with $\textit{particle filter}$ updates, a principled approach for sequential state estimation. Our algorithm is end-to-end differentiable, can be applied with any GNN as backbone and learns richer graph representations with only linear increase in runtime. Experimental evaluation shows that our approach consistently outperforms leading GNN models on both synthetic benchmarks for isomorphism detection as well as real-world datasets.

## item_id: m_0828

TITLE: Input Convex Graph Neural Networks: An Application to Optimal Control and Design Optimization

ABSTRACT: Despite the success of modeling networked systems via graph neural networks (GNN), applying GNN for the model-based control is pessimistic since the non-convexity of GNN models hinders solving model-based control problems. In this regard, we propose the input convex graph neural networks (ICGNN) whose inputs and outputs are related via convex functions. When ICGNN is used to model the target objective function, the decision-making problem becomes a convex optimization problem due to the convexity of ICGNN and the corresponding solution can be obtained efficiently. We assess the prediction and control performance of ICGNN on several benchmarks and physical heat diffusion problems, respectively. On the physical heat diffusion, we further apply ICGNN to solve a design optimization problem, which seeks to find the optimal heater allocations while considering the optimal operation of the heaters, by using a gradient-based method. We cast the design optimization problem as a bi-level optimization problem. In there, the input convexity of ICGNN allows us to compute the gradient of the lower level problem (i.e., control problem with a given heater allocation) without bias. We confirm that ICGNN significantly outperforms non-input convex GNN to solve the design optimization problem.

## item_id: m_0829

TITLE: Optimisation-Based Multi-Modal Semantic Image Editing

ABSTRACT: Image editing affords increased control over the aesthetics and content of generated images. Pre-existing works focus predominantly on text-based instructions to achieve desired image modifications, which limit edit precision and accuracy. In this work, we propose an inference-time editing optimisation, designed to extend beyond textual edits to accommodate multiple editing instruction types (e.g., spatial layout-based; pose, scribbles, edge maps). We propose to disentangle the editing task into two competing subtasks: successful local image modifications and global content consistency preservation, where subtasks are guidedthrough two dedicated loss functions. By allowing to adjust the influence of each loss function, we build a flexible editing solution that can be adjusted to user preferences. We evaluate our method using text, pose and scribble edit conditions, and highlight our ability to achieve complex edits, through both qualitative and quantitative experiments.

## item_id: m_0830

TITLE: Style Memory: Making a Classifier Network Generative

ABSTRACT: Deep networks have shown great performance in classification tasks. However, the parameters learned by the classifier networks usually discard stylistic information of the input, in favour of information strictly relevant to classification. We introduce a network that has the capacity to do both classification and reconstruction by adding a "style memory" to the output layer of the network. We also show how to train such a neural network as a deep multi-layer autoencoder, jointly minimizing both classification and reconstruction losses. The generative capacity of our network demonstrates that the combination of style-memory neurons with the classifier neurons yield good reconstructions of the inputs when the classification is correct. We further investigate the nature of the style memory, and how it relates to composing digits and letters.

## item_id: m_0831

TITLE: Data Interpretation and Reasoning Over Scientific Plots

ABSTRACT: Data Interpretation is an important part of Quantitative Aptitude exams and requires an individual to answer questions grounded in plots such as bar charts, line graphs, scatter plots, \textit{etc}. Recently, there has been an increasing interest in building models which can perform this task by learning from datasets containing triplets of the form \{plot, question, answer\}. Two such datasets have been proposed in the recent past which contain plots generated from synthetic data with limited (i) $x-y$ axes variables (ii) question templates and (iii) answer vocabulary and hence do not adequately capture the challenges posed by this task. To overcome these limitations of existing datasets, we introduce a new dataset containing $9.7$ million question-answer pairs grounded over $270,000$ plots with three main differentiators. First, the plots in our dataset contain a wide variety of realistic $x$-$y$ variables such as CO2 emission, fertility rate, \textit{etc.} extracted from  real word data sources such as World Bank, government sites, \textit{etc}. Second, the questions in our dataset are more complex as they are based on templates extracted from interesting questions asked by a crowd of workers using a fraction of these plots. Lastly, the answers in our dataset are not restricted to a small vocabulary and a large fraction of the answers seen at test time are not present in the training vocabulary. As a result, existing models for Visual Question Answering which largely use end-to-end models in a multi-class classification framework cannot be used for this task. We establish initial results on this dataset and emphasize the complexity of the task using a multi-staged modular pipeline with various sub-components to (i) extract relevant data from the plot and convert it to a semi-structured table (ii) combine the question with this table and use compositional semantic parsing to arrive at a logical form from which the answer can be derived. We believe that such a modular framework is the best way to go forward as it would enable the research community to independently make progress on all the sub-tasks involved in plot question answering.

## item_id: m_0832

TITLE: Learning Deep Features in Instrumental Variable Regression

ABSTRACT: Instrumental variable (IV) regression is a standard strategy for learning causal relationships between confounded treatment and outcome variables from observational data by using an instrumental variable, which affects the outcome only through the treatment. In classical IV regression, learning proceeds in two stages: stage 1 performs linear regression from the instrument to the treatment; and stage 2 performs linear regression from the treatment to the outcome, conditioned on the instrument. We propose a novel method, deep feature instrumental variable regression (DFIV), to address the case where relations between instruments, treatments, and outcomes may be nonlinear. In this case, deep neural nets are trained to define informative nonlinear features on the instruments and treatments. We propose an alternating training regime for these features to ensure good end-to-end performance when composing stages 1 and 2, thus obtaining highly flexible feature maps in a computationally efficient manner.
DFIV outperforms recent state-of-the-art methods on challenging IV benchmarks, including settings involving high dimensional image data. DFIV also exhibits competitive performance in off-policy policy evaluation for reinforcement learning, which can be understood as an IV regression task.

## item_id: m_0833

TITLE: Design-Bench: Benchmarks for Data-Driven Offline Model-Based Optimization

ABSTRACT: Black-box model-based optimization (MBO) problems, where the goal is to find a design input that maximizes an unknown objective function, are ubiquitous in a wide range of domains, such as the design of drugs, aircraft, and robot morphology. Typically, such problems are solved by actively querying the black-box objective on design proposals and using the resulting feedback to improve the proposed designs. However, when the true objective function is expensive or dangerous to evaluate in the real world, we might instead prefer a method that can optimize this function using only previously collected data, for example from a set of previously conducted experiments. This data-driven offline MBO set- ting presents a number of unique challenges, but a number of recent works have demonstrated that viable offline MBO methods can be developed even for high- dimensional problems, using high-capacity deep neural network function approximators. Unfortunately, the lack of standardized evaluation tasks in this emerg- ing new field has made tracking progress and comparing recent methods difficult. To address this problem, we present Design-Bench, a benchmark suite of offline MBO tasks with a unified evaluation protocol and reference implementations of recent methods. Our benchmark suite includes diverse and realistic tasks derived from real-world problems in biology, material science, and robotics that present distinct challenges for offline MBO methods. Our benchmarks, together with the reference implementations, are available at sites.google.com/view/design-bench. We hope that our benchmark can serve as a meaningful metric for the progress of offline MBO methods and guide future algorithmic development.

## item_id: m_0834

TITLE:  Large-Scale Visual Speech Recognition

ABSTRACT: This work presents a scalable solution to continuous visual speech recognition. To achieve this, we constructed the largest existing visual speech recognition dataset, consisting of pairs of text and video clips of faces speaking (3,886 hours of video). In tandem, we designed and trained an integrated lipreading system, consisting of a video processing pipeline that maps raw video to stable videos of lips and sequences of phonemes, a scalable deep neural network that maps the lip videos to sequences of phoneme distributions, and a production-level speech decoder that outputs sequences of words. The proposed system achieves a word error rate (WER) of 40.9% as measured on a held-out set. In comparison, professional lipreaders achieve either 86.4% or 92.9% WER on the same dataset when having access to additional types of contextual information. Our approach significantly improves on previous lipreading approaches, including variants of LipNet and of Watch, Attend, and Spell (WAS), which are only capable of 89.8% and 76.8% WER respectively.

## item_id: m_0835

TITLE: Parameter Release and Knowledge Reuse for Class-Incremental Semantic Segmentation

ABSTRACT: Class-incremental semantic segmentation aims to progressively learn new classes while preserving previously acquired knowledge. This task becomes particularly challenging when prior training samples are unavailable due to data privacy or storage restrictions, resulting in catastrophic forgetting. To address this issue, knowledge distillation is widely adopted as a constraint by maximizing the similarity of representations between the current model (learning new classes) and the previous model (retaining old ones). However, knowledge distillation inherently preserves the old-knowledge distribution with minimal modification. This constraint limits the parameters available for learning new classes when substantial information from old classes is retained. Furthermore, the acquired old knowledge is often ignored to facilitate the learning of new knowledge, resulting in a waste of previously learned procedures. The above two problems result in the risk of class confusion and deviating from the performance of joint learning. Based on such analysis, we propose Distribution-based Knowledge Distillation (DKD) via a minimization--maximization distribution strategy. On the one hand, to alleviate the parameter competition between old and new knowledge, we minimize the distribution of old knowledge after releasing low-sensitivity parameters to old classes. On the other hand, to effectively utilize the valuable knowledge previously acquired, we maximize shared-knowledge distribution between the old and new knowledge after approximating the new knowledge distribution via Laplacian-based projection estimation. The proposed method achieves an excellent balance between stability and plasticity in nine diverse settings on Pascal VOC and ADE20K. Notably, its average performance approaches that of joint learning (upper bound) while effectively reducing class confusion. The source code is provided in the supplementary material and will be made publicly available upon acceptance.

## item_id: m_0836

TITLE: Deep Generative Dual Memory Network for Continual Learning

ABSTRACT: Despite advances in deep learning, artificial neural networks do not learn the same way as humans do. Today, neural networks can learn multiple tasks when trained on them jointly, but cannot maintain performance on learnt tasks when tasks are presented one at a time -- this phenomenon called catastrophic forgetting is a fundamental challenge to overcome before neural networks can learn continually from incoming data. In this work, we derive inspiration from human memory to develop an architecture capable of learning continuously from sequentially incoming tasks, while averting catastrophic forgetting. Specifically, our model consists of a dual memory architecture to emulate the complementary learning systems (hippocampus and the neocortex) in the human brain and maintains a consolidated long-term memory via generative replay of past experiences. We (i) substantiate our claim that replay should be generative, (ii) show the benefits of generative replay and dual memory via experiments, and (iii) demonstrate improved performance retention even for small models with low capacity. Our architecture displays many important characteristics of the human memory and provides insights on the connection between sleep and learning in humans.

## item_id: m_0837

TITLE: Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing

ABSTRACT: High-quality instruction data is critical for aligning large language models (LLMs). Although some models, such as Llama-3-Instruct, have open weights, their alignment data remain private, which hinders the democratization of AI. High human labor costs and a limited, predefined scope for prompting prevent existing open-source data creation methods from scaling effectively, potentially limiting the diversity and quality of public alignment datasets. Is it possible to synthesize high-quality instruction data at scale by extracting it directly from an aligned LLM? We present a self-synthesis method for generating large-scale alignment data named Magpie.  Our key observation is that aligned LLMs like Llama-3-Instruct can generate a user query when we input only the pre-query templates up to the position reserved for user messages, thanks to their auto-regressive nature.  We use this method to prompt Llama-3-Instruct and generate 4 million instructions along with their corresponding responses. We further introduce extensions of Magpie for filtering, generating multi-turn, preference optimization, domain-specific and multilingual datasets. We perform a comprehensive analysis of the Magpie-generated data. To compare Magpie-generated data with other public instruction datasets (e.g., ShareGPT, WildChat, Evol-Instruct, UltraChat, OpenHermes, Tulu-V2-Mix, GenQA), we fine-tune Llama-3-8B-Base with each dataset and evaluate the performance of the fine-tuned models. Our results indicate that using Magpie for supervised fine-tuning (SFT) solely can surpass the performance of previous public datasets utilized for both SFT and preference optimization, such as direct preference optimization with UltraFeedback. We also show that in some tasks, models supervised fine-tuned with Magpie perform comparably to the official Llama-3-8B-Instruct, despite the latter being enhanced with 10 million data points through SFT and subsequent preference optimization. This advantage is evident on alignment benchmarks such as AlpacaEval, ArenaHard, and WildBench.

## item_id: m_0838

TITLE: Improving Generalization with Domain Convex Game

ABSTRACT: Domain generalization (DG) tends to alleviate the poor generalization capability of deep neural networks by learning model with multiple source domains. A classical solution to DG is domain augmentation, the common belief of which is that diversifying source domains will be conducive to the out-of-distribution generalization. However, these claims are understood intuitively, rather than mathematically, and the relation between the diversity of source domains and model generalization still remains unclear. We thus made some explorations and found that the model generalization does not strictly improve with the increase of domain diversity, limiting the effectiveness of domain augmentation. In view of this observation, we propose a new perspective on DG that recast it as a convex game between domains.
We formulate a regularization term based on the supermodularity property of convex game which rigorously demonstrates that the growth of domain diversity will enhance model generalization monotonically. This enables model to best utilize the rich information within input data so that each diversified domain contributes to model generalization. Furthermore, we construct a sample filter to eliminate the bad samples which contain unprofitable or even harmful information to generalization performance, such as noisy or redundant samples. Our framework presents a new avenue for the formal analysis of DG, the rationality and effectiveness of which have been demonstrated on extensive benchmark datasets.

## item_id: m_0839

TITLE: Debiased Contrastive Learning with multi-resolution Kolmogorov-Arnold Network for Gravitational Wave Glitch Detection

ABSTRACT: Time-series gravitational wave glitch detection presents significant challenges for machine learning due to the complexity of the data, limited labeled examples, and data imbalance. To address these issues, we introduce Debiased Contrastive Learning with Multi-Resolution Kolmogorov-Arnold Network(dcMltR-KAN), a novel self-supervised learning (SSL) approach that enhances glitch detection, robustness, explainability, and generalization. dcMltR-KAN consists of three key novel components: Wasserstein Debiased Contrastive Learning (wDCL), a CNN-based encoder, and a Multi-Resolution KAN (MltR-KAN). The wDCL improves the model’s sensitivity to data imbalance and geometric structure. The CNN-based encoder eliminates false negatives during training, refines feature representations through similarity-based weighting (SBW), and reduces data complexity within the embedding. Additionally, MltR-KAN enhances explainability, generalization, and efficiency by adaptively learning parameters. Our model outperforms widely used baselines on O1, O2, and O3 data, demonstrating its effectiveness. Extending dcMltR-KAN to other time-series benchmarks underscores its novelty and efficiency, marking it as the first model of its kind and paving the way for future SSL and astrophysics research.

## item_id: m_0840

TITLE: Rewarding Episodic Visitation Discrepancy for Exploration in Reinforcement Learning

ABSTRACT: Exploration is critical for deep reinforcement learning in complex environments with high-dimensional observations and sparse rewards. To address this problem, recent approaches proposed to leverage intrinsic rewards to improve exploration, such as novelty-based exploration and prediction-based exploration. However, many intrinsic reward modules require sophisticated structures and representation learning, resulting in prohibitive computational complexity and unstable performance. In this paper, we propose Rewarding Episodic Visitation Discrepancy (REVD), a computation-efficient and quantified exploration method. More specifically, REVD provides intrinsic rewards by evaluating the Rényi divergence-based visitation discrepancy between episodes. To estimate the divergence efficiently, a $k$-nearest neighbor estimator is utilized with a randomly-initialized state encoder. Finally, the REVD is tested on Atari games and PyBullet Robotics Environments. Extensive experiments demonstrate that REVD can significantly improve the sample efficiency of reinforcement learning algorithms and outperform the benchmarking methods.

## item_id: m_0841

TITLE: Counting the Paths in Deep Neural Networks as a Performance Predictor

ABSTRACT: We propose a novel quantitative measure to predict the performance of a deep neural network classifier, where the measure is derived exclusively from the graph structure of the network. We expect that this measure is a fundamental first step in developing a method to evaluate new network architectures and reduce the reliance on the computationally expensive trial and error or "brute force" optimisation processes involved in model selection. The measure is derived in the context of multi-layer perceptrons (MLPs), but the definitions are shown to be useful also in the context of deep convolutional neural networks (CNN), where it is able to estimate and compare the relative performance of different types of neural networks, such as VGG, ResNet, and DenseNet. Our measure is also used to study the effects of some important "hidden" hyper-parameters of the DenseNet architecture, such as number of layers, growth rate and the dimension of 1x1 convolutions in DenseNet-BC. Ultimately, our measure facilitates the optimisation of the DenseNet design, which shows improved results compared to the baseline.


## item_id: m_0842

TITLE: Generative Principal Component Analysis

ABSTRACT: In this paper, we study the problem of principal component analysis with generative modeling assumptions, adopting a general model for the observed matrix that encompasses notable special cases, including spiked matrix recovery and phase retrieval. The key assumption is that the first principal eigenvector lies near the range of an $L$-Lipschitz continuous generative model with bounded $k$-dimensional inputs. We propose a quadratic estimator, and show that it enjoys a statistical rate of order $\sqrt{\frac{k\log L}{m}}$, where $m$ is the number of samples. Moreover, we provide a variant of the classic power method, which projects the calculated data onto the range of the generative model during each iteration. We show that under suitable conditions, this method converges exponentially fast to a point achieving the above-mentioned statistical rate. This rate is conjectured in~\citep{aubin2019spiked,cocola2020nonasymptotic} to be the best possible even when we only restrict to the special case of spiked matrix models. We perform experiments on various image datasets for spiked matrix and phase retrieval models, and illustrate performance gains of our method to the classic power method and the truncated power method devised for sparse principal component analysis.

## item_id: m_0843

TITLE: Learning Label Distribution with Subtasks

ABSTRACT: Label distribution learning (LDL) is a novel learning paradigm that emulates label polysemy by assigning label distributions over the label space. However, recent LDL work seems to exhibit a notable contradiction: 1) some existing LDL methods employ auxiliary tasks to enhance performance, which narrows their focus to specific domains, thereby lacking generalization capability; 2) conversely, LDL methods without auxiliary tasks rely on losses tailored solely to label distributions of the primary task, lacking additional supervised information to guide the learning process. In this paper, we propose $\mathcal{S}$-LDL, a novel and minimalist solution that partitions the label distribution of the primary task into subtask label distributions, i.e., a form of pseudo-supervised information, to reconcile the above contradiction. $\mathcal{S}$-LDL encompasses two key aspects: 1) an algorithm capable of generating subtasks without any extra knowledge, with subtasks deemed valid and reconstructable via our analysis; and 2) a plug-and-play framework seamlessly compatible with existing LDL methods, and even adaptable to derivative tasks of LDL. Experiments demonstrate that $\mathcal{S}$-LDL is effective and efficient. To the best of our knowledge, this represents the first endeavor to address LDL via subtasks. The code will soon be available on GitHub to facilitate reproducible research.

## item_id: m_0844

TITLE: Sparta: Spatially Attentive and Adversarially Robust Activations

ABSTRACT: Adversarial training has been demonstrated to be useful for improving the robustness of deep neural networks (DNNs). However, the impacts of basic network components (e.g., ReLU, the widely used activation function for DNNs) to adversarial training effectiveness received less attention and has not been comprehensively investigated so far. To fill this gap, in this work, we argue that the spatially-shared and input-independent activating properties of the ReLU make the DNNs under both standard training and adversarial training less robust to white-box adversarial attacks. To address such challenges, we design a novel activation function, i.e., Sparta: Spatially Attentive and Adversarially Robust Activation, which enables DNNs to achieve higher robustness (i.e., lower error rate on adversarial examples) and accuracy (i.e., lower error rate on clean examples) than the DNNs based on the state-of-the-art activation functions. We further investigate the relationships between our Sparta and the state-of-the-art search-based activation function, i.e., Swish, and feature denoising method, providing insights about the advantages of our method. Moreover, comprehensive evaluations have demonstrated two important properties of our method: First, superior transferability across DNNs. Our adversarially trained Sparta function for one DNN (e.g., ResNet-18) can be fixed to train another adversarially robust DNN (e.g., ResNet-34), achieving higher robustness than the one using vanilla ReLU as activation. Second, superior transferability across datasets. The Sparta function trained on one dataset (e.g., CIFAR-10) can be employed to train adversarially robust DNNs on another dataset (e.g., SVHN) and helps achieve higher robustness than DNNs with vanilla ReLU as activation.  These properties have highlighted the flexibility and versatility of Sparta. Accompanying code is also submitted.

## item_id: m_0845

TITLE: A Unified Framework for Multi-distribution Density Ratio Estimation

ABSTRACT: Binary density ratio estimation (DRE), the problem of estimating the ratio $p_1/p_2$ given their empirical samples, provides the foundation for many state-of-the-art machine learning algorithms such as contrastive representation learning and covariate shift adaptation. In this work, we consider a generalized setting where given samples from multiple distributions $p_1, \ldots, p_k$ (for $k > 2$), we aim to efficiently estimate the density ratios between all pairs of distributions. Such a generalization leads to important new applications such as estimating statistical discrepancy among multiple random variables like multi-distribution $f$-divergence and bias correction via multiple importance sampling. We then develop a general framework from the perspective of Bregman divergence minimization, where each strictly convex multivariate function induces a proper loss for multi-distribution DRE. Moreover, we formally relate multi-distribution density ratio estimation and class probability estimation, theoretically justifying the use of any strictly proper scoring rule composite with a link function for multi-distribution DRE. We show that our framework leads to methods that strictly generalize their counterparts in binary DRE, as well as new methods that show comparable or superior performance on various downstream tasks.

## item_id: m_0846

TITLE: Directional Analysis of Stochastic Gradient Descent via von Mises-Fisher Distributions in Deep Learning

ABSTRACT: Although stochastic gradient descent (SGD) is a driving force behind the recent success of deep learning, our understanding of its dynamics in a high-dimensional parameter space is limited. In recent years, some researchers have used the stochasticity of minibatch gradients, or the signal-to-noise ratio, to better characterize the learning dynamics of SGD. Inspired from these work, we here analyze SGD from a geometrical perspective by inspecting the stochasticity of the norms and directions of minibatch gradients. We propose a model of the directional concentration for minibatch gradients through von Mises-Fisher (VMF) distribution, and show that the directional uniformity of minibatch gradients increases over the course of SGD. We empirically verify our result using deep convolutional networks and observe a higher correlation between the gradient stochasticity and the proposed directional uniformity than that against the gradient norm stochasticity, suggesting that the directional statistics of minibatch gradients is a major factor behind SGD.

## item_id: m_0847

TITLE: Self-training For Few-shot Transfer Across Extreme Task Differences

ABSTRACT: Most few-shot learning techniques are pre-trained on a large, labeled “base dataset”. In problem domains where such large labeled datasets are not available for pre-training (e.g., X-ray, satellite images), one must resort to pre-training in a different “source” problem domain (e.g., ImageNet), which can be very different from the desired target task. Traditional few-shot and transfer learning techniques fail in the presence of such extreme differences between the source and target tasks. In this paper, we present a simple and effective solution to tackle this extreme domain gap: self-training a source domain representation on unlabeled data from the target domain. We show that this improves one-shot performance on the target domain by 2.9 points on average on the challenging BSCD-FSL benchmark consisting of datasets from multiple domains.

## item_id: m_0848

TITLE: LoRA Unleashed: Effortlessly Advancing from Low to Arbitrary Rank

ABSTRACT: Low-Rank Adaptation (LoRA) has emerged as a prominent technique for fine-tuning large foundation models, facilitating a reduction in trainable parameters through the utilization of low-rank matrices to represent weight changes $\mathbf{A}$ and $\mathbf{B}$ (\textit{i.e.,} $\Delta \mathbf{W} = \mathbf{B} \mathbf{A}$). Although LoRA has demonstrated considerable success, its expressiveness is inherently limited by the constrained capacity of its low-rank structure. To ameliorate this limitation, we introduce \underline{Fo}urier-based Flexible \underline{R}ank \underline{A}daptation (FoRA), which harnesses the robust expressiveness of the Fourier basis to re-parameterize $\mathbf{A}$ and $\mathbf{B}$ from a sparse spectral subspace. Utilizing FoRA, adaptation matrices can overcome conventional rank limitations, achieving up to a 15x reduction in the parameter budget. We illustrate that FoRA achieves an optimal balance of efficiency and performance across various tasks, including natural language understanding,  mathematical reasoning, commonsense reasoning, and image classification. Our codes are available at https://anonymous.4open.science/r/FoRA-0E9C.

## item_id: m_0849

TITLE: Unsupervised Image Decomposition with Phase-Correlation Networks

ABSTRACT: The ability to decompose scenes into their object components is a desired property for autonomous agents, allowing them to reason and act in their surroundings.
Recently, different methods have been proposed to learn object-centric representations from data in an unsupervised manner. These methods often rely on latent
representations learned by deep neural networks, hence requiring high computational costs and large amounts of curated data. Such models are also difficult to
interpret. To address these challenges, we propose the Phase-Correlation Decomposition Network (PCDNet), a novel model that decomposes a scene into its object
components, which are represented as transformed versions of a set of learned object prototypes. The core building block in PCDNet is the Phase-Correlation Cell
(PC Cell), which exploits the frequency-domain representation of the images in order to estimate the transformation between an object prototype and its 
transformed version in the image. In our experiments, we show how PCDNet outperforms state-of-the-art methods for unsupervised object discovery and 
segmentation on simple benchmark datasets and on more challenging data, while using a small number of learnable parameters and being fully interpretable.


## item_id: m_0850

TITLE: Solving Imperfect-Recall Games via Sum-of-Squares Optimization

ABSTRACT: Extensive-form games (EFGs) provide a powerful framework for modeling sequential decision making, capturing strategic interaction under imperfect information, chance events, and temporal structure. Most positive algorithmic and theoretical results for EFGs assume perfect recall, where players remember all past information and actions. We study the increasingly relevant setting of imperfect-recall EFGs (IREFGs), where players may forget parts of their history or previously acquired information, and where equilibrium computation is provably hard. We propose sum-of-squares (SOS) hierarchies for computing ex-ante optimal strategies in single-player IREFGs and Nash equilibria in multi-player IREFGs, working over behavioral strategies. Our theoretical results show that (i) these hierarchies converge asymptotically, (ii) under genericity assumptions, the convergence is finite, and (iii) in single-player non-absentminded IREFGs, convergence occurs at a finite level determined by the number of information sets. Finally, we introduce the new classes of (SOS)-concave and (SOS)-monotone IREFGs, and show that in the single-player setting the SOS hierarchy converges at the first level, enabling equilibrium computation with a single semidefinite program (SDP).

## item_id: m_0851

TITLE: Later Span Adaptation for Language Understanding

ABSTRACT: Pre-trained contextualized language models (PrLMs) broadly use fine-grained tokens (words or sub-words) as minimal linguistic unit in pre-training phase. Introducing span-level information in pre-training has shown capable of further enhancing PrLMs. However, such methods require enormous resources and are lack of adaptivity due to huge computational requirement from pre-training. Instead of too early fixing the linguistic unit  input as nearly all previous work did, we propose a novel method that combines span-level information into the representations generated by PrLMs during fine-tuning phase for better flexibility. In this way, the modeling procedure of span-level texts can be more adaptive to different downstream tasks. In detail, we divide the sentence into several spans according to the segmentation generated by a pre-sampled dictionary. Based on the sub-token-level representation provided by PrLMs, we enhance the connection between the tokens in each span and gain a representation with enhanced span-level information. Experiments are conducted on GLUE benchmark and prove that our approach could remarkably enhance the performance of PrLMs in various natural language understanding tasks.

## item_id: m_0852

TITLE: Extrapolation and learning equations

ABSTRACT: In classical machine learning, regression is treated as a black box process of identifying a
suitable function from a hypothesis set without attempting to gain insight into the mechanism connecting inputs and  outputs.
In the natural sciences, however, finding an interpretable function for a phenomenon is the prime goal as it allows to understand and  generalize results. This paper proposes a novel type of function learning network, called equation learner (EQL), that can learn analytical expressions and is able to extrapolate to unseen domains. It is implemented as an end-to-end differentiable feed-forward network and allows for efficient gradient based training. Due to sparsity regularization concise interpretable expressions can be obtained. Often the true underlying source expression is identified.


## item_id: m_0853

TITLE: ENRICHMENT OF FEATURES FOR CLASSIFICATION USING AN OPTIMIZED LINEAR/NON-LINEAR COMBINATION OF INPUT FEATURES

ABSTRACT: Automatic classification of objects is one of the most important tasks in engineering
and data mining applications. Although using more complex and advanced
classifiers can help to improve the accuracy of classification systems, it can be
done by analyzing data sets and their features for a particular problem. Feature
combination is the one which can improve the quality of the features. In this paper,
a structure similar to Feed-Forward Neural Network (FFNN) is used to generate an
optimized linear or non-linear combination of features for classification. Genetic
Algorithm (GA) is applied to update weights and biases. Since nature of data sets
and their features impact on the effectiveness of combination and classification
system, linear and non-linear activation functions (or transfer function) are used
to achieve more reliable system. Experiments of several UCI data sets and using
minimum distance classifier as a simple classifier indicate that proposed linear and
non-linear intelligent FFNN-based feature combination can present more reliable
and promising results. By using such a feature combination method, there is no
need to use more powerful and complex classifier anymore.

## item_id: m_0854

TITLE: Doubly Sparse: Sparse Mixture of Sparse Experts for Efficient Softmax Inference

ABSTRACT: Computations for the softmax function in neural network models are expensive when the number of output classes is large. This can become a significant issue in both training and inference for such models. In this paper, we present Doubly Sparse Softmax (DS-Softmax), Sparse Mixture of Sparse of Sparse Experts, to improve the efficiency for softmax inference. During training, our method learns a two-level class hierarchy by dividing entire output class space into several partially overlapping experts. Each expert is responsible for a learned subset of the output class space and each output class only belongs to a small number of those experts. During inference, our method quickly locates the most probable expert to compute small-scale softmax. Our method is learning-based and requires no knowledge of the output class partition space a priori. We empirically evaluate our method on several real-world tasks and demonstrate that we can achieve significant computation reductions without loss of performance.

## item_id: m_0855

TITLE: Long-term planning, short-term adjustments

ABSTRACT: Deep Reinforcement Learning (RL) algorithms can learn complex policies to optimize
agent operation over time. RL algorithms have shown promising results
in solving complicated problems in recent years. However, their application on
real-world physical systems remains limited. Despite the advancements in RL
algorithms, the industries often prefer traditional control strategies. Traditional
methods are simple, computationally efficient and easy to adjust. In this paper,
we propose a new Q-learning algorithm for continuous action space, which can
bridge the control and RL algorithms and bring us the best of both worlds. Our
method can learn complex policies to achieve long-term goals and at the same time
it can be easily adjusted to address short-term requirements without retraining.
We achieve this by modeling both short-term and long-term prediction models.
The short-term prediction model represents the estimation of the system dynamic
while the long-term prediction model represents the Q-value. The case studies
demonstrate that our proposed method can achieve short-term and long-term goals
without complex reward functions.

## item_id: m_0856

TITLE: Wicked Oddities: Selectively Poisoning for Effective Clean-Label Backdoor Attacks

ABSTRACT: Deep neural networks are vulnerable to backdoor attacks, a type of adversarial attack that poisons the training data to manipulate the behavior of models trained on such data. 
Clean-label backdoor is a more stealthy form of backdoor attacks that can perform the attack without changing the labels of poisoned data.
Early works on clean-label attacks added triggers to a random subset of the training set, ignoring the fact that samples contribute unequally to the attack's success. This results in high poisoning rates and low attack success rates.
To alleviate the problem, several supervised learning-based sample selection strategies have been proposed.
However, these methods assume access to the entire labeled training set and require training, which is expensive and may not always be practical.
This work studies a new and more practical (but also more challenging) threat model where the attacker only provides data for the target class (e.g., in face recognition systems) and has no knowledge of the victim model or any other classes in the training set.
We study different strategies for selectively poisoning a small set of training samples in the target class to boost the attack success rate in this setting. 
Our threat model poses a serious threat in training machine learning models with third-party datasets, since the attack can be performed effectively with limited information. Experiments on benchmark datasets illustrate the effectiveness of our strategies in improving clean-label backdoor attacks.

## item_id: m_0857

TITLE: PDE-Net: Learning PDEs from Data

ABSTRACT: Partial differential equations (PDEs)  play a prominent role in many disciplines such as applied mathematics, physics, chemistry, material science, computer science, etc. PDEs are commonly derived based on physical laws or empirical observations. However, the governing equations for many complex systems in modern applications are still not fully known. With the rapid development of sensors, computational power, and data storage in the past decade, huge quantities of data can be easily collected and efficiently stored. Such vast quantity of data offers new opportunities for data-driven discovery of hidden physical laws. Inspired by the latest development of neural network designs in deep learning, we propose a new feed-forward deep network, called PDE-Net, to fulfill two objectives at the same time: to accurately predict dynamics of complex systems and to uncover the underlying hidden PDE models. The basic idea of the proposed PDE-Net is to learn differential operators by learning convolution kernels (filters), and apply neural networks or other machine learning methods to approximate the unknown nonlinear responses. Comparing with existing approaches, which either assume the form of the nonlinear response is known or fix certain finite difference approximations of differential operators, our approach has the most flexibility by learning both differential operators and the nonlinear responses. A special feature of the proposed PDE-Net is that all filters are properly constrained, which enables us to easily identify the governing PDE models while still maintaining the expressive and predictive power of the network. These constrains are carefully designed by fully exploiting the relation between the orders of differential operators and the orders of sum rules of filters (an important concept originated from wavelet theory). We also discuss relations of the PDE-Net with some existing networks in computer vision such as Network-In-Network (NIN) and Residual Neural Network (ResNet). Numerical experiments show that the PDE-Net has the potential to uncover the hidden PDE of the observed dynamics, and predict the dynamical behavior for a relatively long time, even in a noisy environment.

## item_id: m_0858

TITLE: Image Score: how to select useful samples

ABSTRACT: There has long been debates on how we could interpret neural networks and understand the decisions our models make. Specifically, why deep neural networks tend to be error-prone when dealing with samples that output low softmax scores. We present an efficient approach to measure the confidence of decision-making steps by statistically investigating each unit's contribution to that decision. Instead of focusing on how the models react on datasets, we study the datasets themselves given a pre-trained model. Our approach is capable of assigning a score to each sample within a dataset that measures the frequency of occurrence of that sample's chain of activation. We demonstrate with experiments that our method could select useful samples to improve deep neural networks in a semi-supervised leaning setting.

## item_id: m_0859

TITLE: Local SGD Meets Asynchrony

ABSTRACT: Distributed variants of stochastic gradient descent (SGD) are central to training deep neural networks on massive datasets. 
Several scalable versions of data-parallel  SGD have been developed, leveraging asynchrony, communication-compression, and local gradient steps. Current research seeks a balance between distributed scalability--seeking to minimize the amount of synchronization needed--and generalization performance--seeking to achieve the same or better accuracy relative to the sequential baseline. However, a key issue in this regime is largely unaddressed: if ``local" data-parallelism is aggressively applied to better utilize the computing resources available with workers, generalization performance of the trained model degrades. 

In this paper, we present a method to improve the "local scalability" of decentralized SGD. In particular, we propose two key techniques: (a) shared-memory based asynchronous gradient updates at decentralized workers keeping the local minibatch size small, and (b) an asynchronous non-blocking in-place averaging overlapping the local updates, thus essentially utilizing all compute resources at all times without the need for large minibatches. Empirically, the additional noise introduced in the procedure proves to be a boon for better generalization. On the theoretical side, we show that this method guarantees ergodic convergence for non-convex objectives, and achieves the classic sublinear rate under standard assumptions. 
On the practical side, we show that it improves upon the performance of local SGD and related schemes, without compromising accuracy. 

## item_id: m_0860

TITLE: Deep k-NN for Noisy Labels

ABSTRACT: Modern machine learning models are often trained on examples with noisy labels that hurt performance and are hard to identify. In this paper, we provide an empirical study showing that a simple $k$-nearest neighbor-based filtering approach on the logit layer of a preliminary model can  remove mislabeled training data and produce more accurate models than some recently proposed methods. We also provide new statistical guarantees into its efficacy.

## item_id: m_0861

TITLE: Implicit Causal Models for Genome-wide Association Studies

ABSTRACT: Progress in probabilistic generative models has accelerated, developing richer models with neural architectures, implicit densities, and with scalable algorithms for their Bayesian inference. However, there has been limited progress in models that capture causal relationships, for example, how individual genetic factors cause major human diseases. In this work, we focus on two challenges in particular: How do we build richer causal models, which can capture highly nonlinear relationships and interactions between multiple causes? How do we adjust for latent confounders, which are variables influencing both cause and effect and which prevent learning of causal relationships? To address these challenges, we synthesize ideas from causality and modern probabilistic modeling. For the first, we describe implicit causal models, a class of causal models that leverages neural architectures with an implicit density. For the second, we describe an implicit causal model that adjusts for confounders by sharing strength across examples. In experiments, we scale Bayesian inference on up to a billion genetic measurements. We achieve state of the art accuracy for identifying causal factors: we significantly outperform the second best result by an absolute difference of 15-45.3%.

## item_id: m_0862

TITLE: InfoCLIP++: A Multimodal Learning Framework with Multi-Granular Information-Theoretic Alignment and Adaptive Fusion

ABSTRACT: Multimodal foundation models such as CLIP have significantly advanced vision-language understanding yet face persistent challenges including coarse semantic alignment, high computational overhead, and sensitivity to noisy inputs. This paper introduces \textit{InfoCLIP++}, an integrated framework addressing these limitations through three synergistic components: multi-granular alignment using constrained optimal transport for pixel-level details and Random-Feature HGR correlation for patch-level and global semantics, differentiable adaptive routing for token and modality pruning via entropy-gradient criteria, and hardware-aware optimization with quantized random feature projections for efficient deployment. The model is trained end-to-end with a composite objective combining alignment losses, contrastive learning, and sparsity regularization. Extensive evaluations demonstrate consistent and significant improvements: 84.3\% zero-shot accuracy on ImageNet-1K, representing an 8.1\% gain over CLIP, 74.5\% R@1 on COCO cross-modal retrieval with a 16.1\% improvement, and a Noise Robustness Score of 0.90 on ImageNet-C. Computationally, InfoCLIP++ reduces FLOPs by 87\% and achieves a 6.8$\times$ speedup on FPGA platforms, establishing it as an efficient and robust foundation for resource-constrained multimodal intelligence.

## item_id: m_0863

TITLE: HELMET: How to Evaluate Long-context Models Effectively and Thoroughly

ABSTRACT: Many benchmarks exist for evaluating long-context language models (LCLMs), yet developers often rely on synthetic tasks such as needle-in-a-haystack (NIAH) or an arbitrary subset of tasks. However, it remains unclear whether these benchmarks reflect the diverse downstream applications of LCLMs, and such inconsistencies further complicate model comparison. We investigate the underlying reasons behind these practices and find that existing benchmarks often provide noisy signals due to limited coverage of applications, insufficient context lengths, unreliable metrics, and incompatibility with base models. In this work, we introduce HELMET (How to Evaluate Long-context Models Effectively and Thoroughly), a comprehensive benchmark encompassing seven diverse, application-centric categories. We also address several issues in previous benchmarks by adding controllable lengths up to 128K tokens, model-based evaluation for reliable metrics, and few-shot prompting for robustly evaluating base models. Consequently, we demonstrate that HELMET offers more reliable and consistent rankings of frontier LCLMs. Through a comprehensive study of 59 LCLMs, we find that (1) synthetic tasks like NIAH do not reliably predict downstream performance; (2) the diverse categories in HELMET exhibit distinct trends and low correlations with each other; and (3) while most LCLMs achieve perfect NIAH scores, open-source models significantly lag behind closed ones when tasks require full-context reasoning or following complex instructions---the gap widens as length increases. Finally, we recommend using our RAG tasks for fast model development, as they are easy to run and better predict other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.

## item_id: m_0864

TITLE: DNN Representations as Codewords: Manipulating Statistical Properties via Penalty Regularization

ABSTRACT: Performance of Deep Neural Network (DNN) heavily depends on the characteristics of hidden layer representations. Unlike the codewords of channel coding, however, the representations of learning cannot be directly designed or controlled. Therefore, we develop a family of penalty regularizers where each one aims to affect one of representation's statistical properties such as sparsity, variance, or covariance. The regularizers are extended to perform class-wise regularization, and the extension is found to provide an outstanding shaping capability. A variety of statistical properties are investigated for 10 different regularization strategies including dropout and batch normalization, and several interesting findings are reported. Using the family of regularizers, performance improvements are confirmed for MNIST, CIFAR-100, and CIFAR-10 classification problems. But more importantly, our results suggest that understanding how to manipulate statistical properties of representations can be an important step toward understanding DNN and that the role and effect of DNN regularizers need to be reconsidered.

## item_id: m_0865

TITLE: Recurrent Neural Networks for Multivariate Time Series with Missing Values

ABSTRACT: Multivariate time series data in practical applications, such as health care, geoscience, and biology, are characterized by a variety of missing values. In time series prediction and other related tasks, it has been noted that missing values and their missing patterns are often correlated with the target labels, a.k.a., informative missingness. There is very limited work on exploiting the missing patterns for effective imputation and improving prediction performance. In this paper, we develop novel deep learning models, namely GRU-D, as one of the early attempts. GRU-D is based on Gated Recurrent Units (GRU), a state-of-the-art recurrent neural network. It takes two representations of missing patterns, i.e., masking and time interval, and effectively incorporates them into a deep model architecture so that it not only captures the long-term temporal dependencies in time series, but also utilizes the missing patterns to achieve better prediction results. Experiments of time series classification tasks on real-world clinical datasets (MIMIC-III, PhysioNet) and synthetic datasets demonstrate that our models achieve state-of-the-art performance and provides useful insights for better understanding and utilization of missing values in time series analysis.

## item_id: m_0866

TITLE: Deep Multiple Instance Learning for Taxonomic Classification of Metagenomic read sets

ABSTRACT: Metagenomic studies have increasingly utilized sequencing technologies in order to analyze DNA fragments found in environmental samples. It can provide useful insights for studying the interactions between hosts and microbes, infectious disease proliferation, and novel species discovery. One important step in this analysis is the taxonomic classification of those DNA fragments. Of particular interest is the determination of the distribution of the taxa of microbes in metagenomic samples. Recent attempts using deep learning focus on architectures that classify single DNA reads independently from each other. In this work, we attempt to solve the task of directly predicting the distribution over the taxa of whole metagenomic read sets. We formulate this task as a Multiple Instance Learning (MIL) problem. We extend architectures used in single-read taxonomic classification with two different types of permutation-invariant MIL pooling layers: a) deepsets and b) attention-based pooling. We illustrate that our architecture can exploit the co-occurrence of species in metagenomic read sets and outperforms the single-read architectures in predicting the distribution over the taxa at higher taxonomic ranks.

## item_id: m_0867

TITLE: Error Broadcast and Decorrelation as a Potential Artificial and Natural Learning Mechanism

ABSTRACT: We introduce the Error Broadcast and Decorrelation (EBD) algorithm, a novel learning framework that addresses the credit assignment problem in neural networks by directly broadcasting output error to individual layers. The EBD algorithm leverages the orthogonality property of the optimal minimum mean square error (MMSE) estimator, which states that estimation errors are orthogonal to any nonlinear function of the input, specifically the activations of each layer. By defining layerwise loss functions that penalize correlations between these activations and output errors, the EBD method offers a principled and efficient approach to error broadcasting. This direct error transmission eliminates the need for weight transport inherent in backpropagation. Additionally, the optimization framework of the EBD algorithm naturally leads to the emergence of the experimentally observed three-factor learning rule. We further demonstrate how EBD can be integrated with other biologically plausible learning frameworks, transforming time-contrastive approaches into single-phase, non-contrastive forms, thereby enhancing biological plausibility and performance. Numerical experiments demonstrate that EBD achieves performance comparable to or better than known error-broadcast methods on benchmark datasets. The scalability of algorithmic extensions of EBD to very large or complex datasets remains to be explored. However, our findings suggest that EBD offers a promising, principled direction for both artificial and natural learning paradigms, providing a biologically plausible and flexible alternative for neural network training  with inherent simplicity and adaptability that could benefit future developments in neural network technologies.

## item_id: m_0868

TITLE: The Gaussian-Multinoulli Restricted Boltzmann Machine: A Potts Model Extension of the GRBM

ABSTRACT: Many real-world tasks, from associative memory to symbolic reasoning, benefit from discrete, structured representations that standard continuous latent models can struggle to express. We introduce the Gaussian–Multinoulli Restricted Boltzmann Machine (GM-RBM), a generative energy-based model that extends the Gaussian–Bernoulli RBM (GB-RBM) by replacing binary hidden units with $q$-state categorical (Potts) units, yielding a richer latent state space for multivalued concepts. We provide a self-contained derivation of the energy, conditional distributions, and learning rules, and detail practical training choices (contrastive divergence with temperature annealing and intra-slot diversity constraints) that avoid state collapse. To separate architectural effects from sheer latent capacity, we evaluate under both capacity-matched and parameter-matched setups, comparing GM-RBM with GB-RBM configured to have the same number of possible latent assignments. On analogical recall and structured memory benchmarks, GM-RBM achieves competitive, and in several regimes, improved recall at equal capacity with comparable training cost, despite using only Gibbs updates. The discrete $q$-ary formulation is also amenable to efficient implementation. These results clarify when categorical hidden units provide a simple, scalable alternative to binary latents for discrete inference within tractable RBMs.

## item_id: m_0869

TITLE: Hypothetical Training for Robust Machine Reading Comprehension of Tabular Context

ABSTRACT: Machine Reading Comprehension (MRC) models easily learn the spurious correlations from complex context such as tabular data. Counterfactual training—using the original and augmented data—has become a promising solution. However, it is costly to construct faithful counterfactual examples because it is tricky to maintain the consistency and dependency of the table entries. In this paper, we take a more economic fashion to ask hypothetical questions, e.g., “in which year would the net profit be larger if the revenue in 2019 were $38,298?”, whose effects on the answers are equivalent to those expensive counterfactual tables. We propose a hypothetical training framework that uses pairs of examples with different hypothetical questions to supervise the direction of model gradient w.r.t. the input towards the answer change. We conduct experiments on MRC datasets with factual and hypothetical examples. Performance gain on a newly constructed stress test validates the effectiveness and rationality of our approach.

## item_id: m_0870

TITLE: The wisdom of the crowd: reliable deep reinforcement learning through ensembles of Q-functions

ABSTRACT: Reinforcement learning agents learn by exploring the environment and then exploiting what they have learned.
This frees the human trainers from having to know the preferred action or intrinsic value of each encountered state.
The cost of this freedom is reinforcement learning is slower and more unstable than supervised learning.
We explore the possibility that ensemble methods can remedy these shortcomings and do so by investigating a novel technique which harnesses the wisdom of the crowds by bagging Q-function approximator estimates.

Our results show that this proposed approach improves all three tasks and reinforcement learning approaches attempted.
We are able to demonstrate that this is a direct result of the increased stability of the action portion of the state-action-value function used by Q-learning to select actions and by policy gradient methods to train the policy.


## item_id: m_0871

TITLE: Neural Representations in Multi-Task Learning guided by Task-Dependent Contexts

ABSTRACT: The ability to switch between tasks effectively in response to external stimuli is a hallmark of cognitive control. Our brain is able to filter and to integrate external information to accomplish goal-directed behavior. Task switching occurs rapidly and efficiently, allowing us to perform multiple tasks with ease. In a similar way, deep learning models can be tailored to exhibit multi-task capabilities and achieve high performance across domains. Still, understanding how neural networks make predictions is crucial in many real-world applications.

In this study, we delve into neural representations learned by multi-tasking architectures. Concretely, we compare individual and parallel networks with task switching networks. Task-switching networks leverage task-dependent contexts to learn disentangled representations without hurting the overall task accuracy. We show that task-switching networks operate in an intermediate regime between individual and parallel. In addition, we show that shared representations are produced by the emergence neurons encoding multiple tasks. Furthermore, we study the role of contexts across network processing and show its role at aligning the task with the relevant features. Finally, we investigate how the magnitude of contexts affects the performance in task-switching networks.

## item_id: m_0872

TITLE: Message Passing Neural PDE Solvers

ABSTRACT: The numerical solution of partial differential equations (PDEs) is difficult, having led to a century of research so far. Recently, there have been pushes to build neural--numerical hybrid solvers, which piggy-backs the modern trend towards fully end-to-end learned systems. Most works so far can only generalize over a subset of properties to which a generic solver would be faced, including: resolution, topology, geometry, boundary conditions, domain discretization regularity, dimensionality, etc. In this work, we build a solver, satisfying these properties, where all the components are based on neural message passing, replacing all heuristically designed components in the computation graph with backprop-optimized neural function approximators. We show that neural message passing solvers representationally contain some classical methods, such as finite differences, finite volumes, and WENO schemes. In order to encourage stability in training autoregressive models, we put forward a method that is based on the principle of zero-stability, posing stability as a domain adaptation problem. We validate our method on various fluid-like flow problems, demonstrating fast, stable, and accurate performance across different domain topologies, discretization, etc. in 1D and 2D. Our model outperforms state-of-the-art numerical solvers in the low resolution regime in terms of speed, and accuracy.

## item_id: m_0873

TITLE: Boosting Fast and High-Quality Speech Synthesis with Linear Diffusion

ABSTRACT: Denoising diffusion probabilistic models have shown extraordinary ability on various generative tasks. However, their slow inference speed renders them impractical in speech synthesis. This paper proposes a linear diffusion model (LinDiff) based on an ordinary differential equation to simultaneously reach fast inference and high sample quality. We employs linear interpolation between the target and noise to design a diffusion sequence for training, while previously the diffusion path that links the noise and target is a curved segment. When we decrease the number of sampling steps (i.e., the number of line segments used to fit the path), the ease of fitting straight lines compared to curves allows us to generate higher quality samples from a random noise with fewer iterations. To reduce computational complexity and achieve effective global modeling of noisy speech, LinDiff employs a patch-based processing approach that partitions the input signal into small patches. The patch-wise token leverages transformer architecture for effective modeling of global information. Additionally, the model seamlessly integrates the strengths of both transformer and convolutional neural networks by utilizing a post-convolution module for fine-grained detail restoration. Adversarial training is further used to improve the sample quality with decreased sampling steps. We test this model on speech synthesis conditioned on acoustic feature (Mel-spectrograms). Experimental results verify that our model can synthesize high-quality speech even with only one diffusion step. Both subjective and objective evaluations demonstrate that our model can synthesize speech of a quality comparable to that of autoregressive models with faster synthesis speed.

## item_id: m_0874

TITLE: PGASL: Predictive and Generative Adversarial Semi-supervised Learning for imbalanced data

ABSTRACT: Modern machine learning techniques often suffer from class imbalance where only a small amount of data is available for minority classes. Classifiers trained on an imbalanced dataset, although have high accuracy on majority classes, can perform poorly on minority classes. This is problematic when minority classes are also important. Generative Adversarial Networks (GANs) have been proposed for generating artificial minority examples to balance the training. We propose a class-imbalanced semi-supervised learning algorithm PGASL which can be efficiently trained on unlabeled and class-imbalanced data. In this work, we use a predictive network which is trained adversarially for the discriminator to correct predictions on the unlabeled dataset. Experiments on text datasets show that PGASL outperforms state-of-the-art class-imbalanced learning algorithms by including both predictive network and generator. 


## item_id: m_0875

TITLE: Cross-Domain Few-Shot Relation Extraction via Representation Learning and Domain Adaptation

ABSTRACT: Few-shot relation extraction aims to recognize novel relations with few labeled sentences in each relation. Previous metric-based few-shot relation extraction methods classify by comparing the embeddings of query sentence embedding with those prototypes generated by the few labeled sentences embedding using a learned metric function. However, the generalization ability of these methods on unseen relations in different domains is limited, since these domains always have significant discrepancies from those in the training dataset. Because the prototype is essential for extracting relations between entities in the latent space. To extract new relations in various domains more effectively, we propose to learn more interpretable and robust prototypes by learning from prior knowledge and intrinsic semantics of relations. We improve the prototype representation of relations more efficiently by using prior knowledge to explore the connections between relations. The geometric interpretability of the prototype is improved by making the classification margins between sentence embedding clearer through contrastive learning. Besides, for better-extracting relations in different domains, using a cross-domain approach makes the generation process of the prototype take into account the gap between other domains, which makes the prototype more robust. The experimental results on the benchmark FewRel dataset demonstrate the advantages of the proposed method over some state-of-the-art methods.

## item_id: m_0876

TITLE: A Computation and Communication Efficient Projection-free Algorithm for Decentralized Constrained Optimization

ABSTRACT: Decentralized constrained optimization problems arise in numerous real-world applications, where a major challenge lies in the computational complexity of projecting onto complex sets, especially in large-scale systems. 
The projection-free method, Frank-Wolfe (FW), is popular for the constrained optimization problem with complex sets due to its efficiency in tackling the projection process. 
However, when applying FW methods to decentralized constrained finite-sum optimization problems, previous studies provide suboptimal incremental first-order oracle (IFO) bounds in both convex and non-convex settings. 
In this paper, we propose a stochastic algorithm named Decentralized Variance Reduction Gradient Tracking Frank-Wolfe ($\texttt{DVRGTFW}$), which incorporates the techniques of variance reduction, gradient tracking, and multi-consensus in the FW update to obtain tight bounds. 
We present a novel convergence analysis, diverging from previous decentralized FW methods, and demonstrating $\tilde{\mathcal{O}}(n+\sqrt{\frac{n}{m}}L\varepsilon^{-1})$ and $\mathcal{O}(\sqrt{\frac{n}{m}}L^2\varepsilon^{-2})$ IFO complexity bounds in convex and non-convex settings, respectively. 
To the best of our knowledge, these bounds are the best achieved in the literature to date. Besides, in the non-convex case, $\texttt{DVRGTFW}$ achieves $\mathcal{O}(\frac{L^2\varepsilon^{-2}}{\sqrt{1-\lambda_2(W)}})$ communication complexity which is closed to the lower bound $\Omega(\frac{L\varepsilon^{-2}}{\sqrt{1-\lambda_2(W)}})$. 
Empirical results validate the convergence properties of $\texttt{DVRGTFW}$ and highlight its superior performance over other related methods.

## item_id: m_0877

TITLE: Lyapunov-based Safe Policy Optimization

ABSTRACT: In many reinforcement learning applications, it is crucial that the agent interacts with the environment only through safe policies, i.e.,~policies that do not take the agent to certain undesirable situations. These problems are often formulated as a constrained Markov decision process (CMDP) in which the agent's goal is to optimize its main objective while not violating a number of safety constraints. In this paper, we propose safe policy optimization algorithms that are based on the Lyapunov approach to CMDPs, an approach that has well-established theoretical guarantees in control engineering. We first show how to generate a set of state-dependent Lyapunov constraints from the original CMDP safety constraints. We then propose safe policy gradient algorithms that train a neural network policy using DDPG or PPO, while guaranteeing near-constraint satisfaction at every policy update by projecting either the policy parameter or the action onto the set of feasible solutions induced by the linearized Lyapunov constraints. Unlike the existing (safe) constrained PG algorithms, ours are more data efficient as they are able to utilize both on-policy and off-policy data. Furthermore, the action-projection version of our algorithms often leads to less conservative policy updates and allows for natural integration into an end-to-end PG training pipeline. We evaluate our algorithms and compare them with CPO and the Lagrangian method on several high-dimensional continuous state and action simulated robot locomotion tasks, in which the agent must satisfy certain safety constraints while minimizing its expected cumulative cost. 

## item_id: m_0878

TITLE: CLAS: Central Latent Action Spaces for Coordinated Multi-Robot Manipulation

ABSTRACT: Multi-robot manipulation tasks involve various control entities that can be separated into dynamically independent parts. A typical example of such real-world tasks is dual-arm manipulation. Learning to naively solve such tasks with reinforcement learning is often unfeasible due to the combinatorial explosion of the action and state spaces. Instead, we would like to handle such environments as multi-agent systems and have several agents control parts of the whole. However, decentralizing the generation of actions requires coordination across agents through a channel limited to information central to the task. This paper proposes an approach to coordinating multi-robot manipulation through learned latent action spaces that are shared across different agents. We validate our method in simulated multi-robot manipulation tasks and demonstrate improvement over previous baselines in terms of sample efficiency, learning performance, and interpretability.

## item_id: m_0879

TITLE: Scaling Multi-Task Bayesian Optimization with Large Language Models

ABSTRACT: In multi-task Bayesian optimization, the goal is to leverage experience from optimizing existing tasks to improve the efficiency of optimizing new ones. While approaches using multi-task Gaussian processes or deep kernel transfer exist, the performance improvement is marginal when scaling beyond a moderate number of tasks. We introduce **BOLT**, an initialization-only transfer strategy that distills prior BO runs into an LLM which proposes candidates for new tasks, while the surrogate at test time remains single-task. The LLM is periodically fine-tuned on top solutions from completed runs, creating a closed loop where better BO outputs yield better initializations over time. This decoupled design scales to roughly 1500 tasks without the saturation observed for shared-surrogate MTBO and adds only a small, amortized overhead relative to the BO inner loops. We evaluate on two domains: database query optimization and antimicrobial peptide design. We demonstrate that LLM-generated initializations steadily improve and accelerate BO, and with sufficient fine-tuning, a few LLM samples often match or surpass full ''from-scratch'' BO with far fewer oracle calls.

## item_id: m_0880

TITLE: Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction

ABSTRACT: Despite recent progress in Retrieval-Augmented Generation (RAG) achieved by large language models (LLMs), retrievers often recall uncorrelated documents, regarded as "noise" during subsequent text generation. To address this, some methods train LLMs to distinguish between relevant and irrelevant documents using labeled data, enabling them to select the most likely relevant ones as context. However, they remain sensitive to noise, as LLMs can easily make mistakes when the selected document is noisy. Some approaches increase the number of referenced documents and train LLMs to perform stepwise reasoning when presented with multiple documents. Unfortunately, these methods rely on extensive and diverse annotations to ensure generalization, which is both challenging and costly. In this paper, we propose **Backtracking Correction** to address these limitations. Specifically, we reformulate stepwise RAG into a multi-step decision-making process. Starting from the final step, we optimize the model through error sampling and self-correction, and then backtrack to the previous state iteratively. In this way, the model's learning scheme follows an easy-to-hard progression: as the target state moves forward, the context space decreases while the decision space increases. Experimental results demonstrate that **Backtracking Correction** enhances LLMs' ability to make complex multi-step assessments, improving the robustness of RAG in dealing with noisy documents.

## item_id: m_0881

TITLE: SCHEME: Scalable Channel Mixer for Vision Transformers

ABSTRACT: Vision Transformers have received significant attention due to their impressive performance in many vision tasks. While the token mixer or attention block has been studied in great detail, the channel mixer or feature mixing block (FFN or MLP) has not been explored in depth albeit it accounts for a bulk of the parameters and computation in a model. In this work, we study whether sparse feature mixing can replace the dense connections and confirm this with a block diagonal MLP structure that improves the accuracy by supporting larger expansion ratios. To improve the feature clusters formed by this structure and thereby further improve the accuracy, a lightweight, parameter-free, channel covariance attention (CCA) mechanism is introduced as a parallel branch during training. This design of CCA enables gradual feature mixing across channel groups during training whose contribution decays to zero as the training progresses to convergence. This allows the CCA block to be discarded during inference, thus enabling enhanced performance with no additional computational cost. The resulting $\textit{Scalable CHannEl MixEr}$ (SCHEME) can be plugged into any ViT architecture to obtain a gamut of models with different trade-offs between complexity and performance by controlling the block diagonal structure size in the MLP. This is shown by the introduction of a new family of SCHEMEformer models. Experiments on image classification, object detection, and semantic segmentation, with different ViT backbones, consistently demonstrate substantial accuracy gains over existing designs, especially under lower FLOPs regimes. The SCHEMEformer family is shown to establish new Pareto frontiers for accuracy vs FLOPS, accuracy vs model size, and accuracy vs throughput, especially for fast transformers of small model size.

## item_id: m_0882

TITLE: COMiX: Compositional explanations using prototypes

ABSTRACT: Aligning machine representations with human understanding is key to improving interpretability of machine learning (ML) models. 
When classifying a new image, humans often explain their decisions by decomposing the image into concepts and pointing to corresponding regions in familiar images.
Current ML explanation techniques typically either trace decision-making processes to reference prototypes, generate attribution maps highlighting feature importance, or incorporate intermediate bottlenecks designed to align with human-interpretable concepts.
The proposed method, named COMiX, classifies an image by decomposing it into regions based on learned concepts and tracing each region to corresponding ones in images from the training dataset, assuring that explanations fully represent the actual decision-making process. We dissect the test image into selected internal representations of a neural network to derive prototypical parts (primitives) and match them with the corresponding primitives derived from the training data. 
In a series of qualitative and quantitative experiments, we theoretically prove and demonstrate that our method, in contrast to \textit{post hoc} analysis, provides fidelity of explanations and shows that the efficiency is competitive with other inherently interpretable architectures. Notably, it shows substantial improvements in fidelity and sparsity metrics, including $48.82\%$ improvement in the C-insertion score on the ImageNet dataset over the best state-of-the-art baseline.

## item_id: m_0883

TITLE: Kernel Implicit Variational Inference

ABSTRACT: Recent progress in variational inference has paid much attention to the flexibility of variational posteriors. One promising direction is to use implicit distributions, i.e., distributions without tractable densities as the variational posterior. However, existing methods on implicit posteriors still face challenges of noisy estimation and computational infeasibility when applied to models with high-dimensional latent variables. In this paper, we present a new approach named Kernel Implicit Variational Inference that addresses these challenges. As far as we know, for the first time implicit variational inference is successfully applied to Bayesian neural networks, which shows promising results on both regression and classification tasks.

## item_id: m_0884

TITLE: Weighted Training for Cross-Task Learning

ABSTRACT: In this paper, we introduce Target-Aware Weighted Training (TAWT), a weighted training algorithm for cross-task learning based on minimizing a representation-based task distance between the source and target tasks. We show that TAWT is easy to implement, is computationally efficient, requires little hyperparameter tuning, and enjoys non-asymptotic learning-theoretic guarantees. The effectiveness of TAWT is corroborated through extensive experiments with BERT on four sequence tagging tasks in natural language processing (NLP), including part-of-speech (PoS) tagging, chunking, predicate detection, and named entity recognition (NER). As a byproduct, the proposed representation-based task distance allows one to reason in a theoretically principled way about several critical aspects of cross-task learning, such as the choice of the source data and the impact of fine-tuning.

## item_id: m_0885

TITLE: VALM: Variational Autoencoder Language Models for Highly Parallel Text Generation

ABSTRACT: Autoregressive language models have shown impressive abilities across domains. However, their token-by-token decoding limits inference speed. We introduce Variational Autoencoder Language Models (VALM), a non-autoregressive architecture that predicts entire sequences in parallel from a single global latent, with no denoising or diffusion losses. VALM uses a bidirectional transformer encoder and decoder with an ELBO objective, reducing sequential depth from $\mathcal{O}(LT)$ to $\mathcal{O}(L)$ for an $L$-layer network generating $T$ tokens. We train VALM-1, which generates 32 tokens in a single forward pass, demonstrating the applicability of pure VAEs to discrete text and presenting a novel approach to high-throughput language modeling on standard GPUs.

## item_id: m_0886

TITLE: On Meaning-Preserving Adversarial Perturbations for Sequence-to-Sequence Models

ABSTRACT: Adversarial examples have been shown to be an effective way of assessing the robustness of neural sequence-to-sequence (seq2seq) models, by applying perturbations to the input of a model leading to large degradation in performance. However, these perturbations are only indicative of a weakness in the model if they do not change the semantics of the input in a way that would change the expected output. Using the example of machine translation (MT), we propose a new evaluation framework for adversarial attacks on seq2seq models taking meaning preservation into account and demonstrate that existing methods may not preserve meaning in general. Based on these findings, we propose new constraints for attacks on word-based MT systems and show, via human and automatic evaluation, that they produce more semantically similar adversarial inputs. Furthermore, we show that performing adversarial training with meaning-preserving attacks is beneficial to the model in terms of adversarial robustness without hurting test performance.

## item_id: m_0887

TITLE: Offline Congestion Games: How Feedback Type Affects Data Coverage Requirement

ABSTRACT: This paper investigates when one can efficiently recover an approximate Nash Equilibrium (NE) in offline congestion games. The existing dataset coverage assumption in offline general-sum games inevitably incurs a dependency on the number of actions, which can be exponentially large in congestion games. We consider three different types of feedback with decreasing revealed information. Starting from the facility-level (a.k.a., semi-bandit) feedback, we propose a novel one-unit deviation coverage condition and show a pessimism-type algorithm that can recover an approximate NE. For the agent-level (a.k.a., bandit) feedback setting, interestingly, we show the one-unit deviation coverage condition is not sufficient. On the other hand, we convert the game to multi-agent linear bandits and show that with a generalized data coverage assumption in offline linear bandits, we can efficiently recover the approximate NE. Lastly, we consider a novel type of feedback, the game-level feedback where only the total reward from all agents is revealed. Again, we show the coverage assumption for the agent-level feedback setting is insufficient in the game-level feedback setting, and with a stronger version of the data coverage assumption for linear bandits, we can recover an approximate NE. Together, our results constitute the first study of offline congestion games and imply formal separations between different types of feedback.

## item_id: m_0888

TITLE: Aging with GRACE: Lifelong Model Editing with Key-Value Adaptors

ABSTRACT: Large language models often err during deployment, either due to non-representative training data or distribution shift in the test set. Recently, model editors have been proposed to fix errors by adjusting a pre-trained model's weights. So far, however, existing model editors fail when making sequential edits by quickly decaying a model's performance on its upstream data. Further, when editing deployed online models, they quickly forget how to fix previously-seen mistakes. We advance beyond these existing methods by proposing and studying a novel Lifelong Model Editing setting, where errors stream into a deployed model and we update the model to correct its predictions without influencing its predictions for unrelated inputs. Towards effective methods in this challenging setting, we propose with General Retrieval Adaptors for Continual Editing, or GRACE. GRACE is a new Key-Value framework that casts model editing as a codebook update problem. The proposed approach edits selected model layers by caching activations that are queried using embeddings from the previous layer. The cached activations are trained to correct a model's predictions, treating future layers as a decoder. As edits stream in, the keys and values of a GRACE layer are updated while the model weights remain frozen, ensuring similar edits are treated similarly without altering the model's performance on unrelated instances. Experimentally, we show that \method substantially improves over recent model editors.

## item_id: m_0889

TITLE: MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning

ABSTRACT: Low-rank adaptation (LoRA) is a popular parameter-efficient fine-tuning (PEFT) method for large language models (LLMs). In this paper, we analyze the impact of low-rank updating, as implemented in LoRA. Our findings suggest that the low-rank updating mechanism may limit the ability of LLMs to effectively learn and memorize new knowledge. Inspired by this observation, we propose a new method called MoRA, which employs a square matrix to achieve high-rank updating while maintaining the same number of trainable parameters. To achieve it, we introduce the corresponding non-parameter operators to reduce the input dimension and increase the output dimension for the square matrix. Furthermore, these operators ensure that the weight can be merged back into LLMs, which enables our method to be deployed like LoRA. We perform a comprehensive evaluation of our method across five tasks: instruction tuning, mathematical reasoning, continual pretraining, memory and pretraining. Our method outperforms LoRA on memory-intensive tasks and achieves comparable performance on other tasks.

## item_id: m_0890

TITLE: Emergent Communication with Attention

ABSTRACT: To develop computational agents that can better communicate with others using their own emergent language, we endow the agents with an ability to focus their attention on particular concepts in the environment. Humans often understand a thing or scene as a composite of concepts and those concepts are further mapped onto words. We implement this intuition as attention mechanisms in Speaker and Listener agents in a referential game and show attention leads to more compositional and interpretable emergent language. We also demonstrate how attention helps us understand the learned communication protocol by investigating the attention weights associated with each message symbol and the alignment of attention weights between Speaker and Listener agents. Overall, our results suggest that attention is a promising mechanism for developing more human-like emergent language.

## item_id: m_0891

TITLE: Learnability of Learned Neural Networks

ABSTRACT: This paper explores the simplicity of learned neural networks under various settings: learned on real vs random data, varying size/architecture and using large minibatch size vs small minibatch size. The notion of simplicity used here is that of learnability i.e., how accurately can the prediction function of a neural network be learned from labeled samples from it. While learnability is different from (in fact often higher than) test accuracy, the results herein suggest that there is a strong correlation between small generalization errors and high learnability.
This work also shows that there exist significant qualitative differences in shallow networks as compared to popular deep networks. More broadly, this paper extends in a new direction, previous work on understanding the properties of learned neural networks. Our hope is that such an empirical study of understanding learned neural networks might shed light on the right assumptions that can be made for a theoretical study of deep learning.

## item_id: m_0892

TITLE: Accelerating Retrieval-augmented Language Model Serving with Speculation

ABSTRACT: Retrieval-augmented language models (RaLM) have demonstrated the potential to solve knowledge-intensive natural language processing (NLP) tasks by combining a non-parametric knowledge base with a parametric language model. Instead of fine-tuning a fully parametric model, RaLM excels at its low-cost adaptation to the latest data and better source attribution mechanisms. Among various RaLM approaches, iterative RaLM delivers a better generation quality due to a more frequent interaction between the retriever and the language model. Despite the benefits, iterative RaLM usually encounters high overheads due to the frequent retrieval step. To this end, we propose RaLMSpec, a speculation-inspired framework that provides generic speed-up over iterative RaLM while preserving the same model outputs through speculative retrieval and batched verification. By further incorporating prefetching, optimal speculation stride scheduler, and asynchronous verification, RaLMSpec can automatically exploit the acceleration potential to the fullest. Extensive evaluations over three language models on four downstream QA datasets demonstrate that RaLMSpec can achieve a speed-up ratio of 1.75-2.39×, 1.04-1.39×, and 1.31-1.77× when the retriever is an exact dense retriever, approximate dense retriever, and sparse retriever respectively compared with the baseline.

## item_id: m_0893

TITLE: Query and Response Augmentation Cannot Help Out-of-domain Math Reasoning Generalization

ABSTRACT: In math reasoning with large language models (LLMs), fine-tuning data augmentation by query evolution and diverse reasoning paths is empirically verified effective, profoundly narrowing the gap between open-sourced LLMs and cutting-edge proprietary LLMs. 
In this paper, we conduct an investigation for such data augmentation in math reasoning and are intended to answer: 
(1) What strategies of data augmentation are more effective; 
(2) What is the scaling relationship between the amount of augmented data and model performance; and 
(3) Can data augmentation incentivize generalization to out-of-domain mathematical reasoning tasks?
To this end, we create a new dataset, AugGSM8K, by complicating and diversifying the queries from GSM8K and sampling multiple reasoning paths.
We obtained a series of LLMs called MuggleMath by fine-tuning on subsets of AugGSM8K. MuggleMath substantially achieves new state-of-the-art on GSM8K (from 54\% to 68.4\% at the scale of 7B, and from 63.9\% to 74.0\% at the scale of 13B).
A log-linear relationship is presented between MuggleMath’s performance and the amount of augmented data. 
We also find that MuggleMath is weak in out-of-domain math reasoning generalization to MATH. 
This is attributed to the differences in query distribution between AugGSM8K and MATH which suggest that augmentation on a single benchmark could not help with overall math reasoning performance.

## item_id: m_0894

TITLE: Towards Robust Multi-Objective Optimization: Adversarial Attack and Defense Methods for Neural Solvers

ABSTRACT: Deep reinforcement learning has shown great promise in addressing multi-objective combinatorial optimization problems. Nevertheless, the robustness and generalizability of existing neural solvers remain insufficiently explored, especially across diverse and complex problem distributions. This work provides a novel preference-based adversarial attack method, which aims to generate hard problem instances that expose vulnerabilities of solvers. We measure the vulnerability of a solver by evaluating the extent to which its performance in terms of hypervolume is affected when tested on hard instances. To mitigate the adversarial effect, we propose a defense method that integrates hardness-aware preference selection into adversarial training, achieving substantial improvements in solver robustness and generalizability. 
The experimental results on multi-objective traveling salesman problem (MOTSP), multi-objective capacitated vehicle routing problem (MOCVRP), and multi-objective knapsack problem (MOKP) verify that our attack method successfully learns hard instances for different solvers. Furthermore, our defense method significantly strengthens the robustness and generalizability of neural solvers, delivering superior performance on hard or out-of-distribution instances.

## item_id: m_0895

TITLE: Efficient Unified Multimodal Understanding and Generation with Gated Hybrid Attention

ABSTRACT: Unified multimodal learning requires attention mechanisms that are both efficient and expressive. 
Softmax attention provides strong modeling capacity but suffers from quadratic complexity, while 
linear attention achieves near-linear efficiency at the cost of weaker expressivity. We identify two 
major expressivity challenges in efficient unified multimodal models: (\emph{i}) modality imbalance, 
where dominant signals suppress weaker modalities during fusion, and (\emph{ii}) loss of global context, 
as efficient variants tend to over-smooth long sequences. We propose \textbf{Gated Hybrid Attention (GHA)}, 
a multimodal-specialized operator that augments linear attention with (\emph{i}) a selective gating mechanism 
to balance modality contributions and stabilize training, and (\emph{ii}) agent-token softmax aggregation 
to restore adaptive global context while preserving near-linear complexity. To demonstrate generality, we validate GHA in two representative paradigms: autoregressive-only(AR-only)
and autoregressive+diffusion(AR+Diffusion). In both settings, GHA consistently improves multimodal alignment, 
long-context retention, and efficiency over comparable Transformer and efficient attention baselines. 
These cross-paradigm results highlight that GHA functions as a plug-and-play building block, offering 
a lightweight and extensible approach that is orthogonal to scaling trends and modality complexity.

## item_id: m_0896

TITLE: Estimation of cross-lingual news similarities using text-mining methods

ABSTRACT: Every second, innumerable text data, including all kinds news, reports, messages, reviews, comments, and twits have been generated on the Internet,  which is written not only in English but also in other languages such as Chinese, Japanese, French and so on. Not only SNS sites but also worldwide news agency such as Thomson Reuters News provide news reported in more than 20 languages, reflecting the significance of the multilingual information.
In this research, by taking advantage of multi-lingual text resources provided by the Thomson Reuters News, we developed a bidirectional LSTM based method to calculate cross-lingual semantic text similarity for long text and short text respectively. Thus, users could understand the situation comprehensively, by investigating similar and related cross-lingual articles, when there an important news comes in.

## item_id: m_0897

TITLE: MetaGen: Assessing Conditions of Generalization

ABSTRACT: The Machine Learning (ML) community has been criticized for irreproducible results that do not generalize. Current ML practices identify the best-performing configuration by sampling a limited set of them (e.g. with Hyperparameter Optimization) and evaluating their performance. Model comparison is then performed by aggregating the performance of several trials (e.g. with ANOVA) or based on the best-performing trial (proof-by-existence). We find that both methods of comparison can be inapplicable as ML performance metrics with their corresponding hyperparameter configurations, performance manifold, have unequal variance (heteroscedastic). As such, it is important to know what hyperparameters perform robustly, conditions of generalization. To our knowledge, our work is the first to evaluate the model comparison problem in ML that impacts the safety of existing HPO methods as well as the explainability of the configurations for which a model improves. We propose MetaGen for uncertainty estimation on the performance manifold and identify contiguous regions of consistent performance. We use Meta Gen for post-hoc analysis to compare between hyperparameter regions as opposed to single-point estimates. We extend MetaGen in an online manner and apply HPO on the hyperparameter region for which a method performs robustly. When used for post-hoc analysis, MetaGen avoids bias from misleading evidence by outliers or aggregate effects and improves the explainability of a method’s performance. When used in an online manner, our method can improve the safety of systems that need to be iteratively re-trained by improving the robustness and performance by as much as 5.22% for the three HPO sampling methods that we evaluate. We use the results of 61,475 experimental trials from Transformer, VGG, ResNet trained on 8 different datasets, 200,628 trials from 3 NAS benchmarks and evaluate our method in identifying the hyperparameter regions where a model performs robustly. Our method improves model comparison and is robust to heteroscedasticity.

## item_id: m_0898

TITLE: NOTELA: A Generalizable Method for Source Free Domain Adaptation

ABSTRACT: Source-free domain adaptation (SFDA) is a compelling problem as it allows to leverage any off-the-shelf model without requiring access to its original training set and adapts it using only unlabelled data. While several SFDA approaches have recently been proposed, their evaluation focuses on a narrow set of distribution shifts for vision tasks, and their generalizability outside of that scope has not yet been investigated. We put those recent approaches to the test by evaluating them on a new set of challenging---due to extreme covariate and label shift---and naturally-occurring distribution shifts in the audio domain. We study the task of adapting a bird species classifier trained on focalized recordings of bird songs to datasets of passive recordings for various geographical locations. Interestingly, we find that some recent SFDA methods underperform doing no adaptation at all. Drawing inspiration from those findings and insights, we propose a new method that improves on noisy student approaches by adjusting the teacher's pseudo-labels through Laplacian regularization. Our approach enjoys increased stability and significantly better performance on several of our proposed distribution shifts. We then look back at SFDA benchmarks in the vision domain and find that our approach is competitive with the state-of-the-art there as well. 

## item_id: m_0899

TITLE: Improving Long-Horizon Imitation Through Language Prediction

ABSTRACT: Complex, long-horizon planning and its combinatorial nature pose steep challenges for learning-based agents. Difficulties in such settings are exacerbated in low data regimes where over-fitting stifles generalization and compounding errors hurt accuracy. In this work, we explore the use of an often unused source of auxiliary supervision: language. Inspired by recent advances in transformer-based models, we train agents with an instruction prediction loss that encourages learning temporally extended representations that operate at a high level of abstraction. Concretely, we demonstrate that instruction modeling significantly improves performance in planning environments when training with a limited number of demonstrations on the BabyAI and Crafter benchmarks. In further analysis we find that instruction modeling is most important for tasks that require complex reasoning, while understandably offering smaller gains in environments that require simple plans. Our benchmarks and code will be publicly released.

## item_id: m_0900

TITLE: Coordinate and Generalize: A Unified Framework for Audio-Visual Zero-Shot Learning

ABSTRACT: Audio-Visual Zero-Shot Learning (AV-ZSL) aims to train a model that can classify videos of unseen classes leveraging audio and visual data, which is achieved by transferring knowledge obtained from seen classes. We identify two imperative issues needed to be addressed: (1) \emph{How to effectively exploit both the audio and visual information?} and (2) \emph{How to transfer the knowledge from seen classes to unseen classes?} In this paper, we ameliorate both of the issues in a unified framework by enhancing two ingredients that existing methods seldom consider. (1) \emph{Multi-Modal Coordination}: Different from existing methods simply fusing the audio and visual features by attention mechanism, we further perform knowledge distillation between the visual and audio branches. This allows information interaction between the two branches and encourages them to learn from each other. (2) \emph{Generalization Capacity}: Existing methods only consider the alignment between the audio-visual features and semantic features on the seen classes, which ignores the generalization capacity. Inspired by the interpretability methods of Deep Neural Networks (DNNs), we propose a novel gradient-based approach to generate transferable masks for the visual and audio features, enforcing the model to focus on the most discriminative segments and benefiting knowledge transfer from seen to unseen classes. Extensive experiments on three challenging benchmarks, ActivityNet-GZSL, UCF-GZSL, and VGGSound-GZSL, demonstrate that our proposed approach can significantly outperform the state-of-the-art methods.
