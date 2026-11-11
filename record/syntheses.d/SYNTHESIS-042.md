---
number: 42
status: Proposed
formerly:
- SYNTHESIS-tmpmm13o
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

# SYNTHESIS-042: What a constrained system can reach under a budget is not what it can hold: feasible, reachable and reliably reached come apart, the threshold for a transition is the least peak over admissible paths and can be infinite, a budget enlarges compatibility and reachability only up to what a fixed architecture admits and neither filtration fixes the other, failed transitions sort into obstructions with their own repairs and telling which holds can be hard, an added constraint can improve reliability and never reach, and where an intervention acts can matter more than how much

*A part account of the realizability line ("Resource-bounded realizability
and individuation", [ADR-073](../decisions.d/ADR-073.md)): the part filed from the pasted synthesis on
constraint architectures (2026-11-04) and the pasted synthesis on
resource-bounded realizability (2026-11-05), with the origami cases filed at
the owner's request and the readings filed beside them. The line's account
is built over it and its four sibling parts ([SYNTHESIS-040](SYNTHESIS-040.md) to [SYNTHESIS-046](SYNTHESIS-046.md)). Several of
its entries are also in the readiness line, where [SYNTHESIS-024](SYNTHESIS-024.md) sets them
out; this account integrates them again because their `line` includes
realizability.*

## The account

- **Three properties.** [CLAIM-567](../claims.d/CLAIM-567.md) (the filer's construction from A's two
  separations, demonstrated, Active): feasible, reachable and reliably
  reached are "three properties, each implied by the next and none
  implying it". It "inserts reachability between the structural
  infeasibility and realized violation that [CLAIM-357](../claims.d/CLAIM-357.md) separates".
- **The threshold.** [CLAIM-571](../claims.d/CLAIM-571.md) (A's wording, demonstrated, Active): for a
  fixed architecture and one capacity, the threshold for reaching a target
  "is the least, over admissible transition paths, of the peak requirement
  along the path, and it is infinite when no admissible path joins the
  two". Its body: "It is the resource-quantitative form of the separation
  between a feasible target and a reachable one ([CLAIM-567](../claims.d/CLAIM-567.md))." [CLAIM-563](../claims.d/CLAIM-563.md) (A's,
  sharpened by the reader, demonstrated, Active) says when budgets compose:
  closure holds "exactly when b ⊗ b ≤ b, so always for maximum and, for
  sum, only at 0 and infinity", and under maximum the least cost between
  two configurations is [CLAIM-571](../claims.d/CLAIM-571.md)'s threshold. [TERM-105](../terms.d/TERM-105.md) (A's, Active) sorts
  resource constraints by the function of a path they bound: "These are not
  equivalent problems." [CLAIM-569](../claims.d/CLAIM-569.md) (the filer's construction from A's,
  demonstrated, Active): a form's requirements to construct, maintain and
  move are separate, so "having enough to sustain it is not having enough
  to acquire it", and the acquisition no budget buys "is the disconnection
  of [CLAIM-571](../claims.d/CLAIM-571.md)'s infinite threshold".
- **The instances.** [CASE-206](../cases.d/CASE-206.md) (the filer's, Active): a degree-4 vertex
  whose switch passes the flat state at a footprint of about 1.866 against
  folded states of 0.75 and 0.875. [CASE-204](../cases.d/CASE-204.md) (a documented specimen,
  Proposed): "The case where no budget helps and only the admissible-move
  set does." [CASE-207](../cases.d/CASE-207.md) (a reported study, Proposed): "Here the budget decides
  what the configuration space is." [CASE-198](../cases.d/CASE-198.md) (the filer's numbers on A's
  sequence, Proposed): "The bottleneck of a fixed architecture is not the
  bottleneck once changing the architecture is a move", and [CASE-208](../cases.d/CASE-208.md) (a
  reported study, Proposed) is "the physical counterpart of [CASE-198](../cases.d/CASE-198.md)".
