---
status: Active
status_note: >-
  read 2026-10-27 (NOTE-tmpt77xq) in full, from the arXiv copy (v2, the
  ICLR 2023 version); worth reading as ROME's extension from one edit to
  thousands, by a closed-form least-squares update spread over the range
  of MLP layers that causal tracing implicates, and for the scaling
  curves that show sequential single edits failing where it holds
  (THEORY-tmpukwxl). Read it knowing that it inherits ROME's storage
  reading (THEORY-1011) rather than testing it, that its layer range is
  chosen from traces averaged over facts, which Hase et al.
  (LIT-tmpg22tp) show do not predict per fact where an edit works, and
  that its zsRE specificity hardly moves for any method.
title: 'Mass-Editing Memory in a Transformer'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started
    on the seven works and markov IBP"): one of the works the circuits
    readings named without registering (curation entry of 2026-10-27,
    "Named by the readings, not registered"), ROME's extension to many
    edits (NOTE-1166). Checked as not held: a search of literature.d and
    notes.d for the identifier, the title and "MEMIT" found only passing
    mentions (NOTE-1166, NOTE-755). Checked on 2026-10-27 against the
    arXiv record: Kevin Meng, Arnab Sen Sharma, Alex Andonian, Yonatan
    Belinkov and David Bau, arXiv 2210.07229, v1 submitted 13 October
    2022, which is `published:` (ADR-002); v2 of 1 August 2023 is headed
    "Published as a conference paper at ICLR 2023". The summary follows
    the arXiv abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpt77xq) from the arXiv PDF of 2210.07229v2,
    fetched 2026-10-27. v1 was not compared. Status Deferred → Active.
    One account filed: THEORY-tmpukwxl (Active). It `extends` ROME
    (LIT-1536). The summary is checked against the reading and given the
    measured results.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-27'
published: '2022-10-13'
arxiv: '2210.07229'
first_author: 'Meng'
keywords:
- 'MEMIT'
- 'model editing'
- 'mass editing'
- 'linear associative memory'
- 'causal tracing'
- 'CounterFact'
- 'zsRE'
implementations: []
extends:
- LIT-1536
summary: >-
  Meng et al. (2022), arXiv:2210.07229, ICLR 2023. MEMIT inserts many
  facts at once by treating each MLP output matrix in a range of layers
  implicated by causal tracing as a linear associative memory, solving a
  least-squares update for the whole batch, and spreading each fact's
  required change over those layers. On GPT-J it inserts 10,000
  CounterFact counterfactuals with score 85.8, against 50.3 for ROME
  applied one fact at a time, and does likewise on GPT-NeoX (82.0) and for
  10,000 true zsRE facts.
---
<!-- inactive-ok-file: THEORY-1011 — Proposed; the storage hypothesis this method inherits, cited as open -->

# LIT-tmpsrubd: Mass-Editing Memory in a Transformer

Meng, K., Sen Sharma, A., Andonian, A., Belinkov, Y. and Bau, D. (2022).
Mass-editing memory in a transformer. *ICLR 2023*. arXiv:2210.07229.

Read in full on 2026-10-27 (NOTE-tmpt77xq). One account was drawn from
it: THEORY-tmpukwxl.

## Why this is here

Registered and read at the owner's request of 2026-10-27, to fill a gap
the circuits readings of 2026-10-26 named: ROME's extension to many
edits, which the reading of ROME (NOTE-1166) cited without the record
holding it. It is the method Hase et al. (LIT-tmpg22tp) test alongside
ROME, and its choice of a range of layers rather than one is the clearest
case of a localization used to design an edit. The record's question is
what that design shows about where facts are (THEORY-1011), not how to
edit models, which is practice and the anthology's.
