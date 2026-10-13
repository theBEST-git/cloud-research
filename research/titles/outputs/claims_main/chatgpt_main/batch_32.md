# Batch 32 — 100 items

## item_id: m_3101

TITLE: Complex Query Answering with Neural Link Predictors

ABSTRACT: Neural link predictors are immensely useful for identifying missing edges in large scale Knowledge Graphs. However, it is still not clear how to use these models for answering more complex queries that arise in a number of domains, such as queries using logical conjunctions ($\land$), disjunctions ($\lor$) and existential quantifiers ($\exists$), while accounting for missing edges. In this work, we propose a framework for efficiently answering complex queries on incomplete Knowledge Graphs. We translate each query into an end-to-end differentiable objective, where the truth value of each atom is computed by a pre-trained neural link predictor. We then analyse two solutions to the optimisation problem, including gradient-based and combinatorial search. In our experiments, the proposed approach produces more accurate results than state-of-the-art methods --- black-box neural models trained on millions of generated queries --- without the need of training on a large and diverse set of complex queries. Using orders of magnitude less training data, we obtain relative improvements ranging from 8% up to 40% in Hits@3 across different knowledge graphs containing factual information. Finally, we demonstrate that it is possible to explain the outcome of our model in terms of the intermediate solutions identified for each of the complex query atoms. All our source code and datasets are available online, at https://github.com/uclnlp/cqd.

## item_id: m_3102

TITLE: Online Bayesian Transfer Learning for Sequential Data Modeling

ABSTRACT: We consider the problem of inferring a sequence of hidden states associated with a sequence of observations produced by an individual within a population.  Instead of learning a single sequence model for the population (which does not account for variations within the population), we learn a set of basis sequence models based on different individuals.  The sequence of hidden states for a new individual is inferred in an online fashion by estimating a distribution over the basis models that best explain the sequence of observations of this new individual.  We explain how to do this in the context of hidden Markov models with Gaussian mixture models that are learned based on streaming data by online Bayesian moment matching.  The resulting transfer learning technique is demonstrated with three real-word applications: activity recognition based on smartphone sensors, sleep classification based on electroencephalography data and the prediction of the direction of future packet flows between a pair of servers in telecommunication networks. 

## item_id: m_3103

TITLE: Shift Aggregate Extract Networks

ABSTRACT: The Shift Aggregate Extract Network SAEN is an architecture for learning representations on social network data.
SAEN decomposes input graphs into hierarchies made of multiple strata of objects.
Vector representations of each object are learnt by applying 'shift', 'aggregate' and 'extract' operations on the vector representations of its parts.
We propose an algorithm for domain compression which takes advantage of symmetries in hierarchical decompositions to reduce the memory usage and obtain significant speedups.
Our method is empirically evaluated on real world social network datasets, outperforming the current state of the art.

## item_id: m_3104

TITLE: To Simulate Neural Organoid: A Framework and A Benchmark based on AI

ABSTRACT: Neural organoids hold significant value for AI modeling, cognitive exploration, and medical discovery in academic research.
However, the current research on neural organoids primarily relies on trial-and-error experimental design methods that are time-consuming and expensive.
Moreover, due to the intrinsic unknowability of complex biological systems, purely rational deduction through mathematical and physical modeling is nearly impossible.
As a result, the design of organoid experiments is constrained by the above limitations. 
With AI models being applied to address diverse biological challenges, the demand for novel experimental paths for neural organoids has become urgent.
In response to the above issues, we propose the first neural organoid simulation framework to realistically reconstruct various details of interaction experiments using real mature organoids. 
This framework employs advanced neural computing models as elements, harnessing AI methods to enable stimulation, response, and learning functionalities.
The significant consumption can be mitigated through the combination of the framework with real experiments.
An intelligent expansion platform is also established based on spiking neural network to facilitate the exploration of organoid-machine collaborative intelligence.
In addition, we introduce a benchmark for evaluating our framework, including a set of real organoid experimental data and a series of evaluation metrics.
The experimental results show that our simulation framework features outstanding simulation capabilities and reflects similarity with real organoid experiments in many aspects.
With the intelligent expansion platform, the performance of the combination is comparable to pure AI algorithms in a basic classification task.

## item_id: m_3105

TITLE: Malign Overfitting: Interpolation and Invariance are Fundamentally at Odds

ABSTRACT: Learned classifiers should often possess certain invariance properties meant to encourage fairness, robustness, or out-of-distribution generalization. 
However, multiple recent works empirically demonstrate that common invariance-inducing regularizers are ineffective in the over-parameterized regime, in which classifiers perfectly fit (i.e. interpolate) the training data. This suggests that the phenomenon of ``benign overfitting," in which models generalize well despite interpolating, might not favorably extend to settings in which robustness or fairness are desirable. 

In this work, we provide a theoretical justification for these observations. We prove that---even in the simplest of settings---any interpolating learning rule (with an arbitrarily small margin) will not satisfy these invariance properties. We then propose and analyze an algorithm that---in the same setting---successfully learns a non-interpolating classifier that is provably invariant. We validate our theoretical observations on simulated data and the Waterbirds dataset.

## item_id: m_3106

TITLE: Dealing with Non-Stationarity in MARL via Trust-Region Decomposition

ABSTRACT: Non-stationarity is one thorny issue in cooperative multi-agent reinforcement learning (MARL). One of the reasons is the policy changes of agents during the learning process. Some existing works have discussed various consequences caused by non-stationarity with several kinds of measurement indicators. This makes the objectives or goals of existing algorithms are inevitably inconsistent and disparate. In this paper, we introduce a novel notion, the $\delta$-$stationarity$ measurement, to explicitly measure the non-stationarity of a policy sequence, which can be further proved to be bounded by the KL-divergence of consecutive joint policies. A straightforward but highly non-trivial way is to control the joint policies' divergence, which is difficult to estimate accurately by imposing the trust-region constraint on the joint policy. Although it has lower computational complexity to decompose the joint policy and impose trust-region constraints on the factorized policies, simple policy factorization like mean-field approximation will lead to more considerable policy divergence, which can be considered as the trust-region decomposition dilemma. We model the joint policy as a pairwise Markov random field and propose a trust-region decomposition network (TRD-Net) based on message passing to estimate the joint policy divergence more accurately. The Multi-Agent Mirror descent policy algorithm with Trust region decomposition, called MAMT, is established by adjusting the trust-region of the local policies adaptively in an end-to-end manner. MAMT can approximately constrain the consecutive joint policies' divergence to satisfy $\delta$-stationarity and alleviate the non-stationarity problem. Our method can bring noticeable and stable performance improvement compared with baselines in cooperative tasks of different complexity.

## item_id: m_3107

TITLE: ViT Fine-tuning Vulnerability to Label Noise

ABSTRACT: Automatic annotation of large-scale datasets often introduces noisy labels, which degrade the performance of deep neural networks. Noisy Label Learning (NLL) has been well-studied for Convolutional Neural Networks (CNNs) however, its effectiveness for Vision Transformers (ViTs) remains less explored. In this work, namely \texttt{NLL-ViT}, we comprehensively benchmark the robustness of ViTs under diverse label noise settings, and also recommend an entropy based regularization to improve ViT performance.
To this end, we address many key research questions including vulnerability of ViT to noisy labels,  robustness of ViT relative to CNNs, effectiveness of existing NLL methods for ViT,  correlation of prediction entropy reduction and ViT robustness, and the impact of recommended entropy regularization on robustness. In this study, we conducted more than 850 experiments, evaluating ViT-B/16 and ViT-L/16 fine-tuned via MLP-K on two standard loss functions and ten state-of-the-art NLL methods. Our benchmark spans three noise types including closed-set, open-set, and real-world, across eight datasets: CIFAR-10, CIFAR-100, CIFAR-10N, CIFAR-100N, CIFAR80-O, WebVision, Clothing1M, and Food-101N.
Our findings show that ViT fine-tuning is vulnerable to noisy labels, ViTs fine-tuning is more robust to label noise compared to CNNs, existing CNN-based NLL methods are only effective in closed-set settings while failing to outperform standard losses under open-set and real-world noise settings. We also observe a strong correlation between prediction entropy reduction and ViT robustness. Also, the recommended entropy regularization combined with standard classification losses significantly enhances ViTs' robustness to noisy labels. We will release the \texttt{NLL-ViT} code publicly upon acceptance.

## item_id: m_3108

TITLE: Fast and Noise-Robust Diffusion Solvers for Inverse Problems: A Frequentist Approach

ABSTRACT: Diffusion models have been firmly established as principled zero-shot solvers for linear and nonlinear inverse problems, owing to their powerful image prior and ease of formulation as Bayesian posterior samplers. However, many existing solvers struggle in the noisy measurement regime, either overfitting or underfitting to the measurement constraint, resulting in poor sample quality and inconsistent performance across noise levels. Moreover, existing solvers rely on approximating $x_0$ via Tweedie's formula, where an intractable \textit{conditional} score is replaced by an \textit{unconditional} score network, introducing a fundamental source of error in the resulting solution. In this work, we propose a novel frequentist's approach to diffusion-based inverse solvers, where each diffusion step can be seen as the maximum likelihood solution to a simple single-parameter conditional likelihood model, derived by an adjusted application of Tweedie's formula to the forward measurement model. We demonstrate that this perspective is not only scalable and fast, but also allows for a noise-aware maximization scheme with a likelihood-based stopping criterion that promotes the proper noise-adapted fit given knowledge of the measurement noise $\sigma_\mathbf{y}$. Finally, we demonstrate comparable or improved performance against a wide selection of contemporary inverse solvers across multiple datasets, tasks, and noise levels.

## item_id: m_3109

TITLE: Efficient, Stable, and Analytic Differentiation of the Sinkhorn Loss

ABSTRACT: Optimal transport and the Wasserstein distance have become indispensable building blocks of modern deep generative models, but their computional costs greatly prohibit their applications in statistical machine learning models. Recently, the Sinkhorn loss, as an approximation to the Wasserstein distance, has gained massive popularity, and much work has been done for its theoretical properties. To embed the Sinkhorn loss into gradient-based learning frameworks, efficient algorithms for both the forward and backward passes of the Sinkhorn loss are required. In this article, we first demonstrate issues of the widely-used Sinkhorn's algorithm, and show that the L-BFGS algorithm is a potentially better candidate for the forward pass. Then we derive an analytic form of the derivative of the Sinkhorn loss with respect to the input cost matrix, which results in a very efficient backward algorithm. We rigorously analyze the convergence and stability properties of the advocated algorithms, and use various numerical experiments to validate the superior performance of the proposed methods.

## item_id: m_3110

TITLE: LINGOLY-TOO: Disentangling Reasoning from Knowledge with Templatised Orthographic Obfuscation

ABSTRACT: Frontier language models demonstrate increasing ability at solving reasoning
problems, but their performance is often inflated by circumventing reasoning and
instead relying on their expanding knowledge and memorisation capacity. We
introduce LINGOLY-TOO, a challenging reasoning benchmark of 1,203 questions
and a total of 6,995 sub-questions that counters these shortcuts by applying expert-
designed obfuscations to Linguistics Olympiad problems. These obfuscations
preserve the underlying solution logic while reducing the likelihood problems
are solvable with via knowledge or memorisation. Our experiments show that
models exploit shortcuts on the original question as performance markedly drop
upon obfuscation. Even the best reasoning models remain highly sensitive, with
scores dropping from around 0.59 on original problems to 0.48 after obfuscation.
LINGOLY-TOO disentangles reasoning from knowledge, offering a clearer measure
of true reasoning capabilities.

## item_id: m_3111

TITLE: EXPLORING NEURAL ARCHITECTURE SEARCH FOR LANGUAGE TASKS

ABSTRACT: Neural architecture search (NAS), the task of finding neural architectures automatically, has recently emerged as a promising approach for unveiling better models over human-designed ones. However, most success stories are for vision tasks and have been quite limited for text, except for a small language modeling setup. In this paper, we explore NAS for text sequences at scale, by first focusing on the task of language translation and later extending to reading comprehension. From a standard sequence-to-sequence models for translation, we conduct extensive searches over the recurrent cells and attention similarity functions across two translation tasks, IWSLT English-Vietnamese and WMT German-English. We report challenges in performing cell searches as well as demonstrate initial success on attention searches with translation improvements over strong baselines. In addition, we show that results on attention searches are transferable to reading comprehension on the SQuAD dataset.

## item_id: m_3112

TITLE: Real-time Neural-based Input Method

ABSTRACT: The input method is an essential service on every mobile and desktop devices that provides text suggestions. It converts sequential keyboard inputs to the characters in its target language, which is indispensable for Japanese and Chinese users. Due to critical resource constraints and limited network bandwidth of the target devices, applying neural models to input method is not well explored. In this work, we apply a LSTM-based language model to input method and evaluate its performance for both prediction and conversion tasks with Japanese BCCWJ corpus. We articulate the bottleneck to be the slow softmax computation during conversion. To solve the issue, we propose incremental softmax approximation approach, which computes softmax with a selected subset vocabulary and fix the stale probabilities when the vocabulary is updated in future steps. We refer to this method as incremental selective softmax. The results show a two order speedup for the softmax computation when converting Japanese input sequences with a large vocabulary, reaching real-time speed on commodity CPU. We also exploit the model compressing potential to achieve a 92% model size reduction without losing accuracy.

