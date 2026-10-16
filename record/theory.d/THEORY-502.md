---
number: 502
status: Active
formerly:
- THEORY-tmpdk0fo
title: "Forman–Ricci curvature of a graph edge, taken with no cells above the edges, depends only on the weights of the edge, its two endpoints and the edges adjacent to it, and with unit weights reduces to 4 − deg(v₁) − deg(v₂); it is a local, closed-form degree-and-weight statistic that sees no triangles or cycles, unlike Ollivier's curvature, which needs a transport problem per edge"
version: 1
tags:
- network-science
- mathematics
date: '2026-10-16'
source:
- LIT-020
summary: >-
  Weber, Saucan & Jost (2016; J. Complex Networks 2017), [LIT-020](../literature.d/LIT-020.md), read in
  full in [NOTE-026](../notes.d/NOTE-026.md), which checked the formulas against page renders. The
  formula (Eq. 11) is Forman's (2003) Bochner–Weitzenböck curvature
  specialised to a 1-dimensional complex by dropping the parent terms; the
  unit-weight form is [NOTE-026](../notes.d/NOTE-026.md)'s substitution, not stated in the paper. The
  paper's applications (an EMD distance between curvature distributions, a
  Ricci flow for change detection, a Laplacian flow for denoising) are
  one-table or one-figure demonstrations, and several of its formulas
  carry sign and consistency slips, so it is cited here for the
  definition only.
---

# THEORY-502: Forman–Ricci curvature of a graph edge, taken with no cells above the edges, depends only on the weights of the edge, its two endpoints and the edges adjacent to it, and with unit weights reduces to 4 − deg(v₁) − deg(v₂); it is a local, closed-form degree-and-weight statistic that sees no triangles or cycles, unlike Ollivier's curvature, which needs a transport problem per edge

## Source

Melanie Weber, Emil Saucan and Jürgen Jost (2016), "Characterizing
Complex Networks with Forman-Ricci Curvature and Associated Geometric
Flows", arXiv:1607.08654v2, *Journal of Complex Networks* 5 (2017),
[LIT-020](../literature.d/LIT-020.md), read in full in [NOTE-026](../notes.d/NOTE-026.md). The Supplemental Material was not read.

## What was actually shown

**Where it comes from.** Forman's combinatorial Bochner–Weitzenböck
formula on a weighted cell complex splits the Laplacian as □_p = B_p + F_p,
with B_p non-negative and F_p diagonal; on 1-cells the diagonal entry is
the Ricci curvature (Eq. 5). A graph is treated as a 1-dimensional regular
CW complex: edges have nodes as children and no faces as parents, which
removes half the terms of Forman's general formula (§2.3, pp. 6–7).

**The formula (Eq. 11, checked against the render).** For an edge
e = (v₁, v₂) with weight ω(e) and node weights ω(v):
Ric_F(e) = ω(e) · ( ω(v₁)/ω(e) + ω(v₂)/ω(e) − Σ [ ω(v₁)/√(ω(e)ω(e_v₁)) +
ω(v₂)/√(ω(e)ω(e_v₂)) ] ), the sum over edges adjacent to e at v₁ and at
v₂. With all weights 1 this is 4 − deg(v₁) − deg(v₂).

**What follows.** Every term involves only the edge, its endpoints and the
edges that share an endpoint with it. No triangle, cycle or longer path
enters, because there are no 2-cells; the authors defer triangle and
clique terms to "a forthcoming article" (p. 7). Ollivier's curvature,
κ_xy = 1 − W(m_x, m_y)/d(x,y), needs an optimal-transport solve per edge.

**What could have come out otherwise.** This is a derivation, not an
experiment. It could have been wrong in the specialisation; the step is
short and standard, though the paper does not write it out and quotes
Forman's Eq. 9 rather than deriving it.

## What this does not say

- **That Forman and Ollivier curvature agree.** The paper says there are
  "strong theoretical indications" that they are "closely correlated" and
  defers the evidence to a forthcoming study (C8).
- **That the curvature is independent of degree.** On a 1-complex it is
  essentially a degree-and-weight statistic, which the authors concede
  only in part (p. 8: "Even if curvature cannot be assumed independent of
  node degrees…").
- **That it applies to arbitrary data weights without error.** The formula
  is derived for standard weights; the paper appeals to Forman's theorem
  that admissible weights are dense, and asserts the error is not
  perceptible (C2).
- **That the flows work.** The Forman–Ricci flow γ̃ − γ = −Ric_F·γ (Eq. 36)
  is shown on one Gnutella snapshot pair with no ground truth, and the
  Laplacian-flow denoising on a schematic karate-club figure. The §4.3
  workflow drops the weight factor and so runs the 3-D form the paper had
  rejected (Eq. 38). The authors say the applications are "only
  theoretically proposed and illustrated solely on a small example" (§5).
- **That real networks look like Barabási–Albert graphs in general.**
  Table 1 shows three real networks closer to one BA sample than to ER or
  WS samples, and closer to one another in one case (Facebook–BioGrid
  0.0086) than to BA.
- **That the default weights are consistent.** Eq. 21's signed edge
  weights contradict Eq. 20's range and Forman's positivity requirement.

## Connections

- **Ollivier–Ricci flow** ([THEORY-456](THEORY-456.md), from [LIT-004](../literature.d/LIT-004.md)). Ni et al. run a
  flow of the same shape, curvature times current length, with Ollivier
  curvature, and benchmark it. They report, without data, that Forman
  curvature did worse for community detection. Neither paper tests a
  Forman flow on communities.
- **Higher-order networks** ([THEORY-598](THEORY-598.md), from [LIT-091](../literature.d/LIT-091.md)). The
  simplicial complexes and Hodge Laplacians of Battiston et al.'s review
  are Forman's full setting; Eq. 11 is its 1-skeleton case, the reading
  [NOTE-057](../notes.d/NOTE-057.md) records. The augmented Forman curvatures with triangle terms,
  used in later graph-learning work, are not this formula.
