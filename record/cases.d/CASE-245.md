---
number: 245
status: Proposed
formerly:
- CASE-tmp3431v
title: 'A start state with a one-step edge to the target and a one-step edge to an absorbing trap, and a process that takes the target edge when one step remains and the trap edge when more remain: the target is reachable by a path at every budget from 1, and the process reaches it at budget 1 and never at 2 or more'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Corrected after the owner's review of #485 on 2026-11-12. Under this
    architecture (s to g, s to t, t absorbing) a stochastic stationary
    process that moves s to g with probability p succeeds with probability p
    at every budget b of 1 or more, not 1 - (1 - p)^b as version 1 said;
    that formula needs a retry, a self-loop s to s. The formula is
    corrected, and a variant with an explicit self-loop gives the retry
    formula. Both were computed exactly with python3 -I. The main
    counterexample is unchanged.
standing: stipulated
kind: construction
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- formal-apparatus
illustrates:
- CLAIM-560
summary: >-
  The assistant's construction, built at the owner's acceptance on
  2026-11-12 of the ideas offered after filing the exchange "Medical
  Ethics and Media Enshitification" (2026-11-11). It grounds
  [CLAIM-654](../claims.d/CLAIM-654.md). Checked with python3 -I on 2026-11-12, together with an
  exhaustive check that every stationary successor map on three states
  gives reach monotone in the budget (27 maps, no violation). The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-654 — Proposed; filed in the same follow-up -->

# CASE-245: A start state with a one-step edge to the target and a one-step edge to an absorbing trap, and a process that takes the target edge when one step remains and the trap edge when more remain: the target is reachable by a path at every budget from 1, and the process reaches it at budget 1 and never at 2 or more

## The case

States s (start), g (target) and t (trap, absorbing). Moves s → g and
s → t, each costing one step; a budget b is a number of steps. The
process's choice at s depends on the steps remaining: with one left it
moves to g, and with more it moves to t, as an agent that uses spare
budget to explore first might.

| budget b | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| a path to g within b exists | no | yes | yes | yes | yes |
| the process reaches g within b | no | yes | no | no | no |

The check run with it: for every deterministic stationary process on three
states (a successor map, 27 in all), "g visited within b steps" never goes
from true at b to false at b + 1. For a stochastic stationary process that moves s → g with probability p and
s → t otherwise, the probability of reaching g within b steps is 0 at b = 0
and p at every b ≥ 1: constant, so monotone, and never above p, because the
process has one chance at s. Version 1 gave 1 − (1 − p)^b here, which is
wrong for this architecture (corrected after the owner's review of [#485](https://github.com/dmarx/nucleation/issues/485) on
2026-11-12).

**Variant with a retry.** Add a self-loop s → s. A stationary process that
moves s → g with probability p and stays at s otherwise reaches g within b
steps with probability 1 − (1 − p)^b. With probability p to g, r to s and 1
− p − r to the trap, the probability is p(1 − r^b)/(1 − r). Both rise with
b, as the monotone case of [CLAIM-654](../claims.d/CLAIM-654.md) requires.

Computed exactly with python3 -I on 2026-11-12, as fractions, for p = 1/3
and 1/2 and b from 0 to 5 (r = 1/4 in the three-way variant). Without the
loop: 0, then p at every b. With the retry at p = 1/2: 0, 1/2, 3/4, 7/8,
15/16, 31/32. With r = 1/4 and the trap, at p = 1/2: 0, 1/2, 5/8, 21/32,
85/128, 341/512. Each matched its formula.

## What it shows

The admissible-path reachability [CLAIM-560](../claims.d/CLAIM-560.md) indexes is monotone in the
budget here, as it must be. Reachability by a process whose choices
depend on the remaining budget is not. That is the separation
[CLAIM-654](../claims.d/CLAIM-654.md) states.
