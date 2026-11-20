---
number: 2065
status: Proposed
formerly:
- THEORY-2065
title: 'Chen and colleagues report that at an equal total budget of training steps, training a language model on a mixture of a target skill''s data with the data of its prerequisite skills reaches a given validation loss on the target in fewer steps, or a lower loss in the same steps, than training on the target''s data alone, and that a sequential curriculum over the same skills does no better than random sampling'
version: 1
source:
- LIT-2849
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, or the authors' code run with several seeds,
  reproduces a mixture of target and prerequisite data reaching a target
  loss threshold in fewer total steps than target-only training at equal
  budget on a synthetic and a natural task family, and the sequential
  skill curriculum no better than random on the same skills.
corroborates:
- CLAIM-756
bears_on:
- QUESTION-039
summary: >-
  From the reading of [LIT-2849](../literature.d/LIT-2849.md) in [NOTE-2165](../notes.d/NOTE-2165.md). Co-acquisition
  lowering a target's cost at a fixed budget, the earlier data's cost
  counted. Proposed until its promote_when is met.
---

# THEORY-2065: Chen and colleagues report that at an equal total budget of training steps, training a language model on a mixture of a target skill's data with the data of its prerequisite skills reaches a given validation loss on the target in fewer steps, or a lower loss in the same steps, than training on the target's data alone, and that a sequential curriculum over the same skills does no better than random sampling

## The account

Define a skill by its data. One skill is a prerequisite of another when
mixing its data in lets the other reach a loss threshold with no more
total data than training on the other alone. On synthetic reasoning and
arithmetic tasks such prerequisites save about a third of the steps; on
instruction categories they lower loss a few per cent at fixed budget.
Which skills help is found by short probe runs and departs from the
task's own logic; ordering skills in sequence does not help, and many
groupings give no usable structure.

## Evidence

Continual pretraining of 125M to 3B models; synthetic results without
stated variance, later ones over five seeds; small gains on real corpora.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2076 THEORY-2078 THEORY-2082 THEORY-2083 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Parallels on mixing against sequencing. Stern and colleagues
([THEORY-2081](THEORY-2081.md)) find interleaving keeps what a front-loaded first phase loses,
without a significant natural-language gain. Feng, Prabhumoye and
colleagues ([THEORY-2076](THEORY-2076.md)) find quality-phased order beats random order
of the same blend by 1.74 points, a different kind of ordering and
confounded with a re-anneal. Yıldız and colleagues ([THEORY-2083](THEORY-2083.md)) find
a similarity sequence ends worse than random. Opper and colleagues
([THEORY-2082](THEORY-2082.md)) find random sampling hard to beat. Petty and colleagues
([THEORY-2078](THEORY-2078.md)) find code acts as a prerequisite for formal-output and
arithmetic targets, not natural-language ones. Analogies; none contradicts
this account.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-2089 THEORY-2091 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Thomm and colleagues ([THEORY-2089](THEORY-2089.md)) are in tension: mixing a
composition's sub-tasks into training barely lowers the composed task's
samples, where mixing prerequisites in saved steps here; the measures
differ. Ito and colleagues ([THEORY-2091](THEORY-2091.md)) contrast on order: sequence
decides everything there.
