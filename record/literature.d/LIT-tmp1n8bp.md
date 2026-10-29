---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmpr9b03) from the LREC 2026 PDF; worth
  reading as the only multilingual corpus of the additions human
  translators make for a new audience, with each addition marked in the
  target, and for what it lacks: no reported annotator agreement.
title: 'PETra: A Multilingual Corpus of Pragmatic Explicitation in Translation'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2025-11-04, ahead of
    the LREC 2026 proceedings (Crossref, May 2026 only; ELRA DOI
    10.63317/56tberz7nmwy) (ADR-002). The abstract spells the name
    PeTra; the title and the ACL record PETra.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the LREC 2026 PDF (ACL Anthology 2026.lrec-1.689);
    the arXiv v2 text is the same. Corrections: the corpus is 3,000
    pairs in the abstract (Table 2 sums to 2,982; the release has
    2,989), not 2,900, and the twelve pairs are all English to X. The
    summary is rewritten from the text. Status Deferred to Active.
tags:
- translation
- pragmatics
date: '2026-10-29'
published: '2025-11-04'
arxiv: '2511.02721'
first_author: 'Osmelak'
keywords:
- 'pragmatic explicitation'
- 'translation'
- 'multilingual corpus'
- 'active learning'
- 'null alignment'
implementations: []
summary: >-
  Osmelak et al. (2026). A released corpus of about 3,000 English-source
  sentence pairs from TED-Multi and Europarl in twelve target languages,
  in which the translation adds or replaces material to make culture-bound
  knowledge explicit: unit conversions, entity descriptions and
  specifications, translator glosses, typed under a 19-subtype schema and
  marked as added or replacing. Candidates come from null alignments next
  to a named entity; a multilingual BERT classifier trained by active
  learning on German and Spanish found three quarters of the pairs, its
  accuracy rising 7–8 points over the cycles. Measurement conversion is
  the largest category. No inter-annotator agreement is reported.
---

# LIT-tmp1n8bp: PETra: A Multilingual Corpus of Pragmatic Explicitation in Translation

Osmelak, D., Dutta Chowdhury, K., Sentsova, U., España-Bonet, C., & van Genabith, J. (2026). PETra: A multilingual corpus of pragmatic explicitation in translation. *Proceedings of LREC 2026*, 8756–8766.

Read in full in NOTE-tmpr9b03.

## Why this is here

A5 put it first among the readings: a corpus of what translation adds, which is the target side of [CLAIM-257](../claims.d/CLAIM-257.md)'s change of cover, and a source of items for [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md). Its categories annotate additions; they are not a validated measure of footing or act.

The reading bears this out with two qualifications for CASE-tmph0fxi: the labels would need re-annotation to meet its Stage 0, and the corpus gives one direct route per item, from English only. About half its labels mark replacements, not additions (NOTE-tmpr9b03).

## Key takeaways

- The items are additions to background knowledge ("Tucson" → "Tucson (Arizona)"), not changes of act, stance or footing.
- No agreement statistic, a single annotator implied, and most pairs found by a classifier: the labels are not a validated measure (NOTE-tmpr9b03).
- One English → X route per item; no relay can be read off it.
