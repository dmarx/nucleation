---
number: 171
status: Done
formerly:
- LEAD-tmpurgpv
title: 'Write a threshold version of the crowding-out model'
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Done, at the owner's go-ahead of 2026-11-25 ("go ahead with the
    reruns"), whose brief for the recomputation pass of LEAD-tmpc0rqa
    took in closing the leads whose runs are recorded and meet their
    own "What would count", as housekeeping and not a change of
    credence. What would count, a model that shows whether CLAIM-602's
    limit holds, is held: CLAIM-605 (Active, demonstrated) is the
    threshold version, with an unstable threshold below which capacity
    does not regrow (the note of 2026-11-22). The stage is left as it
    stood.
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

## Note of 2026-11-22: already held, as [CLAIM-605](../claims.d/CLAIM-605.md)

The lead audit of this date found the threshold version already modelled.
[CLAIM-605](../claims.d/CLAIM-605.md) (Active, demonstrated), committed about three hours after the
curation entry of 2026-11-05 (201805) that called it "not modelled", adds
the factor C to [CLAIM-602](../claims.d/CLAIM-602.md)'s learning term, dC/dt = λPC(1 − C) − μC, which
gives an unstable threshold (C = 0.276 at its parameters) below which
capacity does not regrow. It calls this "the capability trap that
[CLAIM-602](../claims.d/CLAIM-602.md) named as a limit", Azam et al.'s trap. The script is
scratch/formal/capability_trap_toy.py. What the lead asks is held;
whether to mark it Done is the owner's. No status or stage is changed
here.

## Note of 2026-11-25: closed

Closed as Done in the recomputation pass of LEAD-tmpc0rqa (history, version 2). The lead's model is CLAIM-605, Active, as the audit of 2026-11-22 found; nothing remains of the lead. The note is the assistant's (Claude, in this session).
