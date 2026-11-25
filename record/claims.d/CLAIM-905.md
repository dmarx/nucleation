---
number: 905
status: Proposed
formerly:
- CLAIM-tmpst09o
title: 'Postmortems rarely trace causes above the team'
statement: >-
  In a pilot coding, public postmortems of software incidents rarely trace a
  contributing cause to a decision above the engineering team, or target one
  in an action item, while Chemical Safety Board investigations of chemical
  accidents mostly do both: the direction a stopped blameless trace
  predicts, not yet separated from domain, severity or publication
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A recoding of the same 40 documents under the committed codebook by a
  coder independent of the assistant, in which the internal arm's rates of
  causes or action items above the team come within 15 points of the
  independent arm's; or a larger sample under the same sampling rule in
  which they do. Not defeated by a matched study in which the difference
  vanishes when domain and severity are held fixed: that would defeat the
  inference from this finding to CLAIM-750, not the finding itself, which
  states the difference only for these corpora and names those confounds.
tags:
- society-and-governance
- software-engineering
date: '2026-11-22'
line:
- rightful-power
- organizational-normativity
bears_on:
- QUESTION-476
grounds:
- CASE-335
corroborates:
- CLAIM-750
summary: >-
  The finding of the pilot filed as [CASE-335](../cases.d/CASE-335.md), run for [LEAD-119](../leads.d/LEAD-119.md). Of 30
  postmortems drawn at random from a public list, 2 name a decision above the
  engineering team among their causes and 4 have an action item above it. Of
  the 10 most recent completed CSB investigations, 7 and 9 do, and the CSB
  reports name corporate governance, corporate oversight, funding and
  regulatory gaps, none of which any postmortem names. The direction is the
  one [CLAIM-750](CLAIM-750.md) predicts, met under a decision rule fixed before coding. It
  corroborates [CLAIM-750](CLAIM-750.md) weakly. The arms differ in domain, severity and
  publication as well as in who reviews. There was one coder, of the same
  model family that wrote [CLAIM-750](CLAIM-750.md), so the pilot is not independent. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-750 — Proposed; the claim this finding corroborates -->
<!-- inactive-ok-file: CASE-335 — new; filed with this claim -->

# CLAIM-905: Postmortems rarely trace causes above the team

## The claim

In the pilot ([CASE-335](../cases.d/CASE-335.md)), causes reach above the engineering team in 2 of the 30 public postmortems and in 7 of the 10 CSB reports. They reach corporate leadership in none of the postmortems and in 5 of the reports. Action items reach above the team in 4 of the postmortems and 9 of the reports. A cause stated as "the system" with no decision named occurs in 12 of the 30 postmortems. One postmortem says outright that "a security incident is a systems failure", moving the account from the employee to the system, which is the move [CLAIM-750](CLAIM-750.md) is about.

## Why a claim

[QUESTION-476](../questions.d/QUESTION-476.md) asks whether blameless practice keeps the upstream provenance that blame supplies. [CLAIM-750](CLAIM-750.md) answers that it does only where its trace crosses the authority of the body that commissions it, and it predicts a difference between internal and independent reviews. Until now no coded corpus bore on that prediction. This pilot is the first, and the difference it finds runs in the predicted direction and is large. The finding is held as a claim, apart from [CLAIM-750](CLAIM-750.md), so that it can be revised on recoding without [CLAIM-750](CLAIM-750.md) being revised with it.

## What it does not say

- **Not that the difference comes from who commissions the review.** The internal arm is software outages, published for customers. The independent arm is fatal or serious chemical accidents, investigated by a public body. Domain, severity and publication genre are not separated from commissioning body. A matched design is [CASE-293](../cases.d/CASE-293.md)'s, with internal and independent reviews of the same incidents, or of incidents of one domain.
- **Not independent evidence in the strict sense.** One coder, of the same model family that wrote [CLAIM-750](CLAIM-750.md) and the codebook, coded with the prediction known. The defeater names a recoding by an independent coder for that reason.
- **Not about completion.** Whether action items above the team are carried out is not measured.
