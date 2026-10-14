---
number: 751
status: Read
formerly:
- NOTE-tmpu7m7r
paper: LIT-258
title: 'Johnson, El Hanchi & Maddison — Contrastive Learning Can Find an Optimal Basis'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (arxiv.org/pdf/2210.01883, 39 pp.,
    14 February 2023, "Published as a conference paper at ICLR 2023"),
    text extracted with pdftotext -layout: §§1–7 and Appendices A–F line
    by line. That covers the Table 1 derivations (B.1–B.4), the proofs of
    Proposition 3.1, Theorem 3.2 and Proposition C.1 (C.1–C.4), the proofs
    of Theorem 4.1 and Proposition 4.2 (D.1–D.2), the estimation methods
    (E.1–E.2) and all experiment details and supplementary results
    (F.1–F.5). The figures were read from their captions and axis labels
    only, because their plotted values have no text layer. The references
    were not read.
date: '2026-10-14'
summary: >-
  On a finite augmentation space, the NT-Logistic and spectral losses are
  minimized over unconstrained kernels by K⁺ = p⁺/(p⊗p), and InfoNCE by
  K⁺ up to a factor constant on communicating classes. Kernel PCA under K⁺
  returns the eigenfunctions of the positive-pair Markov chain
  (h_i = λ_i^(1/2) f_i). The top-d eigenfunctions span the subspace that
  minimizes worst-case L²(p) approximation error over targets with
  E_p⁺[(g(a₁) − g(a₂))²] ≤ ε; that error is ε/(2(1 − λ_(d+1))).
---
<!-- inactive-ok-file: THEORY-001 THEORY-005 THEORY-007 THEORY-009 QUESTION-052 — Proposed or Open; the theories and question that cite this paper, open until it and its companions are read -->
<!-- inactive-ok-file: LIT-249 LIT-228 LIT-246 LIT-251 LIT-252 LIT-242 — Deferred or newly read; the companion papers of the spectral reading of self-supervised learning -->

# NOTE-751: Johnson, El Hanchi & Maddison — Contrastive Learning Can Find an Optimal Basis

## Contribution

The paper puts three contrastive losses into one framework. With the
exponential and the temperature counted as part of the model, NT-Xent,
NT-Logistic and the spectral loss all fit one positive-pair kernel K⁺. It
proves that kernel PCA under K⁺ is exactly the eigendecomposition of the
Markov chain that steps between positive pairs. It then proves that the top
eigenfunctions of that chain give the minimax-optimal d-dimensional linear
representation for targets that change little across positive pairs. The
experiments test how far learned kernels recover those eigenfunctions, on
two synthetic tasks where K⁺ is known.

## Key insight

Expand any function in the eigenfunctions of the positive-pair chain.
Its positive-pair discrepancy is then Σ(2 − 2λ_i)c_i², so view-invariance
is a weight on each coefficient. Functions that are nearly invariant must
put their mass on eigenfunctions with λ_i near 1. The same eigenfunctions,
scaled by λ_i^(1/2), are what kernel PCA under K⁺ returns. So a contrastive
model, which fits K⁺, followed by PCA gives the basis that is best for such
targets.

## Assumptions

- **Finite spaces.** Z and A are "finite but arbitrarily large, e.g. the
  set of 8-bit 32x32 images" (footnote 1). Every theorem is a matrix
  identity on R^A.
- **Full support.** D_Z and D_A are invertible (App. C.1).
- **Conditionally independent, identically drawn views.**
  p⁺(a₁,a₂) = Σ_z p(a₁|z)p(a₂|z)p(z). This makes P_(A,A) = P_(A←Z)D_Z P_(Z→A)
  a Gram matrix, so it is symmetric and positive semidefinite.
- **Assumption 1.1 (approximate view-invariance).**
  E_p⁺(a₁,a₂)[(g(a₁) − g(a₂))²] ≤ ε. Appendix A shows it holds with
  ε = 2E[(g(A) − Y)²] whenever Y ⊥ A | Z, that is, when the augmentations
  do not use the label.
- **Unconstrained minimization** for Table 1. "Minimum" is over all kernel
  functions, "not necessarily representable using the shown
  parameterization". For NT-Xent it is also over symmetric functions only,
  with negatives drawn i.i.d. from p(A).
