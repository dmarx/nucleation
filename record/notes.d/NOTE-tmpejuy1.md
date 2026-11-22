---
status: Skimmed
paper: LIT-2239
title: 'Battiston, Bick, Lucas, Millán, Skardal and Zhang — Collective dynamics on higher-order networks'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-023 from the arXiv copy (2510.05253v2,
    19 March 2026, 17 pages): the abstract and introduction, the
    phase-reduction box and §III B on how nonpairwise phase interactions
    arise, the opening of §IV (reduction and reconstruction from data),
    the topological Kuramoto subsection and the Outlook read; the sections
    on contagion, explosive transitions and inference methods read for
    their headings only. Quotations checked by script.
date: '2026-11-22'
summary: >-
  A review of collective dynamics, mainly synchronization, on hypergraphs
  and simplicial complexes. Points read: nonpairwise phase interactions can
  arise by phase reduction from pairwise physical coupling, so the order of
  the physical and of the effective interactions can differ; in the
  topological Kuramoto model harmonic modes localize on holes, so
  synchronization depends on the complex's topology; frustration enters
  through phase lags; and when higher-order terms are necessary is an open
  question.
---

# NOTE-tmpejuy1: Battiston, Bick, Lucas, Millán, Skardal and Zhang — Collective dynamics on higher-order networks

## Contribution

A Nature Reviews Physics overview of how nonpairwise interactions change
collective dynamics, with the methods (phase reduction, Ott–Antonsen and
Watanabe–Strogatz reductions, multi-order Laplacians) and open problems.

## Key results (parts read)

1. **Effective order differs from physical order (§III B).** "even when
   the coupling terms in Gi are pairwise, one may expect nonpairwise
   interactions to enter the phase dynamics at higher-order expansions";
   "the emergent nonpairwise interactions capture indirect interactions
   between oscillators (e.g., that oscillator i receives input from
   oscillator k via j independent of any direct interaction between i and
   k)." Hence, in reconstruction, "whether one reconstructs physical
   interactions or effective phase interactions" (§IV).
2. **Topological Kuramoto (§III).** Divergence-free and curl-free parts
   evolve independently and "harmonic modes remain stationary"; "Phase
   coupling is thus possible only when the harmonic part of the natural
   frequencies vanishes and the harmonic eigenvectors localize along
   topological holes in the complex". "Frustration may also be introduced
   via the simplicial Sakaguchi-Kuramoto model [201] by adding phase lags."
3. **Open (Outlook).** "it is critical to understand when higher-order
   interactions are necessary", and "one needs to identify equivalences
   between different combinatorial models for network interactions".

## Assumptions

Mostly phase oscillators; hypergraphs or simplicial complexes as given
structures; the review reports others' results.

## Concepts

Higher-order (nonpairwise) interaction; hypergraph; simplicial complex;
phase reduction at higher order; topological (simplicial) Kuramoto model;
Hodge Laplacian and harmonic modes; Dirac operator; multistability.

## Bearing on the record

- **CLAIM-153** (background). The frustrated simplicial model with phase
  lags, which the review names, is the higher-order form of this claim's
  frustrated XY energy; harmonic modes on holes are where the cycle
  conditions of Bačić and colleagues (THEORY-tmpcdxvd) live.
- **CLAIM-480** (a parallel). Its last clause, that a reduced constraint
  can relate three boundary values where every relation among the parts is
  pairwise, has a dynamical counterpart here: eliminating amplitudes by
  phase reduction turns pairwise physical coupling into effective triplet
  and quadruplet phase interactions.

## Limitations

Skimmed; a review, whose claims rest on cited work not checked here.
