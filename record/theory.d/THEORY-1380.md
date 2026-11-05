---
number: 1380
status: Proposed
formerly:
- THEORY-tmp8numn
promote_when: >-
  A reading of the main proofs (§§5–9 of arXiv v11, or the J. ACM version)
  or of a refereed account that checks them confirms that the algorithm,
  combining local consistency with linear algebra over prime fields, solves
  every CSP over a finite language on a finite domain preserved by a weak
  near-unanimity operation in polynomial time; the J. ACM text's Theorem 1.4
  is checked to match arXiv v11.
title: 'Zhuk shows, independently of Bulatov, that for a finite set of relations on a finite domain, deciding satisfiability is solvable in polynomial time if a weak near-unanimity operation preserves every relation and is NP-complete otherwise, by an algorithm that combines local consistency with linear algebra over prime fields'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2023
summary: >-
  Zhuk (2017; J. ACM 2020), [LIT-2023](../literature.d/LIT-2023.md), read in part in [NOTE-1555](../notes.d/NOTE-1555.md) (the
  introduction, outline, definitions, Theorem 5.1 with proof and the
  conclusions). Proposed: the main proofs were not read. It is about
  deciding existence of a solution, for fixed finite languages on finite
  domains. It does not say anything about infinite domains, where the
  author shows CSPs can be undecidable, about quantified CSPs, or about the
  connectivity of the solution space.
---
<!-- inactive-ok-file: NOTE-1555 — Skimmed and new; cited from the reading of Zhuk (2020) as open -->

# THEORY-1380: Zhuk shows, independently of Bulatov, that for a finite set of relations on a finite domain, deciding satisfiability is solvable in polynomial time if a weak near-unanimity operation preserves every relation and is NP-complete otherwise, by an algorithm that combines local consistency with linear algebra over prime fields

## Source

Zhuk (2017; J. ACM 2020), [LIT-2023](../literature.d/LIT-2023.md); read in [NOTE-1555](../notes.d/NOTE-1555.md).

## What was actually shown

- **The theorem** (Theorem 1.4, p. 3): "CSP(Γ) can be solved in polynomial
  time if there exists a WNU preserving Γ; CSP(Γ) is NP-complete
  otherwise."
- **The hardness half** is earlier work (Theorem 1.3, from [47]); the
  algorithm is the paper's.
- **The structural theorem** (Theorem 5.1, p. 17, proof read): four ways a
  finite algebra with a special WNU can be reduced, the last leaving Z_p.
- **The algorithm** (§2, outline read): local consistency and domain
  reductions, then linear equations over prime fields; its correctness
  proofs (§§6–9) were not read.
- **Independence**: Bulatov's proof ([LIT-2115](../literature.d/LIT-2115.md)) appeared at the same time
  and the two algorithms are "significantly different" (p. 3).

## What this does not say

- Anything for infinite domains: "the situation is changing significantly"
  (§10.4), and some such CSPs are undecidable.
- That the algorithm is polynomial in the domain size: it is exponential in
  it (§10.1), polynomial for a fixed language.
- That the algebra governs other questions over the same language: for
  quantified CSPs the classification is open and not a clean dichotomy
  (§10.6).
- Anything about the solution space's connectivity or reconfiguration;
  "linked" in the paper is a local-consistency notion.
- That the Pol–Inv correspondence is a Galois connection: standard, but not
  stated in the paper.
