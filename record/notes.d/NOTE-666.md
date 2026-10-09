---
number: 666
status: Read
formerly:
- NOTE-tmpfkzni
paper: 'LIT-862'
title: 'A mathematical theory of semantic development in deep neural networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09. The published main text was read in full from
    PubMed Central (PMC6561300, the article's HTML; equations checked
    against its MathML where the plain-text extraction dropped square
    roots), with figure captions; figures not seen. The Supplementary
    Material was read from the arXiv PDF of v1 (23 October 2018; pdftotext
    extraction): the derivation of the averaged dynamics, the decoupled
    solution and its stated assumptions, the transition-time and
    illusory-correlation estimates, the hierarchical spectrum, the
    typicality identities, the random-matrix coherence threshold, the
    Eckart–Young argument, the GMRF structural forms, inductive projection
    and the minimum-norm proof, all followed; matrix displays garbled in
    extraction were reconstructed from context, not checked. The published
    SI, which per the main text adds deeper networks and correlated
    inputs, could not be fetched (PMC returned a browser-check page) and
    was not read. The arXiv v1 main text was compared with the published
    one at the equations only. Plain text saved as paper.txt in the
    session's download directory.
date: '2026-10-09'
summary: >-
  Shows that a two-layer linear network trained from small weights learns
  the singular modes of its input–output correlations in order of strength,
  each by a sharp sigmoidal transition, where a shallow network learns all
  modes together; and that the singular structure of data generated on
  trees, rings and clusters, plus a minimum-norm property, accounts for
  coarse-to-fine differentiation, transient errors, narrowing
  generalisation, typicality, coherence thresholds and conserved
  representational similarity. Exact only from decoupled, balanced
  initial weights with white inputs; random initialisation is simulated.
---
<!-- inactive-ok-file: THEORY-186 — Proposed; the account this reading produced -->
<!-- inactive-ok-file: THEORY-182 THEORY-183 THEORY-039 THEORY-004 THEORY-002 THEORY-019 — Proposed; accounts this reading bears on -->

# NOTE-666: A mathematical theory of semantic development in deep neural networks

## Contribution

Simulations had shown that connectionist networks trained on items and
their properties differentiate broad categories before fine ones, change
in stages, and narrow their generalisations, much as children do (Rogers
and McClelland 2004). This paper derives those behaviours analytically in
the simplest model that shows them, a linear network with one hidden
layer. It also gives mathematical definitions of typicality, category
prototype and category coherence, taken from the SVD of the item–feature
correlations, and proves the behavioural consequences the definitions are
meant to have. And it proves that minimum-norm solutions share their
hidden similarity matrix, offered as an account of why representational
similarity is conserved across people and species.

## Key insight

Depth makes learning multiplicative. Each mode's strength is a product of
an input-side and an output-side factor, and each factor's gradient is
proportional to the other. Growth from near zero is therefore
self-reinforcing and sigmoidal, at a rate set by that mode's singular
value. The data's singular spectrum then becomes a schedule. Strong modes,
which in natural hierarchies are the broad distinctions, switch on first
and suddenly; weak ones wait. A shallow network has no such product, so
it learns every mode at once and smoothly. The learned representation is
the SVD of experience, revealed one mode at a time.

## Assumptions

- **Architecture and loss.** ŷ = W₂W₁x, no nonlinearity, squared error,
  online gradient descent with learning rate λ small enough that τ/s₁ ≫ 1,
  i.e. λ ≪ 1/(s₁P). The analysis is of the epoch-averaged continuous-time
  flow τ dW₁/dt = W₂ᵀ(Σyx − W₂W₁Σx), τ dW₂/dt = (Σyx − W₂W₁Σx)W₁ᵀ.
- **White inputs**, Σx = I: one-hot or orthonormal item codes. The
  published main text says the SI treats a special case of correlated
  inputs; the arXiv SI does not.
