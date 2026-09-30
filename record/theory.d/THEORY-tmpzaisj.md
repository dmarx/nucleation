---
status: Active
title: 'Under a superselection rule a coherent superposition across sectors is operationally a mixture, because no observable connects the sectors; Wick, Wightman and Wigner proved such a rule for integer versus half-integer spin and only postulated it for charge'
version: 1
tags:
- quantum-foundations
- mathematics
- logic
date: '2026-09-30'
source:
- LIT-339
- LIT-306
summary: >-
  Wick, Wightman & Wigner (1952), [LIT-339](../literature.d/LIT-339.md) — they define a superselection
  rule and show that a superposition across sectors "is not a pure state,
  but a statistical mixture". They prove the rule from time reversal for
  integer versus half-integer angular momentum, and postulate it for charge
  with "no conclusive evidence". What follows for Birkhoff–von Neumann's
  lattice ([LIT-306](../literature.d/LIT-306.md)), a product of sector lattices with central sector
  projections, is the record's inference. The centre-of-the-algebra
  formulation belongs to Haag, who is not read.
---

# THEORY-tmpzaisj: Under a superselection rule a coherent superposition across sectors is operationally a mixture, because no observable connects the sectors; Wick, Wightman and Wigner proved such a rule for integer versus half-integer spin and only postulated it for charge

## Source

Wick, Wightman & Wigner (1952), [LIT-339](../literature.d/LIT-339.md), pp. 102–104 ([NOTE-304](../notes.d/NOTE-304.md)). Birkhoff & von Neumann (1936), [LIT-306](../literature.d/LIT-306.md), §§6, 12, fn. 28 ([NOTE-275](../notes.d/NOTE-275.md)).

## What was actually shown

Wick, Wightman and Wigner define a superselection rule between subspaces A, B, … as a selection rule (no spontaneous transitions) plus the absence of any measurable quantity with non-zero matrix elements between them (p. 103). Given that, no measurement can tell F_a + F_b + … from e^{iα}F_a + e^{iβ}F_b + …. So an operator with off-diagonal blocks has no defined expectation value and is not measurable. A cross-sector superposition "is not a pure state, but a statistical mixture", to be described by a density matrix (p. 102). The argument is short: every observable is block-diagonal, so the superposition and the matching mixture give the same statistics.

The rule is proved for one case. Time reversal applied twice acts as +1 on integer and −1 on half-integer total angular momentum (eq. 8). So f_A + f_B and f_A − f_B are indistinguishable, and no spinor-field combination ψ + ψ* or i(ψ − ψ*) is measurable (pp. 103–104). The proof leans on the state-independence of the phase ratio, which footnote 8 flags as a point "discussed repeatedly". A charge rule is postulated with "no conclusive evidence", motivated by global phase invariance (p. 104). Linear momentum is shown not to define sectors (p. 103). The physical consequence is that relative intrinsic parities across sectors are conventions, and the paper's explicit moral is that "all Hermitean operators represent measurable quantities" has to go.

The record's inference, from [NOTE-275](../notes.d/NOTE-275.md) and [NOTE-304](../notes.d/NOTE-304.md): BvN's §6 Postulate rests on the conjecture that every Hermitian operator is an observable, and their §12 imposes irreducibility, which excludes central elements (fn. 28). Under superselection the observable propositions are the projections of a block-diagonal algebra. The sector projections are then central, and the lattice is the direct product of the sector lattices, which is exactly the case BvN rule out.

## What this does not say

- That a cross-sector superposition is ill-formed, or that propositions about it lack truth values. It is an ordinary state that happens to act as a mixture. What is missing is an observable, not a truth value ([NOTE-304](../notes.d/NOTE-304.md)).
- That charge superselection is established. It is a postulate here, and later disputes (Aharonov–Susskind) are neither held nor read.
- That superselection is the centre of the observable algebra. That formulation is Haag's ([LIT-321](../literature.d/LIT-321.md), Deferred) and does not appear in this paper, which works with subspaces and matrix elements.
- That the rule is exact rather than an idealisation.

## Connections

- [LIT-313](../literature.d/LIT-313.md) (Gelfand–Naimark §4, [NOTE-303](../notes.d/NOTE-303.md)): factors are the algebras with trivial centre, so an algebra with sectors is not a factor.
- [LIT-352](../literature.d/LIT-352.md) (Murota et al., [NOTE-276](../notes.d/NOTE-276.md)): the simple components of a finite matrix *-algebra, found by block-diagonalisation, play the role of sectors for a finite family of observables.
- [THEORY-017](THEORY-017.md): which operators are observables is data beyond the Hilbert space. Here the symmetry group supplies the decomposition.
