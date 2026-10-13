# Batch 04 — 25 items

## item_id: r3_075

TITLE: Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy

ABSTRACT: The rapid growth of AI conference submissions has created an overwhelming reviewing burden. To alleviate this, recent venues such as ICLR 2026 introduced a reviewer nomination policy: each submission must nominate one of its authors as a reviewer, and any paper nominating an irresponsible reviewer is desk-rejected.
We study this new policy from the perspective of author welfare. Assuming each author carries a probability of being irresponsible, we ask: how can authors (or automated systems) nominate reviewers to minimize the risk of desk rejections?
We formalize and analyze three variants of the desk-rejection risk minimization problem. The basic problem, which minimizes expected desk rejections, is solved optimally by a simple greedy algorithm. We then introduce hard and soft nomination limit variants that constrain how many papers may nominate the same author, preventing widespread failures if one author is irresponsible. These formulations connect to classical optimization frameworks, including minimum-cost flow and linear programming, allowing us to design efficient, principled nomination strategies. Our results provide the first theoretical study for reviewer nomination policies, offering both conceptual insights and practical directions for authors to wisely choose which co-author should serve as the nominated reciprocal reviewer.

## item_id: r3_076

TITLE: Whitening and second order optimization both destroy information about the dataset, and can make generalization impossible

ABSTRACT: Machine learning is predicated on the concept of generalization: a model achieving low error on a sufficiently large training set should also perform well on novel samples from the same distribution. We show that both data whitening and second order optimization can harm or entirely prevent generalization. In general, model training harnesses information contained in the sample-sample second moment matrix of a dataset. For a general class of models, namely models with a fully connected first layer, we prove that the information contained in this matrix is the only information which can be used to generalize. Models trained using whitened data, or with certain second order optimization schemes, have less access to this information; in the high dimensional regime they have no access at all, resulting in poor or nonexistent generalization ability. We experimentally verify these predictions for several architectures, and further demonstrate that generalization continues to be harmed even when theoretical requirements are relaxed. However, we also show experimentally that regularized second order optimization can provide a practical tradeoff, where training is accelerated but less information is lost, and generalization can in some circumstances even improve.

## item_id: r3_077

TITLE: #InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models

ABSTRACT: Pre-trained large language models (LLMs) can understand and align with human instructions by supervised fine-tuning (SFT).
It is commonly believed that diverse and complex SFT data are of the essence to enable good instruction-following abilities.
However, such diversity and complexity are obscure and lack quantitative analyses.
In this work, we propose InsTag, an open-set instruction tagging method, to identify semantics and intentions of human instructions by tags that provide access to definitions and quantified analyses of instruction diversity and complexity.
We obtain 6.6K fine-grained tags to describe instructions from popular open-sourced SFT datasets comprehensively.
We find that the abilities of aligned LLMs benefit from more diverse and complex instructions in SFT data.
Based on this observation, we propose a data sampling procedure based on InsTag, and select 6K diverse and complex samples from open-source datasets for SFT.
The resulting models, TagLM, outperform open-source models based on considerably larger SFT data evaluated by MT-Bench, echoing the importance of instruction diversity and complexity and the effectiveness of InsTag.
InsTag has robust potential to be extended to more applications beyond the data selection as it provides an effective way to analyze the distribution of instructions.

## item_id: r3_078

TITLE: FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization

ABSTRACT: We study the offline meta-reinforcement learning (OMRL) problem, a paradigm which enables reinforcement learning (RL) algorithms to quickly adapt to unseen tasks without any interactions with the environments, making RL truly practical in many real-world applications. This problem is still not fully understood, for which two major challenges need to be addressed. First, offline RL usually suffers from bootstrapping errors of out-of-distribution state-actions which leads to divergence of value functions. Second, meta-RL requires efficient and robust task inference learned jointly with control policy. In this work, we enforce behavior regularization on learned policy as a general approach to offline RL, combined with a deterministic context encoder for efficient task inference. We propose a novel negative-power distance metric on bounded context embedding space, whose gradients propagation is detached from the Bellman backup. We provide analysis and insight showing that some simple design choices can yield substantial improvements over recent approaches involving meta-RL and distance metric learning. To the best of our knowledge, our method is the first model-free and end-to-end OMRL algorithm, which is computationally efficient and demonstrated to outperform prior algorithms on several meta-RL benchmarks.

## item_id: r3_079

TITLE: Just How Toxic is Data Poisoning?  A Benchmark for Backdoor and Data Poisoning Attacks

