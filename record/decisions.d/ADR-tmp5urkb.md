---
status: Proposed
title: 'Readings no line uses are reviewed in a protocol of their own, by line, by topic or by question, and each is tied to an entry that should use it, raised as a question or claim, held with a reason, or flagged'
version: 1
tags:
- record
date: '2026-11-11'
summary: >-
  ADR-090 derives a reading's lines from the entries that use it, and
  its view shows 450 of 856 readings in force used by no line. The owner
  holds that the record should be building on its readings, and that
  reviewing under-used ones is worth its own protocol, maybe several. This
  decision makes it one protocol with three modes, carried by the
  reading-review skill: by line (what a line should build on), by topic
  (where the record reads and does not argue) and by question (evidence
  the argument has not weighed). Each reading reviewed gets one of four
  verdicts: tie it to an entry whose own text should use it, raise a
  question or claim it calls for, hold it with a reason, or flag a defect
  in it. The demonstration runs the by-line mode on
  organizational-normativity, the one line no reading served. Rejected:
  folding it into the synthesis review; three separate protocols; tying
  readings by topic alone.
---

# ADR-tmp5urkb: Readings no line uses are reviewed in a protocol of their own, by line, by topic or by question, and each is tied to an entry that should use it, raised as a question or claim, held with a reason, or flagged

## Context

The record reads more than it argues. ADR-090's view of readings by
line found, on 2026-11-11, 856 readings in force, of which 450 are used by
no claim, argument, question or case of the record's argument, and one
line, organizational-normativity, used one. (The view's first version
missed readings that claims ground on and showed 579; this decision's
demonstration found that, and ADR-090's version 2 corrects it.)

The owner's view, on seeing this: the record should be building on its
readings, and if it is not, that is a large oversight. Reviewing
under-used readings is worth its own protocol, maybe several.

A synthesis review (ADR-078, ADR-084) looks at the argument the record
holds and asks whether its accounts map it faithfully. It does not look at
what the record has read and not used. A reading review does.

## Decision

- **One protocol, three modes.** The reading-review skill carries it. A
  run takes one mode:
  - by line: the unused readings in a line's subject, against its claims
    and questions;
  - by topic: one primary topic's unused readings, against the whole
    record;
  - by question: unused readings that bear on open questions in substance
    without a relation saying so, and open questions none of whose
    readings any claim uses.
- **Four verdicts.** Each reading reviewed is:
  - **tied** to an entry whose own text should use it, by a relation the
    text supports (`grounds`, or `corroborates`, `bears_on` or `answers`
    from the reading);
  - **raised**, where it calls for a question or claim the record lacks:
    a QUESTION filed, or a CLAIM drafted for the owner, a claim resting on
    claims passing ADR-075's step 5;
  - **held**, where the argument does not need it now, with the reason in
    the curation entry;
  - **flagged**, where the reading has a defect, for a sweep.
- **No relation by topic alone.** A reading on the same subject as a claim
  is not evidence for it. A tie needs the claim's or question's own words
  to meet what the reading holds.
- **Demonstration (ADR-071).** The by-line mode, run on
  organizational-normativity, the line no reading served. Its curation
  entry gives each reading's verdict.

## Alternatives considered

- **Fold it into the synthesis review as a third arm.** The two ask
  different questions of different material: one of the argument, one of
  the reading. A line's reading review can run beside its synthesis
  review, and the skill says so, but neither waits on the other.
- **Three separate protocols.** The modes share the verdicts and the
  rules for a tie, and differ only in what they select. One skill with
  three modes keeps the rules in one place.
- **Tie readings by topic.** It would empty the unused list fast and mean
  nothing: the `topics` vocabulary says what a work is about, not what a
  claim needs.

## Consequences

- **The unused list shrinks only by judgement.** Each tie, question or
  claim is argued from the text, and each hold says why.
- **Lines gain readings as they are reviewed.** The view shows it, since a
  reading's lines are derived.
- **Raised questions and claims are the owner's.** A claim drafted by the
  review is Proposed, and its summary says the wording is the assistant's.
