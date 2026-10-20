---
status: Active
title: 'For a reversible diffusion dX = −∇U dt + √2 dW in equilibrium, an eigenfunction ψ of its generator with eigenvalue −λ is closed in conditional mean with no memory: E[ψ(X_{t+s}) | the whole past] = e^{−λs}ψ(X_t), and so the same given ψ''s own past; but ψ(X_t) is a Markov process in its own right only when |∇ψ|² is a function of ψ, since otherwise its own path reveals a noise intensity that its present value does not fix'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpvqn3y. Nadler, Lafon, Coifman and Kevrekidis
    propose the slow eigenfunctions of the Langevin generator, which the
    α = 1/2 diffusion map estimates, as reaction coordinates for the coarse
    long-time dynamics, and they do not say in what sense such a
    coordinate is closed. The statement and its proof are the record's,
    written out step by step below. The proof uses only Itô's formula,
    Lévy's characterization of Brownian motion and the Markov property of
    solutions unique in law, all standard theorems. That meets the
    condition for Active under ADR-047 v2. The 2D Ornstein–Uhlenbeck check
    was run in the scratchpad.
tags:
- mathematics
- probabilistic-modeling
- complex-systems
date: '2026-10-20'
source:
- LIT-tmpg4fmr
answers:
- QUESTION-tmpxapb2
summary: >-
  The record's answer to what Nadler et al. ([LIT-tmpg4fmr](../literature.d/LIT-tmpg4fmr.md), read in [NOTE-tmpvqn3y](../notes.d/NOTE-tmpvqn3y.md))
  leave implicit when they call slow eigenfunctions reaction coordinates. Such
  a coordinate is exactly closed in its mean: its best prediction from the
  full state and from its own history coincide, with no memory term, and
  the Mori–Zwanzig memory and noise for it vanish under Mori's projection.
  It is closed in law only under a further condition. In the paper's
  examples the condition holds; the mixed Ornstein–Uhlenbeck eigenfunction
  x₁x₂ shows it can fail. This does not say that diffusion maps estimate
  the eigenfunctions well from finite data, or that a slow eigenfunction is
  the best coarse variable.
---
<!-- inactive-ok-file: THEORY-tmp3j6t7 THEORY-257 CLAIM-157 CLAIM-331 — Proposed; the α-family limit this reading's bridge rests on, and open criteria set beside this result, nothing here rests on their being settled -->
# THEORY-tmpvmmpz: For a reversible diffusion dX = −∇U dt + √2 dW in equilibrium, an eigenfunction ψ of its generator with eigenvalue −λ is closed in conditional mean with no memory: E[ψ(X_{t+s}) | the whole past] = e^{−λs}ψ(X_t), and so the same given ψ's own past; but ψ(X_t) is a Markov process in its own right only when |∇ψ|² is a function of ψ, since otherwise its own path reveals a noise intensity that its present value does not fix

## Source

Nadler, Lafon, Coifman and Kevrekidis (2006; arXiv 2005), [LIT-tmpg4fmr](../literature.d/LIT-tmpg4fmr.md), read
in full in [NOTE-tmpvqn3y](../notes.d/NOTE-tmpvqn3y.md). The paper supplies the setting: data sampled from the
equilibrium of the Langevin equation (2), ẋ = −∇U(x) + √2ẇ, and an α = 1/2
diffusion map whose small-ε generator is that equation's backward operator
(30), Δψ − ∇ψ·∇U, up to the factor ½ that [NOTE-tmpvqn3y](../notes.d/NOTE-tmpvqn3y.md) finds missing. It
proposes the leading eigenfunctions as reaction coordinates and as the
coarse description "at medium to long times, at which the fast coordinates
have equilibrated". The statement and proof below are the record's.

## What was actually shown

**Setting.** U: ℝⁿ → ℝ is smooth with ∫e^{−U} = 1, and μ = e^{−U}dx. X
solves dX = −∇U(X)dt + √2 dW, has a unique non-exploding strong solution
and is started in equilibrium, X₀ ~ μ, so it is stationary. F_t is the
filtration of (X₀, W). The generator is L = Δ − ∇U·∇, with Δ = ∇². Let
ψ ∈ C² satisfy Lψ = −λψ with λ > 0, and assume ψ ∈ L⁴(μ) and
|∇ψ| ∈ L⁴(μ). Write Y_t = ψ(X_t), h(x) = |∇ψ(x)|², and G_t = σ(Y_r : r ≤ t).

