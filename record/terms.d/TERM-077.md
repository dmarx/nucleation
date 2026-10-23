---
number: 77
status: Active
formerly:
- TERM-tmpu0tg2
title: 'ordinal potential: of a negotiation over a finite set of options in a window of time, an ordering of the options that every move winning one of its conflicts climbs; it exists exactly when the wins never cycle, which is ordinal extendibility, that some complete ordering agrees with every win, and not observed comparability, since pairs never contested are not compared; and it is fixed only up to a class: every strictly increasing transform of one is one, and on a sparse record several orderings can be'
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
  ([CLAIM-434](../claims.d/CLAIM-434.md), part 4), and from a real-valued currency
  ([CLAIM-436](../claims.d/CLAIM-436.md)).
refined_by:
- TERM-078
used_by:
- CLAIM-434
- CLAIM-440
---
<!-- inactive-ok-file: TERM-078 TERM-076 THEORY-896 CLAIM-436 — Proposed; the terms built on this one, the second-hand reading of Monderer and Shapley, and the currency result it is distinguished from, cited as open -->

# TERM-077: ordinal potential: of a negotiation over a finite set of options in a window of time, an ordering of the options that every move winning one of its conflicts climbs; it exists exactly when the wins never cycle, which is ordinal extendibility, that some complete ordering agrees with every win, and not observed comparability, since pairs never contested are not compared; and it is fixed only up to a class: every strictly increasing transform of one is one, and on a sparse record several orderings can be

## Definition

Let a negotiation face the finite options X in a window W, and let
x → y when, in W, a move from x to y won one of its conflicts. An
**ordinal potential** of the negotiation on W is a strict ordering ≻ of
X (or any function P : X → ℝ) with y ≻ x whenever x → y.

- **Existence.** One exists exactly when no chain of wins in W returns to
  where it began; the length of the longest chain ending at x is one
  ([CLAIM-434](../claims.d/CLAIM-434.md), part 1). The relation of wins need only be acyclic:
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
  same record ([CLAIM-434](../claims.d/CLAIM-434.md), part 7). What a record fixes is the class,
  and a claim that a particular ordering is the potential is a claim that
  needs an intervention contesting the pairs that separate it from the
  others.

The term names the first of four ordered senses that "common currency"
ran together:

1. **ordinal extendibility**: the negotiation has an ordinal potential,
   so some complete ordering agrees with every win (on a finite set, an
   acyclic relation extends to a linear order: Szpilrajn's theorem in its
   finite form, which part 1 of [CLAIM-434](../claims.d/CLAIM-434.md) constructs). It establishes
   that a shared ordering *could* account for the record, not that the
   record contains one. If the only win is A over B, three complete
   orderings fit and C's place is not observed (scratch/formal/valence.py,
   case 11);
2. **ordinal comparability**: every pair was contested and the wins are
   complete and transitive, so the record itself orders all the options;
3. **scalar currency**: the ordering has a real-valued representation,
   which a finite ordering always has and a graded lexicographic one on a
   continuum does not ([CLAIM-436](../claims.d/CLAIM-436.md), parts 1 and 2);
4. **cardinal trade-off structure**: differences in the representation
   mean something, so exchange rates between options are fixed up to an
   affine transform. Only here are margins intensities, and only here does
   the Hodge decomposition's least-squares potential measure what it says
   ([THEORY-894](../theory.d/THEORY-894.md)).

The record's "common currency", in the owner's sense, needs only the
first: the existence of a compatible extension, not an observed shared
evaluation of every option. Anything inferred about pairs never contested
is inferred about the class, not observed. The first level was named
"ordinal comparability" in a first revision and renamed "ordinal
extendibility" after a second review of the pull request, which pointed
out that acyclicity licenses only the weaker inference.

## What it is not

- **Not the Hodge gradient.** The gradient of the Hodge decomposition is
  a least-squares fit to margins, a cardinal object. It can rank B above A
  when A won their contest: margins A over B by 1, B over C by 10, A over
  C by 1 give scores 2/3, 3 and −11/3 ([CLAIM-434](../claims.d/CLAIM-434.md), part 4;
  scratch/formal/valence.py, case 1). Its cyclic share is positive on that
  record although the wins are transitive.
- **Not a currency.** On a finite set the two coincide at each instant;
  across instants and on continua they do not ([CLAIM-436](../claims.d/CLAIM-436.md)).
- **Not vacuous only by accident.** A negotiation with no contested
  pairs in W has an empty relation of wins, which is acyclic, so every
  ordering is trivially a potential. The term allows this; terms built on
  it, such as goal-conduciveness valence ([TERM-076](TERM-076.md)), must exclude it.
- **Not persistent.** A potential on each window says nothing about
  whether it is the same potential across windows. That is
  [TERM-078](TERM-078.md).
- **Not a potential game.** Monderer and Shapley's generalized ordinal
  potential ([THEORY-896](../theory.d/THEORY-896.md)) is defined over players' unilateral
  deviations; this term needs only the relation of wins.
