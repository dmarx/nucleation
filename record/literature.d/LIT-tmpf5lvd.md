---
status: Deferred
status_note: >-
  filed 2026-10-19, not read. Registered from the exchange of 2026-10-19 on
  coarse-to-fine processes, which the owner relayed. No NOTE is filed. A
  lawful open copy was found on 2026-10-20 (the `url:`) and has not been
  read. The copy is gzipped PostScript.
title: 'Slow Feature Analysis: Unsupervised Learning of Invariances'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is Crossref's issue date, 1 April 2002, a full date. No arXiv copy and no open copy was found. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Copy hunt, not a reading. Wiskott's own page at the Institut für
    Neuroinformatik, Bochum (Abstracts/WisSej2002.html) links a gzipped
    PostScript of 49 pages. Its first page says: "The final version of this
    article has been published in Neural Computation, 14(4) (2002) published
    by The MIT Press. This version does not differ significantly from the
    final version." It was fetched and its identity confirmed from the title
    strings in the PostScript; the `url:` is added. No PDF is posted at the
    same address (404). Unpaywall and OpenAlex report the work closed, and
    Europe PMC holds only the PubMed record (11936959) with no full text.
    PDF copies on course pages at Berkeley's Redwood Center and at CMU were
    not used, since neither is posted by the authors. This corrects version
    1, which found no open copy. Status stays Deferred.
tags:
- representation-learning
- neuroscience
- anthology-candidate
date: '2026-10-19'
published: '2002-04-01'
doi: '10.1162/089976602317318938'
url: 'https://www.ini.rub.de/PEOPLE/wiskott/Publications/WisSej2002-LearningInvariances-NC.ps.gz'
first_author: 'Wiskott'
keywords:
- 'slow feature analysis'
- 'invariance learning'
- 'unsupervised learning'
implementations: []
summary: >-
  Wiskott & Sejnowski (2002). Learns input–output functions whose outputs vary as slowly as possible over time, under unit-variance and decorrelation constraints, and shows that the slowest features recover invariances such as translation in a model of the visual hierarchy.
---

# LIT-tmpf5lvd: Slow Feature Analysis: Unsupervised Learning of Invariances

Wiskott, L. & Sejnowski, T. J. (2002). Slow Feature Analysis: Unsupervised Learning of Invariances. *Neural Computation* 14(4): 715–770. doi:10.1162/089976602317318938.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A2 recommended it as a route from temporal regularity to learned features, distinct from explicit relevance targets: under which generative assumptions are slow features also coarse, predictively sufficient or quickly learned? Bears on [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md). [LIT-252](LIT-252.md) and [NOTE-824](../notes.d/NOTE-824.md) treat slow feature analysis as the graph-Laplacian case of spectral inference networks. Flagged `anthology-candidate` because it is a representation-learning method; it carries no instruction for practice.
