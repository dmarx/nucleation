---
status: Proposed
title: 'The thresholds for random maps that keep distances and sparse supports share one sufficiency argument and not a necessity argument, while whether random features, superposition and expand-and-threshold maps fall under the same concentration fact, and whether the sparse-recovery transition is universal beyond Gaussian ensembles, stay open'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the random-projection part of the formal-apparatus line left out
  without a reason given; or a link this account states that no component
  states. Its standing is its components': a component retired or demoted
  takes its clause with it, and nothing here holds the clause up.
tags:
- mathematics
- learning-theory
- mathematical-statistics
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- QUESTION-120
- QUESTION-251
- QUESTION-168
---
<!-- inactive-ok-file: ADR-075 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: QUESTION-251 — Answered; cited with its standing -->
<!-- inactive-ok-file: SYNTHESIS-tmphb9rl — Proposed; cited with its standing -->

# SYNTHESIS-tmppyfkv: The thresholds for random maps that keep distances and sparse supports share one sufficiency argument and not a necessity argument, while whether random features, superposition and expand-and-threshold maps fall under the same concentration fact, and whether the sparse-recovery transition is universal beyond Gaussian ensembles, stay open

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, three questions, all first in formal-apparatus, from the
survey of 2026-10-14 that found random projections in three places of the
record and the Johnson–Lindenstrauss lemma in none. The line's account is
built over it and its sibling parts. No other account integrates them.*

## The account

- **The parent question.** QUESTION-120 (the record's; Open, version 5):
  whether, beyond distances and sparse recovery, random features for
  kernels, the superposition toy model's bound and phase changes, and the
  expand-and-threshold codes of sparse distributed memory and the fly are
  one concentration-of-measure fact applied to different families, and
  whether each threshold counts the same thing. Its readings found
  nothing that reaches random features or expand-and-threshold; for the
  latter the record holds two candidate forms, THEORY-261's SDM optimum and
  THEORY-388's LSH exponent, "and neither is the proposed shape".
- **The part answered.** QUESTION-251 (split from QUESTION-120 under
  ADR-049; Answered): for sufficiency, yes, one per-vector tail and a
  union bound give both the distance threshold (THEORY-397) and the
  restricted isometry property (THEORY-390); for necessity, no, the
  distance lower bounds are encoding and bit-counting arguments
  (THEORY-395, THEORY-399), recovery's rests on Gelfand widths and its
  sharp location on face counting (THEORY-391). "So the two sufficiency
  proofs are one argument over two families."
- **Universality of the transition.** QUESTION-168 (filed by the promotion
  audit when it narrowed THEORY-391; Open): whether the ℓ₁ recovery
  transition of some non-Gaussian ensemble provably converges to the
  Gaussian curve, or simulations an order of magnitude beyond N = 1600
  keep the gap shrinking as N^(−1/2). "More simulations at the same sizes
  do not settle it."

## The components

- QUESTION-120, the record's, Open; formal-apparatus only.
- QUESTION-251, split under ADR-049, Answered; formal-apparatus only;
  refines QUESTION-120.
- QUESTION-168, the promotion audit's, Open; formal-apparatus only;
  refines QUESTION-120.

## Links the components state, and where

Two pairs are linked, both by `refines`:

- **QUESTION-251 refines QUESTION-120.** QUESTION-120's version 5 note
  and its closing "Split" paragraph name QUESTION-251 and its answers;
  QUESTION-251's "What it leaves to QUESTION-120" names what stays: the
  superposition model, random features, expand-and-threshold, and whether
  log(2 + ε²n)/ε² dimensions suffice for one set.
- **QUESTION-168 refines QUESTION-120.** It moved THEORY-391's former
  promote_when; QUESTION-120 keeps whether the superposition model's phase
  changes are the Donoho–Tanner transition.

QUESTION-168 and QUESTION-251 name each other nowhere, though both turn on
THEORY-391.

## Links to other parts, stated

None. No member names a member of another part account of this line or an entry the line account integrates directly, and none of them names a member here. CLAIM-313 of the gluing
account (SYNTHESIS-tmphb9rl) cites THEORY-388, which QUESTION-120 names for the
expand-and-threshold thread.

## Where else these entries are integrated

Nowhere.

## Not stated on the record

Tested by ADR-075's step 5 at this review and not filed:

- **A proof for QUESTION-168 would be another non-concentration
  argument.** That if the transition's universality is proved, the proof
  goes through face counting or another route than a union bound, as
  QUESTION-251 finds for the sharp location. The record holds no such
  proof and no reason the route is fixed; the sentence predicts the method
  of an unwritten proof. Fails: no route.

## What it does not say

- That the thresholds of random features, superposition or
  expand-and-threshold maps are, or are not, of the proposed shape; that
  is QUESTION-120, Open.
