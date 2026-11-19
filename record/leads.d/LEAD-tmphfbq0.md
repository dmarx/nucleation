---
status: Open
title: 'Investigate task composition: whether a structure learned for one task lowers the cost of later tasks composed on it, with learners matched on first-stage performance, looking first for prior research that already runs the experiment'
version: 1
stage: idea
method:
- reading
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
  The question behind ChatGPT's first proposal at A80 (f = h∘g,
  structured, memorizing and shortcut learners matched on first-stage
  performance, with an intervention on the learned representation of g).
  At the owner's direction (review of 2026-11-19), the lead is the
  investigation, not a build: prior research on task composition may
  already run the experiment, and building an environment is one way to
  operationalize it, taken only if none does.
---

# LEAD-tmphfbq0: Investigate task composition: whether a structure learned for one task lowers the cost of later tasks composed on it, with learners matched on first-stage performance, looking first for prior research that already runs the experiment

## What it would do

Find out whether, and when, a structure learned for one task lowers the
cost of acquiring later tasks composed on it, and whether that saving
depends on which organization the learner came to (a representation of
the shared structure, memorization, or a shortcut) at matched first-stage
performance. The experiment of interest: tasks generated from a shared
latent mapping g and later rules h over it; learners matched on
first-stage performance; the cost of acquiring h∘g; and an intervention
on the learned representation of g to see whether the saving goes with
it.

## How

1. **Reading first.** Search the literature on task composition and
   compositional transfer (in curriculum, multitask, meta-learning and
   modular-network work, and in synthetic-task studies of language
   models) for designs that already measure the cost of a composed task
   with and without a learned component, ideally with matched first-stage
   performance or an intervention on the component.
2. **Build only if needed.** If no prior work satisfies the experiment, a
   small compositional task environment is one way to operationalize it.

## Why it is still an idea

Pretraining already shows prior learning making later learning cheaper
in general (the owner, U37); what this would add is control over which
organization causes it. Building something should not be presumed (the
owner, review of 2026-11-19).

## Note of 2026-11-19: Hu, Petty, Shi, Merrill and Linzen, read
Hu and colleagues' setup ([NOTE-tmpm4pxy](../notes.d/NOTE-tmpm4pxy.md)) is prior research of the kind this lead looks for first, and a ready testbed for its mediation test: disrupt or reinitialize the subnetwork found after the formal-language phase, before natural-language pretraining, and see whether the token saving goes. Their first phases matching only local statistics are a partial analogue of the shortcut arm. That is the assistant's suggestion, not the paper's.
