---
status: Proposed
title: 'A coordination mode kept by a decaying capacity: in φ̇ = −sin φ − c sin 2φ anti-phase is stable only for c > ½, with relaxation time 1/(2c − 1) and escape barrier (2c − 1)²/(4c); with c produced at 2.2c²/(1 + c²) against unit decay, c = 0.6 holds anti-phase stable while lying below the unstable maintenance level 0.642, so the capacity decays through ½ and the mode is lost'
version: 1
standing: stipulated
kind: construction
tags:
- complex-systems
- mathematics
date: '2026-11-07'
line:
- distributed-agency
- formal-apparatus
variant_of:
- CASE-189
illustrates:
- CLAIM-521
- CLAIM-079
summary: >-
  A29 §2, §3 and §5 of the exchange "Individuation, Possibility, and
  Disposition" (2026-11-06 to 07), answering the owner's U12, "tie this
  back to the synergetics and coordination dynamics material", and U13.
  The Haken–Kelso–Bunz relative-phase equation with its coupling made a
  maintained capacity. A: "The collective coordination pattern is stable,
  but the organization sustaining its stability is not." The reader reran
  the numbers and added a condition A omits: the contrast is a separation
  of time scales only when the maintenance rate ε is small, about 0.1 or
  less. The wording is A's; adopting it is the owner's call.
---

# CASE-tmpn5x96: A coordination mode kept by a decaying capacity: in φ̇ = −sin φ − c sin 2φ anti-phase is stable only for c > ½, with relaxation time 1/(2c − 1) and escape barrier (2c − 1)²/(4c); with c produced at 2.2c²/(1 + c²) against unit decay, c = 0.6 holds anti-phase stable while lying below the unstable maintenance level 0.642, so the capacity decays through ½ and the mode is lost

## The case

A29 §2 of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e) starts
from φ̇ = −a sin φ − 2b sin 2φ, where anti-phase is stable iff 4b > a
(THEORY-1227), and sets a = 1, b = c/2:

- φ̇ = −sin φ − c sin 2φ. Anti-phase is stable iff c > ½.
- ċ = ε(α c²/(1 + c²) − δc + u_ext), with α = 2.2, δ = 1 and no external
  supply.
- c(0) = 0.6. "At that moment, anti-phase coordination is stable because
  \(0.6>0.5\)."

A29 §3 adds noise in the potential V(φ; c) = −cos φ − (c/2) cos 2φ. The
saddle is at cos φ_s = −1/(2c), and the barrier against escape from
anti-phase is ΔV(c) = (2c − 1)²/(4c), which vanishes at c = ½. A29 §5 gives
the anti-phase relaxation time 1/(2c − 1).

**The reader's rerun.**

- c² − 2.2c + 1 = 0 gives c₋ = 0.64174 and c₊ = 1.55826. The production
  minus decay has slope −1 at 0, +0.417 at c₋ (unstable) and −0.417 at c₊
  (stable).
- At c = 0.6 it is −0.0176, so c decays, crossing ½ at t ≈ 2.88/ε.
- The barrier matches A's nine chart values to four places, and anti-phase
  is always the shallower well.

**The reader's ε caveat.** At c = 0.6 the anti-phase relaxation time is 5.
With ε = 1 the mode is lost at t ≈ 2.9, before it has relaxed once. With
ε = 0.1 the loss comes at t ≈ 29. The contrast between a stable pattern
and an unsustained organization reads as a separation of time scales only
for ε about 0.1 or less. A29 §5 notes that the relaxation time diverges near ½ but does
not set ε.

**What is held.** The maintenance law is CASE-189's Construction 1 on its
symmetric diagonal, 3c²/(1 + c²) − (1 + d)c, with gain 2.2 for 3/(1 + d);
positive equilibria exist iff the gain is at least twice the decay. Its
unstable level is CLAIM-604's ignition threshold. New here are the HKB
coupling b = c/2 and the barrier as a function of the maintained capacity.

## What it can show

That a coordination mode can be stable now while the capacity keeping it
stable is not maintained, given ε small. It has CLAIM-521's shape, a
currently effective pattern over an unsustained maintenance, though by
another mechanism: decline from below an unstable threshold, not a
recovery rate vanishing at a saddle-node.

As a proposed study, A29 §10 sets four arms with matched short-term phase
dynamics: c held fixed, c slowly decaying, c kept by an outside controller,
and c kept by internal production (compare CLAIM-522 and CLAIM-456). None
has been run.

It cannot show anything about biological closure. A: "This is an
illustrative phenomenological model. It does not yet establish biological
closure of constraints."