ABSTRACT: Data poisoning and backdoor attacks manipulate training data in order to cause models to fail during inference.  A recent survey of industry practitioners found that data poisoning is the number one concern among threats ranging from model stealing to adversarial attacks. However, we find that the impressive performance evaluations from data poisoning attacks are, in large part, artifacts of inconsistent experimental design. Moreover, we find that existing poisoning methods have been tested in contrived scenarios, and many fail in more realistic settings. In order to promote fair comparison in future work, we develop standardized benchmarks for data poisoning and backdoor attacks.

## item_id: r3_080

TITLE: The Deep Bootstrap Framework: Good Online Learners are Good Offline Generalizers

ABSTRACT: We propose a new framework for reasoning about generalization in deep learning. 
The core idea is to couple the Real World, where optimizers take stochastic gradient steps on the empirical loss, to an Ideal World, where optimizers take steps on the population loss. This leads to an alternate decomposition of test error into: (1) the Ideal World test error plus (2) the gap between the two worlds. If the gap (2) is universally small, this reduces the problem of generalization in offline learning to the problem of optimization in online learning.
We then give empirical evidence that this gap between worlds can be small in realistic deep learning settings, in particular supervised image classification. For example, CNNs generalize better than MLPs on image distributions in the Real World, but this is "because" they optimize faster on the population loss in the Ideal World. This suggests our framework is a useful tool for understanding generalization in deep learning, and lays the foundation for future research in this direction. 

## item_id: r3_081

TITLE: Learn from the Past: Dynamic Data Pruning with Historically Weighted Bernoulli Sampling

ABSTRACT: Dynamic data pruning, which also known as data importance sampling, has been proposed to improve training efficiency. For the case of sampling with replacement, the optimal sampling distribution to minimize the variance is to sample proportional to the gradient norm, which can be approximated by the gradient norm of the logits from an extra forward pass. However, this could result in repeated samples, which can be an undesirable property. Noticing that most dynamic data pruning methods that avoids repeated samples can be seen as weighted Bernoulli sampling, in this work we study the optimal distribution to reduce its variance. Furthermore, to avoid an extra forward pass, we study the use of historic statistics. We propose the use of exponential moving average and probability smoothing to improve the performance.

## item_id: r3_082

TITLE: S$^6$-DAMON: Bridging Self-Supervised Speech Models and Real-time Speech Recognition

ABSTRACT: There has been an growing demand for deep neural network (DNN) powered automatic speech recognition (ASR) on mobile platforms for real-time speech recognition. However, ubiquitous on-device ASR systems are still hindered by two bottlenecks: (1) the lack of large-scale transcribed speech data especially for low-resource spoken languages and (2) the large gap between DNNs' prohibitive complexity and mobiles' limited resources. In parallel, speech models pretrained via self-supervised learning (SSL) have emerged to reduce the reliance on the availability of transcribed speech data, which however further enlarges the efficiency gap because they often adopt large transformers to ensure expressive speech representations. Thus, it is highly desired to trim down the complexity of speech SSL models to enable real-time on-device ASR. This is particularly challenging since only structured sparsity can favor hardware efficiency in commercial devices, under which the speech representation learned by SSL could easily be demolished. To this end, we develop a framework dubbed S$^6$-DAMON to pursue structured sparsity in speech SSL models via data-model co-compression. On the data side, leveraging both the duration of each phoneme and the pauses between the words/phonemes of human utterances, we propose a salient audio token detector, dubbed SALAD, to remove input audio tokens that are redundant; On the model side, we identify that the failure of the SOTA ASR pruning method under structured sparsity is caused by the sparsity discrepancy between finetuning/deployment and their limited learnability of sparsity distributions, and then tackle it via a new ASR pruning pipeline dubbed SAFARI, which adopts a three-step pipeline - sparsify, finetune, and adjust sparsity. Extensive experiments validate that S$^6$-DAMON can enable real-time ASR with limited transcribed speech data requirements while maintaining decent recognition performance. All source codes will be released upon acceptance.

## item_id: r3_083

TITLE: MBMamba: When Memory Buffer Meets Mamba for Structure-Aware Image Deblurring

