---
number: 645
status: Active
formerly:
- THEORY-tmpupzrd
title: "A countable discrete abelian group and a compact second-countable abelian group can each be recovered as the character group of the other, and a locally compact, connected, second-countable abelian group is a compact group plus ℝʳ; Pontryagin's 1934 paper does not prove duality for general locally compact abelian groups"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-333
summary: >-
  Pontryagin (1934), [LIT-333](../literature.d/LIT-333.md), read in full in [NOTE-284](../notes.d/NOTE-284.md). Theorem 5 and the
  First Fundamental Theorem give the duality between countable discrete
  and compact second-countable abelian groups, with characters valued in
  ℝ/ℤ. The compact half rests on Peter–Weyl with Haar measure, used to
  extract one-dimensional characters. The Second and Third Fundamental
  Theorems are structure theorems, not duality. Commutative only; for
  non-abelian groups the relevant object is Peter–Weyl, and characters are
  traces, not homomorphisms. General locally compact duality is van
  Kampen's (1935).
---

<!-- inactive-ok-file: THEORY-019 THEORY-022 — Proposed; named in Connections, not leaned on -->

# THEORY-645: A countable discrete abelian group and a compact second-countable abelian group can each be recovered as the character group of the other, and a locally compact, connected, second-countable abelian group is a compact group plus ℝʳ; Pontryagin's 1934 paper does not prove duality for general locally compact abelian groups

## Source

Pontrjagin (1934), "The theory of topological commutative groups", *Annals
of Mathematics* 35(2):361–388, [LIT-333](../literature.d/LIT-333.md), read in full in [NOTE-284](../notes.d/NOTE-284.md).

## What was actually shown

**Characters.** For a discrete abelian group 𝔊, its character group X is the
set of homomorphisms 𝔊 → K = ℝ/ℤ, with pointwise convergence. For a
countable 𝔊, X is compact and second countable (Thm 1). Subgroups and
quotients correspond through annihilators (Thms 2–4). If X and 𝔊 form an
orthogonal couple, a continuous pairing into K with trivial annihilators,
each is the character group of the other (Thm 5).

**The First Fundamental Theorem (p. 372).** "Let Ω be a continuous compact
commutative group satisfying the second axiom of countability, and 𝔊 the
discrete group of its characters, then the group Ω is isomorphic to the group
of characters of 𝔊." The proof takes Peter–Weyl's separating family of
orthogonal representations, available via Haar measure, simultaneously
diagonalises the commuting matrices to get one-dimensional characters that
separate points (Lemmas 9–10), and applies Theorem 5.

**Structure (Second and Third Fundamental Theorems).** A locally compact,
connected, second-countable abelian group is a compact subgroup, uniquely
determined, plus a vector group ℝʳ with r an invariant (p. 377). If it is
also locally connected, it is a sum of countably many circles and a vector
group (p. 380).

**The dictionary (Appendices 1–2).** Direct-sum decompositions correspond
under duality. X is connected iff 𝔊 is torsion-free, dim X = rank 𝔊, and X is
zero-dimensional iff 𝔊 is torsion. Example 2, a rank-2 torsion-free
indecomposable group, refutes a published decomposition claim of van
Dantzig.

**What could have come out otherwise.** A compact abelian group could have
had too few characters to be recovered from them. Peter–Weyl rules that
out.

## What this does not say

- **Duality for general locally compact abelian groups.** Chapters III–IV
  treat structure, not duality. Each locally compact abelian group being the
  dual of its dual, ℝ included, came with van Kampen (1935).
- **Anything without second countability.** Remark 2 notes one lemma extends
  to uncountable groups; the theorems are stated with countability.
- **Anything for non-abelian groups.** There the relevant object is
  Peter–Weyl ([LIT-329](../literature.d/LIT-329.md)), and characters are traces, not homomorphisms
  ([NOTE-284](../notes.d/NOTE-284.md)).
- **That the finite case is used.** Remark 3 notes that a finite abelian
  group is isomorphic to its dual, a "well-known fact" the paper does not use.
- **That Gelfand, Stone and Pontryagin form one duality.** The paper draws no
  connection to Stone or to operator algebras.

## Connections

- [THEORY-620](THEORY-620.md): the Walsh system is the character group of the compact
  group (ℤ/2)^ℕ, whose dual is the countable discrete group ⊕ℤ/2, a case of
  the First Fundamental Theorem with zero-dimensional X and torsion 𝔊. Walsh
  did not see it, and neither paper mentions the other.
- [THEORY-022](THEORY-022.md) reads the grokking network's computation as products of
  characters of ℤ/p, the finite case of this duality.
- [THEORY-019](THEORY-019.md): commuting operators force degeneracy along real irreducibles;
  for abelian groups over ℂ these are the one-dimensional characters
  extracted here, and over ℝ they pair up.
- [THEORY-592](THEORY-592.md) and [THEORY-020](THEORY-020.md) are the Gelfand and Stone legs of the
  owner's "duality tripod".
