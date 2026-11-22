---
status: Proposed
title: 'A simulated sensor network whose correspondences drift: revising them to reduce the sensors'' disagreement restores consistency and not accuracy, revising them against beacons the world places through a channel the revision cannot rewrite or refuse restores accuracy, and a revisable beacon map or a right to refuse disagreeing beacons gives back part or all of the gain'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-177 as a delegated
    lead worker. The code, its tests and the results are committed under
    scratch/studies/lead-177/.
standing: documented
kind: executed-study
tags:
- epistemology
- network-science
- probabilistic-modeling
date: '2026-11-22'
line:
- distributed-agency
draws_on:
- THEORY-1077
- THEORY-1088
illustrates:
- CLAIM-342
bears_on:
- QUESTION-285
- QUESTION-282
summary: >-
  The top rung [LEAD-177](../leads.d/LEAD-177.md) asked for: a sensor network revising its
  correspondences, as [QUESTION-285](../questions.d/QUESTION-285.md)'s answer 3 proposes for Robinson's networks,
  whose correspondences are fixed. Four sensors report a moving target through
  maps that drift (a slow walk of every bias and, at step 500, a jump and a
  rotation of one sensor). The apparatus fuses by least squares and reports its
  consistency radius; 40 seeds, 3,000 steps. Fixed maps: late error 0.40,
  radius 1.16 (the radius flags the trouble). Revised by disagreement alone:
  radius 0.10, error 0.40, no better than fixed in 21 of 40 seeds. Revised
  only against beacons the world places, through a channel the revision cannot
  touch: error 0.044, as before the jump, in 40 of 40 seeds; sparser beacons
  give less (0.095 and 0.24). The beacon as one more revisable map: 0.30.
  Beacons admitted only when they agree with the current maps: 59 of 300
  admitted, error 0.37; with a looser threshold, 260 admitted and error 0.045.
  The run makes [QUESTION-285](../questions.d/QUESTION-285.md)'s structural condition concrete in one
  construction. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpz762n CLAIM-tmpvqmwc — new; the companion run and the claim filed from this one -->

# CASE-tmp33vf4: A simulated sensor network whose correspondences drift: revising them to reduce the sensors' disagreement restores consistency and not accuracy, revising them against beacons the world places through a channel the revision cannot rewrite or refuse restores accuracy, and a revisable beacon map or a right to refuse disagreeing beacons gives back part or all of the gain

## What was done

[QUESTION-285](../questions.d/QUESTION-285.md) asks, for the top rung, for "a structural condition on G, the
part of the apparatus its own revisions cannot reach, under which revision
improves prediction on interventions the system did not choose, and without
which it does not", and proposes Robinson's distributed sensor networks
([NOTE-1221](../notes.d/NOTE-1221.md)) as the test bed "once their correspondences are allowed to be
revised". [LEAD-177](../leads.d/LEAD-177.md) asks for that network as the ladder's top rung; the lower
rungs are [CASE-tmpz762n](CASE-tmpz762n.md). Code and results: scratch/studies/lead-177/
(`network.py`, `results/network_summary.md`).

A target moves in a 6 × 6 box. Four sensors report o_i = A_i z + b_i + noise
(sd 0.05). The apparatus holds correspondences (Â_i, b̂_i), starting correct,
fuses by least squares (the nearest global section) and computes its
consistency radius, the largest residual ([THEORY-1077](../theory.d/THEORY-1077.md)). The true maps drift:
every bias walks (sd 0.004 a step), and at step 500 one sensor's bias jumps by
(1.0, −0.6) and its gain rotates by 20°. Error is measured on the target's
true positions, which no arm sees. Late is the last 1,000 of 3,000 steps.

| arm | what the revision may not rewrite | error before the jump | late error | late radius | late error below fixed (seeds) |
|---|---|---|---|---|---|
| fixed | everything (no revision) | 0.063 | 0.399 | 1.155 | – |
| self | nothing outside the reports: maps revised to reduce disagreement | 0.062 | 0.402 | 0.102 | 19/40 |
| self, slower | as above, learning rate 0.005 | 0.062 | 0.408 | 0.134 | 17/40 |
| anchored | a beacon every 10 steps at a position the world draws, given through a channel G cannot revise or refuse | 0.045 | 0.044 | 0.114 | 40/40 |
| anchored, every 50 | as above | 0.055 | 0.095 | 0.241 | 39/40 |
| anchored, every 200 | as above | 0.060 | 0.241 | 0.649 | 34/40 |
| writable | the beacon is one more sensor, its map revised by disagreement | 0.061 | 0.302 | 0.114 | 30/40 |
| admitted | the protected channel, but an event is used only if its residual is under 0.3 | 0.045 | 0.369 | 1.070 | 22/40 (59 of 300 admitted) |
| admitted, looser | threshold 1.0 | 0.045 | 0.045 | 0.117 | 40/40 (260 of 300) |

## What it can show

- **Consistency without accuracy.** Revision by disagreement brings the
  radius back near its level before the jump (0.10 against 0.09) and leaves
  the error where fixed maps leave it. A common shift of every map, with the state shifted back, changes no
  residual (a test checks it), so disagreement cannot see the part of the drift
  that moves the whole network. This is [THEORY-1088](../theory.d/THEORY-1088.md)'s "learning to lie" in a
  sensor network, with no collapse needed: the guards that stop collapse do
  not make the apparatus answerable.
- **The condition, in one construction.** Revision improves prediction on
  positions the apparatus did not choose when it answers to something it
  cannot rewrite (the beacon's position and its channel) and cannot decline
  (every event is used). Make the beacon's map revisable and much of the gain
  goes (0.30); let the apparatus refuse events it disagrees with and, once
  the drift exceeds the threshold, it refuses them all and keeps a large
  radius it no longer acts on (0.37). That is [CLAIM-342](../claims.d/CLAIM-342.md)'s condition, evidence
  whose arrival or scoring does not pass through the interpretation it tests,
  with each half of it removed in turn. It is [CLAIM-tmpvqmwc](../claims.d/CLAIM-tmpvqmwc.md).
- **The fixed network's radius is a detector, not a repair.** It rises to
  1.16 and flags the drift, as in Robinson's paper ([NOTE-1221](../notes.d/NOTE-1221.md)), and nothing
  acts on it.

## What it cannot show

- That the condition is necessary in general. Here the anchor is the only
  route to the common part of the drift; a network with another source of
  scale or position (a physical constraint, redundant independent sensors that
  do not all drift together) might do without it.
- How the threshold result generalizes: refusal locks in only when the change
  exceeds the threshold, and a looser threshold admits enough to recover.
- Anything about who places the beacons. Here the world draws them; a
  network that chose its own beacon positions was not run, so "interventions
  the system did not choose" is met by construction and not tested against
  its contrary.
