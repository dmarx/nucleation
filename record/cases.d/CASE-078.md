---
number: 78
status: Active
formerly:
- CASE-tmp7b477
title: 'Who keeps placing on r/place: the proposed survival analysis of the released placement logs, testing whether participants return while their art survives and whether unaffiliated placement cools'
version: 1
standing: stipulated
kind: proposed-study
tags:
- complex-systems
- social-science
date: '2026-10-13'
line: distributed-agency
summary: >-
  Proposed by the owner on 2026-10-13, not run. On the released 2017, 2022
  and 2023 logs, model each participant's hazard of stopping, with the
  survival of the art they placed into as a time-varying covariate, and
  estimate the rate of placements that fit no artwork over the event. The
  main threat is reverse causality: persistent defenders keep their art
  alive. So the design leans on destruction the participant did not cause,
  such as the 2022 moderator wipes and large raids. It is the test named in
  [CLAIM-274](../claims.d/CLAIM-274.md)'s defeater.
---
<!-- inactive-ok-file: CLAIM-274 CLAIM-273 QUESTION-085 CLAIM-280 THEORY-214 THEORY-216 THEORY-218 THEORY-224 QUESTION-084 — Proposed or Open; claims, questions and readings the study would test, cited as open -->

# CASE-078: Who keeps placing on r/place: the proposed survival analysis of the released placement logs, testing whether participants return while their art survives and whether unaffiliated placement cools

## The case

The owner asked for it to be filed as a potential experiment, after
[CLAIM-274](../claims.d/CLAIM-274.md) said: "The released logs (2017, 2022, 2023) would allow a
survival analysis". It tests three things, in order of difficulty.

**1. Cooling.** Does the rate of unaffiliated placement fall over an event?

- *Measure.* Fix a set of plans: artwork outlines from the community atlases
  for 2017 and 2022, or coalitions recovered from the log as Wu and Silva do
  ([THEORY-216](../theory.d/THEORY-216.md)). An unaffiliated placement is one that matches no
  artwork's colour at its site. Estimate its rate per hour and per region,
  the canvas temperature T(x, t) of [TERM-054](../terms.d/TERM-054.md).
- *Decompose* the change in T into fewer active participants and less
  unaffiliated placing per participant. Only the second part, together with
  test 2, says anything about selection.
- *Caveat.* The set of plans is a choice ([TERM-054](../terms.d/TERM-054.md)). Falmagne et al.
  could not tell an attack from an adopted "innovation" ([THEORY-214](../theory.d/THEORY-214.md)).
  Report T under at least two plan sets.

**2. Selective retention.** Do participants stop sooner when the art they
placed into is lost?

- *Unit.* A participant in one edition. User ids are hashed separately per
  edition.
- *Outcome.* Time to last placement, with stopping defined as no placement
  for G hours. Report several values of G. A recurrent-event model of the
  gaps between placements is the alternative.
- *Exposure, time-varying.* The share of a participant's placed pixels that
  still show the colour they placed. Separately, whether the artwork or
  artworks they contributed to are still standing.
- *Controls.* Event time, as the baseline hazard, which absorbs novelty
  wearing off for everyone. Also the participant's placements so far,
  their cooldown regime, and a bot filter (Wu and Silva's, and the 2023
  likely-bot share noted in [CASE-079](CASE-079.md)).
- *Model.* Cox proportional hazards with time-varying covariates and a
  per-user frailty, or a discrete-time hazard per hour.
- *The threat, and the remedy.* Persistent participants keep their art
  alive, so survival of the art and return of the participant are
  confounded in both directions. The estimate needs losses the participant
  did not cause:
  - **moderator removals in 2022**, which appear in the log as rectangle
    edits (x1, y1, x2, y2). This is the cleanest exogenous destruction;
  - **large raids** by coalitions unrelated to the participant, such as the
    Void;
  - **contributors who were a small share** of an artwork that fell, whose
    own absence cannot have caused the fall.

  Compare matched participants whose art was or was not destroyed this way,
  matching on activity before the loss.

**3. Recruitment.** Does visible growth or damage draw newcomers to an
artwork?

- *Measure.* First-ever placements near an artwork in the hour after it
  grows, is damaged or gains an on-canvas link, against matched windows
  without such events.
- *A natural experiment already described.* The Mona Lisa group wrote its
  forum's URL on the canvas in 2017. Within two hours newcomers said they
  had come because of it (Litherland and Mørch, [THEORY-218](../theory.d/THEORY-218.md)). The log
  can show whether first placements near it rose.

## What it can show

- A positive test 2 under exogenous loss would support [CLAIM-274](../claims.d/CLAIM-274.md)'s
  selective part. A positive test 3 would support the recruitment route.
  Either is feedback from pattern to flow, which puts an artwork on the
  candle flame's rung and not the convection cell's ([QUESTION-085](../questions.d/QUESTION-085.md)).
- Test 1 alone fixes whether the decay in [CLAIM-273](../claims.d/CLAIM-273.md) (version 2) cools.
- A null on test 2, with event time controlled and enough exogenous losses,
  is what [CLAIM-274](../claims.d/CLAIM-274.md)'s `defeated_if` names. The claim would then keep
  only its cooling part, and only if test 1 shows it.
- The coalition recovery that test 2 needs bears on [QUESTION-084](../questions.d/QUESTION-084.md). The
  placement log shows who placed together, not who followed whom.

## What it cannot show

- Why anyone stays. Investment in a particular artwork, attachment to a
  community, and enjoying the contest all predict the same retention. Forum
  records ([THEORY-218](../theory.d/THEORY-218.md)) would be needed to separate them.
- Anything about a mind. The owner named the dwindling population as what
  separates r/place from the psychological model ([CLAIM-274](../claims.d/CLAIM-274.md)).
- Facts not yet checked: that atlas outlines exist for 2017 as well as
  2022, and that the moderator rectangles in the 2022 log are removals and
  not other edits. Both should be confirmed against the data before
  analysis.

Nothing has been run.
