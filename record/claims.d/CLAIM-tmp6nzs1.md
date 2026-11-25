---
status: Proposed
title: "Where a party's fallback is a capacity learned by doing that needs capacity already present to grow, and its terms are bargained against that fallback, substitutive supply moves the terms against the party while it never exits; ending the supply reverses the movement up to the capacity's deadline and not after it, and under capacity-first supply, or where the party cannot exit, the decay does not move the terms"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in
  scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py
  whose correction, at the parameters run, leaves the party's Nash share
  unchanged under full substitutive supply; lets supply ended after
  CLAIM-605's deadline restore the fallback; or moves the share under
  capacity-first supply or with no exit. Or a showing that the outside
  option of a party whose capacity follows CLAIM-605's model is not
  monotone in that capacity under any valuation of its stand-alone path,
  so that the decay need not lower it. Not defeated by parameters under
  which the fall is gradual rather than a step at the deadline, which
  the claim does not assert; nor by the absence of a measured case, since
  the claim is about the model.
tags:
- game-theory
- society-and-governance
- complex-systems
date: '2026-11-25'
line:
- dependence-and-domination
- transient-support
rests_on:
- CLAIM-605
grounds:
- CASE-264
complements:
- CLAIM-tmp2jhc1
- CLAIM-670
summary: >-
  The assistant's computation for the manuscript governance-of-becoming,
  Article 9 §9.4 (gap G9.1, join J9.1), filed under write-manuscript step
  6. The record held a capacity that decays under substitutive supply
  ([CLAIM-605](CLAIM-605.md)) and a Nash split that moves with an outside option set by
  hand ([CASE-264](../cases.d/CASE-264.md)'s arm A; [CLAIM-tmp2jhc1](CLAIM-tmp2jhc1.md)), and no model joining them.
  Here P's outside option is valued from its decaying capacity: over six
  time units of full substitution P's share falls from 6.000 to 4.199
  with no exit and no term rewritten; supply ended before the deadline
  restores the fallback toward 4, and after it leaves it at 0.041 or
  0.003; capacity-first supply and the no-exit arm move nothing. Checked
  with python3 -I; the script asserts its figures and prints "checks
  pass". It answers, for a scalar capacity under both of its readings,
  the item [LEAD-tmpeo8wq](../leads.d/LEAD-tmpeo8wq.md) left open. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CASE-264 CLAIM-tmp2jhc1 CLAIM-670 CLAIM-690 TERM-123 TERM-124 — Proposed or new; the bargaining case, the claims this complements, and the terms a verdict of exploitation or domination would need, cited with their standing -->

# CLAIM-tmp6nzs1: Where a party's fallback is a capacity learned by doing that needs capacity already present to grow, and its terms are bargained against that fallback, substitutive supply moves the terms against the party while it never exits; ending the supply reverses the movement up to the capacity's deadline and not after it, and under capacity-first supply, or where the party cannot exit, the decay does not move the terms

## The gap it fills

[CLAIM-605](CLAIM-605.md) (Active, demonstrated) holds capacity learned by doing,
dC/dt = λPC(1 − C) − μC, under substitutive support P = min(τC, 1 − A)
or capacity-first support P = min(τC, 1), with a deadline after which
withdrawal no longer restores capacity. [CASE-264](../cases.d/CASE-264.md)'s arm A and
[CLAIM-tmp2jhc1](CLAIM-tmp2jhc1.md) hold the symmetric Nash split, u_P = o_P + (S − o_P − o_R)/2,
in which each unit of outside option moves half a unit of the split
whether or not it is used. In both, the outside option is a number set
by hand. No entry put the first under the second, so the record had no
model of terms moving as the fallback decays. The manuscript's digest
searched by mechanism and found the joint dynamics "not done"; no
account declines the join. [LEAD-tmpeo8wq](../leads.d/LEAD-tmpeo8wq.md), in its first note of
2026-11-24, keeps open "whether solo reach's shrinkage, not a price,
moves the terms the other can offer".

## The construction

The script is
`scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py`,
with its README beside it; its output of 2026-11-25 is
`analysis/fallback_decay_bargaining.2026-11-25.txt`. Run with
`python3 -I`; deterministic.

- **Capacity**: [CLAIM-605](CLAIM-605.md)'s model and parameters, λ = 1, μ = 0.3,
  τ = 1.5. Under full substitution C(t) = 0.7e^(−0.3t). The script
  recovers the threshold 0.2764, the kept state 0.7 and the deadline
  3.098.
- **Bargain**: [CASE-264](../cases.d/CASE-264.md)'s arm A, S = 10, o_R = 2. The script recovers
  [CASE-264](../cases.d/CASE-264.md)'s 4 and 6 at o_P = 0 and [CLAIM-tmp2jhc1](CLAIM-tmp2jhc1.md)'s 8, 9 and 10.
- **Fallback**: o_P(t) is w times the annuitized, discounted value of P's
  stand-alone output min(τC_s, 1), with C_s following the unsupported
  dynamics from C(t). Added, and invented: w = 4, r = 0.25 and a horizon
  of 80, fixed before the run. A second valuation, current output only,
  w·min(τC, 1), is reported beside it. They answer the two readings
  [LEAD-tmpeo8wq](../leads.d/LEAD-tmpeo8wq.md)'s second note of 2026-11-24 leaves open: current output
  to capacity as the actor's state, the forward value, nearer, to a
  cost of reaching that includes rebuilding the capacity.

## Results (r = 0.25 unless stated)

| t | C(t) | o_P, forward | u_P | o_P, current output | u_P on it |
|---|---|---|---|---|---|
| 0 | 0.700 | 4.000 | 6.000 | 4.000 | 6.000 |
| 2.0 | 0.384 | 2.954 | 5.477 | 2.305 | 5.153 |
| 3.0 | 0.285 | 1.817 | 4.908 | 1.708 | 4.854 |
| 4.0 | 0.211 | 0.942 | 4.471 | 1.265 | 4.633 |
| 6.0 | 0.116 | 0.399 | 4.199 | 0.694 | 4.347 |

1. **The terms move with no exit and no term rewritten.** P's share
   never rises and falls 6.000 to 4.199 by t = 6; each unit of fallback
   lost moves half a unit to R, checked at every step.
2. **Reversible before the deadline, not after.** Supply ended at
   T = 2.0 or 3.0, then 20 units unsupported: o_P = 4.000 and 3.916.
   Ended at T = 3.5 or 5.0: o_P = 0.041 and 0.003, P's share near 4.
3. **Controls.** Capacity-first supply: the share stays 6.000. Partial
   substitution at A = 0.5, below [CLAIM-605](CLAIM-605.md)'s a* = 0.585: capacity
   settles at 0.400 and the share at 5.535, no cliff. [CASE-264](../cases.d/CASE-264.md)'s arm B
   (no exit): P gets 1 whatever its fallback is worth, by construction.
   [CLAIM-602](CLAIM-602.md)'s model, without a threshold, run through the same
   pipeline: a smooth fall to 5.547, largest fall per 0.05 of 0.005
   against 0.042.
4. **Under both readings.** On the current-output valuation the terms
   still move (6.000 to 4.347), so the claim's first clause holds on
   either of [LEAD-tmpeo8wq](../leads.d/LEAD-tmpeo8wq.md)'s readings. Its second clause, reversibility,
   concerns the capacity, which is the same under both; but only the
   forward valuation shows the deadline in the terms.

## What it does not say

- **Not a step at the deadline in general.** The steepest fall is in the
  interval centred at t = 3.075, against the deadline 3.098, for
  r ≤ 0.25; at r = 0.5 it moves to t = 2.275. Within half a unit of the
  deadline lies 85 % of the fall by t = 6 at r = 0.02 and 33 % at 0.25.
  The assistant's expectation, stated before the run, was a step at the
  deadline: it holds for where the fall is steepest and fails as a step
  except for a patient party. On the current-output valuation the fall
  is steepest at t = 0.225 and the deadline does not show in the terms.
- **Not the world's numbers.** Every parameter is [CLAIM-605](CLAIM-605.md)'s,
  [CASE-264](../cases.d/CASE-264.md)'s, or invented here (w, r, the horizon).
- **Not intent or gain.** Supply is exogenous. R's cost of supplying,
  and so whether R would choose to supply past the deadline, is not
  modelled.
- **Not exploitation or domination.** No standard is declared, as
  [TERM-123](../terms.d/TERM-123.md) and [TERM-124](../terms.d/TERM-124.md) require; [CLAIM-670](CLAIM-670.md)'s step to exploitation stays
  interpretive. What is shown is a bargaining vulnerability produced by
  supply. That exit is what lets the decay matter at all is [CLAIM-690](CLAIM-690.md)'s
  point, which the no-exit control shows in the dynamic case.
- **Not reach over [TERM-114](../terms.d/TERM-114.md)**, the authority index or the four
  predicates [LEAD-tmpeo8wq](../leads.d/LEAD-tmpeo8wq.md) asks for: a scalar capacity and a scalar
  split.

## Standing

Proposed. Run by its filer only, on 2026-11-25; recomputation by
another session is the check before any promotion. A candidate member
of governance-of-becoming under [ADR-104](../decisions.d/ADR-104.md)'s rule (it is stated in §9.4);
adding it is the owner's call.
