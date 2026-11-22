---
status: Proposed
title: 'Under a budget set each period to the last period''s peak spending, a capability stays funded exactly as long as every period contains a mobilization at its cost, whether a use, a drill, a false alarm or a cancelled dispatch, so dispatching it provisionally to every report keeps it funded far longer than dispatching it only on confirmation of need'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-080, from the
    study of CASE-tmpvnozj.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: under the pure rule B_{t+1} = s_t, starting
  at B_0 ≥ B*, a period containing an occupation costing at least B* after
  which the budget is below B*, or a period without one after which it is
  at least B*; or, with independent periods, a chance of loss within n
  periods other than 1 − ∏(1 − q_t); or, in CASE-tmpvnozj's model, loss
  frequencies that differ from that formula beyond sampling error. Not
  defeated by budgets kept in money or hours, which count how long a
  capability is used and not its peak, nor by rules with a floor, growth
  or carry-over, none of which the claim covers.
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-22'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-577
grounds:
- CASE-tmpvnozj
complements:
- CLAIM-561
uses:
- TERM-109
bears_on:
- QUESTION-386
- QUESTION-394
summary: >-
  A corollary of [CLAIM-577](CLAIM-577.md), found in running [LEAD-080](../leads.d/LEAD-080.md)'s study
  ([CASE-tmpvnozj](../cases.d/CASE-tmpvnozj.md)). Under spend-matching the next budget is this period's
  peak, so a capability costing B* to mobilize stays affordable exactly as
  long as every period has something that mobilizes it, and its first
  period with nothing loses it for good. If q_t is the chance that period
  t has nothing, the chance of losing it within n periods is
  1 − ∏(1 − q_t). Whatever mobilizes counts: a use, a drill, a false alarm
  or a provisional dispatch ([TERM-109](../terms.d/TERM-109.md)) cancelled minutes later. So the
  dispatch policy decides how long the capability survives the rule. Sent
  provisionally to six reports a month, a heavy rescue squad is quiet in a
  month with chance e^(−6) and was still funded after nine years in 80 %
  of the study's runs; sent only on confirmation it was lost in every run within months.
  [CLAIM-561](CLAIM-561.md) says a high cancellation rate does not show waste; under this
  rule the cancellations are also what keeps the capability funded. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmpvnozj — new; the study this claim is drawn from, filed with it -->

# CLAIM-tmpocsw4: Under a budget set each period to the last period's peak spending, a capability stays funded exactly as long as every period contains a mobilization at its cost, whether a use, a drill, a false alarm or a cancelled dispatch, so dispatching it provisionally to every report keeps it funded far longer than dispatching it only on confirmation of need

## The claim

Take [CLAIM-577](CLAIM-577.md)'s rule, B_{t+1} = s_t, with s_t the peak capacity occupied
in period t, and a capability whose mobilization costs B* above holding
cost h < B*. Start at B_0 ≥ B*.

1. **Funded exactly while every period mobilizes it.** B_{t+1} ≥ B* if and
   only if period t occupied something costing at least B*. If every
   period has a mobilization, the budget stays at least B*; the first
   period with none sets it below B*, and by [CLAIM-577](CLAIM-577.md) it never returns.
2. **The chance of loss.** If period t has no mobilization with chance
   q_t, independently, the chance the capability is still funded after n
   periods is ∏(1 − q_t), and the chance it has been lost is
   1 − ∏(1 − q_t).
3. **Anything that mobilizes counts.** The rule sees the peak, not its
   purpose or its length. A rescue, a drill, a dispatch to a false alarm and
   a provisional dispatch ([TERM-109](../terms.d/TERM-109.md)) cancelled after five minutes each set
   s_t = B*.
4. **So the dispatch policy sets q_t.** A policy that mobilizes on every
   report of a possible need has q_t equal to the chance of no report; one
   that mobilizes only on confirmed need has q_t equal to the chance of no
   confirmed need, which is far larger when need is rare.

Steps 1 to 4 follow from the rule. [CASE-tmpvnozj](../cases.d/CASE-tmpvnozj.md) shows their size in a
model of [CASE-213](../cases.d/CASE-213.md)'s squad: at six reports a month, a tenth needing
extrication, quarterly drills, the squad was lost in 20 % of 300 runs within
nine years under provisional dispatch and in all of them, by a median of
month 3, under confirmation. Monthly drills kept it in every run under
either policy.

## What it adds

- **A second reason a cancellation rate cannot show waste.** [CLAIM-561](CLAIM-561.md)'s is
  that provisional dispatch minimizes expected loss when the delay it
  saves is costly. Under spend-matching there is another: the cancelled
  dispatches are the spending that keeps the capability in the budget. A
  manager who cut them as waste would, under this rule, be cutting the
  capability.
- **Quiet means unmobilized, not unneeded.** [CLAIM-577](CLAIM-577.md)'s quiet period is
  a period spent holding. In an organization it is a period in which
  nothing at all sent the capability out, which can be rare even when
  true need is rarer still.
- **Maintenance as spending.** A drill each period holds the budget,
  which is the over-spending [CLAIM-577](CLAIM-577.md) says an organization anticipating
  the rule would do. For [QUESTION-386](../questions.d/QUESTION-386.md) it means that whether utilization-
  based budgeting defunds a rare capability turns on whether its practice
  is counted as utilization.

## What it does not say

- That provisional dispatch is the better policy. At the study's costs and
  p = 0.1, it costs more in expected loss ([CLAIM-561](CLAIM-561.md)'s threshold is 0.143);
  the claim says only how long each keeps the capability funded.
- Anything about budgets in money or hours. Those count how long a squad
  is out, so a cancelled dispatch holds far less of them, and step 3 fails.
- That periods are independent in practice. Step 2 needs it; seasonal or
  clustered demand changes the product, not steps 1, 3 and 4.
