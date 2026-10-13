# Batch 01 — 100 items

## item_id: m_0001

TITLE: SNIP: SINGLE-SHOT NETWORK PRUNING BASED ON CONNECTION SENSITIVITY

ABSTRACT: Pruning large neural networks while maintaining their performance is often desirable due to the reduced space and time complexity. In existing methods, pruning is done within an iterative optimization procedure with either heuristically designed pruning schedules or additional hyperparameters, undermining their utility. In this work, we present a new approach that prunes a given network once at initialization prior to training. To achieve this, we introduce a saliency criterion based on connection sensitivity that identifies structurally important connections in the network for the given task. This eliminates the need for both pretraining and the complex pruning schedule while making it robust to architecture variations. After pruning, the sparse network is trained in the standard way. Our method obtains extremely sparse networks with virtually the same accuracy as the reference network on the MNIST, CIFAR-10, and Tiny-ImageNet classification tasks and is broadly applicable to various architectures including convolutional, residual and recurrent networks. Unlike existing methods, our approach enables us to demonstrate that the retained connections are indeed relevant to the given task.

## item_id: m_0002

TITLE: Deep Learning as a Mixed Convex-Combinatorial Optimization Problem

ABSTRACT: As neural networks grow deeper and wider, learning networks with hard-threshold activations is becoming increasingly important, both for network quantization, which can drastically reduce time and energy requirements, and for creating large integrated systems of deep networks, which may have non-differentiable components and must avoid vanishing and exploding gradients for effective learning. However, since gradient descent is not applicable to hard-threshold functions, it is not clear how to learn them in a principled way. We address this problem by observing that setting targets for hard-threshold hidden units in order to minimize loss is a discrete optimization problem, and can be solved as such. The discrete optimization goal is to find a set of targets such that each unit, including the output, has a linearly separable problem to solve. Given these targets, the network decomposes into individual perceptrons, which can then be learned with standard convex approaches. Based on this, we develop a recursive mini-batch algorithm for learning deep hard-threshold networks that includes the popular but poorly justified straight-through estimator as a special case. Empirically, we show that our algorithm improves classification accuracy in a number of settings, including for AlexNet and ResNet-18 on ImageNet, when compared to the straight-through estimator.

## item_id: m_0003

TITLE: Secure Domain Adaptation with Multiple Sources

ABSTRACT: Multi-source unsupervised domain adaptation (MUDA) is a recently explored  learning framework within UDA, where the goal is to address the challenge of annotated data scarcity in a target domain via transferring knowledge from multiple source domains with annotated data.  When the source domains are distributed, data privacy and security can become a significant concern, e.g., medical domains, yet existing MUDA methods overlook this concern. We develop an algorithm to address MUDA when source domains' data cannot be shared.  Our method is based on aligning the distributions of the source and target domains indirectly via  internally learned distributions in an intermediate embedding space. Our  theoretical analysis supports our approach and extensive empirical results demonstrate our algorithm is effective and compares favorably against existing MUDA methods.

## item_id: m_0004

TITLE: On Layer Normalization in the Transformer Architecture

ABSTRACT: The Transformer architecture is popularly used in natural language processing tasks. To train a Transformer model, a carefully designed learning rate warm-up stage is usually needed: the learning rate has to be set to an extremely small value at the beginning of the optimization and then gradually increases in some given number of iterations. Such a stage is shown to be crucial to the final performance and brings more hyper-parameter tunings. In this paper, we study why the learning rate warm-up stage is important in training the Transformer and theoretically show that the location of layer normalization matters. It can be proved that at the beginning of the optimization, for the original Transformer, which places the layer normalization between the residual blocks, the expected gradients of the parameters near the output layer are large. Then using a large learning rate on those gradients makes the training unstable. The warm-up stage is practically helpful to avoid this problem. Such an analysis motivates us to investigate a slightly modified Transformer architecture which locates the layer normalization inside the residual blocks. We show that the gradients in this Transformer architecture are well-behaved at initialization. Given these findings,  we are the first to show that this Transformer variant is easier and faster to train. The learning rate warm-up stage can be safely removed, and the training time can be largely reduced on a wide range of applications.

## item_id: m_0005

TITLE: Semi-supervised learning by selective training with pseudo labels via confidence estimation

ABSTRACT: We propose a novel semi-supervised learning (SSL) method that adopts selective training with pseudo labels. In our method, we generate hard pseudo-labels and also estimate their confidence, which represents how likely each pseudo-label is to be correct. Then, we explicitly select which pseudo-labeled data should be used to update the model. Specifically, assuming that loss on incorrectly pseudo-labeled data sensitively increase against data augmentation, we select the data corresponding to relatively small loss after applying data augmentation. The confidence is used not only for screening candidates of pseudo-labeled data to be selected but also for automatically deciding how many pseudo-labeled data should be selected within a mini-batch. Since accurate estimation of the confidence is crucial in our method, we also propose a new data augmentation method, called MixConf, that enables us to obtain confidence-calibrated models even when the number of training data is small. Experimental results with several benchmark datasets validate the advantage of our SSL method as well as MixConf.

## item_id: m_0006

TITLE: Crafting Data-free Universal Adversaries with Dilate Loss

ABSTRACT: We introduce a method to create Universal Adversarial Perturbations (UAP) for a given CNN in a data-free manner. Data-free approaches suite scenarios where the original training data is unavailable for crafting adversaries. We show that the adversary generation with full training data can be approximated to a formulation without data. This is realized through a sequential optimization of the adversarial perturbation with the proposed dilate loss. Dilate loss basically maximizes the Euclidean norm of the output before nonlinearity at any layer. By doing so, the perturbation constrains the ReLU activation function at every layer to act roughly linear for data points and thus eliminate the dependency on data for crafting UAPs. Extensive experiments demonstrate that our method not only has theoretical support, but achieves higher fooling rate than the existing data-free work. Furthermore, we evidence improvement in limited data cases as well.

## item_id: m_0007

TITLE: Improved Group Robustness via Classifier Retraining on Independent Splits

ABSTRACT: Deep neural networks learned by minimizing the average risk can achieve strong average performance, but their performance for a subgroup may degrade, if the subgroup is underrepresented in the overall data population. Group distributionally robust optimization (Sagawa et al., 2020a, GDRO) is a standard baseline for learning models with strong worst-group performance. However, GDRO requires group labels for every example during training and can be prone to overfitting, often requiring careful model capacity control via regularization or early stopping. When only a limited amount of group labels is available, Just Train Twice (Liu et al., 2021, JTT) is a popular approach which infers a pseudo-group-label for every unlabeled example. The process of inferring pseudo labels can be highly sensitive during model selection. To alleviate overfitting for GDRO and the pseudo labeling process for JTT, we propose a new method via classifier retraining on independent splits (of the training data). We find that using a novel sample splitting procedure achieves robust worst-group performance in the fine-tuning step. When evaluated on benchmark image and text classification tasks, our approach consistently reduces the requirement of group labels and hyperparameter search during training. Experimental results confirm that our approach performs favorably compared with existing methods (including GDRO and JTT) when either group labels are available during training or are only available during validation.

## item_id: m_0008

TITLE: Words or Characters? Fine-grained Gating for Reading Comprehension

ABSTRACT: Previous work combines word-level and character-level representations using concatenation or scalar weighting, which is suboptimal for high-level tasks like reading comprehension. We present a fine-grained gating mechanism to dynamically combine word-level and character-level representations based on properties of the words. We also extend the idea of fine-grained gating to modeling the interaction between questions and paragraphs for reading comprehension. Experiments show that our approach can improve the performance on reading comprehension tasks, achieving new state-of-the-art results on the Children's Book Test and Who Did What datasets. To demonstrate the generality of our gating mechanism, we also show improved results on a social media tag prediction task.

## item_id: m_0009

TITLE: Learning through Dialogue Interactions by Asking Questions

ABSTRACT: A good dialogue agent should have the ability to interact with users by both responding to questions and by asking questions, and importantly to learn from both types of interactions. In this work, we explore this direction by designing a simulator and a set of synthetic tasks in the movie domain that allow such interactions between a learner and a teacher. We investigate how a learner can benefit from asking questions in both offline and online reinforcement learning settings, and demonstrate that the learner improves when asking questions. Our work represents a first step in developing such end-to-end learned interactive dialogue agents.


## item_id: m_0010

TITLE: A Benchmark for Learning to Translate a New Language from One Grammar Book

ABSTRACT: Large language models (LLMs) can perform impressive feats with in-context learning or lightweight finetuning. It is natural to wonder how well these models adapt to genuinely new tasks, but how does one find tasks that are unseen in internet-scale training sets? We turn to a field that is explicitly motivated and bottlenecked by a scarcity of web data: low-resource languages. In this paper, we introduce MTOB (Machine Translation from One Book), a benchmark for learning to translate between English and Kalamang—a language with less than 200 speakers and therefore virtually no presence on the web—using several hundred pages of field linguistics reference materials. This task framing is novel in that it asks a model to learn a language from a single human-readable book of grammar explanations, rather than a large mined corpus of in-domain data, more akin to L2 language learning than L1 language acquisition. We demonstrate that baselines using current LLMs are promising but fall short of human performance, achieving 44.7 chrF on Kalamang to English translation and 45.8 chrF on English to Kalamang translation, compared to 51.6 and 57.0 chrF by a human who learned Kalamang from the same reference materials. We hope that MTOB will help measure LLM capabilities along a new dimension, and that the methods developed to solve it could help expand access to language technology for underserved communities by leveraging qualitatively different kinds of data than traditional machine translation.

## item_id: m_0011

TITLE: Reward Estimation via State Prediction

ABSTRACT: Reinforcement learning typically requires carefully designed reward functions in order to learn the desired behavior. We present a novel reward estimation method that is based on a finite sample of optimal state trajectories from expert demon- strations and can be used for guiding an agent to mimic the expert behavior. The optimal state trajectories are used to learn a generative or predictive model of the “good” states distribution. The reward signal is computed by a function of the difference between the actual next state acquired by the agent and the predicted next state given by the learned generative or predictive model. With this inferred reward function, we perform standard reinforcement learning in the inner loop to guide the agent to learn the given task. Experimental evaluations across a range of tasks demonstrate that the proposed method produces superior performance compared to standard reinforcement learning with both complete or sparse hand engineered rewards. Furthermore, we show that our method successfully enables an agent to learn good actions directly from expert player video of games such as the Super Mario Bros and Flappy Bird.

## item_id: m_0012

TITLE: Fast Adaptation in Generative Models with Generative Matching Networks

ABSTRACT: Despite recent advances, the remaining bottlenecks in deep generative models are necessity of extensive training and difficulties with generalization from small number of training examples.
Both problems may be addressed by conditional generative models that are trained to adapt the generative distribution to additional input data.
So far this idea was explored only under certain limitations such as restricting the input data to be a single object or multiple objects representing the same concept.  
In this work we develop a new class of deep generative model called generative matching networks which is inspired by the recently proposed matching networks for one-shot learning in discriminative tasks and the ideas from meta-learning.
By conditioning on the additional input dataset, generative matching networks may instantly learn new concepts that were not available during the training but conform to a similar generative process, without explicit limitations on the number of additional input objects or the number of concepts they represent. 
Our experiments on the Omniglot dataset demonstrate that generative matching networks can significantly improve predictive performance on the fly as more additional data is available to the model and also adapt the latent space which is beneficial in the context of feature extraction.

## item_id: m_0013

TITLE: Deconfounding Reinforcement Learning in Observational Settings

ABSTRACT: In this paper, we propose a general formulation to cope with a family of reinforcement learning tasks in observational settings, that is, learning good policies solely from the historical data produced by real environments with confounders (i.e., the factors affecting both actions and rewards). Based on the proposed approach, we extend one representative of reinforcement learning algorithms: the Actor-Critic method, to its deconfounding variant, which is also straightforward to be applied to other algorithms. In addition, due to lack of datasets in this direction, a benchmark is developed for deconfounding reinforcement learning algorithms by revising OpenAI Gym and MNIST. We demonstrate that the proposed algorithms are superior to traditional reinforcement learning algorithms in confounded environments. To the best of our knowledge, this is the first time that confounders are taken into consideration for addressing full reinforcement learning problems.

## item_id: m_0014

TITLE: Leveraging Hard Negative Priors for Automatic Medical Report Generation