- **Same p(A) at pretraining and downstream** (§7, for Theorem 4.1).
- **Scalar targets.** Vector targets are handled one coordinate at a time.

## Key results

- **Table 1 and App. B (population minima).**
  - NT-Logistic: K̂* = p⁺(a₁,a₂)/(p(a₁)p(a₂)) exactly. The minimizer of the
    logistic loss is the log-odds log(p⁺/(p⊗p)), with equal priors on the
    positive and negative classes (B.2).
  - Spectral: the loss is Σ(p⁺/√(p⊗p) − √(p⊗p)·K̂)² − C, so K̂* = K⁺ (B.3).
  - NT-Xent/InfoNCE: K̂*(a₁,a₂) = K⁺(a₁,a₂)·b(a₁), with b(a₁) = b(a₂)
    whenever p⁺(a₁,a₂) > 0. So b is constant on each communicating class,
    and constant everywhere if the chain is irreducible (B.1). The general
    form f*(c,a) = p(a|c)/p(a)·b(c) is taken from Van den Oord et al.
    (2018), not re-derived. "This optimum is not unique for cross-entropy
    loss."
- **Definition 2.1.** K⁺(a₁,a₂) = p⁺(a₁,a₂)/(p(a₁)p(a₂)) = ⟨φ⁺(a₁), φ⁺(a₂)⟩
  with φ⁺(a)_z = p(a|z)√p(z)/p(a), a feature map into R^|Z|. Points that
  can never form a positive pair have orthogonal features.
- **Proposition 3.1.** For c_i = E[f_i(a)g(a)],
  E_p⁺[(g(a₁) − g(a₂))²] = Σ_i (2 − 2λ_i)c_i², so for g = f_i it is
  2 − 2λ_i (eq. 4).
- **Theorem 3.2.** Population kernel PCA under K⁺ gives σ_i² = λ_i and
  h_i(a) = σ_i f_i(a) = λ_i^(1/2) f_i(a), up to reordering and choice of
  basis within eigenspaces. The proof takes the SVD of B = Φ⁺D_A^(1/2).
  Then BBᵀ = Σ, the feature covariance, and
  BᵀB = D_A^(−1/2)P_(A,A)D_A^(−1/2) = M, the symmetrized adjacency.
- **Proposition C.1.** K⁺(a₁,a₂) = Σ_i λ_i f_i(a₁)f_i(a₂).
- **App. C.3.** M is "exactly the symmetrized adjacency matrix described
  by HaoChen et al.", and its eigenvectors are D_A^(1/2)f_i. They are
  orthonormal under counting measure; the f_i are orthonormal under p(A).
  Assumption 1.1 can be written as 2gᵀLg ≤ ε with L = D_A − P_(A,A).
- **Theorem 4.1.** With r*_d = [f₁, …, f_d], the top-d eigenfunctions, the
  span F_(r*_d) is the argmin over d-dimensional F of two things:
  - max over ĝ ∈ F with E[ĝ²] = 1 of E_p⁺[(ĝ(a₁) − ĝ(a₂))²] (eq. 5);
  - max over g ∈ S_ε of min over ĝ ∈ F of E_p[(g − ĝ)²] (eq. 6).
- **From the proof of Theorem 4.1 (App. D.1).** Three things are in the
  proof but not in the statement.
  - If d is smaller than d*, the dimension of the null space of L (the
    number of eigenvalues equal to 1), "every representation has unbounded
    worst-case approximation error".
  - For d ≥ d*, max over g ∈ S_ε of min over ĝ ∈ F_(r*_d) of
    E[(g − ĝ)²] = ε/(2(1 − λ_(d+1))).
  - The worst-case discrepancy of a unit-norm predictor in F_(r*_d) is
    2(1 − λ_d).
- **Proposition 4.2.** For the absolute loss and the constrained ERM over
  ‖β‖₂ ≤ R,
  E[excess risk] ≤ 2dR/√n + √d·(‖β*‖₂ − R)₊ + √(ε/(2(1 − λ_(d+1)))),
  assuming the Bayes predictor g* satisfies Assumption 1.1.
