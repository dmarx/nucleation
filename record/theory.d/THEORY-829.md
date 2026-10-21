---
number: 829
status: Active
formerly:
- THEORY-tmpicur7
title: "In Hrbacek's relative analysis, if belief at a context level is credence ultraclose to 1 at that level, the conjunction of any standard number of believed propositions is believed, while for an ultralarge number it can fail: in a fair lottery with an ultralarge number of tickets each 'this ticket loses' is believed and their conjunction has probability 0"
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Split from THEORY-647 by the promotion audit (batch 078, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-770's split from THEORY-673 and
    THEORY-779's from THEORY-209. THEORY-647 bundled this conditional
    result with Wenmackers's thesis that outright belief works this way
    and that the Lottery Paradox dissolves. The result was re-derived in
    the review, step by step, as written out below; THEORY-647 keeps the
    thesis and extends this one.
tags:
- mathematics
- epistemology
- probabilistic-modeling
date: '2026-10-21'
source:
- LIT-163
summary: >-
  Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), Ch. 3 (Stratified Belief, Def. 1; the
  Stratified Conjunction Principle, Def. 2, eq. 3.5 and §3.6.3.2), read in
  full in [NOTE-139](../notes.d/NOTE-139.md); re-derived by the promotion audit from finite
  subadditivity and Hrbacek's Closure principle. A result inside the
  framework: it says nothing about whether belief has levels, and any
  explicit level boundary collapses the model back to a fixed threshold.
extended_by:
- THEORY-647
---
<!-- inactive-ok-file: THEORY-647 — Proposed; the thesis this result was split from, cited for what it argues -->

# THEORY-829: In Hrbacek's relative analysis, if belief at a context level is credence ultraclose to 1 at that level, the conjunction of any standard number of believed propositions is believed, while for an ultralarge number it can fail: in a fair lottery with an ultralarge number of tickets each 'this ticket loses' is believed and their conjunction has probability 0

## Source

Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapter 3, read in full in [NOTE-139](../notes.d/NOTE-139.md). Stratified
Belief is Def. 1 (eq. 3.4), the Stratified Conjunction Principle is Def. 2
(eq. 3.5), and its extension to any standard number of conjuncts is
§3.6.3.2. The level axioms are Hrbacek's (§3.5.3.1). [NOTE-139](../notes.d/NOTE-139.md) rates the
result strong within relative analysis (C8).

## What was actually shown

Work at a context level V. A real x is V-ultrasmall if x ≠ 0 and |x| < r
for every V-standard r > 0, and x ≃_V y means x − y is V-ultrasmall or 0.
Stratified Belief: E is believed iff P(E) ≃_V 1.

**Re-derivation, step by step.** Let E₁, …, Eₙ be believed, with n
V-standard, and put eᵢ = 1 − P(Eᵢ). Each eᵢ is 0 or V-ultrasmall, and
eᵢ ≥ 0.

1. Finite subadditivity, an ordinary theorem for every finite n:
   1 − P(E₁ ∧ … ∧ Eₙ) = P(¬E₁ ∨ … ∨ ¬Eₙ) ≤ e₁ + … + eₙ.
2. Fix any V-standard r > 0. Since r and n are V-standard, r/n is
   V-standard, by the Closure principle: anything defined from V-standard
   parameters is V-standard.
3. Each eᵢ is below every V-standard positive number, so eᵢ < r/n for each
   i, and e₁ + … + eₙ < n·(r/n) = r.
4. Since r was arbitrary, the sum is 0 or V-ultrasmall. As
   1 ≥ P(E₁ ∧ … ∧ Eₙ) ≥ 1 − (e₁ + … + eₙ), the conjunction is ultraclose to
   1, so it is believed.
5. For an ultralarge number, take a fair lottery with N tickets, N
   V-ultralarge, so 1/N is V-ultrasmall. "Ticket i loses" has probability
   1 − 1/N ≃_V 1 and is believed for every i. The conjunction of all N has
   probability 0 (1 − N/N = 0), so it is not believed. Step 2 is what
   fails: r/N is not V-standard.

The argument uses Closure, not induction on n. That matters, because
induction fails across levels: a level is a predicate, not a set ([NOTE-139](../notes.d/NOTE-139.md),
glossary).

**What could have come out otherwise.** Conjunction could have failed
inside the framework even for two conjuncts, as it does for any fixed
threshold below 1 (eq. 3.3). It does not.

## What this does not say

- **That belief works this way.** That is Wenmackers's thesis, which
  [THEORY-647](THEORY-647.md) carries and which stays Proposed. Relative analysis's levels
  have no explicit boundary by design, and any explicit threshold collapses
  the model to the Lockean one (§3.5.5).
- **That conjunction fails for every ultralarge collection.** It can fail;
  N copies of a single believed proposition never do.
- **That the Lottery Paradox is dissolved.** Inside the model the
  paradox's conjunction is not believed. Whether that is the right
  diagnosis is the argument [THEORY-647](THEORY-647.md) makes.
- **Anything for the threshold variant SB_θ.** Its conjunction rule holds
  only for an arbitrary event plus a singleton (Def. 3); it is not covered
  here.

## Connections

- [THEORY-647](THEORY-647.md) extends this result into a thesis about outright belief.
- [THEORY-401](THEORY-401.md) holds the thesis's fair-lottery construction, whose rounding
  diagnosis this result applies to belief.
