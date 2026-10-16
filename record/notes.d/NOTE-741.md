---
number: 741
status: Read
formerly:
- NOTE-tmpdlxl6
paper: LIT-242
title: 'Simon et al. — On the Stepwise Nature of Self-Supervised Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2303.15438v2, 30 May 2023, 25 pages),
    text extracted with pdftotext: §§1–7, every proposition, Result 4.6
    and Definitions 4.2–4.5, and Appendices A–G, including the proofs of
    Propositions 4.3 and 5.1 (App. B), the informal derivation of Result
    4.6 (App. C), the experimental details (App. D), the empirical-NTK
    comparison (App. E), the symmetry-breaking appendix (F) and the
    speed-up proposals (G). Figures were read from their captions and the
    surrounding text; plotted values were not read off the images. The
    reference list was consulted only for the works named below. Replaces
    the seeded skim, NOTE-218.
date: '2026-10-14'
summary: >-
  For a simplified Barlow Twins loss on a linear or kernel model trained by
  gradient flow from small initialization, the embedding learns the top
  eigenvectors of a symmetrized cross-correlation operator one at a time,
  each at a time set by its eigenvalue, and lands on the minimum-norm
  zero-loss solution: kernel PCA on K_Γ. Exact for aligned initialization;
  an informal derivation for generic small initialization. ResNets trained
  with Barlow Twins, SimCLR and VICReg show the same stepwise rank growth,
  which is an empirical finding, not a consequence of the theory.
---
<!-- inactive-ok-file: THEORY-009 QUESTION-052 — Proposed or Open; the theories that cite this paper and the question they answer -->

# NOTE-741: Simon et al. — On the Stepwise Nature of Self-Supervised Learning

## Contribution

The paper solves the gradient-flow dynamics of a simplified Barlow Twins
loss on a linear model, and kernelizes the solution so that it covers any
kernel machine, including an infinitely wide network in the NTK regime.
From small initialization, the embedding gains rank one step at a time,
and each step learns the next eigenvector of a symmetrized
cross-correlation matrix Γ. The step for mode j comes at a time set
mainly by 1/γ_j. Among the many zero-loss solutions, training reaches the
minimum-norm one, and in kernel form that solution is kernel PCA on a
matrix K_Γ. The same stepwise growth of embedding rank is then observed
in ResNet-50s trained with Barlow Twins, SimCLR and VICReg.

## Key insight

SSL losses of this kind have a symmetry, f → −f, and in fact f → Uf for any
orthogonal U, so each embedding direction starts at an unstable
equilibrium near zero. A mode escapes it after a time proportional to
−log(initial size)/γ_j, so modes are picked up in eigenvalue order, with
plateaus in between. The optimum-based accounts say which subspace is
optimal. This paper says which of several zero-loss optima training
reaches (the minimum-norm one), and in what order its directions arrive.

## Assumptions

- **A simplified Barlow Twins loss (§3).** L = ‖C − I_d‖²_F, with
  C = (1/2n) Σ_i [f(x_i) f(x′_i)ᵀ + f(x′_i) f(x_i)ᵀ]. Relative to Zbontar
  et al., λ is set to 1, batch norm is removed from C, and C is
  symmetrized. Neither SimCLR nor VICReg is analysed.
- **A linear model f(x) = Wx, or a fixed-kernel model (§5).** The kernel
  case covers random features, last-layer training and the infinite-width
  NTK limit. A network whose NTK moves during training is outside the
  theory.
- **Full-batch gradient flow**, dW/dt = −∇_W L, on n fixed positive pairs
  (n → ∞ gives the population case, footnote 6).
- **Small initialization.** Proposition 4.1 needs aligned initialization:
  the right singular vectors of W(0) are eigenvectors of Γ. Result 4.6
  needs initialization scale α → 0, distinct γ_1, …, γ_d, γ_1, …, γ_d > 0,
  γ_d > γ_(d+1), and W̃_0 Γ_(≤d) of full rank.
- **Result 4.6 is not a theorem.** The authors style it a Result
  "because we give an informal derivation rather than a formal proof"
  (footnote 8). The derivation in App. C argues that the off-diagonal
  entries a_jk(t) stay o(1). It is checked numerically only for d = 3,
  m = 5 (Figure 6).
- **Γ is symmetric by construction.** Γ = (1/2n) Σ_i (x_i x′_iᵀ + x′_i x_iᵀ),
  because C was symmetrized by hand. The pair data need not be symmetric
  for this.

## Key results

