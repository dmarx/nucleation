---
number: 379
status: Proposed
formerly:
- CASE-tmp5w2ty
title: 'Directed decision signature reduces to a symmetric two-step operator for decisions about the input'
version: 1
standing: documented
kind: executed-study
tags:
- representation-learning
- mathematical-statistics
- mathematics
date: '2026-11-22'
illustrates:
- CLAIM-209
bears_on:
- QUESTION-052
draws_on:
- THEORY-239
line:
- pragmatic-transport
- formal-apparatus
---

# CASE-379: Directed decision signature reduces to a symmetric two-step operator for decisions about the input

## The case

A small numerical study, by [LEAD-142](../leads.d/LEAD-142.md), of the signature [QUESTION-052](../questions.d/QUESTION-052.md) names for
the directed case. The setup is Zhai's conditional-expectation operator
([THEORY-239](../theory.d/THEORY-239.md)): for a joint law P⁺(x, a) of an input X and a context A,
`T: L²(P_A) → L²(P_X)`, `(Tg)(x) = E[g(A) | X = x]`, with singular values
s_i and left and right singular functions μ_i (of x) and ν_i (of a). The
candidate directed signature is the top-d **left** singular span
span{μ₁…μ_d}. The code and tests are in `scratch/studies/lead-142/`
(numpy, `python3 -I`, BLAS threads 1; runs in under a second on 3×3 and 4×4
matrices).

Four things were computed and checked by pytest.

**A. Reduction.** The top-d left singular span equals the top-d eigenspace of
the self-adjoint two-step chain M(x, x′) = Σ_a P(a | x) P(x′ | a), that is,
M = T T*, the "same-kind on X" chain x → a → x′. Numerically M μ_i = s_i² μ_i
to 1e-15, M is reversible with respect to P_X to 1e-17, and the μ_i are
L²(P_X)-orthonormal. Checked on the three-state chain and on twenty random
non-reversible 4×4 kernels.

**B. The held directed linear result, reproduced.** On the non-reversible
three-state chain of [THEORY-239](../theory.d/THEORY-239.md)'s note (rows (0.1, 0.8, 0.1),
(0.1, 0.1, 0.8), (0.6, 0.2, 0.2)): π = (0.287, 0.338, 0.374), singular values
(1, 0.655, 0.534), μ₂ ∝ (−1.30, 1.22, −0.11) — matching the entry — and the
left and right singular functions differ (the pair is genuinely directed).
The worst-case linear-probe error over the (1 − ε)-compatible class was
computed by the S-procedure dual: with s = (1, 0.9, 0.8, 0.5, 0.1), ε = 0.15,
d = 2, the top span and the tilted spans span{μ₁, cos θ·μ₂ + sin θ·μ₄} all
reach r* = 0.7708 for θ = 0.05, 0.2, 0.5, rising to 0.973 only at θ = 1. The
spans tie even with a spectral gap, as the entry says.

**C. Beyond linear probes.** On a product chain (two independent two-state
chains, ρ_a = 0.9, ρ_b = 0.8), the interaction χ_a·χ_b is a stable target
(two-step eigenvalue 0.518) whose linear-probe residual on the top-2 span is
the full 1.0, while a nonlinear (product) readout of the same two-dimensional
encoder recovers it exactly (residual 0). And the compatible target χ_b
(eigenvalue 0.64) has residual 1.0 from the top-1 encoder χ_a yet 0 from the
competitor encoder χ_b: which span is sufficient depends on the decision.

**D. Direction obstruction.** The left signature is a function of x only. The
order decision sign(x − a) on ordered pairs has residual 0.2245 (of variance
0.824) from any function of x, and 0 from the pair itself. A decision that
turns on the direction of the transport is not a function of the left
signature at any d.

## What it can show

Being an executed computation on exact finite laws, it demonstrates the
identities and exhibits the counterexamples outright; it is not an empirical
sample. It does not speak to what a trained network reaches, to infinite
spaces, or to estimation from data — the same limits [THEORY-239](../theory.d/THEORY-239.md) carries. The
product-chain and three-state examples are chosen for transparency, not drawn
from any corpus, so they bound what is claimed (a candidate can fail) without
measuring how often it does.
