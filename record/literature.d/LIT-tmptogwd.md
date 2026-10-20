---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpuwro4](../notes.d/NOTE-tmpuwro4.md)) in full; worth reading for
  [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md) and [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md) as the multilevel case of an
  operator-induced coarse-to-fine hierarchy. The levels V_j are spanned by
  the eigenvectors of a self-adjoint diffusion T with λ^t ≥ ε at dyadic t.
  They are exactly nested, the wavelet spaces W_j are spectral bands of
  about one octave, and a localized orthonormal basis of each level is
  built without computing eigenvectors. Read it knowing that the levels
  are spectral bands and not spatial blocks (the dyadic cubes only shape
  the basis); that nesting needs no spectral decay, which buys only
  compression; that the compressed algorithm as written thresholds
  T^{2^{j−1}}, not T^{2^j−1} as §5.4 and Fig. 1 say, and the paper's own
  Fig. 9 follows the former ([THEORY-tmpm2oxc](../theory.d/THEORY-tmpm2oxc.md)); that the indexing of V_j
  is inconsistent between (4.8), §4.6 and Theorem 27; that only the
  uncompressed route (Theorems 27 and 29) has proofs, while the
  compressed scheme's error, localization and O(n log² n) cost are
  argued or observed; and that the non-self-adjoint extension is
  asserted, not carried out.
title: 'Diffusion wavelets'
version: 3
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
- version: 3
  date: '2026-10-20'
  note: >-
    Read in full in NOTE-tmpuwro4 from the `url:` copy, the published
    version: §§1–12 with the proofs of Proposition 22, Corollary 23,
    Lemma 26 and Theorems 27 and 29, the algorithmic and complexity
    sections and the examples summarized more briefly, and garbled
    displays checked against page renders. Deferred to Active. The summary
    is corrected from the reading. The earlier one said the scales are set
    by the spectrum "rather than by an imposed spatial partition", which is
    right for the levels. But the proved localization (Theorem 27) does use
    a dyadic-cube partition of the space, to shape each level's basis.
    Tags gain the anthology-candidate flag (ADR-005), for the reason the
    companion diffusion-maps paper (LIT-tmpc7k0w) carries it: a
    multiscale representation for graphs and point clouds that an
    anthology topic could hold. It carries no instruction for ML practice.
    THEORY-tmpm2oxc (Active) is filed from the reading.
tags:
- mathematics
- anthology-candidate
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
  Coifman & Maggioni (2006). A self-adjoint diffusion operator T defines a
  multiresolution analysis by thresholding its dyadic powers at a precision
  ε: V_j is spanned by the eigenvectors with λ^t ≥ ε, so the levels are
  exactly nested spectral bands set by the operator, not by a partition.
  The contribution is an algorithm that squares T on each compressed
  orthonormal basis to build localized scaling functions and wavelets for
  approximations of these spaces, and compressed dyadic powers that apply
  the Green's function fast. Proofs cover the uncompressed construction;
  the compressed scheme's error and cost are argued, not proved.
---

# LIT-tmptogwd: Diffusion wavelets

Coifman, R. R. & Maggioni, M. (2006). Diffusion wavelets. *Applied and Computational Harmonic Analysis* 21(1): 53–94. doi:10.1016/j.acha.2006.04.004.

Read in full in [NOTE-tmpuwro4](../notes.d/NOTE-tmpuwro4.md) (2026-10-20).

## Why this is here

A2 recommended it at high priority: a hierarchy of scales induced by an operator's persistent modes, to compare with the hierarchy learning or prediction favours. Bears on [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md). [NOTE-675](../notes.d/NOTE-675.md) already cites it without a LIT.
