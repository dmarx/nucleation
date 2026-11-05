---
number: 1388
status: Proposed
formerly:
- THEORY-tmpegbva
promote_when: >-
  The multi-period formulations of §3 read, confirming that both the FLEET
  and the local-reliability expected covering models are given forms over
  several periods that let ambulances move among bases between periods,
  and that the number of bases is traded against coverage as a second
  objective, for the emergency medical service of Belo Horizonte.
title: "De Oliveira, de Sá and Martins give multi-period forms of the FLEET and local-reliability expected covering models, letting ambulances move among bases between periods, and trade the number of bases against coverage as a bi-objective problem, for Belo Horizonte's emergency medical service"
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2092
summary: >-
  De Oliveira, de Sá and Martins (2020), [LIT-2092](../literature.d/LIT-2092.md), read in part in
  [NOTE-1621](../notes.d/NOTE-1621.md) (the abstract and §2). Proposed: the account is the
  abstract's description of the paper's models, whose formulations in §3
  were not read. The coverage gains the abstract reports are not part of
  the account. What was read, §2, is the paper's survey of MEXCLP, MALP and
  LR-MEXCLP, and bears on the unread Daskin (1983) and ReVelle and Hogan
  (1989), not on this account.
---
<!-- inactive-ok-file: NOTE-1621 — Skimmed and new; the reading this account comes from, cited as open -->

# THEORY-1388: De Oliveira, de Sá and Martins give multi-period forms of the FLEET and local-reliability expected covering models, letting ambulances move among bases between periods, and trade the number of bases against coverage as a bi-objective problem, for Belo Horizonte's emergency medical service

## Source

De Oliveira, de Sá and Martins (2020), [LIT-2092](../literature.d/LIT-2092.md); read in [NOTE-1621](../notes.d/NOTE-1621.md).

## What was actually shown

- **The abstract.** "The proposed multi-period models introduce the concept
  of relocation to the local EMS, which allows ambulances to move among
  bases in different periods to raise the system coverage", and "This
  paper also proposes a bi-objective approach aiming to minimize the number
  of bases and maximize the coverage of demands".
- **The models it builds on** (§2, read): LR-MEXCLP's reliability
  q_{i,k} = 1 − (b_{i,k})^k for k servers in a neighbourhood with
  area-specific busy fraction b_{i,k}.

The formulations themselves were not read.

## What this does not say

- That relocation raises coverage by the amounts the abstract reports;
  those figures were not checked.
- That the probabilistic model escapes the independence assumption: by the
  paper's own §2, LR-MEXCLP still assumes independent servers and locally
  constrained service areas.
- Anything about the value of an idle or rarely used ambulance.
