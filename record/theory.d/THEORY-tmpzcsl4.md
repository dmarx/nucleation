---
status: Proposed
promote_when: >-
  In the same toy model, the critical sample sizes of the antecedents of
  each observed chain of training transitions confirmed by posterior
  sampling (phase occupancy across n, as for 5 → 6), not only by the free
  energy formula with estimated learning coefficients; and SGD trained at
  sample sizes on both sides of n ≈ 600, over a sweep of learning rates,
  batch sizes and initialisations, showing whether the 6-gon is reached.
  What would refute the second half: SGD at n = 1000 reaching the 6-gon
  routinely at some ordinary setting. What would refute the first: a chain
  whose antecedents' critical sizes fall while training proceeds. Runs at
  the paper's single setting cannot settle it.
title: "In the toy model of superposition, SGD's transitions have Bayesian counterparts whose critical sample sizes rise in the order training meets them, yet SGD was not seen to take the posterior's main transition and ends in a phase the posterior has left at the training sample size"
version: 1
tags:
- learning-theory
- model-comparison
- loss-landscapes
date: '2026-10-31'
source:
- LIT-tmpogi33
summary: >-
  Chen, Lau, Mendel, Wei and Murfet (2023), [LIT-tmpogi33](../literature.d/LIT-tmpogi33.md), read in
  [NOTE-tmp1z319](../notes.d/NOTE-tmp1z319.md). Their Bayesian antecedent hypothesis is one-way: training's
  transitions have Bayesian counterparts. From their numbers the
  antecedents of the chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ fall at n ≈ 190, 370 and
  1,600–2,500, rising with training. But the posterior's transition 5 → 6
  at n ≈ 600 was not seen in training, and SGD on 1000 samples ends at the
  5- or 5⁺-gon while the posterior at n = 1000 favours the 6-gon. Proposed:
  one model, one SGD setting, estimated learning coefficients.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l QUESTION-039 — Open; the question this bears on, and the question it refines -->

# THEORY-tmpzcsl4: In the toy model of superposition, SGD's transitions have Bayesian counterparts whose critical sample sizes rise in the order training meets them, yet SGD was not seen to take the posterior's main transition and ends in a phase the posterior has left at the training sample size

## Source

Chen, Lau, Mendel, Wei and Murfet (2023), [LIT-tmpogi33](../literature.d/LIT-tmpogi33.md), §§4–5 and
Appendices C, D, F and K of arXiv 2310.06301v1; read in [NOTE-tmp1z319](../notes.d/NOTE-tmp1z319.md).

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
5 → 6 has not been observed as a dynamical transition" (§5.1).

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
the posterior favours the 6-gon, and of the two phases SGD ends in it
prefers the one SGD left.

**What could have failed.** The antecedents' critical sizes could have
fallen along the chain, and SGD could have reached the 6-gon. Neither
happened in this model at this setting.

## What this does not say

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
