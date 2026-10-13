# Batch 27 — 100 items

## item_id: m_2601

TITLE: Culture in Artificial Intelligence: A Literature Review & Proposal

ABSTRACT: Within the last few years, there has been an explosion of various Artificial Intelligence technologies poised to change the world. However, a lot of these technologies are made by the few to represent the many. This absence of diversity amongst researchers and overall innovators creates technology that is microscopic in worldview. It brings questions of Fairness, Accountability, Transparency, and Ethics (FATE) to the forefront. Most research undertaken in the context of FATE is done within a Western cultural context, which, in turn, imparts Western values. However, most research does not holistically address the question of the relationship between culture and AI. In this paper, we conduct a literature review of relevant research on Artificial Intelligence and culture and its importance in analyzing concepts of FATE. Additionally, we argue for and propose a definition of Culture in AI. We assume that through a combination of activation points (data collection and annotation, algorithm choice/development, problem framing, etc.), AI systems/agents perpetuate and produce culture in their dealings. This paper posits the need to situate Artificial intelligence systems within specific cultural paradigms consistent with their operative environments. We end by discussing future areas of study to be considered.

## item_id: m_2602

TITLE: Dynamic Neural Program Embeddings for Program Repair

ABSTRACT: Neural program embeddings have shown much promise recently for a variety of program analysis tasks, including program synthesis, program repair, code completion, and fault localization. However, most existing program embeddings are based on syntactic features of programs, such as token sequences or abstract syntax trees. Unlike images and text, a program has well-deﬁned semantics that can be difﬁcult to capture by only considering its syntax (i.e. syntactically similar programs can exhibit vastly different run-time behavior), which makes syntax-based program embeddings fundamentally limited. We propose a novel semantic program embedding that is learned from program execution traces. Our key insight is that program states expressed as sequential tuples of live variable values not only capture program semantics more precisely, but also offer a more natural ﬁt for Recurrent Neural Networks to model. We evaluate different syntactic and semantic program embeddings on the task of classifying the types of errors that students make in their submissions to an introductory programming class and on the CodeHunt education platform. Our evaluation results show that the semantic program embeddings signiﬁcantly outperform the syntactic program embeddings based on token sequences and abstract syntax trees. In addition, we augment a search-based program repair system with predictions made from our semantic embedding and demonstrate signiﬁcantly improved search efﬁciency.


## item_id: m_2603

TITLE: Emerging Disentanglement in Auto-Encoder Based Unsupervised Image Content Transfer

ABSTRACT: We study the problem of learning to map, in an unsupervised way, between domains $A$ and $B$, such that the samples $\vb \in B$ contain all the information that exists in samples $\va\in A$ and some additional information. For example, ignoring occlusions, $B$ can be people with glasses, $A$ people without, and the glasses, would be the added information. When mapping a sample $\va$ from the first domain to the other domain, the missing information is replicated from an independent reference sample $\vb\in B$. Thus, in the above example, we can create, for every person without glasses a version with the glasses observed in any face image. 

Our solution employs a single two-pathway encoder and a single decoder for both domains. The common part of the two domains and the separate part are encoded as two vectors, and the separate part is fixed at zero for domain $A$. The loss terms are minimal and involve reconstruction losses for the two domains and a domain confusion term. Our analysis shows that under mild assumptions, this architecture, which is much simpler than the literature guided-translation methods, is enough to ensure disentanglement between the two domains. We present convincing results in a few visual domains, such as no-glasses to glasses, adding facial hair based on a reference image, etc.

## item_id: m_2604

TITLE: Rethinking Adversarial Robustness in the Context of the Right to be Forgotten

ABSTRACT: The past few years have seen an intense research interest in the practical needs of the "right to be forgotten", which enables machine learning models to unlearn a fraction of training data and its lineage. As a result of this growing interest, numerous machine unlearning methods have been proposed and developed to address this important aspect of data privacy. While existing machine unlearning methods prioritize the protection of individuals' private and sensitive data, they overlook investigating the unlearned models' susceptibility to adversarial attacks and security breaches. In this work, we uncover a novel security vulnerability of machine unlearning based on the insight that the adversarial vulnerabilities can be bolstered especially for adversarial robust models. To exploit this observed vulnerability, we propose a novel attack called Adversarial Unlearning Attack (AdvUA), which aims to generate a small fraction of malicious unlearning requests during the unlearning process. AdvUA causes a significant reduction of adversarial robustness in the unlearned model compared to the original model, providing an entirely new capability for adversaries that is infeasible in conventional machine learning pipelines. Notably, we also show that AdvUA can effectively enhance model stealing attacks by extracting additional decision boundary information, further emphasizing the breadth and significance of our research. Extensive numerical studies are conducted to demonstrate the effectiveness of the proposed attack. Our code is available in the supplementary material.

## item_id: m_2605

TITLE: Learning continuous-time PDEs from sparse data with graph neural networks

ABSTRACT: The behavior of many dynamical systems follow complex, yet still unknown partial differential equations (PDEs). While several machine learning methods have been proposed to learn PDEs directly from data, previous methods are limited to discrete-time approximations or make the limiting assumption of the observations arriving at regular grids. We propose a general continuous-time differential model for dynamical systems whose governing equations are parameterized by message passing graph neural networks. The model admits arbitrary space and time discretizations, which removes constraints on the locations of observation points and time intervals between the observations. The model is trained with continuous-time adjoint method enabling efficient neural PDE inference. We demonstrate the model's ability to work with unstructured grids, arbitrary time steps, and noisy observations. We compare our method with existing approaches on several well-known physical systems that involve first and higher-order PDEs with state-of-the-art predictive performance.

## item_id: m_2606

TITLE: AD-NEGF: An End-to-End Differentiable Quantum Transport Simulator for Sensitivity Analysis and Inverse Problems

ABSTRACT: Quantum transport theory describes transport phenomena from first principles, which is essential for domains such as semiconductor fabrication. As a representative, the Non-Equilibrium Green Function (NEGF) method achieves superiority in numerical accuracy. However, its tremendous computational cost makes it unbearable for high-throughput simulation tasks such as sensitivity analysis, inverse design, etc. In this work, we propose AD-NEGF, to the best of our knowledge the first Automatic Differentiation (AD) based quantum transport simulator. AD-NEGF calculates gradient information efficiently by utilizing automatic differentiation and implicit layer techniques, while guaranteeing the correctness of the forward simulation. Such gradient information enables accurate and efficient calculation of differential physical quantities and solving inverse problems that are intractable by traditional optimization methods.

## item_id: m_2607

TITLE: MAS-GAN: Adversarial Calibration of Multi-Agent Market Simulators.

ABSTRACT: We look at the problem of how the simulation of a financial market should be configured so that it most accurately emulates the behavior of a real market.  In particular, we address agent-based simulations of markets that are composed of many hundreds or thousands of trading agents. A solution to this problem is important because it provides a credible test bed for evaluating potential trading algorithms (e.g., execution strategies). Simple backtesting of such algorithms suffers from a critical weaknesses, chiefly that the overall market is not responsive to the candidate trading algorithm. Multi-agent simulations address this weakness by simulating {\it market impact} via interaction between market participants. Calibration of such multi-agent simulators to ensure realism, however, is a challenge. In this paper, we present MAS-GAN -- a multi-agent simulator calibration method that allows to tune simulator parameters and to support more accurate evaluations of candidate trading algorithm. Our calibration focus is on high level parameters such as the relative proportions of the various types of agents that populate the simulation.
MAS-GAN is a two-step approach: first, we train a discriminator that is able to distinguish between ``real'' and ``fake'' market data as a part of GAN with self-attention, and then utilize it within an optimization framework to refine simulation parameters. The paper concludes with quantitative examples of applying MAS-GAN to improve simulator realism.

## item_id: m_2608

TITLE: Transferring Jailbreak Attacks from Public to Private LLMs via Local Prompt Optimization

ABSTRACT: Large Language Models (LLMs) demonstrate remarkable capabilities across natural language processing tasks but remain vulnerable to jailbreak attacks, where adversarial inputs are crafted to elicit harmful or undesirable responses. Existing optimization-based attacks often achieve high success rates but are impractical in black-box settings.
We focus on a practical scenario in which private LLMs are fine-tuned from public models and accessible only via query APIs, reflecting common real-world deployments. To address this, we propose a two-stage local prompt optimization framework that transfers jailbreak attacks from public to private LLMs. Our method introduces an auxiliary adversarial suffix to align output distributions between the public and target private models, enabling gradient-informed optimization in a purely local setup. Experiments show that our approach achieves high attack success rates on both open-source (Vicuna, LLaMA3) and proprietary models (GPT-4, Claude), and remains effective under diverse fine-tuning regimes, including LoRA-based updates.
These results highlight the practical security risks of fine-tuning LLMs and the need for robust defenses, while showing that highly transferable black-box attacks can be executed efficiently without accessing private model parameters.

## item_id: m_2609

TITLE: Distributed Deep Policy Gradient for Competitive Adversarial Environment

ABSTRACT: This work considers the problem of cooperative learners in partially observable, stochastic environment, receiving feedback in the form of joint reward. The paper presents a flexible multi-agent competitive environment for online training and direct policy performance comparison. This forms a formal problem of a multi-agent Reinforcement Learning (RL) under partial observability, where the goal is to maximize the score performance measured in a direct confrontation. To address the complexity of the problem we propose a distributed deep stochastic policy gradient with individual observations, experience replay, policy transfer, and self-play.

## item_id: m_2610

TITLE: Measuring Asymmetric Gradient Discrepancy in Parallel Continual Learning

ABSTRACT: In Parallel Continual Learning (PCL), the parallel multiple tasks start and end training unpredictably, thus suffering from training conflict and catastrophic forgetting issues. The two issues are raised because the gradients from parallel tasks differ in directions and magnitudes. Thus, in this paper, we formulate the PCL into a minimum distance optimization problem among gradients and propose an explicit Asymmetric Gradient Distance (AGD) to evaluate the gradient discrepancy in PCL. AGD considers both gradient magnitude ratios and directions, and has a tolerance when updating with a small gradient of inverse direction, which reduces the imbalanced influence of gradients on parallel task training. Moreover, we propose a novel Maximum Discrepancy Optimization (MaxDO) strategy to minimize the maximum discrepancy among multiple gradients. Solving by MaxDO with AGD, parallel training reduces the influence of the training conflict and suppresses the catastrophic forgetting of finished tasks. Extensive experiments validate the effectiveness of our approach on three image recognition datasets.

## item_id: m_2611

TITLE: Multi-level Residual Networks from Dynamical Systems View

ABSTRACT: Deep residual networks (ResNets) and their variants are widely used in many computer vision applications and natural language processing tasks.  However, the theoretical principles for designing and training ResNets are still not fully understood. Recently, several points of view have emerged to try to interpret ResNet theoretically, such as unraveled view, unrolled iterative estimation and dynamical systems view. In this paper, we adopt the dynamical systems point of view, and analyze the lesioning properties of ResNet both theoretically and experimentally.  Based on these analyses, we additionally propose a novel method for accelerating ResNet training. We apply the proposed method to train ResNets and Wide ResNets for three image classification benchmarks, reducing training time by more than 40\% with superior or on-par accuracy.

## item_id: m_2612

TITLE: A Critical Analysis of Distribution Shift

ABSTRACT: We introduce three new robustness benchmarks consisting of naturally occurring distribution changes in image style, geographic location, camera operation, and more. Using our benchmarks, we take stock of previously proposed hypotheses for out-of-distribution robustness and put them to the test. We find that using larger models and synthetic data augmentation can improve robustness on real-world distribution shifts, contrary to claims in prior work. Motivated by this, we introduce a new data augmentation method which advances the state-of-the-art and outperforms models pretrained with 1000x more labeled data. We find that some methods consistently help with distribution shifts in texture and local image statistics, but these methods do not help with some other distribution shifts like geographic changes. Hence no evaluated method consistently improves robustness. We conclude that future research should study multiple distribution shifts simultaneously.

## item_id: m_2613

TITLE: End-to-End Learnable Histogram Filters

ABSTRACT: Problem-specific algorithms and generic machine learning approaches have complementary strengths and weaknesses, trading-off data efficiency and generality. To find the right balance between these, we propose to use problem-specific information encoded in algorithms together with the ability to learn details about the problem-instance from data. We demonstrate this approach in the context of state estimation in robotics, where we propose end-to-end learnable histogram filters---a differentiable implementation of histogram filters that encodes the structure of recursive state estimation using prediction and measurement update but allows the specific models to be learned end-to-end, i.e. in such a way that they optimize the performance of the filter, using either supervised or unsupervised learning.

## item_id: m_2614

TITLE: Latent-Predictive Empowerment: Measuring Empowerment without a Simulator

