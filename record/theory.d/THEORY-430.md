---
number: 430
status: Active
formerly:
- THEORY-tmp3t9ds
title: "A real hyperplane arrangement in ℝⁿ has (−1)ⁿχ(−1) regions and (−1)^rank χ(1) bounded regions, where χ is the characteristic polynomial of its intersection poset, so these counts depend only on which hyperplanes meet and in what dimension, not on the shapes of the regions"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-355
summary: >-
  Stanley (2006), [LIT-355](../literature.d/LIT-355.md), lecture notes read in full in [NOTE-313](../notes.d/NOTE-313.md), with
  Lectures 1–2 and 6 read closely. Zaslavsky's theorem (Thm 2.5) is proved
  twice, by a deletion–restriction recurrence and by Euler characteristic;
  the bounded-region half has two unanswered "[why?]" steps in the first
  proof and an omitted fact in the second. Faces of every dimension are
  counted by Möbius values (Thm 2.6). The notes never use "topes" or
  "covectors", and do not cite Zaslavsky's own texts. A region is fixed by
  its side of each hyperplane only implicitly (p. 89).
---

<!-- inactive-ok-file: LIT-332 LIT-359 — Unavailable; Zaslavsky's own texts, named as what the notes do not cite -->

# THEORY-430: A real hyperplane arrangement in ℝⁿ has (−1)ⁿχ(−1) regions and (−1)^rank χ(1) bounded regions, where χ is the characteristic polynomial of its intersection poset, so these counts depend only on which hyperplanes meet and in what dimension, not on the shapes of the regions

## Source

Stanley (2006), "An Introduction to Hyperplane Arrangements", PCMI lecture
notes (printed 2007), [LIT-355](../literature.d/LIT-355.md), read in full in [NOTE-313](../notes.d/NOTE-313.md) together with the
author's errata of 2020.

## What was actually shown

**The objects.** An arrangement is a finite set of affine hyperplanes in ℝⁿ.
Its regions are the connected components of the complement; each is open and
convex with a polyhedral closure (pp. 3–4). Its intersection poset L(A) is the
set of non-empty intersections ordered by reverse inclusion, graded by
codimension (Def. 1.1, Prop. 1.1). Its characteristic polynomial is
χ_A(t) = Σ_{x∈L(A)} μ(x) t^{dim x}, with μ the Möbius function (Def. 1.3).

**Zaslavsky's theorem (Thm 2.5).** r(A) = (−1)ⁿ χ_A(−1) and
b(A) = (−1)^{rank A} χ_A(1). The first proof is the recurrence
r(A) = r(A′) + r(A″) under deletion and restriction (Lemma 2.1, with the
errata's corrected Lemma 2.2). The second uses Euler characteristic and
Möbius inversion.

**What it implies (Cor. 2.1).** r(A) and b(A) depend only on L(A). Figure 2
gives two arrangements with the same L(A) and different face structure.

**All faces (Thm 2.6).** f_k(A) = Σ_{x≤y in L(A), dim x = k} |μ(x, y)|.

**Checks.** m lines in general position in ℝ² give C(m,2) + m + 1 regions
(Ex. 1.2). The braid arrangement x_i = x_j gives n! (Ex. 1.3). A graphical
arrangement's χ is the chromatic polynomial, so its regions number the
acyclic orientations (Thm 2.7, Cor. 2.3). The Shi arrangement has
(n + 1)^{n−1} regions (Thm 5.16, Cor. 5.11).

**Separating hyperplanes (§6.1, p. 89).** d(R, R′), the number of hyperplanes
separating two regions, is a metric on regions, said to be "easily seen".

**What could have come out otherwise.** Two arrangements with the same
intersection pattern but differently shaped regions could have had
different numbers of regions. They cannot.

## What this does not say

- **That regions are topes.** The notes never use oriented-matroid language.
  That a region is determined by its side of each hyperplane follows from
  d being a metric, which is [NOTE-313](../notes.d/NOTE-313.md)'s reading, not the notes' statement
  (C6). The theory of topes and covectors needs an oriented-matroid source
  the record does not hold.
- **That anything depending on region shape can be read from L(A).** Only
  counts can. A claim about "concept regions" that depends on their shape
  cannot be checked from the intersection lattice.
- **That the bounded-region formula is fully proved here.** The recurrence
  proof leaves two "[why?]" steps, and the topological proof omits ψ(Γ) = 1
  (p. 21; C3).
- **What Zaslavsky's own texts contain.** The notes attribute Thm 2.5 to him
  but do not cite [LIT-332](../literature.d/LIT-332.md) or [LIT-359](../literature.d/LIT-359.md).
- **That identifying ultrafilters of a Boolean algebra with regions is
  done.** That is the owner's own step ([NOTE-272](../notes.d/NOTE-272.md), [NOTE-290](../notes.d/NOTE-290.md)).

## Connections

- [THEORY-020](THEORY-020.md): Stone's representation gives a Boolean algebra's points as
  ultrafilters. Matching them to the regions of a generally non-orthogonal
  arrangement is the step the owner's map row 8 needs, and neither account
  supplies it.
