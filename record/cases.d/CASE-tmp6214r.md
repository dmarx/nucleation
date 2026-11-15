---
status: Proposed
title: 'Reconstruction channels in a phase-coded associative memory: readdressing, readout suppression and deletion of a stored association all read zero at its original query, and further queries tell them apart; suppressing the readout at one of 64 canonical queries drops the measurement rank to 63, and one half-step query restores it; but two internal pathways that cancel at the output are indistinguishable from none under every query until one is silenced'
version: 1
standing: stipulated
kind: construction
tags:
- information-theory
- representation-learning
- mathematics
date: '2026-11-15'
line:
- learned-structure
- formal-apparatus
illustrates:
- CLAIM-182
- CLAIM-407
bears_on:
- QUESTION-274
summary: >-
  A's construction from A21–A22 of the continuation of the exchange
  "Explain String Theory" (2026-11-15), after the owner's example of "a
  hologram of a scene which only reveals a particular (unocluded?) object
  when viewed from a particular angle". A ran it and reported a study note,
  a program and a figure, none of which reached the record. It is
  rebuilt here from the text (scratch/formal/reconstruction_channel_checks.py),
  and every value but one is reproduced. A's suppressed-readout amplitude
  of 0.551 at the half step depends on how the suppression was
  implemented, which the text does not give; under the reconstruction
  used here (a zero readout at the canonical query) it is 0.637, so 0.551
  is A's and unverified. Proposed because the construction is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-182 — Proposed; the claim the construction illustrates -->

# CASE-tmp6214r: Reconstruction channels in a phase-coded associative memory

## The construction

A key is a phase code, k(φ) = d^(−1/2)(1, e^{iφ}, …, e^{(d−1)iφ}), with
d = 64. A memory superposes associations, m = Σ_j a_j k(φ_j), and a query
reads y(φ) = k(φ)†m. One association's response is a_j·D_d(φ_j − φ), where
D_d is the normalized Dirichlet kernel. It equals a_j at the matching
query and is exactly zero at every offset that is a multiple of 2π/d. The
target-specific response is the memory's response minus that of a matched
memory without the target. That comparison is available in the toy, and a
trained model would need designed contrasts in its place.

| intervention | original query | half step | new address |
|---|---|---|---|
| intact | 1.000 | 0.637 | 0.000 |
| attenuated (×¼) | 0.250 | 0.159 | 0.000 |
| readdressed (one step) | 0.000 | 0.637 | 1.000 |
| readout suppressed | 0.000 | (A: 0.551) | 0.000 |
| deleted | 0.000 | 0.000 | 0.000 |

(Rechecked, except the bracketed value; see the summary.)

- **One failed query identifies nothing.** Readdressing, suppression and
  deletion agree at the original query. More queries separate them.
- **Query design restores observability.** The 64 canonical queries have
  full rank. With the readout at the target's address suppressed, the rank
  is 63. One half-step query restores 64. Choosing queries that maximize
  the least eigenvalue of the observability Gramian on a target subspace
  is A's proposed design rule.
- **Some differences no query reveals.** Two internal pathways h₁ = u and
  h₂ = −u, read only through their sum, give zero for every query, exactly
  as a system with neither does. Silencing h₂ reveals u. The two count as
  separately retained pathways only if they exist as separately
  intervenable variables.
- **Phase matters.** An observer who sees only intensity |A_q z|² cannot
  recover a global phase. Activations, logits, probabilities and sampled
  answers are different observation channels.

## What it shows

Retrieval is relative to a query family. A distinction can be retained,
unaddressed under one cue and addressed under another (CLAIM-182). And
agreement under every ordinary observation does not fix the mechanism
behind it, which only an intervention reveals (CLAIM-407).

## What it cannot show

That trained transformers store facts this way. Plate's holographic
reduced representations and the attention–memory equivalences read for
this filing make the construction a coherent model of keyed retrieval
from superposed storage, not evidence that language models use it.
