---
status: Open
title: "Generate a coverage report of the record's lines against its works, giving for each view the entries it draws on with their standings, whether it has been reviewed, and its missing dependencies, unsupported joins and unchecked overlaps"
version: 1
stage: idea
method:
- operationalization
tags:
- design-rationale
date: '2026-11-25'
line:
- record-as-apparatus
advances:
- CLAIM-tmpd1a2h
summary: >-
  A53 §4 of the exchange "Hyper article interpretation" (2026-11-25),
  its fifth priority: "Create a maintained atlas-coverage report. Generate
  a matrix of inquiry lines against manuscript scopes, with each candidate
  view's claims, arguments, cases, terms, syntheses, their standings, and
  whether the view has been independently reviewed. Crucially, report
  missing dependencies and unsupported joins—not just counts." A59 §7
  asks the same of v0.3. The wording is A's (ChatGPT's, at A53 and A59 of
  the exchange "Hyper article interpretation"); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpd1a2h CLAIM-tmp6xzjy ADR-143 — Proposed or new; the coverage claim it would measure, the cycle check and the manuscript protocol -->

# LEAD-tmpsgkxe: Generate a coverage report of the record's lines against its works, giving for each view the entries it draws on with their standings, whether it has been reviewed, and its missing dependencies, unsupported joins and unchecked overlaps

## The idea

A53 counted entries by line by hand, from the generated indexes, and
A59 ended: "the atlas doesn't yet measure how much of Nucleation's
underlying argument each view actually covers. The next useful audit
would map each candidate view to its source objects and measure orphaned
regions, unsupported joins, repeated exposition, and missing cases."

## What the record already derives

Parts of it exist. The `works` field gives each view's members, and each
work has a generated index. The synthesis review (ADR-083's coverage of
scopes by accounts) and the reading review (ADR-091, readings no line
builds on) derive two of A59's measures. ADR-143's manuscript workspaces
keep each manuscript's review and its joins. What no report gives is the
matrix of lines against works, with standings and review state, and the
overlaps between views (CLAIM-tmp6xzjy: checked on cycles).

## What it needs first

A decision on whether the report is a luria report or a script, since a
new generated view changes `luria.yaml` or CI, which waits on the owner;
and a definition of "unsupported join" a script can apply, for which
ADR-143's third invariant (a join no entry maps to) is the start.
Counts alone would repeat a hand-made table as a generated one, and A53
itself says counts do not measure coverage.
