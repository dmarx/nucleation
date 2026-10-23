---
number: 78
status: Proposed
formerly:
- TERM-tmpuilar
title: 'persistent potential: an ordinal potential of a negotiation that is the same, up to its class, across successive windows of time, that decides the conflicts it bears on (priority), and towards which the dynamics climb again after a perturbation (resumption); exact when no move outside a perturbation descends it, and then a Lyapunov function of the one-move-at-a-time dynamics, and approximate when some do, and then no Lyapunov function, short of a drift condition that needs a cardinal potential and further assumptions'
version: 1
tags:
- emotion-and-affect
- game-theory
- mathematics
date: '2026-10-23'
line: organizational-affect
refines:
- TERM-077
summary: >-
  The second level of the hierarchy the review of PR [#327](https://github.com/dmarx/nucleation/issues/327) proposed,
  which the review called "dynamical ascendancy". Named for the potential
  rather than reviving "ascendancy", which the record retired the same day
  ([TERM-076](TERM-076.md)). It reads Frijda's three marks of control precedence
  ([THEORY-055](../theory.d/THEORY-055.md)) as properties of an ordinal potential over time.
refined_by:
- TERM-076
used_by:
- CLAIM-440
---

# TERM-078: persistent potential: an ordinal potential of a negotiation that is the same, up to its class, across successive windows of time, that decides the conflicts it bears on (priority), and towards which the dynamics climb again after a perturbation (resumption); exact when no move outside a perturbation descends it, and then a Lyapunov function of the one-move-at-a-time dynamics, and approximate when some do, and then no Lyapunov function, short of a drift condition that needs a cardinal potential and further assumptions

## Definition

Let W₁, W₂, … be successive windows of a negotiation's history, each
with its relation of wins and its class of ordinal potentials
([TERM-077](TERM-077.md)). An ordering ≿_v is a **persistent potential** over the
windows when Frijda's three marks of control precedence ([THEORY-055](../theory.d/THEORY-055.md))
hold of it:

- **Priority.** In each window, on contested pairs where ≿_v and some
  other perspective's ordering disagree, the wins follow ≿_v, up to the
  window's least reversal fraction.
- **Persistence.** ≿_v is in, or within a stated reversal fraction of,
  each window's class. A sequence of per-window potentials that are
  different orderings is not one persistent potential, however coherent
  each window is ([CLAIM-436](../claims.d/CLAIM-436.md), part 4).
- **Resumption.** After a perturbation moves the system down ≿_v, the
  one-move-at-a-time dynamics climb it again.

**Exact and approximate.** The marks admit a tolerance, and the
tolerance changes what follows.
- An **exact** persistent potential is one that no move outside a
  perturbation descends. Then ≿_v is a Lyapunov function of the
  one-move-at-a-time dynamics, non-decreasing along them, and
  resumption follows.
- An **approximate** one fits each window only up to a reversal
  fraction, so some moves descend it. It is then no Lyapunov function.
  A recurring cycle of moves A → B → C → A has a best-fitting ordering
  that misfits one move in three, yet no function is non-decreasing
  along all three moves except a constant ([CLAIM-434](../claims.d/CLAIM-434.md), part 9). The
  ordering's fit does not make the system climb it.
- What can stand in for the Lyapunov reading in the approximate case is
  a **drift condition**: the expected change of the potential along the
  dynamics is non-negative, or positive away from the top. That needs
  more than this term supplies. An expectation of changes needs a
  cardinal potential, differences that mean something, which is the
  fourth sense of currency, not the first ([TERM-077](TERM-077.md)). It also needs
  a stochastic model of the moves, Markov or stationary over the
  windows, under which the expectation is taken. Where those are not
  stated, an approximate persistent potential claims priority and
  persistence only, and resumption is read off the record as the
  ordering's return after perturbations, not inferred from a Lyapunov
  property.
- An ordinal surrogate, that moves climb the ordering more often than
  they descend it, is not a drift condition and does not by itself give
  return: frequent small climbs and rare long descents can coexist with
  no tendency to return.

The record of wins is kept per window and in sequence, never netted over
the whole history. Netting erases exactly what the term needs: a pair won
alternately by each side nets to no conflict ([CLAIM-434](../claims.d/CLAIM-434.md), part 5).
Direction, the number of contests and their variability are three
quantities, not one.

## What it is not

- **Not "ascendancy".** The review of PR [#327](https://github.com/dmarx/nucleation/issues/327) named this level
  "dynamical ascendancy". The record had retired "ascendancy" earlier the
  same day for "potential", the mathematical word ([TERM-076](TERM-076.md)), and
  this term keeps that choice; "persistent" names what is added.
- **Not an ordinal potential on the pooled record.** Pooling the windows
  can produce an acyclic record from alternating ones, or a cyclic one
  from windows each acyclic.
- **Not valence.** A persistent potential can rank anything. It becomes
  goal-conduciveness valence ([TERM-076](TERM-076.md)) only when it ranks the
  system's own states by their bearing on its maintenance, over a
  non-empty set of contested pairs.
- **Not a Lyapunov function when approximate.** See above; the
  distinction was added before merge after a second review of the pull
  request.
- **Not stable under simultaneous moves.** The Lyapunov reading needs
  winning moves one at a time; simultaneous moves can cycle even in an
  exact potential game ([CLAIM-434](../claims.d/CLAIM-434.md)).