ABSTRACT: Empowerment has the potential to help agents learn large skillsets, but is not yet a scalable solution for training general-purpose agents.  Recent empowerment methods learn large skillsets by maximizing the mutual information between skills and states, but these approaches require a model of the transition dynamics, which can be challenging to learn in realistic settings with high-dimensional and stochastic observations.  We present an algorithm, Latent-Predictive Empowerment (LPE), that can compute empowerment in a more scalable manner.   LPE learns large skillsets by maximizing an objective that under certain conditions has the same optimal skillset as the mutual information between skills and states, but our objective is more tractable to optimize because it only requires learning a simpler latent-predictive model rather than a full simulator of the environment.   We show empirically in a variety of settings, includes ones with high-dimensional observations and highly stochastic transition dynamics, that our empowerment objective learns similar-sized skillsets as the leading empowerment algorithm, which assumes access to a model of the transition dynamics, and outperforms other model-based approaches to empowerment.

## item_id: m_2615

TITLE: RGI: robust GAN-inversion for mask-free image inpainting and unsupervised pixel-wise anomaly detection

ABSTRACT: Generative adversarial networks (GANs), trained on a large-scale image dataset, can be a good approximator of the natural image manifold. GAN-inversion, using a pre-trained generator as a deep generative prior, is a promising tool for image restoration under corruptions. However, the performance of GAN-inversion can be limited by a lack of robustness to unknown gross corruptions, i.e., the restored image might easily deviate from the ground truth. In this paper, we propose a Robust GAN-inversion (RGI) method with a provable robustness guarantee to achieve image restoration under unknown \textit{gross} corruptions, where a small fraction of pixels are completely corrupted. Under mild assumptions, we show that the restored image and the identified corrupted region mask converge asymptotically to the ground truth. Moreover, we extend RGI to Relaxed-RGI (R-RGI) for generator fine-tuning to mitigate the gap between the GAN learned manifold and the true image manifold while avoiding trivial overfitting to the corrupted input image, which further improves the image restoration and corrupted region mask identification performance. The proposed RGI/R-RGI method unifies two important applications with state-of-the-art (SOTA) performance: (i) mask-free semantic inpainting, where the corruptions are unknown missing regions, the restored background can be used to restore the missing content. (ii) unsupervised pixel-wise anomaly detection, where the corruptions are unknown anomalous regions, the retrieved mask can be used as the anomalous region’s segmentation mask.

## item_id: m_2616

TITLE: RareFlow: Physics-Aware Flow-Matching for Cross-Sensor Super-Resolution of Rare-Earth Features

ABSTRACT: Super-resolution (SR) for remote sensing imagery often fails under out-of-distribution (OOD) conditions, such as rare geomorphic features captured by diverse sensors, producing visually plausible but physically inaccurate results.We present RareFlow, a physics-aware SR framework designed for OOD robustness. RareFlow's core is a dual-conditioning architecture. A Gated ControlNet preserves fine-grained geometric fidelity from the low-resolution input, while textual prompts provide semantic guidance for synthesizing complex features. To ensure physically sound outputs, we introduce a multifaceted loss function that enforces both spectral and radiometric consistency with sensor properties. Furthermore, the framework quantifies its own predictive uncertainty by employing a stochastic forward pass approach; the resulting output variance directly identifies unfamiliar inputs, mitigating feature hallucination.We validate RareFlow on a new, curated benchmark of multi-sensor satellite imagery. In blind evaluations, geophysical experts rated our model's outputs as approaching the fidelity of ground truth imagery, significantly outperforming state-of-the-art baselines. This qualitative superiority is corroborated by quantitative gains in perceptual metrics, including a nearly 40\% reduction in FID. RareFlow provides a robust framework for high-fidelity synthesis in data-scarce scientific domains and offers a new paradigm for controlled generation under severe domain shift.

## item_id: m_2617

TITLE: Scheduled Intrinsic Drive: A Hierarchical Take on Intrinsically Motivated Exploration

ABSTRACT: Exploration in sparse reward reinforcement learning remains an open challenge. Many state-of-the-art methods use intrinsic motivation to complement the sparse extrinsic reward signal, giving the agent more opportunities to receive feedback during exploration. Commonly these signals are added as bonus rewards, which results in a mixture policy that neither conducts exploration nor task fulfillment resolutely.
In this paper, we instead learn separate intrinsic and extrinsic task policies and schedule between these different drives to accelerate exploration and stabilize learning. Moreover, we introduce a new type of intrinsic reward denoted as successor feature control (SFC), which is general and not task-specific. It takes into account statistics over complete trajectories and thus differs from previous methods that only use local information to evaluate intrinsic motivation. We evaluate our proposed scheduled intrinsic drive (SID) agent using three different environments with pure visual inputs: VizDoom, DeepMind Lab and DeepMind Control Suite. The results show a substantially improved exploration efficiency with SFC and the hierarchical usage of the intrinsic drives. A video of our experimental results can be found at https://gofile.io/?c=HpEwTd.

## item_id: m_2618

TITLE: Prompt Distribution Matters: Tuning Visual Prompt Through Semantic Metric Guidance

ABSTRACT: Visual Prompt Tuning (VPT) has become a promising solution for Parameter-Efficient Fine-Tuning (PEFT) of pre-trained Vision Transformer (ViT) models on downstream vision tasks. VPT partially fine-tunes a set of learnable tokens while keeping the majority of the model parameters frozen. Recent research has explored modifying the connection structures of the prompts. However, the fundamental correlation and distribution between the prompts and image tokens remain unexplored. In this paper, we leverage \textit{metric learning} techniques to investigate how the distribution of prompts affects fine-tuning and transfer learning performance. Specifically, we propose a novel framework, \textbf{D}istribution \textbf{A}ware \textbf{V}isual \textbf{P}rompt Tuning (DA-VPT), to guide the distributions of the prompts by learning the distance metric from their class-related semantic data. Our method demonstrates that the prompts can serve as an effective bridge to share semantic information between image patches and the class token. We extensively evaluated our approach on popular benchmarks in both recognition and segmentation tasks. The results show the effectiveness of our proposed method and offer a new direction for PEFT optimization in vision transformers. We demonstrate that our approach enables more effective and efficient fine-tuning of ViT models by leveraging semantic information to guide the learning of the prompts, leading to improved performance on various downstream vision tasks.

## item_id: m_2619

TITLE: On the Safety of Open-Sourced Large Language Models: Does Alignment Really Prevent Them From Being Misused?

ABSTRACT: Large Language Models (LLMs) have achieved unprecedented performance in Natural Language Generation (NLG) tasks. However, many existing studies have shown that they could be misused to generate undesired content. In response, before releasing LLMs for public access, model developers usually align those language models through Supervised Fine-Tuning (SFT) or Reinforcement Learning with Human Feedback (RLHF). Consequently, those aligned large language models refuse to generate undesired content when facing potentially harmful/unethical requests. A natural question is "could alignment really prevent those open-sourced large language models from being misused to generate undesired content?''.  In this work, we provide a negative answer to this question. In particular, we show those open-sourced, aligned large language models could be easily misguided to generate undesired content without heavy computations or careful prompt designs. Our key idea is to directly manipulate the generation process of open-sourced LLMs to misguide it to generate undesired content including harmful or biased information and even private data. We evaluate our method on 4 open-sourced LLMs accessible publicly and our finding highlights the need for more advanced mitigation strategies for open-sourced LLMs.

## item_id: m_2620

TITLE: Word Mover's Embedding: From Word2Vec to Document Embedding

ABSTRACT: Learning effective text representations is a key foundation for numerous machine learning and NLP applications. While the celebrated Word2Vec technique yields semantically rich word representations, it is less clear whether sentence or document representations should be built upon word representations or from scratch. Recent work has demonstrated that a distance measure between documents called \emph{Word Mover's Distance} (WMD) that aligns semantically similar words, yields unprecedented KNN classification accuracy. However, WMD is very expensive to compute, and is harder to apply beyond simple KNN than feature embeddings. In this paper, we propose the \emph{Word Mover's Embedding } (WME), a novel approach to building an unsupervised document (sentence) embedding from pre-trained word embeddings. Our technique extends the theory of \emph{Random Features} to show convergence of the inner product between WMEs to a positive-definite kernel that can be interpreted as a soft version of (inverse) WMD. The proposed embedding is more efficient and flexible than WMD in many situations. As an example, WME with a simple linear classifier reduces the computational cost of WMD-based KNN \emph{from cubic to linear} in document length and \emph{from quadratic to linear} in number of samples, while simultaneously improving accuracy. In experiments on 9 benchmark text classification datasets and 22 textual similarity tasks the proposed technique consistently matches or outperforms state-of-the-art techniques, with significantly higher accuracy on problems of short length.

## item_id: m_2621

TITLE: Intrinsic Lorentz Neural Network

ABSTRACT: Real-world data frequently exhibit latent hierarchical structures, which can be naturally represented by hyperbolic geometry. Although recent hyperbolic neural networks have demonstrated promising results, many existing architectures remain partially intrinsic, mixing Euclidean operations with hyperbolic ones or relying on extrinsic parameterizations. To address it, we propose the \emph{Intrinsic Lorentz Neural Network} (ILNN), a fully intrinsic hyperbolic architecture that conducts all computations within the Lorentz model. At its core, the network introduces a novel \emph{point-to-hyperplane} fully connected layer (FC), replacing traditional Euclidean affine logits with closed-form hyperbolic distances from features to learned Lorentz hyperplanes, thereby ensuring that the resulting geometric decision functions respect the inherent curvature. 
Around this fundamental layer, we design intrinsic modules: GyroLBN, a Lorentz batch normalization that couples gyro-centering with gyro-scaling, consistently outperforming both LBN and GyroBN while reducing training time. We additionally proposed a gyro-additive bias for the FC output, a Lorentz patch-concatenation operator that aligns the expected log-radius across feature blocks via a digamma-based scale, and a Lorentz dropout layer.
Extensive experiments conducted on CIFAR-10/100 and two genomic benchmarks (TEB and GUE) illustrate that ILNN achieves state-of-the-art performance and computational cost among hyperbolic models and consistently surpasses strong Euclidean baselines.

## item_id: m_2622

TITLE: The Sword of DamocleSpeech: Demystifying Jailbreaking Attack in Discrete Token-based Speech Large Language Models

ABSTRACT: Speech Large Language Models (SpeechLLMs) and Omni models have recently achieved remarkable progress in human-like dialogue, prosody, and expressive emotion. How- ever, due to fragmented architectures, diverse training data, and inconsistent alignment strategies, research on jailbreak attacks and safety alignment in SpeechLLMs and Omni models remains limited and largely unsystematic. In this work, we observe that main- stream SpeechLLMs typically employ joint modeling of text tokens and discretized audio tokens, which often adopt distinct generation strategies. However, these discrete token- based SpeechLLMs remain highly vulnerable to prefilling attacks—where inserting a sin- gle token is sufficient to trigger simultaneous jailbreaks in both speech and text modali- ties. Through systematic evaluation of eight mainstream open-source SpeechLLMs and Omni models across three common benchmarks, we find that heterogeneous token co- operation during cross-modal generation leads to a reproducible jailbreak trajectory. To understand the underlying mechanism, we conduct manifold analysis and reveal modal misalignment between discretized audio representations and textual embeddings. In ad- dition, we propose a new set of metrics for evaluating jailbreak effectiveness, offering a multi-perspective assessment of safety bypasses. Our findings highlight fundamental weaknesses in current joint modeling strategies and provide a foundation for designing robust defenses in multimodal generative models. All code and logs are available on our anonymous GitHub.

## item_id: m_2623

TITLE: Symbolic Regression with Self-Supervised Heuristic Beam Search

ABSTRACT: Symbolic Regression (SR) aims to discover simple and interpretable mathematical expressions that explain observed data, making it a powerful tool for scientific discovery. In this work, we introduce a conceptually simple SR method that is both sample-efficient with respect to observed data points and self-supervised on large-scale synthetic data. By design, our approach favors parsimony, yielding interpretable and concise expressions. We focus on problems with exact solutions, evaluating our method on datasets containing physical laws and dynamical
equations. Our results demonstrate that combining beam search with a learned heuristic achieves competitive performance compared to existing methods in SRBench. Additionally, our approach effectively handles expressions with constants, a common challenge in the SR field. Finally, we provide a comprehensive scalability analysis across four key dimensions: (i) expression length, (ii) number of variables, (iii) number of domains, and (iv) number of observed data points.

## item_id: m_2624

TITLE: Learning to Reason without External Rewards

