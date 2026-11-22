---
status: Read
paper: LIT-2244
title: 'Augustsson and colleagues 2026, read for how adaptive coupling makes and remakes a split between synchronized and desynchronized groups of identical oscillators'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-094 from the arXiv preprint
    (arxiv.org/pdf/2608.20517v1, a 6-page letter with references, 10 pp.
    in all), text extracted with pdftotext. The letter read in full,
    figure captions read, figures not viewed; the Supplementary Material
    (the master stability analysis, further regimes, Fig. S1–S2) is not in
    the preprint file and was not read. Quotations rechecked by script
    against the downloaded text. Read by the lead worker itself. No email
    address sent.
date: '2026-11-22'
summary: >-
  N = 100 identical Kuramoto oscillators with phase lag, coupled through a
  product-form weight wₖₗ = ηₖζₗ whose factors adapt slowly (ε = 0.01) to
  the global order parameter. From random starts the population splits
  into a synchronized cluster and a desynchronized group, an "adaptive
  chimera", with no group structure imposed. Along a branch of fixed
  cluster fraction ρ the desynchronized group passes from stationary to
  breathing to chaotic; each branch ends when some desynchronized units
  join the cluster, a crisis-like jump to a new branch. The landscape is
  highly multistable and path-dependent. The reading is THEORY-tmpq02z9.
---
<!-- inactive-ok-file: THEORY-tmpq02z9 — Proposed; this reading's account -->
<!-- inactive-ok-file: CLAIM-478 — Proposed; a claim the reading bears on -->

# NOTE-tmp3oxzv: Augustsson and colleagues 2026, read for how adaptive coupling makes and remakes a split between synchronized and desynchronized groups of identical oscillators

## Contribution

A minimal adaptive network in which chimera states self-organize, and a
bifurcation structure that repeats on each branch of fixed cluster
fraction. The reading is THEORY-tmpq02z9.

## Key results

1. **Self-organized split** (abstract): "The system spontaneously
   self-organizes into adaptive chimera states, where identical
   oscillators separate into synchronized and desynchronized groups
   through adaptive weight dynamics." Against the classical case, where
   chimeras came "with a predefined subpopulation structure imprinted in
   the coupling strengths" (p. 1).
2. **Slow adaptation, fixed** (p. 2): "We set ϵ = 0.01 for slow
   adaptation"; ε is not varied.
3. **Exact reductions on invariant cluster subspaces** (p. 2–3):
   permutation symmetry makes every cluster subspace invariant; the
   two-cluster dynamics closes on six variables with ρ as a parameter
   (eqs. 10–11); the synchronized state loses transverse stability at a
   cluster-branching point given in closed form (eq. 9).
4. **A persistent partition through changing dynamics** (p. 5): "within
   each fixed-ρ branch, the system passes through the same sequence of
   dynamical regimes without any reconfiguration of which units belong to
   the synchronized versus desynchronized populations", by a
   quasiperiodic route to chaos (Lyapunov exponents, Fig. 4b).
5. **Reorganization** (p. 5): "Each branch terminates when a subset of
   desynchronized oscillators synchronizes with the coherent cluster,
   abruptly increasing ρ and establishing a new chimera branch—a
   transition reminiscent of a crisis."
6. **History** (p. 6): "the specific sequence of cluster sizes depends on
   the initial conditions and the direction of the parameter sweep"; the
   authors suggest such networks "can retain information about their
   dynamical history".

## Assumptions

Identical oscillators, global coupling of product form, slow adaptation
(ε = 0.01), N = 100, one parameter (β_in) swept by quasi-continuation.

## Concepts

Adaptive chimera; cluster subspace (invariant by permutation symmetry);
transverse stability; cluster-branching point; fixed-ρ branch;
crisis-like reorganization.

## Bearing on the record

- **QUESTION-281** (bears on). A worked case of distinctions coming into
  being and passing away: the split into groups arises at a transverse
  instability of synchrony (eq. 9), persists through a sequence of
  bifurcations of the desynchronized group's dynamics, and is remade by
  crisis-like jumps. The group's membership survives changes of its
  dynamics, which bears on the question's separation of a form's creation
  from its stabilization.
- **CLAIM-478** (note only). The slow weights carry the partition, and
  the fast phases stay organized by it along a branch, which has the
  claim's shape; but the separation is imposed (ε fixed at 0.01), not
  made or varied, so it is not evidence for the mechanism.
- **CLAIM-172** (note only). The synchronized cluster is a group of
  mutually entrained peers formed from a population with no imposed
  groups; the claim's sufficiency is not tested.
- **Ott and Antonsen's reduction** (NOTE-tmpd7trg). The paper's own
  reductions are exact closures on invariant subspaces given by
  permutation symmetry, finite-N, not the Ott–Antonsen manifold.

## Limitations

- One parameter swept, one ε, one N; stability boundaries of the chimeras
  are not determined, by the authors' account, because of multistability.
- The supplementary analyses are not read here.
- The mechanism that homogenizes the desynchronized units' mean
  frequencies is described, not derived.
