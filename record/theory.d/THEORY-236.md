---
number: 236
status: Proposed
formerly:
- THEORY-tmpuowt1
promote_when: >-
  An independent statement of the result in the literature, or a second
  reader's line-by-line check of the App. A proof together with a written
  version for column-centred representations, whose rank is at most n − 1
  so that the theorem's hypothesis rank = n is never met by them. It is
  refuted by a similarity index invariant to all invertible linear maps
  that distinguishes two representations of full row rank on the same
  examples. What cannot settle it: experiments showing that CCA-family
  indexes fail sanity checks, which bear on which index to prefer, not on
  whether this degeneracy holds.
title: "A representational similarity index that is invariant to every invertible linear map takes the same value on all representations whose rank equals the number of examples"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-254
summary: >-
  Kornblith, Norouzi, Lee & Hinton (2019), [LIT-254](../literature.d/LIT-254.md), Theorem 1, read in
  [NOTE-743](../notes.d/NOTE-743.md). If s(X, Z) = s(XA, Z) for every invertible A, and
  rank(X) = rank(Y) = n, then s(X, Z) = s(Y, Z): any two full-row-rank
  representations of the same n examples are related by an invertible
  linear map. So when width reaches the number of examples, an index with
  that invariance, such as CCA, says nothing. The theorem fixes no group;
  the paper's case for orthogonal invariance plus isotropic scaling is an
  argument from training dynamics, not a consequence of it.
---
<!-- inactive-ok-file: THEORY-002 THEORY-008 CLAIM-193 — Proposed; cited for context, nothing here rests on them -->

# THEORY-236: A representational similarity index that is invariant to every invertible linear map takes the same value on all representations whose rank equals the number of examples

## Source

Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), read in [NOTE-743](../notes.d/NOTE-743.md): §2.1–2.3,
Theorem 1 and its proof (App. A), Proposition 1 (App. B).

## What was actually shown

**Theorem 1.** Let X and Y be n × p representations of the same n examples
with rank(X) = rank(Y) = n, which needs p ≥ n. If an index satisfies
s(X, Z) = s(XA, Z) for every full-rank A, then s(X, Z) = s(Y, Z). The
proof stacks X and Y with bases of their row null spaces to get
invertible X′ and Y′, and sets A = X′⁻¹Y′, so that XA = Y. Any two such
representations are one orbit of GL(p), and an invariant index is constant
on it.

**Two companions.**
- An index invariant to orthogonal maps and to non-isotropic scaling is
  invariant to every invertible linear map, by the SVD (§2.3). So the group
  cannot be widened from orthogonal maps by per-axis rescaling without
  inheriting the degeneracy.
- Proposition 1: an orthogonally invariant index applied to orthonormalized
  columns, s(Q_X, Q_Y), is invariant to invertible linear maps. This is how
  CCA acquires the invariance.

What could have failed: an invariant index could have kept some
information about how two full-rank representations are placed relative
to the examples. It cannot, because the group acts transitively on them.

**A precision of the record's.** The paper centres columns. A centred
n × p matrix has rank at most n − 1, so centred representations never meet
the hypothesis rank = n as written. The same construction should go
through at rank n − 1, since two centred full-rank representations share
the column space orthogonal to the all-ones vector. That is the record's
inference, not a statement of the paper, and it is what promote_when asks
to have written out.

## What this does not say

- **Not which group is right.** The theorem says only that GL(p) is too
  large once p ≥ n. The case for orthogonal maps plus isotropic scaling
  (§2.2) rests on permutation symmetry, on a linear-case result about
  gradient descent and on rotationally symmetric initialization. The case
  against GL(p) is empirical (Fig. 1). Neither is a theorem.
- **Not that such indexes are blank below full rank.** When the rank is
  below n, an invertible-linear-invariant index can distinguish
  representations, but only through their column spaces, since XA has the
  column space of X.
- **Not that CKA is the right index.** CKA's success on the sanity check
  (Table 2) is a separate, empirical finding.

## Connections

- **[THEORY-018](THEORY-018.md) and [THEORY-002](THEORY-002.md).** Softmax training identifies the final
  representation only up to an invertible linear map. This theorem is the
  other side of that: a comparison invariant to everything the distribution
  leaves free is uninformative once the representation is wide enough.
  Comparisons must either fix a smaller group by stipulation, which is
  [THEORY-018](THEORY-018.md)'s point about inner products, or move to identified
  coordinates, as Nielsen et al. do ([LIT-253](../literature.d/LIT-253.md)).
- **[THEORY-004](THEORY-004.md).** Orthogonal invariance is what a centred kernel leaves
  free. This theorem gives the reason a kernel comparison is not traded for
  an invertible-linear one.
- **[CLAIM-193](../claims.d/CLAIM-193.md).** That kernels fix a representation only up to the symmetry
  of what is observed is safe from this degeneracy only when that symmetry
  is smaller than GL(p) or the rank is below n.
- **[THEORY-008](THEORY-008.md).** Kornblith et al. also show that R²_CCA, linear regression
  and linear CKA are one family, differing in eigenvalue weighting
  (Eqs. 11–14). That result is held there, as the precursor of the
  readout account.