ABSTRACT: Training large language models (LLMs) for complex reasoning via Reinforcement Learning with Verifiable Rewards (RLVR) is effective but limited by reliance on costly, domain-specific supervision. We explore Reinforcement Learning from Internal Feedback (RLIF), a framework that enables LLMs to learn from intrinsic signals without external rewards or labeled data. We propose Intuitor, an RLIF method that uses a model's own confidence—termed self-certainty—as its sole reward signal. Intuitor replaces external rewards in Group Relative Policy Optimization (GRPO) with self-certainty scores, enabling fully unsupervised learning. Experiments demonstrate that Intuitor matches GRPO's performance on mathematical benchmarks while achieving better generalization to out-of-domain tasks like code generation, without requiring gold solutions or test cases. Our findings show that intrinsic model signals can drive effective learning across domains, offering a scalable alternative to RLVR for autonomous AI systems where verifiable rewards are unavailable. Code is available at https://github.com/sunblaze-ucb/Intuitor

## item_id: m_2625

TITLE: Q-Pensieve: Boosting Sample Efficiency of Multi-Objective RL Through Memory Sharing of Q-Snapshots

ABSTRACT: Many real-world continuous control problems are in the dilemma of weighing the pros and cons, multi-objective reinforcement learning (MORL) serves as a generic framework of learning control policies for different preferences over objectives. However, the existing MORL methods either rely on multiple passes of explicit search for finding the Pareto front and therefore are not sample-efficient, or utilizes a shared policy network for coarse knowledge sharing among policies. To boost the sample efficiency of MORL, we propose $Q$-Pensieve, a policy improvement scheme that stores a collection of $Q$-snapshots to jointly determine the policy update direction and thereby enables data sharing at the policy level. We show that $Q$-Pensieve can be naturally integrated with soft policy iteration with convergence guarantee. To substantiate this concept, we propose the technique of $Q$ replay buffer, which stores the learned $Q$-networks from the past iterations, and arrive at a practical actor-critic implementation. Through extensive experiments and an ablation study, we demonstrate that with much fewer samples, the proposed algorithm can outperform the benchmark MORL methods on a variety of MORL benchmark tasks.

## item_id: m_2626

TITLE: Kurisu-G²: A Knowledge Retrieval and Generation Algorithm Based on Document Structure

ABSTRACT: Retrieval-Augmented Generation (RAG) has become a standard paradigm for enriching
large language models with external knowledge, yet it often treats retrieved chunks inde-
pendently and overlooks their semantic and logical dependencies, leading to incoherent
or incomplete answers. GraphRAG addresses this by introducing graph-based context
representations, but it remains limited by the quality of the constructed graph, the heavy
reliance on LLMs for graph generation, and the lack of global logical consistency. In this
work, we propose an alternative perspective: leveraging principled graph-based similarity
measures, such as the Gromov–Wasserstein distance, to guide the retrieval, selection, and
unification of knowledge units. This approach preserves both the structural and relational
properties of the knowledge base, while enabling the enrichment of missing links that are
crucial for semantic integrity. We show that this perspective yields more coherent and
interpretable retrieval contexts compared to LLM-driven graph construction. Our results
highlight a promising path toward robust and logically consistent retrieval mechanisms in
RAG-based systems, with strong implications for high-stakes domains such as medicine
and law.

## item_id: m_2627

TITLE: Modulate Your Spectrum in Self-Supervised Learning

ABSTRACT: Whitening loss offers a theoretical guarantee against feature collapse in self-supervised learning (SSL) with joint embedding architectures. Typically, it involves a hard whitening approach, transforming the embedding and applying loss to the whitened output. In this work, we introduce Spectral Transformation (ST), a framework to modulate the spectrum of embedding and to seek for functions beyond whitening that can avoid dimensional collapse. We show that whitening is a special instance of ST by definition, and our empirical investigations unveil other ST instances capable of preventing collapse. Additionally, we propose a novel ST instance named IterNorm with trace loss (INTL). Theoretical analysis confirms INTL's efficacy in preventing collapse and modulating the spectrum of embedding toward equal-eigenvalues during optimization. Our experiments on ImageNet classification and COCO object detection demonstrate INTL's potential in learning superior representations. The code is available at https://github.com/winci-ai/INTL.

## item_id: m_2628

TITLE: Spanning Tree-based Graph Generation for Molecules

ABSTRACT: In this paper, we explore the problem of generating molecules using deep neural networks, which has recently gained much interest in chemistry. To this end, we propose a spanning tree-based graph generation (STGG) framework based on formulating molecular graph generation as a construction of a spanning tree and the residual edges. Such a formulation exploits the sparsity of molecular graphs and allows using compact tree-constructive operations to define the molecular graph connectivity. Based on the intermediate graph structure of the construction process, our framework can constrain its generation to molecular graphs that satisfy the chemical valence rules. We also newly design a Transformer architecture with tree-based relative positional encodings for realizing the tree construction procedure. Experiments on QM9, ZINC250k, and MOSES benchmarks verify the effectiveness of the proposed framework in metrics such as validity, Frechet ChemNet distance, and fragment similarity. We also demonstrate the usefulness of STGG in maximizing penalized LogP value of molecules.

## item_id: m_2629

TITLE: Nested Dithered Quantization for Communication Reduction in Distributed Training

ABSTRACT: In distributed training, the communication cost due to the transmission of gradients
or the parameters of the deep model is a major bottleneck in scaling up the number
of processing nodes. To address this issue, we propose dithered quantization for
the transmission of the stochastic gradients and show that training with Dithered
Quantized Stochastic Gradients (DQSG) is similar to the training with unquantized
SGs perturbed by an independent bounded uniform noise, in contrast to the other
quantization methods where the perturbation depends on the gradients and hence,
complicating the convergence analysis. We study the convergence of training
algorithms using DQSG and the trade off between the number of quantization
levels and the training time. Next, we observe that there is a correlation among the
SGs computed by workers that can be utilized to further reduce the communication
overhead without any performance loss. Hence, we develop a simple yet effective
quantization scheme, nested dithered quantized SG (NDQSG), that can reduce the
communication significantly without requiring the workers communicating extra
information to each other. We prove that although NDQSG requires significantly
less bits, it can achieve the same quantization variance bound as DQSG. Our
simulation results confirm the effectiveness of training using DQSG and NDQSG
in reducing the communication bits or the convergence time compared to the
existing methods without sacrificing the accuracy of the trained model.

## item_id: m_2630

TITLE: Under what circumstances do local codes emerge in feed-forward neural networks

ABSTRACT: Localist coding schemes are more easily interpretable than the distributed schemes but generally believed to be biologically implausible. Recent results have found highly selective units and object detectors in NNs that are indicative of local codes (LCs). Here we undertake a constructionist study on feed-forward NNs and find LCs emerging in response to invariant features, and this finding is robust until the invariant feature is perturbed by 40%. Decreasing the number of input data, increasing the relative weight of the invariant features and large values of dropout all increase the number of LCs. Longer training times increase the number of LCs and the turning point of the LC-epoch curve correlates well with the point at which NNs reach 90-100% on both test and training accuracy. Pseudo-deep networks (2 hidden layers) which have many LCs lose them when common aspects of deep-NN research are applied (large training data, ReLU activations, early stopping on training accuracy and softmax), suggesting that LCs may not be found in deep-NNs. Switching to more biologically feasible constraints (sigmoidal activation functions, longer training times, dropout, activation noise) increases the number of LCs. If LCs are not found in the feed-forward classification layers of modern deep-CNNs these data suggest this could either be caused by a lack of (moderately) invariant features being passed to the fully connected layers or due to the choice of training conditions and architecture. Should the interpretability and resilience to noise of LCs be required, this work suggests how to tune a NN so they emerge. 

## item_id: m_2631

TITLE: Emergence of foveal image sampling from learning to attend in visual scenes

ABSTRACT: We describe a neural attention model with a learnable retinal sampling lattice. The model is trained on a visual search task requiring the classification of an object embedded in a visual scene amidst background distractors using the smallest number of fixations. We explore the tiling properties that emerge in the model's retinal sampling lattice after training. Specifically, we show that this lattice resembles the eccentricity dependent sampling lattice of the primate retina, with a high resolution region in the fovea surrounded by a low resolution periphery. Furthermore, we find conditions where these emergent properties are amplified or eliminated providing clues to their function.

## item_id: m_2632

TITLE: A novel method to determine the number of latent dimensions with SVD

ABSTRACT: Determining the number of latent dimensions is a ubiquitous problem in machine
learning. In this study, we introduce a novel method that relies on SVD to discover
the number of latent dimensions. The general principle behind the method is to
compare the curve of singular values of the SVD decomposition of a data set with
the randomized data set curve. The inferred number of latent dimensions corresponds
to the crossing point of the two curves. To evaluate our methodology, we
compare it with competing methods such as Kaisers eigenvalue-greater-than-one
rule (K1), Parallel Analysis (PA), Velicers MAP test (Minimum Average Partial).
We also compare our method with the Silhouette Width (SW) technique which is
used in different clustering methods to determine the optimal number of clusters.
The result on synthetic data shows that the Parallel Analysis and our method have
similar results and more accurate than the other methods, and that our methods is
slightly better result than the Parallel Analysis method for the sparse data sets.

## item_id: m_2633

TITLE: DEEP ADVERSARIAL FORWARD MODEL

ABSTRACT: Learning world dynamics has recently been investigated as a way to make reinforcement
learning (RL) algorithms to be more sample efficient and interpretable.
In this paper, we propose to capture an environment dynamics with a novel forward
model that leverages recent works on adversarial learning and visual control. Such
a model estimates future observations conditioned on the current ones and other
input variables such as actions taken by an RL-agent. We focus on image generation
which is a particularly challenging topic but our method can be adapted to
other modalities. More precisely, our forward model is trained to produce realistic
observations of the future while a discriminator model is trained to distinguish
between real images and the model’s prediction of the future. This approach overcomes
the need to define an explicit loss function for the forward model which is currently
used for solving such a class of problem. As a consequence, our learning protocol
does not have to rely on an explicit distance such as Euclidean distance which
tends to produce unsatisfactory predictions. To illustrate our method, empirical
qualitative and quantitative results are presented on a real driving scenario, along
with qualitative results on Atari game Frostbite.

## item_id: m_2634

TITLE: Discovering objects and their relations from entangled scene representations

ABSTRACT: Our world can be succinctly and compactly described as structured scenes of objects and relations. A typical room, for example, contains salient objects such as tables, chairs and books, and these objects typically relate to each other by virtue of their correlated features, such as position, function and shape. Humans exploit knowledge of objects and their relations for learning a wide spectrum of tasks, and more generally when learning the structure underlying observed data. In this work, we introduce relation networks (RNs) - a general purpose neural network architecture for object-relation reasoning. We show that RNs are capable of learning object relations from scene description data. Furthermore, we show that RNs can act as a bottleneck that induces the factorization of objects from entangled scene description inputs, and from distributed deep representations of scene images provided by a variational autoencoder. The model can also be used in conjunction with differentiable memory mechanisms for implicit relation discovery in one-shot learning tasks. Our results suggest that relation networks are a powerful architecture for solving a variety of problems that require object relation reasoning.

## item_id: m_2635

TITLE: New Perspective on the Global Convergence of Finite-Sum Optimization

ABSTRACT: Deep neural networks (DNNs) have shown great success in many machine learning tasks. Their training is challenging since the loss surface of the network architecture is generally non-convex, or even non-smooth. How and under what assumptions is guaranteed convergence to a \textit{global} minimum possible? We propose a reformulation of the minimization problem allowing for a new recursive algorithmic framework. By using bounded style assumptions, we prove convergence to an $\varepsilon$-(global) minimum using $\mathcal{\tilde{O}}(1/\varepsilon^2)$ gradient computations. Our theoretical foundation motivates  further study, implementation, and optimization of the new  algorithmic framework and further investigation of its non-standard bounded style assumptions. This new direction broadens our understanding of why and under what circumstances  training of a DNN converges to a global minimum.

## item_id: m_2636

TITLE: Daylight: Assessing Generalization Skills of Deep Reinforcement Learning Agents

ABSTRACT: Deep reinforcement learning algorithms have recently achieved significant success in learning high-performing policies from purely visual observations. The ability to perform end-to-end learning from raw high dimensional input alone has led to deep reinforcement learning algorithms being deployed in a variety of fields. Thus, understanding and improving the ability of deep reinforcement learning agents to generalize to unseen data distributions is of critical importance. Much recent work has focused on assessing the generalization of deep reinforcement learning agents by introducing specifically crafted adversarial perturbations to their inputs. In this paper, we propose another approach that we call daylight: a framework to assess the generalization skills of trained deep reinforcement learning agents. Rather than focusing on worst-case analysis of distribution shift, our approach is based on black-box perturbations that correspond to semantically meaningful changes to the environment or the agent's visual observation system ranging from brightness to compression artifacts. We demonstrate that even the smallest changes in the environment cause the performance of the agents to degrade significantly in various games from the Atari environment despite having orders of magnitude lower perceptual similarity distance compared to state-of-the-art adversarial attacks. We show that our framework captures a diverse set of bands in the Fourier spectrum, giving a better overall understanding of the agent's generalization capabilities. We believe our work can be crucial towards building resilient and generalizable deep reinforcement learning agents.

