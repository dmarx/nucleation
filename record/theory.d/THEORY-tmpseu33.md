---
status: Active
title: 'In any logical system presented as an institution, theories can be glued wherever their vocabularies can: if the category of signatures has colimits, so does the category of theories, the glued theory being the semantic closure of the union of the parts'' translated sentences; and because constraints requiring free or initial interpretation also obey the Satisfaction Condition, theories carrying them glue the same way'
version: 1
tags:
- logic
- mathematics
date: '2026-10-29'
source:
- LIT-1661
summary: >-
  Goguen and Burstall (1992), LIT-1661, read in NOTE-tmpyi64y from the
  published JACM article. Theorem 11 (p. 108) proves that the forgetful
  functor from theories to signatures reflects colimits, using only the
  Satisfaction Condition and the Closure Lemma; Proposition 23 and
  Theorem 24 (p. 119) extend it to theories with data constraints. Active:
  proved, and checked on a toy propositional institution. It does not say
  that signatures have colimits in a given logic, that the glued theory
  is consistent, or anything about proofs: closure is semantic.
---
<!-- inactive-ok-file: CLAIM-469 — Proposed; the claim this result bears on, cited as open -->

# THEORY-tmpseu33: In any logical system presented as an institution, theories can be glued wherever their vocabularies can: if the category of signatures has colimits, so does the category of theories, the glued theory being the semantic closure of the union of the parts' translated sentences; and because constraints requiring free or initial interpretation also obey the Satisfaction Condition, theories carrying them glue the same way

## Source

Goguen and Burstall (1992), LIT-1661, §2.2–2.4 and §3.2, pp. 103–109 and
116–121 of the Journal of the ACM 39(1); read in NOTE-tmpyi64y.

## What was actually shown

**The setting.** An institution: signatures **Sign**, sentences
Sen: **Sign** → **Set**, models **Mod**: **Sign** → **Cat**^op, and a
satisfaction relation per signature, with the Satisfaction Condition
m′ ⊨ Sen(φ)(e) iff Mod(φ)(m′) ⊨ e for every signature morphism φ
(Definition 1, pp. 101–102). A theory is (Σ, E) with E closed under
E• = E** (semantic consequence); a theory morphism is a signature
morphism φ with φ(E) ⊆ E′ (Definitions 2 and 5, pp. 103–105).

**The lemmas.** The Satisfaction Condition reads φ⁻¹(E*) = φ(E)*
(p. 105). From it, the Closure Lemma φ(E•) ⊆ φ(E)• (Lemma 7), and the
Presentation Lemma: φ is a theory morphism (Σ, E•) → (Σ′, E′•) iff
φ(E) ⊆ E′• (Lemma 8, p. 105).

**Theorem 11 (p. 108).** Sign: **Th** → **Sign** reflects colimits. Given
a diagram of theories (Σₙ, Eₙ) and a colimit α′ of the signatures with
apex Σ, set E = (∪ₙ αₙ(Eₙ))•. Each αₙ is a theory morphism. For any other
cone βₙ: (Σₙ, Eₙ) → (Π, F), the unique signature map φ: Σ → Π with
αₙ; φ = βₙ satisfies φ(E) ⊆ (∪ₙ βₙ(Eₙ))• ⊆ F by the Closure Lemma, so φ
is a theory morphism. Hence theories are [finitely] cocomplete when
signatures are (p. 108). The authors say the converse is easy and that
"Sign creates colimits" (p. 109), without proof.

**Constraints.** A Σ-constraint (F: T″ → T′, θ: Sign(T′) → Σ) is
satisfied by A iff θA satisfies T′ and is F-free (Definition 19, p. 117);
it translates along φ to (F, θ; φ), and the Satisfaction Condition for it
is functoriality of Mod (Lemma 21, p. 118). So sentences plus constraints
form an institution (Proposition 23) and constraining theories are
cocomplete when signatures are (Theorem 24, p. 119). The same holds for
the generalized constraints of Proposition 26 and, by an omitted proof,
for duplex institutions (Theorems 44 and 45, p. 130).

**A check.** In a toy institution of my own (propositional logic,
signatures finite sets of atoms, every function a signature morphism), I
glued ({a, b}, {a → b}) and ({a, c}, {a}) over ({a}, ∅). The colimit
theory contains b, which neither part contains, and for all 69 cones into
theories over a three-atom signature the mediating signature map was a
theory morphism. The Satisfaction Condition itself held in all 1,414
cases tried, including non-injective morphisms.

**What could have failed.** The mediating signature map could have
failed to carry the glued sentences into the target theory. The
Satisfaction Condition, through the Closure Lemma, is exactly what rules
that out; without it the semantic closure of the union need not be
respected by maps that respect the parts.

## What this does not say

- **That a given logic's signatures have colimits.** That has to be
  shown per logic; the paper cites it for equational signatures and
  asserts it for first-order ones (pp. 108–109).
- **That the glued theory has models.** A colimit can be inconsistent:
  adding 1 + n = n to the constrained NP theory leaves no models
  (pp. 120–121).
- **Anything about proofs.** Closure is semantic (p. 103). The glued
  theory's consequences are fixed, not computed; no inference rules for
  constraints are given (p. 119).
- **That every structuring operation a specification language uses is a
  colimit.** The paper argues the principle (p. 107) and shows sum and
  parameter application; hiding and derived operations are not treated.
- **That gluing preserves conservativity.** The glued theory can entail
  sentences over a part's vocabulary that the part did not, as the toy
  example's b shows.
