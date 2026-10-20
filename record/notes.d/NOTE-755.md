---
number: 755
status: Read
formerly:
- NOTE-tmpzfpxp
paper: LIT-936
title: 'Picozzi — The information geometry of large language models is shared, learned, and controllable'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v1 of 10 September 2026, 91 pages),
    fetched from arxiv.org/pdf/2609.11063 and extracted with pdftotext,
    with and without -layout: the main text, Methods, all ten Extended Data
    figures and the Extended Data note, and Supplementary Notes 1–20 with
    every theorem and proof. The main-text reference list was checked only
    for the works named below. Figure panels were read from their captions,
    as the plotted values do not survive extraction. Expressions were
    restored by eye where extraction split them across lines.
date: '2026-10-14'
summary: >-
  The Fisher–Rao distance matrix of a model's next-token laws over a context
  battery is a function of the laws alone, so behaviour fixes it, whereas
  activation geometry has a GL(d) gauge. Across ten models of three
  architecture kinds it agrees at a mean rank correlation of 0.88, against
  0.62 for mid-layer activations. The agreement is proved to follow from each
  model's closeness to the same language law, and only about 9% of shared
  eigenvector structure goes beyond what the shared laws imply. The pullback
  metric also gives minimum-disturbance steering, whose cost advantage over
  Euclidean steering it predicts.
---
<!-- inactive-ok-file: QUESTION-027 QUESTION-052 CLAIM-209 CLAIM-193 CLAIM-142 — Open or Proposed; the question this work was registered for and the entries it is set beside, open -->

# NOTE-755: Picozzi — The information geometry of large language models is shared, learned, and controllable

## Contribution

The paper takes the Fisher–Rao metric on a model's next-token distributions,
and its pullback to hidden activations, as the object to study across
language models. It proves that the output-side relational geometry is fixed
by behaviour and is invariant under any output-preserving reparameterisation
of hidden layers, which activation geometry is not. It proves that two
models with small excess risk to a common law must have similar relational
geometry, and it measures that agreement across transformers, state-space
and recurrent models. The rest of the paper is a large empirical programme
on the same object: how token statistics shape the metric's spectrum, how
corpus statistics time the learning of facts, and natural-gradient control
that disturbs other outputs less than Euclidean control.

## Key insight

Activations have no privileged coordinates, since any invertible change of a
hidden layer, undone downstream, leaves behaviour unchanged. Output
distributions do have a privileged geometry, since Chentsov's theorem makes
Fisher–Rao the unique metric invariant under sufficient statistics. So
compare models, and measure the cost of interventions, in output geometry.
Pulled back to activations, that geometry tells which activation directions
matter to the output and how much.

## Assumptions

- **Affine-softmax read-out.** p = softmax(W_U h_L + b_U). The output
  Fisher is H = Cov_p(w) = W_Uᵀ(diag(p) − p pᵀ)W_U, and its pullback to a
  layer is G = Jᵀ H J with J = ∂h_L/∂h (Methods).
- **Identification theorem (SN3, Theorem 5).** A finite set of contexts
  with positive weights. A strictly positive target law, p* =
  min π_X(i) > 0. A resolved representation θ_X = β + U z_X with UᵀU = I_r,
  E z_X = 0 and Cov(z_X) ≻ 0. A rank-matched or overcomplete candidate
  subspace.
- **Convergence theorems (SN4).** A shared outcome space, so the bounds
  apply directly only to models with the same tokenizer. Different
  tokenizers are compared after coarse-graining to the first decoded byte
  (Corollary 4). Native-vocabulary agreement across tokenizers is "empirical"
  only. The population excess risks to the true language law are not
  estimated.
- **Local control.** The KL expansion and the cost-ratio prediction are
  second-order and local. Measured-to-predicted ratios fall as intervention
  magnitude grows (Extended Data Fig. 8b).
