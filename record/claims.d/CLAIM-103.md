---
number: 103
status: Proposed
formerly:
- CLAIM-tmptzrxc
title: 'Symmetry is not opposed to transport: exact symmetries are the invertible core of a nested family of transports, and their main use is to supply the invariants against which non-symmetric transports are assessed'
version: 1
role: thesis
defeated_if: >-
  The invariants of exact symmetries of a scenario fail to discriminate
  between good and bad lossy transports of it as judges rank them.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
rests_on:
- CLAIM-113
summary: >-
  A110 §25, recovered. The manuscript §4 keeps "invertible symmetry maps
  are special cases" and drops the nesting and the yardstick role,
  apparently by inadvertence.
---
<!-- inactive-ok-file: CLAIM-113 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-103: Symmetry is not opposed to transport: exact symmetries are the invertible core of a nested family of transports, and their main use is to supply the invariants against which non-symmetric transports are assessed

## The claim

A110 §25: "Stochastic communicative transports ⊃ Structure-compatible transports ⊃
Exact structure-preserving symmetries. The last inclusion should be read within
an appropriately shared observational scenario: exact symmetries are generally
invertible automorphisms, whereas structure-compatible transports need not be.
Thus symmetry is not opposed to transport. **Symmetry identifies special
transport operations and, more importantly, the invariants against which other
transports can be assessed.**"

## Where it went

Manuscript §4: "The more inclusive notion is a category or semigroup of stochastic
transformations, within which invertible symmetry maps are special cases." The
second half, that symmetry gives the measuring stick for transports that are not
symmetries, is the bridge the manuscript lacks between its §4 symmetry and its §6
functional ([TERM-036](../terms.d/TERM-036.md)). It is the owner's U37 point carried through ([CLAIM-113](CLAIM-113.md)).

## Note of 2026-10-10: restored, and the invertible core of stochastic maps

The nesting was restored after the manuscript dropped it: at A178 ("Exact
symmetries as special transport cases"), at A203 §20, which displays the
chain exact symmetry ⊂ structure-preserving transport ⊂ general directed
stochastic transport, and at A218 Ch11.10 ("Exact equivalences as a special
case of a broader transport theory"). A203 §20 also keeps the yardstick role: "symmetries identify
invariants against which more general transformations can be evaluated."

A qualification, from A198 §§8–9 and checked by reasoning. A198 §9 puts the
exact symmetries in "a larger category of communicative transports, whose
invertible subcategory forms a groupoid". For Markov kernels between finite
sets that subcategory is small. A stochastic matrix whose inverse is also
stochastic is a permutation matrix, because a nonnegative matrix with a
nonnegative inverse is monomial. So among stochastic maps on finite
observation spaces the invertible core is the relabellings, and the only
characters it carries are permutation characters, which count fixed points.
The nesting stands. Its innermost term is narrower than A198 suggests.

A198 §8 also says: "Different objects can have different automorphism groups,
while still being related by isomorphisms." That is false. An invertible
u : A → B induces an isomorphism Aut(A) ≅ Aut(B), by g ↦ ugu⁻¹. Objects with
non-isomorphic automorphism groups lie in different connected components of a
groupoid and are joined by no arrow.
