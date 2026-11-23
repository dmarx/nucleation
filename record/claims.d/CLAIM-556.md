---
number: 556
status: Active
formerly:
- CLAIM-tmp06538
title: 'Before the four obstructions to a transition stands a failure of compatibility, no configuration meeting the demands, repaired by changing the constraints, since dropping a demand is not relief; and after them a failure of regeneration, the capability not surviving turnover, repaired by maintenance or reproduction; so a diagnosis runs through six levels, each with its own repair'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings); interpretive, so
    listed for the owner. Its premises, CLAIM-568 (promoted in the same
    change) and CLAIM-566, are Active, no objection is on file, and its
    defeat condition already sets the failure of information aside.
    CLAIM-347 moves from complements to rests_on and CLAIM-586 joins it:
    the body uses them for the repair of compatibility, that dropping a
    demand is not relief and that no resource relieves a non-face while the
    architecture is fixed.
role: thesis
warrant: interpretive
defeated_if: >-
  A failed capability, in a declared model, that falls under none of the six
  levels and is not the failure of information this claim names as missing;
  or a class of cases in which the repair the hierarchy assigns to a failure
  of compatibility or of regeneration does not touch it while another
  level's repair does, so that the two added levels do not track what would
  repair the failure. Not defeated by failures at several levels at once,
  which the claim allows, nor by organizational settings where the
  mechanical readings do not carry over; the claim is a classification
  relative to a declared model.
tags:
- complex-systems
- control-theory
- operations-research
date: '2026-11-05'
line:
- realizability
- readiness
rests_on:
- CLAIM-568
- CLAIM-566
- CLAIM-347
- CLAIM-586
complements:
- CLAIM-575
bears_on:
- QUESTION-392
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 2 §3: a six-level
  diagnostic hierarchy, compatibility, reachability, affordability,
  controllability, reliability and regeneration, each with what repairs it.
  Four levels are [CLAIM-568](CLAIM-568.md)'s obstructions and the sixth is
  [CLAIM-566](CLAIM-566.md)'s regeneration; filed here are only the levels those lack,
  compatibility before and regeneration after, and the ordering. Two
  qualifications: by [CLAIM-347](CLAIM-347.md), dropping a demand is not relief, so the
  repair of compatibility is a change of constraints; and A's repair of
  reachability, a change of the transformation repertoire, can be had
  without a new architecture. A's further hope that the levels are
  "substrate-independent" is left to [CLAIM-573](CLAIM-573.md). The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-194 CASE-207 CLAIM-573 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-556: Before the four obstructions to a transition stands a failure of compatibility, no configuration meeting the demands, repaired by changing the constraints, since dropping a demand is not relief; and after them a failure of regeneration, the capability not surviving turnover, repaired by maintenance or reproduction; so a diagnosis runs through six levels, each with its own repair

## The claim

A's table (Response 2 §3):

| level | question | what can repair the failure |
|---|---|---|
| Compatibility | "Does a valid state exist?" | "Change constraints or demands" |
| Reachability | "Is there an admissible path?" | "Change transformation repertoire" |
| Affordability | "Does a path fit the budget?" | "Add or reallocate resources" |
| Controllability | "Can available inputs execute it?" | "Change actuation or policy" |
| Reliability | "Can it be realized robustly?" | "Improve feedback and stabilization" |
| Regeneration | "Can the capability persist through turnover?" | "Establish reproductive or maintenance mechanisms" |

**What is held.** The middle four are [CLAIM-568](CLAIM-568.md)'s geometric
disconnection, capacity bottleneck, control limitation and dynamic
instability, with the same remedies. Regeneration is the third of
[CLAIM-566](CLAIM-566.md)'s properties, that a form assembles, persists and is
regenerated after turnover, which A cites.

**What is added.**

- **Compatibility first.** Before any transition can fail, the target may
  not exist: no configuration meets the demands together, a non-face of
  [CLAIM-347](CLAIM-347.md)'s complex. It is the precondition of the other five, since a
  target reached is feasible ([CLAIM-567](CLAIM-567.md)), and no resource, input or
  feedback relieves it while the architecture is fixed ([CLAIM-586](CLAIM-586.md)).
  A's repair needs one correction: [CLAIM-347](CLAIM-347.md) holds that "dropping or
  suppressing a demand is not relief". Changing the demands changes the
  question; the repair that answers it is a change of the constraints.
- **Regeneration last.** A capability reached, affordably, under control
  and reliably, can still be lost when its carriers turn over. Its repair
  is of another kind from the other five: not a path, input or margin but a
  process that rebuilds the conditions of the capability.
