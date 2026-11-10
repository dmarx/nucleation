---
number: 568
status: Active
formerly:
- CLAIM-tmpal9mc
title: 'A transition can fail in four ways that call for different remedies: a feasible path exceeds a resource ceiling, no path exists in the fixed configuration space, a path exists that no available input can execute, or a path exists that cannot be reliably followed; added actuation can overcome an energy barrier and cannot join disconnected configurations'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings); interpretive, so
    listed for the owner. THEORY-1423, THEORY-1417, THEORY-1427 and
    THEORY-1383 move from grounds to corroborated_by (ADR-058): the body
    cites each as one mechanical case of an obstruction, and the argued
    core, that more resource meets a finite threshold and none meets an
    infinite one, is CLAIM-571's, now in rests_on. The defeat condition's
    first clause, "A failed transition, in a declared model, that falls
    under none of the four", made the four exhaustive, which the body
    disclaims; it is removed as a mis-statement (ADR-047 kind 3), and
    whether a failure of information is a fifth obstruction, as CASE-194's
    observational arm and CLAIM-556 suggest, goes to QUESTION-404
    (ADR-047 kind 4). The body now says that paths are directed where moves
    are one-way, so a deadlock (CLAIM-591) is a disconnection. No objection
    is on file.
role: thesis
warrant: interpretive
defeated_if: >-
  A class of cases, in a declared model, in which the remedy the
  classification assigns to an obstruction does not touch it while another
  class's remedy does, so that the classification does not track what would
  repair the failure. Not defeated by a failed transition that falls under
  none of the four, since the claim does not say they are exhaustive; nor by
  failures that combine several obstructions at once, which the claim
  allows; nor by organizational settings where the mechanical reading
  fails. The claim is a classification of obstructions to a transition,
  relative to a declared model.
tags:
- complex-systems
- control-theory
- mathematics
date: '2026-11-05'
line:
- realizability
- readiness
rests_on:
- CLAIM-571
complements:
- CLAIM-567
- CLAIM-586
- CLAIM-575
- CLAIM-591
bears_on:
- QUESTION-392
- QUESTION-404
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Parts 3 and 4: a
  table of four obstructions with their remedies (capacity bottleneck,
  geometric disconnection, control limitation, dynamic instability), and
  three transition mechanisms (energetic, kinematic, singular) that
  "should not be conflated". Filed as one claim, since the second is the
  first seen from the configuration space. The four refine the gaps
  between [CLAIM-567](CLAIM-567.md)'s feasible, reachable and reliable, and the
  readings give one mechanical case of each: Zang et al. an energetic
  barrier that prestress moves, Berry et al. a disconnection, Chen and
  Santangelo a singular branch point, Obayashi et al. a thin basin.
  Interpretive: the classification is argued, not proved exhaustive. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-205 THEORY-1383 — Proposed; A's proposals of 2026-11-04, the entries filed beside them and the readings' accounts, cited as filed -->

# CLAIM-568: A transition can fail in four ways that call for different remedies: a feasible path exceeds a resource ceiling, no path exists in the fixed configuration space, a path exists that no available input can execute, or a path exists that cannot be reliably followed; added actuation can overcome an energy barrier and cannot join disconnected configurations

## The claim

**A's table (Part 4).**

| obstruction | what fails | remedy |
|---|---|---|
| Capacity bottleneck | "A feasible path exceeds a resource ceiling" | "Increase or reallocate resources" |
| Geometric disconnection | "No path exists within the fixed configuration space" | "Change the constraint architecture" |
| Control limitation | "A path exists, but no available input can execute it" | "Add or rearrange actuation, change policy" |
| Dynamic instability | "A path exists but cannot be reliably followed" | "Add feedback, stabilization, robustness margins" |

**A's three mechanisms (Part 3).** "Some transitions are energetic: a
system must cross a barrier. Others are kinematic: a pathway does not
exist under the current constraints. And others are singular: a pathway
exists, but only through a special configuration at which the ordinary
local description changes. Those mechanisms should not be conflated."

**Where they sit.** [CLAIM-567](CLAIM-567.md) separates a feasible target, a
reachable one and a reliably reached one. The four obstructions say why
each step can fail:

