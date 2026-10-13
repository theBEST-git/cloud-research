# Batch 02 — 25 items

## item_id: g_026

TITLE: wav2tok: Deep Sequence Tokenizer for Audio Retrieval

ABSTRACT: Search over audio sequences is a fundamental problem. In this paper, we propose a method to extract concise discrete representations for audio that can be used for efficient retrieval. Our motivation comes from orthography which represents speech of a given language in a concise and distinct discrete form. The proposed method, wav2tok, learns such representations for any kind of audio, speech or non-speech, from pairs of similar audio. wav2tok compresses the query and target sequences into shorter sequences of tokens that are faster to match. The learning method makes use of CTC loss and expectation-maximization algorithm, which are generally used for supervised automatic speech recognition and for learning discrete latent variables, respectively. Experiments show the consistent performance of wav2tok across two audio retrieval tasks: music search (query by humming) and speech search via audio query, outperforming state-of-the-art baselines.

## item_id: g_027

TITLE: Are adversarial examples inevitable?

ABSTRACT: A wide range of defenses have been proposed to harden neural networks against adversarial attacks. However, a pattern has emerged in which the majority of adversarial defenses are quickly broken by new attacks.  Given the lack of success at generating robust defenses, we are led to ask a fundamental question:  Are adversarial attacks inevitable?
This paper analyzes adversarial examples from a theoretical perspective, and identifies fundamental bounds on the susceptibility of a classifier to adversarial attacks.   We show that, for certain classes of problems, adversarial examples are inescapable.  Using experiments, we explore the implications of theoretical guarantees for real-world problems and discuss how factors such as dimensionality and image complexity limit a classifier's robustness against adversarial examples.



## item_id: g_028

TITLE: LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer

ABSTRACT: Graphic layout designs play an essential role in visual communication. Yet handcrafting layout designs is skill-demanding, time-consuming, and non-scalable to batch production. Generative models emerge to make design automation scalable but it remains non-trivial to produce designs that comply with designers' multimodal desires, i.e., constrained by background images and driven by foreground content. We propose LayoutDETR that inherits the high quality and realism from generative modeling, while reformulating content-aware requirements as a detection problem: we learn to detect in a background image the reasonable locations, scales, and spatial relations for multimodal foreground elements in a layout. Our solution sets a new state-of-the-art performance for layout generation on public benchmarks and on our newly-curated ad banner dataset. We integrate our solution into a graphical system that facilitates user studies, and show that users prefer our designs over baselines by significant margins.

## item_id: g_029

TITLE: Vision Transformers Need Registers

ABSTRACT: Transformers have recently emerged as a powerful tool for learning visual representations. In this paper, we identify and characterize artifacts in feature maps of both supervised and self-supervised ViT networks. The artifacts correspond to high-norm tokens appearing during inference primarily in low-informative background areas of images, that are repurposed for internal computations. We propose a simple yet effective solution based on providing additional tokens to the input sequence of the Vision Transformer to fill that role. We show that this solution fixes that problem entirely for both supervised and self-supervised models, sets a new state of the art for self-supervised visual models on dense visual prediction tasks, enables object discovery methods with larger models, and most importantly leads to smoother feature maps and attention maps for downstream visual processing.

## item_id: g_030

TITLE: Weakly Supervised Disentanglement with Guarantees

ABSTRACT: Learning disentangled representations that correspond to factors of variation in real-world data is critical to interpretable and human-controllable machine learning. Recently, concerns about the viability of learning disentangled representations in a purely unsupervised manner has spurred a shift toward the incorporation of weak supervision. However, there is currently no formalism that identifies when and how weak supervision will guarantee disentanglement. To address this issue, we provide a theoretical framework to assist in analyzing the disentanglement guarantees (or lack thereof) conferred by weak supervision when coupled with learning algorithms based on distribution matching. We empirically verify the guarantees and limitations of several weak supervision methods (restricted labeling, match-pairing, and rank-pairing), demonstrating the predictive power and usefulness of our theoretical framework.

