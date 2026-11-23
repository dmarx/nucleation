---
status: Proposed
title: 'In a simulated federated learner with two of seven evaluators compromised, revisable safeguards with an honest monitor moved the trade-off between attack and dissent further than fixed role-limited audit: they cut the success of an attack that mimics dissent from 0.27 to 0.10 and raised the minority''s capability from 0.59 to 0.77, suspending attackers far more often than dissenters; their suspension of the honest majority''s mistaken pull is the safeguard working, not suppression of dissent'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-180, from the
    executed study CASE-tmpqnoj1, as one of two alternative readings of
    its adaptive arm; the assistant's lean.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of scratch/studies/lead-180/ (run.py e1, e4), or a correction of
  its code, in which the adaptive arm with an honest monitor and 2 of 7
  evaluators compromised does not lower the mimic attack's success below
  role-limited audit's while keeping minority capability at or above it,
  or suspends dissenters as often as attackers. A showing that suspending
  members for a mistaken contribution suppresses the disagreement
  self-governance needs would defeat the second clause.
tags:
- self-governance
- complex-systems
- society-and-governance
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-tmpqnoj1
complements:
- CLAIM-tmpd6gon
bears_on:
- QUESTION-090
- QUESTION-089
summary: >-
  Reading (a) of [CASE-tmpqnoj1](../cases.d/CASE-tmpqnoj1.md)'s adaptive arm, the assistant's lean.
  Under the mimic attack with 2 of 7 evaluators compromised, the adaptive
  arm with an honest monitor held attack success to 0.097 against
  role-limited audit's 0.272, kept minority capability at 0.765 against
  0.585 and the dissenters' influence at 1.9 times parity against 0.9, and
  recovered in 19 of 30 seeds against 1. It suspended, at some point, 89%
  of the attackers, 36% of the dissenters and 72% of the cooperatives,
  whose pull of the minority's tasks toward the prior the monitor scores
  as harmful. On this reading [CASE-108](../cases.d/CASE-108.md)'s measure is suppression of honest
  minorities, the cooperatives' suspension is a safeguard against honest
  error and part of its cost, and the arm meets the lead's criterion under
  compromised evaluators, while its monitor is honest. [CLAIM-tmp3t5y3](CLAIM-tmp3t5y3.md) is
  the other reading. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp3t5y3 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpf0b31: In a simulated federated learner with two of seven evaluators compromised, revisable safeguards with an honest monitor moved the trade-off between attack and dissent further than fixed role-limited audit: they cut the success of an attack that mimics dissent from 0.27 to 0.10 and raised the minority's capability from 0.59 to 0.77, suspending attackers far more often than dissenters; their suspension of the honest majority's mistaken pull is the safeguard working, not suppression of dissent

## The claim

[CASE-tmpqnoj1](../cases.d/CASE-tmpqnoj1.md), e1 and e4, mimic attack, 2 of 7 evaluators compromised,
30 seeds:

| Arm | Attack success | Minority capability | Dissent influence | Recovered | Suspended: attackers, dissenters, cooperatives |
|---|---|---|---|---|---|
| Role-limited | 0.272 | 0.585 | 0.94 | 1 of 30 | none |
| Adaptive, honest monitor | 0.097 | 0.765 | 1.94 | 19 of 30 | 89%, 36%, 72% |
| Adaptive, compromised monitor | 0.265 | 0.560 | 0.30 | 2 of 30 | 0%, 100%, 59% |

The revisable safeguards (revocable authorization, a quorum raised after
a loss, panels widened for a starved block) are A41's "role limitations
plus internally revisable safeguards", and with an honest monitor they
repaired much of what compromise of the evaluators did to the minority's
tasks. The cooperatives are suspended because on those tasks their
proposals are wrong; [CASE-108](../cases.d/CASE-108.md) scores the suppression of honest
minorities, and the minority here is the dissenters, whose influence the
arm doubles. So the arm moves [CLAIM-359](CLAIM-359.md)'s trade-off under compromise, as
that claim allows ("Role-limited and revisable safeguards may move it"),
and it does so only while the monitor, a new process that evaluates the
others, is honest: compromised, it suspends every dissenter and no
attacker, A41's "manipulation of the revision mechanism itself".

## What it does not say

- It does not say revision removes the single point of failure; it moves
  it to the monitor ([CLAIM-tmpd6gon](CLAIM-tmpd6gon.md) moves it to the thinnest block).
- It does not say suspending honest members is free. It costs 0.01 of main
  capability without an attack, and it is a cost of the safeguard.

## Note of 2026-11-23: what holds it back

It and [CLAIM-tmp3t5y3](CLAIM-tmp3t5y3.md) are alternative readings of [CASE-tmpqnoj1](../cases.d/CASE-tmpqnoj1.md)'s adaptive
arm, on the same numbers, which reproduce. Which reading the record takes,
whether suspending the honest but mistaken majority counts as suppressing
honest participation, is the owner's choice and has not been made. The
assistant leaned to CLAIM-tmpf0b31.
