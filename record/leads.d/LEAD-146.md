---
number: 146
status: Open
formerly:
- LEAD-tmpqgbxs
title: 'Fix what the discriminating fidelity study must fix before data: a strong contextual baseline, named receiver populations and sampling frames, an equivalence margin with power, and an interlingual arm'
version: 1
stage: specified
priority: high
method:
- operationalization
- conceptual
tags:
- translation
- philosophy-of-science
- philosophy-of-language
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- CLAIM-202
- CLAIM-205
- CLAIM-226
- CLAIM-222
- CLAIM-233
- QUESTION-074
operationalized_in:
- CASE-055
summary: >-
  The preregistration the discriminating study binds; cheap, and three
  Active counters ask for it. Named in [CASE-055](../cases.d/CASE-055.md), [CLAIM-205](../claims.d/CLAIM-205.md), [CLAIM-226](../claims.d/CLAIM-226.md) and
  [CLAIM-222](../claims.d/CLAIM-222.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-202 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-146: Fix what the discriminating fidelity study must fix before data: a strong contextual baseline, named receiver populations and sampling frames, an equivalence margin with power, and an interlingual arm

## What it would do

Write the study's preregistration: the contextual baseline the incremental
thesis is restated against, the receiver populations and how they are
sampled, the equivalence margin and the power to detect it, the prevalence
rates it assumes, and one language pair for the interlingual arm.

Where the record names it:

- [CASE-055](../cases.d/CASE-055.md): "It has not been run, and its margins are not yet fixed."
- [CLAIM-205](../claims.d/CLAIM-205.md): "The incremental thesis restated against a strong contextual
  baseline, specified in advance, with the margin fixed as [CLAIM-202](../claims.d/CLAIM-202.md) already
  requires."
- [CLAIM-226](../claims.d/CLAIM-226.md): "A named receiver population and sampling frame in each
  design."
- [CLAIM-222](../claims.d/CLAIM-222.md): "An interlingual design: at least one language pair in which
  footing or politeness is grammatically marked on one side only, with
  judges on both sides."

## What would count

The lead is done when the margins are fixed in [CASE-055](../cases.d/CASE-055.md). It answers
[CLAIM-226](../claims.d/CLAIM-226.md) and [CLAIM-222](../claims.d/CLAIM-222.md) by meeting what they ask, and lets [CLAIM-202](../claims.d/CLAIM-202.md) and
[CLAIM-205](../claims.d/CLAIM-205.md) be defeated or not by data.

## Note of 2026-11-22: the preregistration drafted, the margins not fixed


The assistant drafted the preregistration this lead asks for, in
scratch/studies/lead-146/preregistration-draft.md. Beside it are a power
simulation (power.py, its tests and results.json), and a dated note on
[CASE-055](../cases.d/CASE-055.md) summarizes it. It covers the five things the lead names:

- **The contextual baseline**, specified for [CLAIM-205](../claims.d/CLAIM-205.md) on the same inputs
  as the transport measures.
- **Receiver populations and sampling frames**, named for [CLAIM-226](../claims.d/CLAIM-226.md), with a
  rule for the anchor-item invariance test.
- **The margin, with its power computed.** The lean is 0.05 in held-out R²
  at 160 analysed items an arm; 0.02 and 0.01 are costed.
- **The prevalence rates**, stated as assumptions for a pilot to replace.
- **The language pair** for [CLAIM-222](../claims.d/CLAIM-222.md): English → German, French or
  Japanese, with the lean on German.

The simulation also finds that the defeat rule is too liberal at the
margin. A thesis whose true increment equals the margin is defeated 9% of
the time at the lean, not 5%. The draft gives four remedies.

What remains: the lead is done "when the margins are fixed in [CASE-055](../cases.d/CASE-055.md)",
and fixing them is the owner's. The draft lists seventeen choices with
their alternatives. The margin, the baseline's extent and the language pair
are the ones the lead turns on. Stage 0's reliability target is [LEAD-162](LEAD-162.md)'s,
and the pilot that would replace the assumed rates has not been run. This
lead's stage and status are unchanged.
