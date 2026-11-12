---
status: Proposed
title: 'A start state with a one-step edge to the target and a one-step edge to an absorbing trap, and a process that takes the target edge when one step remains and the trap edge when more remain: the target is reachable by a path at every budget from 1, and the process reaches it at budget 1 and never at 2 or more'
version: 1
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
  CLAIM-tmpff0cq. Checked with python3 -I on 2026-11-12, together with an
  exhaustive check that every stationary successor map on three states
  gives reach monotone in the budget (27 maps, no violation). The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpff0cq — Proposed; filed in the same follow-up -->

# CASE-tmp3431v: A start state with a one-step edge to the target and a one-step edge to an absorbing trap, and a process that takes the target edge when one step remains and the trap edge when more remain: the target is reachable by a path at every budget from 1, and the process reaches it at budget 1 and never at 2 or more

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
from true at b to false at b + 1. For a stochastic stationary process
that moves s → g with probability p, the hitting probability 1 − (1 − p)^b
rises with b (computed exactly for p = 1/3 and 1/2).

## What it shows

The admissible-path reachability CLAIM-560 indexes is monotone in the
budget here, as it must be. Reachability by a process whose choices
depend on the remaining budget is not. That is the separation
CLAIM-tmpff0cq states.
