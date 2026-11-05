---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmp241k1](../notes.d/NOTE-tmp241k1.md)) from the accepted preprint of
  November 2007 posted on the second author's University of Alberta page;
  worth reading as the argument, with a pathological example, that 0–1
  coverage within a time standard is a poor proxy for the real objective
  of an EMS, survivors, and as the construction of survival-maximizing
  versions of four standard covering models, compared on Edmonton data.
  The switch to a survival objective gives up to 7.7% more expected
  survivors than maximal covering and up to 23.5% more than the q-median
  in the deterministic models, and the gap shrinks once random response
  times or busy probabilities enter the coverage model. Its main limits:
  survival functions for cardiac arrest only, assumed to hold for all
  urgent calls; static location models with no dispatch or relocation;
  one city. Filed as a stand-in for McLay and Mayorga (2010),
  [LIT-tmprh2zk](LIT-tmprh2zk.md), for the shared idea only; it partly pulls against that
  paper's headline.
title: 'Ambulance location for maximum survival'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04, at the owner's request, as a
    stand-in for McLay and Mayorga (2010), LIT-tmprh2zk, a work cited in
    the pasted bibliography on emergency readiness (written by another
    assistant, A, and pasted by the owner on 2026-11-04) of which no
    lawful full text was found. This work is not in A's list. Citation
    checked against Crossref: Erhan Erkut, Armann Ingolfsson and Güneş
    Erdoğan, Naval Research Logistics 55(1), 42–58,
    doi:10.1002/nav.20267, a journal article; online 3 December 2007
    (`published:`), issue February 2008. Not held before. Copy: the
    accepted preprint, headed "This is a preprint of an article accepted
    for publication in Naval Research Logistics" and dated November 2007,
    at https://sites.ualberta.ca/~aingolfs/documents/survival15november07.pdf
    on Ingolfsson's University of Alberta page (an author copy), 32 pages,
    extracted with pdftotext. It is not the typeset version of record;
    page numbers in the reading are the preprint's.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
published: '2007-12-03'
doi: '10.1002/nav.20267'
first_author: 'Erkut'
keywords:
- 'ambulance location'
- 'covering models'
- 'survival function'
implementations: []
summary: >-
  Erkut, Ingolfsson & Erdoğan (2008). Takes the real objective of an EMS
  to be survivors, with coverage within a time standard a proxy, and
  replaces 0–1 coverage in four standard location models (MCLP, MEXCLP and
  their probabilistic-response versions) with a survival function for
  out-of-hospital cardiac arrest. On Edmonton data (180 demand points, 16
  candidate sites), evaluated with the approximate hypercube model,
  maximal-covering locations give up to 7.7% fewer expected survivors and
  q-median locations up to 23.5% fewer than survival-maximizing ones in the
  deterministic models; with random response times the gain averages 0.9%,
  and in the model with both random response times and busy probabilities
  it adds little. Locating to minimize average response time does worse
  still, by 6.5% on average against the full survival model.
---
<!-- inactive-ok-file: LIT-tmprh2zk THEORY-tmpagbfa — Unavailable or Proposed; the unread paper this stands in for, and the account filed from this reading -->

# LIT-tmprfb8b: Ambulance location for maximum survival

Erkut, E., Ingolfsson, A. & Erdoğan, G. (2008). Ambulance location for maximum survival. *Naval Research Logistics* 55(1): 42–58. doi:10.1002/nav.20267.

## Key takeaways

*From the reading, [NOTE-tmp241k1](../notes.d/NOTE-tmp241k1.md). Page numbers are the preprint's.*

- **Coverage is a proxy.** "We will take as given that the real objective
  for an EMS system is to maximize the number of patients that survive and
  that coverage is used as a proxy for the real objective" (p. 1).
- **A proxy can be arbitrarily bad.** By a two-point example, "covering
  models can result in arbitrarily poor location decisions for emergency
  facilities" (p. 2).
- **How much it matters.** Deterministic models: survivors up to 7.7%
  lower with maximal covering and up to 23.5% lower with the q-median
  (pp. 12–13). With random response times the gain averages 0.9% over 16
  problems (p. 18).
- **The objective, not the uncertainty.** In the comparison of all ten
  models, "just changing the objective function to expected number of
  survivors achieves all of the benefits, even without incorporating the
  two elements of uncertainty in the model" (p. 22).

## Standing in the record

Filed at the owner's request as a stand-in for McLay and Mayorga (2010),
[LIT-tmprh2zk](LIT-tmprh2zk.md), which could not be read. It stands in for the shared idea,
that a response-time standard is a proxy for survival and that locating
for the proxy can differ from locating for survivors, and states it more
strongly than that paper's abstract. It does not stand in for McLay and
Mayorga's evaluation method or their Hanover County findings, and it
partly pulls against them: it argues that standard coverage models
"should not be used for EMS vehicle location" (p. 2), while that abstract
reports thresholds whose optimum is the survival optimum. Its own Table 6
softens the difference: coverage with response-time randomness or busy
probabilities reaches the best-known survival value. Filed from it:
[THEORY-tmpagbfa](../theory.d/THEORY-tmpagbfa.md).