## item_id: m_3113

TITLE: Automatic Portrait Video Matting via Context Motion Network

ABSTRACT: Automatic portrait video matting is an under-constrained problem. Most state-of-the-art methods only exploit the semantic information and process each frame individually. Their performance is compromised due to the lack of temporal information between the frames. To solve this problem, we explore the optical flow between video frames for the automatic portrait video matting. Specifically, we propose the context motion network to leverage semantic information and motion information. To capture the motion information, we estimate the optical flow and design a context-motion updating operator to integrate features between frames recurrently. Our experiments show that our network outperforms state-of-the-art matting methods significantly on the Video240K SD dataset.

## item_id: m_3114

TITLE: Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions

ABSTRACT: In order to understand the in-context learning phenomenon, recent works have adopted a stylized experimental framework and demonstrated that Transformers can match the performance of gradient-based learning algorithms for various classes of real-valued functions. However, the limitations of Transformers in implementing learning algorithms, and their ability to learn other forms of algorithms are not well understood. Additionally, the degree to which these capabilities are confined to attention-based models is unclear. Furthermore, it remains to be seen whether the insights derived from these stylized settings can be extrapolated to pretrained Large Language Models (LLMs). In this work, we take a step towards answering these questions by demonstrating the following: (a) On a test-bed with a variety of Boolean function classes, we find that Transformers can nearly match the optimal learning algorithm for 'simpler' tasks, while their performance deteriorates on more 'complex' tasks. Additionally, we find that certain attention-free models perform (almost) identically to Transformers on a range of tasks. (b) When provided a *teaching sequence*, i.e. a set of examples that uniquely identifies a function in a class, we show that Transformers learn more sample-efficiently. Interestingly, our results show that Transformers can learn to implement *two distinct* algorithms to solve a *single* task, and can adaptively select the more sample-efficient algorithm depending on the sequence of in-context examples. (c) Lastly, we show that extant LLMs, e.g. LLaMA-2, GPT-4, can compete with nearest-neighbor baselines on prediction tasks that are guaranteed to not be in their training set.

## item_id: m_3115

TITLE: ANOCE: Analysis of Causal Effects with Multiple Mediators via Constrained Structural Learning

ABSTRACT: In the era of causal revolution, identifying the causal effect of an exposure on the outcome of interest is an important problem in many areas, such as epidemics, medicine, genetics, and economics. Under a general causal graph, the exposure may have a direct effect on the outcome and also an indirect effect regulated by a set of mediators. An analysis of causal effects that interprets the causal mechanism contributed through mediators is hence challenging but on demand. To the best of our knowledge, there are no feasible algorithms that give an exact decomposition of the indirect effect on the level of individual mediators, due to common interaction among mediators in the complex graph. In this paper, we establish a new statistical framework to comprehensively characterize causal effects with multiple mediators, namely, ANalysis Of Causal Effects (ANOCE), with a newly introduced definition of the mediator effect, under the linear structure equation model. We further propose a constrained causal structure learning method by incorporating a novel identification constraint that specifies the temporal causal relationship of variables. The proposed algorithm is applied to investigate the causal effects of 2020 Hubei lockdowns on reducing the spread of the coronavirus in Chinese major cities out of Hubei. 

## item_id: m_3116

TITLE: AD-VAT: An Asymmetric Dueling mechanism for learning Visual Active Tracking

ABSTRACT: Visual Active Tracking (VAT) aims at following a target object by autonomously controlling the motion system of a tracker given visual observations. Previous work has shown that the tracker can be trained in a simulator via reinforcement learning and deployed in real-world scenarios. However, during training, such a method requires manually specifying the moving path of the target object to be tracked, which cannot ensure the tracker’s generalization on the unseen object moving patterns. To learn a robust tracker for VAT, in this paper, we propose a novel adversarial RL method which adopts an Asymmetric Dueling mechanism, referred to as AD-VAT. In AD-VAT, both the tracker and the target are approximated by end-to-end neural networks, and are trained via RL in a dueling/competitive manner: i.e., the tracker intends to lockup the target, while the target tries to escape from the tracker. They are asymmetric in that the target is aware of the tracker, but not vice versa. Specifically, besides its own observation, the target is fed with the tracker’s observation and action, and learns to predict the tracker’s reward as an auxiliary task. We show that such an asymmetric dueling mechanism produces a stronger target, which in turn induces a more robust tracker. To stabilize the training, we also propose a novel partial zero-sum reward for the tracker/target. The experimental results, in both 2D and 3D environments, demonstrate that the proposed method leads to a faster convergence in training and yields more robust tracking behaviors in different testing scenarios. For supplementary videos, see: https://www.youtube.com/playlist?list=PL9rZj4Mea7wOZkdajK1TsprRg8iUf51BS 
 The code is available at https://github.com/zfw1226/active_tracking_rl

## item_id: m_3117

TITLE: Noisy Machines: Understanding noisy neural networks and enhancing robustness to analog hardware errors using distillation

ABSTRACT: The success of deep learning has brought forth a wave of interest in computer hardware design to better meet the high demands of neural network inference. In particular, analog computing hardware has been heavily motivated specifically for accelerating neural networks, based on either electronic, optical or photonic devices, which may well achieve lower power consumption than conventional digital electronics. However, these proposed analog accelerators suffer from the intrinsic noise generated by their physical components, which makes it challenging to achieve high accuracy on deep neural networks. Hence, for successful deployment on analog accelerators, it is essential to be able to train deep neural networks to be robust to random continuous noise in the network weights, which is a somewhat new challenge in machine learning. In this paper, we advance the understanding of noisy neural networks. We outline how a noisy neural network has reduced learning capacity as a result of loss of mutual information between its input and output. To combat this, we propose using knowledge distillation combined with noise injection during training to achieve more noise robust networks, which is demonstrated experimentally across different networks and datasets, including ImageNet. Our method achieves models with as much as 2X greater noise tolerance compared with the previous best attempts, which is a significant step towards making analog hardware practical for deep learning.

## item_id: m_3118

TITLE: Neural Thompson Sampling

ABSTRACT: Thompson Sampling (TS) is one of the most effective algorithms for solving contextual multi-armed bandit problems. In this paper, we propose a new algorithm, called Neural Thompson Sampling, which adapts deep neural networks for both exploration and exploitation. At the core of our algorithm is a novel posterior distribution of the reward, where its mean is the neural network approximator, and its variance is built upon the neural tangent features of the corresponding neural network. We prove that, provided the underlying reward function is bounded, the proposed algorithm is guaranteed to achieve a cumulative regret of $O(T^{1/2})$, which matches the regret of other contextual bandit algorithms in terms of total round number $T$. Experimental comparisons with other benchmark bandit algorithms on various data sets corroborate our theory.

## item_id: m_3119

TITLE: Remember, Retrieve and Generate: Understanding Infinite Visual Concepts as Your Personalized Assistant

ABSTRACT: The development of large language models (LLMs) has significantly enhanced the capabilities of multimodal LLMs (MLLMs) as general assistants. However, lack of user-specific knowledge still restricts their application in human's daily life. In this paper, we introduce the **R**etrieval **A**ugmented **P**ersonalization (RAP) framework for MLLMs' personalization. Starting from a general MLLM, we turn it into a personalized assistant in three steps. (a) Remember: We design a key-value database to store user-related information, *e.g.*, user's name, avatar and other attributes. (b) Retrieve: When the user initiates a conversation, RAP will retrieve relevant information from the database using a multimodal retriever. (c) Generate: The input query and retrieved concepts' information are fed into MLLMs to generate personalized, knowledge-augmented responses. Unlike previous methods, RAP allows real-time concept editing via updating the external database. To further improve generation quality and alignment with user-specific information, we design a pipeline for data collection and create a specialized dataset for personalized training of MLLMs. Based on the dataset, we train a series of MLLMs as personalized multimodal assistants. By pretraining on large-scale dataset, RAP-MLLMs can generalize to infinite visual concepts without additional finetuning. Our models demonstrate outstanding flexibility and generation quality across a variety of tasks, such as personalized image captioning, question answering and visual recognition. The code, data and models will be available.

## item_id: m_3120

TITLE: Offline Robustness of Distributional Actor-Critic Ensemble Reinforcement Learning

ABSTRACT: Offline reinforcement learning (RL) focuses on learning policies using static datasets without further exploration. With the introduction of distributional reinforcement learning into offline RL, current methods excel at quantifying the risk and ensuring the security of learned policies. However, these algorithms can not effectively balance the distribution shift and robustness, and even a minor perturbation in observations can significantly impair policy performance. In this paper, we propose Offline Robustness of Distributional actor-critic Ensemble Reinforcement Learning (ORDER) to improve the robustness of policies. In ORDER, we introduce two approaches to enhance the robustness: i) introduce the smoothing technique to policies and distribution functions for states near the dataset; ii) strengthen the quantile network. In addition to improving the robustness, we also theoretically prove that ORDER converges to a conservative lower bound, which can alleviate the distribution shift. In our experiments, we validate the effectiveness of ORDER in the D4RL benchmark through comparative experiments and ablation studies.

## item_id: m_3121

TITLE: A Comparison of Hamming Errors of Representative Variable Selection Methods

ABSTRACT: Lasso is a celebrated method for variable selection in linear models, but it faces challenges when the covariates are moderately or strongly correlated. This motivates alternative approaches such as using a non-convex penalty, adding a ridge regularization, or conducting a post-Lasso thresholding. In this paper, we compare Lasso with 5 other methods: Elastic net, SCAD, forward selection, thresholded Lasso, and forward backward selection. We measure their performances theoretically by the expected Hamming error, assuming that the regression coefficients are ${\it iid}$ drawn from a two-point mixture and that the Gram matrix is block-wise diagonal. By deriving the rates of convergence of Hamming errors and the phase diagrams, we obtain useful conclusions about the pros and cons of different methods.

## item_id: m_3122

TITLE: Counterpoint by Convolution

ABSTRACT: Machine learning models of music typically break down the task of composition into a chronological process, composing a piece of music in a single pass from beginning to end. On the contrary, human composers write music in a nonlinear fashion, scribbling motifs here and there, often revisiting choices previously made. We explore the use of blocked Gibbs sampling as an analogue to the human approach, and introduce Coconet, a convolutional neural network in the NADE family of generative models. Despite ostensibly sampling from the same distribution as the NADE ancestral sampling procedure, we find that a blocked Gibbs approach significantly improves sample quality. We provide evidence that this is due to some conditional distributions being poorly modeled. Moreover, we show that even the cheap approximate blocked Gibbs procedure from Yao et al. (2014) yields better samples than ancestral sampling. We demonstrate the versatility of our method on unconditioned polyphonic music generation.

## item_id: m_3123

TITLE: A NEW POINTWISE CONVOLUTION IN DEEP NEURAL NETWORKS THROUGH EXTREMELY FAST AND NON PARAMETRIC TRANSFORMS

ABSTRACT:     Some conventional transforms such as Discrete Walsh-Hadamard Transform (DWHT) and Discrete Cosine Transform (DCT) have been widely used as feature extractors in image processing but rarely applied in neural networks. However, we found that these conventional transforms have the ability to capture the cross-channel correlations without any learnable parameters in DNNs. This paper firstly proposes to apply conventional transforms on pointwise convolution, showing that such transforms significantly reduce the computational complexity of neural networks without accuracy performance degradation. Especially for DWHT, it requires no floating point multiplications but only additions and subtractions, which can considerably reduce computation overheads. In addition, its fast algorithm further reduces complexity of floating point addition from O(n^2) to O(nlog n). These non-parametric and low computational properties construct extremely efficient networks in the number parameters and operations, enjoying accuracy gain. Our proposed DWHT-based model gained 1.49% accuracy increase with 79.4% reduced parameters and 48.4% reduced FLOPs compared with its baseline model (MoblieNet-V1) on the CIFAR 100 dataset.

## item_id: m_3124

TITLE: On Learning Heteroscedastic Noise Models within Differentiable Bayes Filters

ABSTRACT: In many robotic applications, it is crucial to maintain a belief about the state of 
a system, like the location of a robot or the pose of an object.
These state estimates serve as input for planning and decision making and 
provide feedback during task execution. 
Recursive Bayesian Filtering algorithms address the state estimation problem,
but they require a model of the process dynamics and the sensory observations as well as 
noise estimates that quantify the accuracy of these models. 
Recently, multiple works have demonstrated that the process and sensor models can be 
learned by end-to-end training through differentiable versions of Recursive Filtering methods.
However, even if the predictive models are known, finding suitable noise models 
remains challenging. Therefore, many practical applications rely on very simplistic noise 
models. 
Our hypothesis is that end-to-end training through differentiable Bayesian 
Filters enables us to learn more complex heteroscedastic noise models for
the system dynamics. We evaluate learning such models with different types of 
filtering algorithms and on two different robotic tasks. Our experiments show that especially 
for sampling-based filters like the Particle Filter, learning heteroscedastic noise 
models can drastically improve the tracking performance in comparison to using 
constant noise models.

