---
number: 320
status: Proposed
formerly:
- THEORY-tmpr8y66
promote_when: >-
  A check of the eigenvector computations in appendix B behind Theorems
  5.2–5.3 and Lemma 5.4, which this reading took at the level of their
  statements, together with a second example of the harm case outside the
  one-sample-per-kind toy: a population augmentation graph with several
  samples per kind, where adding a known class that shares a rival
  attribute measurably raises the novel labelling's residual
  ‖(I − P_{L♭})U♭ᵀy‖². It is refuted by an error in the C.1 identity, or
  by a graph satisfying the toy's τ ordering in which a rival-attribute
  known class does not demote the target eigenvector. What cannot settle
  it: clustering accuracies of trained networks on benchmarks, which
  measure the method, not the population residual.
title: "In a spectral contrastive graph that joins labelled known classes to unlabelled data, a novel labelling's linear-probe residual is exactly its part outside the top eigenspace that the labelled rows of the discarded eigenvectors cannot absorb, so which partition of the unlabelled data is discovered depends on the known classes: ones sharing the target's attribute can remove the residual, and ones sharing a rival attribute can raise it"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Carrying out the promotion audit's decision for THEORY-320 (batch 025,
    ADR-047). The exact residual identity is filed apart as
    THEORY-tmp9irmk, Active, re-derived in three steps (ADR-047 v2). This
    THEORY extends it and keeps the toy help-and-harm clauses, which rest
    on appendix B. A reconstruction of the toy from NOTE-833's description
    reproduced Theorem 5.2 and not Theorem 5.3 or Lemma 5.4 (note of
    2026-10-19 below). The status stays Proposed, and the promote_when is
    unchanged.
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-235
summary: >-
  Sun, Shi, Liang & Li (2023), [LIT-235](../literature.d/LIT-235.md), read in [NOTE-833](../notes.d/NOTE-833.md). On the
  population graph, at the exact rank-k optimum,
  R(U*, y) = ‖(I − P_{L♭})U♭ᵀy‖² (Theorem 5.5, stated as ≤, proved as =
  in C.1). In a one-sample-per-kind toy, a known class sharing colour
  makes a colour labelling recoverable, and one sharing shape makes it
  worse than none (Lemma 5.4). The general error bound (Theorem 5.6) is
  approximate and pools all known classes into one block, and is not
  part of this account. Nothing here is about trained networks.
answers:
- QUESTION-052
extends:
- THEORY-tmp9irmk
---
<!-- inactive-ok-file: THEORY-228 THEORY-005 — Proposed; the bound whose framework this extends, and an operator account it does not restate -->

# THEORY-320: In a spectral contrastive graph that joins labelled known classes to unlabelled data, a novel labelling's linear-probe residual is exactly its part outside the top eigenspace that the labelled rows of the discarded eigenvectors cannot absorb, so which partition of the unlabelled data is discovered depends on the known classes: ones sharing the target's attribute can remove the residual, and ones sharing a rival attribute can raise it

## Source

Sun, Shi, Liang & Li (2023), [LIT-235](../literature.d/LIT-235.md), read in [NOTE-833](../notes.d/NOTE-833.md): §4
(Eq. 1–4, Theorem 4.1), §5.1–5.3 (Lemma 5.1, Theorems 5.2, 5.3, 5.5,
Lemma 5.4), appendix A and appendix C.1.

## What was actually shown

**The graph.** Vertices are augmented views. The edge weight adds α
times the chance that x and x′ are views of two labelled samples of the
same known class to β times the chance that they are views of one
unlabelled image (Eq. 1). Labelled and unlabelled data meet only through
views they share. The rank-k factorization of the normalized adjacency
Ȧ is the minimizer of a contrastive loss with labelled same-class
positives (Theorem 4.1, an exact equivalence after HaoChen et al.).

**The residual identity (Theorem 5.5, proof in C.1).** Split the top-k
singular vectors into labelled rows L* and unlabelled rows U*, and the
rest into L♭ and U♭. Let the labelled entries of the target float. Then
the least-squares residual of a novel labelling y on U* is

R(U*, y) = min_ζ ‖L♭ᵀζ + U♭ᵀy‖² = ‖(I − P_{L♭})U♭ᵀy‖²,

