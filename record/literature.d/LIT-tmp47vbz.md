---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpcuba0](../notes.d/NOTE-tmpcuba0.md)); worth reading as the four-page origin of the nonequilibrium work relation ⟨e^{−βW}⟩ = e^{−βΔF}: an equality, independent of path and switching rate, that turns irreversible work measurements into an equilibrium free-energy difference and gives ⟨W⟩ ≥ ΔF as a corollary by Jensen. Read it knowing two things. The physical-reservoir proof rests on weak coupling (Eq. 9 → 10), which the author states; and its usefulness is limited by the author''s own estimate to work fluctuations of order k_BT, so nanoscale systems or simulations.'
title: 'Nonequilibrium Equality for Free Energy Differences'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv cond-mat/9610209 v1, 30 Oct 1996, the only arXiv
    version, 11 pp., from the arXiv PDF; text extracted with PyMuPDF). I
    read every page: the abstract, the derivation for an isolated
    Hamiltonian system (Eqs. 6–8), the extension to a system weakly coupled
    to a reservoir (Eqs. 9–10), the corollaries (Eqs. 11–12), the
    Nosé–Hoover argument (Eqs. 13–17), the practical caveats and all 12
    references. I checked Eqs. 7–8 and the cumulant reduction (12) against
    the definitions. The Physical Review Letters version of record
    (78(14):2690–2693, 7 April 1997) was not seen and has a different
    title ("Nonequilibrium Equality …" for the preprint's "A
    nonequilibrium equality …"). Not held in the Anthology of the SOTA: a
    grep of its literature.d for "Jarzynski", the DOI and the arXiv id
    found nothing. `published:` is the arXiv v1 date. Filed with the
    critics of Prigogine's extremum principles and the fluctuation
    theorems, at the owner's request to fill out the record's coverage of
    dissipative structures.
tags:
- thermodynamics
- natural-sciences
date: '2026-10-02'
published: '1996-10-30'
doi: '10.1103/PhysRevLett.78.2690'
arxiv: 'cond-mat/9610209'
first_author: 'Jarzynski'
keywords:
- 'Jarzynski equality'
- 'free energy difference'
- 'nonequilibrium work'
- 'dissipated work'
- 'Nosé–Hoover thermostat'
- 'thermodynamic integration'
- 'free energy perturbation'
implementations: []
summary: >-
  Jarzynski (1997), DOI-10.1103/PhysRevLett.78.2690. For a classical
  system that starts in canonical equilibrium and is switched from
  Hamiltonian H_0 to H_1 at any finite rate, the average of e^{−βW} over
  repetitions equals e^{−βΔF} (Eq. 2), whatever the path and the switching
  time. The proof is exact for an isolated system and for Nosé–Hoover
  thermostats, and needs weak coupling for a physical reservoir.
  Thermodynamic integration and the Zwanzig perturbation formula are its
  slow and fast limits, and ⟨W⟩ ≥ ΔF follows by Jensen.
---
<!-- source-ok-file: cond-mat/9610209 — the arXiv version is titled "A nonequilibrium equality for free energy differences"; the published PRL title, recorded here, drops the article -->
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->

# LIT-tmp47vbz: Nonequilibrium Equality for Free Energy Differences

C. Jarzynski (1997), *Physical Review Letters 78(14), 2690–2693* — DOI-10.1103/PhysRevLett.78.2690 (preprint arXiv:cond-mat/9610209, 30 October 1996)

## Standing in the record

Filed on 2026-10-02 with the critics of Prigogine's extremum principles, the
maximum-entropy-production literature and the fluctuation theorems, at the
owner's request to fill out the record's coverage of dissipative
structures. No anthology topic can hold a result in nonequilibrium
statistical mechanics read for itself, and the anthology does not hold it.

[NOTE-tmpcuba0](../notes.d/NOTE-tmpcuba0.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. It is the founding statement of one of the two exact
far-from-equilibrium relations every later fluctuation-theorem paper builds
on. Crooks ([LIT-tmpc4996](LIT-tmpc4996.md)) derived it again from an entropy-production
fluctuation theorem for stochastic dynamics, and Seifert's review
([LIT-tmpcfjz8](LIT-tmpcfjz8.md)) places it as the integral fluctuation theorem for
dissipated work. The record already reads its equation once, in the quantum
thermodynamics review [LIT-010](LIT-010.md), which derives the classical Jarzynski and
Crooks relations in full and notes that Crooks needs detailed balance with
the bath.

Its bearing on the record's stochastic-thermodynamics-of-computation line is
background, not support. Still et al. ([LIT-327](LIT-327.md)) cite it as the relation that
assumes a known protocol, which is exactly the assumption they drop.
[THEORY-026](../theory.d/THEORY-026.md) does not rest on it: its identity is an ensemble average for a
discrete Markov chain and uses no work fluctuation relation. The paper is
also the first place the record can point for "dissipated work" as W − ΔF
with ΔF the equilibrium free energy. [LIT-327](LIT-327.md)'s dissipation subtracts a
nonequilibrium free energy instead, and [NOTE-tmpcuba0](../notes.d/NOTE-tmpcuba0.md) says how the two
differ.

It has nothing to say about dissipative structures in Prigogine's sense: it
concerns finite systems driven between equilibrium states, not steady states
held far from equilibrium.
