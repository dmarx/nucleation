---
number: 45
status: Active
formerly:
- CASE-tmpazmsq
title: 'Measuring the dancing couple: is the pair a nearly decomposable block during the dance and not after it?'
version: 3
history:
- version: 2
  date: '2026-10-11'
  note: >-
    The direction measurement is reread as an architecture measurement,
    after the objection it was for (CLAIM-173) was rejected
    (CLAIM-167). A one-way coupling no longer counts against the
    pair. It says the pair is a hierarchy, lead driving follow.
- version: 3
  date: '2026-10-11'
  note: >-
    A drive-profile measurement is added (TERM-051), so the study
    can also ask whether "the dance leads": whether the pair's joint mode
    shows causal decoupling, beyond the lead driving the follow.
standing: stipulated
tags:
- embodied-cognition
- individuation
date: '2026-10-11'
line: distributed-agency
variant_of:
- CASE-046
illustrates:
- CLAIM-157
summary: >-
  A proposed study, not run. Motion-capture several couples dancing an
  improvised partner dance to recorded music, and record the same people
  standing and talking after the song. Fit a linear model to the joint
  kinematics, with the music's beat as an exogenous input. Then ask
  whether the pair is a block whose gap beats its Occam factor during
  the dance and not after, whether it compensates under a perturbation,
  and whether the coupling runs both ways.
---
<!-- inactive-ok-file: LIT-902 — Deferred, unread; the source of the compensation test the design borrows, not leaned on -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-167 — Proposed; the claim the study would test and the reply that rereads its direction measurement -->
<!-- inactive-ok-file: CLAIM-173 — Rejected; cited as the objection the measurement was first designed for -->

# CASE-045: Measuring the dancing couple: is the pair a nearly decomposable block during the dance and not after it?

## The case

A stipulated design, so that the criterion has a concrete test.

- **Participants and conditions.** Several experienced couples in an
  improvised partner dance (lindy hop, tango or salsa) to recorded music.
  A control condition records the same two people standing and talking
  after the song. A second control pairs each dancer with a stranger, so a
  practised pair can be compared with a new one.
- **Data.** Motion capture of both dancers' trunks and arms at a rate fast
  enough for the dance's timescale. The music's beat is taken as an
  exogenous input. The target is one-beat-ahead positions.
- **Analysis.** Fit a VAR model to the joint kinematics. Group the
  variables by dancer, and by pair against the rest. Compute the gap that
  separates the pair's block and its Occam factor ([CLAIM-154](../claims.d/CLAIM-154.md)) in each
  condition.
- **Perturbations.** A mild, unannounced resistance applied to one
  dancer's arm. Does the partner compensate within the beat ([LIT-902](../literature.d/LIT-902.md))?
- **Architecture.** Estimate the lead→follow and follow→lead couplings
  separately. Their ratio says whether the pair works as peers or as a
  hierarchy ([CLAIM-167](../claims.d/CLAIM-167.md)).
- **Drive profile.** Take the pair's relative phase as the macro-variable
  and estimate the information decomposition's downward-causation and
  causal-decoupling terms ([LIT-025](../literature.d/LIT-025.md)) over windows ([TERM-051](../terms.d/TERM-051.md)). The
  question is whether the dance has dynamics of its own that neither
  dancer accounts for (decoupling), whether it constrains the dancers
  (downward), or whether it is only their resultant.

## What it can show

- **If the pair clears the threshold while dancing and not after,** the
  owner's claim is a measured result, relative to this target.
- **If the pair clears it but does not compensate,** that counts against
  [CLAIM-157](../claims.d/CLAIM-157.md).
- **If the follow→lead coupling is near zero** while the pair clears the
  threshold, the pair is one system with a hierarchical architecture: the
  lead drives. That is a finding about its structure, not against its
  unity. How far follows feed back, through styling and hijacking, is
  then an empirical question about the dance.

It is stipulated. Nothing here has been run, and the design's choices (the
target, the linear model, the prior variances) are exactly what
[CLAIM-152](../claims.d/CLAIM-152.md) says a verdict is relative to.
