---
number: 790
status: Proposed
formerly:
- THEORY-tmp12b36
promote_when: >-
  The law of balance measured in a deep network trained on real data, during
  its limiting dynamics. What would promote: for parameter groups related by
  a rescaling symmetry (adjacent layers through a ReLU, or the query and key
  matrices of attention), the difference of squared norms moving toward the
  value at which the groups' gradient-noise traces are equal, at a rate that
  scales with learning rate over batch size, with weight decay adding to it.
  That should hold from more than one initialization. What would refute it:
  in such a network at stationarity, the difference staying at its initial
  value, as under gradient flow, or diffusing without a preferred value, as
  under isotropic noise. A failure of the SDE approximation at the learning
  rates used would limit it, not refute it. More solvable toy models cannot
  settle it.
title: In deep networks trained by SGD on real data, minibatch noise drives parameter groups related by a rescaling symmetry toward the point where their gradient noise balances, at a rate set by learning rate over batch size, so that at stationarity they sit neither where gradient flow would leave them nor spread out as under isotropic noise, as Ziyin, Li and Ueda propose
version: 1
tags:
- learning-theory
- loss-landscapes
- thermodynamics
- anthology-candidate
date: '2026-10-20'
source:
- LIT-1012
- LIT-1013
extends:
- THEORY-211
answers:
- QUESTION-164
summary: >-
  Ziyin, Li & Ueda, [LIT-1012](../literature.d/LIT-1012.md), read in [NOTE-714](../notes.d/NOTE-714.md), with the Itô term from
  [LIT-1013](../literature.d/LIT-1013.md). The law of balance is proved in the SDE model of SGD, and that
  part is the Active [THEORY-211](THEORY-211.md). The authors present the law as general to
  networks with rescaling symmetry, but test it only on small synthetic
  networks. This THEORY holds the general claim, for deep networks on real
  data, which no measurement in the record yet supports.
---

# THEORY-790: In deep networks trained by SGD on real data, minibatch noise drives parameter groups related by a rescaling symmetry toward the point where their gradient noise balances, at a rate set by learning rate over batch size, so that at stationarity they sit neither where gradient flow would leave them nor spread out as under isotropic noise, as Ziyin, Li and Ueda propose

## Source

[LIT-1012](../literature.d/LIT-1012.md), [LIT-1013](../literature.d/LIT-1013.md). Filed by the promotion audit's narrowing-loss sweep
(batch 066, [ADR-047](../decisions.d/ADR-047.md) v4) on 2026-10-20, to carry the wider claim that the
narrowing of [THEORY-211](THEORY-211.md) dropped. [THEORY-211](THEORY-211.md) is Active and is this
THEORY's evidence; this one stays Proposed.

## What was actually shown

Within the stochastic-differential-equation model of SGD, with noise
that depends on the parameters, Itô's lemma gives a deterministic drift
of the difference of squared norms along a rescaling symmetry, toward the
point where the two groups' gradient-noise traces are equal, at a rate
proportional to η/S. [THEORY-211](THEORY-211.md) states that result, re-derived in the
promotion audit. The authors call the law general ([NOTE-714](../notes.d/NOTE-714.md),
Limitations), and they read edge-of-stability behaviour and the claim
that the minimal model's phenomena "exist uniquely in deep networks"
from it. Their tests are a two-layer ReLU network on Gaussian data and
toy and tanh models. Whether a deep network on real data, in its
limiting dynamics, shows the drift is what this THEORY claims.

## What would settle it

The promote_when is inherited from [THEORY-211](THEORY-211.md)'s before it was
narrowed, and [QUESTION-164](../questions.d/QUESTION-164.md) asks the same question.

## What this does not say

It does not say that the SDE approximation holds at the learning
rates deep networks are trained with; where it fails, the law is limited,
not refuted. It does not carry the authors' edge-of-stability reading,
which is argued from the minimal model only.
