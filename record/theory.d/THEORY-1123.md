---
number: 1123
status: Active
formerly:
- THEORY-tmp1lvzk
title: 'In COTA''s formulation of causal abstraction learning as multi-marginal optimal transport, the term meant to impose do-calculus relations between the transport plans of comparable interventions depends only on the plans'' marginals and on normalisers built from them, which the transport constraints fix to the empirical distributions, so it is constant on the feasible set; its weight changes the solution only by rescaling the cost and entropy weights, and the paper''s evidence that the constraints help, a sweep over that weight, cannot separate the two'
version: 1
tags:
- causality
- mathematics
date: '2026-10-29'
source:
- LIT-1806
summary: >-
  Felekis, Zennaro, Branchini and Damoulas (CLeaR 2024), [LIT-1806](../literature.d/LIT-1806.md),
  eqs. (6), (9), (10), (12) and Appendices A–B, read in [NOTE-1342](../notes.d/NOTE-1342.md) from
  the arXiv preprint v1. A derivation from the paper's own equations,
  which state the term as a divergence between column (or row) sums of
  two plans; Theorem 1's proof writes it the same way. Active as
  mathematics about the problem as written. The released code, read but
  not run, builds a different problem for posets with several chains, in
  which the term acts on copies of plans that carry no marginal
  constraints.
---

# THEORY-1123: In COTA's formulation of causal abstraction learning as multi-marginal optimal transport, the term meant to impose do-calculus relations between the transport plans of comparable interventions depends only on the plans' marginals and on normalisers built from them, which the transport constraints fix to the empirical distributions, so it is constant on the feasible set; its weight changes the solution only by rescaling the cost and entropy weights, and the paper's evidence that the constraints help, a sweep over that weight, cannot separate the two

## Source

Felekis et al. (2024), [LIT-1806](../literature.d/LIT-1806.md), §4 (pp. 5–8), §6 (Fig. 2 and Table 1,
p. 10) and Appendices A–B (pp. 14–16) of arXiv 2312.08107v1; read in
[NOTE-1342](../notes.d/NOTE-1342.md).

## What was actually shown

**The problem as written.** For each intervention ι in a maximal chain, a
plan P^ι in the transport polytope U(π_ι): its column sums equal the base
model's empirical distribution under ι and its row sums the abstracted
model's under ω(ι) (eq. 6, p. 6). COTA minimises
Σ_ι κ⟨C_ω, P^ι⟩ + λᵀD(P^ι, P^{ι+1}) − μH(P^ι) over these plans, with κ, λ,
λ′, μ ≥ 0 summing to 1 (eq. 12, p. 7).

**The term.** D = [δ, δ′]. The base part is
δ_{ι,η}(P^ι, P^η) = d(Σ_i P^η_{ij}, (1/Z^η_j) Σ_i P^ι_{ij}) over columns
compatible with η (eq. 9), the abstracted part the same on rows (eq. 10).
The normaliser Z^η is a ratio of sums of entries of P^ι over index sets
fixed by conditions on the base state x_j (eq. 17, p. 14), and Z^{ω(η)}
the same on rows.

**The derivation.** Every quantity inside δ is a sum of entries of P^ι or
P^η over whole columns, so it is a function of the column marginals; δ′
is a function of the row marginals. On U(π) those marginals are the data.
So D(P^ι, P^η) has one value on the feasible set. The minimiser of eq. (12)
is then the minimiser of Σ κ⟨C_ω, P^ι⟩ − μH(P^ι), which depends on (κ, λ,
μ) only through μ/κ, and λ enters that ratio only through the constraint
κ + λ + λ′ + μ = 1. The proof of Theorem 1 states the term in this form,
δ(P_n, P_{n+1}) = d(P_n 1, P_{n+1} 1), with P_n 1 "the marginals of P_n"
(p. 15).

**What the paper offers as evidence.** Fig. 2 (p. 10) sweeps (κ, λ, μ)
over the simplex and finds high error near λ = 0: "demonstrating the
benefit of the do-calculus constraints in the OT problem". Moving along
that simplex at fixed μ/κ would not change the plans; moving λ at fixed μ
changes μ/κ. The figure does not hold μ/κ fixed. In Table 1 (p. 10) the
best COTA setting and the baseline with independent plans and no causal
term have the same Wasserstein error, 0.011.

**What could have failed.** The normalisers could have depended on
entries of a plan other than through whole-column sums, or the marginal
constraints could have been relaxed; either would have made the term act.
Eq. (17)'s index sets are defined by conditions on x_j (or x′_i) only, and
eq. (12) keeps the plans in U(π).

## What this does not say

- **That COTA's results are wrong.** The errors reported are what the
  method produced. They are explained by the ω-cost and the entropy
  weight, not by the causal term ([THEORY-1137](THEORY-1137.md)).
- **That the released code solves eq. (12).** Read without running, it
  puts every chain into one problem and gives a plan marginal constraints
  only the first time its intervention appears; later appearances are new
  variables without them, coupled by the δ term ([NOTE-1342](../notes.d/NOTE-1342.md)). There the
  term can act. That variant is not described in the paper.
- **Anything about Approximate COTA** (Appendix F), whose element-wise term
  does depend on the plans' entries.
- **That do-calculus constraints cannot help abstraction learning.** A
  formulation in which they couple the entries of the plans, or a joint
  plan over interventions, is untested here.
