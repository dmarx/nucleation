---
number: 994
status: Active
formerly:
- THEORY-tmpm4ifd
title: 'In Ameisen et al.''s evaluations, the local replacement model of their 18-layer language model, built from a 10-million-feature cross-layer transcoder, responded to small perturbations much as the model did one layer after the intervention and increasingly differently over later layers, more in the size of the effect than its direction and slightly more for larger dictionaries, and over 20 prompts the graph''s influence of one feature on another ranked the effect of ablating the first on the second with a Spearman correlation of 0.72'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1185. One study; the sections that measure
    this (Evaluating Mechanistic Faithfulness and the appendix Validating
    the Replacement Model) were read in full. The title claims no more than
    they measured, on one model, with the authors' qualitative wording kept
    where the figures could not be read (ADR-047 v3). The two figures the
    article gives for one-layer agreement disagree, and the title uses
    neither.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1552
summary: >-
  Ameisen et al. (2025), [LIT-1552](../literature.d/LIT-1552.md), read in [NOTE-1185](../notes.d/NOTE-1185.md). It is the
  method's own measurement of where a circuit read off its stand-in stops
  being the model's: close for a layer, diverging with depth. It does not
  say how faithful the circuits of any case study are, which were chosen
  and validated separately, and it is measured on 18L, not on Claude 3.5
  Haiku, where the companion's case studies were run.
---
# THEORY-994: In Ameisen et al.'s evaluations, the local replacement model of their 18-layer language model, built from a 10-million-feature cross-layer transcoder, responded to small perturbations much as the model did one layer after the intervention and increasingly differently over later layers, more in the size of the effect than its direction and slightly more for larger dictionaries, and over 20 prompts the graph's influence of one feature on another ranked the effect of ablating the first on the second with a Spearman correlation of 0.72

## Source

Ameisen et al. (2025), *Circuit Tracing*, [LIT-1552](../literature.d/LIT-1552.md), read in
[NOTE-1185](../notes.d/NOTE-1185.md): "Evaluating Mechanistic Faithfulness" and the appendix
"Validating the Replacement Model" (node-to-logit influence,
feature-to-feature influence, faithfulness of the local replacement
model).

## What was actually shown

**Feature-to-feature influence.** On 20 prompts, every feature in each
graph was ablated by constrained patching over layers [i, i + 2], i its
encoder layer, and the change in each downstream feature's activation was
recorded, normalized by its original activation, in absolute value.
Against the graph's (unsigned) influence of source on target: Spearman
0.72. Few pairs had large influence and no effect, or small influence and
a large effect. The section does not say which model or dictionary these
20 prompts were run on; its scatter plots are of examples "from the
paper".

**Node-to-logit influence.** On 20 prompts, ablating each feature and
measuring the KL divergence of the output: log-log correlation with the
node's indirect logit influence was higher than with its direct logit edge,
and both higher than with its activation.

**Whole-model faithfulness.** At single token positions, the local
replacement model (error terms added back, attention frozen in both
models) and the model were given the same perturbation: along a feature's
encoder, along a random direction of the same size, or by raising an
upstream feature's activation by 0.1 and copying the resulting residual
into the model at an intervention layer. The net change at each later
layer was compared by cosine similarity and normalized MSE. The authors'
findings: agreement is "reasonably similar … one layer after the
intervention"; "perturbation discrepancies compound significantly over
layers"; the direction degrades gradually and "largely consistent[ly]
across CLT sizes, with signs of faithfulness worsening slightly as
dictionary size increases"; the magnitude degrades "catastrophically",
worse for larger dictionaries. Per-layer transcoders were broadly similar
in cosine, lower in normalized MSE one layer after, and compounded
slightly faster.

**The one-layer figure.** The Evaluations section gives "~0.8 cosine
similarity, ~0.4 normalized mean squared error"; the appendix gives the
10M dictionary's cosine one layer after as "around 60–80%". The record
takes the appendix's range as the measurement and states neither number in
the title.

**What could have come out otherwise.** Agreement could have held over many
layers, as it would if the replacement computed as the model does; or
influence could have failed to predict ablation effects.

## What this does not say

- **Not about Claude 3.5 Haiku.** The faithfulness study is on 18L. The
  companion's circuits are on Haiku, with a 30M CLT whose reconstruction
  error is about twice 18L's.
- **Not about the case studies' circuits.** Those are validated by
  perturbing chosen supernodes at the most effective layer, which the
  authors call coarse; they suggest supernodes may "denoise" errors and
  that cruxy features are perturbed where their output is strong.
- **Not a test of independent validity for direct effects.** Part of any
  agreement is guaranteed by construction ([THEORY-979](THEORY-979.md)).
- **Not that larger dictionaries are less useful.** Larger CLTs reconstruct
  better and give better graphs on other metrics; this is only their
  perturbation faithfulness.
