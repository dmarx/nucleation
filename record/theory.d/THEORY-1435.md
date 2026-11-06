---
number: 1435
status: Active
formerly:
- THEORY-tmpzax66
title: 'Marsden and Zwart propose that quantitative resource theories are categories enriched in a commutative quantale, whose monoid combines the costs, probabilities or strengths of successive conversion steps and whose join selects the best alternative, with costly conversions as profunctors and closure under composition as a free internal monad'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review of 2026-11-06, at the status review's
    ruling (the owner delegated these rulings), under ADR-065 §2. The title
    reports what Marsden and Zwart propose, NOTE-1602 read the paper in
    full, and nothing in the record contradicts the report. The old
    promote_when: "A reading that checks the proofs (in the paper or a full
    version) confirms that the paper defines resource conversions as
    categories and profunctors enriched in a commutative quantale, with the
    Lawvere, interval and multiplicative quantales as examples, and that
    every endomorphism generates a free internal monad by
    reflexive–transitive closure (Proposition 37, Corollary 38)." Its
    definitional part is met by NOTE-1602. The truth of the closure result,
    which the paper asserts, moves with the condition word for word to
    THEORY-1527, which extends this entry (ADR-047 kind 1, ADR-065 §3).
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2054
summary: >-
  Marsden & Zwart (CSL 2018), [LIT-2054](../literature.d/LIT-2054.md), read in full in [NOTE-1602](../notes.d/NOTE-1602.md).
  The paper's proofs are sketches and were not checked further; the
  closure result is THEORY-1527's.
  It uses one quantale per theory and static resources. It does not say
  anything about several quantities at once beyond a product quantale,
  whose componentwise join loses a Pareto frontier of budgets, nor about
  costs that depend on the order of operations, nor about graded
  categories that keep every morphism with its grade.
---
<!-- inactive-ok-file: THEORY-1527 — Proposed and new; the closure result split off at the status review of 2026-11-06, cited as open -->

# THEORY-1435: Marsden and Zwart propose that quantitative resource theories are categories enriched in a commutative quantale, whose monoid combines the costs, probabilities or strengths of successive conversion steps and whose join selects the best alternative, with costly conversions as profunctors and closure under composition as a free internal monad

## Source

Marsden & Zwart (2018), [LIT-2054](../literature.d/LIT-2054.md); read in [NOTE-1602](../notes.d/NOTE-1602.md).

## What was actually shown

- **The quantale reading** (§2.1): the monoid "allows us to combine
  quantities across the different steps of a process or algorithm", and
  the join "is then an optimizer".
- **Examples**: the Lawvere quantale ([0, ∞], inf, +) for costs (Examples
  4, 9), the interval quantale with min for connection strengths
  (Example 8), and a multiplicative quantale for success probabilities.
- **Free and costly**: base Q-categories and Q-profunctors (Defs. 6, 15,
  18); free constructions and distributive laws giving comonads
  (Theorems 27–28, Corollary 29), with proofs sketched.
- **Closure** (Proposition 37, Corollary 38): every endomorphism generates a
  free internal monad by reflexive–transitive closure.

## What this does not say

- That the peak-capacity law (max along a path) is an example: it is not
  among the paper's, though it satisfies the definition (the reader's
  check, [NOTE-1602](../notes.d/NOTE-1602.md)).
- That several quantities can be kept together without loss: a product
  quantale's join is componentwise.
- That the morphisms within a budget form a category: they do only when
  b ⊗ b ≤ b (the reader's derivation).
- Anything about dynamics, replenishment or state-dependent cost.