- **The ordering.** Compatibility is necessary for all the rest and
  regeneration presupposes a form to regenerate. Between them the four are
  distinct and can combine, as [CLAIM-568](CLAIM-568.md) says; the table's order is a
  sequence for diagnosis, not a chain of implications.

**A's repair of reachability** differs from [CLAIM-568](CLAIM-568.md)'s, which is a
change of the constraint architecture. A's is a change of the
transformation repertoire, which can be had within one architecture:
admitting facet bending as a move in the square twist ([CASE-207](../cases.d/CASE-207.md)), at
an energy price, joins states that rigid motions do not.

## What it does not say

- **That the six are exhaustive.** Neither A's table nor [CLAIM-568](CLAIM-568.md) has
  a level for information: a path exists and the inputs could execute it,
  but the system cannot tell which state it is in or which response the
  context calls for, [CASE-194](../cases.d/CASE-194.md)'s observational cause.
- **That diagnosis is easy.** Which level a failure is at can itself be a
  hard question over a family ([CLAIM-575](CLAIM-575.md)).
- **That the levels are substrate-independent.** A: "The interesting
  possibility is that these distinctions are substrate-independent", so
  that a robot, a folding sheet, a computational agent and an institution
  "could all exhibit the same abstract obstruction profile." That is a
  hypothesis about translations between systems ([CLAIM-573](CLAIM-573.md)), not part
  of this classification.
- **That organizations have the declared models** the levels are relative
  to. The cases are mechanical; the organizational reading is A's analogy.

## Note of 2026-11-21: the synthesis review's audit

Audited at the synthesis review of 2026-11-21 ([ADR-075](../decisions.d/ADR-075.md), step 5) by a reader briefed neutrally. **Verdict: it adds nothing to its premises, and its defeater is met as written.**

- **A juxtaposition.** The defensible content is [CLAIM-567](CLAIM-567.md), [CLAIM-568](CLAIM-568.md), [CLAIM-566](CLAIM-566.md), [CLAIM-586](CLAIM-586.md) and [CLAIM-347](CLAIM-347.md) side by side. "Compatibility first" is [CLAIM-567](CLAIM-567.md). "No budget relieves a non-face" is [CLAIM-586](CLAIM-586.md). That inputs and feedback leave the target unchanged holds by definition.
- **The distinct-repair clause has a separating case.** Mordvintsev and colleagues' neural cellular automata ([THEORY-2024](../theory.d/THEORY-2024.md), noted in [CLAIM-566](CLAIM-566.md)) get persistence and regeneration from one stabilization repair. That does not meet the defeater, which needs the assigned repair not to touch the failure.
- **The defeater's first clause is met.** A capability reached reliably and then lost over a horizon with no turnover and no information failure falls under none of the six levels. Creep or fatigue of a folded structure is an example, as is [CLAIM-566](CLAIM-566.md)'s persistence failing on its own. The body says the six are not exhaustive, but the defeater makes them so. This is the misstatement [CLAIM-568](CLAIM-568.md) removed from its own defeater in version 2.
- **Two premises misstated.** "With the same remedies" misstates [CLAIM-568](CLAIM-568.md), whose disconnection remedy is also a change of the declared transformations. "Can the capability persist through turnover?" runs together [CLAIM-566](CLAIM-566.md)'s persistence and regeneration.

**What the skill would do.** Fold the mapping into its scope's account and set the claim Superseded. That is a status change on an Active entry, so it waits for the owner ([ADR-127](../decisions.d/ADR-127.md)).

**A narrower sentence the reader thought might pass by derivation**, with [CLAIM-516](CLAIM-516.md) as a further premise: "Under turnover with no basal production, no remedy for [CLAIM-568](CLAIM-568.md)'s four obstructions keeps a capability over horizons longer than turnover unless it creates a productive cycle among the capability's producers." Before filing it, check that [CLAIM-531](CLAIM-531.md) and [CLAIM-532](CLAIM-532.md) do not already hold it.

## Note of 2026-11-23: the synthesis review's audit, again

At the synthesis review of 2026-11-23 a second reader, briefed neutrally and
not told of the note above, reached the same verdict: the claim adds nothing
to [CLAIM-568](CLAIM-568.md), [CLAIM-566](CLAIM-566.md), [CLAIM-347](CLAIM-347.md) and [CLAIM-586](CLAIM-586.md) set side by side, and the
first clause of its `defeated_if` is met by a capability lost over a horizon
with no turnover and no failure of information, such as creep or fatigue of
a folded structure. The recommendation stands: fold the mapping into the
realizability and readiness accounts and set the claim Superseded, and, if it
is kept, drop the defeater's exhaustiveness. Both wait for the owner.