## item_id: g_031

TITLE: BRAC+: Going Deeper with Behavior Regularized Offline Reinforcement Learning

ABSTRACT: Online interactions with the environment to collect data samples for training a Reinforcement Learning agent is not always feasible due to economic and safety concerns. The goal of Offline Reinforcement Learning (RL) is to address this problem by learning effective policies using previously collected datasets. Standard off-policy RL algorithms are prone to overestimations of the values of out-of-distribution (less explored) actions and are hence unsuitable for Offline RL. Behavior regularization, which constraints the learned policy within the support set of the dataset, has been proposed to tackle the limitations of standard off-policy algorithms. In this paper, we improve the behavior regularized offline reinforcement learning and propose \emph{BRAC+}. We use an analytical upper bound on KL divergence as the behavior regularizor to reduce variance associated with sample based estimations. Additionally, we employ state-dependent Lagrange multipliers for the regularization term to avoid distributing KL divergence penalty across all states of the sampled batch. The proposed Lagrange multipliers allow more freedom of deviation to high probability (more explored) states leading to better rewards while simultaneously restricting low probability (less explored) states to prevent out-of-distribution actions. \textcolor{blue}{To prevent catastrophic performance degradation due to rare out-of-distribution actions, we add a gradient penalty term to the policy evaluation objective to penalize the gradient of the Q value w.r.t the out-of-distribution actions. By doing so, the Q values evaluated at the out-of-distribution actions are bounded.} On challenging offline RL benchmarks, BRAC+ outperforms the state-of-the-art model-free and model-based approaches.

## item_id: g_032

TITLE: Network Pruning That Matters:  A Case Study on Retraining Variants

ABSTRACT: Network pruning is an effective method to reduce the computational expense of over-parameterized neural networks for deployment on low-resource systems. Recent state-of-the-art techniques for retraining pruned networks such as weight rewinding and learning rate rewinding have been shown to outperform the traditional fine-tuning technique in recovering the lost accuracy (Renda et al., 2020), but so far it is unclear what accounts for such performance. In this work, we conduct extensive experiments to verify and analyze the uncanny effectiveness of learning rate rewinding. We find that the reason behind the success of learning rate rewinding is the usage of a large learning rate. Similar phenomenon can be observed in other learning rate schedules that involve large learning rates, e.g., the 1-cycle learning rate schedule (Smith et al., 2019). By leveraging the right learning rate schedule in retraining, we demonstrate a counter-intuitive phenomenon in that randomly pruned networks could even achieve better performance than methodically pruned networks (fine-tuned with the conventional approach). Our results emphasize the cruciality of the learning rate schedule in pruned network retraining - a detail often overlooked by practitioners during the implementation of network pruning. 

## item_id: g_033

TITLE: S2VG: Soft Stochastic Value Gradient method

ABSTRACT: Model-based reinforcement learning (MBRL) has shown its advantages in sample-efficiency over model-free reinforcement learning (MFRL). Despite the impressive results it achieves, it still faces a trade-off between the ease of data generation and model bias. In this paper, we propose a simple and elegant model-based reinforcement learning algorithm called soft stochastic value gradient method (S2VG). S2VG combines the merits of the maximum-entropy reinforcement learning and MBRL, and exploits both real and imaginary data. In particular, we embed the model in the policy training and learn $Q$ and $V$ functions from the real (or imaginary) data set. Such embedding enables us to compute an analytic policy gradient through the back-propagation rather than the likelihood-ratio estimation, which can reduce the variance of the gradient estimation. We name our algorithm Soft Stochastic Value Gradient method to indicate its connection with the well-known stochastic value gradient method in \citep{heess2015Learning}.

## item_id: g_034

TITLE: Point-and-Click: A Procedural Benchmark for 2D Adventure Puzzle Solving

