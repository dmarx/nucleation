---
number: 218
status: Proposed
formerly:
- CASE-tmpli7gt
title: 'A two-stage toy of nucleus stabilization, nucleation s/(1+s) and completion 1/(1+s²/4), whose final yield peaks at s ≈ 1.11 with 40.2 %, so that stabilizing the nucleus beyond the optimum makes it easier to form and lowers what forms'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-595
- CLAIM-185
summary: >-
  A's toy, from the fourth synthesis on DNA origami pasted by the owner on
  2026-11-05 ("Predicting which organizations will successfully
  nucleate"), Prediction 3. A stabilization strength s raises the chance
  of forming a nucleus, P_N(s) = s/(1+s), and lowers the chance that a
  nucleus completes instead of trapping, P_F|N(s) = 1/(1+s²/4). Yield
  Y(s) = P_N · P_F|N has an interior optimum. A's figures at s = 1.10 are
  nucleation 52.4 %, completion 76.8 % and yield 40.2 %, with the optimum
  near s = 1.11; they are checked with python3 -I, the optimum at s =
  1.1134. The functional forms are A's, invented to show the mechanism.
  Dunn et al.'s weakened seams and Majikes et al. 2021's blocked fold are
  the molecular instances of the descending side. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-185 CLAIM-594 CLAIM-595 — Proposed, Skimmed or new; entries cited as open -->

# CASE-218: A two-stage toy of nucleus stabilization, nucleation s/(1+s) and completion 1/(1+s²/4), whose final yield peaks at s ≈ 1.11 with 40.2 %, so that stabilizing the nucleus beyond the optimum makes it easier to form and lowers what forms

## The case

A: "Early structural stability can have two opposing effects. It can give
subsequent interactions enough time to form, but it can also make mistakes
difficult to undo." With stabilization strength s:

  P_N(s) = s/(1+s),  P_F|N(s) = 1/(1+s²/4),  Y(s) = P_N(s) · P_F|N(s).

Checked with python3 -I:

| s | P_N | P_F\|N | Y |
|---|---|---|---|
| 1.10 | 0.524 | 0.768 | 0.402 |
| 1.1134 (optimum) | | | 0.4022 |

Past the optimum the nucleus forms more easily and the yield falls.

## What it can show

- **The second half of [CLAIM-595](../claims.d/CLAIM-595.md),** in A's proposed wording:
  "strengthening an intermediate can increase initial formation while
  reducing final yield".
- **An anchor that is too good** ([CLAIM-185](../claims.d/CLAIM-185.md)). A useful nucleus must be
  "stable enough to coordinate further organization but not so inflexible
  that it prevents correction."
- **A window in a resource,** of the kind [CLAIM-594](../claims.d/CLAIM-594.md) finds for heat,
  here for binding strength.

## What it does not show

A says the curve "is an invented model demonstrating a possible
mechanism, not an empirical measurement". A's test is the right one: "The
key is not simply to observe an inverted-U curve. It's to establish that
its descending side arises from increased trapping rather than, say,
chemical degradation." In DNA origami, Dunn et al.'s halved seams cut
misfolds, and Majikes et al. 2021's yield falls with staple excess. Both
show a descending side with trapping or blocking as the stated cause, at
one point each, not as a sweep.
