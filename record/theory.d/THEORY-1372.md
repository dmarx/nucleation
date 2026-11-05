---
number: 1372
status: Proposed
formerly:
- THEORY-tmp34oop
promote_when: >-
  A second reading, of the journal version or of arXiv 2410.07666,
  confirms the statements of Theorems 1, 2, 4, 5 and 7 as given here, and
  no later erratum withdraws one of them.
title: 'Eppstein shows that folding problems split by question: deciding whether a finite crease pattern folds flat is fixed-parameter tractable in ply and treewidth with an ETH-optimal dependence on treewidth, reaching one flat state from another in a hinged-square toy model is PSPACE-complete and counting its states #P-complete, and flat-foldability of self-similar crease patterns with infinitely many creases on a finite square is undecidable'
version: 1
tags:
- mathematics
- operations-research
date: '2026-11-05'
source:
- LIT-2063
summary: >-
  Eppstein (2025), [LIT-2063](../literature.d/LIT-2063.md), read in [NOTE-1611](../notes.d/NOTE-1611.md) (main text and all
  theorem statements in full; the §6 gadgets and the proofs of Lemmas 7–10
  skimmed). Proposed: the gadget constructions behind Theorems 6 and 7
  were not checked. It does not say that flat folding is NP-complete
  because of this paper (that is earlier work), nor anything about
  continuous rigid folding of one sheet, since the PSPACE result is for a
  toy model of hinged squares with discrete moves.
---

# THEORY-1372: Eppstein shows that folding problems split by question: deciding whether a finite crease pattern folds flat is fixed-parameter tractable in ply and treewidth with an ETH-optimal dependence on treewidth, reaching one flat state from another in a hinged-square toy model is PSPACE-complete and counting its states #P-complete, and flat-foldability of self-similar crease patterns with infinitely many creases on a finite square is undecidable

## Source

Eppstein (2025), [LIT-2063](../literature.d/LIT-2063.md); read in [NOTE-1611](../notes.d/NOTE-1611.md).

## What was actually shown

- **Finding a flat state** (Theorems 1 and 2): a dynamic program over a
  tree decomposition of the cell adjacency graph runs in (p!)^O(w) n²;
  under ETH no 2^o(w) algorithm exists, even for ply O(1).
- **Reaching one** (Theorem 4): in flaps and flips, squares each hinged
  along one edge to a tabletop, pairwise and global connectivity are
  PSPACE-complete, even for bounded treewidth, by reduction from planar
  nondeterministic constraint logic.
- **Counting** (Theorem 5): counting flaps-and-flips states is #P-complete
  under polynomial-time counting reductions.
- **Infinite patterns** (Theorem 7): flat-foldability of a pattern that
  repeats one finite crease set in each tile of the square binary tiling
  is undecidable; Theorem 6 gives coRE-completeness with a finite partial
  folding fixed.
- The paper also proves (Theorem 3) that exact 3D folded shapes of
  integer-edged bipyramids cannot be computed by radicals or bounded-degree
  roots; the title leaves it out.

## What this does not say

- That this paper proves NP-hardness of flat folding. It cites it.
- That reconfiguration of a single folded sheet, by continuous rigid
  motion, is PSPACE-complete. Flaps and flips is a toy model of separate
  uncreased squares with discrete moves that need not be rigid.
- That counting is #P-complete under parsimonious reductions; the author
  leaves that open.
- That flat folding with finitely many creases is undecidable.
