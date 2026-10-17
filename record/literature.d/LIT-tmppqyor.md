---
status: Unavailable
status_note: 'unread, registered 2026-10-16. A lawful copy was sought and not reached: Crossref and the Econometric Society give only the JSTOR copy (stable 1912791), behind a login; a course-hosted copy on a University of Freiburg seminar page (jeti.uni-freiburg.de, stud_sem_SS_09/grangercausality.pdf) refused this client''s connection three times and answered WebFetch with HTTP 503; a Bilkent course copy found by search returned 404. Searched again on 2026-10-17: the Freiburg host still reset the connection, and the only other copies found (ResearchGate, Scribd) are user uploads whose authorization could not be established. The record reads it through Barnett, Barrett and Seth ([LIT-tmpmi22s](LIT-tmpmi22s.md)), Seth ([LIT-tmplr1w9](LIT-tmplr1w9.md)) and Eichler and Didelez ([LIT-tmp7q0hf](LIT-tmp7q0hf.md)), which restate its definition, until a copy is supplied.'
title: 'Investigating Causal Relations by Econometric Models and Cross-spectral Methods'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed at the owner's request as the source of the definition that nine
    of the record's documents use without holding it. Citation checked
    against Crossref on 2026-10-16. Not held in the Anthology of the SOTA:
    a grep of its record/ (clone of 2026-10-12, d1573d2) for "Granger" and
    the DOI found nothing, and its topic vocabulary has no word for causal
    inference or time series. Crossref gives August 1969 and no day.
tags:
- causality
- mathematical-statistics
date: '2026-10-16'
published: '1969-08-01'
doi: '10.2307/1912791'
first_author: 'Granger'
keywords:
- 'causality'
- 'feedback'
- 'cross-spectral methods'
- 'econometric models'
- 'prediction'
implementations: []
summary: >-
  Granger (1969), *Econometrica* 37(3): 424–438. Proposes testable definitions of causality and feedback between stationary time series: Y causes X if the past of Y improves the prediction of X beyond what the other relevant past information gives. Shows the cross spectrum can be decomposed into two parts, one for each causal arm of a feedback loop. Unread; known through the works that restate it.
extended_by:
- LIT-tmp7q0hf
- LIT-tmpj9yuo
- LIT-tmplr1w9
- LIT-tmpmi22s
---

# LIT-tmppqyor: Investigating Causal Relations by Econometric Models and Cross-spectral Methods

C. W. J. Granger (1969), "Investigating Causal Relations by Econometric Models and Cross-spectral Methods", *Econometrica* 37(3): 424–438 — doi:10.2307/1912791

## Key takeaways

*Unread. From citing works, to be checked against the text.*

- **The definition.** Y causes X if including the past of Y reduces the
  prediction error of X, relative to a predictor that already uses all
  other relevant past information. The abstract calls the definitions
  "testable", and Barnett, Barrett and Seth credit the idea to Wiener
  (1956) and its linear-autoregressive form to this paper.
- **Relative to an information set.** Eichler and Didelez say Granger
  required the set of series to contain all "relevant" processes, and did
  not ask whether an intervention on the cause is possible at all
  ([NOTE-tmpm48uq](../notes.d/NOTE-tmpm48uq.md), Conclusion).
- **Feedback and the cross spectrum.** By the abstract, the cross spectrum
  of two series in a feedback relation splits into two parts, each tied to
  one direction of influence. Geweke (1982) is the frequency decomposition
  later work uses.

## Standing in the record

Filed on 2026-10-16 because the record names Granger causality in nine
documents, all through other authors. Its content is here only as citing
works state it. [TERM-tmpq0ms2](../terms.d/TERM-tmpq0ms2.md) defines the term from those statements, not
from this paper. A supplied copy would let the record check two things:
whether the paper's information set is the causal-sufficiency condition
Eichler and Didelez read into it, and what it says about instantaneous
causality.
