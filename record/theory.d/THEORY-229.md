---
number: 229
status: Active
formerly:
- THEORY-tmpbaoyn
title: "For a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from a small initialization of common scale aligned with the top eigenvectors of the pairs' symmetrized cross-correlation learns them one at a time, in order of eigenvalue, and ends at a top spectral solution, which is exactly a minimum-norm zero-loss solution: kernel PCA on K_Γ"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-229 (batch 036, ADR-047 v2).
    Propositions 4.1, 4.3 and 5.1 were re-derived, in the dated note
    below; the minimum-norm step is re-proved by interlacing in place of
    App. B.1's brief argument. The title now covers initialization aligned
    with the top eigenvectors at a common small scale, where the dynamics
    are exact and the order is the eigenvalue order. Generic small
    initialization rests on Result 4.6, an informal derivation, and the
    former promote_when's request for its proof moves to QUESTION-tmpqtbzj.
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-242
summary: >-
  Simon et al. (2023), [LIT-242](../literature.d/LIT-242.md), read in [NOTE-741](../notes.d/NOTE-741.md). For L = ‖C − I‖²_F
  with λ = 1, no batch norm and C symmetrized by hand, a linear model from
  aligned initialization learns mode j at τ_j ≈ −log(s_j(0)²γ_j)/(8γ_j)
  (Prop. 4.1, proved), the top spectral solutions are exactly the
  minimum-norm zero-loss ones (Prop. 4.3), and the kernel version is kernel
  PCA on K_Γ (Prop. 5.1). Generic small initialization is covered by an
  informal derivation only. The operator is built from the model's kernel
  and the sample pairs, not from the positive-pair density ratio, and the
  stepwise growth seen in ResNets under SimCLR and VICReg is an experiment,
  not a consequence.
answers:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-182 THEORY-186 QUESTION-039 QUESTION-052 — Proposed or Open, or Active and cited for context; this account rests on none of them -->

# THEORY-229: For a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from a small initialization of common scale aligned with the top eigenvectors of the pairs' symmetrized cross-correlation learns them one at a time, in order of eigenvalue, and ends at a top spectral solution, which is exactly a minimum-norm zero-loss solution: kernel PCA on K_Γ

## Source

Simon et al. (2023), [LIT-242](../literature.d/LIT-242.md), read
in [NOTE-741](../notes.d/NOTE-741.md): §§3–5, Propositions 4.1, 4.3 and 5.1 with their proofs
(App. B), Result 4.6 and its derivation (App. C), §6 and App. E.

## What was actually shown

**The setting.** The loss is a simplified Barlow Twins,
L = ‖C − I_d‖²_F with C = (1/2n) Σ_i [f(x_i)f(x′_i)ᵀ + f(x′_i)f(x_i)ᵀ]:
λ = 1, no batch norm, and C symmetrized by hand. For a linear model
f(x) = Wx, C = WΓWᵀ with Γ = (1/2n) Σ_i (x_i x′_iᵀ + x′_i x_iᵀ), so the
loss is a symmetric matrix-factorization problem (eqs. 4–6). Training is
full-batch gradient flow on n fixed pairs.

**Aligned initialization, exact (Prop. 4.1).** If the right singular
vectors of W(0) are eigenvectors of Γ, the singular values evolve
independently, s_j(t) = e^(4γ_j t)/√(s_j(0)^(−2) + (e^(8γ_j t) − 1)γ_j)
(eq. 10), and tend to γ_j^(−1/2) for γ_j > 0. From s_j(0) ≪ γ_j^(−1/2) a
mode stays small until τ_j = −log(s_j(0)²γ_j)/(8γ_j) (eq. 16) and then
rises sharply, so the loss falls by about one per mode, in order of
eigenvalue (eq. 20).

**Which optimum (Prop. 4.3).** Other zero-loss solutions exist. The top
spectral solutions, W = U diag(γ_j^(−1/2)) Γ_(≤d), are exactly the
minimum-Frobenius-norm ones (eq. 15). The proof (App. B.1) is brief, with
index slips.

**Kernel form (Prop. 5.1).** For any fixed kernel, including the
infinite-width NTK, the final embedding is given in closed form by the top
eigenvectors of K_Γ = K̃^(−1/2) Z K̃^(−1/2) (eq. 24), and these are the
minimum-RKHS-norm zero-loss solutions (eq. 25). The nonzero eigenvalues of
K_Γ are those of Γ. With X = X′, K_Γ = K̃ and the model learns its base
kernel's top eigenmodes: kernel PCA.

**Generic initialization, informal (Result 4.6).** For W(0) = αW̃₀ with
distinct positive γ_1, …, γ_d and γ_d > γ_(d+1), the trajectory approaches
the aligned one as α → 0. The authors call it a Result "because we give an
informal derivation rather than a formal proof". It is checked numerically
at d = 3 and on 500 CIFAR-10 crop pairs, where predicted step times and
eigenvalues agree with simulation (§4.4).

What could have come out the other way: the linear simulation could have
shown modes arriving together or out of order from random small
initialization, and it did not.

## What this does not say