## item_id: m_2637

TITLE: Diffusion Model for Dense Matching

ABSTRACT: The objective for establishing dense correspondence between paired images con- sists of two terms: a data term and a prior term. While conventional techniques focused on defining hand-designed prior terms, which are difficult to formulate, re- cent approaches have focused on learning the data term with deep neural networks without explicitly modeling the prior, assuming that the model itself has the capacity to learn an optimal prior from a large-scale dataset. The performance improvement was obvious, however, they often fail to address inherent ambiguities of matching, such as textureless regions, repetitive patterns, large displacements, or noises. To address this, we propose DiffMatch, a novel conditional diffusion-based framework designed to explicitly model both the data and prior terms for dense matching. This is accomplished by leveraging a conditional denoising diffusion model that explic- itly takes matching cost and injects the prior within generative process. However, limited input resolution of the diffusion model is a major hindrance. We address this with a cascaded pipeline, starting with a low-resolution model, followed by a super-resolution model that successively upsamples and incorporates finer details to the matching field. Our experimental results demonstrate significant performance improvements of our method over existing approaches, and the ablation studies validate our design choices along with the effectiveness of each component. Code and pretrained weights are available at https://ku-cvlab.github.io/DiffMatch.

## item_id: m_2638

TITLE: Unsupervised Learning of Goal Spaces for Intrinsically Motivated Goal Exploration

ABSTRACT: Intrinsically motivated goal exploration algorithms enable machines to discover repertoires of policies that produce a diversity of effects in complex environments. These exploration algorithms have been shown to allow real world robots to acquire skills such as tool use in high-dimensional continuous state and action spaces. However, they have so far assumed that self-generated goals are sampled in a specifically engineered feature space, limiting their autonomy. In this work, we propose an approach using deep representation learning algorithms to learn an adequate goal space. This is a developmental 2-stage approach: first, in a perceptual learning stage, deep learning algorithms use passive raw sensor observations of world changes to learn a corresponding latent space; then goal exploration happens in a second stage by sampling goals in this latent space. We present experiments with a simulated robot arm interacting with an object, and we show that exploration algorithms using such learned representations can closely match, and even sometimes improve, the performance obtained using engineered representations.

## item_id: m_2639

TITLE: Learning to Protect Communications with Adversarial Neural Cryptography

ABSTRACT: We ask whether neural networks can learn to use secret keys to protect
information from other neural networks.  Specifically, we focus on
ensuring confidentiality properties in a multiagent system, and we
specify those properties in terms of an adversary.  Thus, a
system may consist of neural networks named Alice and Bob, and we aim
to limit what a third neural network named Eve learns from
eavesdropping on the communication between Alice and Bob.
We do not prescribe specific cryptographic algorithms to these neural networks;
instead, we train end-to-end, adversarially.
We demonstrate that the neural networks can learn 
how to perform forms of encryption and decryption, and also
how to apply these operations selectively in order to meet
confidentiality goals.


## item_id: m_2640

TITLE: Multi-source Multi-view Transfer Learning in Neural Topic Modeling with Pretrained Topic and Word Embeddings

ABSTRACT: Though word embeddings and topics are complementary representations, several
past works have only used pretrained word embeddings in (neural) topic modeling
to address data sparsity problem in short text or small collection of documents.
However, no prior work has employed (pretrained latent) topics in transfer learning
paradigm. In this paper, we propose a framework to perform transfer learning
in neural topic modeling using (1) pretrained (latent) topics obtained from a large
source corpus, and (2) pretrained word and topic embeddings jointly (i.e., multiview)
in order to improve topic quality, better deal with polysemy and data sparsity
issues in a target corpus. In doing so, we first accumulate topics and word representations
from one or many source corpora to build respective pools of pretrained
topic (i.e., TopicPool) and word embeddings (i.e., WordPool). Then, we identify
one or multiple relevant source domain(s) and take advantage of corresponding
topics and word features via the respective pools to guide meaningful learning
in the sparse target domain. We quantify the quality of topic and document representations
via generalization (perplexity), interpretability (topic coherence) and
information retrieval (IR) using short-text, long-text, small and large document
collections from news and medical domains. We have demonstrated the state-ofthe-
art results on topic modeling with the proposed transfer learning approaches.

## item_id: m_2641

TITLE: Deep Learning and Quantum Entanglement: Fundamental Connections with Implications to Network Design

ABSTRACT: Formal understanding of the inductive bias behind deep convolutional networks, i.e. the relation between the network's architectural features and the functions it is able to model, is limited. In this work, we establish a fundamental connection between the fields of quantum physics and deep learning, and use it for obtaining novel theoretical observations regarding the inductive bias of convolutional networks. Specifically, we show a structural equivalence between the function realized by a convolutional arithmetic circuit (ConvAC) and a quantum many-body wave function, which facilitates the use of quantum entanglement measures as quantifiers of a deep network's expressive ability to model correlations. Furthermore, the construction of a deep ConvAC in terms of a quantum Tensor Network is enabled. This allows us to perform a graph-theoretic analysis of a convolutional network, tying its expressiveness to a min-cut in its underlying graph. We demonstrate a practical outcome in the form of a direct control over the inductive bias via the number of channels (width) of each layer. We empirically validate our findings on standard convolutional networks which involve ReLU activations and max pooling. The description of a deep convolutional network in well-defined graph-theoretic tools and the structural connection to quantum entanglement, are two interdisciplinary bridges that are brought forth by this work.

## item_id: m_2642

TITLE: A Way out of the Odyssey: Analyzing and Combining Recent Insights for LSTMs

ABSTRACT: LSTMs have become a basic building block for many deep NLP models. In recent years, many improvements and variations have been proposed for deep sequence models in general, and LSTMs in particular. We propose and analyze a series of architectural modifications for LSTM networks resulting in improved performance for text classification datasets. We observe compounding improvements on traditional LSTMs using Monte Carlo test-time model averaging, deep vector averaging (DVA), and residual connections, along with four other suggested modifications. Our analysis provides a simple, reliable, and high quality baseline model.

## item_id: m_2643

TITLE: Predicting Multiple Actions for Stochastic Continuous Control

ABSTRACT: We introduce a new approach to estimate continuous actions using actor-critic algorithms for reinforcement learning problems. Policy gradient methods usually predict one continuous action estimate or parameters of a presumed distribution (most commonly Gaussian) for any given state which might not be optimal as it may not capture the complete description of the target distribution. Our approach instead predicts M actions with the policy network (actor) and then uniformly sample one action during training as well as testing at each state. This allows the agent to learn a simple stochastic policy that has an easy to compute expected return. In all experiments, this facilitates better exploration of the state space during training and converges to a better policy. 

## item_id: m_2644

TITLE: Explaining Patterns in Data  with  Language Models via Interpretable Autoprompting

ABSTRACT: Large language models (LLMs) have displayed an impressive ability to harness natural language to perform complex tasks. In this work, we explore whether we can leverage this learned ability to find and explain patterns in data. Specifically, given a pre-trained LLM and data examples, we introduce interpretable autoprompting (iPrompt), an algorithm that generates a natural-language string explaining the data. iPrompt iteratively alternates between generating explanations with an LLM and reranking them based on their performance when used as a prompt. Experiments on a wide range of datasets, from synthetic mathematics to natural-language understanding, show that iPrompt can yield meaningful insights by accurately finding groundtruth dataset descriptions. Moreover, the prompts produced by iPrompt are simultaneously human-interpretable and highly effective for generalization: on real-world sentiment classification datasets, iPrompt produces prompts that match or even improve upon human-written prompts for GPT-3. Finally, experiments with an fMRI dataset show the potential for iPrompt to aid in scientific discovery.

## item_id: m_2645

TITLE: Analyzing adversarial robustness of vision transformers against spatial and spectral attacks

ABSTRACT: Vision Transformers have emerged as a powerful architecture that can outperform convolutional neural networks (CNNs) in image classification tasks. Several attempts have been made to understand robustness of Transformers against adversarial attacks, but existing studies draw inconsistent results, i.e., some conclude that Transformers are more robust than CNNs, while some others find that they have similar degrees of robustness. In this paper, we address two issues unexplored in the existing studies examining adversarial robustness of Transformers. First, we argue that the image quality should be simultaneously considered in evaluating adversarial robustness. We find that the superiority of one architecture to another in terms of robustness can change depending on the attack strength expressed by the quality of the attacked images. Second, by noting that Transformers and CNNs rely on different types of information in images, we formulate an attack framework as a tool for implementing flexible attacks, where an image can be attacked in the spectral domain as well as in the spatial domain. This attack perturbs the magnitude and phase information of particular frequency components selectively. Through extensive experiments, we find that Transformers tend to rely more on phase information and low frequency information than CNNs, and thus sometimes they are even more vulnerable under frequency-selective attacks. It is our hope that this work provides new perspectives in understanding the properties and adversarial robustness of Transformers.

## item_id: m_2646

TITLE: NEURAL EXECUTION ENGINES

ABSTRACT: Turing complete computation and reasoning are often regarded as necessary pre- cursors to general intelligence. There has been a significant body of work studying neural networks that mimic general computation, but these networks fail to generalize to data distributions that are outside of their training set. We study this problem through the lens of fundamental computer science problems: sorting and graph processing. We modify the masking mechanism of a transformer in order to allow them to implement rudimentary functions with strong generalization. We call this model the Neural Execution Engine, and show that it learns, through supervision, to numerically compute the basic subroutines comprising these algorithms with near perfect accuracy. Moreover, it retains this level of accuracy while generalizing to unseen data and long sequences outside of the training distribution.

## item_id: m_2647

TITLE: TrajGRU-Attention-ODE: Novel Spatiotemporal Predictive Models

ABSTRACT: To perform the long-term spatiotemporal sequence prediction (SSP) task with irregular time sampling assumptions, we build the sequence-to-sequence models based on the Trajectory Gated Recurrent Unit (TrajGRU) network and our proposed deep learning modules. First, we design a novel attention mechanism, namely Motion-based Attention (MA), and insert it into the TrajGRU network to create the TrajGRU-Attention model. In particular, the TrajGRU-Attention model can alleviate the impact of the vanishing gradient, which leads to the blurry effect in the long-term predictions and handle both regularly sampled and irregularly sampled time series. Second, leveraging the advances in Neural Ordinary Differential Equation (NODE) technique, we proposed the TrajGRU-Attention-ODE model, which can be applied in continuous-time applications. To evaluate the performance of the proposed models, we select three available spatiotemporal datasets based on the complexity level, including the MovingMNIST, MovingMNIST++, and KTH Action. Our models outperform the state-of-the-art NODE model and generate better results than the standard TrajGRU model for SSP tasks with different circumstances of time sampling. 

## item_id: m_2648

TITLE: ViCo: Plug-and-play Visual Condition for Personalized Text-to-image Generation

ABSTRACT: Personalized text-to-image generation using diffusion models has recently emerged and garnered significant interest. This task learns a novel concept (e.g., a unique toy), illustrated in a handful of images, into a generative model that captures fine visual details and generates photorealistic images based on textual embeddings. In this paper, we present ViCo, a novel lightweight plug-and-play method that seamlessly integrates visual condition into personalized text-to-image generation. ViCo stands out for its unique feature of not requiring any fine-tuning of the original diffusion model parameters, thereby facilitating more flexible and scalable model deployment. This key advantage distinguishes ViCo from most existing models that necessitate partial or full diffusion fine-tuning. ViCo incorporates an image attention module that conditions the diffusion process on patch-wise visual semantics, and an attention-based object mask that comes almost at no cost from the attention module. Despite only requiring light parameter training (~6% compared to the diffusion U-Net), ViCo delivers performance that is on par with, or even surpasses, all state-of-the-art models, both qualitatively and quantitatively. This underscores the efficacy of ViCo, making it a highly promising solution for personalized text-to-image generation without the need for diffusion model fine-tuning.

## item_id: m_2649

TITLE: TabStruct: Measuring Structural Fidelity of Tabular Data

ABSTRACT: Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, global utility, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present TabStruct, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results. Code is available at https://github.com/SilenceX12138/TabStruct.

## item_id: m_2650

TITLE: Understanding AdamW through Proximal Methods and Scale-Freeness

ABSTRACT: Adam has been widely adopted for training deep neural networks due to less hyperparameter tuning and remarkable performance. To improve generalization, Adam is typically used in tandem with a squared $\ell_2$ regularizer (referred to as Adam-$\ell_2$). However, even better performance can be obtained with AdamW, which decouples the gradient of the regularizer from the update rule of Adam-$\ell_2$. Yet, we are still lacking a complete explanation of the advantages of AdamW. In this paper, we tackle this question from both an optimization and an empirical point of view. First, we show how to re-interpret AdamW as an approximation of a proximal gradient method, which takes advantage of the closed-form proximal mapping of the regularizer instead of only utilizing its gradient information as in Adam-$\ell_2$. Next, we consider the property of ``scale-freeness'' enjoyed by AdamW and by its proximal counterpart: their updates are invariant to component-wise rescaling of the gradients. We provide empirical evidence across a wide range of deep learning experiments showing a correlation between the problems in which AdamW exhibits an advantage over Adam-$\ell_2$ and the degree to which we expect the gradients of the network to exhibit multiple scales, thus motivating the hypothesis that the advantage of AdamW could be due to the scale-free updates.

