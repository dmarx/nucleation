---
status: Active
status_note: >-
  read in full 2026-10-15 from the NIH author manuscript in PubMed Central (PMC3062724,
  NIHMS252298), taken as JATS XML from NCBI E-utilities (eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3062724)
  because the PMC article page served a reCAPTCHA; the typeset Elsevier open-archive
  PDF returned 403, so printed pagination was not checked. Worth reading as a compact
  statement of Bayesian ideal observer analysis: the ideal is optimal "given the
  available information and any specified constraints", written as an expected-utility
  argmax over the posterior given either the stimulus or a constrained neural representation
  Z = g(S;θ), with a survey of applications and some numbers (r = 0.83 for colour
  naming on individual cone mosaics; 42% lower MSE for a natural-statistics decoder
  of peripheral samples; about 99% of variance in contour-occlusion judgments).
  For [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md) it shows less than the question assumes: it gives no formula
  for efficiency (the squared d′ ratio is not stated here and should be cited to
  Burgess et al. 1981 or Pelli and Farell 1999, or owned by the record), and its
  constrained ideals restrict the input, a garbling of the stimulus, with unrestricted
  computation on it, so losses are located stage by stage by the data-processing
  logic, not by an optimum over a restricted class of observers as in [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md).
  Its nearest analogue to a bounded class is the comparison with named heuristic
  rules (serial one-location attention, MAP fixation selection), and its remark
  that far-below-ideal performance leaves many models standing is the empirical
  form of the point that a gap does not identify its cause. Consistent with [THEORY-031](../theory.d/THEORY-031.md);
  no bearing on [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) itself.
title: Contributions of ideal observer theory to vision research
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref
    gives April 2011, so `published:` is the first of the month. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the authors, title and identifier found nothing. Read the same day (NOTE-tmph7b4n).'
tags:
- cognition
- neuroscience
- probabilistic-modeling
date: '2026-10-15'
published: '2011-04-01'
doi: 10.1016/j.visres.2010.09.027
first_author: Geisler
keywords:
- ideal observer
- efficiency
- vision
- signal detection
implementations: []
summary: >-
  Geisler (2011), Vision Research 51(7). A short review, not a methods paper. It
  defines the ideal observer as the device that "performs a given task at the optimal
  level possible, given the available information and any specified constraints",
  writes the Bayesian ideal as an argmax of expected utility over the posterior
  given either the stimulus S or a constrained neural representation Z = g(S;θ)
  (eq. 1), and surveys applications from photon-noise detection to eye-movement
  search. It gives no formula for efficiency and no procedure for locating information
  loss beyond saying that constraints are added to the ideal one at a time (optics,
  receptor sampling, receptor noise, ganglion-cell summation) and that models are
  built by "degrading the ideal observer with hypothesized neural noise or with
  hypothesized heuristic computations". Its constraints restrict the information
  available to an optimal decoder; it has no notion of an optimum over a restricted
  class of computations, though its attention examples compare the ideal with specific
  suboptimal rules (a one-location "serial" mechanism, a MAP searcher, a random
  searcher).
---

# LIT-tmp5yjyp: Contributions of ideal observer theory to vision research

Geisler, W. S. (2011). Contributions of ideal observer theory to vision research. *Vision Research* 51(7), 771–781. DOI 10.1016/j.visres.2010.09.027

## Key takeaways

Read in full ([NOTE-tmph7b4n](../notes.d/NOTE-tmph7b4n.md)). A short review, not a methods paper. It defines the ideal observer as the device that "performs a given task at the optimal level possible, given the available information and any specified constraints", writes the Bayesian ideal as an argmax of expected utility over the posterior given either the stimulus S or a constrained neural representation Z = g(S;θ) (eq. 1), and surveys applications from photon-noise detection to eye-movement search. It gives no formula for efficiency and no procedure for locating information loss beyond saying that constraints are added to the ideal one at a time (optics, receptor sampling, receptor noise, ganglion-cell summation) and that models are built by "degrading the ideal observer with hypothesized neural noise or with hypothesized heuristic computations". Its constraints restrict the information available to an optimal decoder; it has no notion of an optimum over a restricted class of computations, though its attention examples compare the ideal with specific suboptimal rules (a one-location "serial" mechanism, a MAP searcher, a random searcher).

## Why this is here

The owner asked whether material downstream of computational indistinguishability, or the signal detection literature, could help with [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) and the bounded-observer questions. Read for [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md). Ideal-observer efficiency is the empirical measure of the gap between an ideal and a bounded observer.

The reading ([NOTE-tmph7b4n](../notes.d/NOTE-tmph7b4n.md)) narrows this. The review defines efficiency nowhere; the squared ratio of human to ideal d′ is from Burgess et al. 1981 and Pelli and Farell 1999. And its constrained ideal observers degrade the input, which loses information, while [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) restricts the tests on an intact input. The two are the two receivers [CLAIM-199](../claims.d/CLAIM-199.md) separates.
