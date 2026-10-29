---
status: Proposed
promote_when: >-
  A study that embeds the same hierarchies many times across seeds and
  methods and measures how far the runs are from isometric, without
  using the correspondences. It then runs, on the same pairs, an
  isometry-free aligner (GW), isometry-class aligners (orthogonal or
  Möbius maps) and a non-linear registration, with restarts and P@1. The
  account is confirmed if the runs' departure from isometry predicts the
  failure of the isometry-class aligners and of GW alike, and a
  non-linear registration beats both. It is refuted if GW matches the
  non-linear registration, which would make the failure a wrong choice
  of invariance class rather than distortion.
title: 'Poincaré embeddings of one hierarchy from different random seeds differ by more than an isometry of the hyperbolic ball, with branches placed differently and pairwise distances changed, so aligners that allow only a global orthogonal or Möbius map recover almost none of the correspondence, while a non-linear registration by a hyperbolic neural network, trained through a Sinkhorn divergence and started from a pretraining step, recovers a substantial part of it but finds the exact match for under a quarter of items even when the two hierarchies are identical'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-29'
source:
- LIT-tmpentcd
summary: >-
  Alvarez-Melis, Mroueh and Jaakkola (2020), [LIT-tmpentcd](../literature.d/LIT-tmpentcd.md), §§5–7, Figs.
  1–2, Tables 1–2; read in [NOTE-tmp1ftl1](../notes.d/NOTE-tmp1ftl1.md). Proposed: single runs, one
  embedding method for the matching experiments, and GW, the obvious
  isometry-free baseline, is not run. It does not say why seeds disagree
  (the paper conjectures negative sampling), nor that the matching
  preserves the hierarchy's direction, which it does not enforce.
---

# THEORY-tmpd02kg: Poincaré embeddings of one hierarchy from different random seeds differ by more than an isometry of the hyperbolic ball, with branches placed differently and pairwise distances changed, so aligners that allow only a global orthogonal or Möbius map recover almost none of the correspondence, while a non-linear registration by a hyperbolic neural network, trained through a Sinkhorn divergence and started from a pretraining step, recovers a substantial part of it but finds the exact match for under a quarter of items even when the two hierarchies are identical

## Source

Alvarez-Melis, Mroueh and Jaakkola (2020), [LIT-tmpentcd](../literature.d/LIT-tmpentcd.md), §§5–7 and
Appendices A–D, pp. 5–8 and 12–13 of arXiv 1911.02536v2; read in
[NOTE-tmp1ftl1](../notes.d/NOTE-tmp1ftl1.md).

## What was actually shown

**Seeds disagree non-isometrically.** One simple hierarchy embedded twice
in the Poincaré disk, with the same hyperparameters and different seeds,
places its branches differently (Fig. 1, p. 5). Over 5 repetitions on
WordNet mammals, the pairwise-distance matrices of different seeds differ
for three embedding methods, "although less prominent" in high dimension.
"Truly isometric embeddings would yield 0 discrepancy" (Fig. 2, p. 6).

**Isometry-class aligners fail.** On a 10-dimensional, five-language
WordNet, Muse, Self-Learn and Invar-OT reach P@10 of at most 7.65 and
mostly under 2.5. Hyperbolic OT with an orthogonal map reaches 0.47 to
11.2 (Table 1b, p. 8).

**A non-linear registration recovers much of it.** A 10-layer hyperbolic
network, trained by a Sinkhorn divergence under the hyperbolic distance
and pretrained by CrossMap, reaches P@10 of 38.4 to 60.1 across
languages (Table 1b). Matching the English hierarchy to a second
embedding of itself, it gets P@1 22.2 and P@10 88.8. Without pretraining
it gets 0.1 and 0.2, and with Euclidean distance 3.1 and 13.0 (Table 1a,
p. 8). On OAEI ontologies it scores 4.49 to 16.67 against at most 4.00
for the baselines (Table 2).

**What could have failed.** Seeds could have agreed up to an isometry, in
which case an orthogonal or Möbius map would have sufficed. The neural
registration could have done no better than the linear ones. Neither
happened.

## What this does not say

- **Why the seeds disagree.** Negative sampling is the authors'
  conjecture, "left for future work" (p. 6).
- **That an isometry-free method would fail.** GW is invariant to every
  isometry and needs no registration. The paper asserts that GW cannot
  handle this case (p. 3) and never runs it.
- **That the matches are exact.** P@1 is 22.2 even when the two
  hierarchies are identical; across languages only P@10 is reported.
- **That the result is stable.** All numbers are single runs. The full
  model starts from a random permutation (CrossMap), so which
  correspondence it settles on depends on the optimiser's path.
- **That the hierarchy's direction is preserved.** The transport cost is
  the symmetric hyperbolic distance, and the registration is constrained
  only to map the ball into itself. Ancestry and entailment are not in
  the objective.
- **That the tree's own symmetries are resolved.** Swapping isomorphic
  subtrees is an isometry of the tree, and no structure-only method can
  choose between the swaps ([THEORY-tmpa43ta](THEORY-tmpa43ta.md)).
