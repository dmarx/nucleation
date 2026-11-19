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

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-tmpf6s7m THEORY-tmpmy98s THEORY-tmpq9sev — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Candidates for the reading this lead now asks for first, from the
follow-up readings, none a full match. Petty and colleagues
([THEORY-tmpq9sev](../theory.d/THEORY-tmpq9sev.md)) measure how a learned component (code) changes later
compositional generalization, at size-matched controls, but as final
accuracy without a matched first stage or an intervention. The
procedural-pretraining paper ([THEORY-tmpmy98s](../theory.d/THEORY-tmpmy98s.md)) measures a later cost with
and without a learned component and removes the saving by shuffling the
transferred weights, an intervention on the learned representation; its
components are procedures, not a shared latent mapping. Papadimitriou and
Jurafsky ([THEORY-tmpf6s7m](../theory.d/THEORY-tmpf6s7m.md)) transfer frozen structure to a later task. A
targeted search of the task-composition literature is still to do.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-tmp442o6 THEORY-tmp51mqd THEORY-tmp80vhs THEORY-tmpezk6j THEORY-tmpmir63 THEORY-tmpoqh3f THEORY-tmpowquo THEORY-tmpw5877 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

The search this lead asked for, and eight readings. No work runs the full
design. The parts are covered separately. (a) A later cost with and
without the earlier learning: Zhang, Lepori and Pavlick (THEORY-tmp51mqd),
Goudar and colleagues (THEORY-tmp80vhs), Ito and colleagues
(THEORY-tmpoqh3f, pretraining counted), Driscoll and colleagues
(THEORY-tmpmir63), Furuta and colleagues (THEORY-tmp442o6). (b)
Organizations compared: only He and colleagues (THEORY-tmpowquo), where a
shortcut model with higher first-stage accuracy than a grokked one
composes new facts worse; not matched, observational, single runs. (c) An
intervention on the learned component: a frozen transplant of the located
subnetwork against a size-matched random one (Zhang, Lepori and Pavlick),
a readout barred from the reused subspace (Goudar and colleagues),
covariance resampling (Maennel and colleagues, THEORY-tmpw5877). Against
the lead's hope: mixing sub-tasks in gives little (Thomm and colleagues,
THEORY-tmpezk6j), and transplanting g's own grokked module often raises
the cost of h∘g (Furuta and colleagues). For the memorization arm, Maennel
and colleagues show a random-label first stage changes later cost through
input statistics, so that arm needs covariance and norm controls. The gap:
He and colleagues' circuit-against-shortcut contrast, matched on
first-stage accuracy, with Zhang, Lepori and Pavlick's transplant and
random-subnetwork controls. That combination is not in the literature
found; stage stays idea.
