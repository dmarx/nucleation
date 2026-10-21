---
number: 647
status: Proposed
formerly:
- THEORY-tmpux6wn
promote_when: >-
  An account of what fixes the context level of belief that could be
  checked without collapsing into a fixed threshold, together with evidence
  that reasoners accept the conjunction of a few believed propositions and
  refuse the conjunction of many, with the switch tracking the context and
  not a probability cut-off. It is refuted if any operational version of
  the level reduces to the threshold model, which the thesis says happens
  with any explicit boundary (§3.5.5), or if conjunction behaviour tracks a
  fixed probability. More proofs inside relative analysis cannot settle it;
  they show the model is consistent, not that belief works this way.
title: "If outright belief is credence ultraclose to 1 relative to a context level, conjunction holds for any standard ('few') number of believed propositions and fails for an ultralarge number, which dissolves the Lottery Paradox as an accumulation of negligible rounding errors"
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    The promotion audit (batch 078) split this THEORY's conditional result
    off as THEORY-tmpicur7, Active, re-derived from finite subadditivity
    and Hrbacek's Closure principle (ADR-040, ADR-047 v2). This THEORY
    keeps Wenmackers's thesis that outright belief works this way and that
    the Lottery Paradox dissolves; it now extends the split result, stays
    Proposed, and its promote_when is unchanged. Title unchanged.
tags:
- epistemology
- logic
extends:
- THEORY-tmpicur7
date: '2026-10-16'
source:
- LIT-163
summary: >-
  Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapter 3, read in [NOTE-139](../notes.d/NOTE-139.md). Stratified
  Belief, B(x) iff P(x) ≃_V 1 in Hrbacek's relative analysis, satisfies a
  Stratified Conjunction Principle for a standard number of conjuncts
  (proved) and fails for an ultralarge number. The proofs hold inside the
  framework. That belief works this way is argued: any explicit threshold
  collapses the model back to the Lockean one, the author calls it
  "crude", and knowledge is set aside.
---
<!-- inactive-ok-file: LIT-171 — Unavailable; a neighbour on credence and belief, not engaged -->

# THEORY-647: If outright belief is credence ultraclose to 1 relative to a context level, conjunction holds for any standard ('few') number of believed propositions and fails for an ultralarge number, which dissolves the Lottery Paradox as an accumulation of negligible rounding errors

## Source

Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapters 3 and 4, read in full in [NOTE-139](../notes.d/NOTE-139.md).

## What was actually shown

**The problem.** The threshold Lockean thesis (believe x iff P(x) ≥ θ < 1)
violates the conjunction principle even for two beliefs (eq. 3.3, proved).
In a large fair lottery one believes of each ticket that it loses, and not
that all lose.

**The diagnosis (§4.2).** The infinite lottery's failure of countable
additivity and the Lottery Paradox's failure of conjunction are cast as one
"adding problem": each term carries a negligible rounding error, and many
times small is not small.

**The model.** In Hrbacek's relative analysis, with levels as a context
parameter and ≃_V meaning ultraclose at level V:

- **Stratified Belief (Def. 1, eq. 3.4).** B(x) iff P(x) ≃_V 1.
- **Stratified Conjunction Principle (Def. 2, eq. 3.5).** If both
  conjuncts are ultraclose to 1 at V, so is their conjunction, by a short
  proof, extended in §3.6.3.2 to any standard number of conjuncts.
- **Its limit.** For an ultralarge number N of conjuncts it fails
  (1 − N/N = 0).
- **A threshold variant, SB_θ (Def. 3).** P(x) ≳_V θ keeps conjunction only
  for an arbitrary event plus a singleton. It is offered as a model of
  epistemicist vagueness.

Rational belief about a fair infinite lottery then takes two roundings:
first to the standard part, then relative-infinitesimal rounding (§4.4).

**What could have come out otherwise.** The conjunction rule could have
failed inside the framework even for two conjuncts. It does not. That is a
result about the model, not about believers.

## What this does not say

- **That belief has levels.** Relative analysis's levels have no explicit
  boundary by design. Any explicit threshold collapses the model to the
  standard one (§3.5.5, §3.7.2.1), so it is not operational. The author
  calls it "a crude model" (§3.6.4).
- **That it is psychologically real.** The support is an analogy with
  Dehaene's mental number line (C10, weak).
- **That the Lottery Paradox is a vagueness problem.** That is argued
  informally (C9, weak).
- **Anything about knowledge.** The knowledge version is explicitly set
  aside (fn. 1, fn. 22). The bank case and voting-paradox applications are
  sketches (§3.7).
- **That belief is graded.** Belief is binary here. One context level is
  allowed per agent at a time.

## Note, 2026-10-21

The conditional result in this title, that conjunction holds for any
standard number of believed propositions and can fail for an ultralarge
number, is now [THEORY-tmpicur7](THEORY-tmpicur7.md), Active, with the re-derivation written out.
The title's "fails for an ultralarge number" is stronger than what is
proved: conjunction *can* fail for an ultralarge number (the fair lottery),
not for every ultralarge collection. What stays open here is the thesis:
that belief has context levels and that the Lottery Paradox is an
accumulation of negligible rounding errors.

## Connections

- It extends [THEORY-tmpicur7](THEORY-tmpicur7.md), the conditional result inside relative
  analysis.

- It applies the rounding diagnosis of the thesis's lottery construction
  ([THEORY-401](THEORY-401.md)) to belief.
- Pettigrew's accuracy-first credence ([LIT-171](../literature.d/LIT-171.md)) is a neighbour on the
  relation of credence to outright belief. It is not engaged, and the
  thesis predates it.
