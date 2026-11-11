---
status: Proposed
title: 'Ideal-observer efficiency is not the empirical measure of the gap computational indistinguishability describes: a constrained ideal observer is the optimal decoder of a degraded input, so efficiency measures what a real observer loses against an input garbled at some stage, while indistinguishability keeps the input and restricts the class of tests; the two gaps are those of different receivers, and the record holds no measure of the second on real observers'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A definition of efficiency in a work read by the record that compares a
  real observer with the best decoder in a restricted class of
  computations on the undegraded input, rather than with the optimal
  decoder of a degraded one; or a showing, for the observer classes
  computational indistinguishability uses, that the best test in the
  class performs as the ideal observer of one fixed garbling of the input
  does, so that the two gaps coincide. Not defeated by further efficiency
  measurements, which measure the first gap again, or by the ROC reading
  of a test's advantage, which the claim keeps.
tags:
- probabilistic-modeling
- cognition
- information-theory
date: '2026-11-11'
line:
- formal-apparatus
grounds:
- THEORY-336
- THEORY-357
- THEORY-031
- THEORY-349
answers:
- QUESTION-103
summary: >-
  An offered part-answer to QUESTION-103, on its second limb: whether
  ideal-observer efficiency is the empirical measure of computational
  indistinguishability. The question's note of 2026-10-15 found the
  bridge narrower than first stated, and THEORY-336 says so in its own
  connections ("efficiency, so defined, measures the first gap"), but no
  entry of the argument states it. The first limb, whether
  indistinguishability is the bounded-observer form of signal detection's
  chance ROC, and its criterion question stay open. Drafted by the reading
  review of 2026-11-11, by question. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

# CLAIM-tmpqmfkl: Ideal-observer efficiency is not the empirical measure of the gap computational indistinguishability describes: a constrained ideal observer is the optimal decoder of a degraded input, so efficiency measures what a real observer loses against an input garbled at some stage, while indistinguishability keeps the input and restricts the class of tests; the two gaps are those of different receivers, and the record holds no measure of the second on real observers

## The claim

QUESTION-103 asks two things: whether computational indistinguishability
is the bounded-observer form of signal detection's chance ROC, and whether
ideal-observer efficiency is its empirical measure. This answers the
second, no.

**What efficiency compares.** An ideal observer is optimal "given the
available information and any specified constraints", and its constraints
are added by passing the stimulus through a stage of the visual system,
Z = g(S; θ). So a constrained ideal is the optimal decoder of a degraded
input, not a restricted decoder of the full one (THEORY-336). Efficiency
compares a real observer with such an ideal. What it measures is how much
of the information available at a stage the observer uses.

**What indistinguishability restricts.** Computational indistinguishability
keeps the input whole and restricts the tests: no test in a bounded class
tells two ensembles apart, though their total variation is near 1
(THEORY-357). The best test in the class can sit near the chance diagonal
while the likelihood-ratio detector on the same input sits near perfect
(THEORY-031). Outcome indistinguishability does the same for predictors:
adequacy is relative to a class of distinguishers, whatever nature's
complexity (THEORY-349).

**Different receivers.** The first is a loss of information before
decoding, the second a restriction on decoding with the information
intact. CLAIM-199 separates the same two receivers, Blackwell's ceiling
and a rule class. An efficiency below one says the observer is not the
ideal for the input it was compared on. It does not say which class of
computations the observer is confined to, and a gap of the second kind
can be total with no information lost.

**What survives of the bridge.** A test's advantage is hit rate minus
false-alarm rate, a point on its ROC (THEORY-357's connections), so the
ROC reading of indistinguishability holds as a matter of definition. Its
counterpart of a criterion shift, and a measure of the restricted-class
gap that can be taken on people or models, are not in the record.

## What it does not say

- Not that efficiency is useless to the bounded-observer questions
  (QUESTION-104, QUESTION-111). It bounds what an observer can do from
  above, by the information it has.
- Not that a real observer's shortfall is never computational. A
  stage-by-stage analysis may place a loss in "central factors"
  (THEORY-336), which may be a restriction on computation. Efficiency
  does not say which class it is.
- Not an answer to the first limb, or to whether efficiency is well
  defined for a class of observers.
