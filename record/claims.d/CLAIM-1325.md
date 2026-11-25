---
number: 1325
status: Proposed
formerly:
- CLAIM-tmpu6e4u
title: 'Sufficient views can be incomparable'
statement: >-
  Two evaluators of one research record facing the same decision can need
  incomparable views of it: the coarsest observations sufficient for a
  decision can be several and incomparable, so which view suffices depends
  on which acceptable action an evaluator commits to and not on the decision
  alone
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing: it is about evaluating and
    publishing research over a record, and the line's first synthesis
    (SYNTHESIS-126) integrates it. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A research-evaluation decision whose acceptable actions, over the
  circumstances evaluators face, never overlap in the way CLAIM-535's
  incomparability needs, so that each decision has one coarsest
  sufficient view; or an error in CLAIM-535's construction.
tags:
- society-and-governance
- design-rationale
date: '2026-11-25'
line:
- scholarly-publishing
- record-as-apparatus
- will-organization
rests_on:
- CLAIM-535
- CLAIM-1323
complements:
- CLAIM-1292
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A24 §4 of the exchange "Hyper article
  interpretation" (2026-11-22). A24's design goal, "Provide the
  distinctions required for justified action", reads as though one
  decision fixed one set of distinctions. [CLAIM-535](CLAIM-535.md) says otherwise: where
  acceptable actions overlap, the coarsest sufficient observations are
  several and incomparable. A three-circumstance example, checked by
  script, shows it. Hence two evaluators facing one decision over one
  record can legitimately need incomparable views, which gives the
  owner's many-views thesis ([CLAIM-1292](CLAIM-1292.md)) a reason from [CLAIM-535](CLAIM-535.md) and
  not only from audiences' interests. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1323 CLAIM-1292 — Proposed; the claim this qualifies and the owner's claim it complements -->

# CLAIM-1325: Sufficient views can be incomparable

## The gap it fills

A24 §4 of the exchange "Hyper article interpretation"
(https://chatgpt.com/share/6b064f1b-9ea8-83e8-951e-634ed41675b6) concludes
that "which distinctions need to be legible depends on what decisions the
institution needs to make", and sets the goal "Provide the distinctions
required for justified action" ([CLAIM-1323](CLAIM-1323.md)). [CLAIM-535](CLAIM-535.md)'s title says
more: "where acceptable actions overlap the coarsest observations that
suffice are several and incomparable, so which distinctions must be made
legible depends on which acceptable action the organization commits to."
A24 drops the second half. The decision does not fix the distinctions; a
commitment within it does.

## The check

Three circumstances, with acceptable actions A(1) = {a, b}, A(2) = {b} and
A(3) = {a}. Every circumstance has an acceptable action, but an evaluator
who tells none apart has none common to all three. A script run with
`python3 -I` enumerated the five partitions of {1, 2, 3} and kept those
whose cells each share an acceptable action:

- sufficient: {1,2 | 3}, {1,3 | 2} and {1 | 2 | 3};
- coarsest sufficient: {1,2 | 3} and {1,3 | 2};
- neither refines the other.

An evaluator who commits to b in circumstance 1 must tell 3 from the rest.
One who commits to a must tell 2 from the rest. Both views are minimal, and
neither contains the other.

## The claim

Put in research-evaluation terms, the circumstances are kinds of record a
committee may face, and the actions are what it may do. Two committees with
the same decision and the same acceptable actions can each be justified in
asking for a different, incomparable view of one record. A record that
serves evaluation must then be able to yield more than one minimal view.
That is the owner's thesis ([CLAIM-1292](CLAIM-1292.md)), reached from [CLAIM-535](CLAIM-535.md) rather
than from differences of interest between audiences.

## What it does not say

- Not that real evaluation decisions have overlapping acceptable actions of
  this shape. The example shows that they can. Whether a tenure or a grant
  decision does is the defeat condition.
- The example is demonstrated within its stated model, and the reading of
  evaluators as [CLAIM-535](CLAIM-535.md)'s organizations is interpretive. The warrant
  given is the claim's as stated.
