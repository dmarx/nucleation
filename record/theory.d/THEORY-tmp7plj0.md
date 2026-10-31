---
status: Active
title: 'When a conservative experiment is safe under every plausible model, can be repeated from a common state and keeps informing, a controller that acts on the lower end of an anytime confidence sequence stays safe with probability 1 − δ and approaches the safe oracle, at O(√(T log T)) regret in a braking example; a certainty-equivalent controller in the same example is unsafe with probability ½ in every episode however much data it has'
version: 1
tags:
- control-theory
- mathematics
- learning-theory
date: '2026-10-31'
source:
- LIT-tmp1o60r
summary: >-
  Saligrama (2026), [LIT-tmp1o60r](../literature.d/LIT-tmp1o60r.md), §5 (Lemma 5, Theorem 2, Corollaries
  5–7, §5.6.1), read in [NOTE-tmp5ibkm](../notes.d/NOTE-tmp5ibkm.md) with the proofs of Lemma 5 and
  Theorem 2. Active: a short proof by a Gaussian mixture martingale and
  Ville's inequality, checked by hand, and an elementary calculation for
  certainty equivalence. Narrow: a scalar parameter with a known
  conservative direction, an experiment that returns to a common state,
  and Gaussian observations.
---

# THEORY-tmp7plj0: When a conservative experiment is safe under every plausible model, can be repeated from a common state and keeps informing, a controller that acts on the lower end of an anytime confidence sequence stays safe with probability 1 − δ and approaches the safe oracle, at O(√(T log T)) regret in a braking example; a certainty-equivalent controller in the same example is unsafe with probability ½ in every episode however much data it has

## Source

Saligrama (2026), [LIT-tmp1o60r](../literature.d/LIT-tmp1o60r.md), §5 and Appendix B, pp. 20–25 and 38–40 of
arXiv 2607.16895v1; read in [NOTE-tmp5ibkm](../notes.d/NOTE-tmp5ibkm.md).

## What was actually shown

**Assumption 1.** A scalar θ in [θ_lo, θ_hi]. An experiment κ_ϑ with
ϑ ≤ θ is safe under θ and returns the system to a common state (P2); its
value loss is at most ω(θ − ϑ) (P3); each episode yields y = θa + ξ,
ξ ~ N(0, σ²), and V_t = Σa²/σ² accumulates.

**Lemma 5.** Mixing exp(λM_t − λ²V_t/2) over λ ~ N(0, 1/ν) gives a
nonnegative martingale √(ν/(V_t + ν))·exp(M_t²/(2(V_t + ν))). Ville's
inequality makes |θ̂_t − θ| ≤ b(V_t, δ; ν) =
√(2(V_t + ν)log(√(1 + V_t/ν)/δ))/V_t hold at every t at once with
probability 1 − δ.

**Theorem 2.** Run κ at ϑ_t = θ̂_{t−1} − b(V_{t−1}), clipped. On the
confidence event every ϑ_t ≤ θ, so every episode is safe, and
θ − ϑ_t ≤ 2b, so the loss is ω(2b). Regret ≤ r_max + Σ E ω(2b(V_{t−1}))
+ r_max Tδ. With V_t ≍ t and ω linear this is O(√(T log T)); in the
braking example O(σ√(D/θ)·√(T log T)).

**Certainty equivalence.** Using the sample mean, the next entry speed
overshoots the safe one exactly when θ̂ > θ, which for Gaussian noise has
probability ½ for every n. A one-episode risk δ < ½ needs a margin of at
least σΦ⁻¹(1 − δ)/√n, and a guarantee over the whole trajectory needs a
time-uniform one.

**What could have failed.** Persistent information could have been
unusable: the controller might have had to leave the common safe regime
to exploit it. The common-reset condition rules that out here.

## What this does not say

- **That recovery is generic.** The author: "These are sufficient
  conditions, not necessary ones. Vector parameters, multiple
  control-equivalence classes, non-resetting trajectories, and dynamic
  latent environments require additional transition and exploitation
  arguments" (Remark 9).
- **That growth of information suffices.** Information must also be
  convertible into a safe transition to the selected regime (§6, §9).
- **Anything when information is bounded.** That is [THEORY-tmp78ls3](THEORY-tmp78ls3.md)'s
  regime, where no rule recovers the gap.
