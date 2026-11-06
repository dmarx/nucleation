---
status: Proposed
promote_when: >-
  A proof, or an independent computation on generic triangulations that are
  not H1, that the number of real branches of nearly-flat configurations
  meeting at the flat state of a four-boundary-vertex triangulated rigid
  origami is 2^Vi, and that the branches pair with the patterns of vertex
  popping states up to global sign.
title: 'A flat triangulated rigid origami sits at a singular point of its configuration space where generically 2^Vi folding branches meet, one pair for each pattern of vertex popping states, so folding from flat is exponentially ambiguous'
version: 1
tags:
- mathematics
- natural-sciences
date: '2026-11-06'
source:
- LIT-2021
extends:
- THEORY-1427
summary: >-
  The generalization Chen and Santangelo (2018), LIT-2021, assert from
  numerics, split from THEORY-1427 when the twenty-seventh status review
  narrowed that reading to what was computed and proven (ADR-047 kind 1,
  ADR-065). Proven only for Henneberg-1 triangulations, a vanishing fraction
  of all.
---

# THEORY-tmpcpymq: A flat triangulated rigid origami sits at a singular point of its configuration space where generically 2^Vi folding branches meet, one pair for each pattern of vertex popping states, so folding from flat is exponentially ambiguous

## Source

Chen and Santangelo (2018), LIT-2021, read in NOTE-1614 (main text in full, appendices skimmed).

## What was actually shown

What THEORY-1427 reports: the count of 2^Vi branches, two for each pair of a vertex popping pattern and its global reversal, found by numerical root-finding on random four-boundary-vertex triangulations with Vi from 2 to 8, with a few exceptions that contain triangulated triangles, and proven to all orders for triangulations built by Henneberg-1 moves. This entry asserts the count for generic triangulations.

## What this does not say

- That second-order solutions are always configurations; the authors know of no general guarantee.
- Anything about more than one degree of freedom, or about how branches join away from the flat state.
- How often a real sheet misfolds; that is inferred, not measured.
