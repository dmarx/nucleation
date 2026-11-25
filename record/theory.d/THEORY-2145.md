---
number: 2145
status: Proposed
formerly:
- THEORY-tmpuxsx9
promote_when: >-
  An independent study of frozen decoder transformers, on a family other
  than Llama2, reproducing that skipping or reordering middle layers
  degrades benchmarks gracefully where skipping early layers does not,
  that replacing middle layers with copies of one layer is catastrophic,
  and that math or reasoning benchmarks decline more steeply under
  reordering or parallel execution than commonsense ones.
title: 'Middle layers share a space but do distinct work'
statement: >-
  Sun, Pickett, Nain and Jones report that in frozen pretrained transformers
  the hidden states fall into a few beginning layers, a large middle and one
  or two ending layers, and that the middle layers share a representation
  space but do different work: skipping, reordering or running them in
  parallel degrades benchmarks gracefully, replacing them with copies of one
  layer is catastrophic, and math and reasoning tasks depend most on layer
  order
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2946
summary: >-
  Evidence for a broad, robust middle in transformer depth, with the
  correction that it is uniform without being redundant ([CLAIM-771](../claims.d/CLAIM-771.md)).
  Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-771 THEORY-2140 THEORY-2144 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2145: Middle layers share a space but do distinct work

## Source

Sun, Pickett, Nain and Jones, [LIT-2946](../literature.d/LIT-2946.md), read in [NOTE-2223](../notes.d/NOTE-2223.md) from arXiv 2407.09298v4 (12 Feb 2025; the AAAI 2025 paper with appendix).

## What was actually shown

§§3.1–3.8, §5 and A.5 as quoted in the NOTE.

## What this does not say

Not that middle layers are redundant or interchangeable in function; not tested on final layers separately.

## Connections

[THEORY-2144](THEORY-2144.md) (Lad and colleagues, its closest neighbour); [THEORY-2140](THEORY-2140.md) (tuned lens); [LIT-657](../literature.d/LIT-657.md).