- **Scale.** Models from 70M to 7B parameters. A full GPU pullback solve fits
  up to 2.8B. At 6.9B the evidence is limited to spectra and CPU-based
  calibration (SN20).

## Key results

**Origin and identification (Part I).**

- **Local model of output change.**
  KL(p_h ∥ p_{h+δh}) = ½ δhᵀ G_h δh + O(‖δh‖³) (Eq. 1). Across 99
  model–depth–prompt cells in 11 models, the measured-to-predicted KL ratio
  has median 1.000, range 0.948–1.224 (Fig. 1b).
- **Theorem 2 (excess-risk Gibbs duality).** For the induced joint law
  Q(dh, a) = P_H(dh) q(a | h), L(q) − H_P(Y | H) = KL(P ∥ Q), and
  ∇²B(h) = Cov_Q(w_Y | h) is exactly the output Fisher. "Next-token training
  therefore induces the geometry."
- **Theorem 5 (global identification).** K_{D,d}(S) ≥ c_{D,d} Δ_d(S, T)²,
  with c_{D,d} = min{p*² m_z/64, w* p*/(4r)} > 0 and
  Δ_d(S, T) = ‖P_{S^⊥} P_T‖_F. K_{D,d}(S) = 0 iff T ⊂ S. "Hence a
  rank-matched read-out identifies the unique subspace T". Corollary 1 gives
  recovery at a square-root rate:
  Δ_d ≤ (√ζ_r + √ε_m)/√c. Empirically, held-out profiled loss grows
  linearly in squared subspace distance, R² ≥ 0.9999 on all eight paths
  (Fig. 1a, Pythia 70M–1.4B against a rank-32 reference from Pythia-6.9B).
- **Proposition 1 (activation geometry is not identifiable).** For every
  A ∈ GL(d), f = (g ∘ A⁻¹) ∘ (A h) has identical conditional laws, and the
  activation Gram matrix becomes Z AᵀA Zᵀ. "Behaviour does not determine a
  unique Euclidean activation geometry, whereas the output geometry is a
  functional of the conditional laws." Proposition 3 gives an integer
  example of two models with identical outputs whose hidden relational
  geometries have rank agreement exactly −4/17.
- **Causal language assignment (SN3.1).** Three architectures at two
  capacities were trained on eight pairs of synthetic languages (64
  contexts, 64 outcomes, matched entropy). The assigned law recovers
  0.997836 of the imposed geometric separation, and changing architecture
  within a law leaves the geometry nearly unchanged. Both contrasts are
  positive in all eight pairs (P = 1/256).

**Shared geometry (Part II).**

- **Measured agreement.** Agreement is the Spearman correlation of the upper
  triangles of the Fisher–Rao distance matrices
  d_ij = 2 arccos Σ_a √(p_i(a) p_j(a)). Over ten models (70M–7B; seven
  training pipelines, four tokenizers), the mean is 0.88 on natural text,
  against 0.62 for mid-layer and 0.61 for last-layer activation geometry.
  The gap's bootstrap interval excludes zero. At the first-byte level,
  cross-tokenizer agreement is 0.91. Random anisotropic reparameterisations
  leave output agreement constant to machine precision, while activation
  CKA, mutual k-NN and cosine RSA degrade.
- **Theorem 6 (excess risk forces relational convergence).**
  E_{X,Y}{d_A(X,Y) − d_B(X,Y)}² ≤ 4(ε_A + ε_B) for root-probability distance
  matrices. **Theorem 8:** 1 − τ ≤ 2F_q(t) + 32(R_m + R_m′)/t², so τ → 1 as
  the risks vanish, given no ties in the reference.
- **Remark 2 (why the bound is not the explanation).** On real models "the
  worst-case form of Theorem 7 is vacuous". The per-context disagreement is
  large (median root-probability distance 0.30–0.71) while the margins are
  0.08–0.14. The observed stability comes from low coherence (median
  0.024–0.034). The direction in which two models disagree is nearly
  orthogonal to the relational structure. "A model pair that disagreed
  systematically along relational directions could agree far less at the
  same per-context excess risk." Deterministic certificates on same-tokenizer
  pairs give τ ≥ 0.61–0.67 against an observed 0.76–0.83 (Supplementary
  Table 1). Agreement rises along the Pythia ladder as KL to Pythia-6.9B
  falls.
