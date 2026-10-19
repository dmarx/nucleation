---
number: 737
status: Active
formerly:
- THEORY-tmp9irmk
title: 'In a spectral contrastive graph that joins labelled known classes to unlabelled data, the least-squares residual of a novel labelling on the top-k eigenspace, with the labelled entries left free, equals exactly the part of the labelling outside that eigenspace that the labelled rows of the discarded eigenvectors cannot absorb'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-320 and filed Active, carrying out the promotion
    audit's decision for THEORY-320 (batch 025, ADR-047 v2). THEORY-320's
    title joins this exact identity to toy results that rest on an
    appendix the record has not read. NOTE-833 read the identity's proof
    in C.1, and the three-step derivation below re-derives it. THEORY-320
    keeps the toy clauses and extends this entry.
tags:
- representation-learning
- learning-theory
date: '2026-10-19'
source:
- LIT-235
summary: >-
  Sun, Shi, Liang & Li (2023), [LIT-235](../literature.d/LIT-235.md), Theorem 5.5 with its proof in
  C.1, read in [NOTE-833](../notes.d/NOTE-833.md). The paper states the identity as ≤, and its proof
  is a chain of equalities. Re-derived here in three steps from
  orthogonality and least squares. With the paper's Lemma 5.1 it bounds
  the novel labelling's 0–1 linear-probe error by twice this residual. It
  is about the exact rank-k factorization of a population graph, not
  about trained networks.
extended_by:
- THEORY-320
---
<!-- inactive-ok-file: THEORY-320 THEORY-228 — Proposed; the toy help-and-harm account this was split from and that extends it, and the conductance bound whose graph this uses, cited as open -->

# THEORY-737: In a spectral contrastive graph that joins labelled known classes to unlabelled data, the least-squares residual of a novel labelling on the top-k eigenspace, with the labelled entries left free, equals exactly the part of the labelling outside that eigenspace that the labelled rows of the discarded eigenvectors cannot absorb

## Source

Sun, Shi, Liang & Li (2023), [LIT-235](../literature.d/LIT-235.md), §4 (the graph, Eq. 1), §5.3
(Theorem 5.5) and appendix C.1, read in [NOTE-833](../notes.d/NOTE-833.md).

## What was actually shown

**The setting.** Vertices are augmented views. Edges join views of
labelled samples of one known class and views of one unlabelled image
(Eq. 1). Let V = [F G] be an orthogonal matrix whose first k columns F
are the top-k singular vectors of the normalized adjacency. Split the
rows into labelled and unlabelled: F = [L*; U*] and G = [L♭; U♭]. For a
novel labelling y of the unlabelled vertices, let the labelled entries of
the target float:

R(U*, y) = min over w, z of ‖F w − [z; y]‖².

**The identity, re-derived.**

1. For a fixed target t = [z; y], min_w ‖F w − t‖² = ‖(I − FFᵀ)t‖² =
   ‖Gᵀt‖², because F has orthonormal columns and FFᵀ + GGᵀ = I.
2. Gᵀt = L♭ᵀz + U♭ᵀy.
3. Minimizing ‖L♭ᵀz + U♭ᵀy‖² over z is least squares. Its value is
   ‖(I − P_{L♭})U♭ᵀy‖², where P_{L♭} = L♭ᵀ(L♭L♭ᵀ)†L♭ projects onto the
   range of L♭ᵀ.

So R(U*, y) = ‖(I − P_{L♭})U♭ᵀy‖², an equality. The residual is zero iff
U♭ᵀy lies in the range of L♭ᵀ, that is, iff some ω has u_iᵀy = l_iᵀω for
every discarded i. By the paper's Lemma 5.1, the 0–1 linear-probe error
on the unlabelled data is at most 2R.

What could have come out otherwise: the residual could have depended on
the top-k rows of the labelled data, or have been only bounded by the
projection. It is exactly the projection.

## What this does not say

- **Nothing about trained networks.** The identity holds at the exact
  rank-k factorization of the population graph.
- **Not the toy results.** That a known class sharing the target's
  attribute removes the residual, and that one sharing a rival attribute
  raises it, are [THEORY-320](THEORY-320.md)'s claims. They rest on eigenvector
  computations in an appendix the record has not read.
- **Not Theorem 5.6.** The paper's approximate coverage bound is not part
  of this.

## Connections

- **[THEORY-320](THEORY-320.md)** extends this. It adds the paper's toy demonstrations of
  help and harm, and keeps them Proposed.
- **[THEORY-228](THEORY-228.md)** (HaoChen's conductance bound) is the framework the graph
  comes from. This gives the residual exactly, through the discarded
  eigenvectors.
