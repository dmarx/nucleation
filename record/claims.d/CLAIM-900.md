---
number: 900
status: Proposed
formerly:
- CLAIM-tmp6rhuv
title: 'Selection-rule energy forecasts generalization'
statement: >-
  In small networks trained on addition modulo a prime, the share of the
  network's input-output Fourier energy on the couplings the group's
  selection rule names, measured early in training, forecasts when the
  network generalizes under a training intervention it was not fitted on,
  better than Fourier sparsity, test-set performance and the training
  kernel, and better than the same number of couplings chosen at random; it
  does not foresee whether the network generalizes at all
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from the run of LEAD-172
    (CASE-331), as a delegated worker.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the same comparison, with the same two-parameter forecasts
  fitted on one setting of a training intervention and scored on settings
  it was not fitted on, finds the selection-rule coupling no better than
  Fourier sparsity or test loss, or no better than random coupling sets of
  the same size, on held-out arms; or finds that its advantage disappears
  in a transformer with attention, at another prime or width, or under
  another intervention family (data fraction, learning rate, optimizer);
  or finds that the advantage comes from the measure reading test-set
  outputs, in that a weights-only form of the same coupling loses it. A
  forecast that fails only on runs that never generalize does not defeat
  the claim, which excludes them.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-22'
line:
- learned-structure
grounds:
- CASE-331
bears_on:
- QUESTION-275
corroborates:
- CLAIM-698
summary: >-
  What the run of [CASE-331](../cases.d/CASE-331.md) finds, stated so that it can fail. At step 250 or 500 of
  training, the logits' share of Fourier energy on the p − 1 triads
  (k, k, −k) forecast log10 of the generalization step on 8 held-out
  weight-decay arms with RMSE 0.13 to 0.15, against 0.19 to 0.20 for
  Fourier sparsity, 0.24 to 0.40 for test loss and accuracy, 0.19 to 0.35
  for kernel alignment, and a median of 0.34 for 20 random triad sets of
  the same size, none better. It foresaw none of the 5 arms that did not
  generalize. Evidence for [CLAIM-698](CLAIM-698.md)'s criterion in its easiest setting,
  where the task's group supplies the modes. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-331 CLAIM-698 CASE-272 — new or Proposed; the run this claim reports, the thesis it bears on and the design it reduces -->

# CLAIM-900: Selection-rule energy forecasts generalization

## The claim

In the setting of [CASE-331](../cases.d/CASE-331.md), three things hold.

1. **Which couplings matter, not how many.** The selection rule
   χ_k(a)χ_k(b) = χ_k(a + b) names p − 1 couplings from input modes to
   output modes. The network's early share of energy on them forecasts its
   generalization time on held-out arms; random sets of p − 1 couplings
   forecast no better than a constant. This is the null at equal edge
   budget that [QUESTION-275](../questions.d/QUESTION-275.md) asks for.
2. **It out-forecasts the feature-level baseline.** Fourier sparsity of
   the embeddings, the progress measure for this task, forecasts less well
   on the same held-out arms (RMSE 0.20 against 0.13 at step 500; C2 lower
   in 99.6% of paired bootstrap resamples). On the fit arms themselves the
   two are level, so the difference appears only under the intervention
   the forecasts were not fitted on.
3. **It forecasts timing, not completion.** Under weight decay 2.0 the
   coupling was high early, and test accuracy rose early, stalled below
   0.95 and never reached it. The claim covers runs that generalize.

## Why it is empirical and narrow

One task, one prime (37), one width, one attention-free architecture,
one intervention family, 25 runs. The modes are given by the task's group,
so this is the easy case of [CLAIM-698](CLAIM-698.md): it does not show that modes can be
found where no symmetry supplies them ([CASE-272](../cases.d/CASE-272.md)'s limit). The coupling is
measured on the network's outputs over all inputs, test inputs included;
it beats the test-set baselines, but it is not a forecast from weights
alone. No held-out ablation and no circuit-attribution or
parameter-overlap comparator was run.

## What it changes

[CLAIM-698](CLAIM-698.md) had no executed test; this is one, in its easiest setting, and
it comes out on the claim's side on two of its comparators (feature-level
and random couplings) and silent on the others. The training kernel's top
eigenspace, which [CASE-272](../cases.d/CASE-272.md) also proposed to track, stayed at chance
alignment with the task's functions throughout, so in this network the
coupling description does the work and the kernel description does not.
