---
number: 1043
status: Proposed
formerly:
- CLAIM-tmp7n00e
title: 'Rescaling changes what fine-tuning learns'
statement: >-
  In Lippl and Lindsey's pretraining and fine-tuning of a diagonal linear
  network, scaling the first layer by c and the auxiliary readout by 1/c
  after pretraining keeps the pretrained function and what readout-only
  training reaches from it, but changes the penalty full fine-tuning
  minimizes, so the rescaled and unrescaled networks learn different
  solutions, and which is better reverses between a main task using a sparse
  subset of the pretrained features and one using all of them
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23: the derivation that run draws
    from Lippl and Lindsey's Corollary 2 and their network's symmetry,
    with the run that checks it.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: that the compensated rescaling
  changes the pretrained function; that readout-only training from P_c
  and P₁ reaches different solutions; that the fine-tuning penalty of
  Corollary 2, applied to P_c, is not the one with |β^aux| replaced by
  c²|β^aux|; or a rerun of CASE-407 in which full fine-tuning from
  P_c and P₁ converges to the same solutions, or in which the ordering of
  c does not reverse between the nested and dense main tasks.
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
grounds:
- THEORY-2305
- CASE-407
bears_on:
- QUESTION-495
summary: >-
  Lippl and Lindsey note of their ReLU networks that the function "is
  invariant to rescaling the hidden weights by α>0 and the readout weights
  by 1/α", which holds as plainly for the diagonal ones, and they rescale
  the weights after pretraining to move fine-tuning between
  regimes. They do not say that the rescaled network, with its readout
  compensated, computes the pretrained function. It does, and readout
  training from it reaches what it reaches from the original; full
  fine-tuning does not, by their own penalty. [CASE-407](../cases.d/CASE-407.md) runs it over
  40 seeds. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2305 CASE-407 CLAIM-1013 CLAIM-1089 — Proposed; the reading and the run this rests on, and the readings of it filed by the lead run of 2026-11-23 -->

# CLAIM-1043: Rescaling changes what fine-tuning learns

## The derivation

Let P₁ be the network after pretraining, β^aux = v₊∘w₊ − v₋∘w₋, and P_c
the network with first layer c·w and auxiliary readout v/c.

1. **Same function.** Each coordinate of β is a product of a readout
   weight and a first-layer weight, so (v/c)∘(c·w) = v∘w: P_c computes
   β^aux exactly.
2. **Same reach and same solution under readout-only training.** With
   the first layer fixed, the network is linear regression on features
   x∘w. P_c's features are c times P₁'s, so each readout u of P₁ has the
   readout u/c of P_c computing the same β, and gradient descent from a
   zero-function start converges in each to the minimum-norm readout, the
   same β. The operational frontier, taken either as the pretrained
   function or as what readout-only training reaches, is the same.
3. **Different penalty under full fine-tuning.** By Lippl and Lindsey's
   Corollary 2 ([THEORY-2305](../theory.d/THEORY-2305.md)), fine-tuning from first-layer weights of
   magnitude √|β^aux_d|, with the readout reset to γ, minimizes Σ_d
   (|β^aux_d| + γ²) q(2β_d / (|β^aux_d| + γ²)). From P_c the first-layer
   magnitude is c√|β^aux_d|, so the same penalty holds with |β^aux_d|
   replaced by c²|β^aux_d|. Smaller c makes the penalty more ℓ1-like over
   the pretrained dimensions; larger c more like a weighted ℓ2 (their
   §4.2-4.4).
4. **The ranking depends on the main task.** An ℓ1-like penalty over the
   pretrained dimensions suits a main task that uses few of them; a
   weighted ℓ2 one suits a task that uses all of them with varied
   coefficients.

## The check

[CASE-407](../cases.d/CASE-407.md), 40 seeds: the function after rescaling agrees to
2·10⁻¹⁶; readout-only training gives the same solution for every c;
under full fine-tuning, c = 0.3 beat c = 2 on the nested task in 29 of 40
seeds (p = 0.006), and c = 2 beat c = 0.3 on the dense task in 40 of 40.

## What it does not say

- Whether P_c and P₁ are two learners or one learner under two
  procedures. That is the dispute between [CLAIM-1013](CLAIM-1013.md) and
  [CLAIM-1089](CLAIM-1089.md).
- Anything about deep networks, where the paper does not say whether its
  rescaling keeps the pretrained function.
- Anything about pretraining of different lengths.
