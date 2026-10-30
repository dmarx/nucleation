---
number: 351
status: Proposed
formerly:
- THEORY-tmpp4dqy
promote_when: >-
  A measured comparison, in a simulator or in line operations, of crews
  doing the same approach with the speeds set as bugs and without them,
  under the same workload and interruptions, recording errors and timing
  in coordinating speeds with configurations at the moment of use and the
  pilots' own recall of the speed values. It promotes the account if the
  bugged system keeps performance under load and interruption while the
  pilots' recall of the values is no better, so that the gain is the
  system's and not the pilots'; it refutes the system-level claim if crews
  without bugs do as well under the same load, or if the gain goes with
  better pilot recall. Further task analysis, or more observation of
  flights that succeed, cannot settle it: the account is already a task
  analysis of successful flights.
title: "In a two-pilot airliner cockpit, setting the approach speeds as bugs on the airspeed indicators, prepared 25 to 30 minutes ahead in a low-workload phase from a card selected by the displayed gross weight, turns recall and scale reading at the moment of use into a judgement of spatial proximity, so the cockpit system remembers the speeds without either pilot's memory being improved; this is argued by task analysis of mandated procedure, not measured"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    The supports entry for CLAIM-296 is replaced by corroborates: the
    sixteenth status review (ADR-057), at the status review's ruling
    (the owner delegated these rulings), moved this reading from
    CLAIM-296's grounds to its corroborated_by (ADR-058). That claim
    cites it as one illustration of its general form and does not use
    its contested thesis. A dated note says what holds it back. The
    status is unchanged.
tags:
- cognition
- embodied-cognition
- social-ontology
date: '2026-10-15'
source:
- LIT-1066
summary: >-
  Hutchins (1995), [LIT-1066](../literature.d/LIT-1066.md), read in [NOTE-867](../notes.d/NOTE-867.md). A stylized task analysis of
  one airline's MD-80 procedure, informed by observation but reporting no
  measurements. The speed-card booklet, filtered by the displayed gross
  weight, is the system's long-term memory; the values pass through speech
  to bugs on two airspeed indicators, and on approach the pilots judge the
  needle's nearness to a bug instead of recalling and reading speeds. The
  paper concludes that the memory is "not made primarily of pilot memory".
  It analyses only success, for an anticipated, mandated and invariant task
  with a few values needed in a fixed order, so it says nothing about
  search for one item among many under a deadline. Cognition in the Wild
  ([LIT-1060](../literature.d/LIT-1060.md)) is Unavailable.
bears_on:
- QUESTION-101
corroborates:
- CLAIM-296
---
<!-- inactive-ok-file: LIT-1060 — Unavailable; held without a reading, cited as such -->
<!-- inactive-ok-file: CLAIM-296 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# THEORY-351: In a two-pilot airliner cockpit, setting the approach speeds as bugs on the airspeed indicators, prepared 25 to 30 minutes ahead in a low-workload phase from a card selected by the displayed gross weight, turns recall and scale reading at the moment of use into a judgement of spatial proximity, so the cockpit system remembers the speeds without either pilot's memory being improved; this is argued by task analysis of mandated procedure, not measured

## Source

Hutchins (1995), [LIT-1066](../literature.d/LIT-1066.md) (Cognitive Science 19(3), 265–288), read in
[NOTE-867](../notes.d/NOTE-867.md) from the author's posted scan. The book Cognition in the Wild
([LIT-1060](../literature.d/LIT-1060.md)) is Unavailable; only its posted Introduction was seen.

## What was actually shown

**The method.** The unit of analysis is a functional system, "a
constellation of structures, some of them internal to the human actors,
some external, involved in the performance of some invariant task". The
account is "somewhat stylized", from one airline's MD-80 manual, informed
by more than 100 observer flights, simulator recordings and interviews.
Three descriptions of one activity: the procedure, the representations
outside the pilots, and what those leave the pilots to do inside.

