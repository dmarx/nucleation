---
status: Proposed
title: 'Function-preserving rescaling of a pretrained diagonal linear network before fine-tuning, run on two main tasks'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as the check of the inference
    that run draws from Lippl and Lindsey. Code, tests and results are
    committed under scratch/studies/lead-007/.
standing: documented
kind: executed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
draws_on:
- THEORY-tmpw69kb
bears_on:
- QUESTION-495
illustrates:
- CLAIM-tmp2tjpt
summary: >-
  Lippl and Lindsey's pretraining and fine-tuning of a two-layer diagonal
  linear network, with one change: before fine-tuning, the pretrained
  network P₁ is replaced by P_c, its first layer times c and its auxiliary
  readout divided by c, which computes the same function to 2·10⁻¹⁶. Over
  40 seeds, readout-only training from P_c reaches the same solution for
  every c, while full fine-tuning does not: on a main task using 2 of the
  10 pretrained dimensions, c = 0.3 beat c = 2 in 29 of 40 seeds (sign
  test p = 0.006); on one using all 10 with varied coefficients, c = 2 beat
  c = 0.3 in 40 of 40. Halving the step size moved errors by far less
  than these gaps. One solvable model, Gaussian inputs, numpy on CPU. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp7n00e THEORY-tmpw69kb CLAIM-tmp2k67n — Proposed; the claim this run grounds, the reading whose setup it uses, the verdict it illustrates, and the identity it is read with -->

# CASE-tmpjn7jc: Function-preserving rescaling of a pretrained diagonal linear network before fine-tuning, run on two main tasks

## What was done

On 2026-11-23, with numpy on CPU (scratch/studies/lead-007/: README.md,
diag_rescale.py, four tests, analyze.py, check_lr.py, results/).

- **Network and pretraining.** β = v₊∘w₊ − v₋∘w₋ in D = 100 dimensions,
  all weights started at 10⁻³, trained by full-batch gradient descent on
  80 samples (Gaussian inputs) of an auxiliary teacher with ten unit
  coefficients, to squared error on β below 6·10⁻⁵.
- **Rescaling.** P_c: w₊, w₋ times c and v₊, v₋ divided by c, for c in
  {2, 1, 0.3, 0.1}. The function, β, is the same as P₁'s to 2·10⁻¹⁶.
- **Fine-tuning,** as in Lippl and Lindsey's §3.3 ([THEORY-tmpw69kb](../theory.d/THEORY-tmpw69kb.md)):
  pathway weights set to their sum, readout reset to γ = 0.01, then
  gradient descent to training loss below 10⁻⁹, either on all weights
  (full) or on the readout alone (probe).
- **Main tasks.** Nested: 2 of the 10 pretrained dimensions, coefficient
  1, 8 samples. Dense: all 10, magnitudes 0.5 to 1.5 with random signs, 14
  samples. Error is ‖β − β_main‖².
- 40 seeds, each with its own teacher and data, and a step-size check
  (three seeds, step halved).

## What it found

| main task | c = 2 | c = 1 | c = 0.3 | c = 0.1 | probe, any c |
|---|---|---|---|---|---|
| nested, mean error | 0.384 | 0.376 | 0.320 | 0.485 | 0.384 |
| dense, mean error | 0.035 | 0.124 | 1.65 | 3.90 | 0.029 |

- **Probe.** The solution is the same for every c, to machine precision
  in this run.
- **Full fine-tuning, nested task.** c = 0.3 beat c = 2 in 29 of 40
  paired seeds (two-sided sign test p = 0.006) and c = 1 in 28 (p =
  0.017); medians 0.147 against 0.266 and 0.272. Shrinking further
  (c = 0.1) hurt.
- **Full fine-tuning, dense task.** Larger c won in every seed: c = 2 beat
  c = 1 and c = 0.3 in 40 of 40.
- **Step size.** Halving it changed errors by under 6% in eleven of twelve
  rechecked runs and by 27% in the worst, against gaps of tenfold between
  c = 0.3 and c = 2 on the dense task.

## What it shows, and what it cannot

That, in this model, function-equivalent pretrained networks learn the
same thing under readout-only training and different things under full
fine-tuning, and that the better one depends on the declared main task:
shrinking helps where the main task uses a sparse subset of the
pretrained features, as Lippl and Lindsey's nested regime predicts, and
hurts where it uses all of them. It grounds [CLAIM-tmp7n00e](../claims.d/CLAIM-tmp7n00e.md).

It cannot say whether the pair is two learners or one learner under two
procedures. In the run, the step-size rule is set from the weights'
scale, so it too differs with c; the converged solutions approximate
gradient flow, as the step-size check shows, and the identity of
[CLAIM-tmp2k67n](../claims.d/CLAIM-tmp2k67n.md) holds in either case. Nothing here is a deep network,
cross-entropy, or pretraining of varying length.