- **Loss in matrix-factorization form (§4.1).** C = WΓWᵀ (eq. 4), so
  L = ‖WΓWᵀ − I_d‖²_F (eq. 5) and dW/dt = −4(WΓWᵀ − I_d)WΓ (eq. 6).
- **Proposition 4.1 (exact trajectory, aligned initialization).** If
  W(0) = U S_0 Γ_(≤d), then W(t) = U S(t) Γ_(≤d) with
  s_j(t) = e^(4γ_j t) / √(s_j(0)^(−2) + (e^(8γ_j t) − 1) γ_j) (eq. 10). As
  t → ∞, s_j → γ_j^(−1/2) if γ_j > 0, stays s_j(0) if γ_j = 0, and → 0 if
  γ_j < 0 (eq. 13). The loss separates as L = Σ_j (1 − γ_j s_j²)² (eq. 14).
  The eigenvalues of C, λ_j = γ_j s_j², follow nearly sigmoidal curves.
- **Proposition 4.3 (minimum norm).** The top spectral W,
  W = U diag(γ_j^(−1/2) 1[γ_j > 0]) Γ_(≤d) (Definition 4.2), "are
  precisely the solutions to argmin ‖W‖_F s.t. L(W) = 0" (eq. 15). Other
  zero-loss optima exist, for example ones aligned with other positive
  eigenvectors. The main text says the proof is in Appendix C; it is in
  App. B.1. That proof minimizes L + ε‖W‖²_F as ε → 0 and argues that
  the stationary points share eigenvectors with Γ.
- **Step times (§4.3).** For s_j(0) ≪ γ_j^(−1/2), s_j stays small until
  τ_j = −log(s_j(0)² γ_j) / (8γ_j) (eq. 16), then grows quickly. The loss
  steps down by about one per mode, L(t) ≈ Σ_(j: τ_j > t) 1 (eq. 20).
- **Result 4.6 (generic small initialization).** With W(0) = αW̃_0, and
  W*(t) the aligned trajectory started from the alignment transformation
  (QR with off-diagonals of R zeroed) of W(0), ‖W(t) − W*(t)‖_F → 0 for
  all t as α → 0. The effective initial singular values come from a
  Gram–Schmidt-like recursion (eq. 19). Off-diagonal terms grow as
  a_jk(t) = O(α^(1 − γ_k/γ_j)) for j < k (eq. 48).
- **Linear check (§4.4, Figure 1A–B).** n = 500 CIFAR-10 crop pairs,
  m = 1200, d = 10, α = 10⁻⁷. The predicted step times and eigenvalues
  agree with simulation ("excellent agreement").
- **Proposition 5.1 (kernelized solution).** Let
  K̃ = [[K_XX, K_XX′], [K_X′X, K_X′X′]], let Z be as in eq. 23, and let
  K_Γ = K̃^(−1/2) Z K̃^(−1/2), with (γ_j, b_j) its eigenpairs in descending
  order.
  - (a) "All nonzero eigenvalues of K_Γ are eigenvalues of Γ and vice
    versa."
  - (b) The top spectral solution gives
    f(x) = U S̃ [b_1 … b_d]ᵀ K̃^(−1/2) [K_xX K_xX′]ᵀ (eq. 24).
  - (c) These are the solutions of argmin ‖f‖_K s.t. L(f) = 0 (eq. 25),
    which follows from Proposition 4.3.
  App. B.2 also gives the embedding over time, f(x, t), from small
  initialization (eqs. 40–42).
- **Readings of Proposition 5.1 (§5.2).**
  - With X = X′, K_Γ = K̃, and the model learns the top eigenmodes of its
    base kernel.
  - "SSL with neural networks amounts to kernel PCA in the infinite-width
    limit." K_Γ "is not technically a kernel matrix as it can have
    negative eigenvalues" (footnote 11).
  - For CLIP-like two-tower setups, K_XX′ = K_X′X = 0, and the solution
    "remain[s] valid and nonvacuous".
- **ResNet experiments (§6, App. D).**
  - ResNet-50 encoders on STL-10 with small parameterwise initialization
    and small learning rates show discrete steps for Barlow Twins (λ = 1,
    no pre-loss batch norm), SimCLR and VICReg (Figures 1C–D, 2C–F).
  - "Agreement with predictions using the initial NTK is poor", so theory
    curves are omitted.
  - With standard initialization and hyperparameters, the eigenvalues
    split into a grown band and an ungrown band, and the histograms are
    bimodal (Figures 3–4). For Barlow Twins and VICReg the directions may
    come "a few at a time" (footnote 17).
  - Hidden representations step at the same times as the embeddings
    (Figure 5).
  - Linear-probe accuracy with small initialization is a few percent
    below standard, and training is slower (Figure 7).
  - BYOL: "we did not immediately see stepwise learning" (footnote 16).
