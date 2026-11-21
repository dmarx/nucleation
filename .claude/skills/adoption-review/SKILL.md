---
name: adoption-review
description: A review of the record's Proposed decisions (ADRs) for adoption - which are already in force, built into the configuration or tooling or carried as steps in CLAUDE.md or a skill and applied, and which are not; it derives the evidence by script, sorts the decisions into adopt, adopt after a look, and leave, and puts them to the owner as a checklist. Use it when the owner asks to promote decisions that are already adopted, at a status review, or when the decisions index shows many pending. ADR-tmpvmzl6 holds the invariants.
---
<!-- .claude/skills/adoption-review/SKILL.md -->
<!-- inactive-ok-file: ADR-tmpvmzl6 — Proposed; the decision this skill carries out, until the owner adopts it -->

# Adoption review

A decision is Proposed until the owner adopts it, and the record applies it
from the start. This review finds the decisions whose rules are already in
force and asks the owner to adopt them. ADR-tmpvmzl6 holds the invariants;
this file holds the steps, and changes when a step proves wrong.

## 1. Derive the evidence

Cut a branch from `staging`. Run

    python3 -I scratch/tools/adoption_signals.py . <scratchpad>/signals.json

which prints, for each Proposed ADR: age in days; files citing it;
`inactive-ok` directives excusing it, and how many say it is being applied;
and citations from CLAUDE.md, skills, workflows and `luria.yaml`. Keep the
output for the workbench entry. Do not trust the counts as verdicts: a
decision can be cited often because it is argued over.

## 2. Check the mechanism

For each decision that says it changes something mechanical (a line, a topic,
a work, a field, a relation, a scheme, a workflow, a cadence), confirm the
change exists: the term in `luria.yaml`, the job in `.github/workflows/`, the
behaviour in luria. A decision whose mechanism exists is in force whatever
its age.

## 3. Check the practice

For each process decision (how to file, read, review, cite): find the step
that carries it (CLAUDE.md, a skill) and two or three entries that applied
it since it was filed. Look for contrary signals: a later decision that
changes it, a history note that reverses it, practice that ignores it.

## 4. Sort

- **adopt**: mechanism exists, or a carried step applied for a week or more,
  with nothing contrary;
- **adopt after a look**: applied, but recent, thin, or still being revised;
  say what to look at;
- **leave**: too new, not applied, or superseded in practice; say which, and
  recommend Rejected or Superseded where practice has moved on.

Decisions filed in the same session as the pass, or ruled on in an open pull
request, are left to that pull request.

## 5. Put it to the owner

Open the pull request into `staging` with the workbench entry, the
decision's first application if this is the first pass, and the checklist:
one group per verdict, each line the code, a short title and the evidence in
a phrase. Say how many statuses the groups would change; many at once is a
reason to raise it, CRM style, before applying any. Do not change a status
before the owner rules. A go-ahead adopts the recommendations as stated.

## 6. Apply the ruling

In the same pull request: each status changed with a version and a history
entry naming the review, the date and the evidence. Leave directives for CI's
repair. Update the workbench entry with the ruling.
