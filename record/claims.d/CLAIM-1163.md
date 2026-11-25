---
number: 1163
status: Active
formerly:
- CLAIM-tmprbieu
title: 'Linear tests see only the mean representation'
statement: >-
  Linear tests of a representation see a distribution only through its mean
  representation: their largest disagreement is the dual norm of the
  difference of means, so two distributions with one mean, as a point mass
  at 0 and an even split between −1 and 1, are at distance zero under every
  linear test and are told apart by a single nonlinear one
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from A29 §2 of the exchange "Explain
    First Contact RL" (ChatGPT, shared 2026-11-22); checked with python3 -I.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): rests on CLAIM-1186, promoted in the same
    change; the identity is the dual norm's definition, and the example
    checks.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the identity: a norm ‖·‖ on ℝ^d and two distributions with
  integrable features φ for which sup over ‖w‖ ≤ 1 of |∫ wᵀφ d(μ − ν)|
  differs from the dual norm of E_μ[φ] − E_ν[φ], or affine tests that
  separate two distributions with equal feature means. That a richer
  feature map separates them does not defeat the claim; the claim is
  relative to φ.
tags:
- representation-learning
- mathematics
- probabilistic-modeling
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
rests_on:
- CLAIM-1186
complements:
- CLAIM-269
summary: >-
  A29 §2 of the exchange "Explain First Contact RL" (2026-11-22). With
  tests f_w(x) = wᵀφ(x), ‖w‖ ≤ 1, the pseudometric of [CLAIM-1186](CLAIM-1186.md) is
  ‖E_μ[φ] − E_ν[φ]‖_*, the dual norm of the difference of mean
  representations (an added constant cancels). A29's example with φ(x) = x:
  ½δ₋₁ + ½δ₁ and δ₀ have one mean, so every affine test agrees on them,
  while g(x) = x²/(1 + x²) gives ½ and 0. So A29's "Which concepts are linearly
  decodable from individual representations?" and "Which distributions
  of organizational states can be distinguished by linear expectations?"
  are different questions, the
  second much more restrictive unless φ is rich. It is the linear-kernel
  case of the mean-embedding view of MMD. Checked by the assistant
  (Claude, in this session) with python3 -I. The wording is A's (ChatGPT,
  in the exchange of 2026-11-22); adopting it is the owner's call.
---

# CLAIM-1163: Linear tests see only the mean representation

## The claim

Let φ: X → ℝ^d be a representation and take the linear tests
f_w = wᵀφ with ‖w‖ ≤ 1. Then

d_lin(μ, ν) = sup_{‖w‖≤1} |wᵀ(E_μ[φ] − E_ν[φ])| = ‖E_μ[φ] − E_ν[φ]‖_*,

the dual norm (Euclidean for Euclidean). An affine test wᵀφ + b gives the
same value, since b integrates to b under both. A29: "Linear tests of
distributions see their mean feature representation, not necessarily the
distributions themselves."

A29's example, φ(x) = x on the line: μ = ½δ₋₁ + ½δ₁ and ν = δ₀ both
have mean 0, so d_lin(μ, ν) = 0, yet g(x) = x²/(1 + x²) gives ∫g dμ = ½
and ∫g dν = 0. One distribution is split between two states, the other
concentrated between them.

## Bearing

A29: "Two organizations may have identical aggregate linear signatures
while possessing very different internal distributions." That linear
probes decode a concept from each representation is one claim; that
linear expectations tell apart distributions of states is another, and
the second fails whenever two distributions share a mean representation.
[CLAIM-269](CLAIM-269.md) states the counterpart for representations (a regularized
linear readout separates only representations differing in normalized
kernel); this is the counterpart for distributions of a fixed
representation. It does not tell against the linear representation
hypothesis ([LIT-304](../literature.d/LIT-304.md)), which concerns single representations.

## Check

python3 -I: the five random affine tests gave equal expectations under μ
and ν; ∫g dμ = 0.5, ∫g dν = 0.0; for random discrete measures on ℝ³ the
sampled supremum over 200 000 unit w (1.397462) matched ‖Δmean‖
(1.397463).
