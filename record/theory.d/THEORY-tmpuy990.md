---
status: Proposed
title: 'Keller and colleagues show that a simple recurrent network whose recurrence is a local convolution initialised as a shift carries travelling waves in its hidden state, and that on copy, adding and sequential-image tasks it learns faster and keeps inputs over far longer delays than a matched wave-free recurrent network, because propagation moves each input along instead of letting later inputs overwrite it'
version: 1
source:
- LIT-tmptu1jw
tags:
- representation-learning
- neuroscience
date: '2026-11-19'
bears_on:
- QUESTION-tmpcb0bf
promote_when: >-
  The comparison reproduced by others, or by the authors at larger scale,
  with the advantage tied to propagation itself: a trained wave model
  whose memory advantage disappears when propagation is blocked or
  reversed at test time while weights and readout stay fixed, or a wave-
  free control that differs from the wave model only in whether activity
  propagates.
summary: >-
  From the reading of [LIT-tmptu1jw](../literature.d/LIT-tmptu1jw.md) in [NOTE-tmpv8ehw](../notes.d/NOTE-tmpv8ehw.md). Keller, Muller,
  Sejnowski and Welling (2024), ICLR 2024, arXiv 2309.08045. A recurrent
  network whose recurrence is a ring convolution initialised as a one-step
  shift (the Wave-RNN) carries travelling waves in its hidden state, and
  against a matched wave-free network (the identity-initialised RNN) it
  learns faster and keeps inputs far longer: more than five orders of
  magnitude lower loss on the copy task, the adding task solved at length
  1000, and much more input information retained with the recurrence
  frozen. The authors read the wave field as a register in which
  propagation stops later inputs overwriting earlier ones; randomly
  initialised local recurrences learn waves in training. Here because A15
  of the exchange "Topological protection explained" listed it among ways
  learned systems keep information through time ([QUESTION-tmpcb0bf](../questions.d/QUESTION-tmpcb0bf.md)), and
  [LIT-647](../literature.d/LIT-647.md) mentions it. The evidence is comparative across models, with no
  intervention on the waves themselves. Read in its NOTE.
---
<!-- inactive-ok-file: LIT-647 — Unavailable; cited in this filing of 2026-11-19 -->

# THEORY-tmpuy990: Keller and colleagues show that a simple recurrent network whose recurrence is a local convolution initialised as a shift carries travelling waves in its hidden state, and that on copy, adding and sequential-image tasks it learns faster and keeps inputs over far longer delays than a matched wave-free recurrent network, because propagation moves each input along instead of letting later inputs overwrite it

## The account

A ring of hidden units with a circulant recurrence that shifts activity one step per time step is the discretised one-way wave equation. Inputs written at one site travel around the ring, so the time of each input becomes its position in the wave field and later inputs do not overwrite it. In the static alternative (an identity-initialised RNN), activity stays where it was written and decays, so inputs to the same site collide. On the copy task the wave model reaches losses five orders of magnitude lower and copies over 500 steps where the static model fails beyond ten; it solves the adding task at length 1000; it is unaffected by permuting the pixel order; with frozen recurrence and encoder it keeps far more input information (89.0% against 44.3% on sMNIST). Randomly initialised convolutional recurrences learn waves during training; identity-initialised ones never do.

## What it does not show

- That waves in cortex serve memory: the paper models none.
- That the advantage is due to propagation alone, as distinct from the convolutional, sparse recurrence that produces it: the iRNN given the shift initialisation improves but stays behind.
- Any intervention on a wave inside a trained network.
- Anything about defects, walls, or features individuated in the wave field.
