---
number: 542
status: Active
formerly:
- CLAIM-tmpptgk8
title: 'Sensitivity does not fix the allocation or the authorship of control: linearized, every input reaches the final state through the same transition operator, ∂x_T/∂w_t = Φ(T, t)B_w(t), so systems with the same Lyapunov spectrum can differ arbitrarily in what an agent''s own channel, an outside party''s channel and noise each reach and at what least energy; and along one unstable direction a larger exponent λ lowers the least effort to reach a displacement, since W_T = b²(e^{2λT} − 1)/2λ grows with λ, while a constant open-loop input against white noise entering the same direction has terminal signal-to-noise ratio tending to (bu/σ)√(2/λ), which falls as λ grows, so only feedback that observes the state turns cheaper control into reliable direction'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a pair of linear time-varying systems with
  the same A(t) whose input channels must have Gramians with the same
  range and least-energy form; a finite-time Lyapunov spectrum that fixes
  the Gramian of every input channel; or an error in the mean and
  variance of the scalar case, so that the open-loop ratio is not
  decreasing in λ under the stated assumptions (x(0) = 0, constant u,
  white noise of intensity σ, horizon long against 1/λ).
tags:
- control-theory
- mathematics
- free-will
date: '2026-11-02'
line:
- will-organization
- formal-apparatus
rests_on:
- CLAIM-345
complements:
- CLAIM-354
grounds:
- LIT-1997
summary: >-
  The demonstrated part of the owner's U16 and U20 of the exchange "Assess
  SDT Coverage" (2026-11-02), "controllability vs sensitivity". A20 §2
  stated the impulse case ("the relative contribution is not determined by
  e^{λT}") and A22 §5 the channel case. The scalar signal-to-noise result
  is the reader's derivation, checked by simulation. It sharpens the
  owner's point: sensitivity makes control cheaper and, without feedback,
  less decisive against noise. [CLAIM-345](CLAIM-345.md) holds the cost formula and not
  the allocation across channels.
---
<!-- inactive-ok-file: NOTE-1536 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: CLAIM-354 CLAIM-533 LIT-1997 — Proposed, Open, Deferred or Unavailable; cited from the exchange "Assess SDT Coverage" of 2026-11-02 as open, works registered unread among them -->

# CLAIM-542: Sensitivity does not fix the allocation or the authorship of control: linearized, every input reaches the final state through the same transition operator, ∂x_T/∂w_t = Φ(T, t)B_w(t), so systems with the same Lyapunov spectrum can differ arbitrarily in what an agent's own channel, an outside party's channel and noise each reach and at what least energy; and along one unstable direction a larger exponent λ lowers the least effort to reach a displacement, since W_T = b²(e^{2λT} − 1)/2λ grows with λ, while a constant open-loop input against white noise entering the same direction has terminal signal-to-noise ratio tending to (bu/σ)√(2/λ), which falls as λ grows, so only feedback that observes the state turns cheaper control into reliable direction

## The claim

**Channels.** Linearize the dynamics about a trajectory:
δẋ = A(t)δx + B_s(t)u + B_a(t)v + Σ(t)ξ, with u the agent's own input, v an
outside party's and ξ noise. By variation of constants every input reaches
the final state through the same Φ(T, t). The Lyapunov spectrum is a property
of Φ. What each input can reach is a property of (Φ, B_w), its Gramian
W_w(T) = ∫₀ᵀ Φ(T, t)B_wB_wᵀΦ(T, t)ᵀ dt, and its least energy for a
displacement Δx in range is Δxᵀ W_w^† Δx ([CLAIM-345](CLAIM-345.md)). So two systems equally
chaotic can differ arbitrarily in how control is shared among the three.
Over long horizons any channel with a generic component along the leading
unstable direction grows at the same rate λ, so the channels differ in their
projections onto the unstable directions and in what they reach at finite
horizons, not in exponential rate.

**One unstable direction.** dx = (λx + bu)dt + σ dW, x(0) = 0, constant u.

- Least effort to reach a displacement: W_T = b²(e^{2λT} − 1)/(2λ), which
  grows with λ, so the cost Δx²/W_T falls.
- Open loop against noise: the terminal mean is bu(e^{λT} − 1)/λ and the
  variance σ²(e^{2λT} − 1)/(2λ), so the signal-to-noise ratio tends to
  (bu/σ)√(2/λ) for λT large. It falls as λ grows. Noise is fed in all along,
  while only the early input is amplified.

Simulated (20,000 paths, T = 8, b = u = σ = 1): λ = 0.5, 1, 2 give ratios
1.98, 1.40, 1.00, against the exact 1.96, 1.41, 1.00 and the limit 2.00,
1.41, 1.00.

So sensitivity lowers the cost of control but does not raise the
controller's share of the outcome against disturbances in the same
direction. Feedback that observes the state changes that, which is what
Ott, Grebogi and Yorke's control of chaos does ([LIT-1997](../literature.d/LIT-1997.md)).

**Mode by mode** (A28 §4 of the exchange). For ż = −κLz + B_s u + B_e v with L
symmetric and eigenvectors w_k, a constant outside input along mode k
displaces it by (w_kᵀB_e v)/(κλ_k), so the slowest modes are the most
displaced. If w_kᵀB_s = 0 the agent's own channel cannot reach that mode at
all, by the PBH eigenvector test. And a channel of rank one cannot control a
system with a repeated eigenvalue, so a single channel cannot control a sheaf
with dim H⁰ ≥ 2. Stabilizability and detectability with H⁰ = 0 are [NOTE-1222](../notes.d/NOTE-1222.md)'s
Thms 6.1–6.2.

## What it does not say

- **Anything beyond the linearization.** Nonlinear basins, separatrices
  and slow modes are where an effect can outlast its cause; the claim is
  local.
- **That the agent is the author of what its channel does.** A channel's
  reach is not whose input it carries ([CLAIM-022](CLAIM-022.md), [QUESTION-071](../questions.d/QUESTION-071.md)).
- **That comparisons of energy across channels are free.** As [CLAIM-345](CLAIM-345.md)
  says, they need inputs in common units and budgets.

## Note of 2026-11-03: the stable side

On a stable direction, dx = (−|λ|x + bu)dt + σ dW, the stationary
signal-to-noise ratio is (bu/σ)√(2/|λ|), which rises as a fold is approached
(the reader of Scheffer et al., [NOTE-1536](../notes.d/NOTE-1536.md)). So the open-loop ratio goes as
1/√|λ| on both sides of marginal stability: near the fold a constant input is
most decisive against noise and cheapest to sustain, and slowing down is
where it is. Linear regime only.

## Note of 2026-11-03 (later): Kane's relabelling

Kane's self-forming action ([NOTE-1518](../notes.d/NOTE-1518.md), p. 40) makes the noise that hinders
each choice the agent's own competing effort. In this claim's terms that moves
Σ into B_self: two of the agent's channels, each the other's disturbance. The
share of the outcome against outside noise is then undefined, because there is
none. The claim's results hold wherever some of the noise is exogenous, which
neural noise generally is.

## Note of 2026-11-05: the constraint-architecture readings

Murray and Sastry ([NOTE-1622](../notes.d/NOTE-1622.md)), from the pasted synthesis on constraint architectures, support the claim in kind, from nonlinear control: that a driftless system is controllable says nothing of which inputs reach a direction or how much cycling it takes, motion along higher brackets needing more cycles. It is the same family as [CLAIM-345](CLAIM-345.md), outside the linear setting the claim works in. The paper computes no least energy beyond the first-order case, says nothing of Lyapunov exponents or noise, and does not separate an agent's own channel from an outside party's. No status changes.
