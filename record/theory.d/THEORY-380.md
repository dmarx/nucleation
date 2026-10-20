---
number: 380
status: Active
formerly:
- THEORY-tmplwy86
title: "For datalog over a finite input instance annotated from a commutative ω-continuous semiring, with an answer's tag defined as the sum over its derivation trees of the product of its leaves' tags, the tags are the least fixed point of a finite polynomial system and factor through formal power series N∞⟦X⟧ in the input tuple ids; an answer tuple's series has an infinite coefficient exactly when one of its derivation trees contains a tuple lying on a cycle of unit rules"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Corrected and promoted, carrying out the promotion audit's decision
    for THEORY-380 (batch 054, ADR-047 v2). The paper states Theorems 5.6,
    6.4 and 6.5 without proof; the dated note below proves all three, which
    is the read proof the promote_when asked for. The input instance is
    made explicit as finite. The infinite-coefficient clause is corrected:
    as the paper states it, with the unit-rule cycle passing through the
    tuple itself, it is false. A cycle on any tuple in one of the tuple's
    derivation trees suffices, and the note gives a four-rule
    counterexample. The paper's own Monomial-Coefficient algorithm already
    uses the corrected condition.
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

# THEORY-380: For datalog over a finite input instance annotated from a commutative ω-continuous semiring, with an answer's tag defined as the sum over its derivation trees of the product of its leaves' tags, the tags are the least fixed point of a finite polynomial system and factor through formal power series N∞⟦X⟧ in the input tuple ids; an answer tuple's series has an infinite coefficient exactly when one of its derivation trees contains a tuple lying on a cycle of unit rules

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

## Note of 2026-10-20: the three theorems, proved

Proved for the promotion audit (batch 054, [ADR-047](../decisions.d/ADR-047.md) v2). The paper states
Theorems 5.6, 6.4 and 6.5 without proof. Taken as given: in a commutative
ω-continuous semiring K, a countable sum (the supremum of its finite
partial sums) does not depend on order or grouping, + and · distribute
over it, and an ω-continuous map has least fixed point sup_n T^n(0)
(Kleene). The input instance is finite, so the instantiated program has
finitely many IDB tuples N and finitely many rules.

1. **Least fixed point (Theorem 5.6).** The immediate consequence operator
   T sends x to the vector whose t-component is the sum, over instantiated
   rules with head t, of the product of the body's EDB tags and IDB
   components x_u. T is polynomial, hence ω-continuous. By induction,
   T^n(0)_t is the sum over derivation trees of t of height at most n of
   the product of their leaf tags: for n + 1, distribute the finite product
   over the finite sums T^n(0)_u, which gives one term per rule for t and
   choice of a height-≤n tree for each IDB body atom. Every finite set of
   trees lies within some height, so the least fixed point sup_n T^n(0)_t
   is the countable sum over all of t's trees, Definition 5.1's tag. This
   holds when the tag is 0 as well.
2. **Factorization (Theorem 6.4).** With each input tuple tagged by its id,
   t's provenance is Σ_μ N_μ μ in N∞⟦X⟧, where N_μ counts t's trees with
   fringe μ. For a valuation ν: X → K let Eval_ν(Σ c_μ μ) = Σ c_μ·ν(μ), with
   ∞·a = sup_n n·a. Regrouping the countable sum gives
   Eval_ν(prov(t)) = Σ over trees of the product of ν at the leaves, which
   is t's tag in the K-relation with tags ν. Eval_ν is an ω-continuous
   semiring homomorphism.
3. **Infinite coefficients (Theorem 6.5, corrected).** A unit rule has a
   single IDB atom as its body. *If* a tree τ of t contains a tuple u with
   a cycle of unit rules back to u, splicing the cycle in above u's node m
   times gives distinct trees with τ's fringe, so that coefficient is ∞.
   *Only if*: suppose no tree of t contains a tuple on a unit cycle, and
   take a fringe of degree m. At most m internal nodes have a leaf child,
   and at most m − 1 have two or more internal children. Every other
   internal node has exactly one internal child, and those nodes form at
   most 2m − 1 vertical chains. A chain cannot repeat a tuple, since that
   would be a unit cycle, so it has at most N nodes. The tree then has at
   most (2m − 1)(N + 1) internal nodes, so there are finitely many such
   trees and every coefficient is finite.
4. **Why the paper's wording fails.** Theorem 6.5 asks for a unit-rule cycle
   with t itself on it. Take EDB facts e, f and the instantiated rules
   u ← e, v ← u, u ← v and t ← u, f. Then t is on no unit cycle, but u has
   infinitely many trees with fringe e, so the coefficient of e·f in t's
   series is ∞. Counting t's trees by height gives 0, 1, 1, 2, 2, 3, 3, …
   with no bound. As written, the paper's "t is in the result" conjunct
   also fails for a tuple with no derivation: its series is 0, which has no
   ∞ coefficient. The Monomial-Coefficient algorithm (Figure 9) marks a
   tree infinite when any child pair is, which is the corrected
   condition, so the algorithms are unaffected.