## item_id: m_3125

TITLE: Optimal Transport-Induced Samples against Out-of-Distribution Overconfidence

ABSTRACT: Deep neural networks (DNNs) often produce overconfident predictions on out-of-distribution (OOD) inputs, undermining their reliability in open-world environments. Singularities in semi-discrete optimal transport (OT) mark regions of semantic ambiguity, where classifiers are particularly prone to unwarranted high-confidence predictions. Motivated by this observation, we propose a principled framework to mitigate OOD overconfidence by leveraging the geometry of OT-induced singular boundaries. Specifically, we formulate an OT problem between a continuous base distribution and the latent embeddings of training data, and identify the resulting singular boundaries. By sampling near these boundaries, we construct a class of OOD inputs, termed optimal transport-induced OOD samples (OTIS), which are geometrically grounded and inherently semantically ambiguous. During training, a confidence suppression loss is applied to OTIS to guide the model toward more calibrated predictions in structurally uncertain regions. Extensive experiments show that our method significantly alleviates OOD overconfidence and outperforms state-of-the-art methods.

## item_id: m_3126

TITLE: Predicting Auction Price of Vehicle License Plate with Deep Recurrent Neural Network

ABSTRACT: In Chinese societies, superstition is of paramount importance, and vehicle license plates with desirable numbers can fetch very high prices in auctions. Unlike other valuable items, license plates are not allocated an estimated price before auction. 

I propose that the task of predicting plate prices can be viewed as a natural language processing (NLP) task, as the value depends on the meaning of each individual character on the plate and its semantics. I construct a deep recurrent neural network (RNN) to predict the prices of vehicle license plates in Hong Kong, based on the characters on a plate. I demonstrate the importance of having a deep network and of retraining. Evaluated on 13 years of historical auction prices, the deep RNN's predictions can explain over 80 percent of price variations, outperforming previous models by a significant margin.  I also demonstrate how the model can be extended to become a search engine for plates and to provide estimates of the expected price distribution.

## item_id: m_3127

TITLE: HyperDynamics: Meta-Learning Object and Agent Dynamics with Hypernetworks

ABSTRACT: We propose HyperDynamics, a dynamics meta-learning framework that conditions on an agent’s interactions with the environment and optionally its visual observations, and generates the parameters of neural dynamics models based on inferred properties of the dynamical system. Physical and visual properties of the environment that are not part of the low-dimensional state yet affect its temporal dynamics are inferred from the interaction history and visual observations, and are implicitly captured in the generated parameters. We test HyperDynamics on a set of object pushing and locomotion tasks. It outperforms existing dynamics models in the literature that adapt to environment variations by learning dynamics over high dimensional visual observations, capturing the interactions of the agent in recurrent state representations, or using gradient-based meta-optimization. We also show our method matches the performance of an ensemble of separately trained experts, while also being able to generalize well to unseen environment variations at test time. We attribute its good performance to the multiplicative interactions between the inferred system properties—captured in the generated parameters—and the low-dimensional state representation of the dynamical system.

## item_id: m_3128

TITLE: HierT2S: Enhancing Part-Level Text-to-Shape Generation via Hierarchical Structure Modeling

ABSTRACT: Text-driven 3D shape generation still faces key challenges, especially in achieving high levels of control over the generated outputs. Paticularly, existing text-to-shape methods ignore the explicit modeling of hierarchical structures in the text and 3D shapes, which makes it hard for using long text descriptions with multiple prompts to guide the coherent part-level 3D shape generation. In this work, we introduce HierT2S, a framework that integrates a hierarchical tree representation with a conditional diffusion model, to enhance the generation of 3D shapes with coherent structures induced by the hierarchical and structured text representations. The key idea is to first segment the input text into several clusters and construct a hierarchical tree representation, with each node representing a parent entity or the fine-level part components. Then, we process the lower-level clusters of the tree with a relation graph module which uses self-attention mechanism to aggregate the relationships of the clusters, and generate a new sequence containing the processed text features. Finally, the text features are embedded into the 3D feature space and used for learning the 3D shape generation by a conditional diffusion model, where the sparsely implicit parsed hierarchical tree graph further enhances the structural details of the generated 3D shapes, leading to results that are close to structure-aware generation. We conducted comprehensive experiments on the existing text-to-shape pairing dataset Text2Shape, and the results demonstrate that our model significantly outperforms current state-of-the-art methods. Moreover, our method can enable progressive part-level 3D shape manipulation and modification guided by the partially modified text prompt.

## item_id: m_3129

TITLE: Second-Moment Loss: A Novel Regression Objective for Improved Uncertainties

ABSTRACT: Quantification of uncertainty is one of the most promising  approaches to establish safe machine learning. Despite its importance, it is far from being generally solved, especially for neural networks. One of the most commonly used approaches so far is Monte Carlo dropout, which is computationally cheap and easy to apply in practice. However, it can underestimate the uncertainty. We propose a new objective, referred to as second-moment loss (SML), to address this issue. While the full network is encouraged to model the mean, the dropout networks are explicitly used to optimize the model variance. We analyze the performance of the new objective on various toy and UCI regression datasets. Comparing to the state-of-the-art of deep ensembles, SML leads to comparable prediction accuracies and uncertainty estimates while only requiring a single model. Under distribution shift, we observe moderate improvements. From a safety perspective also the study of worst-case uncertainties is crucial. In this regard we improve considerably. Finally, we show that SML can be successfully applied to SqueezeDet, a modern object detection network. We improve on its uncertainty-related scores while not deteriorating regression quality. As a side result, we introduce an intuitive Wasserstein distance-based uncertainty measure that is non-saturating and thus allows to resolve quality differences between any two uncertainty estimates.

## item_id: m_3130

TITLE: Recursive Regression with Neural Networks: Approximating the HJI PDE Solution

ABSTRACT: Most machine learning applications using neural networks seek to approximate some function g(x) by minimizing some cost criterion. In the simplest case, if one has access to pairs of the form (x, y) where y = g(x), the problem can be framed as a regression problem. Beyond this family of problems, we find many cases where the unavailability of data pairs makes this approach unfeasible. However, similar to what we find in the reinforcement learning literature, if we have some known properties of the function we are seeking to approximate, there is still hope to frame the problem as a regression problem. In this context, we present an algorithm that approximates the solution to a partial differential equation known as the Hamilton-Jacobi-Isaacs PDE and compare it to current state of the art tools. This PDE, which is found in the fields of control theory and robotics, is of particular importance in safety critical systems where guarantees of performance are a must.

## item_id: m_3131

TITLE: Attention: Self-Expression Is All You Need

ABSTRACT: Transformer models have achieved significant improvements in performance for various learning tasks in natural language processing and computer vision. Much of their success is attributed to the use of attention layers that capture long-range interactions among data tokens (such as words and image patches) via attention coefficients that are global and adapted to the input data at test time. In this paper we study the principles behind attention and its connections with prior art. Specifically, we show that attention builds upon a long history of prior work on manifold learning and image processing, including methods such as kernel-based regression, non-local means, locally linear embedding, subspace clustering and sparse coding. Notably, we show that self-attention is closely related to the notion of self-expressiveness in subspace clustering, wherein data points to be clustered are expressed as linear combinations of other points with global coefficients that are adapted to the data and capture long-range interactions among data points. We also show that heuristics in sparse self-attention can be studied in a more principled manner using prior literature on sparse coding and sparse subspace clustering. We thus conclude that the key innovations of attention mechanisms relative to prior art are the use of many learnable parameters, and multiple heads and layers.

## item_id: m_3132

TITLE: Flow Matching with General Discrete Paths: A Kinetic-Optimal Perspective

ABSTRACT: The design space of discrete-space diffusion or flow generative models are significantly less well-understood than their continuous-space counterparts, with many works focusing only on a simple masked construction.
In this work, we aim to take a holistic approach to the construction of discrete generative models based on continuous-time Markov chains, and for the first time, allow the use of arbitrary discrete probability paths, or colloquially, corruption processes. 
Through the lens of optimizing the symmetric kinetic energy, we propose velocity formulas that can be applied to any given probability path, completely decoupling the probability and velocity, and giving the user the freedom to specify any desirable probability path based on expert knowledge specific to the data domain. 
Furthermore, we find that a special construction of mixture probability paths optimizes the symmetric kinetic energy for the discrete case.
We empirically validate the usefulness of this new design space across multiple modalities: text generation, inorganic material generation, and image generation. We find that we can outperform the mask construction even in text with kinetic-optimal mixture paths, while we can make use of domain-specific constructions of the probability path over the visual domain.

## item_id: m_3133

TITLE: Bi-Stride Multi-Scale Graph Neural Network for Mesh-Based Physical Simulation

ABSTRACT: Learning physical systems on unstructured meshes by flat Graph neural networks (GNNs) faces the challenge of modeling the long-range interactions due to the scaling complexity w.r.t. the number of nodes, limiting the generalization under mesh refinement. On regular grids, the convolutional neural networks (CNNs) with a U-net structure can resolve this challenge by efficient stride, pooling, and upsampling operations. Nonetheless, these tools are much less developed for graph neural networks (GNNs), especially when GNNs are employed for learning large-scale mesh-based physics. The challenges arise from the highly irregular meshes and the lack of effective ways to construct the multi-level structure without losing connectivity. Inspired by the bipartite graph determination algorithm, we introduce Bi-Stride Multi-Scale Graph Neural Network (BSMS-GNN) by proposing \textit{bi-stride} as a simple pooling strategy for building the multi-level GNN. \textit{Bi-stride} pools nodes by striding every other BFS frontier; it 1) works robustly on any challenging mesh in the wild, 2) avoids using a mesh generator at coarser levels, 3) avoids the spatial proximity for building coarser levels, and 4) uses non-parametrized aggregating/returning instead of MLPs during pooling and unpooling. Experiments show that our framework significantly outperforms the state-of-the-art method's computational efficiency in representative physics-based simulation cases.

## item_id: m_3134

TITLE: Pruning Filters for Efficient ConvNets

ABSTRACT: The success of CNNs in various applications is accompanied by a significant increase in the computation and parameter storage costs. Recent efforts toward reducing these overheads involve pruning and compressing the weights of various layers without hurting original accuracy.  However, magnitude-based pruning of weights reduces a significant number of parameters from the fully connected layers and may not adequately reduce the computation costs in the convolutional layers due to irregular sparsity in the pruned networks. We present an acceleration method for CNNs, where we prune filters from CNNs that are identified as having a small effect on the output accuracy. By removing whole filters in the network together with their connecting feature maps, the computation costs are reduced significantly. In contrast to pruning weights, this approach does not result in sparse connectivity patterns. Hence, it does not need the support of sparse convolution libraries and can work with existing efficient BLAS libraries for dense matrix multiplications. We show that even simple filter pruning techniques can reduce inference costs for VGG-16 by up to 34% and ResNet-110 by up to 38% on CIFAR10 while regaining close to the original accuracy by retraining the networks.  

## item_id: m_3135

TITLE: Going Deeper with Lean Point Networks

ABSTRACT: We introduce three generic point cloud processing blocks that improve both accuracy and memory consumption of multiple state-of-the-art networks, thus allowing to design deeper and more accurate networks.

The novel processing blocks that facilitate efficient information flow are a convolution-type operation block for point sets that blends neighborhood information in a memory-efficient manner; a multi-resolution point cloud processing block; and a crosslink block that efficiently shares information across low- and high-resolution processing branches. Combining these blocks, we design significantly wider and deeper architectures.

We extensively evaluate the proposed architectures on multiple point segmentation benchmarks (ShapeNetPart, ScanNet, PartNet) and report systematic improvements in terms of both accuracy and memory consumption by using our generic modules in conjunction with multiple recent architectures (PointNet++, DGCNN, SpiderCNN, PointCNN). We report a 9.7% increase in IoU on the PartNet dataset, which is the most complex, while decreasing memory footprint  by  57%.

## item_id: m_3136

TITLE: Beyond the Pixels: Exploring the Effects of Bit-Level Network and File Corruptions on Video Model Robustness

ABSTRACT: We investigate the robustness of video machine learning models to bit-level network and file corruptions, which can arise from network transmission failures or hardware errors, and explore defenses against such corruptions. We simulate network and file corruptions at multiple corruption levels, and find that bit-level corruptions can cause substantial performance drops on common action recognition and multi-object tracking tasks. We explore two types of defenses against bit-level corruptions: corruption-agnostic and corruption-aware defenses. We find that corruption-agnostic defenses such as adversarial training have limited effectiveness, performing up to 11.3 accuracy points worse than a no-defense baseline. In response, we propose Bit-corruption Augmented Training (BAT), a corruption-aware baseline that exploits knowledge of bit-level corruptions to enforce model invariance to such corruptions. BAT outperforms corruption-agnostic defenses, recovering up to 7.1 accuracy points over a no-defense baseline on highly-corrupted videos while maintaining competitive performance on clean/near-clean data.