ABSTRACT: The Mamba architecture has emerged as a promising alternative to CNNs and Transformers for image deblurring. However, its flatten-and-scan strategy often results in local pixel forgetting and channel redundancy, limiting its ability to effectively aggregate 2D spatial information. Although existing methods mitigate this by modifying the scan strategy or incorporating local feature modules, it increase computational complexity and hinder real-time performance. In this paper, we propose a structure-aware image deblurring network  without changing the original Mamba architecture. Specifically, we design a memory buffer mechanism to preserve historical information for later fusion, enabling reliable modeling of relevance between adjacent features. Additionally, we introduce an Ising-inspired regularization loss that simulates the energy minimization of the physical system's "mutual attraction" between pixels, helping to maintain image structure and coherence. Building on this, we develop MBMamba. Experimental results show that our method outperforms state-of-the-art approaches.

## item_id: r3_084

TITLE: KnowData: Knowledge-Enabled Data Generation for Improving Multimodal Models

ABSTRACT: In this paper, we introduce a framework to enhance the quality of synthetic image-text pairs for multimodal models such as CLIP. Our approach, named KnowData, integrates real-world knowledge explicitly into the generation of text descriptions. It combines structured knowledge from knowledge graphs like ConceptNet and unstructured knowledge extracted from Wikipedia, to ensure that the generated text descriptions are both contextually rich and accurately reflective of real-world knowledge. Additionally, we leverage Large Language Models for the expansion, summarization, and refinement of the text descriptions to ensure their coherence. These enriched texts are subsequently used to generate images through advanced text-to-image models like Stable Diffusion and DALLE-3. CLIP models are then fine-tuned with these synthetic image-text pairs for zero-shot classification tasks. Our experiments across 9 datasets demonstrate that CLIP models fine-tuned with our knowledge-guided synthetic datasets outperform state-of-the-art (SOTA) zero-shot CLIP methods (e.g., +11.23% on DTD and +4% on EuroSAT based on ViT-B/16 model; +11.47% on CIFAR-100 and +7.99% on DTD based on ResNet-50 model). These results showcase the improved out-of-distribution robustness and adaptability of our approach across a diverse set of data domains. We further substantiate the design of KnowData through ablation studies, revealing that the integration of knowledge not only enhances zero-shot performance but also contributes to the reliability, diversity, and detail-orientation of the generated synthetic images, thereby offering better data scaling laws for model performance.

## item_id: r3_085

TITLE: NeuroFabric: Identifying Ideal Topologies for Training A Priori Sparse Networks

