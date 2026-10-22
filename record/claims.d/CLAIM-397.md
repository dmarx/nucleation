---
number: 397
status: Active
formerly:
- CLAIM-tmp511ss
title: 'For a scalar stationary process with autocovariance C, the Mori–Zwanzig memory kernels for the projection onto the current value are fixed by C alone, through C(m+1) = Σ_{k≤m} c_k C(m−k); the memory vanishes iff C is geometric, and when C has finite Hankel rank d the memory has Hankel rank exactly d − 1'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A5 restated this claim's "What it
    does not say" as its Proposition A without noticing it; the widening
    from memory measures to any functional of Y's law is shown by one
    explicit pair, CLAIM-389's Y against an autonomous AR(1). The claim is
    unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a scalar stationary process whose
  autocovariance has rational generating function of Hankel rank d, for
  which the Mori memory sequence (c_k)_{k≥1}, computed from the Volterra
  recursion, has Hankel rank other than d − 1.
tags:
- probabilistic-modeling
- mathematics
- complex-systems
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-222
grounds:
- LIT-1307
- THEORY-819
summary: >-
  Derived in the reading of Lin and Lu (2019), [NOTE-1029](../notes.d/NOTE-1029.md), and
  re-checked here. It settles the minimal-order question [CLAIM-398](CLAIM-398.md)
  left open, for every scalar stationary process with rational
  autocovariance, and gives the structural reason for [CLAIM-389](CLAIM-389.md)'s "not
  conversely": the memory is a functional of the coarse variable's own law,
  so it cannot register dependence on the rest of the system.
supports:
- CLAIM-401
---
<!-- inactive-ok-file: NOTE-1029 — new reading, cited as where the result was derived -->

# CLAIM-397: For a scalar stationary process with autocovariance C, the Mori–Zwanzig memory kernels for the projection onto the current value are fixed by C alone, through C(m+1) = Σ_{k≤m} c_k C(m−k); the memory vanishes iff C is geometric, and when C has finite Hankel rank d the memory has Hankel rank exactly d − 1

## The claim

**The kernels are fixed by C.** Project onto the span of the current value
Y_t. Taking the covariance of the discrete Mori–Zwanzig equation
([THEORY-819](../theory.d/THEORY-819.md)) with Y₀, the noise term drops out, being orthogonal to
the projection space at the initial time, and what remains is the Volterra
recursion C(m+1) = Σ_{k=0}^{m} c_k C(m−k). In generating functions,
1 − Σ_k c_k w^{k+1} = C(0)/Ĉ(w). So the kernels c_k are a functional of C,
that is, of Y's own second-order law. The memory (c_k for k ≥ 1) vanishes
iff C(m) = c₀^m C(0).

**Its order.** Let Ĉ = N/D in lowest terms with D(0) = 1, so that the
Hankel rank of C is d = max(deg D, deg N + 1) (Kronecker). The memory
sequence has generating function num/N, with
w²·num = N − C(0)D − c₀wN. num and N share no root: a common root r would
give C(0)D(r) = 0, against coprimality. So the memory's Hankel rank is
max(deg N, deg num + 1). If deg N = d − 1, that is d − 1. Otherwise
deg D = d, the w^d coefficient of N − C(0)D − c₀wN is −C(0)D_d ≠ 0, so
deg num = d − 2, and the rank is again d − 1.

**Checks** ([NOTE-1029](../notes.d/NOTE-1029.md)). In a random n = 4 VAR(1) the Mori kernels
computed from the projection blocks matched the Volterra recursion from C
to 2 × 10⁻¹⁶, with d = 4 and memory rank 3; seven cases in all, including
[CLAIM-389](CLAIM-389.md)'s counterexample (d = 1, rank 0). Re-run by the coordinator.

## What it does not say

- **Not that memory detects dependence.** Since the kernels depend only on
  Y's own law, no memory measure can tell whether the rest of the system
  drives Y. That needs the joint law, which is what [THEORY-257](../theory.d/THEORY-257.md)'s
  transfer entropy uses ([CLAIM-389](CLAIM-389.md)).
- **Not about other projections.** Projecting onto Y's whole past (the
  Wiener projection) gives a different kernel with the same numerator
  and a different denominator in the VAR(1) case; that is in
  [NOTE-1029](../notes.d/NOTE-1029.md), not here.
- **Nothing about nonlinear functionals.** Second order only.

## Note of 2026-10-21: the widening to any functional of the law

A5 of the exchange of 2026-10-20 restated this claim's "What it does not
say" as "Proposition A": "No method operating exclusively on the marginal
law of the observed process can, in general, identify its dynamical
independence from omitted variables." It cited this claim without noticing
that it already says so for memory. A4 had put it as "whether external
influence can be detected in the reduced process's own temporal
structure", and A7 §III made it a proposition: "This is not a sample-size
limitation. It survives even with perfect knowledge of the observable
distribution."

The widening, from memory measures to any functional of Y's law, is shown
by one pair, checked on 2026-10-21. [CLAIM-389](CLAIM-389.md)'s Y has autocovariance 0.5ᵗ
and unit variance. A stationary Gaussian process is fixed by its mean and
autocovariance, so Y has the law of the autonomous AR(1)
Y′_t = 0.5 Y′_{t−1} + η_t with Var η = 0.75. Yet T(X → Y) =
½ ln(0.75/0.59) = 0.120 nats per step, while Y′, taken as its own whole
system, receives nothing. By [CLAIM-350](CLAIM-350.md), a property decidable from 𝓛(Y)
must be constant on the models that share that law, and dynamical
independence is not. Dependence can still be found from the joint law of
the whole system, and nothing here is about interventions.

The pair was proposed as a claim of its own and not filed; it is recorded
here and on [CLAIM-389](CLAIM-389.md). [QUESTION-252](../questions.d/QUESTION-252.md)'s leave-one-out uses it as the
witness for memory without independence.
