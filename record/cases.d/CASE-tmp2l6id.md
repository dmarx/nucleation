---
status: Proposed
title: "Dynamical dependence of block aggregates in nearly decomposable linear Gaussian VAR(1) models, computed exactly: the two-sided bound held on 600 items, a block sum with equal column sums had dependence of order ε², one with unequal sums kept a floor as ε → 0 and as the fast eigenvalues went to zero, and with the slow gap proportional to ε the order fell to first"
version: 1
standing: documented
kind: executed-study
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-11-22'
bears_on:
- QUESTION-221
illustrates:
- CLAIM-tmpllgpb
line:
- distributed-agency
- formal-apparatus
summary: >-
  Run on 2026-11-22 for [LEAD-178](../leads.d/LEAD-178.md) (scratch/studies/lead-178/, on the branch
  claude/lead-178-var1-dependence). Every number comes from exact
  stationary covariances and the steady noise-free Kalman filter, with
  numpy; nothing is simulated, and 57 pytest checks pass. It checks
  [CLAIM-tmpllgpb](../claims.d/CLAIM-tmpllgpb.md)'s two-sided bound and its consequences for nearly
  decomposable systems. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpllgpb — new; the claim this study checks -->

# CASE-tmp2l6id: Dynamical dependence of block aggregates in nearly decomposable linear Gaussian VAR(1) models, computed exactly: the two-sided bound held on 600 items, a block sum with equal column sums had dependence of order ε², one with unequal sums kept a floor as ε → 0 and as the fast eigenvalues went to zero, and with the slow gap proportional to ε the order fell to first

## The case

**The class.** Ten variables in three blocks of sizes 3, 4 and 3.
A = A* + εC, with A* block-diagonal and C zero on the diagonal blocks,
‖C‖₂ = 1, Gaussian entries. Each block of A* is λ times a column-stochastic
matrix mixed towards uniform (so its columns sum to λ and its other
eigenvalues are at most 0.6λ), or, for the "unequal" block, that matrix
with its columns rescaled by up to ±30% and the whole rescaled to spectral
radius λ. The noise covariance is a random positive definite matrix with
condition number up to 5. The aggregate is the sum over the first block.
Dynamical dependence T is computed from the steady filter, and checked
against regression on 60 lags of Y's autocovariances (agreement to 10⁻⁸).

**Results** (scratch/studies/lead-178/results.md).

- *Sandwich.* Lower ≤ T ≤ upper on all 600 items, and on 40 random
  unstructured systems with aggregates of dimension 1 to 3 in the tests.
- *Equal column sums,* 20 systems, ε from 0.2 to 0.00625. T at ε = 0 was
  at most 5.6 × 10⁻¹⁷. T/ε² at ε = 0.00625 ran from 0.026 to 0.59, with
  lower constants from 0.012 and upper ones to 0.59, and had settled by
  ε = 0.025.
- *Unequal column sums,* the same 20 systems otherwise. T at ε = 0 ran from
  6.7 × 10⁻⁴ to 0.034 nats, the lower bound at least 6.7 × 10⁻⁴.
  |T(ε) − T(0)|/ε at most 0.034 at ε = 0.00625: the approach to the floor
  is first order.
- *The same blocks aggregated by their left Perron vector.* T = 0 at
  ε = 0 (to 10⁻¹⁶), and T/ε² from 0.052 to 0.73: the floor belongs to the
  sum, not the block.
- *Fast gap,* 10 systems, unequal sums, ε = 0, the block's other
  eigenvalues shrunk from at most 0.24 to 0. The smallest floor went from
  1.8 × 10⁻³ to 1.6 × 10⁻³ and the largest from 0.032 to 0.029.
- *Slow gap,* 10 systems, equal sums, every block's leading eigenvalue
  1 − γ, ε = 0.004 and 0.002. Median T/ε² was 0.18, 0.26, 0.67 and 1.6 at
  γ = 0.3, 0.1, 0.03 and 0.01, the same at both ε; the median lower
  constant stayed at 0.14, and the upper bound exceeded T by at most 3.2%.
- *Simon–Ando scaling,* γ = 2ε, ε from 0.04 to 0.0025. Median T/ε fell
  from 0.019 to 0.0093 and was levelling off, while T/ε² rose from 0.47
  to 3.7: first order.
- *Scalar bound* ε²‖LC‖²κ(V)²‖Σ‖/(2G(1 − ρ²)) on 250 items of the
  equal-sum, slow-gap and Simon–Ando families: T was at most 0.14 of it,
  median 0.008, with κ(V) from 1.6 to 48.

## What it shows and does not

It shows the bound and both regimes on random instances of one size. It
does not test aggregates of several blocks at once, larger systems,
non-diagonalizable A, or any horizon beyond one step.
