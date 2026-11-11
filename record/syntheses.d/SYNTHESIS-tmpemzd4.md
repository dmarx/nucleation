---
status: Proposed
title: 'Present stability does not show persistence: a system can hold a stable regime while it has no trajectory that keeps meeting its constraints, the statistics of survivors can be stationary and quickly reached while absorption is certain, a coupling can stay as strong as ever while the process maintaining it reaches its fold, a slow mode means different things according to which mode slows, and coupling separates time scales only where it dissipates differences'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the stability part of the formal-apparatus line left out without a
  reason given; or a link this account states that no component states.
  Its standing is its components': a component retired or demoted takes
  its clause with it, and nothing here holds the clause up.
tags:
- complex-systems
- mathematics
- probabilistic-modeling
- individuation
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-tmpsh6jv
- CLAIM-079
- CLAIM-612
- CASE-231
- ARG-056
- CLAIM-521
- CLAIM-626
- CLAIM-481
- CASE-227
- ARG-068
---
<!-- inactive-ok-file: ADR-075 THEORY-142 ARG-056 CASE-227 CASE-231 CLAIM-157 CLAIM-478 CLAIM-612 CLAIM-625 CLAIM-626 CASE-223 SYNTHESIS-035 SYNTHESIS-039 SYNTHESIS-048 — Proposed; components and citations, with their standing, and the audit this review applies -->
<!-- inactive-ok-file: ARG-068 CLAIM-473 — Rejected; a component and the conjecture a component refutes -->
<!-- inactive-ok-file: SYNTHESIS-003 SYNTHESIS-006 — Superseded; cited as earlier accounts, not integrated -->
<!-- inactive-ok-file: CLAIM-tmpsh6jv SYNTHESIS-tmpc35sn SYNTHESIS-tmpe15k3 SYNTHESIS-tmphb9rl SYNTHESIS-tmpvz4mj — Proposed; cited with its standing -->

# SYNTHESIS-tmpemzd4: Present stability does not show persistence: a system can hold a stable regime while it has no trajectory that keeps meeting its constraints, the statistics of survivors can be stationary and quickly reached while absorption is certain, a coupling can stay as strong as ever while the process maintaining it reaches its fold, a slow mode means different things according to which mode slows, and coupling separates time scales only where it dissipates differences

*A part account of the formal-apparatus line: the part a mechanical
community map of the line's stored relations and mentions calls stability,
nine entries. The line's account is built over it and the accounts of its
sibling parts. Every member carries another line first: CLAIM-079 is first
in will-organization, and the other eight are first in distributed-agency.
They are integrated again here because their `line` includes
formal-apparatus. SYNTHESIS-048, the account of the individuation part of
distributed-agency, integrates the eight; SYNTHESIS-039, the account of a
part of will-organization, and SYNTHESIS-035, that line's account over it,
integrate CLAIM-079. SYNTHESIS-003 and SYNTHESIS-006, which integrated
CLAIM-079, CLAIM-612 and CLAIM-481, are Superseded.*

## The account

The part answers one question: what a system's present stability, the
strength of its coupling, or the steadiness of what is observed of it
shows about whether it persists. It answers by separations, each held by
one claim and shown by a construction.

- **Stability and viability.** CLAIM-079 (the paper's, applied from
  viability theory, THEORY-134, and the stability/resilience distinction,
  THEORY-132; thesis, demonstrated, Active): "A system can currently satisfy
  the relevant constraints without possessing a trajectory that continues
  to satisfy them over the relevant horizon." It does not say that more
  options are better: "A narrow path can be viable. A large option set can
  be nonviable." Its note of 2026-11-04 records two qualifications from
  the readings: under small noise every stable state is only metastable,
  "so occupying a stable regime is itself temporary", and Kuehn's
  mechanism, a system "stable at every frozen parameter value, yet drifts
  to a point where normal hyperbolicity is lost and jumps far away". Its
  note of 2026-11-05 reads four constraint-architecture works as partial
  support or analogy, with no change of status.