ABSTRACT: Point-and-click adventure games offer an ideal platform for testing multimodal large language model agents on long-horizon reasoning, commonsense knowledge, and language-perception grounding. Such games demand creative, compositional reasoning and the deduction of implicit goals. However, existing benchmarks provide limited support for compositional and generative puzzles, and often suffer from data contamination. To bridge this gap, we present Point-and-Click, a benchmark for 2D adventure games that procedurally generates rich puzzles and provides ground-truth solutions for evaluation. The environment instantiates controllable directed acyclic graphs of puzzle dependencies over primitives like keys/locks, codes, and pattern matching, spanning an exponentially scaling number of layouts with tunable difficulty. Experiments reveal the limitations of current multimodal LLM/VLM agents on this benchmark. We hope Point-and-Click serves as a rigorous testbed for progress on general-purpose embodied reasoning and implicit goal deduction in interactive environments.

## item_id: g_035

TITLE: SGD on Neural Networks learns Robust Features before Non-Robust

ABSTRACT: Neural networks are known to be vulnerable to adversarial attacks - small, imperceptible perturbations that cause the network to misclassify an input. A recent line of work attempts to explain this behavior by positing the existence of non-robust features - well-generalizing but brittle features present in the data distribution that are learned by the network and can be perturbed to cause misclassification.

In this paper, we look at the dynamics of neural network training through the perspective of robust and non-robust features. We find that there are two very distinct pathways that neural network training can follow, depending on the hyperparameters used. In the first pathway, the network initially learns only predictive, robust features and weakly predictive non-robust features, and subsequently learns predictive, non-robust features. On the other hand, a network trained via the second pathway eschews predictive non-robust features altogether, and rapidly overfits the training data. We provide strong empirical evidence to corroborate this hypothesis, as well as theoretical analysis in a simplified setting. Key to our analysis is a better understanding of the relationship between predictive non-robust features and adversarial transferability. We present our findings in light of other recent results on the evolution of inductive biases learned by neural networks over the course of training.

Finally, we digress to show that rather than being quirks of the data distribution, predictive non-robust features might actually occur across datasets with different distributions drawn from independent sources, indicating that they perhaps possess some meaning in terms of human semantics.

## item_id: g_036

TITLE: SaProt: Protein Language Modeling with Structure-aware Vocabulary

ABSTRACT: Large-scale protein language models (PLMs), such as the ESM family, have achieved remarkable performance in various downstream tasks related to protein structure and function by undergoing unsupervised training on residue sequences. They have become essential tools for researchers and practitioners in biology.  However, a limitation of vanilla PLMs is their lack of explicit consideration for protein structure information, which suggests the potential for further improvement. Motivated by this, we introduce the concept of a ``structure-aware vocabulary" that  integrates residue tokens with structure tokens.    The structure tokens are  derived  by encoding the 3D structure of proteins using Foldseek. We then propose SaProt, a large-scale general-purpose PLM trained on an extensive dataset comprising approximately 40 million protein sequences and structures. Through extensive evaluation, our SaProt model surpasses well-established and renowned baselines across 10 significant downstream tasks, demonstrating its exceptional capacity and broad applicability. We have made the code, pre-trained model, and all relevant materials available at https://github.com/westlake-repl/SaProt.

## item_id: g_037

TITLE: Incorporating BERT into Neural Machine Translation

ABSTRACT: The recently proposed BERT (Devlin et al., 2019) has shown great power on a variety of natural language understanding tasks, such as text classification, reading comprehension, etc. However, how to effectively apply BERT to neural machine translation (NMT) lacks enough exploration. While BERT is more commonly used as fine-tuning instead of contextual embedding for downstream language understanding tasks, in NMT, our preliminary exploration of using BERT as contextual embedding is better than using for fine-tuning. This motivates us to think how to better leverage BERT for NMT along this direction. We propose a new algorithm named BERT-fused model, in which we first use BERT to extract representations for an input sequence, and then the representations are fused with each layer of the encoder and decoder of the NMT model through attention mechanisms. We conduct experiments on supervised (including sentence-level and document-level translations), semi-supervised and unsupervised machine translation, and achieve state-of-the-art results on seven benchmark datasets. Our code is available at https://github.com/bert-nmt/bert-nmt