## item_id: m_3137

TITLE: Handwritten Amharic Character Recognition System Using Convolutional Neural Networks

ABSTRACT: Amharic language is an official language of the federal government of the Federal Democratic Republic of Ethiopia. Accordingly, there is a bulk of handwritten Amharic documents available in libraries, information centres, museums, and offices. Digitization of these documents enables to harness already available language technologies to local information needs and developments. Converting these documents will have a lot of advantages including (i) to preserve and transfer history of the country (ii) to save storage space (ii) proper handling of documents (iv) enhance retrieval of information through internet and other applications. Handwritten Amharic character recognition system becomes a challenging task due to inconsistency of a writer, variability in writing styles of different writers, relatively large number of characters of the script, high interclass similarity, structural complexity and degradation of documents due to different reasons. In order to recognize handwritten Amharic character a novel method based on deep neural networks is used which has recently shown exceptional performance in various pattern recognition and machine learning applications, but has not been endeavoured for Ethiopic script. The CNN model is trained and tested our database that contains 132,500 datasets of handwritten Amharic characters. Common machine learning methods usually apply a combination of feature extractor and trainable classifier. The use of CNN leads to significant improvements across different machine-learning classification algorithms. Our proposed CNN model is giving an accuracy of 91.83% on training data and 90.47% on validation data.

## item_id: m_3138

TITLE: BAT-Chain: Bayesian-Aware Transport Chain for Topic Hierarchies Discovery

ABSTRACT: Topic modeling has been an important tool for text analysis. Originally, topics discovered by a model are usually assumed to be independent. However, as a semantic representation of a concept, a topic is naturally related to others, which motivates the development of learning hierarchical topic structure. Most existing Bayesian models are designed to learn hierarchical structure, but they need non-trivial posterior inference. Although the recent transport-based topic models bypass the posterior inference, none of them considers deep topic structures. In this paper, we interpret document as its word embeddings and propose a novel Bayesian-aware transport chain to discover multi-level topic structures, where each layer learns a set of topic embeddings and the document hierarchical representations are defined as a series of empirical distributions according to the topic proportions and corresponding topic embeddings. To fit such hierarchies, we develop an upward-downward optimizing strategy under the recent conditional transport theory, where document information is first transported via the upward path, and then its hierarchical representations are refined by the downward path under the Bayesian perspective. Extensive experiments on text corpora show that our approach enjoys superior modeling accuracy and interpretability. Moreover, we also conduct experiments on learning hierarchical visual topics from images, which demonstrate the adaptability and flexibility of our method.

## item_id: m_3139

TITLE: AutoUAD: Hyper-parameter Optimization for Unsupervised Anomaly Detection

ABSTRACT: Unsupervised anomaly detection (UAD) has important applications in diverse fields such as manufacturing industry and medical diagnosis. In the past decades, although numerous insightful and effective UAD methods have been proposed, it remains a huge challenge to tune the hyper-parameters of each method and select the most appropriate method among many candidates for a specific dataset, due to the absence of labeled anomalies in the training phase of UAD methods and the high diversity of real datasets. In this work, we aim to address this challenge, so as to make UAD more practical and reliable. We propose two internal evaluation metrics, relative-top-median and expected-anomaly-gap, and one semi-internal evaluation metric, normalized pseudo discrepancy (NPD), as surrogate functions of the expected model performance on unseen test data. For instance, NPD measures the discrepancy between the anomaly scores of a validation set drawn from the training data and a validation set drawn from an isotropic Gaussian. NPD is simple and hyper-parameter-free and is able to compare different UAD methods, and its effectiveness is theoretically analyzed. We integrate the three metrics with Bayesian optimization to effectively optimize the hyper-parameters of UAD models. Extensive experiments on 38 datasets show the effectiveness of our methods.

## item_id: m_3140

TITLE: Quantum-Inspired Structure-Aware Diffusion for Efficient 3D Molecular Generation

ABSTRACT: The high computational cost of classical diffusion models can limit their use in large-scale 3D molecular generation for drug and material discovery. We introduce $\textbf{S}$tructure-aware $\textbf{Q}$uantum $\textbf{Diff}$usion (SQ-Diff), the first full quantum diffusion model for this task, designed to leverage potential quantum advantages in the Noisy Intermediate-Scale Quantum era. Structural priors (e.g., inter-atomic distances) are encoded into the initial quantum state via a novel state preparation procedure that yields a unified normalization scheme dependent only on the number of atoms. The denoising process is driven by a Quantum U-Net, a fully quantum architecture that combines learnable variational quantum circuits with parameter-free operators. Training is guided by these structural priors enforced through a graph-based objective function to maintain structural consistency. Experimentally, SQ-Diff generates valid and diverse 3D molecules and shows improved performance over existing quantum-based methods. While a gap in generation quality compared to leading classical models remains, our model matches the inference speed of the fastest classical approaches with only a few quantum parameters, setting a new benchmark for pure quantum generative models.

## item_id: m_3141

TITLE: Differentiable Canonical Correlation Analysis

ABSTRACT: Canonical Correlation Analysis (CCA) computes maximally-correlated 
linear projections of two modalities. We propose Differentiable CCA, a 
formulation of CCA that can be cast as a layer within a multi-view 
neural network. Unlike Deep CCA, an earlier extension of CCA to 
nonlinear projections, our formulation enables gradient flow through the 
computation of the CCA projection matrices, and free choice of the final 
optimization target. We show the effectiveness of this approach in 
cross-modality retrieval experiments on two public image-to-text 
datasets, surpassing both Deep CCA and a multi-view network with 
freely-learned projections. We assume that Differentiable CCA could be a 
useful building block for many multi-modality tasks.

## item_id: m_3142

TITLE: LARG2, Language-based Automatic Reward and Goal Generation

ABSTRACT: Robotic tasks currently addressed with reinforcement learning such as locomotion, navigation, and manipulation are challenged with the problem of defining reward functions to maximize and goals to reach. 
Alternative methodologies, like imitation learning, often require labor-intensive human annotations to produce datasets of task descriptions  associated with trajectories.
As a response, this paper introduces "Language-based Automatic Reward and Goal Generation" (LARG), a framework that harnesses code generation capabilities of LLMs to enables the conversion of text-based task descriptions into corresponding reward and goal-generation functions.
We leverages Chain-of-thought mechanisms and the common-sense knowledge embedded in Large Language Models (LLMs) for this purpose.
It is complemented by automatic error discovery and correction mechanisms.
We validate the effectiveness of LARG by conducting extensive experiments in the context of robotic manipulation demonstrating its ability to train and execute without human annotation of any kind.

## item_id: m_3143

TITLE: $\lambda$-SecAgg: Partial Vector Freezing for Lightweight Secure Aggregation in Federated Learning

ABSTRACT: Secure aggregation of user update vectors (e.g. gradients) has become a critical issue in the field of federated learning. Many Secure Aggregation Protocols (SAPs) face exorbitant computation costs, severely constraining their applicability. Given the observation that a considerable portion of SAP's computation burden stems from processing each entry in the private vectors, we propose Partial Vector Freezing (PVF), a portable module for compressing computation costs without introducing additional communication overhead. $\lambda$-SecAgg, which integrates SAP with PVF, "freezes" a substantial portion of the private vector through specific transformations, requiring only $\frac{1}{\lambda}$ of the original vector to participate in SAP. Eventually, users can "thaw" the public sum of the "frozen entries" by the result of SAP. To avoid potential privacy leakage, we devise Disrupting Variables Element for PVF. We demonstrate that PVF can seamlessly integrate with various SAPs and it poses no threat to user privacy in the semi-honest and active adversary settings. We include $7$ baselines, encompassing $5$ distinct types of masking schemes, and explore the acceleration effects of PVF on these SAPs. Empirical investigations indicate that when $\lambda=100$, PVF yields up to $99.5\times$ speedup and up to $32.3\times$ communication reduction.

## item_id: m_3144

TITLE: Distribution Regression Network

ABSTRACT: We introduce our Distribution Regression Network (DRN) which performs regression from input probability distributions to output probability distributions. Compared to existing methods, DRN learns with fewer model parameters and easily extends to multiple input and multiple output distributions. On synthetic and real-world datasets, DRN performs similarly or better than the state-of-the-art. Furthermore, DRN generalizes the conventional multilayer perceptron (MLP). In the framework of MLP, each node encodes a real number, whereas in DRN, each node encodes a probability distribution. 

## item_id: m_3145

TITLE: LatticeGen: A Cooperative Framework Which Hides Generated Text in A Lattice For Privacy-Aware Generation on Cloud

ABSTRACT: In the current user-server interaction paradigm of prompted generation with large language model (LLM) on cloud, the server fully controls the generation process, which leaves zero option for users who want to keep the generated text to themselves. We propose LatticeGen, a cooperative framework in which the server still handles most of computation while the user controls the sampling operation. The key idea is that the true generated sequence is mixed with noise tokens by the user and hidden in a noised lattice. Considering potential attack from a hypothetically malicious server and how the user can defend against it, we propose the repeated beam-search attack and the mixing noise scheme. In our experiments we apply LatticeGen to protect both prompt and generation. It is shown that while the noised lattice degrades generation quality, LatticeGen successfully protects the true generation to a remarkable degree under strong attacks (more than 50\% of the semantic remains hidden as measured by BERTScore).

## item_id: m_3146

TITLE: Learning objects from pixels

ABSTRACT: We show how discrete objects can be learnt in an unsupervised fashion from pixels, and how to perform reinforcement learning using this object representation.

More precisely, we construct a differentiable mapping from an image to a discrete tabular list of objects, where each object consists of a differentiable position, feature vector, and scalar presence value that allows the representation to be learnt using an attention mechanism.

Applying this mapping to Atari games, together with an interaction net-style architecture for calculating quantities from objects, we construct agents that can play Atari games using objects learnt in an unsupervised fashion. During training, many natural objects emerge, such as the ball and paddles in Pong, and the submarine and fish in Seaquest.

This gives the first reinforcement learning agent for Atari with an interpretable object representation, and opens the avenue for agents that can conduct object-based exploration and generalization.

## item_id: m_3147

TITLE: Hierarchical Multiscale Recurrent Neural Networks

ABSTRACT: Learning both hierarchical and temporal representation has been among the long- standing challenges of recurrent neural networks. Multiscale recurrent neural networks have been considered as a promising approach to resolve this issue, yet there has been a lack of empirical evidence showing that this type of models can actually capture the temporal dependencies by discovering the latent hierarchical structure of the sequence. In this paper, we propose a novel multiscale approach, called the hierarchical multiscale recurrent neural network, that can capture the latent hierarchical structure in the sequence by encoding the temporal dependencies with different timescales using a novel update mechanism. We show some evidence that the proposed model can discover underlying hierarchical structure in the sequences without using explicit boundary information. We evaluate our proposed model on character-level language modelling and handwriting sequence generation.

## item_id: m_3148

TITLE: Learning Control by Iterative Inversion

