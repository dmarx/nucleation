---
number: 211
status: Active
formerly:
- THEORY-tmpdsy58
title: 'In the stochastic-differential-equation model of SGD, with a gradient-noise covariance that depends on the parameters, minibatch noise drives the difference of squared norms along a rescaling symmetry, at a rate proportional to learning rate over batch size, to the point on the symmetry orbit where the gradient-noise traces of the two parameter groups are equal, whenever both groups carry noise; so at stationarity SGD neither keeps the difference fixed, as gradient flow does, nor lets it diffuse, as isotropic noise does, and differs from gradient descent by a finite amount however small the noise'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-211 (batch 027,
    ADR-047). The title now names the model the law of balance is proved in,
    the SDE model of SGD with parameter-dependent noise, and the condition that
    both groups carry noise. NOTE-714 did not check the paper's proofs; the
    law, the restoring drift along the orbit and the contrasts with gradient
    flow and isotropic noise are re-derived in the note of 2026-10-19 below
    (ADR-047 v2). The promote_when asked for the law measured in a deep
    network on real data, which the body disclaims. It moves, unchanged, to
    QUESTION-164.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 066, ADR-047 v4) filed
    THEORY-790 as a Proposed THEORY that extends this one, to carry
    what the narrowing dropped: the law of balance in deep networks
    trained on real data, which the authors present as general. This
    entry's status and title are unchanged.
tags:
- learning-theory
- loss-landscapes
- thermodynamics
- anthology-candidate
date: '2026-10-13'
source:
- LIT-1012
- LIT-1013
answers:
- QUESTION-069
- QUESTION-080
summary: >-
  Ziyin, Li & Ueda ([LIT-1012](../literature.d/LIT-1012.md), read in [NOTE-714](../notes.d/NOTE-714.md)), with the gradient
  flow conservation law and the Itô term from Neural Mechanics
  ([LIT-1013](../literature.d/LIT-1013.md)). If ℓ(u, w) = ℓ(λu, w/λ) for every sample, then under the
  SDE model of SGD d(‖u‖² − ‖w‖²)/dt = −T(uᵀC₁u − wᵀC₂w), with T = η/S. The
  noise has no component along the symmetry, but its dependence on the
  parameters produces a deterministic drift through Itô's lemma. The drift
  points to the noise-balanced point, and weight decay adds to its rate.
  In a diagonal linear network the stationary distribution follows exactly:
  it is non-ergodic, has a memory of initialization, and collapses to zero
  above a critical temperature. The law is re-derived here (2026-10-19)
  within the SDE model; the tests are small synthetic networks, and
  whether it holds in deep networks on real data is QUESTION-164.
supports:
- CLAIM-093
extended_by:
- THEORY-790
---
<!-- inactive-ok-file: THEORY-790 — Proposed; the wider claim this account was narrowed from, which extends it and is cited as open -->
<!-- inactive-ok-file: THEORY-209 THEORY-210 THEORY-108 QUESTION-080 — Proposed or Open; the accounts and question this one is set beside, open -->

# THEORY-211: In the stochastic-differential-equation model of SGD, with a gradient-noise covariance that depends on the parameters, minibatch noise drives the difference of squared norms along a rescaling symmetry, at a rate proportional to learning rate over batch size, to the point on the symmetry orbit where the gradient-noise traces of the two parameter groups are equal, whenever both groups carry noise; so at stationarity SGD neither keeps the difference fixed, as gradient flow does, nor lets it diffuse, as isotropic noise does, and differs from gradient descent by a finite amount however small the noise

## Source

Ziyin, Li & Ueda (2023; v2 2025), [LIT-1012](../literature.d/LIT-1012.md), read in [NOTE-714](../notes.d/NOTE-714.md):
§§I–IV, with Appendix A's proofs unchecked. Kunin et al. (2021), *Neural
Mechanics*, [LIT-1013](../literature.d/LIT-1013.md), read in [NOTE-713](../notes.d/NOTE-713.md), for the conservation law
under gradient flow and the noise's orthogonality to symmetry generators.

## The claim

**Three dynamics on one flat valley.** Take a loss with a rescaling
symmetry, as at every ReLU neuron and between attention's query and key
matrices. Under gradient flow, ‖u‖² − ‖w‖² is conserved (Neural
Mechanics, Theorem 1). Under gradient descent with isotropic Gaussian
noise, it diffuses without bound along the degenerate direction. Under
SGD, it decays to a fixed value (Ziyin et al., Figs. 1, 3, 7).

**The mechanism.** Minibatch gradients obey the symmetry, so the noise has
no component along the generator (Neural Mechanics, §5). The noise
covariance still depends on the parameters. Through Itô's lemma that
dependence gives the symmetry coordinate a deterministic drift:

d(‖u‖² − ‖w‖²)/dt = −T(uᵀC₁u − wᵀC₂w),   T = η/S

