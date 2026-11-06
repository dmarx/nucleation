---
number: 537
status: Active
formerly:
- CLAIM-tmpkogzd
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
- CLAIM-538
uses:
- TERM-064
- TERM-060
complements:
- CLAIM-354
- CLAIM-535
grounds:
- LIT-1975
bears_on:
- QUESTION-282
summary: >-
  A30 §§2–3 of the exchange "Assess SDT Coverage" (2026-11-02), at the
  owner's "keep going", with the second and third conditions derived by
  the reader of U30–U31 and checked by simulation (500 random instances,
  no mismatch). It is the first concrete instance of the branch's note of
  2026-11-02 on [CLAIM-354](CLAIM-354.md), that a reachable set should range over the
  policies an organization can carry out on what it can read. The framing
  is adjustable robust optimization ([LIT-1975](../literature.d/LIT-1975.md)). Static selection only,
  scalar overlaps only.
---

# CLAIM-537: In tolerance-bounded compatibility on a graph with disturbed offsets, |Dx − a₀ − w| ≤ δ for |w_e| ≤ η_e, a compatible configuration exists for every disturbance exactly when |cᵀa₀| + Σ η_e|c_e| ≤ Σ δ_e|c_e| on every cycle, and one configuration serves every disturbance exactly when η ≤ δ and |cᵀa₀| ≤ Σ(δ_e − η_e)|c_e|; an agent that chooses its configuration from what it observes needs the second condition within each class of disturbances it cannot tell apart, so whether a compatible state can be selected lies between the two and depends on what the agent can read

## The claim

Let the offsets of [CLAIM-538](CLAIM-538.md) be disturbed, a = a₀ + w with |w_e| ≤ η_e.
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

This is [CLAIM-354](CLAIM-354.md)'s note of 2026-11-02 made concrete: what an agent can
achieve is what the policies it can carry out on what it can read achieve,
not what exists state by state. [CLAIM-535](CLAIM-535.md) states the same in general.

## What it does not say

- **Anything about feedback over time.** The selection is one-shot.
- **Anything beyond scalar overlaps.**
- **That A30's moving-target example shows a gluing effect.** It fails on one
  overlap whose target moves faster than its relative actuation; the cycle
  plays no part.

## Note of 2026-11-03: Ben-Tal et al., read

Conditions I and II are exactly Ben-Tal et al.'s adjustable and ordinary
robust counterparts ([NOTE-1503](../notes.d/NOTE-1503.md)). Condition III matches what the paper calls
an "information basis", which it names (p. 353) and does not develop, so III is
this claim's own result, not a citation. The paper's in-between case, the
affinely adjustable counterpart, restricts the rule's form, not what it reads.
Its Theorem 2.1 explains the gap here: an edge's two inequalities share one
disturbance, so the uncertainty is not constraint-wise.

## Note of 2026-11-04: a resource-budget index, from "Organizational Nucleation and SLT"

This claim indexes compatibility by what the agent can read. The exchange
proposed a second index, by resources. A9: "We could therefore replace a
single compatibility complex with a **resource- and tolerance-indexed
family of complexes**", 𝒦(B, τ, ℓ; H), with B "a resource budget,
potentially distributed across sensing, control, and maintenance". A29 §7
applied it to attention: allocations rᵢ with Σᵢ rᵢ ≤ Bₜ, and a face is a set
S for which some feasible r lies in ⋂_{i∈S} Aᵢ(c). "A decrease in available
cognitive resources can make previously compatible requirements
incompatible without changing the person's motivations."

The reader checked it. The family is downward-closed and monotone in B.
With Aᵢ = {rᵢ ≥ nᵢ} it is a knapsack test, Σ_{i∈S} nᵢ ≤ B, and pairwise
compatibility does not give joint compatibility (three perspectives with
nᵢ = 0.4B), as in [CASE-119](../cases.d/CASE-119.md). What follows is A29's: low performance alone
does not tell "attention dysregulation due to governance" from "attention
limitations due to capacity". [CLAIM-475](CLAIM-475.md) and [TERM-092](../terms.d/TERM-092.md) index inquiry by a
budget in the same way. If this index is filed, it is a sibling of this
claim's index by legibility, not a consequence of it. The wording is A's,
sharpened by the reader; adopting it is the owner's call. No status
changes.
