# Batch 22 — 100 items

## item_id: m_2101

TITLE: DiffAR: Denoising Diffusion Autoregressive Model for Raw Speech Waveform Generation

ABSTRACT: Diffusion models have recently been shown to be relevant for high-quality speech generation. Most work has been focused on generating spectrograms, and as such, they further require a subsequent model to convert the spectrogram to a waveform (i.e., a vocoder). This work proposes a diffusion probabilistic end-to-end model for generating a raw speech waveform. The proposed model is autoregressive, generating overlapping frames sequentially, where each frame is conditioned on a portion of the previously generated one. Hence, our model can effectively synthesize an unlimited speech duration while preserving high-fidelity synthesis and temporal coherence. We implemented the proposed model for unconditional and conditional speech generation, where the latter can be driven by an input sequence of phonemes, amplitudes, and pitch values. Working on the waveform directly has some empirical advantages. Specifically, it allows the creation of local acoustic behaviors, like vocal fry, which makes the overall waveform sounds more natural. Furthermore, the proposed diffusion model is stochastic and not deterministic; therefore, each inference generates a slightly different waveform variation, enabling abundance of valid realizations. Experiments show that the proposed model generates speech with superior quality compared with other state-of-the-art neural speech generation systems.

## item_id: m_2102

TITLE: UTC-IE: A Unified Token-pair Classification Architecture for Information Extraction

ABSTRACT: Information Extraction (IE) spans several tasks with different output structures, such as named entity recognition, relation extraction and event extraction. Previously, those tasks were solved with different models because of diverse task output structures. Through re-examining IE tasks, we find that all of them can be interpreted as extracting spans and span relations. We propose using the start and end token of a span to pinpoint the span in texts, and using the start-to-start and end-to-end token pairs of two spans to determine the relation. Hence, we can unify all IE tasks under the same token-pair classification formulation. Based on the reformulation, we propose a \textbf{U}nified \textbf{T}oken-pair \textbf{C}lassification architecture for \textbf{I}nformation \textbf{E}xtraction (\textbf{UTC-IE}), where we introduce Plusformer on top of the token-pair feature matrix. Specifically, it models axis-aware interaction with plus-shaped self-attention and local interaction with Convolutional Neural Network over token pairs. Experiments show that our approach outperforms task-specific and unified models on all tasks in 10 datasets, and achieves better or comparable results on 2 joint IE datasets. Moreover, UTC-IE speeds up over state-of-the-art models on IE tasks significantly in most datasets, which verifies the effectiveness of our architecture.

## item_id: m_2103

TITLE: MCTransformer: Combining Transformers And Monte-Carlo Tree Search For Offline Reinforcement Learning

ABSTRACT: Recent studies explored the framing of reinforcement learning as a sequence modeling problem, and then using Transformers to generate effective solutions. In this study, we introduce MCTransformer, a framework that combines Monte-Carlo Tree Search (MCTS) with Transformers. Our approach uses an actor-critic setup, where the MCTS component is responsible for navigating previously-explored states, aided by input from the Transformer. The Transformer controls the exploration and evaluation of new states, enabling an effective and efficient evaluation of various strategies. In addition to the development of highly effective strategies, our setup enables the use of more efficient sampling compared to existing MCTS-based solutions. MCTransformer is therefore able to perform a small number of evaluations for each newly-explored node, and to do so without degrading its performance. Our evaluation, conducted on the challenging and well-known problem of SameGame, shows that our approach outperforms both Transformer-based and MCTS-based solutions.

## item_id: m_2104

TITLE: Striving for Simplicity in Off-Policy Deep Reinforcement Learning

ABSTRACT: This paper advocates the use of offline (batch) reinforcement learning (RL) to help (1) isolate the contributions of exploitation vs. exploration in off-policy deep RL, (2) improve reproducibility of deep RL research, and (3) facilitate the design of simpler deep RL algorithms. We propose an offline RL benchmark on Atari 2600 games comprising all of the replay data of a DQN agent. Using this benchmark, we demonstrate that recent off-policy deep RL algorithms, even when trained solely on logged DQN data, can outperform online DQN. We present Random Ensemble Mixture (REM), a simple Q-learning algorithm that enforces optimal Bellman consistency on random convex combinations of multiple Q-value estimates. The REM algorithm outperforms more complex RL agents such as C51 and QR-DQN on the offline Atari benchmark and performs comparably in the online setting.

## item_id: m_2105

TITLE: Multi-task Learning on MNIST Image Datasets

ABSTRACT: We apply multi-task learning to image classification tasks on MNIST-like datasets. MNIST dataset has been referred to as the {\em drosophila} of machine learning and has been the testbed of many learning theories. The NotMNIST dataset and the FashionMNIST dataset have been created with the MNIST dataset as reference. In this work, we exploit these MNIST-like datasets for multi-task learning. The datasets are pooled together for learning the parameters of joint classification networks. Then the learned parameters are used as the initial parameters to retrain disjoint classification networks. The baseline recognition model are all-convolution neural networks. Without multi-task learning, the recognition accuracies for MNIST, NotMNIST and FashionMNIST are 99.56\%, 97.22\% and 94.32\% respectively. With multi-task learning to pre-train the networks, the recognition accuracies are respectively 99.70\%, 97.46\% and 95.25\%. The results re-affirm that multi-task learning framework, even with data with different genres, does lead to significant improvement.


## item_id: m_2106

TITLE: Crystal Diffusion Variational Autoencoder for Periodic Material Generation

ABSTRACT: Generating the periodic structure of stable materials is a long-standing challenge for the material design community. This task is difficult because stable materials only exist in a low-dimensional subspace of all possible periodic arrangements of atoms: 1) the coordinates must lie in the local energy minimum defined by quantum mechanics, and 2) global stability also requires the structure to follow the complex, yet specific bonding preferences between different atom types. Existing methods fail to incorporate these factors and often lack proper invariances. We propose a Crystal Diffusion Variational Autoencoder (CDVAE) that captures the physical inductive bias of material stability. By learning from the data distribution of stable materials, the decoder generates materials in a diffusion process that moves atomic coordinates towards a lower energy state and updates atom types to satisfy bonding preferences between neighbors. Our model also explicitly encodes interactions across periodic boundaries and respects permutation, translation, rotation, and periodic invariances. We significantly outperform past methods in three tasks: 1) reconstructing the input structure, 2) generating valid, diverse, and realistic materials, and 3) generating materials that optimize a specific property. We also provide several standard datasets and evaluation metrics for the broader machine learning community.

## item_id: m_2107

TITLE: Equivariant Graph Neural Operator for Modeling 3D Dynamics

ABSTRACT: Modeling the complex three-dimensional (3D) dynamics of relational systems is an important problem in the natural sciences, with applications ranging from molecular simulations to particle mechanics. Machine learning methods have achieved good success by learning graph neural networks to model spatial interactions. However, these approaches do not faithfully capture temporal correlations since they only model next-step predictions. In this work, we propose Equivariant Graph Neural Operator (EGNO), a novel and principled method that directly models dynamics as trajectories instead of just as next-step prediction. Different from existing methods, EGNO explicitly learns the temporal evolution of 3D dynamics where we formulate the dynamics as a function over time and learn neural operators to approximate it. To capture the temporal correlations while keeping the intrinsic SE(3)-equivariance, we develop equivariant temporal convolutions parameterized in the Fourier space and build EGNO by stacking the Fourier layers over equivariant networks. Comprehensive experiments in multiple domains, including particle simulations, human motion capture, and molecular dynamics, demonstrate the significantly superior performance of EGNO against existing methods, thanks to the equivariant temporal modeling.

## item_id: m_2108

TITLE: Visualizing High-Dimensional Trajectories on the Loss-Landscape of ANNs

ABSTRACT: Training artificial neural networks requires the optimization of highly non-convex loss functions. Throughout the years, the scientific community has developed an extensive set of tools and architectures that render this optimization task tractable and a general intuition has been developed for choosing hyper parameters that help the models reach minima that generalize well to unseen data. However, for the most part, the difference in trainability in between architectures, tasks and even the gap in network generalization abilities still remain unexplained. Visualization tools have played a key role in uncovering key geometric characteristics of the loss-landscape of ANNs and how they impact trainability and generalization capabilities. However, most visualizations methods proposed so far have been relatively limited in their capabilities since they are of linear nature and only capture features in a limited number of dimensions. We propose the use of the modern dimensionality reduction method PHATE which represents the SOTA in terms of capturing both global and local structures of high-dimensional data. We apply this method to visualize the loss landscape during and after training. Our visualizations reveal differences in training trajectories and generalization capabilities when used to make comparisons between optimization methods, initializations, architectures, and datasets. Given this success we anticipate this method to be used in making informed choices about these aspects of neural networks.

## item_id: m_2109

TITLE: Collaborative World Models: An Online-Offline Transfer RL Approach

ABSTRACT: Training offline reinforcement learning (RL) models with visual inputs is challenging due to the coupling of overfitting issue in representation learning and the risk of overestimating true value functions. Recent work has attempted to alleviate the overestimation bias by encouraging conservative behaviors beyond the scope of the offline dataset. This paper, in contrast, tries to build flexible constraints for the offline policies without impeding the exploration of potential advantages. The key idea is to leverage an off-the-shelf RL simulator, with which can be easily interacted in an online manner. In this auxiliary domain, we perform an actor-critic algorithm whose value model is aligned to the target data and thus serves as a “$\textit{test bed}$” for the offline policies. In this way, the online simulator can be used as the $\textit{playground}$ for the offline agent, allowing for mildly-conservative value estimation. Experimental results demonstrate the remarkable effectiveness of our approach in challenging environments such as DeepMind Control, Meta-World, and RoboDesk. It outperforms existing offline visual RL approaches by substantial margins.

## item_id: m_2110

TITLE: ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery

ABSTRACT: The advancements of language language models (LLMs) have piqued growing interest in developing LLM-based language agents to automate scientific discovery end-to-end, which has sparked both excitement and skepticism about the true capabilities of such agents. In this work, we argue that for an agent to fully automate scientific discovery, it must be able to complete all essential tasks in the workflow. Thus, we call for rigorous assessment of agents on individual tasks in a scientific workflow before making bold claims on end-to-end automation. To this end, we present ScienceAgentBench, a new benchmark for evaluating language agents for data-driven scientific discovery. To ensure the scientific authenticity and real-world relevance of our benchmark, we extract 102 tasks from 44 peer-reviewed publications in four disciplines and engage nine subject matter experts to validate them. We unify the target output for every task to a self-contained Python program file and employ an array of evaluation metrics to examine the generated programs, execution results, and costs. Each task goes through multiple rounds of manual validation by annotators and subject matter experts to ensure its annotation quality and scientific plausibility. We also propose two effective strategies to mitigate data contamination concerns. Using our benchmark, we evaluate five open-weight and proprietary LLMs, each with three frameworks: direct prompting, OpenHands, and self-debug. Given three attempts for each task, the best-performing agent can only solve 32.4% of the tasks independently and 34.3% with expert-provided knowledge. These results underscore the limited capacities of current language agents in generating code for data-driven discovery, let alone end-to-end automation for scientific research.

## item_id: m_2111

TITLE: Few-Shot Intent Inference via Meta-Inverse Reinforcement Learning

ABSTRACT: A significant challenge for the practical application of reinforcement learning toreal world problems is the need to specify an oracle reward function that correctly defines a task. Inverse reinforcement learning (IRL) seeks to avoid this challenge by instead inferring a reward function from expert behavior.  While appealing, it can be impractically expensive to collect datasets of demonstrations that cover the variation common in the real world (e.g. opening any type of door). Thus in practice, IRL must commonly be performed with only a limited set of demonstrations where it can be exceedingly difficult to unambiguously recover a reward function. In this work, we exploit the insight that demonstrations from other tasks can be used to constrain the set of possible reward functions by learning a "prior" that is specifically optimized for the ability to infer expressive reward functions from limited numbers of demonstrations.  We demonstrate that our method can efficiently recover rewards from images for novel tasks and provide intuition as to how our approach is analogous to learning a prior.

## item_id: m_2112

TITLE: Sample Relationships through the Lens of Learning Dynamics with Label Information

ABSTRACT: Although much research has been done on proposing new models or loss functions to improve the generalisation of artificial neural networks (ANNs), less attention has been directed to the data, which is also an important factor for training ANNs. In this work, we start from approximating the interaction between two samples, i.e. how learning one sample would modify the model's prediction on the other sample. Through analysing the terms involved in weight updates in supervised learning, we find that the signs of labels influence the interactions between samples. Therefore, we propose the labelled pseudo Neural Tangent Kernel (lpNTK) which takes label information into consideration when measuring the interactions between samples. We first prove that lpNTK would asymptotically converge to the well-known empirical NTK in terms of the Frobenius norm under certain assumptions. Secondly, we illustrate how lpNTK helps to understand learning phenomena identified in previous work, specifically the learning difficulty of samples and forgetting events during learning. Moreover, we also show that lpNTK can help to improve the generalisation performance of ANNs in image classification tasks, compared with the original whole training sets.

