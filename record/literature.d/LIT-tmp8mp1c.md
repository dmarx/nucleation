---
status: Active
status_note: >-
  read in full 2026-11-02 ([NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md)), from arXiv:2506.02970v3 with its
  supplementary material; worth reading as a clean physical case of
  slowness picking out structure: under weak local noise, a Hamiltonian's
  small conserved quantities are the slowest modes because they do not
  spread, while generic operators spread and decay. The correspondence is
  shown by exact diagonalization at nine sites or fewer; its large-system
  footing is a perturbative argument the authors qualify themselves.
title: 'Integrals of motion as slow modes in dissipative many-body operator dynamics'
version: 1
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed and read on the owner's request, after the owner asked whether
    it bears on the record. Citation checked against arXiv metadata and
    Crossref (no email address sent, ADR-008): Tian-Hua Yang and Dmitry
    A. Abanin, Physical Review B 112, 094304, published online
    2025-09-08. `published:` is the arXiv v1 submission date,
    2025-06-03, per ADR-002. Two THEORYs are filed from it
    (THEORY-tmpggrkf, THEORY-tmpull8q).
tags:
- natural-sciences
- complex-systems
date: '2026-11-02'
published: '2025-06-03'
arxiv: '2506.02970'
doi: '10.1103/d9b4-wlv6'
first_author: 'Yang'
keywords:
- 'Lindbladian'
- 'integrals of motion'
- 'slow modes'
- 'operator growth'
- 'open quantum many-body systems'
- 'approximate conservation laws'
implementations: []
summary: >-
  Yang & Abanin (2025), PRB 112, 094304. Under weak local noise an
  operator's norm decays at a rate proportional to its size, the number of
  sites it acts on. Under chaotic Hamiltonian dynamics generic operators
  grow, so they decay ever faster, while small-sized integrals of motion
  do not grow and decay slowly. Exact diagonalization of the Lindbladian
  for Ising and Heisenberg chains of up to nine sites finds the slowest
  eigenoperators to be linear combinations of the known exact and
  approximate integrals of motion, and turns up approximate ones not put
  in by hand. A perturbation theory argues that this survives at large
  size because the relevant gap is not the level spacing but one of order
  min(γL, √(v_Bγ)); the authors add that hydrodynamic modes may close
  that gap.
---
<!-- inactive-ok-file: CLAIM-478 THEORY-tmpull8q — Proposed; the claim it bears on most and a THEORY filed from it, cited as open -->

# LIT-tmp8mp1c: Integrals of motion as slow modes in dissipative many-body operator dynamics

Yang, T.-H., & Abanin, D. A. (2025). Integrals of motion as slow modes in dissipative many-body operator dynamics. *Physical Review B*, 112, 094304. doi:10.1103/d9b4-wlv6. Preprint: arXiv:2506.02970.

Read in full on 2026-11-02 ([NOTE-tmpxpf7y](../notes.d/NOTE-tmpxpf7y.md)).

## Key takeaways

- Under weak local noise, slowness ranks operators by how far they have
  spread. A conserved quantity on a few sites is slow because the
  Hamiltonian cannot spread it; the time-scale ratio between it and a
  generic operator is set by the system's own operator growth, not by the
  noise alone.
- The slowest Lindbladian eigenoperators of the chains studied are their
  small exact and approximate integrals of motion, so diagonalizing a
  weakly dissipative Lindbladian is a way to find conservation laws.
- Which quantities come out slowest depends on the noise strength: stronger
  noise promotes approximate conservation laws over exact but larger ones.

## Standing in the record

Filed for [CLAIM-478](../claims.d/CLAIM-478.md)'s list of the ways slowness arises, and for [CLAIM-331](../claims.d/CLAIM-331.md)
and [CLAIM-394](../claims.d/CLAIM-394.md) on what slowness picks out. It is the record's first work on
open quantum many-body dynamics. It carries no instruction for
machine-learning practice.
