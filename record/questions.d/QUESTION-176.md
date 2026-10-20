---
number: 176
status: Open
formerly:
- QUESTION-tmpygew3
title: "Do networks trained by gradient descent on a mixture of random facts and a second domain reach the capacity-optimal allocation, so that their threshold size and mixing ratio are the optimal learner's?"
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-039
summary: >-
  Filed when the promotion audit (batch 036, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) narrowed
  and promoted [THEORY-293](../theory.d/THEORY-293.md). The theorem about the optimal capacity-bounded
  learner was re-derived, and Gu et al.'s Pythia runs were accepted as
  showing a threshold. That the trained networks' thresholds are the
  optimal learner's was the former promote_when, and this question holds
  it.
answered_by:
- THEORY-tmptwk75
---

# QUESTION-176: Do networks trained by gradient descent on a mixture of random facts and a second domain reach the capacity-optimal allocation, so that their threshold size and mixing ratio are the optimal learner's?

## Why it is a question

[THEORY-293](../theory.d/THEORY-293.md) now states two things separately: an optimal learner whose
capacity is bounded learns none of a set of equally frequent facts below
a threshold set by the mixing ratio, and all of them once capacity
exceeds it by the facts' total entropy; and Pythia models trained on
synthetic biographies mixed into web text show a threshold in model size
and in mixing ratio. That the second is an instance of the first is
asserted by Gu et al. ([LIT-984](../literature.d/LIT-984.md)) and supported only by the shape of the
curves and one exponent, 1.152 against a predicted 1.283, with no
interval ([NOTE-796](../notes.d/NOTE-796.md)). Below the threshold, much longer training barely
helps. That fits an allocation that never reaches the facts, and also a
dynamical wall the static theory does not see.

## What would answer it

Thresholds predicted in advance from the measured loss-versus-size curve
of the second domain and the facts' total entropy, matched by networks
trained to convergence over several seeds and several mixing ratios, with
recall rising over a width of about the facts' entropy past the threshold,
would answer it yes. Thresholds departing systematically from
(1/(r·p))^(1/(α+1)), or networks below the threshold that learn the facts
given enough further training, would answer it no. More sigmoid-shaped
curves in r or in size do not settle it: they show a threshold, not that
capacity allocation sets it.
