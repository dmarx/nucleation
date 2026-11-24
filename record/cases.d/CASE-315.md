---
number: 315
status: Proposed
formerly:
- CASE-tmpvnozj
title: 'A readiness simulator run under spend-matching and under carry-over: a heavy rescue squad whose budget is set to the last month''s peak is lost for good in every run within months where it is sent only on confirmation, in a fifth of runs within nine years where it is sent provisionally to each of six reports a month, and never where it drills each month or the unspent budget rolls over'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-080. The code,
    tests and outputs are under scratch/studies/lead-080/.
standing: documented
kind: executed-study
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-22'
illustrates:
- CLAIM-577
bears_on:
- QUESTION-394
- QUESTION-386
line:
- readiness
- formal-apparatus
- realizability
summary: >-
  [LEAD-080](../leads.d/LEAD-080.md) asked for A's simulator of [QUESTION-394](../questions.d/QUESTION-394.md) to be run twice, once
  with each month's budget set to the last month's peak spending
  ([CLAIM-577](../claims.d/CLAIM-577.md)) and once with carry-over, to see whether the heavy-rescue
  response of [CASE-213](CASE-213.md) stays reachable. The simulator has one or two
  squads, reported collisions of which a tenth need extrication, Poisson
  arrivals, a first-unit assessment right nine times in ten, travel from
  distance, mutual aid, skill that halves in about seven months without
  practice, and [CLAIM-577](../claims.d/CLAIM-577.md)'s capacity of 0.7 to hold and 1.3 with a squad
  out. Under spend-matching the squad is lost for good in every one of 300
  runs, by a median of month 2 to 8, when it is sent only on confirmation
  or reports are few (two a month), and in 20 % of runs within nine years when
  it is sent provisionally to every one of six reports a month; drilling
  every month keeps it in every run. Rolling over the unspent part keeps
  it in every run; rolling over 60 % of it loses it as fast as
  spend-matching. [CASE-200](CASE-200.md)'s carry-over rule never loses it for good but,
  used every month, leaves it reachable in half the months. So the claim's
  prediction holds, and a quiet period turns out to mean a month in which
  nothing at all mobilizes the squad, not a month without a true need. The
  model is the assistant's and its rates are invented. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-200 CLAIM-878 TERM-110 — Proposed or new; CASE-200's carry-over rule is run as filed, the claim is filed with this study, and TERM-110 is cited as CLAIM-577 cites it -->

# CASE-315: A readiness simulator run under spend-matching and under carry-over: a heavy rescue squad whose budget is set to the last month's peak is lost for good in every run within months where it is sent only on confirmation, in a fifth of runs within nine years where it is sent provisionally to each of six reports a month, and never where it drills each month or the unspent budget rolls over

## The study

[QUESTION-394](../questions.d/QUESTION-394.md)'s note of 2026-11-05: "Run it twice, once with each period's
budget set to the last period's peak spending and once with carry-over,
and measure whether the rare, deadline-bound transition, the heavy-rescue
response of [CASE-213](CASE-213.md), stays reachable. The claim predicts it is lost under
the first rule after a quiet period and survives under the second."
[LEAD-080](../leads.d/LEAD-080.md) asks for that run.

**The simulator** is the one [QUESTION-394](../questions.d/QUESTION-394.md) records from A: rescue squads
(one, or two in one variant), two incident types (a reported collision
that does or does not need extrication, p = 0.1), Poisson arrivals
(λ = 2 or 6 reports a month), a first-unit assessment of accuracy 0.9,
travel times from distance, mutual aid as the substitute, and a skill k
that decays by 9 % a month and gains 0.3 for each drill or extrication,
[QUESTION-386](../questions.d/QUESTION-386.md)'s recursion with a cap; a squad is qualified while k ≥ 0.5.
A true need is met when a qualified responder is on scene within 20
minutes. Two dispatch policies: provisional dispatch with cancellation
([CASE-213](CASE-213.md)) and dispatch on confirmation. Drills every month, every third
month or never.

**The budget** is [CLAIM-577](../claims.d/CLAIM-577.md)'s capacity resource. Holding costs 0.7; each
squad mobilized, on a call or a drill, adds 0.6, so one squad out costs
1.3, the claim's worked numbers. A month's spending is its peak, so a
dispatch cancelled after five minutes spends 1.3 as much as a rescue does.
A mobilization that would exceed the month's budget is refused, and the
need goes to mutual aid. The regimes:

