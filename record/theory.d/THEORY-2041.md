---
number: 2041
status: Proposed
formerly:
- THEORY-tmpqtb3q
title: 'Schoenholz and colleagues show, in mean-field theory of wide random fully connected networks with bounded activations and in experiments on MNIST and CIFAR-10, that the correlation between two inputs approaches its limit over a depth scale that diverges only at the order-to-chaos transition, that gradients vanish or explode over the same scale on either side, that networks train when their depth is below about six times that scale, and that dropout removes the transition and so caps trainable depth'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    A dated note: CLAIM-767 reads the ordered phase as
    the contracting row of the record's drift model. No change of status or title.
source:
- LIT-2825
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-281
- QUESTION-125
- QUESTION-507
promote_when: >-
  An independent study of deep fully connected tanh networks reproduces
  the measured correlation depth scale against the mean-field prediction,
  its divergence at the transition, the trainability boundary near a fixed
  multiple of it, and the loss of the divergence under dropout.
summary: >-
  From the reading of [LIT-2825](../literature.d/LIT-2825.md) in [NOTE-2101](../notes.d/NOTE-2101.md). Schoenholz, Gilmer,
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
  tmpyahtz ([THEORY-2051](THEORY-2051.md)) claims to avoid over a whole symmetry-broken
  phase. Read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-767 CLAIM-773 — Proposed; filed in the contribution of 2026-11-20 on μP, depth scaling and modular duality -->
<!-- inactive-ok-file: THEORY-2051 — Proposed; cited in this filing of 2026-11-19 -->

<!-- inactive-ok-file: THEORY-2168 LIT-3028 — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22, and the Deferred work it names -->

# THEORY-2041: Schoenholz and colleagues show, in mean-field theory of wide random fully connected networks with bounded activations and in experiments on MNIST and CIFAR-10, that the correlation between two inputs approaches its limit over a depth scale that diverges only at the order-to-chaos transition, that gradients vanish or explode over the same scale on either side, that networks train when their depth is below about six times that scale, and that dropout removes the transition and so caps trainable depth

## The account

In a wide random network, iterating the mean-field maps for one input's variance and two inputs' correlation shows exponential approach to fixed points over depth scales ξq and ξc. ξc diverges where χ1 = 1, the boundary between an ordered phase (inputs become identical) and a chaotic one (inputs decorrelate). The backward pass mirrors it: gradients vanish in the ordered phase, explode in the chaotic, stay stable at criticality. Trained networks of depth 10–300 succeed where depth is below about 6ξc, independent of dataset, optimizer and training time, so arbitrarily deep networks train only at the edge of chaos. Dropout breaks the c* = 1 fixed point, keeps ξc finite and limits trainable depth to about 100 layers in their experiments.

## What it does not show

Anything for ReLU or other unbounded activations, convolutional or residual architectures, or trained (not initial) networks; why the threshold is about 6ξc; anything about generalization; any route to depth that does not require tuning to criticality.

## Note of 2026-11-19: Poole and colleagues, read
<!-- inactive-ok-file: THEORY-2031 — Proposed; cited from the readings of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-2204 — Proposed or Unavailable; the reading of the NIPS 2004 companion and the work it stands in for, 2026-11-22 -->

The direct ancestor, read ([THEORY-2031](THEORY-2031.md); [NOTE-2099](../notes.d/NOTE-2099.md)). Poole and colleagues derive the length and correlation maps, χ1 and the phase diagram this account rests on, and already note that "correlations typically take about 20 layers to approach the fixed point, while lengths need only 4" (§3), anticipating the two depth scales. They have no gradients, depth scales or trainability, and their emphasis is on the chaotic phase, not on criticality.

## Note of 2026-11-20: the ordered phase as contraction in depth

[CLAIM-767](../claims.d/CLAIM-767.md) reads depth as a restatement chain. In this reading's ordered
phase each layer pulls the correlation between inputs toward its fixed point,
which is the contracting row of [CLAIM-773](../claims.d/CLAIM-773.md)'s drift model: the input is
forgotten geometrically, over this reading's depth scale. A residual skip
connection moves the chain to the copied-with-error row. [CLAIM-767](../claims.d/CLAIM-767.md)
grounds on this reading for that row; it adds nothing to the reading's
mean-field result.

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

A contrast ([NOTE-2259](../notes.d/NOTE-2259.md), [THEORY-2168](THEORY-2168.md)). That paper's transition is
branching (absorbing-to-active) criticality in a stochastic spiking
network, not the order-to-chaos transition of this reading, and it says
the side on which a finite-time optimum lies depends on "the type of
phase transition", citing for the chaos transition Toyoizumi and Abbott
([LIT-3028](../literature.d/LIT-3028.md), registered, Deferred), where the supercritical side helps.
It does not bear on the depth scales shown here. No relation is written.

## Note of 2026-11-22: Natschläger, Bertschinger and Legenstein, read

**A parallel** ([LIT-3058](../literature.d/LIT-3058.md), [NOTE-2288](../notes.d/NOTE-2288.md), [THEORY-2204](THEORY-2204.md)). The same
Derrida-style annealed mean field of two trajectories, following Derrida
and Pomeau, gives the order-to-chaos line of driven recurrent threshold
networks, K·P_bf = 1, as this reading gives it for wide random
feedforward networks; there the input is injected at every step and the
states are binary. The companion ties the line to readout performance on
time series, which this reading's depth scales do not address. No
relation is written.
