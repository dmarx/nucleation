---
number: 141
status: Open
formerly:
- QUESTION-tmph1bq0
title: 'For an asymmetric self-supervised objective, such as BYOL or SimSiam with a predictor and stop-gradient, does the eigenfunction characterization of spectral methods fail, or is it replaced by the singular functions of a non-self-adjoint operator?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: pragmatic-transport
refines:
- QUESTION-052
summary: >-
  The open clause of [THEORY-009](../theory.d/THEORY-009.md)'s former promote_when. On 2026-10-19
  [THEORY-009](../theory.d/THEORY-009.md) was narrowed to its reading of the positive-pair papers, where
  self-adjointness comes from the symmetry of the positive-pair
  distribution, and promoted. What replaces eigenfunctions when the
  objective is asymmetric was never part of that reading. No published
  analysis held by the record answers it. The near misses are [LIT-228](../literature.d/LIT-228.md),
  [LIT-242](../literature.d/LIT-242.md) and [LIT-975](../literature.d/LIT-975.md).
---

# QUESTION-141: For an asymmetric self-supervised objective, such as BYOL or SimSiam with a predictor and stop-gradient, does the eigenfunction characterization of spectral methods fail, or is it replaced by the singular functions of a non-self-adjoint operator?

## Why it is a question

[THEORY-009](../theory.d/THEORY-009.md) reads how the spectral self-supervised papers get their
eigenbases. In Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) and HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)) the
operator is self-adjoint because the positive-pair distribution is
symmetric. Until 2026-10-19 its promote_when asked for something the
THEORY's body disclaims: a published analysis of an asymmetric objective.
At the owner's direction, from the promotion audit's batch 007
(the audit's decision file for [THEORY-009](../theory.d/THEORY-009.md), [ADR-047](../decisions.d/ADR-047.md)), the reading
was narrowed and promoted, and the asymmetric case moved here unchanged.

It is open because no source the record holds analyses an asymmetric
objective of the BYOL kind. These are the near misses recorded on
2026-10-14:

- **Balestriero and LeCun's Theorem 7** ([LIT-228](../literature.d/LIT-228.md), [NOTE-752](../notes.d/NOTE-752.md)) handles a
  non-symmetric pair structure by CCA. But the objective is Barlow Twins,
  and the CCA identification is asserted, not derived.
- **Simon et al.** ([LIT-242](../literature.d/LIT-242.md), [NOTE-741](../notes.d/NOTE-741.md)) treat two-tower pairs, but with a
  symmetrized loss.
- **Zhai's thesis** ([LIT-975](../literature.d/LIT-975.md), [NOTE-770](../notes.d/NOTE-770.md)) derives the singular value
  decomposition (Theorem 2.11) for X ≠ A. But it only names asymmetric
  objectives such as BYOL and SimSiam, without analysing them.

## What would answer it

The condition formerly on [THEORY-009](../theory.d/THEORY-009.md): a published analysis of an
asymmetric self-supervised objective. It would have to show either that
the eigenfunction characterization fails, or that it is replaced by the
singular functions of a non-self-adjoint operator. A further symmetric
example cannot settle it.
