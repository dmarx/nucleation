---
status: Active
status_note: >-
  read 2026-10-31 ([NOTE-tmpif2g2](../notes.d/NOTE-tmpif2g2.md); appendices skimmed); worth reading
  for the cycle–cocycle geometry of reaction hypergraphs and as the
  exact form of the exchange's "a productive cycle need not be a
  stoichiometric cycle": catalysts cancel from the stoichiometric
  matrix, so mutual catalytic production is not a cycle of it
  ([THEORY-tmp05y8u](../theory.d/THEORY-tmp05y8u.md)).
title: 'Geometry of Nonequilibrium Reaction Networks'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A13 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (PRX 13, 021040, 2023-06-27) and arXiv (v1 2022-08-02);
    `published:` takes the arXiv date (ADR-002). The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read from the arXiv preprint 2208.01290v4, 36 pp., main text in
    full and appendices skimmed, in NOTE-tmpif2g2; status Deferred →
    Active. The citation stands. The summary is rewritten from the text.
    The reading produced THEORY-tmp05y8u and supplies the one-chemostat
    proof in THEORY-tmplh6oa.
tags:
- thermodynamics
- mathematics
date: '2026-10-31'
published: '2022-08-02'
arxiv: '2208.01290'
doi: '10.1103/PhysRevX.13.021040'
first_author: 'Dal Cengio'
keywords:
- 'reaction networks'
- 'cycles'
- 'nonequilibrium'
- 'geometry'
implementations: []
summary: >-
  Dal Cengio, Lecomte & Polettini (2023). Extends Hill–Schnakenberg
  cycle analysis from linear reaction networks to interacting ones,
  which are hypergraphs, by row-reducing the stoichiometric matrix:
  cycles span its kernel and carry steady currents and the
  non-conservative part of the affinity, cocycles span the orthogonal
  complement and carry transient currents and conservative forces, and
  an integrator recovers chemical potentials. One chemostat cannot drive
  a network; suppressing a cocycle creates a new conservation law. Near
  equilibrium the relaxation and response Onsager matrices share their
  spectrum, and the decomposition gives a linear-regime reconstruction
  of metabolic fluxes that satisfies Kirchhoff's laws.
---

# LIT-tmpw6f74: Geometry of Nonequilibrium Reaction Networks

Dal Cengio, S., Lecomte, V., & Polettini, M. (2023). Geometry of nonequilibrium reaction networks. *Physical Review X*, 13, 021040.

Read in [NOTE-tmpif2g2](../notes.d/NOTE-tmpif2g2.md).

## Why this is here

A13 §4 used it to separate three kinds of cycle that the exchange had run together: a production cycle among constraints, a stoichiometric cycle in the kernel of the reaction network, and a cycle in a sheaf's kernel. "A productive cycle need not be a stoichiometric cycle." The reading confirms this and makes it exact ([THEORY-tmp05y8u](../theory.d/THEORY-tmp05y8u.md)): the paper's cycles are built from net stoichiometry, from which a catalyst cancels, so the mutual production that [CLAIM-tmpczfpk](../claims.d/CLAIM-tmpczfpk.md) proves necessary is invisible to them and to the thermodynamic budget. In [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) rewritten as chemistry, the stoichiometric cycles are the fuel-to-waste pathways. Its islands also give [CLAIM-478](../claims.d/CLAIM-478.md) a chemical mechanism: a slowed reaction channel makes an approximate conservation law over the window the slowing opens.
