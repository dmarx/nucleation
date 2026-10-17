---
number: 689
status: Active
formerly:
- THEORY-tmpytg92
title: "A mobile robot built from parallel layers of simple finite-state machines, each linking sensing to action by itself and combined only by one layer suppressing or inhibiting another's signals, avoids obstacles, wanders and heads for distant places with no central world model, goal list or controller; shown at insect scale, on three layers of one physical robot"
version: 1
tags:
- behavioral-integration
- agency
date: '2026-10-16'
source:
- LIT-436
summary: >-
  Brooks (1991, written 1987), [LIT-436](../literature.d/LIT-436.md), read in [NOTE-351](../notes.d/NOTE-351.md). An existence
  proof by construction: the absence of central representation and
  control is true of the architecture by design, and the robot ran "for
  well over a year". The evidence is described, not measured; three
  layers ran on a robot and six in simulation. The claims that coherence
  exists only "in the eye of an observer", that representation is the
  wrong unit for most of intelligence, and that the method scales are
  assertion or labelled hypothesis.
supports:
- CLAIM-045
---
<!-- inactive-ok-file: THEORY-043 THEORY-056 — Proposed; related or rival accounts named in Connections, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-429 — Unavailable; a related work named by the reading, not leaned on for its content -->

# THEORY-689: A mobile robot built from parallel layers of simple finite-state machines, each linking sensing to action by itself and combined only by one layer suppressing or inhibiting another's signals, avoids obstacles, wanders and heads for distant places with no central world model, goal list or controller; shown at insect scale, on three layers of one physical robot

## Source

Brooks (1991), "Intelligence without representation", [LIT-436](../literature.d/LIT-436.md)
(*Artificial Intelligence* 47:139–159, written in 1987), read in full in
[NOTE-351](../notes.d/NOTE-351.md) from the copy Brooks posts.

## What was actually shown

**The architecture (§6.2).** Each layer is a fixed network of finite-state
machines with "a handful of states, one or two internal registers, one or
two internal timers", passing 1-bit or 24-bit messages. A higher layer
subsumes a lower one by suppression (a new wire replaces an input for a set
time) or inhibition (a new wire blocks an output for a set time). There are
no variables, no rule matching and no shared data.

**The robot.** On Allen, three layers: avoid (twelve sonars, collide,
feelforce, runaway, turn, forward); wander (a random heading every ten
seconds or so, summed with repulsion); explore (look, stereo, path-plan,
steering around the obstacles the lower layer avoids). The robots ran "for
well over a year". Six layers ran in simulation.

**What follows by construction (§5).** "Not by design, but rather by
observation", there is no central representation. Each layer has "its own
implicit purpose (or goal if you insist)", checked continuously against the
world, and "there need be no explicit representation of goals that some
central (or distributed) process selects from". "Just as there is no central
representation there is not even a central system" (§5.1). Low layers react
fast because they keep no representations, and a change in the world
disables some layers, not all.

What could have come out otherwise: the layered robot could have failed to
behave purposively in a real, unsimplified environment, or needed an
arbiter. As described, it did neither, at three layers.

## What this does not say

- **That intelligence in general needs no representation.** That is the
  paper's labelled hypothesis (H), supported by the robots and an
  evolutionary timeline. The timeline does not show that reasoning is
  "pretty simple" once mobility is solved.
- **That there are no representations in the robot.** Brooks declines the
  word because the system has no variables, rule matching or choice. He
  concedes that "an extremist might say that we really do have
  representations, but that they are just implicit". The claim is about
  explicit, central, symbolic representation.
- **That the robot's unity is only in the observer.** Brooks says coherence
  emerges "in the eye of an observer". That is an interpretive assertion,
  not a result. Whether the whole is a real agent is not argued against.
- **That it scales.** How many layers before their interactions become too
  complex, how complex the behaviours can be, and whether learning is
  possible are posed in §8 and not answered. The fourteen-layer robot is a
  plan, and learning works only "as an isolated subsystem".
- **That performance was measured.** It is described, never measured or
  compared. "The most reactive real-time mobile robots in existence" is the
  author's report.
- **Anything about minds or experience.** "I have no particular interest in
  demonstrating how human beings work", and "no biological significance" is
  claimed.

## Connections

- Minsky's society of mind ([LIT-429](../literature.d/LIT-429.md)) gives, in Brooks's words, "a similar
  account of how human behavior is generated". Minsky's agents carry memory
  and representational machinery; Brooks's layers pass uninterpreted
  numbers. This is the more austere decomposition, built.
- [THEORY-043](THEORY-043.md) treats a mind of mindless agents as one direction of a single
  functionalist move. This is the mindless direction realised in hardware.
- Goal-directedness without self-representation: Schwitzgebel ([LIT-159](../literature.d/LIT-159.md))
  counts goal-directed responsiveness, self-monitoring and
  self-representation among the marks of a possible group mind. These
  robots have the first and none of the others, so the marks come apart
  ([NOTE-351](../notes.d/NOTE-351.md)).
- [CLAIM-045](../claims.d/CLAIM-045.md) assigns Brooks the sub-question of how coherent behaviour
  arises without a central executive. This is the result it relies on.
- [THEORY-056](THEORY-056.md) holds that emotion regulation is one motive state checking
  another, with no regulating system above them, and cites this
  architecture as that structure built.