- **Decoupled, balanced initial conditions.** In the SVD basis
  W̄₁ = RᵀW₁V and W̄₂ = UᵀW₂R start diagonal, with equal diagonal entries
  c_α = d_α. Then a_α = c_αd_α obeys τ ȧ_α = 2a_α(s_α − a_α), which is
  separable. From small random weights the SI says off-diagonal terms
  "decay to zero" and the decoupled solution is a "good approximation", and
  supports this by simulation (red lines, Fig. 3C), not by proof. It states
  that the solution does not describe learning that starts with
  substantial prior knowledge.
- **Data models.** Hierarchy: binary features diffusing down a regular tree
  of depth D with flip probability ε per branch, and many features
  (N₃ → ∞). Coherence: one planted block, entries Bernoulli(p) inside and
  Bernoulli(q) outside, with N_o, N_f → ∞, N_o/N_f = c ∈ (0, 1] and
  K_oK_f of order √(N_oN_f). Structural forms: Gaussian Markov random
  fields f ∼ N(0, (L + I/σ²)⁻¹) on a graph, restricted to item nodes, again
  with many features.
- **Inductive projection** adds one new unit and trains only its weights,
  to a fixed point, with the rest of the network frozen.
- **Representational similarity** results compare minimum-Frobenius-norm
  implementations of the same map, with white probe inputs.

## Key results

- **Eq. 6, deep dynamics.** a_α(t) = s_α e^{2s_αt/τ} / (e^{2s_αt/τ} − 1 +
  s_α/a_α⁰), and W₂W₁ = U A(t) Vᵀ. *Holds when:* decoupled, balanced start
  and Σx = I. Exact under those conditions.
- **Eq. 7–8, hidden layer.** W₁ = Q√A Vᵀ, W₂ = U√A Q⁻¹ for any invertible
  Q. From small weights Q ≈ R orthogonal, and h_iα(t) = √a_α(t) v_iα up to
  that rotation.
- **Eq. 9, shallow dynamics.** b_α(t) = s_α(1 − e^{−t/τ}) + b_α⁰e^{−t/τ}.
- **Eqs. 10–11, timing.** From a(0) = ε to within ε of s, the deep network
  takes t ≈ (τ/s) ln(s/ε), and the shallow one t ≈ τ ln(s/ε). With a
  separate cutoff ε₀ for the start, t_trans/t_tot → 0 as ε₀ → 0 for the
  deep network and → 1 for the shallow one. Hence the stages.
- **SSE(t)** = (P/2)Tr Σʸ − (P/2)Tr[(2S − A(t))A(t)], from Tr Σʸ at the
  start to the linear residual Tr Σʸ − Tr S² at the end.
- **Hierarchical spectrum (SI).** With q_k the feature overlap of two items
  whose last common ancestor is at level k, every eigenvector of the item
  similarity matrix is a level-l function, constant below each level-l node
  and summing to zero over the children of a level-(l − 1) node. Its
  eigenvalue is λ_l = P Σ_{k ≥ l} Δ_k/M_k with Δ_k = q_k − q_{k−1},
  decreasing in l, with degeneracy M_{l−1}(B_{l−1} − 1). So structure below
  level l cannot appear before level l − 1 is learned. To leading order in
  large branching, τ_l ∝ √(M_l/Δ_l), which grows exponentially with depth
  for constant branching.
- **Illusory correlations.** For successive modes with s_{k+1} = s_k − Δ
  and opposite-signed contributions to one feature of one item, the
  reversal lasts about (τΔ/s_k²) ln(s_k/ε), of order Δ, for ε ≪ Δ ≪ s_k.
  Total error never rises. The shallow prediction c₁ − (c₁ − c₂)e^{−t/τ} is
  monotone, so a shallow network never shows one.
- **Eqs. 12–14, typicality and prototypes.** With Σyx = O/P,
  v_iα = (1/(Ps_α)) Σ_m u_mα o_mi and u_mα = (1/(Ps_α)) Σ_i v_iα o_mi. The
  mode-α contribution to the output, u_mα s_α v_iα, grows with |v_iα|, so
  more typical items get larger responses.
