---
status: Proposed
title: 'persistent potential: an ordinal potential of a negotiation that is the same, up to its class, across successive windows of time, that decides the conflicts it bears on (priority), and towards which the dynamics climb again after a perturbation (resumption), serving as a Lyapunov function of the one-move-at-a-time dynamics'
version: 1
tags:
- emotion-and-affect
- game-theory
- mathematics
date: '2026-10-23'
line: organizational-affect
refines:
- TERM-tmpu0tg2
summary: >-
  The second level of the hierarchy the review of PR [#327](https://github.com/dmarx/nucleation/issues/327) proposed,
  which the review called "dynamical ascendancy". Named for the potential
  rather than reviving "ascendancy", which the record retired the same day
  ([TERM-tmp8gbrt](TERM-tmp8gbrt.md)). It reads Frijda's three marks of control precedence
  ([THEORY-055](../theory.d/THEORY-055.md)) as properties of an ordinal potential over time.
refined_by:
- TERM-tmp8gbrt
used_by:
- CLAIM-tmpz8lli
---

# TERM-tmpuilar: persistent potential: an ordinal potential of a negotiation that is the same, up to its class, across successive windows of time, that decides the conflicts it bears on (priority), and towards which the dynamics climb again after a perturbation (resumption), serving as a Lyapunov function of the one-move-at-a-time dynamics

## Definition

Let W₁, W₂, … be successive windows of a negotiation's history, each
with its relation of wins and its class of ordinal potentials
([TERM-tmpu0tg2](TERM-tmpu0tg2.md)). An ordering ≿_v is a **persistent potential** over the
windows when Frijda's three marks of control precedence ([THEORY-055](../theory.d/THEORY-055.md))
hold of it:

- **Priority.** In each window, on contested pairs where ≿_v and some
  other perspective's ordering disagree, the wins follow ≿_v, up to the
  window's least reversal fraction.
- **Persistence.** ≿_v is in, or within a stated reversal fraction of,
  each window's class. A sequence of per-window potentials that are
  different orderings is not one persistent potential, however coherent
  each window is ([CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md), part 4).
- **Resumption.** After a perturbation moves the system down ≿_v, the
  one-move-at-a-time dynamics climb it again: ≿_v is a Lyapunov function
  of those dynamics, non-decreasing along them outside perturbations.

The record of wins is kept per window and in sequence, never netted over
the whole history. Netting erases exactly what the term needs: a pair won
alternately by each side nets to no conflict ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md), part 5).
Direction, the number of contests and their variability are three
quantities, not one.

## What it is not

- **Not "ascendancy".** The review of PR [#327](https://github.com/dmarx/nucleation/issues/327) named this level
  "dynamical ascendancy". The record had retired "ascendancy" earlier the
  same day for "potential", the mathematical word ([TERM-tmp8gbrt](TERM-tmp8gbrt.md)), and
  this term keeps that choice; "persistent" names what is added.
- **Not an ordinal potential on the pooled record.** Pooling the windows
  can produce an acyclic record from alternating ones, or a cyclic one
  from windows each acyclic.
- **Not valence.** A persistent potential can rank anything. It becomes
  goal-conduciveness valence ([TERM-tmp8gbrt](TERM-tmp8gbrt.md)) only when it ranks the
  system's own states by their bearing on its maintenance, over a
  non-empty set of contested pairs.
- **Not stable under simultaneous moves.** The Lyapunov reading needs
  winning moves one at a time; simultaneous moves can cycle even in an
  exact potential game ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md)).
