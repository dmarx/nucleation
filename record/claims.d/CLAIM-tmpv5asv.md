---
status: Proposed
title: 'Some of the slow, power-law-like relaxation seen in training deep networks may be the algebraic relaxation of degenerate singular modes rather than critical slowing down in a collective phase, and a dependency tree of feature transitions yields power laws only if its thresholds or relaxation times are themselves broadly or self-similarly distributed'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  For networks whose training shows power-law relaxation, a measurement
  showing that the slow modes are nondegenerate: perturbations along them
  decay exponentially with rates that do not approach zero, and the local
  loss is quadratic along them, so that the slowness comes from a
  continuum of small curvatures or from a diverging correlation length and
  not from higher-order degeneracy. For the second part, a finite
  dependency tree of threshold transitions with narrowly distributed
  thresholds that nonetheless yields scale-free statistics of onset times
  or event sizes.
tags:
- learning-theory
- complex-systems
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-tmpcbfdj
grounds:
- LIT-tmp0z602
- LIT-tmpv9upr
summary: >-
  A39 §5 and A43 §17 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21): "Some apparent critical slowing down may reflect
  higher-order degeneracy of the optimization landscape … It could be a
  collection of algebraically relaxing singular modes", and "a finite
  dependency tree can produce a stagewise learning process without any
  scale-free statistics". An alternative to reading training's slow modes
  as criticality. The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A39, A43); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-tmpcbfdj CLAIM-tmpuc8ro — Proposed; claims filed with this one -->
<!-- inactive-ok-file: LEAD-200 — Done; the check of relaxation over an ultrametric tree, cited for what it did -->

# CLAIM-tmpv5asv: Some of the slow, power-law-like relaxation seen in training deep networks may be the algebraic relaxation of degenerate singular modes rather than critical slowing down in a collective phase, and a dependency tree of feature transitions yields power laws only if its thresholds or relaxation times are themselves broadly or self-similarly distributed

## The claim

A39 §5: "This creates another possible origin for the broad timescale
hierarchies observed during DNN training. Some apparent critical slowing
down may reflect higher-order degeneracy of the optimization landscape. A
hierarchy of such degeneracies could generate a broad distribution of
learning times. However, that would not automatically establish a
scale-free collective phase. It could be a collection of algebraically
relaxing singular modes."

The premise is CLAIM-tmpcbfdj: a degenerate direction relaxes as a power
of t with no collective mode and no tuning to a critical point. The
claim offers this as a rival explanation of observed slow relaxation in
training, beside criticality. It does not say which explanation holds for
any network.

A43 §17 adds a limit on the other side: "A finite dependency tree can
produce a stagewise learning process without any scale-free statistics.
But if the dependency structure itself becomes self-similar, or if the
relevant thresholds and relaxation times follow a broad scaling
distribution, then the sequence of feature activations might produce
power laws … That would be an additional mechanism to derive and test —
not a consequence of singularity theory alone." The record's LEAD-200
(Done) checked the related question whether relaxation summed over an
ultrametric tree gives a power law.

## The gap, and where it is filled

The ledger notes that A gives no step from one algebraic mode to the
broad distribution of timescales an observed power law needs. One
quartic mode gives t^(−1/2), and CLAIM-tmpcbfdj shows it needs a balanced
start. CLAIM-tmpuc8ro, the assistant's, supplies one step. A population
of independent factored modes from a small random start relaxes on
average as a power law with a logarithmic correction. The cause is that
the conserved imbalance of each mode sets its exponential rate, and those
rates are distributed down to zero. That route needs no criticality and
no hierarchy of degeneracies, which narrows A's alternative. A
power law in training relaxation does not even indicate a hierarchy of
singular orders.

## Cross-reference

The rival it names, criticality and critical slowing in learning, is
another theme of the same exchange. The record's entries on critical
slowing belong to it.