ABSTRACT: We formulate learning for control as an inverse problem - inverting a dynamical system to give the actions which yield desired behavior. The key challenge in this formulation is a distribution shift in the inputs to the function to be inverted - the learning agent can only observe the forward mapping (its actions' consequences) on trajectories that it can execute, yet must learn the inverse mapping for inputs-outputs that correspond to a different, desired behavior. We propose a general recipe for inverse problems with a distribution shift that we term $\textit{iterative inversion}$ - learn the inverse mapping under the current input distribution (policy), then use it on the desired output samples to obtain a new input distribution, and repeat.
As we show, iterative inversion can converge to the desired inverse mapping, but under rather strict conditions on the mapping itself.
We next apply iterative inversion to learn control. Our input is a set of demonstrations of desired behavior, given as video embeddings of trajectories (without actions), and our method iteratively learns to imitate trajectories generated by the current policy, perturbed by random exploration noise. We find that constantly adding the demonstrated trajectory embeddings as input to the policy when generating trajectories to imitate, a-la iterative inversion, we effectively steer the learning towards the desired trajectory distribution. To the best of our knowledge, this is the first exploration of learning control from the viewpoint of inverse problems, and the main advantage of our approach is simplicity - it does not require rewards, and only employs supervised learning, which can be easily scaled to use state-of-the-art trajectory embedding techniques and policy representations. Indeed, with a VQ-VAE embedding, and a transformer-based policy, we demonstrate non-trivial continuous control on several tasks. Further, we report an improved performance on imitating diverse behaviors compared to reward based methods. 

## item_id: m_3149

TITLE: In-Context Learning Learns Label Relationships but Is Not Conventional Learning

ABSTRACT: The predictions of Large Language Models (LLMs) on downstream tasks often improve significantly when including examples of the input–label relationship in the context. However, there is currently no consensus about how this in-context learning (ICL) ability of LLMs works. For example, while Xie et al. (2022) liken ICL to a general-purpose learning algorithm, Min et al. (2022b) argue ICL does not even learn label relationships from in-context examples. In this paper, we provide novel insights into how ICL leverages label information, revealing both capabilities and limitations. To ensure we obtain a comprehensive picture of ICL behavior, we study probabilistic aspects of ICL predictions and thoroughly examine the dynamics of ICL as more examples are provided. Our experiments show that ICL predictions almost always depend on in-context labels and that ICL can learn truly novel tasks in-context. However, we also find that ICL struggles to fully overcome prediction preferences acquired from pre-training data and, further, that ICL does not consider all in-context information equally.

## item_id: m_3150

TITLE: Sigma Delta Quantized Networks

ABSTRACT: Deep neural networks can be obscenely wasteful. When processing video, a convolutional network expends a fixed amount of computation for each frame with no regard to the similarity between neighbouring frames. As a result, it ends up repeatedly doing very similar computations. To put an end to such waste, we introduce Sigma-Delta networks. With each new input, each layer in this network sends a discretized form of its change in activation to the next layer. Thus the amount of computation that the network does scales with the amount of change in the input and layer activations, rather than the size of the network. We introduce an optimization method for converting any pre-trained deep network into an optimally efficient Sigma-Delta network, and show that our algorithm, if run on the appropriate hardware, could cut at least an order of magnitude from the computational cost of processing video data.


## item_id: m_3151

TITLE: Offline Reinforcement Learning with Resource Constrained Online Deployment

ABSTRACT: Offline reinforcement learning is used to train policies in scenarios where real-time access to the environment is expensive or impossible.
As a natural consequence of these harsh conditions, an agent may lack the resources to fully observe the online environment before taking an action. We dub this situation the resource-constrained setting. This leads to situations where the offline dataset (available for training) can contain fully processed features (using powerful language models, image models, complex sensors, etc.) which are not available when actions are actually taken online.
This disconnect leads to an interesting and unexplored problem in offline RL: Is it possible to use a richly processed offline dataset to train a policy which has access to fewer features in the online environment? 
In this work, we introduce and formalize this novel resource-constrained problem setting. We highlight the performance gap between policies trained using the full offline dataset and policies trained using limited features. 
We address this performance gap with a policy transfer algorithm which first trains a teacher agent using the offline dataset where features are fully available, and then transfers this knowledge to a student agent that only uses the resource-constrained features. To better capture the challenge of this setting, we propose a data collection procedure: Resource Constrained-Datasets for RL (RC-D4RL). We evaluate our transfer algorithm on RC-D4RL and the popular D4RL benchmarks and observe consistent improvement over the baseline (TD3+BC without transfer).

## item_id: m_3152

TITLE: Learning to Generate Filters for Convolutional Neural Networks

ABSTRACT: Conventionally, convolutional neural networks (CNNs) process different images with the same set of filters. However, the variations in images pose a challenge to this fashion. In this paper, we propose to generate sample-specific filters for convolutional layers in the forward pass. Since the filters are generated on-the-fly, the model becomes more flexible and can better fit the training data compared to traditional CNNs. In order to obtain sample-specific features, we extract the intermediate feature maps from an autoencoder. As filters are usually high dimensional, we propose to learn a set of coefficients instead of a set of filters. These coefficients are used to linearly combine the base filters from a filter repository to generate the final filters for a CNN. The proposed method is evaluated on MNIST, MTFL and CIFAR10 datasets. Experiment results demonstrate that the classification accuracy of the baseline model can be improved by using the proposed filter generation method.

## item_id: m_3153

TITLE: Equivariant 3D-Conditional Diffusion Models for Molecular Linker Design

ABSTRACT: Fragment-based drug discovery has been an effective paradigm in early-stage drug development. An open challenge in this area is designing linkers between disconnected molecular fragments of interest to obtain chemically-relevant candidate drug molecules. In this work, we propose DiffLinker, an E(3)-equivariant 3D-conditional diffusion model for molecular linker design. Given a set of disconnected fragments, our model places missing atoms in between and designs a molecule incorporating all the initial fragments. Unlike previous approaches that are only able to connect pairs of molecular fragments, our method can link an arbitrary number of fragments. Additionally, the model automatically determines the number of atoms in the linker and its attachment points to the input fragments. We demonstrate that DiffLinker outperforms other methods on the standard datasets generating more diverse and synthetically-accessible molecules. Besides, we experimentally test our method in real-world applications, showing that it can successfully generate valid linkers conditioned on target protein pockets.

## item_id: m_3154

TITLE: Improved Gradient Estimators for Stochastic Discrete Variables

ABSTRACT: In many applications we seek to optimize an expectation with respect to a distribution over discrete variables. Estimating gradients of such objectives with respect to the distribution parameters is a challenging problem. We analyze existing solutions including finite-difference (FD) estimators and continuous relaxation (CR) estimators in terms of bias and variance. We show that the commonly used Gumbel-Softmax estimator is biased and propose a simple method to reduce it. We also derive a simpler piece-wise linear continuous relaxation that also possesses reduced bias. We demonstrate empirically that reduced bias leads to a better performance in variational inference and on binary optimization tasks.

## item_id: m_3155

TITLE: Evaluating Synthetic Activations composed of SAE Latents in GPT-2

ABSTRACT: Sparse Auto-Encoders (SAEs) are commonly employed in mechanistic interpretability to decompose the residual stream into monosemantic SAE latents. Recent work demonstrates that perturbing a model's activations at an early layer results in a step-function-like change in the model's final layer activations. Furthermore, the model's sensitivity to this perturbation differs between model-generated (real) activations and random activations. In our study, we assess model sensitivity in order to compare real activations to synthetic activations composed of SAE latents. Our findings indicate that synthetic activations closely resemble real activations when we control for the sparsity and cosine similarity of the constituent SAE latents. This suggests that real activations cannot be explained by a simple "bag of SAE latents" lacking internal structure, and instead suggests that SAE latents possess significant geometric and statistical properties. Notably, we observe that our synthetic activations exhibit less pronounced activation plateaus compared to those typically surrounding real activations.

## item_id: m_3156

TITLE: b-GAN: Unified Framework of Generative Adversarial Networks

ABSTRACT: Generative adversarial networks (GANs) are successful deep generative models. They are based on a two-player minimax game. However, the objective function derived in the original motivation is changed to obtain stronger gradients when learning the generator. We propose a novel algorithm that repeats density ratio estimation and f-divergence minimization. Our algorithm offers a new unified perspective toward understanding GANs and is able to make use of multiple viewpoints obtained from the density ratio estimation research, e.g. what divergence is stable and relative density ratio is useful. 

## item_id: m_3157

TITLE: Understanding intermediate layers using linear classifier probes

ABSTRACT: Neural network models have a reputation for being black boxes. We propose a new method to better understand the roles and dynamics of the intermediate layers. This has direct consequences on the design of such models and it enables the expert to be able to justify certain heuristics (such as adding auxiliary losses in middle layers). Our method uses linear classifiers, referred to as ``probes'', where a probe can only use the hidden units of a given intermediate layer as discriminating features. Moreover, these probes cannot affect the training phase of a model, and they are generally added after training. They allow the user to visualize the state of the model at multiple steps of training. We demonstrate how this can be used to develop a better intuition about models and to diagnose potential problems.

## item_id: m_3158

TITLE: What is Missing? Explaining Neurons Activated by Absent Concepts

ABSTRACT: Explainable artificial intelligence (XAI) aims to provide human-interpretable insights into the behavior of deep neural networks (DNNs), typically by estimating a simplified causal structure of the model. In existing work, this causal structure often includes relationships where the presence of an input pattern or latent feature is associated with a strong activation of a neuron. For example, attribution methods primarily identify input pixels that contribute most to a prediction, and feature visualization methods reveal inputs that cause high activation of a target neuron – both implicitly assuming that neurons encode the presence of concepts. However, a largely overlooked type of causal relationship is that of encoded absences, where the absence of a concept increases activation, or vice versa, the presence of a concept inhibits activation. In this work, we show that such inhibitory relationships are common and that mainstream XAI methods struggle to reveal them when applied in their standard form. To address this, we propose two extensions to attribution and feature visualization techniques that uncover encoded absences. Across experiments, we show how mainstream XAI methods can be used to reveal and explain encoded absences, how ImageNet models exploit them, and that debiasing can be improved when considering them.

## item_id: m_3159

TITLE: Ensemble Methods as a Defense to Adversarial Perturbations Against Deep Neural Networks

ABSTRACT: Deep learning has become the state of the art approach in many machine learning problems such as classification. It has recently been shown that deep learning is highly vulnerable to adversarial perturbations. Taking the camera systems of self-driving cars as an example, small adversarial perturbations can cause the system to  make errors in important tasks, such as classifying traffic signs or detecting pedestrians. Hence, in order to use deep learning without safety concerns a proper defense strategy is required. We propose to use ensemble methods as a defense strategy against adversarial perturbations. We find that an attack leading one model to misclassify does not imply the same for other networks performing the same task. This makes ensemble methods an attractive defense strategy against adversarial attacks. We empirically show for the MNIST and the CIFAR-10 data sets that ensemble methods not only improve the accuracy of neural networks on test data but also increase their robustness against adversarial perturbations.

## item_id: m_3160

TITLE: Neural Topic Model via Optimal Transport

ABSTRACT: Recently, Neural Topic Models (NTMs) inspired by variational autoencoders have obtained increasingly research interest due to their promising results on text analysis. However, it is usually hard for existing NTMs to achieve good document representation and coherent/diverse topics at the same time. Moreover, they often degrade their performance severely on short documents. The requirement of reparameterisation could also comprise their training quality and model flexibility. To address these shortcomings, we present a new neural topic model via the theory of optimal transport (OT). Specifically, we propose to learn the topic distribution of a document by directly minimising its OT distance to the document's word distributions. Importantly, the cost matrix of the OT distance models the weights between topics and words, which is constructed by the distances between topics and words in an embedding space. Our proposed model can be trained efficiently with a differentiable loss. Extensive experiments show that our framework significantly outperforms the state-of-the-art NTMs on discovering more coherent and diverse topics and deriving better document representations for both regular and short texts.

## item_id: m_3161

TITLE: Certifiably Robust Transformers with 1-Lipschitz Self-Attention

ABSTRACT: Recent works have shown that neural networks with Lipschitz constraints will lead to high adversarial robustness. In this work, we propose the first One-Lipschitz Self-Attention (OLSA) mechanism for Transformer models. In particular, we first orthogonalize all the linear operations in the self-attention mechanism. We then bound the overall Lipschitz constant by aggregating the Lipschitz of each element in the softmax with weighted sum. Based on the proposed self-attention mechanism, we construct an OLSA Transformer to achieve model deterministic certified robustness. We evaluate our model on multiple natural language processing (NLP) tasks and show that it outperforms existing certification on Transformers, especially for models with multiple layers. As an example, for 3-layer Transformers we achieve an ℓ2 deterministic certified robustness radius of 1.733 and 0.979 on the word embedding space for the Yelp and SST dataset, while the existing SOTA certification baseline of the same embedding space can only achieve 0.061 and 0.110. In addition, our certification is significantly more efficient than previous works, since we only need the output logits and Lipschitz constant for certification. We also fine-tune our OLSA Transformer as a downstream classifier of a pre-trained BERT model and show that it achieves significantly higher certified robustness on BERT embedding space compared with previous works (e.g. from 0.071 to 0.368 on the QQP datasets).

## item_id: m_3162

TITLE: When, Why, and Which Pretrained GANs Are Useful?

ABSTRACT: The literature has proposed several methods to finetune pretrained GANs on new datasets, which typically results in higher performance compared to training from scratch, especially in the limited-data regime. However, despite the apparent empirical benefits of GAN pretraining, its inner mechanisms were not analyzed in-depth, and understanding of its role is not entirely clear. Moreover, the essential practical details, e.g., selecting a proper pretrained GAN checkpoint, currently do not have rigorous grounding and are typically determined by trial and error. 

This work aims to dissect the process of GAN finetuning. First, we show that initializing the GAN training process by a pretrained checkpoint primarily affects the model's coverage rather than the fidelity of individual samples. Second, we explicitly describe how pretrained generators and discriminators contribute to the finetuning process and explain the previous evidence on the importance of pretraining both of them. Finally, as an immediate practical benefit of our analysis, we describe a simple recipe to choose an appropriate GAN checkpoint that is the most suitable for finetuning to a particular target task. Importantly, for most of the target tasks, Imagenet-pretrained GAN, despite having poor visual quality, appears to be an excellent starting point for finetuning, resembling the typical pretraining scenario of discriminative computer vision models.

## item_id: m_3163

TITLE: Zero-Shot Non-Autoregressive TTS Beyond Autoregressive Models Using Soft Alignment Generation and Residual Modeling

ABSTRACT: Autoregressive TTS leverages soft alignment generated by the attention mechanism, which provides the decoder with a well-designed context vector. Subsequently, the decoder receives both the semantic representation and the acoustic representation generated at the previous time step. For this reason, autoregressive TTS achieves strong performance. Thus, we propose novel algorithms to bring similar benefits to non-autoregressive TTS. First, we propose a method to distill soft alignments—originally provided by attention in autoregressive models—into a flow matching model trained between mel-spectrograms and text representations. This allows non-autoregressive models to leverage attention-like context vectors without requiring autoregressive decoding. Second, we introduce an invertible encoder, designed based on normalizing flow, to disentangle semantic and residual acoustic representations. The invertible encoder maps the residual information, which is absent in the context vector, closer to a Gaussian distribution. During inference, we can treat the context vector as the semantic representation and Gaussian noise as the acoustic representation. Lastly, to improve zero-shot TTS performance, we propose a prompt-aware lightweight convolution, where the kernel weights are dynamically adjusted for each speech prompt. With the proposed methods, our non-autoregressive TTS model achieves comparable performance to existing autoregressive models.

## item_id: m_3164

TITLE: Adding Gradient Noise Improves Learning for Very Deep Networks

ABSTRACT: Deep feedforward and recurrent networks have achieved impressive results in many perception and language processing applications.  Recently, more complex architectures such as Neural Turing Machines and Memory Networks have been proposed for tasks including question answering and general computation, creating a new set of optimization challenges. In this paper, we explore the low-overhead and easy-to-implement optimization technique of adding annealed Gaussian noise to the gradient, which we find surprisingly effective when training these very deep architectures.  Unlike classical weight noise, gradient noise injection is complementary to advanced stochastic optimization algorithms such as Adam and AdaGrad. The technique not only helps to avoid overfitting, but also can result in lower training loss. We see consistent improvements in performance across an array of complex models, including state-of-the-art deep networks for question answering and algorithm learning. We observe that this optimization strategy allows a fully-connected 20-layer deep network to escape a bad initialization with standard stochastic gradient descent. We encourage further application of this technique to additional modern neural architectures.

## item_id: m_3165

TITLE: Rotation Plane Doubly Orthogonal Recurrent Neural Networks

ABSTRACT: Recurrent Neural Networks (RNNs) applied to long sequences suffer from the well known vanishing and exploding gradients problem.  The recently proposed Unitary Evolution Recurrent Neural Network (uRNN) alleviates the exploding gradient problem and can learn very long dependencies, but its nonlinearities make it still affected by the vanishing gradient problem and so learning can break down for extremely long dependencies. We propose a new RNN transition architecture where the hidden state is updated multiplicatively by a time invariant orthogonal transformation followed by an input modulated orthogonal transformation. There are no additive interactions and so our architecture exactly preserves forward hid-den state activation norm and backwards gradient norm for all time steps, and is provably not affected by vanishing or exploding gradients.  We propose using the rotation plane parameterization to represent the orthogonal matrices. We validate our model on a simplified memory copy task and see that our model can learn dependencies as long as 5,000 timesteps.

## item_id: m_3166

TITLE: Learning to Model Editing Processes

ABSTRACT: Most existing sequence generation models produce outputs in one pass, usually left-to-right. However, this is in contrast with a more natural approach that humans use in generating content; iterative refinement and editing. Recent work has introduced edit-based models for various tasks (such as neural machine translation and text style transfer), but these generally model a single edit. In this work, we propose to model editing processes, modeling the whole process of iteratively generating sequences. We form a conceptual framework to describe the likelihood of multi-step edits, and describe neural models that can learn a generative model of sequences based on these multi-step edits. We introduce baseline results and metrics on this task, finding that modeling editing processes improves performance on a variety of axes on both our proposed task and related downstream tasks compared to previous single-step models of edits.

## item_id: m_3167

TITLE: Coupled Ensembles of Neural Networks

ABSTRACT: We investigate in this paper the architecture of deep convolutional networks. Building on existing state of the art models, we propose a reconfiguration of the model parameters into several parallel branches at the global network level, with each branch being a standalone CNN. We show that this arrangement is an efficient way to significantly reduce the number of parameters while at the same time improving the performance. The use of branches brings an additional form of regularization. In addition to splitting the parameters into parallel branches, we propose a tighter coupling of these branches by averaging their log-probabilities. The tighter coupling favours the learning of better representations, even at the level of the individual branches, as compared to when each branch is trained independently. We refer to this branched architecture as "coupled ensembles". The approach is very generic and can be applied with almost any neural network architecture. With coupled ensembles of DenseNet-BC and parameter budget of 25M, we obtain error rates of 2.92%, 15.68% and 1.50% respectively on CIFAR-10, CIFAR-100 and SVHN tasks. For the same parameter budget, DenseNet-BC has an error rate of 3.46%, 17.18%, and 1.8% respectively.  With ensembles of coupled ensembles, of DenseNet-BC networks, with 50M total parameters, we obtain error rates of 2.72%, 15.13% and 1.42% respectively on these tasks.

## item_id: m_3168

TITLE: Training GANs with Optimism

ABSTRACT: We address the issue of limit cycling behavior in training Generative Adversarial Networks and propose the use of Optimistic Mirror Decent (OMD) for training Wasserstein GANs. Recent theoretical results have shown that optimistic mirror decent (OMD) can enjoy faster regret rates in the context of zero-sum games. WGANs is exactly a context of solving a zero-sum game with simultaneous no-regret dynamics.  Moreover, we show that optimistic mirror decent addresses the limit cycling problem in training WGANs. We formally show that in the case of bi-linear zero-sum games the last iterate of OMD dynamics converges to an equilibrium, in contrast to GD dynamics which are bound to cycle. We also portray the huge qualitative difference between GD and OMD dynamics with toy examples, even when GD is modified with many adaptations proposed in the recent literature, such as gradient penalty or momentum. We apply OMD WGAN training to a bioinformatics problem of generating DNA sequences. We observe that models trained with OMD achieve consistently smaller KL divergence with respect to the true underlying distribution, than models trained with GD variants. Finally, we introduce a new algorithm, Optimistic Adam, which is an optimistic variant of Adam. We apply it to WGAN training on CIFAR10 and observe improved performance in terms of inception score as compared to Adam.

## item_id: m_3169

TITLE: Minimizing Change in Classifier Likelihood to Mitigate Catastrophic Forgetting

ABSTRACT: Continual learning is a longstanding goal of artificial intelligence, but is often counfounded by catastrophic forgetting that prevents neural networks from learning tasks sequentially. Previous methods in continual learning have demonstrated how to mitigate catastrophic forgetting, and learn new tasks while retaining performance on the previous tasks. We analyze catastrophic forgetting from the perspective of change in classifier likelihood and propose a simple L1 minimization criterion which can be adapted to different use cases. We further investigate two ways to minimize forgetting as quantified by this criterion and propose strategies to achieve finer control over forgetting. Finally, we evaluate our strategies on 3 datasets of varying difficulty and demonstrate improvements over previously known L2 strategies for mitigating catastrophic forgetting.

## item_id: m_3170

TITLE: InfoNet: Missing Information Retrieval in Multi-Stream Sensing Systems

ABSTRACT: Faulty sensors in a multiple input stream setup are more prone to corrupted input data streams, hindering the performance of Deep Neural Networks (DNN), which focus on deducing information from data. However, the relevant information among multiple input streams has correlations and contains mutual information. This paper utilizes this opportunity to retrieve perturbed information caused by corrupted input streams. We propose InfoNet, which estimates the information entropy at every element of the input feature to the network and retrieves the missing information in the input feature matrix. Finally, using the estimated information entropy and retrieved data, we introduce a novel guided replacement procedure to recover the complete information that is the input to the downstream DNN task. We evaluate the proposed algorithm for sound localization where audio streams from the microphone array are corrupted. We have recovered the performance drop due to the corrupted input stream and reduced the localization error with non-corrupted input streams. Finally, we assess the potential of using the proposed algorithm for retrieving information in other sensing modalities, e.g., wireless signal-based source localization.

## item_id: m_3171

TITLE: Proximal Validation Protocol

ABSTRACT: Modern machine learning algorithms are generally built upon a train/validation/test split protocol. In particular, with the absence of accessible testing set in real-world ML development, how to split out a validation set becomes crucial for reliable model evaluation, selection and etc. Concretely, under a randomized splitting setup, the split ratio of the validation set generally acts as a vital meta-parameter; that is, with more data picked and used for validation, it would cost model performance due to the less training data, and vice versa. Unfortunately, this implies a vexing trade-off between performance enhancement against trustful model evaluation. However, to date, the research conducted on this line remains very few. We reason this could be due to a workflow gap between the academic and ML production which we may attribute to a form of technical debt of ML. In this article, we propose a novel scheme --- dubbed Proximal Validation Protocol (PVP) --- which is targeted to resolve this problem of validation set construction. Core to PVP is to assemble a \emph{proximal set} as a substitution for the traditional validation set while avoiding the valuable data wasted by the training procedure. The construction of the proximal validation set is established with dense data augmentation followed by a novel distributional-consistent sampling algorithm. With extensive empirical findings, we prove that PVP works (much) better than all the other existing validation protocols on three data modalities (images, text, and tabular data), demonstrating its feasibility towards ML production.

## item_id: m_3172

TITLE: Indirect Gradient Matching for Adversarial Robust Distillation

ABSTRACT: Adversarial training significantly improves adversarial robustness, but superior performance is primarily attained with large models. 
This substantial performance gap for smaller models has spurred active research into adversarial distillation (AD) to mitigate the difference. 
Existing AD methods leverage the teacher’s logits as a guide.
In contrast to these approaches, we aim to transfer another piece of knowledge from the teacher, the input gradient.
In this paper, we propose a distillation module termed Indirect Gradient Distillation Module (IGDM) that indirectly matches the student’s input gradient with that of the teacher.
Experimental results show that IGDM seamlessly integrates with existing AD methods, significantly enhancing their performance.
Particularly, utilizing IGDM on the CIFAR-100 dataset improves the AutoAttack accuracy from 28.06\% to 30.32\% with the ResNet-18 architecture and from 26.18\% to 29.32\% with the MobileNetV2 architecture when integrated into the SOTA method without additional data augmentation.

## item_id: m_3173

TITLE: Improving Adversarial Defense with Self-supervised Test-time Fine-tuning

ABSTRACT: Although adversarial training and its variants currently constitute the most effective way to achieve robustness against adversarial attacks, their poor generalization limits their performance on the test samples. In this work, we propose to improve the generalization and robust accuracy of adversarially-trained networks via self-supervised test-time fine-tuning. To this end, we introduce a meta adversarial training method to find a good starting point for test-time fine-tuning. It incorporates the test-time fine-tuning procedure into the training phase and strengthens the correlation between the self-supervised and classification tasks. The extensive experiments on CIFAR10, STL10 and Tiny ImageNet using different self-supervised tasks show that our method consistently improves the robust accuracy under different attack strategies for both the white-box and black-box attacks.

## item_id: m_3174

TITLE: A Comprehensive Overhaul of Distilling Unconditional GANs

ABSTRACT: Generative adversarial networks (GANs) have achieved impressive results on various content generation tasks. Yet, their high demand on storage and computation impedes their deployment on resource-constrained devices. Though several GAN compression methods have been proposed to address the problem, most of them focus on conditional GANs. In this paper, we provide a comprehensive overhaul of distilling unconditional GAN, especially for the popular StyleGAN2 architecture. Our key insight is that the main challenge of unconditional GAN distillation lies in the output discrepancy issue, where the teacher and student model yield different outputs given the same input latent code. Standard knowledge distillation losses typically fail under this heterogeneous distillation scenario. We conduct thorough analysis about the reasons and effects of this discrepancy issue, and identify that the style module plays a vital role in determining semantic information of generated images. Based on this finding, we propose a novel initialization strategy for the student model, which can ensure the output consistency to the maximum extent. To further enhance the semantic consistency between the teacher and student model, we present another latent-direction-based distillation loss that preserves the semantic relations in latent space. Extensive experiments demonstrate that our framework achieves state-of-the-art results in StyleGAN2 distillation, outperforming the existing GAN distillation methods by a large margin.

## item_id: m_3175

TITLE: Token-Shuffle: Towards High-Resolution Image Generation with Autoregressive Models

ABSTRACT: AutoRegressive (AR) models, long dominant in language generation, are increasingly applied to image synthesis but are often seen as less competitive than diffusion-based models. A primary limitation is the substantial number of image tokens required for AR models, which constrains both training and inference efficiency as well as image resolution. To address this, we present Token-Shuffle, a novel yet simple method that reduces the visual token number in causal masked Transformer architectures. Our motivation is the dimensional redundancy of visual vocabularies in Multimodal Large Language Models (MLLMs). Leveraging this, our method employs two key operations: token-shuffle, which merges spatially local tokens along channel dimension to decrease the token number, and token-unshuffle, which untangles the inferred tokens after Transformer blocks to restore the spatial arrangement for output. Jointly training with textual prompts, our strategy requires no additional pretrained text-encoder, and enables MLLMs to support extremely high-resolution image synthesis (over 1k resolution) in a unified next-token prediction way while maintaining efficient training and inference. For the first time, we push the boundary of AR text-to-image generation to resolution of 2048 × 2048, and set new baselins for AR-model image generation. In GenAI-benchmark, our 2.7B model achieves 0.77 overall score on hard prompts, outperforming the previous autore-gressive models LlamaGen by 0.18 and diffusion models LDM by 0.15. Based on large-scale human evaluation, we demonstrate that a pure AR-model can provide comparative or even better image generation quality as Diffusion-model and generate high-resolution images simultaneously.

## item_id: m_3176

TITLE: Pre-trained Transformers as Plug-in Defenders Against Adversarial Perturbations

ABSTRACT: With more and more deep neural networks being deployed as various daily ser- vices, their reliability is essential. It is frightening that deep neural networks are vulnerable and sensitive to adversarial attacks, the most common one of which for the services is evasion-based. Recent works usually strengthen the robustness by adversarial training or leveraging the knowledge of an amount of clean data. However, retraining and redeploying the model need a large computational budget, leading to heavy losses to the online service. In addition, when training, it is likely that only limited adversarial examples are available for the service provider, while much clean data may not be accessible. Based on the analysis on the defense for deployed models, we find that how to rapidly defend against a certain attack for a frozen original service model with limitations of few clean and adversarial examples, which is named as RaPiD (Rapid Plug-in Defender), is really important. Motivated by the generalization and the universal computation ability of pre-trained transformer models, we come up with a new defender method, CeTaD, which stands for Considering Pre-trained Transformers as Defenders. In particular, we evaluate the effectiveness and the transferability of CeTaD in the case of one-shot adversarial examples and explore the impact of different parts of CeTaD as well as training data conditions. CeTaD is flexible for different differentiable service models, and suitable for various types of attacks.

## item_id: m_3177

TITLE: Sequence to Sequence Transduction with Hard Monotonic Attention

ABSTRACT: We present a supervised sequence to sequence transduction model with a hard attention mechanism which combines the more traditional statistical alignment methods with the power of recurrent neural networks. We evaluate the model on the task of morphological inflection generation and show that it provides state of the art results in various setups compared to the previous neural and non-neural approaches. Eventually we present an analysis of the learned representations for both hard and soft attention models, shedding light on the features such models extract in order to solve the task.

## item_id: m_3178

TITLE: What Does Vision Supervision Bring to Language Models? A Case Study of CLIP

ABSTRACT: Vision-language~(V+L) pre-training has shown promising performance in cross-modal tasks such as image-text retrieval and image captioning. On the other hand, these models surprisingly perform worse than text-only models (e.g., BERT) on widely-used text-only understanding tasks. The conflicting results naturally raise a question: What does vision supervision bring to language models? 
In this paper, we investigate this under-explored problem with one representative cross-modal model CLIP.
We compare the text encoder of CLIP and widely-used text-only models on a wide range of tasks. We design a suite of evaluation tasks across three perception aspects, including the linguistic world featuring syntactic knowledge~(e.g., dependency labeling), the visual world examining visual-related commonsense knowledge (e.g., color), and the embodied world featuring physical-related commonsense knowledge (e.g., mass). Experiments demonstrate that text-only models are not always better than CLIP on these perception tasks. 
Although the text encoder of CLIP falls far behind text-only models in linguistic-related tasks, CLIP achieves better zero-shot results in visual and embodied worlds with only $0.3\%$ parameters compared to OPT-175B (one of the largest text-only models). This proves that CLIP can empower text encoders to learn rich visual and embodied knowledge through vision-text pre-training. Furthermore, qualitative studies show that CLIP pre-training yet restricts the text encoder from learning fine-grained semantics, like understanding ambiguous texts. These results shed light on future directions to improve V+L pre-training. 

## item_id: m_3179

TITLE: Protecting Your NLG Models with Semantic and Robust Watermarks

ABSTRACT: Natural language generation (NLG) applications have gained great popularity due to the powerful deep learning techniques and large training corpus. The deployed NLG models may be stolen or used without authorization, while watermark has become a useful tool to protect Intellectual Property (IP). However, existing watermark technologies are easily detected or harmful for the applications. In this paper, we propose a semantic and robust watermarking scheme for NLG models that utilize pair-matched phrases as watermarks for IP protection. The watermarks give NLG models personal preference for some special phrase combinations. When the key phrase appears behinds a specific prefix phrase, the model would give the congenial predication for the key phrase. We use word tag n-gram to generate semantic watermark which is syntax correctly. For the key phrase's predication, we choose the original model's second predication, which makes nearly no harmfulness to the task and also undetectable. Extensive experimental results demonstrate the effectiveness, robustness, and undetectability of the proposed scheme.

## item_id: m_3180

TITLE: On the Stability of Multi-branch Network

ABSTRACT: Multi-branch architectures are widely used  in state-of-the-art neural networks. Their empirical success relies on some design wisdom, like adding normalization layers or/and scaling down the initialization.  In this paper, we investigate the multi-branch architecture from the stability perspective. Specifically, we establish the forward/backward stability of multi-branch network, which leads to several new findings. Our analysis shows that only scaling down the initialization may not be enough for training multi-branch network successfully because of the uncontrollable backward process. We also unveil a new role of the normalization layer in terms of stabilizing the multi-branch architectures. More importantly, we propose a new design ``STAM aggregation" that can guarantee to STAbilize the forward/backward process of Multi-branch networks irrespective of the number of branches. We demonstrate that with STAM aggregation, the same training strategy is applicable to models with different numbers of branches, which can reduce the hyper-parameter tuning burden. Our experiments verify our theoretical findings and also demonstrate that the STAM aggregation can improve the performance of multi-branch networks considerably.

## item_id: m_3181

TITLE: Beyond Faithfulness: A Framework to Characterize and Compare Saliency Methods

ABSTRACT: Saliency methods calculate how important each input feature is to a machine learning model’s prediction, and are commonly used to understand model reasoning. “Faithfulness,” or how fully and accurately the saliency output reflects the underlying model, is an oft-cited desideratum for these methods. However, explanation methods must necessarily sacrifice certain information in service of user-oriented goals such as simplicity. To that end, and akin to performance metrics, we frame saliency methods as abstractions: individual tools that provide insight into specific aspects of model behavior and entail tradeoffs. Using this framing, we describe a framework of nine dimensions to characterize and compare the properties of saliency methods. We group these dimensions into three categories that map to different phases of the interpretation process: methodology, or how the saliency is calculated; sensitivity, or relationships between the saliency result and the underlying model or input; and, perceptibility, or how a user interprets the result. As we show, these dimensions give us a granular vocabulary for describing and comparing saliency methods — for instance, allowing us to develop “saliency cards” as a form of documentation, or helping downstream users understand tradeoffs and choose a method for a particular use case. Moreover, by situating existing saliency methods within this framework, we identify opportunities for future work, including filling gaps in the landscape and developing new evaluation metrics.


## item_id: m_3182

TITLE: ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness

ABSTRACT: Convolutional Neural Networks (CNNs) are commonly thought to recognise objects by learning increasingly complex representations of object shapes. Some recent studies suggest a more important role of image textures. We here put these conflicting hypotheses to a quantitative test by evaluating CNNs and human observers on images with a texture-shape cue conflict. We show that ImageNet-trained CNNs are strongly biased towards recognising textures rather than shapes, which is in stark contrast to human behavioural evidence and reveals fundamentally different classification strategies. We then demonstrate that the same standard architecture (ResNet-50) that learns a texture-based representation on ImageNet is able to learn a shape-based representation instead when trained on 'Stylized-ImageNet', a stylized version of ImageNet. This provides a much better fit for human behavioural performance in our well-controlled psychophysical lab setting (nine experiments totalling 48,560 psychophysical trials across 97 observers) and comes with a number of unexpected emergent benefits such as improved object detection performance and previously unseen robustness towards a wide range of image distortions, highlighting advantages of a shape-based representation.

## item_id: m_3183

TITLE: Making Stochastic Neural Networks from Deterministic Ones

ABSTRACT: It has been believed that stochastic feedforward neural networks (SFNN) have several advantages beyond deterministic deep neural networks (DNN): they have more expressive power allowing multi-modal mappings and regularize better due to their stochastic nature. However, training SFNN is notoriously harder. In this paper, we aim at developing efficient training methods for large-scale SFNN, in particular using known architectures and pre-trained parameters of DNN. To this end, we propose a new intermediate stochastic model, called Simplified-SFNN, which can be built upon any baseline DNN and approximates certain SFNN by simplifying its upper latent units above stochastic ones. The main novelty of our approach is in establishing the connection between three models, i.e., DNN
-> Simplified-SFNN -> SFNN, which naturally leads to an efficient training procedure of the stochastic models utilizing pre-trained parameters of DNN. Using several popular DNNs, we show how they can be effectively transferred to the corresponding stochastic models for both multi-modal and classification tasks on MNIST, TFD, CIFAR-10, CIFAR-100 and SVHN datasets. In particular, our stochastic model built from the wide residual network has 28 layers and 36 million parameters, where the former consistently outperforms the latter for the classification tasks on CIFAR-10 and CIFAR-100 due to its stochastic regularizing effect.

## item_id: m_3184

TITLE: Towards Understanding Linear Value Decomposition in Cooperative Multi-Agent Q-Learning

ABSTRACT: Value decomposition is a popular and promising approach to scaling up multi-agent reinforcement learning in cooperative settings. However, the theoretical understanding of such methods is limited. In this paper, we introduce a variant of the fitted Q-iteration framework for analyzing multi-agent Q-learning with value decomposition. Based on this framework, we derive a closed-form solution to the empirical Bellman error minimization with linear value decomposition. With this novel solution, we further reveal two interesting insights: 1) linear value decomposition implicitly implements a classical multi-agent credit assignment called counterfactual difference rewards; and 2) On-policy data distribution or richer Q function classes can improve the training stability of multi-agent Q-learning. In the empirical study, our experiments demonstrate the realizability of our theoretical closed-form formulation and implications in the didactic examples and a broad set of StarCraft II unit micromanagement tasks, respectively. 

