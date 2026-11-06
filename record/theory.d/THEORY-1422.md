---
number: 1422
status: Active
formerly:
- THEORY-tmprk262
title: 'Botnan and Lesnick report that multiparameter persistence modules are of wild representation type, so that no barcode-like complete invariant is practical and good barcodes need not exist, while the interleaving distance extends the bottleneck distance with stability and universality but is NP-hard to compute for two or more parameters'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    The thirtieth status review: Proposed → Active, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The survey was
    read in full in every part the title draws on (NOTE-1568, now Read),
    and each clause of the promote_when holds: wild type is stated (§1.1,
    §8.2, Theorem 8.9), Example 4.6 gives a module with no good barcode
    (its proof checked, scratch/formal/botnan_lesnick_checks.py), Theorem
    6.7 states stability and, over prime fields, universality, and §1.2
    and Theorem 6.9 state NP-hardness with its source. The title reports
    the survey; it draws on the statements, and on a proof only for
    Example 4.6, which the survey gives. Nothing on the record contradicts
    it. Title unchanged. Old promote_when, verbatim: "A reading confirms
    that the survey states wild representation type for multiparameter
    modules over commutative grids, gives an example of a module with no
    good barcode, states stability and universality of the interleaving
    distance with its hypotheses (prime fields), and states, with a
    source, that computing the interleaving distance is NP-hard for two or
    more parameters." Removed on promotion. The body gains Theorem 6.9's
    hypotheses and Theorem 8.9's finite and tame grids.
tags:
- mathematics
date: '2026-11-05'
source:
- LIT-2022
summary: >-
  Botnan & Lesnick (2022; EMS 2023), [LIT-2022](../literature.d/LIT-2022.md), read in
  [NOTE-1568](../notes.d/NOTE-1568.md). Active: the title reports what the survey states; the
  NP-hardness and wild-type results are cited from the literature, not
  proved in it. It is a report of the field. It does not say
  anything about direction, paths or the cost of traversal.
---
# THEORY-1422: Botnan and Lesnick report that multiparameter persistence modules are of wild representation type, so that no barcode-like complete invariant is practical and good barcodes need not exist, while the interleaving distance extends the bottleneck distance with stability and universality but is NP-hard to compute for two or more parameters

## Source

Botnan & Lesnick (2022; 2023), [LIT-2022](../literature.d/LIT-2022.md); read in [NOTE-1568](../notes.d/NOTE-1568.md).

## What was actually shown

- **Wild type** (§1.1, §8.2): stated, with Drozd's trichotomy (§8.1);
  "the representation type of a commutative grid is wild even for small
  grid sizes".
- **No good barcode** (Example 4.6): proved by a short contradiction on a
  3 × 3 grid.
- **Incomplete rank invariant** for N² (§4.2).
- **Stability and universality** (§6.1; Theorem 6.7, prime fields).
- **NP-hardness** (§1.2): reported from the literature for n ≥ 2. Theorem
  6.9 states it more exactly: over a finite field, approximating the
  interleaving distance between 2-parameter modules within a factor of 3
  is NP-hard (Bjerkevik, Botnan and Kerber 2019).

## What this does not say

- That multiparameter modules cannot be compared: the metrics are well
  behaved, only hard to compute.
- That useful incomplete invariants are lacking: several are surveyed.
- Anything about direction or reachability.
- That every grid is wild: small grids are of finite or tame type
  (Theorem 8.9: finite for m = 1 or n = 1 and for (2,2), (2,3), (2,4),
  (3,2), (4,2); tame for (2,5), (3,3), (5,2)). The survey's "wild
  representation type" is the general case.
- That NP-hardness is proved here, or for every field: Theorem 6.9, cited
  from Bjerkevik, Botnan and Kerber, is stated for finite fields and two
  parameters, and covers approximation within a factor of 3.
