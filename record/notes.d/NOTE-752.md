---
number: 752
status: Read
formerly:
- NOTE-tmpwlhed
paper: LIT-228
title: 'Balestriero & LeCun — SSL Recovers Global and Local Spectral Embedding Methods'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2205.11508v3, 10 June 2022, 32
    pages), text extracted with pdftotext: §§1–7, every theorem and
    proposition (Theorems 1–10, Propositions 1–3), and all of Appendix A
    (A.1–A.17), where the proofs are. The reference list was consulted
    only for the works named below. Figures were read from their captions
    and the surrounding text. This is the arXiv version; the NeurIPS 2022
    proceedings version was not compared with it. Replaces the seeded
    skim, NOTE-199.
date: '2026-10-14'
summary: >-
  On a finite sample with a positive-pair graph G, idealized forms of
  VICReg (squared variance term), SimCLR (a Euclidean graph-matching
  variant) and linear Barlow Twins have optimal representations or
  weights built from the spectrum of G. They are Laplacian eigenmaps, a
  generalized MDS and CCA. All of them align the left singular vectors of
  Z with those of G. SimCLR and Barlow Twins force rank(Z) = rank(G),
  while VICReg can stay full rank. Several proofs are sketches, and the
  experiments are small and synthetic.
---
<!-- inactive-ok-file: THEORY-007 THEORY-009 QUESTION-052 — Proposed or Open; the theory that cites this paper, the theory it bears on, and the question both answer -->
<!-- inactive-ok-file: LIT-249 LIT-252 LIT-258 — Deferred; HaoChen et al., Pfau et al. and Johnson et al., named as the accounts this paper parallels -->

# NOTE-752: Balestriero & LeCun — SSL Recovers Global and Local Spectral Embedding Methods

## Contribution

The paper writes the SSL problem as inputs X with an N × N relation matrix
G that marks positive pairs. It then gives closed-form optima for
idealized versions of three losses.

- **VICReg**, with a squared variance term, gives eigenvectors of
  I − (1/N)11ᵀ − (γ/α)(D − G). With the variance and covariance terms
  forced to zero it is Laplacian eigenmaps. With a linear network it is
  LPP, and LDA when G is the label graph.
- **SimCLR**, in a Euclidean graph-matching variant, gives the top
  eigenvectors of G scaled by the square roots of their eigenvalues. That
  is a generalized MDS, "akin to ISOMAP".
- **Linear Barlow Twins** gives CCA weights.

All of them make the leading left singular vectors of the representation
match those of G. They differ in the rank they allow.

## Key insight

The representation is a signal on the graph G, and each SSL loss is a
spectral embedding of G under a different constraint. What G encodes is
what a linear probe can recover. When G's leading eigenvectors span the
task's, every method is optimal on the training set. When they do not,
the difference that matters is rank. SimCLR and Barlow Twins collapse Z
to rank(G), while VICReg at a low invariance weight keeps Z full rank.

## Assumptions

- **A finite sample and a given graph.** X ∈ R^(N×D), and G ∈ {0,1}^(N×N)
  is symmetric with a zero diagonal. Population results and augmentation
  distributions are outside it.
- **A constant degree for the Laplacian-eigenmaps equivalence.**
  Theorem 2 and App. A.8 need D = cI. With pairs, c = 2 (the paper's
  value); with triplets, c = 3. "Which is always the case in SSL."
- **Free or linear representations.** Theorems 1 and 5 optimize Z
  directly as an N × K matrix. Theorems 3 and 7 take Z = XW. The
  deep-network statements (Propositions 1 and 3, Theorem 6) treat the
  network as a featurizer φ and apply the kernel version of the same
  method.
- **Modified losses.**
  - VICReg's hinge variance term max(0, 1 − √Cov(Z)_kk) is replaced by
    the squared loss Σ_k (1 − Cov(Z)_kk)², and α = β (Theorem 1).
  - SimCLR's closed form (Theorem 5) is proved for the Euclidean
    comparison ‖G − Ĝ‖²_F, with the linear graph estimates of eqs. 17–18
    and τ ≥ max_(i,j) D_ij. For the softmax with cross-entropy, only the
    rank claim is argued, by appeal to Ganea et al. (2019).
  - Barlow Twins is identified with CCA "up to rescaling of the weight
    matrices", with the ε in the denominator read as ridge
    regularization.
- **Invertibility.** Cov(X), or XᵀHX, is invertible for eq. 12, and
  Xᵀ(D − G)X for Theorem 3.

## Key results

- **Invariance as Dirichlet energy (eq. 7, App. A.5).**
  Σ_i Σ_j G_ij ‖Z_i − Z_j‖² = 2 Tr(ZᵀLZ), with L = D − G.
