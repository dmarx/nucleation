---
number: 2088
status: Proposed
formerly:
- THEORY-tmp80vhs
title: 'Goudar and colleagues find that a recurrent network trained without a meta-learning objective on successive sensorimotor association problems sharing a trial structure needs exponentially fewer trials for each new problem, reuses a low-dimensional decision subspace across problems, and loses the saving when its readout is barred from that subspace'
version: 1
source:
- LIT-2881
tags:
- neuroscience
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds finds that recurrent
  networks trained without a meta-objective on successive association
  problems sharing a trial structure show exponentially falling trials to
  criterion, and that barring the readout from the decision subspace
  shared across problems after the first problem restores first-problem
  cost while control readout perturbations do not.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-2881](../literature.d/LIT-2881.md) in [NOTE-2171](../notes.d/NOTE-2171.md). A learned shared
  structure lowers later problems' cost, and barring its use removes the
  saving. Proposed until its promote_when is met.
---

# THEORY-2088: Goudar and colleagues find that a recurrent network trained without a meta-learning objective on successive sensorimotor association problems sharing a trial structure needs exponentially fewer trials for each new problem, reuses a low-dimensional decision subspace across problems, and loses the saving when its readout is barred from that subspace

## The account

Thirty 100-unit RNNs: a few thousand trials for problem 1, a few hundred for problem 2, then an exponential fall to about 21 trials (time constant about 48 problems). A decision subspace of about 2.4 dimensions carries most variance and is reused. Rotating the frozen readout onto stimulus directions after problem 1 makes problem 2 as slow as problem 1; frozen or permuted readouts keep the speed-up.

## Evidence

30 seeds for the curve; ten networks with 50 repeats for the perturbation; one architecture.
