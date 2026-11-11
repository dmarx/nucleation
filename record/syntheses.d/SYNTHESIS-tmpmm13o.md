---
status: Proposed
title: 'What a constrained system can reach under a budget is not what it can hold: feasible, reachable and reliably reached come apart, the threshold for a transition is the least peak over admissible paths and can be infinite, a budget enlarges compatibility and reachability only up to what a fixed architecture admits and neither filtration fixes the other, failed transitions sort into obstructions with their own repairs and telling which holds can be hard, an added constraint can improve reliability and never reach, and where an intervention acts can matter more than how much'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the reaching-under-resources part of the realizability line left out
  without a reason given; or a link this account states that no component
  states. Its standing is its components': a component retired or demoted
  takes its clause with it, and nothing here holds the clause up.
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-11'
line:
- realizability
integrates:
- CLAIM-571
- CLAIM-567
- CLAIM-568
- CLAIM-556
- CLAIM-569
- CLAIM-575
- CLAIM-563
- CLAIM-586
- CLAIM-564
- CLAIM-560
- CLAIM-591
- CLAIM-583
- CLAIM-607
- CLAIM-565
- CLAIM-578
- CLAIM-573
- CLAIM-576
- CLAIM-582
- CLAIM-589
- CLAIM-562
- CLAIM-588
- ARG-054
- CLAIM-609
- TERM-105
- TERM-114
- TERM-111
- CASE-198
- CASE-204
- CASE-205
- CASE-206
- CASE-207
- CASE-208
- CASE-212
- CASE-214
- QUESTION-373
- QUESTION-375
- QUESTION-376
- QUESTION-377
- QUESTION-378
- QUESTION-381
- QUESTION-383
- QUESTION-385
- QUESTION-387
- QUESTION-388
- QUESTION-389
- QUESTION-390
- QUESTION-391
- QUESTION-392
- QUESTION-396
- QUESTION-404
- QUESTION-405
- QUESTION-423
- QUESTION-447
---
<!-- inactive-ok-file: ADR-075 ARG-072 CASE-198 CASE-204 CASE-205 CASE-207 CASE-208 CASE-214 CASE-215 CASE-219 CASE-220 CLAIM-573 CLAIM-576 CLAIM-611 SYNTHESIS-024 TERM-111 TERM-116 — Proposed; components and citations, with their standing -->

# SYNTHESIS-tmpmm13o: What a constrained system can reach under a budget is not what it can hold: feasible, reachable and reliably reached come apart, the threshold for a transition is the least peak over admissible paths and can be infinite, a budget enlarges compatibility and reachability only up to what a fixed architecture admits and neither filtration fixes the other, failed transitions sort into obstructions with their own repairs and telling which holds can be hard, an added constraint can improve reliability and never reach, and where an intervention acts can matter more than how much

*A part account of the realizability line ("Resource-bounded realizability
and individuation", ADR-073): the part filed from the pasted synthesis on
constraint architectures (2026-11-04) and the pasted synthesis on
resource-bounded realizability (2026-11-05), with the origami cases filed at
the owner's request and the readings filed beside them. The line's account
is built over it and its four sibling parts (SYNTHESIS-tmpj2fl0 to SYNTHESIS-tmprngy2). Several of
its entries are also in the readiness line, where SYNTHESIS-024 sets them
out; this account integrates them again because their `line` includes
realizability.*

## The account

- **Three properties.** CLAIM-567 (the filer's construction from A's two
  separations, demonstrated, Active): feasible, reachable and reliably
  reached are "three properties, each implied by the next and none
  implying it". It "inserts reachability between the structural
  infeasibility and realized violation that CLAIM-357 separates".
- **The threshold.** CLAIM-571 (A's wording, demonstrated, Active): for a
  fixed architecture and one capacity, the threshold for reaching a target
  "is the least, over admissible transition paths, of the peak requirement
  along the path, and it is infinite when no admissible path joins the
  two". Its body: "It is the resource-quantitative form of the separation
  between a feasible target and a reachable one (CLAIM-567)." CLAIM-563 (A's,
  sharpened by the reader, demonstrated, Active) says when budgets compose:
  closure holds "exactly when b ⊗ b ≤ b, so always for maximum and, for
  sum, only at 0 and infinity", and under maximum the least cost between
  two configurations is CLAIM-571's threshold. TERM-105 (A's, Active) sorts
  resource constraints by the function of a path they bound: "These are not
  equivalent problems." CLAIM-569 (the filer's construction from A's,
  demonstrated, Active): a form's requirements to construct, maintain and
  move are separate, so "having enough to sustain it is not having enough
  to acquire it", and the acquisition no budget buys "is the disconnection
  of CLAIM-571's infinite threshold".
