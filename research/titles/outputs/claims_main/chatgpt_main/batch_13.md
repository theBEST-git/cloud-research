# Batch 13 — 100 items

## item_id: m_1201

TITLE: HybridNet: A Hybrid Neural Architecture to Speed-up Autoregressive  Models

ABSTRACT: This paper introduces HybridNet, a hybrid neural network to speed-up autoregressive
models for raw audio waveform generation. As an example, we propose
a hybrid model that combines an autoregressive network named WaveNet and a
conventional LSTM model to address speech synthesis. Instead of generating
one sample per time-step, the proposed HybridNet generates multiple samples per
time-step by exploiting the long-term memory utilization property of LSTMs. In
the evaluation, when applied to text-to-speech, HybridNet yields state-of-art performance.
HybridNet achieves a 3.83 subjective 5-scale mean opinion score on
US English, largely outperforming the same size WaveNet in terms of naturalness
and provide 2x speed up at inference.

## item_id: m_1202

TITLE: Joint Multimodal Learning with Deep Generative Models

ABSTRACT: We investigate deep generative models that can exchange multiple modalities bi-directionally, e.g., generating images from corresponding texts and vice versa. Recently, some studies handle multiple modalities on deep generative models, such as variational autoencoders (VAEs). However, these models typically assume that modalities are forced to have a conditioned relation, i.e., we can only generate modalities in one direction. To achieve our objective, we should extract a joint representation that captures high-level concepts among all modalities and through which we can exchange them bi-directionally. As described herein, we propose a joint multimodal variational autoencoder (JMVAE), in which all modalities are independently conditioned on joint representation. In other words, it models a joint distribution of modalities. Furthermore, to be able to generate missing modalities from the remaining modalities properly, we develop an additional method, JMVAE-kl, that is trained by reducing the divergence between JMVAE's encoder and prepared networks of respective modalities. Our experiments show that our proposed method can obtain appropriate joint representation from multiple modalities and that it can generate and reconstruct them more properly than conventional VAEs. We further demonstrate that JMVAE can generate multiple modalities bi-directionally.


## item_id: m_1203

TITLE: HBO: Hierarchical Balancing Optimization for Fine-Tuning Large Language Models

ABSTRACT: Fine-tuning large language models (LLMs) on a mixture of diverse datasets poses challenges due to data imbalance and heterogeneity. Existing methods often address these issues across datasets (globally) but overlook the imbalance and heterogeneity within individual datasets (locally), which limits their effectiveness. We introduce Hierarchical Balancing Optimization (HBO), a novel method that enables LLMs to autonomously adjust data allocation during fine-tuning both across datasets (globally) and within each individual dataset (locally). HBO employs a bilevel optimization strategy with two types of actors: a Global Actor, which balances data sampling across different subsets of the training mixture, and several Local Actors, which optimizes data usage within each subset based on difficulty levels. These actors are guided by reward functions derived from the LLM's training state, which measure learning progress and relative performance improvement. We evaluate HBO on three LLM backbones across nine diverse tasks in multilingual and multitask setups. Results show that HBO consistently outperforms existing baselines, achieving significant accuracy gains. Our in-depth analysis further demonstrates that both the global actor and local actors of HBO effectively adjust data usage during fine-tuning. HBO provides a comprehensive solution to the challenges of data imbalance and heterogeneity in LLM fine-tuning, enabling more effective training across diverse datasets.

## item_id: m_1204

TITLE: Regularization Shortcomings for Continual Learning

ABSTRACT: In most machine learning algorithms, training data is assumed to be independent and identically distributed (iid).  
When it is not the case, the performances of the algorithms are challenged, leading to the famous phenomenon of \textit{catastrophic forgetting}. Algorithms dealing with it are gathered in the \textit{Continual Learning} research field. In this paper, we study the \textit{regularization} based approaches to continual learning and show that those approaches can not learn to discriminate classes from different tasks in an elemental continual benchmark, the class-incremental setting.
We make theoretical reasoning to prove this shortcoming and illustrate it with experiments.
Moreover, we show that it can have some important consequences on multi-tasks reinforcement learning or in pre-trained models used for continual learning.
We believe this paper to be the first to propose a theoretical description of regularization shortcomings for continual learning. 

## item_id: m_1205

TITLE: DyRep: Learning Representations over Dynamic Graphs

ABSTRACT: Representation Learning over graph structured data has received significant attention recently due to its ubiquitous applicability. However, most advancements have been made in static graph settings while efforts for jointly learning dynamic of the graph and dynamic on the graph are still in an infant stage. Two fundamental questions arise in learning over dynamic graphs: (i) How to elegantly model dynamical processes over graphs? (ii) How to leverage such a model to effectively encode evolving graph information into low-dimensional representations? We present DyRep - a novel modeling framework for dynamic graphs that posits representation learning as a latent mediation process bridging two observed processes namely -- dynamics of the network (realized as topological evolution) and dynamics on the network (realized as activities between nodes). Concretely, we propose a two-time scale deep temporal point process model that captures the interleaved dynamics of the observed processes. This model is further parameterized by a temporal-attentive representation network that encodes temporally evolving structural information into node representations which in turn drives the nonlinear evolution of the observed graph dynamics. Our unified framework is trained using an efficient unsupervised procedure and has capability to generalize over unseen nodes. We demonstrate that DyRep outperforms state-of-the-art baselines for dynamic link prediction and time prediction tasks and present extensive qualitative insights into our framework.

## item_id: m_1206

TITLE: Constrained Exploitability Descent: Finding Mixed-Strategy Nash Equilibrium by Offline Reinforcement Learning

ABSTRACT: This paper presents Constrained Exploitability Descent (CED), a novel model-free offline reinforcement learning algorithm for solving adversarial Markov games. CED is a game-theoretic approach combined with policy constraint methods from offline RL. While policy constraints can perturb the optimal pure-strategy solutions in single-agent scenarios, we find this side effect can be mitigated when it comes to solving adversarial games, where the optimal policy can be a mixed-strategy Nash equilibrium. We theoretically prove that, under the uniform coverage assumption on the dataset, CED converges to a stationary point in deterministic two-player zero-sum Markov games. The min-player policy at the stationary point satisfies the necessary condition for making up an exact mixed-strategy Nash equilibrium, even when the offline dataset is fixed and finite. Compared to the model-based method of Exploitability Descent that optimizes the max-player policy, our convergence result no longer relies on the generalized gradient. Experiments in matrix games, a tree-form game, and an infinite-horizon soccer game verify that a single run of CED leads to an optimal min-player policy when the practical offline data guarantees uniform coverage. Besides, CED achieves significantly lower NashConv compared to an existing pessimism-based method and can gradually improve the behavior policy even under non-uniform coverage.

## item_id: m_1207

TITLE: CorrAttack: Black-box Adversarial Attack with Structured Search

ABSTRACT: We present a new method for score-based adversarial attack, where the attacker queries the loss-oracle of the target model.
Our method employs a parameterized search space with a structure that captures the relationship of the gradient of the loss function. We show that searching over the structured space can be approximated by a time-varying contextual bandits problem, where the attacker takes feature of the associated arm to make modifications of the input, and receives an immediate reward as the reduction of the loss function. The time-varying contextual bandits problem can then be solved by a Bayesian optimization procedure, which can take advantage of the features of the structured action space. The experiments on ImageNet and the Google Cloud Vision API demonstrate that the proposed method achieves the state of the art success rates and query efficiencies for both undefended and defended models.

## item_id: m_1208

TITLE: Perfect density models cannot guarantee anomaly detection

ABSTRACT: Thanks to the tractability of their likelihood, some deep generative models show promise for seemingly straightforward but important applications like anomaly detection, uncertainty estimation, and active learning. However, the likelihood values empirically attributed to anomalies conflict with the expectations these proposed applications suggest. In this paper, we take a closer look at the behavior of distribution densities and show that these quantities carry less meaningful information than previously thought, beyond estimation issues or the curse of dimensionality. We conclude that the use of these likelihoods for out-of-distribution detection relies on strong and implicit hypotheses and highlight the necessity of explicitly formulating these assumptions for reliable anomaly detection.

## item_id: m_1209

TITLE: Interpretable Multi-hop Reasoning for Forecasting Future Links on Temporal Knowledge Graphs

ABSTRACT: Temporal knowledge graphs (KGs) have recently attracted growing attention. The temporal KG forecasting task, which plays a crucial role in applications such as event prediction, is predicting future links based on historical facts. The interpretability of the current temporal KG forecasting models is manifested in providing the reasoning paths. However, the comparison of reasoning paths is operated under the black box. Inspired by the observation that reasoning based on multi-hop paths is equivalent to answering questions step by step, this paper designs an Interpretable Multi-hop Reasoning (IMR) model for temporal KG forecasting. IMR transforms reasoning based on path searching into step-by-step question answering. Moreover, IMR designs three indicators according to the characteristics of temporal KGs and reasoning paths: question matching degree, answer completing level and path confidence. Unlike other models that can only utilize paths with a specified hop, IMR can effectively integrate paths of different hops; IMR can provide the reasoning paths like other interpretable models and further explain the basis for path comparison. While being more explainable, IMR has achieved state-of-the-art on four baseline datasets.

## item_id: m_1210

TITLE: Rethinking generalization requires revisiting old ideas: statistical mechanics approaches and complex learning behavior

ABSTRACT: We describe an approach to understand the peculiar and counterintuitive generalization properties of deep neural networks.  The approach involves going beyond worst-case theoretical capacity control frameworks that have been popular in machine learning in recent years to revisit old ideas in the statistical mechanics of neural networks.  Within this approach, we present a prototypical Very Simple Deep Learning (VSDL) model, whose behavior is controlled by two control parameters, one describing an effective amount of data, or load, on the network (that decreases when noise is added to the input), and one with an effective temperature interpretation (that increases when algorithms are early stopped).  Using this model, we describe how a very simple application of ideas from the statistical mechanics theory of generalization provides a strong qualitative description of recently-observed empirical results regarding the inability of deep neural networks not to overfit training data, discontinuous learning and sharp transitions in the generalization properties of learning algorithms, etc.

## item_id: m_1211

TITLE: Multimodal Open-Vocabulary Video Classification via Vision and Language Models

ABSTRACT: Utilizing vision and language models (VLMs) pre-trained on internet-scale image-text pairs is becoming a promising paradigm for open-vocabulary vision tasks. This work conducts an extensive study for multimodal open-vocabulary video classification via pre-trained VLMs by leveraging motion and audio that naturally exist in the video. We design an asymmetrical cross-modal fusion mechanism to aggregate multimodal information differently for video and optical flow / audio. Experiments on Kinetics and VGGSound show that introducing more modalities significantly improves the accuracy on seen classes, while generalizing better to unseen classes over existing approaches. Despite its simplicity, our method achieves state-of-the-art results on UCF and HMDB zero-shot video action recognition benchmarks, significantly outperforming traditional zero-shot techniques, video-text pre-training methods and recent VLM-based approaches. Code and models will be released.

## item_id: m_1212

TITLE: ABSTRACTING INFLUENCE PATHS  FOR EXPLAINING (CONTEXTUALIZATION OF) BERT MODELS

ABSTRACT: While “attention is all you need” may be proving true, we do not yet know why: attention-based transformer models such as BERT are superior but how they contextualize information even for simple grammatical rules such as subject-verb number agreement(SVA) is uncertain. We introduce multi-partite patterns, abstractions of sets of paths through a neural network model. Patterns quantify and localize the effect of an input concept (e.g., a subject’s number) on an output concept (e.g. corresponding verb’s number) to paths passing through a sequence of model components, thus surfacing how BERT contextualizes information. We describe guided pattern refinement, an efficient search procedure for finding sufficient and sparse patterns representative of concept-critical paths. We discover that patterns generate succinct and meaningful explanations for BERT, highlighted by “copy” and “transfer” operations implemented by skip connections and attention heads, respectively. We also show how pattern visualizations help us understand how BERT contextualizes various grammatical concepts, such as SVA across clauses, and why it makes errors in some cases while succeeding in others.

## item_id: m_1213

TITLE: Correcting Nuisance Variation using Wasserstein Distance

