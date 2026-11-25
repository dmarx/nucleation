---
status: Proposed
title: Publishing is a set of separable guarantees, persistent access, stable identifiers, versioned records, metadata, attribution, discoverability and preservation, which different providers can give, so the identity of a scholarly object must be independent of the identity of its host, and keeping it online is distinct from keeping it after the host fails
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A guarantee on the list that one provider cannot give without also
  giving another, so that the set is not separable in practice; or a
  showing that a scholarly object whose identity is independent of its
  host cannot be authenticated across hosts, so that independence costs
  the trust in its versions that a single host gives.
tags:
- society-and-governance
- software-engineering
date: '2026-11-25'
line:
- records-of-inquiry
- scholarly-publishing
complements:
- CLAIM-tmpv0sv7
summary: >-
  A13 of the exchange "Hyper article interpretation" (2026-11-22),
  developing the owner's U6 ([CLAIM-tmpv0sv7](CLAIM-tmpv0sv7.md)): "these are separable
  guarantees", "The identity of the research must be independent of the
  identity of the host", and "A host can promise uptime; a custodian must
  also arrange for persistence after the host itself fails." Its slogan:
  "Scientific publishing should be a protocol, not a place." The
  assistant's check of the migration test on this record is
  [CLAIM-tmp80nuw](CLAIM-tmp80nuw.md). The wording is A's (ChatGPT's, at A13 of the exchange
  "Hyper article interpretation"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpv0sv7 CLAIM-tmp80nuw CLAIM-tmpzz0eu — Proposed; the owner's thesis, and the assistant's gap fills -->

# CLAIM-tmpk6vy2: Publishing is a set of separable guarantees, persistent access, stable identifiers, versioned records, metadata, attribution, discoverability and preservation, which different providers can give, so the identity of a scholarly object must be independent of the identity of its host, and keeping it online is distinct from keeping it after the host fails

## The claim

A13: "A scholarly webhost needs to provide some combination of persistent
access, stable identifiers, versioned records, machine-readable metadata,
attribution, discoverability, accessibility, and preservation. But the
important observation is that these are separable guarantees." It cites
the separations already made: identifier registration apart from hosting
(Crossref, DataCite), and preservation apart from hosting (LOCKSS,
CLOCKSS). The record holds none of these as readings.

**The migration test.** "Suppose I publish a hyperarticle with Host A. A
few years later, Host A raises its prices, changes its policies, or shuts
down. What happens? Ideally, almost nothing interesting." Hence "The
identity of the research must be independent of the identity of the
host", with its claims, versions, relationships and contributor records
surviving the move. A13 says the hard part is trust across hosts: "Mirroring
content is relatively easy. Preserving a trustworthy record of revisions,
authorship, and editorial assessments across different providers is
harder."

**Host and custodian.** "A host can promise uptime; a custodian must also
arrange for persistence after the host itself fails. Those may be
different organizations, and making them different is arguably a
feature."

**Responsibility by failure.** "If a webhost loses data, that's a hosting
failure. If an editor falsely certifies a methodological review, that's
an editorial failure." Bundling "just places them under the same
institutional roof."

## What it does not say

Not that publishers do nothing: "the useful things publishers do are
services, and services can be provided independently of editorial
authority." Which functions, and which a host lacks, is [CLAIM-tmpzz0eu](CLAIM-tmpzz0eu.md).
