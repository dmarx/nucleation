---
number: 593
status: Active
formerly:
- CLAIM-tmpye2m2
title: 'Isomorphism is not persistence, in either direction: two separately made mechanisms with the same costed transformation structure are isomorphic and still two, and one mechanism whose hinge is replaced can persist while its costed structure becomes non-isomorphic to the earlier one, so which morphisms count as continuations is structure added by assumptions about the domain, not read off the category'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): CASE-199 was promoted in the same change,
    THEORY-032 is Active; the M′ table and the search over all six
    bijections were re-run. The claim's opening paragraph now states
    the stipulation its second direction rests on, that the mechanism
    with its hinge replaced is the same mechanism, which before was
    said only in the summary and the body's later example.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either example: an equivalence-invariant property of a
  category that tells apart two uniquely isomorphic objects, or counts
  them as other than one up to equivalence; or an isometry between the
  three-state Lawvere metric spaces of CASE-199 before and after the
  cost of moving from U to R falls from 3 to 1. Not defeated by a criterion
  of persistence that is itself structural, such as a chosen class of
  continuation morphisms, which the claim says must be added; nor by a
  domain in which persistence is taken to be isomorphism by stipulation,
  which is such a choice.
tags:
- individuation
- mathematics
- metaphysics
date: '2026-11-05'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-032
- CASE-199
complements:
- CLAIM-544
- CLAIM-134
- CLAIM-150
bears_on:
- QUESTION-284
- QUESTION-393
- QUESTION-029
summary: >-
  A's proposal, from the owner's paste of 2026-11-05 (fourth), A's "Toward a
  resource-sensitive Yoneda theory of individuation" §7: "Structural
  isomorphism ⇏ token identity, and token persistence ⇏ structural
  isomorphism", with continuation morphisms as "a distinguished class",
  since "Copying, replacing, and transporting can be categorically
  representable without establishing that an original individual
  persists." Both non-implications are shown by example. The first is the
  categorical form of [CLAIM-134](CLAIM-134.md)'s two singletons in Set: a category with two
  uniquely isomorphic objects is equivalent to one with a single object, so
  nothing invariant under equivalence, Yoneda profiles included, counts
  the tokens. The second uses A's three-state toy ([CASE-199](../cases.d/CASE-199.md)): lowering
  one move's cost leaves a space with no isometry to the first, though the
  mechanism is stipulated to be the same one. Checked by the filer with
  python3 -I. [CLAIM-544](CLAIM-544.md) holds the same point for willed agents, as "a
  question of continuation, not of resemblance". The construction is the filer's, from
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-134 CLAIM-170 CLAIM-544 — Proposed; the record's open theses on structural identity and willed agents, its open term for the senses of individuation, and A's proposals of 2026-11-05 with the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-593: Isomorphism is not persistence, in either direction: two separately made mechanisms with the same costed transformation structure are isomorphic and still two, and one mechanism whose hinge is replaced can persist while its costed structure becomes non-isomorphic to the earlier one, so which morphisms count as continuations is structure added by assumptions about the domain, not read off the category

## The claim

A (§7): "Suppose two independently manufactured origami mechanisms have
exactly the same construction and admissible transformation structure.
They may be isomorphic as objects of the category we've chosen. But
they're still two physical mechanisms. Conversely, one particular
mechanism can have its crease pattern modified or a hinge replaced. Its
available transformations may change so much that the later mechanism is
no longer isomorphic to the earlier one. Nevertheless, we might regard it
as the same persisting physical object." So: "Structural isomorphism ⇏
token identity, and token persistence ⇏ structural isomorphism. Yoneda
doesn't remove this distinction." The second direction rests on a
stipulation: that the mechanism with its hinge replaced is the same
mechanism. The claim shows that the costed structure does not decide
this, so "can persist" means that persistence, so stipulated, is
consistent with the loss of isomorphism.

**Isomorphic and two.** Let 𝓜 be a category whose objects are mechanisms
and whose isomorphisms are the isometries of their costed transformation
structures, and let M₁ and M₂ be two separately made copies of one
design, so that the identity map of the design is an isometry
f: M₁ → M₂. By Yoneda ([THEORY-032](../theory.d/THEORY-032.md)) their profiles are isomorphic,
Hom(−, M₁) ≅ Hom(−, M₂), so no profile tells them apart. More: the full
subcategory on {M₁, M₂} has exactly one morphism between any two of its
objects and is equivalent to the category with one object and its
identity. Any property of the category that is invariant under
equivalence, which is every property category theory states without
naming objects, comes out the same whether there are one, two or a
thousand copies. The count of tokens is not in the structure. [CLAIM-134](CLAIM-134.md)
holds this for graphs and sets: "Two singletons in Set are the
categorical version" of Leitgeb and Ladyman's edgeless two-node graph,
whose "two nodes are not even weakly discernible, yet graph theory
counts two."

