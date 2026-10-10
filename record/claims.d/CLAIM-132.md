---
number: 132
status: Active
formerly:
- CLAIM-tmp3sn40
title: 'Characters classify finite-dimensional representations of a finite or compact group up to isomorphism only over a field of characteristic zero; they forget the isomorphisms, fix neither the group nor a permutation action, and classify kinds, not tokens or positions'
version: 1
role: granted
tags:
- mathematics
- individuation
date: '2026-10-10'
line: 'pragmatic-transport'
objects_to:
- CLAIM-137
- CLAIM-136
grounds:
- LIT-893
- THEORY-032
complements:
- CLAIM-043
- CLAIM-148
summary: >-
  Standard representation theory, which the exchange states correctly
  with its main hypotheses (A194 §1, A198 §§2 and 4, A203 §§5–6, A218
  §3.2). This entry adds the limits the exchange left out, and the exact
  link to Yoneda: a character is a counts-only relational profile,
  complete because the category is semisimple. Granted, because it bounds
  the owner's analogy: priority for classifying kinds up to isomorphism,
  in the most favourable setting, and no further.
---
<!-- inactive-ok-file: LIT-893 — Deferred; registered unread as the standard source for results checked here by reasoning -->
<!-- inactive-ok-file: CLAIM-137 CLAIM-136 — Proposed; the owner's two theses this entry bounds, both open -->
<!-- inactive-ok-file: CLAIM-063 — Proposed; cited as the parallel commutator bound, open -->

# CLAIM-132: Characters classify finite-dimensional representations of a finite or compact group up to isomorphism only over a field of characteristic zero; they forget the isomorphisms, fix neither the group nor a permutation action, and classify kinds, not tokens or positions

## The claim

These are standard results, checked here by reasoning. Serre's *Linear
Representations of Finite Groups* ([LIT-893](../literature.d/LIT-893.md)) is registered as their
standard source and is unread here.

1. The character χ_ρ(g) = Tr ρ(g) is a class function, χ(hgh⁻¹) = χ(g), and
   it is unchanged when ρ is replaced by SρS⁻¹. So a change of coordinates
   cannot change it.
2. For a finite group G and finite-dimensional representations over ℂ, or
   over any field of characteristic zero, χ_ρ₁ = χ_ρ₂ exactly when ρ₁ ≅ ρ₂.
   Over ℂ the reason is short. Maschke's theorem makes every representation
   a direct sum of irreducibles, and the irreducible characters are
   orthonormal for ⟨χ, ψ⟩ = |G|⁻¹ Σ_g χ(g)ψ(g)̄. So the multiplicities
   m_i = ⟨χ, χ_i⟩ can be read off the character, and they fix ρ up to
   isomorphism.
3. The irreducible characters form a basis of the class functions, and
   there are as many of them as there are conjugacy classes.
4. The same holds for continuous finite-dimensional complex representations
   of a compact group.

The exchange states the core correctly. A194 §1: "For finite-dimensional
complex representations of finite groups", ρ₁ ≅ ρ₂ ⇔ χ_ρ₁ = χ_ρ₂, which
"follows from complete reducibility and the orthogonality of irreducible
characters". A198 §2 gives the multiplicity formula. A218 §3.2: "Under the
standard finite-group, finite-dimensional complex assumptions, characters
classify linear representations up to isomorphism."

## Where it fails

- **Characteristic p, even when everything is semisimple.** Over F_p, for the
  trivial group, the one-dimensional and the (p+1)-dimensional trivial
  representations both have character 1. Multiplicities are known only mod
  p. So semisimplicity is not enough.
- **Non-semisimple settings.** For the cyclic group C_p over F_p, the regular
  representation, which is indecomposable, and p copies of the trivial
  representation both have character 0.
- **Infinite groups.** ℤ acting on ℂ² by n ↦ [[1, n], [0, 1]], and ℤ acting
  trivially on ℂ², both have the constant character 2. The two
  representations are not isomorphic. Equal characters give at most
  isomorphic semisimplifications.

A194 §4 says completeness "depends on conditions such as semisimplicity",
which is hedged and incomplete. A218 Ch3.5, "Completeness of characters under
finite-group semisimplicity assumptions", is wrong as worded. It should read
"characteristic zero". A218 §3.2 states the condition correctly.

## What the character forgets

- **The isomorphisms.** A character fixes the isomorphism class, not the
  representation, and the isomorphisms are not unique. By Schur's lemma the
  automorphisms of ⊕ S_i^{m_i} form ∏ GL(m_i). A character lives in the
  representation ring, where the intertwiners are gone. It is a
  decategorification.
- **The group.** The dihedral group D₄ and the quaternion group Q₈ are not
  isomorphic and have the same character table.
