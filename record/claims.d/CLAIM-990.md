---
number: 990
status: Proposed
formerly:
- CLAIM-tmpo59pd
title: 'Intervention discriminates only within its scope'
statement: >-
  A targeted intervention discriminates implementations matched in behaviour
  only relative to its declared scope: in a small gridworld, writing a
  blocked passage into the two units that carry it repairs every failed
  route of a planner on a learned transition table and about a tenth of
  those of a goal-conditioned value learner and of a bank of occupancy
  predictors, though the planner and the value learner act identically,
  while propagating the same block through all the predictors' contents
  repairs every route without any transition table, so responding to an
  intervention as a model would does not by itself show a central model
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A showing that the content-level edit uses a transition table after all,
  that is, that propagating the block through the demons needs the
  next-state function in some form beyond what the demons' own values
  carry. Or a matched comparison in this class in which no edit specified
  on the distributed agent's own contents reproduces the planner's
  response. Not defeated by the unit-level contrast, which the claim
  reports; nor by the planner's edit being cheaper, which it also reports.
tags:
- agency
- cognition
- philosophy-of-science
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-384
corroborates:
- CLAIM-519
bears_on:
- QUESTION-362
summary: >-
  From the run of [CASE-187](../cases.d/CASE-187.md) for [LEAD-160](../leads.d/LEAD-160.md) ([CASE-384](../cases.d/CASE-384.md)). The planner and
  the goal-conditioned value learner choose the same action in every
  (state, goal) pair, so no goal test tells them apart. Writing a blocked
  passage into the two units that carry it does tell them apart. It
  repairs all of the planner's failed routes, 9% of the value learner's
  and 14% of the occupancy predictors'. The same block, propagated through
  every demon by the Woodbury identity from the demons' own values,
  repairs all of the predictors' routes, with no transition table
  anywhere. So the discriminating power [CLAIM-519](CLAIM-519.md) gives targeted
  interventions holds, but relative to the declared intervention
  repertoire, which its defeated_if already lists among what must be
  matched. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-384 CLAIM-519 CLAIM-991 — new or Proposed; the study that grounds this claim, the thesis it corroborates and its companion claim -->

# CLAIM-990: Intervention discriminates only within its scope

## The claim

In [CASE-384](../cases.d/CASE-384.md) the planner and the value learner are behaviourally
identical. Their greedy actions agree in every (state, goal) pair at
every level of competence, so the value learner is the planner's policy
as a table. The occupancy predictors match both in success and nearly in
path length.

A **unit-level intervention** wrote "this passage is blocked" into the
units that carry it in each agent's own representation:
- the planner's two table entries;
- the value learner's two value rows, set to their locally consistent
  values;
- the predictors' two demon rows, likewise.

It repaired 100%, 9% and 14% of the routes each agent failed in the
blocked maze. That is [CLAIM-519](CLAIM-519.md)'s point made concrete: an intervention
separates implementations that every behavioural test leaves together.

A **content-level intervention** on the predictors changes the
predictions themselves. It propagates the block through every demon by
the Woodbury identity, reading the two columns it needs off the demons.
It reproduces retraining exactly and repairs 100% of their failed routes.
Nothing in the agent is a transition table, and no one-step model is
consulted.

So "the edited agent behaves as an agent with a model would" separates
the planner from the predictors under one declared intervention and not
under another. An intervention discriminates relative to its scope. The
scope belongs with memory, computation and history among what a
comparison must match. [CLAIM-519](CLAIM-519.md)'s defeated_if already names a "matched
intervention repertoire". This is a measured case of why.

## What it does not say

- **That the predictors contain a model in disguise.** Their demons hold
  occupancy predictions, not next states. Reading next states out of them
  costs about 4,000 operations per move. See [CLAIM-991](CLAIM-991.md).
- **That the two interventions cost the same.** The planner's edit writes
  2 numbers. The content-level edit writes 16,384. That asymmetry is
  itself evidence about the mechanism, as [CLAIM-519](CLAIM-519.md)'s compression point
  says.
- **Anything about the value learner beyond this.** No content-level edit
  on its values was run. Repairing it means re-solving its Bellman
  equations, which needs the next-state function its values encode only
  implicitly.