## item_id: g_038

TITLE: Identifying the Limits of Cross-Domain Knowledge Transfer for Pretrained Models

ABSTRACT: There is growing evidence that pretrained language models improve task-specific fine-tuning even where the task examples are radically different from those seen in training. What is the nature of this surprising cross-domain transfer? We offer a partial answer via a systematic exploration of how much transfer occurs when models are denied any information about word identity via random scrambling. In four classification tasks and two sequence labeling tasks, we evaluate LSTMs using GloVe embeddings, BERT, and baseline models. Among these models, we find that only BERT shows high rates of transfer into our scrambled domains, and for classification but not sequence labeling tasks. Our analyses seek to explain why transfer succeeds for some tasks but not others, to isolate the separate contributions of pretraining versus fine-tuning, to show that the fine-tuning process is not merely learning to unscramble the scrambled inputs, and to quantify the role of word frequency. These findings help explain where and why cross-domain transfer occurs, which can guide future studies and practical fine-tuning efforts.

## item_id: g_039

TITLE: Stochastic Latent Actor-Critic: Deep Reinforcement Learning with a Latent Variable Model

ABSTRACT: Deep reinforcement learning (RL) algorithms can use high-capacity deep networks to learn directly from image observations. However, these kinds of observation spaces present a number of  challenges in practice, since the policy must now solve two problems: a representation learning problem, and a task learning problem. In this paper, we aim to explicitly learn representations that can accelerate reinforcement learning from images. We propose the stochastic latent actor-critic (SLAC) algorithm: a sample-efficient and high-performing RL algorithm for learning policies for complex continuous control tasks directly from high-dimensional image inputs. SLAC learns a compact latent representation space using a stochastic sequential latent variable model, and then learns a critic model within this latent space. By learning a critic within a compact state space, SLAC can learn much more efficiently than standard RL methods. The proposed model improves performance substantially over alternative representations as well, such as variational autoencoders. In fact, our experimental evaluation demonstrates that the sample efficiency of our resulting method is comparable to that of model-based RL methods that directly use a similar type of model for control. Furthermore, our method outperforms both model-free and model-based alternatives in terms of final performance and sample efficiency, on a range of difficult image-based control tasks. Our code and videos of our results are available at our website.

## item_id: g_040

TITLE: Markovian Compression: Looking to the Past Helps Accelerate the Future

ABSTRACT: This paper deals with distributed optimization problems that use compressed communication to achieve efficient performance and mitigate the communication bottleneck. We propose a family of compression schemes in which operators transform vectors fed to their input according to a Markov chain, i.e., the stochasticity of the compressors depends on previous iterations. Intuitively, this should accelerate the convergence of optimization methods, as considering previous iterations seems more natural and robust. The compressors are implemented in the vanilla Quantized Stochastic Gradient Descent (QSGD) algorithm. To further improve efficiency and convergence rate, we apply the momentum acceleration method. We prove convergence results for our algorithms with Markovian compressors and show theoretically that the accelerated method converges faster than the basic version. The analysis covers non-convex, Polyak-Lojasiewicz (PL), and strongly convex cases. Experiments are conducted to demonstrate the applicability of the results to distributed data-parallel optimization problems. Practical results demonstrate the superiority of methods utilizing our compressors design over several existing optimization algorithms.

## item_id: g_041

TITLE: Weights Having Stable Signs Are Important: Finding Primary Subnetworks and Kernels to Compress Binary Weight Networks