ABSTRACT: Recently, automatic medical report generation has become an active research topic in medical imaging field. It is imperative for the model to identify normal and abnormal regions in a medical image to generate a coherent and diverse report. However, medical datasets are highly biased towards normal regions. This makes most existing models tend to generate a generic report without sufficiently considering the uniqueness of individual images. In this paper, we propose a learning framework to extract distinctive image and report features for each sample by distinguishing it from its closest peer (denoted as hard negative in this paper) and gradually increasing the difficulty of such a task through synthesizing harder and harder negatives during training. Specifically, a prior hard negative report, which is the report closest to an anchor report in the dataset, is initially identified by using a pre-trained Sentence Transformer. To force our report decoder to capture highly distinctive and image-correlated text features, harder and harder negative reports keep being synthesized by gradually moving the prior hard negative report towards the anchor report in the latent space during training. The harder negative report is used to evaluate a triplet loss that is minimized to enforce the distance between the matched image and report to be smaller than the distance between an image and its synthesized harder negative report. Meanwhile, the associated images of the anchor report and its prior hard negative report form a hard negative image pair, and a cosine similarity loss is used to capture the distinctive features of the anchor image by pushing the hard negative image away.  In this way, our model could achieve subtle representative resolution (i.e., the ability to distinguish two similar samples). As a general method, we demonstrate experimentally that our framework could be readily incorporated into a variety of existing medical report generation models, and significantly improve the corresponding baselines. Our code will be publicly released at

## item_id: m_0015

TITLE: Discovering Non-monotonic Autoregressive Orderings with Variational Inference

ABSTRACT: The predominant approach for language modeling is to encode a sequence of tokens from left to right, but this eliminates a source of information: the order by which the sequence was naturally generated. One strategy to recover this information is to decode both the content and ordering of tokens. Some prior work supervises content and ordering with hand-designed loss functions to encourage specific orders or bootstraps from a predefined ordering. These approaches require domain-specific insight. Other prior work searches over valid insertion operations that lead to ground truth sequences during training, which has high time complexity and cannot be efficiently parallelized. We address these limitations with an unsupervised learner that can be trained in a fully-parallelizable manner to discover high-quality autoregressive orders in a data driven way without a domain-specific prior. The learner is a neural network that performs variational inference with the autoregressive ordering as a latent variable. Since the corresponding variational lower bound is not differentiable, we develop a practical algorithm for end-to-end optimization using policy gradients. Strong empirical results with our solution on sequence modeling tasks suggest that our algorithm is capable of discovering various autoregressive orders for different sequences that are competitive with or even better than fixed orders.

## item_id: m_0016

TITLE: Graph Neural Networks with Learnable Structural and Positional Representations

ABSTRACT: Graph neural networks (GNNs) have become the standard learning architectures for graphs. GNNs have been applied to numerous domains ranging from quantum chemistry, recommender systems to knowledge graphs and natural language processing. A major issue with arbitrary graphs is the absence of canonical positional information of nodes, which decreases the representation power of GNNs to distinguish e.g. isomorphic nodes and other graph symmetries. An approach to tackle this issue is to introduce Positional Encoding (PE) of nodes, and inject it into the input layer, like in Transformers. Possible graph PE are Laplacian eigenvectors. In this work, we propose to decouple structural and positional representations to make easy for the network to learn these two essential properties. We introduce a novel generic architecture which we call \texttt{LSPE} (Learnable Structural and Positional Encodings). We investigate several sparse and fully-connected (Transformer-like) GNNs, and observe a performance increase for molecular datasets, from $1.79\%$ up to $64.14\%$ when considering learnable PE for both GNN classes.

## item_id: m_0017

TITLE: Towards More Theoretically-Grounded Particle Optimization Sampling for Deep Learning

ABSTRACT: Many deep-learning based methods such as Bayesian deep learning (DL) and deep reinforcement learning (RL) have heavily relied on the ability of a model being able to efficiently explore via Bayesian sampling. Particle-optimization sampling (POS) is a recently developed technique to generate high-quality samples from a target distribution by iteratively updating a set of interactive particles, with a representative algorithm the Stein variational gradient descent (SVGD). Though obtaining significant empirical success, the {\em non-asymptotic} convergence behavior of SVGD remains unknown. In this paper, we generalize POS to a stochasticity setting by injecting random noise in particle updates, called stochastic particle-optimization sampling (SPOS). Notably, for the first time, we develop {\em non-asymptotic convergence theory} for the SPOS framework, characterizing convergence of a sample approximation w.r.t.\! the number of particles and iterations under both convex- and noncovex-energy-function settings. Interestingly, we provide theoretical understanding of a pitfall of SVGD that can be avoided in the proposed SPOS framework, {\it i.e.}, particles tend to collapse to a local mode in SVGD under some particular conditions. Our theory is based on the analysis of nonlinear stochastic differential equations, which serves as an extension and a complementary development to the asymptotic convergence theory for SVGD such as (Liu, 2017). With such theoretical guarantees, SPOS can be safely and effectively applied on both Bayesian DL and deep RL tasks. Extensive results demonstrate the effectiveness of our proposed framework.

## item_id: m_0018

TITLE: Continuously Discovering Novel Strategies via Reward-Switching Policy Optimization

ABSTRACT: We present Reward-Switching Policy Optimization (RSPO), a paradigm to discover diverse strategies in complex RL environments by iteratively finding novel policies that are both locally optimal and sufficiently different from existing ones. To encourage the learning policy to consistently converge towards a previously undiscovered local optimum, RSPO switches between extrinsic and intrinsic rewards via a trajectory-based novelty measurement during the optimization process. When a sampled trajectory is sufficiently distinct, RSPO performs standard policy optimization with extrinsic rewards. For trajectories with high likelihood under existing policies, RSPO utilizes an intrinsic diversity reward to promote exploration. Experiments show that RSPO is able to discover a wide spectrum of strategies in a variety of domains, ranging from single-agent navigation tasks and MuJoCo control to multi-agent stag-hunt games and the StarCraft II Multi-Agent Challenge.

## item_id: m_0019

TITLE: On the Fast Convergence of Unstable Reinforcement Learning Problems

ABSTRACT:   For many of the reinforcement learning applications, the system is assumed to be inherently stable and with bounded reward, state and action space. These are key requirements for the optimization convergence of classical reinforcement learning reward function with discount factors. Unfortunately, these assumptions do not hold true for many real world problems such as an unstable linear–quadratic regulator (LQR). In this work, we propose new methods to stabilize and speed up the convergence of unstable reinforcement learning problems with the policy gradient methods. We provide theoretical insights on the efficiency of our methods. In practice, our method achieve good experimental results over multiple examples where the vanilla methods mostly fail to converge due to system instability.

## item_id: m_0020

TITLE: From Five Dimensions to Many: Large Language Models as Precise and Interpretable Psychological Profilers

ABSTRACT: Psychological constructs within individuals are widely believed to be interconnected. We investigated whether and how Large Language Models (LLMs) can model the correlational structure of human psychological traits from minimal quantitative inputs. We prompted various LLMs with Big Five Personality Scale responses from 816 human individuals to role-play their responses on nine other psychological scales. LLMs demonstrated remarkable accuracy in capturing human psychological structure, with the inter-scale correlation patterns from LLM-generated responses strongly aligning with those from human data (R² > 0.88). This zero-shot performance substantially exceeded predictions based on semantic similarity and approached the accuracy of machine learning algorithms trained directly on the dataset. Analysis of reasoning traces revealed that LLMs use a systematic two-stage process: First, they transform raw Big Five responses into natural language personality summaries through information selection and compression, analogous to generating sufficient statistics. Second, they generate target scale responses based on reasoning from these summaries. For information selection, LLMs identify the same key personality factors as trained algorithms, though they fail to differentiate item importance within factors. The resulting compressed summaries are not merely redundant representations but capture synergistic information—adding them to original scores enhances prediction alignment, suggesting they encode emergent, second-order patterns of trait interplay. Our findings demonstrate that LLMs can precisely predict individual participants' psychological traits from minimal data through a process of abstraction and reasoning, offering both a powerful tool for psychological simulation and valuable insights into their emergent reasoning capabilities.

## item_id: m_0021

TITLE: Critical Percolation as a Framework to Analyze the Training of Deep Networks

ABSTRACT: In this paper we approach two relevant deep learning topics: i) tackling of graph structured input data and ii) a better understanding and analysis of deep networks and related learning algorithms. With this in mind we focus on the topological classification of reachability in a particular subset of planar graphs (Mazes). Doing so, we are able to model the topology of data while staying in Euclidean space, thus allowing its processing with standard CNN architectures. We suggest a suitable architecture for this problem and show that it can express a perfect solution to the classification task. The shape of the cost function around this solution is also derived and, remarkably, does not depend on the size of the maze in the large maze limit. Responsible for this behavior are rare events in the dataset which strongly regulate the shape of the cost function near this global minimum. We further identify an obstacle to learning in the form of poorly performing local minima in which the network chooses to ignore some of the inputs. We further support our claims with training experiments and numerical analysis of the cost function on networks with up to $128$ layers.

## item_id: m_0022

TITLE: Label Cleaning with Likelihood Ratio Test

ABSTRACT: To collect large scale annotated data, it is inevitable to introduce label noise, i.e., incorrect class labels. A major challenge is to develop robust deep learning models that achieve high test performance despite training set label noise.  We introduce a novel approach that directly cleans labels in order to train a high quality model. Our method leverages statistical principles to correct data labels and has a theoretical guarantee of the correctness.  In particular, we use a likelihood ratio test(LRT) to flip the labels of training data.  We prove that our LRT label correction algorithm is guaranteed to flip the label so it is consistent with the true Bayesian optimal decision rule with high probability.  We incorporate our label correction algorithm into the training of deep neural networks and train models that achieve superior testing performance on multiple public datasets.

## item_id: m_0023

TITLE: Smooth Mathematical Functions from Compact Neural Networks

ABSTRACT: This is paper for the smooth function approximation by neural networks (NN). Mathematical or physical functions can be replaced by NN models through regression. In this study, we get NNs that generate highly accurate and highly smooth function, which only comprised of a few weight parameters, through discussing a few topics about regression. First, we reinterpret inside of NNs for regression; consequently, we propose a new activation function--integrated sigmoid linear unit (ISLU). Then special charateristics of metadata for regression, which is different from other data like image or sound, is discussed for improving the performance of neural networks. Finally, the one of a simple hierarchical NN that generate models substituting mathematical function is presented, and the new batch concept ``meta-batch" which improves the performance of NN several times more is introduced. The new activation function, meta-batch method, features of numerical data, meta-augmentation with metaparameters, and a structure of NN generating a compact multi-layer perceptron(MLP) are essential in this study.

## item_id: m_0024

TITLE: DropMax: Adaptive Stochastic Softmax

ABSTRACT: We propose DropMax, a stochastic version of softmax classifier which at each iteration drops non-target classes with some probability, for each instance. Specifically, we overlay binary masking variables over class output probabilities, which are learned based on the input via regularized variational inference. This stochastic regularization has an effect of building an ensemble classifier out of combinatorial number of classifiers with different decision boundaries. Moreover, the learning of dropout probabilities for non-target classes on each instance allows the classifier to focus more on classification against the most confusing classes. We validate our model on multiple public datasets for classification, on which it obtains improved accuracy over regular softmax classifier and other baselines. Further analysis of the learned dropout masks shows that our model indeed selects confusing classes more often when it performs classification.

## item_id: m_0025

TITLE: Improving Semantic Parsing with Neural Generator-Reranker Architecture

ABSTRACT: Semantic parsing is the problem of deriving machine interpretable meaning representations from natural language utterances. Neural models with encoder-decoder architectures have recently achieved substantial improvements over traditional methods. Although neural semantic parsers appear to have relatively high recall using large beam sizes, there is room for improvement with respect to one-best precision. In this work, we propose a generator-reranker architecture for semantic parsing. The generator produces a list of potential candidates and the reranker, which consists of a pre-processing step for the candidates followed by a novel critic network, reranks these candidates based on the similarity between each candidate and the input sentence. We show the advantages of this approach along with how it improves the parsing performance through extensive analysis. We experiment our model on three semantic parsing datasets (GEO, ATIS, and OVERNIGHT). The overall architecture achieves the state-of-the-art results in all three datasets. 

## item_id: m_0026

TITLE: AbnormalLog: A Deep Anomaly Detection Method for Log Sequence Data

ABSTRACT: Anomaly detection for computer log sequence data plays a very important role in various industries. Log data is complex time series with plenty of text information, which is difficult to process due to both its non-structural characteristics and temporal correlation. Existing log anomaly detection schemes do not utilize all available data information such as the semantic and parameter information, nor do they consider weighting of data based on time. The AbnormalLog algorithm proposed in this paper implements semantic parsing technique to expand current detection schemes by analyzing template and parameter information of the log data. AbnormalLog is comprised of four functional modules: Log Parsing, Semantic Embedding, Parameter Anomaly Detection and Template Anomaly Detection. We compare the proposed method to three most commonly used log anomaly detection methods in industry. The results demonstrate that AbnormalLog is superior to the other algorithms with respect to common model evaluation criteria.

## item_id: m_0027

TITLE: The loss landscape of overparameterized neural networks

