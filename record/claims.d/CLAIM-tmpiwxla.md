---
status: Proposed
title: Where a response runs through stages that do not compete for a shared resource,
  its time is a property of the route, stages in sequence adding their times, stages
  that overlap contributing the longest of theirs and a stage completed before
  the contingency contributing nothing, so the slowest component bounds the response
  time only when it lies on the route and is still to be done
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the construction; or a route of stages that share no resource
  whose completion time differs from the longest chain of its stages still to be
  done.
tags:
- operations-research
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- readiness
- distributed-agency
uses:
- TERM-085
summary: 'A gap fill: a gap of the manuscript governance-of-possibility, §10.3 (GC8),
  "The simple part could be shown by construction". It is the critical path, applied
  to TERM-085''s split of the time to correct. Checked with python3 -I. The wording
  is the assistant''s (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-711 CLAIM-423 CASE-316 — Proposed; the claims the manuscript's join also uses, and the case of competing stages -->

# CLAIM-tmpiwxla: Where a response runs through stages that do not compete for a shared resource, its time is a property of the route, stages in sequence adding their times, stages that overlap contributing the longest of theirs and a stage completed before the contingency contributing nothing, so the slowest component bounds the response time only when it lies on the route and is still to be done

## The construction

A route from detection to completed action is a set of stages, each with a
duration, and a precedence: a stage starts when every stage it needs has
finished. A stage done before the contingency has duration 0 from the
contingency on. If no two stages that run at the same time compete for a
resource, each finishes at its start plus its duration, and by induction
on the route's structure:

- **in sequence**, the finish is the start plus the sum of the durations;
- **overlapping** (started together, the route going on when all are
  done), the finish is the start plus the largest duration;
- **done in advance**, a stage adds nothing.

For a general precedence graph the response time is the longest chain of
stages still to be done: the critical path. So a stage of duration d on
the route and still to be done makes the response time at least d, and a
stage done in advance, however slow, gives no bound. The slowest component
sets the response time only when it is on the critical path at the time of
the contingency. TERM-085's "discovery, verification, coordination and
execution" are such stages; its note on Hutchins, that preparation "moves
the cost of search ahead of the deadline", is the third clause.

With random durations the construction holds sample by sample, so the
readiness curve of TERM-115 is the distribution of that longest chain,
and the mean of a maximum exceeds the maximum of the means.

## The check

With python3 -I: 20,000 random routes built in sequence and in parallel
to depth four, durations uniform on [0, 10], a quarter of the stages done
in advance. Event times computed by precedence equalled the rule in every
case. In 2,037 of them the slowest stage had been done in advance and the
response time was below its duration.

## What it does not say

- Nothing where stages compete. TERM-085's stages "overlap and compete":
  stages sharing reviewers or a budget can take longer than the longest of
  them, up to their sum on one server, as CASE-316's saturated reviewers
  show.
- Not the manuscript's join JC8 as a whole: that a commitment set slowly
  can be applied fast (CLAIM-711), or that speed does not settle authority
  (CLAIM-423), which is more than this construction.

## Gap filled

A gap of the manuscript governance-of-possibility, §10.3 (GC8): "stages
done in sequence add their times; stages that overlap contribute their
maximum; a stage completed before the contingency contributes nothing."
