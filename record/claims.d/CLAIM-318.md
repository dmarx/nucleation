---
number: 318
status: Active
formerly:
- CLAIM-tmp6eegl
title: 'Within a shared observational scenario, exact structure-preserving symmetries are the invertible members of a nested family of stochastic transports, and among Markov kernels between finite sets the invertible ones are the permutation matrices, so the invertible core is the relabellings, a groupoid in which objects joined by an arrow have isomorphic automorphism groups'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stochastic matrix between finite sets whose
  inverse is also stochastic and which is not a permutation matrix, or an
  invertible arrow between two objects whose automorphism groups are not
  isomorphic. The claim is a derivation, so only an error in it defeats it;
  a finding that symmetries are of little use in assessing lossy
  transports does not.
tags:
- mathematics
date: '2026-10-15'
line: pragmatic-transport
complements:
- CLAIM-098
summary: >-
  Split from [CLAIM-103](CLAIM-103.md) under [ADR-043](../decisions.d/ADR-043.md): the nesting and its invertible core,
  stated on their own so that their warrant can be. A110 §25 nests exact
  symmetries inside structure-compatible transports inside stochastic
  communicative transports, within a shared scenario, and the exact
  symmetries are the invertible ones. For Markov kernels between finite
  sets, a stochastic matrix with a stochastic inverse is a permutation
  matrix, because a nonnegative matrix with a nonnegative inverse is
  monomial, so the invertible core is the relabellings. In that groupoid an
  invertible u : A → B gives Aut(A) ≅ Aut(B), which corrects A198 §8. It
  does not say what symmetries are for: that they supply the yardstick for
  non-symmetric transports is [CLAIM-103](CLAIM-103.md)'s, and interpretive.
supports:
- CLAIM-103
---
<!-- inactive-ok-file: CLAIM-098 CLAIM-103 — Proposed; the semigroup claim this complements and the claim this was split from, cited as open -->

# CLAIM-318: Within a shared observational scenario, exact structure-preserving symmetries are the invertible members of a nested family of stochastic transports, and among Markov kernels between finite sets the invertible ones are the permutation matrices, so the invertible core is the relabellings, a groupoid in which objects joined by an arrow have isomorphic automorphism groups

## The claim

This is the nesting [CLAIM-103](CLAIM-103.md) states, with the qualification its note of
2026-10-10 adds, filed on its own so that its warrant can be. A110 §25:
"Stochastic communicative transports ⊃ Structure-compatible transports ⊃
Exact structure-preserving symmetries. The last inclusion should be read
within an appropriately shared observational scenario: exact symmetries
are generally invertible automorphisms, whereas structure-compatible
transports need not be." [CLAIM-098](CLAIM-098.md) holds the coarser form from the
manuscript §4: "The more inclusive notion is a category or semigroup of
stochastic transformations, within which invertible symmetry maps are
special cases."

The invertible core is small. A198 §9 puts the exact symmetries in "a
larger category of communicative transports, whose invertible
subcategory forms a groupoid". For Markov kernels between finite sets, a
stochastic matrix whose inverse is also stochastic is a permutation
matrix, because a nonnegative matrix with a nonnegative inverse is
monomial. So among stochastic maps on finite observation spaces the
invertible core is the relabellings, and the only characters it carries
are permutation characters, which count fixed points.

In that groupoid, objects joined by an arrow have isomorphic automorphism
groups. An invertible u : A → B induces an isomorphism Aut(A) ≅ Aut(B), by
g ↦ ugu⁻¹. Objects with non-isomorphic automorphism groups lie in different
connected components of a groupoid and are joined by no arrow. A198 §8's
"Different objects can have different automorphism groups, while still
being related by isomorphisms" is therefore false.

## What it does not say

- It does not say what symmetries are for. That their main use is to
  supply the invariants against which non-symmetric transports are
  assessed is [CLAIM-103](CLAIM-103.md)'s conclusion, and it is interpretive.
- It does not define the middle term. "Structure-compatible transports"
  are placed between the two by A110 §25; this claim fixes only the
  innermost term and the outermost one.
- It does not cover kernels on infinite spaces, where the derivation given
  here, by monomial matrices, does not apply as stated.
