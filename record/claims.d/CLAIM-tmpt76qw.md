---
status: Active
title: 'Comparing characters across realizations needs one group identified on both, which is fixed only up to automorphism, and automorphisms permute the irreducible characters, so "the same character" is relative to a chosen correspondence: the collapse problem again, at the level of the symmetry group'
version: 1
role: granted
tags:
- mathematics
- individuation
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-011
- CLAIM-132
- CLAIM-098
objects_to:
- CLAIM-137
uses:
- TERM-041
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. To say a visual realization has the
  same character as a spoken one, the same group element must be named on
  both sides. Changing that identification by an automorphism α turns χ
  into χ∘α, and for the cyclic group of order 3 the automorphism g ↦ g²
  swaps the two nontrivial characters. The transformations the line
  studies form a semigroup, so the group is a symmetry group the analyst
  chooses, with its action on each medium fixed independently: [CLAIM-011](CLAIM-011.md)'s
  anchoring once more. Granted, because the argument is elementary.
  [CLAIM-132](CLAIM-132.md) and [TERM-041](../terms.d/TERM-041.md) hold neighbouring limits, not this one.
illustrated_by:
- CASE-tmp4iy8h
---
<!-- inactive-ok-file: CLAIM-137 — Proposed; the owner's thesis, open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-098 CLAIM-103 — Proposed; cited for the semigroup of transformations and the invertible core of stochastic maps, open -->
<!-- inactive-ok-file: CLAIM-138 — Proposed; the Newman counter this objection complements, open -->

# CLAIM-tmpt76qw: Comparing characters across realizations needs one group identified on both, which is fixed only up to automorphism, and automorphisms permute the irreducible characters, so "the same character" is relative to a chosen correspondence: the collapse problem again, at the level of the symmetry group

## The objection

[CLAIM-137](CLAIM-137.md) makes the spoken, translated and visual realizations of a
teasing remark "like one representation written in different
coordinates", with a shared character-like invariant as what makes them
one act. A character is a function on a group. To compare χ_A on a spoken
realization with χ_B on a visual one, the same group element g has to be
named on both sides: one group G acts on both media, and some
transformation of the image is identified as the transformation g of the
speech.

**The identification is fixed only up to automorphism.** Change it by an
automorphism α of G, and the character read off becomes χ∘α. Inner
automorphisms change nothing, because a character is a class function
([CLAIM-132](CLAIM-132.md), item 1). Other automorphisms can move characters.

A worked case. Let G = {1, g, g²} be the cyclic group of order 3, and
ω = e^(2πi/3). Its two nontrivial irreducible characters are
χ₁(g^k) = ω^k and χ₂(g^k) = ω^(2k). The map α(g) = g² is an automorphism.
G is abelian, so its only inner automorphism is the identity, and α is
not inner. Then

χ₁(α(g^k)) = χ₁(g^(2k)) = ω^(2k) = χ₂(g^k).

So α swaps χ₁ and χ₂. A realization identified with G one way "has" χ₁,
and identified the other way "has" χ₂. The realization does not fix which.
The same happens in any group with an automorphism that moves a character:
in an abelian group, inversion sends each character χ to its complex
conjugate, which differs from χ whenever χ takes a non-real value.

**Which group?** The transformations the line studies are not group
elements. [CLAIM-098](CLAIM-098.md): "The more inclusive notion is a category or semigroup
of stochastic transformations, within which invertible symmetry maps are
special cases." [CLAIM-103](CLAIM-103.md)'s note adds that "A stochastic matrix whose
inverse is also stochastic is a permutation matrix", so among stochastic
maps on finite observation spaces the invertible core is the relabellings.
So G has to be a symmetry group of the situation that the analyst chooses,
such as [CLAIM-132](CLAIM-132.md)'s swap of the two participants, with its action on each
medium specified independently. That is [CLAIM-011](CLAIM-011.md)'s requirement of an
anchored correspondence, and [CLAIM-138](CLAIM-138.md)'s Newman point, once more, now at
the level of the symmetry group.

**For semigroups, traces say less.** For representations of a monoid,
traces fix at most the semisimplification. [CLAIM-132](CLAIM-132.md)'s example, read as
an action of the monoid ℕ, shows it: n ↦ [[1, n], [0, 1]] and the trivial
action on ℂ² both have trace 2 for every n, and they are not isomorphic.

**What the record holds nearby.** [CLAIM-132](CLAIM-132.md)'s title says characters "fix
neither the group nor a permutation action", and its approximate bound
"needs an invertible S between representations of one group, which is not
the translation case". [TERM-041](../terms.d/TERM-041.md) says the signature is "Not yet built".
Neither names the identification of G across realizations, or the
automorphism ambiguity of that identification.

## What it does not say

- It does not say the character analogy is useless. Within one medium, or
  once the identification of G across media is fixed independently,
  characters are a complete invariant in characteristic zero ([CLAIM-132](CLAIM-132.md)).
- It does not say the ambiguity always bites. The cyclic group of order 2
  has no nontrivial automorphism, so [CLAIM-132](CLAIM-132.md)'s worked model of the swap is
  unaffected. The ambiguity bites for groups with automorphisms that move
  characters.
- It complements [CLAIM-138](CLAIM-138.md), which makes the same point for relations in
  general.