- **Theorem 10 (six-scalar identity).**
  Corr(C_m, C_n) = (v_S + c_m + c_n + k_mn)/√((v_S + v_m + 2c_m)(v_S + v_n + 2c_n)).
  It reconstructs all 112 measured configurations. The attenuation floors of
  Theorem 11 are "valid but vacuous": realised variances are near 0.005
  against bounds near 1.3.
- **What is shared beyond the laws (SN18).** The top-six cross-family
  eigenvector overlap is 0.698. A displacement-magnitude-matched null gives
  0.636, so the residual is +0.063 (+0.056 to +0.070), "about 9% of the raw
  overlap". "The remaining 91% is the shared displacement-magnitude
  structure, which follows from the shared output distributions alone."
- **Meaning and transfer (SN5, SN19).** The consensus geometry aligns with a
  Sentence-BERT geometry at 0.044 (natural), 0.102 (templated) and 0.440
  (factual relation). The factual-relation figure falls to +0.231 after
  partialling out surface form. Model residuals align at about zero. A
  probe on Fisher–Rao distances to 40 anchor prompts, trained on one model
  and tested on held-out prompts through another, gets 0.659 eight-way
  accuracy (0.700 through the consensus alone, 0.724 within model, chance
  0.125). Through the residual it gets 0.091.
- **Human predictions (SN19).** Model–human semantic distance falls with
  scale on two corpora. A risk-to-alignment relation fitted on Pythia
  predicts OLMo and five external models without refitting, r = 0.758,
  RMSE 0.029. On a third corpus the leading model directions recover human
  directional structure (lower bounds positive in six of seven families), but
  "full-reconstruction bounds remain non-positive".

**Learned structure (Part III).**

- **Spectrum.** Output-Fisher eigenvalues fall as λ_i ∼ i^{−β}, β ≈ 1, over
  ranks 2–80. **Theorem 12:** a_K q_k ≤ λ_k(H) ≤ A_K q_k + ε_K, with
  q_a = p_a ‖v_a‖². On real models A_K has median 14, so the band is loose.
  The realised spectrum still tracks the profile within a median exponent
  deviation of 0.04. A token-profile prediction with no fitted parameters
  gives held-out spectral errors of 0.0617–0.0884 decades in five external
  families.
- **Clusters (SN6.3).** The head needs singleton tokens and the bulk forms
  interchangeable clusters. "Fresh-context tests do not support a universal
  fixed partition".
- **Acquisition (SN7).** Corpus n-gram margins predict fact-acquisition
  trajectories without refitting, R² = 0.775–0.792. In a randomised
  synthetic language, deep evidence delays the 10th–20th percentile of
  acquisition by Δ = 2.103 [1.79, 2.40] log₂ steps, about 4.3×. In a crossed
  study of three decoder styles and two languages, the delay is 0.81–1.51
  log₂ steps. **Theorem 22:** nominal depth alone cannot order acquisition
  time without an assumption about learner-relative rates.

**Control (Part IV).**

- **Theorem 26.** The minimum-cost step for q ᵀδ = b under A = G + αR is
  δ_N = b A⁻¹q/(qᵀA⁻¹q). Every feasible step has excess cost ½‖δ − δ_N‖²_A.
  The Euclidean-to-natural cost ratio is
  Γ_A(q) = (qᵀAq)(qᵀA⁻¹q)/(qᵀq)² ∈ [1, (M + m)²/(4Mm)], and it falls to 1
  as damping grows.