- **Eq. 15, coherence threshold.** After centring and rescaling, the data
  matrix is noise plus a rank-one signal of size θ =
  (p − q)√(K_fK_o)/√(N_f q(1 − q)). The learned analyzers overlap the true
  category only if θ > c^{1/4} (Benaych-Georges and Nadakuditi, Thm 2.9),
  i.e. C = SNR·K_oK_f/√(N_oN_f) > 1, with SNR = (p − q)²/(q(1 − q)), and the
  overlaps have closed forms in C and c (Eqs. S25–S26). Simulations fall on
  the curves (Fig. 7E–F).
- **Basic level.** The eigenvalue for a category C at level k is
  Σ_{j∈C} Σʸ_ij − Σ_{j∈S(C)} Σʸ_ij for any member i and any sibling category
  S(C): within-category similarity minus similarity to a sibling.
  Anticorrelation between sibling categories at one level raises that
  level's singular values above the superordinate's (Fig. 8).
- **Global optimality (SI).** Truncating to k modes is the best rank-k
  linear predictor (Eckart–Young–Mirsky, re-proved by Weyl's inequality).
  So a network stopped early holds the best available summary for its
  stage.
- **Structural forms (SI).** For a GMRF the object analyzers are the
  eigenvectors of the item covariance (L + I/σ²)⁻¹ restricted to items, and
  s_α = √N₃ / (P√ζ_α), with ζ_α the eigenvalues of the precision matrix
  Φ (inversion keeps the eigenvectors). Clusters
  give block-constant analyzers, and the shared mode always beats the
  item-specific ones (s₁ > s₂, shown by a boundary analysis). Trees give
  ultrametric covariance diagonalised by tree wavelets. Rings give
  circulant covariance diagonalised by Fourier modes, with the singular
  value the Fourier coefficient's magnitude, broad scales first when
  correlation falls with distance. Grids are called Toeplitz, and only
  asymptotically Fourier. Transitive orderings give a staircase.
  Cross-cutting features add dimensions spanning branches.
- **Eqs. 16–17, inductive projection.** A new feature m taught for item i
  generalises to item j as h_jᵀh_i/‖h_i‖². A new item given feature m gets
  feature n as h_nᵀh_m/‖h_m‖², with h_nα = u_nα√a_α(t). Both are similarity
  in one hidden space, which differentiates over development (Fig. 10E).
- **Minimum norm (SI, proved).** min ‖W₁‖²_F + ‖W₂‖²_F subject to W₂W₁ =
  USVᵀ is attained exactly at W₁ = R√S Vᵀ, W₂ = U√S Rᵀ, R orthogonal, by a
  Lagrangian argument. So minimum-norm networks share HᵀH = XᵀVAVᵀX, and
  networks with non-orthogonal Q do not. With white probes, behavioural
  similarity is YᵀY = XᵀVA²VᵀX = (HᵀH)².

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | From decoupled, balanced starts, a two-layer linear network learns each SVD mode of Σyx by a sigmoid at time ≈ (τ/s)ln(s/ε), while a shallow network learns all modes on the timescale τ ln(s/ε) | strong (exact solution) | Eqs. 6, 9–11; SI derivation |
| C2 | The same ordering and sharpness hold from small random initial weights | moderate (simulation) | Fig. 3C; SI's statement that couplings decay, not proved |
| C3 | Data generated by diffusion on a tree have item-similarity eigenvectors that respect the tree, with eigenvalues falling with depth, so broad distinctions are learned first | strong (derivation) | SI hierarchical spectrum |
| C4 | Deep but not shallow networks show transient, non-monotone predictions for individual item–feature pairs, lasting O(Δ) | strong (derivation) | SI illusory-correlation section |
| C5 | Typicality and prototype, defined from the SVD, determine each other and order response magnitude | strong (identity) | Eqs. 12–14 |
| C6 | A planted category is recoverable only above coherence C = 1 | strong (theorem cited), in the stated high-dimensional limit | Eqs. S20–S26, Benaych-Georges and Nadakuditi |
| C7 | Between-category anticorrelation can make an intermediate level the most coherent | moderate (formula and constructed examples) | Eq. S30, Fig. 8 |
| C8 | Ring-structured data give Fourier analyzers learned from low to high frequency | strong (circulant algebra) | SI, rings and grids |
| C9 | Generalisation of a newly taught fact narrows with development | moderate (derived under a frozen-network fast-learning model, shown for a tree) | Eqs. 16–17, Fig. 10E |
| C10 | Minimum-norm implementations of a map have identical hidden similarity matrices, and behavioural similarity is its square | strong (proof) | SI minimum-norm section |
| C11 | Conserved neural similarity across people and species "suggests" near-optimal, minimum-norm learning in brains | weak (speculation, flagged by the authors) | Discussion of Fig. 11 |
| C12 | Deep linear networks capture the learning dynamics of their nonlinear counterparts | weak (one visual comparison) | Fig. 2 |

## Method

Average the online updates over an epoch, pass to continuous time, rotate
into the SVD basis of Σyx and assume the rotated weights diagonal. Each
mode is then a two-variable system, (c, d), whose product obeys a logistic
equation. Integrate it, and invert the change of variables. Everything
downstream comes from computing (s_α, u_α, v_α) for a data model and
substituting into the solution. For the hierarchy that is the block
structure of an ultrametric matrix, for the planted category a
spiked-random-matrix theorem, and for the structural forms the spectra of
graph covariances.

## Concepts

- **object analyzer** v_α: a right singular vector of Σyx, a function on
  items; its entries place items on semantic dimension α.
- **feature synthesizer** u_α: a left singular vector, a function on
  features; the paper's category prototype.
- **effective singular value** a_α(t): the strength with which the network
  currently expresses mode α.
- **typicality** of item i for distinction α: v_iα.
- **category coherence**: for a planted category, C =
  SNR·K_oK_f/√(N_oN_f); in general, the singular value of the category's
  mode.
- **illusory correlation**: a transient wrong prediction for an
  item–feature pair, between two stages.
- **tabula rasa**: small, decoupled, balanced initial weights, the
  condition the solution assumes.
- **optimal learning**: implementing the map with minimum total Frobenius
  norm.

## Connections

The dynamics are the authors' own (Saxe, McClelland and Ganguli 2014, ICLR,
arXiv 1312.6120), which this paper restates but does not cite. Its
reference lists in PMC (48 entries) and the arXiv SI (14) do not include
it. The error surface without spurious minima is Baldi and Hornik (1989).
The phenomena and the animals-and-plants dataset are Rogers and
McClelland's *Semantic Cognition* (2004). The structural forms, and the
GMRF construction of features from a graph, are Kemp and Tenenbaum's
(2008), here learned without a prior over forms. The coherence threshold
is the BBP transition (Baik, Ben Arous and Péché) in Benaych-Georges and
Nadakuditi's form. Tree wavelets are Khrennikov and Kozyrev's and
Murtagh's; circulant diagonalisation is from Gray.

