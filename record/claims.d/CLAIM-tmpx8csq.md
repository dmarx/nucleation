---
status: Proposed
title: 'A mode''s slowness says how it persists, not how hard it is to redirect:
  for ȧ = −γa + bu the least quadratic effort to move a from 0 to Δ by time
  H is 2γΔ²/(b²(1 − e^{−2γH})), which falls as γ falls, so a slower mode is
  cheaper to redirect through the same input, and a mode with b = 0 cannot
  be redirected through it at any rate; persistence, redirection and the renewal
  of a mode''s supports are three timescales that need not coincide'
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the formula or its monotonicity. As a reading of
  organizations, an institution whose slowest-persisting structures are always
  the costliest to redirect through every available channel, so that persistence
  does fix redirectability there.
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-22'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-345
complements:
- CLAIM-589
- CLAIM-626
summary: A40 §3 of the exchange "Explain First Contact RL" (ChatGPT, second
  share of 2026-11-22), answering the owner's U21 (slow modes and slow degrees
  of freedom). The formula is the one-mode case of [CLAIM-345](CLAIM-345.md)'s Gramian. A40
  says smaller γ "can actually make the displacement cheaper"; the assistant's
  check shows that for fixed b and H the least effort strictly increases with
  γ, and tends to Δ²/(b²H) as γ → 0. The idea and formula are A's (ChatGPT,
  in the exchange of 2026-11-22); the monotonicity statement and the wording
  are the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-626 THEORY-1052 — Proposed; cited in this filing of 2026-11-22 (second share) -->

# CLAIM-tmpx8csq: A mode's slowness says how it persists, not how hard it is to redirect: for ȧ = −γa + bu the least quadratic effort to move a from 0 to Δ by time H is 2γΔ²/(b²(1 − e^{−2γH})), which falls as γ falls, so a slower mode is cheaper to redirect through the same input, and a mode with b = 0 cannot be redirected through it at any rate; persistence, redirection and the renewal of a mode's supports are three timescales that need not coincide

## Derivation and check

For ȧ = −γa + bu, a(0) = 0, the reachability Gramian on [0, H] is W_H =
∫₀ᴴ b² e^{−2γt} dt = b²(1 − e^{−2γH})/(2γ). The least ∫u² reaching Δ is
Δ²/W_H = 2γΔ²/(b²(1 − e^{−2γH})), as A40 gives. That is [CLAIM-345](CLAIM-345.md)'s
Δxᵀ W_H^† Δx in one dimension. The function 2γ/(1 − e^{−2γH}) is strictly
increasing in γ > 0, with limit 1/H as γ → 0. Checked with python3 -I:
the closed form matches a numerical quadrature of the Gramian at three
parameter settings, and the monotonicity holds on a grid of 200 values of
γ.

## What it shows

A40: "a mode's slowness tells us how it persists, not by itself how
difficult it is to redirect." It names three timescales: τ_relax (natural
persistence), τ_control (least effective intervention time) and
τ_reproduce (renewal of the mode's supports), as in "A legal norm may
persist for decades, be suspended in an emergency within minutes, and
depend on institutional practices that must be reproduced over years."
This complements [CLAIM-589](CLAIM-589.md) (permitted, actuated, affordable), and
[CLAIM-626](CLAIM-626.md), whose maintenance mode is τ_reproduce slowing.

## Neighbours A40 cites, checked

- [CLAIM-481](CLAIM-481.md) holds the dissipative pair and its collective and relative
  rates a and a + 2k, which A40 §2 restates.
- [CLAIM-626](CLAIM-626.md) holds the three meanings of critical slowing, with the
  detuned phase oscillators whose transverse rate √(4K² − Δω²) A40 §5
  gives. Checked: 2K cos(arcsin(Δω/2K)) = √(4K² − Δω²).
- [THEORY-1052](../theory.d/THEORY-1052.md) holds rate-induced tipping (A40 §7).
