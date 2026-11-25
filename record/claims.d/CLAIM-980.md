---
number: 980
status: Proposed
formerly:
- CLAIM-tmpllgpb
title: 'VAR(1) aggregate dependence of order ε²'
statement: >-
  In a stable linear Gaussian VAR(1) the dynamical dependence of a linear
  aggregate Y = LX lies between ½ log det(I + G⁻¹ LA Σ_|L AᵀLᵀ) and the same
  with the stationary Π_|L for the noise Σ_|L, so for a nearly decomposable
  A = A* + εC the sum over a block has dependence of exact order ε² when the
  block's columns have equal sums, with a constant that grows as the slow
  gap closes, and a floor that neither ε → 0 nor a wider fast gap removes
  when they do not
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable VAR(1) with Σ ≻ 0 and a full-rank L
  whose dynamical dependence falls outside the two bounds; or a
  block-diagonal stable A* whose block has equal column sums and for which
  T(ε)/ε² is unbounded as ε → 0; or one whose block has unequal column
  sums and for which T(ε) → 0 as ε → 0. A system in which the floor is
  small does not defeat it; the claim says the floor is positive, not
  large.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-221
grounds:
- THEORY-733
- CASE-381
corroborates:
- CLAIM-390
complements:
- CLAIM-386
summary: >-
  Derived for [LEAD-178](../leads.d/LEAD-178.md) and checked with numpy from exact stationary
  covariances (scratch/studies/lead-178/, 57 pytest checks; the study is
  [CASE-381](../cases.d/CASE-381.md)). For linear Gaussian VAR(1) at the Barnett–Seth one-step
  horizon it gives both results [QUESTION-221](../questions.d/QUESTION-221.md) allows: a bound of order ε²
  when the block's aggregate is closed under the block's own dynamics, and
  a nearly decomposable family with a floor when it is not. The longer
  horizon the question also asks for is not covered, so it bears on the
  question rather than answering it.
  The bound's upper half, for a block's full state, is [CLAIM-390](CLAIM-390.md)'s; the
  lower half and the aggregate are new. The closure condition for the sum
  is [CLAIM-386](CLAIM-386.md)'s equal column sums. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account whose quantity this bounds, nothing here rests on its being settled -->
<!-- inactive-ok-file: CASE-381 — new; the numerical study filed with this claim -->
<!-- inactive-ok-file: CLAIM-925 — Proposed; the filter it describes is the one used here, nothing rests on it -->

# CLAIM-980: VAR(1) aggregate dependence of order ε²

## The claim

**Setting.** X_t = AX_{t−1} + e_t, A stable, e_t ~ N(0, Σ) independent,
Σ ≻ 0, and an aggregate Y = LX with L of full row rank m, observed
without noise. Dynamical dependence is the transfer entropy
T(X → Y) = ½ log det Var(Y_t | Y⁻) / det Var(Y_t | X⁻) ([THEORY-257](../theory.d/THEORY-257.md),
[THEORY-733](../theory.d/THEORY-733.md)), and Var(Y_t | X⁻) = G := LΣLᵀ. Write Π for the stationary
covariance, Π_|L = Π − ΠLᵀ(LΠLᵀ)⁻¹LΠ = Cov(X | LX), and
Σ_|L = Σ − ΣLᵀG⁻¹LΣ = Cov(e | Le).

**1. The identity.** Since e_t is independent of the past,
E[Y_t | Y⁻] = LA E[X_{t−1} | Y⁻] and

Var(Y_t | Y⁻) = G + LA P AᵀLᵀ, P := Cov(X_{t−1} | Y_{t−1}, Y_{t−2}, …),

