---
status: Proposed
title: 'The character of a perspective''s representation detects the transformations it is blind to, not the states it merges: its kernel is the observational invariance subgroup when the projection is equivariant and its image spans, but a projection can merge states no transformation relates while its character shows no blindness at all'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the example below, for a finite group G
  acting on world states X, a projection h_P from X to the points of a
  finite set Y_P, and the permutation representation of G on Y_P, as A6
  §3 sets them up. Not defeated by another choice of representation: the
  claim is about the one A6 describes.
tags:
- mathematics
- epistemology
date: '2026-11-24'
line:
- formal-apparatus
- organizational-normativity
rests_on:
- CLAIM-350
- CLAIM-132
complements:
- CLAIM-tmpjlxfy
uses:
- TERM-tmp9mag8
summary: >-
  A gap fill (ADR-137) for A6 §3 of the exchange "Memes, Contracts, and
  Systemic Normativity" (ChatGPT, 2026-11-24), which defines the
  observational invariance subgroup K_P of a perspective's projection h_P,
  says the kernel of a representation ρ_P "Under suitable conditions ...
  corresponds to the observational invariance subgroup", and calls this
  "a candidate formal apparatus for studying **characteristic
  blindness**". The conditions are stated, the kernel is read off the
  character, and an example shows the character missing merged states;
  checked by script (python3 -I). The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: TERM-tmp9mag8 — Proposed, Deferred or Rejected; entries filed from the exchange 'Memes, Contracts, and Systemic Normativity' and held entries it is read against, cited whatever their standing -->

# CLAIM-tmpqbaic: The character of a perspective's representation detects the transformations it is blind to, not the states it merges: its kernel is the observational invariance subgroup when the projection is equivariant and its image spans, but a projection can merge states no transformation relates while its character shows no blindness at all

## The gap

A6 §3 takes a projection h_P : X → Y_P, whose fibres are "distinctions
that the perspective cannot make", and, for a group G of transformations
of world states, K_P = {g ∈ G : h_P(gx) = h_P(x) for all x}, "transformations
to which the projection is insensitive". If G acts on the representational
space by ρ_P, "The kernel of this representation describes
transformations that act trivially on the entire representational space.
Under suitable conditions, it corresponds to the observational invariance
subgroup. This gives us a candidate formal apparatus for studying
**characteristic blindness**." The conditions are not given, nor how much
of the blindness the fibres locate this apparatus captures.

## The derivation

1. **The conditions.** Let h_P be equivariant, h_P(gx) = ρ_P(g)h_P(x), and
   let its image span Y_P (for a permutation action on a finite Y_P: be
   onto). Then g ∈ K_P iff ρ_P(g) fixes every h_P(x), iff ρ_P(g) is the
   identity, so K_P = ker ρ_P. Without equivariance K_P need not be a
   subgroup that ρ_P sees at all.
2. **The kernel is in the character.** For a finite group and a complex
   representation, ρ_P(g) is diagonalizable with eigenvalues roots of
   unity, so |χ_P(g)| ≤ χ_P(e) = dim, with χ_P(g) = χ_P(e) exactly when
   every eigenvalue is 1, that is when ρ_P(g) = I. So
   K_P = {g : χ_P(g) = χ_P(e)}: the character does detect this blindness.
3. **It is not the fibres.** Every K_P-orbit lies in a fibre of h_P, but a
   fibre can merge states that no element of G relates. Example:
   X = {a, a′, b, b′}, G = {e, s} with s swapping a ↔ b and a′ ↔ b′.
   - h₁ sends a, a′ to y₁ and b, b′ to y₂, with s swapping y₁ and y₂. It is
     equivariant and onto; K = {e}; the permutation character is
     (χ(e), χ(s)) = (2, 0). The character shows no blindness, yet h₁ merges
     a with a′ and b with b′.
   - h₂ sends a, b to y and a′, b′ to y′, with s fixing both. K = G; the
     character is (2, 2), all blindness.

   Both projections merge two pairs of states, equally coarse; the
   character tells them apart only by whether the merged states are
   related by a transformation.

## The check

By script (python3 -I), the two cases above: equivariance holds in both;
K and {g : χ(g) = χ(e)} agree ({e} and {e, s}); the merged fibres are
{a, a′}, {b, b′} and {a, b}, {a′, b′}.

## What follows for A6

The character apparatus captures blindness to transformations, a symmetry
of the perspective, and misses the ignorance CLAIM-350 locates, which is a
judgment not constant on the fibres, whatever their relation to any
group. A6 says "Character theory alone cannot establish that relevance"
of the ignored distinctions; this adds that it cannot establish which
distinctions are ignored either, beyond those a group moves. Agnotological
character (TERM-tmp9mag8) is rightly "not necessarily a literal group
character".
