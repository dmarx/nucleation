---
number: 2181
status: Proposed
formerly:
- THEORY-tmpmsncg
promote_when: >-
  An independent derivation or simulation of the same growing tree (new
  sites attaching with probability proportional to A_k) reproduces the
  three regimes for A_k = k^γ (a stretched exponential for 0 < γ < 1, one
  site holding nearly all links for γ > 1, a power law at γ = 1) and the
  dependence of the exponent on an asymptotically linear kernel,
  ν = 1 + μ/a∞; for example a rigorous treatment of superlinear
  attachment, or the authors' longer paper checked against this letter.
  Not met by a restatement that cites this paper, and not defeated by a
  model with fitness or aging, which the title does not cover.
title: 'Only linear attachment gives a power law'
statement: >-
  Krapivsky, Redner and Leyvraz, solving the rate equations of a growing
  tree whose new sites attach with probability proportional to a kernel A_k,
  find a stretched-exponential degree distribution for A_k = k^γ with 0 < γ
  < 1, a single site taking nearly all links for γ > 1, and a power law only
  at γ = 1, where an asymptotically linear kernel A_k → a∞k gives an
  exponent ν = 1 + μ/a∞ that can take any value above 2
version: 1
tags:
- network-science
- complex-systems
- probabilistic-modeling
date: '2026-11-22'
source:
- LIT-2974
bears_on:
- QUESTION-505
summary: >-
  Krapivsky, Redner & Leyvraz (2000), [LIT-2974](../literature.d/LIT-2974.md), read in [NOTE-2267](../notes.d/NOTE-2267.md).
  The record's source for the regimes of the attachment kernel, which
  [CLAIM-817](../claims.d/CLAIM-817.md) and [CLAIM-806](../claims.d/CLAIM-806.md) state and [ARG-184](../arguments.d/ARG-184.md) takes them from. The
  sharp edge: the power law is the borderline case, k^(−3) only for
  A_k = k exactly, and the authors themselves say that for 0.8 ≲ γ ≲ 1 a
  stretched exponential and a power law are hard to tell apart up to
  k = 1000. Proposed until an independent derivation confirms it.
---
<!-- inactive-ok-file: CLAIM-817 CLAIM-806 ARG-184 — Proposed or new; the claims this reading grounds and the argument that says how -->

# THEORY-2181: Only linear attachment gives a power law

## Source

Krapivsky, Redner & Leyvraz (2000), "Connectivity of Growing Random
Networks", Physical Review Letters 85, 4629, [LIT-2974](../literature.d/LIT-2974.md), read in the arXiv
preprint in [NOTE-2267](../notes.d/NOTE-2267.md).

## What was actually shown

A rate equation for the mean number N_k(t) of sites with k links, with
entry of one new site per step, solved by kernel. "A power law
distribution N_k ∼ k^−ν arises only for γ = 1. In this case, finer details
of the dependence of the connection kernel on k affect the exponent ν"
(p. 1). For A_k = k exactly, n_k = 4/[k(k+1)(k+2)]; for γ = 0,
n_k = 2^(−k); for 0 < γ < 1 a stretched exponential with leading term
exp[−μk^(1−γ)/(1−γ)]; for γ > 1 "a single “gel” site connects to nearly
every other site of the graph", with a cascade of transitions at
γ = (m+1)/m; for A_k → a∞k, "ν = 1 + µ/a∞" (p. 2), which with A_1 = 1 and
A_k = a∞k becomes ν = (3 + √(1 + 8/a∞))/2.

What could have come out otherwise: the sublinear tail could have been a
power law with a γ-dependent exponent. It is not, and so a power law is
marginal in γ.

## What this does not say

- Not that any real degree distribution comes from this mechanism. The
  authors fit the ISI citation data equally well with γ ≈ 0.86 and with
  ν ≈ 2.5, and say that for 0.8 ≲ γ ≲ 1 the two forms are hard to
  distinguish up to k = 1000.
- Not that the linear case has exponent 3. It is a family, ν in (2, ∞).
- Not anything about networks without entry, or with fitness or aging,
  none of which the paper treats.
- Not a rigorous result: the equations are for averages, and the γ > 1
  analysis is leading order.