- **The instances.** CASE-206 (the filer's, Active): a degree-4 vertex
  whose switch passes the flat state at a footprint of about 1.866 against
  folded states of 0.75 and 0.875. CASE-204 (a documented specimen,
  Proposed): "The case where no budget helps and only the admissible-move
  set does." CASE-207 (a reported study, Proposed): "Here the budget decides
  what the configuration space is." CASE-198 (the filer's numbers on A's
  sequence, Proposed): "The bottleneck of a fixed architecture is not the
  bottleneck once changing the architecture is a move", and CASE-208 (a
  reported study, Proposed) is "the physical counterpart of CASE-198".
- **Two filtrations.** CLAIM-586 (A's, demonstrated, Active): the
  compatibility complex indexed by a budget grows with it and never exceeds
  the unbudgeted complex, "So a missing face is either short of resources
  at b or structurally frustrated, and the unbudgeted complex tells which."
  CASE-212 (the filer's on A's, Active) shows it, "so raising the budget
  relieves scarcity and leaves the frustration where it was". CLAIM-564 (the
  reader's derivation from A's, demonstrated, Active) makes the
  implications among demands antitone in the budget, "the implication
  counterpart of CLAIM-586's split between being short of resources and
  being structurally frustrated". CLAIM-560 (A's, demonstrated, Active)
  pairs the compatibility filtration with a reachability filtration:
  "Neither fixes the other." CLAIM-583 (the filer's construction from A's,
  demonstrated, Active) gives two systems with the same complex, move rule
  and costs and different reachability, and CLAIM-607 (the record's own
  conditional demonstration, split from it, Active) the same "one level
  up, for constraint languages". CLAIM-591 (A's, demonstrated, Active):
  under directed moves "persistence gives a necessary condition only".
