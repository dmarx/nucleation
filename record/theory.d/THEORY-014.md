---
number: 14
status: Active
formerly:
- THEORY-tmprs2he
title: 'In both formalisms of contextuality, classicality is the existence of a nonnegative version of a linear representation that always exists over the reals, so negativity is universal and only its unavoidability is nonclassical'
version: 3
history:
- version: 2
  date: '2026-10-09'
  note: >-
    A sentence added: Contextuality-by-Default (LIT-777, Theorems 4.1
    and 6.1) is a third instance of the pattern, extending it to signalling
    data. The claim itself is unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-014.yaml,
    batch 010, ADR-047). Each half of the title is a theorem proved in a work
    the record has read: LIT-016 Thms 5.4, 5.9 and 8.1 (NOTE-016), LIT-003
    Thm 2.8, Cor 3.5 and Prop 4.4 with Thm 4.1's proof in App. B (NOTE-017),
    and LIT-777 Thms 4.1 and 6.1 (NOTE-600). The title states them side by
    side and adds no step, so no re-derivation was needed. The promote_when
    asked for something the title does not claim, a map between the
    formalisms, which "What this does not say" already disclaimed. It moves,
    unchanged, to QUESTION-tmpx8hzz. The claim is unchanged.
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-09-27'
source:
- LIT-016
- LIT-003
summary: >-
  An inference joining two proved results: [LIT-016](../literature.d/LIT-016.md) Thms 5.4 and 5.9 with Thm
  8.1, and [LIT-003](../literature.d/LIT-003.md) Thm 2.8 with Cor 3.5. Each half is proved and read; the
  parallel is the record's own, and [LIT-003](../literature.d/LIT-003.md) attempts no comparison with
  [LIT-016](../literature.d/LIT-016.md).
extends:
- THEORY-012
- THEORY-016
supports:
- CLAIM-037
---

# THEORY-014: In both formalisms of contextuality, classicality is the existence of a nonnegative version of a linear representation that always exists over the reals, so negativity is universal and only its unavoidability is nonclassical

## Source

Abramsky & Brandenburger (2011), [LIT-016](../literature.d/LIT-016.md), Thms 5.4, 5.9, 8.1. Schmid et al. (2020), [LIT-003](../literature.d/LIT-003.md), Thm 2.8, Cor 3.5, Prop 4.4. [NOTE-017](../notes.d/NOTE-017.md) records that [LIT-003](../literature.d/LIT-003.md) attempts no formal comparison with [LIT-016](../literature.d/LIT-016.md).

## What was actually shown

In the sheaf formalism every no-signalling model has a real signed global section, and noncontextuality is the existence of a nonnegative one ([LIT-016](../literature.d/LIT-016.md) Thms 5.4, 5.9, 8.1). In the GPT formalism every tomographically local GPT has a real-linear diagram-preserving representation, and generalized noncontextuality is the existence of a positive quasiprobabilistic one ([LIT-003](../literature.d/LIT-003.md) Thm 2.8, Cor 3.5, Prop 4.4). Both halves are proved in works this record has read. The shared shape — a linear representation that always exists, with classicality as its positivity — is the record's inference. Contextuality-by-Default gives a third instance, and one that does not need no-signalling: for every finite system of categorical random variables, signalling or not, a signed maximally connected quasi-coupling always exists ([LIT-777](../literature.d/LIT-777.md), Theorem 6.1), and noncontextuality is the existence of a nonnegative one (Theorem 4.1; [NOTE-600](../notes.d/NOTE-600.md)).

## What this does not say

- That the two representations are the same object. The sheaf section lives on global outcome assignments for one empirical model; the GPT representation lives on the state and effect spaces of a whole theory.
- That a sheaf-noncontextual empirical model yields a diagram-preserving ontological model of the corresponding GPT fragment, or the reverse.
- Anything beyond finite, tomographically local settings.
- **Whether a map between the formalisms exists.** A map from signed global
  sections to a GPT fragment's quasiprobability representation, or a proof
  that none preserves positivity, is [QUESTION-tmpx8hzz](../questions.d/QUESTION-tmpx8hzz.md).
