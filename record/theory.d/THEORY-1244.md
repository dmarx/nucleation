---
number: 1244
status: Proposed
formerly:
- THEORY-tmptf9gh
promote_when: >-
  A proof, in a stated cost model (cell-probe, external-memory or the like)
  and for a stated set of operations, of a quantified version: a lower bound
  on one of read, update and memory overhead that exceeds 1.0 and grows as
  bounds on the other two are tightened. It is refuted, for that model and
  operation set, by a construction that keeps all three overheads within
  constants at once. More placements of structures on the triangle,
  asymptotic tables of known methods, or benchmarks cannot settle it, since
  they show where particular designs sit, not what no design can reach.
title: 'No access method is optimal on read, update and memory overhead at once: bounding any two of the three forces the third above a hard lower bound that cannot be further reduced'
version: 1
tags:
- databases
date: '2026-10-30'
source:
- LIT-1085
extends:
- THEORY-344
summary: >-
  The RUM conjecture as its authors intend it, filed beside [THEORY-344](THEORY-344.md) by
  the status review of 2026-10-30 ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md) kind 1). [THEORY-344](THEORY-344.md),
  Active, reports the conjecture and what its formal wording and toy
  extremes do and do not show; whether the trade holds, quantified, is this
  entry's question.
---

# THEORY-1244: No access method is optimal on read, update and memory overhead at once: bounding any two of the three forces the third above a hard lower bound that cannot be further reduced

## Source

Athanassoulis et al. (2016), [LIT-1085](../literature.d/LIT-1085.md), read in full in [NOTE-888](../notes.d/NOTE-888.md). The paper
asserts the trade: designing access methods "that set an upper bound for two of
the RUM overheads, leads to a hard lower bound for the third overhead which
cannot be further reduced" (§1), and "optimizing in any two areas negatively
impacts the third" (abstract).

## Where the evidence stands

Nothing is proved. What the paper states, and what its formal wording and its
three extreme designs do and do not show, is [THEORY-344](THEORY-344.md), Active, which this
entry extends: that entry is the reading, this one the thesis. The
`promote_when` above is [THEORY-344](THEORY-344.md)'s condition before the status review of
2026-10-30 promoted it, carried here word for word: a proof of a quantified
version in a stated cost model.

## What this does not say

- How large the forced bound is, or how it grows as the other two are
  tightened. That is what a proof would have to supply.
- That the trade is symmetric. At the paper's extremes the memory-minimal design
  is also update-minimal ([THEORY-344](THEORY-344.md)).
