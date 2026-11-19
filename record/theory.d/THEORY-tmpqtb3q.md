---
status: Proposed
title: 'Schoenholz and colleagues show, in mean-field theory of wide random fully connected networks with bounded activations and in experiments on MNIST and CIFAR-10, that the correlation between two inputs approaches its limit over a depth scale that diverges only at the order-to-chaos transition, that gradients vanish or explode over the same scale on either side, that networks train when their depth is below about six times that scale, and that dropout removes the transition and so caps trainable depth'
version: 1
source:
- LIT-tmpn5ate
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-281
- QUESTION-125
promote_when: >-
  An independent study of deep fully connected tanh networks reproduces
  the measured correlation depth scale against the mean-field prediction,
  its divergence at the transition, the trainability boundary near a fixed
  multiple of it, and the loss of the divergence under dropout.
summary: >-
  From the reading of LIT-tmpn5ate in NOTE-tmpaon0o. Schoenholz, Gilmer,
  Ganguli and Sohl-Dickstein (2017), ICLR 2017, arXiv 1611.01232. In the
  mean-field theory of wide random networks with bounded activations, the
  correlation between two inputs decays to its limit over a depth scale ξc
  that diverges only at the order-to-chaos transition; gradients vanish or
  explode over the same scale on either side, and in experiments on MNIST
  and CIFAR-10 networks train only when their depth is below about 6ξc, so
  very deep networks train only near criticality, and dropout, which
  removes the transition, caps trainable depth. Here because A15 set it
  against domain walls as a way of keeping information through depth: it
  is the fine-tuned edge-of-chaos route that the read stand-in LIT-
  tmpyahtz (THEORY-tmpvtafk) claims to avoid over a whole symmetry-broken
  phase. Read in its NOTE.
---
<!-- inactive-ok-file: THEORY-tmpvtafk — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpqtb3q: Schoenholz and colleagues show, in mean-field theory of wide random fully connected networks with bounded activations and in experiments on MNIST and CIFAR-10, that the correlation between two inputs approaches its limit over a depth scale that diverges only at the order-to-chaos transition, that gradients vanish or explode over the same scale on either side, that networks train when their depth is below about six times that scale, and that dropout removes the transition and so caps trainable depth

## The account

In a wide random network, iterating the mean-field maps for one input's variance and two inputs' correlation shows exponential approach to fixed points over depth scales ξq and ξc. ξc diverges where χ1 = 1, the boundary between an ordered phase (inputs become identical) and a chaotic one (inputs decorrelate). The backward pass mirrors it: gradients vanish in the ordered phase, explode in the chaotic, stay stable at criticality. Trained networks of depth 10–300 succeed where depth is below about 6ξc, independent of dataset, optimizer and training time, so arbitrarily deep networks train only at the edge of chaos. Dropout breaks the c* = 1 fixed point, keeps ξc finite and limits trainable depth to about 100 layers in their experiments.

## What it does not show

Anything for ReLU or other unbounded activations, convolutional or residual architectures, or trained (not initial) networks; why the threshold is about 6ξc; anything about generalization; any route to depth that does not require tuning to criticality.
