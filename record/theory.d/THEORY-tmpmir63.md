---
status: Proposed
title: 'Driscoll, Shenoy and Sussillo find that recurrent networks trained on many cognitive tasks reuse shared dynamical motifs across tasks that share subtasks, carried in unit clusters whose lesion impairs only those tasks, and that a held-out task is learned quickly by training only its rule input when earlier training contained its motifs and slowly or not at all when it did not'
version: 1
source:
- LIT-tmpexypk
tags:
- neuroscience
- representation-learning
- learning-theory
date: '2026-11-19'
promote_when: >-
  An independent study of multitask recurrent networks finds across
  several seeds that learning a held-out task by training only its input
  vector is faster after pretraining on tasks sharing its subtasks than
  after pretraining on tasks lacking one of them, and that zeroing a unit
  cluster or subspace tied to one subtask impairs only the tasks that use
  it.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-tmpexypk](../literature.d/LIT-tmpexypk.md) in [NOTE-tmp7fq38](../notes.d/NOTE-tmp7fq38.md). Reuse of learned
  components lowers a later task's cost in RNNs; the transferred component
  is not intervened on. Proposed until its promote_when is met.
---

# THEORY-tmpmir63: Driscoll, Shenoy and Sussillo find that recurrent networks trained on many cognitive tasks reuse shared dynamical motifs across tasks that share subtasks, carried in unit clusters whose lesion impairs only those tasks, and that a held-out task is learned quickly by training only its rule input when earlier training contained its motifs and slowly or not at all when it did not

## The account

Leaky RNNs and GRUs of 128 to 1024 units, trained on 15 tasks with one-hot rule inputs, share fixed-point motifs across tasks with shared subtasks. Training only a new rule-input vector learns MemoryAnti fast after pretraining that included the anti and memory motifs, and slowly or not at all after pretraining lacking the anti motif or no pretraining. Cluster lesions impair only the tasks using the cluster's motif.

## Evidence

3–5 networks per condition; learning curves without threshold numbers; lesions on one network.
