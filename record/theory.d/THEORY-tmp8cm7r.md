---
status: Proposed
title: 'Brown and colleagues show that in autoregressive language models from 125M to 175B parameters, each pretrained on 300B tokens, performance with task demonstrations given in the context and no weight update rises with the number of demonstrations and with model size, the gain over zero-shot growing with size, so that larger models reach a given accuracy with fewer in-context examples; they leave open whether this learns new tasks or recognizes tasks acquired in pretraining'
version: 1
source:
- LIT-tmpjzvu6
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  A replication on another model family with fixed pretraining data finds
  that the number of in-context demonstrations needed to reach a fixed
  accuracy on held-out tasks falls with model size, and that the gap
  between zero- and few-shot widens with size.
summary: >-
  From the reading of [LIT-tmpjzvu6](../literature.d/LIT-tmpjzvu6.md) in [NOTE-tmprmye5](../notes.d/NOTE-tmprmye5.md). The owner's
  suggestion for showing that pretraining makes later task acquisition
  cheap; it shows that across model sizes, not against no pretraining, and
  the acquisition retains nothing. Proposed until its promote_when is met.
---

# THEORY-tmp8cm7r: Brown and colleagues show that in autoregressive language models from 125M to 175B parameters, each pretrained on 300B tokens, performance with task demonstrations given in the context and no weight update rises with the number of demonstrations and with model size, the gain over zero-shot growing with size, so that larger models reach a given accuracy with fewer in-context examples; they leave open whether this learns new tasks or recognizes tasks acquired in pretraining

## The account

Pretrain transformers of increasing size on the same 300B tokens; give
each K demonstrations of a task in its context and no weight update.
Accuracy rises with K and with size, and faster with size than zero-shot
accuracy does, so larger models make more use of each demonstration: on
the plotted synthetic task, the examples needed to reach a level fall
with size. The inner loop is computation in activations over one
sequence; the authors call it in-context learning and leave open whether
it learns new tasks or recognizes tasks learned in pretraining, a
spectrum on which tasks differ.

## Evidence

Benchmarks and synthetic tasks across eight sizes, one run each. No model
without pretraining, no variation in pretraining length, no cost to a
threshold reported as a number.
