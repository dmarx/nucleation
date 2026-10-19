---
number: 714
status: Read
formerly:
- NOTE-tmpl70rd
paper: LIT-1012
title: 'Noise Balance and Stationary Distribution of Stochastic Gradient Descent'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read from arXiv v2 (12 June 2025) through the PDF text layer, extracted
    without layout because of the two-column format: §§I–IV in full,
    including figure captions. The proofs in Appendix A were not checked.
date: '2026-10-13'
summary: >-
  SDE: dθ = −∇L dt + √(T C(θ)) dW, with T = η/S. With ℓ(u, w) =
  ℓ(λu, w/λ), d(‖u‖² − ‖w‖²)/dt = −T(uᵀC₁u − wᵀC₂w) (Theorem 1). The
  stationary point is Tr C(w) = Tr C(u). With weight decay γ the rate is
  TC₀ + γ (Corollary 2.1). Diagonal linear network ℓ = (Σᵢ ∏ₖ u_i^{(k)} x − y)²:
  sign coherence and balance for depth D > 1 (Theorem 3), exact stationary
  distribution (Theorem 4), collapse above T_c = β₂/α₃ for D = 1, tail
  ∝ v^{−5+3/(D+1)} independent of data.
---
<!-- inactive-ok-file: THEORY-209 THEORY-210 — Proposed; the accounts this reading bears on, open -->

# NOTE-714: Noise Balance and Stationary Distribution of Stochastic Gradient Descent

## Contribution

An exact statement of what minibatch noise does along a rescaling
symmetry, and the first stationary distribution of SGD solved for a model
with both depth and width. Earlier stationary distributions assumed
parameter-independent noise and came out Gibbs-like and ergodic. This one
does not.

## Key insight

Along a symmetry direction the noise has no component, so it cannot push
the parameters there directly. But the noise covariance depends on where
the parameters are, and through Itô's lemma that dependence produces a
deterministic drift along the symmetry. For a rescaling symmetry the drift
always points toward the point where the two layers' gradient noise is
equal. So SGD does three different things on the same flat valley. Gradient
descent stays where it started. Gradient descent with isotropic noise
wanders off along it. SGD slides to one particular point.

## Assumptions

- **The SDE model** (Eq. 1) with the exact minibatch covariance C(θ),
  valid to O(T³) per step for small learning rates.
- **Rescaling symmetry** ℓ(u, w, v, x) = ℓ(λu, w/λ, v, x) holding for
  every sample x, not only in expectation.
- **For the stationary distribution:** the diagonal linear network of
  Eq. 16 with scalar input. Results are conditioned on the effective width
  d, which depends on the initialization.

## Key results

- **Law of balance (Theorem 1).** d(‖u‖² − ‖w‖²)/dt = −T(uᵀC₁u − wᵀC₂w),
  with C₁ and C₂ positive semidefinite. A unique balancing rescaling λ*
  exists when the right side does not vanish.
- **Two balances.** The stationary point equates the noise traces,
  Tr_w C(w) = Tr_u C(u). The norm ratio satisfies
  λ⁴ = w*ᵀC₂w*/u*ᵀC₁u*, bounded by the extreme eigenvalues of C₁ and C₂
  (Eq. 7). The noise balance is exact; the norms balance only
  approximately (Fig. 2).
- **Full rank (Theorem 2).** For a two-layer ReLU network, C₁ and C₂ are
  full rank for every neuron that is ever active.
- **Weight decay.** With L2 strength γ the decay rate is TC₀ + γ: "when
  rescaling symmetry is present, the implicit bias of SGD is equivalent to
  weight decay".
- **Three dynamics on one valley (Figs. 1, 3, 7).** On ℓ = (uwx − y)²,
  GD conserves u² − w², GD with isotropic Gaussian noise diverges along the
  degenerate direction, and SGD decays to u² = w². The stationary
  distribution of the conserved charge is a delta for SGD and uniform for
  the Gibbs distribution, so the KL divergence between them is infinite.
