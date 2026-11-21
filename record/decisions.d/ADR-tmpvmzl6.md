---
status: Proposed
title: 'A decision''s status is reviewed for adoption in a protocol of its own: a pass derives, from the record and its tooling, the evidence that each Proposed decision is already in force, sorts them into adopt, adopt after a look, and leave, and puts its recommendations to the owner as a checklist; the owner rules, and the pass changes statuses in its own pull request'
version: 1
tags:
- record
- process
date: '2026-11-21'
summary: >-
  The owner, 2026-11-21: "we're probably overdue to promote some ADRs that
  are functionally already adopted. we should probably encapsulate that as
  another ADR-steered audit skill. write that ADR and kick off an audit".
  [ADR-057](ADR-057.md)'s status review ranks claims by reliance and judges credence; a
  decision's status is adoption, not credence, and nothing reviewed it.
  Forty-eight decisions stood Proposed on staging, many of them carried as
  steps in a skill, built into the configuration or a workflow, and excused
  dozens of times in directives "until the owner adopts it". This decision
  adds an adoption review, with its steps in the adoption-review skill and
  its evidence derived by a script each pass. First application: the pass
  of 2026-11-21.
---

# ADR-tmpvmzl6: A decision's status is reviewed for adoption in a protocol of its own: a pass derives, from the record and its tooling, the evidence that each Proposed decision is already in force, sorts them into adopt, adopt after a look, and leave, and puts its recommendations to the owner as a checklist; the owner rules, and the pass changes statuses in its own pull request

## Context

A decision enters Proposed and becomes Active when the owner adopts it. In
practice the record applies a decision from the pull request that proposes
it (CLAUDE.md: a decision goes with a demonstration of its effects), so a
decision can be in force for weeks while its status says otherwise. The cost
is not only a wrong label: every entry that cites such a decision carries an
`inactive-ok` directive excusing it, [ADR-095](ADR-095.md) alone 106 times, and the
decisions index shows as pending what the record already does.

[ADR-057](ADR-057.md)'s status review does not reach them. It ranks Proposed entries by
reliance and asks whether the evidence warrants belief; a decision's status
says whether the record has adopted a rule, which is a question about
practice and tooling, not about evidence.

## Decision

**An adoption review**, in its own pass, with its steps in the
`adoption-review` skill and these invariants:

1. **Evidence is derived, each pass, and kept nowhere** (as [ADR-057](ADR-057.md) has it
   for reliance). `scratch/tools/adoption_signals.py` reports, for each
   Proposed decision: its age; how many files cite it; how many
   `inactive-ok` directives excuse it, and how many of those say it is being
   applied ("until the owner adopts it", "the decision this follows"); and
   whether CLAUDE.md, a skill, a workflow or `luria.yaml` cites it.
2. **Three verdicts**, each with its evidence named:
   - **adopt**: the rule is in force, because it is built into the
     configuration, a workflow or the tooling, or because it is a step in
     CLAUDE.md or a skill and has been applied in entries for a week or
     more, and nothing in the record contradicts it;
   - **adopt after a look**: it is applied, but recently, thinly, or while
     still being revised; the pass names what the owner should look at;
   - **leave**: too new to have been applied, not applied, or superseded in
     practice; the pass says which, and recommends Rejected or Superseded
     where practice has moved past it.
3. **The owner rules.** Adoption is a change of status, the owner's under
   the dialectic regime. The pass puts its verdicts in its pull request as a
   checklist, grouped by verdict, so the owner can rule a group at once; a
   go-ahead adopts the recommendations as stated.
   A ticked box on the checklist is a ruling for that group, as a comment
   is; the pass reads the checklist's state as well as the comments before
   it applies anything (first pass: the ticks were missed and read only
   when the owner said so).
4. **The ruling lands in the pass's own pull request**: each status change
   with a history entry naming the review and the evidence. Directives that
   excused the newly Active decisions are left for CI's repair, which drops
   those that answer for nothing.
5. **Recorded in one workbench entry per pass**: the derived table, the
   verdicts and the reasons, so the next pass can see what was decided.
6. **When.** At a status review, when the decisions index shows many
   pending, or when the owner asks; not on a schedule.

## Alternatives considered

- **Fold it into [ADR-057](ADR-057.md)'s status review.** One review, but its ranking by
  reliance and its test of credence are the wrong instruments for a rule
  whose question is whether it is in force.
- **Adopt on merge.** Treat a decision as Active once its pull request
  merges. It would remove the gap but also the owner's adoption, which is
  the point of Proposed: a decision can be merged and applied as a trial.
- **Promote by script.** The signals are evidence, not a verdict: a decision
  can be cited often because it is contested.

## Consequences

- The decisions index says what the record actually does, and directives
  excusing adopted rules drop away.
- One more pass to run; the script keeps its cost to the judgement.
- The CRM rule of the dialectic regime applies: a pass that would change many
  statuses at once says so and waits for the owner.

## First application

The pass of 2026-11-21 (workbench entry of that date, 063801), over the 48
Proposed decisions on staging, with its checklist in this pull request.
