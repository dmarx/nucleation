---
number: 755
status: Proposed
formerly:
- CLAIM-tmp449rr
title: 'Dynamical separation of time scales (fast deviations relax, leaving a slow collective variable) and economic separation (costly formation, cheap repeated use) are different and come apart both ways: a slow variable can save no work, and a result reused cheaply need not be an attractor of any dynamics; so amortization is not in general a separation of time scales in the sense of the owner''s scale-separation claim, and a constraint that is both is a further fact'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §3.1. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  A showing that CASE-116's arms do not separate the two: that arm A's slow
  register does save work for some process, or that arm C's archived rule
  is the slow variable of some dynamics in CLAIM-478's sense, so that the
  economic separation it shows is a dynamical one after all.
tags:
- complex-systems
- information-theory
date: '2026-11-19'
line:
- realizability
- distributed-agency
grounds:
- CASE-116
complements:
- CLAIM-478
- CLAIM-475
- CLAIM-303
- CLAIM-443
summary: >-
  A's, from A39 §3 of the exchange "Topological protection explained"
  (2026-11-18), after the owner tied amortization to the record's
  time-scale separation (U14, U17): "Dynamical separation: fast deviations
  relax, leaving an effective collective variable that evolves more
  slowly. Economic separation: expensive formation is separated from
  repeated inexpensive operation". "These are related, but not identical.
  A stable slow variable might save no work, while a frequently reused
  computational result might be amortized successfully without being an
  attractor". [CLAIM-475](CLAIM-475.md)'s summary, written on 2026-10-27, identifies them:
  "A stable specification amortizes the work that made it, which is a
  separation of time scales ([CLAIM-478](CLAIM-478.md))". [CASE-116](../cases.d/CASE-116.md) already holds a witness
  for each direction. A's conjecture that productive constraints often
  have both is not part of the claim. The wording is A's; adopting it is
  the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: ARG-121 CLAIM-478 CLAIM-756 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-755: Dynamical separation of time scales (fast deviations relax, leaving a slow collective variable) and economic separation (costly formation, cheap repeated use) are different and come apart both ways: a slow variable can save no work, and a result reused cheaply need not be an attractor of any dynamics; so amortization is not in general a separation of time scales in the sense of the owner's scale-separation claim, and a constraint that is both is a further fact

## The claim

A39 §3 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):

> Dynamical separation: fast deviations relax, leaving an effective collective variable that evolves more slowly.
>
> Economic separation: expensive formation is separated from repeated inexpensive operation, allowing the initial cost to be distributed over many uses.
>
> These are related, but not identical. A stable slow variable might save no work, while a frequently reused computational result might be amortized successfully without being an attractor of any physical dynamical system.

## Why it is demonstrated

[CASE-116](../cases.d/CASE-116.md)'s three finite-state systems separate the two in both
directions ([ARG-121](../arguments.d/ARG-121.md)). Arm A is a slow flip register that no member
reads: dynamically separated, with second eigenvalue 0.98, and saving no
one any work. Arm C passes a rule through an archive between two episodes
that never run together: the second episode reuses the rule without
rederiving it, and nothing relaxes onto anything.

## What it corrects

[CLAIM-475](CLAIM-475.md)'s summary says that a stable specification's amortization "is
a separation of time scales ([CLAIM-478](CLAIM-478.md))". That holds for the economic
sense. [CLAIM-478](CLAIM-478.md)'s sense is the dynamical one, so the identification is a
slip of wording. [CLAIM-475](CLAIM-475.md)'s claim itself does not depend on it.

## The stronger reading it invites and does not support

That the two are unrelated. A conjectured that "many productive emergent
constraints instantiate both separations at once", and that the work one
stabilized organization saves can be invested in forming another
([CLAIM-761](CLAIM-761.md), [CLAIM-756](CLAIM-756.md)). Whether they usually coincide is open.

## Note of 2026-11-20: what holds it back

The second direction's witness may meet the claim's own defeated_if: arm A counts as dynamically separated by slowness alone (second eigenvalue 0.98; nothing relaxes onto Z), and by that measure arm C's archive, once counted as a state of the system, is slower still: eigenvalue 1 across the gap, read by episode B and fixed on B's time scale, which makes it a constraint in [CLAIM-478](CLAIM-478.md)'s sense, the case of "a rule stored in a file" that [CLAIM-478](CLAIM-478.md) itself names. What is missing is either a definition of dynamical separation, such as relaxation onto a slow variable, under which arm A's register counts and arm C's archive does not, or a witness in which a result is reused cheaply while held by no variable slower than its uses, such as one result read by many users at once. [ARG-121](../arguments.d/ARG-121.md)'s second critical question qualifies arm C's saving, not its dynamics, and the first direction, a slow variable that saves no work, is not in doubt.

## Note of 2026-11-25: rerun, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-252](../leads.d/LEAD-252.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). No script was kept, so the computations this claim cites from its ground [CASE-116](../cases.d/CASE-116.md) were rebuilt from the entries as `scratch/formal/scale_separation_arms_check.py` (numpy), run with python3 -I: arm A's joint chain has eigenvalues 1, 0.98 and six zeros, and dependence on Z's start decays as 0.98^t (0.904 at t = 5, 0.133 at t = 100); arm B's register has eigenvalues 1 and 0.2, with P(Z′ = 1) = 0.4 and 0.6 under do(Z = 0) and do(Z = 1); arm C's archive, counted as a state, has eigenvalue 1 across the gap and B follows θ_A. Everything reproduces. What holds it back is not computation: the note of 2026-11-20 above, which the rerun confirms rather than answers. Counted as a state, arm C's archive is the slowest variable there is (eigenvalue 1), so by the slowness-only measure arm A is judged by, arm C is dynamically separated too. The missing definition or witness that note names is still missing. The note is the assistant's (Claude, in this session). No status change.
