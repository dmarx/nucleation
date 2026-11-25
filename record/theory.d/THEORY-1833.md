---
number: 1833
status: Proposed
formerly:
- THEORY-tmpu5f7u
promote_when: >-
  A reading or reproduction that checks the proofs of Theorems 3.4, 3.7,
  4.1 and 5.3 under the stated assumptions. That is: the existence of the
  C¹ state-to-latent map for κ > 2L_f; its Lipschitz injectivity with
  constant of order κ^ℓ under differential observability and the
  filter-rank condition; the exponential error bound with the exact
  inverse; and discrete tunability for a small step. It does not need the
  empirical claim that trained GRUs become contracting, which the title
  does not assert.
title: 'Contracting recurrent estimators are KKL observers'
statement: >-
  On Andrieu, Bernard, Brivadis, Praly and Wolf, a recurrent estimator ż =
  κg(z, o) whose latent vector field is contracting is a nonlinear KKL
  observer: if the observed system is differentially observable of order ℓ
  and the latent dynamics meet a generic filter-rank condition with
  dimension at least p(ℓ+1), then for a large enough gain the true state
  maps injectively into the latent space, and decoding gives an error
  bounded by a constant times κ^ℓ e^{−κt}, made small after any time at the
  price of a decoder growing like (κ^ℓ/ε)^m and a noise floor growing like
  κ^ℓ
version: 1
tags:
- control-theory
- learning-theory
- mathematics
date: '2026-11-15'
source:
- LIT-2553
summary: >-
  Andrieu, Bernard, Brivadis, Praly & Wolf (2026), [LIT-2553](../literature.d/LIT-2553.md), read in
  [NOTE-1907](../notes.d/NOTE-1907.md). The results are theorems whose proofs were skimmed, not
  verified, here. The sharp edges: existence results only, with no
  training guarantee; thresholds and constants not explicit; a decoder
  bound exponential in latent dimension; and experiments run at κ = 1,
  outside the theorems' large-gain regime.
---

# THEORY-1833: Contracting recurrent estimators are KKL observers

## Source

Andrieu et al. (2026), [LIT-2553](../literature.d/LIT-2553.md), read in [NOTE-1907](../notes.d/NOTE-1907.md) from arXiv v1.

## What was actually shown

Proofs, in the appendices, of Thms 3.4, 3.7, 4.1, 4.2 and 5.3 and of
Prop. 4.3, not checked here. Also a genericity proof of the filter rank
for single-layer analytic RNNs (Prop. K.1).

Empirically:

- a contracting GRU outperforms a vanilla GRU on robot odometry
  correction (5 runs);
- a trained vanilla GRU forgets its initial state on that task (one
  figure);
- on a simulated oscillator, error falls with gain up to κ ≈ 2 and then
  rises.

## What this does not say

- **That training finds an observer.** The results are existence
  results.
- **That trained sequence models become contracting in general.** That
  is the authors' suggestion from one task.
- **That a large gain helps in practice.** In the simulation, error
  grows past κ ≈ 2, which the authors attribute to decoder cost.