## item_id: m_2651

TITLE: There is More to Graphs than Meets the Eye: Learning Universal Features with Self-supervision

ABSTRACT: We study the problem of learning universal features from multiple graphs through self-supervision. Graph self-supervised learning has been shown to facilitate representation learning, and produce competitive models compared to supervised baselines. However, existing methods of self-supervision learn features from one graph, and thus, produce models that are specialized to a particular graph. We hypothesize that leveraging multiple graphs of a family can improve the quality of learnt representations in the model by extracting features that are universal to the family of graphs. To achieve this, we propose a framework that can learn generalisable representations from disparate node features of different graphs. We first homogenise the disparate features with graph-specific modules, which feed into a universal representation learning module for generalisable feature learning. We show that leveraging multiple graphs of the same family improves the quality of representations and results in better performance on downstream node classification task compared to self-supervision with one graph. In this paper, we present a principled way to design foundation graph models that are capable of learning from a set of graphs in a holistic manner. This approach  bridges the gap between self-supervised and supervised performance, while reducing the computational time for self-supervision and parameters of the model.

## item_id: m_2652

TITLE: Dynamic Neighborhood Construction for Structured Large Discrete Action Spaces

ABSTRACT: Large discrete action spaces (LDAS) remain a central challenge in reinforcement learning. Existing solution approaches can handle unstructured LDAS with up to a few million actions. However, many real-world applications in logistics, production, and transportation systems have combinatorial action spaces, whose size grows well beyond millions of actions, even on small instances. Fortunately, such action spaces exhibit structure, e.g., equally spaced discrete resource units. With this work, we focus on handling structured LDAS (SLDAS) with sizes that cannot be handled by current benchmarks: we propose Dynamic Neighborhood Construction (DNC), a novel exploitation paradigm for SLDAS. We present a scalable neighborhood exploration heuristic that utilizes this paradigm and efficiently explores the discrete neighborhood around the continuous proxy action in structured action spaces with up to $10^{73}$ actions. We demonstrate the performance of our method by benchmarking it against three state-of-the-art approaches designed for large discrete action spaces across three distinct environments. Our results show that DNC matches or outperforms state-of-the-art approaches while being computationally more  efficient. Furthermore, our method scales to action spaces that so far remained computationally intractable for existing methodologies.

## item_id: m_2653

TITLE: Exploring Target Representations for Masked Autoencoders

ABSTRACT: Masked autoencoders have become popular training paradigms for self-supervised visual representation learning. These models randomly mask a portion of the input and reconstruct the masked portion according to assigned target representations. In this paper, we show that a careful choice of the target representation is unnecessary for learning good visual representation since different targets tend to derive similarly behaved models. Driven by this observation, we propose a multi-stage masked distillation pipeline and use a randomly initialized model as the teacher, enabling us to effectively train high-capacity models without any effort to carefully design the target representation. 
On various downstream tasks, the proposed method to perform masked knowledge distillation with bootstrapped teachers (dbot) outperforms previous self-supervised methods by nontrivial margins. We hope our findings, as well as the proposed method, could motivate people to rethink the roles of target representations in pre-training masked autoencoders.

## item_id: m_2654

TITLE: Bridging Implicit-Explicit Representations for Ultra-Low Bitrate Image Compression

ABSTRACT: While recent VAE-based neural codecs achieve impressive results at low bitrates when optimized for perceptual quality, their performance degrades significantly under ultra-low bitrate conditions. To address this, generative methods that exploit semantic priors from pretrained models have emerged, revolutionizing ultra-low bitrate compression. However, these approaches remain constrained by a fundamental tradeoff between semantic faithfulness and perceptual realism. Methods relying on explicit semantic guidance preserve content accuracy but often lack textural fidelity, while those based on implicit representation can generate convincing details but may suffer from semantic drift. In this work, we introduce a unified framework that bridges this gap by coherently integrating explicit and implicit semantic representations. We condition a diffusion model with explicit high-level semantics while using reverse-channel coding to implicitly encode fine-grained information. In addition, a novel plugin encoder provides flexible control over the distortion-perception balance. Extensive experiments demonstrate that our framework achieves state-of-the-art rate–perception performance, outperforming existing approaches and surpassing DiffC by 23.49\%, 12.25\%, and 23.09\% DISTS-BD-Rate on the Kodak, DIV2K, and CLIC2020 datasets, respectively.

## item_id: m_2655

TITLE: Loss-aware Binarization of Deep Networks

ABSTRACT: Deep neural network models, though very powerful and highly successful, are computationally expensive in terms of space and time. Recently, there have been a number of attempts on binarizing the network weights and activations. This greatly reduces the network size, and replaces the underlying multiplications to additions or even XNOR bit operations. However, existing binarization schemes are based on simple matrix approximations and ignore the effect of binarization on the loss. In this paper, we propose a proximal Newton algorithm with diagonal Hessian approximation that directly minimizes the loss w.r.t. the binarized weights. The underlying proximal step has an efficient closed-form solution, and the second-order information can be efficiently obtained from the second moments already computed by the Adam optimizer. Experiments on both feedforward and recurrent networks show that the proposed loss-aware binarization algorithm outperforms existing binarization schemes, and is also more robust for wide and deep networks.

## item_id: m_2656

TITLE: ML-Bench: Evaluating Large Language Models for Code Generation in Repository-Level Machine Learning Tasks

ABSTRACT: Despite Large Language Models (LLMs) achieving impressive results in code generation, significant challenges remain in automated ML development, particularly in utilizing existing ML repositories effectively.
Also, recently, people have developed LLM agents that attempt to interact with repository code (e.g., resolving issues), prompting the need for end-to-end evaluations starting from environment setup to deploying the repository rather than merely generating code in already-configured environments. 
These two gaps have motivated our development of ML-Bench, a benchmark rooted in real-world ML applications that leverage existing code repositories. 
ML-Bench encompasses annotated 9,641 examples across 18 GitHub repositories, challenging LLMs to accommodate user-specified arguments and documentation intricacies effectively.
To evaluate both LLMs and agents, two setups are employed: 
ML-Bench-L for assessing LLMs' text-to-code conversion within a predefined deployment environment, and ML-Bench-A for testing autonomous agents in an end-to-end task execution within a Linux sandbox environment. 
Our findings indicate that while GPT-4o leads with a Pass@5 rate surpassing 50%, there remains significant scope for improvement, highlighted by issues such as hallucinated outputs and difficulties with bash script generation. 
Notably, in the more demanding ML-Agent-Bench, GPT-4o achieves a 76.47% success rate, reflecting the efficacy of iterative action and feedback in complex task resolution. 
Our resources, including code, data, and models, are available at \url{https://anonymous.4open.science/r/ML-Bench}.

## item_id: m_2657

TITLE: Context is Environment

ABSTRACT: Two lines of work are taking the central stage in AI research. On the one hand, the community is making increasing efforts to build models that discard spurious correlations and generalize better in novel test environments. Unfortunately, the hard lesson so far is that no proposal convincingly outperforms a simple empirical risk minimization baseline. On the other hand, large language models (LLMs) have erupted as algorithms able to learn in-context, generalizing on-the-fly to eclectic contextual circumstances that users enforce by means of prompting. In this paper, we argue that context is environment, and posit that in-context learning holds the key to better domain generalization. Via extensive theory and experiments, we show that paying attention to context$\unicode{x2013}\unicode{x2013}$unlabeled examples as they arrive$\unicode{x2013}\unicode{x2013}$allows our proposed In-Context Risk Minimization (ICRM) algorithm to zoom-in on the test environment risk minimizer, leading to significant out-of-distribution performance improvements. Furthermore, training with context helps the model learn a better featurizer. From all of this, two messages are worth taking home. Researchers in domain generalization should consider environment as context, and harness the adaptive power of in-context learning. Researchers in LLMs should consider context as environment, to better structure data towards generalization. Code is available at https://github.com/facebookresearch/ICRM.

## item_id: m_2658

TITLE: Decoupled Weight Decay Regularization

ABSTRACT: L$_2$ regularization and weight decay regularization are equivalent for standard stochastic gradient descent (when rescaled by the learning rate), but as we demonstrate this is \emph{not} the case for adaptive gradient algorithms, such as Adam. While common implementations of these algorithms employ L$_2$ regularization (often calling it ``weight decay'' in what may be misleading due to the inequivalence we expose), we propose a simple modification to recover the original formulation of weight decay regularization by \emph{decoupling} the weight decay from the optimization steps taken w.r.t. the loss function. We provide empirical evidence that our proposed modification (i) decouples the optimal choice of weight decay factor from the setting of the learning rate for both standard SGD and Adam and (ii) substantially improves Adam's generalization performance, allowing it to compete with SGD with momentum on image classification datasets (on which it was previously typically outperformed by the latter). Our proposed decoupled weight decay has already been adopted by many researchers, and the community has implemented it in TensorFlow and PyTorch; the complete source code for our experiments is available at \url{https://github.com/loshchil/AdamW-and-SGDW}

## item_id: m_2659

TITLE: Revisiting the Train Loss: an Efficient Performance Estimator for Neural Architecture Search

ABSTRACT: Reliable yet efficient evaluation of generalisation performance of a proposed architecture is crucial to the success of neural architecture search (NAS). Traditional approaches face a variety of limitations: training each architecture to completion is prohibitively expensive, early stopping estimates may correlate poorly with fully trained performance, and model-based estimators require large training sets. Instead, motivated by recent results linking training speed and generalisation with stochastic gradient descent, we propose to estimate the final test performance based on the sum of training losses. Our estimator is inspired by the marginal likelihood, which is used for Bayesian model selection. Our model-free estimator is simple, efficient, and cheap to implement, and does not require hyperparameter-tuning or surrogate training before deployment. We demonstrate empirically that our estimator consistently outperforms other baselines under various settings and can achieve a rank correlation of 0.95 with final test accuracy on the NAS-Bench201 dataset within 50 epochs.

## item_id: m_2660

TITLE: TabUnite: Efficient Encoding Schemes for Flow and Diffusion Tabular Generative Models

ABSTRACT: Flow matching and diffusion generative models for tabular data face challenges in modeling heterogeneous feature interrelationships, especially in data with continuous and categorical input features. Capturing these interrelationships is crucial as it allows these models to understand complex patterns and dependencies in the underlying data. A promising option to address the challenge is to devise suitable encoding schemes for the input features before the generative modeling process. However, prior methods often rely on either suboptimal heuristics such as one-hot encoding of categorical features followed by separated modeling of categorical/continuous features, or latent space diffusion models. Instead, our proposed solution unifies the data space and jointly applies a single generative process across all the encodings, efficiently capturing heterogeneous feature interrelationships. Specifically, it employs encoding schemes such as PSK Encoding,  Dictionary Encoding, and Analog Bits that effectively convert categorical features into continuous ones. Extensive experiments on datasets comprised of heterogeneous features demonstrate that our encoding schemes, combined with Flow Matching or Diffusion as our choice of generative model, significantly enhance model capabilities. Our TabUnite models help address data heterogeneity, achieving superior performance across a broad suite of datasets, baselines, and benchmarks while generating accurate, robust, and diverse tabular data.

## item_id: m_2661

TITLE: Non-linear System Identification from Partial Observations via Iterative Smoothing and Learning

ABSTRACT: System identification is the process of building a mathematical model of an unknown system from measurements of its inputs and outputs. It is a key step for model-based control, estimator design, and output prediction. This work presents an algorithm for non-linear offline system identification from partial observations, i.e. situations in which the system's full-state is not directly observable. The algorithm presented, called SISL, iteratively infers the system's full state through non-linear optimization and then updates the model parameters. We test our algorithm on a simulated system of coupled Lorenz attractors, showing our algorithm's ability to identify high-dimensional systems that prove intractable for particle-based approaches. We also use SISL to identify the dynamics of an aerobatic helicopter. By augmenting the state with unobserved fluid states, we learn a model that predicts the acceleration of the helicopter better than state-of-the-art approaches.

## item_id: m_2662

TITLE: PeFLL: Personalized Federated Learning by Learning to Learn

ABSTRACT: We present PeFLL, a new personalized federated learning algorithm that improves over the state-of-the-art in three aspects: 1) it produces more accurate models, especially in the low-data regime, and not only for clients present during its training phase, but also for any that may emerge in the future; 2) it reduces the amount of on-client computation and client-server communication by providing future clients with ready-to-use personalized models that require no additional finetuning or optimization; 3) it comes with theoretical guarantees that establish generalization from the observed clients to future ones. 
At the core of PeFLL lies a learning-to-learn approach that jointly trains an embedding network and a hypernetwork. The embedding network is used to represent clients in a latent descriptor space in a way that reflects their similarity to each other. The hypernetwork takes as input such descriptors and outputs the parameters of fully personalized client models. In combination, both networks constitute a learning algorithm that achieves state-of-the-art performance in several personalized federated learning benchmarks.

