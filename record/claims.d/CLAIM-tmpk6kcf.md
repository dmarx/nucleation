---
status: Proposed
title: 'Code citations resolve to the current version'
statement: >-
  In a luria record a citation by code, read on the branch or from another
  record, resolves to the entry's current version and not to the version
  cited, because entries are rewritten to stay true, and a content pin
  detects that a cited document changed since it was vouched for without
  making the vouched version reachable, so a citation that must reach the
  version it relied on has to name a commit
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
warrant: demonstrated
defeated_if: >-
  A luria citation form, or a convention this record follows, that
  resolves a code to a stated version of the entry; or a pin that stores
  a reference from which the vouched version can be fetched and not only
  a hash it can be compared with.
tags:
- software-engineering
- design-rationale
date: '2026-11-25'
line:
- record-as-apparatus
- scholarly-publishing
complements:
- CLAIM-789
- CLAIM-tmp48g02
summary: >-
  The assistant's, filling a gap the idea ledger found where A5 and A10
  of the exchange "Hyper article interpretation" (2026-11-22) put Nucleation
  forward as a hyperarticle: A5 requires that "A citation to a particular
  version should remain resolvable even after the living document
  evolves", and A10 that a tag link "a particular versioned scholarly
  object". The record versions its entries; its citations do not name the
  versions. Checked against luria's documentation and this record's
  remotes.lock.json on 2026-11-25. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-789 CLAIM-tmp48g02 CLAIM-tmpgli4k CLAIM-tmpnqzvj CLAIM-tmpjf44i — Proposed; the claim on exact copying, A45's reference-implementation claim, A's claims on citing and tagging a version, and the owner's thesis -->

# CLAIM-tmpk6kcf: Code citations resolve to the current version

## The gap

A5: "A citation to a particular version should remain resolvable even
after the living document evolves." A10 binds a tag to "a particular
versioned scholarly object" ([CLAIM-tmpnqzvj](CLAIM-tmpnqzvj.md)), and [CLAIM-tmpgli4k](CLAIM-tmpgli4k.md) has a
citation name "the version they used". The owner offers Nucleation as a
hyperarticle ([CLAIM-tmpjf44i](CLAIM-tmpjf44i.md)). Does it meet the requirement?

## The claim

- **Entries are versioned.** Each carries `version` and a `history` that
  says what changed, and luria's lint refuses a version bump with no
  account of itself. Git keeps every earlier text.
- **Codes name entries, not versions.** Inside the record a code is
  repaired into a relative link, which resolves against whatever revision
  the reader is viewing: on the branch, the entry's current text; at the
  commit where the citing text was written, the text it relied on. A
  foreign code is a link to the other record's branch (this record's
  remotes name `ref: main`), so it always reaches the current text. The
  record rewrites entries to keep them true ([LU-DP-017](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-17): "A record states
  what is true now — git already keeps what was written then"), so what a
  code reaches on the branch tomorrow need not be what the citing text
  relied on.
- **Pins detect, they do not reach.** For foreign codes, `luria remotes
  --pin` "stores a hash of each cited document in the lockfile as an
  endorsement", and the lint reports each pinned document "that changed
  since a human vouched for it" (luria, docs/project-memory.md). A hash
  tells that the text moved; it is not a link to the text vouched for.
  This record pins nothing: its remotes.lock.json holds discovered titles
  and no content pins (checked 2026-11-25).
- **So a version is reached by commit.** A link to the file at a commit
  reaches the cited version, and nothing in the record's citation syntax
  writes one. The entry's `version` number is not enough: no luria link
  takes one.

This is [CLAIM-789](CLAIM-789.md)'s point from the other side. Copying exactly anchors a
copy to the version it was taken from; a code is the other kind of tie, one
a revision passes through, so it follows the entry. A reader who wants the
version relied on must browse by commit, and a reader outside the record
must be given the commit.

## What it does not say

It sharpens [CLAIM-tmp48g02](CLAIM-tmp48g02.md), whose body notes that "versions are git's": they
are, and the record's citations do not reach them.

Not that following the current version is wrong. Inside the record it is
the point: a dependant should meet its premise as it now stands, and
retirement reports what rests on an entry ([CLAIM-664](CLAIM-664.md)). The gap is for a
reader outside, citing a claim as it stood.
