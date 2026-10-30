---
status: Proposed
title: 'When each agent''s Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours'' average; with homogeneous agents, mean field Q-learning converges to the Nash Q-value under assumptions the authors call strong, and learned tasks of 500 and 1000 agents where independent and centralized-critic baselines failed'
version: 1
tags:
- game-theory
- learning-theory
- complex-systems
date: '2026-10-30'
source:
- LIT-1512
extends:
- THEORY-945
promote_when: >-
  A checked derivation, recorded here, of the expansion that removes the
  first-order term and of the remainder bound (made when filed, from
  NOTE-1148), together with either a proof that reconciles the contraction
  condition (Boltzmann temperature above K/2) with the greedy-in-the-limit
  assumption, or an independent replication in which mean field Q-learning
  learns tasks of hundreds of homogeneous agents where independent
  learners fail. It is refuted if the expansion's first-order term does
  not vanish, or if replications with heterogeneous but exchangeable
  agents fail where the paper's succeed. Results for agents that are not
  exchangeable within a neighbourhood fall outside it and neither promote
  nor refute it.
summary: >-
  The wide form of Yang et al. (2018), LIT-1512, kept here when the
  twenty-fourth status review narrowed THEORY-945 to the re-derived
  expansion and to what the paper states and ran, and promoted it
  (ADR-047, kind 1). The paper asserts that mean field Q-learning
  converges to the Nash Q-value under its assumptions, and that it makes
  many-agent learning tractable. Its proof does not reconcile a
  high-temperature contraction with a greedy limit, and its many-agent
  evidence is one task at two sizes.
---

# THEORY-tmp3xe34: When each agent's Q-function is approximated as an average of pairwise terms and expanded about the mean action of its neighbours, the first-order term vanishes and the approximation error is a second-order remainder bounded by the curvature of the pairwise Q-function, leaving a two-body problem between an agent and its neighbours' average; with homogeneous agents, mean field Q-learning converges to the Nash Q-value under assumptions the authors call strong, and learned tasks of 500 and 1000 agents where independent and centralized-critic baselines failed

## Source

Yang, Luo, Li, Zhou, Zhang & Wang (2018), LIT-1512, read in NOTE-1148
from arXiv:1802.05438v5.

## What is shown and what is not

THEORY-945 holds the expansion and the bound, re-derived, and reports the
theorem and the Gaussian Squeeze runs. This entry asserts the theorem,
and asserts the runs as the method's general capacity. Against the
theorem: Proposition 1, which the proof uses, needs the Boltzmann
temperature above K/2, while Assumption 2 needs it to go to zero, and the
paper does not reconcile them (NOTE-1148). Against the general capacity:
the experiment at 500 and 1000 agents is one task, run by the authors.
