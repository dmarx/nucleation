---
status: Deferred
status_note: 'filed 2026-10-13 from its Crossref record, not read. Registered at the owner''s request from the survey of the Mathematics of Meaning corpus, for [CLAIM-098](../claims.d/CLAIM-098.md), [CLAIM-011](../claims.d/CLAIM-011.md) and [QUESTION-005](../questions.d/QUESTION-005.md). No NOTE is filed, and it stays Deferred until it is read, not on merit. Looked for on 2026-10-13, none found: OpenAlex reports it closed, with no open-access or repository location; Semantic Scholar has no record of the DOI; Crossref gives only Cambridge Core''s terms licence; Cambridge Core sells the chapters behind ''Get access''; a web search found no author-posted chapter or draft, and no personal page for Jerry (Jeremy) Seligman listing one; the PhilArchive record (BARIFT) could not be opened from here (bot challenge). Seligman''s later chapter on channels in Sommaruga (ed.), Formal Theories of Information (Springer 2009; Auckland ResearchSpace 2292/13632) is a separate work, not a chapter of this book, and was not read.'
title: 'Information Flow: The Logic of Distributed Systems'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-13
    (doi:10.1017/CBO9780511895968): Jon Barwise and Jerry Seligman,
    Information Flow, Cambridge University Press, issued 28 July 1997, which
    is the `published:` date; online 5 November 2011; ISBNs 9780521583862,
    9780521070997 and 9780511895968. The subtitle is the book's as standardly
    cited; Crossref's record carries the main title only. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-13, commit
    d1573d2) for Barwise and Seligman found nothing (the phrase "information
    flow" appears there only in other works' titles), and no anthology topic
    holds channel theory, so ADR-013 does not apply. Mathematics of Meaning
    names it in MOM-LIT-006, a survey entry noting its corpus listed the book
    and never used it.
tags:
- logic
- information-theory
date: '2026-10-13'
published: '1997-07-28'
doi: '10.1017/CBO9780511895968'
first_author: 'Barwise'
keywords:
- 'information flow'
- 'classification'
- 'infomorphism'
- 'channel theory'
- 'local logic'
- 'distributed systems'
implementations: []
summary: >-
  Barwise & Seligman (1997), Cambridge University Press. Channel theory: a
  classification is a set of tokens, a set of types and a relation saying
  which token is of which type; infomorphisms are maps between
  classifications, channels are families of infomorphisms into a core, and
  information flows along a channel by the regularities of its core, captured
  by local logics. Not read.
---
<!-- inactive-ok-file: CLAIM-098 — Proposed; open, cited as the claim a reading should test -->

# LIT-tmpd0loo: Information Flow: The Logic of Distributed Systems

Jon Barwise and Jerry Seligman (1997), *Cambridge University Press* — DOI-10.1017/CBO9780511895968

## Key takeaways

*Filed, not read.* Known here by what it is standardly cited for.

- **Classifications.** Tokens, types and a classifying relation: the two-sided
  structure of an entity-by-predicate table.
- **Infomorphisms** between two classifications are a pair of maps, one on
  types forward and one on tokens backward, that respect classification.
  Classifications and infomorphisms form a category.
- **Channels** connect several classifications through a core, and information
  flows from one part of a distributed system to another by the regularities
  that hold in the core. Local logics say which regularities hold, and on
  which tokens.

## Standing in the record

Filed for the pragmatic-transport line, as a ready theory of what it means to
carry structure from one system of distinctions to another. Three points of
contact a reading should test:

- [CLAIM-098](../claims.d/CLAIM-098.md) holds that translations form a category or semigroup of directed
  transformations, not a group. Classifications with infomorphisms are such a
  category, with arrows that need not be invertible.
- [CLAIM-011](../claims.d/CLAIM-011.md) requires the source–target correspondence to be anchored to
  independently measured distinctions. A channel's core is a worked account of
  a correspondence as an object of its own, through which two classifications
  become comparable.
- [QUESTION-005](../questions.d/QUESTION-005.md) asks how to set up the correspondence of communicative
  environments without building the preferred notion of fidelity into it.
  Channel theory makes the correspondence an object of its own, which is the
  separation the question wants, though it does not say how to measure one.
