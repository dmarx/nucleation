---
status: Open
title: 'How does the optimal threshold for provisionally committing a specialized resource vary with congestion, geography, available substitutes, assessment accuracy, and the cost of leaving other contingencies uncovered?'
version: 1
tags:
- operations-research
- probabilistic-modeling
- society-and-governance
date: '2026-11-04'
line:
- distributed-agency
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 10 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)", with its
  proposed experiment (section 13) as what would answer it. [CLAIM-tmp5rh3v](../claims.d/CLAIM-tmp5rh3v.md)'s
  threshold has fixed costs; here the costs depend on the state of the
  system, so a threshold right under ample coverage may be wrong when one
  scarce unit is the last responder. The wording is A's; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp5rh3v TERM-tmp5t7y8 CASE-tmpt6fm7 — Proposed or new; A's proposals of 2026-11-04 and the readings they cite, as open -->
<!-- inactive-ok-file: CLAIM-tmplo4ca — Proposed; the assistant's claim of 2026-11-05, cited as open -->

# QUESTION-tmpvweyo: How does the optimal threshold for provisionally committing a specialized resource vary with congestion, geography, available substitutes, assessment accuracy, and the cost of leaving other contingencies uncovered?

## Why it is a question

[CLAIM-tmp5rh3v](../claims.d/CLAIM-tmp5rh3v.md)'s threshold for provisional commitment ([TERM-tmp5t7y8](../terms.d/TERM-tmp5t7y8.md))
treats the costs as fixed. In a real system they are endogenous:

  ΔV(p, s) = pH(s) − C_dispatch(p, s) − C_coverage(s),

with the state s including the other units already committed, their
locations, mutual aid, and the specialist's proficiency. A low threshold
may be right when coverage is ample and wrong when one scarce unit is the
last responder. How the threshold moves with s is not settled by the
fixed-cost model.

Four policies are to be compared: immediate provisional dispatch with
cancellation ([CASE-tmpt6fm7](../cases.d/CASE-tmpt6fm7.md)); dispatch after confirmation; immediate
dispatch without effective cancellation; and prepositioning or standby.

## What would answer it

A's proposed experiment, which A treats as future work: a small
simulator with one or two rescue companies, two incident types,
stochastic arrivals, a first-unit assessment of configurable accuracy,
travel delays, and a skill variable that decays without maintenance. Its
outputs: the probability of timely qualified response to true needs, busy
time, cancellations, coverage gaps and expected cost, and "not ... the
raw number of extrications". An answer is the threshold, or the ranking of
the four policies, as a function of congestion, geography, substitutes,
assessment accuracy and coverage cost, with the regimes in which the
ranking changes.

## What would not answer it

A threshold computed from fixed costs, which is [CLAIM-tmp5rh3v](../claims.d/CLAIM-tmp5rh3v.md)'s, or a
policy's count of extrications.

## Note of 2026-11-05: a test for the pinning claim

A's simulator is also the cheapest test of CLAIM-tmplo4ca. Run it twice, once with each period's budget set to the last period's peak spending and once with carry-over, and measure whether the rare, deadline-bound transition, the heavy-rescue response of CASE-tmpt6fm7, stays reachable. The claim predicts it is lost under the first rule after a quiet period and survives under the second. Most of what the constraint-architecture filing added is mechanical analogy; this would be its first organizational test. No status changes.