ABSTRACT: Binary Weight Networks (BWNs) have significantly lower computational and memory costs compared to their full-precision counterparts. To address the non-differentiable issue of BWNs, existing methods usually use the Straight-Through-Estimator (STE). In the optimization, they learn optimal binary weight outputs represented as a combination of scaling factors and weight signs to approximate 32-bit floating-point weight values, usually with a layer-wise quantization scheme. In this paper, we begin with an empirical study of training BWNs with STE under the settings of using common techniques and tricks. We show that in the context of using batch normalization after convolutional layers, adapting scaling factors with either hand-crafted or learnable methods brings marginal or no accuracy gain to final model, while the change of weight signs is crucial in the training of BWNs. Furthermore, we observe two astonishing training phenomena. Firstly, the training of BWNs demonstrates the process of seeking primary binary sub-networks whose weight signs are determined and fixed at the early training stage, which is akin to recent findings on the lottery ticket hypothesis for efficient learning of sparse neural networks. Secondly, we find binary kernels in the convolutional layers of final models tend to be centered on a limited number of the most frequent binary kernels, showing binary weight networks may has the potential to be further compressed, which breaks the common wisdom that representing each weight with a single bit puts the quantization to the extreme compression. To testify this hypothesis, we additionally propose a binary kernel quantization method, and we call resulting models Quantized Binary-Kernel Networks (QBNs). We hope these new experimental observations would shed new design insights to improve the training and broaden the usages of BWNs.

## item_id: g_042

TITLE: Make SVM great again with Siamese kernel for  few-shot learning

ABSTRACT: While deep neural networks have shown outstanding results in a wide range of applications,
learning from a very limited number of examples is still a challenging
task. Despite the difficulties of the few-shot learning, metric-learning techniques
showed the potential of the neural networks for this task. While these methods
perform well, they don’t provide satisfactory results. In this work, the idea of
metric-learning is extended with Support Vector Machines (SVM) working mechanism,
which is well known for generalization capabilities on a small dataset.
Furthermore, this paper presents an end-to-end learning framework for training
adaptive kernel SVMs, which eliminates the problem of choosing a correct kernel
and good features for SVMs. Next, the one-shot learning problem is redefined
for audio signals. Then the model was tested on vision task (using Omniglot
dataset) and speech task (using TIMIT dataset) as well. Actually, the algorithm
using Omniglot dataset improved accuracy from 98.1% to 98.5% on the one-shot
classification task and from 98.9% to 99.3% on the few-shot classification task.

## item_id: g_043

TITLE: Measuring Model Robustness via Fisher Information: Spectral Bounds, Theoretical Guarantees, and Practical Algorithms

ABSTRACT: The robustness of deep neural networks is critical for their deployment in safety-sensitive domains. This paper establishes a novel theoretical framework for quantifying model robustness through the lens of Fisher information. We first start with the known conclusion that maximizing the KL divergence of the posterior probability is equivalent to minimizing half the Mahalanobis distance defined by the Fisher Information Matrix (FIM), and further reveal that the FIM is equal to the variance of the input Jacobian matrix. Based on this insight, we propose the FIM's principal eigenvalue (or its reciprocal) as a principled robustness metric. We derive closed-form spectral bounds for common architectural components (e.g., ReLU, convolution) and theoretically compare the robustness of VGG, ResNet, DenseNet, and Transformer. To enable scalable computation, we resort to efficient algorithms, including power iteration and randomized Hutchinson, to estimate the robustness metric. Furthermore, we propose to use Hutchinson and finite differences to achieve robust estimation in a black-box setting. Extensive experiments validate our theoretical claims and demonstrate the metric's utility in predicting adversarial vulnerability. Code: https://anonymous.4open.science/r/8F4D7E6R/

## item_id: g_044

TITLE: Round and Round We Go! What makes Rotary Positional Encodings useful?

