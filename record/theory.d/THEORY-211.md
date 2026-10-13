---
number: 211
status: Proposed
formerly:
- THEORY-tmpdsy58
promote_when: >-
  The law of balance measured in a deep network trained on real data,
  during its limiting dynamics. What would promote: for parameter groups
  related by a rescaling symmetry (adjacent layers through a ReLU, or the
  query and key matrices of attention), the difference of squared norms
  moving toward the value at which the groups' gradient-noise traces are
  equal, at a rate that scales with learning rate over batch size, with
  weight decay adding to it. That should hold from more than one
  initialization. What would refute it: in such a network at stationarity,
  the difference staying at its initial value, as under gradient flow, or
  diffusing without a preferred value, as under isotropic noise. A failure
  of the SDE approximation at the learning rates used would limit it, not
  refute it. More solvable toy models cannot settle it.
title: 'Along a rescaling symmetry, minibatch noise drives SGD to the point where the gradient noise of the two parameter groups balances, at a rate set by learning rate over batch size, so at stationarity SGD neither stays where gradient flow would leave it nor diffuses as isotropic noise would, and differs from gradient descent by a finite amount however small the noise'
version: 1
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
  above a critical temperature. Proposed: the theorem's proof was not
  checked here, and the tests are small synthetic networks.
---
<!-- inactive-ok-file: THEORY-209 THEORY-210 THEORY-108 QUESTION-080 — Proposed or Open; the accounts and question this one is set beside, open -->

# THEORY-211: Along a rescaling symmetry, minibatch noise drives SGD to the point where the gradient noise of the two parameter groups balances, at a rate set by learning rate over batch size, so at stationarity SGD neither stays where gradient flow would leave it nor diffuses as isotropic noise would, and differs from gradient descent by a finite amount however small the noise

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