- **Not that deep SSL networks are kernel PCA.** Theory covers linear and
  fixed-kernel models. For ResNet-50s the initial-NTK predictions are
  "poor" and the authors omit them. The final empirical NTK predicts about
  half the learned subspace (alignments 0.52–0.62 against 0.025 random,
  App. E, one run each).
- **Not that SimCLR or VICReg step for this reason.** Their stepwise rank
  growth on STL-10 is an observation (§6). Neither loss is analysed, and
  BYOL was not seen to step.
- **Not the positive-pair density ratio.** Γ and K_Γ are built from the
  model's kernel and the sample pairs. They are not K⁺ or the positive-pair
  Markov chain of [THEORY-007](THEORY-007.md), so this supports that account by analogy
  only. Whether K_Γ converges to K⁺-kernel PCA as n → ∞ is open.
- **Not a symmetric pair distribution.** Γ is symmetric because the loss
  was symmetrized, which is why the paper can apply it to two-tower pairs
  ([THEORY-009](THEORY-009.md)).
- **Not a claim about speed-ups.** App. G's proposals for faster training
  are untested, and they are machine-learning practice. They are not filed
  here.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md) (what sets the order and moment of acquisition).** An
  answer in part, for this loss and model class: the order is the
  eigenvalue order of Γ, and the moment is set by 1/γ_j and the log of the
  initial scale. It is the self-supervised instance of a mechanism the
  record holds for supervised deep linear networks ([THEORY-186](THEORY-186.md),
  [THEORY-187](THEORY-187.md)) and for the kernel regime ([THEORY-086](THEORY-086.md)). Unlike [THEORY-086](THEORY-086.md),
  where every eigenspace is fitted at once at its own rate, here each mode
  waits at an unstable equilibrium near zero, because the loss is
  invariant to f → Uf.
- **[THEORY-182](THEORY-182.md).** Karkada, Simon et al. ([LIT-855](../literature.d/LIT-855.md)) carry the same analysis
  to a quartic word2vec proxy. That account and this one share a mechanism
  and an author, and neither is a rival of the other.
- **[THEORY-007](THEORY-007.md).** The optimum-based account says which subspace is
  optimal. This one says which of the degenerate zero-loss optima a
  linearized model reaches, and in what order. The paper describes itself
  as completing HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)) in that way.
- **[QUESTION-052](../questions.d/QUESTION-052.md).** For a symmetrized loss on directed or cross-modal
  pairs, the operator that takes the top eigenspace's place is the
  symmetric part of the cross-correlation. That answers only for this loss.

## Note of 2026-10-19: Propositions 4.1, 4.3 and 5.1, re-derived

Let f(x) = Wx with W ∈ R^{d×D}, and let Γ have eigenpairs (γ_j, v_j),
γ_1 > … > γ_d > 0 and γ_d > γ_(d+1). The loss is
L(W) = ‖WΓWᵀ − I_d‖²_F, and gradient flow is
dW/dt = −4(WΓWᵀ − I)WΓ.

1. Alignment is kept. If W = U diag(s) V_dᵀ with U orthogonal and
   V_d = [v_1 … v_d], then WΓWᵀ = U diag(s_j²γ_j) Uᵀ and the gradient is
   4U diag((s_j²γ_j − 1)s_jγ_j) V_dᵀ, of the same form. So U stays fixed
   and ds_j/dt = 4γ_j s_j − 4γ_j² s_j³, each mode on its own.
2. With u_j = s_j^(−2), du_j/dt = −8γ_j u_j + 8γ_j², so
   s_j(t) = e^(4γ_j t)/√(s_j(0)^(−2) + (e^(8γ_j t) − 1)γ_j), which tends
   to γ_j^(−1/2) (eq. 10).
3. For s_j(0)²γ_j ≪ 1, mode j stays small until about
   τ_j = −log(s_j(0)²γ_j)/(8γ_j) (eq. 16) and then rises. With a common
   initial scale s_0, dτ/dγ = (log γ − 1 − log s_0^(−2))/(8γ²), which is
   negative whenever s_0²γ < e, so larger eigenvalues arrive first.
4. Minimum norm. Let AΓAᵀ = I_d, G = AAᵀ and Q = G^(−1/2)A, so QQᵀ = I_d
   and QΓQᵀ = G^(−1). Its eigenvalues θ_1 ≥ … ≥ θ_d are positive and, by
   Cauchy interlacing, θ_j ≤ γ_j. So ‖A‖²_F = tr G = Σ 1/θ_j ≥
   Σ_(j≤d) 1/γ_j, with equality only if the row space of Q is
   span(v_1 … v_d), which makes A = U diag(γ_j^(−1/2)) V_dᵀ. The top
   spectral solutions are exactly the minimum-norm zero-loss ones.
5. A fixed-kernel model is linear in its feature map, so 1–4 hold in
   feature space. The non-zero eigenvalues there are those of
   K_Γ = K̃^(−1/2) Z K̃^(−1/2) (Proposition 5.1), and the minimum-RKHS-norm
   solution is given by K_Γ's top eigenvectors.

From a generic small initialization, Simon et al. give only an informal
derivation that the flow follows the aligned trajectory (Result 4.6).
That is [QUESTION-tmpqtbzj](../questions.d/QUESTION-tmpqtbzj.md).
