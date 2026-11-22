---
status: Proposed
title: 'A modular-addition checkpoint study run on CPU: in 25 small attention-free networks trained on addition mod 37, the share of the logits'' Fourier energy on the selection-rule triads at step 250 or 500 forecasts when held-out-weight-decay runs generalize better than Fourier energy, test accuracy, test loss and kernel alignment, and better than every random edge set of the same size, but foresaw none of the runs that failed to generalize'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-172 as a delegated
    worker. Scripts, tests, per-step results and analysis are committed
    under scratch/studies/lead-172/.
standing: documented
kind: executed-study
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-275
- QUESTION-217
variant_of:
- CASE-272
summary: >-
  A reduced run of the design of [CASE-272](CASE-272.md), for [LEAD-172](../leads.d/LEAD-172.md). numpy only, CPU, about
  20 minutes of compute on a shared machine. 25 networks (p = 37, an
  embedding for each operand summed into 128 ReLU units, then an
  unembedding; full-batch AdamW, lr 0.01): 15 fit arms at weight decay 1.0
  (training fraction 0.4, 0.5, 0.6), 10 held-out arms at weight decay 0.5
  and 2.0, a training intervention the fits never saw. At early checkpoints
  each measure is a two-parameter linear forecast of log10 of the step at
  which test accuracy reaches 0.95. The logits' energy on the p − 1 triads
  (k, k, −k) that the identity χ_k(a)χ_k(b) = χ_k(a + b) selects forecasts
  the 8 held-out arms that generalized with RMSE 0.154 (step 250) and 0.130
  (step 500), against 0.345 for a constant, 0.19 to 0.20 for Fourier
  energy, 0.25 to 0.28 for test accuracy and 0.19 to 0.35 for kernel
  alignment; 20 random off-rule sets of p − 1 triads give a median of 0.34
  and never beat it. No measure foresaw the 5 runs that did not reach 0.95
  in 15000 steps; under weight decay 2.0 the rule coupling was high early,
  test accuracy rose to 0.64 to 0.75 by step 2000 and then crept, to 0.86 at
  most. The network is not a transformer, the target is a time and not a held-out ablation, and the
  held-out intervention is one
  hyperparameter. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-272 CLAIM-698 THEORY-022 CLAIM-tmp6rhuv — Proposed or new; the design this run reduces, the thesis it tests, the held mechanism and the claim filed from it -->

# CASE-tmpb4hg0: A modular-addition checkpoint study run on CPU: in 25 small attention-free networks trained on addition mod 37, the share of the logits' Fourier energy on the selection-rule triads at step 250 or 500 forecasts when held-out-weight-decay runs generalize better than Fourier energy, test accuracy, test loss and kernel alignment, and better than every random edge set of the same size, but foresaw none of the runs that failed to generalize

## What was run

[LEAD-172](../leads.d/LEAD-172.md) asks for [CASE-272](CASE-272.md)'s design, run: train small transformers on
modular addition, track the training kernel's eigenspaces and each layer's
coupling among Fourier modes over checkpoints, fit on early checkpoints,
predict later change under held-out interventions, and compare with a null
at equal edge budget. This is a reduced version, sized to an hour of CPU.

- **Model.** torch is not installed here, so the network was written in
  numpy with a hand-written backward pass, checked against finite
  differences. It is the attention-free reduction of a one-layer
  transformer on (a, b): z = E_a[a] + E_b[b] + b₁, h = ReLU(z),
  logits = hW₂ + b₂, with p = 37 and 128 hidden units. It has no attention,
  which is the study's largest departure from the design.
- **Training.** Full-batch AdamW, learning rate 0.01, weight decay applied
  as in AdamW, cross-entropy on a random fraction of the 1369 pairs.
- **Arms.** Fit set: weight decay 1.0, training fraction 0.4 (seeds 0–2),
  0.5 and 0.6 (seeds 0–5). Held-out intervention: weight decay 0.5
  (fraction 0.5 and 0.6, seeds 0–3) and 2.0 (fraction 0.5, seeds 0–1).
  A run stops 500 steps after test accuracy first reaches 0.95, or at
  15000 steps.
- **Persistence.** Every 50 steps each arm appends a row to its results
  file; weights and optimizer state are saved every 250 steps so a killed
  arm resumes.

## The measures

All are taken in the Fourier basis of ℤ/37, which the task supplies, not
the data.

- **Rule coupling in the logits (C2).** The class-centred logits f(a, b, c)
  over all p² inputs, transformed in all three indices. The task's own
  target, 1[c = a + b], has all its energy on the p − 1 triads
  (k, k, −k), k ≠ 0, the selection rule χ_k(a)χ_k(b) = χ_k(a + b). C2 is
  the share of the logits' energy on those triads. It is a global
  coupling, input modes to output modes through the whole network, not
  [CASE-272](CASE-272.md)'s per-layer Jacobian M_ℓ(x).
- **Rule coupling in the hidden layer (C1sel).** Of the hidden
  activations' energy on mixed modes χ_k(a)χ_l(b), k, l ≠ 0, the share on
  l = k. The first layer is additive in a and b, so all mixing is made by
  the ReLU.
- **The null at equal edge budget.** For each, 20 fixed random sets of
  p − 1 off-rule cells (hidden) or triads with nonzero class index
  (logits). The rule and the null have the same number of edges; only
  which edges differs.
- **Fourier energy.** The mean over hidden units of the top frequency's
  share of each embedding's spectrum: the sparsity measure of the progress
  measures literature ([THEORY-022](../theory.d/THEORY-022.md)).
