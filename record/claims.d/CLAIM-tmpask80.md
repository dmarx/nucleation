---
status: Proposed
title: 'Nearness to a dynamical transition changes what a system computes well rather than raising every computational ability: memory and separation, sensitivity, reliability and speed pull apart, total capacity is bounded by the number of independent state variables, and the best distance from the transition depends on the task, the integration window and the correlations of the environment'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A class of dynamical systems, with a named transition and a capacity
  measure covering memory, nonlinear transformation and discrimination,
  in which every component of that measure is maximized at the
  transition for every task in a stated family and every finite
  integration window, so that nearness to the transition raises all
  computational abilities at once; or a showing that the
  information-processing capacity of a reservoir with fading memory is
  not bounded by its number of independent state variables. A single task
  whose optimum sits at the transition does not defeat it.
tags:
- complex-systems
- information-theory
- neuroscience
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
answers:
- QUESTION-tmp2hhlc
grounds:
- LIT-tmp7sbn6
- LIT-tmpe6jga
- LIT-tmpkvpg4
- THEORY-2041
- THEORY-1431
summary: >-
  A's answer, at A15 §1–§9 of the exchange "Rich Get Richer Power Laws",
  to whether criticality is good for computation: it "may change what
  kinds of computations a system is good at, rather than universally
  increasing all computational abilities". A rests it on Dambre and
  colleagues' capacity bound, a finite-window study, and a three-way
  tradeoff of sensitivity, reliability and speed; scale-free memory helps
  only if the environment has correlations across scales, and large
  cascades help only if they keep inputs distinguishable. The works are
  unread. A's illustrative mechanism, a memory–noise tradeoff in a scalar
  linear model, does not hold as stated ([CLAIM-tmpd1shn](CLAIM-tmpd1shn.md)), though the
  conclusion survives. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A15); adopting it is the owner's
  call.
rests_on:
- CLAIM-tmpd1shn
bears_on:
- QUESTION-tmp2hhlc
---
<!-- inactive-ok-file: CLAIM-tmpd1shn ARG-tmpubyzo — filed with this claim from the same exchange, Open or Proposed -->
<!-- inactive-ok-file: LIT-tmp7sbn6 LIT-tmpe6jga LIT-tmpkvpg4 — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: CLAIM-769 CLAIM-626 — Proposed, bearing on the claim -->

# CLAIM-tmpask80: Nearness to a dynamical transition changes what a system computes well rather than raising every computational ability: memory and separation, sensitivity, reliability and speed pull apart, total capacity is bounded by the number of independent state variables, and the best distance from the transition depends on the task, the integration window and the correlations of the environment

## The claim

A15 gives five strands, each A's unless a work is named.

1. **Memory against separation.** A reservoir, x_{t+1} = φ(Wx_t + Bu_t)
   with a trained linear readout, needs "**Memory:** The current network
   state retains information about past inputs" and "**Separation:**
   Different input histories produce sufficiently distinguishable internal
   states" (A15 §3). An ordered network forgets; a chaotic one separates
   but cannot be read reliably; near the transition both can hold, the
   edge-of-chaos result ([LIT-tmpkvpg4](../literature.d/LIT-tmpkvpg4.md), unread).
2. **A bound on capacity.** "Dambre and colleagues showed that, under
   specified conditions, a reservoir's total information-processing
   capacity is bounded by its number of independent state variables.
   Different dynamical regimes can redistribute that capacity between
   linear memory and nonlinear transformations" (A15 §3; [LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md),
   unread).
3. **Sensitivity, reliability, speed.** Near criticality susceptibility,
   fluctuations and relaxation time all grow, so "exactly critical may not
   be exactly optimal" (A15 §6). A finite integration window moves the
   best discrimination of inputs away from the critical point
   ([LIT-tmpe6jga](../literature.d/LIT-tmpe6jga.md), unread).
4. **The environment sets the value of multiscale memory.** A superposition
   of exponential relaxations with rates spread as λ^(α−1) gives power-law
   memory without criticality (A15 §4; the record's [CLAIM-769](CLAIM-769.md)), but "the
   computational value depends on whether the environment itself contains
   meaningful correlations across those timescales" (A15 §4, §8).
5. **Magnitude is not discriminability.** Rare large cascades may carry
   much of the global transfer, "but … if they saturate the network, they
   may erase distinctions between different inputs. Useful computation
   depends on the *structure and discriminability of responses*, not
   merely their magnitude" (A15 §9).

Hence: "**Near-critical may be useful, but the optimal distance from
criticality depends on what the system needs to accomplish.**"

## Where the turn needs correcting

- **The scalar model's tradeoff.** A15 §2 illustrates the tension with
  x_{t+1} = a x_t + u_t + η_t: memory half-life ln(½)/ln a diverges as
  a → 1 (A's table is right: 1, 3.1, 6.6, 69 and 693 steps at a = 0.5,
  0.8, 0.9, 0.99 and 0.999, which the assistant recomputed), and so does
  the noise variance σ²/(1 − a²), whence "Criticality amplifies both
  information and uncertainty." But input and noise pass through the same
  filter, so their ratio in the state does not depend on a, and nor does
  the total memory capacity. The gain only spreads capacity over lags.
  The conclusion A wants survives, by a different route: [CLAIM-tmpd1shn](CLAIM-tmpd1shn.md),
  and [ARG-tmpubyzo](../arguments.d/ARG-tmpubyzo.md) for how far it carries.
- **Marginal stability is not criticality.** The scalar model at a → 1 is
  at the edge of linear stability, which A rightly says "resembles
  critical slowing down"; it is not a collective transition. [CLAIM-626](CLAIM-626.md)
  holds that slowing has no single organizational meaning.
- **Misattribution.** A15 §3 names "Bertschinger, Natschläger, and
  Legenstein" for the 2004 study. The 2004 Neural Computation paper is by
  Bertschinger and Natschläger ([LIT-tmpkvpg4](../literature.d/LIT-tmpkvpg4.md)); Legenstein is an author of
  a separate paper with Maass (2007), not registered.
- **Two transitions.** A runs the order-to-chaos transition and branching
  criticality together ([QUESTION-tmp2hhlc](../questions.d/QUESTION-tmp2hhlc.md), point 1).
- **Power-law memory's range.** The Γ(α) integral converges for α > 0,
  and with rates confined to [λ_min, λ_max] the power law holds for
  1/λ_max ≪ t ≪ 1/λ_min; the long-time end, where memory matters, is set
  by the slowest rates. A says only "an intermediate range of times".

## What it does not say

- Not that nearness to a transition never helps: it can shift capacity
  toward long memory, which some tasks need.
- Not that brains are critical. A15 §5 calls the evidence "contested",
  and the record holds only that 1/f structure does not discriminate
  mechanism ([CLAIM-692](CLAIM-692.md)).
