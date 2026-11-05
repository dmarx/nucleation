---
number: 1375
status: Proposed
formerly:
- THEORY-tmp57bxg
promote_when: >-
  A reading of the version of record confirms Theorems 1, 2, 4 and 6 and
  Propositions 1 and 2 as stated here, and no later erratum withdraws one
  of them.
title: 'Ito, Demaine, Harvey, Papadimitriou, Sideri, Uehara and Uno show that deciding whether one feasible solution can be turned into another through feasible solutions differing in one element at a time is PSPACE-complete for the reconfiguration versions of many NP-complete problems and polynomial for some problems in P such as matroid bases and matchings, and that minimising or maximising the worst intermediate objective is NP-hard to approximate in some cases and 2-approximable in others'
version: 1
tags:
- operations-research
- mathematics
date: '2026-11-05'
source:
- LIT-2104
summary: >-
  Ito et al. (2011), [LIT-2104](../literature.d/LIT-2104.md), read in [NOTE-1595](../notes.d/NOTE-1595.md) (main text in
  full; the matching algorithm and the proofs of Lemmas 3–4 and Theorem 7
  skimmed). Proposed: most PSPACE-hardness proofs in the paper are
  sketches, and the copy read is the article-in-press PDF posted by a
  co-author. It does not say that reconfiguration is always harder than
  search, nor anything about how long the paths are or how to find them,
  since the problems are decision problems about existence.
---

# THEORY-1375: Ito, Demaine, Harvey, Papadimitriou, Sideri, Uehara and Uno show that deciding whether one feasible solution can be turned into another through feasible solutions differing in one element at a time is PSPACE-complete for the reconfiguration versions of many NP-complete problems and polynomial for some problems in P such as matroid bases and matchings, and that minimising or maximising the worst intermediate objective is NP-hard to approximate in some cases and 2-approximable in others

## Source

Ito et al. (2011), [LIT-2104](../literature.d/LIT-2104.md); read in [NOTE-1595](../notes.d/NOTE-1595.md).

## What was actually shown

- **Membership** (§2.1): reconfiguration of any NP search problem is in
  NPSPACE, hence PSPACE by Savitch's theorem.
- **Hardness** (Theorems 1 and 2): power supply reconfiguration, by
  reduction from satisfiability reconfiguration; independent set, clique,
  vertex cover, set cover and 0–1 integer programming reconfiguration,
  independent set and vertex cover even on planar graphs of maximum
  degree 3. Theorem 2's proofs are sketches.
- **Polynomial cases** (Propositions 1 and 2): matroid bases within a
  weight bound connect by |B0 \ Bt| exchanges; matching reconfiguration is
  in P.
- **The worst intermediate state** (§4): maxmin clique reconfiguration has
  no constant-factor approximation unless P = NP (Theorem 4); minmax power
  supply is strongly NP-hard even with two supply vertices (Lemma 3);
  minmax set cover has a linear-time 2-approximation through C0 ∪ Ct
  (Theorem 6).

## What this does not say

- That reconfiguration is harder than search in every case: matroid bases
  and matchings are in P for both, and the paper shows no case where search
  is hard and reconfiguration easy (Gopalan et al. do).
- Anything about path length, or about constructing a path: the problems
  ask only whether one exists.
- That the §4 problems are PSPACE-hard to approximate; the authors leave it
  open.
- Anything about continuous or physical reconfiguration.
