---
number: 743
status: Active
formerly:
- THEORY-tmp35hmc
title: 'For finite X and Y, every information-bottleneck optimum at every β gives one encoder to all inputs sharing p(y|x), so it is a stochastic coarsening of the minimal sufficient partition (the causal states of memoryless transduction); as β → ∞ the optima converge to that partition, but in general no finite β attains it, except when Y is a function of X'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-976. The β → ∞ identification is the
    paper's, which calls it evident and gives no proof. The proofs below
    are the record's, written out step by step, which meets the condition
    for Active under ADR-047 v2. They are the limit against stochastic
    encoders, the factoring at finite β, the binary symmetric
    counterexample and the deterministic case. The averaging inequality and
    the counterexample were also checked numerically in the scratchpad.
tags:
- information-theory
- mathematical-statistics
date: '2026-10-20'
source:
- LIT-1240
- LIT-338
answers:
- QUESTION-tmpt5ucu
summary: >-
  Shalizi and Crutchfield ([LIT-1240](../literature.d/LIT-1240.md), read in [NOTE-976](../notes.d/NOTE-976.md)) assert that the
  information bottleneck recovers the causal states as β → ∞. The record
  proves it, against stochastic encoders as well as partitions, and adds
  that every finite-β optimum factors through those states. So the IB
  hierarchy always nests under its top. It says nothing about whether
  optima at two finite β nest. Finite alphabets only.
---
<!-- inactive-ok-file: THEORY-157 THEORY-163 — Proposed; connections named for context, nothing here rests on them -->
# THEORY-743: For finite X and Y, every information-bottleneck optimum at every β gives one encoder to all inputs sharing p(y|x), so it is a stochastic coarsening of the minimal sufficient partition (the causal states of memoryless transduction); as β → ∞ the optima converge to that partition, but in general no finite β attains it, except when Y is a function of X

## Source

Shalizi and Crutchfield (2002; arXiv 2000), [LIT-1240](../literature.d/LIT-1240.md), read in full in
[NOTE-976](../notes.d/NOTE-976.md), Sections III–VI. The IB functional is Tishby, Pereira and
Bialek's ([LIT-338](../literature.d/LIT-338.md), [NOTE-300](../notes.d/NOTE-300.md)). The paper asserts the β → ∞ identification
("evident"). The proofs below are the record's.

## What was actually shown

**Setting.** X and Y are finite, with p(x) > 0 for every x. An encoder is
q(x̃|x) on a finite alphabet T, and
F_β(q) = I(X̃; X) − β I(X̃; Y), with X̃ → X → Y a Markov chain. The
**causal partition** ε groups x with x′ iff p(·|x) = p(·|x′). It is the
minimal sufficient partition of X for Y. Write C = H(ε(X)), and assume
|T| ≥ the number of cells, so ε is a feasible encoder.

**1. Every optimum factors through ε, at every β > 0.** Take any encoder q,
and replace its rows on each cell c by their average
q̄_c = Σ_{x∈c} p(x|c) q(·|x).

- *p(x̃, y) is unchanged.* For x ∈ c, p(y|x) = p_c(y). So
  Σ_{x∈c} p(x) q̄_c(x̃) p_c(y) = Σ_{x∈c} p(x) q(x̃|x) p(y|x). Summing over
  cells gives the same joint law of (X̃, Y), so I(X̃; Y) and H(X̃) are
  unchanged.
- *I(X̃; X) does not increase.* I(X̃; X) = H(X̃) − Σ_x p(x) H(q(·|x)).
  Within a cell, Σ_{x∈c} p(x) H(q(·|x)) ≤ p(c) H(q̄_c), by concavity of
  entropy. Strict concavity makes the inequality strict unless all rows in
  the cell are equal.

So averaging strictly lowers F_β unless q is already constant on every
cell. Every minimizer is constant on cells, which means X → ε(X) → X̃ is a
Markov chain. Checked numerically: over 2,000 random encoders and random β
on a five-input example, averaging never raised F.

**2. As β → ∞, the optima converge to ε.** Let q_β be a minimizer. One
exists, since F_β is continuous on a compact set. Comparing it with ε gives
I_X(q_β) − β I_Y(q_β) ≤ C − β I(X; Y). Two bounds follow.

- I(X; Y) − I_Y(q_β) ≤ C/β, using I_X ≥ 0.
- I_X(q_β) ≤ C, using I_Y ≤ I(X; Y).

Let q* be any limit point. By continuity, I_Y(q*) = I(X; Y) and
I_X(q*) ≤ C.

