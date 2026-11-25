---
number: 1259
status: Proposed
formerly:
- CLAIM-tmpc3ndh
title: 'Where competence decays without funded maintenance, a capability is committed only when competent enough and its budget follows observed use, a rarer capability is lost sooner at the same expected funding: its time to loss is stochastically shorter, not only the lower bound on its chance of loss higher'
version: 1
history:
- version: 1
  date: '2026-11-24'
  note: >-
    Filed at the status pass of 2026-11-24, at the owner's word ("handle
    the fixes for the twelve ... use your best judgement"), as the clause
    CLAIM-921's narrowing dropped: its old title said "so at the same
    expected funding a rarer capability is lost sooner", which its
    derivation does not show (its step 2 is a lower bound). The record's
    own extrapolation, so a Proposed interpretive claim resting on the
    narrowed entry (status-review README, narrowing kind 2).
role: thesis
warrant: interpretive
defeated_if: >-
  In CASE-343's model, or in any model with the three processes of
  QUESTION-386 and a threshold on commitment, two rarities at the same
  expected funding, with the base budget sustaining competence below the
  threshold, at which the rarer capability's chance of loss within some
  horizon is lower, beyond sampling error; or a derivation that the
  ordering fails for some parameters of that model.
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-24'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-921
grounds:
- CASE-343
bears_on:
- QUESTION-386
summary: >-
  The ordering [CLAIM-921](CLAIM-921.md)'s title once stated, kept as its own Proposed
  claim when that title was narrowed to the lower bound its derivation
  gives. [CASE-343](../cases.d/CASE-343.md) observes it at the rarities it ran (loss within thirty
  years in every run at one occasion in five or in two and a half years,
  93 % at one a year, 39 % at four, under 1 % at sixteen, with ηλ fixed),
  and there most of the loss at moderate rarity runs through partial
  commitment, which the bound does not cover. No derivation of the
  ordering is held. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CLAIM-1259: Where competence decays without funded maintenance, a capability is committed only when competent enough and its budget follows observed use, a rarer capability is lost sooner at the same expected funding: its time to loss is stochastically shorter, not only the lower bound on its chance of loss higher

## The claim

In [CLAIM-921](CLAIM-921.md)'s model (A's model from [QUESTION-386](../questions.d/QUESTION-386.md), with a threshold on
commitment), hold ηλ fixed so that a capability used on every occasion
earns the same on average, and let occasions grow rarer. [CLAIM-921](CLAIM-921.md) derives
that the lower bound on the chance of loss within T periods,
1 − (1 − e^(−λL))^⌊T/L⌋, rises as λ falls. This claim says more: that the
chance of loss within every horizon rises as λ falls, so that time to loss
is stochastically shorter for the rarer capability.

The evidence is [CASE-343](../cases.d/CASE-343.md)'s sweep, in which loss frequencies within thirty
years fall monotonically from every run at one occasion in five years to
under 1 % at sixteen a year, and in which averaging the activity over a
year lowers them "without changing the ordering". At one occasion a year
and more often the bound accounts for little of the loss (0.04 against
0.93 observed): there the path runs through partial commitment, a
capability committed less, funded less and so weaker still. That path is
the reason to expect the ordering beyond the bound, and the reason no
derivation of it is yet held.

## What it does not say

- That the ordering holds where the base budget alone sustains competence
  at or above the threshold; there nothing is lost for good ([CLAIM-921](CLAIM-921.md),
  step 4, and [CASE-343](../cases.d/CASE-343.md) at B̄ = 1.35).
- That it holds at every horizon in models other than [CASE-343](../cases.d/CASE-343.md)'s; the
  sweep checked one horizon, thirty years, at five rarities.

## Note of 2026-11-24: what holds it back

A derivation of the ordering, or a sweep of [CASE-343](../cases.d/CASE-343.md)'s model over horizons
and over B̄ and the commitment ramp, is missing; one horizon at five
rarities is what is observed.
