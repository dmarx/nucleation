---
number: 629
status: Active
formerly:
- THEORY-tmpryy39
title: "Every continuous linear functional on a Hilbert space is the inner product with a unique vector of the same norm, given in any orthonormal basis by the conjugated values of the functional on the basis; completeness is what makes it so, and Riesz's 1907 statement on L² asserted only that a representing function exists"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-243
- LIT-326
summary: >-
  Adler (2021), [LIT-243](../literature.d/LIT-243.md), read in full in [NOTE-854](../notes.d/NOTE-854.md): two complete proofs,
  by projection (Thm 3.5) and by an orthonormal basis (Thm 4.9), with
  completeness used once, in the projection theorem. Riesz (1907),
  [LIT-326](../literature.d/LIT-326.md), read in [NOTE-289](../notes.d/NOTE-289.md), is the priority note: existence of k with U(f)
  = ∫ f k for continuous linear U on square-summable functions, stated
  without proof, uniqueness or norm. The theorem says nothing about kernels,
  factorisation or uniqueness of representations. Both readings advise
  citing a textbook for anything leaned on.
---

# THEORY-629: Every continuous linear functional on a Hilbert space is the inner product with a unique vector of the same norm, given in any orthonormal basis by the conjugated values of the functional on the basis; completeness is what makes it so, and Riesz's 1907 statement on L² asserted only that a representing function exists

## Source

Adler (2021), "Hilbert Spaces and the Riesz Representation Theorem",
University of Chicago REU paper, [LIT-243](../literature.d/LIT-243.md), read in full in [NOTE-854](../notes.d/NOTE-854.md). Riesz
(1907), "Sur une espèce de géométrie analytique des systèmes de fonctions
sommables", *Comptes rendus* 144:1409–1411, [LIT-326](../literature.d/LIT-326.md), read in full in
[NOTE-289](../notes.d/NOTE-289.md).

## What was actually shown

**The theorem ([LIT-243](../literature.d/LIT-243.md), Thm 3.5).** With the inner product conjugate-linear
in its first slot, for every continuous linear φ on a Hilbert space V there
is a unique u with φ(v) = ⟨u, v⟩ for all v, and ‖u‖ = ‖φ‖. The proof takes a
unit w normal to ker φ and sets u = conj φ(w) w. Completeness enters once, in
the Hilbert projection theorem (Thm 2.2), where a minimising sequence must
converge.

**The basis formula (Thm 4.9).** For any orthonormal basis {e_k},
u = Σ_k conj φ(e_k) e_k and ‖φ‖² = Σ_k |φ(e_k)|². The groundwork is Bessel's
inequality and the closed span as the square-summable combinations (Thms
4.5–4.8). This is the finite-dimensional dual-basis computation of §3,
carried to infinite dimensions.

**A consequence (Thm 5.1).** Applied to f ↦ ∫ f dν on L²(ν + μ), the theorem
gives the Radon–Nikodym derivative dν/dμ = g/(1 − g) for finite positive
measures with ν ≪ μ.

**The first statement ([LIT-326](../literature.d/LIT-326.md), p. 1410).** Riesz states that for every
operation U on square-summable functions that is linear and continuous for
convergence in mean, there is a function k with U(f) = ∫ f k. He calls it an
immediate consequence of his existence theorem, that every square-summable
coordinate sequence is the image of a square-integrable function (the
Riesz–Fischer theorem), and gives no argument.

**What could have come out otherwise.** On an incomplete inner-product space
the projection step fails, and a continuous functional need not be
represented by any vector of the space.

## What this does not say

- **Anything about kernels, RKHS or factorisation.** Neither paper mentions
  them ([NOTE-854](../notes.d/NOTE-854.md)). A "unique factorization" argument must bring its own
  uniqueness: of the representer here, or of a representation up to an
  orthogonal transformation ([THEORY-004](THEORY-004.md)). Riesz 1907 states no uniqueness
  at all ([NOTE-289](../notes.d/NOTE-289.md)).
- **That the 1907 note proves the theorem, or proves it for Hilbert space.**
  It asserts existence of k on L² only, with no uniqueness, no norm identity
  and an unspecified domain. Fréchet's note in the same issue states it
  simultaneously.
- **That the representer is Σ φ(e_k) e_k.** The conjugate matters on complex
  spaces; [LIT-243](../literature.d/LIT-243.md)'s seeded summary dropped it ([NOTE-854](../notes.d/NOTE-854.md)).
- **That the bracket of Dirac notation is an inner product everywhere.**
  It is only where the theorem holds. On a Banach space bras and kets can be
  written, but the bracket is only a functional applied to a vector
  ([LIT-237](../literature.d/LIT-237.md), [NOTE-855](../notes.d/NOTE-855.md)).
- **Radon–Nikodym in general.** [LIT-243](../literature.d/LIT-243.md) proves it for finite measures; the
  σ-finite, signed and complex cases are asserted.

## Connections

- [THEORY-009](THEORY-009.md) holds that spectral self-supervised learning gets
  self-adjointness from symmetry of the pair distribution, not from this
  theorem. [THEORY-003](THEORY-003.md) is the one place in that family where it is invoked:
  kernel mean embeddings exist by it. [THEORY-314](THEORY-314.md)'s representer theorem uses
  the reproducing property, not this theorem.
- [LIT-230](../literature.d/LIT-230.md), the Wikipedia statement, gives the same theorem in the opposite
  convention.