with P_{L♭} = L♭ᵀ(L♭L♭ᵀ)†L♭. The theorem prints ≤; the proof's chain is
equalities. R = 0 iff some ω has u_iᵀy = l_iᵀω for every discarded i.
Through the eigen-equations, this is condition (23):
⟨yᵀ(σ_iI − A_uu)†A_ul, l_i⟩ = ⟨ω, l_i⟩ for all i > k. By Lemma 5.1, the
0–1 linear-probe error is at most 2R.

**Help and harm in a toy (§5.2).** The unlabelled set is a red cube, a
red sphere, a blue cube and a blue sphere, one sample each. The target
class is "red". Same-shape pairs are linked with probability τ_s and
same-colour pairs with τ_c. With τ_s > τ_c, shape dominates, and with no
informative known class the colour labelling has residual 1 (Theorem
5.2, gray cylinder). Adding a red cylinder makes it 0. Theorem 5.3
interpolates in the strength t of the known–novel link: residual 1 at
t = 0, in (0, 1) below a threshold t̄, 0 above it. Adding a gray cube,
which shares shape, makes the residual 1 higher than the gray-cylinder
case when τ_s/τ_c ∈ (1, 1.5) (Lemma 5.4).

What could have come out otherwise: the identity could have failed to
reduce to a projection, and the toy's rival-attribute case could have
left the residual unchanged.

## What this does not say

- **Nothing about trained networks.** The analysis is at the exact
  rank-k factorization of a population graph. The CIFAR experiments test
  NSCL as a method, and neither T(y) nor κ(y) is measured on them.
- **Not Theorem 5.6.** The paper's general bound in terms of "coverage"
  κ is approximate (≲). It replaces every labelled row by the mean over
  all labelled data, so the known classes act as one block with one
  direction. It has notational slips (|Y_u| redefined in Lemma C.6; T(y)
  against T(y)²). It is not filed here.
- **The harm result is a toy.** Lemma 5.4 is exact for one sample per
  kind with τ₁ = 1, τ₀ = 0 and 1 < τ_s/τ_c < 1.5. That rival-attribute
  known classes hurt in general is the paper's reading, not a theorem.
- **Not that labels carry information about novel classes.** The
  labelled data acts only by reshaping the graph's spectrum, through
  shared augmented views.
- **No instruction.** Which known classes to supply for discovery is a
  question of ML practice and belongs in the Anthology of the SOTA.

## Note of 2026-10-19: the toy could not be rebuilt from the record

For the promotion audit (batch 025), the toy graph was rebuilt from
[NOTE-833](../notes.d/NOTE-833.md)'s description and its residuals computed exactly:
- an unnormalized adjacency with 1 on the diagonal;
- τ_s between same-shape objects and τ_c between same-colour objects;
- the known class linked by its shared attribute;
- k = 3, with the labelled entry floating.

The reconstruction reproduces Theorem 5.2. With a gray cylinder the
residual is 1 when τ_s > τ_c and 0 when τ_s < τ_c. With a red cylinder it
is 0.

It does not reproduce Theorem 5.3. The residual falls from 1 to 0 for any
link t > 0, not at t̄. Nor does it reproduce Lemma 5.4. With a gray cube
and τ_s/τ_c ∈ (1, 1.5), the residual is 0, where the lemma has 2.

So the reconstruction is not the paper's set-up. One candidate is that
the labelled entry is fixed rather than floating in the toy. The help and
harm clauses can be checked only from appendix B, which the promote_when
already asks for. The identity itself is [THEORY-tmp9irmk](THEORY-tmp9irmk.md).

## Connections

- **answers [QUESTION-052](../questions.d/QUESTION-052.md), in part.** The question asks whether a kind's
  stable signature is the top eigenspace of its pair operator. This
  account shows the top eigenspace is not a property of the kind alone.
  Adding other kinds to the graph changes which attribute's partition
  ranks in the top k. A signature read off the spectrum is stable only
  relative to the rest of the operator.
- **[THEORY-228](THEORY-228.md)** (HaoChen's conductance bound) is the framework this
  extends. The two are compatible. [THEORY-228](THEORY-228.md) bounds the error through
  conductance and the label-change probability. This account gives the
  residual exactly through the discarded eigenvectors.
- **[CLAIM-152](../claims.d/CLAIM-152.md)** (individuation by sufficiency is relative to its target).
  This is a formal instance on the representation side. The same
  unlabelled data is partitioned by colour or by shape according to the
  auxiliary data, with no change to the unlabelled data itself.
- **[THEORY-005](THEORY-005.md), [THEORY-007](THEORY-007.md).** The operator accounts of spectral
  representations. This paper works on a finite graph and does not use
  their operator form.
