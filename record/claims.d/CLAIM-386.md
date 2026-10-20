---
number: 386
status: Active
formerly:
- CLAIM-tmp614wx
title: 'For x(t+1) = (A* + εC)x with A* block-diagonal, the Simon–Ando aggregate Â = QAV has one-step closure defect exactly QA − ÂQ = QA(I − VQ); the part from the blocks'' own dynamics vanishes iff every block has equal column sums, and then the whole defect is ε·QC(I − VQ)'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An algebraic error: a block-diagonal A* with equal column sums in each
  block, with V its blocks' leading eigenvectors normalized to sum one,
  for which QA*(I − VQ) ≠ 0; or a block with unequal column sums for which
  it is zero.
tags:
- complex-systems
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-221
grounds:
- LIT-1241
- THEORY-755
summary: >-
  Derived in the reading of Shpak, Stadler, Wagner and Altenberg (2004),
  [NOTE-977](../notes.d/NOTE-977.md), which states the Simon–Ando aggregate without an error
  term, and re-checked here. It splits the closure defect of block
  aggregates into a part from coupling between blocks, which is exactly
  first order in ε, and a part from the blocks' own dynamics, which
  vanishes exactly in the equitable case of [THEORY-755](../theory.d/THEORY-755.md). Deterministic
  dynamics, one step; the post-transient orders reported below are
  numerical, not part of the claim.
---

# CLAIM-386: For x(t+1) = (A* + εC)x with A* block-diagonal, the Simon–Ando aggregate Â = QAV has one-step closure defect exactly QA − ÂQ = QA(I − VQ); the part from the blocks' own dynamics vanishes iff every block has equal column sums, and then the whole defect is ε·QC(I − VQ)

## The claim

Let A = A* + εC with A* = diag(A*₁, …, A*_m). Let Q be the block-sum map
(Q_Ii = 1 for i in block I). Let V be the n × m matrix whose I-th column is
block I's leading eigenvector v_I, normalized so that 1ᵀv_I = 1, so
QV = I. The Simon–Ando aggregate, in the form [NOTE-977](../notes.d/NOTE-977.md) reads from
Shpak et al.'s (3.13b), is Â = QAV.

- **The identity.** D := QA − ÂQ = QA − QAVQ = QA(I − VQ). Since
  A = A* + εC, D = QA*(I − VQ) + ε QC(I − VQ).
- **The blocks' own part.** Block I's row of QA*(I − VQ) is
  1ᵀA*_I(I − v_I1ᵀ) on block I's coordinates. If every column of A*_I sums
  to λ, then 1ᵀA*_I = λ1ᵀ, and λ1ᵀ(I − v_I1ᵀ) = λ(1ᵀ − 1ᵀ) = 0.
  Conversely, if 1ᵀA*_I(I − v_I1ᵀ) = 0, then 1ᵀA*_I = (1ᵀA*_I v_I)1ᵀ, a
  constant row: the column sums are equal. Equal column sums is
  [THEORY-755](../theory.d/THEORY-755.md)'s column-equitability for the trivial partition of each
  block, and includes stochastic blocks.

So with equal column sums the one-step defect is exactly εQC(I − VQ).
Without them it has an O(1) part from the blocks themselves, which Simon
and Ando's argument relies on the fast transient to remove.

**The checks.** Three blocks of sizes 3, 4 and 3, with a random C. The
identity held to 2 × 10⁻¹⁶. The blocks' own part was 2.6 × 10⁻¹⁶ with
column-stochastic blocks, and 0.51 with unequal column sums. Measured on
states after 200 steps, the relative defect ‖Dx‖/‖QAx‖ was 5.6 × 10⁻⁵,
4.2 × 10⁻⁷ and 4.0 × 10⁻⁹ at ε = 10⁻², 10⁻³ and 10⁻⁴ with equal column
sums (second order), and 2.3 × 10⁻³, 1.7 × 10⁻⁴ and 1.6 × 10⁻⁵ without
(first order). Those orders are numerical. They rest on the standard
estimate that post-transient states lie within O(ε) of the slow subspace,
which was not proved here.

## What it does not say

- **No bound on dynamical dependence.** The defect is deterministic and
  one-step. For the information-theoretic version, for a block's full
  state, see [CLAIM-390](CLAIM-390.md).
- **Nothing about the length of the window.** Simon and Ando's
  aggregate is meant to hold between the end of the fast transient and the
  onset of global relaxation. This identity holds at every step, but the
  smallness of D on actual states needs the transient to have passed.
- **Not that Shpak et al. state it.** They give Â and no error term.
