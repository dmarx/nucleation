---
number: 178
status: Open
formerly:
- LEAD-tmpvzskp
title: 'Bound the dynamical dependence of a block''s aggregate in terms of off-block coupling, gap and noise, linear Gaussian VAR(1) first'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- complex-systems
- information-theory
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-221
summary: >-
  Named in [QUESTION-221](../questions.d/QUESTION-221.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-178: Bound the dynamical dependence of a block's aggregate in terms of off-block coupling, gap and noise, linear Gaussian VAR(1) first

## What it would do

Derive the bound for VAR(1), or construct a nearly decomposable family in
which it stays bounded away from zero as coupling vanishes.

Where the record names it:

- [QUESTION-221](../questions.d/QUESTION-221.md): "a bound on the dynamical dependence of a block's
  aggregate"

## What would count

Either answers [QUESTION-221](../questions.d/QUESTION-221.md) for the class.

## Note of 2026-11-22: what was done
<!-- inactive-ok-file: CASE-tmp2l6id CLAIM-tmpllgpb — new; filed from this lead -->

Worked on the branch claude/lead-178-var1-dependence
(scratch/studies/lead-178/). For linear Gaussian VAR(1) at the one-step
horizon both outcomes the lead names were reached, under a condition on
the block. [CLAIM-tmpllgpb](../claims.d/CLAIM-tmpllgpb.md) bounds the dynamical dependence of any linear
aggregate on both sides. For A = A* + εC it is of order ε² when the
block's aggregate is closed under A* (for the sum, equal column sums),
with a constant growing as the slow gap closes, and has a positive floor
as ε → 0 when it is not, whatever the fast gap. [CASE-tmp2l6id](../cases.d/CASE-tmp2l6id.md) is the
numerical study.

Choices made: "the block's aggregate" was read as the block sum, as in
[CLAIM-386](../claims.d/CLAIM-386.md); the bound holds for any linear aggregate, and the study also
ran the left-Perron-weighted one, which is closed. The horizon is Barnett
and Seth's one step given the whole past.

What remains:

- **A longer horizon,** which [QUESTION-221](../questions.d/QUESTION-221.md) also asks for.
- **A rate in the gap.** The ε² constant's growth as the slow gap closes
  was measured slower than the 1/gap of the explicit bound; its true
  order is not derived.
- **Beyond the class:** Markov chains ([NOTE-1030](../notes.d/NOTE-1030.md)'s target), VAR(p),
  nonlinear systems.
