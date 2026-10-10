---
number: 32
status: Active
formerly:
- THEORY-tmp9666i
title: 'The Yoneda lemma determines an object only up to isomorphism, from its whole hom-functor, among objects the category already has; as a formal version of "an object is determined by its relations" it presupposes the relata'
version: 1
tags:
- philosophy-of-mathematics
- mathematics
- individuation
- metaphysics
date: '2026-09-30'
source:
- LIT-221
- LIT-222
- LIT-154
summary: >-
  nLab, Yoneda lemma (rev. 2026-08-17), [LIT-221](../literature.d/LIT-221.md) — y is fully faithful and
  y(c) ≅ y(d) iff c ≅ d, and pointwise bijections of hom-sets without
  naturality do not suffice. Lam & Wüthrich ([LIT-222](../literature.d/LIT-222.md)) state two of its
  consequences without the name. The philosophical reading, a relational
  criterion of identity up to isomorphism rather than a construction of
  objects from relations, is the record's own. It does not say that the
  lemma supports eliminating objects.
supports:
- CLAIM-132
- CLAIM-135
- CLAIM-136
- CLAIM-137
- CLAIM-142
- CLAIM-150
---

# THEORY-032: The Yoneda lemma determines an object only up to isomorphism, from its whole hom-functor, among objects the category already has; as a formal version of "an object is determined by its relations" it presupposes the relata

## Source

nLab, *Yoneda lemma*, revision of 2026-08-17, [LIT-221](../literature.d/LIT-221.md), read in [NOTE-195](../notes.d/NOTE-195.md):
Proposition and proof, Corollaries I–III, "Necessity of naturality", "In
semicategories". Supporting: Lam & Wüthrich, [LIT-222](../literature.d/LIT-222.md) §§4–5 ([NOTE-194](../notes.d/NOTE-194.md));
Leitgeb & Ladyman, [LIT-154](../literature.d/LIT-154.md) ([NOTE-133](../notes.d/NOTE-133.md)), for the matching limit of structural
identity criteria.

## What was actually shown

**The mathematics (proved, and checked in [NOTE-195](../notes.d/NOTE-195.md)).** For a locally small
category C, a presheaf X and an object c, natural transformations
Hom(−,c) ⇒ X correspond bijectively to X(c), by η ↦ η_c(id_c). Taking X
to be a representable gives Corollary I: the Yoneda embedding
y : c ↦ Hom(−,c) is fully faithful. Because fully faithful functors reflect
isomorphisms, Corollary II follows: y(c) ≅ y(d) exactly when c ≅ d.

**Three conditions the page's own content exposes.**

1. *The relational profile is the hom-functor with its action by
   composition, not a list of hom-sets.* The page gives two non-isomorphic
   objects A and B with Hom(A,−)(Z) and Hom(B,−)(Z) in bijection for every
   Z (hom-sets ℤ≥0 and ℤ≥1 under addition). Only natural isomorphism of
   hom-functors fixes the object. Bare counts suffice only in special
   classes: finite relational structures (Lovász 1967), Pultr's categories.
2. *Identities are needed.* The proof evaluates at id_c, and the lemma
   fails for semicategories in general.
3. *The objects are presupposed.* y(c) is indexed by every object of C,
   and the conclusion is an isomorphism between two of them.

**Up to isomorphism, and no further.** Two distinct but isomorphic
objects, such as two singletons in Set, have isomorphic profiles. The lemma
cannot tell them apart. Leitgeb & Ladyman meet the same limit for graphs:
the two nodes of the edgeless two-node graph share every relational
property, yet mathematicians count them as two ([LIT-154](../literature.d/LIT-154.md)). The categorical
response is to deny that the distinction matters (identity = isomorphism,
as in univalent foundations). It does not discern them.

**Its unnamed use in the OSR literature.** Lam & Wüthrich argue that
generalized elements X → A exist in every category, and that morphisms
"only distinguish isomorphism classes of structures" ([LIT-222](../literature.d/LIT-222.md) §4 p. 10, §5
p. 11). These are consequences of the lemma, although the paper never
names it. The record's search found no core OSR paper that names it
([NOTE-193](../notes.d/NOTE-193.md), [NOTE-194](../notes.d/NOTE-194.md)).

**So, the record's reading.** The lemma is the precise form of "an object
is determined by its relations" for objects that are already there. It is
a relational criterion of identity up to isomorphism. It does not
construct objects from relations that lack relata.

## What this does not say

- That the lemma supports radical (eliminative) ontic structural realism.
  On this reading it supports at most objects as positions in a structure.
  The argument about ROSR is a separate claim, filed beside this one.
- That any author in the OSR debate reads the lemma this way. Bain
  ([LIT-223](../literature.d/LIT-223.md)) and Lam & Wüthrich do not mention it. The two works found that
  do name it were not filed: Adlam 2025 misreads its own source, and
  Hendren et al. 2026 assert rather than argue ([NOTE-194](../notes.d/NOTE-194.md)).
- Anything about enriched, bicategorical or (∞,1)-versions, whose
  statements differ. Nor anything about Riehl & Shulman's directed
  dependent Yoneda ([LIT-032](../literature.d/LIT-032.md)).
- That the nLab page is flawless. Its finite counterexample breaks the
  identity law as written, and its classical statement omits naturality
  in c and X ([NOTE-195](../notes.d/NOTE-195.md)).

## Connections

- [LIT-223](../literature.d/LIT-223.md) and [LIT-222](../literature.d/LIT-222.md): the category-theoretic ROSR debate that this
  settles the formal side of.
- [LIT-196](../literature.d/LIT-196.md) (Chakravartty): inside a category the lemma is a partial
  counterexample to "relations cannot fix identity without intrinsic
  features". It fixes identity only up to isomorphism, and the objects are
  presupposed.
- [THEORY-004](THEORY-004.md) and [THEORY-017](THEORY-017.md) have the same shape in other settings:
  something is fixed only up to a symmetry group (orthogonal, unitary) by
  the data taken to be intrinsic. This is an analogy, not a shared
  mechanism.