**One and non-isomorphic.** Take A's toy ([CASE-199](../cases.d/CASE-199.md)) as M: moves
U → L 1, L → U 3, U → R 3, R → U 1, costs adding. Replace the hinge that
drives U → R with one that costs 1, and call the result M′. Their
distance tables are

| | M: to L, U, R | M′: to L, U, R |
|---|---|---|
| from L | 0, 3, 6 | 0, 3, 4 |
| from U | 1, 0, 3 | 1, 0, 1 |
| from R | 2, 1, 0 | 2, 1, 0 |

The multisets of distances differ (M has a 6, M′ none), so no bijection of
states is an isometry, and M and M′ are not isomorphic in any category
whose isomorphisms are isometries. Whether M′ is M, later, is not
decided by the tables: it is the same sheet with one hinge swapped, and
whether that is the same mechanism is a question about mechanisms. Even in
the path groupoid, where M and M′ are both one connected groupoid on
three objects and so equivalent, the equivalence would hold equally
between M and a new mechanism built to M′'s design.

**Continuations are added structure.** A: "One possible approach is to
equip the total process category with a distinguished class of
continuation morphisms. These would express which transformations
preserve the historical continuity relevant to a particular kind of
object. But not every morphism should automatically count as
continuation. Copying, replacing, and transporting can be categorically
representable without establishing that an original individual
persists." The first example shows why the class cannot be defined from
the category: if f: M₁ → M₂ is read as a transport (M₂ is M₁, moved) or as
a copy (M₂ is a replica), the category is the same in both readings, and
only the first puts f in the class. A: "deciding which physical
transformations count as continuations requires assumptions about the
domain."

**Checked** by the filer with python3 -I: the closures of both move sets
under addition give the tables above; a search over all six bijections of
{L, U, R} finds no isometry from M to M′; the sorted distances are
(0, 0, 0, 1, 1, 2, 3, 3, 6) and (0, 0, 0, 1, 1, 1, 2, 3, 4).

## What it adds

- **For the categorical program.** A Yoneda profile, however enriched,
  identifies up to isomorphism ([THEORY-032](../theory.d/THEORY-032.md)), and so is blind to the count
  of tokens and to history. A (§7): "The mathematical model therefore needs
  to represent actual continuations through time, not merely compare
  endpoint structures." The examples say what the added class must carry:
  not more structure on the objects, but a choice among morphisms that the
  category already has or lacks.
- **For willed agents.** [CLAIM-170](CLAIM-170.md) individuates a willed agent as "the
  jurisdiction of a will-organization", and [CLAIM-544](CLAIM-544.md) makes a revision of
  it a possible re-individuation, "a question of continuation, not of
  resemblance". The second example is that point outside agents: a
  persisting individual whose organization changes past isomorphism. A:
  "Both are proposed philosophical claims, not established categorical
  theorems."
- **For [QUESTION-284](../questions.d/QUESTION-284.md).** A: "That's exactly the sort of distinction
  [QUESTION-284](../questions.d/QUESTION-284.md) asks us to confront: when do relations merely characterize
  an object, when do they causally affect it, and when do they partly
  constitute its identity?" The claim shows only that structure alone does
  not settle the matter; it does not answer when relations constitute.

## What it does not say

- **That persistence has no structural criterion.** One can be added, as
  a class of continuation morphisms, or by a theory of maintenance
  ([TERM-088](../terms.d/TERM-088.md)'s dynamical and autonomy senses); the claim says it is
  added, not that it is arbitrary.
- **What makes a hinge swap a continuation.** That is the domain's
  assumption, as A says, and the record holds none for mechanisms.
- **That the tokens are primitive.** [CLAIM-134](CLAIM-134.md)'s dilemma, whether
  numerical plurality without relational difference concedes a
  non-relational ground of identity, is not decided here; the examples
  show only that the categorical structure does not decide it either.
- **Anything about the Grothendieck construction** of A's §6 ([TERM-114](../terms.d/TERM-114.md)'s
  changes of architecture as moves); the second example compares two
  architectures' categories, not a total category.
