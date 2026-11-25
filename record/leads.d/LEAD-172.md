---
number: 172
status: Open
formerly:
- LEAD-tmput8rh
title: 'Run the modular-addition checkpoint study and its prospective test: fit the coupled feature-circuit description on early checkpoints and predict later functional change under held-out training interventions'
version: 1
stage: specified
priority: high
method:
- empirical
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-275
- QUESTION-360
- QUESTION-217
- CLAIM-698
operationalized_in:
- CASE-272
summary: >-
  The first test of the owner's hypothesis that wave mathematics applies
  to learning, for a question cited over a hundred times. Named in
  [QUESTION-275](../questions.d/QUESTION-275.md) and [CASE-272](../cases.d/CASE-272.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-331 CLAIM-900 — new; the run of LEAD-172 and its finding, filed 2026-11-22 -->
<!-- inactive-ok-file: CASE-272 CLAIM-698 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-172: Run the modular-addition checkpoint study and its prospective test: fit the coupled feature-circuit description on early checkpoints and predict later functional change under held-out training interventions

## What it would do

Train small transformers on modular addition, track training-kernel
eigenspaces and each layer's coupling among Fourier modes over
checkpoints, fit the coupled description on early ones, and predict later
change, including under held-out interventions, against a null at equal
edge budget.

Where the record names it:

- [QUESTION-275](../questions.d/QUESTION-275.md): "fit the model using early training checkpoints, then test
  its predictions about later functional changes, including changes under
  held-out training interventions"
- [QUESTION-275](../questions.d/QUESTION-275.md): "it needs a null at equal edge budget before it bears on
  the coupling"
- [CASE-272](../cases.d/CASE-272.md): "the first test of the owner's hypothesis that wave
  mathematics applies to learning"

## What would count

Predictions that beat the null support [CLAIM-698](../claims.d/CLAIM-698.md) and answer [QUESTION-275](../questions.d/QUESTION-275.md)
for this task; predictions no better than the null defeat the coupling as
an account of the circuit's formation.

## Note of 2026-11-22: a reduced run, done

A delegated worker ran a reduced form of the study on CPU (numpy; torch is not installed), filed as [CASE-331](../cases.d/CASE-331.md), with the finding as [CLAIM-900](../claims.d/CLAIM-900.md). Scripts, tests, per-step results and the analysis are under scratch/studies/lead-172/.

Done:
- 25 attention-free networks on addition mod 37: 15 fit arms at weight decay 1.0 and 10 held-out arms at weight decay 0.5 and 2.0, as the held-out training intervention.
- Fourier coupling in the hidden layer and in the logits, Fourier sparsity, the training kernel's top eigenspace and its rotation, measured over checkpoints.
- Two-parameter forecasts of the generalization step, fitted at step 250 or 500 on the fit arms and scored on the held-out arms, against a null of 20 random coupling sets of the same edge count.

Result: the logits' selection-rule coupling forecasts best (RMSE 0.13 to 0.15 in log10 steps, against 0.19 to 0.20 for Fourier sparsity and 0.34 for the null's median), and no null draw beats it. No measure foresaw the five arms that never generalized. The kernel's eigenspace stayed at chance alignment.

What remains of the lead:
- a transformer with attention, which needs torch or a longer hand-written backward pass;
- held-out Fourier ablations as the predicted response, not only the generalization time;
- interventions other than weight decay;
- [QUESTION-275](../questions.d/QUESTION-275.md)'s comparators: the feature-allocation model and circuit-only descriptions.

The stage and status are the owner's.
