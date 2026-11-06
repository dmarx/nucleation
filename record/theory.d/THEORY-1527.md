---
number: 1527
status: Proposed
formerly:
- THEORY-tmpif6q2
promote_when: >-
  A reading that checks the proofs (in the paper or a full version)
  confirms that the paper defines resource conversions as categories and
  profunctors enriched in a commutative quantale, with the Lawvere,
  interval and multiplicative quantales as examples, and that every
  endomorphism generates a free internal monad by reflexive–transitive
  closure (Proposition 37, Corollary 38).
title: 'Every endomorphism in Marsden and Zwart''s categories of quantale-enriched profunctors generates a free internal monad, its reflexive–transitive closure (Proposition 37, Corollary 38)'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-sixth status review (ADR-057), at the status review's
    ruling (the owner delegated these rulings): a second checker followed
    the re-derivation of Proposition 37 for Q-profunctors (ADR-065 §5) and
    found it correct, with two steps made explicit (a join of profunctors is
    a profunctor; in a locally posetal 2-category the least monad above R is
    the free one). The condition also asks for Corollary 38, which is not
    re-derived. A blocker note is added. No status change; the title and
    condition are unchanged.
tags:
- mathematics
- operations-research
date: '2026-11-06'
source:
- LIT-2054
extends:
- THEORY-1435
summary: >-
  The closure result of Marsden & Zwart (CSL 2018), [LIT-2054](../literature.d/LIT-2054.md), read in full
  in [NOTE-1602](../notes.d/NOTE-1602.md), whose proofs the paper sketches. Split from [THEORY-1435](THEORY-1435.md) by
  the status review of 2026-11-06 ([ADR-047](../decisions.d/ADR-047.md) kind 1, [ADR-065](../decisions.d/ADR-065.md) §3): that entry
  reports the proposal and is Active; this one asserts the result and keeps
  the old condition word for word. A re-derivation of Proposition 37 for
  Q-profunctors is below, awaiting a second checker ([ADR-065](../decisions.d/ADR-065.md) §5); Corollary
  38's wider scope is not re-derived.
---

# THEORY-1527: Every endomorphism in Marsden and Zwart's categories of quantale-enriched profunctors generates a free internal monad, its reflexive–transitive closure (Proposition 37, Corollary 38)

## Source

Marsden & Zwart (2018), [LIT-2054](../literature.d/LIT-2054.md); read in [NOTE-1602](../notes.d/NOTE-1602.md). The proposal is [THEORY-1435](THEORY-1435.md)'s.

## What was actually shown

The paper states Proposition 37 and Corollary 38 with proofs sketched: "Every
endomorphism in our categories of interest can be used to construct a free
internal monad using the reflexive transitive closure construction of
proposition 37" ([NOTE-1602](../notes.d/NOTE-1602.md)).

**Proposition 37 for Q-profunctors, re-derived** (by the reviewer of
2026-11-06; a second checker must follow each step before a ruling):

- Let R : A ⇸ A be a Q-profunctor, Rⁿ its n-fold composite, and R⁰ = A,
  the identity profunctor.
- A profunctor composite is a join over intermediates of ⊗, and ⊗
  distributes over all joins, so composition preserves joins in each
  argument.
- Put R* = ⋁_{n≥0} Rⁿ. Then A = R⁰ ≤ R*, and R* ∘ R* = ⋁_{m,n} R^{m+n} = R*.
  So R* is an internal monad in the sense of Definition 22, and R ≤ R*.
- If M is a monad with R ≤ M, then R⁰ = A ≤ M, and if Rⁿ ≤ M then
  R^{n+1} = R ∘ Rⁿ ≤ M ∘ M ≤ M. So R* ≤ M: R* is the least monad above R,
  which, the 2-cells being inclusions, is the free one. R* is a
  Q-profunctor, since the action inequalities survive joins by
  distributivity; and since Prof(Q) is locally posetal, a monad morphism
  R* → M is just R* ≤ M, so the least monad above R has the free monad's
  universal property.

Second check of 2026-11-06: each step followed; correct with the two
clauses above.

## What this does not say

- That Corollary 38 holds in the co-Kleisli categories of the free
  constructions: whether composition there preserves joins was not checked.
- That the free constructions of Theorems 27–28 hold; their proofs are also
  sketched.
- Anything beyond static resources and one quantale per theory.

## Note of 2026-11-06: what holds it back

Proposition 37 is re-derived and checked for Q-profunctors; the condition also asks for Corollary 38, in the co-Kleisli categories of the free constructions, where the closure argument needs composition to preserve joins and nobody has checked that it does. It waits on that check, or on a reading of a full version's proof.
