---
status: Deferred
status_note: >-
  filed 2026-10-19, not read. Registered from the exchange of 2026-10-19 on
  coarse-to-fine processes, which the owner relayed. No NOTE is filed. A
  lawful open copy was found on 2026-10-20 (the `url:`) and has not been
  read.
title: 'Successive refinement of information'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is the first of Crossref's month, March 1991, per ADR-002. An earlier workshop abstract exists (Cover & Equitz, IEEE/CAM Information Theory Workshop 1989, doi:10.1109/ITW.1989.761420). The exchange named the topic, "successive refinement in rate–distortion theory", and no paper; this is the record's identification of its classical source. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Copy hunt, not a reading. Thomas Cover's Stanford page posts the
    published version (IEEE TIT 37(2):269–275, 6 pages) at two addresses,
    papers/paper94.pdf and papers/transIT/0269equi.pdf. Both were fetched
    and confirmed as this paper by the title page and abstract, and the
    first is the `url:`. Unpaywall and OpenAlex report the work closed.
    Status stays Deferred.
tags:
- information-theory
date: '2026-10-19'
published: '1991-03-01'
doi: '10.1109/18.75242'
url: 'https://isl.stanford.edu/~cover/papers/paper94.pdf'
first_author: 'Equitz'
keywords:
- 'successive refinement'
- 'rate–distortion'
- 'Markov chain condition'
- 'progressive coding'
implementations: []
summary: >-
  Equitz & Cover (1991). A source is successively refinable when describing it at a coarse distortion and then refining loses nothing against describing it optimally at the finer distortion directly; this holds exactly when the optimal descriptions can be written as a Markov chain from the finer to the coarser, and fails for some sources.
---

# LIT-tmp25otd: Successive refinement of information

Equitz, W. H. R. & Cover, T. M. (1991). Successive refinement of information. *IEEE Transactions on Information Theory* 37(2): 269–275. doi:10.1109/18.75242.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A2's highest-priority bridge: when optimal compressed representations at different budgets nest, rather than reorganize into incompatible solutions. It is the classical answer for rate–distortion, which [QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md) asks to carry to the information bottleneck.
