---
number: 1114
status: Active
formerly:
- CLAIM-tmpiwxla
title: 'Response time is a property of the route'
statement: >-
  Where a response runs through stages that do not compete for a shared
  resource, its time is a property of the route, stages in sequence adding
  their times, stages that overlap contributing the longest of theirs and a
  stage completed before the contingency contributing nothing, so the
  slowest component bounds the response time only when it lies on the route
  and is still to be done
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-252). Rechecked by a session other than the filer's
    with a kept script and a seed,
    scratch/formal/critical_path_route_check.py (seed 1114): on 20,000
    random routes built in sequence and in parallel to depth four,
    with a quarter of the stages done in advance, the finish time by
    event simulation on the precedence graph equals the rule in every
    case, and a one-server control breaks it. The entry's count of
    2,037 depends on a generator it does not state; this run gives
    1,596. ADR-057: it rests on no claim and grounds on nothing; it
    uses TERM-085, Active; no objection targets it; and nothing meets
    its defeated_if.
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
  to [TERM-085](../terms.d/TERM-085.md)''s split of the time to correct. Checked with python3 -I. The wording
  is the assistant''s (Claude, in this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-711 CLAIM-423 CASE-316 — Proposed; the claims the manuscript's join also uses, and the case of competing stages -->

# CLAIM-1114: Response time is a property of the route

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
the contingency. [TERM-085](../terms.d/TERM-085.md)'s "discovery, verification, coordination and
execution" are such stages; its note on Hutchins, that preparation "moves
the cost of search ahead of the deadline", is the third clause.

With random durations the construction holds sample by sample, so the
readiness curve of [TERM-115](../terms.d/TERM-115.md) is the distribution of that longest chain,
and the mean of a maximum exceeds the maximum of the means.

## The check

With python3 -I: 20,000 random routes built in sequence and in parallel
to depth four, durations uniform on [0, 10], a quarter of the stages done
in advance. Event times computed by precedence equalled the rule in every
case. In 2,037 of them the slowest stage had been done in advance and the
response time was below its duration.

## What it does not say

- Nothing where stages compete. [TERM-085](../terms.d/TERM-085.md)'s stages "overlap and compete":
  stages sharing reviewers or a budget can take longer than the longest of
  them, up to their sum on one server, as [CASE-316](../cases.d/CASE-316.md)'s saturated reviewers
  show.
- Not the manuscript's join JC8 as a whole: that a commitment set slowly
  can be applied fast ([CLAIM-711](CLAIM-711.md)), or that speed does not settle authority
  ([CLAIM-423](CLAIM-423.md)), which is more than this construction.

## Gap filled

A gap of the manuscript governance-of-possibility, §10.3 (GC8): "stages
done in sequence add their times; stages that overlap contribute their
maximum; a stage completed before the contingency contributes nothing."

## Note of 2026-11-23: restated for parallel inquiry

<!-- inactive-ok-block: CLAIM-1004 — new; the entries filed from "Explain First Contact RL", U28 and A54 -->
A54 §2 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23), on the owner's conjecture that parallel processing complicates the joint boundary of inquiry and response ([CLAIM-1004](CLAIM-1004.md)), restates this construction for three inquiries of 3, 4 and 5 days: 12 in sequence, "approach" 5 in parallel; it checks. A54 adds what the construction leaves aside: parallelism "can reduce **calendar-time latency** while increasing the amount of **simultaneously committed capacity**", and "a centralized approval process may remain the bottleneck even if all inquiry streams operate independently", which is this claim's exclusion of stages that compete. The joint set of questions an organization can pose and answer, which depends on this route structure and not only on the two frontiers, is [CLAIM-1025](CLAIM-1025.md); the three sources of coupling are [CLAIM-1157](CLAIM-1157.md). No status change.

## Note of 2026-11-25: rechecked with a kept script and a seed

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-252](../leads.d/LEAD-252.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). The stated check gave no seed and was not kept (the manuscript governance-of-becoming, G5.9). It was rebuilt from "The check" above as `scratch/formal/critical_path_route_check.py` (standard library, seed 1114), run with python3 -I: 20,000 random routes, each node a stage (duration uniform on [0, 10], done in advance with probability 1/4) or a sequence or parallel block of two or three sub-routes, to depth four. The finish time from an event simulation on the precedence graph each route defines equals the rule (sequence adds, overlap takes the longest, a stage done in advance adds nothing) in all 20,000. In 1,596 of them the slowest stage had been done in advance and the response time was below its duration; the entry's 2,037 came from a generator whose branching it does not state, so the count is not comparable and the rule is what reproduces. A negative control runs three stages of 3, 4 and 5 on one server, where they compete: 12, not the rule's 5. Promoted in the same pass (history, version 2). That frees [CLAIM-1157](CLAIM-1157.md), rerun on 2026-11-25 and held back only by this claim, and through it [CLAIM-1025](CLAIM-1025.md), [CLAIM-1008](CLAIM-1008.md) and [CLAIM-1203](CLAIM-1203.md); their promotion is the next status step and is not taken here. The note is the assistant's (Claude, in this session).
