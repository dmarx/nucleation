---
status: Read
paper: 'LIT-tmp06otw'
title: 'Symmetry in Language Statistics and Representation Geometry'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:2602.15029v3, 29 June 2026,
    the ICML 2026 camera-ready, 36 pages), as text extracted with pdftotext;
    figures read from their captions, extracted labels and the text, since
    their plots do not survive extraction. Sections 1–5, Limitations, and
    Appendices A (experimental details), B (the review of word-embedding
    factorisation, the asymmetric extension, Assumption B.1 and the relation
    to PMI), C (additional evidence and the helper-word reconstruction), D
    (the combined seasonal and binary-attribute model, Theorem 5) and E (the
    proofs of Proposition 1, Corollary 2, Proposition 3 and Proposition 4,
    followed step by step) read. The reference list consulted for the works
    cited. v1 and v2 compared by abstract only. The code repository was not
    inspected.
date: '2026-10-09'
summary: >-
  Proves that if co-occurrence among words on a latent continuum depends
  only on their separation, a full-rank spectral word embedding places
  them on Fourier modes of the latent coordinate, with amplitudes from the
  kernel's Fourier transform, and solves the exponential kernel exactly for
  periodic and open boundaries. The symmetry is measured in Wikipedia, the
  geometry seen in Gemma 2 by PCA, and its robustness to deleting the
  words' mutual co-occurrences explained by a latent variable shared by
  many words.
---
<!-- inactive-ok-file: THEORY-tmp1cak6 THEORY-182 THEORY-022 THEORY-019 THEORY-002 — Proposed; cited as what this reading produced or bears on -->

# NOTE-tmprkfaf: Symmetry in Language Statistics and Representation Geometry

## Contribution

Circles for months and weekdays, rippled curves for years and number
lines, and linearly decodable coordinates for places had each been found in
language models (Engels et al., [LIT-322](../literature.d/LIT-322.md); Gurnee and Tegmark; Gurnee et al.)
without an account of why. This paper derives all three from one property
of the training data, translation symmetry of pairwise co-occurrence, in
the one model where the map from statistics to representation is known in
closed form: the spectral word embedding of [LIT-855](../literature.d/LIT-855.md). It gives the full
parametric curve, including the open-boundary case, and a decoding bound.
It also explains a robustness that would otherwise be puzzling: the
geometry of the months survives deleting the months' co-occurrences with
each other, because many other words carry the same latent variable.

## Key insight

A shift-invariant kernel is diagonalised by Fourier modes. If the words of
a concept are points on a line, circle or plane, and how often two of them
co-occur depends only on how far apart they are, then the block of the
co-occurrence matrix that an embedding factorises commutes with the
translations, its eigenvectors are sinusoids of position, and so the
embedding's principal components are those sinusoids. The longest
wavelengths carry the most variance, which is why the top two components
draw a circle or a horseshoe and the third adds the ripple. The shape is a
property of the statistics; the embedding only reads it off.

## Assumptions

- **Embedding model**: W Wᵀ factorises M* (or |M*|) exactly. The symmetric
  case is [LIT-855](../literature.d/LIT-855.md)'s tied quartic proxy for word2vec. The asymmetric case
  (Appendix B.2) uses separate word and context matrices initialised with
  W′(0) = QW(0), Q orthogonal, so the conserved quantity
  WᵀW − W′ᵀW′ is zero and both share right singular vectors; gradient flow
  is assumed to reach the Eckart–Young optimum. Then W W ⊤ = |M*|.
- **No compression**: d ≥ rank M* in Propositions 1–3 and Corollary 2, so
  the Gram matrix restricted to S is exactly the S-block of |M*|. Moderate
  d is treated only in §4.
- **Translation symmetry (Assumption 3.1)**: P_ij = P_iP_j C̃(dist(x_i, x_j))
  for i, j ∈ S, hence M*_ij = C(dist(x_i, x_j)), and M* positive
  semidefinite. Assumption B.1 (used for Proposition 1 and Corollary 2 in
  the appendix) instead asks M⁺ and M⁻ each to be translation invariant.
  Proposition 3 is proved under 3.1.
