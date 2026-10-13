# Batch 15 — 100 items

## item_id: m_1401

TITLE: Node Identifiers: Compact, Discrete Representations for Efficient Graph Learning

ABSTRACT: We present a novel end-to-end framework that generates highly compact (typically 6-15 dimensions), discrete (int4 type), and interpretable node representations—termed node identifiers (node IDs)—to tackle inference challenges on large-scale graphs. By employing vector quantization, we compress continuous node embeddings from multiple layers of a Graph Neural Network (GNN) into discrete codes, applicable under both self-supervised and supervised learning paradigms. These node IDs capture high-level abstractions of graph data and offer interpretability that traditional GNN embeddings lack. Extensive experiments on 34 datasets, encompassing node classification, graph classification, link prediction, and attributed graph clustering tasks, demonstrate that the generated node IDs significantly enhance speed and memory efficiency while achieving competitive performance compared to current state-of-the-art methods. Our source code is available at https://github.com/LUOyk1999/NodeID.

## item_id: m_1402

TITLE: De novo design of protein target specific scaffold-based Inhibitors via Reinforcement Learning

ABSTRACT: Efficient design and discovery of target-driven molecules is a critical step in facilitating lead optimization in drug discovery. Current approaches to develop molecules for a given protein target are intuition-driven, hampered by slow iterative design-test cycles due to computational challenges in utilizing 3D structural data, and ultimately limited by the expertise of the chemist – leading to bottlenecks in molecular design. In this contribution, we propose a novel framework, called 3D-MolGNN_RL, coupling reinforcement learning (RL) to a deep generative model based on 3D-Scaffold to generate target candidates specific to a protein pocket building up atom by atom from the starting core scaffold. 3D-MolGNN_RL provides an efficient way to optimize key features by multi-objective reward function within a protein pocket using parallel graph neural network models. The agent learns to build molecules in 3D space while optimizing the binding affinity, potency, and synthetic accessibility of the candidates generated for the SARS-CoV-2 Main Protease.

## item_id: m_1403

TITLE: Trust-PCL: An Off-Policy Trust Region Method for Continuous Control

ABSTRACT: Trust region methods, such as TRPO, are often used to stabilize policy optimization algorithms in reinforcement learning (RL). While current trust region strategies are effective for continuous control, they typically require a large amount of on-policy interaction with the environment. To address this problem, we propose an off-policy trust region method, Trust-PCL, which exploits an observation that the optimal policy and state values of a maximum reward objective with a relative-entropy regularizer satisfy a set of multi-step pathwise consistencies along any path. The introduction of relative entropy regularization allows Trust-PCL to maintain optimization stability while exploiting off-policy data to improve sample efficiency. When evaluated on a number of continuous control tasks, Trust-PCL significantly improves the solution quality and sample efficiency of TRPO.

## item_id: m_1404

TITLE: Certified Adversarial Robustness for Rate Encoded Spiking Neural Networks

