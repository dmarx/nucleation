---
number: 286
status: Read
formerly:
- NOTE-tmpdauv3
paper: LIT-302
title: 'The Platonic Representation Hypothesis'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 2405.07987 v5 (25 Jul 2024, the
    ICML 2024 / PMLR 235 version), from the arXiv PDF, 27 pp. I read the
    abstract, §§1–6, the acknowledgements, the references, and Appendices A
    (the mutual-kNN metric and CKNNA), B (consistency across metrics, the
    Fig. 11 table and the Fig. 12 rank-correlation matrix), C (model lists
    and alignment protocol), D (the colour experiment), E (caption density)
    and F (the NCE and InfoNCE optima, Proposition F.1 with proof, Remark
    F.2). Nothing was skipped. Figs 2–4, 9, 10, 13 and 14 are plots. Their
    values survive only as axis ticks, so I give numbers only where the text
    states them, or where the figure prints them (the Fig. 12 matrix). I
    read the anthology's holding first, ANTH-LIT-458 and its reading
    (anthology NOTE-206). Disagreements are reported under ADR-013 and
    nothing in the anthology was edited. I also read THEORY-002, THEORY-004
    and THEORY-008 here to relate them.). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  A position paper with one argument and three measurements. Measured with
  mutual 10-nearest-neighbour overlap, vision models that solve more VTAB
  tasks agree more with each other (78 models). Language models with lower
  bits-per-byte agree more with DINOv2, CLIP and others on Wikipedia
  image–caption pairs, and this alignment tracks HellaSwag and GSM8K
  scores. The cross-modal score "only reaches 0.16" out of a maximum of 1
  (§6), and a CKA version "revealed a very weak trend" (App. A). The
  formal argument (§4.2, App. F) shows only this: in an idealised world of
  discrete events seen through bijective observations, the Bayes-optimal
  NCE critic is the pointwise-mutual-information kernel plus a constant,
  and that kernel is representable as an inner product under a sufficient
  smoothness condition (Prop. F.1). So every such modality shares one
  kernel, up to an additive constant.
---

# NOTE-286: The Platonic Representation Hypothesis

## Contribution

The paper puts a name and a single conjecture on a scattered literature: models trained on different data, architectures, objectives and modalities come to "measure distance between datapoints" alike (abstract). The conjecture is that this convergence has an endpoint, "a representation of the joint distribution over events in the world that generate the data we observe" (§1). The authors call it the platonic representation.

The paper adds three measurements of its own and one formal argument:

- vision–vision alignment against transfer competence (Fig. 2);
- language–vision alignment against language-modelling score and downstream scores (Figs 3, 4);
- a caption-density test (Fig. 9);
- a proof that, in an idealised discrete world with bijective observations, NCE-type contrastive learners in every modality have the same optimal kernel, the PMI kernel, up to a constant (§4.2, App. F).

## Key insight

The formal core is this. A contrastive learner's optimal dot-product kernel is the pointwise mutual information of co-occurrence. Bijective observations preserve probabilities over discrete events, and so preserve PMI. So any modality that sees the same events bijectively must learn the same kernel, K_PMI(x_a, x_b) + c_X = K_PMI(z_a, z_b) + c_X (eqs 6–8). Convergence, on this account, is kernel convergence, and it rests on shared information. That is why the paper's own limitation (§6) is the right one: where modalities carry different information, the argument gives nothing, and alignment should be capped by the mutual information between the signals.

## Assumptions

- **A representation is its kernel (§2).** f: X → Rⁿ is characterised by K(x_i, x_j) = ⟨f(x_i), f(x_j)⟩. Alignment is a similarity metric over kernels.
- **The idealised world (§4.1).**
  - Events: a sequence of T *discrete* events Z = [z_1, …, z_T] ~ P(Z).
  - Observations: each is "a bijective, deterministic function obs: Z → ·".
  - What counts as an event: footnote 4 allows "the joint distribution of observation indices" itself to be the platonic reality.
