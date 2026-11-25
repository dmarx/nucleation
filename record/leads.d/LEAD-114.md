---
number: 114
status: Open
formerly:
- LEAD-tmpjnlxv
title: 'Learn a non-abelian task with no matrix representation imposed, and recover its irreducibles from the weights without supplying the group, or show them unrecoverable'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-058
summary: >-
  Named in [QUESTION-058](../questions.d/QUESTION-058.md). Filed by the backlog audit of 2026-11-19.
---

<!-- inactive-ok-file: CLAIM-972, CLAIM-973, CASE-378 — Proposed; the findings and the study filed under this lead on 2026-11-22 -->

# LEAD-114: Learn a non-abelian task with no matrix representation imposed, and recover its irreducibles from the weights without supplying the group, or show them unrecoverable

## What it would do

Train a network on a small non-abelian group operation and search the
weights for irreducible representations by a method that is not given the
group.

Where the record names it:

- [QUESTION-058](../questions.d/QUESTION-058.md): "A non-abelian task learned without a matrix
  representation imposed, analysed without the group being supplied in
  advance."

## What would count

Irreducibles recovered blind answer [QUESTION-058](../questions.d/QUESTION-058.md); failure with the group
supplied as a control says the method, not the network, is the limit.

## Note of 2026-11-22: carried out
Done under this lead (branch `claude/lead-114-blind-irrep`,
`scratch/studies/lead-114/`): [CASE-378](../cases.d/CASE-378.md) trains small numpy networks on S3
and S4 composition with elements as one-hot indices (no matrix representation
imposed), recovers the irreducibles blind from the operation each network
itself computes, and compares against a group-supplied control. [CLAIM-972](../claims.d/CLAIM-972.md):
the irreducibles are recovered blind, exactly, when the network has learned the
group, and the control shows the gate is the network's competence not the
method's. [CLAIM-973](../claims.d/CLAIM-973.md): the learned embedding carries the irreducibles as a
group-Fourier spectrum concentrated on the faithful ones. Recovery is up to
isomorphism (characters, dimensions, isotypic projectors), not canonical
per-element matrices. What remains: larger non-abelian groups, the mechanism by
which a generalising network comes to compute a valid group, and whether
explicit `ρ(g)` matrices can be pinned beyond a per-block basis. Status and
stage left for the owner.
