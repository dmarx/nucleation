---
number: 378
status: Active
formerly:
- CLAIM-tmp67453
title: 'A representational similarity index invariant to every invertible linear map depends on a representation only through its column space, so it takes one value on all column-centred representations of rank n − 1, as it does on all representations of rank n'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed Active at the owner's direction, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/THEORY-236.yaml,
    batch 006, ADR-047). THEORY-236's promote_when asked for a written
    version of Kornblith et al.'s Theorem 1 for column-centred
    representations. The version written here is more general: any two
    representations with the same column space are related by an invertible
    linear map. It is the record's own, so it is a CLAIM (ADR-032).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: two n × p matrices with the same column
  space that no invertible p × p matrix maps one onto the other.
tags:
- mathematics
- representation-learning
date: '2026-10-19'
line: formal-apparatus
grounds:
- LIT-254
summary: >-
  The generalization of [THEORY-236](../theory.d/THEORY-236.md)'s theorem. If col(X) = col(Y), write
  X = BC and Y = BD with B a basis of the common column space and C, D of
  full row rank, extend C and D to invertible matrices, and the quotient
  maps X onto Y. Since XA always has the column space of X, the GL(p)
  orbits are exactly the sets of n × p matrices sharing a column space.
  Theorem 1 is the case of column space ℝⁿ. Column-centred matrices of
  rank n − 1 all have column space 1^⊥, so an invariant index cannot tell
  them apart either.
---

# CLAIM-378: A representational similarity index invariant to every invertible linear map depends on a representation only through its column space, so it takes one value on all column-centred representations of rank n − 1, as it does on all representations of rank n

## The claim

Let X and Y be n × p representations of the same n examples, and let s be
an index with s(X, Z) = s(XA, Z) for every invertible p × p matrix A. If
col(X) = col(Y), then s(X, Z) = s(Y, Z). So s(·, Z) is a function of the
column space alone.

## Proof

Let W = col(X) = col(Y), of dimension r ≤ p, and let B be an n × r matrix
whose columns are a basis of W. Then X = BC and Y = BD for r × p matrices C
and D. Each has rank r, because rank(X) = r and rank(BC) ≤ rank(C) ≤ r.
Extend the r independent rows of C by p − r further rows E to an
invertible p × p matrix C′ = [C; E], and likewise D′ = [D; F]. Put
A = C′⁻¹D′, which is invertible. Then C′A = D′, whose first r rows give
CA = D. So XA = BCA = BD = Y, and s(Y, Z) = s(XA, Z) = s(X, Z).

Conversely, col(XA) = col(X) for every invertible A, so the orbit of X under
GL(p) is exactly the set of n × p matrices with column space W.

**Two cases.** If r = n, then W = ℝⁿ, which is Kornblith et al.'s Theorem 1
([THEORY-236](../theory.d/THEORY-236.md)). If the columns are centred, every column is orthogonal to the
all-ones vector 1, so col(X) ⊆ 1^⊥. At rank n − 1 it equals 1^⊥, for every
such X. So an invariant index takes one value on all centred representations
of rank n − 1, given Z.

## What it does not say

- **Anything below the maximal rank.** There an invariant index can
  separate representations, but only by their column spaces.
- **Which group a comparison should use.** That is [THEORY-236](../theory.d/THEORY-236.md)'s caveat, and
  it is empirical.
