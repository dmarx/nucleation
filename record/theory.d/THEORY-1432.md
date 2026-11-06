---
number: 1432
status: Active
formerly:
- THEORY-tmpxup0v
title: 'Murray and Sastry show, with Chow''s theorem as they recall it, that locally, where the bracket distributions have constant rank, a driftless system whose input vector fields, with their iterated Lie brackets, span every direction can be steered between configurations even though its constraints forbid instantaneous motion in some directions, and that for first-order, second-order and chained systems sinusoids at integrally related frequencies do the steering, one bracketing level at a time'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057, ADR-065 section 2): a reported title, its source
    read in full in NOTE-1622, whose claims table carries Chow's theorem
    as recalled and the chained-system steering of Proposition 5 and
    Algorithm 3. The proofs were read as text but not checked line by
    line; the title reports what the paper presents. The title was
    narrowed to the paper's own hedges (local, regular) and to its word
    "level"; it read "Murray and Sastry show that a driftless system
    whose input vector fields, with their iterated Lie brackets, span
    every direction can be steered between configurations even though
    its constraints forbid instantaneous motion in some directions, and
    that for first-order, second-order and chained systems sinusoids at
    integrally related frequencies do the steering, one bracket
    direction at a time". "One bracket direction" was a mis-statement
    of the source's bracketing level (ADR-047, kind 3). The condition
    deleted read "A reading confirms that Chow's theorem as the paper
    states it (Theorem 1) and Proposition 5 with Algorithm 3 (chained
    systems steered to an arbitrary configuration) carry this claim as
    titled, within the paper's assumptions of driftless, regular systems
    on an open set."
tags:
- control-theory
- mathematics
date: '2026-11-05'
source:
- LIT-2020
summary: >-
  Murray and Sastry (1993), [LIT-2020](../literature.d/LIT-2020.md), read in [NOTE-1622](../notes.d/NOTE-1622.md) from an OCR
  scan, so the equations were read from the layout. Its statements and proofs were
  read, the proofs as text and not checked line by line; Chow's theorem
  is recalled, not proved, in the paper. It is local,
  for driftless, regular systems in free space. It does not say that a path
  can be constructed for every controllable system, that simple sinusoids
  suffice beyond the classes named, or what the steering costs.
---

# THEORY-1432: Murray and Sastry show, with Chow's theorem as they recall it, that locally, where the bracket distributions have constant rank, a driftless system whose input vector fields, with their iterated Lie brackets, span every direction can be steered between configurations even though its constraints forbid instantaneous motion in some directions, and that for first-order, second-order and chained systems sinusoids at integrally related frequencies do the steering, one bracketing level at a time

## Source

Murray and Sastry (1993), [LIT-2020](../literature.d/LIT-2020.md); read in [NOTE-1622](../notes.d/NOTE-1622.md).

## What was actually shown

- **Reachability** (§II-A, p. 702): Chow's theorem, recalled: "if we can
  move in every direction using Lie bracket motions (possibly of higher
  order than one), then the system is controllable." A bracket is "the
  infinitesimal motion that results from flowing around a square defined by
  two tangent vectors".
- **Steering** (§§III–IV): Algorithms 1 and 2 for first- and second-order
  canonical systems, and Algorithm 3 for chained systems (Prop. 5), steer
  with "sinusoids at integrally related frequencies" (abstract), one
  bracket level at a time.
- **What could have failed and did** (§IV-A, p. 709): for a general
  fourth-order two-input system it is "not possible to get motion only in
  the x 7 direction using simple sinusoids", which is why the chained class
  is needed.

## What this does not say

- That a trajectory can be constructed whenever one exists: "construction
  of a trajectory for systems with drift is still an open problem"
  (p. 715).
- That reaching a bracket direction is cheap: it takes cycles of input,
  and the paper does not compute the cost.
- That the results are global, hold near singular configurations, or
  survive obstacles, which are set aside.
- That feedback can stabilize such systems smoothly; the paper says it
  cannot, to a point.
- The sentence the pasted synthesis on constraint architectures puts in
  quotation marks, about immediate directions and reachable states, which
  is A's paraphrase.
