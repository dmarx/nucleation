---
number: 544
status: Active
formerly:
- THEORY-tmpi29l7
title: "In homotopy type theory extended with a strict directed interval and a layer of shapes, one contractibility condition, the Segal condition, gives a type identities, associativity and three-dimensional coherence, makes every function between Segal types a functor, and yields a dependent Yoneda lemma for covariant families; that such types are (∞,1)-categories rests on a semantics only sketched"
version: 1
tags:
- mathematics
- logic
date: '2026-10-16'
source:
- LIT-032
summary: >-
  Riehl & Shulman (2017), [LIT-032](../literature.d/LIT-032.md), read in full in [NOTE-069](../notes.d/NOTE-069.md). The internal
  results of §§5–11 are proved: associativity from the Segal condition
  applied to A^2 (Prop. 5.9), inner 3-horns (Prop. 5.21), functoriality
  of every function (Prop. 6.1), the dependent Yoneda lemma (Thm 9.5), and
  uniqueness of left adjoints into a Segal type from a Rezk type (Thm
  11.23). Segal and Rezk types match Segal and complete Segal spaces
  (Props A.21, A.25), but soundness of the type theory in bisimplicial sets
  is sketched and depends on an unproved initiality theorem. Coherence in
  all dimensions is conjectured, not proved.
---

# THEORY-544: In homotopy type theory extended with a strict directed interval and a layer of shapes, one contractibility condition, the Segal condition, gives a type identities, associativity and three-dimensional coherence, makes every function between Segal types a functor, and yields a dependent Yoneda lemma for covariant families; that such types are (∞,1)-categories rests on a semantics only sketched

## Source

Riehl & Shulman (2017), "A type theory for synthetic ∞-categories",
*Higher Structures* 1(1):147–224, [LIT-032](../literature.d/LIT-032.md), read in full in [NOTE-069](../notes.d/NOTE-069.md) from
arXiv v5 (2023).

## What was actually shown

**The type theory (§§2–4).** Intensional Martin-Löf type theory with Σ, Π,
identity types and function extensionality, with no univalence and no HITs.
To it are added a layer of cubes (powers of a strict interval 2), a layer of
topes (coherent formulas in cube variables), and extension types: functions
on a shape judgmentally fixed on a sub-shape. hom_A(x, y) is the extension
type of arrows 2 → A from x to y. Relative function extensionality (Axiom
4.6) is assumed.

**The Segal condition.** A is Segal if for composable f and g the type
Σ_h hom²_A(f, g; h) is contractible. Equivalently, restriction from the
2-simplex to the 2-1-horn is an equivalence (Thm 5.5).

**What it gives, all proved internally.**
- Π-types of Segal types are Segal, including A^X for a shape X (Cor. 5.6).
- Identity laws and associativity (Props 5.8–5.9). Associativity comes from
  applying the Segal condition to A^2 and restricting along Δ³ → Δ² × 2.
- Homotopies are 2-simplices (Props 5.10, 5.12).
- The 3-1- and 3-2-horn inclusions are inner anodyne (Prop. 5.21).
- Every function between Segal types preserves identities and composition,
  and arrows in a function type are natural transformations (Props 6.1,
  6.3–6.6).
- λx. hom_A(a, x) is covariant iff A is Segal (Prop. 8.13, repaired in v5).
- The dependent Yoneda lemma (Thm 9.5): for a covariant family over hom(a, −),
  evaluation at (a, id_a) is an equivalence. The paper reads it as a directed
  form of path induction.
- For A Segal and B Rezk, the left adjoints of u : B → A form a proposition,
  and the whole adjunction is unique (Thm 11.23). This is stronger than the
  abstract's "between Rezk types".

**The semantics (Appendix A).** In the Reedy model structure on bisimplicial
sets, Segal types are Segal spaces (Prop. A.21, proving Joyal's conjecture)
and Rezk types are complete Segal spaces (Prop. A.25).

**What could have come out otherwise.** Associativity or the 3-horn fillers
could have needed further axioms beyond the 2-horn condition. They did not.

## What this does not say

- **That the type theory is sound for (∞,1)-categories.** §A.2 says "We will
  not give a complete proof, but only sketch the main ideas". Soundness waits
  on Lumsdaine–Warren coherence and an initiality theorem (p. 66). The
  internal results stand on their own; their meaning as (∞,1)-category
  theory rests on the sketch ([NOTE-069](../notes.d/NOTE-069.md), C7).
- **That the Segal condition gives all higher coherences.** Only horns up to
  dimension 3 are proved. The general statement is conjectured (p. 4) and the
  general inner-horn statement is "presumably" a theorem-schema (p. 31).
- **That the rules are checked.** The rule (∗) is postulated to patch
  admissibility (p. 10), and the reading could not check every premise of
  the rule figures, which did not survive extraction.
- **That it covers categorical fibrations or directed univalence.** Only
  groupoid-valued (covariant) families are treated, and no universe of
  covariant families is built.
- **That the HoTT book's Yoneda lemma is this one.** The 1-categorical lemma
  (HoTT book Thm 9.5.4) is a different statement ([NOTE-195](../notes.d/NOTE-195.md)).
- **Anything about the Rzk proof assistant.** The paper does not name it.

## Connections

- [THEORY-032](THEORY-032.md) reads the ordinary Yoneda lemma as a criterion of identity up to
  isomorphism. Thm 9.5 here is the directed, dependent version, and the
  record should not merge the two.
- [THEORY-642](THEORY-642.md) states two-level type theory's conservativity over HoTT.
  The paper names 2LTT as the "brute force" alternative it declines, keeping
  every type fibrant and moving cofibrations into a separate syntax
  (pp. 5–6). The two are alternative answers to how to make coherence towers
  internal; both can be right.
