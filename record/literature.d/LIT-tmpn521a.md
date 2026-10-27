---
status: Active
status_note: >-
  read in full 2026-10-27 ([NOTE-tmpdshmx](../notes.d/NOTE-tmpdshmx.md)), from arXiv v3; worth reading as
  the source of the consistency radius and of sheaf-based data fusion as
  the nearest global section, with a clear worked example. It is
  expository: "canonical" is argued by positing axioms whose models are
  sheaves, not proved, and the paper calls sheaves one of "many
  co-universal information representations". The demonstration is one
  simulated scenario; its uniqueness result for linear fusion
  (Proposition 25) does not follow from its proof.
title: 'Sheaves are the canonical data structure for sensor integration'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against Crossref and the arXiv API on
    2026-10-27: Michael Robinson, Information Fusion 36, 208–224, July
    2017. arXiv 1603.01446 v1 was submitted on 4 March 2016, which is
    `published:` per ADR-002.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 1603.01446v3 (2 December 2016), 42 pp., the
    current version, the first NOTE on the work (NOTE-tmpdshmx). The
    published Information Fusion text was not read. Status set from the
    reading: Active. `published:` (2016-03-04, v1) and the identifiers
    stand. The arXiv listing's title spells "datastructure" as one word;
    the PDF and the journal title as registered spell "data structure",
    which the title here keeps. The summary is replaced by one from the text. The
    registration's summary held up on global sections as consistent fused
    states and on the consistency radius, with two corrections: the radius
    is defined on a presheaf, so the restriction maps carry the sensor
    models and need no gluing; and the paper credits locating faults to
    the pattern of discrepancies in one simulated case, and model failure
    to cohomology, not to the radius. Three THEORYs are filed from it
    (THEORY-tmpiycpt, THEORY-tmp5nb96, THEORY-tmpy95x7).
tags:
- mathematics
- information-theory
date: '2026-10-27'
published: '2016-03-04'
arxiv: '1603.01446'
doi: '10.1016/j.inffus.2016.12.002'
first_author: 'Robinson'
keywords:
- 'sheaves'
- 'sensor integration'
- 'data fusion'
- 'consistency radius'
implementations: []
summary: >-
  Robinson (2017), Information Fusion 36. An expository paper on sensor
  integration with sheaves. Sensor models become restriction maps between
  spaces of observations over sets of entities; the consistency radius of
  an assignment is its largest disagreement between an observation and the
  restriction of another, and with K-Lipschitz restrictions it bounds the
  distance to every global section below by ε/(1 + K). Fusion is the search
  for the nearest global section; in one simulated search-and-rescue
  scenario it cut the crash-location error 2–8×, and the pattern of
  discrepancies singled out a biased sensor. Cohomology, for linear sheaves,
  flags sensor and processing configurations whose data can be locally but
  not globally consistent. "Canonical" rests on axioms, not a theorem.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 QUESTION-tmpubsi9 THEORY-tmpy95x7 — Proposed or Open; the entries it was filed for and a THEORY filed from it, cited as open -->

# LIT-tmpn521a: Sheaves are the canonical data structure for sensor integration

Robinson, M. (2017). Sheaves are the canonical data structure for sensor integration. *Information Fusion*, 36, 208–224. doi:10.1016/j.inffus.2016.12.002.

Read in full on 2026-10-27 ([NOTE-tmpdshmx](../notes.d/NOTE-tmpdshmx.md)).

## Why this is here

A21 §5 called it "almost the practical engineering version of our
abstract proposal": distributed local observations supporting global
inference without a privileged observer, with residuals as evidence
against the correspondence model. It bears on [CLAIM-tmpdjt64](../claims.d/CLAIM-tmpdjt64.md) and
[QUESTION-tmpubsi9](../questions.d/QUESTION-tmpubsi9.md).
