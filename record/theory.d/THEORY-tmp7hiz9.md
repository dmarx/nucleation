---
status: Active
title: 'The Gromov–Wasserstein distance, half the least Lp distortion of a coupling, is a pseudometric on all networks with a probability measure on the nodes and any bounded edge weights, symmetric or not, and it is zero exactly when the two networks are weakly isomorphic, images of one network under maps that preserve weights and measures; so it compares only what the weight function and node measure record'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-29'
source:
- LIT-tmpu05fk
summary: >-
  Chowdhury and Mémoli (2019), [LIT-tmpu05fk](../literature.d/LIT-tmpu05fk.md), read in [NOTE-tmp72o0n](../notes.d/NOTE-tmp72o0n.md) from
  arXiv 1808.04337v2. Theorems 16 and 18, with full proofs in the main
  text (pp. 8–9). Active: proved. The sharp edge is the zero set. A
  distance of zero says the recorded weights and measures agree up to
  merging and splitting nodes with identical profiles; it says nothing
  about relations the record leaves out, and the measure is chosen by the
  user.
---

# THEORY-tmp7hiz9: The Gromov–Wasserstein distance, half the least Lp distortion of a coupling, is a pseudometric on all networks with a probability measure on the nodes and any bounded edge weights, symmetric or not, and it is zero exactly when the two networks are weakly isomorphic, images of one network under maps that preserve weights and measures; so it compares only what the weight function and node measure record

## Source

Chowdhury and Mémoli (2019), [LIT-tmpu05fk](../literature.d/LIT-tmpu05fk.md), §2, pp. 4–10 of arXiv
1808.04337v2; read in [NOTE-tmp72o0n](../notes.d/NOTE-tmp72o0n.md).

## What was actually shown

**The setting.** A measure network is (X, ωX, µX): X Polish, µX a fully
supported Borel probability measure, ωX bounded and measurable on X × X
(Definition 1, p. 4). For finite X it is a complete directed graph with
real, possibly asymmetric weights and node weights. dN,p(X, Y) is half the
minimum over couplings µ of ‖ωX(x, x′) − ωY(y, y′)‖ in Lp(µ ⊗ µ), for
p ∈ [1, ∞] (p. 8). The minimum is attained (Theorem 12, p. 8).

**Pseudometric (Theorem 16, pp. 8–9).** Non-negativity and dN,p(X, X) = 0
by the diagonal coupling; symmetry by swapping coordinates; the triangle
inequality by gluing optimal couplings of X–Y and Y–Z into a coupling of
X–Z and applying Minkowski. Nothing uses symmetry, the triangle inequality
or any other property of ωX: "the metric structure on N is not inherited
from its elements, but is rather enforced by the structure of dN,p" (p. 9).

**The zero set (Theorem 18, p. 9).** dN,p(X, Y) = 0 iff there is a
probability space (Z, µZ) and maps f, g with f∗µZ = µX, g∗µZ = µY and
f*ωX = g*ωY almost everywhere (Definition 3, p. 5). One direction pushes
µZ forward to a coupling of zero distortion; the other takes an optimal
coupling of zero distortion as Z. Two distinct networks can therefore be
at distance zero: splitting a node into copies with the same in- and
out-weights, and dividing its measure among them, changes nothing (p. 5;
Fig. 2). It is not a metric modulo strong isomorphism (Remark 15, p. 8).

**What could have failed.** The triangle inequality could have needed a
metric ground weight, as the Wasserstein distance needs a ground metric
(Remark 17); it does not. The zero set could have been strong isomorphism,
or something weaker than weak isomorphism; Theorem 18 fixes it exactly.

## What this does not say

- **That networks at distance zero describe the same system.** They agree
  on the recorded weights and node measure. Whatever was not measured into
  ωX, and whatever the imputation of missing entries supplied (Remark 1,
  p. 4), is invisible to the distance.
- **That the node measure is given by the data.** "The user adjusts the
  measure to signify important network substructures and to smooth out the
  effect of outliers" (p. 2). Change it and the distance changes.
- **That it can be computed.** The minimization is a non-convex quadratic
  program (p. 2). The paper computes only lower bounds ([THEORY-tmptcy1h](THEORY-tmptcy1h.md)).
- **Which coupling achieves it.** An optimal coupling exists; it need not
  be unique, and a symmetry of either network gives another of equal cost
  ([THEORY-tmpa43ta](THEORY-tmpa43ta.md)).
- **That it is new for symmetric data.** For symmetric L² weights it is
  Sturm's gauged measure spaces (p. 3); the extension is to asymmetric,
  bounded weights.
