---
status: Proposed
title: 'Thomm and colleagues find that transformer language models trained from scratch on algorithmic composition tasks, with the sub-tasks mixed into the same training, need more composed-task samples than the sub-task sets together contain and gain little from the sub-tasks, while pretraining on a composition lowers the cost of later learning one of its sub-tasks'
version: 1
source:
- LIT-tmpaqjh5
tags:
- compositionality
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  A replication with more than one seed per data point finds that mixing a
  composed algorithmic task's sub-tasks into training does not materially
  lower the composed-task samples needed to reach near-perfect accuracy,
  and that pretraining on the composed task lowers the samples later
  needed to fine-tune one of its sub-tasks.
summary: >-
  From the reading of [LIT-tmpaqjh5](../literature.d/LIT-tmpaqjh5.md) in [NOTE-tmp8n812](../notes.d/NOTE-tmp8n812.md). A negative case for
  joint training; staged training is not tested in the forward direction.
  Proposed until its promote_when is met.
---

# THEORY-tmpezk6j: Thomm and colleagues find that transformer language models trained from scratch on algorithmic composition tasks, with the sub-tasks mixed into the same training, need more composed-task samples than the sub-task sets together contain and gain little from the sub-tasks, while pretraining on a composition lowers the cost of later learning one of its sub-tasks

## The account

A 150M LLaMA on PEN, PERM, HSS and MUL: composed-task accuracy with and without the sub-tasks mixed in is about the same at matched composed-task samples, and reaching near-perfect accuracy takes more samples than the sub-task sets together (PEN about 10 times). Composition-pretrained models fine-tune to a sub-task with 25K to 50K samples.

## Evidence

One run per data point; no error bars; one scale.
