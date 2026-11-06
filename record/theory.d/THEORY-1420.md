---
number: 1420
status: Proposed
formerly:
- THEORY-tmpqzxwh
promote_when: >-
  A reading confirms that the zero-dimensional sublevelset barcode of a
  landscape is determined by its disconnectivity graph, that its
  one-dimensional bars record transition paths the disconnectivity graph
  omits, and that the paper's barcode formula for the analytical alkane
  landscape is proved.
title: 'The sublevelset persistent homology of an energy landscape contains its disconnectivity graph as the zero-dimensional part and also records alternative transition paths and higher critical points, and for the alkane torsional landscape it has a closed form in every dimension'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-fifth status review (ADR-057), at the status review's
    ruling (the owner delegated these rulings): a re-derivation of the bar
    counts of Theorems 1 and 2 is added to the body, since appendix A,
    which holds the paper's proof, was skimmed in NOTE-1616. It meets the
    condition's third part once a second reader has checked it (ADR-065
    §5). No status change; the title and condition are unchanged.
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-2047
summary: >-
  Mirth, Zhai, Bush, Alvarado, Jordan, Heim, Krishnamoorthy, Pflaum, Clark,
  Zhang and Adams (2021), [LIT-2047](../literature.d/LIT-2047.md), read in [NOTE-1616](../notes.d/NOTE-1616.md), appendices
  with the full proofs skimmed. The first two parts are standard
  correspondences the paper states and illustrates; the closed form is its
  Theorems 1 and 2. It treats one scalar energy only: nothing here covers
  several resources at once, which would need multi-parameter persistence.
---

# THEORY-1420: The sublevelset persistent homology of an energy landscape contains its disconnectivity graph as the zero-dimensional part and also records alternative transition paths and higher critical points, and for the alkane torsional landscape it has a closed form in every dimension

## Source

Mirth, Zhai, Bush, Alvarado, Jordan, Heim, Krishnamoorthy, Pflaum, Clark,
Zhang and Adams (2021), [LIT-2047](../literature.d/LIT-2047.md); read in [NOTE-1616](../notes.d/NOTE-1616.md).

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

## Re-derivation of 2026-11-06: the bar counts of Theorems 1 and 2

1. Each one-dimensional torsion term is a Morse function on the circle with
   three minima and three maxima (trans and two gauche; [NOTE-1616](../notes.d/NOTE-1616.md), §V). The
   sum f_n on Tⁿ is then Morse. A critical point picks a critical point in
   each coordinate, and its index is the number of coordinates at a
   maximum, so index k has C(n, k)·3^k·3^(n−k) = 3ⁿ·C(n, k) critical points,
   as in Theorem 1.
2. The semi-infinite bars in dimension k are the Betti numbers of Tⁿ,
   C(n, k).
3. Each index-k critical point either begins a k-bar or ends a (k−1)-bar
   (the paper's §IV.A count, quoted in [NOTE-1616](../notes.d/NOTE-1616.md)). This holds with tied
   critical values, counted with multiplicity, by the long exact sequence of
   each handle attachment. Writing x_k for the finite k-bars,
   3ⁿ·C(n, k) = C(n, k) + x_k + x_{k−1}, with x_{−1} = 0.
4. The recursion fixes every x_k, and x_k = (3ⁿ − 1)·C(n − 1, k) solves it:
   by Pascal's rule, (3ⁿ − 1)[C(n−1, k) + C(n−1, k−1)] = (3ⁿ − 1)·C(n, k).
   The ends check: x_0 = 3ⁿ − 1, and x_n = 0, so every n-bar is
   semi-infinite.
5. Dimension k therefore has C(n, k) + (3ⁿ − 1)·C(n − 1, k) bars, C(n, k) of
   them semi-infinite: Theorem 2's count.

It does not cover "the rest of one length" above, which the title does not
assert; that stays transcribed from the proof.

## Note of 2026-11-06: what holds it back

Its condition asks that the closed form be proved, and appendix A, which holds the proof, was skimmed in [NOTE-1616](../notes.d/NOTE-1616.md). The promotion awaits a second reader's check of the re-derivation above ([ADR-065](../decisions.d/ADR-065.md) §5), or a reading of appendix A; nothing rests on this entry once the claims' edges have moved to corroborated_by.
