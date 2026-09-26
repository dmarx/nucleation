---
number: 9
status: Proposed
formerly:
- THEORY-tmpwf2pt
promote_when: >-
  A published analysis of an asymmetric self-supervised objective showing
  either that the eigenfunction characterization fails, or that it is replaced
  by singular functions of a non-self-adjoint operator. A further symmetric
  example cannot settle it.
title: 'Spectral self-supervised learning gets its self-adjointness from the symmetry of the positive-pair distribution, not from the Riesz representation theorem'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-258
- LIT-249
- LIT-252
- LIT-242
- LIT-230
summary: >-
  An inference from how the spectral SSL papers ([LIT-258](../literature.d/LIT-258.md), [LIT-249](../literature.d/LIT-249.md),
  [LIT-252](../literature.d/LIT-252.md), [LIT-242](../literature.d/LIT-242.md)) obtain their eigenbases: each uses a symmetric pair
  matrix or kernel, and none invokes Riesz. Answers the owner's "do we even
  need Riesz?" for this family of results.
extends:
- THEORY-007
---
<!-- inactive-ok-file: LIT-261 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-260 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-252 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-258 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-249 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-009: Spectral self-supervised learning gets its self-adjointness from the symmetry of the positive-pair distribution, not from the Riesz representation theorem

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), App. C; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F; Pfau et al. (2019), [LIT-252](../literature.d/LIT-252.md), §5.2; Simon et al., [LIT-242](../literature.d/LIT-242.md), eq. 4; the Riesz statement, [LIT-230](../literature.d/LIT-230.md).

## What was actually shown

Every spectral result in these papers rests on a symmetric operator. Johnson et al. use the symmetry of P_(A,A) to make D^(−½)P D^(−½) orthogonally diagonalizable, which yields the orthonormality all their theorems use (App. C). HaoChen et al. use a symmetric square-integrable kernel to apply the spectral theorem (App. F). Pfau et al. note that reversible dynamics make "the transition function … a symmetric operator" (§5.2). Simon et al. symmetrize by hand, Γ = (1/2n)Σ(x_i x_i′ᵀ + x_i′ x_iᵀ) (eq. 4). For finite matrices and integral operators the adjoint is the transpose, written down directly; Riesz is what defines the adjoint of a general bounded operator ([LIT-230](../literature.d/LIT-230.md)).

The representer theorem is a parallel case: Schölkopf, Herbrich & Smola's proof ([LIT-261](../literature.d/LIT-261.md), eqs. 18–24) uses the reproducing property and orthogonal projection, not Riesz.

## What this does not say

- That Riesz is irrelevant. It is what makes an abstract space of functions with bounded evaluation into an RKHS, and it is what makes a kernel mean embedding exist (see the mean-embedding claim, from Muandet et al., [LIT-260](../literature.d/LIT-260.md), Lemma 3.1).
- What happens for non-reversible pair structures: predictors and stop-gradient (BYOL, SimSiam), directed augmentations, cross-modal pairs. There the natural object would be the singular value decomposition of a non-self-adjoint operator, which needs the adjoint in earnest; no such account was found.