## item_id: m_2113

TITLE: On the Expressive Power of Deep Neural Networks

ABSTRACT: We study the expressive power of deep neural networks before and after
training. Considering neural nets after random initialization, we show that
three natural measures of expressivity all display an exponential dependence
on the depth of the network. We prove, theoretically and experimentally,
that all of these measures are in fact related to a fourth quantity, trajectory
length. This quantity grows exponentially in the depth of the network, and
is responsible for the depth sensitivity observed. These results translate
to consequences for networks during and after training. They suggest that
parameters earlier in a network have greater influence on its expressive power
– in particular, given a layer, its influence on expressivity is determined by
the remaining depth of the network after that layer. This is verified with
experiments on MNIST and CIFAR-10. We also explore the effect of training
on the input-output map, and find that it trades off between the stability
and expressivity of the input-output map.

## item_id: m_2114

TITLE: MetaFormer with Holistic Attention Modelling Improves Few-Shot Classification

ABSTRACT: Pre-trained vision transformers have revolutionized few-shot image classification, and it has been recently demonstrated that the previous common practice of meta-learning in synergy with these pre-trained transformers still holds significance and contributes to further advancing their performance. Unfortunately, the majority of working insights such as task conditioning are specifically tailored for convolutional neural networks, thus failing to translate effectively to vision transformers. This work sets out to bridge this gap via a coherent and lightweight framework called MetaFormer, which maintains compatibility with off-the-shelf pre-trained vision transformers. The proposed MetaFormer consists of two attention modules, i.e., the Sample-level Attention Module (SAM) and the Task-level Attention Module (TAM). SAM works in conjunction with the patch-level attention in Transformers to enforce consistency in the attended features across samples within a task, while TAM regularizes learning of the current task with an attended task in the pool. Empirical results on four few-shot learning benchmarks, i.e., miniImageNet, tieredImageNet, CIFAR-FS, and FC100, showcase that our approach achieves the new state-of-the-art at a very modest increase in computational overhead. Furthermore, our approach excels in cross-domain task generalization scenarios.

## item_id: m_2115

TITLE: Backpropagation Path Search On Adversarial Transferability

ABSTRACT: Transfer-based attackers craft adversarial examples against surrogate models and transfer them to victim models deployed in the black-box situation. It is generally accepted that gradients from diverse modules of surrogate models used for perturbation generation contribute differently to transferability. In this paper, we propose backPropagation pAth Search (PAS), which enhances adversarial transferability from the backpropagation perspective. We use structural reparameterization to make the basic modules of DNNs (i.e., convolution and activation) calculate forward as normal but backpropagate the gradients in a skip connection form. Thus, a DAG-based search space is constructed for the backpropagation path. PAS employs Bayesian Optimization to search for the most transferable path and reduces the search overhead by the one-step approximation. We conduct comprehensive attack experiments in a wide range of transfer settings, showing that PAS improves the attack success rate by a huge margin for both normally trained and defense models.

## item_id: m_2116

TITLE: Data-dependent Gaussian Prior Objective for Language Generation

ABSTRACT: For typical sequence prediction problems such as language generation, maximum likelihood estimation (MLE) has commonly been adopted as it encourages the predicted sequence most consistent with the ground-truth sequence to have the highest probability of occurring. However, MLE focuses on once-to-all matching between the predicted sequence and gold-standard, consequently treating all incorrect predictions as being equally incorrect. We refer to this drawback as {\it negative diversity ignorance} in this paper. Treating all incorrect predictions as equal unfairly downplays the nuance of these sequences' detailed token-wise structure. To counteract this, we augment the MLE loss by introducing an extra Kullback--Leibler divergence term derived by comparing a data-dependent Gaussian prior and the detailed training prediction. The proposed data-dependent Gaussian prior objective (D2GPo) is defined over a prior topological order of tokens and is poles apart from the data-independent Gaussian prior (L2 regularization) commonly adopted in smoothing the training of MLE. Experimental results show that the proposed method makes effective use of a more detailed prior in the data and has improved performance in typical language generation tasks, including supervised and unsupervised machine translation, text summarization, storytelling, and image captioning.


## item_id: m_2117

TITLE: Fine-grained Analysis of Sentence Embeddings Using Auxiliary Prediction Tasks

ABSTRACT: There is a lot of research interest in encoding variable length sentences into fixed
length vectors, in a way that preserves the sentence meanings. Two common
methods include representations based on averaging word vectors, and representations based on the hidden states of recurrent neural networks such as LSTMs.
The sentence vectors are used as features for subsequent machine learning tasks
or for pre-training in the context of deep learning. However, not much is known
about the properties that are encoded in these sentence representations and about
the language information they capture.
We propose a framework that facilitates better understanding of the encoded representations. We define prediction tasks around isolated aspects of sentence structure (namely sentence length, word content, and word order), and score representations by the ability to train a classifier to solve each prediction task when
using the representation as input. We demonstrate the potential contribution of the
approach by analyzing different sentence representation mechanisms. The analysis sheds light on the relative strengths of different sentence embedding methods with respect to these low level prediction tasks, and on the effect of the encoded
vector’s dimensionality on the resulting representations.

## item_id: m_2118

TITLE: Reward Learning with Trees: Methods and Evaluation

ABSTRACT: Recent efforts to learn reward functions from human feedback have tended to use deep neural networks, whose lack of transparency hampers our ability to explain agent behaviour or verify alignment. We explore the merits of learning intrinsically interpretable tree models instead. We develop a recently proposed method for learning reward trees from preference labels, and show it to be broadly competitive with neural networks on challenging high-dimensional tasks, with good robustness to limited or corrupted data. Having found that reward tree learning can be done effectively in complex settings, we then consider why it should be used, demonstrating that the interpretable reward structure gives significant scope for traceability, verification and explanation.

## item_id: m_2119

TITLE: PerLDiff: Controllable Street View Synthesis Using Perspective-Layout Diffusion Model

ABSTRACT: Controllable generation is considered a potentially vital approach to address the challenge of annotating 3D data, and the precision of such controllable generation becomes particularly imperative in the context of data production for autonomous driving. Existing methods focus on the integration of diverse generative information into controlling inputs, utilizing frameworks such as GLIGEN or ControlNet, to produce commendable outcomes in controllable generation. However, such approaches intrinsically restrict generation performance to the learning capacities of predefined network architectures. In this paper, we explore the integration of controlling information and introduce PerLDiff (\textbf{Per}spective-\textbf{L}ayout \textbf{Diff}usion Models), a method for effective street view image generation that fully leverages perspective 3D geometric information. Our PerLDiff employs 3D geometric priors to guide the generation of street view images with precise object-level control within the network learning process, resulting in a more robust and controllable output. Moreover, it demonstrates superior controllability compared to alternative layout control methods. Empirical results justify that our PerLDiff markedly enhances the precision of generation on the NuScenes and KITTI datasets.

## item_id: m_2120

TITLE: SpinVLA: A Spectral-Invariant Vision-Language-Action Model for Robotic Manipulation

ABSTRACT: Vision-language-action (VLA) models trained on large-scale robot demonstration datasets have achieved impressive in-distribution performance, yet they can fail catastrophically under minor domain shifts. For instance, a VLA-trained robot tasked to “pick the red block” may flounder due to various environmental disturbances such as lighting changes or scene clutter. To address this limitation, we propose SpinVLA, a novel end-to-end VLA architecture that leverages the mathematical equivalence between spectral decomposition and contrastive learning to improve robustness. Drawing inspiration from causal inference principles, which suggest that stable features persist across environments, we hypothesize that consistent patterns in successful demonstrations represent task-relevant information rather than spurious correlations, i.e., statistical associations unrelated to the true causal factors of task performance. Our approach integrates spectral decomposition to identify demonstration-consistent features, contrastive learning to enforce representational stability, and efficient low-rank adaptation modules for environment-specific tuning. Extensive experiments using the open-source LIBERO datasets show that SpinVLA significantly improves robotic manipulation task success rates compared to baseline VLAs under visual perturbations and the presence of out-of-distribution objects, while maintaining comparable in-distribution performance.

## item_id: m_2121

TITLE: Hyper-Connections

ABSTRACT: We present hyper-connections, a simple yet effective method that can serve as an alternative to residual connections. This approach specifically addresses common drawbacks observed in residual connection variants, such as the seesaw effect between gradient vanishing and representation collapse. Theoretically, hyper-connections allow the network to adjust the strength of connections between features at different depths and dynamically rearrange layers. We conduct experiments focusing on the pre-training of large language models, including dense and sparse models, where hyper-connections show significant performance improvements over residual connections. Additional experiments conducted on vision tasks also demonstrate similar improvements. We anticipate that this method will be broadly applicable and beneficial across a wide range of AI problems.

## item_id: m_2122

TITLE: Hierarchical Meta Reinforcement Learning for Multi-Task Environments

ABSTRACT: Deep reinforcement learning algorithms aim to achieve human-level intelligence by solving practical decisions-making problems, which are often composed of multiple sub-tasks. Complex and subtle relationships between sub-tasks make traditional methods hard to give a promising solution. We implement a first-person shooting environment with random spatial structures to illustrate a typical representative of this kind. A desirable agent should be capable of balancing between different sub-tasks: navigation to find enemies and shooting to kill them. To address the problem brought by the environment, we propose a Meta Soft Hierarchical reinforcement learning framework (MeSH), in which each low-level sub-policy focuses on a specific sub-task respectively and high-level policy automatically learns to utilize low-level sub-policies through meta-gradients. The proposed framework is able to disentangle multiple sub-tasks and discover proper low-level policies under different situations. The effectiveness and efficiency of the framework are shown by a series of comparison experiments. Both environment and algorithm code will be provided for open source to encourage further research.

## item_id: m_2123

TITLE: REV: Information-Theoretic Evaluation of Free-Text Rationales

ABSTRACT: Free-text rationales are a promising step towards explainable AI, yet their evaluation remains an open research problem. While existing metrics have mostly focused on measuring the direct association between the rationale and a given label, we argue that an ideal metric should also be able to focus on the new information uniquely provided in the rationale that is otherwise not provided in the input or the label. We investigate this research problem from an information-theoretic perspective using the conditional $\mathcal{V}$-information \citep{hewitt-etal-2021-conditional}. More concretely, we propose a metric called REV (Rationale Evaluation with conditional $\mathcal{V}$-information), that can quantify the new information in a rationale supporting a given label beyond the information already available in the input or the label. Experiments on reasoning tasks across four benchmarks, including few-shot prompting with GPT-3, demonstrate the effectiveness of REV in evaluating different types of rationale-label pairs, compared to existing metrics. Through several quantitative comparisons, we demonstrate the capability of REV in providing more sensitive measurements of new information in free-text rationales with respect to a label. Furthermore, REV is consistent with human judgments on rationale evaluations. Overall, when used alongside traditional performance metrics, REV provides deeper insights into a models' reasoning and prediction processes.

## item_id: m_2124

TITLE: Improving One-Shot NAS By Suppressing The Posterior Fading

ABSTRACT: There is a growing interest in automated neural architecture search (NAS). To improve the efficiency of NAS, previous approaches adopt  weight sharing method to force all models share the same set of weights.  However, it has been observed that a model performing better with shared weights does not necessarily perform  better when trained alone. In this paper, we analyse existing weight sharing one-shot NAS approaches from a Bayesian point of view and identify the posterior fading problem, which compromises the effectiveness of shared weights. To alleviate this problem, we present a practical approach to guide the parameter posterior towards its true distribution. Moreover, a hard latency constraint is introduced during the search so that the desired latency can be achieved. The resulted method, namely Posterior Convergent NAS (PC-NAS), achieves state-of-the-art performance under standard GPU latency constraint on ImageNet. In our small search space, our model PC-NAS-S attains76.8% top-1 accuracy, 2.1% higher than MobileNetV2 (1.4x) with the same latency. When adopted to our large search space, PC-NAS-L achieves 78.1% top-1 accuracy within 11ms. The discovered architecture also transfers well to other computer vision applications such as object detection and person re-identification.

## item_id: m_2125

TITLE: Non-greedy Gradient-based Hyperparameter Optimization Over Long Horizons

