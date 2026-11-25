---
number: 1158
status: Proposed
formerly:
- CLAIM-tmpqpfvh
title: 'Recognition follows maintainers, not the name'
statement: >-
  In contested open-source successions the community's recognition followed
  the maintainers and not the name: where the creator or the body of core
  maintainers moved, the successor became the recognized line, where only
  part moved recognition split, and no successor took the original's name
  except by reunion
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A contested open-source succession in which the original's creator or
  body of core maintainers moved to the successor, the original kept no
  active core team, and the major independent downstreams nonetheless
  stayed with the name holder; or one in which a successor that the core
  did not join became the recognized line; or a re-coding of Hudson and
  Jenkins or freenode and Libera Chat showing the maintainers did not move
  wholesale.
tags:
- individuation
- social-ontology
- social-identity
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-411
corroborates:
- CLAIM-329
- CLAIM-328
bears_on:
- QUESTION-118
summary: >-
  From the run of [CASE-223](../cases.d/CASE-223.md)'s design on public records ([CASE-411](../cases.d/CASE-411.md)).
  Where the maintainers moved wholesale, the successor became the
  recognized line: Hudson's later steward wrote that "Jenkins is the
  replacement for it", and freenode was abandoned for Libera Chat by
  Ubuntu, Wikimedia and others. Where part of the core moved and the
  steward kept a paid team, recognition split (MySQL and MariaDB, Redis and
  Valkey) or went to the successor (OpenOffice.org, whose name passed to
  Apache). The name went with the successor only when io.js and Node.js
  reunited under Node.js on io.js's code. Two cases in the "moved
  wholesale" row; the pattern is [CLAIM-329](CLAIM-329.md)'s criterion as the community
  applied it. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-411 — new, Proposed; the study this rests on -->
<!-- inactive-ok-file: CASE-223 — Proposed; the design the study runs -->

# CLAIM-1158: Recognition follows maintainers, not the name

## The claim

In [CASE-411](../cases.d/CASE-411.md)'s eight contested cases the name stayed with the steward
in every case but one, and the community's recognition (coded from major
independent downstreams and the original's own later steward) went:

| maintainers moved | successor | split | reunited | undetermined |
|---|---|---|---|---|
| yes (Hudson, freenode) | 2 | | | |
| partial (OpenOffice.org, MySQL, Node.js, Redis, Gitea) | 1 | 2 | 1 | 1 |
| no (Terraform) | | | | 1 |

So recognition never followed the name against the maintainers, and
followed the maintainers against the name in both cases where they moved
wholesale. This is [CLAIM-329](CLAIM-329.md)'s criterion, persistence by transmission of
the producing organization, as the participants applied it, and the split
cases are [CLAIM-328](CLAIM-328.md)'s successors in different respects, at a change of
steward rather than a relocation.

## What it does not say

- Which successor, if any, is the project persisting. That stays
  [QUESTION-118](../questions.d/QUESTION-118.md)'s question; this says which one the community treats as
  continuing it.
- Anything at scale: two cases make the "yes" row, and three outcomes are
  undetermined because their downstreams were not checked.
- That the maintainers' move caused the recognition rather than both
  following a third thing (the steward's act).
