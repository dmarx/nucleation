---
status: Proposed
title: 'Keeping an entry costs its retrieval, not only its storage'
statement: >-
  Keeping an entry costs its retrieval, not only its storage: retired and
  superseded entries still add to the cost of retrieval and lower
  discoverability, as do Proposed or Active entries that nothing develops
  further, and redundant content in entries that were developed on could be
  condensed or removed; the record prices whether to keep information, but
  its apparatus offers only present or absent, with no grading of how
  readily what is kept is reached
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A measure of retrieval on the record's own tasks, the time, tokens or
  misses it takes to reach what a task needs, that does not improve when
  retired, idle or redundant entries are taken out of default retrieval
  while what the task needs stays reachable; or a showing that the
  apparatus already grades how readily its entries are reached, beyond the
  status an entry carries. A count of how much of the record is retired
  bears on how much the first clause can buy, not on whether it holds.
tags:
- information-retrieval
- databases
- design-rationale
date: '2026-11-26'
line:
- records-of-inquiry
- record-as-apparatus
bears_on:
- QUESTION-tmpz8xkx
summary: >-
  The owner's, at U15 of the exchange "Alignment consequences brainstorm"
  (ChatGPT, 2026-11-26), offered as "one immediate opportunity", controlled
  forgetting, prompted by "how large nucleation has gotten". The record
  prices the keeping of an entry ([CLAIM-303](CLAIM-303.md), [CLAIM-308](CLAIM-308.md), [CLAIM-314](CLAIM-314.md)); the
  owner's point is that what it keeps is all equally present. Filed in the
  owner's voice. The section "The record as it stands" is the assistant's
  (Claude, in this session): at the commit this filing was cut from,
  retired entries were 1.9 % of the record's entries and 1.4 % of its
  bytes, Proposed ones 25 %, and dated notes 23 % of the bytes of claims
  and 30 % of questions, so the owner's later clauses carry most of the
  weight; and the apparatus already keeps one cold store, git history, for
  versions though not for entries. Adopting the assistant's sections is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-314 CLAIM-891 CLAIM-184 CLAIM-1290 CLAIM-tmp5zt7f TERM-tmp96b3g TERM-tmp3t5jq CLAIM-tmpg2wk1 CLAIM-tmpdkwbk LIT-tmp8113m CLAIM-tmpdid0k — Proposed or Deferred; held claims the owner's point extends and the entries filed from the same exchange on 2026-11-26 -->

# CLAIM-tmpu1fef: Keeping an entry costs its retrieval, not only its storage

## The claim