- **Prediction of cost.** The finite-damping ratio
  R_pred = Π_G(q)/Π_G(A⁻¹q) is computed before intervention. Over 3,515
  matched responses from 1,188 cells, the measured-to-predicted median is
  0.967 (0.957–0.975) and the log–log slope 0.982 (0.966–0.997). Relinearised
  Fisher paths accumulate 11–127 times less local KL than Euclidean ones.
- **Reusable control (SN10.5).** One activation update per model and
  objective, built on four donor prompts with a reference-prompt Fisher,
  moves eight unseen prompts of the same model in the right direction in
  all 24 settings. At matched donor change, its reference-continuation KL is
  2.90–6.29 times lower than Euclidean. "The experiment does not require
  aligned hidden coordinates between models": the reuse is within a model.
- **Other operations (Table 1).**
  - Knowledge editing: 10.57× lower other-token KL than the matched
    Euclidean edit on 30 GPT-2 edits. The EasyEdit comparison with ROME and
    MEMIT is "benchmark context rather than a controlled method ranking".
  - SAE ablation cost: ρ = 0.997, against 0.896 for activation magnitude.
  - Planted-feature recovery: 0.167 → 0.480.
  - Natural-gradient LoRA: 1.57× better preservation frontier than
    AdamW + KL. The task-transfer and capability endpoints "did not support a
    broader conclusion".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The output Fisher–Rao relational geometry is a function of the conditional laws, invariant under output-preserving reparameterisation; activation geometry is not | strong | Lemma 2(a), Proposition 1, Proposition 3; numerical gauge test |
| C2 | Behaviour identifies the read-out subspace at matched rank, with a quadratic margin | strong | Theorem 5, Corollary 1 (finite support, positive laws) |
| C3 | Excess risk to a common law forces relational convergence | strong | Theorems 6 and 8, on a shared outcome space |
| C4 | Across architectures, output geometries agree more than activation geometries (0.88 against 0.62) | moderate | ten models, three batteries, bootstrap; cross-tokenizer native agreement is empirical |
| C5 | Observed agreement comes from disagreement being nearly orthogonal to relational structure, not from the bound | moderate | coherence measurements, SN4 Remark 2 |
| C6 | Shared structure beyond the shared laws is small (+0.063, about 9% of raw overlap) and lives in the leading modes | moderate | displacement-magnitude-matched null, SN18 |
| C7 | The shared component carries transferable category structure | moderate | 40-anchor probe transfer, 0.659 against chance 0.125; one eight-way task |
| C8 | The language law, not the architecture, determines the learned geometry | strong | randomised synthetic assignment, eight pairs; synthetic only |
| C9 | Evidence depth causally delays fact acquisition | strong | randomised and crossed synthetic experiments |
| C10 | The pullback metric gives minimum-disturbance interventions, and their advantage over Euclidean is predicted without fitted parameters | strong | Theorem 26; 3,515 matched observations |
| C11 | The same correction improves editing, attribution, dictionary learning and fine-tuning | weak | single configurations, mostly one model each; descriptive benchmark comparisons |

## Method

- **Relational geometry.** For a fixed battery of contexts, compute each
  model's next-token laws, form the matrix of Fisher–Rao distances
  2 arccos(Bhattacharyya affinity), and compare models by the Spearman
  correlation of the upper triangles. Activation geometries use cosine
  distances of mid- or last-layer states. Three batteries are used: 200
  WikiText prefixes, 160 templated contexts in eight topics, and 120
  factual-relation prompts.
- **Pullback metric.** Apply G = JᵀHJ matrix-free, with a Jacobian–vector
  product, the closed-form H, and a vector–Jacobian product. Solve
  (G + αI)⁻¹q by conjugate gradients or a Woodbury low-rank form, with
  α = c λ_max(G) and c ≈ 10⁻². The CG iteration bound is independent of
  width (Proposition 8: at most 85 iterations at c = 10⁻² and residual
  10⁻⁶).
- **Matched comparisons.** Each method's step is scaled by binary search to
  the same realised objective change, and off-target KL is compared there.

## Concepts