## item_id: m_3185

TITLE: DBA: Distributed Backdoor Attacks against Federated Learning

ABSTRACT: Backdoor attacks aim to manipulate a subset of training data by injecting adversarial triggers such that machine learning models trained on the tampered dataset will make arbitrarily (targeted) incorrect prediction on the testset with the same trigger embedded. While federated learning (FL) is capable of aggregating information provided by different parties for training a better model, its distributed learning methodology and inherently heterogeneous data distribution across parties may bring new vulnerabilities. In addition to recent centralized backdoor attacks on FL where each party embeds the same global trigger during training, we propose the distributed backdoor attack (DBA) --- a novel threat assessment framework developed by fully exploiting the distributed nature of FL. DBA decomposes a global trigger pattern into separate local patterns and embed them into the training set of different adversarial parties respectively. Compared to standard centralized backdoors, we show that DBA is substantially more persistent and stealthy against FL on diverse datasets such as finance and image data. We conduct extensive experiments to show that the attack success rate of DBA is significantly higher than centralized backdoors under different settings. Moreover, we find that distributed attacks are indeed more insidious, as DBA can evade two state-of-the-art robust FL algorithms against centralized backdoors. We also provide explanations for the effectiveness of DBA via feature visual interpretation and feature importance ranking.
To further explore the properties of DBA, we test the attack performance by varying different trigger factors, including local trigger variations (size, gap, and location), scaling factor in FL, data distribution, and poison ratio and interval. Our proposed DBA and thorough evaluation results shed lights on characterizing the robustness of FL.

