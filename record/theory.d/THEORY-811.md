---
number: 811
status: Proposed
formerly:
- THEORY-tmpbqu7h
promote_when: 'A line-by-line check of the proof of Proposition 5 (appendix B), which this reading followed only in outline, and a second source: either an independent derivation of D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q), or a later paper that uses it and confirms the O(σ²) gap beyond the torus. The inequalities themselves follow from joint convexity and monotonicity of quantum relative entropy and are not in doubt. It is refuted by a unit-diagonal kernel and a pair p, q with D(Σ_p‖Σ_q) > D(p‖q), or with equality at a non-orthonormal embedding. What cannot settle it: numerical agreement of kernel and Shannon estimates on examples, which the inequalities permit at any bandwidth.'
title: 'With a kernel normalised to unit diagonal, the kernel quantum relative entropy of two distributions is within O(σ²) of their Kullback–Leibler divergence as the bandwidth σ shrinks, for translation-invariant kernels on the torus generally and for kernels on other compact groups'
version: 1
tags:
- information-theory
- mathematics
- probabilistic-modeling
date: '2026-10-20'
source:
- LIT-255
summary: >-
  The general reading that [THEORY-313](THEORY-313.md) held before the
  promotion audit narrowed it to the one kernel family on the torus that the
  rate is shown for. Bach (2022), [LIT-255](../literature.d/LIT-255.md),
  read in [NOTE-837](../notes.d/NOTE-837.md), asserts that other
  translation-invariant kernels and kernels on compact groups behave alike,
  and sketches a leverage-score argument without completing it. Filed under
  [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis
  evidence can confirm or reject.
extends:
- THEORY-313
answers:
- QUESTION-198
---

# THEORY-811: With a kernel normalised to unit diagonal, the kernel quantum relative entropy of two distributions is within O(σ²) of their Kullback–Leibler divergence as the bandwidth σ shrinks, for translation-invariant kernels on the torus generally and for kernels on other compact groups

## Source

Bach (2022), [LIT-255](../literature.d/LIT-255.md), read in [NOTE-837](../notes.d/NOTE-837.md): Proposition 5 and the torus computation (claim C3, strong for the exponential Fourier family), and the assertion, with a leverage-score sketch, that the rate extends.

## What is asserted, and by whom

The thesis is that the O(σ²) gap between the kernel and Shannon relative entropies is not special to kernels with Fourier coefficients proportional to e^(−σ‖ω‖₁): it holds for translation-invariant kernels on the torus generally, and on other compact groups, for strictly positive Lipschitz densities. Bach asserts it; the argument is a sketch.

## What the record holds toward it

- [THEORY-313](THEORY-313.md) (Active): the bounds D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q) and, for the exponential Fourier family on the torus, a gap of at most dσ²/16.
- The lower bound by the smoothed KL holds for any unit-diagonal kernel, so the thesis reduces to how fast the smoothed KL approaches the KL.

## What would confirm or reject it

A completed proof for another translation-invariant family on the torus, or for a kernel on another compact group, would confirm it; a family on the torus with a strictly slower gap for Lipschitz densities would reject it. [QUESTION-198](../questions.d/QUESTION-198.md) asks this as a question; this entry is the answer Bach proposes.
