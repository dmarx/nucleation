---
status: Proposed
title: 'weak direction (in a learned model), in six senses that come apart'
version: 1
tags:
- information-geometry
- learning-theory
- representation-learning
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
draws_on:
- THEORY-087
- THEORY-420
- THEORY-186
summary: >-
  A41's table of spectra in the exchange "Rich Get Richer Power Laws"
  (2026-11-21), with its three kinds of weakness (A41 §5) and A37 §7's
  warning that singular values are not singularities, put together as one
  term so that a claim about a "small" or "weak" direction says which.
  The record had pieces in [THEORY-078](../theory.d/THEORY-078.md) and [THEORY-084](../theory.d/THEORY-084.md) and no term. The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A37, A41), assembled by the assistant (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: THEORY-186 THEORY-084 THEORY-078 CLAIM-tmpcgvcp CLAIM-tmppkdjz CASE-tmpb2gly — Proposed or new; cited for the sense each fixes -->
<!-- inactive-ok-file: TERM-tmptiim0 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# TERM-tmpnxjq4: weak direction (in a learned model), in six senses that come apart

## Definition

A **weak direction** is a direction v, in parameters or in a
representation, along which some quadratic form or local expansion is
small. The term is always used with its sense stated. Six senses:

| sense | small quantity | space | what "small" means |
|---|---|---|---|
| 1. low variance | vᵀC_repr v | representation | little of the data's spread lies along v |
| 2. small singular value | vᵀWᵀWv | input of a weight matrix W | W amplifies v little |
| 3. low curvature | vᵀHv | parameters | the loss changes little to second order |
| 4. sloppy | vᵀIv, with I invertible | parameters | predictions change little; identified given enough data |
| 5. singular | vᵀIv = 0, higher-order effect nonzero | parameters, on a stratum | no first-order effect on the predictions, but an effect at higher order (a²b² at the origin) |
| 6. redundant | the function does not change at any order | parameters | a true symmetry: permutation, rescaling, a dead unit |

Senses 1–4 are from A41's table ("A direction can be small in one of
these geometries and extremely important in another"). Senses 4–6 are
A41 §5's three kinds of weakness: "Small but nonzero functional
sensitivity. Exactly zero first-order sensitivity with nonzero
higher-order effects. Genuine parameter redundancy with no change to the
implemented function." The Fisher matrix in 4 and 5 is relative to a
stated observation (I = JᵀJ/σ² for Gaussian noise, or a pullback such as
Wᵀ(diag p − ppᵀ)W to a hidden state), and changing the observation changes
the ranking ([CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md)).

## What it must not be confused with

- **Singular value and singularity.** "It's important not to confuse the
  singular values in that result with algebraic singularities in
  Watanabe's theory" (A37 §7). The strong singular modes Saxe et al.'s
  networks learn first ([THEORY-186](../theory.d/THEORY-186.md)) are sense 2, applied to a
  correlation matrix. A singularity is sense 5. A small singular value is
  not a singularity: polynomial regression has an ill-conditioned design
  and no singular point ([CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md)).
- **Sloppy and singular.** Sense 4 and sense 5 differ in kind, not in
  degree, though 4 can approach 5 near a stratum ([CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md),
  [CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md)).
- **Weak and unimportant.** None of the six says a direction does not
  matter to the task. A label can sit wholly in a sense-1 weak direction
  ([CLAIM-tmppkdjz](../claims.d/CLAIM-tmppkdjz.md)), and [THEORY-420](../theory.d/THEORY-420.md) holds a reading in which zeroing
  sense-2 weak directions can damage a trained transformer.

## Note of 2026-11-21: Transtrum, Machta & Sethna (2011) and Transtrum et al. (2015), read

Qualifies sense 4 (sloppy: vᵀIv with I invertible, "identified given
enough data"). In the sources a sloppy direction runs to the manifold's
boundary, mostly at parameters going to 0 or ∞: "Any parameter can be
varied by an infinite amount and the model could still fit the data"
(2015, §I), and best fits to noisy data "evaporate" parameters to extreme
values along directions thinner than the noise (2011, §III). Near the
point where I is evaluated, more data do identify the direction; globally,
at a fixed design, a sloppy combination can be unidentified because it
runs to a boundary, where the metric is singular (2011, p. 10). Sense 4
holds locally; the sources' sloppiness mixes it with a global failure of
identification that sense 5 (singular) captures at the edges
([TERM-tmptiim0](TERM-tmptiim0.md), version 2).