- *Each code word sees only one cell.* By the chain rule,
  I(X̃, X; Y) = I(X; Y) + I(X̃; Y|X) = I(X; Y), and also
  I(X̃, X; Y) = I(X̃; Y) + I(X; Y|X̃). So I(X; Y|X̃) = 0. Then for x̃ and x
  with q*(x̃|x) > 0, p(y|x̃) = p(y|x, x̃) = p(y|x). So every x that x̃ can
  come from lies in one cell, and ε(X) = f(X̃) almost surely.
- *Its information equals C.* By data processing,
  I(X̃; X) ≥ I(f(X̃); X) = I(ε(X); X) = C. So I_X(q*) = C.
- *It is ε up to splitting.* Equality in data processing gives
  I(X̃; X | ε(X)) = 0. So X̃ is ε(X), relabelled, with each label possibly
  split by noise independent of X within the cell.

This also settles the limiting problem the paper states. Among all encoders
(not only partitions) that keep all of I(X; Y), the least I(X̃; X) is C,
and it is attained only by ε up to that splitting.

**3. In general no finite β attains it.** Take X uniform on {0, 1} and Y
equal to X flipped with probability p = 0.1, so ε is the identity. Let the
encoder flip X with probability δ. Then I_X = 1 − h(δ) and
I_Y = 1 − h(p ∗ δ), where p ∗ δ = p(1 − δ) + (1 − p)δ. So
dF/dδ = −h′(δ) + β(1 − 2p) h′(p ∗ δ). As δ → 0⁺, this tends to −∞,
because h′(δ) = log₂((1 − δ)/δ) → ∞ while the second term stays finite. So
the identity is not optimal at any finite β. Numerically, the best δ is
1.5 × 10⁻⁴ at β = 5, 2.3 × 10⁻⁸ at β = 10 and 3.5 × 10⁻¹² at β = 15. The
standard iterative algorithm nevertheless converges to the identity at
β ≥ 10, because its multiplicative updates cannot leave a zero entry.

**4. When Y is a function of X, it is attained for every β > 1.** By data
processing, I(X̃; X) ≥ I(X̃; Y). So F_β ≥ (1 − β) I(X̃; Y). For β > 1, the
bound I(X̃; Y) ≤ H(Y) gives F_β ≥ (1 − β) H(Y), and ε attains it. For
β < 1, the same inequality gives F_β ≥ 0, so the trivial encoder is
optimal. The solution path has only these two points.

What could have failed: a stochastic encoder could have kept all of
I(X; Y) with less than C bits about X, so that the limit was not a
partition at all. Step 2 rules this out. The factoring could also have
failed at small β, with optima mixing inputs that the causal partition
separates in ways not expressible as a function of the cell. Step 1 rules
this out.

## What this does not say

- **Not that optima at two finite β nest.** Step 1 places every finite-β
  optimum under the β = ∞ one. It says nothing about β₁ < β₂ < ∞, which is
  [QUESTION-220](../questions.d/QUESTION-220.md)'s case. Within the quotient by ε, the finite-β problem
  is a general IB problem, and nothing here constrains its path.
- **Not that finite-β optima are partitions.** Step 3 shows they need not
  be. Deterministic-encoder results (the deterministic IB) are a different
  problem.
- **Not anything for continuous variables or for processes with memory.**
  For a stationary process, the analogue of step 2 needs a finite
  statistical complexity and a choice of future length. The paper defers
  transducers with memory.
- **Not that the paper proves it.** The paper asserts the limit and is
  silent on steps 1, 3 and 4.
- **Not that the iterative algorithm finds these optima.** It finds
  stationary points, and step 3 shows it can stop at a deterministic one
  that is not optimal.

## Connections

- **[QUESTION-220](../questions.d/QUESTION-220.md): answers in part.** The IB family always nests under
  its β → ∞ end, so the coarse-to-fine reading is safe with respect to the
  finest level. It is untested between finite levels. A search for
  incomparable optima must use a stochastic p(y|x) (step 4) and stochastic
  encoders (step 3).
- **[CLAIM-152](../claims.d/CLAIM-152.md).** The whole hierarchy, every β, is a function of ε, and ε is
  fixed by Y. A change of target changes every level at once.
- **[THEORY-157](THEORY-157.md).** With p(y) > 0, ε is the classical minimal sufficient
  statistic of the finite model y ↦ p(x|y) (likelihood-ratio partition), so
  it is the FinStoch case of Fritz's theorems with Y as the parameter.
- **[THEORY-668](THEORY-668.md).** There nesting is imposed by restricting encoders to
  prunings of a fixed hierarchy. Here nesting under the top level holds
  without that restriction.
- **[THEORY-163](THEORY-163.md).** Its annealed colour-naming hierarchy lies, at every β,
  under the partition of colour chips by their meaning distributions.
