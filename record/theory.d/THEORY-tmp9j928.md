---
status: Proposed
promote_when: >-
  A second reading of the appendix confirms that its example postmortem
  gives technical root causes (a resource leak under exceptional load),
  assigns each action item to an engineer of the responding teams, names
  no decision above those teams, and records the one human error in its
  timeline without naming who made it. Whether real postmortems look like
  this is not asserted.
title: 'Google''s example postmortem traces a fictional outage to a latent bug and a traffic surge, assigns every action item to an engineer of the responding teams, names no decision above them, and records a human error in its timeline without naming who made it'
version: 1
tags:
- software-engineering
- society-and-governance
date: '2026-11-22'
source:
- LIT-tmpnjnwq
bears_on:
- QUESTION-476
summary: >-
  Appendix D of Google's Site Reliability Engineering (2016),
  LIT-tmpnjnwq, read in NOTE-tmpdiani. The template of a blameless
  postmortem, filled in. It bears on QUESTION-476 as the practice's own
  picture of a finished review: blame withheld, correction kept. It is
  fictional and its causes are a bug and a surge, so it cannot show where
  a trace stops when an upstream decision was in play. The wording is the
  filer's (Claude, in this session); adopting it is the owner's call.
---

# THEORY-tmp9j928: Google's example postmortem traces a fictional outage to a latent bug and a traffic surge, assigns every action item to an engineer of the responding teams, names no decision above them, and records a human error in its timeline without naming who made it

Appendix D of *Site Reliability Engineering* (2016), LIT-tmpnjnwq, read
in NOTE-tmpdiani.

## The account

Root causes: "Cascading failure due to combination of exceptionally high
load and a resource leak". Nine action items, each owned by an engineer
named in the timeline, fix the playbook, the load balancing, the leak and
the tests; the one policy item applies the error-budget freeze already in
force. The timeline records "found order-of-magnitude error in whiteboard
calculations for instance count increase", with no agent, while naming who
took each other step.

## Bearing

- **QUESTION-476**: bears on. A blameless review as designed: correction
  without blame, at the level of the teams that responded.

## What it does not show

- Anything about real postmortems, or about decisions above the teams:
  the fictional incident has none to trace.
