---
status: Proposed
title: "A forager whose expected profile is set by its own upkeep against one whose profile is a designer's stored yield: they flag the same silent patch, and come apart when the yield falls but still pays and when the upkeep rises past an unchanged yield"
version: 1
standing: fictional
kind: construction
tags:
- philosophy-of-biology
- control-theory
date: '2026-11-12'
line:
- organizational-normativity
- record-as-apparatus
variant_of:
- CASE-tmpaky45
draws_on:
- THEORY-220
bears_on:
- QUESTION-128
summary: >-
  A construction for the question A5 §5 of "Meaning Transmission
  Explained" (2026-11-07) asked, whether an expected-response profile can
  be the system's own and not a designer's. Two foragers have stored
  energy that pays an upkeep each step, and either dies at zero. Each
  forages on a patch and switches patch on a registered failure. One
  expects only that the interaction sustains it (yield at least upkeep);
  the other expects the yield its designer stored. Rerun with exact
  arithmetic on 2026-11-12. They agree when the patch falls silent, the
  owner's debugging case in this setting. The designer's profile flags a
  failure when the yield falls but still pays. When the upkeep rises past
  an unchanged yield, it flags nothing and its forager dies at step 119,
  while the self-set one switches and lives. Stipulated throughout,
  dissolution condition included. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpaky45 CLAIM-tmpkr3ti — filed in this pull request, Proposed -->
<!-- inactive-ok-file: THEORY-220 THEORY-628 THEORY-tmp0d8vu — Proposed; readings cited with their standing -->

# CASE-tmpfobkh: A forager whose expected profile is set by its own upkeep against one whose profile is a designer's stored yield: they flag the same silent patch, and come apart when the yield falls but still pays and when the upkeep rises past an unchanged yield

## The construction

A forager has stored energy E, starting at 10, and dissolves when E ≤ 0.
Each step it pays an upkeep c and takes the yield of the patch it is on.
Patch A yields 3 and patch B yields 4, and the upkeep starts at 1. At step
20 one thing changes (the scenarios). Each forager registers a failure by
its expected profile and, on its first failure, switches patch. The run
lasts 200 steps.

- **Self-set profile.** The forager expects only that the interaction
  sustains it: y ≥ c. A failure is y < c, a step on which it lost
  energy. What it expects is fixed by its upkeep, a condition of its own
  persistence.
- **Designer's profile.** The forager expects patch A's yield to be what
  the designer stored, 3, within ½. A failure is |y − 3| > ½ on A.

## Results

Rerun on 2026-11-12 with exact fractions:

| from step 20 | self-set profile | designer's profile |
|---|---|---|
| S1: nothing changes | no failure; E = 410 | no failure; E = 410 |
| S2: A falls to 1.5, upkeep 1 | no failure; stays on A; E = 140 | failure at 20; to B; E = 587.5 |
| S3: A falls silent, yield 0 | failure at 20; to B; E = 586 | failure at 20; to B; E = 586 |
| S4: upkeep rises to 3.5, A still 3 | failure at 20; to B; E = 139 | no failure; dies at step 119 |

- **S3 is the owner's debugging case, endogenous.** An interaction
  expected to answer gives nothing. Both profiles register the absence
  as a failure ([CASE-tmpaky45](CASE-tmpaky45.md); [CLAIM-tmpkr3ti](../claims.d/CLAIM-tmpkr3ti.md)).
- **S2: the designer's profile flags what is no failure by the forager's
  own lights.** A still pays. The designer's flag happens to send its
  forager to the richer patch, so the self-set profile is a norm of
  going on, not of doing best.
- **S4: the designer's profile misses what is a failure by the forager's
  own lights.** The yield is as specified, the upkeep has outrun it, and
  the forager dies without registering anything. At step 20 it has 50,
  and it loses ½ a step.

## What it can show

That a profile set by a system's upkeep and one stored by a designer are
different norms, telling apart cases that matter for the system's
persistence (S4) and cases that do not (S2), while agreeing on the silent
case (S3). That is the distinction Bickhard draws ([THEORY-220](../theory.d/THEORY-220.md)): the
anticipation of a self-maintaining system can be "false by its own
lights", because what it anticipates is its own going on.

## What it cannot show

- **That the norm is not the modeller's.** The upkeep, the dissolution
  condition and the switching rule are all written by the modeller. What
  makes the self-set profile "own" is only that its failure condition is
  the same as the condition of the forager's persistence. The modeller
  wrote both, as Kolchinsky and Wolpert concede of their viability
  function ([THEORY-tmp0d8vu](../theory.d/THEORY-tmp0d8vu.md)). A construction cannot remove this; a
  physical self-maintaining system would.
- **Learning or revision.** The self-set profile is fixed by the upkeep
  rule, and nothing here changes how the forager discriminates.
- **Any graded norm.** Di Paolo's adaptivity ([THEORY-628](../theory.d/THEORY-628.md)) would need the
  forager to sense a trend toward its boundary, not only a losing step.