the steady error of the noise-free Kalman filter ([CLAIM-925](CLAIM-925.md)'s filter).

**2. The sandwich.** Conditioning on more cannot enlarge a Gaussian
conditional covariance. Adding X_{t−2}, X_{t−3}, … to the conditioning
set leaves Cov(e_{t−1} | Le_{t−1}), and dropping all but Y_{t−1} leaves
Cov(X_{t−1} | Y_{t−1}). So Σ_|L ⪯ P ⪯ Π_|L, and since log det is monotone,

½ log det(I + G⁻¹ LA Σ_|L AᵀLᵀ) ≤ T(X → Y) ≤ ½ log det(I + G⁻¹ LA Π_|L AᵀLᵀ).

The upper bound is the dependence measured with one lag of Y. With L the
projection onto a block it is [CLAIM-390](CLAIM-390.md)'s bound.

**3. Only the closure defect enters.** LΣ_|L = 0 and LΠ_|L = 0, so LA can
be replaced in both bounds by D = LA − BL for any m × m matrix B. The null
space of Σ_|L is the span of Lᵀ, so the lower bound is zero iff
LA = BL for some B. That re-derives [THEORY-733](../theory.d/THEORY-733.md)'s condition for VAR(1):
T = 0 iff Y is closed, and otherwise T is at least the lower bound.

**4. Nearly decomposable systems.** Let A = A* + εC with A* block-diagonal
and stable, and let L be supported on one block I.

- *Closed at ε = 0* (LA*_I = BL; for the plain sum, every column of A*_I
  has the same sum, [CLAIM-386](CLAIM-386.md)'s condition; for weights w, w a left
  eigenvector of A*_I). Then D = εLC and

  ½ log det(I + ε² G⁻¹ LC Σ_|L CᵀLᵀ) ≤ T ≤ ½ log det(I + ε² G⁻¹ LC Π_|L(ε) CᵀLᵀ).

  The lower constant depends on the noise alone; the upper one on the
  noise and the stationary covariance, which tends to its ε = 0 value. So
  T = Θ(ε²) whenever LCΣ_|L ≠ 0, which holds for generic coupling. For a
  scalar aggregate and diagonalizable A = VΛV⁻¹, ‖Π‖ ≤ κ(V)²‖Σ‖/(1 − ρ(A)²)
  gives the explicit bound

  T ≤ ε² ‖LC‖² κ(V)² ‖Σ‖ / (2G(1 − ρ(A)²)),

  of order ε² over the slow gap 1 − ρ(A). Where the slow gap is itself
  proportional to ε, as in Simon and Ando's scaling, this is first order.
- *Not closed at ε = 0* (unequal column sums for the sum). The lower
  bound at ε = 0, ½ log det(I + G⁻¹ LA* Σ_|L A*ᵀLᵀ), is positive and
  continuous in ε, so T stays above it as ε → 0. This is a nearly
  decomposable family with dependence bounded away from zero. The floor
  depends on A* only through LA*_I. Making the block's fast eigenvalues
  zero leaves LA*_I = λ₁(Lr₁)u₁ᵀ, still not a multiple of L, so the
  floor survives an arbitrarily wide fast gap. Noise re-excites the fast
  modes at every step, so the aggregate is at every step a noisy reading
  of the slow mode; the transient that Simon and Ando's argument waits
  out never ends.

**The check** ([CASE-381](../cases.d/CASE-381.md)). The sandwich held on all 600 items. With
equal column sums, T was zero to 10⁻¹⁶ at ε = 0 and T/ε² settled between
0.026 and 0.59 by ε = 0.025, inside its two constants. With unequal sums,
T at ε = 0 was between 6.7 × 10⁻⁴ and 0.034 nats, and T(ε) − T(0) was
first order. Shrinking the fast eigenvalues to zero left the floor's
smallest value at 1.6 × 10⁻³. With the slow gap 0.3, 0.1, 0.03 and 0.01,
the median T/ε² was 0.18, 0.26, 0.67 and 1.6 while the lower constant
stayed at 0.14. With the slow gap 2ε, T/ε settled near 0.009. The scalar
bound held on 250 items, with T at most 0.14 of it.

## What it does not say

- **Not beyond one step.** The horizon is Barnett and Seth's: one step,
  given the whole past. A dependence over a longer horizon, which
  [QUESTION-221](../questions.d/QUESTION-221.md) also asks for, was not bounded.
- **Not that a block's sum is the wrong aggregate.** The floor is a
  property of the sum over a block with unequal column sums. The same
  block aggregated by its left Perron vector is closed, and its
  dependence is of order ε². Which aggregate counts as the block's is not
  settled here.
- **Not that the floor is large.** In the study it was a few
  hundredths of a nat at most. It is positive, and does not shrink with ε
  or the fast gap.
- **Not a uniform rate in the gap.** The ε² constant grows as the slow
  gap closes; the measured growth was slower than 1/gap over the range
  run, and the scalar bound's 1/(1 − ρ²) is not shown tight.
- **Not beyond linear Gaussian VAR(1).** Markov chains ([NOTE-1030](../notes.d/NOTE-1030.md)'s open
  target) and nonlinear systems are untouched.
