---
number: 147
status: Open
formerly:
- QUESTION-tmpmiu6o
title: 'In a second system of near-identical units on a known graph, are the synchronized clusters the symmetry orbits computed in advance, and does each cluster desynchronize in isolation where its own transverse block predicts?'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    `refines` QUESTION-063 added. The summary: whether the stability
    predictions hold in a second system is what "the record's use of
    this result as a coupling signature (QUESTION-063) needs".
    QUESTION-063's first line, distributed-agency, is already this
    question's (ADR-085). Reported by the synthesis review of
    2026-11-11 (seventh round). No other change.
tags:
- network-science
- complex-systems
date: '2026-10-19'
line: distributed-agency
refines:
- QUESTION-063
summary: >-
  The empirical condition formerly in [THEORY-276](../theory.d/THEORY-276.md)'s promote_when. On
  2026-10-19 [THEORY-276](../theory.d/THEORY-276.md) was promoted: that symmetry orbits are
  flow-invariant synchronization clusters, and that a cluster whose own
  factor moves nothing else can desynchronize while the others stay
  synchronized, was checked by a fixed-point-subspace derivation. Whether
  the stability predictions hold up in a second physical or biological
  system, as the record's use of this result as a coupling signature
  ([QUESTION-063](QUESTION-063.md)) needs, rests on one 11-node experiment.
---

# QUESTION-147: In a second system of near-identical units on a known graph, are the synchronized clusters the symmetry orbits computed in advance, and does each cluster desynchronize in isolation where its own transverse block predicts?

## Why it is a question

[THEORY-276](../theory.d/THEORY-276.md) states what the graph allows: orbit-wise synchrony is
invariant, and so is the state in which one cluster, moved only by its own
factor of the symmetry group, is unsynchronized while the rest are not.
Which of these states are stable, and so which clusters are seen, is set
by the node dynamics through the transverse IRR blocks. Pecora et al.
([LIT-960](../literature.d/LIT-960.md)) tested the predictions in one electro-optic network of 11 nodes,
with one bifurcation parameter. Until 2026-10-19 [THEORY-276](../theory.d/THEORY-276.md)'s
promote_when asked for a second test. At the owner's direction, from the
promotion audit's batch 013
(the audit's decision file for [THEORY-276](../theory.d/THEORY-276.md), [ADR-047](../decisions.d/ADR-047.md)), the
invariance was promoted and the condition moved here unchanged.

## What would answer it

An independent experiment or analysis, in a second physical or biological
system of near-identical units on a known graph, in which the
synchronized clusters observed are the symmetry orbits computed in
advance, and a cluster desynchronizes in isolation where its own
transverse block, and only it, is predicted to lose stability. A stable
synchronized pattern that splits an orbit, or an isolated
desynchronization that the IRR blocks do not predict, would count against
the predictions. Networks with nonidentical units, weighted or directed
coupling, or clusters from input-equitable partitions without symmetry
are outside the claim and cannot settle it.

## Note of 2026-11-07: the lattice of balanced partitions, from "Individuation, Possibility, and Disposition"

In the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07; https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e), A20 §2 notes that balanced synchrony partitions form a lattice (Stewart 2007; unread, identifier not given) and that "The lattice of structurally admissible synchrony patterns would generally be different from the collection of attractors and basins actually realized." That is this question's comparison of computed orbits with observed clusters, generalized from symmetry to balance ([THEORY-1065](../theory.d/THEORY-1065.md)). The suggestion is A's; the question stays open.
