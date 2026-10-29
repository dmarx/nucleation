---
number: 910
status: Active
formerly:
- THEORY-tmpf8za8
title: "Brown, Price and Dombrovski propose, without a model run or data, that in aversive environments avoiding uncertain states keeps their uncertainty high and so perpetuates avoidance, that anxiety strengthens this loop by misreading noise as change, and that exposure works by reducing the uncertainty rather than an excess of learned threat"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted by the thirteenth status review (ADR-057; ADR-047's
    evidence ruling, read in full in NOTE-1120). The title claims no
    more than the source showed and is unchanged. The promote_when moves
    unchanged to QUESTION-tmp8bdml, as THEORY-285's did to QUESTION-303.
    CLAIM-446 now lists this reading under corroborated_by, not grounds
    (ADR-058): the claim's argument does not rest on it.
tags:
- psychopathology-and-treatment
- learning-and-conditioning
date: '2026-10-24'
source:
- LIT-1479
bears_on:
- QUESTION-tmp8bdml
summary: >-
  Brown, Price & Dombrovski (2023; preprint 2022), [LIT-1479](../literature.d/LIT-1479.md), read in
  full in [NOTE-1120](../notes.d/NOTE-1120.md). A framework stated in words and schematic
  figures: the loop is avoidance, unreduced uncertainty, more avoidance.
  It runs through an uncertainty estimate, a belief, with no authority or
  control variable. For fear-based disorders; by the authors' statement it
  does not explain exposure in GAD.
corroborates:
- CLAIM-446
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim and readings this bears on, named, nothing here rests on them -->

# THEORY-910: Brown, Price and Dombrovski propose, without a model run or data, that in aversive environments avoiding uncertain states keeps their uncertainty high and so perpetuates avoidance, that anxiety strengthens this loop by misreading noise as change, and that exposure works by reducing the uncertainty rather than an excess of learned threat

## Source

Brown, Price & Dombrovski, [LIT-1479](../literature.d/LIT-1479.md), read in full in [NOTE-1120](../notes.d/NOTE-1120.md)
from the NIH author manuscript (PMC10475148): the sections from "The
explore-exploit dilemma and avoidance" to "Practical advantages of
incorporating uncertainty into anxiety treatment", and Figures 3 and 4.

## What was actually shown

Nothing was shown in the sense of a result. The paper argues:

- In aversive environments people shift toward avoiding short-term losses,
  and "normative behavior in uncertain, aversive MDPs will show avoidance
  of uncertain states from increased exploitation of safer states. This
  avoidance maintains high uncertainty and perpetuates avoidance by
  preventing exploration of more uncertain states."
- In anxiety, misreading noise as estimation or unexpected uncertainty
  raises exactly the uncertainty that reduces exploration under threat:
  "Continued avoidance of uncertain states will maintain inappropriately
  elevated uncertainty estimates, ensuring continued avoidance."
- Exposure is forced exploration of the avoided states; it lowers their
  uncertainty, and lower uncertainty in turn favours exploration. Because
  values update at the end of an episode, the update shows between
  sessions, which the authors offer as the reason between-session fear
  reduction predicts outcome.

What could come out otherwise, if tested: avoidance might track the
expected threat of the avoided option and not its uncertainty, or
lowering uncertainty with threat fixed might leave avoidance in place.

## What this does not say

- **That the loop has been demonstrated.** No agent is simulated and no
  participant is tested. The figures are schematics with illustrative
  values.
- **That the threat estimate is wrong.** The account is built so that
  avoidance can persist with a correct expected threat and an inflated
  uncertainty estimate. It is not an excess-threat account.
- **That anything other than a belief maintains the loop.** The variable
  that keeps avoidance going is the uncertainty estimate. There is no
  separate process granted influence over action or sampling.
- **That it covers anxiety in general.** Fear-based disorders only; the
  authors say it does not explain exposure in GAD or eating disorders.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** Supports the step "the defense keeps the uncertainty
  unresolved", and the claim's caution that defensive policy can be
  rational. It is also the belief-maintained rival the claim's defeater
  names: a loop of the same shape with no authority variable. A test of
  the claim has to hold the uncertainty estimate fixed as well as the
  represented threat.
- **[QUESTION-045](../questions.d/QUESTION-045.md).** A candidate maintaining link (avoidance of uncertain
  states) and a candidate cut (exposure), at the level of verbal theory.
- **[THEORY-285](THEORY-285.md).** The same self-sealing shape in active inference, where
  an over-precise prior makes sampling look uninformative. Both are
  model-level; neither has individual data.