- **Survivors' statistics and absorption.** CLAIM-612 (A's wording on A22
  §5 of "Individuation, Possibility, and Disposition", the general
  statement the reader's framing; thesis, demonstrated, Proposed): "The
  conditional organization can be extraordinarily stable while its
  unconditional survival is not." In a finite chain whose viable states
  all lead to an absorbing failure, the survivors' distribution settles on
  the mixing time, they die out on a time longer by the ratio of the gap to
  the hazard, "so a surviving organization's stable statistics are no
  evidence that it persists". It does not say they are evidence against
  persistence: "They are no evidence either way; the hazard has to be
  estimated separately." CASE-231 (A's construction, stipulated, Proposed)
  is the chain: A and B exchange at rate 1, B fails into an absorbing D at
  rate 0.02; the survivors reach (0.5025, 0.4975) within a few time units
  while survival decays as e^(−0.00995t), a mean lifetime of 100.5, and the
  ratio of the two times is about 4k/ε. ARG-056 (the assistant's wording,
  existence, Proposed) concludes CLAIM-612 from it and limits the last
  clause: the values of the quasi-stationary distribution carry a trace of
  the hazard of order ε/(8k), so "The last clause holds of stationarity and
  speed, and only nearly of the values." CLAIM-612's own section "How far
  'no evidence' holds" records the same.
