---
number: 84
status: Proposed
formerly:
- THEORY-tmpjae36
promote_when: >-
  A numerical check, plus a held source for the perturbation step. Compute
  the Gauss–Newton spectrum of wide fully connected ReLU networks (two
  layers and at least three) under squared loss on uniform data on
  S^(d−1), at initialisation and after training in the lazy regime. Look
  for plateaus of N(d, k) near-equal eigenvalues at heights proportional
  to µ_k, ordered by height. Then resample the data and measure principal
  angles between the subspaces kept by thresholds at several positions.
  The account is promoted if thresholds inside a plateau keep subspaces
  that change from sample to sample while thresholds at gaps keep stable
  ones, with stability tracking the gap as Cao et al.'s eigengap condition
  suggests. A held statement of a Davis–Kahan-type bound would replace
  the filer's appeal to it. The account is refuted if no plateaus appear at
  widths where the lazy approximation otherwise holds. It is also refuted
  if thresholds inside a plateau keep stable subspaces, which would mean
  the splitting within a block is systematic rather than sampling noise.
  Spectra of classifiers trained with cross-entropy (LIT-613) cannot
  settle it, since that is a different matrix in a different regime.
title: "Because the Gauss–Newton Fisher JᵀJ and the NTK Gram matrix JJᵀ share their non-zero spectrum, the lazy-regime Fisher of a ReLU network on spherical data inherits the NTK's harmonic-degree blocks, and a spectral threshold on it is well posed only at gaps between blocks"
version: 2
history:
- version: 2
  date: '2026-10-05'
  note: >-
    `extends: THEORY-086` re-filed as `presupposes: THEORY-086` (ADR-029).
    The NTK eigenstructure is taken as given for a claim about Fisher
    thresholds. `extends: THEORY-019` is unchanged: this account works the
    near-degenerate case that account leaves open.
tags:
- information-geometry
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-03'
source:
- LIT-608
- LIT-624
- LIT-612
extends:
- THEORY-019
summary: >-
  The filer's synthesis, stated by no source. The identity is linear
  algebra: JᵀJ (parameters × parameters) and JJᵀ (samples × samples) have
  the same non-zero eigenvalues. Under squared loss JᵀJ is the Gauss–Newton
  matrix and the Fisher. JJᵀ is the empirical NTK Gram matrix, which in
  the kernel regime on uniform spherical data has the degree-block
  spectrum of Bietti & Bach (2021), [LIT-608](../literature.d/LIT-608.md): µ_k with multiplicity
  N(d, k). The threshold claim draws on Cao et al. (2019), [LIT-624](../literature.d/LIT-624.md).
  Their guarantees are stated only for whole eigenspaces, with sample costs
  that grow as the gap below them shrinks. It also draws on Basri et al.
  (2019), [LIT-612](../literature.d/LIT-612.md), where a structural zero block shows up in a
  finite sample as small non-zero eigenvalues. No paper filed computes a
  Fisher spectrum in this regime.
presupposes:
- THEORY-086
---
<!-- inactive-ok-file: THEORY-019 THEORY-078 THEORY-080 — Proposed; THEORY-019 is extended and this account is no firmer than it, the others are named in Connections -->

# THEORY-084: Because the Gauss–Newton Fisher JᵀJ and the NTK Gram matrix JJᵀ share their non-zero spectrum, the lazy-regime Fisher of a ReLU network on spherical data inherits the NTK's harmonic-degree blocks, and a spectral threshold on it is well posed only at gaps between blocks

## Source

- Bietti & Bach (2021), [LIT-608](../literature.d/LIT-608.md), read in [NOTE-475](../notes.d/NOTE-475.md): Eq. 8
  (degree blocks and their multiplicities) and Corollary 3 (k^(−d) decay at
  every depth).
- Cao et al. (2019), [LIT-624](../literature.d/LIT-624.md), read in [NOTE-483](../notes.d/NOTE-483.md): Lemma 4.1
  (sampled eigenfunctions are nearly orthonormal) and Theorem 4.2
  (guarantees for whole eigenspaces, with an eigengap condition).
- Basri et al. (2019), [LIT-612](../literature.d/LIT-612.md), read in [NOTE-481](../notes.d/NOTE-481.md): Theorem 4 and
  Figure 4 (the bias-free zero block, seen in a finite sample).

## The argument

