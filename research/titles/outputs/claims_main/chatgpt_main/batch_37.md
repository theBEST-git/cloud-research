# Batch 37 — 100 items

## item_id: m_3601

TITLE: The impacts of known and unknown demonstrator irrationality on reward inference

ABSTRACT: Algorithms inferring rewards from human behavior typically assume that people are (approximately) rational. In reality, people exhibit a wide array of irrationalities. Motivated by understanding the benefits of modeling these irrationalities, we analyze the effects that demonstrator irrationality has on reward inference. We propose operationalizing several forms of irrationality in the language of MDPs, by altering the Bellman optimality equation, and use this framework to study how these alterations affect inference. 

We find that incorrectly assuming noisy-rationality for an irrational demonstrator can lead to remarkably poor reward inference accuracy, even in situations where inference with the correct model leads to good inference. This suggests a need to either model irrationalities or find reward inference algorithms that are more robust to misspecification of the demonstrator model. Surprisingly, we find that if we give the learner access to the correct model of the demonstrator's irrationality, these irrationalities can actually help reward inference. In other words, if we could choose between a world where humans were perfectly rational and the current world where humans have systematic biases, the current world might counter-intuitively be preferable for reward inference. We reproduce this effect in several domains. While this finding is mainly conceptual, it is perhaps actionable as well: we might ask human demonstrators for myopic demonstrations instead of optimal ones, as they are more informative for the learner and might be easier for a human to generate.

## item_id: m_3602

TITLE: Long-tailed Recognition by Routing Diverse Distribution-Aware Experts

ABSTRACT: Natural data are often long-tail distributed over semantic classes.  Existing recognition methods tackle this imbalanced classification by placing more emphasis on the tail data, through class re-balancing/re-weighting or ensembling over different data groups, resulting in increased tail accuracies but reduced head accuracies.
We take a dynamic view of the training data and provide a principled model bias and variance analysis as the training data fluctuates: Existing long-tail classifiers invariably increase the model variance and the head-tail model bias gap remains large, due to more and larger confusion with hard negatives for the tail.
We propose a new long-tailed classifier called RoutIng Diverse Experts (RIDE).  It reduces the model variance with multiple experts, reduces the model bias with a distribution-aware diversity loss, reduces the computational cost with a dynamic expert routing module.  RIDE outperforms the state-of-the-art by 5% to 7% on CIFAR100-LT, ImageNet-LT and iNaturalist 2018 benchmarks.  It is also a universal framework that is applicable to various backbone networks, long-tailed algorithms and training mechanisms for consistent performance gains. Our code is available at: https://github.com/frank-xwang/RIDE-LongTailRecognition.

## item_id: m_3603

TITLE: Sampling Generative Networks

ABSTRACT: We introduce several techniques for sampling and visualizing the latent spaces of generative models. Replacing linear interpolation with spherical linear interpolation prevents diverging from a model's prior distribution and produces sharper samples. J-Diagrams and MINE grids are introduced as visualizations of manifolds created by analogies and nearest neighbors. We demonstrate two new techniques for deriving attribute vectors: bias-corrected vectors with data replication and synthetic vectors with data augmentation.  Binary classification using attribute vectors is presented as a technique supporting quantitative analysis of the latent space. Most techniques are intended to be independent of model type and examples are shown on both Variational Autoencoders and Generative Adversarial Networks.


## item_id: m_3604

TITLE: Provably Communication-efficient Data-parallel SGD via Nonuniform Quantization

ABSTRACT: As the size and complexity of models and datasets grow, so does the need for communication-efficient variants of stochastic gradient descent that can be deployed on clusters to perform model fitting in parallel. Alistarh et al. (2017) describe two variants of data-parallel SGD that quantize and encode gradients to lessen communication costs. For the first variant, QSGD, they provide strong theoretical guarantees. For the second variant, which we call QSGDinf, they demonstrate impressive empirical gains for distributed training of large neural networks. Building on their work, we propose an alternative scheme for quantizing gradients and show that it yields stronger theoretical guarantees than exist for QSGD while matching the empirical performance of QSGDinf.

## item_id: m_3605

TITLE: HFH: Homologically Functional Hashing for Compressing Deep Neural Networks

ABSTRACT: As the complexity of deep neural networks (DNNs) trends to grow to absorb the increasing sizes of data, memory and energy consumption has been receiving more and more attentions for industrial applications, especially on mobile devices. This paper presents a novel structure based on homologically functional hashing to compress DNNs, shortly named as HFH. For each  weight entry in a deep net, HFH uses multiple low-cost hash functions to fetch values in a compression space, and then employs a small reconstruction network to recover that entry. The compression space is homological because all layers fetch hashed values from it. The reconstruction network is plugged into the whole network and trained jointly. On several benchmark datasets, HFH demonstrates high compression ratios with little loss on prediction accuracy. Particularly, HFH includes the recently proposed HashedNets as a degenerated scenario and shows significantly improved performance. Moreover, the homological hashing essence facilitates us to efficiently figure out one single desired compression ratio, instead of exhaustive searching throughout a combinatory space configured by all layers.

## item_id: m_3606

TITLE: Deep Generative Modeling for Identification of Noisy, Non-Stationary Dynamical Systems

ABSTRACT: An important challenge in many fields of science and engineering is making sense of time-dependent measurement data by recovering governing equations in the form of differential equations. We focus on finding parsimonious ordinary differential equation (ODE) models for nonlinear, noisy, and non-autonomous dynamical systems and propose a machine learning method for data-driven system identification. While many methods tackle noisy and limited data, non-stationarity – where differential equation parameters change over time – has received less attention. Our method, dynamic SINDy, combines variational inference with SINDy (sparse identification of nonlinear dynamics) to model time-varying coefficients of sparse ODEs. This framework allows for uncertainty quantification of ODE coefficients,
expanding on previous methods for autonomous systems. These coefficients are then interpreted as latent variables and added to the system to obtain an autonomous dynamical model. We validate our approach using synthetic data, including nonlinear oscillators and the Lorenz system, and apply it to neuronal activity data from C. elegans. Dynamic SINDy uncovers a global nonlinear model, showing it can
handle real, noisy, and chaotic datasets. We aim to apply our method to a wide range of problems, specifically to dynamic systems where complex parametric time dependencies are expected.

## item_id: m_3607

TITLE: Precise Parameter Localization for Textual Generation in Diffusion Models

ABSTRACT: Novel diffusion models can synthesize photo-realistic images with integrated high-quality text. Surprisingly, we demonstrate through 
attention activation patching that only less than $1$\% of diffusion models' parameters, all contained in attention layers, influence the generation of textual content within the images.  Building on this observation, we improve textual generation efficiency and performance by targeting cross and joint attention layers of diffusion models.  We introduce several applications that benefit from localizing the layers responsible for textual content generation. We first show that a LoRA-based fine-tuning solely of the localized layers enhances, even more, the general text-generation capabilities of large diffusion models while preserving the quality and diversity of the diffusion models' generations. Then, we demonstrate how we can use the localized layers to edit textual content in generated images. Finally, we extend this idea to the practical use case of preventing the generation of toxic text in a cost-free manner. In contrast to prior work, our localization approach is broadly applicable across various diffusion model architectures, including U-Net (e.g., SDXL and DeepFloyd IF) and transformer-based (e.g., Stable Diffusion 3), utilizing diverse text encoders (e.g., from CLIP to the large language models like T5). Project page available at https://t2i-text-loc.github.io/.

## item_id: m_3608

TITLE: Equivariant Graph Self-Attention Transformer for Learning Higher-Order Interactions in 3D Molecular Structures

ABSTRACT: Despite their considerable success in multiple fields, studying 3D molecular structures of varying sizes presents a significant challenge in machine learning, particularly in drug discovery, as existing methods often struggle to accurately capture complex geometric relationships and tend to be less effective at generalizing across diverse molecular environments. To address these limitations, we propose a novel Equivariant Graph Self-Attention  Transformer, namely EG-SAT, which effectively leverages both geometric and relational features of molecular data while maintaining equivariance under Euclidean transformations. This approach enables the model to capture molecular geometry through higher-order representations, enhancing its ability to understand intricate spatial relationships and atomic interactions. By effectively modeling the radial and angular distributions of neighboring atoms within a specified cutoff distance using Atom-Centered Symmetry Functions (ACSFs), EG-SAT leads to a more nuanced and comprehensive understanding of molecular interactions. We validate our model on the QM9 and MD17 datasets, demonstrating that EG-SAT achieves state-of-the-art performance in predicting most quantum mechanical properties, thus showcasing its effectiveness and robustness in this domain.

## item_id: m_3609

TITLE: Neural Architecture Retrieval

ABSTRACT: With the increasing number of new neural architecture designs and substantial existing neural architectures, it becomes difficult for the researchers to situate their contributions compared with existing neural architectures or establish the connections between their designs and other relevant ones. To discover similar neural architectures in an efficient and automatic manner, we define a new problem Neural Architecture Retrieval which retrieves a set of existing neural architectures which have similar designs to the query neural architecture. Existing graph pre-training strategies cannot address the computational graph in neural architectures due to the graph size and motifs. To fulfill this potential, we propose to divide the graph into motifs which are used to rebuild the macro graph to tackle these issues, and introduce multi-level contrastive learning to achieve accurate graph representation learning. Extensive evaluations on both human-designed and synthesized neural architectures demonstrate the superiority of our algorithm. Such a dataset which contains 12k real-world network architectures, as well as their embedding, is built for neural architecture retrieval.

## item_id: m_3610

TITLE: Emergent Communication through Negotiation

ABSTRACT: Multi-agent reinforcement learning offers a way to study how communication could emerge in communities of agents needing to solve specific problems. In this paper, we study the emergence of communication in the negotiation environment, a semi-cooperative model of agent interaction. We introduce two communication protocols - one grounded in the semantics of the game, and one which is a priori ungrounded.  We show that self-interested agents can use the pre-grounded communication channel to negotiate fairly, but are unable to effectively use the ungrounded, cheap talk channel to do the same.  However, prosocial agents do learn to use cheap talk to find an optimal negotiating strategy, suggesting that cooperation is necessary for language to emerge. We also study communication behaviour in a setting where one agent interacts with agents in a community with different levels of prosociality and show how agent identifiability can aid negotiation.

## item_id: m_3611

TITLE: MAE: Mutual Posterior-Divergence Regularization for Variational AutoEncoders

ABSTRACT: Variational Autoencoder (VAE), a simple and effective deep generative model, has led to a number of impressive empirical successes and spawned many advanced variants and theoretical investigations. However, recent studies demonstrate that, when equipped with expressive generative distributions (aka. decoders), VAE suffers from learning uninformative latent representations with the observation called KL Varnishing, in which case VAE collapses into an unconditional generative model. In this work, we introduce mutual posterior-divergence regularization, a novel regularization that is able to control the geometry of the latent space to accomplish meaningful representation learning, while achieving comparable or superior capability of density estimation.Experiments on three image benchmark datasets demonstrate that, when equipped with powerful decoders, our model performs well both on density estimation and representation learning.

## item_id: m_3612

TITLE: Differentiable Weighted Finite-State Transducers

ABSTRACT: We introduce a framework for automatic differentiation with weighted finite-state transducers (WFSTs) allowing them to be used dynamically at training time. Through the separation of graphs from operations on graphs, this framework enables the exploration of new structured loss functions which in turn eases the encoding of prior knowledge into learning algorithms. We show how the framework can combine pruning and back-off in transition models with various sequence-level loss functions. We also show how to learn over the latent decomposition of phrases into word pieces. Finally, to demonstrate that WFSTs can be used in the interior of a deep neural network, we propose a convolutional WFST layer which maps lower-level representations to higher-level representations and can be used as a drop-in replacement for a traditional convolution. We validate these algorithms with experiments in handwriting recognition and speech recognition.

## item_id: m_3613

TITLE: Discriminator Rejection Sampling

ABSTRACT: We propose a rejection sampling scheme using the discriminator of a GAN to
approximately correct errors in the GAN generator distribution. We show that
under quite strict assumptions, this will allow us to recover the data distribution
exactly. We then examine where those strict assumptions break down and design a
practical algorithm—called Discriminator Rejection Sampling (DRS)—that can be
used on real data-sets. Finally, we demonstrate the efficacy of DRS on a mixture of
Gaussians and on the state of the art SAGAN model. On ImageNet, we train an
improved baseline that increases the best published Inception Score from 52.52 to
62.36 and reduces the Frechet Inception Distance from 18.65 to 14.79. We then use
DRS to further improve on this baseline, improving the Inception Score to 76.08
and the FID to 13.75.

