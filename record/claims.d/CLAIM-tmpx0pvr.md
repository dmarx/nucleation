---
status: Proposed
title: 'In a percept–action loop, the nostalgia of a memory depends on the policy that uses it and not only on what it keeps: a memory of the context, used to make the action succeed, leaves no trace of itself in the next percept and is wholly nonpredictive, while the same memory left unused can be wholly predictive, and its heat per step is the same either way, so under feedback nostalgia is neither a property of the memory nor its cost'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation such that, corrected, the memory's nostalgia
  in the toy loop does not change with the policy, or its heat per step
  does; or a proof that in every feedback loop with a fixed memory map and
  a kernel that keeps each equilibrium stationary the nostalgia is fixed by
  the map. A loop in which the two happen to coincide does not defeat it.
tags:
- thermodynamics
- information-theory
- agency
- causality
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
grounds:
- CASE-tmp3axlj
- THEORY-026
bears_on:
- QUESTION-494
summary: >-
  From [CASE-tmp3axlj](../cases.d/CASE-tmp3axlj.md)'s loop. Percepts are a fresh context u, a sticky
  nuisance v and the outcome y of the last action, which succeeds when it
  matches u. A memory that keeps u and acts on it makes every outcome a
  success, so the next percept says nothing about u: its nostalgia is its
  whole content, ln 2 per step in the noiseless limit. The same memory with
  the action fixed lets the outcome reveal u, and its nostalgia is 0. Its
  heat per step is the same, because the policy only moves dissipation
  between the switch and the relaxation. Without feedback a memory's
  nostalgia is fixed by the memory and the drive; with feedback the use
  that makes the memory worth having is what makes it nonpredictive. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmp3axlj — filed by the lead run of 2026-11-23 -->

# CLAIM-tmpx0pvr: In a percept–action loop, the nostalgia of a memory depends on the policy that uses it and not only on what it keeps: a memory of the context, used to make the action succeed, leaves no trace of itself in the next percept and is wholly nonpredictive, while the same memory left unused can be wholly predictive, and its heat per step is the same either way, so under feedback nostalgia is neither a property of the memory nor its cost

## The claim

In [CASE-tmp3axlj](../cases.d/CASE-tmp3axlj.md)'s loop the percept is (u, v, y). u is a fresh fair coin,
v is sticky, and y' = [a = u], flipped with probability δ. The memory keeps
u, stored with an energy gap and re-equilibrated after each switch.

| policy | success | I[s;x_t] | I[s;x_{t+1}] | nostalgia | heat per step |
|---|---|---|---|---|---|
| a = u (δ = 0, gap 30) | 1 | ln 2 | 0 | ln 2 | equal |
| a = 0 (δ = 0, gap 30) | ½ | ln 2 | ln 2 | 0 | equal |
| a = u (δ = 0.05, gap 6) | 0.948 | 0.676 | 0.000 | 0.676 | 2.985 |
| a = 0 (δ = 0.05, gap 6) | 0.500 | 0.676 | 0.488 | 0.188 | 2.985 |

The first two rows are tested exactly in scratch/studies/lead-005/.

## Why it matters for the question

[THEORY-026](../theory.d/THEORY-026.md)'s slogan, that only nonpredictive memory is wasteful, ranks
memories by what they keep. Under feedback the ranking is not available:
the next percept depends on the action, so whether a memory predicts it
depends on what is done with the memory. Here acting well on a memory
erases its trace from what comes next. A cost criterion for [QUESTION-494](../questions.d/QUESTION-494.md)
built on the per-switch nostalgia would charge the memory for being used
well. The total heat per step in this loop is set by how often the memory
must be rewritten, which the policy does not change.

## Limits

- One loop, built so the effect is clean. The claim is that the dependence
  exists, not how large it is elsewhere.
- The heat per step is that of a sudden switch with full
  re-equilibration. That it is unchanged by the policy follows from the
  memory's rewriting being driven by u alone; a memory whose rewriting
  depended on the outcome would differ.
