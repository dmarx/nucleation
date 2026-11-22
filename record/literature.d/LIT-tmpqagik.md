---
status: Active
status_note: >-
  Read in full on 2026-11-22 for LEAD-tmp3xevc (NOTE-tmpbrc1z) from arXiv
  1908.05839v2 (14 November 2020), the authors' preprint of the ACM
  Computing Surveys article. Worth reading as the standard account of
  bidirectional typing: checking a term against a type given as input,
  synthesizing a type from the term as output, the Pfenning recipe that
  assigns the two rule by rule, and mode-correctness. It treats
  elaboration and coercion only by citation.
title: 'Bidirectional Typing'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed, not read, for LEAD-tmp3xevc, which names "Dunfield and
    Krishnaswami (2021), a survey of bidirectional typing". Checked first:
    no LIT on staging held arXiv 1908.05839, DOI 10.1145/3450952, the
    title or the first author (grep of record/literature.d, 2026-11-22;
    the one hit for "Dunfield", in NOTE-407, is a different Dunfield).
    Identifiers from the arXiv API, Crossref and OpenAlex, no email
    address sent: Jana Dunfield and Neel Krishnaswami, "Bidirectional
    Typing", ACM Computing Surveys 54(5), pp. 1–38, online 2021-05-25,
    print 2022-06-30; arXiv v1 2019-08-16, v2 2020-11-14. The article
    number 98 is the brief's and the usual citation's; Crossref and
    OpenAlex give pages and no article number. `published:` is the arXiv
    v1 date, the earliest exact date the sources give (ADR-002).
- version: 2
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 (NOTE-tmpbrc1z) from the arXiv v2 PDF (37 pages,
    extracted with pdftotext -layout), lawful under ADR-074: the authors'
    own arXiv deposit. Every section and the notation table read; the
    reference list scanned. The published ACM text was not compared, so
    the quotations are the preprint's. Account THEORY-tmptsz1u. Status set
    Active from the reading; summary rewritten from it.
tags:
- logic
date: '2026-11-22'
published: '2019-08-16'
arxiv: '1908.05839'
doi: '10.1145/3450952'
first_author: 'Dunfield'
keywords:
- 'bidirectional typing'
- 'type checking'
- 'type synthesis'
- 'mode-correctness'
- 'subsumption'
implementations: []
summary: >-
  Dunfield and Krishnaswami, ACM Computing Surveys 54(5), 2021 (arXiv
  1908.05839, 2019). A survey of bidirectional type systems, which split
  typing into checking a term against a known type and synthesizing a
  type from a term. It reads the split as modes in the logic-programming
  sense, which parts of a judgment are inputs and which outputs; gives
  four criteria for a system (mode-correctness, completeness or
  annotatability, size, annotation character); restates the Pfenning
  recipe (introduction rules check, elimination rules synthesize, a
  subsumption rule changes direction from synthesis to checking, an
  annotation rule the other way); and surveys polymorphism, mixed and
  backwards modes, the proof-theoretic links (subformula property,
  verifications and uses, focusing) and the history. Read for
  LEAD-tmp3xevc in NOTE-tmpbrc1z; account THEORY-tmptsz1u. It bears on CLAIM-tmpnookt,
  CLAIM-tmpmk056 and TERM-tmp8b1yl.
---

# LIT-tmpqagik: Bidirectional Typing

Jana Dunfield and Neel Krishnaswami (2021). "Bidirectional Typing." *ACM
Computing Surveys* 54(5), pp. 1–38. arXiv 1908.05839 (2019; v2 2020).

## Key takeaways

- **Two modes.** Checking takes context, term and type as inputs;
  synthesis outputs the type. The authors read this as a mode in the
  logic-programming sense: "The status of each meta-variable—input or
  output—is its mode" (§1).
- **The recipe.** Introduction rules check, elimination rules synthesize;
  subsumption switches from synthesis to checking, annotation from
  checking to synthesis (§4). Annotations are then needed exactly where
  an introduction form meets an elimination form (§4.5.4).
- **Mode-correctness.** Every input known before it is used, so that no
  type is guessed (§3.1); a property of a strategy for applying a rule,
  not of the rule's meaning.
- **Information flow, not polarity.** The modes can be mixed, combined or
  reversed (§6); "the essence of bidirectional typing is the management
  of information flow" (§8.4).

## Standing in the record

Registered and read on 2026-11-22 for LEAD-tmp3xevc, which tests
CLAIM-tmpnookt's correspondences against their sources. Read in NOTE-tmpbrc1z;
its account is THEORY-tmptsz1u. The reading supports the claim's fact and
requirement reading of synthesis and checking, shows that neither mode
moves the term, and leaves open whether elaboration is the performative
half (see ARG-tmpcpo8g and CLAIM-tmpugw2q).