- **The learner (§4.2).** Positive pairs are drawn from P_coor, co-occurrence within a window T_window; negatives from the marginal. The critic is a dot product ⟨f_X(x_a), f_X(x_b)⟩.
- **Exact representability (Prop. F.1).** This is a sufficient condition. The off-diagonal PMI entries lie in [log ρ_min, log ρ_min + δ] ⊂ (−∞, 0], and P_coor(z_i | z_i)/P_coor(z_i) ≥ e^{Nδ} ρ_min for all i, where N is the number of events. Then K_PMI + C is diagonally dominant, hence PSD, hence an inner product. Remark F.2 calls this "somewhat strict".
- **Reaching the optimum.** "With sufficient data and optimization, we will observe convergence to this point" (§4.2). This is asserted, not shown.
- **The measurement setting (App. A, C).**
  - *Metric:* mutual k-NN with k = 10.
  - *Vision:* the vision–vision comparison uses 1,000 Places-365 validation images.
  - *Cross-modal data:* the cross-modal comparison uses 1,024 WIT image–caption pairs.
  - *Features:* ViT class tokens for vision, and average-pooled hidden states for language (the last token "did not show any strong alignment signal").
  - *Processing:* features are l2-normalised, activations above the 95th percentile are truncated, and the score is the maximum over all layer pairs, concatenations included.

## Key results

- **Vision–vision (Fig. 2, App. C.1).** The 78 models are 17 ViTs, 1 random ResNet-50, 11 contrastive ResNet-50s and 49 ResNet-18s on real and synthetic datasets. Those solving more of the 19 VTAB tasks have higher intra-bucket alignment. "Solves" means ≥ 80% of the best model's score. A UMAP of −log(alignment) clusters the competent models. The slogan offered: "all strong models are alike, each weak model is weak in its own way".
- **Language–vision (Fig. 3, App. C.2).** The language models are BLOOM, OpenLLaMA and LLaMA families, compared against DINOv2, MAE, ImageNet-21K, CLIP and CLIP fine-tuned on ImageNet-12K. Alignment rises roughly linearly with 1 − bits-per-byte. CLIP aligns most, and the ImageNet-fine-tuned CLIP aligns less. The converse is also stated: better vision models align more with LLMs.
- **Alignment and downstream performance (Fig. 4).** Alignment to DINOv2 correlates with HellaSwag ("linear") and with GSM8K ("emergence-esque"). No coefficient is given.
- **Metric robustness (App. B, Fig. 12).** For the 78 vision models, the printed Spearman rank correlation between mutual k-NN (k = 10, batch 1,000) and CKA is 0.73. It is 0.70 with unbiased CKA and 0.55 with SVCCA. For cross-modal alignment, sensitivity "depends on the metric" and on the vision model's training task (Figs 13–14).
- **Theory (§4.2, App. F.1).**
  - *Binary NCE.* The Bayes-optimal critic is g = log[P_coor(x_a, x_b)/(P(x_a)P(x_b))] + log[p_pos/(1 − p_pos)] = K_PMI + c_X (eqs 20–25).
  - *InfoNCE.* At τ = 1 the optimum is K_PMI + c_X(x_a); for τ ≠ 1 it holds "up to an offset and a scale" (eqs 26–30).
  - *The offset.* The symmetry of the dot-product critic forces c_X to be constant (eq. 6).
  - *Across modalities.* Bijective discrete observations preserve P_coor and hence K_PMI. The modalities' kernels therefore agree up to their separate constants c_X and c_Y (eqs 7–8).
