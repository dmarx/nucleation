---
number: 1097
status: Proposed
formerly:
- CLAIM-tmpg5p8v
title: For demands on the configuration held at the horizon, the history complex
  over horizon H at a capacity budget B is the configuration complex restricted
  to the configurations reachable from the start within H at B, when holding a
  configuration is an admissible move and the attainable histories are exactly
  the move sequences that stay within B; without holding, or with demands met
  at different times, the two differ
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the derivation; or an architecture with one capacity held
  at each moment, holding admissible, attainable histories exactly the budgeted
  move sequences and every demand a condition on the configuration at H, whose
  history complex differs from the configuration complex restricted to the configurations
  reachable within H.
tags:
- mathematics
- operations-research
- society-and-governance
date: '2026-11-23'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-347
- CLAIM-560
summary: 'A gap fill: a gap of the manuscript governance-of-possibility, §2.4 (GA1),
  which identifies the history-indexed complex of [CLAIM-347](CLAIM-347.md) with the configuration-indexed
  filtrations of [CLAIM-560](CLAIM-560.md) "without proof". As the manuscript states it the identification
  holds only under three conditions, which the title names; two counterexamples
  show what fails without them. Checked by enumeration with python3 -I. The wording
  is the assistant''s (Claude, in this session); adopting it is the owner''s call.'
---

# CLAIM-1097: For demands on the configuration held at the horizon, the history complex over horizon H at a capacity budget B is the configuration complex restricted to the configurations reachable from the start within H at B, when holding a configuration is an admissible move and the attainable histories are exactly the move sequences that stay within B; without holding, or with demands met at different times, the two differ

## The derivation

Take [CLAIM-560](CLAIM-560.md)'s architecture: configurations Q, moves between them, a
capacity requirement r held at each moment, Q(B) = {q : r(q) ≤ B}, and a
start q₀ ∈ Q(B). Take [CLAIM-347](CLAIM-347.md)'s complex indexed by horizon and budget,
𝒦(𝒪; D, H, B) = {S ⊆ D : ℛ(𝒪; H, B) ∩ ⋂_{i∈S} A_i ≠ ∅}. Three conditions:

1. **Demands on the configuration reached.** Each demand i is a condition on
   the configuration at H: A_i = {h : h_H ∈ C_i} for a set C_i ⊆ Q.
2. **Holding is a move.** From each configuration, staying put is admissible.
3. **Attainable means budgeted.** ℛ(𝒪; H, B) is exactly the sequences
   q₀ q₁ … q_H of moves (or holds) with every q_t in Q(B).

Let Reach_H(B) be the configurations reachable from q₀ in at most H moves
through Q(B), q₀ included. Under 1, S is a face exactly when some
attainable history ends in ⋂_{i∈S} C_i, that is, when the set of end
points {h_H : h ∈ ℛ} meets ⋂ C_i. Under 2 and 3 that set of end points is
Reach_H(B): a configuration reached in k ≤ H moves is held for the
remaining H − k periods, and every end point is reached in at most H
moves. So

  𝒦(𝒪; D, H, B) = {S : Reach_H(B) ∩ ⋂_{i∈S} C_i ≠ ∅},

which is [CLAIM-560](CLAIM-560.md)'s K(B) with Q(B) replaced by Reach_H(B). Since
Reach_H(B) ⊆ Q(B), the history complex is always contained in K(B). They
are equal when every face of K(B) is met by a reachable configuration, and
they differ exactly where [CLAIM-560](CLAIM-560.md)'s "feasible and unreachable" bites.
For H at least the number of configurations, Reach_H(B) is q₀ with
everything (q₀, q) joins in [CLAIM-560](CLAIM-560.md)'s R(B).

## Where it fails

- **Without holding.** [CLAIM-560](CLAIM-560.md)'s row s₁ — s₂ — s₃ with r = (1, 3, 1),
  B = 3, H = 2 and no hold: the histories are s₁s₂s₁ and s₁s₂s₃. A demand
  met only at s₂ is a face of the restricted configuration complex (s₂ is
  reachable within 2) and not of the history complex (no history ends
  there). "Within H" and "at H" come apart.
- **Demands met at different times.** Same row, holding allowed, with
  "at some time in s₁" and "at some time in s₃": the history s₁s₂s₃ meets
  both, and no configuration meets both, so {1, 3} is a face of the history
  complex and not of the configuration complex. Demands on a whole history,
  such as persistence throughout H ([CLAIM-347](CLAIM-347.md)'s note of 2026-11-04) or a
  response by a deadline, are not conditions on a configuration at all.
- **A cumulative budget.** If B bounds a sum along the history rather than
  what is held at each moment, reachability within B is not closed under
  composition ([CLAIM-563](CLAIM-563.md)), and the restriction has to be to histories.
- **A policy.** If ℛ is restricted to the histories the organization's
  actual policy produces, the restriction is to the configurations reached
  under that policy, not to all that are reachable.

## The check

With python3 -I, by enumeration: 3,000 random architectures (two to six
configurations, requirements in {1, 2, 3}, random moves, one to four
demands as sets of configurations, budgets 1 to 3, horizons 0 to 4), the
history complex over terminal demands against the configuration complex
restricted to Reach_H(B). With holding allowed there were no mismatches.
The two counterexamples above were reproduced: without holding the history
complex is {∅} and the restricted complex {∅, {2}}; with demands met at
some time, {1, 3} is a history face only.

## What it does not say

- Not that the configuration formulation can replace the history one: for
  the manuscript's deadline and persistence demands it cannot.
- Nothing for several resources ([CLAIM-585](CLAIM-585.md)).

## Gap filled

A gap of the manuscript governance-of-possibility, §2.4 (GA1): "the
history complex over horizon H should be the configuration complex
restricted to configurations reachable from the start within H at budget
B". True under conditions 1 to 3, and not otherwise.