Later work in this record uses the dynamics. [LIT-855](../literature.d/LIT-855.md) (Karkada et al. 2025)
shows a quadratic word2vec proxy following the same per-mode sigmoids on
the eigenvectors of a co-occurrence matrix. [LIT-859](../literature.d/LIT-859.md) (Mainali and Teixeira)
gets the same staged learning in a linear-attention layer from the product
of its two weight blocks, without depth. [LIT-860](../literature.d/LIT-860.md) (Karkada et al. 2026)
names this paper's ring result as its nearest precedent and generalises it
to word embeddings of translation-symmetric co-occurrence.

## Bearing on the record

- **It produces [THEORY-186](../theory.d/THEORY-186.md).** That is the deep linear result: stage-like,
  strength-ordered mode learning comes from the multiplicative
  parametrisation plus the data's singular spectrum, and a shallow network
  lacks it. [NOTE-658](NOTE-658.md) recorded that the record held this pattern as no one's
  source. Its scope is the decoupled, balanced, white-input case.
- **[THEORY-182](../theory.d/THEORY-182.md).** Its "one at a time, in order of eigenvalue" is this
  dynamics, applied to a symmetric factorisation. Consistent. This paper
  does not supply the random-initialisation proof that [THEORY-182](../theory.d/THEORY-182.md)'s
  promote_when asks for; it has the same gap, filled by simulation.