ABSTRACT: We explore some mathematical features of the loss landscape of overparameterized neural networks.  A priori one might imagine that the loss function looks like a typical function from $\mathbb{R}^n$ to $\mathbb{R}$ - in particular, nonconvex, with discrete global minima.  In this paper, we prove that in at least one important way, the loss function of an overparameterized neural network does not look like a typical function.  If a neural net has $n$ parameters and is trained on $d$ data points, with $n>d$, we show that the locus $M$ of global minima of $L$ is usually not discrete, but rather an $n-d$ dimensional submanifold of $\mathbb{R}^n$.  In practice, neural nets commonly have orders of magnitude more parameters than data points, so this observation implies that $M$ is typically a very high-dimensional subset of $\mathbb{R}^n$. 

## item_id: m_0028

TITLE: LOGOS: Precision Retrieval via Logical Document Graphs for Retrieval-Augmented Generation

ABSTRACT: Retrieval-Augmented Generation (RAG) systems struggle with long documents because conventional retrieval methods provide noisy, page-level context that degrades generation quality. These methods are fundamentally limited by treating documents as a linear sequence of pages, which breaks the crucial logical dependencies—like tables, paragraphs, or references—that span across page boundaries. To overcome this limitation, we propose Precision Retrieval via Logical Document Graphs for Retrieval-Augmented Generation (LOGOS), a new RAG method that achieves precision retrieval by modeling a document's intrinsic logical structure. LOGOS transforms a document into a graph where semantic regions are nodes and logical connections are edges, effectively bridging page breaks. A Graph Neural Network then generates fine-grained, context-aware representations for each node, enabling a more concise and semantically relevant context for the generator. Extensive experiments on the ViDoRe and MMDOCIR benchmarks show that LOGOS sets a new state-of-the-art, significantly outperforming strong baselines by up to 2\%  in average Recall@1.

## item_id: m_0029

TITLE: Learning deep representations by mutual information estimation and maximization

ABSTRACT: This work investigates unsupervised learning of representations by maximizing mutual information between an input and the output of a deep neural network encoder. Importantly, we show that structure matters: incorporating knowledge about locality in the input into the objective can significantly improve a representation's suitability for downstream tasks. We further control characteristics of the representation by matching to a prior distribution adversarially. Our method, which we call Deep InfoMax (DIM), outperforms a number of popular unsupervised learning methods and compares favorably with fully-supervised learning on several classification tasks in with some standard architectures. DIM opens new avenues for unsupervised learning of representations and is an important step towards flexible formulations of representation learning objectives for specific end-goals.

## item_id: m_0030

TITLE: Neural Non-additive Utility Aggregation

ABSTRACT: Neural architectures for set regression problems aim at learning representations such that good predictions can be made based on the learned representations. This strategy, however, ignores the fact that meaningful intermediate results might be helpful to perform well. We study two new architectures that explicitly model latent intermediate utilities and use non-additive utility aggregation to estimate the set utility based on the latent utilities. We evaluate the new architectures with visual and textual datasets, which have non-additive set utilities due to redundancy and synergy effects. We find that the new architectures perform substantially better in this setup.

## item_id: m_0031

TITLE: Multilevel Generative Samplers for Investigating Critical Phenomena

ABSTRACT: Investigating critical phenomena or phase transitions is of high interest in physics and chemistry, for which Monte Carlo (MC) simulations, a crucial tool for numerically analyzing macroscopic properties of given systems, are often hindered by an emerging divergence of correlation length---known as scale invariance at criticality (SIC) in the renormalization group theory.  SIC causes the system to behave the same at any length scale, from which many existing sampling methods suffer: long-range correlations cause critical slowing down in Markov chain Monte Carlo (MCMC), and require intractably large receptive fields for generative samplers. In this paper, we propose a Renormalization-informed Generative Critical Sampler (RiGCS)---a novel sampler specialized for near-critical systems, where SIC is leveraged as an advantage rather than a nuisance. Specifically, RiGCS builds on MultiLevel Monte Carlo (MLMC) with Heat Bath (HB) algorithms, which perform ancestral sampling from low-resolution to high-resolution lattice configurations with site wise-independent conditional HB sampling.  Although MLMC-HB is highly efficient under exact SIC, it suffers from a low acceptance rate under slight SIC violation. Notably, SIC violation always occurs in finite-size systems, and may induce long-range and higher-order interactions in the renormalized distributions, which are not considered by independent HB samplers.  RiGCS enhances MLMC-HB by replacing a part of the conditional HB sampler with generative models that capture those residual interactions and improve the sampling efficiency. Our experiments show that the effective sample size of RiGCS is a few orders of magnitude higher than state-of-the-art generative model baselines in sampling configurations for $128 \times 128$ two-dimensional Ising systems.  SIC also allows us to adopt a specialized sequential training protocol with model transfer, which significantly accelerates training.

## item_id: m_0032

TITLE: Assessing Visually-Continuous Corruption Robustness of Neural Networks Relative to Human Performance

ABSTRACT: While Neural Networks (NNs) have surpassed human accuracy in image classi- fication on ImageNet, they often lack robustness against image corruption, i.e., corruption robustness. Yet such robustness is seemingly effortless for human perception. In this paper, we propose visually-continuous corruption robustness (VCR) – an extension of corruption robustness to allow assessing it over the wide and continuous range of changes that correspond to the human perceptive quality (i.e., from the original image to the full distortion of all perceived visual information), along with two novel human-aware metrics for NN evaluation. To compare VCR of NNs with human perception, we conducted extensive experiments on 14 commonly used image corruptions with 7,718 human participants and state-of-the-art robust NN models with different training objectives (e.g., standard, adversarial, corruption robustness), different architectures (e.g., convolution NNs, vision transformers), and different amounts of training data augmentation.
Our study showed that: 1) assessing robustness against continuous corruption can reveal insufficient robustness undetected by existing benchmarks; as a result, 2) the gap between NN and human robustness is larger than previously known; and finally, 3) some image corruptions have a similar impact on human perception, offering opportunities for more cost-effective robustness assessments. Our validation set with 14 image corruptions, human robustness data, and the evaluation code is provided as a toolbox and a benchmark.

## item_id: m_0033

TITLE: LLM Spark: Critical Thinking Evaluation of Large Language Models

ABSTRACT: Large language models (LLMs) excel in complex tasks but often struggle with
inconsistencies in problem framing, a critical skill for real-world scenarios. This
paper introduces SPARK, a novel evaluation framework grounded in the Hierar-
chical Three-Space Theory, to assess LLMs’ ability to identify missing informa-
tion and challenge flawed problem setups. We propose a general framework to
create benchmarks by introducing inconsistencies and misleading cues in diverse
question-answering datasets, covering mathematics, science, and reading compre-
hension. To assist with robust measuring of critical thinking, we employ two key
metrics: problem-solving capability rate and challenge rate. Our experiments with
state-of-the-art LLMs reveal their limitations in critical thinking, particularly in
recognizing inconsistencies. We also explore mitigation strategies, such as modi-
fied prompting and targeted fine-tuning. Furthermore, we conduct comprehensive
experiments to investigate how model and problem properties influence critical
thinking capabilities in LLMs.

## item_id: m_0034

TITLE: Efficient Controllable Generation with Guarantee

ABSTRACT: Generative models have achieved great success in image synthesis, and controllability of the generative process is a key requirement for their successful adoption in real-world applications. Most existing methods for controllable generation lack theoretical guarantees and are time-consuming, which weakens their reliability and applicability. In this paper, we propose an identifiability theorem to provide a guarantee of controllability. This theorem ensures that semantic attributes can be disentangled and hence independently controlled by orthogonalization in latent space in a supervised manner. Based on the theoretical analysis, we propose a general method for controllable generation, which can be integrated with most latent-variable generative models. We further propose to plug it into a pre-trained NVAE. Such a scheme significantly reduces the cost of time and has better consistency in image editing due to the merits of NVAE. Experiments show that our method is comparable with the state-of-the-art methods in attribute-conditional generation and image editing, and has advantages in efficiency and consistency.

## item_id: m_0035

TITLE: Uncovering Model Vulnerabilities With Multi-Turn Red Teaming

ABSTRACT: Recent large language model (LLM) defenses have greatly improved models' ability to refuse harmful queries, even when adversarially attacked. However, LLM defenses are primarily evaluated against automated adversarial attacks in a single turn of conversation, an insufficient threat model for real-world malicious use. We demonstrate that multi-turn human jailbreaks uncover significant vulnerabilities, exceeding 70% attack success rate (ASR) on HarmBench against defenses that report single-digit ASRs with automated single-turn attacks. Human jailbreaks also reveal vulnerabilities in machine unlearning defenses, successfully recovering dual-use biosecurity knowledge from unlearned models. We compile these results into Multi-Turn Human Jailbreaks (MHJ), a dataset of 2,912 prompts across 537 multi-turn jailbreaks. We publicly release MHJ alongside a compendium of jailbreak tactics developed across dozens of commercial red teaming engagements, supporting research towards stronger LLM defenses.

## item_id: m_0036

TITLE: Bridging Fairness and Explainability: Can Input-Based Explanations Promote Fairness in Hate Speech Detection?

ABSTRACT: Natural language processing (NLP) models often replicate or amplify social bias from training data, raising concerns about fairness.
At the same time, their black-box nature makes it difficult for users to recognize biased predictions and for developers to effectively mitigate them.
While some studies suggest that input-based explanations can help detect and mitigate bias, others question their reliability in ensuring fairness.
Existing research on explainability in fair NLP has been predominantly qualitative, with limited large-scale quantitative analysis.
In this work, we conduct the first systematic study of the relationship between explainability and fairness in hate speech detection, focusing on both encoder- and decoder-only models.
We examine three key dimensions: (1) identifying biased predictions, (2) selecting fair models, and (3) mitigating bias during model training.
Our findings show that input-based explanations can effectively detect biased predictions and serve as useful supervision for reducing bias during training, but they are unreliable for selecting fair models among candidates.
Our code is available at https://github.com/Ewanwong/fairness_x_explainability.

## item_id: m_0037

TITLE: Disentangling Trainability and Generalization in Deep Learning

ABSTRACT: A fundamental goal in deep learning is the characterization of trainability and generalization of neural networks as a function of their architecture and hyperparameters. In this paper, we discuss these challenging issues in the context of wide neural networks at large depths where we will see that the situation simplifies considerably. To do this, we leverage recent advances that have separately shown: (1) that in the wide network limit, random networks before training are Gaussian Processes governed by a kernel known as the Neural Network Gaussian Process (NNGP) kernel, (2) that at large depths the spectrum of the NNGP kernel simplifies considerably and becomes ``weakly data-dependent'', and (3) that gradient descent training of wide neural networks is described by a kernel called the Neural Tangent Kernel (NTK) that is related to the NNGP. Here we show that by combining the in the large depth limit the spectrum of the NTK simplifies in much the same way as that of the NNGP kernel. By analyzing this spectrum, we arrive at a precise characterization of trainability and generalization across a range of architectures including Fully Connected Networks (FCNs) and Convolutional Neural Networks (CNNs). We find that there are large regions of hyperparameter space where networks will train but will fail to generalize, in contrast with several recent results. By comparing CNNs with- and without-global average pooling, we show that CNNs without average pooling have very nearly identical learning dynamics to FCNs while CNNs with pooling contain a correction that alters its generalization performance. We perform a thorough empirical investigation of these theoretical results and finding excellent agreement on real datasets.

## item_id: m_0038

TITLE: EMTL: A Generative Domain Adaptation Approach

ABSTRACT: We propose an unsupervised domain adaptation approach based on generative models. We show that when the source probability density function can be learned, one-step Expectation–Maximization iteration plus an additional marginal density function constraint will produce a proper mediator probability density function to bridge the gap between the source and target domains. The breakthrough is based on modern generative models (autoregressive mixture density nets) that are competitive to discriminative models on moderate-dimensional classification problems. By decoupling the source density estimation from the adaption steps, we can design a domain adaptation approach where the source data is locked away after being processed only once, opening the door to transfer when data security or privacy concerns impede the use of traditional domain adaptation. We demonstrate that our approach can achieve state-of-the-art performance on synthetic and real data sets, without accessing the source data at the adaptation phase.

## item_id: m_0039

TITLE: Talking Turns: Benchmarking Audio Foundation Models on Turn-Taking Dynamics

ABSTRACT: The recent wave of audio foundation models (FMs) could provide new capabilities for conversational modeling. However, there have been limited efforts to evaluate these audio FMs comprehensively on their ability to have natural and interactive conversations. To engage in meaningful conversation with the end user, we would want the FMs to additionally perform a fluent succession of turns without too much overlapping speech or long stretches of silence. Inspired by this, we ask whether the recently proposed audio FMs can understand, predict, and perform turn-taking events? To answer this, we propose a novel evaluation protocol that can assess spoken dialog system's turn-taking capabilities using a supervised model as a judge that has been trained to predict turn-taking events in human-human conversations. Using this protocol, we present the first comprehensive user study that evaluates existing spoken dialogue systems on their ability to perform turn-taking events and reveal many interesting insights, such as they sometimes do not understand when to speak up, can interrupt too aggressively and rarely backchannel. We further evaluate multiple open-source and proprietary audio FMs accessible through APIs on carefully curated test benchmarks from Switchboard to measure their ability to understand and predict turn-taking events and identify significant room for improvement. We will open source our evaluation platform to promote the development of advanced conversational AI systems.

