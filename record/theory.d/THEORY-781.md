---
number: 781
status: Proposed
formerly:
- THEORY-tmp43jo4
promote_when: >-
  The SGD half shown beyond the second-order, diagonal-Hessian argument,
  or measured in a trained network. What would promote: a network with a
  known permutation, rotation or rescaling symmetry, trained with SGD
  across learning rates, batch sizes and weight decays, with a measured
  distance to the symmetric subspace (neuron coincidence, rank, sparsity)
  that falls to zero beyond a threshold predicted from the noise and
  curvature. The same should not happen when the symmetry is removed by
  reparametrization. What would refute it: training that reaches the
  symmetric subspace and leaves it, which part 1 of the theorem forbids;
  or no dependence of the outcome on weight decay and noise where the
  threshold predicts one. More toy factorizations cannot settle it.
title: 'Strong gradient noise in SGD, like weight decay above a threshold, makes the subspace fixed by a mirror symmetry of a network''s loss attracting even where it is a saddle, so that networks trained with SGD at large learning rates or small batches reach sparse, low-rank and identical-neuron solutions, as Ziyin proposes'
version: 1
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-20'
source:
- LIT-1014
summary: >-
  Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), read in [NOTE-716](../notes.d/NOTE-716.md). Beyond the exact half that
  [THEORY-213](THEORY-213.md) holds, the paper argues by a Lyapunov-exponent analysis that
  strong SGD noise makes a mirror's subspace attracting even at a strict
  saddle, and reads sparsity, low rank and identical neurons in trained
  networks as its result. That analysis rests on a second-order, diagonal-
  Hessian approximation, and the network evidence is a ResNet18's
  correlation blocks. The test is [QUESTION-206](../questions.d/QUESTION-206.md).
extends:
- THEORY-213
answers:
- QUESTION-206
---

# THEORY-781: Strong gradient noise in SGD, like weight decay above a threshold, makes the subspace fixed by a mirror symmetry of a network's loss attracting even where it is a saddle, so that networks trained with SGD at large learning rates or small batches reach sparse, low-rank and identical-neuron solutions, as Ziyin proposes

## Source

Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), §§2.4 and 3, read in [NOTE-716](../notes.d/NOTE-716.md), with Appendix C's
proofs unchecked.

## What is asserted

That gradient noise, not only weight decay, pushes training into the
subspaces a network's mirror symmetries fix. Near such a subspace, SGD's
random kicks shrink the off-mirror component on average when the
Lyapunov exponent is negative, roughly when the learning rate exceeds
−2E[ξ + γ]/E[(ξ + γ)²]; that can hold where the subspace is a strict saddle
and gradient descent would leave it. Large learning rates, small batches
and noisy data favour it. Rescaling, rotation and permutation symmetries
then give sparse weights, low rank and identical neurons in SGD-trained
networks.

## What the Active account establishes toward it

[THEORY-213](THEORY-213.md) holds the exact half of Theorem 1, re-derived: the subspace is
invariant under gradient training, and weight decay above half the lower
bound on the Hessian puts every minimum in it. What it does not hold is
this entry's claim, which rests on the approximation and on Fig. 3: sparse
solutions in a reparametrised regression, low rank in a matrix
factorisation, and homogeneous correlation blocks in a ResNet18 on
CIFAR-10, which appear with weight decay and rarely without.

## What would confirm or reject it

The promote_when above, [QUESTION-206](../questions.d/QUESTION-206.md)'s test. Rescaling symmetry counts
here only where it contains a mirror (λ = −1); ReLU's positive rescaling
does not ([THEORY-213](THEORY-213.md), history of version 2).

## Provenance

Filed on 2026-10-20 by the narrowing-loss sweep ([ADR-047](../decisions.d/ADR-047.md) v4, batch 068),
from the gradient-noise clause [THEORY-213](THEORY-213.md)'s title carried before it was
narrowed on 2026-10-20.
