---
number: 2055
status: Proposed
formerly:
- THEORY-tmpz825j
title: 'Covering partitions only coarsen under GD'
statement: >-
  Velarde, Parra, Hashemi and Makse show that in layered networks a covering
  partition of units, units with equal colour-summed input and output
  weights, can only coarsen under gradient descent, and report that
  tolerance-defined quasi-covers grow during training of an MLP, a CNN and
  an LSTM agent and allow compression to 17–18% of size with little loss,
  while exact automorphisms are never observed
version: 1
source:
- LIT-2843
tags:
- representation-learning
- network-science
date: '2026-11-19'
bears_on:
- QUESTION-492
promote_when: >-
  The record re-derives the cover-persistence step (Theorem 1 for exact
  covers under plain GD) and either an independent replication or the
  paper's own figures show quasi-cover counts at fixed tolerance falling
  during training against an untrained or shuffled-label baseline at the
  same tolerance
summary: >-
  From the reading of [LIT-2843](../literature.d/LIT-2843.md) in [NOTE-2085](../notes.d/NOTE-2085.md). Velarde, Parra,
  Hashemi and Makse (2026), arXiv 2609.01768 (v1, not peer reviewed). They
  carry graph fibrations to weighted layered networks as balanced
  colourings of units. They prove that a covering partition (equal colour-
  summed input and output weights) can only coarsen under gradient
  descent, and report that tolerance-defined quasi-covers grow during
  training of an MLP, a CNN and an LSTM agent, allowing compression to
  17–18% of size; transformers are shown compressed, not tracked in
  training. Fibers here are computed with every input coordinate its own
  colour, so they are input-independent redundancies, not quotients of
  inputs, and the paper has no relational or rule task. Here because it is
  the evidence on the fibration side of the owner's U9 hunch, QUESTION-
  tmpex36a: it shows that balanced structure among units is learned
  without symmetry forcing it, and is silent on role abstraction. Read in
  its NOTE.
---

# THEORY-2055: Covering partitions only coarsen under GD

## The account

For a layered network, call two units in a layer a fiber when, for every fiber colour of the previous layer, their summed input weights from that colour are equal, starting from distinct colours on every input coordinate (Eq. 14). Units in one fiber have the same activity for every input (Eq. 15). Units in one flavoured opfiber, defined by the same condition on output weights, have the same backpropagated error (Eq. 17). Where both hold, a cover, the weight updates in the block are equal (Eq. 5), and so the covering partition only coarsens under gradient descent (Theorem 1, proof in Methods 4.11). Empirically, with a tolerance, the number of distinct quasi-covers falls during training of a three-layer MLP on MNIST and a CNN on ImageNet. In a PPO-trained LSTM it falls and then rises again (Fig. 3a, c, e). Merging each cover into a base graph preserves the forward computation exactly for exact covers and approximately for quasi-covers. It compresses the MLP to 17% of its size with no change in accuracy, and a translation transformer to 18% with tolerated loss (Fig. 3b, d, f).

## What it does not show

- That covers form from random initialization by any proved mechanism. The theorem is about persistence, and its stability under SGD is cited from Chen and colleagues (2023), not proved here.
- That the observed quasi-covers exceed what a fixed tolerance would find in untrained or shuffled-label networks of the same weight statistics. No such baseline was found in the parts read.
- Emergence during training in transformers. Only post-hoc compression is shown.
- Anything about relational tasks, role abstraction or invariance to relabelling of inputs. Fibers here are input-independent: each input coordinate is its own colour, and fiber units agree on every input.
- That the synchronized units are units of anything beyond redundancy. Compression merges them because they are interchangeable, and class-conditional synchrony clusters are coarser than fibers.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
<!-- inactive-ok-file: THEORY-2009 — Proposed; cited from the readings of 2026-11-19 -->

Chen, Kunin, Yamamura and Ganguli, read ([THEORY-2009](THEORY-2009.md); [NOTE-2127](../notes.d/NOTE-2127.md)): the source this account cites for stability under SGD supports less than it is cited for. Velarde and colleagues write that "Any parameter set that is invariant under GD becomes a stable attractor under stochastic GD for sufficiently large learning rates". Chen and colleagues require invariance under every minibatch update, not full-batch descent (Def. 3.1); give only a sufficient condition for attraction, weighing curvature against noise, and call necessity future work; show in a toy that "An increase in the learning rate accelerates the collapsing process until reaching a critical threshold, beyond which the collapsing ceases" (App. G); and work in a continuous model of SGD. Their sets are a vanishing neuron and pairs of identical neurons, the finest case of a cover; covers balanced only by colour sums are not treated. So the stability of learned covers is not established by the cited source. The account's "What it does not show" already says stability is cited, not proved; this says the citation itself is too broad.