## item_id: m_3614

TITLE: KARE-RAG: Knowledge-Aware Refinement and Enhancement for RAG

ABSTRACT: Retrieval-Augmented Generation (RAG) enables Large Language Models (LLMs) to access external knowledge sources, significantly enhancing their ability to perform knowledge-intensive tasks. As RAG systems become increasingly vital for real-world applications, improving their ablility of leveraginge externel knowledge has emerged as a critical research direction. Recent studies have explored fine-tuning approaches to enhance LLMs' adaptability in RAG scenarios. However, the inherent complexity of RAG systems makes it challenging to achieve robust performance without substantial amounts of high-quality training data, particularly when handling multi-hop reasoning and other complex tasks that require rich information content and intricate relationships between knowledge elements.

In this paper, we present KARE-RAG (Knowledge-Aware Refinement and Enhancement for RAG), which introduces a novel strategy for RAG optimization. Our key insight is that by training models to construct structured knowledge representations as intermediate outputs, models can learn robust information discrimination strategies from minimal training data while maintaining the flexibility of end-to-end generation. Experiments show our method achieves superior OOD performance while requiring substantially less training data. Notably, these improvements are achieved without compromising general capabilities or requiring modifications to standard RAG inference pipelines. Our findings establish that targeted training strategies focusing on knowledge organization can unlock more efficient optimization pathways for RAG systems. All data and code will be publicly available on Github.

## item_id: m_3615

TITLE: BAAAN: Backdoor Attacks Against Auto-encoder and GAN-Based Machine Learning Models

ABSTRACT: The tremendous progress of autoencoders and generative adversarial networks (GANs) has led to their application to multiple critical tasks, such as fraud detection and sanitized data generation. This increasing adoption has fostered the study of security and privacy risks stemming from these models. However, previous works have mainly focused on membership inference attacks. In this work, we explore one of the most severe attacks against machine learning models, namely the backdoor attack, against both autoencoders and GANs. The backdoor attack is a training time attack where the adversary implements a hidden backdoor in the target model that can only be activated by a secret trigger. State-of-the-art backdoor attacks focus on classification-based tasks. We extend the applicability of backdoor attacks to autoencoders and GAN-based models. More concretely, we propose the first backdoor attack against autoencoders and GANs where the adversary can control what the decoded or generated images are when the backdoor is activated. Our results show that the adversary can build a backdoored autoencoder that returns a target output for all backdoored inputs, while behaving perfectly normal on clean inputs. Similarly, for the GANs, our experiments show that the adversary can generate data from a different distribution when the backdoor is activated, while maintaining the same utility when the backdoor is not.

## item_id: m_3616

TITLE: Can In-context Learning Really Generalize to Out-of-distribution Tasks?

ABSTRACT: In this work, we explore the mechanism of in-context learning (ICL) on out-of-distribution (OOD) tasks that were not encountered during training. To achieve this, we conduct synthetic experiments where the objective is to learn OOD mathematical functions through ICL using a GPT-2 model. We reveal that Transformers may struggle to learn OOD task functions through ICL. Specifically, ICL performance resembles implementing a function within the pretraining hypothesis space and optimizing it with gradient descent based on the in-context examples. Additionally, we investigate ICL's well-documented ability to learn unseen abstract labels in context. We demonstrate that such ability only manifests in the scenarios without distributional shifts and, therefore, may not serve as evidence of new-task-learning ability. Furthermore, we assess ICL's performance on OOD tasks when the model is pretrained on multiple tasks. Both empirical and theoretical analyses demonstrate the existence of the \textbf{low-test-error preference} of ICL, where it tends to implement the pretraining function that yields low test error in the testing context. We validate this through numerical experiments. This new theoretical result, combined with our empirical findings, elucidates the mechanism of ICL in addressing OOD tasks.

## item_id: m_3617

TITLE: NeuManifold: Neural Watertight Manifold Reconstruction with Efficient and High-Quality Rendering Support

ABSTRACT: We present a method for generating high-quality watertight manifold meshes from multi-view input images. Existing volumetric rendering methods are robust in optimization but tend to generate noisy meshes with poor topology. Differentiable rasterization-based methods can generate high-quality meshes but are sensitive to initialization. Our method combines the benefits of both worlds; we take the geometry initialization obtained from neural volumetric fields, and further optimize the geometry as well as a compact neural texture representation 
with differentiable rasterizers. Through extensive experiments, we demonstrate that our method can generate accurate mesh reconstructions with faithful appearance that are comparable to previous volume rendering methods while being an order of magnitude 
faster in rendering. We also show that our generated mesh and neural texture reconstruction is compatible with existing graphics pipelines and enables downstream 3D applications such as simulation.

## item_id: m_3618

TITLE: Unsupervised Word Alignment via Cross-Lingual  Contrastive Learning

ABSTRACT: Word alignment is essential for the down-streaming cross-lingual language understanding and generation tasks. Recently, the performance of the neural word alignment models has exceeded that of statistical models. However, they heavily rely on sophisticated translation models. In this study, we propose a super lightweight unsupervised word alignment model, dubbed MirrorAlign, in which bidirectional symmetric attention trained with a contrastive learning objective is introduced, and an agreement loss is employed to bind the attention maps, such that the alignments follow mirror-like symmetry hypothesis. Experimental results on several public benchmarks demonstrate that our model achieves competitive, if not better, performance compared to the state of the art in word alignment while significantly reducing the training and decoding time on average. Further ablation analysis and case studies show the superiority of our proposed MirrorAlign. Notably, we recognize our model as a pioneer attempt to unify bilingual word embedding and word alignments. Encouragingly, our approach achieves 16.4X speedup against GIZA++, and 50X parameter compression compared with the Transformer-based alignment methods. We released our code to facilitate the community: https://github.com/ICLR20anonymous/mirroralign

## item_id: m_3619

TITLE: Improving Stochastic Gradient Descent with Feedback

ABSTRACT: In this paper we propose a simple and efficient method for improving stochastic gradient descent methods by using feedback from the objective function. The method tracks the relative changes in the objective function with a running average, and uses it to adaptively tune the learning rate in stochastic gradient descent. We specifically apply this idea to modify Adam, a popular algorithm for training deep neural networks. We conduct experiments to compare the resulting algorithm, which we call Eve, with state of the art methods used for training deep learning models. We train CNNs for image classification, and RNNs for language modeling and question answering. Our experiments show that Eve outperforms all other algorithms on these benchmark tasks. We also analyze the behavior of the feedback mechanism during the training process.


## item_id: m_3620

TITLE: Expressiveness of Neural Networks Having Width Equal or Below the Input Dimension

ABSTRACT: The understanding about the minimum width of deep neural networks needed to ensure universal approximation for different activation functions has progressively been extended \citep{park2020minimum}. In particular,  with respect to approximation on general compact sets in the input space, a network width less than or equal to the input dimension excludes universal approximation. In this work, we focus on network functions of width less than or equal to the latter critical bound. We prove a maximum principle from which we conclude that for all continuous and monotonic activation functions, universal approximation of arbitrary continuous functions is impossible on sets that coincide with the boundary of an open set plus an inner point. Conversely, we prove that in this regime, the exact fit of partially constant functions on disjoint compact sets is still possible for ReLU network functions under some conditions on the mutual location of these components. We also show that with cosine as activation function, a three layer network of width one is sufficient to approximate any function on arbitrary finite sets.

## item_id: m_3621

TITLE: GEP: A GCG-Based method for extracting personally identifiable information from chatbots built on small language models

ABSTRACT: Small language models (SLMs) become unprecedentedly appealing due to their approximately equivalent performance compared to large language models (LLMs) in certain fields with less energy and time consumption during training and inference. However, the personally identifiable information (PII) leakage of SLMs for downstream tasks has yet to be explored. In this study, we investigate the PII leakage of the chatbot based on SLM. We first finetune a new chatbot, i.e., ChatBioGPT based on the backbone of BioGPT using medical datasets Alpaca and HealthCareMagic. It shows a matchable performance in BERTscore compared with previous studies of ChatDoctor and ChatGPT. Based on this model, we prove that the previous template-based PII attacking methods cannot effectively extract the PII in the dataset for leakage detection under the SLM condition. We then propose GEP, which is a greedy coordinate gradient-based (GCG) method specifically designed for PII extraction. We conduct experimental studies of GEP and the results show an increment of up to 60$\times$ more leakage compared with the previous template-based methods. We further expand the capability of GEP in the case of a more complicated and realistic situation by conducting free-style insertion where the inserted PII in the dataset is in the form of various syntactic expressions instead of fixed templates, and GEP is still able to reveal a PII leakage rate of up to 4.53%.

## item_id: m_3622

TITLE: Artificial Design: Modeling Artificial Super Intelligence with Extended General Relativity and Universal Darwinism via Geometrization for Universal Design Automation

ABSTRACT: Let us share the joy of our unprecedented discovery with you: Physical Geometry and Biological Geometry are the outcome of the physical laws and biological laws respectively, and Artificial Super Intelligence (ASI) has to be a combination of both design and learning instead of learning alone, with that we propose Artificial Design, a bio-physical inspired mathematical model for Hierarchical Multi-Agent Multi-Environment Model-agnostic Policy-agnostic Deep Reinforcement Learning (HMMMPDRL) based ASI by reusing and extending General Relativity and Universal Darwinism with Geometrization. With Artificial Design we solve Deep Reinforcement Learning blackbox puzzle in AI and ASI. By treating HMMMPDRL as multiverse regardless the mutual exclusiveness between Multi-Agent and Multi-Environment, we reuse General Relativity's 4-Dimensional Pseudo-Riemannian Manifold based SpaceTime Model for Reinforcement Learning part of HMMMPDRL,
we also make a T-symmetry extension to General 
Relativity, replace N-Dimensional space with N-Dimensional GeneSpace, 
and formulate a N-Dimensional Riemannian Manifold based GeneSpace Model for Deep Learning part of HMMMPDRL, whereas Deep Learning architecture is adopted to approximate very complex state-action space composed environments in HMMMPDRL. By modeling ASI with Artificial Design rigorously in this way, we claim that intelligence, whether natural, artificial, or super-artificial like ASI, is just the geometry effect of N-Dimensional GeneSpace caused by Geometrization, and that paves the way in achieving ASI through Universal Design Automation of Artificial Design in theory. Of course, our Multiversal endeavor won't stop from there, endorse us to artificially co-accelerate human civilization in every possible way you might imagine. 



## item_id: m_3623

TITLE: PETformer: Long-term Time Series Forecasting via Placeholder-enhanced Transformer

ABSTRACT: Recently, the superiority of Transformer for long-term time series forecasting (LTSF) tasks has been challenged, particularly since recent work has shown that simple models can outperform numerous Transformer-based approaches. This suggests that a notable gap remains in fully leveraging the potential of Transformer in LTSF tasks. Consequently, this study investigates key issues when applying Transformer to LTSF, encompassing aspects of temporal continuity, information density, and multi-channel relationships. We introduce the Placeholder-enhanced Technique (PET) to enhance the computational efficiency and predictive accuracy of Transformer in LTSF tasks. Furthermore, we delve into the impact of larger patch strategies and channel interaction strategies on Transformer's performance, specifically Long Sub-sequence Division (LSD) and Multi-channel Separation and Interaction (MSI). These strategies collectively constitute a novel model termed PETformer. Extensive experiments have demonstrated that PETformer achieves state-of-the-art performance on eight commonly used public datasets for LTSF, surpassing all existing models. The insights and enhancement methodologies presented in this paper serve as valuable reference points and sources of inspiration for future research endeavors.

## item_id: m_3624

TITLE: ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation

ABSTRACT: The ability to perform pixel-wise semantic segmentation in real-time is of paramount importance in practical mobile applications. Recent deep neural networks aimed at this task have the disadvantage of requiring a large number of floating point operations and have long run-times that hinder their usability. In this paper, we propose a novel deep neural network architecture named ENet (efficient neural network), created specifically for tasks requiring low latency operation. ENet is up to 18x faster, requires 75x less FLOPs, has 79x less parameters, and provides similar or better accuracy to existing models.           
We have tested it on CamVid, Cityscapes and SUN datasets and report on comparisons with existing state-of-the-art methods, and the trade-offs between accuracy and processing time of a network. We present performance measurements of the proposed architecture on embedded systems and suggest possible software improvements that could make ENet even faster.      


