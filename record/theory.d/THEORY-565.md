---
number: 565
status: Proposed
formerly:
- THEORY-tmpk9r9m
promote_when: >-
  A Read NOTE on a copy of the paper whose equations can be read, together
  with Coifman and Lafon's companion paper, that follows the proofs of the
  heat-kernel convergence theorem (Thm 2.1) and of the α-family of
  normalizations, and states their sampling conditions. The account is
  promoted if the α = 1 normalization converges to the Laplace–Beltrami
  operator with no dependence on the sampling density, under conditions
  that can be stated; it is refuted in part if the limit keeps a density
  term. More embeddings that look right, or classification examples, cannot
  settle it.
title: "From a symmetric, positivity-preserving, positive semi-definite affinity, the normalized Markov operator is conjugate to a symmetric one, so its leading eigenfunctions scaled by powers of their eigenvalues embed the data with Euclidean distance equal to diffusion distance, and a density-corrected normalization recovers the Laplace–Beltrami operator independently of how the data were sampled"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-565.yaml, batch 010, ADR-047),
    the finite-data construction and its isometry are filed apart as
    THEORY-728, Active, with the derivation written out (ADR-047 v2).
    This THEORY extends it and keeps the α-family and Theorem 2.1. Its
    promote_when already concerned only those and is unchanged. The claim
    is unchanged, and the status stays Proposed.
