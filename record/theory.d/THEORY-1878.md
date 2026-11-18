---
number: 1878
status: Proposed
formerly:
- THEORY-tmp81mlq
promote_when: >-
  Theorem 1 checked from its proof, and an independent run, or the
  released code, showing probe decoders recovering more forget-set
  content from hidden states than the output leaks, after at least one of
  the six unlearning methods, on at least one of TOFU, MUSE-News or
  WMDP-Bio.
title: 'On Reisizadeh and colleagues, output-level unlearning can leave forget-set content in a language model''s hidden states: in a Gaussian model the output''s information about a sensitive variable and the representation''s are set by separate quantities, so the output can carry none while the representation carries arbitrarily much, and per-layer probe decoders trained on part of the forget set recover held-out forget content after six standard unlearning methods whose outputs show near-zero leakage'
version: 1
tags:
- representation-learning
- information-theory
date: '2026-11-15'
source:
- LIT-2628
summary: >-
  Reisizadeh, Ruan, Liu & Hong (2026), [LIT-2628](../literature.d/LIT-2628.md), read in
  [NOTE-1960](../notes.d/NOTE-1960.md). The probe is trained on 80% of the forget set, so its
  recovery on the other 20% is what a forget-trained readout generalizes
  to, and the paper does not separate it from relearning. The wording is
  the reader's; adopting it is the owner's call.
---

# THEORY-1878: On Reisizadeh and colleagues, output-level unlearning can leave forget-set content in a language model's hidden states: in a Gaussian model the output's information about a sensitive variable and the representation's are set by separate quantities, so the output can carry none while the representation carries arbitrarily much, and per-layer probe decoders trained on part of the forget set recover held-out forget content after six standard unlearning methods whose outputs show near-zero leakage

## Source

Reisizadeh et al. (2026), [LIT-2628](../literature.d/LIT-2628.md); read in [NOTE-1960](../notes.d/NOTE-1960.md).

## The result

- Theorem 1 (§2.2): the representation's information I(S; R) is bounded
  below by a backbone quantity and the output's I(S; Z | C) above by the
  decoder's sensitivity ε, so "one can simultaneously achieve
  I(S; Z | C) = 0 and I(S; R) ≥ M for any M > 0 by setting ε = 0".
- §3.2: on MUSE-News "all methods appear successful under output-level
  evaluation, with near-zero verbatim leakage; however, probe decoders
  still recover significant verbatim information from hidden states
  across multiple layers"; on TOFU "almost all unlearning methods exhibit
  more sensitive information leakage under ES metric in their hidden
  states than at the output level".

## What it does not show

- That the recovered content was never relearned: the probe is trained on
  forget-set answers.
- Anything beyond the Gaussian model for the theorem, or beyond 1B–7B
  models and the three benchmarks for the experiments.
- That PARS, the paper's remedy, resists probes other than those it is
  trained against.
