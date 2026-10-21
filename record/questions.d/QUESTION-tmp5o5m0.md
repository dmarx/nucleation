---
status: Answered
title: 'For linear decisions at the population level, if a kind''s admissible transformations are given as a distribution over pairs of its realizations, is the top eigenspace of the pair operator a stable, decision-sufficient span, and what span takes that role when the pairs are directed?'
version: 1
tags:
- representation-learning
- information-theory
- mathematics
date: '2026-10-21'
line: pragmatic-transport
refines:
- QUESTION-052
summary: >-
  The linear part of [QUESTION-052](QUESTION-052.md), split off under [ADR-049](../decisions.d/ADR-049.md). For symmetric
  pairs, yes: the top eigenfunctions are the most view-invariant
  directions, and their span is minimax-optimal for linear prediction of
  approximately view-invariant targets ([THEORY-007](../theory.d/THEORY-007.md)) and bounds
  linear-probe error by leakage over conductance ([THEORY-228](../theory.d/THEORY-228.md)). For
  directed pairs, the top left singular functions of the
  conditional-expectation operator take that role ([THEORY-239](../theory.d/THEORY-239.md)), and a
  linear readout of the full density ratio suffices for redundant labels
  ([THEORY-319](../theory.d/THEORY-319.md)). Other spans can tie. Nonlinear decisions, and what picks
  one signature out, stay with [QUESTION-052](QUESTION-052.md).
answered_by:
- THEORY-007
- THEORY-228
- THEORY-239
- THEORY-319
---

# QUESTION-tmp5o5m0: For linear decisions at the population level, if a kind's admissible transformations are given as a distribution over pairs of its realizations, is the top eigenspace of the pair operator a stable, decision-sufficient span, and what span takes that role when the pairs are directed?

## Answer

Yes for symmetric pairs, and the top left singular span for directed
ones. Each result is at the population level, for linear probes, and for a
stated class of targets. This is the part of [QUESTION-052](QUESTION-052.md) that the Active
readings settle, split off on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).

- **Symmetric, stability and optimality.** [THEORY-007](../theory.d/THEORY-007.md) (Active), Johnson,
  El Hanchi & Maddison. On a finite augmentation space, the top
  eigenfunctions of the positive-pair chain are the most view-invariant
  directions (Prop. 3.1). Their span is minimax-optimal for linear
  prediction of approximately view-invariant targets, given d ≥ d*, the
  number of communicating classes (Thm 4.1).
- **Symmetric, classification.** [THEORY-228](../theory.d/THEORY-228.md) (Active), HaoChen et al. On a
  finite augmentation space, every population minimizer of the spectral
  contrastive loss spans the top eigenvectors. Its linear-probe error is
  Õ(α/ρ²), the error of recovering the label from an augmentation over
  the squared sparsest-partition conductance (Thm 3.8).
- **Directed.** [THEORY-239](../theory.d/THEORY-239.md) (Active), Zhai. For any joint law, symmetric or
  not, the top-d left singular functions of the conditional-expectation
  operator attain the minimum worst-case linear-probe error over tasks of
  compatibility at least 1 − ε. Its note of 2026-10-19 re-derives this
  without symmetry and works a non-reversible three-state chain on one
  space: the left and right singular functions differ, and the guarantee
  sits on the left ones.
- **Directed, the whole kernel.** [THEORY-319](../theory.d/THEORY-319.md) (Active), Tosh,
  Krishnamurthy & Hsu. When two views are redundant for a label, a linear
  readout of random evaluations of the density ratio approaches the
  near-Bayes predictor at rate 1/m, with no symmetry between the views.

So the answer is "a minimax-optimal span", not "the signature". [THEORY-239](../theory.d/THEORY-239.md)'s
note shows other spans can tie, even with a gap in the singular values.

## What it leaves to [QUESTION-052](QUESTION-052.md)

Whether any span is the kind's signature for nonlinear decisions, and what
picks one out when other spans tie. None of the four says what a trained
network reaches. [THEORY-007](../theory.d/THEORY-007.md) and [THEORY-228](../theory.d/THEORY-228.md) hold on finite spaces only. The
task classes differ: view invariance, label recoverability with
conductance, compatibility, and redundancy. [CLAIM-210](../claims.d/CLAIM-210.md) holds that
kind-sharing is symmetric, so whether a directed pair distribution
describes a kind at all, or a transport, also stays with the parent.
