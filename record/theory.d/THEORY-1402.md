---
number: 1402
status: Proposed
formerly:
- THEORY-tmpj5wcc
promote_when: >-
  The two reductions, from Partition for foldability using all creases and
  from 1-in-3 SAT for foldability with optional creases, checked in the
  journal version or confirmed by an independent proof.
title: 'Akitaya, Demaine, Horiyama, Hull, Ku and Tachi prove that deciding whether a crease pattern can fold rigidly from flat is NP-hard: weakly when every crease must fold, and strongly when creases are optional'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2071
summary: >-
  Akitaya et al. (2020), [LIT-2071](../literature.d/LIT-2071.md), read in [NOTE-1579](../notes.d/NOTE-1579.md) (model and
  main text in full, reduction gadgets skimmed). Proposed: the gadget
  constructions behind Theorems 15 and 16 were not checked line by line. It
  does not say that the problem is in NP in general, which is open, or
  anything about the mechanics of folding a real sheet.
---

# THEORY-1402: Akitaya, Demaine, Horiyama, Hull, Ku and Tachi prove that deciding whether a crease pattern can fold rigidly from flat is NP-hard: weakly when every crease must fold, and strongly when creases are optional

## Source

Akitaya et al. (2020), [LIT-2071](../literature.d/LIT-2071.md); read in [NOTE-1579](../notes.d/NOTE-1579.md).

## What was actually shown

- **The model** (§2): rigid foldability near flat is the loop condition,
  crease rotations multiplying to the identity around every closed
  vertex-avoiding curve, which there is necessary and sufficient.
- **The reduction's core** (§3): flat-foldable degree-4 vertices have two
  modes meeting only at flat (Theorem 6), and a mode assignment folds
  exactly when every face's speed coefficients multiply to 1
  (Corollary 11).
- **Weak hardness** (Theorem 15): finite-precision degree-4 flat-foldable
  foldability using all creases is weakly NP-hard, from Partition; that
  class is in NP (Theorem 13).
- **Strong hardness** (Theorem 16): foldability with optional creases is
  strongly NP-hard, from 1-in-3 SAT.

## What this does not say

- That rigid foldability is in NP in general; it is in ∃R, and a tight
  bound is open.
- That the hardness comes from self-intersection; near flat there is none.
- Anything about whether a self-folding material can be programmed to fold
  along a path that exists.
