---
# Don't copy this file by hand — run `luria new claim`, which assigns the
# code. A CLAIM is the record's OWN proposition, not a reading of someone
# else's: a reading is a THEORY, and a claim rests on it (ADR-032).

# Active | Proposed | Deferred | Superseded | Rejected — whether the record
# BELIEVES it. Same words and meanings as a THEORY's. An answered objection
# is a counter that went Rejected. A conceded one is recorded by its
# target's revision, and keeps the status its own evidence gives it (ADR-059).
status: Proposed

# One sentence, stated as a finding. Repeat it as the `# CLAIM-…:` heading.
title: What the record holds, stated as a finding

version: 1

# thesis | counter | granted | disclaimed | supposed — whose voice this is
# in. Independent of status; the mismatched pairs are the information.
role: thesis

# demonstrated | empirical | interpretive — how the claim AS STATED is
# supported (ADR-043): by proof or construction, by observation, or by
# argument and synthesis. Independent of status and role: a theorem whose
# reading is disputed is demonstrated and Proposed. Never inherited: a claim
# resting on a demonstrated one is not demonstrated for that. If parts of the
# claim are warranted differently, split it; do not pick one. REQUIRED.
warrant: interpretive

# REQUIRED for a thesis: what would defeat it. A kind of result or argument,
# stated so that the wrong kind cannot satisfy it.
defeated_if: >-
  The kind of result or argument that would defeat this.

tags:
- agency

date: '2026-01-01'

# REQUIRED: the line or lines of inquiry, from `lines` in luria.yaml. The
# claims index is grouped by it, and the `argument` chain reports a
# `rests_on` step that crosses from one line to another (ADR-032). A general
# result that rests on no claim may also hold `formal-apparatus`, so that
# setting its first line aside does not retire it (ADR-040).
line:
- will-organization

# Optional. The manuscript(s) this claim is marshalled into.
# works:
# - WORK-001

# Relations, each optional; converses are written by `luria link --fix`.
# `rests_on` names the record's own claims this one could not stand without —
# the spine the `argument` chain walks. `grounds` names evidence from outside
# it: THEORY (a reading), CASE, or LIT (a work cited without a reading, the
# weakest). `objects_to` names a CLAIM (rebut or undermine) and is the thread
# the `dialectic` chain walks; `undercuts` names an ARG whose inference this
# denies.
# Before filing a counter, ask: does it say the conclusion is false, or that
# something does not show it? The second is not a claim but an ARG from the
# premises to the conclusion, Rejected or Proposed (ADR-061).
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
