---
status: Open
title: Extend the oversight queueing model with an affected party who petitions
  to revise a precommitted limit and a revision process of its own speed, and measure
  the harm done to that party before the limit can be revised against the speed
  of application
version: 1
stage: specified
method:
- formal
tags:
- society-and-governance
- operations-research
date: '2026-11-23'
line:
- distributed-agency
- dependence-and-domination
advances:
- CLAIM-730
- CLAIM-879
summary: 'A gap of the manuscript governance-of-possibility, §7.2 (GB7): CASE-316''s
  model "has no affected party and never revises a limit", so CLAIM-730''s first
  clause is untested. The design is fixed here. The wording is the assistant''s
  (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-730 CLAIM-879 CASE-316 — Proposed; what this would test and the model it extends -->

# LEAD-tmp2npy0: Extend the oversight queueing model with an affected party who petitions to revise a precommitted limit and a revision process of its own speed, and measure the harm done to that party before the limit can be revised against the speed of application

## The design

Start from CASE-316's model unchanged: actions at 2 a day, one in ten
objectionable, irreversibility gamma with shape 4 and mean 30/s days,
four reviewers, the precommitted-limits variant with coverage q = 0.8.
Add:

1. **A blind spot.** A class of actions, 5 per cent of all, falls inside
   the limits and harms an affected party P. The overseer's ordinary
   review does not class them objectionable.
2. **The affected party.** P notices each harm after an exponential delay,
   mean 5 days, and after its third harm files a petition to revise the
   limit.
3. **Revision.** A petition waits a revision time, gamma with shape 4 and
   mean τ_rev; once revised, the limits cover the class.
4. **Arms.** Speed s ∈ {1, 3, 10}, latency and throughput readings as in
   CASE-316; τ_rev ∈ {10, 90, 365} days; and a revision-on-demand arm in
   which a petition suspends the class at once pending revision.

20 seeds per configuration, shared across arms. Measure the harms to P
that become irreversible before revision, per thousand actions, and
reviewer load, since escalations share the reviewers.

## Checks the record can run

- **CLAIM-730's first clause** predicts that, at fixed τ_rev, the harm to P
  before revision rises with s. If it does not, the clause fails in the
  model.
- **Its second clause** predicts that revision on demand brings the harm
  back toward the slow arm's level. If a petition channel at the same
  τ_rev does as well as suspension, the domination is not from the
  separation of speeds.
- **Negative control:** with τ_rev → 0 the harm must equal the slow arm's.