- **Empirical NTK after training (App. E, Table 1).** d = 50, n = 1000
  pairs. The subspace alignment between the true embeddings and the eq. 24
  prediction from the final empirical NTK is 0.615 (Barlow Twins), 0.517
  (SimCLR) and 0.592 (VICReg), against 0.025 for random subspaces. The top
  d eigenvectors of K̃ alone give 0.510, 0.450 and 0.481. The three
  methods' embeddings align with each other at 0.405–0.504 (Table 2).
- **Speed-up proposals (App. G).** Preconditioning ∇_F L by (FᵀF + αI)⁻¹,
  a loss with a kink at zero (g(λ) = sign(λ)|λ|^(1/2)), and losses with
  wider minima. "We leave our results at the level of theoretical
  speculation." None is tested.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | From aligned initialization, the linear simplified-Barlow-Twins model learns the top eigenvectors of Γ one by one, mode j at τ_j ≈ −log(s_j(0)²γ_j)/(8γ_j) | strong | Proposition 4.1, eqs. 10, 16; proof by substitution |
| C2 | The top spectral solutions are exactly the minimum-Frobenius-norm zero-loss solutions | moderate | Proposition 4.3, App. B.1; the proof is brief, with index slips |
| C3 | Generic small initialization follows the aligned trajectory as α → 0 | moderate | Result 4.6, an informal derivation in App. C; numerical checks at d = 3 and in §4.4 |
| C4 | For a fixed-kernel model, the final embedding is given in closed form by the top eigenvectors of K_Γ: kernel PCA | strong | Proposition 5.1, App. B.2 |
| C5 | ResNets trained with Barlow Twins, SimCLR and VICReg gain embedding rank stepwise, most clearly from small initialization | moderate | §6, Figures 1–5; one dataset (STL-10); BYOL not seen to step |
| C6 | The final empirical NTK predicts about half of the learned embedding subspace | weak | App. E, Table 1; d = 50, n = 1000, one run per method |
| C7 | SSL is slow because low-eigenvalue modes take long to grow, and targeting them would speed training | weak | App. G; an untested hypothesis supported by Figure 3 |

## Method

The analysis rewrites the loss as a symmetric matrix-factorization
problem in W and Γ. It solves the singular-value ODE
s′_j = 4(1 − γ_j s_j²) γ_j s_j under an ansatz that keeps the singular
vectors fixed. It then argues that generic small initialization first
aligns with the top-d eigenspace of Γ, since W ≈ W(0) e^(4Γt) early on,
and then follows the aligned solution. Kernelization rewrites every
quantity in terms of inner products through the dual vector
b = K̃^(−1/2) [X; X′] g (eq. 33).

## Concepts

- **Γ, the feature cross-correlation matrix.**
  Γ = (1/2n) Σ_i (x_i x′_iᵀ + x′_i x_iᵀ), symmetric by construction. It
  "characterizes the spectral bias of the model on the dataset".
- **Top spectral W.** W = U S̃ Γ_(≤d), with S̃ = diag(γ_j^(−1/2) 1[γ_j > 0])
  and U orthogonal. Following HaoChen et al., the rotation U does not
  affect a linear probe.
- **K_Γ.** K̃^(−1/2) Z K̃^(−1/2), "a kernelized version of Γ". It is
  symmetric but can have negative eigenvalues.
- **Alignment transformation.** A(M) = QR̃, where M = QR is a QR
  factorization and R̃ is R with its off-diagonal entries set to zero.
- **Stepwise learning.** The sequential growth of embedding rank, one
  orthogonal direction per stage, with loss plateaus in between.

## Connections

The paper places itself after HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)), whose optimal
representation it calls "model-agnostic" and "usually highly degenerate in
realistic cases". It says it completes that picture by "characterizing
this inductive bias for linearized SSL models as a bias towards small RKHS
norm". It groups Balestriero & LeCun ([LIT-228](../literature.d/LIT-228.md)), Kiani et al. and Cabannes
et al. as works that "jump to optima" and whose final representations
"differ from ours". Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) appears only in a list of kernel
and spectral approaches. The loss form comes from Ziyin et al. (2022). The
dynamics parallel deep linear networks (Saxe et al.; Jacot et al. 2021)
and Landau's 1944 model of the onset of turbulence. [LIT-855](../literature.d/LIT-855.md) extends the
approach to word2vec-like models.

