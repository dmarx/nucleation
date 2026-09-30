---
number: 26
status: Proposed
formerly:
- THEORY-tmp4trgp
promote_when: >-
  A derivation that states the conditions under which the per-step
  nostalgia I[s_t;x_t] − I[s_t;x_{t+1}] is a nonnegative lower bound on
  dissipation. NOTE-295 found two unstated conditions: a Markov drive, and
  p_eq(·|x) stationary under the kernel. The derivation should either prove
  the bound under them or show it fails without them. A worked physical
  system in which measured dissipation tracks nonpredictive information
  would support the claim. An example with a fixed-kernel, feedback-free,
  Markov-driven system that dissipates less than its nostalgia would
  refute it. Results on systems with feedback (LIT-041) bear on the scope
  of the claim, not on its truth.
title: 'For a system driven without feedback, the work dissipated equals the memory that fails to predict the drive, so only nonpredictive memory is wasteful; once actions feed back, prediction is no longer what efficiency requires'
version: 1
tags:
- information-theory
- natural-sciences
- learning-theory
- agency
date: '2026-09-30'
source:
- LIT-327
- LIT-041
summary: >-
  Still, Sivak, Bell & Crooks (2012), [LIT-327](../literature.d/LIT-327.md): β⟨W_diss⟩ for the step x_t →
  x_{t+1} equals I[s_t;x_t] − I[s_t;x_{t+1}] (Eq. 14, an identity). The
  summed nostalgia lower-bounds dissipation and adds to Landauer's bound
  (Eq. 21). Fiderer et al. ([LIT-041](../literature.d/LIT-041.md)) show that with feedback, predictive,
  max-entropy-action and efficient agents can be disjoint. The claim is an
  ensemble average, not a per-operation floor. It needs a Markov drive to be
  nonnegative, and the prediction-is-necessary slogan fails under feedback.
---

# THEORY-026: For a system driven without feedback, the work dissipated equals the memory that fails to predict the drive, so only nonpredictive memory is wasteful; once actions feed back, prediction is no longer what efficiency requires

## Source

- Still, Sivak, Bell & Crooks (2012), [LIT-327](../literature.d/LIT-327.md), Eqs. (14)–(21) and footnote [24], as read in [NOTE-295](../notes.d/NOTE-295.md).
- Fiderer et al. (2025), [LIT-041](../literature.d/LIT-041.md), Thms 4–5 (Thms 9–10 in the supplement) and Lemma 10, as read in [NOTE-032](../notes.d/NOTE-032.md).

## What was actually shown

**The identity ([LIT-327](../literature.d/LIT-327.md)).** A system with state s_t is driven by a signal x_t through a fixed Markov kernel. Work is done only when the signal changes, and there is no feedback from system to signal. Then the average dissipated work in the step x_t → x_{t+1} is k_BT times I[s_t;x_t] − I[s_t;x_{t+1}] (Eq. 14). [NOTE-295](../notes.d/NOTE-295.md) re-derived this from footnote [24]; given the definitions it is an identity. Summed over a protocol, the "nostalgia" lower-bounds dissipation and excess work (Eq. 18). The heat released is then at least k_BT·(I_e + I_mem − I_pred) (Eq. 21). Here I_e is the Landauer term for entropy removed. The account prices only the part of memory that does not carry over to the next input. Predictive memory costs nothing in it.

**The feedback case ([LIT-041](../literature.d/LIT-041.md)).** Fiderer et al. model agent and environment as coupled hidden-Markov channels. They bound work per round by ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t. Without feedback (a unifilar product environment), the efficient agents are exactly those that are maximally predictive and randomise-and-forget their actions (Thm 4). This is Boyd, Mandal and Crutchfield's tape-setting principle, "randomize-and-forget your actions, predict your percepts", extended beyond stationarity, and its prediction half is the [LIT-327](../literature.d/LIT-327.md) slogan. With feedback, one binary memoryless channel makes the predictive, max-entropy-action and efficient agents three nonempty, pairwise-disjoint sets (Thm 5). Every predictive agent there extracts at most zero. [NOTE-032](../notes.d/NOTE-032.md) checked the numbers: the optimum is ≈ 0.272 bits per round, and uniform-random agents extract ≈ 0.189.

Read together, the two papers bound the claim. Predictive memory is what thermodynamic efficiency asks for only when the system does not act on its source. That reading is the record's. [LIT-041](../literature.d/LIT-041.md) presents itself as breaking the tape-setting principle, and [NOTE-295](../notes.d/NOTE-295.md) says to read the two as baseline and break.

## What this does not say

- **That the per-step nostalgia is always a nonnegative cost.** [NOTE-295](../notes.d/NOTE-295.md) finds that nonnegativity needs a Markov drive, which the paper does not state. Under a non-Markov drive, a state that remembers x_{t−1} can predict x_{t+1} better than it tracks x_t, and then the step's "dissipation" as defined is negative. The relaxation step ⟨ΔF^relax_neq⟩ ≤ 0 also needs an unstated stationarity condition.
- **Anything per operation.** Every quantity is an average over paths and protocols. The unit is nats, not bits, and neither paper states a "k_BT ln 2 per bit" cost.
- **Anything about learning systems.** Both papers hold the kernel fixed. [LIT-327](../literature.d/LIT-327.md)'s Discussion raises adaptation but proves nothing about it. [LIT-041](../literature.d/LIT-041.md)'s agent has no learning. Its "prediction and energy efficiency may be at odds in active learning systems" is a hedged extrapolation ([NOTE-032](../notes.d/NOTE-032.md), C14).
- **That efficiency under feedback is a trade-off between prediction and forgetting.** In the only proved example the efficient agent is memoryless ([NOTE-032](../notes.d/NOTE-032.md), C13). No interior optimum is exhibited.
- **Anything about real hardware.** Neither paper models a device.

## Connections

- [LIT-338](../literature.d/LIT-338.md) (IB) is the ancestor, through Still 2009, of the "maximise predictive power at fixed memory" objective that [LIT-327](../literature.d/LIT-327.md)'s Discussion recommends.
- [LIT-308](../literature.d/LIT-308.md) bounds information *acquired* by entropy production, and [LIT-327](../literature.d/LIT-327.md) bounds information *kept but useless* by dissipation. The Landauer term they share is the subject of [THEORY-030](THEORY-030.md).
