---
number: 2143
status: Proposed
formerly:
- THEORY-tmprwljl
promote_when: >-
  Theorems 13(ii) and 24 rederived from the paper's definitions; Example
  16 checked to reach the kernel while a coordinate diverges; and a
  numerical run of ẋ = −Lx + b on a small digraph with a globally
  reachable node and vᵀb = 0 converging to L†b + (vᵀx₀)1 from several
  starts.
title: 'Jafarpour, Cisneros-Velarde and Bullo show that a continuous-time system contracting in a seminorm converges to a translate of the seminorm''s kernel without fixing where on it each trajectory ends, and may diverge along it; that one also weakly contracting, with a kernel of equilibria, converges to a single equilibrium; and that in affine averaging that equilibrium is fixed by a conserved linear functional, not by the seminorm'
version: 1
tags:
- control-theory
- mathematics
- network-science
date: '2026-11-21'
source:
- LIT-2945
summary: >-
  The reading the record needed for [CLAIM-772](../claims.d/CLAIM-772.md)'s appeal to
  semicontraction. Semicontraction is the forgetting half of the record's
  picture only: it contracts what lies off the kernel. The keeping half
  comes from an exact invariant (vᵀx, as πF in [THEORY-960](THEORY-960.md)). Proposed until
  its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2043 THEORY-2044 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-772 THEORY-2142 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2143: Jafarpour, Cisneros-Velarde and Bullo show that a continuous-time system contracting in a seminorm converges to a translate of the seminorm's kernel without fixing where on it each trajectory ends, and may diverge along it; that one also weakly contracting, with a kernel of equilibria, converges to a single equilibrium; and that in affine averaging that equilibrium is fixed by a conserved linear functional, not by the seminorm

## Source

Jafarpour, Cisneros-Velarde and Bullo, [LIT-2945](../literature.d/LIT-2945.md), read in [NOTE-2229](../notes.d/NOTE-2229.md) from arXiv 2005.09774v8 (4 Oct 2020; the technical report, with Appendices D–F beyond the IEEE TAC version).

## What was actually shown

Definitions 12 and 17 and Theorems 13, 24 and 26–30 as quoted in the NOTE. Semi-contraction: µ_|||·|||(Df) ≤ −c gives exponential convergence to x∗ + Ker|||·||| (Theorem 13(ii)), with trajectories free to diverge along the kernel (Example 16). Weak contraction (µ(Df) ≤ 0) plus semi-contraction, with the kernel made of equilibria, gives convergence to an equilibrium (Theorem 24). In ẋ = −Lx + b, vᵀb = 0, the limit is L†b + (vᵀx₀)1, fixed by the invariant vᵀx (Theorem 26).

## What this does not say

Nothing about discrete time, Markov chains, noise or approximate conservation. It does not say what a semi-contracting system keeps of its start: that comes, in its examples, from an exact conserved functional.

## Connections

[THEORY-960](THEORY-960.md) (DeGroot: the same invariant, πF, in discrete time); [THEORY-2044](THEORY-2044.md) and [THEORY-2043](THEORY-2043.md) (partial and full contraction); [THEORY-2142](THEORY-2142.md) (De Pasquale and colleagues, the discrete-time sibling); [CLAIM-481](../claims.d/CLAIM-481.md) (Laplacian flow, kernel as exact compatibility).
