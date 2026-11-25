---
number: 903
status: Active
formerly:
- CLAIM-tmpo7igy
title: 'Passive tests cannot tell drive from coupling'
statement: >-
  In a network of oscillators, passive tests of timing and of gluing cannot
  tell a shared drive from coupling among the members, while displacing the
  drive for one member only, perturbing one member, or withdrawing the drive
  can; and a revision of the correspondence maps that only restores
  consistency makes an apparatus coherent without making it predict
  interventions it did not choose
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-tmpc0rqa). ADR-057: its one ground, CASE-333, was rerun by a
    session other than the filer's and promoted in the same pass; it
    rests on no claim; no objection targets it; and the rerun meets
    none of its defeated_if (the uncoupled members follow the
    displaced drive by 0.002, against 0.30 and 0.58 coupled, and
    revision to the observed offsets leaves the held-out error
    unchanged). Every figure in the summary matches the rerun.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of the study, or a variant within its model family (other
  graphs, frequency spreads, noise levels, drive strengths in the locking
  range), in which the phase-locking value or the holonomy of the observed
  offsets separates the uncoupled and the coupled driven networks by a
  margin comparable to the displacement and perturbation readouts; or in
  which displacing one member's drive moves the uncoupled members by a
  comparable fraction; or in which a revision of the maps to the observed
  offsets improves prediction of held-out interventions. Not defeated by
  the point that a real system's drive may be unrecorded or its members
  unequal: the claim is an existence result in the model, and says so.
tags:
- complex-systems
- causality
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-333
bears_on:
- QUESTION-063
- QUESTION-035
corroborates:
- CLAIM-474
summary: >-
  From the run of [CASE-179](../cases.d/CASE-179.md)'s design for [LEAD-098](../leads.d/LEAD-098.md) ([CASE-333](../cases.d/CASE-333.md)). Under
  a shared drive, eight uncoupled and eight coupled oscillators lock
  alike (phase-locking value 0.9985 and 0.9996) and their observed
  offsets glue alike. Displacing one member's drive moves the others by
  0.2 per cent of its shift without coupling and 30 to 58 per cent with
  it; a kick reaches the others at 0.010 against 0.12 to 0.14; withdrawal
  leaves order 0.47 against 0.996. A coupling fitted to passive
  fluctuations with the drive unrecorded finds a spurious gain a quarter
  of the true one. Maps revised to the observed offsets reach coherence
  and leave prediction unchanged; gains checked against held-out kicks
  find the coupling where it is and none where it is not. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-616 — Proposed; the laboratory claim this result bears on -->

# CLAIM-903: Passive tests cannot tell drive from coupling

## The claim

Three parts, each shown in [CASE-333](../cases.d/CASE-333.md).

1. **Passive tests are blind to the architecture.** A shared drive that
   realizes the apparatus's maps brings uncoupled units to the same phase
   locking and the same glued offsets as coupling does. [QUESTION-035](../questions.d/QUESTION-035.md)'s
   entrainment-by-timing and gluing tests pass both. A coupling strength
   fitted to fluctuations misreads a shared drive as weak coupling unless
   the drive is recorded and its pull is modelled.
2. **The interventions [QUESTION-063](../questions.d/QUESTION-063.md) asks for are not blind.** Displacing
   the drive for one member and perturbing one member separate the two
   by a factor of more than a hundred and of more than ten, and the
   response falls off along the graph. Withdrawing the drive separates
   them too, but also separates self-sustained from damped units, so it
   answers a different question as well (A12's arm; [CASE-225](../cases.d/CASE-225.md)).
3. **Consistency is not knowledge.** Revising the maps to whatever
   offsets are observed makes an apparatus coherent with the system in
   every arm and changes none of its predictions. Revision checked
   against interventions the apparatus did not choose is what improves
   them.

## What it does not say

- That a real system's architecture can be read this way. The drive here
  is known to the experimenter, the graph is known and small, the units
  alike. An unrecorded drive acting on members unequally is [QUESTION-063](../questions.d/QUESTION-063.md)'s
  open case.
- That coupling makes the members one system. It is [CLAIM-172](CLAIM-172.md)'s
  criterion that the perturbation readout operationalizes; whether that
  criterion is [QUESTION-035](../questions.d/QUESTION-035.md)'s answer is another matter.
- That the oscillator results transfer to organizations ([CLAIM-616](CLAIM-616.md)'s own
  reservation).

## Bearing

It gives [QUESTION-063](../questions.d/QUESTION-063.md) a constructed answer for oscillator networks, and
the statement [QUESTION-063](../questions.d/QUESTION-063.md) asks for of which of [QUESTION-035](../questions.d/QUESTION-035.md)'s tests can
see the difference. It adds a constructed case to [CLAIM-474](CLAIM-474.md)'s partial
order, for the separation of compatibility, dynamics and inquiry. For
[CLAIM-616](CLAIM-616.md), it is a run whose arms could have come out otherwise: the
uncoupled members could have followed the displaced drive, and the
knocked-out unit's loss could have shown in its output.

## Note of 2026-11-25: rerun by a session other than the filer's

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-tmpc0rqa](../leads.d/LEAD-tmpc0rqa.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). [CASE-333](../cases.d/CASE-333.md)'s study was regenerated from nothing (its note of this date): every item agrees with the stored results but timings, and every figure this claim quotes matches: phase-locking 0.9985 and 0.9996, displacement followed by 0.2, 30 and 58 per cent, kicks reaching the others at 0.010 against 0.12 to 0.14, withdrawal orders 0.47 and 0.996, the passive fit's spurious gain 0.068 against the true 0.3, and maps revised to the observed offsets reaching coherence (incompatibility 10⁻⁶ to 2 × 10⁻⁵) with the held-out error unchanged, while gains checked against held-out kicks find 0.001, 0.29 and 0.90. The factors in part 2 are 0.30/0.0022 ≈ 136 and 0.117/0.0102 ≈ 11.5. Promoted in the same pass (history, version 2). The note is the assistant's (Claude, in this session).