## Bearing on the record

- **[THEORY-007](../theory.d/THEORY-007.md).**
  - The paper supports the theory only by analogy. Its operator is Γ, or
    K_Γ, built from the model's kernel and the sample pairs. It is not
    K⁺, nor the positive-pair Markov chain, nor a population density
    ratio. With X = X′ it reduces to the base kernel's own eigenmodes. It
    says nothing on the minimax optimality of Thm 4.1 of [LIT-258](../literature.d/LIT-258.md).
  - [THEORY-007](../theory.d/THEORY-007.md) says that "Simon et al. say their final representations
    differ from those of the optimum-based accounts". That is stronger
    than the text. The "differ from ours" remark is about Balestriero &
    LeCun, Kiani et al. and Cabannes et al. Towards HaoChen et al. the
    paper claims to complete their account, by picking one of their
    degenerate optima, not to differ from it. Of Johnson et al. it says
    nothing beyond a citation.
  - Otherwise [THEORY-007](../theory.d/THEORY-007.md)'s "does not say" item is accurate: the kernel is
    built from the NTK and the pair structure.
- **[THEORY-009](../theory.d/THEORY-009.md).**
  - The citation is accurate: Γ is symmetrized by hand. It is defined
    just after eq. 4, and the symmetrization is made in C (eq. 2).
  - But this paper does not fit [THEORY-009](../theory.d/THEORY-009.md)'s title. Here the symmetry
    comes from symmetrizing the loss, not from a symmetric positive-pair
    distribution. The paper applies the same symmetric Γ to CLIP-like
    two-tower pairs (§5.2, K_XX′ = 0), where there is no single space
    and no symmetric pair distribution.
  - In that case, writing the two towers' features on orthogonal
    subspaces makes Γ a block off-diagonal matrix of the
    cross-covariance and its transpose. Its eigenvalues are then ± the
    singular values of the cross-covariance. This is my inference, a
    standard one (the Jordan–Wielandt construction); the paper does not
    say it.
  - So this paper is a published account in which a cross-modal
    objective is handled by the singular vectors of a non-self-adjoint
    cross-covariance, inside a symmetric eigenproblem. [THEORY-009](../theory.d/THEORY-009.md) says no
    such account was found. It does not meet the `promote_when`, which
    asks for an asymmetric objective: the objective here is symmetrized.
    It should still be cited as the nearest case.
- **[QUESTION-052](../questions.d/QUESTION-052.md)** asks what takes the place of the top eigenspace
  when the transformations are directed. For a symmetrized loss on
  directed or cross-modal pairs, this paper's answer is the symmetric part
  of the cross-correlation. It answers only for that loss.
- **Practice.** App. G proposes ways to speed up SSL training. They are
  untested, and they are instructions for machine-learning practice, so
  they belong in the anthology if anywhere. The `anthology-candidate` flag
  on the LIT stands.

## Limitations

- The theory covers one simplified loss: Barlow Twins with λ = 1, no
  batch norm and a symmetrized C. SimCLR and VICReg are covered only by
  experiment.
- The theory is for linear and fixed-kernel models. The authors say "the
  NTK is known to change over time", and the predictions from the initial
  NTK are "poor" for ResNets.
- Result 4.6 is derived informally. There are small slips in the text:
  the proof of Proposition 4.3 is said to be in App. C but is in App. B.1,
  and B.1 writes "eigenvalues" for eigenvectors and lists indices from
  {1, …, d} where {1, …, m} is meant.
- The theory describes the final embeddings, while downstream probes use
  hidden layers. The steps seen in hidden layers are empirical only.
- No downstream generalization result: "We leave this direction for
  future work."
- BYOL did not show steps, and predictor or stop-gradient methods are not
  analysed.
- All experiments use STL-10 (CIFAR-10 for the linear model), with a
  single run per configuration.

## Open questions

- Can stepwise learning be derived for a time-varying NTK? The authors
  conjecture so in App. F, via the escape from saddle points of
  decreasing index.
- Why does BYOL not step? A dynamical analysis of a predictor or
  stop-gradient objective would settle it.
- Do the App. G modifications speed up training without hurting
  representations? A controlled comparison of wall-clock time to a fixed
  linear-probe accuracy would settle it.
- How does the K_Γ solution relate to the population eigenfunctions of
  [LIT-258](../literature.d/LIT-258.md) and the augmentation-graph eigenvectors of [LIT-249](../literature.d/LIT-249.md)? A
  derivation of K_Γ's limit as n → ∞ for a universal kernel would show
  whether it converges to K⁺-kernel PCA.
