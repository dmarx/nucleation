---
status: Proposed
promote_when: >-
  An independent study of frozen decoder transformers, on a family other
  than Llama2, reproducing that skipping or reordering middle layers
  degrades benchmarks gracefully where skipping early layers does not,
  that replacing middle layers with copies of one layer is catastrophic,
  and that math or reasoning benchmarks decline more steeply under
  reordering or parallel execution than commonsense ones.
title: 'Sun, Pickett, Nain and Jones report that in frozen pretrained transformers the hidden states fall into a few beginning layers, a large middle and one or two ending layers, and that the middle layers share a representation space but do different work: skipping, reordering or running them in parallel degrades benchmarks gracefully, replacing them with copies of one layer is catastrophic, and math and reasoning tasks depend most on layer order'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmpi3ty1
summary: >-
  Evidence for a broad, robust middle in transformer depth, with the
  correction that it is uniform without being redundant (CLAIM-tmpcvuyr).
  Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-tmpcvuyr LIT-tmpi3ty1 NOTE-tmpekh8j THEORY-tmpky55f THEORY-tmpthk75 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmpuxsx9: Sun, Pickett, Nain and Jones report that in frozen pretrained transformers the hidden states fall into a few beginning layers, a large middle and one or two ending layers, and that the middle layers share a representation space but do different work: skipping, reordering or running them in parallel degrades benchmarks gracefully, replacing them with copies of one layer is catastrophic, and math and reasoning tasks depend most on layer order

## Source

Sun, Pickett, Nain and Jones, LIT-tmpi3ty1, read in NOTE-tmpekh8j from arXiv 2407.09298v4 (12 Feb 2025; the AAAI 2025 paper with appendix).

## What was actually shown

§§3.1–3.8, §5 and A.5 as quoted in the NOTE.

## What this does not say

Not that middle layers are redundant or interchangeable in function; not tested on final layers separately.

## Connections

THEORY-tmpthk75 (Lad and colleagues, its closest neighbour); THEORY-tmpky55f (tuned lens); LIT-657.