- **Lattice**: the words are equally spaced, L per axis, coordinates in
  [−1, 1]^D. Periodic boundary for Proposition 1 and Corollary 2; open
  boundary, D = 1, and the continuum limit L → ∞ for Proposition 3.
- **Kernel**: arbitrary for Proposition 1; exponential, e^(−|Δx|/σ) (or its
  periodisation), for Corollary 2 and Proposition 3.
- **Proposition 4**: periodic lattice, eigenvalues non-increasing in |k|
  ("eigenmode monotonicity"), r at a spectral gap, L odd.
- **§4.1**: words' seasonal centres t_i equispaced; P(i | t) =
  P(i)(1 + g(t − t_i)) with g symmetric, zero-mean, unimodal;
  conditional independence of two words given t; N → ∞.
- **The "word embeddings" in the experiments** are not trained: they are
  computed by diagonalising Wikipedia's M* (V = 25,000, 2.72 billion
  tokens, window 16 with linear down-weighting) and applying Equation (2).

## Key results

- **Proposition 1** (proved). Under B.1 on a periodic lattice of any
  dimension D, with d ≥ rank M*, up to orthogonal transformations within
  degenerate subspaces and permutations of the principal directions, the
  PCA coordinates are √(2|m̃(k_μ)|/|S|) sin(k_μᵀx_i) and
  √(2|m̃(k_μ)|/|S|) cos(k_μᵀx_i) in pairs, plus Nyquist modes with
  normalisation 1/|S|, where m̃ is the discrete Fourier transform of the
  kernel and k = πn. Proof: plane-wave ansatz for a block-circulant matrix;
  evenness of the kernel gives m̃(k) = m̃(⊖k) and the degenerate pairs;
  centring removes only the constant mode.
- **Corollary 2** (proved). Periodised exponential kernel, D = 1:
  amplitudes a_μ = √((2/L)(1 − q²)/(1 − 2q cos(2k_μ/L) + q²)),
  q = e^(−2/(σL)), tending to √(2σ/(1 + σ²k²)) with k_n = πn. A closed
  loop with integer frequencies.
- **Proposition 3** (proved, continuum limit). Open boundary, exponential
  kernel: the kernel is the Green's function of (1 − σ²∂²)/(2σ) with Robin
  boundary conditions u′(±1) = ∓u(±1)/σ; eigenfunctions are sin(kx) (odd,
  tan k = −σk) and, after centring, cos(kx) − sin k / k (even,
  tan k = k/(1 + σ(1 + σ)k²)); eigenvalue 2σ/(1 + σ²k²) in both sectors;
  k_μ < k_{μ+1}. Centring changes the even wavenumbers but not the
  eigenvalue formula. An open curve with non-integer frequencies.
- **Proposition 4** (proved). On a periodic lattice with monotone
  eigenvalues, the OLS rank-r probe returns the projection of the
  coordinates onto the r slowest Fourier modes, and
  min ε² ≤ (6/π²)(L²/(L² − 1))((r/Vol_D)^(1/D) − √D/2)⁻¹: about 1/r for
  D = 1 and 1/√r for D = 2. Proof: the overlaps with x_ℓ vanish unless the
  wavevector is axis-aligned, so the problem splits into D one-dimensional
  sums, evaluated by Gradshteyn–Ryzhik 1.352.1 and bounded by an integral.
- **Theorem 5** (proved, Appendix D). With PMI = K_t ⊗ J + J ⊗ K_attr + A J ⊗ J
  for a seasonal kernel and Korchinski et al.'s multiplicative binary
  attributes, the eigenvectors are products of Fourier modes and Walsh
  characters, and the seasonal and attribute subspaces are orthogonal;
  attributes contribute eigenvalue N2^dβ_r on (k = 0, S = {r}). The
  seasonal factor's logarithm is taken as given, so the decomposition is
  exact only "up to seasonal linearization".