ABSTRACT: Profiling cellular phenotypes from microscopic imaging can provide meaningful biological information resulting from various factors affecting the cells. One motivating application is drug development: morphological cell features can be captured from images, from which similarities between different drugs applied at different dosages can be quantified. The general approach is to find a function mapping the images to an embedding space of manageable dimensionality whose geometry captures relevant features of the input images. An important known issue for such methods is separating relevant biological signal from nuisance variation. For example, the embedding vectors tend to be more correlated for cells that were cultured and imaged during the same week than for cells from a different week, despite having identical drug compounds applied in both cases. In this case, the particular batch a set of experiments were conducted in constitutes the domain of the data; an ideal set of image embeddings should contain only the relevant biological information (e.g. drug effects). We develop a general framework for adjusting the image embeddings in order to `forget' domain-specific information while preserving relevant biological information. To do this, we minimize a loss function based on distances between marginal distributions (such as the Wasserstein distance) of embeddings across domains for each replicated treatment. For the dataset presented, the replicated treatment is the negative control. We find that for our transformed embeddings (1) the underlying geometric structure is not only preserved but the embeddings also carry improved biological signal (2) less domain-specific information is present.

## item_id: m_1214

TITLE: FastGCN: Fast Learning with Graph Convolutional Networks via Importance Sampling

ABSTRACT: The graph convolutional networks (GCN) recently proposed by Kipf and Welling are an effective graph model for semi-supervised learning. Such a model, however, is transductive in nature because parameters are learned through convolutions with both training and test data. Moreover, the recursive neighborhood expansion across layers poses time and memory challenges for training with large, dense graphs. To relax the requirement of simultaneous availability of test data, we interpret graph convolutions as integral transforms of embedding functions under probability measures. Such an interpretation allows for the use of Monte Carlo approaches to consistently estimate the integrals, which in turn leads to a batched training scheme as we propose in this work---FastGCN. Enhanced with importance sampling, FastGCN not only is efficient for training but also generalizes well for inference. We show a comprehensive set of experiments to demonstrate its effectiveness compared with GCN and related models. In particular, training is orders of magnitude more efficient while predictions remain comparably accurate.


## item_id: m_1215

TITLE: DSI-Bench: A Benchmark for Dynamic Spatial Intelligence

ABSTRACT: Reasoning about dynamic spatial relationships is essential, as both observers and objects often move simultaneously. Although vision-language models (VLMs) and visual expertise models excel in 2D tasks and static scenarios, their ability to fully understand dynamic 3D scenarios remains limited. We introduce \textbf{D}ynamic  \textbf{S}patial  \textbf{I}ntelligence and propose DSI-Bench, a benchmark with nearly 1,000 dynamic videos and over 1,700 manually annotated questions covering nine decoupled motion patterns of observers and objects. Spatially and temporally symmetric designs reduce biases and enable systematic evaluation of models’ reasoning about self-motion and object motion. Our evaluation of 14 VLMs and expert models reveals key limitations: models often conflate observer and object motion, exhibit semantic biases, and fail to accurately infer relative relationships in dynamic scenarios. Our DSI-Bench provides valuable findings and insights about the future development of general and expertise models with dynamic spatial intelligence.

## item_id: m_1216

TITLE: Rule Mining in Feature Space

ABSTRACT: Relational embeddings have emerged as an excellent tool for inferring novel facts
from partially observed knowledge bases. Recently, it was shown that some
classes of embeddings can also be exploited to perform a simplified form of rule
mining. By interpreting logical conjunction as a form of composition between re-
lation embeddings, simplified logical theories can be mined directly in the space
of latent representations. In this paper, we present a method to mine full-fledged
logical theories, which are significantly more expressive, by casting the semantics
of the logical operators to the space of the embeddings. In order to extract relevant
rules in the space of relation compositions we borrow sparse reconstruction pro-
cedures from the field of compressed sensing. Our empirical analysis showcases
the advantages of our approach.

## item_id: m_1217

TITLE: Image as Set of Points

ABSTRACT: 
What is an image, and how to extract latent features? 
Convolutional Networks (ConvNets) consider an image as organized pixels in a rectangular shape and extract features via convolutional operation in a local region; Vision Transformers (ViTs) treat an image as a sequence of patches and extract features via attention mechanism in a global range. In this work, we introduce a straightforward and promising paradigm for visual representation, which is called Context Clusters. Context clusters (CoCs) view an image as a set of unorganized points and extract features via a simplified clustering algorithm. In detail, each point includes the raw feature (e.g., color) and positional information (e.g., coordinates), and a simplified clustering algorithm is employed to group and extract deep features hierarchically. Our CoCs are convolution- and attention-free, only relying on clustering algorithm for spatial interaction. Owing to the simple design, we show CoCs endow gratifying interpretability via the visualization of the clustering process.  
Our CoCs aim at providing a new perspective on image and visual representation, which may enjoy broad applications in different domains and exhibit profound insights. Even though we are not targeting SOTA performance, COCs still achieve comparable or even better performance than ConvNets or ViTs on several benchmarks.

## item_id: m_1218

TITLE: Diffusion Meta-Prompts for Foundation Models

ABSTRACT: Parameter-efficient fine-tuning techniques, such as prompting, are now popular to adapt foundation models to many tasks. In this paper, we introduce a diffusion-based approach to model the distribution of learned foundation models prompts. Specifically, we propose a $\textbf{Diffusion Meta-Prompt (DMP)}$ model that generates prompts conditioned on text or prompt embeddings, and can be used to prompt both vision-language models and diffusion models for image synthesis. DMPs have several advantages: improved generalization of learned prompts; memory and runtime efficiency by eliminating the need to store and search over large repositories of prompts or LoRA weights; multiple applications ranging from  open-set classification, to personalization or attribute control of image synthesis; support for operations like subject and concept composition, novel subject generation, negative prompting, and editing without explicit training. For open-set classification, DMP improves base-to-new class generalization, achieving upto $\textbf{3}$% average gain across 11 datasets with gains as high as $\textbf{7.8/5.4}$% on specific datasets such as Eurosat/UCF101 respectively.  DMP also enhances domain, cross-dataset and cross-task generalization with $\sim$$\textbf{6-12}$% improvement for hierarchical classification task. For image synthesis tasks, DMP improves generalization and prompt compliance by $\textbf{1.4}$ points as measured by CLIP score and reduces storage requirements by $\textbf{91}$% while improving runtime efficiency by $\textbf{92}$% over retrieval methods.

## item_id: m_1219

TITLE: CLAREL: classification via retrieval loss for zero-shot learning

ABSTRACT: We address the problem of learning fine-grained cross-modal representations. We propose an instance-based deep metric learning approach in joint visual and textual space. The key novelty of this paper is that it shows that using per-image semantic supervision leads to substantial improvement in zero-shot performance over using class-only supervision. On top of that, we provide a probabilistic justification for a metric rescaling approach that solves a very common problem in the generalized zero-shot learning setting, i.e., classifying test images from unseen classes as one of the classes seen during training. We evaluate our approach on two fine-grained zero-shot learning datasets: CUB and FLOWERS. We find that on the generalized zero-shot classification task CLAREL consistently outperforms the existing approaches on both datasets.

## item_id: m_1220

TITLE: Limitations of measure-first protocols in quantum machine learning

ABSTRACT: In recent times, there have been major developments in two distinct yet connected domains of quantum information. On the one hand, substantial progress has been made in so-called randomized measurement protocols. Here, a number of properties of unknown quantum states can be deduced from surprisingly few measurement outcomes, using schemes such as classical shadows. On the other hand, significant progress has been made in quantum machine learning. For example, exponential advantages have been proven when the data consists of quantum states and quantum algorithms can coherently measure multiple copies of input states. In this work, we aim to understand the implications and limitations of combining randomized measurement protocols with quantum machine learning, although the implications are broader. Specifically, we investigate quantum machine learning algorithms that, when dealing with quantum data, can either process it entirely using quantum methods or measure the input data through a fixed measurement scheme and utilize the resulting classical information. We prove limitations for quantum machine learning algorithms that use fixed measurement schemes on the input quantum states.
Our results have several implications. From the perspective of randomized measurement procedures, we show limitations of measure-first protocols in the average case, improving on the state-of-the-art which only focuses on worst-case scenarios. Additionally, previous lower bounds were only known for physically unrealizable states. We improve upon this by employing quantum pseudorandom functions to prove that a learning separation also exists when dealing with physically realizable states, which may be encountered in experiments. From a machine learning perspective, our results are crucial for defining a physically meaningful task that shows fully quantum machine learning processing is not only more efficient but also necessary for solving certain problems. The tasks at hand are also realistic, as the algorithms and proven separations hold when working with efficiently preparable states and remain robust in the presence of measurement and preparation errors.

## item_id: m_1221

TITLE: Context-Aware Kernel Search for Bayesian Optimization with Large Language Models

ABSTRACT: The efficiency of Bayesian optimization (BO) relies on careful selection of the surrogate model to balance exploration and exploitation under limited budget. Traditional BO methods often struggle with sub-optimal kernel choices when using Gaussian processes (GPs) as the surrogate model. When the kernel is inadequately chosen, BO may converge slowly or even get stuck at an undesired local minimum. To address such drawback, we propose the novel Context-Aware Kernel Search (CAKES) to automate optimal kernel design in BO with large language models (LLMs). Concretely, CAKES exploits LLMs as crossover and mutation operators to adaptively generate and refine GP kernels based on the observed data. CAKES works entirely in-context and can be easily integrated into existing systems without requiring any fine-tuning. We further present a theoretical analysis demonstrating that our method achieves sub-linear regret relative to the budget for any input dimension. Experimental results demonstrate that CAKES outperforms various salient baseline methods in numerous synthetic and real-world optimization tasks. Notably, CAKES improves the overall performance on benchmark functions by roughly 36\%. In hyperparameter tuning tasks, CAKES can effectively leverage fewer data samples to quickly identify high-performing configurations and consistently ranks first across various datasets. As an encouraging real application, we successfully applied CAKES to design photonic chips,  achieving significant improvements in key performance indicators while speeding up the design cycle by a factor of ten compared to the baselines. Our code is accessible at https://github.com/cakes4bo/cakes.

## item_id: m_1222

TITLE: Learning State Representations in Complex Systems with Multimodal Data

ABSTRACT: Representation learning becomes especially important for complex systems with multimodal data sources such as cameras or sensors. Recent advances in reinforcement learning and optimal control make it possible to design control algorithms on these latent representations, but the field still lacks a large-scale standard dataset for unified comparison. In this work, we present a large-scale dataset and evaluation framework for representation learning for the complex task of landing an airplane. We implement and compare several approaches to representation learning on this dataset in terms of the quality of simple supervised learning tasks and disentanglement scores. The resulting representations can be used for further tasks such as anomaly detection, optimal control, model-based reinforcement learning, and other applications.

## item_id: m_1223

TITLE: Enhancing Group Fairness in Online Settings Using Oblique Decision Forests

ABSTRACT: Fairness, especially group fairness, is an important consideration in the context of machine learning systems. The most commonly adopted group fairness-enhancing techniques are in-processing methods that rely on a mixture of a fairness objective (e.g., demographic parity) and a task-specific objective (e.g., cross-entropy) during the training process. However, when data arrives in an online fashion – one instance at a time – optimizing such fairness objectives poses several challenges. In particular, group fairness objectives are defined using expectations of predictions across different demographic groups. In the online setting, where the algorithm has access to a single instance at a time, estimating the group fairness objective requires additional storage and significantly more computation (e.g., forward/backward passes) than the task-specific objective at every time step. In this paper, we propose Aranyani, an ensemble of oblique decision trees, to make fair decisions in online settings. The hierarchical tree structure of Aranyani enables parameter isolation and allows us to efficiently compute the fairness gradients using aggregate statistics of previous decisions, eliminating the need for additional storage and forward/backward passes. We also present an efficient framework to train Aranyani and theoretically analyze several of its properties. We conduct empirical evaluations on 5 publicly available benchmarks (including vision and language datasets) to show that Aranyani achieves a better accuracy-fairness trade-off compared to baseline approaches.

## item_id: m_1224

TITLE: Thermometer Encoding: One Hot Way To Resist Adversarial Examples

ABSTRACT: It is well known that it is possible to construct "adversarial examples"
for neural networks: inputs which are misclassified by the network
yet indistinguishable from true data. We propose a simple
modification to standard neural network architectures, thermometer
encoding, which significantly increases the robustness of the network to
adversarial examples. We demonstrate this robustness with experiments
on the MNIST, CIFAR-10, CIFAR-100, and SVHN datasets, and show that
models with thermometer-encoded inputs consistently have higher accuracy
on adversarial examples, without decreasing generalization.
State-of-the-art accuracy under the strongest known white-box attack was 
increased from 93.20% to 94.30% on MNIST and 50.00% to 79.16% on CIFAR-10.
We explore the properties of these networks, providing evidence
that thermometer encodings help neural networks to
find more-non-linear decision boundaries.

## item_id: m_1225

TITLE: PQP: A one-shot collaborative method for post-quantization pruning of LLMs

ABSTRACT: Achieving large-scale model compression at a lower cost without significantly compromising performance remains an important challenge in the deployment of LLMs. To address this, we propose Post-Quantization Pruning (PQP), a framework that enables effective synergy between quantization and pruning. Specifically, we introduce a pruning metric tailored for post-quantization scenarios. In addition, we integrate the statistical properties of quantization error into the loss function for block-wise pruning, allowing the model to simultaneously eliminate weights that are unimportant or heavily affected by quantization noise. The PQP method integrates post-training quantization and one-shot pruning, reducing the compressed model's storage requirements to just 1/8 of the original size, with minimal impact on performance. The entire compression process is lightweight, easy to implement, and does not require fine-tuning. Experimental results on LLaMA and LLaMA-2 models demonstrate that PQP consistently outperforms existing methods in compressing models of various scales. Our code is available at \url{https://anonymous.4open.science/r/PQP}.

## item_id: m_1226

TITLE: AuToMATo: An Out-Of-The-Box Persistence-Based Clustering Algorithm

ABSTRACT: We present AuToMATo, a novel clustering algorithm based on persistent homology. While AuToMATo is not parameter-free per se, we provide default choices for its parameters that make it into an out-of-the-box clustering algorithm that performs well across the board. AuToMATo combines the existing ToMATo clustering algorithm with a bootstrapping procedure in order to separate significant peaks of an estimated density function from non-significant ones. We perform a thorough comparison of AuToMATo (with its parameters fixed to their defaults) against many other state-of-the-art clustering algorithms. We find not only that AuToMATo compares favorably against parameter-free clustering algorithms, but in many instances also significantly outperforms even the best selection of parameters for other algorithms. AuToMATo is motivated by applications in topological data analysis, in particular the Mapper algorithm, where it is desirable to work with a clustering algorithm that does not need tuning of its parameters. Indeed, we provide evidence that AuToMATo performs well when used with Mapper. Finally, we provide an open-source implementation of AuToMATo in Python that is fully compatible with the standard scikit-learn architecture.

## item_id: m_1227

TITLE: Phase Conductor on Multi-layered Attentions for Machine Comprehension

ABSTRACT: Attention models have been intensively studied to improve NLP tasks such as machine comprehension via both question-aware passage attention model and self-matching attention model. Our research proposes phase conductor (PhaseCond) for attention models in two meaningful ways. First, PhaseCond, an architecture of multi-layered attention models, consists of multiple phases each implementing a stack of attention layers producing passage representations and a stack of inner or outer fusion layers regulating the information flow.  Second, we extend and improve the dot-product attention function for PhaseCond by simultaneously encoding multiple question and passage embedding layers from different perspectives. We demonstrate the effectiveness of our proposed model PhaseCond on the SQuAD dataset, showing that our model significantly outperforms both state-of-the-art single-layered and multiple-layered attention models. We deepen our results with new findings via both detailed qualitative analysis and visualized examples showing the dynamic changes through multi-layered attention models.

## item_id: m_1228

TITLE: Exploring Transferability of Perturbations in Deep Reinforcement Learning

ABSTRACT: The use of Deep Neural Networks (DNNs) as function approximators has led to striking progress for reinforcement learning algorithms and applications. At the same time, deep reinforcement learning agents have inherited the vulnerability of DNNs to imperceptible adversarial perturbations to their inputs. Prior work on adversarial perturbations for deep reinforcement learning has generally relied on calculating an adversarial perturbation customized to each state visited by the agent. In this paper we propose a more realistic threat model in which the adversary computes the perturbation only once based on a single state. Furthermore, we show that to cause a deep reinforcement learning agent to fail it is enough to have only one adversarial offset vector in a black-box setting. We conduct experiments in various games from the Atari environment, and use our single-state adversaries to demonstrate the transferability of perturbations both between states of one MDP, and between entirely different MDPs. We believe our adversary framework reveals fundamental properties of the environments used in deep reinforcement learning training, and is a tangible step towards building robust and reliable deep reinforcement learning agents.

## item_id: m_1229

TITLE: VADv2: End-to-End Vectorized Autonomous Driving via Probabilistic Planning

ABSTRACT: Learning a human-like driving policy from large-scale driving demonstrations is promising, but the uncertainty and non-deterministic nature of planning make it challenging. Existing learning-based planning methods follow a deterministic paradigm to directly regress the action, failing to cope with the uncertainty problem. In this work, we propose a probabilistic planning model for end-to-end autonomous driving, termed VADv2. We resort to a probabilistic field function to model the mapping from the action space to the probabilistic distribution. Since the planning action space is a high-dimensional continuous spatiotemporal space and hard to tackle, we first discretize the planning action space to a large planning vocabulary and then tokenize the planning vocabulary into planning tokens. Planning tokens interact with scene tokens and output the probabilistic distribution of action. Mass driving demonstrations are leveraged to supervise the distribution. VADv2 achieves state-of-the-art closed-loop performance on the CARLA Town05 benchmark, significantly outperforming existing methods, and also leads the recent Bench2Drive benchmark. We further provide comprehensive evaluations on NAVSIM and a large-scale 3DGS-based benchmark, demonstrating its effectiveness in real-world applications. Code is available at https://github.com/hustvl/VAD.

## item_id: m_1230

TITLE: Combinatorial Pure Exploration of Causal Bandits

ABSTRACT: The combinatorial pure exploration of causal bandits is the following online learning task: given a causal graph with unknown causal inference distributions, in each round we choose a subset of variables to intervene or do no intervention, and observe the random outcomes of all random variables, with the goal that using as few rounds as possible, we can output an intervention that gives the best (or almost best) expected outcome on the reward variable $Y$ with probability at least $1-\delta$, where $\delta$ is a given confidence level. We provide the first gap-dependent and fully adaptive pure exploration algorithms on two types of causal models --- the binary generalized linear model (BGLM) and general graphs. For BGLM, our algorithm is the first to be designed specifically for this setting and achieves polynomial sample complexity, while all existing algorithms for general graphs have either sample complexity exponential to the graph size or some unreasonable assumptions. For general graphs, our algorithm provides a significant improvement on sample complexity, and it nearly matches the lower bound we prove. Our algorithms achieve such improvement by a novel integration of prior causal bandit algorithms and prior adaptive pure exploration algorithms, the former of which utilize the rich observational feedback in causal bandits but are not adaptive to reward gaps, while the latter of which have the issue in reverse.

## item_id: m_1231

TITLE: Convolutional Conditional Neural Processes

ABSTRACT: We introduce the Convolutional Conditional Neural Process (ConvCNP), a new member of the Neural Process family that models translation equivariance in the data. Translation equivariance is an important inductive bias for many learning problems including time series modelling, spatial data, and images. The model embeds data sets into an infinite-dimensional function space, as opposed to finite-dimensional vector spaces. To formalize this notion, we extend the theory of neural representations of sets to include functional representations, and demonstrate that any translation-equivariant embedding can be represented using a convolutional deep-set. We evaluate ConvCNPs in several settings, demonstrating that they achieve state-of-the-art performance compared to existing NPs. We demonstrate that building in translation equivariance enables zero-shot generalization to challenging, out-of-domain tasks.

## item_id: m_1232

TITLE: A Hierarchical Circuit Symbolic Discovery Framework for Efficient Logic Optimization

ABSTRACT: The efficiency of Logic Optimization (LO) has become one of the key bottlenecks in chip design. To prompt efficient LO, many graph-based machine learning (ML) methods, such as graph neural networks (GNNs), have been proposed to predict and prune a large number of ineffective subgraphs of the LO heuristics.  However, the high inference cost and limited interpretability of these approaches severely limit their wide application to modern LO tools.  To address this challenge, we propose a novel **H**ierarchical C**i**rcuit **S**ymbolic Discovery Framework, namely HIS, to learn a *lightweight* and *interpretable* symbolic function that can *accurately* identify ineffective subgraphs for efficient LO.  Specifically, HIS proposes a hierarchical tree structure to represent the circuit symbolic function, where every layer of the symbolic tree performs an efficient and interpretable message passing to capture the structural information of the circuit graph. To learn the hierarchical tree, we propose a circuit symbolic generation framework that leverages reinforcement learning to optimize a structure-aware Transformer model for symbolic token generation.  To the best of our knowledge, HIS is *the first* approach to discover an efficient, interpretable, and high-performance symbolic function from the circuit graph for efficient LO.  Experiments on two widely used circuit benchmarks show that the learned graph symbolic functions outperform previous state-of-the-art approaches in terms of efficiency and optimization performance. Moreover, we integrate HIS with the Mfs2 heuristic, one of the most time-consuming LO heuristics. Results show that HIS significantly enhances both its efficiency and optimization performance on a CPU-based machine, achieving an average runtime improvement of 27.22% and a 6.95% reduction in circuit size.

## item_id: m_1233

TITLE: Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models

ABSTRACT: Fine-tuning language models (LMs) with the standard Adam optimizer often demands excessive memory, limiting accessibility. The ``in-place'' version of Stochastic Gradient Descent (IP-SGD) and Memory-Efficient Zeroth-order Optimizer (MeZO) have been proposed as solutions to improve memory efficiency. However, IP-SGD still requires a decent amount of memory, and MeZO suffers from slow convergence and degraded final performance due to its zeroth-order nature. This paper introduces Addax, a novel method that improves both memory efficiency and algorithm performance of IP-SGD by integrating it with MeZO. Specifically, Addax computes the zeroth-order or first-order gradient of the data points in the minibatch based on their memory consumption and combines zeroth- and first-order gradient estimates to obtain the updated direction in each step.
By computing the zeroth-order order gradient of data points that require more memory and the first-order gradient of the ones that require less memory, Addax overcomes the slow convergence of MeZO and excessive memory requirement of IP-SGD. Additionally, the zeroth-order gradient acts as a regularizer for the first-order gradient, further enhancing the model's final performance.
Theoretically, we establish the convergence of Addax under mild assumptions, demonstrating faster convergence and less restrictive hyper-parameter choices than MeZO. Our extensive experiments with diverse LMs and tasks show that Addax consistently outperforms MeZO in terms of accuracy and convergence speed, while having a comparable memory footprint. 
In particular, our experiments using one A100 GPU on OPT-13B model reveal that, on average, Addax outperforms MeZO in terms of accuracy/F1 score by 14%, and runs $15\times$ faster, while having a comparable memory footprint to MeZO. In our experiments on the larger OPT-30B model, on average, Addax outperforms MeZO in terms of accuracy/F1 score by >16% and runs $30\times$ faster on a single H100 GPU. Moreover, Addax surpasses the performance of standard fine-tuning approaches, such as IP-SGD and Adam, in most tasks in terms of Accuracy/F1 score with significantly less memory requirement.

## item_id: m_1234

TITLE: Understanding Medical Time Series Event Piece by Piece: A Fine-Grained Event Detection Network

ABSTRACT: Event detection in medical time series is fundamental to supporting health monitoring and clinical decision-making. However, most existing methods divide time series into fixed-length segments and perform coarse-grained, segment-level detection, which fails to precisely localize the start and end times of events. This limitation can mislead clinical assessment and obscure the true severity of conditions. To address this, we propose EventCompreNet——a universal network for fine-grained event detection leveraging auxiliary tasks. Inspired by the cognitive processes that human detect events, we introduce four human comprehension tasks to enhance the model’s understanding of each piece of events. Moreover, to overcome the limited knowledge transfer in existing multi-task learning structures, we develop a task-deep-coupling framework that facilitates deeper interaction among tasks. Through these designs, EventCompreNet achieves a comprehensive understanding of the entire event life cycle. Experimental results on four benchmark datasets demonstrate that our model significantly outperforms existing state-of-the-art time series models in fine-grained event detection and exhibits strong event comprehension capabilities.

## item_id: m_1235

TITLE: Learning to Compose Words into Sentences with Reinforcement Learning

ABSTRACT: We use reinforcement learning to learn
tree-structured neural networks for computing representations of natural language sentences.
In contrast with prior work on tree-structured models, in which the trees are either provided as input or
predicted using supervision from explicit treebank annotations,
the tree structures in this work are optimized to improve performance on a downstream task.
Experiments demonstrate the benefit of
learning task-specific composition orders, outperforming both sequential encoders and recursive encoders based on treebank annotations.
We analyze the induced trees and show that while they discover
some linguistically intuitive structures (e.g., noun phrases, simple verb phrases),
they are different than conventional English syntactic structures.

## item_id: m_1236

TITLE: Choosing Public Datasets for Private Machine Learning via Gradient Subspace Distance

ABSTRACT: Differentially private stochastic gradient descent privatizes model training by injecting noise into each iteration, where the noise magnitude increases with the number of model parameters. Recent works suggest that we can reduce the noise by leveraging public data for private machine learning, by projecting gradients onto a subspace prescribed by the public data. However, given a choice of public datasets, it is not a priori clear which one may be most appropriate for the private task. We give an algorithm for selecting a public dataset by measuring a low-dimensional subspace distance between gradients of the public and private examples. We provide theoretical analysis demonstrating that the excess risk scales with this subspace distance. This distance is easy to compute and robust to modifications in the setting. Empirical evaluation shows that trained model accuracy is monotone in this distance.

## item_id: m_1237

TITLE: Graph-informed Neural Point Process With Monotonic Nets

ABSTRACT: Multi-class event data is ubiquitous in real-world applications. The recent neural temporal point processes have used monotonic nets to model the cumulative conditional intensity to avoid an intractable integration in the likelihood. While successful, they are restricted to single-type events and easily sink into poor learning results. To address these limitations and exploit valuable structural information within event participants, we develop a Graph-Informed Neural Point Process (GINPP) that can freely handle multiple event types, greatly improve learning efficiency with the monotonic net, and effectively integrate the graph information to facilitate training. First, we find the bottleneck of the previous model arises from the standard soft-plus transformation over the output of the monotonic net, which greatly enlarges the prediction variations of the monotonic net and increases the training challenge. We propose a shift-scale version that can significantly reduce the variation and promote learning efficiency. Second, we use a conditional mark distribution to model multiple event types, without the need for explicitly estimating the intensity for each type. The latter can be much more challenging. Third, we use random walks to collect the neighborhood of each event participant and use an attention mechanism to update the hidden state of each participant according to the observed events of both the participant itself and its neighborhood. In this way, we can effectively leverage the graph knowledge, and scale up to large graphs. We have shown the advantage of our approach in both ablation studies and real-world applications.

## item_id: m_1238

TITLE: LeCO-NeRF: Learning Compact Occupancy for Large-scale Neural Radiance Fields

ABSTRACT: Neural Radiance Fields (NeRFs) have shown impressive results in modeling large-scale scenes. A critical problem is how to effectively estimate the occupancy to guide empty-space skipping and point sampling. Although grid-based methods show their advantages in occupancy estimation for small-scale scenes, large-scale scenes typically have irregular scene bounds and more complex scene geometry and appearance distributions, which present severe challenges to the grid-based methods for handling large scenes, because of the limitations of predefined bounding boxes and grid resolutions, and high memory usage for grid updating. In this paper, we propose to learn a compact and efficient occupancy representation of large-scale scenes. Our main contribution is to learn and encode the occupancy of a scene into a compact MLP in an efficient and self-supervised manner. We achieve this by three core designs. First, we propose a novel Heterogeneous Mixture of Experts (HMoE) structure with common Scene Experts and a tiny Empty-Space Expert. The heterogeneous structure can be effectively used to model the imbalanced unoccupied and occupied regions in NeRF where unoccupied regions need much fewer parameters. Second, we propose a novel imbalanced gate loss for HMoE, motivated by the prior that most of the 3D points are unoccupied. It enables the gating network of HMoE to accurately dispatch the unoccupied and occupied points. Third, we also design an explicit density loss to guide the gating network. Then, the occupancy of the entire large-scale scene can be encoded into a very compact gating network of the HMoE. As far as we know, we are the first to learn the compact occupancy of large-scale NeRF by an MLP. We show in the experiments that our occupancy network can very quickly learn more accurate, smooth, and clean occupancy compared to the occupancy grid. With our learned occupancy as guidance for empty space skipping, our method can consistently obtain $2.5\times$ speed-up on the state-of-the-art method Switch-NeRF, while achieving highly competitive performances on several challenging large-scale benchmarks.

## item_id: m_1239

TITLE: Model-agnostic Measure of Generalization Difficulty

ABSTRACT: The measure of a machine learning algorithm is the difficulty of the tasks it can perform, and sufficiently difficult tasks are critical drivers of strong machine learning models. However, quantifying the generalization difficulty of machine learning benchmarks has remained challenging. We propose what is to our knowledge the first model-agnostic measure of the inherent generalization difficulty of tasks. Our inductive bias complexity measure quantifies the total information required to generalize well on a task minus the information provided by the data. It does so by measuring the fractional volume occupied by hypotheses that generalize on a task given that they fit the training data. It scales exponentially with the intrinsic dimensionality of the space over which the model must generalize but only polynomially in resolution per dimension, showing that tasks which require generalizing over many dimensions are drastically more difficult than tasks involving more detail in fewer dimensions. Our measure can be applied to compute and compare supervised learning, reinforcement learning and meta-learning task difficulties against each other. We show that applied empirically, it formally quantifies intuitively expected trends, e.g. that in terms of required inductive bias, MNIST $<$ CIFAR10 $<$ Imagenet and fully observable Markov decision processes (MDPs) $<$ partially observable MDPs. Further, we show that classification of complex images $<$ few-shot meta-learning with simple images. Our measure provides a quantitative metric to guide the construction of more complex tasks requiring greater inductive bias, and thereby encourages the development of more sophisticated architectures and learning algorithms with more powerful generalization capabilities.

## item_id: m_1240

TITLE: Regularly varying representation for sentence embedding

ABSTRACT: The dominant approaches to sentence representation in natural language rely on learning embeddings on massive corpuses. The obtained embeddings have desirable properties such as compositionality and distance preservation (sentences with similar meanings have similar representations). In this paper, we develop a novel method for learning an embedding enjoying a dilation invariance property. We propose two algorithms: Orthrus, a classification algorithm, constrains the distribution of the embedded variable to be regularly varying, i.e. multivariate heavy-tail. and uses Extreme Value Theory (EVT) to tackle the classification task on two separate regions: the tail and the bulk. Hydra, a text generation algorithm for dataset augmentation, leverages the invariance property of the embedding learnt by Orthrus to generate coherent sentences with controllable attribute, e.g. positive or negative sentiment. Numerical experiments on synthetic and real text data demonstrate the relevance of the proposed framework.


## item_id: m_1241

TITLE: Language Models' Internal Conflicts: Layer-wise Usable Information For Detecting Model (Un)answerability

ABSTRACT: We propose a new framework for detecting unanswerable questions. Large language models often sound overly convincing when providing inaccurate answers. We explore how language models behave when required to answer questions without relevant information in the provided context, a situation that is likely to result in hallucination. We state that unanswerable questions represent a deficiency of $\mathcal{V}$-usable information across the layers of a pre-trained language model $\mathcal{V}$. To capture this, we propose a layer-wise usable information ($\mathcal{L}$I), tracking how much information is usable by language models within their mechanism of updating layers. We empirically argue that information is not always monotonically gained or lost across layers, and hence tracking all the layers within the language models is far more informative than embracing the final layer as the complete form of computation. 
Our method does not require label annotations to fine-tune classifiers or modify model architectures. Hence it is computationally feasible to universal large language models.

## item_id: m_1242

TITLE: Why Does Hierarchy (Sometimes) Work So Well in Reinforcement Learning?

ABSTRACT: Hierarchical reinforcement learning has demonstrated significant success at solving difficult reinforcement learning (RL) tasks. Previous works have motivated the use of hierarchy by appealing to a number of intuitive benefits, including learning over temporally extended transitions, exploring over temporally extended periods, and training and exploring in a more semantically meaningful action space, among others. However, in fully observed, Markovian settings, it is not immediately clear why hierarchical RL should provide benefits over standard "shallow" RL architectures. In this work, we isolate and evaluate the claimed benefits of hierarchical RL on a suite of tasks encompassing locomotion, navigation, and manipulation.
Surprisingly, we find that most of the observed benefits of hierarchy can be attributed to improved exploration, as opposed to easier policy learning or imposed hierarchical structures. Given this insight, we present exploration techniques inspired by hierarchy that achieve performance competitive with hierarchical RL while at the same time being much simpler to use and implement. 

## item_id: m_1243

TITLE: Single Pair Cross-Modality Super Resolution

ABSTRACT: Non-visual imaging sensors are widely used in the industry for different purposes. Those sensors are more expensive than visual (RGB) sensors, and usually produce images with lower resolution. To this end, Cross-Modality Super-Resolution methods were introduced, where an RGB image of a high-resolution assists in increasing the resolution of a low-resolution modality. However, fusing images from different modalities is not a trivial task, since each multi-modal pair varies greatly in its internal correlations. For this reason, traditional state-of-the-arts which are trained on external datasets often struggle with yielding an artifact-free result that is still loyal to the target modality characteristics.

We present CMSR, a single-pair approach for Cross-Modality Super-Resolution. The network is internally trained on the two input images only, in a self-supervised manner, learns their internal statistics and correlations, and applies them to upsample the target modality. CMSR contains an internal transformer which is trained on-the-ﬂy together with the up-sampling process itself and without supervision, to allow dealing with pairs that are only weakly aligned. We show that CMSR produces state-of-the-art super resolved images, yet without introducing artifacts or irrelevant details that originate from the RGB image only.

## item_id: m_1244

TITLE: Natural Image Manipulation for Autoregressive Models Using Fisher Scores

ABSTRACT: Deep autoregressive models are one of the most powerful models that exist today which achieve state-of-the-art bits per dim. However, they lie at a strict disadvantage when it comes to controlled sample generation compared to latent variable models. Latent variable models such as VAEs and normalizing flows allow meaningful semantic manipulations in latent space, which autoregressive models do not have. In this paper, we propose using Fisher scores as a method to extract embeddings from an autoregressive model to use for interpolation and show that our method provides more meaningful sample manipulation compared to alternate embeddings such as network activations.

## item_id: m_1245

TITLE: Efficient Lifelong Learning with A-GEM

ABSTRACT: In lifelong learning, the learner is presented with a sequence of tasks, incrementally building a data-driven prior which may be leveraged to speed up learning of a new task. In this work, we investigate the efficiency of current lifelong approaches, in terms of sample complexity, computational and memory cost. Towards this end, we first introduce a new and a more realistic evaluation protocol, whereby learners observe each example only once and hyper-parameter selection is done on a small and disjoint set of tasks, which is not used for the actual learning experience and evaluation. Second, we introduce a new metric measuring how quickly a learner acquires a new skill. Third, we propose an improved version of GEM (Lopez-Paz & Ranzato, 2017), dubbed Averaged GEM (A-GEM), which enjoys the same or even better performance as GEM, while being almost as computationally and memory efficient as EWC (Kirkpatrick et al., 2016) and other regularization-based methods. Finally, we show that all algorithms including A-GEM can learn even more quickly if they are provided with task descriptors specifying the classification tasks under consideration. Our experiments on several standard lifelong learning benchmarks demonstrate that A-GEM has the best trade-off between accuracy and efficiency

## item_id: m_1246

TITLE: Dynamical System Embedding for Efficient Intrinsically Motivated Artificial Agents

ABSTRACT: Mutual Information between agent Actions and environment States (MIAS) quantifies the influence of agent on its environment. Recently, it was found that intrinsic motivation in artificial agents emerges from the maximization of MIAS.
For example, empowerment is an information-theoretic approach to intrinsic motivation, which has been shown to solve a broad range of standard RL benchmark problems. The estimation of empowerment for arbitrary dynamics is a challenging problem because it relies on the estimation of MIAS. Existing approaches rely on sampling, which have formal limitations, requiring exponentially many samples. In this work, we develop a novel approach for the estimation of empowerment in unknown arbitrary dynamics from visual stimulus only, without sampling for the estimation of MIAS. The core idea is to represent the relation between action sequences and future states by a stochastic dynamical system in latent space, which admits an efficient estimation of MIAS by the ``Water-Filling" algorithm from information theory. We construct this embedding with deep neural networks trained on a novel objective function and demonstrate our approach by numerical simulations of non-linear continuous-time dynamical systems. We show that the designed embedding preserves information-theoretic properties of the original dynamics, and enables us to solve the standard AI benchmark problems.

## item_id: m_1247

TITLE: The Context-Aware Learner

ABSTRACT: One important aspect of generalization in machine learning involves reasoning about previously seen data in new settings. Such reasoning requires learning disentangled representations of data which are interpretable in isolation, but can also be combined in a new, unseen scenario. To this end, we introduce the context-aware learner, a model based on the variational autoencoding framework, which can learn such representations across data sets exhibiting a number of distinct contexts. Moreover, it is successfully able to combine these representations to generate data not seen at training time. The model enjoys an exponential increase in representational ability for a linear increase in context count. We demonstrate that the theory readily extends to a meta-learning setting such as this, and describe a fully unsupervised model in complete generality. Finally, we validate our approach using an adaptation with weak supervision.

## item_id: m_1248

TITLE: Speech denoising by listening to noise

ABSTRACT: Speech denoising is the task of obtaining clean speech from the speech signal corrupted by background noise. Except in high end recording studios, we do not get clean speech signal as some background noise, or noise due to the recording device is always present. We propose an approach to denoise noisy speech signal by modeling the noise explicitly. Existing approaches model speech, potentially of multiple speakers, for denoising. Such approaches have an inherent drawback as a separate model is required for each speaker. We show that instead of modeling speaker(s), modelling the noise helps obtain a unified speaker independent denoiser, cf.\ speaker dependent ones in existing popular approaches. In addition to a novel speech denoising network, we also propose a large scale noise dataset, \texttt{AudioNoiseSet}, derived from Audioset dataset, to train our model. We show that our model outperforms prior approaches by significant margin in a large scale, in the wild speech datasets, \ie AVspeech, with standard quantitative metrics. In addition we show with multiple human ratings that the method is preferred over state-of-the-art approaches. The user study also points towards limitations of the metrics used, which we discuss. We also provide many qualitative results to demonstrate our better results.


## item_id: m_1249

TITLE: MS3: A Multimodal Supervised Pretrained Model for Semantic Segmentation

ABSTRACT: Due to the limited labeled data, current segmentation models are usually transferred from ImageNet pretrained models. This pipeline introduces task gaps, where the pretraining is based on global image-level recognition while the downstream is focused on local pixel level prediction. In this paper, we aim at mitigating this task gap and building a segmentation-oriented pretrained model, in this way different downstream segmentation tasks can be better and easily adapted. Towards this goal, we combine off-the-shelf annotations from diverse segmentation datasets and make use of both visual and language supervision for jointly training. The highlight is that the two kinds of supervision are complementary and can be boosted to better model the class relation from diverse datasets. The proposed learning framework, termed as MS3 (short for Multimodal Supervision for Semantic Segmentation), not only adjusts and improves the quality of language embeddings to fit the segmentation scene, but also generates momentum-updated visual embeddings for each category to facilitate better visual representation modeling. Besides, considering that the original one-by-one pixel-embedding pairing may cause similar classes from other datasets to be incorrectly pulled away, we further extend the original loss with multi-label mapping via cross-modal information exchange to better model the class relations. Experiments conducted on several benchmarks demonstrate that MS3 consistently outperforms the ImageNet pretrained models by a considerable margin under standard fine-tuning, as well as fitting some rapid deployment scenarios, e.g., frozen-backbone fine-tuning or zero shot predicting.

## item_id: m_1250

TITLE: Inverse Virtual Try-On: Generating Multi-Category Product-Style Images from Clothed Individuals

ABSTRACT: Virtual try-on (VTON) has been widely explored for rendering garments onto person images, while its inverse task, virtual try-off (VTOFF), remains largely overlooked. VTOFF aims to recover standardized product images of garments directly from photos of clothed individuals. This capability is of great practical importance for e-commerce platforms, large-scale dataset curation, and the training of foundation models. Unlike VTON, which must handle diverse poses and styles, VTOFF naturally benefits from a consistent output format in the form of flat garment images. However, existing methods face two major limitations: (i) exclusive reliance on visual cues from a single photo often leads to ambiguity, and (ii) generated images usually suffer from loss of fine details, limiting their real-world applicability.
To address these challenges, we introduce TEMU-VTOFF, a Text-Enhanced MUlti-category framework for VTOFF. Our architecture is built on a dual DiT-based backbone equipped with a multimodal attention mechanism that jointly exploits image, text, and mask information to resolve visual ambiguities and enable robust feature learning across garment categories. To explicitly mitigate detail degradation, we further design an alignment module that refines garment structures and textures, ensuring high-quality outputs. Extensive experiments on VITON-HD and Dress Code show that TEMU-VTOFF achieves new state-of-the-art performance, substantially improving both visual realism and consistency with target garments. Code and models are available at: https://temu-vtoff-page.github.io/.

## item_id: m_1251

TITLE: Explorative Latent Self-Supervised Active Search Algorithm (ELSA)

ABSTRACT: In computer vision, attaining exceptional performance often necessitates access to large labeled datasets. The creation of extensive datasets through manual annotation is not only cost-prohibitive but also practically infeasible due to the scarcity of positive samples in imbalanced datasets where negative samples dominate. To tackle this intricate problem, we introduce Efficient Latent Space-based Self-Supervised Active Learning Search (ELSA), an active learning-based labeling assistant. ELSA distinguishes itself from existing interactive annotation methods by focusing exclusively on positive class labeling in massively imbalanced datasets replete with a substantial number of negative samples. Through the automatic exclusion of the majority of negative samples, ELSA achieves a remarkable level of precision and accuracy in its search. This novel framework comprises three fundamental components: a)an iterative Nearest Neighbor Search, b)a Sophisticated Random Sampler, c)a Linear Head powered by Active Learning. Our comprehensive study provides insights into the interplay of these components and their collective impact on search efficiency. Notably, we demonstrate that ELSA achieves orders of magnitude superior performance, in average starting with as little as 5 or less positive samples in ImageNet 1k we managed to detect as much as 80\% of all the examples belonging to that class by only labeling as little as 0.67\% of the entire dataset manually.

## item_id: m_1252

TITLE: Multi-Task Learning for Document Ranking and Query Suggestion

ABSTRACT: We propose a multi-task learning framework to jointly learn document ranking and query suggestion for web search. It consists of two major components, a document ranker, and a query recommender. Document ranker combines current query and session information and compares the combined representation with document representation to rank the documents. Query recommender tracks users' query reformulation sequence considering all previous in-session queries using a sequence to sequence approach. As both tasks are driven by the users' underlying search intent, we perform joint learning of these two components through session recurrence, which encodes search context and intent. Extensive comparisons against state-of-the-art document ranking and query suggestion algorithms are performed on the public AOL search log, and the promising results endorse the effectiveness of the joint learning framework.

## item_id: m_1253

TITLE: Budgeted Training for Vision Transformer

ABSTRACT: The superior performances of Vision Transformers often come with higher training costs. Compared to their CNN counterpart, Transformer models are hungry for large-scale data and their training schedules are usually prolonged. This sets great restrictions on training Transformers with limited resources, where a proper trade-off between training cost and model performance is longed. In this paper, we address the problem by proposing a framework that enables the training process under \textit{any training budget} from the perspective of model structure, while achieving competitive model performances. Specifically, based on the observation that Transformer exhibits different levels of model redundancies at different training stages, we propose to dynamically control the activation rate of the model structure along the training process and meet the demand on the training budget by adjusting the duration on each level of model complexity. Extensive experiments demonstrate that our framework is applicable to various Vision Transformers, and achieves competitive performances on a wide range of training budgets. 

## item_id: m_1254

TITLE: Data-centric Prediction Explanation via Kernelized Stein Discrepancy

ABSTRACT: Existing example-based prediction explanation methods often bridge test and training data points through the model’s parameters or latent representations. While these methods offer clues to the causes of model predictions, they often exhibit innate shortcomings, such as incurring significant computational overhead or producing coarse-grained explanations. This paper presents a Highly-precise and Data-centric Explanation (HD-Explain) prediction explanation method that exploits properties of Kernelized Stein Discrepancy (KSD). Specifically, the KSD uniquely defines a parameterized kernel function for a trained model that encodes model-dependent data correlation. By leveraging the kernel function, one can identify training samples that provide the best predictive support to a test point efficiently. We conducted thorough analyses and experiments across multiple classification domains, where we show that HD-Explain outperforms existing methods from various aspects, including 1) preciseness (fine-grained explanation), 2) consistency, and 3) computation efficiency, leading to a surprisingly simple, effective, and robust prediction explanation solution.

## item_id: m_1255

TITLE: An Empirical Analysis of Deep Network Loss Surfaces

ABSTRACT: The training of deep neural networks is a high-dimension optimization problem with respect to the loss function of a model. Unfortunately, these functions are of high dimension and non-convex and hence difficult to characterize. In this paper, we empirically investigate the geometry of the loss functions for state-of-the-art networks with multiple stochastic optimization methods. We do this through several experiments that are visualized on polygons to understand how and when these stochastic optimization methods find minima.

## item_id: m_1256

TITLE: Efficient Federated Learning via Variational Dropout

ABSTRACT: As an emerging field, federated learning has recently attracted considerable attention.
Compared to distributed learning in the datacenter setting, federated learning
has more strict constraints on computate efficiency of the learned model and communication
cost during the training process. In this work, we propose an efficient
federated learning framework based on variational dropout. Our approach is able
to jointly learn a sparse model while reducing the amount of gradients exchanged
during the iterative training process. We demonstrate the superior performance
of our approach on achieving significant model compression and communication
reduction ratios with no accuracy loss.

## item_id: m_1257

TITLE: Convex Dominance in Deep Learning I: A Scaling Law of Loss and Learning Rate

ABSTRACT: Deep learning has non-convex loss landscape and its optimization dynamics is hard to analyze or control. Nevertheless, the dynamics can be empirically convex-like across various tasks, models, optimizers, hyperparameters, etc. In this work, we examine the applicability of convexity and Lipschitz continuity in deep learning, in order to precisely control the loss dynamics via the learning rate schedules. We illustrate that deep learning quickly becomes weakly convex after a short period of training, and the loss is predicable by an upper bound on the last iterate, which further informs the scaling of optimal learning rate. Through the lens of convexity, we build scaling laws of learning rates and losses that extrapolate as much as $80\times$ across training horizons and $70\times$ across model sizes.

## item_id: m_1258

TITLE: The Variational Homoencoder: Learning to Infer High-Capacity Generative Models from Few Examples

ABSTRACT: Hierarchical Bayesian methods have the potential to unify many related tasks (e.g. k-shot classification, conditional, and unconditional generation) by framing each as inference within a single generative model. We show that existing approaches for learning such models can fail on expressive generative networks such as PixelCNNs, by describing the global distribution with little reliance on latent variables. To address this, we develop a modification of the Variational Autoencoder in which encoded observations are decoded to new elements from the same class; the result, which we call a Variational Homoencoder (VHE), may be understood as training a hierarchical latent variable model which better utilises latent variables in these cases. Using this framework enables us to train a hierarchical PixelCNN for the Omniglot dataset, outperforming all existing models on test set likelihood. With a single model we achieve both strong one-shot generation and near human-level classification, competitive with state-of-the-art discriminative classifiers. The VHE objective extends naturally to richer dataset structures such as factorial or hierarchical categories, as we illustrate by training models to separate character content from simple variations in drawing style, and to generalise the style of an alphabet to new characters.

## item_id: m_1259

TITLE: Adversarially Guided Actor-Critic

ABSTRACT: Despite definite success in deep reinforcement learning problems, actor-critic algorithms are still confronted with sample inefficiency in complex environments, particularly in tasks where efficient exploration is a bottleneck. These methods consider a policy (the actor) and a value function (the critic) whose respective losses are built using different motivations and approaches. This paper introduces a third protagonist: the adversary. While the adversary mimics the actor by minimizing the KL-divergence between their respective action distributions, the actor, in addition to learning to solve the task, tries to differentiate itself from the adversary predictions. This novel objective stimulates the actor to follow strategies that could not have been correctly predicted from previous trajectories, making its behavior innovative in tasks where the reward is extremely rare. Our experimental analysis shows that the resulting Adversarially Guided Actor-Critic (AGAC) algorithm leads to more exhaustive exploration. Notably, AGAC outperforms current state-of-the-art methods on a set of various hard-exploration and procedurally-generated tasks.

## item_id: m_1260

TITLE: Zebra: In-Context and Generative Pretraining for Solving Parametric PDEs

ABSTRACT: Solving time-dependent parametric partial differential equations (PDEs) is challenging, as models must adapt to variations in parameters such as coefficients, forcing terms, and boundary conditions. Data-driven neural solvers either train on data sampled from the PDE parameters distribution in the hope that the model generalizes to new instances or rely on gradient-based adaptation and meta-learning to implicitly encode the dynamics from observations. This often comes with increased inference complexity.
Inspired by the in-context learning capabilities of large language models (LLMs), we introduce Zebra, a novel generative auto-regressive transformer designed to solve parametric PDEs without requiring gradient adaptation at inference. By leveraging in-context information during both pre-training and inference, Zebra dynamically adapts to new tasks by conditioning on input sequences that incorporate context trajectories or preceding states. This approach enables Zebra to flexibly handle arbitrarily sized context inputs and supports uncertainty quantification through the sampling of multiple solution trajectories.
We evaluate Zebra across a variety of challenging PDE scenarios, demonstrating its adaptability, robustness, and superior performance compared to existing approaches.

## item_id: m_1261

TITLE: Adaptive Acquisition Selection for Bayesian Optimization with Large Language Models

ABSTRACT: Bayesian Optimization critically depends on the choice of acquisition function, but no single strategy is universally optimal; the best choice is non-stationary and problem-dependent. 
Existing adaptive portfolio methods often base their decisions on past function values while ignoring richer information like remaining budget or surrogate model characteristics. 
To address this, we introduce LMABO, a novel framework that casts a pre-trained Large Language Model (LLM) as a zero-shot, online strategist for the BO process. 
At each iteration, LMABO uses a structured state representation to prompt the LLM to select the most suitable acquisition function from a diverse portfolio.
In an evaluation across 50 benchmark problems, LMABO demonstrates a significant performance improvement over strong static, adaptive portfolio, and other LLM-based baselines. 
We show that the LLM's behavior is a comprehensive strategy that adapts to real-time progress, proving its advantage stems from its ability to process and synthesize the complete optimization state into an effective, adaptive policy.

## item_id: m_1262

TITLE: Perturb-and-Compare Approach for Detecting Out-of-Distribution Samples in Constrained Access Environments

ABSTRACT: Accessing machine learning models through remote APIs has been gaining more prevalence following the recent trend of scaling up model parameters for increased performance. Even though these models exhibit remarkable ability, detecting out-of-distribution (OOD) samples is still an important issue concerning the safety of the end users, as these samples may induce unreliable outputs from the model. In this work, we propose an OOD detection framework, MixDiff, that is applicable even when the model parameters or its activations are not accessible to the end user. To bypass the access restriction, MixDiff applies an identical input-level perturbation to a given target sample and an in-distribution (ID) sample that is similar to the target and compares the relative difference of the model outputs of these two samples. MixDiff is model-agnostic and compatible with existing output-based OOD detection methods. We provide theoretical analysis to illustrate MixDiff’s effectiveness at discerning OOD samples that induce overconfident outputs from the model and empirically show that MixDiff consistently improves the OOD detection performance on various datasets in vision and text domains.

## item_id: m_1263

TITLE: Behaviour Suite for Reinforcement Learning

ABSTRACT: This paper introduces the Behaviour Suite for Reinforcement Learning, or bsuite for short. bsuite is a collection of carefully-designed experiments that investigate core capabilities of reinforcement learning (RL) agents with two objectives. First, to collect clear, informative and scalable problems that capture key issues in the design of general and efficient learning algorithms. Second, to study agent behaviour through their performance on these shared benchmarks. To complement this effort, we open source this http URL, which automates evaluation and analysis of any agent on bsuite. This library facilitates reproducible and accessible research on the core issues in RL, and ultimately the design of superior learning algorithms. Our code is Python, and easy to use within existing projects. We include examples with OpenAI Baselines, Dopamine as well as new reference implementations. Going forward, we hope to incorporate more excellent experiments from the research community, and commit to a periodic review of bsuite from a committee of prominent researchers.

## item_id: m_1264

TITLE: UGC: UNIVERSAL GRAPH COARSENING

ABSTRACT: In the era of big data, graphs have emerged as a natural representation for intricate relationships. However, graph sizes often become unwieldy, leading to storage, computation, and analysis challenges. A crucial demand arises for methods that can effectively downsize large graphs while retaining vital insights. Graph coarsening seeks to simplify large graphs while maintaining essential features. Most published methods are suitable for homophilic datasets, limiting their universal use. We propose Universal Graph Coarsening (UGC), a framework equally suitable for homophilic and heterophilic datasets. UGC integrates node attributes and adjacency information, leveraging the dataset's heterophily factor and is a first ever linear time-complexity framework. Results on benchmark datasets demonstrate that UGC preserves spectral similarity while coarsening. In comparison to state of the art methods, UGC is 4x to 15x faster, has lower eigen-error, and yields superior performance on downstream processing tasks even at 70\% coarsening ratios.

## item_id: m_1265

TITLE: Learning Altruistic Behaviours in Reinforcement Learning without External Rewards

ABSTRACT: Can artificial agents learn to assist others in achieving their goals without knowing what those goals are? Generic reinforcement learning agents could be trained to behave altruistically towards others by rewarding them for altruistic behaviour, i.e., rewarding them for benefiting other agents in a given situation. Such an approach assumes that other agents' goals are known so that the altruistic agent can cooperate in achieving those goals. However, explicit knowledge of other agents' goals is often difficult to acquire. In the case of human agents, their goals and preferences may be difficult to express fully; they might be ambiguous or even contradictory. Thus, it is beneficial to develop agents that do not depend on external supervision and learn altruistic behaviour in a task-agnostic manner. We propose to act altruistically towards other agents by giving them more choice and allowing them to achieve their goals better. Some concrete examples include opening a door for others or safeguarding them to pursue their objectives without interference. We formalize this concept and propose an altruistic agent that learns to increase the choices another agent has by preferring to maximize the number of states that the other agent can reach in its future. We evaluate our approach in three different multi-agent environments where another agent's success depends on altruistic behaviour. Finally, we show that our unsupervised agents can perform comparably to agents explicitly trained to work cooperatively, in some cases even outperforming them.

## item_id: m_1266

TITLE: Adversarial reading networks for machine comprehension

ABSTRACT: Machine reading has recently shown remarkable progress thanks to differentiable
reasoning models. In this context, End-to-End trainable Memory Networks
(MemN2N) have demonstrated promising performance on simple natural language
based reasoning tasks such as factual reasoning and basic deduction. However,
the task of machine comprehension is currently bounded to a supervised setting
and available question answering dataset. In this paper we explore the paradigm
of adversarial learning and self-play for the task of machine reading comprehension.
Inspired by the successful propositions in the domain of game learning, we
present a novel approach of training for this task that is based on the definition
of a coupled attention-based memory model. On one hand, a reader network is
in charge of finding answers regarding a passage of text and a question. On the
other hand, a narrator network is in charge of obfuscating spans of text in order
to minimize the probability of success of the reader. We experimented the model
on several question-answering corpora. The proposed learning paradigm and associated
models present encouraging results.

## item_id: m_1267

TITLE: Machine Learning Applications in Forecasting of COVID-19 Based on Patients' Individual Symptoms

ABSTRACT: Predicting the COVID-19 outbreak has been studied by many researchers in recent years. Many
machine learning models have been used for the prediction of the transmission in a country or
region, but few studies aim to predict whether an individual has been infected by COVID-19.
However, due to the gravity of this global pandemic, prediction at an individual level is critical.
The objective of this paper is to predict if an individual has COVID-19 based on the symptoms
and features. The prediction results can help the government better allocate the medical resources
during this pandemic. Data of this study was taken on June 18th from the Israeli Ministry of
Health on COVID-19. The purpose of this study is to compare and analyze different models,
which are Support Vector Machine (SVM), Logistic Regression (LR), Naive Bayesian (NB),
Decision Tree (DT), Random Forest (RF) and Neural Network (NN).

## item_id: m_1268

TITLE: GDL-DS: A Benchmark for Geometric Deep Learning under Distribution Shifts

ABSTRACT: Geometric deep learning (GDL) has gained significant attention in various scientific fields, chiefly for its proficiency in modeling data with intricate geometric structures. Yet, very few works have delved into its capability of tackling the distribution shift problem, a prevalent challenge in many relevant applications. To bridge this gap, we propose GDL-DS, a comprehensive benchmark designed for evaluating the performance of GDL models in scenarios with distribution shifts. Our evaluation datasets cover diverse scientific domains from particle physics and material science to biochemistry, and encapsulates a broad spectrum of distribution shifts including conditional, covariate, and concept shifts. 
Furthermore, we study three levels of information access from the out-of-distribution (OOD) testing data, including no OOD information, only OOD features without labels, and OOD features with a few labels. 
Overall, our benchmark results in 30 different experiment settings, and evaluates 3 GDL backbones and 11 learning algorithms in each setting. A thorough analysis of the evaluation results is provided, poised to illuminate insights for DGL researchers and domain practitioners who are to use DGL in their applications.

## item_id: m_1269

TITLE: Self-supervised Learning for Sequential Recommendation with Model Augmentation

ABSTRACT: The sequential recommendation aims at predicting the next items in user behaviors, which can be solved by characterizing item relationships in sequences. Due to the data sparsity and noise issues in sequences, a new self-supervised learning (SSL) paradigm is proposed to improve the performance, which employs contrastive learning between positive and negative views of sequences. 
However, existing methods all construct views by adopting augmentation from data perspectives, while we argue that 1) optimal data augmentation methods are hard to devise, 2) data augmentation methods destroy sequential correlations, and 3) data augmentation fails to incorporate comprehensive self-supervised signals. 
Therefore, we investigate the possibility of model augmentation to construct view pairs. We propose three levels of model augmentation methods: neuron masking, layer dropping, and encoder complementing. 
This work opens up a novel direction in constructing views for contrastive SSL. Experiments verify the efficacy of model augmentation for the SSL in the sequential recommendation. 


## item_id: m_1270

TITLE: Towards Adapting Vision-Language Models for Semi-Supervised Domain Generalization

ABSTRACT: Semi-supervised Domain Generalization (SSDG) offers a cost-effective solution for generalizing models to unseen domains with limited labels. While existing SSDG methods, mainly built upon small-scale backbones, struggle to match fully supervised DG performance, large-scale vision-language models like CLIP have shown remarkable generalization through downstream fine-tuning. However, adapting these models to SSDG remains underexplored. In this paper, we identify a critical issue: existing popular fine-tuning methods suffer from under-utilizing unlabeled data in the semi-supervised learning frameworks, thereby overfitting the limited labeled data, leading to training collapse and generalization ability degradation. To address these challenges, we propose two novel components: (1) the De-False-Correlation Adapter (DFC-Adapter), which reduces false correlations to refine visual features and (2) Learnable Multi-granularity Text-guided Embedding Augmentation (LMTEA), which synthesizes semantic-aligned but domain-perturbed augmented visual embedding for consistency regularization through multi-granularity text guidance and learnable style encoding. We establish the first benchmark for CLIP fine-tuning methods in SSDG, conducting extensive experiments across six DG datasets and two ImageNet variants. Our results demonstrate that our method significantly outperforms existing CLIP fine-tuning approaches and achieves performance comparable to fully supervised DG methods in some cases.

## item_id: m_1271

TITLE: Multi-Agent Collaboration via Reward Attribution Decomposition

ABSTRACT: Recent advances in multi-agent reinforcement learning (MARL) have achieved super-human performance in games like Quake 3 and Dota 2. Unfortunately, these techniques require orders-of-magnitude more training rounds than humans and don't generalize to new agent configurations even on the same game. In this work, we propose Collaborative Q-learning (CollaQ) that achieves state-of-the-art performance in the StarCraft multi-agent challenge and supports ad hoc team play. We first formulate multi-agent collaboration as a joint optimization on reward assignment and show that each agent has an approximately optimal policy that decomposes into two parts: one part that only relies on the agent's own state, and the other part that is related to states of nearby agents. Following this novel finding, CollaQ decomposes the Q-function of each agent into a self term and an interactive term, with a Multi-Agent Reward Attribution (MARA) loss that regularizes the training. CollaQ is evaluated on various StarCraft maps and shows that it outperforms existing state-of-the-art techniques  (i.e., QMIX, QTRAN, and VDN) by improving the win rate by 40% with the same number of samples. In the more challenging ad hoc team play setting (i.e., reweight/add/remove units without re-training or finetuning), CollaQ outperforms previous SoTA by over 30%. 

## item_id: m_1272

TITLE: Entropy Never Lies: Signed Entropy Integral Unmasks Mislabeled Data

ABSTRACT: Mislabeled samples in training datasets severely degrade the performance of deep networks, as overparameterized models tend to memorize erroneous labels. We address this challenge by proposing a novel approach for mislabeled data detection that leverages training dynamics. Our method is grounded in the key observation that correctly labeled samples exhibit consistent entropy decrease during training, while mislabeled samples maintain relatively high entropy throughout the training process. Building on this insight, we introduce a signed entropy integral (SEI) statistic that captures both the magnitude and temporal trend of prediction entropy across training epochs. SEI is broadly applicable to classification networks and demonstrates particular effectiveness when integrated with contrastive language-image pretraining (CLIP) architectures. Through extensive experiments on three medical imaging datasets---a domain particularly susceptible to labeling errors due to diagnostic complexity---spanning diverse modalities and pathologies, we demonstrate that SEI achieves state-of-the-art performance in mislabeled data identification, outperforming existing methods while maintaining computational efficiency and implementation simplicity.

## item_id: m_1273

TITLE: Improving Policy Gradient by Exploring Under-appreciated Rewards

ABSTRACT: This paper presents a novel form of policy gradient for model-free reinforcement learning (RL) with improved exploration properties. Current policy-based methods use entropy regularization to encourage undirected exploration of the reward landscape, which is ineffective in high dimensional spaces with sparse rewards. We propose a more directed exploration strategy that promotes exploration of under-appreciated reward regions. An action sequence is considered under-appreciated if its log-probability under the current policy under-estimates its resulting reward. The proposed exploration strategy is easy to implement, requiring only small modifications to the standard REINFORCE algorithm. We evaluate the approach on a set of algorithmic tasks that have long challenged RL methods. We find that our approach reduces hyper-parameter sensitivity and demonstrates significant improvements over baseline methods. Notably, the approach is able to solve a benchmark multi-digit addition task. To our knowledge, this is the first time that a pure RL method has solved addition using only reward feedback.

## item_id: m_1274

TITLE: Boosting the Actor with Dual Critic

ABSTRACT: This paper proposes a new actor-critic-style algorithm called Dual Actor-Critic or Dual-AC.  It is derived in a principled way from the Lagrangian dual form of the Bellman optimality equation, which can be viewed as a two-player game between the actor and a critic-like function, which is named as dual critic.  Compared to its actor-critic relatives, Dual-AC has the desired property that the actor and dual critic are updated cooperatively to optimize the same objective function, providing a more transparent way for learning the critic that is directly related to the objective function of the actor. We then provide a concrete algorithm that can effectively solve the minimax optimization problem, using techniques of multi-step bootstrapping, path regularization, and stochastic dual ascent algorithm. We demonstrate that the proposed algorithm achieves the state-of-the-art performances across several benchmarks.

## item_id: m_1275

TITLE: MLP-based architecture with variable length input for automatic speech recognition

ABSTRACT: We propose multi-layer perceptron (MLP)-based architectures suitable for variable length input.
Recently, several such architectures that do not rely on self-attention have been proposed for image classification. 
They achieve performance competitive with that of transformer-based architectures, albeit with a simpler structure and low computational cost. 
They split an image into patches and mix information by applying MLPs within and across patches alternately. 
Due to the use of MLPs, one such model can only be used for inputs of a fixed, pre-defined size.
However, many types of data are naturally variable in length, for example acoustic signals. 
We propose three approaches to extend MLP-based architectures for use with sequences of arbitrary length. 
In all of them, we start by splitting the signal into contiguous tokens of fixed size (equivalent to patches in images). 
Naturally, the number of tokens is variable. 
The two first approaches use a gating mechanism that mixes local information across tokens in a shift-invariant and length-agnostic way.
One uses a depthwise convolution to derive the gate values, while the other rely on shifting tokens.
The final approach explores non-gated mixing using a circular convolution applied in the Fourier domain.
We evaluate the proposed architectures on an automatic speech recognition task with the Librispeech and Tedlium2 corpora. Compared to Transformer, our proposed architecture reduces the WER by \SI{1.9 / 3.4}{\percent} on Librispeech test-clean/test-other set, and 1.8 / 1.6 % on Tedlium2 dev/test set, using only 75.3 % of the parameters.

## item_id: m_1276

TITLE: Learning an Ethical Module for Bias Mitigation of pre-trained Models

ABSTRACT: In spite of the high performance and reliability of deep learning algorithms in broad range everyday applications, many investigations tend to show that a lot of models exhibit biases, discriminating against some subgroups of the population. This urges the practitioner to develop fair systems whose performances are uniform among individuals. In this work, we propose a post-processing method designed to mitigate bias of state-of-the-art models. It consists in learning a shallow neural network, called the Ethical Module, which transforms the deep embeddings of a pre-trained model in order to give more representation power to the disadvantaged subgroups. Its training is supervised by the von Mises-Fisher loss, whose hyperparameters allow to control the space allocated to each subgroup in the latent space. Besides being very simple, the resulting methodology is more stable and faster than most current bias mitigation methods. In order to illustrate our idea in a concrete use case, we focus here on gender bias in facial recognition and conduct extensive numerical experiments on standard datasets.

## item_id: m_1277

TITLE: Faster Last-iterate Convergence of Policy Optimization in Zero-Sum Markov Games

ABSTRACT: Multi-Agent Reinforcement Learning (MARL)---where multiple agents learn to interact in a shared dynamic environment---permeates across a wide range of critical applications. While there has been substantial progress on understanding the global convergence of policy optimization methods in single-agent RL, designing and analysis of efficient policy optimization algorithms in the MARL setting present significant challenges and new desiderata, which unfortunately, remain highly inadequately addressed by existing theory. In this paper, we focus on the most basic setting of competitive multi-agent RL, namely two-player zero-sum Markov games, and study equilibrium finding algorithms in both the infinite-horizon discounted setting and the finite-horizon episodic setting. We propose a single-loop policy optimization method with symmetric updates from both agents, where the policy is updated via the entropy-regularized optimistic multiplicative weights update (OMWU) method and the value is updated on a slower timescale. We show that, in the full-information tabular setting, the proposed method achieves a finite-time last-iterate linear convergence to the quantal response equilibrium of the regularized problem, which translates to a sublinear convergence to the Nash equilibrium by controlling the amount of regularization. Our convergence results improve upon the best known iteration complexities, and lead to a better understanding of policy optimization in competitive Markov games.

## item_id: m_1278

TITLE: Delta-Triplane Transformers as Occupancy World Models

ABSTRACT: Occupancy World Models (OWMs) aim to predict future scenes via 3D voxelized representations of the environment to support intelligent motion planning. Existing approaches typically generate full future occupancy states from VAE-style latent encodings. In contrast, we propose Delta-Triplane Transformers (DTT), a novel 4D OWM for autonomous driving. DTT adopts temporal triplane as the occupancy representation, and focuses on modeling changes in occupancy rather than dealing with full states. The core insight is that changes in the compact 3D latent space are naturally sparser and easier to model, enabling higher accuracy with a lighter-weight architecture. We first pretrain a triplane representation model that encodes 3D occupancy compactly, and then extract multi-scale motion features from historical data and iteratively predict future triplane deltas. These deltas are combined with past states to decode future occupancy and ego-motion trajectories. Extensive experiments show that DTT achieves a state-of-the-art mean IoU of 30.85, reduces mean absolute planning error to 1.0 meter, and runs in real time at 26 FPS on an RTX 4090. Demo videos and code are provided in the supplementary material.

## item_id: m_1279

TITLE: Finding Physical Adversarial Examples for Autonomous Driving with Fast and Differentiable Image Compositing

ABSTRACT: There is considerable evidence that deep neural networks are vulnerable to adversarial perturbations applied directly to their digital inputs. However, it remains an open question whether this translates to vulnerabilities in real-world systems. Specifically, in the context of image inputs to autonomous driving systems, an attack can be achieved only by modifying the physical environment, so as to ensure that the resulting stream of video inputs to the car's controller leads to incorrect driving decisions. Inducing this effect on the video inputs indirectly through the environment requires accounting for system dynamics and tracking viewpoint changes. We propose a scalable and efficient approach for finding adversarial physical modifications, using a differentiable approximation for the mapping from environmental modifications—namely, rectangles drawn on the road—to the corresponding video inputs to the controller network. Given the color, location, position, and orientation parameters of the rectangles, our mapping composites them onto pre-recorded video streams of the original environment. Our mapping accounts for geometric and color variations, is differentiable with respect to rectangle parameters, and uses multiple original video streams obtained by varying the driving trajectory. When combined with a neural network-based controller, our approach allows the design of adversarial modifications through end-to-end gradient-based optimization. We evaluate our approach using the Carla autonomous driving simulator, and show that it is significantly more scalable and far more effective at generating attacks than a prior black-box approach based on Bayesian Optimization.

## item_id: m_1280

TITLE: Generating Adversarial Examples with Adversarial Networks

ABSTRACT: Deep neural networks (DNNs) have been found to be vulnerable to adversarial examples resulting from adding small-magnitude perturbations to inputs. Such adversarial examples can mislead DNNs to produce adversary-selected results.
Different attack strategies have been proposed to generate adversarial examples, but how to produce them with high perceptual quality and more efficiently requires more research efforts. 
In this paper, we propose AdvGAN to generate adversarial examples with generative adversarial networks (GANs), which can learn and approximate the distribution of original instances. 
For AdvGAN, once the generator is trained, it can generate adversarial perturbations efficiently for any instance, so as to potentially accelerate adversarial training as defenses.  
We apply AdvGAN in both semi-whitebox and black-box attack settings. In semi-whitebox attacks, there is no need to access the original target model after the generator is trained, in contrast to traditional white-box attacks. In black-box attacks, we dynamically train a distilled model for the black-box model and optimize the generator accordingly.
Adversarial examples generated by AdvGAN on different target models have high attack success rate under state-of-the-art defenses compared to other attacks. Our attack  has placed the first with 92.76% accuracy on a public MNIST black-box attack challenge. 

## item_id: m_1281

TITLE: Learning Word-Like Units from Joint Audio-Visual Analylsis

ABSTRACT: Given a collection of images and spoken audio captions, we present a method for discovering word-like acoustic units in the continuous speech signal and grounding them to semantically relevant image regions. For example, our model is able to detect spoken instances of the words ``lighthouse'' within an utterance and associate them with image regions containing lighthouses. We do not use any form of conventional automatic speech recognition, nor do we use any text transcriptions or conventional linguistic annotations. Our model effectively implements a form of spoken language acquisition, in which the computer learns not only to recognize word categories by sound, but also to enrich the words it learns with semantics by grounding them in images.

## item_id: m_1282

TITLE: Unleashing the Creative Mind: Language Model As Hierarchical Policy For Improved Exploration on Challenging Problem Solving

ABSTRACT: Large Language Models (LLMs) have achieved tremendous progress, yet they still often struggle with challenging reasoning problems. Current approaches address this challenge by sampling or searching detailed and low-level reasoning chains. However, these methods are still limited in their exploration capabilities, making it challenging for correct solutions to stand out in the huge solution space. In this work, we unleash LLMs' creative potential for exploring multiple diverse problem solving strategies by framing an LLM as a hierarchical policy via in-context learning. This policy comprises of a visionary leader that proposes multiple diverse high-level problem-solving tactics as hints, accompanied by a follower that executes detailed problem-solving processes following each of the high-level instruction. The follower uses each of the leader's directives as a guide and samples multiple reasoning chains to tackle the problem, generating a solution group for each leader proposal. Additionally, we propose an effective and efficient tournament-based approach to select among these explored solution groups to reach the final answer. Our approach produces meaningful and inspiring hints, enhances problem-solving strategy exploration, and improves the final answer accuracy on challenging problems in the MATH dataset.

## item_id: m_1283

TITLE: Mitigating Mode Collapse in Sequential Disentanglement via an Architecture Bias

ABSTRACT: One of the fundamental representation learning tasks is unsupervised sequential disentanglement, where latent representations of the inputs are decomposed to a single static factor and a sequence of dynamic factors. To extract this latent information, existing variational methods condition the static and dynamic codes on the entire input sequence. Unfortunately, these models often suffer from mode collapse, i.e., the dynamic vectors encode static and dynamic information, leading to a non-meaningful static component.  Attempts to alleviate this problem via reducing the dynamic dimension and mutual information loss terms gain only partial success.  Often, promoting a certain functionality of the model is better achieved via specific architectural biases instead of incorporating additional loss terms. For instance, convolutional nets gain translation-invariance with shared kernels and attention models realize the underlying correspondence between source and target sentences. Inspired by these successes, we propose in this work a novel model that mitigates mode collapse by conditioning the static component on a single sample from the sequence, and subtracting the resulting code from the dynamic factors.  Remarkably, our variational model has less hyper-parameters in comparison to existing work, and it facilitates the analysis and visualization of disentangled latent data. 
We evaluate our work on multiple data-modality benchmarks including general time series, video, and audio, and we show beyond state-of-the-art results on generation and prediction tasks in comparison to several strong baselines.

## item_id: m_1284

TITLE: Eigenvalues of the Hessian in Deep Learning: Singularity and Beyond

ABSTRACT: We look at the eigenvalues of the Hessian of a loss function before and after training. The eigenvalue distribution is seen to be composed of two parts, the bulk which is concentrated around zero, and the edges which are scattered away from zero. We present empirical evidence for the bulk indicating how over-parametrized the system is, and for the edges that depend on the input data.

## item_id: m_1285

TITLE: GraphOmni: A Comprehensive and Extensible Benchmark Framework for Large Language Models on Graph-theoretic Tasks

ABSTRACT: This paper introduces GraphOmni, a comprehensive benchmark designed to evaluate the reasoning capabilities of LLMs on graph-theoretic tasks articulated in natural language. GraphOmni spans diverse graph types, serialization formats, and prompting schemes, substantially extending upon prior efforts in both scope and depth. Through systematic evaluation, we uncover critical interactions among these dimensions, revealing their decisive impact on model performance. Our experiments show that state-of-the-art closed-source models such as Claude-3.5 and o4-mini consistently lead overall, yet still leave considerable headroom, while open-source models display pronounced sensitivity to various design choices. Beyond the standard scope, larger graphs, real-world graphs, and additional NP-hard tasks are further discussed. We further analyze efficiency via output token usage, highlighting cost–accuracy trade-offs, and introduce a reinforcement learning-based optimizer that adaptively selects factor combinations, reducing evaluation cost by 75\% while retaining strong accuracy. This flexible and extensible benchmark not only deepens understanding of LLM performance on structured graph reasoning but also establishes a robust foundation for advancing model design and evaluation.

## item_id: m_1286

TITLE: SeWA: Selective Weight Average via Probabilistic Masking

ABSTRACT: Weight averaging has become a standard technique for enhancing model performance. However, methods such as Stochastic Weight Averaging (SWA) and Latest Weight Averaging (LAWA) rely on manually designed checkpoint selection rules, which struggle under unstable training dynamics. To minimize human bias, this paper proposes Selective Weight Averaging (SeWA), which adaptively selects checkpoints during the final stages of training for averaging. Both theoretically and empirically, we show that SeWA achieves a better generalization. From an algorithm implementation perspective, SeWA can be formulated as a discrete subset selection problem, which is inherently challenging to solve. To address this, we transform it into a continuous probabilistic optimization framework and employ the Gumbel-Softmax estimator to learn the non-differentiable mask for each checkpoint. Theoretically, we first prove that SeWA converges to a critical point with flatter curvature, thereby explaining its underlying mechanism. We further derive stability-based generalization bounds for SeWA, which are sharper than those of SGD under both convex and non-convex assumptions, thus providing formal guarantees of improved generalization. Finally, extensive empirical evaluations across diverse domains, including behavior cloning, image classification, and text classification, demonstrate the robustness and effectiveness of our approach.

## item_id: m_1287

TITLE: Learning a metacognition for object detection

ABSTRACT: In contrast to object recognition models, humans do not blindly trust their perception when building representations of the world, instead recruiting metacognition to detect percepts that are unreliable or false, such as when we realize that we mistook one object for another. We propose METAGEN, an unsupervised model that enhances object recognition models through a metacognition. Given noisy output from an object-detection model, METAGEN learns a meta-representation of how its perceptual system works and uses it to infer the objects in the world responsible for the detections. METAGEN achieves this by conditioning its inference on basic principles of objects that even human infants understand (known as Spelke principles: object permanence, cohesion, and spatiotemporal continuity). We test METAGEN on a variety of state-of-the-art object detection neural networks. We find that METAGEN quickly learns an accurate metacognitive representation of the neural network, and that this improves detection accuracy by filling in objects that the detection model missed and removing hallucinated objects. This approach enables generalization to out-of-sample data and outperforms comparison models that lack a metacognition.

## item_id: m_1288

TITLE: Gated Multimodal Units for Information Fusion

ABSTRACT: This paper presents a novel model for multimodal learning based on gated neural networks. The Gated Multimodal Unit (GMU) model is intended to be used as an internal unit in a neural network architecture whose purpose is to find an intermediate representation based on a combination of data from different modalities. The GMU learns to decide how modalities influence the activation of the unit using multiplicative gates. It was evaluated on a multilabel scenario for genre classification of movies using the plot and the poster. The GMU improved the macro f-score performance of single-modality approaches and outperformed other fusion strategies, including mixture of experts models. Along with this work, the MM-IMDb dataset is released which, to the best of our knowledge, is the largest publicly available multimodal dataset for genre prediction on movies.

## item_id: m_1289

TITLE: Online Target Q-learning with Reverse Experience Replay: Efficiently finding the Optimal Policy for Linear MDPs

ABSTRACT: Q-learning is a popular Reinforcement Learning (RL) algorithm which is widely used in practice with function approximation (Mnih et al., 2015). In contrast, existing theoretical results are pessimistic about Q-learning. For example, (Baird, 1995) shows that Q-learning does not converge even with linear function approximation for linear MDPs. Furthermore, even for tabular MDPs with synchronous updates, Q-learning was shown to have sub-optimal sample complexity (Li et al., 2021, Azar et al., 2013). The goal of this work is to bridge the gap between practical success of Q-learning and the relatively pessimistic theoretical results. The starting point of our work is the observation that in practice, Q-learning is used with two important modifications: (i) training with two networks, called online network and target network simultaneously (online target learning, or OTL) , and (ii) experience replay (ER) (Mnih et al., 2015). While they have been observed to play a significant role in the practical success of Q-learning, a thorough theoretical understanding of how these two modifications improve the convergence behavior of Q-learning has been missing in literature. By carefully combining the Q-learning with OTL and reverse experience replay (RER) (a form of experience replay), we present novel methods Q-Rex and Q-RexDaRe (Q-Rex+data reuse). We show that Q-Rex efficiently finds the optimal policy for linear MDPs and provide non-asymptotic bounds on sample complexity -- the first such result for a Q-learning method with linear MDPs. Furthermore, we demonstrate that Q-RexDaRe in fact achieves near optimal sample complexity in the tabular setting, improving upon the existing results for vanilla Q-learning. 


## item_id: m_1290

TITLE: Bridging HMMs and RNNs through Architectural Transformations

ABSTRACT: A distinct commonality between HMMs and RNNs is that they both learn hidden representations for sequential data. In addition, it has been noted that the backward computation  of  the  Baum-Welch  algorithm  for  HMMs  is  a  special  case  of  the back propagation algorithm used for neural networks (Eisner (2016)).  Do these observations  suggest  that,  despite  their  many apparent  differences,  HMMs  are a special case of RNNs?   In this paper,  we investigate a series of architectural transformations between HMMs and RNNs, both through theoretical derivations and empirical hybridization, to answer this question. In particular, we investigate three key design factors—independence assumptions between the hidden states and the observation, the placement of softmax, and the use of non-linearity—in order to pin down their empirical effects.  We present a comprehensive empirical study to provide insights on the interplay between expressivity and interpretability with respect to language modeling and parts-of-speech induction. 

## item_id: m_1291

TITLE: Visual Timing For Sound Source Depth Estimation in the Wild

ABSTRACT: Depth estimation enables a wide variety of 3D applications, such as robotics and autonomous driving. Despite significant work on various depth sensors, it is challenging to develop an all-in-one method to meet multiple basic criteria. In this paper, we propose a novel audio-visual learning scheme by integrating semantic features with physical spatial cues to boost monocular depth with only one microphone. Inspired by the flash-to-bang theory, we develop FBDepth, the first passive audio-visual depth estimation framework. It is based on the difference between the time-of-flight (ToF) of the light and the sound. We formulate sound source depth estimation as an audio-visual event localization task for collision events. To approach decimeter-level depth accuracy, we design a coarse-to-fine pipeline to push the temporary localization accuracy from event-level to millisecond-level by aligning audio-visual correspondence and manipulating optical flow. FBDepth feeds the estimated visual timestamp together with the audio clip and object visual features to regress the source depth. We use a mobile phone to collect 3.6K+ video clips with 24 different objects at up to 60m. FBDepth shows superior performance especially at a long range compared to monocular and stereo methods.

## item_id: m_1292

TITLE: pix2code: Generating Code from a Graphical User Interface Screenshot

ABSTRACT: Transforming a graphical user interface screenshot created by a designer into computer code is a typical task conducted by a developer in order to build customized software, websites, and mobile applications. In this paper, we show that deep learning methods can be leveraged to train a model end-to-end to automatically generate code from a single input image with over 77% of accuracy for three different platforms (i.e. iOS, Android and web-based technologies).

## item_id: m_1293

TITLE: Learning to Optimize Neural Nets

ABSTRACT: Learning to Optimize is a recently proposed framework for learning optimization algorithms using reinforcement learning. In this paper, we explore learning an optimization algorithm for training shallow neural nets. Such high-dimensional stochastic optimization problems present interesting challenges for existing reinforcement learning algorithms. We develop an extension that is suited to learning optimization algorithms in this setting and demonstrate that the learned optimization algorithm consistently outperforms other known optimization algorithms even on unseen tasks and is robust to changes in stochasticity of gradients and the neural net architecture. More specifically, we show that an optimization algorithm trained with the proposed method on the problem of training a neural net on MNIST generalizes to the problems of training neural nets on the Toronto Faces Dataset, CIFAR-10 and CIFAR-100. 

## item_id: m_1294

TITLE: RLSBench: A Large-Scale Empirical Study of Domain Adaptation Under Relaxed Label Shift

ABSTRACT: Despite the emergence of principled methods for domain adaptation under label shift (where only the class balance changes), the sensitivity of these methods to natural-seeming covariate shifts remains precariously underexplored. Meanwhile, popular deep domain adaptation heuristics, despite showing promise on benchmark datasets, tend to falter when faced with shifts in the class balance. Moreover, it's difficult to assess the state of the field owing to inconsistencies among relevant papers in evaluation criteria, datasets, and baselines. In this paper, we introduce \textsc{RLSbench}, a large-scale benchmark for such \emph{relaxed label shift} settings, consisting of 11 vision datasets spanning $>$200 distribution shift pairs with different class proportions. We evaluate 12 popular domain adaptation methods, demonstrating a more widespread susceptibility to failure under extreme shifts in the class proportions than was previously known. We develop an effective meta-algorithm, compatible with most deep domain adaptation heuristics, that consists of the following two steps: (i) \emph{pseudo-balance} the data at each epoch; and (ii) adjust the final classifier with (an estimate of) target label distribution. Furthermore, we discover that batch-norm adaption of a model trained on source with aforementioned corrections offers a strong baseline, largely missing from prior comparisons. We hope that these findings and the availability of \textsc{RLSbench} will encourage researchers to include rigorously evaluate proposed methods in relaxed label shift settings. Code is publicly available at https://github.com/ICLR2023Anon.



## item_id: m_1295

TITLE: Deep Graph Infomax

ABSTRACT: We present Deep Graph Infomax (DGI), a general approach for learning node representations within graph-structured data in an unsupervised manner. DGI relies on maximizing mutual information between patch representations and corresponding high-level summaries of graphs---both derived using established graph convolutional network architectures. The learnt patch representations summarize subgraphs centered around nodes of interest, and can thus be reused for downstream node-wise learning tasks. In contrast to most prior approaches to unsupervised learning with GCNs, DGI does not rely on random walk objectives, and is readily applicable to both transductive and inductive learning setups. We demonstrate competitive performance on a variety of node classification benchmarks, which at times even exceeds the performance of supervised learning.

## item_id: m_1296

TITLE: pSAE-chiatry: Utilizing Sparse Autoencoders to Uncover Mental-Health-Related Features in Language Models

ABSTRACT: As AI-powered mental health chatbots become more prevalent, their inability to recognize and respond to psychiatric emergencies, such as suicidality and mania, raises significant safety concerns. This study explores the internal representations of mental-health-related features (MHRF) in the Gemma-2-2B language model, focusing on crises related to suicide, mania, and psychosis. Using a sparse autoencoder (GemmaScope-RES-16K11) and psychiatric expertise (from M.D. mental health clinicians), MHRF's were identified across all 25 layers of the model, finding 29 features related to suicide and 42 to sadness. However, no features related to mania or paranoia were identified, suggesting critical gaps in the model’s ability to handle complex psychiatric symptoms. One feature pertaining to "suicide" was selected for further, directed study. Four prompts (two pertaining to homicide, two pertaining to suicide) were tested to evaluate the associated activations of this particular "suicide" feature, and this feature was preferentially activated by prompts pertaining to suicide, supporting the relevance of the identified features. Lastly, as proof-of-concept, steering Gemma-2-2B through enhancement of this "suicide" feature causally impacted model behavior, making Gemma-2-2B far more likely to discuss concepts related to suicide. These findings underscore the need for improved feature identification and modulation within AI models to enhance their safety and effectiveness in mental healthcare applications. Trigger warning: This work contains references to suicide.

## item_id: m_1297

TITLE: Understanding Local Minima in Neural Networks by Loss Surface Decomposition

ABSTRACT: To provide principled ways of designing proper Deep Neural Network (DNN) models, it is essential to understand the loss surface of DNNs under realistic assumptions. We introduce interesting aspects for understanding the local minima and overall structure of the loss surface. The parameter domain of the loss surface can be decomposed into regions in which activation values (zero or one for rectified linear units) are consistent. We found that, in each region, the loss surface have properties similar to that of linear neural networks where every local minimum is a global minimum. This means that every differentiable local minimum is the global minimum of the corresponding region. We prove that for a neural network with one hidden layer using rectified linear units under realistic assumptions. There are poor regions that lead to poor local minima, and we explain why such regions exist even in the overparameterized DNNs.

## item_id: m_1298

TITLE: Factorizing Declarative and Procedural Knowledge in Structured, Dynamical Environments

ABSTRACT: Modeling a structured, dynamic environment like a video game requires keeping track of the objects and their states (declarative knowledge) as well as predicting how objects behave (procedural knowledge). Black-box models with a monolithic hidden state often fail to apply procedural knowledge consistently and uniformly, i.e., they lack systematicity. For example, in a video game, correct prediction of one enemy's trajectory does not ensure correct prediction of another's. We address this issue via an architecture that factorizes declarative and procedural knowledge and that imposes modularity within each form of knowledge. The architecture consists of active modules called object files that maintain the state of a single object and invoke passive external knowledge sources called schemata that prescribe state updates. To use a video game as an illustration, two enemies of the same type will share schemata but will have separate object files to encode their distinct state (e.g., health, position). We propose to use attention to determine which object files to update, the selection of schemata, and the propagation of information between object files. The resulting architecture is a drop-in replacement conforming to the same input-output interface as normal recurrent networks (e.g., LSTM, GRU) yet achieves substantially better generalization on environments that have multiple object tokens of the same type, including a challenging intuitive physics benchmark.


## item_id: m_1299

TITLE: Recursive Construction of Stable Assemblies of Recurrent Neural Networks

ABSTRACT: Advanced applications of modern machine learning will likely involve combinations of trained networks, as are already used in spectacular systems such as DeepMind's AlphaGo. Recursively building such combinations in an effective and stable fashion while also allowing for continual refinement of the individual networks - as nature does for biological networks - will require new analysis tools. This paper takes a step in this direction by establishing contraction properties of broad classes of nonlinear recurrent networks and neural ODEs, and showing how these quantified properties allow in turn to recursively construct stable networks of networks in a systematic fashion. The results can also be used to stably combine recurrent networks and physical systems with quantified contraction properties. Similarly, they may be applied to modular computational models of cognition. We perform experiments with these combined networks on benchmark sequential tasks (e.g permuted sequential MNIST) to demonstrate their capacity for processing information across a long timescale in a provably stable manner.

## item_id: m_1300

TITLE: Enhancing Sparse Event Detection in Healthcare Time-Series via Adaptive Gate of Context–Detail Interaction

ABSTRACT: Accurate detection of clinically meaningful events in healthcare time-series data is crucial for reliable downstream analysis and decision support. However, most existing methods struggle to jointly localize event boundaries and classify event types; even detection transformer (DETR)-based approaches show limited performance when confronted with extremely sparse events typical of clinical recordings. To address these challenges, we propose a coarse-to-fine detection framework combining a global context explorer, a local detail inspector, and an adaptive gating module (AGM) that fuses multiple label perspectives. The AGM uses transformed labels—encoding event presence and temporal position—to improve learning on sparse events. This design acts as a switch that selectively activates detailed feature extraction only when an event is likely, thereby reducing noise and improving efficiency in sparse settings. We evaluate our framework on diverse healthcare datasets—including arrhythmia detection, emotion recognition, and human-activity monitoring—and demonstrate substantial performance gains over existing DETR-based models, with particularly strong improvements in sparse event detection. With precise and robust event detection, our framework enables interpretation and actionable insights in real-world clinical applications.