## item_id: m_3625

TITLE: RuAG: Learned-rule-augmented Generation for Large Language Models

ABSTRACT: In-context learning (ICL) and Retrieval-Augmented Generation (RAG) have gained attention for their ability to enhance LLMs' reasoning by incorporating external knowledge but suffer from limited contextual window size, leading to insufficient information injection. To this end, we propose a novel framework to automatically distill large volumes of offline data into interpretable first-order logic rules, which are injected into LLMs to boost their reasoning capabilities. Our method begins by formulating the search process relying on LLMs' commonsense, where LLMs automatically define head and body predicates. Then, we apply Monte Carlo Tree Search (MCTS)  to address the combinational searching space and efficiently discover logic rules from data. The resulting logic rules are translated into natural language, allowing targeted knowledge injection and seamless integration into LLM prompts for LLM's downstream task reasoning. We evaluate our framework on public and private industrial tasks, including Natural Language Processing (NLP), time-series, decision-making, and industrial tasks, demonstrating its effectiveness in enhancing LLM's capability over diverse tasks.

## item_id: m_3626

TITLE: Differentiable learning of numerical rules in knowledge graphs

ABSTRACT: Rules over a knowledge graph (KG) capture interpretable patterns in data and can be used for KG cleaning and completion. Inspired by the TensorLog differentiable logic framework, which compiles rule inference into a sequence of differentiable operations, recently a method called Neural LP has been proposed for learning the parameters as well as the structure of rules. However, it is limited with respect to the treatment of numerical features like age, weight or scientific measurements. We address this limitation by extending Neural LP to learn rules with numerical values, e.g., ”People younger than 18 typically live with their parents“. We demonstrate how dynamic programming and cumulative sum operations can be exploited to ensure efficiency of such extension. Our novel approach allows us to extract more expressive rules with aggregates, which are of higher quality and yield more accurate predictions compared to rules learned by the state-of-the-art methods, as shown by our experiments on synthetic and real-world datasets.

## item_id: m_3627

TITLE: Improving Exploration of Deep Reinforcement Learning using Planning for Policy Search

ABSTRACT: Most Deep Reinforcement Learning methods perform local search and
therefore are prone to get stuck on non-optimal
solutions. Furthermore, in simulation based training, such as
domain-randomized simulation training, the availability of a simulation
model is not exploited, which potentially decreases
efficiency. To overcome issues of local search and exploit
access to simulation models, we propose the use of kino-dynamic
planning methods as part of a model-based reinforcement learning
method and to learn in an off-policy fashion from solved planning
instances. We show that, even on a simple toy domain, D-RL
methods (DDPG, PPO, SAC) are not immune to local optima and
require additional exploration mechanisms. We show that our
planning method exhibits a better state space coverage, collects
data that allows for better policies than D-RL methods without
additional exploration mechanisms and that starting from the
planner data and performing additional training results in as
good as or better policies than vanilla D-RL methods, while also
creating data that is more fit for re-use in modified tasks.


## item_id: m_3628

TITLE: Efficiently Modeling Long Sequences with Structured State Spaces