## item_id: m_0040

TITLE: Uncertainty-based out-of-distribution detection requires suitable function space priors

ABSTRACT: The need to avoid confident predictions on unfamiliar data has sparked interest in out-of-distribution (OOD) detection. It is widely assumed that Bayesian neural networks (BNNs) are well suited for this task, as the endowed epistemic uncertainty should lead to disagreement in predictions on outliers. In this paper, we question this assumption and show that proper Bayesian inference with function space priors induced by neural networks does not necessarily lead to good OOD detection. To circumvent the use of approximate inference, we start by studying the infinite-width case, where Bayesian inference can be exact due to the correspondence with Gaussian processes. Strikingly, the kernels induced under common architectural choices lead to uncertainties that do not reflect the underlying data generating process and are therefore unsuited for OOD detection. Importantly, we find this OOD behavior to be consistent with the corresponding finite-width networks. Desirable function space properties can be encoded in the prior in weight space, however, this currently only applies to a specified subset of the domain and thus does not inherently extend to OOD data.  Finally, we argue that a trade-off between generalization and OOD capabilities might render the application of BNNs for OOD detection undesirable in practice. Overall, our study discloses fundamental problems when naively using BNNs for OOD detection and opens interesting avenues for future research.

## item_id: m_0041

TITLE: Multi-Policy Pareto Front Tracking Based Multi-Objective Reinforcement Learning

ABSTRACT: Multi-objective reinforcement learning (MORL) plays a pivotal role in addressing multi-criteria decision-making problems in the real world. The multi-policy
(MP)-based approaches are widely used to obtain high-quality Pareto front approximations for the MORL problems. Relying primarily on the online reinforcement learning (RL), the traditional MP approaches usually adopt the evolutionary
framework that requires maintaining a large policy population. In practice, however, this often leads to sample inefficiency and/or excessive agent-environment
interactions. To address these issues, we propose the novel Multi-policy Pareto
Front Tracking (MPFT) framework that eliminates the need to maintain any policy population, compatible with both online and offline MORL algorithms. The
proposed MPFT framework comprises four stages: Stage 1 approximates all the
Pareto-vertex policies whose mappings to the objective space lie on the vertices
of the Pareto front; Stage 2 proposes a new Pareto tracking mechanism that starts
from each Pareto-vertex policy to track the Pareto front, where a proof of its exponential convergence is provided; Stage 3 identifies the sparse regions in the tracked
Pareto front, and then newly designs an objective weight adjustment method to facilitate the policy tracking for filling these regions; Finally, by combining all the
policies tracked in Stages 2 and 3, Stage 4 approximates the complete Pareto front.
Experiments are conducted on seven continuous-action robotic control tasks using
both online and offline MORL algorithms. Results demonstrate that our proposed
MPFT approach outperforms state-of-the-art benchmarks in terms of hypervolume and expected utility performances, while significantly reducing the agentenvironment interactions.

## item_id: m_0042

TITLE: GANSynth: Adversarial Neural Audio Synthesis

ABSTRACT: Efficient audio synthesis is an inherently difficult machine learning task, as human perception is sensitive to both global structure and fine-scale waveform coherence. Autoregressive models, such as WaveNet, model local structure at the expense of global latent structure and slow iterative sampling, while Generative Adversarial Networks (GANs), have global latent conditioning and efficient parallel sampling, but struggle to generate locally-coherent audio waveforms. Herein, we demonstrate that GANs can in fact generate high-fidelity and locally-coherent audio by modeling log magnitudes and instantaneous frequencies  with sufficient frequency resolution in the spectral domain. Through extensive empirical investigations on the NSynth dataset, we demonstrate that GANs are able to outperform strong WaveNet baselines on automated and human evaluation metrics, and efficiently generate audio several orders of magnitude faster than their autoregressive counterparts.


## item_id: m_0043

TITLE: ChartReasoner: Code-Driven Modality Bridging for Long-Chain Reasoning in Chart Question Answering

ABSTRACT: Recently, large language models have shown remarkable reasoning capabilities through long-chain reasoning before responding. However, how to extend this capability to visual reasoning tasks remains an open challenge. Existing multimodal reasoning approaches transfer such visual reasoning task into textual reasoning task via several image-to-text conversions, which often lose critical structural and semantic information embedded in visualizations, especially for tasks like chart question answering that require a large amount of visual details. To bridge this gap, we propose ChartReasoner, a code-driven novel two-stage framework designed to enable precise, interpretable reasoning over charts. We first train a high-fidelity model to convert diverse chart images into structured ECharts codes, preserving both layout and data semantics as lossless as possible. Then, we design a general chart reasoning data synthesis pipeline, which leverages this pretrained transport model to automatically and scalably generate chart reasoning trajectories and utilizes a code validator to filter out low-quality samples. Finally, we train the final multimodal model using a combination of supervised fine-tuning and reinforcement learning on our synthesized chart reasoning dataset and experimental results on four public benchmarks clearly demonstrate the effectiveness of our proposed ChartReasoner. It can preserve the original details of the charts as much as possible and perform comparably with state-of-the-art open-source models while using fewer parameters, approaching the performance of proprietary systems like GPT-4o in out-of-domain settings.

## item_id: m_0044

TITLE: CERTIFIED VS. EMPIRICAL ADVERSARIAL ROBUSTNESS VIA HYBRID CONVOLUTIONS WITH ATTENTION STOCHASTICITY

ABSTRACT: We introduce Hybrid Convolutions with Attention Stochasticity (HyCAS), an adversarial defense that narrows the long-standing gap between provable robustness under ℓ2 certificates and empirical robustness against strong ℓ∞ attacks, while preserving strong generalization across diverse imaging benchmarks. HyCAS unifies deterministic and randomized principles by coupling 1-Lipschitz, spectrally normalized convolutions with two stochastic components—spectral normalized random-projection filters and a randomized attention-noise mechanism—to realize a randomized defense. Injecting smoothing randomness inside the architecture yields an overall ≤ 2-Lipschitz network with formal certificates. Extensive experiments on diverse imaging benchmarks—including CIFAR-10/100, ImageNet-1k, NIH Chest X-ray, HAM10000—show that HyCAS surpasses prior leading certified and empirical defenses, boosting certified accuracy by up to ≈ 7.3% (on NIH Chest X-ray) and empirical robustness by up to ≈ 3.1% (on HAM10000), without sacrificing clean accuracy. These results show that a randomized Lipschitz constrained architecture can simultaneously improve both certified ℓ2 and empirical ℓ∞ adversarial robustness, thereby supporting safer deployment of deep models in high-stakes applications.

## item_id: m_0045

TITLE: Self-Normalized Resets for Plasticity in Continual Learning

ABSTRACT: Plasticity Loss is an increasingly important phenomenon that refers to the empirical observation that as a neural network is continually trained on a sequence of changing tasks, its ability to adapt to a new task diminishes over time. We introduce Self-Normalized Resets (SNR), a simple adaptive algorithm that mitigates plasticity loss by resetting a neuron’s weights when evidence suggests its firing rate has effectively dropped to zero. Across a battery of continual learning problems and network architectures, we demonstrate that SNR consistently attains superior performance compared to its competitor algorithms. We also demonstrate that SNR is robust to its sole hyperparameter, its rejection percentile threshold, while competitor algorithms show significant sensitivity. SNR’s threshold-based reset mechanism is motivated by a simple hypothesis test we derive. Seen through the lens of this hypothesis test, competing reset proposals yield suboptimal error rates in correctly detecting inactive neurons, potentially explaining our experimental observations. We also conduct a theoretical investigation of the optimization landscape for the problem of learning a single ReLU. We show that even when initialized adversarially, an idealized version of SNR learns the target ReLU, while regularization based approaches can fail to learn.

## item_id: m_0046

TITLE: Benchmarking Ethics in Text-to-Image Models: A Holistic Dataset and Evaluator for Fairness, Toxicity, and Privacy

ABSTRACT: Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models raise significant ethical concerns, including the risk of generating harmful, biased, or private content. Existing safety benchmarks are limited in scope, lacking comprehensive coverage of critical ethical aspects such as detailed categories of toxicity, privacy, and fairness, and often rely on inadequate evaluation techniques. To address these gaps, we introduce T2IEthics, a comprehensive benchmark that rigorously evaluates T2I models across three key ethical dimensions: fairness, toxicity, and privacy. Additionally, we propose ImageGuard, a multimodal large language model-based evaluator designed for more accurate and nuanced ethical assessments. It significantly outperforms existing models including GPT-4o across all ethical dimensions. Using this benchmark, we evaluate 12 diffusion models, including popular models from the Stable Diffusion series. Our results indicate persistent issues with racial fairness, a tendency to generate toxic content, and significant variation in privacy protection among the models even when defense methods like concept erasing are employed.

## item_id: m_0047

TITLE: MT-GBM: A Multi-Task Gradient Boosting Machine  with Shared Decision Trees

ABSTRACT: Despite the success of deep learning in computer vision and natural language processing, Gradient Boosted Decision Tree (GBDT) is yet one of the most powerful tools for applications with tabular data such as e-commerce and FinTech. However, applying GBDT to multi-task learning is still a challenge. Unlike deep models that can jointly learn a shared latent representation across multiple tasks, GBDT can hardly learn a shared tree structure.

In this paper, we propose Multi-Task Gradient Boosting Machine (MT-GBM), a GBDT-based method for multi-task learning. The MT-GBM can find the shared tree structures and split branches according to multi-task losses. First, it assigns multiple outputs to each leaf node. Next, it computes the gradient corresponding to each output (task). Then, we also propose an algorithm to combine the gradients of all tasks and update the tree. Finally, we apply MT-GBM to LightGBM. Experiments show that our MT-GBM improves the performance of the main task significantly, which means the proposed MT-GBM is efficient and effective.

## item_id: m_0048

TITLE: Incremental few-shot learning via vector quantization in deep embedded space

ABSTRACT: The capability of incrementally learning new tasks without forgetting old ones is a challenging problem due to catastrophic forgetting. This challenge becomes greater when novel tasks contain very few labelled training samples. Currently, most methods are dedicated to class-incremental learning and rely on sufficient training data to learn additional weights for newly added classes. Those methods cannot be easily extended to incremental regression tasks and could suffer from severe overfitting when learning few-shot novel tasks. In this study, we propose a nonparametric method in deep embedded space to tackle incremental few-shot learning problems. The knowledge about the learned tasks are compressed into a small number of quantized reference vectors. The proposed method learns new tasks sequentially by adding more reference vectors to the model using few-shot samples in each novel task. For classification problems, we employ the nearest neighbor scheme to make classification on sparsely available data and incorporate intra-class variation, less forgetting regularization and calibration of reference vectors to mitigate catastrophic forgetting. In addition, the proposed learning vector quantization (LVQ) in deep embedded space can be customized as a kernel smoother to handle incremental few-shot regression tasks. Experimental results demonstrate that the proposed method outperforms other state-of-the-art methods in incremental learning.

## item_id: m_0049

TITLE: CAN AI GENERATE LOVE ADVICE?: TOWARD NEURAL ANSWER GENERATION FOR NON-FACTOID QUESTIONS

ABSTRACT: 
Deep learning methods that extract answers for non-factoid questions from QA sites are seen as critical since they can assist users in reaching their next decisions through conversations with AI systems. The current methods, however, have the following two problems: (1) They can not understand the ambiguous use of words in the questions as word usage can strongly depend on the context (e.g. the word “relationship” has quite different meanings in the categories of Love advice and other categories). As a result, the accuracies of their answer selections are not good enough. (2) The current methods can only select from among the answers held by QA sites and can not generate new ones. Thus, they can not answer the questions that are somewhat different with those stored in QA sites. Our solution, Neural Answer Construction Model, tackles these problems as it: (1) Incorporates the biases of semantics behind questions (e.g. categories assigned to questions) into word embeddings while also computing them regardless of the semantics. As a result, it can extract answers that suit the contexts of words used in the question as well as following the common usage of words across semantics. This improves the accuracy of answer selection. (2) Uses biLSTM to compute the embeddings of questions as well as those of the sentences often used to form answers (e.g. sentences representing conclusions or those supplementing the conclusions). It then simultaneously learns the optimum combination of those sentences as well as the closeness between the question and those sentences. As a result, our model can construct an answer that corresponds to the situation that underlies the question; it fills the gap between answer selection and generation and is the first model to move beyond the current simple answer selection model for non-factoid QAs. Evaluations using datasets created for love advice stored in the Japanese QA site, Oshiete goo, indicate that our model achieves 20 % higher accuracy in answer creation than the strong baselines. Our model is practical and has already been applied to the love advice service in Oshiete goo.

