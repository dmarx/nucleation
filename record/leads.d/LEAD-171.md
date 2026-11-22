---
number: 171
status: Open
formerly:
- LEAD-tmpurgpv
title: 'Write a threshold version of the crowding-out model'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- society-and-governance
- complex-systems
date: '2026-11-19'
line:
- transient-support
- readiness
advances:
- CLAIM-602
summary: >-
  Named in the curation entry of 2026-11-05 (201805). Filed by the backlog
  audit of 2026-11-19.
---

# LEAD-171: Write a threshold version of the crowding-out model

## What it would do

Model the threshold version.

Where the record names it:

- The curation entry of 2026-11-05 (201805): "stated as a limit of
  [CLAIM-602](../claims.d/CLAIM-602.md), not modelled."

## What would count

A model shows whether the limit stated in [CLAIM-602](../claims.d/CLAIM-602.md) holds.

## Note of 2026-11-22: already held, as CLAIM-605

The lead audit of this date found the threshold version already modelled.
CLAIM-605 (Active, demonstrated), committed about three hours after the
curation entry of 2026-11-05 (201805) that called it "not modelled", adds
the factor C to CLAIM-602's learning term, dC/dt = λPC(1 − C) − μC, which
gives an unstable threshold (C = 0.276 at its parameters) below which
capacity does not regrow. It calls this "the capability trap that
CLAIM-602 named as a limit", Azam et al.'s trap. The script is
scratch/formal/capability_trap_toy.py. What the lead asks is held;
whether to mark it Done is the owner's. No status or stage is changed
here.
