---
status: Proposed
title: 'Chen and colleagues report that at an equal total budget of training steps, training a language model on a mixture of a target skill''s data with the data of its prerequisite skills reaches a given validation loss on the target in fewer steps, or a lower loss in the same steps, than training on the target''s data alone, and that a sequential curriculum over the same skills does no better than random sampling'
version: 1
source:
- LIT-tmpagqou
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
  From the reading of LIT-tmpagqou in NOTE-tmpwrmog. Co-acquisition
  lowering a target's cost at a fixed budget, the earlier data's cost
  counted. Proposed until its promote_when is met.
---

# THEORY-tmpd6l4a: Chen and colleagues report that at an equal total budget of training steps, training a language model on a mixture of a target skill's data with the data of its prerequisite skills reaches a given validation loss on the target in fewer steps, or a lower loss in the same steps, than training on the target's data alone, and that a sequential curriculum over the same skills does no better than random sampling

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