## item_id: m_0050

TITLE: Causal Abstraction Finds Universal Representation of Race in Large Language Models

ABSTRACT: While there is growing interest in the potential bias of large language models (LLMs), especially in high-stakes decision making, it remains an open question how LLMs mechanistically encode such bias. We use causal abstraction (Geiger et al., 2023) to study how models use the race information in two high-stakes decision settings: college admissions and hiring. We find that Alpaca 7B, Mistral 7B, and Gemma 2B check for an applicants’ race and apply different preferential or discriminatory decision boundaries. The race subspace found by distributed alignment search generalizes across different tasks with average interchange intervention accuracies from 78.09% to 88.64% across the three models. We also propose a novel RaceQA task, where the model is asked to guess an applicant’s race from the name in their profile, to further probe the mechanism of the bias. We show that patching in a different race representation changes the model’s perception of the applicant’s race 99.80% of the time for Alpaca and 98.20% of the time for Mistral. Overall, our work provides evidence for a universal mechanism of racial bias in LLMs’ decision-making.

## item_id: m_0051

TITLE: GSmooth: Certified Robustness against Semantic Transformations via Generalized Randomized Smoothing

ABSTRACT: The vulnerability of deep learning models to adversarial examples and semantic transformations has limited the applications in risk-sensitive areas. The recent development of certified defense approaches like randomized smoothing provides a promising direction towards building reliable machine learning systems. However, current certified defenses cannot handle complex semantic transformations like rotational blur and defocus blur which are common in practical applications. In this paper, we propose a generalized randomized smoothing framework (GSmooth) for certified robustness against semantic transformations. We provide both a unified and rigorous theoretical framework and scalable algorithms for certified robustness on complex semantic transformations. Specifically, our key idea is to use a surrogate image-to-image neural network to approximate a transformation which provides a powerful tool for studying the properties of semantic transformations and certify the transformation based on this neural network. Experiments on multiple types of semantic perturbations and corruptions using multiple datasets demonstrate the effectiveness of our approach.

## item_id: m_0052

TITLE: An object-centric sensitivity analysis of deep learning based instance segmentation

ABSTRACT: In this study we establish a comprehensive baseline regarding the object-centric robustness of deep learning models for instance segmentation. Our approach is motivated by the work of Geirhos et al. (2019) on texture bias in CNNs. However, we do not compare against human performance but instead incorporate ideas from object-centric representation learning. In addition, we analyze and control the effect of strong stylization that can lead to disappearing objects. The result is a stylized and object-centric version of MS COCO on which we perform an extensive sensitivity analysis regarding visual feature corruptions. We evaluate a broad range of frameworks including Cascade and Mask R-CNN, Swin Transformer, YOLACT(++), DETR, SOTR and SOLOv2. We find that framework choice, data augmentation and dynamic architectures improve robustness whereas supervised and self supervised pre-training does surprisingly not. In summary we evaluate 63 models on 61 versions of COCO for a total of 3843 evaluations.

## item_id: m_0053

TITLE: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks

ABSTRACT: Large language models (LLMs) have achieved remarkable performance in various evaluation benchmarks. However, concerns are raised about potential data contamination in their considerable volume of training corpus. Moreover, the static nature and fixed complexity of current benchmarks may inadequately gauge the advancing capabilities of LLMs. 
In this paper, we introduce DyVal, a general and flexible protocol for dynamic evaluation of LLMs. Based on our framework, we build graph-informed DyVal by leveraging the structural advantage of directed acyclic graphs to dynamically generate evaluation samples with controllable complexities. DyVal generates challenging evaluation sets on reasoning tasks including mathematics, logical reasoning, and algorithm problems. We evaluate various LLMs ranging from Flan-T5-large to GPT-3.5-Turbo and GPT-4. Experiments show that LLMs perform worse in DyVal-generated evaluation samples with different complexities, highlighting the significance of dynamic evaluation.
We also analyze the failure cases and results of different prompting methods.
Moreover, DyVal-generated samples are not only evaluation sets, but also helpful data for fine-tuning to improve the performance of LLMs on existing benchmarks.
We hope that DyVal can shed light on future evaluation research of LLMs. Code is available at: https://github.com/microsoft/promptbench.

## item_id: m_0054

TITLE: Causal Generative Neural Networks

ABSTRACT: We introduce CGNN, a framework to learn functional causal models as generative neural networks. These networks are trained using backpropagation to minimize the maximum mean discrepancy to the observed data. Unlike previous approaches, CGNN leverages both conditional independences and distributional asymmetries to seamlessly discover bivariate and multivariate 
 causal structures, with or without hidden variables. CGNN does not only estimate the causal structure, but a full and differentiable generative model of the data. Throughout an extensive variety of experiments, we illustrate the competitive  esults of CGNN w.r.t state-of-the-art alternatives in observational causal discovery on both simulated and real data, in the tasks of cause-effect inference, v-structure identification, and multivariate causal discovery. 

## item_id: m_0055

TITLE: Evaluation of Defensive Methods for DNNs against Multiple Adversarial Evasion Models

ABSTRACT: Due to deep cascades of nonlinear units, deep neural networks (DNNs) can automatically learn non-local generalization priors from data and have achieved high performance in various applications.
However, such properties have also opened a door for adversaries to generate the so-called adversarial examples to fool DNNs. Specifically, adversaries can inject small perturbations to the input data and therefore decrease the performance of deep neural networks significantly.
Even worse, these adversarial examples have the transferability to attack a black-box model based on finite queries without knowledge of the target model. 
Therefore, we aim to empirically compare different defensive strategies against various adversary models and analyze the cross-model efficiency for these robust learners. We conclude that the adversarial retraining framework also has the transferability, which can defend adversarial examples without requiring prior knowledge of the adversary models.
We compare the general adversarial retraining framework with the state-of-the-art robust deep neural networks, such as distillation, autoencoder stacked with classifier (AEC), and our improved version, IAEC, to evaluate their robustness as well as the vulnerability in terms of the distortion required to mislead the learner.
Our experimental results show that the adversarial retraining framework can defend most of the adversarial examples notably and consistently without adding additional
vulnerabilities or performance penalty to the original model.

## item_id: m_0056

TITLE: Tradeoffs Between Alignment and Helpfulness in Language Models with Representation Engineering

ABSTRACT: Language model alignment has become an important component of AI safety, allowing safe interactions between humans and language models, by enhancing desired behaviors and inhibiting undesired ones. It is often done by tuning the model or inserting preset aligning prompts. Recently, representation engineering, a method which alters the model’s behavior via changing its representations post-training, was shown to be effective in aligning LLMs (Zou et al., 2023a). Representation engineering yields gains in alignment oriented tasks such as resistance to adversarial attacks and reduction of social biases, but was also shown to cause a decrease in the ability of the model to perform basic tasks. In this paper we study the tradeoff between the increase in alignment and decrease in helpfulness of the model. We propose a theoretical framework which provides bounds for these two quantities, and demonstrate their relevance empirically. First, we find that under the conditions of our framework, alignment can be guaranteed with representation engineering, and at the same time that helpfulness is harmed in the process. Second, we show that helpfulness is harmed quadratically with the norm of the representation engineering vector, while the alignment increases linearly with it, indicating a regime in which it is efficient to use representation engineering. We validate our findings empirically, and chart the boundaries to the usefulness of representation engineering for alignment.

## item_id: m_0057

TITLE: On the Minimal Supervision for Training Any Binary Classifier from Only Unlabeled Data

ABSTRACT: Empirical risk minimization (ERM), with proper loss function and regularization, is the common practice of supervised classification. In this paper, we study training arbitrary (from linear to deep) binary classifier from only unlabeled (U) data by ERM. We prove that it is impossible to estimate the risk of an arbitrary binary classifier in an unbiased manner given a single set of U data, but it becomes possible given two sets of U data with different class priors. These two facts answer a fundamental question---what the minimal supervision is for training any binary classifier from only U data. Following these findings, we propose an ERM-based learning method from two sets of U data, and then prove it is consistent. Experiments demonstrate the proposed method could train deep models and outperform state-of-the-art methods for learning from two sets of U data.

## item_id: m_0058

TITLE: Intrinsically Guided Exploration in Meta Reinforcement Learning

ABSTRACT: Deep reinforcement learning algorithms generally require large amounts of data to solve a single task. Meta reinforcement learning (meta-RL) agents learn to adapt to novel unseen tasks with high sample efficiency by extracting useful prior knowledge from previous tasks. Despite recent progress, efficient exploration in meta-training and adaptation remains a key challenge in sparse-reward meta-RL tasks. We propose a novel off-policy meta-RL algorithm to address this problem, which disentangles exploration and exploitation policies and learns intrinsically motivated exploration behaviors. We design novel intrinsic rewards derived from information gain to reduce task uncertainty and encourage the explorer to collect informative trajectories about the current task. Experimental evaluation shows that our algorithm achieves state-of-the-art performance on various sparse-reward MuJoCo locomotion tasks and more complex Meta-World tasks.

## item_id: m_0059

TITLE: Probabilistic Semantic Embedding

ABSTRACT: We present an extension of a variational auto-encoder that creates semantically richcoupled probabilistic latent representations that capture the semantics of multiplemodalities of data. We demonstrate this model through experiments using imagesand textual descriptors as inputs and images as outputs. Our latent representationsare not only capable of driving a decoder to generate novel data, but can also be useddirectly for annotation or classification. Using the MNIST and Fashion-MNISTdatasets we show that the embedding not only provides better reconstruction andclassification performance than the current state-of-the-art, but it also allows us toexploit the semantic content of the pretrained word embedding spaces to do taskssuch as image generation from labels outside of those seen during training.

## item_id: m_0060

TITLE: Investigating Recurrence and Eligibility Traces in Deep Q-Networks

ABSTRACT: Eligibility traces in reinforcement learning are used as a bias-variance trade-off and can often speed up training time by propagating knowledge back over time-steps in a single update. We investigate the use of eligibility traces in combination with recurrent networks in the Atari domain.  We illustrate the benefits of both recurrent nets and eligibility traces in some Atari games, and highlight also the importance of the optimization used in the training.

## item_id: m_0061

TITLE: Eidetic 3D LSTM: A Model for Video Prediction and Beyond

ABSTRACT: Spatiotemporal predictive learning, though long considered to be a promising self-supervised feature learning method, seldom shows its effectiveness beyond future video prediction. The reason is that it is difficult to learn good representations for both short-term frame dependency and long-term high-level relations. We present a new model, Eidetic 3D LSTM (E3D-LSTM), that integrates 3D convolutions into RNNs. The encapsulated 3D-Conv makes local perceptrons of RNNs motion-aware and enables the memory cell to store better short-term features. For long-term relations, we make the present memory state interact with its historical records via a gate-controlled self-attention module. We describe this memory transition mechanism eidetic as it is able to effectively recall the stored memories across multiple time stamps even after long periods of disturbance. We first evaluate the E3D-LSTM network on widely-used future video prediction datasets and achieve the state-of-the-art performance. Then we show that the E3D-LSTM network also performs well on the early activity recognition to infer what is happening or what will happen after observing only limited frames of video. This task aligns well with video prediction in modeling action intentions and tendency.

## item_id: m_0062

TITLE: Fine-Grained Image Retrieval with Neighbor-Attention Label Correction

ABSTRACT: This paper studies noise-resistant deep model training for the fine-grained image retrieval task, which has a unconstrained target label space and suffers from the difficulty of acquiring accurate fine-grained labels. A Neighbor-Attention Label Correction (NALC) model is proposed based on the meta-learning framework to correct labels during the training stage. A training batch and a validation batch are sampled from the training set, which hence allows to optimize the NALC model by referring to the validation batch. We also propose a novel nested optimization for the meta-learning framework to enhance the optimization efficiency. The training procedure consistently boosts the label accuracy in training batch, which in-turn ensures a more accurate training set. Experiments results show that our method boosts the label accuracy from 70% to 97+% and it outperforms recent works up to 11.5% in rank1 accuracy on various fine-grained image retrieval tasks, e.g., fine-grained instance retrieval on CUB200 and CARS, as well as person re-identification, respectively. Ablation studies also show the NALC generalizes well on different types of noises, e.g., Asymmetric, Pair-Flip, Pattern noises, etc.

## item_id: m_0063

TITLE: Regularizing Neural Networks by Penalizing Confident Output Distributions

