---
number: 661
status: Active
formerly:
- THEORY-tmpx1n2e
title: "In a nearly decomposable system, where interactions within subsystems are much stronger than interactions between them, each subsystem's short-run behaviour is approximately independent of the others', and in the long run each depends on the others only through their aggregate behaviour; so a hierarchy defined by intensity of interaction separates fast dynamics inside its parts from slow, aggregate dynamics between them"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    The Source section said the record does not hold Simon & Ando (1961).
    It has held it, unread, as LIT-1127 since 2026-10-16; corrected. A
    connection is added for the exchange of 2026-10-19 on coarse-to-fine
    processes: the closure of block aggregates stated here is not bounded,
    and closure does not need a block (CLAIM-388, QUESTION-221).
    The account is unchanged.
- version: 3
  date: '2026-10-20'
  note: >-
    The readings of 2026-10-20. Simon & Ando (LIT-1127) is Unavailable;
    the nearest open statement of the theorem, Shpak, Stadler, Wagner and
    Altenberg (LIT-1241, NOTE-977), joins the Source section. It
    gives no rate in ε, so "to order ε" is withdrawn. Connections gain the
    bounds of CLAIM-390 and CLAIM-386 and the contrast with scale
    locality (THEORY-754). The account is unchanged.
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
<!-- inactive-ok-file: LIT-1127 LIT-1242 — Deferred; works registered unread, cited as open, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-194 CLAIM-331 THEORY-257 THEORY-265 — Proposed; claims that rest on this result and neighbouring accounts, named for context -->
<!-- inactive-ok-file: CLAIM-173 — Rejected; the objection named for what the theorem does not settle -->

# THEORY-661: In a nearly decomposable system, where interactions within subsystems are much stronger than interactions between them, each subsystem's short-run behaviour is approximately independent of the others', and in the long run each depends on the others only through their aggregate behaviour; so a hierarchy defined by intensity of interaction separates fast dynamics inside its parts from slow, aggregate dynamics between them

## Source

Simon (1962), [LIT-905](../literature.d/LIT-905.md), "The Architecture of Complexity", *Proceedings of
the American Philosophical Society* 106(6):467–482, read in full in
[NOTE-704](../notes.d/NOTE-704.md). The theorem is Simon & Ando (1961), which the lecture cites and
the record could not obtain ([LIT-1127](../literature.d/LIT-1127.md), Unavailable). The nearest open statement
of it is Shpak, Stadler, Wagner and Altenberg (2004), [LIT-1241](../literature.d/LIT-1241.md), read in
[NOTE-977](../notes.d/NOTE-977.md): Theorems 2.1–2.2 there give the eigenprojector convergence
and the four time windows as existence statements, with no rate in ε and
no error term on the aggregate.

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
one for ε small enough. The open statement the record holds gives no rate
in ε ([NOTE-977](../notes.d/NOTE-977.md)), so this entry does not claim one.

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
  The record has no bound of the one by the other ([QUESTION-221](../questions.d/QUESTION-221.md)),
  and the converse fails: a collective variable can be exactly closed
  while no grouping of the units is a block ([CLAIM-388](../claims.d/CLAIM-388.md)). Shpak et al.
  ([LIT-1242](../literature.d/LIT-1242.md), unread) separate aggregation from decomposition in
  Simon and Ando's setting.
- **Modular synchronisation ([THEORY-265](THEORY-265.md))** is a model of the same shape:
  coupling strong inside modules makes each module respond as a unit.
- **Coupling is not constitution ([CLAIM-173](../claims.d/CLAIM-173.md), [CLAIM-194](../claims.d/CLAIM-194.md)).** A block can be
  strongly coupled because one side drives the other, or because a
  boundary was imposed on it. The theorem is silent on both.
- **Bounds the record has derived (2026-10-20).** For a block's full state
  in a linear Gaussian VAR(1), dynamical dependence is of second order in
  the coupling into the block ([CLAIM-390](../claims.d/CLAIM-390.md)). For a block's aggregate,
  the one-step closure defect splits exactly into a first-order part from
  coupling between blocks and a part from the blocks' own dynamics, which
  vanishes iff each block has equal column sums ([CLAIM-386](../claims.d/CLAIM-386.md)).
- **Nearly decomposable is a spectral condition.** [NOTE-977](../notes.d/NOTE-977.md)'s flat
  landscape has entrywise weak coupling between blocks at every mutation
  rate and no fast–slow separation at any. Read entrywise, the hypothesis
  is not sufficient.
- **Scale locality is a different pattern** ([THEORY-754](THEORY-754.md)). In a
  turbulent cascade, coupling between scales falls off as a power of their
  ratio with no gap, and the whole flux crosses every scale. It is banded,
  not block-diagonal, so this theorem does not apply to it.