- **Kernel.** The empirical tangent kernel over all p² inputs, summed over
  classes, in closed form (checked against explicit Jacobians). KA is the
  share of its top-37 eigenspace lying in the span of functions of a + b;
  K_rot, the rotation of that eigenspace between kernel checkpoints
  250 steps apart, is a proxy for the moving-basis term Ω of
  [QUESTION-217](../questions.d/QUESTION-217.md)'s note of 2026-11-15.
- **Training loss, test loss and test accuracy** at the same checkpoint.

## The prospective test

Every arm memorizes its training set by step 50 to 150, so the
memorization step does not separate arms. The early checkpoint is a fixed
step, 250 or 500, before every arm's generalization (the earliest T_gen is
850). Each measure at that step is a two-parameter linear forecast of
log10 T_gen, fitted on the 12 fit arms that generalized and scored on the 8
held-out-weight-decay arms that generalized. Every forecast has the same
two parameters, so complexity is matched.

| measure at step | 250: held-out RMSE | 500: held-out RMSE | P(C2 better), 500 |
|---|---|---|---|
| constant (fit mean) | 0.345 | 0.345 | |
| rule coupling, logits (C2) | **0.154** | **0.130** | |
| rule coupling, hidden (C1sel) | 0.176 | 0.195 | 0.95 |
| Fourier energy | 0.192 | 0.197 | 0.996 |
| kernel alignment (KA) | 0.186 | 0.350 | 0.998 |
| test accuracy | 0.276 | 0.247 | 0.9995 |
| test loss | 0.397 | 0.243 | 0.99 |
| kernel rotation (K_rot) | 0.639 | 0.511 | 0.9995 |
| training loss (log) | 2.514 | 3.974 | 1.0 |
| null, logits: median (best) of 20 | 0.345 (0.331) | 0.343 (0.290) | |
| null, hidden: median (best) of 20 | 0.273 (0.197) | 0.264 (0.188) | |

RMSE is in log10 steps, so 0.13 is a factor of about 1.35. "P(C2 better)"
is the share of 2000 paired bootstrap resamples of the 8 held-out arms in
which C2's error is lower. Within the fit arms (leave-one-out), C2, Fourier
energy, test accuracy and test loss are all within 0.05 to 0.10; the
difference shows only under the held-out intervention.

## What it shows

- **Rule coupling forecasts generalization timing under an unseen
  intervention.** At both checkpoints the logits' share on the
  selection-rule triads is the best forecast, and every random set of the
  same number of triads does no better than a constant. What carries the
  forecast is which couplings, not how many: the null that [QUESTION-275](../questions.d/QUESTION-275.md)
  asks for is met for this measure in this setting.
- **It beats Fourier energy, the progress-measure baseline, but not by
  much.** 0.13 against 0.20, on 8 held-out arms from 2 settings.
- **The hidden-layer coupling is weaker.** C1sel beats every null at step
  250, but 6 of 20 random sets beat it at step 500.
- **The kernel measures carry little.** The top kernel eigenspace stays at
  chance alignment with functions of a + b (0.028 to 0.033, chance 1/37)
  throughout, even after generalization; its small early variation
  forecasts at step 250 and not at 500. The eigenspace rotation forecasts
  nothing. This trace kernel is a poor witness of the circuit here.
- **Rule coupling does not rise ahead of generalization in the half-way
  sense.** Where it reaches half its maximum (training fraction 0.6), it
  does so 0 to 150 steps after test accuracy reaches 0.95. Its early
  level, not an early crossing, is what forecasts.
- **No measure foresaw failure.** Five arms never reached 0.95 in 15000
  steps: training fraction 0.4 and weight decay 2.0. Every forecast put
  them inside the observed range. Under weight decay 2.0 the rule coupling
  was as high early as in the fast arms, and test accuracy rose to 0.64 to
  0.75 by step 2000 and crept to 0.79 to 0.86 by step 15000. The forecast was right that much of
  the circuit forms early and wrong that it completes.

## Its limits

- **Not a transformer.** No attention, one hidden layer, so "each layer's
  coupling" is two measures, not a stack.
- **One task, one modulus, one width.** The Fourier basis is given by ℤ/37.
  As [CASE-272](CASE-272.md) says, a positive result here does not show that modes
  can be found where no symmetry supplies them.
- **The target is a time, not an intervention response.** The design also
  asks for held-out Fourier ablations; none was run.
- **One intervention family.** Weight decay, at two held-out values, of
  which only one (0.5) yielded scorable arms.
- **The measures see the network's outputs on test inputs.** C2, like test
  loss and test accuracy, is computed over all p² pairs; Fourier energy and
  the kernel alignment are not outcome measures in that sense. C2 beats the
  test-set baselines, so this is not the whole of its advantage, but it is
  not a weights-only forecast.
- **Small.** 25 arms, a two-parameter forecast, one analyst, no
  preregistration beyond the scripts committed before the analysis.

## Where it sits

It is the first executed run of [CASE-272](CASE-272.md) and evidence on [CLAIM-698](../claims.d/CLAIM-698.md)'s
criterion: a description in modes the task justifies, and the couplings
its group selects, forecasts a training response under an unseen
intervention better than feature-level (Fourier energy) and outcome-level
accounts fitted on the same arms, and better than couplings chosen at
random. It is not the matched comparison against circuit-attribution or
parameter-overlap accounts that [CLAIM-698](../claims.d/CLAIM-698.md)'s defeater names, and it
does not test [QUESTION-275](../questions.d/QUESTION-275.md)'s feature-allocation model. What it finds is
filed as [CLAIM-tmp6rhuv](../claims.d/CLAIM-tmp6rhuv.md).

Rerun: scratch/studies/lead-172/README.md.
