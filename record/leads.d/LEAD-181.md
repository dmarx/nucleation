---
number: 181
status: Open
formerly:
- LEAD-tmpweaab
title: 'Use the tolerance-indexed simulation to test whether penalizing newly recognized violations produces avoidance of inquiry'
version: 1
stage: specified
priority: medium
method:
- empirical
tags:
- society-and-governance
- epistemology
- mathematics
date: '2026-11-19'
line:
- distributed-agency
- organizational-normativity
advances:
- CLAIM-662
- CLAIM-657
- CLAIM-663
- QUESTION-279
- QUESTION-456
operationalized_in:
- CASE-249
summary: >-
  Named in [CLAIM-662](../claims.d/CLAIM-662.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-249 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-181: Use the tolerance-indexed simulation to test whether penalizing newly recognized violations produces avoidance of inquiry

## What it would do

Run [CASE-249](../cases.d/CASE-249.md)'s simulation with and without penalties for newly recognized
violations, measuring how much inquiry the agents undertake.

Where the record names it:

- [CLAIM-662](../claims.d/CLAIM-662.md): "[CASE-249](../cases.d/CASE-249.md) gives a design that would test whether the
  incentive produces avoidance of inquiry."

## What would count

Less inquiry under the penalty supports [CLAIM-662](../claims.d/CLAIM-662.md); none defeats it.

## Note of 2026-11-23: the simulation built and run
<!-- inactive-ok-file: CASE-tmp8mk6w CLAIM-tmpbbfcj CLAIM-tmpjz94s CLAIM-tmp0bqyu — new; filed by the lead run of 2026-11-23 -->

Carried out by the assistant. [CASE-tmp8mk6w](../cases.d/CASE-tmp8mk6w.md) builds [CASE-249](../cases.d/CASE-249.md)'s institution
(scratch/studies/lead-181/): 30 fixed requirements, 20 of them found only by
inquiry, an internal evaluator counting recognized violations and an
independent one counting all, a stationary policy splitting each period's
budget among inquiry, remediation and output, chosen both by Monte Carlo
optimum and by 16 gradient-bandit learners. Five governance regimes in four
settings. Under the penalty on every recognized violation with discovery
unrewarded, the institution makes no inquiry in any setting ([CLAIM-tmpbbfcj](../claims.d/CLAIM-tmpbbfcj.md)
proves it path by path where nothing surfaces from outside) and its internal
count ends near 0 while about a third to two thirds of its violations remain.

What "without penalties" means decides the test, so two readings are filed
as alternatives for the owner. [CLAIM-tmpjz94s](../claims.d/CLAIM-tmpjz94s.md): against scoring by the
independent count, inquiry falls from 5 or 6 units of 10 to 0 in every
setting, and the lead's test is met. [CLAIM-tmp0bqyu](../claims.d/CLAIM-tmp0bqyu.md): against internal
scoring with only that penalty removed (amnesty, or none), inquiry is 0 both
ways where inquiry costs output and earns nothing else, and lower under the
penalty only where inquiry is free or being found out from outside costs
extra; there the test is met in two settings of four, and where it is not,
[CLAIM-662](../claims.d/CLAIM-662.md) is not defeated, since the incentive is present and there is no
inquiry for it to remove. The assistant leans to [CLAIM-tmp0bqyu](../claims.d/CLAIM-tmp0bqyu.md) as the
reading of what the result means, since it varies only the penalty, and
reads [CLAIM-tmpjz94s](../claims.d/CLAIM-tmpjz94s.md) as the lead's test taken at its word.

Not done: [CASE-249](../cases.d/CASE-249.md)'s tolerance axis and its breadth and depth budgets (k, T)
were not exercised, nor relaxing tolerances as a second route to a better
score; policies are stationary. The lead's status and stage are the owner's.
