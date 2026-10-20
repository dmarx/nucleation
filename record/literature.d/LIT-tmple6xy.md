---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpi32zs](../notes.d/NOTE-tmpi32zs.md)) in full, from the published version on
  Chorin's Berkeley page; worth reading for the exact generalized Langevin
  equation under three projections (conditional expectation, linear,
  finite-rank), for computing the memory kernel from equilibrium
  correlation functions through a Volterra equation, and for the
  t-damping (t-model) equation dΦ/dt = R̄(Φ) + tS(Φ) with its proof that,
  for separable Hamiltonians, it dissipates the effective energy
  ([THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md)). Read it knowing that it has one 4-variable example,
  no error bound for any approximation, no Markovian augmentation by memory
  coordinates, that its abstract's "close to the best possible estimate"
  holds on that example only to t ≈ 8, and that the t-model it calls a
  short-memory approximation treats the kernel as constant over the whole
  window.
title: 'Optimal prediction with memory'
version: 3
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is the first of Crossref's month, June 2002, per ADR-002. No open copy was confirmed; arXiv:math/0101022 ("Non-Markovian Optimal Prediction") is a different paper. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Copy hunt, not a reading. Semantic Scholar's open-access link points to
    the published version (Physica D 166:239–257, 19 pages) posted on
    Chorin's own Berkeley page; it was fetched and confirmed as this paper
    by its first and last pages, and the `url:` is added. Unpaywall and
    OpenAlex report the work closed; OpenAlex also lists a CiteSeerX record,
    not followed. arXiv:math/0101022 is confirmed a different paper:
    "Non-Markovian Optimal Prediction" (2001), whose abstract presents a
    Monte Carlo approximation of the orthogonal dynamics and cites the need
    for memory as "previous work". An arXiv search by title and author found
    no version of this paper. Status stays Deferred.
- version: 3
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpi32zs) from the published version at the `url:`.
    Status Deferred → Active. THEORY-tmpepvai is filed from Theorem 8.1.
    The summary is corrected: the paper keeps the memory term and shows on
    one example that it is needed past a couple of oscillations, but its
    main content is how to approximate the memory (a Volterra equation
    from correlation functions, short-memory and t-damping forms), so the
    summary now says so. The body's "Not read" paragraph is replaced.
tags:
- mathematics
- natural-sciences
- probabilistic-modeling
date: '2026-10-19'
published: '2002-06-01'
doi: '10.1016/S0167-2789(02)00446-3'
url: 'https://math.berkeley.edu/~chorin/CHK02.pdf'
first_author: 'Chorin'
keywords:
- 'Mori–Zwanzig'
- 'optimal prediction'
- 'memory kernel'
- 'model reduction'
implementations: []
summary: >-
  Chorin, Hald & Kupferman (2002). Writes the resolved variables of an ODE with uncertain unresolved initial data as an exact generalized Langevin equation (Markovian term, memory, noise) under three projections, computes the memory from equilibrium correlation functions through a Volterra equation, and introduces the t-damping (t-model) equation, whose leading-order memory term dissipates the effective energy of separable Hamiltonian systems. On one 4-variable example the memory restores the decay of the conditional mean that the Markovian equation misses. No error bounds.
---
<!-- inactive-ok-file: CLAIM-327 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# LIT-tmple6xy: Optimal prediction with memory

Chorin, A. J., Hald, O. H. & Kupferman, R. (2002). Optimal prediction with memory. *Physica D* 166(3–4): 239–257. doi:10.1016/S0167-2789(02)00446-3.

Read in full in [NOTE-tmpi32zs](../notes.d/NOTE-tmpi32zs.md). [THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md) is filed from it.

## Why this is here

A5 called it "the most direct foundation for comparing reduced-model prediction, unresolved dynamics, and memory", to be read before any reformulation of dynamical independence. Bears on [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md), [THEORY-257](../theory.d/THEORY-257.md) and [CLAIM-327](../claims.d/CLAIM-327.md).
