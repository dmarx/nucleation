---
number: 502
status: Active
formerly:
- CLAIM-tmphnxf0
title: 'Multi-hop delegation can keep an operator''s authority exactly independent of its own endorsements: under leave-one-out damped delegation, which counts the authority reaching each operator only along paths that have not already passed through it, an operator''s endorsements raise the authority of every operator the endorsed one reaches and leave its own unchanged'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed Active by the nineteenth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-057). The eighteenth
    review found the construction (p18/cluster_da_checks.py, part B); the
    nineteenth re-derived it and checked it independently, with controls
    (p19/claim282_loo.py). It shows CLAIM-282's old title false, and
    CLAIM-282 is narrowed in the same change (ADR-047, kind 3; ADR-059).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction below: a graph, a damping 0 < η < 1 and
  positive budgets under which operator i's authority, computed by the
  rule as stated, changes when i's own row of endorsements changes with
  every other row fixed. Or a case in which raising E_ij, every other
  entry fixed, lowers the authority of any operator, or leaves unchanged
  that of an operator k other than i that j reaches by a path of
  positive endorsements.
tags:
- self-governance
- mathematics
date: '2026-10-30'
works:
- self-as-recursive-ecology
line:
- distributed-agency
- formal-apparatus
objects_to:
- CLAIM-282
uses:
- TERM-053
complements:
- CLAIM-375
summary: >-
  A construction that shows [CLAIM-282](CLAIM-282.md)'s old title false. Compute each
  operator's authority from A2's damped recursive rule with that
  operator's own outgoing endorsements removed. Then authority reaches it
  along paths of any length, but only along paths that have not passed
  through it, so nothing it endorses can return to it. Its authority is
  exactly independent of its own endorsements, and an endorsement moves
  authority two hops and more. It does not say the rule conserves
  authority, that it closes the social route of moving others'
  endorsements, or that [CLAIM-375](CLAIM-375.md)'s guarantee carries over.
---
<!-- inactive-ok-file: CLAIM-285 — Proposed; the incentive thesis this construction bears on, cited as open -->

# CLAIM-502: Multi-hop delegation can keep an operator's authority exactly independent of its own endorsements: under leave-one-out damped delegation, which counts the authority reaching each operator only along paths that have not already passed through it, an operator's endorsements raise the authority of every operator the endorsed one reaches and leave its own unchanged

## The claim

Take operators 1, …, N with budgets b_k > 0, endorsements E_kj ≥ 0 with
E_kk = 0 and each row summing to at most 1, and a damping 0 < η < 1.
[CLAIM-282](CLAIM-282.md)'s damped recursive rule is g = (1 − η)(I − ηEᵀ)⁻¹b, and under it
an operator's authority depends on its own endorsements through every
cycle through it.

**The rule.** Let E₍₋ᵢ₎ be E with row i, i's own outgoing endorsements, set
to zero. Operator i's authority is g_i = [(1 − η)(I − ηE₍₋ᵢ₎ᵀ)⁻¹b]_i. Each
operator's authority is read from the recursive rule on a graph in which
it endorses no one.

1. **What it counts.** Expanded as a series, g_i is (1 − η)b_i plus, for
   every walk of endorsements that ends at i and does not visit i before
   its end, (1 − η)b_s η^ℓ times the product of the endorsements along it,
   s being the walk's start and ℓ its length. Authority reaches i along
   paths of any length, and cycles that avoid i still feed it. What never
   reaches i is authority that has already passed through i, its own
   budget included. In [CASE-077](../cases.d/CASE-077.md)'s pair, g₁ = (1 − η)b₁ + η(1 − η)b₂,
   against (b₁ + ηb₂)/(1 + η) under the recursive rule. Where no cycle
   passes through i, g_i is its value under the recursive rule.
2. **Its own endorsements do not move it.** E₍₋ᵢ₎ does not contain row i,
   so g_i is a function of the other rows and of b alone. This is exact
   independence, not a vanishing derivative: any change to i's
   endorsements, of any size, leaves g_i where it was.
3. **Its endorsements carry beyond one hop.** For k ≠ i, let
   M = (I − ηE₍₋ₖ₎ᵀ)⁻¹, whose entries are non-negative. Then
   ∂g_k/∂E_ij = (1 − η)η M_kj (Mb)_i, with (Mb)_i ≥ b_i > 0, and M_kj > 0
   exactly when j reaches k by a path of positive endorsements. So raising
   E_ij raises the authority of j and of every operator j reaches, however
   many hops away. It lowers no one's, and it leaves i's own unchanged.

So an operator's authority can be independent of its own endorsements
while endorsement carries authority further than one hop.

## The check

p19/claim282_loo.py (numpy) checks each step on random graphs, with
controls:

- **Step 2.** Redrawing i's whole row moved g_i by exactly 0 in 300
  graphs. The recursive rule moved it by up to 0.58, and the one-hop rule
  by 0.
- **Step 1.** An absorbing-walk computation with no inverse agrees with
  the formula to 6e-16. The pair and the no-cycle cases match their closed
  forms.
- **Step 3.** Raising E_ij raised every reachable k ≠ i, 1,325 cases, and
  lowered none. The 213 unreachable operators stayed put. Two hops out,
  the one-hop rule gives zero.

The eighteenth review's script (p18/cluster_da_checks.py, part B) found
the same by finite differences. The derivative in step 3 was re-derived by
hand at the nineteenth review's ruling.

## What it does not say

- **That authority is conserved.** Each operator's authority is read off a
  different graph, so the vector is not one fixed point. In the check the
  total ran from 17% to 99.7% of the budgets, where the recursive rule
  keeps it equal to them. A2 said the same of its path-based rule with
  origin tags ([CLAIM-282](CLAIM-282.md)), whose open conventions this rule may be one way
  to fix.
- **That it closes the social route.** g_i still depends on what others
  endorse, so an operator can change its authority by changing what others
  endorse ([CLAIM-282](CLAIM-282.md)).
- **That delegating to a nearer ally pays, as under one hop.** [CLAIM-375](CLAIM-375.md)'s
  guarantee does not carry over. Raising an endorsement of an ally nearer
  the endorser's policy than the authority-weighted decision moved the
  decision toward the endorser in 1,772 of 2,141 trials, against all 2,138
  under one-hop allocation. The added authority also flows on from the ally
  to those it endorses. Whether the incentive still does work is
  [CLAIM-285](CLAIM-285.md)'s question.
- **That it is a cycle ban.** The graph keeps its cycles. Only each
  operator's own accounting stops at its boundary, so [CLAIM-282](CLAIM-282.md)'s point
  about cycle bans stands.
