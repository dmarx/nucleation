---
number: 239
status: Active
formerly:
- THEORY-tmp1iy33
title: "For any joint law of an input and a context, symmetric or not, the top-d left singular functions of the conditional-expectation operator attain the minimum, over d-dimensional spans, of worst-case linear-probe approximation error over tasks of compatibility at least 1 − ε, namely (s₁² − (1 − ε)²)/(s₁² − s²_{d+1}) when s_{d+1} < 1 − ε ≤ s₁, though other spans can tie"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-239.yaml, batch 012, ADR-047).
    The title called the top-d left singular span "the unique" minimizer.
    That is false. With s = (1, 0.9, 0.8, 0.5, 0.1), ε = 0.15 and d = 2,
    the span of μ₁ and cos θ·μ₂ + sin θ·μ₄ has the same worst-case error,
    0.7708, for every θ up to at least 0.5. The title now says the top span
    attains the minimum and that other spans can tie, and it states the
    range of ε in which the formula holds. The promote_when asked for a
    second, independent derivation of Theorem 3.4 for a general joint law,
    and a worked non-reversible case on one space. The note of 2026-10-19
    below gives both. The derivation uses only the singular value
    decomposition, and the worked case is a three-state chain. Under
    ADR-047 v2 (the owner's rule of 2026-10-19), that meets the condition
    for the narrowed claim.
- version: 3
  date: '2026-10-21'
  note: >-
    QUESTION-052 was split under ADR-049, and this entry's answers link
    moves to the Answered child, QUESTION-tmp5o5m0. The summary, the "does
    not say" line on one space and the Connections paragraph on
    QUESTION-052 said the directed case on one space was not worked. The
    note of 2026-10-19 works it, so they now say so. Title and status are
    unchanged.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-14'
source:
- LIT-975
summary: >-
  Zhai (2025), [LIT-975](../literature.d/LIT-975.md), read in [NOTE-770](../notes.d/NOTE-770.md): Lemma 1.4, Theorem 3.2 and
  Theorem 3.4 with App. B. The operator g ↦ E[g(A)|X] runs from L²(P_A) to
  L²(P_X) and is never assumed self-adjoint; its singular value
  decomposition comes from composing it with its adjoint. The guarantee is
  for linear probes and approximation error at the population level only.
  The thesis never works a non-reversible kernel on one space; the note of
  2026-10-19 works a three-state one. It says nothing of what a trained
  network reaches.
answers:
- QUESTION-tmp5o5m0
---
<!-- inactive-ok-file: THEORY-005 CLAIM-098 — Proposed; accounts and a claim this one bears on, open -->

# THEORY-239: For any joint law of an input and a context, symmetric or not, the top-d left singular functions of the conditional-expectation operator attain the minimum, over d-dimensional spans, of worst-case linear-probe approximation error over tasks of compatibility at least 1 − ε, namely (s₁² − (1 − ε)²)/(s₁² − s²_{d+1}) when s_{d+1} < 1 − ε ≤ s₁, though other spans can tie

## Source

Zhai, *Contextures: The Mechanism of Representation Learning* (CMU PhD
dissertation, 2025), [LIT-975](../literature.d/LIT-975.md), read in [NOTE-770](../notes.d/NOTE-770.md): Definition 1.1,
Lemmas 1.4–1.5, Definitions 1.7 and 3.1, Theorems 3.2 and 3.4 (proofs in
App. B.1–B.2), Theorems 2.9 and 2.11 (App. A.5–A.6).

## What was actually shown

**The operator.** For a joint law P⁺(x,a) of an input X and a context A on
possibly different spaces, (T_P⁺g)(x) = E[g(A)|x] maps L²(P_A) to L²(P_X).
Its adjoint is written out by Bayes' rule: (T_P⁺*f)(a) = E[f(X)|a]. Assuming
T_P⁺T_P⁺* and T_P⁺*T_P⁺ Hilbert–Schmidt, both are self-adjoint by
construction, share eigenvalues s_i² ∈ [0,1], and their eigenfunctions
μ_i, ν_i are linked by μ_i = s_i⁻¹T_P⁺ν_i (Lemma 1.4). The density ratio has
the expansion P⁺(x,a)/(P_X(x)P_A(a)) = Σ s_i μ_i(x)ν_i(a) (Lemma 1.5).

**The task class.** A target f is (1 − ε)-compatible when
(Σ s_i²u_i² / Σ u_i²)^(1/2) ≥ 1 − ε for f̃ = Σ u_iμ_i. Such an f is
E[g(A)|x] for a g that varies little across two context draws for the
same x: E[(g(A) − g(A′))²] ≤ 4ε‖g‖² (Theorem 3.2).

**The guarantee.** If 1 − ε ≤ s₁, then among all d-dimensional encoders in
L²(P_X), one whose span is that of the top-d left singular functions
μ₁…μ_d minimizes the worst-case linear-probe approximation error over the
compatible class, and when s_{d+1} < 1 − ε the minimum is
(s₁² − (1 − ε)²)/(s₁² − s²_{d+1}). Every other encoder has a compatible
task with at least that error (Theorem 3.4). The thesis states the
optimality as "if and only if". The "only if" fails: other spans can tie
(note of 2026-10-19). The proof (App. B.2) builds,
for any d-dimensional span, a unit target β₁μ₁ + β₂f₀ with f₀ in
span{μ₂, …, μ_{d+1}} that is compatible and reaches the bound, and shows
equality only when the span is that of μ₁…μ_d.

**How the span is reached.** At their population optima, the spectral
contrastive loss and the covariance-constrained non-contrastive loss give
an encoder on A spanning the top right singular functions, whose average
T_P⁺Ψ spans the left ones (Theorem 2.9); a two-encoder objective,
min E‖Φ(X) − Ψ(A)‖² with Cov[Φ] = I imposed on Φ only, reaches the left
span directly (Theorem 2.11).

What could have failed: the optimal encoder could have depended on the
context's right space, or on how the pair is symmetrized, and it does not.
Only the left singular space and the singular values enter.

## What this does not say

- **Not that the optimal span is unique.** A span that tilts μ_d towards
  μ_{d+2} can match the worst case, because the worst target lies in the
  plane of μ₁ and μ_{d+1}. That holds even with a gap s_d > s_{d+1}.
- **Not a directed transport worked in the thesis.** X and A may differ,
  and the operator is not self-adjoint, but the thesis never works a case
  where A = X with a non-reversible kernel. Its only graph example
  (Example 1.13, Theorem 2.8) assumes w(u,v) = w(v,u). The record's note
  of 2026-10-19 works one, a three-state chain. The guarantee there
  follows from the general statement; the example shows only that the
  left and right functions differ.
- **Not about what training reaches.** All results are at the population
  optimum of squared-error objectives; the thesis sets aside optimization
  and architecture, and does not cover cross-entropy or InfoNCE.
- **Not about BYOL or SimSiam.** The two-encoder objective is asymmetric
  only in where the constraint sits. The thesis names predictor and
  stop-gradient methods but does not analyse them.
- **Not estimation error.** Theorem 3.4 bounds approximation by a linear
  probe on an exact span; finite-sample bounds (Chapter 5) depend on a
  context complexity that grows exponentially in input dimension for
  masking contexts.
- **Not a measure of a context's quality.** The thesis's claim that a
  moderate association is best is argued and tested with a heuristic
  metric that fails on some datasets; it is not part of this account.

## Connections

- **[QUESTION-tmp5o5m0](../questions.d/QUESTION-tmp5o5m0.md)**, split from [QUESTION-052](../questions.d/QUESTION-052.md). The answer, for linear
  decisions, to what replaces the eigenspace when the pairing is not
  symmetric. It is the left singular space of the conditional-expectation
  operator, with a sufficiency guarantee for linear decisions on
  compatible tasks, on two spaces or on one (note of 2026-10-19). It is a
  minimax-optimal span, not the only one. Nonlinear decisions stay with
  [QUESTION-052](../questions.d/QUESTION-052.md).
- **[THEORY-009](THEORY-009.md).** It complicates that account. Self-adjointness here comes
  from composing T_P⁺ with its adjoint (X → A → X′), not from any symmetry
  of the original pair. In the multi-view case the two views are
  exchangeable because both are drawn given the same x, which is the
  symmetry [THEORY-009](THEORY-009.md) names. The adjoint is closed-form, with no Riesz. It
  is a nearer miss for [THEORY-009](THEORY-009.md)'s promote_when than [LIT-228](../literature.d/LIT-228.md), but not a
  BYOL-type objective.
- **[THEORY-007](THEORY-007.md).** The symmetric sibling: the same top span, with a
  minimax guarantee over view-invariant targets instead of compatible ones.
- **[THEORY-228](THEORY-228.md).** A different guarantee on the same object in the
  symmetric, finite case: cluster leakage over conductance rather than a
  worst case over a compatibility class.
- **[THEORY-005](THEORY-005.md).** The Hilbert–Schmidt condition is assumed here; the
  thesis's context complexity is the same χ² quantity taken pointwise.
- **[CLAIM-098](../claims.d/CLAIM-098.md).** Translation is directed; this account shows a signature
  survives an asymmetric pairing between two spaces, which is weaker than
  surviving a non-invertible transport on one.
- The training objectives themselves are ML practice and are held in the
  Anthology ([ANTH-LIT-459](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-459.md)), not here.

## Note of 2026-10-19: the guarantee re-derived, its uniqueness refuted, and a non-reversible case

Let T have singular triples (s_i, μ_i, ν_i), with the μ_i extended by an
orthonormal basis of ker T* (s = 0 there). Nothing below uses symmetry of
the pair. A unit target f = Σ u_iμ_i is (1 − ε)-compatible when
Σ s_i²u_i² ≥ (1 − ε)². The error of a span V is e(V), the supremum over
compatible f of ‖f − P_V f‖². Assume s_{d+1} < 1 − ε ≤ s₁, and put
r* = (s₁² − (1 − ε)²)/(s₁² − s²_{d+1}).

**The top span attains r*.** For U_d = span{μ₁…μ_d}, the residual is
ρ = Σ_{i>d} u_i². The compatibility is then at most (1 − ρ)s₁² + ρs²_{d+1},
so ρ ≤ r*. The target √(1 − r*)·μ₁ + √r*·μ_{d+1} attains it.

**No span does better.** Let V be any d-dimensional span. span{μ₁…μ_{d+1}}
has dimension d + 1, so it holds a unit h ⊥ V. Write
h = cos ψ·μ₁ + sin ψ·w with w a unit vector in span{μ₂…μ_{d+1}},
0 ≤ ψ ≤ π/2, and q = Σ s_i²⟨w, μ_i⟩² ≥ s²_{d+1}. The target
f_φ = cos φ·μ₁ + sin φ·w is compatible iff
sin²φ ≤ ρ_w = (s₁² − (1 − ε)²)/(s₁² − q), and ρ_w ≥ r*. Its error is at
least ⟨f_φ, h⟩² = cos²(φ − ψ). If sin²ψ ≤ ρ_w, take φ = ψ, for error 1.
Otherwise take sin²φ = ρ_w with φ < ψ, so cos²(ψ − φ) ≥ sin²φ = ρ_w ≥ r*.
If 1 − ε ≤ s_{d+1}, every span has error 1.

**Uniqueness fails.** Take s = (1, 0.9, 0.8, 0.5, 0.1), ε = 0.15 and d = 2,
so r* = 0.7708. Let V = span{μ₁, cos θ·μ₂ + sin θ·μ₄}. Its error was
computed through the dual of the quadratic program,
min over λ ≥ 0 of λ_max(I − P_V + λ(diag s² − (1 − ε)²I)), and bounded
below by 4×10⁵ sampled targets. It equals r* at θ = 0.05, 0.2 and 0.5, and
rises to 0.973 only at θ = 1. Tilting is free while
sin²θ/(s₁² − s_d²) + cos²θ/(s₁² − s²_{d+2}) ≤ 1/(s₁² − s²_{d+1}), because
the worst target still lies in the μ₁–μ_{d+1} plane. For small θ
that holds whenever s_{d+2} < s_{d+1}, so the tie is the usual case, not
an accident of these numbers.

**A non-reversible case on one space.** Take A = X = {1, 2, 3}, with the
kernel P(a | x) given by the rows (0.1, 0.8, 0.1), (0.1, 0.1, 0.8) and
(0.6, 0.2, 0.2), at its stationary law π = (0.287, 0.338, 0.374). Then
P⁺(x, a) ≠ P⁺(a, x), so the pair is not reversible. The singular values
are (1, 0.655, 0.534). The second left and right singular functions
differ: μ₂ ∝ (−1.30, 1.23, −0.11) and ν₂ ∝ (−0.11, −1.20, 1.17). Targets
are functions of x, in L²(P_X), so the guarantee above sits on the left
functions μ_i, as the general statement says.
