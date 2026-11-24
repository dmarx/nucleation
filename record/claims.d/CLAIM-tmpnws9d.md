---
status: Proposed
title: 'In the salience–realization model of hyperstition, coupling alone never lets a realization outlast its representation: once circulation stops the realization decays at its own rate whatever the gains were; it persists only if the realized organization has a self-maintaining loop of its own strong enough to have a second stable state, and the realization crossed that loop''s threshold while the representation still circulated'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the analysis: a parameter set of the model as stated (A10's
  bounded salience–realization system, with or without an added
  self-maintenance term k r²(1 − r)) in which, after salience is set to
  zero, realization persists although the system for r alone has no stable
  state above zero, or decays although it has one and r had passed its
  threshold.
tags:
- complex-systems
- mathematics
date: '2026-11-24'
line:
- transient-support
- formal-apparatus
rests_on:
- CLAIM-tmpvic6m
summary: >-
  Fills a gap in A10 §9 of the exchange "Memes, Contracts, and Systemic
  Normativity" (ChatGPT, 2026-11-24), which separates a hyperstition whose
  realization outlasts its representation from one that stays dependent on
  it (CLAIM-tmpyp5bu) and leaves telling them apart as "a central research
  question", while its own model (CLAIM-tmpvic6m) contains only the second
  kind. This claim gives the condition for the first in that model, with
  an added self-maintenance term, checked with python3 -I. It is CASE-189's
  transient encounter and maintained connector, in hyperstition's
  variables. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpvic6m CLAIM-tmpyp5bu — Proposed; A's claims filed with this fill from the exchange of 2026-11-24 -->

# CLAIM-tmpnws9d: In the salience–realization model of hyperstition, coupling alone never lets a realization outlast its representation: once circulation stops the realization decays at its own rate whatever the gains were; it persists only if the realized organization has a self-maintaining loop of its own strong enough to have a second stable state, and the realization crossed that loop's threshold while the representation still circulated

## The gap

A10 §9: "A successful hyperstition might ultimately produce something that
no longer needs to be believed in order to exist. The reverse is also
possible ... Distinguishing these outcomes would be a central research
question." A10 §4's model, ṁ = αr − μm, ṙ = βm − νr (and its bounded
version), cannot show the first outcome, and the turn does not say so.

## The claim

1. **Coupling alone.** Set m = 0 from some time on. Then ṙ = −νr in the
   linear model, and ṙ = −0.5r in A10's bounded one: r decays to zero at
   its own rate, whatever α and β were and however far realization had
   gone. Coupling above threshold (CLAIM-tmpvic6m) makes the realization
   grow while the representation circulates; it does nothing for it after.
2. **With a loop of its own.** Add to ṙ a term for the realized
   organization's self-maintenance, k r²(1 − r) (the realization producing
   more of what maintains it). With m = 0, ṙ = r[k r(1 − r) − ν]. A state
   above zero exists exactly when k ≥ 4ν; for k > 4ν there are two, the
   upper stable at r = [1 + √(1 − 4ν/k)]/2 and the lower, the threshold,
   at r = [1 − √(1 − 4ν/k)]/2. Realization outlasts the representation
   exactly when k > 4ν and r is above the threshold when circulation stops.
3. **What withdrawal tells.** Withdrawing circulation after formation
   separates the two outcomes of CLAIM-tmpyp5bu: decay means maintenance
   was the representation's; persistence means it passed to the realized
   organization. Withdrawal before the threshold is crossed ends the
   realization in both kinds of system, so a single withdrawal at an
   unknown stage does not discriminate. This is TERM-100's pair of tests,
   a knockout of upkeep now and an intervention during formation.

**Check.** `python3 -I`, A10's bounded system with α = β = 0.8 and
ν = 0.5, run to t = 200 with circulation, then m = 0 for t = 2000:
k = 0 gives r = 0.375 at withdrawal and 0 after; k = 1.5 (below 4ν = 2)
gives 0.697 and 0; k = 2.5 gives 0.806 and 0.724, the predicted upper
state; k = 3 gives 0.836 and 0.789, predicted 0.789.

## What it does not say

- **Not that the self-maintenance term is the right one.** Any loop that
  gives the realization's own dynamics a second stable state will do; the
  quadratic term is the simplest. CASE-189 builds a richer one.
- **Not that persistence after withdrawal shows the representation was
  true.** It shows where maintenance lies now (CLAIM-402).
