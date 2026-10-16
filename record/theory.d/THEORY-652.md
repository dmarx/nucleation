---
number: 652
status: Active
formerly:
- THEORY-tmpvk1js
title: "Over any field, a finite-dimensional associative algebra with no nilpotent two-sided ideal is uniquely a direct sum of simple algebras, and each simple algebra is a full matrix algebra over a division algebra, which over the reals can be the complex numbers or the quaternions"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-309
summary: >-
  Wedderburn (1908), [LIT-309](../literature.d/LIT-309.md), read in full in [NOTE-280](../notes.d/NOTE-280.md). Thm 17 with Thm
  10 gives the unique decomposition into simple algebras; Thms 20–22 build
  n² matrix units from primitive idempotents and give simple = primitive ×
  full matrix algebra. Primitive here means one idempotent, which makes the
  factor a division algebra once semisimple (Thm 15). The field is
  arbitrary, which was the paper's novelty. That the centre is spanned by
  the block identities follows from Thm 23's corollary; the paper never
  says "centre". The general splitting of an algebra into nilpotent plus
  semisimple parts is claimed in the summary but proved only in special
  cases.
---

<!-- inactive-ok-file: LIT-331 — Unavailable; named as the later generalisation, not read -->
<!-- inactive-ok-file: THEORY-019 — Proposed; named for the half of its promote_when this account supplies, not leaned on -->

# THEORY-652: Over any field, a finite-dimensional associative algebra with no nilpotent two-sided ideal is uniquely a direct sum of simple algebras, and each simple algebra is a full matrix algebra over a division algebra, which over the reals can be the complex numbers or the quaternions

## Source

Wedderburn (1908), "On hypercomplex numbers", *Proceedings of the London
Mathematical Society* (2) 6:77–118, [LIT-309](../literature.d/LIT-309.md), read in full in [NOTE-280](../notes.d/NOTE-280.md).

## What was actually shown

**The setting.** Associative algebras with a finite basis over a field F
that is "constant throughout but otherwise arbitrary" (§1). Semi-simple
means no nilpotent invariant sub-algebra, that is no nilpotent two-sided
ideal (§4).

**The radical (Thm 13).** A maximal nilpotent ideal N contains all others, so
A/N is semi-simple.

**Into simple blocks (Thms 10, 16, 17).** A semi-simple algebra has an
identity and, if not simple, splits along central idempotents. It is
therefore the direct sum A₁ + ⋯ + A_n of simple algebras with A_pA_q = 0 for
p ≠ q, uniquely.

**Each block is a matrix algebra (Thms 20–23).** In a simple algebra the
primitive idempotents e_p give Peirce pieces e_pAe_q with A_pqA_qr = A_pr
(Thm 20). Choosing x_pq with x_pqx_qp = e_p gives n² matrix units
e_pqe_qr = e_pr (Thm 21), and A is the direct product of the corner algebra
A₁₁ with the full matrix algebra (e_pq) (Thm 22). A₁₁ is primitive: it has
one idempotent, so every element is invertible or nilpotent (Thm 15), and
being semi-simple it is a division algebra. Conversely such a product is
simple, and only multiples of the identity commute with a full matrix
algebra (Thm 23 and corollary).

**Idempotents without field extension (Thm 14).** Every algebra that is not
nilpotent contains an idempotent rational in F. This is what replaces the
characteristic roots of Cartan's and Frobenius's methods, which needed ℂ or
ℝ.

**What could have come out otherwise.** Over a field that is not
algebraically closed the decomposition could have failed to exist or to be
unique. It does neither.

## What this does not say

- **That every block is a matrix algebra over the field.** The division
  factor can be non-trivial. Over ℝ it can be ℂ or ℍ, and the paper's own §11
  has a quaternion example. A real *-algebra's block can be M_n(ℂ) or M_n(ℍ),
  which [LIT-352](../literature.d/LIT-352.md)'s Theorem 3.1(C) forgets ([NOTE-280](../notes.d/NOTE-280.md)).
- **That the paper speaks of a centre or of isotypic components.** It works
  with algebras, not modules, and never uses the word "centre". That Z(A) is
  spanned by the block identities follows from Thm 23's corollary and the
  uniqueness of the blocks; "types = Z(𝒜)" is a modern gloss.
- **That every algebra is nilpotent plus semi-simple.** Summary (iii) claims
  it, citing Thms 24 and 28, which prove it only when A/N is simple or
  primitive. Thm 28's proof needed a correction added on 1 February 1908.
- **Anything beyond a finite basis.** The generalisation to rings with chain
  conditions is Artin's ([LIT-331](../literature.d/LIT-331.md)).
- **A classification of division algebras.** The paper concedes it leaves
  them unclassified (§6).

## Connections

- [THEORY-019](THEORY-019.md) needs the commutant of an isotypic component to be M_m(𝔽) with
  𝔽 = ℝ, ℂ or ℍ, and its `promote_when` asks for a held source that proves it.
  This theorem supplies the algebra-side half: every simple real block is a
  full matrix algebra over a real division algebra. That ℝ, ℂ and ℍ are the
  only real division algebras is Frobenius's theorem, which neither the paper
  nor the record holds. It does not supply the representation-side step,
  that the commutant of a representation is such a block.
- [LIT-313](../literature.d/LIT-313.md)'s Theorem 3, on simple weakly closed rings being factors, is the
  infinite-dimensional descendant of the trivial-centre corollary
  ([THEORY-592](THEORY-592.md)).
