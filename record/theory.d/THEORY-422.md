---
number: 422
status: Active
formerly:
- THEORY-tmp2psod
title: "In the standard formal models of group learning, no communication network is best for every epistemic problem: costly transmission favours minimally connected or star networks, pooling of estimates by averaging favours regular networks, and learning by trying in bandit problems can favour sparse ones, so a group's network cannot be judged until its learning problem is known"
version: 1
tags:
- epistemology
- network-science
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-716
extends:
- THEORY-143
summary: >-
  Zollman (2013), [LIT-716](../literature.d/LIT-716.md), a survey read in [NOTE-567](../notes.d/NOTE-567.md). Each result it
  gathers is proved or simulated in its source (Bala and Goyal, Jackson and
  Wolinsky, DeGroot, Hegselmann and Krause, Zollman). Under their
  idealisations the optimal structure changes with the problem, so neither
  "too little communication" nor unequal centrality is by itself an
  epistemic pathology. It is a claim about models: utilitarian optimality
  only, with fairness, robustness and the route to the optimum left out.
---
<!-- inactive-ok-file: THEORY-143 THEORY-148 — Proposed; the bandit result this account widens and its mechanism, named as the narrower case -->

# THEORY-422: In the standard formal models of group learning, no communication network is best for every epistemic problem: costly transmission favours minimally connected or star networks, pooling of estimates by averaging favours regular networks, and learning by trying in bandit problems can favour sparse ones, so a group's network cannot be judged until its learning problem is known

## Source

Zollman (2013), [LIT-716](../literature.d/LIT-716.md), "Network Epistemology: Communication in Epistemic
Communities", read in full in [NOTE-567](../notes.d/NOTE-567.md) from the author's manuscript of
5 November 2012.

## What was actually shown

The survey sorts results by kind of learning problem. Each is a result of
its source, under that source's assumptions.

- **Transmission (§2).** With lossless second-hand transmission and costly
  links, minimally connected networks are optimal. With loss over distance,
  stars are. Optimal networks are usually stable but may not be reached.
- **Pooling (§3.1).** Under DeGroot averaging, regular networks are optimal
  in the long run, and more connected ones converge faster.
- **Specialised knowledge (§3.2).** A few heavily contacted individuals
  emerge naturally, so prominence is not evidence of sociological
  distortion.
- **Active learning (§4).** With a pull toward the truth and a connected
  network, structure does not affect the limit. In bandit problems,
  minimally connected networks did best in small simulated groups.

The switches that change the answer are named: whether information passes
on second-hand, whether links cost anything, whether evidence arrives
independently of what agents do, and whether agents learn new facts while
deliberating.

**What could have come out otherwise.** One structure, say the complete
network, could have been optimal across all the problem types. In these
models it is not.

## What this does not say

- **That real communities behave like the models.** All of it is idealised
  models, proved or simulated. Where real groups sit in parameter space is
  not addressed.
- **That less communication is generally better.** That holds only in the
  bandit case, and [LIT-733](../literature.d/LIT-733.md) later narrowed even that to hard problems
  ([THEORY-143](THEORY-143.md)). For pooling, denser is faster.
- **That a network optimal in principle is reachable.** How groups find
  their way to optimal structures is the survey's own open question.
- **Anything beyond utilitarian optimality.** Fairness and robustness to
  link failure are outside most of the models.
- **Anything about sharing reasons.** The agents share attitudes, not
  arguments; Betz (2012) is the one exception cited.

## Connections

- It widens [THEORY-143](THEORY-143.md), Zollman's own bandit result as narrowed by
  Rosenstock et al., into a landscape in which that result is one case.
  [THEORY-148](THEORY-148.md) (transient diversity) is the active-learning mechanism behind
  it.
- It is the record's best single source for the claim that research on
  epistemic networks complicates any simple claim that more communication
  improves collective judgment ([NOTE-567](../notes.d/NOTE-567.md)). §1 names corporations as group
  believers.
- The one-step theory-averaging result of [THEORY-649](THEORY-649.md) is a pooling
  model of a different kind, over logical theories rather than estimates.