- **Feasible, not reachable at all**: geometric disconnection, the
  kinematic case. Berry, Lee-Trimble and Santangelo ([NOTE-1605](../notes.d/NOTE-1605.md);
  [THEORY-1423](../theory.d/THEORY-1423.md)): for a positively curved vertex "the two nappes have
  split into two disconnected components". No resource reaches across;
  only a change of the declared transformations does. Paths here are the
  admissible paths of the declared transformations, directed where moves
  are one-way, so a deadlock, a state that shares a component with its
  target and has no directed path to it ([CLAIM-591](CLAIM-591.md)), is a disconnection
  of this kind.
- **Reachable, not within the ceiling**: the capacity bottleneck, the
  energetic case. The bottleneck budget of [CLAIM-571](CLAIM-571.md) is finite and
  above what is available. Zang, Zhao, Misseroni and Paulino
  ([NOTE-1569](../notes.d/NOTE-1569.md); [THEORY-1417](../theory.d/THEORY-1417.md)): prestress "enables the eight
  previously infeasible folding paths of Fig. 4C to be achieved as
  feasible folding paths in Fig. 5B", while "sixteen out of fifty-six
  folding paths are unachievable without transiting through other stable
  states". Moving the barriers opened the eight and not the sixteen.
- **Reachable, not by the inputs available**: control limitation.
  [CASE-205](../cases.d/CASE-205.md)'s step profile is admissible and outside what three
  grouped actuators can command.
- **Reachable, not reliably**: dynamic instability. Obayashi, Aoi,
  Tsuchiya and Kokubu ([NOTE-1586](../notes.d/NOTE-1586.md); [THEORY-1383](../theory.d/THEORY-1383.md)): the passive
  walker's gait exists and "The basin of attraction is very small and
  thin, and it has a fractal-like shape".

**The singular case** sits across the last two. A path exists, through a
point where several branches meet, and which one the system leaves on is
not fixed by the local description. Chen and Santangelo ([NOTE-1614](../notes.d/NOTE-1614.md);
[THEORY-1427](../theory.d/THEORY-1427.md)): "once an origami structure begins folding along the
wrong branch, it is potentially very difficult to return it to the
desired branch". It is an obstruction to reliability that more actuation,
placed to select the branch, can relieve.

**Why it matters.** A: "an energy barrier that is too high for the
current actuators is not the same thing as topological disconnection.
Increasing available actuation or modifying prestress may overcome the
former without changing the latter." Each remedy acts on one thing:
resources on the ceiling, architecture on the configuration space,
actuation on the inputs, feedback on the basin. Applied to the wrong
obstruction it buys nothing. A: "This distinction helps avoid labeling
every difficult organizational transition a bifurcation or a topological
obstruction." [CLAIM-586](CLAIM-586.md) makes the same split for joint demands
rather than paths: a budget enlarges the complex up to the unbudgeted
one and no further.

## What it does not say

- **That the four are exhaustive.** They are A's, and they cover the
  readings the record holds; a failure from missing information, where a
  path exists and the system cannot tell which one it is on, fits
  uneasily under control limitation.
- **That an obstruction is one kind.** A transition can be over budget
  and unstable at once; the claim is that the kinds are distinct, not
  that they come singly.
- **That the remedies are cheap or available.** Changing an architecture
  may be the dearest move there is.
- **That organizations have configuration spaces** in which these can be
  located. The mapping is A's analogy; the cases are mechanical.

## Note of 2026-11-05: the resource-bounded realizability readings

The pasted synthesis on resource-bounded realizability, and the readings and entries filed from it, bear on the classification. [CLAIM-556](CLAIM-556.md) extends it at both ends, with a failure of compatibility before the four and of regeneration after them. Telling which obstruction holds can itself be hard over families of problems. In Eppstein's flaps and flips ([NOTE-1611](../notes.d/NOTE-1611.md)) whether any path joins two valid states is PSPACE-complete; in Ito et al. ([NOTE-1595](../notes.d/NOTE-1595.md)) reconfiguration within a threshold is PSPACE-complete for many problems, and computing the least worst intermediate cost is strongly NP-hard or inapproximable in some. Both readers asked whether diagnosis is a fifth mode; [CLAIM-575](CLAIM-575.md) holds it a property of the four, not a fifth.

The reading of Raussen ([NOTE-1581](../notes.d/NOTE-1581.md)) asks the claim to say whether its paths are directed. A deadlock lies in a connected state space with no directed path out of it: a mode the claim misses if "no path" means undirected connectivity, covered if it means directed paths. [CLAIM-591](CLAIM-591.md) states the point. The same reader notes that raising a capacity shrinks the forbidden region and can remove a deadlock, so there a capacity bottleneck and a disconnection meet; that is the reader's reading of the model. No status changes.
