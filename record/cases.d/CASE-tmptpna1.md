---
status: Proposed
title: 'Priority inversion on one preemptive processor: a high-priority process blocked on a lock held by a low-priority one misses its deadline under fixed priorities, because a medium-priority process preempts the holder, and meets it under priority inheritance, which moves the delay onto the medium-priority process'
version: 1
standing: stipulated
kind: construction
tags:
- software-engineering
- operations-research
- agency
date: '2026-11-24'
line:
- will-organization
- distributed-agency
illustrates:
- CLAIM-tmpkvzcn
- CLAIM-tmpe6yfm
- CLAIM-283
- CLAIM-357
summary: >-
  A16 §4 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24), its "Priority inversion laboratory": three
  processes, one lock, one processor, two arbitration rules. A16 reads it
  as granted authority without efficacy, and its remedy as "temporarily
  empowering a lower-priority process upon which it depends". Priority
  inheritance is Sha, Rajkumar and Lehoczky's ([LIT-tmphhs41](../literature.d/LIT-tmphhs41.md)). The
  note of 2026-11-24 is the assistant's: the schedules checked, and what
  the relief costs the medium-priority process. The wording is A's
  (ChatGPT, in the exchange 'Memes, Contracts, and Systemic Normativity');
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmp2dpcv CLAIM-tmpersgx — Proposed; cited as filed or held beside this entry, whatever its standing -->
<!-- inactive-ok-file: LIT-tmphhs41 — Deferred; cited as filed or held beside this entry, whatever its standing -->

# CASE-tmptpna1: Priority inversion on one preemptive processor: a high-priority process blocked on a lock held by a low-priority one misses its deadline under fixed priorities, because a medium-priority process preempts the holder, and meets it under priority inheritance, which moves the delay onto the medium-priority process

## The construction

A16 §4: "Three processes share a preemptive single CPU. L holds a lock from
time zero. H and M arrive at time 1. H must finish by time 5." "L requires
four units of CPU time, M five, and H one. Only the arbitration
arrangement changes." H needs the lock L holds.

- **Fixed priorities.** "M preempts L, preventing the release of the
  resource. H misses its deadline despite having the highest assigned
  priority." H completes at 10.
- **Priority inheritance.** "The resource holder temporarily inherits H's
  priority, completes its work and releases the lock. H then finishes by
  its deadline." H completes at 5.

## A16's reading

| Phenomenon | A16's interpretation |
|---|---|
| Structural conflict | "Multiple processes require incompatible uses of a resource." |
| Governance-induced frustration | "An available satisfactory arrangement is not selected by the current governance." |
| Claimed precedence | "H requests the highest priority." |
| Granted authority | "The scheduler recognizes H's assigned priority." |
| Practical efficacy | "H remains unable to act because of its dependency." |
| Intervention | "Priority is temporarily conferred upon L." |
| Relief | "The organization becomes capable of fulfilling the relevant commitments together." |

"**Advancing the interests of the highest-priority process requires
temporarily empowering a lower-priority process upon which it depends.**
Authority is relational. It cannot be adequately allocated by examining
processes in isolation." A16 calls this a realization of [CLAIM-357](../claims.d/CLAIM-357.md)'s
separation of structural infeasibility from governance-induced
frustration, and of [CLAIM-283](../claims.d/CLAIM-283.md)'s claimed precedence against granted
authority.

## Note of 2026-11-24: the assistant's check

The schedules were simulated unit by unit with `python3 -I` (a preemptive
scheduler running the highest effective priority among ready processes, H
not ready while L holds the lock):

- fixed priorities: L, M×5, L×3, H; completions M at 6, L at 9, H at 10;
- inheritance: L×4, H, M×5; completions L at 4, H at 5, M at 10.

A16's numbers are right. What its table leaves out is M. Under
inheritance M finishes at 10, not 6: the relief moves four units of delay
from H to M. And no schedule could do better for both. The work totals ten
units on one processor; for H to finish by 5, L's four units and H's one
must fill the interval up to 5, so M cannot start before 5 and finishes at
10 at the earliest. So:

