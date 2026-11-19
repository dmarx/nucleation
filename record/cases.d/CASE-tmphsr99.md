---
status: Proposed
title: 'A proposed study: across Pythia checkpoints of one pretraining run, measure the budget each checkpoint needs to acquire held-out synthetic task families by fine-tuning, in-context learning and test-time training, and the success it reaches by sampling and interaction, to see whether later checkpoints are better now but cost more to teach new tasks (overconsolidation), and what exchange rates hold among these ways of spending work'
version: 1
standing: stipulated
kind: proposed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
draws_on:
- THEORY-1353
- THEORY-439
- THEORY-1894
bears_on:
- QUESTION-tmpwqepn
- QUESTION-338
summary: >-
  Requested by the owner at U23 of the exchange "Topological protection
  explained" (2026-11-19), "design an experiment using pythia", to test
  overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)). A52 designed it; A54, A56, A58, A60,
  A62 and A67 added arms after the owner raised meta-learning (U24),
  in-context learning (U25), test-time training (U26), Large Language
  Monkeys and PASS@(k,T) (U27) and active learning (U30). Its prior result
  is Dong's plasticity loss over Pythia training ([THEORY-1353](../theory.d/THEORY-1353.md), Proposed).
  Not run. The design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp2gj7u LIT-tmpjmy81 LIT-tmpkfcwr LIT-tmppcswh LIT-tmpws19o LIT-tmpyyhs0 — Deferred; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-697 CLAIM-tmp8ljvp THEORY-1353 THEORY-1703 THEORY-1894 — Proposed; cited in this filing of 2026-11-19 -->

# CASE-tmphsr99: A proposed study: across Pythia checkpoints of one pretraining run, measure the budget each checkpoint needs to acquire held-out synthetic task families by fine-tuning, in-context learning and test-time training, and the success it reaches by sampling and interaction, to see whether later checkpoints are better now but cost more to teach new tasks (overconsolidation), and what exchange rates hold among these ways of spending work

## The core design (A52)

- **Models.** Pythia-70M-deduped checkpoints from early to final (eight
  steps), with 160M for replication ([LIT-tmpyyhs0](../literature.d/LIT-tmpyyhs0.md)). Seeds of fine-tuning
  are not independent pretraining runs, which the design says.
- **Tasks.** Three synthetic families randomized per example: parity,
  associative retrieval and two-hop composition.
- **Measure.** The adaptation cost of a checkpoint on a task: the least
  fine-tuning budget reaching a threshold accuracy, with fresh optimizer
  state and a preregistered learning-rate rule, censored at a cap. The
  old language-modelling loss is measured before and after.
- **Hypothesis.** Later checkpoints need more budget to acquire the new
  families (overconsolidation), not explained by forgetting.
- **Interventions.** Reset query–key weights; reset value–output weights;
  a matched random perturbation; replay. Each is scored on two axes, new
  capability gained and old lost: "it is not a free restoration of
  plasticity." [CLAIM-347](../claims.d/CLAIM-347.md)'s note of 2026-11-04 already says a reset counts
  as relief only if background skills survive.
- **Readings.** Slower and better at keeping old competence is a
  stability–plasticity trade, not a failure; only slower with no better
  retention is clear evidence.
- **Pilot.** Four checkpoints, two tasks, three seeds: 24 runs.

## Arms added in later turns

- **Meta-learning (A54, after U24).** Three adaptation modes (frozen
  readout, full fine-tuning, in-context); a Reptile meta-trained arm with
  matched resources ([LIT-tmp2gj7u](../literature.d/LIT-tmp2gj7u.md)); held-out task-generating processes,
  not only held-out tasks, against meta-overfitting ([LIT-tmpws19o](../literature.d/LIT-tmpws19o.md),
  [LIT-tmpjmy81](../literature.d/LIT-tmpjmy81.md)); higher pretraining weight decay as a preventive arm
  ([LIT-tmpkfcwr](../literature.d/LIT-tmpkfcwr.md)).
- **In-context learning (A56, after U25).** A response surface over
  checkpoint, number of demonstrations and fine-tuning budget, with the
  prediction that in-context adaptability may rise while fine-tuning
  plasticity falls, which would defeat the overconsolidation reading for
  that model ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)'s defeated_if). Controls separating task
  recognition from task learning ([LIT-tmppcswh](../literature.d/LIT-tmppcswh.md); Min et al., [THEORY-496](../theory.d/THEORY-496.md)).
- **Test-time training (A58, after U26).** In-context, episodic test-time
  training by Akyürek's leave-one-out protocol ([THEORY-439](../theory.d/THEORY-439.md)), continual
  test-time training and persistent fine-tuning, with separate budgets
  for context, compute, latency and memory. If a newly initialized small
  adapter does much better than updating existing weights, that points to
  a shortage of modifiable organization ([THEORY-1353](../theory.d/THEORY-1353.md)'s uncommitted heads).
- **Sampling and interaction (A60, after U27).** Pass@k curves per
  checkpoint and an interactive task varying breadth k and depth T, with a
  separate verifier, so coverage is kept apart from delivered success
  ([CLAIM-697](../claims.d/CLAIM-697.md), [THEORY-1894](../theory.d/THEORY-1894.md), [THEORY-1703](../theory.d/THEORY-1703.md)).
- **Exchange rates (A62).** The least multi-resource budget per
  checkpoint and task as a Pareto frontier ([CLAIM-585](../claims.d/CLAIM-585.md)), read as exchange
  rates among training, context, adaptation, sampling and verification:
  [QUESTION-338](../questions.d/QUESTION-338.md)'s question in general form.
- **Active acquisition (A67, after U30).** Random, uncertainty,
  information-gain and capability-value selection of demonstrations, with
  selection compute charged, matched budgets, and held-out tasks chosen
  independently of the policy.

## What it could and could not show

It could show that later checkpoints of one run need a larger budget to learn new
task families and whether any intervention or acquisition route relieves
it. It could not distinguish pretraining length from the shape of that
run's schedule, with one run; nor show that the synthetic families stand
for capabilities that matter. The owner asked for the design; whether to
run it is the owner's call.
