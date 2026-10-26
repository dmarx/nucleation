---
status: Active
title: 'On one prompt, a transformer whose MLPs are replaced by a cross-layer transcoder, with its attention patterns and normalization denominators frozen and each MLP''s reconstruction error added back as a constant, reproduces the model''s activations and outputs exactly and is linear between features, so each active feature''s pre-activation is the sum of its attribution-graph edges and constants; a perturbation that clamps MLP outputs up to the target feature''s encoder layer then confirms a direct edge by construction, and tests only knock-on effects and the output'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpn9fx3, the reading of Ameisen et al. (2025).
    The first part is the article's construction of the local replacement
    model and its attribution graph; the second is its own statement in the
    appendix on steering with cross-layer features. The record re-derived
    both step by step below (ADR-047 v2). The derivation adds one
    qualification the article leaves implicit: the guarantee is exact when
    the normalization denominators are also frozen in the perturbed run.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmpsuo6l
summary: >-
  Ameisen et al. (2025), [LIT-tmpsuo6l](../literature.d/LIT-tmpsuo6l.md), read in [NOTE-tmpn9fx3](../notes.d/NOTE-tmpn9fx3.md): the local
  replacement model, the edge formula and the appendix on steering,
  re-derived here. It is a statement about what an attribution graph is
  exact for, not about the model: exactness holds at the unperturbed point
  only, the error terms are constants with no inputs, and the
  frozen attention patterns are the part of the computation the graph does
  not explain.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 — Proposed; the record's own claim, named, nothing here rests on it -->
# THEORY-tmpbtnf0: On one prompt, a transformer whose MLPs are replaced by a cross-layer transcoder, with its attention patterns and normalization denominators frozen and each MLP's reconstruction error added back as a constant, reproduces the model's activations and outputs exactly and is linear between features, so each active feature's pre-activation is the sum of its attribution-graph edges and constants; a perturbation that clamps MLP outputs up to the target feature's encoder layer then confirms a direct edge by construction, and tests only knock-on effects and the output

## Source

Ameisen et al. (2025), *Circuit Tracing*, Transformer Circuits Thread,
[LIT-tmpsuo6l](../literature.d/LIT-tmpsuo6l.md), read in [NOTE-tmpn9fx3](../notes.d/NOTE-tmpn9fx3.md): "The Local Replacement Model",
"Constructing an Attribution Graph for a Prompt", "Validating Attribution
Graph Hypotheses with Interventions" and the appendix "Nuances of Steering
with Cross-Layer Features". The companion, LIT-tmpjvwet, restates the
second part in its Method Overview.

## What was actually shown

A construction, checked by the record step by step.

**Step 1: exactness.** At each position and layer of prompt p the local
replacement model's MLP output is the CLT output plus the error term e =
MLP(x) − CLT(x), with both evaluated on the model's own activations on p.
So it equals the model's MLP output. Attention patterns and normalization
denominators are copied from the model's forward pass on p. By induction
over layers, every residual-stream state, and so every logit, equals the
model's. The article: "all of the error-corrected replacement model's
activations and logit outputs exactly match those of the underlying
model."

**Step 2: linearity.** With patterns fixed, an attention head's output is a
fixed weighted sum of W_OV applied to normalized source states; with the
denominators fixed, normalization is an affine map. Neither has any other
nonlinearity. The MLPs are gone, replaced by CLT decodings, which are
linear in the feature activations. So the residual state at a feature's
encoder layer is an affine function of the feature activations, the token
embeddings and the error terms, and the feature's pre-activation h_t is
Σ_s a_s w_{s→t} plus embedding, error and bias terms, with w_{s→t} the sum
over linear paths from s's decoders to t's encoder. The only remaining
nonlinearity is each feature's own JumpReLU. (The article writes h_t =
Σ w_{s→t}, omitting the factor a_s it defined two paragraphs earlier as part
of the edge A_{s→t} = a_s w_{s→t}.)

**Step 3: a direct edge is confirmed by construction.** Constrained
patching changes a source feature's activation by δ and clamps the MLP
outputs of the layers in a chosen range to values computed once, at the
outset, from the change. If the range ends at the target's encoder layer
and attention patterns are frozen, the only change reaching the target's
encoder is δ times the source's decodings carried along the same linear
paths that define w_{s→t}. If the denominators are also frozen, the change
in the target's pre-activation is exactly δ w_{s→t}; if they are
recomputed, it is that to first order. The article: direct interactions
are "nearly forced to be confirmed in steering experiments (when we freeze
attention patterns) … and guaranteed when choosing the intervention layer
to be the same as the target feature's encoder layer. Thus, the nontrivial
thing we are testing with perturbation experiments is the validity of the
attribution graph's claims about 'knock-on effects.'"

**What could have come out otherwise.** As derivations, nothing. They set
what an experiment in the article can and cannot show: an effect on a
feature after the intervention layer, or on the output, can disagree with
the graph; a direct effect before it cannot.

## What this does not say

- **Not that the model uses the graph's mechanism.** Exactness holds at
  the unperturbed point. Away from it the replacement and the model can
  respond differently, and the article measures that they do
  ([THEORY-tmpm4ifd](THEORY-tmpm4ifd.md)). Its own analogy: "a Taylor approximation of a function
  f at a point a".
- **Not that the error terms are small.** They are constants with no
  inputs; an attribution graph whose influence runs through them explains
  little, as on the article's obfuscated jailbreak prompt.
- **Nothing about attention.** The patterns are inputs here. Why the model
  attended where it did is outside the graph.
- **Not that a validated case study is validated only trivially.** The case
  studies also report effects on outputs and on later features, which can
  fail. The point is that a reader has to know which kind each reported
  effect is.

## Connections

- **[THEORY-tmp9ii0y](THEORY-tmp9ii0y.md)** is the per-layer form of Step 2, from Dunefsky et al.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The graph is exact for a stand-in at a point, which
  is what a recovered feature set can at most give before the stand-in's
  mechanism is checked against the model's.