## item_id: m_3186

TITLE: A Structured Pruning Algorithm for Model-based Deep Learning

ABSTRACT: There is a growing interest in model-based deep learning (MBDL) for solving imaging inverse problems. MBDL networks can be seen as iterative algorithms that estimate the desired image using a physical measurement model and a learned image prior specified using a convolutional neural net (CNNs). The iterative nature of MBDL networks increases the test-time computational complexity, which limits their applicability in certain large-scale applications. We address this issue by presenting structured pruning algorithm for model-based deep learning (SPADE) as the first structured pruning algorithm for MBDL networks. SPADE reduces the computational complexity of CNNs used within MBDL networks by pruning its non-essential weights. We propose three distinct strategies to fine-tune the pruned MBDL networks to minimize the performance loss. Each fine-tuning strategy has a unique benefit that depends on the presence of a pre-trained model and a high-quality ground truth. We validate SPADE on two distinct inverse problems, namely compressed sensing MRI and image super-resolution. Our results highlight that MBDL models pruned by SPADE can achieve substantial speed up in testing time while maintaining competitive performance.

## item_id: m_3187

TITLE: Exact Stochastic Newton Method for Deep Learning: the feedforward networks case.

ABSTRACT: The inclusion of second-order information into Deep Learning optimization has drawn consistent interest as a way forward to improve upon gradient descent methods. Estimating the second-order update is often convoluted and computationally expensive, which drastically limits its usage scope and forces the use of various truncations and approximations.
This work demonstrates that it is possible to solve the Newton direction in the stochastic case exactly. We consider feedforward networks as a base model, build a second-order Lagrangian which we call Sifrian, and provide a closed-form formula for the exact stochastic Newton direction under some monotonicity and regularization conditions. We propose a convexity correction to escape saddle points, and we reconsider the intrinsic stochasticity of the online learning process to improve upon the formulas.  We finally compare the performance of the developed solution with well-established training methods and show its viability as a training method for Deep Learning.