- **Coupling strength and maintenance.** CLAIM-521 (A12 §6 of "Analyze
  nucleation concepts"; thesis, demonstrated, Active): in CASE-189's
  seed–capture construction the maintenance's slowest eigenvalue goes to
  zero at its saddle-node while the three-unit coupling's gap stays near
  0.9894. "The coupled units are as tightly integrated at the edge of
  collapse as well inside the regime." It says the result is built in, not
  surprising: with no feedback from the coupled units to the core, "the gap
  depends on the equilibrium's value and not on its stability". It says
  that "Critical slowing appears in the maintenance, not in the coupling",
  and that in a finite system the regime is metastable and the coupling is
  lost at escape: "The dissociation holds for as long as the regime does."
  Its note of 2026-11-01 sets the SCN beside it, where coupling does feed
  maintenance and the dissociation fails: "This is a contrast, not a
  counterexample."
- **What slowing means.** CLAIM-626 (A's, A20 §4 with A14 §2's
  computation; thesis, demonstrated, Proposed) sorts critical slowing by
  the mode that slows: a collective mode (reduction improves; CLAIM-478's
  second half), the mode restoring a collective relation (two detuned
  phase oscillators near the edge of locking, restoring rate
  √(4K² − Δω²), where the one-unit reduction "is lost before the locked
  state is"), and the maintenance of the coupling (CLAIM-521's arm, the
  reduction staying good while the organization nears its fold). "So an
  observed slow mode does not say, by itself, whether organization is
  forming, a reduction is failing, or a maintained capacity is failing."
  It does not say the three kinds are exhaustive.
- **Coupling and time scales.** CLAIM-481 (A20, A21 and A23 of the
  exchange on the owner's U20; counter, demonstrated, Active) objects to
  CLAIM-473: two identical undamped oscillators coupled with stiffness k
  split into normal modes at ω₀ and √(ω₀² + 2k) and neither decays, "So
  coupling does not necessarily induce scale separation, and CLAIM-473 is
  false as stated." Dissipative coupling relaxes the collective and
  relative modes at a and a + 2k, and for a Laplacian flow "A spectral gap
  is a separation of time scales"; for a chain of n units the slowest
  nonzero eigenvalue is about π²/n², so "Size alone makes a slow collective
  mode." It does not show "That a gap makes an individual."
- **A decaying capacity under a coordination mode.** CASE-227 (A's A29
  construction, stipulated, Proposed; a variant of CASE-189): in the
  Haken–Kelso–Bunz relative-phase equation with its coupling made a
  maintained capacity, c = 0.6 holds anti-phase stable while lying below
  the unstable maintenance level 0.642, so the capacity decays through ½
  and the mode is lost. It can show "That a coordination mode can be
  stable now while the capacity keeping it stable is not maintained, given
  ε small", by "decline from below an unstable threshold, not a recovery
  rate vanishing at a saddle-node". The reader's caveat: the contrast is a
  separation of time scales only for ε about 0.1 or less. ARG-068 (the
  assistant's wording on A's inference, evidence, Rejected) rejects A's
  reading of the case as an instance of CLAIM-521: "The case fits the
  threshold and not the fold." In CASE-227 "critical slowing shows in the
  coordination itself", and "The two cases dissociate different things."

## The components

- CLAIM-079, the paper's (organization-of-will, Section 6.3), thesis,
  demonstrated, Active; first line will-organization, then
  formal-apparatus; grounds THEORY-134 and THEORY-132; THEORY-142
  corroborates it; complements CLAIM-521, CLAIM-566, CLAIM-577, CLAIM-612 and
  CLAIM-625.
- CLAIM-612, A's wording, the reader's framing, thesis, demonstrated,
  Proposed; first line distributed-agency; grounds CASE-231; complements
  CLAIM-079 and CLAIM-566; uses TERM-071.
- CASE-231, A's construction (stipulated), Proposed; first line
  distributed-agency; illustrates CLAIM-612 and CLAIM-079.
- ARG-056, the assistant's wording, existence, Proposed; first line
  distributed-agency; grounds CASE-231; concludes CLAIM-612; uses TERM-071.
- CLAIM-521, A12's, thesis, demonstrated, Active; first line
  distributed-agency; grounds CASE-189; complements CLAIM-414, CLAIM-079,
  CLAIM-481 and CLAIM-626; bears on QUESTION-125.
- CLAIM-626, A's, thesis, demonstrated, Proposed; first line
  distributed-agency; grounds CASE-189; complements CLAIM-478, CLAIM-521
  and CLAIM-481; bears on QUESTION-125.
- CLAIM-481, A20, A21 and A23, counter, demonstrated, Active; first line
  distributed-agency; objects to CLAIM-473; complements CLAIM-478,
  CLAIM-521 and CLAIM-626; grounds LIT-1659 and LIT-1649.
- CASE-227, A's construction (stipulated), Proposed; first line
  distributed-agency; variant of CASE-189; illustrates CLAIM-521 and
  CLAIM-079.
- ARG-068, the assistant's wording on A's inference, evidence, Rejected;
  first line distributed-agency; grounds CASE-227; concludes CLAIM-521.

## Links the components state, and where

Fourteen of the 36 pairs of members are joined by a relation or a
mention, six among the first four entries above, six among the last five,
and two across.

- **Survival extends stability without viability.** CLAIM-079 and
  CLAIM-612 complement each other, and CASE-231 illustrates both.
  CLAIM-612's body: "It extends CLAIM-079's note of 2026-11-04 (under small
  noise "every stable state is only metastable") from deterministic
  stability to statistics conditioned on survival." CLAIM-079's note of
  2026-11-07 says the same from its side: "That extends this claim's note
  of 2026-11-04 from deterministic stability to the statistics of
  survivors." CASE-231's "What it can show": "It extends CLAIM-079 from
  stability to statistics conditioned on survival." CLAIM-612's
  `defeated_if` makes the extension its condition: it is defeated "if it
  only restates CLAIM-079's note of 2026-11-04". ARG-056's critical
  questions: "It also separates what CLAIM-079's note did not: the
  stationary object is a law over survivors, not a deterministic regime."
- **The argument and its case.** ARG-056 grounds on CASE-231 and concludes
  CLAIM-612; CLAIM-612's section "How far 'no evidence' holds" cites it.
- **A decaying capacity as stability without viability.** CASE-227
  illustrates CLAIM-079, and CLAIM-079's note of 2026-11-07 calls A29 §2's
  adaptive HKB system "another mechanism: a mode stable now, with the
  capacity that keeps it stable decaying."
- **Stability without viability and coupling without maintenance.**
  CLAIM-079 and CLAIM-521 complement each other. Neither body names the
  other.
- **The decaying capacity and the fold.** CASE-227 illustrates CLAIM-521,
  and ARG-068 concludes CLAIM-521 from CASE-227 and is Rejected. CLAIM-521's
  note of 2026-11-07 on A29 §2: "The shape matches: a currently effective
  coordination pattern over an unsustained maintenance. The mechanism
  differs." CASE-227's "What it can show" says the same, and ARG-068's
  "What would bear on the conclusion" names the model's upper branch near
  the fold as what would instance CLAIM-521.
- **Slowing and the fold.** CLAIM-626 and CLAIM-521 complement each other.
  CLAIM-626's maintenance arm is CLAIM-521's construction, and its
  `defeated_if` says the claim is "that the three bear oppositely on the
  reduction", which neither CLAIM-478 nor CLAIM-521 states. Its "What it
  does not say" carries CLAIM-521's two caveats. CLAIM-521's note of
  2026-11-07 on A18 §4 says the construction "is the basis of the
  maintenance arm of CLAIM-626".
- **Coupling, time scales and maintenance.** CLAIM-481 complements
  CLAIM-521 and CLAIM-626. CLAIM-521's "What it does not say": "CLAIM-481
  separates what coupling does to time scales; this claim separates what
  coupling shows about its own maintenance." CLAIM-626 names CLAIM-481
  only in its front matter.

## Links to other parts, stated

Seven pairs join a member to a member of another part of the line, by a
relation or a mention in either entry. Each is listed with the entry that
states it.

- **To the reachability part (SYNTHESIS-tmpc35sn).**
  - CLAIM-079 complements CLAIM-577, stated in both entries' front matter.
    CLAIM-577's summary: "It is CLAIM-079's stability without viability,
    produced by a budget rule." Its body: "It is stability without
    viability by budget (CLAIM-079): the organization stays in a stable
    regime while losing the transitions it would need when that regime
    stops serving."
  - CLAIM-589 mentions CLAIM-079 in its body, on a state reached under an
    input bound that cannot be held: "This is the shape of CLAIM-079's split
    between stability and viability, with the input bound as the
    constraint." No relation joins them.
- **To the gluing part (SYNTHESIS-tmphb9rl).**
  - CLAIM-079 complements CLAIM-625, stated in both entries' front matter.
  - CLAIM-625 mentions CASE-231 in its "What it does not say": "On the
    A ↔ B → D chain of CASE-231 every finite horizon has surviving
    histories, while surviving forever has probability zero (A25 §3)."
  - QUESTION-437 mentions CASE-227: "A29 §10 proposes the test on an
    adaptive HKB system (CASE-227)", asking whether locally realizable
    histories of the observed relative phase assemble into a globally
    realizable history of the full system.
- **To the intervention part (SYNTHESIS-tmpe15k3).**
  - CLAIM-521 complements CLAIM-414, stated in both entries' front matter.
    Neither body names the other.
  - CASE-227 mentions CLAIM-522 for A29 §10's proposed study, whose arms
    include "c kept by an outside controller, and c kept by internal
    production (compare CLAIM-522 and CLAIM-456)".

No member links to the effective, frustration or naming parts, to the
small clusters or to the entries the line account (SYNTHESIS-tmpvz4mj) integrates directly.

## Links outside the line, stated

These name entries that are not in formal-apparatus. They are listed so
that the part's dependence is visible.

- CLAIM-079 and CLAIM-612 complement CLAIM-566 (realizability first, also
  distributed-agency): CLAIM-612 "separates what CLAIM-566 calls
  persistence over a horizon from the stationarity of what the survivors
  do". CLAIM-612 and ARG-056 use TERM-071, and CLAIM-612 names
  "Conditional persistence" as a sense TERM-071 lacks; TERM-071's note of
  2026-11-07 records it. CLAIM-612, CASE-231 and ARG-056 cite CLAIM-456
  for regeneration, which an absorbing failure excludes.
- CLAIM-521 and CLAIM-626 ground on CASE-189, CASE-227 is a variant of
  it, and ARG-068 cites it; CASE-227 and ARG-068 cite CLAIM-604's ignition threshold
  as CASE-227's unstable level. CLAIM-521 and CLAIM-626 bear on
  QUESTION-125, whose note of 2026-11-07 places CLAIM-626's locking arm and
  CLAIM-521 in two of its three regions.
- CLAIM-481 objects to CLAIM-473 (Rejected) and "gives a mechanism for
  CLAIM-478's second half"; it cites CLAIM-471's sheaf Laplacian, and
  of the two-cluster window says "That window is CLAIM-478's and
  CLAIM-157's". CLAIM-626's collective arm is CLAIM-478's second
  half.
- CLAIM-079's note of 2026-10-13 says CLAIM-195 rests on it; its "What it
  does not say" leaves who fixes the constraint set to ARG-007. CLAIM-521's
  note of 2026-11-07 records CASE-223 as a proposed social counterpart.

## Not stated on the record

Links across the members that no entry states, tested by ADR-075's step 5
at this review:

- **One thesis over the three separations.** That a system's present
  stability, its coupling strength and its survivors' statistics are each
  no evidence that it persists, across CLAIM-079, CLAIM-521 and CLAIM-612.
  As "can", it is the conjunction of three existence claims, and adds
  nothing. As a general law it is false on the record's own terms:
  CLAIM-521's note of 2026-11-01 on the SCN, where coupling feeds
  maintenance and the dissociation fails, and ARG-056's finding that the
  survivors' distribution carries a trace of the hazard. Not filed.
- **CLAIM-521 as an instance of CLAIM-079.** The two complement each other,
  and no body says that the coupled organization near its fold is stable
  without being viable. Whether it is depends on what CLAIM-079 leaves
  open: who fixes the constraint set (ARG-007) and whether the damage
  drifts, which is Kuehn's mechanism in CLAIM-079's note of 2026-11-04. At
  a fixed damage below the fold the regime is viable. The link turns on a
  free parameter. Not filed.
- **CASE-227 as CLAIM-626's transverse arm driven by maintenance.** That in
  CASE-227 a failing maintained capacity shows as slowing of the mode that
  restores the relative phase. ARG-068 states the content ("critical
  slowing shows in the coordination itself") without naming CLAIM-626, and
  CLAIM-626's conclusion that a slow mode does not by itself say which
  thing is failing already covers it. Not filed.
- **The survivors settle at the exchange Laplacian's gap.** That the time
  scale separation behind CLAIM-612 is, for symmetric exchange among the
  viable regimes, the separation CLAIM-481 gives a dissipative coupling: the
  restricted generator is a Laplacian flow plus the hazards, so the
  survivors' relaxation rate is within the largest hazard of the exchange
  Laplacian's gap, and the ratio of the two times depends on the exchange
  graph, falling as the number of regimes in a line grows. No entry states
  it. It passes by derivation, with a discriminating prediction, and is
  filed at this review as CLAIM-tmpsh6jv (Proposed), which this account integrates.

## What it does not say

- That stable statistics or a strong coupling are evidence against
  persistence (CLAIM-612, "no evidence either way"; CLAIM-521's SCN
  contrast).
- That CASE-227 instances CLAIM-521 (ARG-068, Rejected).
- That the three kinds of slowing are exhaustive (CLAIM-626), or that a
  spectral gap makes an individual (CLAIM-481).
- Anything about regeneration: every failure here is absorbing or a fold.
- Anything with standing of its own.
