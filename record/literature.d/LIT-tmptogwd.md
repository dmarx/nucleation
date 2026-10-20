---
status: Deferred
status_note: >-
  filed 2026-10-19, not read. Registered from the exchange of 2026-10-19 on
  coarse-to-fine processes, which the owner relayed. No NOTE is filed. A
  lawful open copy was found on 2026-10-20 (the `url:`) and has not been
  read.
title: 'Diffusion wavelets'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is 11 June 2006, OpenAlex's day, which is probably the ScienceDirect online date; Crossref gives the issue month only (2006-07). The publisher's page refused the lookup, so the day is unconfirmed. No arXiv copy was found. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Copy hunt, not a reading. The journal's back file is in Elsevier's open
    archive: Crossref carries Elsevier's open-access user licence for the
    version of record from 2013-08-22, and Unpaywall and OpenAlex mark the
    article free to read at the publisher. ScienceDirect returned a 403
    bot-check page to this client. The published version (42 pages, pp.
    53–94) was fetched from Naoki Saito's page at UC Davis, which hosts the
    special issue's papers, and confirmed by its first and last pages; the
    `url:` is that copy. Its first page reads "Received 28 October 2004;
    revised 11 April 2006; accepted 12 April 2006; Available online 8 June
    2006". `published:` is corrected from 2006-06-11 to 2006-06-08 under
    ADR-002: the publisher's online date is earlier than every Crossref
    field. The old day was Crossref's `created` (deposit) date, which
    OpenAlex copies and ADR-002 excludes. Crossref reports no
    published-online date, only the issue month, 2006-07. Status stays
    Deferred.
tags:
- mathematics
date: '2026-10-19'
published: '2006-06-08'
doi: '10.1016/j.acha.2006.04.004'
url: 'https://www.math.ucdavis.edu/~saito/data/diffgeomharm/ACHA-Special/diffusionwavelets.pdf'
first_author: 'Coifman'
keywords:
- 'diffusion operators'
- 'multiresolution analysis'
- 'wavelets on graphs and manifolds'
implementations: []
summary: >-
  Coifman & Maggioni (2006). Builds a multiresolution analysis on graphs and manifolds from dyadic powers of a diffusion operator, compressing each power's range, so the scales are set by the operator's spectrum rather than by an imposed spatial partition.
---

# LIT-tmptogwd: Diffusion wavelets

Coifman, R. R. & Maggioni, M. (2006). Diffusion wavelets. *Applied and Computational Harmonic Analysis* 21(1): 53–94. doi:10.1016/j.acha.2006.04.004.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A2 recommended it at high priority: a hierarchy of scales induced by an operator's persistent modes, to compare with the hierarchy learning or prediction favours. Bears on [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md). [NOTE-675](../notes.d/NOTE-675.md) already cites it without a LIT.
