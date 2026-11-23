---
status: Active
title: 'In the toy model of superposition trained by plain SGD on squared error, a feature whose output is silenced for every input and whose input excites no output gets an exactly zero gradient from every sample, so no learning rate, batch size or training time revives it; at the 5-gon the dropped feature is such a feature for as long as the other biases stay non-positive'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): the proof is re-derived step by step (the step to z_i
    <= 0 holds for either sign of W_m.W_i since mu is in [0, 1]; Wg = 0
    follows by convexity in mu), and the frozen-column test reproduces.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a configuration (W, b) and a feature i with
  W_k·W_i + b_i ≤ 0 for every k, and b_j ≤ 0 and W_i·W_j + b_j ≤ 0 for
  every j ≠ i,
  and a sample μe_m with μ in [0, 1], whose squared-error gradient with
  respect to W_i or b_i is not zero.
tags:
- learning-theory
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-363
grounds:
- CASE-tmpgqbyq
complements:
- CLAIM-tmp9zqvq
summary: >-
  Derived for [LEAD-175](../leads.d/LEAD-175.md) and checked in its study ([CASE-tmpgqbyq](../cases.d/CASE-tmpgqbyq.md)). It is
  the mechanism behind the missing 5 → 6 in Chen et al.'s toy model
  ([THEORY-1275](../theory.d/THEORY-1275.md)): at the 5-gon the sixth column is zero and its bias
  negative, so the sixth output is zero for every input and the sixth
  input reaches no output. SGD's noise, a sum of per-sample gradients, is
  then zero in those coordinates, and they stay where they are. The
  posterior moves them through the prior. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1353 — Proposed; Dong's test of a temperature, cited as the neighbouring point -->

# CLAIM-tmpg8m7a: In the toy model of superposition trained by plain SGD on squared error, a feature whose output is silenced for every input and whose input excites no output gets an exactly zero gradient from every sample, so no learning rate, batch size or training time revives it; at the 5-gon the dropped feature is such a feature for as long as the other biases stay non-positive

## The claim

**Setting.** f(x) = ReLU(WᵀWx + b) with W of size 2 × 6, trained on samples
x = μe_m (μ in [0, 1]) with per-sample loss ‖x − f(x)‖², by plain SGD:
each step subtracts a rate times the mean of per-sample gradients.

**Statement.** Suppose feature i satisfies both of:

- **(a) its output is silenced:** W_k·W_i + b_i ≤ 0 for every k;
- **(b) its input excites nothing:** b_j ≤ 0 and W_i·W_j + b_j ≤ 0 for
  every j ≠ i.

Then every per-sample gradient with respect to W_i and b_i is zero.

**Proof.** Write z = WᵀWx + b and g = ∂loss/∂z, so g_j = 2(ReLU(z_j) − x_j)
on z_j > 0 and 0 otherwise. For the sample μe_m, z_i = μW_m·W_i + b_i ≤ 0
by (a), because μ ≤ 1 and b_i ≤ −‖W_i‖² ≤ 0 (take k = i). Hence g_i = 0 for every sample, and
∂/∂b_i = g_i = 0. The gradient in W_i is W(μe_m)g_i + μ[m = i]Wg. Its
first term vanishes with g_i. Its second arises only from samples of
feature i. For these, z_j = μW_i·W_j + b_j ≤ 0 for j ≠ i by (b), so
g_j = 0, and g_i = 0 as before; so Wg = 0. ∎

The gradient in W is ugᵀ + (Wg)xᵀ with u = Wx, which is where the two
terms come from.

**At the 5-gon.** W_6 = 0, so (a) and (b) reduce to b_6 ≤ 0 and to
b_j ≤ 0 for j ≠ 6. Since W_6 and b_6 receive no gradient, they keep
their values. The conditions then hold for as long as the five other
biases stay non-positive, and those biases are −0.28 at the 5-gon. The
6-gon needs ‖W_6‖ ≈ 1.32, so no SGD run inside that set reaches it,
whatever its rate, batch size or length.

**Checked.** In scratch/studies/lead-175/:

- the test `test_dead_column_of_the_5gon_is_frozen_under_sgd` runs 3,000
  steps from the perturbed 5-gon at three settings, up to rate 0.1 at
  batch 1, and finds the column bit-for-bit unchanged;
- in the sweep, every one of 288 5-gon starts ended at the 5-gon.

## What it does not say

- **That the 6-gon is closed to SGD from every start.** A feature still
  alive, such as the positive-bias column of the 5⁺-gon, is not covered.
  That route is [CLAIM-tmp9zqvq](CLAIM-tmp9zqvq.md)'s, and it is empirical.
- **Anything about other trainers.** Weight decay, injected Langevin noise
  and momentum with a nonzero initial velocity in those coordinates are
  not plain SGD. The first two act on the frozen coordinates directly.
- **That the noise is a temperature.** It says where SGD's noise is not a
  temperature in Dong's sense ([THEORY-1353](../theory.d/THEORY-1353.md)): it vanishes identically on a
  set where the posterior's does not.
