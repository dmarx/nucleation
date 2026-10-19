---
status: Active
title: 'Under one-hop allocation within an epoch, an operator that endorses an ally whose policy is nearer its own than the collective decision is raises how far its preferred policy is realized while its own authority stays fixed, so the two conditions of the endorsement scheme hold together'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-285 and filed Active at the owner's direction, carrying
    out the promotion audit's decision (record/promotion-audit/decisions/CLAIM-285.yaml,
    batch 001, ADR-047). CLAIM-285 was filed as demonstrated, but its body
    argues in prose, and its defeat condition has an empirical disjunct
    with no observation under it. This claim is the existence result,
    written as a construction. CLAIM-285 keeps the rest and rests on it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction below: under the one-hop rule as stated, an
  operator whose authority depends on its own outgoing endorsements, or an
  ally with ‖p_j − p_i‖ < ‖p* − p_i‖ for whom raising E_ij does not bring the
  collective decision strictly nearer p_i.
tags:
- game-theory
- mathematics
date: '2026-10-19'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-282
uses:
- TERM-053
summary: >-
  The demonstrated core of [CLAIM-285](CLAIM-285.md). Under A3's one-hop rule
  I_j = I_j⁰ + Σ_(k≠j) b_k E_kj, with budgets and baselines fixed within an
  epoch ([CLAIM-282](CLAIM-282.md)), an operator's authority does not respond to its own
  endorsements. If the collective decision is the authority-weighted mean
  of the operators' policies, then endorsing an ally whose policy is nearer
  one's own than the decision is moves the decision strictly toward one's
  policy. So the reward for realized policy, and not for held authority,
  pays for delegating. It does not say operators behave so, or that any
  rule beyond one hop keeps both conditions.
supports:
- CLAIM-285
---
<!-- inactive-ok-file: CLAIM-285 — Proposed; the incentive thesis this construction was split from and that rests on it, cited as open -->

# CLAIM-tmpso62d: Under one-hop allocation within an epoch, an operator that endorses an ally whose policy is nearer its own than the collective decision is raises how far its preferred policy is realized while its own authority stays fixed, so the two conditions of the endorsement scheme hold together

## The claim

Take operators 1, …, N with policies p_k in ℝᵈ and endorsements E_kj ≥ 0
for k ≠ j. Within an epoch, authority is allocated in one hop, as A3 §4
proposed ([CLAIM-282](CLAIM-282.md)):

I_j = I_j⁰ + Σ_(k≠j) b_k E_kj,

with budgets b_k > 0 and baselines I_j⁰ ≥ 0 fixed independently of the
endorsements made in the epoch. The collective decision is the
authority-weighted mean p* = Σ_j I_j p_j / S, with S = Σ_j I_j > 0.
Operator i's objective is J_i = −‖p* − p_i‖² − λ Cost(E_i), as in A2.

1. **Its authority is fixed.** I_i depends on E_ki for k ≠ i only, so
   ∂I_i/∂E_ij = 0 for every j. This is [CLAIM-282](CLAIM-282.md)'s one-hop case.
2. **Delegating to a nearer ally pays.** Let ‖p_j − p_i‖ < ‖p* − p_i‖.
   Raising E_ij by δ > 0 adds Δ = b_i δ to I_j and nothing else, so the new
   decision is p*′ = p* + t(p_j − p*) with t = Δ/(S + Δ) in (0, 1). The map
   f(t) = ‖p* + t(p_j − p*) − p_i‖² is convex, with f(1) < f(0). So
   f(t) ≤ (1 − t)f(0) + t f(1) < f(0): the decision is strictly nearer p_i.
   The same convexity gives f′(0) ≤ f(1) − f(0) < 0, so the gain has a
   positive rate at δ = 0. When λ times the marginal cost is below that
   rate, a small increase in E_ij raises J_i.

So A2's two conditions, an authority that does not respond to one's own
endorsements and a reward for how far one's preferred policy is realized,
hold at once. They constrain different quantities. That is [CLAIM-285](CLAIM-285.md)'s
point, stated as a construction.

## What it does not say

- **That operators delegate.** That operators bound by the constraint
  actually delegate, and do it better than at random, is a claim about
  behaviour. It is [CLAIM-285](CLAIM-285.md)'s.
- **Anything beyond one hop.** Under recursive delegation the first
  condition fails ([CLAIM-282](CLAIM-282.md)). Whether some other multi-hop rule keeps
  both conditions is open.
- **That the decision rule is the right one.** The weighted mean is one
  rule. A rule under which p* does not move toward an ally's policy as the
  ally's authority grows would need its own argument.
- **That endorsement cannot be gamed.** An operator can still change its
  authority by moving others' endorsements, which is social feedback, not
  an accounting loop ([CLAIM-282](CLAIM-282.md)). And an aligned ally can be incompetent
  (A2 §6).
