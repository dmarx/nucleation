---
status: Open
title: 'In trained networks, how far do CKA and normalized Bures similarity disagree in ranking pairs of representations, and does the rank-dependent envelope between them matter in practice?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The empirical clause of [THEORY-233](../theory.d/THEORY-233.md)'s former promote_when. On 2026-10-19
  [THEORY-233](../theory.d/THEORY-233.md) was promoted: its envelope between CKA and NBS was checked by
  a direct derivation. Harvey, Larsen & Williams ([LIT-250](../literature.d/LIT-250.md)) illustrate the
  gap only on random Wishart matrices. Whether it matters for real
  representations needs a measurement on trained networks, and the record
  holds none.
---

# QUESTION-tmpg9cvp: In trained networks, how far do CKA and normalized Bures similarity disagree in ranking pairs of representations, and does the rank-dependent envelope between them matter in practice?

## Why it is a question

[THEORY-233](../theory.d/THEORY-233.md) holds the envelope CKA/√(r(K_X)r(K_Y)) ≤ NBS² ≤
min[r(K_X), r(K_Y)]·CKA ([LIT-250](../literature.d/LIT-250.md), eq. 24). The rank factors leave room for
the two measures to order pairs of representations differently. Until
2026-10-19 the THEORY's promote_when also asked for "a measurement on
trained networks of how far CKA and NBS disagree in practice". At the
owner's direction, from the promotion audit's batch 007
(record/promotion-audit/decisions/[THEORY-233](../theory.d/THEORY-233.md).yaml, [ADR-047](../decisions.d/ADR-047.md)), the
inequality was promoted and that clause moved here unchanged.

It is open because the paper shows the discrepancy only on random Wishart
matrices, with factors of two to three (Fig. 2), and the record holds no
comparison on trained networks.

## What would answer it

A measurement of CKA and NBS on pairs of representations from trained
networks, reporting how often and by how much the two order the pairs
differently. Agreement on particular model pairs cannot settle it, because
the envelope permits agreement. The answer needs the rate of disagreement
across a stated family of pairs, at the ranks those representations have.
