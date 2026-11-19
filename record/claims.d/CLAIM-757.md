---
number: 757
status: Proposed
formerly:
- CLAIM-tmp5vg7p
title: 'Whether relief from overconsolidation has a deadline depends on how the capacity to acquire is lost: if it is sustained by use and decays with disuse (the conditions of the owner-endorsed model of learning by doing), renewed varied practice restores it before a threshold point in training and not after; if it is used up by training, as in plasticity loss under continued varied practice, renewed practice does not restore it at any point, and only an intervention that renews what was used up, such as reinitializing units, does, at any point; the evidence read so far fits the second'
version: 2
role: thesis
warrant: interpretive
defeated_if: >-
  A case that fits neither branch: a network whose capacity to acquire,
  lost under continued training, is restored by renewed varied practice
  after every reinitializing intervention has failed; or one in which
  practice restores it at every point, with no threshold, while the
  capacity also decays with disuse. Also defeated if the loss Dohare and
  colleagues measure, read as depletion here, turns out to be disuse of
  some sub-capacity that varied practice does not exercise, so that the
  first branch covers their case too.
history:
- version: 2
  date: '2026-11-19'
  note: >-
    Revised after the readings of 2026-11-19 (curation entry 071802), at
    the owner's request. Dohare and colleagues find plasticity lost
    gradually while networks keep practising on new tasks, with no
    threshold, and kept by continually reinitializing little-used units:
    decay with use, against version 1's antecedent. Version 1 was a
    conditional on CLAIM-605's conditions; version 2 states both branches
    and which the evidence fits. Role changed from supposed to thesis: the
    claim no longer rests on an unshown antecedent. Version 1's title read:
    'If a learner''s capacity to acquire new structure is itself learned by use, decays with disuse and needs capacity already present to regrow, then recovery from overconsolidation by renewed practice has a deadline: renewed exposure to varied tasks restores the capacity to acquire when it comes before a threshold point in training and not after, while an intervention that raises the capacity directly (a reset of some weights) can still restore it after the threshold if it lifts the capacity back above it; in a heterogeneous population the threshold may show as a steep or probabilistic transition rather than a step'.
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
- readiness
rests_on:
- CLAIM-605
- CLAIM-758
bears_on:
- QUESTION-495
summary: >-
  The assistant's, offered on 2026-11-19 after filing the exchange
  "Topological protection explained" and accepted by the owner the same
  day. It joins [CLAIM-605](CLAIM-605.md), which shows that where capacity is learned by
  doing, decays with disuse and needs capacity to grow, support that does
  the work has a deadline after which withdrawal no longer restores
  capacity, to overconsolidation ([CLAIM-758](CLAIM-758.md), the owner's
  generalization of overfitting). Supposed: it holds only if [CLAIM-605](CLAIM-605.md)'s
  three conditions describe a network's capacity to acquire, which nothing
  on record shows. Its test is an arm of [CASE-294](../cases.d/CASE-294.md). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
  Revised to version 2 after the readings of 2026-11-19: it now states two
  branches, and the evidence (Dohare and colleagues) fits depletion by use.
uses:
- TERM-131
---
<!-- inactive-ok-file: THEORY-2006 THEORY-2027 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-294 CLAIM-758 THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-757: Whether relief from overconsolidation has a deadline depends on how the capacity to acquire is lost: if it is sustained by use and decays with disuse (the conditions of the owner-endorsed model of learning by doing), renewed varied practice restores it before a threshold point in training and not after; if it is used up by training, as in plasticity loss under continued varied practice, renewed practice does not restore it at any point, and only an intervention that renews what was used up, such as reinitializing units, does, at any point; the evidence read so far fits the second


## Version 2, after the readings

Dohare and colleagues ([THEORY-2027](../theory.d/THEORY-2027.md)), read, find networks losing the
ability to learn new tasks gradually, while they keep training on a
stream of varied tasks, with no threshold reported. The loss is kept by
continual backpropagation, which reinitializes a small share of
little-used units throughout. That is the second branch: the capacity is
used up by training, not left unexercised, so practice cannot be what
restores it, and a direct renewal works whenever it is applied. Dong's
depletion reading ([THEORY-1353](../theory.d/THEORY-1353.md)) is the same branch at the level of
attention heads. The first branch, version 1's, stays as [CLAIM-605](CLAIM-605.md)'s
consequence where its conditions hold; nothing read shows them for
networks. Springer and colleagues ([THEORY-2006](../theory.d/THEORY-2006.md)) explain their
inflection mostly by forgetting, which neither branch is about.

The test is unchanged in form. In [CASE-294](../cases.d/CASE-294.md), apply renewed practice
and, separately, reinitialization or resets at each checkpoint. Under the
second branch practice fails throughout and reinitialization works
throughout; under the first, practice fails only after a point.

## The claim

[CLAIM-605](CLAIM-605.md)'s model is dC/dt = λPC(1 − C) − μC, with practice P itself
limited by capacity (at most τC). Growth then falls short of decay below
an unstable threshold, where λτC(1 − C) = μ (C = 0.276 in its numbers),
so capacity held down long enough falls below the point from which
practice can rebuild it, and withdrawing the support no longer restores
it. Its subject is a party whose work is done by support. In
overconsolidation ([CLAIM-758](CLAIM-758.md)) the learner's own efficient procedure
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

In [CASE-294](../cases.d/CASE-294.md), at every checkpoint, apply renewed practice
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
([CLAIM-758](CLAIM-758.md), [CLAIM-520](CLAIM-520.md)).

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Dohare and colleagues ([THEORY-2027](../theory.d/THEORY-2027.md)), read, bear on the antecedent. Networks lose plasticity while continually trained on varied new tasks, which is renewed practice, and the decline is gradual: performance "began falling steadily". Only direct interventions maintain plasticity (small weights with injected randomness, selective reinitialization of units), and all run from the start, so a late rescue is untested. In this setting the capacity to acquire decays with use, not disuse, which reads against [CLAIM-605](CLAIM-605.md)'s model describing it and presses the defeater's second clause.

Springer and colleagues ([THEORY-2006](../theory.d/THEORY-2006.md)), read, try no late intervention that raises plasticity; their mitigations are fine-tuning-time choices (a smaller learning rate, regularization toward the pre-trained weights) that trade the new task against the old. Their inflection point in training time is explained by forgetting, which is the claim's last defeater. So the one inflection on record is not this claim's deadline. It leaves the claim open.

What the readings do to its standing. The conditional is untouched, but nothing read supports its antecedent for networks, and the one setting that applies varied practice throughout shows gradual decline under use. To survive, the claim would have to say what exercising the capacity to acquire is, so that Dohare's continual training is not already it, and measure the deadline as a rise in acquisition cost with held capabilities kept, so that a forgetting-driven inflection like Springer's does not count. The test in [CASE-294](../cases.d/CASE-294.md) stands as written.

No status change.

## Note of 2026-11-19: Anguita and colleagues, read
An analogy only (NOTE-tmpr453b): rescaling the readout, or shrinking all weights, at the start of fine-tuning moves a network back toward learning new features, which resembles the branch where an intervention renews what training used up. There is no loss of capacity over training and no threshold in their model, so no evidence for either branch.