ABSTRACT: Long training times of deep neural networks are a bottleneck in machine learning research. The major impediment to fast training is the quadratic growth of both memory and compute requirements of dense and convolutional layers with respect to their information bandwidth. Recently, training `a priori' sparse networks has been proposed as a method for allowing layers to retain high information bandwidth, while keeping memory and compute low. However, the choice of which sparse topology should be used in these networks is unclear. In this work, we provide a theoretical foundation for the choice of intra-layer topology. First, we derive a new sparse neural network initialization scheme that allows us to explore the space of very deep sparse networks. Next, we evaluate several topologies and show that seemingly similar topologies can often have a large difference in attainable accuracy. To explain these differences, we develop a data-free heuristic that can evaluate a topology independently from the dataset the network will be trained on. We then derive a set of requirements that make a good topology, and arrive at a single topology that satisfies all of them. 

## item_id: r3_086

TITLE: STAIRS-Former: Spatio-Temporal Attention with Interleaved Recursive Structure TransFormer for Offline Mulit-task Multi-agent Reinforcement Learning

ABSTRACT: Offline multi-agent reinforcement learning (MARL) with multi-task datasets is challenging due to varying numbers of agents across tasks and the need to generalize to unseen scenarios. Prior works employ transformers with observation tokenization and hierarchical skill learning to address these issues. However, they underutilize the transformer attention mechanism for inter-agent coordination and rely on a single history token, which limits their ability to capture long-horizon temporal dependencies in partially observable MARL settings. In this paper, we propose STAIRS-Former, a transformer architecture augmented with spatial and temporal hierarchies that enables effective attention over critical tokens while capturing long interaction histories. We further introduce token dropout to enhance robustness and generalization across varying agent populations. Extensive experiments on diverse multi-agent benchmarks, including SMAC, SMAC-v2, MPE, and MaMuJoCo, with multi-task datasets demonstrate that STAIRS-Former consistently outperforms prior methods and achieves new state-of-the-art performance.

## item_id: r3_087

TITLE: What's in the Box? Exploring the Inner Life of Neural Networks with Robust Rules

ABSTRACT: We propose a novel method for exploring how neurons within a neural network interact. In particular, we consider activation values of a network for given data, and propose to mine noise-robust rules of the form $X \rightarrow Y$ , where $X$ and $Y$ are sets of neurons in different layers. To ensure we obtain a small and non-redundant set of high quality rules, we formalize the problem in terms of the Minimum Description Length principle, by which we identify the best set of rules as the one that best compresses the activation data. To discover good rule sets, we propose the unsupervised ExplaiNN algorithm. Extensive evaluation shows that our rules give clear insight in how networks perceive the world: they identify shared, resp. class-specific traits, compositionality within the network, as well as locality in convolutional layers. Our rules are easily interpretable, but also super-charge prototyping as they identify which groups of neurons to consider in unison.

## item_id: r3_088

TITLE: A Label is a Label is a Label: Relation Augmentation for Scene Graph Generation

ABSTRACT: The goal of scene graph generation (SGG) is to identify the relationships between objects in an image. Many recent methods have been proposed to address a critical challenge in SGG - the biased distribution of relations in the dataset and the semantic space. Although the unbiased SGG problem has recently gained popularity, current SGG research has not thoroughly examined different types of augmentation. Recent works have focused on augmenting objects instead of relations and ignored the opportunities for pixel-level augmentation. We propose a novel relation augmentation method to use semantic and visual perturbations to balance the relation distribution. We use relation dataset statistics to boost the distribution of rare relation classes. We also use visual MixUp and grafting techniques to increase the sample size of triplets with tail relation labels. Our proposed method, RelAug, effectively reduces the long-tail distribution of predicates. We demonstrate this method can be easily adapted to existing methods and produces state-of-the-art performance on the Visual Genome dataset. The authors will make the source code publicly available for reproduction.

## item_id: r3_089

TITLE: Learning Fair Representations with High-Confidence Guarantees

ABSTRACT: Representation learning is increasingly employed to generate representations that are predictive across multiple downstream tasks.
The development of representation learning algorithms that provide strong fairness guarantees is thus important because it can prevent unfairness towards disadvantaged groups for $all$ downstream prediction tasks.
In this paper, we formally define the problem of learning representations that are fair with high confidence.
We then introduce the $\textbf{F}$air $\textbf{R}$epresentation learning with high-confidence $\textbf{G}$uarantees (FRG) framework, which provides high-confidence guarantees for limiting unfairness across all downstream models and tasks, with user-defined upper bounds.
After proving that FRG ensures fairness for all downstream models and tasks with high probability, we present empirical evaluations that demonstrate FRG's effectiveness at upper bounding unfairness for multiple downstream models and tasks.

## item_id: r3_090

TITLE: Improve Novel Class Generalization By Adaptive Feature Distribution for Few-Shot Learning

ABSTRACT: In this work, we focus on improving the novel class generalization of few-shot learning. By addressing the difference between feature distributions of base and novel classes, we propose the adaptive feature distribution method which is to finetune one scale vector using the support set of novel classes. The scale vector is applied on the normalized feature distribution and by using one scale vector to reshape the feature space manifold, we obtain consistent performance improvement for both in-domain and cross-domain evaluations. By simply finetuning one scale vector using 5 images, we observe a $2.23\%$ performance boost on 5-way 1-shot cross-domain evaluation with CUB over statistics results of 2000 episodes. This approach is simple yet effective. By just finetuning a single scale vector we provide a solution of reducing number of parameters while still obtain generalization ability for few-shot learning. We achieve the state-of-the-art performance on mini-Imagenet, tiered-Imagenet as well as cross-domain evaluation on CUB.

## item_id: r3_091

TITLE: Fast Intent Classification for LLM Routing via Statistical Analysis of Representations

ABSTRACT: Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency.
In this work, we conduct a systematic study comparing training-free vs training-based approaches for intent classification. For this purpose, we introduce two lightweight, training-free methods based on statistical analysis of internal model representations and compare them against MLP classifiers and linear probes. The training-free methods use key statistical metrics from hidden features, enabling intent inference during the initial forward pass with minimal overhead. Our comprehensive empirical evaluation reveals that 1) both training-free and training-based methods saturate easy benchmarks (mathematics vs. coding vs. natural language), 2) Training-based classifiers have an advantage on harder classification tasks (e.g. Java vs Python), and 3) Training-free methods are more robust to out-of-distribution and ambiguous prompts.

## item_id: r3_092

TITLE: LASER: Linear Compression in Wireless Distributed Optimization

ABSTRACT: Data-parallel SGD is the de facto algorithm for distributed optimization, especially for large scale machine learning. Despite its merits, communication bottleneck is one of its persistent issues. Most compression schemes to alleviate this either assume noiseless communication links, or fail to achieve good performance on practical tasks. In this paper, we close this gap and introduce ${\bf LASER}$: ${\bf L}$ine${\bf A}$r Compre${\bf S}$sion in Wir${\bf E}$less Dist${\bf R}$ibuted Optimization. LASER capitalizes on the inherent low-rank structure of gradients and transmits them efficiently over the noisy channels. Whilst enjoying theoretical guarantees similar to that of the classical SGD, LASER shows consistent gains over baselines on a variety of practical benchmarks. In particular, it outperforms the state-of-the-art compression schemes on challenging computer vision and GPT language modeling tasks. On the latter, we obtain $50$-$64$ % improvement in perplexity over our baselines for noisy channels.

## item_id: r3_093

TITLE: Variation-Bounded Losses for Learning with Noisy Labels

ABSTRACT: The presence of noisy labels poses a significant challenge for training accurate deep neural networks.
Previous works have proposed various robust loss functions designed to address this issue, which, however, often suffer from several drawbacks, such as  underfitting or insufficient noise-tolerance. Furthermore, there is currently no reliable metric to guide the design of more effective robust loss functions.
In this paper, we introduce the *Variation Ratio* as a novel metric to measure the robustness of loss functions.  Leveraging this metric, we propose a new family of robust loss functions, termed *Variation-Bounded Losses* (VBL), characterized by a bounded variation ratio.
We investigate theoretical properties of variation-bounded losses and prove that a smaller variation ratio would lead to better robustness. Additionally, we show that the variation ratio provides a more relaxed condition than the commonly used symmetric condition for achieving noise-tolerant learning, making it a valuable tool for designing effective robust loss functions.
We modify several commonly used loss functions to the variation-bounded form.
These variation-bounded losses are characterized by their simplicity, effectiveness, and theoretical guarantees.
Extensive experiments demonstrate the superiority of our method in mitigating various types of label noise.

## item_id: r3_094

TITLE: Flow Matching with Gaussian Process Priors for Probabilistic Time Series Forecasting

ABSTRACT: Recent advancements in generative modeling, particularly diffusion models, have opened new directions for time series modeling, achieving state-of-the-art performance in forecasting and synthesis. However, the reliance of diffusion-based models on a simple, fixed prior complicates the generative process since the data and prior distributions differ significantly. We introduce TSFlow, a conditional flow matching (CFM) model for time series combining Gaussian processes, optimal transport paths, and data-dependent prior distributions. By incorporating (conditional) Gaussian processes, TSFlow aligns the prior distribution more closely with the temporal structure of the data, enhancing both unconditional and conditional generation. Furthermore, we propose conditional prior sampling to enable probabilistic forecasting with an unconditionally trained model. In our experimental evaluation on eight real-world datasets, we demonstrate the generative capabilities of TSFlow, producing high-quality unconditional samples. Finally, we show that both conditionally and unconditionally trained models achieve competitive results across multiple forecasting benchmarks.

## item_id: r3_095

TITLE: Not All Samples Are Equal: Quantifying Instance-level Difficulty in Targeted Data Poisoning

ABSTRACT: Targeted data poisoning attacks pose an increasingly serious threat due to their ease of deployment and high success rates. These attacks aim to manipulate the prediction for a single test sample in classification models. Unlike indiscriminate attacks that aim to decrease overall test performance, targeted attacks present a unique threat to individual test instances. This threat model raises a fundamental question: what factors make certain test samples more susceptible to successful poisoning than others? We investigate how attack difficulty varies across different test instances and identify key characteristics that influence vulnerability. This paper introduces three predictive criteria for targeted data poisoning difficulty: ergodic prediction accuracy  (analyzed through clean training dynamics), poison distance, and poison budget. Our experimental results demonstrate that these metrics effectively predict the varying difficulty of real-world targeted poisoning attacks across diverse scenarios, offering practitioners valuable insights for vulnerability assessment and understanding data poisoning attacks.

## item_id: r3_096

TITLE: RF-POLICY: Rectified Flows are Adaptive Decision Makers

ABSTRACT: Diffusion-based imitation learning improves Behavioral Cloning (BC) on multi-modal decision-making but comes at the cost of significantly slower inference due to the recursion in the diffusion process. However, in real-world scenarios, states that require multi-modal decision-making are rare, and the huge consumption of diffusion models is not necessary for most cases. It inspires us to design efficient policy generators that can wisely allocate computation for different contexts. To address this challenge, we propose RF-POLICY (Rectified Flow-Policy), an imitation learning algorithm based on Rectified Flow, a recent advancement in flow-based generative modeling~\citep{liu2022flow}. RF-POLICY adopts probability flow ordinary differential equations (ODEs) for diverse policy generation, with the learning principle of following straight trajectories as much as possible. We uncover and leverage a surprisingly intriguing advantage of these flow-based models over previous diffusion models: their training objective indicates the uncertainty of a certain state, and
when the state is uni-modal, they automatically reduce to one-step generators since the probability flows admit straight lines.
Therefore, RF-POLICY is naturally an adaptive decision maker, offering rapid inference without sacrificing diversity. Our comprehensive empirical evaluation shows that \ours{}, to the best of our knowledge, is the first algorithm to achieve high performance across all dimensions, including success rate, behavioral diversity, and inference speed.

## item_id: r3_097

TITLE: Diffusion-based dynamics as a cognitive model of human speech production

ABSTRACT: Human language production requires transforming abstract communicative intent into fluent speech, yet the algorithmic nature of this transformation remains less understood. Most studies aligning large language models (LLMs) with brain activity have focused on autoregressive LLMs (aLLMs), which generate text left-to-right by committing to the next token. While effective at predicting neural and behavioral signatures of comprehension, this paradigm assumes incremental generation. In contrast, diffusion LLMs (dLLMs) construct sentences by iteratively denoising global representations. Despite their distinct generative dynamics, dLLMs now rival aLLMs on standard NLP benchmarks, prompting the question of whether the brain likewise engages in global, iterative refinement—especially during pre-articulatory planning when sentence structure remains flexible. To test this hypothesis, we correlated intermediate denoising steps of a dLLM with electrocorticography (ECoG) activity during naturalistic speech production. dLLM representations explained significant neural variance from pre- to post-production, with especially strong encoding in middle/inferior temporal and motor-related regions. These results support iterative refinement as a plausible neural mechanism of human speech planning.

## item_id: r3_098

TITLE: Towards Understanding Factual Knowledge of Large Language Models

ABSTRACT: Large language models (LLMs) have recently driven striking performance improvements across a range of natural language processing tasks. The factual knowledge acquired during pretraining and instruction tuning can be useful in various downstream tasks, such as question answering, and language generation. Unlike conventional Knowledge Bases (KBs) that explicitly store factual knowledge, LLMs implicitly store facts in their parameters. Content generated by the LLMs can often exhibit inaccuracies or deviations from the truth, due to facts that can be incorrectly induced or become obsolete over time. To this end, we aim to explore the extent and scope of factual knowledge within LLMs by designing the benchmark Pinocchio. Pinocchio contains 20K diverse factual questions that span different sources, timelines, domains, regions, and languages. Furthermore, we investigate whether LLMs can compose multiple facts, update factual knowledge temporally, reason over multiple pieces of facts, identify subtle factual differences, and resist adversarial examples. Extensive experiments on different sizes and types of LLMs show that existing LLMs still lack factual knowledge and suffer from various spurious correlations. We believe this is a critical bottleneck for realizing trustworthy artificial intelligence. The dataset Pinocchio and our codes are publicly available at: https://github.com/THU-BPM/Pinocchio.

## item_id: r3_099

TITLE: Deep learning mutation prediction enables early stage lung cancer detection in liquid biopsy

ABSTRACT: Somatic cancer mutation detection at ultra-low variant allele frequencies (VAFs) is an unmet challenge that is intractable with current state-of-the-art mutation calling methods. Specifically, the limit of VAF detection is closely related to the depth of coverage, due to the requirement of multiple supporting reads in extant methods, precluding the detection of mutations at VAFs that are orders of magnitude lower than the depth of coverage. Nevertheless, the ability to detect cancer-associated mutations in ultra low VAFs is a fundamental requirement for low-tumor burden cancer diagnostics applications such as early detection, monitoring, and therapy nomination using liquid biopsy methods (cell-free DNA). Here we defined a spatial representation of sequencing information adapted for convolutional architecture that enables variant detection at VAFs, in a manner independent of the depth of sequencing. This method enables the detection of cancer mutations even in VAFs as low as 10x-4^, >2 orders of magnitude below the current state-of-the-art. We validated our method on both simulated plasma and on clinical cfDNA plasma samples from cancer patients and non-cancer controls. This method introduces a new domain within bioinformatics and personalized medicine – somatic whole genome mutation calling for liquid biopsy.