## item_id: m_2663

TITLE: Nugget 2D: Dynamic Contextual Compression for Scaling Decoder-only Language Models

ABSTRACT: Standard Transformer-based language models (LMs) scale poorly to long contexts. We propose a solution based on dynamic contextual compression, which extends the Nugget approach of Qin & Van Durme (2023) from BERT-like frameworks to decoder-only LMs. Our method models history as compressed “nuggets” which are trained to allow for reconstruction, and it can be initialized with off-the-shelf models such as LLaMA. We demonstrate through experiments in language modeling, question answering, and summarization that Nugget2D retains capabilities in these tasks, while drastically reducing the overhead during decoding in terms of time and space. For example, in the experiments of autoencoding, Nugget2D can shrink context at a 20x compression ratio with a BLEU score of 98% for reconstruction, achieving nearly lossless encoding.

## item_id: m_2664

TITLE: On Convergence and Stability of GANs

ABSTRACT: We propose studying GAN training dynamics as regret minimization, which is in contrast to the popular view that there is consistent minimization of a divergence between real and generated distributions. We analyze the convergence of GAN training from this new point of view to understand why mode collapse happens. We hypothesize the existence of undesirable local equilibria in this non-convex game to be responsible for mode collapse. We observe that these local equilibria often exhibit sharp gradients of the discriminator function around some real data points. We demonstrate that these degenerate local equilibria can be avoided with a gradient penalty scheme called DRAGAN. We show that DRAGAN enables faster training, achieves improved stability with fewer mode collapses, and leads to generator networks with better modeling performance across a variety of architectures and objective functions.

## item_id: m_2665

TITLE: Learning Latent Permutations with Gumbel-Sinkhorn Networks

ABSTRACT: Permutations and matchings are core building blocks in a variety of latent variable models, as they allow us to align, canonicalize, and sort data. Learning in such models is difficult, however, because exact marginalization over these combinatorial objects is intractable. In response, this paper introduces a collection of new methods for end-to-end learning in such models that approximate discrete maximum-weight matching using the continuous Sinkhorn operator.  Sinkhorn iteration is attractive because it functions as a simple, easy-to-implement analog of the softmax operator. With this, we can define the Gumbel-Sinkhorn method, an extension of the Gumbel-Softmax method (Jang et al. 2016, Maddison2016 et al. 2016) to distributions over latent matchings. We demonstrate the effectiveness of our method by outperforming competitive baselines on a range of qualitatively different tasks: sorting numbers, solving jigsaw puzzles, and identifying neural signals in worms. 

## item_id: m_2666

TITLE: Efficient Bi-level Optimization for Non-smooth Optimization

ABSTRACT: Bi-level optimization plays a key role in a lot of machine learning applications.  However, existing state-of-the-art bi-level optimization methods are limited to smooth or some specific non-smooth lower-level problems.  Even worse, most of them depend on approximating hypergradients to update upper-level variable which is the inherent reason for non-efficiency. Currently, achieving a generalized and efficient optimization algorithm for bi-level problems with a non-smooth, even non-Lipschitz continuous lower-level objective is still an open question to the best of our knowledge. To address these challenging problems, in this paper, we propose a new bi-level optimization algorithm based on the smoothing and penalty techniques. Specifically, we first produce a sequence of smoothed lower-level objectives with an exponential decay smoothing parameter for the non-smooth lower-level problem. Then, we transform the smoothed bi-level optimization to an unconstrained penalty problem by replacing the smoothed sub-problem with its first-order necessary conditions. Finally, we update the upper and lower-level variables alternately with doubly stochastic gradients of the unconstrained penalty problem. Importantly, we provide the theoretical analysis to show that our method can converge to a stationary point of original non-smooth bi-level problem if the lower-level problem is convex, and we give the necessary condition of the original problem if the lower-level problem is nonconvex. We compare our method with existing state-of-the-art bi-level optimization methods in three tasks, and all the experimental results demonstrate that our method is superior to the others in terms of accuracy and efficiency.

## item_id: m_2667

TITLE: VLSA: Enhancing Vision-Language Understanding via Perception and Cognition Alignment

ABSTRACT: Prevalent Vision-Language (VL) alignment techniques within Multi-modal Large Language Models (MLLMs) struggle to adequately align the language model with visual inputs, resulting in hallucinations and undermining reliability.  We rethink the modality alignment in MLLMs from the perspective of reducing information loss and present an efficient plug-in, VL Superior Alignment (VLSA), which decouples the alignment into two stages. The first stage, referred to as Perception Alignment, minimizes information loss in visual encoding through compressive encoding for high-resolution images and innovative reconstructive training leveraging latent diffusion models. The second stage, termed Cognition Alignment, reduces information loss in response generation by enhancing the language model's ability to grasp both high-level visual semantics and low-level image appearances, achieved by novel auxiliary self-supervised fine-tuning (SSFT) objectives. Extensive experiments across over 25 MLLM benchmarks and 7 MLLM architectures, thorough ablations, and analyses of computational overhead underscore the improvement of both performance and efficiency brought by VLSA. In service to the MLLM research community, our code and model checkpoints will be publicly available.

## item_id: m_2668

TITLE: ResFields: Residual Neural Fields for Spatiotemporal Signals

ABSTRACT: Neural fields, a category of neural networks trained to represent high-frequency signals, have gained significant attention in recent years due to their impressive performance in modeling complex 3D data, such as signed distance (SDFs) or radiance fields (NeRFs), via a single multi-layer perceptron (MLP). However, despite the power and simplicity of representing signals with an MLP, these methods still face challenges when modeling large and complex temporal signals due to the limited capacity of MLPs. In this paper, we propose an effective approach to address this limitation by incorporating temporal residual layers into neural fields, dubbed ResFields. It is a novel class of networks specifically designed to effectively represent complex temporal signals. We conduct a comprehensive analysis of the properties of ResFields and propose a matrix factorization technique to reduce the number of trainable parameters and enhance generalization capabilities. Importantly, our formulation seamlessly integrates with existing MLP-based neural fields and consistently improves results across various challenging tasks: 2D video approximation, dynamic shape modeling via temporal SDFs, and dynamic NeRF reconstruction. Lastly, we demonstrate the practical utility of ResFields by showcasing its effectiveness in capturing dynamic 3D scenes from sparse RGBD cameras of a lightweight capture system.

## item_id: m_2669

TITLE: FedHPO-Bench: A Benchmark Suite for Federated Hyperparameter Optimization

ABSTRACT: Hyperparameter optimization (HPO) is crucial for machine learning algorithms to achieve satisfactory performance. Its research progress has been boosted by existing HPO benchmarks. Nonetheless, existing efforts in benchmarking all focus on HPO for traditional centralized learning while ignoring federated learning (FL), a promising paradigm for collaboratively learning models from dispersed data. In this paper, we first identify some uniqueness of HPO for FL algorithms from various aspects. Due to this uniqueness, existing HPO benchmarks no longer satisfy the need to compare HPO methods in the FL setting. To facilitate the research of HPO in the FL setting, we propose and implement a benchmark suite FedHPO-Bench that incorporates comprehensive FedHPO problems, enables flexible customization of the function evaluations, and eases continuing extensions. We also conduct extensive experiments based on FedHPO-Bench to provide the community with more insights into FedHPO. We open-sourced FedHPO-Bench at https://github.com/FedHPO-Bench/FedHPO-Bench-ICLR23.

## item_id: m_2670

TITLE: Cooperating RPN's Improve Few-Shot Object Detection

ABSTRACT: Learning to detect an object in an image from very few training examples - few-shot object detection - is challenging, because the classifier that sees proposal boxes has very little training data.  A particularly challenging training regime occurs when there are one or two training examples. In this case, if the region proposal network (RPN) misses even one high intersection-over-union (IOU) training box, the classifier's model of how object appearance varies can be severely impacted. We use multiple distinct yet cooperating RPN's.  Our RPN's are trained to be different, but not too different; doing so yields significant performance improvements over state of the art for COCO and PASCAL VOC in the very few-shot setting. This effect appears to be independent of the choice of classifier or dataset.  


## item_id: m_2671

TITLE: Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding

ABSTRACT: Time series are often complex and rich in information but sparsely labeled and therefore challenging to model. In this paper, we propose a self-supervised framework for learning robust and generalizable representations for time series. Our approach, called Temporal Neighborhood Coding (TNC), takes advantage of the local smoothness of a signal's generative process to define neighborhoods in time with stationary properties. Using a debiased contrastive objective, our framework learns time series representations by ensuring that in the encoding space, the distribution of signals from within a neighborhood is distinguishable from the distribution of non-neighboring signals. Our motivation stems from the medical field, where the ability to model the dynamic nature of time series data is especially valuable for identifying, tracking, and predicting the underlying patients' latent states in settings where labeling data is practically impossible. We compare our method to recently developed unsupervised representation learning approaches and demonstrate superior performance on clustering and classification tasks for multiple datasets.

## item_id: m_2672

TITLE: Learning Efficient Tensor Representations with Ring Structure Networks

ABSTRACT: \emph{Tensor train (TT) decomposition} is a powerful representation for high-order tensors, which has been successfully applied to various machine learning tasks in recent years.  In this paper, we propose a more generalized tensor decomposition with ring structure network  by employing circular multilinear products over a sequence of lower-order core tensors, which is termed as TR representation. Several learning algorithms including blockwise ALS  with adaptive tensor ranks and  SGD  with high scalability are presented. Furthermore, the mathematical properties are investigated, which enables us to perform basic algebra operations in a computationally efficiently way by using TR representations. Experimental results on synthetic signals and real-world datasets demonstrate the effectiveness of TR model and the learning algorithms. In particular, we show that  the structure information and high-order correlations within a 2D image can be captured efficiently by employing tensorization and TR representation. 


## item_id: m_2673

TITLE: $f$-Mutual Information Contrastive Learning

ABSTRACT: Self-supervised contrastive learning is an emerging field due to its power in providing good data representations. Such learning paradigm widely adopts the InfoNCE loss, which is closely connected with maximizing the mutual information. In this work, we propose the $f$-Mutual Information Contrastive Learning framework ($f$-MICL) , which directly maximizes the $f$-divergence-based generalization of mutual information. We theoretically prove that, under mild assumptions, our $f$-MICL naturally attains the alignment for positive pairs and the uniformity for data representations, the two main factors for the success of contrastive learning.  We further provide theoretical guidance on designing the similarity function and choosing the effective $f$-divergences for $f$-MICL. Using several benchmark tasks from both vision and natural text, we empirically verify that our novel method outperforms or performs on par with state-of-the-art strategies.

## item_id: m_2674

TITLE: Leave No Observation Behind: Real-time Correction for VLA Action Chunks

ABSTRACT: To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. We introduce Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA(base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction. This preserves the base model’s competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC). On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, our method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay. Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models. These results indicate that A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

## item_id: m_2675

TITLE: Emergence of functional and structural properties of the head direction system by optimization of recurrent neural networks

ABSTRACT: Recent work suggests goal-driven training of neural networks can be used to model neural activity in the brain. While response properties of neurons in artificial neural networks bear similarities to those in the brain, the network architectures are often constrained to be different. Here we ask if a neural network can recover both neural representations and, if the architecture is unconstrained and optimized, also the anatomical properties of neural circuits. We demonstrate this in a system where the connectivity and the functional organization have been characterized, namely, the head direction circuit of the rodent and fruit fly. We trained recurrent neural networks (RNNs) to estimate head direction through integration of angular velocity. We found that the two distinct classes of neurons observed in the head direction system, the Compass neurons and the Shifter neurons, emerged naturally in artificial neural networks as a result of training. Furthermore, connectivity analysis and in-silico neurophysiology revealed structural and mechanistic similarities between artificial networks and the head direction system. Overall, our results show that optimization of RNNs in a goal-driven task can recapitulate the structure and function of biological circuits, suggesting that artificial neural networks can be used to study the brain at the level of both neural activity and anatomical organization.

## item_id: m_2676

TITLE: Hierarchical Reinforcement Learning by Discovering Intrinsic Options