- **The permutation action.** The permutation character of a G-set counts
  fixed points, χ_X(g) = |Fix_X(g)|, and non-isomorphic G-sets can share it.
  A198 §4: "Two G-sets can even have the same permutation character without
  being isomorphic as G-sets." Two checked instances:
  - In the Klein four-group, take the regular G-set plus two fixed points,
    and the union of the three G-sets G/H₁, G/H₂, G/H₃ for its three
    subgroups of order two. Both have permutation character (6, 2, 2, 2).
    Their orbit sizes are {4, 1, 1} and {2, 2, 2}.
  - GL(3, 2) acts on the seven points and on the seven lines of the Fano
    plane. The two actions have the same permutation character and are not
    isomorphic as G-sets.

**The exact link to Yoneda.** Over ℂ, ⟨χ_V, χ_i⟩ = dim Hom_G(S_i, V) for each
irreducible S_i. So a character records the *dimensions* of the hom-sets from
the irreducibles. That is a counts-only relational profile, taken on a
restricted family of probes. [THEORY-032](../theory.d/THEORY-032.md)'s first condition says that bare
counts of morphisms do not in general fix an object, and that only special
classes are exceptions. Finite-dimensional representations of a finite group
in characteristic zero are one such class, because the category is semisimple.
The character theorem is a case of the Yoneda moral, and it holds only up to
isomorphism, as Yoneda does.

The loss is of a familiar kind. Equal entropies do not give equal relational
structure ([CLAIM-043](CLAIM-043.md)), and a factorization fixes its latent coordinates only up
to a gauge ([CLAIM-148](CLAIM-148.md)). In each case an invariant is kept and structure is
discarded.

## Kinds, not tokens

Take V irreducible over ℂ. Inside V ⊕ V, the subrepresentations isomorphic to
V correspond to the lines in ℂ², so there are infinitely many, among them
V ⊕ 0, 0 ⊕ V and the diagonal. Every one has the character χ_V. What tells them apart is how
each is embedded in the whole, which is a relation to the larger structure.
A194 §6 states the moral: "A group character classifies the *representation*
up to equivalence. It does not generally individuate each vector."

So a character can classify a kind. It cannot individuate a token or a
position. That is why the owner's two theses at U54 come apart. The character
analogy is evidence for the kind claim ([CLAIM-137](CLAIM-137.md)), bounded by the
results above. It is no evidence for the individuation claim
([CLAIM-136](CLAIM-136.md)), which needs positions and automorphism orbits instead.

## An illustration

A198 §III gives a worked model of [CASE-004](../cases.d/CASE-004.md)'s scene: "two participants, a and
b, and an interaction concerning overspending". The basis is e₁ = a→b and
e₂ = b→a, where the arrow "means only 'occupies the active evaluative
position relative to.'" The group C₂ swaps the participants, ρ(s) is the swap
matrix, and χ = (2, 0), the sum of the trivial and the sign characters. The
arithmetic is right.

But the character carries no communicative content. Any free action of C₂ on
two configurations has character (2, 0), whatever the configurations mean, and
the two "organizational types" are just the two irreducible representations
of C₂. The contrast A198 wants sits elsewhere. As relational structures, the
one-way reprimand {a→b} is moved by the swap, so its stabilizer is trivial,
while the mutual configuration {a→b, b→a} is fixed by it, with stabilizer C₂.
That is a difference of stabilizers, at the level of the G-set, which is the
level A198 §4 says characters forget. So A198's "This is an exact mathematical
model of what a representation-independent communicative invariant could look
like" overstates it. A198's own hedge stands: "A reprimand is not
mathematically equivalent to an antisymmetric representation".

## What survives approximately

A198 §VII Stage 3, A203 §21 and A218 Ch12.5 give an elementary bound. Let S be
an invertible correspondence between two d-dimensional representations of
the same group, and E_g = Sρ_A(g) − ρ_B(g)S its defect in intertwining. Then
ρ_B(g) = Sρ_A(g)S⁻¹ − E_gS⁻¹, so

|χ_A(g) − χ_B(g)| = |Tr(E_gS⁻¹)| ≤ d‖E_gS⁻¹‖ ≤ d‖E_g‖‖S⁻¹‖,

in the operator norm. The derivation is correct, and A198 calls it "not a new
deep representation-theoretic theorem". Its use is the factor ‖S⁻¹‖. It puts
[CLAIM-011](CLAIM-011.md)'s anti-collapse condition into a character setting: "a
noninvertible or badly conditioned correspondence does not support the same
argument" (A198). It has the same shape as [CLAIM-063](CLAIM-063.md)'s bound on commutators,
and it needs an invertible S between representations of one group, which is
not the translation case.

## What it does not say

- That the analogy fails. It holds in the most favourable setting, for kinds,
  and up to isomorphism.
- That characters are useless to the programme. Within a fixed finite group
  in characteristic zero they are a complete invariant of linear
  representations.
- Anything about lossy stochastic channels, where "full character
  preservation is generally unavailable" (A198 §VII).
