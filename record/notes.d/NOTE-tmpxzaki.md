---
status: Skimmed
paper: 'LIT-tmpe9zd7'
title: 'Larson and Odoni — Urban Operations Research, the hypercube queueing model'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in part on 2026-11-04, as a stand-in for Larson (1974),
    LIT-tmpum63p, at the owner's request, from the online edition of the
    book posted openly by MIT at http://web.mit.edu/urban_or_book/www/book/
    (chapter 5 pages at .../chapter5/5.4.html and following), fetched as
    HTML and converted to text. Only the prose was read: the equations,
    Tables 5-4 to 5-7 and Figures 5.10 to 5.17 are images and were not
    seen, and an em-dash renders as "-" in the text. Read: §§5.4, 5.4.1–
    5.4.5 and the opening of §5.5, with §5.3.5 (Larson and Stevenson's
    two-server facility location) and the chapter 5 reference list.
    Skipped: §§5.1–5.3.4, 5.5.1–5.5.3 (the details of the approximation),
    5.6–5.8, the problems, and chapters 1–4 and 6–8. Section numbers below
    are the book's.
date: '2026-11-04'
summary: >-
  The book's own statement of the hypercube queueing model, read in prose
  only. N distinguishable units, each busy or free, over a city split into
  Poisson-source atoms, with a fixed preference list for dispatch per atom;
  from the steady state, unit workloads, dispatch fractions by unit and
  atom, dispatches across response areas and travel times. Backup
  dispatching evens out unit workloads. The basic model evaluates response
  areas a user supplies and does not optimize them; exact solution grows as
  2^N, and Larson's approximation reduces it to N equations.
---
<!-- inactive-ok-file: LIT-tmpum63p THEORY-tmph4325 — Unavailable or Proposed, and new; the unread original this book stands in for, and the account filed from this reading, cited as open -->

# NOTE-tmpxzaki: Larson and Odoni — Urban Operations Research, the hypercube queueing model

## Contribution

A planning model that keeps the identity, location and availability of
each unit of an urban emergency service, so that the city's actual
geography and dispatch policy, rather than assumptions of uniformity, enter
the evaluation of patrol beats, response areas and sites. The book states
it for N units, gives the N = 3 balance equations, and derives the
performance measures a planner reads off.

## Key insight

The state of the system is which units are busy. Because a call from an
atom goes to the first free unit on that atom's list, a unit's workload
and the travel times it delivers depend on the joint state of all the
units, not on its own response area alone: backup dispatching spreads load,
so that in the N = 3 example "the workload sharing among response units
caused the workloads of the units to be more evenly distributed than the
workloads of the primary response areas" (§5.4.4).

## Assumptions

The nine of §5.4.2, as the prose states them:

1. Geographical atoms: each reporting area is modelled as a point.
2. Independent Poisson arrivals from each atom, at known rates.
3. Mean travel times between atoms are known or estimated.
4. N servers, each able to travel to any atom.
5. Server locations: where each unit is while free is known, at least
   statistically (the location matrix).
6. Server assignment: exactly one unit is sent per call; when none is free,
   the call queues, is lost or goes to a backup system, with a queue
   discipline that does not depend on service time or location.
7. Fixed-preference dispatching.
8. Service times: a known mean, possibly different for each unit; the
   analysis assumes exponential times, but "reasonable deviations from
   this assumption have been found not to alter in any practical way the
   predictive accuracy of the model."
9. Variation in service time due solely to travel is second order.

"Successful generalizations of this basic model have allowed modifications
to assumptions 6, 7, and 9 [LARS 74a, 75b, 78, 80; JARV 74; HALP 77; CHEL
80]." The travel-time assumption "is most nearly satisfied by urban police
departments" and least by rural emergency services, especially
rural ambulances (§5.4.2).

## Key results

- **§5.4, the name.** "The model's name derives from the state space
  describing the availabilities of servers"; "each server can be in one of
  two states: busy or free ."
- **§5.4.2, dispatch.** "This procedure is called a "fixed-preference"
  procedure since the ordered list of preferences does not change with the
  state of the system."
- **§5.4.4, workload sharing.** With N = 3 and an average workload of 0.5,
  the response areas' own loads would have been 0.75, 0.35 and 0.40 had
  each unit served only its own area; backup dispatching makes the units'
  workloads more even. (The units' workloads themselves are in equation
  images and were not seen.)
- **§5.4.1, units of last resort.** "These units would not ordinarily be
  used in the routine assignment of units to service requests; however,
  they would be called upon during heavy workload conditions to avoid the
  formation of (or reduce the probability of) queues." The model computes
  their workloads and where they respond.