- version: 3
  date: '2026-10-30'
  note: >-
    The twenty-first status review, at the status review's ruling (the
    owner delegated these rulings). LIT-981 is read in full with every
    equation seen (NOTE-1441), and the text is corrected from it
    (ADR-047 kind 3). (1) It gave the diffusion distance as "the distance
    between the m-step transition distributions from two points, weighted
    by the inverse stationary density (the standard definition; the
    paper's formula was not seen)"; the paper defines it as the distance
    the symmetric kernel ã^(m) induces, which is the companion's and
    THEORY-728's weighted distance only after each coordinate is
    rescaled. (2) It said truncation "is approximately isometric for m
    beyond some m₀"; the paper claims a relative error 1 + O(e^{−αm}),
    the form THEORY-745 shows wrong for nearby points. (3) It said the
    companion paper is one "which the record does not hold"; it is
    LIT-1246, read in NOTE-985 on 2026-10-20. It now extends THEORY-744,
    the Active α-family limit. The title and status are unchanged.
tags:
- mathematics
- representation-learning
date: '2026-10-16'
source:
- LIT-981
extends:
- THEORY-728
- THEORY-744
summary: >-
  Coifman et al. (2005), [LIT-981](../literature.d/LIT-981.md), read in full in [NOTE-1441](../notes.d/NOTE-1441.md). The
  finite construction and its isometry are [THEORY-728](THEORY-728.md); the paper's own
  diffusion distance is the one ã^(m) induces, not the
  inverse-stationary-weighted one. Theorem 2.1 and the α-family are
  stated without proof; the companion ([LIT-1246](../literature.d/LIT-1246.md), [NOTE-985](../notes.d/NOTE-985.md)) proves the
  α-family's limit, Active without boundary as [THEORY-744](THEORY-744.md), and its
  heat-kernel step is [QUESTION-231](../questions.d/QUESTION-231.md). Self-adjointness comes from the
  kernel's symmetry, and "directed diffusion" is anisotropic, not a
  non-reversible chain.
bears_on:
- QUESTION-052
---

<!-- inactive-ok-file: NOTE-784 QUESTION-231 — Superseded or Open; the skim this was first filed from, and the open heat-kernel step -->

# THEORY-565: From a symmetric, positivity-preserving, positive semi-definite affinity, the normalized Markov operator is conjugate to a symmetric one, so its leading eigenfunctions scaled by powers of their eigenvalues embed the data with Euclidean distance equal to diffusion distance, and a density-corrected normalization recovers the Laplace–Beltrami operator independently of how the data were sampled

## Source

Coifman, Lafon, Lee, Maggioni, Nadler, Warner & Zucker (2005), "Geometric
diffusions as a tool for harmonic analysis and structure definition of
data: Diffusion maps", *PNAS* 102(21):7426–7431, [LIT-981](../literature.d/LIT-981.md), read in full
in [NOTE-1441](../notes.d/NOTE-1441.md) (2026-10-30) with every displayed equation seen; it
replaces the skim of [NOTE-784](../notes.d/NOTE-784.md). The proofs it defers are in Coifman and
Lafon's companion, [LIT-1246](../literature.d/LIT-1246.md), read in [NOTE-985](../notes.d/NOTE-985.md).

## What was actually shown

**The construction.** The kernel k is required to be symmetric, positivity
preserving and positive semi-definite. It is renormalized into a Markov
kernel a(x, y), read as a random walker's step probability. a is not
symmetric, but its conjugate ã is, which gives a spectral decomposition
1 = λ₀ ≥ λ₁ ≥ ⋯. Powers of the operator give the m-step walk.

**The embedding.** The paper writes ã's eigenvalues as λ_i², so
ã^(m)(x, y) = Σ λ_i^{2m} φ_i(x) φ_i(y), and defines
D_m²(x, y) = ã^(m)(x, x) + ã^(m)(y, y) − 2ã^(m)(x, y) (p. 7427).
Φ_m(x) = (λ_i^m φ_i(x)) is then an exact isometry for D_m, being the
kernel's feature map. This is not the inverse-stationary-weighted distance
between m-step transition rows, which is the companion's ([LIT-1246](../literature.d/LIT-1246.md)) and
[THEORY-728](THEORY-728.md)'s; the two differ by rescaling each coordinate by the square
root of the stationary density, and each has its own exact isometry. The
paper claims that the first j₀ coordinates keep D_m to a relative factor
1 + O(e^{−αm}), with no proof; [THEORY-745](THEORY-745.md) shows the relative form fails for
nearby points in the companion's coordinates, where only an absolute bound
holds.

**The α-family.** α = 0 gives the normalized graph Laplacian, α = 1/2 the
backward Fokker–Planck operator, and α = 1 the Laplace–Beltrami operator,
on which "the density plays no role". Theorem 2.1 states that, for data on
or near a compact submanifold, the density-corrected kernel converges as
ε → 0 to the Laplace–Beltrami heat kernel, with error of order ε^{1/2} on
bandlimited functions. Neither is proved in the paper.

**What could have come out otherwise.** Without the symmetric conjugate, the
walk's operator need have no real orthogonal eigenbasis, and the embedding
would not be defined. The paper does not consider that case.

## What this does not say

- **That the theorem is proved here.** Thm 2.1 and the α-family are deferred
  to the companion ([LIT-1246](../literature.d/LIT-1246.md), [NOTE-985](../notes.d/NOTE-985.md)). There the α-family's limit is
  proved, Active without boundary as [THEORY-744](THEORY-744.md); the heat-kernel limit's
  semigroup step does not follow as written, and the boundary rate is
  slower than printed ([QUESTION-231](../questions.d/QUESTION-231.md)).
- **Anything for non-symmetric kernels.** "Directed diffusion" means
  diffusion along the level sets of a given function through an anisotropic
  distance; the kernel stays a symmetric affinity. A non-reversible walk is
  not treated.
- **How many eigenfunctions to keep.** It is set by a precision threshold,
  not by any task.
- **That the classification example is evidence of accuracy.** The
  hyperspectral result is a specialist's judgement, with no accuracies.
- **The sampling conditions of convergence.** "Relatively densely sampled"
  is not quantified in the text.

## Connections

- [QUESTION-052](../questions.d/QUESTION-052.md) asks whether the top eigenspace of a pair operator is a
  stable, decision-sufficient signature, and what replaces it for directed
  pairs. This is its symmetric case: the eigenspace exists because the
  kernel is symmetric, and the α = 1 normalization makes it insensitive to
  how densely each region was sampled, one sense of "stable". It does not
  reach the directed half, and gives no decision guarantee; [THEORY-228](THEORY-228.md) and
  [THEORY-239](THEORY-239.md) give those for linear probes.
- [THEORY-009](THEORY-009.md) holds that self-adjointness in spectral self-supervised
  learning comes from the symmetry of the pair distribution, not from the
  Riesz theorem. Here too it comes from k(x, y) = k(y, x), checked directly.
- [LIT-975](../literature.d/LIT-975.md) (§5.3) identifies the kernel metric of its power kernels with this
  diffusion distance ([THEORY-239](THEORY-239.md) is filed from it).
- [QUESTION-027](../questions.d/QUESTION-027.md)'s "stable" might require the α = 1 property; its exact
  conditions are not stated in this paper.

## Note of 2026-10-19: the finite construction filed apart

The construction and the embedding, as far as they hold on a finite data
set, are now [THEORY-728](THEORY-728.md), Active, with the derivation the paper's
unseen equations left out: the symmetric conjugate, the spectral form of
the walk, and the exact isometry for the 1/π-weighted diffusion distance.
What keeps this THEORY Proposed is only the analytic half, the α-family
and the Laplace–Beltrami limit of Theorem 2.1, whose proofs are in a
companion paper the record does not hold.

## Note of 2026-10-30: what holds it back

Its promote_when asks that the proof of Theorem 2.1, the heat-kernel limit,
be followed. The companion's proof ([LIT-1246](../literature.d/LIT-1246.md), Proposition 11) has a
semigroup step that does not follow as written, and its rate with boundary
is slower than printed, which is [QUESTION-231](../questions.d/QUESTION-231.md), Open; the α-family's
generator limit is held without boundary by [THEORY-744](THEORY-744.md). The paper, now read
in full ([NOTE-1441](../notes.d/NOTE-1441.md)), proves neither.