- **Two filtrations.** [CLAIM-586](../claims.d/CLAIM-586.md) (A's, demonstrated, Active): the
  compatibility complex indexed by a budget grows with it and never exceeds
  the unbudgeted complex, "So a missing face is either short of resources
  at b or structurally frustrated, and the unbudgeted complex tells which."
  [CASE-212](../cases.d/CASE-212.md) (the filer's on A's, Active) shows it, "so raising the budget
  relieves scarcity and leaves the frustration where it was". [CLAIM-564](../claims.d/CLAIM-564.md) (the
  reader's derivation from A's, demonstrated, Active) makes the
  implications among demands antitone in the budget, "the implication
  counterpart of [CLAIM-586](../claims.d/CLAIM-586.md)'s split between being short of resources and
  being structurally frustrated". [CLAIM-560](../claims.d/CLAIM-560.md) (A's, demonstrated, Active)
  pairs the compatibility filtration with a reachability filtration:
  "Neither fixes the other." [CLAIM-583](../claims.d/CLAIM-583.md) (the filer's construction from A's,
  demonstrated, Active) gives two systems with the same complex, move rule
  and costs and different reachability, and [CLAIM-607](../claims.d/CLAIM-607.md) (the record's own
  conditional demonstration, split from it, Active) the same "one level
  up, for constraint languages". [CLAIM-591](../claims.d/CLAIM-591.md) (A's, demonstrated, Active):
  under directed moves "persistence gives a necessary condition only".
