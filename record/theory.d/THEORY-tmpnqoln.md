---
status: Proposed
promote_when: >-
  An independent simulation, or the authors' released code rerun on their
  data, reproduces lower mean allocation cost for the Markov preparedness
  policy than for the nine comparators in most of the configurations the
  paper reports.
title: 'Guigues, Kleywegt and Nascimento propose that a per-station steady-state Markov-chain preparedness metric, used inside a one-step integer program for ambulance selection and reassignment, gives a real-time EMS policy whose mean allocation cost is lower than nine published dispatch policies in most simulated Rio de Janeiro configurations'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmphy35q
summary: >-
  Guigues, Kleywegt and Nascimento (2026), [LIT-tmphy35q](../literature.d/LIT-tmphy35q.md), read in part in
  [NOTE-tmp5y2s6](../notes.d/NOTE-tmp5y2s6.md). Proposed: the metric and policies were read in full, but
  the comparison rests on a simulation with assumed allocation costs whose
  per-figure results were skimmed, in an unrefereed preprint. The account
  is about mean allocation cost in one city's simulated system; it does
  not say the policy beats approximate dynamic programming, which was not
  compared, or that it holds under heavy load, where the authors say the
  metric may be inaccurate.
---
<!-- inactive-ok-file: NOTE-tmp5y2s6 — Skimmed; the reading this account comes from -->

# THEORY-tmpnqoln: Guigues, Kleywegt and Nascimento propose that a per-station steady-state Markov-chain preparedness metric, used inside a one-step integer program for ambulance selection and reassignment, gives a real-time EMS policy whose mean allocation cost is lower than nine published dispatch policies in most simulated Rio de Janeiro configurations

## Source

Guigues, Kleywegt and Nascimento (2026), [LIT-tmphy35q](../literature.d/LIT-tmphy35q.md); read in part in
[NOTE-tmp5y2s6](../notes.d/NOTE-tmp5y2s6.md).

## What was actually shown

- **The metric (§2).** For each station and supply vector, the
  steady-state cost rate of a continuous-time Markov chain over the
  station's busy ambulances by type, computed offline (Table 2: up to
  346,000 s for 16 ambulances).
- **The policies (§§3–4).** Each selection or reassignment decision
  solves a small integer program trading immediate cost, a queueing
  penalty and Γ times the change in preparedness, in milliseconds.
- **The comparison (§5, §7).** Simulated on Rio de Janeiro data with two
  distance models and two discretizations; "In most cases, this policy
  performed better than the 9 policies in terms of mean allocation
  costs" (p. 29), and it was among the best on mean response time. In the
  first configuration it was best at every fleet size but 12 (p. 21).
  Source code and data are released (§6).

## What this does not say

- That the metric beats approximate dynamic programming: the ADP
  policies were not among the nine.
- That the costs are right: they are assumed, and the authors say the
  results "serve as examples only, and not as guidelines for dispatching
  decisions" (p. 12).
- That it holds when demand is large relative to supply, where the local
  approximation "may be inaccurate" (p. 13).
- Anything about patient outcomes, or beyond one city.