ABSTRACT: A central goal of sequence modeling is designing a single principled model that can address sequence data across a range of modalities and tasks, particularly on long-range dependencies.  Although conventional models including RNNs, CNNs, and Transformers have specialized variants for capturing long dependencies, they still struggle to scale to very long sequences of $10000$ or more steps.  A promising recent approach proposed modeling sequences by simulating the fundamental state space model (SSM) \( x'(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t) \), and showed that for appropriate choices of the state matrix \( A \), this system could handle long-range dependencies mathematically and empirically.  However, this method has prohibitive computation and memory requirements, rendering it infeasible as a general sequence modeling solution.  We propose the Structured State Space sequence model (S4) based on a new parameterization for the SSM, and show that it can be computed much more efficiently than prior approaches while preserving their theoretical strengths.  Our technique involves conditioning \( A \) with a low-rank correction, allowing it to be diagonalized stably and reducing the SSM to the well-studied computation of a Cauchy kernel.  S4 achieves strong empirical results across a diverse range of established benchmarks, including (i) 91\% accuracy on sequential CIFAR-10 with no data augmentation or auxiliary losses, on par with a larger 2-D ResNet, (ii) substantially closing the gap to Transformers on image and language modeling tasks, while performing generation $60\times$ faster (iii) SoTA on every task from the Long Range Arena benchmark, including solving the challenging Path-X task of length 16k that all prior work fails on, while being as efficient as all competitors.

## item_id: m_3629

TITLE: Efficient iterative policy optimization

ABSTRACT: We tackle the issue of finding a good policy when the number of policy updates is limited. This is done by approximating the expected policy reward as a sequence of concave lower bounds which can be efficiently maximized, drastically reducing the number of policy updates required to achieve good performance. We also extend existing methods to negative rewards, enabling the use of control variates.

## item_id: m_3630

TITLE: Unsupervised Learning of State Representations for Multiple Tasks

ABSTRACT: We present an approach for learning state representations in multi-task reinforcement learning. Our method learns multiple low-dimensional state representations from raw observations in an unsupervised fashion, without any knowledge of which task is executed, nor of the number of tasks involved.
The method is based on a gated neural network architecture, trained with an extension of the learning with robotic priors objective. In simulated experiments, we show that our method is able to learn better state representations for reinforcement learning, and we analyze why and when it manages to do so.

## item_id: m_3631

TITLE: Regularization Matters in Policy Optimization - An Empirical Study on Continuous Control

ABSTRACT: Deep Reinforcement Learning (Deep RL) has been receiving increasingly more attention  thanks to its encouraging performance on a variety of control tasks. Yet, conventional regularization techniques in training neural networks (e.g., $L_2$ regularization, dropout) have been largely ignored in RL methods, possibly because agents are typically trained and evaluated in the same environment, and because the deep RL community focuses more on high-level algorithm designs. In this work, we present the first comprehensive study of regularization techniques with multiple policy optimization algorithms on continuous control tasks. Interestingly, we find conventional regularization techniques on the policy networks can often bring large improvement, especially on harder tasks. Our findings are shown to be robust against training hyperparameter variations. We also compare these techniques with the more widely used entropy regularization. In addition, we study regularizing different components and find that only regularizing the policy network is typically the best. We further analyze why regularization may help generalization in RL from four perspectives - sample complexity, reward distribution, weight norm, and noise robustness. We hope our study provides guidance for future practices in regularizing policy optimization algorithms. Our code is available at https://github.com/xuanlinli17/iclr2021_rlreg .

## item_id: m_3632

TITLE: Improving length generalization in transformers via task hinting

ABSTRACT: It has been observed in recent years that transformers have problems
  with length generalization for certain types of reasoning and
  arithmetic tasks. In particular, the performance of a transformer
  model trained on tasks (say addition) up to a certain
  length (e.g., 5 digit numbers) drops sharply when applied to longer instances of the
  same problem. This work proposes an
  approach based on task hinting towards addressing length generalization. Our key idea is that while training the model on task-specific data, it
  is helpful to simultaneously train the model to solve a
  simpler but related auxiliary task as well.

  We study the classical sorting problem as a canonical example
  to evaluate our approach. We design a multitask training
  framework and show that models trained via task hinting
  significantly improve length generalization. In particular, for sorting we show that it is possible to
  train models on data consisting of sequences having length at most
  $20$, and improve the test accuracy on sequences of length $100$
  from less than $1$% (for standard training) to more than $92$%
  (via task hinting).

  Our study uncovers several interesting aspects of length
  generalization. We observe that while several auxiliary tasks may
  seem natural a priori, their effectiveness in improving
  length generalization differs dramatically. We further use probing
  and visualization-based techniques to understand the internal
  mechanisms via which the model performs the task, and propose a theoretical construction
  consistent with the observed learning behaviors of the model. Based
  on our construction, we show that introducing a small number of
  length dependent parameters into the training procedure can further
  boost the performance on unseen lengths. Finally, we also show the
  efficacy of our task hinting based approach beyond
  sorting, giving hope that these techniques will be applicable in
  broader contexts.

## item_id: m_3633

TITLE: Incremental Learning in Deep Convolutional Neural Networks Using Partial Network Sharing

ABSTRACT: Deep convolutional neural network (DCNN) based supervised learning is a widely practiced approach for large-scale image classification.  However, retraining these large networks to accommodate new, previously unseen data demands high computational time and energy requirements. Also, previously seen training samples may not be available at the time of retraining. We propose an efficient training methodology and incrementally growing a DCNN to allow new classes to be learned while sharing part of the base network. Our proposed methodology is inspired by transfer learning techniques, although it does not forget previously learned classes. An updated network for learning new set of classes is formed using previously learned convolutional layers (shared from initial part of base network) with addition of few newly added convolutional kernels included in the later layers of the network. We evaluated the proposed scheme on several recognition applications. The classification accuracy achieved by our approach is comparable to the regular incremental learning approach (where networks are updated with new training samples only, without any network sharing).

## item_id: m_3634

TITLE: Learning To Simulate

ABSTRACT: Simulation is a useful tool in situations where training data for machine learning models is costly to annotate or even hard to acquire. In this work, we propose a reinforcement learning-based method for automatically adjusting the parameters of any (non-differentiable) simulator, thereby controlling the distribution of synthesized data in order to maximize the accuracy of a model trained on that data. In contrast to prior art that hand-crafts these simulation parameters or adjusts only parts of the available parameters, our approach fully controls the simulator with the actual underlying goal of maximizing accuracy, rather than mimicking the real data distribution or randomly generating a large volume of data. We find that our approach (i) quickly converges to the optimal simulation parameters in controlled experiments and (ii) can indeed discover good sets of parameters for an image rendering simulator in actual computer vision applications.

## item_id: m_3635

TITLE: Meta-Learning by Hallucinating Useful Examples

ABSTRACT: Learning to hallucinate additional examples has recently been shown as a promising direction to address few-shot learning tasks, which aim to learn novel concepts from very few examples. The hallucination process, however, is still far from generating effective samples for learning. In this work, we investigate two important requirements for the hallucinator --- (i) precision: the generated examples should lead to good classifier performance, and (ii) collaboration: both the hallucinator and the classification component need to be trained jointly. By integrating these requirements as novel loss functions into a general meta-learning with hallucination framework, our model-agnostic PrecisE Collaborative hAlluciNator (PECAN) facilitates data hallucination to improve the performance of new classification tasks. Extensive experiments demonstrate state-of-the-art performance on competitive miniImageNet and ImageNet based few-shot benchmarks in various scenarios.

## item_id: m_3636

TITLE: ENHANCING THE PRIVACY OF FEDERATED LEARNING THROUGH DATA SYNTHESIS

ABSTRACT: Federated Learning (FL) is a distributed machine learning architecture where edge devices collaboratively learn the shared model, while the training data is securely held at the edge devices. FL promises a way forward to preserving data privacy by sending model updates in the form of gradients or the weights themselves. However, these updates still contain the essence of the original training data and can be
reconstructed using gradient-based attacks. To overcome this, we propose a novel Privacy-Preserving Federated Learning algorithm (PPFed) wherein we generate a condensed dataset from the original training data at each edge device. The client’s then train their local models on the condensed dataset which is then broadcasted to the server, followed by regular federated averaging. Our method provides privacy by being robust against gradient-based attacks, which holds across different benchmark datasets and CNN based architectures

## item_id: m_3637

TITLE: Inference of unobserved event streams with neural Hawkes particle smoothing

ABSTRACT: Events that we observe in the world may be caused by other, unobserved events. We consider sequences of discrete events in continuous time. When only some of the events are observed, we propose particle smoothing to infer the missing events. Particle smoothing is an extension of particle filtering in which proposed events are conditioned on the future as well as the past. For our setting, we develop a novel proposal distribution that is a type of continuous-time bidirectional LSTM. We use the sampled particles in an approximate minimum Bayes risk decoder that outputs a single low-risk prediction of the missing events. We experiment in multiple synthetic and real domains, modeling the complete sequences in each domain with a neural Hawkes process (Mei & Eisner, 2017). On held-out incomplete sequences, our method is effective at inferring the ground-truth unobserved events. In particular, particle smoothing consistently improves upon particle filtering, showing the benefit of training a bidirectional proposal distribution.

## item_id: m_3638

TITLE: CoGANs: Collaborative Generative Adversarial Networks

ABSTRACT: In complex creative scenarios, co-creativity by multiple agents offer great advantages. Each agent has a specific skill set and a set of abilities, which is sometimes not enough to perform a general, large and complex task single-handed.
These kinds of tasks benefit substantially from collaboration. In deep learning applications, data generation is an example of such a complex, potentially multi-modal task. Previous Generative Adversarial Networks (GANs) focused on using a single generator to generate multi-modal datasets, which is sometimes known to face issues such as mode-collapse and failure to converge. The multi-generator based works such as MGAN, MMGAN, MADGAN and AdaGAN either require training a classifier online, the use of complex mixture models or sequentially adding generators, which is computationally complex.
  In this work, we present a simple, novel approach of training collaborative GANs (CoGAN), with multiple generators and a single critic/discriminator, without introducing external complexities such as a classifier model. We show that this method of workload division meets the state-of-the-art quality metrics, and makes GAN training robust. We present a proof-of-concept on the MNIST dataset, which has 10 modes of data. The individual generators learn to generate different digits from the distribution, and together learn to generate the whole distribution. We introduce a new component to the generator loss during GAN training, based on the Total Variation Distance (TVD) and show that it significantly improves stability during training and performance over state-of-the-art single generator GANs.

## item_id: m_3639

TITLE: CrIBo: Self-Supervised Learning via Cross-Image Object-Level Bootstrapping

ABSTRACT: Leveraging nearest neighbor retrieval for self-supervised representation learning has proven beneficial with object-centric images. However, this approach faces limitations when applied to scene-centric datasets, where multiple objects within an image are only implicitly captured in the global representation. Such global bootstrapping can lead to undesirable entanglement of object representations. Furthermore, even object-centric datasets stand to benefit from a finer-grained bootstrapping approach. In response to these challenges, we introduce a novel $\textbf{Cr}$oss-$\textbf{I}$mage Object-Level $\textbf{Bo}$otstrapping method tailored to enhance dense visual representation learning. By employing object-level nearest neighbor bootstrapping throughout the training, CrIBo emerges as a notably strong and adequate candidate for in-context learning, leveraging nearest neighbor retrieval at test time. CrIBo shows state-of-the-art performance on the latter task while being highly competitive in more standard downstream segmentation tasks. Our code and pretrained models are publicly available at https://github.com/tileb1/CrIBo.

## item_id: m_3640

TITLE: Towards Enhanced Image Generation via Multi-Modal Chain of Thought in Unified Generative Models

ABSTRACT: Unified generative models have shown remarkable performance in both text and image generation. When faced with image synthesis tasks, they adopt straightforward text-to-image (T2I) generation. However, we find that direct T2I generation limits unified generative models in handling complex compositional instructions. Such instructions frequently occur in realistic application scenarios. Although this is a vital issue, existing works predominantly focus on improving the basic image generation capability of unified generative models. While improvements in basic image generation can contribute to complex image generation to some extent, they still fail to adequately resolve the problem. Inspired by Chain of Thought (CoT) solving complex problems in a step-by-step manner, this work aims to introduce CoT into unified generative models to address the challenges of complex image generation that direct T2I generation cannot effectively solve, thereby endowing models with enhanced image generation ability. To achieve this, we first introduce Functionality-oriented eXperts (FoXperts), an expert-parallel architecture in our model FoX, which assigns experts based on function. In this way, FoXperts disentangles the potential conflicts in current mainstream modality-oriented designs and provide a sound foundation for CoT. When introducing CoT, the first question is how to design a CoT approach specifically for complex image generation. To this end, we emulate a human-like artistic workflow---planning, acting, reflection, and correction---and propose the Multimodal Chain of Thought (MCoT) approach, since the data here involves multiple modalities (text and image). In response to the subsequent challenge---how to design an effective MCoT training paradigm---we develop a multi-task joint training paradigm that equips the model with all capabilities required for each MCoT step in a disentangled manner. This paradigm overcomes the difficulty and impracticality of collecting consistent multi-step data tuples for training. Extensive experiments demonstrate that FoX consistently outperforms existing unified models on various T2I benchmarks, delivering notable quantitative improvements in complex image generation.

## item_id: m_3641

TITLE: Do recent advancements in model-based deep reinforcement learning really improve data efficiency?

ABSTRACT: Reinforcement learning (RL) has seen great advancements in the past few years. Nevertheless, the consensus among the RL community is that currently used model-free methods, despite all their benefits, suffer from extreme data inefficiency. To circumvent this problem, novel model-based approaches were introduced that often claim to be much more efficient than their model-free counterparts. In this paper, however, we demonstrate that the state-of-the-art model-free Rainbow DQN algorithm can be trained using a much smaller number of samples than it is commonly reported. By simply allowing the algorithm to execute network updates more frequently we manage to reach similar or better results than existing model-based techniques, at a fraction of complexity and computational costs. Furthermore, based on the outcomes of the study, we argue that the agent similar to the modified Rainbow DQN that is presented in this paper should be used as a baseline for any future work aimed at improving sample efficiency of deep reinforcement learning.

## item_id: m_3642

TITLE: Parameterizing Activation Functions for Adversarial Robustness

ABSTRACT: Deep neural networks are known to be vulnerable to adversarially perturbed inputs.  A commonly used defense is adversarial training, whose performance is influenced by model capacity.  While previous works have studied the impact of varying model width and depth on robustness, the impact of increasing capacity by using learnable parametric activation functions (PAFs) has not been studied. We study how using learnable PAFs can improve robustness in conjunction with adversarial training.  We first ask the question: how should we incorporate parameters into activation functions to improve robustness?  To address this, we analyze the direct impact of activation shape on robustness through PAFs and observe that activation shapes with positive outputs on negative inputs and with high finite curvature can increase robustness.  We combine these properties to create a new PAF, which we call Parametric Shifted Sigmoidal Linear Unit (PSSiLU).   We then combine PAFs (including PReLU, PSoftplus and PSSiLU) with adversarial training and analyze robust performance.  We find that PAFs optimize towards activation shape properties found to directly affect robustness.  Additionally, we find that while introducing only 1-2 learnable parameters into the network, smooth PAFs can significantly increase robustness over ReLU.  For instance, when trained on CIFAR-10 with additional synthetic data, PSSiLU improves robust accuracy by 4.54% over ReLU on ResNet-18 and 2.69% over ReLU on WRN-28-10 in the $\ell_{\infty}$ threat model while adding only 2 additional parameters into the network architecture.   The PSSiLU WRN-28-10 model achieves 61.96% AutoAttack accuracy, improving over the state-of-the-art robust accuracy on RobustBench (Croce et. al, 2020).  Overall, our work puts into context the importance of activation functions in adversarially trained models.

## item_id: m_3643

TITLE: Learning Reasoning Paths over Semantic Graphs for Video-grounded Dialogues

ABSTRACT: Compared to traditional visual question answering, video-grounded dialogues require additional reasoning over dialogue context to answer questions in a multi-turn setting. Previous approaches to video-grounded dialogues mostly use dialogue context as a simple text input without modelling the inherent information flows at the turn level. In this paper, we propose a novel framework of Reasoning Paths in Dialogue Context (PDC). PDC model discovers information flows among dialogue turns through a semantic graph constructed based on lexical components in each question and answer. PDC model then learns to predict reasoning paths over this semantic graph. Our path prediction model predicts a path from the current turn through past dialogue turns that contain additional visual cues to answer the current question. Our reasoning model sequentially processes both visual and textual information through this reasoning path and the propagated features are used to generate the answer. Our experimental results demonstrate the effectiveness of our method and provide additional insights on how models use semantic dependencies in a dialogue context to retrieve visual cues.

## item_id: m_3644

TITLE: Few-Shot Multi-task Learning via Implicit regularization

ABSTRACT: Modern machine learning is highly data-intensive. Few-shot learning (FSL) aims to resolve this sample efficiency problem by learning from multiple tasks and quickly adapt to new tasks containing only a few samples. However,  FSL problems proves to be significantly more challenging and require more compute expensive process to optimize. In this work, we consider multi-task linear regression (MTLR) as a canonical problem for few-shot learning, and investigate the source of challenge of FSL. We find that the MTLR exhibits local minimum problems that are not present in single-task problem, and thus making the learning much more challenging. We also show that the problem can be resolved by  overparameterizing the  model by increasing both the width and depth of the linear network and initializing the weights with small values, exploiting the implicit regularization bias of gradient descent-based learning.  

## item_id: m_3645

TITLE: Towards Understanding the Invertibility of Convolutional Neural Networks

ABSTRACT: Several recent works have empirically observed that Convolutional Neural Nets (CNNs) are (approximately) invertible. To understand this approximate invertibility phenomenon and how to leverage it more effectively, we focus on a theoretical explanation and develop a mathematical model of sparse signal recovery that is consistent with CNNs with random weights. We give an exact connection to a particular model of model-based compressive sensing (and its recovery algorithms) and random-weight CNNs. We show empirically that several learned networks are consistent with our mathematical analysis and then demonstrate that with such a simple theoretical framework, we can obtain reasonable reconstruction results on real images. We also discuss gaps between our model assumptions and the CNN trained for classification in practical scenarios.

## item_id: m_3646

TITLE: Transformer Is Inherently a Causal Learner

ABSTRACT: We reveal that transformers trained in an autoregressive manner  naturally encode time-delayed causal structures in their learned representations. When predicting future values in multivariate time series, the gradient sensitivities of transformer outputs with respect to past inputs directly recover the underlying causal graph, without any explicit causal objectives or structural constraints. We prove this connection theoretically under standard identifiability conditions and develop a practical extraction method using aggregated gradient attributions. On challenging cases such as nonlinear dynamics, long-term dependencies and non-stationary systems, we see this approach greatly surpass the performance of state-of-the-art discovery algorithms, especially as data heterogeneity increases, exhibiting scaling potential where causal accuracy improves with data volume, a property traditional methods lack. This unifying view opens a new paradigm where causal discovery operates through the lens of foundation models, and foundation models gain interpretability and enhancement through the lens of causality.

## item_id: m_3647

TITLE: Stochastic Adversarial Networks for Multi-Domain Text Classification

ABSTRACT: Adversarial training has played a pivotal role in the significant advancements of multi-domain text classification (MDTC). Recent MDTC methods often adopt the shared-private paradigm, wherein a shared feature extractor captures domain-invariant knowledge, while private feature extractors per domain extract domain-dependent knowledge. These approaches have demonstrated state-of-the-art performance. However, a major challenge remains: the exponential increase in model parameters as new domains emerge. To address this challenge, we propose the Stochastic Adversarial Network (SAN), which models multiple domain-specific feature extractors as a multivariate Gaussian distribution rather than weight vectors. With SAN, we can sample as many domain-specific feature extractors as necessary without drastically increasing the number of model parameters. Consequently, the model size of SAN remains comparable to having a single domain-specific feature extractor when data from multiple domains. Additionally, we incorporate domain label smoothing and robust pseudo-label regularization techniques to enhance the stability of the adversarial training and improve feature discriminability, respectively. The evaluations conducted on two prominent MDTC benchmarks validate the competitiveness of our proposed SAN method against state-of-the-art approaches.

## item_id: m_3648

TITLE: A Self-Supervised Method for Mapping Human Instructions to Robot Policies

ABSTRACT: In this paper, we propose a modular approach which separates the instruction-to-action mapping procedure into two separate stages. The two stages are bridged via an intermediate representation called a goal, which stands for the result after a robot performs a specific task. 
The first stage maps an input instruction to a goal, while the second stage maps the goal to an appropriate policy selected from a set of robot policies.  The policy is selected with an aim to guide the robot to reach the goal as close as possible.  We implement the above two stages as a framework consisting of two distinct modules: an instruction-goal mapping module and a goal-policy mapping module.  Given a human instruction in the evaluation phase, the instruction-goal mapping module first translates the instruction to a robot-interpretable goal.  Once a goal is derived by the instruction-goal mapping module, the goal-policy mapping module then follows up to search through the goal-policy pairs to look for policy to be mapped by the instruction.  Our experimental results show that the proposed method is able to learn an effective instruction-to-action mapping procedure in an environment with a given instruction set more efficiently than the baselines.   In addition to the impressive data-efficiency, the results also show that our method can be adapted to a new instruction set and a new robot action space much faster than the baselines.  The evidence suggests that our modular approach does lead to better adaptability and efficiency.  

## item_id: m_3649

TITLE: Efficient Planning with Latent Diffusion

ABSTRACT: Temporal abstraction and efficient planning pose significant challenges in offline reinforcement learning, mainly when dealing with domains that involve temporally extended tasks and delayed sparse rewards. Existing methods typically plan in the raw action space and can be inefficient and inflexible. Latent action spaces offer a more flexible approach, capturing only possible actions within the behavior policy support and decoupling the temporal structure between planning and modeling. However, current latent-action-based methods are limited to discrete spaces and require expensive planning steps. This paper presents a unified framework for continuous latent action space representation learning and planning by leveraging latent, score-based diffusion models. We establish the theoretical equivalence between planning in the latent action space and energy-guided sampling with a pretrained diffusion model and introduce a novel sequence-level exact sampling method. Our proposed method, $\texttt{LatentDiffuser}$, demonstrates competitive performance on low-dimensional locomotion control tasks and surpasses existing methods in higher-dimensional tasks.

## item_id: m_3650

TITLE: Learning From Noisy Singly-labeled Data

ABSTRACT: Supervised learning depends on annotated examples, which are taken to be the ground truth. But these labels often come from noisy crowdsourcing platforms, like Amazon Mechanical Turk. Practitioners typically collect multiple labels per example and aggregate the results to mitigate noise (the classic crowdsourcing problem). Given a fixed annotation budget and unlimited unlabeled data, redundant annotation comes at the expense of fewer labeled examples. This raises two fundamental questions: (1) How can we best learn from noisy workers? (2) How should we allocate our labeling budget to maximize the performance of a classifier? We propose a new algorithm for jointly modeling labels and worker quality from noisy crowd-sourced data. The alternating minimization proceeds in rounds, estimating worker quality from disagreement with the current model and then updating the model by optimizing a loss function that accounts for the current estimate of worker quality. Unlike previous approaches, even with only one annotation per example, our algorithm can estimate worker quality. We establish a generalization error bound for models learned with our algorithm and establish theoretically that it's better to label many examples once (vs less multiply) when worker quality exceeds a threshold. Experiments conducted on both ImageNet (with simulated noisy workers) and MS-COCO (using the real crowdsourced labels) confirm our algorithm's benefits. 

## item_id: m_3651

TITLE: Pareto Prompt Optimization

ABSTRACT: Natural language prompt optimization, or prompt engineering, has emerged as a powerful technique to unlock the potential of Large Language Models (LLMs) for various tasks. While existing methods primarily focus on maximizing a single task-specific performance metric for LLM outputs, real-world applications often require considering trade-offs between multiple objectives. In this work, we address this limitation by proposing an effective technique for multi-objective prompt optimization for LLMs. Specifically, we propose **ParetoPrompt**, a reinforcement learning~(RL) method that leverages dominance relationships between prompts to derive a policy model for prompts optimization using preference-based loss functions. By leveraging multi-objective dominance relationships, ParetoPrompt enables efficient exploration of the entire Pareto front without the need for a predefined scalarization of multiple objectives. Our experimental results show that ParetoPrompt consistently outperforms existing algorithms that use specific objective values. ParetoPrompt also yields robust performances when the objective metrics differ between training and testing.

## item_id: m_3652

TITLE: Task-Based Top-Down Modulation Network for Multi-Task-Learning Applications

ABSTRACT: A general problem that received considerable recent attention is how to perform multiple tasks in the same network, maximizing both efficiency and prediction accuracy. A popular approach consists of a multi-branch architecture on top of a
shared backbone, jointly trained on a weighted sum of losses. However, in many cases, the shared representation results in non-optimal performance, mainly due to an interference between conflicting gradients of uncorrelated tasks. Recent approaches address this problem by a channel-wise modulation of the feature-maps along the shared backbone, with task specific vectors, manually or dynamically tuned. Taking this approach a step further, we propose a novel architecture which
modulate the recognition network channel-wise, as well as spatial-wise, with an efficient top-down image-dependent computation scheme. Our architecture uses no task-specific branches, nor task specific modules. Instead, it uses a top-down modulation network that is shared between all of the tasks. We show the effectiveness of our scheme by achieving on par or better results than alternative approaches on both correlated and uncorrelated sets of tasks. We also demonstrate our advantages in terms of model size, the addition of novel tasks and interpretability. 
Code will be released.

## item_id: m_3653

TITLE: Active Automated Machine Learning with Self-Training

ABSTRACT: Automated Machine Learning (AutoML) aims to automatically select and configure machine learning algorithms for optimal performance on given datasets. In real-world applications, training data oftentimes contain a large amount of unlabeled examples, whereas the amount of labeled examples is limited. However, AutoML tools have so far only focused on supervised learning, i.e., utilizing labeled data for training, leaving the valuable information provided by unlabeled data untapped. To address this limitation, we introduce our augmented AutoML system AutoActiveSelf-Labeling (AutoASL), which combines principles from self-training and active learning to effectively leverage unlabeled data during the training process. AutoASL iteratively self-labels previously unlabeled data instances, which is achieved through a powerful ensemble of AutoML and traditional ML algorithms, resulting in a substantial expansion of the labeled training data. We observe synergetic effects between the incorporated self-training and active learning components, leading to an improvement of the overall accuracy compared to state-of-the-art tools.

## item_id: m_3654

TITLE: C-Learning: Horizon-Aware Cumulative Accessibility Estimation

ABSTRACT: Multi-goal reaching is an important problem in reinforcement learning needed to achieve algorithmic generalization. Despite recent advances in this field, current algorithms suffer from three major challenges: high sample complexity, learning only a single way of reaching the goals,  and difficulties in solving complex motion planning tasks. In order to address these limitations, we introduce the concept of cumulative accessibility functions, which measure the reachability of a goal from a given state within a specified horizon. We show that these functions obey a recurrence relation, which enables learning from offline interactions. We also prove that optimal cumulative accessibility functions are monotonic in the planning horizon. Additionally, our method can trade off speed and reliability in goal-reaching by suggesting multiple paths to a single goal depending on the provided horizon. We evaluate our approach on a set of multi-goal discrete and continuous control tasks. We show that our method outperforms state-of-the-art goal-reaching algorithms in success rate, sample complexity, and path optimality. Our code is available at https://github.com/layer6ai-labs/CAE, and additional visualizations can be found at https://sites.google.com/view/learning-cae/.

## item_id: m_3655

TITLE: Discrete-Valued Neural Networks Using Variational Inference

ABSTRACT: The increasing demand for neural networks (NNs) being employed on embedded devices has led to plenty of research investigating methods for training low precision NNs. While most methods involve a quantization step, we propose a principled Bayesian approach where we first infer a distribution over a discrete weight space from which we subsequently derive hardware-friendly low precision NNs. To this end, we introduce a probabilistic forward pass to approximate the intractable variational objective that allows us to optimize over discrete-valued weight distributions for NNs with sign activation functions. In our experiments, we show that our model achieves state of the art performance on several real world data sets. In addition, the resulting models exhibit a substantial amount of sparsity that can be utilized to further reduce the computational costs for inference.

## item_id: m_3656

TITLE: Deep Variational Semi-Supervised Novelty Detection

ABSTRACT: In anomaly detection (AD), one seeks to identify whether a test sample is abnormal,  given a data set of normal samples.   A recent and promising approach to AD relies on deep generative models, such as variational autoencoders (VAEs),for unsupervised learning of the normal data distribution. In semi-supervised AD (SSAD), the data also includes a small sample of labeled anomalies. In this work,we propose two variational methods for training VAEs for SSAD. The intuitive idea in both methods is to train the encoder to ‘separate’ between latent vectors for normal and outlier data. We show that this idea can be derived from principled probabilistic formulations of the problem, and propose simple and effective algorithms.  Our methods can be applied to various data types, as we demonstrate on SSAD datasets ranging from natural images to astronomy and medicine, and can be combined with any VAE model architecture. When comparing to state-of-the-art SSAD methods that are not specific to particular data types, we obtain marked improvement in outlier detection.

## item_id: m_3657

TITLE: A Theory for Token-Level Harmonization in Retrieval-Augmented Generation

ABSTRACT: Retrieval-augmented generation (RAG) utilizes retrieved texts to enhance large language models (LLMs). Studies show that while RAG provides valuable external information (benefit), it may also mislead LLMs (detriment) with noisy or incorrect retrieved texts. Although many existing methods attempt to preserve benefit and avoid detriment, they lack a theoretical explanation for RAG. The benefit and detriment in the next token prediction of RAG remain a 'black box' that cannot be quantified or compared in an explainable manner, so existing methods are data-driven, need additional utility evaluators or post-hoc. This paper takes the first step towards providing a theory to explain and trade off the benefit and detriment in RAG. We model RAG as the fusion between distributions of LLMs’ knowledge and distributions of retrieved texts. Then, we formalize the trade-off between the value of external knowledge (benefit) and its potential risk of misleading LLMs (detriment) in next token prediction of RAG by distribution difference in this fusion. Finally, we prove that the actual effect of RAG on the token, which is the comparison between benefit and detriment, can be predicted without any training or accessing the utility of retrieval. Based on our theory, we propose a practical novel method, Tok-RAG, which achieves collaborative generation between the pure LLM and RAG at token level to preserve benefit and avoid detriment. Experiments in real-world tasks using LLMs such as OPT, LLaMA-2, and Mistral show the effectiveness of our method and support our theoretical findings. Code is in supplemental material and will be released on GitHub after acceptance.

## item_id: m_3658

TITLE: Navigating the Latent Space Dynamics of Neural Models

ABSTRACT: Neural networks transform high-dimensional data into compact, structured representations, often modeled as elements of a lower dimensional latent space. In this paper, we present an alternative interpretation of neural models as dynamical systems acting on the latent manifold. Specifically, we show that autoencoder models implicitly define a _latent vector field_ on the manifold, derived by iteratively applying the encoding-decoding map, without any additional training. We observe that standard training procedures introduce inductive biases that lead to the emergence of attractor points within this vector field.
Drawing on this insight, we propose to leverage the vector field as a _representation_ for the network, providing a novel tool to analyze the properties of the model and the data. This representation enables to: $(i)$ analyze the generalization and memorization regimes of neural models, even throughout training; $(ii)$ extract prior knowledge encoded in the network's parameters from the attractors, without requiring any input data; $(iii)$ identify out-of-distribution samples from their trajectories in the vector field.
We further validate our approach on vision foundation models, showcasing the applicability and effectiveness of our method in real-world scenarios.

## item_id: m_3659

TITLE: The magnitude vector of images

ABSTRACT: The magnitude of a finite metric space is a recently-introduced invariant quantity. Despite beneficial theoretical and practical properties, such as a general utility for outlier detection, and a close connection to Laplace radial basis kernels, magnitude has received little attention by the machine learning community so far. In this work, we investigate the properties of magnitude on individual images, with each image forming its own metric space. We show that the known properties of outlier detection translate to edge detection in images and we give supporting theoretical justifications. In addition, we provide a proof of concept of its utility by using a novel magnitude layer to defend against adversarial attacks. Since naive magnitude calculations may be computationally prohibitive, we introduce an algorithm that leverages the regular structure of images to dramatically reduce the computational cost.

## item_id: m_3660

TITLE: The Differentiable Cross-Entropy Method

ABSTRACT: We study the Cross-Entropy Method (CEM) for the non-convex optimization of a continuous and parameterized objective function and introduce a differentiable variant (DCEM) that enables us to differentiate the output of CEM with respect to the objective function's parameters. In the machine learning setting this brings CEM inside of the end-to-end learning pipeline in cases this has otherwise been impossible. We show applications in a synthetic energy-based structured prediction task and in non-convex continuous control. In the control setting we show on the simulated cheetah and walker tasks that we can embed their optimal action sequences with DCEM and then use policy optimization to fine-tune components of the controller as a step towards combining model-based and model-free RL.

## item_id: m_3661

TITLE: SampleRNN: An Unconditional End-to-End Neural Audio Generation Model

ABSTRACT: In this paper we propose a novel model for unconditional audio generation task that generates one audio sample at a time. We show that our model which profits from combining memory-less modules, namely autoregressive multilayer perceptron, and stateful recurrent neural networks in a hierarchical structure is de facto powerful to capture the underlying sources of variations in temporal domain for very long time on three datasets of different nature. Human evaluation on the generated samples indicate that our model is preferred over competing models. We also show how each component of the model contributes to the exhibited performance.

## item_id: m_3662

TITLE: Online Structure Learning for Sum-Product Networks with Gaussian Leaves

ABSTRACT: Sum-product networks have recently emerged as an attractive representation due to their dual view as a special type of deep neural network with clear semantics and a special type of probabilistic graphical model for which inference is always tractable. Those properties follow from some conditions (i.e., completeness and decomposability) that must be respected by the structure of the network.  As a result, it is not easy to specify a valid sum-product network by hand and therefore structure learning techniques are typically used in practice.  This paper describes the first {\em online} structure learning technique for continuous SPNs with Gaussian leaves. We also introduce an accompanying new parameter learning technique.

## item_id: m_3663

TITLE: Automatic Rule Extraction from Long Short Term Memory Networks

ABSTRACT: Although deep learning models have proven effective at solving problems in natural language processing, the mechanism by which they come to their conclusions is often unclear.   As a result, these models are generally treated as black boxes, yielding no insight of the underlying learned patterns.  In this paper we consider Long Short Term Memory networks (LSTMs) and demonstrate a new approach for tracking the importance of a given input to the LSTM for a given output. By identifying consistently important patterns of words, we are able to distill state of the art LSTMs on sentiment analysis and question answering into a set of representative phrases. This representation is then quantitatively validated by using the extracted phrases to construct a simple, rule-based classifier which approximates the output of the LSTM.

## item_id: m_3664

TITLE: Private GANs, Revisited

ABSTRACT: We show that with improved training, the standard approach for differentially private GANs -- updating the discriminator with noisy gradients -- achieves or competes with state-of-the-art results for private image synthesis. Existing instantiations of this approach neglect to consider how adding noise only to discriminator updates disrupts the careful balance between generator and discriminator necessary for successful GAN training. We show that a simple fix restores parity: taking more discriminator steps between generator steps. Finally, with the goal of restoring parity between generator and discriminator, we experiment with further modifications to improve discriminator training and see further improvements. For MNIST at $\eps=10$, our private GANs improve the record FID from 48.4 to 13.0, as well as downstream classifier accuracy from 83.2\% to 95.0\%.

## item_id: m_3665

TITLE: Cooperate or Compete: A New Perspective on Training of Generative Networks

ABSTRACT: GANs have two competing modules: the generator module is trained to generate new examples, and the discriminator module is trained to discriminate real examples from generated examples. The training procedure of GAN is modeled as a finitely repeated simultaneous game. Each module tries to increase its performance at every repetition of the base game (at every batch of training data) in a non-cooperative manner. We observed that each module can perform better and learn faster if training is modeled as an infinitely repeated simultaneous game. At every repetition of the base game (at every batch of training data) the stronger module (whose performance is increased or remains the same compared to the previous batch of training data) cooperates with the weaker module (whose performance is decreased compared to the previous batch of training data) and only the weaker module is allowed to increase its performance. 

## item_id: m_3666

TITLE: SemanticAdv: Generating Adversarial Examples via Attribute-Conditional Image Editing

ABSTRACT: Deep neural networks (DNNs) have achieved great success in various applications due to their strong expressive power. However, recent studies have shown that DNNs are vulnerable to adversarial examples which are manipulated instances targeting to mislead DNNs to make incorrect predictions. Currently, most such adversarial examples try to guarantee “subtle perturbation" by limiting the Lp norm of the perturbation. In this paper, we aim to explore the impact of semantic manipulation on DNNs predictions by manipulating the semantic attributes of images and generate “unrestricted adversarial examples". Such semantic based perturbation is more practical compared with the Lp bounded perturbation. In particular, we propose an algorithm SemanticAdv which leverages disentangled semantic factors to generate adversarial perturbation by altering controlled semantic attributes to fool the learner towards various “adversarial" targets. We conduct extensive experiments to show that the semantic based adversarial examples can not only fool different learning tasks such as face verification and landmark detection, but also achieve high targeted attack success rate against real-world black-box services such as Azure face verification service based on transferability. To further demonstrate the applicability of SemanticAdv beyond face recognition domain, we also generate semantic perturbations on street-view images. Such adversarial examples with controlled semantic manipulation can shed light on further understanding about vulnerabilities of DNNs as well as potential defensive approaches.

## item_id: m_3667

TITLE: Search and Retrieval in Semantic-Structural Representations of Novel Malware

ABSTRACT: In this study we present a novel representation for binary programs, which captures semantic similarity and structural properties.  Our representation is composed in a bottom-up approach and enables new methods of analysis.  We show that we can perform search and retrieval of binary executable programs based on similarity of behavioral properties, with an adjustable level of feature resolution.  We begin by extracting data dependency graphs (DDG), which are representative of both program structure and operational semantics.  We then encode each program as a set of graph hashes representing isomorphic uniqueness, a method we have labeled DDG Fingerprinting.  Next, we use k-Nearest Neighbors to search in a metric space constructed from examples.  This approach allows us to perform a quantitative analysis of patterns of program operation. By evaluating similarity of behavior we are able to recognize patterns in novel malware with functionality not previously identified.  We present experimental results from search based on program semantics and structural properties in a dataset of binary executables with features extracted using our method of representation.  We show that the associated metric space allows an adjustable level of resolution.  Resolution of the features may be decreased for breadth of search and retrieval, or as the search space is reduced, the resolution may be increased for accuracy and fine-grained analysis of malware behavior.

## item_id: m_3668

TITLE: Fingerprints of Super Resolution Networks

ABSTRACT: Several recent studies have demonstrated that deep-learning based image generation models, such as GANs, can be uniquely identified, and possibly even reverse engineered, by the fingerprints they leave on their output images. We extend this research to a previously unstudied type of image generator: single image super-resolution (SISR) networks. Compared to previously studied models, SISR networks are a uniquely challenging class of image generation model from which to extract and analyze fingerprints, as they can often generate images that closely match the corresponding ground truth and thus likely leave little flexibility to embed signatures. We take SISR models as examples to investigate if the findings from the previous work on fingerprints of GAN-based networks are valid for general image generation models. In this paper, we present an analysis of the capabilities and limitations of model fingerprinting in this domain. We show that SISR networks with a high upscaling factor or trained using adversarial loss leave highly distinctive fingerprints, and show promising results for reverse engineering some hyperparameters of SISR networks, including scale and loss function.

## item_id: m_3669

TITLE: Memory Architectures in Recurrent Neural Network Language Models

ABSTRACT: We compare and analyze sequential, random access, and stack memory architectures for recurrent neural network language models. Our experiments on the Penn Treebank and Wikitext-2 datasets show that stack-based memory architectures consistently achieve the best performance in terms of held out perplexity. We also propose a generalization to existing continuous stack models (Joulin & Mikolov,2015; Grefenstette et al., 2015)  to allow a variable number of pop operations more naturally that further improves performance. We further evaluate these language models in terms of their ability to capture non-local syntactic dependencies on a subject-verb agreement dataset  (Linzen et al., 2016) and establish new state of the art results using memory augmented language models. Our results demonstrate the value of stack-structured memory for explaining the distribution of words in natural language, in line with linguistic theories claiming a context-free backbone for natural language.

## item_id: m_3670

TITLE: Synthesizing Programmatic Policy for Domain Generalization

ABSTRACT: Deep reinforcement learning has effectively addressed numerous complex control tasks. 
However, when the environment undergoes changes, such as increasing the number of discs from three to four in the `Tower of Hanoi', learned policies often struggle with generalization. 
We propose an algorithm for learning programmatic policies capable of capturing environment variations. 
In doing so, these policies gain the capability to generalize to instances where certain aspects of the domain exhibit variations, a property we term domain generalization.
We design a Domain Specific Language to construct the structure of the policy.
Through sampling tasks from a task distribution, we can train the policy with a meta-learning algorithm.
Furthermore, our approach incorporates Recurrent Neural Network (RNN) into the structure of the programmatic policy to enhance agent-environment interactions.
Experiment results demonstrate the efficiency of our approach across three environments with domain generalization. 
In addition, the learned policy shows its ability to generalize to tasks under different variations of environments.

## item_id: m_3671

TITLE: Self-Organizing Visual Embeddings for Non-Parametric Self-Supervised Learning

ABSTRACT: We present Self-Organizing Visual Embeddings (SOVE) a new training technique for unsupervised representation learning.
SOVE avoids learning prototypes from scratch and explores relationships between visual embeddings in a non-parametric space.
Unlike existing clustering-based techniques that employ a single prototype to encode all the relevant features of a complex concept, we propose the SOVE method where a concept is represented by many semantically similar representations, or judges, each containing a complement set of features that together can fully characterize the concept and maximize training performance.
We reaffirm the feasibility of non-parametric self-supervised learning (SSL) by introducing novel non-parametric adaptions of two loss functions with the SOVE technique: (1) non-parametric cluster assignment prediction for class-level representations and (2) non-parametric Masked Image Modeling (MIM) for patch-level reconstruction.
SOVE achieves state-of-the-art performance on many downstream benchmarks, including transfer learning, image retrieval, object detection, and segmentation.
Moreover, SOVE demonstrates scaling performance when trained with Vision Transformers (ViTs), showing increased performance gains as more complex encoders are employed.

## item_id: m_3672

TITLE: $i$-Mix: A Domain-Agnostic Strategy for Contrastive Representation Learning

ABSTRACT: Contrastive representation learning has shown to be effective to learn representations from unlabeled data. However, much progress has been made in vision domains relying on data augmentations carefully designed using domain knowledge. In this work, we propose i-Mix, a simple yet effective domain-agnostic regularization strategy for improving contrastive representation learning. We cast contrastive learning as training a non-parametric classifier by assigning a unique virtual class to each data in a batch. Then, data instances are mixed in both the input and virtual label spaces, providing more augmented data during training. In experiments, we demonstrate that i-Mix consistently improves the quality of learned representations across domains, including image, speech, and tabular data. Furthermore, we confirm its regularization effect via extensive ablation studies across model and dataset sizes. The code is available at https://github.com/kibok90/imix.

## item_id: m_3673

TITLE: Learning to Generate Grounded Visual Captions without Localization Supervision

ABSTRACT: When automatically generating a sentence description for an image or video, it often remains unclear how well the generated caption is grounded, or if the model hallucinates based on priors in the dataset and/or the language model. The most common way of relating image regions with words in caption models is through an attention mechanism over the regions that are used as input to predict the next word. The model must therefore learn to predict the attentional weights without knowing the word it should localize. This is difficult to train without grounding supervision since recurrent models can propagate past information and there is no explicit signal to force the captioning model to properly ground the individual decoded words. In this work, we help the model to achieve this via a novel cyclical training regimen that forces the model to localize each word in the image after the sentence decoder generates it, and then reconstruct the sentence from the localized image region(s) to match the ground-truth. Our proposed framework only requires learning one extra fully-connected layer (the localizer), a layer that can be removed at test time. We show that our model significantly improves grounding accuracy without relying on grounding supervision or introducing extra computation during inference for both image and video captioning tasks.

## item_id: m_3674

TITLE: MAT: Mixed-Strategy Game of  Adversarial Training in Fine-tuning

ABSTRACT: Fine-tuning large-scale models from pre-trained checkpoints has been demonstrated effective for various natural language processing (NLP) tasks. Previous works reveal that leveraging adversarial training methods during the fine-tuning stage significantly enhances the generalization and robustness of the models. However, from the perspective of optimization, the previous adversarial training methods suffer from converging onto local optima due to the non-convexity of the objective. In this work, we reformulate the adversarial training in the view of mixed strategy in game theory and incorporate full strategy space to avoid trapping in local stationarity. Methodologically, we derive the Nash equilibrium of mixed-strategy for adversarial training using entropy mirror descent to establish a novel mixed-strategy adversarial training algorithm (MAT). Numerically, to verify the effectiveness of MAT, we conducted extensive benchmark experiments over the large-scale pre-trained models such as BERT and RoBERTa. The experimental results show that MAT outperforms the previous state-of-the-art on both GLUE and ANLI benchmarks in terms of generalization and robustness.

## item_id: m_3675

TITLE: Benchmarking Algorithms for Domain Generalization in Federated Learning

ABSTRACT: In this paper, we present a unified platform to study domain generalization in the federated learning (FL) context and conduct extensive empirical evaluations of the current state-of-the-art domain generalization algorithms adapted to FL. In particular, we perform a fair comparison of nine existing algorithms in solving domain generalization {either centralized domain generalization algorithms adapted to the FL context or existing FL domain generalization algorithms } to comprehensively explore the challenges introduced by FL. These challenges include statistical heterogeneity among clients, the number of clients, the number of communication rounds, etc. The evaluations are conducted on three diverse datasets including PACS (image dataset covering photo, sketch, cartoon, and painting domains), iWildCam (image dataset with 323 domains), and Py150 (natural language processing dataset with 8421 domains). The experiments show that the challenges brought by federated learning stay unsolved in the realistic experiment setting. Furthermore, the code base supports fair and reproducible new algorithm evaluation with easy implementation.

## item_id: m_3676

TITLE: Near-Optimal Regret Bounds for Model-Free RL in Non-Stationary Episodic MDPs

ABSTRACT: We consider model-free reinforcement learning (RL) in non-stationary Markov decision processes (MDPs). Both the reward functions and the state transition distributions are allowed to vary over time, either gradually or abruptly, as long as their cumulative variation magnitude does not exceed certain budgets. We propose an algorithm, named Restarted Q-Learning with Upper Confidence Bounds (RestartQ-UCB), for this setting, which adopts a simple restarting strategy and an extra optimism term. Our algorithm outperforms the state-of-the-art (model-based) solution in terms of dynamic regret. Specifically, RestartQ-UCB with Freedman-type bonus terms achieves a dynamic regret of $\widetilde{O}(S^{\frac{1}{3}} A^{\frac{1}{3}} \Delta^{\frac{1}{3}} H T^{\frac{2}{3}})$, where $S$ and $A$ are the numbers of states and actions, respectively, $\Delta>0$ is the variation budget, $H$ is the number of steps per episode, and $T$ is the total number of steps. We further show that our algorithm is near-optimal by establishing an information-theoretical lower bound of $\Omega(S^{\frac{1}{3}} A^{\frac{1}{3}} \Delta^{\frac{1}{3}} H^{\frac{2}{3}} T^{\frac{2}{3}})$, which to the best of our knowledge is the first impossibility result in non-stationary RL in general.

## item_id: m_3677

TITLE: Reward Design in Cooperative Multi-agent Reinforcement Learning for Packet Routing

ABSTRACT: In cooperative multi-agent reinforcement learning (MARL), how to design a suitable reward signal to accelerate learning and stabilize convergence is a critical problem. The global reward signal assigns the same global reward to all agents without distinguishing their contributions, while the local reward signal provides different local rewards to each agent based solely on individual behavior. Both of the two reward assignment approaches have some shortcomings: the former might encourage lazy agents, while the latter might produce selfish agents.

In this paper, we study reward design problem in cooperative MARL based on packet routing environments. Firstly, we show that the above two reward signals are prone to produce suboptimal policies. Then, inspired by some observations and considerations, we design some mixed reward signals, which are off-the-shelf to learn better policies. Finally, we turn the mixed reward signals into the adaptive counterparts, which achieve best results in our experiments. Other reward signals are also discussed in this paper. As reward design is a very fundamental problem in RL and especially in MARL, we hope that MARL researchers can rethink the rewards used in their systems.

## item_id: m_3678

TITLE: FlyOrien: A bio-inspired model for incremental learning of object orientation

ABSTRACT: Visual orientation detection helps navigation, especially without a reliable magnetic compass or GPS. Inspired by the neural mechanisms of the insect brain, particularly the mushroom body (MB) and the central complex (CX), we propose FlyOrien—a bio-inspired model for object orientation detection. The model mimics the MB for random feature extraction, sparse coding and associative learning, while the CX provides multi-clue sensory integration, enabling interpolation for finer orientation representation. FlyOrien's biologically plausible learning rule allows one-shot learning, reducing the need for large datasets and repeated training. We tested FlyOrien on a dataset containing images labeled with orientations, which introduce strong interferences because images of the same object have different labels. In this challenging context, FlyOrien achieves competitive performance compared to convolutional neural networks (CNNs), significantly reducing training time and computational resources. It also has the potential for real-world applications like robotics, where incremental learning is essential.

## item_id: m_3679

TITLE: Reasoning with Latent Thoughts: On the Power of Looped Transformers

ABSTRACT: Large language models have shown remarkable reasoning abilities and scaling laws suggest that large parameter count, especially along the depth axis, is the primary driver. In this work, we make a stronger claim --- many reasoning problems require a large depth but not necessarily many parameters. This unlocks a novel application of looped models for reasoning. Firstly, we show that for many synthetic reasoning problems like addition, $p$-hop induction, and math problems, a $k$-layer transformer looped $L$ times nearly matches the performance of a $kL$-layer non-looped model, and is significantly better than a $k$-layer model. This is further corroborated by theoretical results showing that many such reasoning problems can be solved via iterative algorithms, and thus, can be solved effectively using looped models with nearly optimal depth. Perhaps surprisingly, these benefits also translate to practical settings of language modeling --- on many downstream reasoning tasks, a language model with $k$-layers looped $L$ times can be competitive to, if not better than, a $kL$-layer language model. In fact, our empirical analysis reveals an intriguing phenomenon: looped and non-looped models exhibit scaling behavior that depends on their effective depth, akin to the inference-time scaling of chain-of-thought (CoT) reasoning. We further elucidate the connection to CoT reasoning by proving that looped models implicitly generate latent thoughts and can simulate $T$ steps of CoT with $T$ loops. Inspired by these findings, we also present an interesting dichotomy between reasoning and memorization, and design a looping-based regularization that is effective on both fronts.

## item_id: m_3680

TITLE: ELBOing Stein: Variational Bayes with Stein Mixture Inference

ABSTRACT: Stein variational gradient descent (SVGD) (Liu & Wang, 2016) performs approximate Bayesian inference by representing the posterior with a set of particles.
However, SVGD suffers from variance collapse, i.e. poor predictions due to underestimating uncertainty (Ba et al., 2021), even for moderately-dimensional models
such as small Bayesian neural networks (BNNs). To address this issue, we generalize SVGD by letting each particle parameterize a component distribution in
a mixture model. Our method, Stein Mixture Inference (SMI), optimizes a lower
bound to the evidence (ELBO) and introduces user-specified guides parameterized
by particles. SMI extends the Nonlinear SVGD framework (Wang & Liu, 2019) to
the case of variational Bayes. SMI effectively avoids variance collapse, judging by
a previously described test developed for this purpose, and performs well on standard data sets. In addition, SMI requires considerably fewer particles than SVGD
to accurately estimate uncertainty for small BNNs. The synergistic combination of
NSVGD, ELBO optimization and user-specified guides establishes a promising
approach towards variational Bayesian inference in the case of tall and wide data.

## item_id: m_3681

TITLE: Exploring Over-smoothing in Graph Attention Networks from the Markov Chain Perspective

ABSTRACT: The over-smoothing problem causing the depth limitation is an obstacle of developing deep graph neural network (GNN). Compared with Graph Convolutional Networks (GCN), over-smoothing in Graph Attention Network (GAT) has not drawed enough attention. In this work, we analyze the over-smoothing problem in GAT from the Markov chain perspective. First we establish a connection between GAT and a time-inhomogeneous random walk on the graph. Then we show that the GAT is not always over-smoothing using conclusions in the time-inhomogeneous Markov chain. Finally,  we derive a sufficient condition for GAT to avoid over-smoothing based on our findings about the existence of the limiting distribution of the time-inhomogeneous Markov chain. We design experiments to verify our theoretical findings. Results show that our proposed sufficient condition can effectively improve over-smoothing problem in GAT and enhance the performance of the model.

## item_id: m_3682

TITLE: DyST: Towards Dynamic Neural Scene Representations on Real-World Videos

ABSTRACT: Visual understanding of the world goes beyond the semantics and flat structure of individual images. In this work, we aim to capture both the 3D structure and dynamics of real-world scenes from monocular real-world videos. Our Dynamic Scene Transformer (DyST) model leverages recent work in neural scene representation to learn a latent decomposition of monocular real-world videos into scene content, per-view scene dynamics, and camera pose. This separation is achieved through a novel co-training scheme on monocular videos and our new synthetic dataset DySO. DyST learns tangible latent representations for dynamic scenes that enable view generation with separate control over the camera and the content of the scene.

## item_id: m_3683

TITLE: Improving End-to-End Object Tracking Using Relational Reasoning

ABSTRACT: Relational reasoning, the ability to model interactions and relations between objects, is valuable for robust multi-object tracking and pivotal for trajectory prediction. In this paper, we propose MOHART, a class-agnostic, end-to-end multi-object tracking and trajectory prediction algorithm, which explicitly accounts for permutation invariance in its relational reasoning. We explore a number of permutation invariant architectures and show that multi-headed self-attention outperforms the provided baselines and better accounts for complex physical interactions in a challenging toy experiment. We show on three real-world tracking datasets that adding relational reasoning capabilities in this way increases the tracking and trajectory prediction performance, particularly in the presence of ego-motion, occlusions, crowded scenes, and faulty sensor inputs. To the best of our knowledge, MOHART is the first fully end-to-end multi-object tracking from vision approach applied to real-world data reported in the literature. 

## item_id: m_3684

TITLE: Reinforcement Learning with Unsupervised Auxiliary Tasks

ABSTRACT: Deep reinforcement learning agents have achieved state-of-the-art results by directly maximising cumulative reward. However, environments contain a much wider variety of possible training signals. In this paper, we introduce an agent that also maximises many other pseudo-reward functions simultaneously by reinforcement learning. All of these tasks share a common representation that, like unsupervised learning, continues to develop in the absence of extrinsic rewards. We also introduce a novel mechanism for focusing this representation upon extrinsic rewards, so that learning can rapidly adapt to the most relevant aspects of the actual task. Our agent significantly outperforms the previous state-of-the-art on Atari, averaging 880\% expert human performance, and a challenging suite of first-person, three-dimensional \emph{Labyrinth} tasks leading to a mean speedup in learning of 10$\times$ and averaging 87\% expert human performance on Labyrinth.

## item_id: m_3685

TITLE: Multi-timestep models for Model-based Reinforcement Learning

ABSTRACT: In model-based reinforcement learning (MBRL), most algorithms rely on simulating trajectories from one-step dynamics models learned on data. A critical challenge of this approach is the compounding of one-step prediction errors as length of the trajectory grows. In this paper we tackle this issue by using a multi-timestep objective to train one-step models. Our objective is a weighted sum of a loss function (e.g., negative log-likelihood) at various future horizons. We explore and test a range of weights profiles. We find that exponentially decaying weights lead to models that significantly improve the long-horizon R2 score. This improvement is particularly noticeable when the models were evaluated on noisy data. Finally, using a soft actor-critic (SAC) agent in pure batch reinforcement learning (RL) and iterated batch RL scenarios, we found that our multi-timestep models outperform or match standard one-step models. This was especially evident in a noisy variant of the considered environment, highlighting the potential of our approach in real-world applications.

## item_id: m_3686

TITLE: Online Coreset Selection for Rehearsal-based Continual Learning

ABSTRACT: A dataset is a shred of crucial evidence to describe a task. However, each data point in the dataset does not have the same potential, as some of the data points can be more representative or informative than others. This unequal importance among the data points may have a large impact in rehearsal-based continual learning, where we store a subset of the training examples (coreset) to be replayed later to alleviate catastrophic forgetting. In continual learning, the quality of the samples stored in the coreset directly affects the model's effectiveness and efficiency. The coreset selection problem becomes even more important under realistic settings, such as imbalanced continual learning or noisy data scenarios. To tackle this problem, we propose Online Coreset Selection (OCS), a simple yet effective method that selects the most representative and informative coreset at each iteration and trains them in an online manner. Our proposed method maximizes the model's adaptation to a target dataset while selecting high-affinity samples to past tasks, which directly inhibits catastrophic forgetting. We validate the effectiveness of our coreset selection mechanism over various standard, imbalanced, and noisy datasets against strong continual learning baselines, demonstrating that it improves task adaptation and prevents catastrophic forgetting in a sample-efficient manner. 

## item_id: m_3687

TITLE: Attribute Alignment and Enhancement for Generalized Zero-Shot Learning

ABSTRACT: Generalized zero-shot learning (GZSL) aims to recognize both seen and unseen classes, which challenges the generalization ability of a model. In this paper, we propose a novel approach to fully utilize attributes information, referred to as attribute alignment and enhancement (A3E) network. It contains two modules. First, attribute localization (AL) module utilizes the supervision of class attribute vectors to guide visual localization for attributes through the implicit localization capability within the feature extractor, and the visual features corresponding to the attributes (attribute-visual features) are obtained. Second, enhanced attribute scoring (EAS) module employs the supervision of the attribute word vectors (attribute semantics) to project input attribute visual features to attribute semantic space using Graph Attention Network (GAT). Based on the constructed attribute relation graph (ARG), EAS module generates enhanced representation of attributes. Experiments on standard datasets demonstrate that the enhanced attribute representation greatly improves the classification performance, which helps A3E to achieve state-of-the-art performances in both ZSL and GZSL tasks.

## item_id: m_3688

TITLE: ANALYSIS ON GRADIENT PROPAGATION IN BATCH NORMALIZED RESIDUAL NETWORKS

ABSTRACT: We conduct a mathematical analysis on the Batch normalization (BN) effect on gradient backpropagation in residual network training in this work, which is believed to play a critical role in addressing the gradient vanishing/explosion problem. Specifically, by analyzing the mean and variance behavior of the input and the gradient in the forward and backward passes through the BN and residual branches, respectively, we show that they work together to confine the gradient variance to a certain range across residual blocks in backpropagation. As a result, the gradient vanishing/explosion problem is avoided. Furthermore, we use the same analysis to discuss the tradeoff between depth and width of a residual network and demonstrate that shallower yet wider resnets have stronger learning performance than deeper yet thinner resnets.

## item_id: m_3689

TITLE: Gaussian Process Behaviour in Wide Deep Neural Networks

ABSTRACT: Whilst deep neural networks have shown great empirical success, there is still much work to be done to understand their theoretical properties. In this paper, we study the relationship between Gaussian processes with a recursive kernel definition and random wide fully connected feedforward networks with more than one hidden layer. We exhibit limiting procedures under which finite deep networks will converge in distribution to the corresponding Gaussian process. To evaluate convergence rates empirically, we use maximum mean discrepancy. We then exhibit situations where existing Bayesian deep networks are close to Gaussian processes in terms of the key quantities of interest. Any Gaussian process has a flat representation. Since this behaviour may be undesirable in certain situations we discuss ways in which it might be prevented.

## item_id: m_3690

TITLE: Rethinking the Noise Schedule of Diffusion-Based Generative Models

ABSTRACT: In this work, we undertake both theoretical and empirical analysis of noise scheduling strategies within the scope of denoising diffusion generative models. We investigate the training noise schedule through the lens of power spectrum and introduce a novel metric, weighted signal-noise-ratio (WSNR), to uniformly represent the noise level in both RGB and latent spaces, enhancing the performance of high-resolution models in these spaces with WSNR-Equivalent training noise schedules. Further, we examine the reverse sampling process using the framework of Ordinary Differential Equations (ODEs), elucidating the concept of the optimal denoiser and providing insights into data-driven sampling noise schedules. We explore the correlation between the number of evaluation points and the generation quality to optimize the acceleration of the ODE solver in the diffusion model. Based on practical considerations of evaluation point effects, we propose an adaptive scheme to choose numerical methods within computational constraints, balancing efficacy and efficiency. Our approach, requiring no additional training, refines the FID of pre-trained CIFAR-10 and FFHQ-64 models from 1.92 and 2.45 to 1.89 and 2.25, respectively, utilizing 35 network evaluations per image.

## item_id: m_3691

TITLE: On the Vulnerability of Adversarially Trained Models Against Two-faced Attacks

ABSTRACT: Adversarial robustness is an important standard for measuring the quality of learned models, and adversarial training is an effective strategy for improving the adversarial robustness of models. In this paper, we disclose that adversarially trained models are vulnerable to two-faced attacks, where slight perturbations in input features are crafted to make the model exhibit a false sense of robustness in the verification phase. Such a threat is significantly important as it can mislead our evaluation of the adversarial robustness of models, which could cause unpredictable security issues when deploying substandard models in reality. More seriously, this threat seems to be pervasive and tricky: we find that many types of models suffer from this threat, and models with higher adversarial robustness tend to be more vulnerable. Furthermore, we provide the first attempt to formulate this threat, disclose its relationships with adversarial risk, and try to circumvent it via a simple countermeasure. These findings serve as a crucial reminder for practitioners to exercise caution in the verification phase, urging them to refrain from blindly trusting the exhibited adversarial robustness of models.

## item_id: m_3692

TITLE: Surprisal-Driven Feedback in Recurrent Networks

ABSTRACT: Recurrent neural nets are widely used for predicting temporal data. Their inherent deep feedforward structure allows learning complex sequential patterns. It is believed that top-down feedback might be an important missing ingredient which in theory could help disambiguate similar patterns depending on broader context. In this paper, we introduce surprisal-driven recurrent networks, which take into account past error information when making new predictions. This is achieved by continuously monitoring the discrepancy between most recent predictions and the actual observations. Furthermore, we show that it outperforms other stochastic and fully deterministic approaches on enwik8 character level prediction task achieving 1.37 BPC.

## item_id: m_3693

TITLE: Learning to Optimize

ABSTRACT: Algorithm design is a laborious process and often requires many iterations of ideation and validation. In this paper, we explore automating algorithm design and present a method to learn an optimization algorithm. We approach this problem from a reinforcement learning perspective and represent any particular optimization algorithm as a policy. We learn an optimization algorithm using guided policy search and demonstrate that the resulting algorithm outperforms existing hand-engineered algorithms in terms of convergence speed and/or the final objective value. 

## item_id: m_3694

TITLE: Acquiring Target Stacking Skills by Goal-Parameterized Deep Reinforcement Learning

ABSTRACT: Understanding physical phenomena is a key component of human intelligence and enables physical interaction with previously unseen environments. In this paper, we study how an artificial agent can autonomously acquire this intuition through interaction with the environment. We created a synthetic block stacking environment with physics simulation in which the agent can learn a policy end-to-end through trial and error. Thereby, we bypass to explicitly model physical knowledge within the policy. We are specifically interested in tasks that require the agent to reach a given goal state that may be different for every new trial. To this end, we propose a deep reinforcement learning framework that learns policies which are parametrized by a goal. We validated the model on a toy example navigating in a grid world with different target positions and in a block stacking task with different target structures of the final tower. In contrast to prior work, our policies show better generalization across different goals.

## item_id: m_3695

TITLE: Are BERT Families Zero-Shot Learners? A Study on Their Potential and Limitations

ABSTRACT: Starting from the resurgence of deep learning, language models (LMs) have never been so popular. Through simply increasing model scale and data size, large LMs pre-trained with self-supervision objectives demonstrate awe-inspiring results on both task performance and generalization. At the early stage, supervised fine-tuning is indispensable in adapting pre-trained language models (PLMs) to downstream tasks. Later on, the sustained growth of model capacity and data size, as well as newly presented pre-training techniques, make the PLMs perform well under the few-shot setting, especially in the recent paradigm of prompt-based learning. After witnessing the success of PLMs for few-shot tasks, we propose to further study the potential and limitations of PLMs for the zero-shot setting. We utilize 3 models from the most popular BERT family to launch the empirical study on 20 different datasets. We are surprised to find that a simple Multi-Null Prompting (without manually/automatically created prompts) strategy can yield very promising results on a few widely-used datasets, e.g., $86.59\%(\pm0.59)$ accuracy on the IMDB dataset, and $86.22\%(\pm2.71)$ accuracy on the Amazon dataset, which outperforms manually created prompts without engineering in achieving much better and stable performance with the accuracy of $74.06\%(\pm13.04)$, $75.54\%(\pm11.77)$ for comparison. However, we also observe some limitations of PLMs under the zero-shot setting, particularly for the language understanding tasks (e.g., GLUE).

## item_id: m_3696

TITLE: The Mind's Transformer: Computational Neuroanatomy of LLM-Brain Alignment

ABSTRACT: The alignment of Large Language Models (LLMs) and brain activity provides a powerful framework to advance our understanding of cognitive neuroscience and artificial intelligence. In this work, we zoom into one of the fundamental units of LLMs—the transformer block—to provide the first systematic computational neuroanatomy of its internal operations and human brain acitivity during language processing. Analyzing 21 state-of-the-art LLMs across five model families, we extract and evaluate 13 distinct intermediate states per transformer block—from initial layer normalization through attention mechanisms to feed-forward networks (FFNs). Our analysis reveals three key findings: (1) The commonly used hidden states in LLMs are surprisingly suboptimal, with over 90\% of brain voxels in sensory and language regions better explained by previously unexplored intermediate computations; (2) Different computational stages within a single transformer block map to anatomically distinct brain systems, revealing an intra-block hierarchy where early attention states align with sensory cortices while later FFN states correspond to association areas—mirroring the cortical processing hierarchy; (3) Rotary Positional Embeddings (RoPE) specifically enhance alignment along the brain's auditory processing streams. Per-head queries with RoPE best explain 74\% of auditory cortex activity compared to 8\% without RoPE, providing the first neurobiological validation of this architectural component in LLMs. Building on these insights, we propose MindTransformer, a feature selection framework that learns brain-aligned representations from all intermediate states. MindTransformer achieves significant brain alignment performance, with correlation improvements in primary auditory cortex exceeding gains from 456× model scaling. Our computational neuroanatomy approach opens new directions for understanding both biological intelligence through the lens of transformer computations and artificial intelligence through principles of brain organization.

## item_id: m_3697

TITLE: Improving Deep Regression with Ordinal Entropy

ABSTRACT: In computer vision, it is often observed that formulating regression problems as a classification task yields better performance. We investigate this curious phenomenon and provide a derivation to show that classification, with the cross-entropy loss, outperforms regression with a mean squared error loss in its ability to learn high-entropy feature representations. Based on the analysis, we propose an ordinal entropy loss to encourage higher-entropy feature spaces while maintaining ordinal relationships to improve the performance of regression tasks. Experiments on synthetic and real-world regression tasks demonstrate the importance and benefits of increasing entropy for regression.

## item_id: m_3698

TITLE: The Deep Weight Prior

ABSTRACT: Bayesian inference is known to provide a general framework for incorporating prior knowledge or specific properties into machine learning models via carefully choosing a prior distribution. In this work, we propose a new type of prior distributions for convolutional neural networks, deep weight prior (DWP), that exploit generative models to encourage a specific structure of trained convolutional filters e.g., spatial correlations of weights. We define DWP in the form of an implicit distribution and propose a method for variational inference with such type of implicit priors. In experiments, we show that DWP improves the performance of Bayesian neural networks when training data are limited, and initialization of weights with samples from DWP accelerates training of conventional convolutional neural networks.


## item_id: m_3699

TITLE: Nonlinear ICA Using Volume-Preserving Transformations

ABSTRACT: Nonlinear ICA is a fundamental problem in machine learning, aiming to identify the underlying independent components (sources) from data which is assumed to be a nonlinear function (mixing function) of these sources. Recent works prove that if the sources have some particular structures (e.g. temporal structure), they are theoretically identifiable even if the mixing function is arbitrary. However, in many cases such restrictions on the sources are difficult to satisfy or even verify, hence it inhibits the applicability of the proposed methods. Different from these works, we propose a general framework for nonlinear ICA, in which the mixing function is assumed to be a volume-preserving transformation, and meanwhile the conditions on the sources can be much looser. We provide an insightful proof of the identifiability of the proposed framework. We implement the framework by volume-preserving Flow-based models, and verify our theory by experiments on artificial data and synthesized images. Moreover, results on real-world images indicate that our framework can disentangle interpretable features.

## item_id: m_3700

TITLE: PDP: A General Neural Framework for Learning SAT Solvers

ABSTRACT: There have been recent efforts for incorporating Graph Neural Network models for learning fully neural solvers for constraint satisfaction problems (CSP) and particularly Boolean satisfiability (SAT). Despite the unique representational power of these neural embedding models, it is not clear to what extent they actually learn a search strategy vs. statistical biases in the training data. On the other hand, by fixing the search strategy (e.g. greedy search), one would effectively deprive the neural models of learning better strategies than those given. In this paper, we propose a generic neural framework for learning SAT solvers (and in general any CSP solver) that can be described in terms of probabilistic inference and yet learn search strategies beyond greedy search. Our framework is based on the idea of propagation, decimation and prediction (and hence the name PDP) in graphical models, and can be trained directly toward solving SAT in a fully unsupervised manner via energy minimization, as shown in the paper. Our experimental results demonstrate the effectiveness of our framework for SAT solving compared to both neural and the industrial baselines.
