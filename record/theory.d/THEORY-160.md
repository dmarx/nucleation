---
number: 160
status: Active
formerly:
- THEORY-tmp3dh4x
title: 'In the algebraic Hamiltonian setting, symmetry and conservation correspond because the bracket is antisymmetric, which for a bilinear bracket is each observable conserving itself; the theorem''s content lies in identifying observables with generators'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-160.yaml,
    batch 008, ADR-047). The symmetry–conservation equivalence for a bracket
    with unique flows (Baez's Theorems 3, 4, 8 and 10) is re-derived step by
    step in the decision. Under ADR-047 v2, the owner's rule of 2026-10-19,
    that meets the promote_when's request for a second, independent
    treatment. Alfsen and Shultz's JB-algebra theorem, which Baez quotes as
    Theorem 12 without proof, is now stated as quoted and not checked, and
    the promote_when's clause about it moves to QUESTION-tmpb09gm. The
    title's last clause reports Baez's reading, which the body already marks
    as interpretation. The promote_when is removed. The title is unchanged.
tags:
- mathematics
- natural-sciences
- quantum-foundations
date: '2026-10-09'
source:
- LIT-819
summary: >-
  Baez (2020), [LIT-819](../literature.d/LIT-819.md), read in [NOTE-630](../notes.d/NOTE-630.md), Theorems 3, 4, 8 and
  10, with Alfsen and Shultz's theorem quoted as Theorem 12 and not
  checked here (QUESTION-tmpb09gm). With unique solutions to the flow
  equations, "a generates symmetries of b iff b
  generates symmetries of a" is {a, b} = 0 ⇔ {b, a} = 0. It assumes
  reversible one-parameter groups and an observable–generator map; it says
  nothing about dissipative or stochastic dynamics, nor about the
  Lagrangian form of Noether's theorem.
supports:
- CLAIM-094
---


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
dim O ≠ dim L and no invariant map exists. For unital JB-algebras, Baez
quotes Alfsen and Shultz (his Theorem 12): such a map with ψ_a(a) = 0 and a
second condition exists exactly when O is the self-adjoint part of a
C*-algebra. The record has not read that theorem, so it is reported as
quoted, not checked ([QUESTION-tmpb09gm](../questions.d/QUESTION-tmpb09gm.md)).

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
- **It does not include Alfsen and Shultz's theorem.** The JB-algebra
  characterisation is quoted by Baez without proof, and the record has not
  read it. It is [QUESTION-tmpb09gm](../questions.d/QUESTION-tmpb09gm.md).
- It does not settle why observables should be generators. Alfsen and
  Shultz's theorem says what follows if they are; Baez's reading of the
  second condition as "inverse temperature is imaginary time" is an
  interpretation he calls incomplete.
- Existence and uniqueness of flows is assumed, not proved, outside
  bounded settings (compact Poisson manifolds, C*- and Banach–Lie
  algebras).

## Note of 2026-10-19: the bracket equivalence, re-derived

The promotion audit's batch 008 re-derived the equivalence ([ADR-047](../decisions.d/ADR-047.md) v2).
Assume that, for each a, the flow equation d/dt F_t(b) = {a, F_t(b)},
F_0(b) = b, has a unique solution.

1. If F_t^a(b) = b for all t, differentiating at t = 0 gives {a, b} = 0.
2. If {a, b} = 0, the constant path c(t) = b satisfies
   c′(t) = 0 = {a, b} = {a, c(t)} and c(0) = b. By uniqueness, F_t^a(b) = b
   for all t. So "a generates symmetries of b", meaning F_t^a(b) = b for all
   t, holds iff {a, b} = 0.
3. Antisymmetry gives {a, b} = 0 iff {b, a} = 0, so the relation is
   symmetric.
4. For a bilinear bracket over a field of characteristic other than 2,
   antisymmetry is equivalent to {a, a} = 0 for all a. Antisymmetry gives
   {a, a} = −{a, a}. Conversely, expanding {a + b, a + b} = 0 gives
   {a, b} + {b, a} = 0.

The Jacobi identity and any associative product are used nowhere, as
Theorem 8 has it.
