---
status: Proposed
title: 'DeVille and Lerman show that a graph fibration between networks of continuous-time systems, a map lifting each incoming edge uniquely, induces a map of dynamical systems in the opposite direction for every modular vector field, so a surjective fibration (the quotient by a balanced relation) embeds the quotient''s dynamics as an invariant synchrony polydiagonal and an injective fibration projects a network onto the subsystem that drives it'
version: 1
source:
- LIT-tmp31ier
tags:
- mathematics
- network-science
date: '2026-11-19'
bears_on:
- QUESTION-tmpex36a
promote_when: >-
  The record checks Theorem 4.3.1 and Lemmas 5.1.1 and 5.2.1 against their
  proofs (pp. 24–28) and confirms that balanced quotients are surjective
  fibrations as defined (Definition 4.1.1)
summary: >-
  From the reading of [LIT-tmp31ier](../literature.d/LIT-tmp31ier.md) in [NOTE-tmpubt2l](../notes.d/NOTE-tmpubt2l.md). DeVille and Lerman
  (2013), arXiv 1303.3907. In a coordinate-free framework of networks of
  control systems on manifolds, they prove that a graph fibration (Boldi
  and Vigna's unique lifting of incoming edges, equivalently input-tree
  isomorphism) induces a map of dynamical systems in the opposite
  direction for every modular vector field. Surjective fibrations, which
  include quotients by balanced relations, embed the quotient's dynamics
  as an invariant synchrony polydiagonal. Injective fibrations project a
  network onto the subsystem that drives it, which they call an
  abstraction. Only this direction is proved, and stability is not
  treated. Here because it is the fibration form of the balanced-partition
  result held as [THEORY-1065](THEORY-1065.md) and [THEORY-1059](THEORY-1059.md), which it generalizes in one
  direction. Read in its NOTE.
---

# THEORY-tmp31d9a: DeVille and Lerman show that a graph fibration between networks of continuous-time systems, a map lifting each incoming edge uniquely, induces a map of dynamical systems in the opposite direction for every modular vector field, so a surjective fibration (the quotient by a balanced relation) embeds the quotient's dynamics as an invariant synchrony polydiagonal and an injective fibration projects a network onto the subsystem that drives it

## The account

A network is a finite directed multigraph with a manifold at each node. A modular dynamical system on it gives each node a control system depending only on its inputs, the same one for nodes whose input networks are isomorphic. For a graph fibration ϕ : G → G′ (Definition 4.1.1), each modular vector field on G′ pulls back to one on G, and the phase-space map Pϕ intertwines the two flows (Theorem 4.3.1). If ϕ is surjective, Pϕ embeds the dynamics of G′ as the polydiagonal where nodes with the same image agree (Lemma 5.1.1). The quotient maps of Golubitsky and Stewart's balanced relations are exactly such surjective fibrations (§1.3). If ϕ is injective, Pϕ projects the dynamics of G′ onto those of the subnetwork G, which drives the rest (Lemma 5.2.1). Every fibration factors as a surjection followed by an injection (§5.3).

## What it does not show

- The converse: that every invariant polydiagonal of all modular fields comes from a fibration (Remark 4.3.3).
- Stability of the embedded or projected dynamics.
- Discrete-time, stochastic or weighted settings, such as trained neural networks.
- How its modular class compares with Golubitsky and Stewart's admissible class. In particular it does not reconcile its isomorphism of invariant fields under surjective fibrations (Corollary 6.2.4) with the 2003 result that quotient dynamics need not lift.

## Note of 2026-11-19: Wang and Slotine, read
<!-- inactive-ok-file: THEORY-tmprqrdn — Proposed; cited from the readings of 2026-11-19 -->

A complement (THEORY-tmprqrdn; NOTE-tmp9eyoy): fibrations give invariant synchrony patterns; Wang and Slotine give conditions under which synchrony is also globally attracting, for identical units with symmetric positive-definite diffusive coupling (Theorem 6).
