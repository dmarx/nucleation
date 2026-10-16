---
status: Active
title: "In a finite-dimensional probabilistic theory with unrestricted effects and local tomography, if every system can steer each of its own states from a composite with a copy of itself, every irreducible state space is homogeneous and weakly self-dual; steering does not yet give strong self-duality, so it stops short of the Jordan-algebraic and quantum state spaces"
version: 1
tags:
- quantum-foundations
- mathematics
date: '2026-10-16'
source:
- LIT-081
summary: >-
  Barnum, Gaebler & Wilce (2009), [LIT-081](../literature.d/LIT-081.md), read in full in [NOTE-082](../notes.d/NOTE-082.md). A
  bipartite state steers its marginal iff its map on effects is a strong
  quotient of order intervals (Thm 5.4). With matching dimensions a
  steering state is an order-isomorphism, and a cone is homogeneous iff
  every interior state purifies to an isomorphism state (Thm 4.1). Hence
  universal self-steering gives homogeneity and weak self-duality (Prop.
  5.8). The weaker Prop. 5.7 is thinly argued. The C*-algebraic conclusion
  of §6 needs strong self-duality, which the paper assumes rather than
  derives.
---

# THEORY-tmpx4zft: In a finite-dimensional probabilistic theory with unrestricted effects and local tomography, if every system can steer each of its own states from a composite with a copy of itself, every irreducible state space is homogeneous and weakly self-dual; steering does not yet give strong self-duality, so it stops short of the Jordan-algebraic and quantum state spaces

## Source

Barnum, Gaebler & Wilce (2009; *Found. Phys.* 2013), [LIT-081](../literature.d/LIT-081.md), read in full
in [NOTE-082](../notes.d/NOTE-082.md).

## What was actually shown

**Setting.** Finite-dimensional ordered linear spaces with a regular cone
and an order unit (Def. 2.1). Every effect in [0, u_A] is a measurement
outcome (no restriction). Composites lie between the minimal and maximal
tensor products, and local tomography is a working assumption (p. 7).

**Steering as order theory.** A bipartite state ω is a positive map
ω̂ : A* → B. It steers its B-marginal when every ensemble of that marginal
is the image of an observable on A (Def. 5.1). Theorem 5.4: ω steers its
marginal iff ω̂ restricted to [0, u_A] is a strong quotient map onto
[0, ω_B], every chain lifting to a chain. Both directions are proved.

**From steering to geometry.**
- Cor. 5.5: if ω steers an interior marginal and ω̂ is injective, ω̂ is an
  order-isomorphism. When dim A = dim B, the steering states are exactly
  the isomorphism states.
- Thm 4.1: a cone is homogeneous iff every normalised interior state is the
  marginal of an isomorphism state with one fixed ancilla isomorphic to A*.
  Cor. 4.2: for irreducible A, homogeneous and weakly self-dual iff every
  interior state is the marginal of an isomorphism state in A ⊗max A.
- Prop. 5.8: universal self-steering implies every irreducible state space
  is homogeneous and weakly self-dual. With the extra assumption that
  direct summands of a theory's state spaces are in the theory, this
  extends to all state spaces (p. 15).

**What could have come out otherwise.** A non-homogeneous cone could have
admitted self-steering states for every interior state. The proof rules it
out: matching dimensions force the steering map to be bijective.

## What this does not say

- **That steering forces quantum theory.** The paper's §6 argues that
  self-steering plus strong self-duality, local tomography and a qubit would
  give finite-dimensional C*-algebraic quantum theory, via Koecher–Vinberg
  and Hanche-Olsen. Strong self-duality is a hypothesis there ("If one could
  motivate the stronger assumption", p. 16), and the operational match to
  Hanche-Olsen's conditions is deferred to work "elsewhere" ([NOTE-082](../notes.d/NOTE-082.md), C7,
  weak). The weak-to-strong gap is the paper's own stated limitation.
- **That uniform universal steering already gives homogeneity.** Prop. 5.7
  claims it in one line. Cor. 5.5 covers only an injective steering map, and
  a steering system of larger dimension need not give one ([NOTE-082](../notes.d/NOTE-082.md),
  corrections). Only the self-steering case, Prop. 5.8, is secured.
- **That including all steering states yields a weakly self-dual
  composite.** For two qubits the steering product equals the maximal tensor
  product, which is not weakly self-dual (Fact B.3).
- **Anything about ψ-ontology.** [NOTE-082](../notes.d/NOTE-082.md) records that the paper has no
  ontological-model content; its link to PBR is only a shared ancestor in
  Schrödinger's 1935–36 papers.
- **Real-Hilbert-space quantum theory.** It violates local tomography and
  so falls outside the framework (fn. 5).

## Connections

- The record's general-probabilistic-theory vocabulary is [LIT-073](../literature.d/LIT-073.md), whose
  "steering" is a different, channel notion ([NOTE-082](../notes.d/NOTE-082.md)). The GPT structure
  theorem for noncontextuality is [THEORY-016](THEORY-016.md).
- PBR ([THEORY-tmppgcbt](THEORY-tmppgcbt.md)) shares the Schrödinger lineage and nothing
  technical.
