---
number: 497
status: Active
formerly:
- CLAIM-tmpxk5cy
title: "A system's causes are found at the coarsest description whose interventions are unambiguous: a macro description is causally proportionate where it merges only micro states that intervention cannot tell apart, and no coarse-graining carries more causal information than the micro description it supervenes on"
version: 2
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed at the owner's direction of 2026-10-30, in place of THEORY-787,
    which is Rejected the same day: "reject it and adopt the proportionality
    thesis". Filed as a CLAIM, not a THEORY, because the formal part is
    already the record's (THEORY-1167, THEORY-1169) and what this adds is
    the record's own interpretive step from those results to where causes
    are (ADR-032, ADR-043).
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted at the nineteenth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), on the owner's
    direction of 2026-10-30 to "adopt the proportionality thesis". Its
    grounds are Active: THEORY-1167 and THEORY-1169, and LIT-1833 and
    LIT-1834, read in full in NOTE-1420 and NOTE-1415. Nothing objects
    to it, and nothing in the record meets its defeated_if. The reviewer
    re-checked the bound, the characterization of the lossless
    partitions and the uniqueness of the coarsest one by enumeration
    (p19/claim497_partitions.py, with a uniform-per-level control).
    QUESTION-204 moves from answers to bears_on (ADR-060): whether real
    systems have a stable proportionate level, the question's empirical
    half, is this claim's own defeated_if, not something it settles. The
    claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  On systems not built to display it, with effects estimated from data,
  the proportionate partition has no stable plateau: it changes with the
  threshold for "the same effect" and with sample size across the whole
  usable range, so that the level is picked by the analyst and not by the
  system. Or intervening on different realizers of one macro state of such
  a partition gives effects that differ systematically, beyond sampling
  error, when the system is probed more finely. Or a coarse-graining of one
  transition is found that, under one intervention distribution at both
  levels, carries more effective information than its micro description,
  which would mean THEORY-1167 is wrong. Toy transition matrices with exact
  equalities cannot settle it, since there it holds by construction.
tags:
- causality
- information-theory
- philosophy-of-science
date: '2026-10-30'
line:
- formal-apparatus
- distributed-agency
bears_on:
- QUESTION-204
grounds:
- THEORY-1167
- THEORY-1169
- LIT-1833
- LIT-1834
summary: >-
  The record's position on causal emergence after [THEORY-787](../theory.d/THEORY-787.md) was rejected.
  A coarse-graining can be the right causal description, but not by beating
  the micro. Under one intervention distribution at both levels, no
  coarse-graining of a transition carries more effective information than
  its micro ([THEORY-1167](../theory.d/THEORY-1167.md)). The ones that lose nothing are exactly causal
  feature learning's partitions, which merge only micro states with the
  same interventional effects ([THEORY-1169](../theory.d/THEORY-1169.md)). The step from there to "the
  causes are found at the coarsest such description" is the record's own,
  in the sense of proportionality. It does not say the macro adds causal
  information.
---
<!-- inactive-ok-file: QUESTION-204 QUESTION-335 — Open; the question this claim bears on and the case it leaves open, cited as open -->
<!-- inactive-ok-file: THEORY-787 — Rejected; the account this claim replaces, cited as rejected -->

# CLAIM-497: A system's causes are found at the coarsest description whose interventions are unambiguous: a macro description is causally proportionate where it merges only micro states that intervention cannot tell apart, and no coarse-graining carries more causal information than the micro description it supervenes on

## The claim

There is a level at which a system's causes are found, and it can be a
macro level. It is the coarsest description in which every macro
intervention is unambiguous: every micro state merged into one macro
state has the same distribution of effects under intervention. At that
level a coarser description loses causal information, and a finer one
adds none. This is proportionality, the condition that a cause be neither
broader nor narrower than its effect requires.

What the claim gives up is [THEORY-787](../theory.d/THEORY-787.md)'s further thesis, that a macro
description can carry more causal information than the micro and so be
where causation emerges. A macro can be the proportionate description. It
is never a richer one.

## What it rests on

- **The bound.** [THEORY-1167](../theory.d/THEORY-1167.md) (Active) shows that under one intervention
  distribution over micro states at both levels, a coarse-graining of one
  transition has at most the micro effective information. This is data
  processing.
- **The ties.** [THEORY-1169](../theory.d/THEORY-1169.md) (Active) shows that a coarse-graining keeps
  all of the micro effective information if and only if it merges only
  causes with identical rows P(Y | do(x)) and only effects with
  proportional columns. That holds for every full-support distribution.
  Those are the causal partitions of Chalupka, Perona and Eberhardt
  ([LIT-1833](../literature.d/LIT-1833.md), [LIT-1834](../literature.d/LIT-1834.md)), with effects grouped by normalized likelihood.
- **The interpretive step.** Of the descriptions that lose nothing, the
  coarsest is the one at which the causes are found. It is the record's
  own step, which is why this is a CLAIM and its warrant is interpretive.
  It takes the coarsest description because a finer one distinguishes
  micro states that no intervention tells apart. Those distinctions are
  realization detail, not causal structure.

## What it does not say

- **Not that the macro beats the micro.** No coarse-graining gains under a
  common distribution. A positive causal emergence of effective
  information, scored with a separate uniform distribution at each level,
  measures the change of distribution ([THEORY-1167](../theory.d/THEORY-1167.md), [THEORY-222](../theory.d/THEORY-222.md)).
- **Not that the micro description is wrong.** It is true, and it is
  finer than the causes require.
- **Not how to merge estimated rows.** Exact equality is the condition.
  With data, rows are merged by a threshold, and whether real systems have
  a stable proportionate level is what `defeated_if` tests.
- **Not about temporal or spatio-temporal macros**, where a macro step
  spans several micro steps. [QUESTION-335](../questions.d/QUESTION-335.md) holds that case.
- **Not that only causal partitions are useful.** A description chosen
  for prediction or compression for a declared target can be coarser or
  finer ([QUESTION-252](../questions.d/QUESTION-252.md)), and normalized measures can rise at a macro
  ([LIT-1843](../literature.d/LIT-1843.md)). This claim concerns where causes are, not which description
  serves a purpose.
