---
status: Active
title: "Under Montévil and Mossio's definition of closure, a closed set of constraints has at least two members, and if each constraint is produced at the time scale of a constraint in the set that generates it and not at the scale at which it is itself conserved, the set includes at least one slow and one fast dependence, so a system with a single constraint of its own cannot realise closure"
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed from THEORY-072 under ADR-032 (promotion audit, batch 064, the
    triage-007 control). THEORY-072's body says the 2015 closure "already
    requires several distinct constraints" and marks that as the record's
    reading; NOTE-468 says the same of the single-pattern flame. Montévil
    and Mossio state the slow-and-fast property ("as shown in the
    diagram") and do not prove it. The proof below is the record's, so the
    claim is filed Active, demonstrated, as CLAIM-391 was from
    THEORY-085. THEORY-072 keeps the demarcation thesis and stays
    Proposed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a set of constraints meeting Definition 4
  of Montévil and Mossio (2015) that has one member; or a closed set in
  which every constraint is produced at the conserved time scale of one of
  its direct generators in the set, no constraint is produced at its own
  conserved time scale, and every dependence is slow (or every one fast).
  A reading of Definitions 2-4 on which τd of a constraint is not the
  conserved time scale of a generator would not defeat the claim; it
  would show its condition unmet.
tags:
- philosophy-of-biology
- complex-systems
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
grounds:
- LIT-582
---
<!-- inactive-ok-file: THEORY-072 THEORY-085 — Proposed; the account this was filed from, which keeps the demarcation thesis, and the precedent named in the history; neither is leaned on -->

# CLAIM-tmp2pvi2: Under Montévil and Mossio's definition of closure, a closed set of constraints has at least two members, and if each constraint is produced at the time scale of a constraint in the set that generates it and not at the scale at which it is itself conserved, the set includes at least one slow and one fast dependence, so a system with a single constraint of its own cannot realise closure

## The claim

Montévil and Mossio ([LIT-582](../literature.d/LIT-582.md), read in [NOTE-468](../notes.d/NOTE-468.md)) define a
constraint by a time symmetry: C acts on a process at a time scale
τs(C) at which its relevant aspects are conserved (Definition 1). C1
depends on C2 when C2 constrains, at τs(C2), a process that produces
aspects of C1 (Definitions 2-3). A set of constraints realises overall
closure if each member "depends directly on at least one other
constraint belonging to" the set and at least one other member depends
on it (Definition 4, conditions 1-2; strict closure adds that the set
cannot be split into two closed sets). Each constraint in a closed set
also has a time scale τd(C) at which it is produced or maintained, and
the paper reads it off the diagram as the scale of the constraint that
produces it (τd(C3) = τ4 = τs(C4)). A dependence is slow when the
dependent constraint is conserved longer than the process that makes it
(τs − τd > 0) and fast in the opposite case.

Two readings are needed, and the title states them as conditions:

- **(A)** each member C of the set has a direct generator g(C) in the set
  with τd(C) = τs(g(C));
- **(B)** no member is produced at its own conserved scale:
  τs(C) ≠ τd(C).

Then:

1. A closed set has at least two members.
2. Under (A) and (B), it has a member with τs − τd > 0 and a member with
   τs − τd < 0: at least one slow and one fast dependence.
3. So a system whose only constraint of its own is a single macroscopic
   pattern cannot realise closure, under any reading.

## Proof

**1.** Let C be closed and C ∈ C. By Definition 4, condition 1, C depends
directly on some other constraint in C, which is distinct from C. So
|C| ≥ 2. No reading of (A) or (B) is used.

**2.** Assume (A) and (B). Choose for each member C a generator g(C) as in
(A); by Definition 4 it is another member, so g(C) ≠ C. C is finite, so
iterating g from any member eventually revisits one: there is a cycle
C₁, …, C_k (k ≥ 2) with g(Cᵢ) = Cᵢ₊₁ and g(C_k) = C₁. Sum the
differences around it:

Σᵢ [τs(Cᵢ) − τd(Cᵢ)] = Σᵢ τs(Cᵢ) − Σᵢ τs(g(Cᵢ)) = 0,

because g permutes the cycle's members, so the two sums have the same
terms. By (B) no term is zero. A sum of non-zero terms that equals zero
has a positive term and a negative term. ∎

**3.** Follows from 1: a set with one member is not closed.

**A check.** For 100,000 random generator maps on 2-8 constraints with
τs drawn from {1, …, 5} (Python, seed 0), the 42,328 that satisfy (B)
all contain both signs of τs − τd. The generator map was drawn with
g(i) uniform over j ≠ i and τd(i) = τs(g(i)), and draws with any
τs(i) = τd(i) were dropped.

## What this does not say

- **Not that a flame fails closure.** Part 3 is conditional on the flame
  having one constraint of its own, which is how Mossio, Saborido and
  Moreno (2009) describe it ("a unique contribution") and which no paper
  checks under the 2015 definitions. A flame whose wick and wax pool
  turned out to be constraints that it produces, at distinct time
  scales, would not be touched by this claim.
- **Not that closure is differentiation.** [THEORY-072](../theory.d/THEORY-072.md) reads the 2015
  closure as building in the 2009 paper's organisational
  differentiation. This claim shows only that closure needs at least two
  constraints and, under (A) and (B), two time scales. Whether two
  constraints at distinct scales are "different and localizable
  patterns ... each making a specific contribution" is interpretation.
- **Not that the paper's property holds without (A) and (B).** If a
  constraint can be produced at its own conserved scale, a cycle of such
  constraints has every difference zero and neither a slow nor a fast
  dependence. Montévil and Mossio's Definition 1 makes (B) natural, since
  a constraint changed at the scale it acts would not be conserved there,
  but the paper does not state it as a condition.
- **Not that closure defines the organism.** The paper denies that
  (footnote 27), and so does [THEORY-072](../theory.d/THEORY-072.md).
