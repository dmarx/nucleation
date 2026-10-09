---
number: 160
status: Proposed
formerly:
- THEORY-tmp3dh4x
promote_when: >-
  A second, independent treatment read and checked: a textbook or paper on
  Poisson or Jordan–Lie algebras that derives the symmetry–conservation
  equivalence from antisymmetry (or self-conservation) of the bracket plus
  uniqueness of flows, under stated analytic conditions, or a checked
  reading of Alfsen and Shultz (1998) showing that a dynamical
  correspondence's condition (A) is exactly what gives the equivalence for
  JB-algebras. Refuted by a structure with a bilinear antisymmetric bracket
  and unique flows in which some a generates symmetries of b but b does not
  generate symmetries of a.
title: 'In the algebraic Hamiltonian setting, symmetry and conservation correspond because the bracket is antisymmetric, which for a bilinear bracket is each observable conserving itself; the theorem''s content lies in identifying observables with generators'
version: 1
tags:
- mathematics
- natural-sciences
- quantum-foundations
date: '2026-10-09'
source:
- LIT-819
summary: >-
  Baez (2020), [LIT-819](../literature.d/LIT-819.md), read in [NOTE-630](../notes.d/NOTE-630.md), Theorems 3, 4, 8 and
  10, with Alfsen and Shultz's theorem quoted as Theorem 12. With unique
  solutions to the flow equations, "a generates symmetries of b iff b
  generates symmetries of a" is {a, b} = 0 ⇔ {b, a} = 0. It assumes
  reversible one-parameter groups and an observable–generator map; it says
  nothing about dissipative or stochastic dynamics, nor about the
  Lagrangian form of Noether's theorem.
supports:
- CLAIM-094
---

<!-- inactive-ok-file: THEORY-158 — Proposed; named as the Markov-process contrast, not leaned on -->

# THEORY-160: In the algebraic Hamiltonian setting, symmetry and conservation correspond because the bracket is antisymmetric, which for a bilinear bracket is each observable conserving itself; the theorem's content lies in identifying observables with generators

## Source

Baez (2020), [LIT-819](../literature.d/LIT-819.md), read in [NOTE-630](../notes.d/NOTE-630.md): Theorems 3, 4, 8 and 10
with their proofs, the remark on bilinearity after Theorem 3, and
Theorem 12 (Alfsen and Shultz, quoted).

## What was actually shown

Let a, b each generate a flow: the equation d/dt F_t^a(b) = {a, F_t^a(b)},
F_0^a(b) = b, has a unique solution. Then F_t^a(b) = b for all t iff
{a, F_t^a(b)} = 0 for all t iff {a, b} = 0, the last step because the
constant path solves the equation when {a, b} = 0 and solutions are unique.
Antisymmetry turns {a, b} = 0 into {b, a} = 0, and the chain runs back
with a and b exchanged. This is proved for Poisson algebras (Theorem 3),
for self-adjoint elements of complex *-algebras with the bracket i[a, b]
(Theorem 4), for a bare vector space with a bilinear bracket in which each
element conserves itself (Theorem 8), and for Banach–Lie algebras, where
flows always exist and are unique (Theorem 10). For a bilinear bracket,
antisymmetry is equivalent to {a, a} = 0, the self-conservation principle.

Where observables and generators are different kinds of thing (a Jordan
algebra O and a Lie algebra L), the equivalence needs a map ψ : O → L. In
complex quantum mechanics ψ(a) = ia. For real and quaternionic matrices
dim O ≠ dim L and no invariant map exists. For unital JB-algebras, Alfsen
and Shultz show such a map with ψ_a(a) = 0 and a second condition exists
exactly when O is the self-adjoint part of a C*-algebra.

What could have come out otherwise: Theorem 8 could have needed the Jacobi
identity or an associative product; it does not. The proofs are short and
were checked in the reading.

## What this does not say

- It does not say symmetries give conservation laws in general. The
  equivalence needs reversible one-parameter groups and an antisymmetric
  bracket between the two quantities. For Markov semigroups, a diagonal
  observable and the generator have no such bracket, and a conserved mean
  does not give a symmetry ([THEORY-158](THEORY-158.md)). Reading this THEORY as "Noether's
  theorem holds for any dynamics with a generator" is the error it invites.
- It does not cover the Lagrangian form of Noether's theorem or field
  theories; the link back is cited, not shown.
- It does not settle why observables should be generators. Alfsen and
  Shultz's theorem says what follows if they are; Baez's reading of the
  second condition as "inverse temperature is imaginary time" is an
  interpretation he calls incomplete.
- Existence and uniqueness of flows is assumed, not proved, outside
  bounded settings (compact Poisson manifolds, C*- and Banach–Lie
  algebras).