- **spend-matching**: B_{t+1} = s_t;
- **peak plus carry-over**: B_{t+1} = s_t + ρ(B_t − s_t), with ρ = 1 (the
  budget stays at 1.3) or 0.6;
- **[CASE-200](CASE-200.md)'s carry-over**: B_{t+1} = 1.0 + ρ(B_t − s_t), ρ = 1 or 0.6,
  uncapped.

The lead does not say which carry-over rule it means, so both were run.
Every choice left open is listed, as made before running, in the study's
README. 300 runs of 120 months each in each of 65 configurations; runs with the same
λ see the same call histories. Thirteen tests pass, among them [CLAIM-577](../claims.d/CLAIM-577.md)'s
steps 1 and 3 on random histories and the loss probability below against
2,000 runs.

## Results

**One squad, drills every third month.** Lost: share of runs lost for good, that is with the budget below 1.3
from some month to the end and for at least the last 12 months, so within
nine years;
month: quartiles of the month of loss; reach: share of months the budget
allows the squad; met: share of true needs met, mean (sd over runs).

| Reports a month, policy | Regime | Lost | Month | Reach | Met |
|---|---|---|---|---|---|
| 6, provisional | spend-matching | 0.20 | 29, 50, 78 | 0.89 | 0.83 (0.20) |
| 6, provisional | peak, ρ = 1 | 0 | | 1.00 | 0.91 (0.03) |
| 6, provisional | peak, ρ = 0.6 | 0.20 | 29, 50, 78 | 0.89 | 0.83 (0.20) |
| 6, provisional | [CASE-200](CASE-200.md), ρ = 1 | 0 | | 0.50 | 0.52 (0.06) |
| 6, confirmation | spend-matching | 1.00 | 2, 3, 6 | 0.04 | 0.03 (0.03) |
| 6, confirmation | peak, ρ = 1 | 0 | | 1.00 | 0.67 (0.06) |
| 6, confirmation | [CASE-200](CASE-200.md), ρ = 1 | 0 | | 0.63 | 0.42 (0.06) |
| 2, provisional | spend-matching | 1.00 | 3, 8, 15 | 0.09 | 0.22 (0.11) |
| 2, provisional | peak, ρ = 1 | 0 | | 1.00 | 0.92 (0.06) |
| 2, confirmation | spend-matching | 1.00 | 2, 2, 3 | 0.02 | 0.01 (0.03) |
| 2, confirmation | peak, ρ = 1 | 0 | | 1.00 | 0.67 (0.10) |

With drills every month, spend-matching loses the squad in no run, under
either policy and either λ, and matches the peak, ρ = 1 rule exactly. With
no drills, it loses it in 27 % of runs at six reports a month with
provisional dispatch and in every run otherwise. Under spend-matching,
once lost, the squad also stops drilling, and its skill decays below the
qualified level within about eight months. Years 6 to 10 alone show the same ordering.

- **The prediction holds.** Under spend-matching the budget cannot rise
  (s_t ≤ B_t; checked on random histories in the tests), and a squad once
  priced out never came back. Under full
  carry-over it was never lost.
- **A quiet month is a month without any mobilization.** The budget stays
  at 1.3 exactly as long as every month has something that sends the
  squad: a rescue, a drill, a false alarm or a cancelled provisional
  dispatch. Under provisional dispatch every report sends it, so a month is
  quiet with chance e^(−λ), and the chance of loss within n undrilled
  months is 1 − (1 − e^(−λ))^n: 0.16 for the 72 undrilled months of the
  first nine years at λ = 6, against 0.20 observed (standard error 0.02;
  the same runs give 0.27 with no drills against 0.24 predicted, and the
  formula holds within sampling error over 2,000 runs in the tests). Under confirmation only
  true needs and false alarms send it, about 0.4 a month at λ = 2, so the
  first undrilled month usually prices it out.
- **Cancellations keep the capability funded.** At six reports a month the
  provisionally dispatched squad is cancelled 3.7 times a month. Under
  spend-matching that is what holds its budget, and the 20 % of runs that
  still lose it are those with one month of no reports. [CLAIM-561](../claims.d/CLAIM-561.md) says a
  high cancellation rate does not show waste; here, under this budget
  rule, cutting it would cost the capability.