- **§4.1** (argued). Under the seasonal latent model, PMI(i, j) =
  log(1 + K̃(t_i − t_j)) is circulant, its eigenvalues μ_k grow like N
  times the kernel's Fourier coefficients, and a perturbation of a fixed
  number of entries (the month pairs; the paper says "122", where
  12 × 12 = 144) is small against gaps of order N, so the top-d
  eigenvectors are stable. The appeal to Weyl and
  Davis–Kahan is one sentence; no bound is stated.
- **Measurements.** Month and year blocks of Wikipedia's M* (and of |M*|,
  M⁺, M⁻) look circulant and Toeplitz and fit an exponential kernel off
  the diagonal (Figures 5–6; the year fit needs a constant shift). The
  spectrum of M* is roughly symmetric about zero, rank M⁺ ≈ rank M⁻
  (Figure 7), so Assumption 3.1's PSD clause fails and absolute amplitudes
  are mispredicted. Predicted Lissajous curves match the year embeddings,
  with kinks at the world wars (Figure 2, Figure 11); 365 calendar dates
  (Figure 9). Decoding years 1900–2020: train and test error over 100
  splits of 60/60, error falling with r and a double-descent peak at r = 60
  (Figure 2, Figure 13 with ridge).
- **Robustness experiments.** Setting the month block of M* to zero
  (P_ij = P_iP_j), the d = 1000 embedding still orders the months on a
  circle and its Gram matrix approximates the deleted block (Figure 4,
  left). Factorising only months plus ten seasonal words, with the month
  block still zero, recovers the order; seventeen number words do not
  (Figures 4 right, 15, 16). Procrustes error falls as about 1/√H with H
  helper words, faster for seasonal than random helpers (Figure 17).
- **Language models.** Gemma 2 2B, residual stream after each block,
  last token of "The month of the year is x", "In the year x", "The
  location of the US state x"; EmbeddingGemma (308M, 768-d) for states.
  PCA plots and Gram matrices resemble the predictions (Figures 1, 3, 12).
  The first Gemma mode for states is dropped as a tokenisation artefact;
  digit tokenisation puts bright off-diagonals in the year Gram matrix.
  Context removes the distortion of "May" across layers (Figure 14).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | If the S-block of the factorised matrix is translation invariant on a periodic lattice and d ≥ rank M*, the embeddings' principal components are Fourier modes of the latent coordinate in degenerate cos/sin pairs, with amplitudes √\|m̃(k)\| | strong (proof) | Proposition 1, Appendix E.2 |
| C2 | For the exponential kernel the geometry is solved exactly: integer frequencies and a closed loop for periodic boundary, non-integer frequencies fixed by transcendental conditions and an open curve for open boundary, amplitudes √(2σ/(1 + σ²k²)) | strong (proof) | Corollary 2, Proposition 3, Appendices E.3–E.4 |
| C3 | Under monotone eigenvalues the best rank-r linear probe has relative error O(r^(−1/D)) | strong (proof) for the periodic lattice; moderate as applied to years, which have open boundary | Proposition 4, Appendix E.5; Figure 2 |
| C4 | In Wikipedia the month and year co-occurrence statistics are approximately translation symmetric with an exponential kernel | moderate | Figures 5–6, one corpus, one window scheme; diagonal excluded from the fit |
| C5 | The predicted curves match spectral word embeddings in relative amplitude and frequency, not in absolute scale | moderate | Figures 1, 2, 9, 11; Appendix B.3 explains the scale miss by the indefinite M* |
| C6 | The month circle survives removing all month–month co-occurrences at moderate d, and is carried by seasonal words, not arbitrary ones | moderate | Figures 4, 15–17 |
| C7 | A latent variable modulating many words makes the relevant eigenvalues grow with vocabulary, so the geometry is stable under bounded perturbation | weak | §4.1, a perturbation argument stated in one sentence |
| C8 | The same mechanism shapes the geometry in large language models and text embedders | weak | qualitative PCA of Gemma 2 2B and EmbeddingGemma, one prompt template each; no intervention on the statistics |