ABSTRACT: We propose a hierarchical reinforcement learning method, HIDIO, that can learn task-agnostic options in a self-supervised manner while jointly learning to utilize them to solve sparse-reward tasks. Unlike current hierarchical RL approaches that tend to formulate goal-reaching low-level tasks or pre-define ad hoc lower-level policies, HIDIO encourages lower-level option learning that is independent of the task at hand, requiring few assumptions or little knowledge about the task structure. These options are learned through an intrinsic entropy minimization objective conditioned on the option sub-trajectories. The learned options are diverse and task-agnostic. In experiments on sparse-reward robotic manipulation and navigation tasks, HIDIO achieves higher success rates with greater sample efficiency than regular RL baselines and two state-of-the-art hierarchical RL methods. Code at: https://github.com/jesbu1/hidio.

## item_id: m_2677

TITLE: Generative Adversarial Networks for Image Steganography

ABSTRACT: Steganography is collection of methods to hide secret information ("payload") within non-secret information ("container"). Its counterpart, Steganalysis, is the practice of determining if a message contains a hidden payload, and recovering it if possible. Presence of hidden payloads is typically detected by a binary classifier. In the present study, we propose a new model for generating image-like containers based on Deep Convolutional Generative Adversarial Networks (DCGAN). This approach allows to generate more setganalysis-secure message embedding using standard steganography algorithms. Experiment results demonstrate that the new model successfully deceives the steganography analyzer, and for this reason, can be used in  steganographic applications.

## item_id: m_2678

TITLE: CorBenchX: Large-Scale Chest X-Ray Error Dataset and Vision–Language Model Benchmark for Report Error Correction

ABSTRACT: AI-driven models have shown great promise in detecting errors in radiology reports, yet the field lacks a unified benchmark for rigorous evaluation of error detection and further correction. To address this gap, we introduce \textbf{CorBenchX}, a comprehensive suite for automated error detection and correction in chest X-ray reports, designed to advance AI-assisted quality control in clinical practice. We first synthesize a large-scale dataset of 26,326 chest X-ray error reports by injecting clinically common errors via prompting DeepSeek-R1, with each corrupted report paired with its original text, error type, and human-readable description. Leveraging this dataset, we benchmark both open- and closed-source vision–language models (\eg, InternVL, Qwen-VL, GPT-4o, o4-mini, and Claude-3.7) for error detection and correction under zero-shot prompting. Among these models, o4-mini achieves the best performance, with 50.6 \% detection accuracy and correction scores of BLEU 0.853, ROUGE 0.924, BERTScore 0.981, SembScore 0.865, and CheXbertF1 0.954, remaining below clinical-level accuracy, highlighting the challenge of precise report correction. To advance the state of the art, we propose a multi-step reinforcement learning (MSRL) framework that optimizes a multi-objective reward combining format compliance, error-type accuracy, and BLEU similarity. We apply MSRL to QwenVL2.5-7B, the top open-source model in our benchmark, achieving an improvement of 38.3\% in single-error detection precision and 5.2\% in single-error correction over the zero-shot baseline.

## item_id: m_2679

TITLE: DraftAttention: Fast Video Diffusion via Low-Resolution Attention Guidance

ABSTRACT: Video generation models based on diffusion transformers have recently attracted widespread attention for their excellent generation quality.
Despite recent progress, their computational expense remains the principal bottleneck. In particular, attention alone accounts for more than 80\% of the overall latency, and the synthesis of only 8 seconds 720p video takes tens of minutes, which severely restricts practical applicability and scalability.
To address this, we propose **DraftAttention**, a training-free framework for the acceleration of video diffusion transformers with dynamic sparse attention on GPUs.
The key idea is to compute the low-resolution draft attention based on the downsampled low-resolution query and key with minor computational overhead. The draft attention exposes redundancy both spatially within each feature map and temporally across frames, thus identifying the most important areas in the attention map.
The resulting low-resolution sparse mask then guides full-resolution sparse attention computations.
To align region-level sparsity with token-level computations, we further propose a deterministic reordering of tokens such that entries in each region become contiguous in memory, ensuring hardware-friendly execution of sparse attention.
Our theoretical analysis demonstrates that the low-resolution draft attention closely approximates the full attention, providing reliable guidance for constructing accurate sparse attention.
Experimental results show that our method outperforms existing sparse attention approaches in video generation quality and achieves up to 2x end-to-end speedup on GPUs.

## item_id: m_2680

TITLE: Event extraction from unstructured Amharic text

ABSTRACT: In information extraction, event extraction is one of the types that extract the specific knowledge of certain incidents from texts. Event extraction has been done on different languages texts but not on one of the Semitic language Amharic. In this study, we present a system that extracts an event from unstructured Amharic text. The system has designed by the integration of supervised machine learning and rule-based approaches together.  We call it a hybrid system. The model from the supervised machine learning detects events from the text, then, handcrafted rules and the rule-based rules extract the event from the text. The hybrid system has compared with the standalone rule-based method that is well known for event extraction. The study has shown that the hybrid system has outperformed the standalone rule-based method. For the event extraction, we have been extracting event arguments. Event arguments identify event triggering words or phrases that clearly express the occurrence of the event. The event argument attributes can be verbs, nouns, occasionally adjectives such as ሰርግ/wedding and time as well.

## item_id: m_2681

TITLE: Prompt Optimization via Adversarial In-Context Learning

ABSTRACT: We propose a new method, Adversarial In-Context Learning (adv-ICL), to optimize prompt for in-context learning (ICL) by employing one LLM as a generator, another as a discriminator, and a third as a prompt modifier. As in traditional adversarial learning, adv-ICL is implemented as a two player game between the generator and discriminator, where the generator tries to generate realistic enough output to fool the discriminator. In each round, given an input prefixed by task instructions and several exemplars, the generator produces an output. The discriminator is then tasked with classifying the generator input-output pair as model-generated or real data. Based on the discriminator loss, the prompt modifier proposes possible edits to the generator and discriminator prompts, and the edits that most improve the adversarial loss are selected. We show that adv-ICL results in significant improvements over state-of-the-art prompt optimization techniques for both open and closed-source models on 11 generation and classification tasks including summarization, arithmetic reasoning, machine translation, data-to-text generation, and the MMLU and big-bench hard benchmarks. In addition, because our method uses pre-trained models and updates only prompts rather than model parameters, it is computationally efficient, easy to extend to any LLM and task, and effective in low-resource settings.

## item_id: m_2682

TITLE: Is Label Smoothing Truly Incompatible with Knowledge Distillation: An Empirical Study

ABSTRACT: This work aims to empirically clarify a recently discovered perspective that label smoothing is incompatible with knowledge distillation. We begin by introducing the motivation behind on how this incompatibility is raised, i.e., label smoothing erases relative information between teacher logits. We provide a novel connection on how label smoothing affects distributions of semantically similar and dissimilar classes. Then we propose a metric to quantitatively measure the degree of erased information in sample's representation. After that, we study its one-sidedness and imperfection of the incompatibility view through massive analyses, visualizations and comprehensive experiments on Image Classification, Binary Networks, and Neural Machine Translation. Finally, we broadly discuss several circumstances wherein label smoothing will indeed lose its effectiveness.

## item_id: m_2683

TITLE: Language Modeling Teaches You More Syntax than Translation Does: Lessons Learned Through Auxiliary Task Analysis

ABSTRACT: Recent work using auxiliary prediction task classifiers to investigate the properties of LSTM representations has begun to shed light on why pretrained representations, like ELMo (Peters et al., 2018) and CoVe (McCann et al., 2017), are so beneficial for neural language understanding models. We still, though, do not yet have a clear understanding of how the choice of pretraining objective affects the type of linguistic information that models learn. With this in mind, we compare four objectives - language modeling, translation, skip-thought, and autoencoding - on their ability to induce syntactic and part-of-speech information.  We make a fair comparison between the tasks by holding constant the quantity and genre of the training data, as well as the LSTM architecture. We find that representations from language models consistently perform best on our syntactic auxiliary prediction tasks, even when trained on relatively small amounts of data. These results suggest that language modeling may be the best data-rich pretraining task for transfer learning applications requiring syntactic information. We also find that the representations from randomly-initialized, frozen LSTMs perform strikingly well on our syntactic auxiliary tasks, but this effect disappears when the amount of training data for the auxiliary tasks is reduced.

## item_id: m_2684

TITLE: Saliency-Guided Hidden Associative Replay for Continual Learning

ABSTRACT: Continual Learning (CL) is a burgeoning domain in next-generation AI, focusing on training neural networks over a sequence of tasks akin to human learning. While CL provides an edge over traditional supervised learning, its central challenge remains to counteract \emph{catastrophic forgetting} and ensure the retention of prior tasks during subsequent learning. Amongst various strategies to tackle this, replay-based methods have emerged as preeminent, echoing biological memory mechanisms. However, these methods are memory-intensive, often preserving entire data samples—an approach inconsistent with humans' selective memory retention of salient experiences. While some recent works have explored the storage of only significant portions of data in episodic memory, the inherent nature of partial data necessitates innovative retrieval mechanisms. Current solutions, like inpainting, approximate full data reconstruction from partial cues, a method that diverges from genuine human memory processes. Addressing these nuances, this paper presents the **S**aliency-Guided **H**idden **A**ssociative **R**eplay for **C**ontinual Learning (**SHARC**). This novel framework synergizes associative memory with replay-based strategies. SHARC primarily archives salient data segments via sparse memory encoding. Importantly, by harnessing associative memory paradigms, it introduces a content-focused memory retrieval mechanism, promising swift and near-perfect recall, bringing CL a step closer to authentic human memory processes. Extensive experimental results demonstrate the effectiveness of our proposed method for various continual learning tasks. Anonymous code can be found at: https://anonymous.4open.science/r/SHARC-6319.

## item_id: m_2685

TITLE: Beyond Size: How Gradients Shape Pruning Decisions in Large Language Models

ABSTRACT: Large Language Models (LLMs) with a billion or more parameters are prime targets for network pruning, which aims to reduce a portion of the network weights without compromising performance. Prior approaches such as Weights Magnitude, SparseGPT, and Wanda, either concentrated solely on weights or integrated weights with activations for sparsity. However, they overlooked the informative gradients derived from pretrained large language models. In this paper, we present a novel sparsity-centric pruning method for pretrained LLMs, termed **G**radient-**b**ased **L**anguage **M**odel **P**runer (**GBLM-Pruner**). Distinctively, GBLM-Pruner operates in a training-free manner by harnessing normalized gradients, and substantially outperforms competitive counterparts like SparseGPT and Wanda in multiple benchmarks. Intriguing, after incorporating gradients, the unstructured pruning method tends to reveal some structural patterns post-pruning, which mirrors the geometric interdependence inherent in the LLMs' parameter structure. Additionally, GBLM-Pruner functions without any subsequent retraining or weight updates to maintain its simplicity as other counterparts. Extensive evaluations on LLaMA-1 and LLaMA-2 across various language benchmarks and perplexity show that GBLM-Pruner surpasses magnitude pruning, Wanda (*weights+activations*), and SparseGPT (*weights+activations+weight update*) by significant margins. Our code and models will be publicly available.

## item_id: m_2686

TITLE: Leveraging Low-Rank and Sparse Recurrent Connectivity for Robust Closed-Loop Control

ABSTRACT: Developing autonomous agents that can interact with changing environments is an open challenge in machine learning. Robustness is particularly important in these settings as agents are often fit offline on expert demonstrations but deployed online where they must generalize to the closed feedback loop within the environment. In this work, we explore the application of recurrent neural networks to tasks of this nature and understand how a parameterization of their recurrent connectivity influences robustness in closed-loop settings. Specifically, we represent the recurrent connectivity as a function of rank and sparsity and show both theoretically and empirically that modulating these two variables has desirable effects on network dynamics. The proposed low-rank, sparse connectivity induces an interpretable prior on the network that proves to be most amenable for a class of models known as closed-form continuous-time neural networks (CfCs). We find that CfCs with fewer parameters can outperform their full-rank, fully-connected counterparts in the online setting under distribution shift. This yields memory-efficient and robust agents while opening a new perspective on how we can modulate network dynamics through connectivity.

## item_id: m_2687

TITLE: Induction Head Implementation Across Diverse Transformer Weight Constructions

ABSTRACT: Induction heads are a class of self-attention mechanisms empirically crucial for in-context learning in transformer models.
Although previous research has suggested possible forms of induction heads, it remains unclear how they interact with other network modules and operate on their outputs.
In this work, we address this question by showing that a two-layer induction head allows flexibility in the construction of its first layer. This flexibility enables the induction head to operate alongside other modules within the network.
Additionally, in the multi-layer networks where it's difficult for the induction heads to retrieve the original input, we propose a new mechanism akin to induction heads (in the sense of using the information of inter-token identity) that still functions in deep networks.
We also performed proof-of-concept experiments showing that induction heads are trainable using only a subset of the model’s layers.
Our key insight is that information about which tokens are identical are possible to be extracted from the outputs of many transformer networks, which is essential for applying the induction head mechanism.
Our work presents the diversity in the realization of induction heads, which serves as an explanation for why induction heads consistently appear across models.

## item_id: m_2688

