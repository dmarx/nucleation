---
number: 1376
status: Proposed
formerly:
- THEORY-tmp5ebls
promote_when: >-
  A reading of the 1973 article's introduction from a text that can be
  checked (a searchable copy or a verified transcription) confirms that it
  defines metric spaces as categories valued in ([0, ∞], ≥, +, 0), with the
  triangle inequality and zero self-distance as the composition and
  identity laws, argues that symmetry and finiteness are not required, and
  shows that enriched-category constructions (functors, the Yoneda
  embedding) specialize to metric-space notions.
title: 'Lawvere shows that a generalized metric space is exactly a category enriched in the extended non-negative reals under addition, with the triangle inequality as composition, so that dropping symmetry and finiteness is natural and enriched-category constructions specialise to metric-space theory'
version: 1
tags:
- mathematics
date: '2026-11-05'
source:
- LIT-2106
summary: >-
  Lawvere (1973; TAC Reprints 2002), [LIT-2106](../literature.d/LIT-2106.md), read in part in
  [NOTE-1585](../notes.d/NOTE-1585.md): the 2002 commentary in full, the 1973 introduction by eye
  from a scan with no text layer. Proposed: the article's own statements
  were read only from page images, and its general theory (original
  pp. 143–166) not read. It concerns one additive tensor; it does not say
  anything about other composition laws such as max, about algorithms, or
  about resources whose cost depends on the order of operations.
---
<!-- inactive-ok-file: NOTE-1585 — Skimmed and new; cited from the reading of Lawvere (1973) as open -->

# THEORY-1376: Lawvere shows that a generalized metric space is exactly a category enriched in the extended non-negative reals under addition, with the triangle inequality as composition, so that dropping symmetry and finiteness is natural and enriched-category constructions specialise to metric-space theory

## Source

Lawvere (1973; reprinted 2002), [LIT-2106](../literature.d/LIT-2106.md); read in [NOTE-1585](../notes.d/NOTE-1585.md).

## What was actually shown

- **The identification**, restated in the commentary: [0, ∞] with ≥, +
  and truncated subtraction is "a bona fide example of a complete,
  symmetric, monoidal closed category V" (p. 1), and metric spaces satisfy
  only the two axioms for a V-category (p. 2).
- **Against the usual definition**: "the evidence is compelling that the
  usually-given more restrictive definition was too hastily fixed"
  (p. 2), with non-symmetric metrics arising in dynamics and analysis.
- **The introduction** (original pp. 135–142, read by eye): the table of
  V-valued categories, a non-symmetric example in which distance is work
  done uphill, and normed categories, whose infimum of norms gives a
  metric.
- **Specialization** of V-functors, Yoneda and Cauchy completion: stated in
  the commentary and the summary; the pages that carry it out were not
  read.

## What this does not say

- That other composition laws (max, min) give enriched categories of the
  same kind: true for quantales, but not this paper's case; the max base
  for peak capacity is the reader's derivation ([NOTE-1585](../notes.d/NOTE-1585.md)).
- Anything about computing distances, or their complexity.
- Anything about costs that depend on the order of operations or on a
  running reserve.
