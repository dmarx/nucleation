---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmp3zjqz](../notes.d/NOTE-tmp3zjqz.md)); worth reading as the short,
  self-contained proof, for overdamped diffusions, that a nonequilibrium
  escape rate e^{−ΩΔI} is bracketed by the entropy produced in relaxing
  into the attractor and in escaping it ([THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md)), with a
  recursive expansion of the quasi-potential about the free energy. The
  bracket closes only at detailed balance.
title: 'Bridging Freidlin-Wentzell large deviations theory and stochastic thermodynamics'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A14 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (PRE 111, 024106, 2025-02-04) and arXiv (v1 2024-09-11);
    `published:` takes the arXiv date (ADR-002). The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full in NOTE-tmp3zjqz from arXiv 2409.07599v1. Status
    Deferred → Active. The citation stands. The summary is rewritten from
    the text. The registration's "entropy production along the
    transition" is right; the result is a two-sided bound, not an
    identity. Produces THEORY-tmpjzj2n with LIT-tmpm46ks.
tags:
- thermodynamics
- mathematics
date: '2026-10-31'
published: '2024-09-11'
arxiv: '2409.07599'
doi: '10.1103/PhysRevE.111.024106'
first_author: 'Santolin'
keywords:
- 'Freidlin-Wentzell theory'
- 'large deviations'
- 'stochastic thermodynamics'
- 'quasipotential'
- 'escape rate'
- 'instanton'
implementations: []
summary: >-
  Santolin, Freitas, Esposito & Falasco (2025). For overdamped
  diffusions with weak noise and a nonconservative force, the
  Freidlin–Wentzell quasi-potential is expanded in powers of the force
  about the detailed-balance free energy, each order computed along
  detailed-balanced relaxation; the first order saturates the emergent
  second law. Splitting the drift into a quasi-potential gradient and an
  orthogonal circulation, the escape rate from an attractor is bracketed
  between minus the entropy produced in relaxing into it and the entropy
  produced along the most likely escape path. The bracket closes at
  detailed balance; a sheared double well illustrates it.
---

# LIT-tmp24302: Bridging Freidlin-Wentzell large deviations theory and stochastic thermodynamics

Santolin, D., Freitas, N., Esposito, M., & Falasco, G. (2025). Bridging Freidlin-Wentzell large deviations theory and stochastic thermodynamics. *Physical Review E*, 111, 024106.

Read in full in [NOTE-tmp3zjqz](../notes.d/NOTE-tmp3zjqz.md).

## Why this is here

With [LIT-tmpm46ks](LIT-tmpm46ks.md), A14's source for reading a maintained regime's lifetime and escape route thermodynamically, beside the SLT reading of a posterior concentrating on a singular set. The reading supplies the theorem: lifetime e^{ΩΔI}, with ΔI between the dissipation of relaxing in and minus that of escaping out ([THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md)). It also marks where the SLT side has no counterpart: the circulation that separates relaxation from escape, and so opens the bracket, is absent from a Gibbs posterior.
