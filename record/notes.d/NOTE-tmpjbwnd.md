---
status: Skimmed
paper: LIT-tmp1c0df
title: 'Bencomo, Götz and Song — Models@run.time: a guided tour of the state of the art and research challenges'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from
    https://publications.aston.ac.uk/id/eprint/37117/1/mrt_survey.pdf.
    Skimmed: §1, §3 (taxonomy) and §7–§8 (challenges, conclusions) read;
    §2 method, §4–§6 (cross-dimensional analysis, Kiviat graphs) skipped. A
    delegated reader drafted the reading; quotations were rechecked by script
    against the downloaded copy, and any that did not match were kept as
    paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  A systematic literature review of 271 papers on models@run.time, mainly
  since 2006, plus 5 predecessor papers. It defines a runtime model, citing
  the 2009 Blair et al. article as [40], and grounds the idea in Maes's
  computational reflection. It builds a taxonomy: applied against
  fundamental research; for applied work, level of abstraction, model type,
  purpose and MDE technique; then domain, intersecting areas and
  initiatives.
---
<!-- inactive-ok-file: CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: LIT-2305 — Unavailable; cited for what each holds, not as settled -->

# NOTE-tmpjbwnd: Bencomo, Götz and Song — Models@run.time: a guided tour of the state of the art and research challenges

## Key results

- Definition (§1, across a page break): a runtime model is defined as a causally connected self-representation of the associated system that emphasizes the structure, behaviour, or goals of the system and which can be manipulated at runtime for specific purposes [40].
- Causal connection, via Maes (§1): "every change in the runtime model leads to a change in the reflected system and vice versa."
- Concentration (§8): most applied research "(a) focused on the architectural level of abstraction, (b) used structural runtime models, (c) used the runtime models for self-adaptive software and (d) used model transformations."
- Purposes (§3.2.3): self-adaptation (124 papers), assurance (42), development (35), evolution (18). Metamodels as runtime models are rare (3 papers).
- Open problem (§7.5, transaction-safe causal connections): "When are system and model allowed to be out of sync? What happens when a decision is made based on outdated information in the model?"
- Distributed runtime models are rare (§7.5): "we only found 8 papers investigating distributed models@run.time".

## Assumptions

It is an SLR whose inclusion criteria the reader did not read (§2). The counts depend on its classification. The reader read the author manuscript, not the published version.

## Bearing on the record

The exchange (§12) treats models@run.time as "a closer technical comparison than generic agent memory" for luria. The survey bears that out: the field treats a runtime model as a reflection layer for adaptation. It also bears out A's caveat. The defining property, causal connection, is one a governed record does not have toward its agents.

It restates the 2009 article's **definition** (cited as [40]) and the programme the article launched. It does **not** restate the 2009 article's arguments, examples or claims beyond the definition.

- **QUESTION-tmps5iou**: **qualifies** the comparison class, as in LIT-2305's report. Models@run.time couples a model to a system causally. It does not, in this survey's taxonomy, couple model change to recorded decision or authority. Governance appears nowhere among the taxonomy's dimensions (purposes, techniques). That is a point for the question's distinctiveness half, from a survey's coverage, not from a test.
- **CLAIM-tmp8qsef**: the transaction-safe causal-connection challenge, in which decisions are made on an outdated model, is the runtime-systems version of stale dependants in a record. A point of contact only.