- **Obstructions and their repairs.** CLAIM-568 (A's, interpretive, Active):
  four obstructions with their remedies, and "added actuation can overcome
  an energy barrier and cannot join disconnected configurations"; its
  summary says the four "refine the gaps between CLAIM-567's feasible,
  reachable and reliable". CASE-205 (the filer's instance on A's model,
  Proposed) is its control limitation, where which profiles can be
  commanded "is fixed by the grouping, not the count". CLAIM-556 (A's,
  interpretive, Active) adds compatibility before and regeneration after,
  "so a diagnosis runs through six levels, each with its own repair".
  Whether a failure of information is a further level is QUESTION-404
  (Open, moved from CLAIM-568's defeat condition).
- **Diagnosis and complexity.** CLAIM-578 (A's, demonstrated, Active):
  complexity belongs to a family of problems, not to one space, and "For
  the record it means that one organization's compatibility complex carries
  no complexity." CLAIM-575 (the filer's, from the complexity readings,
  demonstrated, Active), resting on it: "So telling geometric disconnection
  from a capacity bottleneck can be PSPACE-hard, and knowing how far over
  budget the cheapest path is can be NP-hard." CLAIM-565 (the filer's, from
  A's question and the readings, demonstrated, Active): with constants,
  positive 1-in-3 SAT and positive NAE-3SAT have "the same clone, and
  navigation on opposite sides of the dichotomy".
- **Constraints, inputs and placement.** CLAIM-582 (A's, the second half's
  construction the filer's, demonstrated, Active): an added hard constraint
  in a fixed model cannot enlarge reach, and "So the reachability dimension
  of CLAIM-354 cannot grow under an added constraint in a fixed model";
  what it can improve is robustness or reliability. CLAIM-589 (A's,
  demonstrated, Active): permitted, driven and achievable motions are three
  objects, "the second contained in the first at each instant, while over a
  horizon what is reachable can exceed what either spans at an instant".
  CLAIM-562 (the filer's construction from A's reading of Stern, Pinson and
  Murugan, empirical, Active): where actuators sit predicts success better
  than how many, and an added actuator can stop a successful folding; "A
  count of interventions is blind to that." CASE-214 (the filer's on A's
  stage, Proposed) is a static analogue of CLAIM-345: equal freedom spaces,
  different disturbance error and drive force.
- **Mismatch as a design target.** CLAIM-588 (A's, interpretive, Active):
  relieving, redistributing and exploiting a mismatch are three targets,
  and "The last two could occur without achieving the first." ARG-054 (the
  status review's, analogy, Active) concludes it from Rocks and Mehta as a
  parallel: "The separation transfers: what is carried, and what it does,
  can change while the compatibility structure stays fixed." CLAIM-609 (the
  status review's own result, demonstrated, Active) proves that the force
  exciting a linear zero mode is (T + λI)u, and "It sharpens the reading of
  Rocks and Mehta (THEORY-1414)".
- **The frame and the general object.** TERM-114 (A's, Active) is the
  resource-bounded constraint system the claims are stated in. CLAIM-576
  (A's conjecture, interpretive, Proposed): "Each of the three ways is held
  separately; the conjecture is that together they, and not a state space,
  are the invariant." TERM-111 (A's, Proposed) separates expressive,
  computational and scaling universality, and CLAIM-573 (A's hypothesis,
  interpretive, Proposed) is stated in its computational sense; QUESTION-385
  (A's, Open) is its test.

What stays open is A's programme of questions on constraint architectures:
who supplies the resource that crosses a bottleneck (QUESTION-373, the
assistant's), whether a topological summary detects navigation complexity
(QUESTION-375), what fixes navigation beyond Boolean languages (QUESTION-376,
answered for Boolean languages with constants by CLAIM-565), thresholds in
an organization's feasible set (QUESTION-377), freedoms at an interface of
rigid parts (QUESTION-378), synthesis of architectures from capabilities
(QUESTION-381), what survives of FACT's duality (QUESTION-383), stress as a
resource (QUESTION-387), programmable against self-governing
reconfiguration (QUESTION-388), conflict as load or missing freedom
(QUESTION-389), what coupling origami modules generates (QUESTION-390),
when an effective constraint fails (QUESTION-391), when an intervention
creates a capability rather than cheapening one (QUESTION-392), and when
memory helps control (QUESTION-396), with three replications of readings
the part rests on (QUESTION-405, QUESTION-423, QUESTION-447).

## The components

- CLAIM-571, A's wording, thesis, demonstrated, Active; first line
  readiness, then realizability and formal-apparatus.
- CLAIM-567, the filer's construction from A's, thesis, demonstrated,
  Active; also readiness and formal-apparatus; rests on CLAIM-571.
- CLAIM-568, A's, thesis, interpretive, Active; also readiness; rests on
  CLAIM-571.
- CLAIM-556, A's, thesis, interpretive, Active; also readiness; rests on
  CLAIM-568, CLAIM-566 (the line's hinge), CLAIM-347 and CLAIM-586.
- CLAIM-569, the filer's construction from A's, thesis, demonstrated,
  Active; first line readiness; rests on CLAIM-571; uses TERM-105.
- CLAIM-575, the filer's, thesis, demonstrated, Active; also
  formal-apparatus; rests on CLAIM-578.
- CLAIM-563, A's, sharpened by the reader, thesis, demonstrated, Active;
  also formal-apparatus; uses TERM-105 and TERM-114.
- CLAIM-586, A's, thesis, demonstrated, Active; also formal-apparatus and
  distributed-agency; rests on CLAIM-347.
- CLAIM-564, the reader's derivation from A's, thesis, demonstrated,
  Active; also formal-apparatus; grounds CASE-212.
- CLAIM-560, A's, thesis, demonstrated, Active; also formal-apparatus;
  rests on CLAIM-586 and CLAIM-571.
- CLAIM-591, A's, thesis, demonstrated, Active; also formal-apparatus.
- CLAIM-583, the filer's construction from A's, thesis, demonstrated,
  Active; also formal-apparatus; rests on CLAIM-347.
- CLAIM-607, the record's own conditional demonstration, split from
  CLAIM-583, thesis, demonstrated, Active; also formal-apparatus.
- CLAIM-565, the filer's (the Post-lattice step the filer's and the
  lead's), thesis, demonstrated, Active; also formal-apparatus.
- CLAIM-578, A's, thesis, demonstrated, Active; also formal-apparatus.
- CLAIM-573, A's hypothesis, thesis, interpretive, Proposed; uses TERM-111
  and TERM-114.
- CLAIM-576, A's conjecture, thesis, interpretive, Proposed; rests on
  CLAIM-583.
- CLAIM-582, A's, thesis, demonstrated, Active; also formal-apparatus.
- CLAIM-589, A's, thesis, demonstrated, Active; also formal-apparatus;
  rests on CLAIM-345 and CLAIM-542.
- CLAIM-562, the filer's construction from A's reading, thesis, empirical,
  Active.
- CLAIM-588, A's, thesis, interpretive, Active; rests on CLAIM-347 and
  CLAIM-538.
- ARG-054, the status review's wording, analogy, Active; concludes
  CLAIM-588.
- CLAIM-609, the status review's own result, thesis, demonstrated, Active.
- TERM-105, A's, Active; first line readiness. TERM-114, A's, Active.
  TERM-111, A's, Proposed.
- CASE-206, the filer's construction, Active; also readiness. CASE-212,
  the filer's construction on A's definition, Active.
- CASE-198 and CASE-205, constructions on A's models with the filer's
  numbers, Proposed; first line readiness. CASE-204, a documented specimen,
  and CASE-207 and CASE-208, reported studies, filed at the owner's request,
  Proposed. CASE-214, the filer's construction, Proposed; it illustrates
  CLAIM-345, outside the line, and names no component.
- QUESTION-373, the assistant's, Open; also distributed-agency.
- QUESTION-375, QUESTION-376, QUESTION-383 and QUESTION-391, A's, Open; also
  formal-apparatus.
- QUESTION-377, QUESTION-378, QUESTION-381, QUESTION-385, QUESTION-387,
  QUESTION-389 and QUESTION-396, A's, Open.
- QUESTION-388 and QUESTION-390, A's, Open; also distributed-agency;
  QUESTION-390 refines QUESTION-283.
- QUESTION-392, A's, Open; also readiness.
- QUESTION-404, moved from CLAIM-568's defeat condition by the
  twenty-sixth status review, Open; also readiness.
- QUESTION-405, QUESTION-423 and QUESTION-447, Open: promotion conditions
  moved from THEORY-1417, THEORY-1414 and THEORY-1428. QUESTION-405 and
  QUESTION-447 link to no component by a relation or a mention; they reach
  the part through the readings CLAIM-568, CASE-208 and CLAIM-588 cite, and
  are listed because their `line` field places them here. QUESTION-423's
  note names CLAIM-609.

## Links the components state, and where

- **Everything rests on the threshold and the three properties.**
  CLAIM-567, CLAIM-568, CLAIM-569 and CLAIM-560 rest on CLAIM-571, and
  CASE-198, CASE-204, CASE-206, CASE-207 and CASE-208 illustrate it;
  CASE-204 and CASE-206 also illustrate CLAIM-567. CLAIM-571's note of
  2026-11-05 lists the cases; CLAIM-567's notes add CASE-206 and CASE-207.
- **Composition and the threshold.** CLAIM-563's body: "The peak case is
  the record's threshold." CLAIM-571's note of 2026-11-05: "In that
  category the affordable processes compose at every budget (CLAIM-563)."
- **The filtrations.** CLAIM-560's body: "CLAIM-583 shows reachability can
  differ where the complex agrees at every budget." CLAIM-591 says the
  persistence of sublevel sets "bounds the reachability filtration of
  CLAIM-560 from above". CLAIM-586's note of 2026-11-05 reads CLAIM-564,
  CLAIM-583 and CLAIM-578 as what the complex does not carry.
- **Obstructions.** CLAIM-568's body: "CLAIM-586 makes the same split for
  joint demands rather than paths". CLAIM-568's note of 2026-11-05:
  "CLAIM-575 holds it a property of the four, not a fifth", and CLAIM-591
  states the deadlock as a disconnection under directed paths. CLAIM-556's
  repair of reachability cites CASE-207. CLAIM-578: "Diagnosing which
  obstruction blocks a transition is another, with its own complexity
  (CLAIM-575)."
- **Constraints and inputs.** CLAIM-589's reliability step cites
  CLAIM-567's fork; CLAIM-582's reliability witness is the same fork with
  the distractor blocked. TERM-114's "What it is not" keeps CLAIM-582's
  guard. CLAIM-567's body: "Where intervention is placed can matter more
  than how much (CLAIM-562)."
- **The general object.** CLAIM-576 cites CLAIM-586, CLAIM-571, CLAIM-582,
  CASE-198, QUESTION-392 and CLAIM-583 for its three ways. QUESTION-392
  names CASE-198 as a case of its third kind, and its note of 2026-11-05
  cites CLAIM-556 as one form of a classification of interventions. CLAIM-573 is stated in
  TERM-111 and names CLAIM-556's obstruction profile as one structure a
  simulation would preserve; QUESTION-385 calls CLAIM-573 the hypothesis it
  would test. TERM-114's "What it adds" places CLAIM-563, CLAIM-560,
  CLAIM-591, CASE-198 and CASE-207.
- **The questions.** QUESTION-387 is asked after CLAIM-588's table.
  QUESTION-376's summary: "CLAIM-565 gives a pair with one clone and
  opposite navigation." QUESTION-377 relates to CLAIM-571 and CLAIM-567;
  QUESTION-373 cites CLAIM-571; QUESTION-389 cites CLAIM-567; QUESTION-391's
  note of 2026-11-05 reads CASE-207 and CLAIM-586; QUESTION-388's note reads
  TERM-114; QUESTION-390 cites CASE-206 and QUESTION-385; QUESTION-404
  cites CLAIM-568 and CLAIM-556.

## Links across to the sibling parts, stated

- **To budgeted individuation (SYNTHESIS-tmpj2fl0).** CLAIM-581 and CLAIM-590 rest on
  CLAIM-571 and CLAIM-563; CLAIM-590 grounds on CASE-206 and CLAIM-572 and
  CLAIM-592 are illustrated by it. CLAIM-574: "CLAIM-564 is the same shape
  on the side of demands". CLAIM-572 calls a reallocation between
  observing and acting "a transition with its own threshold, as in
  CLAIM-571, but in budget space rather than configuration space".
  TERM-116 prices CLAIM-569's three requirements per configuration.
- **To assembly and nucleation (SYNTHESIS-tmpq7bvl).** CLAIM-599 rests on CLAIM-562,
  and CASE-215 illustrates it. CASE-216 illustrates CLAIM-569 and CLAIM-571;
  CASE-217, CASE-219 and CASE-220 illustrate CLAIM-567. CLAIM-594
  complements CLAIM-569. QUESTION-380 asks when a local face raises
  "reliable emergence and not only feasibility (CLAIM-567)".
- **To transient-support, outside the line.** CLAIM-601 uses TERM-105, reading a savings buffer as
  a replenishable reserve.
- **To persisting individuals (SYNTHESIS-tmprngy2).** CLAIM-611 rests on CLAIM-576 and
  CLAIM-567; QUESTION-379 cites CLAIM-569 and TERM-114; ARG-072 names
  CLAIM-567's split and ARG-054's difference.
- **To the line's hinge.** CLAIM-556 rests on CLAIM-566, and CLAIM-567's
  note of 2026-11-05 reads A's synthesis on DNA origami as "this claim
  together with CLAIM-566".

## Not stated on the record

Links across the components that no entry states, tested by ADR-075's
step 5 at this review and not filed:

- **A budget as a constraint that can cost reliability.** That raising a
  budget at a fixed architecture can lower how reliably a process reaches
  a target, by admitting a distractor branch, while it cannot shrink what
  is reachable (CLAIM-582's reliability witness, with CLAIM-560's and
  CLAIM-586's monotonicity). How a budget acts on a running process is a
  free parameter: if it aborts runs that exceed it, nothing is gained at the
  lower budget, and if it removes the unaffordable continuations, the
  sentence is CLAIM-582's witness with the constraint called a budget.
- **Placement over quantity as a general law.** That where a fixed
  quantity of intervention is spent decides more than the quantity, across
  CLAIM-562's actuators, CASE-215's timing and CLAIM-602's order of supply
  (transient-support).
  As "can", it is a conjunction of held instances; as a general law, it is
  against CLAIM-571's and CLAIM-586's budgets and the threshold on size that
  CLAIM-600 adds to CLAIM-602.
- **That the state space is not enough.** CLAIM-576 draws it from
  CLAIM-583; CLAIM-576's own note of 2026-11-06 says that CLAIM-583 does not show
  it, since with a fixed move rule the configurations and their moves
  carry reachability, and that no comparison is on file that a costed
  configuration space with its moves fails to make.

## What it does not say

- That organizations have configuration spaces with such costs; each
  claim here says its organizational reading is A's analogy or a model.
- That the four obstructions or the six levels are exhaustive (CLAIM-568,
  CLAIM-556; QUESTION-404).
- That any universality across substrates is shown (CLAIM-573, Proposed).
- Anything with standing of its own.