ABSTRACT: The spiking neural networks are inspired by the biological neurons that employ binary spikes to propagate information in the neural network. It has garnered considerable attention as the next-generation neural network, as the spiking activity simplifies the computation burden of the network to a large extent and is known for its low energy deployment enabled by specialized neuromorphic hardware. One popular technique to feed a static image to such a network is rate encoding, where each pixel is encoded into random binary spikes, following a Bernoulli distribution that uses the pixel intensity as bias. By establishing a novel connection between rate-encoding and randomized smoothing, we give the first provable robustness guarantee for spiking neural networks against adversarial perturbation of inputs bounded under $l_1$-norm. We introduce novel adversarial training algorithms for rate-encoded models that significantly improve the state-of-the-art empirical robust accuracy result. Experimental validation of the method is performed across various static image datasets, including CIFAR-10, CIFAR-100 and ImageNet-100. The code is available at \url{https://github.com/BhaskarMukhoty/CertifiedSNN}.

## item_id: m_1405

TITLE: AutoMiSeg: Automatic Medical Image Segmentation via Test-Time Adaptation of Foundation Models

ABSTRACT: Medical image segmentation is vital for clinical diagnosis, yet current deep learning methods often demand extensive expert effort, i.e., either through annotating large training datasets or providing prompts at inference time for each new case. This paper introduces a zero-shot and automatic segmentation pipeline that combines off-the-shelf vision-language and segmentation foundation models. Given a medical image and a task definition (e.g., "segment the optic disc in an eye fundus image"), our method uses a grounding model to generate an initial bounding box, followed by a visual prompt boosting module that enhance the prompts, which are then processed by a promptable segmentation model to produce the final mask. To address the challenges of domain gap and result verification, we introduce a test-time adaptation framework featuring a set of learnable adaptors that align the medical inputs with foundation model representations. Its hyperparameters are optimized via Bayesian Optimization, guided by a proxy validation model without requiring ground-truth labels. Our pipeline offers an annotation-efficient and scalable solution for zero-shot medical image segmentation across diverse tasks. Our pipeline is evaluated on seven diverse medical imaging datasets and shows promising results. By proper decomposition and test-time adaptation, our fully automatic pipeline not only substantially surpasses the previously best-performing method, yielding a 69\% relative improvement in accuracy (Dice Score from 42.53 to 71.81), but also performs competitively with weakly-prompted interactive foundation models.

## item_id: m_1406

TITLE: A Spectral Perspective on Deep Supervised Community Detection

ABSTRACT: In this work, we study the behavior of standard models for community detection under spectral manipulations. Through various ablation experiments, we evaluate the impact of bandpass filtering on the numerical performances of a GCN: we empirically show that most of the necessary and used information for nodes classification is contained in the low-frequency domain, and thus contrary to Euclidean graph (e.g., images),  high-frequencies are less crucial to community detection. In particular, it is possible to obtain accuracies at a state-of-the-art level with simple classifiers that rely only on a few low frequencies: this is surprising because contrary to GCNs, no cascade of filtering along the graph structure is involved and it indicates that the important spectral components for the supervised community detection task are essentially in the low-frequency domain.

## item_id: m_1407

TITLE: Causal Discovery via Cholesky Factorization

ABSTRACT: Discovering the causal relationship via recovering the directed acyclic graph (DAG) structure from the observed data is a challenging combinatorial problem. This paper proposes an extremely fast, easy to implement, and high-performance DAG structure recovering algorithm. The algorithm is based on the Cholesky factorization of the covariance/precision matrix. The time complexity of the algorithm is $\mathcal{O}(p^2n + p^3)$, where $p$ and $n$ are the numbers of nodes and samples, respectively. Under proper assumptions, we show that our algorithm takes $\mathcal{O}(\log(p/\epsilon))$ samples to exactly recover the DAG structure with probability at least $1-\epsilon$. In both time and sample complexities, our algorithm is better than previous algorithms. On synthetic and real-world data sets, our algorithm is significantly faster than previous methods and achieves state-of-the-art performance.

## item_id: m_1408

TITLE: A preconditioned accelerated stochastic gradient descent algorithm

ABSTRACT: We propose a preconditioned accelerated stochastic gradient method suitable for large scale optimization. We derive sufficient convergence conditions for the minimization of convex functions using a generic class of diagonal preconditioners and provide a formal convergence proof based on a framework originally used for on-line learning. Inspired by recent popular adaptive per-feature algorithms, we propose a specific preconditioner based on the second moment of the gradient. The sufficient convergence conditions motivate a critical adaptation of the per-feature updates in order to ensure convergence. We show empirical results for the minimization of convex and non-convex cost functions, in the context of neural network training. The method compares favorably with respect to current, first order, stochastic optimization methods.

## item_id: m_1409

TITLE: A Simple, Yet Effective Approach to Finding Biases in Code Generation

ABSTRACT: Recently, scores of high-performing code generation systems have surfaced. Like most natural language tasks, code generation is approached using large language models as a core, trained under the masked or causal language modeling schema. 
This work shows that current code generation systems exhibit biases inherited from large language model backbones, which might leak into generated code under specific circumstances.
To investigate the effect, we propose a framework that automatically removes hints and exposes various biases that these code generation models use. We apply our framework to three coding challenges and test it across top-performing coding generation models. Our experiments reveal biases towards specific prompt structure and exploitation of keywords during code generation. Finally, we demonstrate how to use our framework as a data transformation technique, which we find a promising direction toward more robust code generation.

## item_id: m_1410

TITLE: KNIFE: Kernelized-Neural Differential Entropy Estimation

ABSTRACT: Estimation of (differential) entropy and the related mutual information has been pursued with significant efforts by the machine learning community. To address shortcomings in previously proposed estimators for differential entropy, here we introduce KNIFE, a fully parameterized, differentiable kernel-based estimator of differential entropy. The flexibility of our approach also allows us to construct KNIFE-based estimators for conditional (on either discrete or continuous variables) differential entropy, as well as mutual information. We empirically validate our method on high-dimensional synthetic data and further apply it to guide the training of neural networks for real-world tasks. Our experiments on a large variety of tasks, including visual domain adaptation, textual fair classification, and textual fine-tuning demonstrate the effectiveness of KNIFE-based estimation.

## item_id: m_1411

TITLE: Computationally Efficient RL under Linear Bellman Completeness for Deterministic Dynamics

ABSTRACT: We study computationally and statistically efficient Reinforcement Learning algorithms for the *linear Bellman Complete* setting. This setting uses linear function approximation to capture value functions and unifies existing models like linear Markov Decision Processes (MDP) and Linear Quadratic Regulators (LQR).  While it is known from the prior works that this setting is statistically tractable, it remained open whether a computationally efficient algorithm exists. Our work provides a computationally efficient algorithm for the linear Bellman complete setting that works for MDPs with large action spaces, random initial states, and random rewards but relies on the underlying dynamics to be deterministic. Our approach is based on randomization: we inject random noise into least squares regression problems to perform optimistic value iteration. Our key technical contribution is to carefully design the noise to only act in the null space of the training data to ensure optimism while circumventing a subtle error amplification issue.

## item_id: m_1412

TITLE: Policy Optimization by Genetic Distillation 

ABSTRACT: Genetic algorithms have been widely used in many practical optimization problems.
Inspired by natural selection, operators, including mutation, crossover
and selection, provide effective heuristics for search and black-box optimization.
However, they have not been shown useful for deep reinforcement learning, possibly
due to the catastrophic consequence of parameter crossovers of neural networks.
Here, we present Genetic Policy Optimization (GPO), a new genetic algorithm
for sample-efficient deep policy optimization. GPO uses imitation learning
for policy crossover in the state space and applies policy gradient methods for mutation.
Our experiments on MuJoCo tasks show that GPO as a genetic algorithm
is able to provide superior performance over the state-of-the-art policy gradient
methods and achieves comparable or higher sample efficiency.

## item_id: m_1413

TITLE: NeMo: Neural Mesh Models of Contrastive Features for Robust 3D Pose Estimation

ABSTRACT: 3D pose estimation is a challenging but important task in computer vision. In this work, we show that standard deep learning approaches to 3D pose estimation are not robust to partial occlusion. Inspired by the robustness of generative vision models to partial occlusion, we propose to integrate deep neural networks with 3D generative representations of objects into a unified neural architecture that we term NeMo. In particular, NeMo learns a generative model of neural feature activations at each vertex on a dense 3D mesh. Using differentiable rendering we estimate the 3D object pose by minimizing the reconstruction error between NeMo and the feature representation of the target image. To avoid local optima in the reconstruction loss, we train the feature extractor to maximize the distance between the individual feature representations on the mesh using contrastive learning. Our extensive experiments on PASCAL3D+, occluded-PASCAL3D+ and ObjectNet3D show that NeMo is much more robust to partial occlusion compared to standard deep networks, while retaining competitive performance on non-occluded data. Interestingly, our experiments also show that NeMo performs reasonably well even when the mesh representation only crudely approximates the true object geometry with a cuboid, hence revealing that the detailed 3D geometry is not needed for accurate 3D pose estimation.

## item_id: m_1414

TITLE: Learning to Write by Learning the Objective

ABSTRACT: Recurrent Neural Networks (RNNs) are powerful autoregressive sequence models for learning prevalent patterns in natural language.   Yet language generated by RNNs often shows several degenerate characteristics that are uncommon in human language; while fluent, RNN language production can be overly generic, repetitive, and even self-contradictory.  We postulate that the objective function optimized by RNN language models, which amounts to the overall perplexity of a text, is not expressive enough to capture the abstract qualities of good generation such as Grice’s Maxims. In this paper, we introduce a general learning framework that can construct a decoding objective better suited for generation. Starting with a generatively trained RNN language model, our framework learns to construct a substantially stronger generator by combining several discriminatively trained models that can collectively address the limitations of RNN generation.  Human evaluation demonstrates that text generated by the resulting generator is preferred over  that  of  baselines  by  a  large  margin  and  significantly  enhances  the  overall coherence, style, and information content of the generated text.

## item_id: m_1415

TITLE: KAN versus MLP on Irregular or Noisy Functions

ABSTRACT: In this paper, we compare the performance of Kolmogorov-Arnold Networks (KAN) and Multi-Layer Perceptron (MLP) networks on irregular or noisy functions. We control the number of parameters and the size of the training samples to ensure a fair comparison. For clarity, we categorize the functions into six types: regular functions, continuous functions with local non-differentiable points, functions with jump discontinuities, functions with singularities, functions with coherent oscillations, and noisy functions. Our experimental results indicate that KAN does not always perform best. For some types of functions, MLP outperforms or performs comparably to KAN. Furthermore, increasing the size of training samples can improve performance to some extent. When noise is added to functions, the irregular features are often obscured by the noise, making it challenging for both MLP and KAN to extract these features effectively. We hope these experiments provide valuable insights for future neural network research and encourage further investigations to overcome these challenges.

## item_id: m_1416

TITLE: When Prompt Engineering Meets Software Engineering: CNL-P as Natural and Robust "APIs'' for Human-AI Interaction

ABSTRACT: With the growing capabilities of large language models (LLMs), they are increasingly applied in areas like intelligent customer service, code generation, and knowledge management.
Natural language (NL) prompts act as the ``APIs'' for human-LLM interaction. 
To improve prompt quality, best practices for prompt engineering (PE) have been developed, including writing guidelines and templates. 
Building on this, we propose Controlled NL for Prompt (CNL-P), which not only incorporates PE best practices but also draws on key principles from software engineering (SE).
CNL-P introduces precise grammar structures and strict semantic norms, further eliminating NL's ambiguity, allowing for a declarative but structured and accurate expression of user intent. 
This helps LLMs better interpret and execute the prompts, leading to more consistent and higher-quality outputs. 
We also introduce an NL2CNL-P conversion tool based on LLMs, enabling users to write prompts in NL, which are then transformed into CNL-P format, thus lowering the learning curve of CNL-P.
In particular, we develop a linting tool that checks CNL-P prompts for syntactic and semantic accuracy, applying static analysis techniques to NL for the first time.
Extensive experiments demonstrate that CNL-P enhances the quality of LLM responses through the novel and organic synergy of PE and SE. 
We believe that CNL-P can bridge the gap between emerging PE and traditional SE, laying the foundation for a new programming paradigm centered around NL.
To further demonstrate the effectiveness of CNL-P, we develop the AI-native CNL-P IDE, UGAiForge that leverages CNL-P to enable users to Think, Describe, and Build with AI and for AI.
For detailed information, please refer https://ugaiforge.ai.

## item_id: m_1417

TITLE: Probabilistic Binary Neural Networks

ABSTRACT: Low bit-width weights and activations are an effective way of combating the increasing need for both memory and compute power of Deep Neural Networks. In this work, we present a probabilistic training method for Neural Network with both binary weights and activations, called PBNet. By embracing stochasticity during training, we circumvent the need to approximate the gradient of functions for which the derivative is zero almost always, such as $\textrm{sign}(\cdot)$, while still obtaining a fully Binary Neural Network at test time. Moreover, it allows for anytime ensemble predictions for improved performance and uncertainty estimates by sampling from the weight distribution. Since all operations in a layer of the PBNet operate on random variables, we introduce stochastic versions of Batch Normalization and max pooling, which transfer well to a deterministic network at test time.  We evaluate two related training methods for the PBNet: one in which activation distributions are propagated throughout the network, and one in which binary activations are sampled in each layer. Our experiments indicate that sampling the binary activations is an important element for stochastic training of binary Neural Networks.


## item_id: m_1418

TITLE: Gradient penalty from a maximum margin perspective

ABSTRACT: A popular heuristic for improved performance in Generative adversarial networks (GANs) is to use some form of gradient penalty on the discriminator. This gradient penalty was originally motivated by a Wasserstein distance formulation. However, the use of gradient penalty in other GAN formulations is not well motivated. We present a unifying framework of expected margin maximization and show that a wide range of gradient-penalized GANs (e.g., Wasserstein, Standard, Least-Squares, and Hinge GANs) can be derived from this framework. Our results imply that employing gradient penalties induces a large-margin classifier (thus, a large-margin discriminator in GANs). We describe how expected margin maximization helps reduce vanishing gradients at fake (generated) samples, a known problem in GANs. From this framework, we derive a new $L^\infty$ gradient norm penalty with Hinge loss which generally produces equally good (or better) generated output in GANs than $L^2$-norm penalties (based on the Fréchet Inception Distance).

## item_id: m_1419

TITLE: Kronecker Attention Networks

ABSTRACT: Attention operators have been applied on both 1-D data like texts and higher-order data such as images and videos. Use of attention operators on high-order data requires flattening of the spatial or spatial-temporal dimensions into a vector, which is assumed to follow a multivariate normal distribution. This not only incurs excessive requirements on computational resources, but also fails to preserve structures in data. In this work, we propose to avoid flattening by developing Kronecker attention operators (KAOs) that operate on high-order tensor data directly. KAOs lead to dramatic reductions in computational resources. Moreover, we analyze KAOs theoretically from a probabilistic perspective and point out that KAOs assume the data follow matrix-variate normal distributions. Experimental results show that KAOs reduce the amount of required computational resources by a factor of hundreds, with larger factors for higher-dimensional and higher-order data. Results also show that networks with KAOs outperform models without attention, while achieving competitive performance as those with original attention operators.

## item_id: m_1420

TITLE: Generating Wikipedia by Summarizing Long Sequences

ABSTRACT: We show that generating English Wikipedia articles can be approached as a multi-
document summarization of source documents. We use extractive summarization
to coarsely identify salient information and a neural abstractive model to generate
the article. For the abstractive model, we introduce a decoder-only architecture
that can scalably attend to very long sequences, much longer than typical encoder-
decoder architectures used in sequence transduction. We show that this model can
generate fluent, coherent multi-sentence paragraphs and even whole Wikipedia
articles. When given reference documents, we show it can extract relevant factual
information as reflected in perplexity, ROUGE scores and human evaluations.

## item_id: m_1421

TITLE: Improving Self-supervised Pre-training via a Fully-Explored Masked Language Model

ABSTRACT: Masked Language Model (MLM) framework has been widely adopted for self-supervised language pre-training.  In this paper, we argue that randomly sampled masks in MLM would lead to undesirably large gradient variance. Thus, we theoretically quantify the gradient variance via correlating the gradient covariance with the Hamming distance between two different masks (given a certain text sequence). To reduce the variance due to the sampling of masks, we propose a fully-explored masking strategy, where a text sequence is divided into a certain number of non-overlapping segments. Thereafter, the tokens within one segment are masked for training. We prove, from a theoretical perspective, that the gradients derived from this new masking schema have a smaller variance and can lead to more efficient self-supervised training. We conduct extensive experiments on both continual pre-training and general pre-training from scratch. Empirical results confirm that this new masking strategy can consistently outperform standard random masking. Detailed efficiency analysis and ablation studies further validate the advantages of our fully-explored masking strategy under the MLM framework.

## item_id: m_1422

TITLE: Adversarial Attacks on Adversarial Bandits

ABSTRACT: We study a security threat to adversarial multi-armed bandit, in which an attacker perturbs the loss or reward signal to control the behavior of the victim bandit player. We show that the attacker is able to mislead any no-regret adversarial bandit algorithm into selecting a suboptimal target action in every but sublinear (T−o(T )) number of rounds, while incurring only sublinear (o(T)) cumulative attack cost. This result implies critical security concern in real-world bandit-based systems, e.g., in online recommendation, an attacker might be able to hijack the recommender system and promote a desired product. Our proposed attack algorithms require knowledge of only the regret rate, thus are agnostic to the concrete bandit algorithm employed by the victim player. We also derived a theoretical lower bound on the cumulative attack cost that any victim-agnostic attack algorithm must incur. The lower bound matches the upper bound achieved by our attack, which shows that our attack is asymptotically optimal.

## item_id: m_1423

TITLE: Contrastive  Learning  with Adversarial Perturbations for Conditional Text Generation

ABSTRACT: Recently, sequence-to-sequence (seq2seq) models with the Transformer architecture have achieved remarkable performance on various conditional text generation tasks, such as machine translation. However, most of them are trained with teacher forcing with the ground truth label given at each time step, without being exposed to incorrectly generated tokens during training, which hurts its generalization to unseen inputs, that is known as the "exposure bias" problem. In this work, we propose to solve the conditional text generation problem by contrasting positive pairs with negative pairs, such that the model is exposed to various valid or incorrect perturbations of the inputs, for improved generalization. However, training the model with naïve contrastive learning framework using random non-target sequences as negative examples is suboptimal, since they are easily distinguishable from the correct output, especially so with models pretrained with large text corpora. Also, generating positive examples requires domain-specific augmentation heuristics which may not generalize over diverse domains. To tackle this problem, we propose a principled method to generate positive and negative samples for contrastive learning of seq2seq models. Specifically, we generate negative examples by adding small perturbations to the input sequence to minimize its conditional likelihood, and positive examples by adding  large perturbations while enforcing it to have a high conditional likelihood. Such `"hard'' positive and negative pairs generated using our method guides the model to better distinguish correct outputs from incorrect ones. We empirically show that our proposed method significantly improves the generalization of the seq2seq on three text generation tasks --- machine translation, text summarization, and question generation.

## item_id: m_1424

TITLE: ContraDiff: Planning Towards High Return States via Contrastive Learning

ABSTRACT: The performance of offline reinforcement learning (RL) is sensitive to the proportion of high-return trajectories in the offline dataset. However, in many simulation environments and real-world scenarios, there are large ratios of low-return trajectories rather than high-return trajectories, which makes learning an efficient policy challenging. In this paper, we propose a method called Contrastive Diffuser (ContraDiff) to make full use of low-return trajectories and improve the performance of offline RL algorithms. Specifically, ContraDiff groups the states of trajectories in the offline dataset into high-return states and low-return states and treats them as positive and negative samples correspondingly. Then, it designs a contrastive mechanism to pull the planned trajectory of an agent toward high-return states and push them away from low-return states. Through the contrast mechanism, trajectories with low returns can serve as negative examples for policy learning, guiding the agent to avoid areas associated with low returns and achieve better performance. Through the contrast mechanism, trajectories with low returns provide a ``counteracting force'' guides the agent to avoid areas associated with low returns and achieve better performance.
Experiments on 27 sub-optimal datasets demonstrate the effectiveness of our proposed method. Our code is publicly available at https://github.com/Looomo/contradiff.

## item_id: m_1425

TITLE: Fine-Tuning Attention Modules Only: Enhancing Weight Disentanglement in Task Arithmetic

ABSTRACT: In recent years, *task arithmetic* has garnered increasing attention. This approach edits pre-trained models directly in weight space by combining the fine-tuned weights of various tasks into a *unified model*. Its efficiency and cost-effectiveness stem from its training-free combination, contrasting with traditional methods that require model training on large datasets for multiple tasks. However, applying such a unified model to individual tasks can lead to interference from other tasks (lack of *weight disentanglement*). To address this issue, Neural Tangent Kernel (NTK) linearization has been employed to leverage a ''kernel behavior'', facilitating weight disentanglement and mitigating adverse effects from unrelated tasks. Despite its benefits, NTK linearization presents drawbacks, including doubled training costs, as well as reduced performance of individual models. To tackle this problem, we propose a simple yet effective and efficient method that is to finetune the attention modules only in the Transformer. Our study reveals that the attention modules exhibit kernel behavior, and fine-tuning the attention modules only significantly improves weight disentanglement. To further understand how our method improves the weight disentanglement of task arithmetic, we present a comprehensive study of task arithmetic by differentiating the role of the representation module and task-specific module. In particular, we find that the representation module plays an important role in improving weight disentanglement whereas the task-specific modules such as the classification heads can degenerate the weight disentanglement performance.

## item_id: m_1426

TITLE: TiDAL: Learning Training Dynamics for Active Learning

ABSTRACT: Active learning (AL) aims to select the most useful data samples from an unlabeled data pool and annotate them to expand the labeled dataset under a limited budget. Especially, uncertainty-based methods choose the most uncertain samples, which are known to be effective in improving model performance. However, AL literature often overlooks training dynamics (TD), defined as the ever-changing model behavior during optimization via stochastic gradient descent, even though other areas of literature have empirically shown that TD provides important clues for measuring the sample uncertainty. In this paper, we propose a novel AL method, Training Dynamics for Active Learning (TiDAL), which leverages the TD to quantify uncertainties of unlabeled data. Since tracking the TD of all the large-scale unlabeled data is impractical, TiDAL utilizes an additional prediction module that learns the TD of labeled data. To further justify the design of TiDAL, we provide theoretical and empirical evidence to argue the usefulness of leveraging TD for AL. Experimental results show that our TiDAL achieves better or comparable performance on both balanced and imbalanced benchmark datasets compared to state-of-the-art AL methods, which estimate data uncertainty using only static information after model training.

## item_id: m_1427

TITLE: SCALOR: Generative World Models with Scalable Object Representations

ABSTRACT: Scalability in terms of object density in a scene is a primary challenge in unsupervised sequential object-oriented representation learning. Most of the previous models have been shown to work only on scenes with a few objects. In this paper, we propose SCALOR, a probabilistic generative world model for learning SCALable Object-oriented Representation of a video. With the proposed spatially parallel attention and proposal-rejection mechanisms, SCALOR can deal with orders of magnitude larger numbers of objects compared to the previous state-of-the-art models. Additionally, we introduce a background module that allows SCALOR to model complex dynamic backgrounds as well as many foreground objects in the scene. We demonstrate that SCALOR can deal with crowded scenes containing up to a hundred objects while jointly modeling complex dynamic backgrounds. Importantly, SCALOR is the ﬁrst unsupervised object representation model shown to work for natural scenes containing several tens of moving objects.

## item_id: m_1428

TITLE: Tree Cross Attention

ABSTRACT: Cross Attention is a popular method for retrieving information from a set of context tokens for making predictions. At inference time, for each prediction, Cross Attention scans the full set of $\mathcal{O}(N)$ tokens. In practice, however, often only a small subset of tokens are required for good performance. 
Methods such as Perceiver IO are cheap at inference as they distill the information to a smaller-sized set of latent tokens $L < N$ on which cross attention is then applied, resulting in only $\mathcal{O}(L)$ complexity. 
However, in practice, as the number of input tokens and the amount of information to distill increases, the number of latent tokens needed also increases significantly. 
In this work, we propose Tree Cross Attention (TCA) - a module based on Cross Attention that only retrieves information from a logarithmic $\mathcal{O}(\log(N))$ number of tokens for performing inference. 
TCA organizes the data in a tree structure and performs a tree search at inference time to retrieve the relevant tokens for prediction. 
Leveraging TCA, we introduce ReTreever, a flexible architecture for token-efficient inference. 
We show empirically that Tree Cross Attention (TCA) performs comparable to Cross Attention across various classification and uncertainty regression tasks while being significantly more token-efficient. 
Furthermore, we compare ReTreever against Perceiver IO, showing significant gains while using the same number of tokens for inference.

## item_id: m_1429

TITLE: Revisiting Distribution Reconstruction via Sample Adaptability: Diffusion-Guided Data-Free Quantization

ABSTRACT: Data-Free Quantization (DFQ), which seeks to align a low-bit quantized network Q with its full-precision counterpart P without access to original training data, has attracted growing attention. The core idea is to synthesize reconstructed samples that approximate the underlying distribution of real data. However, we observe that reconstructed samples in existing arts are adaptive only to Q with specific bit widths, rather than all bit widths, especially ultra-low bit widths. This raises a key challenge: how to rectify distributional information during sample reconstruction to produce desirable samples that generalize across varied quantization levels. In this paper, we revisit distribution reconstruction via sample adaptability, revealing that 1) the desirable samples enjoy benefits of rectifying distribution reconstruction via adaptability information; beyond that, 2) the forward diffusion process is an optimal noise strategy to rectify reconstructed samples for obtaining desirable samples; and propose a novel Diffusion-Guided Data-Free Quantization approach, dubbed DiffDFQ. Unlike conventional direct optimization, we rectify distribution reconstruction via noise diffusion in a progressive approximation manner. Technically, we decompose DFQ into three stages: sample synthesis to obtain reconstructed samples; upon that, sample diffusion to progressively infuse the noise via forward diffusion process, yielding desirable samples for varied Q; and network calibration to calibrate Q with progressive selection strategy over a series of diffused samples. Our DiffDFQ enjoys the appealing insights: 1) the diffused samples exhibit effective balance between distribution reconstruction and sample adaptability to facilitate varied Q, especially ultra-low bit widths, e.g., 2 bits and 3 bits; notably, 2) unlike the generator-reliance arts requiring up to 1.2M synthetic samples, DiffDFQ synthesizes merely 5.12K (1K) samples to earn performance gain over ImageNet for classification. Our empirical studies verify the merits of DiffDFQ over state-of-the-arts for classification across varied bits to Q. Our code is available in the supplementary material package.

## item_id: m_1430

TITLE: Generating Images from Sounds Using Multimodal Features and GANs

ABSTRACT: Although generative adversarial networks (GANs) have enabled us to convert images from one domain to another similar one, converting between different sensory modalities, such as images and sounds, has been difficult. This study aims to propose a network that reconstructs images from sounds. First, video data with both images and sounds are labeled with pre-trained classifiers. Second, image and sound features are extracted from the data using pre-trained classifiers. Third, multimodal layers are introduced to extract features that are common to both the images and sounds. These layers are trained to extract similar features regardless of the input modality, such as images only, sounds only, and both images and sounds. Once the multimodal layers have been trained, features are extracted from input sounds and converted into image features using a feature-to-feature GAN. Finally, the generated image features are used to reconstruct images. Experimental results show that this method can successfully convert from the sound domain into the image domain. When we applied a pre-trained classifier to both the generated and original images, 31.9% of the examples had at least one of their top 10 labels in common, suggesting reasonably good image generation. Our results suggest that common representations can be learned for different modalities, and that proposed method can be applied not only to sound-to-image conversion but also to other conversions, such as from images to sounds.

## item_id: m_1431

TITLE: Policy Pre-training for Autonomous Driving via Self-supervised Geometric Modeling

ABSTRACT: Witnessing the impressive achievements of pre-training techniques on large-scale data in the field of computer vision and natural language processing, we wonder whether this idea could be adapted in a grab-and-go spirit, and mitigate the sample inefficiency problem for visuomotor driving. Given the highly dynamic and variant nature of the input, the visuomotor driving task inherently lacks the view and translation invariance, and the visual input contains massive irrelevant information for decision making, resulting in predominant pre-training approaches from general vision less suitable for the autonomous driving task. To this end, we propose PPGeo (Policy Pre-training via Geometric modeling), an intuitive and straightforward fully self-supervised framework curated for the policy pre-training in visuomotor driving. We aim at learning policy representations as a powerful abstraction by modeling 3D geometric scenes on large-scale unlabeled and uncalibrated YouTube driving videos. The proposed PPGeo is performed in two stages to support effective self-supervised training. In the first stage, the geometric modeling framework generates pose and depth predictions simultaneously, with two consecutive frames as input. In the second stage, the visual encoder learns driving policy representation by predicting the future ego-motion and optimizing with the photometric error based on current visual observation only. As such, the pre-trained visual encoder is equipped with rich driving policy related representations and thereby competent for multiple visuomotor driving tasks. As a side product, the pre-trained geometric modeling networks could bring further improvement to the depth and odometry estimation tasks. Extensive experiments covering a wide span of challenging scenarios have demonstrated the superiority of our proposed approach, where improvements range from 2% to even over 100% with very limited data.

## item_id: m_1432

TITLE: PivotMesh: Generic 3D Mesh Generation via Pivot Vertices Guidance

ABSTRACT: Generating compact and sharply detailed 3D meshes poses a significant challenge for current 3D generative models. Different from extracting dense meshes from neural representation, some recent works try to model the native mesh distribution (i.e., a set of triangles), which generates more compact results as humans crafted. However, due to the complexity and variety of mesh topology, most of these methods are typically limited to generating meshes with simple geometry. In this paper, we introduce a generic and scalable mesh generation framework PivotMesh, which makes an initial attempt to extend the native mesh generation to large-scale datasets. We employ a transformer-based autoencoder to encode meshes into discrete tokens and decode them from face level to vertex level hierarchically. Subsequently, to model the complex typology, our model first learns to generate pivot vertices as coarse mesh representation and then generate the complete mesh tokens with the same auto-regressive Transformer. This reduces the difficulty compared with directly modeling the mesh distribution and further improves the model controllability. PivotMesh demonstrates its versatility by effectively learning from both small datasets like Shapenet, and large-scale datasets like Objaverse and Objaverse-xl. Extensive experiments indicate that PivotMesh can generate compact and sharp 3D meshes across various categories, highlighting its great potential for native mesh modeling.

## item_id: m_1433

TITLE: LSD-Net: Look, Step and Detect for Joint Navigation and Multi-View Recognition with Deep Reinforcement Learning

ABSTRACT: Multi-view recognition is the task of classifying an object from multi-view image sequences. Instead of using a single-view for classification, humans generally navigate around a target object to learn its multi-view representation. Motivated by this human behavior, the next best view can be learned by combining object recognition with navigation in complex environments. Since deep reinforcement learning has proven successful in navigation tasks, we propose a novel multi-task reinforcement learning framework for joint multi-view recognition and navigation. Our method uses a hierarchical action space for multi-task reinforcement learning. The framework was evaluated with an environment created from the ModelNet40 dataset. Our results show improvements on object recognition and demonstrate human-like behavior on navigation.

## item_id: m_1434

TITLE: Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models

ABSTRACT: Large Language Models (LLMs) have significantly advanced natural language processing with exceptional task generalization capabilities. Low-Rank Adaption (LoRA) offers a cost-effective fine-tuning solution, freezing the original model parameters and training only lightweight, low-rank adapter matrices. However, the memory footprint of LoRA is largely dominated by the original model parameters. To mitigate this, we propose LoRAM, a memory-efficient LoRA training scheme founded on the intuition that many neurons in over-parameterized LLMs have low training utility but are essential for inference. LoRAM presents a unique twist: it trains on a pruned (small) model to obtain pruned low-rank matrices, which are then recovered and utilized with the original (large) model for inference. Additionally, minimal-cost continual pre-training, performed by the model publishers in advance, aligns the knowledge discrepancy between pruned and original models. Our extensive experiments demonstrate the efficacy of LoRAM across various pruning strategies and downstream tasks. For a model with 70 billion parameters, LoRAM enables training on a GPU with only 20G HBM, replacing an A100-80G GPU for LoRA training and 15 GPUs for full fine-tuning. Specifically, QLoRAM implemented by structured pruning combined with 4-bit quantization, for LLaMA-3.1-70B (LLaMA-2-70B), reduces the parameter storage cost that dominates the memory usage in low-rank matrix training by 15.81× (16.95×), while achieving dominant performance gains over both the original LLaMA-3.1-70B (LLaMA-2-70B) and LoRA-trained LLaMA-3.1-8B (LLaMA-2-13B). Code is available at https://github.com/junzhang-zj/LoRAM.

## item_id: m_1435

TITLE: Characterizing Audio Adversarial Examples Using Temporal Dependency

ABSTRACT: Recent studies have highlighted adversarial examples as a ubiquitous threat to different neural network models and many downstream  applications. Nonetheless, as unique data properties have inspired distinct and powerful learning principles, this paper aims to explore their potentials towards mitigating adversarial inputs. In particular, our results reveal the importance of using the temporal dependency in audio data to gain discriminate power against adversarial examples. Tested on the automatic speech recognition (ASR) tasks and three recent audio adversarial attacks, we find that (i) input transformation developed from image adversarial defense provides limited robustness improvement and is subtle to advanced attacks; (ii) temporal dependency can be exploited to gain discriminative power against audio adversarial examples and is resistant to adaptive attacks considered in our experiments. Our results not only show promising means of improving the robustness of ASR systems, but also offer novel insights in exploiting domain-specific data properties to mitigate negative effects of adversarial examples.

## item_id: m_1436

TITLE: Group Ligands Docking to Protein Pockets

ABSTRACT: Molecular docking is a key task in computational biology that has attracted increasing interest from the machine learning community. While existing methods have achieved success, they generally treat each protein-ligand pair in isolation. Inspired by the biochemical observation that ligands binding to the same target protein tend to adopt similar poses, we propose \textsc{GroupBind}, a novel molecular docking framework that simultaneously considers multiple ligands docking to a protein. This is achieved by introducing an interaction layer for the group of ligands and a triangle attention module for embedding protein-ligand and group-ligand pairs. By integrating our approach with diffusion based docking model, we set a new state-of-the-art performance on the PDBBind blind docking benchmark, demonstrating the effectiveness of our paradigm in enhancing molecular docking accuracy.

## item_id: m_1437

TITLE: Self-Aware Reinforcement Learning for Improving LLMs with Minimal Data

ABSTRACT: Reinforcement learning (RL) has demonstrated potential in enhancing the reasoning capabilities of large language models (LLMs), but such training typically demands substantial efforts in creating and annotating data. In this work, we explore improving LLMs through RL with minimal data. Our approach alternates between the LLM proposing a task and then attempting to solve it. To minimize data dependency, we introduce two novel mechanisms grounded in self-awareness: (1) self-aware difficulty prediction, where the model learns to assess task difficulty relative to its own abilities and prioritize challenging yet solvable tasks, and (2) self-aware limit breaking, where the model recognizes when a task is beyond its capability boundary and proactively requests external data to break through that limit. Extensive experiments on nine benchmarks showing a 53.8% relative improvement with less than 1.2% extra data demonstrate the efficacy of self-aware RL and underscore the promise of self-evolving agent training. Our code is available at https://anonymous.4open.science/r/SARL-B7FE/.

## item_id: m_1438

TITLE: DipDNN: Decomposed Invertible Pathway Deep Neural Networks

ABSTRACT: Deep neural networks (DNNs) enable highly accurate one-way inferences from inputs to outputs. However, there is an elevated need for consistency in bi-directional inferences, such as state estimation, signal recovery, privacy preservation, and reasoning. Since standard DNNs are not inherently invertible, previous works use multiple DNNs in a nested manner to obtain consistent and analytical forms of inverse solutions. However, such a design is not only computationally expensive due to DNN compositions, but also forces splitting the input/output equally, which is inapplicable in many applications. To reduce the restriction, other works use fixed-point iterations to enable approximation of one-to-one mapping, but the numerical approximation leads to reconstruction errors compared with the analytical inverse. To preserve the analytical form with minimum computational redundancy, we proposed decomposed-invertible-pathway DNNs (DipDNN) that decompose the nested design. We enforce one-to-one mapping in each layer by minimally adjusting the weights and activation functions of standard dense DNNs. We prove that such an adjustment guarantees strict invertibility without hurting the universal approximation. As our design relaxes the alternative stacking of nested DNNs, the proposed method does not need a fixed splitting of inputs/outputs, making it applicable for general inverse problems. To further boost the two-way learning accuracy, we show that the proposed DipDNN is easily integrated into a parallel structure. With the analytical invertibility, bi-Lipschitz stability regularization naturally fits into the scheme to avoid numerical issues. Numerical results show that DipDNN can recover the input exactly and quickly in diverse systems.

## item_id: m_1439

TITLE: Online Rounding and Learning Augmented Algorithms for Facility Location

ABSTRACT: Facility Location is a fundamental problem in clustering and unsupervised learning. Recently, significant attention has been given to studying this problem in the classical online setting enhanced with machine learning advice. While (almost) tight bounds exist for the fractional version of the problem, the integral version remains less understood, with only weaker results available. In this paper, we address this gap by presenting the first online rounding algorithms for the facility location problem, and by showing their applications to online facility location with machine learning advice.

## item_id: m_1440

TITLE: Surprise Minimizing Multi-Agent Learning with Energy-based Models

ABSTRACT: Multi-Agent Reinforcement Learning (MARL) has demonstrated significant success by virtue of collaboration across agents. Recent work, on the other hand, introduces surprise which quantifies the degree of change in an agent's environment. Surprise-based learning has received significant attention in the case of single-agent entropic settings but remains an open problem for fast-paced dynamics in multi-agent scenarios. A potential alternative to address surprise may be realized through the lens of free-energy minimization. We explore surprise minimization in multi-agent learning by utilizing the free energy across all agents in a multi-agent system. A temporal Energy-Based Model (EBM) represents an estimate of surprise which is minimized over the joint agent distribution. Our formulation of the EBM is theoretically akin to the minimum conjugate entropy objective and highlights suitable convergence towards minimum surprising states. We further validate our theoretical claims in an empirical study of multi-agent tasks demanding collaboration in the presence of fast-paced dynamics.

## item_id: m_1441

TITLE: Efficient Semi-Discrete Optimal Transport Using the Maximum Relative Error between Distributions

ABSTRACT: Semi-Discrete Optimal Transport (SDOT) transforms a continuous distribution to a discrete distribution. However, existing SDOT algorithms for high dimensional distributions have two limitations. 1) It is difficult to evaluate the quality of the transport maps produced by SDOT algorithms, because computing a high-dimensional Wasserstein distance for SDOT is intractable and 2) The transport map cannot guarantee that all target points have the corresponding source points that are mapped to them. To address these limitations, we introduce the Maximum Relative Error (\texttt{MRE}) between the target distribution and the transported distribution computed by an SDOT map. If the \texttt{MRE} is smaller than 1, then every target point is guaranteed to have an area in the source distribution that is mapped to it. We propose a statistical method to compute the lower and upper bounds of the \texttt{MRE} given a confidence threshold and a precision. The gap between the lower bound and the upper bound approaches 0 as the number of samples goes to infinity. We present an efficient Epoch Gradient Descent algorithm for SDOT (SDOT-EGD) that computes the learning rate, number of iterations, and number of epochs in order to guarantee an arbitrarily small \texttt{MRE} in expectation. Experiments on both low and high-dimensional data show that SDOT-EGD is much faster and converges much better than state-of-the-art SDOT algorithms. We also show our method's potential to improve GAN training by avoiding the oscillation caused by randomly changing the association between noise and the real images.

## item_id: m_1442

TITLE: Escaping Flat Areas via Function-Preserving Structural Network Modifications

ABSTRACT: Hierarchically embedding smaller networks in larger networks, e.g.~by increasing the number of hidden units, has been studied since the 1990s. The main interest was in understanding possible redundancies in the parameterization, as well as in studying  how such embeddings affect critical points. We take these results as a point of departure to devise a novel strategy for escaping from flat regions of the error surface and to address the slow-down of gradient-based methods experienced in plateaus of saddle points. The idea is to expand the dimensionality of a network in a way that guarantees the existence of new escape directions. We call this operation the opening of a tunnel. One may then continue with the larger network either temporarily, i.e.~closing the tunnel later, or permanently, i.e.~iteratively growing the network, whenever needed. We develop our method for fully-connected as well as convolutional layers.   Moreover, we present a practical version of our algorithm that requires no network structure modification and can be deployed as plug-and-play into any current deep learning framework. Experimentally, our method shows significant speed-ups.

## item_id: m_1443

TITLE: Dynamic Pricing on E-commerce Platform with Deep Reinforcement Learning

ABSTRACT: In this paper we develop an approach based on deep reinforcement learning (DRL) to address dynamic pricing problem on E-commerce platform. We models  real-world E-commerce dynamic pricing problem as Markov Decision Process. Environment state are defined with four groups of different business data. We make several main improvements on the state-of-the-art DRL-based dynamic pricing approaches: 1. We first extend the application of dynamic pricing to a continuous pricing action space. 2. We solve the unknown demand function problem by designing different reward functions. 3. The cold-start problem is addressed by introducing pre-training and evaluation using the historical sales data. Field experiments are designed and conducted on real-world E-commerce platform, pricing thousands of SKUs of products lasting for months. The experiment results shows that, on E-commerce platform, the difference of the revenue conversion rates (DRCR) is a more suitable reward function than the revenue only, which is different from  the conclusion from previous researches. Meanwhile, the proposed continuous action model performs better than the discrete one.

## item_id: m_1444

TITLE: Improving Subgraph Representation Learning via Multi-View Augmentation

ABSTRACT: Subgraph representation learning based on Graph Neural Network (GNN) has exhibited broad applications in scientific advancements, such as predictions of molecular structure-property relationships and collective cellular function. In particular, graph augmentation techniques have shown promising results in improving graph-based and node-based classification tasks. Still, they have rarely been explored in the existing GNN-based subgraph representation learning studies. In this study, we develop a novel multi-view augmentation mechanism to improve subgraph representation learning models and thus the accuracy of downstream prediction tasks. Our augmentation technique creates multiple variants of subgraphs and embeds these variants into the original graph to achieve highly improved training efficiency, scalability, and accuracy. Benchmark experiments on several real-world biological and physiological datasets demonstrate the superiority of our proposed multi-view augmentation techniques in subgraph representation learning.

## item_id: m_1445

TITLE: Learning to Navigate in Complex Environments

ABSTRACT: Learning to navigate in complex environments with dynamic elements is an important milestone in developing AI agents. In this work we formulate the navigation question as a reinforcement learning problem and show that data efficiency and task performance can be dramatically improved by relying on additional auxiliary tasks to bootstrap learning. In particular we consider jointly learning the goal-driven reinforcement learning problem with an unsupervised depth prediction task and a self-supervised loop closure classification task. Using this approach we can learn to navigate from raw sensory input in complicated 3D mazes, approaching human-level performance even under conditions where the goal location changes frequently. We provide detailed analysis of the agent behaviour, its ability to localise, and its network activity dynamics, that show that the agent implicitly learns key navigation abilities, with only sparse rewards and without direct supervision.

## item_id: m_1446

TITLE: TEAC: Intergrating Trust Region and Max Entropy Actor Critic for Continuous Control

ABSTRACT: Trust region methods and maximum entropy methods are two state-of-the-art branches used in reinforcement learning (RL) for the benefits of stability and exploration in continuous environments, respectively. This paper proposes to integrate both branches in a unified framework, thus benefiting from both sides. We first transform the original RL objective to a constraint optimization problem and then proposes trust entropy actor-critic (TEAC), an off-policy algorithm to learn stable and sufficiently explored policies for continuous states and actions. TEAC trains the critic by minimizing the refined Bellman error and updates the actor by minimizing KL-divergence loss derived from the closed-form solution to the Lagrangian. 
We prove that the policy evaluation and policy improvement in TEAC is guaranteed to converge.
We compare TEAC with 4 state-of-the-art solutions on 6 tasks in the MuJoCo environment. The results show that TEAC outperforms state-of-the-art solutions in terms of efficiency and effectiveness.


## item_id: m_1447

TITLE: Emergent Geometry in Neural Representations of the Visual World

ABSTRACT: How does the brain transform the complex visual world into meaningful representations that facilitate generalization across diverse conditions? One hypothesis is that the geometric structure of neural manifolds mirrors causal structures in the environment, facilitating strong generalization across natural contexts. The analysis of neural manifold structure has yielded neuroscientific insights in domains such as navigation and motor control, which often possess simple, low-dimensional structure. Vision, however, presents unique challenges due to its more complex, high-dimensional, hierarchical structure. Leveraging a digital twin model of primate V4 neurons, we conduct targeted in silico experiments that allow us to systematically investigate  the relationship between the structure of the visual world and its encoding in the visual cortex. Our findings reveal structural equivalences between world properties and neural activity patterns for rotating objects and textures. Specifically, we demonstrate the emergence of equivariant representations that disentangle latent factors such as object identity and orientation. Finally, we demonstrate that these representations facilitate out-of-distribution generalization, as a decoder trained to linearly decode the orientation of one texture can successfully transfer to novel textures. Remarkably, artificial neural networks trained on object recognition tasks exhibit similar geometric principles. These results provide empirical support for the mirroring hypothesis in visual processing and suggest universal principles govern the formation of neural representations across biological and artificial vision.

## item_id: m_1448

TITLE: Semi-supervised Outlier Detection using Generative And Adversary Framework

ABSTRACT: In a conventional binary/multi-class classification task, the decision boundary is supported by data from two or more classes. However, in one-class classification task, only data from one class are available. To build an robust outlier detector using only data from a positive class, we propose a corrupted GAN(CorGAN), a deep convolutional Generative Adversary Network requiring no convergence during training. In the adversarial process of training CorGAN, the Generator is supposed to generate outlier samples for negative class, and the Discriminator as an one-class classifier is trained to distinguish data from training datasets (i.e. positive class) and generated data from the Generator (i.e. negative class). To improve the performance of the Discriminator (one-class classifier), we also propose a lot of techniques to improve the performance of the model. The proposed model outperforms the traditional method PCA + PSVM and the solution based on Autoencoder.

## item_id: m_1449

TITLE: Harnessing the Power of Federated Learning in Federated Contextual Bandits

ABSTRACT: Federated contextual bandits (FCB), a pivotal integration of federated learning (FL) and sequential decision-making, has garnered significant attention in recent years. Prior research on FCB can be understood as specific instantiations of a unified design principle articulated in this paper: "FCB = FL + CB". Here, FL enhances agents' performance by aggregating the information of other agents' local data to better contextual bandits (CB) policies. Nevertheless, it is evident that existing approaches largely employ tailored FL protocols, often deviating from the canonical FL framework. Consequently, even renowned algorithms like FedAvg remain underutilized in FCB, let alone other FL advancements. To bridge this gap between the canonical FL study and the FL component in FCB, our work introduces a novel FCB design, termed FedIGW, that incorporates inverse gap weighting as the CB algorithm. This design permits the integration of versatile FL protocols as long as they can solve a standard FL problem. With this flexible FL choice, FedIGW advances FCB research by enabling the utilization of the entire spectrum of FL innovations, encompassing canonical algorithmic designs (e.g., FedAvg and SCAFFOLD), convergence analyses, and valuable extensions (such as personalization, robustness, and privacy). We substantiate these claims through rigorous theoretical analyses and empirical evaluations.

## item_id: m_1450

TITLE: Modeling Bounded Rationality in Multi-Agent Simulations Using Rationally Inattentive Reinforcement Learning

ABSTRACT: Multi-agent reinforcement learning (MARL) is a powerful framework for studying emergent behavior in complex agent-based simulations. However, RL agents are often assumed to be rational and behave optimally, which does not fully reflect human behavior. Here, we study more human-like RL agents which incorporate an established model of human-irrationality, the Rational Inattention (RI) model. RI models the cost of cognitive information processing using mutual information. Our RIRL framework generalizes and is more flexible than prior work by allowing for multi-timestep dynamics and information channels with heterogeneous processing costs. We evaluate RIRL in Principal-Agent (specifically manager-employee relations) problem settings of varying complexity where RI models information asymmetry (e.g. it may be costly for the manager to observe certain information about the employees). We show that using RIRL yields a rich spectrum of new equilibrium behaviors that differ from those found under rational assumptions. For instance, some forms of a Principal's inattention can increase Agent welfare due to increased compensation, while other forms of inattention can decrease Agent welfare by encouraging extra work effort. Additionally, new strategies emerge compared to those under rationality assumptions, e.g., Agents are incentivized to misrepresent their ability. These results suggest RIRL is a powerful tool towards building AI agents that can mimic real human behavior. 

## item_id: m_1451

TITLE: CDPS: Constrained DTW-Preserving Shapelets

ABSTRACT: The analysis of time series for clustering and classification is becoming ever more popular because of the increasingly ubiquitous nature of IoT, satellite constellations, and handheld and smart-wearable devices, etc. Euclidean distance is unsuitable because of potential phase shift, differences in sample duration, and compression and dilation of characteristic signals. As such, several similarity measures specific to time-series have been proposed, Dynamic Time Warping (DTW) being the most popular. Nevertheless, DTW does not respect the axioms of a metric and therefore DTW-preserving shapelets have been developed to regain these properties. This unsupervised approach to representation learning models DTW properties through the shapelet transform. This article proposes constrained DTW-preserving shapelets (CDPS), in which a limited amount of user knowledge is available in the form of must link and cannot link constraints, to guide the representation such that it better captures the user’s interpretation of the data rather than the algorithm’s bias. Subsequently, any unconstrained algorithm can be applied, e.g. K-means clustering, k-NN classification, etc, to obtain a result that fulfills the constraints (without explicit knowledge of them). Furthermore, this representation is generalisable to out-of-sample data, overcoming the limitations of standard transductive constrained-clustering algorithms. The proposed algorithm is studied on multiple time-series datasets, and its advantages over classical constrained clustering algorithms and unsupervised DTW-preserving shapelets are demonstrated. An open-source implementation based on PyTorch is available to take full advantage of GPU acceleration

## item_id: m_1452

TITLE: Variational Reparametrized Policy Learning with Differentiable Physics

ABSTRACT: We study the problem of policy parameterization for reinforcement learning (RL) with high-dimensional continuous action space. Our goal is to find a good way to parameterize the policy of continuous RL as a multi-modality distribution. To this end, we propose to treat the continuous RL policy as a generative model over the distribution of optimal trajectories. We use a diffusion process-like strategy to model the policy and derive a novel variational bound which is the optimization objective to learn the policy. To maximize the objective by gradient descent, we introduce the Reparameterized Policy Gradient Theorem. This theorem elegantly connects classical method REINFORCE and trajectory return optimization for computing the gradient of a policy. Moreover, our method enjoys strong exploration ability due to the multi-modality policy parameterization; notably, when a strong differentiable world model presents, our method also enjoys the fast convergence speed of trajectory optimization. We evaluate our method on numerical problems and manipulation tasks within a differentiable simulator. Qualitative results show its ability to capture the multi-modality distribution of optimal trajectories, and quantitative results show that it can avoid local optima and outperforms baseline approaches.

## item_id: m_1453

TITLE: Revisiting the Generalization of Adaptive Gradient Methods

ABSTRACT: A commonplace belief in the machine learning community is that using adaptive gradient methods hurts generalization. We re-examine this belief both theoretically and experimentally, in light of insights and trends from recent years.
We revisit some previous oft-cited experiments and theoretical accounts in more depth, and provide a new set of experiments in larger-scale, state-of-the-art settings. We conclude that with proper tuning, the improved training performance of adaptive optimizers does not in general carry an overfitting penalty, especially in contemporary deep learning. Finally, we synthesize a ``user's guide'' to adaptive optimizers, including some proposed modifications to AdaGrad to mitigate some of its empirical shortcomings.

## item_id: m_1454

TITLE: The Hidden Language of Diffusion Models

ABSTRACT: Text-to-image diffusion models have demonstrated an unparalleled ability to generate high-quality, diverse images from a textual prompt. However, the internal representations learned by these models remain an enigma. In this work, we present Conceptor, a novel method to interpret the internal representation of a textual concept by a diffusion model. This interpretation is obtained by decomposing the concept into a small set of human-interpretable textual elements. Applied over the state-of-the-art Stable Diffusion model, Conceptor reveals non-trivial structures in the representations of concepts. For example, we find surprising visual connections between concepts, that transcend their textual semantics. We additionally discover concepts that rely on mixtures of exemplars, biases, renowned artistic styles, or a simultaneous fusion of multiple meanings of the concept.
Through a large battery of experiments, we demonstrate Conceptor's ability to provide meaningful, robust, and faithful decompositions for a wide variety of abstract, concrete, and complex textual concepts, while allowing to naturally connect each decomposition element to its corresponding visual impact on the generated images.

## item_id: m_1455

TITLE: FastEnsemble: Benchmarking and Accelerating Ensemble-based Uncertainty Estimation for Image-to-Image Translation

ABSTRACT: Estimating prediction uncertainty and confidence of deep learning models is crucial for mission-critical machine learning applications, such as biomedical imaging for diagnostics or therapy, and self-driving cars. However, making robust uncertainty estimation is complicated given the variety of learning objectives, data modalities, types of data corruption. Previous studies often addressed such a challenge by restricting datasets to standard ones like CIFAR or ImageNet. While convenient, it is doubtful whether the same conclusion holds for real-life datasets, in which more complicated image generation tasks are involved. This paper presents a different perspective to evaluate how confidence and uncertainty estimators behave under distribution shifts, focusing on the biomedical imaging domain. Specifically, we test a series of pair-wise cell imaging datasets using a new metric to compare existing models. In addition, we introduce FastEnsemble, a fast ensemble method which only requires less than $8\%$ of the full-ensemble training time to generate a new ensemble member. Our experiments show that the proposed fast ensemble method is able to substantially improve the speed vs. quality trade-off.

## item_id: m_1456

TITLE: CATER: A diagnostic dataset for Compositional Actions & TEmporal Reasoning

ABSTRACT: Computer vision has undergone a dramatic revolution in performance, driven in large part through deep features trained on large-scale supervised datasets. However, much of these improvements have focused on static image analysis; video understanding has seen rather modest improvements. Even though new datasets and spatiotemporal models have been proposed, simple frame-by-frame classification methods often still remain competitive. We posit that current video datasets are plagued with implicit biases over scene and object structure that can dwarf variations in temporal structure. In this work, we build a video dataset with fully observable and controllable object and scene bias, and which truly requires spatiotemporal understanding in order to be solved. Our dataset, named CATER, is rendered synthetically using a library of standard 3D objects, and tests the ability to recognize compositions of object movements that require long-term reasoning. In addition to being a challenging dataset, CATER also provides a plethora of diagnostic tools to analyze modern spatiotemporal video architectures by being completely observable and controllable. Using CATER, we provide insights into some of the most recent state of the art deep video architectures.

## item_id: m_1457

TITLE: Understanding Deep Neural Networks with Rectified Linear Units

ABSTRACT: In this paper we investigate the family of functions representable by deep neural networks (DNN) with rectified linear units (ReLU). We give an algorithm to train a ReLU DNN with one hidden layer to {\em global optimality} with runtime polynomial in the data size albeit exponential in the input dimension. Further, we improve on the known lower bounds on size (from exponential to super exponential) for approximating a ReLU deep net function by a shallower ReLU net. Our gap theorems hold for smoothly parametrized families of ``hard'' functions, contrary to countable, discrete families known in the literature.  An example consequence of our gap theorems is the following: for every natural number $k$ there exists a function representable by a ReLU DNN with $k^2$ hidden layers and total size $k^3$, such that any ReLU DNN with at most $k$ hidden layers will require at least $\frac12k^{k+1}-1$ total nodes. Finally, for the family of $\R^n\to \R$ DNNs with ReLU activations, we show a new lowerbound on the number of affine pieces, which is larger than previous constructions in certain regimes of the network architecture and most distinctively our lowerbound is demonstrated by an explicit construction of a \emph{smoothly parameterized} family of functions attaining this scaling. Our construction utilizes the theory of zonotopes from polyhedral theory.

## item_id: m_1458

TITLE: GenDrugCLIP: A Generation-Augmented Framework for ContrastiveDrug-Target Representation Learning

ABSTRACT: Virtual screening (VS) has become an indispensable component of early drug discovery, aiming to identify potential ligands for a given protein target. While CLIP-style methods (e.g., DrugCLIP) have emerged as a powerful solution by enabling efficient compound retrieval through drug-target representation alignment, current models face two fundamental challenges: (1) the scarcity of true binding data for training limits coverage of diverse binding modes, and (2) the use of trivial negatives—molecules binding to other pockets—leads to a significant train-test domain gap. To address these challenges, we introduce GenDrugCLIP, a novel generation-augmented framework that repositions structure-based drug design (SBDD) models as controllable data engines. GenDrugCLIP implements a Generate-Filter-Score-Select pipeline to construct target-aware pseudo positives and hard negatives for triplet contrastive learning. Our approach not only expands the chemical space but also prevents the model from relying solely on trivial negatives. Extensive experiments on three benchmarks demonstrate that GenDrugCLIP achieves state-of-the-art performance, outperforming DrugCLIP by +7.66% in BEDROC and +7.45 in early enrichment on the DUD-E benchmark. Our work highlights the untapped potential of SBDD models as powerful data engines for representation learning, opening a new paradigm for data-efficient drug discovery.

## item_id: m_1459

TITLE: Some Considerations on Learning to Explore via Meta-Reinforcement Learning

ABSTRACT: We consider the problem of exploration in meta reinforcement learning. Two new meta reinforcement learning algorithms are suggested: E-MAML and ERL2. Results are presented on a novel environment we call 'Krazy World'  and a set of maze environments. We show E-MAML and ERL2 deliver better performance on tasks where exploration is important.

## item_id: m_1460

TITLE: Counterfactual Generative Models for Time-Varying Treatments

ABSTRACT: Estimating the counterfactual outcome of treatment is essential for decision-making in public health and clinical science, among others. Often, treatments are administered in a sequential, time-varying manner, leading to an exponentially increased number of possible counterfactual outcomes. Furthermore, in modern applications, the outcomes are high-dimensional and conventional average treatment effect estimation fails to capture disparities in individuals.  To tackle these challenges, we propose a novel conditional generative framework capable of producing counterfactual samples under time-varying treatment, without the need for explicit density estimation. 
Our method carefully addresses the distribution mismatch between the observed and counterfactual distributions via a loss function based on inverse probability weighting. We present a thorough evaluation of our method using both synthetic and real-world data. 
Our results demonstrate that our method is capable of generating high-quality counterfactual samples and outperforms the state-of-the-art baselines.

## item_id: m_1461

TITLE: Efficiently Computing Nash Equilibria in Adversarial Team Markov Games

ABSTRACT:     Computing Nash equilibrium policies is a central problem in multi-agent reinforcement learning that has received extensive attention both in theory and in practice. However, in light of computational intractability barriers in general-sum games, provable guarantees have been thus far either limited to fully competitive or cooperative scenarios or impose strong assumptions that are difficult to meet in most practical applications.
    
    In this work, we depart from those prior results by investigating infinite-horizon \emph{adversarial team Markov games}, a natural and well-motivated class of games in which a team of identically-interested players---in the absence of any explicit coordination or communication---is competing against an adversarial player. This setting allows for a unifying treatment of zero-sum Markov games and Markov potential games, and serves as a step to model more realistic strategic interactions that feature both competing and cooperative interests. Our main contribution is the first algorithm for computing stationary $\epsilon$-approximate Nash equilibria in adversarial team Markov games with computational complexity that is polynomial in all the natural parameters of the game, as well as $1/\epsilon$.
    
    The proposed algorithm is based on performing independent policy gradient steps for each player in the team, in tandem with best responses from the side of the adversary; in turn, the policy for the adversary is then obtained by solving a carefully constructed linear program. Our analysis leverages non-standard techniques to establish the KKT optimality conditions for a nonlinear program with nonconvex constraints, thereby leading to a natural interpretation of the induced Lagrange multipliers.

## item_id: m_1462

TITLE: ALFA: Adversarial Feature Augmentation for Enhanced Image Recognition

ABSTRACT: Adversarial training is an effective method to combat adversarial attacks in order to create robust neural networks. By using an auxiliary batch normalization on adversarial examples, it has been shown recently to possess great potential in improving the generalization ability of neural networks for image recognition as well. However, crafting pixel-level adversarial perturbations is computationally expensive. To address this issue, we propose AdversariaL Feature Augmentation (ALFA), which advocates adversarial training on the intermediate layers of feature embeddings. ALFA utilizes both clean and adversarial augmented features jointly to enhance standard trained networks. To eliminate laborious tuning of key parameters such as locations and strength of feature augmentations, we further design a learnable adversarial feature augmentation (L-ALFA) framework to automatically adjust the perturbation magnitude of each perturbed feature. Extensive experiments demonstrate that our proposed ALFA and L-ALFA methods achieve significant and consistent generalization improvement over strong baselines on CIFAR-10, CIFAR-100, and ImageNet benchmarks across different backbone networks for image recognition. 

## item_id: m_1463

TITLE: Deep Spike Decoder (DSD)

ABSTRACT: Spike-sorting is of central importance for neuroscience research.  We introducea novel spike-sorting method comprising a deep autoencoder trained end-to-endwith a biophysical generative model, biophysically motivated priors, and a self-supervised loss function to training a deep autoencoder. The encoder infers the ac-tion potential event times for each source, while the decoder parameters representeach source’s spatiotemporal response waveform.  We evaluate this approach inthe context of real and synthetic multi-channel surface electromyography (sEMG)data, a noisy superposition of motor unit action potentials (MUAPs).  Relative toan established spike-sorting method, this autoencoder-based approach shows su-perior recovery of source waveforms and event times.  Moreover, the biophysicalnature of the loss functions facilitates interpretability and hyperparameter tuning.Overall, these results demonstrate the efficacy and motivate further developmentof self-supervised spike sorting techniques.

## item_id: m_1464

TITLE: Unsupervised domain adaptation with imputation

ABSTRACT: Motivated by practical applications, we consider unsupervised domain adaptation for classification problems, in the presence of missing data in the target domain. More precisely, we focus on the case where there is a domain shift between source and target domains, while some components of the target data are systematically absent. We propose a way to impute non-stochastic missing data for a classification task by leveraging supervision from a complete source domain through domain adaptation. We introduce a single model performing joint domain adaptation, imputation and classification which is shown to perform well under various representative divergence families (H-divergence, Optimal Transport). We perform experiments on two families of datasets: a classical digit classification benchmark commonly used in domain adaptation papers and real world digital advertising datasets, on which we evaluate our model’s classification performance in an unsupervised setting. We analyze its behavior showing the benefit of explicitly imputing non-stochastic missing data jointly with domain adaptation.

## item_id: m_1465

TITLE: LightSAM: Parameter-Agnostic Sharpness-Aware Minimization

ABSTRACT: Sharpness-Aware Minimization (SAM) optimizer enhances the generalization ability of the machine learning model by exploring the flat minima landscape through weight perturbations. Despite its empirical success, SAM introduces an additional hyper-parameter, the perturbation radius, which causes the sensitivity of SAM to it. Moreover, it has been proved that the perturbation radius and learning rate of SAM are constrained by problem-dependent parameters to guarantee convergence. These limitations indicate the requirement of parameter-tuning in practical applications. In this paper, we propose the algorithm LightSAM which sets the perturbation radius and learning rate of SAM adaptively, thus extending the application scope of SAM. LightSAM employs three popular adaptive optimizers, including AdaGrad-Norm, AdaGrad and Adam, to replace the SGD optimizer for weight perturbation and model updating, reducing sensitivity to parameters. Theoretical results show that under weak assumptions, LightSAM could converge ideally with any choices of perturbation radius and learning rate, thus achieving parameter-agnostic. We conduct preliminary experiments on several deep learning tasks, which together with the theoretical findings validate the the effectiveness of LightSAM.

## item_id: m_1466

TITLE: Correcting Momentum in Temporal Difference Learning

ABSTRACT: A common optimization tool used in deep reinforcement learning is momentum, which consists in accumulating and discounting past gradients, reapplying them at each iteration. We argue that, unlike in supervised learning, momentum in Temporal Difference (TD) learning accumulates gradients that become doubly stale: not only does the gradient of the loss change due to parameter updates, the loss itself changes due to bootstrapping. We first show that this phenomenon exists, and then propose a first-order correction term to momentum. We show that this correction term improves sample efficiency in policy evaluation by correcting target value drift. An important insight of this work is that deep RL methods are not always best served by directly importing techniques from the supervised setting.

## item_id: m_1467

TITLE: Neural Bayes: A Generic Parameterization Method for Unsupervised Learning

ABSTRACT: We introduce a parameterization method called Neural Bayes which allows computing statistical quantities that are in general difficult to compute and opens avenues for formulating new objectives for unsupervised representation learning. Specifically, given an observed random variable $\mathbf{x}$ and a latent discrete variable $z$, we can express $p(\mathbf{x}|z)$, $p(z|\mathbf{x})$ and $p(z)$ in closed form in terms of a sufficiently expressive function (Eg. neural network) using our parameterization without restricting the class of these distributions. To demonstrate its usefulness, we develop two independent use cases for this parameterization: 

1. Disjoint Manifold Separation: Neural Bayes allows us to formulate an objective which can optimally label samples from disjoint manifolds present in the support of a continuous distribution. This can be seen as a specific form of clustering where each disjoint manifold in the support is a separate cluster. We design clustering tasks that obey this formulation and empirically show that the model optimally labels the disjoint manifolds.

2. Mutual Information Maximization (MIM): MIM has become a popular means for self-supervised representation learning. Neural Bayes allows us to compute mutual information between observed random variables $\mathbf{x}$ and latent discrete random variables $z$ in closed form. We use this for learning image representations and show its usefulness on downstream classification tasks. 

## item_id: m_1468

TITLE: Suppression helps: Lateral Inhibition-inspired Convolutional Neural Network for Image Classification

ABSTRACT: Convolutional neural networks (CNNs) have become powerful and popular tools since deep learning emerged for image classification in the computer vision field. For better recognition, the dimensions of depth and width have been explored, leading to convolutional neural networks with more layers and more channels. In addition to these factors, neurobiology also suggests the widely existing lateral inhibition (e.g., Mach band effect), which increases the contrast of nearby neuron excitation in the lateral direction, to help recognition. However, such an important mechanism has not been well explored in modern convolutional neural networks. In this paper, we explicitly explore the filter dimension in the lateral direction and propose our lateral inhibition-inspired (LI) design. Our naive design incorporates the low-pass filter, while eliminating the central weight to mimic the inhibition strength decay. The inhibition value is computed from the filtering result of the input, with a simple learnable weight parameter per channel for multiplication to decide the strength. Then the inhibition value is subtracted from the input as suppression, which could increase the contrast to help recognition. We also suggest an alternative using depthwise convolution, as a general form. Our design could work on both the plain convolution and the convolutional block with residual connection, while being compatible with existing modules. Without any channel attention along the channel dimension, the preliminary results demonstrate an absolute improvement of 3.68\% and 0.69\% over AlexNet and ResNet-18, respectively, in the ImageNet data set, with little increase in parameters, indicating the merits of our design to help feature learning for image classification.

## item_id: m_1469

TITLE: Fully Convolutional Approach for Simulating Wave Dynamics

ABSTRACT: We investigate the performance of fully convolutional networks to predict the motion and interaction of surface waves in open and closed complex geometries. We focus on a U-Net type architecture and assess its ability to capture and extrapolate wave propagation in time as well as the reflection, interference and diffraction of waves.  We investigate how well the network generalises both to long-time predictions and to geometric configurations not seen during training. We demonstrate that this neural network is capable of accurately predicting the height distribution of waves on a liquid surface within curved and multi-faceted open and closed geometries, when only simple box and right-angled corner geometries were seen during training. We found that the RMSE of the predictions remained of order $1\times10^{-4}$ times the characteristic length of the domain for at least 20 time-steps.

## item_id: m_1470

TITLE: TRACE: Coarse-to-Fine Automated Evaluation of Mobile Agents with Safety Considerations in Realistic Environments

ABSTRACT: The online evaluation of mobile agents is becoming increasingly important for both accurately assessing agent capabilities and providing reward signals for online reinforcement learning. Evaluating mobile agents on complex multi-step tasks remains challenging, as existing work suffers from limitations in reliability and generality, while overlooking issues of environmental realism and operational safety. This paper introduces TRACE (TRajectory-based Automated Coarse-to-fine Evaluation), a fully automated vision language model (VLM)-based method designed to evaluate arbitrary mobile agents across diverse environments. TRACE evaluates agent trajectories in a two-stage manner, first through step-wise assessment and then through overall judgment, which significantly reduces evaluation difficulty and enhances reliability. Potentially risky or harmful operations are also detected simultaneously during the step-wise assessment. Furthermore, we construct TRACEBench, a scalable benchmark consisting of 187 tasks from 35 commonly used mobile applications, to better reflect the actual performance of agents in realistic online environments. Task design explicitly considers operational safety, and evaluation metrics cover three key dimensions: task completion, safety, and resource consumption. Experiments show that TRACE achieves an F1 score of 0.836 with the open-sourced Qwen2.5-VL-72B-Instruct, indicating high precision as well as better usability and cost-effectiveness. Extensive evaluation of 8 representative mobile agents on TRACEBench reveals that current mobile agents still have substantial room for improvement, particularly in terms of task completion and operational safety.

## item_id: m_1471

TITLE: Predicting Medications from Diagnostic Codes with Recurrent Neural Networks

ABSTRACT: It is a surprising fact that electronic medical records are failing at one of their primary purposes, that of tracking the set of medications that the patient is actively taking. Studies estimate that up to 50% of such lists omit active drugs, and that up to 25% of all active medications do not appear on the appropriate patient list. Manual efforts to maintain these lists involve a great deal of tedious human labor, which could be reduced by computational tools to suggest likely missing or incorrect medications on a patient’s list. We report here an application of recurrent neural networks to predict the likely therapeutic classes of medications that a patient is taking, given a sequence of the last 100 billing codes in their record. Our best model was a GRU that achieved high prediction accuracy (micro-averaged AUC 0.93, Label Ranking Loss 0.076), limited by hardware constraints on model size. Additionally, examining individual cases revealed that many of the predictions marked incorrect were likely to be examples of either omitted medications or omitted billing codes, supporting our assertion of a substantial number of errors and omissions in the data, and the likelihood of models such as these to help correct them.

## item_id: m_1472

TITLE: Graph Classification with 2D Convolutional Neural Networks

ABSTRACT: Graph classification is currently dominated by graph kernels, which, while powerful, suffer some significant limitations. Convolutional Neural Networks (CNNs) offer a very appealing alternative. However, processing graphs with CNNs is not trivial. To address this challenge, many sophisticated extensions of CNNs have recently been proposed. In this paper, we reverse the problem: rather than proposing yet another graph CNN model, we introduce a novel way to represent graphs as multi-channel image-like structures that allows them to be handled by vanilla 2D CNNs. Despite its simplicity, our method proves very competitive to state-of-the-art graph kernels and graph CNNs, and outperforms them by a wide margin on some datasets. It is also preferable to graph kernels in terms of time complexity. Code and data are publicly available.

## item_id: m_1473

TITLE: Learning to Generalize Compositionally by Transferring Across Semantic Parsing Tasks

ABSTRACT: Neural network models often generalize poorly to mismatched domains or distributions. In NLP, this issue arises in particular when models are expected to generalize compositionally, that is, to novel combinations of familiar words and constructions. We investigate learning representations that facilitate transfer learning from one compositional task to another: the representation and the task-specific layers of the models are strategically trained differently on a pre-finetuning task such that they generalize well on mismatched splits that require compositionality. We apply this method to semantic parsing, using three very different datasets, COGS, GeoQuery and SCAN, used alternately as the pre-finetuning and target task. Our method significantly improves compositional generalization over baselines on the test set of the target task, which is held out during fine-tuning. Ablation studies characterize the utility of the major steps in the proposed algorithm and support our hypothesis. 

## item_id: m_1474

TITLE: Learning from Label Proportions with Consistency Regularization

ABSTRACT: The problem of learning from label proportions (LLP) involves training classifiers with weak labels on bags of instances, rather than strong labels on individual instances. The weak labels only contain the label proportions of each bag. The LLP problem is important for many practical applications that only allow label proportions to be collected because of data privacy or annotation costs, and has recently received lots of research attention. Most existing works focus on extending supervised learning models to solve the LLP problem, but the weak learning nature makes it hard to further improve LLP performance with a supervised angle. In this paper, we take a different angle from semi-supervised learning.
In particular, we propose a novel model inspired by consistency regularization, a popular concept in semi-supervised learning that encourages the model to produce a decision boundary that better describes the data manifold. With the introduction of consistency regularization, we further extend our study to non-uniform bag-generation and validation-based parameter-selection procedures that better match practical needs. Experiments not only justify that LLP with consistency regularization achieves superior performance, but also demonstrate the practical usability of the proposed procedures.

## item_id: m_1475

TITLE: Incorporating long-range consistency in CNN-based texture generation

ABSTRACT: Gatys et al. (2015) showed that pair-wise products of features in a convolutional network are a very effective representation of image textures. We propose a simple modification to that representation which makes it possible to incorporate long-range structure into image generation, and to render images that satisfy various symmetry constraints. We show how this can greatly improve rendering of regular textures and of images that contain other kinds of symmetric structure. We also present applications to inpainting and season transfer.

## item_id: m_1476

TITLE: WordsWorth Scores for Attacking CNNs and LSTMs for Text Classification

ABSTRACT: Black box attacks on traditional deep learning models trained for text classifica- tion target important words in a piece of text, in order to change model prediction. Current approaches towards highlighting important features are time consuming and require large number of model queries. We present a simple yet novel method to calculate word importance scores, based on model predictions on single words. These scores, which we call WordsWorth scores, need to be calculated only once for the training vocabulary. They can be used to speed up any attack method that requires word importance, with negligible loss of attack performance. We run ex- periments on a number of datasets trained on word-level CNNs and LSTMs, for sentiment analysis and topic classification and compare to state-of-the-art base- lines. Our results show the effectiveness of our method in attacking these models with success rates that are close to the original baselines. We argue that global importance scores act as a very good proxy for word importance in a local context because words are a highly informative form of data. This aligns with the manner in which humans interpret language, with individual words having well- defined meaning and powerful connotations. We further show that these scores can be used as a debugging tool to interpret a trained model by highlighting rele- vant words for each class. Additionally, we demonstrate the effect of overtraining on word importance, compare the robustness of CNNs and LSTMs, and explain the transferability of adversarial examples across a CNN and an LSTM using these scores. We highlight the fact that neural networks make highly informative pre- dictions on single words.

## item_id: m_1477

TITLE: Encouraging Disentangled and Convex Representation with Controllable Interpolation Regularization

ABSTRACT: We focus on controllable disentangled representation learning (C-Dis-RL), where users can control the partition of the disentangled latent space to factorize dataset attributes (concepts) for downstream tasks. Two general problems remain underexplored in current methods: (1) They lack comprehensive disentanglement constraints, especially missing the minimization of mutual information between different attributes across latent and observation domains. (2) They lack convexity constraints in disentangled latent space, which is important for meaningfully manipulating specific attributes for downstream tasks. To encourage both comprehensive C-Dis-RL and convexity simultaneously, we propose a simple yet efficient method: Controllable Interpolation Regularization (CIR), which creates a positive loop
where the disentanglement and convexity can help each other. Specifically, we conduct controlled interpolation in latent space during training and ’reuse’ the encoder to help form a ’perfect disentanglement’ regularization. In that case, (a) disentanglement loss implicitly enlarges the potential ’understandable’ distribution to encourage convexity; (b) convexity can in turn improve robust and precise disentanglement. CIR is a general module and we merge CIR with three different algorithms: ELEGANT, I2I-Dis, and GZS-Net to show the compatibility and effectiveness. Qualitative and quantitative experiments show improvement in C-Dis-RL and latent convexity by CIR. This further improves downstream tasks: controllable image synthesis, cross-modality image translation and zero-shot synthesis. More
experiments demonstrate CIR can also improve other downstream tasks, such as new attribute value mining, data augmentation, and eliminating bias for fairness.

## item_id: m_1478

TITLE: Transforming Recurrent Neural Networks with Attention and Fixed-point Equations

ABSTRACT: Transformer has achieved state of the art performance in multiple Natural Language Processing tasks recently. Yet the Feed Forward Network(FFN) in a Transformer block is computationally expensive. In this paper, we present a framework to transform Recurrent Neural Networks(RNNs) and their variants into self-attention-style models, with an approximation of Banach Fixed-point Theorem. Within this framework, we propose a new model, StarSaber, by solving a set of equations obtained from RNN with Fixed-point Theorem and further approximate it with a Multi-layer Perceptron. It provides a view of stacking layers. StarSaber achieves better performance than both the vanilla Transformer and an improved version called ReZero on three datasets and is more computationally efficient, due to the reduction of Transformer's FFN layer. It has two major parts. One is a way to encode position information with two different matrices. For every position in a sequence, we have a matrix operating on positions before it and another matrix operating on positions after it. The other is the introduction of direct paths from the input layer to the rest of layers. Ablation studies show the effectiveness of these two parts. We additionally show that other RNN variants such as RNNs with gates can also be transformed in the same way, outperforming the two kinds of Transformers as well.

## item_id: m_1479

TITLE: Contrastive Mutual Information Maximization for Binary Neural Networks

ABSTRACT: Neural network binarization accelerates deep models by quantizing their weights and activations into 1-bit. However, there is still a huge performance gap between Binary Neural Networks (BNNs) and their full-precision counterparts. As the quantization error caused by weights binarization has been reduced in earlier works, the activations binarization becomes the major obstacle for further improvement of the accuracy. In spite of studies about the full-precision networks highlighting the distributions of activations, few works study the distribution of the binary activations in BNNs. In this paper, we introduce mutual information as the metric to measure the information shared by the binary and the latent full-precision activations. Then we maximize the mutual information by establishing a contrastive learning framework while training BNNs. Specifically, the representation ability of the BNNs is greatly strengthened via pulling the positive pairs with binary and full-precision activations from the same input samples, as well as pushing negative pairs from different samples (the number of negative pairs can be exponentially large). This benefits the downstream tasks, not only classification but also segmentation and depth estimation, etc. The experimental results show that our method can be implemented as a pile-up module on existing state-of-the-art binarization methods and can remarkably improve the performance over them on CIFAR-10/100 and ImageNet, in addition to the good generalization ability on NYUD-v2.

## item_id: m_1480

TITLE: Adversarial Defense Via Data Dependent Activation Function and  Total Variation Minimization

ABSTRACT: We improve the robustness of deep neural nets  to adversarial attacks by using an interpolating function as the output activation.   This data-dependent activation function remarkably improves both classification accuracy and stability to adversarial perturbations. Together with the total variation minimization of adversarial images and augmented training, under the strongest attack, we achieve up to 20.6%, 50.7%, and 68.7% accuracy improvement w.r.t.  the fast gradient sign method, iterative fast gradient sign method, and Carlini-WagnerL2attacks, respectively.  Our defense strategy is additive to many of the existing methods.  We give an intuitive explanation of our defense strategy via analyzing the geometry of the feature space. For reproducibility, the code will be available on GitHub.

## item_id: m_1481

TITLE: DROPS: Deep Retrieval of Physiological Signals via Attribute-specific Clinical Prototypes

ABSTRACT: The ongoing digitization of health records within the healthcare industry results in large-scale datasets. Manually extracting clinically-useful insight from such datasets is non-trivial. However, doing so at scale while simultaneously leveraging patient-specific attributes such as sex and age can assist with clinical-trial enrollment, medical school educational endeavours, and the evaluation of the fairness of neural networks. To facilitate the reliable extraction of clinical information, we propose to learn embeddings, known as clinical prototypes (CPs), via supervised contrastive learning. We show that CPs can be efficiently used for large-scale retrieval and clustering of physiological signals based on multiple patient attributes. We also show that CPs capture attribute-specific semantic relationships.

## item_id: m_1482

TITLE: Incremental Network Quantization: Towards Lossless CNNs with Low-precision Weights

ABSTRACT: This paper presents incremental network quantization (INQ), a novel method, targeting to efficiently convert any pre-trained full-precision convolutional neural network (CNN) model into a low-precision version whose weights are constrained to be either powers of two or zero. Unlike existing methods which are struggled in noticeable accuracy loss, our INQ has the potential to resolve this issue, as benefiting from two innovations. On one hand, we introduce three interdependent operations, namely weight partition, group-wise quantization and re-training. A well-proven measure is employed to divide the weights in each layer of a pre-trained CNN model into two disjoint groups. The weights in the first group are responsible to form a low-precision base, thus they are quantized by a variable-length encoding method. The weights in the other group are responsible to compensate for the accuracy loss from the quantization, thus they are the ones to be re-trained. On the other hand, these three operations are repeated on the latest re-trained group in an iterative manner until all the weights are converted into low-precision ones, acting as an incremental network quantization and accuracy enhancement procedure. Extensive experiments on the ImageNet classification task using almost all known deep CNN architectures including AlexNet, VGG-16, GoogleNet and ResNets well testify the efficacy of the proposed method. Specifically, at 5-bit quantization (a variable-length encoding: 1 bit for representing zero value, and the remaining 4 bits represent at most 16 different values for the powers of two), our models have improved accuracy than the 32-bit floating-point references. Taking ResNet-18 as an example, we further show that our quantized models with 4-bit, 3-bit and 2-bit ternary weights have improved or very similar accuracy against its 32-bit floating-point baseline. Besides, impressive results with the combination of network pruning and INQ are also reported. We believe that our method sheds new insights on how to make deep CNNs to be applicable on mobile or embedded devices. The code will be made publicly available.

## item_id: m_1483

TITLE: How Useful are Gradients for OOD Detection Really?

ABSTRACT: One critical challenge in deploying machine learning models in real-life applications is out-of-distribution (OOD) detection. Given a predictive model which is accurate on in distribution (ID) data, an OOD detection system can further equip the model with the option to defer prediction when the input is novel and the model has low confidence. Notably, there has been some recent interest in utilizing gradient information in pretrained models for OOD detection. While these methods are competitive, we argue that previous works conflate their performance with the necessity of gradients. In this work, we provide an in-depth analysis of gradient-based methods and elucidate the key components that warrant their OOD detection performance. We further demonstrate that a general, non-gradient-based family of OOD detection methods are just as competitive, casting doubt on the usefulness of gradients for OOD detection

## item_id: m_1484

TITLE: Diverse Machine Translation with a Single Multinomial Latent Variable

ABSTRACT: There are many ways to translate a sentence into another language. Explicit modeling of such uncertainty may enable better model fitting to the data and it may enable users to express a preference for how to translate a piece of content. Latent variable models are a natural way to represent uncertainty. Prior work investigated the use of multivariate continuous and discrete latent variables, but their interpretation and use for generating a diverse set of hypotheses have been elusive. In this work, we drastically simplify the model, using just a single multinomial latent variable. The resulting mixture of experts model can be trained efficiently via hard-EM and can generate a diverse set of hypothesis by parallel greedy decoding. We perform extensive experiments on three WMT benchmark datasets that have multiple human references, and we show that our model provides a better trade-off between quality and diversity of generations compared to all baseline methods.\footnote{Code to reproduce this work is available at: anonymized URL.}

## item_id: m_1485

TITLE: Correcting Three Existing Beliefs on Mutual Information in Contrastive Learning

ABSTRACT: Contrastive learning has played a pivotal role in the recent success of unsupervised representation learning. It has been commonly explained with instance discrimination and a mutual information loss, and some of the fundamental explanations are based on mutual information analysis. In this work, we develop new methods that enable rigorous analysis of mutual information in contrastive learning. Using the methods, we investigate three existing beliefs and show that they are incorrect. Based on the investigation results, we address two issues in the discussion section. In particular, we question if contrastive learning is indeed an unsupervised representation learning method because the current framework of contrastive learning relies on validation performance for tuning the augmentation design.

## item_id: m_1486

TITLE: Equal Long-term Benefit Rate: Adapting Static Fairness Notions to Sequential Decision Making

ABSTRACT: Decisions made by machine learning models may have lasting impacts over time, making long-term fairness a crucial consideration. 
It has been shown that when ignoring the long-term effect, naively imposing fairness criterion in static settings can actually exacerbate bias over time. To explicitly address biases in sequential decision-making, recent works formulate long-term fairness notions in Markov Decision Process (MDP) framework. They define the long-term bias to be the sum of static bias over each time step. However, we demonstrate that naively summing up the step-wise bias can cause a false sense of fairness since it fails to consider the importance difference of different time steps during transition. In this work, we introduce a long-term fairness notion called Equal Long-term Benefit Rate (ELBERT), which explicitly considers varying temporal importance and adapts static fairness principles to the sequential setting. Moreover, we show that the policy gradient of Long-term Benefit Rate can be analytically reduced to standard policy gradient. This makes standard policy optimization methods applicable for reducing bias, leading to our bias mitigation method ELBERT-PO. Extensive experiments on diverse sequential decision making environments consistently show that ELBERT-PO significantly reduces bias and maintains high utility.

## item_id: m_1487

TITLE: Efficient Vector Representation for Documents through Corruption

ABSTRACT: We present an efficient document representation learning framework, Document Vector through Corruption (Doc2VecC). Doc2VecC represents each document as a simple average of word embeddings. It ensures a representation generated as such captures the semantic meanings of the document during learning. A corruption model is included, which introduces a data-dependent regularization that favors informative or rare words while forcing the embeddings of common and non-discriminative ones to be close to zero. Doc2VecC produces significantly better word embeddings than Word2Vec. We compare Doc2VecC with several state-of-the-art document representation learning algorithms. The simple model architecture introduced by Doc2VecC matches or out-performs the state-of-the-art in generating high-quality document representations for sentiment analysis, document classification as well as semantic relatedness tasks. The simplicity of the model enables training on billions of words per hour on a single machine. At the same time, the model is very efficient in generating representations of unseen documents at test time.


## item_id: m_1488

TITLE: Communicating Hierarchical Neural Controllers for Learning Zero-shot Task Generalization

ABSTRACT: The ability to generalize from past experience to solve previously unseen tasks is a key research challenge in reinforcement learning (RL). In this paper, we consider RL tasks defined as a sequence of high-level instructions described by natural language and study two types of generalization: to unseen and longer sequences of previously seen instructions, and to sequences where the instructions themselves were previously not seen. 
We present a novel hierarchical deep RL architecture that consists of two interacting neural controllers: a meta controller that reads instructions and repeatedly communicates subtasks to a subtask controller that in turn learns to perform such subtasks. To generalize better to unseen instructions, we propose a regularizer that encourages to learn subtask embeddings that capture correspondences between similar subtasks. We also propose a new differentiable neural network architecture in the meta controller that learns temporal abstractions which makes learning more stable under delayed reward. Our architecture is evaluated on a stochastic 2D grid world and a 3D visual environment where the agent should execute a list of instructions. We demonstrate that the proposed architecture is able to generalize well over unseen instructions as well as longer lists of instructions.

## item_id: m_1489

TITLE: Efficient Masked AutoEncoder for Video Object Counting and A Large-Scale Benchmark

ABSTRACT: The dynamic imbalance of the fore-background is a major challenge in video object counting, which is usually caused by the sparsity of target objects. This remains understudied in existing works and often leads to severe under-/over-prediction errors. To tackle this issue in video object counting, we propose a density-embedded Efficient Masked Autoencoder Counting (E-MAC) framework in this paper. To empower the model’s representation ability on density regression, we develop a new Density-Embedded Masked mOdeling (DEMO) method, which first takes the density map as an auxiliary modality to perform multimodal self-representation learning for image and density map. Although DEMO contributes to effective cross-modal regression guidance, it also brings in redundant background information, making it difficult to focus on the foreground regions. To handle this dilemma, we propose an efficient spatial adaptive masking derived from density maps to boost efficiency. Meanwhile, we employ an optical flow-based temporal collaborative fusion strategy to effectively capture the dynamic variations across frames, aligning features to derive multi-frame density residuals. The counting
accuracy of the current frame is boosted by harnessing the information from adjacent frames. In addition, considering that most existing datasets are limited to human-centric scenarios, we propose a large video bird counting dataset, DroneBird, in natural scenarios for migratory bird protection. Extensive experiments on three crowd datasets and our DroneBird validate our superiority against
the counterparts. The code and dataset are available.

## item_id: m_1490

TITLE: RNAS-CL: Robust Neural Architecture Search by Cross-Layer Knowledge Distillation

ABSTRACT: Deep Neural Networks are vulnerable to adversarial attacks. Neural Architecture Search (NAS), one of the driving tools of deep neural networks, demonstrates superior performance in prediction accuracy in various machine learning applications. However, it is unclear how it performs against adversarial attacks. Given the presence of a robust teacher, it would be interesting to investigate if NAS would produce robust neural architecture by inheriting robustness from the teacher. In this paper, we propose Robust Neural Architecture Search by Cross-Layer Knowledge Distillation (RNAS-CL), a novel NAS algorithm that improves the robustness of NAS by learning from a robust teacher through cross-layer knowledge distillation. Unlike previous knowledge distillation methods that encourage close student/teacher output only in the last layer, RNAS-CL automatically searches for the best teacher layer to supervise each student layer. Experimental result evidences the effectiveness of RNAS-CL and shows that RNAS-CL produces small and robust neural architecture.

## item_id: m_1491

TITLE: An Attention-Based Model for Learning Dynamic Interaction Networks

ABSTRACT: While machine learning models achieve human-comparable performance on sequential data, exploiting structured knowledge is still a challenging problem. Spatio-temporal graphs have been proved to be a useful tool to abstract interaction graphs and previous works exploits carefully designed feed-forward architecture to preserve such structure. We argue to scale such network design to real-world problem, a model needs to automatically learn a meaningful representation of the possible relations. Learning such interaction structure is not trivial: on the one hand, a model has to discover the hidden relations between different problem factors in an unsupervised way; on the other hand, the mined relations have to be interpretable. 

In this paper, we propose an attention module able to project a graph sub-structure in a fixed size embedding, preserving the influence that the neighbours exert on a given vertex. On a comprehensive evaluation done on real-world as well as toy task, we found our model competitive against strong baselines.

## item_id: m_1492

TITLE: Unsupervised Audiovisual Synthesis via Exemplar Autoencoders

ABSTRACT: We present an unsupervised approach that converts the input speech of any individual into audiovisual streams of potentially-infinitely many output speakers. Our approach builds on simple autoencoders that project out-of-sample data onto the distribution of the training set. We use exemplar autoencoders to learn the voice, stylistic prosody, and visual appearance of a specific target exemplar speech. In contrast to existing methods, the proposed approach can be easily extended to an arbitrarily large number of speakers and styles using only 3 minutes of target audio-video data, without requiring any training data for the input speaker. To do so, we learn audiovisual bottleneck representations that capture the structured linguistic content of speech. We outperform prior approaches on both audio and video synthesis.


## item_id: m_1493

TITLE: Self-Tuning Networks: Bilevel Optimization of Hyperparameters using Structured Best-Response Functions

ABSTRACT: Hyperparameter optimization can be formulated as a bilevel optimization problem, where the optimal parameters on the training set depend on the hyperparameters. We aim to adapt regularization hyperparameters for neural networks by fitting compact approximations to the best-response function, which maps hyperparameters to optimal weights and biases. We show how to construct scalable best-response approximations for neural networks by modeling the best-response as a single network whose hidden units are gated conditionally on the regularizer. We justify this approximation by showing the exact best-response for a shallow linear network with L2-regularized Jacobian can be represented by a similar gating mechanism. We fit this model using a gradient-based hyperparameter optimization algorithm which alternates between approximating the best-response around the current hyperparameters and optimizing the hyperparameters using the approximate best-response function. Unlike other gradient-based approaches, we do not require differentiating the training loss with respect to the hyperparameters, allowing us to tune discrete hyperparameters, data augmentation hyperparameters, and dropout probabilities. Because the hyperparameters are adapted online, our approach discovers hyperparameter schedules that can outperform fixed hyperparameter values. Empirically, our approach outperforms competing hyperparameter optimization methods on large-scale deep learning problems. We call our networks, which update their own hyperparameters online during training, Self-Tuning Networks (STNs).

## item_id: m_1494

TITLE: Interleaving Optimizers for DNN Training

ABSTRACT: Optimizers are crucial in deep neural network (DNN) training, affecting model quality and convergence. Researchers have found that different optimizers often suit different problems or different stages of a problem. Hence, some studies have tried to combine different optimizers to better train DNNs. However, existing methods are limited to simple optimizer switch strategies, which leads to unstable model quality and slow convergence. In this paper, we propose a fine-grain optimizer switch method called Iterleaving Optimizer for Model Training (IOMT), which automatically switches to the appropriate optimizer and hyperparameters based on the training stage information, achieving faster convergence and better model quality. IOMT employs surrogate models to estimate the performance of different optimizers during training and is supported by a transferability assessment to predict the training cost. By combining the transferability assessment, performance estimation, and training process information with an acquisition function, IOMT calculates the optimization gain of each optimizer and switches the optimizer with the largest gain for the next training stage. The experimental results on full training and fine-tuning demonstrate that IOMT achieves faster convergence (e.g., 10\% on the *stl10* dataset) and better performance (e.g., 3\% accuracy improvement on the *cifar10* dataset) compared to existing methods.

## item_id: m_1495

TITLE: Snapshot Ensembles: Train 1, Get M for Free

ABSTRACT: Ensembles of neural networks are known to be much more robust and accurate than individual networks. However, training multiple deep networks for model averaging is computationally expensive. In this paper, we propose a method to obtain the seemingly contradictory goal of ensembling multiple neural networks at no additional training cost. We achieve this goal by training a single neural network, converging to several local minima along its optimization path and saving the model parameters.  To obtain repeated rapid convergence, we leverage recent work on cyclic learning rate schedules. The resulting technique, which we refer to as Snapshot Ensembling, is simple, yet surprisingly effective.  We show in a series of experiments that our approach is compatible with diverse network architectures and learning tasks. It consistently yields  lower error rates than state-of-the-art single models at no additional training cost, and compares favorably with traditional network ensembles. On CIFAR-10 and CIFAR-100 our DenseNet Snapshot Ensembles obtain error rates of 3.4% and 17.4% respectively.

## item_id: m_1496

TITLE: LipNet: End-to-End Sentence-level Lipreading

ABSTRACT: Lipreading is the task of decoding text from the movement of a speaker's mouth. Traditional approaches separated the problem into two stages: designing or learning visual features, and prediction. More recent deep lipreading approaches are end-to-end trainable (Wand et al., 2016; Chung & Zisserman, 2016a). However, existing work on models trained end-to-end perform only word classification, rather than sentence-level sequence prediction. Studies have shown that human lipreading performance increases for longer words (Easton & Basala, 1982), indicating the importance of features capturing temporal context in an ambiguous communication channel. Motivated by this observation, we present LipNet, a model that maps a variable-length sequence of video frames to text, making use of spatiotemporal convolutions, a recurrent network, and the connectionist temporal classification loss, trained entirely end-to-end. To the best of our knowledge, LipNet is the first end-to-end sentence-level lipreading model that simultaneously learns spatiotemporal visual features and a sequence model. On the GRID corpus, LipNet achieves 95.2% accuracy in sentence-level, overlapped speaker split task, outperforming experienced human lipreaders and the previous 86.4% word-level state-of-the-art accuracy (Gergen et al., 2016).

## item_id: m_1497

TITLE: Attention on Abstract Visual Reasoning

ABSTRACT: Attention mechanisms have been boosting the performance of deep learning models on a wide range of applications, ranging from speech understanding to program induction.  However, despite experiments from psychology which suggest that attention plays an essential role in visual reasoning, the full potential of attention mechanisms has so far not been explored to solve abstract cognitive tasks on image data. In this work, we propose a hybrid network architecture, grounded on self-attention and relational reasoning. We call this new model Attention Relation Network (ARNe). ARNe combines features from the recently introduced Transformer and the Wild Relation Network (WReN). We test ARNe on the Procedurally Generated Matrices (PGMs) datasets for abstract visual reasoning. ARNe excels the WReN model on this task by 11.28 ppt. Relational concepts between objects are efficiently learned demanding only 35% of the training samples to surpass reported accuracy of the base line model. Our proposed hybrid model, represents an alternative on learning abstract relations using self-attention and demonstrates that the Transformer network is also well suited for abstract visual reasoning.

## item_id: m_1498

TITLE: The Information-Autoencoding Family: A Lagrangian Perspective on Latent Variable Generative Modeling

ABSTRACT: A variety of learning objectives have been recently proposed for training generative models. We show that many of them, including InfoGAN, ALI/BiGAN, ALICE, CycleGAN, VAE, $\beta$-VAE, adversarial autoencoders, AVB, and InfoVAE, are Lagrangian duals of the same primal optimization problem. This generalization reveals the implicit modeling trade-offs  between flexibility and  computational requirements being made by these models. Furthermore, we characterize the class of all objectives that can be optimized under certain computational constraints.
Finally, we show how this new Lagrangian perspective can explain undesirable behavior of existing methods and provide new principled solutions.

## item_id: m_1499

TITLE: Black-box Adversarial Attacks with Bayesian Optimization

ABSTRACT: We focus on the problem of black-box adversarial attacks, where the aim is to generate adversarial examples using information limited to loss function evaluations of input-output pairs. We use Bayesian optimization (BO) to specifically
cater to scenarios involving low query budgets to develop query efficient adversarial attacks. We alleviate the issues surrounding BO in regards to optimizing high dimensional deep learning models by effective dimension upsampling techniques. Our proposed approach achieves performance comparable to the state of the art black-box adversarial attacks albeit with a much lower average query count. In particular, in low query budget regimes, our proposed method reduces the query count up to 80% with respect to the state of the art methods.

## item_id: m_1500

TITLE: Learning to Describe Scenes with Programs

ABSTRACT: Human scene perception goes beyond recognizing a collection of objects and their pairwise relations. We understand higher-level, abstract regularities within the scene such as symmetry and repetition. Current vision recognition modules and scene representations fall short in this dimension. In this paper, we present scene programs, representing a scene via a symbolic program for its objects, attributes, and their relations. We also propose a model that infers such scene programs by exploiting a hierarchical, object-based scene representation. Experiments demonstrate that our model works well on synthetic data and transfers to real images with such compositional structure. The use of scene programs has enabled a number of applications, such as complex visual analogy-making and scene extrapolation.