- **Colour case study (§4.2, Fig. 8, App. D).** Multidimensional scaling of −K_PMI from CIFAR-10 pixel co-occurrences, and of distances among 20 colour words in SimCSE and RoBERTa-L, each aligned to CIELAB by Kabsch–Umeyama, "recovers roughly the same perceptual representation". This is by eye, on 20 colours, and the colour-word set differs from Abdou et al.'s 18.
- **Caption density (Fig. 9, App. E).** Alignment rises from 5-word to 30-word captions, averaged over all vision and language models, with standard deviation over the language models.
- **Implications (§5), argued rather than shown.**
  - *Data across modalities:* image data should help language models and conversely ("a pixel is worth a words").
  - *Translation:* translation and adaptation across modalities should be easy.
  - *Hallucination and bias:* scale may reduce hallucination and bias amplification, "conditioned on the training data … constituting a sufficiently lossless and diverse set of measurements".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Competent vision models are more mutually aligned than weak ones | moderate (experiment) | Fig. 2, 78 models, mutual-kNN on Places-365; error bars are standard errors |
| C2 | Language models with better LM scores align more with vision models on paired image–caption data | moderate (experiment), small effect | Fig. 3; scores reach ~0.16 of a maximum 1 (§6); max over layer pairs; CKA showed "a very weak trend" (App. A) |
| C3 | Alignment with vision predicts LLM downstream performance | weak–moderate | Fig. 4, scatter plots; no statistic reported |
| C4 | For binary NCE and InfoNCE (τ = 1), the optimal critic is K_PMI plus a constant | strong (proof) | App. F.1; a standard Bayes-optimality computation |
| C5 | Under bijective discrete observations, all modalities' optimal kernels coincide up to an additive constant | strong (proof), in the idealised setting | §4.2 eqs 6–8 with Prop. F.1 (a sufficient, "somewhat strict" representability condition) |
| C6 | Trained models do converge to that kernel "with sufficient data and optimization" | weak (assertion) | §4.2, one sentence |
| C7 | The endpoint is "a statistical model of the underlying reality", a representation of P(Z) | weak (conjecture) | Fig. 1 and §4; the proof reaches only pairwise co-occurrence PMI |
| C8 | Richer captions align better with images | weak–moderate | Fig. 9, one dataset, LLM-generated summaries |
| C9 | Training on images improves language models | weak (citation) | one sentence citing OpenAI (2023), no numbers |
| C10 | Scale may reduce hallucination and bias amplification | weak (implication) | §5, explicitly conditional |

## Method

*(A position paper with measurements.)*

1. Survey convergence evidence (model stitching, Rosetta neurons, model merging, brain alignment).
2. Measure mutual k-NN alignment for vision–vision and vision–language pairs, against competence.
3. Construct an idealised world and derive the NCE optimum.
4. Probe the information limit with caption density.

## Concepts

- **Kernel** — K(x_i, x_j) = ⟨f(x_i), f(x_j)⟩; the paper's definition of what a representation "is" for comparison (§2).
- **Representational alignment** — a similarity metric between kernels (CKA, SVCCA, nearest-neighbour metrics).
- **Mutual k-NN (mNN)** — for paired samples, (1/k)|S(φ_i) ∩ S(ψ_i)|, averaged, where S is the k-nearest-neighbour set within each model's features (App. A, eq. 11).
- **CKNNA** — CKA's cross-covariance restricted to mutual nearest neighbours. It tends to CKA as k grows (App. A, eqs 16–18). Note the typo: "k = 1024 … recovers CKA" in the Fig. 10 caption, while the batch is 1,000.
- **K_PMI** — log P_coor(x_a | x_b)/P_coor(x_a) (eq. 4).
- **Platonic representation** — the hypothesised endpoint of convergence: "a statistical model of reality".
- **Multitask Scaling, Capacity and Simplicity Bias hypotheses (§3)** — three argued pressures toward convergence, none isolated.

## Connections

