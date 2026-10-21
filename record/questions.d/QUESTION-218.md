---
number: 218
status: Open
formerly:
- QUESTION-tmplru2n
title: 'Can a collective mode that is dynamically closed, but is not a weakly coupled block of the units carrying it, be one system, and if so what should a boundary test take as the unit: a subset of members or a function of the whole state?'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A6–A9 built their paper on the two
    warnings this question records from THEORY-820; closed coarse-grainings
    are neither upward- nor downward-closed in the refinement order
    (CLAIM-tmpshzxc), and no independent mark of unity was offered. The
    question is unchanged.
tags:
- individuation
- complex-systems
- mathematics
date: '2026-10-19'
line: distributed-agency
refines:
- QUESTION-035
summary: >-
  A5 of the exchange of 2026-10-19 on coarse-to-fine processes, its
  candidate Q2: "Does organizational unity require a subsystem boundary, or
  can it arise from a dynamically closed collective mode distributed
  across multiple otherwise entangled subsystems?" [CLAIM-388](../claims.d/CLAIM-388.md) shows
  the two come apart; [CASE-120](../cases.d/CASE-120.md) is the construction. The question is
  which of them the record's "one system" should track.
answered_by:
- THEORY-755
- THEORY-758
- THEORY-820
- THEORY-822
---
<!-- inactive-ok-file: CLAIM-157 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
<!-- inactive-ok-file: TERM-tmpfezzd — Proposed; cited in the note of 2026-10-21, nothing here rests on it -->
# QUESTION-218: Can a collective mode that is dynamically closed, but is not a weakly coupled block of the units carrying it, be one system, and if so what should a boundary test take as the unit: a subset of members or a function of the whole state?

## Why it is a question

[CLAIM-157](../claims.d/CLAIM-157.md)'s unit is already a projector, "the pair's joint mode, not
either member" ([CLAIM-164](../claims.d/CLAIM-164.md)), but it is found by grouping members into a
block whose edge is weakly coupled. [THEORY-257](../theory.d/THEORY-257.md)'s candidates are "linear
subspaces mixing all units, not partitions". A5, after Shpak et al.
([LIT-1242](../literature.d/LIT-1242.md), read in [NOTE-979](../notes.d/NOTE-979.md)): aggregation, a map whose dynamics close, is not
decomposition, a split into weakly coupled subsets, and "systems that are
both aggregable and decomposable are a special case."

[CLAIM-388](../claims.d/CLAIM-388.md) makes the split exact. In [CASE-120](../cases.d/CASE-120.md), with uniform
coupling, the sum of all units is closed at every coupling strength, and
no partition is nearly decomposable. So a block test finds nothing below
the whole and a closure test finds the mode.

## What the record holds

- [CLAIM-157](../claims.d/CLAIM-157.md), [CLAIM-164](../claims.d/CLAIM-164.md) and [THEORY-661](../theory.d/THEORY-661.md) on the block side.
- [THEORY-257](../theory.d/THEORY-257.md) and [THEORY-733](../theory.d/THEORY-733.md) on the closure side.
- A third kind of unit, from Shpak et al. ([THEORY-755](../theory.d/THEORY-755.md), read
  2026-10-20): a partition of members whose block sums jointly close, which
  happens iff the partition is column-equitable, while the blocks interact
  strongly. In [CASE-120](../cases.d/CASE-120.md) every partition is one. It is a grouping of
  members, as a block is, and closed, as a mode is, and it is neither.
- Published cases of the same kind ([NOTE-977](../notes.d/NOTE-977.md)). On a single-peak
  fitness landscape, Hamming-distance classes aggregate exactly although
  their members "did not communicate with one another at all". Schema
  marginals close on the linkage-equilibrium manifold although rates
  between classes are as large as rates within them.
- Coarse levels of an operator ([THEORY-758](../theory.d/THEORY-758.md), diffusion wavelets). Each
  level is an exactly closed subspace, but its localized basis is a choice
  the level does not fix. On three tight clusters the localized scaling
  functions each sat on one cluster. On a circle, with no gap, no
  localized coarse basis exists. So closure belongs to the subspace, and
  blockhood to a basis that only a gap supplies, as [CLAIM-157](../claims.d/CLAIM-157.md) and
  [CLAIM-164](../claims.d/CLAIM-164.md) would have it.
- Rosas et al. (2024, [LIT-1306](../literature.d/LIT-1306.md), read in [NOTE-1030](../notes.d/NOTE-1030.md)) take the
  unit to be a function of the whole state, up to computational
  equivalence. Informational closure, causal closure and Barnett–Seth
  dynamical independence coincide ([THEORY-820](../theory.d/THEORY-820.md)); for a partition of a
  Markov chain, closure is strong lumpability, the equitable condition of
  [THEORY-755](../theory.d/THEORY-755.md) on Pᵀ ([THEORY-822](../theory.d/THEORY-822.md)). Two warnings: closure is cheap, since
  an i.i.d. noise component is closed; and two closed coarse-grainings
  taken together need not be closed, contrary to the paper's sublattice
  claim. The paper offers no independent mark of unity.
- [CLAIM-157](../claims.d/CLAIM-157.md)'s guard: clearing a test is not being an agent or a self. A5
  kept it: "A newly discovered distributed collective mode should not
  automatically be treated as an individual, much less an agent."

## What would count as an answer

A5's table gives the four cells: strong block and strong closure, block
without closure, closure without block, neither. An answer says which cells
the record's "one system" covers, with an independent mark of unity
([CLAIM-157](../claims.d/CLAIM-157.md)'s compensation under perturbation, or entrainment) measured in a
closure-without-block case. If the mode compensates and entrains and the
block test misses it, that meets [CLAIM-157](../claims.d/CLAIM-157.md)'s `defeated_if` ("forms that do
compensate and entrain but never clear it"). If it does not, the block is
the better unit and closure tracks something else.

## Note of 2026-10-21: closure gives no mereology, and is monotone in neither direction

The exchange of 2026-10-20 (A6–A9) built its paper on the two warnings
this question already records from [THEORY-820](../theory.d/THEORY-820.md). A6 called the second "the
biggest discovery". Two facts were checked from the exact three-bit chain.
(A, C) and (B, C) are closed, though (A, B) is not, and A⊕B, a coarsening
of (A, B), is not closed (1 bit), so the closed coarse-grainings are
neither upward- nor downward-closed in the refinement order. That is filed
as [CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md), with the reason: refinement changes the future that
closure asks to be predicted. A8 and A9 drew from this that closure
"cannot be a sufficient criterion" of a unit or an agent, which is this
question's open half and [CLAIM-157](../claims.d/CLAIM-157.md)'s guard, and offered no independent
mark of unity either. [TERM-tmpfezzd](../terms.d/TERM-tmpfezzd.md) separates the senses of "closure" the
exchange ran together.
