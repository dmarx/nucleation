---
status: Active
title: 'In a simulated forager that learns from its own energy account which features warn of a loss, revising which features count is needed for, and pays only on, a change whose warning sign is a feature it never attended to; a change on a feature it already attends to is met by re-estimating, and a change that shows itself as an absence is met by registering the absence'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-177 as a delegated
    lead worker, from the run filed as CASE-tmpz762n.
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): CASE-tmpz762n, its ground, reproduces and is Active,
    and the figures match the reproduced forager summary; no objection;
    the defeater is not met.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-177/forager.py such that, once corrected,
  the stated construction gives a different pattern: the frozen arms
  matching the learner on the new-feature change under either rule, or the
  learner beating the features-only freeze on the delayed change, or an arm
  without in-visit registration surviving the silent change as well as one
  with it. Another world, with other sizes of change or other learning rules,
  does not defeat it; the claim is about this construction and these two
  rules.
tags:
- learning-and-conditioning
- philosophy-of-biology
- control-theory
date: '2026-11-22'
line:
- distributed-agency
- organizational-normativity
grounds:
- CASE-tmpz762n
bears_on:
- QUESTION-285
- QUESTION-128
summary: >-
  From [LEAD-177](../leads.d/LEAD-177.md)'s run of [CASE-239](../cases.d/CASE-239.md) ([CASE-tmpz762n](../cases.d/CASE-tmpz762n.md)). Three changes nobody
  trained the forager for, 40 seeds, two learning rules. A delayed cost on a
  feature it never attended to: the learner, which may add features, survives
  in 40 and 38 of 40 seeds; the same learner barred from adding them survives
  in 21 and 22 (13 and 24 with its threshold and probes frozen too). The same
  cost on a feature it already attends to: barred and free learners are
  identical (35 and 31 of 40), since new weights suffice. A silent patch:
  every arm that registers a shortfall during a visit survives, and adding the
  silence feature paid under one rule and cost under the other. So [CASE-239](../cases.d/CASE-239.md)'s
  separation of revising estimates from revising criteria shows up exactly
  where the warning sign is new to the forager. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpz762n — new; the run this claim is drawn from -->
<!-- inactive-ok-file: CASE-239 CASE-241 CLAIM-651 — Proposed; the study design run, the profiles it compares and the claim on registering a non-response -->

# CLAIM-tmppa4rs: In a simulated forager that learns from its own energy account which features warn of a loss, revising which features count is needed for, and pays only on, a change whose warning sign is a feature it never attended to; a change on a feature it already attends to is met by re-estimating, and a change that shows itself as an absence is met by registering the absence

## The claim

[CASE-239](../cases.d/CASE-239.md) proposed separating a forager that revises its criteria of failure
from one that only revises its estimates, by freezing which features and
probes count (its arm 5). In the run ([CASE-tmpz762n](../cases.d/CASE-tmpz762n.md)), the three changes it
named sort cleanly by what they need:

1. **A warning sign the forager never attended to** (a feature irrelevant in
   training that comes to predict a later rise in upkeep). Re-estimating the
   attended features cannot see it. Only an arm that may add a feature
   survives reliably: 40 and 38 of 40 against 21 and 22 for the
   features-only freeze, under recursive least squares and a table. The
   learner added the feature in 40 and 37 runs.
2. **A warning sign it already attends to** (red patches come to raise upkeep
   later). New weights on red suffice; barring new features changes nothing
   (35 and 31 of 40 either way).
3. **An absence** (a feature-linked silent patch). Registering the shortfall
   at the first silent step suffices, for every arm that has an in-visit test,
   including [CASE-241](../cases.d/CASE-241.md)'s fixed self-set profile. Learning to avoid the patch
   and probing for it paid against arm 5 under one rule (39 of 40 seeds) and
   cost under the other (lost in 38 of 40).

So criterion revision, in [CASE-239](../cases.d/CASE-239.md)'s sense of changing which distinctions
count, is what the first change needs and the other two do not. This is
[QUESTION-285](../questions.d/QUESTION-285.md)'s top rung, revision of what is discriminated, separated from
the rung of use by a test that fails without it.

## What it does not say

- That the criterion is the forager's own. The energy variable, the
  dissolution condition, the learning rules and the features available to a
  criterion are the modeller's ([CASE-239](../cases.d/CASE-239.md)'s main threat; [CASE-tmpz762n](../cases.d/CASE-tmpz762n.md), "What
  it cannot show").
- That revision is free. Where the change was an absence, revising features
  and probes cost as often as it paid; a fixed profile that registers the
  absence did better than both learners. Registering an absence and revising
  what counts are different achievements ([CLAIM-651](CLAIM-651.md) is about the first).
- That the result holds for changes of other sizes, or for learners beyond
  the two run.
