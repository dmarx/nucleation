---
number: 26
status: Active
formerly:
- THEORY-tmp4trgp
title: "For a system driven without feedback through fixed kernels, the average work dissipated at each switch of the drive equals the memory that fails to predict the next input; that is nonnegative when the drive is Markov and, summed, bounds the protocol's dissipation from below when each kernel keeps its equilibrium stationary, so there only nonpredictive memory is wasteful; with feedback, in one binary channel no predictive agent is efficient"
version: 4
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Connections names the stochastic-thermodynamics review LIT-523 (read in
    NOTE-420) as the framework in which the protocol-level nonnegativity of
    this account's dissipation is a reported result, and the
    fluctuation-theorem account THEORY-431 as background. Neither is a
    source, as NOTE-420 recommends.
- version: 3
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-026 (batch 045, ADR-047 v2). The dated note below derives the
    per-switch identity, proves the nostalgia nonnegative under a Markov
    drive and the summed bound when each kernel keeps its equilibrium
    stationary, and recomputes the feedback channel. "Equals" is held to one
    switch, the two conditions enter the title, and the feedback clause is
    held to the one proved channel. The rest of the promote_when moves to
    QUESTION-191.
- version: 4
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 072, ADR-047 v4) filed THEORY-817,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
tags:
- information-theory
- thermodynamics
- natural-sciences
- learning-theory
- agency
date: '2026-09-30'
source:
- LIT-327
- LIT-041
summary: >-
  Still, Sivak, Bell & Crooks (2012), [LIT-327](../literature.d/LIT-327.md): β⟨W_diss⟩ for the switch
  x_t → x_{t+1} equals I[s_t;x_t] − I[s_t;x_{t+1}] (Eq. 14, an identity).
  Under a Markov drive this nostalgia is nonnegative, and summed it lower-
  bounds dissipation when each kernel keeps its equilibrium stationary;
  both conditions are unstated in the paper and derived here. Fiderer et
  al. ([LIT-041](../literature.d/LIT-041.md)) show that with feedback, in one binary channel,
  predictive, max-entropy-action and efficient agents are disjoint. The
  claim is an ensemble average, not a per-operation floor. Whether the
  bound fails without the two conditions is [QUESTION-191](../questions.d/QUESTION-191.md).
extended_by:
- THEORY-817
---
<!-- inactive-ok-file: THEORY-817 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->

# THEORY-026: For a system driven without feedback through fixed kernels, the average work dissipated at each switch of the drive equals the memory that fails to predict the next input; that is nonnegative when the drive is Markov and, summed, bounds the protocol's dissipation from below when each kernel keeps its equilibrium stationary, so there only nonpredictive memory is wasteful; with feedback, in one binary channel no predictive agent is efficient

## Source

- Still, Sivak, Bell & Crooks (2012), [LIT-327](../literature.d/LIT-327.md), Eqs. (14)–(21) and footnote [24], as read in [NOTE-295](../notes.d/NOTE-295.md).
- Fiderer et al. (2025), [LIT-041](../literature.d/LIT-041.md), Thms 4–5 (Thms 9–10 in the supplement) and Lemma 10, as read in [NOTE-032](../notes.d/NOTE-032.md).

## What was actually shown

**The identity ([LIT-327](../literature.d/LIT-327.md)).** A system with state s_t is driven by a signal x_t through a fixed Markov kernel. Work is done only when the signal changes, and there is no feedback from system to signal. Then the average dissipated work in the step x_t → x_{t+1} is k_BT times I[s_t;x_t] − I[s_t;x_{t+1}] (Eq. 14). [NOTE-295](../notes.d/NOTE-295.md) re-derived this from footnote [24]; given the definitions it is an identity. Summed over a protocol, the "nostalgia" lower-bounds dissipation and excess work (Eq. 18). The heat released is then at least k_BT·(I_e + I_mem − I_pred) (Eq. 21). Here I_e is the Landauer term for entropy removed. The account prices only the part of memory that does not carry over to the next input. Predictive memory costs nothing in it.

**The feedback case ([LIT-041](../literature.d/LIT-041.md)).** Fiderer et al. model agent and environment as coupled hidden-Markov channels. They bound work per round by ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t. Without feedback (a unifilar product environment), the efficient agents are exactly those that are maximally predictive and randomise-and-forget their actions (Thm 4). This is Boyd, Mandal and Crutchfield's tape-setting principle, "randomize-and-forget your actions, predict your percepts", extended beyond stationarity, and its prediction half is the [LIT-327](../literature.d/LIT-327.md) slogan. With feedback, one binary memoryless channel makes the predictive, max-entropy-action and efficient agents three nonempty, pairwise-disjoint sets (Thm 5). Every predictive agent there extracts at most zero. [NOTE-032](../notes.d/NOTE-032.md) checked the numbers: the optimum is ≈ 0.272 bits per round, and uniform-random agents extract ≈ 0.189.

Read together, the two papers bound the claim. Predictive memory is what thermodynamic efficiency asks for only when the system does not act on its source. That reading is the record's. [LIT-041](../literature.d/LIT-041.md) presents itself as breaking the tape-setting principle, and [NOTE-295](../notes.d/NOTE-295.md) says to read the two as baseline and break.

## What this does not say