ABSTRACT: Gradient-based meta-learning has earned a widespread popularity in few-shot learning, but remains broadly impractical for tasks with long horizons (many gradient steps), due to memory scaling and gradient degradation issues. A common workaround is to learn meta-parameters online, but this introduces greediness which comes with a significant performance drop. In this work, we enable non-greedy meta-learning of hyperparameters over long horizons by sharing hyperparameters that are contiguous in time, and using the sign of hypergradients rather than their magnitude to indicate convergence. We implement this with forward-mode differentiation, which we extend to the popular momentum-based SGD optimizer. We demonstrate that the hyperparameters of this optimizer can be learned non-greedily without gradient degradation over $\sim 10^4$ inner gradient steps, by only requiring $\sim 10$ outer gradient steps. On CIFAR-10, we outperform greedy and random search methods for the same computational budget by nearly $10\%$. Code will be available upon publication.

## item_id: m_2126

TITLE: Efficient Differentiable Approximation of the Generalized Low-rank Regularization

ABSTRACT: Low-rank regularization (LRR) has been widely applied in various machine learning tasks, but the associated optimization is challenging. Directly optimizing the rank function under constraints is NP-hard in general. To overcome this difficulty, various relaxations of the rank function were studied. However, optimization of these relaxed LRRs typically depends on singular value decomposition, which is a time-consuming and nondifferentiable operator that cannot be optimized with gradient-based techniques. To address these challenges, in this paper we propose an efficient differentiable approximation of the generalized LRR. The considered LRR form subsumes many popular choices like the nuclear norm, the Schatten-$p$ norm, and various nonconvex relaxations. Our method enables LRR terms to be appended to loss functions in a plug-and-play fashion, and be conveniently optimized by off-the-shelf machine learning libraries. Furthermore, the proposed approximation solely depends on matrix multiplication, which is a GPU-friendly operation that enables efficient parallel implementation. In the experimental study, the proposed method is applied to various tasks, which demonstrates its versatility and efficiency.

## item_id: m_2127

TITLE: Inverse Constrained Reinforcement Learning

ABSTRACT: Standard reinforcement learning (RL) algorithms train agents to maximize given reward functions. However, many real-world applications of RL require agents to also satisfy certain constraints which may, for example, be motivated by safety concerns. Constrained RL algorithms approach this problem by training agents to maximize given reward functions while respecting \textit{explicitly} defined constraints. However, in many cases, manually designing accurate constraints is a challenging task. In this work, given a reward function and a set of demonstrations from an expert that maximizes this reward function while respecting \textit{unknown} constraints, we propose a framework to learn the most likely constraints that the expert respects. We then train agents to maximize the given reward function subject to the learned constraints. Previous works in this regard have either mainly been restricted to tabular settings or specific types of constraints or assume knowledge of transition dynamics of the environment. In contrast, we empirically show that our framework is able to learn arbitrary \textit{Markovian} constraints in high-dimensions in a model-free setting.

## item_id: m_2128

TITLE: Learning to superoptimize programs

ABSTRACT:   Code super-optimization is the task of transforming any given program to a more efficient version while preserving its input-output behaviour. In some sense, it is similar to the paraphrase problem from natural language processing where the intention is to change the syntax of an utterance without changing its semantics. Code-optimization has been the subject of years of research that has resulted in the development of rule-based transformation strategies that are used by compilers. More recently, however, a class of stochastic search based methods have been shown to outperform these strategies. This approach involves repeated sampling of modifications to the program from a proposal distribution, which are accepted or rejected based on whether they preserve correctness, and the improvement they achieve. These methods, however, neither learn from past behaviour nor do they try to leverage the semantics of the program under consideration. Motivated by this observation, we present a novel learning based approach for code super-optimization. Intuitively, our method works by learning the proposal distribution using unbiased estimators of the gradient of the expected improvement. Experiments on benchmarks comprising of automatically generated as well as existing (``Hacker's Delight'') programs show that the proposed method is able to significantly outperform state of the art approaches for code super-optimization.


## item_id: m_2129

TITLE: Fast Generic Interaction Detection for Model Interpretability and Compression

ABSTRACT: The ability of discovering feature interactions in a black-box model is vital to explainable deep learning. We propose a principled, global interaction detection method by casting our target as a multi-arm bandits problem and solving it swiftly with the UCB algorithm. This adaptive method is free of ad-hoc assumptions and among the cutting-edge methods with outstanding detection accuracy and stability. Based on the detection outcome, a lightweight and interpretable deep learning model (called ParaACE) is further built using the alternating conditional expectation (ACE) method. Our proposed ParaACE improves the prediction performance by 26 % and reduces the model size by 100+ times as compared to its Teacher model over various datasets. Furthermore, we show the great potential of our method for scientific discovery through interpreting various real datasets in the economics and smart medicine sectors. The code is available at https://github.com/zhangtj1996/ParaACE. 

## item_id: m_2130

TITLE: M3GIA: A Cognition Inspired Multilingual and Multimodal General Intelligence Ability Benchmark

ABSTRACT: As recent multi-modal large language models (MLLMs) have shown formidable proficiency on various complex tasks, there has been increasing attention on debating whether these models could eventually mirror human intelligence. However, existing benchmarks mainly focus on evaluating solely on task performance, such as the accuracy of identifying the attribute of an object. Combining well-developed cognitive science to understand the intelligence of MLLMs beyond superficial achievements remains largely unexplored. To this end, we introduce the first cognitive-driven multi-lingual and multi-modal benchmark to evaluate the general intelligence ability of MLLMs, dubbed M3GIA. Specifically, we identify five key cognitive factors based on the well-recognized Cattell-Horn-Carroll (CHC) model of intelligence and propose a novel evaluation metric. In addition, since most MLLMs are trained to perform in different languages, we go beyond English to encompass other languages, including Chinese, French, Spanish, Portuguese and Korean, to construct our M3GIA. We make sure all the data relevant to the cultural backgrounds are collected from their native context to avoid English-centric bias. We collected a significant corpus of data from human participants, revealing that the most advanced MLLM barely reaches the lower boundary of human performance in English, and there remains a pronounced disparity in the other five languages. Importantly, we found that designing IQ tests for MLLMs is crucial, as the evaluation of M3GIA achieves a significantly stronger alignment with human preferences compared to traditional task-oriented benchmarks. Moreover, grounded in CHC theory, we discovered that the number of samples seen by the vision encoder has a greater influence on the model's visual capabilities than its parameter size.

## item_id: m_2131

TITLE: Exploring Efficient Foundational Multi-modal Models for Video Summarization

ABSTRACT: Foundational models are able to generate text outputs given prompt instructions and text, audio, or image inputs. Recently these models have been combined to perform tasks on video, such as video summarization. Such video foundation models perform pre-training by aligning outputs from each modality-specific model into the same embedding space. Then the embeddings from each model are used within a language model, which is fine-tuned on a desired instruction set. Aligning each modality during pre-training is computationally expensive and prevents rapid testing of different base modality models. During fine-tuning, evaluation is carried out within in-domain videos where it is hard to understand the generalizability and data efficiency of these methods. To alleviate these issues we propose a plug-and-play video language model. It directly uses the texts generated from each input modality into the language model, avoiding pre-training alignment overhead. Instead of fine-tuning we leverage few-shot instruction adaptation strategies. We compare the performance versus the computational costs for our plug-and-play style method and baseline tuning methods. Finally, we explore the generalizability of each method during domain shift and present insights on what data is useful when training data is limited. Through this analysis, we present practical insights on how to leverage multi-modal foundational models for effective results given realistic compute and data limitations.

## item_id: m_2132

TITLE: Rendering Wireless Environments Useful for Gradient Estimators: A Zero-Order Stochastic Federated Learning Method

ABSTRACT: Federated learning (FL) is a novel approach to machine learning that allows multiple edge devices to collaboratively train a model without disclosing their raw data. However, several challenges hinder the practical implementation of this approach, especially when devices and the server communicate over wireless channels, as it suffers from communication and computation bottlenecks in this case. By utilizing a communication-efficient framework, we propose a novel zero-order (ZO) method with two types of gradient estimators, one-point and two-point, that harnesses the nature of the wireless communication channel without requiring the knowledge of the channel state coefficient. It is the first method that includes the wireless channel in the learning algorithm itself instead of wasting resources to analyze it and remove its impact. The two main difficulties of this work are that in FL, the objective function is usually not convex, which makes the extension of FL to ZO methods challenging, and that including the impact of wireless channels requires extra attention. However, we overcome these difficulties and comprehensively analyze the proposed zero-order federated learning (ZOFL) framework. We establish its convergence theoretically, and we prove a convergence rate of $O(\frac{1}{\sqrt[3]{K}})$ with the one-point estimate and $O(\frac{1}{\sqrt{K}})$ with the two-point one in the nonconvex setting. We further demonstrate the potential of our algorithms with experimental results, taking into account independent and identically distributed (IID) and non-IID device data distributions.

## item_id: m_2133

TITLE: VC dimensions for deep neural networks with bounded-rank weight matrices

ABSTRACT: Deep neural networks (DNNs) have seen immense success in the past decade, yet their lack of interpretability remains a challenge. Recent research on the VC (Vapnik-Chervonenkis) dimension of DNNs has provided valuable insights into the underlying mechanisms of deep learning's powerful generalization capabilities. Understanding the VC dimension offers a promising path toward unraveling the enigma of deep learning, ultimately leading to more interpretable and trustworthy AI systems. In this paper, we study the VC dimensions for DNNs with piecewise polynomial activations and bounded-rank weight matrices. Our main results show that the VC dimensions for DNNs with weight matrices that have bounded rank $r$ are at most $\mathcal{O}(nrL^2\log (nrL))$, where $n$ is the width of the network, and $L$ is the depth of the network. We also construct a ReLU DNN with bounded rank $r$ that can achieve the VC dimension $\Omega(nr)$, which confirms that the upper bound we obtain is nearly tight for large $n$. Based on these bounds, we compare the generalization power in terms of VC dimensions for various different DNN architectures.

## item_id: m_2134

TITLE: Self-conditioned Embedding Diffusion for Text Generation

ABSTRACT: Can continuous diffusion models bring the same performance breakthrough on natural language they did for image generation? To circumvent the discrete nature of text data, we can simply project tokens in a continuous space of embeddings, as is standard in language modeling. We propose Self-conditioned Embedding Diffusion (SED), a continuous diffusion mechanism that operates on token embeddings and allows to learn flexible and scalable diffusion models for both conditional and unconditional text generation. Through qualitative and quantitative evaluation, we show that our text diffusion models generate samples comparable with those produced by standard autoregressive language models — while being in theory more efficient on accelerator hardware at inference time.  Our work paves the way for scaling up diffusion models for text, similarly to autoregressive models, and for improving performance with recent refinements to continuous diffusion.

## item_id: m_2135

TITLE: MCAL: Minimum Cost Human-Machine Active Labeling

ABSTRACT: Today, ground-truth generation uses data sets annotated by cloud-based annotation services. These services rely on human annotation, which can be prohibitively expensive. In this paper, we consider the problem of hybrid human-machine labeling, which trains a classifier to accurately auto-label part of the data set. However, training the classifier can be expensive too. We propose an iterative approach that minimizes total overall cost by, at each step, jointly determining which samples to label using humans and which to label using the trained classifier. We validate our approach on well known public data sets such as Fashion-MNIST, CIFAR-10, CIFAR-100, and ImageNet. In some cases, our approach has 6× lower overall cost relative to human labeling the entire data set, and is always cheaper than the cheapest competing strategy.

## item_id: m_2136

TITLE: Bias-Variance Decomposition for Boltzmann Machines

ABSTRACT: We achieve bias-variance decomposition for Boltzmann machines using an information geometric formulation. Our decomposition leads to an interesting phenomenon that the variance does not necessarily increase when more parameters are included in Boltzmann machines, while the bias always decreases. Our result gives a theoretical evidence of the generalization ability of deep learning architectures because it provides the possibility of increasing the representation power with avoiding the variance inflation.

## item_id: m_2137

TITLE: Identifying through Flows for Recovering Latent Representations

ABSTRACT: Identifiability, or recovery of the true latent representations from which the observed data originates, is de facto a fundamental goal of representation learning. Yet, most deep generative models do not address the question of identifiability, and thus fail to deliver on the promise of the recovery of the true latent sources that generate the observations. Recent work proposed identifiable generative modelling using variational autoencoders (iVAE) with a theory of identifiability. Due to the intractablity of KL divergence between variational approximate posterior and the true posterior, however, iVAE has to maximize the evidence lower bound (ELBO) of the marginal likelihood, leading to suboptimal solutions in both theory and practice. In contrast, we propose an identifiable framework for estimating latent representations using a flow-based model (iFlow). Our approach directly maximizes the marginal likelihood, allowing for theoretical guarantees on identifiability, thereby dispensing with variational approximations. We derive its optimization objective in analytical form, making it possible to train iFlow in an end-to-end manner. Simulations on synthetic data validate the correctness and effectiveness of our proposed method and demonstrate its practical advantages over other existing methods.

## item_id: m_2138

TITLE: Here's My Point: Argumentation Mining with Pointer Networks

ABSTRACT: One of the major goals in automated argumentation mining is to uncover the argument structure present in argumentative text. In order to determine this structure, one must understand how different individual components of the overall argument are linked. General consensus in this field dictates that the argument components form a hierarchy of persuasion, which manifests itself in a tree structure. This work provides the first neural network-based approach to argumentation mining, focusing on extracting links between argument components, with a secondary focus on classifying types of argument components. In order to solve this problem, we propose to use a modification of a Pointer Network architecture. A Pointer Network is appealing for this task for the following reasons: 1) It takes into account the sequential nature of argument components; 2) By construction, it enforces certain properties of the tree structure present in argument relations; 3) The hidden representations can be applied to auxiliary tasks. In order to extend the contribution of the original Pointer Network model, we construct a joint model that simultaneously attempts to learn the type of argument component, as well as continuing to predict links between argument components. The proposed model achieves state-of-the-art results on two separate evaluation corpora. Furthermore, our results show that optimizing for both tasks, as well as adding a fully-connected layer prior to recurrent neural network input, is crucial for high performance.