ABSTRACT: We propose regularizing neural networks by penalizing low entropy output distributions. We show that penalizing low entropy output distributions, which has been shown to improve exploration in reinforcement learning, acts as a strong regularizer in supervised learning. We connect our confidence penalty to label smoothing through the direction of the KL divergence between networks output distribution and the uniform distribution. We exhaustively evaluate our proposed confidence penalty and label smoothing (uniform and unigram) on 6 common benchmarks: image classification (MNIST and Cifar-10), language modeling (Penn Treebank), machine translation (WMT'14 English-to-German), and speech recognition (TIMIT and WSJ). We find that both label smoothing and our confidence penalty improve state-of-the-art models across benchmarks without modifying existing hyper-parameters.


## item_id: m_0064

TITLE: Learning Rotation-Equivariant Features for Visual Correspondence

ABSTRACT: Extracting discriminative local features that are invariant to imaging variations is an integral part of establishing correspondences between images. In this work, we introduce a self-supervised learning framework to extract discriminative rotation-invariant descriptors using group-equivariant CNNs. Thanks to employing group-equivariant CNNs, our method effectively learns to obtain rotation-equivariant features and their orientations explicitly, without having to perform sophisticated data augmentations. The resultant features and their orientations are further processed by group aligning, a novel invariant mapping technique that shifts the group-equivariant features by their orientations along the group dimension. Our group aligning technique achieves rotation-invariance without any collapse of the group dimension and thus eschews loss of discriminability. The proposed method is trained end-to-end in a self-supervised manner, where we use an orientation alignment loss for the orientation estimation and a contrastive descriptor loss for robust local descriptors to geometric/photometric variations. Our method demonstrates state-of-the-art matching accuracy among existing rotation-invariant descriptors under varying rotation and also show competitive results when transferred to the task of keypoint matching and camera pose estimation.

## item_id: m_0065

TITLE: Evolving Alignment via Asymmetric Self-Play

ABSTRACT: Current RLHF approaches for aligning large language models (LLMs) typically assume a fixed prompt distribution, which is sub-optimal and limits the generalization capabilities for language models. To address this issue, we introduce a general framework that casts alignment as an asymmetric game between two players:  (i) a creator, which strategically generates informative prompt distributions using reward signals, and (ii) a solver, which learns to produce preferred responses on prompts produced by the creator.

This framework of Evolving Alignment via Asymmetric Self-Play (`eva`), results in a simple and efficient approach that can utilize any existing RLHF algorithm. `eva` achieves a new state of the art in widely adopted alignment benchmarks, without the need of any additional human crafted prompts, e.g., it can improve the win rate of finetuned gemma-2-9b-it on Arena-Hard from 51.6% to 60.1% with DPO, from 55.7% to 58.9% with SPPO, from 52.3% to 60.7% with SimPO, and from 54.8% to 60.3% with ORPO, surpassing its 27B version and matching Claude-3-opus. Finally, we show `eva` is effective and robust under various ablation settings. 

We hope `eva` can serve as a scalable and easy-to-use methodology for the research community to build open-ended, robust, and self-improving language agents, that align with human values.

## item_id: m_0066

TITLE: Mollifying Networks

ABSTRACT: The optimization of deep neural networks can be more challenging than the traditional convex optimization problems due to highly non-convex nature of the loss function, e.g. it can involve pathological landscapes such as saddle-surfaces that can be difficult to escape from for algorithms based on simple gradient descent. In this paper, we attack the problem of optimization of highly non-convex neural networks objectives by starting with a smoothed -- or mollified -- objective function which becomes more complex as the training proceeds.  Our proposition is inspired by the recent studies in continuation methods: similarly to curriculum methods, we begin by learning an easier (possibly convex) objective function and let it evolve during training until it eventually becomes the original, difficult to optimize objective function. The complexity of the mollified networks is controlled by a single hyperparameter that is annealed during training. We show improvements on various difficult optimization tasks and establish a relationship between recent works on continuation methods for neural networks and mollifiers.


## item_id: m_0067

TITLE: SAMPQ: Saliency-aware Mixed-Precision Quantization

ABSTRACT: Although mixed-precision quantization (MPQ) achieves a remarkable accuracy-complexity trade-off, conventional gradient-based MPQ methods are susceptible to input noise, which leads to suboptimal bit-width allocation strategies. Through saliency analysis, we indicate that treating sample feature regions as equally significant exacerbates the quantization error in MPQ. To mitigate this issue, we propose saliency-aware MPQ (SAMPQ), a novel framework designed to dynamically evaluate the sample saliency. In particular, SAMPQ is formulated as a three-stage cascade-optimized training procedure. At the first stage, the neural network (NN) weights are trained on vanilla samples with its bit-width configuration tentatively fixed. At the second stage, saliency maps are generated by one-step optimized weights. At the third stage, the bit-width allocation is optimized on saliency-reweighted samples while freezing NN weights. By iteratively alternating these optimization phases, SAMPQ enables the quantized NN modules to focus on fine-grained features. Experiments conducted on the benchmark demonstrate the effectiveness of our proposed method within existing MPQ frameworks.

## item_id: m_0068

TITLE: A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale Reconstruction with External Memory

ABSTRACT: Gaussian Splatting has emerged as a high-performance technique for novel view synthesis, enabling real-time rendering and high-quality reconstruction of small scenes. However, scaling to larger environments has so far relied on partitioning the scene into chunks - a strategy that introduces artifacts at chunk boundaries, complicates training across varying scales, and is poorly suited to unstructured scenarios such as city-scale flyovers combined with street-level views. Moreover, rendering remains fundamentally limited by GPU memory, as all visible chunks must reside in VRAM simultaneously.
We introduce A LoD of Gaussians, a framework for training and rendering ultra-large-scale Gaussian scenes on a single consumer-grade GPU - without partitioning. Our method stores the full scene out-of-core (e.g., in CPU memory) and trains a Level-of-Detail (LoD) representation directly, dynamically streaming only the relevant Gaussians. A hybrid data structure combining Gaussian hierarchies with Sequential Point Trees enables efficient, view-dependent LoD selection, while a lightweight caching and view scheduling system exploits temporal coherence to minimize the loading overhead. Together, these innovations enable seamless multi-scale reconstruction and interactive visualization of complex scenes - from broad aerial views to fine-grained ground-level details.

## item_id: m_0069

TITLE: Invariant-equivariant representation learning for multi-class data

ABSTRACT: Representations learnt through deep neural networks tend to be highly informative, but opaque in terms of what information they learn to encode. We introduce an approach to probabilistic modelling that learns to represent data with two separate deep representations: an invariant representation that encodes the information of the class from which the data belongs, and an equivariant representation that encodes the symmetry transformation defining the particular data point within the class manifold (equivariant in the sense that the representation varies naturally with symmetry transformations). This approach to representation learning is conceptually transparent, easy to implement, and in-principle generally applicable to any data comprised of discrete classes of continuous distributions (e.g. objects in images, topics in language, individuals in behavioural data). We demonstrate qualitatively compelling representation learning and competitive quantitative performance, in both supervised and semi-supervised settings, versus comparable modelling approaches in the literature with little fine tuning.

## item_id: m_0070

TITLE: Exploring Curvature Noise in Large-Batch Stochastic Optimization

ABSTRACT: Using stochastic gradient descent (SGD) with large batch-sizes to train deep neural networks is an increasingly popular technique. By doing so, one can improve parallelization by scaling to multiple workers (GPUs) and hence leading to significant reductions in training time. Unfortunately, a major drawback is the so-called generalization gap: large-batch training typically leads to a degradation in generalization performance of the model as compared to small-batch training. In this paper, we propose to correct this generalization gap by adding diagonal Fisher curvature noise to large-batch gradient updates. We provide a theoretical analysis of our method in the convex quadratic setting. Our empirical study with state-of-the-art deep learning models shows that our method not only improves the generalization performance in large-batch training but furthermore, does so in a way where the training convergence remains desirable and the training duration is not elongated. We additionally connect our method to recent works on loss surface landscape in the experimental section. 

## item_id: m_0071

TITLE: Contextual HyperNetworks  for Novel Feature Adaptation

ABSTRACT: While deep learning has obtained state-of-the-art results in many applications, the adaptation of neural network architectures to incorporate new features remains a research challenge. This issue is particularly severe in online learning settings, where new features are added continually with few or no associated observations. As such, methods for adapting neural networks to novel features which are both time and data-efficient are desired. To address this, we propose the Contextual HyperNetwork (CHN), which predicts the network weights associated with new features by incorporating information from both existing data as well as the few observations for the new feature and any associated feature metadata. At prediction time, the CHN requires only a single forward pass through a small neural network, yielding a significant speed-up when compared to re-training and fine-tuning approaches. In order to showcase the performance of CHNs, in this work we use a CHN to augment a partial variational autoencoder (P-VAE), a flexible deep generative model which can impute the values of missing features in sparsely-observed data. We show that this system obtains significantly improved performance for novel feature adaptation over existing imputation and meta-learning baselines across recommender systems, e-learning, and healthcare tasks.

## item_id: m_0072

TITLE: Unit Ball Model for Embedding Hierarchical Structures in the Complex Hyperbolic Space

ABSTRACT: Learning the representation of data with hierarchical structures in the hyperbolic space attracts increasing attention in recent years. Due to the constant negative curvature, the hyperbolic space resembles tree metrics and captures the tree-like properties naturally, which enables the hyperbolic embeddings to improve over traditional Euclidean models. However, most real-world hierarchically structured data such as taxonomies and multitree networks have varying local structures and they are not trees, thus they do not ubiquitously match the constant curvature property of the hyperbolic space. To address this limitation of hyperbolic embeddings, we explore the complex hyperbolic space, which has the variable negative curvature, for representation learning. Specifically, we propose to learn the embeddings of hierarchically structured data in the unit ball model of the complex hyperbolic space. The unit ball model based embeddings have a more powerful representation capacity to capture a variety of hierarchical structures. Through experiments on synthetic and real-world data, we show that our approach improves over the hyperbolic embedding models significantly. We also explore the competence of complex hyperbolic geometry on the multitree structure and 1-N structure.

## item_id: m_0073

TITLE: Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning

ABSTRACT: Reinforcement Learning with verifiable rewards (RLVR) has emerged as a primary learning paradigm for enhancing the reasoning capabilities of multi-modal large language models (MLLMs). However, during RL training, the enormous state space of MLLM and sparse rewards often leads to entropy collapse, policy degradation, or over-exploitation of suboptimal behaviors. This necessitates an exploration strategy that maintains productive stochasticity while avoiding the drawbacks of uncontrolled random sampling, yielding inefficient exploration. In this paper, we propose CalibRL, a hybrid-policy RLVR framework that supports controllable exploration with expert guidance, enabled by two key mechanisms. First, a distribution-aware advantage weighting scales updates by group rareness to calibrate the distribution, therefore preserving exploration. Meanwhile, the asymmetric activation function (LeakyReLU) leverages the expert knowledge as a calibration baseline to moderate overconfident updates while preserving their corrective direction. CalibRL increases policy entropy in a guided manner and clarifies the target distribution by estimating the on-policy distribution through online sampling. Updates are driven by these informative behaviors, avoiding convergence to erroneous patterns. Importantly, these designs help alleviate the distributional mismatch between the model’s policy and expert trajectories, thereby achieving a more stable balance between exploration and exploitation. Extensive experiments across eight benchmarks, including both in-domain and out-of-domain settings, demonstrate consistent improvements, validating the effectiveness of our controllable hybrid-policy RLVR training. Code is available at https://github.com/zhh6425/CalibRL.

## item_id: m_0074

TITLE: Language Agents for Detecting Implicit Stereotypes in Text-to-image Models at Scale

ABSTRACT: The recent surge in the research of diffusion models has accelerated the adoption of text-to-image models in various Artificial Intelligence Generated Content (AIGC) commercial products. While these exceptional AIGC products are gaining increasing recognition and sparking enthusiasm among consumers, the questions regarding whether, when, and how these models might unintentionally reinforce existing societal stereotypes remain largely unaddressed. Motivated by recent advancements in language agents, here we introduce a novel agent architecture tailored for stereotype detection in text-to-image models. This versatile agent architecture is capable of accommodating free-form detection tasks and can autonomously invoke various tools to facilitate the entire process, from generating corresponding instructions and images, to detecting stereotypes. 
We build the stereotype-relevant benchmark based on multiple open text datasets, and apply this architecture to commercial products and popular open source text-to-image models. We find that these models often display serious biases when it comes to certain prompts about personal characteristics, social cultural context and crime-related aspects. In summary, these empirical findings underscore the pervasive existence of stereotypes across social dimensions, including gender, race, and religion, which not only validate the effectiveness of our proposed approach, but also emphasize the critical necessity of addressing potential ethical risks in the burgeoning realm of AIGC. As AIGC continues its rapid expansion trajectory, with new models and plugins emerging daily in staggering numbers, the challenge lies in the timely detection and mitigation of potential biases within these models.

## item_id: m_0075

TITLE: Wavelet-Packet Powered Deepfake Image Detection

ABSTRACT: As neural networks become able to generate realistic artificial images, they have the potential to improve movies, music, video games and make the internet an even more creative and inspiring place.
Yet, at the same time, the latest technology potentially enables new digital ways to lie. In response, the need for a diverse and reliable method toolbox arises to identify artificial images and other content.
Previous work primarily relies on pixel-space CNN or the Fourier transform. To the best of our knowledge, synthesized fake image analysis and detection methods based on a multi-scale wavelet representation,
which is localized in both space and frequency, have been absent thus far. 
This paper proposes to learn a model for the detection of synthetic images based on the wavelet-packet representation of natural and GAN-generated images. We evaluate our method on FFHQ, CelebA, and LSUN source identification problems and find improved or competitive performance. Our forensic classifier has a small network size and can be learned efficiently.
Furthermore, a comparison of the wavelet coefficients from these two sources of images allows an interpretation and identifies significant differences.

## item_id: m_0076

TITLE: Fuzzing-Based Hard-Label Black-Box Attacks Against Machine Learning Models

ABSTRACT: Machine learning models are known to be vulnerable to adversarial examples. Based on different levels of knowledge that attackers have about the models, adversarial example generation methods can be categorized into white-box and black-box attacks. We study the most realistic attacks, hard-label black-box attacks, where attackers only have the query access of a model and only the final predicted labels are available. The main limitation of the existing hard-label black-box attacks is that they need a large number of model queries, making them inefficient and even infeasible in practice. Inspired by the very successful fuzz testing approach in traditional software testing and computer security domains, we propose fuzzing-based hard-label black-box attacks against machine learning models. We design an AdvFuzzer to explore multiple paths between a source image and a guidance image, and design a LocalFuzzer to explore the nearby space around a given input for identifying potential adversarial examples. We demonstrate that our fuzzing attacks are feasible and effective in generating successful adversarial examples with significantly reduced number of model queries and L0 distance. More interestingly, supplied with a successful adversarial example as a seed, LocalFuzzer can immediately generate more successful adversarial examples even with smaller L2 distance from the source example, indicating that LocalFuzzer itself can be an independent and useful tool to augment many adversarial example generation algorithms.

## item_id: m_0077

TITLE: SIM-Shapley: A Stable and Computationally Efficient Approach to Shapley Value Approximation

ABSTRACT: Explainable artificial intelligence (XAI) is essential for trustworthy  machine learning (ML), particularly in high-stakes domains such as healthcare and finance. Shapley value (SV) methods provide a principled framework for feature attribution in complex  models but incur high computational costs, limiting their scalability in high-dimensional settings. We propose Stochastic IterativeMomentum for Shapley Value Approximation (SIM-Shapley), a stable and efficient SV approximation method inspired by stochastic optimization. We analyze variance theoretically, prove linear $Q$-convergence, and demonstrate improved empirical stability and low bias in practice on real-world datasets.
In our numerical experiments, SIM-Shapley reduces computation time by up to 85\% relative to state-of-the-art baselines while maintaining comparable feature attribution quality. Beyond feature attribution, our stochastic mini-batch iterative framework extends naturally to a broader class of sample average approximation problems, offering a new avenue for improving computational efficiency with stability guarantees. Code is publicly available at https://anonymous.4open.science/r/SIM-Shapley.

## item_id: m_0078

TITLE: A Theoretical Analysis of the Number of Shots in Few-Shot Learning

ABSTRACT: Few-shot classification is the task of predicting the category of an example from a set of few labeled examples. The number of labeled examples per category is called the number of shots (or shot number). Recent works tackle this task through meta-learning, where a meta-learner extracts information from observed tasks during meta-training to quickly adapt to new tasks during meta-testing. In this formulation, the number of shots exploited during meta-training has an impact on the recognition performance at meta-test time. Generally, the shot number used in meta-training should match the one used in meta-testing to obtain the best performance. We introduce a theoretical analysis of the impact of the shot number on Prototypical Networks, a state-of-the-art few-shot classification method. From our analysis, we propose a simple method that is robust to the choice of shot number used during meta-training, which is a crucial hyperparameter. The performance of our model trained for an arbitrary meta-training shot number shows great performance for different values of meta-testing shot numbers. We experimentally demonstrate our approach on different few-shot classification benchmarks.

## item_id: m_0079

TITLE: Simple Black-box Adversarial Attacks

ABSTRACT: The construction of adversarial images is a search problem in high dimensions within a small region around a target image. The goal is to find an imperceptibly modified image that is misclassified by a target model. In the black-box setting, only sporadic feedback is provided through occasional model evaluations. In this paper we provide a new algorithm whose search strategy is based on an intriguingly simple iterative principle: We randomly pick a low frequency component of the discrete cosine transform (DCT) and either add or subtract it to the target image. Model evaluations are only required to identify whether an operation decreases the adversarial loss. Despite its simplicity, the proposed method can be used for targeted and untargeted attacks --- resulting in previously unprecedented query efficiency in both settings. We require a median of 600 black-box model queries (ResNet-50) to produce an adversarial ImageNet image, and we successfully attack Google Cloud Vision with 2500 median queries, averaging to a cost of only $3 per image. We argue that our proposed algorithm should serve as a strong baseline for future adversarial black-box attacks, in particular because it is extremely fast and can be implemented in less than 20 lines of PyTorch code. 

## item_id: m_0080

TITLE: When less is more: Simplifying inputs aids neural network understanding

ABSTRACT: Are all bits useful? In this work, we propose SimpleBits, a method to synthesize simplified inputs by reducing information content, and carefully measure the effect of such simplification on learning. Crucially, SimpleBits does not require any domain-specific knowledge to constrain which input features should be removed. Instead, SimpleBits learns to remove the features of inputs which are least relevant for a given task. Concretely, we jointly optimize for input simplification by reducing inputs' bits per dimension as given by a pretrained generative model, as well as for the classification performance. We apply the simplification approach to a wide range of scenarios: conventional training, dataset condensation and post-hoc explanations. In this way, we analyze what simplified inputs tell us about the decisions made by classification networks. We show that our simplification approach successfully removes superfluous information for tasks with injected distractors.  When applied post-hoc, our approach provides intuition into reasons for misclassifications of conventionally trained classifiers. Finally, for dataset condensation, we find that inputs can be simplified with only minimal accuracy degradation. Overall, our learning-based simplification approach offers a valuable new tool to explore the basis of network decisions.

## item_id: m_0081

TITLE: Quality Evaluation of GANs Using Cross Local Intrinsic Dimensionality

ABSTRACT: Generative Adversarial Networks (GANs) are an elegant mechanism for data generation.  However, a key challenge when using GANs is how to best measure their ability to generate realistic data. In this paper, we demonstrate that an intrinsic dimensional characterization of the data space learned by a GAN model leads to an effective evaluation metric for GAN quality.  In particular, we propose a new evaluation measure, CrossLID, that assesses the local intrinsic dimensionality (LID) of input data with respect to neighborhoods within GAN-generated samples.  In experiments on 3 benchmark image datasets, we compare our proposed measure to several state-of-the-art evaluation metrics. Our experiments show that CrossLID is strongly correlated with sample quality, is sensitive to mode collapse, is robust to small-scale noise and image transformations, and can be applied in a model-free  manner.  Furthermore, we show how CrossLID can be used within the GAN training process to improve generation quality.

## item_id: m_0082

TITLE: Recurrent Mixture Density Network for Spatiotemporal Visual Attention

ABSTRACT: In many computer vision tasks, the relevant information to solve the problem at hand is mixed to irrelevant, distracting information. This has motivated researchers to design attentional models that can dynamically focus on parts of images or videos that are salient, e.g., by down-weighting irrelevant pixels. In this work, we propose a spatiotemporal attentional model that learns where to look in a video directly from human fixation data. We model visual attention with a mixture of Gaussians at each frame. This distribution is used to express the probability of saliency for each pixel. Time consistency in videos is modeled hierarchically by: 1) deep 3D convolutional features to represent spatial and short-term time relations and 2) a long short-term memory network on top that aggregates the clip-level representation of sequential clips and therefore expands the temporal domain from few frames to seconds. The parameters of the proposed model are optimized via maximum likelihood estimation using human fixations as training data, without knowledge of the action in each video. Our experiments on Hollywood2 show state-of-the-art performance on saliency prediction for video. We also show that  our attentional model trained on Hollywood2 generalizes well to UCF101 and it can be leveraged to improve action classification accuracy on both datasets.

