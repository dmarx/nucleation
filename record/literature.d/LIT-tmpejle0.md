---
status: Active
status_note: >-
  read in full 2026-10-31 (NOTE-tmpxh170); worth reading as the letter that
  named the thermodynamic uncertainty relation: a current counted in a
  steady state with relative uncertainty ε costs at least 2k_BT/ε² of
  dissipation, proved within linear response and for single-cycle
  networks, conjectured with numerical support for many-cycle ones
  (THEORY-tmpnaoak). It bounds the precision of currents, not of
  occupations.
title: 'Thermodynamic Uncertainty Relation for Biomolecular Processes'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A13 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (PRL 114, 158101, 2015-04-15) and arXiv (v1 2015-02-20);
    `published:` takes the arXiv date (ADR-002). A13 gave the
    relation through a citation marker that did not render; this is
    the paper that introduced it. The summary follows the abstract
    and the exchange's description; a reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full in NOTE-tmpxh170 from arXiv 1502.05944v2 with its
    supplement. Status Deferred → Active. The citation stands. The
    summary is rewritten from the text: the relation is for currents in
    finite Markov networks, proved here only within linear response and
    for unicyclic networks. Produces THEORY-tmpnaoak.
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
published: '2015-02-20'
arxiv: '1502.05944'
doi: '10.1103/PhysRevLett.114.158101'
first_author: 'Barato'
keywords:
- 'thermodynamic uncertainty relation'
- 'entropy production'
- 'precision'
- 'biomolecular processes'
- 'Fano factor'
implementations: []
summary: >-
  Barato & Seifert (2015). In a nonequilibrium steady state of a Markov
  jump network obeying local detailed balance, the entropy produced while
  a current is counted times the current's squared relative uncertainty
  is at least 2k_BT, independent of time. Proved within linear response
  for any network and for unicyclic networks at any affinity, where the
  sharper bound is (A/N) coth(A/2N), which also tightens the Fano-factor
  bound on the number of states in an enzyme cycle. For multicyclic
  networks far from equilibrium it is a conjecture supported by
  numerics on seven networks.
---

# LIT-tmpejle0: Thermodynamic Uncertainty Relation for Biomolecular Processes

Barato, A. C., & Seifert, U. (2015). Thermodynamic uncertainty relation for biomolecular processes. *Physical Review Letters*, 114, 158101.

Read in full in NOTE-tmpxh170.

## Why this is here

A13 §6 cited it as tying the resource cost of maintenance to its precision. Read with Seifert's review (LIT-523). The reading narrows that: the relation prices the precision of a current, such as a production flux counted over time, and the authors set occupation observables aside explicitly. It does not price how reliably, or for how long, a maintained state is held; that is the escape-rate question of THEORY-tmpjzj2n. Applied to a construction like CASE-tmpwxags it bites only once every production step is reversible.