- **[THEORY-183](../theory.d/THEORY-183.md)** and **[THEORY-019](../theory.d/THEORY-019.md).** The ring result is the precedent for
  [THEORY-183](../theory.d/THEORY-183.md)'s Fourier geometry: circulant covariance gives Fourier
  analyzers, learned from low frequency up. My addition, not the paper's:
  over the reals the cos and sin modes of one frequency share a singular
  value, so they are learned at the same moment and appear together as a
  circle in the hidden layer. That is [THEORY-019](../theory.d/THEORY-019.md)'s forced pairing at work.
  The paper calls grids Toeplitz and only asymptotically Fourier. [LIT-860](../literature.d/LIT-860.md)'s
  open-boundary solution is the exact version of that case.
- **[THEORY-004](../theory.d/THEORY-004.md)** and **[THEORY-002](../theory.d/THEORY-002.md).** The minimum-norm result is a concrete
  case of a representation fixed by its kernel up to an orthogonal map.
  Gradient descent from small weights selects W₁ = R√A Vᵀ, so the hidden
  kernel is the same across networks and only R differs. Large
  initialisation breaks it (Q not orthogonal), so a shared kernel across
  learners is a property of the solution selected, not of the task. That
  sharpens [THEORY-002](../theory.d/THEORY-002.md)'s point that convergence of representations is
  convergence of kernels, and says when it should be expected.
- **[THEORY-039](../theory.d/THEORY-039.md).** It adds a derived kind of phase: plateaus and sharp
  transitions per mode, whose transition-to-total time ratio goes to zero
  with the initial scale. It concerns the transitions themselves, not what
  follows them.
- **[THEORY-086](../theory.d/THEORY-086.md).** It is the contrast case. In the kernel regime, fitting
  goes eigenspace by eigenspace at exponential rates, which is this paper's
  shallow network. Sigmoidal stages need the weights to move
  multiplicatively.
- No instruction for machine-learning practice. The subject is training
  dynamics, which is why the LIT carries `anthology-candidate`.

## Limitations

- **Exactness is conditional.** The closed form needs decoupled, balanced
  initial weights and Σx = I. The random-initialisation case is simulated
  on small hand-built datasets, and the main text's "exact solutions" and
  "mathematical proof" of progressive differentiation hold only
  under those conditions.
- **Linear networks only.** The authors list context dependence, dementia,
  causal structure and role binding as beyond them. The link to nonlinear
  networks is one MDS figure.
- **Data models are idealised.** Regular trees, many independent features,
  one planted block in a high-dimensional limit. Typicality results are
  stated for binary trees only.
- **Cognitive and neural fit is qualitative.** No child or cortical data are
  fitted. The behaviour-equals-neural-similarity-squared relation is said
  to be untested, and the inference to "optimal learning in the brain" is
  marked speculative.
- **Inductive projection** assumes a fast learner that freezes everything
  but the new weights, a modelling choice taken from Rogers and McClelland.
- **The published SI was not read.** Its deeper-network and
  correlated-input sections, mentioned in the main text, are known here only
  from that mention.

## Open questions

- A proof that, from small random and unbalanced weights, the trajectory
  converges to the decoupled one as the initial scale goes to zero, with a
  rate. The silent-alignment analyses [LIT-855](../literature.d/LIT-855.md) cites (Atanasov, Bordelon and
  Pehlevan 2022) are where that is claimed, and the record holds none of
  them.
- Whether nonlinear networks trained on the same structured data keep the
  strength-ordered schedule, and when they depart from it.
- Whether people's behavioural and neural similarity matrices stand in the
  squared relation the minimum-norm solution predicts.
- How degenerate modes, such as the cos/sin pairs of a ring, behave from
  random initialisation: whether the hidden circle forms at once or one
  axis leads.
