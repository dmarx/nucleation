---
status: Proposed
promote_when: >-
  An inspection of the restriction maps a sheaf-learning model fits on
  real heterophilic graphs, against a labelling held out from that
  inspection, showing that the learned transports take the class-aligned
  form the separation theory prescribes (sign flips or rotations across
  classes, identity within them) and that accuracy depends on that form,
  for instance by an ablation that keeps the learned maps' magnitudes and
  scrambles their alignment. Benchmark accuracy alone, however high, does
  not settle it.
title: 'A graph network that learns its sheaf restriction maps from node features succeeds on heterophilic graphs because it learns the class-aligned transports its separation theory prescribes: sign flips or rotations across classes, identity within them'
version: 1
tags:
- representation-learning
- network-science
date: '2026-10-30'
source:
- LIT-1811
extends:
- THEORY-1139
summary: >-
  The wider thesis of Bodnar et al. (2022), [LIT-1811](../literature.d/LIT-1811.md), kept here when the
  twenty-second status review promoted [THEORY-1139](THEORY-1139.md), the reading of what
  was measured ([ADR-065](../decisions.d/ADR-065.md); [ADR-047](../decisions.d/ADR-047.md) kind 1). The learned maps were inspected
  only in the synthetic bipartite case; whether the maps learned on real
  graphs have this geometry, and whether accuracy depends on it, is open.
---

# THEORY-tmpu5c8o: A graph network that learns its sheaf restriction maps from node features succeeds on heterophilic graphs because it learns the class-aligned transports its separation theory prescribes: sign flips or rotations across classes, identity within them

## Source

Bodnar et al. (2022), [LIT-1811](../literature.d/LIT-1811.md), §§3.2, 5–6 and Appendix F of arXiv
2202.04579v4; read in full in [NOTE-1332](../notes.d/NOTE-1332.md). What the experiments showed is
[THEORY-1139](THEORY-1139.md), which this entry extends.

## The thesis

The paper's separation results say that diffusion with the right sheaf
separates any labelling: sign flips across the two classes of a bipartite
graph, rotations by class for more (Propositions 10–13). It concludes that
"solving any node classification task can be reduced to performing
diffusion with the right sheaf" (p. 6), and offers its learned model as a
way to find that sheaf from features. Its accuracy on heterophilic
benchmarks is then credited to the geometry it learns.

## Why it is not held

The learned maps were compared with the theory only on a synthetic
bipartite graph, where the right sheaf is negative everywhere and the
model learned negative transports. No learned map is shown for any
benchmark dataset. The model is also a feature-conditioned message
function, and such models do well under heterophily for other reasons
(p. 10), so benchmark accuracy cannot tell the theory's mechanism from
theirs.
