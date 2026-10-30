---
number: 499
status: Proposed
formerly:
- CLAIM-tmp79btt
title: 'The linear barrier left after aligning independently trained networks over the architecture''s symmetries rises with depth'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  The barrier after alignment, tracked against depth at fixed width, with
  seeds, for convnets or transformers, under one alignment method fixed in
  advance, does not rise with depth.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-30'
line:
- learned-structure
grounds:
- THEORY-112
bears_on:
- QUESTION-317
summary: >-
  The depth clause of [THEORY-112](../theory.d/THEORY-112.md)'s old title, kept as a Proposed claim by
  the [ADR-047](../decisions.d/ADR-047.md) sweep of 2026-10-30 (kind 2) when the eleventh status
  review's narrowing had dropped it. No source measures or states it for
  barriers after alignment: it is the record's composition of Entezari et
  al.'s unaligned depth curves with Ferbach et al.'s compounding width
  bound. Its defeater is the depth paragraph of the old promote_when.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-2 rule this entry is filed under -->

# CLAIM-499: The linear barrier left after aligning independently trained networks over the architecture's symmetries rises with depth

## The claim

At fixed width, deeper networks keep more of their straight-line barrier
after alignment. The record put this together from two sources that
[THEORY-112](../theory.d/THEORY-112.md) reads. Entezari et al. ([LIT-652](../literature.d/LIT-652.md)) find the unaligned barrier
rising quickly with depth for MLPs and shallow CNNs, and saturating high
for VGG and ResNet, and they blame depth rather than width. Their search
found zero-barrier permutations only for MNIST MLPs of depth 1, 2 and 4.
Ferbach et al. ([LIT-680](../literature.d/LIT-680.md)) bound the width layer ℓ needs for alignment to
work by a quantity exponential in the width of the layer before, so the
requirement compounds with depth, and their lower bound shows the rate is
tight for independent neurons.

## What it does not say

Neither source measures the barrier after alignment against depth. Entezari
et al.'s curves are before alignment, and Ferbach et al.'s width is
sufficient, not necessary, and falls if weights concentrate near a
low-dimensional subspace. Nor does it hold for curved paths: Draxler et
al. ([LIT-653](../literature.d/LIT-653.md)) find barriers on minimum-energy paths falling as networks get
deeper.

## Note of 2026-10-30: what holds it back

The measurement its defeated_if names has not been made: no reading in the
record tracks the barrier after alignment against depth at fixed width
under one alignment method (QUESTION-317). It composes Entezari et al.'s
depth curves, which are before alignment, with Ferbach et al.'s width
bound, which is sufficient and not necessary, and neither measures it.
