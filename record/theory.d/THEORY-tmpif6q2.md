---
status: Proposed
promote_when: >-
  A reading that checks the proofs (in the paper or a full version)
  confirms that the paper defines resource conversions as categories and
  profunctors enriched in a commutative quantale, with the Lawvere,
  interval and multiplicative quantales as examples, and that every
  endomorphism generates a free internal monad by reflexive–transitive
  closure (Proposition 37, Corollary 38).
title: 'Every endomorphism in Marsden and Zwart''s categories of quantale-enriched profunctors generates a free internal monad, its reflexive–transitive closure (Proposition 37, Corollary 38)'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-06'
source:
- LIT-2054
extends:
- THEORY-1435
summary: >-
  The closure result of Marsden & Zwart (CSL 2018), LIT-2054, read in full
  in NOTE-1602, whose proofs the paper sketches. Split from THEORY-1435 by
  the status review of 2026-11-06 (ADR-047 kind 1, ADR-065 §3): that entry
  reports the proposal and is Active; this one asserts the result and keeps
  the old condition word for word. A re-derivation of Proposition 37 for
  Q-profunctors is below, awaiting a second checker (ADR-065 §5); Corollary
  38's wider scope is not re-derived.
---

# THEORY-tmpif6q2: Every endomorphism in Marsden and Zwart's categories of quantale-enriched profunctors generates a free internal monad, its reflexive–transitive closure (Proposition 37, Corollary 38)

## Source

Marsden & Zwart (2018), LIT-2054; read in NOTE-1602. The proposal is THEORY-1435's.

## What was actually shown

The paper states Proposition 37 and Corollary 38 with proofs sketched: "Every
endomorphism in our categories of interest can be used to construct a free
internal monad using the reflexive transitive closure construction of
proposition 37" (NOTE-1602).

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
  which, the 2-cells being inclusions, is the free one.

## What this does not say

- That Corollary 38 holds in the co-Kleisli categories of the free
  constructions: whether composition there preserves joins was not checked.
- That the free constructions of Theorems 27–28 hold; their proofs are also
  sketched.
- Anything beyond static resources and one quantale per theory.