**Step 1. The conditional mean given the full state.** By Itô's formula,
d(e^{λt}Y_t) = e^{λt}(λψ + Lψ)(X_t)dt + e^{λt}√2∇ψ(X_t)·dW_t
= e^{λt}√2∇ψ(X_t)·dW_t. The integrand is square-integrable on [0, T]:
by stationarity, E∫₀ᵀ e^{2λs}·2h(X_s)ds = 2∫h dμ·∫₀ᵀe^{2λs}ds < ∞. So
e^{λt}Y_t is a martingale, and

  E[Y_{t+s} | F_t] = e^{−λs}Y_t.

**Step 2. No memory given ψ's own past.** G_t ⊆ F_t, so by the tower
property E[Y_{t+s} | G_t] = E[e^{−λs}Y_t | G_t] = e^{−λs}Y_t. The best
mean-square predictor of ψ's future from its own history uses only its
present value, linearly. Nothing is gained by adding the rest of the
state: the two predictors are equal. In Mori's form of the Mori–Zwanzig
decomposition, with the projection Pf = ⟨f, ψ⟩_μ ψ/‖ψ‖²_μ applied to the
evolution of observables, Lψ = −λψ lies in the range of P. So QLψ = 0, and
the memory and orthogonal-dynamics terms for ψ vanish identically.

**Step 3. The path of Y.** Let n(x) = ∇ψ(x)/|∇ψ(x)| where ∇ψ ≠ 0, and a
fixed unit vector elsewhere, and B_t = ∫₀ᵗ n(X_s)·dW_s. B is a continuous
martingale with ⟨B⟩_t = t, so it is a Brownian motion by Lévy's
characterization. Then

  dY_t = −λY_t dt + √(2h(X_t)) dB_t,  ⟨Y⟩_t = 2∫₀ᵗ h(X_s)ds.

**Step 4. When Y is Markov.** If h = g∘ψ μ-almost everywhere for some g,
then Y is a weak solution of the one-dimensional equation
dY = −λY dt + √(2g(Y)) dB. Where that equation has uniqueness in law (for
instance when √g is locally Lipschitz and non-explosive), its solutions
are strong Markov processes, so Y is Markov.

**Step 5. When it is not.** The quadratic variation ⟨Y⟩ is a functional
of Y's path, so h(X_t) = lim_{δ↓0}(⟨Y⟩_t − ⟨Y⟩_{t−δ})/2δ is
G_t-measurable. Now expand the squared increment:
E[(Y_{t+s} − Y_t)² | G_t] = 2E[∫_t^{t+s}h(X_r)dr | G_t] + R_s, where R_s
collects the drift terms. E|R_s| ≤ E[(λ∫Y)²] + 2(E[(λ∫Y)²]E[M²])^{1/2}
= O(s^{3/2}), using ψ ∈ L²(μ) and h ∈ L¹(μ). By stationarity and path
continuity, with h ∈ L²(μ) for uniform integrability,
(1/s)E[∫_t^{t+s}h dr | G_t] → h(X_t) in L¹. So

  (1/s)E[(Y_{t+s} − Y_t)² | G_t] → 2h(X_t)  in L¹.

If Y were Markov in its own filtration, then since ψ ∈ L⁴(μ) and
E[Y_{t+s} | G_t] = e^{−λs}Y_t, the left side would be a function of Y_t
for each s, and so would its L¹ limit. Hence h(X_t) would be
σ(Y_t)-measurable, i.e. h = g∘ψ μ-a.e. Contrapositively, if |∇ψ|² is not
a.e. a function of ψ, then Y is not Markov. Its own past predicts the size
of its next fluctuation better than its present does.

**Checked numerically.** Take the 2D Ornstein–Uhlenbeck process
U = x₁²/2τ₁ + x₂²/2τ₂ with τ₁ = 1 and τ₂ = 1/4, the paper's §5.2 with
these values. It was simulated by Euler–Maruyama, dt = 10⁻³, for 2 × 10⁶
steps, and three eigenfunctions were examined at lag s = 0.2:

