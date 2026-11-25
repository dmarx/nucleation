---
status: Proposed
title: 'Only judgements need keeping as feed memory'
statement: >-
  The memory of a feed divides into the history of its data, of its
  definition and of its decisions; where the feed is a deterministic query,
  why an object was included follows from the first two as its
  why-provenance, so only judgements, such as an editor's tag or an owner's
  ruling, must be kept as events, and a luria record keeps them in its
  sources while its generated views keep none
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
  A deterministic view, with its data and its definition versioned, for
  which why an object was included at some past state cannot be recovered
  from those two histories; or a luria record whose generated views hold
  a judgement that no source does.
tags:
- databases
- software-engineering
date: '2026-11-25'
line:
- records-of-inquiry
- record-as-apparatus
- scholarly-publishing
uses:
- TERM-tmpx49xx
rests_on:
- CLAIM-tmpmq8lk
grounds:
- THEORY-367
complements:
- CLAIM-tmpzsuh2
summary: >-
  The assistant's, filling a gap the idea ledger found in U5 and A11 of
  the exchange "Hyper article interpretation" (2026-11-22): what a
  feed's memory must keep, and whether a feed with memory is a journal.
  A11 says a memory "can tell you why"; this says when the why must be
  stored and when it can be recomputed, and where a luria record keeps
  each part. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpmq8lk CLAIM-tmpzsuh2 CLAIM-tmpnqzvj CLAIM-tmp80nuw — Proposed; the owner's feed and journal, A's claims on the memory and the tag, and the assistant's claim on what lives on the host -->

# CLAIM-tmptn64c: Only judgements need keeping as feed memory

## The gap

U5 defines a feed as "A 'view' (with a memory) over data", and A11 says
the memory is "durable provenance for the decisions and events that
shaped the view", not a cache ([CLAIM-tmpmq8lk](CLAIM-tmpmq8lk.md)). Neither says which
decisions must be stored. A view can change because its data changed,
because its definition changed, or because someone judged.

## The claim

**Three histories.** A feed's state at a time is fixed by the data then,
the definition then, and any judgements made into it then. Its memory can
keep each.

**The first two suffice for a query.** If the feed is a deterministic
function of its data and definition, then given both histories, its state
at any past time can be recomputed, and why each object was in it can be
read off the derivation. For positive relational queries that "why" is
the object's why-provenance, the minimal sets of source facts from which
the query still derives it ([THEORY-367](../theory.d/THEORY-367.md), Buneman, Khanna and Tan). A cache
of past outputs adds nothing to that except speed. A ranking that reads
engagement, or a random draw, is deterministic only once those inputs are
counted as data.

**Judgements must be kept.** An editor's tag, a review or an owner's
ruling is not derived from anything the feed holds. If it is not kept as
an event, with author, target and reason ([CLAIM-tmpnqzvj](CLAIM-tmpnqzvj.md)), the why is
lost. That is the part of A11's memory that is not a cache.

**A luria record.** Its data are the sources, kept with their history in
git. Its definition is `luria.yaml`, whose changes are decided in ADRs and
kept in git. Its judgements (statuses, rulings, the voice each entry is
filed in, the curation entries saying what was filed and why) are written
into the sources themselves, as history notes and journal entries, so far
as they have been filed: the owner's choices are first written on the
host, in pull-request descriptions ([CLAIM-tmp80nuw](CLAIM-tmp80nuw.md)). Its
generated views are rebuilt by `luria index`, hold no hand-written file,
and keep only the git history of their outputs on the default branch. So
the record taken whole is a feed in the owner's sense, and none of its
views is: each view is a query over a memory kept elsewhere.

## Is a feed with memory a journal?

Not by that alone. The owner's U4 makes a journal a feed over editors
([CLAIM-tmpzsuh2](CLAIM-tmpzsuh2.md)): a feed whose data are judgements. A feed with memory
over raw data is an index or an archive. On this account a journal is a
feed whose data include attributable judgements, kept as events, with its
rule for combining them declared (A10's "what their feeds actually mean").
The record is one in this sense, with a single editor: the owner's
rulings, kept in its sources.

## What it does not say

Not that judgements are arbitrary, only that they are not derivable from
what the feed holds.