ABSTRACT: Positional Encodings (PEs) are a critical component of Transformer-based Large Language Models (LLMs), providing the attention mechanism with important sequence-position information. One of the most popular types of encoding used today in LLMs are Rotary Positional Encodings (RoPE), that rotate the queries and keys based on their relative distance. A common belief is that RoPE is useful because it helps to decay token dependency as relative distance increases. In this work, we argue that this is unlikely to be the core reason. We study the internals of a trained Gemma 7B model to understand how RoPE is being used at a mechanical level. We find that Gemma learns to use RoPE to construct robust `positional' attention patterns by exploiting the highest frequencies. We also find that, in general, Gemma greatly prefers to use the lowest frequencies of RoPE, which we suspect are used to carry semantic information. We mathematically prove interesting behaviours of RoPE and conduct experiments to verify our findings, proposing a modification of RoPE that fixes some highlighted issues and improves performance. We believe that this work represents an interesting step in better understanding PEs in LLMs, which we believe holds crucial value for scaling LLMs to large sizes and context lengths.

## item_id: g_045

TITLE: UNITER: Learning UNiversal Image-TExt Representations

ABSTRACT: Joint image-text embedding is the bedrock for most Vision-and-Language (V+L) tasks, where multimodality inputs are jointly processed for visual and textual understanding. In this paper, we introduce UNITER, a UNiversal Image-TExt Representation, learned through large-scale pre-training over four image-text datasets (COCO, Visual Genome, Conceptual Captions, and SBU Captions), which can power heterogeneous downstream V+L tasks with joint multimodal embeddings. We design three pre-training tasks: Masked Language Modeling (MLM), Image-Text Matching (ITM), and Masked Region Modeling (MRM, with three variants). Different from concurrent work on multimodal pre-training that apply joint random masking to both modalities, we use Conditioned Masking on pre-training tasks (i.e., masked language/region modeling is conditioned on full observation of image/text). Comprehensive analysis shows that conditioned masking yields better performance than unconditioned masking. We also conduct a thorough ablation study to find an optimal combination of pre-training tasks for UNITER. Extensive experiments show that UNITER achieves new state of the art across six V+L tasks over nine datasets, including Visual Question Answering, Image-Text Retrieval, Referring Expression Comprehension, Visual Commonsense Reasoning, Visual Entailment, and NLVR2. 

## item_id: g_046

TITLE: Learning to Defer on Anonymously Annotated Data

ABSTRACT: Recent advancements in machine learning have prompted the development in human-machine cooperation to leverage the efficiency of machines and the reliability of human expertise. One such approach is *learning to defer* (L2D), where a model learns to selectively defer decision-making to humans based on their historical performance on labelled data. Traditional L2D methods require the same set of human experts in both training and deployment phase, so that the system can leverage their historical performance to allocate queries accordingly. This human-specific nature, however, renders inflexibility in dynamic real-world environments where expert availability can fluctuate due to leave, retirement, or the integration of new team members. To address this challenge, we propose leveraging anonymously-annotated datasets, which are commonly available in practice, to infer annotation patterns and cluster human annotators based on behavioural similarities. Building upon the clustering of human experts, we develop a variant L2D, known as L2D-Clusters, that defers queries to a cluster rather than a specific expert, with one expert from the cluster randomly selected to make the final decision. Empirical results show that our clustering aligns with known annotator behaviour and that L2D-Clusters performs comparably to expert-specific L2D, especially in onboarding scenarios with limited annotator-identified data.

## item_id: g_047

TITLE: Reasoning with Sampling: Your Base Model is Smarter Than You Think

ABSTRACT: Frontier reasoning models have exhibited incredible capabilities across a wide array of disciplines, driven by posttraining large language models (LLMs) with reinforcement learning (RL). However, despite the widespread success of this paradigm, much of the literature has been devoted to disentangling truly novel behaviors that emerge during RL but are not present in the base models. In our work, we approach this question from a different angle, instead asking whether comparable reasoning capabilities can be elicited from base models at inference time by pure sampling, without any additional training. Inspired by Markov chain Monte Carlo (MCMC) techniques for sampling from sharpened distributions, we propose a simple iterative sampling algorithm leveraging the base models' own likelihoods. Over different base models, we show that our algorithm offers substantial boosts in reasoning that nearly match and even outperform those from RL on a wide variety of single-shot tasks, including MATH500, HumanEval, and GPQA. Moreover, our sampler avoids the collapse in diversity over multiple samples that is characteristic of RL-posttraining. Crucially, our method does not require training, curated datasets, or a verifier, suggesting broad applicability beyond easily verifiable domains.

## item_id: g_048

TITLE: Personal Tokens Matter: Towards Token-Aware Training for Personalized LLMs

ABSTRACT: With large language models (LLMs) now performing strongly across diverse tasks, there is growing demand for them to personalize outputs for individual users. Personalization is typically framed as an additional layer on top of a base NLP task, requiring models to meet user-specific needs while still completing the underlying task. This overlay nature means that many tokens in a response serve the base task, while only a subset encode user-specific information. We term these personal tokens, as they are essential for rendering responses personalized. However, their varying positions and contents across tasks make them difficult to detect directly.
To address this challenge, we propose PerContrast, a causal intervention–based method that identifies personal tokens by measuring each output token’s dependence on user-specific information, achieving up to 87.8\% F1 score on our benchmark. Building on this insight, we develop the PerCE loss, which adaptively upweights personal tokens during training via an expectation–maximization procedure, enabling the model to alternately identify and optimize these tokens.
Experiments on multiple LLMs show that PerCE substantially improves personalization performance with minimal additional cost, yielding average gains over 10\% and up to 40.57\% on the LongLaMP dataset, along with strong cross-task and cross-scenario transferability. These results highlight the central role of personal tokens and establish token-aware training as a simple yet effective paradigm for advancing personalized LLMs.

## item_id: g_049

TITLE: Bandwith Enables Generalization in Quantum Kernel Models

ABSTRACT: Quantum computers are known to provide speedups over classical state-of-the-art machine learning methods in some specialized settings. For example, quantum kernel methods have been shown to provide an exponential speedup on a learning version of the discrete logarithm problem. Understanding the generalization of quantum models is essential to realizing similar speedups on practically interesting problems. Recent results demonstrate that generalization is hindered by the exponential size of the quantum feature space. Although these results suggest that quantum models cannot generalize when the number of qubits is large, in this paper we show that these results rely on overly restrictive assumptions. We consider a wider class of models by varying a hyperparameter that we call quantum kernel bandwidth. We analyze the large-qubit limit and provide explicit formulas for the generalization of a quantum model that can be solved in closed form. Specifically, we show that changing the value of bandwidth can take a model from provably not being able to generalize on any target function to good generalization for well-aligned targets. Our analysis shows how the bandwidth controls the spectrum of the kernel integral operator, and thereby the inductive bias of the model. We demonstrate empirically that our theory correctly predicts how varying the bandwidth affects generalization of quantum models on challenging datasets, including those far outside our theoretical assumptions. We discuss the implications of our results for quantum advantage in machine learning.

## item_id: g_050

TITLE: Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance

ABSTRACT: Large Language Model's are instruction-finetuned to enhance their ability to follow user instructions and better comprehend input context. Still, they often struggle to follow the input context, especially when it contradicts model's parametric knowledge. This manifests as various failures, such as hallucinations where a model inserts outdated or unwarranted facts into its response. In this work, we observe an intriguing phenomenon: the context reliance of the model decreases as instruction finetuning progresses, $\textit{despite an initial expected increase}$. We call this phenomenon as the $\textbf{context-parametric inversion}$. This is surprising, as one would expect instruction tuning to improve the model's ability to follow input instructions.  We observe this behavior on multiple general purpose instruction tuning datasets such as TULU, Alpaca and Ultrachat, across multiple model families like Llama, Mistral and Pythia.  We perform various controlled studies to eliminate some simple hypothesis for this observed behavior and isolate what datapoints cause this counter-intuitive behavior. We then analyze the phenomenon theoretically, to explain why context reliance varies across the trajectory of finetuning. 
We tie the observed context-parametric inversion to the properties of the finetuning data, which provides us with some potential mitigation strategies that provide limited but insightful gains.