## item_id: m_2139

TITLE: Learning and Data Selection in Big Datasets

ABSTRACT: Finding a dataset of minimal cardinality to characterize the optimal parameters of a model is of paramount importance in machine learning and distributed optimization over a network. This paper investigates the compressibility of large datasets. More specifically, we propose a framework that jointly learns the input-output mapping as well as the most representative samples of the dataset (sufficient dataset). Our analytical results show that the cardinality of the sufficient dataset increases sub-linearly with respect to the original dataset size. Numerical evaluations of real datasets reveal a large compressibility, up to 95%, without a noticeable drop in the learnability performance, measured by the generalization error.


## item_id: m_2140

TITLE: On the generalization capacity of neural networks during generic multimodal reasoning

ABSTRACT: The advent of the Transformer has led to the development of large language models (LLM), which appear to demonstrate human-like capabilities. To assess the generality of this class of models and a variety of other base neural network architectures to multimodal domains, we evaluated and compared their capacity for multimodal generalization. We introduce a multimodal question-answer benchmark to evaluate three specific types of out-of-distribution (OOD) generalization performance: distractor generalization (generalization in the presence of distractors), systematic compositional generalization (generalization to new task permutations), and productive compositional generalization (generalization to more complex tasks with deeper dependencies). While we found that most architectures faired poorly on most forms of generalization (e.g., RNNs and standard Transformers), models that leveraged cross-attention mechanisms between input domains, such as the Perceiver, fared better. Our positive results demonstrate that for multimodal distractor and systematic generalization, cross-attention is an important mechanism to integrate multiple sources of information. On the other hand, all architectures failed in productive generalization, suggesting fundamental limitations of existing architectures for specific types of multimodal OOD generalization. These results demonstrate the strengths and limitations of specific architectural components underlying modern neural models for multimodal reasoning. Finally, we provide *Generic COG* (gCOG), a configurable benchmark with several multimodal generalization splits, for future studies to explore.

## item_id: m_2141

TITLE: Stacked U-Nets: A No-Frills Approach to Natural Image Segmentation

ABSTRACT: Many imaging tasks require global information about all pixels in an image. Conventional bottom-up classification networks globalize information by decreasing resolution; features are pooled and down-sampled into a single output. But for semantic segmentation and object detection tasks, a network must provide higher-resolution pixel-level outputs. To globalize information while preserving resolution, many researchers propose the inclusion of sophisticated auxiliary blocks, but these come at the cost of a considerable increase in network size and computational cost. This paper proposes stacked u-nets (SUNets), which iteratively combine features from different resolution scales while maintaining resolution. SUNets leverage the information globalization power of u-nets in a deeper net- work architectures that is capable of handling the complexity of natural images. SUNets perform extremely well on semantic segmentation tasks using a small number of parameters.

## item_id: m_2142

TITLE: Efficient Offline Policy Optimization with a Learned Model

ABSTRACT: MuZero Unplugged presents a promising approach for offline policy learning from logged data. It conducts Monte-Carlo Tree Search (MCTS) with a learned model and leverages Reanalyze algorithm to learn purely from offline data. For good performance, MCTS requires accurate learned models and a large number of simulations, thus costing huge computing time. This paper investigates a few hypotheses where MuZero Unplugged may not work well under the offline RL settings, including 1) learning with limited data coverage; 2) learning from offline data of stochastic environments; 3) improperly parameterized models given the offline data; 4) with a low compute budget. We propose to use a regularized one-step look-ahead approach to tackle the above issues. Instead of planning with the expensive MCTS, we use the learned model to construct an advantage estimation based on a one-step rollout. Policy improvements are towards the direction that maximizes the estimated advantage with regularization of the dataset. We conduct extensive empirical studies with BSuite environments to verify the hypotheses and then run our algorithm on the RL Unplugged Atari benchmark. Experimental results show that our proposed approach achieves stable performance even with an inaccurate learned model. On the large-scale Atari benchmark, the proposed method outperforms MuZero Unplugged by 43%. Most significantly, it uses only 5.6% wall-clock time (i.e., 1 hour) compared to MuZero Unplugged (i.e., 17.8 hours) to achieve a 150% IQM normalized score with the same hardware and software stacks. Our implementation is open-sourced at https://github.com/sail-sg/rosmo.

## item_id: m_2143

TITLE: Semantic Code Repair using Neuro-Symbolic Transformation Networks

ABSTRACT: We study the problem of semantic code repair, which can be broadly defined as automatically fixing non-syntactic bugs in source code. The majority of past work in semantic code repair assumed access to unit tests against which candidate repairs could be validated. In contrast, the goal here is to develop a strong statistical model to accurately predict both bug locations and exact fixes without access to information about the intended correct behavior of the program. Achieving such a goal requires a robust contextual repair model, which we train on a large corpus of real-world source code that has been augmented with synthetically injected bugs. Our framework adopts a two-stage approach where first a large set of repair candidates are generated by rule-based processors, and then these candidates are scored by a statistical model using a novel neural network architecture which we refer to as Share, Specialize, and Compete. Specifically, the architecture (1) generates a  shared encoding of the source code using an RNN over the abstract syntax tree, (2) scores each candidate repair using specialized network modules, and (3) then normalizes these scores together so they can compete against one another in comparable probability space. We evaluate our model on a real-world test set gathered from GitHub containing four common categories of bugs. Our model is able to predict the exact correct repair 41% of the time with a single guess, compared to 13% accuracy for an attentional sequence-to-sequence model.

## item_id: m_2144

TITLE: An Actor-Critic Algorithm for Sequence Prediction

ABSTRACT: We present an approach to training neural networks to generate sequences using actor-critic methods from reinforcement learning (RL). Current log-likelihood training methods are limited by the discrepancy between their training and testing modes, as models must generate tokens conditioned on their previous guesses rather than the ground-truth tokens. We address this problem by introducing a textit{critic} network that is trained to predict the value of an output token, given the policy of an textit{actor} network. This results in a training procedure that is much closer to the test phase, and allows us to directly optimize for a task-specific score such as BLEU. Crucially, since we leverage these techniques in the supervised learning setting rather than the traditional RL setting, we condition the critic network on the ground-truth output. We show that our method leads to improved performance on both a synthetic task, and for German-English machine translation. Our analysis paves the way for such methods to be applied in natural language generation tasks, such as machine translation, caption generation, and dialogue modelling. 

## item_id: m_2145

TITLE: Backpropagation through the Void: Optimizing control variates for black-box gradient estimation

ABSTRACT: Gradient-based optimization is the foundation of deep learning and reinforcement learning.
Even when the mechanism being optimized is unknown or not differentiable, optimization using high-variance or biased gradient estimates is still often the best strategy. We introduce a general framework for learning low-variance, unbiased gradient estimators for black-box functions of random variables, based on gradients of a learned function.
These estimators can be jointly trained with model parameters or policies, and are applicable in both discrete and continuous settings. We give unbiased, adaptive analogs of state-of-the-art reinforcement learning methods such as advantage actor-critic. We also demonstrate this framework for training discrete latent-variable models.

## item_id: m_2146

TITLE: D3PG: Deep Differentiable Deterministic Policy Gradients

ABSTRACT: Over the last decade, two competing control strategies have emerged for solving complex control tasks with high efficacy. Model-based control algorithms, such as model-predictive control (MPC) and trajectory optimization, peer into the gradients of underlying system dynamics in order to solve control tasks with high sample efficiency.  However, like all gradient-based numerical optimization methods,model-based control methods are sensitive to intializations and are prone to becoming trapped in local minima. Deep reinforcement learning (DRL), on the other hand, can somewhat alleviate these issues by exploring the solution space through sampling — at the expense of computational cost. In this paper, we present a hybrid method that combines the best aspects of gradient-based methods and DRL. We base our algorithm on the deep deterministic policy gradients (DDPG) algorithm and propose a simple modification that uses true gradients from a differentiable physical simulator to increase the convergence rate of both the actor and the critic.  We demonstrate our algorithm on seven 2D robot control tasks, with the most complex one being a differentiable half cheetah with hard contact constraints. Empirical results show that our method boosts the performance of DDPGwithout sacrificing its robustness to local minima.

## item_id: m_2147

TITLE: A Program to Build E(N)-Equivariant Steerable CNNs 

ABSTRACT: Equivariance is becoming an increasingly popular design choice to build data efficient neural networks by exploiting prior knowledge about the symmetries of the problem at hand. Euclidean steerable CNNs are one of the most common classes of equivariant networks. While the constraints these architectures need to satisfy are understood, existing approaches are tailored to specific (classes of) groups. No generally applicable method that is practical for implementation has been described so far. In this work, we generalize the Wigner-Eckart theorem proposed in Lang & Weiler (2020), which characterizes general $G$-steerable kernel spaces for compact groups $G$ over their homogeneous spaces, to arbitrary $G$-spaces. This enables us to directly parameterize filters in terms of a band-limited basis on the whole space rather than on $G$'s orbits, but also to easily implement steerable CNNs equivariant to a large number of groups. To demonstrate its generality, we instantiate our method on a variety of isometry groups acting on the Euclidean space $\mathbb{R}^3$. Our framework allows us to build $E(3)$ and $SE(3)$-steerable CNNs like previous works, but also CNNs with arbitrary $G\leq O(3)$-steerable kernels. For example, we build 3D CNNs equivariant to the symmetries of platonic solids or choose $G=SO(2)$ when working with 3D data having only azimuthal symmetries. We compare these models on 3D shapes and molecular datasets, observing improved performance by matching the model's symmetries to the ones of the data.

## item_id: m_2148

TITLE: Cross-Dimensional Self-Attention for Multivariate, Geo-tagged Time Series Imputation

ABSTRACT: Many real-world applications involve multivariate, geo-tagged time series data: at each location, multiple sensors record corresponding measurements. For example, air quality monitoring system records PM2.5, CO, etc. The resulting time-series data often has missing values due to device outages or communication errors. In order to impute the missing values, state-of-the-art methods are built on Recurrent Neural Networks (RNN), which process each time stamp sequentially, prohibiting the direct modeling of the relationship between distant time stamps. Recently, the self-attention mechanism has been proposed for sequence modeling tasks such as machine translation, significantly outperforming RNN because the relationship between each two time stamps can be modeled explicitly. In this paper, we are the first to adapt the self-attention mechanism for multivariate, geo-tagged time series data. In order to jointly capture the self-attention across different dimensions (i.e. time, location and sensor measurements) while keep the size of attention maps reasonable, we propose a novel approach called Cross-Dimensional Self-Attention (CDSA) to process each dimension sequentially, yet in an order-independent manner. On three real-world datasets, including one our newly collected NYC-traffic dataset, extensive experiments demonstrate the superiority of our approach compared to state-of-the-art methods for both imputation and forecasting tasks. 


## item_id: m_2149

TITLE: Exploring the Space of Black-box Attacks on Deep Neural Networks

ABSTRACT: Existing black-box attacks on deep neural networks (DNNs) so far have largely focused on transferability, where an adversarial instance generated for a locally trained model can “transfer” to attack other learning models. In this paper, we propose novel Gradient Estimation black-box attacks for adversaries with query access to the target model’s class probabilities, which do not rely on transferability. We also propose strategies to decouple the number of queries required to generate each adversarial sample from the dimensionality of the input. An iterative variant of our attack achieves close to 100% adversarial success rates for both targeted and untargeted attacks on DNNs. We carry out extensive experiments for a thorough comparative evaluation of black-box attacks and show that the proposed Gradient Estimation attacks outperform all transferability based black-box attacks we tested on both MNIST and CIFAR-10 datasets, achieving adversarial success rates similar to well known, state-of-the-art white-box attacks. We also apply the Gradient Estimation attacks successfully against a real-world content moderation classiﬁer hosted by Clarifai. Furthermore, we evaluate black-box attacks against state-of-the-art defenses. We show that the Gradient Estimation attacks are very effective even against these defenses.