## Method

Two moves. First, reduce representation geometry to linear algebra on the
data: if the embedding's Gram matrix equals (the absolute value of) a
co-occurrence matrix, its PCA is that matrix's eigendecomposition. Second,
diagonalise that matrix analytically by symmetry: circulant blocks by the
discrete Fourier transform; the open-boundary exponential kernel by
recognising it as the Green's function of a second-order operator, turning
the integral eigenproblem into a Helmholtz equation with Robin boundary
conditions, and handling mean-centring as a constant inhomogeneity. The
robustness result moves from a fixed word set to a vocabulary-wide latent
variable, where the same Fourier structure appears with eigenvalues that
scale with vocabulary size.

## Concepts

- **semantic continuum / latent semantic lattice**: the latent coordinate
  x_i ∈ [−1, 1]^D of the words of a concept (time of year, historical
  year, geographic position), equally spaced on a lattice for the
  theorems; "periodic" or "open" boundary conditions.
- **co-occurrence kernel C**: the function of separation that M*_S is
  assumed to be; C = f ∘ C̃ with f(y) = 2(y − 1)/(y + 1).
- **"co-occurrence statistics"**: the paper's shorthand for M*, not the
  raw P_ij (footnote 1).
- **translation symmetry**: dependence of co-occurrence on separation only;
  for words, not tokens or contexts.
- **eigenmode monotonicity**: amplitudes decreasing with wavenumber, so
  the top principal components are the slowest modes.
- **collective effect**: geometry carried by the many words that share a
  latent variable, not by the concept's own words.
- **helper (bath) words**: the extra words used to reconstruct the month
  geometry with the month block zeroed.

## Connections

It is the sequel of [LIT-855](../literature.d/LIT-855.md) (Karkada, Simon, Bahri and DeWeese), whose
result that a word embedding factorises M* ([THEORY-182](../theory.d/THEORY-182.md)) is the premise of
every theorem here. It cites that paper for more than it proved: that
"word2vec … learn[s] to represent the top eigenmodes" of M* is [LIT-855](../literature.d/LIT-855.md)'s
result for a tied quartic proxy, and the untied case here rests on a
special initialisation that word2vec does not use. It extends Korchinski et
al. (2025, NeurIPS; not held), who derived parallelogram analogies from
Kronecker structure in M* for binary latent attributes, to continuous
attributes, and Appendix D combines the two. The latent-variable model of
§4.1 is close to Arora et al.'s latent-variable account of PMI embeddings
([ANTH-LIT-613](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-613.md)), which it does not cite. The circles it
explains are those of Engels et al. ([LIT-322](../literature.d/LIT-322.md), read in [NOTE-273](NOTE-273.md)), which
[THEORY-022](../theory.d/THEORY-022.md) reads as real two-dimensional irreducibles of ℤ/12 and ℤ/7; the
degenerate cos/sin pairs of Proposition 1 are an instance of [THEORY-019](../theory.d/THEORY-019.md).
Saxe, McClelland and Ganguli's circular hidden representations of a
periodic lattice are its nearest precedent; Park et al.'s in-context grid
representations get a hypothesis but no test (Figure 10).

## Bearing on the record

- **It produces [THEORY-tmp1cak6](../theory.d/THEORY-tmp1cak6.md)**: under translation-symmetric
  co-occurrence, a spectral word embedding's geometry is the Fourier
  geometry of the latent continuum, so the symmetry is supplied by the
  data. Nothing in the record held this.
- **[THEORY-022](../theory.d/THEORY-022.md)**: its last clause, "in both the group comes from the task,
  not the network", gains a mechanism for the language-model half. The
  cyclic group whose characters the month circle carries is a symmetry of
  the corpus statistics, and a model that factorises those statistics
  inherits it. The paper does not test whether Llama's or Mistral's circles
  arise this way, so it supports the clause for word embeddings and only
  suggests it for LLMs. It also predicts Engels et al.'s second harmonic in
  the months: the frequency-2 pair is the next Fourier mode, with smaller
  amplitude, and is what gives the "Pringle" saddle (Figure 8).
