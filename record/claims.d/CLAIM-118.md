---
number: 118
status: Proposed
formerly:
- CLAIM-tmpxrgp3
title: 'Context and interpreter are separate sources of interpretive change: in-context conditioning changes the effective decoding context, adaptation changes the decoder, and improving the signal differs from improving the interpreter'
version: 1
role: thesis
defeated_if: >-
  Changes of interpretation produced by in-context conditioning and by
  adaptation of the interpreter are behaviourally indistinguishable:
  equally persistent, equally transferable, and predicted by the same
  model.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
summary: >-
  A43's first point about the U17 proposal, developed at A44–A45 into
  three sources of change (evidence, transient computation, parameters).
  The manuscript §5 keeps it in two sentences.
supports:
- CLAIM-074
---
<!-- inactive-ok-file: THEORY-169 — Proposed; attention as an inner learner, cited as evidence on one side, not as settled -->
<!-- inactive-ok-file: CLAIM-074 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-118: Context and interpreter are separate sources of interpretive change: in-context conditioning changes the effective decoding context, adaptation changes the decoder, and improving the signal differs from improving the interpreter

## The claim

A43: the model "lets us **separate changes in communicative context from changes
in the underlying interpretive system**". A44 §4 gave two axes, context c and
interpreter parameters θ′_c = A(θ, c). A45 §7 named "**three sources of
apparent interpretive change**: changes in evidence, changes in transient
computation, and changes in the interpreter's parameters", with the interpreter
state s_t = (c_t, h_t, θ_t).

Manuscript §5: "In-context learning changes the effective decoding context
without necessarily changing model weights. Test-time training or learned
fast-state adaptation modifies the decoder itself. We thus distinguish
improving the signal from improving the interpreter."

## What it does not say

A44 §3B: "One should not identify this with literal weight updating in an
ordinary transformer", and "TTT terminology needs care". The consequence for
fidelity ([CLAIM-074](CLAIM-074.md)) is not in the manuscript.

## What the in-context-learning readings say

The evidence is mixed:

- **Against, at the level of the layer.** In linear attention, conditioning
  on a context is one gradient step of an inner learner (Sun et al.,
  [LIT-801](../literature.d/LIT-801.md); von Oswald et al., [LIT-792](../literature.d/LIT-792.md); [THEORY-169](../theory.d/THEORY-169.md)). So in
  that class of system, context and interpreter are the same computation.
- **For, at the level of the whole model.** Akyürek et al. ([LIT-796](../literature.d/LIT-796.md))
  hold the demonstrations fixed and also update the weights on them, and
  that beats conditioning alone (BIG-Bench Hard 50.5% to 57.8%). The two
  are behaviourally distinguishable.