## item_id: m_0083

TITLE: VTG-Reasoner: Long Video Temporal Grounding via Reinforcement Fine-Tuning

ABSTRACT: Video temporal grounding aims to identify the start and end timestamps of a target event in videos with varying duration. Most of existing methods are trained mainly on short videos through supervised fine-tuning. It is challenging for them to handle long videos, which show diverse data distributions, and thus require to perform reasoning with semantic cues. 
To conquer this challenge, we propose VTG-Reasoner, a reinforcement fine-tuning framework to enhance the model’s reasoning ability for long video temporal grounding. Instead of directly supervising model outputs, VTG-Reasoner explores multiple temporal grounding predictions based on video contexts through an explicit reasoning process. These exploration predictions are then evaluated by our proposed IoU and Intersection Compactness reward to optimize the model.
To further enhance the reasoning performance, we adopt relative frame number to replace absolute timestamps, providing a unified temporal representation for videos with varying duration. Quantitative results demonstrate that VTG-Reasoner achieves superior performance on four long video temporal grounding benchmarks in a zero-shot manner, outperforming SFT-based models trained with 20$\times$ amount of data.

## item_id: m_0084

TITLE: Context Dependent Modulation of Activation Function

ABSTRACT: We propose a modification to traditional Artificial Neural Networks (ANNs), which provides the ANNs with new aptitudes motivated by biological neurons.  Biological neurons work far beyond linearly summing up synaptic inputs and then transforming the integrated information.  A biological neuron change firing modes accordingly to peripheral factors (e.g., neuromodulators) as well as intrinsic ones.  Our modification connects a new type of ANN nodes, which mimic the function of biological neuromodulators and are termed modulators, to enable other traditional ANN nodes to adjust their activation sensitivities in run-time based on their input patterns.  In this manner, we enable the slope of the activation function to be context dependent.  This modification produces statistically significant improvements in comparison with traditional ANN nodes in the context of Convolutional Neural Networks and Long Short-Term Memory networks. 

## item_id: m_0085

TITLE: Smooth markets: A basic mechanism for organizing gradient-based learners

ABSTRACT: With the success of modern machine learning, it is becoming increasingly important to understand and control how learning algorithms interact. Unfortunately, negative results from game theory show there is little hope of understanding or controlling general n-player games. We therefore introduce smooth markets (SM-games), a class of n-player games with pairwise zero sum interactions. SM-games codify a common design pattern in machine learning that includes some GANs, adversarial training, and other recent algorithms. We show that SM-games are amenable to analysis and optimization using first-order methods.

## item_id: m_0086

TITLE: FigureQA: An Annotated Figure Dataset for Visual Reasoning

ABSTRACT: We introduce FigureQA, a visual reasoning corpus of over one million question-answer pairs grounded in over 100,000 images. The images are synthetic, scientific-style figures from five classes: line plots, dot-line plots, vertical and horizontal bar graphs, and pie charts. We formulate our reasoning task by generating questions from 15 templates; questions concern various relationships between plot elements and examine characteristics like the maximum, the minimum, area-under-the-curve, smoothness, and intersection. To resolve, such questions often require reference to multiple plot elements and synthesis of information distributed spatially throughout a figure. To facilitate the training of machine learning systems, the corpus also includes side data that can be used to formulate auxiliary objectives. In particular, we provide the numerical data used to generate each figure as well as bounding-box annotations for all plot elements. We study the proposed visual reasoning task by training several models, including the recently proposed Relation Network as strong baseline. Preliminary results indicate that the task poses a significant machine learning challenge. We envision FigureQA as a first step towards developing models that can intuitively recognize patterns from visual representations of data.

## item_id: m_0087

TITLE: A Painless Attention Mechanism for Convolutional Neural Networks

ABSTRACT: We propose a novel attention mechanism to enhance Convolutional Neural Networks for fine-grained recognition. The proposed mechanism reuses CNN feature activations to find the most informative parts of the image at different depths with the help of gating mechanisms and without part annotations. Thus, it can be used to augment any layer of a CNN to extract low- and high-level local information to be more discriminative. 

Differently, from other approaches, the mechanism we propose just needs a single pass through the input and it can be trained end-to-end through SGD. As a consequence, the proposed mechanism is modular, architecture-independent, easy to implement, and faster than iterative approaches.

Experiments show that, when augmented with our approach, Wide Residual Networks systematically achieve superior performance on each of five different fine-grained recognition datasets: the Adience age and gender recognition benchmark, Caltech-UCSD Birds-200-2011, Stanford Dogs, Stanford Cars, and UEC Food-100, obtaining competitive and state-of-the-art scores.

## item_id: m_0088

TITLE: Comparing Distributions by Measuring Differences that Affect Decision Making

