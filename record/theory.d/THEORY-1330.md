---
number: 1330
status: Active
formerly:
- THEORY-tmple55n
title: 'In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, activation vectors for 275 prompted character roles span a low-dimensional space whose first principal component runs from fantastical to Assistant-like roles, with role loadings correlated above 0.92 between models and the default Assistant at its extreme; the contrast vector from the default Assistant to the role mean aligns with it and is largely present before post-training'
version: 1
tags:
- representation-learning
- self
date: '2026-11-03'
source:
- LIT-1991
summary: >-
  Lu et al. (2026), [LIT-1991](../literature.d/LIT-1991.md), main text read in [NOTE-1505](../notes.d/NOTE-1505.md). Active
  as the reported geometry, with its sizes: three open-weight models,
  judge-filtered role vectors at one layer, base-model evidence from one
  model's PCs and two models' steering. It does not say the Assistant is
  a single direction (the authors call the linear assumption "likely
  flawed"), nor that the axis's meaning beyond its ends is settled.
---
<!-- inactive-ok-file: NOTE-1505 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->

# THEORY-1330: In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, activation vectors for 275 prompted character roles span a low-dimensional space whose first principal component runs from fantastical to Assistant-like roles, with role loadings correlated above 0.92 between models and the default Assistant at its extreme; the contrast vector from the default Assistant to the role mean aligns with it and is largely present before post-training

## Source

Lu, Gallagher, Michala, Fish and Lindsey (2026), [LIT-1991](../literature.d/LIT-1991.md),
arXiv:2601.10387v1; read in [NOTE-1505](../notes.d/NOTE-1505.md).

## What was actually shown

- 4–19 PCs explain 70% of the variance of 377–463 role vectors (§2.1.3).
- PC1 role loadings correlate > 0.92 between every pair of models; its
  ends are fantastical (bard, ghost, leviathan) and Assistant-like
  (evaluator, reviewer, consultant) (§2.2).
- The default Assistant projects to within 0.03 of one end of PC1, against
  0.27–0.50 on PCs 2–10 (§2.3.1).
- The Assistant Axis (default minus role mean) has cosine > 0.71 with PC1 at
  the middle layer (§3.1).
- Gemma 2 27B's base model gives "nearly identical" PCs on the same rollouts;
  steering base Gemma and Llama 3.1 70B with the instruct axis moves
  self-descriptions toward helpful professional humans (§§2.1.3, 3.2.2).

The geometry could have been otherwise: the Assistant could have sat in the
middle of persona space, or PC1 could have differed between models.

## What this does not say

- That the Assistant persona is the axis: one notion of its representation;
  some of it "encoded in the weights, but not explicitly in the
  activations" (§8.1).
- That post-training creates nothing: the AI-assistant associations are
  acquired in post-training (p. 10).
- That persona space has been mapped: the role list is likely incomplete.