**Step 1, linear algebra.** Let J be the n × p matrix whose rows are the
gradients of the network output at the n training inputs. For any matrix,
JᵀJ and JJᵀ have the same non-zero eigenvalues with the same
multiplicities. Under squared loss, the likelihood is Gaussian with noise
precision β. The Gauss–Newton matrix is then βJᵀJ, and it is the Fisher
information. JJᵀ is the empirical NTK Gram matrix, K_ij = ∇f(x_i)·∇f(x_j).
So the non-zero Fisher spectrum is the empirical NTK spectrum times β. This
step needs no source. [NOTE-475](../notes.d/NOTE-475.md) records it as a fact of linear
algebra and not a claim of [LIT-608](../literature.d/LIT-608.md).

**Step 2, from the sources.** In the kernel regime the empirical NTK stays
close to its infinite-width limit. On uniform data on S^(d−1), that
limit's integral operator has one eigenvalue µ_k per harmonic degree, with
multiplicity N(d, k) ([LIT-608](../literature.d/LIT-608.md), Eq. 8). Its non-zero µ_k decay as
k^(−d) at every depth (Corollary 3). The sampled eigenfunctions are nearly
orthonormal, ‖V_{r_k}ᵀV_{r_k} − I‖_max ≤ CM²√(log(r_k/δ)/n) ([LIT-624](../literature.d/LIT-624.md),
Lemma 4.1). So the leading eigenvalues of the Gram matrix are close to
nµ_k, in groups of N(d, k).

**Together.** The lazy-regime Fisher of such a network should show
plateaus of N(d, k) near-equal eigenvalues at heights near βnµ_k, ordered
by height, with a null space of dimension at least p − n.

**Step 3, thresholds.** Within a degree block the population eigenvalues
are exactly equal. In a sample they are split by an amount that shrinks
with n. A threshold that falls inside a block keeps an arbitrary,
sample-dependent subspace of an eigenspace that has no preferred basis.
[THEORY-019](THEORY-019.md) says that the basis inside a multiplet is invisible to the
spectrum. A threshold that falls in a gap keeps the span of every harmonic
up to some degree, which is a stable object. Cao et al.'s guarantee has
this shape. It is stated only for the first r_k eigenfunctions, a set
closed under multiplicity, and its sample requirement grows as
(λ_{r_k} − λ_{r_k+1})^(−2) (Theorem 4.2). Basri et al. add a warning
([LIT-612](../literature.d/LIT-612.md), Figure 4). The bias-free two-layer kernel's odd-degree block has
eigenvalue exactly zero, yet in a finite sample it appears as the smallest
non-zero eigenvalues. A threshold would remove those directions for the
right reason without being able to tell them from directions the data
merely under-determine. That the stability of a kept subspace is governed
by the gap is a Davis–Kahan-type statement. The record holds no source
for it, so this step is the filer's.

## What this does not say

- **It does not cover cross-entropy.** There the Gauss–Newton matrix is
  JᵀΛJ, with Λ the softmax Hessian, and the identity holds for Λ^{1/2}J
  instead. Papyan's class-structured Fisher spectra ([THEORY-078](THEORY-078.md)) are
  that case, outside the lazy regime. They show a different block
  structure, indexed by class rather than by degree.
- **It does not say the blocks survive feature learning.** Whether a
  trained network outside the lazy regime keeps any trace of the degree
  blocks is the comparison this account would make possible. It does not
  answer it.
- **The ordering is by height, not degree.** The constants in Corollary 3
  depend on parity, so two adjacent degrees may swap. Gaps between degrees
  also shrink as k grows, so for high degrees the blocks blur together at
  any finite n.
- **No source states it.** Bietti & Bach say nothing about Fisher
  matrices, thresholds or evidence. Cao et al. say nothing about the
  Fisher. Each step is checkable, but the combination is the filer's.

## Connections

- **Presupposes [THEORY-086](THEORY-086.md).** That account gives the NTK's eigenstructure
  and its role in training dynamics. This one carries the same blocks
  into the Fisher and asks what a threshold on them can mean.
- **Extends [THEORY-019](THEORY-019.md).** That account leaves near-degeneracy and the
  thresholds a test would need open. This one takes the case of a
  symmetry-forced block split by sampling noise, and says where a
  threshold is well posed.
- **[THEORY-080](THEORY-080.md)** uses the same spectrum to compute an Occam factor.
  There, directions inside a block are priced equally, so no threshold is
  needed.
