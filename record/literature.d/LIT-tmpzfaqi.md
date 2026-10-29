---
status: Active
status_note: >-
  read 2026-10-29 (NOTE-tmpcmbzs) in full, from arXiv's v1; worth reading
  as the defenders' survey that rewrites a dozen measures of causal
  strength (Eells, Suppes, Cheng, Lewis, Pearl's PN/PS/PNS, Galton,
  bit-flip, effect information, EI) as functions of sufficiency P(e | c)
  and necessity 1 − P(e | C\c), and that reports causal emergence for
  every measure on one bipartite Markov chain under maximum-entropy,
  stationary and local intervention distributions. Read it knowing that
  the model is built so its macro is a deterministic NOT gate whatever
  the micro noise; that in its symmetric version the macro distributions
  are the images of the micro ones, so it is a common-distribution test,
  and there the system-level EI cannot show emergence under either the
  stationary or the maximum-entropy distribution (data processing; the
  record's computation agrees), which the paper concedes only for the
  stationary case; that "we
  prove" in the abstract covers rewritings of definitions, not a theorem
  that emergence must occur; and that the per-transition and normalized
  measures that do show emergence are not bounded by data processing.
  It does not meet THEORY-787's promote_when.
title: 'Causal emergence is widespread across measures of causation'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Registered on 2026-10-29 from the triage of the day (curation entry
    of 20:59), File tier, for QUESTION-204 and THEORY-787's promote_when:
    it is the paper Hoel offers as the result that the macro advantage
    survives non-uniform intervention distributions, so reading it
    either meets the promote_when or shows it to be more toy systems,
    which the promote_when says cannot settle it. Citation checked
    against arXiv (2202.01854, v1 submitted 3 February 2022, the only
    version; 22 pages, physics.soc-ph): Renzo Comolatti and Erik Hoel,
    "Causal emergence is widespread across measures of causation".
    arXiv lists Comolatti first; the PDF prints the two names side by
    side with Hoel, the corresponding author, on the left. `published:`
    is the arXiv v1 date (ADR-002). Crossref holds a later journal
    article by the same authors, "Consilience in Causation: Causal
    Emergence Is Found Across Measures of Causation", Entropy 27(8), 825
    (2025-08-04, doi:10.3390/e27080825); it was not read and is not this
    work.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full (NOTE-tmpcmbzs). Status Deferred → Active. The authors'
    code (github.com/renzocom/causal_emergence) was read where it settles
    how the figures' averages are computed. The summary is written from
    the reading.
tags:
- causality
- information-theory
- complex-systems
date: '2026-10-29'
published: '2022-02-03'
arxiv: '2202.01854'
first_author: 'Comolatti'
keywords:
- 'causal emergence'
- 'causal primitives'
- 'sufficiency'
- 'necessity'
- 'determinism'
- 'degeneracy'
- 'intervention distribution'
- 'measures of causation'
implementations:
- 'https://github.com/renzocom/causal_emergence'
extends:
- LIT-1038
rivals:
- LIT-tmpr2bnp
summary: >-
  Comolatti & Hoel (arXiv 2022). Twelve measures of causal strength from
  philosophy, statistics and psychology are written in terms of
  sufficiency P(e | c) and necessity 1 − P(e | C\c), or of Hoel's
  determinism and degeneracy; several turn out to be the same measure
  (Pearl's PNS, PN and PS are Eells's, Lewis's and Cheng's). Each needs an
  intervention distribution P(C): observational (stationary), maximum
  entropy, or a local Hamming ball. On one 16-state bipartite Markov chain,
  whose two-state macro is a deterministic NOT gate, every measure shows
  causal emergence for some transitions and parameters; the system-level
  effective information under the stationary distribution does not, which
  the paper says was known.
---

# LIT-tmpzfaqi: Causal emergence is widespread across measures of causation

Comolatti, R. & Hoel, E. (2022). Causal emergence is widespread across
measures of causation. arXiv:2202.01854.

Read in full on 2026-10-29 (NOTE-tmpcmbzs).

## Why this is here

The triage of 2026-10-29 (curation entry of 20:59) filed it for
QUESTION-204 and THEORY-787's promote_when, which is met by a result that
the macro advantage survives an intervention distribution other than the
uniform one imposed separately at each level, on systems not built for
it. This is the paper Hoel offers as that result. Read with Eberhardt and
Lee 2022 (LIT-tmpr2bnp), it does not meet the promote_when
(NOTE-tmpcmbzs, THEORY-tmphfpe7).