(Ziyin et al., Theorem 1). Its stationary point equates the two groups'
gradient-noise traces, and fixes a norm ratio. With weight decay γ the
rate becomes TC₀ + γ. For two-layer ReLU networks the noise matrices are
full rank for every live neuron, so the drift does not vanish (Theorem 2).

**What follows at stationarity.**

- **Not perturbative.** SGD differs from gradient descent by O(1),
  because the long-time and small-noise limits do not commute.
- **Not ergodic.** Equal-loss solutions are not visited equally, and the
  stationary distribution keeps a memory of the initialization.
- **Not Gibbs.** In a diagonal linear network the stationary distribution
  is solved exactly. It collapses to zero above a critical temperature
  T_c, its variance falls as T rises, and its tail depends on depth alone.

## What it bears on

- **[THEORY-209](THEORY-209.md)**, the limiting dynamics, assumes noise covariance
  proportional to the Hessian and independent of the parameters. That
  assumption removes the Itô drift, so in [THEORY-209](THEORY-209.md)'s model the coordinate
  along a symmetry is frozen. This account says it is driven to a balance.
  The two agree on the Hessian's image and differ on its null space, and
  the difference traces to that one assumption.
- **[THEORY-210](THEORY-210.md)** says the position along a symmetry orbit is set by
  initialization and optimizer, not by the loss. This account gives the
  mechanism for rescaling symmetry. The optimizer's temperature sets where
  along the orbit SGD ends up, and the initialization sets which
  stationary distribution it reaches.
- **[QUESTION-069](../questions.d/QUESTION-069.md).** It is a mechanism on the "regime" side. Two networks
  related by a rescaling are equally good, but SGD at a given T prefers one
  of them.
- **[QUESTION-080](../questions.d/QUESTION-080.md).** Motion along symmetry directions changes no function,
  so it is one way the parameters can keep moving while the features stay
  fixed.

## What this does not say

- It does not establish the law in a deep network trained on real data.
  The evidence is a small synthetic ReLU network, toy models and tanh
  models.
- It does not cover symmetries other than rescaling. Scale and
  translation have their own forms (Neural Mechanics), and mirror
  symmetries are treated in Ziyin (2024), which is not held.
- It does not say the norms balance exactly. The noise balances exactly,
  and the norms only approximately.
- It does not instruct. Using the effect for training belongs to the
  anthology.

## Note of 2026-10-19: the law of balance re-derived

Carried out for the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md) v2). Let every
per-sample loss satisfy ℓ(λu, w/λ, ·) = ℓ(u, w, ·) for λ > 0, so that
uᵀ∇_uℓ − wᵀ∇_wℓ = 0 sample by sample. Model SGD as
dθ = −∇L dt + √(TΣ(θ)) dW with T = η/S, and let J = ‖u‖² − ‖w‖².

1. **No drift from the loss.** ∇Jᵀ(−∇L) = −2(uᵀ∇_uL − wᵀ∇_wL) = 0.
2. **No noise along J.** Every per-sample gradient g has
   ∇Jᵀg = 2(uᵀg_u − wᵀg_w) = 0, so ∇JᵀΣ∇J = 0.
3. **The Itô term.** ½T tr(Σ∇²J) = T(tr Σ_u − tr Σ_w), the difference of the
   two groups' gradient-noise traces. Locally ℓ depends on (u, w) through
   M = uwᵀ. With A = ∂ℓ/∂M per sample, g_u = Aw and g_w = Aᵀu, so the traces
   are wᵀC₂w and uᵀC₁u with C₁ = E[(A − Ā)(A − Ā)ᵀ] and
   C₂ = E[(A − Ā)ᵀ(A − Ā)]. Hence dJ/dt = −T(uᵀC₁u − wᵀC₂w).
4. **Restoring along the orbit.** On the orbit (λu, w/λ) the product M,
   and so C₁ and C₂, is fixed, and the drift is −T(λ²a − λ⁻²b) with
   a = uᵀC₁u and b = wᵀC₂w. When a and b are positive, J is driven to the
   unique balanced point λ⁴ = b/a, at a rate proportional to T.
5. **Contrasts.** With T = 0, J is conserved. Under isotropic noise σ²I,
   J receives noise of variance 4σ²(‖u‖² + ‖w‖²) and only a constant Itô
   drift, so it diffuses.
6. **A finite difference.** For any T > 0 the balance is reached on a time
   scale of order 1/T, while gradient descent keeps the initial J, so the
   long-time and small-noise limits do not commute.
7. **Weight decay.** (γ/2)(‖u‖² + ‖w‖²) adds −2γJ to the drift.

Step 4 assumes the product has stopped moving, that is, stationarity of the
loss-reducing motion. While M still moves, step 3 gives the drift but not
convergence.

## Note of 2026-10-20: the wider claim filed separately

When this THEORY was narrowed to what its source showed, the wider claim
it had stated was left with nowhere to go but this body and a QUESTION.
Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now its own Proposed THEORY, [THEORY-790](THEORY-790.md), which extends
this one: the law of balance in deep networks trained on real data, which the authors present as general. This entry is that THEORY's evidence and is not
changed by it.
