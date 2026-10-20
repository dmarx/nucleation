---
number: 198
status: Open
formerly:
- QUESTION-tmphxde6
title: 'Does the O(σ²) gap between the kernel and Shannon relative entropies hold for translation-invariant kernels on the torus beyond the exponential Fourier family, and on other compact spaces?'
version: 1
tags:
- information-theory
- mathematics
date: '2026-10-19'
line: 'formal-apparatus'
summary: >-
  Filed when the promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-313](../theory.d/THEORY-313.md) to the kernel family Bach (2022) works out. The
  former promote_when asked for a confirmation of the O(σ²) gap beyond
  the torus; this question holds it.
answered_by:
- THEORY-811
---

# QUESTION-198: Does the O(σ²) gap between the kernel and Shannon relative entropies hold for translation-invariant kernels on the torus beyond the exponential Fourier family, and on other compact spaces?

## Why it is a question

[THEORY-313](../theory.d/THEORY-313.md) now states Bach's sandwich D(p̃‖q̃) ≤ D(Σ_p‖Σ_q) ≤ D(p‖q) for
unit-diagonal kernels. It also states the gap bound: D(p‖q) − D(p̃‖q̃) is
at most a constant times sup_x ∫h(x, y)d(x, y)² dy. On the torus with
Fourier coefficients proportional to e^(−σ‖ω‖₁), that integral is at most
dσ²/16. The audit re-derived all three ([LIT-255](../literature.d/LIT-255.md), [NOTE-837](../notes.d/NOTE-837.md)).

Bach asserts that the rate extends to every translation-invariant kernel
on [0, 1]^d and to translation-invariant kernels on compact spaces, and
sketches a leverage-score argument. Neither is carried through. The
quantity that has to be controlled is ∫h(x, y)d(x, y)² dy, with h the
squared normalized kernel, and that depends on how fast the kernel's
spectrum decays.

## What would answer it

A bound of ∫h d² = O(σ²) for a stated wider class of translation-invariant
kernels would answer it yes for that class: for example, kernels whose
Fourier coefficients are a fixed decreasing profile rescaled by σ, or
Gaussian kernels on the torus. So would the same bound for invariant
kernels on a compact group or homogeneous space, or a later paper that
proves either. A translation-invariant unit-diagonal kernel family whose
gap shrinks more slowly than σ² as its bandwidth shrinks would answer it
no. Numerical agreement between kernel and Shannon estimates on examples
cannot settle it, since the inequalities permit agreement at any
bandwidth.
