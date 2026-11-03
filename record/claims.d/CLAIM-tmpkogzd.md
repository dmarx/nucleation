---
status: Active
title: 'In tolerance-bounded compatibility on a graph with disturbed offsets, |Dx − a₀ − w| ≤ δ for |w_e| ≤ η_e, a compatible configuration exists for every disturbance exactly when |cᵀa₀| + Σ η_e|c_e| ≤ Σ δ_e|c_e| on every cycle, and one configuration serves every disturbance exactly when η ≤ δ and |cᵀa₀| ≤ Σ(δ_e − η_e)|c_e|; an agent that chooses its configuration from what it observes needs the second condition within each class of disturbances it cannot tell apart, so whether a compatible state can be selected lies between the two and depends on what the agent can read'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A counterexample within the scalar model: offsets, tolerances and
  disturbance bounds for which the stated cycle inequalities hold and the
  corresponding configuration fails to exist, or fail and it exists.
tags:
- mathematics
- agency
date: '2026-11-03'
line:
- will-organization
- formal-apparatus
rests_on:
- CLAIM-tmplvc8b
uses:
- TERM-064
- TERM-060
complements:
- CLAIM-354
- CLAIM-tmpg1n2c
grounds:
- LIT-tmphox4k
bears_on:
- QUESTION-282
summary: >-
  A30 §§2–3 of the exchange "Assess SDT Coverage" (2026-11-02), at the
  owner's "keep going", with the second and third conditions derived by
  the reader of U30–U31 and checked by simulation (500 random instances,
  no mismatch). It is the first concrete instance of the branch's note of
  2026-11-02 on CLAIM-354, that a reachable set should range over the
  policies an organization can carry out on what it can read. The framing
  is adjustable robust optimization (LIT-tmphox4k). Static selection only,
  scalar overlaps only.
---
<!-- inactive-ok-file: CLAIM-354 CLAIM-tmplvc8b CLAIM-tmpg1n2c LIT-tmphox4k QUESTION-282 — Proposed, Open, Deferred or new; cited as open -->

# CLAIM-tmpkogzd: In tolerance-bounded compatibility on a graph with disturbed offsets, |Dx − a₀ − w| ≤ δ for |w_e| ≤ η_e, a compatible configuration exists for every disturbance exactly when |cᵀa₀| + Σ η_e|c_e| ≤ Σ δ_e|c_e| on every cycle, and one configuration serves every disturbance exactly when η ≤ δ and |cᵀa₀| ≤ Σ(δ_e − η_e)|c_e|; an agent that chooses its configuration from what it observes needs the second condition within each class of disturbances it cannot tell apart, so whether a compatible state can be selected lies between the two and depends on what the agent can read

## The claim

Let the offsets of CLAIM-tmplvc8b be disturbed, a = a₀ + w with |w_e| ≤ η_e.
Three conditions, in increasing strength:

- **I, adjustable.** For every w some x(w) is within tolerance. Swapping ∀w
  with the cycle quantifier and taking max_w cᵀw = Σ η_e|c_e| gives
  |cᵀa₀| + Σ η_e|c_e| ≤ Σ δ_e|c_e| for every cycle.
- **II, static.** One x serves every w. Then each overlap must absorb its own
  disturbance, so η ≤ δ, and what is left must cover the nominal holonomy:
  |cᵀa₀| ≤ Σ (δ_e − η_e)|c_e|.
- **III, observed.** The agent sees o = h(w) and picks x(o). That holds exactly
  when II holds within each class h⁻¹(o) of disturbances it cannot tell apart.
  Perfect legibility gives I; none gives II.

A30's triangle with offsets ±0.6 shows the gap. I holds (0.6 ≤ 0.9), so each
world has a compatible configuration. II fails, since edge 12 would need
x₂ − x₁ in both [0.3, 0.9] and [−0.9, −0.3]. An agent that cannot tell the two
worlds apart cannot select a compatible state, though one exists in each.

This is CLAIM-354's note of 2026-11-02 made concrete: what an agent can
achieve is what the policies it can carry out on what it can read achieve,
not what exists state by state. CLAIM-tmpg1n2c states the same in general.

## What it does not say

- **Anything about feedback over time.** The selection is one-shot.
- **Anything beyond scalar overlaps.**
- **That A30's moving-target example shows a gluing effect.** It fails on one
  overlap whose target moves faster than its relative actuation; the cycle
  plays no part.
