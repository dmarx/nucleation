---
number: 1382
status: Proposed
formerly:
- THEORY-tmp99dad
promote_when: >-
  A reading of the proof's tractability half (the block-minimality
  algorithm of §3 and Part II's lemmas), or of a refereed account that
  checks it, confirms that every finite idempotent algebra with a weak
  near-unanimity term has a polynomial-time CSP; the theorem's statement is
  already confirmed by Zhuk's independent proof.
title: 'Bulatov shows that for every finite constraint language over a finite domain, deciding satisfiability is solvable in polynomial time when the language has a weak near-unanimity polymorphism, and with the hardness already known this makes every such problem polynomial-time solvable or NP-complete'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2115
summary: >-
  Bulatov (2017), [LIT-2115](../literature.d/LIT-2115.md), read in part in [NOTE-1572](../notes.d/NOTE-1572.md) (§§1–2 and
  the opening of §3; the proofs not read). Proposed: the tractability
  algorithm and its 80 pages of proof were not checked. It concerns
  decision problems over a fixed finite language on a finite domain. It
  does not classify systems or single instances, and says nothing about
  infinite domains or about moving between solutions.
---
<!-- inactive-ok-file: NOTE-1572 — Skimmed and new, or Proposed; cited from the reading of Bulatov (2017) as open -->

# THEORY-1382: Bulatov shows that for every finite constraint language over a finite domain, deciding satisfiability is solvable in polynomial time when the language has a weak near-unanimity polymorphism, and with the hardness already known this makes every such problem polynomial-time solvable or NP-complete

## Source

Bulatov (2017), [LIT-2115](../literature.d/LIT-2115.md); read in [NOTE-1572](../notes.d/NOTE-1572.md).

## What was actually shown

- **The dichotomy** (Theorem 1, p. 4): "For any finite constraint language Γ
  over a finite set the problem CSP(Γ) is either solvable in polynomial
  time or is NP-complete."
- **The algebraic form** (Theorem 4, p. 8): for a finite idempotent algebra,
  polynomial-time solvability is equivalent to "A has a weak near-unanimity
  term operation". Languages reduce to idempotent algebras by adding the
  constant relations ([26]).
- **What is the paper's own**: the algorithm. "The hardness part of the
  conjecture has been known for long time" (p. 4).
- **Why polymorphisms decide it** (Theorem 3, p. 6, from Jeavons et al.):
  inclusion of polymorphisms gives a reduction between the problems.
- The proof of the algorithm's correctness, Part II, was not read.

## What this does not say

- That a system, or a single instance, has a complexity class: the theorem
  classifies the family CSP(Γ) of all instances over a fixed language.
- That polymorphisms are operations a system performs: they act
  coordinatewise on the tuples of the relations.
- Anything about infinite domains, or continuous configuration spaces,
  without a finite-domain encoding.
- Anything about the connectivity of the solution space or the
  reachability of one solution from another; it is about whether a
  solution exists, the first of [CLAIM-567](../claims.d/CLAIM-567.md)'s three properties.
- That the Pol–Inv correspondence is a Galois connection: true and
  standard, but not stated in the paper.
