---
status: Unavailable
status_note: 'unread, registered 2026-10-16. A lawful copy was sought and not reached: OpenAlex marks it closed with no repository full text, Crossref lists only the Taylor & Francis and JSTOR copies, and web searches found no author-posted or course-hosted copy. Its generalized-variance measure and χ² asymptotics are restated by Barnett, Barrett and Seth ([LIT-tmpmi22s](LIT-tmpmi22s.md)), which is how the record reads it until a copy is supplied.'
title: 'Measurement of Linear Dependence and Feedback between Multiple Time Series'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed at the owner's request as the multivariate and frequency-domain
    form of Granger causality that Barnett, Barrett and Seth (2009) and
    Barnett and Bossomaier (2012, NOTE-053) build on. Citation checked
    against Crossref on 2026-10-16. Not held in the Anthology of the SOTA:
    a grep of its record/ (clone of 2026-10-12) for "Geweke" and the DOI
    found nothing. Crossref gives June 1982 and no day. Published with
    discussion; the comments and the rejoinder (doi:10.2307/2287243) are
    separate items and are not filed.
tags:
- mathematical-statistics
- causality
date: '2026-10-16'
published: '1982-06-01'
doi: '10.1080/01621459.1982.10477803'
first_author: 'Geweke'
keywords:
- 'linear dependence'
- 'feedback'
- 'multiple time series'
- 'spectral decomposition'
- 'Granger causality'
implementations: []
summary: >-
  Geweke (1982), *Journal of the American Statistical Association* 77(378): 304–313. Measures the linear dependence between two multivariate time series as the sum of three parts: feedback from the first to the second, feedback from the second to the first, and instantaneous feedback. The directed measures are log ratios of generalized variances (determinants of residual covariance matrices), have asymptotic χ² null distributions, and decompose additively by frequency. Unread; known through Barnett, Barrett and Seth and the abstract.
extends:
- LIT-tmppqyor
extended_by:
- LIT-tmpmi22s
---

# LIT-tmpj9yuo: Measurement of Linear Dependence and Feedback between Multiple Time Series

John Geweke (1982), "Measurement of Linear Dependence and Feedback between Multiple Time Series", *Journal of the American Statistical Association* 77(378): 304–313 — doi:10.1080/01621459.1982.10477803

## Key takeaways

*Unread. From the abstract and citing works, to be checked against the text.*

- **Three-way split.** The abstract, as Semantic Scholar gives it: the
  measure of linear dependence is the sum of linear feedback from the
  first series to the second, from the second to the first, and
  instantaneous linear feedback.
- **Generalized variance.** For a multivariate predictee the residual
  variance is replaced by its determinant, F = ln(|Σ(ε)|/|Σ(ε′)|).
  Barnett, Barrett and Seth adopt this form, say Geweke lists several
  motivations for it, and add the Gaussian equivalence with transfer
  entropy as another ([NOTE-tmp2veo7](../notes.d/NOTE-tmp2veo7.md)).
- **Inference.** The maximum-likelihood estimator is asymptotically χ²
  under the null and non-central χ² under the alternative, as Barnett,
  Barrett and Seth cite it ([14]).
- **By frequency.** The directed measures decompose additively over
  frequency, which is the spectral Granger causality later work uses.

## Standing in the record

Filed on 2026-10-16 as the form of Granger causality that the record's two
transfer-entropy readings rest on. Barnett, Barrett and Seth's equivalence
is stated for this measure, not for Granger's univariate one. Until a copy
is supplied the record holds only what they and the abstract say. That
includes the non-central χ² claim, which [NOTE-053](../notes.d/NOTE-053.md) argues can only be a
local-alternative approximation.
