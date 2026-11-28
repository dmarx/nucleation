---
number: 1369
status: Proposed
formerly:
- CLAIM-tmp6toz6
title: 'Derived projections inflate retrieval prominence'
statement: >-
  Generated projections multiply an entry's retrieval prominence without
  adding evidence: a search over a record and its generated views meets the
  same entry's title and summary on many pages, and an entry met in ten
  projections is not ten independent pieces of evidence, so which surfaces
  a search covers is a retrieval policy to be governed apart from what the
  record holds
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A31 §14 of the exchange "Alignment consequences
    brainstorm" (ChatGPT, 2026-11-26). The count in the body is the
    assistant's, made on the working tree of 2026-11-26 with python3 -I
    (25 claims drawn with seed 1, each code searched in the 1,088 markdown
    pages under docs/).
role: thesis
warrant: interpretive
defeated_if: >-
  A comparison of agent inquiries run with and without the generated views
  in their search path, on tasks whose answers the record holds, finding
  that entries repeated across many projections are no more often taken
  as the answer, cited, or treated as better supported than entries of
  comparable relevance repeated across few; or an argument that the
  repetition carries information a reader needs (each projection placing
  the entry in a different relation) so that it is not mere duplication.
tags:
- information-retrieval
- design-rationale
- epistemology
date: '2026-11-26'
line:
- record-as-apparatus
bears_on:
- QUESTION-109
summary: >-
  A31 §14: "A claim that appears in ten projections is not ten independent
  pieces of evidence." Generated indexes, tag pages, line pages, chains and
  accounts repeat entries' titles and summaries, so an unrestricted search
  meets one entry many times, which A calls "artificial prominence"; the
  remedy A offers is a purpose-specific retrieval surface, not fewer views.
  On the working tree of 2026-11-26 a claim's code appears on a median of
  25 generated pages. It is the retrieval-side form of the danger
  [CLAIM-301](CLAIM-301.md) names, and of A43's "repeated citation of derivative claims as
  independent evidence" ([CLAIM-184](CLAIM-184.md), note of 2026-11-12). The wording is
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-301 CLAIM-184 CLAIM-183 CLAIM-1394 — Proposed; the claims and the lead this one is filed among on 2026-11-26 -->

# CLAIM-1369: Derived projections inflate retrieval prominence

## The claim

A31 §14 of the exchange: Luria "generates numerous indexes, tag pages,
line pages, chain pages, reports and projections. Many of these repeat the
same entry titles and summaries. If an agent performs an unrestricted
repository search, it can encounter the same underlying information across
several generated files. That can produce artificial prominence." And: "A
claim that appears in ten projections is not ten independent pieces of
evidence."

On this record the multiplier is larger than A's example. Of 25 claims
drawn at random, each code appears on between 10 and 75 of the 1,088
markdown pages under `docs/`, median 25.

A's remedy is a table of purposes and preferred surfaces: a canonical index
to find a concept, the working account for the current position, a line's
projection to investigate a line, the entry and its chain to trace a
dependency, archive and journals for history, the complete record for
exhaustive verification. "The existing generated indexes need not
immediately disappear. But agent workflows should avoid searching both
authoritative sources and all their derived copies by default."

## Where it sits

- [CLAIM-301](CLAIM-301.md): iterative retrieval can turn a provisional framing into a
  premise, since a framing selects what is encountered. Repetition across
  projections is one way an entry gets encountered more than its relevance
  warrants.
- [CLAIM-183](CLAIM-183.md) holds the other face of generated views: fed back into an
  exchange they become instruments of the argument. This claim does not
  deny it; it concerns search that meets the views as copies.
- [CLAIM-1394](CLAIM-1394.md): duplication adds to the accessible corpus without adding
  information, which is the case that hypothesis is about.

## What it does not say

- It does not say generated views should go. A's point is about which of
  them a search covers.
- It does not say an agent is in fact misled by the repetition; that is
  what the defeater would test.
