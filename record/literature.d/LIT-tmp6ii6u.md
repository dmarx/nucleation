---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpdmtd9](../notes.d/NOTE-tmpdmtd9.md)) in full, from the Distill article; worth
  reading as the only place the Circuits thread gives a denominator: it
  sorts every one of the 1,056 units of InceptionV1's first five layers
  into 77 named groups, with each group's share of its layer
  ([THEORY-tmpjdph0](../theory.d/THEORY-tmpjdph0.md)). Read it knowing that the groups are, in the authors'
  words, "ad-hoc, human defined", that 391 of the 1,056 units (37%) sit in
  groups the authors' own captions call catch-all, broad and not well
  defined, low-confidence, unstudied or not understood, and that being
  sorted into a group is not the same as being understood in Zoom In's
  sense. The authors' wider claim, that neuron families are real and recur
  across models, is [THEORY-tmpehpcu](../theory.d/THEORY-tmpehpcu.md).
title: 'An Overview of Early Vision in InceptionV1'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"), one of the works the circuits readings merged in
    dmarx/nucleation#338 named and did not register (the curation entry
    of 2026-10-27 02:06, "Named by the readings, not registered"): NOTE-1198
    and THEORY-1013's dated note name it as the likeliest source of the
    per-layer count THEORY-1013's promote_when asks for. Checked on
    2026-10-27 against the article's own page: Chris Olah, Nick Cammarata,
    Ludwig Schubert, Gabriel Goh, Michael Petrov and Shan Carter (OpenAI),
    Distill, "Published April 1, 2020" (citation_publication_date
    2020/04/01), DOI 10.23915/distill.00024.002, which gives `published:`
    (ADR-002). The DOI given in the request is the one the page prints,
    but on 2026-10-27 it did not resolve: doi.org and its handle API
    returned 404, and Crossref has no record of it, while the thread's
    other DOIs (.001, .003, .004, .005, .007, .008) resolve to their
    articles. The work has no arXiv record, so the article's URL is the
    source, and the printed DOI is kept in the citation only. The summary
    follows the article's own subtitle and structure.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpdmtd9) from the Distill article,
    https://distill.pub/2020/circuits/early-vision/, fetched 2026-10-27,
    its text extracted from the HTML; the neuron grids were parsed from
    the HTML to count every group's units, and the circuit figures were
    read from their captions and the surrounding text only. Status
    Deferred → Active. Two accounts filed: THEORY-tmpjdph0 (Active, the
    taxonomy's counts, re-derived) and THEORY-tmpehpcu (Proposed, the
    authors' claim that the families are real and recur). The summary is
    checked against the reading and given the counts.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-27'
published: '2020-04-01'
url: 'https://distill.pub/2020/circuits/early-vision/'
first_author: 'Olah'
keywords:
- 'early vision'
- 'neuron groups'
- 'neuron families'
- 'taxonomy'
- 'feature visualization'
- 'InceptionV1'
- 'circuits'
implementations: []
summary: >-
  Olah et al. (2020), Distill (printed DOI 10.23915/distill.00024.002,
  unregistered on 2026-10-27). A guided
  tour of InceptionV1's first five layers (conv2d0, conv2d1, conv2d2,
  mixed3a, mixed3b; 1,056 units), every unit sorted into one of 77
  "neuron groups" with its share of the layer, and selected circuits
  (complex Gabors, a black-and-white detector, small circles, triangles,
  boundary, curve-based and oriented-fur detectors). The authors call the
  groups ad hoc and many of them low-confidence; by their own captions 37%
  of the units are in catch-all, broad, low-confidence or unstudied
  groups. The curve family is 10 of mixed3b's 480 units.
---
<!-- inactive-ok-file: THEORY-tmpehpcu THEORY-1013 — Proposed; the authors' wider claim filed from this reading and the circuits account it bears on, cited as open -->

# LIT-tmp6ii6u: An Overview of Early Vision in InceptionV1

Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M. and Carter, S.
(2020). An overview of early vision in InceptionV1. *Distill*, 1 April
2020. https://distill.pub/2020/circuits/early-vision/ (the page prints
doi:10.23915/distill.00024.002, which did not resolve on 2026-10-27).

Read in full on 2026-10-27 ([NOTE-tmpdmtd9](../notes.d/NOTE-tmpdmtd9.md)). Two accounts were drawn from
it: [THEORY-tmpjdph0](../theory.d/THEORY-tmpjdph0.md) (Active) and [THEORY-tmpehpcu](../theory.d/THEORY-tmpehpcu.md) (Proposed).

## Why this is here

Registered and read at the owner's request of 2026-10-27 ("file the next
readings"), as one of the works the circuits readings named and did not
register. [THEORY-1013](../theory.d/THEORY-1013.md), Zoom In's claim that units of a trained vision
network are typically meaningful features, is Proposed because its
evidence is chosen examples with no denominator; its promote_when asks
for "the fraction of units that meet" a stated criterion over whole
layers. Curve Detectors ([LIT-1575](LIT-1575.md), [NOTE-1198](../notes.d/NOTE-1198.md)) gave one family, ten of
mixed3b's 480 units. This article is the thread's only census: it puts
every unit of five layers somewhere. The record's circuits line held the
programme statement and two single-family articles, and nothing that said
how much of a layer the families cover. Read against [THEORY-1013](../theory.d/THEORY-1013.md), it
supplies a denominator but not the criterion: being sorted into a group
is not being understood, and the authors say most groups were given "a
few minutes of cursory investigation".