- **Output Fisher, H.** The p-weighted covariance of read-out rows,
  Cov_p(w). It is blind to the p-weighted mean direction (Eq. 37).
- **Pullback metric, G.** JᵀHJ at an intervention layer. Its null space is
  the activation directions with no effect on p.
- **Relational geometry.** The context-by-context matrix of Fisher–Rao
  distances between next-token laws.
- **Consensus and residual.** The mean of rank-transformed distance matrices
  across models, and one model's matrix with the consensus partialled out.
- **Effective dimension.** N_eff(α) = Σ_k λ_k/(λ_k + α), a soft count of
  modes resolved at damping α.
- **Anisotropy ratio.** Γ_A(q) or R_pred: how much more output a Euclidean
  step disturbs than the natural step, for the same objective change.

## Connections

The comparison recasts the convergence of the Platonic Representation
Hypothesis ([LIT-302](../literature.d/LIT-302.md)) in output geometry, where convergence "follows from
predictive fit rather than from a chosen activation-similarity measure". It
contrasts its measure with CKA ([LIT-254](../literature.d/LIT-254.md), unread here) and calibrates
against Gröger et al.'s permutation-null critique. The transfer probe uses
relative representations (Moschella et al., [LIT-849](../literature.d/LIT-849.md)) with Fisher–Rao
distances in place of cosines. The paper cites Marconato et al. ([LIT-950](../literature.d/LIT-950.md))
for identifiable properties of next-token predictors, and Nielsen et al.
([LIT-253](../literature.d/LIT-253.md), unread) for when closeness in distribution implies
representational similarity. Its steering builds on FishBack and Park, Nief,
Choe and Veitch's "information geometry of softmax". The natural gradient is
Amari's. The paper notes the quantum analogue, the Fubini–Study metric, and
the author's own quantum natural-gradient work.

## Bearing on the record

