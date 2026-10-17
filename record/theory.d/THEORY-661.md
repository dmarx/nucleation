---
number: 661
status: Active
formerly:
- THEORY-tmpx1n2e
title: "In a nearly decomposable system, where interactions within subsystems are much stronger than interactions between them, each subsystem's short-run behaviour is approximately independent of the others', and in the long run each depends on the others only through their aggregate behaviour; so a hierarchy defined by intensity of interaction separates fast dynamics inside its parts from slow, aggregate dynamics between them"
version: 1
tags:
- complex-systems
date: '2026-10-16'
source:
- LIT-905
summary: >-
  Simon (1962), [LIT-905](../literature.d/LIT-905.md), read in full in [NOTE-704](../notes.d/NOTE-704.md). The two propositions
  are a theorem of Simon & Ando (1961), cited and not reproduced, and
  established since. Simon widens hierarchy to any nesting of interrelated
  subsystems, with or without authority, identified by who interacts with
  whom. His claims that social systems are prominently nearly decomposable,
  and that higher organisational levels run slower, are assertion and
  "probably true". The watchmaker argument is a model whose numbers he
  says not to take seriously.
supports:
- CLAIM-157
- CLAIM-331
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-194 CLAIM-331 THEORY-257 THEORY-265 — Proposed; claims that rest on this result and neighbouring accounts, named for context -->
<!-- inactive-ok-file: CLAIM-173 — Rejected; the objection named for what the theorem does not settle -->

# THEORY-661: In a nearly decomposable system, where interactions within subsystems are much stronger than interactions between them, each subsystem's short-run behaviour is approximately independent of the others', and in the long run each depends on the others only through their aggregate behaviour; so a hierarchy defined by intensity of interaction separates fast dynamics inside its parts from slow, aggregate dynamics between them

## Source

Simon (1962), [LIT-905](../literature.d/LIT-905.md), "The Architecture of Complexity", *Proceedings of
the American Philosophical Society* 106(6):467–482, read in full in
[NOTE-704](../notes.d/NOTE-704.md). The theorem is Simon & Ando (1961), which the lecture cites and
the record does not hold.

## What was actually shown

**The propositions.** "(a) in a nearly decomposable system, the short-run
behavior of each of the component subsystems is approximately independent
of the short-run behavior of the other components; (b) in the long run,
the behavior of any one of the components depends in only an aggregate
way on the behavior of the other components." Formally, the matrix of
interaction coefficients is block-diagonal with off-diagonal entries below
a small ε.

**The worked example.** A building of rooms divided into cubicles. Within
hours each room equalises its temperature; over days the building does.
"After the intraroom short-run equilibria have been reached, a single
thermometer in each room will be adequate".

**Hierarchy by interaction.** Simon defines a hierarchy as a system of
interrelated subsystems, each hierarchic in turn down to some elementary
level, and includes systems "in which there is no relation of
subordination among subsystems". Spatial and social hierarchies are
reconciled "by defining hierarchy in terms of intensity of interaction":
nerve cells and telephone wires "permit very specific strong interactions
at great distances".

**Description.** Near decomposability is one reason hierarchic systems can
be described briefly: "most things are only weakly connected with most
other things".

**What could have come out otherwise.** Weak coupling between blocks
could have left no separation of time scales. The theorem says it leaves
one, to order ε.

## What this does not say

- **That complex systems are in fact nearly decomposable.** That is
  Simon's empirical generalisation across examples, with no count. He
  allows that complex systems that are not hierarchic "may to a
  considerable extent escape our observation", and leaves open which way
  that dependence runs.
- **That social systems are.** "Near decomposability is generally very
  prominent" in social systems is asserted from formal organisations and
  channels of communication.
- **That higher levels of an organisation are slower.** "It is probably
  true" that higher-frequency dynamics belong to subsystems; that
  executives' horizons lengthen with rank is "generally believed". No data.
- **How fast hierarchies evolve.** The watchmaker parable (Hora against
  Tempus, about 4,000 times slower) shows that the time to assemble a
  complex form "depends critically on the numbers and distribution of
  potential intermediate stable forms". Simon calls its assumptions "not
  particularly realistic" and says the number cannot be taken seriously.
- **Where a block's boundary is.** The theorem takes the partition as given.
  Choosing it, and how small ε must be, are separate questions.

## Connections

- **The record's own argument.** [CLAIM-157](../claims.d/CLAIM-157.md) holds that a combined form is
  one system while its joint dynamics are nearly decomposable with the
  form as a block whose gap beats the Occam factor; this is the result it
  relies on for "nearly decomposable". [CLAIM-331](../claims.d/CLAIM-331.md) holds that higher-level
  variables are characteristically slower than their constituents; this
  supplies the fast-inside, slow-aggregate-outside half, and does not
  supply Simon's unsupported claim about organisations. [CLAIM-154](../claims.d/CLAIM-154.md) prices
  the block.
- **Dynamical independence ([THEORY-257](THEORY-257.md))** asks when a coarse variable is
  closed given its own history. Near decomposability gives approximate
  closure of block aggregates over the long run, by coupling strength.
- **Modular synchronisation ([THEORY-265](THEORY-265.md))** is a model of the same shape:
  coupling strong inside modules makes each module respond as a unit.
- **Coupling is not constitution ([CLAIM-173](../claims.d/CLAIM-173.md), [CLAIM-194](../claims.d/CLAIM-194.md)).** A block can be
  strongly coupled because one side drives the other, or because a
  boundary was imposed on it. The theorem is silent on both.
