---
number: 1275
status: Active
formerly:
- THEORY-tmpzcsl4
title: "In the toy model of superposition, at the paper's one SGD setting, the Bayesian counterparts of the observed training chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ have critical sample sizes that rise in the order training meets it at the point estimates of the learning coefficients, though not across their spread; SGD was not seen to take the posterior's main transition, 5 → 6, and trained on 1,000 samples it ends in a phase that the posterior at n = 1,000, dominated by the 6-gon, does not favour"
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed (kind 3) and promoted at the status review's ruling (the owner
    delegated these rulings), the twenty-ninth status review (ADR-065). Old
    title, verbatim: "In the toy model of superposition, SGD's transitions have Bayesian counterparts whose critical sample sizes rise in the order training meets them, yet SGD was not seen to take the posterior's main transition and ends in a phase the posterior has left at the training sample size". Old promote_when, verbatim: "In the same toy model, the critical sample sizes of the antecedents of each observed chain of training transitions confirmed by posterior sampling (phase occupancy across n, as for 5 → 6), not only by the free energy formula with estimated learning coefficients; and SGD trained at sample sizes on both sides of n ≈ 600, over a sweep of learning rates, batch sizes and initialisations, showing whether the 6-gon is reached. What would refute the second half: SGD at n = 1000 reaching the 6-gon routinely at some ordinary setting. What would refute the first: a chain whose antecedents' critical sizes fall while training proceeds. Runs at the paper's single setting cannot settle it."
    The rising order was computed for one chain of Eq. 10's four, holds at
    the λ̂ point estimates and fails in 36 of 81 combinations at ±1 sd; and
    "a phase the posterior has left" misdescribes the 5⁺-gon, which the
    posterior never favours. The record's computation was re-run by a
    second checker from the model, with controls, in
    scratch/formal/tms_critical_sizes_check.py, and by the coordinator,
    which meets ADR-065's point 5; NOTE-1462 v2 reread the paper and is
    Read. The old condition's demands, posterior sampling of the
    antecedents and an SGD sweep across rates, batch sizes and
    initialisations, are independent tests and move to QUESTION-363 as a
    dated note. Status Proposed → Active; promote_when removed on promotion.
tags:
- learning-theory
- model-comparison
- loss-landscapes
date: '2026-10-31'
source:
- LIT-1894
summary: >-
  Chen, Lau, Mendel, Wei and Murfet (2023), [LIT-1894](../literature.d/LIT-1894.md), read in
  [NOTE-1462](../notes.d/NOTE-1462.md). Their Bayesian antecedent hypothesis is one-way: training's
  transitions have Bayesian counterparts. From their numbers the
  antecedents of the chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ fall at n ≈ 190, 370 and
  1,600–2,500, rising with training. But the posterior's transition 5 → 6
  at n ≈ 600 was not seen in training, and SGD on 1000 samples ends at the 5-gon, a 4-gon variant or the 5⁺-gon,
  none of which the posterior at n = 1000 favours; it favours the 6-gon. The
  rising order holds at the point estimates, not across the estimates'
  spread. One model, one SGD setting, estimated learning coefficients; the
  computation was re-run by a second checker on 2026-11-06
  (scratch/formal/tms_critical_sizes_check.py).
---

# THEORY-1275: In the toy model of superposition, at the paper's one SGD setting, the Bayesian counterparts of the observed training chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ have critical sample sizes that rise in the order training meets it at the point estimates of the learning coefficients, though not across their spread; SGD was not seen to take the posterior's main transition, 5 → 6, and trained on 1,000 samples it ends in a phase that the posterior at n = 1,000, dominated by the 6-gon, does not favour

## Source

Chen, Lau, Mendel, Wei and Murfet (2023), [LIT-1894](../literature.d/LIT-1894.md), §§4–5 and
Appendices C, D, F and K of arXiv 2310.06301v1; read in [NOTE-1462](../notes.d/NOTE-1462.md).

