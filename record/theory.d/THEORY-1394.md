---
number: 1394
status: Active
formerly:
- THEORY-tmph4325
title: "Larson and Odoni's hypercube model represents an urban emergency service's N distinguishable units, each busy or free, as a Markov chain on the vertices of an N-cube under fixed-preference dispatch from point sources of Poisson calls, and from its steady state computes each unit's workload, the inter-district dispatch fractions and the mean travel times"
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the thirtieth status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065. NOTE-1620 v2
    reads §5.4 with its equations, tables and figures from the MIT online
    edition. Its condition held: the balance equations (5.21)-(5.29) and
    the formulas (5.30)-(5.44) were checked against the images and
    re-derived by scratch/formal/larson_odoni_hypercube_check.py, which
    reproduces the example's state probabilities, workloads and dispatch
    fractions; the state is the busy/free status of N distinguishable
    units, upward transitions follow each atom's fixed preference list,
    and the measures are computed from the steady state. The deleted
    promote_when read: 'The balance equations and performance-measure
    formulas of §5.4 checked against the equation images or the print
    edition, confirming that the model's state is the busy or free status
    of each of N distinguishable units, that transitions follow
    fixed-preference dispatch from atoms generating Poisson calls, and
    that each unit's workload, the inter-district dispatch fractions and
    the mean travel times are computed from the steady-state
    probabilities of that chain.' The online image for (5.28) duplicates
    (5.26) and was rebuilt from Figure 5.17. The title is unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-093. corroborates CLAIM-296 and CLAIM-312 added.
    CLAIM-296: "In the hypercube model (Larson and Odoni, NOTE-1620 ...),
    a unit busy on another call is present but not deployable". CLAIM-312:
    "That is a special case of the claim with no search or retrieval
    component". No other change.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2053
summary: >-
  Larson and Odoni (1981), [LIT-2053](../literature.d/LIT-2053.md), chapter 5, §5.4, read with its
  equations in [NOTE-1620](../notes.d/NOTE-1620.md); the textbook restatement of the model introduced
  in Larson (1974), [LIT-2105](../literature.d/LIT-2105.md), which could not be read. Active: the book
  states the model in general-N notation and works N = 3 in full, and a
  re-derivation reproduces its numbers. A unit's own mean travel time is
  an approximation, the others exact. It says nothing about valuing a
  unit, and the basic model evaluates response areas a user supplies
  rather than optimizing them.
corroborates:
- CLAIM-296
- CLAIM-312
---
<!-- inactive-ok-file: LIT-2105 — Unavailable; the unread original this account restates, cited as open -->

# THEORY-1394: Larson and Odoni's hypercube model represents an urban emergency service's N distinguishable units, each busy or free, as a Markov chain on the vertices of an N-cube under fixed-preference dispatch from point sources of Poisson calls, and from its steady state computes each unit's workload, the inter-district dispatch fractions and the mean travel times

## Source

Larson and Odoni (1981), [LIT-2053](../literature.d/LIT-2053.md); read in [NOTE-1620](../notes.d/NOTE-1620.md), §5.4 with its
equations and the opening of §5.5. The model is Larson (1974), [LIT-2105](../literature.d/LIT-2105.md), unread.

## What was actually shown

- **The state space.** "The model's name derives from the state space
  describing the availabilities of servers" (§5.4); each server is busy or
  free, so the state is a vertex of an N-cube, with a tail of queue states
  when a queue is allowed.
- **Dispatch.** A fixed preference list per atom: "the ordered list of
  preferences does not change with the state of the system" (§5.4.2).
- **The assumptions.** Nine, including atoms as points, independent Poisson
  arrivals per atom, one unit per call and exponential service (§5.4.2).
- **The measures.** Workloads (5.30), dispatch fractions by unit and atom
  (5.31)–(5.35), inter-response-area fractions (5.36)–(5.38) and travel
  times (5.39)–(5.44), all from the steady-state probabilities; for the
  N = 3 example, a re-derivation from the book's inputs reproduces the
  probabilities, workloads and dispatch fractions to the printed
  rounding (scratch/formal/larson_odoni_hypercube_check.py). A unit's own
  mean travel time has "no known (exact) expression" and (5.44)
  approximates it.
- **The book's slips and the online edition's defect.** Re-derived from
  the book's own inputs (Fig. 5.11, Tables 5-4 and 5-6, the location
  matrix), two printed travel times are off by more than rounding: the
  mean queued-request travel time is 196/45 = 4.356 minutes exactly,
  printed 4.34, and the mean travel time to atom 7 is 2.68, printed 2.64.
  Neither touches the method. On the MIT site the image shown as (5.28),
  balance of flow about state 011, is a second scan of (5.26); it was
  rebuilt from the rates of Figure 5.17 as
  P011(3/2 + 2) = 1·P111 + 0.85·P001 + 1.10·P010, which closes the system
  and returns the book's probabilities.
- **Workload sharing.** Backup dispatching makes the units' workloads "more
  evenly distributed than the workloads of the primary response areas"
  (§5.4.4).

## What this does not say

- That a unit has a value, or that its worth depends on the others' states:
  that framing is the pasted bibliography's, not the book's.
- That the model optimizes locations or districts: in the basic model
  "Response areas were not optimized in any sense" (§5.4.5), and the
  trade-offs are left to "the user of the model, not by the model itself"
  (§5.4.1).
- Anything about priority dispatching, multiple units per call, or systems
  where travel time dominates service time, which the basic model excludes.
- What the 1974 paper itself contains beyond the model the book restates.
