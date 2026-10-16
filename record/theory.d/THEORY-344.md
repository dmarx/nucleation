---
number: 344
status: Proposed
formerly:
- THEORY-tmpipw5a
promote_when: >-
  A proof, in a stated cost model (cell-probe, external-memory or the like) and
  for a stated set of operations, of a quantified version: a lower bound on one
  of read, update and memory overhead that exceeds 1.0 and grows as bounds on the
  other two are tightened. It is refuted, for that model and operation set, by a
  construction that keeps all three overheads within constants at once. More
  placements of structures on the triangle, asymptotic tables of known methods,
  or benchmarks cannot settle it, since they show where particular designs sit,
  not what no design can reach.
title: "An access method's read, update and memory overheads, each a ratio to the base data alone with a floor of 1.0, are conjectured to trade so that bounding any two forces a lower bound on the third; the conjecture is unproved, its formal wording says no more than the floor already does, and the paper's extreme designs show conflicts between pairs, read against memory and update against read, not a symmetric three-way trade"
version: 1
tags:
- databases
date: '2026-10-15'
source:
- LIT-1085
answers:
- QUESTION-114
summary: >-
  Athanassoulis et al. (2016), [LIT-1085](../literature.d/LIT-1085.md), read in [NOTE-888](../notes.d/NOTE-888.md). A six-page
  vision paper defines read, update and memory amplification and conjectures
  that an access method optimal on one cannot be optimal on both others. Its
  evidence is three one-paragraph propositions about extreme designs on an
  integer array, a qualitative triangle and a table of asymptotic I/O costs. The
  formal statement asserts only some lower bound on the third overhead, which
  every design has. The extremes are not symmetric: the memory-minimal design is
  also update-minimal. Build cost, workload and time are outside the triangle.
---

# THEORY-344: An access method's read, update and memory overheads, each a ratio to the base data alone with a floor of 1.0, are conjectured to trade so that bounding any two forces a lower bound on the third; the conjecture is unproved, its formal wording says no more than the floor already does, and the paper's extreme designs show conflicts between pairs, read against memory and update against read, not a symmetric three-way trade

## Source

Athanassoulis, Kester, Maas, Stoica, Idreos, Ailamaki and Callaghan (2016),
[LIT-1085](../literature.d/LIT-1085.md), EDBT, read in full in [NOTE-888](../notes.d/NOTE-888.md): the definitions and
Propositions 1–3 (§2), the conjecture (§3), Figure 1 and Table 1.

## What was actually shown

**The overheads.** Read overhead is "the ratio between the total amount of data
read including auxiliary and base data, divided by the amount of retrieved
data"; update overhead the physical over the logical update size; memory
overhead the space for auxiliary and base data over base data alone. "The
theoretical minimum for each overhead is to have the ratio equal to 1.0".

**The hypothesis.** "An access method that is optimal with respect to one of the
read, update, and memory overheads, cannot achieve the optimal value for both
remaining overheads." Each proposition is a paragraph, on an array of N
integers, one per block:

- Minimum read (each value stored at the block its value names): "Prop. 1
  min(RO) = 1.0 ⇒ UO = 2.0 and MO → ∞".
- Minimum update (append to a log): "Prop. 2 min(UO) = 1.0 ⇒ RO → ∞ and MO → ∞".
- Minimum memory (dense array, scans): "Prop. 3 min(MO) = 1.0 ⇒ RO = N and
  UO = 1.0".

**The conjecture as stated.** "An access method that can set an upper bound for
two out of the read, update, and memory overheads, also sets a lower bound for
the third overhead." It does not say how large that bound is or how it depends
on the other two.

**A further point in the paper's own table.** A sorted column with no auxiliary
structure has memory overhead 1.0, logarithmic reads and linear updates, so
organizing the base data trades read against update without spending space;
auxiliary structure trades read against memory.

## What this does not say

- **That the trade is proved.** Nothing is proved; the authors write that
  "proving the RUM Conjecture will expand on this line of research."
- **That the formal conjecture has content.** Every overhead is at least 1.0, so
  "some lower bound on the third" holds of every design. The intended content is
  in the hypothesis and the gloss ("pay the price by having the third overhead
  greater than a hard lower bound"), and is not quantified.
- **That the three overheads conflict symmetrically.** Proposition 3's design is
  optimal on memory and update at once, and Proposition 1's keeps update at 2.0.
  At the extremes the conflicts are read against memory and update against read.
- **That the triangle prices a workload or a build.** There is no query mix or
  frequency in the definitions, building a structure is a separate column of
  Table 1 outside the conjecture, and costs are amounts of data per operation,
  with no time or deadline.
- **That computation is free.** The paper notes designs that lower two overheads
  at once by "computation and knowledge about the data" (clustered block indexes,
  compression); computation is a resource the triangle does not count.
- **That every item read costs the same in every domain.** Read overhead counts
  items examined, uniformly. A target that stands out among its neighbours has
  no term here.

## Connections

- For [QUESTION-114](../questions.d/QUESTION-114.md) it splits "organizing ahead" into two trades, auxiliary
  structure paid in space and sorting paid in upkeep, and is a vocabulary for the
  question's terms, not the joint cost model it lacks.
- Adaptive methods such as cracking ([THEORY-333](THEORY-333.md)) sit in the middle of the
  triangle in the paper's figure; their amortization is cited, not modelled.
- Yao 1981 ([LIT-1097](../literature.d/LIT-1097.md), [THEORY-340](THEORY-340.md)) is the record's cell-probe reading; it bounds lookup
  cost alone, which is one corner of this trade.
- [CLAIM-307](../claims.d/CLAIM-307.md) and [CLAIM-310](../claims.d/CLAIM-310.md): counting search as items examined per item
  wanted is read overhead in these terms, and pop-out is outside them.