TITLE: Sequence generation with a physiologically plausible model of handwriting and Recurrent Mixture Density Networks

ABSTRACT: The purpose of this study is to explore the feasibility and potential benefits of using a physiological plausible model of handwriting as a feature representation for sequence generation with recurrent mixture density networks. We build on recent results in handwriting prediction developed by Graves (2013), and we focus on generating sequences that possess the statistical and dynamic qualities of handwriting and calligraphic art forms. Rather than model raw sequence data, we first preprocess and reconstruct the input training data with a concise representation given by a motor plan (in the form of a coarse sequence of `ballistic' targets) and corresponding dynamic parameters (which define the velocity and curvature of the pen-tip trajectory). This representation provides a number of advantages, such as enabling the system to learn from very few examples by introducing artificial variability in the training data, and mixing of visual and dynamic qualities learned from different datasets.

## item_id: m_2689

TITLE: Adversarial Paritial Multi-label Learning

ABSTRACT: Partial multi-label learning (PML), which tackles the problem of learning multi-label prediction models from instances with overcomplete noisy annotations, has recently started gaining attention from the research community. In this paper, we propose a novel adversarial learning model, PML-GAN, under a generalized encoder-decoder framework for partial multi-label learning. The PML-GAN model uses a disambiguation network to identify noisy labels and uses a multi-label prediction network to map the training instances to the disambiguated label vectors, while deploying a generative adversarial network as an inverse mapping from label vectors to data samples in the input feature space. The learning of the overall model corresponds to a minimax adversarial game, which enhances the correspondence of input features with the output labels. Extensive experiments are conducted on multiple datasets, while the proposed model demonstrates the state-of-the-art performance for partial multi-label learning.

## item_id: m_2690

TITLE: InstructScene: Instruction-Driven 3D Indoor Scene Synthesis with Semantic Graph Prior

ABSTRACT: Comprehending natural language instructions is a charming property for 3D indoor scene synthesis systems. Existing methods directly model object joint distributions and express object relations implicitly within a scene, thereby hindering the controllability of generation. We introduce InstructScene, a novel generative framework that integrates a semantic graph prior and a layout decoder to improve controllability and fidelity for 3D scene synthesis. The proposed semantic graph prior jointly learns scene appearances and layout distributions, exhibiting versatility across various downstream tasks in a zero-shot manner. To facilitate the benchmarking for text-driven 3D scene synthesis, we curate a high-quality dataset of scene-instruction pairs with large language and multimodal models. Extensive experimental results reveal that the proposed method surpasses existing state-of-the-art approaches by a large margin. Thorough ablation studies confirm the efficacy of crucial design components. Project page: https://chenguolin.github.io/projects/InstructScene.

## item_id: m_2691

TITLE: Localised Generative Flows

ABSTRACT: We argue that flow-based density models based on continuous bijections are limited in their ability to learn target distributions with complicated topologies, and propose localised generative flows (LGFs) to address this problem. LGFs are composed of stacked continuous mixtures of bijections, which enables each bijection to learn a local region of the target rather than its entirety. Our method is a generalisation of existing flow-based methods, which can be used without modification as the basis for an LGF model. Unlike normalising flows, LGFs do not permit exact computation of log likelihoods, but we propose a simple variational scheme that performs well in practice. We show empirically that LGFs yield improved performance across a variety of common density estimation tasks.

## item_id: m_2692

TITLE: QXplore: Q-Learning Exploration by Maximizing Temporal Difference Error

ABSTRACT: A major challenge in reinforcement learning is exploration, especially when reward landscapes are sparse. Several recent methods provide an intrinsic motivation to explore by directly encouraging agents to seek novel states. A potential disadvantage of pure state novelty-seeking behavior is that unknown states are treated equally regardless of their potential for future reward. In this paper, we propose an exploration objective using the temporal difference error experienced on extrinsic rewards as a secondary reward signal for exploration in deep reinforcement learning. Our objective yields novelty-seeking in the absence of extrinsic reward, while accelerating exploration of reward-relevant states in sparse (but nonzero) reward landscapes. This objective draws inspiration from dopaminergic pathways in the brain that influence animal behavior. We implement the objective with an adversarial Q-learning method in which Q and Qx are the action-value functions for extrinsic and secondary rewards, respectively. Secondary reward is given by the absolute value of the TD-error of Q. Training is off-policy, based on a replay buffer containing a mix of trajectories sampled using Q and Qx.  We characterize performance on a set of continuous control benchmark tasks, and demonstrate comparable or faster convergence on all tasks when compared with other state-of-the-art exploration methods.

## item_id: m_2693

TITLE: DualTune: Decoupled Fine-tuning for On-Device Agentic Systems

ABSTRACT: The deployment of Large Language Models (LLMs) as agentic orchestrators has revolutionized task automation, but the need for privacy-preserving, cost-effective solutions demands on-device inference capabilities. However, local LLMs consistently underperform compared to frontier models in tool calling scenarios, struggling with both tool selection from large tool sets and accurate argument generation for complex parameter structures. 
We introduce a methodology that disaggregates a tool-calling task into two distinct subtasks: tool selection and argument generation. We propose "decoupled fine-tuning", a novel post-training approach that employs LoRA fine-tuning to create dedicated LoRA adapters for tool selection and tool-specific argument generation using separate loss masking for each of the subtasks. Furthermore, we present DualTune, an inference framework that leverages the LoRA adapters created using decoupled fine-tuning to perform efficient agent orchestration with the help of local models on end-user devices. DualTune decomposes the tool-call generation step into tool selection and argument generation, and dynamically loads the corresponding LoRA adapters to generate tool calls. Additionally, DualTune implements hierarchical orchestration to restrict the number of tools required for tool selection. Our experiments on the MCP-Bench benchmark demonstrate that the Qwen-2.5-7B model trained using decoupled fine-tuning improves the tool calling accuracy of the base model by 46%, and outperforms other local reasoning, non-reasoning and fine-tuned models of similar size in all cases, and models that are 2x larger, in most cases.

## item_id: m_2694

TITLE: Large Learning Rate Tames Homogeneity: Convergence and Balancing Effect

ABSTRACT: Recent empirical advances show that training deep models with large learning rate often improves generalization performance. However, theoretical justifications on the benefits of large learning rate are highly limited, due to challenges in analysis. In this paper, we consider using Gradient Descent (GD) with a large learning rate on a homogeneous matrix factorization problem, i.e., $\min_{X, Y} \|A - XY^\top\|_{\sf F}^2$. We prove a convergence theory for constant large learning rates well beyond $2/L$, where $L$ is the largest eigenvalue of Hessian at the initialization. Moreover, we rigorously establish an implicit bias of GD induced by such a large learning rate, termed `balancing', meaning that magnitudes of $X$ and $Y$ at the limit of GD iterations will be close even if their initialization is significantly unbalanced. Numerical experiments are provided to support our theory.

## item_id: m_2695

TITLE: Explainable Adversarial Learning: Implicit Generative Modeling of Random Noise during Training for Adversarial Robustness

ABSTRACT: We introduce Explainable Adversarial Learning, ExL, an approach for training neural networks that are intrinsically robust to adversarial attacks. We find that the implicit generative modeling of random noise with the same loss function used during posterior maximization, improves a model's understanding of the data manifold furthering adversarial robustness. We prove our approach's efficacy and provide a simplistic visualization tool for understanding adversarial data, using Principal Component Analysis. Our analysis reveals that adversarial robustness, in general, manifests in models with higher variance along the high-ranked principal components. We show that models learnt with our approach perform remarkably well against a wide-range of attacks. Furthermore, combining ExL with state-of-the-art adversarial training extends the robustness of a model, even beyond what it is adversarially trained for, in both white-box and black-box attack scenarios.

## item_id: m_2696

TITLE: Boosting LLM Translation Skills without General Ability Loss via Rationale Distillation

ABSTRACT: Large Language Models (LLMs) have achieved impressive results across numerous NLP tasks but still encounter difficulties in machine translation. Traditional methods to improve translation have typically involved fine-tuning LLMs using parallel corpora. However, vanilla fine-tuning often leads to catastrophic forgetting of the instruction-following capabilities and alignment with human preferences, compromising their broad general abilities and introducing potential security risks. These abilities, which are developed using proprietary and unavailable training data, make existing continual instruction tuning methods ineffective. To overcome this issue, we propose a novel approach called $\textbf{RaDis}$ ($\textbf{Ra}$tionale $\textbf{Dis}$tillation). RaDis harnesses the strong generative capabilities of LLMs to create rationales for training data, which are then “replayed” to prevent forgetting. These rationales $\textit{connect prior knowledge with new tasks}$, acting as $\textit{self-distillation targets}$ to regulate the training process. By jointly training on reference translations and self-generated rationales, the model can learn new translation skills while preserving its general abilities. Extensive experiments demonstrate that our method enhances machine translation performance while maintaining the broader capabilities of LLMs across other tasks. This work presents a pathway for creating more versatile LLMs that excel in specialized tasks without compromising generality or safety and provides a fresh angle for utilizing rationales in the CL field.

## item_id: m_2697

TITLE: FCR: Flow Chart Recognition Network for Program Synthesis

ABSTRACT:   Program synthesis is the task to automatically generate programs   based on user specification.   In this paper, we present a framework that synthesizes programs from images of flow chart that serve   as accurate and intuitive specifications. In order doing so, we propose a deep neural network called FCR that recognizes   graph structure from its image.    FCR is trained end-to-end, which can predict edges and nodes    of the flow chart simultaneously.   Experiments show that the accuracy to synthesize a program is 66.4%, and the accuracy to recognize edges and nodes are 94.1% and  67.9%, respectively. On average, it takes about 60 milliseconds to synthesize a program. 


## item_id: m_2698

TITLE: Is PGD-Adversarial Training Necessary? Alternative Training via a Soft-Quantization Network with Noisy-Natural Samples Only

ABSTRACT: Recent work on adversarial attack and defense suggests that projected gradient descent (PGD) is a universal $l_\infty$ first-order attack, and PGD adversarial training can significantly improve network robustness against a wide range of first-order $l_\infty$-bounded attacks, represented as the state-of-the-art defense method. However, an obvious weakness of PGD adversarial training is its highly-computational cost in generating adversarial samples, making it computationally infeasible for large and high-resolution real datasets such as the ImageNet dataset. In addition, recent work also has suggested a simple ``close-form'' solution to a robust model on MNIST. Therefore, a natural question raised is that is PGD adversarial training really necessary for robust defense? In this paper, surprisingly, we give a negative answer by proposing a training paradigm that is comparable to PGD adversarial training on several standard datasets, while only using noisy-natural samples. Specifically, we reformulate the min-max objective in PGD adversarial training by a minimization problem to minimize the original network loss plus $l_1$ norms of its gradients evaluated on the inputs (including adversarial samples). The original loss can be solved by natural training; for the $l_1$-norm loss, we propose a computationally-feasible solution by embedding a differentiable soft-quantization layer after the input layer of a network. We show formally that the soft-quantization layer trained with noisy-natural samples is an alternative approach to minimizing the $l_1$-gradient norms as in PGD adversarial training. Extensive empirical evaluations on three standard datasets including MNIST, CIFAR-10 and ImageNet show that our proposed models are comparable to PGD-adversarially-trained models under PGD and BPDA attacks using both cross-entropy and $CW_\infty$ losses. Remarkably, our method achieves a 24X speed-up on MNIST while maintaining a comparable defensive ability, and for the first time fine-tunes a robust Imagenet model within only two days. Code for the experiments will be released on Github.

## item_id: m_2699

TITLE: Non-Gaussian processes and neural networks at finite widths

ABSTRACT: Gaussian processes are ubiquitous in nature and engineering. A case in point is a class of neural networks in the infinite-width limit, whose priors correspond to Gaussian processes. Here we perturbatively extend this correspondence to finite-width neural networks, yielding non-Gaussian processes as priors. The methodology developed herein allows us to track the flow of preactivation distributions by progressively integrating out random variables from lower to higher layers, reminiscent of renormalization-group flow. We further develop a perturbative prescription to perform Bayesian inference with weakly non-Gaussian priors.

## item_id: m_2700

TITLE: Causal Contextual Bandits with Targeted Interventions

ABSTRACT: We study a contextual bandit setting where the learning agent has the ability to perform interventions on targeted subsets of the population, apart from possessing qualitative causal side-information. This novel formalism captures intricacies in real-world scenarios such as software product experimentation where targeted experiments can be conducted. However, this fundamentally changes the set of options that the agent has, compared to standard contextual bandit settings, necessitating new techniques. This is also the first work that integrates causal side-information in a contextual bandit setting, where the agent aims to learn a policy that maps contexts to arms (as opposed to just identifying one best arm). We propose a new algorithm, which we show empirically performs better than baselines on experiments that use purely synthetic data and on real world-inspired experiments. We also prove a bound on regret that theoretically guards performance.
