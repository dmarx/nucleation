---
status: Open
title: 'Does linear mode connectivity emerge during training rather than at initialization outside image classification and beyond MLPs: in a language model or transformer, for copies spawned from a shared state and for independent runs aligned under the architecture''s symmetry group, and for standard-width convnets or ResNets after alignment?'
version: 1
tags:
- loss-landscapes
- learning-theory
date: '2026-10-29'
line: learned-structure
refines:
- QUESTION-069
summary: >-
  The promotion condition formerly on THEORY-114, moved here when the
  tenth status review narrowed it to the image-classification networks
  and MLPs its two sources measured and promoted it, as THEORY-285's
  moved to QUESTION-303.
---

# QUESTION-tmpqgo1h: Does linear mode connectivity emerge during training rather than at initialization outside image classification and beyond MLPs: in a language model or transformer, for copies spawned from a shared state and for independent runs aligned under the architecture's symmetry group, and for standard-width convnets or ResNets after alignment?

## Why it is a question

THEORY-114 holds that linear mode connectivity appeared during training
and not at initialization, in the settings its sources measured. Frankle
et al.'s onset covers six vision networks, and Git Re-Basin's aligned
onset covers MLPs on MNIST and CIFAR-10 only. Whether the same holds for
other architectures and tasks is not shown.

## What would answer it

THEORY-114's former promote_when, unchanged:

The onset measured outside image classification, and the aligned half
measured on more than MLPs. Frankle et al.'s onset covers six vision
networks, and Git Re-Basin's aligned onset covers MLPs on MNIST and
CIFAR-10 only. What would promote: in a language model or a transformer,
the barrier tracked against training time, with seeds, both between copies
spawned from a shared state and between independently initialized runs
aligned under the architecture's symmetry group, with each high at step 0
and falling to near zero later. Or the aligned onset reproduced for
standard-width convnets or ResNets. What would refute it: independently
initialized networks of practical width that are linearly connected after
alignment at step 0, under an alignment computed from the initial weights
alone. Or copies spawned at initialization of a standard deep network that
end up linearly connected. More vision networks with the same onset curve
cannot settle it.
