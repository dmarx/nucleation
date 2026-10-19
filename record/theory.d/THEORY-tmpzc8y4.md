---
status: Active
title: 'An adjunction between a category and the opposite of another restricts to a dual equivalence between the full subcategories on which its unit and counit are isomorphisms'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-604 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-604.yaml, batch 009, ADR-047).
    LIT-115 states the construction (§3, p. 58) without proof. The proof is
    re-derived below under ADR-047 v2 (the owner's rule of 2026-10-19).
    THEORY-604 keeps the thesis that most mathematical dualities have this
    form, and the verdicts on physicists' dualities, and extends this one.
tags:
- mathematics
- philosophy-of-mathematics
date: '2026-10-19'
source:
- LIT-115
summary: >-
  Corfield (2017), [LIT-115](../literature.d/LIT-115.md), §3, read in full in [NOTE-141](../notes.d/NOTE-141.md), with the proof
  the paper omits written out here. For F : C → D^op left adjoint to
  G : D^op → C, let C′ and D′ be the full subcategories on which the unit
  and the counit are isomorphisms. Then F and G restrict to inverse
  equivalences C′ ≃ D′, and D′ is a full subcategory of D^op, so C′ is
  dually equivalent to a full subcategory of D. Pontrjagin duality is the
  example. That most dualities are of this form is [THEORY-604](THEORY-604.md)'s thesis,
  still Proposed.
extended_by:
- THEORY-604
---
<!-- inactive-ok-file: THEORY-604 — Proposed; the breadth thesis this construction was split from and that extends it, cited as open -->

# THEORY-tmpzc8y4: An adjunction between a category and the opposite of another restricts to a dual equivalence between the full subcategories on which its unit and counit are isomorphisms

## Source

Corfield (2017), [LIT-115](../literature.d/LIT-115.md), §3, p. 58, read in full in [NOTE-141](../notes.d/NOTE-141.md). The paper
states the construction, with Pontrjagin duality as its example, and gives
no proof. The proof below is the record's (ADR-047 v2).

## What was actually shown

Let F : C → D^op be left adjoint to G : D^op → C, with unit η : 1 → GF and
counit ε : FG → 1. Let C′ be the full subcategory of C on the objects c for
which η_c is an isomorphism, and D′ the full subcategory of D^op on the
objects d for which ε_d is an isomorphism.

**F maps C′ into D′.** For c in C′, the triangle identity gives
ε_(Fc) ∘ F(η_c) = 1_(Fc). Since η_c is invertible, so is F(η_c), and then
ε_(Fc) = F(η_c)⁻¹ is invertible. So Fc is in D′.

**G maps D′ into C′.** For d in D′, the other triangle identity gives
G(ε_d) ∘ η_(Gd) = 1_(Gd). Since ε_d is invertible, so is G(ε_d), and then
η_(Gd) = G(ε_d)⁻¹ is invertible. So Gd is in C′.

**They are inverse equivalences.** On C′ the unit is a natural isomorphism
1 ≅ GF, and on D′ the counit is a natural isomorphism FG ≅ 1. So the
restrictions F : C′ → D′ and G : D′ → C′ are inverse equivalences. D′ is a
full subcategory of D^op, so C′ is equivalent to the opposite of a full
subcategory of D: a dual equivalence.

The construction is standard category theory. Its use to the record is as
the precise statement that [THEORY-604](THEORY-604.md)'s thesis is about.

## What this does not say

- **That most mathematical dualities are of this form.** That is
  [THEORY-604](THEORY-604.md)'s thesis. The source shows it by worked exposition of
  standard cases, not by proof, and says there is unlikely to be "a single
  monolithic account".
- **Anything about the dualities physicists name.** Those verdicts rest on
  a stated preference and a paragraph per case, and stay in [THEORY-604](THEORY-604.md).
- **That C′ or D′ is large.** Either can be empty. The construction says
  where the adjunction is an equivalence, not that it is one anywhere.