- **That the per-step nostalgia is a nonnegative cost under any drive.** [NOTE-295](../notes.d/NOTE-295.md) found that nonnegativity needs a Markov drive, which the paper does not state. The note below proves it under that condition; that it fails without it is not shown ([QUESTION-191](../questions.d/QUESTION-191.md)). Under a non-Markov drive, a state that remembers x_{t−1} can predict x_{t+1} better than it tracks x_t, and then the step's "dissipation" as defined is negative. The relaxation step ⟨ΔF^relax_neq⟩ ≤ 0 also needs an unstated stationarity condition.
- **Anything per operation.** Every quantity is an average over paths and protocols. The unit is nats, not bits, and neither paper states a "k_BT ln 2 per bit" cost.
- **Anything about learning systems.** Both papers hold the kernel fixed. [LIT-327](../literature.d/LIT-327.md)'s Discussion raises adaptation but proves nothing about it. [LIT-041](../literature.d/LIT-041.md)'s agent has no learning. Its "prediction and energy efficiency may be at odds in active learning systems" is a hedged extrapolation ([NOTE-032](../notes.d/NOTE-032.md), C14).
- **That efficiency under feedback is a trade-off between prediction and forgetting.** In the only proved example the efficient agent is memoryless ([NOTE-032](../notes.d/NOTE-032.md), C13). No interior optimum is exhibited.
- **Anything about real hardware.** Neither paper models a device.

## Connections

- [LIT-338](../literature.d/LIT-338.md) (IB) is the ancestor, through Still 2009, of the "maximise predictive power at fixed memory" objective that [LIT-327](../literature.d/LIT-327.md)'s Discussion recommends.
- [LIT-308](../literature.d/LIT-308.md) bounds information *acquired* by entropy production, and [LIT-327](../literature.d/LIT-327.md) bounds information *kept but useless* by dissipation. The Landauer term they share is the subject of [THEORY-030](THEORY-030.md).
- [LIT-523](../literature.d/LIT-523.md) (Seifert's review, read in [NOTE-420](../notes.d/NOTE-420.md)) is the framework, not a
  source. For one protocol started in equilibrium, [LIT-327](../literature.d/LIT-327.md)'s dissipation
  equals ⟨W⟩ − ΔF − k_BT·D_KL(p_τ‖p_eq), and the review's Eq. 150 says that
  is nonnegative. That is a protocol total for continuous Langevin
  dynamics; it does not settle the sign of the per-step nostalgia this
  account's `promote_when` asks about.
- [THEORY-431](THEORY-431.md) (Crooks and Jarzynski's fluctuation theorems) is the
  trajectory-level background. This account rests on an average-level
  identity for a discrete Markov chain and uses no fluctuation theorem.

## Note of 2026-10-19: the identity and the bound, re-derived

Re-derived for the promotion audit (batch 045, [ADR-047](../decisions.d/ADR-047.md) v2). The setup is
[LIT-327](../literature.d/LIT-327.md)'s. A system with state s is driven by x. Energies are E(s, x),
and p_eq(s|x) ∝ exp(−βE(s, x)). At each step the drive switches
x_t → x_{t+1} with s_t held, which is where work is done. Then s relaxes
under a kernel K_x at fixed x_{t+1}. Nothing feeds back from s to x.

1. **The identity, with no further condition.** Write
   F_neq(x) = ⟨E(s, x)⟩ − kT·H[p(s|x)] for the free energy of the
   conditional distribution, averaged over x. At the switch,
   ⟨W_t⟩ = ⟨E(s_t, x_{t+1})⟩ − ⟨E(s_t, x_t)⟩. The averaged F_neq changes by
   the same energy difference minus kT(H[S_t|X_{t+1}] − H[S_t|X_t]). So
   β(⟨W_t⟩ − ΔF_neq) = H[S_t|X_{t+1}] − H[S_t|X_t] = I[s_t;x_t] − I[s_t;x_{t+1}].
2. **Nonnegative under a Markov drive.** With no feedback, s_t depends
   on x_0, …, x_t and on noise independent of the drive. A Markov drive
   makes x_{t+1} independent of the earlier inputs given x_t. So
   s_t – x_t – x_{t+1} is a Markov chain, and data processing gives
   I[s_t;x_t] ≥ I[s_t;x_{t+1}].
3. **A lower bound when each kernel keeps its equilibrium stationary.**
   Start the protocol in equilibrium and write
   F_neq = F_eq + kT·D_KL(p(s|x) ‖ p_eq(s|x)). Then
   W − ΔF_eq = Σ_t (W_t − ΔF_neq at the switch) − Σ_t (ΔF_neq in the
   relaxation) + kT·D_final. Relaxation does no work. Relative entropy to a
   distribution the kernel keeps stationary cannot grow under that kernel,
   so each relaxation term is nonnegative. D_final ≥ 0. Hence
   βW_diss ≥ Σ_t (I[s_t;x_t] − I[s_t;x_{t+1}]).
4. **A numerical check.** For a 4-state system driven by a 3-symbol
   Markov chain through Metropolis kernels, the identity in step 1 holds to
   10⁻¹⁰, and over six steps the dissipation, 0.426 nats, exceeds the
   summed nostalgia, 0.076.
5. **The feedback channel.** In [LIT-041](../literature.d/LIT-041.md)'s Theorem 5 channel, action 0
   gives percept 0 and action 1 a fair coin. A memoryless agent that plays
   0 with probability q extracts at most h(q) − h((1+q)/2) bits per round.
   That is largest at q = 1/√2, about 0.272, and equals 1 − h(3/4) ≈ 0.189
   at q = ½. A predictive agent there has H(A|M) = 0, so it extracts at
   most −H(S|M) ≤ 0. In this channel no predictive agent is efficient.

Steps 2 and 3 meet the promote_when's request for a derivation under the
two conditions. A system in which the bound fails without them is not
built, and neither is a physical test; both are [QUESTION-191](../questions.d/QUESTION-191.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 072) filed [THEORY-817](THEORY-817.md)
as Proposed, extending this entry. It carries the claim this entry's
title gave up when batch 045 narrowed it: that once actions feed back on the drive, maximal prediction is generally not what thermodynamic efficiency requires, which Fiderer et al. assert from their one proved binary channel.
This entry is its evidence and is not changed by the filing.
