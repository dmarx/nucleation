---
number: 985
status: Proposed
formerly:
- CLAIM-tmpo8u76
title: 'Change predicates fit neither sort'
statement: >-
  A predicate about how an entry may change, rather than what it is now, is
  neither passed nor failed when it is added, since its test is on versions
  not yet written; so it is neither a descriptor nor an imposition in the
  sense that predicates are sorted by whether the entry passes them when
  added, and two such predicates the present entry is consistent with can
  still conflict over what may be written next
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A sorting of predicates by passing that already decides predicates on
  future versions at the time they are added; or a pair of predicates on
  future versions that the present version is consistent with and that
  cannot conflict over any later version.
tags:
- logic
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
grounds:
- THEORY-2260
complements:
- CLAIM-783
- CLAIM-974
uses:
- TERM-134
- TERM-151
- TERM-154
summary: >-
  Offered by the Davies and Pfenning reader as an analogy only the two
  readings together show, and filed under the dialectic regime,
  2026-11-22. In Davies and Pfenning a reference cell's type governs future
  writes as well as present contents, which is why intersections are
  restricted to values. The record's sorting of predicates into
  descriptors and impositions decides each by the version it is added to;
  this claim says where that sorting stops. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

# CLAIM-985: Change predicates fit neither sort

## The claim

[CLAIM-783](CLAIM-783.md) sorts a predicate by whether the entry passes it when it is
added: a descriptor if it does, an imposition if it does not. Its part 6,
that descriptors never conflict, takes the entry's present version as the
witness. That works for a predicate on the present version. A predicate
on how the entry may change ("revised only to restore its source", "its
scope only ever narrows") is tested on a history, and the present version
is not a history: at the moment it is added it is neither passed nor
failed. It is a requirement whose test is deferred.

Davies and Pfenning show the shape. A reference cell holding a positive
number has both the types of a cell of naturals and a cell of positives
as a description of its contents now, yet as requirements on what may be
written next they conflict: one permits writing zero and the other
forbids it. That is why they restrict intersection to values. The
analogue in the record: two constraints on an entry's future revisions,
each consistent with what it says now, can leave no revision that
satisfies both.

## Scope

This narrows nothing [CLAIM-783](CLAIM-783.md) states, since part 6 is about predicates
the entry passes when added, and these are not. It names a third kind
the two-way sorting leaves out, and says that part 6 does not reach it.
It is an analogy from types to records; no record case is filed.