**The retrieval.** The speed-card booklet holds speeds for each weight
interval, unchanged by crew action. The gross weight, displayed on the
fuel quantity indicator, "is used as a filter on this written memory",
and since weight and speeds share a card, "selecting the correct weight
can't help but select the correct speeds." The card posted where both
pilots see it allows cross-checking against the displayed weight.

**The transformation.** The speeds are spoken, read back, and set as bugs
on both airspeed indicators. "What was accomplished without speed bugs by
remembering speed values, reading the ASI needle values, and comparing the
two values is accomplished with the use of speed bugs by judgments of
spatial proximity. Individual pilot memory has not been enhanced; rather,
the memory function has now become a property of a larger system in which
the individual engages in a different sort of cognitive behavior." What
the pilots must hold is the meaning of each region of the dial, not the
speeds.

**Across time.** "Speed bugs permit a shift in the distribution of
cognitive effort across time. They enable the crew to calculate
correspondences between speeds and configurations during a low workload
phase of flight, and save the results of that computation for later use."
Landing data are prepared "about 25 to 30 minutes prior to landing" and
used "ten to fifteen minutes later", and the bugs are "relatively
insensitive to the interruptions, the distractions, and the delays that
may disrupt internal memories."

## What this does not say

- **That the claims are measured.** No timings, error rates or comparison
  of crews or procedures. The system without bugs is imagined, and the
  pilots' internal memories are inferred: "Lacking additional evidence, we
  cannot know the duration or quality of these memories."
- **That the bugs give a better outcome.** The bugged system "achieves the
  same results" as one without; the gain claimed is lower demand on scarce
  resources at the moment of use and robustness to interruption.
- **That pilot memory plays no part.** The memory process "emerges from the
  activity of the pilots"; the claim is that the cockpit's memory "is not
  made primarily of pilot memory", not that pilots remember nothing.
- **That it covers unanticipated retrieval or search.** The task is
  mandated, done "on every flight", with four values needed in a fixed
  order and known in advance. Nothing here bears on finding one item
  among many on a request under a deadline ([CASE-085](../cases.d/CASE-085.md)'s situation).
- **That such systems do not fail.** Only success is analysed: "In all of
  my observations, never have I seen a crew fail to compute and set the
  approach speeds." Missed speeds are mentioned, not examined.
- **That it generalises beyond this cockpit.** One aircraft type, one task,
  one airline's manual; the paper says similar procedures exist on every
  airliner, without showing them.

## Connections

- [QUESTION-101](../questions.d/QUESTION-101.md) asks, for a stated class of tasks, when availability is a
  property of the system and not of a member, with a case where changing
  the arrangement alone changes it. This is that case argued in principle,
  for anticipated, invariant tasks prepared in advance: the system
  remembers when the task's structure is built into artifacts, the cue
  (displayed weight, the needle nearing a bug) supplied by the environment.
- [CLAIM-296](../claims.d/CLAIM-296.md) holds that deployability is a relation, not a property of one
  element. This corroborates it, the nearest case the record holds,
  without the claim resting on it, and adds a factor the
  claim does not list: when the work of retrieval is done relative to the
  deadline.
- [QUESTION-095](../questions.d/QUESTION-095.md) starts from this case: a result computed once at low load
  and read back by perception. [THEORY-331](THEORY-331.md) and [THEORY-342](THEORY-342.md) price the
  machine-learning versions of moving computation before the request.

## Note of 2026-10-29: what holds it back

Read in full (NOTE-867), but its promote_when is unmet. The record holds
no measured comparison of crews with and without speed bugs under the same
load that records timing, errors and the pilots' recall. The paper is a
stylized task analysis of successful flights, as the title's "argued …,
not measured" already says. An Active "Hutchins argues" reading on
THEORY-1110's pattern would free nothing, now that CLAIM-296 cites it as
corroboration.
