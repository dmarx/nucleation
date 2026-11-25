---
number: 2132
status: Proposed
formerly:
- THEORY-tmp3dee0
promote_when: >-
  A probing study on another pretrained transformer finding the same
  aggregate order of layer positions for part of speech, constituents and
  coreference, with syntactic tasks more concentrated across layers than
  semantic ones.
title: 'BERT puts syntax lower, semantics higher'
statement: >-
  Tenney, Das and Pavlick find in frozen BERT, by probes pooling layers with
  learned weights, syntactic information best extracted lower and more
  locally and semantic information higher and spread across many layers, an
  ordering that holds in aggregate, overlaps in the middle, and is revised
  for individual examples from higher-level information
version: 1
tags:
- linguistics
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2936
summary: >-
  The main evidence for an ordering of abstraction by depth, read as
  overlapping regions rather than dependent levels ([CLAIM-771](../claims.d/CLAIM-771.md)).
  Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-1030 THEORY-104 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-771 THEORY-2144 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2132: BERT puts syntax lower, semantics higher

## Source

Tenney, Das and Pavlick, [LIT-2936](../literature.d/LIT-2936.md), read in [NOTE-2222](../notes.d/NOTE-2222.md) from arXiv 1905.05950v2 (9 Aug 2019).

## What was actually shown

§4, §4.1, Figures 1, 2, A.2 and the Limitations as quoted in the NOTE.

## What this does not say

Not that later layers depend on earlier ones, nor how the information is used; not beyond BERT.

## Connections

[THEORY-1030](THEORY-1030.md), [THEORY-1033](THEORY-1033.md) (Geva and colleagues); [THEORY-104](THEORY-104.md); [THEORY-2144](THEORY-2144.md) (Lad and colleagues' stages).
