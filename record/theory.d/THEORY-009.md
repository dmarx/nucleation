---
number: 9
status: Proposed
formerly:
- THEORY-tmpwf2pt
promote_when: >-
  A published analysis of an asymmetric self-supervised objective showing
  either that the eigenfunction characterization fails, or that it is replaced
  by singular functions of a non-self-adjoint operator. A further symmetric
  example cannot settle it. Near misses found on 2026-10-14: Balestriero &
  LeCun's Theorem 7 (NOTE-752) handles a non-symmetric pair structure by
  CCA, but the objective is Barlow Twins, not an asymmetric objective of the
  BYOL kind, and the CCA identification is asserted, not derived; Simon et
  al. (NOTE-741) treat two-tower pairs, but with a symmetrized loss.
  Neither meets it.
title: 'Spectral self-supervised learning gets its self-adjointness from the symmetry of the positive-pair distribution, not from the Riesz representation theorem'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-258 (NOTE-751), LIT-249
    (NOTE-740), LIT-242 (NOTE-741) and LIT-228 (NOTE-752).
    LIT-228's Theorem 7 is now cited as the nearest published case of a
    non-symmetric pair structure handled by a singular value decomposition,
    with its two caveats. LIT-242 is now said to get its symmetry from
    symmetrizing the loss, not from the pair distribution, with its CLIP-like
    two-tower case (§5.2). HaoChen et al. are said never to write
    "symmetric"; their symmetry comes from w(u,v) = w(v,u). Johnson et al.'s
    M is said to be the Gram matrix BᵀB, which needs both views drawn from
    the same p(A|Z). Neither paper mentions Riesz. promote_when keeps its
    clauses and records the near misses; it is not met. The stale Deferred
    comments on LIT-258 and LIT-249 removed.
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-258
- LIT-249
- LIT-252
- LIT-242
- LIT-228
- LIT-230
summary: >-
  An inference from how the spectral SSL papers ([LIT-258](../literature.d/LIT-258.md), [LIT-249](../literature.d/LIT-249.md),
  [LIT-252](../literature.d/LIT-252.md), [LIT-242](../literature.d/LIT-242.md)) obtain their eigenbases: each uses a symmetric pair
  matrix or kernel, and none invokes Riesz. In all but Simon et al., whose
  loss is symmetrized by hand, that symmetry is the symmetry of the
  positive-pair distribution. Answers the owner's "do we even need Riesz?"
  for this family of results.
extends:
- THEORY-007
answers:
- QUESTION-052
---
<!-- inactive-ok-file: LIT-261 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-260 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-252 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-009: Spectral self-supervised learning gets its self-adjointness from the symmetry of the positive-pair distribution, not from the Riesz representation theorem

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), App. C; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F; Pfau et al. (2019), [LIT-252](../literature.d/LIT-252.md), §5.2; Simon et al., [LIT-242](../literature.d/LIT-242.md), eq. 4 and §5.2; Balestriero & LeCun, [LIT-228](../literature.d/LIT-228.md), Theorem 7; the Riesz statement, [LIT-230](../literature.d/LIT-230.md).

## What was actually shown

Every spectral result in these papers rests on a symmetric operator. Johnson et al. use the symmetry of P_(A,A) to make D^(−½)P D^(−½) orthogonally diagonalizable, which yields the orthonormality all their theorems use (App. C). They call M "the symmetric matrix" without argument; it is symmetric, and positive semidefinite, because the proof of Thm 3.2 writes it as a Gram matrix BᵀB, which holds because both views are drawn independently from the same p(A|Z). HaoChen et al. apply the spectral theorem to a square-integrable kernel k(u,v) = w(u,v)/√(w(u)w(v)) (App. F). They never write "symmetric": the symmetry follows from w(u,v) = w(v,u), which holds because both views come from the same A(·|x̄), and they use it throughout the finite case as well. Pfau et al. note that reversible dynamics make "the transition function … a symmetric operator" (§5.2). Simon et al. symmetrize by hand, Γ = (1/2n)Σ(x_i x_i′ᵀ + x_i′ x_iᵀ) (eq. 4); there the symmetry comes from symmetrizing the loss, not from the pair distribution, and they apply the same Γ to CLIP-like two-tower pairs (§5.2), where there is no single space and no symmetric pair distribution. Neither Johnson et al. nor HaoChen et al. mention Riesz. For finite matrices and integral operators the adjoint is the transpose, written down directly; Riesz is what defines the adjoint of a general bounded operator ([LIT-230](../literature.d/LIT-230.md)).

The representer theorem is a parallel case: Schölkopf, Herbrich & Smola's proof ([LIT-261](../literature.d/LIT-261.md), eqs. 18–24) uses the reproducing property and orthogonal projection, not Riesz.

## What this does not say

- That Riesz is irrelevant. It is what makes an abstract space of functions with bounded evaluation into an RKHS, and it is what makes a kernel mean embedding exist (see the mean-embedding claim, from Muandet et al., [LIT-260](../literature.d/LIT-260.md), Lemma 3.1).
- What happens for non-reversible pair structures: predictors and stop-gradient (BYOL, SimSiam), directed augmentations, cross-modal pairs. There the natural object would be the singular value decomposition of a non-self-adjoint operator, which needs the adjoint in earnest. No account for an asymmetric objective was found. The nearest is Balestriero & LeCun's Theorem 7 ([LIT-228](../literature.d/LIT-228.md)): in the linear regime Barlow Twins recovers CCA, the singular value decomposition of the non-self-adjoint whitened cross-covariance, and a symmetric pair matrix G is what yields weight sharing; the paper says G's symmetry "is often not required". But the objective is Barlow Twins, not a BYOL-type asymmetric one, and the identification with CCA is asserted rather than derived. In Simon et al.'s two-tower case the symmetric Γ is block off-diagonal in the cross-covariance, so its eigenvalues are ± that matrix's singular values; that reading (the Jordan–Wielandt construction) is the record's, not the paper's.
