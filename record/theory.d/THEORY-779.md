---
number: 779
status: Active
formerly:
- THEORY-tmpopk8o
title: "In Kunin et al.'s underdamped Langevin model of SGD with momentum on linear regression, with gradient-noise covariance σ²H independent of the parameters, the stationary state is Gaussian with parameter covariance ησ²H(H + λI)⁻¹/(2S(1 − β)) and velocity covariance σ²H/(S(1 − β²)): for small weight decay it spreads equally along every nonzero Hessian direction and not along the null space, each Hessian eigenmode is a damped oscillator with damping ratio (1 − β)/√(2η(1 + β)(ρ + λ)), and the expected squared step is η²σ² tr(H)/(S(1 − β²))"
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Split from THEORY-209 by the promotion audit (batch 062, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-770's split from THEORY-673.
    THEORY-209 bundled Kunin et al.'s exact linear-regression result with
    the claim that converged deep networks are in that state. This THEORY
    holds the model result, re-derived in the review; THEORY-209 keeps the
    deep-network claim and its promote_when, and extends this one.
tags:
- learning-theory
- loss-landscapes
- thermodynamics
- anthology-candidate
date: '2026-10-20'
source:
- LIT-1011
summary: >-
  Kunin et al. (2021), [LIT-1011](../literature.d/LIT-1011.md), §§4–6 and App. G, read in [NOTE-711](../notes.d/NOTE-711.md); the
  stationary moments re-derived by the promotion audit. An exact result
  for a model: Σ ∝ H constant and a quadratic loss are assumptions, and
  nothing here says a deep network meets them. The probability current is
  nonzero but reversible: under the model's assumptions the stationary
  process is time-reversible once velocities are flipped, so it is
  "broken detailed balance" only in the paper's sense, a nonzero current.
extended_by:
- THEORY-209
---
<!-- inactive-ok-file: THEORY-209 THEORY-673 — Proposed; the account this one is split from, and the earlier split it follows -->

# THEORY-779: In Kunin et al.'s underdamped Langevin model of SGD with momentum on linear regression, with gradient-noise covariance σ²H independent of the parameters, the stationary state is Gaussian with parameter covariance ησ²H(H + λI)⁻¹/(2S(1 − β)) and velocity covariance σ²H/(S(1 − β²)): for small weight decay it spreads equally along every nonzero Hessian direction and not along the null space, each Hessian eigenmode is a damped oscillator with damping ratio (1 − β)/√(2η(1 + β)(ρ + λ)), and the expected squared step is η²σ² tr(H)/(S(1 − β²))

## Source

Kunin, Sagastuy-Brena, Gillespie, Margalit, Tanaka, Ganguli & Yamins (2021),
[LIT-1011](../literature.d/LIT-1011.md), arXiv 2107.09133v4: §4 (the modified equation, Eqs. 2–5), §5
(linear regression, Eqs. 7–8, Assumption 3), §6 (the modified loss and
current, Eqs. 13–14) and App. G (Eq. 18). Read in [NOTE-711](../notes.d/NOTE-711.md), and re-read
from the PDF by the promotion audit (batch 062), which re-derived the
stationary moments.

## What was actually shown

**The model.** SGD with momentum β, learning rate η, batch size S and
weight decay λ updates v_{k+1} = βv_k − g(θ_k) − λθ_k and
θ_{k+1} = θ_k + ηv_{k+1}. Kunin et al. model it by the modified equation

(η/2)(1 + β)θ̈ + (1 − β)θ̇ + λθ = −g(θ) + √(η/S) √Σ ξ(t).

For linear regression g = Hθ − b. Assumption 3 takes the gradient-noise
covariance to be constant and equal to σ²H. In phase space this is an
Ornstein–Uhlenbeck process with inverse temperature κ = S(1 − β²).

**The derivation.** H, K = H + λI and Σ commute, so in H's eigenbasis
each mode with Hessian eigenvalue ρ is a damped oscillator. Write
a = 2/(η(1 + β)) and c = 2(1 − β)/(η(1 + β)). Then
q̈ = −a(ρ + λ)q − c q̇ + noise, with noise intensity 2cσ²ρ/κ. Its
stationary moments are ⟨v²⟩ = σ²ρ/κ, ⟨q²⟩ = ⟨v²⟩/(a(ρ + λ)) and
⟨qv⟩ = 0. So the stationary state is Gaussian:

- Cov(θ) = ησ²H(H + λI)⁻¹/(2S(1 − β)).
- Cov(v) = σ²H/(S(1 − β²)).

This is the paper's Gibbs distribution exp(−κΨ) on a modified loss, whose
curvature in θ is proportional to H⁻¹(H + λI)/(η(1 + β)) (Eq. 15).

**What follows.**

- **Isotropy.** For λ → 0, Cov(θ) is ησ²/(2S(1 − β)) times the
  projector on H's column space. The run spreads equally along sharp and
  flat-but-nonzero directions, and not at all along the null space. A
  Gibbs distribution on the training loss would spread as (H + λI)⁻¹.
- **Damping.** Each mode's damping ratio is
  c/(2√(a(ρ + λ))) = (1 − β)/√(2η(1 + β)(ρ + λ)). A larger learning
  rate makes modes underdamped.
- **Speed.** The expected squared step is
  E‖θ_{k+1} − θ_k‖² = η² tr Cov(v) = η²σ² tr(H)/(S(1 − β²)), which is
  Eq. 18.
- **Current.** The stationary probability current is
  J = (v, −a(H + λI)(θ − μ))p_ss (Eq. 17). It is nonzero, so the run
  circulates in each eigen-plane at a rate set by its eigenvalue.

**Checks.** The audit used a four-dimensional H with eigenvalues
(3, 1, 0.2, 0) in a random basis, σ² = 0.5, and three settings of
(η, β, S, λ). The continuous Lyapunov equation reproduces the paper's
covariance κ⁻¹U⁻¹ to 10⁻¹³, with no cross-covariance between θ and v.
The exact stationary covariance of the discrete recursion agrees with the
model to O(ηρ): 0.8% at η = 0.01, and up to 8% at η = 0.05, ρ = 3. The
step size agrees to within 0.6% and 6% at the same two settings.

## What this does not say

- **That a deep network is in this state.** Σ ∝ H is derived for a noisy
  linear teacher, not measured. The end-of-training Hessian of a deep
  network has negative eigenvalues, which a quadratic loss excludes.
  Whether converged networks behave this way is [THEORY-209](THEORY-209.md)'s question,
  with its own promote_when.
- **That the state is out of equilibrium in the usual sense.** The paper
  calls it "broken detailed balance" because the current is nonzero
  (§6). Under Assumption 3 that current is the reversible, Hamiltonian
  part. The stationary autocovariance C(t) satisfies C(t) = εC(t)ᵀε with
  ε = diag(I, −I), to machine precision, so the process is time-reversible
  once velocities are flipped. Each eigenmode is an equilibrium oscillator
  at its own temperature σ²ρ/κ. Genuine irreversibility needs a Σ that does
  not commute with H. For a random Σ the same check fails by 4 × 10⁻³.
- **Anything about the null space beyond "no spread".** With Σ constant,
  noise and drift both vanish there. With Σ depending on the parameters,
  symmetry directions are driven to balance ([THEORY-211](THEORY-211.md)).
- **The discrete process exactly.** The modified equation is accurate to
  O(ηρ). At large ηρ the discrete stationary covariance departs from it.
