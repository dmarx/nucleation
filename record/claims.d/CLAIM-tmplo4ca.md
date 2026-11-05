---
status: Proposed
title: 'A budget set each period to the peak resource spent the period before never rises, so the configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a period, under the rule as stated, in
  which the budget rises without an outside increase; a reachable set that
  grows from one period to the next; or a transition with a threshold above
  the holding cost that stays reachable after a period spent holding.
  Not defeated by budget rules with a floor, growth term, carry-over or
  discretion, which the claim does not cover, nor by cumulative or
  rate-limited resources; the claim is about one capacity resource under
  the pure spend-matching rule.
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-05'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-tmpbi4ca
complements:
- CLAIM-079
uses:
- TERM-tmp2ysyt
- TERM-tmpbxjmx
summary: >-
  The assistant's own proposition, offered at the owner's invitation on
  2026-11-05 after the constraint-architecture and emergency-readiness
  filings. It joins A's budget ratchet to the transition threshold of
  [CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md). Under a capacity budget set each period to the previous
  period's peak spending, an organization that only holds its configuration
  spends the holding cost, so its budget falls to that cost and stays
  there; what it can reach is the connected part of the sublevel set at
  that level around where it is, and every transition needing reconfiguration
  slack is lost without anyone choosing to give it up and without any sign
  in routine output. It is [CLAIM-079](CLAIM-079.md)'s stability without viability, produced
  by a budget rule. Demonstrated for the pure rule; real budget rules have
  floors, growth and discretion that weaken it. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp0g3pa CASE-tmp4op8y CLAIM-tmpbi4ca CLAIM-tmpuk8gq TERM-tmp26wo4 TERM-tmp2ysyt — Proposed or Skimmed; entries of 2026-11-04 and 2026-11-05 from the readiness and constraint-architecture filings, cited as open -->
<!-- inactive-ok-file: CLAIM-tmp42yq0 — Proposed or new; entries of 2026-11-05 from A's fourth paste and the assistant, cited as open -->

# CLAIM-tmplo4ca: A budget set each period to the peak resource spent the period before never rises, so the configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference

## The claim

Let a connected configuration space Q carry a capacity requirement
r(q) ≥ 0, and let the threshold B*(q, q′) of a transition be as in
[CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md): the least, over admissible paths, of the peak of r along
the path. In period t the organization has budget B_t, may move along any
path whose peak is at most B_t, and spends s_t, the peak of r over what it
occupied in the period. The rule is

  B_{t+1} = s_t.

Then:

1. **The budget never rises.** s_t ≤ B_t, since nothing above the budget
   can be occupied, so B_{t+1} ≤ B_t.
2. **What is reachable shrinks.** At budget B, the configurations
   reachable from q are R_B(q), the connected component containing q of the
   sublevel set {r ≤ B}. If the organization ends period t at q_{t+1}, then
   q_{t+1} ∈ R_{B_t}(q_t), and R_{B_{t+1}}(q_{t+1}) ⊆ R_{B_t}(q_t), because
   a smaller sublevel set's component through a point of the larger
   component lies inside it.
3. **Holding forecloses.** A period spent holding q costs r(q), so
   B_{t+1} = r(q). Any transition from q with B*(q, q′) > r(q), that is
   with positive reconfiguration slack against the current configuration
   ([TERM-tmp2ysyt](../terms.d/TERM-tmp2ysyt.md)), is then out of reach in every later period.
4. **Only outside money restores it.** Under the rule the budget cannot
   climb back, so reaching q′ again needs an increase from outside of at
   least B*(q, q′) − r(q).

## Worked instance

A's example: r(q) = 0.7 + 2.4q(1 − q) on [0, 1], with B* = 1.3 between the
two ends, each held at 0.7. Start at q = 0 with B_0 = 1.3: the transition is
affordable. Spend the period holding at q = 0: s_0 = 0.7, so B_1 = 0.7,
and the sublevel set at 0.7 is the two endpoints alone. The transition is
gone, and so is every move at all. [CASE-tmp0g3pa](../cases.d/CASE-tmp0g3pa.md) is the same numbers with a
carry-over rule, under which the transition survives.

## What it adds

- **It is a mechanism, not a choice.** Nothing in the rule decides to give
  up the transition; ordinary efficient operation does it, which is why A's
  worry about utilization-based budgeting ([QUESTION-tmpmtvei](../questions.d/QUESTION-tmpmtvei.md)) can come true
  without anyone wanting it.
- **The loss leaves no trace in output.** The organization holds its
  configuration as well as before; only the set of places it could go has
  changed. [CLAIM-414](CLAIM-414.md)'s matched trajectories and the unrecorded calls of
  [CASE-tmp4op8y](../cases.d/CASE-tmp4op8y.md) are the observational side of this.
- **It is stability without viability by budget** ([CLAIM-079](CLAIM-079.md)): the
  organization stays in a stable regime while losing the transitions it
  would need when that regime stops serving.

## What it does not say

- Real budget rules are rarely pure spend-matching. A floor B̄ ≥ B*, a
  growth term, carry-over ([CASE-tmp0g3pa](../cases.d/CASE-tmp0g3pa.md)) or discretion each break the
  argument, and which real rules are close enough to the pure one is
  empirical.
- It concerns one capacity resource. Cumulative and rate-limited budgets
  ([TERM-tmp26wo4](../terms.d/TERM-tmp26wo4.md)) need their own treatment, and several resources at once
  bring in [CLAIM-tmpuk8gq](CLAIM-tmpuk8gq.md).
- It says nothing about whether the lost transitions were worth keeping.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CLAIM-tmp42yq0](CLAIM-tmp42yq0.md) reads this claim as a decoupling of two budgets: spend-matching shrinks the acting budget, fragmenting what the organization can become, while the observing budget, and so what outsiders can tell apart, is untouched. No status changes.
