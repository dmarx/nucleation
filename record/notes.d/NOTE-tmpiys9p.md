---
status: Read
paper: 'LIT-tmp2n2m4'
title: 'Closed-Form Training Dynamics in Word2Vec-like Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:2502.09863v3, 16 October
    2025, the NeurIPS 2025 camera-ready, 26 pages), as text extracted with
    pdftotext; figures read from their captions and the extracted labels.
    Sections 1–5 read; Appendices A (experimental details, the reweighting
    derivations of A.3, the analogy metric, the Marchenko–Pastur fit), B
    (additional figures, captions only), C (the proofs of Theorem 1,
    Proposition 2 and Lemma 3.1, followed step by step, and the derivation
    of Result 3, followed but not re-derived) and D (relations to PMI,
    SimCLR, next-token prediction and the NTK) read. The reference list
    read. v1 (14 February 2025, then titled "Solvable Dynamics of
    Self-Supervised Word Embeddings and the Emergence of Analogical
    Reasoning", trained on WikiText) was not read; only its abstract was
    compared. The code repository was not inspected.
date: '2026-10-09'
summary: >-
  Proves that word2vec's loss, approximated to fourth order and reweighted
  so that every pair carries the same aggregate weight, is unweighted
  factorisation of M*, the relative deviation of co-occurrence from
  independence, whose rank-d minimisers are its top eigenvectors; derives,
  without full rigour, that gradient flow from small random initialisation
  learns those eigenvectors one at a time in sigmoidal steps; and shows on
  Wikipedia that the predicted embeddings match word2vec's features and
  scores better than truncated PMI or PPMI. Its account of analogies is an
  empirical spiked-random-matrix fit.
---
<!-- inactive-ok-file: LIT-242 — Deferred; the stepwise SSL paper this one extends, cited for lineage -->
<!-- inactive-ok-file: THEORY-001 — Proposed; named for the bearing of this reading on its caveat -->
<!-- inactive-ok-file: THEORY-002 — Proposed; named for a bearing, not as settled -->
<!-- inactive-ok-file: THEORY-009 — Proposed; named for a bearing, not as settled -->
<!-- inactive-ok-file: LIT-208 — Proposed; named for a bearing on the distributional hypothesis -->
<!-- inactive-ok-file: THEORY-tmpw5yp5 — Proposed; the account this reading produced -->

# NOTE-tmpiys9p: Closed-Form Training Dynamics in Word2Vec-like Models

## Contribution

It was known that word2vec without a rank constraint factorises shifted PMI
(Levy and Goldberg 2014), but not which rank-d approximation it actually
reaches; truncated SVD of PMI is a poor answer (8.4% on Google analogies
against word2vec's 68.0%). This paper answers the question for a close
proxy. It replaces the logistic loss by its quartic Taylor expansion at the
origin and chooses reweighting hyperparameters under which the problem is
unweighted symmetric matrix factorisation of a bounded target M*. It then
solves the rank-constrained minimiser in closed form and the gradient-flow
trajectory from small initialisation (the latter by an approximate
derivation), so the learned features and the time at which each appears are
given by the eigendecomposition of a matrix built from corpus statistics
and hyperparameters alone.

## Key insight

From a small start, a contrastive word-embedding model is a greedy spectral
method. Whatever the random initial directions, the embedding first rotates
silently onto the eigenbasis of M* while its scale stays tiny, and then
acquires one eigendirection at a time, the largest first, each by a
sigmoidal jump in time about (1/λ_k) ln(λ_k/σ²). Stopping early or shrinking
d only cuts the list of features; it does not change them. The answer to
"which low-rank approximation" is therefore set by the optimisation path,
not by the unconstrained optimum, which is why factorising PMI and then
truncating gets it wrong.

## Assumptions

- **Tied weights**: the context matrix W′ is set equal to W. The authors
  name this as the main limitation.
- **Quartic approximation** of L_w2v around W = 0: log(1 + e^{∓x}) is
  replaced by its expansion to fourth order, giving loss terms
  Ψ⁺(−x + x²/4) on positive pairs and Ψ⁻(x + x²/4) on negative pairs, with
  x = w_iᵀw_j.
- **Setting 3.1**: Ψ⁺ and Ψ⁻ symmetric in (i, j), and
  G_ij = Ψ⁺_ij P_ij + Ψ⁻_ij P_i P_j = g constant. The worked instance is
  Ψ⁺ = Ψ⁻ = (P_ij + P_iP_j)⁻¹, so g = 1. word2vec's own negative
  distribution, P_j^{3/4} upweighted by k, is asymmetric and not covered.
- **Λ[:d,:d] positive semidefinite**: the top d eigenvalues of M* are
  non-negative. Empirically M* (V = 10,000) has 4,795 non-negative
  eigenvalues, so it holds for d ≪ V.
- **Full-batch gradient flow from vanishing initialisation**,
  W_ij(0) ∼ N(0, σ²), σ² → 0, for Result 3. The experiments use SGD with
  mini-batches and finite initialisation, and still match.
- **Distinct eigenvalues** λ_i ≠ λ_j, used in Result 3, and distinct
  singular values at initialisation (true with probability one), used in
  Lemma 3.1.
- **Under-parameterisation**, d ≪ V.

## Key results

- **Theorem 1** (proved). Under Setting 3.1,
  L(W) = (g/4)‖W Wᵀ − M*‖²_F + const, with
  M*_ij = (Ψ⁺_ij P_ij − Ψ⁻_ij P_iP_j) / (½(Ψ⁺_ij P_ij + Ψ⁻_ij P_iP_j)).
  If Λ[:d,:d] ⪰ 0, the global minima are REquiv(V*[:, :d] Λ[:d,:d]^{1/2}),
  the set of all W U with U orthogonal. Proof: complete the square, then
  Eckart–Young–Mirsky.
- **Proposition 2** (proved). Without Setting 3.1,
  L(W) = ¼ Σ_ij G_ij (W Wᵀ − M*)²_ij + const: the target is unchanged, only
  the weights change. If G = g gᵀ is rank one, with Γ = diag(g)^{1/2}, the
  minimiser is Γ⁻¹ (Γ M* Γ)_[d] Γ⁻¹. For general G it is weighted low-rank
  approximation, NP-hard (Gillis and Glineur 2011), and is left alone.
- **Lemma 3.1** (proved). If V(0) = V*[:, :d], the gradient flow
  dW/dt = −(1/2g)∇L keeps U and V fixed and each singular value follows
  s_k²(t) = s_k²(0) λ_k e^{λ_k t} / (λ_k + s_k²(0)(e^{λ_k t} − 1)),
  reaching λ_k at the characteristic time τ_k = (1/λ_k) ln(λ_k / s_k²(0)).
  These are Saxe, McClelland and Ganguli's (2014) dynamics.
- **Result 3** (derived, not proved). From W_ij(0) ∼ N(0, σ²), in rescaled
  time t̃ = t/τ₁ with τ₁ = λ₁⁻¹ ln(λ₁/σ²), the distance from the trajectory
  to the aligned trajectory of Lemma 3.1, minimised over right orthogonal
  transformations, goes to zero as σ² → 0, with high probability. The
  derivation writes U S Oᵀ = QR, keeps only the diagonal of R in the
  couplings, solves the off-diagonals exactly under that approximation and
  shows their maximum, about σ^{2(λ_i − λ_j)/λ_i} up to factors, vanishes
  with σ². The authors "conjecture that our argument can be made rigorous".
  It holds in practice when log σ² ≪ −(λ_iλ_j/(λ_i − λ_j)) log(λ_j/(λ_i − λ_j))
  for all pairs.
- **M* and PMI** (Appendix D.1). Writing P_ij/(P_iP_j) = 1 + 2x/(2 − x),
  x = M*_ij (equal reweightings), PMI = x + x³/12 + x⁵/80 + …, so M* is PMI
  to third order but confined to [−2, 2].
- **Benchmarks** (Figure 3b; V = 10,000, d = 200, 2.0 billion Wikipedia
  tokens). Google analogies: word2vec 68.0%, trained quadratic model 65.1%,
  svd(M*) 66.3%, svd(PPMI) 50.6%, svd(PMI) 8.4%. MEN: 0.744, 0.755, 0.755,
  0.740, 0.448. WordSim353: 0.698, 0.682, 0.683, 0.690, 0.221. Figure 5
  shows word2vec's eigen-features overlap the quadratic model's closely and
  PPMI's less.
- **Ablation** (Figure 7, a different 41-million-token corpus). The quartic
  approximation alone hardly changes word2vec's singular-value dynamics;
  Setting 3.1 alone produces the clean separation into steps; the quartic
  loss stops the late divergence of the weights that logistic losses show.
- **Task vectors** (Figure 4 and Appendix A.6, empirical). For each analogy
  class, the stacked difference vectors R_d (N ≈ 30 pairs) have a Gram
  spectrum fitted by a Marchenko–Pastur bulk plus one outlier; the outlier
  carries the mean task vector (ratio above 0.9 in every class); the fitted
  effective dimension d_eff is well below d. SNR = λ_max · rank / trace
  first rises and then falls as d grows, and its maximum orders the classes
  by analogy accuracy. Top-1 accuracy stays high at large d although the
  parallelogram degrades, because all embeddings spread apart (Figure 8).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Setting 3.1 the quartic word2vec objective is exactly unweighted symmetric factorisation of M*, and its rank-d minimisers are M*'s top-d eigenvectors scaled by √λ, up to rotation | strong (proof) | Theorem 1, Appendix C |
| C2 | Without constant G the target M* is unchanged and only the weights change; the minimiser is known only when G is rank one | strong (proof) | Proposition 2 |
| C3 | From aligned initialisation the eigen-directions are learned independently, each by a sigmoid with time τ_k = (1/λ_k) ln(λ_k/s_k²(0)) | strong (proof) | Lemma 3.1 |
| C4 | From vanishing random initialisation the trajectory converges to the aligned one up to rotation, so features are learned one at a time in order of eigenvalue | moderate | Result 3, an approximate derivation; Figure 2 |
| C5 | word2vec's learned features and benchmark scores are much closer to the quadratic model's, and to svd(M*), than to truncated PMI or PPMI | moderate | Figures 3 and 5, one corpus, V = 10,000, d = 200, k = 1 negatives |
| C6 | The stepwise structure comes from the reweighting (Setting 3.1), not from the quartic approximation | moderate | ablation, Figure 7, one smaller corpus |
| C7 | Analogy difference vectors within a class behave like a spiked random matrix whose spike is the mean difference, and spike SNR predicts analogy accuracy | weak | Figure 4 and Figure 6, manual Marchenko–Pastur fits, N ≈ 30 |
| C8 | Contrastive losses of the form E₊f⁺(wᵀw′) + E₋f⁻(wᵀw′) reduce in the same way to factorisation; SimCLR in a linearised regime should step | weak | Appendix D.2, a sketch |

## Method

Two moves carry the paper. First, approximate the loss rather than its
minimiser: expanding around the origin and completing the square turns the
contrastive objective into a squared distance between W Wᵀ and a fixed
target, and the hyperparameter condition makes that distance unweighted, so
Eckart–Young gives the answer. Second, solve the dynamics in the target's
eigenbasis: aligned initialisation decouples the modes into Saxe-type
sigmoids, and for random initialisation a QR reparameterisation of
U S Oᵀ shows the off-diagonal (misaligned) part grows more slowly than the
diagonal and dies away, so alignment happens first and silently.

## Concepts

- **QWEM (quadratic word embedding model)**: not a new architecture; the
  embeddings obtained by minimising the quartic approximation of the
  word2vec loss with tied weights.
- **M\***: the target matrix of relative deviations of the reweighted
  skip-gram distribution from the reweighted product of unigrams. Zero
  everywhere if words were independent.
- **Setting 3.1**: symmetric reweightings Ψ⁺, Ψ⁻ with constant aggregate
  weight G_ij = g.
- **REquiv(W)**: the right orthogonal equivalence class {W U : UᵀU = I};
  the loss depends on W only through W Wᵀ, so embeddings are determined
  only up to this class.
- **eigen-feature**: an eigenvector of M*, a direction in word space; the
  paper's "learned feature".
- **task vector**: the difference between the embeddings of a semantic pair,
  such as man − woman (after Ilharco et al. 2022).
- **SNR of a task family**: λ_max(G) · rank(G) / Tr G for the Gram matrix of
  its task vectors.

## Connections

It applies the deep-linear-network dynamics of Saxe, McClelland and Ganguli
(2014) and the silent-alignment idea of Atanasov, Bordelon and Pehlevan
(2022) to a self-supervised language task, and it sits in the
incremental-rank literature on matrix factorisation (Li, Luo and Lyu 2021;
Jacot et al. 2021), claiming to need neither over-parameterisation nor
special initialisation. Its closest relatives are the linearised
contrastive analyses of HaoChen et al. (2021) and Simon et al. (2023b), and
Appendix D.2 offers an explanation for the stepwise learning Simon et al.
observed under SimCLR. Its target is a bounded relative of the PMI matrix of
Church and Hanks (1990) and Levy and Goldberg (2014), and it answers the
question Arora et al. (2016) left open of which low-rank approximation
word2vec finds. Its analogy analysis borrows the spiked covariance model of
Baik, Ben Arous and Péché (2005). The authors set it against the NTK regime
(Appendix D.4): small initialisation, feature learning, saddle-to-saddle
dynamics.

## Bearing on the record

- **[LIT-242](../literature.d/LIT-242.md)** (Simon et al., *On the Stepwise Nature of Self-Supervised
  Learning*, Deferred). This is the same picture, stepwise acquisition of
  the eigenmodes of a contrastive kernel, carried to word co-occurrence, by
  one of its authors. The LIT records `extends: LIT-242`.
- **[THEORY-001](../theory.d/THEORY-001.md).** It states the shared unconstrained optimum of
  contrastive losses, the positive-pair density ratio, and says it is "not
  about what a network reaches". This paper is a worked case of exactly that
  gap: the unconstrained word2vec optimum is (shifted) PMI, and truncating
  it predicts word2vec badly (8.4% against 68.0% on analogies), while the
  rank-constrained path of an approximate loss predicts it well. It
  supports [THEORY-001](../theory.d/THEORY-001.md)'s caveat; it does not touch its theorem.
- **[THEORY-009](../theory.d/THEORY-009.md).** It holds that spectral SSL gets its self-adjointness from
  the symmetry of the pair distribution. Here too the eigendecomposition of
  M* exists because Ψ⁺ and Ψ⁻ are taken symmetric and the weights tied; the
  asymmetric case (word2vec's real negative sampling, untied W′) is exactly
  where the closed form stops. It is another symmetric example, so by
  [THEORY-009](../theory.d/THEORY-009.md)'s own promotion condition it cannot settle it.
- **[THEORY-002](../theory.d/THEORY-002.md).** The loss depends on W only through W Wᵀ, and the paper
  determines embeddings only up to right orthogonal transformation: an
  instance of a kernel fixing a representation only up to the symmetry of
  what is observed.
- **[THEORY-086](../theory.d/THEORY-086.md)** (the kernel regime fits the target eigenspace by
  eigenspace of the NTK). This paper is the small-initialisation
  counterpart: the eigen-by-eigen order survives, but the eigenbasis is the
  data's target M*, not a fixed kernel's, and the weights move.
- **[LIT-208](../literature.d/LIT-208.md)** and the distributional hypothesis. The paper is an exact
  instance of meaning-as-co-occurrence: the embedding geometry is a
  function of P_ij − P_iP_j and nothing else. That is a statement about a
  model, not about language; it does not decide the philosophical questions
  [LIT-208](../literature.d/LIT-208.md) raises.
- It produces [THEORY-tmpw5yp5](../theory.d/THEORY-tmpw5yp5.md), on what a rank-limited contrastive word
  embedding learns and in what order.
- It is a theory of an ML algorithm and would fit the anthology's
  representation-learning reading; the LIT carries `anthology-candidate`.
  It gives no practice instruction beyond the remark that factorising M*
  directly is fast.

## Limitations

- Tied weights only; untied encoder/decoder is not treated.
- Setting 3.1 excludes word2vec's own negative-sampling distribution, which
  is asymmetric; the match to real word2vec is empirical.
- Result 3 is a derivation with dropped terms, not a theorem.
- One main corpus and vocabulary size (Wikipedia, V = 10,000, d = 200), and
  SGNS run with k = 1 negatives "for fair comparison"; no comparison with
  GloVe and nothing at state-of-the-art scale, as the authors say.
- The analogy account is a visual fit of an asymptotic law at N ≈ 30, with
  the aspect ratio fitted by hand; the authors themselves find the fit
  surprising at that size.
- Top-1 analogy accuracy is shown to be a misleading measure of linear
  structure at large d (Figure 8), which weakens it as evidence either way.

## Open questions

- A rigorous version of Result 3: bounds on the discarded couplings in the
  QR dynamics.
- The general weighted case (G not rank one), and the asymmetric case of
  untied weights and word2vec's own negative distribution, where the natural
  object would be a singular value decomposition.
- Whether the spiked-random-matrix description of task vectors can be
  derived from M* rather than fitted, so that which analogies a model can
  complete, and when, becomes a prediction.
- The authors' conjecture (Appendix D.3) that next-token prediction needs a
  dynamical theory of learning sparse higher-order tensors.
