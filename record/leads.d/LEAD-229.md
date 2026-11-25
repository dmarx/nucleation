---
number: 229
status: Open
formerly:
- LEAD-tmpps25j
title: 'Design a test of counterfactual epistemic richness that holds current task performance fixed, perturbs the environment and introduces unencountered questions, and measures the breadth, cost, speed and reliability of the paths to renewed understanding; and read the definitions of intelligence it would compete with'
version: 1
stage: idea
priority: low
method:
- operationalization
- reading
tags:
- cognition
- psychometrics
- philosophy-of-science
date: '2026-11-23'
line:
- distributed-agency
- learning-and-inquiry
advances:
- CLAIM-1106
- CLAIM-1102
- CLAIM-1156
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A62b's closing proposal, in the exchange
  "Explain First Contact RL" (ChatGPT, the branch of 2026-11-23 08:51),
  that "epistemic intelligence might be measured by counterfactual richness
  rather than observed performance alone", which it offers as "an empirical
  research program" without a design. The lead supplies the design's
  questions and the readings the record lacks: no definition of
  intelligence as efficiency of skill acquisition, or as performance across
  environments, is on the record. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-754 CLAIM-1102 CLAIM-1106 CLAIM-1118 CLAIM-1134 CLAIM-1156 — Proposed; entries filed from this exchange or neighbours cited, not leaned on as in force -->

# LEAD-229: Design a test of counterfactual epistemic richness that holds current task performance fixed, perturbs the environment and introduces unencountered questions, and measures the breadth, cost, speed and reliability of the paths to renewed understanding; and read the definitions of intelligence it would compete with

## The gap

A62b's proposal: "hold current task performance constant, perturb the environment, introduce questions the organization has not encountered, and measure the breadth, cost, speed, and reliability of its available paths toward renewed understanding." It names the measures and no design: what is held constant and how, what counts as a perturbation, how the questions are chosen so that they are new to the organization and not to the experimenter, and how "breadth" of paths is counted.

## The plan

1. **Design.** Specify, for one kind of organization (a team, or a population of artificial agents, where interventions are cheap; [CLAIM-1128](../claims.d/CLAIM-1128.md) says a team's separable members make it an experimental model):
   - *matching*: pairs equal on a declared battery of current tasks, so that the operational frontier of [CLAIM-754](../claims.d/CLAIM-754.md) is held fixed;
   - *perturbation*: a novelty hierarchy, borrowing SAIL-ON's levels ([NOTE-1822](../notes.d/NOTE-1822.md)), so that how new a question is can be declared;
   - *outcome*: for each new question, the time, cost and reliability of reaching an adequate answer, and the number of distinct routes taken, routes told apart by which perspectives contributed; this is the developmental kernel of [CLAIM-1156](../claims.d/CLAIM-1156.md), measured with the repair of [CLAIM-1095](../claims.d/CLAIM-1095.md);
   - *the contrast*: whether the matched pairs differ, which is what [CLAIM-1106](../claims.d/CLAIM-1106.md)'s "equally competent today but unequally intelligent" predicts, and whether the difference tracks diversity under a content metric ([CLAIM-1118](../claims.d/CLAIM-1118.md)).
2. **Read.** Register and read, under the `read-and-file` skill, the definitions such a test would compete with. The identifiers are from memory and must be checked at registration (step 3):
   - Chollet, "On the Measure of Intelligence" (2019, arXiv:1911.01547): intelligence as skill-acquisition efficiency over a scope of tasks, given priors and experience. It is the nearest rival: a developmental, counterfactual measure of one agent.
   - Legg and Hutter, "Universal Intelligence: A Definition of Machine Intelligence" (2007, arXiv:0712.3329): expected performance over all computable environments, weighted by simplicity.

## What it would settle

Whether "counterfactual richness" measures anything that efficiency of skill acquisition, applied to the whole organization, does not; and so whether [CLAIM-1106](../claims.d/CLAIM-1106.md)'s ecological account of intelligence adds to the single-agent developmental accounts or restates them for a collective.

## What it would not settle

Whether the owner meant intelligence to be richness or to be understood through it ([CLAIM-1134](../claims.d/CLAIM-1134.md), [CLAIM-1102](../claims.d/CLAIM-1102.md)). That is the owner's choice.
