---
number: 576
status: Proposed
formerly:
- CLAIM-tmpisvzb
title: 'What characterizes a constrained system is a repertoire of realizable processes, indexed by resources and dependent on its architecture, rather than its set or space of states, and the repertoire changes in three ways an equivalence between such systems must keep apart: a budget makes an existing transformation affordable, observational or computational capability makes an existing possibility discoverable or controllable, and a change of architecture alters which transformations are possible'
version: 3
history:
- version: 2
  date: '2026-11-11'
  note: >-
    From the defects listed in the synthesis review of 2026-11-11
    (curation entry 015730): the body's paragraph "The state space is
    not enough" drew from CLAIM-583 what the claim's own note of
    2026-11-06 says it does not show. It is retitled "The
    compatibility complex is not enough", keeps CLAIM-583's quotation,
    and adds that CLAIM-583 does not show the state space
    insufficient, since its two systems have different configurations
    and, with a fixed move rule, configurations and moves carry
    reachability. The title, thesis and defeater are unchanged. No
    other change.
- version: 3
  date: '2026-11-15'
  note: >-
    Note of 2026-11-15 added, from the readings of repeated sampling and RL
    post-training: Brown et al. measure affordability and discoverability
    apart (THEORY-1894 corroborates the claim); Yue et al., Meng et al.
    and Balasubramanian and Kasiviswanathan read RL as reweighting; ProRL is
    the test of whether training ever does more, and does not settle it. The
    architecture clause is not answered. No status change.
role: thesis
warrant: interpretive
defeated_if: >-
  A comparison of constrained systems the record needs, such as telling
  apart CASE-194's three organizations or deciding whether an intervention
  creates a capability, that a description by states and configuration
  spaces alone makes as well as the repertoire does; or a class of declared
  models in which the three ways cannot be told apart even in principle,
  because every change of budget, of observation and of architecture can be
  re-described as each of the others without loss. Also defeated as new,
  though not as true, if it says no more than the held separations of
  feasible from reachable, of budget from architecture and of observation
  from action jointly say. Not defeated by the continued usefulness of
  configuration spaces, which the claim keeps as one layer.
tags:
- philosophy-of-science
- metaphysics
- complex-systems
date: '2026-11-05'
line:
- realizability
rests_on:
- CLAIM-583
complements:
- CLAIM-586
- CLAIM-582
uses:
- TERM-114
bears_on:
- QUESTION-385
- QUESTION-392
summary: >-
  A's conjecture, from the pasted synthesis on resource-bounded
  realizability (three responses, pasted by the owner on 2026-11-05,
  continuing the exchange on constraint architectures), Response 3 §11:
  "the most promising candidate for the general object" is "a
  resource-indexed, architecture-dependent algebra of realizable processes",
  and its repertoire changes three ways that "should be preserved by any
  proposed equivalence". Merged with its earlier forms: Response 1's
  constitutive against operational constraints, where "its operationally
  accessible structure changes" and not the object, and Response 2's
  "universality theory of resource-bounded realizability, rather than a
  universality theory of constraint satisfaction alone". Each of the three
  ways is held separately; the conjecture is that together they, and not a
  state space, are the invariant. Interpretive. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-194 CASE-198 CLAIM-477 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-576: What characterizes a constrained system is a repertoire of realizable processes, indexed by resources and dependent on its architecture, rather than its set or space of states, and the repertoire changes in three ways an equivalence between such systems must keep apart: a budget makes an existing transformation affordable, observational or computational capability makes an existing possibility discoverable or controllable, and a change of architecture alters which transformations are possible

## The claim

A (Response 3 §11): "An object is not adequately characterized by a set of
states or even by a space of possible states. Instead, it possesses a
structured repertoire of capabilities, determined jointly by its
constraints, operations, information, and resource availability. This
repertoire changes in at least three distinct ways. An increase in budget
can make an existing transformation affordable. An increase in
computational or observational capability can make an existing possibility
discoverable or controllable. An architectural change can alter the
underlying repertoire of possible transformations. These differences
should be preserved by any proposed equivalence between resource-bounded
constraint systems." The general object is then "a resource-indexed,
architecture-dependent algebra of realizable processes".

**Its earlier forms.**

- Response 1 §4: "Constitutive constraints determine which states count as
  realizations of the object. Operational constraints determine which
  transitions are available under given computational and physical
  resources." "This need not imply that the object itself changes whenever
  a resource budget changes. Rather, its operationally accessible structure
  changes."
- Response 1: "An object's physical organization can be understood as an
  implementation of a computational constraint system, but its physical
  dynamics determine which computations can actually be realized within
  given resources."
- Response 2: "You may be looking for a universality theory of
  resource-bounded realizability, rather than a universality theory of
  constraint satisfaction alone." And §6: "A solution is a state. An
  organization has a repertoire of transformations."

**Each of the three ways is held.**

- **Budget.** At a fixed architecture a budget enlarges the compatibility
  complex only up to the unbudgeted one ([CLAIM-586](CLAIM-586.md)) and admits a
  transition only at its threshold, never one with no path
  ([CLAIM-571](CLAIM-571.md)): it makes affordable what was already possible.
