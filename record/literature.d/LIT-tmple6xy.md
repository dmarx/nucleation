---
status: Deferred
status_note: >-
  filed 2026-10-19, not read. Registered from the exchange of 2026-10-19 on
  coarse-to-fine processes, which the owner relayed. No NOTE is filed. A
  lawful open copy was found on 2026-10-20 (the `url:`) and has not been
  read.
title: 'Optimal prediction with memory'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is the first of Crossref's month, June 2002, per ADR-002. No open copy was confirmed; arXiv:math/0101022 ("Non-Markovian Optimal Prediction") is a different paper. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Copy hunt, not a reading. Semantic Scholar's open-access link points to
    the published version (Physica D 166:239–257, 19 pages) posted on
    Chorin's own Berkeley page; it was fetched and confirmed as this paper
    by its first and last pages, and the `url:` is added. Unpaywall and
    OpenAlex report the work closed; OpenAlex also lists a CiteSeerX record,
    not followed. arXiv:math/0101022 is confirmed a different paper:
    "Non-Markovian Optimal Prediction" (2001), whose abstract presents a
    Monte Carlo approximation of the orthogonal dynamics and cites the need
    for memory as "previous work". An arXiv search by title and author found
    no version of this paper. Status stays Deferred.
tags:
- mathematics
- natural-sciences
- probabilistic-modeling
date: '2026-10-19'
published: '2002-06-01'
doi: '10.1016/S0167-2789(02)00446-3'
url: 'https://math.berkeley.edu/~chorin/CHK02.pdf'
first_author: 'Chorin'
keywords:
- 'Mori–Zwanzig'
- 'optimal prediction'
- 'memory kernel'
- 'model reduction'
implementations: []
summary: >-
  Chorin, Hald & Kupferman (2002). Extends optimal prediction to keep the memory term of the Mori–Zwanzig equation, and shows on examples that the memory is needed to predict the resolved variables over longer times.
---
<!-- inactive-ok-file: CLAIM-327 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# LIT-tmple6xy: Optimal prediction with memory

Chorin, A. J., Hald, O. H. & Kupferman, R. (2002). Optimal prediction with memory. *Physica D* 166(3–4): 239–257. doi:10.1016/S0167-2789(02)00446-3.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A5 called it "the most direct foundation for comparing reduced-model prediction, unresolved dynamics, and memory", to be read before any reformulation of dynamical independence. Bears on [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md), [THEORY-257](../theory.d/THEORY-257.md) and [CLAIM-327](../claims.d/CLAIM-327.md).
