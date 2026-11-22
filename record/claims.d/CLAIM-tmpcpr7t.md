---
status: Proposed
title: 'In small models trained by gradient descent on MSE without continual re-whitening, the whitened class-separation singular values neither grow as (4t/N)^(1/4) nor tend to equality, so the quarter-power law describes the renormalized flow and not gradient descent'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from the study that carries out
    LEAD-035 (CASE-tmpjn6f4).
role: thesis
warrant: empirical
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-181
- QUESTION-051
grounds:
- CASE-tmpjn6f4
- THEORY-278
defeated_if: >-
  A model trained by ordinary gradient descent (or SGD) on MSE, with no
  imposed within-class re-whitening, whose ω_j, the singular values of
  Σ_W^(−1/2)M̃ in its penultimate features, grow with a late log-log slope
  near 1/4 over at least a decade of training time while their max/min
  ratio falls toward 1, near the central path. A run with weight decay
  counts only if ω_j are still growing at that rate, not settling. A
  closed-form result in the renormalized model does not count, nor do
  NC1–NC4 curves alone, nor a fit of the level of (4t/N)^(1/4) with the
  slope free.
summary: >-
  Han, Papyan and Donoho derive ω_j ~ (4t/N)^(1/4), with ratios tending to
  1, for unconstrained features re-whitened after every step
  ([THEORY-278](../theory.d/THEORY-278.md)); [THEORY-797](../theory.d/THEORY-797.md) proposes that trained networks follow those
  dynamics. In [CASE-tmpjn6f4](../cases.d/CASE-tmpjn6f4.md) the renormalized flow reproduces the law
  exactly, and nothing trained without the re-whitening does. Without
  weight decay, unconstrained features and two small ReLU networks grow
  ω_j exponentially or with log-log slopes of 2.4 to 5.5 and spread them
  apart, while NC1 stalls: plain gradient flow conserves Σ_T, so ω can
  diverge only by Σ_W turning singular along the readout directions. With
  weight decay, ω_j grow, stall, regrow and settle at finite, unequal
  values, or fall back in an instability. So on this evidence the law is a
  property of the renormalization A3, and [QUESTION-181](../questions.d/QUESTION-181.md)'s answer is "no"
  for small models; at the scale of Han and colleagues' networks it is
  untested. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-797 CASE-tmpjn6f4 — Proposed or new; the proposal this claim bears against and the study it rests on -->

# CLAIM-tmpcpr7t: In small models trained by gradient descent on MSE without continual re-whitening, the whitened class-separation singular values neither grow as (4t/N)^(1/4) nor tend to equality, so the quarter-power law describes the renormalized flow and not gradient descent

## The claim

The quarter-power law of [LIT-974](../literature.d/LIT-974.md)'s Corollary 1 is a property of the
continually renormalized flow, not of gradient descent on MSE. Dropping the
renormalization, and nothing else, changes the growth of ω_j from a
quarter power to an exponential and makes them spread apart; adding
ordinary training of the classifier, or a network that produces the
features, or batch normalization, does not bring the law back; weight
decay makes ω_j settle at finite values instead.

## Grounds

- [CASE-tmpjn6f4](../cases.d/CASE-tmpjn6f4.md): three unconstrained-features dynamics and two small
  networks, weight decay 0 and 5×10⁻⁴, three seeds, numpy. The control
  reproduces Proposition 2 to 4×10⁻⁵, which shows the measurement and the
  time unit are right.
- [THEORY-278](../theory.d/THEORY-278.md): the law and its assumptions, A3 among them.
- The reason, shown in the study's tests: the least-squares loss is
  invariant to affine maps of the features, so plain gradient flow
  conserves Σ_T, and separation in whitened coordinates can grow only by
  within-class variance vanishing along the readout directions, which
  need not be the class means. Re-whitening closes that route.

## What it does not say

- Nothing at the scale of Han and colleagues' VGG, ResNet and DenseNet
  runs on image data, with SGD and momentum; that test is still open.
- Not that trained networks leave the central path: in the study they
  stay near it while the loss is above 10⁻⁴.
- Nothing about cross-entropy, or about the limiting direction of
  Corollary 2.
