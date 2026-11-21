---
status: Proposed
title: 'A reframe of an entry, a change in how its content is framed whether or not its wording changes, is recorded in that entry''s own prose, in a dated Reframings section saying who reframed it, the framing before and after, and what the reframe changed; a version still records a changed title or claim, and a term''s senses stay how a term holds framings side by side'
version: 1
tags:
- record
- process
date: '2026-11-21'
summary: >-
  The owner, 2026-11-21: "do we have a mechanism/convention for documenting
  reframes? If not, I propose we should add them to the prose of the
  relevant claim or whatever. I think we're sort of doing this already for
  TERMs via how we describe multiple senses." The record had none: a
  reframe showed up as a version's history note, a curation entry's
  narrative, or a term's senses, and not in the body a reader reads. An
  entry reframed now carries a Reframings section in its prose. First
  application: the two reframes of 2026-11-20 on [CLAIM-772](../claims.d/CLAIM-772.md) and [CLAIM-778](../claims.d/CLAIM-778.md).
---
<!-- inactive-ok-file: CLAIM-772 CLAIM-778 — Proposed; the first application -->

# ADR-tmpd4rgx: A reframe of an entry, a change in how its content is framed whether or not its wording changes, is recorded in that entry's own prose, in a dated Reframings section saying who reframed it, the framing before and after, and what the reframe changed; a version still records a changed title or claim, and a term's senses stay how a term holds framings side by side

## Context

Much of the record's recent development has come by reframing: the owner
restating an account in other terms, and the record's entries following.
On 2026-11-20 the owner asked whether stabilization and contraction were
one phenomenon, and [CLAIM-772](../claims.d/CLAIM-772.md) was rewritten as one contraction; [CLAIM-778](../claims.d/CLAIM-778.md)
moved from "constraints accumulate" to "copied with error". On 2026-11-21
the owner reframed the narrowing as the accrual of predicates, each a
constraint, and fixed "stabilization" in its control-theoretic sense.

The record caught each of these, but in places a reader of the entry does
not look:

- **A version's history note** says what changed in the title or claim. It
  sits in front matter, is written as a change log, and is not written when
  a reframe changes no wording.
- **A curation entry** tells the story of a filing, the reframe among other
  things, and is not linked from the entry as its framing.
- **A term's senses** ([ADR-050](ADR-050.md); [TERM-071](../terms.d/TERM-071.md), [TERM-088](../terms.d/TERM-088.md)) hold several
  framings of one word side by side. That is the nearest the record had to
  a convention, and it works for terms because a term's senses are its
  content.

So a claim read today does not say what framing it replaced, or that the
owner's turn is where its present framing came from. A reframe that changed
the account and not the title leaves no mark on the entry at all.

## Decision

**A reframe is recorded in the prose of the entry it reframes.** A reframe
is a change in how an entry's content is framed: the mechanism it is
explained by, the vocabulary it is stated in, or the question it is taken to
answer. It need not change the entry's wording, and it need not be the
owner's.

**Where.** A section `## Reframings`, after the sections that state and
limit the entry and before its tests and dated notes, one dated paragraph per reframe, oldest first. Each
says:

- **who** reframed it and **where**: the owner at a turn of a session, a
  reader, the assistant, quoted where the reframe was in words;
- the framing **before** and **after**, each in a sentence;
- **what it changed**: the wording, the account, the sense of a word, or
  nothing yet; and where the reframed content lives, in this entry's next
  version or in another entry it names.

**With a version, not instead of one.** If the reframe changes the title or
the claim, the entry also takes a version and a history note, as now. The
note says what changed; the section says what framing it was changed from
and to, in prose the entry keeps.

**Terms.** A term's senses stay how a term holds framings side by side. A
reframe of a term that keeps its definition goes in a Reframings section as
for any entry. One that changes the definition is a new term that supersedes
the old ([ADR-032](ADR-032.md)), and the new term's Reframings section names the
framing it replaced.

**Not a reframe.** Correcting an error is not a reframe, nor is a revision
that keeps the framing and fixes a step. Those go in history notes and
curation entries as now; when an owner's correction is what fixed it, the
curation entry quotes it.

## Alternatives considered

- **A scheme of its own, REFRAME.** It would give each reframe a code and
  a page. But a reframe is about one entry or a few, and a separate page is
  one more place a reader of the entry does not look, the problem this
  decision is for. If reframes come to cross many entries, a scheme can be
  added then.
- **History notes only.** They already exist and are terse, which is the
  point of them. They are not written when the wording is unchanged, and
  they do not keep the before-and-after framing in prose.
- **Curation entries only.** The status quo. They hold the story of a
  filing, and they are where the reframes of this session were recorded;
  they are not read as the entry's framing.
- **A front-matter field, `reframed_by`.** A relation would say that a
  reframe happened, not what it was; the content is prose.

## Consequences

- Entries the owner reframes carry their framings with them, and a reader
  of a claim can see where its present terms came from.
- One more section for a filer to write when a reframe lands, and to keep
  ordered. The `read-and-file` skill's steps do not change; this is a
  convention of the body, not of intake.
- No lint checks it. If reframes go unrecorded in practice, a lint rule or
  a field is the next rung of [DP-3](../../docs/design-principles.md#dp-3)'s ladder.

## First application

The two reframes of 2026-11-20 are recorded in Reframings sections on
[CLAIM-772](../claims.d/CLAIM-772.md) (two mechanisms reframed as one contraction, at the owner's
question whether stabilization was monotone contraction) and [CLAIM-778](../claims.d/CLAIM-778.md)
(the narrowing reframed from accumulating constraints to features copied
with error). The reframe of 2026-11-21, predicates as constraints and
stabilization in the control-theoretic sense, is filed in pull request 568;
its Reframings paragraph on [CLAIM-778](../claims.d/CLAIM-778.md) is added once both pull requests are
in staging, so neither cites the other's temporary codes.