- **Theorem 1 (VICReg optimum).** Take the eigendecomposition
  I − (1/N)11ᵀ − (γ/α)(D − G) = P_(α,γ) diag(λ_(α,γ)) P_(α,γ)ᵀ (eq. 8).
  Then Z*_(α,γ) = (P_(α,γ) (diag(λ_(α,γ)) N)^(1/2))_(:,1:K) and
  min L_VIC = α(K − ‖(λ)_(1:K)‖²₂). Any K-out-of-N columns give a local
  minimum. "Only the ratio γ/α governs the VICReg representation." The
  indexing is not consistent: Figure 4's caption says the optimum is the
  [1 : K − 1] case, and eq. 9's sparse version takes [2 : K].
- **Theorem 2 (Laplacian eigenmaps).** L_vic(Z*_LE) = min_Z L_inv(Z)
  s.t. L_var = 0 and L_cov = 0. LE solves min Tr(Zᵀ(D − G)Z) s.t.
  ZᵀDZ = I (eq. 10). When D − G is idempotent, LE is also LLE.
- **Proposition 1.** Constrained VICReg "solves LE in embedding space and
  KLLE in input space", with a deep network as Wᵀ ∘ φ. This is asserted
  from He and Niyogi (2003), not proved here.
- **Linear VICReg (eq. 12, App. A.9).**
  W* = Cov(X)⁻¹ (Cov(X) − (γ/(αN)) XᵀLX)^(1/2), first K columns. This
  is shown for K = D. For K < D, any K columns give the same loss.
- **Theorem 3 (LPP and LDA).** With the variance-covariance constraint
  and a linear network, W* is given by "the top-K eigenvectors of
  (Xᵀ(D − G)X)⁻¹XᵀGX", with G = G_s and K = C for LDA. The LDA
  equivalence is with the trace-ratio surrogate, not exact LDA
  (App. A.15).
