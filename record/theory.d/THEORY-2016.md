---
number: 2016
status: Proposed
formerly:
- THEORY-tmp9tvpg
title: 'Friston and colleagues show, in simulations of a three-ball rule-discovery task, that adding to expected free energy the expected information gain over a prespecified set of model structures, computed by Bayesian model reduction, lets an active-inference agent choose observations that identify the generating rule faster than when only information gain over states and parameters, or none, drives its choices'
version: 1
source:
- LIT-2815
tags:
- neuroscience
- probabilistic-modeling
date: '2026-11-19'
promote_when: >-
  An independent rerun of the three-ball simulations (or the authors'
  code) reproducing that, over the same 64 games, removing model
  information gain lengthens discovery or prevents it in some games, and
  removing all information gain leaves the rule undiscovered in about
  half; or the same ordering on a second task with a prespecified
  hypothesis space.
summary: >-
  From the reading of [LIT-2815](../literature.d/LIT-2815.md) in [NOTE-2105](../notes.d/NOTE-2105.md). Friston, Da Costa,
  Tschantz, Heins, Buckley, Verbelen and Parr (2026), Nature
  Communications 17:10125, DOI 10.1038/s41467-026-77209-5 (open access).
  The paper adds to active inference's expected free energy an expected
  information gain over model structures. It computes that gain by
  Bayesian model reduction over a hypothesis space fixed in advance by
  symmetry priors (81 rules in a three-ball task), so the agent chooses
  the observations that best discriminate rules. In 64 simulated games the
  rule was found in a modal 14 trials. Without information gain about half
  the games failed. It assumes the rest of the generative model is known.
  Here because the exchange named it as prior art for structure learning
  beside [THEORY-564](THEORY-564.md). It qualifies that entry without meeting its
  promote_when, and it shows the mechanism [CASE-153](../cases.d/CASE-153.md)'s sentry would block.
  Read in its NOTE.
---
<!-- inactive-ok-file: THEORY-564 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2016: Friston and colleagues show, in simulations of a three-ball rule-discovery task, that adding to expected free energy the expected information gain over a prespecified set of model structures, computed by Bayesian model reduction, lets an active-inference agent choose observations that identify the generating rule faster than when only information gain over states and parameters, or none, drives its choices

## The account

In a POMDP where the rule lives in the likelihood to a feedback modality, the authors enumerate 81 candidate rules from symmetry priors. Their Bayesian model average is the full prior. Bayesian model reduction of the accumulated Dirichlet posterior then scores each rule, both after the data and in prospect under each policy, which gives an expected information gain over models. With this term added, an agent found the true rule in a modal 14 trials over 64 games. Mean discovery fell from 28.5 to 19.4 trials when model and parameter information gain were restored. Without any information gain about half the games never found the rule. One game committed prematurely to a wrong rule.

## What it does not show

- Nothing about structure learning when the hypothesis space is not given or does not contain the truth. The authors note that each added symmetry raises the chance of excluding the true rule.
- No comparison with other optimal-design or active-learning criteria, or with nonparametric structure learners.
- It does not show that Bayesian model reduction recovers structure such as the number of hidden causes, the open part of [THEORY-564](THEORY-564.md).
- Simulation only, on one task; no human or neural evidence.