- **Observation and computation.** [CASE-194](../cases.d/CASE-194.md)'s observational organization
  has the actions and lacks the information to choose among them;
  [TERM-064](../terms.d/TERM-064.md) makes legibility relative to an observer's resources.
- **Architecture.** [QUESTION-392](../questions.d/QUESTION-392.md) asks when an intervention creates a
  capability rather than cheapening one, and [CASE-198](../cases.d/CASE-198.md) lowers a
  threshold by a change of architecture; within one architecture an added
  constraint cannot enlarge what is reachable ([CLAIM-582](CLAIM-582.md)).

**The compatibility complex is not enough.** [CLAIM-583](CLAIM-583.md) shows two systems
with the same compatibility complex and different reachability; the
configuration layer "alone cannot detect that distinction". It does not
show that the state space is not enough: its two systems have different
sets of configurations, and with a fixed move rule the configurations and
their moves carry reachability (the note of 2026-11-06 below).

**What is conjectured** is the joining: that the repertoire, with the three
ways kept apart, is the invariant by which constrained systems should be
compared, and that a translation which conflates them, reading an
architectural change as a budget, say, loses something any comparison
needs.

## What it does not say

- **That the three ways never mix.** [CLAIM-586](CLAIM-586.md) notes that money can
  buy a new architecture; an intervention can do all three, and A says
  "those effects should be modeled separately", not that they come apart in
  the world.
- **That an object is its repertoire.** [CLAIM-477](CLAIM-477.md)'s account, on which an
  entity is partly fixed by the constraints on the configurations it can
  enter, is the nearest held relative; the conjecture is about what a
  comparison must preserve, not about what an object is.
- **That the algebra exists.** The word "algebra" is A's; no operations on
  repertoires are defined beyond the composition of processes
  ([CLAIM-563](CLAIM-563.md)).

## Note of 2026-11-06: what holds it back

[CLAIM-583](CLAIM-583.md), narrowed and promoted at this review, shows that the compatibility complex does not carry reachability; its two systems have different sets of configurations, and with a fixed move rule the configurations and their moves do carry it, so it does not show what "The state space is not enough" draws from it. No comparison is on file that the repertoire makes and a costed configuration space with its moves ([TERM-114](../terms.d/TERM-114.md)) does not, which is what the first and novelty clauses of the defeat condition ask, and the observational way is held only through [CASE-194](../cases.d/CASE-194.md), which is Proposed.

## Note of 2026-11-07: a feature flag against a release, from "Individuation, Possibility, and Disposition"

A, at A32 §8 of the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07): "A feature flag changes which existing behavior is operative. A new release can change which behaviors exist at all." That is this claim's distinction between selecting within a repertoire of realizable processes and an architecture change that alters the repertoire. A34 §10 adds that the possibility space is itself constructed. A does not cite this claim. No status changes.

## Note of 2026-11-15: inference budgets, and RL post-training as the hard case

<!-- inactive-ok-file: THEORY-1894 CLAIM-697 THEORY-1880 THEORY-1899 THEORY-1896 THEORY-1908 CLAIM-695 — Proposed; the readings and claims filed 2026-11-15 from the continuation of "Explain String Theory", cited as cases and as open, nothing here rests on them -->

Readings filed on 2026-11-15 give the claim machine-learning cases on each side of its distinction between a budget making an existing process affordable and a change making a new process possible.

- **Repeated sampling.** Brown et al. ([THEORY-1894](../theory.d/THEORY-1894.md), which corroborates this claim) give two of the three ways measured apart. The number of samples is a budget that makes already-possible solutions affordable to reach: a frozen model's SWE-bench Lite coverage goes from 15.9% at one sample to 56% at 250. The gap between coverage and majority-vote or reward-model selection (98% against 41% on MATH) separates reaching a correct output from being able to identify it, which is discoverability. [CLAIM-697](CLAIM-697.md) adds that coverage is not delivery without a selector.
- **RL post-training, the hard case.** Yue et al. ([THEORY-1880](../theory.d/THEORY-1880.md)) and Meng et al. ([THEORY-1899](../theory.d/THEORY-1899.md)) read RLVR as reweighting within what the base model already reaches, nearer affordability than a change of repertoire, while distillation lifts the boundary at every k. Balasubramanian and Kasiviswanathan ([THEORY-1896](../theory.d/THEORY-1896.md)) prove, in an idealization with disjoint support, that an exponential tilt of a fixed reference cannot create a mode: a formal case of a change that reweights without altering what is possible.
- **The test.** ProRL ([THEORY-1908](../theory.d/THEORY-1908.md), [CLAIM-695](CLAIM-695.md)) reports new strategies under prolonged RL, with pass@k rising from zero on some tasks. It does not settle the matter, since "zero" is read at k ≤ 128 from a distilled start.

The claim's question, whether a change makes a process possible or only cheaper, is here answered per training run, by matched-budget coverage. None of these readings is listed as corroborating the architecture clause: whether a change of weights is a change of architecture in this claim's sense is the claim's own question, and they do not answer it. No status change.
