---
number: 15
status: Active
formerly:
- THEORY-tmpszumj
title: 'Kochen–Specker noncontextuality is measurement noncontextuality plus outcome determinism for sharp measurements, and preparation noncontextuality implies that determinism, so every Kochen–Specker proof refutes universal generalized noncontextuality while measurement noncontextuality alone is consistent with quantum theory'
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    LIT-266 was read in full (NOTE-748), and the §VIII.A proof was
    checked step by step. It holds, and it needs quantum theory's full
    preparation set: Ω is defined through every density operator (Eq. 85),
    and Eq. 86 holds only because every ρ appears in some decomposition of
    I/d. That is what the promotion condition asked, so the status moved
    from Proposed to Active and the condition was removed. The reading's
    precisions were added: the proof covers rank-1 PVMs directly and the
    rest by coarse-graining, and the old Kochen–Specker proofs refute
    preparation plus measurement noncontextuality, not preparation
    noncontextuality alone. The join to the sheaf form is still the
    record's own.
- version: 3
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-263 (NOTE-tmpmru91). The review never
    states the decomposition of Kochen–Specker noncontextuality or the
    implication; it is now cited only for §IV.B.3, §IV.E.1 and §IV.E.4.
    The Deferred comment on LIT-263 removed.
tags:
- contextuality
- quantum-foundations
date: '2026-09-27'
source:
- LIT-266
- LIT-263
- LIT-016
- LIT-007
summary: >-
  Spekkens (2005), [LIT-266](../literature.d/LIT-266.md), §III, §VIII.A (Eqs. 77–88), §VIII.B, §IX —
  the bridge between the record's two contextuality threads, which no held
  work states. Read in full in NOTE-748, which confirmed the §VIII.A proof and its
  need for the full preparation set. Joining it to the sheaf form
  ([LIT-016](../literature.d/LIT-016.md)) is the record's inference.
extends:
- THEORY-012
- THEORY-016
answers:
- QUESTION-067
---

# THEORY-015: Kochen–Specker noncontextuality is measurement noncontextuality plus outcome determinism for sharp measurements, and preparation noncontextuality implies that determinism, so every Kochen–Specker proof refutes universal generalized noncontextuality while measurement noncontextuality alone is consistent with quantum theory

## Source

Spekkens (2005), [LIT-266](../literature.d/LIT-266.md), §III, §VIII.A–B, §IX ([NOTE-748](../notes.d/NOTE-748.md)). Supporting, thinly: Budroni et al. ([LIT-263](../literature.d/LIT-263.md), §IV.B.3 on unsharp response functions under measurement noncontextuality, §IV.E.1 for the definitions, and §IV.E.4 on the preparation contextuality of Bell's and Kochen & Specker's qubit models; the review does not state the decomposition or the implication, [NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md)); Abramsky & Brandenburger, [LIT-016](../literature.d/LIT-016.md), Thm 8.1 and Prop 3.1; Spekkens (2014), [LIT-007](../literature.d/LIT-007.md), §IV.B.

## What was actually shown

Spekkens shows that the traditional (Kochen–Specker) notion is measurement noncontextuality — independence of a sharp measurement's representation from how its projectors are grouped — together with outcome determinism, sharp measurements being represented by indicator functions (§III). He then proves that preparation noncontextuality forces outcome determinism for every projective measurement: the ontic supports of an orthonormal basis's preparations must cover the ontic space, because they all decompose the maximally mixed state, whose representation is unique (§VIII.A, Eqs. 77–88; the proof is given for rank-1 projective measurements and extended to the rest by coarse-graining). So universal noncontextuality implies Kochen–Specker noncontextuality, and every Kochen–Specker proof is a proof against the universal notion. Measurement noncontextuality on its own is consistent with quantum theory: the Beltrametti–Bugajski model is measurement-noncontextual for all POVMs, and pays with outcome indeterminism and preparation contextuality (§VIII.B). "One cannot confine all the contextuality into the measurements" (§IX).

The held record already uses the link in one direction: Spekkens 2014 rules out a nonnegative quasiprobability representation of the qubit stabilizer theory because that theory contains the Mermin-square and GHZ Kochen–Specker proofs ([LIT-007](../literature.d/LIT-007.md) §IV.B, by citation).

The record's own join: by [LIT-016](../literature.d/LIT-016.md) Thm 8.1 and Prop 3.1, a sheaf-contextual model built from projective measurements has no outcome-deterministic, measurement-noncontextual model; by the above, the operational theory it comes from then has no universally noncontextual model — provided it contains the preparations §VIII.A uses.

## What this does not say

- That the two notions coincide (they do not: see the qubit claim in this group).
- That Kochen–Specker proofs refute preparation noncontextuality alone. They refute preparation plus measurement noncontextuality, which universal noncontextuality includes; refuting preparation noncontextuality alone takes a proof such as the one in §IV ([THEORY-011](THEORY-011.md)).
- That the implication holds in restricted fragments. §VIII.A uses quantum theory's full preparation set (Eqs. 85–86); inside a stabilizer or interferometric fragment ([LIT-019](../literature.d/LIT-019.md)) it must be re-checked.
- Anything about noisy or unsharp Kochen–Specker tests, which is Kunjwal & Spekkens's programme (not held, not read).
- That the sheaf-form statement appears in any source; it is the record's join.
