---
status: Proposed
title: 'Liu, Neubig and Xiong find in Pythia-architecture models of 70M to 1B parameters pretrained on C4 that replacing part of the later pretraining data with specialized data, at matched total tokens, lowers loss after a fixed fine-tuning budget on distant target domains and little on close ones, and that a heavy code mix helps most when introduced early and, introduced late, ends worse than none, which they read as a plasticity window inferred from timing'
version: 1
source:
- LIT-tmpvfc1j
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication at a second scale or schedule shows a matched
  mix of specialized data in pretraining lowering loss after fine-tuning
  on that domain at matched total tokens, and the advantage of a heavy mix
  declining with its start time when the learning-rate schedule and the
  count of specialized tokens are held fixed across start times.
summary: >-
  From the reading of LIT-tmpvfc1j in NOTE-tmphfhfu. Bears on the deadline
  and overconsolidation claims as a parallel; plasticity is not measured.
  Proposed until its promote_when is met.
---

# THEORY-tmpd6smn: Liu, Neubig and Xiong find in Pythia-architecture models of 70M to 1B parameters pretrained on C4 that replacing part of the later pretraining data with specialized data, at matched total tokens, lowers loss after a fixed fine-tuning budget on distant target domains and little on close ones, and that a heavy code mix helps most when introduced early and, introduced late, ends worse than none, which they read as a plasticity window inferred from timing

## The account

Mix data from the expected fine-tuning domain into the later part of
pretraining, keeping total tokens fixed: fine-tuning on that domain then
ends at lower loss, and general competence is better kept, when the
domain is distant from the pretraining corpus. When matters: a heavy mix
started early does best, and started late does worse than none, with
the benefit falling gradually with start time. The authors call this a
plasticity window and assume plasticity declines in their theory.

## Evidence

Controlled runs, one per condition, at small scale; fine-tuning with
seeds; final loss after a fixed budget; schedule confound unaddressed.
