---
status: Proposed
title: 'predicate (of an entry), read as a test'
version: 1
tags:
- design-rationale
- epistemology
date: '2026-11-21'
line:
- record-as-apparatus
- nucleating-argument
complements:
- TERM-132
summary: >-
  A yes-or-no question about a version of an entry, read as the indicator
  test it defines, so that the predicate is a probe in TERM-069's sense and
  the versions that pass it are a constraint set. The owner's reframe of
  2026-11-21, "adding predicates to an item is a manifestation of adding
  constraints", and their pointer to the record's mapping of predicates to
  test functions; the definition is the assistant's (Claude, in this
  session), and adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-132 CLAIM-772 CLAIM-tmp8v75o CLAIM-tmpj4fzn — Proposed; the term this complements, and the claims filed with it on 2026-11-21 -->

# TERM-tmp7m4at: predicate (of an entry), read as a test

## Definition

A **predicate** of an entry is a yes-or-no question about a version x of it,
answered from the version alone: does it rest on CLAIM-772, is its status
Proposed, does its quoted passage read so, does its title match its
heading. It is **read as a test** when it is taken as the indicator
f_p(x) ∈ {0, 1}, an observable of the kind the record's formal results are
stated for ([CLAIM-107](../claims.d/CLAIM-107.md), [CLAIM-635](../claims.d/CLAIM-635.md)) and a probe in the sense of [TERM-069](TERM-069.md). A
graded predicate is a bounded observable in the same place.

Its **constraint set** is A_p = {x : f_p(x) = 1}, the versions that pass. An
entry's predicates together allow the versions in A = ∩ A_p.

A restating step can respect a predicate in two ways, and the difference is
the one [CLAIM-772](../claims.d/CLAIM-772.md) draws:

- it **enforces** the predicate when it makes every version pass, whatever
  it was before: f_p becomes constant, the feature is in the contracting
  part ([TERM-132](TERM-132.md)), and its value is the predicate's, from the schema or
  from a source;
- it **preserves** the predicate when it copies the test's outcome:
  K f_p = f_p, the feature is in the conserved part, and versions that
  differed on it go on differing.

A predicate is **hard** when the step refuses a version that fails it (lint,
a resolving code) and **soft** when failing it only costs something (a prose
convention, a reviewer's habit).

## What it is not

- **A field.** A field is a slot the schema offers; a predicate is a filled
  slot or a relation, a question with an answer for this entry.
- **A claim.** A claim's title is a proposition the record holds a credence
  in, about the world or the record. A predicate is about one entry's text,
  and the entry passes it or not.
- **The probe family of [TERM-069](TERM-069.md).** That is a declared set of tests under
  which two objects are equivalent. An entry's predicates are one entry's
  tests, accrued over its life, and they say what versions of it are
  allowed, not when two things count as the same.
