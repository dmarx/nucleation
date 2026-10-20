---
number: 234
status: Open
formerly:
- QUESTION-tmpszev1
title: 'Do interchange interventions leave the mediating direction underdetermined in trained networks: do two basis-related alignments in a trained model tie on every interchange drawn from the data, and for which networks are alignments that agree on all such interventions unique up to a stated symmetry?'
version: 1
tags:
- causality
- philosophy-of-science
- representation-learning
date: '2026-10-20'
line: learned-structure
summary: >-
  Filed when the promotion audit (batch 062, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-243](../theory.d/THEORY-243.md) to what the constructed three-unit network proves:
  two basis-related alignments tie on every interchange intervention on
  the input. Whether such ties occur in trained networks, or are ruled
  out for some class up to a symmetry, was the old promote_when, and it
  moves here.
answered_by:
- THEORY-802
---

# QUESTION-234: Do interchange interventions leave the mediating direction underdetermined in trained networks: do two basis-related alignments in a trained model tie on every interchange drawn from the data, and for which networks are alignments that agree on all such interventions unique up to a stated symmetry?

## Why it is a question

[THEORY-243](../theory.d/THEORY-243.md) now states an existence result. In the identity network
x ↦ x(1, 0, 1) ↦ (0, 2, 1)·h, aligning the input with the third unit and
aligning it with (h₁ + h₂)/√2 pass every interchange intervention on the
input equally (Makelov et al., [LIT-968](../literature.d/LIT-968.md); Wu et al., [LIT-961](../literature.d/LIT-961.md)). So
interventions on that variable alone do not fix which direction mediates
it. The general reading, that the mediating direction is fixed only
relative to a chosen decomposition into units, needs more than one
constructed case.

An answer is one of the following:

- **A trained-network tie.** In a trained network, two alignments of
  the same high-level variable that differ by a change of basis crossing
  component boundaries and agree on every interchange intervention drawn
  from the data distribution. Then a showing of what, if anything,
  separates them.
- **A uniqueness bound.** A proof that, for a stated class of networks
  and high-level models, alignments that agree on all such interventions
  for every aligned variable are unique up to a stated symmetry.

Further cases where one alignment scores higher than another cannot
settle it, since the question is about ties under a fixed set of
interventions.
