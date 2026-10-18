---
status: Active
title: 'Two competing components with interaction matrix A = [[1, ρ], [ρ, 1]]: with equal growth rates their invasion growth is 1 − ρ, the smallest eigenvalue of the Gram matrix, and with growth rates 1 ± δ the same matrix supports coexistence only when |δ| < (1 − ρ)/(1 + ρ), so feature geometry alone does not fix coexistence'
version: 1
standing: fictional
kind: construction
tags:
- ecology
- mathematics
- learning-theory
date: '2026-10-18'
line: distributed-agency
supports:
- CLAIM-tmpc36bo
summary: >-
  From the synthesis the owner relayed on 2026-10-18, checked. The
  two-component Lotka–Volterra system with symmetric overlap ρ: invasion
  growth 1 − ρ equals λ_min(A), and κ(A) = (1 + ρ)/(1 − ρ), so overlap
  weakens recovery and ill-conditions the features together. Holding A
  fixed and setting r = (1 + δ, 1 − δ) gives the coexistence equilibrium
  n* = (1/(1 + ρ) ± δ/(1 − ρ)), feasible only when |δ| < (1 − ρ)/(1 + ρ).
  The same representation geometry supports coexistence under one supply
  and exclusion under another.
---

# CASE-tmptwfjg: Two competing components with interaction matrix A = [[1, ρ], [ρ, 1]]: with equal growth rates their invasion growth is 1 − ρ, the smallest eigenvalue of the Gram matrix, and with growth rates 1 ± δ the same matrix supports coexistence only when |δ| < (1 − ρ)/(1 + ρ), so feature geometry alone does not fix coexistence

## The construction

Two components with abundances n₁, n₂ ≥ 0 and

  ṅ_i = n_i (r_i − (An)_i),  A = [[1, ρ], [ρ, 1]],  0 ≤ ρ < 1.

A is the Gram matrix of two unit feature vectors at inner product ρ.

**Equal growth rates, r₁ = r₂ = 1.** Component 1 alone settles at
n₁ = 1. A rare component 2 then grows at r₂ − ρn₁ = 1 − ρ, and by symmetry
the same holds the other way. The eigenvalues of A are 1 ± ρ, so
λ_min(A) = 1 − ρ, and κ(A) = (1 + ρ)/(1 − ρ). As overlap ρ → 1, the
invasion advantage vanishes and the feature system becomes
ill-conditioned together.

**Unequal growth rates, r = (1 + δ, 1 − δ), same A.** Solving An = r:

  n₁* = 1/(1 + ρ) + δ/(1 − ρ),  n₂* = 1/(1 + ρ) − δ/(1 − ρ).

The equilibrium is feasible, both positive, only when
|δ| < (1 − ρ)/(1 + ρ). Outside that range one component excludes the
other with the Gram matrix unchanged. Checked at ρ = 0.5, δ = 0.1:
n* = (0.867, 0.467), bound 0.333; eigenvalues 0.5 and 1.5; κ = 3.

## What it shows

The kernel is not enough to determine coexistence. One must also know
what resources, tasks or evaluative opportunities the system supplies.
That is CLAIM-152's target-relativity applied to persistence: what a
representation supports depends on what it is asked for.

It separates three things an experiment on QUESTION-083 could conflate:

- **structural differentiation**, measured from feature geometry (ρ, the
  Gram spectrum; THEORY-004, CLAIM-193);
- **functional differentiation**, measured by conditional performance
  across contexts;
- **dynamical stabilization**, measured by recovery when rare and by
  persistence.

A feature can be geometrically distinct without being useful. A specialist
can be useful without enough influence to survive. And differentiated
specialists can persist without any higher-level governance.
