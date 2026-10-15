---
number: 380
status: Proposed
formerly:
- THEORY-tmplwy86
promote_when: >-
  A read proof of Theorems 5.6, 6.4 and 6.5, which this paper states
  without proof (a journal or thesis version by the authors would do), or an
  independent proof of the fixed-point characterization and the
  factorization through formal power series for commutative ω-continuous
  semirings. Worked examples and the paper's algorithms cannot settle it;
  they presuppose the theorems.
title: "For datalog on relations annotated from a commutative ω-continuous semiring, with an answer's tag defined as the sum over its derivation trees of the product of its leaves' tags, the tags are the least fixed point of a finite polynomial system and factor through formal power series N∞⟦X⟧ in the input tuple ids; an answer tuple's series has an infinite coefficient exactly when the tuple lies on a cycle of unit rules"
version: 1
tags:
- databases
- mathematics
- logic
date: '2026-10-15'
source:
- LIT-1110
extends:
- THEORY-373
summary: >-
  Green, Karvounarakis and Tannen (2007), [LIT-1110](../literature.d/LIT-1110.md), read in [NOTE-913](../notes.d/NOTE-913.md).
  A recursive query can derive a tuple in infinitely many ways, so
  polynomials do not suffice and the semiring needs infinite sums. With
  ω-continuous semirings and the provenance semiring N∞⟦X⟧ the paper
  states the analogues of the relational results: a fixed-point
  characterization (Theorem 5.6), factorization (Theorem 6.4), and a test
  for infinite coefficients (Theorem 6.5), with algorithms that decide
  finiteness and compute coefficients. Proofs are not given. Plain N and
  N[X] are excluded, the provenance can be an infinite object held only as
  equations, and negation remains outside.
---

# THEORY-380: For datalog on relations annotated from a commutative ω-continuous semiring, with an answer's tag defined as the sum over its derivation trees of the product of its leaves' tags, the tags are the least fixed point of a finite polynomial system and factor through formal power series N∞⟦X⟧ in the input tuple ids; an answer tuple's series has an infinite coefficient exactly when the tuple lies on a cycle of unit rules

## Source

Green, Karvounarakis and Tannen (2007), [LIT-1110](../literature.d/LIT-1110.md) (PODS 2007), read in
[NOTE-913](../notes.d/NOTE-913.md): Sections 5–8, Definitions 5.1, 5.5 and 6.1, Propositions
5.2–5.4, 5.7, 6.2 and 6.3, Theorems 5.6, 6.4 and 6.5, Figures 7–9.

## What was actually shown

**The semantics.** For pure datalog over a countable domain, the tag of an
answer is the sum over all its derivation trees of the product of the tags
at the leaves (Definition 5.1). This needs countable sums, so K must be
commutative and ω-continuous: naturally ordered, with least upper bounds of
ω-chains and continuous operations. Booleans, N∞, PosBool(B) for finite B,
event sets, the tropical and the fuzzy semirings qualify; N and N[X] do not.
Over the Booleans this is ordinary datalog (Proposition 5.4), and on
non-recursive translations of RA+ queries with equality selections it
agrees with the relational semantics (Propositions 5.3, 6.2).

**The theorems, as stated.** Each nonzero tag is the corresponding
component of the least fixed point of the finite algebraic system built
from the immediate consequence operator (Theorem 5.6). With N∞⟦X⟧ as the
provenance semiring, "The semantics of datalog on K-relations for any
commutative ω-continuous semiring K factors through the semantics of the
same in provenance semirings (of formal power series)" (Theorem 6.4). A
tuple's series has no ∞ coefficient if and only if it is in the result and
the instantiated program has no cycle of unit rules through it (Theorem
6.5). Algorithm All-Trees decides whether a series is a polynomial and
computes it; Monomial-Coefficient computes any single coefficient, ∞
included. For a finite distributive lattice a modified All-Trees always
terminates with polynomials, which gives datalog on Boolean c-tables and
on event tables over a finite domain.

**Why it is Proposed.** These theorems are stated without proof in the
paper; only Proposition 5.2 has a sketch. The record has not read a proof.

## What this does not say

- **That datalog provenance is a finite object.** A tuple's provenance can
  be an infinite series (in the transitive-closure example,
  v = s + s² + 2s³ + 5s⁴ + 14s⁵ + ⋯), held finitely only as a system of
  equations, with coefficients computable one at a time.
- **Anything about cost.** Termination is argued for the algorithms; no
  complexity bounds are given.
- **Anything for negation or stratified datalog.** Only pure positive
  datalog is treated.
- **That the tropical semiring is handled.** The authors leave an
  evaluation procedure for it as a conjecture.

## Connections

- [THEORY-373](THEORY-373.md) is the non-recursive case; this extends it to recursion.
- [QUESTION-105](../questions.d/QUESTION-105.md): for a record whose conclusions support each other in
  cycles, the retained state that factors every semiring revision is an
  equation system, not a list of supports.
- [CLAIM-303](../claims.d/CLAIM-303.md): when derivations recur, dependency tracking stores equations
  whose solution is computed on demand, a mixed position in the trade.
