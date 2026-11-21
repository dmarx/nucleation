---
status: Proposed
title: 'The earmark convention is stated as steps in a procedure of its own, apart from the decision that records why: the decision holds the invariants, as the decision on filing does for its skill, and the procedure, beside the retrospective''s, holds what to do'
version: 1
tags:
- record
- process
date: '2026-11-21'
summary: >-
  Reading C of the owner's request ([ADR-tmpyzxw8](ADR-tmpyzxw8.md)): "new convention" separable from "ADR". The decision records the invariants and the reasons; the convention is the procedure the assistant follows, kept where procedures are, as the `read-and-file` skill is kept apart from [ADR-068](ADR-068.md). An alternative to [ADR-tmpyzxw8](ADR-tmpyzxw8.md), [ADR-tmp7kh0t](ADR-tmp7kh0t.md) and [ADR-tmpuu4y4](ADR-tmpuu4y4.md).
---
<!-- inactive-ok-file: ADR-tmpyzxw8 ADR-tmp7kh0t ADR-tmpuu4y4 ADR-115 ADR-068 — Proposed; the alternative readings of one request, and the decisions they sit beside -->

# ADR-tmps83ka: The earmark convention is stated as steps in a procedure of its own, apart from the decision that records why: the decision holds the invariants, as the decision on filing does for its skill, and the procedure, beside the retrospective's, holds what to do

## Context

The owner, 2026-11-21, after an earmark of theirs was filed as a devlog note:
"oh nice, let's persist and standardize that as a new convention with an ADR. I feel like those are separable." "Separable" has at least three readings, which would be filed
differently. Under the dialectic regime's rule for several readings, each is
filed as an alternative decision, and the owner chooses:

- **[ADR-tmpyzxw8](ADR-tmpyzxw8.md)**: separable from [ADR-115](ADR-115.md). One decision on earmarks, apart from the
  one on the assistant's own devlog notes.
- **[ADR-tmp7kh0t](ADR-tmp7kh0t.md)** and **[ADR-tmpuu4y4](ADR-tmpuu4y4.md)**: separable as *persist* and *standardize*. Two
  decisions: that an earmark is kept until a retrospective answers it, and
  what form the note takes.
- **ADR-tmps83ka**: separable as *convention* and *ADR*. The convention stated as
  steps in a procedure of its own, apart from the decision that records why,
  as [ADR-068](ADR-068.md)'s invariants stand apart from the `read-and-file` skill's
  steps.

When one is chosen the others go Rejected, and the readings stay on the
record. The assistant's lean is in [ADR-tmpyzxw8](ADR-tmpyzxw8.md)'s Readings section.

## Decision

The invariants are a decision: an owner's earmark becomes a devlog note, and
a retrospective answers it. The steps are a procedure, written as a skill
(`.claude/skills/retrospective/SKILL.md`) that covers filing an earmarked
note and, at a retrospective, gathering the `earmarked` notes and answering
each. CLAUDE.md points to the skill rather than stating the steps. The skill
can change without a new decision, as long as the invariants hold.

## Alternatives considered

[ADR-tmpyzxw8](ADR-tmpyzxw8.md), with the steps inside the decision and a sentence in CLAUDE.md, and the
pair [ADR-tmp7kh0t](ADR-tmp7kh0t.md) and [ADR-tmpuu4y4](ADR-tmpuu4y4.md).

## Consequences

A skill to write, for the retrospective as a whole and not only earmarks,
which the record lacks: retrospectives are written today from [ADR-110](ADR-110.md) and
[ADR-115](ADR-115.md) directly. Choosing this reading would make that skill its first
application; it is not written in this pull request.

## First application

None yet: the skill is written if this reading is chosen.