- the case shows governance-induced frustration, in [CLAIM-357](../claims.d/CLAIM-357.md)'s sense,
  only because M has no deadline. Give M any deadline before 10 and the
  commitments to H and M are jointly infeasible under every arbitration
  rule: the frustration is structural, and inheritance only chooses which
  commitment fails;
- "fulfilling the relevant commitments together" is true of H's deadline
  and the lock's mutual exclusion; it is a reallocation of delay, not a
  costless gain, which matters for reading the remedy as relief rather
  than as a choice of whose claim prevails ([CLAIM-556](../claims.d/CLAIM-556.md): dropping a demand
  is not relief).

The two arbitration rules give the same schedule whenever L does not hold
a lock H needs, so the case is also an instance of arrangements alike on
the ordinary course that part under contention ([CLAIM-tmpersgx](../claims.d/CLAIM-tmpersgx.md), argued in
[ARG-tmp2dpcv](../arguments.d/ARG-tmp2dpcv.md)). The note's wording is the assistant's (Claude, in this
session); adopting it is the owner's call.

## Note of 2026-11-24: a correction to the delay figure

The assistant's note above says "the relief moves four units of delay from
H to M". The manuscript review of 2026-11-24 found that imprecise. Against
the schedule without inheritance, H and L each finish five units earlier
and M four units later. So inheritance takes five units of delay off H,
and off L, and puts four on M. It is a reallocation, as the note says, but
not of one block of four units. The total delay summed over the three
processes falls by six. The conclusion stands: no schedule finishes H by 5
and M before 10. Bearing: a corrected figure; no change of status. The
wording is the assistant's (Claude, in this session).

## Note of 2026-11-24: from the revision of the manuscript governance-of-becoming, Part I
<!-- inactive-ok-file: TERM-tmpgiy6r SYNTHESIS-tmp4tvbr — Proposed; cited with their standing -->

The manuscript's first draft read this case's "Granted authority" row as
an instance of [TERM-tmpgiy6r](../terms.d/TERM-tmpgiy6r.md)'s operational standing without effective
authority (Article 2's join J2.4). The independent reader of the joins
found the reading a relabelling, since the glosses match ("The scheduler
recognizes H's assigned priority"; the term's "The arrangement recognizes
its eligibility to make that request consequential"), and found that it
exposes a conflict between this case and the term over [CLAIM-283](../claims.d/CLAIM-283.md)'s
"granted authority" ([SYNTHESIS-tmp4tvbr](../syntheses.d/SYNTHESIS-tmp4tvbr.md), "The joins of the manuscript
governance-of-becoming, Part I"). The two readings:

- **This case's.** A16's table calls the scheduler's recognition of H's
  priority [CLAIM-283](../claims.d/CLAIM-283.md)'s granted authority, and sets it apart from
  "Practical efficacy" ("H remains unable to act because of its
  dependency"). On this reading a grant is a recognition that can hold
  without efficacy. Granted authority then sits with the term's middle
  quantity, operational standing, and efficacy is a third thing.
- **The term's.** [TERM-tmpgiy6r](../terms.d/TERM-tmpgiy6r.md)'s Relations: "Asserted claim against
  effective authority is [CLAIM-283](../claims.d/CLAIM-283.md)'s split of claimed precedence from
  granted authority". On this reading a grant is the influence actually
  received, as in A4 §2 in [CLAIM-283](../claims.d/CLAIM-283.md) ("granted influence I_i"; "An
  operator can urgently demand control without receiving it"). Granted
  authority is then effective authority, and what this case shows of H
  is standing without a grant.

Both cannot hold of the same row. Which reading of [CLAIM-283](../claims.d/CLAIM-283.md) the record
takes is not decided here. It bears on [CLAIM-283](../claims.d/CLAIM-283.md) (Active), on the term
and on this case's table. The manuscript's Article 2 (§2.6) states the
conflict and takes neither reading. Bearing: a conflict between two
entries' readings of a third; no change to the case, its links or its
status. The wording is the assistant's (Claude, in this session).