- **[THEORY-002](../theory.d/THEORY-002.md) (convergence is convergence of kernels, fixing representations only up to the observed symmetry).** The text supports it on every point it takes from this paper, and supplies more.
  - *"Prove".* [THEORY-002](../theory.d/THEORY-002.md)'s word is right for the NCE optimum, with two qualifications. The proof is of the minimiser and of representability under a sufficient condition (Prop. F.1). Reaching the minimiser is asserted. And the kernel reached is the PMI of *windowed co-occurrence*, not a representation of P(Z).
  - *The measurements are weaker than kernel equality.* Confirmed, and more so than [THEORY-002](../theory.d/THEORY-002.md) says. The authors themselves report CKA as showing "a very weak trend" and moved to mNN for that reason. The measured kernel is also not the §4.2 kernel: the features are l2-normalised (cosine, not dot product), truncated, average-pooled, and maximised over layer pairs. The theory's prediction, equality of dot-product kernels up to a constant, is never directly tested.
  - *Toward [THEORY-002](../theory.d/THEORY-002.md)'s promote_when.* App. B gives a partial answer to its second condition. Across the 78 vision models, mNN and linear CKA rank model pairs with Spearman ρ = 0.73 (Fig. 12, printed values). That is mNN against CKA, not Bures, and vision–vision only. So it is a proxy for the measurement promote_when asks for, not the measurement.
  - *The constant offset.* Across modalities the kernels agree only up to separate constants c_X and c_Y (eqs 7–8). Centring (CKA) removes this, and so does any rank-based metric. So the theory is, strictly, about centred kernels. This bears on [LIT-254](../literature.d/LIT-254.md)'s open point about K + c11ᵀ, which it confirms.
- **[THEORY-004](../theory.d/THEORY-004.md).** A representation fixed by its kernel is fixed up to an orthogonal transformation. That is exactly the equivalence the paper adopts in §2. The parenthetical in [THEORY-004](../theory.d/THEORY-004.md) claiming the Platonic claim "disputes it" is not supported (see Corrections).
- **[THEORY-008](../theory.d/THEORY-008.md).** It says CKA, CCA and GULP are averages of readout agreement. Mutual-kNN is not among them. It is not a readout-agreement average but a local, rank-based statistic. So [THEORY-008](../theory.d/THEORY-008.md)'s link between alignment and decodability does not transfer to the paper's headline numbers without an argument.
- **[LIT-253](../literature.d/LIT-253.md) (Nielsen et al.).** Their point that closeness in distribution does not bound representational dissimilarity is the formal reason why C6 (reaching the kernel) cannot be inferred from C5 (it is the optimum). This paper does not engage it (it predates it).
- **[LIT-304](../literature.d/LIT-304.md) (Park et al.).** This is my inference, not the paper's. For language models, the context kernel of the final layer is not identified by the softmax objective: λ ↦ A⁻ᵀλ changes λ(x)ᵀλ(x′) ([LIT-304](../literature.d/LIT-304.md), eq. 3.1). This paper's language kernels are average-pooled hidden states over layers, where that argument does not directly apply. But any claim that two language models "have the same kernel" at the output inherits the gauge [LIT-304](../literature.d/LIT-304.md) identifies.
- **[LIT-241](../literature.d/LIT-241.md) / [LIT-254](../literature.d/LIT-254.md).** [LIT-241](../literature.d/LIT-241.md)'s analogy (GNS: a state fixes the representation up to unitary equivalence) is consistent with §2's kernel definition. The paper itself never mentions GNS.

## Bearing on the record

