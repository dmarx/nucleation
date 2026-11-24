---
status: Proposed
version: 1
standing: stipulated
kind: construction
tags:
- society-and-governance
- epistemology
date: '2026-11-24'
line:
- dependence-and-domination
- organizational-normativity
illustrates:
- CLAIM-350
- CLAIM-670
title: "Retention under switching costs, stipulated: with retention a logistic function of a service's quality less an alternative's value plus the cost of switching, a service of quality 80 that costs nothing to leave and one of quality 20 that costs 60 to leave keep the same 63.5 percent of their customers, so the retention figure merges satisfaction with lock-in"
summary: >-
  A46 §4 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24): retention as a KPI that "can merge all these
  circumstances", from excellence to the cost of leaving, and the lesson
  "Continued participation is not necessarily satisfaction." The model is
  A46's; the matched pair and the numbers are the assistant's check (python3
  -I). It illustrates CLAIM-350's fibres and CLAIM-670's dependence produced
  by an arrangement. The model's wording is A's (ChatGPT, in the exchange
  "Memes, Contracts, and Systemic Normativity"); the pair is the assistant's
  (Claude, in this session); adopting either is the owner's call.
---

<!-- inactive-ok-file: CLAIM-670 THEORY-150 THEORY-152 — Proposed; the claim illustrated and the held accounts of exit -->

# CASE-tmp3so1p: Retention under switching costs, stipulated: with retention a logistic function of a service's quality less an alternative's value plus the cost of switching, a service of quality 80 that costs nothing to leave and one of quality 20 that costs 60 to leave keep the same 63.5 percent of their customers, so the retention figure merges satisfaction with lock-in

## The case

A46 §4's model: an alternative service gives 75 units of value before the
cost of switching; with quality q and switching cost s, retention is
σ((q − 75 + s)/9), with σ the logistic function. "Stipulated logistic
response, not empirical data."

Checked with python3 -I:

| quality q | switching cost s | retention |
|---|---|---|
| 80 | 0 | 63.5% |
| 20 | 60 | 63.5% |
| 80 | 35 | 98.8% |
| 40 | 35 | 50.0% |
| 40 | 60 | 94.1% |
| 40 | 0 | 2.0% |

The first two rows are the point. Same retention, one service good and free
to leave, the other poor and costly to leave: one fibre of the retention
map holds both, and any judgment that tells them apart (satisfaction,
consent, whether the provider owes better terms) does not factor through
retention (CLAIM-350). The last three rows are A46's: "Increasing switching
costs can sustain retention even as service quality deteriorates."

## What A46 draws from it

"This produces a particularly important form of measurement naivety:
**treating behavior under constraint as evidence of unconstrained
endorsement**. Continued participation is not necessarily satisfaction.
Compliance is not necessarily agreement. Tolerance is not necessarily
consent."

And a separation: "a greedy institution need not be naive about these
distinctions. It may understand perfectly well that retention increasingly
reflects lock-in rather than satisfaction. Measurement naivety and
exploitation are therefore separate mechanisms."

## Held around it

CLAIM-670, an arrangement producing the dependence it exploits, which A46
§3 calls "almost exactly the mechanism"; Doctorow's decay "set by the cost
of leaving" (THEORY-150); Hirschman's exit as a recuperation signal
(THEORY-152), which the case shows silenced by the cost of exit.
