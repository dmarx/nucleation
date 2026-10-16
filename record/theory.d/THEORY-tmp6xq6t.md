---
status: Active
title: "Iterating Ollivier–Ricci flow on edge weights lengthens edges between communities relative to edges within them, so a weight threshold can separate the communities; but the separation is proved only on symmetric clique graphs under the uniform neighbour measure, and there only by a constant factor for gateway edges, and on a two-block stochastic block model the method fails at an inter/intra ratio near 0.55, where other methods still recover the blocks and well short of the detectability threshold near 0.78"
version: 1
tags:
- network-science
- mathematics
date: '2026-10-16'
source:
- LIT-004
summary: >-
  Ni, Lin, Luo & Gao (2019), [LIT-004](../literature.d/LIT-004.md), read in full with its SI in [NOTE-006](../notes.d/NOTE-006.md),
  which checked Lemma E.1 by linear programming and iterated the proof's
  matrix. The flow w ← (1 − κ)d replaces each weight by the transport cost
  between the endpoints' neighbourhoods; bridge edges, with few shared
  neighbours, are negatively curved and grow. Theorem 4.1 (α = p = 0,
  cliques G(a,b), a > b ≥ 2) shows only non-gateway intra-clique edges
  shrinking; gateway edges grow at the inter-community rate with a ratio
  k ∈ (0,1) from Maple. Experiments use α = ½, p = 2, which no theorem
  covers. The Kesten–Stigum figure is [NOTE-006](../notes.d/NOTE-006.md)'s calculation.
---

# THEORY-tmp6xq6t: Iterating Ollivier–Ricci flow on edge weights lengthens edges between communities relative to edges within them, so a weight threshold can separate the communities; but the separation is proved only on symmetric clique graphs under the uniform neighbour measure, and there only by a constant factor for gateway edges, and on a two-block stochastic block model the method fails at an inter/intra ratio near 0.55, where other methods still recover the blocks and well short of the detectability threshold near 0.78

## Source

Chien-Chun Ni, Yu-Yao Lin, Feng Luo and Jie Gao (2019), "Community
Detection on Networks with Ricci Flow", arXiv 1907.03993v1, [LIT-004](../literature.d/LIT-004.md), read
in full with the Supplementary Information in [NOTE-006](../notes.d/NOTE-006.md).

## What was actually shown

**The mechanism (§3).** Ollivier curvature is κ_xy = 1 − W(m_x, m_y)/d(x,y),
with W the 1-Wasserstein distance between the endpoints' neighbour
measures. An edge between communities has few shared neighbours, so
transport must use the edge itself and κ < 0; an edge inside a community
has shortcuts and κ ≥ 0. The flow w^(k+1) = (1 − κ^(k)) d^(k), which is
exactly W, lengthens the first kind and contracts the second. Surgery then
removes edges above a threshold and reads communities off as connected
components.

**The theorem (Theorem 4.1, SI §E).** On G(a,b), b+1 cliques of a+1 nodes
joined through one gateway node each, with α = p = 0 (the Lin–Lu–Yau
uniform measure), non-gateway intra-clique distances shrink as (1/a)ⁿ.
Gateway-to-member distances grow at the same rate λ₁ⁿ as inter-community
edges, with ratio k ∈ (0,1); [NOTE-006](../notes.d/NOTE-006.md)'s iteration of the proof's matrix
gives k = 0.455 for (3,2), 0.433 for (5,3), 0.172 for (10,2) and 0.625 for
(10,9). Thresholding still separates the cliques, by a constant factor.
The proof's claim that the gateway edges grow as o(λ₁ⁿ) is an error, and
k ∈ (0,1) rests on a Maple calculation.

**Benchmarks (Fig. 5).**
- Two-block SBM, n = 500, p_intra = 0.15, 10 graphs per point: ARI ≈ 1 up
  to p_inter/p_intra = 0.5, ≈ 0.12 at 0.55, ≈ 0 by 0.6. Spinglass (≈ 0.9)
  and Fast Greedy (≈ 0.8) still succeed at 0.55 and stay above it to about
  0.65. The two-block Kesten–Stigum threshold with c_in = 75 is near 0.78
  ([NOTE-006](../notes.d/NOTE-006.md)'s calculation).
- LFR, n = 500, average degree 20: ARI ≈ 1 up to μ = 0.6, ≈ 0.8 at 0.65,
  ≈ 0.2 at 0.7, where Spinglass is higher.
- Six small real networks: best on 2, tied on 3, behind on Polblogs.

**What could have come out otherwise.** The flow could have kept pace with
the best baselines up to the detectability limit. On the one benchmark
with a known limit it stops at about 0.55, and the paper's reading of the
collapse as "the non-existence of community structure" is contradicted by
its own figure.

## What this does not say

- **That the flow detects communities whenever they exist.** That is the
  abstract's and §1.1's claim, and it holds where most baselines also
  succeed.
- **That the experimental setting is covered by the theorem.** Experiments
  use α = ½, p = 2; the authors say they could not prove the result for
  p > 0.
- **That the method is label-free.** Iterations, surgery schedule and final
  cutoff are hand-set per network, and how the Fig. 5 cutoffs were chosen
  is not stated. The "first modularity plateau" rule was proposed from one
  labelled graph.
- **That Forman curvature does worse.** The paper says so with no data.
- **Anything about the analogy with Ricci flow on 3-manifolds** beyond a
  heuristic the authors call "our heuristic thinking".

## Connections

- **Forman–Ricci curvature** ([THEORY-tmpdk0fo](THEORY-tmpdk0fo.md), from [LIT-020](../literature.d/LIT-020.md)). Weber,
  Saucan and Jost propose a flow of the same form with Forman's local
  curvature and never benchmark it. Whether a Forman flow recovers
  communities as this one does is open.
- **Spectral gap and density of states** ([THEORY-tmplo7ui](THEORY-tmplo7ui.md), from [LIT-028](../literature.d/LIT-028.md))
  and **higher-order interactions** ([THEORY-tmpodgn4](THEORY-tmpodgn4.md), from [LIT-091](../literature.d/LIT-091.md)) are the
  record's other network-geometry accounts. This one is pairwise
  throughout.
