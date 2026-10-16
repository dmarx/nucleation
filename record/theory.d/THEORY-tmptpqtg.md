---
status: Active
title: "Basic two-level type theory, an inner homotopy type theory with an outer level of strict equality, is conservative over homotopy type theory, so an inner type it proves inhabited is already inhabited in HoTT, but a fibrant-replacement type former would force uniqueness of identity proofs on the inner level"
version: 1
tags:
- mathematics
- logic
date: '2026-10-16'
source:
- LIT-095
summary: >-
  Annenkov, Capriotti, Kraus & Sattler (2017; MSCS 2023), [LIT-095](../literature.d/LIT-095.md), whose
  §§1–3 were read in full in [NOTE-047](../notes.d/NOTE-047.md), the reading of the nLab page it
  supersedes ([LIT-040](../literature.d/LIT-040.md)). Props 2.18–2.19 prove that inhabitation of inner
  types is reflected, through a presheaf model over any model of HoTT.
  Thm 2.20 proves that a fibrant-replacement former implies UIP for inner
  types. The conservativity is the weak, inhabitation-reflecting kind.
  Results that use the axioms relating the two levels' natural numbers,
  which untruncated semisimplicial types need, are not known to transfer.
---

<!-- inactive-ok-file: LIT-040 — Superseded by LIT-095; its NOTE is where LIT-095 was read, named for that -->

# THEORY-tmptpqtg: Basic two-level type theory, an inner homotopy type theory with an outer level of strict equality, is conservative over homotopy type theory, so an inner type it proves inhabited is already inhabited in HoTT, but a fibrant-replacement type former would force uniqueness of identity proofs on the inner level

## Source

Annenkov, Capriotti, Kraus & Sattler, "Two-Level Type Theory and
Applications" (arXiv:1705.03307v5; *Mathematical Structures in Computer
Science* 2023), [LIT-095](../literature.d/LIT-095.md). It was read as the paper behind the nLab page
[LIT-040](../literature.d/LIT-040.md), in [NOTE-047](../notes.d/NOTE-047.md): §§1–3, §4.7 from Def. 4.46 and §5 in full, and §§4.3–4.6
at the level of statements. [LIT-095](../literature.d/LIT-095.md) has no NOTE of its own.

## What was actually shown

**Definition by models (Defs 2.6–2.9).** A model of 2LTT is two cwf
hierarchies on one category of contexts. The outer level is a set-level type
theory with UIP and funext. The inner level is a model of HoTT with
univalent universes. A conversion c maps inner types to outer ones and
preserves context extension. It is not assumed injective, strict or replete.

**Conservativity (Props 2.13, 2.18–2.19).** For any model C of HoTT, the
presheaf category Ĉ is a model of 2LTT, and Yoneda acts bijectively on inner
types and terms. Hence an inner type over a HoTT context that is inhabited in
2LTT is inhabited in HoTT. This survives outer type formers the presheaf
model validates, equality reflection included, and the strictness
conditions (T1) and (T2).

**The limit (Thm 2.20).** An internal fibrant-replacement type former
forces UIP on inner types, so it cannot be added while keeping homotopical
models.

**What the outer level buys.** Inner HoTT cannot quantify over the external
ℕ that indexes coherence towers. The outer level's ℕ is that ℕ. Reedy fibrant
diagrams over finite inverse categories become internal, and finite
truncations of semisimplicial types become definable in basic 2LTT (Lemma
4.38).

**What could have come out otherwise.** Strict outer equality could have let
2LTT prove inner statements HoTT cannot. For basic 2LTT it does not.

## What this does not say

- **That every 2LTT result transfers.** Results using (A1)–(A3), which relate
  the two natural-number types, are not known to transfer to plain HoTT
  (§5). The untruncated type of semisimplicial types needs (A2) or similar.
- **That conservativity is bijective.** It reflects inhabitation only (Def.
  2.17). A stronger, bijective conservativity under equality reflection is
  conjectured, with an argument credited to Kovács (p. 23).
- **That the syntax is the initial model.** The correspondence is not proved
  (Remark 2.1).
- **That inner types are "fibrant".** The paper reserves "fibrant" for an
  outer type with a chosen isomorphism to an inner one, which is structure,
  not a property. The nLab page uses the word differently ([NOTE-047](../notes.d/NOTE-047.md),
  corrections).
- **That the principle of equivalence is an open question for basic 2LTT.**
  The nLab page says it is; its own cited paper answers it for the basic
  theory.

## Connections

- [THEORY-tmpi29l7](THEORY-tmpi29l7.md): Riehl and Shulman's type theory with shapes is the other
  answer to the same question, keeping every type homotopy-invariant instead
  of adding strict equality.