- **§5.4.1, specialized units.** For bilingual or cardiac units, "This
  consideration of matching the service capabilities of the unit to the
  needs of the neighborhood would probably outweigh narrow efficiency
  considerations such as minimizing travel times."
- **§5.4.1, a decision aid.** "the exact trade-off among the various
  factors must be determined by the user of the model, not by the model
  itself."
- **§5.4.5, no optimization in the basic model.** "Response areas were not
  optimized in any sense"; the optimal design of response areas for
  arbitrary N is credited to Jarvis.
- **§5.4.5, cost.** For N = 15 "the problem quickly gets out of hand, even
  for today's very large computers"; "Thus, as discussed in [LARS 74a],
  much time has been invested in using the special structure of the
  hypercube model to derive computer-efficient means for developing and
  solving its equations."
- **§5.5, the approximation.** "The approximation has been found to compute
  results to within 1 or 2 percent of the exact results."

## Concepts

- **Geographical atom** — a reporting area modelled as a point source of
  calls.
- **Primary response area** — the atoms to which a unit is sent first if
  it is free.
- **Patrol area** — where a mobile unit may be while free; it need not
  coincide with its response area. The location matrix gives the chance a
  free unit is in each atom.
- **Hyperplane** — the states with the same number of busy units.
- **Inter-response-area dispatch** — a unit sent outside its primary
  response area.
- **Unit of last resort** — a unit outside routine assignment, dispatched
  only under heavy load.

## Connections

The book is the authors' own restatement of the model introduced in Larson
(1974), [LIT-tmpum63p](../literature.d/LIT-tmpum63p.md), which it cites as [LARS 74a]. Of that paper it
restates the model: the binary busy/free state space on the vertices of an
N-cube and its name, geographical atoms, response and patrol areas and the
location matrix, fixed-preference dispatch, the assumptions, the balance
equations (for N = 3) and the performance measures. It cites the paper for
the generalizations of assumptions 6, 7 and 9 and for the
computer-efficient solution. It does not restate that paper's solution
algorithm (which Hua, Luo, Swersey and Wen, [LIT-tmpws93a](../literature.d/LIT-tmpws93a.md), credit to it as
the alternating hyperplane method and TOUR), any facility-location or
redistricting search the paper may carry, its numerical examples or its
review of the literature. The N-equation approximation is Larson (1975),
not the 1974 paper.

## Bearing on the record

- **The pasted bibliography on emergency readiness** cites Larson (1974),
  not this book, as showing that "a unit's value depends on its
  availability and on the locations and states of other units, not just
  its own completed-call count". So far as this book shows the model, that
  is A's framing, not Larson's: nothing here values a unit, and nothing is
  contrasted with a count of completed calls. What the book shows is that a
  unit's workload and the travel times it delivers depend on the joint
  busy/free state. "distinguishable response units" is right. A misses that the
  basic model evaluates configurations rather than optimizing them, and
  the units of last resort, the construction closest to A's theme of
  rarely exercised capability; the book treats them only as a dispatch
  device and makes no claim about their worth.
- **[TERM-055](../terms.d/TERM-055.md) (operational availability): qualifies.** A unit's
  availability here is the chance it is free when a call arrives,
  unavailable only through congestion. That is at most a special case of
  [TERM-055](../terms.d/TERM-055.md), which adds the cue, the procedure and the deadline.
- **[CLAIM-296](../claims.d/CLAIM-296.md) and [CLAIM-312](../claims.d/CLAIM-312.md): qualify.** A busy unit is present but not
  deployable; a unit of last resort is deployable only in saturation.
- [CLAIM-079](../claims.d/CLAIM-079.md), [CLAIM-347](../claims.d/CLAIM-347.md), [CLAIM-517](../claims.d/CLAIM-517.md), [QUESTION-132](../questions.d/QUESTION-132.md) and the LITs A listed
  beside this work: unrelated.
- Filed from this reading: [THEORY-tmph4325](../theory.d/THEORY-tmph4325.md).

## Limitations

- §5.4.1: "complicated priority-oriented procedures cannot be treated by
  the model-and this is perhaps the model's largest single limitation at
  its current state of development." Selective stacking, preemption and
  priority queues are excluded, and simulation is suggested for them.
- One unit per call; the travel-time assumption limits it outside dense
  urban police work; exact computation grows as 2^N.
- This reading's own: no equation, table or figure was seen, so no
  formula or number in an image has been checked.

## Open questions

Whether the 1974 paper optimizes locations and districts or, like the
book's basic model, evaluates those a user supplies. Reading the paper
would settle it.
