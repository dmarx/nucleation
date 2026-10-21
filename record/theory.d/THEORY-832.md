---
number: 832
status: Proposed
formerly:
- THEORY-tmpylmuq
promote_when: >-
  A reading of Fagin's own proof (LIT-1108, the PODS 1996 paper or its
  JCSS 1999 journal version), or a checked step-by-step re-derivation,
  that states the lower bound with its probability model and its cost
  model: what independence of the orderings means, which accesses are
  counted (sorted and random), what "with high probability" quantifies
  over, and the exact strictness condition on the combining function. It
  is refuted if that proof states a different bound or conditions, or if
  a correct algorithm is exhibited that beats N^((m−1)/m) k^(1/m) under
  them. Further secondary statements of the bound, including more of
  Fagin, Lotem and Naor, cannot settle it: the record already holds one.
title: "For strict combining functions and m attribute-sorted lists of N objects whose orderings are probabilistically independent, no correct top-k algorithm does essentially better than Fagin's Algorithm in the worst case with high probability: every one needs on the order of N^((m−1)/m) k^(1/m) accesses"
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed by the promotion audit (batch 077, ADR-047 v4) when THEORY-379
    was narrowed to Fagin's Algorithm's upper bound and correctness, which
    the review re-derived. This entry carries the lower bound THEORY-379
    dropped. Fagin asserts it; Fagin, Lotem and Naor report it; the record
    has not read the proof and the review did not re-derive it. It
    inherits THEORY-379's promote_when, widened to say which accesses
    are counted.
tags:
- databases
- information-retrieval
date: '2026-10-21'
source:
- LIT-1108
- LIT-1115
extends:
- THEORY-379
summary: >-
  Fagin (1996/1999), [LIT-1108](../literature.d/LIT-1108.md), as reported by Fagin, Lotem and Naor
  (2001), [LIT-1115](../literature.d/LIT-1115.md), Sections 1 and 3, read in [NOTE-924](../notes.d/NOTE-924.md): "his algorithm is
  optimal with high probability in the worst case if the aggregation
  function is strict ... and if the orderings in the sorted lists are
  probabilistically independent." Strict means the combined grade is 1
  exactly when every grade is 1. Not read in the original; not
  re-derived.
---
<!-- inactive-ok-file: LIT-1108 — Unavailable; the source of the bound, cited as reported by LIT-1115 -->

# THEORY-832: For strict combining functions and m attribute-sorted lists of N objects whose orderings are probabilistically independent, no correct top-k algorithm does essentially better than Fagin's Algorithm in the worst case with high probability: every one needs on the order of N^((m−1)/m) k^(1/m) accesses

## Source

Fagin (1996; journal version 1999), [LIT-1108](../literature.d/LIT-1108.md), not read: no lawful copy
could be fetched. The statement is as Fagin, Lotem and Naor (2001),
[LIT-1115](../literature.d/LIT-1115.md), report it, read in [NOTE-924](../notes.d/NOTE-924.md).

## What is claimed

A matching lower bound for [THEORY-379](THEORY-379.md)'s upper bound. If the combining
function is strict (score 1 exactly when every grade is 1), then under
the same probability model every correct algorithm, in the worst case
and with high probability, uses on the order of N^((m−1)/m) k^(1/m)
accesses, so Fagin's Algorithm is optimal up to a constant. For √(Nk)
with two lists, this says no algorithm finds the top k of two
independent lists with essentially fewer accesses.

## What would confirm or reject it

A reading of Fagin's proof, or a re-derivation, stating which accesses
are counted and what "with high probability" quantifies over. A lower
bound over all correct algorithms with random access allowed needs an
adversary argument; the report gives none. It would be rejected by a
correct algorithm beating the bound under the stated model.

## What this does not say

- **Anything for non-strict functions.** For max, a simple algorithm
  uses at most mk sorted accesses ([LIT-1115](../literature.d/LIT-1115.md)), so the bound fails there.
- **Anything per instance.** It is a worst-case, high-probability bound.
  Fagin, Lotem and Naor's threshold algorithm is instance optimal
  ([THEORY-363](THEORY-363.md)), a different kind of guarantee.
- **That independence alone is the model.** [THEORY-379](THEORY-379.md)'s re-derivation of
  the upper bound needed at least m − 1 of the orderings to be uniformly
  random as well as independent: two deterministic lists in opposite
  orders are independent, and Fagin's Algorithm then needs depth about
  N/2. What Fagin's own model requires is the open part of this entry.