## What was actually shown

**The setting.** TMS with r = 2 hidden and c = 6 input dimensions in the
high-sparsity limit ([LIT-323](../literature.d/LIT-323.md)). Phases are regions dominated by k-gon
critical points. The local free energy is F_n(W_α) ≈ nL_α + λ_α log n + c_α,
and a Bayesian transition α → β happens where the two cross (Eq. 12).

**The posterior.** 5-gon (λ = 7, L = 0.06874) to 6-gon (λ = 8.5,
L = 0.04819) at n_cr ≈ 601 by the formula, between 600 and 700 by NUTS
sampling (Fig. 2). I recomputed both losses from the model by quadrature
and n_cr from Eq. 12.

**Training.** SGD on n = 1000 samples (batch 20, rate 0.005, 4500 epochs,
from a perturbed 4-gon, 30 seeds; and 400 runs from posterior samples at
n = 100) plateaus at k-gon critical points and makes the transitions of
Eq. 10, among them 4⁺⁺⁻ → 4⁺ → 5 → 5⁺. "the Bayesian phase transition
5 → 6 has not been observed as a dynamical transition" (§5.1). The eight
transition runs of the 30 seeds end at the 5-gon (four) or at 4-gon
variants (four) (App. B).

**The hypothesis and its scope.** "The dynamical transitions α → β
encountered in neural network training have Bayesian antecedents" (§5.1).
The paper adds: "There is no necessary relation between these two kinds
of transitions", and explains the missing 5 → 6 by distance or barriers.
It does not claim that every Bayesian transition occurs in training, or
that the two orders coincide. App. C.4 gives the condition under which
they could: with constants ignored, successive transitions occur at
increasing n only if the slope ΔL/Δλ rises along the chain.

**My computation from their numbers.** With Table C.2's constants, Table
K.1's λ̂ and the losses above, the antecedents fall at n ≈ 190
(4⁺⁺⁻ → 4⁺), 370 (4⁺ → 5) and 2,500 (5 → 5⁺; 1,600 with the theoretical
λ). The slopes, −0.029, −0.018, −0.003, rise. Along this chain the order in
training time is the order in sample size. At n = 1000 the free energies
are about 113 for the 6-gon, 121 for the 5-gon and 124 for the 5⁺-gon:
the posterior favours the 6-gon, and the 6-gon beats the 5⁺-gon for every
n above about 202, so 5⁺ is never the posterior's phase. Re-run on
2026-11-06 by a second checker from the model, with controls
(scratch/formal/tms_critical_sizes_check.py; NOTE-1462 v2): all numbers
reproduced. At ±1 sd of each λ̂ the order fails in 36 of 81 combinations,
mostly the first two steps.

**What could have failed.** The antecedents' critical sizes could have
fallen along the chain, and SGD could have reached the 6-gon. Neither
happened in this model at this setting.

## What this does not say

- **That the order is robust.** It holds at the point estimates; at ±1 sd
  of Table K.1 it fails in 36 of 81 combinations.
- **That training time maps onto sample size.** A monotone map along one
  chain would still have to send the end of training at n = 1000 to a
  sample size above 1,600 for the 5⁺ step, and could not send it to the
  6-gon that the posterior at 1000 favours. No single t ↦ n map makes
  training's endpoint the posterior's state at its own n.
- **That the 6-gon is inaccessible.** One learning rate, one batch size
  and chosen initialisations; "it may occur, just with low probability per
  SGD step" (§5.1). Inaccessible and not reached in 4500 epochs are not
  yet told apart.
- **That the critical sizes are exact.** The free energy formula is
  asymptotic and used at n of a few hundred, the constants are heuristic
  (App. C.1), and the λ̂ for 4-gon variants have standard deviations near
  1 (Table K.1). The lowest-n antecedents are inconclusive by the authors'
  account (App. D).
- **That the pattern generalises.** One toy model with exact learning
  coefficients for a few critical points.
