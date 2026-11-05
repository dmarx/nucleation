---
status: Proposed
title: 'A transition can fail in four ways that call for different remedies: a feasible path exceeds a resource ceiling, no path exists in the fixed configuration space, a path exists that no available input can execute, or a path exists that cannot be reliably followed; added actuation can overcome an energy barrier and cannot join disconnected configurations'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A failed transition, in a declared model, that falls under none of the
  four; or a class of cases in which the remedy the classification assigns
  to an obstruction does not touch it while another class's remedy does,
  so that the classification does not track what would repair the
  failure. Not defeated by failures that combine several obstructions at
  once, which the claim allows, nor by organizational settings where the
  mechanical reading fails; the claim is a classification of obstructions
  to a transition, relative to a declared model.
tags:
- complex-systems
- control-theory
- mathematics
date: '2026-11-05'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-tmps6lqg
- THEORY-tmppn4nt
- THEORY-tmpucnpz
- THEORY-tmpabuss
complements:
- CLAIM-tmp9jvpb
- CLAIM-tmpuxuo4
bears_on:
- QUESTION-tmpt9dhv
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Parts 3 and 4: a
  table of four obstructions with their remedies (capacity bottleneck,
  geometric disconnection, control limitation, dynamic instability), and
  three transition mechanisms (energetic, kinematic, singular) that
  "should not be conflated". Filed as one claim, since the second is the
  first seen from the configuration space. The four refine the gaps
  between [CLAIM-tmp9jvpb](CLAIM-tmp9jvpb.md)'s feasible, reachable and reliable, and the
  readings give one mechanical case of each: Zang et al. an energetic
  barrier that prestress moves, Berry et al. a disconnection, Chen and
  Santangelo a singular branch point, Obayashi et al. a thin basin.
  Interpretive: the classification is argued, not proved exhaustive. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp9jvpb CLAIM-tmpuxuo4 CLAIM-tmpbi4ca CASE-tmpe3itu THEORY-tmps6lqg THEORY-tmppn4nt THEORY-tmpucnpz THEORY-tmpabuss — Proposed; A's proposals of 2026-11-04, the entries filed beside them and the readings' accounts, cited as filed -->
<!-- inactive-ok-file: CLAIM-tmp06538 CLAIM-tmphme89 NOTE-tmpdizof CLAIM-tmpy685m — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-tmpal9mc: A transition can fail in four ways that call for different remedies: a feasible path exceeds a resource ceiling, no path exists in the fixed configuration space, a path exists that no available input can execute, or a path exists that cannot be reliably followed; added actuation can overcome an energy barrier and cannot join disconnected configurations

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

**Where they sit.** [CLAIM-tmp9jvpb](CLAIM-tmp9jvpb.md) separates a feasible target, a
reachable one and a reliably reached one. The four obstructions say why
each step can fail:

- **Feasible, not reachable at all**: geometric disconnection, the
  kinematic case. Berry, Lee-Trimble and Santangelo ([NOTE-tmpt066u](../notes.d/NOTE-tmpt066u.md);
  [THEORY-tmps6lqg](../theory.d/THEORY-tmps6lqg.md)): for a positively curved vertex "the two nappes have
  split into two disconnected components". No resource reaches across;
  only a change of the declared transformations does.
- **Reachable, not within the ceiling**: the capacity bottleneck, the
  energetic case. The bottleneck budget of [CLAIM-tmpbi4ca](CLAIM-tmpbi4ca.md) is finite and
  above what is available. Zang, Zhao, Misseroni and Paulino
  ([NOTE-tmp7wdij](../notes.d/NOTE-tmp7wdij.md); [THEORY-tmppn4nt](../theory.d/THEORY-tmppn4nt.md)): prestress "enables the eight
  previously infeasible folding paths of Fig. 4C to be achieved as
  feasible folding paths in Fig. 5B", while "sixteen out of fifty-six
  folding paths are unachievable without transiting through other stable
  states". Moving the barriers opened the eight and not the sixteen.
- **Reachable, not by the inputs available**: control limitation.
  [CASE-tmpe3itu](../cases.d/CASE-tmpe3itu.md)'s step profile is admissible and outside what three
  grouped actuators can command.
- **Reachable, not reliably**: dynamic instability. Obayashi, Aoi,
  Tsuchiya and Kokubu ([NOTE-tmpescek](../notes.d/NOTE-tmpescek.md); [THEORY-tmpabuss](../theory.d/THEORY-tmpabuss.md)): the passive
  walker's gait exists and "The basin of attraction is very small and
  thin, and it has a fractal-like shape".

**The singular case** sits across the last two. A path exists, through a
point where several branches meet, and which one the system leaves on is
not fixed by the local description. Chen and Santangelo ([NOTE-tmpwpp63](../notes.d/NOTE-tmpwpp63.md);
[THEORY-tmpucnpz](../theory.d/THEORY-tmpucnpz.md)): "once an origami structure begins folding along the
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
obstruction." [CLAIM-tmpuxuo4](CLAIM-tmpuxuo4.md) makes the same split for joint demands
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

The pasted synthesis on resource-bounded realizability, and the readings and entries filed from it, bear on the classification. CLAIM-tmp06538 extends it at both ends, with a failure of compatibility before the four and of regeneration after them. Telling which obstruction holds can itself be hard over families of problems. In Eppstein's flaps and flips (NOTE-tmpv7lp6) whether any path joins two valid states is PSPACE-complete; in Ito et al. (NOTE-tmpmqj4b) reconfiguration within a threshold is PSPACE-complete for many problems, and computing the least worst intermediate cost is strongly NP-hard or inapproximable in some. Both readers asked whether diagnosis is a fifth mode; CLAIM-tmphme89 holds it a property of the four, not a fifth.

The reading of Raussen (NOTE-tmpdizof) asks the claim to say whether its paths are directed. A deadlock lies in a connected state space with no directed path out of it: a mode the claim misses if "no path" means undirected connectivity, covered if it means directed paths. CLAIM-tmpy685m states the point. The same reader notes that raising a capacity shrinks the forbidden region and can remove a deadlock, so there a capacity bottleneck and a disconnection meet; that is the reader's reading of the model. No status changes.
