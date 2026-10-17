---
number: 530
status: Active
formerly:
- THEORY-tmpgx4tw
title: "The spectrum of a matrix bounds the norm of its rational functions up to a constant only if the matrix is diagonalisable, with the eigenvector condition number as the constant, while the closed numerical range of any Hilbert-space operator does so with a universal constant between 2 and 11.08, exactly 2 for 2×2 matrices"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-011
summary: >-
  Badea & Beckermann (2013), [LIT-011](../literature.d/LIT-011.md), a handbook survey read in full in
  [NOTE-009](../notes.d/NOTE-009.md). Example 107.2.5: σ(A) is K-spectral iff A is diagonalisable,
  with K ≤ cond(V). Fact 107.7.2: the closure of W(A) is completely
  K-spectral for every bounded A with a universal K ∈ [2, 11.08], and 2
  suffices for 2×2. The chapter proves almost nothing itself; the numerical
  range result is cited to Crouzeix (2007). The bound 11.08 was the 2013
  state; a later improvement to 1 + √2 is recalled in the reading but not
  verified. Whether the constant is 2 was open.
---

<!-- inactive-ok-file: THEORY-325 — Proposed; named in Connections for contrast, not leaned on -->

# THEORY-530: The spectrum of a matrix bounds the norm of its rational functions up to a constant only if the matrix is diagonalisable, with the eigenvector condition number as the constant, while the closed numerical range of any Hilbert-space operator does so with a universal constant between 2 and 11.08, exactly 2 for 2×2 matrices

## Source

Badea & Beckermann (2013), "Spectral Sets", chapter 107 of the *Handbook of
Linear Algebra*, 2nd ed., [LIT-011](../literature.d/LIT-011.md), read in full in [NOTE-009](../notes.d/NOTE-009.md).

## What was actually shown

A closed set X containing σ(A) is K-spectral for A when ‖f(A)‖ ≤ K·sup_X|f|
for every rational f with poles off X (§107.2). For a normal matrix the
spectrum is spectral with K = 1. The chapter collects what holds when A is
not normal.

**The spectrum (Example 107.2.5).** σ(A) is K-spectral iff A is
diagonalisable, with K ≤ cond(V) for V the eigenvector matrix. No finite set
is K-spectral for a non-diagonalisable matrix. The proof is sketched in
Examples 107.2.3–107.2.5, and the reading rates it strong ([NOTE-009](../notes.d/NOTE-009.md), C1).
The characterisations of normal, Hermitian and unitary A by σ(A), ℝ or 𝕋
being spectral are Fact 107.2.9, with the converse in Example 107.2.6 (C2).

**The numerical range (Fact 107.7.2).** For every bounded operator A on a
Hilbert space, the closure of W(A) = {⟨Ax, x⟩ : ‖x‖ = 1} is a complete
K-spectral set with a universal K_Crouzeix ∈ [2, 11.08] ([Cro07, Thm 1]).
For 2×2 matrices W(A) is completely 2-spectral, and 2 is attained (Fact
107.7.2b, Example 107.7.7). Shape-dependent constants exist for any compact
convex X ⊃ W(A) (Fact 107.7.1), and special shapes have explicit ones, such
as 2 + 2/√3 for sectors, strips, parabolas and hyperbolas (Example 107.7.3).

**Other sets.** The closure of the ε-pseudospectrum is K-spectral with K =
length(∂X)/(2πε) (Example 107.2.7). The numerical-radius disk is 2-spectral,
and 2 is best possible (Example 107.2.8).

**What follows for computation (§107.8).** Any polynomial or rational
approximation error of f on a convex E ⊃ W(A) transfers to the matrix at a
cost of at most that constant. For Arnoldi, ε_m ≤ 2K_Crouzeix ρ_{m−1}(f, E).

**What could have come out otherwise.** The spectrum could have controlled
‖f(A)‖ for some non-diagonalisable A, and the numerical range's constant
could have grown with the dimension. Neither is the case.

## What this does not say

- **That the constant is 2.** Whether K_Crouzeix = 2, even for 3×3 matrices,
  is Open Problem 107.7.1. The 2×2 case is weak evidence for the complete
  version, since Example 107.7.4 gives a 3×3 matrix whose W(A) is 2-spectral
  but not completely 2-spectral. That example rests on a personal
  communication ([NOTE-009](../notes.d/NOTE-009.md), C5).
- **That 11.08 is current.** The chapter is frozen at early 2013. [NOTE-009](../notes.d/NOTE-009.md)
  recalls Crouzeix and Palencia (2017) proving 1 + √2, from outside the
  chapter and unverified. Check it before quoting either number as the
  best known.
- **That the chapter proves these results.** Apart from §107.2's short
  arguments and the annulus computation of Example 107.6.2, every Fact is
  cited, and its support is the cited paper.
- **That the Krylov bounds are always informative.** They need E convex and
  containing W(A). When W(A) contains or nearly contains 0, the GMRES and FOM
  bounds become vacuous ([NOTE-009](../notes.d/NOTE-009.md), Limitations).
- **Anything about learning systems.** The chapter mentions no ML. For a
  symmetric Hessian, which is normal, the spectrum is already spectral and
  this machinery adds nothing.

## Connections

- [THEORY-325](THEORY-325.md) is the dynamical face of the same gap: a non-normal linear
  system can be destabilised by time dependence while stable at every
  instant, and non-normality is necessary for it. There the spectrum fails
  to control a product of operators; here it fails to control a function of
  one.
