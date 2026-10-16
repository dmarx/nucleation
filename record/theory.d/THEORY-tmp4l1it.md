---
status: Active
title: "When each agent's feasible actions depend on the others' actions, an equilibrium exists if every action set is a contractible polyhedron, every constraint correspondence has a closed graph with non-empty compact values, payoffs and the maximum-value functions are continuous, and every best-response set is contractible; convexity is not needed"
version: 1
tags:
- mathematics
- game-theory
date: '2026-10-16'
source:
- LIT-067
summary: >-
  Debreu (1952), [LIT-067](../literature.d/LIT-067.md), read in full in [NOTE-037](../notes.d/NOTE-037.md). The theorem (p. 888) is
  proved by applying the Eilenberg–Montgomery/Begle fixed-point theorem to
  the product of best-response correspondences. A Remark reduces the
  continuity of the value function to a compact graph plus continuity
  (lower hemicontinuity) of the constraint. It is existence only, in
  finite dimensions with finitely many agents and real-valued payoffs.
  That it contains Nash's theorem is asserted; the reduction is routine but
  not in the paper.
---

# THEORY-tmp4l1it: When each agent's feasible actions depend on the others' actions, an equilibrium exists if every action set is a contractible polyhedron, every constraint correspondence has a closed graph with non-empty compact values, payoffs and the maximum-value functions are continuous, and every best-response set is contractible; convexity is not needed

## Source

Debreu (1952), "A Social Equilibrium Existence Theorem", *PNAS*
38(10):886–893, [LIT-067](../literature.d/LIT-067.md), read in full in [NOTE-037](../notes.d/NOTE-037.md) from an archival scan,
with the theorem, lemma, proof and Remark checked against page images.

## What was actually shown

**The setting.** ν agents. Agent ι chooses a_ι from A_ι(ā_ι), a subset of its
action set 𝔄_ι that depends on the others' actions ā_ι, and maximises f_ι.
An equilibrium is a profile in which each a*_ι is feasible given ā*_ι and
maximises f_ι there (Definition, p. 888). This is now called an abstract
economy or generalized game.

**The theorem (p. 888).** An equilibrium exists if, for every ι:
- 𝔄_ι ⊂ ℝ^{n_ι} is a contractible polyhedron;
- A_ι has non-empty compact values and a closed graph G_ι;
- f_ι is continuous on G_ι into the extended reals;
- the value function φ_ι(ā_ι) = max f_ι over A_ι(ā_ι) is continuous;
- each best-response set M_ā_ι is contractible.

**The proof (p. 889).** The product of the 𝔄_ι is a contractible
polyhedron. The map sending a profile to the product of best-response sets
has contractible values and a closed graph. A Lemma, a case of
Eilenberg–Montgomery (1946) or Begle (1950), gives such a map a fixed
point, and a fixed point is an equilibrium.

**The Remark (p. 889).** If G_ι is compact, A_ι is continuous in Debreu's
sense (lower hemicontinuous, in modern terms) and f_ι is continuous, then
φ_ι is continuous. Debreu flags the continuity of φ_ι as "a joint
requirement … not well adapted to applications", which the Remark answers.

**The saddle-point Corollary (§3).** With contractible argmin and argmax
sets, a continuous f on a product of contractible polyhedra has a saddle
point. This contains the theorems of Kakutani and of von Neumann, since
convex sets are contractible.

**What could have come out otherwise.** Existence could have needed convex
best-response sets, as in Kakutani and Nash. It needs only that they be
topologically trivial: "The convexity assumptions were, however,
irrelevant" (§4, p. 892).

## What this does not say

- **Uniqueness, stability or a way to compute an equilibrium.** The proof is
  a fixed-point argument and gives no algorithm or rate.
- **That the theorem is shown to contain Nash's.** The introduction asserts
  it, and §4 only restates Nash's theorem. The reduction (constant
  constraint equal to a mixed-strategy simplex, convex best responses, the
  Remark for continuity) is routine but left to the reader ([NOTE-037](../notes.d/NOTE-037.md), C4).
- **That the hypotheses are easy to check.** Contractibility of best-response
  sets is hard to verify outside convex or quasi-concave settings.
- **That it covers infinite dimensions, infinitely many agents or
  incomplete preferences.** Payoffs are real-valued, so preferences are
  complete orderings. Later work weakens these; it is not assessed here.
- **That every agent is a contractible polyhedron.** The conditions are on
  action sets and best-response sets, not on agents.

## Connections

- The record's other game-theory accounts concern evolutionary and repeated
  games. This is the existence theorem under Arrow and Debreu's competitive
  equilibrium.
