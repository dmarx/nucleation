---
status: Proposed
title: 'Rate differences between levels, where they exceed the rate differences within a level, do two jobs in a hierarchy: the ratio of the rate within a level''s blocks to the rate between them is the margin by which the block aggregate is a slow manifold and the coarse variable closes, and its logarithm is the spacing between that level and the next in the tree the time geometry becomes; so dynamical hyperbolicity at every level makes the whole geometrically hyperbolic, which is how rate differences make hierarchical structure and not only mark it'
version: 3
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Restated before merging, at the owner's turn of 2026-11-20 preferring
    "rate differences" to "scale separation", and after the check of
    2026-11-20 (hyp6.py) that a designed hierarchy keeps its topology in the
    time geometry once the rate ratio between levels beats the spread of
    rates within them, and is rearranged otherwise. The title names that
    comparison in place of "one rate gap". Version 1's title: "One rate gap does two jobs in a hierarchy: at each level, the ratio of the rate between blocks to the rate within them is the margin by which the block aggregate is a slow manifold and the coarse variable closes, and its logarithm is the spacing between that level and the next in the tree the time geometry becomes; so dynamical hyperbolicity at every level makes the whole geometrically hyperbolic, which is how scale separation makes hierarchical structure and not only marks it".
- version: 3
  date: '2026-11-21'
  note: >-
    A dated note: the metastability and ultradiffusion readings support
    the closure side and add the branching to the condition. No change of
    status or title.
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A nearly decomposable system in which the
  between-to-within rate ratio that makes a block's aggregate close
  (CLAIM-386's ε) and the spacing of that block's level in the log
  commute-time geometry are set by different quantities, so that one can
  be large while the other is small. (b) A system in which the blocks
  CLAIM-157 counts as one system at some target do not appear as classes
  of the budgeted tree, or classes of the tree do not satisfy CLAIM-157's
  gap condition.
tags:
- complex-systems
- mathematics
- philosophy-of-biology
date: '2026-11-20'
line:
- distributed-agency
- realizability
- formal-apparatus
rests_on:
- CLAIM-tmpxi826
- CLAIM-tmp9lm3d
- CLAIM-478
- CLAIM-157
- CLAIM-386
- CLAIM-581
grounds:
- THEORY-1558
- THEORY-1306
- THEORY-1429
bears_on:
- QUESTION-281
summary: >-
  The owner, 2026-11-20, of the dynamical sense of hyperbolicity ("a level
  exists because of a rate gap"): "this connects us to entries about how
  scale separation drives structure formation". The assistant's reading:
  the gap that makes a level dynamically (normal hyperbolicity, Simon–Ando
  closure, [CLAIM-157](CLAIM-157.md)'s gap-isolated block) is the gap that spaces it in the
  tree-like time geometry [CLAIM-tmpxi826](CLAIM-tmpxi826.md) derives, so [CLAIM-478](CLAIM-478.md)'s "rate
  differences help make structure" has a formal sense: rate differences
  between levels that exceed those within make the state space's time
  geometry a hierarchy. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmph10k5 THEORY-tmppuotc — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpxi826 CLAIM-tmp9lm3d CLAIM-tmpdx6l8 — Proposed; filed in this contribution or the one it builds on -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-157 THEORY-1558 THEORY-1429 CLAIM-762 SYNTHESIS-048 SYNTHESIS-108 CLAIM-755 LIT-1638 — Proposed or Unfetched; the claims and readings this joins -->

# CLAIM-tmpy75jv: Rate differences between levels, where they exceed the rate differences within a level, do two jobs in a hierarchy: the ratio of the rate within a level's blocks to the rate between them is the margin by which the block aggregate is a slow manifold and the coarse variable closes, and its logarithm is the spacing between that level and the next in the tree the time geometry becomes; so dynamical hyperbolicity at every level makes the whole geometrically hyperbolic, which is how rate differences make hierarchical structure and not only mark it

## The claim

The owner, after the assistant distinguished the senses of hyperbolicity:
"this connects us to entries about how scale separation drives structure
formation".

**Job one: the level exists.** Within a block, states mix at a fast rate;
between blocks, at a slow one. The block occupations are then a slow
variable onto which the fast dynamics relax. In geometric terms the space of
block-constant laws is an attracting slow manifold, normally hyperbolic when
the transverse (within-block) rate dominates the tangential (between-block)
one ([THEORY-1429](../theory.d/THEORY-1429.md), after Fenichel). [CLAIM-386](CLAIM-386.md) gives the linear version: the
Simon–Ando aggregate closes to order ε, the coupling ratio. [CLAIM-157](CLAIM-157.md) makes
the same block "one system" while its gap beats the cost of naming it.
[THEORY-1306](../theory.d/THEORY-1306.md) and [THEORY-1558](../theory.d/THEORY-1558.md) (Juarrero, after Salthe, Allen and Starr): levels
are "demarcated by sharp discontinuities in characteristic process and
relaxation rates". In each, the quantity that makes the level is the ratio
of between-block to within-block rates.

**Job two: the level is a node of a tree.** [CLAIM-tmpxi826](CLAIM-tmpxi826.md): with rates
ε^U, the log commute-time geometry is within a constant of log(1/ε) times
the minimax-barrier ultrametric, so it becomes a tree as ε → 0. A block whose
exit barrier exceeds its internal barriers by Δu is a class of that tree,
separated from the next level by log(1/ε)·Δu, which is the logarithm of
the between-to-within rate ratio.

**The same number.** The ratio ε^(Δu) is the closure margin of job one and,
in logarithm, the spacing of job two. So a hierarchy of normally hyperbolic
levels is a hierarchy whose time geometry is Gromov-hyperbolic: dynamical
hyperbolicity level by level gives geometric hyperbolicity of the whole.
When the rates converge, both fail together: the aggregate stops closing and
the level stops showing in the geometry ([CLAIM-tmp9lm3d](CLAIM-tmp9lm3d.md)).

**Between against within.** What matters is not a gap alone but the gap
between levels set against the spread of rates within a level. In a designed
binary hierarchy whose within-level rates varied by factors up to e^h, the
time geometry's tree kept the designed topology in every run once the ratio
between levels, 1/g, beat that spread (roughly 1/g > e^(2h)), and was
rearranged, with as many classes added as lost, when it did not (curation
entry of 2026-11-20, 232905, hyp6.py). The rule was conservative at the
largest spread tried. Where the spread within a level beats the difference
between levels, the rates still make a tree, but not that hierarchy's.

## What it adds to the line on structure

- **[CLAIM-478](CLAIM-478.md)** holds, in its version of 2026-11-20, that rate differences
  help make structure and not only mark it: where some degrees of freedom
  settle faster than others by more than the rates vary among them, the
  relation they settle into is a constraint over the window between the
  rates. This
  claim gives the structure a shape: nested windows make a tree, the tree of
  [CLAIM-581](CLAIM-581.md)'s budgeted classes, and the time geometry is that tree.
- **[CLAIM-762](CLAIM-762.md) and [SYNTHESIS-108](../syntheses.d/SYNTHESIS-108.md)** (collapsing differences that do not matter
  into equivalence classes is how classes become units): the fast mixing
  within a block is the collapse; the budgeted classes are the equivalence
  classes it leaves; the tree is their nesting.
- **[SYNTHESIS-048](../syntheses.d/SYNTHESIS-048.md)** records that "coupling separates time scales only where
  it dissipates differences" and leaves open "how distinctions are made and
  unmade". This claim takes the separation as given; [CLAIM-tmp9lm3d](CLAIM-tmp9lm3d.md) says
  where, in a barrier model, distinctions are made and unmade.
- **The contraction thread** ([CLAIM-tmpdx6l8](CLAIM-tmpdx6l8.md)): a level's block occupations
  are conserved on the fast scale and forgotten on the slow one. A hierarchy
  is a nested sequence of approximately conserved parts, each lost on its own
  time scale ε^(−u).

## What it does not say

- Not that the normal-hyperbolicity side is proved here. The record has not
  read Fenichel ([LIT-1638](../literature.d/LIT-1638.md), Unfetched) and holds Kuehn's statement as a
  Proposed reading; the link to [CLAIM-tmpxi826](CLAIM-tmpxi826.md) is by the shared rate ratio.
- Not that every hierarchy is a time-scale hierarchy. [CLAIM-755](CLAIM-755.md) separates
  dynamical from economic separation; a hierarchy of reuse need not be a
  tree of time scales.
- Not that the blocks are produced by the system. The barriers are given;
  where they come from is [CLAIM-478](CLAIM-478.md)'s and [SYNTHESIS-048](../syntheses.d/SYNTHESIS-048.md)'s question.

## Note of 2026-11-21: the eigenvector side, and the branching

- **Closure, spectrally.** Bovier and colleagues ([THEORY-tmph10k5](../theory.d/THEORY-tmph10k5.md)) give each metastable point one low-lying eigenvalue whose eigenvector is near the indicator of its valley: the spectral form of a block aggregate closing. The ratio that matters there combines rates with valley masses and capacities, which depend on the shape of the space, not on rates alone.
- **The branching counts.** In Bachas and Huberman's ultradiffusion ([THEORY-tmppuotc](../theory.d/THEORY-tmppuotc.md)), relaxation within a subtree is stable only while the per-level rate ratio beats the branching (gb < 1); otherwise the subtree collapses to a single state. So the comparison this claim makes, between-level rate differences against within-level spread, needs a third term: the number of states in a block. This qualifies the claim; whether to restate it is left to its next revision.