- **What it supplies for the prior-art map's role (row 10; §2 item 5; the `𝒜^∞` cross-model realism; the R2 warning).** The map says PRH "owns the empirical convergence claim" and that the owner's "Universal Convergence theorem" should be demoted to "PRH-measured + Riesz-argued".
  - *It does own the name and the claim.* It is the paper to cite for "representations converge across models and modalities".
  - *But "PRH-measured" must be stated as what was measured.* That is local nearest-neighbour agreement, rising with competence, small in absolute value (≈0.16 of 1 cross-modally), chosen after a global kernel metric showed "a very weak trend", and taken as the maximum over layer pairs. A response that writes "PRH measured convergence" without these qualifiers inherits the paper's most citable sentence and drops its hedge.
  - *PRH's own theory is a kernel theorem, not a factorisation theorem.* It shows modalities share the PMI kernel up to a constant. By [THEORY-004](../theory.d/THEORY-004.md) that fixes the representation only up to O(d), and by [LIT-304](../literature.d/LIT-304.md) not even that much at a softmax output. Nothing in the paper forces a unique factorisation, a basis, or a concept algebra. There is no Riesz argument anywhere in it. So "Riesz-argued" is the owner's contribution, and it has to stand without PRH behind it.
  - *For `𝒜^∞` ("real concept = stable across every adequate model's concept algebra, anchored to PRH").* Kernel equality would suffice for cross-model invariance of *linear concept geometry* (the Gram matrix of probe directions), since an orthogonal map preserves it. But PRH neither measures kernel equality nor claims it for real models. And §6 caps convergence by the mutual information between modalities and by capacity, and excludes special-purpose systems. "Every adequate model" should be restricted to models sharing the relevant information, as the paper itself restricts it.
- **[THEORY-002](../theory.d/THEORY-002.md).** Supported (see Connections). The reading could add to it:
  - *The metric history.* The measurement metric was adopted after CKA failed to show a trend.
  - *The co-occurrence kernel.* The §4.2 kernel is the PMI of windowed co-occurrence, not a model of P(Z).
  - *A proxy for promote_when.* App. B gives a mNN–CKA Spearman of 0.73 across vision models.

  These are suggestions for the owner; I have not edited [THEORY-002](../theory.d/THEORY-002.md).
- **[THEORY-004](../theory.d/THEORY-004.md).** The "(disputes it)" parenthetical should be revisited. The paper adopts orthogonal equivalence rather than disputing it.
- **[LIT-267](../literature.d/LIT-267.md) (Xiong).** No direct connection. Xiong's lattice is built inside one model, and PRH compares models. The one bridge is conditional: if PRH's kernel convergence held exactly, Xiong's probe-derived incidence would transfer across models, since [NOTE-240](NOTE-240.md) shows it is kernel-determined. PRH does not show exact kernel convergence.
- **ML practice.** Held in the anthology ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md), with [ANTH-THEORY-036](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-036.md) and a practice). Nothing new for practice, beyond the anthology disagreements above.
- **For filing.** Tags as seeded: `representation-learning` first, `philosophy-of-science` second (convergent realism is invoked explicitly, §1). Also defensible: `information-theory` (the PMI kernel, the mutual-information cap). Not proposed: `metaphysics`, because Plato is a gloss and there is no metaphysical argument.

## Limitations

- **A local measure, small in size.** The headline convergence is local nearest-neighbour agreement of modest size. The authors leave open whether 0.16 is "strong alignment" or "poor alignment with major differences left to explain" (§6).
- **The metric was chosen after the fact.** It was adopted after CKA showed "a very weak trend" (App. A). The cross-modal score is also a maximum over all layer pairs, which favours finding alignment.
- **The theory is idealised.** It covers only discrete events and bijective, deterministic observations. It characterises the optimum, not training, and its kernel is pairwise co-occurrence PMI. Stochastic or lossy observations "will not hold" (§6).
- **The three pressures (§3) are arguments.** None is isolated by an intervention.
- **The implications (§5) are conditional speculation.** This includes the hallucination and bias claims, which the authors flag.
- **Scope.** Vision and language only, and the authors say robotics has not converged. Special-purpose systems are excluded by the paper's own argument.

## Open questions

- Do the dot-product kernels of two models trained contrastively on bijectively related data actually match up to a constant? This is the theory's direct prediction and was not tested.
- Does mNN alignment track Bures or CKA alignment across modalities as it does (ρ ≈ 0.73) within vision? This is [THEORY-002](../theory.d/THEORY-002.md)'s promote_when.
- What replaces the theorem when observations are lossy? The paper's suggested cap, alignment bounded by the mutual information between signals and by capacity, is stated without a formal version (§6).