- **Obstructions and their repairs.** [CLAIM-568](../claims.d/CLAIM-568.md) (A's, interpretive, Active):
  four obstructions with their remedies, and "added actuation can overcome
  an energy barrier and cannot join disconnected configurations"; its
  summary says the four "refine the gaps between [CLAIM-567](../claims.d/CLAIM-567.md)'s feasible,
  reachable and reliable". [CASE-205](../cases.d/CASE-205.md) (the filer's instance on A's model,
  Proposed) is its control limitation, where which profiles can be
  commanded "is fixed by the grouping, not the count". [CLAIM-556](../claims.d/CLAIM-556.md) (A's,
  interpretive, Active) adds compatibility before and regeneration after,
  "so a diagnosis runs through six levels, each with its own repair".
  Whether a failure of information is a further level is [QUESTION-404](../questions.d/QUESTION-404.md)
  (Open, moved from [CLAIM-568](../claims.d/CLAIM-568.md)'s defeat condition).
- **Diagnosis and complexity.** [CLAIM-578](../claims.d/CLAIM-578.md) (A's, demonstrated, Active):
  complexity belongs to a family of problems, not to one space, and "For
  the record it means that one organization's compatibility complex carries
  no complexity." [CLAIM-575](../claims.d/CLAIM-575.md) (the filer's, from the complexity readings,
  demonstrated, Active), resting on it: "So telling geometric disconnection
  from a capacity bottleneck can be PSPACE-hard, and knowing how far over
  budget the cheapest path is can be NP-hard." [CLAIM-565](../claims.d/CLAIM-565.md) (the filer's, from
  A's question and the readings, demonstrated, Active): with constants,
  positive 1-in-3 SAT and positive NAE-3SAT have "the same clone, and
  navigation on opposite sides of the dichotomy".
- **Constraints, inputs and placement.** [CLAIM-582](../claims.d/CLAIM-582.md) (A's, the second half's
  construction the filer's, demonstrated, Active): an added hard constraint
  in a fixed model cannot enlarge reach, and "So the reachability dimension
  of [CLAIM-354](../claims.d/CLAIM-354.md) cannot grow under an added constraint in a fixed model";
  what it can improve is robustness or reliability. [CLAIM-589](../claims.d/CLAIM-589.md) (A's,
  demonstrated, Active): permitted, driven and achievable motions are three
  objects, "the second contained in the first at each instant, while over a
  horizon what is reachable can exceed what either spans at an instant".
  [CLAIM-562](../claims.d/CLAIM-562.md) (the filer's construction from A's reading of Stern, Pinson and
  Murugan, empirical, Active): where actuators sit predicts success better
  than how many, and an added actuator can stop a successful folding; "A
  count of interventions is blind to that." [CASE-214](../cases.d/CASE-214.md) (the filer's on A's
  stage, Proposed) is a static analogue of [CLAIM-345](../claims.d/CLAIM-345.md): equal freedom spaces,
  different disturbance error and drive force.
- **Mismatch as a design target.** [CLAIM-588](../claims.d/CLAIM-588.md) (A's, interpretive, Active):
  relieving, redistributing and exploiting a mismatch are three targets,
  and "The last two could occur without achieving the first." [ARG-054](../arguments.d/ARG-054.md) (the
  status review's, analogy, Active) concludes it from Rocks and Mehta as a
  parallel: "The separation transfers: what is carried, and what it does,
  can change while the compatibility structure stays fixed." [CLAIM-609](../claims.d/CLAIM-609.md) (the
  status review's own result, demonstrated, Active) proves that the force
  exciting a linear zero mode is (T + λI)u, and "It sharpens the reading of
  Rocks and Mehta ([THEORY-1414](../theory.d/THEORY-1414.md))".
- **The frame and the general object.** [TERM-114](../terms.d/TERM-114.md) (A's, Active) is the
  resource-bounded constraint system the claims are stated in. [CLAIM-576](../claims.d/CLAIM-576.md)
  (A's conjecture, interpretive, Proposed): "Each of the three ways is held
  separately; the conjecture is that together they, and not a state space,
  are the invariant." [TERM-111](../terms.d/TERM-111.md) (A's, Proposed) separates expressive,
  computational and scaling universality, and [CLAIM-573](../claims.d/CLAIM-573.md) (A's hypothesis,
  interpretive, Proposed) is stated in its computational sense; [QUESTION-385](../questions.d/QUESTION-385.md)
  (A's, Open) is its test.

What stays open is A's programme of questions on constraint architectures:
who supplies the resource that crosses a bottleneck ([QUESTION-373](../questions.d/QUESTION-373.md), the
assistant's), whether a topological summary detects navigation complexity
([QUESTION-375](../questions.d/QUESTION-375.md)), what fixes navigation beyond Boolean languages ([QUESTION-376](../questions.d/QUESTION-376.md),
answered for Boolean languages with constants by [CLAIM-565](../claims.d/CLAIM-565.md)), thresholds in
an organization's feasible set ([QUESTION-377](../questions.d/QUESTION-377.md)), freedoms at an interface of
rigid parts ([QUESTION-378](../questions.d/QUESTION-378.md)), synthesis of architectures from capabilities
([QUESTION-381](../questions.d/QUESTION-381.md)), what survives of FACT's duality ([QUESTION-383](../questions.d/QUESTION-383.md)), stress as a
resource ([QUESTION-387](../questions.d/QUESTION-387.md)), programmable against self-governing
reconfiguration ([QUESTION-388](../questions.d/QUESTION-388.md)), conflict as load or missing freedom
([QUESTION-389](../questions.d/QUESTION-389.md)), what coupling origami modules generates ([QUESTION-390](../questions.d/QUESTION-390.md)),
when an effective constraint fails ([QUESTION-391](../questions.d/QUESTION-391.md)), when an intervention
creates a capability rather than cheapening one ([QUESTION-392](../questions.d/QUESTION-392.md)), and when
memory helps control ([QUESTION-396](../questions.d/QUESTION-396.md)), with three replications of readings
the part rests on ([QUESTION-405](../questions.d/QUESTION-405.md), [QUESTION-423](../questions.d/QUESTION-423.md), [QUESTION-447](../questions.d/QUESTION-447.md)).

## The components

- [CLAIM-571](../claims.d/CLAIM-571.md), A's wording, thesis, demonstrated, Active; first line
  readiness, then realizability and formal-apparatus.
- [CLAIM-567](../claims.d/CLAIM-567.md), the filer's construction from A's, thesis, demonstrated,
  Active; also readiness and formal-apparatus; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-568](../claims.d/CLAIM-568.md), A's, thesis, interpretive, Active; also readiness; rests on
  [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-556](../claims.d/CLAIM-556.md), A's, thesis, interpretive, Active; also readiness; rests on
  [CLAIM-568](../claims.d/CLAIM-568.md), [CLAIM-566](../claims.d/CLAIM-566.md) (the line's hinge), [CLAIM-347](../claims.d/CLAIM-347.md) and [CLAIM-586](../claims.d/CLAIM-586.md).
- [CLAIM-569](../claims.d/CLAIM-569.md), the filer's construction from A's, thesis, demonstrated,
  Active; first line readiness; rests on [CLAIM-571](../claims.d/CLAIM-571.md); uses [TERM-105](../terms.d/TERM-105.md).
- [CLAIM-575](../claims.d/CLAIM-575.md), the filer's, thesis, demonstrated, Active; also
  formal-apparatus; rests on [CLAIM-578](../claims.d/CLAIM-578.md).
- [CLAIM-563](../claims.d/CLAIM-563.md), A's, sharpened by the reader, thesis, demonstrated, Active;
  also formal-apparatus; uses [TERM-105](../terms.d/TERM-105.md) and [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-586](../claims.d/CLAIM-586.md), A's, thesis, demonstrated, Active; also formal-apparatus and
  distributed-agency; rests on [CLAIM-347](../claims.d/CLAIM-347.md).
- [CLAIM-564](../claims.d/CLAIM-564.md), the reader's derivation from A's, thesis, demonstrated,
  Active; also formal-apparatus; grounds [CASE-212](../cases.d/CASE-212.md).
- [CLAIM-560](../claims.d/CLAIM-560.md), A's, thesis, demonstrated, Active; also formal-apparatus;
  rests on [CLAIM-586](../claims.d/CLAIM-586.md) and [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-591](../claims.d/CLAIM-591.md), A's, thesis, demonstrated, Active; also formal-apparatus.
- [CLAIM-583](../claims.d/CLAIM-583.md), the filer's construction from A's, thesis, demonstrated,
  Active; also formal-apparatus; rests on [CLAIM-347](../claims.d/CLAIM-347.md).
- [CLAIM-607](../claims.d/CLAIM-607.md), the record's own conditional demonstration, split from
  [CLAIM-583](../claims.d/CLAIM-583.md), thesis, demonstrated, Active; also formal-apparatus.
- [CLAIM-565](../claims.d/CLAIM-565.md), the filer's (the Post-lattice step the filer's and the
  lead's), thesis, demonstrated, Active; also formal-apparatus.
- [CLAIM-578](../claims.d/CLAIM-578.md), A's, thesis, demonstrated, Active; also formal-apparatus.
- [CLAIM-573](../claims.d/CLAIM-573.md), A's hypothesis, thesis, interpretive, Proposed; uses [TERM-111](../terms.d/TERM-111.md)
  and [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-576](../claims.d/CLAIM-576.md), A's conjecture, thesis, interpretive, Proposed; rests on
  [CLAIM-583](../claims.d/CLAIM-583.md).
- [CLAIM-582](../claims.d/CLAIM-582.md), A's, thesis, demonstrated, Active; also formal-apparatus.
- [CLAIM-589](../claims.d/CLAIM-589.md), A's, thesis, demonstrated, Active; also formal-apparatus;
  rests on [CLAIM-345](../claims.d/CLAIM-345.md) and [CLAIM-542](../claims.d/CLAIM-542.md).
- [CLAIM-562](../claims.d/CLAIM-562.md), the filer's construction from A's reading, thesis, empirical,
  Active.
- [CLAIM-588](../claims.d/CLAIM-588.md), A's, thesis, interpretive, Active; rests on [CLAIM-347](../claims.d/CLAIM-347.md) and
  [CLAIM-538](../claims.d/CLAIM-538.md).
- [ARG-054](../arguments.d/ARG-054.md), the status review's wording, analogy, Active; concludes
  [CLAIM-588](../claims.d/CLAIM-588.md).
- [CLAIM-609](../claims.d/CLAIM-609.md), the status review's own result, thesis, demonstrated, Active.
- [TERM-105](../terms.d/TERM-105.md), A's, Active; first line readiness. [TERM-114](../terms.d/TERM-114.md), A's, Active.
  [TERM-111](../terms.d/TERM-111.md), A's, Proposed.
- [CASE-206](../cases.d/CASE-206.md), the filer's construction, Active; also readiness. [CASE-212](../cases.d/CASE-212.md),
  the filer's construction on A's definition, Active.
- [CASE-198](../cases.d/CASE-198.md) and [CASE-205](../cases.d/CASE-205.md), constructions on A's models with the filer's
  numbers, Proposed; first line readiness. [CASE-204](../cases.d/CASE-204.md), a documented specimen,
  and [CASE-207](../cases.d/CASE-207.md) and [CASE-208](../cases.d/CASE-208.md), reported studies, filed at the owner's request,
  Proposed. [CASE-214](../cases.d/CASE-214.md), the filer's construction, Proposed; it illustrates
  [CLAIM-345](../claims.d/CLAIM-345.md), outside the line, and names no component.
- [QUESTION-373](../questions.d/QUESTION-373.md), the assistant's, Open; also distributed-agency.
- [QUESTION-375](../questions.d/QUESTION-375.md), [QUESTION-376](../questions.d/QUESTION-376.md), [QUESTION-383](../questions.d/QUESTION-383.md) and [QUESTION-391](../questions.d/QUESTION-391.md), A's, Open; also
  formal-apparatus.
- [QUESTION-377](../questions.d/QUESTION-377.md), [QUESTION-378](../questions.d/QUESTION-378.md), [QUESTION-381](../questions.d/QUESTION-381.md), [QUESTION-385](../questions.d/QUESTION-385.md), [QUESTION-387](../questions.d/QUESTION-387.md),
  [QUESTION-389](../questions.d/QUESTION-389.md) and [QUESTION-396](../questions.d/QUESTION-396.md), A's, Open.
- [QUESTION-388](../questions.d/QUESTION-388.md) and [QUESTION-390](../questions.d/QUESTION-390.md), A's, Open; also distributed-agency;
  [QUESTION-390](../questions.d/QUESTION-390.md) refines [QUESTION-283](../questions.d/QUESTION-283.md).
- [QUESTION-392](../questions.d/QUESTION-392.md), A's, Open; also readiness.
- [QUESTION-404](../questions.d/QUESTION-404.md), moved from [CLAIM-568](../claims.d/CLAIM-568.md)'s defeat condition by the
  twenty-sixth status review, Open; also readiness.
- [QUESTION-405](../questions.d/QUESTION-405.md), [QUESTION-423](../questions.d/QUESTION-423.md) and [QUESTION-447](../questions.d/QUESTION-447.md), Open: promotion conditions
  moved from [THEORY-1417](../theory.d/THEORY-1417.md), [THEORY-1414](../theory.d/THEORY-1414.md) and [THEORY-1428](../theory.d/THEORY-1428.md). [QUESTION-405](../questions.d/QUESTION-405.md) and
  [QUESTION-447](../questions.d/QUESTION-447.md) link to no component by a relation or a mention; they reach
  the part through the readings [CLAIM-568](../claims.d/CLAIM-568.md), [CASE-208](../cases.d/CASE-208.md) and [CLAIM-588](../claims.d/CLAIM-588.md) cite, and
  are listed because their `line` field places them here. [QUESTION-423](../questions.d/QUESTION-423.md)'s
  note names [CLAIM-609](../claims.d/CLAIM-609.md).

## Links the components state, and where

- **Everything rests on the threshold and the three properties.**
  [CLAIM-567](../claims.d/CLAIM-567.md), [CLAIM-568](../claims.d/CLAIM-568.md), [CLAIM-569](../claims.d/CLAIM-569.md) and [CLAIM-560](../claims.d/CLAIM-560.md) rest on [CLAIM-571](../claims.d/CLAIM-571.md), and
  [CASE-198](../cases.d/CASE-198.md), [CASE-204](../cases.d/CASE-204.md), [CASE-206](../cases.d/CASE-206.md), [CASE-207](../cases.d/CASE-207.md) and [CASE-208](../cases.d/CASE-208.md) illustrate it;
  [CASE-204](../cases.d/CASE-204.md) and [CASE-206](../cases.d/CASE-206.md) also illustrate [CLAIM-567](../claims.d/CLAIM-567.md). [CLAIM-571](../claims.d/CLAIM-571.md)'s note of
  2026-11-05 lists the cases; [CLAIM-567](../claims.d/CLAIM-567.md)'s notes add [CASE-206](../cases.d/CASE-206.md) and [CASE-207](../cases.d/CASE-207.md).
- **Composition and the threshold.** [CLAIM-563](../claims.d/CLAIM-563.md)'s body: "The peak case is
  the record's threshold." [CLAIM-571](../claims.d/CLAIM-571.md)'s note of 2026-11-05: "In that
  category the affordable processes compose at every budget ([CLAIM-563](../claims.d/CLAIM-563.md))."
- **The filtrations.** [CLAIM-560](../claims.d/CLAIM-560.md)'s body: "[CLAIM-583](../claims.d/CLAIM-583.md) shows reachability can
  differ where the complex agrees at every budget." [CLAIM-591](../claims.d/CLAIM-591.md) says the
  persistence of sublevel sets "bounds the reachability filtration of
  [CLAIM-560](../claims.d/CLAIM-560.md) from above". [CLAIM-586](../claims.d/CLAIM-586.md)'s note of 2026-11-05 reads [CLAIM-564](../claims.d/CLAIM-564.md),
  [CLAIM-583](../claims.d/CLAIM-583.md) and [CLAIM-578](../claims.d/CLAIM-578.md) as what the complex does not carry.
- **Obstructions.** [CLAIM-568](../claims.d/CLAIM-568.md)'s body: "[CLAIM-586](../claims.d/CLAIM-586.md) makes the same split for
  joint demands rather than paths". [CLAIM-568](../claims.d/CLAIM-568.md)'s note of 2026-11-05:
  "[CLAIM-575](../claims.d/CLAIM-575.md) holds it a property of the four, not a fifth", and [CLAIM-591](../claims.d/CLAIM-591.md)
  states the deadlock as a disconnection under directed paths. [CLAIM-556](../claims.d/CLAIM-556.md)'s
  repair of reachability cites [CASE-207](../cases.d/CASE-207.md). [CLAIM-578](../claims.d/CLAIM-578.md): "Diagnosing which
  obstruction blocks a transition is another, with its own complexity
  ([CLAIM-575](../claims.d/CLAIM-575.md))."
- **Constraints and inputs.** [CLAIM-589](../claims.d/CLAIM-589.md)'s reliability step cites
  [CLAIM-567](../claims.d/CLAIM-567.md)'s fork; [CLAIM-582](../claims.d/CLAIM-582.md)'s reliability witness is the same fork with
  the distractor blocked. [TERM-114](../terms.d/TERM-114.md)'s "What it is not" keeps [CLAIM-582](../claims.d/CLAIM-582.md)'s
  guard. [CLAIM-567](../claims.d/CLAIM-567.md)'s body: "Where intervention is placed can matter more
  than how much ([CLAIM-562](../claims.d/CLAIM-562.md))."
- **The general object.** [CLAIM-576](../claims.d/CLAIM-576.md) cites [CLAIM-586](../claims.d/CLAIM-586.md), [CLAIM-571](../claims.d/CLAIM-571.md), [CLAIM-582](../claims.d/CLAIM-582.md),
  [CASE-198](../cases.d/CASE-198.md), [QUESTION-392](../questions.d/QUESTION-392.md) and [CLAIM-583](../claims.d/CLAIM-583.md) for its three ways. [QUESTION-392](../questions.d/QUESTION-392.md)
  names [CASE-198](../cases.d/CASE-198.md) as a case of its third kind, and its note of 2026-11-05
  cites [CLAIM-556](../claims.d/CLAIM-556.md) as one form of a classification of interventions. [CLAIM-573](../claims.d/CLAIM-573.md) is stated in
  [TERM-111](../terms.d/TERM-111.md) and names [CLAIM-556](../claims.d/CLAIM-556.md)'s obstruction profile as one structure a
  simulation would preserve; [QUESTION-385](../questions.d/QUESTION-385.md) calls [CLAIM-573](../claims.d/CLAIM-573.md) the hypothesis it
  would test. [TERM-114](../terms.d/TERM-114.md)'s "What it adds" places [CLAIM-563](../claims.d/CLAIM-563.md), [CLAIM-560](../claims.d/CLAIM-560.md),
  [CLAIM-591](../claims.d/CLAIM-591.md), [CASE-198](../cases.d/CASE-198.md) and [CASE-207](../cases.d/CASE-207.md).
- **The questions.** [QUESTION-387](../questions.d/QUESTION-387.md) is asked after [CLAIM-588](../claims.d/CLAIM-588.md)'s table.
  [QUESTION-376](../questions.d/QUESTION-376.md)'s summary: "[CLAIM-565](../claims.d/CLAIM-565.md) gives a pair with one clone and
  opposite navigation." [QUESTION-377](../questions.d/QUESTION-377.md) relates to [CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-567](../claims.d/CLAIM-567.md);
  [QUESTION-373](../questions.d/QUESTION-373.md) cites [CLAIM-571](../claims.d/CLAIM-571.md); [QUESTION-389](../questions.d/QUESTION-389.md) cites [CLAIM-567](../claims.d/CLAIM-567.md); [QUESTION-391](../questions.d/QUESTION-391.md)'s
  note of 2026-11-05 reads [CASE-207](../cases.d/CASE-207.md) and [CLAIM-586](../claims.d/CLAIM-586.md); [QUESTION-388](../questions.d/QUESTION-388.md)'s note reads
  [TERM-114](../terms.d/TERM-114.md); [QUESTION-390](../questions.d/QUESTION-390.md) cites [CASE-206](../cases.d/CASE-206.md) and [QUESTION-385](../questions.d/QUESTION-385.md); [QUESTION-404](../questions.d/QUESTION-404.md)
  cites [CLAIM-568](../claims.d/CLAIM-568.md) and [CLAIM-556](../claims.d/CLAIM-556.md).

## Links across to the sibling parts, stated

- **To budgeted individuation ([SYNTHESIS-040](SYNTHESIS-040.md)).** [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-590](../claims.d/CLAIM-590.md) rest on
  [CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-563](../claims.d/CLAIM-563.md); [CLAIM-590](../claims.d/CLAIM-590.md) grounds on [CASE-206](../cases.d/CASE-206.md) and [CLAIM-572](../claims.d/CLAIM-572.md) and
  [CLAIM-592](../claims.d/CLAIM-592.md) are illustrated by it. [CLAIM-574](../claims.d/CLAIM-574.md): "[CLAIM-564](../claims.d/CLAIM-564.md) is the same shape
  on the side of demands". [CLAIM-572](../claims.d/CLAIM-572.md) calls a reallocation between
  observing and acting "a transition with its own threshold, as in
  [CLAIM-571](../claims.d/CLAIM-571.md), but in budget space rather than configuration space".
  [TERM-116](../terms.d/TERM-116.md) prices [CLAIM-569](../claims.d/CLAIM-569.md)'s three requirements per configuration.
- **To assembly and nucleation ([SYNTHESIS-045](SYNTHESIS-045.md)).** [CLAIM-599](../claims.d/CLAIM-599.md) rests on [CLAIM-562](../claims.d/CLAIM-562.md),
  and [CASE-215](../cases.d/CASE-215.md) illustrates it. [CASE-216](../cases.d/CASE-216.md) illustrates [CLAIM-569](../claims.d/CLAIM-569.md) and [CLAIM-571](../claims.d/CLAIM-571.md);
  [CASE-217](../cases.d/CASE-217.md), [CASE-219](../cases.d/CASE-219.md) and [CASE-220](../cases.d/CASE-220.md) illustrate [CLAIM-567](../claims.d/CLAIM-567.md). [CLAIM-594](../claims.d/CLAIM-594.md)
  complements [CLAIM-569](../claims.d/CLAIM-569.md). [QUESTION-380](../questions.d/QUESTION-380.md) asks when a local face raises
  "reliable emergence and not only feasibility ([CLAIM-567](../claims.d/CLAIM-567.md))".
- **To transient-support, outside the line.** [CLAIM-601](../claims.d/CLAIM-601.md) uses [TERM-105](../terms.d/TERM-105.md), reading a savings buffer as
  a replenishable reserve.
- **To persisting individuals ([SYNTHESIS-046](SYNTHESIS-046.md)).** [CLAIM-611](../claims.d/CLAIM-611.md) rests on [CLAIM-576](../claims.d/CLAIM-576.md) and
  [CLAIM-567](../claims.d/CLAIM-567.md); [QUESTION-379](../questions.d/QUESTION-379.md) cites [CLAIM-569](../claims.d/CLAIM-569.md) and [TERM-114](../terms.d/TERM-114.md); [ARG-072](../arguments.d/ARG-072.md) names
  [CLAIM-567](../claims.d/CLAIM-567.md)'s split and [ARG-054](../arguments.d/ARG-054.md)'s difference.
- **To the line's hinge.** [CLAIM-556](../claims.d/CLAIM-556.md) rests on [CLAIM-566](../claims.d/CLAIM-566.md), and [CLAIM-567](../claims.d/CLAIM-567.md)'s
  note of 2026-11-05 reads A's synthesis on DNA origami as "this claim
  together with [CLAIM-566](../claims.d/CLAIM-566.md)".

## Not stated on the record

Links across the components that no entry states, tested by [ADR-075](../decisions.d/ADR-075.md)'s
step 5 at this review and not filed:

- **A budget as a constraint that can cost reliability.** That raising a
  budget at a fixed architecture can lower how reliably a process reaches
  a target, by admitting a distractor branch, while it cannot shrink what
  is reachable ([CLAIM-582](../claims.d/CLAIM-582.md)'s reliability witness, with [CLAIM-560](../claims.d/CLAIM-560.md)'s and
  [CLAIM-586](../claims.d/CLAIM-586.md)'s monotonicity). How a budget acts on a running process is a
  free parameter: if it aborts runs that exceed it, nothing is gained at the
  lower budget, and if it removes the unaffordable continuations, the
  sentence is [CLAIM-582](../claims.d/CLAIM-582.md)'s witness with the constraint called a budget.
- **Placement over quantity as a general law.** That where a fixed
  quantity of intervention is spent decides more than the quantity, across
  [CLAIM-562](../claims.d/CLAIM-562.md)'s actuators, [CASE-215](../cases.d/CASE-215.md)'s timing and [CLAIM-602](../claims.d/CLAIM-602.md)'s order of supply
  (transient-support).
  As "can", it is a conjunction of held instances; as a general law, it is
  against [CLAIM-571](../claims.d/CLAIM-571.md)'s and [CLAIM-586](../claims.d/CLAIM-586.md)'s budgets and the threshold on size that
  [CLAIM-600](../claims.d/CLAIM-600.md) adds to [CLAIM-602](../claims.d/CLAIM-602.md).
- **That the state space is not enough.** [CLAIM-576](../claims.d/CLAIM-576.md) draws it from
  [CLAIM-583](../claims.d/CLAIM-583.md); [CLAIM-576](../claims.d/CLAIM-576.md)'s own note of 2026-11-06 says that [CLAIM-583](../claims.d/CLAIM-583.md) does not show
  it, since with a fixed move rule the configurations and their moves
  carry reachability, and that no comparison is on file that a costed
  configuration space with its moves fails to make.

## What it does not say

- That organizations have configuration spaces with such costs; each
  claim here says its organizational reading is A's analogy or a model.
- That the four obstructions or the six levels are exhaustive ([CLAIM-568](../claims.d/CLAIM-568.md),
  [CLAIM-556](../claims.d/CLAIM-556.md); [QUESTION-404](../questions.d/QUESTION-404.md)).
- That any universality across substrates is shown ([CLAIM-573](../claims.d/CLAIM-573.md), Proposed).
- Anything with standing of its own.
