---
status: Active
title: "Averaging constant-rate SGD iterates at stationarity gives a covariance that shrinks with the number of examples processed, and equals the Gaussian posterior's for that many observations when the noise covariance equals the Hessian"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-31'
source:
- LIT-tmpwzrx7
summary: >-
  Mandt, Hoffman and Blei (2017), [LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md), §6 and App. G, read in
  [NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md). In their OU model, the mean of T stationary iterates at
  batch S has covariance A⁻¹BBᵀA⁻¹/(TS) to leading order in 1/(Tελ),
  whatever the step size or constant preconditioner; under a well-specified
  regular model (BBᵀ = A) that is A⁻¹/(TS), the Gaussian posterior's
  covariance for TS observations. Checked against the exact discrete
  covariance. It is the one place the paper ties examples processed to a
  sample size, and it is about spread in one basin after equilibration,
  not about which region dominates.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l — Open; the question this bears on -->

# THEORY-tmp8ggnh: Averaging constant-rate SGD iterates at stationarity gives a covariance that shrinks with the number of examples processed, and equals the Gaussian posterior's for that many observations when the noise covariance equals the Hessian

## Source

Mandt, Hoffman and Blei (2017), [LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md), §§6.1–6.2 (Eqs. 28–34,
Algorithm 1) and App. G (Eqs. 48–50) of arXiv 1704.04289v2; read in
[NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md).

## What was actually shown

Start constant SGD at its stationary law ([THEORY-tmp7gcht](THEORY-tmp7gcht.md)) and average T
successive iterates. From the OU autocovariance E[θ(t)θ(s)ᵀ] = e^(−A(t−s))Σ,
the average's covariance is

D = (1/T)(ΣA⁻¹ + A⁻¹Σ) + O(1/(Tε)²) = A⁻¹BBᵀA⁻¹/(TS)

with T counted in iterations (Eqs. 30–31, 50). It does not depend on ε,
and preconditioning by any constant H leaves it unchanged, because the
changes to the stationary covariance and to the autocorrelation cancel
(Eq. 31). That is Polyak and Juditsky's optimality, rederived. Under
Assumption 5, a well-specified regular model with BBᵀ = A, D ≈ A⁻¹/(TS),
and with T = N/S, one pass, D ≈ A⁻¹/N, the posterior covariance
(Eqs. 33–34). The error is largest along the Hessian's smallest
eigenvalue, of relative size about S/(εNλ_min) (p. 20).

**Check ([NOTE-tmpiaa2o](../notes.d/NOTE-tmpiaa2o.md)).** For a 3 × 3 A with eigenvalues 2, 0.5, 0.2,
BBᵀ = A, S = 5 and ε = 0.01, the exact covariance of the mean of T
iterates of the discrete stationary recursion differs from A⁻¹/(TS) by
23%, 4.7% and 0.9% at T = 2,000, 10,000 and 50,000, tracking
1/(Tελ_min) = 0.25, 0.05, 0.01.

**What could have failed.** The covariance could have depended on ε or on
the preconditioner, as the stationary covariance itself does. It does not.

## What this does not say

- **That training time maps to sample size in general.** The
  correspondence is between examples processed after equilibration, TS,
  and the sample size of a Gaussian posterior, in one basin of a regular,
  well-specified model. It describes how tightly the average pins down the
  fixed-data optimum, not which region of a multi-region posterior
  dominates. It says nothing about the order in which training visits
  regions, which is what [QUESTION-tmpiir0l](../questions.d/QUESTION-tmpiir0l.md) asks.
- **That the averaged iterates are posterior samples without Assumption
  5.** Otherwise D ≈ A⁻¹BBᵀA⁻¹/(TS), the sandwich covariance, which is
  not the posterior's A⁻¹/N for any T.
- **That no sampler can beat one sample per pass.** The paper argues it
  from Polyak–Juditsky under Assumptions 1–5, informally, and calls the
  assumptions "optimistic" (p. 21).
- **Anything before stationarity.** The averaging starts from the
  stationary law; the search phase is excluded.