- **Theorem 4 (SimCLR's similarity as graph estimation).** Minimize
  Tr(DĜ) + R(Ĝ), with R_log(G) = Σ_(i≠j) τ G_ij (log G_ij − 1). The
  result is Ĝ_ij = e^(−d_ij/τ) over all graphs, or its row-normalized
  softmax over right-stochastic graphs (eq. 16). With cosine distance this
  is SimCLR's similarity. With ℓ2 distance it is the lifted structured
  loss.
- **Theorem 5 (SimCLR optimum).** Z*_τ = (U_G Σ_G^(1/2))_(:,1:K) and
  min L_SimCLR = Σ_(k=K+1)^N (Σ_G²)_(k,k). The rank of Z*_τ is
  min(K, rank(G)) "regardless of the loss and graph estimation".
  - The statement treats G as "symmetric semi-definite positive". A
    zero-diagonal adjacency matrix is not. The proof (App. A.11) works
    with G + I, which has the same eigenvectors.
  - The proof ends by citing Higham (1988), and for cross-entropy Ganea
    et al. (2019) and Knaf (2007).
- **Proposition 2.** SimCLR recovers "a Generalized MDS akin to ISOMAP",
  and MDS iff G = XXᵀ. App. A.12 is two sentences: G and G + I share
  eigenvectors.
- **Proposition 3** (credited to Williams, 2000). Where SimCLR recovers
  ISOMAP or MDS in feature space, it recovers kernel ISOMAP or kernel PCA
  in input space.
- **Theorem 6 (Barlow Twins as kernel CCA).** It "produce[s] a
  representation with rank min(K, D, rank(G))". App. A.13 refers back to
  the linear proof and stops without deriving the rank claim.
- **Theorem 7 (linear Barlow Twins as CCA).**
  - W_a* = top-K eigenvectors of C_aa⁻¹ C_ab C_bb⁻¹ C_ba, and
    W_b* = C_bb⁻¹ C_ba W_a*.
  - "With a symmetric G and same dimensional X_a, X_b, weight-sharing
    naturally occurs": W_a* = W_b* = top-K eigenvectors of C_bb⁻¹ C_ba.
  - With the label graph and K = C, it recovers LDA, and so VICReg.
  - The proof (App. A.16) derives CCA's Lagrangian and asserts that it is
    the Barlow Twins objective. Figure 3's caption says that G "is
    commonly symmetric, it is often not required (see Theorem 7)".
- **Theorem 8 (linear probe).**
  min_W ½‖Y − ZW‖²_F = ½‖Y‖²_F − ½‖Û_zᵀ U_y Σ_y‖²_F (eq. 22). It is 0 iff
  the columns of Û_z span those of Û_y.
- **Theorem 9 (optimality).** For VICReg, SimCLR or Barlow Twins,
  min_W ‖Y − Z*W‖²_F = 0 ⟺ Û_y ∈ span(Û_g). The proof (App. A.17) is
  three sentences and names VICReg only.
- **Theorem 10 (bounds).**
  Σ_(i=R)^K (Σ_y²)_(i,i) ≤ min L(W, Z*_SimCLR(G)) − min L(W, Z*_VICReg(G))
  ≤ ‖Y‖²_F, over all G of rank R, "and are tight. Hence one should prefer
  VICReg, then BarlowTwins and finally SimCLR". No proof is given in the
  appendix. Barlow Twins does not appear in the bound.
- **Experiments.** All use synthetic graphs, with Z or W optimized
  directly.
  - Figure 4: N = 256, K = 16, rank(G) = 4.
  - Figure 5: N = 256, K = 32, rank(G) = 8.
  - Figure 6: N = 512, D = 64. SGD and RMSProp reach Theorem 1's loss and
    eq. 12's weights.
  - Figure 8: rank(G) ∈ {8, 16, 32}. SimCLR's learned rank equals
    rank(G).
  - Figure 9: N = 512, K = 128, rank(G) ∈ {32, 128}. Barlow Twins'
    learned rank equals rank(G).
  - No deep network is trained on real data.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | VICReg's invariance term is the Dirichlet energy of Z on G | strong | eq. 7, App. A.5; a standard identity |
| C2 | With a squared variance term, VICReg's global optimum is the top eigenvectors of I − (1/N)11ᵀ − (γ/α)(D − G), scaled | moderate | Theorem 1, App. A.7; index conventions inconsistent |
| C3 | With variance and covariance forced to zero and constant degree, VICReg is Laplacian eigenmaps, and linear VICReg is LPP | moderate | Theorems 2–3, Apps. A.8, A.14; LPP by citation |
| C4 | The Euclidean SimCLR variant's optimum is the top eigenvectors of G scaled by √eigenvalue, and SimCLR's rank equals rank(G) | moderate | Theorem 5, App. A.11; closed form for the Euclidean variant only, rank for cross-entropy by citation; Figure 8 |
| C5 | Linear Barlow Twins is CCA, with shared weights when G is symmetric | weak | Theorem 7, App. A.16; the identification with CCA is asserted |
| C6 | Any of the three is optimal for a linear probe on the training set iff the task's left singular vectors lie in G's | moderate | Theorems 8–9; Theorem 8 proved, Theorem 9 sketched |
| C7 | Under a misaligned G, low-invariance VICReg should be preferred to Barlow Twins and SimCLR | weak | Theorem 10, unproved; Figure 5, synthetic |
| C8 | Contrastive methods are global spectral methods and non-contrastive ones local | weak | analogy from Propositions 1–2; no experiment separates them |

## Method

For each loss, the paper writes it as a trace or Frobenius problem in Z
and G. It replaces the parts that block a closed form (the hinge, the
softmax with cross-entropy) with squared or linear surrogates. It then
reads the optimum off an eigendecomposition, by Eckart–Young or a
Lagrangian. Spectral-method equivalences are then quoted from the
manifold-learning literature (He and Niyogi; Williams; Kokiopoulou et
al.; Kursun et al.).

## Concepts

- **G, the relation matrix.** A symmetric N × N matrix, nonnegative or
  binary, with G_ij = 1 iff samples i and j are positives. Built from
  views (eq. 1) or labels (G_s, eq. 13).
- **Global and local spectral methods.** Global methods (MDS, ISOMAP)
  preserve all pairwise similarities. Local methods (Laplacian
  eigenmaps, LLE, LPP) preserve neighbourhoods. The paper maps
  contrastive methods to the first and non-contrastive methods to the
  second.
- **Aligned G.** G's left singular vectors with nonzero singular values
  span those of the target matrix Y.
- **Dimensional collapse.** Here: rank(Z*) = rank(G) < K, which is forced
  by SimCLR and Barlow Twins.

## Connections

The paper sets itself after HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)), whose spectral
contrastive loss it calls "a modified objective" for SimCLR. It names
Pfau et al.'s Spectral Inference Networks ([LIT-252](../literature.d/LIT-252.md)) with Sprekeler's
link from slow feature analysis to Laplacian eigenmaps as "a perhaps more
direct connection". It extends Bao et al. and HaoChen et al.'s downstream
results to several losses (§6). Simon et al. ([LIT-242](../literature.d/LIT-242.md)) later place this
paper among works that "jump to optima" and say its final representations
differ from theirs. Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) is later work and is not
cited.

## Bearing on the record

