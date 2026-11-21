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
  test it defines, so that the predicate is a probe in [TERM-069](TERM-069.md)'s sense and
  the versions that pass it are a constraint set. The owner's reframe of
  2026-11-21, "adding predicates to an item is a manifestation of adding
  constraints", and their pointer to the record's mapping of predicates to
  test functions; the definition is the assistant's (Claude, in this
  session), and adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-132 CLAIM-772 — Proposed; the term this complements, and the claims filed with it on 2026-11-21 -->

# TERM-tmp7m4at: predicate (of an entry), read as a test

## Definition

A **predicate** of an entry is a yes-or-no question about a version x of it,
answered from the version alone: does it rest on [CLAIM-772](../claims.d/CLAIM-772.md), is its status
Proposed, does its quoted passage read so, does its title match its
heading. It is **read as a test** when it is taken as the indicator
f_p(x) ∈ {0, 1}, an observable of the kind the record's formal results are
stated for ([CLAIM-107](../claims.d/CLAIM-107.md), [CLAIM-635](../claims.d/CLAIM-635.md)) and a probe in the sense of [TERM-069](TERM-069.md). A
graded predicate is a bounded observable in the same place.

Its **constraint set** is A_p = {x : f_p(x) = 1}, the versions that pass. An
entry's predicates together allow the versions in A = ∩ A_p.

A predicate is added to an entry whose version passes it or fails it, and
the difference is the one CLAIM-772 draws between anchoring and convention:

- a **descriptor** is one the entry passes when it is added, such as an
  exact value on a dimension that was undescribed. Adding it moves nothing:
  it only excludes other versions, so the admissible sets go down and the
  entry stays in each. The dimension stops drifting at the entry's own
  value, which puts it in the conserved part (TERM-132);
- an **imposition** is one the entry fails when it is added, such as a
  schema default it did not meet. Enforcing it moves the entry to the
  predicate's value, and if that value is common to entries the dimension
  carries nothing of this one: the contracting part, at the convention.

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
