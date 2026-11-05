---
status: Proposed
promote_when: >-
  A reading confirms that the zero-dimensional sublevelset barcode of a
  landscape is determined by its disconnectivity graph, that its
  one-dimensional bars record transition paths the disconnectivity graph
  omits, and that the paper's barcode formula for the analytical alkane
  landscape is proved.
title: 'The sublevelset persistent homology of an energy landscape contains its disconnectivity graph as the zero-dimensional part and also records alternative transition paths and higher critical points, and for the alkane torsional landscape it has a closed form in every dimension'
version: 1
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-tmpbs8e0
summary: >-
  Mirth, Zhai, Bush, Alvarado, Jordan, Heim, Krishnamoorthy, Pflaum, Clark,
  Zhang and Adams (2021), [LIT-tmpbs8e0](../literature.d/LIT-tmpbs8e0.md), read in [NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md), appendices
  with the full proofs skimmed. The first two parts are standard
  correspondences the paper states and illustrates; the closed form is its
  Theorems 1 and 2. It treats one scalar energy only: nothing here covers
  several resources at once, which would need multi-parameter persistence.
---

# THEORY-tmpqzxwh: The sublevelset persistent homology of an energy landscape contains its disconnectivity graph as the zero-dimensional part and also records alternative transition paths and higher critical points, and for the alkane torsional landscape it has a closed form in every dimension

## Source

Mirth, Zhai, Bush, Alvarado, Jordan, Heim, Krishnamoorthy, Pflaum, Clark,
Zhang and Adams (2021), [LIT-tmpbs8e0](../literature.d/LIT-tmpbs8e0.md); read in [NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md).

## What was actually shown

- **Dimension zero** (§II.B): the disconnectivity graph completely
  determines the zero-dimensional barcode; a bar dies where two components
  first join, at the lowest barrier between them.
- **Higher dimensions** (introduction, §II.B, §IV.A): loops born at index-1
  saddles that do not merge components record further transition paths;
  for a Morse function the bars count critical points of each index.
- **Closed form** (§V): f_n on the n-torus is Morse with 3^n·C(n, k)
  critical points of index k, and its barcode has
  C(n, k) + (3^n − 1)·C(n − 1, k) bars in dimension k, C(n, k)
  semi-infinite and the rest of one length; proof by induction on k,
  sketched in the main text and given in appendix A.

## What this does not say

- That the closed form extends beyond landscapes that are sums of
  identical one-dimensional terms.
- Anything about thresholds on several quantities at once: the paper
  mentions multi-parameter persistence only in a citation.
- That the barcode determines the landscape: the Morse–Smale complex holds
  strictly more.
- That MD-sampled landscapes are Morse functions; the correspondence holds
  for them only approximately.
