---
number: 2251
status: Proposed
formerly:
- THEORY-tmp3va8j
promote_when: >-
  The lattice theorem is checked: on a small network, all balanced
  partitions enumerated by computer form a lattice under refinement with a
  unique coarsest element, and a pair of balanced partitions whose
  intersection is not balanced is exhibited (Example 5·5 or another).
title: 'Balanced synchrony patterns form a lattice'
statement: >-
  Stewart shows that on any coupled cell network of finite type the balanced
  equivalence relations, the patterns of synchrony invariant under every
  dynamics the architecture admits, form a complete lattice under refinement
  whose join is that of equivalence relations but whose meet is not
  intersection, with a unique coarsest element computable from input trees
version: 1
tags:
- mathematics
- network-science
date: '2026-11-22'
source:
- LIT-2249
extends:
- THEORY-1065
bears_on:
- QUESTION-147
summary: >-
  From the reading of [LIT-2249](../literature.d/LIT-2249.md) in [NOTE-2342](../notes.d/NOTE-2342.md), for [LEAD-023](../leads.d/LEAD-023.md). Structure
  on the candidates for robust synchrony; nothing on which of them attract.
  Proposed until its promote_when is met.
---

# THEORY-2251: Balanced synchrony patterns form a lattice

## Source

Stewart (2007), [LIT-2249](../literature.d/LIT-2249.md), read in [NOTE-2342](../notes.d/NOTE-2342.md).

## What was actually shown

A proof through the order-reversing bijection between balanced relations
and flow-invariant polydiagonals, whose intersections are again
polydiagonals; an eight-cell counterexample to closure under
intersection; a characterization of the top element on the universal
cover.

## What this does not say

Which balanced patterns are stable or observed. That the meet has a simple
combinatorial form.
