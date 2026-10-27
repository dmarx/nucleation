---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmphb6el](../notes.d/NOTE-tmphb6el.md)) in full, from the Distill article; worth
  reading as the second part of Curve Detectors ([LIT-1575](LIT-1575.md)) and the one that
  supplies the three arguments that article deferred: the circuit that
  builds the ten mixed3b curve units from earlier families, a downstream
  use in mixed4a, and a hand-written "artificial artificial neural
  network" whose curve units approximate the natural ones
  ([THEORY-tmp90225](../theory.d/THEORY-tmp90225.md)). Read it knowing that every comparison but one is
  qualitative (figures), that the one number, the accuracy recovered by
  substituting the hand-written units, is on 2,000 validation images and
  called preliminary by the authors, that the hand-written units are
  grayscale, and that the claim that the circuit is "a simple algorithm"
  is the authors' ([THEORY-tmpxjvwo](../theory.d/THEORY-tmpxjvwo.md)).
title: 'Curve Circuits'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"), one of the works the circuits readings merged in
    dmarx/nucleation#338 named and did not register (the curation entry
    of 2026-10-27 02:06, "Named by the readings, not registered"): Curve
    Detectors (LIT-1575, NOTE-1198) defers to it the circuit, downstream
    and reimplementation arguments that Zoom In counts for curve
    detectors, and THEORY-1013's dated note names it. Checked on
    2026-10-27 against the article's own page: Nick Cammarata, Gabriel
    Goh, Shan Carter, Chelsea Voss, Ludwig Schubert and Chris Olah
    (OpenAI; Carter at Observable), Distill, "Published Jan. 30, 2021"
    (citation_publication_date 2021/01/30), which gives `published:`
    (ADR-002). The page prints DOI 10.23915/distill.00024.006, the suffix
    the curation entry had not checked; on 2026-10-27 it did not resolve
    (doi.org and its handle API returned 404, and Crossref has no record),
    while Curve Detectors' .003 resolves. The work has no arXiv record, so
    the article's URL is the source, and the printed DOI is kept in the
    citation only.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmphb6el) from the Distill article,
    https://distill.pub/2020/circuits/curve-circuits/, fetched 2026-10-27.
    The page's HTML holds only the front matter; the article is compiled
    into its index.js, whose text was extracted by a static parse of the
    bundle's element calls, without running it. The figures are
    interactive and were not rendered; their content was taken from
    their captions and the text. Status Deferred → Active. Two accounts
    filed: THEORY-tmp90225 (Active, what the article measured) and
    THEORY-tmpxjvwo (Proposed, the authors' claim that the algorithm is
    simple and their reimplementation shows the circuit is understood).
tags:
- representation-learning
- anthology-candidate
date: '2026-10-27'
published: '2021-01-30'
url: 'https://distill.pub/2020/circuits/curve-circuits/'
first_author: 'Cammarata'
keywords:
- 'curve circuits'
- 'curve detectors'
- 'equivariance'
- 'decomposed feature visualization'
- 'artificial artificial neural network'
- 'circuit editing'
- 'InceptionV1'
- 'circuits'
extends:
- LIT-1575
implementations: []
summary: >-
  Cammarata et al. (2021), Distill (printed DOI 10.23915/distill.00024.006,
  unregistered on 2026-10-27). The second of the curve-detector articles,
  on how the ten curve units of InceptionV1's mixed3b are built: from
  conv2d0 Gabors through conv2d2 and mixed3a lines and early curves, each
  family tiled along the curve's tangent, with rotational and scale
  equivariance said to cut the circuit's 50,000-plus parameters about
  50-fold. Negative weights from opposite early curves remove the 180°
  echo, and deleting them by circuit editing brings it back. A hand-set
  network written from the description approximates the curve units on
  synthetic curves, and substituting it for them recovers 26 of the 46
  top-5 classifications lost by removing them, on 2,000 images.
---
<!-- inactive-ok-file: THEORY-tmpxjvwo THEORY-1013 THEORY-1022 — Proposed; the authors' wider claim filed from this reading and the circuits accounts it bears on, cited as open -->

# LIT-tmpl1s2e: Curve Circuits

Cammarata, N., Goh, G., Carter, S., Voss, C., Schubert, L. and Olah, C.
(2021). Curve circuits. *Distill*, 30 January 2021.
https://distill.pub/2020/circuits/curve-circuits/ (the page prints
doi:10.23915/distill.00024.006, which did not resolve on 2026-10-27).

Read in full on 2026-10-27 ([NOTE-tmphb6el](../notes.d/NOTE-tmphb6el.md)). Two accounts were drawn from
it: [THEORY-tmp90225](../theory.d/THEORY-tmp90225.md) (Active) and [THEORY-tmpxjvwo](../theory.d/THEORY-tmpxjvwo.md) (Proposed).

## Why this is here

Registered and read at the owner's request of 2026-10-27 ("file the next
readings"), as one of the works the circuits readings named and did not
register. Zoom In ([LIT-1543](LIT-1543.md)) argues curve detectors seven ways; Curve
Detectors ([LIT-1575](LIT-1575.md)) supplied four of them and deferred the other three,
the implementing circuit, the downstream use and the hand-written
reimplementation, to this article. [THEORY-1013](../theory.d/THEORY-1013.md) and [THEORY-1022](../theory.d/THEORY-1022.md) both name
it as the missing piece. The record's circuits line held the vision
case's behaviour and none of its mechanism. Read against them, it
supplies all three deferred arguments for one family, mostly as figures
and once as a small number, and it gives no count over a layer.
