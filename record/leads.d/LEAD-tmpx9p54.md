---
status: Open
title: "Define a metric on the record's argument graph and compute routes through it, testing whether the routes an editor proposes are walks on the graph's typed edges and how far they are from the shortest"
version: 1
stage: specified
method:
- formal
- operationalization
tags:
- design-rationale
- network-science
date: '2026-11-25'
line:
- record-as-apparatus
advances:
- TERM-tmp1bef0
- CLAIM-tmpc4q8o
summary: >-
  A gap fill (ADR-137) for A61 of the exchange "Hyper article
  interpretation" (2026-11-25), whose geodesics are "editorial metaphors,
  not yet computed shortest paths through Nucleation's argument graph":
  "geodesic" has no metric. A first check by script finds that of the
  nine consecutive steps in four of A61's routes, three follow a stored
  edge and six do not. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: TERM-tmp1bef0 CLAIM-tmpc4q8o CLAIM-794 SYNTHESIS-012 CLAIM-181 SYNTHESIS-056 ADR-143 CASE-253 — Proposed, Open or new; the term and thesis it advances, the entries the shortest paths pass through, the manuscript protocol, the selection question and a proposed study on the route -->

# LEAD-tmpx9p54: Define a metric on the record's argument graph and compute routes through it, testing whether the routes an editor proposes are walks on the graph's typed edges and how far they are from the shortest

## The gap

A61 calls its routes geodesics and admits the word is a metaphor: "building
a graph that could identify and score such routes would be an
interesting extension of the atlas", with edges that "aren't merely
shared tags" but carry "different kinds of warrant: formal dependency,
empirical application, conceptual translation, analogy, or open
conjecture". A shortest route needs a length.

## A first check

The assistant built the undirected graph of every code-valued relation in
the record's frontmatter (python3 -I, this session; tags, lines, works and
history left out) and tested A61's routes step by step:

- "The Knowledge Graph That Lied": CASE-131 to CLAIM-469 is a stored edge
  (CLAIM-469 grounds on it), and CLAIM-469 to CLAIM-419 is one (it rests on
  it). CLAIM-419 to CLAIM-470 is not: the shortest path is two steps, through
  CLAIM-794. CLAIM-470 to CASE-084 is three, through SYNTHESIS-012 and
  CLAIM-181.
- "One Complaint, Two Correct Classifications": CASE-132 to TERM-064 is two
  steps, through SYNTHESIS-056; TERM-064 to CLAIM-523 is an edge (CLAIM-523
  uses it).
- "More Resources Don't Always Mean Finer Categories": CLAIM-387 to
  CLAIM-470 is three steps.
- "The Record That Proved Itself Right": CASE-084 to CASE-162 is five steps,
  CASE-162 to CLAIM-266 three, CLAIM-266 to CASE-253 two.

So three of the nine steps follow a stored edge. The others are joins the
editor makes and no entry states, the kind ADR-143's third invariant asks a
manuscript to file before it is ready.

## The design

- **Edges.** The record's typed relations, each with a length by kind:
  `rests_on` and `grounds` short, `complements` and `uses` longer, an
  ARG's step by its `form` (formal-application shorter than analogy), and
  a membership in a synthesis longest, since it says only that an
  account holds both.
- **Routes.** Shortest paths between a starting entry and a target, and
  routes constrained to return (orbits), on that metric.
- **Test.** For each route an editor proposes, the share of its steps that
  are stored edges, and its length against the shortest. A step with no
  short path is a join to file, or a sign the route crosses what the
  record keeps apart.
- **What it would settle.** Whether "geodesic" can be made exact on the
  record, and whether editors' routes cross unrecorded joins at a rate
  that matters. QUESTION-258's selection problem is the same graph's other
  use.
