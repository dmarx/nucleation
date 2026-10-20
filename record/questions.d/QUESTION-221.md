---
number: 221
status: Open
formerly:
- QUESTION-tmpt64jh
title: 'Does near-decomposability bound dynamical dependence: when the coupling into a block from the rest of the system is at most ε, is the dynamical dependence of the block''s aggregate small to a stated order in ε, and is the converse false?'
version: 1
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-19'
line: distributed-agency
refines:
- QUESTION-065
summary: >-
  A5 of the exchange of 2026-10-19 on coarse-to-fine processes, its
  candidate Q1 and its "most valuable near-term result". [THEORY-661](../theory.d/THEORY-661.md) says
  near-decomposability gives approximate closure of block aggregates over
  the long run, by coupling strength, and [THEORY-733](../theory.d/THEORY-733.md) characterizes exact
  closure for linear Gaussian VARs. No entry bounds the one by the other.
  [CLAIM-388](../claims.d/CLAIM-388.md) shows that the converse fails: a closed aggregate need not
  be a weakly coupled block.
answered_by:
- CLAIM-388
- CLAIM-386
- CLAIM-390
- THEORY-771
---
<!-- inactive-ok-file: CLAIM-157 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-221: Does near-decomposability bound dynamical dependence: when the coupling into a block from the rest of the system is at most ε, is the dynamical dependence of the block's aggregate small to a stated order in ε, and is the converse false?

## Why it is a question

The record has two criteria for a unit. [CLAIM-157](../claims.d/CLAIM-157.md) names a block whose
coupling across its edge is weak ([THEORY-661](../theory.d/THEORY-661.md), Simon). [THEORY-257](../theory.d/THEORY-257.md) names a
coarse variable into which no information flows from the rest given its own
history (Barnett and Seth). [CLAIM-157](../claims.d/CLAIM-157.md) already records that they pick
different blocks when coupling is one-way. What is missing is a bound in the
symmetric case. [THEORY-661](../theory.d/THEORY-661.md) states the link only qualitatively:
"Near decomposability gives approximate closure of block aggregates over
the long run, by coupling strength."

## What the record holds

- [THEORY-733](../theory.d/THEORY-733.md): for a stable linear Gaussian VAR, Y = LX is exactly
  independent iff L A_k = B_k L for every lag. A5 proposed the closure
  defect min_B E‖LAX_t − BLX_t‖² as the approximate version, and noted that
  it differs from total prediction error, since a closed macroprocess can
  still have large innovation noise.
- [THEORY-700](../theory.d/THEORY-700.md) and [THEORY-257](../theory.d/THEORY-257.md): in the Gaussian case the dependence is a ratio
  of generalized variances. A5's ½ log det R / det Q, with R and Q the
  innovation covariances of Y given its own past and given the micro past,
  is that form.
- [CLAIM-388](../claims.d/CLAIM-388.md): the converse fails. Under uniform coupling the sum of all
  units is exactly closed while no partition is nearly decomposable.
- The forward half, answered in part on 2026-10-20:
  - For a block's full state in a linear Gaussian VAR(1), dynamical
    dependence is at most ½ log det(I + Σ_YY⁻¹ A_YR C A_YRᵀ), of second
    order in the coupling into the block, whatever the coupling out of it
    ([CLAIM-390](../claims.d/CLAIM-390.md)).
  - For a block's aggregate, the Simon–Ando one-step closure defect is
    exactly QA(I − VQ). Its part from the blocks' own dynamics vanishes
    iff each block has equal column sums ([CLAIM-386](../claims.d/CLAIM-386.md)). Numerically,
    the relative defect after the transient is then second order in ε,
    and first order otherwise.
  - Still open: the aggregate's dynamical dependence itself, rather than
    the deterministic defect, and any bound over a horizon longer than one
    step. The open statement of Simon–Ando ([NOTE-977](../notes.d/NOTE-977.md)) gives no rate.
  - A rate for trajectory error, not dependence: under contraction of the
    fast modules and of the reduced slow system, and a small-gain
    separation ε < ε_c, fast states stay O(ε) from quasi-steady values
    and slow states O(ε) from the reduced trajectory, uniformly in time
    after a transient (Bousquet and Slotine, [THEORY-tmp5mn7l](../theory.d/THEORY-tmp5mn7l.md)).
    It is deterministic. With that estimate the block sums' closure
    defect ε·QCx̃ is O(ε²), matching [CLAIM-386](../claims.d/CLAIM-386.md)'s measured second order.
    One numerical check in the reading, not a proof, put the transfer
    entropy into block sums at second order in ε.

## What would count as an answer

For a stated class (linear Gaussian VAR(1) first), a bound on the
dynamical dependence of a block's aggregate in terms of the size of the
off-block coupling, the spectral gap and the noise covariance, over a
stated horizon; or a family of nearly decomposable systems in which it
stays bounded away from zero as ε → 0. A5 was explicit that the useful
results "would be conditional bounds, with the distributions and norms
explicit."
