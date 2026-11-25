---
number: 1302
status: Proposed
formerly:
- CLAIM-tmpmq8lk
title: A feed's memory is the durable provenance of the decisions and events that shaped it and not a cache of what it displayed, since a cache says what was shown and a memory says why, so a feed can be modelled as a versioned query with an append-only history of editorial actions, and curation becomes part of the record it curates
version: 3
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
- version: 3
  date: '2026-11-25'
  note: >-
    Joins the work hyperarticles (ADR-145): Article 3 of A45 in the
    exchange "Hyper article interpretation" states its proposition without
    citing it, in §6. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A feed whose kept output history, without any record of decisions,
  answers the questions A11 says a memory answers (what was considered
  important, which recommendations were revised, who identified a result
  first, and why each was included), so that provenance adds nothing a
  cache of outputs lacks.
tags:
- databases
- design-rationale
date: '2026-11-25'
line:
- records-of-inquiry
- scholarly-publishing
uses:
- TERM-177
rests_on:
- CLAIM-250
summary: >-
  A11 of the exchange "Hyper article interpretation" (2026-11-22),
  developing the owner's U5 ([TERM-177](../terms.d/TERM-177.md)): memory "means maintaining
  durable provenance for the decisions and events that shaped the view.
  The difference is that a cache tells you what was displayed. A memory
  can tell you why." And: "a feed could be modeled as a versioned query
  plus an append-only history of editorial actions", so that "Curation
  becomes part of the scientific record." The wording is A's (ChatGPT's,
  at A11 of the exchange "Hyper article interpretation"); adopting it is
  the owner's call.
works:
- hyperarticles
---

<!-- inactive-ok-file: TERM-177 CLAIM-250 CLAIM-1321 — Proposed; the owner's feed, what a record should preserve through revision, and the assistant's refinement -->

# CLAIM-1302: A feed's memory is the durable provenance of the decisions and events that shaped it and not a cache of what it displayed, since a cache says what was shown and a memory says why, so a feed can be modelled as a versioned query with an append-only history of editorial actions, and curation becomes part of the record it curates

## The claim

A11: "memory shouldn't mean merely keeping a cache of previously generated
feed results. It means maintaining durable provenance for the decisions
and events that shaped the view. The difference is that a cache tells you
what was displayed. A memory can tell you why."

The model: "a versioned query plus an append-only history of editorial
actions. That separates the current output from the decisions and
historical states that produced it." And so "curation isn't just how we
navigate the scientific record. Curation becomes part of the scientific
record."

## Where the record meets it

What a memory keeps, on this reading, is what [CLAIM-250](CLAIM-250.md) says a developing
argument should preserve through revision: its accountability structure,
what was asserted, why, how it was challenged and what justified the
change. The record's own curation journal is curation kept as part of the
record, in A11's sense. [CLAIM-1321](CLAIM-1321.md) (the assistant's) divides the memory
further and says where a luria record keeps each part.

## What it does not say

Not that the history must be append-only in a luria record, which rewrites
its entries to stay true and leaves the history of what was written to git
([LU-DP-017](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-17)).
