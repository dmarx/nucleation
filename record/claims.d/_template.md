---
# Don't copy this file by hand — run `luria new claim`, which assigns the
# code. A CLAIM is the record's OWN proposition, not a reading of someone
# else's: a reading is a THEORY, and a claim rests on it (ADR-032).

# Active | Proposed | Deferred | Superseded | Rejected — whether the record
# BELIEVES it. Same words and meanings as a THEORY's. An answered objection
# is a counter that went Rejected; a conceded one went Active.
status: Proposed

# One sentence, stated as a finding. Repeat it as the `# CLAIM-…:` heading.
title: What the record holds, stated as a finding

version: 1

# thesis | counter | granted | disclaimed | supposed — whose voice this is
# in. Independent of status; the mismatched pairs are the information.
role: thesis

# REQUIRED for a thesis: what would defeat it. A kind of result or argument,
# stated so that the wrong kind cannot satisfy it.
defeated_if: >-
  The kind of result or argument that would defeat this.

tags:
- agency

date: '2026-01-01'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml. The claims index
# is grouped by it, and the `argument` chain reports a `rests_on` step that
# crosses from one line to another (ADR-032).
line: will-organization

# Optional. The manuscript(s) this claim is marshalled into.
# works:
# - organization-of-will

# Relations, each optional; converses are written by `luria link --fix`.
# `rests_on` names the record's own claims this one could not stand without —
# the spine the `argument` chain walks. `grounds` names evidence from outside
# it: THEORY (a reading), CASE, or LIT (a work cited without a reading, the
# weakest). `objects_to` names a CLAIM (rebut or undermine) and is the thread
# the `dialectic` chain walks; `undercuts` names an ARG whose inference this
# denies.
# answers: [QUESTION-000]
# rests_on: [CLAIM-000]
# grounds: [THEORY-000]
# objects_to: [CLAIM-000]
# undercuts: [ARG-000]
# complements: [CLAIM-000]
# uses: [TERM-000]

summary: >-
  Who argued it and where, and the sharp edge: what it does not say.
---

<!-- unresolved-ok-file: QUESTION-000, THEORY-000, CLAIM-000, TERM-000, ARG-000 — the placeholders a new document replaces -->

# CLAIM-NNN: What the record holds, stated as a finding

## The claim

The claim in a paragraph, and the argument for it if no ARG carries it.

## What it does not say

The stronger reading it invites and does not support.