## item_id: m_2150

TITLE: Private and Efficient Meta-Learning with Low Rank and Sparse decomposition

ABSTRACT: Meta-learning is critical for a variety of practical ML systems -- like personalized recommendations systems -- that are  required to generalize to new tasks despite a small number of task-specific training points. Existing meta-learning techniques use two complementary approaches of either learning a low-dimensional representation of points for all tasks, or task-specific fine-tuning of a global model trained using all the tasks. In this work, we propose a novel meta-learning framework that combines both the techniques to enable handling of a large number of data-starved tasks. Our framework models network weights as a sum of low-rank  and sparse matrices. This allows us to capture information from multiple domains together in the low-rank part while still allowing task specific personalization using the sparse part.  We instantiate and study the framework in the linear setting, where the problem reduces to that of estimating the sum of a rank-$r$ and a $k$-column sparse matrix using a small number of linear measurements. We propose an alternating minimization method with hard thresholding -- AMHT-LRS -- to learn the low-rank and sparse part effectively and efficiently. For the realizable, Gaussian data setting, we show that AMHT-LRS indeed solves the problem efficiently with nearly optimal samples.  We extend  AMHT-LRS  to ensure that it preserves privacy of each individual user in the dataset, while still ensuring strong  generalization with nearly optimal number of samples. Finally, on multiple datasets, we demonstrate that the framework allows personalized models to obtain superior performance in the data-scarce regime.

## item_id: m_2151

TITLE: Diffusion Models Improve Adversarial Robustness by Compressing Image Space

ABSTRACT: Recent work suggests that diffusion models significantly enhance empirical adversarial robustness. While several intuitive explanations have been proposed, the precise mechanisms remain unclear. In this work, we systematically investigate how diffusion models improve adversarial robustness. First, we observe that diffusion models intriguingly increase, rather than decrease, the $\ell_p$ distance to clean samples—challenging the notion that purification denoises inputs closer to the clean data. Second, we find that the purified images are heavily influenced by the internal randomness of diffusion models. When the randomness of the diffusion model is fixed, diffusion models substantially compress the image space. Importantly, we discover a lawful relationship between the adversarial robustness gain and the model’s ability to compress the image space, quantified by the expected compression rate (CR). Further theoretical analyses show that (i) convergent score fields encoded in diffusion models explain these compression effects, and (ii) under a low-dimensional data manifold hypothesis, the expected CR captures the compression along off-manifold directions. Our findings uncover the precise mechanisms underlying diffusion-based purification and offer guidance for developing more effective and principled adversarial purification systems.

## item_id: m_2152

TITLE: Few-shot Backdoor Attacks via Neural Tangent Kernels

ABSTRACT: In a backdoor attack, an attacker injects corrupted examples into the training set. The goal of the attacker is to cause the final trained model to predict the attacker's desired target label when a predefined trigger is added to test inputs. Central to these attacks is the trade-off between the success rate of the attack and the number of corrupted training examples injected. We pose this attack as a novel bilevel optimization problem: construct strong poison examples that maximize the attack success rate of the trained model. We use neural tangent kernels to approximate the training dynamics of the model being attacked and automatically learn strong poison examples. We experiment on subclasses of CIFAR-10 and ImageNet with WideResNet-34 and ConvNeXt architectures on periodic and patch trigger attacks and show that NTBA-designed poisoned examples achieve, for example, an attack success rate of  90% with ten times smaller number of poison examples injected compared to the baseline. We provided an interpretation of the NTBA-designed attacks using the analysis of kernel linear regression. We further demonstrate a vulnerability in overparametrized deep neural networks, which is revealed by the shape of the neural tangent kernel.


## item_id: m_2153

TITLE: SpikeGrad: An ANN-equivalent Computation Model for Implementing Backpropagation with Spikes

ABSTRACT: Event-based neuromorphic systems promise to reduce the energy consumption of deep neural networks by replacing expensive floating point operations on dense matrices by low energy, sparse operations on spike events. While these systems can be trained increasingly well using approximations of the backpropagation algorithm, this usually requires high precision errors and is therefore incompatible with the typical communication infrastructure of neuromorphic circuits. In this work, we analyze how the gradient can be discretized into spike events when training a spiking neural network. To accelerate our simulation, we show that using a special implementation of the integrate-and-fire neuron allows us to describe the accumulated activations and errors of the spiking neural network in terms of an equivalent artificial neural network, allowing us to largely speed up training compared to an explicit simulation of all spike events. This way we are able to demonstrate that even for deep networks, the gradients can be discretized sufficiently well with spikes if the gradient is properly rescaled. This form of spike-based backpropagation enables us to achieve equivalent or better accuracies on the MNIST and CIFAR10 datasets than comparable state-of-the-art spiking neural networks trained with full precision gradients. The algorithm, which we call SpikeGrad, is based on only accumulation and comparison operations and can naturally exploit sparsity in the gradient computation, which makes it an interesting choice for a spiking neuromorphic systems with on-chip learning capacities.

## item_id: m_2154

TITLE: Visually-Augmented Language Modeling

ABSTRACT: Human language is grounded on multimodal knowledge including visual knowledge like colors, sizes, and shapes. However, current large-scale pre-trained language models rely on the text-only self-supervised training with massive text data, which precludes them from utilizing relevant visual information when necessary. To address this, we propose a novel pre-training framework, named VaLM, to Visually-augment text tokens with retrieved relevant images for Language Modeling. Specifically, VaLM builds on a novel latent text-image alignment method via an image retrieval module to fetch corresponding images given a textual context. With the visually-augmented context, VaLM uses a visual knowledge fusion layer to enable multimodal grounded language modeling by attending on both text context and visual knowledge in images. We evaluate VaLM on various visual knowledge intensive commonsense reasoning tasks, which require visual information to excel. The experimental results illustrate that VaLM outperforms all strong language-only and vision-language baselines with substantial gains on reasoning object commonsense including color, size, and shape.

## item_id: m_2155

TITLE: Controlling Space and Time with Diffusion Models

ABSTRACT: We present 4DiM, a cascaded diffusion model for 4D novel view synthesis (NVS), supporting generation with arbitrary camera trajectories and timestamps, in natural scenes, conditioned on one or more images. With a novel architecture and sampling procedure, we enable training on a mixture of 3D (with camera pose), 4D (pose+time) and video (time but no pose) data, which greatly improves generalization to unseen images and camera pose trajectories over prior works which generally operate in limited domains (e.g., object centric).
4DiM is the first-ever NVS method with intuitive metric-scale camera pose control enabled by our novel calibration pipeline for structure-from-motion-posed data. Experiments demonstrate that 4DiM outperforms prior 3D NVS models both in terms of 
image fidelity and pose alignment, while also enabling the generation of scene dynamics. 4DiM provides a general framework for a variety of tasks including single-image-to-3D, two-image-to-video (interpolation and extrapolation), and pose-conditioned video-to-video translation, which we illustrate qualitatively on a variety of scenes.
See https://4d-diffusion.github.io for video samples.

## item_id: m_2156

TITLE: Adversarial Sampling for Active Learning

ABSTRACT: This paper proposes ASAL, a new pool based active learning method that generates high entropy samples. Instead of directly annotating the synthetic samples, ASAL searches similar samples from the pool and includes them for training. Hence, the quality of new samples is high and annotations are reliable.  ASAL is particularly suitable for large data sets because it achieves a better run-time complexity (sub-linear) for sample selection than traditional uncertainty sampling (linear). We present a comprehensive set of experiments on two data sets and show that ASAL outperforms similar methods and clearly exceeds the established baseline (random sampling).  In the discussion section we analyze in which situations ASAL performs best and why it is sometimes hard to outperform random sample selection. To the best of our knowledge this is the first adversarial active learning technique that is applied for multiple class problems using deep convolutional classifiers and demonstrates superior performance than random sample selection.

## item_id: m_2157

TITLE: A Near-Optimal Recipe for Debiasing Trained Machine Learning Models

ABSTRACT: We present an efficient and scalable algorithm for debiasing trained models, including deep neural networks (DNNs), which we prove to be near-optimal by bounding its excess Bayes risk.  Unlike previous black-box reduction methods to cost-sensitive classification rules, the proposed algorithm operates on models that have been trained without having to retrain the model. Furthermore, as the algorithm is based on projected stochastic gradient descent (SGD), it is particularly attractive for deep learning applications. We empirically validate the proposed algorithm on standard benchmark datasets across both classical algorithms and modern DNN architectures and demonstrate that it outperforms previous post-processing approaches for unbiased classification.

## item_id: m_2158

TITLE: {COMPANYNAME}11K: An Unsupervised Representation Learning Dataset for Arrhythmia Subtype Discovery

ABSTRACT: We release the largest public ECG dataset of continuous raw signals for representation learning containing over 11k patients and 2 billion labelled beats. Our goal is to enable semi-supervised ECG models to be made as well as to discover unknown subtypes of arrhythmia and anomalous ECG signal events. To this end, we propose an unsupervised representation learning task, evaluated in a semi-supervised fashion.  We provide a set of baselines for different feature extractors that can be built upon.  Additionally, we perform qualitative evaluations on results from PCA embeddings, where we identify some clustering of known subtypes indicating the potential for representation learning in arrhythmia sub-type discovery.

## item_id: m_2159

TITLE: Deep Graph Translation

ABSTRACT: Deep graph generation models have achieved great successes recently, among which, however, are typically unconditioned generative models that have no control over the target graphs are given an input graph. In this paper, we propose a novel Graph-Translation-Generative-Adversarial-Networks (GT-GAN) that transforms the input graphs into their target output graphs. GT-GAN consists of a graph translator equipped with innovative graph convolution and deconvolution layers to learn the translation mapping considering both global and local features, and a new conditional graph discriminator to classify target graphs by conditioning on input graphs. Extensive experiments on multiple synthetic and real-world datasets demonstrate that our proposed GT-GAN significantly outperforms other baseline methods in terms of both effectiveness and scalability. For instance, GT-GAN achieves at least 10X and 15X faster runtimes than GraphRNN and RandomVAE, respectively, when the size of the graph is around 50.

## item_id: m_2160

TITLE: Do Users Benefit From Interpretable Vision? A User Study, Baseline, And Dataset

ABSTRACT: A variety of methods exist to explain image classification models. However, whether they provide any benefit to users over simply comparing various inputs and the model’s respective predictions remains unclear. We conducted a user study (N=240) to test how such a baseline explanation technique performs against concept-based and counterfactual explanations. To this end, we contribute a synthetic dataset generator capable of biasing individual attributes and quantifying their relevance to the model. In a study, we assess if participants can identify the relevant set of attributes compared to the ground-truth. Our results show that the baseline outperformed concept-based explanations. Counterfactual explanations from an invertible neural network performed similarly as the baseline. Still, they allowed users to identify some attributes more accurately. Our results highlight the importance of measuring how well users can reason about biases of a model, rather than solely relying on technical evaluations or proxy tasks. We open-source our study and dataset so it can serve as a blue-print for future studies.

## item_id: m_2161

TITLE: PUMA: Secure Inference of LLaMA-7B in Five Minutes

ABSTRACT: With ChatGPT as a representative, tons of companies have began to provide ser-
vices based on large Transformers models. However, using such a service inevitably
leak users’ prompts to the model provider. Previous studies have studied secure in-
ference for Transformer models using secure multiparty computation (MPC), where
model parameters and clients’ prompts are kept secret. Despite this, these frame-
works are still limited in terms of model performance, efficiency, and deployment.
To address these limitations, we propose framework PUMA to enable fast and secure
Transformer model inference. Our framework designs high quality approximations
for expensive functions such as GeLU and softmax, and significantly reduce the
cost of secure inference while preserving the model performance. Additionally, we
design secure Embedding and LayerNorm procedures that faithfully implement the
desired functionality without undermining the Transformer architecture. PUMA is
about 2× faster than the state-of-the-art framework MPCFORMER(ICLR 2023) and
has similar accuracy as plaintext models without fine-tuning (which the previous
works failed to achieve). PUMA can even evaluate LLaMA-7B in around 5 minutes
to generate 1 token. To our best knowledge, this is the first time that a model with
such a parameter size is able to be evaluated under MPC.

## item_id: m_2162

TITLE: Multi-task learning with deep model based reinforcement learning

