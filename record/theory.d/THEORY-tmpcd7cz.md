---
status: Proposed
promote_when: >-
  An independent replication with the same 2 × 2 logic (shared music
  removed, visual contact removed, each independently) in a new sample,
  ideally from the public data (IIT Dataverse, doi:10.48557/UR2GBG)
  reanalysed under a different movement decomposition, showing that the
  music-driven and partner-driven components stay distinct, that an
  equivalence test bounds their interaction near zero, and that a
  periodicity measure still fails to classify them while a spatial one
  succeeds. It is refuted for the claim of independence if a powered test
  finds an interaction, and for the claim about timing if another temporal
  representation (phase lags, directional measures) does tell the two
  kinds apart. Even if promoted it says nothing about the direction of the
  partner-driven coupling, which the study did not measure.
title: "In dyads of untrained dancers facing each other, shared music and visual contact each raise interpersonal movement synchrony, independently and in different movement components: lateral and hand movements synchronize through seeing the partner, anteroposterior movements such as head bobs through the shared music, and vertical bounce through both; which factor drives a component's synchrony can be read from its spatial direction and not from the timing of the synchrony"
version: 1
tags:
- complex-systems
- embodied-cognition
- social-science
date: '2026-10-23'
source:
- LIT-tmpzp314
answers:
- QUESTION-063
summary: >-
  Bigand, Bianco, Abalde & Novembre (2024), LIT-tmpzp314, read in full in
  NOTE-tmp6hvjr from PubMed Central. A 2 × 2 within-dyad experiment, 35
  dyads, that removes the shared external drive and the coupling channel
  independently and finds synchrony from each in different components, no
  interaction, and a timing signature that cannot tell them apart. It
  answers QUESTION-063 in part: separate interventions on drive and
  channel do discriminate, and a timing-only measure does not. Direction
  of coupling, and a perturbation of one member, are not in it.
---
<!-- inactive-ok-file: QUESTION-063 CLAIM-172 CLAIM-167 CASE-045 THEORY-129 THEORY-275 — Proposed or Open; the question it bears on and the accounts it sits beside, named, not leaned on -->

# THEORY-tmpcd7cz: In dyads of untrained dancers facing each other, shared music and visual contact each raise interpersonal movement synchrony, independently and in different movement components: lateral and hand movements synchronize through seeing the partner, anteroposterior movements such as head bobs through the shared music, and vertical bounce through both; which factor drives a component's synchrony can be read from its spatial direction and not from the timing of the synchrony

## Source

Bigand et al. (2024), LIT-tmpzp314, read in full in NOTE-tmp6hvjr from
PMC11266842 (CC BY), with Figure 2 and Document S1.

## What was actually shown

- **Design.** 70 participants in 35 dyads danced freely, facing each
  other, to 32 trials of eight rearranged songs. "we manipulated musical
  input (whether participants listened to the same or different music,
  presented through earphones) and visual contact (whether participants
  could see or not see each other) in a 2 × 2 factorial design." The
  different-music trials paired songs 8.5% apart in tempo.
- **Measure.** Whole-body motion capture decomposed by PCA into 15
  principal movements (over 95% of variance); synchrony per movement as
  cross-wavelet power between the partners' velocities.
- **Result.** Four movements synchronized more with visual contact, five
  more with shared music, and bounce with both; "we found no evidence of
  an interaction between musical input and visual contact, and this was
  so for all PMs." The spatial direction of the movements classified the
  three categories "with 100% accuracy"; their periodicity did not, and
  "confused 48% of the data associated with music-driven synchrony with
  partner-driven synchrony". The authors: "when (unlike where)
  participants move does not reflect whether synchrony is established
  through music or partner vision."
- **What could have come out otherwise.** The same components might have
  synchronized under both factors, with the music's effect absorbing the
  partner's (an interaction); the categories might have shared a spatial
  signature; or the periodicity might have separated them. None did.

## What this does not say

- **Not the direction of coupling.** The synchrony measure is symmetric.
  That visual contact raises synchrony shows a coupling channel, not that
  the coupling is mutual rather than one partner following.
- **Not that the components are causally sealed off from each other.**
  "Independent" here is the absence of a statistical interaction in this
  sample, not a demonstrated equivalence.
- **Not a general law of synchrony.** One decomposition, one setting:
  untrained familiar pairs, 2.5 m apart, no touch, 40-second songs. The
  authors expect a side-by-side arrangement might reorganize the geometry,
  and give the visibility explanation as unproven.
- **Not that timing can never discriminate.** The negative result is for
  the periodicity profile of synchrony; phase lags or directional
  measures were not tried.

## Which part of QUESTION-063 it answers

QUESTION-063 asks, when a collective outcome such as synchrony can come
from a shared external drive or from coupling among the members, what
measurement tells which architecture produced it. Its "what would answer
it" names two interventions and a statement of which tests can and cannot
see the difference.

- **Answered in part, for one human case.** Removing the shared drive and
  removing the coupling channel, each independently, separates the two
  architectures, and shows that both can operate at once in one pair, on
  different components. A timing-only measure of synchrony could not see
  the difference; a spatial decomposition could. That is a case of the
  question's second requirement: a test (timing) that cannot see it, and
  one (component-wise intervention) that can.
- **Left open.** The question's other intervention, perturbing one member
  and measuring the others, is not done, so direction and peer-versus-
  hierarchy architecture (CLAIM-167, CLAIM-172) are not settled. Nor is
  a test for a shared drive that is unrecorded, which is what the
  question's own limits on THEORY-275 point to: here the drive was the
  experimenter's music, known and manipulable. And the second part of the
  question, telling one internal route to an outcome from another, is not
  touched.

The question stays Open. A Proposed THEORY cannot make it Answered
(ADR-049).

## Connections

- **CASE-tmpg5qs0** documents the study as the record's case, and bears on
  the proposed study CASE-045, which already takes the music's beat as an
  exogenous input; this result says to expect the music and the partner
  to drive different components.
- **THEORY-129** is the shared-cue half in coral spawning, with coupling
  untested; this study tests both halves in one system.
- **THEORY-275**: there, a directional measure follows a recorded drive and
  misreports symmetric coupling. Here, a timing measure cannot apportion
  synchrony between drive and coupling. Both are cases of an observational
  test failing where an intervention succeeds.
