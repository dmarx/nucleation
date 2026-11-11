---
status: Proposed
title: 'A case can bear on a question, by the same `bears_on` claims, readings and accounts carry, and a question''s `bearing` lists the cases with them; how the case bears is its kind''s to say, not the relation''s'
version: 1
tags:
- record
date: '2026-11-11'
summary: >-
  A CASE could point only at claims (`illustrates`, `counterexample_to`)
  and at other cases, so a case filed for a question could not say so: the
  defect sweeps of 2026-11-11 found a dozen cases whose text names the
  question they serve, and the case filed for QUESTION-tmpmus93 could reach
  it only through its readings. A CASE now carries `bears_on`, to
  questions, with the meaning it has on a claim, and QUESTION's `bearing`
  converse takes cases. Whether a case tests, models or is an instance of
  the question is its `kind` (ADR-042), so one relation serves. ADR-085's
  line rule applies: a case takes the first line of a question it bears
  on. The demonstration adds the relation to the cases the sweeps found.
  Rejected: a relation per kind (tests, models, probes, examines);
  `motivates`; widening `illustrates` to questions.
---

# ADR-tmpcrpf5: A case can bear on a question, by the same `bears_on` claims, readings and accounts carry, and a question's `bearing` lists the cases with them; how the case bears is its kind's to say, not the relation's

## Context

A CASE's relations were to claims (`illustrates`, `counterexample_to`),
to cases (`variant_of`, `substitutes_for`) and to its source
(`reported_in`). A question could be borne on by a claim, a reading or an
account (ADR-060), but not by a case.

The defect sweeps of 2026-11-11 found a dozen cases whose text names the
question they were filed for, with no relation to it: CASE-104 and
CASE-140 on QUESTION-119, CASE-145 on QUESTION-260, CASE-148 on
QUESTION-118, CASE-058 on QUESTION-076, the symbiosis cases on
QUESTION-277, CASE-195 on QUESTION-117, and CASE-117's proposed study,
which maps its measures to six questions. The sweeps' history notes say "no
relation a case can carry". The owner then filed a case for
QUESTION-tmpmus93 (CASE-tmp4xp5m), and it could reach the question only
through the two readings that report it.

## Decision

- **CASE carries `bears_on`, to QUESTION.** Its meaning is the claim's: a
  question the case is evidence for or against, or a test, model or
  instance of, without answering it.
- **QUESTION's `bearing` takes cases.** `luria link --fix` derives it from
  the cases' `bears_on`, as from claims' and readings'.
- **The case's `kind` says how it bears.** A proposed or executed study
  tests the question; a construction models it; a specimen or reported
  study is an instance; a thought experiment probes it. The kinds are
  ADR-042's, orthogonal to standing, so the relation does not repeat them.
- **ADR-085 applies.** `bears_on` is one of its four relations, so a case
  that bears on a question takes the question's first line after its own.
- **Demonstration (ADR-071).** The cases above gain the relation, each
  with a history note quoting the text that names the question.
  CASE-195 takes distributed-agency, QUESTION-117's first line. The rest
  already carry their question's line.

## Alternatives considered

- **A relation per kind**: `tests`, `models`, `probes`, `examines`. Each
  restates a kind, and a case whose kind and standing cross (a documented
  construction, a study that is also a specimen) would need two relations
  for one fact. Every reader of `bearing` (the line rule, the reading
  review, the views) would have to merge them back.
- **`motivates`**: that the case gave rise to the question. That is
  provenance, not evidence, and a question's summary already says where it
  came from. No case was found where it mattered apart from bearing; it can
  be added when one is.
- **Widening `illustrates` to questions.** `illustrates` is defined
  against a claim: it makes the claim vivid without bearing its weight. A
  question has no weight to bear.

## Consequences

- A question's page lists the cases that bear on it beside its claims and
  readings.
- The reading review's by-question mode, and ADR-090's view, can count a
  case's bearing. ADR-090's view counts a reading's cases through
  `reported_in`; a case's own `bears_on` gives it a line of its own.
- A sweep could add the relation wherever a case's text names a question.
  This decision adds it only where the sweeps found it.
