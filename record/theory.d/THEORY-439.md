---
number: 439
status: Active
formerly:
- THEORY-tmp4sei8
title: "Given the same few demonstrations, temporarily updating a language model's weights on them and then conditioning beats conditioning alone, most on tasks with structural rules or distribution shift and most when the update is trained in the in-context format: for models of 1–8B parameters, examples used as context and the same examples used as a training signal are not interchangeable"
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-16'
source:
- LIT-796
summary: >-
  Akyürek et al. (2024; ICML 2025), [LIT-796](../literature.d/LIT-796.md), read in [NOTE-637](../notes.d/NOTE-637.md). On BIG-Bench
  Hard with Llama 3.1 8B and 10 demonstrations over five seeds, zero-shot
  40.9%, in-context 50.5%, per-task LoRA test-time training then
  in-context 57.8%; 12 of 27 tasks gain at least 2 points, and Boolean
  expressions falls. Training the update on leave-one-out in-context tasks
  beats training on bare pairs (57.8% against 51.5%). The update is
  discarded after each task, so it is as transient as a context. It is two
  benchmarks and one model family, and which task property predicts the
  gain is open.
supports:
- CLAIM-118
---
<!-- inactive-ok-file: CLAIM-118 THEORY-169 — Proposed; the claim this finding bears on and the neighbouring account of attention as an inner learner, named, not leaned on -->

# THEORY-439: Given the same few demonstrations, temporarily updating a language model's weights on them and then conditioning beats conditioning alone, most on tasks with structural rules or distribution shift and most when the update is trained in the in-context format: for models of 1–8B parameters, examples used as context and the same examples used as a training signal are not interchangeable

## Source

Akyürek, Damani, Zweiger, Qiu, Guo, Pari, Kim & Andreas (2024; ICML 2025),
[LIT-796](../literature.d/LIT-796.md), read in full in [NOTE-637](../notes.d/NOTE-637.md).

## What was actually shown

**The comparison.** A test task arrives with K demonstrations (10 for
BIG-Bench Hard, 2–7 for ARC) and nothing else. Either the model conditions
on them, or it first trains a task-specific LoRA adapter on them, then
conditions, then discards the adapter. No other data enters. The training
set is leave-one-out in-context tasks: each demonstration in turn is the
query, the rest the context, in permuted orders.

**BIG-Bench Hard (Fig. 1, §5.3).** Llama 3.1 8B, 27 tasks, five seeds:
zero-shot 40.9%, in-context 50.5%, test-time training 57.8%, standard errors
about 0.4%. Training on bare input–output pairs gives 51.5%; dropping the
permutations 55.7%; a shared adapter across tasks 59.8%.

**Where it helps (Fig. 9).** The largest gains are on Dyck languages, Ruin
names, Movie recommendation and Hyperbaton, 20–50 points. Boolean
expressions falls from 85.7% to 80.4%. Of 27 tasks, 12 gain at least 2
points and 2 lose at least 2.

**ARC.** On an 80-task subset with a fine-tuned 1B model, 5% → 29% (Fig. 5);
direct I/O training loses 11 of the solved tasks and dropping the
invertible augmentations 16. On the full public validation set the
fine-tuned 8B model goes from 18.3% to 47.1% (Table 1).

**What could have come out otherwise.** Conditioning could have extracted
everything the demonstrations offer, leaving the update nothing to add. It
did not, on most tasks.

## What this does not say

- **That in-context learning learns nothing.** It gains 9.6 points over
  zero-shot on BBH. The update adds to it, not replaces it, and works best
  when it improves the model's use of context.
- **That the difference is persistence.** The update is discarded after
  the task, so it is as short-lived as a context, yet it is a change of
  parameters. Persistence and the locus of change come apart here.
- **Why some tasks gain and others lose.** The authors propose structural
  rules and distribution shift and leave it "an open question".
- **That it matches people on ARC.** The ensemble with program synthesis
  scores 61.9% in the text and 62.8% in Table 1; hyperparameters were tuned
  on the ablation subset; the ARC models were first fine-tuned on synthetic
  ARC-like tasks; contamination of public ARC and BBH is possible.
- **That it holds beyond 8B parameters or one model family.**

## Connections

- **[THEORY-169](THEORY-169.md)** says that in attention layers conditioning on a context
  is exactly training an inner learner on it. There the update is to a
  model held in activations; here it is to the network's own weights, and
  behaviourally the two uses of the same examples differ.
- **Min et al. ([LIT-814](../literature.d/LIT-814.md), [THEORY-496](THEORY-496.md))**, which this paper cites, find
  that in-context gains are carried by form more than by the
  input–label mapping. The update's advantage is largest where the mapping
  is what the task needs.
- **[CLAIM-118](../claims.d/CLAIM-118.md)** holds that context and interpreter are separate sources of
  interpretive change. This is the measured case at the level of the whole
  model.
- **The anthology** holds the paper as [ANTH-LIT-379](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-379.md) with a practice built
  on it; the method is practice and belongs there.
