---
status: Proposed
promote_when: >-
  A second reading of Kevei's published note (Electronic Communications in
  Probability 21, 2016), or of Goldie (1991), confirms what the title
  says: that the stationary solution of X = AX + B satisfies
  P{X > x} ∼ c+ x^(−κ) and P{X < −x} ∼ c− x^(−κ) with c+ + c− > 0 under
  EA^κ = 1, EA^κ log⁺A < ∞, nonarithmetic log A, E|B|^κ < ∞ and
  non-degeneracy; that EA^κ = 1 with A ≢ 1 forces E log A < 0; and that
  the max equation X = AX ∨ B has P{X > x} ∼ c x^(−κ) under the same
  conditions, with c > 0 if and only if P{B > 0} > 0.
title: "Kevei restates the Kesten–Grincevičius–Goldie theorem: the stationary solution of X = AX + B has a two-sided Pareto-like tail with index κ solving EA^κ = 1, given EA^κ log⁺A < ∞, a nonarithmetic log A, E|B|^κ < ∞ and non-degeneracy, a condition that forces E log A < 0; and, after Goldie, the max equation X = AX ∨ B has the same tail index"
version: 1
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-22'
source:
- LIT-tmpk12vu
summary: >-
  Kevei (2016), LIT-tmpk12vu, skimmed in NOTE-tmpv02cb as a stand-in for
  Kesten (1973), LIT-3005. Its introduction states the one-dimensional
  theorem with Kesten's hypotheses, its two-sided tail (c+ + c− > 0, so a
  tail may sit on one side only), the fact that EA^κ = 1 forces
  log-contraction, Grey's result that with EA^κ < 1 a regularly varying
  tail can come from B alone, and Goldie's Theorem 5.2 for the max form.
  It is the record's ground for CLAIM-824's Kesten half, at second hand.
  Proposed until the reading is confirmed.
---
<!-- inactive-ok-file: LIT-3005 — Unfetched; the original this reading stands in for -->
<!-- inactive-ok-file: LIT-tmpn76uh CLAIM-824 — Deferred or Proposed; Goldie, registered from this reading, and the claim it grounds -->

# THEORY-tmpsmrhx: Kevei restates the Kesten–Grincevičius–Goldie theorem: the stationary solution of X = AX + B has a two-sided Pareto-like tail with index κ solving EA^κ = 1, given EA^κ log⁺A < ∞, a nonarithmetic log A, E|B|^κ < ∞ and non-degeneracy, a condition that forces E log A < 0; and, after Goldie, the max equation X = AX ∨ B has the same tail index

## Source

Kevei (2016), "A note on the Kesten–Grincevičius–Goldie theorem",
Electronic Communications in Probability 21, LIT-tmpk12vu, skimmed from
the arXiv v2 in NOTE-tmpv02cb (§1 in full; proofs skipped).

## The account

For X =d AX + B with (A, B) independent of X, A ≥ 0, A ≢ 1 and
P{Ax + B = x} < 1 for every x: if EA^κ = 1, EA^κ log⁺A < ∞, log A given
A ≠ 0 is nonarithmetic and E|B|^κ < ∞ for some κ > 0, then
P{X > x} ∼ c+ x^(−κ) and P{X < −x} ∼ c− x^(−κ), "for some c+, c− ≥ 0,
c+ + c− > 0" (p. 1). Kesten proved it "in d dimension"; Goldie re-proved
the one-dimensional case. EA^κ = 1 with A ≢ 1 forces E log A < 0 (p. 6);
P{A > 1} > 0 is what makes the tail polynomial (p. 2). For the max form
X =d AX ∨ B, "Theorem 5.2 in [18] [Goldie] states that if (2) holds,
then there is a unique solution X to (12), and P{X > x} ∼ cx−κ with some
c ≥ 0, and c > 0 if and only if P{B > 0} > 0" (p. 4).

## What would have come out otherwise

The tail could have been lognormal-like or exponential; it is exponential
when A ≤ 1 a.s. (Goldie and Grübel, p. 2), and carries a slowly varying
correction when EA^κ log⁺A = ∞ (Kevei's own theorems).

## What it does not license

- That a Pareto stationary tail shows the A-driven mechanism: by Grey
  (p. 2), with EA^κ < 1 the tail is regularly varying "if and only if
  the tail of B is".
- Kesten's own hypotheses in d dimensions, which this note does not give.
