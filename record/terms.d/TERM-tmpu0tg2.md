---
status: Active
title: 'ordinal potential: of a negotiation over a finite set of options in a window of time, an ordering of the options that every move winning one of its conflicts climbs; it exists exactly when the wins never cycle, needs no comparison of pairs that were never contested, and is fixed only up to a class: every strictly increasing transform of one is one, and on a sparse record several orderings can be'
version: 1
tags:
- mathematics
- game-theory
- emotion-and-affect
date: '2026-10-23'
line: formal-apparatus
summary: >-
  The first level of the hierarchy the review of PR [#327](https://github.com/dmarx/nucleation/issues/327) proposed:
  ordinal coherence. Separated from the Hodge decomposition, which
  measures cardinal inconsistency and can reverse an ordinal comparison
  ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md), part 4), and from a real-valued currency
  ([CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md)).
refined_by:
- TERM-tmpuilar
used_by:
- CLAIM-tmp7df5r
- CLAIM-tmpz8lli
---
<!-- inactive-ok-file: TERM-tmpuilar TERM-tmp8gbrt THEORY-tmpj4ciq CLAIM-tmp85p0g — Proposed; the terms built on this one, the second-hand reading of Monderer and Shapley, and the currency result it is distinguished from, cited as open -->

# TERM-tmpu0tg2: ordinal potential: of a negotiation over a finite set of options in a window of time, an ordering of the options that every move winning one of its conflicts climbs; it exists exactly when the wins never cycle, needs no comparison of pairs that were never contested, and is fixed only up to a class: every strictly increasing transform of one is one, and on a sparse record several orderings can be

## Definition

Let a negotiation face the finite options X in a window W, and let
x → y when, in W, a move from x to y won one of its conflicts. An
**ordinal potential** of the negotiation on W is a strict ordering ≻ of
X (or any function P : X → ℝ) with y ≻ x whenever x → y.

- **Existence.** One exists exactly when no chain of wins in W returns to
  where it began; the length of the longest chain ending at x is one
  ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md), part 1). The relation of wins need only be acyclic:
  pairs never contested in W need not be compared, so completeness is not
  required. A complete, transitive relation is the special case in which
  every pair was contested.
- **Approximation.** Where the wins cycle, the negotiation's distance
  from having one is the least fraction of its wins whose reversal leaves
  them acyclic, a minimum feedback arc set; the orderings that attain it
  are its best-fitting orderings. This is ordinal throughout: it counts
  wins and reverses none of them by margin.
- **The class.** An ordinal potential is never unique. Every strictly
  increasing transform of one is one; and where pairs were not contested,
  orderings that rank those pairs differently are all potentials of the
  same record ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md), part 7). What a record fixes is the class,
  and a claim that a particular ordering is the potential is a claim that
  needs an intervention contesting the pairs that separate it from the
  others.

The term names the first of three ordered senses that "common currency"
ran together:

1. **ordinal comparability**: the negotiation has an ordinal potential;
2. **scalar currency**: the ordering has a real-valued representation,
   which a finite ordering always has and a graded lexicographic one on a
   continuum does not ([CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md), parts 1 and 2);
3. **cardinal trade-off structure**: differences in the representation
   mean something, so exchange rates between options are fixed up to an
   affine transform. Only here are margins intensities, and only here does
   the Hodge decomposition's least-squares potential measure what it says
   ([THEORY-tmp4zhyp](../theory.d/THEORY-tmp4zhyp.md)).

## What it is not

- **Not the Hodge gradient.** The gradient of the Hodge decomposition is
  a least-squares fit to margins, a cardinal object. It can rank B above A
  when A won their contest: margins A over B by 1, B over C by 10, A over
  C by 1 give scores 2/3, 3 and −11/3 ([CLAIM-tmp7df5r](../claims.d/CLAIM-tmp7df5r.md), part 4;
  scratch/formal/valence.py, case 1). Its cyclic share is positive on that
  record although the wins are transitive.
- **Not a currency.** On a finite set the two coincide at each instant;
  across instants and on continua they do not ([CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md)).
- **Not vacuous only by accident.** A negotiation with no contested
  pairs in W has an empty relation of wins, which is acyclic, so every
  ordering is trivially a potential. The term allows this; terms built on
  it, such as goal-conduciveness valence ([TERM-tmp8gbrt](TERM-tmp8gbrt.md)), must exclude it.
- **Not persistent.** A potential on each window says nothing about
  whether it is the same potential across windows. That is
  [TERM-tmpuilar](TERM-tmpuilar.md).
- **Not a potential game.** Monderer and Shapley's generalized ordinal
  potential ([THEORY-tmpj4ciq](../theory.d/THEORY-tmpj4ciq.md)) is defined over players' unilateral
  deviations; this term needs only the relation of wins.
