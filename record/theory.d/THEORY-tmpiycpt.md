---
status: Active
title: 'On a presheaf of pseudometric spaces, the consistency radius of an assignment, the largest distance between an observation and the restriction of another, is zero exactly for assignments induced by global sections (in metric spaces) and, when the restrictions are K-Lipschitz, bounds the assignment''s sup-distance from every global section below by ε/(1 + K); so fusing data into a consistent state must move it at least that far, and the bound needs no sheaf condition'
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-27'
source:
- LIT-tmpn521a
summary: >-
  Robinson (2017), LIT-tmpn521a, Definition 20 and Propositions 21 and 23,
  read in NOTE-tmpdshmx from arXiv v3; both proofs checked. Active as
  mathematics. It does not say that the nearest global section is unique
  (the paper's Proposition 25 claims so for Banach sheaves and the proof
  does not reach it), that the radius locates a fault, or that a small
  radius means the data are right.
---
<!-- inactive-ok-file: THEORY-tmpy95x7 — Proposed; the localization finding filed beside this one, cited as open -->

# THEORY-tmpiycpt: On a presheaf of pseudometric spaces, the consistency radius of an assignment, the largest distance between an observation and the restriction of another, is zero exactly for assignments induced by global sections (in metric spaces) and, when the restrictions are K-Lipschitz, bounds the assignment's sup-distance from every global section below by ε/(1 + K); so fusing data into a consistent state must move it at least that far, and the bound needs no sheaf condition

## Source

Robinson (2017), LIT-tmpn521a, §4, pp. 22–25 of arXiv 1603.01446v3; read
in NOTE-tmpdshmx.

## What was actually shown

**The setting.** A presheaf S of pseudometric spaces on a topology T over a
set X of entities: a space of observations S(U) for each open U, with
continuous restrictions S(U ⊆ V): S(V) → S(U) that compose (Axioms 1–5,
pp. 8–16). An assignment picks one observation per open set. Assignments
are compared by D(a, b) = sup_{U ∈ T} d_U(a(U), b(U)) (Definition 18, p. 23).
A global section is an element of S(X).

**The radius.** An assignment s is ε-approximate if
d_V(s(V), S(V ⊆ U)s(U)) ≤ ε for all V ⊆ U, and its consistency radius is
the least such ε (Definition 20, p. 24).

**Zero radius is consistency.** Every global section induces a
0-approximate section by restriction; for metric spaces this is a
homeomorphism onto the 0-approximate sections (Proposition 21, p. 24). With
only pseudometrics it is not: Remark 22 gives two global sections and four
0-approximate sections (pp. 24–25).

**The bound.** If the restrictions are K-Lipschitz and a has radius ε, then
D(a, s) ≥ ε/(1 + K) for every global section s (Proposition 23, p. 25). The
proof is the triangle inequality: d_V(a(V), S(V ⊆ U)a(U)) ≤
d_V(a(V), s(V)) + K d_U(s(U), a(U)) ≤ (1 + K)D(a, s), since s(V) is the
restriction of s(U). The printed last line writes d_V for d_U; the
conclusion is unaffected. Data fusion, the search for the global section
nearest an assignment (Problem 19, p. 23), therefore distorts the data by
at least ε/(1 + K): "The consistency radius of the original data places a
lower bound on the amount of distortion incurred by the fusion process"
(p. 3).

None of this uses Axiom 6, the sheaf condition.

## What this does not say

- **That the nearest global section is unique.** The paper's Proposition 25
  (p. 29) claims a unique solution for sheaves of Banach spaces on finite
  topologies; its proof only shows that D is a max-norm metric, under
  which nearest points to a subspace need not be unique. NOTE-tmpdshmx
  gives a two-point counterexample.
- **That the radius locates anything.** It is a single number. In the
  paper's simulation the biased case had a smaller radius than the
  unbiased one; the bias was found from the pattern of the discrepancies
  (THEORY-tmpy95x7).
- **That a small radius means correct data.** Data that agree under wrong
  restriction maps, or that share a common error, have a small radius. The
  radius measures agreement under the given maps, not accuracy.
- **That fusion improves accuracy.** It gives consistency, with a minimum
  cost; whether the consistent state is closer to the truth is an empirical
  question the paper answers once, in simulation.
- **How to weigh different units.** The supremum runs over spaces whose
  distances may be in km, degrees or hours; the result holds for whatever
  pseudometrics are chosen, and the choice decides what the radius means.