- **[THEORY-007](../theory.d/THEORY-007.md)** cites the paper as supporting, and in its "does not
  say" list asks "which of Balestriero & LeCun's dictionaries (Laplacian
  eigenmaps, ISOMAP, CCA) is the right one for a given method".
  - **The framing is off.** The paper does not offer three dictionaries
    for one method. It gives one per method: VICReg is LE, SimCLR is
    generalized MDS, Barlow Twins is CCA.
  - **They pick the same eigenvectors.** The paper itself says that "all
    SSL methods' optimal learn a representation Z whose top left singular
    vectors align with the ones of G". With D = cI, as the paper assumes,
    L = cI − G and the random-walk matrix D⁻¹G = G/c have the same
    eigenvectors as G. So, on the sample, the three dictionaries select
    the same eigenvectors and differ only in scaling and rank.
  - **Those eigenvectors are [THEORY-007](../theory.d/THEORY-007.md)'s objects on a finite sample.**
    G/c is the transition matrix of the positive-pair chain on the sample
    graph, and D^(−1/2)GD^(−1/2) = G/c is HaoChen et al.'s normalized
    adjacency. So the paper supports the eigenvector identification of
    [THEORY-007](../theory.d/THEORY-007.md) at the finite-sample level, for its idealized losses,
    where uniform degree makes the normalizations coincide. This
    reconciliation is mine; the paper states the shared alignment but
    not the link to K⁺ or the Markov chain.
  - **Nothing on population eigenfunctions or minimax optimality.** The
    paper says nothing on population eigenfunctions, K⁺, or the minimax
    optimality of [LIT-258](../literature.d/LIT-258.md)'s Thm 4.1. Its downstream result (Theorem 9) is
    weaker and of a different kind: zero linear-probe loss on the
    training set iff the task's left singular vectors lie in G's span.
- **[THEORY-009](../theory.d/THEORY-009.md)** does not cite this paper, but should.
  - Theorem 7 is a published account in which a non-symmetric pair
    structure is handled by CCA. CCA is the singular value decomposition
    of the whitened cross-covariance C_aa^(−1/2) C_ab C_bb^(−1/2), a
    non-self-adjoint operator. The paper says that G being symmetric "is
    often not required (see Theorem 7)". Symmetry of G is exactly what
    yields weight sharing, W_a* = W_b*.
  - This is the case [THEORY-009](../theory.d/THEORY-009.md) says no account was found for. It is
    close to the theory's `promote_when`. Two caveats: the objective is
    Barlow Twins, not an asymmetric objective of the BYOL kind; and the
    identification of Barlow Twins with CCA is asserted, not derived.
- **[QUESTION-052](../questions.d/QUESTION-052.md)** asks what replaces the top eigenspace when the
  transformations are directed. In the linear regime, this paper's
  answer is canonical correlation directions, the singular vectors of the
  whitened cross-covariance.
- **Practice.** The practical advice is an instruction for ML practice:
  prefer low-invariance VICReg when G is misaligned, and raise VICReg's
  invariance weight in the low-data regime. It rests on Theorem 10, which
  is unproved, and on synthetic figures with N = 256. The
  `anthology-candidate` flag on the LIT stands.

## Limitations

- Everything is finite-sample with a fixed G. Nothing is said about
  augmentation distributions, generalization beyond the training set, or
  what gradient descent on a deep network reaches. Figure 6 checks
  convergence only for free Z and for a linear W.
- The closed forms hold for modified losses: a squared variance term for
  VICReg, and a Euclidean comparison with linear graph estimates for
  SimCLR. For SimCLR as used (softmax with cross-entropy), only the rank
  claim is argued.
- Several proofs are sketches or citations: Proposition 1, Proposition 2
  (A.12), Theorem 6 (A.13 stops before the rank claim), Theorem 9 (A.17)
  and Theorem 10 (no proof). There are typographical errors in the
  statements: λ_(α,β) for λ_(α,γ), C_aa = X_aᵀX_b, and 1{1≠j}.
- The global/local mapping is an analogy. Barlow Twins is called
  non-contrastive but is mapped to CCA, which is neither a local nor a
  global embedding method.
- The "prefer VICReg, then BarlowTwins, then SimCLR" ranking is not
  supported for Barlow Twins by the stated bound.

## Open questions

- Do the closed forms survive the hinge variance term and the
  softmax with cross-entropy? Solving those losses, or showing their
  minimizers differ, would settle it.
- Is Theorem 10 true as stated? A proof, or a counterexample with an
  aligned G of rank R where SimCLR and VICReg both reach zero loss, would
  settle it.
- Does the identification of Barlow Twins with CCA hold, given that
  Barlow Twins pushes the diagonal of the cross-correlation to 1 while
  CCA's canonical correlations are generally below 1? An explicit
  minimization of eq. 5 for linear Z would settle it.
- Does low-invariance VICReg beat SimCLR and Barlow Twins with a
  misaligned G on real data? An experiment on real data where G is
  deliberately misaligned would settle it.