ABSTRACT: Measuring the discrepancy between two probability distributions is a fundamental problem in machine learning and statistics. We propose a new class of discrepancies based on the optimal loss for a decision task -- two distributions are different if the optimal decision loss is higher on their mixture than on each individual distribution. By suitably choosing the decision task, this generalizes the Jensen-Shannon divergence and the maximum mean discrepancy family. We apply our approach to two-sample tests, and on various benchmarks, we achieve superior test power compared to competing methods. In addition, a modeler can directly specify their preferences when comparing distributions through the decision loss. We apply this property to understanding the effects of climate change on different social and economic activities, evaluating sample quality, and selecting features targeting different decision tasks.

## item_id: m_0089

TITLE: Transferable Unlearnable Examples

ABSTRACT: With more people publishing their personal data online, unauthorized data usage has become a serious concern. The unlearnable examples strategies have been introduced to prevent third parties from training on the data without permission. They add perturbations to the users’ data before publishing, so as to make the models trained on the perturbed published dataset invalidated. These perturbations have been generated for a specific training setting and a target dataset. However, their unlearnable effects significantly decrease when used in other training settings or datasets. To tackle this issue, we propose a novel unlearnable strategy based on Class-wise Separability Discriminant (CSD), which boosts the transferability of the unlearnable perturbations by enhancing the linear separability. Extensive experiments demonstrate the transferability of the unlearnable examples crafted by our proposed method across training settings and datasets.

## item_id: m_0090

TITLE: Relation-Aware Diffusion for Heterogeneous Graphs with Partially Observed Features

ABSTRACT: Diffusion-based imputation methods, which impute missing features through the iterative propagation of observed features, have shown impressive performance in homogeneous graphs. However, these methods are not directly applicable to heterogeneous graphs, which have multiple types of nodes and edges, due to two key issues: (1) the presence of nodes with undefined features hinders diffusion-based imputation; (2) treating various edge types equally during diffusion does not fully utilize information contained in heterogeneous graphs. To address these challenges, this paper presents a novel imputation scheme that enables diffusion-based imputation in heterogeneous graphs. Our key idea involves (1) assigning a {\it virtual feature} to an undefined node feature and (2) determining the importance of each edge type during diffusion according to a new criterion. Through experiments, we demonstrate that our virtual feature scheme effectively serves as a bridge between existing diffusion-based methods and heterogeneous graphs, maintaining the advantages of these methods. Furthermore, we confirm that adjusting the importance of each edge type leads to significant performance gains on heterogeneous graphs. Extensive experimental results demonstrate the superiority of our scheme in both semi-supervised node classification and link prediction tasks on heterogeneous graphs with missing rates ranging from low to exceedingly high. The source code is available at https://github.com/daehoum1/hetgfd.

## item_id: m_0091

TITLE: Towards Dynamic Sparsification by Iterative Prune-Grow LookAheads

ABSTRACT: Model sparsification is a process of removing redundant connections in a neural network, making it more compact and faster. Most pruning methods start with a dense pretrained model, which is computationally intensive to train. Other pruning approaches perform compression at initialization which saves training time, however, at the cost of final accuracy as an unreliable architecture can be selected given weak feature representation. In this work, we re-formulate network sparsification as an exploitation-exploration process during initial training to enable dynamic learning of network sparsification. The exploitation phase assumes architecture stability and trains it to maximize accuracy. Whereas the exploration phase challenges the current architecture with a novel $\textit{LookAhead}$ step that reactivates pruned parameters, quickly updates them together with existing ones, and reconfigures the sparse architecture with a pruning-growing paradigm. We demonstrate that $\textit{LookAhead}$ methodology can effectively and efficiently oversee both architecture and performance during training, enabling early pruning with a capability of future recovery to correct previous poor pruning selections. Extensive results on ImageNet and CIFAR datasets show consistent improvements over the prior art by large margins, for varying networks towards both structured and unstructured sparsity. For example, our method surpasses recent work by $+1.3\%$ top-1 accuracy at the same compression ratio for ResNet50-ImageNet unstructured sparsity. Moreover, our structured sparsity results also improve upon the previous best hardware-aware pruning method by $+0.8\%$ top-1 accuracy for MobileNet-ImageNet sparsification, offering $+134$ in hardware FPS(im/s), while halving the training cost.

## item_id: m_0092

TITLE: Composing Ensembles of Pre-trained Models via Iterative Consensus

ABSTRACT: Large pre-trained models exhibit distinct and complementary capabilities dependent on the data they are trained on. Language models such as GPT-3 are capable of textual reasoning but cannot understand visual information, while vision models such as DALL-E can generate photorealistic photos but fail to understand complex language descriptions. In this work, we propose a unified framework for composing ensembles of different pre-trained models -- combining the strengths of each individual model to solve various multimodal problems in a zero-shot manner. We use pre-trained models as "generators" or "scorers" and compose them via closed-loop iterative consensus optimization. The generator constructs proposals and the scorers iteratively provide feedback to refine the generated result. Such closed-loop communication enables models to correct errors caused by other models, significantly boosting performance on downstream tasks, e.g. improving accuracy on grade school math problems by 7.5%, without requiring any model finetuning. We demonstrate that consensus achieved by an ensemble of scorers outperforms the feedback of a single scorer, by leveraging the strengths of each expert model. Results show that the proposed method can be used as a general purpose framework for a wide range of zero-shot multimodal tasks, such as image generation, video question answering, mathematical reasoning, and robotic manipulation. 


## item_id: m_0093

TITLE: SpaMHMM: Sparse Mixture of Hidden Markov Models for Graph Connected Entities

ABSTRACT: We propose a framework to model the distribution of sequential data coming from
a set of entities connected in a graph with a known topology. The method is
based on a mixture of shared hidden Markov models (HMMs), which are trained
in order to exploit the knowledge of the graph structure and in such a way that the
obtained mixtures tend to be sparse. Experiments in different application domains
demonstrate the effectiveness and versatility of the method.

## item_id: m_0094

TITLE: CausalAgents: A Robustness Benchmark for Motion Forecasting Using Causal Relationships

ABSTRACT: As machine learning models become increasingly prevalent in motion forecasting systems for autonomous vehicles (AVs), it is critical that we ensure that model predictions are safe and reliable. However, exhaustively collecting and labeling the data necessary to fully test the long tail of rare and challenging scenarios is difficult and expensive. In this work, we construct a new benchmark for evaluating and improving model robustness by applying perturbations to existing data. Specifically, we conduct an extensive labeling effort to identify causal agents, or agents whose presence influences human driver behavior in any way, in the Waymo Open Motion Dataset (WOMD), and we use these labels to perturb the data by deleting non-causal agents from the scene. We then evaluate a diverse set of state-of-the-art deep-learning model architectures on our proposed benchmark and find that all models exhibit large shifts under perturbation. Under non-causal perturbations, we observe a 25-38% relative change in minADE as compared to the original. We then investigate techniques to improve model robustness, including increasing the training dataset size and using targeted data augmentations that drop agents throughout training. We provide the causal agent labels as an additional attribute to WOMD and release the robustness benchmarks to aid the community in building more reliable and safe deep-learning models for motion forecasting. 


## item_id: m_0095

TITLE: SLMRec: Distilling Large Language Models into Small for Sequential Recommendation

ABSTRACT: Sequential Recommendation (SR) task involves predicting the next item a user is likely to interact with, given their past interactions. 
The SR models examine the sequence of a user's actions to discern more complex behavioral patterns and temporal dynamics. 
Recent research demonstrates the great impact of LLMs on sequential recommendation systems, either viewing sequential recommendation as language modeling or serving as the backbone for user representation. Although these methods deliver outstanding performance, there is scant evidence of the necessity of a large language model and how large the language model is needed, especially in the sequential recommendation scene. Meanwhile, due to the huge size of LLMs, it is inefficient and impractical to apply a LLM-based model in real-world platforms that often need to process billions of traffic logs daily. In this paper, we explore the influence of LLMs' depth by conducting extensive experiments on large-scale industry datasets. Surprisingly, our motivational experiments reveal that most intermediate layers of LLMs are redundant, indicating that pruning the remaining layers can still maintain strong performance.
Motivated by this insight, we empower small language models for SR, namely SLMRec, which adopt a simple yet effective knowledge distillation method. Moreover, SLMRec is orthogonal to other post-training efficiency techniques, such as quantization and pruning, so that they can be leveraged in combination. Comprehensive experimental results illustrate that the proposed SLMRec model attains the best performance using only 13\% of the parameters found in LLM-based recommendation models while simultaneously achieving up to 6.6x and 8.0x speedups in training and inference time costs, respectively. Besides, we provide a theoretical justification for why small language models can perform comparably to large language models in SR.

## item_id: m_0096

TITLE: Decentralized Knowledge Graph Representation Learning

ABSTRACT: Knowledge graph (KG) representation learning methods have achieved competitive performance in many KG-oriented tasks, among which the best ones are usually based on graph neural networks (GNNs), a powerful family of networks that learns the representation of an entity by aggregating the features of its neighbors and itself. However, many KG representation learning scenarios only provide the structure information that describes the relationships among entities, causing that entities have no input features. In this case, existing aggregation mechanisms are incapable of inducing embeddings of unseen entities as these entities have no pre-defined features for aggregation. In this paper, we present a decentralized KG representation learning approach, decentRL, which encodes each entity from and only from the embeddings of its neighbors. For optimization, we design an algorithm to distill knowledge from the model itself such that the output embeddings can continuously gain knowledge from the corresponding original embeddings. Extensive experiments show that the proposed approach performed better than many cutting-edge models on the entity alignment task, and achieved competitive performance on the entity prediction task. Furthermore, under the inductive setting, it significantly outperformed all baselines on both tasks.

## item_id: m_0097

TITLE: Cat2Vec: Learning Distributed Representation of Multi-field Categorical Data

ABSTRACT: This paper presents a method of learning distributed representation for multi-field categorical data, which is a common data format with various applications such as recommender systems, social link prediction, and computational advertising. The success of non-linear models, e.g., factorisation machines, boosted trees, has proved the potential of exploring the interactions among inter-field categories. Inspired by Word2Vec, the distributed representation for natural language, we propose Cat2Vec (categories to vectors) model. In Cat2Vec, a low-dimensional continuous vector is automatically learned for each category in each field. The interactions among inter-field categories are further explored by different neural gates and the most informative ones are selected by pooling layers. In our experiments, with the exploration of the interactions between pairwise categories over layers, the model attains great improvement over state-of-the-art models in a supervised learning task, e.g., click prediction, while capturing the most significant interactions from the data. 

## item_id: m_0098

TITLE: Learning a Generative Model for Validity in Complex Discrete Structures

ABSTRACT: Deep generative models have been successfully used to learn representations for high-dimensional discrete spaces by representing discrete objects as sequences and employing powerful sequence-based deep models. Unfortunately, these sequence-based models often produce invalid sequences: sequences which do not represent any underlying discrete structure; invalid sequences hinder the utility of such models. As a step towards solving this problem, we propose to learn a deep recurrent validator model, which can estimate whether a partial sequence can function as the beginning of a full, valid sequence. This validator provides insight as to how individual sequence elements influence the validity of the overall sequence, and can be used to constrain sequence based models to generate valid sequences — and thus faithfully model discrete objects. Our approach is inspired by reinforcement learning, where an oracle which can evaluate validity of complete sequences provides a sparse reward signal. We demonstrate its effectiveness as a generative model of Python 3 source code for mathematical expressions, and in improving the ability of a variational autoencoder trained on SMILES strings to decode valid molecular structures.

## item_id: m_0099

TITLE: Dynamic Coattention Networks For Question Answering

ABSTRACT: Several deep learning models have been proposed for question answering. How- ever, due to their single-pass nature, they have no way to recover from local maxima corresponding to incorrect answers. To address this problem, we introduce the Dynamic Coattention Network (DCN) for question answering. The DCN first fuses co-dependent representations of the question and the document in order to focus on relevant parts of both. Then a dynamic pointer decoder iterates over potential answer spans. This iterative procedure enables the model to recover from initial local maxima corresponding to incorrect answers. On the Stanford question answering dataset, a single DCN model improves the previous state of the art from 71.0% F1 to 75.9%, while a DCN ensemble obtains 80.4% F1.

## item_id: m_0100

TITLE: Learning Deep Mean Field Games for Modeling Large Population Behavior

ABSTRACT: We consider the problem of representing collective behavior of large populations and predicting the evolution of a population distribution over a discrete state space. A discrete time mean field game (MFG) is motivated as an interpretable model founded on game theory for understanding the aggregate effect of individual actions and predicting the temporal evolution of population distributions. We achieve a synthesis of MFG and Markov decision processes (MDP) by showing that a special MFG is reducible to an MDP. This enables us to broaden the scope of mean field game theory and infer MFG models of large real-world systems via deep inverse reinforcement learning. Our method learns both the reward function and forward dynamics of an MFG from real data, and we report the first empirical test of a mean field game model of a real-world social media population.
