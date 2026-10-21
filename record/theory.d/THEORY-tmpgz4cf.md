---
status: Active
title: 'Information usable by a predictor restricted to a family V can be created by computing on the data, so the data-processing inequality fails for V-information: with Z the exclusive-or of two fair independent bits, linear and one-coordinate families extract nothing about Z from the pair and all of it from their exclusive-or; V-information computed from any function of the source is bounded by the source''s Shannon information when the family''s input-free predictions can match the marginal of the target, and can exceed it otherwise'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpvnsxo. The definitions and the monotonicity
    used are Xu et al.'s (Definitions 1–3, Proposition 2). The paper
    argues that computation creates V-information from informal examples;
    the exact XOR instance, the bound by Shannon information, its
    condition and the counterexample are the record's, re-derived below
    and checked numerically, which meets the condition for Active under
    ADR-047 v2.
tags:
- information-theory
- learning-theory
date: '2026-10-21'
source:
- LIT-tmp07k7g
summary: >-
  Xu, Zhao, Song, Stewart and Ermon (2020), [LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), read in
  [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md), define V-information and say it "can be created through
  computation". The record's worked case is [CLAIM-199](../claims.d/CLAIM-199.md)'s XOR under the
  paper's linear families, and its addition is the ceiling: usable
  information never exceeds the source's Shannon information when V can
  predict the marginal of Y without input, and can exceed it when V
  cannot. It says nothing about which family a real observer has.
supports:
- CLAIM-199
---
<!-- inactive-ok-file: CLAIM-199 CLAIM-081 — Proposed; the claims this account bears on, cited as open -->

# THEORY-tmpgz4cf: Information usable by a predictor restricted to a family V can be created by computing on the data, so the data-processing inequality fails for V-information: with Z the exclusive-or of two fair independent bits, linear and one-coordinate families extract nothing about Z from the pair and all of it from their exclusive-or; V-information computed from any function of the source is bounded by the source's Shannon information when the family's input-free predictions can match the marginal of the target, and can exceed it otherwise

## Source

Xu, Zhao, Song, Stewart and Ermon (2020), ICLR 2020, [LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), read in
full in [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md). Definitions 1–3, Proposition 1 (items 1 and 5) and
Proposition 2 are the paper's. The paper's claim that computation creates
V-information is §3.2, argued from decryption and from learned features,
with no worked case. The derivations below are the record's.

## What was actually shown

A predictive family V is a set of maps f from X ∪ {∅} to distributions on
Y, closed under optional ignorance: for each f ∈ V and each P that f
outputs, V contains the constant map to P. H_V(Y | X) = inf_{f∈V}
E[−log f[X](Y)], H_V(Y) is the same with ∅ for X, and I_V(X → Y) =
H_V(Y) − H_V(Y | X). With V = Ω, all maps, these are Shannon's quantities
(Proposition 1.1). If V ⊆ U then H_V ≥ H_U (Proposition 2.1).

**Creation by computation.** Let X₁, X₂ be fair independent bits,
Z = X₁ ⊕ X₂, X = (X₁, X₂) and t(X) = X₁ ⊕ X₂. Shannon:
I(X; Z) = I(t(X); Z) = H(Z) = log 2.

- *Linear logistic V*: f[x] = Bernoulli(σ(wᵀx + b)), f[∅] =
  Bernoulli(σ(b)). Optional ignorance holds (w = 0). H_V(Z) = log 2 at
  b = 0. From X: the loss is convex in (w, b), and its gradient at 0 is
  E[(½ − Z)Xⱼ] = 0 and E[½ − Z] = 0, since Z is independent of each Xⱼ
  and fair. So 0 is the global minimum, H_V(Z | X) = log 2 and
  I_V(X → Z) = 0. From t(X) = Z: w = 2W, b = −W gives loss
  log(1 + e^(−W)) → 0, so I_V(t(X) → Z) = log 2, the infimum not
  attained. With ‖(w, b)‖ ≤ c, as Theorem 1 needs, I_V(t(X) → Z) was
  0.21, 0.59 and 0.693 nats at c = 1, 5 and 20, rising to log 2.