- **Partial carry-over on the peak rule is spend-matching.** With ρ = 0.6,
  one quiet month leaves 0.7 + 0.6 × 0.6 = 1.06, below 1.3, and the
  results match spend-matching run for run.
- **[CASE-200](CASE-200.md)'s rule keeps the squad but rations it.** It is never lost for
  good, since every month held adds 0.3. But a month at the peak spends the
  whole carried balance and leaves 1.0 for the next, so a squad sent every
  month is allowed in only every other month, and needs met fall to about
  half. Used rarely, as under confirmation with no drills, the uncapped
  balance grows to a mean budget of 7.8 against 1.3. With ρ = 0.6 it
  rebuilds in three months (1.18, 1.29, 1.35), not one, and the squad is
  allowed in 27 to 57 % of months.
- **Two squads.** Under spend-matching, the second squad is priced out
  after the first month in which the two are never out together, which in
  these runs is the second month: both are allowed in 1.7 % of months.

**Skill as well as budget.** Full carry-over keeps the squad funded but
not qualified: with no drills and two reports a month its final skill is
0.58 on average and needs met fall from 0.92 to 0.59 under provisional
dispatch. Funding and maintenance are separate conditions, as [QUESTION-386](../questions.d/QUESTION-386.md)
says.

## What it can show

- That [CLAIM-577](../claims.d/CLAIM-577.md)'s mechanism runs in a model of the organization it was
  stated for, with arrivals, travel and decay, and that its prediction
  holds there: a capability lost under spend-matching after a month in
  which nothing called on it at the peak, and kept under full carry-over.
- What makes a month quiet: no mobilization of any kind. Whether quiet
  months occur depends on the dispatch policy and the drill schedule, so
  policies [CLAIM-561](../claims.d/CLAIM-561.md) judges by expected loss differ, under this budget
  rule, in how long they keep the capability funded ([CLAIM-878](../claims.d/CLAIM-878.md)).
- That monthly drilling at the peak holds the budget, the over-spending
  [CLAIM-577](../claims.d/CLAIM-577.md) says an organization that anticipated the rule would do
  (in [TERM-110](../terms.d/TERM-110.md)'s sense), here done for the skill alone.
- That the two carry-over rules differ: rolling over what the peak rule
  leaves unspent holds the budget, while [CASE-200](CASE-200.md)'s base-plus-balance rule
  rations a capability used every period.

## What it cannot show

- That real budgets are set this way, or are capacity ceilings set at a
  month's peak. A real squad called out for an hour does not spend its
  month's capacity; a budget in money or hours would count the hour, and
  then a cancellation would hold far less of the budget. The result
  belongs to the peak accounting [CLAIM-577](../claims.d/CLAIM-577.md) and [CASE-200](CASE-200.md) use.
- That the rates, distances, deadline or decay belong to any department.
  They are invented.
- The policy ranking [QUESTION-394](../questions.d/QUESTION-394.md) asks for. Only two of its four policies
  are run, at one value of congestion, accuracy and coverage cost; at
  p = 0.1 provisional dispatch is below [CLAIM-561](../claims.d/CLAIM-561.md)'s threshold in these
  costs and costs more per month, which the study does not weigh against
  the capability it keeps.

Code: `scratch/studies/lead-080/` (`sim.py`, `test_sim.py`, outputs in
`results.txt` and `results.json`; how to rerun in its README).

## Note of 2026-11-24: rerun, for the promotion review the owner proposed at U33 of the exchange 'Memes, Contracts, and Systemic Normativity'

Rerun on 2026-11-24 by the assistant, from a copy of `scratch/studies/lead-080/` as on this branch: `sim.py` regenerates `results.json` byte for byte and `results.txt` unchanged, and the 13 tests of `test_sim.py` pass. A53 of the exchange names this case as a promotion candidate, a study "executed" and awaiting review. The run is now checked by a session other than the one that filed it, which the status-review README (section 2) asks of a demonstrated case; the ruling is the status review's ([LEAD-tmp0j28l](../leads.d/LEAD-tmp0j28l.md)). The note is the assistant's (Claude, in this session). No status change.
