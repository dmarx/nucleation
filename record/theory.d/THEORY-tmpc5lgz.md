---
status: Proposed
promote_when: >-
  An independent study, read first-hand, with new scenarios and parameters
  fixed before the test data, in which an inverse rational-planning model
  with line-of-sight perception and belief updating predicts adults' graded
  belief, desire or world-state judgements on held-out scenarios better
  than the same model without belief uncertainty or without action cost,
  and better than a motion-feature or other cue-based model fitted to the
  same training judgements. Refuted if a cue-based model with no
  mental-state variables does as well on held-out beliefs and desires
  together. A re-analysis of the 2017 data cannot settle it.
title: 'Baker, Jara-Ettinger, Saxe and Tenenbaum propose that people attribute beliefs, desires and percepts to an agent moving through a spatial scene by jointly inverting a model of it as an approximately rational planner that perceives by line of sight and updates its beliefs, so that such a model predicts adults'' graded mental-state and world-state judgements better than versions lacking action costs or uncertain beliefs and better than motion-feature heuristics'
version: 1
tags:
- cognition
- probabilistic-modeling
- model-comparison
date: '2026-11-04'
source:
- LIT-tmphd2wq
summary: >-
  Baker, Jara-Ettinger, Saxe and Tenenbaum (2017), LIT-tmphd2wq, read in
  full in NOTE-tmpnv4hf. Proposed: two experiments (16 and 176 adults)
  support it against the lesioned models, but the motion heuristic tied on
  Experiment 1 beliefs, the desire fit carries no information within
  scenario type, and the test is cross-validation over the authors' own
  scenarios. It is a computational-level claim, not an account of the
  algorithm; it does not say the model is hierarchical, a word that is A's,
  from the owner's pasted synthesis.
---

# THEORY-tmpc5lgz: Baker, Jara-Ettinger, Saxe and Tenenbaum propose that people attribute beliefs, desires and percepts to an agent moving through a spatial scene by jointly inverting a model of it as an approximately rational planner that perceives by line of sight and updates its beliefs, so that such a model predicts adults' graded mental-state and world-state judgements better than versions lacking action costs or uncertain beliefs and better than motion-feature heuristics

## Source

Baker, Jara-Ettinger, Saxe and Tenenbaum (2017), LIT-tmphd2wq; read in
NOTE-tmpnv4hf.

## What was actually shown

- **Experiment 1** (16 adults, 73 scenarios): desire and belief ratings
  predicted at r_BSCV 0.91 and 0.78 over scenarios. Without belief
  uncertainty or action cost, desire fits fall to 0.72 and 0.75 and belief
  fits to −0.022 and 0.10. The motion heuristic predicted beliefs as well
  (0.77) but desires worst (0.62).
- **Experiment 2** (176 online adults, 19 scenarios): inferring hidden cart
  locations from a search path, a task "Our BToM model was not developed to
  account for", BToM 0.91, motion heuristic 0.61, TrueBelief 0.63, NoCost
  0.46.
- These could have come out the other way: the heuristic, fitted to each
  experiment with many more weights, could have matched BToM throughout.

## What this does not say

- That people compute the joint posterior algorithmically; the authors call
  it "a computational-level claim".
- That BToM beats the heuristic on beliefs in Experiment 1: it does not.
- That it predicts desire differences within a scenario type: it does not.
- That it holds for children, recursive beliefs, or settings beyond small
  grid-worlds.
- That the model is hierarchical in the sense of shared, learned
  higher-level knowledge: its priors are fixed grids.
- Anything about how well agents' behaviour is predicted; it predicts
  observers' judgements of scripted agents.
