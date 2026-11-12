---
status: Proposed
title: 'A proposed study: a forager that learns from its own energy dynamics which environmental distinctions predict a loss of viability, and revises its testing and action policy, to find whether it adapts its criteria of failure to changes nobody foresaw without the correct criterion being supplied'
version: 1
standing: stipulated
kind: proposed-study
tags:
- philosophy-of-biology
- control-theory
- learning-and-conditioning
date: '2026-11-12'
line:
- organizational-normativity
- record-as-apparatus
variant_of:
- CASE-tmpfobkh
draws_on:
- THEORY-220
- THEORY-tmp0d8vu
bears_on:
- QUESTION-128
- QUESTION-285
summary: >-
  The review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed on 2026-11-12 found that the
  two-profile forager ([CASE-tmpfobkh](CASE-tmpfobkh.md)) "compares two criteria, not
  endogenous norm formation", since the programmer specified upkeep,
  dissolution and response policy. It asked for a forager "that learns
  from its own energy dynamics which environmental distinctions predict
  future loss of viability, and changes its testing and action policy
  accordingly". The question is whether it can adapt its criteria to
  unforeseen changes without having the correct criterion supplied in
  advance. Arms, measures, the outcome that would count against
  endogenous revision and the main threat to inference are set out
  below. The main threat: the designer still chooses the learning rule
  and the viability variable. Not built or run. The design's wording is
  the assistant's (Claude, in this session), from the review's request;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpfobkh CASE-tmpaky45 — filed in this pull request, Proposed -->
<!-- inactive-ok-file: THEORY-220 THEORY-tmp0d8vu THEORY-628 — Proposed; readings cited with their standing -->

# CASE-tmp5ijqy: A proposed study: a forager that learns from its own energy dynamics which environmental distinctions predict a loss of viability, and revises its testing and action policy, to find whether it adapts its criteria of failure to changes nobody foresaw without the correct criterion being supplied

## Why

[CASE-tmpfobkh](CASE-tmpfobkh.md) fixes both profiles in advance. Its self-set profile, y ≥ c,
is written by the modeller. So it compares two criteria and cannot show a
criterion being formed or revised. The review of [#483](https://github.com/dmarx/nucleation/issues/483) the owner relayed
on 2026-11-12: "The experimental question: can it adapt its criteria to
unforeseen changes without having the correct criterion supplied in
advance?"

## The world

As in [CASE-tmpfobkh](CASE-tmpfobkh.md), a forager has energy E, pays an upkeep each step and
dissolves at E ≤ 0. Patches now have observable features, such as colour,
temperature, a neighbour's presence or time since last visit. The
forager's energy change depends on these through rules the forager is not
given. Some features predict a yield. Others predict a later loss, for
example a patch that pays now and raises upkeep later.

The forager can **probe**: spend energy on a short test visit, the
analogue of the debugger's test smoke ([CASE-tmpaky45](CASE-tmpaky45.md)). It can also
**act**: stay, switch or rest.

## The learner

- **What it learns.** A predictor of its own energy trajectory ΔE over
  the next k steps from the features. Its "criterion of failure" is the
  predicted loss of viability: a feature pattern counts as a warning if
  it predicts falling below a margin of E.
- **What it revises.** Which features it attends to, which probes it
  runs, and when an expected yield that did not come counts as a
  failure. That is, its profile and its testing policy, not only its
  estimates.
- **What is not supplied.** No feature-to-failure mapping, and no list
  of which changes will happen. Only the energy variable and the learning
  rule are given.

## Arms

1. **Learner**, as above.
2. **Fixed self-set profile**, [CASE-tmpfobkh](CASE-tmpfobkh.md)'s y ≥ c, no learning.
3. **Designer's profile**, [CASE-tmpfobkh](CASE-tmpfobkh.md)'s stored yield.
4. **Oracle**, given the true feature-to-loss mapping after each change.
   This is the ceiling.
5. **Learner with a frozen criterion**: it learns ΔE predictions but may
   not change which features or probes count. This separates revising
   estimates from revising criteria.

## Changes nobody foresaw

After a training period, introduce changes the learner was not trained
on:
- a delayed cost, where a feature that predicted gain now predicts a
  later upkeep rise;
- a new relevant feature, a variable that was always present but
  irrelevant and becomes predictive;
- a silent patch whose silence depends on a feature, the endogenous form
  of the debugger's case.

## Measures

- survival time and final energy after each change;
- time from a change to the first correct warning;
- false warnings, flags where viability is not at risk ([CASE-tmpfobkh](CASE-tmpfobkh.md)'s
  S2);
- missed failures ([CASE-tmpfobkh](CASE-tmpfobkh.md)'s S4);
- the regret of arm 1 against the oracle, arm 4;
- whether the learner's attended features and probes change after a
  change, and whether the change tracks the new predictor (arm 1 against
  arm 5).

## What would count against endogenous revision

The learner does no better than the frozen-criterion learner (arm 5) on
changes that need a new feature or probe. Or its gains vanish when the
viability variable is replaced by any other variable the designer could
have chosen, so that what it tracks is whatever it was told to keep.
Either outcome means it revises estimates and not criteria, or that its
criteria are the designer's in another form.

## The main threat to inference

The designer still chose the learning rule and the viability variable,
as Kolchinsky and Wolpert concede of theirs ([THEORY-tmp0d8vu](../theory.d/THEORY-tmp0d8vu.md)). A positive
result shows that, given a viability variable and a learning rule, the
criterion of failure need not be supplied. It does not show that the
system's norm is its own in Bickhard's sense ([THEORY-220](../theory.d/THEORY-220.md)), unless the
viability variable is the condition of the forager's actual dissolution
and not a score. Partial controls:
- tie the variable to dissolution, as here;
- vary the learning rule, and check that the qualitative result
  survives several rules;
- report which features the learner came to treat as warnings, so a
  reader can check that they are not a disguised designer's list.

## Status

Not built and not run. Building it is a few hours for a tabular or
linear learner, more for a learner that can add probes. The bearing on
[QUESTION-128](../questions.d/QUESTION-128.md) (norms from an organization's own dynamics) and [QUESTION-285](../questions.d/QUESTION-285.md)
(an apparatus revising what it discriminates) depends on the outcome.
Di Paolo's adaptivity ([THEORY-628](../theory.d/THEORY-628.md)), a graded norm that tracks a tendency
toward the boundary, is what the warning margin approximates.