- **App. E.1.** "When using the spectral contrastive loss with a
  d-dimensional linear kernel head, the population minimizer of the loss
  will exactly correspond to the best d-dimensional approximation of K⁺".
  So the output layer is the top-d principal component functions up to an
  orthogonal rotation. This is asserted, not proved here.
- **App. E.2.** The kernel-operator eigenproblem
  λf(a₁) = Σ_(a₂) K⁺(a₁,a₂)f(a₂)p(a₂) equals E_(a₂|a₁)[f(a₂)] = λf(a₁). So
  SpIN or NeuralEF applied to K⁺ learns the chain's eigenfunctions, and
  NeuralEF's terms become R_ij = E_p⁺[f̂_i(a₁)f̂_j(a₂)]. The result
  resembles VICReg. Their experiments use NeuralEF on a lazy chain
  P_mix = 0.5P + 0.5I, so that eigenfunctions with eigenvalues near 0 can
  be recovered.
- **Experiments (§6, App. F).**
  - On the overlapping-regions task, linear kernels with the spectral
    loss, hypersphere kernels with a learned bias, and NeuralEF recover
    the eigenspaces well. Alignment "emerges during training" and is
    absent at random initialization.
  - Some constraints degrade the estimates: a smaller output dimension, a
    fixed norm ‖h‖ = c as in HaoChen et al., or b = 0 as implicitly in
    SimCLR.
  - On MNIST with k-pixel multinomial augmentation, fewer eigenfunctions
    are recovered as augmentations weaken (k = 10, 20, 50). Even two runs
    of kernel PCA on the exact K⁺ diverge as eigenvalues crowd near 1.
  - Learned eigenvalues decay faster than K⁺'s.
  - Downstream error is similar across representations (Table 2). At
    k = 50 the true eigenfunctions are best, but approximate ones do not
    always beat the ResNet embedding.
- **App. E.1 and F.5 (real data).** The authors "have been so far unable
  to obtain a reliable estimate of the eigenfunctions for real-world
  datasets". On a pretrained SimCLR model the Nyström step ran into
  numerical precision issues. A spectral-loss ImageNet model with ‖h‖ = c
  "does not appear to be a good approximation of K⁺". Its kernel-PCA
  eigenvalues sum to exactly c, so the norm constraint caps the spectrum.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | NT-Logistic and spectral losses have population minimum K⁺ over unconstrained kernels | strong | App. B.2–B.3, exact |
| C2 | NT-Xent/InfoNCE has minimum K⁺ times a factor constant on communicating classes | moderate | App. B.1, over symmetric functions, using Van den Oord et al.'s form of the minimizer |
| C3 | Kernel PCA under K⁺ returns λ_i^(1/2) times the positive-pair chain's eigenfunctions | strong | Theorem 3.2, App. C.2 |
| C4 | The top-d eigenfunctions' span is minimax-optimal for L²(p) approximation of targets in S_ε, with worst-case error ε/(2(1 − λ_(d+1))) | strong | Theorem 4.1, App. D.1; finite A, d ≥ d* |
| C5 | Learned contrastive kernels plus kernel PCA approximately recover these eigenfunctions | moderate | two synthetic tasks, App. F.1; recovery degrades with constraints and weak augmentation |
| C6 | The correspondence has not been shown on real-data training | strong (as a negative) | App. E.1, F.5, the authors' own report |
| C7 | NeuralEF applied to K⁺ resembles VICReg | weak | informal comparison, App. E.2 |

## Method

The pipeline (App. E.1): train with an existing contrastive loss; read off
the learned kernel K̂_θ from Table 1; run kernel PCA (exact on the toy task,
Nyström on MNIST) on a large sample from p(A); take the first d projection
functions h_i and optionally rescale to f_i = σ_i⁻¹h_i. Equation 4 serves as
a diagnostic, since each recovered f_i should satisfy
E[(f_i(a₁) − f_i(a₂))²] ≈ 2 − 2λ_i. The alternative is NeuralEF trained on
positive pairs with the lazy-chain modification (App. E.2).

## Concepts