- *Linear-Gaussian V* (Proposition 1.5): I_V = R² · Var(Z). Cov(Xⱼ, Z) = 0,
  so R² = 0 from X. R² = 1 from t(X), so I_V(t(X) → Z) = Var(Z) = 1/4.
- *One-coordinate V* ([CLAIM-199](../claims.d/CLAIM-199.md)'s receiver): each f reads one coordinate
  and outputs any distribution on {0, 1} for each value. Each coordinate
  of X is independent of Z, so I_V(X → Z) = 0, and I_V(t(X) → Z) = log 2.

In all three, I_V(t(X) → Z) > I_V(X → Z) although t(X) is a function of X.
That is the failure of the data-processing inequality, exactly.

**The ceiling, and its condition.** Suppose V's input-free predictions
include the marginal P_Y, so H_V(Y) = H(Y). (The logistic and
one-coordinate families above do, and so does any family that can output
every distribution on a finite Y.) Then for any function t,

I_V(t(X) → Y) = H(Y) − H_V(Y | t(X)) ≤ H(Y) − H(Y | t(X)) = I(t(X); Y)
≤ I(X; Y),

by Proposition 2.1 with V ⊆ Ω and then the data-processing inequality.
Computation can raise usable information up to the source's Shannon
information and no further. In general,
I_V(t(X) → Y) ≤ I(X; Y) + [H_V(Y) − H(Y)].

**Without the condition the bound fails.** Let Y be a fair bit, X = Y, and
let V be every map from X ∪ {∅} into {Bernoulli(ε), Bernoulli(1 − ε)}.
V satisfies optional ignorance. H_V(Y) = ½ log(1/ε) + ½ log(1/(1 − ε)) and
H_V(Y | X) = log(1/(1 − ε)), so I_V(X → Y) = ½ log((1 − ε)/ε): 1.10,
2.30 and 3.45 nats at ε = 0.1, 0.01 and 0.001, against I(X; Y) = log 2 =
0.69. V-information exceeds Shannon information because a family that
cannot represent "I don't know" is penalized more without input.

What could have failed: the paper's linear families could have extracted
some information about Z from the pair, as they would for most targets.
Here they extract none, because the target is uncorrelated with every
coordinate.

## What this does not say

- **Not that computation usually helps.** It helps only when it computes
  something the family cannot compute itself, as with the exclusive-or for
  a linear family.
- **Not that usable information can exceed what the source makes possible
  for an ideal receiver, in risk.** In risk terms [CLAIM-199](../claims.d/CLAIM-199.md)'s ceiling holds
  for any family: H_V(Y | t(X)) ≥ H(Y | t(X)) ≥ H(Y | X). Only the
  difference, V-information, can overshoot, and only through H_V(Y).
- **Not which family a real observer, reader or institution has.**
- **Not an order on representations.** For a fixed V there is no
  garbling theorem here, and none in the paper.

## Connections

- **[CLAIM-199](../claims.d/CLAIM-199.md).** This is its XOR example in Xu et al.'s terms, for the
  paper's own linear families as well as the claim's one-coordinate
  receiver. Its ceiling holds in V-information when the receiver's
  input-free predictions include the marginal, as its receiver's do.
- **[TERM-tmp5lqn0](../terms.d/TERM-tmp5lqn0.md).** A22's "legibility need not be monotone in
  informational refinement for bounded observers" is this failure of the
  data-processing inequality, with legibility read as V-information.
- **[CLAIM-225](../claims.d/CLAIM-225.md).** The ideal receiver is V = Ω, the bounded one V ⊊ Ω.
- **[CLAIM-081](../claims.d/CLAIM-081.md) and [CLAIM-270](../claims.d/CLAIM-270.md).** Legibility up and information down at once
  is I_V rising while I falls. The ceiling shows the rise is capped by what
  remains, I(t(X); Y), not by what the source had.
- **[THEORY-176](THEORY-176.md).** A stitching penalty restricts the map class the same
  way, and loses Blackwell's order for the same reason.
- **[CLAIM-304](../claims.d/CLAIM-304.md)** is the opposite direction, computation that destroys usable
  information for efficient families while keeping it in principle.
