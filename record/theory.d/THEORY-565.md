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
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-16'
source:
- LIT-981
answers:
- QUESTION-052
summary: >-
  Coifman et al. (2005), [LIT-981](../literature.d/LIT-981.md), skimmed in [NOTE-784](../notes.d/NOTE-784.md) from extracted text
  whose displayed equations were not visible. The construction and the
  embedding are standard. The convergence theorem and the α-family are
  stated without proof, which is deferred to a companion paper. [NOTE-784](../notes.d/NOTE-784.md)
  filed no THEORY for those reasons. It is filed Proposed on the owner's
  ruling that a well-established result may rest on a skim when it is not
  wrong as stated. Self-adjointness comes from the kernel's symmetry, and
  the paper's "directed diffusion" is anisotropic, not a non-reversible
  chain.
---

<!-- inactive-ok-file: NOTE-784 — Skimmed; the reading this account rests on, which is why it is Proposed -->
<!-- inactive-ok-file: THEORY-009 THEORY-228 THEORY-239 — Proposed; named in Connections for comparison, not leaned on -->

# THEORY-565: From a symmetric, positivity-preserving, positive semi-definite affinity, the normalized Markov operator is conjugate to a symmetric one, so its leading eigenfunctions scaled by powers of their eigenvalues embed the data with Euclidean distance equal to diffusion distance, and a density-corrected normalization recovers the Laplace–Beltrami operator independently of how the data were sampled

## Source

Coifman, Lafon, Lee, Maggioni, Nadler, Warner & Zucker (2005), "Geometric
diffusions as a tool for harmonic analysis and structure definition of
data: Diffusion maps", *PNAS* 102(21):7426–7431, [LIT-981](../literature.d/LIT-981.md), skimmed in
[NOTE-784](../notes.d/NOTE-784.md). Every section's prose, the theorem's statement and the figure
captions were read; the displayed equations were images that could not be
seen, so no expression here is quoted from the paper.

## What was actually shown

**The construction.** The kernel k is required to be symmetric, positivity
preserving and positive semi-definite. It is renormalized into a Markov
kernel a(x, y), read as a random walker's step probability. a is not
symmetric, but its conjugate ã is, which gives a spectral decomposition
1 = λ₀ ≥ λ₁ ≥ ⋯. Powers of the operator give the m-step walk.

**The embedding.** Mapping each point to its eigenfunction values scaled by
λ^m makes Euclidean distance equal the diffusion distance at time m: the
distance between the m-step transition distributions from two points,
weighted by the inverse stationary density (the standard definition; the
paper's formula was not seen). Truncating to the eigenfunctions above a
precision threshold is approximately isometric for m beyond some m₀.

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
  to Coifman and Lafon's companion paper, which the record does not hold.
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
