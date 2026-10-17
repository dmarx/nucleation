---
number: 710
status: Active
formerly:
- THEORY-tmpkovi2
title: "In a finite causal Bayesian network, a set of nodes is causally independent of another, imposing a third, for every choice of mechanisms exactly when every directed path between them passes through the third; information flow, conditional mutual information computed from interventional instead of observational distributions, vanishes under causal independence, and it can differ from transfer entropy and conditional mutual information in either direction"
version: 1
tags:
- causality
- information-theory
date: '2026-10-17'
source:
- LIT-1174
summary: >-
  Ay & Polani (2008), [LIT-1174](../literature.d/LIT-1174.md), read in full in [NOTE-946](../notes.d/NOTE-946.md) from the
  2006 preprint. Theorem 2 and Prop. 3 are proved; Examples 3–6 were
  recomputed. Example 6's one bit holds at k = 1 and fails for k ≥ 2 as
  stated. The measure needs the mechanisms, and estimation and
  identification are not addressed.
---

# THEORY-710: In a finite causal Bayesian network, a set of nodes is causally independent of another, imposing a third, for every choice of mechanisms exactly when every directed path between them passes through the third; information flow, conditional mutual information computed from interventional instead of observational distributions, vanishes under causal independence, and it can differ from transfer entropy and conditional mutual information in either direction

## Source

Ay & Polani (2008), "Information Flows in Causal Networks", *Advances in
Complex Systems* 11(1): 17–41, [LIT-1174](../literature.d/LIT-1174.md), read in full in
[NOTE-946](../notes.d/NOTE-946.md) from the authors' preprint of 12 May 2006. The journal version
was not compared.

## What was actually shown

**Setting.** A DAG with finite state sets and known mechanisms
p_v(x_v | x_pa(v)). Interventions by truncated factorization.

**Causal independence (Eq. 4) and Theorem 2.** X_B ⫫ X_A | X̂_S if setting
x_A after x_S leaves X_B's post-interventional distribution unchanged. For
every model on the DAG, this holds iff B is ud-separated from A by S:
every directed path from A to B meets S. d-separation implies
ud-separation (Prop. 1).

**Information flow (§5, Prop. 3).** I(X_A → X_B | X̂_S) is the conditional
mutual information formula with interventional conditionals, averaged
over the observational p(x_S). It is zero under causal independence, and
only then if every x_S has positive probability. Positive flow implies an
unblocked directed path (Corollary 2).

**Divergence from correlational measures (Examples 3–6).**
- Diamond, Z = X ⊕ Y: I(X:Y) = 1 but I(X → Y) = 0; I(W:Z | Y) = 0 but
  I(W → Z | Ŷ) = 1.
- Same joint distribution, two mechanisms: I(X → Z | Ŷ) = 1 or ≈ 0.311,
  while I(X:Z | Y) = 0 in both.
- Two chains copying each other against two independent inverters,
  observationally identical: transfer entropy zero in both, flow one bit
  against zero at k = 1.

The reading recomputed every value. For Example 6 at k ≥ 2, imposing the
whole past X_[1,k] gives zero flow in the copying case too, because it
fixes Y_k = x_{k−1}. Imposing X_k alone restores one bit at every k. The
paper does not state k.

What could have come out otherwise: Theorem 2's "if" direction could have
failed for some DAG, with an unblocked directed path but no model showing
dependence. The copying construction shows one always exists.

## What this does not say

- **How to compute it from data.** It needs the mechanisms. Identification
  from observational data is [THEORY-704](THEORY-704.md)'s kind of result, not this.
- **That transfer entropy is always wrong about flow.** The two formulas
  coincide term by term when conditioning on the pasts equals setting
  them, for every value, and the observational distribution has full
  support. That is the record's reading of the definitions
  ([NOTE-946](../notes.d/NOTE-946.md)).
- **Anything outside small deterministic examples.** Determinism is where
  observational measures are degenerate.
- **That flow is additive like matter flow.** Imposing a node can raise it
  (diamond) or lower it (channel splitting).

## Connections

- [THEORY-704](THEORY-704.md): the time-series identification of interventional
  effects. Together they say what an interventional information flow is
  and when observational data can deliver one. My connection.
- [CLAIM-333](../claims.d/CLAIM-333.md) and Example 6 show the same gap from opposite sides:
  zero transfer entropy with a real effect.
- [THEORY-711](THEORY-711.md) (directed information) and [THEORY-641](THEORY-641.md) (transfer entropy
  as a likelihood ratio) are observational measures.
- [TERM-058](../terms.d/TERM-058.md), [TERM-057](../terms.d/TERM-057.md).
