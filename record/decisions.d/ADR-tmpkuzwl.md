---
status: Proposed
title: 'A reading named as evidence in a question''s or claim''s text is tied when the name is written, supporting cases corroborate, a question''s instruments are its premises, and readings used only by cases, terms or syntheses are held as used'
version: 1
tags:
- record
date: '2026-11-11'
summary: >-
  The first by-topic reading review (2026-11-11, five readers, 222
  readings) found that most readings the view counted unused were already
  named as evidence in a question's or claim's text, with no relation
  written, and its readers met the same unsettled cases. This decision
  settles them for the reading review and for filing: a note that names a
  reading as evidence writes the relation; a claim's supporting cases,
  instances and in-scope precedents corroborate it; a question's named
  instruments, measures and cautions are premises it bears on; a reading
  tied to several entries is one verdict; a reading used only by a case, a
  term or a synthesis is held as used in fact; a claim grounding on a work
  that now has a reading gets the reading as corroboration or ground, and
  the LIT edge goes to a sweep; and a split run coordinates its raises.
  The reading-review and read-and-file skills carry the instructions.
  Rejected: a relation from a case, term or synthesis to a reading;
  stretching `reported_in` to cover use; leaving the cases to each reader.
---
<!-- inactive-ok-file: ADR-091 ADR-090 — Proposed; the reading review and its view, which this decision extends -->

# ADR-tmpkuzwl: A reading named as evidence in a question's or claim's text is tied when the name is written, supporting cases corroborate, a question's instruments are its premises, and readings used only by cases, terms or syntheses are held as used

## Context

ADR-091 set up the reading review; its skill carries the steps, and ADR-090
derives a reading's lines from the entries that use it. The first by-topic
run, on 2026-11-11, took the five largest primary topics of the readings
no line used: 222 readings, read by five readers in parallel. It tied 101,
raised a question and a claim from 4, and held 117.

Three findings bear on how the record should work, not only on that run:

- **Most of the "unused" readings were named.** QUESTION-271,
  QUESTION-275, QUESTION-276 and CLAIM-454, among others, named readings
  as their evidence in their bodies and dated notes without the relation.
  QUESTION-271 alone took twelve ties, QUESTION-275 fourteen, CLAIM-454
  ten. The view counted them unused because the relation was never
  written when the note was.
- **The readers met the same unsettled cases.** All five asked whether a
  claim's "supporting cases" are evidence it does not need (ADR-058's
  corroboration), whether a question's named instruments and cautions are
  premises (ADR-060), how to count a reading tied to several entries, and
  what to do when the only entry using a reading is one that cannot carry
  a relation to it: a case (which reaches a reading only by `reported_in`,
  provenance), a term (for a definition) or a synthesis. Each answered
  alone; their answers agreed, but nothing held them.
- **Two parts raised the same question** from readings in different topics
  (constructor theory's laws of possibility as constraints realized by
  nothing, CLAIM-477's defeater (b)). The second withdrew its duplicate
  only because the coordinator relayed the first.

## Decision

1. **A note that names a reading as evidence writes the relation.** When a
   question's or claim's dated note, or its body, cites a reading as
   evidence for or on it, the same change writes `bears_on` or
   `corroborates` from the reading. In a reading review, the reading's
   code, NOTE and LIT are searched for first.
2. **Supporting cases, instances and precedents corroborate.** A claim that
   lists a reading among its supporting cases, or cites it as an instance,
   parallel or precedent it does not need, takes it as `corroborates`
   (ADR-058). A claim that disclaims a reading as evidence takes nothing. A
   precedent from another domain corroborates only a claim whose scope
   reaches that domain.
3. **A question's instruments are its premises.** A question that names a
   reading as an instrument, measure or caution for its own test takes it
   as `bears_on` (ADR-060). So does a reading that qualifies the answer of
   an Answered question without answering it alone.
4. **One verdict per reading.** A reading tied to several entries is one
   tie in a review's count; the account lists every relation.
5. **Used by an entry that cannot carry the relation.** Where the only
   entries using a reading are cases, terms or syntheses, the review holds
   it as used in fact, says which entry uses it, and the account lists it
   apart from readings unused. `reported_in` is provenance and is not
   stretched to record use. Several such readings that jointly state a
   result no claim holds may be raised as a claim.
6. **A claim grounding on a work that has a reading.** The review ties the
   reading as `corroborates` where the claim does its own work with the
   result, or as `grounds` where the claim uses it as an unproved premise.
   The claim's LIT edge is moved or dropped by a defect sweep, under
   ADR-058.
7. **A split run coordinates its raises.** Each reader checks a shared list
   of the run's raises before filing one, and adds its own. The
   coordinator merges any duplicate left, keeping the first code. Where two
   parts change the same entry, both changes stand as successive versions.

The reading-review skill carries 1 to 7 as instructions; the read-and-file
skill carries 1.

## Alternatives considered

- **A relation from a case, term or synthesis to a reading.** It would let
  the view count their use. It is a schema change for every scheme
  involved, and a case's use of a reading as a check or a design
  constraint is not one relation but several (evidence, method,
  provenance). Holding such readings as used, with the entry named, keeps
  the fact without the schema change; a relation can be decided when one
  kind of use recurs enough to name.
- **Stretching `reported_in` to cover use.** `reported_in` says where a
  case comes from. A proposed study is reported in no reading it uses as
  a design constraint; writing it so would make provenance false.
- **Leaving the cases to each reader.** The five readers agreed, but only
  because their briefs were alike. A brief is not where a rule should live.

## Consequences

- The next reading review has fewer judgement calls, and its counts are
  comparable with this one's.
- Filing writes the relation that a dated note implies, so the view's
  unused list shrinks at filing time rather than only by review.
- Readings used by cases, terms and syntheses stay in the view's unused
  list until a relation for them is decided; the reviews' accounts say
  which they are.
