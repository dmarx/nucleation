---
status: Proposed
title: 'availability'
statement: >-
  availability (of an entry): how readily an entry the record keeps enters
  its ongoing work, fixed by which retrieval and review operations meet it
  by default, independently of its standing; graded hot (met by default
  search, routine views, review and the context an agent is given), warm
  (met as a compact representation, the full entry fetched when relevant,
  its reactivation conditions watched), cold (left out of ordinary
  retrieval, reached by code, by explicit archive search or by a trigger)
  and purged (full content no longer kept within the record, a minimal
  identity or disposal record left), with dependency tracking kept at
  every tier above purged
version: 1
tags:
- information-retrieval
- databases
- design-rationale
date: '2026-11-26'
line:
- records-of-inquiry
- record-as-apparatus
summary: >-
  A27 §§3 and 11 of the exchange "Alignment consequences brainstorm"
  (ChatGPT, 2026-11-26), after the owner's U15 ([CLAIM-tmpu1fef](../claims.d/CLAIM-tmpu1fef.md)). The job
  of the definition is to let the record say that an entry is in force and
  out of the way, or retired and in the way on purpose ([CLAIM-tmp5zt7f](../claims.d/CLAIM-tmp5zt7f.md)).
  The tiers are logical, not storage: "most of Nucleation's immediate
  memory problem is probably not the cost of storage. It is the cost of
  attention", which A calls "a hypothesis worth measuring rather than
  assuming". A29 §6 adds admission apart from eviction (TinyLFU,
  [LIT-tmp7yb7v](../literature.d/LIT-tmp7yb7v.md)) and a ghost representation for cold entries (ARC,
  [LIT-tmpua7jt](../literature.d/LIT-tmpua7jt.md)). The wording is A's (ChatGPT, in the exchange of
  2026-11-26); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpu1fef CLAIM-tmp5zt7f CLAIM-tmpdkwbk LIT-tmp7yb7v LIT-tmpua7jt LIT-tmp6hqrz CLAIM-1068 CLAIM-tmpg2wk1 — Proposed or Deferred; filed from the same exchange on 2026-11-26, and a held claim cited -->

# TERM-tmp96b3g: availability

## Definition

How readily an entry the record keeps enters its ongoing work. A27 §3
defines the tiers by organizational state, not by where the bytes are:

- **Hot, working knowledge.** "Participates in default retrieval, routine
  synthesis, ongoing review and ordinary agent context construction."
- **Warm, maintained nuclei.** "Compact representations remain
  discoverable. Full material is retrieved when relevant. Important
  reactivation conditions remain monitored."
- **Cold, historical archive.** "Excluded from ordinary retrieval.
  Recoverable by identity, historical investigation, explicit archive
  search or designated triggers."
- **Purged, intentionally unavailable.** "Full content is no longer
  retained within the defined storage boundary." It "Requires stronger
  justification because reconstruction may be impossible."

All but purged "could remain within the same Git repository".

## The retrieval contract

A27 §11: "The tier needs operational semantics."

| Operation | Hot | Warm | Cold |
|---|---|---|---|
| Default semantic search | Full | Capsule | Excluded |
| Ordinary generated views | Included | Selectively included | Separate archive view |
| Direct identifier lookup | Full | Resolvable | Resolvable |
| Dependency tracking | Yes | Yes | Relevant metadata retained |
| Historical inquiry | Yes | Yes | Yes |
| Routine substantive review | Regular | Triggered or periodic | Triggered |
| Automatic agent context | Eligible | On demand | Explicit recovery |

The row that makes it a tier and not a hiding place is dependency
tracking; [CLAIM-tmpdkwbk](../claims.d/CLAIM-tmpdkwbk.md) is the claim that it must hold.

## Moving between tiers

- **Admission is not working-set admission.** A29 §6, after TinyLFU
  ([LIT-tmp7yb7v](../literature.d/LIT-tmp7yb7v.md)): "admission to the record need not imply admission to the
  working set." The record has many rules for the first and none for the
  second.
- **Ghosts.** A29 §6, after ARC's ghost lists ([LIT-tmpua7jt](../literature.d/LIT-tmpua7jt.md)): a cooled entry
  keeps a small representation (code, title, standing, keywords, a pointer
  to the full version) searched by a second, cheap pass, so an inquiry that
  meets cooled material is offered its reactivation. A adds that a ghost
  list alone "is insufficient": the record also needs identity and
  dependency information. [CLAIM-1068](../claims.d/CLAIM-1068.md) is why the keywords matter: in the
  record's exchanges a code was found by what its content said, so an entry
  reachable only by code is not found when needed.
- **Reactivation.** A27 §12's triggers: "a new objection to a consolidated
  conclusion, a change to a formerly relevant assumption, repeated
  attempts to derive something already known, or the emergence of a new
  inquiry that intersects archived material." "Cooling should not require
  the organization to predict all future relevance accurately."
- **Grace periods, pins and tombstones.** A29 §12, after git's own
  collection and database tombstones: a cooled entry can be cooled
  provisionally, pinned against collection, or reduced to a record that a
  disposition happened, and restored without a new identity.

## What it does not fix

Who sets an entry's tier, and on what evidence: [CLAIM-tmpg2wk1](../claims.d/CLAIM-tmpg2wk1.md) prices a
tier, and [QUESTION-tmpz8xkx](../questions.d/QUESTION-tmpz8xkx.md) asks the rest. Nor does it say that agents will
honour it. A27 §13: "An AI agent searching the entire repository
indiscriminately would bypass the policy"; luria "would need to provide
suitable retrieval surfaces, not merely conventions about how agents ought
to search." MemGPT ([LIT-tmp6hqrz](../literature.d/LIT-tmp6hqrz.md), unread) is prior work on tiers an agent
manages for itself.
