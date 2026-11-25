---
number: 951
status: Proposed
formerly:
- CLAIM-tmpk6abl
title: 'A partial loop can need more outside supply'
statement: >-
  Where a nucleus makes the constraint of its own formation from the
  material its formation also draws on, a loop that falls short of closing
  can need more outside supply of the constraint than no loop at all, so the
  share of the constraint a nucleus makes for itself is not a measure of
  progress toward closure: in one kinetic construction the loop cut the
  supply needed only while turnover stayed below about 0.73, where what it
  made equalled the extra constraint needed to offset its draw on material
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-093, from the
    runs of CASE-365.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in CASE-365's e3: at k_T = 1 and N = 2, a teacher
  supply with the loop (β = 0.02) that is not larger than without it
  (β = 0), recomputed from the steady-state equations. Not defeated by
  systems where the constraint is made from a material formation does not
  use, where the claim predicts the loop always helps, nor by loops that
  close, where the supply needed is zero.
tags:
- complex-systems
- individuation
- mathematics
date: '2026-11-22'
line:
- transient-support
- distributed-agency
grounds:
- CASE-365
bears_on:
- QUESTION-399
summary: >-
  A partial loop is not partway to a closed one. In [CASE-365](../cases.d/CASE-365.md) the
  nuclei's own teacher production competes with formation for material.
  Above a turnover of about 0.73, holding two nuclei takes more outside
  teacher with the loop than without it, though the nuclei then make 10
  to 18 % of their teachers themselves (k_T from 0.85 to 1.5). The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-365 — new; the run this claim is drawn from -->

# CLAIM-951: A partial loop can need more outside supply

## The claim

In [CASE-365](../cases.d/CASE-365.md), consider holding N = 2 nuclei in steady state. The
model with the loop (β = 0.02) and without it (β = 0) need different
outside teacher supplies:

| k_T | with the loop | without | self-made share |
|---|---|---|---|
| 0.15 | 0 | 0.173 | 1 |
| 0.25 | 0.138 | 0.289 | 0.62 |
| 0.4 | 0.358 | 0.462 | 0.39 |
| 0.7 | 0.799 | 0.808 | 0.22 |
| 1.0 | 1.239 | 1.154 | 0.16 |

**Why.** Making teachers uses material that formation also needs. With
the loop, material sits at 5.71 rather than 8.0. So more teacher is needed
to form the same nuclei: 1.467 against 1.154.

**The crossover.** The loop pays while what it makes, βmN = 0.229,
exceeds what that extra teacher costs to keep, k_T(1.467 − 1.154). That
holds below k_T ≈ 0.73.

**What follows.** A rising self-made share is not, by itself, progress
toward closure. It can come with a larger dependence on outside supply.

## What it does not say

- **Not every partial loop costs.** Where the constraint is made from a
  material that formation does not use, or where material is plentiful,
  the loop only helps.
- **No general crossover value.** The value 0.73 is this model's, at
  N = 2.
