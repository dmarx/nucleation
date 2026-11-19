---
status: Proposed
title: 'If a learner''s capacity to acquire new structure is itself learned by use, decays with disuse and needs capacity already present to regrow, then recovery from overconsolidation by renewed practice has a deadline: renewed exposure to varied tasks restores the capacity to acquire when it comes before a threshold point in training and not after, while an intervention that raises the capacity directly (a reset of some weights) can still restore it after the threshold if it lifts the capacity back above it; in a heterogeneous population the threshold may show as a steep or probabilistic transition rather than a step'
version: 1
role: supposed
warrant: interpretive
defeated_if: >-
  Across checkpoints of one training run, the gain in later acquisition
  from renewed practice (varied-task exposure) declines gradually with
  training time, with no point or narrow band after which it falls to
  near zero, where the population of runs is homogeneous enough that a
  threshold would show as a steep transition; or the
  antecedent fails, that is, the capacity to acquire is not drawn down by
  disuse and rebuilt by use, so that CLAIM-605's model does not describe
  training at all. Also defeated if the apparent deadline is explained by
  forgetting of held capabilities rather than by lost capacity to
  acquire.
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
- readiness
rests_on:
- CLAIM-605
- CLAIM-tmp8ljvp
bears_on:
- QUESTION-tmpwqepn
summary: >-
  The assistant's, offered on 2026-11-19 after filing the exchange
  "Topological protection explained" and accepted by the owner the same
  day. It joins [CLAIM-605](CLAIM-605.md), which shows that where capacity is learned by
  doing, decays with disuse and needs capacity to grow, support that does
  the work has a deadline after which withdrawal no longer restores
  capacity, to overconsolidation ([CLAIM-tmp8ljvp](CLAIM-tmp8ljvp.md), the owner's
  generalization of overfitting). Supposed: it holds only if [CLAIM-605](CLAIM-605.md)'s
  three conditions describe a network's capacity to acquire, which nothing
  on record shows. Its test is an arm of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp3dqbl THEORY-tmpgjb4y — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-tmp5vg7p: If a learner's capacity to acquire new structure is itself learned by use, decays with disuse and needs capacity already present to regrow, then recovery from overconsolidation by renewed practice has a deadline: renewed exposure to varied tasks restores the capacity to acquire when it comes before a threshold point in training and not after, while an intervention that raises the capacity directly (a reset of some weights) can still restore it after the threshold if it lifts the capacity back above it; in a heterogeneous population the threshold may show as a steep or probabilistic transition rather than a step

## The claim

[CLAIM-605](CLAIM-605.md)'s model is dC/dt = λPC(1 − C) − μC, with practice P itself
limited by capacity (at most τC). Growth then falls short of decay below
an unstable threshold, where λτC(1 − C) = μ (C = 0.276 in its numbers),
so capacity held down long enough falls below the point from which
practice can rebuild it, and withdrawing the support no longer restores
it. Its subject is a party whose work is done by support. In
overconsolidation ([CLAIM-tmp8ljvp](CLAIM-tmp8ljvp.md)) the learner's own efficient procedure
plays the part of the support: the more training is spent on the present
objective, the less the capacity to acquire other structure is
exercised. If that capacity obeys the same three conditions, the same
threshold follows for recovery by practice: renewed practice restores
the capacity before a point and not after. It does not follow for every
intervention. In [CLAIM-605](CLAIM-605.md)'s model a direct boost that lifts capacity
above the threshold restores growth, so an intervention that raises the
capacity itself, as a weight reset might, can work after the point where
practice alone fails. And across runs that differ in their thresholds, a
step in each run can show as a steep or probabilistic transition in the
pooled curve. (Narrowed at ChatGPT's review of 2026-11-19, forwarded by
the owner: the first version predicted that every plasticity-restoring
intervention fails after the threshold.)

## Why it is supposed

The antecedent is the whole question. Nothing on record shows that a
network's capacity to acquire new task structure is learned by use or
decays with disuse in [CLAIM-605](CLAIM-605.md)'s sense. Dong's plasticity loss
([THEORY-1353](../theory.d/THEORY-1353.md)) reads it instead as uncommitted capacity used up, which
would predict a slope: less relief the more capacity has been committed,
with no threshold. The two readings are what the test separates.

## The test

In [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md), at every checkpoint, apply renewed practice
(mixed-task exposure) and, separately, direct interventions (the
query–key reset, the value–output reset, higher weight decay from a
checkpoint onward), and plot the gain in later acquisition cost against
the checkpoint, per run and pooled. A steep fall in the practice curve,
with direct interventions still working after it, supports this claim; a
gradual decline in both supports the depletion reading. Each intervention is scored on both axes, new capacity
gained and old competence lost, as the case requires.

## The stronger reading it invites and does not support

That training should stop before the threshold. Whether the lost capacity
matters depends on what the learner will later be asked to acquire
([CLAIM-tmp8ljvp](CLAIM-tmp8ljvp.md), [CLAIM-520](CLAIM-520.md)).

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Dohare and colleagues (THEORY-tmpgjb4y), read, bear on the antecedent. Networks lose plasticity while continually trained on varied new tasks, which is renewed practice, and the decline is gradual: performance "began falling steadily". Only direct interventions maintain plasticity (small weights with injected randomness, selective reinitialization of units), and all run from the start, so a late rescue is untested. In this setting the capacity to acquire decays with use, not disuse, which reads against CLAIM-605's model describing it and presses the defeater's second clause.

Springer and colleagues (THEORY-tmp3dqbl), read, try no late intervention that raises plasticity; their mitigations are fine-tuning-time choices (a smaller learning rate, regularization toward the pre-trained weights) that trade the new task against the old. Their inflection point in training time is explained by forgetting, which is the claim's last defeater. So the one inflection on record is not this claim's deadline. It leaves the claim open.

What the readings do to its standing. The conditional is untouched, but nothing read supports its antecedent for networks, and the one setting that applies varied practice throughout shows gradual decline under use. To survive, the claim would have to say what exercising the capacity to acquire is, so that Dohare's continual training is not already it, and measure the deadline as a rise in acquisition cost with held capabilities kept, so that a forgetting-driven inflection like Springer's does not count. The test in CASE-tmphsr99 stands as written.

No status change.