- **[THEORY-019](../theory.d/THEORY-019.md)**: Proposition 1 is its forward direction on a concrete
  case: the circulant block commutes with ℤ/L, so its eigenspaces are the
  real two-dimensional irreducibles and the spectrum comes in pairs; and,
  as [THEORY-019](../theory.d/THEORY-019.md) says, the basis inside a pair is not fixed (the theorems
  hold "up to orthogonal transformations within degenerate subspaces").
  The open-boundary case shows what happens when the symmetry is broken by
  edges: the degeneracy lifts and the even modes shift.
- **[THEORY-182](../theory.d/THEORY-182.md)**: this paper assumes its conclusion and extends it to
  untied weights only under a conservation-law initialisation. The
  experiments factorise M* directly and train nothing, so they add no
  evidence for [THEORY-182](../theory.d/THEORY-182.md)'s promote_when, which asks for untied weights
  with word2vec's own negative sampling.
- **[THEORY-002](../theory.d/THEORY-002.md)**: the paper's claim that geometry is "largely governed by
  task-agnostic and architecture-agnostic principles" is the kernel-
  convergence reading [THEORY-002](../theory.d/THEORY-002.md) sets out: what it predicts is the Gram
  matrix, fixed up to orthogonal maps within degenerate subspaces.
- **[THEORY-159](../theory.d/THEORY-159.md) and the manuscript's [CLAIM-082](../claims.d/CLAIM-082.md)** (noted for the
  coordinator; no claim edited): Figure 4 is a model case of position fixed
  by relations to coexisting terms, since the months are placed correctly
  from their co-occurrence with other words when their co-occurrences with
  each other are deleted. But the relations are organised by an
  extralinguistic variable (the time of year), and the learned geometry is
  isomorphic to it. It therefore does not set relation against reference.
- **ML practice**: none. The paper gives no instruction. It describes what
  a class of models comes to contain.

## Limitations

- The theorems are about an idealised spectral embedding at full rank,
  d ≥ rank M*, not about a trained network at the dimension used. The
  experimental "word embeddings" are computed from M* by Equation (2).
- Assumption 3.1 includes positive semidefiniteness, which Wikipedia's M*
  violates badly (rank M⁺ ≈ rank M⁻). B.1 relaxes it, but then the kernel
  must be estimated from |M*|, a global spectral transform, and the figures
  use the 3.1 fit instead. Relative, not absolute, amplitudes are matched.
- The open-boundary result is a continuum limit, and Proposition 4 is
  proved on a periodic lattice. It is applied to years, which have an open
  boundary.
- The robustness theory (§4.1) assumes equispaced seasonal centres and
  conditional independence given the season, and its perturbation step is
  asserted, not proved. The abstract's "We prove that this robustness
  emerges" overstates it.
- The language-model evidence is PCA of one layer or one embedding model
  with one prompt template per concept, judged by eye. There is no
  quantitative fit, no control concept, and no intervention that changes
  the statistics and watches the geometry move.
- Translation symmetry is measured for months and years. For states it is
  modelled with a hand-chosen kernel 10 exp(−d/20) "chosen by visual
  inspection".
- The authors' own limitation is that the theory is for word embeddings,
  while LLMs adapt to context.

## Open questions

- Does a trained word2vec at moderate d, with untied weights and its own
  negative sampling, show the same Fourier geometry? Is it the same when
  the corpus is edited to break the symmetry, for example by making some
  month pairs co-occur unusually often? An intervention on the data that
  moves the geometry as predicted would make the account causal.
- Is there a rigorous version of §4.1, with eigengaps and perturbation norms
  stated, that gives the embedding dimension at which the geometry
  survives a given deletion?
- Do LLM circles track the corpus kernel quantitatively, for example in σ,
  harmonic amplitudes or the open-boundary wavenumbers, across models
  trained on different corpora?
- What does the theory say for hierarchical attributes (Park et al.), which
  the authors name as unexplained?
