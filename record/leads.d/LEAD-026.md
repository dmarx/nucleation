---
number: 26
status: Open
formerly:
- LEAD-tmp2guat
title: 'Simulate populations with the same turnover and aggregate statistics where the criteria of individuality disagree, and test a search procedure and a lagged block criterion against them'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: carried out on a simulated model
    (CASE-347, CLAIM-926); what remains is listed. Status and
    stage unchanged.
stage: specified
priority: medium
method:
- empirical
- formal
tags:
- individuation
- information-theory
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-115
- QUESTION-116
- CLAIM-157
- CLAIM-194
operationalized_in:
- CASE-101
summary: >-
  Named in [QUESTION-115](../questions.d/QUESTION-115.md) and [QUESTION-116](../questions.d/QUESTION-116.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-347 CLAIM-926 — new, filed 2026-11-22 from LEAD-026's study -->

# LEAD-026: Simulate populations with the same turnover and aggregate statistics where the criteria of individuality disagree, and test a search procedure and a lagged block criterion against them

## What it would do

Run [CASE-101](../cases.d/CASE-101.md)'s three populations and apply [QUESTION-115](../questions.d/QUESTION-115.md)'s search procedure
and a lagged block criterion to each.

Where the record names it:

- [QUESTION-115](../questions.d/QUESTION-115.md): "A specified search procedure that recovers independently
  known system boundaries and characteristic timescales in controlled
  models"
- [QUESTION-116](../questions.d/QUESTION-116.md): "rejects a population whose members are correlated only
  because they receive the same input"

## What would count

A procedure that recovers the known boundaries and rejects the commonly
driven population answers [QUESTION-115](../questions.d/QUESTION-115.md) and [QUESTION-116](../questions.d/QUESTION-116.md) for the model.

## Note of 2026-11-22: carried out on a simulated model

**What was done.**

- *The populations.* [CASE-101](../cases.d/CASE-101.md)'s three arms were simulated with numpy, with
  pytest tests. A fourth arm, C0, has an institution that does not answer
  to its members. All are matched in turnover, member variance, member
  correlation and the aggregate's lag-1 autocorrelation.
- *The search.* [QUESTION-115](../questions.d/QUESTION-115.md)'s search was applied: Krakauer et al.'s
  retention measures at lags 1 to 64, Bourrat's interventional retention,
  and transfer entropy into each candidate.
- *The lagged block.* A block test priced by [CLAIM-154](../claims.d/CLAIM-154.md) was run on all
  subsets at windows of 1 to 16 steps.
- *Where it is filed.* The study is [CASE-347](../cases.d/CASE-347.md) and the finding is
  [CLAIM-926](../claims.d/CLAIM-926.md). The materials are under scratch/studies/lead-026/.

**The result, against "What would count".**

- The procedure recovers the transmitting population with its lag.
- It recovers the institutional population's boundary, which includes the
  institution.
- It rejects the commonly driven members alone only while their driver is
  observed. It joins them to the driver, the same verdict it gives a
  population held by an institution that does not answer to it.

So the procedure meets the criterion for B and C. For A it meets it only
relative to an observed set that contains the input. Whether that answers
[QUESTION-115](../questions.d/QUESTION-115.md) and [QUESTION-116](../questions.d/QUESTION-116.md) for the model is the owner's call.

**What remains.**

- Effective information and the macrostate leg of [QUESTION-115](../questions.d/QUESTION-115.md).
- Sensitivity:
  - a driver as persistent as B's tradition, where A(Δ) with the driver
    hidden may no longer separate B;
  - other priors for the price;
  - a nonlinear or discrete version, where the estimates are not only
    linear-Gaussian lower bounds.
- The same lagged test on the dancing couple ([LEAD-037](LEAD-037.md)), or on a stored
  artifact such as [CASE-043](../cases.d/CASE-043.md).

Status and stage are unchanged.
