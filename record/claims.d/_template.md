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

# Optional. The line of inquiry and the manuscript(s) it belongs to.
# line: will-organization
# works:
# - organization-of-will

# Relations, each optional. `rests_on` is what this could not stand without:
# THEORY (a reading), CLAIM, CASE, or LIT (a work cited without a reading,
# the weakest). `objects_to` names a CLAIM (rebut or undermine) or an ARG
# (undercut). Converses are written by `luria link --fix`.
# answers: [QUESTION-000]
# rests_on: [THEORY-000]
# objects_to: [CLAIM-000]
# complements: [CLAIM-000]
# uses: [TERM-000]

summary: >-
  Who argued it and where, and the sharp edge: what it does not say.
---

<!-- unresolved-ok-file: QUESTION-000, THEORY-000, CLAIM-000, TERM-000 — the placeholders a new document replaces -->

# CLAIM-NNN: What the record holds, stated as a finding

## The claim

The claim in a paragraph, and the argument for it if no ARG carries it.

## What it does not say

The stronger reading it invites and does not support.
