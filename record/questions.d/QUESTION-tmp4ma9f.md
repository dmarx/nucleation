---
status: Open
title: 'What rate ratio between the levels of a hierarchy, set against the spread of rates within a level and the size of the state space, is enough for a level to show in a chain''s time geometry and keep its place in the tree: the proven sufficient factor, the square of the larger of the edge count and one less than the state count, is far above the ratios at which simulated hierarchies show'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    A dated note: Bovier and colleagues' ultrametric slack is ln 3,
    independent of n and E. No change of status or title.
tags:
- mathematics
- complex-systems
date: '2026-11-20'
line:
- formal-apparatus
- distributed-agency
summary: >-
  [CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md) proves that a level shows in the log commute-time
  geometry once the rate ratio across it exceeds max(E, n − 1)², which is
  1,024 for 16 states on a torus. In a designed binary hierarchy on 16
  states, levels kept their designed place at ratios near 10, once the
  ratio between levels beat the spread within them (roughly 1/g > e^(2h)).
  The sharp threshold, and how it depends on the spread and on the
  branching, are open. Filed at the owner's turn of 2026-11-20 preferring
  "rate differences" to "scale separation".
---
<!-- inactive-ok-file: THEORY-tmph10k5 CLAIM-tmpxi826 — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpxi826 CLAIM-tmpy75jv CLAIM-478 — Proposed; filed in, or restated by, the contribution of 2026-11-20 on hierarchy and hyperbolicity -->

# QUESTION-tmp4ma9f: What rate ratio between the levels of a hierarchy, set against the spread of rates within a level and the size of the state space, is enough for a level to show in a chain's time geometry and keep its place in the tree: the proven sufficient factor, the square of the larger of the edge count and one less than the state count, is far above the ratios at which simulated hierarchies show

## What makes it open

The bound in [CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md) is worst case on both sides: a minimax path of
n − 1 edges for the upper bound, a cut of all E edges for the lower. In a
hierarchy the cut between two blocks has many edges in parallel, and their
heterogeneity averages; the path within a block is short. So the slack that
must be beaten is likely set by the spread of rates within a level and the
branching, not by n and E. The simulation (curation entry of 2026-11-20,
232905, hyp6.py) suggests 1/g > e^(2h) for a binary tree of depth 4,
conservatively at the largest spread.

## What would count as an answer

- A bound on the defect of the log commute-time metric in terms of the
  within-level spread and the branching, with the threshold ratio that
  follows; or
- a construction showing that the n- and E-dependence cannot be removed in
  general, and the class of hierarchies in which it can.

It bears on [CLAIM-tmpy75jv](../claims.d/CLAIM-tmpy75jv.md), whose "between against within" rests on the
simulation, and on [CLAIM-478](../claims.d/CLAIM-478.md) in its version of 2026-11-20, which asks for
rate differences between levels that exceed those within.

## Note of 2026-11-21: a size-independent slack in the metastability literature

Bovier and colleagues (THEORY-tmph10k5, read in NOTE-tmpjot4l) show that minus the logarithm of the capacity between metastable points is an ultrametric up to an additive ln 3, independent of N, n and E (Corollary 2.6, from Lemma 2.5, which holds for any points). That supports the suspicion here that CLAIM-tmpxi826's size-dependent factor is an artefact of worst-case bounds. It does not settle the question: their slack bounds the defect among capacities, not the distance from the minimax-barrier ultrametric, which still carries prefactors, and their results beyond §2 assume diverging time ratios.