## Corrections to the seeded skim

- Seeded from metadata; the seed's summary is accurate as far as it goes. The text adds three things the summary cannot carry.
  - *The convergence measured is local.* Mutual k-NN with k = 10, over 1,000–1,024 samples (App. C). The authors chose it because CKA "revealed a very weak trend of alignment between models, even when comparing models within their own modality" (App. A). At larger k, which approaches CKA, alignment is "less conclusive" (Fig. 10).
  - *It is small in absolute terms.* "Alignment clearly increases but only reaches a score of 0.16 … The maximum theoretical value for this metric is 1", and whether that is strong or poor alignment is left "as an open question" (§6).
  - *The proof covers pairwise co-occurrence statistics, not P(Z).* The §4.2 heading says contrastive learners "converge to a representation of P(Z)". What is shown is convergence to K_PMI of the windowed co-occurrence distribution P_coor, "certain pairwise statistics of P(Z)" in the paper's own words (§4.2), and that does not determine P(Z).
- Venue and version verified. The v5 PDF carries "Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024", with four equal-contribution authors from MIT. The seed is correct.
- Anthology disagreements ([ADR-013](../decisions.d/ADR-013.md): reported, not fixed).
  - *[NOTE-206](NOTE-206.md) omits the metric-selection history and the ceiling.* Neither [NOTE-206](NOTE-206.md) nor [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md) records that CKA gave "a very weak trend" and that mutual-kNN was adopted afterwards. Nor do they record the 0.16-of-1 ceiling or that the cross-modal score is the *maximum over all layer pairs*, concatenations included (App. C.2). These are the hedges that decide how much "representations are converging" says (DP-010).
  - *[NOTE-206](NOTE-206.md) calls the measure "agreement on pairwise distances".* The measure is overlap of k = 10 nearest-neighbour sets after l2 normalisation and truncation of activations above the 95th percentile (App. A, C.2). It is rank-based and local, and is not agreement on distances.
  - *[NOTE-206](NOTE-206.md) C4 is rated moderate on one citation.* The claim is that training on a second modality improves the first. Its whole support is one sentence citing OpenAI (2023), with no numbers (§2.3, §5). I would rate it weak, and [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)'s "the paper cites a case where that was measured" should say it cites one, unquantified.
  - *[LIT-458](../literature.d/LIT-458.md) and [NOTE-206](NOTE-206.md) frame the caption-density experiment as the hypothesis's "predicted failure direction", measured.* It is one experiment. It uses captions *shortened by LLaMA3-8B-Instruct* summarisation of DCI dense captions, at 5, 10, 20 and 30 words, and averages over all vision and language models (App. E, Fig. 9). It tests whether more caption information raises alignment, which the hypothesis predicts. It does not test bijectivity, and the paper's phrasing is only that denser captions make the mapping "may become more bijective".
  - *[NOTE-206](NOTE-206.md) lists weight-space convergence under Key results.* That is survey (Ainsworth et al., Nagarajan & Kolter, and others), not a result of this paper.
  - *"As models get larger".* [NOTE-206](NOTE-206.md)'s first key result says cross-modal alignment rises with scale. Fig. 3's x-axis is language-modelling score (1 − bits-per-byte on 4M OpenWebText tokens), not parameter count. The abstract's "as vision models and language models get larger" is the paper's own looser phrasing.
- Nucleation disagreement (reported, not fixed). [THEORY-004](../theory.d/THEORY-004.md)'s "What this does not say" has the parenthetical "(see the Platonic-convergence claim, which disputes it)", about orthogonal equivalence being the right notion of sameness. The paper does not dispute it. It *defines* a representation by its kernel (§2, Preliminaries), which is exactly orthogonal equivalence, and its metric is invariant to even more.
