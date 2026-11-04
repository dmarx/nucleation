---
status: Proposed
promote_when: >-
  The convergence proof read and checked, confirming that for the spatial
  hypercube queueing model with server-specific exponential service rates
  the authors' iteration, built on a birth–death process and an
  equivalent reformulation, converges to the exact stationary
  distribution at a geometric rate.
title: 'Hua, Luo, Swersey and Wen solve the spatial hypercube queueing model with server-specific service rates exactly, through a birth–death process and an equivalent reformulation whose iteration converges to the stationary distribution at a geometric rate'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmpws93a
summary: >-
  Hua, Luo, Swersey and Wen (2026), [LIT-tmpws93a](../literature.d/LIT-tmpws93a.md), read in part in
  [NOTE-tmpx391x](../notes.d/NOTE-tmpx391x.md) (§1, the model statement, the TOUR paragraph and the
  comparison of §5). Proposed: the extension and the geometric convergence
  are stated in the abstract and introduction, but the proof was not read.
  The reported speed-ups against a sparse solver, simulation and Larson's
  own method are not part of the account and were not checked against the
  tables.
---
<!-- inactive-ok-file: NOTE-tmpx391x — Skimmed and new; the reading this account comes from, cited as open -->

# THEORY-tmptcu66: Hua, Luo, Swersey and Wen solve the spatial hypercube queueing model with server-specific service rates exactly, through a birth–death process and an equivalent reformulation whose iteration converges to the stationary distribution at a geometric rate

## Source

Hua, Luo, Swersey and Wen (2026), [LIT-tmpws93a](../literature.d/LIT-tmpws93a.md); read in [NOTE-tmpx391x](../notes.d/NOTE-tmpx391x.md).

## What was actually shown

- **The claim, as stated.** "we extend it to handle heterogeneous service
  rates by devising an exact solution through a birth-death process and an
  equivalent reformulation. We demonstrate that our algorithm converges to
  the exact solution at a geometric rate" (abstract). The introduction adds
  that the result extends to homogeneous rates and that the proof bounds
  the differences between consecutive iterations.
- **Its place.** Larson's alternating hyperplane approach is the earlier
  exact method for homogeneous rates (§1); against a reimplementation of
  it, "In the case of 20 units, our algorithm is approximately 83% faster
  in terms of total time" (§5).

Nothing here was checked beyond the authors' statements.

## What this does not say

- That the method scales without limit: exact solution still works over
  the 2^N states.
- Anything about the approximation methods' accuracy, except that the
  authors say they lack convergence guarantees.
- Anything about facility location, districting or the value of a unit.
