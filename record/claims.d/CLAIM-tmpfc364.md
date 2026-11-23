---
status: Proposed
title: "A response kernel that includes the organization's state after answering is not an observational quantity: compared directly, it separates any two organizations whose post-states differ, even when no test could tell them apart, so the developmental comparison should observe the post-state only through its later responses, as a bisimulation pseudometric does, which keeps the separation of a learning and a suppressing organization"
version: 1
role: counter
warrant: demonstrated
defeated_if: >-
  An error in the construction below; or a metric on organizational states,
  fixed independently of their responses, under which A64b's d_𝒬 is
  zero for the first pair of the construction and positive for the
  second.
tags:
- probabilistic-modeling
- individuation
- mathematics
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
objects_to:
- CLAIM-tmpq1usu
grounds:
- THEORY-247
uses:
- TERM-tmpwc4la
bears_on:
- QUESTION-384
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A64b §4 of the exchange "Explain First Contact
  RL" (ChatGPT, the branch of 2026-11-23 08:51), whose observational
  distance d_𝒬(S, T) compares kernels K_S(q) = Law(a, τ, c, S′ | do(q), S)
  that include the next state S′. It objects to that formal step, not to
  [CLAIM-tmpq1usu](CLAIM-tmpq1usu.md)'s thesis, and gives the repair the record already holds:
  the bisimulation metric ([THEORY-247](../theory.d/THEORY-247.md)). Checked by script (python3 -I). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CLAIM-615 CLAIM-tmpq1usu TERM-tmpwc4la — Proposed; entries filed from this exchange or neighbours cited, not leaned on as in force -->

# CLAIM-tmpfc364: A response kernel that includes the organization's state after answering is not an observational quantity: compared directly, it separates any two organizations whose post-states differ, even when no test could tell them apart, so the developmental comparison should observe the post-state only through its later responses, as a bisimulation pseudometric does, which keeps the separation of a learning and a suppressing organization

## The gap

A64b §4 calls d_𝒬(S, T) = sup_{q∈𝒬} d_resp(K_S(q), K_T(q)) an "observational distance" that "measures how similarly the organizations respond and develop under the available tests". The kernel includes S′, the organization's next state. To compare two laws over S′ one needs a metric on states, and A64b leaves it open. If S′ is compared directly, as a state, the distance stops being observational. Two organizations whose next states differ in any respect are apart, whether or not any test in 𝒬, now or later, could tell those states apart. The intended relativity to the test family, the record's ([TERM-tmpwc4la](../terms.d/TERM-tmpwc4la.md), [CLAIM-574](CLAIM-574.md)), is lost.

## The construction

Two queries: a familiar q0 and a novel q1. Each state answers each query adequately with a stated probability and moves deterministically to a next state.

- **s and t.** Both answer q0 with 0.9 and q1 with 0.2 and move to s1 and t1. These are distinct states that answer as s and t do and stay where they are. No test can tell s from t, at any depth.
- **u and v.** Both answer as s does now. u moves to u1, which answers q1 with 0.7 (it learned); v moves to v1, which answers q1 with 0.1 (it suppressed).

Distances, in this session's script (python3 -I), with the answer term the total-variation distance between the adequacy laws:

| pair | answers only | S′ compared directly (discrete metric) | bisimulation, γ = 0.9 |
|---|---|---|---|
| s, t | 0 | 1 | 0 |
| u, v | 0 | 1 | 5.4 (0.54 scaled by 1 − γ) |

Answers alone miss the u, v difference, which is A64b's point. Comparing S′ directly finds it, but also finds an s, t difference no test can find. The bisimulation metric gets both right.

## The repair

Let the metric on states be the one the kernel itself induces: d(S, T) = max over q of [d_answer(S, T; q) + γ W_d(law of S′ from S, law of T′ from T)], where W_d is the optimal-transport distance under d itself. This is the discounted bisimulation metric, the fixed point of Ferns and colleagues' equation, which the record holds as [THEORY-247](../theory.d/THEORY-247.md) (Calo et al.: it is a bicausal optimal-transport distance and is computable by a linear program on finite chains). It observes S′ only through what S′ will answer, so it is zero for observationally equivalent organizations and positive for the learning and suppressing pair. Restricting the queries to 𝒬 at every step keeps it relative to the declared family, as A64b intended.

## What it leaves

- A64b's further point stands and needs no metric: "Two independently formed organizations might have identical response kernels without being the same historically continuous organization." With the repair, duplicates are at distance zero, and their difference is historical ([CLAIM-615](CLAIM-615.md)), as A64b says.
- [QUESTION-384](../questions.d/QUESTION-384.md) asks when profile-based and bisimulation distinctions agree for resource-graded systems; this is one place the answer would be used.