- **Positive-pair kernel** K⁺: the ratio p⁺(a₁,a₂)/(p(a₁)p(a₂)), a Mercer
  kernel with feature map φ⁺ into R^|Z|. App. B.4 notes that log K⁺ is the
  pointwise mutual information of the two views.
- **Positive-pair Markov chain**: from a_t, draw z ∼ p(z|a_t) and then
  a_(t+1) ∼ p(a|z). Its eigenfunctions satisfy E[f_i(a_(t+1))|a_t] = λ_i f_i(a_t)
  with λ_i ∈ [0, 1], and are orthonormal in L²(p).
- **Positive-pair discrepancy**: E_p⁺[(g(a₁) − g(a₂))²] = 2gᵀ(D_A − P_(A,A))g.
- **S_ε**: the targets with discrepancy at most ε (Assumption 1.1).
- **Communicating class**: a set of augmentations reachable from one
  another along the chain. InfoNCE fixes K⁺ only up to a positive
  constant on each.

## Connections

The paper places itself after analyses based on a single loss each:
- Saunshi et al. (conditional independence within latent classes);
- Wang and Isola (alignment and uniformity on the hypersphere);
- Tosh et al. ([LIT-251](../literature.d/LIT-251.md), landmark embeddings and the logistic loss);
- HaoChen et al. ([LIT-249](../literature.d/LIT-249.md), the augmentation graph and spectral loss).

Its matrix M is HaoChen et al.'s normalized adjacency, and its
eigenfunctions are HaoChen et al.'s eigenvectors divided by p(a)^(1/2). It
reads Lee et al.'s non-linear CCA (2020) as "an asymmetric variant of
Kernel PCA with K⁺". It notes Balestriero and LeCun's ([LIT-228](../literature.d/LIT-228.md)) link
between SimCLR and kernel ISOMAP, and Tian's (2022) game-theoretic account,
without reconciling them with K⁺. On the estimation side it links to SpIN
(Pfau et al., [LIT-252](../literature.d/LIT-252.md)) and NeuralEF. App. B.4 ties K⁺ to the optimal critic
of mutual-information bounds (Poole et al., [LIT-246](../literature.d/LIT-246.md)).

## Bearing on the record

- **[THEORY-001](../theory.d/THEORY-001.md)** is confirmed for the spectral and logistic losses. Its
  promote_when asks for a check of "the Table 1 derivations (App.
  B.1–B.3) and their finite-space and unconstrained-function conditions",
  and both conditions hold as stated. Two corrections, both about
  InfoNCE:
  - **The minimizer is cited, not derived.** The theory says "the
    minimizer over all functions of the two views is derived explicitly".
    For InfoNCE the paper takes the form f* = (p(a|c)/p(a))·b(c) from Van
    den Oord et al. It then restricts to symmetric K̂ to get
    b(a₁) = b(a₂) on positive pairs.
  - **The minimum is over symmetric functions only.** The negatives are
    i.i.d. from the marginal, not drawn from other positive pairs as in
    practice. "Over all functions" should read "over all symmetric
    functions" for NT-Xent.

  The paper also says that this optimum "is not unique for cross-entropy
  loss". The theory's "minimized by K⁺ times a factor that is constant on
  each communicating class" is what the paper says.
- **[THEORY-007](../theory.d/THEORY-007.md)** is confirmed on every cited point: Def. 2.1, Thm 3.2
  (h_i = λ_i^(1/2) f_i), Prop. 3.1 and Thm 4.1, §5 and App. C.3. Its
  promote_when, as it concerns this paper, is met. Three precisions:
  - **Theorem 4.1 needs d ≥ d*.** d* is the multiplicity of eigenvalue 1,
    one per communicating class. Below it, every representation has
    unbounded worst-case error. The minimax value is ε/(2(1 − λ_(d+1))).
  - **The optimality is for squared L²(p) approximation of S_ε, with one
    p(A) shared** between pretraining and the downstream task. The paper
    flags distribution shift, other evaluation protocols and other prior
    knowledge about g as outside it (§7).
  - **"Johnson et al. App. E.2 applies them to K⁺" is true of NeuralEF
    only.** SpIN is named but not run.

  The "does not say" line on trained networks can be strengthened from
  the paper itself. The authors could not obtain reliable eigenfunctions
  from a pretrained SimCLR model. Their ImageNet spectral-loss model "does
  not appear to be a good approximation of K⁺" (E.1, F.5).
