---
number: 253
status: Proposed
formerly:
- THEORY-tmp99x1h
promote_when: >-
  An analysis of sign descent, or of Adam at small β, on a sum of
  frequency-weighted quadratic losses whose eigendirections are not
  aligned with the coordinates. It would need to derive the delayed onset
  of each weaker skill, and the ratio t₂/t₁ → 2, that the paper shows
  only in simulation. Or a trained network on independent skills of
  unequal frequency whose onsets go from simultaneous to sequential when
  only the optimizer is changed from SGD to sign descent. It is refuted by
  a case in which orthogonal skills under plain gradient descent start one
  after another without small-initialization plateaus, or by sign descent
  on a rotated quadratic that learns all directions together. Further fits
  of the Resource ODE cannot settle it, since that model was fitted to
  the behaviour it would be confirming.
title: 'In a model of independent skills with linear task vectors, sequential onset of acquisition comes from the optimizer: under gradient descent orthogonal skills are learned together at rates set by their frequencies, while under sign descent they compete for coordinate signs, so each starts as the previous finishes'
version: 1
tags:
- learning-theory
date: '2026-10-14'
source:
- LIT-951
summary: >-
  Liu, Liu, Michaud, Gore and Tegmark (2025), [LIT-951](../literature.d/LIT-951.md), read in
  [NOTE-794](../notes.d/NOTE-794.md). The Geometry model has loss Σ p_i L((θ − θ₀)·t_i) with
  orthogonal t_i. In it, SGD learns task 2 in time ∝ 1/p₂, while SignGD
  holds task 2 back until task 1 is done and then takes a constant extra
  delay (t₂/t₁ → 2). A rotated quadratic shows the same split (Fig. 12).
  The order is frequency order either way. The evidence is simulation
  and one fitted ODE. Sequential onset caused by dependency between
  skills is a separate experiment, not part of this account.
answers:
- QUESTION-039
supports:
- CLAIM-tmpw4w7a
---
<!-- inactive-ok-file: THEORY-229 THEORY-186 THEORY-187 THEORY-212 THEORY-039 — Proposed; accounts this one is set beside, none of them rested on -->

# THEORY-253: In a model of independent skills with linear task vectors, sequential onset of acquisition comes from the optimizer: under gradient descent orthogonal skills are learned together at rates set by their frequencies, while under sign descent they compete for coordinate signs, so each starts as the previous finishes

## Source

Liu, Liu, Michaud, Gore and Tegmark (2025), [LIT-951](../literature.d/LIT-951.md), read in
[NOTE-794](../notes.d/NOTE-794.md). The account rests on §§2.2–2.6, Figs. 4, 5, 7 and 12, and
Eqs. 1–3 and 6–9.

## What was actually shown

**The model.** The Geometry model has loss ℓ = Σ_i p_i L(s_i), with skill
level s_i = (θ − θ₀)·t_i and L(s) = (1 − s)² or −log σ(s). The t_i are
random and orthogonalised when n_task ≤ n_dim, and p_i ∝ i^(−α).

**Two orthogonal tasks (Fig. 4).** The setting is n_dim = 1000, batch
128, and p₁ + p₂ = 1, with SGD, SignGD and Adam.
- Under SGD, task 2's convergence time grows roughly as 1/p₂, as the
  decoupled linear dynamics require.
- Under SignGD, task 2 makes rapid progress only once task 1 is done,
  and t₂/t₁ saturates at 2 however small p₂ is.
- Adam lies between, sub-linear in p₁/p₂.

The mechanism offered is sign(g₁ + g₂) ≈ sign(g₁) when ‖g₁‖ ≫ ‖g₂‖. The
number of coordinates whose update sign agrees with each task's gradient
falls for task 1 as it rises for task 2 (Fig. 5).

**A rotated quadratic (Fig. 12).** Take ℓ = x₁² + 0.1x₂² + 0.01x₃² + 0.001x₄²
with x = Rθ.
- SGD gives the same dynamics for R = I and for a Hadamard R.
- SignGD learns all four together when R = I, and in Domino sequence
  when R = H₄.
- So the sequence needs the loss's eigendirections to be misaligned with
  the coordinates the optimizer acts on.

**Many tasks (Fig. 5).** Under SignGD skills are learned in frequency
order. The clean Domino form holds "only for large α and the first few
skills".

**The reduced models.**
- **Resource model (Eq. 1).** du_i/dt = −η_eff p_i u_i/(Σ_j p_j u_j + N₀),
  with one fitted constant N₀. It matches the SignGD curves (Fig. 7). It
  conserves u_i^(1/p_i) = C exactly.
- **Domino model.** Its limit N₀ → 0, p₁ ≫ p₂ ≫ … gives strict sequence,
  with t_n ∝ n, against t_n ∝ n^α for SGD.

**What could have come out otherwise.**
- SignGD could have shown the same 1/p₂ scaling as SGD.
- The rotated quadratic could have shown a sequence under both
  optimizers, or under neither.

## What this does not say

- **Not proved.** The Domino effect under SignGD is a simulation result.
  The Resource model is fitted to it, not derived from the optimizer, and
  the Domino model is a limit of that fit.
- **Not about the order.** Frequency sets the order under every
  optimizer tested. The optimizer changes whether onsets overlap and how
  the n-th onset scales.
- **Not that real networks owe their stages to Adam.** The real-network
  evidence is small. Two sparse parities with Adam show the effect
  (Fig. 2), and one two-variable regression shows t₂ ≳ 2t₁. Gradient
  descent was not run on these for contrast.
- **Not the only cause of sequential onset.** In the same paper, a parity
  that is the XOR of two others waits for them under Adam (Fig. 16), and
  an independent parity of the same order waits longer. That is
  dependency, a different cause, and this account does not hold it.
- **Not an instruction.** The paper's reweighting, SignGD-against-grokking
  and optimizer comparisons are machine-learning practice and are left to
  the anthology.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md).** It answers in part, and it adds to the question's
  list (data statistics, initial scale, depth, architecture) a factor the
  list lacks: the optimizer. In this model the optimizer decides whether
  acquisitions arrive together or one at a time. Read with the dependency
  experiment, the paper gives at least two kinds of event behind
  "sequential acquisition".
- **[THEORY-229](THEORY-229.md), [THEORY-186](THEORY-186.md) and [THEORY-187](THEORY-187.md).** These get one-at-a-time
  acquisition under gradient flow from small initialization. Each mode
  waits near an unstable fixed point for a time set by its eigenvalue
  and the log of the initial scale. The Geometry model has no such fixed
  point, and under gradient descent it shows no sequence. So the two
  mechanisms make opposite predictions under the same intervention:
  - replace sign descent with gradient descent, and the Domino sequence
    disappears while [THEORY-229](THEORY-229.md)'s steps remain;
  - start from order-one scale, and [THEORY-229](THEORY-229.md)'s steps shrink while the
    Domino sequence does not depend on scale.
- **[THEORY-086](THEORY-086.md).** Under SGD the Geometry model is the kernel picture
  there: every direction is fitted at once, at a rate set by its weight.
- **[THEORY-212](THEORY-212.md).** There a conserved quantity of the initialization
  decides between staged and simultaneous learning. Here the optimizer
  does. Neither leaves "staged or not" to the data alone.
- **[THEORY-039](THEORY-039.md).** Its caution that transitions differ in kind is borne
  out. Optimizer competition, dependency and small-initialization escape
  are three different routes to the same-looking staircase.