| ψ | λ | \|∇ψ\|² | slope of E[Y_{t+s} \| Y_t] vs e^{−λs} | coefficient on Y_{t−s} in the mean | R² for the squared residual: present, + past |
|---|---|---|---|---|---|
| x₁ | 1 | 1 | 0.821 vs 0.819 | −0.008 | 0.000, 0.001 |
| x₁² − τ₁ | 2 | 4(ψ + τ₁) | 0.660 vs 0.670 | +0.017 | 0.118, 0.118 |
| x₁x₂ | 5 | x₁² + x₂² | 0.370 vs 0.368 | −0.003 | 0.025, 0.032 |

The mean is closed in all three cases. For x₁x₂ only, the past adds to
the prediction of the squared residual, as Step 5 requires.

What could have failed: an eigenfunction's conditional mean could have
depended on unresolved coordinates through the noise. Step 1 shows it
cannot, because the noise term is a martingale. And closure in the mean
could have implied closure in law. x₁x₂ shows that it does not.

## What this does not say

- **Not that diffusion maps recover the eigenfunctions.** That rests on the
  α = 1/2 limit ([THEORY-tmp3j6t7](THEORY-tmp3j6t7.md), Proposed; Nadler et al.'s expansion is
  formal) and on finite-sample convergence, which neither paper proves.
  [NOTE-tmpvqn3y](../notes.d/NOTE-tmpvqn3y.md) found that, from equilibrium samples of a double well, the
  eigenfunction was recovered well and the slow eigenvalue was not.
- **Not that the slowest eigenfunction is the best coarse variable.**
  Exact closure of the mean holds for every eigenfunction, slow or fast.
  Slowness matters only for how much of the dynamics the variable carries
  at long times.
- **Not for non-reversible or non-equilibrium dynamics.** Steps 1–5 use
  only Lψ = −λψ, the martingale property and stationarity. For a
  non-reversible generator, eigenfunctions are complex and may lack a
  real eigenbasis, which this entry does not treat. The data-driven link
  needs reversibility as well.
- **Not that a closed mean makes a level.** Under [THEORY-257](THEORY-257.md)'s dynamical
  independence the coarse variable's own past must exhaust what the micro
  past says about its future in law, not only in mean. Step 5 shows the two
  come apart.
- **Not anything about finite collections of eigenfunctions.** The
  argument covers one ψ. The vector (ψ₁, …, ψ_k) is closed in mean
  componentwise. It is Markov when the matrix ⟨∇ψ_i, ∇ψ_j⟩ is a function
  of the vector, by the same argument; that matrix version is not written
  out here.

## Connections

- **[QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md): answers in part.** For coarse variables that are
  generator eigenfunctions of a reversible diffusion, the memory term of
  the mean dynamics is exactly zero, so no augmentation is needed for the
  mean. What can carry memory is the second moment, through the noise
  intensity |∇ψ|². The natural augmentation is then the single coordinate
  h(X) = |∇ψ(X)|², which ψ's own path reveals. This is the converse shape
  of [CLAIM-tmpmonrv](../claims.d/CLAIM-tmpmonrv.md): there zero memory did not imply closure, and here
  closure of the mean does not imply closure in law.
- **[THEORY-257](THEORY-257.md).** The criterion conditions on the coarse variable's own
  history, in law. An eigenfunction that fails Step 4's condition fails
  it. Even its own past is not summarized by its present, though its mean
  is.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** In a reversible system the slow coarse variables that
  diffusion maps find are generator eigenfunctions, and they are closed in
  mean at every timescale, not only at long times. What separates the
  timescales is the decay rate λ, not any degree of closure.
- **[CLAIM-tmpkoi6k](../claims.d/CLAIM-tmpkoi6k.md).** An eigenfunction is a function of the whole state, not
  of a block, and its mean closes exactly. That is another instance of
  closure without a block, in the mean.
- **[CLAIM-157](../claims.d/CLAIM-157.md) and [CLAIM-164](../claims.d/CLAIM-164.md).** Nothing here uses a gap. A gap decides
  which eigenfunctions dominate after time t. It does not decide which are
  closed.
