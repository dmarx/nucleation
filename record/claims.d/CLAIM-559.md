---
number: 559
status: Active
formerly:
- CLAIM-tmp4pk8d
title: 'In a sequential decision problem with informative reassessment, provisional activation and subsequent cancellation of a capability can both be optimal under one unchanged objective'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings); ADR-057. CASE-213, which the body never uses, moves from
    grounds to illustrated_by, and rests_on gains CLAIM-561, whose
    expected-loss model supplies the first stage's ΔV(p0) > 0; both are
    Active in the same change. No objection is filed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the two-stage model, or a showing that under its assumptions
  the reversal is impossible: that no belief p0 with ΔV(p0) > 0 can be
  followed, on an informative report, by a belief p1 with
  ΔV_continue(p1, s1) < 0. It is not defeated by cancellations that were
  wrong, or dispatches that were; the claim is that both decisions can be
  right, not that they always are.
tags:
- operations-research
- probabilistic-modeling
- self-governance
date: '2026-11-04'
line:
- readiness
- formal-apparatus
rests_on:
- CLAIM-561
complements:
- CLAIM-535
uses:
- TERM-109
bears_on:
- QUESTION-394
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 6 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)". With an
  initial belief at which dispatch pays and a later report that makes
  continuing not pay, dispatching and then cancelling are each optimal for
  the information held when they are taken. A: "The original dispatch is
  not retrospectively refuted by later cancellation." The wording is A's;
  adopting it is the owner's call.
---

# CLAIM-559: In a sequential decision problem with informative reassessment, provisional activation and subsequent cancellation of a capability can both be optimal under one unchanged objective

## The claim

**Two stages.** At time zero the belief that the capability is needed is
p0, with organizational state s0, and dispatch has expected advantage
ΔV(p0) > 0, as in [CLAIM-561](CLAIM-561.md). After the first unit reports, the
belief is p1 and the state s1, and continuing has expected advantage
ΔV_continue(p1, s1) < 0.

**Both can hold for one incident.** An informative report can move the
belief from above the dispatch threshold to below the threshold for
continuing; for instance, an engine that finds no one trapped moves p
toward 0. The two decisions are made with (p0, s0) and (p1, s1), under
one objective. Each is optimal for what was known when it was taken. In
A's words, "The original dispatch is not retrospectively refuted by later
cancellation," and "appropriate withdrawal of a commitment can be a
successful act of governance."

**What makes it possible** is that the commitment was provisional
([TERM-109](../terms.d/TERM-109.md)): the policy allowed release on new information.

[CLAIM-535](CLAIM-535.md) says which observations a single policy must distinguish for
every circumstance to get an acceptable action. This claim adds the
sequential case: as observations arrive, the acceptable action changes
without the objective changing, so a reversal is not by itself evidence of
an error in either decision.

## What it does not say

- **That all cancellations are appropriate.**
- **That a cancellation shows the dispatch was appropriate.** The
  dispatch is judged at (p0, s0), not by what followed.
- **That real reassessments are informative**, or reliable; the
  construction assumes the report changes the belief in the right
  direction.