ABSTRACT: In recent years, model-free methods that use deep learning have achieved great success in many different reinforcement learning environments. Most successful approaches focus on solving a single task, while multi-task reinforcement learning remains an open problem. In this paper, we present a model based approach to deep reinforcement learning which we use to solve different tasks simultaneously. We show that our approach not only does not degrade but actually benefits from learning multiple tasks. For our model, we also present a new kind of recurrent neural network inspired by residual networks that decouples memory from computation allowing to model complex environments that do not require lots of memory. The code will be released before ICLR 2017.

## item_id: m_2163

TITLE: A Compressed Sensing View of Unsupervised Text Embeddings, Bag-of-n-Grams, and LSTMs

ABSTRACT: Low-dimensional vector embeddings, computed using LSTMs or simpler techniques, are a popular approach for capturing the “meaning” of text and a form of unsupervised learning useful for downstream tasks. However, their power is not theoretically understood. The current paper derives formal understanding by looking at the subcase of linear embedding schemes. Using the theory of compressed sensing we show that representations combining the constituent word vectors are essentially information-preserving linear measurements of Bag-of-n-Grams (BonG) representations of text. This leads to a new theoretical result about LSTMs: low-dimensional embeddings derived from a low-memory LSTM are provably at least as powerful on classification tasks, up to small error, as a linear classifier over BonG vectors, a result that extensive empirical work has thus far been unable to show. Our experiments support these theoretical findings and establish strong, simple, and unsupervised baselines on standard benchmarks that in some cases are state of the art among word-level methods. We also show a surprising new property of embeddings such as GloVe and word2vec: they form a good sensing matrix for text that is more efficient than random matrices, the standard sparse recovery tool, which may explain why they lead to better representations in practice.

## item_id: m_2164

TITLE: General-Purpose In-Context Learning by Meta-Learning Transformers

ABSTRACT: Modern machine learning requires system designers to specify aspects of the learning pipeline, such as losses, architectures, and optimizers. Meta-learning, or learning-to-learn, instead aims to learn those aspects, and promises to unlock greater capabilities with less manual effort. One particularly ambitious goal of meta-learning is to train general-purpose in-context learning algorithms from scratch, using only black-box models with minimal inductive bias. Such a model takes in training data, and produces test-set predictions across a wide range of problems, without any explicit definition of an inference model, training loss, or optimization algorithm. In this paper we show that Transformers and other black-box models can be meta-trained to act as general-purpose in-context learners. We characterize transitions between algorithms that generalize, algorithms that memorize, and algorithms that fail to meta-train at all, induced by changes in model size, number of tasks, and meta-optimization. We further show that the capabilities of meta-trained algorithms are bottlenecked by the accessible state size (memory) determining the next prediction, unlike standard models which are thought to be bottlenecked by parameter count. Finally, we propose practical interventions such as biasing the training distribution that improve the meta-training and meta-generalization of general-purpose in-context learning algorithms.

## item_id: m_2165

TITLE: OptiMUS: Optimization Modeling Using mip Solvers and large language models

