---
number: 1368
status: Proposed
formerly:
- THEORY-tmp278tq
promote_when: >-
  An independent analysis or simulation of quad kirigami linkages confirms
  that the minimum rigidifying link count δ(L) = ⌈(3L²−3)/2⌉ exceeds the
  minimum connecting count γ(L) = L² − 1 for every L ≥ 2, and finds for
  randomly placed links that the density of maximum internal degrees of
  freedom, connectivity percolation and rigidity percolation are distinct
  and ordered ρ_i < ρ_c < ρ_r.
title: 'Chen, Choi and Mahadevan show that in a quad kirigami sheet read as a linkage the fewest links that rigidify the sheet always outnumber the fewest that connect it, and that under random links the maximum of internal mechanisms, connectivity percolation and rigidity percolation fall at distinct link densities in that order'
version: 1
tags:
- mathematics
- natural-sciences
- network-science
date: '2026-11-05'
source:
- LIT-2064
summary: >-
  Chen, Choi & Mahadevan (2020), [LIT-2064](../literature.d/LIT-2064.md), read from arXiv v2 in
  [NOTE-1574](../notes.d/NOTE-1574.md) (main text; the SI with the proofs was not read).
  Proposed: the minimal counts are proved by construction in the SI,
  which was not read; the thresholds are numerical, and the rigidity
  threshold is a peak of a second derivative with a heuristic explanation.
  Planar quad kirigami and infinitesimal rigidity only; no experiments.
corroborates:
- CLAIM-562
---

# THEORY-1368: Chen, Choi and Mahadevan show that in a quad kirigami sheet read as a linkage the fewest links that rigidify the sheet always outnumber the fewest that connect it, and that under random links the maximum of internal mechanisms, connectivity percolation and rigidity percolation fall at distinct link densities in that order

## Source

Chen, Choi & Mahadevan, "Deterministic and stochastic control of kirigami
topology", PNAS (2020), [LIT-2064](../literature.d/LIT-2064.md); read from arXiv 1910.07090v2 in
[NOTE-1574](../notes.d/NOTE-1574.md).

## What was actually shown

- **Minima.** δ(L) = ⌈(3L²−3)/2⌉ and "γ(L) = L2 − 1" (Theorems 1 and 2,
  L2 being L²), by hierarchical construction: "there is no MRP which is
  also an MCP for L ≥ 2."
- **Placement.** For large L it is "almost impossible to" "obtain an MRP
  (or MCP) by randomly picking" the minimum number of links.
- **Thresholds.** In simulations to L = 100, "ρi < ρc < ρr", with
  ρ_i ≈ 0.26, ρ_c ≈ 0.293 (1 − 1/√2 analytically) and ρ_r ≈ 0.429; "the
  number of internal DoF must be non-monotonic as links are added".

## What this does not say

- Anything about finite motions; rigidity here is infinitesimal.
- That ρ_r is a thermodynamic rigidity-percolation threshold. It is a peak
  in a numerical curve, compared only qualitatively with generic 2D
  rigidity percolation.
- Anything about sheets other than planar quad (and, in the SI, kagome)
  kirigami, or about physical sheets.

## Note of 2026-11-06: what holds it back

The title says the authors show the minimum rigidifying and connecting counts, whose proofs are in the SI Appendix that [NOTE-1574](../notes.d/NOTE-1574.md) did not read; a reading of those proofs, or a re-derivation of δ(L) and γ(L) checked by a second reader, would meet it. Its promote_when's demand for an independent analysis or simulation asks more than a reported title asserts ([ADR-065](../decisions.d/ADR-065.md)). Nothing rests on it now that [CLAIM-562](../claims.d/CLAIM-562.md) cites it as corroboration.
