---
status: Proposed
promote_when: >-
  In the paper's Edmonton comparisons, evaluated by the approximate
  hypercube model, the survival-maximizing deterministic model yields more
  expected cardiac-arrest survivors than the maximal covering and q-median
  solutions at some station counts, and the survival objective's advantage
  over coverage is smaller in the models with random response times or
  busy probabilities than in the deterministic ones, as the paper's
  tables report; or a rerun on the published Edmonton data reproduces
  both.
title: 'Erkut, Ingolfsson and Erdoğan show that locating ambulances to maximize expected cardiac-arrest survivors, rather than coverage within a time standard or average response time, saves more lives in deterministic models, with the advantage shrinking once random response times or ambulance busy probabilities enter the coverage model'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmprfb8b
summary: >-
  Erkut, Ingolfsson and Erdoğan (2008), [LIT-tmprfb8b](../literature.d/LIT-tmprfb8b.md), read in [NOTE-tmp241k1](../notes.d/NOTE-tmp241k1.md).
  Proposed: the comparisons are the paper's own, on one city's data, with
  survival functions for cardiac arrest assumed for all urgent calls and a
  non-optimal heuristic for the richest models. The account is about
  expected survivors under the authors' survival functions and evaluation
  model; it does not say coverage is useless, since by the paper's Table 6
  coverage with either source of uncertainty reaches the best-known value.
---

# THEORY-tmpagbfa: Erkut, Ingolfsson and Erdoğan show that locating ambulances to maximize expected cardiac-arrest survivors, rather than coverage within a time standard or average response time, saves more lives in deterministic models, with the advantage shrinking once random response times or ambulance busy probabilities enter the coverage model

## Source

Erkut, Ingolfsson and Erdoğan (2008), [LIT-tmprfb8b](../literature.d/LIT-tmprfb8b.md); read in [NOTE-tmp241k1](../notes.d/NOTE-tmp241k1.md).

## What was actually shown

- **Deterministic models (§4.2).** On Edmonton data (180 demand points,
  16 candidate sites), maximal-covering solutions give up to 7.7% fewer
  expected survivors and q-median solutions up to 23.5% fewer than the
  survival-maximizing MSLP (pp. 12–13); the MSLP solutions were the same
  under three survival functions (p. 14).
- **Random response times (§6.1, Table 2).** MSLP+PR over MCLP+PR: up to
  5.3%, 0.9% on average over 16 problems, equal in 8 of them (p. 18).
- **Busy probabilities (§6.2).** For MEXCLP+PR "the inclusion of the
  survival function does not add much" (p. 20).
- **Average response time (§6.3, Table 5).** MEXSLP+PR beats Jarvis's
  heuristic by 6.5% on average and up to 21.6% (p. 21).
- **All ten models (§6.4, Table 6).** At six vehicles and busy probability
  0.3, coverage rises from 761.6 to 809.1 expected survivors with either
  source of uncertainty, the survival models give 809.1 in every version,
  and average response time stays at or below 745.0 (p. 22).

These are optimizations and evaluations that could have come out the
other way: the survival objective could have picked the same locations as
coverage, as it sometimes did.

## What this does not say

- That coverage is always a bad proxy: realistic coverage models reached
  the survival optimum in Table 6.
- Anything about calls other than cardiac arrest, which the authors name
  as their main shortcoming (p. 23).
- Anything about dispatch, relocation or response-time thresholds as
  performance measures: these are static location models.
- That it holds beyond Edmonton.