ABSTRACT: Optimization problems are pervasive across various sectors, from manufacturing and distribution to healthcare. However, most such problems are still solved heuristically by hand rather than optimally by state-of-the-art solvers, as the expertise required to formulate and solve these problems limits the widespread adoption of optimization tools and techniques. We introduce OptiMUS, a Large Language Model (LLM)-based agent designed to formulate and solve MLIP problems from their natural language descriptions. OptiMUS is capable of developing mathematical models, writing and debugging solver code, developing tests, and checking the validity of generated solutions. To benchmark our agent, we present NLP4LP, a novel dataset of linear programming (LP) and mixed integer linear programming (MILP) problems. Our experiments demonstrate that OptiMUS is able to solve 67\% more problems compared to a basic LLM prompting strategy. The code OptiMUS and the data for NLP4LP are available at \href{https://anonymous.4open.science/r/nlp4lp-8F62/README.md}{https://anonymous.4open.science/r/nlp4lp-8F62/README.md}

## item_id: m_2166

TITLE: SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection

ABSTRACT: Fine-tuning on task-specific data to boost downstream performance is a crucial step for leveraging Large Language Models (LLMs). However, though fine-tuning enhances the model performance for specialized applications, previous studies have demonstrated that fine-tuning the models on several adversarial samples or even benign data can greatly comprise the model's pre-equipped alignment and safety capabilities. In this work, we propose SEAL, a novel framework to enhance safety in LLM fine-tuning. SEAL learns a data ranker based on the bilevel optimization to up rank the safe and high-quality fine-tuning data and down rank the unsafe or low-quality ones. Models trained with SEAL demonstrate superior quality over multiple baselines, with 8.5\% and 9.7\% win rate increase compared to random selection respectively on Llama-3-8b-Instruct and Merlinite-7b models. Our code is available on github https://github.com/hanshen95/SEAL.

## item_id: m_2167

TITLE: Associative Conversation Model: Generating Visual Information from Textual Information

ABSTRACT: In this paper, we propose the Associative Conversation Model that generates visual information from textual information and uses it for generating sentences in order to utilize visual information in a dialogue system without image input. In research on Neural Machine Translation, there are studies that generate translated sentences using both images and sentences, and these studies show that visual information improves translation performance. However, it is not possible to use sentence generation algorithms using images for the dialogue systems since many text-based dialogue systems only accept text input. Our approach generates (associates) visual information from input text and generates response text using context vector  fusing associative visual information and sentence textual information. A comparative experiment between our proposed model and a model without association showed that our proposed model is generating useful sentences by associating visual information related to sentences. Furthermore, analysis experiment of visual association showed that our proposed model generates (associates) visual information effective for sentence generation.

## item_id: m_2168

TITLE: Exploring Non-Contrastive Representation Learning for Deep Clustering

ABSTRACT: Existing deep clustering methods rely on contrastive learning for representation learning, which require negative examples to form an embedding space where all instances are well-separated. However, the negative examples inevitably give rise to the class collision issue, compromising the representation learning for clustering. In this paper, we explore the non-contrastive representation learning for deep clustering, termed NCC, which is based on BYOL, a representative method without negative examples.  First, we propose a positive sampling strategy to align one augmented view of instance with the neighbors of another view so that we can avoid the class collision issue caused by the negative examples and hence improve the within-cluster compactness. Second, we propose a novel prototypical contrastive loss, ProtoCL, which can encourage prototypical alignment between two augmented views and prototypical uniformity, hence maximizing the inter-cluster distance.  Moreover, we formulate NCC in an Expectation-Maximization (EM) framework, in which E-step utilizes spherical k-means to estimate the pseudo-labels of instances and distribution of prototypes from the target network and M-step leverages the proposed losses to optimize the online network. As a result, NCC is able to form an embedding space where all clusters are well-separated and within-cluster examples are compact. Experimental results on several clustering benchmark datasets as well as ImageNet-1K demonstrate that the proposed NCC outperforms the state-of-the-art methods by a significant margin.

## item_id: m_2169

TITLE: META-STORM: Generalized Fully-Adaptive Variance Reduced SGD for Unbounded Functions

ABSTRACT: We study the application of variance reduction (VR) techniques to general non-convex stochastic optimization problems. In this setting, the recent work STORM (Cutkosky & Orabona, 2019) overcomes the drawback of having to compute gradients of “mega-batches” that earlier VR methods rely on. There, STORM utilizes recursive momentum to achieve the VR effect and is then later made fully adaptive in STORM+ (Levy et al., 2021), where full-adaptivity removes the requirement for obtaining certain problem-specific parameters such as the smoothness of the objective and bounds on the variance and norm of the stochastic gradients in order to set the step size. However, STORM+ crucially relies on the assumption that the function values are bounded, excluding a large class of useful functions. In this work, we propose META-STORM, a generalized framework of STORM+ that removes this bounded function values assumption while still attaining the optimal convergence rate for non-convex optimization. META-STORM not only maintains full-adaptivity, removing the need to obtain problem specific parameters, but also improves the convergence rate’s dependency on the problem parameters. Furthermore, META-STORM can utilize a large range of parameter settings that subsumes previous methods allowing for more flexibility in a wider range of settings. Finally, we demonstrate the effectiveness of META-STORM through experiments across common deep learning tasks. Our algorithm improves upon the previous work STORM+ and is competitive with widely used algorithms after the addition of per-coordinate update and exponential moving average heuristics.

## item_id: m_2170

TITLE: Sparse Binary Compression: Towards Distributed Deep Learning with minimal Communication

ABSTRACT: Currently, progressively larger deep neural networks are trained on ever growing data corpora. In result, distributed training schemes are becoming increasingly relevant. A major issue in distributed training is the limited communication bandwidth between contributing nodes or prohibitive communication cost in general. 
%These challenges become even more pressing, as the number of computation nodes increases. 
To mitigate this problem we propose Sparse Binary Compression (SBC), a compression framework that allows for a drastic reduction of communication cost for distributed training. SBC combines existing techniques of communication delay and gradient sparsification with a novel binarization method and optimal weight update encoding to push compression gains to new limits. By doing so, our method also allows us to smoothly trade-off gradient sparsity and temporal sparsity to adapt to the requirements of the learning task. 
%We use tools from information theory to reason why SBC can achieve the striking compression rates observed in the experiments.
Our experiments show, that SBC can reduce the upstream communication on a variety of convolutional and recurrent neural network architectures by more than four orders of magnitude without significantly harming the convergence speed in terms of forward-backward passes. For instance, we can train ResNet50 on ImageNet in the same number of iterations to the baseline accuracy, using $\times 3531$ less bits or train it to a $1\%$ lower accuracy using $\times 37208$ less bits. In the latter case, the total upstream communication required is cut from 125 terabytes to 3.35 gigabytes for every participating client. Our method also achieves state-of-the-art compression rates in a Federated Learning setting with 400 clients.

## item_id: m_2171

TITLE: Discovering Motor Programs by Recomposing Demonstrations

ABSTRACT: In this paper, we present an approach to learn recomposable motor primitives across large-scale and diverse manipulation demonstrations. Current approaches to decomposing demonstrations into primitives often assume manually defined primitives and bypass the difficulty of discovering these primitives. On the other hand, approaches in primitive discovery put restrictive assumptions on the complexity of a primitive, which limit applicability to narrow tasks. Our approach attempts to circumvent these challenges by jointly learning both the underlying motor primitives and recomposing these primitives to form the original demonstration. Through constraints on both the parsimony of primitive decomposition and the simplicity of a given primitive, we are able to learn a diverse set of motor primitives, as well as a coherent latent representation for these primitives. We demonstrate both qualitatively and quantitatively, that our learned primitives capture semantically meaningful aspects of a demonstration. This allows us to compose these primitives in a hierarchical reinforcement learning setup to efficiently solve robotic manipulation tasks like reaching and pushing. Our results may be viewed at https://sites.google.com/view/discovering-motor-programs. 

## item_id: m_2172

TITLE: Universal Unlearnable Examples: Cluster-wise Perturbations without Label-consistency

ABSTRACT: There is a growing interest in employing unlearnable examples against privacy leaks on the Internet, which prevents the unauthorized models from being properly trained by adding invisible image noise. However, existing attack methods rely on an ideal assumption called label-consistency. In this work, we clarify a more practical scenario called \emph{label-inconsistency} that allows hackers and protectors to hold different labels for the same image. Inspired by disrupting the \emph{uniformity} and \emph{discrepancy}, we present a novel method called \emph{UniversalCP} on label-inconsistency scenario, which generates the universal unlearnable examples by cluster-wise perturbation. Furthermore, we investigate a new strategy for selecting the CLIP as the surrogate model, since vision-and-language pre-training models are trained on large-scale data and more semantic supervised information. We also verify the effectiveness of the proposed methods and the strategy for selecting surrogate models under a variety of experimental settings including black-box backbones, datasets and even commercial platforms Microsoft {\tt Azure} and Baidu {\tt PaddlePaddle}.

## item_id: m_2173

TITLE: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

ABSTRACT: We consider the two related problems of detecting if an example is misclassified or out-of-distribution. We present a simple baseline that utilizes probabilities from softmax distributions. Correctly classified examples tend to have greater maximum softmax probabilities than erroneously classified and out-of-distribution examples, allowing for their detection. We assess performance by defining several tasks in computer vision, natural language processing, and automatic speech recognition, showing the effectiveness of this baseline across all. We then show the baseline can sometimes be surpassed, demonstrating the room for future research on these underexplored detection tasks.

## item_id: m_2174

TITLE: Scaling up Trustless DNN Inference with Zero-Knowledge Proofs

ABSTRACT: As ML models have increased in capabilities and accuracy, so has the complexity of their deployments. Increasingly, ML model consumers are turning to service providers to serve the ML models in the ML-as-a-service (MLaaS) paradigm. As MLaaS proliferates, a critical requirement emerges: how can model consumers verify that the correct predictions were served, in the face of malicious, lazy, or buggy service providers?

We present the first practical ImageNet-scale method to verify ML model inference non-interactively, i.e., after the inference has been done. To do so, we leverage recent developments in ZK-SNARKs (zero-knowledge succinct non-interactive argument of knowledge), a form of zero-knowledge proofs. ZK-SNARKs allows us to verify ML model execution non-interactively and with only standard cryptographic hardness assumptions. We provide the first ZK-SNARK proof of valid inference for a full-resolution ImageNet model, achieving 79% top-5 accuracy, with verification taking as little as one second. We further use these ZK-SNARKs to design protocols to verify ML model execution in a variety of scenarios, including verifying MLaaS predictions, verifying MLaaS model accuracy, and using ML models for trustless retrieval. Together, our results show that ZK-SNARKs have the promise to make verified ML model inference practical.

## item_id: m_2175

TITLE: A Closer Look at Machine Unlearning for Large Language Models

ABSTRACT: Large language models (LLMs) may memorize sensitive or copyrighted content, raising privacy and legal concerns. Due to the high cost of retraining from scratch, researchers attempt to employ machine unlearning to remove specific content from LLMs while preserving the overall performance. In this paper, we discuss several issues in machine unlearning for LLMs and provide our insights on possible approaches. To address the issue of inadequate evaluation of model outputs after unlearning, we introduce three additional metrics to evaluate token diversity, sentence semantics, and factual correctness. We then categorize unlearning methods into untargeted and targeted, and discuss their issues respectively. Specifically, the behavior that untargeted unlearning attempts to approximate is unpredictable and may involve hallucinations, and existing regularization is insufficient for targeted unlearning. To alleviate these issues, we propose using the objective of maximizing entropy (ME) for untargeted unlearning and incorporate answer preservation (AP) loss as regularization for targeted unlearning. Experimental results across three scenarios, i.e., fictitious unlearning, continual unlearning, and real-world unlearning, demonstrate the effectiveness of our approaches. The code is available at https://github.com/sail-sg/closer-look-LLM-unlearning.

## item_id: m_2176

TITLE: Gradient-Based Neural DAG Learning

ABSTRACT: We propose a novel score-based approach to learning a directed acyclic graph (DAG) from observational data. We adapt a recently proposed continuous constrained optimization formulation to allow for nonlinear relationships between variables using neural networks. This extension allows to model complex interactions while avoiding the combinatorial nature of the problem. In addition to comparing our method to existing continuous optimization methods, we provide missing empirical comparisons to nonlinear greedy search methods. On both synthetic and real-world data sets, this new method outperforms current continuous methods on most tasks while being competitive with existing greedy search methods on important metrics for causal inference.

## item_id: m_2177

TITLE: DiffTaichi: Differentiable Programming for Physical Simulation

ABSTRACT: We present DiffTaichi, a new differentiable programming language tailored for building high-performance differentiable physical simulators. Based on an imperative programming language, DiffTaichi generates gradients of simulation steps using source code transformations that preserve arithmetic intensity and parallelism. A light-weight tape is used to record the whole simulation program structure and replay the gradient kernels in a reversed order, for end-to-end backpropagation.
We demonstrate the performance and productivity of our language in gradient-based learning and optimization tasks on 10 different physical simulators. For example, a differentiable elastic object simulator written in our language is 4.2x shorter than the hand-engineered CUDA version yet runs as fast, and is 188x faster than the TensorFlow implementation.
Using our differentiable programs, neural network controllers are typically optimized within only tens of iterations.

## item_id: m_2178

TITLE: No Spurious Local Minima: on the Optimization Landscapes of Wide and Deep Neural Networks

ABSTRACT: Empirical studies suggest that wide neural networks are comparably easy to optimize, but mathematical support for this observation is scarce. In this paper, we analyze the optimization landscapes of deep learning with wide networks. We prove especially that constraint and unconstraint empirical-risk minimization over such networks has no spurious local minima. Hence, our theories substantiate the common belief that increasing network widths not only improves the expressiveness of deep-learning pipelines but also facilitates their optimizations.

## item_id: m_2179

TITLE: A self-explanatory method for the black box problem on discrimination part of CNN

ABSTRACT: Recently, for finding inherent causality implied in CNN, the black box problem of its discrimination part, which is composed of all fully connected layers of the CNN, has been studied by different scientific communities. Many methods were proposed, which can extract various interpretable models from the optimal discrimination part based on inputs and outputs of the part for finding the inherent causality implied in the part. However, the inherent causality cannot readily be found. We think that the problem could be solved by shrinking an interpretable distance which can evaluate the degree for the discrimination part to be easily explained by an interpretable model. This paper proposes a lightweight interpretable model, Deep Cognitive Learning Model(DCLM). And then, a game method between the DCLM and the discrimination part is implemented for shrinking the interpretation distance. Finally, the proposed self-explanatory method was evaluated by some contrastive experiments with certain baseline methods on some standard image processing benchmarks. These experiments indicate that the proposed method can effectively find the inherent causality implied in the discrimination part of the CNN without largely reducing its generalization performance. Moreover, the generalization performance of the DCLM also can be improved.

## item_id: m_2180

TITLE: ChePAN: Constrained Black-Box Uncertainty Modelling with Quantile Regression

ABSTRACT: Most predictive systems currently in use do not report any useful information for auditing their associated uncertainty and evaluating the corresponding risk. Taking it for granted that their replacement may not be advisable in the short term, in this paper we propose a novel approach to modelling confidence in such systems while preserving their predictions. The method is based on the Chebyshev Polynomial Approximation Network (the ChePAN), a new way of modelling aleatoric uncertainty in a regression scenario. In the case addressed here, uncertainty is modelled by building conditional quantiles on top of the original pointwise forecasting system considered as a black box, i.e. without making assumptions about its internal structure. Furthermore, the ChePAN allows users to consistently choose how to constrain any predicted quantile with respect to the original forecaster. Experiments show that the proposed method scales to large size data sets and transfers the advantages of quantile regression to estimating black-box uncertainty.

## item_id: m_2181

TITLE: A Robust Initialization of Residual Blocks for Effective ResNet Training without Batch Normalization

ABSTRACT: Batch Normalization is an essential component of all state-of-the-art neural networks architectures. However, it introduces many practical issues so that in recent years a lot of research has been devoted to designing normalization-free architectures. In this paper, we show that weights initialization is key to train ResNet-like normalization-free networks. In particular, we propose a slight modification of the summation operation of a block output with the skip-connection branch so that the whole network is correctly initialized. We show that this modified architecture achieves competitive results on CIFAR-10 without additional regularization or algorithmic modifications.

## item_id: m_2182

TITLE: Residual Loss Prediction: Reinforcement Learning With No Incremental Feedback

ABSTRACT: We consider reinforcement learning and bandit structured prediction problems with very sparse loss feedback: only at the end of an episode. We introduce a novel algorithm, RESIDUAL LOSS PREDICTION (RESLOPE), that solves such problems by automatically learning an internal representation of a denser reward function. RESLOPE operates as a reduction to contextual bandits, using its learned loss representation to solve the credit assignment problem, and a contextual bandit oracle to trade-off exploration and exploitation. RESLOPE enjoys a no-regret reduction-style theoretical guarantee and outperforms state of the art reinforcement learning algorithms in both MDP environments and bandit structured prediction settings.

## item_id: m_2183

TITLE: Learning Non-Metric Visual Similarity for Image Retrieval

ABSTRACT: Measuring visual (dis)similarity between two or more instances within a data distribution is a fundamental task in many applications, specially in image retrieval. Theoretically, non-metric distances are able to generate a more complex and accurate similarity model than metric distances, provided that the non-linear data distribution is precisely captured by the similarity model. In this work, we analyze a simple approach for deep learning networks to be used as an approximation of non-metric similarity functions and we study how these models generalize across different image retrieval datasets.

## item_id: m_2184

TITLE: Deep Complex Networks

ABSTRACT: At present, the vast majority of building blocks, techniques, and architectures for deep learning are based on real-valued operations and representations. However, recent work on recurrent neural networks and older fundamental theoretical analysis suggests that complex numbers could have a richer representational capacity and could also facilitate noise-robust memory retrieval mechanisms. Despite their attractive properties and potential for opening up entirely new neural architectures, complex-valued deep neural networks have been marginalized due to the absence of the building blocks required to design such models. In this work, we provide the key atomic components for complex-valued deep neural networks and apply them to convolutional feed-forward networks. More precisely, we rely on complex convolutions and present algorithms for complex batch-normalization, complex weight initialization strategies for complex-valued neural nets and we use them in experiments with end-to-end training schemes. We demonstrate that such complex-valued models are competitive with their real-valued counterparts. We test deep complex models on several computer vision tasks, on music transcription using the MusicNet dataset and on Speech spectrum prediction using TIMIT. We achieve state-of-the-art performance on these audio-related tasks.

## item_id: m_2185

TITLE: Cooperative Minibatching in Graph Neural Networks

ABSTRACT: Significant computational resources are required to train Graph Neural Networks (GNNs) at a large scale,
and the process is highly data-intensive.
One of the most effective ways to reduce resource requirements is minibatch training 
coupled with graph sampling.
GNNs have the unique property that items in a minibatch have overlapping data. 
However, the commonly implemented Independent Minibatching approach assigns each Processing 
Element (PE) its own minibatch to process, leading to duplicated computations and input data access across PEs. 
This amplifies the Neighborhood Explosion Phenomenon (NEP), which is the main bottleneck limiting scaling. 
To reduce the effects of NEP in the multi-PE setting,
we propose a new approach called Cooperative Minibatching. 
Our approach capitalizes on the fact that the size of the sampled subgraph is a concave function of the batch size, leading to 
significant reductions in the amount of work per seed vertex as batch sizes increase. Hence, it is favorable for 
processors to work on a large minibatch together as a single larger processor, instead of working on separate smaller 
minibatches, even though global batch size is identical.
We also show how to take advantage of the same phenomenon in serial execution by generating dependent consecutive minibatches. 
Our experimental evaluations show up to 4x bandwidth savings for fetching vertex embeddings, by simply increasing 
this dependency without harming model convergence. Combining our proposed approaches, we achieve up to 64\% 
speedup over Independent Minibatching on single-node multi-GPU systems and show 
that load balancing is not an issue despite the use of lock-step communication.

## item_id: m_2186

TITLE: On Sequence Segmentation with overlapped Chunks in Machine Learning

ABSTRACT: Operating on very long sequences can be problematic for many sequence modelling methods like Transformers or recurrent neural networks. To avoid this issue, long sequences are often split into smaller chunks instead.
For various reasons, these chunks typically are overlapped with each other which causes an increase in tensor size by however much the chunks are overlapping.

This paper attempts to find a better understanding on overlapped sequence chunks and what they accomplish. Specifically, the focus of this paper is on audio inputs in both the time and frequency domain. Previous models for speech separation and audio super resolution which use overlapped chunks are modified to allow for reduced or even removed overlaps which causes significant decreases in computational cost while maintaining accuracy.

## item_id: m_2187

TITLE: Skip Connections Matter: On the Transferability of Adversarial Examples Generated with ResNets

ABSTRACT: Skip connections are an essential component of current state-of-the-art deep neural networks (DNNs) such as ResNet, WideResNet, DenseNet, and ResNeXt. Despite their huge success in building deeper and more powerful DNNs, we identify a surprising \emph{security weakness} of skip connections in this paper. Use of skip connections \textit{allows easier generation of highly transferable adversarial examples}. Specifically, in ResNet-like (with skip connections) neural networks, gradients can backpropagate through either skip connections or residual modules. We find that using more gradients from the skip connections rather than the residual modules according to a decay factor, allows one to craft adversarial examples with high transferability. Our method is termed \emph{Skip Gradient Method} (SGM). We conduct comprehensive transfer attacks against state-of-the-art DNNs including ResNets, DenseNets, Inceptions, Inception-ResNet, Squeeze-and-Excitation Network (SENet) and robustly trained DNNs. We show that employing SGM on the gradient flow can greatly improve the transferability of crafted attacks in almost all cases. Furthermore, SGM can be easily combined with existing black-box attack techniques, and obtain high improvements over state-of-the-art transferability methods. Our findings not only motivate new research into the architectural vulnerability of DNNs, but also open up further challenges for the design of secure DNN architectures.

## item_id: m_2188

TITLE: MAJOR-MINOR LSTMS FOR WORD-LEVEL LANGUAGE MODEL

ABSTRACT: As a widely-accepted evaluation criterion, complexity has attracted more and more attention in the design of language models. The parameter count is a proxy for complexity, which is often reported and compared in research papers. In general, more parameters means better model performance, but higher complexity. Therefore, reconciling the contradiction between the complexity and the model performance is necessary. In this paper, we propose a simple method to make use of model parameters more effectively, so that the LSTM-based language models can reach better results without the cost of increasing parameters. The method constructs another small-scale LSTM with a part of parameters originally belonging to the vanilla LSTM in each layer, whose output can assist the next layer in processing the output of the vanilla LSTM. We name these two LSTMs Major Minor LSTMs. In experiments, we demonstrate the language model with Major Minor LSTMs surpasses the existing state-of-the-art model on Penn Treebank and WikiText-2 with fewer parameters.

## item_id: m_2189

TITLE: CyCADA: Cycle-Consistent Adversarial Domain Adaptation

ABSTRACT: Domain adaptation is critical for success in new, unseen environments.
Adversarial adaptation models applied in feature spaces discover domain invariant representations, but are difficult to visualize and sometimes fail to capture pixel-level and low-level domain shifts.
Recent work has shown that generative adversarial networks combined with cycle-consistency constraints are surprisingly effective at  mapping images between domains, even without the use of aligned image pairs.
We propose a novel discriminatively-trained Cycle-Consistent Adversarial Domain Adaptation model.
CyCADA adapts representations at both the pixel-level and feature-level, enforces cycle-consistency while leveraging a task loss, and does not require aligned pairs.  Our model can be applied in a variety of visual recognition and prediction settings.
We show new state-of-the-art results across multiple adaptation tasks, including digit classification and semantic segmentation of road scenes demonstrating transfer from synthetic to real world domains.

## item_id: m_2190

TITLE: Compressing multidimensional weather and climate data into neural networks

ABSTRACT: Weather and climate simulations produce petabytes of high-resolution data that are later analyzed by researchers in order to understand climate change or severe weather. We propose a new method of compressing this multidimensional weather and climate data: a coordinate-based neural network is trained to overfit the data, and the resulting parameters are taken as a compact representation of the original grid-based data. While compression ratios range from 300x to more than 3,000x, our method outperforms the state-of-the-art compressor SZ3 in terms of weighted RMSE, MAE. It can faithfully preserve important large scale atmosphere structures and does not introduce significant artifacts.
When using the resulting neural network as a 790x compressed dataloader to train the WeatherBench forecasting model, its RMSE increases by less than 2%. The three orders of magnitude compression democratizes access to high-resolution climate data and enables numerous new research directions.

## item_id: m_2191

TITLE: Text-to-3D Generation with Bidirectional Diffusion using both 3D and 2D priors

ABSTRACT: Most research in 3D object generation focuses on boosting 2D foundational models into the 3D space, either by minimizing 2D SDS loss or fine-tuning on multi-view datasets. Without explicit 3D priors, these methods often lead to geometric anomalies and multi-view inconsistency. Recently, researchers have attempted to improve the genuineness of 3D objects by training directly on 3D datasets, albeit at the cost of low-quality texture generation due to the limited 2D texture variation in 3D datasets. To harness the advantages of both approaches, in this paper, we propose Bidirectional Diffusion (BiDiff), a unified framework that incorporates both a 3D and a 2D diffusion process, to preserve both 3D fidelity and 2D texture richness, respetively. Recognizing that a simple combination of two diffusion processes can yield inconsistent generation results, we further bridge them with innovative bidirectional guidance. At last, we also demonstrate that this is the first 3D generative model that can separately control texture and geometry generation. Experimental results have shown that our model achieves high-quality, diverse, and scalable 3D generation. The project website is https://bidiff.github.io

## item_id: m_2192

TITLE: “Style” Transfer for Musical Audio Using Multiple Time-Frequency Representations

ABSTRACT: Neural Style Transfer has become a popular technique for
generating images of distinct artistic styles using convolutional neural networks. This
recent success in image style transfer has raised the question of
whether similar methods can be leveraged to alter the “style” of musical
audio. In this work, we attempt long time-scale high-quality audio transfer
and texture synthesis in the time-domain that captures harmonic,
rhythmic, and timbral elements related to musical style, using examples that
may have different lengths and musical keys. We demonstrate the ability
to use randomly initialized convolutional neural networks to transfer
these aspects of musical style from one piece onto another using 3
different representations of audio: the log-magnitude of the Short Time
Fourier Transform (STFT), the Mel spectrogram, and the Constant-Q Transform
spectrogram. We propose using these representations as a way of
generating and modifying perceptually significant characteristics of
musical audio content. We demonstrate each representation's
shortcomings and advantages over others by carefully designing
neural network structures that complement the nature of musical audio. Finally, we show that the most
compelling “style” transfer examples make use of an ensemble of these
representations to help capture the varying desired characteristics of
audio signals.

## item_id: m_2193

TITLE: On Generalization Error Bounds of Noisy Gradient Methods for Non-Convex Learning

ABSTRACT: Generalization error (also known as the out-of-sample error) measures how well the hypothesis learned from training data generalizes to previously unseen data. Proving tight generalization error bounds is a central question in statistical learning  theory.   In  this  paper,  we  obtain  generalization  error  bounds  for  learning general  non-convex  objectives,  which  has  attracted  significant  attention  in  recent years.   We develop a new framework,  termed Bayes-Stability,  for proving algorithm-dependent generalization error bounds.  The new framework combines ideas from both the PAC-Bayesian theory and the notion of algorithmic stability.  Applying the Bayes-Stability method, we obtain new data-dependent generalization bounds for stochastic gradient Langevin dynamics (SGLD) and several other noisy gradient methods (e.g., with momentum, mini-batch and acceleration, Entropy-SGD). Our result recovers (and is typically tighter than) a recent result in Mou et al. (2018) and improves upon the results in Pensia et al. (2018).  Our experiments demonstrate that our data-dependent bounds can distinguish randomly labelled data from normal data, which provides an explanation to the intriguing phenomena observed in Zhang et al. (2017a). We also study the setting where the total loss is the sum of a bounded loss and an additiona l`2 regularization term. We obtain new generalization bounds for the continuous Langevin dynamic in this setting by developing a new Log-Sobolev inequality for the parameter distribution at any time. Our new bounds are more desirable when the noise level of the processis not very small, and do not become vacuous even when T tends to infinity.

## item_id: m_2194

TITLE: Probable Dataset Searching Method with Uncertain Dataset Information in Adjusting Architecture Hyper Parameter

ABSTRACT: Different types of tasks with uncertain dataset information are studied because different parts of data may have different difficulties to achieve. For example, in unsupervised learning and domain adaptation, datasets are provided without label information because of the cost of human annotation.  In deep learning, adjusting architecture hyper parameters is important for the model performance and is also time consuming, so we try to adjust hyper parameters in two types of uncertain dataset information:1, dataset labels are postponed to be obtained so hyper parameters need to be adjusted without complete dataset information. 2, hyper parameters are adjusted with a subset training dataset since training models with complete training dataset is time consuming. Here, we propose several loss functions to search for probable dataset when the complete dataset information is not obtained. The experiments on 9 real world data demonstrate the performance of our method.

## item_id: m_2195

TITLE: IFR-Explore: Learning Inter-object Functional Relationships in 3D Indoor Scenes

ABSTRACT: Building embodied intelligent agents that can interact with 3D indoor environments has received increasing research attention in recent years. While most works focus on single-object or agent-object visual functionality and affordances, our work proposes to study a novel, underexplored, kind of visual relations that is also important to perceive and model -- inter-object functional relationships (e.g., a switch on the wall turns on or off the light, a remote control operates the TV). Humans often spend no effort or only a little to infer these relationships, even when entering a new room, by using our strong prior knowledge (e.g., we know that buttons control electrical devices) or using only a few exploratory interactions in cases of uncertainty (e.g., multiple switches and lights in the same room). In this paper, we take the first step in building AI system learning inter-object functional relationships in 3D indoor environments with key technical contributions of modeling prior knowledge by training over large-scale scenes and designing interactive policies for effectively exploring the training scenes and quickly adapting to novel test scenes. We create a new dataset based on the AI2Thor and PartNet datasets and perform extensive experiments that prove the effectiveness of our proposed method.

## item_id: m_2196

TITLE: Latent forward model for Real-time Strategy game planning with incomplete information

ABSTRACT: Model-free deep reinforcement learning approaches have shown superhuman performance in simulated environments (e.g., Atari games, Go, etc). During training, these approaches often implicitly construct a latent space that contains key information for decision making. In this paper, we learn a forward model on this latent space and apply it to model-based planning in miniature Real-time Strategy game with incomplete information (MiniRTS). We first show that the latent space constructed from existing actor-critic models contains relevant information of the game, and design training procedure to learn forward models. We also show that our learned forward model can predict meaningful future state and is usable for latent space Monte-Carlo Tree Search (MCTS), in terms of win rates against rule-based agents.

## item_id: m_2197

TITLE: Wider Networks Learn Better Features

ABSTRACT: Transferability of learned features between tasks can massively reduce the cost of training a neural network on a novel task. We investigate the effect of network width on learned features using activation atlases --- a visualization technique that captures features the entire hidden state responds to, as opposed to individual neurons alone. We find that, while individual neurons do not learn interpretable features in wide networks, groups of neurons do. In addition, the hidden state of a wide network contains more information about the inputs than that of a narrow network trained to the same test accuracy. Inspired by this observation, we show that when fine-tuning the last layer of a network on a new task, performance improves significantly as the width of the network is increased, even though test accuracy on the original task is independent of width. 

## item_id: m_2198

TITLE: Deep Lipschitz networks and Dudley GANs

ABSTRACT: Generative adversarial networks (GANs) have enjoyed great success, however often suffer instability during training which motivates many attempts to resolve this issue. Theoretical explanation for the cause of instability is provided in Wasserstein GAN (WGAN), and wasserstein distance is proposed to stablize the training. Though WGAN is indeed more stable than previous GANs, it takes much more iterations and time to train. This is because the ways to ensure Lipschitz condition in WGAN (such as weight-clipping) significantly limit the capacity of the network. In this paper, we argue that it is beneficial to ensure Lipschitz condition as well as maintain sufficient capacity and expressiveness of the network. To facilitate this, we develop both theoretical and practical building blocks, using which one can construct different neural networks using a large range of metrics, as well as ensure Lipschitz condition and sufficient capacity of the networks. Using the proposed building blocks, and a special choice of a metric called Dudley metric, we propose Dudley GAN that outperforms the state of the arts in both convergence and sample quality. We discover a natural link between Dudley GAN (and its extension) and empirical risk minimization, which gives rise to generalization analysis.

## item_id: m_2199

TITLE: Diffusion Implicit Policy for Unpaired Scene-aware Motion Synthesis

ABSTRACT: Human motion generation is a long-standing problem, and scene-aware motion synthesis has been widely researched recently due to its numerous applications. Prevailing methods rely heavily on paired motion-scene data whose quantity is limited. Meanwhile, it is difficult to generalize to diverse scenes when trained only on a few specific ones. Thus, we propose a unified framework, termed Diffusion Implicit Policy (DIP), for scene-aware motion synthesis, where paired motion-scene data are no longer necessary. In this framework, we disentangle human-scene interaction from motion synthesis during training and then introduce an interaction-based implicit policy into motion diffusion during inference. Synthesized motion can be derived through iterative diffusion denoising and implicit policy optimization, thus motion naturalness and interaction plausibility can be maintained simultaneously. The proposed implicit policy optimizes the intermediate noised motion in a GAN Inversion manner to maintain motion continuity and control keyframe poses though the ControlNet branch and motion inpainting. For long-term motion synthesis, we introduce motion blending for stable transitions between multiple sub-tasks, where motions are fused in rotation power space and translation linear space. The proposed method is evaluated on synthesized scenes with ShapeNet furniture, and real scenes from PROX and Replica. Results show that our framework presents better motion naturalness and interaction plausibility than cutting-edge methods. This also indicates the feasibility of utilizing the DIP for motion synthesis in more general tasks and versatile scenes.

## item_id: m_2200

TITLE: Lossy Compression with Gaussian Diffusion

ABSTRACT: We consider a novel lossy compression approach based on unconditional diffusion generative models, which we call DiffC. Unlike modern compression schemes which rely on transform coding and quantization to restrict the transmitted information, DiffC relies on the efficient communication of pixels corrupted by Gaussian noise. We implement a proof of concept and find that it works surprisingly well despite the lack of an encoder transform, outperforming the state-of-the-art generative compression method HiFiC on ImageNet 64x64. DiffC only uses a single model to encode and denoise corrupted pixels at arbitrary bitrates. The approach further provides support for progressive coding, that is, decoding from partial bit streams. We perform a rate-distortion analysis to gain a deeper understanding of its performance, providing analytical results for multivariate Gaussian data as well as theoretic bounds for general distributions. Furthermore, we prove that a flow-based reconstruction achieves a 3 dB gain over ancestral sampling at high bitrates.
