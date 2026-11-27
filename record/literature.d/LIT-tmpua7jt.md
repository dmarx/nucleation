---
status: Deferred
status_note: >-
  Registered 2026-11-26 from A29 §6 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), which names "Megiddo and Modha's ARC
  algorithm". Not sought or read. The USENIX page links the paper's PDF at
  https://www.usenix.org/legacy/events/fast03/tech/full_papers/megiddo/megiddo.pdf,
  which answered HTTP 200 to a header request; it was not opened.
title: 'ARC: A Self-Tuning, Low Overhead Replacement Cache'
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed, not read. Held check before filing: record/literature.d searched
    for the title, "adaptive replacement", Megiddo and Modha; not held.
    Identifier check: Crossref has no DOI for the FAST '03 paper (it gives
    the later IEEE Computer article, Megiddo and Modha 2004, "Outperforming
    LRU with an adaptive replacement cache algorithm",
    10.1109/mc.2004.1297303, not registered); the USENIX conference page
    gives the title, the authors (Nimrod Megiddo and Dharmendra S. Modha,
    IBM Almaden Research Center) and the date 2003-03-31, the first day of
    FAST '03 (USENIX technical programme, "March 31, 2003").
tags:
- databases
- software-engineering
date: '2026-11-26'
published: '2003-03-31'
url: 'https://www.usenix.org/conference/fast-03/arc-self-tuning-low-overhead-replacement-cache'
first_author: 'Megiddo'
keywords: ['cache replacement', 'adaptive replacement cache', 'recency', 'frequency', 'ghost lists']
implementations: []
summary: >-
  Megiddo and Modha (2003), FAST '03. Registered for A29 §6 of the exchange
  "Alignment consequences brainstorm", which says ARC "balances frequency
  and recency, adapting to the access workload", resists pollution from
  one-time scans, and keeps "lightweight histories of recently evicted
  cache keys" whose hits tell it that eviction was too aggressive. A reads
  the ghost list as a model for a cooled entry's stub ([CLAIM-tmpdkwbk](../claims.d/CLAIM-tmpdkwbk.md),
  [TERM-tmp96b3g](../terms.d/TERM-tmp96b3g.md)). What A says of the work is unverified until read.
---
<!-- inactive-ok-file: CLAIM-tmpdkwbk TERM-tmp96b3g — Proposed; filed from the same exchange on 2026-11-26 -->

# LIT-tmpua7jt: ARC: A Self-Tuning, Low Overhead Replacement Cache

Megiddo and Modha (2003), Proceedings of the 2nd USENIX Conference on File
and Storage Technologies (FAST '03).

## Key takeaways

- Not read.

## Standing in the record

The source of the ghost-list mechanism that A29 §6 borrows for cooled
entries: a cheap record of what was evicted, so that later demand for it
can be detected and the eviction policy corrected. A reading would say what
ARC's ghost lists keep, and whether the self-tuning it gives depends on a
workload the record's retrieval would not have.