## item_id: m_3188

TITLE: Data-Dependent Randomized Smoothing

ABSTRACT: Randomized smoothing is a recent technique that achieves state-of-art performance in training certifiably robust deep neural networks. While the smoothing family of distributions is often connected to the choice of the norm used for certification, the parameters of these distributions are always set as global hyper parameters independent from the input data on which a network is certified. In this work, we revisit Gaussian randomized smoothing and show that the variance of the Gaussian distribution can be optimized at each input so as to maximize the certification radius for the construction of the smooth classifier. We also propose a simple memory-based approach to certifying the resultant smooth classifier. This new approach is generic, parameter-free, and easy to implement. In fact, we show that our data dependent framework can be seamlessly incorporated into 3 randomized smoothing approaches, leading to consistent improved certified accuracy. When this framework is used in the training routine of these approaches followed by a data dependent certification, we achieve 9% and 6% improvement over the certified accuracy of the strongest baseline for a radius of 0.5 on CIFAR10 and ImageNet. 

## item_id: m_3189

TITLE: Learning to Decompose Compound Questions with Reinforcement Learning

ABSTRACT: As for knowledge-based question answering, a fundamental problem is to relax the assumption of answerable questions from simple questions to compound questions. Traditional approaches firstly detect topic entity mentioned in questions, then traverse the knowledge graph to find relations as a multi-hop path to answers, while we propose a novel approach to leverage simple-question answerers to answer compound questions. Our model consists of two parts: (i) a novel learning-to-decompose agent that learns a policy to decompose a compound question into simple questions and (ii) three independent simple-question answerers that classify the corresponding relations for each simple question. Experiments demonstrate that our model learns complex rules of compositionality as stochastic policy, which benefits simple neural networks to achieve state-of-the-art results on WebQuestions and MetaQA. We analyze the interpretable decomposition process as well as generated partitions.

## item_id: m_3190

TITLE: Non-maximum Suppression Also Closes the Variational Approximation Gap of Multi-object Variational Autoencoders

ABSTRACT: Learning object-centric scene representations is crucial for scene structural understanding. However, current unsupervised scene factorization and representation learning models do not reason about scene objects' relations while making an inference. In this paper, we address the issue by introducing a differentiable correlation prior that forces the inference models to suppress duplicate object representations. The extension is evaluated by adding it to three different scene understanding approaches. The results show that the models trained with the proposed method not only outperform the original models in scene factorization and have fewer duplicate representations, but also close the approximation gap between the data evidence and the evidence lower bound.

## item_id: m_3191

TITLE: Fast Chirplet Transform to Enhance CNN Machine Listening - Validation on Animal calls and Speech

ABSTRACT: The scattering framework offers an optimal hierarchical convolutional decomposition according to its kernels.  Convolutional Neural Net (CNN) can be seen asan optimal kernel decomposition, nevertheless it requires large amount of trainingdata to learn its kernels.  We propose a trade-off between these two approaches: a Chirplet kernel as an efficient Q constant bioacoustic representation to pretrainCNN. First we motivate Chirplet bioinspired auditory representation. Second we give the first algorithm (and code) of a Fast Chirplet Transform (FCT). Third, we demonstrate the computation efficiency of FCT on large environmental data base: months of Orca recordings, and 1000 Birds species from the LifeClef challenge. Fourth, we validate FCT on the vowels subset of the Speech TIMIT dataset. The results show that FCT accelerates CNN when it pretrains low level layers: it reduces training duration by -28% for birds classification, and by -26% for vowels classification. Scores are also enhanced by FCT pretraining, with a relative gain of +7.8% of Mean Average Precision on birds,  and +2.3% of vowel accuracy against raw audio CNN. We conclude on perspectives on tonotopic FCT deep machine listening, and inter-species bioacoustic transfer learning to generalise the representation of animal communication systems.

## item_id: m_3192

TITLE: Using Planning to Improve Semantic Parsing of Instructional Texts

ABSTRACT: We develop a method for few-shot semantic parsing of instructional texts. The system takes long-form instructional texts as input and produces sequences of actions in a formal language that enable execution of the instructions. This task poses unique challenges since input texts may contain long context dependencies and ambiguous and domain-specific language. Valid semantic parses also require sequences of steps that constitute an executable plan. We build on recent progress in semantic parsing by leveraging large language models to learn parsers from small amounts of training data. During decoding, our method employs planning methods and domain information to rank and correct candidate parses. To validate our method, we investigate recipe interpretation in two cooking domains. We present results for few-shot semantic parsing using leave-one-out cross-validation. We show that utilizing planning domain information improves the quality of generated plans. Through ablations we also explore the effects of our decoder design choices and model size.

## item_id: m_3193

TITLE: Learning the Latent Noisy Data Generative Process for Label-Noise Learning

ABSTRACT: In learning with noisy labels, the noise transition reveals how an instance relates from its clean label to its noisy one. Accurately inferring an instance's noise transition is crucial for inferring its clean label.  However, when only a noisy dataset is available, noise transitions can typically be inferred only for a ``special'' group of instances. To use these learned transitions to assist in inferring others, it is essential to understand the connections among different transitions across different instances.
Existing work usually addresses this by introducing assumptions that explicitly define the similarity of noise transitions across various instances. However, these similarity-based assumptions often lack empirical validation and may not be aligned with real-world data. The misalignment can lead to misinterpretations of both noise transitions and clean labels.
In this work, instead of directly defining similarity, we propose modeling the generative process of noisy data. Intuitively, to understand the connections among noise transitions across different instances, we represent the causal generative process of noisy data using a learnable graphical model. Relying solely on noisy data, our method can effectively discern the underlying causal generative process, subsequently inferring the noise transitions of instances and their clean labels. Experiments on various datasets with different types of label noise further demonstrate our method's effectiveness.

## item_id: m_3194

TITLE: Neural Collaborative Filtering Bandits via Meta Learning

ABSTRACT: Contextual multi-armed bandits provide powerful tools to solve the exploitation-exploration dilemma in decision making, with direct applications in the personalized recommendation. In fact, collaborative effects among users carry the significant potential to improve the recommendation. In this paper, we introduce and study the problem by exploring `Neural Collaborative Filtering Bandits', where the rewards can be non-linear functions and groups are formed dynamically given different specific contents. To solve this problem, we propose a meta-learning based bandit algorithm,  Meta-Ban (\textbf{meta-ban}dits), where a meta-learner is designed to represent and rapidly adapt to dynamic groups, along with an informative UCB-based exploration strategy. Furthermore, we analyze that Meta-Ban can achieve the regret bound of $\mathcal{O}(\sqrt{nT\log T})$, which is sharper over state-of-the-art related works. In the end, we conduct extensive experiments showing that Meta-Ban outperforms six strong baselines.

## item_id: m_3195

TITLE: Character Generation through Self-Supervised Vectorization

ABSTRACT: The prevalent approach in self-supervised image generation is to operate on pixel level representations. While this approach can produce high quality images, it cannot benefit from the simplicity and innate quality of vectorization. Here we present  a drawing agent that operates on stroke-level representation of images. At each time step, the agent first assesses the current canvas and decides whether to stop or keep drawing. When a `draw’ decision is made, the agent outputs a program indicating the stroke to be drawn. As a result, it produces a final raster image by drawing the strokes on a canvas, using a minimal number of strokes and dynamically deciding when to stop. We train our agent through reinforcement learning on MNIST and Omniglot  datasets for unconditional generation and parsing (reconstruction) tasks. We utilize our parsing agent for exemplar generation and type conditioned concept generation in Omniglot challenge without any further training. We present successful results on all three generation tasks and the parsing task. Crucially, we do not need  any stroke-level or vector supervision; we only use raster images for training.  Code will be made available upon acceptance. 


## item_id: m_3196

TITLE: Decomposing Motion and Content for Natural Video Sequence Prediction

ABSTRACT: We propose a deep neural network for the prediction of future frames in natural video sequences. To effectively handle complex evolution of pixels in videos, we propose to decompose the motion and content, two key components generating dynamics in videos. Our model is built upon the Encoder-Decoder Convolutional Neural Network and Convolutional LSTM for pixel-level prediction, which independently capture the spatial layout of an image and the corresponding temporal dynamics. By independently modeling motion and content, predicting the next frame reduces to converting the extracted content features into the next frame content by the identified motion features, which simplifies the task of prediction. Our model is end-to-end trainable over multiple time steps, and naturally learns to decompose motion and content without separate training. We evaluate the pro- posed network architecture on human activity videos using KTH, Weizmann action, and UCF-101 datasets. We show state-of-the-art performance in comparison to recent approaches. To the best of our knowledge, this is the first end-to-end trainable network architecture with motion and content separation to model the spatio-temporal dynamics for pixel-level future prediction in natural videos.

## item_id: m_3197

TITLE: Graph Synthetic Out-of-Distribution Exposure with Large Language Models

ABSTRACT: Out-of-distribution (OOD) detection in graphs is critical for ensuring model robustness in open-world and safety-sensitive applications. Existing graph OOD detection approaches typically train an in-distribution (ID) classifier on ID data alone, then apply post-hoc scoring to detect OOD instances. While OOD exposure—adding auxiliary OOD samples during training—can improve detection, current graph-based methods often assume access to real OOD nodes, which is often impractical or costly. In this paper, we present GOE-LLM, a framework that leverages Large Language Models (LLMs) to achieve OOD exposure on text-attributed graphs without using any real OOD nodes. GOE-LLM introduces two pipelines: (1) identifying pseudo-OOD nodes from the initially unlabeled graph using zero-shot LLM annotations, and (2) generating semantically informative synthetic OOD nodes via LLM-prompted text generation. These pseudo-OOD nodes are then used to regularize ID classifier training and enhance OOD detection awareness. Empirical results on multiple benchmarks show that GOE-LLM substantially outperforms state-of-the-art methods without OOD exposure, achieving up to a 23.5% improvement in AUROC for OOD detection, and attains performance on par with those relying on real OOD labels for exposure.

## item_id: m_3198

TITLE: Revisit Model Adaptation from Parameters to Features

ABSTRACT: In this paper, we focus on an intriguing question: Can existing fine-tuning adapters, such as LoRA, trained on one model be effectively transferred to its parameter-wise variants? To investigate this problem, we first examine the technical underpinnings of widely adopted parameter-efficient fine-tuning methods. Our theoretical analysis reveals that, due to the strong coupling between adaptation components and base weights, these methods are vulnerable to weight transformations, leading to unsatisfactory cross-model performance and potential model-specific overfitting. To alleviate this issue, we accordingly propose two alternatives, which pose the adaptation on the input and output features, respectively, with an explicit decoupling scheme. In this way, the adaptation components for an unseen base model can be modulated by its native parameters and thus exhibit more robust transferability. Notably, the proposed methods can serve as plug-and-play components with merely one-line code modifications required. Though extremely simple, extensive experiments across a variety of models and applications demonstrate that our method achieves comparable performance to existing counterparts on the source model and consistently outperforms them in cross-model transfer settings.

## item_id: m_3199

TITLE: Automated Fine-Grained Mixture-of-Experts Quantization

ABSTRACT: Mixture of Experts (MoE) enables efficient parameter scaling in large language models by dynamically activating relevant parameter subsets per input token. 
Compressing MoE models presents unique challenges due to their inherent sparsity. Traditional quantization techniques, which are typically effective for dense models, prove inadequate when applied to MoE architectures.
This paper proposes an efficient MoE quantization algorithm.
We propose a fine-grained, adaptive quantization approach coupled with an efficient method for determining optimal configurations.
Specifically, we construct a mixed-precision quantization search space encompassing different granularities from expert-level to channel-level. 
This approach facilitates precise bit-width resource allocation across model components based on their significance and activation frequency. 
And then, we leverage evolutionary algorithms to efficiently navigate this search space, autonomously identifying optimal quantization configurations. 
The synergy between adaptive granularity and automated search effectively mitigates the distinctive quantization challenges inherent to MoE models, culminating in a fully automated framework for efficient MoE quantization.
Experimental results indicate that our method achieves significant performance improvements across multiple evaluation tasks, with particularly notable results in low-bit quantization scenarios.
When applied to the Mixtral-8x7b-v0.1 model, our approach outperforms the current state-of-the-art by $9.24$\% , setting a new benchmark in MoE quantization. Code is available in supplementary materials.

## item_id: m_3200

TITLE: D$^2$ETR: Decoder-Only DETR with Computationally Efficient Cross-Scale Attention

ABSTRACT: DETR is the first fully end-to-end detector that predicts a final set of predictions without post-processing. However, it suffers from problems such as low performance and slow convergence. A series of works aim to tackle these issues in different ways, but the computational cost is yet expensive due to the sophisticated encoder-decoder architecture. To alleviate this issue, we propose a decoder-only detector called D$^2$ETR. In the absence of encoder, the decoder directly attends to the fine-fused feature maps generated by the Transformer backbone with a novel computationally efficient cross-scale attention module. D$^2$ETR demonstrates low computational complexity and high detection accuracy in evaluations on the COCO benchmark, outperforming DETR and its variants.
