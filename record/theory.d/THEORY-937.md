---
number: 937
status: Proposed
formerly:
- THEORY-tmpgtvdv
promote_when: >-
  A checked derivation, recorded here, that under the error of Eq. 1.3 the
  gradient for each expert is its posterior responsibility for the case
  times its error, and that with a uniform gate and every error above 1 the
  best-fitting expert takes the largest step and under Eq. 1.2 the
  smallest (made when filed, from NOTE-1147); together with a second
  study, on another task, in which mixtures trained this way leave most
  experts with near-zero mixing proportions while matching a dense network
  of equal size. It is refuted if the gradients differ from those stated,
  or if the vowel result does not replicate. Whether the idle experts could
  regain responsibility is a separate question, and a result about it
  neither promotes nor refutes this.
title: 'When a mixture of experts is trained on the error of a single expert chosen stochastically by the gate, or on the negative log-likelihood of the mixture, an expert that fits a case better than the gate-weighted average gains responsibility for it; on a four-class vowel task, mixtures of 4 or 8 linear experts learned in about half the epochs of backpropagation networks of equal size, at equal accuracy, and divided the task by class pair, leaving all but 2 or 3 experts with mixing proportions effectively zero'
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-24'
source:
- LIT-1514
summary: >-
  Jacobs, Jordan, Nowlan and Hinton (1991), read in full in [NOTE-1147](../notes.d/NOTE-1147.md)
  from a scan of the published article. The gradients of Eqs. 1.4 and 1.5
  were re-derived when filed. The task is small (two formants, 75
  speakers, 25 runs per system) and has two natural subtasks; the idle
  experts are read by the authors as economy, and their recovery is not
  tested.
---

# THEORY-937: When a mixture of experts is trained on the error of a single expert chosen stochastically by the gate, or on the negative log-likelihood of the mixture, an expert that fits a case better than the gate-weighted average gains responsibility for it; on a four-class vowel task, mixtures of 4 or 8 linear experts learned in about half the epochs of backpropagation networks of equal size, at equal accuracy, and divided the task by class pair, leaving all but 2 or 3 experts with mixing proportions effectively zero

## Source

Jacobs, Jordan, Nowlan & Hinton (1991), [LIT-1514](../literature.d/LIT-1514.md), read in
[NOTE-1147](../notes.d/NOTE-1147.md): Eqs. 1.2–1.5 (pp. 80–82), Table 1 and Figures 2–3
(pp. 84–87).

## What was actually shown

- **The rule.** With E = −log Σ_i p_i exp(−½e_i²), e_i = ‖d − o_i‖, the
  gradient for expert i is its posterior responsibility h_i = p_i
  exp(−½e_i²) / Σ_j p_j exp(−½e_j²) times (d − o_i). The gate's gradient
  moves p_i toward h_i, so an expert whose likelihood is above the
  p-weighted average gains share for that case. Re-derived when filed.
- **The speed.** 1124 and 1083 mean epochs to criterion for 4 and 8
  experts against 2209 and 2435 for 6 and 12 hidden units, 25 runs each,
  with 88% train and 90% test accuracy for all four.
- **The division.** From equal mixing proportions, experts first converge
  on the one-line average solution, then split by class pair once their
  errors differ; in every run all but 2 or 3 experts end with mixing
  proportions effectively zero.

## What this does not say

That the concentration on a few experts is entrenchment rather than
economy: the task needs two or three lines, and the split follows
differences in error, not a head start. That an idle expert could regain
responsibility if the task changed; this was not tested. Or anything
about large mixtures, where Shazeer et al. ([LIT-1507](../literature.d/LIT-1507.md)) report the
imbalance as a failure.
