---
number: 229
status: Proposed
formerly:
- THEORY-tmpbaoyn
promote_when: >-
  A formal proof of Simon et al.'s Result 4.6 (generic small initialization
  follows the aligned trajectory as the scale goes to zero), which the
  paper derives only informally, or a proof of the same stepwise order for
  a second spectral SSL loss on a linear or fixed-kernel model. Either
  would settle the account in the regime it claims. It is refuted by a
  linear or fixed-kernel case of this loss, from vanishing generic
  initialization with distinct positive eigenvalues, that does not reach
  the minimum-norm solution or learns a lower mode first. What cannot
  settle it: more ResNet runs showing stepwise rank growth, since the
  theory does not cover a moving tangent kernel and the paper's own
  initial-NTK predictions for ResNets are poor.
title: "For a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from small initialization learns the top eigenvectors of the pairs' symmetrized cross-correlation one at a time, in order of eigenvalue, and ends at the minimum-norm zero-loss solution, kernel PCA"
version: 1
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
<!-- inactive-ok-file: THEORY-182 THEORY-186 THEORY-187 QUESTION-039 QUESTION-052 — Proposed or Open, or Active and cited for context; this account rests on none of them -->

# THEORY-229: For a symmetrized Barlow Twins loss on a linear or fixed-kernel model, gradient flow from small initialization learns the top eigenvectors of the pairs' symmetrized cross-correlation one at a time, in order of eigenvalue, and ends at the minimum-norm zero-loss solution, kernel PCA

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