- **Non-perturbative.** At stationarity SGD differs from GD by O(1)
  however small T is, because the t → ∞ and T → 0 limits do not commute.
  Not all solutions of equal loss are visited with equal probability, so
  ergodicity is lost.
- **Depth (Theorem 3).** At stationarity all subnetworks v_i share a sign
  ("sign coherence"). For D = 1 the ratios |v_i|/|v_j| are conserved; for
  D > 1 the differences |v_i|² − |v_j|² decay to zero.
- **Stationary distribution (Theorem 4, Eq. 18).** For D = 1, if
  T > T_c = β₂/α₃ (or (β₂ − γ)/α₃ with weight decay), the distribution
  collapses to v = 0 and nothing is learned. Below T_c the variance of v
  falls as T rises ("fluctuation inversion"). The tail is ∝ v^{−7/2} for
  D = 1 and v^{−5} as D → ∞, independent of data and hyperparameters.
- **Bias.** SGD estimates the minimizer β₂/β₁ only as T → 0. Its
  stationary distribution is not the Bayesian posterior.
- **Infinite depth.** The width-to-depth ratio enters only with 1/T,
  suggesting d·S/(D·η) = constant as a scaling relation.

## Claims

- That the law explains the edge-of-stability observation, through
  fluctuation inversion and the power-law tail. This is argued from the
  minimal model, not measured in a network at the edge of stability.
- That the minimal model's phenomena "exist uniquely in deep networks".
  This is shown for the diagonal linear network and illustrated with tanh
  networks.

## Concepts

- **Temperature:** T = η/S.
- **Noether charge:** the quantity a symmetry conserves under gradient
  flow, here ‖u‖² − ‖w‖².
- **Memory effect:** the stationary distribution depends on the
  initialization, for instance through the effective width.

## Connections

- **[LIT-1013](../literature.d/LIT-1013.md) (Neural Mechanics)** derives the same conservation law
  for gradient flow and an Itô forcing term for scale symmetry. This paper
  carries the Itô treatment through for rescale symmetry and solves for
  the stationary point.
- **[THEORY-209](../theory.d/THEORY-209.md) (Kunin et al. 2021, limiting dynamics)** assumes noise
  covariance proportional to the Hessian and independent of the
  parameters. Under that assumption the Itô drift vanishes, and the
  coordinate along a symmetry is frozen. This paper's result needs the
  parameter dependence [THEORY-209](../theory.d/THEORY-209.md) removes. The two agree on the image of
  the Hessian and differ on its null space.
- **[THEORY-210](../theory.d/THEORY-210.md)** quoted this paper, through the survey, as finding a
  distribution "different from predictions from a Langevin model". The
  comparison here is with gradient descent plus isotropic, full-rank
  noise. It is not with [THEORY-209](../theory.d/THEORY-209.md)'s Hessian-shaped noise.
- **[THEORY-108](../theory.d/THEORY-108.md)**'s temperature axis is this paper's T, with a phase
  transition in it for the minimal model.

## Bearing on the record

It supports [THEORY-211](../theory.d/THEORY-211.md), filed from this reading. It also settles how
[THEORY-209](../theory.d/THEORY-209.md) and [THEORY-210](../theory.d/THEORY-210.md) meet. Along symmetry directions, a converged
network is neither frozen nor diffusing: it is driven to a noise-balanced
point at a rate set by η/S, plus weight decay.

## Limitations

- **A minimal model.** The stationary distribution is solved for a
  diagonal linear network with scalar input. The law of balance is
  general, but the networks it is tested on are small and synthetic (a
  two-layer ReLU network on Gaussian data, toy and tanh models).
- **The SDE approximation.** It is valid for small learning rates, which
  is not where the non-perturbative effects are largest.
- **The proofs were not checked here.**

## Open questions

- Does a deep network trained on real data reach noise balance between
  layers in its limiting dynamics, at a rate scaling with η/S?
- Which other symmetries have a law of balance? Ziyin (2024) extends it to
  mirror symmetries; that paper is not held.

## Corrections

None.
