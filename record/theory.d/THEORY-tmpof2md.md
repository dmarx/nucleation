---
status: 'Proposed'
promote_when: 'A test on embedded real networks that compares the layers produced by geometric coarse-graining with those produced from a null ordering of the circle (random angles, or angles shuffled within degree classes), with the self-similarity of degree distribution, clustering and degree–degree correlations measured by a stated statistic over more than a handful of layers, and the geometric layers collapsing where the null layers do not. It is refuted if null orderings collapse as well, since then the blocks, not the hidden geometry, produce the collapse. Further collapses judged by eye cannot settle it.'
title: 'Real complex networks embedded in the hyperbolic plane are self-similar under geometric renormalization, their coarse-grained layers keeping the degree distribution, clustering and degree–degree correlations of the original, and this self-similarity is evidence that a hidden metric space underlies them'
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-20'
source:
- LIT-869
summary: >-
  The empirical claim [THEORY-190](THEORY-190.md) set aside when the promotion audit (batch 048) narrowed it to the model. García-Pérez, Boguñá and Serrano (2017), [LIT-869](../literature.d/LIT-869.md), find six embedded real networks self-similar under the renormalization and call this new evidence of hidden metric spaces. The collapse was judged by eye over two to five layers with no null ordering of the circle. Filed under [ADR-047](../decisions.d/ADR-047.md) v4.
extends:
- THEORY-190
---


# THEORY-tmpof2md: Real complex networks embedded in the hyperbolic plane are self-similar under geometric renormalization, their coarse-grained layers keeping the degree distribution, clustering and degree–degree correlations of the original, and this self-similarity is evidence that a hidden metric space underlies them

## Source

García-Pérez, Boguñá and Serrano (2017), [LIT-869](../literature.d/LIT-869.md): six real networks,
read in [NOTE-673](../notes.d/NOTE-673.md) (the Internet, airports, a metabolic network, a proteome,
a music network and a word network), embedded in ℍ², renormalized, and
their layers compared with the original (Fig. 7).

## What is asserted, and by whom

That real networks show the self-similarity the S¹ model has under
geometric coarse-graining, and that this is new evidence that hidden
metric spaces underlie them. The authors assert both.

## What the record holds toward it

- [THEORY-190](THEORY-190.md) (Active): what the model does under the transformation,
  asymptotically. It says nothing of real networks; its former
  promote_when said explicitly that a collapse in data cannot show the
  model is why.
- Against the inference: the layers nest because the procedure takes
  contiguous blocks on the circle, so some collapse may come from the
  blocking itself. No null ordering was run, and the collapse was judged
  by eye.

## What would confirm or reject it

The comparison against a null ordering that the promote_when describes.
If null layers collapse as well, the self-similarity is not evidence of
the geometry.
