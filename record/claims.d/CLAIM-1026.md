---
number: 1026
status: Proposed
formerly:
- CLAIM-tmp4ybsw
title: 'One adopted line cannot settle the defeater'
statement: >-
  One adopted line from a top-circulated video favours a circulation model
  over a list of identifiable contributions that names the distributors by
  at most about five to one, and by under two when the case is known partly
  for the video's fame, so a single case like the Juggernaut line cannot
  meet or discharge a defeater that asks the network model to beat that list
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, from scratch/studies/lead-188/
    (model.py, 8 tests passing; results.json; sensitivity.jsonl, 36
    settings).
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of the committed scripts that does not reproduce the stated
  ranges; or, within the model's own family (percolation on a
  heavy-tailed network, one adopted video, priors as stated), a setting
  in which the Bayes factor of circulation over the list with named
  distributors exceeds about ten without ascertainment, or about three
  with full ascertainment. A different observation (several adopted
  videos, timing, the route itself) is not this claim's and does not
  count.
tags:
- model-comparison
- social-ontology
- network-science
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-119
grounds:
- CASE-410
summary: >-
  [CLAIM-332](CLAIM-332.md)'s defeater asks whether a circulation-network model adds to
  the list of identifiable creators, distributors and decision-makers,
  priced so that the network is not credited for its parameters. In a
  percolation model of fan videos on a heavy-tailed network, with one
  decision-maker adopting one line, the Juggernaut case's one observation
  (the adopted video was among the top 1% by reach) gives exact Bayes
  factors over stated priors of 10 to 32 for circulation over a list
  without distributors, 2.3 to 4.7 over a list with them, and 1.3 to 1.6
  over either if the case was ascertained by fame. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-410 — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-332 — Proposed; the thesis whose defeater is priced here -->

# CLAIM-1026: One adopted line cannot settle the defeater

## The claim

The model and runs are in [CASE-410](../cases.d/CASE-410.md). Three accounts of which video
a decision-maker adopts: M0, a list without distributors (all equally
likely); MH, a list naming the distributors (weight 1 + κ·hubs reached);
MC, circulation (weight s^α, s the video's reach). The observation is
that the adopted video is in the top 1% by reach. With weight s^γ for
the chance that the case came to the record's notice:

| ascertainment | MC over M0 | MH over M0 | MC over MH |
|---|---|---|---|
| none | 10 to 32 | 3.0 to 12 | 2.3 to 4.7 |
| full (γ = 1) | 1.47 to 1.64 | 1.0 to 1.14 | 1.33 to 1.60 |

(36 settings: network size, number of named distributors, transmissibility
prior, seed.)

## Why it is demonstrated

The figures are computed, not estimated from data about 2006: within the
stated model the Bayes factors are what they are, checked by tests (MC at
α = 0 equals M0; M0 without ascertainment gives exactly q; MC is
monotone in α). What carries over to the real case is the shape: one
adopted video carries at most one observation's worth of evidence, and
it is confounded with how the case was chosen.

## Pricing

[CLAIM-154](CLAIM-154.md)'s rule is the large-sample form of a Bayes factor; with one
observation the exact marginal likelihood is used instead, which is what
the rule approximates. The circulation model is regular where α = 0
switches it off, so the narrowing to regular candidates ([CLAIM-188](CLAIM-188.md)) does
not bite. The priors are stated, and a wider prior on α would lower MC's
marginal likelihood further.

## What it does not say

- That circulation did not matter. A list that names the sites that
  carried the video already absorbs most of what reach explains, because
  in a heavy-tailed network the far-reaching videos are the ones the hubs
  carried.
- What a study of many adoptions would show. The test [CLAIM-332](CLAIM-332.md) needs is
  cross-case: across many videos, does adoption track reach beyond what
  the named distributors predict?
