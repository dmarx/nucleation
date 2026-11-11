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

- **The parent question.** [QUESTION-120](../questions.d/QUESTION-120.md) (the record's; Open, version 5):
  whether, beyond distances and sparse recovery, random features for
  kernels, the superposition toy model's bound and phase changes, and the
  expand-and-threshold codes of sparse distributed memory and the fly are
  one concentration-of-measure fact applied to different families, and
  whether each threshold counts the same thing. Its readings found
  nothing that reaches random features or expand-and-threshold; for the
  latter the record holds two candidate forms, [THEORY-261](../theory.d/THEORY-261.md)'s SDM optimum and
  [THEORY-388](../theory.d/THEORY-388.md)'s LSH exponent, "and neither is the proposed shape".
- **The part answered.** [QUESTION-251](../questions.d/QUESTION-251.md) (split from [QUESTION-120](../questions.d/QUESTION-120.md) under
  [ADR-049](../decisions.d/ADR-049.md); Answered): for sufficiency, yes, one per-vector tail and a
  union bound give both the distance threshold ([THEORY-397](../theory.d/THEORY-397.md)) and the
  restricted isometry property ([THEORY-390](../theory.d/THEORY-390.md)); for necessity, no, the
  distance lower bounds are encoding and bit-counting arguments
  ([THEORY-395](../theory.d/THEORY-395.md), [THEORY-399](../theory.d/THEORY-399.md)), recovery's rests on Gelfand widths and its
  sharp location on face counting ([THEORY-391](../theory.d/THEORY-391.md)). "So the two sufficiency
  proofs are one argument over two families."
- **Universality of the transition.** [QUESTION-168](../questions.d/QUESTION-168.md) (filed by the promotion
  audit when it narrowed [THEORY-391](../theory.d/THEORY-391.md); Open): whether the ℓ₁ recovery
  transition of some non-Gaussian ensemble provably converges to the
  Gaussian curve, or simulations an order of magnitude beyond N = 1600
  keep the gap shrinking as N^(−1/2). "More simulations at the same sizes
  do not settle it."

## The components

- [QUESTION-120](../questions.d/QUESTION-120.md), the record's, Open; formal-apparatus only.
- [QUESTION-251](../questions.d/QUESTION-251.md), split under [ADR-049](../decisions.d/ADR-049.md), Answered; formal-apparatus only;
  refines [QUESTION-120](../questions.d/QUESTION-120.md).
- [QUESTION-168](../questions.d/QUESTION-168.md), the promotion audit's, Open; formal-apparatus only;
  refines [QUESTION-120](../questions.d/QUESTION-120.md).

## Links the components state, and where

Two pairs are linked, both by `refines`:

- **[QUESTION-251](../questions.d/QUESTION-251.md) refines [QUESTION-120](../questions.d/QUESTION-120.md).** [QUESTION-120](../questions.d/QUESTION-120.md)'s version 5 note
  and its closing "Split" paragraph name [QUESTION-251](../questions.d/QUESTION-251.md) and its answers;
  [QUESTION-251](../questions.d/QUESTION-251.md)'s "What it leaves to [QUESTION-120](../questions.d/QUESTION-120.md)" names what stays: the
  superposition model, random features, expand-and-threshold, and whether
  log(2 + ε²n)/ε² dimensions suffice for one set.
- **[QUESTION-168](../questions.d/QUESTION-168.md) refines [QUESTION-120](../questions.d/QUESTION-120.md).** It moved [THEORY-391](../theory.d/THEORY-391.md)'s former
  promote_when; [QUESTION-120](../questions.d/QUESTION-120.md) keeps whether the superposition model's phase
  changes are the Donoho–Tanner transition.

[QUESTION-168](../questions.d/QUESTION-168.md) and [QUESTION-251](../questions.d/QUESTION-251.md) name each other nowhere, though both turn on
[THEORY-391](../theory.d/THEORY-391.md).

## Links to other parts, stated

None. No member names a member of another part account of this line or an entry the line account integrates directly, and none of them names a member here. [CLAIM-313](../claims.d/CLAIM-313.md) of the gluing
account ([SYNTHESIS-tmphb9rl](SYNTHESIS-tmphb9rl.md)) cites [THEORY-388](../theory.d/THEORY-388.md), which [QUESTION-120](../questions.d/QUESTION-120.md) names for the
expand-and-threshold thread.

## Where else these entries are integrated

Nowhere.

## Not stated on the record

Tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5 at this review and not filed:

- **A proof for [QUESTION-168](../questions.d/QUESTION-168.md) would be another non-concentration
  argument.** That if the transition's universality is proved, the proof
  goes through face counting or another route than a union bound, as
  [QUESTION-251](../questions.d/QUESTION-251.md) finds for the sharp location. The record holds no such
  proof and no reason the route is fixed; the sentence predicts the method
  of an unwritten proof. Fails: no route.

## What it does not say

- That the thresholds of random features, superposition or
  expand-and-threshold maps are, or are not, of the proposed shape; that
  is [QUESTION-120](../questions.d/QUESTION-120.md), Open.
