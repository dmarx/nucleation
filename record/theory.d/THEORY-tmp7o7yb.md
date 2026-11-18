---
status: Proposed
promote_when: >-
  The update's convergence to stationary points (by the concave–convex
  procedure) and its identity with one attention step at β = 1/√d_k
  (Eq. 10) re-derived from the definitions, and the capacity and one-step
  retrieval bounds (Theorems 3–5) checked against their proofs in the
  appendix or reproduced numerically on random patterns on the sphere.
  Measurements of how trained transformers' heads behave cannot settle it:
  the entry asserts what the update computes and what it can store, not
  what trained models do.
title: 'For N patterns stored on a sphere in R^d, the continuous Hopfield update ξ ← X softmax(βXᵀξ) descends an energy −lse(β, Xᵀξ) + ½ξᵀξ to a stationary point, can store a number of random patterns exponential in d with high probability, and retrieves a well-separated pattern in one step with error exponentially small in its separation; through key, query and value projections at β = 1/√d_k, one such update is transformer attention, as Ramsauer et al. prove'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed Proposed from NOTE-tmp2munq, the reading of Ramsauer et al.'s
    main text in full on 2026-11-15; the proofs were not read or checked.
tags:
- representation-learning
- information-retrieval
- neuroscience
date: '2026-11-15'
source:
- LIT-tmpxroua
summary: >-
  Ramsauer et al. (2020; venue reported as ICLR 2021, unconfirmed),
  [LIT-tmpxroua](../literature.d/LIT-tmpxroua.md), read in [NOTE-tmp2munq](../notes.d/NOTE-tmp2munq.md): a continuous modern Hopfield
  network whose one-step update is softmax attention, with proved
  convergence, exponential capacity for random patterns and one-step
  retrieval for separated ones. The theorems are carried as stated; the
  proofs, in a roughly 90-page appendix, were not read. It says what one
  attention step computes, not that trained keys act as attractors. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1030 — Proposed; the FFN-memory reading, cited as open -->

# THEORY-tmp7o7yb: For N patterns stored on a sphere in R^d, the continuous Hopfield update ξ ← X softmax(βXᵀξ) descends an energy −lse(β, Xᵀξ) + ½ξᵀξ to a stationary point, can store a number of random patterns exponential in d with high probability, and retrieves a well-separated pattern in one step with error exponentially small in its separation; through key, query and value projections at β = 1/√d_k, one such update is transformer attention, as Ramsauer et al. prove

## Source

Ramsauer et al. (2020), [LIT-tmpxroua](../literature.d/LIT-tmpxroua.md); read in [NOTE-tmp2munq](../notes.d/NOTE-tmp2munq.md).

## The result

- **Energy and rule** (§2): E = −lse(β, Xᵀξ) + ½ξᵀξ + β⁻¹ log N + ½M²,
  and ξ_new = X softmax(βXᵀξ) (Eq. 3). The rule "converges globally"
  (Theorem 1) to "stationary points (local minima or saddle points)"
  (Theorem 2).
- **Capacity** (Theorem 3): for random patterns on a sphere, with
  probability 1 − p, at least √p c^((d−1)/4) can be stored, with c
  proved at d = 20 and d = 75 for p = 0.001.
- **One-step retrieval** (Theorems 4–5): the error after one update "is
  exponentially small in the separation ∆i".
- **Attention** (Eq. 10): with stored patterns as keys, the state as the
  query, a value projection and β = 1/√d_k, "The Hopfield network update
  rule is the attention mechanism used in transformer and BERT models".

All of this is proved in the appendix, which was not read; the statements
are carried from the main text.

## What it does not show

- That attention in trained transformers performs pattern retrieval in
  this sense, with keys acting as stored attractors. The identity is about
  one update; the capacity and retrieval bounds are for random or
  well-separated patterns, not trained ones.
- That its BERT finding, heads "predominantly in metastable states", is
  more than a description under the authors' thresholds.
- Anything about the feed-forward layers of trained models. Its
  HopfieldLayer is a softmax-normalized version of the memory form
  [THEORY-1030](THEORY-1030.md) reads into trained FFN units, and that is a construction,
  not evidence for the reading.
- Anything about the classical Hebbian network's capacity at large N
  ([QUESTION-201](../questions.d/QUESTION-201.md)): the 0.138d it cites is other authors' result.
