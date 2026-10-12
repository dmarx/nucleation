---
number: 59
status: Proposed
formerly:
- CLAIM-tmph3w8f
title: 'Repeated reconstruction has three regimes, contracting toward conventions, neutral accumulation and amplification, and amplification needs a metric other than total variation, an enlarged state or state-dependent dynamics'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-tmp6zbr9: the metric and the
    estimation of the sensitivities are fixed before the data. Version
    1's condition read: 'Measured per-generation sensitivity of real
    reconstruction chains shows no difference between conditions that
    the theory assigns to different regimes.'
role: thesis
defeated_if: >-
  Per-generation sensitivities, estimated in a metric fixed in advance
  (not total variation, in which no Markov step amplifies) from several
  independent retellers per generation on held-out and perturbed inputs,
  show no difference between conditions that the theory assigns, in
  advance, to different regimes.
tags:
- complex-systems
- mathematics
date: '2026-10-08'
line: pragmatic-transport
rests_on:
- CLAIM-056
summary: >-
  A50 §3, A52 §5.3 and the crystallized argument §19, recovered. The
  manuscript and C7 Appendix B keep the corrected bound and the remark
  that κ ≤ 1 in total variation; the taxonomy and its third experiment's
  test were dropped.
objected_by:
- CLAIM-tmp6zbr9
---
<!-- inactive-ok-file: CLAIM-049 CLAIM-056 CLAIM-068 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-059: Repeated reconstruction has three regimes, contracting toward conventions, neutral accumulation and amplification, and amplification needs a metric other than total variation, an enlarged state or state-dependent dynamics

## The claim

A110 §19: contracting (L < 1: "convergence toward stable conventions"), neutral
(L = 1: "Local distortions can accumulate without amplification"), amplifying
(L > 1: "Small deviations may become disproportionately consequential"). "For
Markov kernels acting on probability measures under total variation distance,
the contraction coefficient is at most one. Amplification requires a different
metric, an expanded state model, or an appropriate state-dependent dynamics." The
argument's Experiment 3 tested it: "Do relational structures exhibit identifiable
contraction, instability, or convergence toward conventions distinct from the
source?"

## Where it went

The manuscript §8 corrects the bound, measuring e_i against a reference transport
with Lipschitz constants κ_i, and keeps the caveat: "For stochastic kernels in
total variation, contraction coefficients do not exceed one; amplification may
arise under other metrics or nonlinear, adaptive representations." C7 Appendix B:
"distances on reconstructed relational representations need not satisfy the same
bound." The regimes as a classification, and the experiment that would tell them
apart, are gone. The contracting regime is [CLAIM-068](CLAIM-068.md); the amplifying one needs
the enlarged state of [CLAIM-049](CLAIM-049.md).
