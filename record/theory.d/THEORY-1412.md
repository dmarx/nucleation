---
number: 1412
status: Active
formerly:
- THEORY-tmpnqoln
title: 'Guigues, Kleywegt and Nascimento propose that a per-station steady-state Markov-chain preparedness metric, used inside a one-step integer program for ambulance selection and reassignment, gives a real-time EMS policy whose mean allocation cost is lower than nine published dispatch policies in most simulated Rio de Janeiro configurations'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the thirtieth status review, at the status review's
    ruling (the owner delegated these rulings), under ADR-065: the title
    reports what one study proposes and found, with its hedges, and
    NOTE-1567 v2 reads it in full, the figures checked by
    scratch/formal/guigues_figures_check.py. The promotion condition
    asked for replication, and it moves unchanged to QUESTION-444.
    It read: 'An independent simulation, or the authors' released code
    rerun on their data, reproduces lower mean allocation cost for the
    Markov preparedness policy than for the nine comparators in most of
    the configurations the paper reports.' The body now gives the
    reviewer's reading of the figures beside the authors' statements,
    including on mean response time.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2066
summary: >-
  Guigues, Kleywegt and Nascimento (2026), [LIT-2066](../literature.d/LIT-2066.md), read in full in
  [NOTE-1567](../notes.d/NOTE-1567.md). Active as one simulation study's finding, in an unrefereed
  preprint, with assumed allocation costs that the policy itself
  optimizes. It does not say the policy beats approximate dynamic
  programming, which was not compared, that it holds when ambulances are
  few relative to demand, where it lost, or that it gives the shortest
  response times, which it seldom did. Whether the result reproduces is
  [QUESTION-444](../questions.d/QUESTION-444.md).
bears_on:
- QUESTION-444
---
# THEORY-1412: Guigues, Kleywegt and Nascimento propose that a per-station steady-state Markov-chain preparedness metric, used inside a one-step integer program for ambulance selection and reassignment, gives a real-time EMS policy whose mean allocation cost is lower than nine published dispatch policies in most simulated Rio de Janeiro configurations

## Source

Guigues, Kleywegt and Nascimento (2026), [LIT-2066](../literature.d/LIT-2066.md); read in full in
[NOTE-1567](../notes.d/NOTE-1567.md).

## What was actually shown

- **The metric (§2).** For each station and supply vector, the
  steady-state cost rate of a continuous-time Markov chain over the
  station's busy ambulances by type, computed offline (Table 2: up to
  346,000 s for 16 ambulances).
- **The policies (§§3–4).** Each selection or reassignment decision
  solves a small integer program trading immediate cost, a queueing
  penalty and Γ times the change in preparedness, in milliseconds.
- **The comparison (§5, §7).** Simulated on Rio de Janeiro data with two
  distance models and two discretizations. The authors: "In most cases,
  this policy performed better than the 9 policies in terms of mean
  allocation costs, and this policy also performed among the best of the
  9 policies in terms of mean response time" (p. 29).
- **The figures, read by the reviewer.** Read from the plotted series of
  Figures 1–8 (the reviewer's reading of the vector paths, not the
  authors' statement): lowest mean allocation cost at 38 of 46 fleet
  sizes, every loss at 14 ambulances or fewer; lowest mean response time
  at 2 of 46, usually fifth of ten
  (scratch/formal/guigues_figures_check.py). In Figure 1 the one loss is
  at 12 ambulances, where the text says "the heuristic of (Andersson and
  Värbrand, 2007) is slightly better" (p. 21) but the plotted series
  below MP is Lee (2011)'s.
- **Code.** Source code and data are stated to be released (§6). No
  replication counts or intervals are reported for the simulated means.

## What this does not say

- That the metric beats approximate dynamic programming: the ADP
  policies were not among the nine.
- That it wins on a measure it does not optimize: its integer programs
  use the allocation costs it is scored on, and most comparators target
  response time.
- That the costs are right: they are assumed, and the authors say the
  results "serve as examples only, and not as guidelines for dispatching
  decisions" (p. 12).
- That it holds when demand is large relative to supply, where the local
  approximation "may be inaccurate" (p. 13).
- Anything about patient outcomes, or beyond one city.
