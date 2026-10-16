---
number: 668
status: Active
formerly:
- THEORY-tmpxbuz6
title: "When the encoder is restricted to prunings of one fixed hierarchy of nested partitions, any non-negatively weighted sum of relevant information, irrelevant information and compression decomposes into per-node terms, so a bottom-up recursion finds the unique optimal tree with fewest leaves exactly in linear time, while greedy top-down splitting can miss information lying below a level that carries none; penalising irrelevant information only prunes the information-bottleneck tree"
version: 1
tags:
- information-theory
- operations-research
date: '2026-10-16'
source:
- LIT-868
summary: >-
  Larsson, Maity & Tsiotras (2022), [LIT-868](../literature.d/LIT-868.md), read in full in [NOTE-676](../notes.d/NOTE-676.md),
  every proof followed step by step. The decomposition is the chain rule
  for refinements, and the recursion is the classic bottom-up pruning of
  a fixed tree. [NOTE-676](../notes.d/NOTE-676.md) declined a THEORY as exact but narrow; it is
  filed because the reading supports it as stated and its greedy-failure
  point bears on how hierarchy is measured. The hierarchy is given, not
  found, and the evaluation is one image.
---

<!-- inactive-ok-file: QUESTION-025 THEORY-163 THEORY-186 CLAIM-092 CLAIM-119 — Open or Proposed; named for what this result bears on, nothing here rests on them -->

# THEORY-668: When the encoder is restricted to prunings of one fixed hierarchy of nested partitions, any non-negatively weighted sum of relevant information, irrelevant information and compression decomposes into per-node terms, so a bottom-up recursion finds the unique optimal tree with fewest leaves exactly in linear time, while greedy top-down splitting can miss information lying below a level that carries none; penalising irrelevant information only prunes the information-bottleneck tree

## Source

Larsson, Maity & Tsiotras (2022), "A Generalized Information-Theoretic
Framework for the Emergence of Hierarchical Abstractions", *Entropy*,
[LIT-868](../literature.d/LIT-868.md), read in full in [NOTE-676](../notes.d/NOTE-676.md) from the PMC copy. Algorithms 1 and 2
are images and were not seen; they are known from the prose.

## What was actually shown

**Setting.** X lives on the finest cells of a d-dimensional grid of side
2^ℓ; the encoder T is a deterministic pruning of the full quadtree, so
I(T;X) = H(T). The objective weights relevant variables Y_i by β_i ≥ 0,
irrelevant variables Z_j by γ_j ≥ 0, and compression by α ≥ 0.

**Decomposition (Eqs. 13–21).** Splitting a cell t adds p(t)·JS of the
children's conditionals p(y|t′) to the information about each variable,
and p(t)·H(Π) to the rate. So the objective of any pruning is the sum of
ΔJ over its interior nodes.

**Recursion (Eq. 22, Lemmas 6–10, Theorem 11).** G(t) = max{ΔJ(t) +
Σ_children G(t′), 0}. Expanding a leaf iff G > 0 returns the optimal
tree, every strict subtree of which is strictly worse, and that tree is
unique. Cost is of order (n + m + 3) times the number of finest cells.

**Greedy failure (§6.1, Fig. 4).** A greedy search expands t only when β
exceeds H(Π)/JS. In a symmetric 4 × 4 example JS = 0 at the root, so the
greedy tree is the root alone for every β, although the grid holds
relevant information below.

**Nesting (Lemma 12, Corollary 13).** For fixed β, every node the
information-bottleneck-with-side-information search expands, the plain
IB search also expands. [NOTE-676](../notes.d/NOTE-676.md) derives, by the same induction, that the
trees are also nested across α.

What could have come out otherwise: the optimum over prunings could have
needed a search over all subtrees. The decomposition makes it a single
pass.

## What this does not say

- **That hierarchy is found in data.** The quadtree is fixed in advance;
  the objective chooses only how deep to go in each region. Partitions
  that cut across its cells are excluded.
- **That the objective respects shared or synergistic information.** Each
  relevant variable's information is counted separately, from pairwise
  marginals, so shared information is double counted and synergy among
  the Y_i is invisible. Penalising I(T;Z₁) and I(T;Z₂) separately does not
  bound I(T;Z₁,Z₂), so the privacy reading guarantees less than §4
  suggests ([NOTE-676](../notes.d/NOTE-676.md)'s observation).
- **That the abstractions are useful for planning.** One segmented road
  image, no baseline, no downstream task (C6, weak).
- **How to choose the weights.** They are set by hand.
- **That it extends to general trees as proved.** The authors say it
  "applies straightforwardly"; the proofs use only parent–child
  structure, but that is asserted, not shown.

## Connections

- [QUESTION-025](../questions.d/QUESTION-025.md) asks whether correlated or hierarchical attributes still
  give linear directions in an embedding. [NOTE-676](../notes.d/NOTE-676.md) judges this no
  answer, but one point carries: a level carries information about Y
  exactly where sibling cells differ, weighted by their mass, and it can
  sit below a level that carries none, so a test of recovered hierarchy
  should score each level, not only the first split.
- In colour naming ([THEORY-163](THEORY-163.md)), annealing β finds a hierarchy by
  bifurcation with soft encoders; here the hierarchy is imposed and the
  nesting holds by construction.
- Saxe et al.'s tree case ([THEORY-186](THEORY-186.md)) and [CLAIM-119](../claims.d/CLAIM-119.md)'s cross-cutting
  attributes mark what a partition hierarchy cannot represent.
- [CLAIM-092](../claims.d/CLAIM-092.md)'s designed objective, a weighted sum of separately computed
  mutual informations, has a precedent here, solved exactly over a
  structured encoder class.
