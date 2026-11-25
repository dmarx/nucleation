---
number: 2085
status: Proposed
formerly:
- THEORY-tmp1xpyh
title: 'Identity learning may proceed in phases'
statement: >-
  The owner hypothesizes that a text-to-image model learns a named identity
  in phases, from domination by biases carried by parts of the name, through
  stabilized coarse attributes, to a unique identity it can apply flexibly,
  and then to overfitting, and that giving an identity its own concept
  direction is a detectable change in the weights
version: 1
source:
- LIT-2875
tags:
- representation-learning
- learning-theory
- individuation
date: '2026-11-19'
promote_when: >-
  A training run in which a text-to-image model learns new named
  identities, measured across checkpoints, shows the dispersion of samples
  for a name falling through distinct stages in the stated order, and a
  probe or intervention finds a name-specific direction appearing at the
  stage where the identity becomes flexible.
summary: >-
  From the owner's unfinished proposal [LIT-2875](../literature.d/LIT-2875.md), read in
  [NOTE-2172](../notes.d/NOTE-2172.md). A hypothesis, not a finding; the design to test it is
  [CASE-298](../cases.d/CASE-298.md). Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CASE-298 — newly filed in this contribution -->

# THEORY-2085: Identity learning may proceed in phases

## The account

Phases of identity learning: (1) identity overridden by name-part biases;
(2) coarse components stabilize; (3) a unique identity, applied flexibly;
(4) overfit. A sub-hypothesis that the move to (3) is a change in the
weights, an identity given its own concept direction rather than composed
from others, with the open possibility that all identities stay
compositional.

## Evidence

None yet; the companion project measures identity strength at one fixed model, not over training.
