---
number: 1195
status: Proposed
formerly:
- CLAIM-tmpy25jo
title: 'In a linear model of maintained nuclei, holding a nucleus at a usable level costs its decay rate times that level over the efficiency of investment whether or not it is used, so the budget bounds how many can be held ready and restored funding always restores a nucleus; a threshold below which a funded nucleus is still lost appears only when building capability needs capability already present'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the averaging bound or in the equilibria of the sigmoidal
  model; or a recomputation in which a nucleus cut below the lower
  equilibrium recovers when its funding is restored.
tags:
- complex-systems
- operations-research
- society-and-governance
date: '2026-11-23'
line:
- learning-and-inquiry
- readiness
- transient-support
rests_on:
- CLAIM-1148
- CLAIM-605
- CLAIM-463
summary: >-
  A gap in A54 §4 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-23), filled. A54 models maintained nuclei as ċ = αu − δc under a
  shared budget, says the linear model "doesn't yet exhibit genuine
  nucleation", and conjectures "a possible critical conceptual nucleus",
  citing [CLAIM-605](CLAIM-605.md) and [CLAIM-463](CLAIM-463.md) for thresholds. Here: what the linear
  model does give, the standing cost of readiness and the bound it puts on
  how many nuclei can be held, and the smallest change that yields A54's
  threshold, each checked with python3 -I. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1148 CLAIM-921 CASE-386 — Proposed; the claim whose gap this fills, the budget rule and the case read against it -->

# CLAIM-1195: In a linear model of maintained nuclei, holding a nucleus at a usable level costs its decay rate times that level over the efficiency of investment whether or not it is used, so the budget bounds how many can be held ready and restored funding always restores a nucleus; a threshold below which a funded nucleus is still lost appears only when building capability needs capability already present

## The gap

A54 §4 ([CLAIM-1148](CLAIM-1148.md)): ċ_i = α_i u_i − δ_i c_i, Σ u_i + u_coord ≤ B.
"Some might require only a small maintenance allocation to remain usable";
"The linear maintenance model doesn't yet exhibit genuine nucleation. A
stronger model would have a threshold below which a developing perspective
cannot sustain the activity needed to reproduce its own capabilities."
A54 neither prices the maintenance nor writes the stronger model.

## The linear model

- **The cost of readiness.** Integrating, c(T) − c(0) = α∫u − δ∫c. If c
  stays at or above a usable level c̄ on [0, T], then
  c(T) ≤ c(0) + T(αū − δc̄), with ū the average funding, so a nucleus can
  be held at c̄ indefinitely only if ū ≥ δc̄/α. The cost is set by the
  decay rate and the level, and is owed whether or not the nucleus is used.
- **How many.** Holding nuclei i = 1, …, n ready needs
  Σ δ_i c̄_i/α_i ≤ B − u_coord. A54's "maintain many conceptual nuclei
  while actively developing only a selected subset" is bounded by this sum,
  and fast-decaying nuclei (skills kept by practice) are dearer to hold
  than slow ones (a written method), however rarely either is used.
- **No threshold.** From any c the funded nucleus tends to αu/δ. Funding
  restored after any lapse restores the nucleus, so [CLAIM-463](CLAIM-463.md)'s
  irreversibility cannot occur in it.

## The smallest change that gives a threshold

Make building capability need capability already present, as in
[CLAIM-605](CLAIM-605.md)'s learning by doing: ċ = αu·c²/(c² + K²) − δc. Then c = 0 is
always stable (slope −δ there), and the other equilibria solve
δc² − αuc + δK² = 0. They exist when αu ≥ 2δK; the lower root
c₋ = [αu − √(α²u² − 4δ²K²)]/(2δ) is the threshold and the upper c₊ the
maintained level. A nucleus below c₋ decays to nothing even while funded,
and one cut off long enough to fall below c₋ is not restored by restoring
its funding: [CLAIM-463](CLAIM-463.md)'s case.

## The check

With python3 -I (Euler steps of 0.01):

- Linear, α = 1, δ = 0.1: from c₀ = 0, 1 and 5 the level tends to αu/δ
  (0.5 at u = 0.05, 2.0 at u = 0.2). With random funding averaging 0.9 of
  δc̄/α, a nucleus started at c̄ = 2 ends at 1.61.
- Sigmoidal, K = 1: at u = 0.15 (below 2δK/α = 0.2) every start decays to
  0; at u = 0.25 the roots are 0.5 and 2.0, and starts at 0.2 decay while
  starts at 1, 2 and 5 reach 2.0; at u = 0.4 the roots are 0.268 and 3.732.
- Hysteresis at u = 0.4: from 3.732, funding cut for 26 time units leaves
  0.277 and restoring it returns the nucleus to 3.732; cut for 27 leaves
  0.250, below c₋, and restoring it returns nothing. The predicted cut-off,
  ln(3.732/0.268)/δ, is 26.3.

## What it does not say

- Not that perspectives have such a threshold. A54: "We should not assume
  every perspective has such a threshold. That is a mechanism to test." The
  sigmoidal form is one assumption that gives it.
- Not how the budget is set. If it follows observed use, [CLAIM-921](CLAIM-921.md) shows a
  rarely used capability can be lost whatever each use was paid, which is
  the manager of [CASE-386](../cases.d/CASE-386.md) funding only what is used now.
