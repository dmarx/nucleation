---
status: Active
title: 'In the Overview of Early Vision''s taxonomy of InceptionV1, every one of the 1,056 units of conv2d0 to mixed3b is assigned by the authors to exactly one of 77 groups, and 391 of them (37%), from 7% of conv2d2 to 48% of conv2d1 and 45% of mixed3b, are in groups whose own captions call them catch-all, broad and not well defined, low-confidence, unstudied or not understood; the mixed3b curve family is 10 of that layer''s 480 units'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpdmtd9, the reading of Olah et al. (2020) in
    full. The counts were re-derived on 2026-10-27 by parsing the
    article's neuron grids and checked against the five taxonomy files it
    offers for download, which agree unit for unit; the rule for a
    flagged group is stated below, so the count can be repeated. One
    study, read in full; the title claims no more than the article states
    and its grids show, and nothing in the record contradicts it
    (ADR-047 v3). The authors' wider claim, that the families are real
    and recur across models, is THEORY-tmpehpcu, Proposed.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmp6ii6u
summary: >-
  Olah et al. (2020), LIT-tmp6ii6u, read in NOTE-tmpdmtd9: the census of
  InceptionV1's early vision, counted. A complete partition of 1,056 units
  into 77 groups, by eye; 37% in groups the authors flag as uncertain or
  catch-all, by their own words. It is a denominator for the circuits
  claim that units are typically features (THEORY-1013), not a measure of
  how many units are understood.
---
<!-- inactive-ok-file: THEORY-tmpehpcu THEORY-1013 THEORY-1022 — Proposed; the authors' wider claim, the Zoom In account this count serves and the curve account, cited as open -->
# THEORY-tmpjdph0: In the Overview of Early Vision's taxonomy of InceptionV1, every one of the 1,056 units of conv2d0 to mixed3b is assigned by the authors to exactly one of 77 groups, and 391 of them (37%), from 7% of conv2d2 to 48% of conv2d1 and 45% of mixed3b, are in groups whose own captions call them catch-all, broad and not well defined, low-confidence, unstudied or not understood; the mixed3b curve family is 10 of that layer's 480 units

## Source

Olah, Cammarata, Schubert, Goh, Petrov and Carter (2020), *An Overview of
Early Vision in InceptionV1*, Distill, LIT-tmp6ii6u, read in full in
NOTE-tmpdmtd9: the five layer sections, every group's caption and neuron
grid, and the taxonomy files of its Resources section.

## What was actually shown

**The partition.** The article lists, for each of conv2d0 (64 units),
conv2d1 (64), conv2d2 (192), mixed3a (256) and mixed3b (480), named groups
with the units in each and each group's share of the layer: 3, 8, 14, 18
and 34 groups. Every unit of each layer appears in exactly one group, and
the printed shares agree with the counts to rounding.

**The flagged groups.** A group is counted as flagged when its caption
says it is a catch-all ("Catch-all category", "Units that don't fit in
another category", "don't fall in any other category"), "broad, not very
well defined", "low confidence", "haven't studied them very carefully",
"didn't know what else to do with", "don't really understand", or "likely
best thought of as a polysemantic neuron". By that rule:

| layer | units | flagged | share |
|---|---|---|---|
| conv2d0 | 64 | 9 | 14% |
| conv2d1 | 64 | 31 | 48% |
| conv2d2 | 192 | 14 | 7% |
| mixed3a | 256 | 122 | 48% |
| mixed3b | 480 | 215 | 45% |
| all | 1,056 | 391 | 37% |

**The curve family** is 10 of mixed3b's 480 units (2.1%). The fourteen
mixed3b groups the article presents as "particularly interesting and well
understood" hold 118 units (24.6%).

**What could have come out otherwise.** Units could have been left out or
counted twice, the shares could have disagreed with the grids, and the
flagged share could have been small or concentrated in one layer. None of
these happened.

## What this does not say

- **Not that 63% of early vision is understood.** An unflagged group is a
  label given by eye, in the authors' words often after "a few minutes of
  cursory investigation", and the article states no criterion for
  membership.
- **Not that the flagged units are meaningless.** A catch-all says the
  authors have no name for them, not that the units have no function.
- **Not about other models or bases.** One network, its neuron basis.
- **The rule is this record's,** applied to the authors' words; another
  reader might count "Gabor-like" (conv2d1, "We haven't studied them very
  carefully") or a borderline caption differently. The flagged list is in
  NOTE-tmpdmtd9.

## Connections

- **THEORY-1013.** Its promote_when asks for a fraction of units meeting a
  stated criterion over whole layers. This is the denominator, and the
  authors' own uncertainty over it; the criterion is still missing.
- **THEORY-1028 and THEORY-1022.** The curve family of the census is the
  one those accounts describe.
