---
status: Proposed
title: 'In a simulated sensor network whose correspondences drift, revision improves prediction on positions the network did not choose only when it answers to beacons whose position and channel the revision can neither rewrite nor refuse; revision by the sensors'' disagreement alone restores consistency and not accuracy, and a revisable beacon map or a right to refuse disagreeing beacons loses part or all of the gain'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-177 as a delegated
    lead worker, from the run filed as CASE-tmp33vf4.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-177/network.py such that, once corrected,
  the stated construction gives a different pattern: revision by
  disagreement alone reducing the late error below the fixed network's in
  most seeds, or the anchored arm failing to, or the writable and
  refusing arms matching the anchored one at the stated settings. A network
  with another source of the common drift (a physical constraint, sensors
  that do not drift together) does not defeat it; the claim is about this
  construction.
tags:
- epistemology
- network-science
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-tmp33vf4
corroborates:
- CLAIM-342
complements:
- CLAIM-471
bears_on:
- QUESTION-285
- QUESTION-282
summary: >-
  From [LEAD-177](../leads.d/LEAD-177.md)'s top rung ([CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md)): four sensors, drifting maps, 40
  seeds. Revised by disagreement alone, the network's consistency radius
  returns to normal (0.10) while its error on the target's true positions
  stays where fixed maps leave it (0.40, below fixed in 19 of 40 seeds).
  Revised against beacons the world places, through a channel the revision
  cannot rewrite or refuse, the error returns to its level before the drift
  (0.044, 40 of 40). With the beacon's own map revisable the error is 0.30;
  with the right to refuse beacons that disagree with the current maps, the
  network refuses them all once the drift passes the threshold (error 0.37).
  This is [QUESTION-285](../questions.d/QUESTION-285.md)'s structural condition on G in one construction, and
  independent evidence for [CLAIM-342](CLAIM-342.md). The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp33vf4 — new; the run this claim is drawn from -->

# CLAIM-tmpvqmwc: In a simulated sensor network whose correspondences drift, revision improves prediction on positions the network did not choose only when it answers to beacons whose position and channel the revision can neither rewrite nor refuse; revision by the sensors' disagreement alone restores consistency and not accuracy, and a revisable beacon map or a right to refuse disagreeing beacons loses part or all of the gain

## The claim

[QUESTION-285](../questions.d/QUESTION-285.md) asks what part of an apparatus its own revisions G must not
reach, if revision is to improve prediction on interventions the system did
not choose. In the network of [CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md) the answer has two parts, and
removing either loses the gain:

1. **What G cannot rewrite.** The beacon's position and the map of its
   channel. Made revisable, the beacon becomes one more report to agree with,
   and the error is 0.30 against 0.044.
2. **What G cannot refuse.** Every beacon event is used. Allowed to admit
   only events that agree with its current maps, the network admits 59 of
   300, none after the drift passes the threshold, and keeps a large
   consistency radius that it no longer acts on (error 0.37).

Without any such anchor, revision reduces disagreement and not error: a
common shift of every map changes no residual, so the part of the drift that
moves the whole network is invisible to it. With fixed maps the radius flags
the drift (1.16) and nothing repairs it.

This corroborates [CLAIM-342](CLAIM-342.md), that what keeps a judgement–observation loop
from confirming itself is evidence whose arrival or scoring does not pass
through the interpretation it tests: the writable beacon is the arrival
passing through it, the refusing network the scoring. It complements
[CLAIM-471](CLAIM-471.md), which separates measurement that estimates correspondences from
adaptation that revises them; here adaptation is answerable only when tied to
an estimate it does not control.

## What it does not say

- That an anchor is necessary in general: here it is the only source of the
  common drift's correction.
- That refusal always locks in: with a looser threshold the refusing network
  admits 260 of 300 events and recovers fully. It locks in when the change
  exceeds what the apparatus will admit.
- Anything about beacons the network places itself; that arm was not run.

<!-- inactive-ok-file: CLAIM-tmpw11e6 — Proposed; filed 2026-11-23 -->

## Note of 2026-11-23: the beacon arm not run, now run

This claim's beacons are placed by the world, so they are correct by
construction. With the beacon protected but miscalibrated, the network's
late error equals the miscalibration (0.360 against 0.361), and its
consistency is unchanged. A rarer protected survey of the beacon brings
the error down to 0.122. So protection is necessary here, and it secures
accuracy only relative to the anchor. That qualification is
CLAIM-tmpw11e6, a complement to this claim. The note on CASE-tmp33vf4
gives the table.
