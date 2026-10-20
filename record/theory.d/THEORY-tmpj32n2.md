---
status: Active
title: 'For a linear system x(t+1) = Ax and a partition of its variables, the vector of block sums evolves autonomously from every initial state iff the partition is column-equitable, every column of each block of A summing to the same value; the aggregate operator then keeps a subset of A''s eigenvalues, and the blocks may interact as strongly as they like, so exact aggregation is not decomposition'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpl2r9w. The condition is the paper's
    (1.10)–(1.11), the spectral inclusion its Theorem 2.1 (cited there from
    Stadler and Tinhofer). Both are re-derived below step by step, which
    meets the condition for Active under ADR-047 v2. The example that the
    blocks may interact strongly, and the identification with THEORY-733,
    are the record's.
tags:
- complex-systems
- mathematics
date: '2026-10-20'
source:
- LIT-tmp6vpg9
answers:
- QUESTION-tmplru2n
summary: >-
  Shpak, Stadler, Wagner and Hermisson (2004), [LIT-tmp6vpg9](../literature.d/LIT-tmp6vpg9.md), read in
  [NOTE-tmpl2r9w](../notes.d/NOTE-tmpl2r9w.md). Exact aggregation of a linear system by the sums over a
  partition holds for every state iff the partition is column-equitable, a
  symmetry condition, not a weak-coupling one. Linear dynamics and
  partition-based aggregation only. It says nothing about approximate
  aggregation, the Simon–Ando case, or nonlinear systems, where the paper
  itself shows aggregations with no linear counterpart.
supports:
- CLAIM-tmp614wx
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; the block criterion this account is contrasted with, open -->
# THEORY-tmpj32n2: For a linear system x(t+1) = Ax and a partition of its variables, the vector of block sums evolves autonomously from every initial state iff the partition is column-equitable, every column of each block of A summing to the same value; the aggregate operator then keeps a subset of A's eigenvalues, and the blocks may interact as strongly as they like, so exact aggregation is not decomposition

## Source

Shpak, Stadler, Wagner and Hermisson (2004), *Theory in Biosciences*
123(1):33–68, [LIT-tmp6vpg9](../literature.d/LIT-tmp6vpg9.md), read in full in [NOTE-tmpl2r9w](../notes.d/NOTE-tmpl2r9w.md) from the authors'
manuscript. The condition is the paper's (1.10)–(1.11). The spectral
inclusion is its Theorem 2.1, which it cites from Stadler and Tinhofer
(2000). The derivations below are the record's.

## What was actually shown

Let x(t+1) = Ax(t) in ℝⁿ, and let C₁, …, C_m (1 ≤ m < n) partition the
variables. Q is the m × n matrix with Q_Ii = 1 if i ∈ C_I and 0 otherwise,
so y = Qx is the vector of block sums.

**The condition.** The block sums evolve autonomously from every initial
state iff y(t+1) is a function of y(t) alone. Since the map is linear, that
means QA = ĀQ for some m × m matrix Ā.

- *If.* Suppose that for every pair I, J, the sum s_IJ = Σ_{i∈C_I} A_ij is
  the same for every j ∈ C_J (column-equitability). Then
  (QA)_Ij = Σ_{i∈C_I} A_ij = s_IJ = (ĀQ)_Ij with Ā = (s_IJ). So
  y(t+1) = QAx(t) = ĀQx(t) = Āy(t).
- *Only if.* If QA = ĀQ, then for j ∈ C_J,
  Σ_{i∈C_I} A_ij = (QA)_Ij = (ĀQ)_Ij = Ā_IJ, which does not depend on which
  j ∈ C_J. That is column-equitability.

QQᵀ is the diagonal matrix of block sizes, so Ā = QAQᵀ(QQᵀ)⁻¹, the paper's
(1.2a).

**The spectrum.** If wᵀĀ = λwᵀ with w ≠ 0, then (wᵀQ)A = wᵀĀQ = λ(wᵀQ). And
wᵀQ ≠ 0, because Q has full row rank. So every eigenvalue of Ā is an
eigenvalue of A. The paper's landscape example shows the multiplicities
falling to one (Fig. 1).

**Aggregation is not decomposition.** Column-equitability constrains block
sums, not their size. With A = αI + β(11ᵀ − I), every partition is
column-equitable: each cross-block column sum is β|C_I|, and each
within-block one is α + β(|C_I| − 1). So every partition aggregates exactly
for any β, including β ≥ α, where coupling between blocks is as strong as
coupling within them. Re-checked numerically as a VAR(1) with Gaussian noise
([NOTE-tmpl2r9w](../notes.d/NOTE-tmpl2r9w.md)): the transfer entropy from the six units into the pair of
three-unit block sums was zero to machine precision.

What could have failed: aggregability could have needed more than a
condition on column sums, such as conditions on the within-block
distribution of the state. The paper's (1.10) shows that it does for a
single fixed state. For all states, it reduces to column sums alone.

## What this does not say

- **Not that a single block's sum closes.** The vector of all block sums
  closes. One block's sum alone generally depends on the others: in the
  uniform example its transfer entropy was 5.0 × 10⁻² at
  (α, β) = (0.2, 0.1).
- **Not anything approximate.** Nearly equitable partitions, and the
  Simon–Ando case of weak coupling between blocks, have no bound here. The
  paper treats Simon–Ando as a limiting case without one.
- **Not about aggregations that are not partitions.** Eigenvector
  aggregations (the paper's Results 1.1–1.2) close without being
  partitions, and [THEORY-733](THEORY-733.md) covers every linear map.
- **Not about nonlinear systems.** The paper's own Wagner–Laubichler
  example aggregates genotype classes in relative frequencies that do not
  aggregate in the linear representation.

## Connections

- **[THEORY-733](THEORY-733.md).** Exact aggregation ĀQ = QA is [THEORY-733](THEORY-733.md)'s VAR(1)
  criterion L A = B L with L = Q. So in a linear Gaussian VAR(1), a
  partition's block sums are jointly exactly dynamically independent iff
  the partition is column-equitable. This is the partition case of
  [THEORY-733](THEORY-733.md), for the joint vector of block sums.
- **[CLAIM-tmpkoi6k](../claims.d/CLAIM-tmpkoi6k.md).** The uniform-coupling system in [CASE-tmpvt6wb](../cases.d/CASE-tmpvt6wb.md) is
  aggregable along every partition, though none is a block. The claim is
  about the sum of all units and about blocks, and stands.
- **[QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md): answers in part.** It asks whether a boundary test's
  unit should be a subset of members or a function of the whole state.
  This gives a third kind: a partition of members whose group summaries
  jointly close while the groups interact strongly. It does not say
  whether such a partition is one system or several.
- **[CLAIM-157](../claims.d/CLAIM-157.md) and [THEORY-661](THEORY-661.md).** Equitability is a symmetry condition and
  near-decomposability a weak-coupling one. They select different
  partitions, and only the second is a block.
