---
status: Proposed
title: 'In a simulated engagement network, only engagement under randomized exposure tells classes inferred, classes used and classes that reshape preferences apart: steering exposure by the classes raises concentration, fit and stability whether or not preferences move; the randomized-exposure gap stays put when preferences are fixed, grows when the classes steer exposure while users and creators adapt, and shrinks under the same adaptation without them'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  In the laboratory as committed, or in a variant that changes only its
  scales (numbers of users and items, rates of adaptation and turnover,
  the strength of steering, K), the randomized-exposure gap moves when the
  classes steer exposure over fixed preferences, or grows as much under
  adaptation without the classes as with them; or a measure computed from
  the policy's own data (concentration, block-model fit to raw counts,
  stability, the closure defect) separates the three arms in the same
  order as the randomized-exposure gap. Not defeated by a real platform
  whose users do not adapt in this way: the claim is about what the
  measures can tell apart, not about any platform.
tags:
- network-science
- social-science
- individuation
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
grounds:
- CASE-tmpw8bs2
bears_on:
- QUESTION-028
- QUESTION-276
summary: >-
  From [LEAD-030](../leads.d/LEAD-030.md)'s run of [CASE-296](../cases.d/CASE-296.md)'s laboratory ([CASE-tmpw8bs2](../cases.d/CASE-tmpw8bs2.md)), four seeds
  in each arm. With genres planted in preferences, the in-class minus
  out-of-class engagement rate under uniform random exposure was 0.35 at
  the start and 0.36, 0.48 and 0.23 after fifteen periods with the classes
  steering exposure over fixed preferences, steering it while users and
  creators adapted, and adaptation without steering. Concentration of
  engagement in the class went from 0.42 to 0.90 in both steered arms. In
  the world where exposure alone made the clusters, the gap moved off zero
  (to 0.024) only when the classes steered exposure with adaptation. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-296 CLAIM-762 CLAIM-327 — Proposed; the case this study runs and the claims it bears on -->
<!-- inactive-ok-file: CASE-tmpw8bs2 — new; the study this claim reports -->

# CLAIM-tmph4j0u: In a simulated engagement network, only engagement under randomized exposure tells classes inferred, classes used and classes that reshape preferences apart: steering exposure by the classes raises concentration, fit and stability whether or not preferences move; the randomized-exposure gap stays put when preferences are fixed, grows when the classes steer exposure while users and creators adapt, and shrinks under the same adaptation without them

## The claim

[CASE-296](../cases.d/CASE-296.md) proposed a laboratory to separate three kinds of class: classes
inferred and never used, classes used to steer exposure while preferences
stay fixed, and classes used while users and creators adapt.
[CASE-tmpw8bs2](../cases.d/CASE-tmpw8bs2.md) ran it, with a fourth arm the lead's criterion needs:
the same adaptation with the classes not used.

- **Inferred against used.** At the end, against the unsteered arm,
  steering had raised concentration (0.40 to 0.90), the block model's fit
  to raw counts (3.6 to 41.1 millinats per cell) and the stability of
  re-inferred classes (0.49 to 0.89). It left
  the randomized-exposure gap where it was, to every digit, because the
  preferences had not moved. Every observational measure registers use.
- **Used against reshaping.** With adaptation the gap rose from 0.35 to
  0.48, and the true gap in engagement probability rose with it (0.34 to
  0.47). Concentration was 0.90 in both arms and cannot tell them apart.
- **Reshaping by use against adaptation alone.** Without steering, the
  same adaptation lowered the gap to 0.23: users drawn toward what they
  engage with, under exposure that crosses genres, drift across them. The
  closure defect turned negative in both adaptive arms, since it registers
  that preferences homogenized within classes, not that the classes
  separated. Only the randomized-exposure gap separated them.
- **Where exposure made the clusters**, the gap was zero and stayed zero
  under every arm but one: steering with adaptation moved it to 0.024
  [0.015, 0.034], against 0.005 [0.000, 0.012] for adaptation alone.

So in this model the classes reshape preferences only when used, which is
what [LEAD-030](../leads.d/LEAD-030.md) said would count for [CLAIM-762](CLAIM-762.md)'s reading, and the
randomized-exposure arm ChatGPT proposed at its review of CASE-296 is
the measure that shows it. Used with adaptation, the class is in this model
[CLAIM-327](CLAIM-327.md)'s self-reinforcing collective variable: the platform reads it,
conditions exposure on it, and by doing so regenerates it.

## What it does not say

That real genres are reshaped. The simulator was built with users who
drift toward what they engage with and a recommender that channels
exposure; the claim is that the laboratory's measures can tell the cases
apart where the cases are known, and which measures cannot. It does not
say how large the effects are on any platform, or that randomized exposure
of 20 items per user is affordable there. It does not say the reshaped
classes are real kinds: whether a class confirmed through its own use is
one is [CLAIM-402](CLAIM-402.md)'s question, and this result is an instance of
CLAIM-402's worry, not an answer to it.
