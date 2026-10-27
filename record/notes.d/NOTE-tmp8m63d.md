---
status: Read
paper: LIT-tmp9yvin
title: 'Scherlis et al. — Polysemanticity and capacity in neural networks'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the arXiv PDF of 2210.01892v4 (23
    pp., 25 March 2025; its comment: "Improved notation and corrected an
    error in the description of the most general efficient matrices"),
    text extracted with pdftotext. Read: the abstract, §§1–5 (capacity
    and superposition, the quadratic model, its phase diagrams, other
    models and nonlinearities, the geometry of efficient matrices,
    conclusions), the author contributions, the acknowledgements, the
    references, and Appendices A–H (the expected loss, covariances, the
    loss minimization and its feasibility, kurtosis and sparsity, the
    correlation-coefficient reading, the proof of the capacity bound, the
    alternative capacity, and the feasibility proofs with Lemmas 1–2 and
    Theorems 1–2). v1, v2 and v3 were fetched and compared at the places
    noted below. The Alignment Forum post announcing the paper
    (kWp4R9SYgKJFHAufB, 2022-10-07) was read in full. The seven figures
    were read from their captions and the text; no number was taken from
    a chart. Equations (12), (13), (14), (15), (19), (20) and the phase
    boundaries of §3.5.2 were re-derived, and (12)–(13) and the
    allocation were checked numerically (the reader's own script, not
    part of the record).
date: '2026-10-27'
summary: >-
  In a model computing Σ(W_i·x)² + b to fit Σ v_i x_i², with independent
  unit-variance inputs of fourth moment k, the expected loss is
  (k − 1)Σ(n_i − v_i)² − 2Σn_i² + 2Σn_i²/C_i, so the marginal value of
  capacity is −2n_i²/C_i² and the optimum has a closed form: dense inputs
  (k ≤ 3) give every feature all or nothing, sparse ones (k > 3) share
  features whose importance lies between 2λ/(k − 1) and λ. Efficient
  embeddings are exactly block-semiorthogonal. Re-derived and checked.
  The bearing on trained networks is argued, not shown.
---
<!-- inactive-ok-file: THEORY-tmp2tsxo THEORY-1013 THEORY-802 — Proposed; the authors' wider account filed from this reading and the accounts it bears on, cited as open -->
# NOTE-tmp8m63d: Scherlis et al. — Polysemanticity and capacity in neural networks

## Contribution

It recasts superposition as a budget problem. A feature's capacity is the
fraction of an embedding dimension it uses; a layer has at most as much
capacity as it has dimensions; and at the loss minimum each feature gets
capacity until its marginal value falls to a common threshold, unless it
is worth a whole dimension even then or nothing even at zero. Features
are polysemantic exactly when they are partially represented. The paper
then gives a toy model in which the whole allocation can be solved in
closed form, and classifies the embedding matrices that use all their
capacity.

## Key insight

In the quadratic model the interference between features enters the
loss only through each feature's own capacity: the loss is a sum of a
term in the embedding lengths and one term per feature in n_i²/C_i. So
the marginal value of capacity for feature i, −∂L/∂C_i = 2n_i²/C_i²,
depends on nothing else in the model, and the allocation problem
separates. Sparsity enters through the fourth moment k: above 3, returns
to capacity diminish and sharing pays; at or below 3, they do not.

## Assumptions

- **Capacity** C_i = (w_i·w_i)² / Σ_j (w_i·w_j)², with w_i the embedding
  vector of feature i (a column of W) and C_i = 0 for w_i = 0. It lies in
  [0, 1], and Σ C_i ≤ D, the embedding dimension (Appendix F). It is the
  squared correlation between x_i and (WᵀWx)_i (Appendix E).
- **The general argument (§2.2)** assumes only that more capacity never
  raises the loss and that every allocation satisfying the constraints
  is realizable by some W; it does not depend on the definition of
  capacity.
- **The quadratic model (§3).** Target y = Σ v_i x_i², a scalar, with v_i
  the importance of feature i; model ỹ = Σ_rows (W_r·x)² + b, a sum of
  squared neuron pre-activations. Inputs independent, mean 0, variance 1,
  common fourth moment k (the paper calls k "the kurtosis", which it is
  for unit variance). Squared-error loss, optimal bias.
- **Sparsity** is modelled as x = s·z with s ~ Bernoulli(p) and
  Var z = 1/p, so k = Kurt(z)/p rises as p falls; for z uniform,
  k = 9/(5p) (Appendix D).
- **Comparison models (§3.7)** are Elhage et al.'s autoencoder ([LIT-323](../literature.d/LIT-323.md))
  and this model, each with quadratic, ReLU and GeLU activations, six
  features in three or five dimensions, solved numerically.

## Key results

- **The expected loss (eq. 12, Appendix A).**
  E[L] = (k − 1)Σ_i(‖w_i‖² − v_i)² + 2Σ_{i≠j}(w_i·w_j)². The first term is
  the fit to true correlations, the second "hallucinated correlations"
  Cov[ỹ, x_i x_j] that the target does not have (Appendix B). Large k
  weights the first more heavily, so the model accepts interference.
- **In capacities (eq. 13–14).** With n_i = ‖w_i‖²,
  E[L] = (k − 1)Σ(n_i − v_i)² − 2Σn_i² + 2Σn_i²/C_i, and
  ∂L/∂C_i = −2n_i²/C_i² at the optimal lengths.
- **The optimum (eq. 15–18, Appendix C).**
  C_i = clip((k − 1)v_i/((k − 3)λ) − 2/(k − 3), 0, 1), with λ fixed by
  Σ C_i = D, and n_i = λC_i in the interior. For k > 3, feature i is
  ignored if v_i ≤ 2λ/(k − 1), fully represented if v_i ≥ λ, and shared
  in between. For k ≤ 3 the loss is concave in each C_i, so the D most
  important features each get a dimension and the rest none. The
  solution is feasible: any allocation with 0 ≤ C_i ≤ 1 summing to D is
  realized by a semiorthogonal W (Theorem 1, Appendix H).
- **One feature apart (§3.5.2).** N features, D < N dimensions,
  v_1 = V and the rest 1: λ = (k − 1)(N − 1 + V)/((k − 3)D + 2N);
  C_1 = D/N at V = 1; feature 1 takes a whole dimension once
  V ≥ (k − 1)(N − 1)/((k − 3)(D − 1) + 2(N − 1)), which tends to
  (N − 1)/(D − 1) as k grows and never exceeds it, and is dropped once
  V ≤ 2(N − 1)/((k − 3)D + 2(N − 1)). At k = 3 both thresholds are 1.
- **The phase diagram (Figure 4).** Six features in three neurons: a
  sharp jump from ignored to monosemantic at low sparsity and a smooth
  passage through a shared phase at high sparsity, meeting at a
  critical point, likened to a second-order transition. The analytic and
  empirical panels are shown side by side; no numerical agreement is
  stated.
- **Other models (§3.7, Figure 7).** The same shape for this model under
  ReLU and GeLU. Elhage et al.'s autoencoder has a large region stuck
  near C = 1/2 (antipodal pairs), a wider shared region, and, with six
  features in three dimensions, sharing even for features far more
  important than the rest.
- **Efficient matrices (§4, Appendix H).** W with Σ C_i = D are exactly
  those of the form QBP: an orthogonal rotation, a block-diagonal B of
  scaled semiorthogonal blocks, and a permutation (Theorem 2). Within a
  block n_i ∝ C_i; across blocks features do not interfere. Small blocks
  are the polytopes Elhage et al. found; this model always has one large
  block, so its shared features project onto many neurons in any basis.
  With many small blocks a basis exists in which each neuron mixes only a
  few features.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | At the optimum, capacity is allocated until marginal loss reduction equals a common threshold, with 0 and 1 as corners | demonstrated (KKT) | §2.2, under its two assumptions |
| C2 | In the quadratic model the loss depends on W only through capacities and lengths, with the closed-form optimum above | demonstrated | Appendices A and C; re-derived and checked here |
| C3 | Sparser (higher-kurtosis) inputs favour superposition; k ≤ 3 never shares | demonstrated in this model | eq. 15–18, Appendix D |
| C4 | Σ C_i ≤ D, and equality holds exactly for block-semiorthogonal W | demonstrated | Appendices F and H, Theorems 1–2 |
| C5 | The quadratic model's phase diagram predicts "a broad family of 2-layer models" | weak to moderate | Figure 7, six features, by eye |
| C6 | Architecture sets block size, and so how polysemantic neurons are, and could be used to control it | weak (a conjecture) | the contrast with Elhage et al.'s model |
| C7 | The capacity framework captures something of how real networks allocate features | weak | the authors' hope ("probably substantially messier" in large models) |

## Concepts

- **Capacity**: the fraction of a dimension a feature uses,
  (w_i·w_i)²/Σ_j(w_i·w_j)².
- **Efficient embedding**: one whose capacities sum to the dimension.
- **Hallucinated correlation**: a correlation of the output with x_i x_j
  that the target lacks, the cost of sharing.
- **Semiorthogonal (the "everything bagel")**: rows orthonormal,
  WWᵀ = λI; all capacity in one block.
- **Tegum product**: a block-diagonal combination of semiorthogonal
  blocks in orthogonal subspaces.

## Connections

It builds on Toy Models of Superposition ([LIT-323](../literature.d/LIT-323.md)) and contrasts its
model with that one throughout: the autoencoder compresses and recovers a
vector, this model computes a nonlinear function of many features with
fewer neurons. It cites Softmax Linear Units for changing the activation
to reduce polysemanticity, and Zoom In ([LIT-1543](../literature.d/LIT-1543.md)) and Feature
Visualization for the phenomenon. The causal scrubbing appendix
([LIT-1583](../literature.d/LIT-1583.md), [NOTE-1202](NOTE-1202.md), §6) uses this model with two features and one
neuron, ỹ = (cx₁ + dx₂)² + e for y = ax₁² + bx₂², and the condition it
states for superposition there ("a and b having similar values and x₁
and x₂ having high kurtosis") is the interval of eq. 17–18: with v₁ =
v₂, k > 3 puts both features in the shared phase.

## Bearing on the record

- **[LIT-1583](../literature.d/LIT-1583.md) and [NOTE-1202](NOTE-1202.md).** §6's model is identified and its condition
  for superposition is now derived in the record ([THEORY-tmp68zar](../theory.d/THEORY-tmp68zar.md)). The
  appendix's rewrite into monosemantic terms and a resampled interference
  term 2cd·x₁x₂ is exactly the second term of eq. 12, the
  "hallucinated correlations" the model pays for.
- **[THEORY-1013](../theory.d/THEORY-1013.md) and the curve units.** A reason, in a toy, why some units
  are clean and others shared: features important enough relative to the
  threshold get a dimension of their own. Whether the curve units are such
  features is not something this paper can say. The Overview's three
  double-curve units "likely best thought of as a polysemantic neuron"
  ([NOTE-tmpdmtd9](NOTE-tmpdmtd9.md)) are the kind of case it describes.
- **[THEORY-802](../theory.d/THEORY-802.md) and [THEORY-991](../theory.d/THEORY-991.md).** The geometry result is basis-relative in
  the way [THEORY-802](../theory.d/THEORY-802.md) says: a small-block solution is monosemantic only
  after the right rotation, while a large block is polysemantic in every
  basis. [THEORY-991](../theory.d/THEORY-991.md)'s sparse dictionary in a real transformer is the
  practical counterpart: a change of basis that recovers features the
  neurons share.
- **Accounts filed.** [THEORY-tmp68zar](../theory.d/THEORY-tmp68zar.md) (Active, re-derived and checked
  numerically): the quadratic model's loss decomposition and optimal
  allocation. [THEORY-tmp2tsxo](../theory.d/THEORY-tmp2tsxo.md) (Proposed): the authors' wider account,
  that polysemanticity in trained networks is capacity allocation of this
  kind, driven by sparsity and shaped by architecture.

No instruction for machine-learning practice; the anthology may want the
work as a reading (`anthology-candidate`).

## Limitations

- **A toy.** One hidden layer, a scalar output, independent features of
  equal fourth moment, quadratic activation for the analytics; the other
  activations and models only in figures with six features.
- **The analytic and empirical phase diagrams** are compared by eye.
- **No trained network** is examined. The authors call the work "more of
  a side-project than a core research project" in the announcing post.
- **Internal inconsistencies and slips** (all in v4; checked in v1 where
  noted).
  - The model is "one-layer" in §1 and §2.1 and "two-layer" or "2-layer"
    in §3, §1 and §5 (also so in v1).
  - λ is used for three things: the Lagrange multiplier of eq. 4, a
    rescaled quantity in eq. 15–20 (with ∂L/∂C_i = −λ₄ at an interior
    point, eq. 15's λ is n_i/C_i = √(λ₄/2), not λ₄), and the scale of a
    semiorthogonal matrix in §4.2.
  - §4.3 makes the blocks λ_k R_k and then states n_i = λ_k C_i
    (eq. 24), which holds for blocks √λ_k R_k, as §4.2's √λ R and v4's
    corrected §4.4 (√γ_k R_k) have it. v1 to v3 state §4.4 without any
    scale; §4.3 is unchanged in v4.
  - §3.6 says the marginal loss curves go "from convex (A) to flat (C),
    and eventually to concave (E)" as sparsity increases, and three
    sentences later that "when features are dense, the curves are
    concave". The two sentences give dense inputs opposite curvatures;
    §2.2 and §3.4 (the loss concave in C_i for k ≤ 3) agree with the
    second.
  - Figure 4's caption calls ∂L/∂C_i the "marginal loss reduction", which
    is −∂L/∂C_i, as Figure 2's caption has it.
  - Appendix E writes "(k − 1)(X, Y)" where a covariance is meant, in its
    definition of ρ² and in eq. 63–66 (also in v1): a substitution error
    that leaves the derivation unreadable as printed. The result,
    ρ² = C_i, follows with Cov in its place.
  - §3.2 says no restriction beyond zero mean and identity covariance is
    imposed, but eq. 12 needs independence and a common fourth moment,
    as §3.1 and Appendix A assume.
  - Appendix H's proof switches between N and n, sets the sum of
    capacities to m where D is meant, and writes dim T = m.
  - The contributions credit "JS" with feedback, and no author has those
    initials. The Alignment Forum post lists Jacob Steinhardt among the
    authors; every arXiv version lists five authors without him and
    thanks him in the acknowledgements.

## Open questions

- Do capacities measured in a trained network, at any layer, follow the
  threshold rule: features with C_i strictly between 0 and 1 having equal
  marginal loss reduction?
- Does block size in trained models track architecture, as the
  comparison with Elhage et al.'s model suggests, or the data?
- With dependent features, as real ones are, does the loss still separate
  by capacity?
