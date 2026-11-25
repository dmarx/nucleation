---
number: 994
status: Proposed
formerly:
- CLAIM-tmpv22hv
title: 'The toy study meets the barrier defeater'
statement: >-
  Read at the grain of the input cue relied on, the toy study meets both
  clauses of the defeater of the claim that a barrier surviving alignment
  marks a different mechanism
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-157, as one of two
    alternative readings of CASE-385 for the owner to choose between;
    the other is CLAIM-992.
role: counter
warrant: interpretive
tags:
- loss-landscapes
- representation-learning
date: '2026-11-22'
line:
- learned-structure
- pragmatic-transport
rests_on:
- CLAIM-993
objects_to:
- CLAIM-263
bears_on:
- QUESTION-069
summary: >-
  One reading of [CASE-385](../cases.d/CASE-385.md), an alternative to [CLAIM-992](CLAIM-992.md). [CLAIM-263](CLAIM-263.md)'s
  defeater gives its independent test of a shared mechanism as "the same
  input attributes relied on". Read at that grain, the toy meets both of
  its clauses. At width 5, pairs that rely on the same cue stay separated
  after an exhaustive search over the full symmetry group of a ReLU MLP.
  At widths 64 and 256, pairs relying on different cues are connected
  after alignment, and their features roughly interpolate along the path
  (midpoint cosine 0.88 to 0.90). So step 2 of the protocol, reading a
  surviving barrier as a different mechanism, fails in this toy. [CLAIM-187](CLAIM-187.md)
  inherits the failure through its `rests_on`. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-385 CLAIM-993 CLAIM-992 — new; the study, the finding this rests on, and the alternative reading -->
<!-- inactive-ok-file: CLAIM-263 CLAIM-187 THEORY-116 CLAIM-142 — Proposed; the claims this objects to, the reading behind their step 2, and the probe caution, open -->

# CLAIM-994: The toy study meets the barrier defeater

## The objection

[CLAIM-263](CLAIM-263.md) is defeated by "pairs of trained networks that share a mechanism
by an independent test (the same input attributes relied on, the same
features up to alignment) found separated by a barrier that survives
quotienting the full symmetry group; or pairs that do not share one found
connected after alignment, with features that interpolate along the path".

Take "the same input attributes relied on" as the independent test.
[CASE-385](../cases.d/CASE-385.md)'s cue-reliance test is that test, built so that the
mechanism is known. [CLAIM-993](CLAIM-993.md) gives the result:

- **First clause.** Three of four width-5 pairs that both rely on cue A
  (0.87–0.91 on A-only, chance on B-only) keep loss barriers of 0.09 to
  0.25 after the best of all permutation pairs plus optimised rescaling.
  That is the full symmetry group of the architecture up to measure-zero
  extras. Same-B pairs keep 0.10 to 0.65.
- **Second clause.** At widths 64 and 256, all eight pairs of an A-net and
  a B-net are at zero barrier after activation matching. Their layerwise
  midpoint features are proportional to the interpolation of the
  endpoints' (cosine 0.88–0.90), which is [THEORY-111](../theory.d/THEORY-111.md)'s sense of
  "interpolate", though below the same-cue pairs' 0.94–0.97.

On this reading the barrier tracks capacity, not mechanism. Step 2 of
[CLAIM-263](CLAIM-263.md) ([THEORY-116](../theory.d/THEORY-116.md)'s direction) does not hold here, and neither does
[CLAIM-187](CLAIM-187.md)'s carry-over, which rests on it.

The alternative reading, [CLAIM-992](CLAIM-992.md), takes the features grain instead
and finds the protocol narrowed, not defeated.

## What it does not say

- It does not say the protocol fails for wide image classifiers or
  transformers. The study is a toy.
- It does not answer the objection that the probe set (inputs where both
  cues agree) cannot see the difference ([CLAIM-142](CLAIM-142.md)). On this reading that
  objection changes the test's object, not its result.
