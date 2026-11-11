---
status: Proposed
title: 'Normative judgment about organizations becomes a line of its own, organizational-normativity, split from will-organization: whether an organization''s own dynamics ground norms, and what judging one needs, is a question of its own, while acting as one stays, because its root question refines the line''s own'
version: 1
tags:
- record
date: '2026-11-11'
summary: >-
  The synthesis review of 2026-11-11 gave will-organization its first
  account, over six parts. Two parts were mostly closed: acting as one, and
  normative judgment about organizations. The owner left the split to the
  assistant's judgement. This decision adds the line organizational-normativity,
  "Normative judgment about organizations", and moves the 23 entries of the
  normative part to it in place of will-organization. Its root question
  asks whether an organization's own dynamics ground norms and what more
  judging one needs, which is not what organizes practical efficacy in an
  agent. Its ties to the line are two uses of a term and premises, which
  are dependencies. No relation supplies will-organization to any moved
  entry, and no entry outside the part gains the new line. Acting as one
  stays: its root question refines the line's own. Rejected: keeping
  both parts; splitting both; moving the normative part into
  distributed-agency or authenticity.
---
<!-- inactive-ok-file: ADR-085 — Proposed; the split rule, the accounts and the line rule this applies -->
<!-- inactive-ok-file: SYNTHESIS-038 SYNTHESIS-035 SYNTHESIS-036 SYNTHESIS-037 — Proposed; the accounts the split rests on and revises -->

# ADR-tmpczmfi: Normative judgment about organizations becomes a line of its own, organizational-normativity, split from will-organization: whether an organization's own dynamics ground norms, and what judging one needs, is a question of its own, while acting as one stays, because its root question refines the line's own

## Context

A line is "a named line of the record's own argument, so that a line can be
set aside as a whole and what depends on it can be found" ([ADR-032](ADR-032.md)).
will-organization is "what organizes practical efficacy in an agent, and how
that organization becomes precarious".

The sixth synthesis review gave it an account over six parts
([SYNTHESIS-035](../syntheses.d/SYNTHESIS-035.md)). Counting stored relations as `line_parts.py` does, two
parts are mostly closed:

| part | inside | out | in |
|---|---|---|---|
| acting as one ([SYNTHESIS-037](../syntheses.d/SYNTHESIS-037.md)) | 53 | 11 | 9 |
| normative judgment about organizations ([SYNTHESIS-038](../syntheses.d/SYNTHESIS-038.md)) | 32 | 15 | 7 |

The account set out, for each, the question it asks and whether it would
rightly go with the line if the line were set aside. The owner left the
split to the assistant's judgement.

## Decision

- **One line is added:** `organizational-normativity`, "Normative judgment
  about organizations". Its blurb names the part's findings and says it was
  split from will-organization. will-organization's blurb points to it.
- **The normative part's 23 entries move.** In each, `line` changes
  will-organization to organizational-normativity in place, and other lines
  are kept. Each entry gets a history note. No status, title or relation
  changes.
  - The part's root is [QUESTION-128](../questions.d/QUESTION-128.md): "Does the record's organizational
    account give a path to normativity from first principles: can norms of
    function and failure be defined from an organization's own dynamics, and
    what more do practical and moral authority need?" That is a question
    about organizations in general, not about what organizes efficacy in an
    agent.
  - Only two of its stored relations point into the line's core, and both
    are uses of [TERM-118](../terms.d/TERM-118.md). Its premises from the line, [CLAIM-523](../claims.d/CLAIM-523.md) and
    [CLAIM-445](../claims.d/CLAIM-445.md), are dependencies, and the argument chain reports them as
    crossings.
  - No moved entry answers, objects to, bears on or refines a
    will-organization-first entry, so none keeps will-organization
    ([ADR-085](ADR-085.md)). No entry outside the part relates in those ways to a moved
    entry, so none gains the new line.
- **Acting as one stays.** Its root, [QUESTION-034](../questions.d/QUESTION-034.md) ("If an agent is a
  population of interests, what makes it act as one"), refines the line's
  own [QUESTION-015](../questions.d/QUESTION-015.md), so it takes part in the line's argument. That most of
  its claims rest on readings other than the line's thesis makes them
  dependents of those readings. It does not make the part a separate
  inquiry.
- **The accounts follow the split.**
  - [SYNTHESIS-038](../syntheses.d/SYNTHESIS-038.md) becomes organizational-normativity's account
    (version 2).
  - [SYNTHESIS-035](../syntheses.d/SYNTHESIS-035.md), will-organization's line account, is revised over
    the five remaining parts (version 2). It keeps its version 1 counts as
    the record of why the line was split.
  - [SYNTHESIS-036](../syntheses.d/SYNTHESIS-036.md) names the new line (version 2).

## Alternatives considered

- **Keep both parts.** Setting will-organization aside would then retire a
  normative inquiry that depends on the line but does not argue its
  question, which is the opposite of what a line is for.
- **Split both.** Acting as one would leave a root question that refines
  the line's own question. That refinement would become a crossing, and the
  line would lose the question its paper starts from.
- **Move the normative part into distributed-agency or authenticity.**
  Eight of its entries already carry distributed-agency, four of them
  first, and they keep it. But its question is not what an organized whole
  is. Authenticity's blurb names "normativity across the scales an agent
  spans", but that line is set aside as future work, and moving open
  claims into it would set them aside too.

## Consequences

- The current-account view shows organizational-normativity as a line with
  one account. will-organization's account is built over five parts.
- `luria lint` may report `rests_on` steps between the two lines, such as
  [CLAIM-614](../claims.d/CLAIM-614.md) and [CLAIM-624](../claims.d/CLAIM-624.md) resting on [CLAIM-523](../claims.d/CLAIM-523.md). They are dependencies.
- The name and blurb of the new line are the assistant's proposal. A
  rename is a vocabulary edit plus the same 23 `line` values.
