---
status: Proposed
title: 'Nucleation is a reference implementation of a governed research record and of views generated over it, not of hyperarticle publishing: it has no distributed editorial network and no archival or identifier guarantees beyond its repository'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the record already provides what A45 says it lacks, or that
  a hyperarticle needs nothing beyond a governed record and views over it.
tags:
- philosophy-of-technology
- design-rationale
date: '2026-11-25'
line:
- record-as-apparatus
complements:
- CLAIM-178
- CLAIM-469
- CLAIM-tmpjf44i
summary: >-
  A45 of the exchange "Hyper article interpretation" (2026-11-22), the third of three articles the
  owner asked for at U21: "Nucleation is a reference implementation of the
  underlying governed research record and of generating different
  navigational views over that record. It is not yet a complete
  implementation of hyperarticle publishing." A44 had set it as the third
  article's distinction, "between Nucleation as a working reference for
  governed source records and a complete hyperarticle network, which does not
  yet exist". One of A45's three lacks is corrected in the body. The wording
  is A's (ChatGPT's, at A45 of the exchange "Hyper article interpretation");
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-178 ADR-143 — Proposed; the manuscript-as-view claim and the manuscript protocol -->
<!-- inactive-ok-file: CLAIM-tmpjf44i — new; the hyperarticle thesis filed from the same exchange -->

# CLAIM-tmp48g02: Nucleation is a reference implementation of a governed research record and of views generated over it, not of hyperarticle publishing: it has no distributed editorial network and no archival or identifier guarantees beyond its repository

## The claim

A45, Article 3 §4: "the present system doesn't automatically compose
publication-ready prose, manage a distributed editorial network, or provide
all the identifier, archival, and version-resolution guarantees scholarly
publication would require. This article is manually composed." And: "That's a
partial implementation of the proposed relationship, not proof that the
whole publishing architecture works."

What the record implements: entries with stable codes, statuses, voices and
declared relations; views generated from them (the indexes, chains and
pages in `docs/`, and templates in `record/views.d`); and manuscripts written
as views over the argument ([CLAIM-178](CLAIM-178.md), [ADR-143](../decisions.d/ADR-143.md)).

## A correction to A45

"This article is manually composed" was true of A45, which ChatGPT wrote
from the outside. It is not the record's only way. [ADR-143](../decisions.d/ADR-143.md) (Proposed), dated
the day after the exchange, holds a protocol by which a manuscript is
written from the record as a view: each step cites the entry that holds it
with its standing, nothing in it is new to the record, and each version is
fact-checked against the entries. Three manuscripts are in
`scratch/manuscripts/`. Composition is assisted and checked, not automatic,
so A45's "automatically" stands; "manually" does not. Of the other lacks:
codes are stable across concretization, with the temporary code kept under
`formerly:`, and versions are git's; there is no editorial network, and no
archiving or identifier service beyond the repository's host. Those two are
what the record does not implement.

## What it does not say

- Not that the hyperarticle proposal ([CLAIM-tmpjf44i](CLAIM-tmpjf44i.md)) is right; only how far Nucleation goes
  toward implementing it.