- **[THEORY-005](../theory.d/THEORY-005.md)** credits the eigenfunction identification to Thm 3.2, and
  says the operator derivation is the record's own. App. E.2 already
  writes it:
  λ_i f_i(a₁) = Σ K⁺(a₁,a₂)f_i(a₂)p(a₂) = E_(a₂|a₁)[f_i(a₂)]. That is,
  K⁺ is the kernel of the conditional-expectation operator with respect
  to p, with the integral form given as motivation. What the paper does
  not state is:
  - the χ² integrability condition;
  - any result off a finite space.

  So the theory's summary ("No source states the operator formulation with
  its integrability condition") is accurate only with the condition
  included. The formulation without the condition is in this paper.

  The promote_when also asks for "a proof that features trained with a
  standard contrastive loss span the top eigenfunctions of T". App. E.1
  asserts this for the population minimizer of the spectral loss with a
  d-dimensional linear head, and HaoChen et al. prove it (Lemma B.8 with
  Eckart–Young). Neither addresses trained networks, so the condition is
  not met.
- **[THEORY-009](../theory.d/THEORY-009.md)** says the paper uses "the symmetry of P_(A,A) to make
  D^(−½)P D^(−½) orthogonally diagonalizable". That is right in substance,
  and the paper gives a little more than the theory says.
  - App. C.2 calls M "the symmetric matrix" without argument. The
    symmetry holds because P_(A,A) = P_(A←Z)D_Z P_(Z→A) is a Gram matrix.
  - The proof of Theorem 3.2 works through M = BᵀB, which gives positive
    semidefiniteness (λ_i ∈ [0, 1]) as well as symmetry.
  - The main text cites Levin and Peres (ch. 12) on reversible chains for
    the orthonormal basis.

  So the source of self-adjointness is that both views are drawn
  independently from the same p(A|Z). Two things bear on the theory's
  open side:
  - The paper never mentions Riesz.
  - Its pointer to Lee et al.'s non-linear CCA as "an asymmetric variant
    of Kernel PCA with K⁺" is the nearest thing in these sources to the
    singular-function account that [THEORY-009](../theory.d/THEORY-009.md)'s promote_when asks for.
    It is a remark, not an analysis.
- The paper carries an instruction for ML practice: train a contrastive
  model, then run kernel PCA, and prefer unconstrained heads and learned
  biases (App. E.1, F.1). Its anthology-candidate flag stands. This record
  holds it for the kernel and eigenfunction statements.

## Limitations

- Everything is proved on finite Z and A. The integral form in App. E.2 is
  motivation, and no integrability condition is given.
- Table 1's minima are over unconstrained kernels. A finite-dimensional
  dot-product or hypersphere head cannot represent K⁺ in general. The
  experiments show the constraints matter.
- InfoNCE fixes K⁺ only up to per-class constants. The paper restores the
  scale with a logistic-loss term or with Equation 4 (C.4).
- The positive results are on two synthetic tasks built so that K⁺ is
  computable. On real data the authors report failure to extract the
  eigenfunctions.
- Minimax optimality is relative to Assumption 1.1 alone. The authors
  note, after Saunshi et al. (2022), that real augmentations give many
  eigenvalues near 1. That is the regime where their learned kernels stop
  matching K⁺, and where inductive bias rather than K⁺ may carry
  performance.

## Open questions

- Is there an infinite-space version of Theorems 3.2 and 4.1? It would
  need the stated integrability condition on K⁺, for example
  Hilbert–Schmidt on L²(p).
- Can a learned kernel be made to approximate K⁺ in the weak-augmentation
  regime, on real data, well enough for kernel PCA to be stable? The
  authors name better-conditioned linear approximations as the direction.
- How does the optimal basis change under distribution shift between
  pretraining and downstream p(A)? The authors raise this.
- What replaces the eigenbasis when the two views come from different
  conditionals, so that p⁺ is not symmetric? Lee et al.'s CCA is the
  paper's pointer.
