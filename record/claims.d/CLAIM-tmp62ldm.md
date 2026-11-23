---
status: Proposed
title: 'In the robust interrogation game the worst query distribution against any fixed response policy is a single query, and when each query can be answered on its own the game reduces to the worst query''s best response; it is a game, with a mixed query strategy at equilibrium, only when one prepared policy must serve several queries through shared state or resources, or when the permitted query distributions are restricted'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a policy set Π(S) that is a product over queries
  (each query's response chosen apart from the others) and an unrestricted
  𝒫(Q) for which inf over π of sup over ρ of E[ℓ] differs from the largest
  over q of the best achievable loss on q; or a fixed policy whose worst
  distribution in an unrestricted 𝒫(Q) is not attained at a point mass.
tags:
- game-theory
- operations-research
- mathematics
date: '2026-11-23'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-tmp2oloi
bears_on:
- QUESTION-tmpn4we1
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A50 §3 of the exchange "Explain First Contact RL"
  (2026-11-23), which titles itself "Make it a genuine two-player game" and
  writes inf over π, sup over ρ, of expected loss without saying what makes
  it a game rather than worst-case design. The ledger's gap: whether it is
  a game at all, and what its equilibrium is. Argued in [ARG-tmpo1l8y](../arguments.d/ARG-tmpo1l8y.md) and
  checked with python3 -I. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp2oloi ARG-tmpo1l8y — Proposed; the formulation this analyses and the argument for it, filed with it -->

# CLAIM-tmp62ldm: In the robust interrogation game the worst query distribution against any fixed response policy is a single query, and when each query can be answered on its own the game reduces to the worst query's best response; it is a game, with a mixed query strategy at equilibrium, only when one prepared policy must serve several queries through shared state or resources, or when the permitted query distributions are restricted

## The gap it fills

A50 §3 writes the game as inf over π ∈ Π(S) of sup over ρ ∈ 𝒫(Q) of
E[ℓ(q, a)], q ~ ρ, a ~ P_π(· | q, S) ([CLAIM-tmp2oloi](CLAIM-tmp2oloi.md)), under the heading
"Make it a genuine two-player game". It does not say what the query side's
distribution adds, when the formula is strategic, or what its equilibrium
is.

## The result

Write L(π, q) for the expected loss of policy π on query q. Then
E[ℓ] = Σ_q ρ(q) L(π, q) is linear in ρ.

1. **Against a fixed policy the worst distribution is a point mass.** A
   linear function on the simplex is maximized at a vertex, so with
   𝒫(Q) unrestricted, sup over ρ = max over q of L(π, q), and the value is
   inf over π of max over q of L(π, q).
2. **With answers chosen query by query, nothing is strategic.** The
   response a ~ P_π(· | q, S) is conditioned on q. If Π(S) lets each
   query's response be chosen apart from the others, the infimum splits,
   and the value is max over q of (the best achievable loss on q): each
   query is a separate design problem and the worst one sets the value.
3. **It is a game when one policy must serve several queries.** When the
   responses draw on shared state or resources fixed before the query is
   known, as reserves, trained staff and infrastructure are, the respondent
   cannot optimize each query separately. Its best policy hedges across
   queries, and, the loss being convex in a mixed or divisible policy, the
   minimax theorem gives the query side an equilibrium mixed strategy. This
   is the readiness setting of [TERM-115](../terms.d/TERM-115.md): preparation is chosen before the
   contingency arrives.
4. **Or when 𝒫(Q) is restricted.** A testing budget, a requirement of
   diversity or a legitimacy constraint that excludes concentrating on the
   worst query makes the sup a constrained linear programme whose solution
   is mixed. This is the formal place of A50's "The query side itself needs
   justified constraints."

So the game's strategic content lies in the coupling of responses across
queries through the target's shared state, and in what the query side is
permitted, not in the minimax form as such. It is a zero-sum game, with
the minimax value as its solution, only in its adversarial form; the
diagnostic and developmental forms need a query-side payoff of their own
([QUESTION-tmpn4we1](../questions.d/QUESTION-tmpn4we1.md)).

## The check

`python3 -I`, numpy and scipy, on 2026-11-23. Three queries with weights
w = (1, 0.6, 0.3), a respondent preparing capacities x on the simplex
before the query (shared budget), loss w_i(1 − x_i):

- the prepared value inf over x of max over i was 0.375, with losses
  equalized across queries (the hedge of point 3);
- over 5,000 sampled distributions ρ, none exceeded the point-mass maximum
  for any x (point 1);
- with each query answered separately and given the full budget, the value
  was 0 (point 2);
- with ρ restricted to ρ_i ≤ 0.5, solved by linear programming, the value
  fell to 0.362 (point 4).

## Standing

Proposed, the assistant's.
