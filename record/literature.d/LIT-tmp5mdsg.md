---
status: Active
status_note: >-
  Read on 2026-11-12 ([NOTE-tmp2txvh](../notes.d/NOTE-tmp2txvh.md)) from
  https://wwwbroy.in.tum.de/publ/papers/ECOOP2009_herrmannsdoerfer_cope_automating_coupled.pdf.
title: 'COPE - Automating Coupled Evolution of Metamodels and Models'
version: 3
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI or arXiv id, exact title and first author in record/literature.d. `published:`: Crossref gives the year only. No email address was sent to any service.
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 (NOTE-tmp2txvh; THEORY-tmph4vkf). Read from the TUM
    chair's copy. The registration said the paper introduced the
    coupled-evolution approach Edapt grew from; it does neither: it never
    names Edapt, and its §3 surveys earlier coupled transformation of database
    schemas, grammars and metamodels. It introduces COPE, a tool coupling each
    metamodel change to a migration of its models with a replayable history;
    that COPE later became Eclipse Edapt comes from outside the paper. ECOOP
    2009, LNCS 5653, pp. 52–76; authors Markus Herrmannsdoerfer, Sebastian
    Benz and Elmar Juergens.
- version: 3
  date: '2026-11-12'
  note: >-
    software-engineering added after the existing tags, by ADR-tmppzz2h,
    once it joined the topics: coupled metamodel evolution is in that
    word's blurb. Primary topic unchanged; nothing removed.
tags:
- databases
- design-rationale
- software-engineering
date: '2026-11-12'
published: '2009-01-01'
doi: '10.1007/978-3-642-03013-0_4'
first_author: 'Herrmannsdoerfer'
keywords: []
implementations: []
summary: >-
  Herrmannsdoerfer, Benz and Juergens (2009), COPE - Automating Coupled
  Evolution of Metamodels and Models. When a modeling language's metamodel
  changes, the existing models must be migrated. The paper calls this
  pairing "coupled evolution". **The requirements study.** An earlier study
  of two industrial metamodel histories found: - about half the changes were
  metamodel-only; - more than three quarters of the coupled changes were
  metamodel-independent, so they could be reused; - the rest were
  metamodel-specific; - none were model-specific. This yields two
  requirements: reuse and expressiveness. **COPE's answer.** A language
  evolves through a sequence of coupled transactions, each pairing a
  metamodel adaptation with its model migration. There are two kinds: -
  **Reusable** transactions, drawn from a library: rename, extract class,
  generalize reference, and so on. - **Custom** transactions, written in a
  Turing-complete language. Read for the exchange "luria experiment design".
---
<!-- inactive-ok-file: ADR-tmppzz2h — Proposed; the decision the history note of 2026-11-12 applies -->
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: THEORY-tmph4vkf — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# LIT-tmp5mdsg: COPE - Automating Coupled Evolution of Metamodels and Models

Markus Herrmannsdoerfer et al. (2009), ECOOP 2009, LNCS. DOI 10.1007/978-3-642-03013-0_4.

## Key takeaways

*Seeded from the exchange; read on 2026-11-12, below.* A cites it for changes to a metamodel paired with migrations of its existing instances; A calls it "the strongest technical competitor". A named the tool, Edapt. The paper introduces COPE, which couples each metamodel change to a migration of existing models with a replayable history; it does not name Edapt, into which COPE later developed according to sources outside the paper, and does not claim to introduce coupled evolution.

## Standing in the record

Registered on 2026-11-12 from the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A22 (as "Edapt / coupled metamodel evolution"). It bears on [QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md) and [CASE-tmppm4do](../cases.d/CASE-tmppm4do.md).

## Reading of 2026-11-12

Read in [NOTE-tmp2txvh](../notes.d/NOTE-tmp2txvh.md), from https://wwwbroy.in.tum.de/publ/papers/ECOOP2009_herrmannsdoerfer_cope_automating_coupled.pdf; its account is [THEORY-tmph4vkf](../theory.d/THEORY-tmph4vkf.md).
