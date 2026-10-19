---
number: 604
status: Proposed
formerly:
- THEORY-tmppcg14
promote_when: >-
  A case-by-case analysis of the dualities physicists name (T-, S-, mirror,
  gauge–gravity), each stated precisely, that checks whether it involves
  arrow reversal into an opposite category or is an equivalence. The
  account is supported if the mathematical dualities fall under
  adjunctions into opposites and the physicists' cases sort cleanly into
  reversals and equivalences; it is refuted by a standard duality with no
  adjunction behind it, or by physicists' cases that fit neither. More
  examples of dualities that are adjunctions cannot settle it, since the
  paper already concedes there is no single account.
title: "Most mathematical dualities are adjunctions between one category and the opposite of another, which become dual equivalences on their fixed points; what makes them dualities rather than equivalences is the reversal of arrows, so many of the 'dualities' physicists name are, in the mathematician's sense, equivalences or symmetries"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-604.yaml, batch 009, ADR-047),
    the core construction is filed apart as THEORY-tmpzc8y4, Active. That
    construction is that an adjunction into an opposite category restricts
    to a dual equivalence on its fixed points, with the proof the paper
    omits re-derived under ADR-047 v2. This THEORY extends it and keeps the
    breadth thesis and the verdicts on physicists' dualities. The
    promote_when bears on those and is unchanged, and the status stays
    Proposed.
tags:
- philosophy-of-mathematics
- mathematics
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-115
summary: >-
  Corfield (2017), [LIT-115](../literature.d/LIT-115.md), read in [NOTE-141](../notes.d/NOTE-141.md). A short programmatic paper.
  That most dualities of interest are covered by constructions around
  adjunction is shown by worked exposition of standard cases, not proved.
  There is unlikely to be "a single monolithic account" (pp. 59–60).
  Reserving "duality" for structural reversal is a stated preference, and
  the verdicts on string dualities are a paragraph each. The proposal that
  philosophers of physics need homotopy type theory is an expectation.
extends:
- THEORY-tmpzc8y4
---
<!-- inactive-ok-file: THEORY-459 THEORY-690 — Proposed; the De Haro and Butterfield accounts named for their different use of the word -->

# THEORY-604: Most mathematical dualities are adjunctions between one category and the opposite of another, which become dual equivalences on their fixed points; what makes them dualities rather than equivalences is the reversal of arrows, so many of the 'dualities' physicists name are, in the mathematician's sense, equivalences or symmetries

## Source

Corfield (2017), [LIT-115](../literature.d/LIT-115.md), "Duality as a category-theoretic concept",
*Studies in History and Philosophy of Modern Physics* 59: 55–61, read in
full in [NOTE-141](../notes.d/NOTE-141.md). Page references are the journal's.

## What was actually shown

**The core construction (§3, p. 58).** An adjunction between C and D^op,
restricted to the objects isomorphic to their round-trip image, gives an
equivalence C′ ≃ D′^op, a dual equivalence. Pontrjagin duality is the
example.

**The family around it (§3, pp. 57–59).** Representational duality from a
pairing A × B → C; enrichment in truth values, which gives six classic
Galois-connection dualities, and in extended reals, which gives
Fenchel–Legendre duality; Isbell conjugation; dualising objects that
"keep summer and winter homes" in two categories (2 for Stone duality, R/Z
for Pontrjagin); profunctors; Lawvere and Rosebrugh's formal against
concrete duality. All "revolve around" adjunction.

**Sameness (p. 60).** The right notion of sameness for categories is
equivalence. C and C^op are not equivalent unless C is self-dual, and
C ↦ C^op is the one nontrivial autoequivalence of the category of
categories. Set is not self-dual (∅ and 1 behave asymmetrically), so making
Set the default for concrete categories breaks a symmetry; Rel is
self-dual.

**The physicists' cases (pp. 57, 60).** Homological mirror symmetry can be
read as an equivalence of A∞-categories. Mirror symmetry is a Z2 action on
the Hodge diamond, and a Z2 action alone need not be called a duality.
S-duality is a vestige of an SL(2,Z) action. T-duality involves "extra
choices", so a background may have none, one or several T-duals.

**What could have come out otherwise.** The standard dualities could have
resisted any common categorical form. In Corfield's survey they do not,
though the survey is exposition drawn from the literature, not a proof.

## What this does not say

- **That duality has one account.** "There is unlikely to be a single
  monolithic account of duality" (pp. 59–60).
- **That set theory cannot express dualities.** It can "in principle"; the
  claim is that it could not do so as "naturally" or systematically (C4).
- **That physicists are wrong to say "duality".** Reserving the word for
  "involution with some form of structural reversal" is a preference
  ("In my view it is preferable", p. 57).
- **That predicate logic fails for these questions.** That it is "far from
  optimal" is an expectation, with one worked contrast (quotient against
  action groupoid); no failure is exhibited ([NOTE-141](../notes.d/NOTE-141.md), Corrections).
- **Anything about gauge–gravity duality.** AdS/CFT is not mentioned.

## Connections

- De Haro and Butterfield ([LIT-199](../literature.d/LIT-199.md)) define a duality as an isomorphism of
  model roots, which is an equivalence in Corfield's vocabulary. Their
  accounts in the record, [THEORY-459](THEORY-459.md) and [THEORY-690](THEORY-690.md), use the word
  for a different relation from this one, and a reader moving between them
  has to translate. The two do not disagree on any fact.
- Wallace's open question of what notion of mathematical equivalence a
  structural realism needs ([LIT-151](../literature.d/LIT-151.md)) gets a direction from this paper,
  equivalence and groupoids, not a criterion.
- Stone duality, the dualising object 2, is the record's [THEORY-020](THEORY-020.md).

## Note of 2026-10-19: the core construction filed apart

The construction in §3 is now [THEORY-tmpzc8y4](THEORY-tmpzc8y4.md), Active, with the proof
written out: an adjunction between C and D^op restricts to a dual
equivalence between the full subcategories on which its unit and counit are
isomorphisms. What keeps this THEORY Proposed is the claim that most
mathematical dualities have that form, which the source shows by worked
exposition and not by proof. Also kept are the verdicts on the dualities
physicists name, which rest on a stated preference. The promote_when says
what would settle both.
