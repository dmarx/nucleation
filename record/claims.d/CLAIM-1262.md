---
number: 1262
status: Proposed
formerly:
- CLAIM-tmpcet1g
title: 'An organization''s corrective mobilization can be scaled by its tolerance and horizon rather than by the bare size of a discrepancy: burn-rate alerting recruits response by how fast an error budget is being spent relative to its window, so that a small sustained discrepancy and a large brief one are ranked by what they cost the allowance'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the record's account of organizational affect already
  makes mobilization relative to a maintained tolerance over a horizon, so
  that the claim restates CLAIM-552 and TERM-017; or that burn-rate
  alerting, as practiced, ranks discrepancies exactly as a threshold on
  the present error rate would, the budget and window adding nothing to
  which events recruit response.
tags:
- emotion-and-affect
- software-engineering
date: '2026-11-24'
line:
- organizational-affect
works:
- governance-of-becoming
complements:
- CLAIM-552
uses:
- TERM-017
grounds:
- LIT-3216
summary: >-
  A34 §5 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24): burn-rate alerting as "an engineering realization
  of concern-relative appraisal", which "suggests a useful refinement to
  our account of organizational affect". The gap fill narrows A34's
  "projected exhaustion" to what burn-rate alerts compute. The wording is
  A's (ChatGPT, in the exchange "Memes, Contracts, and Systemic
  Normativity"); adopting it is the owner's call.
---

<!-- inactive-ok-file: LIT-3216 — Proposed, Deferred or new; filed or registered with the exchange 'Memes, Contracts, and Systemic Normativity', cited whatever their standing -->

# CLAIM-1262: An organization's corrective mobilization can be scaled by its tolerance and horizon rather than by the bare size of a discrepancy: burn-rate alerting recruits response by how fast an error budget is being spent relative to its window, so that a small sustained discrepancy and a large brief one are ranked by what they cost the allowance

## The claim

A34 §5 defines the burn rate as the observed error fraction over the
permitted one, b_t = e_t / e*. "A
burn rate of 1 means that the service would exactly consume its error
budget over the full objective window if the rate persisted." It then
says: "Corrective mobilization need not depend only on present
discrepancy. It can depend upon projected exhaustion of the
organization's capacity to tolerate that discrepancy." And: "An alert is
not necessarily an emotion. But the broader alerting-and-response
organization can exhibit several functional properties of affective
regulation: appraisal, action readiness, claimed precedence, persistence,
suspension and recovery."

A34's table, for a 30-day window and uniform traffic, was checked with
`python3 -I`: 720 hours divided by the burn rate gives 720, 360, 72, 24
and 1 hours for burn rates 1, 2, 10, 30 and 720, which are A34's 30 days,
15 days, 3 days, 24 hours and 1 hour.

## Gap filled: what a burn-rate alert computes

A burn rate is the present error rate divided by the allowed one, so on
its own it is a rescaled present discrepancy. What makes the alerts the
workbook describes ([LIT-3216](../literature.d/LIT-3216.md)) more than a threshold on the present
rate is that the scale and the windows are set by the maintained demand:
the objective fixes \(e^*\), the window fixes the horizon, and an alert
fires on the share of the whole window's budget spent within a short
window. At a burn rate of 14.4 for one hour, a 30-day budget loses 14.4 ×
1/720 = 2% (checked with `python3 -I`); the workbook's Table 5-6 pairs "2% 1 hour 14.4 Page" (checked against the web edition on 2026-11-24). That is appraisal relative to a
tolerance and a horizon, which is the claim.

"projected exhaustion" in A34's stronger sense, time to exhaust the budget
that remains, needs the remaining budget in the rule. A burn-rate alert
of the kind just described does not use it: two services at the same
burn rate alert alike whatever budget each has left. The claim is
therefore stated in the weaker sense; a policy that conditions on the
remaining budget, such as an error-budget policy that freezes releases on
exhaustion, is where the stronger sense would be found. The section is
the assistant's (Claude, in this session); adopting it is the owner's
call.

## Standing

Proposed, in A's voice. Its affect side is an analogy A34 itself hedges;
it complements [CLAIM-552](CLAIM-552.md), whose tolerances are a perspective's criteria
for conferring influence, by adding the horizon over which a tolerance is
spent. That error budgets regulate precedence between competing concerns
was introduced earlier in the exchange (A16) and is filed by another
group.
