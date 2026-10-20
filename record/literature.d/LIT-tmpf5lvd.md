---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmp6kiiy](../notes.d/NOTE-tmp6kiiy.md)) in full, from Wiskott's own PostScript
  preprint; worth reading for the slowness objective stated exactly
  (minimize ⟨ẏ²⟩ under zero mean, unit variance and decorrelation), for its
  closed-form solution within a fixed nonlinear expansion by sphering and
  an eigendecomposition of the derivative covariance ([THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md)), and
  for the demonstration that stacked modules learn translation, size,
  rotation, contrast and, less well, illumination invariance for 1-D
  patterns from the training stimulus alone. Read it knowing that
  optimality holds per module, on the training signal and within the
  chosen function space, and not for the greedy hierarchy; that "slower is
  more abstract" is its premise, not a finding, so a stack built this way
  is slower at higher stages by construction; that the slowest outputs
  include location, so slowness is not invariance; that no generative model
  and no learning dynamics appear; and that every stimulus is synthetic and
  one-dimensional.
title: 'Slow Feature Analysis: Unsupervised Learning of Invariances'
version: 3
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
- version: 3
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmp6kiiy) from the PostScript at the `url:`,
    converted with Ghostscript and extracted with pdftotext. The typeset
    article was not compared. Status Deferred → Active. THEORY-tmp45pcv
    filed. The summary is corrected: the slowest outputs of the visual
    model include location, not only invariants, and the closed form,
    the hierarchy and its limits are now stated. The body's "Not read"
    paragraph is replaced.
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
  Wiskott & Sejnowski (2002). Learns instantaneous functions of the input whose outputs vary as slowly as possible, minimizing ⟨ẏ²⟩ under zero-mean, unit-variance and decorrelation constraints, solved in closed form within a fixed (usually quadratic) expansion by sphering and taking the smallest eigenvectors of the derivative covariance. Stacked modules in a 1-D model of the visual hierarchy learn translation, size, rotation, contrast and, less well, illumination invariance from the training stimulus, with location ("where") among the slowest outputs alongside identity ("what").
---

# LIT-tmpf5lvd: Slow Feature Analysis: Unsupervised Learning of Invariances

Wiskott, L. & Sejnowski, T. J. (2002). Slow Feature Analysis: Unsupervised Learning of Invariances. *Neural Computation* 14(4): 715–770. doi:10.1162/089976602317318938.

Read in full in [NOTE-tmp6kiiy](../notes.d/NOTE-tmp6kiiy.md). The closed form is re-derived in
[THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md).

## Why this is here

A2 recommended it as a route from temporal regularity to learned features, distinct from explicit relevance targets: under which generative assumptions are slow features also coarse, predictively sufficient or quickly learned? Bears on [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md). [LIT-252](LIT-252.md) and [NOTE-824](../notes.d/NOTE-824.md) treat slow feature analysis as the graph-Laplacian case of spectral inference networks. Flagged `anthology-candidate` because it is a representation-learning method; it carries no instruction for practice.