- **[QUESTION-027](../questions.d/QUESTION-027.md).** The relational geometry is a signature of the kind the
  question describes. It is stable under an admissible class of
  transformations: every output-preserving reparameterisation of hidden
  coordinates, exactly (Proposition 1), and as measured. It is identified
  from the probes, which are the conditional laws on a context battery. It
  is the record's first held, measured case. But both properties hold
  because the signature is a function of the observed laws (Lemma 2(a):
  "immediate"). That is the in-probe case that [QUESTION-027](../questions.d/QUESTION-027.md) calls
  automatic. The admissible transformations are reparameterisations of one
  network, or changes of architecture fitted to one law. They are not
  transports between realizations whose laws differ. [LIT-936](../literature.d/LIT-936.md)'s status note
  ("measures a coordinate-free relational signature that agrees across
  architectures") is accurate as a description of the measurement. It does
  not say, and the paper does not show, that the signature is identified
  where the latent model is not in [QUESTION-027](../questions.d/QUESTION-027.md)'s restricted sense.
- **Where the paper reaches outside the probes.** Two results reach decisions
  beyond the fitted relations, and both are empirical and narrow. One is
  the 40-anchor probe trained on one model and applied to held-out prompts
  of another (0.659 against 0.724 within model). The other is the
  risk-to-human-alignment relation applied to unseen model families without
  refitting (r = 0.758). Neither is a theorem, and the transfer probe is one
  eight-way topic task.
- **[CLAIM-209](../claims.d/CLAIM-209.md).** The paper is evidence for the unrestricted second sentence,
  which [CLAIM-209](../claims.d/CLAIM-209.md) already grants. For the restricted clause, the transfer
  results above are a measured case of a decision outside the training
  prompts that is supported across realizations. They come with a stated
  margin (0.659 against chance 0.125) and are not a construction. They bear
  on [CLAIM-209](../claims.d/CLAIM-209.md)'s second defeat disjunct, failure on held-out realizations,
  and they do not meet it.
- **[CLAIM-148](../claims.d/CLAIM-148.md).** Propositions 1 and 3 restate [CLAIM-148](../claims.d/CLAIM-148.md)'s point for networks:
  the GL(d) gauge of a hidden layer is not a symmetry of anything
  observable. Proposition 3 sharpens it. Two models with identical outputs
  can have hidden relational geometries that rank-correlate negatively
  (−4/17), so no floor on hidden-geometry agreement follows from output
  agreement.
- **[THEORY-175](../theory.d/THEORY-175.md).** Consistent with it. Distances to matched anchors give a
  representation that transfers between models with loss. Here the
  distances are Fisher–Rao on outputs, not cosines on activations, and the
  invariance is to every output-preserving map, not only to cosine-preserving
  ones. Cross-model transfer goes through the shared consensus. The
  model-specific residual transfers below chance.
- **[CLAIM-193](../claims.d/CLAIM-193.md) and [CLAIM-142](../claims.d/CLAIM-142.md).** Remark 2 is a measured instance of agreement
  relative to probes. Agreement on a battery holds because disagreement
  falls in directions the battery's relational structure does not see. The
  paper itself says a pair disagreeing "along relational directions could
  agree far less at the same per-context excess risk".
- **[QUESTION-052](../questions.d/QUESTION-052.md).** The output Fisher's leading eigenspace is where
  cross-model sharing, steering weight and answer-relevant motion
  concentrate (Extended Data Fig. 9). That is a measured case of a top
  eigenspace being the shared, decision-relevant part, though of a
  per-context covariance operator, not of the pair operator [QUESTION-052](../questions.d/QUESTION-052.md)
  defines. Only about 9% of the eigenvector overlap exceeds what the shared
  laws imply.
- **Machine-learning practice.** The paper carries instructions for
  machine-learning practice: steer, edit and fine-tune with the pullback
  Fisher metric, and compare models in output geometry. Those belong in the
  Anthology of the SOTA, which the `anthology-candidate` flag records. It
  is held here only for [QUESTION-027](../questions.d/QUESTION-027.md), under [ADR-013](../decisions.d/ADR-013.md).

## Limitations

- A v1 preprint by a single author, not yet peer-reviewed. Generative AI
  "assisted with research and manuscript preparation". Code and derived data
  are available only on request.
- The convergence theorems need a shared outcome space and the population
  risks are not estimated. On real models the worst-case bounds and floors
  are vacuous, and the stability is explained by a measured coherence, not
  by a theorem.
- "Agreement" is rank agreement of distance matrices on fixed batteries of
  120–200 contexts. Semantic alignment of the shared component is small on
  natural text (0.044).
- The identification theorem is for finite support and strictly positive
  laws, and its empirical test uses a rank-32 reference built from
  Pythia-6.9B, not the language itself.
- The causal results (language assignment, evidence depth) are on small
  synthetic languages and compact models.
- Control results are local. The advantage shrinks with intervention size
  and towards the read-out layer. Several operations (editing, SAE, LoRA)
  rest on one model or one configuration each. The paper says that broader
  capability retention is not established.
- Negative findings are reported. There is no universal fixed token
  partition. Full human-law recovery bounds are non-positive. Qwen2's
  calibration gain is negative. The direct item-level cost–meaning
  association is null (SN18).

## Open questions

- Does output-geometry agreement survive between models trained on
  different laws, such as different corpora, languages or post-training?
  The same-corpus control is near zero on natural text, so the paper does
  not separate law from corpus there.
- What is shared beyond the laws? Only the +0.063 residual is, and it is
  graded by training lineage. A study that holds the law fixed and varies
  training would say whether that residual is a signature of the procedure.
- For [QUESTION-027](../questions.d/QUESTION-027.md): is there a theorem for decisions outside the battery,
  such as the anchor-probe transfer? It would need to bound held-out decision
  loss by battery-level excess risk and anchor coverage.
- Native-vocabulary agreement across tokenizers has no proof. A common
  outcome space finer than the first byte would close part of the gap.
