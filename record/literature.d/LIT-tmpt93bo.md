---
status: Deferred
status_note: >-
  Registered 2026-11-26 from A29 §18 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), which names the LETHE tool. Not sought
  or read; the CEUR-WS copy is open
  (https://ceur-ws.org/Vol-1387/paper_9.pdf; its first page was opened only
  to confirm title and authors).
title: 'Lethe: Saturation-Based Reasoning for Non-Standard Reasoning Tasks'
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed, not read. Held check before filing: record/literature.d searched
    for LETHE, Koopmann and "uniform interpolation"; not held. Identifier
    check: Crossref has no record. A names the tool and links its page at
    TU Dresden, which answered 404 on 2026-11-26. The paper describing the
    tool is registered instead: Patrick Koopmann and Renate A. Schmidt, in
    the informal proceedings of the 4th OWL Reasoner Evaluation Workshop
    (ORE 2015), CEUR-WS Vol-1387, pp. 23-30, workshop held at Athens on
    2015-06-06 (the volume's front page). `published:` is the workshop
    date, the earliest exact date the sources give.
tags:
- logic
- databases
date: '2026-11-26'
published: '2015-06-06'
url: 'https://ceur-ws.org/Vol-1387/paper_9.pdf'
first_author: 'Koopmann'
keywords: ['uniform interpolation', 'forgetting', 'description logics', 'TBox abduction', 'logical difference']
implementations: ['LETHE']
summary: >-
  Koopmann and Schmidt (2015), ORE 2015, CEUR-WS 1387. Registered for A29
  §18 of the exchange "Alignment consequences brainstorm", which lists
  LETHE for "formal forgetting and uniform interpolation in supported
  description logics", the logical sense of forgetting A29 §10 sets against
  consolidation: a smaller knowledge base over a reduced vocabulary with
  the same consequences in that vocabulary. The paper's first page says
  the tool serves uniform interpolation, forgetting, TBox abduction and
  logical difference; the rest is unverified until read. It bears on
  [CLAIM-tmpnf6q4](../claims.d/CLAIM-tmpnf6q4.md), which shows why entailment-preserving forgetting can
  fail a correction.
---
<!-- inactive-ok-file: CLAIM-tmpnf6q4 — Proposed; filed from the same exchange on 2026-11-26 -->

# LIT-tmpt93bo: Lethe: Saturation-Based Reasoning for Non-Standard Reasoning Tasks

Koopmann and Schmidt (2015), Informal Proceedings of the 4th International
Workshop on OWL Reasoner Evaluation (ORE 2015), CEUR-WS Vol-1387, pp. 23-30.

## Key takeaways

- Not read.

## Standing in the record

The working implementation of forgetting in the logical sense: given a
vocabulary to keep, compute a knowledge base over it with exactly the old
one's consequences in that vocabulary. [CLAIM-tmpnf6q4](../claims.d/CLAIM-tmpnf6q4.md) shows that such a
projection can merge two records that a later retraction would tell apart,
so a reading would say whether LETHE keeps anything, such as the
eliminated symbols' role in derivations, that a correction could use.
