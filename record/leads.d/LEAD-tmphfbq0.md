---
status: Open
title: 'Build a small compositional task environment in which one learned structure can be reused by later tasks, with learners matched on first-stage performance'
version: 1
stage: idea
method:
- empirical
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-756
summary: >-
  ChatGPT's first proposal at A80 (f = h∘g, structured, memorizing and
  shortcut learners matched on first-stage performance, with an
  intervention on the learned representation of g). Demoted after the
  owner's U37, but still the environment the inquiry lead needs.
---

# LEAD-tmphfbq0: Build a small compositional task environment in which one learned structure can be reused by later tasks, with learners matched on first-stage performance

## What it would do

Tasks generated from a shared latent mapping g and later rules h over
it; compare learners that come to represent g, memorize, or take a
shortcut, matched on first-stage performance; measure the cost of
acquiring h∘g; disrupt the representation of g to see whether the saving
goes with it.

## Why it is still an idea

Pretraining already shows prior learning making later learning cheaper
in general (the owner, U37); what this would add is control over which
organization causes it. Worth specifying only if the readings of the
pretraining literature leave that open.

## Note of 2026-11-19: Hu, Petty, Shi, Merrill and Linzen, read
Hu and colleagues' setup ([NOTE-tmpm4pxy](../notes.d/NOTE-tmpm4pxy.md)) is a ready testbed for this lead's mediation test: disrupt or reinitialize the subnetwork found after the formal-language phase, before natural-language pretraining, and see whether the token saving goes. Their first phases matching only local statistics are a partial analogue of the shortcut arm. That is the assistant's suggestion, not the paper's.
