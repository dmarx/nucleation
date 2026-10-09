---
status: Active
title: 'fidelity, as observational equivalence over response trajectories'
version: 1
tags:
- philosophy-of-language
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  A35 §8 and A39 §5.3: two systems are faithful when corresponding
  intervention sequences yield matching distributions of observed
  responses, P_o(Y_1:k | a_1:k) ≈ P_t(Y'_1:k | a'_1:k), with no shared
  latent state required. Put "at the center of the formal theory" at
  A39.
used_by:
- CLAIM-tmpd81nk
- CLAIM-tmpeponh
- CLAIM-tmpnvxfj
- CLAIM-tmpizns9
- CLAIM-tmpj4s3r
superseded_by:
- TERM-tmpct68m
---

# TERM-tmpvpzy0: fidelity, as observational equivalence over response trajectories

## Definition

A35 §8 weakened intertwining to "observational simulation",
O_t(U_t(Φ(s))) ≈ O_o(U_o(s)), because "Exact dynamical equivalence may be too
strong for translation. The original and target audiences need not possess
corresponding internal states at every intermediate point." A39 §5.3 stated it
over sequences: P_o(Y_1:k | a_1:k, c_o) ≈ P_t(Y'_1:k | a'_1:k, c_t), "preservation
of the distribution of possible response trajectories under corresponding
action sequences", which "does not require a shared latent state space". Its
functional L_obs(τ) sums a distance over a finite family of intervention
sequences.

## What it is not

Not [TERM-tmp6p5t2](TERM-tmp6p5t2.md), which compares internal states through Φ; A39 demoted that to an
optional refinement. Not [TERM-tmpmvvf2](TERM-tmpmvvf2.md) either: A24 compared single judgements across
contexts, this compares trajectories under interventions ([TERM-tmpkoyrc](TERM-tmpkoyrc.md)). The manuscript
went back to the context form for L_obs (§6) and kept intertwining in §9;
trajectories appear only in §8 ("how selected invariants ... evolve together").
