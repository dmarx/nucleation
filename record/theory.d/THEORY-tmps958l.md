---
status: Active
title: 'For symmetric matrices compared under squared loss, co-optimal transport with independent row and column couplings is a lower bound on the Gromov–Wasserstein value, and for squared Euclidean distance matrices the two are equal and share optimal couplings, because GW is then a concave quadratic program whose bilinear relaxation is tight; for other symmetric matrices the bound can be strict'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-29'
source:
- LIT-tmpbnbe3
summary: >-
  Redko, Vayer, Flamary and Courty (2020), [LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md), Propositions 2–3,
  read in [NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md) from arXiv v3. Proved via Konno's theorem on
  concave quadratic programs and checked numerically, including strict
  inequality for non-Euclidean symmetric matrices. Active. It does not say
  COOT's two couplings coincide at every optimum, nor that either is
  unique.
---

# THEORY-tmps958l: For symmetric matrices compared under squared loss, co-optimal transport with independent row and column couplings is a lower bound on the Gromov–Wasserstein value, and for squared Euclidean distance matrices the two are equal and share optimal couplings, because GW is then a concave quadratic program whose bilinear relaxation is tight; for other symmetric matrices the bound can be strict

## Source

Redko, Vayer, Flamary and Courty (2020), [LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md), §3 and §§C.1–C.3,
pp. 5, 13–16 of arXiv 2002.03731v3; read in [NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md).

## What was actually shown

**The bound.** GW(C, C′) minimizes ⟨L(C, C′) ⊗ π, π⟩ over one coupling.
COOT(C, C′, w, w′, w, w′) minimizes ⟨L(C, C′) ⊗ π^s, π^v⟩ over two
couplings with the same marginals. Setting π^s = π^v gives every GW plan as
a COOT plan, so COOT ≤ GW for any symmetric C, C′ (Prop. 3, p. 5; proof p.
15).

**The equality.** For L = |·|² and squared Euclidean distance matrices
C = x1ᵀ + 1xᵀ − 2XXᵀ, the GW objective is a quadratic in vec(π) with Hessian
−4 XXᵀ ⊗_K X′X′ᵀ, which is negative semi-definite (Prop. 2, Lemma 1, p.
14). Konno's theorem (Theorem 1, p. 13): for a positive semi-definite Q,
maximizing cᵀx + ½xᵀQx over a polytope equals maximizing
½cᵀx + ½cᵀy + ½xᵀQy over pairs, and optimal points correspond. Applied
here, "if (π∗s , π∗v ) is an optimal solution of (1), then both π∗s , π∗v
are solutions of (3). Conversely, if π∗s is an optimal solution of (3),
then (π∗s , π∗s ) is an optimal solution for (1)" (p. 5).

**The algorithmic corollary.** In that case one may set π^s = π^v in the
block coordinate descent. The iteration becomes a DC algorithm identical to
Frank–Wolfe for GW, with line-search step 1 (Algorithms 3–5, pp. 15–16).

**Checked.** By enumerating all permutation pairs (exact for uniform
weights and equal sizes, since a bilinear program attains its optimum at a
pair of vertices): on five random pairs of 5-point squared-distance
matrices the COOT value equalled the GW value over permutations (exact
here, since a concave program attains its minimum at a vertex). On five
random symmetric non-Euclidean pairs COOT was strictly lower in three. In
three further such pairs, 40 Frank–Wolfe restarts over the whole polytope
found GW values of 1.78, 4.42 and 1.15 against exact COOT values of 1.39,
4.14 and 0.91.

**What could have failed.** The bilinear relaxation could have been loose
for squared Euclidean matrices, with an optimal COOT pair whose components
were not GW-optimal. Konno's argument rules that out given the
semi-definite Hessian.

## What this does not say

- **That an optimal COOT pair has π^s = π^v.** Only that each component is
  GW-optimal. When GW has several optimal plans, a pair of two different
  ones is not excluded by the proposition. In my check on a square's
  squared-distance matrix, all 8 optimal permutation pairs had π^s = π^v,
  because the zero diagonal penalizes mismatched pairs.
- **That either plan is unique.** GW's plans are determined only up to the
  symmetries of the two structures ([THEORY-tmpa43ta](THEORY-tmpa43ta.md)), and the equality
  carries those over.
- **Anything about COOT on raw data matrices.** That is the general case
  where COOT is not a GW problem at all ([THEORY-tmpvn82m](THEORY-tmpvn82m.md)).
- **That COOT is easier.** Exact COOT is NP-hard in general (p. 4). The
  equality gives a simpler algorithm for one special case of GW, not a
  global solver.