The owner, at U15 of the exchange "Alignment consequences brainstorm"
(https://chatgpt.com/share/6b07d7ae-9434-83ea-888b-9b20796f291c):

> one immediate opportunity is controlled forgetting. consider how large
> nucleation has gotten. retired and superseded content still impacts
> retrieval cost and discoverability, as do proposed/active items that
> don't contribute to further development, and even developed-upon content
> which contains redundant information could potentially even be condensed
> or removed. nucleation provides some guidance on how to price the cost of
> keeping information or not, but luria doesn't even have a hot vs warm vs
> cold storage distinction, just present or not.

Three kinds of entry are named as costs: the retired, the idle (Proposed or
Active entries that nothing builds on), and the redundant (content in
developed entries that later entries restate). Three remedies are named or
implied: grading what is kept by how readily it is reached (hot, warm,
cold), condensing, and removing. The claim is about the record's apparatus,
luria, as well as about this record: it can say whether an entry is in
force, not whether it should be in the way.

## What the record already prices

The owner's "some guidance on how to price the cost of keeping information"
is held. [CLAIM-303](CLAIM-303.md) prices filing against later reconstruction, and
[CLAIM-308](CLAIM-308.md) gives the competitive filing rule when reuse cannot be
forecast. [CLAIM-314](CLAIM-314.md) is the nearest held claim to this one: recognizing
which filed argument answers a new question costs more as the store grows,
so "each filing raises the cost of later reuse and per-item break-even
decisions are not independent". [CLAIM-891](CLAIM-891.md) prices a filed argument partly
by "what recognizing it costs in a growing store". Every one of these prices
admission. None prices an entry's continued place among what a search or a
reader meets, which is the owner's point. [CLAIM-184](CLAIM-184.md) is the closest on
retirement: retirement by status remedies entrenchment "only if superseded
anchors stop attracting new structure", and it names a count that would
show whether they do.

## The record as it stands

*The assistant's (Claude, in this session), counted with `python3 -I` over
the tree at commit 95013454, before this filing's entries.* The record held
11,320 entries in its eleven schemes, 81.6 MB of source:

- **Retired** (Superseded, Rejected, Dissolved or Dropped): 220 entries,
  1.9 % of entries and 1.4 % of bytes. Taking every retired entry out of
  default retrieval would barely shrink it.
- **Proposed:** 2,831 entries, 25.0 % of entries and 22.9 % of bytes, 1,365
  of them THEORY readings and 818 CLAIMs. Which of them nothing develops is
  not counted here.
- **Unread works:** 893 LITs are Unavailable, Deferred or Unfetched.
- **Accreted notes:** dated "Note of" sections are 23.0 % of the bytes of
  CLAIMs, 30.2 % of QUESTIONs and 22.7 % of TERMs, in 761 of 1,347 CLAIMs.
  These are the likeliest place for the owner's "developed-upon content
  which contains redundant information".
- **The largest scheme** is NOTE, 29.5 MB of 81.6.

So the owner's first clause, retired content, is real but small at this
size; the second and third, idle and redundant content, are where a
measure would have to look. A count is not the measure the `defeated_if`
asks for: whether removing an entry from default retrieval helps depends
on how often it is met in tasks that do not need it, and nothing here
measures that. [LEAD-tmpeqy94](../leads.d/LEAD-tmpeqy94.md) would, and so would [LEAD-tmpolbqp](../leads.d/LEAD-tmpolbqp.md)'s trial on
one line and [LEAD-tmpe579v](../leads.d/LEAD-tmpe579v.md)'s replay of retention policies over the
record's history, both filed from U17 to U19 of the same exchange.

## What the apparatus already has

*The assistant's.* "Just present or not" holds for entries and not quite for
versions. Luria's own principle on rewriting ([LU-DP-017](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-17), "A record states
what is true now — git already keeps what was written then") treats git
history as the store of what an entry used to say, so a rewritten entry's
old text is already cold: kept, reachable by commit, out of every view.
[CLAIM-1290](CLAIM-1290.md) is the cost of that: a citation by code reaches the current
version, and reaching the one relied on needs a commit. For entries the
record forbids the move: "Retire by status, never by deletion"
(CLAUDE.md's enforced rules), so a retired entry stays in the tree, in the
views and in every search. A tier between in force and deleted is what is
missing.

## What it bears on

A34, later in the same exchange, states the claim generally and with a
threshold as its second hypothesis ([CLAIM-tmpdid0k](CLAIM-tmpdid0k.md), filed from U17 to
U19): past some point, a larger readily accessible corpus raises the cost
of the inquiries it already holds enough to support.

[QUESTION-tmpz8xkx](../questions.d/QUESTION-tmpz8xkx.md) asks what a governed record should cool, condense or
erase. A's answers in the same exchange are filed apart: the separation of
standing, availability and fidelity ([CLAIM-tmp5zt7f](CLAIM-tmp5zt7f.md), [TERM-tmp96b3g](../terms.d/TERM-tmp96b3g.md)), the
operations of cooling and consolidation ([TERM-tmp3t5jq](../terms.d/TERM-tmp3t5jq.md)), the pricing of a
tier ([CLAIM-tmpg2wk1](CLAIM-tmpg2wk1.md)) and the condition that cooling leave dependencies
visible ([CLAIM-tmpdkwbk](CLAIM-tmpdkwbk.md)). Luria's name already states the danger: it is
named for a mnemonist whose total recall worked against abstraction
([LU-ADR-011](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-011.md), [LIT-tmp8113m](../literature.d/LIT-tmp8113m.md), unread).
